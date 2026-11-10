#!/usr/bin/env python3
"""Run the official VideoPhy-1 (VideoCon-Physics) and VideoPhy-2 (AutoEval) raters on our benchmark clips.

Both raters are the same mPLUG-Owl-video 7B architecture released with
https://github.com/Hritikbansal/videophy; the official inference code is used as-is
(`VIDEOPHY2/mplug_owl_video`, identical to the VideoCon copy) with one change that
does not touch the model path: clips come from our manifests and results are written as
resumable JSONL.

Scoring reproduces the official scripts exactly:
  videophy1 : videocon/training/pipeline_video/entailment_inference.py -> P(Yes) / (P(Yes)+P(No))
              at the answer position, prompts from utils/constants.py (PROMPT_VTA / PROMPT_PHYSICS).
  videophy2 : VIDEOPHY2/inference.py -> greedy generation, first 0-5 word/digit found, prompts
              from VIDEOPHY2/template.py (PROMPT_SA / PROMPT_PHYSICS).
Both use 32 uniformly spaced frames at 224x224.

Output: <out-root>/<model>/<tag>.shard<i>of<n>.jsonl, one row per clip with both tasks.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OFFICIAL = Path(os.environ.get("VIDEOPHY_CODE", ROOT / "third_party" / "videophy"))   # clone of github.com/Hritikbansal/videophy
DEFAULT_CKPT_ROOT = Path(os.environ.get("PJ_MODELS", ROOT / "models"))                      # <root>/videocon_physics, <root>/videophy_2_auto
DEFAULT_OUT_ROOT = Path(os.environ.get("PJ_RUNS", ROOT / "runs")) / "baselines"
MANIFEST_DIR = ROOT / "gen_videos" / "manifests"
EVAL_TAGS = [
    "CogVideoX1.5-5B",
    "Cosmos-Predict2.5-14B",
    "Cosmos-Predict2.5-2B",
    "HunyuanVideo-1.5-480p",
    "LTX-2.3-22B-distilled",
    "LTX-Video-2B-0.9.8-distilled",
    "Wan2.2-T2V-A14B",
    "Wan2.2-TI2V-5B",
    "Seedance-2.5-480p",
]
CHECKPOINTS = {"videophy1": "videocon_physics", "videophy2": "videophy_2_auto"}

# --- prompts, verbatim from the official repo -------------------------------------------
# videophy/utils/constants.py
V1_PROMPT_SA = '''The following is a conversation between a curious human and AI assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
Human: <|video|>
Human: Does this video entail the description: "{caption}"?
AI: '''
V1_PROMPT_PC = '''The following is a conversation between a curious human and AI assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
Human: <|video|>
Human: Does this video follow the physical laws?
AI: '''
# videophy/VIDEOPHY2/template.py
V2_PROMPT_SA = (
    "The following is a conversation between a curious human and an AI assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    "Human: <|video|>\n"
    "Human: Does this video match the description: \"{caption}\"? "
    "Please rate the video on a scale from 1 to 5, where 5 indicates a perfect match and 1 indicates no relevance.\n"
    "AI: "
)
V2_PROMPT_PC = (
    "The following is a conversation between a curious human and an AI assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    "Human: <|video|>\n"
    "Human: Does this video adhere to the physical laws? "
    "Rate the video on a scale from 1 to 5, where 5 means full compliance and 1 means significant violations.\n"
    "AI: "
)
V2_GENERATE_KWARGS = {"do_sample": False, "top_k": 1, "temperature": 0.001, "max_length": 256}
# VideoPhy-2 soft score (2026-10-18, --soft): the LLaMA tokenizer emits the digit as its own token (ids below, after a "▁"),
# so the expectation over 1..5 of the softmax at the first digit step is the same construction as our judge's soft score.
V2_DIGIT_IDS = {0: 29900, 1: 29896, 2: 29906, 3: 29941, 4: 29946, 5: 29945}
V2_NUM_MAP = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
}


# --- clip selection ---------------------------------------------------------------------
def load_clips(split: str, tags: list[str]) -> list[dict]:
    clips = []
    for tag in tags:
        path = MANIFEST_DIR / f"{tag}.jsonl"
        if not path.is_file():
            print(f"warning: no manifest for {tag}", file=sys.stderr)
            continue
        last: dict[str, dict] = {}
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("split") != split or not row.get("output_path"):
                continue
            last[row["id"]] = row
        for cid in sorted(last):
            row = last[cid]
            if os.path.isfile(row["output_path"]):
                clips.append({"id": cid, "tag": tag, "caption": row["caption"], "video": row["output_path"]})
    return clips


def done_ids(out_root: Path, model: str, tag: str) -> set[str]:
    done = set()
    for path in (out_root / model).glob(f"{tag}.shard*.jsonl"):
        for line in path.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)["id"])
    return done


# --- model wrapper ------------------------------------------------------------------------
def v2_parse_score(output: str):
    """Exactly the parsing in VIDEOPHY2/inference.py (dict order matters)."""
    output_lower = output.lower().strip()
    for key, val in V2_NUM_MAP.items():
        if key in output_lower:
            return val
    digits = "".join(c for c in output_lower if c.isdigit())
    return int(digits) if digits and int(digits) in V2_NUM_MAP.values() else 0


class OfficialRater:
    def __init__(self, model: str, checkpoint: Path, official: Path, device: str, num_frames: int, soft: bool = False):
        self.soft = soft
        sys.path.insert(0, str(official / "videocon" / "training" / "pipeline_video"))  # mplug_owl_video, data_utils, utils
        import torch
        from transformers.models.llama.tokenization_llama import LlamaTokenizer
        from mplug_owl_video.modeling_mplug_owl import MplugOwlForConditionalGeneration
        from mplug_owl_video.processing_mplug_owl import MplugOwlImageProcessor, MplugOwlProcessor

        self.model_name = model
        self.torch = torch
        self.num_frames = num_frames
        self.device = torch.device(device)
        self.tokenizer = LlamaTokenizer.from_pretrained(str(checkpoint))
        image_processor = MplugOwlImageProcessor.from_pretrained(str(checkpoint))
        self.processor = MplugOwlProcessor(image_processor, self.tokenizer)
        t0 = time.time()
        self.model = MplugOwlForConditionalGeneration.from_pretrained(
            str(checkpoint), torch_dtype=torch.bfloat16, device_map={"": "cpu"}
        )
        self.model = self.model.to(self.device).to(torch.bfloat16).eval()
        print(f"loaded {model} from {checkpoint} in {time.time() - t0:.0f}s", flush=True)

        if model == "videophy1":
            from data_utils.xgpt3_dataset import MultiModalDataset
            from utils import batchify

            # MultiModalDataset.__init__ reads a csv and the training args; we only need its
            # tokenisation method, so build an instance without running __init__.
            ds = MultiModalDataset.__new__(MultiModalDataset)
            ds.tokenizer = self.tokenizer
            ds.max_length = 256
            ds.media_tokens = {"<image>": -1, "<|video|>": -2}
            ds.media_lengths = {"<image>": 1 + 64, "<|video|>": 1 + 64}
            self.ds = ds
            self.batchify = batchify
            self.yes_id = self.tokenizer.encode("Yes", add_special_tokens=False)[0]
            self.no_id = self.tokenizer.encode("No", add_special_tokens=False)[0]

    # VideoPhy-1 ---------------------------------------------------------------------------
    def _v1_entail(self, logits, input_ids):
        """get_entail() from entailment_inference.py."""
        logits = self.torch.softmax(logits.float(), dim=2)
        scores = []
        for j in range(len(logits)):
            for i in range(len(input_ids[j])):
                if input_ids[j][i] == self.tokenizer.pad_token_id:
                    i = i - 1
                    break
                elif i == len(input_ids[j]) - 1:
                    break
            yes, no = logits[j][i][self.yes_id], logits[j][i][self.no_id]
            scores.append(float(yes / (yes + no)))
        return scores

    def _v1_score(self, video: str, prompt: str) -> float:
        video_input = self.processor(videos=[video], num_frames=self.num_frames, return_tensors="pt")
        text_input = self.ds._extract_text_token_from_conversation(prompt, self.ds.max_length, 0)
        batch = self.batchify([{"video": video_input, "text": text_input, "videopath": video, "caption": prompt}])
        inputs = {}
        for k, v in batch.items():
            if self.torch.is_tensor(v):
                if v.dtype == self.torch.float:
                    v = v.bfloat16()
                v = v.to(self.device)
            inputs[k] = v
        with self.torch.no_grad():
            out = self.model(
                pixel_values=inputs["pixel_values"], video_pixel_values=inputs["video_pixel_values"], labels=None,
                num_images=inputs["num_images"], num_videos=inputs["num_videos"], input_ids=inputs["input_ids"],
                non_padding_mask=inputs["non_padding_mask"], non_media_mask=inputs["non_media_mask"],
                prompt_mask=inputs["prompt_mask"],
            )
        return self._v1_entail(out["logits"], inputs["input_ids"])[0]

    # VideoPhy-2 ---------------------------------------------------------------------------
    def _v2_generate(self, video: str, prompt: str) -> tuple[int, str]:
        inputs = self.processor(text=[prompt], videos=[video], num_frames=self.num_frames, return_tensors="pt")
        inputs = {k: v.bfloat16() if v.dtype == self.torch.float else v for k, v in inputs.items()}
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with self.torch.no_grad():
            if self.soft:
                res = self.model.generate(**inputs, **V2_GENERATE_KWARGS, output_scores=True, return_dict_in_generate=True)
                seq = res.sequences
            else:
                res = self.model.generate(**inputs, **V2_GENERATE_KWARGS)
                seq = res
        output = self.tokenizer.decode(seq.tolist()[0], skip_special_tokens=True)
        if not self.soft:
            return v2_parse_score(output), output
        # first generated step whose greedy token is a digit; probabilities of 0..5 there, expectation over 1..5
        gen = seq[0, -len(res.scores):].tolist()
        soft, probs = None, None
        for step, tok in enumerate(gen):
            if tok in V2_DIGIT_IDS.values():
                pr = self.torch.softmax(res.scores[step][0].float(), dim=-1)
                probs = {d: float(pr[i]) for d, i in V2_DIGIT_IDS.items()}
                z = sum(probs[d] for d in range(1, 6))
                soft = sum(d * probs[d] for d in range(1, 6)) / z if z > 0 else None
                break
        return v2_parse_score(output), output, soft, probs

    def judge(self, clip: dict, tasks: list[str]) -> dict:
        row = {"id": clip["id"], "tag": clip["tag"], "caption": clip["caption"], "video": clip["video"],
               "model": self.model_name, "num_frames": self.num_frames}
        t0 = time.time()
        for task in tasks:
            if self.model_name == "videophy1":
                prompt = V1_PROMPT_SA.format(caption=clip["caption"]) if task == "sa" else V1_PROMPT_PC
                row[f"{task}_score"] = self._v1_score(clip["video"], prompt)
            else:
                prompt = V2_PROMPT_SA.format(caption=clip["caption"]) if task == "sa" else V2_PROMPT_PC
                if self.soft:
                    score, raw, soft, probs = self._v2_generate(clip["video"], prompt)
                    row[f"{task}_soft"] = round(soft, 4) if soft is not None else None
                    row[f"{task}_digit_probs"] = {k: round(v, 4) for k, v in probs.items()} if probs else None
                else:
                    score, raw = self._v2_generate(clip["video"], prompt)
                row[f"{task}_score"] = score
                row[f"{task}_raw"] = raw
        row["elapsed_s"] = round(time.time() - t0, 2)
        return row


# --- main ---------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(CHECKPOINTS))
    ap.add_argument("--tasks", nargs="+", default=["sa", "pc"], choices=["sa", "pc"])
    ap.add_argument("--split", default="eval")
    ap.add_argument("--tags", nargs="+", default=EVAL_TAGS)
    ap.add_argument("--ids", nargs="+", help="only these clip ids")
    ap.add_argument("--shard", default="0/1", help="i/n stride split of the (tag, id)-sorted clip list")
    ap.add_argument("--limit", type=int, help="stop after this many new clips")
    ap.add_argument("--num-frames", type=int, default=32)
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--checkpoint-root", type=Path, default=DEFAULT_CKPT_ROOT)
    ap.add_argument("--official-code", type=Path, default=DEFAULT_OFFICIAL)
    ap.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    ap.add_argument("--check-only", action="store_true", help="list the work and the environment; no model load")
    ap.add_argument("--soft", action="store_true", help="videophy2: also record the digit-probability soft score; outputs go to <model>_soft/")
    args = ap.parse_args()
    out_name = f"{args.model}_soft" if args.soft else args.model

    shard_i, shard_n = (int(x) for x in args.shard.split("/"))
    clips = load_clips(args.split, args.tags)
    if args.ids:
        wanted = set(args.ids)
        clips = [c for c in clips if c["id"] in wanted]
    clips = clips[shard_i::shard_n]
    done = {}
    for tag in args.tags:
        done[tag] = done_ids(args.out_root, out_name, tag)
    todo = [c for c in clips if c["id"] not in done[c["tag"]]]
    print(f"{args.model} shard {shard_i}/{shard_n}: {len(clips)} clips, {len(todo)} to do, tasks={args.tasks}", flush=True)
    if args.limit:
        todo = todo[: args.limit]

    checkpoint = args.checkpoint_root / CHECKPOINTS[args.model]
    if args.check_only:
        import importlib.util
        print(f"checkpoint {checkpoint}: {'ok' if (checkpoint / 'config.json').is_file() else 'MISSING'}")
        for mod in ("torch", "transformers", "av", "peft", "h5py", "icecream", "einops", "sentencepiece"):
            print(f"  {mod}: {'ok' if importlib.util.find_spec(mod) else 'MISSING'}")
        mplug = args.official_code / "videocon" / "training" / "pipeline_video" / "mplug_owl_video" / "modeling_mplug_owl.py"
        print(f"  official code: {'ok' if mplug.is_file() else 'MISSING'} ({mplug})")
        return 0
    if not todo:
        return 0

    rater = OfficialRater(args.model, checkpoint, args.official_code, args.device, args.num_frames, soft=args.soft)
    out_dir = args.out_root / out_name
    out_dir.mkdir(parents=True, exist_ok=True)
    handles = {}
    t_start = time.time()
    for n, clip in enumerate(todo, 1):
        try:
            row = rater.judge(clip, args.tasks)
        except Exception as exc:  # keep going; the clip stays undone for a rerun
            print(f"ERROR {clip['tag']} {clip['id']}: {exc!r}", file=sys.stderr, flush=True)
            continue
        tag = clip["tag"]
        if tag not in handles:
            handles[tag] = open(out_dir / f"{tag}.shard{shard_i}of{shard_n}.jsonl", "a")
        handles[tag].write(json.dumps(row) + "\n")
        handles[tag].flush()
        if n % 10 == 0 or n == len(todo):
            rate = (time.time() - t_start) / n
            print(f"[{n}/{len(todo)}] {tag} {clip['id']} {row.get('sa_score')} {row.get('pc_score')} "
                  f"({rate:.1f}s/clip)", flush=True)
    for h in handles.values():
        h.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
