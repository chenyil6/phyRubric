#!/usr/bin/env python3
"""Work lists for rubric authoring.

    python3 rubrics/assign.py list                         # missing rubrics per split / category / subcategory
    python3 rubrics/assign.py show --split train --category Heat --subcategory melt_freeze [--ids ID ...]
                                                           # data records (id, caption, violation_types, expectation) still lacking a rubric
    python3 rubrics/assign.py examples --category Heat [--subcategory melt_freeze]
                                                           # existing rubric files of that branch, same-subcategory ones first
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data"
SCHEMA = json.loads((DATA / "schema.json").read_text())
CATEGORIES = list(SCHEMA["subcategories"])


def load() -> dict[str, tuple[str, dict]]:
    out = {}
    for split in ("train", "eval"):
        for cat in CATEGORIES:
            p = DATA / split / f"{cat.lower()}.json"
            if p.exists():
                for rec in json.loads(p.read_text()):
                    out[rec["id"]] = (split, rec)
    return out


def have() -> set[str]:
    return {p.stem for p in ROOT.glob("*/*/*.json")}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    s = sub.add_parser("show")
    s.add_argument("--split", choices=("train", "eval"))
    s.add_argument("--category", choices=CATEGORIES)
    s.add_argument("--subcategory", nargs="*")
    s.add_argument("--ids", nargs="*")
    s.add_argument("--all", action="store_true", help="include ids that already have a rubric")
    e = sub.add_parser("examples")
    e.add_argument("--category", choices=CATEGORIES, required=True)
    e.add_argument("--subcategory", nargs="*")
    args = ap.parse_args(argv)
    data, done = load(), have()

    if args.cmd == "list":
        c = Counter((sp, r["category"], r["subcategory"]) for rid, (sp, r) in data.items() if rid not in done)
        for k in sorted(c):
            print(f"{k[0]:5s} {k[1]:12s} {k[2]:24s} {c[k]}")
        print(f"total missing {sum(c.values())} of {len(data)}")
        return 0

    if args.cmd == "show":
        rows = []
        for rid, (sp, r) in data.items():
            if args.ids and rid not in args.ids:
                continue
            if args.split and sp != args.split:
                continue
            if args.category and r["category"] != args.category:
                continue
            if args.subcategory and r["subcategory"] not in args.subcategory:
                continue
            if rid in done and not args.all and not args.ids:
                continue
            rows.append({"id": rid, "split": sp, "category": r["category"], "subcategory": r["subcategory"], "caption": r["caption"], "violation_types": r["violation_types"], "expectation": r["expectation"]})
        rows.sort(key=lambda x: x["id"])
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        print(f"\n{len(rows)} records", file=sys.stderr)
        return 0

    if args.cmd == "examples":
        files = sorted(ROOT.glob(f"*/{args.category.lower()}/*.json"))
        same = [f for f in files if args.subcategory and data[f.stem][1]["subcategory"] in args.subcategory]
        rest = [f for f in files if f not in same]
        for f in same + rest:
            print(f"{f.relative_to(ROOT.parent)}  [{data[f.stem][1]['subcategory']}]")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
