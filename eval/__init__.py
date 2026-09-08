"""Evaluation layer: how good is the judge, measured against human annotations.

Separate from `pjudge` on purpose. `pjudge` answers "is this video physically
plausible"; this package answers "does pjudge agree with people, and at what
cost". Without the second question every prompt change to the judge is a blind
change -- which is exactly what happened before this layer existed: a video
humans scored 5/5 was being scored 2/5 and nothing in the judge could reveal it.
"""

from .baselines import BaselineResult, CaptionOnlyBaseline, SinglePassBaseline, parse_reply
from .dataset import Sample, VideoPhy2Dataset, make_video_id, resolve_path
from .metrics import (
    binary_metrics,
    bootstrap_ci,
    correlations,
    cost_curve,
    open_discovery_match,
    risk_coverage,
    summarise,
)
from .runner import (
    RunStats,
    completed_ids,
    failed_ids,
    join_with_gold,
    load_results,
    results_frame,
    run_batch,
)

__all__ = [
    # dataset
    "Sample",
    "VideoPhy2Dataset",
    "make_video_id",
    "resolve_path",
    # metrics
    "correlations",
    "binary_metrics",
    "risk_coverage",
    "open_discovery_match",
    "cost_curve",
    "bootstrap_ci",
    "summarise",
    # baselines
    "BaselineResult",
    "SinglePassBaseline",
    "CaptionOnlyBaseline",
    "parse_reply",
    # runner
    "RunStats",
    "run_batch",
    "load_results",
    "completed_ids",
    "failed_ids",
    "results_frame",
    "join_with_gold",
]
