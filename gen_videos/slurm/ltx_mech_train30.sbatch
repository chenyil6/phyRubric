#!/bin/bash
# Prompt check: the first 30 Mechanics train IDs (MECH-0001..0030, 26 records, IDs have gaps) with
# LTX-Video 2B 0.9.8 distilled, official two-stage recipe (1216x704x121 @ 24 fps, 8+4 fixed steps, no CFG).
# ~15 GB VRAM, so any GPU works: ask for an A40 or an A100, whichever frees up first.
# 4 array shards x 6-7 videos on one GPU each.
#   cd ~/phyRubric && sbatch gen_videos/slurm/ltx_mech_train30.sbatch
# Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA40x4,gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48g
#SBATCH --time=01:30:00
#SBATCH --array=0-3
#SBATCH --job-name=ltx_mech30
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.err

set -euo pipefail
echo "job $SLURM_JOB_ID shard $SLURM_ARRAY_TASK_ID on $(hostname) at $(date)"
REPO="$HOME/phyRubric"
MODELS="/work/nvme/bilw/hchen56/models"
OUT_ROOT="/work/hdd/bilw/hchen56/phyRubric_outputs"
export HF_HOME="/work/hdd/bilw/hchen56/hf"
module reset
source ~/miniconda3/etc/profile.d/conda.sh
conda activate ~/conda-envs/t2v

cd "$REPO"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python gen_videos/generate.py \
  --backend ltx --model "$MODELS/LTX-Video-2B-0.9.8-distilled" --tag LTX-Video-2B-0.9.8-distilled \
  --out-root "$OUT_ROOT" --split train --category Mechanics --limit 26 --shard "${SLURM_ARRAY_TASK_ID}/4"
echo "done at $(date)"
