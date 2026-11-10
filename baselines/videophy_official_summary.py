#!/usr/bin/env python3
"""Summarise official rater outputs (VideoPhy-1/2, VideoScore-v1.1, VideoScore2) against our eval labels.

Reads <out-root>/<model>/<tag>.shard*.jsonl (from videophy_official.py) and
annotations/eval/<tag>.json (gold sa_score / pc_score, 1-5), and prints
per-generator and pooled agreement:
  * Spearman / Pearson / Kendall between rater score and gold, for SA and PC;
  * AUROC of the rater score for gold >= 4 (works for both the 0-1 VideoCon-Physics
    probability and the 1-5 AutoEval integer);
  * binary agreement (accuracy, F1 on "pass", Cohen's kappa) after thresholding the rater at its
    own pass line (0.5 for VideoPhy-1 probabilities, 4 for 1-5 raters, 2.5 for VideoScore 1-4) and
    gold at >= 4; joint pass = SA pass & PC pass on both sides;
  * for integer 1-5 raters: exact and within-one accuracy.
Clips without a gold label (e.g. LTX-2.3 before labelling) are counted but not scored.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
ANN_DIR = ROOT / "annotations"
DEFAULT_OUT_ROOT = Path(os.environ.get("PJ_RUNS", ROOT / "runs")) / "baselines"

# model -> (field holding the SA-like score, field holding the PC-like score, integer 1-5 scale?,
#           threshold at which the rater's own score counts as "pass")
MODELS = {
    "videophy1": ("sa_score", "pc_score", False, 0.5),        # P(Yes), official threshold 0.5
    "videophy2": ("sa_score", "pc_score", True, 4),           # 1-5, pass = >= 4 as in VideoPhy-2
    "videophy2_soft": ("sa_soft", "pc_soft", False, 3.5),     # same run with --soft: digit-probability expectation (Eq. soft), pass = >= 3.5
    "videoscore1": ("t2v_alignment", "factual_consistency", False, 2.5),  # 1.0-4.0 regression, midpoint
    # VideoScore2 authors' mapping of VideoScore-v1.1 to 1-5 (eval_methods/vs1.py): round(x * 1.25), clipped
    "videoscore1_x125": ("t2v_alignment_5", "factual_consistency_5", True, 4),
    "videoscore2": ("t_score", "p_score", True, 4),           # 1-5 hard scores
    # Soft score = expectation over the digit probabilities at the score token (the paper's single soft-score definition,
    # Eq. soft, applied to every generative judge; derived in load_preds from t_digit_probs / p_digit_probs). User decision 2026-10-23.
    "videoscore2_soft": ("t_exp", "p_exp", False, 3.5),
    # For reference only: VideoScore2's own "normalized float" (argmax digit x its renormalised probability; its paper's default),
    # recorded by the runner as t_soft / p_soft.
    "videoscore2_normed": ("t_soft", "p_soft", False, 3.5),
}
GOLD_PASS = 4  # our joint-pass line: SA >= 4 and PC >= 4


def load_gold(split: str) -> dict[tuple[str, str], dict]:
    gold = {}
    for path in sorted((ANN_DIR / split).glob("*.json")):
        data = json.loads(path.read_text())
        for clip in data["clips"]:
            gold[(clip["tag"], clip["id"])] = clip
    return gold


def load_preds(out_root: Path, model: str) -> dict[tuple[str, str], dict]:
    preds = {}
    if model == "videoscore1_x125":
        preds = load_preds(out_root, "videoscore1")
        for row in preds.values():
            for k in ("t2v_alignment", "factual_consistency"):
                row[f"{k}_5"] = min(5, max(1, round(row[k] * 1.25)))
        return preds
    if model == "videoscore2_normed":        # same rows as videoscore2; t_soft / p_soft are already in them
        return load_preds(out_root, "videoscore2")
    if model == "videoscore2_soft":          # expectation over the digit probabilities (same definition as the judge's soft score)
        preds = load_preds(out_root, "videoscore2")
        for row in preds.values():
            for k in ("t", "p"):
                probs = row.get(f"{k}_digit_probs")
                if isinstance(probs, str):
                    try:
                        probs = json.loads(probs.replace("'", '"'))
                    except Exception:
                        probs = None
                if isinstance(probs, dict) and sum(probs.values()) > 0:
                    z = sum(probs.values())
                    row[f"{k}_exp"] = round(sum(int(d) * v for d, v in probs.items()) / z, 4)
        return preds
    for path in sorted((out_root / model).glob("*.jsonl")):
        for line in path.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                preds[(row["tag"], row["id"])] = row
    return preds


def auroc(scores: np.ndarray, positive: np.ndarray) -> float | None:
    pos, neg = scores[positive], scores[~positive]
    if len(pos) == 0 or len(neg) == 0:
        return None
    # rank-based AUROC = P(score_pos > score_neg) with ties counting half
    ranks = stats.rankdata(np.concatenate([pos, neg]))
    return float((ranks[: len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def corr_block(pred: np.ndarray, gold: np.ndarray) -> dict:
    out = {"n": int(len(pred))}
    if len(pred) < 3 or np.std(pred) == 0 or np.std(gold) == 0:
        out.update(spearman=None, pearson=None, kendall=None)
    else:
        out["spearman"] = round(float(stats.spearmanr(pred, gold).statistic), 4)
        out["pearson"] = round(float(stats.pearsonr(pred, gold).statistic), 4)
        out["kendall"] = round(float(stats.kendalltau(pred, gold).statistic), 4)
    a = auroc(pred, gold >= 4)
    out["auroc_gold_ge4"] = None if a is None else round(a, 4)
    return out


def binary_block(pred_pass: np.ndarray, gold_pass: np.ndarray) -> dict:
    """Agreement after binarising both sides (rater threshold vs gold >= 4)."""
    tp = int((pred_pass & gold_pass).sum())
    fp = int((pred_pass & ~gold_pass).sum())
    fn = int((~pred_pass & gold_pass).sum())
    tn = int((~pred_pass & ~gold_pass).sum())
    n = tp + fp + fn + tn
    acc = (tp + tn) / n
    p_e = ((tp + fp) * (tp + fn) + (fn + tn) * (fp + tn)) / (n * n)
    kappa = (acc - p_e) / (1 - p_e) if p_e < 1 else None
    prec = tp / (tp + fp) if tp + fp else None
    rec = tp / (tp + fn) if tp + fn else None
    f1 = 2 * prec * rec / (prec + rec) if prec and rec else (0.0 if prec is not None and rec is not None else None)
    rnd = lambda x: None if x is None else round(float(x), 4)
    return {"n": n, "accuracy": rnd(acc), "f1_pass": rnd(f1), "kappa": rnd(kappa),
            "pred_pass_rate": rnd(pred_pass.mean()), "gold_pass_rate": rnd(gold_pass.mean()),
            "tp": tp, "fp": fp, "fn": fn, "tn": tn}


def summarise(rows: list[tuple[dict, dict]], model: str) -> dict:
    sa_field, pc_field, integer_scale, pred_thr = MODELS[model]
    fields = {"sa": sa_field, "pc": pc_field}
    report = {"n_clips": len(rows), "pred_fields": fields, "pred_pass_threshold": pred_thr}
    for task in ("sa", "pc"):
        pairs = [(p[fields[task]], g[f"{task}_score"]) for p, g in rows
                 if p.get(fields[task]) is not None and g.get(f"{task}_score") is not None]
        if not pairs:
            continue
        pred, gold = (np.array(x, dtype=float) for x in zip(*pairs))
        block = corr_block(pred, gold)
        block["pred_mean"] = round(float(pred.mean()), 3)
        block["gold_mean"] = round(float(gold.mean()), 3)
        block["binary"] = binary_block(pred >= pred_thr, gold >= GOLD_PASS)
        if integer_scale:
            delta = np.abs(pred - gold)
            block["exact_acc"] = round(float((delta == 0).mean()), 4)
            block["within1_acc"] = round(float((delta <= 1).mean()), 4)
            block["mae"] = round(float(delta.mean()), 4)
            block["mean_bias"] = round(float(pred.mean() - gold.mean()), 4)              # signed, score points
            block["rel_bias"] = round(float((pred.mean() - gold.mean()) / gold.mean()), 4)  # signed; PhyGround reports |.|, per dimension
            block["pred_hist"] = {int(k): int(v) for k, v in zip(*np.unique(pred, return_counts=True))}
        report[task] = block
    both = [(p, g) for p, g in rows
            if all(p.get(f) is not None for f in fields.values()) and all(g.get(k) is not None for k in ("sa_score", "pc_score"))]
    if both:
        pj = np.array([p[sa_field] >= pred_thr and p[pc_field] >= pred_thr for p, _ in both])
        gj = np.array([g["sa_score"] >= GOLD_PASS and g["pc_score"] >= GOLD_PASS for _, g in both])
        report["joint_pass"] = binary_block(pj, gj)
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--split", default="eval")
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--save", type=Path, help="write the JSON report here")
    args = ap.parse_args()

    gold = load_gold(args.split)
    preds = load_preds(args.out_root, args.model)
    by_tag = defaultdict(list)
    unlabelled = defaultdict(int)
    for key, pred in preds.items():
        if key in gold:
            by_tag[key[0]].append((pred, gold[key]))
        else:
            unlabelled[key[0]] += 1
    report = {"model": args.model, "split": args.split, "n_pred": len(preds),
              "unlabelled_by_tag": dict(unlabelled), "by_tag": {}, "pooled": None}
    pooled = []
    for tag in sorted(by_tag):
        report["by_tag"][tag] = summarise(by_tag[tag], args.model)
        pooled.extend(by_tag[tag])
    if pooled:
        report["pooled"] = summarise(pooled, args.model)
    print(json.dumps(report, indent=2))
    if args.save:
        args.save.write_text(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
