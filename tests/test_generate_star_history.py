from __future__ import annotations

import datetime as dt
import xml.etree.ElementTree as ET
import urllib.error

import pytest

from scripts.generate_star_history import github_json, render_svg, update_history


class _FakeResponse:
    def __init__(self, body: bytes) -> None:
        self._body = body

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def read(self) -> bytes:
        return self._body


def test_update_history_keeps_one_sample_per_day() -> None:
    history = [(dt.date(2026, 7, 18), 523)]

    assert update_history(history, dt.date(2026, 7, 18), 524) == [
        (dt.date(2026, 7, 18), 524)
    ]
    assert update_history(history, dt.date(2026, 7, 19), 524) == [
        (dt.date(2026, 7, 18), 523),
        (dt.date(2026, 7, 19), 524),
    ]


def test_render_svg_produces_branded_star_history_card() -> None:
    svg = render_svg(
        "917Dhj/DeepPaperNote",
        [(dt.date(2026, 4, 1), 1), (dt.date(2026, 4, 2), 3)],
        generated_at=dt.datetime(2026, 4, 3, 12, 30, tzinfo=dt.timezone.utc),
    )

    root = ET.fromstring(svg)

    assert root.tag.endswith("svg")
    assert root.attrib["viewBox"] == "0 0 960 560"
    assert "917Dhj/DeepPaperNote" in svg
    assert "3 stars" in svg
    assert "2026-04-03 12:30 UTC" in svg
    assert "#0e1729" in svg
    assert "#2e4264" in svg
    assert "#f3f6fb" in svg
    assert "#99abc7" in svg
    assert "#77a2ff" in svg
    assert "#d69a4a" in svg


def test_github_json_uses_bearer_token_when_available(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GITHUB_TOKEN", "token-123")
    seen_headers: dict[str, str | None] = {}

    def fake_urlopen(request: object, timeout: int) -> _FakeResponse:
        request_headers = getattr(request, "headers")
        seen_headers["Authorization"] = request_headers.get("Authorization")
        assert timeout == 45
        return _FakeResponse(b'{"stargazers_count": 42}')

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    github_json("https://api.github.com/repos/owner/repo", retries=0)

    assert seen_headers["Authorization"] == "Bearer " + "token-123"


def test_github_json_retries_and_surfaces_rate_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    sleeps: list[int] = []
    attempts = 0

    def fake_urlopen(request: object, timeout: int) -> _FakeResponse:
        nonlocal attempts
        attempts += 1
        raise urllib.error.HTTPError(
            getattr(request, "full_url"),
            403,
            "rate limit exceeded",
            {"Retry-After": "1"},
            None,
        )

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    monkeypatch.setattr("time.sleep", lambda seconds: sleeps.append(seconds))

    with pytest.raises(RuntimeError, match="rate limit persisted after 3 attempts"):
        github_json("https://api.github.com/repos/owner/repo", retries=2)

    assert attempts == 3
    assert sleeps == [1, 1]
