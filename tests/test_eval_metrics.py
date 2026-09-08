"""Offline tests for eval/metrics.py. No network, no model, no dataset.

Every number asserted here is either computed by hand in a comment or by an
independent formula written out longhand, because a metrics module that agrees
with itself proves nothing. The cases that matter:

  - a Pearson/Spearman/Kendall triple small enough to differentiate on paper
  - AUROC at its three known fixed points (separable 1.0, reversed 0.0, tied 0.5)
    and an average precision computed by summing the precision-recall steps
  - a risk-coverage case where dropping the least confident item provably takes
    MAE from 1.0 to 0.0 and Pearson from negative to +1.0
  - an abstention that claims the highest confidence and must still be ranked last
  - an open-discovery paraphrase that must match and a near-miss that must not,
    plus the one-to-one consumption rule
  - the full degenerate battery, run with warnings promoted to errors so that a
    stray scipy/sklearn warning fails the test rather than the harness
"""

from __future__ import annotations

import importlib.util
import math
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Loaded by path rather than imported: eval/ has no __init__.py yet (the
# integrator writes it), and the package name would shadow the builtin `eval`.
_spec = importlib.util.spec_from_file_location("pjudge_eval_metrics", ROOT / "eval" / "metrics.py")
assert _spec and _spec.loader
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)


def close(a, b, tol: float = 1e-6) -> bool:
    if a is None or b is None:
        return a is b or a == b
    return abs(float(a) - float(b)) <= tol


def pearson_longhand(xs, ys) -> float:
    """Independent implementation, used to check the scipy path."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return cov / (sx * sy)


# --------------------------------------------------------------------------
# correlations
# --------------------------------------------------------------------------


def test_correlations_hand_computed() -> None:
    # pred=[1,2,3], gold=[1,3,2]: both means 2, cov = 1, sd = sqrt(2) each
    #   pearson = 1/2 = 0.5; ranks are identical to values so spearman = 0.5
    #   kendall: pairs (0,1) concordant, (0,2) concordant, (1,2) discordant
    #            tau = (2 - 1) / 3 = 0.333333
    #   mae = (0 + 1 + 1)/3 = 0.666667; rmse = sqrt(2/3) = 0.816497
    pred, gold = [1, 2, 3], [1, 3, 2]
    out = M.correlations(pred, gold)
    assert close(out["pearson"], 0.5), out
    assert close(out["pearson"], pearson_longhand(pred, gold)), out
    assert close(out["spearman"], 0.5), out
    assert close(out["kendall"], 1 / 3), out
    assert close(out["mae"], 2 / 3), out
    assert close(out["rmse"], math.sqrt(2 / 3)), out
    assert (out["n_total"], out["n_scored"], out["n_abstained"]) == (3, 3, 0), out
    assert out["coverage"] == 1.0, out

    # exact endpoints, and rounding must clean up float dust to a flat 1.0
    assert M.correlations([1, 2, 3, 4], [2, 4, 6, 8])["pearson"] == 1.0
    assert M.correlations([1, 2, 3], [3, 2, 1])["pearson"] == -1.0
    assert M.correlations([1, 2, 3], [3, 2, 1])["kendall"] == -1.0

    # the module-level helpers must agree with the block
    assert M.pearson(pred, gold) == out["pearson"]
    assert M.mae(pred, gold) == out["mae"]
    print(f"  correlations ok: {out}")


def test_abstentions_excluded_but_counted() -> None:
    """None and NaN leave the correlation untouched and cut coverage."""
    pred = [1, 2, 3, None, float("nan")]
    gold = [1, 3, 2, 5, 5]
    out = M.correlations(pred, gold)
    assert (out["n_total"], out["n_scored"], out["n_abstained"]) == (5, 3, 2), out
    assert close(out["coverage"], 0.6), out
    assert close(out["pearson"], 0.5), out          # unchanged from the 3-row case
    assert close(out["mae"], 2 / 3), out            # gold 5s must not enter the mean
    assert M.correlations(pred, gold)["pearson"] == M.correlations([1, 2, 3], [1, 3, 2])["pearson"]
    print(f"  abstention accounting ok: coverage={out['coverage']} "
          f"n_abstained={out['n_abstained']}")


def test_length_mismatch_raises() -> None:
    for call in (
        lambda: M.correlations([1, 2], [1, 2, 3]),
        lambda: M.binary_metrics([1], [1, 2]),
        lambda: M.risk_coverage([1, 2], [1, 2], [0.5]),
        lambda: M.cost_curve([{}], [1, 2], [1, 2]),
        lambda: M.bootstrap_ci(M.pearson, [1], [1, 2]),
        lambda: M.summarise([1], [1, 2]),
    ):
        try:
            call()
        except ValueError:
            continue
        raise AssertionError("length mismatch did not raise ValueError")
    print("  length validation ok: every entry point raises ValueError")


# --------------------------------------------------------------------------
# binary
# --------------------------------------------------------------------------


def test_binary_metrics_known_points() -> None:
    gold = [5, 5, 2, 2]  # positives (gold >= 4) are items 0 and 1

    sep = M.binary_metrics([4, 5, 1, 2], gold)
    assert sep["n_pos"] == 2 and sep["n_neg"] == 2, sep
    assert sep["auroc"] == 1.0, sep                     # perfectly separable
    assert sep["average_precision"] == 1.0, sep
    assert sep["f1_at_threshold"] == 1.0, sep
    assert sep["precision_at_threshold"] == 1.0 and sep["recall_at_threshold"] == 1.0, sep
    assert sep["accuracy_at_threshold"] == 1.0, sep
    # sweep of >= cuts: 1 -> f1 0.667, 2 -> 0.8, 4 -> 1.0, 5 -> 0.667
    assert sep["best_f1"] == 1.0 and sep["best_threshold"] == 4.0, sep

    rev = M.binary_metrics([1, 2, 4, 5], gold)
    assert rev["auroc"] == 0.0, rev                     # ranking exactly inverted
    # AP by hand: descending scores 5(neg) 4(neg) 2(pos) 1(pos)
    #   recall 0.5 at precision 1/3, recall 1.0 at precision 2/4
    #   AP = 0.5*(1/3) + 0.5*(1/2) = 0.416667
    assert close(rev["average_precision"], 0.5 * (1 / 3) + 0.5 * 0.5), rev
    assert rev["f1_at_threshold"] == 0.0, rev           # predicts the wrong two
    assert rev["accuracy_at_threshold"] == 0.0, rev
    # best is the degenerate "everything is plausible" rule: p=0.5, r=1
    assert close(rev["best_f1"], 2 / 3) and rev["best_threshold"] == 1.0, rev

    tied = M.binary_metrics([3, 3, 3, 3], gold)
    assert tied["auroc"] == 0.5, tied                   # no information at all
    assert tied["average_precision"] == 0.5, tied
    assert tied["f1_at_threshold"] == 0.0, tied         # nothing reaches 4
    assert tied["accuracy_at_threshold"] == 0.5, tied
    assert close(tied["best_f1"], 2 / 3) and tied["best_threshold"] == 3.0, tied

    single = M.binary_metrics([5, 5, 4, 4], [5, 5, 4, 4])
    assert single["n_neg"] == 0, single
    assert single["auroc"] is None and single["average_precision"] is None, single
    assert single["f1_at_threshold"] == 1.0, single      # still a well-defined decision

    # ties in best F1 must resolve to the lowest threshold, or the reported
    # operating point wanders between runs. pred=[1,1,1,2], gold=[2,2,5,5]:
    #   cut 1 -> tp2 fp2 fn0 -> 4/6      cut 2 -> tp1 fp0 fn1 -> 2/3
    tie = M.binary_metrics([1, 1, 1, 2], [2, 2, 5, 5])
    assert close(tie["best_f1"], 2 / 3) and tie["best_threshold"] == 1.0, tie
    assert tie["precision_at_best"] == 0.5 and tie["recall_at_best"] == 1.0, tie
    assert tie["accuracy_at_best"] == 0.5, tie

    # a different cut moves the class boundary, and the reported threshold follows
    at3 = M.binary_metrics([4, 5, 1, 2], [5, 5, 2, 2], threshold=3.0)
    assert at3["threshold"] == 3.0 and at3["n_pos"] == 2, at3
    print(f"  binary metrics ok: auroc {sep['auroc']}/{rev['auroc']}/{tied['auroc']} "
          f"ap_reversed={rev['average_precision']}")


# --------------------------------------------------------------------------
# risk-coverage
# --------------------------------------------------------------------------


def test_risk_coverage_rewards_good_abstention() -> None:
    # Three exact predictions with high confidence, one bad one with low.
    pred = [3, 4, 5, 1]
    gold = [3, 4, 5, 5]
    conf = [0.9, 0.8, 0.7, 0.1]
    rc = M.risk_coverage(pred, gold, conf, risk="mae")

    risks = [pt["risk"] for pt in rc["curve"]]
    assert risks == [0.0, 0.0, 0.0, 1.0], rc["curve"]   # |1-5| / 4 = 1.0 at full coverage
    assert close(rc["aurc"], (0.0 + 0.0 + 0.0 + 1.0) / 4), rc["aurc"]
    assert rc["risk_at"]["1.0"] == 1.0, rc["risk_at"]
    assert rc["risk_at"]["0.9"] == 0.0, rc["risk_at"]   # floor(3.6) = 3 items kept
    assert rc["risk_at"]["0.75"] == 0.0 and rc["risk_at"]["0.5"] == 0.0, rc["risk_at"]
    assert [pt["coverage"] for pt in rc["curve"]] == [0.25, 0.5, 0.75, 1.0], rc["curve"]

    # and the same abstention rescues the correlation from noise to perfect
    assert rc["curve"][2]["pearson"] == 1.0, rc["curve"][2]
    assert close(rc["curve"][3]["pearson"], pearson_longhand(pred, gold)), rc["curve"][3]
    assert rc["curve"][3]["pearson"] < 0, rc["curve"][3]

    # err@4: gold>=4 is [F,T,T,T], pred>=4 is [F,T,T,F] -> one misclassification
    err = M.risk_coverage(pred, gold, conf, risk="err@4")
    assert [pt["risk"] for pt in err["curve"]] == [0.0, 0.0, 0.0, 0.25], err["curve"]
    assert close(err["aurc"], 0.25 / 4), err["aurc"]

    # a flat curve is the failure this metric exists to expose: same errors, but
    # confidence ordered so the bad item is retained first
    noisy = M.risk_coverage(pred, gold, [0.1, 0.2, 0.3, 0.9], risk="mae")
    assert noisy["curve"][0]["risk"] == 4.0, noisy["curve"]
    assert noisy["aurc"] > rc["aurc"], (noisy["aurc"], rc["aurc"])
    print(f"  risk-coverage ok: aurc {rc['aurc']} (informative) vs {noisy['aurc']} (noise), "
          f"risk_at={rc['risk_at']}")


def test_abstention_is_ranked_last_whatever_it_claims() -> None:
    # Item 0 abstained but claims 0.99 confidence; it must still be retained last.
    pred = [None, 5, 4, 3]
    gold = [1, 5, 5, 5]
    conf = [0.99, 0.8, 0.7, 0.6]
    rc = M.risk_coverage(pred, gold, conf, risk="mae")

    # errors of the scored items in confidence order: 0, 1, 2
    assert [pt["risk"] for pt in rc["curve"]] == [0.0, 0.5, 1.0, 1.0], rc["curve"]
    assert [pt["n"] for pt in rc["curve"]] == [1, 2, 3, 4], rc["curve"]
    assert [pt["n_scored"] for pt in rc["curve"]] == [1, 2, 3, 3], rc["curve"]
    assert close(rc["aurc"], (0.0 + 0.5 + 1.0 + 1.0) / 4), rc["aurc"]
    assert rc["n_scored"] == 3 and rc["n_total"] == 4, rc

    # a missing confidence on a scored item is also treated as the worst
    rc2 = M.risk_coverage([5, 1], [5, 5], [None, 0.9], risk="mae")
    assert rc2["curve"][0]["risk"] == 4.0, rc2["curve"]

    try:
        M.risk_coverage([1], [1], [0.5], risk="brier")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown risk name must raise")
    print(f"  abstention ranking ok: n_scored per point={[p['n_scored'] for p in rc['curve']]}")


def test_risk_coverage_curve_is_thinned_but_aurc_is_not() -> None:
    n = 500
    pred = [3.0] * n
    gold = [3.0 if i % 2 else 5.0 for i in range(n)]
    conf = [i / n for i in range(n)]
    rc = M.risk_coverage(pred, gold, conf, risk="mae", max_points=50)
    assert len(rc["curve"]) <= 50, len(rc["curve"])
    assert rc["curve"][-1]["coverage"] == 1.0 and rc["curve"][-1]["n"] == n
    # half the items are off by 2, so full-coverage MAE is exactly 1.0
    assert close(rc["risk_at"]["1.0"], 1.0), rc["risk_at"]
    assert rc["aurc"] is not None
    print(f"  curve thinning ok: {len(rc['curve'])} points for n={n}, aurc={rc['aurc']}")


# --------------------------------------------------------------------------
# open-ended discovery
# --------------------------------------------------------------------------


GOLD_RULE = "The ball passes through the solid floor instead of bouncing."
PARAPHRASE = "The ball sinks through the floor rather than bouncing back."
NEAR_MISS = "The ball's colour changes from red to blue midway."
OTHER_RULE = "The candle flame does not flicker when the man blows on it."


def test_open_discovery_paraphrase_and_near_miss() -> None:
    # content words: gold {ball,passe,through,solid,floor,instead,bouncing}
    #                pred {ball,sink,through,floor,rather,bouncing,back}
    #                jaccard = 4/10 = 0.4 >= 0.34 -> match
    assert M.lexical_match(PARAPHRASE, GOLD_RULE)
    # near miss shares only "ball": 1/12 = 0.083 -> no match
    assert not M.lexical_match(NEAR_MISS, GOLD_RULE)

    hit = M.open_discovery_match([PARAPHRASE], [GOLD_RULE])
    assert hit["precision"] == 1.0 and hit["recall"] == 1.0 and hit["f1"] == 1.0, hit
    assert hit["matches"] == [(0, 0)] and hit["unmatched_gold"] == [], hit

    miss = M.open_discovery_match([NEAR_MISS], [GOLD_RULE])
    assert miss["precision"] == 0.0 and miss["recall"] == 0.0 and miss["f1"] == 0.0, miss
    assert miss["unmatched_gold"] == [GOLD_RULE], miss

    partial = M.open_discovery_match([PARAPHRASE], [GOLD_RULE, OTHER_RULE])
    assert partial["precision"] == 1.0 and partial["recall"] == 0.5, partial
    assert close(partial["f1"], 2 / 3), partial
    assert partial["unmatched_gold"] == [OTHER_RULE], partial
    print(f"  paraphrase matching ok: {hit['matches']} precision={partial['precision']} "
          f"recall={partial['recall']}")


def test_open_discovery_is_one_to_one() -> None:
    """Two ways of saying the same thing must not earn two matches."""
    duplicate = "The ball goes through the floor without bouncing."
    assert M.lexical_match(duplicate, GOLD_RULE)  # would match on its own
    out = M.open_discovery_match([PARAPHRASE, duplicate], [GOLD_RULE])
    assert out["n_matched"] == 1, out
    assert out["matches"] == [(0, 0)], out
    assert out["precision"] == 0.5 and out["recall"] == 1.0, out
    assert close(out["f1"], 2 / 3), out

    # blanks are not claims: dropped from the counts, but indices stay original
    blanks = M.open_discovery_match(["", "   ", PARAPHRASE], [GOLD_RULE, "  "])
    assert blanks["n_pred"] == 1 and blanks["n_gold"] == 1, blanks
    assert blanks["matches"] == [(2, 0)], blanks

    # the matcher is the extension point: swapping it changes only the pairing
    everything = M.open_discovery_match(
        [NEAR_MISS, "anything"], [GOLD_RULE, OTHER_RULE, "third"], matcher=lambda a, b: True
    )
    assert everything["n_matched"] == 2 and everything["matches"] == [(0, 0), (1, 1)], everything
    assert everything["precision"] == 1.0 and close(everything["recall"], 2 / 3), everything

    empty = M.open_discovery_match([], [])
    assert empty["precision"] is None and empty["recall"] is None and empty["f1"] is None, empty
    nothing_found = M.open_discovery_match([], [GOLD_RULE])
    assert nothing_found["recall"] == 0.0 and nothing_found["precision"] is None, nothing_found
    print(f"  one-to-one matching ok: {out['n_matched']} match for 2 predictions")


# --------------------------------------------------------------------------
# cost
# --------------------------------------------------------------------------


class DummyCost:
    """Stands in for ObservationCost: accepted via as_dict, not just Mapping."""

    def __init__(self, frames: int):
        self.frames = frames

    def as_dict(self) -> dict[str, int]:
        return {"frames": self.frames}


def test_cost_curve_buckets() -> None:
    costs = [{"frames": 2}, {"frames": 4}, {"frames": 6}, {"frames": 8}]
    pred = [1, 5, 5, 1]
    gold = [5, 1, 5, 1]
    out = M.cost_curve(costs, pred, gold, key="frames", buckets=2)
    assert out["n_buckets"] == 2 and out["n_with_cost"] == 4, out

    lo, hi = out["buckets"]
    assert (lo["n"], lo["cost_lo"], lo["cost_hi"], lo["mean_cost"]) == (2, 2.0, 4.0, 3.0), lo
    assert lo["pearson"] == -1.0 and lo["mae"] == 4.0, lo   # pred [1,5] vs gold [5,1]
    assert (hi["n"], hi["mean_cost"]) == (2, 7.0), hi
    assert hi["pearson"] == 1.0 and hi["mae"] == 0.0, hi     # pred [5,1] vs gold [5,1]

    # abs errors [4,4,0,0] against costs [2,4,6,8]: rank correlation -4/sqrt(20)
    assert close(out["cost_vs_abs_error_spearman"], -4 / math.sqrt(20)), out

    # more buckets than rows collapses to one row per bucket, no crash, no pearson
    fine = M.cost_curve(costs, pred, gold, buckets=10)
    assert fine["n_buckets"] == 4, fine
    assert all(b["n"] == 1 and b["pearson"] is None for b in fine["buckets"]), fine
    assert [b["mae"] for b in fine["buckets"]] == [4.0, 4.0, 0.0, 0.0], fine

    # missing or unusable costs are counted, never imputed
    sparse = M.cost_curve([{"frames": 2}, {}, {"frames": 6}, {"other": 1}], pred, gold, buckets=2)
    assert sparse["n_with_cost"] == 2 and sparse["n_missing_cost"] == 2, sparse
    assert sum(b["n"] for b in sparse["buckets"]) == 2, sparse

    # abstentions inside a bucket reduce n_scored but not n
    with_abstain = M.cost_curve(costs, [1, None, 5, 1], gold, buckets=2)
    assert with_abstain["buckets"][0]["n"] == 2, with_abstain
    assert with_abstain["buckets"][0]["n_scored"] == 1, with_abstain
    assert with_abstain["buckets"][0]["pearson"] is None, with_abstain
    assert with_abstain["buckets"][0]["mae"] == 4.0, with_abstain

    # an ObservationCost-shaped object works as well as a dict
    objs = M.cost_curve([DummyCost(c["frames"]) for c in costs], pred, gold, buckets=2)
    assert objs["buckets"] == out["buckets"], objs
    print(f"  cost curve ok: mean_cost {lo['mean_cost']}->{hi['mean_cost']}, "
          f"mae {lo['mae']}->{hi['mae']}, spearman={out['cost_vs_abs_error_spearman']}")


# --------------------------------------------------------------------------
# bootstrap
# --------------------------------------------------------------------------


def test_bootstrap_is_deterministic_and_brackets_the_point() -> None:
    pred = [1, 2, 2, 3, 4, 4, 5, 5]
    gold = [1, 3, 2, 3, 5, 4, 5, 4]
    a = M.bootstrap_ci(M.pearson, pred, gold, n_resamples=200, seed=0)
    b = M.bootstrap_ci(M.pearson, pred, gold, n_resamples=200, seed=0)
    assert a == b, (a, b)                               # same seed, same numbers
    assert a["point"] == M.pearson(pred, gold), a
    assert a["lo"] <= a["point"] <= a["hi"], a
    assert a["n_resamples"] == 200 and a["n_requested"] == 200, a
    c = M.bootstrap_ci(M.pearson, pred, gold, n_resamples=200, seed=1)
    assert c["point"] == a["point"] and (c["lo"], c["hi"]) != (a["lo"], a["hi"]), (a, c)

    # undefined resamples are skipped, not counted as zero: any resample that
    # misses index 2 leaves pred constant, which happens about (2/3)^3 of the time
    thin = M.bootstrap_ci(M.pearson, [1, 1, 2], [1, 2, 3], n_resamples=200, seed=0)
    assert 0 < thin["n_resamples"] < 200, thin
    assert thin["point"] is not None and thin["lo"] is not None, thin

    # a wider interval must come from a wider alpha, deterministically
    tight = M.bootstrap_ci(M.pearson, pred, gold, n_resamples=200, seed=0, alpha=0.5)
    assert tight["lo"] >= a["lo"] and tight["hi"] <= a["hi"], (a, tight)
    print(f"  bootstrap ok: point={a['point']} ci=({a['lo']}, {a['hi']}) "
          f"used {thin['n_resamples']}/200 resamples on the degenerate case")


# --------------------------------------------------------------------------
# summarise
# --------------------------------------------------------------------------


def test_summarise_is_consistent_with_its_parts() -> None:
    pred = [1, 2, None, 4, 5, 3]
    gold = [1, 3, 5, 4, 5, 2]
    conf = [0.9, 0.5, 0.95, 0.8, 0.7, 0.2]
    costs = [{"frames": f} for f in (10, 20, 5, 30, 40, 50)]
    row = M.summarise(pred, gold, confidence=conf, costs=costs, threshold=4.0, n_boot=100)

    assert row["pearson"] == M.correlations(pred, gold)["pearson"], row
    assert row["auroc"] == M.binary_metrics(pred, gold)["auroc"], row
    assert row["n_total"] == 6 and row["n_scored"] == 5 and row["n_abstained"] == 1, row
    assert close(row["coverage"], 5 / 6), row
    assert row["pearson_ci"]["point"] == row["pearson"], row
    assert row["pearson_ci"]["lo"] <= row["pearson_ci"]["hi"], row
    assert row["aurc"] == row["risk_coverage"]["aurc"], row
    assert row["risk_coverage"]["risk"] == "mae", row
    assert row["risk_coverage_err"]["risk"] == "err@4", row
    assert row["cost"]["key"] == "frames" and row["cost"]["n_buckets"] == 5, row
    assert row["risk_at"]["1.0"] == row["mae"], row     # full coverage is plain MAE

    # the abstained row must be last in the ranking despite its 0.95 confidence
    assert row["risk_coverage"]["curve"][-1]["n_scored"] == 5, row["risk_coverage"]["curve"]

    bare = M.summarise(pred, gold)
    assert bare["risk_coverage"] is None and bare["cost"] is None, bare
    assert bare["pearson"] == row["pearson"], bare

    # determinism of the whole row
    assert M.summarise(pred, gold, confidence=conf, costs=costs, n_boot=100) == row
    print(f"  summarise ok: pearson={row['pearson']} ci=({row['pearson_ci']['lo']}, "
          f"{row['pearson_ci']['hi']}) auroc={row['auroc']} aurc={row['aurc']}")


# --------------------------------------------------------------------------
# degenerate battery
# --------------------------------------------------------------------------


def test_degenerate_inputs() -> None:
    """Empty, all-abstain, constant, single-class and n=1, with warnings fatal."""
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        empty = M.correlations([], [])
        assert empty["n_total"] == 0 and empty["coverage"] is None, empty
        assert all(empty[k] is None for k in ("pearson", "spearman", "kendall", "mae", "rmse"))

        allnone = M.correlations([None, None, None], [1, 2, 3])
        assert allnone["n_scored"] == 0 and allnone["coverage"] == 0.0, allnone
        assert allnone["pearson"] is None and allnone["mae"] is None, allnone

        # constant gold: correlation undefined, error terms still meaningful
        const_gold = M.correlations([1, 2, 3], [4, 4, 4])
        assert const_gold["pearson"] is None and const_gold["spearman"] is None, const_gold
        assert const_gold["kendall"] is None, const_gold
        assert close(const_gold["mae"], 2.0), const_gold
        assert close(const_gold["rmse"], math.sqrt(14 / 3)), const_gold

        const_pred = M.correlations([3, 3, 3], [1, 2, 3])
        assert const_pred["pearson"] is None and close(const_pred["mae"], 1.0), const_pred

        one = M.correlations([3], [4])
        assert one["pearson"] is None and one["mae"] == 1.0 and one["coverage"] == 1.0, one

        # pred, gold, expected aurc, expected best_f1 (all four are single-class
        # or unscoreable, so auroc and average precision must be None throughout)
        cases = [
            ([], [], None, None),
            ([None, None], [1, 5], None, None),
            ([3], [4], 1.0, 1.0),
            ([2, 2], [5, 5], 3.0, 1.0),
        ]
        for pred, gold, want_aurc, want_best_f1 in cases:
            b = M.binary_metrics(pred, gold)
            assert b["auroc"] is None and b["average_precision"] is None, (pred, b)
            assert b["best_f1"] == want_best_f1, (pred, b)

            rc = M.risk_coverage(pred, gold, None)
            assert rc["n_total"] == len(gold), (pred, rc)
            assert len(rc["curve"]) == len(gold), (pred, rc)
            assert rc["aurc"] == want_aurc, (pred, rc)
            assert rc["risk_at"]["1.0"] == want_aurc, (pred, rc)  # flat: one risk level

            cc = M.cost_curve([{} for _ in gold], pred, gold)
            assert cc["n_with_cost"] == 0 and cc["buckets"] == [], (pred, cc)

            boot = M.bootstrap_ci(M.pearson, pred, gold, n_resamples=25)
            assert boot["point"] is None and boot["lo"] is None, (pred, boot)

            s = M.summarise(pred, gold, confidence=[0.5] * len(gold), costs=[{}] * len(gold))
            assert s["pearson"] is None, (pred, s)
            assert s["n_total"] == len(gold), (pred, s)

        # all-abstain risk-coverage: nothing to compute a risk over
        rc_none = M.risk_coverage([None, None], [1, 5], [0.9, 0.1])
        assert rc_none["aurc"] is None, rc_none
        assert all(pt["risk"] is None and pt["n_scored"] == 0 for pt in rc_none["curve"]), rc_none
        assert all(v is None for v in rc_none["risk_at"].values()), rc_none

        # single-class gold with a real spread of predictions
        single = M.binary_metrics([1, 2, 3], [2, 2, 2])
        assert single["n_pos"] == 0 and single["auroc"] is None, single
        assert single["f1_at_threshold"] == 0.0, single

        assert M.bootstrap_ci(M.pearson, [1, 2], [1, 2], n_resamples=0)["n_resamples"] == 0
        assert M.lexical_match("", GOLD_RULE) is False
        assert M.content_words("!!! ???") == set()
    print("  degenerate battery ok: no exceptions and no warnings escaped")


def main() -> int:
    cases = [
        ("test_correlations_hand_computed", test_correlations_hand_computed),
        ("test_abstentions", test_abstentions_excluded_but_counted),
        ("test_length_mismatch", test_length_mismatch_raises),
        ("test_binary_metrics", test_binary_metrics_known_points),
        ("test_risk_coverage", test_risk_coverage_rewards_good_abstention),
        ("test_abstention_ranked_last", test_abstention_is_ranked_last_whatever_it_claims),
        ("test_curve_thinning", test_risk_coverage_curve_is_thinned_but_aurc_is_not),
        ("test_open_discovery", test_open_discovery_paraphrase_and_near_miss),
        ("test_open_discovery_one_to_one", test_open_discovery_is_one_to_one),
        ("test_cost_curve", test_cost_curve_buckets),
        ("test_bootstrap", test_bootstrap_is_deterministic_and_brackets_the_point),
        ("test_summarise", test_summarise_is_consistent_with_its_parts),
        ("test_degenerate_inputs", test_degenerate_inputs),
    ]
    for name, fn in cases:
        print(name)
        fn()
    print("\nALL EVAL METRICS TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
