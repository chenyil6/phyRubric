#!/bin/bash
# Download LTX-Video 2B 0.9.8 distilled to /work/nvme: the single-file checkpoint (transformer + VAE,
# 6.3 GB), the 0.9.8 spatial upscaler for the official two-pass pipeline (0.5 GB), and the Diffusers
# layout pieces (T5-XXL text encoder, tokenizer, scheduler, model_index) from the same repo (~18 GB).
export HF_HOME=/work/hdd/bilw/hchen56/hf
MODELS=/work/nvme/bilw/hchen56/models
NAME=LTX-Video-2B-0.9.8-distilled
source ~/miniconda3/etc/profile.d/conda.sh; conda activate ~/conda-envs/t2v
echo "== $(date) downloading Lightricks/LTX-Video -> $MODELS/$NAME"
huggingface-cli download Lightricks/LTX-Video --local-dir "$MODELS/$NAME" \
  --include "ltxv-2b-0.9.8-distilled.safetensors" "ltxv-spatial-upscaler-0.9.8.safetensors" \
            "model_index.json" "scheduler/*" "text_encoder/*" "tokenizer/*" \
  > "$MODELS/$NAME.download.log" 2>&1
echo "== $(date) exit $?  size $(du -sh "$MODELS/$NAME" | cut -f1)"; ls -la "$MODELS/$NAME"
