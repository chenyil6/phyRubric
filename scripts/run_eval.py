#!/usr/bin/env python
"""Evaluate a judge on VideoPhy-2 and print the results row.

    # the passive baseline we have to beat
    python scripts/run_eval.py --judge single_pass --n 200

    # how much of that is just prompt predictability
    python scripts/run_eval.py --judge caption_only --n 200

    # the agentic judge
    python scripts/run_eval.py --judge agentic --n 200 --workers 4

Results are appended to a jsonl, so a killed run resumes where it stopped.

Thread safety: every worker gets its OWN judge and its own LLMClient. The clients
accumulate usage counters and the cost of a single video is read from them, so
sharing one client across threads would attribute other videos' tokens to this
one. The disk cache is shared and that is fine -- writes are atomic.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import sys
import threading
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval.baselines import CaptionOnlyBaseline, SinglePassBaseline  # noqa: E402
from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.metrics import correlations, summarise  # noqa: E402
from eval.runner import COST_FIELDS, join_with_gold, run_batch  # noqa: E402
from pjudge.backends.llm import LLMClient, LLMConfig  # noqa: E402
from pjudge.runtime import JudgeRuntime  # noqa: E402


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


class PerThreadJudge:
    """Lazily builds one judge per worker thread.

    The factory is called once per thread, not once per video, so per-video cost
    still comes out of a counter only this thread touches.
    """

    def __init__(self, factory):
        self._factory = factory
        self._local = threading.local()

    def __call__(self, sample):
        judge = getattr(self._local, "judge", None)
        if judge is None:
            judge = self._factory()
            self._local.judge = judge
        return judge(sample)


def make_single_pass(cfg: dict, model: str | None, n_frames: int):
    def factory():
        llm = copy.deepcopy(cfg["llm"])
        if model:
            llm["default_model"] = model
        client = LLMClient(LLMConfig.from_dict(llm, "single_pass"), role="baseline")
        baseline = SinglePassBaseline(client, n_frames=n_frames)

        def judge(sample):
            r = baseline.judge(sample.video_path, sample.caption, sample.video_id)
            return r.as_dict()

        return judge

    return factory


def make_caption_only(cfg: dict, model: str | None):
    def factory():
        llm = copy.deepcopy(cfg["llm"])
        if model:
            llm["default_model"] = model
        client = LLMClient(LLMConfig.from_dict(llm, "caption_only"), role="baseline")
        baseline = CaptionOnlyBaseline(client)

        def judge(sample):
            r = baseline.judge(sample.video_path, sample.caption, sample.video_id)
            return r.as_dict()

        return judge

    return factory


def make_agentic(cfg: dict, model: str | None):
    def factory():
        local_cfg = copy.deepcopy(cfg)
        if model:
            local_cfg["llm"]["default_model"] = model
            local_cfg["llm"]["roles"] = {k: None for k in local_cfg["llm"].get("roles", {})}
        judge_obj = JudgeRuntime.from_config(local_cfg)

        def judge(sample):
            result = judge_obj.judge(sample.video_path, sample.caption, sample.video_id)
            report = result.report
            out = report.as_dict()
            out.update(
                {
                    "trace_path": str(result.trace_path) if result.trace_path else "",
                    "frames": report.cost.frames,
                    "rounds": report.cost.rounds,
                    "prompt_tokens": report.cost.prompt_tokens,
                    "completion_tokens": report.cost.completion_tokens,
                    "llm_calls": report.cost.llm_calls,
                    "cache_hits": report.cost.cache_hits,
                }
            )
            return out

        return judge

    return factory


JUDGES = {
    "single_pass": make_single_pass,
    "caption_only": make_caption_only,
    "agentic": make_agentic,
}


def _fmt(value, spec: str = ".3f") -> str:
    """Never print a fabricated zero for an undefined metric."""
    return "n/a" if value is None else format(value, spec)


def _headline(report: dict) -> str:
    """The row that goes in the results table. Full detail lands in the json."""
    ci = report.get("pearson_ci") or {}
    cost = report.get("cost") or {}
    buckets = cost.get("buckets") or []
    lines = [
        f"n         : {report.get('n_scored')}/{report.get('n_total')} scored"
        f"  (coverage {_fmt(report.get('coverage'), '.3f')},"
        f" {report.get('n_abstained')} abstained,"
        f" {report.get('n_without_score', 0)} no-score,"
        f" {report.get('n_imputed', 0)} imputed)",
        f"pearson   : {_fmt(report.get('pearson'))}"
        f"  95% CI [{_fmt(ci.get('lo'))}, {_fmt(ci.get('hi'))}]"
        + (f"   excl-imputed {_fmt(report.get('pearson_excl_imputed'))}"
           f" (n={report.get('n_excl_imputed')})" if report.get('n_imputed') else ""),
        f"spearman  : {_fmt(report.get('spearman'))}"
        f"   kendall {_fmt(report.get('kendall'))}",
        f"mae/rmse  : {_fmt(report.get('mae'))} / {_fmt(report.get('rmse'))}",
        f"binary@{_fmt(report.get('threshold'), '.1f')}: "
        f"auroc {_fmt(report.get('auroc'))}"
        f"  ap {_fmt(report.get('average_precision'))}"
        f"  f1 {_fmt(report.get('f1_at_threshold'))}"
        f"  best_f1 {_fmt(report.get('best_f1'))} @ {_fmt(report.get('best_threshold'), '.1f')}"
        f"  ({report.get('n_pos')}+/{report.get('n_neg')}-)",
        f"selective : aurc {_fmt(report.get('aurc'))}"
        f"  risk@cov " + ", ".join(
            f"{k}:{_fmt(v)}" for k, v in sorted((report.get("risk_at") or {}).items())
        ),
    ]
    if buckets:
        lines.append(
            "cost      : "
            + " | ".join(
                f"{b.get('mean_cost', 0):.0f}{cost.get('key', '')}"
                f"->r={_fmt(b.get('pearson'), '.2f')}(n={b.get('n')})"
                for b in buckets
            )
        )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", choices=sorted(JUDGES), required=True)
    ap.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    ap.add_argument("--split", default="test")
    ap.add_argument("--n", type=int, default=200, help="stratified subset size; 0 = all")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--model", default=None, help="override the model for every role")
    ap.add_argument("--n-frames", type=int, default=16, help="single_pass only")
    ap.add_argument("--hard-only", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-resume", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    load_env()
    cfg = yaml.safe_load(Path(args.config).read_text())

    ds = VideoPhy2Dataset.from_config(cfg, split=args.split)
    print(f"loaded {len(ds)} rows; {len(ds.missing)} have no local video file")
    ds = ds.filter(has_video=True, hard=True if args.hard_only else None)
    if args.n:
        ds = ds.stratified_subset(args.n, seed=args.seed)
    print(f"evaluating {len(ds)} videos with judge={args.judge} "
          f"model={args.model or cfg['llm']['default_model']}")

    tag = f"{args.judge}_{args.model or cfg['llm']['default_model']}_n{len(ds)}_s{args.seed}"
    out_path = Path(args.out or ROOT / "results" / f"{tag}.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    factory = (
        JUDGES[args.judge](cfg, args.model, args.n_frames)
        if args.judge == "single_pass"
        else JUDGES[args.judge](cfg, args.model)
    )
    stats = run_batch(
        list(ds),
        PerThreadJudge(factory),
        out_path,
        workers=args.workers,
        resume=not args.no_resume,
        limit=args.limit,
    )
    print(f"\nrun: {stats.as_dict()}")

    frame = join_with_gold(out_path, ds)
    # A row is usable when it carries a score. Filtering on `error` being empty
    # would also discard rows whose only problem was a soft note -- a clamped or
    # prose-recovered score -- silently shrinking the sample. Rows with no score
    # at all are counted, not hidden: abstentions belong in coverage, and crashes
    # belong in the failure count.
    usable = frame[frame["pred"].notna()].copy()
    n_no_score = int(len(frame) - len(usable))
    imputed_mask = usable["score_imputed"].fillna(False).astype(bool)

    report = summarise(
        pred=list(usable["pred"]),
        gold=list(usable["pc"]),
        confidence=list(usable["confidence"]) if "confidence" in usable else None,
        costs=usable[list(COST_FIELDS)].to_dict("records"),
    )
    report["n_rows_joined"] = int(len(frame))
    report["n_without_score"] = n_no_score
    report["n_imputed"] = int(imputed_mask.sum())
    if imputed_mask.any():
        # An imputed score is a placeholder, not a prediction. Report the metric
        # with it excluded so the headline number is not propped up by filler.
        honest = usable[~imputed_mask]
        report["pearson_excl_imputed"] = correlations(
            list(honest["pred"]), list(honest["pc"])
        ).get("pearson")
        report["n_excl_imputed"] = int(len(honest))
    scored = usable

    print("\n" + "=" * 70)
    print(f"{tag}")
    print("=" * 70)
    print(_headline(report))

    summary_path = out_path.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps(
            {"tag": tag, "run": stats.as_dict(), "metrics": report},
            indent=2,
            default=str,
        )
    )
    print(f"\nresults : {out_path}\nsummary : {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
