#!/bin/bash
# Official VideoScore-v1.1 / VideoScore2 raters (TIGER-Lab) on the eval clips, then metrics against the gold labels.
# Checkpoints VideoScore-v1.1 and VideoScore2 under $PJ_MODELS; videoscore1 needs the Mantis package, videoscore2 qwen-vl-utils.
#
#   MODEL=videoscore2 bash scripts/baseline_videoscore.sh
#   MODEL=videoscore1 SHARD=0 SHARDS=4 bash scripts/baseline_videoscore.sh
#   MODEL=videoscore2 SUMMARY=1 bash scripts/baseline_videoscore.sh
# Variables: MODEL (videoscore1 | videoscore2), SHARD, SHARDS, IDS, TAGS, LIMIT, DTYPE (videoscore2: fp32 | bf16).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${MODEL:?set MODEL=videoscore1|videoscore2}"
export TOKENIZERS_PARALLELISM=false
if [ -z "${SUMMARY:-}" ]; then
  EXTRA=()
  [ -n "${IDS:-}" ] && EXTRA+=(--ids $IDS)
  [ -n "${LIMIT:-}" ] && EXTRA+=(--limit "$LIMIT")
  [ -n "${TAGS:-}" ] && EXTRA+=(--tags $TAGS)
  [ -n "${DTYPE:-}" ] && EXTRA+=(--dtype "$DTYPE")
  python baselines/videoscore_official.py --model "$MODEL" --shard "${SHARD:-0}/${SHARDS:-1}" "${EXTRA[@]}"
fi
if [ -n "${SUMMARY:-}" ] || [ "${SHARDS:-1}" = "1" ]; then
  python baselines/videophy_official_summary.py --model "$MODEL" --save "${PJ_RUNS:-runs}/baselines/${MODEL}_metrics.json"
fi
