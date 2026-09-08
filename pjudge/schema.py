"""Serializable contracts for the two-agent rubric judge.

The trace has three immutable layers:

    rubric item -> ToolCall (T*) -> Evidence (E*) -> RubricDecision

Ids are assigned by :mod:`pjudge.runtime`, never by either model.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Literal, Sequence


@dataclass(frozen=True)
class TimeSpan:
    start: float
    end: float

    def __post_init__(self) -> None:
        if self.end < self.start:
            raise ValueError(f"end {self.end} precedes start {self.start}")

    @property
    def duration(self) -> float:
        return self.end - self.start

    def clipped_to(self, duration: float) -> "TimeSpan":
        return TimeSpan(max(0.0, min(self.start, duration)), max(0.0, min(self.end, duration)))

    def as_dict(self) -> dict[str, float]:
        return {"start": round(self.start, 3), "end": round(self.end, 3)}


@dataclass(frozen=True)
class BBox:
    """Normalised image box."""

    x0: float
    y0: float
    x1: float
    y1: float

    def __post_init__(self) -> None:
        if not (0 <= self.x0 < self.x1 <= 1 and 0 <= self.y0 < self.y1 <= 1):
            raise ValueError(f"degenerate or unnormalised bbox: {self}")

    @property
    def area(self) -> float:
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def to_pixels(self, width: int, height: int) -> tuple[int, int, int, int]:
        return (int(round(self.x0 * width)), int(round(self.y0 * height)), int(round(self.x1 * width)), int(round(self.y1 * height)))

    def padded(self, margin: float, min_side: float = 0.0) -> "BBox":
        cx, cy = (self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2
        x0, y0 = self.x0 - margin, self.y0 - margin
        x1, y1 = self.x1 + margin, self.y1 + margin
        if min_side:
            half = min_side / 2
            x0, x1 = min(x0, cx - half), max(x1, cx + half)
            y0, y1 = min(y0, cy - half), max(y1, cy + half)
        return BBox(max(0.0, x0), max(0.0, y0), min(1.0, x1), min(1.0, y1))

    def as_dict(self) -> dict[str, float]:
        return {k: round(v, 4) for k, v in asdict(self).items()}

    @classmethod
    def full(cls) -> "BBox":
        return cls(0.0, 0.0, 1.0, 1.0)


def span_from_any(value: Any, duration: float | None = None) -> TimeSpan | None:
    if not isinstance(value, dict):
        return None
    try:
        span = TimeSpan(float(value["start"]), float(value["end"]))
    except (KeyError, TypeError, ValueError):
        return None
    return span.clipped_to(duration) if duration is not None else span


def bbox_from_any(value: Any) -> BBox | None:
    if not isinstance(value, dict):
        return None
    try:
        return BBox(*(float(value[k]) for k in ("x0", "y0", "x1", "y1")))
    except (KeyError, TypeError, ValueError):
        return None


class Tool(str, Enum):
    OVERVIEW = "overview"
    INSPECT_CLIP = "inspect_clip"
    INSPECT_REGION = "inspect_region"
    COMPARE_FRAMES = "compare_frames"
    PRESENCE_CHECK = "presence_check"


DecisionStatus = Literal["pass", "fail", "not_shown"]


@dataclass
class ToolCall:
    id: str
    tool: Tool
    rubric_ids: list[str]
    arguments: dict[str, Any]
    reason: str = ""
    round: int = 0
    status: Literal["pending", "completed", "failed"] = "pending"
    timestamps: list[float] = field(default_factory=list)
    artifacts: list[str] = field(default_factory=list)
    error: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {"id": self.id, "round": self.round, "tool": self.tool.value, "rubric_ids": list(self.rubric_ids), "arguments": self.arguments, "reason": self.reason, "status": self.status, "timestamps": [round(t, 3) for t in self.timestamps], "artifacts": list(self.artifacts), "error": self.error}

    def for_prompt(self) -> dict[str, Any]:
        """Model-visible form; artifact paths are intentionally blinded."""
        result = self.as_dict()
        result.pop("artifacts", None)
        return result


@dataclass
class RubricEvidence:
    id: str
    tool_call_id: str
    rubric_ids: list[str]
    observation: str
    timestamps: list[float] = field(default_factory=list)
    artifacts: list[str] = field(default_factory=list)
    confidence: float = 0.5
    visible: bool | None = None
    limitations: str = ""
    raw_response: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {"id": self.id, "tool_call_id": self.tool_call_id, "rubric_ids": list(self.rubric_ids), "observation": self.observation, "timestamps": [round(t, 3) for t in self.timestamps], "artifacts": list(self.artifacts), "confidence": round(self.confidence, 3), "visible": self.visible, "limitations": self.limitations, "raw_response": self.raw_response}

    def for_prompt(self) -> dict[str, Any]:
        """Model-visible form without file paths or duplicated raw model text."""
        result = self.as_dict()
        result.pop("artifacts", None)
        result.pop("raw_response", None)
        return result

    def digest(self) -> str:
        return f"[{self.id} via {self.tool_call_id} for {','.join(self.rubric_ids)}] {self.observation}"


@dataclass
class RubricDecision:
    rubric_id: str
    status: DecisionStatus
    evidence_ids: list[str]
    explanation: str
    confidence: float = 0.5
    source: Literal["agent", "runtime_fallback"] = "agent"

    def as_dict(self, tool_call_ids: Sequence[str] | None = None) -> dict[str, Any]:
        result: dict[str, Any] = {"rubric_id": self.rubric_id, "status": self.status, "evidence_ids": list(self.evidence_ids), "explanation": self.explanation, "confidence": round(self.confidence, 3), "source": self.source}
        if tool_call_ids is not None:
            result["tool_call_ids"] = list(tool_call_ids)
        return result


@dataclass
class InspectionResult:
    tool_calls: list[ToolCall]
    evidence: list[RubricEvidence]
    decisions: list[RubricDecision]
    recognisable_attempt: bool = True
    incomplete_ids: list[str] = field(default_factory=list)


@dataclass
class Feedback:
    rubric_id: str
    evidence_ids: list[str]
    problem: str
    suggested_fix: str

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ObservationCost:
    rounds: int = 0
    frames: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    llm_calls: int = 0
    cache_hits: int = 0

    def as_dict(self) -> dict[str, int]:
        return asdict(self)


@dataclass
class JudgeReport:
    video_id: str
    rubric_id: int | str
    sa_score: int
    pc_score: int
    confidence: float
    decisions: list[RubricDecision]
    feedback: list[Feedback]
    summary: str
    trace_summary: dict[str, Any]
    cost: ObservationCost = field(default_factory=ObservationCost)
    score_note: str = ""
    error: str = ""

    @property
    def failed_pc(self) -> list[RubricDecision]:
        return [d for d in self.decisions if d.rubric_id.startswith("P") and d.status == "fail"]

    def as_dict(self) -> dict[str, Any]:
        failed_sa = [d for d in self.decisions if d.rubric_id.startswith("S") and d.status == "fail"]
        not_shown = [d for d in self.decisions if d.status == "not_shown"]
        score_imputed = any(d.source == "runtime_fallback" for d in self.decisions)
        return {"video_id": self.video_id, "rubric_id": self.rubric_id, "sa_score": self.sa_score, "pc_score": self.pc_score, "confidence": round(self.confidence, 3), "abstain": False, "score_imputed": score_imputed, "fatal": False, "n_violations": len(self.failed_pc), "n_failed_sa": len(failed_sa), "n_failed_pc": len(self.failed_pc), "n_not_shown": len(not_shown), "n_tool_calls": int(self.trace_summary.get("n_tool_calls", 0)), "n_evidence": int(self.trace_summary.get("n_evidence", 0)), "violation_descriptions": [d.explanation for d in self.failed_pc], "decisions": [d.as_dict() for d in self.decisions], "feedback": [f.as_dict() for f in self.feedback], "summary": self.summary, "trace_summary": self.trace_summary, "cost": self.cost.as_dict(), "score_note": self.score_note, "error": self.error}


@dataclass
class JudgeResult:
    report: JudgeReport
    trace: dict[str, Any]
    trace_path: Path | None = None

    @property
    def verdict(self) -> JudgeReport:
        return self.report


def validate_trace_links(tool_calls: Sequence[ToolCall], evidence: Sequence[RubricEvidence], decisions: Sequence[RubricDecision]) -> list[str]:
    problems: list[str] = []
    calls = {t.id: t for t in tool_calls}
    evs = {e.id: e for e in evidence}
    if len(calls) != len(tool_calls):
        problems.append("duplicate tool-call id")
    if len(evs) != len(evidence):
        problems.append("duplicate evidence id")
    for ev in evidence:
        if ev.tool_call_id not in calls:
            problems.append(f"{ev.id} cites unknown tool call {ev.tool_call_id}")
    for decision in decisions:
        if not decision.evidence_ids:
            problems.append(f"{decision.rubric_id} cites no evidence")
        for eid in decision.evidence_ids:
            ev = evs.get(eid)
            if ev is None:
                problems.append(f"{decision.rubric_id} cites unknown evidence {eid}")
            elif decision.rubric_id not in ev.rubric_ids:
                problems.append(f"{decision.rubric_id} is not linked to evidence {eid}")
    return problems
