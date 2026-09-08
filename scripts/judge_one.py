#!/usr/bin/env python
"""Judge one VideoPhy-2 video and print rubric decisions and trace links.

    python scripts/judge_one.py --video clip.mp4 --caption "a ball bounces"

Reads .env from the project root if the key variable is not already exported.
The full trace lands in runs/<video_id>/trace.json.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pjudge.runtime import JudgeRuntime  # noqa: E402


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--caption", required=True)
    ap.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    ap.add_argument("--video-id", default=None)
    ap.add_argument("--dataset", default="videophy2")
    ap.add_argument("--model", default=None, help="override every role's model")
    ap.add_argument("--max-rounds", type=int, default=None)
    ap.add_argument("--max-frames", type=int, default=None)
    args = ap.parse_args()

    load_env()
    cfg = yaml.safe_load(Path(args.config).read_text())
    if args.model:
        cfg["llm"]["default_model"] = args.model
        cfg["llm"]["roles"] = {k: None for k in cfg["llm"].get("roles", {})}
    if args.max_rounds is not None:
        cfg.setdefault("budget", {})["max_rounds"] = args.max_rounds
    if args.max_frames is not None:
        cfg.setdefault("budget", {})["max_frames"] = args.max_frames

    judge = JudgeRuntime.from_config(cfg, dataset=args.dataset)
    result = judge.judge(args.video, args.caption, video_id=args.video_id)
    report, trace = result.report, result.trace

    print("=" * 78)
    print(f"video   : {args.video}")
    print(f"caption : {args.caption}")
    print(f"duration: {trace['video_meta']['duration']}s @ {trace['video_meta']['fps']}fps")
    print("=" * 78)

    print("\n--- tool calls and evidence ---")
    evidence = {item["id"]: item for item in trace["evidence"]}
    for call in trace["tool_calls"]:
        print(
            f"[{call['id']}] {call['tool']} rubrics={call['rubric_ids']} "
            f"frames={len(call['timestamps'])} status={call['status']}"
        )
        for item in evidence.values():
            if item["tool_call_id"] == call["id"]:
                print(f"    [{item['id']}] {item['observation'][:500]}")

    print("\n--- rubric decisions ---")
    for decision in trace["decisions"]:
        chain = " -> ".join(
            [decision["rubric_id"], *decision["tool_call_ids"], *decision["evidence_ids"], decision["status"]]
        )
        print(f"{chain}: {decision['explanation']}")

    print("\n--- scores and feedback ---")
    print(f"SA={report.sa_score}/5  PC={report.pc_score}/5  confidence={report.confidence}")
    for item in report.feedback:
        print(f"[{item.rubric_id}] {item.problem}")
        print(f"    fix: {item.suggested_fix}  evidence={item.evidence_ids}")
    print(f"\nsummary: {report.summary}")
    if report.score_note:
        print(f"score audit: {report.score_note}")
    if report.error:
        print(f"fallback: {report.error}")
    print(f"\ncost: {report.cost.as_dict()}")
    print(f"trace: {result.trace_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
