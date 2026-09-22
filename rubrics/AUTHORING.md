# Writing a rubric

One rubric per caption at `rubrics/<split>/<branch>/<ID>.json`. The 50 files already there were
reviewed and approved; match them in structure, length and tone. `_policy.json` is the contract
(record format, scoring, what is not penalised, branch notes); this file is the working method.

Inputs for one caption (from `python3 rubrics/assign.py show ...`): `id`, `caption`, `category`,
`subcategory`, `violation_types` (1-3 of the ten), `expectation` (hidden field: how the outcome should
unfold; seed for the core PC items, never copied into SA). Read the subcategory note in
`data/schema.json` (`subcategory_notes`) and the branch note in `_policy.json` (`branch_notes`).

## The record

```json
{"id": "ACOU-0001", "caption": "<verbatim data caption>",
 "sa": [{"id": "S1", "weight": "core|minor", "check": "..."}, ...],
 "pc": [{"id": "P1", "severity": "fatal|core|major|minor", "type": "<violation_type>", "expect": "...", "fail": "...", "precondition": "..."}, ...],
 "note": "optional"}
```

British spelling (colour, centre), present tense, plain words, no numbers with units, no camera or
image-quality language. Write with `json.dumps(obj, indent=2, ensure_ascii=False) + "\n"`.

## SA: does the clip show what the caption says?

- One item per visible fact the caption requires: the objects, the action, the stated outcome.
  Nothing the caption does not say. Nothing about physics or quality; SA never asks "plausibly".
- `core` = facts without which the clip is not this caption (the objects, the action, the outcome).
  `minor` = qualifiers the caption states (once, slowly, a single hit, sunny, wooden) and the
  ordering item.
- Order: core items first, in the order the caption states them; then minor qualifiers; the ordering
  item last. When the caption names several sub-actions, each is its own item plus one item asking
  whether they happen in the caption's order ("The strike comes first and the jump follows").
- 4-6 items. At least two core and one minor (build.py enforces). Every item must be decidable on any
  clip: SA is never not_shown.
- A stated outcome ("the light comes on", "the grains jump") is an SA item. Whether what is shown is
  physically possible is PC's job; both can fail on one clip.

## PC: is what the clip shows physically possible?

Six items is the norm (5-7 allowed, 4-8 hard limit). Fixed order:

1. **core** items, one per declared `violation_type` where it is the central mechanism, in the order
   the event unfolds (before the cause, at the cause, after it). These are built from `expectation`.
2. **major** items: accompanying physics of side elements (gravity on a secondary object, material
   response, trajectory, a secondary consequence). Pick the ones this scene actually puts at risk.
3. **fatal** item, second to last: the whole-clip object invariants (`permanence_count`,
   `shape_identity` or `solidity`, whichever fits): nothing appears, vanishes, merges, morphs or
   passes through anything. Name the scene's objects.
4. **minor** `attribute_drift` item, last: colour, texture, label, position of untouched things.

Every declared `violation_type` must be the `type` of at least one item (build.py warns). `type` names
the axis a FAIL counts toward; pick the closest of the ten.

### expect and fail

`expect` says what a correct clip shows and, by doing so, tells the judge WHICH moment, region or
event the item is about. `fail` is the only ground for a FAIL: two to four concrete visible events,
joined by "; or", each something a viewer can point at in the frames.

- fail is NOT the negation of expect. "The grains lie still until the strike" -> fail: "Grains bounce or
  shift before the stick reaches the head; or jump with the stick nowhere near; or stay still as the
  stick hits." Three distinct ways it goes wrong, each pointable.
- Direction and order only, never magnitude or rate: "the drip runs upward" yes; "melts too fast",
  "does not melt enough", "bounces too high" no. A correct clip in which the process has barely
  advanced must pass.
- No unseen causes: heat sources, current, sound, wind, breath and hands are routinely out of frame.
  Never write a fail clause that needs the cause to be visible.
- Not violations: blur, flicker, resolution, colour cast, style, set dressing, self-driven agents
  starting or stopping, athletic form.
- Ban vague words: unrealistic, implausible, physically, properly, correctly, natural, smoothly.
  Name the event instead.
- No two items with the same fail text; keep items from overlapping (the fatal item does not repeat
  the core item's clauses).

### precondition

Only for scene content the caption does not guarantee (loose objects in the car, a reflective
surface that may or may not be in view). When the precondition does not occur, the item is
not_shown. The unconditional set must still contain a core, a major, a minor and a fatal item
(build.py enforces). Items about things the caption guarantees never get a precondition.

### note

Optional, one or two sentences, only when needed: why a person is kept (only when the body IS the
physics), what is deliberately not judged, or how the judge must read an ambiguity in the caption.

## Branch reminders (see `_policy.json` branch_notes for the full text)

- Mechanics: rates, exact rebound heights and stopping distances are not judged, only direction and
  order. People/animals/powered vehicles may start, stop and turn on their own.
- Heat: the source is usually invisible; judge the material's response by direction and monotonicity
  (softer, wetter, blacker, never back). Steam and smoke rise, melt runs down. Browning and other
  chemistry are outside the branch.
- Optics: geometry only: which side, attached to what, moving with what, at the same moment. Never
  brightness, softness or colour accuracy. Reflections judged only where a reflective surface is in view.
- Electricity: the cause is invisible; judge the link between the visible control and the visible
  device (timing, direction, staying on/off) and the visible behaviour of sparks, bolts, magnets.
- Acoustics: sound is neither visible nor audible; judge visible causes (strike, moving cone) and
  visible effects (grains jump, water ripples). If no source is visible, the effect alone is not a
  violation.

## Checklist before you finish an id

- caption is a verbatim copy; file name equals id; ids S1..Sn, P1..Pn sequential.
- SA: >=2 core, >=1 minor, ordering item last if the caption has several sub-actions, nothing the
  caption did not say.
- PC: declared violation_types covered; unconditional core + major + minor + fatal; fail clauses are
  concrete, "or"-joined, no magnitude, no unseen cause, no vague words; order core -> major -> fatal -> minor.
- `python3 rubrics/build.py check --ids <your ids>` reports 0 errors and 0 warnings.
