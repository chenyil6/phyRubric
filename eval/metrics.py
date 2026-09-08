"""The numbers that decide whether the judge is good.

Every prompt change to the judge is a blind change until these exist, so this
module is deliberately the least clever code in the project: pure functions over
sequences, no I/O, no dataset knowledge, no model calls. Anything that can be
recomputed from a results table belongs here; anything that needs a file does
not.

Three things shape the design.

1. A judge that may abstain cannot be compared on correlation alone. Refusing
   the hard cases raises Pearson for free, so every correlation is reported next
   to the coverage it was computed at, and `risk_coverage` measures whether the
   abstentions were the *right* ones -- whether risk on what we kept falls
   faster than coverage does.
2. Degenerate input is normal here, not exceptional. A 20-video pilot can easily
   produce all-abstain, constant-gold or single-class slices, and the harness
   must print a table with a blank cell rather than crash mid-sweep. So every
   metric returns None when it is undefined, and no scipy/sklearn warning is
   ever allowed to escape. The only exception raised is ValueError for a
   pred/gold length mismatch, which is a caller bug, not data.
3. Open-ended discovery needs a pluggable matcher. Half the VideoPhy-2 rows
   carry free-text violations that humans wrote in by hand because the automatic
   rule list missed them; matching our findings against those is the point of
   the whole exercise. The lexical default here is a floor, not the answer -- it
   is the same interface an LLM matcher will implement later.

Results are rounded to `DECIMALS` so that a table, a re-run and a JSON round
trip all agree.
"""

from __future__ import annotations

import math
import warnings
from typing import Any, Callable, Mapping, Sequence

import numpy as np
from scipy import stats
from sklearn.metrics import average_precision_score, roc_auc_score

DECIMALS = 6

# Deliberately tiny: this list exists to stop "the", "is" and "to" from
# inflating Jaccard overlap between unrelated sentences, not to do linguistics.
STOPWORDS = frozenset(
    """
    a an the this that these those it its is are was were be been being am
    do does did done has have had having will would shall should can could may
    might must of to in into on at by for from with without as and or but not
    no nor if then than there their they them he she his her we us our you your
    i me my which who whom whose what when where while about over under out up
    down off again very s t
    """.split()
)


# --------------------------------------------------------------------------
# internals
# --------------------------------------------------------------------------


def _r(value: float | None) -> float | None:
    """Round for reporting; None passes through."""
    if value is None:
        return None
    return round(float(value), DECIMALS)


def _as_number(value: Any) -> float | None:
    """Finite float, or None for anything that cannot serve as a prediction."""
    if value is None:
        return None
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    return f if math.isfinite(f) else None


def _check_lengths(**arrays: Sequence[Any]) -> None:
    lengths = {name: len(seq) for name, seq in arrays.items()}
    if len(set(lengths.values())) > 1:
        raise ValueError(f"length mismatch: {lengths}")


def _scored(pred: Sequence[Any], gold: Sequence[Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Indices and values of the pairs both sides could supply.

    A row is scored only if the prediction is a finite number *and* the gold
    label is. Gold is never dropped from `n_total`: coverage is a fraction of
    every row we were asked about, including the ones we refused.
    """
    idx: list[int] = []
    p_vals: list[float] = []
    g_vals: list[float] = []
    for i, (p, g) in enumerate(zip(pred, gold)):
        pf, gf = _as_number(p), _as_number(g)
        if pf is None or gf is None:
            continue
        idx.append(i)
        p_vals.append(pf)
        g_vals.append(gf)
    return (
        np.asarray(idx, dtype=int),
        np.asarray(p_vals, dtype=float),
        np.asarray(g_vals, dtype=float),
    )


def _quiet(fn: Callable[[], Any]) -> Any:
    """Run `fn` with warnings muted; degenerate input is data, not a bug."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return fn()


def _defined(value: Any) -> float | None:
    """Turn a scipy/sklearn result into a reportable number or None."""
    try:
        f = float(value)
    except (TypeError, ValueError):
        return None
    return f if math.isfinite(f) else None


def _correlatable(x: np.ndarray, y: np.ndarray) -> bool:
    """Rank and moment correlations both need two points and some variation."""
    if x.size < 2:
        return False
    return bool(np.ptp(x) > 0 and np.ptp(y) > 0)


# --------------------------------------------------------------------------
# metric_fn-shaped helpers
# --------------------------------------------------------------------------
# Each takes (pred, gold), skips abstentions and returns None when undefined,
# which is exactly the shape `bootstrap_ci` wants for its first argument.


def pearson(pred: Sequence[Any], gold: Sequence[Any]) -> float | None:
    """Pearson r over the scored pairs; None if fewer than two or constant."""
    _check_lengths(pred=pred, gold=gold)
    _, p, g = _scored(pred, gold)
    if not _correlatable(p, g):
        return None
    return _r(_defined(_quiet(lambda: stats.pearsonr(p, g)).statistic))


def spearman(pred: Sequence[Any], gold: Sequence[Any]) -> float | None:
    """Rank correlation: the honest one when the judge's 1-5 scale is skewed."""
    _check_lengths(pred=pred, gold=gold)
    _, p, g = _scored(pred, gold)
    if not _correlatable(p, g):
        return None
    return _r(_defined(_quiet(lambda: stats.spearmanr(p, g)).statistic))


def kendall(pred: Sequence[Any], gold: Sequence[Any]) -> float | None:
    """Tau-b, so the heavy ties of a 5-point scale are handled properly."""
    _check_lengths(pred=pred, gold=gold)
    _, p, g = _scored(pred, gold)
    if not _correlatable(p, g):
        return None
    return _r(_defined(_quiet(lambda: stats.kendalltau(p, g)).statistic))


def mae(pred: Sequence[Any], gold: Sequence[Any]) -> float | None:
    """Mean absolute error in pc points, over the scored pairs only."""
    _check_lengths(pred=pred, gold=gold)
    _, p, g = _scored(pred, gold)
    if p.size == 0:
        return None
    return _r(float(np.mean(np.abs(p - g))))


def rmse(pred: Sequence[Any], gold: Sequence[Any]) -> float | None:
    """Root mean squared error: MAE's companion, sensitive to the big misses."""
    _check_lengths(pred=pred, gold=gold)
    _, p, g = _scored(pred, gold)
    if p.size == 0:
        return None
    return _r(float(np.sqrt(np.mean((p - g) ** 2))))


# --------------------------------------------------------------------------
# correlation block
# --------------------------------------------------------------------------


def correlations(pred: Sequence[Any], gold: Sequence[Any]) -> dict[str, Any]:
    """Agreement with human pc, reported together with the coverage it was
    measured at.

    Abstentions (None or NaN predictions) are excluded from the correlations and
    the error terms but counted in `n_abstained`, so a high Pearson at low
    coverage cannot be mistaken for a good judge. Rows whose gold label is
    itself missing are also unscoreable and land in `n_abstained`; gold is
    expected to be complete.
    """
    _check_lengths(pred=pred, gold=gold)
    n_total = len(gold)
    _, p, g = _scored(pred, gold)
    n_scored = int(p.size)
    ok = _correlatable(p, g)
    return {
        "n_total": n_total,
        "n_scored": n_scored,
        "n_abstained": n_total - n_scored,
        "coverage": _r(n_scored / n_total) if n_total else None,
        "pearson": _r(_defined(_quiet(lambda: stats.pearsonr(p, g)).statistic)) if ok else None,
        "spearman": _r(_defined(_quiet(lambda: stats.spearmanr(p, g)).statistic)) if ok else None,
        "kendall": _r(_defined(_quiet(lambda: stats.kendalltau(p, g)).statistic)) if ok else None,
        "mae": _r(float(np.mean(np.abs(p - g)))) if n_scored else None,
        "rmse": _r(float(np.sqrt(np.mean((p - g) ** 2)))) if n_scored else None,
    }


# --------------------------------------------------------------------------
# binary block
# --------------------------------------------------------------------------


def _prf(tp: int, fp: int, fn: int, tn: int) -> tuple[float, float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    total = tp + fp + fn + tn
    accuracy = (tp + tn) / total if total else 0.0
    return precision, recall, f1, accuracy


def _confusion(p: np.ndarray, y: np.ndarray, threshold: float) -> tuple[int, int, int, int]:
    hat = p >= threshold
    return (
        int(np.sum(hat & y)),
        int(np.sum(hat & ~y)),
        int(np.sum(~hat & y)),
        int(np.sum(~hat & ~y)),
    )


def binary_metrics(
    pred: Sequence[Any], gold: Sequence[Any], threshold: float = 4.0
) -> dict[str, Any]:
    """Ranking and decision quality for VideoPhy-2's "physically plausible" cut.

    The positive class is gold >= `threshold` (4 by default, matching the
    dataset's own `joint` criterion). Two operating points are reported: the
    natural one, where the judge's own 1-5 score is thresholded at the same
    value as the humans', and the best achievable one, which says how much of
    any weakness is calibration rather than ranking. `best_threshold` is the
    lowest threshold attaining the best F1, so it is stable under ties.
    """
    _check_lengths(pred=pred, gold=gold)
    n_total = len(gold)
    _, p, g = _scored(pred, gold)
    y = g >= threshold
    n_pos, n_neg = int(np.sum(y)), int(np.sum(~y))

    out: dict[str, Any] = {
        "n_total": n_total,
        "n_scored": int(p.size),
        "n_pos": n_pos,
        "n_neg": n_neg,
        "threshold": _r(threshold),
        "auroc": None,
        "average_precision": None,
        "f1_at_threshold": None,
        "precision_at_threshold": None,
        "recall_at_threshold": None,
        "accuracy_at_threshold": None,
        "best_f1": None,
        "best_threshold": None,
        "precision_at_best": None,
        "recall_at_best": None,
        "accuracy_at_best": None,
    }
    if p.size == 0:
        return out

    if n_pos and n_neg:  # both undefined with a single class present
        out["auroc"] = _r(_defined(_quiet(lambda: roc_auc_score(y, p))))
        out["average_precision"] = _r(_defined(_quiet(lambda: average_precision_score(y, p))))

    prec, rec, f1, acc = _prf(*_confusion(p, y, threshold))
    out["precision_at_threshold"] = _r(prec)
    out["recall_at_threshold"] = _r(rec)
    out["f1_at_threshold"] = _r(f1)
    out["accuracy_at_threshold"] = _r(acc)

    best = (-1.0, None, 0.0, 0.0, 0.0)
    for cut in np.unique(p):  # ascending, so ties keep the lowest threshold
        prec_c, rec_c, f1_c, acc_c = _prf(*_confusion(p, y, float(cut)))
        if f1_c > best[0]:
            best = (f1_c, float(cut), prec_c, rec_c, acc_c)
    out["best_f1"] = _r(best[0])
    out["best_threshold"] = _r(best[1])
    out["precision_at_best"] = _r(best[2])
    out["recall_at_best"] = _r(best[3])
    out["accuracy_at_best"] = _r(best[4])
    return out


# --------------------------------------------------------------------------
# risk-coverage: the value of abstention
# --------------------------------------------------------------------------


def _risk_fn(risk: str) -> Callable[[np.ndarray, np.ndarray], np.ndarray]:
    """Per-item loss. "mae" is absolute score error; "err@x" is 0/1
    misclassification of gold >= x, of which "err@4" is the one that matters."""
    if risk == "mae":
        return lambda p, g: np.abs(p - g)
    if risk.startswith("err@"):
        try:
            cut = float(risk[len("err@") :])
        except ValueError:
            raise ValueError(f"unparseable risk threshold: {risk!r}") from None
        return lambda p, g: ((p >= cut) != (g >= cut)).astype(float)
    raise ValueError(f"unknown risk {risk!r}; expected 'mae' or 'err@<x>'")


def risk_coverage(
    pred: Sequence[Any],
    gold: Sequence[Any],
    confidence: Sequence[Any] | None,
    risk: str = "mae",
    max_points: int = 200,
) -> dict[str, Any]:
    """Does refusing the least confident cases actually reduce error?

    Items are ranked by stated confidence, highest first, and the risk is
    recomputed over each retained prefix. A judge whose confidence is
    informative shows risk falling as coverage falls; a judge whose confidence
    is noise shows a flat curve, which is the failure this metric exists to
    expose.

    Abstentions are forced to the bottom of the ranking whatever confidence
    they claim -- an abstention is a refusal to be scored, so it can only ever
    be retained last. Risk is computed over the scored members of the retained
    prefix, and each curve point carries both `n` (retained) and `n_scored` so
    that a risk measured over fewer items than it covers is visible rather than
    silently flattering.

    `aurc` is the mean selective risk across all coverage levels 1/n .. 1;
    lower is better. The curve itself is thinned to `max_points` for reporting,
    but `aurc` and `risk_at` always use full resolution.
    """
    if confidence is None:
        confidence = [0.0] * len(gold)
    _check_lengths(pred=pred, gold=gold, confidence=confidence)
    loss_of = _risk_fn(risk)
    n_total = len(gold)
    out: dict[str, Any] = {
        "risk": risk,
        "n_total": n_total,
        "n_scored": 0,
        "curve": [],
        "aurc": None,
        "risk_at": {k: None for k in ("1.0", "0.9", "0.75", "0.5")},
    }
    if n_total == 0:
        return out

    idx, p, g = _scored(pred, gold)
    out["n_scored"] = int(p.size)
    scored_at = {int(i): j for j, i in enumerate(idx)}
    losses = loss_of(p, g) if p.size else np.zeros(0)

    def stated(i: int) -> float:
        if i not in scored_at:
            return -math.inf  # refused: retained last whatever it claims
        c = _as_number(confidence[i])
        return c if c is not None else -math.inf

    # Descending confidence, ties broken by original position for determinism.
    order = sorted(range(n_total), key=lambda i: (-stated(i), i))

    is_scored = np.array([1.0 if i in scored_at else 0.0 for i in order])
    step_loss = np.array([losses[scored_at[i]] if i in scored_at else 0.0 for i in order])
    cum_scored = np.cumsum(is_scored)
    cum_loss = np.cumsum(step_loss)

    risks: list[float | None] = [
        float(cum_loss[k] / cum_scored[k]) if cum_scored[k] > 0 else None
        for k in range(n_total)
    ]
    usable = [r for r in risks if r is not None]
    out["aurc"] = _r(float(np.mean(usable))) if usable else None

    for target in (1.0, 0.9, 0.75, 0.5):
        k = min(n_total, max(1, int(math.floor(target * n_total + 1e-9))))
        out["risk_at"][f"{target}"] = _r(risks[k - 1])

    if n_total <= max_points:
        cuts = list(range(1, n_total + 1))
    else:
        cuts = sorted({int(round(v)) for v in np.linspace(1, n_total, max_points)})

    curve: list[dict[str, Any]] = []
    for k in cuts:
        prefix = order[:k]
        sub = [scored_at[i] for i in prefix if i in scored_at]
        pp, gg = p[sub], g[sub]
        curve.append(
            {
                "coverage": _r(k / n_total),
                "n": k,
                "n_scored": len(sub),
                "risk": _r(risks[k - 1]),
                "pearson": (
                    _r(_defined(_quiet(lambda: stats.pearsonr(pp, gg)).statistic))
                    if _correlatable(pp, gg)
                    else None
                ),
            }
        )
    out["curve"] = curve
    return out


# --------------------------------------------------------------------------
# open-ended discovery
# --------------------------------------------------------------------------


def content_words(text: str) -> set[str]:
    """Lowercased, de-punctuated, stopword-free tokens with a crude plural fold.

    The plural fold ("floors" -> "floor") is applied to both sides, so it can
    only add matches that a reader would agree with; anything subtler than that
    is the LLM matcher's job.
    """
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in str(text).lower())
    words: set[str] = set()
    for tok in cleaned.split():
        if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
            tok = tok[:-1]
        if tok and tok not in STOPWORDS and not tok.isdigit():
            words.add(tok)
    return words


def lexical_match(a: str, b: str, threshold: float = 0.34) -> bool:
    """Content-word Jaccard overlap at or above `threshold`."""
    wa, wb = content_words(a), content_words(b)
    if not wa or not wb:
        return False
    union = len(wa | wb)
    return (len(wa & wb) / union) >= threshold if union else False


def open_discovery_match(
    predicted: Sequence[str],
    gold: Sequence[str],
    matcher: Callable[[str, str], bool] | None = None,
) -> dict[str, Any]:
    """Did we find the violations humans had to write in by hand?

    `human_violated_rules` is free text that annotators added because the
    automatic rule list missed the failure, so this is the only metric in the
    file that measures discovery rather than scoring.

    Matching is greedy and one-to-one: predictions are taken in order and claim
    the first not-yet-consumed gold rule they match, so two predictions
    describing the same human-written violation earn one match, not two. Blank
    entries are ignored on both sides and excluded from the counts, but the
    indices in `matches` refer to the original sequences.

    `matcher` is the extension point. The default is lexical and therefore
    strict about vocabulary; an LLM matcher with the same signature replaces it
    without touching anything else here.
    """
    match = matcher or lexical_match
    pred_items = [(i, s) for i, s in enumerate(predicted) if str(s).strip()]
    gold_items = [(i, s) for i, s in enumerate(gold) if str(s).strip()]
    n_pred, n_gold = len(pred_items), len(gold_items)

    consumed: set[int] = set()
    matches: list[tuple[int, int]] = []
    for pi, ptext in pred_items:
        for gi, gtext in gold_items:
            if gi in consumed:
                continue
            if match(str(ptext), str(gtext)):
                consumed.add(gi)
                matches.append((pi, gi))
                break

    precision = len(matches) / n_pred if n_pred else None
    recall = len(matches) / n_gold if n_gold else None
    if precision is None or recall is None:
        f1: float | None = None
    elif precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    return {
        "precision": _r(precision),
        "recall": _r(recall),
        "f1": _r(f1),
        "n_pred": n_pred,
        "n_gold": n_gold,
        "n_matched": len(matches),
        "matches": matches,
        "unmatched_gold": [str(s) for i, s in gold_items if i not in consumed],
    }


# --------------------------------------------------------------------------
# cost
# --------------------------------------------------------------------------


def _cost_value(cost: Any, key: str) -> float | None:
    if cost is None:
        return None
    if isinstance(cost, Mapping):
        return _as_number(cost.get(key))
    if hasattr(cost, "as_dict"):
        return _as_number(cost.as_dict().get(key))
    return _as_number(getattr(cost, key, None))


def cost_curve(
    costs: Sequence[Any],
    pred: Sequence[Any],
    gold: Sequence[Any],
    key: str = "frames",
    buckets: int = 5,
) -> dict[str, Any]:
    """Accuracy as a function of observation spent -- the adaptive-budget claim.

    Rows are sorted by `cost[key]` and split into equal-sized buckets, which is
    quantile bucketing done by rank so that heavily tied cost distributions
    (frame counts are quantised) still yield non-empty buckets. Ties may
    straddle a boundary; `cost_lo`/`cost_hi` make that visible.

    `cost_vs_abs_error_spearman` is the summary statement: negative means the
    loop spent more where it helped, positive means it spent more where it was
    already lost. Rows with no cost recorded are counted, not imputed.
    """
    _check_lengths(costs=costs, pred=pred, gold=gold)
    n_total = len(gold)
    values = [_cost_value(c, key) for c in costs]
    with_cost = [i for i, v in enumerate(values) if v is not None]

    out: dict[str, Any] = {
        "key": key,
        "n_total": n_total,
        "n_with_cost": len(with_cost),
        "n_missing_cost": n_total - len(with_cost),
        "n_buckets": 0,
        "buckets": [],
        "cost_vs_abs_error_spearman": None,
    }
    if not with_cost:
        return out

    idx, p, g = _scored(pred, gold)
    pair_at = {int(i): (float(pv), float(gv)) for i, pv, gv in zip(idx, p, g)}
    err_at = {i: abs(pv - gv) for i, (pv, gv) in pair_at.items()}
    both = [i for i in with_cost if i in err_at]
    if len(both) >= 2:
        cv = np.array([values[i] for i in both], dtype=float)
        ev = np.array([err_at[i] for i in both], dtype=float)
        if _correlatable(cv, ev):
            out["cost_vs_abs_error_spearman"] = _r(
                _defined(_quiet(lambda: stats.spearmanr(cv, ev)).statistic)
            )

    n_buckets = max(1, min(int(buckets), len(with_cost)))
    ordered = sorted(with_cost, key=lambda i: (values[i], i))
    groups = [list(map(int, grp)) for grp in np.array_split(np.asarray(ordered), n_buckets)]

    rows: list[dict[str, Any]] = []
    for b, group in enumerate(groups):
        if not group:
            continue
        cvals = np.array([values[i] for i in group], dtype=float)
        scored = [i for i in group if i in pair_at]
        pp = np.array([pair_at[i][0] for i in scored], dtype=float)
        gg = np.array([pair_at[i][1] for i in scored], dtype=float)
        rows.append(
            {
                "bucket": b,
                "n": len(group),
                "n_scored": len(scored),
                "cost_lo": _r(float(cvals.min())),
                "cost_hi": _r(float(cvals.max())),
                "mean_cost": _r(float(cvals.mean())),
                "pearson": (
                    _r(_defined(_quiet(lambda: stats.pearsonr(pp, gg)).statistic))
                    if _correlatable(pp, gg)
                    else None
                ),
                "mae": _r(float(np.mean(np.abs(pp - gg)))) if scored else None,
            }
        )
    out["buckets"] = rows
    out["n_buckets"] = len(rows)
    return out


# --------------------------------------------------------------------------
# uncertainty
# --------------------------------------------------------------------------


def bootstrap_ci(
    metric_fn: Callable[[Sequence[Any], Sequence[Any]], float | None],
    pred: Sequence[Any],
    gold: Sequence[Any],
    n_resamples: int = 1000,
    seed: int = 0,
    alpha: float = 0.05,
) -> dict[str, Any]:
    """Percentile bootstrap over paired indices.

    Paired resampling keeps each prediction with its own gold label, which is
    the only correct unit here: the videos are independent, the two columns are
    not. Resamples where the metric is undefined (a resample can easily be
    constant, or all-abstain) are skipped rather than counted as zero, so
    `n_resamples` reports how many actually contributed.
    """
    _check_lengths(pred=pred, gold=gold)
    n = len(gold)
    point = None
    try:
        point = metric_fn(pred, gold)
    except (ValueError, ZeroDivisionError, IndexError):
        point = None

    out: dict[str, Any] = {
        "point": _r(_defined(point)) if point is not None else None,
        "lo": None,
        "hi": None,
        "n_resamples": 0,
        "n_requested": int(n_resamples),
        "alpha": _r(alpha),
    }
    if n == 0 or n_resamples <= 0:
        return out

    rng = np.random.default_rng(seed)
    pred_list, gold_list = list(pred), list(gold)
    values: list[float] = []
    for _ in range(int(n_resamples)):
        take = rng.integers(0, n, n)
        try:
            v = metric_fn([pred_list[i] for i in take], [gold_list[i] for i in take])
        except (ValueError, ZeroDivisionError, IndexError):
            continue
        f = _defined(v)
        if f is not None:
            values.append(f)
    out["n_resamples"] = len(values)
    if values:
        lo, hi = np.percentile(values, [100 * alpha / 2, 100 * (1 - alpha / 2)])
        out["lo"], out["hi"] = _r(float(lo)), _r(float(hi))
    return out


# --------------------------------------------------------------------------
# the results-table row
# --------------------------------------------------------------------------


def summarise(
    pred: Sequence[Any],
    gold: Sequence[Any],
    confidence: Sequence[Any] | None = None,
    costs: Sequence[Any] | None = None,
    threshold: float = 4.0,
    n_boot: int = 1000,
    seed: int = 0,
) -> dict[str, Any]:
    """One row of the results table.

    Headline numbers are flattened so a run can be printed as a line; the full
    sub-dicts are nested under `binary`, `risk_coverage` and `cost` for anything
    that wants the curves. The Pearson CI is here rather than optional because a
    single-number comparison between two prompt variants on a 50-video pilot is
    otherwise indistinguishable from noise.
    """
    _check_lengths(pred=pred, gold=gold)
    core = correlations(pred, gold)
    binary = binary_metrics(pred, gold, threshold=threshold)
    row: dict[str, Any] = dict(core)
    row["pearson_ci"] = bootstrap_ci(pearson, pred, gold, n_resamples=n_boot, seed=seed)
    row["threshold"] = _r(threshold)
    for k in ("auroc", "average_precision", "f1_at_threshold", "best_f1", "best_threshold",
              "n_pos", "n_neg"):
        row[k] = binary[k]
    row["binary"] = binary

    # Both risks, because they answer different questions: whether abstention
    # buys accuracy on the 1-5 scale, and whether it buys the plausible/not call.
    rc = rc_err = None
    if confidence is not None:
        rc = risk_coverage(pred, gold, confidence, risk="mae")
        rc_err = risk_coverage(pred, gold, confidence, risk=f"err@{threshold:g}")
    row["aurc"] = rc["aurc"] if rc else None
    row["risk_at"] = rc["risk_at"] if rc else None
    row["aurc_err"] = rc_err["aurc"] if rc_err else None
    row["risk_coverage"] = rc
    row["risk_coverage_err"] = rc_err
    row["cost"] = cost_curve(costs, pred, gold) if costs is not None else None
    return row
