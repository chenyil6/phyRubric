#!/usr/bin/env python3
"""Validate, merge and count the caption dataset.

    python data/build.py check                      # validate train/ and eval/, print counts
    python data/build.py build                      # check, then write train.json / eval.json
    python data/build.py accept drafts/X.json train # validate a draft, append it to train/<category>.json

Records follow schema.json. Ids must be unique across train and eval.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / "schema.json").read_text())
CATEGORIES = list(SCHEMA["subcategories"])
PREFIX = {"Mechanics": "MECH", "Heat": "HEAT", "Optics": "OPT", "Electricity": "ELEC", "Acoustics": "ACOU"}
FIELDS = ["id", "caption", "category", "subcategory", "violation_types", "expectation"]
# (train, eval) targets. Acoustics is smaller: sound is judged only through its visible effects.
TARGET = {"Mechanics": (250, 50), "Heat": (250, 50), "Optics": (250, 50), "Electricity": (250, 50), "Acoustics": (100, 20)}
SPLITS = ("train", "eval")


def load(path: Path) -> list[dict]:
    text = path.read_text().strip()
    return json.loads(text) if text else []


def category_file(split: str, category: str) -> Path:
    return ROOT / split / f"{category.lower()}.json"


def validate(records: list[dict], where: str) -> list[str]:
    errors = []
    for i, r in enumerate(records):
        tag = f"{where}[{i}] {r.get('id', '?')}"
        missing = [f for f in FIELDS if f not in r]
        extra = [f for f in r if f not in FIELDS]
        if missing or extra:
            errors.append(f"{tag}: missing {missing} extra {extra}")
            continue
        cat = r["category"]
        if cat not in CATEGORIES:
            errors.append(f"{tag}: unknown category {cat!r}")
            continue
        if not (r["id"].startswith(PREFIX[cat] + "-") and r["id"][len(PREFIX[cat]) + 1:].isdigit()):
            errors.append(f"{tag}: id does not match {PREFIX[cat]}-NNNN")
        if r["subcategory"] not in SCHEMA["subcategories"][cat]:
            errors.append(f"{tag}: unknown subcategory {r['subcategory']!r} for {cat}")
        vts = r["violation_types"]
        if not isinstance(vts, list) or not 1 <= len(vts) <= 3:
            errors.append(f"{tag}: violation_types must be a list of 1-3 tags")
        else:
            for v in vts:
                if v not in SCHEMA["violation_types"]:
                    errors.append(f"{tag}: unknown violation_type {v!r}")
        for f in ("caption", "expectation"):
            if not str(r[f]).strip():
                errors.append(f"{tag}: empty {f}")
    return errors


def load_split(split: str) -> dict[str, list[dict]]:
    out = {}
    for cat in CATEGORIES:
        path = category_file(split, cat)
        out[cat] = load(path) if path.exists() else []
    return out


def check(verbose: bool = True) -> tuple[dict[str, dict[str, list[dict]]], list[str]]:
    data = {split: load_split(split) for split in SPLITS}
    errors = []
    seen: dict[str, str] = {}
    for split in SPLITS:
        for cat, records in data[split].items():
            errors += validate(records, f"{split}/{cat.lower()}.json")
            for r in records:
                if r["category"] != cat:
                    errors.append(f"{split}/{cat.lower()}.json {r['id']}: category {r['category']} in wrong file")
                if r["id"] in seen:
                    errors.append(f"duplicate id {r['id']} in {seen[r['id']]} and {split}")
                seen[r["id"]] = split
    if verbose:
        print(f"{'category':12s} {'train':>6s} {'eval':>6s}   target")
        for cat in CATEGORIES:
            tr, ev = TARGET[cat]
            print(f"{cat:12s} {len(data['train'][cat]):6d} {len(data['eval'][cat]):6d}   {tr} / {ev}")
        for split in SPLITS:
            all_records = [r for recs in data[split].values() for r in recs]
            if not all_records:
                continue
            print(f"\n[{split}] subcategories:")
            for cat in CATEGORIES:
                c = Counter(r["subcategory"] for r in data[split][cat])
                if c:
                    print(f"  {cat}: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
            vt = Counter(v for r in all_records for v in r["violation_types"])
            print(f"[{split}] violation_types: " + ", ".join(f"{k} {v}" for k, v in vt.most_common()))
        print()
        for e in errors:
            print("ERROR", e)
        print(f"{len(errors)} errors")
    return data, errors


def build() -> int:
    data, errors = check()
    if errors:
        return 1
    for split in SPLITS:
        merged = [r for cat in CATEGORIES for r in data[split][cat]]
        (ROOT / f"{split}.json").write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {split}.json ({len(merged)} records)")
    return 0


def accept(draft: Path, split: str) -> int:
    if split not in SPLITS:
        print(f"split must be one of {SPLITS}")
        return 1
    records = load(draft)
    errors = validate(records, draft.name)
    cats = {r["category"] for r in records}
    if len(cats) != 1:
        errors.append(f"draft must contain exactly one category, found {sorted(cats)}")
    existing, _ = check(verbose=False)
    known = {r["id"] for s in SPLITS for recs in existing[s].values() for r in recs}
    for r in records:
        if r["id"] in known:
            errors.append(f"{r['id']} already exists")
    if errors:
        for e in errors:
            print("ERROR", e)
        return 1
    cat = cats.pop()
    target = category_file(split, cat)
    current = load(target) if target.exists() else []
    target.write_text(json.dumps(current + records, indent=2, ensure_ascii=False) + "\n")
    print(f"appended {len(records)} records to {target.relative_to(ROOT)} (now {len(current) + len(records)})")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "check":
        sys.exit(1 if check()[1] else 0)
    if args[0] == "build":
        sys.exit(build())
    if args[0] == "accept" and len(args) == 3:
        sys.exit(accept(ROOT / args[1] if not Path(args[1]).is_absolute() else Path(args[1]), args[2]))
    print(__doc__)
    sys.exit(2)
