#!/usr/bin/env python3
"""Copy videos whose caption did not change from the <tag>_old snapshot into the fresh <tag>/ directory.

    python scripts/reuse_old_videos.py MECH-0001:MECH-0050 --tags CogVideoX1.5-5B Wan2.2-T2V-A14B LTX-Video-2B-0.9.8-distilled
    python scripts/reuse_old_videos.py HEAT-0001:HEAT-0050 --tags LTX-Video-2B-0.9.8-distilled --id-map data/heat_id_map.json

For every row of gen_videos/manifests/<tag>_old.jsonl whose id is selected: if the row's caption is identical to
the caption now in data/train.json or data/eval.json, the mp4 is copied (not moved) to <out-root>/<tag>/<split>/ and the
row is appended to gen_videos/manifests/<tag>.jsonl with output_path pointing at the copy and `copied_from` set.
Rows whose caption changed are listed as stale and left alone; files already present in the fresh dir are skipped.
generate.py then skips the copied ids and renders only the stale ones.

--id-map: JSON with an "old_to_new" dict for branches whose ids were renumbered AFTER the _old snapshot was taken
(Heat). Old-manifest ids are translated through it before matching; null = record removed; ids not in the map are
kept as they are. Selection ranges refer to the NEW ids. The copy is renamed to <new_id>_s<seed>.mp4 and the manifest
row carries `old_id`.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ROOT / "gen_videos" / "manifests"
OUT_ROOT = Path("/work/hdd/bilw/hchen56/phyRubric_outputs")


def expand(spec: str, order: list[str]) -> list[str]:
    if ":" in spec:
        lo, hi = spec.split(":")
        return order[order.index(lo):order.index(hi) + 1]
    return [spec]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+", help="ids or ranges like MECH-0001:MECH-0050 (new ids when --id-map is used)")
    ap.add_argument("--tags", nargs="+", required=True)
    ap.add_argument("--id-map", type=Path, help="JSON with old_to_new for renumbered branches (e.g. data/heat_id_map.json)")
    ap.add_argument("--id-map-key", default="old_to_new", help="which dict inside --id-map to use (Mechanics _old snapshots: sep10_to_final)")
    ap.add_argument("--out-root", type=Path, default=OUT_ROOT)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    current: dict[str, str] = {}
    split_of: dict[str, str] = {}
    order: list[str] = []
    for split in ("train", "eval"):
        for r in json.loads((ROOT / "data" / f"{split}.json").read_text()):
            current[r["id"]] = r["caption"]
            split_of[r["id"]] = split
            order.append(r["id"])
    selected = {i for s in a.ids for i in expand(s, order)}
    id_map: dict[str, str | None] = json.loads(a.id_map.read_text())[a.id_map_key] if a.id_map else {}

    for tag in a.tags:
        old_manifest = MANIFESTS / f"{tag}_old.jsonl"
        new_manifest = MANIFESTS / f"{tag}.jsonl"
        fresh_dir = a.out_root / tag
        rows = []
        for l in old_manifest.read_text().splitlines():
            if not l.strip():
                continue
            r = json.loads(l)
            new_id = id_map.get(r["id"], r["id"])
            if new_id is None or new_id not in selected:
                continue
            rows.append((r, new_id))
        copied, stale, present, missing = [], [], [], []
        for r, new_id in rows:
            if r["caption"] != current.get(new_id):
                stale.append(new_id)
                continue
            src = Path(r["output_path"])
            dst = fresh_dir / split_of[new_id] / src.name.replace(r["id"], new_id, 1)
            if dst.exists():
                present.append(new_id)
                continue
            if not src.exists():
                missing.append(new_id)
                continue
            if not a.dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                row = dict(r, id=new_id, split=split_of[new_id], output_path=str(dst), copied_from=str(src))
                if new_id != r["id"]:
                    row["old_id"] = r["id"]
                with new_manifest.open("a") as f:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
            copied.append(new_id)
        print(f"{tag}: selected {len(rows)} | copied {len(copied)} | stale (caption changed) {len(stale)} | "
              f"already present {len(present)} | source missing {len(missing)}{'  [dry run]' if a.dry_run else ''}")
        if copied:
            print("  copied:", " ".join(sorted(copied)))
        if stale:
            print("  stale: ", " ".join(sorted(stale)))
        if present:
            print("  present:", " ".join(sorted(present)))
        if missing:
            print("  missing:", " ".join(sorted(missing)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
