#!/bin/bash
# Full Heat train split (250 captions) with Wan2.2-T2V-A14B at its
# official 480p settings (832x480x81, 40 steps, cfg 4.0/3.0, flow_shift 12).
# 25 array shards x 10 captions on one A100-40GB each (~825 s/video + ~1400 s weight load -> ~3.5 h/shard).
# Both 14B experts + umT5 exceed 40 GB, so the pipeline uses model CPU offload (~70 GB host RAM in bf16).
# Weights come from the bf16 copy (gen_videos/tools/convert_wan22_bf16.py): the published fp32 shards
# needed a 121 GB host peak and ~23 min per load; bf16 loads in seconds; measured steady-state host RSS is 84 GB, so --mem=96g.
# Delta bills by max(GPU, host-mem) fraction: 96g = 1.5 GPU-equivalents on gpuA100x4, 1 on gpuA100x8
# (250 GB per GPU there), so both partitions are listed and whichever starts first wins.
#   cd ~/phyRubric && sbatch gen_videos/slurm/wan22_heat_train.sbatch
# Resubmitting is safe: finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA100x4,gpuA100x8
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96g
#SBATCH --time=05:00:00
#SBATCH --array=0-24
#SBATCH --job-name=wan22_heat
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
  --backend wan22 --model "$MODELS/Wan2.2-T2V-A14B-Diffusers-bf16" --tag Wan2.2-T2V-A14B \
  --out-root "$OUT_ROOT" --split train --category Heat --shard "${SLURM_ARRAY_TASK_ID}/25"
echo "done at $(date)"
