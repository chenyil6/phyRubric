"""Shared parsing and retry helpers for the two LLM agents."""

from __future__ import annotations

from typing import Any, Sequence

from ..backends.llm import ImageInput, LLMClient, parse_json


def ask_json(
    client: LLMClient,
    system: str,
    prompt: str,
    images: Sequence[ImageInput] | None = None,
    retries: int = 2,
    **kwargs: Any,
) -> dict[str, Any]:
    """Ask for a JSON object, retrying with the parse error fed back.

    Appending the error to the prompt changes the cache key, so the retry is a
    genuine second attempt rather than a replay of the cached bad reply.

    An EMPTY reply is retried differently, with a larger output-token cap rather
    than with a complaint. All four hard failures of the n=150 run were this case
    ("model reply is not JSON: ''"), always from the pixel-seeing role
    with images attached and the longest answers: a reasoning model that spends
    its whole budget thinking returns a well-formed response with no text in it.
    Telling it its reply was unusable does not buy it room to answer; raising the
    cap does.
    """
    attempt_prompt = prompt
    extra = dict(kwargs)
    last_error = ""
    for attempt in range(retries + 1):
        resp = client.ask(
            attempt_prompt, system=system, images=images, json_mode=True, **extra
        )
        try:
            data = parse_json(resp.text)
        except ValueError as exc:
            last_error = str(exc)
        else:
            if isinstance(data, dict):
                return data
            last_error = f"expected a JSON object, got {type(data).__name__}"
        if attempt < retries:
            if not resp.text.strip():
                # Keep the prompt identical so the retry is the same question, and
                # let the raised cap change the cache key on its own.
                cap = int(extra.get(client.token_param, client.cfg.max_tokens))
                extra[client.token_param] = cap * 2
            else:
                attempt_prompt = (
                    f"{prompt}\n\nYour previous reply could not be used: {last_error}\n"
                    "Reply with one valid JSON object and nothing else."
                )
    raise ValueError(f"{client.role} agent produced no usable JSON: {last_error}")


def as_float(value: Any, default: float = 0.0, lo: float = 0.0, hi: float = 1.0) -> float:
    """Model replies put numbers in strings, use nulls, and overshoot ranges."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return default
    if v != v:  # NaN
        return default
    return min(hi, max(lo, v))


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def as_text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip()
    return str(value)
