#!/usr/bin/env python3
"""Baseline 1: a generic VLM assigns one PC score in one fixed pass.

The model sees the caption and uniformly sampled video frames, but none of the
caption-specific rubrics.  This is the clean control for asking whether the
rubrics themselves add anything.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
import threading
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval.baselines import SinglePassBaseline  # noqa: E402
from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.metrics import summarise  # noqa: E402
from eval.runner import COST_FIELDS, join_with_gold, run_batch  # noqa: E402
from pjudge.backends.llm import LLMClient, LLMConfig  # noqa: E402


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def select_dataset(cfg: dict, split: str, n: int, seed: int, hard_only: bool):
    dataset = VideoPhy2Dataset.from_config(cfg, split=split).filter(
        has_video=True, hard=True if hard_only else None
    )
    return dataset.stratified_subset(n, seed=seed) if n else dataset


class PerThreadJudge:
    """Give each worker its own client and usage counters."""

    def __init__(self, factory):
        self.factory = factory
        self.local = threading.local()

    def __call__(self, sample):
        judge = getattr(self.local, "judge", None)
        if judge is None:
            judge = self.factory()
            self.local.judge = judge
        return judge(sample)


def write_summary(out_path: Path, dataset, run_stats: dict, seed: int) -> Path:
    frame = join_with_gold(out_path, dataset)
    usable = frame[frame["pred"].notna()].copy()
    report = summarise(
        pred=list(usable["pred"]),
        gold=list(usable["pc"]),
        confidence=list(usable["confidence"]),
        costs=usable[list(COST_FIELDS)].to_dict("records"),
        seed=seed,
    )
    report["n_rows_joined"] = int(len(frame))
    report["n_without_score"] = int(len(frame) - len(usable))
    if len(usable):
        delta = (usable["pred"] - usable["pc"]).abs()
        report["exact_accuracy"] = round(float((delta == 0).mean()), 6)
        report["within_one_accuracy"] = round(float((delta <= 1).mean()), 6)
    summary_path = out_path.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps({"baseline": "direct_vlm", "run": run_stats, "metrics": report}, indent=2)
    )
    return summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    parser.add_argument("--split", default="test")
    parser.add_argument("--n", type=int, default=200, help="0 means the full split")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--model", default=None)
    parser.add_argument("--n-frames", type=int, default=16)
    parser.add_argument("--hard-only", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    dataset = select_dataset(cfg, args.split, args.n, args.seed, args.hard_only)
    model = args.model or cfg["llm"]["default_model"]
    print(f"selected {len(dataset)} VideoPhy-2 videos; model={model}; frames={args.n_frames}")
    if args.check_only:
        return 0

    load_env()

    def factory():
        llm_cfg = copy.deepcopy(cfg["llm"])
        llm_cfg["default_model"] = model
        client = LLMClient(LLMConfig.from_dict(llm_cfg, "observer"), role="direct_vlm")
        baseline = SinglePassBaseline(client, n_frames=args.n_frames)

        def judge(sample):
            return baseline.judge(sample.video_path, sample.caption, sample.video_id).as_dict()

        return judge

    safe_model = re.sub(r"[^A-Za-z0-9._-]+", "_", model)
    out_path = args.out or ROOT / "results" / f"baseline_direct_vlm_{safe_model}_n{len(dataset)}_s{args.seed}.jsonl"
    stats = run_batch(
        list(dataset),
        PerThreadJudge(factory),
        out_path,
        workers=args.workers,
        resume=not args.no_resume,
        limit=args.limit,
    )
    summary = write_summary(out_path, dataset, stats.as_dict(), args.seed)
    print(f"results: {out_path}\nsummary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
