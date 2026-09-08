"""A two-agent, rubric-driven judge for physical plausibility in video.

Agent 1 actively inspects frames and resolves fixed rubric items. Agent 2 turns
those evidence-linked decisions into scores, feedback, and a trace summary.
Python executes tools, assigns trace ids, validates links, and enforces scoring.
"""

__version__ = "0.1.0"
