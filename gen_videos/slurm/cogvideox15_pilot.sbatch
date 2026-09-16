#!/bin/bash
# Pilot: one Mechanics caption with CogVideoX1.5-5B (official settings: 1360x768, 81 frames, 50 steps, cfg 6).
#   cd ~/phyRubric && sbatch gen_videos/slurm/cogvideox15_pilot.sbatch
# Output goes to the same directory as the full run, so the pilot video is reused there.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64g
#SBATCH --time=01:30:00
#SBATCH --job-name=cogx15_pilot
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.err

set -euo pipefail
echo "job $SLURM_JOB_ID on $(hostname) at $(date)"
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
  --out-root "$OUT_ROOT" --split train --category Mechanics --ids MECH-0001
echo "done at $(date)"
