#!/bin/bash
# Download Cosmos-Predict2.5-2B in Diffusers layout (official branch diffusers/base/post-trained; the
# post-trained checkpoint is the one that supports text2world) to /work/nvme. Gated repo: needs the NVIDIA
# license accepted on HF and a token in $HF_HOME/token. Held-out generator, eval split only.
export HF_HOME=/work/hdd/bilw/hchen56/hf
MODELS=/work/nvme/bilw/hchen56/models
NAME=Cosmos-Predict2.5-2B-Diffusers
source ~/miniconda3/etc/profile.d/conda.sh; conda activate ~/conda-envs/t2v
echo "== $(date) downloading nvidia/Cosmos-Predict2.5-2B@diffusers/base/post-trained -> $MODELS/$NAME"
huggingface-cli download nvidia/Cosmos-Predict2.5-2B --revision diffusers/base/post-trained --local-dir "$MODELS/$NAME" > "$MODELS/$NAME.download.log" 2>&1
echo "== $(date) exit $?  size $(du -sh "$MODELS/$NAME" | cut -f1)"; ls "$MODELS/$NAME"
