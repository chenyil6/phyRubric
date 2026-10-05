# Blind annotations (Claude Sonnet 5.5)

One JSON per (split, generator): `train/<tag>.json`, `eval/<tag>.json`. Each file is an object with header fields
(`purpose`, `annotator`, `date`, `split`, `tag`, `n_clips`, ...) and a `clips` list; one record per video.

Record: `id`, `tag`, `category`, `video`, `caption`, `sa_score`, `pc_score` (computed by teacher/scoring.py from the
item statuses, never emitted by the annotator), `recognisable_attempt`, `clip_confidence`, `clip_confidence_reason`,
`clip_summary`, `items` (every SA and PC item with `status` and `evidence`; PC items also carry `expect`, `fail`,
`matched_fail`; the universal fatal item carries `source` = supplementary_judged | inferred_pass | blind), `uncovered`.

Labelling protocol: teacher/review/labelling/INSTRUCTIONS.md (blind: caption + rubric + frames only). Rubric version:
7 PC items including the scene-wide universal fatal item (rubrics/_policy.json universal_pc_item, 2026-10-01).
Scoring and reporting definitions: teacher/review/train_blind_sonnet_distribution.md (§10, §15); `python teacher/report.py train/*.json`.

- `train/`: 2,841 clips = 947 rubrics x CogVideoX1.5-5B, LTX-Video-2B-0.9.8-distilled, Wan2.2-T2V-A14B. Same records as
  `teacher/review/train_blind_sonnet.json` (kept as is), split by generator. Universal item: 537 judged, 2,304 inferred pass.
- `eval/`: benchmark reference labels, 1,462 clips = 245 eval rubrics x CogVideoX1.5-5B, HunyuanVideo-1.5-480p,
  LTX-Video-2B-0.9.8-distilled, Wan2.2-T2V-A14B, Wan2.2-TI2V-5B (245 each) + Cosmos-Predict2.5-2B (237; 8 captions blocked
  by its safety filter, see data/drafts/cosmos_blocklist_screen.json). All 7 PC items blind-judged (no inferred statuses).
  Labelled 2026-10-04/05 by Claude Sonnet 5.5 subagents, 5 clips per task, 287 tasks.
- `archive/`: pre-universal train labels; the 30-clip Hunyuan eval pilot (its 30 clips are merged into eval/HunyuanVideo-1.5-480p.json).
