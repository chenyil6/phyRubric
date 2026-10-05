#!/usr/bin/env python3
"""Merge eval blind-label outputs into teacher/review/annotations/eval/<tag>.json (one file per generator).

    python teacher/review/merge_eval.py --work /work/hdd/bilw/hchen56/phyRubric_outputs/_eval_blind

Reads every WORK/outputs/<ID>__<tag>.json, validates it against rubrics/eval.json, computes SA/PC with
teacher/scoring.py, and rebuilds the per-tag files from scratch (idempotent; safe to run on a partial batch).
Clips from teacher/review/annotations/archive/eval_pilot_hunyuan15_sonnet.json are merged into the Hunyuan file.
Prints per-tag counts and any clips whose output could not be used.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from teacher.scoring import score  # noqa: E402

OUT_DIR = ROOT / "teacher/review/annotations/eval"
PILOT = ROOT / "teacher/review/annotations/archive/eval_pilot_hunyuan15_sonnet.json"
STATUSES = {"pass", "fail", "not_shown"}


def build_clip(out: dict, rub: dict, tag: str, video: str, source: str) -> tuple[dict | None, list[str]]:
    problems: list[str] = []
    ids = [x["id"] for x in rub["sa"]] + [x["id"] for x in rub["pc"]]
    got = {it.get("id"): it for it in out.get("items", []) if isinstance(it, dict)}
    items = []
    for sec in ("sa", "pc"):
        for x in rub[sec]:
            it = got.get(x["id"])
            if it is None:
                problems.append(f"missing {x['id']}")
                status = "fail" if sec == "sa" else "not_shown"
                it = {"status": status, "evidence": ""}
            status = str(it.get("status", "")).strip().lower().replace("-", "_")
            if status not in STATUSES:
                problems.append(f"{x['id']} bad status {it.get('status')!r}")
                status = "fail" if sec == "sa" else "not_shown"
            if sec == "sa" and status == "not_shown":
                problems.append(f"{x['id']} SA not_shown -> fail")
                status = "fail"
            rec = {"id": x["id"], "status": status, "evidence": it.get("evidence", "")}
            if sec == "sa":
                rec.update(weight=x["weight"], check=x["check"])
            else:
                rec.update(severity=x["severity"], type=x["type"], expect=x["expect"], fail=x["fail"],
                           matched_fail=it.get("matched_fail") if status == "fail" else None)
                if "precondition" in x:
                    rec["precondition"] = x["precondition"]
                if x["expect"].startswith("Everything in view"):
                    rec["source"] = source
            items.append(rec)
    extra = set(got) - set(ids)
    if extra:
        problems.append(f"unknown items {sorted(extra)}")
    recognisable = out.get("recognisable_attempt", True)
    if isinstance(recognisable, str):
        recognisable = recognisable.strip().lower() not in {"false", "no", "0"}
    sa, pc = score(rub, [{"id": i["id"], "status": i["status"]} for i in items], bool(recognisable))
    clip = {"id": rub["id"], "tag": tag, "category": rub["category"], "video": video, "caption": rub["caption"],
            "sa_score": sa, "pc_score": pc, "recognisable_attempt": bool(recognisable),
            "clip_confidence": out.get("clip_confidence"), "clip_confidence_reason": out.get("clip_confidence_reason"),
            "clip_summary": out.get("clip_summary"), "uncovered": out.get("uncovered") or [], "items": items}
    if problems:
        clip["problems"] = problems
    return clip, problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", type=Path, required=True)
    a = ap.parse_args()
    rub = {r["id"]: r for r in json.loads((ROOT / "rubrics/eval.json").read_text())}
    by_tag: dict[str, list[dict]] = {}
    bad: list[str] = []
    for f in sorted((a.work / "outputs").glob("*.json")):
        try:
            out = json.loads(f.read_text())
        except Exception as e:  # noqa: BLE001
            bad.append(f"{f.name}: unreadable ({e})")
            continue
        key = out.get("key") or f.stem
        if "__" not in key:
            bad.append(f"{f.name}: no key")
            continue
        rid, tag = key.split("__", 1)
        if rid not in rub:
            bad.append(f"{f.name}: unknown id {rid}")
            continue
        inp = a.work / "inputs" / f"{key}.json"
        video = json.loads(inp.read_text())["video"] if inp.exists() else ""
        clip, problems = build_clip(out, rub[rid], tag, video, "blind")
        if problems:
            bad.append(f"{key}: {'; '.join(problems)}")
        by_tag.setdefault(tag, []).append(clip)
    if PILOT.exists():
        for c in json.loads(PILOT.read_text())["clips"]:
            lst = by_tag.setdefault(c["tag"], [])
            if not any(x["id"] == c["id"] for x in lst):
                # pilot records already carry full items; re-score to be safe
                sa, pc = score(rub[c["id"]], [{"id": i["id"], "status": i["status"]} for i in c["items"]], c.get("recognisable_attempt", True))
                c = {**c, "sa_score": sa, "pc_score": pc, "from_pilot": True}
                lst.append(c)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for tag, clips in sorted(by_tag.items()):
        clips.sort(key=lambda c: c["id"])
        dup = [k for k, v in Counter(c["id"] for c in clips).items() if v > 1]
        if dup:
            bad.append(f"{tag}: duplicate ids {dup[:5]}")
        hdr = {"purpose": "Benchmark reference labels: blind labels for the eval split, by Claude Sonnet 5.5 subagents (5 clips each, generators mixed per task). Each saw only caption, rubric (7 PC items incl. the universal fatal item) and video frames. sa_score / pc_score computed with teacher/scoring.py.",
               "protocol": "teacher/review/labelling/INSTRUCTIONS.md", "annotator": "Claude Sonnet 5.5 subagents", "date": str(date.today()),
               "split": "eval", "tag": tag, "n_clips": len(clips), "clips": clips}
        (OUT_DIR / f"{tag}.json").write_text(json.dumps(hdr, ensure_ascii=False, indent=1) + "\n")
        print(f"{tag:30s} {len(clips):4d} clips -> {OUT_DIR / (tag + '.json')}")
    print(f"total {sum(len(v) for v in by_tag.values())} clips; {len(bad)} with problems")
    for b in bad[:20]:
        print("  !", b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
