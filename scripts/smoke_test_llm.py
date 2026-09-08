#!/usr/bin/env python
"""Verify the endpoint, image input, caching and JSON mode before building on it.

    export PJUDGE_API_KEY=...            # and set llm.base_url in the yaml
    python scripts/smoke_test_llm.py --config configs/default.yaml

Prints one line per check plus the token/frame tally. Run it again to confirm
the second pass is served entirely from cache (cache_hits == calls).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pjudge.backends import LLMConfig, LLMClient, user_message  # noqa: E402


def synthetic_frame() -> np.ndarray:
    """A red disc on grey -- unambiguous enough that a wrong answer means the
    image never reached the model."""
    img = np.full((360, 640, 3), 128, dtype=np.uint8)
    yy, xx = np.mgrid[:360, :640]
    disc = (xx - 200) ** 2 + (yy - 180) ** 2 < 60**2
    img[disc] = (0, 0, 220)  # BGR
    return img


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--role", default="inspection")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    client = LLMClient(LLMConfig.from_dict(cfg["llm"], args.role), role=args.role)
    print(f"model: {client.cfg.model}  endpoint: {client.cfg.base_url}")

    r = client.ask("Reply with exactly: ok")
    print(f"[text] {r.text.strip()[:40]!r} cached={r.cached}")

    r = client.ask(
        "What shape and colour is the object? Answer in a few words.",
        images=[synthetic_frame()],
    )
    print(f"[vision] {r.text.strip()[:80]!r}")
    lowered = r.text.lower()
    if "red" not in lowered or not any(
        w in lowered for w in ("circle", "disc", "disk", "round", "sphere", "ball")
    ):
        print("  WARNING: expected a red circle -- check that images are accepted")

    r = client.ask(
        'Return JSON: {"n": 2, "unit": "seconds"}', json_mode=True
    )
    print(f"[json] {r.json()}")

    r2 = client.ask("Reply with exactly: ok")
    print(f"[cache] second identical call cached={r2.cached}")

    if client._drop_temperature or client._drop_seed:  # noqa: SLF001 - diagnostic
        print(
            "  note: endpoint rejected "
            + ", ".join(
                n
                for n, d in (("temperature", client._drop_temperature), ("seed", client._drop_seed))
                if d
            )
            + " -- reruns rely on the cache for determinism"
        )
    print(f"usage: {client.usage.as_dict()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
