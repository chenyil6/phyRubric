#!/usr/bin/env python3
"""Build a local HTML page to review generated videos next to their captions.

    python gen_videos/review_page.py --tag cogvideox5b                 # every video present for that tag
    python gen_videos/review_page.py --tag cogvideox5b --category Mechanics --split train

Reads data/{train,eval}.json and gen_videos/outputs/<tag>/<ID>_s<seed>.mp4, writes
gen_videos/review/<tag>[_<filters>].html with relative video paths. Open it in a browser.
Per-video wall time comes from gen_videos/manifests/<tag>.jsonl when available.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "gen_videos" / "outputs"
REVIEW = ROOT / "gen_videos" / "review"
CATEGORIES = ["Mechanics", "Heat", "Optics", "Electricity", "Acoustics"]

STYLE = """
body{font-family:-apple-system,Helvetica,Arial,sans-serif;margin:0;background:#f6f6f4;color:#222}
header{padding:14px 22px;background:#fff;border-bottom:1px solid #ddd;position:sticky;top:0}
header h1{font-size:17px;margin:0 0 4px}
header .meta{color:#666;font-size:13px}
.row{display:grid;grid-template-columns:400px 1fr;gap:18px;padding:16px 22px;border-bottom:1px solid #e3e3e0;background:#fff;margin:10px 14px;border-radius:6px}
video{width:400px;border-radius:4px;background:#000}
.id{font-weight:600;font-size:15px}
.tags{color:#666;font-size:12px;margin:4px 0 10px}
.cap{font-size:15px;line-height:1.45;margin-bottom:8px}
.exp{font-size:13px;line-height:1.45;color:#444;background:#f3f3ee;padding:8px 10px;border-radius:4px}
.exp b{color:#222}
.media{width:400px;min-height:266px}
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--split", nargs="+", choices=("train", "eval"), default=["train", "eval"])
    ap.add_argument("--category", nargs="+", choices=CATEGORIES)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    records = []
    for split in args.split:
        for r in json.loads((ROOT / "data" / f"{split}.json").read_text()):
            if not args.category or r["category"] in args.category:
                records.append({**r, "split": split})
    records.sort(key=lambda r: (CATEGORIES.index(r["category"]), r["id"]))

    elapsed: dict[str, float] = {}
    manifest = ROOT / "gen_videos" / "manifests" / f"{args.tag}.jsonl"
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            try:
                m = json.loads(line)
                elapsed[m["id"]] = m.get("elapsed_s")
            except json.JSONDecodeError:
                pass

    out_dir = OUT_ROOT / args.tag
    REVIEW.mkdir(exist_ok=True)
    name = "_".join([args.tag] + (args.category or []) + (args.split if len(args.split) == 1 else []))
    page = REVIEW / f"{name}.html"

    rows, present = [], 0
    for r in records:
        fname = f"{r['id']}_s{args.seed}.mp4"
        exists = (out_dir / fname).exists()
        present += exists
        # Rows start hidden unless the file exists at build time; the script below re-checks the
        # served directory listing on every page load, so videos that land later appear on refresh.
        t = elapsed.get(r["id"])
        tags = f"{r['split']} · {r['category']} / {r['subcategory']} · {', '.join(r['violation_types'])}"
        if t:
            tags += f" · {t:.0f}s"
        src = f' src="../outputs/{args.tag}/{fname}"' if exists else ""
        hidden = "" if exists else " hidden"
        rows.append(
            f'<div class="row" data-file="{fname}"{hidden}>'
            f'<div class="media"><video controls loop muted preload="metadata"{src}></video></div>'
            f'<div><div class="id">{r["id"]}</div><div class="tags">{html.escape(tags)}</div>'
            f'<div class="cap">{html.escape(r["caption"])}</div>'
            f'<div class="exp"><b>expectation</b> · {html.escape(r["expectation"])}</div></div></div>'
        )

    script = """
<script>
(async () => {
  const dir = '../outputs/%s/';
  try {
    const txt = await (await fetch(dir, {cache: 'no-store'})).text();       // http.server directory listing
    const have = new Set([...txt.matchAll(/href="([^"]+\\.mp4)"/g)].map(m => decodeURIComponent(m[1])));
    let n = 0;
    for (const row of document.querySelectorAll('.row')) {
      const f = row.dataset.file;
      if (have.has(f)) { const v = row.querySelector('video'); if (!v.src) v.src = dir + f; row.hidden = false; n++; }
      else row.hidden = true;
    }
    document.getElementById('count').textContent = n + ' of ' + document.querySelectorAll('.row').length;
  } catch (e) { /* opened as a plain file: keep the build-time state */ }
})();
</script>""" % args.tag
    doc = (f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(name)}</title>"
           f"<style>{STYLE}</style></head><body><header><h1>{html.escape(name)}</h1>"
           f"<div class='meta'><span id='count'>{present} of {len(rows)}</span> videos · seed {args.seed} · "
           f"reload to pick up newly finished videos · videos loop muted</div></header>"
           + "\n".join(rows) + script + "</body></html>")
    page.write_text(doc)
    print(f"{page.relative_to(ROOT)}: {present} videos, {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
