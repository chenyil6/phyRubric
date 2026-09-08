#!/bin/bash
# Download Wan2.2-T2V-A14B (Diffusers layout) and CogVideoX1.5-5B to /work/nvme.
export HF_HOME=/work/hdd/bilw/hchen56/hf
MODELS=/work/nvme/bilw/hchen56/models
source ~/miniconda3/etc/profile.d/conda.sh; conda activate ~/conda-envs/t2v
for repo in Wan-AI/Wan2.2-T2V-A14B-Diffusers zai-org/CogVideoX1.5-5B; do
  name=${repo#*/}
  echo "== $(date) downloading $repo -> $MODELS/$name"
  hf download "$repo" --local-dir "$MODELS/$name" > "$MODELS/$name.download.log" 2>&1
  echo "== $(date) $name exit $?  size $(du -sh "$MODELS/$name" | cut -f1)"
done
echo "== $(date) ALL DOWNLOADS DONE"; du -sh $MODELS/*/ ; df -h /work/nvme | tail -1
