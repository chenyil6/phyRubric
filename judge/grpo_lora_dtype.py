"""Keep LoRA weights in the model dtype (bf16) when the GRPO job loads an adapter (ms-swift external plugin).

peft's load_adapter(..., autocast_adapter_dtype=True) upcasts bf16/fp16 LoRA weights to fp32. The GRPO trainer
casts them back to bf16 before the first optimizer step (every checkpoint it writes holds a bf16 adapter and bf16
Adam moments), so a fresh start is unaffected. A resume is not: transformers' _load_from_checkpoint calls
load_adapter again, the optimizer is built on the fp32 params, optimizer.pt is cast to fp32 on load, and after the
trainer's downcast fused AdamW sees bf16 params with fp32 moments:
    RuntimeError: Mixed-precision fused AdamW requires float32 params, got BFloat16
(jobs 3477466 / 3484389, 2026-10-30). Disabling the upcast keeps the weights bf16 at every stage, which is the
regime the fresh run trained in, so the saved moments load unchanged.

Use: --external_plugins judge/grpo_rewards.py judge/grpo_lora_dtype.py
"""
import swift.tuners  # noqa: F401  ms-swift installs its own peft patches on import; ours must come after them
from peft.tuners.lora import LoraModel
from peft.tuners.tuners_utils import BaseTuner


def _cast_adapter_dtype_no_upcast(self, adapter_name: str, autocast_adapter_dtype: bool = True):
    return BaseTuner._cast_adapter_dtype(self, adapter_name, autocast_adapter_dtype=False)


LoraModel._cast_adapter_dtype = _cast_adapter_dtype_no_upcast
