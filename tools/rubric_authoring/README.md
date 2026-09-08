# Rubric authoring scripts

One-shot tooling used to author the rubrics under `rubrics/` and the PhyGenBench
law audit under `audit/`. Nothing at runtime imports these — they are kept so the
rubrics can be revised and regenerated.

## Naming

Prefix = dataset + purpose:

| Prefix   | Purpose                          | Output                        |
|----------|----------------------------------|-------------------------------|
| `pgb_*`  | PhyGenBench law audit            | `audit/phygenbench/`          |
| `pgbr_*` | PhyGenBench rubrics              | `rubrics/phygenbench/` (160)  |
| `pwbr_*` | PhyWorldBench rubrics            | `rubrics/phyworldbench/` (315)|
| `v2add`  | VideoPhy-2 rubric helper         | `rubrics/videophy2/`          |

Suffix = physics category chunk. PhyGenBench: chem, force, heat, light, props.
PhyWorldBench: biomech, deform, energy, fluid, interaction, kinematics, light,
rigid, scale.

Roles: `pgb.py` / `pgbadd.py` / `pwbadd.py` / `v2add.py` are the shared helpers
(`S()`, `P()`, `add()`, `flush()`); `*_run.py` are the drivers; `render_audit.py`
turns `_audit.json` into `AUDIT.md`.

The bulk of each `pgbr_*` / `pwbr_*` file is rubric content written as Python
literals, not logic — that is what makes them large.

## Running

    python3 pgb_run.py  chem force heat light props
    python3 pgbr_run.py chem force heat light props
    python3 pwbr_run.py biomech deform energy fluid interaction kinematics light rigid scale

All chunks for one dataset must run in a single process: the batch list
(`pwbadd.B` and friends) is in-memory and only written on `flush()`. Running a
driver with no arguments flushes an empty batch — don't.

Drivers resolve their chunks relative to this file, so cwd does not matter.
