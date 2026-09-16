#!/bin/bash
# Full Mechanics train split (250 captions; the 26 pilot videos are skipped) with HunyuanVideo-1.5 480p_t2v
# at its official settings: 848x480x121, 50 steps, cfg 6.0, 24 fps.
# 25 array shards x 10 captions on one A100-40GB each (~850 s/video + ~450 s weight load -> ~2.5 h/shard).
# DiT + Qwen2.5-VL-7B + VAE do not fit together on 40 GB, so the pipeline uses model CPU offload
# (~35 GB host RAM), hence --mem=96g. Attention runs through the sliced processor in generate.py.
# Runs from the separate t2v-hy15 conda env (diffusers 0.40 / transformers 5.16; see README).
#   cd ~/phyRubric && REPO=/path/to/checkout sbatch --export=ALL,REPO gen_videos/slurm/hunyuan15_mech_train.sbatch
# REPO may be overridden to run generate.py from another checkout (e.g. a worktree); the manifest
# always lands in the main checkout's gen_videos/manifests. Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96g
#SBATCH --time=04:00:00
#SBATCH --array=0-24
#SBATCH --job-name=hy15_mech
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.err

set -euo pipefail
echo "job $SLURM_JOB_ID shard $SLURM_ARRAY_TASK_ID on $(hostname) at $(date)"
REPO="${REPO:-$HOME/phyRubric}"
MANIFESTS="$HOME/phyRubric/gen_videos/manifests"
MODELS="/work/nvme/bilw/hchen56/models"
OUT_ROOT="/work/hdd/bilw/hchen56/phyRubric_outputs"
export HF_HOME="/work/hdd/bilw/hchen56/hf"
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
module reset
source ~/miniconda3/etc/profile.d/conda.sh
conda activate ~/conda-envs/t2v-hy15

cd "$REPO"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python gen_videos/generate.py \
  --backend hunyuan15 --model "$MODELS/HunyuanVideo-1.5-Diffusers-480p_t2v" --tag HunyuanVideo-1.5-480p \
  --out-root "$OUT_ROOT" --manifest-dir "$MANIFESTS" --height 480 --width 848 \
  --split train --category Mechanics --shard "${SLURM_ARRAY_TASK_ID}/25"
echo "done at $(date)"
