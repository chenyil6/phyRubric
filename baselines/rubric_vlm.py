#!/usr/bin/env python3
"""Baseline 2: one fixed VLM pass executes the caption-specific rubric.

The model receives exactly one uniformly sampled view of the video.  It marks
every SA item pass/fail and every PC item pass/fail/not_shown; Python then
applies the shared policy deterministically.  There is no replanning, zooming,
or second observation, so comparison with an active evaluator isolates the
value of adaptive evidence gathering.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
import threading
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from eval.dataset import VideoPhy2Dataset  # noqa: E402
from eval.metrics import summarise  # noqa: E402
from eval.runner import COST_FIELDS, join_with_gold, run_batch  # noqa: E402
from pjudge.backends.llm import LLMClient, LLMConfig, parse_json  # noqa: E402
from pjudge.perception.frames import FrameServer  # noqa: E402

SYSTEM = """You are a strict evaluator of generated-video semantics and physical commonsense.
Judge only visible evidence. Apply every supplied rubric item independently. Do not infer an
unseen force, contact, or event. Return one JSON object and no prose outside it."""

TASK = """Prompt used to generate the video:
{caption}

The following {n_frames} frames are sampled uniformly from a {duration:.2f}-second video,
in temporal order, at timestamps: {timestamps}

Dataset-wide policy:
{policy}

Caption-specific rubric:
{rubric}

For every SA item return pass or fail. For every PC item return pass, fail, or not_shown.
Use not_shown when a stated precondition does not occur or the required moment is not visible.
Also state whether the clip is a recognisable attempt at the caption. Evidence must describe
only what is visible in the supplied frames.

JSON schema:
{{
  "recognisable_attempt": true,
  "sa": [{{"id": "S1", "status": "pass|fail", "evidence": "short visible evidence"}}],
  "pc": [{{"id": "P1", "status": "pass|fail|not_shown", "evidence": "short visible evidence"}}],
  "confidence": 0.0
}}"""

SEVERITY_CAP = {"fatal": 1, "core": 2, "major": 3, "minor": 4}


def load_env(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


class RubricIndex:
    def __init__(self, dataset: str = "videophy2"):
        prompts = json.loads((ROOT / "prompts" / f"{dataset}.json").read_text())
        self.by_caption: dict[str, dict[str, Any]] = {}
        for entry in prompts:
            rubric_path = ROOT / "rubrics" / dataset / f"caption_{entry['id']}.json"
            rubric = json.loads(rubric_path.read_text())
            for caption in [entry["caption"], *entry.get("aliases", [])]:
                previous = self.by_caption.setdefault(caption, rubric)
                if previous["id"] != rubric["id"]:
                    raise ValueError(f"caption alias maps to two rubrics: {caption!r}")
        self.policy = json.loads((ROOT / "rubrics" / dataset / "_policy.json").read_text())

    def get(self, caption: str) -> dict[str, Any]:
        try:
            return self.by_caption[caption]
        except KeyError:
            raise KeyError(f"no rubric or alias for caption {caption!r}") from None


def _decision_map(raw: Any, allowed: set[str]) -> dict[str, dict[str, str]]:
    if not isinstance(raw, list):
        raise ValueError("decisions must be a list")
    out: dict[str, dict[str, str]] = {}
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError("each decision must be an object")
        item_id = str(item.get("id", "")).strip()
        status = str(item.get("status", "")).strip().lower()
        if not item_id or status not in allowed or item_id in out:
            raise ValueError(f"invalid or duplicate decision: {item!r}")
        out[item_id] = {"status": status, "evidence": str(item.get("evidence", "")).strip()}
    return out


def _as_bool(value: Any, default: bool = True) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"true", "yes", "1"}:
            return True
        if text in {"false", "no", "0"}:
            return False
    return default


def score_sa(rubric: dict[str, Any], decisions: dict[str, dict[str, str]], recognisable: bool) -> int:
    expected = [item["id"] for item in rubric["sa"]]
    if set(decisions) != set(expected):
        raise ValueError(f"SA ids differ: expected {expected}, got {sorted(decisions)}")
    failed = [item for item in rubric["sa"] if decisions[item["id"]]["status"] == "fail"]
    if not failed:
        return 5
    core_failures = sum(item["weight"] == "core" for item in failed)
    if core_failures == 0:
        return 4
    if core_failures == 1:
        return 3
    return 2 if recognisable else 1


def score_pc(rubric: dict[str, Any], decisions: dict[str, dict[str, str]]) -> int:
    expected = [item["id"] for item in rubric["pc"]]
    if set(decisions) != set(expected):
        raise ValueError(f"PC ids differ: expected {expected}, got {sorted(decisions)}")
    failed = [item for item in rubric["pc"] if decisions[item["id"]]["status"] == "fail"]
    if not failed:
        return 5
    score = min(SEVERITY_CAP[item["severity"]] for item in failed)
    heavy = sum(item["severity"] in {"fatal", "core", "major"} for item in failed)
    return max(1, score - max(0, heavy - 1))


class RubricVLM:
    def __init__(
        self,
        client: LLMClient,
        rubric_index: RubricIndex,
        n_frames: int,
        long_side: int,
        include_note: bool,
    ):
        self.client = client
        self.index = rubric_index
        self.n_frames = n_frames
        self.long_side = long_side
        self.include_note = include_note

    def judge(self, sample) -> dict[str, Any]:
        rubric = copy.deepcopy(self.index.get(sample.caption))
        if not self.include_note:
            rubric.pop("note", None)
        server = FrameServer(sample.video_path)
        frames = server.sample(n_frames=self.n_frames, long_side=self.long_side)
        prompt = TASK.format(
            caption=sample.caption,
            n_frames=len(frames),
            duration=server.duration,
            timestamps=", ".join(f"{t:.2f}s" for t, _ in frames),
            policy=json.dumps(self.index.policy, ensure_ascii=False),
            rubric=json.dumps(rubric, ensure_ascii=False),
        )
        response = self.client.ask(
            prompt,
            system=SYSTEM,
            images=[image for _, image in frames],
            json_mode=True,
        )
        try:
            data = parse_json(response.text)
            sa = _decision_map(data.get("sa"), {"pass", "fail"})
            pc = _decision_map(data.get("pc"), {"pass", "fail", "not_shown"})
            recognisable = _as_bool(data.get("recognisable_attempt"), default=True)
            confidence = min(1.0, max(0.0, float(data.get("confidence", 0.5))))
            sa_score = score_sa(rubric, sa, recognisable)
            pc_score = score_pc(rubric, pc)
            error = ""
            imputed = False
        except Exception as exc:  # one-pass baseline does not ask the model again
            sa, pc = {}, {}
            sa_score = pc_score = 3
            confidence = 0.0
            error = f"unusable rubric reply; imputed 3: {type(exc).__name__}: {exc}"
            imputed = True
        return {
            "video_id": sample.video_id,
            "rubric_id": rubric["id"],
            "sa_score": sa_score,
            "pc_score": pc_score,
            "confidence": confidence,
            "score_imputed": imputed,
            "sa_decisions": sa,
            "pc_decisions": pc,
            "raw_text": response.text,
            "frames": server.frames_served,
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "llm_calls": 1,
            "cache_hits": int(response.cached),
            "error": error,
        }


class PerThreadJudge:
    def __init__(self, factory):
        self.factory = factory
        self.local = threading.local()

    def __call__(self, sample):
        judge = getattr(self.local, "judge", None)
        if judge is None:
            judge = self.factory()
            self.local.judge = judge
        return judge.judge(sample)


def select_dataset(cfg: dict, split: str, n: int, seed: int, hard_only: bool):
    dataset = VideoPhy2Dataset.from_config(cfg, split=split).filter(
        has_video=True, hard=True if hard_only else None
    )
    return dataset.stratified_subset(n, seed=seed) if n else dataset


def write_summary(out_path: Path, dataset, run_stats: dict, seed: int) -> Path:
    frame = join_with_gold(out_path, dataset)
    usable = frame[frame["pred"].notna()].copy()
    report = summarise(
        list(usable["pred"]),
        list(usable["pc"]),
        list(usable["confidence"]),
        usable[list(COST_FIELDS)].to_dict("records"),
        seed=seed,
    )
    report["n_rows_joined"] = int(len(frame))
    report["n_without_score"] = int(len(frame) - len(usable))
    if len(usable):
        delta = (usable["pred"] - usable["pc"]).abs()
        report["exact_accuracy"] = round(float((delta == 0).mean()), 6)
        report["within_one_accuracy"] = round(float((delta <= 1).mean()), 6)
    summary_path = out_path.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps({"baseline": "rubric_vlm", "run": run_stats, "metrics": report}, indent=2)
    )
    return summary_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(ROOT / "configs/default.yaml"))
    parser.add_argument("--split", default="test")
    parser.add_argument("--n", type=int, default=200, help="0 means the full split")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--model")
    parser.add_argument("--n-frames", type=int, default=16)
    parser.add_argument("--long-side", type=int, default=768)
    parser.add_argument("--include-note", action="store_true")
    parser.add_argument("--hard-only", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    dataset = select_dataset(cfg, args.split, args.n, args.seed, args.hard_only)
    rubric_index = RubricIndex()
    missing = [sample.caption for sample in dataset if sample.caption not in rubric_index.by_caption]
    if missing:
        raise RuntimeError(f"{len(missing)} selected rows have no rubric; first={missing[0]!r}")
    model = args.model or cfg["llm"]["default_model"]
    print(
        f"selected {len(dataset)} VideoPhy-2 videos; all captions matched; "
        f"model={model}; frames={args.n_frames}; include_note={args.include_note}"
    )
    if args.check_only:
        return 0

    load_env()

    def factory():
        llm_cfg = copy.deepcopy(cfg["llm"])
        llm_cfg["default_model"] = model
        client = LLMClient(LLMConfig.from_dict(llm_cfg, "observer"), role="rubric_vlm")
        return RubricVLM(client, rubric_index, args.n_frames, args.long_side, args.include_note)

    safe_model = re.sub(r"[^A-Za-z0-9._-]+", "_", model)
    out_path = args.out or ROOT / "results" / f"baseline_rubric_vlm_{safe_model}_n{len(dataset)}_s{args.seed}.jsonl"
    stats = run_batch(
        list(dataset),
        PerThreadJudge(factory),
        out_path,
        workers=args.workers,
        resume=not args.no_resume,
        limit=args.limit,
    )
    summary = write_summary(out_path, dataset, stats.as_dict(), args.seed)
    print(f"results: {out_path}\nsummary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
