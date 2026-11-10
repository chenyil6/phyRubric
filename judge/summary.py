#!/usr/bin/env python3
"""Score a judge run (judge/infer.py output) against the gold labels with the same metrics as the official
baselines (baselines/videophy_official_summary.py): Spearman / AUROC / binary kappa at the SA >= 4, PC >= 4
pass line, exact and within-one accuracy, joint pass, per generator and pooled. Adds the judge-specific numbers:
parse failures and pc_assessable accuracy against the gold flag.

    python judge/summary.py --run sft_lora_r16_full --split eval [--save results/judge/sft_lora_r16_full_eval.json]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from baselines.videophy_official_summary import MODELS, binary_block, corr_block, load_gold, summarise  # noqa: E402
from judge.infer import DEFAULT_OUT_ROOT  # noqa: E402

MODELS.setdefault("judge", ("sa_score", "pc_score", True, 4))


def load_run(run_dir: Path, split: str) -> dict[tuple[str, str], dict]:
    preds = {}
    for path in sorted(run_dir.glob(f"{split}.shard*.jsonl")):
        for line in path.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                preds[(r["tag"], r["id"])] = r
    return preds


def load_gold_assessable(split: str) -> dict[tuple[str, str], bool]:
    """Gold pc_assessable = at least one core PC item judged pass or fail; severities come from the rubric."""
    from baselines.videophy_official_summary import ANN_DIR
    rub = {}
    for p in sorted((ROOT / "rubrics" / split).glob("*/*.json")):
        r = json.loads(p.read_text())
        rub[r["id"]] = r
    out = {}
    for f in sorted((ANN_DIR / split).glob("*.json")):
        for c in json.loads(f.read_text())["clips"]:
            sev = {i["id"]: i["severity"] for i in rub[c["id"]]["pc"]}
            core = [i for i in c["items"] if i["id"].startswith("P") and sev.get(i["id"]) == "core"]
            out[(c["tag"], c["id"])] = any(i["status"] in ("pass", "fail") for i in core)
    return out


def assessable_block(rows: list[tuple[dict, dict]]) -> dict | None:
    pairs = [(p["pc_assessable"], g["pc_assessable"]) for p, g in rows
             if isinstance(p.get("pc_assessable"), bool) and isinstance(g.get("pc_assessable"), bool)]
    if not pairs:
        return None
    pred, gold = (np.array(x, dtype=bool) for x in zip(*pairs))
    return binary_block(pred, gold)


SOFT_METHOD = "expectation"   # "normed" = VideoScore2's normalized float (argmax digit x its renormalised probability; paper default,
                         # user decision 2026-10-23); "expectation" = sum_k k p(k) / sum p (G-Eval style; the runner's stored *_soft)


def soft_from_probs(probs: dict | None, method: str = None) -> float | None:
    """Soft score from the digit probabilities {"1": p1, ..., "5": p5} recorded at the score token."""
    if not probs:
        return None
    items = [(int(k), float(v)) for k, v in probs.items() if str(k) in ("1", "2", "3", "4", "5")]
    tot = sum(v for _, v in items)
    if not items or tot <= 0:
        return None
    if (method or SOFT_METHOD) == "expectation":
        return sum(k * v for k, v in items) / tot
    k, v = max(items, key=lambda kv: kv[1])
    return k * v / tot


def soft_value(p: dict, task: str) -> float | None:
    """Soft score of a judge row: recomputed from the stored digit probabilities with SOFT_METHOD; falls back to the
    runner's stored *_soft (expectation) only when no probabilities were recorded."""
    v = soft_from_probs(p.get(f"{task}_probs"))
    return v if v is not None else p.get(f"{task}_soft")


def soft_block(rows: list[tuple[dict, dict]], task: str) -> dict | None:
    """Spearman / AUROC of the soft score against the gold integer."""
    pairs = [(soft_value(p, task), g[f"{task}_score"]) for p, g in rows
             if soft_value(p, task) is not None and g.get(f"{task}_score") is not None]
    if not pairs:
        return None
    pred, gold = (np.array(x, dtype=float) for x in zip(*pairs))
    block = corr_block(pred, gold)
    block["pred_mean"] = round(float(pred.mean()), 3)
    block["binary_ge3.5"] = binary_block(pred >= 3.5, gold >= 4)
    block["mae"] = round(float(np.abs(pred - gold).mean()), 4)          # soft score vs integer label, same 1-5 scale
    block["mean_bias"] = round(float(pred.mean() - gold.mean()), 4)
    block["rel_bias"] = round(float((pred.mean() - gold.mean()) / gold.mean()), 4)  # signed
    return block


def soft_joint_block(rows: list[tuple[dict, dict]]) -> dict | None:
    """Joint pass on the soft scores (SA_soft >= 3.5 and PC_soft >= 3.5) against gold SA >= 4 and PC >= 4."""
    both = [(p, g) for p, g in rows if soft_value(p, "sa") is not None and soft_value(p, "pc") is not None
            and g.get("sa_score") is not None and g.get("pc_score") is not None]
    if not both:
        return None
    pj = np.array([soft_value(p, "sa") >= 3.5 and soft_value(p, "pc") >= 3.5 for p, _ in both])
    gj = np.array([g["sa_score"] >= 4 and g["pc_score"] >= 4 for _, g in both])
    return binary_block(pj, gj)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run", required=True)
    ap.add_argument("--split", default="eval")
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--save", type=Path)
    ap.add_argument("--soft", choices=("normed", "expectation"), default="expectation", help="soft-score definition")
    args = ap.parse_args()
    globals()["SOFT_METHOD"] = args.soft

    gold = load_gold(args.split) if args.split == "eval" else None
    gold_assess = load_gold_assessable(args.split) if args.split == "eval" else {}
    preds = load_run(args.out_root / args.run, args.split)
    by_tag = defaultdict(list)
    n_parse_fail = 0
    for key, p in preds.items():
        if not p.get("parse_ok"):
            n_parse_fail += 1
        # val/train rows carry their gold in the row itself; eval uses the annotation files (same numbers)
        g = dict(gold[key]) if gold is not None and key in gold else dict(p["gold"])
        g["pc_assessable"] = gold_assess.get(key, p["gold"].get("pc_assessable"))  # from items + rubric severity
        by_tag[key[0]].append((p, g))
    report = {"run": args.run, "split": args.split, "n_pred": len(preds), "n_parse_fail": n_parse_fail,
              "by_tag": {}, "pooled": None}
    pooled = []
    for tag in sorted(by_tag):
        report["by_tag"][tag] = summarise(by_tag[tag], "judge")
        report["by_tag"][tag]["pc_assessable"] = assessable_block(by_tag[tag])
        for task in ("sa", "pc"):
            report["by_tag"][tag][f"{task}_soft"] = soft_block(by_tag[tag], task)
        pooled.extend(by_tag[tag])
    for tag in list(report["by_tag"]):
        report["by_tag"][tag]["joint_pass_soft"] = soft_joint_block(by_tag[tag])
    if pooled:
        report["pooled"] = summarise(pooled, "judge")
        report["pooled"]["joint_pass_soft"] = soft_joint_block(pooled)
        report["pooled"]["pc_assessable"] = assessable_block(pooled)
        for task in ("sa", "pc"):
            report["pooled"][f"{task}_soft"] = soft_block(pooled, task)
    print(json.dumps(report, indent=2))
    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        args.save.write_text(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
