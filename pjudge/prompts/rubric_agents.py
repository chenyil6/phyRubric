"""Prompts for the two rubric-driven agents."""

INSPECTION_SYSTEM = """You are the Active Evidence Agent in a generated-video evaluator.
You receive a fixed caption-specific rubric and may inspect the video through tools.
You own both observation planning and item-level decisions, but you may not add,
delete, rewrite, or reprioritise rubric items. Judge only visible evidence and obey
the dataset policy. A failed PC item must match its stated failure condition; an
unseen cause is not a failure. Return one JSON object and no surrounding prose."""

PLAN_TASK = """Plan the next observation.

Caption:
{caption}

Video duration: {duration:.3f}s
Round: {round_no}/{max_rounds}; frames remaining: {frames_left}

Dataset policy:
{policy}

Rubric:
{rubric}

Current decisions:
{decisions}

Recorded evidence:
{evidence}

Tool calls already made:
{tool_calls}

Available tools:
- overview: arguments {{"n_frames": 4..32}}. Use for whole-video orientation.
- inspect_clip: arguments {{"span":{{"start":s,"end":s}}, "n_frames":2..32}}
  for dense full-frame temporal inspection.
- inspect_region: same plus a normalised bbox, for a magnified region over time.
- compare_frames: arguments {{"timestamps":[...], "bbox":optional}} for direct
  comparison of non-uniformly selected moments.
- presence_check: arguments {{"subject":"...", "span":..., "bbox":optional,
  "n_frames":4..32}} only when disappearance, reappearance, or occlusion is at issue.

One observation should cover several related rubric items when the same frames can
answer them. Prefer high-severity PC items and unresolved SA core items. Do not use
numeric measurement, standalone counting, or coordinate tracking.

Return either:
{{"action":"call_tool", "plan":"brief reason", "tool_call":{{"name":"overview|inspect_clip|inspect_region|compare_frames|presence_check", "rubric_ids":["S1","P1"], "arguments":{{...}}}}}}

or, only when every rubric item has a recorded decision:
{{"action":"finish", "plan":"why evidence is complete"}}"""

OBSERVE_TASK = """Answer the listed rubric items from these tool-result frames.

Caption: {caption}
Tool call: {tool_call}
Frame timestamps in order: {timestamps}
What was fetched: {description}

Relevant rubric items:
{items}

Dataset policy:
{policy}

Prior evidence for these items:
{prior_evidence}

First write one strictly visible observation covering these frames. Then provide a
finding only for an item these frames actually settle. SA findings are pass/fail.
PC findings are pass/fail/not_shown. For PC, not_shown means its precondition did
not occur or the required moment/region is not visible; it is not uncertainty about
physics. Do not decide items outside this tool call.

JSON:
{{"observation":"visible facts with timestamps", "limitations":"", "confidence":0.0,
 "recognisable_attempt":true,
 "findings":[{{"rubric_id":"P1", "status":"pass|fail|not_shown",
   "explanation":"why these frames settle it", "confidence":0.0}}]}}"""

JUDGE_SYSTEM = """You are the Scoring and Feedback Agent in a two-agent video judge.
The Active Evidence Agent has already inspected the video and made every rubric-item
decision. You do not invent or reinterpret visual facts. Audit the supplied links,
apply the supplied scoring policy, explain the result, and write actionable feedback
for failed items. Every feedback claim must cite recorded evidence. Return JSON only."""

JUDGE_TASK = """Produce the final score and report.

Caption: {caption}
Rubric: {rubric}
Policy: {policy}
Item decisions: {decisions}
Evidence: {evidence}
Tool-call trace: {tool_calls}

The deterministic scorer computed SA={sa_score}, PC={pc_score}. Recompute them from
the decisions and return those exact values. Summarise the principal failures, give
specific repair feedback only for failed items, and summarise how the important
items were inspected. Never cite an evidence id not listed above.

JSON:
{{"sa_score":1, "pc_score":1, "confidence":0.0, "summary":"...",
 "feedback":[{{"rubric_id":"P1", "evidence_ids":["E2"], "problem":"...",
   "suggested_fix":"..."}}],
 "trace_summary":"brief account of the important tool/evidence/decision chains"}}"""
