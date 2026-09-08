"""Unified LLM/VLM client shared by every pjudge agent.

All model traffic goes through this module so caching, retries and accounting
live in one place. The disk cache is not an optimisation: the agent loop is only
reproducible -- and ablations only comparable -- if an identical request never
reaches the API twice.

Frames are counted alongside tokens because the observation budget (how much of
the video the judge chose to look at) is a reported quantity, not an
implementation detail.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import random
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Sequence

import cv2
import numpy as np
from openai import OpenAI

ImageInput = str | Path | bytes | np.ndarray

_RETRYABLE_STATUS = {408, 409, 429, 500, 502, 503, 504, 529}


@dataclass
class Usage:
    """Running cost of one client, or of a whole run when summed."""

    calls: int = 0
    cache_hits: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    images: int = 0

    def add(self, other: "Usage") -> None:
        self.calls += other.calls
        self.cache_hits += other.cache_hits
        self.prompt_tokens += other.prompt_tokens
        self.completion_tokens += other.completion_tokens
        self.images += other.images

    def as_dict(self) -> dict[str, int]:
        return {
            "calls": self.calls,
            "cache_hits": self.cache_hits,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "images": self.images,
        }


@dataclass
class LLMConfig:
    model: str
    base_url: str
    api_key: str
    temperature: float | None = 0.0
    seed: int | None = 1234
    max_tokens: int = 4096
    reasoning_effort: str | None = None
    timeout: float = 180.0
    max_retries: int = 5
    cache_dir: Path = Path(".pjudge_cache/llm")
    image_detail: str = "high"
    jpeg_quality: int = 92

    @classmethod
    def from_dict(cls, cfg: dict[str, Any], role: str = "default") -> "LLMConfig":
        """Build the config for one agent role from the `llm` block of the yaml.

        A role whose entry in `llm.roles` is null inherits `default_model`; that
        is the main-results setting where every agent shares one backbone.
        """
        model = (cfg.get("roles") or {}).get(role) or cfg["default_model"]
        key_env = cfg.get("api_key_env", "PJUDGE_API_KEY")
        api_key = os.environ.get(key_env, "")
        if not api_key:
            raise RuntimeError(
                f"environment variable {key_env} is unset; see .env.example"
            )
        base_url = cfg["base_url"]
        if not base_url or base_url == "xxx":
            raise RuntimeError("llm.base_url is still the 'xxx' placeholder")
        return cls(
            model=model,
            base_url=base_url,
            api_key=api_key,
            temperature=cfg.get("temperature", 0.0),
            seed=cfg.get("seed"),
            max_tokens=cfg.get("max_tokens", 4096),
            reasoning_effort=cfg.get("reasoning_effort"),
            timeout=cfg.get("timeout", 180.0),
            max_retries=cfg.get("max_retries", 5),
            cache_dir=Path(cfg.get("cache_dir", ".pjudge_cache/llm")),
            image_detail=cfg.get("image_detail", "high"),
            jpeg_quality=cfg.get("jpeg_quality", 92),
        )


@dataclass
class LLMResponse:
    text: str
    model: str
    role: str
    usage: Usage
    cached: bool
    finish_reason: str | None = None

    def json(self) -> Any:
        """Parse the reply as JSON, tolerating ```json fences."""
        return parse_json(self.text)


def parse_json(text: str) -> Any:
    """Parse a model reply as JSON.

    Kept separate from LLMResponse so agents can reuse it on text assembled
    from several replies. Raises ValueError with the offending text attached --
    agents turn that into a retry rather than a crash.
    """
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.split("```")[1] if "```" in stripped[3:] else stripped[3:]
        if stripped.lstrip().lower().startswith("json"):
            stripped = stripped.lstrip()[4:]
    stripped = stripped.strip().strip("`").strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError as exc:
        start, end = stripped.find("{"), stripped.rfind("}")
        if start != -1 and end > start:
            try:
                return json.loads(stripped[start : end + 1])
            except json.JSONDecodeError:
                pass
        raise ValueError(f"model reply is not JSON: {text[:500]!r}") from exc


# --------------------------------------------------------------------------
# message construction
# --------------------------------------------------------------------------


def encode_image(image: ImageInput, jpeg_quality: int = 92) -> bytes:
    """Encode a frame or crop to JPEG bytes.

    ndarray input is assumed BGR, matching the perception layer's cv2 output.
    """
    if isinstance(image, np.ndarray):
        ok, buf = cv2.imencode(
            ".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
        )
        if not ok:
            raise ValueError("cv2 failed to encode frame")
        return buf.tobytes()
    if isinstance(image, bytes):
        return image
    return Path(image).read_bytes()


def image_part(
    image: ImageInput, detail: str = "high", jpeg_quality: int = 92
) -> dict[str, Any]:
    data = encode_image(image, jpeg_quality)
    b64 = base64.b64encode(data).decode("ascii")
    return {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": detail},
    }


def user_message(
    text: str,
    images: Sequence[ImageInput] | None = None,
    detail: str = "high",
    jpeg_quality: int = 92,
) -> dict[str, Any]:
    """A user turn, optionally carrying frames.

    Frames follow the text so the question is in context before the pixels.
    """
    if not images:
        return {"role": "user", "content": text}
    parts: list[dict[str, Any]] = [{"type": "text", "text": text}]
    parts.extend(image_part(im, detail, jpeg_quality) for im in images)
    return {"role": "user", "content": parts}


def _count_images(messages: Sequence[dict[str, Any]]) -> int:
    n = 0
    for msg in messages:
        content = msg.get("content")
        if isinstance(content, list):
            n += sum(1 for p in content if p.get("type") == "image_url")
    return n


def _fingerprint(messages: Sequence[dict[str, Any]], params: dict[str, Any]) -> str:
    """Stable cache key. Image payloads are hashed, not inlined."""
    norm: list[Any] = []
    for msg in messages:
        content = msg.get("content")
        if isinstance(content, list):
            parts = []
            for p in content:
                if p.get("type") == "image_url":
                    url = p["image_url"]["url"]
                    digest = hashlib.sha1(url.encode()).hexdigest()[:16]
                    parts.append(f"img:{digest}:{p['image_url'].get('detail')}")
                else:
                    parts.append(p.get("text", ""))
            norm.append([msg.get("role"), parts])
        else:
            norm.append([msg.get("role"), content])
    blob = json.dumps([norm, params], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode()).hexdigest()


# --------------------------------------------------------------------------
# client
# --------------------------------------------------------------------------


class LLMClient:
    """One configured model endpoint, used by one agent role.

    Retries, parameter-compat downgrades and caching are handled here so agent
    code stays about rubric decisions and evidence.
    """

    def __init__(self, cfg: LLMConfig, role: str = "default"):
        self.cfg = cfg
        self.role = role
        self.usage = Usage()
        # We do our own retrying so backoff and downgrades are logged.
        self._client = OpenAI(
            base_url=cfg.base_url,
            api_key=cfg.api_key,
            timeout=cfg.timeout,
            max_retries=0,
        )
        # Endpoints disagree about these; discovered once, then remembered.
        self._drop_temperature = cfg.temperature is None
        self._drop_seed = cfg.seed is None
        self._token_param = "max_tokens"
        self._cache_dir = Path(cfg.cache_dir) / cfg.model.replace("/", "_")
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        # Remembered across processes, keyed by endpoint: without this every new
        # process spends one live call per role rediscovering the downgrade, and
        # that call cannot hit the cache written by previous runs.
        self._caps_path = self._cache_dir / (
            f"_capabilities_{hashlib.sha1(cfg.base_url.encode()).hexdigest()[:8]}.json"
        )
        self._load_capabilities()

    # -- public API --------------------------------------------------------

    @property
    def token_param(self) -> str:
        """Name this endpoint accepts for the output-token cap.

        Public because a caller that wants to raise the cap for one retry cannot
        know whether this endpoint took `max_tokens` or was downgraded to
        `max_completion_tokens`; passing the wrong one is a 400, not a default.
        """
        return self._token_param

    def chat(
        self,
        messages: Sequence[dict[str, Any]],
        json_mode: bool = False,
        use_cache: bool = True,
        **extra: Any,
    ) -> LLMResponse:
        params = self._request_params(json_mode, extra)
        key = _fingerprint(messages, {**params, "model": self.cfg.model})
        n_images = _count_images(messages)

        if use_cache:
            hit = self._cache_read(key)
            if hit is not None:
                usage = Usage(
                    calls=1,
                    cache_hits=1,
                    prompt_tokens=hit["usage"].get("prompt_tokens", 0),
                    completion_tokens=hit["usage"].get("completion_tokens", 0),
                    images=n_images,
                )
                self.usage.add(usage)
                return LLMResponse(
                    text=hit["text"],
                    model=self.cfg.model,
                    role=self.role,
                    usage=usage,
                    cached=True,
                    finish_reason=hit.get("finish_reason"),
                )

        text, prompt_tok, completion_tok, finish, params_used = self._post(
            messages, json_mode, extra
        )
        usage = Usage(
            calls=1,
            prompt_tokens=prompt_tok,
            completion_tokens=completion_tok,
            images=n_images,
        )
        self.usage.add(usage)
        if use_cache:
            # Store under the parameters the endpoint actually accepted. This
            # call may have discovered that temperature/seed must be dropped, and
            # every later lookup will be built from the post-downgrade params --
            # writing under the original key would make the entry unreachable.
            write_key = _fingerprint(messages, {**params_used, "model": self.cfg.model})
            self._cache_write(
                write_key,
                {
                    "model": self.cfg.model,
                    "role": self.role,
                    "text": text,
                    "usage": {
                        "prompt_tokens": prompt_tok,
                        "completion_tokens": completion_tok,
                    },
                    "finish_reason": finish,
                },
            )
        return LLMResponse(
            text=text,
            model=self.cfg.model,
            role=self.role,
            usage=usage,
            cached=False,
            finish_reason=finish,
        )

    def ask(
        self,
        prompt: str,
        system: str | None = None,
        images: Sequence[ImageInput] | None = None,
        json_mode: bool = False,
        **extra: Any,
    ) -> LLMResponse:
        """Single-turn convenience wrapper (no conversation history)."""
        messages: list[dict[str, Any]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append(
            user_message(prompt, images, self.cfg.image_detail, self.cfg.jpeg_quality)
        )
        return self.chat(messages, json_mode=json_mode, **extra)

    # -- internals ---------------------------------------------------------

    def _request_params(self, json_mode: bool, extra: dict[str, Any]) -> dict[str, Any]:
        params: dict[str, Any] = {self._token_param: self.cfg.max_tokens}
        if not self._drop_temperature:
            params["temperature"] = self.cfg.temperature
        if not self._drop_seed:
            params["seed"] = self.cfg.seed
        if self.cfg.reasoning_effort:
            params["reasoning_effort"] = self.cfg.reasoning_effort
        if json_mode:
            params["response_format"] = {"type": "json_object"}
        params.update(extra)
        return params

    def _post(
        self, messages: Sequence[dict[str, Any]], json_mode: bool, extra: dict[str, Any]
    ) -> tuple[str, int, int, str | None, dict[str, Any]]:
        """Returns the reply plus the parameter set the endpoint accepted."""
        last_exc: Exception | None = None
        for attempt in range(self.cfg.max_retries):
            params = self._request_params(json_mode, extra)
            try:
                resp = self._client.chat.completions.create(
                    model=self.cfg.model, messages=list(messages), **params
                )
            except Exception as exc:  # noqa: BLE001 - re-raised below
                last_exc = exc
                if self._downgrade(exc):
                    continue  # unsupported parameter dropped; retry immediately
                if not self._is_retryable(exc) or attempt == self.cfg.max_retries - 1:
                    raise
                time.sleep(min(2**attempt + random.random(), 30.0))
                continue

            choice = resp.choices[0]
            text = choice.message.content or ""
            prompt_tok = getattr(resp.usage, "prompt_tokens", 0) or 0
            completion_tok = getattr(resp.usage, "completion_tokens", 0) or 0
            return text, prompt_tok, completion_tok, choice.finish_reason, params

        raise RuntimeError(f"{self.cfg.model} failed after retries") from last_exc

    def _downgrade(self, exc: Exception) -> bool:
        """Drop a parameter the endpoint rejects. Returns True if we changed one.

        Reasoning models commonly reject `temperature`/`seed` and require
        `max_completion_tokens`. Discovering this at runtime keeps one config
        working across the whole model list.
        """
        msg = str(exc).lower()
        if "max_tokens" in msg and "max_completion_tokens" in msg:
            if self._token_param == "max_tokens":
                self._token_param = "max_completion_tokens"
                self._save_capabilities()
                return True
        for name, flag in (("temperature", "_drop_temperature"), ("seed", "_drop_seed")):
            if name in msg and not getattr(self, flag):
                if any(w in msg for w in ("unsupported", "not supported", "unrecognized")):
                    setattr(self, flag, True)
                    self._save_capabilities()
                    return True
        return False

    def _load_capabilities(self) -> None:
        if not self._caps_path.exists():
            return
        try:
            caps = json.loads(self._caps_path.read_text())
        except (json.JSONDecodeError, OSError):
            return
        self._drop_temperature = self._drop_temperature or bool(caps.get("drop_temperature"))
        self._drop_seed = self._drop_seed or bool(caps.get("drop_seed"))
        self._token_param = caps.get("token_param", self._token_param)

    def _save_capabilities(self) -> None:
        payload = {
            "drop_temperature": self._drop_temperature,
            "drop_seed": self._drop_seed,
            "token_param": self._token_param,
        }
        try:
            tmp = self._caps_path.with_suffix(".tmp")
            tmp.write_text(json.dumps(payload, indent=2))
            tmp.replace(self._caps_path)
        except OSError:
            pass  # a read-only cache dir must not break judging

    @staticmethod
    def _is_retryable(exc: Exception) -> bool:
        status = getattr(exc, "status_code", None)
        if status is None:
            status = getattr(getattr(exc, "response", None), "status_code", None)
        if status in _RETRYABLE_STATUS:
            return True
        msg = str(exc).lower()
        return any(w in msg for w in ("timeout", "connection", "rate limit", "overload"))

    def _cache_path(self, key: str) -> Path:
        return self._cache_dir / key[:2] / f"{key}.json"

    def _cache_read(self, key: str) -> dict[str, Any] | None:
        path = self._cache_path(key)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            return None  # corrupt entry: fall through to a live call

    def _cache_write(self, key: str, payload: dict[str, Any]) -> None:
        path = self._cache_path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        tmp.replace(path)  # atomic, so concurrent judges never read half a file


def build_clients(
    llm_cfg: dict[str, Any], roles: Sequence[str] = ("inspection", "judge")
) -> dict[str, LLMClient]:
    """One client per agent role, all sharing the cache directory."""
    return {r: LLMClient(LLMConfig.from_dict(llm_cfg, r), role=r) for r in roles}
