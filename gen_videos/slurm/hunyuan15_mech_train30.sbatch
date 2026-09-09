#!/bin/bash
# Pilot: the first 30 Mechanics train IDs (MECH-0001..0030, 26 records, IDs have gaps) with
# HunyuanVideo-1.5 at its official settings: RES=720p -> 1280x720x121 (default), RES=480p -> 848x480x121;
# 50 steps, cfg 6.0, shift 9, 24 fps. 13 array shards x 2 videos on one A100-40GB each.
# DiT (16.6 GB) + Qwen2.5-VL-7B (14 GB) + VAE do not fit together on 40 GB, so the pipeline uses
# model CPU offload (~35 GB host RAM), hence --mem=96g. Attention runs through the sliced
# processor in generate.py (the stock one builds a 12.7 GB dense mask at 720p and OOMs).
# Runs from the separate t2v-hy15 conda env (diffusers 0.40 / transformers 5.16; see README).
#   sbatch gen_videos/slurm/hunyuan15_mech_train30.sbatch                       # 720p, all 13 shards
#   RES=480p sbatch --export=ALL,RES --array=0 gen_videos/slurm/hunyuan15_mech_train30.sbatch   # 480p, shard 0 only
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
#SBATCH --array=0-12
#SBATCH --job-name=hy15_mech30
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.err

set -euo pipefail
echo "job $SLURM_JOB_ID shard $SLURM_ARRAY_TASK_ID on $(hostname) at $(date)"
REPO="${REPO:-$HOME/phyRubric}"
RES="${RES:-720p}"
MANIFESTS="$HOME/phyRubric/gen_videos/manifests"
MODELS="/work/nvme/bilw/hchen56/models"
OUT_ROOT="/work/hdd/bilw/hchen56/phyRubric_outputs"
export HF_HOME="/work/hdd/bilw/hchen56/hf"
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
module reset
source ~/miniconda3/etc/profile.d/conda.sh
conda activate ~/conda-envs/t2v-hy15

if [ "$RES" = "480p" ]; then SIZE=(--height 480 --width 848); else SIZE=(); fi
cd "$REPO"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python gen_videos/generate.py \
  --backend hunyuan15 --model "$MODELS/HunyuanVideo-1.5-Diffusers-${RES}_t2v" --tag "HunyuanVideo-1.5-${RES}" \
  --out-root "$OUT_ROOT" --manifest-dir "$MANIFESTS" "${SIZE[@]}" \
  --split train --category Mechanics --limit 26 --shard "${SLURM_ARRAY_TASK_ID}/13"
echo "done at $(date)"
