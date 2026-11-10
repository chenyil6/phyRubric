#!/bin/bash
# Zero-shot Qwen3-VL-235B-A22B-Instruct-FP8 as a judge through vLLM (TP=4), then metrics against the gold labels.
#
#   MODEL=Qwen/Qwen3-VL-235B-A22B-Instruct-FP8 TP=4 RUN=base235b bash scripts/baseline_qwen235b.sh
# Variables: MODEL, TP (4), RUN, SPLIT (eval), MAXTOK (512), NFRAMES (16), PIX (448), BATCH (16), LIMIT, PJ_RUNS (runs/).
set -euo pipefail
cd "$(dirname "$0")/.."
EXTRA=()
[ -n "${LIMIT:-}" ] && EXTRA+=(--limit "$LIMIT")
python baselines/qwen3vl_235b.py --model "${MODEL:-Qwen/Qwen3-VL-235B-A22B-Instruct-FP8}" --tp "${TP:-4}" \
  --run "${RUN:-base235b}" --split "${SPLIT:-eval}" --suffix "" --max-tokens "${MAXTOK:-512}" \
  --nframes "${NFRAMES:-16}" --pix "${PIX:-448}" --batch-size "${BATCH:-16}" "${EXTRA[@]}"
python judge/summary.py --run "${RUN:-base235b}" --split "${SPLIT:-eval}" --save "${PJ_RUNS:-runs}/${RUN:-base235b}/${SPLIT:-eval}_metrics.json"
