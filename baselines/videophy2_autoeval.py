#!/usr/bin/env python3
"""Baseline 3: the official VideoPhy-2-AutoEval PC scorer.

This reproduces the official physical-commonsense inference path: 32 video
frames, the released mPLUG-Owl checkpoint, deterministic generation, and a
single 1-5 output.  It intentionally receives no caption or custom rubric.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOT = ROOT.parents[1] / "models" / "videophy_2_auto"
sys.path.insert(0, str(ROOT))

from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.metrics import summarise  # noqa: E402
from eval.runner import COST_FIELDS, join_with_gold, run_batch  # noqa: E402

PROMPT_PHYSICS = (
    "The following is a conversation between a curious human and an AI assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    "Human: <|video|>\n"
    "Human: Does this video adhere to the physical laws? "
    "Rate the video on a scale from 1 to 5, where 5 means full compliance and 1 means "
    "significant violations.\nAI: "
)

EXPECTED_FILES = {
    "pytorch_model-00001-of-00002.bin": 9_995_752_315,
    "pytorch_model-00002-of-00002.bin": 4_309_856_976,
    "pytorch_model.bin.index.json": 92_527,
    "config.json": 7_036,
    "tokenizer.model": 499_723,
}


def checkpoint_status(checkpoint: Path) -> tuple[bool, list[str]]:
    problems = []
    for name, expected_size in EXPECTED_FILES.items():
        path = checkpoint / name
        if not path.is_file():
            problems.append(f"missing {name}")
        elif path.stat().st_size != expected_size:
            problems.append(f"{name}: {path.stat().st_size}/{expected_size} bytes")
    return not problems, problems


def dependency_status(official_code: Path) -> dict[str, bool]:
    return {
        "torch": importlib.util.find_spec("torch") is not None,
        "transformers": importlib.util.find_spec("transformers") is not None,
        "sentencepiece": importlib.util.find_spec("sentencepiece") is not None,
        "decord": importlib.util.find_spec("decord") is not None,
        "official_mplug_owl_video": (official_code / "mplug_owl_video" / "modeling_mplug_owl.py").is_file(),
    }


def parse_score(text: str) -> int:
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    stripped = text.strip().lower()
    if stripped in words:
        return words[stripped]
    if stripped in {"1", "2", "3", "4", "5"}:
        return int(stripped)
    match = re.search(r"(?<!\d)([1-5])(?!\d)", stripped)
    if match:
        return int(match.group(1))
    for word, value in words.items():
        if re.search(rf"\b{word}\b", stripped):
            return value
    raise ValueError(f"no 1-5 score in {text!r}")


class OfficialAutoEval:
    def __init__(self, checkpoint: Path, official_code: Path, device: str, num_frames: int):
        sys.path.insert(0, str(official_code))
        import torch
        from transformers.models.llama.tokenization_llama import LlamaTokenizer
        from mplug_owl_video.modeling_mplug_owl import MplugOwlForConditionalGeneration
        from mplug_owl_video.processing_mplug_owl import MplugOwlImageProcessor, MplugOwlProcessor

        if device.startswith("cuda") and not torch.cuda.is_available():
            raise RuntimeError("CUDA was requested but this PyTorch build has no visible CUDA device")
        self.torch = torch
        self.device = torch.device(device)
        self.dtype = torch.bfloat16 if self.device.type == "cuda" else torch.float32
        self.num_frames = num_frames
        self.tokenizer = LlamaTokenizer.from_pretrained(checkpoint)
        image_processor = MplugOwlImageProcessor.from_pretrained(checkpoint)
        self.processor = MplugOwlProcessor(image_processor, self.tokenizer)
        self.model = MplugOwlForConditionalGeneration.from_pretrained(
            checkpoint, torch_dtype=self.dtype, device_map={"": "cpu"}
        )
        self.model = self.model.to(self.device).to(self.dtype).eval()

    def judge(self, sample) -> dict[str, Any]:
        with self.torch.no_grad():
            inputs = self.processor(
                text=[PROMPT_PHYSICS],
                videos=[str(sample.video_path)],
                num_frames=self.num_frames,
                return_tensors="pt",
            )
            inputs = {
                key: (value.to(self.dtype) if value.dtype.is_floating_point else value).to(self.device)
                for key, value in inputs.items()
            }
            output_ids = self.model.generate(
                **inputs,
                do_sample=False,
                top_k=1,
                temperature=0.001,
                max_length=256,
            )
        raw = self.tokenizer.decode(output_ids.tolist()[0], skip_special_tokens=True)
        score = parse_score(raw)
        return {
            "video_id": sample.video_id,
            "pc_score": score,
            "confidence": 0.5,
            "score_imputed": False,
            "raw_text": raw,
            "frames": self.num_frames,
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "llm_calls": 1,
            "cache_hits": 0,
            "error": "",
        }


def select_dataset(cfg: dict, split: str, n: int, seed: int, hard_only: bool):
    dataset = VideoPhy2Dataset.from_config(cfg, split=split).filter(
        has_video=True, hard=True if hard_only else None
    )
    return dataset.stratified_subset(n, seed=seed) if n else dataset


def write_summary(out_path: Path, dataset, run_stats: dict, seed: int) -> Path:
    frame = join_with_gold(out_path, dataset)
    usable = frame[frame["pred"].notna()].copy()
    report = summarise(
        list(usable["pred"]),
        list(usable["pc"]),
        list(usable["confidence"]),
        usable[list(COST_FIELDS)].to_dict("records"),
        seed=seed,
    )
    report["n_rows_joined"] = int(len(frame))
    report["n_without_score"] = int(len(frame) - len(usable))
    if len(usable):
        delta = (usable["pred"] - usable["pc"]).abs()
        report["exact_accuracy"] = round(float((delta == 0).mean()), 6)
        report["within_one_accuracy"] = round(float((delta <= 1).mean()), 6)
    summary_path = out_path.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps({"baseline": "videophy2_autoeval", "run": run_stats, "metrics": report}, indent=2)
    )
    return summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    parser.add_argument("--checkpoint", type=Path, default=MODEL_ROOT)
    parser.add_argument(
        "--official-code",
        type=Path,
        default=MODEL_ROOT / "official_code",
    )
    parser.add_argument("--split", default="test")
    parser.add_argument("--n", type=int, default=200, help="0 means the full split")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--num-frames", type=int, default=32)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--hard-only", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    dataset = select_dataset(cfg, args.split, args.n, args.seed, args.hard_only)
    complete, problems = checkpoint_status(args.checkpoint)
    deps = dependency_status(args.official_code)
    print(f"selected {len(dataset)} VideoPhy-2 videos; frames={args.num_frames}")
    print(f"checkpoint complete: {complete}")
    for problem in problems:
        print(f"  - {problem}")
    print("dependencies: " + ", ".join(f"{key}={'ok' if value else 'missing'}" for key, value in deps.items()))
    if args.check_only:
        return 0 if complete and all(deps.values()) else 2
    if not complete:
        raise RuntimeError("official checkpoint is incomplete; rerun the download")
    missing_deps = [name for name, present in deps.items() if not present]
    if missing_deps:
        raise RuntimeError("missing AutoEval dependencies: " + ", ".join(missing_deps))

    evaluator = OfficialAutoEval(args.checkpoint, args.official_code, args.device, args.num_frames)
    out_path = args.out or ROOT / "results" / f"baseline_videophy2_autoeval_n{len(dataset)}_s{args.seed}.jsonl"
    stats = run_batch(
        list(dataset),
        evaluator.judge,
        out_path,
        workers=1,
        resume=not args.no_resume,
        limit=args.limit,
    )
    summary = write_summary(out_path, dataset, stats.as_dict(), args.seed)
    print(f"results: {out_path}\nsummary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
