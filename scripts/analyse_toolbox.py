#!/usr/bin/env python
"""Aggregate the new rubric/tool/evidence traces from an agentic run.

Usage:
    python scripts/analyse_toolbox.py --results results/agentic_....jsonl
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.metrics import correlations, mae  # noqa: E402
from eval.runner import join_with_gold  # noqa: E402


def trace_paths(results: Path) -> dict[str, str]:
    paths: dict[str, str] = {}
    for line in results.read_text().splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("video_id") and row.get("trace_path"):
            paths[str(row["video_id"])] = str(row["trace_path"])
    return paths


def load_traces(frame, results: Path) -> list[tuple[dict, dict]]:
    paths = trace_paths(results)
    pairs: list[tuple[dict, dict]] = []
    missing = 0
    for row in frame.to_dict("records"):
        raw = paths.get(str(row["video_id"]))
        if not raw:
            missing += 1
            continue
        path = Path(raw)
        if not path.is_absolute():
            path = ROOT / path
        try:
            pairs.append((row, json.loads(path.read_text())))
        except (OSError, json.JSONDecodeError):
            missing += 1
    if missing:
        print(f"warning: {missing} result rows had no readable trace")
    return pairs


def tool_report(pairs) -> None:
    calls: collections.Counter[str] = collections.Counter()
    frames: collections.Counter[str] = collections.Counter()
    failures: collections.Counter[str] = collections.Counter()
    for _, trace in pairs:
        for call in trace.get("tool_calls", []):
            tool = call.get("tool", "?")
            calls[tool] += 1
            frames[tool] += len(call.get("timestamps", []))
            failures[tool] += call.get("status") == "failed"
    print("\nTOOL USE")
    print(f"{'tool':20} {'calls':>7} {'frames':>8} {'failed':>8} {'frames/call':>12}")
    for tool, count in calls.most_common():
        print(f"{tool:20} {count:7} {frames[tool]:8} {failures[tool]:8} {frames[tool]/count:12.1f}")


def rubric_report(pairs) -> None:
    outcomes: collections.Counter[tuple[str, str]] = collections.Counter()
    missing_evidence = unknown_evidence = unknown_calls = 0
    chains: list[str] = []
    for _, trace in pairs:
        calls = {item["id"] for item in trace.get("tool_calls", [])}
        evidence = {item["id"]: item for item in trace.get("evidence", [])}
        for item in trace.get("evidence", []):
            unknown_calls += item.get("tool_call_id") not in calls
        for decision in trace.get("decisions", []):
            family = "SA" if str(decision.get("rubric_id", "")).startswith("S") else "PC"
            outcomes[(family, decision.get("status", "?"))] += 1
            ids = decision.get("evidence_ids") or []
            missing_evidence += not ids
            unknown_evidence += sum(eid not in evidence for eid in ids)
            if len(chains) < 12:
                chains.append(" -> ".join([
                    str(decision.get("rubric_id")),
                    *(decision.get("tool_call_ids") or []),
                    *ids,
                    str(decision.get("status")),
                ]))
    print("\nRUBRIC OUTCOMES")
    for family in ("SA", "PC"):
        values = ", ".join(f"{status}={outcomes[(family, status)]}" for status in ("pass", "fail", "not_shown"))
        print(f"{family}: {values}")
    print(f"trace-link problems: decisions_without_evidence={missing_evidence}, unknown_evidence={unknown_evidence}, unknown_tool_calls={unknown_calls}")
    print("example chains:")
    for chain in chains:
        print(f"  {chain}")


def accuracy_report(frame) -> None:
    usable = frame[frame["pred"].notna()]
    pred, gold = list(usable["pred"]), list(usable["pc"])
    values = correlations(pred, gold)
    print("\nACCURACY")
    print(f"n={len(usable)}/{len(frame)}  pearson={values.get('pearson')}  spearman={values.get('spearman')}  kendall={values.get('kendall')}  mae={mae(pred, gold)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=ROOT / "configs/default.yaml")
    parser.add_argument("--split", default="test")
    args = parser.parse_args()
    cfg = yaml.safe_load(args.config.read_text())
    dataset = VideoPhy2Dataset.from_config(cfg, split=args.split)
    frame = join_with_gold(args.results, dataset)
    pairs = load_traces(frame, args.results)
    print(f"loaded {len(frame)} result rows and {len(pairs)} traces")
    tool_report(pairs)
    rubric_report(pairs)
    accuracy_report(frame)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
