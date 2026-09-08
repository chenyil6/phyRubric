#!/bin/bash
# One-time setup on Delta: conda env for T2V generation + CogVideoX-5b weights on /work/nvme.
set -uo pipefail
export HF_HOME=/work/hdd/bilw/hchen56/hf
MODELS=/work/nvme/bilw/hchen56/models
mkdir -p "$HF_HOME" "$MODELS" /work/hdd/bilw/hchen56/phyRubric_outputs
source ~/miniconda3/etc/profile.d/conda.sh
echo "== $(date) creating env"
conda create -y -q -p ~/conda-envs/t2v python=3.11 || exit 1
conda activate ~/conda-envs/t2v
python -m pip install -q --upgrade pip
echo "== $(date) installing torch (cu126 wheels)"
pip install -q torch torchvision --index-url https://download.pytorch.org/whl/cu126 || exit 1
echo "== $(date) installing diffusers stack"
pip install -q -r ~/phyRubric/gen_videos/requirements_cogvideox_5b.txt "huggingface_hub[cli]" || exit 1
python - <<'PY'
import torch, diffusers, transformers
print("torch", torch.__version__, "cuda build", torch.version.cuda, "| diffusers", diffusers.__version__, "| transformers", transformers.__version__)
PY
echo "== $(date) downloading zai-org/CogVideoX-5b -> $MODELS/CogVideoX-5b"
hf download zai-org/CogVideoX-5b --local-dir "$MODELS/CogVideoX-5b" > "$MODELS/CogVideoX-5b.download.log" 2>&1 || huggingface-cli download zai-org/CogVideoX-5b --local-dir "$MODELS/CogVideoX-5b" >> "$MODELS/CogVideoX-5b.download.log" 2>&1
echo "== $(date) download exit $?"; du -sh "$MODELS/CogVideoX-5b"
echo "== $(date) SETUP DONE"
