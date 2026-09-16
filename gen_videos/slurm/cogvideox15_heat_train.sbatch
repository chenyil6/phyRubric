#!/bin/bash
# Full Heat train split (250 captions) with CogVideoX1.5-5B, official settings.
# 25 array shards x 10 videos on one A100-40GB each (~17 min/video with CPU offload -> ~3 h/shard).
#   cd ~/phyRubric && sbatch gen_videos/slurm/cogvideox15_heat_train.sbatch
# Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4,gpuA100x8
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64g
#SBATCH --time=05:00:00
#SBATCH --array=0-24
#SBATCH --job-name=cogx15_heat
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
  --backend cogvideox15 --model "$MODELS/CogVideoX1.5-5B" --tag CogVideoX1.5-5B \
  --out-root "$OUT_ROOT" --split train --category Heat --shard "${SLURM_ARRAY_TASK_ID}/25"
echo "done at $(date)"
