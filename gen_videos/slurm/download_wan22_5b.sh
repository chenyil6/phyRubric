#!/bin/bash
# Download Wan2.2-TI2V-5B (Diffusers layout, 34 GB; text-or-image-to-video, used here as a text-only
# held-out generator for the eval split) to /work/nvme.
export HF_HOME=/work/hdd/bilw/hchen56/hf
MODELS=/work/nvme/bilw/hchen56/models
NAME=Wan2.2-TI2V-5B-Diffusers
source ~/miniconda3/etc/profile.d/conda.sh; conda activate ~/conda-envs/t2v
echo "== $(date) downloading Wan-AI/$NAME -> $MODELS/$NAME"
huggingface-cli download "Wan-AI/$NAME" --local-dir "$MODELS/$NAME" > "$MODELS/$NAME.download.log" 2>&1
echo "== $(date) exit $?  size $(du -sh "$MODELS/$NAME" | cut -f1)"; ls "$MODELS/$NAME"
