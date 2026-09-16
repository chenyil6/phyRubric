#!/bin/bash
# One-off: write a bf16 copy of Wan2.2-T2V-A14B-Diffusers (see gen_videos/tools/convert_wan22_bf16.py).
# CPU partition; streaming conversion needs only one 5 GB shard in memory, the reload check needs ~30 GB.
#   cd ~/phyRubric && sbatch gen_videos/slurm/convert_wan22_bf16.sbatch
#SBATCH --account=bilw-delta-cpu
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64g
#SBATCH --time=02:00:00
#SBATCH --job-name=wan22_bf16
#SBATCH --output=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.out
#SBATCH --error=/u/hchen56/phyRubric/gen_videos/logs/%x_%j.err
set -euo pipefail
echo "job $SLURM_JOB_ID on $(hostname) at $(date)"
MODELS="/work/nvme/bilw/hchen56/models"
module reset
source ~/miniconda3/etc/profile.d/conda.sh
conda activate ~/conda-envs/t2v
cd "$HOME/phyRubric"
python gen_videos/tools/convert_wan22_bf16.py "$MODELS/Wan2.2-T2V-A14B-Diffusers" "$MODELS/Wan2.2-T2V-A14B-Diffusers-bf16"
du -sh "$MODELS/Wan2.2-T2V-A14B-Diffusers-bf16/"*/ ; echo "done at $(date)"
