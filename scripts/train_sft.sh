#!/bin/bash
# LoRA-SFT of Qwen3-VL-8B-Instruct into the PhyRubric judge (ms-swift). One GPU.
# Input: data/sft_train.jsonl / data/sft_val.jsonl (caption + 16 uniform frames -> {"sa_score","pc_assessable","pc_score","reason"}).
#
#   MODEL=/path/to/Qwen3-VL-8B-Instruct OUT=runs/sft_lora_r16 bash scripts/train_sft.sh
#   RESUME=1 ... bash scripts/train_sft.sh          # continue from the latest checkpoint in $OUT
# Variables: MODEL (HF id or local dir), OUT, EPOCHS (2), LR (1e-4), RANK (16), GA (8), MAXLEN (4096), NFRAMES (16), PIX (448),
#   MAX_STEPS (smoke test), WORKERS (2).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${MODEL:-Qwen/Qwen3-VL-8B-Instruct}"
OUT="${OUT:-runs/sft_lora_r16}"
TRAIN="${TRAIN:-data/sft_train.jsonl}"; VAL="${VAL:-data/sft_val.jsonl}"
EPOCHS="${EPOCHS:-2}"; LR="${LR:-1e-4}"; RANK="${RANK:-16}"; GA="${GA:-8}"; MAXLEN="${MAXLEN:-4096}"; WORKERS="${WORKERS:-2}"
NFRAMES="${NFRAMES:-16}"; PIX="${PIX:-448}"

# qwen_vl_utils frame sampling: FPS=24 with FPS_MAX_FRAMES=16 takes exactly 16 evenly spaced frames of a 5-6 s clip;
# VIDEO_MAX_PIXELS caps each frame at PIX x PIX (about 1.6k video tokens per clip).
export FORCE_QWENVL_VIDEO_READER=decord
export FPS=24 FPS_MIN_FRAMES="$NFRAMES" FPS_MAX_FRAMES="$NFRAMES"
export VIDEO_MAX_PIXELS=$((PIX*PIX)) VIDEO_MIN_PIXELS=$((128*128))
export TOKENIZERS_PARALLELISM=false
mkdir -p "$OUT"

EXTRA=()
[ -n "${MAX_STEPS:-}" ] && EXTRA+=(--max_steps "$MAX_STEPS")
if [ -n "${RESUME:-}" ]; then
  CKPT=$(ls -dt "$OUT"/*/checkpoint-* 2>/dev/null | head -1)
  [ -n "$CKPT" ] && EXTRA+=(--resume_from_checkpoint "$CKPT") && echo "resuming from $CKPT"
fi

swift sft \
  --model "$MODEL" --model_type qwen3_vl --tuner_type lora \
  --lora_rank "$RANK" --lora_alpha $((RANK*2)) --target_modules all-linear \
  --freeze_vit true --freeze_aligner true \
  --dataset "$TRAIN" --val_dataset "$VAL" --split_dataset_ratio 0 \
  --num_train_epochs "$EPOCHS" --per_device_train_batch_size 1 --per_device_eval_batch_size 1 \
  --gradient_accumulation_steps "$GA" --learning_rate "$LR" --warmup_ratio 0.03 \
  --max_length "$MAXLEN" --truncation_strategy delete \
  --torch_dtype bfloat16 --attn_impl sdpa --gradient_checkpointing true \
  --lazy_tokenize true --dataloader_num_workers "$WORKERS" --dataloader_pin_memory false \
  --save_steps 100 --eval_steps 100 --logging_steps 5 --save_total_limit 3 \
  --report_to tensorboard --seed 42 \
  --output_dir "$OUT" "${EXTRA[@]}"
