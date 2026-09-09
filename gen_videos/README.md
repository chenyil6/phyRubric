# Text-to-video generation

`generate.py` renders the caption dataset (`data/train.json`, `data/eval.json`) with one
model per run. The generation text is the caption verbatim: no upsampling, no style suffix.

Outputs: `outputs/<tag>/<ID>_s<seed>.mp4` (ignored by Git) plus an append-only manifest
`manifests/<tag>.jsonl` with the caption, model, sampling settings, output path and
per-video wall time (for SU budgeting). Finished videos are skipped on rerun, so a killed
Slurm job is just resubmitted.

```bash
# preflight (any node with the env; checks packages, GPU, weights, selection)
python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --check-only --per-category 10

# pilot: 10 per category, shard 0 of 5
python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --per-category 10 --shard 0/5

# a full split in 40 shards (Slurm array)
python gen_videos/generate.py --backend cogvideox --model $MODELS/CogVideoX-5b --split train --shard $SLURM_ARRAY_TASK_ID/40
```

Selection flags: `--split`, `--category`, `--ids MECH-0001 ...`, `--per-category N`
(round-robin over subcategories, deterministic), `--shard K/N`.

Backends: `cogvideox15` (CogVideoX1.5-5B, 1360x768x81), `wan22` (Wan2.2-T2V-A14B, 832x480x81) run in
the `t2v` conda env; `hunyuan15` (HunyuanVideo-1.5 720p_t2v, 1280x720x121) needs diffusers>=0.36 and
runs in the separate `t2v-hy15` env (clone of t2v with diffusers 0.40 / transformers 5.16, because
the t2v env's transformers 4.57 pins huggingface-hub<1). `--manifest-dir` points the manifest at
another checkout's `gen_videos/manifests` when generate.py runs from a worktree.

Adding a model = adding one loader to `BACKENDS` in `generate.py` (see the `cogvideox`
entry). Slurm templates live in `slurm/`; fill in the account, model and env lines.
