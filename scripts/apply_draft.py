#!/usr/bin/env python3
"""Copy reviewed caption/expectation rewrites from a draft into a train/eval category file.

    python scripts/apply_draft.py data/drafts/mechanics_draft.json data/train/mechanics.json MECH-0001:MECH-0050
    python scripts/apply_draft.py data/drafts/heat_draft.json data/train/heat.json HEAT-0007 HEAT-0009

Only `caption` and `expectation` are copied; id / category / subcategory / violation_types stay as they are in
the target file.  A record is applied only if the target's current caption equals the draft's `old_caption`
(so a draft made against an older file cannot silently overwrite later edits); records whose target already
carries the draft caption are reported as already applied.  Records tagged `delete` are skipped and listed.
Run `python data/build.py build` afterwards to refresh train.json / eval.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def expand(spec: str, order: list[str]) -> list[str]:
    if ":" in spec:
        lo, hi = spec.split(":")
        i, j = order.index(lo), order.index(hi)
        return order[i:j + 1]
    return [spec]


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print(__doc__)
        return 1
    draft_path, target_path, specs = Path(argv[1]), Path(argv[2]), argv[3:]
    draft = {r["id"]: r for r in json.loads(draft_path.read_text())}
    target = json.loads(target_path.read_text())
    by_id = {r["id"]: r for r in target}
    order = [r["id"] for r in target]
    ids = [i for s in specs for i in expand(s, order)]

    applied, already, skipped, errors = [], [], [], []
    for i in ids:
        d, t = draft.get(i), by_id.get(i)
        if d is None or t is None:
            errors.append(f"{i}: missing in {'draft' if d is None else 'target'}")
            continue
        if "delete" in d.get("change", []):
            skipped.append(i)
            continue
        if t["caption"] == d["caption"] and t["expectation"] == d["expectation"]:
            already.append(i)
            continue
        if t["caption"] != d["old_caption"]:
            errors.append(f"{i}: target caption differs from draft old_caption; re-make the draft first")
            continue
        t["caption"], t["expectation"] = d["caption"], d["expectation"]
        applied.append(i)

    if errors:
        for e in errors:
            print("ERROR", e)
        print("nothing written")
        return 1
    target_path.write_text(json.dumps(target, indent=2, ensure_ascii=False) + "\n")
    print(f"{target_path}: applied {len(applied)}, already applied {len(already)}, delete-tagged skipped {len(skipped)}")
    if applied:
        print("applied:", " ".join(applied))
    if skipped:
        print("skipped (delete):", " ".join(skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
