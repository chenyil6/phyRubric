"""Python runtime for the two-agent, rubric-driven physical judge."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from .agents.inspection import InspectionPlan, RubricInspectionAgent
from .agents.judge import ScoringFeedbackAgent, build_trace_summary
from .backends.llm import build_clients
from .perception.frames import FrameServer, save_frames
from .rubric import RubricIndex, deterministic_scores, expected_ids, validate_decisions
from .schema import Feedback, InspectionResult, JudgeReport, JudgeResult, ObservationCost, RubricDecision, RubricEvidence, Tool, ToolCall, validate_trace_links
from .tools import VideoToolbox


@dataclass
class RuntimeConfig:
    max_rounds: int = 12
    max_frames: int = 120
    max_output_tokens: int = 60_000
    max_frames_per_call: int = 32
    overview_frames: int = 12
    save_artifacts: bool = True

    def __post_init__(self) -> None:
        if self.max_rounds < 2:
            raise ValueError("max_rounds must be at least 2 (the policy requires two looks)")
        if self.max_frames < 2:
            raise ValueError("max_frames must be at least 2")
        if self.max_frames_per_call < 1:
            raise ValueError("max_frames_per_call must be positive")

    @classmethod
    def from_dict(cls, cfg: dict[str, Any], perception: dict[str, Any]) -> "RuntimeConfig":
        return cls(max_rounds=int(cfg.get("max_rounds", 12)), max_frames=int(cfg.get("max_frames", 120)), max_output_tokens=int(cfg.get("max_output_tokens", 60_000)), max_frames_per_call=int(perception.get("max_frames_per_observation", 32)), overview_frames=int(perception.get("overview_max_frames", 12)), save_artifacts=bool(perception.get("save_artifacts", True)))


class JudgeRuntime:
    """Runs the Active Evidence Agent, then the Scoring and Feedback Agent."""

    def __init__(self, inspection: RubricInspectionAgent, judge: ScoringFeedbackAgent, rubric_index: RubricIndex, config: RuntimeConfig | None = None, runs_dir: str | Path = "runs", perception: dict[str, Any] | None = None, max_decode_frames: int = 900):
        self.inspection = inspection
        self.judge_agent = judge
        self.rubric_index = rubric_index
        self.config = config or RuntimeConfig()
        self.runs_dir = Path(runs_dir)
        self.perception = perception or {}
        self.max_decode_frames = max_decode_frames

    @classmethod
    def from_config(cls, cfg: dict[str, Any], dataset: str = "videophy2") -> "JudgeRuntime":
        clients = build_clients(cfg["llm"], roles=("inspection", "judge"))
        perception = cfg.get("perception", {})
        return cls(inspection=RubricInspectionAgent(clients["inspection"]), judge=ScoringFeedbackAgent(clients["judge"]), rubric_index=RubricIndex(dataset), config=RuntimeConfig.from_dict(cfg.get("budget", {}), perception), runs_dir=cfg.get("paths", {}).get("runs_dir", "runs"), perception=perception)

    def judge(self, video_path: str | Path, caption: str, video_id: str | None = None, rubric: dict[str, Any] | None = None, write_trace: bool = True) -> JudgeResult:
        started = time.time()
        video_id = video_id or Path(video_path).stem
        rubric = rubric or self.rubric_index.get(caption)
        policy = self.rubric_index.policy
        run_dir = self.runs_dir / _safe_name(video_id)
        run_dir.mkdir(parents=True, exist_ok=True)
        usage0 = self._usage_snapshot()
        server = FrameServer(video_path, max_decode_frames=self.max_decode_frames)
        toolbox = VideoToolbox(server, overview_long_side=int(self.perception.get("overview_long_side", 512)), clip_long_side=int(self.perception.get("clip_long_side", 768)), region_long_side=int(self.perception.get("zoom_long_side", 1024)))
        calls: list[ToolCall] = []
        evidence: list[RubricEvidence] = []
        decisions: dict[str, RubricDecision] = {}
        rounds: list[dict[str, Any]] = []
        recognisable = True

        for round_no in range(1, self.config.max_rounds + 1):
            frames_left = self.config.max_frames - sum(len(call.timestamps) for call in calls)
            if frames_left < 2 or self._output_tokens(usage0) >= self.config.max_output_tokens:
                break
            try:
                plan = self.inspection.plan(caption=caption, duration=server.duration, rubric=rubric, policy=policy, decisions=list(decisions.values()), evidence=evidence, tool_calls=calls, round_no=round_no, max_rounds=self.config.max_rounds, frames_left=frames_left)
                plan_error = ""
            except Exception as exc:
                plan = self._fallback_plan(rubric, decisions, calls, server.duration)
                plan_error = f"{type(exc).__name__}: {exc}"

            missing = [rid for rid in expected_ids(rubric) if rid not in decisions]
            if plan.action == "finish":
                completed_calls = sum(call.status == "completed" for call in calls)
                if not missing and completed_calls >= 2:
                    rounds.append({"round": round_no, "plan": plan.plan, "action": "finish", "incomplete_ids": []})
                    break
                reason = "finish requested before two successful observations" if not missing else f"finish requested with unresolved items: {missing}"
                plan_error = f"{plan_error}; {reason}".strip("; ")
                plan = self._fallback_plan(rubric, decisions, calls, server.duration)

            assert plan.tool is not None and plan.rubric_ids and plan.arguments is not None
            if not calls:
                # The first pass is always a whole-video orientation and is linked
                # to every item.  Besides making the trace complete, this prevents
                # an agent from overlooking an item by targeting too early.
                plan = InspectionPlan(
                    "call_tool",
                    "Mandatory whole-video orientation before targeted inspection.",
                    Tool.OVERVIEW,
                    expected_ids(rubric),
                    {"n_frames": self.config.overview_frames},
                )
            arguments = dict(plan.arguments)
            self._cap_frame_request(arguments, frames_left)
            call = ToolCall(id=f"T{len(calls) + 1}", tool=plan.tool, rubric_ids=list(plan.rubric_ids), arguments=arguments, reason=plan.plan, round=round_no)
            calls.append(call)
            entry: dict[str, Any] = {"round": round_no, "plan": plan.plan, "plan_error": plan_error}
            try:
                output = toolbox.execute(call)
                call.status = "completed"
                call.timestamps = output.timestamps
                if self.config.save_artifacts:
                    call.artifacts = save_frames(output.frames, run_dir / "frames", call.id, jpeg_quality=int(self.perception.get("jpeg_quality", 92)))
                observed = self.inspection.observe(caption=caption, rubric=rubric, policy=policy, call=call, frames=output.frames, description=output.description, prior_evidence=evidence)
                ev = RubricEvidence(id=f"E{len(evidence) + 1}", tool_call_id=call.id, rubric_ids=list(call.rubric_ids), observation=observed.observation, timestamps=call.timestamps, artifacts=call.artifacts, confidence=observed.confidence, limitations=observed.limitations, raw_response=observed.raw_response)
                evidence.append(ev)
                if call.tool is Tool.OVERVIEW:
                    recognisable = observed.recognisable_attempt
                for finding in observed.findings:
                    previous = decisions.get(finding.rubric_id)
                    linked = list(previous.evidence_ids) if previous else []
                    if ev.id not in linked:
                        linked.append(ev.id)
                    finding.evidence_ids = linked
                    decisions[finding.rubric_id] = finding
                entry.update({"tool_call": call.as_dict(), "evidence": ev.as_dict(), "findings": [f.as_dict() for f in observed.findings]})
            except Exception as exc:
                call.status = "failed"
                call.error = f"{type(exc).__name__}: {exc}"
                entry.update({"tool_call": call.as_dict(), "error": call.error})
            rounds.append(entry)

        self._complete_missing(rubric, decisions, evidence)
        inspection = InspectionResult(tool_calls=calls, evidence=evidence, decisions=[decisions[rid] for rid in expected_ids(rubric)], recognisable_attempt=recognisable, incomplete_ids=[])
        problems = validate_decisions(rubric, inspection.decisions)
        problems.extend(validate_trace_links(calls, evidence, inspection.decisions))
        if problems:
            raise ValueError("invalid inspection trace: " + "; ".join(problems))
        cost = self._fill_cost(ObservationCost(), len(rounds), calls, usage0)
        try:
            report = self.judge_agent.finalize(video_id=video_id, caption=caption, rubric=rubric, policy=policy, inspection=inspection, cost=cost)
        except Exception as exc:
            report = self._fallback_report(video_id, rubric, inspection, cost, exc)
        self._fill_cost(cost, len(rounds), calls, usage0)
        trace = {"schema_version": 2, "architecture": "active_evidence_agent + scoring_feedback_agent", "video_id": video_id, "video_path": str(video_path), "caption": caption, "rubric": rubric, "policy": policy, "video_meta": server.meta.as_dict(), "recognisable_attempt": recognisable, "models": {"inspection": self.inspection.client.cfg.model, "judge": self.judge_agent.client.cfg.model}, "rounds": rounds, "tool_calls": [call.as_dict() for call in calls], "evidence": [ev.as_dict() for ev in evidence], "decisions": self._decisions_with_tools(inspection.decisions, evidence), "scores": {"sa": report.sa_score, "pc": report.pc_score}, "feedback": [item.as_dict() for item in report.feedback], "trace_summary": report.trace_summary, "report": report.as_dict(), "wall_seconds": round(time.time() - started, 2)}
        trace_path: Path | None = None
        if write_trace:
            trace_path = run_dir / "trace.json"
            trace_path.write_text(json.dumps(trace, indent=2, ensure_ascii=False))
        return JudgeResult(report=report, trace=trace, trace_path=trace_path)

    def _fallback_plan(self, rubric: dict[str, Any], decisions: dict[str, RubricDecision], calls: Sequence[ToolCall], duration: float) -> InspectionPlan:
        missing = [rid for rid in expected_ids(rubric) if rid not in decisions]
        if not calls:
            return InspectionPlan("call_tool", "Fallback whole-video overview.", Tool.OVERVIEW, expected_ids(rubric), {"n_frames": self.config.overview_frames})
        return InspectionPlan("call_tool", "Fallback full-video inspection for unresolved items.", Tool.INSPECT_CLIP, missing or expected_ids(rubric), {"span": {"start": 0.0, "end": duration}, "n_frames": min(self.config.max_frames_per_call, 16)})

    def _cap_frame_request(self, arguments: dict[str, Any], frames_left: int) -> None:
        cap = min(self.config.max_frames_per_call, frames_left)
        if "timestamps" in arguments and isinstance(arguments["timestamps"], list):
            arguments["timestamps"] = arguments["timestamps"][:cap]
        else:
            try:
                requested = int(arguments.get("n_frames", 8))
            except (TypeError, ValueError):
                requested = 8
            arguments["n_frames"] = max(1, min(requested, cap))

    @staticmethod
    def _complete_missing(rubric: dict[str, Any], decisions: dict[str, RubricDecision], evidence: Sequence[RubricEvidence]) -> None:
        if not evidence:
            raise RuntimeError("inspection produced no evidence")
        for rid in expected_ids(rubric):
            if rid in decisions:
                continue
            linked = next((ev for ev in evidence if rid in ev.rubric_ids), evidence[0])
            decisions[rid] = RubricDecision(rubric_id=rid, status="fail" if rid.startswith("S") else "not_shown", evidence_ids=[linked.id], explanation="The available observations did not verify this semantic requirement." if rid.startswith("S") else "The required moment or precondition was not visible in the available observations.", confidence=0.0, source="runtime_fallback")

    @staticmethod
    def _decisions_with_tools(decisions: Sequence[RubricDecision], evidence: Sequence[RubricEvidence]) -> list[dict[str, Any]]:
        by_id = {ev.id: ev for ev in evidence}
        out = []
        for decision in decisions:
            call_ids: list[str] = []
            for eid in decision.evidence_ids:
                ev = by_id.get(eid)
                if ev and ev.tool_call_id not in call_ids:
                    call_ids.append(ev.tool_call_id)
            out.append(decision.as_dict(call_ids))
        return out

    @staticmethod
    def _fallback_report(video_id: str, rubric: dict[str, Any], inspection: InspectionResult, cost: ObservationCost, exc: Exception) -> JudgeReport:
        sa, pc = deterministic_scores(rubric, inspection.decisions, inspection.recognisable_attempt)
        failed = [d for d in inspection.decisions if d.status == "fail"]
        return JudgeReport(video_id=video_id, rubric_id=rubric["id"], sa_score=sa, pc_score=pc, confidence=min((d.confidence for d in inspection.decisions), default=0.0), decisions=inspection.decisions, feedback=[Feedback(d.rubric_id, d.evidence_ids, d.explanation, "Review the failed rubric item and its cited frames.") for d in failed], summary="No rubric item failed." if not failed else "Failed rubric items: " + ", ".join(d.rubric_id for d in failed), trace_summary=build_trace_summary(inspection.tool_calls, inspection.evidence, inspection.decisions), cost=cost, error=f"reporting agent fallback: {type(exc).__name__}: {exc}")

    def _usage_snapshot(self) -> dict[str, int]:
        total = {"prompt_tokens": 0, "completion_tokens": 0, "calls": 0, "cache_hits": 0}
        for client in (self.inspection.client, self.judge_agent.client):
            for key in total:
                total[key] += getattr(client.usage, key)
        return total

    def _output_tokens(self, baseline: dict[str, int]) -> int:
        return self._usage_snapshot()["completion_tokens"] - baseline["completion_tokens"]

    def _fill_cost(self, cost: ObservationCost, rounds: int, calls: Sequence[ToolCall], baseline: dict[str, int]) -> ObservationCost:
        now = self._usage_snapshot()
        cost.rounds = rounds
        cost.frames = sum(len(call.timestamps) for call in calls)
        cost.prompt_tokens = now["prompt_tokens"] - baseline["prompt_tokens"]
        cost.completion_tokens = now["completion_tokens"] - baseline["completion_tokens"]
        cost.llm_calls = now["calls"] - baseline["calls"]
        cost.cache_hits = now["cache_hits"] - baseline["cache_hits"]
        return cost


PhysicalJudge = JudgeRuntime


def _safe_name(value: str, max_len: int = 140) -> str:
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in value)
    return safe[:max_len] or "video"


__all__ = ["JudgeRuntime", "PhysicalJudge", "RuntimeConfig"]
