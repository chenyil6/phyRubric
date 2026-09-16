#!/usr/bin/env python3
"""Renumber Mechanics ids contiguously and rename everything that carries them.

Old ids had gaps (38 records were culled from a 288-record draft). New scheme, in file order:
train MECH-0001..0250, eval MECH-0251..0300, drafts/removed_mechanics.json MECH-0301..0338.
Rewrites the three json files, renames <out-root>/<model>/MECH-XXXX_s<seed>.mp4 for every model
directory, rewrites `id` and `output_path` in gen_videos/manifests/*.jsonl, and saves the
old->new map to data/mechanics_id_map.json. Then run `python data/build.py build`.

    python scripts/renumber_mechanics_ids.py            # dry run: print the plan
    python scripts/renumber_mechanics_ids.py --apply
"""
import json, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = Path("/work/hdd/bilw/hchen56/phyRubric_outputs")
FILES = [("train", ROOT / "data/train/mechanics.json", 1),
         ("eval", ROOT / "data/eval/mechanics.json", 251),
         ("removed", ROOT / "data/drafts/removed_mechanics.json", 301)]
apply = "--apply" in sys.argv

mapping: dict[str, str] = {}
new_sets = {}
for name, path, start in FILES:
    recs = json.loads(path.read_text())
    for i, r in enumerate(recs):
        new = f"MECH-{start + i:04d}"
        assert r["id"] not in mapping, r["id"]
        mapping[r["id"]] = new
    new_sets[name] = (path, recs, [f"MECH-{start + i:04d}" for i in range(len(recs))])
    print(f"{name:8s} {len(recs):3d} records: {recs[0]['id']}..{recs[-1]['id']} -> MECH-{start:04d}..MECH-{start + len(recs) - 1:04d}")
assert len(set(mapping.values())) == len(mapping)
changed = sum(1 for k, v in mapping.items() if k != v)
print(f"{len(mapping)} ids, {changed} change, {len(mapping) - changed} unchanged")

# videos
pat = re.compile(r"^(MECH-\d{4})(_s\d+\.mp4)$")
renames: list[tuple[Path, Path]] = []
for model_dir in sorted(p for p in OUT_ROOT.iterdir() if p.is_dir()):
    n = 0
    for f in sorted(model_dir.iterdir()):
        m = pat.match(f.name)
        if not m:
            continue
        old_id, rest = m.groups()
        if old_id not in mapping:
            raise SystemExit(f"{f}: id not in mapping")
        renames.append((f, model_dir / (mapping[old_id] + rest)))
        n += 1
    if n:
        print(f"videos  {model_dir.name}: {n} files")
targets = [t for _, t in renames]
assert len(set(targets)) == len(targets)

# manifests
man_rows = {}
for mf in sorted((ROOT / "gen_videos/manifests").glob("*.jsonl")):
    rows = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
    touched = 0
    for r in rows:
        if isinstance(r.get("id"), str) and r["id"].startswith("MECH-"):
            new = mapping[r["id"]]
            if "output_path" in r:
                r["output_path"] = r["output_path"].replace(r["id"] + "_s", new + "_s")
            r["id"] = new
            touched += 1
    man_rows[mf] = (rows, touched)
    print(f"manifest {mf.name}: {touched}/{len(rows)} rows")

if not apply:
    print("dry run only; pass --apply to write"); sys.exit(0)

for name, (path, recs, new_ids) in new_sets.items():
    for r, new in zip(recs, new_ids):
        r["id"] = new
    path.write_text(json.dumps(recs, indent=2, ensure_ascii=False) + "\n")
(ROOT / "data/mechanics_id_map.json").write_text(json.dumps(
    {"note": f"Mechanics ids renumbered contiguously on {date.today()}: train 0001-0250, eval 0251-0300, "
             "removed drafts 0301-0338. Keys are the old ids, values the new ones.",
     "old_to_new": mapping}, indent=2) + "\n")
# two-phase rename so no target is ever overwritten by a not-yet-moved source
tmp = [(src, src.with_name("__renum__" + dst.name)) for src, dst in renames]
for src, t in tmp:
    src.rename(t)
for (_, t), (_, dst) in zip(tmp, renames):
    assert not dst.exists(), dst
    t.rename(dst)
for mf, (rows, _) in man_rows.items():
    mf.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
print(f"applied: {len(renames)} videos renamed, {len(man_rows)} manifests rewritten, 3 json files + id map written")
