"""Agent 1: plan video observations and decide every fixed rubric item."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Literal, Sequence

from ..backends.llm import LLMClient
from ..prompts.rubric_agents import INSPECTION_SYSTEM, OBSERVE_TASK, PLAN_TASK
from ..rubric import expected_ids, item_map
from ..schema import RubricDecision, RubricEvidence, Tool, ToolCall
from .base import as_float, as_list, as_text, ask_json


@dataclass
class InspectionPlan:
    action: Literal["call_tool", "finish"]
    plan: str
    tool: Tool | None = None
    rubric_ids: list[str] | None = None
    arguments: dict[str, Any] | None = None


@dataclass
class ObservationResult:
    observation: str
    limitations: str
    confidence: float
    findings: list[RubricDecision]
    recognisable_attempt: bool
    raw_response: str


class RubricInspectionAgent:
    """The only agent that sees frames.

    It chooses the frame-selection tool and returns evidence-grounded item
    findings.  It never assigns an aggregate SA/PC score.
    """

    def __init__(self, client: LLMClient):
        self.client = client

    def plan(
        self,
        *,
        caption: str,
        duration: float,
        rubric: dict[str, Any],
        policy: dict[str, Any],
        decisions: Sequence[RubricDecision],
        evidence: Sequence[RubricEvidence],
        tool_calls: Sequence[ToolCall],
        round_no: int,
        max_rounds: int,
        frames_left: int,
    ) -> InspectionPlan:
        data = ask_json(
            self.client,
            INSPECTION_SYSTEM,
            PLAN_TASK.format(
                caption=caption,
                duration=duration,
                round_no=round_no,
                max_rounds=max_rounds,
                frames_left=frames_left,
                policy=json.dumps(policy, ensure_ascii=False),
                rubric=json.dumps(rubric, ensure_ascii=False),
                decisions=json.dumps([d.as_dict() for d in decisions], ensure_ascii=False),
                evidence=json.dumps([e.for_prompt() for e in evidence], ensure_ascii=False),
                tool_calls=json.dumps([t.for_prompt() for t in tool_calls], ensure_ascii=False),
            ),
        )
        action = as_text(data.get("action")).lower()
        if action == "finish":
            return InspectionPlan("finish", as_text(data.get("plan")))
        raw_call = data.get("tool_call")
        if not isinstance(raw_call, dict):
            raise ValueError("inspection plan has no tool_call object")
        try:
            tool = Tool(as_text(raw_call.get("name")))
        except ValueError as exc:
            raise ValueError(f"unknown inspection tool {raw_call.get('name')!r}") from exc
        known = set(expected_ids(rubric))
        ids = []
        for value in as_list(raw_call.get("rubric_ids")):
            rid = as_text(value)
            if rid in known and rid not in ids:
                ids.append(rid)
        if not ids:
            raise ValueError("tool call must name at least one rubric item")
        arguments = raw_call.get("arguments")
        if not isinstance(arguments, dict):
            raise ValueError("tool call arguments must be an object")
        return InspectionPlan(
            "call_tool",
            as_text(data.get("plan")) or f"inspect {', '.join(ids)}",
            tool,
            ids,
            arguments,
        )

    def observe(
        self,
        *,
        caption: str,
        rubric: dict[str, Any],
        policy: dict[str, Any],
        call: ToolCall,
        frames: list[tuple[float, Any]],
        description: str,
        prior_evidence: Sequence[RubricEvidence],
    ) -> ObservationResult:
        items = item_map(rubric)
        selected = [items[rid] for rid in call.rubric_ids]
        timestamps = [timestamp for timestamp, _ in frames]
        data = ask_json(
            self.client,
            INSPECTION_SYSTEM,
            OBSERVE_TASK.format(
                caption=caption,
                tool_call=json.dumps(call.for_prompt(), ensure_ascii=False),
                timestamps=", ".join(f"{t:.3f}s" for t in timestamps),
                description=description,
                items=json.dumps(selected, ensure_ascii=False),
                policy=json.dumps(policy, ensure_ascii=False),
                prior_evidence=json.dumps(
                    [e.for_prompt() for e in prior_evidence if set(e.rubric_ids) & set(call.rubric_ids)],
                    ensure_ascii=False,
                ),
            ),
            images=[image for _, image in frames],
        )
        findings: list[RubricDecision] = []
        seen: set[str] = set()
        for raw in as_list(data.get("findings")):
            if not isinstance(raw, dict):
                continue
            rid = as_text(raw.get("rubric_id"))
            status = as_text(raw.get("status")).lower()
            explanation = as_text(raw.get("explanation"))
            if rid not in call.rubric_ids or rid in seen or not explanation:
                continue
            if rid.startswith("S") and status not in {"pass", "fail"}:
                continue
            if rid.startswith("P") and status not in {"pass", "fail", "not_shown"}:
                continue
            findings.append(
                RubricDecision(
                    rubric_id=rid,
                    status=status,  # type: ignore[arg-type]
                    evidence_ids=[],
                    explanation=explanation,
                    confidence=as_float(raw.get("confidence"), 0.5),
                )
            )
            seen.add(rid)
        recognisable = data.get("recognisable_attempt")
        if not isinstance(recognisable, bool):
            recognisable = True
        return ObservationResult(
            observation=as_text(data.get("observation")) or "The supplied frames were inspected.",
            limitations=as_text(data.get("limitations")),
            confidence=as_float(data.get("confidence"), 0.5),
            findings=findings,
            recognisable_attempt=recognisable,
            raw_response=json.dumps(data, ensure_ascii=False),
        )
