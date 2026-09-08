"""`ask_json`'s two failure paths, which are not the same failure.

All four hard failures of the n=150 run were "model reply is not JSON: ''" and all
four were the pixel-seeing role -- the one with images and the longest answers. An
empty reply from a reasoning model is not a formatting mistake; it is a response
whose entire output budget went to thinking. Complaining about the format cannot
fix it, so the empty case retries with a doubled cap and the prompt untouched,
while a malformed-but-present reply keeps the old corrective retry.

Keeping the prompt identical on the empty path matters for a second reason: it is
the same question, so the run stays reproducible, and the raised cap is what moves
the cache key.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pjudge.agents.base import ask_json  # noqa: E402
from pjudge.backends.llm import LLMConfig, LLMResponse, Usage  # noqa: E402


class ScriptedClient:
    """Returns canned reply texts and records what it was asked with."""

    def __init__(self, texts, token_param: str = "max_completion_tokens"):
        self.role = "inspection"
        self.texts = list(texts)
        self.usage = Usage()
        self.cfg = LLMConfig(
            model="m", base_url="http://x/v1", api_key="k", max_tokens=4096
        )
        self.seen: list[dict] = []
        self._token_param = token_param

    @property
    def token_param(self) -> str:
        return self._token_param

    def ask(self, prompt, system=None, images=None, json_mode=False, **kw):
        self.seen.append({"prompt": prompt, "kw": dict(kw)})
        return LLMResponse(
            text=self.texts.pop(0), model="m", role=self.role,
            usage=Usage(calls=1), cached=False,
        )

    def caps(self) -> list[int | None]:
        return [s["kw"].get(self._token_param) for s in self.seen]


def test_empty_reply_raises_the_cap():
    c = ScriptedClient(["", json.dumps({"ok": 1})])
    assert ask_json(c, "sys", "PROMPT") == {"ok": 1}
    assert c.caps() == [None, 8192], c.caps()
    assert c.seen[1]["prompt"] == "PROMPT", "the prompt was altered on an empty reply"
    print(f"  empty reply ok: caps {c.caps()}, prompt untouched")


def test_repeated_empties_keep_doubling():
    c = ScriptedClient(["", "   ", json.dumps({"ok": 2})])
    assert ask_json(c, "sys", "P") == {"ok": 2}
    assert c.caps() == [None, 8192, 16384], c.caps()
    assert {s["prompt"] for s in c.seen} == {"P"}, "prompt drifted across retries"
    print(f"  repeated empties ok: caps {c.caps()}")


def test_token_param_name_is_taken_from_the_client():
    """Endpoints downgraded to the other spelling must still get a valid request."""
    c = ScriptedClient(["", json.dumps({"ok": 3})], token_param="max_tokens")
    assert ask_json(c, "sys", "P") == {"ok": 3}
    assert c.seen[1]["kw"] == {"max_tokens": 8192}, c.seen[1]["kw"]
    print("  token param ok: raised under the name this endpoint accepts")


def test_malformed_reply_still_gets_the_complaint():
    c = ScriptedClient(["not json at all", json.dumps({"ok": 4})])
    assert ask_json(c, "sys", "P") == {"ok": 4}
    assert c.caps() == [None, None], c.caps()
    assert "could not be used" in c.seen[1]["prompt"], c.seen[1]["prompt"]
    print("  malformed reply ok: corrected by prompt, cap left alone")


def test_json_array_is_not_an_object():
    c = ScriptedClient([json.dumps([1, 2]), json.dumps({"ok": 5})])
    assert ask_json(c, "sys", "P") == {"ok": 5}
    assert "got list" in c.seen[1]["prompt"], c.seen[1]["prompt"]
    print("  array reply ok: rejected as not an object")


def test_exhaustion_names_the_role():
    c = ScriptedClient(["", "", ""])
    try:
        ask_json(c, "sys", "P")
    except ValueError as exc:
        message = str(exc)
    else:
        raise AssertionError("three empty replies did not raise")
    assert "inspection agent produced no usable JSON" in message, message
    assert len(c.seen) == 3, len(c.seen)
    print(f"  exhaustion ok: {message[:64]}")


TESTS = [
    test_empty_reply_raises_the_cap,
    test_repeated_empties_keep_doubling,
    test_token_param_name_is_taken_from_the_client,
    test_malformed_reply_still_gets_the_complaint,
    test_json_array_is_not_an_object,
    test_exhaustion_names_the_role,
]


def main() -> int:
    for fn in TESTS:
        print(fn.__name__)
        fn()
    print(f"\nALL {len(TESTS)} ASK_JSON TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
