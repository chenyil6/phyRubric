"""Compatibility imports; new code should use :mod:`pjudge.runtime`."""

from .runtime import JudgeRuntime, PhysicalJudge, RuntimeConfig

BudgetConfig = RuntimeConfig

__all__ = ["BudgetConfig", "JudgeRuntime", "PhysicalJudge", "RuntimeConfig"]
