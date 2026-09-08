"""Offline test of the passive baselines. No network, no API key, no real model.

The baselines are the number the agentic judge is measured against, so the things
pinned down here are the ones that would quietly corrupt that comparison:

  - the frames and their timestamps really reach the prompt (a model shown frames
    with no time information cannot reason about rates, so a baseline that forgot
    them would be weaker than the paradigm we claim to beat);
  - the rubric is byte-identical to the agentic judge's;
  - score parsing degrades in three honest tiers -- JSON, prose, imputed -- and
    says which tier it used, because the imputation rate is reported;
  - cost is per-video even when one client judges many videos, since a shared
    client's lifetime totals would charge every video with the whole run;
  - a missing or undecodable file yields a result, not a traceback.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from eval.baselines import (  # noqa: E402
    BASELINE_SYS,
    COST_KEYS,
    IMPUTED_SCORE,
    BaselineResult,
    CaptionOnlyBaseline,
    SinglePassBaseline,
    parse_reply,
)
from pjudge.backends.llm import LLMResponse, Usage  # noqa: E402
from pjudge.perception.frames import FrameServer  # noqa: E402
from pjudge.prompts import PC_RUBRIC  # noqa: E402

CAPTION = "A glass of water is knocked off a table and shatters on the tiled floor."

# Synthetic clip geometry, fixed so the expected timestamps can be derived by
# hand rather than read back out of the code under test.
N_SRC_FRAMES = 72
FPS = 24
WIDTH, HEIGHT = 320, 240
DURATION = N_SRC_FRAMES / FPS  # 3.0s
N_SAMPLED = 16
LONG_SIDE = 256


def make_video(path: Path) -> None:
    writer = cv2.VideoWriter(
        str(path), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (WIDTH, HEIGHT)
    )
    for i in range(N_SRC_FRAMES):
        frame = np.full((HEIGHT, WIDTH, 3), 30, np.uint8)
        cv2.circle(frame, (20 + 4 * i, 120), 12, (240, 240, 240), -1)
        writer.write(frame)
    writer.release()


# --------------------------------------------------------------------------
# mock model
# --------------------------------------------------------------------------


class MockClient:
    """Duck-typed stand-in for LLMClient.

    It carries the real `Usage` accumulator because that is where the baselines
    read cost from; each scripted reply may declare its own token counts, which
    is what makes a wrong (cumulative) delta visible.
    """

    def __init__(self, replies: list[dict]):
        self.role = "baseline"
        self.usage = Usage()
        self.replies = list(replies)
        self.calls: list[dict] = []

    def ask(self, prompt, system=None, images=None, json_mode=False, **kw):
        reply = self.replies[min(len(self.calls), len(self.replies) - 1)]
        self.calls.append(
            {
                "prompt": prompt,
                "system": system,
                "images": images,
                "json_mode": json_mode,
            }
        )
        usage = Usage(
            calls=1,
            cache_hits=1 if reply.get("cached") else 0,
            prompt_tokens=reply.get("prompt_tokens", 100),
            completion_tokens=reply.get("completion_tokens", 20),
            images=len(images or []),
        )
        self.usage.add(usage)
        return LLMResponse(
            text=reply["text"],
            model="mock",
            role=self.role,
            usage=usage,
            cached=bool(reply.get("cached")),
        )


class BoomClient:
    """A dead endpoint."""

    def __init__(self) -> None:
        self.role = "baseline"
        self.usage = Usage()
        self.calls = 0

    def ask(self, prompt, system=None, images=None, json_mode=False, **kw):
        self.calls += 1
        raise RuntimeError("503 upstream is unavailable")


def reply(text: str, **kw) -> dict:
    return {"text": text, **kw}


GOOD_JSON = json.dumps(
    {"pc_score": 4, "confidence": 0.8, "reason": "The glass falls and breaks plausibly."}
)


# --------------------------------------------------------------------------
# expected timestamps, computed independently of the frame server
# --------------------------------------------------------------------------


def expected_timestamps() -> list[float]:
    """Nearest decoded frame time for 16 targets evenly spaced over the clip.

    Frame i sits at i/FPS. The targets are 3.0*k/15 for k in 0..15, so the
    target index is 4.8*k rounded to nearest and clipped to the last frame.
    """
    out: list[float] = []
    for k in range(N_SAMPLED):
        idx = min(N_SRC_FRAMES - 1, int(np.floor(4.8 * k + 0.5)))
        out.append(idx / FPS)
    return out


# --------------------------------------------------------------------------
# tests
# --------------------------------------------------------------------------


def test_video_fixture(video: Path) -> None:
    """The hand-derived constants must match what cv2 actually wrote."""
    fs = FrameServer(video)
    meta = fs.meta
    assert meta.n_frames == N_SRC_FRAMES, meta.n_frames
    assert abs(meta.fps - FPS) < 1e-6, meta.fps
    assert abs(meta.duration - DURATION) < 1e-6, meta.duration
    times = [round(t, 6) for t, _ in fs.sample(n_frames=N_SAMPLED)]
    want = [round(t, 6) for t in expected_timestamps()]
    assert times == want, (times, want)
    assert len(set(times)) == N_SAMPLED, "sampler produced duplicate frames"
    print(f"  fixture ok: {meta.n_frames} frames, {meta.duration:.2f}s, 16 sampled")


def test_good_json(video: Path) -> None:
    client = MockClient([reply(GOOD_JSON, prompt_tokens=3120, completion_tokens=41)])
    baseline = SinglePassBaseline(client, n_frames=N_SAMPLED, long_side=LONG_SIDE)
    r = baseline.judge(video, CAPTION, video_id="synthetic_glass")

    assert r.pc_score == 4.0, r.pc_score
    assert r.confidence == 0.8, r.confidence
    assert not r.score_imputed and not r.fatal
    assert r.error == "", r.error
    assert r.video_id == "synthetic_glass"
    assert r.raw_text == GOOD_JSON

    # frame accounting
    assert r.n_frames == N_SAMPLED, r.n_frames
    assert r.cost["frames"] == N_SAMPLED, r.cost
    assert r.cost["prompt_tokens"] == 3120 and r.cost["completion_tokens"] == 41, r.cost
    assert r.cost["llm_calls"] == 1 and r.cost["cache_hits"] == 0, r.cost
    assert sorted(r.cost) == sorted(COST_KEYS), r.cost

    call = client.calls[0]
    assert call["json_mode"] is True, "baseline did not ask for JSON"
    assert call["system"] == BASELINE_SYS
    assert PC_RUBRIC in call["system"], "baseline used a different rubric"
    assert CAPTION in call["prompt"]
    assert '"pc_score"' in call["prompt"], "reply schema missing from the prompt"

    # every frame reaches the model, at the size we asked for
    images = call["images"]
    assert isinstance(images, list) and len(images) == N_SAMPLED, len(images or [])
    assert all(isinstance(im, np.ndarray) for im in images)
    assert {max(im.shape[:2]) for im in images} == {LONG_SIDE}, "frames not resized"
    assert client.usage.images == N_SAMPLED, client.usage.images

    # and so does the time of each frame, in order
    want = expected_timestamps()
    prompt = call["prompt"]
    for t in want:
        assert f"{t:.2f}s" in prompt, f"timestamp {t:.2f}s missing from prompt"
    positions = [prompt.index(f"{t:.2f}s") for t in want]
    assert positions == sorted(positions), "timestamps out of temporal order"
    assert f"{DURATION:.2f}s" in prompt, "clip duration missing from prompt"
    assert f"{N_SAMPLED} frames" in prompt, "frame count missing from prompt"
    print(f"  good json ok: score={r.pc_score} conf={r.confidence} cost={r.cost}")


def test_prose_fallback(video: Path) -> None:
    client = MockClient([reply("I would say 2 out of 5, the shards float upward.")])
    r = SinglePassBaseline(client, n_frames=4).judge(video, CAPTION)

    assert r.pc_score == 2.0, r.pc_score
    assert not r.score_imputed, "a recovered score must not be flagged as imputed"
    assert "prose" in r.error, r.error
    assert r.confidence == 0.5, r.confidence  # model gave none; harness default
    assert r.video_id == video.stem, r.video_id  # id derived from the file name
    print(f"  prose fallback ok: score={r.pc_score} note={r.error!r}")


def test_imputation_flagged(video: Path) -> None:
    client = MockClient([reply("Honestly, the vibes here are simply off.")])
    r = SinglePassBaseline(client, n_frames=4).judge(video, CAPTION, video_id="garbage")

    assert r.pc_score == IMPUTED_SCORE == 3.0, r.pc_score
    assert r.score_imputed is True
    assert "imputed" in r.error, r.error
    assert r.confidence == 0.0, "an imputed score must rank last on confidence"
    assert not r.fatal, "an imputed score is still a score"
    print(f"  imputation ok: score={r.pc_score} imputed={r.score_imputed} "
          f"note={r.error!r}")


def test_clamping(video: Path) -> None:
    high = MockClient([reply(json.dumps({"pc_score": 9, "confidence": 0.9}))])
    r = SinglePassBaseline(high, n_frames=4).judge(video, CAPTION, video_id="high")
    assert r.pc_score == 5.0, r.pc_score
    assert not r.score_imputed
    assert "clamped to 5" in r.error, r.error

    low = MockClient([reply(json.dumps({"pc_score": 0, "confidence": 1.4}))])
    r2 = SinglePassBaseline(low, n_frames=4).judge(video, CAPTION, video_id="low")
    assert r2.pc_score == 1.0, r2.pc_score
    assert r2.confidence == 1.0, r2.confidence
    assert "clamped to 1" in r2.error and "confidence 1.4" in r2.error, r2.error
    print(f"  clamping ok: 9 -> {r.pc_score}, 0 -> {r2.pc_score}")


def test_parse_reply_table() -> None:
    """The parser on its own, including the cases that must NOT parse."""
    # (reply, score, confidence, imputed, substring the note must contain)
    cases = [
        ('{"pc_score": 5, "confidence": 0.2}', 5.0, 0.2, False, ""),
        ('```json\n{"pc_score": 1, "confidence": 1}\n```', 1.0, 1.0, False, ""),
        ('prose then {"pc_score": 3.5, "confidence": 0.4} then more', 3.5, 0.4, False, ""),
        ('{"pc_score": null, "reason": "I would rate it 4"}', 4.0, 0.5, False, "prose"),
        ('{"pc_score": "4 out of 5"}', 4.0, 0.5, False, ""),
        ('{"score": 2}', 2.0, 0.5, False, ""),
        ('{"pc_score": 6, "confidence": -1}', 5.0, 0.0, False, "clamped"),
        ("I would say 2 out of 5", 2.0, 0.5, False, "prose"),
        ("Rating: 4.5", 4.5, 0.5, False, "prose"),
        ("I'd give it 3/5 for physics", 3.0, 0.5, False, "prose"),
        ("", IMPUTED_SCORE, 0.0, True, "imputed"),
        ("no number here at all", IMPUTED_SCORE, 0.0, True, "imputed"),
        ("score: 15", IMPUTED_SCORE, 0.0, True, "imputed"),  # 15 is no standalone 1-5
        ("scored 7 on a 10-point scale", IMPUTED_SCORE, 0.0, True, "imputed"),
        # a bool must not become 1.0 via float(True)
        ('{"pc_score": true}', IMPUTED_SCORE, 0.0, True, "imputed"),
    ]
    for text, want_score, want_conf, want_imputed, want_note in cases:
        score, conf, imputed, note = parse_reply(text)
        assert (score, conf, imputed) == (want_score, want_conf, want_imputed), (
            text,
            (score, conf, imputed),
            (want_score, want_conf, want_imputed),
        )
        assert want_note in note, (text, want_note, note)
        if not want_note:
            assert note == "", (text, note)  # a clean JSON reply gets no note
    print(f"  parser table ok: {len(cases)} cases")


def test_cost_is_per_video(video: Path, video2: Path) -> None:
    """One client, two videos: each result must carry only its own tokens."""
    client = MockClient(
        [
            reply(GOOD_JSON, prompt_tokens=1000, completion_tokens=30),
            reply(
                json.dumps({"pc_score": 2, "confidence": 0.6}),
                prompt_tokens=2500,
                completion_tokens=45,
                cached=True,
            ),
        ]
    )
    baseline = SinglePassBaseline(client, n_frames=8, long_side=LONG_SIDE)
    first = baseline.judge(video, CAPTION, video_id="v1")
    second = baseline.judge(video2, CAPTION, video_id="v2")

    assert first.cost["prompt_tokens"] == 1000, first.cost
    assert second.cost["prompt_tokens"] == 2500, second.cost  # not 3500
    assert first.cost["completion_tokens"] == 30, first.cost
    assert second.cost["completion_tokens"] == 45, second.cost
    assert first.cost["llm_calls"] == second.cost["llm_calls"] == 1
    assert first.cost["cache_hits"] == 0 and second.cost["cache_hits"] == 1, (
        first.cost,
        second.cost,
    )
    assert first.cost["frames"] == second.cost["frames"] == 8

    # the deltas must add up to the client's lifetime totals
    assert client.usage.prompt_tokens == 3500 and client.usage.calls == 2
    assert (
        first.cost["prompt_tokens"] + second.cost["prompt_tokens"]
        == client.usage.prompt_tokens
    )
    print(f"  per-video cost ok: {first.cost['prompt_tokens']} then "
          f"{second.cost['prompt_tokens']} of {client.usage.prompt_tokens} total")


def test_caption_only_sends_no_images(video: Path) -> None:
    client = MockClient([reply(json.dumps({"pc_score": 3, "confidence": 0.3}))])
    baseline = CaptionOnlyBaseline(client)
    r = baseline.judge(video, CAPTION, video_id="caption_only")

    assert r.pc_score == 3.0 and r.confidence == 0.3
    assert r.error == "" and not r.score_imputed
    assert r.n_frames == 0 and r.cost["frames"] == 0, r.cost
    assert client.usage.images == 0, "caption-only baseline sent pixels"

    call = client.calls[0]
    assert not call["images"], call["images"]
    assert call["system"] == BASELINE_SYS and PC_RUBRIC in call["system"]
    assert CAPTION in call["prompt"]
    assert "timestamp" not in call["prompt"].lower(), "no frames, so no timestamps"

    # interchangeable with the frame baseline: it must not care about the file
    absent = baseline.judge(video.parent / "does_not_exist.mp4", CAPTION, video_id="x")
    assert absent.pc_score == 3.0 and absent.error == "", absent
    missing_path = baseline.judge(None, CAPTION, video_id="y")
    assert missing_path.pc_score == 3.0 and missing_path.video_id == "y"
    print(f"  caption-only ok: images={client.usage.images} calls={len(client.calls)}")


def test_missing_and_broken_files(tmp: Path) -> None:
    client = MockClient([reply(GOOD_JSON)])
    baseline = SinglePassBaseline(client, n_frames=4)

    absent = baseline.judge(tmp / "absent.mp4", CAPTION, video_id="absent")
    assert absent.pc_score is None and absent.fatal, absent
    assert not absent.score_imputed, "an unreadable file is not an imputed score"
    assert absent.error.startswith("frame decode failed"), absent.error
    assert "absent.mp4" in absent.error, absent.error
    assert absent.n_frames == 0
    assert all(absent.cost[k] == 0 for k in COST_KEYS), absent.cost
    assert client.calls == [], "the model was called with no frames"

    broken = tmp / "broken.mp4"
    broken.write_bytes(b"this is not an mp4 file" * 10)
    bad = baseline.judge(broken, CAPTION, video_id="broken")
    assert bad.pc_score is None and bad.error.startswith("frame decode failed"), bad
    assert client.calls == [], "the model was called on an undecodable clip"
    print(f"  missing/broken ok: {absent.error[:58]!r} / {bad.error[:58]!r}")


def test_llm_failure_is_data(video: Path) -> None:
    client = BoomClient()
    baseline = SinglePassBaseline(client, n_frames=N_SAMPLED)
    r = baseline.judge(video, CAPTION, video_id="dead")
    assert r.pc_score is None and r.fatal, r
    assert not r.score_imputed
    assert "llm call failed" in r.error and "503" in r.error, r.error
    assert client.calls == 1, "a baseline must not retry a failed call"
    # the frames were decoded and paid for even though the answer never came
    assert r.cost["frames"] == N_SAMPLED and r.cost["llm_calls"] == 0, r.cost
    print(f"  llm failure ok: {r.error!r}")


def test_as_dict_shape(video: Path) -> None:
    client = MockClient([reply(GOOD_JSON, prompt_tokens=7, completion_tokens=3)])
    r = SinglePassBaseline(client, n_frames=4).judge(video, CAPTION, video_id="shape")
    d = r.as_dict()

    expected = {
        "video_id", "pc_score", "confidence", "score_imputed", "raw_text",
        "n_frames", "error", "fatal", "cost", *COST_KEYS,
    }
    assert set(d) == expected, set(d) ^ expected
    assert d["cost"] == {k: d[k] for k in COST_KEYS}, d
    assert d["prompt_tokens"] == 7 and d["completion_tokens"] == 3
    round_tripped = json.loads(json.dumps(d))  # must survive the results jsonl
    assert round_tripped["pc_score"] == 4.0

    empty = BaselineResult(
        video_id="e", pc_score=None, confidence=0.0, score_imputed=False,
        raw_text="", n_frames=0,
    )
    assert empty.cost == dict.fromkeys(COST_KEYS, 0), empty.cost
    assert empty.as_dict()["fatal"] is True
    print(f"  as_dict ok: {sorted(d)}")


def main() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        video, video2 = tmp / "clip.mp4", tmp / "clip2.mp4"
        make_video(video)
        make_video(video2)
        assert video.exists() and video.stat().st_size > 0

        print("test_video_fixture");     test_video_fixture(video)
        print("test_good_json");         test_good_json(video)
        print("test_prose_fallback");    test_prose_fallback(video)
        print("test_imputation");        test_imputation_flagged(video)
        print("test_clamping");          test_clamping(video)
        print("test_parse_reply_table"); test_parse_reply_table()
        print("test_cost_per_video");    test_cost_is_per_video(video, video2)
        print("test_caption_only");      test_caption_only_sends_no_images(video)
        print("test_missing_files");     test_missing_and_broken_files(tmp)
        print("test_llm_failure");       test_llm_failure_is_data(video)
        print("test_as_dict_shape");     test_as_dict_shape(video)
    print("\nALL BASELINE TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
