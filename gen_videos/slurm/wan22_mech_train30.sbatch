#!/bin/bash
# Prompt check: the first 30 Mechanics train IDs (MECH-0001..0030, 26 records, IDs have gaps) with
# Wan2.2-T2V-A14B at its official 480p settings (832x480x81, 40 steps, cfg 4.0/3.0, flow_shift 12).
# 13 array shards x 2 videos on one A100-40GB each. Both 14B experts + umT5 exceed 40 GB, so the
# pipeline uses model CPU offload (~70 GB host RAM in bf16), hence --mem=128g.
#   cd ~/phyRubric && sbatch gen_videos/slurm/wan22_mech_train30.sbatch
# Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128g
#SBATCH --time=03:00:00
#SBATCH --array=0-12
#SBATCH --job-name=wan22_mech30
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
  --backend wan22 --model "$MODELS/Wan2.2-T2V-A14B-Diffusers" --tag Wan2.2-T2V-A14B \
  --out-root "$OUT_ROOT" --split train --category Mechanics --limit 26 --shard "${SLURM_ARRAY_TASK_ID}/13"
echo "done at $(date)"
