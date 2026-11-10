#!/bin/bash
# Official VideoPhy-1 (VideoCon-Physics) / VideoPhy-2 (AutoEval) raters on the eval clips, then metrics against the gold labels.
# Needs the official repo (github.com/Hritikbansal/videophy) at $VIDEOPHY_CODE and the released checkpoints
# videocon_physics / videophy_2_auto under $PJ_MODELS. 7B mPLUG-Owl, bf16, 32 frames, SA + PC prompts per clip.
#
#   MODEL=videophy2 bash scripts/baseline_videophy.sh                      # whole split on one GPU
#   MODEL=videophy1 SHARD=0 SHARDS=8 bash scripts/baseline_videophy.sh     # one shard; run the summary after all shards
#   MODEL=videophy2 SUMMARY=1 bash scripts/baseline_videophy.sh
# Variables: MODEL (videophy1 | videophy2), SHARD, SHARDS, TASKS ("sa pc"), IDS, TAGS, LIMIT, SOFT (1 = digit-probability soft score).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${MODEL:?set MODEL=videophy1|videophy2}"
export TOKENIZERS_PARALLELISM=false
if [ -z "${SUMMARY:-}" ]; then
  EXTRA=()
  [ -n "${IDS:-}" ] && EXTRA+=(--ids $IDS)
  [ -n "${LIMIT:-}" ] && EXTRA+=(--limit "$LIMIT")
  [ -n "${TAGS:-}" ] && EXTRA+=(--tags $TAGS)
  [ "${SOFT:-0}" = "1" ] && EXTRA+=(--soft)
  python baselines/videophy_official.py --model "$MODEL" --tasks ${TASKS:-sa pc} --shard "${SHARD:-0}/${SHARDS:-1}" "${EXTRA[@]}"
fi
if [ -n "${SUMMARY:-}" ] || [ "${SHARDS:-1}" = "1" ]; then
  python baselines/videophy_official_summary.py --model "$MODEL" --save "${PJ_RUNS:-runs}/baselines/${MODEL}_metrics.json"
fi
