#!/bin/bash
# Quality check: the first 30 Mechanics train captions (17 inertia + 13 gravity_fall) with CogVideoX-5b.
# 3 array shards x 10 videos on one A100 each, ~40 min per shard.
#   cd ~/phyRubric && sbatch gen_videos/slurm/cogvideox_mech_train30.sbatch
# Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48g
#SBATCH --time=01:15:00
#SBATCH --array=0-2
#SBATCH --job-name=cogx_mech30
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%A_%a.err

set -euo pipefail
echo "job $SLURM_JOB_ID shard $SLURM_ARRAY_TASK_ID on $(hostname) at $(date)"
REPO="$HOME/phyRubric"
MODELS="/work/nvme/bilw/hchen56/models"
export HF_HOME="/work/hdd/bilw/hchen56/hf"
module reset
source ~/miniconda3/etc/profile.d/conda.sh
conda activate ~/conda-envs/t2v

cd "$REPO"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
python gen_videos/generate.py \
  --backend cogvideox --model "$MODELS/CogVideoX-5b" --tag cogvideox5b \
  --split train --category Mechanics --limit 30 --shard "${SLURM_ARRAY_TASK_ID}/3"
echo "done at $(date)"
