"""Matching our reported violations against the ones humans wrote by hand.

The lexical matcher in `metrics.py` cannot do this job, for two measured reasons.

Vocabulary: humans annotate in physics language ("the pole tip remains stationary
relative to the background") while the judge reports visual observation ("the
javelin's rod is visible and unobstructed at 0.80s"). On a 12-video pilot the two
shared so few content words that lexical matching scored 0 of 8 gold violations,
including pairs that plainly describe the same failure.

Polarity: lexical overlap is *highest* exactly when one text states an expectation
and the other states that it held. A word-overlap matcher therefore scores its
confident matches on the cases it is most likely to have backwards.

There is also an asymmetry the prompt has to spell out. A gold entry is a
*violated expectation* ("the knife retains its structural integrity"), while our
text is the *observed failure* ("the hilt shrinks and the blade changes
curvature"). The question is not "do these two sentences mean the same thing" but
"is the failure we describe the violation of that expectation".
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pjudge.agents.base import as_text, ask_json
from pjudge.backends.llm import LLMClient

MATCH_SYS = """\
You decide whether two descriptions refer to the same physical failure in one
short video.

You are given:
  RULE     - a physical expectation that a human annotator marked as VIOLATED in
             this video. It is phrased as what SHOULD happen, and the human is
             asserting that it did not.
  REPORT   - a failure that an automatic judge says it observed in the video,
             phrased as what DID happen.

Answer whether REPORT is that violation of RULE.

Say yes when a careful person reading both would conclude they are one failure.
Differences that do NOT matter: wording, level of abstraction, physics language
versus visual language, extra timing or position detail in REPORT, which object
is named as the subject when it is the same interaction.

Say no when:
  - they concern different failures, even if both involve the same object;
  - REPORT describes the expectation HOLDING, or describes something unremarkable,
    rather than a failure;
  - REPORT is a rendering or aesthetic complaint and RULE is about mechanics, or
    vice versa;
  - deciding yes would require assuming a failure REPORT does not actually state.

Being wrong in the direction of "yes" inflates a score, so when the two are only
loosely related, answer no.

Reply with one JSON object and nothing else."""

MATCH_TASK = """\
RULE (human-annotated, violated in this video):
{gold}

REPORT (what the automatic judge says it observed):
{report}

{context}JSON:
{{"same_failure": true|false, "why": "one sentence"}}"""


@dataclass
class MatchStats:
    """How much of the matching was actually decided by the model."""

    comparisons: int = 0
    matches: int = 0
    errors: int = 0
    cache_hits: int = 0
    reasons: list[dict[str, Any]] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "comparisons": self.comparisons,
            "matches": self.matches,
            "errors": self.errors,
            "cache_hits": self.cache_hits,
        }


class LLMMatcher:
    """A `matcher(pred, gold) -> bool` for `metrics.open_discovery_match`.

    Every comparison goes through the client's disk cache, so re-running a
    diagnosis evaluation over the same pairs costs nothing and gives the same
    answer -- which matters here because the endpoint refuses `temperature`.

    A comparison that errors returns False. Failing closed under-reports our own
    recall rather than inventing agreement.
    """

    def __init__(self, client: LLMClient, caption: str = "", record_reasons: bool = True):
        self.client = client
        self.caption = caption
        self.record_reasons = record_reasons
        self.stats = MatchStats()

    def for_video(self, caption: str) -> "LLMMatcher":
        """A matcher bound to one video's prompt, so the model has the scene."""
        sibling = LLMMatcher(self.client, caption, self.record_reasons)
        sibling.stats = self.stats  # share the tally across videos
        return sibling

    def __call__(self, pred: str, gold: str) -> bool:
        pred, gold = as_text(pred), as_text(gold)
        if not pred or not gold:
            return False
        self.stats.comparisons += 1
        context = (
            f"For reference, the prompt the video was generated from:\n{self.caption}\n\n"
            if self.caption
            else ""
        )
        try:
            data = ask_json(
                self.client,
                MATCH_SYS,
                MATCH_TASK.format(gold=gold, report=pred, context=context),
            )
        except Exception as exc:  # noqa: BLE001 - a failed comparison is not a match
            self.stats.errors += 1
            if self.record_reasons:
                self.stats.reasons.append(
                    {"gold": gold, "pred": pred, "same": None, "why": f"error: {exc}"}
                )
            return False
        same = bool(data.get("same_failure"))
        if same:
            self.stats.matches += 1
        if self.record_reasons:
            self.stats.reasons.append(
                {
                    "gold": gold[:200],
                    "pred": pred[:200],
                    "same": same,
                    "why": as_text(data.get("why"))[:200],
                }
            )
        return same


def build_matcher(cfg: dict, role: str = "judge", caption: str = "") -> LLMMatcher:
    """Matcher on the configured endpoint, reusing the judge's own model."""
    from pjudge.backends.llm import LLMConfig

    client = LLMClient(LLMConfig.from_dict(cfg["llm"], role), role="matcher")
    return LLMMatcher(client, caption=caption)
