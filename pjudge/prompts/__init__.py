"""Prompts for the two rubric-driven agents."""

from .rubric_agents import INSPECTION_SYSTEM, JUDGE_SYSTEM, JUDGE_TASK, OBSERVE_TASK, PLAN_TASK

# Shared only by the passive baseline.  The agentic system uses the fixed,
# caption-specific rubric and its deterministic severity caps instead.
PC_RUBRIC = """\
5 - No physical implausibility. Motion, contact, deformation and conservation
    all look as they would in reality.
4 - Physically sound apart from a minor artefact that does not change how the
    event unfolds.
3 - One clear violation, or several ambiguous ones; the event is still readable.
2 - Multiple clear violations, or one that breaks the core interaction.
1 - Pervasively impossible: objects morph, pass through each other, teleport, or
    the depicted interaction could not happen at all."""

__all__ = [
    "INSPECTION_SYSTEM",
    "PLAN_TASK",
    "OBSERVE_TASK",
    "JUDGE_SYSTEM",
    "JUDGE_TASK",
    "PC_RUBRIC",
]
