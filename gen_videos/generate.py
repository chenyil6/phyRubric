#!/usr/bin/env python3
"""Render the caption dataset (data/train.json, data/eval.json) with a text-to-video model.

    # preflight on a compute node: packages, GPU, weights, selection -- no generation
    python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --check-only --per-category 10

    # pilot: 10 captions per category (round-robin over subcategories), split into 5 shards
    python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --per-category 10 --shard 0/5

    # full train split, shard 7 of 40
    python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --split train --shard 7/40

The generation prompt is the caption verbatim: no upsampling, no style suffix. Output is
<out-root>/<tag>/<ID>_s<seed>.mp4 and one append-only manifest line per video in
gen_videos/manifests/<tag>.jsonl. Existing outputs are skipped, so a killed job is
simply resubmitted. `--tag` defaults to the backend name; use it to keep separate
settings apart (e.g. cogvideox5b_steps50).
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import os
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_OUT_ROOT = ROOT / "gen_videos" / "outputs"
MANIFESTS = ROOT / "gen_videos" / "manifests"
CATEGORIES = ["Mechanics", "Heat", "Optics", "Electricity", "Acoustics"]


# --------------------------------------------------------------------------- selection

def load_records(splits: list[str]) -> list[dict[str, Any]]:
    records = []
    for split in splits:
        path = DATA / f"{split}.json"
        if not path.exists():
            raise FileNotFoundError(f"{path} missing; run `python data/build.py build` first")
        for r in json.loads(path.read_text()):
            records.append({**r, "split": split})
    return records


def per_category(records: list[dict[str, Any]], n: int) -> list[dict[str, Any]]:
    """n records per category, round-robin over subcategories in id order. Deterministic."""
    out = []
    for cat in CATEGORIES:
        by_sub: dict[str, list[dict[str, Any]]] = {}
        for r in records:
            if r["category"] == cat:
                by_sub.setdefault(r["subcategory"], []).append(r)
        for q in by_sub.values():
            q.sort(key=lambda r: r["id"])
        picked: list[dict[str, Any]] = []
        while len(picked) < n and any(by_sub.values()):
            for sub in sorted(by_sub):
                if by_sub[sub] and len(picked) < n:
                    picked.append(by_sub[sub].pop(0))
        out.extend(picked)
    return out


def select(args: argparse.Namespace) -> list[dict[str, Any]]:
    records = load_records(args.split)
    if args.category:
        records = [r for r in records if r["category"] in args.category]
    if args.ids:
        wanted = set(args.ids)
        records = [r for r in records if r["id"] in wanted]
        missing = wanted - {r["id"] for r in records}
        if missing:
            raise SystemExit(f"unknown ids: {sorted(missing)}")
    if args.per_category:
        records = per_category(records, args.per_category)
    records.sort(key=lambda r: (CATEGORIES.index(r["category"]), r["id"]))
    if args.limit:
        records = records[: args.limit]
    if args.shard:
        k, n = args.shard
        records = records[k::n]
    return records


# --------------------------------------------------------------------------- backends
# A backend is a function (model_path, args) -> generate(prompt, seed) -> (frames, fps).
# Add a model by writing one loader; nothing else in this file needs to change.

def load_cogvideox(model: Path, args: argparse.Namespace) -> Callable[[str, int], tuple[list, int]]:
    import torch
    from diffusers import CogVideoXDPMScheduler, CogVideoXPipeline

    if args.num_frames % 4 != 1:
        raise SystemExit("CogVideoX needs --num-frames = 4k+1 (49 for CogVideoX-5b, 81 for 1.5-5B)")
    pipe = CogVideoXPipeline.from_pretrained(model, torch_dtype=torch.bfloat16)
    pipe.scheduler = CogVideoXDPMScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
    pipe.vae.enable_slicing()
    pipe.vae.enable_tiling()
    # CogVideoX1.5-5B at 1360x768x81 does not fit next to the T5 encoder on a 40 GB card:
    # keep only the active component on the GPU there (official recipe uses CPU offload too).
    offload = args.cpu_offload or (args.backend == "cogvideox15" and torch.cuda.get_device_properties(0).total_memory < 70e9)
    if offload:
        pipe.enable_model_cpu_offload()
    else:
        pipe.to("cuda")
    print(f"cogvideox: {args.width}x{args.height}x{args.num_frames} steps={args.steps} cfg={args.guidance_scale} "
          f"cpu_offload={offload}", flush=True)

    def generate(prompt: str, seed: int) -> tuple[list, int]:
        frames = pipe(
            prompt=prompt,
            num_videos_per_prompt=1,
            height=args.height,
            width=args.width,
            num_inference_steps=args.steps,
            num_frames=args.num_frames,
            use_dynamic_cfg=True,
            guidance_scale=args.guidance_scale,
            generator=torch.Generator(device="cuda").manual_seed(seed),
        ).frames[0]
        return frames, args.fps

    return generate


# Wan2.1's recommended negative prompt (from the Wan-AI model card). The positive prompt stays the caption verbatim.
WAN_NEGATIVE = ("Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, "
                "overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, "
                "poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, "
                "messy background, three legs, many people in the background, walking backwards")


def load_wan(model: Path, args: argparse.Namespace) -> Callable[[str, int], tuple[list, int]]:
    """Wan2.1 / Wan2.2 T2V (Diffusers layout).

    Wan2.1-14B: one 28 GB bf16 transformer + 11 GB text encoder. Wan2.2-A14B: two 14B experts
    (transformer for high noise, transformer_2 for low noise, switched at boundary_ratio) and a
    second guidance scale. Both exceed a 40 GB card, so components are offloaded to CPU in turn
    there; on 80 GB+ the pipeline stays on GPU. Untested until the first GPU job runs it."""
    import torch
    from diffusers import AutoencoderKLWan, WanPipeline
    from diffusers.schedulers.scheduling_unipc_multistep import UniPCMultistepScheduler

    if (args.num_frames - 1) % 4 != 0:
        raise SystemExit("Wan needs --num-frames = 4k+1 (81 recommended)")
    vae = AutoencoderKLWan.from_pretrained(model, subfolder="vae", torch_dtype=torch.float32)
    pipe = WanPipeline.from_pretrained(model, vae=vae, torch_dtype=torch.bfloat16)
    moe = getattr(pipe, "transformer_2", None) is not None
    if args.flow_shift is None:
        # Wan2.1: 5.0 for 720p, 3.0 for 480p. Wan2.2-A14B: 12.0 (official t2v_A14B config).
        args.flow_shift = 12.0 if moe else (5.0 if args.height >= 720 else 3.0)
    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config, flow_shift=args.flow_shift)
    offload = args.cpu_offload or torch.cuda.get_device_properties(0).total_memory < 70e9
    if offload:
        pipe.enable_model_cpu_offload()
    else:
        pipe.to("cuda")
    print(f"wan: moe={moe} {args.width}x{args.height} flow_shift={args.flow_shift} "
          f"cfg={args.guidance_scale}/{args.guidance_scale_2} cpu_offload={offload}", flush=True)

    def generate(prompt: str, seed: int) -> tuple[list, int]:
        kwargs = {}
        if moe and args.guidance_scale_2 is not None:
            kwargs["guidance_scale_2"] = args.guidance_scale_2
        frames = pipe(
            prompt=prompt,
            negative_prompt=WAN_NEGATIVE,
            height=args.height,
            width=args.width,
            num_frames=args.num_frames,
            num_inference_steps=args.steps,
            guidance_scale=args.guidance_scale,
            generator=torch.Generator(device="cuda").manual_seed(seed),
            **kwargs,
        ).frames[0]
        return frames, args.fps

    return generate


def load_hunyuan15(model: Path, args: argparse.Namespace) -> Callable[[str, int], tuple[list, int]]:
    """HunyuanVideo-1.5 T2V (Diffusers layout: hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-{480p,720p}_t2v).

    8.3B DiT + Qwen2.5-VL-7B text encoder + byT5 + 1.3B VAE, ~34 GB in bf16, so a 40 GB card runs
    with model CPU offload (one component on the GPU at a time; cheap here because each component
    is used once per video). Needs diffusers>=0.36, which conflicts with the t2v env's pinned
    transformers -- run this backend from the separate t2v-hy15 env. CFG lives in the pipeline's
    guider component, not in __call__, so --guidance-scale swaps the guider. The pipeline wraps the
    caption in a fixed Qwen chat template before encoding; the caption text itself is untouched."""
    import torch
    from diffusers import HunyuanVideo15Pipeline
    from diffusers.guiders import ClassifierFreeGuidance

    if (args.num_frames - 1) % 4 != 0:
        raise SystemExit("HunyuanVideo-1.5 needs --num-frames = 4k+1 (121 recommended)")
    pipe = HunyuanVideo15Pipeline.from_pretrained(model, torch_dtype=torch.bfloat16)
    if abs(pipe.guider.guidance_scale - args.guidance_scale) > 1e-6:
        pipe.guider = ClassifierFreeGuidance(guidance_scale=args.guidance_scale)
    pipe.vae.enable_tiling()
    offload = args.cpu_offload or torch.cuda.get_device_properties(0).total_memory < 70e9
    if offload:
        pipe.enable_model_cpu_offload()
    else:
        pipe.to("cuda")
    print(f"hunyuan15: {args.width}x{args.height}x{args.num_frames} steps={args.steps} "
          f"cfg={pipe.guider.guidance_scale} shift={pipe.scheduler.config.shift} cpu_offload={offload}", flush=True)

    def generate(prompt: str, seed: int) -> tuple[list, int]:
        frames = pipe(
            prompt=prompt,
            height=args.height,
            width=args.width,
            num_frames=args.num_frames,
            num_inference_steps=args.steps,
            generator=torch.Generator(device="cuda").manual_seed(seed),
        ).frames[0]
        return frames, args.fps

    return generate


BACKENDS: dict[str, dict[str, Any]] = {
    # defaults are the model authors' recommended sampling settings
    "cogvideox15": {"load": load_cogvideox, "steps": 50, "guidance_scale": 6.0, "num_frames": 81, "fps": 16,
                    "height": 768, "width": 1360,                                  # CogVideoX1.5-5B
                    "packages": ("torch", "diffusers", "transformers", "accelerate", "sentencepiece")},
    "wan22":       {"load": load_wan, "steps": 40, "guidance_scale": 4.0, "guidance_scale_2": 3.0,
                    "num_frames": 81, "fps": 16, "height": 480, "width": 832,      # Wan2.2-T2V-A14B, 480p
                    "packages": ("torch", "diffusers", "transformers", "accelerate", "ftfy")},
    "hunyuan15":   {"load": load_hunyuan15, "steps": 50, "guidance_scale": 6.0, "num_frames": 121, "fps": 24,
                    "height": 720, "width": 1280,                                  # HunyuanVideo-1.5 720p_t2v
                    "packages": ("torch", "diffusers", "transformers", "accelerate")},
}


# --------------------------------------------------------------------------- helpers

def package_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "missing"


def gpu_summary() -> str:
    try:
        q = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                           capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return "unavailable"
    return q.stdout.strip().replace("\n", "; ") if q.returncode == 0 else "unavailable"


def target_path(out_dir: Path, rec: dict[str, Any], seed: int) -> Path:
    return out_dir / f"{rec['id']}_s{seed}.mp4"


def append_manifest(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


# --------------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backend", required=True, choices=sorted(BACKENDS))
    ap.add_argument("--model", type=Path, required=True, help="local weights directory")
    ap.add_argument("--tag", help="output/manifest name; default = backend")
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--manifest-dir", type=Path, default=MANIFESTS,
                    help="where <tag>.jsonl is appended (default: this repo's gen_videos/manifests)")
    sel = ap.add_argument_group("selection")
    sel.add_argument("--split", nargs="+", choices=("train", "eval"), default=["train", "eval"])
    sel.add_argument("--category", nargs="+", choices=CATEGORIES)
    sel.add_argument("--ids", nargs="+", help="explicit record ids, e.g. MECH-0001")
    sel.add_argument("--per-category", type=int, help="pilot: n per category, round-robin over subcategories")
    sel.add_argument("--limit", type=int, help="keep only the first N selected records (id order), before sharding")
    sel.add_argument("--shard", type=lambda s: tuple(int(x) for x in s.split("/")), metavar="K/N",
                     help="take every N-th record starting at K (0-based); use with a Slurm array")
    gen = ap.add_argument_group("sampling (defaults per backend)")
    gen.add_argument("--seed", type=int, default=42)
    gen.add_argument("--steps", type=int)
    gen.add_argument("--guidance-scale", type=float)
    gen.add_argument("--num-frames", type=int)
    gen.add_argument("--fps", type=int)
    gen.add_argument("--height", type=int)
    gen.add_argument("--width", type=int)
    gen.add_argument("--guidance-scale-2", type=float, help="wan22 only: low-noise expert guidance")
    gen.add_argument("--flow-shift", type=float, help="wan/wan22 only: scheduler shift (default per model/resolution)")
    gen.add_argument("--cpu-offload", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--check-only", action="store_true", help="preflight only, no model load")
    args = ap.parse_args()

    spec = BACKENDS[args.backend]
    for key in ("steps", "guidance_scale", "num_frames", "fps", "height", "width", "guidance_scale_2"):
        if getattr(args, key) is None:
            setattr(args, key, spec.get(key))
    if args.shard and not (0 <= args.shard[0] < args.shard[1]):
        ap.error("--shard K/N needs 0 <= K < N")
    tag = args.tag or args.backend
    out_dir = args.out_root / tag
    manifest = args.manifest_dir / f"{tag}.jsonl"

    records = select(args)
    todo = [r for r in records if args.overwrite or not target_path(out_dir, r, args.seed).exists()]

    print(f"host={socket.gethostname()}  backend={args.backend}  tag={tag}")
    print(f"model={args.model} ({'present' if args.model.is_dir() else 'MISSING'})")
    print(f"sampling: steps={args.steps} cfg={args.guidance_scale} frames={args.num_frames} fps={args.fps} "
          f"{args.width}x{args.height} seed={args.seed}")
    print(f"selected {len(records)} records, {len(todo)} to generate -> {out_dir}")
    counts: dict[str, int] = {}
    for r in records:
        counts[r["category"]] = counts.get(r["category"], 0) + 1
    print("per category: " + ", ".join(f"{c} {n}" for c, n in counts.items()))

    if args.check_only:
        versions = {p: package_version(p) for p in spec["packages"]}
        print("packages: " + ", ".join(f"{k}={v}" for k, v in versions.items()))
        print(f"GPU: {gpu_summary()}")
        for r in records[:5]:
            print(f"  {r['id']:10s} {r['caption']}")
        ok = args.model.is_dir() and all(v != "missing" for v in versions.values()) and gpu_summary() != "unavailable"
        return 0 if ok else 2

    if not todo:
        print("nothing to do")
        return 0
    if not args.model.is_dir():
        raise SystemExit(f"model directory not found: {args.model}")

    import torch  # noqa: E402  (import late so --check-only works without CUDA)
    from diffusers.utils import export_to_video  # noqa: E402

    if not torch.cuda.is_available():
        raise SystemExit("no CUDA device visible")
    print(f"GPU: {torch.cuda.get_device_name(0)}; loading weights...", flush=True)
    t0 = time.time()
    generate = spec["load"](args.model, args)
    print(f"weights loaded in {time.time() - t0:.0f}s", flush=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    for i, rec in enumerate(todo, 1):
        target = target_path(out_dir, rec, args.seed)
        print(f"[{i}/{len(todo)}] {rec['id']}: {rec['caption']}", flush=True)
        t1 = time.time()
        frames, fps = generate(rec["caption"], args.seed)
        tmp = target.with_suffix(".partial.mp4")
        export_to_video(frames, str(tmp), fps=fps)
        tmp.replace(target)  # a killed job never leaves a truncated .mp4 behind
        elapsed = round(time.time() - t1, 1)
        append_manifest(manifest, {
            "id": rec["id"], "split": rec["split"], "category": rec["category"],
            "subcategory": rec["subcategory"], "caption": rec["caption"],
            "backend": args.backend, "tag": tag, "model_path": str(args.model),
            "seed": args.seed, "num_inference_steps": args.steps, "guidance_scale": args.guidance_scale,
            "num_frames": args.num_frames, "fps": fps, "height": args.height, "width": args.width,
            "guidance_scale_2": args.guidance_scale_2, "flow_shift": args.flow_shift,
            "output_path": str(target), "elapsed_s": elapsed, "host": socket.gethostname(),
            "created_at": datetime.now(timezone.utc).isoformat(),
        })
        print(f"    saved {target.name} in {elapsed}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
