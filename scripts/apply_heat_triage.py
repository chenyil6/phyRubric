#!/usr/bin/env python3
"""Apply the reviewed Heat triage to data/train/heat.json.

Inputs : data/drafts/heat_draft.json  (person/timescale rewrites)   data/drafts/heat_draft_triage.json (verdicts)
Rules  : drop user_delete + drop_must; REPLACE swaps whole records in place; trim every phenomenon group to <= 8 (user: "6-8"); apply the 17 modify rewrites;
         add 10 new seconds-scale records for under-covered phenomena; renumber HEAT-0001..N in file order.
Outputs: data/train/heat.json, data/heat_id_map.json (old->new; null = removed), data/drafts/removed_heat.json,
         renamed/retired videos + rewritten rows in gen_videos/manifests/<tag>.jsonl (non-_old tags only),
         then `python data/build.py build`.

    python scripts/apply_heat_triage.py            # dry run
    python scripts/apply_heat_triage.py --apply
"""
import json, re, subprocess, sys
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = Path("/work/hdd/bilw/hchen56/phyRubric_outputs")
DRAFT = ROOT / "data/drafts/heat_draft.json"
TRIAGE = ROOT / "data/drafts/heat_draft_triage.json"
TARGET = ROOT / "data/train/heat.json"
apply = "--apply" in sys.argv

# group trims decided with the user (keep 6-8 per phenomenon)
TRIM = {
    "HEAT-0030": "凝固/定型 14→8：盖章需要手，与 0028 重复", "HEAT-0031": "凝固/定型：与 0027 重复", "HEAT-0037": "凝固/定型：巧克力冷凝，与 0027 重复",
    "HEAT-0038": "凝固/定型：手指是主体", "HEAT-0040": "凝固/定型：与 0028 重复", "HEAT-0050": "凝固/定型：巧克力冷凝，与 0027 重复",
    "HEAT-0014": "冰/雪融化 10→7：热路面小冰雹的时间尺度勉强", "HEAT-0016": "冰/雪融化：雪花太小，480p 看不清", "HEAT-0021": "冰/雪融化：狗 + 需改写，最弱的一条",
    "HEAT-0061": "静态汽羽 10→7：静态弥漫，只能判不下沉", "HEAT-0077": "静态汽羽：与 0063 重复", "HEAT-0089": "静态汽羽：烘干太慢",
    "HEAT-0121": "冷容器结露 14→7", "HEAT-0125": "冷容器结露 14→7", "HEAT-0134": "冷容器结露 14→7：罐口内侧场景别扭",
    "HEAT-0141": "冷容器结露 14→7：大理石出汗难渲染", "HEAT-0142": "冷容器结露 14→7", "HEAT-0144": "冷容器结露 14→7", "HEAT-0147": "冷容器结露 14→7",
    "HEAT-0204": "受热膨胀 11→8：与 0249/0225 重复", "HEAT-0218": "受热膨胀：需要手按", "HEAT-0249": "受热膨胀：与 0225 重复",
    "HEAT-0189": "燃料消耗 10→8：手指在画面里", "HEAT-0183": "燃料消耗 10→8：与 0189 重复，手是目标",
    "HEAT-0165": "熄灭 11→8：与 0012/0152 重复", "HEAT-0180": "熄灭 11→8：打火机合盖太平凡", "HEAT-0200": "熄灭 11→8：手指捏灭，与 0162 重复",
    "HEAT-0140": "眼镜起雾 6→5：厨师凑近烤箱，人不是物理",
    "HEAT-0154": "点燃 11→7：与 0184 重复", "HEAT-0178": "点燃：与 0161 重复", "HEAT-0191": "点燃：纸灯笼画面弱", "HEAT-0194": "点燃：热水器引火冷僻",
}
# small expectation fix agreed in review
EXP_FIX = {"HEAT-0001": "The ice cream sags and drips run downward and pool at the base; it never firms back up or drips upward."}
# whole-record swaps decided with the user (old id keeps its slot; content replaced)
REPLACE = {
    "HEAT-0067": {   # campfire tripod pot boiling (dup of 0053) -> yin-yang hot pot: spicy side boils first
        "caption": "A divided hot pot with spicy red oil broth on one side and clear broth on the other heats over a burner, and the red side comes to the boil while the clear side stays calm.",
        "expectation": "Large bubbles rise and burst through the red oil layer and its surface churns, while the clear side stays nearly flat with at most a few tiny bubbles and faint steam; the two broths stay on their own sides of the divider and keep their colours; the red side does not fall quiet while the burner is on, and the clear side does not boil harder than the red side.",
        "violation_types": ["material_response", "process_direction", "attribute_drift"]},
}

def new(sub, cap, exp, vts):
    return {"id": None, "caption": cap, "category": "Heat", "subcategory": sub, "violation_types": vts, "expectation": exp}
NEW = {
 "melt_freeze": [
  new("melt_freeze", "A handful of chocolate chips is dropped into a saucepan of hot cream, and the chips melt into the cream.",
      "The chips soften, lose their sharp edges and go glossy, sinking or smearing into the cream while dark streaks spread through the pale cream; the chips do not stay hard-edged, float unchanged, or re-harden in the hot cream.",
      ["process_direction", "material_response"]),
  new("melt_freeze", "A square of chocolate lies in a skillet over low heat, and it melts into a spreading pool.",
      "The square goes glossy and sags from the bottom, its edges round off and a pool spreads out around it; it does not keep sharp edges, re-harden in the warm pan, or turn pale.",
      ["process_direction", "material_response"]),
  new("melt_freeze", "Hot espresso is poured over a scoop of vanilla ice cream in a glass, and the ice cream melts.",
      "The scoop softens and shrinks where the hot coffee runs over it, and pale melted cream runs down and streaks into the dark coffee at the bottom of the glass; the scoop does not stay a firm ball, grow, or refreeze in the hot liquid.",
      ["process_direction", "material_response"])],
 "boil_steam": [
  new("boil_steam", "A glass electric kettle at a rolling boil clicks off, and the churning bubbles die down and the steam thins.",
      "The streams of bubbles from the base stop within moments of the click and the surface settles, while the steam from the spout weakens gradually; the water does not keep boiling hard with the element off or fall still in a single frame.",
      ["process_direction", "causeless_motion"]),
  new("boil_steam", "A saucepan of boiling water sits on an induction hob that switches off, and the boiling subsides.",
      "The large bubbles shrink to a few small ones and stop within moments of the hob going dark, while steam still rises from the hot water; the water does not keep churning with the hob off or stop the instant it switches.",
      ["process_direction", "causeless_motion"]),
  new("boil_steam", "A garment steamer is run slowly down a wrinkled shirt hanging on a rail, and the creases relax and drop out where the steam passes.",
      "Steam rises from the steamer head, the fabric darkens slightly with moisture and smooths only along the path the head has taken; creases do not come back once steamed and untreated areas stay wrinkled.",
      ["process_direction", "missing_consequence"])],
 "condensation": [
  new("condensation", "A dog waits alone in a parked car on a cold evening, and the windows fog up from the inside as it pants.",
      "The fog forms on the inside face of the glass, thickest near the dog and toward the top, and grows while the dog pants; it does not form on the outside of the windows or clear while the car stays shut.",
      ["process_direction", "attribute_drift"]),
  new("condensation", "A car's defroster is switched on against a windshield fogged from the inside, and a clear patch spreads upward from the vents.",
      "The glass clears first just above the dashboard vents and the clear area grows upward and outward; the fog does not thicken while the defroster runs and does not clear from the top down.",
      ["process_direction", "missing_consequence"]),
  new("condensation", "Chunks of dry ice are dropped into a punch bowl of water, and thick white fog boils up, spills over the rim and sinks toward the table.",
      "The fog rises out of the bowl, pours over the rim, flows down the outside and spreads along the table, thinning as it goes, while the water bubbles; it does not drift up to the ceiling like steam.",
      ["gravity_direction", "process_direction"]),
  new("condensation", "Liquid nitrogen is poured into a metal bowl, and a cloud of white fog rolls over the rim and cascades down the sides.",
      "The liquid boils violently in the bowl and the fog spills downward over the edge, hugging the surface it falls onto and thinning as it spreads; the fog does not drift upward like steam.",
      ["gravity_direction", "process_direction"])],
 "burn_smoke": [],
 "heat_response": [
  new("heat_response", "A hairdryer is aimed at a wet patch on a bathroom mirror, and the patch shrinks from its edges.",
      "The dry area spreads from where the warm air hits and the border of the wet patch retreats inward; the patch does not grow or reappear where it has dried.",
      ["process_direction", "permanence_count"]),
  new("heat_response", "Wet footprints on a sun-baked pool deck dry in the heat, shrinking and fading from their edges.",
      "Each print fades from its thin edges inward, the dark wet area getting smaller and lighter; prints do not darken, spread, or reappear once gone.",
      ["process_direction", "permanence_count"]),
  new("heat_response", "An egg is cracked into a hot frying pan, and the clear white turns opaque white from the edges inward.",
      "The white sets and whitens first where it touches the hot pan and the change spreads inward while the yolk stays yellow and domed; the set white does not turn clear again and the egg does not slide around as one piece before it sets.",
      ["process_direction", "attribute_drift"])],
}

draft = {r["id"]: r for r in json.loads(DRAFT.read_text())}
triage = {r["id"]: r for r in json.loads(TRIAGE.read_text())}
current = list(draft.values())   # draft carries id order + violation_types; heat.json itself is regenerated
assert list(draft) == list(triage)

kept, removed = [], []
for old in current:
    oid, d, t = old["id"], draft[old["id"]], triage[old["id"]]
    rec = {"id": oid, "caption": d["caption"], "category": "Heat", "subcategory": d["subcategory"],
           "violation_types": old["violation_types"], "expectation": d["expectation"]}
    if t["verdict"] in ("user_delete", "drop_must"):
        removed.append({**rec, "reason": f"{t['verdict']}: {t['note']}"}); continue
    if oid in TRIM:
        removed.append({**rec, "reason": f"trim: {TRIM[oid]}"}); continue
    if t["verdict"] == "modify":
        rec["caption"], rec["expectation"] = t["new_caption"], t["new_expectation"]
    if oid in EXP_FIX:
        rec["expectation"] = EXP_FIX[oid]
    if oid in REPLACE:
        rec.update(REPLACE[oid])
    kept.append(rec)
assert not (set(TRIM) - set(current and draft)), "TRIM id typo"
for oid in TRIM: assert triage[oid]["verdict"] not in ("user_delete", "drop_must"), oid

# insert new records at the end of each subcategory block
final = []
for sub in ("melt_freeze", "boil_steam", "condensation", "burn_smoke", "heat_response"):
    block = [r for r in kept if r["subcategory"] == sub]
    for k, n in enumerate(NEW[sub], 1):
        n["id"] = f"NEW-{sub}-{k}"
        block.append(n)
    final += block
assert len(final) == len(kept) + sum(map(len, NEW.values()))

mapping = OrderedDict()
for i, r in enumerate(final, 1):
    mapping[r["id"]] = f"HEAT-{i:04d}"
for r in removed:
    mapping[r["id"]] = None
mapping = OrderedDict(sorted(mapping.items(), key=lambda kv: (not kv[0].startswith("HEAT"), kv[0])))

print(f"current {len(current)}  removed {len(removed)} (user_delete/drop_must {sum(1 for r in removed if not r['reason'].startswith('trim'))}, trim {sum(1 for r in removed if r['reason'].startswith('trim'))})  "
      f"kept {len(kept)}  new {sum(map(len, NEW.values()))}  final {len(final)}")
print("final per subcategory:", dict(Counter(r["subcategory"] for r in final)))
changed_ids = sum(1 for r in final if r["id"] != mapping[r["id"]])
print(f"{changed_ids} ids change; first unchanged run: {[r['id'] for r in final if r['id'] == mapping[r['id']]][:12]}")

# videos + manifests (fresh tags only; *_old snapshots keep the pre-triage ids, bridged by the id map).
# Rows are matched by CAPTION, not id, so the script can be re-run after ids have already been renumbered:
# a row whose caption is still in the final set is renamed to that record's new id; any other row is retired.
by_caption = {}
for r in final:
    assert r["caption"].strip() not in by_caption, f"duplicate caption: {r['caption']}"
    by_caption[r["caption"].strip()] = r
plan = []   # (src, dst or None=retire, note)   /   (manifest_path, rows, note)
for mf in sorted((ROOT / "gen_videos/manifests").glob("*.jsonl")):
    if mf.stem.endswith("_old"): continue
    rows = [json.loads(l) for l in mf.read_text().splitlines() if l.strip()]
    keep_rows, touched = [], 0
    for row in rows:
        rid = row.get("id", "")
        if not (isinstance(rid, str) and rid.startswith("HEAT-")):
            keep_rows.append(row); continue
        touched += 1
        src = Path(row["output_path"])
        rec = by_caption.get(str(row.get("caption", "")).strip())
        if rec is None:
            plan.append((src, None, f"{mf.name}: {rid} caption no longer in heat.json -> retire video, drop row"))
            continue
        nid = mapping[rec["id"]]
        dst = src.with_name(nid + src.name[src.name.index("_s"):])
        row["id"], row["output_path"] = nid, str(dst)
        keep_rows.append(row)
        plan.append((src, dst, f"{mf.name}: {rid} -> {nid}" + (" (unchanged)" if src == dst else "")))
    if touched:
        plan.append((mf, keep_rows, f"rewrite {mf.name}: {len(keep_rows)}/{len(rows)} rows kept"))
for src, dst, note in plan:
    if not (isinstance(dst, Path) and src == dst): print("  ", note)
print(f"   ({sum(1 for s_, d_, _ in plan if isinstance(d_, Path) and s_ == d_)} manifest rows unchanged)")

if not apply:
    print("dry run only; pass --apply to write"); sys.exit(0)

for r in final: r["id"] = mapping[r["id"]]
TARGET.write_text(json.dumps(final, indent=2, ensure_ascii=False) + "\n")
(ROOT / "data/drafts/removed_heat.json").write_text(json.dumps(removed, indent=2, ensure_ascii=False) + "\n")
(ROOT / "data/heat_id_map.json").write_text(json.dumps({
    "note": f"Heat train ids renumbered on {date.today()} after the caption triage (data/drafts/heat_draft_triage.md): "
            f"{len(current)} -> {len(final)} records (HEAT-0001..HEAT-{len(final):04d}). Keys are the pre-triage ids "
            "(the ones used in gen_videos/manifests/*_old.jsonl and phyRubric_outputs/*_old/), values the new ids; null = removed "
            "(archived with reasons in data/drafts/removed_heat.json); NEW-* keys are records added by the triage. Eval ids HEAT-0251..0300 untouched.",
    "old_to_new": mapping}, indent=2, ensure_ascii=False) + "\n")
stale_dir_name = f"stale_{date.today()}"
renames = []
for src, dst, note in plan:
    if isinstance(dst, list):
        src.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in dst)); continue
    if not src.exists(): print("   (missing video)", src); continue
    if dst is None:
        sd = src.parent / stale_dir_name; sd.mkdir(exist_ok=True)
        src.rename(sd / src.name)
    elif dst != src:
        renames.append((src, dst))
# two-phase rename so a shifted id never overwrites a video that has not moved yet
tmp = [(src, src.with_name("__renum__" + dst.name)) for src, dst in renames]
for src, t in tmp: src.rename(t)
for (_, t), (_, dst) in zip(tmp, renames):
    assert not dst.exists(), dst
    t.rename(dst)
print("written; running data/build.py build")
sys.exit(subprocess.call([sys.executable, str(ROOT / "data/build.py"), "build"]))
