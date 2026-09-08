"""Offline contract tests for the two-agent rubric runtime."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pjudge.agents.inspection import RubricInspectionAgent
from pjudge.agents.judge import ScoringFeedbackAgent
from pjudge.backends.llm import LLMConfig, LLMResponse, Usage
from pjudge.rubric import RubricIndex, deterministic_scores, validate_decisions
from pjudge.runtime import JudgeRuntime, RuntimeConfig
from pjudge.schema import RubricDecision, RubricEvidence


RUBRIC = {
    "id": 999,
    "caption": "A ball hits a wall and rebounds.",
    "sa": [
        {"id": "S1", "weight": "core", "check": "A ball is present."},
        {"id": "S2", "weight": "minor", "check": "A wall is present."},
    ],
    "pc": [
        {"id": "P1", "severity": "core", "expect": "The rebound follows contact.", "fail": "It reverses before contact."},
        {"id": "P2", "severity": "major", "expect": "The wall remains rigid.", "fail": "The wall visibly deforms."},
        {"id": "P3", "severity": "minor", "expect": "The ball keeps its colour.", "fail": "Its colour visibly changes."},
    ],
}

POLICY = {"labelling_instructions": ["Judge visible evidence only."]}


class StaticRubricIndex:
    policy = POLICY

    def get(self, caption):
        assert caption == RUBRIC["caption"]
        return RUBRIC


class ScriptedClient:
    def __init__(self, role: str, responses: list[dict]):
        self.role = role
        self.responses = list(responses)
        self.usage = Usage()
        self.cfg = LLMConfig(model=f"test-{role}", base_url="http://unused", api_key="x")
        self.seen: list[dict] = []

    @property
    def token_param(self):
        return "max_tokens"

    def ask(self, prompt, system=None, images=None, json_mode=False, **kwargs):
        self.seen.append({"prompt": prompt, "system": system, "n_images": len(images or [])})
        self.usage.add(Usage(calls=1, prompt_tokens=10, completion_tokens=4, images=len(images or [])))
        payload = self.responses.pop(0)
        return LLMResponse(json.dumps(payload), self.cfg.model, self.role, Usage(calls=1), False)


def make_video(path: Path, n: int = 12) -> Path:
    writer = cv2.VideoWriter(str(path), cv2.VideoWriter_fourcc(*"MJPG"), 6.0, (64, 48))
    assert writer.isOpened()
    for i in range(n):
        frame = np.zeros((48, 64, 3), dtype=np.uint8)
        cv2.circle(frame, (5 + i * 4, 24), 4, (0, 0, 255), -1)
        writer.write(frame)
    writer.release()
    return path


def inspection_script():
    return [
        # Runtime replaces this targeted first call with the mandatory overview.
        {"action": "call_tool", "plan": "look at impact", "tool_call": {"name": "inspect_clip", "rubric_ids": ["P1"], "arguments": {"span": {"start": 0, "end": 1}, "n_frames": 4}}},
        {"observation": "The ball and wall are visible across the overview.", "limitations": "Impact timing needs a denser view.", "confidence": 0.8, "recognisable_attempt": True, "findings": [
            {"rubric_id": "S1", "status": "pass", "explanation": "A red ball is visible.", "confidence": 0.9},
            {"rubric_id": "S2", "status": "pass", "explanation": "A wall is visible.", "confidence": 0.9},
            {"rubric_id": "P2", "status": "pass", "explanation": "The wall remains unchanged.", "confidence": 0.8},
            {"rubric_id": "P3", "status": "pass", "explanation": "The ball stays red.", "confidence": 0.8},
        ]},
        {"action": "call_tool", "plan": "resolve contact timing", "tool_call": {"name": "inspect_clip", "rubric_ids": ["P1"], "arguments": {"span": {"start": 0.5, "end": 1.5}, "n_frames": 6}}},
        {"observation": "The ball reverses before touching the wall.", "limitations": "", "confidence": 0.95, "recognisable_attempt": True, "findings": [
            {"rubric_id": "P1", "status": "fail", "explanation": "Reversal occurs before contact.", "confidence": 0.95}
        ]},
        {"action": "finish", "plan": "all items now have evidence"},
    ]


def judge_script(sa=5, pc=5):
    return [{"sa_score": sa, "pc_score": pc, "confidence": 0.9, "summary": "The depicted scene is semantically correct, but contact timing fails.", "feedback": [
        {"rubric_id": "X", "evidence_ids": ["E999"], "problem": "invented", "suggested_fix": "invented"},
        {"rubric_id": "P1", "evidence_ids": ["E2"], "problem": "The ball turns early.", "suggested_fix": "Make the reversal begin on the wall-contact frame."}
    ], "trace_summary": "P1 was resolved by a dense clip after the overview."}]


def test_runtime_records_tool_evidence_decision_chain(tmp_path: Path):
    inspection_client = ScriptedClient("inspection", inspection_script())
    judge_client = ScriptedClient("judge", judge_script())
    runtime = JudgeRuntime(
        RubricInspectionAgent(inspection_client),
        ScoringFeedbackAgent(judge_client),
        StaticRubricIndex(),
        RuntimeConfig(max_rounds=6, max_frames=30, overview_frames=5, save_artifacts=True),
        runs_dir=tmp_path / "runs",
    )
    result = runtime.judge(make_video(tmp_path / "tiny.avi"), RUBRIC["caption"], "case")

    assert result.report.sa_score == 5
    assert result.report.pc_score == 2
    assert "runtime enforced deterministic" in result.report.score_note
    assert [call["id"] for call in result.trace["tool_calls"]] == ["T1", "T2"]
    assert result.trace["tool_calls"][0]["tool"] == "overview"
    assert result.trace["tool_calls"][0]["rubric_ids"] == ["S1", "S2", "P1", "P2", "P3"]
    assert [item["id"] for item in result.trace["evidence"]] == ["E1", "E2"]
    p1 = next(item for item in result.trace["decisions"] if item["rubric_id"] == "P1")
    assert p1["tool_call_ids"] == ["T2"]
    assert p1["evidence_ids"] == ["E2"]
    assert p1["status"] == "fail"
    assert result.report.feedback[0].evidence_ids == ["E2"]
    assert result.trace_path and result.trace_path.exists()
    assert result.trace["evidence"][0]["artifacts"]
    assert all(str(tmp_path) not in item["prompt"] for item in inspection_client.seen)
    assert str(tmp_path) not in judge_client.seen[0]["prompt"]
    assert result.report.cost.llm_calls == 6  # 3 plans + 2 observations + final report
    assert inspection_client.seen[1]["n_images"] > 0
    assert judge_client.seen[0]["n_images"] == 0


def test_scoring_and_decision_validation():
    decisions = [
        RubricDecision("S1", "pass", ["E1"], "seen"),
        RubricDecision("S2", "fail", ["E1"], "not seen"),
        RubricDecision("P1", "pass", ["E1"], "okay"),
        RubricDecision("P2", "fail", ["E1"], "wall bends"),
        RubricDecision("P3", "fail", ["E1"], "colour changes"),
    ]
    assert validate_decisions(RUBRIC, decisions) == []
    assert deterministic_scores(RUBRIC, decisions) == (4, 3)


def test_sa_not_shown_is_rejected():
    decisions = [RubricDecision("S1", "not_shown", ["E1"], "missing")]
    problems = validate_decisions(RUBRIC, decisions, require_complete=False)
    assert problems == ["SA item S1 cannot be not_shown"]


def test_all_videophy_rubrics_load():
    index = RubricIndex("videophy2")
    assert len(index.by_id) == 591
    assert len(index.by_caption) >= len(index.by_id)


def test_budget_fallback_is_explicitly_marked():
    decisions = {"S1": RubricDecision("S1", "pass", ["E1"], "seen")}
    evidence = [RubricEvidence("E1", "T1", ["S1", "S2", "P1", "P2", "P3"], "overview")]
    JudgeRuntime._complete_missing(RUBRIC, decisions, evidence)
    assert decisions["S1"].source == "agent"
    assert all(decisions[rid].source == "runtime_fallback" for rid in ("S2", "P1", "P2", "P3"))


def main() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as directory:
        test_runtime_records_tool_evidence_decision_chain(Path(directory))
    test_scoring_and_decision_validation()
    test_sa_not_shown_is_rejected()
    test_all_videophy_rubrics_load()
    test_budget_fallback_is_explicitly_marked()
    print("ALL RUBRIC RUNTIME TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
