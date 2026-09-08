"""Offline tests for eval/runner.py: the batch layer a 3400-video run leans on.

No network, no API key, no LLM: the judge is a deterministic fake that counts
how many times each id was judged, which is the only way to prove that resume
skips exactly the finished rows and retries exactly the failed ones.

What this pins down:
  - a clean run writes one record per sample and nothing else
  - resume skips completed ids, and `limit` caps this run's work rather than
    truncating the input list
  - an exception becomes an error record, is counted in `failed`, and is retried
    on the next run until it succeeds -- and then stops being retried
  - an `error` that carries a usable score (the baselines' soft notes) is NOT a
    failure, so a resume converges instead of re-judging for ever
  - a truncated last line from a killed run is survived on read and isolated on
    the next append
  - workers=4 writes every record exactly once; workers=1 spawns no pool
  - join_with_gold: inner join, dataset order, exact columns and dtypes, and
    missing fields becoming None rather than KeyError
"""

from __future__ import annotations

import json
import sys
import threading
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from eval.runner import (  # noqa: E402
    RunStats,
    completed_ids,
    failed_ids,
    is_failure,
    join_with_gold,
    load_results,
    results_frame,
    run_batch,
)

MODELS = ("wan", "cosmos", "sora")

JOIN_COLUMNS = [
    # Kept as a literal on purpose: the join schema is what every downstream
    # metric reads, so a silent change to it should break a test.
    "video_id",
    "pc",
    "sa",
    "is_hard",
    "model_name",
    # gold diagnosis -- open_discovery_match compares against these
    "human_violated_rules",
    "rules_unfollowed",
    "caption",
    # prediction
    "pred",
    "confidence",
    "abstain",
    "score_imputed",
    "fatal",
    # our diagnosis
    "n_violations",
    "violation_descriptions",
    "n_failed_sa",
    "n_failed_pc",
    "n_not_shown",
    "n_tool_calls",
    "n_evidence",
    # cost: rounds and cache_hits carry the adaptive-budget story
    "frames",
    "rounds",
    "prompt_tokens",
    "completion_tokens",
    "llm_calls",
    "cache_hits",
    "error",
]


# --------------------------------------------------------------------------
# fakes
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class FakeSample:
    """The slice of eval.dataset.Sample that the runner and the join touch."""

    video_id: str
    caption: str
    pc: int
    sa: int
    is_hard: bool
    model_name: str


class FakeDataset:
    """Exposes `id_to_sample()` like VideoPhy2Dataset, and is iterable."""

    def __init__(self, samples):
        self._samples = list(samples)

    def __iter__(self):
        return iter(self._samples)

    def __len__(self):
        return len(self._samples)

    def id_to_sample(self):
        return {s.video_id: s for s in self._samples}


def make_samples(n: int, start: int = 0) -> list[FakeSample]:
    out = []
    for i in range(start, start + n):
        out.append(
            FakeSample(
                video_id=f"v{i:03d}",
                caption=f"caption {i}",
                pc=1 + (i % 5),
                sa=1 + ((i + 2) % 5),
                is_hard=bool(i % 2),
                model_name=MODELS[i % len(MODELS)],
            )
        )
    return out


def expected_pred(sample: FakeSample) -> float:
    """Independent formula for what the fake judge will score a sample."""
    return 1.0 + (int(sample.video_id[1:]) % 5)


class RecordingJudge:
    """Deterministic fake judge that records how it was called.

    Thread-safe on purpose: run_batch calls it from several threads and the
    counters are the evidence for the once-and-only-once claims.
    """

    def __init__(self, fail_ids=(), bad_return_ids=(), sleep: float = 0.0):
        self.fail_ids = set(fail_ids)
        self.bad_return_ids = set(bad_return_ids)
        self.sleep = sleep
        self.calls: Counter[str] = Counter()
        self.threads: set[int] = set()
        self.inflight = 0
        self.max_inflight = 0
        self._lock = threading.Lock()

    def __call__(self, sample):
        with self._lock:
            self.calls[sample.video_id] += 1
            self.threads.add(threading.current_thread().ident)
            self.inflight += 1
            self.max_inflight = max(self.max_inflight, self.inflight)
        try:
            if self.sleep:
                time.sleep(self.sleep)
            if sample.video_id in self.fail_ids:
                raise RuntimeError(f"boom on {sample.video_id}")
            if sample.video_id in self.bad_return_ids:
                return ["not", "a", "dict"]
            return {
                "video_id": sample.video_id,
                "pc_score": expected_pred(sample),
                "confidence": 0.7,
                "abstain": False,
                "score_imputed": False,
                "frames": 12,
                "prompt_tokens": 100,
                "completion_tokens": 20,
                "llm_calls": 3,
            }
        finally:
            with self._lock:
                self.inflight -= 1


def raw_lines(path: Path) -> list[str]:
    return [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def parsed_ids(path: Path) -> list[str]:
    return [r["video_id"] for r in load_results(path, quiet=True)]


# --------------------------------------------------------------------------
# tests
# --------------------------------------------------------------------------


def test_clean_run(tmp: Path) -> None:
    out = tmp / "clean.jsonl"
    samples = make_samples(10)
    judge = RecordingJudge()

    stats = run_batch(samples, judge, out, workers=1, progress=False)

    assert isinstance(stats, RunStats)
    d = stats.as_dict()
    assert set(d) == {"total", "done", "skipped", "failed", "wall_seconds"}, d
    assert (d["total"], d["done"], d["skipped"], d["failed"]) == (10, 10, 0, 0), d
    assert d["wall_seconds"] >= 0.0 and d["wall_seconds"] < 60.0, d
    assert stats.total == stats.done + stats.skipped + stats.failed
    assert stats.attempted == 10

    assert len(raw_lines(out)) == 10
    records = load_results(out, quiet=True)
    assert len(records) == 10
    assert [r["video_id"] for r in records] == [s.video_id for s in samples]
    assert records[3]["pc_score"] == expected_pred(samples[3]) == 4.0
    assert judge.calls == Counter({s.video_id: 1 for s in samples})

    assert completed_ids(out) == {s.video_id for s in samples}
    assert failed_ids(out) == set()

    # workers=1 must not spawn a pool: everything ran on the calling thread.
    assert judge.threads == {threading.main_thread().ident}, judge.threads
    print(f"  10 records, one call each, no pool: {d}")


def test_limit_caps_this_run(tmp: Path) -> None:
    out = tmp / "limit.jsonl"
    samples = make_samples(10)

    first = run_batch(samples, RecordingJudge(), out, workers=1, limit=3, progress=False)
    assert (first.total, first.done, first.skipped, first.failed) == (3, 3, 0, 0)
    assert parsed_ids(out) == ["v000", "v001", "v002"]

    second = run_batch(samples, RecordingJudge(), out, workers=1, limit=3, progress=False)
    # `limit` is three more videos, not the first three of the input again.
    assert (second.total, second.done, second.skipped, second.failed) == (6, 3, 3, 0)
    assert parsed_ids(out) == ["v000", "v001", "v002", "v003", "v004", "v005"]

    zero = run_batch(samples, RecordingJudge(), out, workers=1, limit=0, progress=False)
    assert (zero.total, zero.done, zero.skipped) == (0, 0, 0)
    assert len(raw_lines(out)) == 6
    print("  limit=3 twice -> 6 distinct rows; limit=0 is a no-op")


def test_resume_skips_and_extends(tmp: Path) -> None:
    out = tmp / "resume.jsonl"
    first = make_samples(10)
    judge_a = RecordingJudge()
    run_batch(first, judge_a, out, workers=1, progress=False)

    both = make_samples(15)
    judge_b = RecordingJudge()
    stats = run_batch(both, judge_b, out, workers=2, progress=False)

    assert (stats.total, stats.done, stats.skipped, stats.failed) == (15, 5, 10, 0)
    assert set(judge_b.calls) == {f"v{i:03d}" for i in range(10, 15)}
    assert all(v == 1 for v in judge_b.calls.values())
    assert len(raw_lines(out)) == 15
    ids = parsed_ids(out)
    assert len(ids) == len(set(ids)) == 15
    assert completed_ids(out) == {s.video_id for s in both}
    print("  resume: 10 skipped, 5 run, 15 unique rows")


def test_failures_are_data_then_retried(tmp: Path) -> None:
    out = tmp / "failures.jsonl"
    samples = make_samples(12)
    broken = {"v000", "v003", "v006", "v009"}

    judge_a = RecordingJudge(fail_ids=broken)
    first = run_batch(samples, judge_a, out, workers=2, progress=False)
    assert (first.total, first.done, first.skipped, first.failed) == (12, 8, 0, 4), first
    assert len(raw_lines(out)) == 12

    records = {r["video_id"]: r for r in load_results(out, quiet=True)}
    assert len(records) == 12
    for vid in sorted(broken):
        rec = records[vid]
        assert rec["error"] == f"RuntimeError: boom on {vid}", rec["error"]
        assert "raise RuntimeError" in rec["traceback"], rec["traceback"][:200]
        assert "pc_score" not in rec
        assert is_failure(rec) is True
    assert is_failure(records["v001"]) is False

    assert completed_ids(out) == {s.video_id for s in samples} - broken
    assert failed_ids(out) == broken

    # A run over the same samples must retry exactly the four broken rows.
    judge_b = RecordingJudge()
    second = run_batch(samples, judge_b, out, workers=2, progress=False)
    assert (second.total, second.done, second.skipped, second.failed) == (12, 4, 8, 0), second
    assert set(judge_b.calls) == broken
    assert all(v == 1 for v in judge_b.calls.values())

    assert len(raw_lines(out)) == 16
    assert failed_ids(out) == set()
    raw = results_frame(out)
    assert len(raw) == 16
    assert int(raw["error"].notna().sum()) == 4  # the run log keeps the failures

    # A third run has nothing left to do: a fixed row is not retried again.
    judge_c = RecordingJudge()
    third = run_batch(samples, judge_c, out, workers=2, progress=False)
    assert (third.total, third.done, third.skipped, third.failed) == (12, 0, 12, 0), third
    assert judge_c.calls == Counter()
    assert len(raw_lines(out)) == 16

    # The joined table sees one row per video, and the retried ones are clean.
    frame = join_with_gold(out, FakeDataset(samples))
    assert len(frame) == 12
    assert frame["error"].isna().all()
    assert frame["pred"].notna().all()
    assert list(frame["pred"]) == [expected_pred(s) for s in samples]
    print("  4 failures counted, retried once each, then left alone")


def test_bad_return_type_is_an_error_record(tmp: Path) -> None:
    out = tmp / "badreturn.jsonl"
    samples = make_samples(2)
    judge = RecordingJudge(bad_return_ids={"v001"})

    stats = run_batch(samples, judge, out, workers=1, progress=False)
    assert (stats.done, stats.failed) == (1, 1), stats
    records = {r["video_id"]: r for r in load_results(out, quiet=True)}
    assert records["v001"]["error"].startswith("TypeError: judge_fn must return a dict")
    assert failed_ids(out) == {"v001"}
    print("  a non-dict return is an error record, not a crash")


def test_soft_error_note_is_not_a_failure(tmp: Path) -> None:
    """The baselines put clamping notes in `error` beside a valid score."""
    out = tmp / "soft.jsonl"
    soft = {
        "video_id": "v000",
        "pc_score": 5.0,
        "error": "score 7 out of range; clamped to 5",
    }
    fatal = {
        "video_id": "v001",
        "pc_score": None,
        "confidence": 0.0,
        "frames": 16,
        "error": "llm call failed: TimeoutError: read timed out",
    }
    abstained = {"video_id": "v002", "pc_score": None, "abstain": True}
    out.write_text("".join(json.dumps(r) + "\n" for r in (soft, fatal, abstained)))

    assert is_failure(soft) is False
    assert is_failure(fatal) is True
    assert is_failure(abstained) is False
    assert completed_ids(out) == {"v000", "v002"}
    assert failed_ids(out) == {"v001"}

    judge = RecordingJudge()
    stats = run_batch(make_samples(3), judge, out, workers=1, progress=False)
    assert (stats.total, stats.done, stats.skipped, stats.failed) == (3, 1, 2, 0), stats
    assert set(judge.calls) == {"v001"}
    print("  soft note kept, dead endpoint retried, abstention left alone")


def test_corrupt_trailing_line_is_survived(tmp: Path) -> None:
    out = tmp / "corrupt.jsonl"
    samples = make_samples(5)
    run_batch(samples[:4], RecordingJudge(), out, workers=1, progress=False)

    # Simulate a kill mid-write: a truncated line with no terminating newline.
    with out.open("a", encoding="utf-8") as fh:
        fh.write('{"video_id": "v900", "pc_sc')

    assert len(load_results(out, quiet=True)) == 4
    assert completed_ids(out) == {s.video_id for s in samples[:4]}

    judge = RecordingJudge()
    stats = run_batch(samples, judge, out, workers=1, progress=False)
    assert (stats.total, stats.done, stats.skipped, stats.failed) == (5, 1, 4, 0), stats
    assert set(judge.calls) == {"v004"}

    lines = raw_lines(out)
    assert len(lines) == 6  # 4 good, 1 fragment, 1 appended after it
    good, bad = 0, 0
    for line in lines:
        try:
            json.loads(line)
            good += 1
        except ValueError:
            bad += 1
    assert (good, bad) == (5, 1), (good, bad)
    assert json.loads(lines[-1])["video_id"] == "v004"  # the append was not glued on
    assert sorted(parsed_ids(out)) == ["v000", "v001", "v002", "v003", "v004"]
    print("  truncated line isolated; the next append is still valid json")


def test_workers_write_every_record_once(tmp: Path) -> None:
    out = tmp / "parallel.jsonl"
    samples = make_samples(20)
    judge = RecordingJudge(sleep=0.02)

    stats = run_batch(samples, judge, out, workers=4, progress=False)
    assert (stats.total, stats.done, stats.skipped, stats.failed) == (20, 20, 0, 0), stats

    ids = parsed_ids(out)
    assert len(ids) == 20
    assert sorted(ids) == [s.video_id for s in samples]
    assert judge.calls == Counter({s.video_id: 1 for s in samples})
    # Prove the pool really overlapped work; the write path is what must not.
    assert judge.max_inflight >= 2, judge.max_inflight
    assert len(judge.threads) >= 2, judge.threads
    print(f"  20 rows exactly once with 4 workers (max {judge.max_inflight} in flight)")


def test_no_resume_duplicates_but_join_dedupes(tmp: Path) -> None:
    out = tmp / "noresume.jsonl"
    samples = make_samples(6)
    run_batch(samples, RecordingJudge(), out, workers=1, resume=False, progress=False)
    stats = run_batch(samples, RecordingJudge(), out, workers=1, resume=False, progress=False)

    assert (stats.total, stats.done, stats.skipped) == (6, 6, 0), stats
    assert len(raw_lines(out)) == 12
    assert len(results_frame(out)) == 12
    frame = join_with_gold(out, FakeDataset(samples))
    assert len(frame) == 6
    print("  resume=False duplicates rows; the join keeps one per video")


def test_duplicate_ids_within_one_call(tmp: Path) -> None:
    out = tmp / "dupes.jsonl"
    samples = make_samples(3)
    judge = RecordingJudge()
    stats = run_batch(samples + samples, judge, out, workers=1, progress=False)
    assert (stats.total, stats.done, stats.skipped) == (6, 3, 3), stats
    assert judge.calls == Counter({s.video_id: 1 for s in samples})
    print("  a repeated sample in one call is judged once")


def test_join_with_gold(tmp: Path) -> None:
    samples = make_samples(6)
    dataset = FakeDataset(samples)
    records = [
        {
            "video_id": "v000",
            "pc_score": 4.0,
            "confidence": 0.8,
            "abstain": False,
            "score_imputed": False,
            "frames": 12,
            "prompt_tokens": 100,
            "completion_tokens": 20,
            "llm_calls": 3,
        },
        # abstention: no score, no error, and cost nested the way Verdict writes it
        {
            "video_id": "v001",
            "pc_score": None,
            "confidence": 0.2,
            "abstain": True,
            "score_imputed": False,
            "cost": {
                "frames": 7,
                "prompt_tokens": 50,
                "completion_tokens": 5,
                "llm_calls": 2,
            },
        },
        # a record with almost nothing in it must not raise
        {"video_id": "v002"},
        # a failure superseded by a later success for the same id
        {"video_id": "v003", "error": "RuntimeError: boom", "traceback": "..."},
        {
            "video_id": "v003",
            "pc_score": 2.0,
            "confidence": 0.5,
            "abstain": False,
            "score_imputed": True,
            "frames": 9,
            "prompt_tokens": 80,
            "completion_tokens": 10,
            "llm_calls": 2,
        },
        # an unrecoverable row stays in the table, with its error
        {"video_id": "v004", "pc_score": None, "error": "llm call failed: Timeout"},
        # judged but not in the gold set -> dropped by the inner join
        {"video_id": "v999", "pc_score": 3.0},
        # v005 is in gold with no record -> also dropped
    ]

    frame = join_with_gold(records, dataset)

    assert list(frame.columns) == JOIN_COLUMNS, list(frame.columns)
    assert list(frame["video_id"]) == ["v000", "v001", "v002", "v003", "v004"]

    assert list(frame["pc"]) == [1, 2, 3, 4, 5]
    assert list(frame["sa"]) == [3, 4, 5, 1, 2]
    assert list(frame["is_hard"]) == [False, True, False, True, False]
    assert list(frame["model_name"]) == ["wan", "cosmos", "sora", "wan", "cosmos"]

    preds = list(frame["pred"])
    assert preds[0] == 4.0 and preds[3] == 2.0
    assert np.isnan(preds[1]) and np.isnan(preds[2]) and np.isnan(preds[4])
    assert list(frame["confidence"])[:2] == [0.8, 0.2]

    # nested cost is read, missing cost becomes NaN
    assert list(frame["frames"])[:2] == [12.0, 7.0]
    assert np.isnan(frame["frames"].iloc[2]) and np.isnan(frame["frames"].iloc[4])
    assert frame["llm_calls"].iloc[3] == 2.0

    errors = list(frame["error"])
    assert errors[3] is None, errors[3]  # the retry's success replaced the failure
    assert errors[4] == "llm call failed: Timeout"
    assert frame["error"].isna().sum() == 4

    assert list(frame["abstain"]) == [False, True, None, False, None]
    assert list(frame["score_imputed"]) == [False, False, None, True, None]

    dtypes = {c: str(frame[c].dtype) for c in frame.columns}
    assert dtypes["pc"] == "int64" and dtypes["sa"] == "int64", dtypes
    assert dtypes["is_hard"] == "bool", dtypes
    assert dtypes["pred"] == "float64" and dtypes["confidence"] == "float64", dtypes
    assert dtypes["frames"] == "float64", dtypes
    assert dtypes["prompt_tokens"] == "float64", dtypes
    assert dtypes["abstain"] == "object" and dtypes["error"] == "object", dtypes
    assert dtypes["video_id"] == "object", dtypes

    # A complete cost column with no holes stays integral.
    complete = join_with_gold(
        [
            {"video_id": "v000", "pc_score": 4.0, "frames": 12, "llm_calls": 3},
            {"video_id": "v001", "pc_score": 3.0, "frames": 8, "llm_calls": 2},
        ],
        dataset,
    )
    assert str(complete["frames"].dtype) == "int64", complete.dtypes.to_dict()

    # Empty results still produce the table shape downstream code indexes into.
    empty = join_with_gold([], dataset)
    assert list(empty.columns) == JOIN_COLUMNS and len(empty) == 0
    print("  join: 5 of 6 rows, exact columns, dtypes, no KeyError")


def test_join_with_gold_duck_typed_datasets(tmp: Path) -> None:
    samples = make_samples(4)
    records = [
        {"video_id": s.video_id, "pc_score": expected_pred(s), "frames": 10}
        for s in samples
    ]
    reference = join_with_gold(records, FakeDataset(samples))

    as_list = join_with_gold(records, list(samples))
    as_map = join_with_gold(records, {s.video_id: s for s in samples})
    as_dicts = join_with_gold(records, [vars(s) for s in samples])
    as_frame = join_with_gold(records, pd.DataFrame([vars(s) for s in samples]))

    for name, other in (
        ("list", as_list),
        ("mapping", as_map),
        ("list-of-dicts", as_dicts),
        ("dataframe", as_frame),
    ):
        pd.testing.assert_frame_equal(reference, other, obj=name)

    assert list(reference["pred"]) == [expected_pred(s) for s in samples]
    assert join_with_gold(records, None).empty
    print("  gold accepted as dataset, list, mapping, dicts or frame")


def test_progress_and_id_attr(tmp: Path) -> None:
    """The tqdm/resume-print path runs, and a non-default id column works."""
    out = tmp / "progress.jsonl"

    @dataclass(frozen=True)
    class Clip:
        clip_id: str
        pc: int

    clips = [Clip(f"c{i}", 1 + i) for i in range(4)]

    def judge(clip):
        return {"clip_id": clip.clip_id, "pc_score": float(clip.pc)}

    first = run_batch(clips, judge, out, workers=1, progress=True, id_attr="clip_id")
    second = run_batch(clips, judge, out, workers=2, progress=True, id_attr="clip_id")
    assert (first.done, first.skipped) == (4, 0)
    assert (second.done, second.skipped) == (0, 4), second
    assert completed_ids(out, "clip_id") == {"c0", "c1", "c2", "c3"}

    frame = join_with_gold(out, clips, id_attr="clip_id")
    assert list(frame.columns)[0] == "clip_id"
    assert list(frame["pred"]) == [1.0, 2.0, 3.0, 4.0]
    assert list(frame["pc"]) == [1, 2, 3, 4]
    print("  progress path and a custom id column both work")


def test_id_is_stamped_from_the_sample(tmp: Path) -> None:
    """Resume matches on the runner's id, so the record must carry it."""
    out = tmp / "stamp.jsonl"
    samples = make_samples(2)

    def judge(sample):
        if sample.video_id == "v000":
            return {"pc_score": 3.0}  # forgot the id entirely
        return {"video_id": "something-else", "pc_score": 4.0}  # disagrees

    stats = run_batch(samples, judge, out, workers=1, progress=False)
    assert (stats.done, stats.failed) == (2, 0)
    records = {r["video_id"]: r for r in load_results(out, quiet=True)}
    assert set(records) == {"v000", "v001"}
    assert records["v001"]["reported_id"] == "something-else"
    assert completed_ids(out) == {"v000", "v001"}
    print("  ids stamped from the sample; a disagreement is kept, not lost")


_KILLED_WORKER = '''
import sys, time
sys.path.insert(0, {root!r})
from eval.runner import run_batch

class S:
    def __init__(self, i):
        self.video_id = "v%03d" % i

def judge(sample):
    time.sleep(0.05)
    return {{"video_id": sample.video_id, "pc_score": 3.0, "pad": "x" * 4000}}

run_batch([S(i) for i in range(400)], judge, {out!r}, workers=4, progress=False)
'''


def test_sigkill_leaves_a_valid_file(tmp: Path) -> None:
    """The property the whole write path exists for, tested for real.

    A child process is SIGKILLed mid-run -- no cleanup, no flush on exit -- and
    every complete line it left must still be valid json and resumable.
    """
    import os
    import signal
    import subprocess

    out = tmp / "killed.jsonl"
    script = tmp / "killed_worker.py"
    root = str(Path(__file__).resolve().parents[1])
    script.write_text(_KILLED_WORKER.format(root=root, out=str(out)))

    proc = subprocess.Popen([sys.executable, "-u", str(script)])
    try:
        deadline = time.time() + 20.0
        while time.time() < deadline:
            if out.exists() and len(raw_lines(out)) >= 5:
                break
            time.sleep(0.05)
        os.kill(proc.pid, signal.SIGKILL)
    finally:
        proc.wait(timeout=20)

    lines = raw_lines(out)
    assert len(lines) >= 5, len(lines)
    for line in lines:
        json.loads(line)  # no partial write survived, not even the last one
    written = completed_ids(out)
    assert len(written) == len(lines)

    judge = RecordingJudge()
    samples = make_samples(400)
    stats = run_batch(samples, judge, out, workers=4, progress=False)
    assert stats.total == 400
    assert stats.skipped == len(written)
    assert stats.done == 400 - len(written)
    assert stats.failed == 0
    assert set(judge.calls).isdisjoint(written)  # nothing was judged twice
    assert len(completed_ids(out)) == 400
    print(f"  SIGKILL after {len(lines)} rows: file valid, resume finished the rest")


def test_missing_output_file_and_empty_inputs(tmp: Path) -> None:
    absent = tmp / "nested" / "not_written_yet.jsonl"
    assert load_results(absent) == []
    assert completed_ids(absent) == set()
    assert results_frame(absent).empty

    stats = run_batch([], RecordingJudge(), absent, workers=4, progress=False)
    assert stats.as_dict()["total"] == 0
    assert not absent.exists()  # nothing to say, nothing written
    print("  absent file and empty sample list are both non-events")


def main() -> int:
    import tempfile

    tests = [
        test_clean_run,
        test_limit_caps_this_run,
        test_resume_skips_and_extends,
        test_failures_are_data_then_retried,
        test_bad_return_type_is_an_error_record,
        test_soft_error_note_is_not_a_failure,
        test_corrupt_trailing_line_is_survived,
        test_workers_write_every_record_once,
        test_no_resume_duplicates_but_join_dedupes,
        test_duplicate_ids_within_one_call,
        test_join_with_gold,
        test_join_with_gold_duck_typed_datasets,
        test_progress_and_id_attr,
        test_id_is_stamped_from_the_sample,
        test_sigkill_leaves_a_valid_file,
        test_missing_output_file_and_empty_inputs,
    ]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for fn in tests:
            print(fn.__name__)
            fn(tmp)
    print(f"\nALL {len(tests)} EVAL RUNNER TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
