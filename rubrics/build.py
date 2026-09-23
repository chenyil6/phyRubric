#!/usr/bin/env python3
"""Validate, merge and render the rubric set.

    python rubrics/build.py check [--split train|eval] [--category Heat] [--ids ID ...]
    python rubrics/build.py build                       # check everything, then write rubrics/train.json and rubrics/eval.json
    python rubrics/build.py review OUT.md [--split S] [--category C] [--ids ID ...]   # markdown for human review

Layout: one JSON file per caption at rubrics/<split>/<branch>/<ID>.json, <branch> = lower-case category name
(same as data/<split>/<branch>.json). The file name must equal the id. Fields: id, caption (verbatim copy of
the data caption), sa, pc, note (optional). See rubrics/_policy.json for the item format and scoring rules.

Checks (errors): file/dir placement, caption matches data, allowed keys only, S1../P1.. sequential ids, valid
weight/severity/type, non-empty texts, 2-7 SA items and 4-8 PC items, band reachability (>=2 core SA, >=1 minor SA,
unconditional core+major+minor PC, fatal or second heavy unconditional PC), no duplicate fail text.
Warnings: numeric thresholds, single-event fail text, vague wording (realistic, properly, ...), SA items that judge physics,
SA items that restate a PC expect (word overlap) or are hypothetical / conditional (would, if, when X - X not in the caption),
a declared violation_type on the data record not covered by any PC item's type.

The merged train.json / eval.json are products, not sources: records in data order with category and
subcategory copied in from data. Do not edit them by hand.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data"
SCHEMA = json.loads((DATA / "schema.json").read_text())
CATEGORIES = list(SCHEMA["subcategories"])
TYPES = set(SCHEMA["violation_types"])
SPLITS = ("train", "eval")
SEVERITIES = ("fatal", "core", "major", "minor")
WEIGHTS = ("core", "minor")
RECORD_KEYS = {"id", "caption", "sa", "pc", "note"}
SA_KEYS = {"id", "weight", "check"}
PC_KEYS = {"id", "severity", "type", "expect", "fail", "precondition"}
NUM = re.compile(r"\b\d+\s*(cm|mm|m|s|ms|sec|seconds?|deg|degrees|%|kg|g|ml|l|fps|x)\b", re.I)
VAGUE = re.compile(r"\b(unrealistic(?:ally)?|implausibl[ey]|realistic(?:ally)?|plausibl[ey]|correctly|incorrectly|properly|appropriately|unnatural(?:ly)?|convincing(?:ly)?)\b", re.I)
VAGUE_SA = re.compile(r"\b(physic\w*|realistic\w*|plausibl\w*|correct\w*|natural\w*)\b", re.I)
HYPO_SA = re.compile(r"\b(would|if any|if (it|the|they|one|released|moved|switched|turned))\b", re.I)
_STOP = set("a an the and or of to in on at by with from into onto over under through as is are it its they them their this that "
            "there then while when after before only not no one two his her he she be been being".split())
SA_PC_OVERLAP = 0.6  # Jaccard on content words between an SA check and a PC expect -> the SA item restates physics


def _stem(w: str) -> str:
    if w in ("lens", "glass", "grass", "bus", "gas"):
        return w
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("es") and w[:-2].endswith(("s", "x", "z", "ch", "sh")):
        return w[:-2]
    if w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def _words(text: str) -> set[str]:
    return {_stem(w) for w in re.findall(r"[a-z]+", text.lower()) if w not in _STOP and len(w) > 2}


def branch(category: str) -> str:
    return category.lower()


def load_data() -> dict[str, tuple[str, dict]]:
    """id -> (split, record) for every caption in data/."""
    out: dict[str, tuple[str, dict]] = {}
    for split in SPLITS:
        for cat in CATEGORIES:
            path = DATA / split / f"{branch(cat)}.json"
            if path.exists():
                for rec in json.loads(path.read_text()):
                    out[rec["id"]] = (split, rec)
    return out


def rubric_files(split: str | None = None, category: str | None = None) -> list[Path]:
    files: list[Path] = []
    for s in SPLITS if split is None else (split,):
        for cat in CATEGORIES if category is None else (category,):
            d = ROOT / s / branch(cat)
            if d.is_dir():
                files.extend(sorted(d.glob("*.json")))
    return files


def validate(rubric: dict, path: Path, data: dict[str, tuple[str, dict]]) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    rid = rubric.get("id", "?")
    tag = str(path.relative_to(ROOT))
    if path.stem != rid:
        errs.append(f"{tag}: file name does not match id {rid!r}")
    if rid not in data:
        errs.append(f"{tag}: id {rid!r} not in data/")
        return errs, warns
    split, rec = data[rid]
    if path.parent.name != branch(rec["category"]) or path.parent.parent.name != split:
        errs.append(f"{tag}: should live at {split}/{branch(rec['category'])}/{rid}.json")
    if rubric.get("caption") != rec["caption"]:
        errs.append(f"{tag}: caption differs from data (rubric is stale or mistyped)")
    extra = set(rubric) - RECORD_KEYS
    if extra:
        errs.append(f"{tag}: stray record keys {sorted(extra)}")
    if "note" in rubric and not str(rubric["note"]).strip():
        errs.append(f"{tag}: empty note (drop the key instead)")

    sa = rubric.get("sa") or []
    pc = rubric.get("pc") or []
    if not 2 <= len(sa) <= 7:
        errs.append(f"{tag}: {len(sa)} SA items (want 2-7)")
    if not 4 <= len(pc) <= 8:
        errs.append(f"{tag}: {len(pc)} PC items (want 4-8)")
    if [x.get("id") for x in sa] != [f"S{k + 1}" for k in range(len(sa))]:
        errs.append(f"{tag}: SA ids not sequential S1..S{len(sa)}")
    if [x.get("id") for x in pc] != [f"P{k + 1}" for k in range(len(pc))]:
        errs.append(f"{tag}: PC ids not sequential P1..P{len(pc)}")
    for x in sa:
        xid = x.get("id", "?")
        if set(x) - SA_KEYS or set(SA_KEYS) - set(x):
            errs.append(f"{tag}/{xid}: SA keys must be exactly {sorted(SA_KEYS)}")
        if x.get("weight") not in WEIGHTS:
            errs.append(f"{tag}/{xid}: bad weight {x.get('weight')!r}")
        if not str(x.get("check", "")).strip():
            errs.append(f"{tag}/{xid}: empty check")
    for x in pc:
        xid = x.get("id", "?")
        if set(x) - PC_KEYS or {"id", "severity", "type", "expect", "fail"} - set(x):
            errs.append(f"{tag}/{xid}: PC keys must be id, severity, type, expect, fail [, precondition]")
        if x.get("severity") not in SEVERITIES:
            errs.append(f"{tag}/{xid}: bad severity {x.get('severity')!r}")
        if x.get("type") not in TYPES:
            errs.append(f"{tag}/{xid}: type {x.get('type')!r} is not one of the ten violation_types")
        for k in ("expect", "fail"):
            if not str(x.get(k, "")).strip():
                errs.append(f"{tag}/{xid}: empty {k}")
        if "precondition" in x and not str(x["precondition"]).strip():
            errs.append(f"{tag}/{xid}: empty precondition (drop the key instead)")
        if NUM.search(str(x.get("expect", "")) + " " + str(x.get("fail", ""))):
            warns.append(f"{tag}/{xid}: looks like a numeric threshold")
        fail_text = str(x.get("fail", ""))
        if fail_text and not re.search(r";\s*or\b|\bor\b", fail_text):
            warns.append(f"{tag}/{xid}: fail names a single event (list the distinct visible ways it can go wrong, joined by 'or')")
        vague = VAGUE.findall(str(x.get("expect", "")) + " " + fail_text)
        if vague:
            warns.append(f"{tag}/{xid}: vague wording {sorted(set(v.lower() for v in vague))} (name the visible event instead)")
    cap_words = _words(rubric.get("caption", ""))
    for x in sa:
        check = str(x.get("check", ""))
        xid = x.get("id", "?")
        if VAGUE_SA.search(check):
            warns.append(f"{tag}/{xid}: SA check judges physics or quality; SA asks only whether the caption's content is shown")
        if HYPO_SA.search(check):
            warns.append(f"{tag}/{xid}: SA check is hypothetical or conditional ('would' / 'if'); SA must be decidable on every clip")
        cw = _words(check)
        novel = cw - cap_words  # words the caption itself does not use
        if cw and x.get("weight") == "minor" and len(novel) / len(cw) >= 0.5 and not re.search(r"comes first|follows|\border\b|\bthen\b", check, re.I):
            for y in pc:
                if y.get("type") == "permanence_count":
                    continue  # "one X and one Y" templates overlap any stated count or object list
                ew = _words(str(y.get("expect", "")))
                if ew and len(cw & ew) / len(cw | ew) >= SA_PC_OVERLAP:
                    warns.append(f"{tag}/{xid}: SA check restates {y.get('id', '?')}'s expect; SA states caption content, PC judges physics")
                    break
        m = re.search(r"\bwhen (.+?)(,|\.|;|$)", check, re.I)
        if m:
            ww = _words(m.group(1))
            if ww and len(ww & cap_words) / len(ww) < 0.34:
                warns.append(f"{tag}/{xid}: SA check depends on an event the caption does not state ('when {m.group(1).strip()}')")

    # Band reachability. SA: one minor can fail alone (4), one core alone (3), two cores (2).
    w = [x.get("weight") for x in sa]
    if w.count("core") < 2:
        errs.append(f"{tag}: fewer than 2 core SA items -> SA 2 unreachable")
    if w.count("minor") < 1:
        errs.append(f"{tag}: no minor SA item -> SA 4 unreachable")
    # PC: only items without a precondition can fail on every clip.
    u = [x.get("severity") for x in pc if not x.get("precondition")]
    for sev, band in (("core", 2), ("major", 3), ("minor", 4)):
        if sev not in u:
            errs.append(f"{tag}: no unconditional {sev} PC item -> PC {band} unreachable")
    heavy = sum(1 for s in u if s in ("fatal", "core", "major"))
    if "fatal" not in u and not ("core" in u and heavy >= 2):
        errs.append(f"{tag}: PC 1 unreachable (need an unconditional fatal, or core plus another heavy item)")
    fails = [x.get("fail") for x in pc]
    if len(set(fails)) != len(fails):
        errs.append(f"{tag}: duplicate fail text")
    # Presentation order (see _policy.json pc.order / sa): core -> major -> fatal -> minor; SA core before minor.
    sev = [x.get("severity") for x in pc]
    rank = {"core": 0, "major": 1, "fatal": 2, "minor": 3}
    if all(s in rank for s in sev) and [rank[s] for s in sev] != sorted(rank[s] for s in sev):
        warns.append(f"{tag}: PC order is {' '.join(s[0] for s in sev)}; convention is core items, then major, then fatal, then minor")
    if pc and sev[-1] != "minor":
        warns.append(f"{tag}: last PC item should be the minor attribute_drift item")
    if w and w != sorted(w, key=lambda s: 0 if s == "core" else 1):
        warns.append(f"{tag}: SA order puts a core item after a minor one; core items come first")

    covered = {x.get("type") for x in pc}
    missing = [t for t in rec.get("violation_types", []) if t not in covered]
    if missing:
        warns.append(f"{tag}: data violation_types {missing} not covered by any PC item type")
    return errs, warns


def check(split: str | None, category: str | None, ids: list[str] | None, quiet: bool = False) -> tuple[list[dict], bool]:
    data = load_data()
    files = rubric_files(split, category)
    if ids:
        want = set(ids)
        files = [f for f in files if f.stem in want]
    rubrics: list[dict] = []
    all_errs: list[str] = []
    all_warns: list[str] = []
    seen: Counter[str] = Counter()
    for path in files:
        try:
            rubric = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            all_errs.append(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
            continue
        seen[rubric.get("id", "?")] += 1
        errs, warns = validate(rubric, path, data)
        all_errs += errs
        all_warns += warns
        rubrics.append(rubric)
    for rid, n in seen.items():
        if n > 1:
            all_errs.append(f"id {rid} appears in {n} files")
    if not quiet:
        for e in all_errs:
            print("ERROR", e)
        for w in all_warns:
            print("warn ", w)
        # Coverage per split/category.
        have = {r["id"] for r in rubrics}
        rows = []
        for s in SPLITS if split is None else (split,):
            for cat in CATEGORIES if category is None else (category,):
                ids_in_data = [rid for rid, (sp, rec) in data.items() if sp == s and rec["category"] == cat]
                if ids_in_data:
                    n = sum(1 for rid in ids_in_data if rid in have)
                    rows.append((s, cat, n, len(ids_in_data)))
        print(f"\n{'split':6s} {'category':12s} rubrics/captions")
        for s, cat, n, total in rows:
            print(f"{s:6s} {cat:12s} {n:4d}/{total}")
        print(f"\n{len(rubrics)} rubrics checked, {len(all_errs)} errors, {len(all_warns)} warnings")
    return rubrics, not all_errs


def build() -> int:
    rubrics, ok = check(None, None, None)
    if not ok:
        print("not writing merged files: fix the errors first")
        return 1
    data = load_data()
    by_id = {r["id"]: r for r in rubrics}
    for split in SPLITS:
        merged = []
        for cat in CATEGORIES:
            path = DATA / split / f"{branch(cat)}.json"
            if not path.exists():
                continue
            for rec in json.loads(path.read_text()):
                r = by_id.get(rec["id"])
                if r is None:
                    continue
                out = {"id": r["id"], "category": rec["category"], "subcategory": rec["subcategory"], "caption": r["caption"], "sa": r["sa"], "pc": r["pc"]}
                if r.get("note"):
                    out["note"] = r["note"]
                merged.append(out)
        (ROOT / f"{split}.json").write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n")
        print(f"wrote {split}.json ({len(merged)} rubrics)")
    return 0


def render(rubrics: list[dict], data: dict[str, tuple[str, dict]]) -> str:
    lines = ["# Rubric review", ""]
    lines.append(f"{len(rubrics)} rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.")
    lines.append("")
    order = {c: i for i, c in enumerate(CATEGORIES)}
    rubrics = sorted(rubrics, key=lambda r: (order[data[r["id"]][1]["category"]], r["id"]))
    current = None
    for r in rubrics:
        split, rec = data[r["id"]]
        if rec["category"] != current:
            current = rec["category"]
            lines += [f"# {current}", ""]
        lines.append(f"## {r['id']} · {rec['subcategory']} · {split}")
        lines.append("")
        lines.append(f"**Caption.** {r['caption']}")
        lines.append("")
        lines.append(f"**Expectation (hidden).** {rec['expectation']}")
        lines.append("")
        lines.append(f"**Declared violation types.** {', '.join(rec['violation_types'])}")
        lines.append("")
        lines.append("**SA**")
        for x in r["sa"]:
            lines.append(f"- {x['id']} [{x['weight']}] {x['check']}")
        lines.append("")
        lines.append("**PC**")
        for x in r["pc"]:
            head = f"- {x['id']} [{x['severity']} · {x['type']}]"
            if x.get("precondition"):
                head += f" (if: {x['precondition']})"
            lines.append(head)
            lines.append(f"  - expect: {x['expect']}")
            lines.append(f"  - fail: {x['fail']}")
        if r.get("note"):
            lines.append("")
            lines.append(f"**Note.** {r['note']}")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("check", "review"):
        p = sub.add_parser(name)
        if name == "review":
            p.add_argument("out", help="markdown file to write")
        p.add_argument("--split", choices=SPLITS)
        p.add_argument("--category", choices=CATEGORIES)
        p.add_argument("--ids", nargs="*")
    sub.add_parser("build")
    args = ap.parse_args(argv)
    if args.cmd == "check":
        _, ok = check(args.split, args.category, args.ids)
        return 0 if ok else 1
    if args.cmd == "build":
        return build()
    if args.cmd == "review":
        rubrics, ok = check(args.split, args.category, args.ids, quiet=True)
        Path(args.out).write_text(render(rubrics, load_data()) + "\n")
        print(f"wrote {args.out} ({len(rubrics)} rubrics){'' if ok else ' -- NOTE: check reported errors'}")
        return 0 if ok else 1
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
