"""Agent 2: audit rubric decisions and produce scores, feedback and summary."""

from __future__ import annotations

import json
from collections import Counter
from typing import Any, Sequence

from ..backends.llm import LLMClient
from ..prompts.rubric_agents import JUDGE_SYSTEM, JUDGE_TASK
from ..rubric import deterministic_scores, item_map
from ..schema import (
    Feedback,
    InspectionResult,
    JudgeReport,
    ObservationCost,
    RubricDecision,
    RubricEvidence,
    ToolCall,
)
from .base import as_float, as_list, as_text, ask_json


class ScoringFeedbackAgent:
    def __init__(self, client: LLMClient):
        self.client = client

    def finalize(
        self,
        *,
        video_id: str,
        caption: str,
        rubric: dict[str, Any],
        policy: dict[str, Any],
        inspection: InspectionResult,
        cost: ObservationCost,
    ) -> JudgeReport:
        sa, pc = deterministic_scores(
            rubric, inspection.decisions, inspection.recognisable_attempt
        )
        data = ask_json(
            self.client,
            JUDGE_SYSTEM,
            JUDGE_TASK.format(
                caption=caption,
                rubric=json.dumps(rubric, ensure_ascii=False),
                policy=json.dumps(policy, ensure_ascii=False),
                decisions=json.dumps([d.as_dict() for d in inspection.decisions], ensure_ascii=False),
                evidence=json.dumps([e.for_prompt() for e in inspection.evidence], ensure_ascii=False),
                tool_calls=json.dumps([t.for_prompt() for t in inspection.tool_calls], ensure_ascii=False),
                sa_score=sa,
                pc_score=pc,
            ),
        )
        evidence_by_id = {e.id: e for e in inspection.evidence}
        decisions_by_id = {d.rubric_id: d for d in inspection.decisions}
        items = item_map(rubric)
        failed = {d.rubric_id for d in inspection.decisions if d.status == "fail"}
        feedback: list[Feedback] = []
        for raw in as_list(data.get("feedback")):
            if not isinstance(raw, dict):
                continue
            rid = as_text(raw.get("rubric_id"))
            if rid not in items or rid not in failed:
                continue
            cited = [
                as_text(e)
                for e in as_list(raw.get("evidence_ids"))
                if as_text(e) in evidence_by_id
                and rid in evidence_by_id[as_text(e)].rubric_ids
                and as_text(e) in decisions_by_id[rid].evidence_ids
            ]
            problem = as_text(raw.get("problem"))
            suggested_fix = as_text(raw.get("suggested_fix"))
            if not cited or not problem or not suggested_fix:
                continue
            feedback.append(
                Feedback(
                    rubric_id=rid,
                    evidence_ids=cited,
                    problem=problem,
                    suggested_fix=suggested_fix,
                )
            )
        covered = {item.rubric_id for item in feedback}
        for decision in inspection.decisions:
            if decision.status == "fail" and decision.rubric_id not in covered:
                feedback.append(
                    Feedback(
                        rubric_id=decision.rubric_id,
                        evidence_ids=list(decision.evidence_ids),
                        problem=decision.explanation,
                        suggested_fix="Revise the video so the failed rubric condition is no longer visible.",
                    )
                )
        reported_sa = _integer_score(data.get("sa_score"))
        reported_pc = _integer_score(data.get("pc_score"))
        note = ""
        if (reported_sa, reported_pc) != (sa, pc):
            note = (
                f"reporting agent proposed SA={reported_sa}, PC={reported_pc}; "
                f"runtime enforced deterministic SA={sa}, PC={pc}"
            )
        trace_summary = build_trace_summary(
            inspection.tool_calls,
            inspection.evidence,
            inspection.decisions,
            narrative=as_text(data.get("trace_summary")),
        )
        return JudgeReport(
            video_id=video_id,
            rubric_id=rubric["id"],
            sa_score=sa,
            pc_score=pc,
            confidence=as_float(data.get("confidence"), _decision_confidence(inspection.decisions)),
            decisions=inspection.decisions,
            feedback=feedback,
            summary=as_text(data.get("summary")) or _fallback_summary(inspection.decisions),
            trace_summary=trace_summary,
            cost=cost,
            score_note=note,
        )


def build_trace_summary(
    calls: Sequence[ToolCall],
    evidence: Sequence[RubricEvidence],
    decisions: Sequence[RubricDecision],
    narrative: str = "",
) -> dict[str, Any]:
    evidence_by_id = {e.id: e for e in evidence}
    tracks: dict[str, Any] = {}
    for decision in decisions:
        call_ids = []
        for eid in decision.evidence_ids:
            ev = evidence_by_id.get(eid)
            if ev is not None and ev.tool_call_id not in call_ids:
                call_ids.append(ev.tool_call_id)
        tracks[decision.rubric_id] = {
            "tool_call_ids": call_ids,
            "evidence_ids": list(decision.evidence_ids),
            "status": decision.status,
            "source": decision.source,
            "chain": " -> ".join(
                [decision.rubric_id, *call_ids, *decision.evidence_ids, decision.status]
            ),
        }
    return {
        "n_tool_calls": len(calls),
        "n_evidence": len(evidence),
        "frames_served": sum(len(c.timestamps) for c in calls),
        "tools_used": dict(Counter(c.tool.value for c in calls)),
        "rubric_tracks": tracks,
        "narrative": narrative,
    }


def _integer_score(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    if not numeric.is_integer():
        return None
    score = int(numeric)
    return score if 1 <= score <= 5 else None


def _decision_confidence(decisions: Sequence[RubricDecision]) -> float:
    return min((d.confidence for d in decisions), default=0.0)


def _fallback_summary(decisions: Sequence[RubricDecision]) -> str:
    failed = [d.rubric_id for d in decisions if d.status == "fail"]
    return "No rubric item failed." if not failed else "Failed rubric items: " + ", ".join(failed)
