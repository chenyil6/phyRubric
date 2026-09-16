#!/usr/bin/env python3
"""Make a bf16 copy of Wan2.2-T2V-A14B-Diffusers.

The published transformer / transformer_2 shards are fp32 (54 GB each). Loading them with
torch_dtype=bf16 converts on the fly, which costs ~23 min and a 121 GB host-RAM peak per job.
This writes bf16 shards once (streaming, one shard in memory at a time), rewrites the index,
copies config.json, and symlinks every other component (text_encoder is already bf16; the
VAE is loaded in fp32 on purpose). Then it reloads the converted transformer and checks a few
tensors against the originals.

    python gen_videos/tools/convert_wan22_bf16.py SRC_DIR DST_DIR
"""
import json, os, sys, time
from pathlib import Path

import torch
from safetensors import safe_open
from safetensors.torch import save_file

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
dst.mkdir(parents=True, exist_ok=True)
CONVERT = ("transformer", "transformer_2")

for item in sorted(os.listdir(src)):
    if item in CONVERT or item.startswith("."):
        continue
    link = dst / item
    if not link.exists():
        os.symlink(src / item, link)
        print(f"link  {item} -> {src / item}")

for sub in CONVERT:
    (dst / sub).mkdir(exist_ok=True)
    (dst / sub / "config.json").write_bytes((src / sub / "config.json").read_bytes())
    index = json.loads((src / sub / "diffusion_pytorch_model.safetensors.index.json").read_text())
    total = 0
    for shard in sorted(set(index["weight_map"].values())):
        t0 = time.time()
        out = dst / sub / shard
        if out.exists() and out.stat().st_size > 0:
            print(f"skip  {sub}/{shard} (exists)"); 
            with safe_open(out, "pt") as f:
                total += sum(f.get_slice(k).get_shape() and torch.tensor(f.get_slice(k).get_shape()).prod().item() * 2 for k in f.keys())
            continue
        tensors = {}
        with safe_open(src / sub / shard, "pt") as f:
            for k in f.keys():
                t = f.get_tensor(k)
                tensors[k] = t.to(torch.bfloat16) if t.dtype == torch.float32 else t
        save_file(tensors, str(out) + ".tmp", metadata={"format": "pt"})
        os.replace(str(out) + ".tmp", out)
        total += sum(t.numel() * t.element_size() for t in tensors.values())
        print(f"wrote {sub}/{shard}: {len(tensors)} tensors in {time.time() - t0:.0f}s", flush=True)
        del tensors
    index["metadata"] = {"total_size": total}
    (dst / sub / "diffusion_pytorch_model.safetensors.index.json").write_text(json.dumps(index, indent=2))
    print(f"index {sub}: total_size {total / 1e9:.1f} GB", flush=True)

# verification: reload through diffusers and compare a few tensors with the fp32 originals
from diffusers import WanTransformer3DModel  # noqa: E402
import resource  # noqa: E402
t0 = time.time()
m = WanTransformer3DModel.from_pretrained(dst, subfolder="transformer", torch_dtype=torch.bfloat16)
print(f"reload transformer (bf16) in {time.time() - t0:.0f}s; params {sum(p.numel() for p in m.parameters()) / 1e9:.2f}B; "
      f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB", flush=True)
sd = m.state_dict()
index = json.loads((src / "transformer/diffusion_pytorch_model.safetensors.index.json").read_text())
checked = 0
for k in list(sd)[:3] + list(sd)[-3:]:
    with safe_open(src / "transformer" / index["weight_map"][k], "pt") as f:
        ref = f.get_tensor(k)
    err = (sd[k].float() - ref.float()).abs().max().item()
    assert err <= ref.abs().max().item() * 2 ** -7 + 1e-6, (k, err)
    checked += 1
print(f"verified {checked} tensors within bf16 rounding; DONE", flush=True)
