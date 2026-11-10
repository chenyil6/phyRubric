# PhyRubric

PhyRubric is a rubric-grounded diagnostic framework for evaluating **physical commonsense in text-to-video generation**.

For each caption, PhyRubric constructs a caption-specific rubric *before any video is seen*, decomposing the caption into semantic items (what the clip has to show, **SA**) and physical items (what everyday physics has to hold, **PC**). A clip is then judged item by item, each verdict (pass / fail / not shown) grounded in timestamped evidence, and the two 1–5 scores are derived from those verdicts by a fixed rule.

The framework is instantiated as **PhyRubric-Bench**, 245 captions spanning 34 categories across five physical domains (Mechanics, Heat, Optics, Electricity, Acoustics) with 2,433 labelled clips from 10 video generators, and scaled up to **PhyRubric-Train**, 947 captions with 3,788 labelled clips from 4 generators, on which we fine-tune the open-source **PhyRubric-Judge** (Qwen3-VL-8B-Instruct). Given only the caption and the clip, the judge outputs the SA score, whether the clip's physics can be assessed at all (`pc_assessable`, i.e. the central event actually happens), the PC score, and a timestamped reason.

- Paper: *(link)*
- Videos: [PhyRubric-Bench](https://huggingface.co/datasets/HF_USER/PhyRubric-Bench) (eval) · [PhyRubric-Train](https://huggingface.co/datasets/HF_USER/PhyRubric-Train) (train)
- Judge weights: [PhyRubric-Judge](https://huggingface.co/HF_USER/PhyRubric-Judge) (LoRA adapter on Qwen3-VL-8B-Instruct)

## Environment

- Python 3.11, one GPU with 80 GB or more for training and inference of the 8B judge
- [ms-swift](https://github.com/modelscope/ms-swift) 4.5 (training and inference), `decord`, `qwen-vl-utils`
- vLLM 0.30 for the GRPO stage and for the Qwen3-VL-235B baseline
- `google-genai` for the Gemini baseline; the VideoPhy and VideoScore raters each use the environment of their official repository (see the top of the file in `baselines/`)

## Installation

```bash
git clone https://github.com/chenyil6/phyRubric && cd phyRubric
pip install ms-swift==4.5.3 decord qwen-vl-utils huggingface_hub
huggingface-cli download HF_USER/PhyRubric-Bench --repo-type dataset --local-dir PhyRubric-Bench   # 2,433 eval clips, ~3 GB
huggingface-cli download HF_USER/PhyRubric-Train --repo-type dataset --local-dir PhyRubric-Train   # 3,788 train clips, ~3 GB
```

All video paths in the repository are relative to its root (`./PhyRubric-Bench/<generator>/eval/<ID>.mp4`), so nothing else needs to be configured. Two optional checks after the download:

```bash
python rubrics/build.py check              # validates the 1,192 rubrics
python annotations/scoring.py --check      # recomputes every stored SA / PC from the item statuses
```

## Usage

Every experiment is one script in `scripts/`; settings are passed as environment variables (the full list is in each script's header). Checkpoints are looked up under `$PJ_MODELS` (default `models/`), outputs are written to `$PJ_RUNS` (default `runs/`).

### Evaluate the released judge on PhyRubric-Bench

```bash
huggingface-cli download HF_USER/PhyRubric-Judge --local-dir models/PhyRubric-Judge
CKPT=models/PhyRubric-Judge RUN=judge bash scripts/infer.sh
```

`infer.sh` writes one JSON line per clip to `runs/judge/eval.shard0of1.jsonl` (greedy scores, soft scores, reason) and then prints the metrics against the gold labels (Spearman, AUROC, kappa, joint pass; per generator and pooled), saved to `runs/judge/eval_metrics.json`. The base model `Qwen/Qwen3-VL-8B-Instruct` is fetched from Hugging Face automatically; set `MODEL=/path/to/Qwen3-VL-8B-Instruct` to use a local copy.

To split the 2,433 clips over several GPUs, run one shard per GPU and the summary once at the end:

```bash
CKPT=models/PhyRubric-Judge RUN=judge SHARD=0 SHARDS=4 bash scripts/infer.sh    # ... SHARD=1,2,3 on the other GPUs
RUN=judge SUMMARY=1 bash scripts/infer.sh
```

The zero-shot base model is the same command without `CKPT`:

```bash
RUN=base8b bash scripts/infer.sh
```

### Train the judge

```bash
# LoRA-SFT of Qwen3-VL-8B-Instruct on data/sft_train.jsonl: 2 epochs, lr 1e-4, rank 16, one GPU
MODEL=Qwen/Qwen3-VL-8B-Instruct OUT=runs/sft bash scripts/train_sft.sh

# evaluate the result (the last checkpoint is checkpoint-900)
CKPT=runs/sft/<run dir>/checkpoint-900 RUN=sft bash scripts/infer.sh

# optional GRPO stage on top of the SFT adapter (rewards = agreement with the gold scores; needs vLLM)
MODEL=Qwen/Qwen3-VL-8B-Instruct START=runs/sft/<run dir>/checkpoint-900 OUT=runs/grpo bash scripts/train_grpo.sh
```

`RESUME=1` on either training script continues from the latest checkpoint in `$OUT`; `MAX_STEPS=20` makes a smoke test.

### Baselines

```bash
MODEL=videophy2 bash scripts/baseline_videophy.sh          # or videophy1; needs the official repo at $VIDEOPHY_CODE
MODEL=videoscore2 bash scripts/baseline_videoscore.sh      # or videoscore1
MODEL=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 TP=4 bash scripts/baseline_qwen235b.sh
GCP_PROJECT=<project> MODEL=gemini-4-argon THINKING=LOW bash scripts/baseline_gemini.sh
```

The VideoPhy and VideoScore scripts expect the released checkpoints under `$PJ_MODELS` (`videocon_physics`, `videophy_2_auto`, `VideoScore-v1.1`, `VideoScore2`) and accept the same `SHARD` / `SHARDS` / `SUMMARY=1` variables as `infer.sh`. All baseline metrics are computed by `baselines/videophy_official_summary.py` with the same definitions as the judge's.

## Repository layout

```
phyRubric
├── captions/                      the benchmark captions
│   ├── train/<branch>.json        947 train captions, one file per branch (mechanics, heat, optics, electricity, acoustics)
│   └── eval/<branch>.json         245 eval captions. Record: id, caption, category, subcategory, violation_types, expectation
├── rubrics/                       one rubric per caption
│   ├── train/<branch>/<ID>.json   SA items (id, weight core|minor, check) and PC items (id, severity, type, expect, fail)
│   ├── eval/<branch>/<ID>.json
│   ├── _policy.json               the rubric format and the scoring rule (how item statuses become SA / PC)
│   └── build.py                   `check` validates every rubric; load(split) returns {id: rubric}
├── annotations/                   gold labels, one file per generator
│   ├── train/<generator>.json     3,788 clips: sa_score, pc_score, recognisable_attempt, clip_summary, uncovered,
│   ├── eval/<generator>.json      2,433 clips  and items = [{id, status pass|fail|not_shown, evidence}]
│   └── scoring.py                 the scoring rule in code; `--check` recomputes all stored scores from the items
├── data/                          the labels in judge-training form (ms-swift "messages + videos" rows)
│   ├── sft_train.jsonl            3,788 rows: system prompt, caption + <video>, target {sa_score, pc_assessable, pc_score, reason}
│   ├── sft_val.jsonl              188 rows held out from the train captions (47 captions x 4 generators)
│   ├── grpo_train.jsonl           the same prompts without the target, plus sa_gold / pc_gold / assess_gold for the rewards
│   ├── grpo_val.jsonl
│   ├── eval.jsonl                 2,433 rows: the eval split in the same form, used by every judge run
│   └── system_prompt.txt          the judge's system prompt (the two scales in words; no rubric)
├── judge/                         PhyRubric-Judge
│   ├── infer.py                   runs the judge (base model or base + LoRA adapter) on data/eval.jsonl; greedy and soft scores
│   ├── summary.py                 metrics of a run against the gold labels: Spearman, AUROC, kappa, joint pass, per generator
│   ├── grpo_rewards.py            ms-swift reward plugin for GRPO: format, SA, PC and assessable agreement with the gold
│   └── grpo_lora_dtype.py         ms-swift plugin that keeps LoRA weights in bf16 so a GRPO run can resume from a checkpoint
├── baselines/                     the raters the judge is compared with
│   ├── videophy_official.py       official VideoPhy-1 (VideoCon-Physics) and VideoPhy-2 (AutoEval) raters on the eval clips
│   ├── videoscore_official.py     official VideoScore-v1.1 and VideoScore2 raters
│   ├── videophy_official_summary.py   metrics of the raters above against the gold labels (same metrics as judge/summary.py)
│   ├── qwen3vl_235b.py            zero-shot Qwen3-VL-235B-A22B-Instruct-FP8 through vLLM, same prompt and output as the judge
│   └── gemini_judge.py            zero-shot Gemini through Vertex AI, same prompt; optional verbalised 1-5 distribution
├── scripts/                       one shell script per experiment; settings are environment variables, see each header
│   ├── train_sft.sh               LoRA-SFT of Qwen3-VL-8B-Instruct on data/sft_train.jsonl
│   ├── train_grpo.sh              GRPO on top of the SFT adapter with the rewards in judge/grpo_rewards.py
│   ├── infer.sh                   judge inference + summary (shardable over GPUs)
│   ├── baseline_videophy.sh       VideoPhy-1 / VideoPhy-2 + metrics
│   ├── baseline_videoscore.sh     VideoScore-v1.1 / VideoScore2 + metrics
│   ├── baseline_qwen235b.sh       Qwen3-VL-235B + metrics
│   └── baseline_gemini.sh         Gemini + output table
├── PhyRubric-Bench/               the 2,433 eval videos, <generator>/eval/<ID>.mp4 (downloaded from Hugging Face)
└── PhyRubric-Train/               the 3,788 train videos, <generator>/train/<ID>.mp4 (downloaded from Hugging Face)
```

Model checkpoints are read from `$PJ_MODELS` (default `models/`) and outputs are written to `$PJ_RUNS` (default `runs/`); both are ignored by git.

## Citation

```bibtex
@article{phyrubric2026,
  title  = {PhyRubric: ...},
  author = {...},
  year   = {2026}
}
```
