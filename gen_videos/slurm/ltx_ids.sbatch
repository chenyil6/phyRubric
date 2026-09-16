#!/bin/bash
# Render an explicit list of ids with LTX-Video 2B 0.9.8 distilled (A40 only: ~15 GB, ~25 s/video).
#   IDS="HEAT-0001 HEAT-0002" sbatch --export=ALL,IDS gen_videos/slurm/ltx_ids.sbatch
# Output goes to the standard <out-root>/LTX-Video-2B-0.9.8-distilled/<train|eval>/ directory; finished videos are skipped.
#SBATCH --account=bilw-delta-gpu
#SBATCH --partition=gpuA40x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48g
#SBATCH --time=00:40:00
#SBATCH --job-name=ltx_ids
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.err
set -euo pipefail
: "${IDS:?set IDS to a space-separated id list}"
echo "job $SLURM_JOB_ID on $(hostname) at $(date); ids: $IDS"
REPO="$HOME/phyRubric"; MODELS="/work/nvme/bilw/hchen56/models"; OUT_ROOT="/work/hdd/bilw/hchen56/phyRubric_outputs"
export HF_HOME="/work/hdd/bilw/hchen56/hf"
module reset; source ~/miniconda3/etc/profile.d/conda.sh; conda activate ~/conda-envs/t2v
cd "$REPO"
# shellcheck disable=SC2086
python gen_videos/generate.py --backend ltx --model "$MODELS/LTX-Video-2B-0.9.8-distilled" --tag LTX-Video-2B-0.9.8-distilled \
  --out-root "$OUT_ROOT" --ids $IDS
echo "done at $(date)"
