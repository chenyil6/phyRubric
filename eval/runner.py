"""Batch execution of a judge over a dataset, built to survive a long run.

A full VideoPhy-2 pass is 3397 videos of paid API calls taking hours, so the run
is assumed to die halfway: the endpoint rate-limits, a clip fails to decode, the
machine is rebooted. Three properties follow from that assumption and they are
the whole reason this module exists.

1. A failure is data. An exception from `judge_fn` becomes a record with an
   `error` and a traceback, written like any other, so one dead video cannot end
   a run and cannot vanish from the accounting either.
2. Resume is exact. Ids already answered are skipped; ids whose only record is a
   failure are judged again. A transient 500 must not become a permanent hole in
   the results, which is what a plain "skip everything already in the file"
   resume would make it.
3. A kill leaves a valid file. Records are appended one line at a time, flushed
   and fsynced under a lock, and the file is never rewritten. Whatever survived
   the kill is readable, and a half-written last line is tolerated on read and
   isolated on the next append.

The one subtlety worth reading twice is `is_failure`: `error` is not a boolean
"this row is broken" flag, because the baselines also use it for soft notes (a
clamped score, a score recovered from prose) beside a perfectly good score.
Retrying those would mean every resume re-judges them for ever.
"""

from __future__ import annotations

import json
import math
import os
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

import numpy as np
import pandas as pd
from tqdm import tqdm

# Where a prediction may live in a result record, in order of preference. Used
# only to decide whether an errored record still carries a usable answer.
SCORE_KEYS = ("pc_score", "pred", "score")

# Cost fields the results table wants flattened; each may also arrive nested
# under a "cost" object, which is how Verdict.as_dict writes it.
COST_FIELDS = (
    "frames",
    "rounds",          # adaptive-budget evidence: how many probes were spent
    "prompt_tokens",
    "completion_tokens",
    "llm_calls",
    "cache_hits",      # without it the table cannot say whether cost was paid
)

_GOLD_FIELDS = ("pc", "sa", "is_hard", "model_name")
# Diagnosis columns. Scoring the number is only half the comparison: the
# violations we report and the violations humans wrote in by hand are what
# metrics.open_discovery_match consumes, and a join that drops them makes the
# whole diagnosis side of the evaluation unreachable.
_DIAGNOSIS_FIELDS = (
    "n_violations",
    "violation_descriptions",
    "n_failed_sa",
    "n_failed_pc",
    "n_not_shown",
    "n_tool_calls",
    "n_evidence",
)
_GOLD_DIAGNOSIS_FIELDS = ("human_violated_rules", "rules_unfollowed", "caption")
_PRED_FIELDS = (
    "pred",
    "confidence",
    "abstain",
    "score_imputed",
    "fatal",
)
_NUMERIC_COLUMNS = (
    ("pc", "sa", "pred", "confidence")
    + COST_FIELDS
    + ("n_violations", "n_failed_sa", "n_failed_pc", "n_not_shown", "n_tool_calls", "n_evidence")
)
_BOOLEAN_COLUMNS = ("is_hard", "abstain", "score_imputed")


# --------------------------------------------------------------------------
# small duck-typed accessors
# --------------------------------------------------------------------------


def _field(obj: Any, name: str) -> Any:
    """Read `name` off a mapping or an object; None when it is not there."""
    if isinstance(obj, Mapping):
        return obj.get(name)
    return getattr(obj, name, None)


def sample_id(sample: Any, id_attr: str = "video_id") -> str | None:
    """The id a sample will be filed under, or None if it carries none.

    A sample without an id can still be judged, but it cannot be resumed: there
    is nothing to match against the output file.
    """
    value = _field(sample, id_attr)
    return None if value is None else str(value)


def _first_present(record: Mapping[str, Any], keys: Sequence[str]) -> Any:
    """Value of the first key that exists, even if that value is None.

    `pc_score: None` means "abstained", which is an answer; falling through to
    another key would silently invent a score for it.
    """
    for key in keys:
        if key in record:
            return record[key]
    return None


def _cost_field(record: Mapping[str, Any], key: str) -> Any:
    if key in record:
        return record[key]
    cost = record.get("cost")
    if isinstance(cost, Mapping):
        return cost.get(key)
    return None


def _finite(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


# --------------------------------------------------------------------------
# what counts as unfinished
# --------------------------------------------------------------------------


def is_failure(record: Mapping[str, Any], id_attr: str = "video_id") -> bool:
    """True when this record must be judged again on the next run.

    A record has failed when it reports a non-empty `error` *and* carries no
    usable score beside it. Both halves are load-bearing:

      - the baselines write soft notes into `error` ("score read from prose",
        "clamped to 5") next to a valid score; treating those as failures would
        make every resume re-judge them and never converge
      - a dead endpoint or an undecodable file leaves `error` set and the score
        None, and that is exactly the transient hole resume exists to fill

    Abstention is not failure: it has no score, but no error either.
    """
    if not str(record.get("error") or "").strip():
        return False
    return not any(_finite(record.get(key)) for key in SCORE_KEYS)


# --------------------------------------------------------------------------
# reading the output file
# --------------------------------------------------------------------------


@dataclass
class _Scan:
    """What one pass over an existing output file tells us."""

    done: set[str]
    failed: set[str]
    n_records: int
    bad_lines: int


def _read_lines(path: str | Path) -> tuple[list[dict[str, Any]], int]:
    """Every parseable record, plus the count of lines that were not.

    A process killed mid-write leaves a truncated last line. That is expected,
    not corruption to raise on, so unparseable lines are counted and dropped.
    """
    p = Path(path)
    if not p.exists():
        return [], 0
    records: list[dict[str, Any]] = []
    bad = 0
    with p.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except ValueError:
                bad += 1
                continue
            if isinstance(obj, dict):
                records.append(obj)
            else:
                bad += 1
    return records, bad


def load_results(path: str | Path, quiet: bool = False) -> list[dict[str, Any]]:
    """All records in a results jsonl, in file order, bad lines skipped.

    Duplicates are kept: a retried video legitimately appears twice, and hiding
    that here would hide how much of a run was re-judged.
    """
    records, bad = _read_lines(path)
    if bad and not quiet:
        print(
            f"runner: {Path(path).name}: skipped {bad} unparseable line(s)",
            file=sys.stderr,
        )
    return records


def _scan(path: str | Path, id_attr: str = "video_id") -> _Scan:
    records, bad = _read_lines(path)
    done: set[str] = set()
    failed: set[str] = set()
    for record in records:
        vid = record.get(id_attr)
        if vid is None:
            continue
        vid = str(vid)
        if is_failure(record, id_attr):
            failed.add(vid)
        else:
            done.add(vid)
    return _Scan(done=done, failed=failed, n_records=len(records), bad_lines=bad)


def completed_ids(path: str | Path, id_attr: str = "video_id") -> set[str]:
    """Ids that need no further work: at least one non-failed record exists.

    A successful record wins over a failed one for the same id, whichever came
    first, so a retry that worked is never repeated.
    """
    return _scan(path, id_attr).done


def failed_ids(path: str | Path, id_attr: str = "video_id") -> set[str]:
    """Ids whose every record is a failure -- the rows a resume will retry."""
    scan = _scan(path, id_attr)
    return scan.failed - scan.done


# --------------------------------------------------------------------------
# writing the output file
# --------------------------------------------------------------------------


class _JsonlWriter:
    """Append-only jsonl sink: one line per record, durable and thread-safe.

    Each record is serialised outside the lock and written, flushed and fsynced
    inside it, so concurrent workers cannot interleave halves of two lines and a
    kill at any instant leaves every complete line valid. The file is never
    rewritten -- rewriting is what turns a kill into total data loss.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._lock = threading.Lock()
        self._terminate_partial_line(self.path)
        self._fh = self.path.open("a", encoding="utf-8")

    @staticmethod
    def _terminate_partial_line(path: Path) -> None:
        """Close off a half-written last line before appending after it.

        Without this, the first append glues onto the truncated fragment and
        destroys a good record as well as the bad one.
        """
        if not path.exists() or path.stat().st_size == 0:
            return
        with path.open("rb") as fh:
            fh.seek(-1, os.SEEK_END)
            last = fh.read(1)
        if last != b"\n":
            with path.open("ab") as fh:
                fh.write(b"\n")
                fh.flush()
                os.fsync(fh.fileno())

    def write(self, record: Mapping[str, Any]) -> None:
        # allow_nan=False: bare NaN/Infinity is not valid JSON, and a results
        # file that only this interpreter can read is not a results file.
        line = json.dumps(record, ensure_ascii=False, default=str, allow_nan=False)
        with self._lock:
            self._fh.write(line + "\n")
            self._fh.flush()
            os.fsync(self._fh.fileno())

    def close(self) -> None:
        with self._lock:
            if not self._fh.closed:
                self._fh.close()


# --------------------------------------------------------------------------
# the run
# --------------------------------------------------------------------------


@dataclass
class RunStats:
    """Accounting for one invocation of `run_batch`.

    `total == done + skipped + failed` always holds, which is what makes a
    partially finished run readable: nothing is attempted and unaccounted for.
    """

    total: int = 0
    done: int = 0
    skipped: int = 0
    failed: int = 0
    wall_seconds: float = 0.0

    @property
    def attempted(self) -> int:
        return self.done + self.failed

    def as_dict(self) -> dict[str, float | int]:
        return {
            "total": self.total,
            "done": self.done,
            "skipped": self.skipped,
            "failed": self.failed,
            "wall_seconds": round(self.wall_seconds, 3),
        }


def _to_record(value: Any) -> dict[str, Any]:
    """Coerce whatever `judge_fn` returned into a record, or refuse loudly."""
    if isinstance(value, Mapping):
        return dict(value)
    as_dict = getattr(value, "as_dict", None)
    if callable(as_dict):
        out = as_dict()
        if isinstance(out, Mapping):
            return dict(out)
    raise TypeError(f"judge_fn must return a dict, got {type(value).__name__}")


def _stamp_id(record: dict[str, Any], vid: str | None, id_attr: str) -> dict[str, Any]:
    """Guarantee the record is filed under the id the runner planned it with.

    Resume matches on this field, so a record carrying some other id would be
    re-judged on every restart. A disagreement is kept as `reported_id` rather
    than dropped, since it means the judge and the dataset disagree about what
    it just looked at.
    """
    if vid is None:
        return record
    reported = record.get(id_attr)
    if reported is not None and str(reported) != vid:
        record["reported_id"] = reported
    record[id_attr] = vid
    return record


def run_batch(
    samples: Sequence[Any],
    judge_fn: Callable[[Any], dict],
    out_path: str | Path,
    workers: int = 4,
    resume: bool = True,
    limit: int | None = None,
    progress: bool = True,
    id_attr: str = "video_id",
) -> RunStats:
    """Judge every sample, appending one json record per line to `out_path`.

    `judge_fn(sample)` returns a JSON-serialisable dict (or anything with an
    `as_dict()`); the runner stamps the sample's id into it under `id_attr`. If
    it raises, a record `{id_attr, "error", "traceback"}` is written instead, so
    the row is a visible failure rather than a lost one.

    Thread safety: `judge_fn` is called from `workers` threads at once and must
    be safe under that. In particular an `LLMClient` accumulates usage counters,
    so a judge that reads per-video cost off a shared client will attribute
    other videos' tokens to this one -- build one judge per thread (see
    `scripts/run_eval.py::PerThreadJudge`).

    `resume=True` skips ids that already have a non-failed record in the file
    and re-judges ids whose only records are failures. `resume=False` judges
    everything again, appending duplicate records; `join_with_gold` keeps the
    last good record per id, so duplicates skew nothing downstream.

    `limit` caps the work done by *this* invocation, not the input list: with a
    resumed file, `limit=10` means ten more videos, which is what makes it
    useful for a smoke test against a half-finished run. Scanning stops once the
    cap is reached, so `total` counts the plan (skips seen plus work attempted),
    not the whole of `samples`.

    Output line order is not meaningful under concurrency and nothing may depend
    on it; read the file back with `load_results` or `results_frame`.
    """
    started = time.perf_counter()
    out = Path(out_path)
    if str(out.parent) not in ("", "."):
        out.parent.mkdir(parents=True, exist_ok=True)
    workers = max(1, int(workers))

    scan = _scan(out, id_attr) if resume else _Scan(set(), set(), 0, 0)

    plan: list[tuple[str | None, Any]] = []
    skipped = 0
    planned: set[str] = set()
    for sample in samples:
        if limit is not None and len(plan) >= limit:
            break
        vid = sample_id(sample, id_attr)
        # A duplicate id within one call would write two records for one video;
        # the first occurrence is the one that runs.
        if vid is not None and (vid in scan.done or vid in planned):
            skipped += 1
            continue
        if vid is not None:
            planned.add(vid)
        plan.append((vid, sample))

    stats = RunStats(total=skipped + len(plan), skipped=skipped)

    if progress:
        if scan.bad_lines:
            print(
                f"runner: {out.name}: skipped {scan.bad_lines} unparseable line(s) "
                "(a previous run was killed mid-write)",
                file=sys.stderr,
            )
        retries = sum(1 for vid, _ in plan if vid in scan.failed)
        if skipped or retries:
            print(
                f"runner: resuming {out.name}: {skipped} already done, "
                f"{len(plan)} to run ({retries} of them earlier failures)"
            )

    if not plan:
        stats.wall_seconds = time.perf_counter() - started
        return stats

    writer = _JsonlWriter(out)
    bar = tqdm(total=len(plan), desc="judging", unit="video", disable=not progress)

    def run_one(item: tuple[str | None, Any]) -> bool:
        vid, sample = item
        try:
            record = _to_record(judge_fn(sample))
        except Exception as exc:  # noqa: BLE001 - a dead video is data, not a bug
            record = {
                id_attr: vid,
                "error": f"{type(exc).__name__}: {exc}",
                "traceback": traceback.format_exc(),
            }
        record = _stamp_id(record, vid, id_attr)
        try:
            writer.write(record)
        except (TypeError, ValueError) as exc:
            # A record json.dumps refuses must not abort the sweep; degrade it
            # to a failure row so resume retries it later.
            writer.write(
                {
                    id_attr: vid,
                    "error": f"unserialisable record: {type(exc).__name__}: {exc}",
                }
            )
            return True
        return is_failure(record, id_attr)

    def tally(failed: bool) -> None:
        if failed:
            stats.failed += 1
        else:
            stats.done += 1
        bar.update(1)

    try:
        if workers == 1:
            # No pool: a single-threaded run stays debuggable, and tracebacks
            # come from the caller's own stack.
            for item in plan:
                tally(run_one(item))
        else:
            pool = ThreadPoolExecutor(max_workers=workers, thread_name_prefix="pjudge")
            try:
                futures = [pool.submit(run_one, item) for item in plan]
                for future in as_completed(futures):
                    tally(future.result())
            except BaseException:
                # A dead writer or a Ctrl-C must stop spending money now, not
                # after the queue drains.
                pool.shutdown(wait=False, cancel_futures=True)
                raise
            finally:
                pool.shutdown(wait=True)
    finally:
        bar.close()
        writer.close()
        stats.wall_seconds = time.perf_counter() - started

    return stats


# --------------------------------------------------------------------------
# reading results back as a table
# --------------------------------------------------------------------------


def _as_records(source: Any) -> list[dict[str, Any]]:
    """Accept a path to a jsonl or an in-memory sequence of records."""
    if source is None:
        return []
    if isinstance(source, (str, os.PathLike)):
        return load_results(source)
    return [dict(r) for r in source if isinstance(r, Mapping)]


def results_frame(source: str | Path | Iterable[Mapping[str, Any]]) -> pd.DataFrame:
    """One row per record, columns being the union of the records' keys.

    Deliberately unfiltered and undeduplicated: this is the raw run log, for
    asking questions like how many rows errored or how much a retry cost.
    """
    records = _as_records(source)
    if not records:
        return pd.DataFrame()
    return pd.DataFrame(records)


def _latest_by_id(
    records: Sequence[Mapping[str, Any]], id_attr: str
) -> dict[str, dict[str, Any]]:
    """One record per id: the last successful one, else the last failure.

    A retried video leaves both an error record and a later good one in the
    file. Metrics must see exactly one row per video, and it must be the one
    that worked.
    """
    best: dict[str, dict[str, Any]] = {}
    for record in records:
        vid = record.get(id_attr)
        if vid is None:
            continue
        vid = str(vid)
        prev = best.get(vid)
        if prev is None or not is_failure(record, id_attr) or is_failure(prev, id_attr):
            best[vid] = dict(record)
    return best


def _gold_index(dataset: Any, id_attr: str) -> dict[str, Any]:
    """Duck-typed id -> gold row map.

    `eval/dataset.py` is a sibling module written separately, so this depends on
    behaviour rather than on its type: anything with `id_to_sample`, any mapping
    of id to row, a pandas frame of gold, or a plain iterable of rows works.
    """
    if dataset is None:
        return {}

    getter = getattr(dataset, "id_to_sample", None)
    if getter is not None:
        table = getter() if callable(getter) else getter
        if isinstance(table, Mapping):
            return {str(k): v for k, v in table.items()}

    if isinstance(dataset, Mapping):
        return {str(k): v for k, v in dataset.items()}

    to_dict = getattr(dataset, "to_dict", None)
    rows: Iterable[Any]
    if callable(to_dict) and hasattr(dataset, "columns"):
        rows = dataset.to_dict("records")
    else:
        rows = dataset

    out: dict[str, Any] = {}
    for row in rows:
        vid = sample_id(row, id_attr)
        if vid is not None:
            out.setdefault(vid, row)  # first occurrence wins, dataset order kept
    return out


def _bool_column(values: pd.Series) -> pd.Series:
    """bool dtype when every value is one; object (keeping None) otherwise."""
    if len(values) == 0:
        return values.astype(object)

    def boolish(v: Any) -> bool:
        if isinstance(v, (bool, np.bool_)):
            return True
        return isinstance(v, (int, np.integer)) and int(v) in (0, 1)

    if bool(values.map(boolish).all()):
        return values.astype(bool)
    return values.astype(object)


def join_with_gold(
    results: str | Path | Iterable[Mapping[str, Any]],
    dataset: Any,
    id_attr: str = "video_id",
) -> pd.DataFrame:
    """Inner join of a run's results onto the gold labels, one row per video.

    Rows come out in dataset order rather than file order, because file order
    depends on which worker finished first. Absent fields become None (or NaN
    once a numeric column is coerced) instead of raising: a record from a judge
    that reports no cost, or an abstention with no score, is still a row.

    The id column takes the name of `id_attr`. Numeric columns are coerced with
    `to_numeric`, so a column with a hole in it is float and one without is int.
    """
    records = _as_records(results)
    latest = _latest_by_id(records, id_attr)
    gold = _gold_index(dataset, id_attr)

    columns = [
        id_attr,
        *_GOLD_FIELDS,
        *_GOLD_DIAGNOSIS_FIELDS,
        *_PRED_FIELDS,
        *_DIAGNOSIS_FIELDS,
        *COST_FIELDS,
        "error",
    ]
    rows: list[dict[str, Any]] = []
    for vid, sample in gold.items():
        record = latest.get(vid)
        if record is None:
            continue
        row: dict[str, Any] = {id_attr: vid}
        for name in _GOLD_FIELDS + _GOLD_DIAGNOSIS_FIELDS:
            row[name] = _field(sample, name)
        row["pred"] = _first_present(record, SCORE_KEYS)
        row["confidence"] = record.get("confidence")
        row["abstain"] = record.get("abstain")
        row["score_imputed"] = record.get("score_imputed")
        row["fatal"] = record.get("fatal")
        for name in _DIAGNOSIS_FIELDS:
            row[name] = record.get(name)
        for name in COST_FIELDS:
            row[name] = _cost_field(record, name)
        row["error"] = record.get("error")
        rows.append(row)

    frame = pd.DataFrame(rows, columns=columns)
    frame[id_attr] = frame[id_attr].astype(str)
    for name in _NUMERIC_COLUMNS:
        frame[name] = pd.to_numeric(frame[name], errors="coerce")
    for name in _BOOLEAN_COLUMNS:
        frame[name] = _bool_column(frame[name])
    return frame


__all__ = [
    "COST_FIELDS",
    "RunStats",
    "SCORE_KEYS",
    "completed_ids",
    "failed_ids",
    "is_failure",
    "join_with_gold",
    "load_results",
    "results_frame",
    "run_batch",
    "sample_id",
]
