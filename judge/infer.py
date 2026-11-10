#!/usr/bin/env python3
"""Run the SFT judge (Qwen3-VL-8B + LoRA) on data/{eval,sft_val}.jsonl and write one JSONL row per clip.

Same template, system prompt and frame sampling as training: the engine reads args.json next to the adapter,
and scripts/infer.sh sets the same FPS / VIDEO_MAX_PIXELS env (16 uniform frames, <= 448x448). Rows are the input rows
minus the assistant turn, so the prompt is byte-identical to what the model saw in training.

Output: <out-root>/<run>/<split>.shard<i>of<n>.jsonl with
  {"tag","id","category","sa_score","pc_assessable","pc_score","reason","raw","parse_ok","gold":{...},
   "sa_soft","pc_soft","sa_probs","pc_probs"}
sa_soft / pc_soft are the probability-weighted scores (sum over 1-5 of score x P(score) at the digit token, renormalised
over the five digits), for Spearman / AUROC without the integer tie problem. Rows are append-only and resumable:
clips already in the shard file are skipped. Summarise with judge/summary.py.

    python judge/infer.py --adapter <ckpt dir> --run sft_lora_r16_full --split eval --shard 0 --shards 4
    python judge/infer.py --adapter <ckpt dir> --run smoke --split val --limit 8          # quick check
    python judge/infer.py --split eval --check-only                                        # inputs only, no model
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DATA = ROOT / "data"
SPLIT_FILE = {"eval": "eval", "val": "sft_val", "train": "sft_train"}
DEFAULT_OUT_ROOT = Path(os.environ.get("PJ_RUNS", ROOT / "runs"))          # <out-root>/<run>/<split>.shard*.jsonl
BASE_MODEL = os.environ.get("PJ_BASE_MODEL", "Qwen/Qwen3-VL-8B-Instruct")  # HF id or local dir
FIELDS = ("sa_score", "pc_assessable", "pc_score", "reason")


def load_rows(split: str, suffix: str = "") -> list[dict]:
    path = DATA / f"{SPLIT_FILE.get(split, split)}{suffix}.jsonl"
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    rows.sort(key=lambda r: (r["tag"], r["id"]))
    return rows


def parse_answer(text: str) -> tuple[dict, bool]:
    """Return (fields, parse_ok). Falls back to regexes so a truncated reason still yields the scores."""
    out = {k: None for k in FIELDS}
    text = text.strip()
    m = re.search(r"\{.*\}", text, re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            if isinstance(obj, dict):
                for k in FIELDS:
                    out[k] = obj.get(k)
        except json.JSONDecodeError:
            pass
    if out["sa_score"] is None:
        m = re.search(r'"sa_score"\s*:\s*(\d)', text)
        out["sa_score"] = int(m.group(1)) if m else None
    if out["pc_score"] is None:
        m = re.search(r'"pc_score"\s*:\s*(\d)', text)
        out["pc_score"] = int(m.group(1)) if m else None
    if out["pc_assessable"] is None:
        m = re.search(r'"pc_assessable"\s*:\s*(true|false)', text)
        out["pc_assessable"] = (m.group(1) == "true") if m else None
    if out["reason"] is None:
        m = re.search(r'"reason"\s*:\s*"(.*)', text, re.S)
        out["reason"] = m.group(1).rstrip('"} \n') if m else None
    for k in ("sa_score", "pc_score"):
        v = out[k]
        out[k] = int(v) if isinstance(v, (int, float)) and 1 <= int(v) <= 5 else None
    if not isinstance(out["pc_assessable"], bool):
        out["pc_assessable"] = None
    ok = all(out[k] is not None for k in FIELDS)
    return out, ok


def soft_scores(raw: str, logprobs: dict | None) -> dict:
    """Expected score from the digit-token distribution at the sa_score / pc_score positions.

    logprobs is ms-swift's {"content": [{"token", "logprob", "top_logprobs": [{"token", "logprob"}, ...]}, ...]}
    for the generated tokens in order. The digit token is located by character offset in the concatenated text."""
    out = {"sa_soft": None, "pc_soft": None, "sa_probs": None, "pc_probs": None}
    if not logprobs or not logprobs.get("content"):
        return out
    toks = logprobs["content"]
    text = "".join(t["token"] for t in toks)
    starts, pos = [], 0
    for t in toks:
        starts.append(pos)
        pos += len(t["token"])
    for key in ("sa_score", "pc_score"):
        m = re.search(rf'"{key}"\s*:\s*(\d)', text)
        if not m:
            continue
        off = m.start(1)
        idx = max(i for i, st in enumerate(starts) if st <= off)
        probs = {}
        for cand in toks[idx].get("top_logprobs") or []:
            tok = cand["token"].strip()
            if tok in ("1", "2", "3", "4", "5"):
                probs[int(tok)] = probs.get(int(tok), 0.0) + math.exp(cand["logprob"])
        if not probs:
            continue
        z = sum(probs.values())
        probs = {k: v / z for k, v in sorted(probs.items())}
        out[key[:2] + "_soft"] = round(sum(k * v for k, v in probs.items()), 4)
        out[key[:2] + "_probs"] = {k: round(v, 4) for k, v in probs.items()}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--adapter", help="LoRA checkpoint dir (contains adapter_model.safetensors and args.json)")
    ap.add_argument("--model", default=BASE_MODEL)
    ap.add_argument("--run", default="judge", help="output sub-directory name")
    ap.add_argument("--split", default="eval", choices=["eval", "val", "train"])
    ap.add_argument("--suffix", default="", help="data variant, e.g. _rf -> <split>_rf.jsonl")
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0, help="only the first N clips of this shard")
    ap.add_argument("--batch-size", type=int, default=8)
    ap.add_argument("--max-tokens", type=int, default=512)
    ap.add_argument("--check-only", action="store_true", help="verify inputs and exit without loading the model")
    args = ap.parse_args()

    rows = load_rows(args.split, args.suffix)
    rows = rows[args.shard::args.shards]
    if args.limit:
        rows = rows[: args.limit]
    missing = [r["videos"][0] for r in rows if not Path(r["videos"][0]).exists()]
    print(f"split={args.split}{args.suffix} shard={args.shard}/{args.shards} clips={len(rows)} missing_videos={len(missing)}", flush=True)
    for p in missing[:5]:
        print("  missing:", p)
    if args.check_only:
        return 1 if missing else 0
    if not args.adapter and args.model == BASE_MODEL:
        print("note: no --adapter given, running the base model", flush=True)

    out_dir = args.out_root / args.run
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.split}.shard{args.shard}of{args.shards}.jsonl"
    done = set()  # union over every shard file of this run: the stride assignment moves when rows are added (e.g. a new generator)
    for p in out_dir.glob(f"{args.split}.shard*of*.jsonl"):
        for line in p.read_text().splitlines():
            if line.strip():
                rr = json.loads(line)
                done.add((rr["tag"], rr["id"]))
    todo = [r for r in rows if (r["tag"], r["id"]) not in done]
    print(f"already done {len(done)}, to run {len(todo)} -> {out_path}", flush=True)
    if not todo:
        return 0

    import torch
    from swift.infer_engine import InferRequest, RequestConfig, TransformersEngine

    t0 = time.time()
    engine = TransformersEngine(
        args.model,
        adapters=[args.adapter] if args.adapter else None,
        max_batch_size=args.batch_size,
        torch_dtype=torch.bfloat16,
        attn_impl="sdpa",
    )
    print(f"engine ready in {time.time() - t0:.0f}s; template={engine.template.template_meta.template_type}", flush=True)
    cfg = RequestConfig(max_tokens=args.max_tokens, temperature=0.0, seed=42, logprobs=True, top_logprobs=10)

    n_ok = 0
    t_start = time.time()
    with out_path.open("a") as fh:
        for i in range(0, len(todo), args.batch_size):
            batch = todo[i : i + args.batch_size]
            reqs = [InferRequest(messages=[m for m in r["messages"] if m["role"] != "assistant"], videos=r["videos"]) for r in batch]
            resps = engine.infer(reqs, cfg, use_tqdm=False)
            for r, resp in zip(batch, resps):
                raw = resp.choices[0].message.content
                fields, ok = parse_answer(raw)
                n_ok += ok
                rec = {"tag": r["tag"], "id": r["id"], "category": r["category"], **fields,
                       "parse_ok": ok, "raw": raw, "gold": r["target"], "split": args.split,
                       **soft_scores(raw, resp.choices[0].logprobs)}
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            n = i + len(batch)
            rate = (time.time() - t_start) / n
            print(f"[{n}/{len(todo)}] {rate:.1f} s/clip, parse_ok {n_ok}/{n}, eta {rate * (len(todo) - n) / 60:.0f} min", flush=True)
    print(f"done {len(todo)} clips in {(time.time() - t_start) / 60:.1f} min, parse_ok {n_ok}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
