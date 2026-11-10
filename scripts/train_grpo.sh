#!/bin/bash
# GRPO (RLVR on the gold labels) on top of the SFT LoRA, ms-swift with an in-process vLLM engine (colocate mode). One GPU.
# G completions per prompt are sampled, scored by judge/grpo_rewards.py (pj_format / pj_sa / pj_pc / pj_assess against
# sa_gold / pc_gold / assess_gold in data/grpo_train.jsonl) and the merged weights are reloaded into vLLM after every step.
#
#   MODEL=/path/to/Qwen3-VL-8B-Instruct START=runs/sft_lora_r16/<run>/checkpoint-900 OUT=runs/grpo bash scripts/train_grpo.sh
#   RESUME=1 ... bash scripts/train_grpo.sh         # continue from the latest checkpoint in $OUT
# Variables: MODEL, START (SFT adapter dir), OUT, G (4), MAXCOMP (512), TEMP (1.0), LR (1e-5), BS (4), GA (8; BS*GA completions
#   per optimizer step), EPOCHS (1), BETA (0 = no KL / reference model), WEIGHTS ("0.5 1 1 0.5"), SAVE_STEPS (25), MAXLEN (4096),
#   VLLM_MEM (0.4), MAX_STEPS, NFRAMES (16), PIX (448).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${MODEL:-Qwen/Qwen3-VL-8B-Instruct}"
START="${START:?set START=<SFT adapter checkpoint dir>}"
OUT="${OUT:-runs/grpo}"
TRAIN="${TRAIN:-data/grpo_train.jsonl}"
G="${G:-4}"; MAXCOMP="${MAXCOMP:-512}"; TEMP="${TEMP:-1.0}"; LR="${LR:-1e-5}"; BS="${BS:-4}"; GA="${GA:-8}"; EPOCHS="${EPOCHS:-1}"
BETA="${BETA:-0}"; WEIGHTS="${WEIGHTS:-0.5 1 1 0.5}"; SAVE_STEPS="${SAVE_STEPS:-25}"; MAXLEN="${MAXLEN:-4096}"; WORKERS="${WORKERS:-2}"
VLLM_MEM="${VLLM_MEM:-0.4}"; NFRAMES="${NFRAMES:-16}"; PIX="${PIX:-448}"

export FORCE_QWENVL_VIDEO_READER=decord
export FPS=24 FPS_MIN_FRAMES="$NFRAMES" FPS_MAX_FRAMES="$NFRAMES"
export VIDEO_MAX_PIXELS=$((PIX*PIX)) VIDEO_MIN_PIXELS=$((128*128))
export TOKENIZERS_PARALLELISM=false
mkdir -p "$OUT"

EXTRA=()
[ -n "${MAX_STEPS:-}" ] && EXTRA+=(--max_steps "$MAX_STEPS")
CKPT=""
if [ -n "${RESUME:-}" ]; then
  CKPT=$(ls -d "$OUT"/*/checkpoint-* 2>/dev/null | awk -F'checkpoint-' '{print $NF" "$0}' | sort -n | tail -1 | awk '{print $2}')
fi
if [ -n "$CKPT" ]; then echo "resuming from $CKPT"; EXTRA+=(--resume_from_checkpoint "$CKPT"); else EXTRA+=(--adapters "$START"); fi
read -r -a WARR <<< "$WEIGHTS"

swift rlhf --rlhf_type grpo \
  --model "$MODEL" --model_type qwen3_vl --tuner_type lora --freeze_vit true --freeze_aligner true \
  --dataset "$TRAIN" --split_dataset_ratio 0 \
  --external_plugins judge/grpo_rewards.py judge/grpo_lora_dtype.py \
  --reward_funcs pj_format pj_sa pj_pc pj_assess --reward_weights "${WARR[@]}" \
  --use_vllm true --vllm_mode colocate --vllm_gpu_memory_utilization "$VLLM_MEM" --vllm_max_model_len "$MAXLEN" --sleep_level 1 \
  --vllm_limit_mm_per_prompt '{"video": 1, "image": 0}' --vllm_enable_prefix_caching true \
  --num_generations "$G" --max_completion_length "$MAXCOMP" --temperature "$TEMP" --top_p 1.0 \
  --beta "$BETA" --epsilon 0.2 \
  --num_train_epochs "$EPOCHS" --per_device_train_batch_size "$BS" --gradient_accumulation_steps "$GA" \
  --learning_rate "$LR" --warmup_ratio 0.03 \
  --max_length "$MAXLEN" --truncation_strategy delete \
  --torch_dtype bfloat16 --attn_impl sdpa --gradient_checkpointing true \
  --lazy_tokenize true --dataloader_num_workers "$WORKERS" --dataloader_pin_memory false \
  --save_steps "$SAVE_STEPS" --save_total_limit 2 --logging_steps 1 --log_completions true \
  --report_to tensorboard --seed 42 \
  --output_dir "$OUT" "${EXTRA[@]}"
