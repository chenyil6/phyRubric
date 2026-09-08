"""The public five-tool surface and its frame-budget bounds."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pjudge.perception.frames import FrameServer
from pjudge.schema import Tool, ToolCall
from pjudge.tools.video import VideoToolbox
from test_rubric_runtime import make_video


def call(tool: Tool, arguments: dict) -> ToolCall:
    return ToolCall("T1", tool, ["P1"], arguments)


def test_all_five_tools_execute(tmp_path: Path):
    toolbox = VideoToolbox(FrameServer(make_video(tmp_path / "tools.avi")))
    cases = [
        (Tool.OVERVIEW, {"n_frames": 5}),
        (Tool.INSPECT_CLIP, {"span": {"start": 0.1, "end": 1.2}, "fps": 100, "n_frames": 4}),
        (Tool.INSPECT_REGION, {"span": {"start": 0.1, "end": 1.2}, "bbox": {"x0": 0, "y0": 0, "x1": 0.5, "y1": 1}, "n_frames": 4}),
        (Tool.COMPARE_FRAMES, {"timestamps": [0.1, 0.5, 1.0]}),
        (Tool.PRESENCE_CHECK, {"subject": "the ball", "n_frames": 5}),
    ]
    for tool, arguments in cases:
        output = toolbox.execute(call(tool, arguments))
        assert 1 <= len(output.frames) <= arguments.get("n_frames", 16)
        assert output.description


def test_invalid_specialised_calls_fail(tmp_path: Path):
    toolbox = VideoToolbox(FrameServer(make_video(tmp_path / "bad.avi")))
    _raises("bbox", lambda: toolbox.execute(call(Tool.INSPECT_REGION, {"n_frames": 4})))
    _raises("timestamps", lambda: toolbox.execute(call(Tool.COMPARE_FRAMES, {"timestamps": [0.1]})))
    _raises("subject", lambda: toolbox.execute(call(Tool.PRESENCE_CHECK, {"subject": ""})))


def _raises(fragment: str, function) -> None:
    try:
        function()
    except ValueError as exc:
        assert fragment in str(exc)
    else:
        raise AssertionError(f"expected ValueError containing {fragment!r}")


def main() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        test_all_five_tools_execute(root)
        test_invalid_specialised_calls_fail(root)
    print("ALL VIDEO TOOL TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
