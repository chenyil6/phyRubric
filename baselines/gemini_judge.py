"""Gemini-as-judge on Vertex AI (CloudBank Google Cloud project), same task framing as the trained judge:
caption + video -> {sa_score, pc_assessable, pc_score, reason}. System prompt = data/system_prompt.txt
(the wording the main judge was trained on), so the row is comparable to the zero-shot rows of the local judges.

The video is sent inline (eval clips are 1-3 MB) with a frame rate chosen so the model sees ~16 frames of a 5 s
clip (--fps 3), matching NFRAMES=16 of the local judges. Cost: ~258 tokens per frame (Gemini video tokenisation).

Usage (needs GCP_PROJECT and GOOGLE_APPLICATION_CREDENTIALS or gcloud ADC):
  A  python baselines/gemini_judge.py --model gemini-4-argon --thinking-level LOW                     # greedy, main row
  B  python baselines/gemini_judge.py --model gemini-4-argon --thinking-level LOW --probs             # verbalised soft
  C  python baselines/gemini_judge.py --model gemini-4-argon --thinking-level LOW --samples 5 --temperature 1 --stride 11
     (5-sample Monte-Carlo soft score on a ~200-clip subset, to validate B)
Output: runs/gemini/<model>[_<thinking>]_<split>.jsonl, one line per clip, with usage tokens for the bill.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM_PROMPT = (ROOT / "data" / "system_prompt.txt").read_text().strip()


def load_split(split: str) -> list[dict]:
    """Gold clips of a split: annotations/<split>/<tag>.json, sorted by (tag, id); video paths are repo-relative."""
    clips = []
    for path in sorted((ROOT / "annotations" / split).glob("*.json")):
        clips += json.loads(path.read_text())["clips"]
    clips.sort(key=lambda c: (c["tag"], c["id"]))
    return clips


def video_path(clip: dict, split: str) -> Path:
    return ROOT / clip["video"]

# Variant B (2026-11-04, user): Gemini 4 Argon returns no logprobs, so the soft score is asked for verbally: the
# model adds a probability distribution over 1-5 for each score and we take its expectation. This is the model's
# *stated* uncertainty, not its token distribution; variant C (--samples N, temperature 1) estimates the latter by
# Monte Carlo and is used to validate B on a subset.
SYSTEM_PROMPT_PROBS = SYSTEM_PROMPT.replace(
    'Answer with one JSON object: {"sa_score": int, "pc_assessable": bool, "pc_score": int, "reason": str}. The reason states',
    'Answer with one JSON object: {"sa_score": int, "sa_probs": {"1": float, "2": float, "3": float, "4": float, "5": float}, '
    '"pc_assessable": bool, "pc_score": int, "pc_probs": {"1": float, "2": float, "3": float, "4": float, "5": float}, '
    '"reason": str}. sa_probs and pc_probs give your probability that the true score is each value (they sum to 1); '
    'sa_score and pc_score are the most likely values. The reason states')
assert SYSTEM_PROMPT_PROBS != SYSTEM_PROMPT

PROJECT = os.environ.get("GCP_PROJECT") or sys.exit("set GCP_PROJECT to your Google Cloud project id")
LOCATION = os.environ.get("GCP_LOCATION", "global")   # 2026-11-04: Gemini 3.1/3.8/4 are served only from `global`
FIELDS = ("sa_score", "pc_assessable", "pc_score", "reason")
PROB_FIELDS = ("sa_probs", "pc_probs")


def expectation(probs) -> float | None:
    """E[score] from a {"1": p1, ..., "5": p5} dict (renormalised; None if unusable)."""
    try:
        w = {int(k): max(float(v), 0.0) for k, v in dict(probs).items() if int(k) in (1, 2, 3, 4, 5)}
    except (TypeError, ValueError, AttributeError):
        return None
    z = sum(w.values())
    if z <= 0:
        return None
    return round(sum(k * v for k, v in w.items()) / z, 4)


def parse_answer(text: str) -> dict:
    """JSON object from the reply; regex fallback for the three scores (same as judge.infer.parse_answer)."""
    out: dict = {"raw": text, "parse_ok": False}
    m = re.search(r"\{.*\}", text, re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            for k in FIELDS + PROB_FIELDS:
                if k in obj:
                    out[k] = obj[k]
            out["parse_ok"] = all(k in obj for k in FIELDS)
            for k, soft in (("sa_probs", "sa_soft"), ("pc_probs", "pc_soft")):
                if k in obj:
                    out[soft] = expectation(obj[k])
        except json.JSONDecodeError:
            pass
    for k in ("sa_score", "pc_score"):
        if k not in out:
            mm = re.search(rf'"{k}"\s*:\s*([1-5])', text)
            if mm:
                out[k] = int(mm.group(1))
    if "pc_assessable" not in out:
        mm = re.search(r'"pc_assessable"\s*:\s*(true|false)', text, re.I)
        if mm:
            out["pc_assessable"] = mm.group(1).lower() == "true"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="Vertex model id, e.g. gemini-3.1-pro, gemini-2.5-flash")
    ap.add_argument("--split", default="eval")
    ap.add_argument("--limit", type=int, default=0, help="first N clips only (smoke test)")
    ap.add_argument("--tags", default="", help="comma-separated generator tags to keep")
    ap.add_argument("--fps", type=float, default=3.0, help="frame rate the model samples the clip at")
    ap.add_argument("--think", action="store_true", help="leave thinking on (default: thinking_budget=0)")
    ap.add_argument("--thinking-budget", type=int, default=-1, help="with --think: token budget, -1 = dynamic")
    ap.add_argument("--thinking-level", default="", choices=["", "LOW", "MEDIUM", "HIGH"],
                    help="for models that take a level instead of a budget (Gemini 4 Argon: LOW is the minimum)")
    ap.add_argument("--probs", action="store_true", help="variant B: ask for 1-5 probability fields (verbalised soft score)")
    ap.add_argument("--samples", type=int, default=1, help="variant C: N samples per clip (use with --temperature 1)")
    ap.add_argument("--stride", type=int, default=1, help="keep every k-th clip (subset runs)")
    ap.add_argument("--workers", type=int, default=4, help="parallel requests")
    ap.add_argument("--logprobs", action="store_true", help="ask for response logprobs (2026-11-04: rejected by gemini-4-argon)")
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    from google import genai
    from google.genai import types

    client = genai.Client(vertexai=True, project=PROJECT, location=LOCATION)

    clips = load_split(args.split)
    if args.tags:
        keep = set(args.tags.split(","))
        clips = [c for c in clips if c["tag"] in keep]
    if args.stride > 1:
        clips = clips[:: args.stride]
    if args.limit:
        clips = clips[: args.limit]

    suffix = f"_{args.thinking_level.lower()}" if args.thinking_level else ("_think" if args.think else "")
    if args.probs:
        suffix += "_probs"
    if args.samples > 1:
        suffix += f"_s{args.samples}_t{args.temperature:g}"
    if args.stride > 1:
        suffix += f"_stride{args.stride}"
    out_path = Path(args.out) if args.out else ROOT / "runs/gemini" / f"{args.model}{suffix}_{args.split}.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                done.add((r["tag"], r["id"]))
    todo = [c for c in clips if (c["tag"], c["id"]) not in done]
    print(f"model={args.model} location={LOCATION} clips={len(clips)} done={len(done)} todo={len(todo)} -> {out_path}")

    thinking = None
    if args.thinking_level:
        thinking = types.ThinkingConfig(include_thoughts=False, thinking_level=args.thinking_level)
    elif args.think:
        thinking = types.ThinkingConfig(include_thoughts=False, thinking_budget=args.thinking_budget) \
            if args.thinking_budget >= 0 else types.ThinkingConfig(include_thoughts=False)
    else:
        thinking = types.ThinkingConfig(thinking_budget=0)
    cfg_kwargs = dict(system_instruction=SYSTEM_PROMPT_PROBS if args.probs else SYSTEM_PROMPT, temperature=args.temperature,
                      max_output_tokens=2048, thinking_config=thinking)
    if args.logprobs:
        cfg_kwargs.update(response_logprobs=True, logprobs=5)
    config = types.GenerateContentConfig(**cfg_kwargs)

    totals = {"prompt": 0, "output": 0, "thoughts": 0}

    def one_call(contents):
        for attempt in range(6):
            try:
                return client.models.generate_content(model=args.model, contents=contents, config=config)
            except Exception as e:  # quota / transient
                if str(e)[:3] in ("400", "404"):   # bad model/region/argument: retrying cannot help
                    raise SystemExit(f"request rejected: {str(e)[:300]}")
                wait = 15 * (attempt + 1)
                print(f"  {type(e).__name__}: {str(e)[:160]} -> retry in {wait}s", flush=True)
                time.sleep(wait)
        return None

    def judge(clip) -> dict | None:
        path = video_path(clip, args.split)
        video = types.Part.from_bytes(data=Path(path).read_bytes(), mime_type="video/mp4")
        video.video_metadata = types.VideoMetadata(fps=args.fps)
        contents = [types.Content(role="user", parts=[video, types.Part.from_text(text=f"Caption: {clip['caption']}")])]
        t0 = time.time()
        rec = {"id": clip["id"], "tag": clip["tag"], "category": clip["category"], "model": args.model,
               "think": args.think, "thinking_level": args.thinking_level or None, "probs": args.probs,
               "fps": args.fps, "temperature": args.temperature,
               "gold": {"sa_score": clip["sa_score"], "pc_score": clip["pc_score"]}}
        usage = {"prompt": 0, "output": 0, "thoughts": 0}
        preds = []
        for _ in range(args.samples):
            resp = one_call(contents)
            if resp is None:
                return None
            pred = parse_answer(resp.text or "")
            um = resp.usage_metadata
            if um:
                usage["prompt"] += um.prompt_token_count or 0
                usage["output"] += um.candidates_token_count or 0
                usage["thoughts"] += getattr(um, "thoughts_token_count", 0) or 0
            if args.logprobs:
                cand = resp.candidates[0]
                pred["has_logprobs"] = cand.logprobs_result is not None
            preds.append(pred)
        if args.samples == 1:
            rec["pred"] = preds[0]
        else:
            rec["samples"] = preds
            agg = {}
            for k in ("sa_score", "pc_score"):
                vals = [p[k] for p in preds if isinstance(p.get(k), int)]
                agg[k.replace("_score", "_soft")] = round(sum(vals) / len(vals), 4) if vals else None
                agg[k + "_n"] = len(vals)
            pa = [p["pc_assessable"] for p in preds if isinstance(p.get("pc_assessable"), bool)]
            agg["pc_assessable_rate"] = round(sum(pa) / len(pa), 4) if pa else None
            rec["pred"] = agg
        rec["usage"] = usage
        rec["latency_s"] = round(time.time() - t0, 1)
        return rec

    from concurrent.futures import ThreadPoolExecutor, as_completed
    with out_path.open("a") as fh, ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(judge, c): c for c in todo}
        for i, fut in enumerate(as_completed(futures), 1):
            clip = futures[fut]
            try:
                rec = fut.result()
            except SystemExit as e:
                print(e, flush=True)
                pool.shutdown(wait=False, cancel_futures=True)
                return 1
            if rec is None:
                print(f"  giving up on {clip['tag']}/{clip['id']}", flush=True)
                continue
            for k in totals:
                totals[k] += rec["usage"][k]
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            p = rec["pred"]
            print(f"[{i}/{len(todo)}] {clip['tag']}/{clip['id']} gold SA {clip['sa_score']} PC {clip['pc_score']} | "
                  f"pred SA {p.get('sa_score', p.get('sa_soft'))} PC {p.get('pc_score', p.get('pc_soft'))} "
                  f"soft {p.get('sa_soft')}/{p.get('pc_soft')} | tok {rec['usage']} | {rec['latency_s']}s", flush=True)
    print("token totals this run:", totals)
    return 0


if __name__ == "__main__":
    sys.exit(main())
