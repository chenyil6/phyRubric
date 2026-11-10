#!/bin/bash
# Gemini as a zero-shot judge on Vertex AI, same prompt as the local judges (data/system_prompt.txt), ~16 frames per clip (3 fps).
# Needs GCP_PROJECT and GOOGLE_APPLICATION_CREDENTIALS (or gcloud application-default login).
#
#   MODEL=gemini-4-argon bash scripts/baseline_gemini.sh                 # greedy scores
#   MODEL=gemini-4-argon PROBS=1 bash scripts/baseline_gemini.sh         # also a verbalised 1-5 distribution (soft score)
# Variables: MODEL, THINKING (LOW | MEDIUM | HIGH; empty = thinking off), PROBS, LIMIT, WORKERS (4).
set -euo pipefail
cd "$(dirname "$0")/.."
EXTRA=()
[ -n "${THINKING:-}" ] && EXTRA+=(--thinking-level "$THINKING")
[ "${PROBS:-0}" = "1" ] && EXTRA+=(--probs)
[ -n "${LIMIT:-}" ] && EXTRA+=(--limit "$LIMIT")
python baselines/gemini_judge.py --model "${MODEL:?set MODEL=<vertex model id>}" --workers "${WORKERS:-4}" "${EXTRA[@]}"
