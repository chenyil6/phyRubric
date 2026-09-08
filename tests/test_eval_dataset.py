"""Tests for eval/dataset.py, run against the real VideoPhy-2 test CSV.

No network and no model: everything here is CSV parsing, path arithmetic and
`Path.is_file`. What is pinned down:

  - the measured facts of the split (3397 rows, one absent video, the pc/sa/hard
    distributions, the rule-column emptiness rates), so a mis-parse cannot pass
  - path resolution, recomputed by an independent implementation inside the test
  - video_id uniqueness and stability, including ids that must survive
    sanitisation and truncation
  - stratified_subset: determinism under a seed, and a preserved pc distribution
  - the train split, which lacks `model_name` and must derive it from the URL
"""

from __future__ import annotations

import csv
import json
import os
import random
import sys
import tempfile
import urllib.parse
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd  # noqa: E402

from eval.dataset import (  # noqa: E402
    DEFAULT_TEST_CSV,
    DEFAULT_TRAIN_CSV,
    DEFAULT_VIDEOS_ROOT,
    VideoPhy2Dataset,
    _allocate,
    make_video_id,
    model_from_path,
    parse_rule_laws,
    parse_rule_list,
    relative_video_path,
)

ROOT = Path(__file__).resolve().parents[1]
TEST_CSV = ROOT / DEFAULT_TEST_CSV
TRAIN_CSV = ROOT / DEFAULT_TRAIN_CSV
VIDEOS = ROOT / DEFAULT_VIDEOS_ROOT
SAFE = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")

PC_EXPECTED = {1: 129, 2: 469, 3: 1014, 4: 1175, 5: 610}
SA_EXPECTED = {1: 251, 2: 919, 3: 1058, 4: 863, 5: 306}
MODEL_EXPECTED = {
    "cogvideo": 589,
    "cosmos": 585,
    "hunyuan": 587,
    "ray2": 394,
    "sora": 60,
    "videocrafter": 591,
    "wan": 591,
}
TRAIN_MODEL_EXPECTED = {"cogvideo": 1150, "cosmos": 1088, "hunyuan": 1105}


def independent_rel(url: str) -> str:
    """Second implementation of the resolution rule, written from the spec."""
    path = urllib.parse.unquote(urllib.parse.urlparse(url).path).lstrip("/")
    if "amazonaws.com" in url:
        return path
    return "dream_machine/" + os.path.basename(path)


# --------------------------------------------------------------------------
# pure helpers
# --------------------------------------------------------------------------


def test_parsers() -> None:
    assert parse_rule_list("[]") == ()
    assert parse_rule_list("['A ball bounces.', 'It keeps its shape.']") == (
        "A ball bounces.",
        "It keeps its shape.",
    )
    # the three real `[nan]` cells: a bare nan is not a rule
    assert parse_rule_list("[nan]") == ()
    assert parse_rule_list("['a', nan]") == ()  # unparseable list literal
    assert parse_rule_list(float("nan")) == ()
    assert parse_rule_list(None) == ()
    assert parse_rule_list("") == ()
    # apostrophes inside a double-quoted repr entry
    assert parse_rule_list('["The loader\'s bucket bends."]') == (
        "The loader's bucket bends.",
    )
    # free text that is not a literal at all is kept whole
    assert parse_rule_list("the ball must bounce") == ("the ball must bounce",)

    laws = parse_rule_laws("{'a': 'Gravity', 'b': ['Friction', 'Inertia'], 'c': None}")
    assert laws == {"a": ("Gravity",), "b": ("Friction", "Inertia"), "c": ()}, laws
    assert parse_rule_laws("{}") == {}
    assert parse_rule_laws("not a dict") == {}
    assert parse_rule_laws(float("nan")) == {}
    print("  parsers ok")


def test_resolution_rule() -> None:
    s3 = (
        "https://videophysics2testvideos.s3.us-east-2.amazonaws.com/hunyuan_xdit/"
        "A_yo-yo_is_tossed_against_a_brick_wall.mp4"
    )
    assert relative_video_path(s3) == (
        "hunyuan_xdit/A_yo-yo_is_tossed_against_a_brick_wall.mp4"
    )
    luma = (
        "https://storage.cdn-luma.com/dream_machine/5317eb9f-9fbf-4d05-ae76-9bb008792a7f/"
        "7facba57-4c5a-4c77-8a72-de833491ba80_result.mp4"
    )
    assert relative_video_path(luma) == (
        "dream_machine/7facba57-4c5a-4c77-8a72-de833491ba80_result.mp4"
    )
    # percent-encoding is undone, so the path matches the unzipped file
    quoted = "https://x.s3.us-east-2.amazonaws.com/wan_dir/A%20ball%2C%20dropped.mp4"
    assert relative_video_path(quoted) == "wan_dir/A ball, dropped.mp4"
    assert relative_video_path("") == ""
    assert relative_video_path(float("nan")) == ""

    assert model_from_path("dream_machine/x.mp4") == "ray2"
    assert model_from_path("hunyuan_xedit_train/x.mp4") == "hunyuan"
    assert model_from_path("cogvideoX5b_hard_train_upsampled/x.mp4") == "cogvideo"
    assert model_from_path("brand_new_model_dir/x.mp4") == "brand_new_model_dir"
    print("  resolution rule ok")


def test_video_id_rules() -> None:
    # clean, short paths keep a readable id with no digest
    assert make_video_id("hunyuan_xdit/A_ball_falls.mp4") == "hunyuan_xdit__A_ball_falls"
    # sanitisation is lossy, so a digest is appended
    sanitised = make_video_id("hunyuan_xdit/A bowler's run-up; then the ball.mp4")
    assert sanitised.startswith("hunyuan_xdit__A_bowler_s_run-up_then_the_ball-"), sanitised
    assert set(sanitised) <= SAFE, sanitised
    # two paths that agree over their first 100 characters must not collide
    long_a = "wan_dir/" + "A" * 140 + "_first.mp4"
    long_b = "wan_dir/" + "A" * 140 + "_second.mp4"
    assert make_video_id(long_a) != make_video_id(long_b)
    assert len(make_video_id(long_a)) <= 100, len(make_video_id(long_a))
    # and the id is a pure function of the path
    assert make_video_id(long_a) == make_video_id(long_a)
    assert make_video_id("") == "unresolved"
    print(f"  video_id rules ok: {sanitised}")


def test_allocate_invariants() -> None:
    assert _allocate(0, [10, 10]) == [0, 0]
    assert _allocate(5, []) == []
    assert _allocate(10, [0, 0]) == [0, 0]
    assert _allocate(100, [3, 7]) == [3, 7], "n above the total is clamped"
    assert _allocate(10, [50, 50]) == [5, 5]
    # a stratum cannot exceed its own size, and the shortfall goes to strata
    # that still have rows to give
    quota = _allocate(99, [1, 99])
    assert quota == [1, 98] and sum(quota) == 99, quota

    rng = random.Random(7)
    for _ in range(400):
        sizes = [rng.randint(0, 40) for _ in range(rng.randint(1, 6))]
        total = sum(sizes)
        n = rng.randint(0, total + 5)
        quota = _allocate(n, sizes)
        assert all(0 <= q <= s for q, s in zip(quota, sizes)), (sizes, n, quota)
        assert sum(quota) == min(n, total), (sizes, n, quota)
        if total:
            for q, s in zip(quota, sizes):
                assert abs(q - min(n, total) * s / total) < 1.0 + 1e-9, (sizes, n, quota)
    print("  allocation invariants ok (400 random size vectors)")


# --------------------------------------------------------------------------
# the real test split
# --------------------------------------------------------------------------


def load_full() -> VideoPhy2Dataset:
    return VideoPhy2Dataset(TEST_CSV, VIDEOS, split="test")


def test_real_test_split(ds: VideoPhy2Dataset) -> None:
    raw = pd.read_csv(TEST_CSV)
    assert len(ds) == 3397 == len(raw), len(ds)

    ids = [s.video_id for s in ds]
    assert len(set(ids)) == 3397, f"video_id collision: {len(ids) - len(set(ids))} dupes"
    assert all(set(i) <= SAFE for i in ids)
    assert max(len(i) for i in ids) <= 100, max(len(i) for i in ids)

    # resolution: recomputed independently, then checked against the disk
    rels = [independent_rel(u) for u in raw.video_url]
    assert [s.rel_path for s in ds] == rels, "resolution differs from the spec rule"
    on_disk = sum(1 for r in rels if (VIDEOS / r).is_file())
    unresolved = [r for r in rels if not (VIDEOS / r).is_file()]
    if on_disk == 3396:
        assert len(ds.missing) == 1, ds.missing
        assert ds.missing[0].model_name == "cogvideo", ds.missing[0].model_name
    else:
        assert on_disk >= 3000, f"only {on_disk} videos unzipped so far"
        assert len(unresolved) == 1, unresolved
    assert sum(1 for s in ds if s.exists) == on_disk
    assert len(ds.filter()) == on_disk, "the default filter must drop missing videos"
    assert len(ds.filter(has_video=None)) == 3397
    assert len(ds.filter(has_video=False)) == 3397 - on_disk

    # the 204 truncated filenames must be matched verbatim, not repaired
    no_suffix = [s for s in ds if not s.rel_path.endswith(".mp4")]
    assert len(no_suffix) == 204, len(no_suffix)
    assert all(s.video_path.suffix != ".mp4" for s in no_suffix)
    assert sum(1 for s in no_suffix if s.exists) == 204, "verbatim match lost files"

    stats = ds.stats()
    assert stats["pc"] == PC_EXPECTED, stats["pc"]
    assert stats["sa"] == SA_EXPECTED, stats["sa"]
    assert stats["joint"] == {0: 2659, 1: 738}, stats["joint"]
    assert stats["is_hard"] == {0: 2382, 1: 1015}, stats["is_hard"]
    assert stats["model_name"] == MODEL_EXPECTED, stats["model_name"]
    assert stats["n_missing"] == 3397 - on_disk
    assert stats["rules"]["human_violated_rules"]["non_empty"] == 1821
    assert stats["rules"]["physics_rules_unfollowed"]["empty_rate"] == 0.6721
    assert stats["rules"]["physics_rules_cannot_be_determined"]["empty_rate"] == 0.8714
    assert stats["rules"]["physics_rules_followed"]["non_empty"] == 3129
    assert stats["captions"]["upsampled_non_empty"] == 3397 - 18, stats["captions"]
    assert stats["n_categories"] > 1 and stats["physics_laws"]["n_distinct"] > 5

    # the three malformed `[nan]` cells parse to nothing rather than to "nan"
    nan_rows = [
        i
        for i, v in enumerate(raw.physics_rules_cannot_be_determined)
        if isinstance(v, str) and v.strip() == "[nan]"
    ]
    assert len(nan_rows) == 3, nan_rows
    assert all(ds[i].rules_cannot_be_determined == () for i in nan_rows)

    print(
        f"  real split ok: n={len(ds)} on_disk={on_disk} missing={len(ds.missing)} "
        f"unique_ids={len(set(ids))}"
    )
    print(f"  pc={stats['pc']} hard={stats['is_hard']}")


def test_row_level_parsing(ds: VideoPhy2Dataset) -> None:
    """A row known to carry several rules across several columns."""
    s = ds[1]
    assert s.caption.startswith("A bulldozer clears debris"), s.caption
    assert s.model_name == "ray2" and s.pc == 2 and s.sa == 2 and s.joint == 0
    assert s.rel_path.startswith("dream_machine/")
    assert s.rules_followed == (
        "Debris moves upward when scooped by the bucket.",
        "The front-end loader moves across the demolition site.",
    ), s.rules_followed
    assert s.rules_unfollowed == (
        "The front-end loader's bucket changes shape as it scoops debris.",
    ), s.rules_unfollowed
    assert s.rules_cannot_be_determined == ()
    assert len(s.human_violated_rules) == 1, s.human_violated_rules
    assert s.human_violated_rules[0].startswith("The bulldozer cannot simultaneously")
    # metadata_rules mixes a bare string and a list of strings as values
    assert len(s.rule_laws) == 4, s.rule_laws
    assert s.rule_laws["Debris moves upward when scooped by the bucket."] == ("Gravity",)
    assert s.law_for(s.human_violated_rules[0]) == ("Conservation of Energy",)
    assert all(isinstance(v, tuple) for v in s.rule_laws.values())
    # automatic and human violations merge without duplicates
    assert len(s.all_violated_rules) == 2, s.all_violated_rules

    assert s.prompt_for_generation() == s.upsampled_caption
    blank = [x for x in ds if not x.upsampled_caption]
    assert len(blank) == 18, len(blank)
    assert blank[0].prompt_for_generation() == blank[0].caption

    # indexing by id, and round-tripping through as_dict
    assert ds[s.video_id] is s
    assert s.video_id in ds and "nope" not in ds
    d = s.as_dict()
    assert d["video_id"] == s.video_id and d["video_path"] == str(s.video_path)
    assert d["rules_followed"] == list(s.rules_followed)
    assert d["rule_laws"]["Debris moves upward when scooped by the bucket."] == ["Gravity"]
    try:
        ds["definitely-not-an-id"]
    except KeyError:
        pass
    else:
        raise AssertionError("unknown video_id must raise KeyError")
    print(f"  row-level parsing ok: {s.video_id}")


def test_filters_do_not_mutate(ds: VideoPhy2Dataset) -> None:
    before = len(ds)
    ids_before = [s.video_id for s in ds]

    hard = ds.filter(hard=True, has_video=None)
    assert len(hard) == 1015 and all(s.is_hard for s in hard)
    low = ds.filter(pc=1, has_video=None)
    assert len(low) == 129 and {s.pc for s in low} == {1}
    span = ds.filter(pc=(1, 2), has_video=None)
    assert len(span) == 129 + 469, len(span)
    members = ds.filter(pc=[1, 5], has_video=None)
    assert len(members) == 129 + 610, "a list of ints means membership, not a range"
    wan = ds.filter(models="WAN", has_video=None)
    assert len(wan) == 591, "model matching must be case-insensitive"
    pair = ds.filter(models=["sora", "ray2"], has_video=None)
    assert len(pair) == 60 + 394, len(pair)
    pred = ds.filter(predicate=lambda s: bool(s.human_violated_rules), has_video=None)
    assert len(pred) == 1821, len(pred)
    chained = ds.filter(pc=(4, 5), hard=True, has_video=None).filter(models="wan")
    assert chained and all(
        s.pc >= 4 and s.is_hard and s.model_name == "wan" and s.exists for s in chained
    )

    assert len(ds) == before and [s.video_id for s in ds] == ids_before
    assert hard is not ds and isinstance(hard, VideoPhy2Dataset)
    assert hard.split == ds.split and hard.videos_root == ds.videos_root
    # a view shares the row objects, so ids cannot drift between the two
    assert all(hard[s.video_id] is s for s in list(hard)[:50])
    assert [s.video_id for s in load_full()] == ids_before, "video_id is not stable"

    sliced = ds[:10]
    assert isinstance(sliced, VideoPhy2Dataset) and len(sliced) == 10
    print(f"  filters ok: hard={len(hard)} pc1={len(low)} human_rules={len(pred)}")


def test_stratified_subset(ds: VideoPhy2Dataset) -> None:
    full = ds.filter(has_video=None)
    sub = full.stratified_subset(200, seed=0)
    again = full.stratified_subset(200, seed=0)
    assert len(sub) == 200, len(sub)
    assert [s.video_id for s in sub] == [s.video_id for s in again], "not deterministic"

    other = full.stratified_subset(200, seed=1)
    assert len(other) == 200
    assert [s.video_id for s in other] != [s.video_id for s in sub], "seed is ignored"

    counts = Counter(s.pc for s in sub)
    for score, total in PC_EXPECTED.items():
        want = 200 * total / 3397
        assert abs(counts[score] - want) <= 2.0, (score, counts[score], want)
        assert abs(counts[score] / 200 - total / 3397) < 0.02, score
    # the second stratification key is honoured too
    hard_share = sum(1 for s in sub if s.is_hard) / 200
    assert abs(hard_share - 1015 / 3397) < 0.02, hard_share

    # ordering follows the CSV, and the subset is a genuine subset
    assert [s.row_index for s in sub] == sorted(s.row_index for s in sub)
    assert {s.video_id for s in sub} <= {s.video_id for s in full}
    assert len(full) == 3397, "stratification mutated its source"

    # degenerate sizes
    assert len(full.stratified_subset(0)) == 0
    assert len(full.stratified_subset(10_000)) == 3397
    single = full.stratified_subset(7, by="model_name")
    assert len(single) == 7 and len({s.video_id for s in single}) == 7
    print(f"  stratified subset ok: pc={dict(sorted(counts.items()))} hard={hard_share:.3f}")


# --------------------------------------------------------------------------
# the train split and synthetic edge cases
# --------------------------------------------------------------------------


def test_train_split() -> None:
    ds = VideoPhy2Dataset(TRAIN_CSV, VIDEOS, split="train")
    raw = pd.read_csv(TRAIN_CSV)
    assert "model_name" not in raw.columns, "train CSV unexpectedly has model_name"
    assert len(ds) == 3343 == len(raw)
    assert len({s.video_id for s in ds}) == 3343
    stats = ds.stats()
    assert stats["model_name"] == TRAIN_MODEL_EXPECTED, stats["model_name"]
    assert stats["pc"] == {1: 126, 2: 457, 3: 960, 4: 1224, 5: 576}, stats["pc"]
    assert stats["split"] == "train"
    # train clips are not in the unzipped test archive; that is reported, not raised
    assert stats["n_missing"] == len(ds) - sum(1 for s in ds if s.exists)
    print(
        f"  train split ok: n={len(ds)} models={stats['model_name']} "
        f"missing={stats['n_missing']}"
    )


def write_synthetic(path: Path) -> None:
    base = "https://x.s3.us-east-2.amazonaws.com/"
    rows = [
        {
            "caption": "A cup falls.",
            "upsampled_caption": "A ceramic cup falls off a table and shatters.",
            "video_url": base + "sora_hard_videophy2/cup.mp4",
            "sa": 4, "pc": 5, "joint": 1, "action": "falling", "is_hard": 1,
            "physics_rules_followed": "['The cup accelerates downward.']",
            "physics_rules_unfollowed": "[]",
            "physics_rules_cannot_be_determined": "[nan]",
            "human_violated_rules": "[]",
            "metadata_rules": "{'The cup accelerates downward.': 'Gravity'}",
        },
        {
            "caption": "A bike turns.",
            "upsampled_caption": "",
            "video_url": (
                "https://storage.cdn-luma.com/dream_machine/aaaa-bbbb/cccc-dddd_result.mp4"
            ),
            "sa": 2, "pc": 2, "joint": 0, "action": "cycling", "is_hard": 0,
            "physics_rules_followed": "[]",
            "physics_rules_unfollowed": "['The bike leans into the turn.']",
            "physics_rules_cannot_be_determined": "[]",
            "human_violated_rules": "the wheels never rotate",
            "metadata_rules": "{'The bike leans into the turn.': ['Inertia', 'Friction']}",
        },
        {
            "caption": "Unknown generator.",
            "upsampled_caption": "A rope snaps under load.",
            "video_url": base + "futuremodel_v9/rope.mp4",
            "sa": 3, "pc": 3, "joint": 0, "action": "", "is_hard": 0,
            "physics_rules_followed": "[]", "physics_rules_unfollowed": "[]",
            "physics_rules_cannot_be_determined": "[]", "human_violated_rules": "[]",
            "metadata_rules": "{}",
        },
        {
            "caption": "Long name one.",
            "upsampled_caption": "x",
            "video_url": base + "wan_videophy2_test_hard_upsampled/" + "A" * 140 + "_first.mp4",
            "sa": 1, "pc": 1, "joint": 0, "action": "a", "is_hard": 1,
            "physics_rules_followed": "[]", "physics_rules_unfollowed": "[]",
            "physics_rules_cannot_be_determined": "[]", "human_violated_rules": "[]",
            "metadata_rules": "{}",
        },
        {
            "caption": "Long name two.",
            "upsampled_caption": "x",
            "video_url": base + "wan_videophy2_test_hard_upsampled/" + "A" * 140 + "_second.mp4",
            "sa": 1, "pc": 1, "joint": 0, "action": "a", "is_hard": 1,
            "physics_rules_followed": "[]", "physics_rules_unfollowed": "[]",
            "physics_rules_cannot_be_determined": "[]", "human_violated_rules": "[]",
            "metadata_rules": "{}",
        },
        {
            "caption": "Truncated file name.",
            "upsampled_caption": "x",
            "video_url": base + "hunyuan_xdit/A_yo-yo_is_tossed_against_a_brick_wall",
            "sa": 5, "pc": 4, "joint": 1, "action": "yoyo", "is_hard": 0,
            "physics_rules_followed": "[]", "physics_rules_unfollowed": "[]",
            "physics_rules_cannot_be_determined": "[]", "human_violated_rules": "[]",
            "metadata_rules": "{}",
        },
    ]
    fields = list(rows[0].keys()) + ["Unnamed: 13"]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, "Unnamed: 13": ""})


def test_synthetic_edges(tmp: Path) -> None:
    csv_path = tmp / "tiny.csv"
    write_synthetic(csv_path)
    root = tmp / "videos"
    (root / "sora_hard_videophy2").mkdir(parents=True)
    (root / "sora_hard_videophy2" / "cup.mp4").write_bytes(b"\x00")

    ds = VideoPhy2Dataset(csv_path, root, split="test")
    assert len(ds) == 6
    assert len({s.video_id for s in ds}) == 6, "synthetic ids collided"
    # no model_name column at all, so every name is derived from the URL
    assert [s.model_name for s in ds] == [
        "sora", "ray2", "futuremodel_v9", "wan", "wan", "hunyuan",
    ], [s.model_name for s in ds]

    cup, bike, rope, first, second, truncated = list(ds)
    assert cup.exists and cup.video_path == root / "sora_hard_videophy2" / "cup.mp4"
    assert not bike.exists and bike.rel_path == "dream_machine/cccc-dddd_result.mp4"
    assert cup.rules_cannot_be_determined == ()
    assert bike.human_violated_rules == ("the wheels never rotate",)
    assert bike.rule_laws["The bike leans into the turn."] == ("Inertia", "Friction")
    assert bike.prompt_for_generation() == "A bike turns."
    assert rope.action == "" and rope.category == ""
    assert first.video_id != second.video_id and len(first.video_id) <= 100
    assert truncated.video_path.name.endswith("brick_wall"), truncated.video_path.name

    # missing files are reported, never raised
    assert len(ds.missing) == 5 and len(ds.filter()) == 1
    assert ds.stats()["n_missing"] == 5

    # an empty view must still report and serialise: sweeps dump both
    empty = ds.filter(pc=99, has_video=None)
    assert len(empty) == 0 and empty.stats()["n"] == 0
    assert len(empty.stratified_subset(5)) == 0
    json.dumps({"stats": ds.stats(), "sample": cup.as_dict()})

    # from_config: absent keys fall back to the documented layout, present keys win
    fallback = VideoPhy2Dataset.from_config({"llm": {}}, split="test")
    assert fallback.csv_path == TEST_CSV and fallback.videos_root == VIDEOS
    assert len(fallback) == 3397
    train = VideoPhy2Dataset.from_config({}, split="train")
    assert train.csv_path == TRAIN_CSV and len(train) == 3343
    cfg = {"data": {"videophy2": {"test_csv": str(csv_path), "videos_root": str(root)}}}
    tiny = VideoPhy2Dataset.from_config(cfg, split="test")
    assert len(tiny) == 6 and tiny.csv_path == csv_path

    # proportional allocation over uneven strata: pc=1 holds twice the rows of
    # any other score, so it takes twice the quota and the total still hits n
    skewed = VideoPhy2Dataset(csv_path, root, split="test", samples=list(ds) * 20)
    sub = skewed.stratified_subset(30, seed=3, by=("pc",))
    assert len(sub) == 30, len(sub)
    assert dict(sorted(Counter(s.pc for s in sub).items())) == {
        1: 10, 2: 5, 3: 5, 4: 5, 5: 5,
    }, Counter(s.pc for s in sub)
    print(f"  synthetic edges ok: ids={[s.video_id[:28] for s in ds][:3]}")


def main() -> int:
    assert TEST_CSV.exists(), f"missing {TEST_CSV}"
    print("test_parsers");             test_parsers()
    print("test_resolution_rule");     test_resolution_rule()
    print("test_video_id_rules");      test_video_id_rules()
    print("test_allocate");            test_allocate_invariants()

    ds = load_full()
    print("test_real_test_split");     test_real_test_split(ds)
    print("test_row_level_parsing");   test_row_level_parsing(ds)
    print("test_filters");             test_filters_do_not_mutate(ds)
    print("test_stratified_subset");   test_stratified_subset(ds)
    print("test_train_split");         test_train_split()
    with tempfile.TemporaryDirectory() as d:
        print("test_synthetic_edges"); test_synthetic_edges(Path(d))
    print("\nALL EVAL DATASET TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
