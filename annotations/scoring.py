#!/usr/bin/env python3
"""SA / PC scores (1-5) from per-item statuses, following rubrics/_policy.json (sa_scoring, pc_scoring).

    python annotations/scoring.py --check     # recompute every clip's scores from its items + rubric, compare with the stored ones

Every clip in annotations/<split>/<tag>.json carries one status (pass | fail | not_shown) per rubric item; sa_score and
pc_score are derived from those statuses by score() below, nothing else.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SEVERITY_CAP = {"fatal": 1, "core": 2, "major": 3, "minor": 4}   # a failed item of this severity caps PC at this value
HEAVY = {"fatal", "core", "major"}                                 # every further heavy fail costs one more point


def score(rubric: dict, items: list[dict], recognisable: bool = True) -> tuple[int, int]:
    """SA: 5 with no failed SA item; 4 if only minor items failed; 3 with one failed core item; 2 with two or more
    (1 if the clip is not even a recognisable attempt). PC: 5 with no failed PC item; otherwise the cap of the most
    severe failed item, minus one per additional heavy (fatal / core / major) fail, floored at 1."""
    status = {it["id"]: it["status"] for it in items}
    missing = [it["id"] for it in rubric["sa"] + rubric["pc"] if it["id"] not in status]
    if missing:
        raise ValueError(f"statuses missing for {missing}")
    failed_sa = [it for it in rubric["sa"] if status[it["id"]] == "fail"]
    if not failed_sa:
        sa = 5
    else:
        core = sum(it["weight"] == "core" for it in failed_sa)
        sa = 4 if core == 0 else 3 if core == 1 else (2 if recognisable else 1)
    failed_pc = [it for it in rubric["pc"] if status[it["id"]] == "fail"]
    if not failed_pc:
        pc = 5
    else:
        pc = min(SEVERITY_CAP[it["severity"]] for it in failed_pc)
        heavy = sum(it["severity"] in HEAVY for it in failed_pc)
        pc = max(1, pc - max(0, heavy - 1))
    return sa, pc


def check() -> int:
    """Recompute sa_score / pc_score for every annotated clip and report mismatches with the stored values."""
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / "rubrics"))
    from build import load  # rubrics/build.py

    n = bad = 0
    for split in ("train", "eval"):
        rubrics = load(split)
        for path in sorted((root / "annotations" / split).glob("*.json")):
            for c in json.loads(path.read_text())["clips"]:
                sa, pc = score(rubrics[c["id"]], c["items"], c["recognisable_attempt"])
                n += 1
                if (sa, pc) != (c["sa_score"], c["pc_score"]):
                    bad += 1
                    print(f"{path.name} {c['id']}: stored SA {c['sa_score']} PC {c['pc_score']}, recomputed SA {sa} PC {pc}")
    print(f"{n} clips checked, {bad} mismatches")
    return 1 if bad else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="recompute all stored scores and compare")
    args = ap.parse_args()
    raise SystemExit(check() if args.check else ap.print_help())
