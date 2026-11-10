#!/usr/bin/env python3
"""Run the official VideoScore-v1.1 and VideoScore2 raters (TIGER-Lab) on our benchmark clips.

videoscore1 : TIGER-Lab/VideoScore-v1.1, Mantis-8B-Idefics2 regression head. Reproduces
              examples/run_videoscore.py of github.com/TIGER-AI-Lab/VideoScore: up to 48 uniformly
              spaced frames (PyAV), the REGRESSION_QUERY_PROMPT with the caption, bf16, five float
              scores 1.0-4.0 read straight from the logits:
              visual_quality, temporal_consistency, dynamic_degree, t2v_alignment, factual_consistency.
videoscore2 : TIGER-Lab/VideoScore2, Qwen2.5-VL-7B fine-tune. Reproduces vs2_inference.py of
              github.com/TIGER-AI-Lab/VideoScore2: video at 2 fps through qwen_vl_utils, the
              three-dimension prompt with the caption, sampling (temperature 0.7, max 1024 new
              tokens) seeded per clip, integer 1-5 hard scores parsed from the text plus the
              authors' "normed" soft scores from the token probabilities:
              v_score, t_score, p_score (+ *_soft, raw text).

Clip selection, sharding and resumable per-tag JSONL output are shared with videophy_official.py.
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
sys.path.insert(0, str(ROOT / "baselines"))
from videophy_official import DEFAULT_OUT_ROOT, EVAL_TAGS, done_ids, load_clips  # noqa: E402

DEFAULT_CKPT_ROOT = Path(os.environ.get("PJ_MODELS", ROOT / "models"))   # <root>/VideoScore-v1.1, <root>/VideoScore2
CHECKPOINTS = {"videoscore1": "VideoScore-v1.1", "videoscore2": "VideoScore2"}

# --- prompts, verbatim from the official repos ------------------------------------------
# VideoScore/examples/run_videoscore.py
VS1_PROMPT = """
Suppose you are an expert in judging and evaluating the quality of AI-generated videos,
please watch the following frames of a given video and see the text prompt for generating the video,
then give scores from 5 different dimensions:
(1) visual quality: the quality of the video in terms of clearness, resolution, brightness, and color
(2) temporal consistency, both the consistency of objects or humans and the smoothness of motion or movements
(3) dynamic degree, the degree of dynamic changes
(4) text-to-video alignment, the alignment between the text prompt and the video content
(5) factual consistency, the consistency of the video content with the common-sense and factual knowledge

for each dimension, output a float number from 1.0 to 4.0,
the higher the number is, the better the video performs in that sub-score, 
the lowest 1.0 means Bad, the highest 4.0 means Perfect/Real (the video is like a real video)
Here is an output example:
visual quality: 3.2
temporal consistency: 2.7
dynamic degree: 4.0
text-to-video alignment: 2.3
factual consistency: 1.8

For this video, the text prompt is "{text_prompt}",
all the frames of video are as follows:
"""
VS1_MAX_FRAMES = 48
VS1_FIELDS = ["visual_quality", "temporal_consistency", "dynamic_degree", "t2v_alignment", "factual_consistency"]

# VideoScore2/vs2_inference.py (string.Template; the indentation is part of the official prompt)
VS2_PROMPT = """
    You are an expert for evaluating AI-generated videos from three dimensions:
    (1) visual quality – clarity, smoothness, artifacts;
    (2) text-to-video alignment – fidelity to the prompt;
    (3) physical/common-sense consistency – naturalness and physics plausibility.

    Video prompt: $t2v_prompt

    Please output in this format:
    visual quality: <v_score>; 
    text-to-video alignment: <t_score>, 
    physical/common-sense consistency: <p_score>
    """
VS2_FPS = 2.0
VS2_MAX_NEW_TOKENS = 1024
VS2_TEMPERATURE = 0.7
VS2_PATTERN = r"visual quality:\s*(\d+).*?text-to-video alignment:\s*(\d+).*?physical/common-sense consistency:\s*(\d+)"
VS2_PATTERN_LOOSE = (r"visual quality[^\n\d]*?:\s*(\d+).*?text-to-video alignment[^\n\d]*?:\s*(\d+)"
                     r".*?physical/common-sense consistency[^\n\d]*?:\s*(\d+)")


class VideoScore1:
    def __init__(self, checkpoint: Path, device: str):
        import av  # noqa: F401
        import torch
        from transformers import AutoProcessor
        from mantis.models.idefics2 import Idefics2ForSequenceClassification

        self.torch = torch
        self.processor = AutoProcessor.from_pretrained(str(checkpoint), torch_dtype=torch.bfloat16)
        self.model = Idefics2ForSequenceClassification.from_pretrained(str(checkpoint), torch_dtype=torch.bfloat16).eval()
        self.model.to(torch.device(device))

    @staticmethod
    def read_frames(video_path: str):
        import av
        import numpy as np
        from PIL import Image

        container = av.open(video_path)
        total_frames = container.streams.video[0].frames
        if total_frames > VS1_MAX_FRAMES:
            indices = np.arange(0, total_frames, total_frames / VS1_MAX_FRAMES).astype(int)
        else:
            indices = np.arange(total_frames)
        wanted = set(int(i) for i in indices)
        frames = []
        container.seek(0)
        for i, frame in enumerate(container.decode(video=0)):
            if i > indices[-1]:
                break
            if i in wanted:
                frames.append(Image.fromarray(frame.to_ndarray(format="rgb24")))
        container.close()
        return frames

    def judge(self, clip: dict, seed: int) -> dict:
        frames = self.read_frames(clip["video"])
        prompt = VS1_PROMPT.format(text_prompt=clip["caption"])
        prompt += "<image> " * (len(frames) - prompt.count("<image>"))
        inputs = self.processor(text=prompt, images=frames, return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        with self.torch.no_grad():
            logits = self.model(**inputs).logits
        scores = [round(logits[0, i].item(), 3) for i in range(logits.shape[-1])]
        row = dict(zip(VS1_FIELDS, scores))
        row["num_frames"] = len(frames)
        return row


class VideoScore2:
    def __init__(self, checkpoint: Path, device: str, dtype: str):
        import os
        import torch

        os.environ.setdefault("FORCE_QWENVL_VIDEO_READER", "decord")  # qwen_vl_utils: linspace frame sampling via decord
        from transformers import AutoModelForVision2Seq, AutoProcessor, AutoTokenizer

        self.torch = torch
        kwargs = {"trust_remote_code": True}
        if dtype == "bf16":
            kwargs["torch_dtype"] = torch.bfloat16
        self.model = AutoModelForVision2Seq.from_pretrained(str(checkpoint), **kwargs).to(device)
        self.processor = AutoProcessor.from_pretrained(str(checkpoint), trust_remote_code=True)
        self.tokenizer = getattr(self.processor, "tokenizer", None) or AutoTokenizer.from_pretrained(
            str(checkpoint), trust_remote_code=True, use_fast=False)
        self.device = device

    def soft_score(self, hard_val, token_idx, scores):
        """ll_based_soft_score_normed() from vs2_inference.py."""
        import numpy as np

        if hard_val is None or token_idx < 0:
            return None, None
        logits = scores[token_idx][0]
        score_probs = []
        for s in range(1, 6):
            ids = self.tokenizer.encode(str(s), add_special_tokens=False)
            if len(ids) == 1:
                logp = self.torch.log_softmax(logits.float(), dim=-1)[ids[0]].item()
                score_probs.append((s, float(np.exp(logp))))
        if not score_probs:
            return None, None
        digit_probs = {str(s): round(p, 4) for s, p in score_probs}
        scores_list, probs_list = zip(*score_probs)
        total_prob = sum(probs_list)
        max_prob = max(probs_list)
        best_score = scores_list[probs_list.index(max_prob)]
        normalized_prob = max_prob / total_prob if total_prob > 0 else 0
        return round(best_score * normalized_prob, 4), digit_probs

    def score_token_index(self, prompt_text: str, gen_ids: list[int]) -> int:
        """find_score_token_index_by_prompt() from vs2_inference.py, with one change: the label is
        searched only after </think>, because the official search from the start of the text lands
        on the same words inside the reasoning and attaches the soft score to the wrong token."""
        gen_str = self.tokenizer.decode(gen_ids, skip_special_tokens=False)
        offset = gen_str.find("</think>")
        offset = offset if offset >= 0 else 0
        pattern = r"(?:\(\d+\)\s*|\n\s*)?" + re.escape(prompt_text)
        match = re.search(pattern, gen_str[offset:], flags=re.IGNORECASE)
        if not match:
            return -1
        end = offset + match.end()
        num_match = re.search(r"\d", gen_str[end:])
        if not num_match:
            return -1
        target_substr = gen_str[: end + num_match.start() + 1]
        for i in range(len(gen_ids)):
            if self.tokenizer.decode(gen_ids[: i + 1], skip_special_tokens=False) == target_substr:
                return i
        return -1

    def judge(self, clip: dict, seed: int) -> dict:
        from string import Template
        from qwen_vl_utils import process_vision_info

        user_prompt = Template(VS2_PROMPT).substitute(t2v_prompt=clip["caption"])
        messages = [{"role": "user", "content": [
            {"type": "video", "video": clip["video"], "fps": VS2_FPS},
            {"type": "text", "text": user_prompt},
        ]}]
        text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = self.processor(text=[text], images=image_inputs, videos=video_inputs, fps=VS2_FPS,
                                padding=True, return_tensors="pt").to(self.device)
        self.torch.manual_seed(seed)
        with self.torch.no_grad():
            gen_out = self.model.generate(
                **inputs, max_new_tokens=VS2_MAX_NEW_TOKENS, output_scores=True, return_dict_in_generate=True,
                do_sample=True, temperature=VS2_TEMPERATURE,
            )
        input_len = inputs["input_ids"].shape[1]
        gen_ids = gen_out.sequences[0, input_len:].tolist()
        output_text = self.processor.batch_decode(
            gen_out.sequences[:, input_len:], skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        # Official parse first. The released model often answers in the prompt's own wording,
        # "(1) visual quality – clarity, smoothness, artifacts: 4", which the official regex misses,
        # so fall back to the same three labels with any description before the colon, applied to
        # the text after </think> only.
        match = re.search(VS2_PATTERN, output_text, re.DOTALL | re.IGNORECASE)
        parser = "official"
        if not match:
            answer = output_text.split("</think>")[-1]
            match = re.search(VS2_PATTERN_LOOSE, answer, re.DOTALL | re.IGNORECASE)
            parser = "loose" if match else "none"
        hard = [int(match.group(i)) for i in (1, 2, 3)] if match else [None, None, None]
        row = {"v_score": hard[0], "t_score": hard[1], "p_score": hard[2], "parser": parser}
        for name, key in (("visual quality:", "v"), ("text-to-video alignment:", "t"),
                          ("physical/common-sense consistency:", "p")):
            idx = self.score_token_index(name, gen_ids)
            if idx < 0 and parser == "loose":
                idx = self.score_token_index(name[:-1], gen_ids)  # label without the colon
            row[f"{key}_soft"], row[f"{key}_digit_probs"] = self.soft_score(row[f"{key}_score"], idx, gen_out.scores)
            row[f"{key}_idx"] = idx
        row["raw"] = output_text
        row["gen_tokens"] = len(gen_ids)
        row["num_video_frames"] = int(video_inputs[0].shape[0]) if video_inputs else None
        row["seed"] = seed
        return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(CHECKPOINTS))
    ap.add_argument("--split", default="eval")
    ap.add_argument("--tags", nargs="+", default=EVAL_TAGS)
    ap.add_argument("--ids", nargs="+")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--seed", type=int, default=0, help="base seed; videoscore2 sampling uses seed + clip index")
    ap.add_argument("--dtype", default="fp32", choices=["fp32", "bf16"], help="videoscore2 only; official script loads fp32")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--checkpoint-root", type=Path, default=DEFAULT_CKPT_ROOT)
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    shard_i, shard_n = (int(x) for x in args.shard.split("/"))
    clips = load_clips(args.split, args.tags)
    for n, c in enumerate(clips):
        c["index"] = n  # stable seed per clip regardless of sharding
    if args.ids:
        wanted = set(args.ids)
        clips = [c for c in clips if c["id"] in wanted]
    clips = clips[shard_i::shard_n]
    done = {tag: done_ids(args.out_root, args.model, tag) for tag in args.tags}
    todo = [c for c in clips if c["id"] not in done[c["tag"]]]
    print(f"{args.model} shard {shard_i}/{shard_n}: {len(clips)} clips, {len(todo)} to do", flush=True)
    if args.limit:
        todo = todo[: args.limit]
    checkpoint = args.checkpoint_root / CHECKPOINTS[args.model]
    if args.check_only:
        import importlib.util
        print(f"checkpoint {checkpoint}: {'ok' if (checkpoint / 'config.json').is_file() else 'MISSING'}")
        mods = ("torch", "transformers", "av", "mantis") if args.model == "videoscore1" else \
               ("torch", "transformers", "qwen_vl_utils", "cv2", "torchvision", "av")
        for mod in mods:
            print(f"  {mod}: {'ok' if importlib.util.find_spec(mod) else 'MISSING'}")
        return 0
    if not todo:
        return 0

    t0 = time.time()
    rater = VideoScore1(checkpoint, args.device) if args.model == "videoscore1" else \
        VideoScore2(checkpoint, args.device, args.dtype)
    print(f"loaded {args.model} in {time.time() - t0:.0f}s", flush=True)
    out_dir = args.out_root / args.model
    out_dir.mkdir(parents=True, exist_ok=True)
    handles = {}
    t_start = time.time()
    for n, clip in enumerate(todo, 1):
        t1 = time.time()
        try:
            scores = rater.judge(clip, args.seed + clip["index"])
        except Exception as exc:
            print(f"ERROR {clip['tag']} {clip['id']}: {exc!r}", file=sys.stderr, flush=True)
            continue
        row = {"id": clip["id"], "tag": clip["tag"], "caption": clip["caption"], "video": clip["video"],
               "model": args.model, **scores, "elapsed_s": round(time.time() - t1, 2)}
        tag = clip["tag"]
        if tag not in handles:
            handles[tag] = open(out_dir / f"{tag}.shard{shard_i}of{shard_n}.jsonl", "a")
        handles[tag].write(json.dumps(row) + "\n")
        handles[tag].flush()
        if n % 10 == 0 or n == len(todo):
            brief = {k: row[k] for k in ("t2v_alignment", "factual_consistency", "t_score", "p_score") if k in row}
            print(f"[{n}/{len(todo)}] {tag} {clip['id']} {brief} ({(time.time() - t_start) / n:.1f}s/clip)", flush=True)
    for h in handles.values():
        h.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
