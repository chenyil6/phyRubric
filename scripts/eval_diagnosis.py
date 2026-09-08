#!/usr/bin/env python
"""Score the diagnosis, not the number.

    python scripts/eval_diagnosis.py results/agentic_probe_n12.jsonl

Correlation with human pc only measures the compatibility layer -- the single
score that exists so we can be compared to prior judges at all. The claim this
work actually makes is about the diagnosis: that every failed rubric item names a
violation a human would also name, and that we localise it. This script measures
the first half.

Ground truth is `human_violated_rules`, the free-text violations annotators wrote
because the automatic rule list missed them. `physics_rules_unfollowed` is NOT
used as ground truth, and that is a deliberate, measured decision: it contains
rules that contradict the prompt outright. One video captioned "a curler releases
a stone showing a direct path and velocity" carries the unfollowed rule "the
curling stone remains stationary on the ice" while humans scored it 5/5 -- the
rule is wrong, not the video. Counting that as a violation we failed to find
would be scoring us against noise. It is reported separately for reference.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.matchers import build_matcher  # noqa: E402
from eval.metrics import open_discovery_match  # noqa: E402
from eval.runner import load_results  # noqa: E402


def load_env(path: Path = ROOT / ".env") -> None:
    import os

    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def score(records, by_id, matcher_factory, gold_field: str):
    """Greedy one-to-one matching per video, then pool the counts."""
    n_pred = n_gold = n_match = 0
    per_video = []
    for rec in records:
        if rec.get("error"):
            continue
        sample = by_id.get(rec.get("video_id"))
        if sample is None:
            continue
        gold = [g for g in getattr(sample, gold_field) if g and g.strip()]
        pred = [p for p in (rec.get("violation_descriptions") or []) if p and p.strip()]
        matcher = matcher_factory(sample.caption) if matcher_factory else None
        result = open_discovery_match(pred, gold, matcher=matcher)
        n_pred += result["n_pred"]
        n_gold += result["n_gold"]
        n_match += len(result["matches"])
        per_video.append(
            {
                "video_id": rec["video_id"],
                "gold_pc": sample.pc,
                "pred_pc": rec.get("pc_score"),
                "n_pred": result["n_pred"],
                "n_gold": result["n_gold"],
                "matched": len(result["matches"]),
                "unmatched_gold": result.get("unmatched_gold", []),
            }
        )
    precision = n_match / n_pred if n_pred else None
    recall = n_match / n_gold if n_gold else None
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision and recall
        else (0.0 if (precision is not None and recall is not None) else None)
    )
    return {
        "n_videos": len(per_video),
        "n_pred": n_pred,
        "n_gold": n_gold,
        "n_matched": n_match,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "per_video": per_video,
    }


def fmt(v, spec=".3f"):
    return "n/a" if v is None else format(v, spec)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", help="a results jsonl from run_eval.py")
    ap.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    ap.add_argument("--n", type=int, default=12, help="subset size the results came from")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--lexical-only", action="store_true", help="skip the LLM matcher")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    load_env()
    cfg = yaml.safe_load(Path(args.config).read_text())
    ds = VideoPhy2Dataset.from_config(cfg).filter(has_video=True)
    if args.n:
        ds = ds.stratified_subset(args.n, seed=args.seed)
    by_id = ds.id_to_sample()
    records = load_results(args.results)
    print(f"{len(records)} records, {len(by_id)} samples in the subset\n")

    report = {}
    for gold_field, label in (
        ("human_violated_rules", "human-written violations (ground truth)"),
        ("rules_unfollowed", "automatic rules marked unfollowed (reference only)"),
    ):
        print("=" * 72)
        print(label)
        print("=" * 72)
        lex = score(records, by_id, None, gold_field)
        print(f"  lexical matcher : P {fmt(lex['precision'])}  R {fmt(lex['recall'])}  "
              f"F1 {fmt(lex['f1'])}   ({lex['n_matched']}/{lex['n_gold']} gold, "
              f"{lex['n_pred']} predicted)")
        report[f"{gold_field}_lexical"] = {k: v for k, v in lex.items() if k != "per_video"}

        if not args.lexical_only:
            base = build_matcher(cfg)
            llm = score(records, by_id, lambda cap: base.for_video(cap), gold_field)
            print(f"  LLM matcher     : P {fmt(llm['precision'])}  R {fmt(llm['recall'])}  "
                  f"F1 {fmt(llm['f1'])}   ({llm['n_matched']}/{llm['n_gold']} gold, "
                  f"{llm['n_pred']} predicted)")
            print(f"  matcher cost    : {base.stats.as_dict()}")
            report[f"{gold_field}_llm"] = {
                **{k: v for k, v in llm.items() if k != "per_video"},
                "matcher": base.stats.as_dict(),
            }
            report[f"{gold_field}_per_video"] = llm["per_video"]
            if gold_field == "human_violated_rules":
                print("\n  --- what the matcher decided ---")
                for r in base.stats.reasons[:10]:
                    mark = "MATCH " if r["same"] else "no    "
                    print(f"  {mark} {r['why'][:100]}")
                    print(f"         RULE  : {r['gold'][:95]}")
                    print(f"         REPORT: {r['pred'][:95]}")
        print()

    out = Path(args.out or Path(args.results).with_suffix(".diagnosis.json"))
    out.write_text(json.dumps(report, indent=2, default=str))
    print(f"written: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
