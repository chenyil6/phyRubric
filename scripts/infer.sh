#!/bin/bash
# Run the judge (base model or base + LoRA adapter) on data/eval.jsonl and score it against the gold labels.
# Shard the clips over several GPUs by running this once per shard, then the summary once all shards are in.
#
#   CKPT=runs/sft_lora_r16/<run>/checkpoint-900 RUN=judge bash scripts/infer.sh                 # one shard, whole split
#   CKPT=... RUN=judge SHARD=0 SHARDS=4 bash scripts/infer.sh                                     # shard 0 of 4
#   RUN=judge SUMMARY=1 bash scripts/infer.sh                                                     # metrics only
# Variables: CKPT (adapter dir; empty = base model), MODEL (base model, default Qwen/Qwen3-VL-8B-Instruct), RUN, SPLIT (eval | val),
#   SHARD (0), SHARDS (1), BATCH (8), MAXTOK (512), LIMIT, NFRAMES (16), PIX (448), PJ_RUNS (output root, default runs/).
set -euo pipefail
cd "$(dirname "$0")/.."
RUN="${RUN:-judge}"; SPLIT="${SPLIT:-eval}"; SHARD="${SHARD:-0}"; SHARDS="${SHARDS:-1}"; BATCH="${BATCH:-8}"; MAXTOK="${MAXTOK:-512}"
NFRAMES="${NFRAMES:-16}"; PIX="${PIX:-448}"
export FORCE_QWENVL_VIDEO_READER=decord
export FPS=24 FPS_MIN_FRAMES="$NFRAMES" FPS_MAX_FRAMES="$NFRAMES"
export VIDEO_MAX_PIXELS=$((PIX*PIX)) VIDEO_MIN_PIXELS=$((128*128))
export TOKENIZERS_PARALLELISM=false

if [ -z "${SUMMARY:-}" ]; then
  EXTRA=()
  [ -n "${CKPT:-}" ] && EXTRA+=(--adapter "$CKPT")
  [ -n "${MODEL:-}" ] && EXTRA+=(--model "$MODEL")
  [ -n "${LIMIT:-}" ] && EXTRA+=(--limit "$LIMIT")
  python judge/infer.py --run "$RUN" --split "$SPLIT" --shard "$SHARD" --shards "$SHARDS" \
    --batch-size "$BATCH" --max-tokens "$MAXTOK" "${EXTRA[@]}"
fi
if [ -n "${SUMMARY:-}" ] || [ "$SHARDS" = "1" ]; then
  python judge/summary.py --run "$RUN" --split "$SPLIT" --save "${PJ_RUNS:-runs}/$RUN/${SPLIT}_metrics.json"
fi
