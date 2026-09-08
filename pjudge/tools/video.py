"""The five frame-selection tools used by the rubric inspection agent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..perception.frames import FrameServer
from ..schema import BBox, TimeSpan, Tool, ToolCall, bbox_from_any, span_from_any


@dataclass
class ToolOutput:
    frames: list[tuple[float, np.ndarray]]
    description: str

    @property
    def timestamps(self) -> list[float]:
        return [timestamp for timestamp, _ in self.frames]


class VideoToolbox:
    def __init__(
        self,
        frames: FrameServer,
        overview_long_side: int = 512,
        clip_long_side: int = 768,
        region_long_side: int = 1024,
    ):
        self.frames = frames
        self.overview_long_side = overview_long_side
        self.clip_long_side = clip_long_side
        self.region_long_side = region_long_side

    def execute(self, call: ToolCall) -> ToolOutput:
        args = call.arguments
        if call.tool is Tool.OVERVIEW:
            return self._overview(args)
        if call.tool is Tool.INSPECT_CLIP:
            return self._clip(args)
        if call.tool is Tool.INSPECT_REGION:
            return self._region(args)
        if call.tool is Tool.COMPARE_FRAMES:
            return self._compare(args)
        if call.tool is Tool.PRESENCE_CHECK:
            return self._presence(args)
        raise ValueError(f"unsupported tool {call.tool}")

    def _overview(self, args: dict[str, Any]) -> ToolOutput:
        n = _integer(args.get("n_frames"), 12, 1, 32)
        got = self.frames.sample(n_frames=n, long_side=self.overview_long_side)
        return ToolOutput(got, "uniform overview of the complete video")

    def _clip(self, args: dict[str, Any]) -> ToolOutput:
        span = span_from_any(args.get("span"), self.frames.duration) or TimeSpan(0, self.frames.duration)
        n = _integer(args.get("n_frames"), 8, 1, 32)
        fps = _positive_float(args.get("fps"))
        # Keep n_frames even when fps is supplied: FrameServer uses it as a hard
        # cap after constructing the fps-based timestamps.
        got = self.frames.sample(span, n_frames=n, fps=fps, long_side=self.clip_long_side)
        return ToolOutput(got, f"full-frame clip from {span.start:.2f}s to {span.end:.2f}s")

    def _region(self, args: dict[str, Any]) -> ToolOutput:
        span = span_from_any(args.get("span"), self.frames.duration) or TimeSpan(0, self.frames.duration)
        bbox = _required_bbox(args)
        n = _integer(args.get("n_frames"), 8, 1, 32)
        got = self.frames.zoom_clip(span, bbox, n_frames=n, long_side=self.region_long_side)
        return ToolOutput(got, f"magnified region over {span.start:.2f}s to {span.end:.2f}s")

    def _compare(self, args: dict[str, Any]) -> ToolOutput:
        raw = args.get("timestamps")
        if not isinstance(raw, list) or len(raw) < 2:
            raise ValueError("compare_frames requires at least two timestamps")
        timestamps = sorted({max(0.0, min(float(t), self.frames.duration)) for t in raw})[:16]
        bbox = bbox_from_any(args.get("bbox"))
        got = [
            self.frames.zoom(t, bbox, long_side=self.region_long_side)
            if bbox is not None
            else self.frames.frame_at(t, long_side=self.clip_long_side)
            for t in timestamps
        ]
        unique: dict[float, np.ndarray] = {}
        for timestamp, image in got:
            unique.setdefault(timestamp, image)
        return ToolOutput(list(unique.items()), "selected keyframes for direct before/after comparison")

    def _presence(self, args: dict[str, Any]) -> ToolOutput:
        subject = str(args.get("subject") or "").strip()
        if not subject:
            raise ValueError("presence_check requires a subject")
        span = span_from_any(args.get("span"), self.frames.duration) or TimeSpan(0, self.frames.duration)
        bbox = bbox_from_any(args.get("bbox"))
        n = _integer(args.get("n_frames"), 12, 1, 32)
        got = (
            self.frames.zoom_clip(span, bbox, n_frames=n, long_side=self.region_long_side)
            if bbox is not None
            else self.frames.sample(span, n_frames=n, long_side=self.clip_long_side)
        )
        return ToolOutput(got, f"dense presence check for {subject!r}")


def _required_bbox(args: dict[str, Any]) -> BBox:
    bbox = bbox_from_any(args.get("bbox"))
    if bbox is None:
        raise ValueError("inspect_region requires a valid normalised bbox")
    return bbox


def _integer(value: Any, default: int, lo: int, hi: int) -> int:
    try:
        return max(lo, min(hi, int(value)))
    except (TypeError, ValueError):
        return default


def _positive_float(value: Any) -> float | None:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if result > 0 else None
