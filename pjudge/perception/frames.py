"""Frame access for the inspection agent: the only path from video to pixels.

Two things this layer exists to guarantee:

1. Every frame handed to a model is counted (`FrameServer.frames_served`). The
   observation budget is a reported quantity, so it cannot be measured by the
   agent that spends it.
2. Timestamps map to frames deterministically, and looking at the same moment
   twice is free. Physical violations occupy short windows, so the loop revisits
   the same instants repeatedly; without caching that is the dominant cost.

`zoom` upsamples the crop rather than merely cropping. Prior judges feed whole
frames throughout, which is exactly what destroys small-region violations.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np

from ..schema import BBox, TimeSpan


def resize_long_side(img: np.ndarray, long_side: int | None) -> np.ndarray:
    """Scale so the longer side equals `long_side`, preserving aspect ratio."""
    if not long_side:
        return img
    h, w = img.shape[:2]
    scale = long_side / max(h, w)
    if abs(scale - 1.0) < 0.02:
        return img
    interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC
    return cv2.resize(img, (max(1, round(w * scale)), max(1, round(h * scale))), interpolation=interp)


@dataclass
class VideoMeta:
    path: str
    fps: float
    duration: float
    n_frames: int
    width: int
    height: int
    decoded_frames: int
    decode_stride: int

    def as_dict(self) -> dict[str, float | int | str]:
        return {
            "path": self.path,
            "fps": round(self.fps, 3),
            "duration": round(self.duration, 3),
            "n_frames": self.n_frames,
            "width": self.width,
            "height": self.height,
            "decoded_frames": self.decoded_frames,
            "decode_stride": self.decode_stride,
        }


class FrameServer:
    """Serves frames of one video by timestamp.

    Generated clips in VideoPhy-2 are a few seconds long, so the whole video is
    decoded sequentially on first use and kept in memory. Sequential decoding
    avoids the frame-accuracy problems of seeking with cv2 on VFR/B-frame files,
    which would silently misalign every timestamp we report.
    """

    def __init__(self, path: str | Path, max_decode_frames: int = 900):
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(self.path)
        self.max_decode_frames = max_decode_frames
        self.frames_served = 0 # 记录已经向 Observer 提供了多少帧，初始为 0。
        self._frames: list[np.ndarray] | None = None
        self._times: list[float] = []
        self._meta: VideoMeta | None = None

    # -- metadata ----------------------------------------------------------

    @property
    def meta(self) -> VideoMeta:
        self._ensure_decoded()
        assert self._meta is not None
        return self._meta

    @property
    def duration(self) -> float:
        return self.meta.duration

    @property
    def size(self) -> tuple[int, int]:
        return self.meta.width, self.meta.height

    # -- decoding ----------------------------------------------------------

    def _ensure_decoded(self) -> None:
        if self._frames is not None:
            return
        cap = cv2.VideoCapture(str(self.path))
        if not cap.isOpened():
            raise RuntimeError(f"cannot open video: {self.path}")
        fps = cap.get(cv2.CAP_PROP_FPS) or 0.0 # 读取帧率
        claimed = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        # Container metadata is unreliable; stride is a guess refined below.
        stride = max(1, int(np.ceil(claimed / self.max_decode_frames))) if claimed else 1

        frames: list[np.ndarray] = [] # 保存图片
        times: list[float] = [] # 保存对应时间戳
        idx = 0 # 当前读取到第几帧
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if idx % stride == 0:
                frames.append(frame)
                times.append(idx / fps if fps > 0 else float(idx))
            idx += 1
            if len(frames) >= self.max_decode_frames and stride == 1 and not claimed:
                stride = 2  # unknown length and getting long: start subsampling
        cap.release()

        if not frames:
            raise RuntimeError(f"decoded zero frames from {self.path}")
        if fps <= 0:  # some generated clips carry no fps; assume 24 and say so
            fps = 24.0
            times = [i * stride / fps for i in range(len(frames))]

        self._frames = frames
        self._times = times
        h, w = frames[0].shape[:2]
        self._meta = VideoMeta(
            path=str(self.path),
            fps=fps,
            duration=(idx / fps) if fps > 0 else float(idx), # 计算视频时长
            n_frames=idx,
            width=w,
            height=h,
            decoded_frames=len(frames),
            decode_stride=stride,
        )

    # -- sampling ----------------------------------------------------------

    def _index_at(self, t: float) -> int:
        self._ensure_decoded()
        if not self._times:
            return 0
        pos = int(np.searchsorted(self._times, t))
        if pos == 0:
            return 0
        if pos >= len(self._times):
            return len(self._times) - 1
        before, after = self._times[pos - 1], self._times[pos]
        return pos - 1 if (t - before) <= (after - t) else pos

    def frame_at(self, t: float, long_side: int | None = None) -> tuple[float, np.ndarray]:
        """Nearest decoded frame to timestamp `t`, with its true timestamp."""
        i = self._index_at(t)
        self.frames_served += 1
        return self._times[i], resize_long_side(self._frames[i], long_side)  # type: ignore[index]

    # 从视频的某个时间范围内抽取若干帧，并返回每帧的真实时间戳和图片
    # 它支持两种采样方式：
    # 方式一：指定 n_frames，在时间段内均匀抽固定数量的帧
    # 方式二：指定 fps，按照每秒多少帧进行抽帧
    def sample(
        self,
        span: TimeSpan | None = None, # 抽取哪个时间段
        n_frames: int | None = None, # 希望抽取多少帧
        fps: float | None = None, # 希望每秒抽取多少帧
        long_side: int | None = None,
    ) -> list[tuple[float, np.ndarray]]:
        """Frames from `span`, either `n_frames` evenly spaced or at `fps`.

        Returns unique frames only: asking for more frames than the span holds
        yields what exists rather than duplicates, so frame counts stay honest.
        """
        self._ensure_decoded() # 确保视频已解码
        span = (span or TimeSpan(0.0, self.duration)).clipped_to(self.duration)
        if n_frames is None and fps is None:
            n_frames = 8 # 默认均匀抽8帧
        if fps is not None:
            step = 1.0 / max(fps, 1e-6) # 每隔多少秒抽一帧
            targets = list(np.arange(span.start, max(span.end, span.start + 1e-9), step)) # 希望获取的时间
            if n_frames:
                targets = targets[:n_frames]
        elif n_frames == 1:
            targets = [(span.start + span.end) / 2]
        else:
            targets = list(np.linspace(span.start, span.end, int(n_frames)))

        out: list[tuple[float, np.ndarray]] = [] # 最终返回的帧
        seen: set[int] = set() # 记录已经使用过的帧索引
        for t in targets:
            i = self._index_at(float(t)) # 找到距离目标时间最近的真实帧
            if i in seen: # 删除重复帧
                continue
            seen.add(i)
            out.append((self._times[i], resize_long_side(self._frames[i], long_side)))  # 保存时间戳和图片
        self.frames_served += len(out)
        return out

    def overview( # 对整个视频做一次低成本的全局浏览
        self,
        max_frames: int = 16,
        fps: float = 1.0,
        long_side: int = 512,
        min_frames: int = 8,
    ) -> list[tuple[float, np.ndarray]]:
        """Cheap whole-video pass used to ground or drop prompt priors.

        `fps` is a floor on density, not a cap on count. Generated clips are
        often 2-6s, where a fixed 1 fps yields 2-6 frames -- too few to establish
        what is even in the video, which is what this pass exists for.
        """
        n = max_frames
        if fps and fps > 0:
            n = min(max_frames, max(min_frames, int(np.ceil(self.duration * fps))))
        return self.sample(None, n_frames=n, long_side=long_side) # 从整个视频均匀抽帧

    def zoom( # 获取视频某个时间点的画面，裁剪出指定区域，再把这个区域放大后返回。
        self,
        t: float,
        bbox: BBox,
        long_side: int = 1024,
        margin: float = 0.04,
        min_side: float = 0.12,
    ) -> tuple[float, np.ndarray]:
        """A magnified crop: cropped, then upsampled to `long_side`.

        `margin`/`min_side` keep some context and stop tiny boxes from becoming
        unreadable slivers -- a 2%-area box upsampled alone is mostly noise.
        """
        self._ensure_decoded()
        i = self._index_at(t)
        frame = self._frames[i]  # type: ignore[index]
        h, w = frame.shape[:2]
        box = bbox.padded(margin, min_side)
        x0, y0, x1, y1 = box.to_pixels(w, h)
        x1, y1 = max(x1, x0 + 2), max(y1, y0 + 2)
        crop = frame[y0:y1, x0:x1]
        self.frames_served += 1
        return self._times[i], resize_long_side(crop, long_side)

    def zoom_clip( # 在一段时间内，对同一个画面区域连续抽取并放大多帧，用来观察物理异常如何随时间发展
        self,
        span: TimeSpan,
        bbox: BBox,
        n_frames: int = 6,
        long_side: int = 768,
        **zoom_kwargs,
    ) -> list[tuple[float, np.ndarray]]:
        """Same region across time -- how a violation's evolution is inspected."""
        span = span.clipped_to(self.duration)
        targets = (
            [(span.start + span.end) / 2]
            if n_frames == 1
            else list(np.linspace(span.start, span.end, n_frames))
        )
        out: list[tuple[float, np.ndarray]] = []
        seen: set[int] = set()
        for t in targets:
            i = self._index_at(float(t))
            if i in seen:
                continue
            seen.add(i)
            out.append(self.zoom(float(t), bbox, long_side=long_side, **zoom_kwargs))
        return out


def save_frames( # 把 inspection agent 实际看过的视频帧保存成 JPEG 文件，并返回路径。
    frames: list[tuple[float, np.ndarray]],
    out_dir: str | Path,
    prefix: str,
    jpeg_quality: int = 92,
) -> list[str]:
    """Persist what the inspection agent saw, so claims can be audited later."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for t, img in frames:
        p = out / f"{prefix}_t{t:07.3f}.jpg"
        cv2.imwrite(str(p), img, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
        paths.append(str(p))
    return paths
