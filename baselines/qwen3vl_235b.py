#!/usr/bin/env python3
"""Zero-shot Qwen3-VL-235B-A22B-Instruct-FP8 as a judge, through vLLM (TP=4): the largest open VLM row of the judge table.

Same inputs and outputs as judge/infer.py: rows from data/<split><suffix>.jsonl, NFRAMES uniformly
sampled frames, each resized like
qwen_vl_utils.smart_resize to <= PIX x PIX, greedy decoding with top-10 logprobs for the soft scores, one JSON row
per clip in <out-root>/<run>/<split>.shard<k>of<n>.jsonl (resumable), so judge/summary.py works unchanged.

  python baselines/qwen3vl_235b.py --model Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 --tp 4 \
      --run base235b
  python baselines/qwen3vl_235b.py --dry-run --limit 2        # CPU: prompts + frames only
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402

from judge.infer import DEFAULT_OUT_ROOT, load_rows, parse_answer, soft_scores  # noqa: E402

FACTOR = 32  # Qwen3-VL: patch 16 x spatial merge 2


def smart_resize(h: int, w: int, min_pixels: int, max_pixels: int) -> tuple[int, int]:
    """qwen_vl_utils.smart_resize: keep the aspect ratio, round to multiples of FACTOR, stay inside the pixel bounds."""
    hb = max(FACTOR, round(h / FACTOR) * FACTOR)
    wb = max(FACTOR, round(w / FACTOR) * FACTOR)
    if hb * wb > max_pixels:
        beta = math.sqrt(h * w / max_pixels)
        hb = max(FACTOR, math.floor(h / beta / FACTOR) * FACTOR)
        wb = max(FACTOR, math.floor(w / beta / FACTOR) * FACTOR)
    elif hb * wb < min_pixels:
        beta = math.sqrt(min_pixels / (h * w))
        hb = math.ceil(h * beta / FACTOR) * FACTOR
        wb = math.ceil(w * beta / FACTOR) * FACTOR
    return hb, wb


def load_frames(path: str, nframes: int, pix: int) -> tuple[np.ndarray, dict]:
    from PIL import Image

    import decord

    vr = decord.VideoReader(path)
    total, vfps = len(vr), vr.get_avg_fps()
    n = min(nframes, total)
    if n % 2:
        n -= 1
    idx = [int(round(x)) for x in np.linspace(0, total - 1, n)]
    raw = vr.get_batch(idx).asnumpy()
    h, w = raw.shape[1:3]
    hb, wb = smart_resize(h, w, 128 * 128, pix * pix)
    frames = np.stack([np.asarray(Image.fromarray(f).resize((wb, hb), Image.BICUBIC)) for f in raw])
    md = {"total_num_frames": int(total), "fps": float(vfps), "duration": float(total / vfps) if vfps else None,
          "video_backend": "decord", "frames_indices": [int(i) for i in idx], "do_sample_frames": False}
    return frames, md


def to_messages(row: dict) -> list[dict]:
    msgs = []
    for m in row["messages"]:
        if m["role"] == "assistant":
            continue
        if m["role"] == "user":
            text = m["content"].replace("<video>", "", 1).lstrip("\n")
            msgs.append({"role": "user", "content": [{"type": "video", "video": row["videos"][0]}, {"type": "text", "text": text}]})
        else:
            msgs.append({"role": m["role"], "content": m["content"]})
    return msgs


def logprobs_to_swift(out) -> dict:
    """vLLM per-token top logprobs -> the ms-swift structure judge.infer.soft_scores reads."""
    content = []
    for tid, lp in zip(out.token_ids, out.logprobs or []):
        mine = lp.get(tid)
        tok = mine.decoded_token if mine is not None and mine.decoded_token is not None else ""
        content.append({"token": tok, "logprob": mine.logprob if mine is not None else 0.0,
                        "top_logprobs": [{"token": v.decoded_token or "", "logprob": v.logprob} for v in lp.values()]})
    return {"content": content}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3-VL-235B-A22B-Instruct-FP8", help="HF id or local dir")
    ap.add_argument("--run", default="base235b")
    ap.add_argument("--split", default="eval")
    ap.add_argument("--suffix", default="")
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--shard", type=int, default=0)
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--max-tokens", type=int, default=1024)
    ap.add_argument("--nframes", type=int, default=16)
    ap.add_argument("--pix", type=int, default=448)
    ap.add_argument("--tp", type=int, default=4)
    ap.add_argument("--max-model-len", type=int, default=12288)
    ap.add_argument("--gpu-mem", type=float, default=0.90)
    ap.add_argument("--dry-run", action="store_true", help="build prompts and frames for the first rows, no model")
    args = ap.parse_args()

    rows = load_rows(args.split, args.suffix)[args.shard :: args.shards]
    if args.limit:
        rows = rows[: args.limit]
    missing = [r["videos"][0] for r in rows if not Path(r["videos"][0]).exists()]
    print(f"split={args.split}{args.suffix} shard={args.shard}/{args.shards} clips={len(rows)} missing_videos={len(missing)}", flush=True)
    if missing:
        print("  e.g.", missing[:3])
        return 1

    from transformers import AutoProcessor

    processor = AutoProcessor.from_pretrained(args.model)
    if args.dry_run:
        for r in rows[:2]:
            text = processor.apply_chat_template(to_messages(r), tokenize=False, add_generation_prompt=True)
            frames, md = load_frames(r["videos"][0], args.nframes, args.pix)
            print(r["id"], r["tag"], "frames", frames.shape, md, "\nprompt chars", len(text), "\n", text[:300], "...", text[-200:])
        return 0

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

    from vllm import LLM, SamplingParams

    t0 = time.time()
    llm = LLM(model=args.model, tensor_parallel_size=args.tp, max_model_len=args.max_model_len,
              gpu_memory_utilization=args.gpu_mem, max_num_seqs=args.batch_size,
              limit_mm_per_prompt={"video": 1, "image": 0}, seed=0)
    print(f"vLLM engine up in {time.time() - t0:.0f}s", flush=True)
    sampling = SamplingParams(temperature=0.0, max_tokens=args.max_tokens, seed=0, logprobs=10)

    n_ok = 0
    t_start = time.time()
    with out_path.open("a") as fh:
        for i in range(0, len(todo), args.batch_size):
            batch = todo[i : i + args.batch_size]
            prompts = []
            for r in batch:
                text = processor.apply_chat_template(to_messages(r), tokenize=False, add_generation_prompt=True)
                prompts.append({"prompt": text, "multi_modal_data": {"video": load_frames(r["videos"][0], args.nframes, args.pix)}})
            outs = llm.generate(prompts, sampling, use_tqdm=False)
            for r, o in zip(batch, outs):
                raw = o.outputs[0].text
                fields, ok = parse_answer(raw)
                n_ok += ok
                rec = {"tag": r["tag"], "id": r["id"], "category": r["category"], **fields, "parse_ok": ok, "raw": raw,
                       "gold": r["target"], "split": args.split, **soft_scores(raw, logprobs_to_swift(o.outputs[0]))}
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            n = i + len(batch)
            rate = (time.time() - t_start) / n
            print(f"[{n}/{len(todo)}] {rate:.1f} s/clip, parse_ok {n_ok}/{n}, eta {rate * (len(todo) - n) / 60:.0f} min", flush=True)
    print(f"done {len(todo)} clips in {(time.time() - t_start) / 60:.1f} min, parse_ok {n_ok}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
