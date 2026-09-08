"""The passive judges our agentic judge has to beat.

VideoPhy-2's own automatic evaluation, and essentially every judge built on it,
works the way `SinglePassBaseline` does: sample frames uniformly, show them to a
VLM once, demand a 1-5 number. A correlation reported without that reference
point says nothing, so the baseline is built here from the same rubric
(`PC_RUBRIC`), the same frame server and the same cost accounting as the loop.
If it used its own scale or its own sampler, any gap we measured could be an
artefact of either and not of adaptivity.

`CaptionOnlyBaseline` is the other end of the ruler. It never sees the video, so
whatever correlation it reaches is what the caption distribution alone predicts:
generators fail on hard prompts, humans score hard prompts low, and a judge can
inherit that agreement without looking at a single pixel. The margin our judge
holds over this baseline is the part of its skill that is genuinely about video.

Two deliberate design choices:

  - Neither baseline retries. A reply with no usable score is recorded as an
    imputed 3.0 and flagged, because how often a one-pass judge fails to produce
    a number is itself a reported quantity. Re-asking would hide it.
  - Nothing raises. A missing or undecodable file, or a dead endpoint, comes back
    as a result with `error` set and `pc_score=None`, so a 200-video sweep is
    never lost to one bad clip.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pjudge.backends.llm import parse_json
from pjudge.perception.frames import FrameServer
from pjudge.prompts import PC_RUBRIC

# The value filled in when no score can be read at all: the middle of the scale,
# which is also the mode of the human pc distribution, so it is the least
# informative guess rather than an accidental bet.
IMPUTED_SCORE = 3.0

# Used when the model gives a score but no confidence. Imputed scores get 0.0
# instead, so any risk-coverage curve ranks them last -- they carry no signal.
DEFAULT_CONFIDENCE = 0.5

COST_KEYS = ("frames", "prompt_tokens", "completion_tokens", "llm_calls", "cache_hits")


BASELINE_SYS = f"""\
You are a judge of physical plausibility in generated video. You rate how well
what is shown obeys physical commonsense: contact, support, momentum, gravity,
rigidity, volume and count, articulation, fluid behaviour.

Judge physics only. Do not reward or penalise how faithfully the video follows
the prompt it was generated from, and do not judge aesthetics, style or
resolution. Rendering artefacts (flicker, texture swimming, blur) are not
physical violations unless an object's behaviour is actually impossible.

Score on VideoPhy-2's 1-5 physical-commonsense scale:
{PC_RUBRIC}

Always reply with a single JSON object and no prose outside it."""


TASK_SINGLE_PASS = """\
Prompt used to generate the video:
{caption}

You are given {n} frames sampled uniformly across the whole clip
({duration:.2f}s), in temporal order, at these timestamps: {timestamps}

The frames are all you get: there is no second look and no way to request a
closer view. Rate the physical commonsense of the video as a whole.

JSON:
{{"pc_score": 1-5, "confidence": 0.0-1.0, "reason": "one sentence"}}"""


TASK_CAPTION_ONLY = """\
Prompt given to a text-to-video model:
{caption}

You cannot see the video and will not be shown it. Predict the physical
commonsense score a human annotator gave the clip that a current text-to-video
model generated from this prompt. Base it on how demanding the described physics
is for such a model -- multi-body contact, deformation, fluids, fine
articulation and precise timing tend to be rendered badly; slow single-object
motion in a static scene tends to survive.

JSON:
{{"pc_score": 1-5, "confidence": 0.0-1.0, "reason": "one sentence"}}"""


# --------------------------------------------------------------------------
# result
# --------------------------------------------------------------------------


@dataclass
class BaselineResult:
    """One baseline's answer for one video, with what it cost to get it."""

    video_id: str
    pc_score: float | None
    confidence: float
    score_imputed: bool  # True when no parseable score came back
    raw_text: str
    n_frames: int
    cost: dict[str, int] = field(default_factory=lambda: dict.fromkeys(COST_KEYS, 0))
    error: str = ""

    @property
    def fatal(self) -> bool:
        """True when no score was produced at all (missing file, dead endpoint).

        `error` also carries soft notes -- a clamped or imputed score -- so a
        results table that wants to drop only the unscorable rows must test this
        rather than test `error` for emptiness.
        """
        return self.pc_score is None

    def as_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {
            "video_id": self.video_id,
            "pc_score": self.pc_score,
            "confidence": self.confidence,
            "score_imputed": self.score_imputed,
            "raw_text": self.raw_text,
            "n_frames": self.n_frames,
            "error": self.error,
            "fatal": self.fatal,
            "cost": dict(self.cost),
        }
        # Flattened as well: the results table is one row per video with one
        # column per cost component, matching what the agentic judge writes.
        out.update({k: int(self.cost.get(k, 0)) for k in COST_KEYS})
        return out


# --------------------------------------------------------------------------
# reply parsing
# --------------------------------------------------------------------------

# A standalone 1-5, optionally with a decimal part: matches the "2" in
# "I would say 2 out of 5" and the "2.5" in "2.5/5", but not the "1" of "15"
# and not a number glued to a word.
_PROSE_SCORE = re.compile(r"(?<![\w.])([1-5](?:\.\d+)?)(?!\d)")


def _as_number(value: Any) -> float | None:
    """A float from whatever the model put in the field, or None.

    Booleans are rejected on purpose: `float(True)` is 1.0, which would turn
    `{"pc_score": true}` into the harshest possible score.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, str):
        return _score_from_prose(value)
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    return num if num == num and abs(num) != float("inf") else None


def _score_from_prose(text: str) -> float | None:
    """First standalone 1-5 in free text, or None."""
    match = _PROSE_SCORE.search(text)
    return float(match.group(1)) if match else None


def parse_reply(text: str) -> tuple[float, float, bool, str]:
    """Read a score out of a baseline reply.

    Returns `(pc_score, confidence, score_imputed, note)`. Three tiers, in order:
    the JSON object we asked for, then the first standalone 1-5 anywhere in the
    text, then the imputed middle of the scale. The tier used is recorded in
    `note` so the imputation and fallback rates can be counted afterwards rather
    than guessed.
    """
    notes: list[str] = []
    score: float | None = None
    confidence: float | None = None

    try:
        data = parse_json(text)
    except ValueError:
        data = None
    if isinstance(data, dict):
        score = _as_number(data.get("pc_score"))
        if score is None:
            score = _as_number(data.get("score"))
        confidence = _as_number(data.get("confidence"))

    if score is None:
        score = _score_from_prose(text)
        if score is not None:
            notes.append("score read from prose; reply was not usable JSON")

    if score is None:
        return (
            IMPUTED_SCORE,
            0.0,
            True,
            f"no parseable score in reply; imputed {IMPUTED_SCORE}",
        )

    clamped = min(5.0, max(1.0, score))
    if clamped != score:
        notes.append(f"score {score:g} out of range; clamped to {clamped:g}")

    if confidence is None:
        conf = DEFAULT_CONFIDENCE
    else:
        conf = min(1.0, max(0.0, confidence))
        if conf != confidence:
            notes.append(f"confidence {confidence:g} clamped to {conf:g}")

    return clamped, conf, False, "; ".join(notes)


# --------------------------------------------------------------------------
# cost accounting
# --------------------------------------------------------------------------


def _usage_snapshot(client: Any) -> dict[str, int]:
    """The client's lifetime counters right now.

    Duck-typed rather than typed to `LLMClient`: the runner may hand us any
    object with `.ask` and `.usage`, and a client without counters must degrade
    to zero cost instead of failing the video.
    """
    usage = getattr(client, "usage", None)
    fields = ("calls", "cache_hits", "prompt_tokens", "completion_tokens")
    if usage is None:
        return dict.fromkeys(fields, 0)
    out: dict[str, int] = {}
    for name in fields:
        try:
            out[name] = int(getattr(usage, name, 0) or 0)
        except (TypeError, ValueError):
            out[name] = 0
    return out


def _cost_since(client: Any, before: dict[str, int], frames: int) -> dict[str, int]:
    """Cost of this video only, as the delta of the client's counters.

    A worker reuses one client for hundreds of videos, so reporting the client's
    totals would charge every video with the whole run. Deltas are also correct
    when the reply came from the disk cache: the call still counts, and
    `cache_hits` says it was free.
    """
    after = _usage_snapshot(client)
    delta = {k: max(0, after[k] - before.get(k, 0)) for k in after}
    return {
        "frames": int(frames),
        "prompt_tokens": delta["prompt_tokens"],
        "completion_tokens": delta["completion_tokens"],
        "llm_calls": delta["calls"],
        "cache_hits": delta["cache_hits"],
    }


def _video_id_for(video_path: str | Path | None, video_id: str | None) -> str:
    if video_id:
        return video_id
    return Path(video_path).stem if video_path else ""


def _fmt_times(times: list[float]) -> str:
    return ", ".join(f"{t:.2f}s" for t in times)


# --------------------------------------------------------------------------
# baselines
# --------------------------------------------------------------------------


class _PassiveBaseline:
    """Shared machinery: one call, no retry, cost as a delta, never raises.

    Both baselines take `(video_path, caption, video_id)` and return a
    `BaselineResult`, so the runner can hold either behind the same call.
    """

    def __init__(self, client: Any):
        self.client = client

    def _ask(
        self,
        vid: str,
        prompt: str,
        images: list[Any],
        before: dict[str, int],
        frames: int,
        n_frames: int,
    ) -> BaselineResult:
        try:
            resp = self.client.ask(
                prompt, system=BASELINE_SYS, images=images or None, json_mode=True
            )
            text = getattr(resp, "text", "") or ""
        except Exception as exc:  # noqa: BLE001 - endpoint failures are data, not bugs
            return BaselineResult(
                video_id=vid,
                pc_score=None,
                confidence=0.0,
                score_imputed=False,
                raw_text="",
                n_frames=n_frames,
                cost=_cost_since(self.client, before, frames),
                error=f"llm call failed: {type(exc).__name__}: {exc}",
            )

        score, confidence, imputed, note = parse_reply(text)
        return BaselineResult(
            video_id=vid,
            pc_score=score,
            confidence=confidence,
            score_imputed=imputed,
            raw_text=text,
            n_frames=n_frames,
            cost=_cost_since(self.client, before, frames),
            error=note,
        )


class SinglePassBaseline(_PassiveBaseline):
    """Uniformly sampled frames, one forward pass, a forced 1-5 score.

    This is the paradigm VideoPhy/VideoPhy-2 use and the thing we are arguing
    against: the frames are chosen before anything is known about the video, the
    model cannot ask for a closer look at the moment that matters, and it cannot
    decline to answer. Everything except that fixed observation policy is shared
    with the agentic judge so the comparison isolates the policy.
    """

    def __init__(
        self,
        client: Any,
        n_frames: int = 16,
        long_side: int = 768,
        max_decode_frames: int = 900,
    ):
        super().__init__(client)
        self.n_frames = int(n_frames)
        self.long_side = int(long_side)
        self.max_decode_frames = int(max_decode_frames)

    def judge(
        self,
        video_path: str | Path,
        caption: str,
        video_id: str | None = None,
    ) -> BaselineResult:
        vid = _video_id_for(video_path, video_id)
        before = _usage_snapshot(self.client)

        try:
            server = FrameServer(video_path, max_decode_frames=self.max_decode_frames)
            got = server.sample(n_frames=self.n_frames, long_side=self.long_side)
            duration = server.duration
        except Exception as exc:  # noqa: BLE001 - a bad file must not end the sweep
            return BaselineResult(
                video_id=vid,
                pc_score=None,
                confidence=0.0,
                score_imputed=False,
                raw_text="",
                n_frames=0,
                cost=_cost_since(self.client, before, 0),
                error=f"frame decode failed: {type(exc).__name__}: {exc}",
            )

        # frames_served, not len(got): the frame budget is counted by the layer
        # that hands out the pixels, not by the caller that asked for them.
        frames = server.frames_served
        times = [t for t, _ in got]
        prompt = TASK_SINGLE_PASS.format(
            caption=caption.strip(),
            n=len(got),
            duration=duration,
            timestamps=_fmt_times(times),
        )
        return self._ask(vid, prompt, [img for _, img in got], before, frames, len(got))


class CaptionOnlyBaseline(_PassiveBaseline):
    """No video at all: score the prompt alone.

    Measures how much apparent skill is really dataset predictability. Whatever
    correlation this reaches is available to any judge without watching
    anything, so it bounds how impressive a video judge's correlation is.

    `video_path` is accepted and ignored, which is the point: the runner can swap
    the two baselines without knowing which one needs pixels, and this one still
    produces a row for the video whose file is missing from the archive.
    """

    def judge(
        self,
        video_path: str | Path | None = None,
        caption: str = "",
        video_id: str | None = None,
    ) -> BaselineResult:
        vid = _video_id_for(video_path, video_id)
        before = _usage_snapshot(self.client)
        prompt = TASK_CAPTION_ONLY.format(caption=caption.strip())
        return self._ask(vid, prompt, [], before, 0, 0)


__all__ = [
    "BASELINE_SYS",
    "BaselineResult",
    "CaptionOnlyBaseline",
    "COST_KEYS",
    "DEFAULT_CONFIDENCE",
    "IMPUTED_SCORE",
    "SinglePassBaseline",
    "TASK_CAPTION_ONLY",
    "TASK_SINGLE_PASS",
    "parse_reply",
]
