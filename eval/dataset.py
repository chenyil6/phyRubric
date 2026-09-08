"""VideoPhy-2 as a list of local videos with human labels attached.

Everything the evaluation layer reports is indexed by `Sample.video_id`, so this
module owns three things that would otherwise be re-invented (and drift) in every
script:

1. URL -> local file resolution. The archives use two hosts with two different
   layouts, and one clip of the test split is simply absent from the upload. A
   missing file is recorded, never raised: a run that silently scored 3396 rows
   while claiming 3397 is worse than one that says which row it dropped.
2. Stable ids. Scores, caches and run directories are keyed by id, so the id may
   not depend on load order, on the filter that produced the view, or on
   `PYTHONHASHSEED`. It is derived from the resolved relative path alone.
3. The label columns are Python reprs written by a spreadsheet, including entries
   like `"[nan]"`. Parsing lives here so that a malformed cell costs one empty
   rule list rather than a crashed sweep.

`stats()` and every filter touch no video bytes, which keeps them usable while
the archive is still unzipping.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import random
import re
import urllib.parse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_TEST_CSV = "data/videophy2/videophy2_test__videophy2_test.csv"
DEFAULT_TRAIN_CSV = "data/videophy2/videophy2_train__videophy2_training.csv"
DEFAULT_VIDEOS_ROOT = "data/videophy2/videos"

RULE_COLUMNS = (
    "physics_rules_followed",
    "physics_rules_unfollowed",
    "physics_rules_cannot_be_determined",
    "human_violated_rules",
)

# Archive directory -> the short generator name used in every table. The test
# split carries `model_name`; the train split does not, so it is derived here.
MODEL_DIRS = {
    "cogvideoX5b_hard_upsampled": "cogvideo",
    "cogvideoX5b_hard_train_upsampled": "cogvideo",
    "cosmos_videophy2_test_challenging": "cosmos",
    "cosmos_videophy2_train_challenging": "cosmos",
    "hunyuan_xdit": "hunyuan",
    "hunyuan_xedit_train": "hunyuan",
    "dream_machine": "ray2",
    "sora_hard_videophy2": "sora",
    "videocrafter_videophy2_hard": "videocrafter",
    "wan_videophy2_test_hard_upsampled": "wan",
}

# Substring fallbacks for directories added after this was written, longest
# distinguishing token first. An unrecognised directory keeps its own name.
_MODEL_HINTS = (
    ("videocrafter", "videocrafter"),
    ("cogvideo", "cogvideo"),
    ("dream_machine", "ray2"),
    ("hunyuan", "hunyuan"),
    ("cosmos", "cosmos"),
    ("sora", "sora"),
    ("wan", "wan"),
)

_ID_MAX_LEN = 100
_ID_HASH_LEN = 8
_ID_ALLOWED = re.compile(r"[^A-Za-z0-9._-]+")


# -- parsing helpers -------------------------------------------------------


def resolve_path(path: str | Path) -> Path:
    """Absolute path for a config value, tolerating a non-repo working directory.

    Config paths are written relative to the repo root, but sweeps get launched
    from anywhere; a path that does not exist relative to the caller is retried
    against the root before being reported as missing.
    """
    p = Path(path)
    if p.is_absolute():
        return p
    if p.exists():
        return p.resolve()
    return REPO_ROOT / p


def relative_video_path(url: str) -> str:
    """Archive-relative path of the clip a `video_url` points at.

    The two hosts disagree: the S3 uploads mirror `<model_dir>/<file>` exactly,
    while the Luma CDN puts a per-generation uuid directory in the middle that
    the archive drops, keeping only the leaf file under `dream_machine/`.
    """
    if not isinstance(url, str) or not url.strip():
        return ""
    path = urllib.parse.unquote(urllib.parse.urlparse(url).path).lstrip("/")
    if "amazonaws.com" in url:
        return path
    return "dream_machine/" + os.path.basename(path)


def model_from_path(rel: str) -> str:
    """Generator name for an archive-relative path (the train split needs this)."""
    head = rel.split("/", 1)[0] if rel else ""
    if head in MODEL_DIRS:
        return MODEL_DIRS[head]
    low = head.lower()
    for hint, name in _MODEL_HINTS:
        if hint in low:
            return name
    return head


def make_video_id(rel: str) -> str:
    """Filesystem-safe id derived only from the resolved relative path.

    A short digest is appended whenever sanitisation or truncation loses
    information, which is the only way two distinct paths could collapse onto one
    id. Doing it per row (rather than only on an observed collision) keeps ids
    identical whether the whole split or a single filtered view is loaded.
    """
    if not rel:
        return "unresolved"
    parts = rel.split("/")
    stem = Path(parts[-1]).stem or parts[-1]
    raw = f"{parts[0]}__{stem}" if len(parts) > 1 else stem
    clean = _ID_ALLOWED.sub("_", raw).strip("_")
    if not clean:
        clean = "video"
    if clean == raw and len(clean) <= _ID_MAX_LEN:
        return clean
    digest = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:_ID_HASH_LEN]
    stub = clean[: _ID_MAX_LEN - _ID_HASH_LEN - 1].rstrip("._-")
    return f"{stub}-{digest}"


def parse_rule_list(raw: Any) -> tuple[str, ...]:
    """Parse one of the four rule columns: a Python-repr list of strings.

    Malformed cells exist (`"[nan]"` appears three times per split), as do plain
    free-text cells. Neither is worth a traceback; both degrade to what can be
    read out of them.
    """
    if raw is None or isinstance(raw, float):  # NaN arrives as a float
        return ()
    if isinstance(raw, (list, tuple)):
        return _clean_strings(raw)
    text = str(raw).strip()
    if not text or text in {"[]", "{}", "nan", "None"}:
        return ()
    try:
        value = ast.literal_eval(text)
    except (ValueError, SyntaxError):
        # Not a literal: a bracketed cell we cannot trust is dropped, anything
        # else is a human's free-text rule and is kept whole.
        return () if text.startswith(("[", "{")) else (text,)
    if isinstance(value, (list, tuple, set)):
        return _clean_strings(value)
    if isinstance(value, str):
        return _clean_strings([value])
    return ()


def parse_rule_laws(raw: Any) -> dict[str, tuple[str, ...]]:
    """Parse `metadata_rules`: rule text -> physical law, str or list of str."""
    if raw is None or isinstance(raw, float):
        return {}
    text = str(raw).strip()
    if not text or text in {"{}", "[]", "nan", "None"}:
        return {}
    try:
        value = ast.literal_eval(text)
    except (ValueError, SyntaxError):
        return {}
    if not isinstance(value, dict):
        return {}
    out: dict[str, tuple[str, ...]] = {}
    for rule, laws in value.items():
        key = str(rule).strip()
        if not key:
            continue
        if isinstance(laws, (list, tuple, set)):
            out[key] = _clean_strings(laws)
        elif laws is None or isinstance(laws, float):
            out[key] = ()
        else:
            out[key] = _clean_strings([laws])
    return out


def _clean_strings(items: Iterable[Any]) -> tuple[str, ...]:
    out: list[str] = []
    for item in items:
        if item is None or isinstance(item, float):
            continue  # a bare nan inside the list is not a rule
        text = str(item).strip()
        if text and text.lower() != "nan":
            out.append(text)
    return tuple(out)


def _as_text(value: Any) -> str:
    if value is None or isinstance(value, float) and pd.isna(value):
        return ""
    return str(value).strip()


def _as_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or (isinstance(value, float) and pd.isna(value)):
            return default
        return int(round(float(value)))
    except (TypeError, ValueError):
        return default


# -- sample ----------------------------------------------------------------


@dataclass(frozen=True)
class Sample:
    """One row of VideoPhy-2, resolved against the local archive."""

    video_id: str
    caption: str
    upsampled_caption: str
    video_path: Path
    exists: bool
    model_name: str
    sa: int
    pc: int
    joint: int
    is_hard: bool
    action: str
    category: str
    rules_followed: tuple[str, ...] = ()
    rules_unfollowed: tuple[str, ...] = ()
    rules_cannot_be_determined: tuple[str, ...] = ()
    human_violated_rules: tuple[str, ...] = ()
    rule_laws: Mapping[str, tuple[str, ...]] = None  # type: ignore[assignment]
    rel_path: str = ""
    video_url: str = ""
    row_index: int = -1

    def __post_init__(self) -> None:
        if self.rule_laws is None:
            object.__setattr__(self, "rule_laws", {})

    def prompt_for_generation(self) -> str:
        """The text the generator actually saw: dense rewrite when there is one."""
        return self.upsampled_caption or self.caption

    def law_for(self, rule: str) -> tuple[str, ...]:
        return tuple(self.rule_laws.get(rule.strip(), ()))

    @property
    def all_violated_rules(self) -> tuple[str, ...]:
        """Automatic and human-written violations, de-duplicated, order kept.

        The two columns overlap but neither contains the other: 67% of rows have
        no `physics_rules_unfollowed` while 54% carry free-text human rules.
        """
        seen: dict[str, None] = {}
        for rule in self.rules_unfollowed + self.human_violated_rules:
            seen.setdefault(rule, None)
        return tuple(seen)

    def as_dict(self) -> dict[str, Any]:
        return {
            "video_id": self.video_id,
            "caption": self.caption,
            "upsampled_caption": self.upsampled_caption,
            "video_path": str(self.video_path),
            "rel_path": self.rel_path,
            "video_url": self.video_url,
            "exists": self.exists,
            "model_name": self.model_name,
            "sa": self.sa,
            "pc": self.pc,
            "joint": self.joint,
            "is_hard": self.is_hard,
            "action": self.action,
            "category": self.category,
            "rules_followed": list(self.rules_followed),
            "rules_unfollowed": list(self.rules_unfollowed),
            "rules_cannot_be_determined": list(self.rules_cannot_be_determined),
            "human_violated_rules": list(self.human_violated_rules),
            "rule_laws": {k: list(v) for k, v in self.rule_laws.items()},
            "row_index": self.row_index,
        }


# -- dataset ---------------------------------------------------------------


class VideoPhy2Dataset:
    """A split of VideoPhy-2, or any view derived from one by filtering.

    Views share their `Sample` objects with the dataset they came from, so ids
    and labels cannot drift between a sweep and its subset, and nothing here
    mutates: `filter` and `stratified_subset` always return a new instance.
    """

    def __init__(
        self,
        csv_path: str | Path,
        videos_root: str | Path,
        split: str = "test",
        samples: Sequence[Sample] | None = None,
    ):
        self.csv_path = resolve_path(csv_path)
        self.videos_root = resolve_path(videos_root)
        self.split = split
        self._samples: list[Sample] = (
            list(samples) if samples is not None else self._load()
        )
        self._by_id = {s.video_id: s for s in self._samples}

    # -- construction ------------------------------------------------------

    @classmethod
    def from_config(cls, cfg: dict[str, Any], split: str = "test") -> "VideoPhy2Dataset":
        """Build from a loaded config, falling back to the documented layout.

        The shipped config has no `data` section, so absent keys are normal
        rather than exceptional.
        """
        section = ((cfg or {}).get("data") or {}).get("videophy2") or {}
        default_csv = DEFAULT_TRAIN_CSV if split == "train" else DEFAULT_TEST_CSV
        csv_path = section.get(f"{split}_csv") or section.get("csv") or default_csv
        videos_root = section.get("videos_root") or DEFAULT_VIDEOS_ROOT
        return cls(csv_path, videos_root, split=split)

    def _derive(self, samples: Sequence[Sample]) -> "VideoPhy2Dataset":
        return VideoPhy2Dataset(
            self.csv_path, self.videos_root, split=self.split, samples=samples
        )

    def _load(self) -> list[Sample]:
        frame = pd.read_csv(self.csv_path)
        frame = frame.drop(columns=[c for c in frame.columns if str(c).startswith("Unnamed")])
        has_model = "model_name" in frame.columns
        out: list[Sample] = []
        for i, row in enumerate(frame.to_dict("records")):
            rel = relative_video_path(row.get("video_url", ""))
            model = _as_text(row.get("model_name")) if has_model else ""
            path = (self.videos_root / rel) if rel else (self.videos_root / f"unresolved_{i:05d}")
            out.append(
                Sample(
                    video_id=make_video_id(rel) if rel else f"unresolved_{i:05d}",
                    caption=_as_text(row.get("caption")),
                    upsampled_caption=_as_text(row.get("upsampled_caption")),
                    video_path=path,
                    exists=bool(rel) and path.is_file(),
                    model_name=model or model_from_path(rel),
                    sa=_as_int(row.get("sa")),
                    pc=_as_int(row.get("pc")),
                    joint=_as_int(row.get("joint")),
                    is_hard=bool(_as_int(row.get("is_hard"))),
                    action=_as_text(row.get("action")),
                    category=_as_text(row.get("category")),
                    rules_followed=parse_rule_list(row.get("physics_rules_followed")),
                    rules_unfollowed=parse_rule_list(row.get("physics_rules_unfollowed")),
                    rules_cannot_be_determined=parse_rule_list(
                        row.get("physics_rules_cannot_be_determined")
                    ),
                    human_violated_rules=parse_rule_list(row.get("human_violated_rules")),
                    rule_laws=parse_rule_laws(row.get("metadata_rules")),
                    rel_path=rel,
                    video_url=_as_text(row.get("video_url")),
                    row_index=i,
                )
            )
        return out

    # -- container protocol ------------------------------------------------

    def __len__(self) -> int:
        return len(self._samples)

    def __iter__(self):
        return iter(self._samples)

    def __getitem__(self, key: int | str | slice) -> Sample | "VideoPhy2Dataset":
        if isinstance(key, slice):
            return self._derive(self._samples[key])
        if isinstance(key, str):
            try:
                return self._by_id[key]
            except KeyError:
                raise KeyError(f"no sample with video_id {key!r}") from None
        return self._samples[key]

    def __contains__(self, key: object) -> bool:
        return key in self._by_id if isinstance(key, str) else key in self._samples

    def __repr__(self) -> str:
        return (
            f"VideoPhy2Dataset(split={self.split!r}, n={len(self._samples)}, "
            f"missing={len(self.missing)})"
        )

    # -- views -------------------------------------------------------------

    @property
    def samples(self) -> list[Sample]:
        return list(self._samples)

    @property
    def missing(self) -> list[Sample]:
        """Rows whose video is not on disk. Reported, never raised."""
        return [s for s in self._samples if not s.exists]

    def id_to_sample(self) -> dict[str, Sample]:
        return dict(self._by_id)

    def filter(
        self,
        *,
        pc: int | Iterable[int] | tuple[int, int] | None = None,
        models: str | Iterable[str] | None = None,
        hard: bool | None = None,
        has_video: bool | None = True,
        predicate: Callable[[Sample], bool] | None = None,
    ) -> "VideoPhy2Dataset":
        """A new view keeping the matching rows.

        `pc` takes an int, an iterable of ints (membership), or a 2-tuple read as
        an inclusive `(lo, hi)` range -- pass a list or set when you mean exactly
        two scores. `has_video=True` (the default) drops rows whose file is
        absent, `False` keeps only those, `None` keeps everything.
        """
        match_pc = _pc_matcher(pc)
        wanted = _name_set(models)
        keep: list[Sample] = []
        for s in self._samples:
            if has_video is not None and s.exists is not has_video:
                continue
            if match_pc is not None and not match_pc(s.pc):
                continue
            if wanted is not None and s.model_name.lower() not in wanted:
                continue
            if hard is not None and s.is_hard is not bool(hard):
                continue
            if predicate is not None and not predicate(s):
                continue
            keep.append(s)
        return self._derive(keep)

    def stratified_subset(
        self,
        n: int,
        seed: int = 0,
        by: Sequence[str] | str = ("pc", "is_hard"),
    ) -> "VideoPhy2Dataset":
        """`n` rows keeping the joint distribution of the `by` fields.

        Proportional allocation with largest-remainder rounding; a stratum too
        small for its quota hands the shortfall to strata that still have spare
        rows, so the total reaches `n` whenever the split is big enough. Each
        stratum draws from its own seeded stream, keyed by the stratum values, so
        the choice inside one stratum does not depend on the sizes of the others.
        """
        keys = (by,) if isinstance(by, str) else tuple(by)
        n = max(0, min(int(n), len(self._samples)))
        if n == 0:
            return self._derive([])
        if not keys:
            return self._derive(_seeded_sample(self._samples, n, f"{seed}:all"))

        groups: dict[tuple[str, ...], list[Sample]] = {}
        for s in self._samples:
            groups.setdefault(tuple(_stratum_value(s, k) for k in keys), []).append(s)
        order = sorted(groups)
        quotas = _allocate(n, [len(groups[k]) for k in order])

        picked: list[Sample] = []
        for key, quota in zip(order, quotas):
            if quota:
                picked.extend(
                    _seeded_sample(groups[key], quota, f"{seed}:" + "|".join(key))
                )
        rank = {s.video_id: s.row_index for s in self._samples}
        picked.sort(key=lambda s: (rank[s.video_id], s.video_id))
        return self._derive(picked)

    # -- reporting ---------------------------------------------------------

    def stats(self) -> dict[str, Any]:
        """Everything about the split that can be known without opening a video."""
        n = len(self._samples)
        missing = self.missing
        rules: dict[str, dict[str, float | int]] = {}
        for column, attr in zip(
            RULE_COLUMNS,
            (
                "rules_followed",
                "rules_unfollowed",
                "rules_cannot_be_determined",
                "human_violated_rules",
            ),
        ):
            lengths = [len(getattr(s, attr)) for s in self._samples]
            non_empty = sum(1 for k in lengths if k)
            rules[column] = {
                "non_empty": non_empty,
                "empty": n - non_empty,
                "empty_rate": round(1 - non_empty / n, 4) if n else 0.0,
                "total_rules": sum(lengths),
                "mean_rules": round(sum(lengths) / n, 3) if n else 0.0,
            }
        laws = Counter(
            law for s in self._samples for value in s.rule_laws.values() for law in value
        )
        return {
            "split": self.split,
            "csv_path": str(self.csv_path),
            "videos_root": str(self.videos_root),
            "n": n,
            "n_missing": len(missing),
            "missing_ids": [s.video_id for s in missing],
            "pc": _counts(s.pc for s in self._samples),
            "sa": _counts(s.sa for s in self._samples),
            "joint": _counts(s.joint for s in self._samples),
            "is_hard": _counts(int(s.is_hard) for s in self._samples),
            "model_name": dict(Counter(s.model_name for s in self._samples).most_common()),
            "category": dict(Counter(s.category for s in self._samples).most_common()),
            "n_actions": len({s.action for s in self._samples if s.action}),
            "n_categories": len({s.category for s in self._samples if s.category}),
            "rules": rules,
            "physics_laws": {"n_distinct": len(laws), "top": dict(laws.most_common(10))},
            "captions": {
                "unique": len({s.caption for s in self._samples}),
                "mean_chars": round(
                    sum(len(s.caption) for s in self._samples) / n, 1
                ) if n else 0.0,
                "upsampled_non_empty": sum(1 for s in self._samples if s.upsampled_caption),
                "mean_upsampled_chars": round(
                    sum(len(s.upsampled_caption) for s in self._samples) / n, 1
                ) if n else 0.0,
            },
        }


# -- allocation and filtering helpers --------------------------------------


def _counts(values: Iterable[int]) -> dict[int, int]:
    counter = Counter(values)
    return {k: counter[k] for k in sorted(counter)}


def _pc_matcher(
    pc: int | Iterable[int] | tuple[int, int] | None,
) -> Callable[[int], bool] | None:
    if pc is None:
        return None
    if isinstance(pc, bool):
        raise TypeError("pc must be an int, an iterable of ints, or a (lo, hi) tuple")
    if isinstance(pc, int):
        target = int(pc)
        return lambda value: value == target
    if isinstance(pc, tuple) and len(pc) == 2:
        lo, hi = int(pc[0]), int(pc[1])
        return lambda value: lo <= value <= hi
    allowed = {int(v) for v in pc}
    return lambda value: value in allowed


def _name_set(models: str | Iterable[str] | None) -> set[str] | None:
    if models is None:
        return None
    if isinstance(models, str):
        return {models.strip().lower()}
    return {str(m).strip().lower() for m in models}


def _stratum_value(sample: Sample, key: str) -> str:
    value = getattr(sample, key)
    if isinstance(value, bool):
        return str(int(value))
    if isinstance(value, (int, float)):
        return f"{value:g}"
    return str(value)


def _seeded_sample(items: Sequence[Sample], k: int, seed_text: str) -> list[Sample]:
    """`k` items chosen deterministically from `items`.

    Seeding from a string rather than an object keeps the draw stable across
    interpreters: `random.Random` hashes the text itself, whereas `hash()` of a
    tuple of strings moves with `PYTHONHASHSEED`.
    """
    pool = sorted(items, key=lambda s: s.video_id)
    if k >= len(pool):
        return pool
    rng = random.Random(seed_text)
    rng.shuffle(pool)
    return pool[:k]


def _allocate(n: int, sizes: Sequence[int]) -> list[int]:
    """Largest-remainder quotas summing to `min(n, sum(sizes))`, capped by size."""
    total = sum(sizes)
    if n <= 0 or total <= 0:
        return [0] * len(sizes)
    n = min(n, total)
    exact = [n * size / total for size in sizes]
    quota = [min(int(math.floor(e)), size) for e, size in zip(exact, sizes)]
    order = sorted(range(len(sizes)), key=lambda i: (-(exact[i] % 1.0), i))
    left = n - sum(quota)
    while left > 0:
        spent = 0
        for i in order:
            if left == 0:
                break
            if quota[i] < sizes[i]:
                quota[i] += 1
                left -= 1
                spent += 1
        if spent == 0:
            break
    return quota
