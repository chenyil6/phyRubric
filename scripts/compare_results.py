#!/usr/bin/env python
"""Put every finished evaluation side by side.

    python scripts/compare_results.py                  # all summaries in results/
    python scripts/compare_results.py results/*.summary.json

The point of the table is the ordering: an agentic judge that does not beat
`caption_only` is not reading the video, and one that does not beat `single_pass`
is not benefiting from active perception. Both comparisons must be on the same
subset, so the n and seed are printed and mismatches are flagged.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fmt(value, spec: str = ".3f") -> str:
    return "n/a" if value is None else format(value, spec)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("summaries", nargs="*", default=None)
    ap.add_argument("--results-dir", default=str(ROOT / "results"))
    args = ap.parse_args()

    paths = [Path(p) for p in (args.summaries or [])]
    if not paths:
        paths = sorted(Path(args.results_dir).glob("*.summary.json"))
    if not paths:
        print(f"no summaries found in {args.results_dir}")
        return 1

    rows = []
    for p in paths:
        try:
            d = json.loads(p.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            print(f"skipping {p.name}: {exc}", file=sys.stderr)
            continue
        m = d.get("metrics", {})
        ci = m.get("pearson_ci") or {}
        rows.append(
            {
                "tag": d.get("tag", p.stem),
                "n": m.get("n_scored"),
                "n_total": m.get("n_total"),
                "cov": m.get("coverage"),
                "pearson": m.get("pearson"),
                "lo": ci.get("lo"),
                "hi": ci.get("hi"),
                "spearman": m.get("spearman"),
                "mae": m.get("mae"),
                "auroc": m.get("auroc"),
                "best_f1": m.get("best_f1"),
                "aurc": m.get("aurc"),
                "failed": (d.get("run") or {}).get("failed"),
            }
        )

    rows.sort(key=lambda r: (-(r["pearson"] or -9), r["tag"]))
    width = max(len(r["tag"]) for r in rows)
    header = (
        f"{'judge':<{width}}  {'n':>6}  {'cov':>5}  {'pearson (95% CI)':>22}  "
        f"{'spear':>6}  {'mae':>5}  {'auroc':>6}  {'bestF1':>6}  {'aurc':>6}  {'fail':>4}"
    )
    print(header)
    print("-" * len(header))
    for r in rows:
        print(
            f"{r['tag']:<{width}}  {str(r['n']):>6}  {fmt(r['cov'], '.2f'):>5}  "
            f"{fmt(r['pearson']) + ' [' + fmt(r['lo'], '.2f') + ',' + fmt(r['hi'], '.2f') + ']':>22}  "
            f"{fmt(r['spearman'], '.3f'):>6}  {fmt(r['mae'], '.2f'):>5}  "
            f"{fmt(r['auroc'], '.3f'):>6}  {fmt(r['best_f1'], '.3f'):>6}  "
            f"{fmt(r['aurc'], '.3f'):>6}  {str(r['failed'] or 0):>4}"
        )

    sizes = {r["n_total"] for r in rows if r["n_total"]}
    if len(sizes) > 1:
        print(f"\nWARNING: subsets differ in size ({sorted(sizes)}) -- these rows are "
              "not directly comparable. Re-run with the same --n and --seed.")
    print("\nAutoEval (VideoPhy-2, 50k human labels, fine-tuned) reports pearson 0.37 "
          "on physical commonsense.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
