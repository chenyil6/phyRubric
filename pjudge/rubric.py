"""Rubric loading, decision validation and deterministic scoring."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .schema import RubricDecision

ROOT = Path(__file__).resolve().parents[1]
SEVERITY_CAP = {"fatal": 1, "core": 2, "major": 3, "minor": 4}


class RubricIndex:
    def __init__(self, dataset: str = "videophy2", root: Path = ROOT):
        self.dataset = dataset
        prompts = json.loads((root / "prompts" / f"{dataset}.json").read_text())
        self.by_caption: dict[str, dict[str, Any]] = {}
        self.by_id: dict[int, dict[str, Any]] = {}
        for entry in prompts:
            path = root / "rubrics" / dataset / f"caption_{entry['id']}.json"
            rubric = json.loads(path.read_text())
            validate_rubric(rubric)
            self.by_id[int(entry["id"])] = rubric
            for caption in [entry["caption"], *entry.get("aliases", [])]:
                previous = self.by_caption.setdefault(caption, rubric)
                if previous["id"] != rubric["id"]:
                    raise ValueError(f"caption alias maps to two rubrics: {caption!r}")
        self.policy = json.loads((root / "rubrics" / dataset / "_policy.json").read_text())

    def get(self, caption: str) -> dict[str, Any]:
        try:
            return self.by_caption[caption]
        except KeyError:
            raise KeyError(f"no {self.dataset} rubric or alias for caption {caption!r}") from None


def item_map(rubric: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for section in ("sa", "pc") for item in rubric[section]}


def expected_ids(rubric: dict[str, Any]) -> list[str]:
    return [item["id"] for section in ("sa", "pc") for item in rubric[section]]


def validate_rubric(rubric: dict[str, Any]) -> None:
    for key in ("id", "caption", "sa", "pc"):
        if key not in rubric:
            raise ValueError(f"rubric missing {key!r}")
    ids = expected_ids(rubric)
    if len(ids) != len(set(ids)):
        raise ValueError(f"rubric {rubric['id']} has duplicate item ids")
    for item in rubric["sa"]:
        if not str(item.get("id", "")).startswith("S") or item.get("weight") not in {"core", "minor"} or not item.get("check"):
            raise ValueError(f"invalid SA item {item!r}")
    for item in rubric["pc"]:
        if not str(item.get("id", "")).startswith("P") or item.get("severity") not in SEVERITY_CAP or not item.get("expect") or not item.get("fail"):
            raise ValueError(f"invalid PC item {item!r}")


def validate_decisions(rubric: dict[str, Any], decisions: Iterable[RubricDecision], require_complete: bool = True) -> list[str]:
    items = item_map(rubric)
    seen: dict[str, RubricDecision] = {}
    problems: list[str] = []
    for decision in decisions:
        if decision.rubric_id not in items:
            problems.append(f"unknown rubric id {decision.rubric_id}")
            continue
        if decision.rubric_id in seen:
            problems.append(f"duplicate decision for {decision.rubric_id}")
        seen[decision.rubric_id] = decision
        if decision.status not in {"pass", "fail", "not_shown"}:
            problems.append(f"invalid status {decision.status!r} for {decision.rubric_id}")
        if decision.source not in {"agent", "runtime_fallback"}:
            problems.append(f"invalid source {decision.source!r} for {decision.rubric_id}")
        if decision.rubric_id.startswith("S") and decision.status == "not_shown":
            problems.append(f"SA item {decision.rubric_id} cannot be not_shown")
        if not decision.explanation:
            problems.append(f"{decision.rubric_id} has no explanation")
    if require_complete:
        missing = [rid for rid in expected_ids(rubric) if rid not in seen]
        if missing:
            problems.append(f"missing decisions: {missing}")
    return problems


def deterministic_scores(rubric: dict[str, Any], decisions: Iterable[RubricDecision], recognisable: bool = True) -> tuple[int, int]:
    values = list(decisions)
    problems = validate_decisions(rubric, values)
    if problems:
        raise ValueError("; ".join(problems))
    by_id = {d.rubric_id: d for d in values}
    failed_sa = [item for item in rubric["sa"] if by_id[item["id"]].status == "fail"]
    if not failed_sa:
        sa = 5
    else:
        core = sum(item["weight"] == "core" for item in failed_sa)
        sa = 4 if core == 0 else 3 if core == 1 else (2 if recognisable else 1)
    failed_pc = [item for item in rubric["pc"] if by_id[item["id"]].status == "fail"]
    if not failed_pc:
        pc = 5
    else:
        pc = min(SEVERITY_CAP[item["severity"]] for item in failed_pc)
        heavy = sum(item["severity"] in {"fatal", "core", "major"} for item in failed_pc)
        pc = max(1, pc - max(0, heavy - 1))
    return sa, pc
