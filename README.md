# PhyRubric

PhyRubric is a rubric-grounded diagnostic framework for evaluating **physical commonsense in text-to-video generation**.

For each caption, PhyRubric constructs a caption-specific rubric *before any video is seen*, decomposing the caption into semantic items (what the clip has to show, **SA**) and physical items (what everyday physics has to hold, **PC**). A clip is then judged item by item, each verdict (pass / fail / not shown) grounded in timestamped evidence, and the two 1–5 scores are derived from those verdicts by a fixed rule.

The framework is instantiated as **PhyRubric-Bench**, 245 captions spanning 34 categories across five physical domains (Mechanics, Heat, Optics, Electricity, Acoustics) with 2,433 labelled clips from 10 video generators, and scaled up to **PhyRubric-Train**, 947 captions with 3,788 labelled clips from 4 generators, on which we fine-tune the open-source **PhyRubric-Judge** (Qwen3-VL-8B-Instruct). Given only the caption and the clip, the judge outputs the SA score, whether the clip's physics can be assessed at all (`pc_assessable`, i.e. the central event actually happens), the PC score, and a timestamped reason.

- 📄 Paper: [PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in Text-to-Video Generation](https://arxiv.org/abs/2611.13576)
- 🎬 Videos: [PhyRubric-Bench](https://huggingface.co/datasets/kittyhy/PhyRubric-Bench) (eval) · [PhyRubric-Train](https://huggingface.co/datasets/kittyhy/PhyRubric-Train) (train)
- 🤗 Judge weights: [PhyRubric-Judge](https://huggingface.co/kittyhy/PhyRubric-Judge) (LoRA adapter on Qwen3-VL-8B-Instruct)

## Environment

- Python 3.11, one GPU with 80 GB or more for training and inference of the 8B judge
- [ms-swift](https://github.com/modelscope/ms-swift) 4.5 (training and inference), `decord`, `qwen-vl-utils`
- vLLM 0.30 for the GRPO stage and for the Qwen3-VL-235B baseline
- `google-genai` for the Gemini baseline; the VideoPhy and VideoScore raters each use the environment of their official repository (see the top of the file in `baselines/`)

## Installation

```bash
git clone https://github.com/chenyil6/phyRubric && cd phyRubric
pip install ms-swift==4.5.3 decord qwen-vl-utils "huggingface_hub[cli]"
hf download kittyhy/PhyRubric-Bench --repo-type dataset --local-dir PhyRubric-Bench   # 2,433 eval clips, ~3 GB
hf download kittyhy/PhyRubric-Train --repo-type dataset --local-dir PhyRubric-Train   # 3,788 train clips, ~3 GB
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
hf download kittyhy/PhyRubric-Judge --local-dir models/PhyRubric-Judge
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
├── captions/                 captions: captions/<split>/<branch>.json
├── rubrics/                  one rubric per caption: rubrics/<split>/<branch>/<ID>.json
│   ├── _policy.json          rubric format and scoring rule
│   └── build.py              `check` validates the rubrics; load(split) reads them
├── annotations/              gold labels, one file per generator: annotations/<split>/<generator>.json
│   └── scoring.py            SA / PC from the item statuses; `--check` verifies the stored scores
├── data/                     judge-training rows (ms-swift format)
│   ├── sft_train.jsonl, sft_val.jsonl      SFT
│   ├── grpo_train.jsonl, grpo_val.jsonl    GRPO
│   ├── eval.jsonl                          the eval split
│   └── system_prompt.txt                   the judge's system prompt
├── judge/                    PhyRubric-Judge
│   ├── infer.py              inference
│   ├── summary.py            metrics against the gold labels
│   └── grpo_rewards.py, grpo_lora_dtype.py   ms-swift plugins for GRPO
├── baselines/                VideoPhy-1/2, VideoScore-v1.1/2, Qwen3-VL-235B and Gemini raters, plus their metrics script
├── scripts/                  one shell script per experiment (train_sft, train_grpo, infer, baseline_*)
├── PhyRubric-Bench/          eval videos from Hugging Face: <generator>/eval/<ID>.mp4
└── PhyRubric-Train/          train videos from Hugging Face: <generator>/train/<ID>.mp4
```

Checkpoints are read from `$PJ_MODELS` (default `models/`) and outputs are written to `$PJ_RUNS` (default `runs/`); both are git-ignored.

## Citation

```bibtex
@article{phyrubric2026,
  title  = {PhyRubric: ...},
  author = {...},
  year   = {2026}
}
```
