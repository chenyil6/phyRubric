# data/drafts

Provenance of the caption review (2026-09-07 .. 2026-09-15). The live dataset is `data/train/*.json` and
`data/eval/*.json`; nothing here is read by the pipeline.

- `removed_<branch>.json` - every caption removed from a branch during review, with its original text and
  the reason (`reason` / `removed_reason`). Ids are the ORIGINAL ids of the branch (see the id maps in
  `data/<branch>_id_map.json`, which map original ids to final ids; `null` = removed).
- `archive/<branch>_draft.json` + `<branch>_draft_review.md` - the de-personing / 5-second rewrite drafts
  that were reviewed and applied with `scripts/apply_draft.py` (Heat used `scripts/triage_heat_draft.py`
  and `apply_heat_triage.py`; its triage tables are `archive/heat_draft_triage.*`). Kept only as the record of
  what changed and why; the scripts that produced them still point at the pre-archive paths.
- The raw LLM drafts of 2026-09-07 (`train_<branch>_<subcategory>_00.json`, `eval_<branch>_00.json`) were
  deleted on 2026-09-15: their content is the initial dataset at commit b55cde0.

Review principles are in Proposal.md section 4.1.
