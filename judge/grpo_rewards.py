"""Reward functions for GRPO on PhyRubric-Judge (ms-swift external plugin; loaded with --external_plugins).

Verifiable rewards against the blind annotation (dataset columns sa_gold / pc_gold / assess_gold, built by
judge/build_grpo.py). One function per signal so ms-swift logs each separately; combine with --reward_weights.

  pj_format  1 if the completion has the expected shape, else 0.
             plain (PJ_THINK unset): the text starts with one JSON object holding integer sa_score / pc_score in 1-5
               and boolean pc_assessable (the reason may follow inside the object, as in the SFT target).
             think (PJ_THINK=1): exactly one <think>...</think> block first, then that JSON object, nothing else.
  pj_sa      1 - |sa_pred - sa_gold| / 4           (0 if the format is invalid)
  pj_pc      1 - |pc_pred - pc_gold| / 4           (0 if the format is invalid)
  pj_assess  1 if pc_assessable matches the gold flag (0 if invalid)

Use: --external_plugins judge/grpo_rewards.py --reward_funcs pj_format pj_sa pj_pc pj_assess --reward_weights 0.5 1 1 0.5
"""
from __future__ import annotations
import json
import os
import re
from typing import List, Optional

from swift.rewards import ORM, orms

THINK = os.environ.get("PJ_THINK") == "1"
THINK_RE = re.compile(r"^\s*<think>(.*?)</think>\s*(\{.*)$", re.S)
KEYS = ("sa_score", "pc_assessable", "pc_score")


def _first_json(text: str) -> Optional[dict]:
    """The JSON object at the start of text (raw_decode tolerates trailing text, e.g. an EOS-truncated tail)."""
    text = text.lstrip()
    if not text.startswith("{"):
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(text)
    except json.JSONDecodeError:
        # truncated reason: salvage the three score fields with regexes, same as judge/infer.py
        out = {}
        for k, pat in (("sa_score", r'"sa_score"\s*:\s*(\d)'), ("pc_score", r'"pc_score"\s*:\s*(\d)'),
                       ("pc_assessable", r'"pc_assessable"\s*:\s*(true|false)')):
            m = re.search(pat, text)
            if not m:
                return None
            out[k] = int(m.group(1)) if k != "pc_assessable" else m.group(1) == "true"
        return out
    return obj if isinstance(obj, dict) else None


def parse(completion: str) -> Optional[dict]:
    """{"sa": int, "pc": int, "assess": bool} if the completion is well-formed for the active variant, else None."""
    if THINK:
        m = THINK_RE.match(completion)
        if not m or "<think>" in m.group(1) or "<think>" in m.group(2) or "</think>" in m.group(2):
            return None
        if not m.group(1).strip():
            return None
        body = m.group(2)
        obj = _first_json(body)
        if obj is None:
            return None
        # nothing after the JSON object
        try:
            _, end = json.JSONDecoder().raw_decode(body.lstrip())
            if body.lstrip()[end:].strip():
                return None
        except json.JSONDecodeError:
            return None
    else:
        obj = _first_json(completion)
        if obj is None:
            return None
    sa, pc, ass = obj.get("sa_score"), obj.get("pc_score"), obj.get("pc_assessable")
    if not (isinstance(sa, int) and isinstance(pc, int) and isinstance(ass, bool)) or isinstance(sa, bool) or isinstance(pc, bool):
        return None
    if not (1 <= sa <= 5 and 1 <= pc <= 5):
        return None
    return {"sa": sa, "pc": pc, "assess": ass}


class PJFormat(ORM):
    def __call__(self, completions: List[str], **kwargs) -> List[float]:
        return [1.0 if parse(c) is not None else 0.0 for c in completions]


class PJSa(ORM):
    def __call__(self, completions: List[str], sa_gold: List[int], **kwargs) -> List[float]:
        out = []
        for c, g in zip(completions, sa_gold):
            p = parse(c)
            out.append(0.0 if p is None else 1.0 - abs(p["sa"] - int(g)) / 4.0)
        return out


class PJPc(ORM):
    def __call__(self, completions: List[str], pc_gold: List[int], **kwargs) -> List[float]:
        out = []
        for c, g in zip(completions, pc_gold):
            p = parse(c)
            out.append(0.0 if p is None else 1.0 - abs(p["pc"] - int(g)) / 4.0)
        return out


class PJAssess(ORM):
    def __call__(self, completions: List[str], assess_gold: List[bool], **kwargs) -> List[float]:
        out = []
        for c, g in zip(completions, assess_gold):
            p = parse(c)
            out.append(0.0 if p is None else float(p["assess"] == bool(g)))
        return out


orms["pj_format"] = PJFormat
orms["pj_sa"] = PJSa
orms["pj_pc"] = PJPc
orms["pj_assess"] = PJAssess
