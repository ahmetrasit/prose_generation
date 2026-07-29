#!/usr/bin/env python3
"""Shared helpers for the standalone Layer 3 workflow."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
WORKFLOW_ROOT = REPO_ROOT / "_channel" / "layer3"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"error: required file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: invalid JSON in {path}: {exc}") from exc


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as exc:
        raise SystemExit(f"error: required file does not exist: {path}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"error: invalid JSONL in {path}:{line_number}: {exc}"
            ) from exc
        if not isinstance(row, dict):
            raise SystemExit(
                f"error: expected object in {path}:{line_number}, got "
                f"{type(row).__name__}"
            )
        rows.append(row)
    return rows


def write_json(path: Path, value: Any, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        rendered = json.dumps(
            value, ensure_ascii=False, separators=(",", ":")
        )
    else:
        rendered = json.dumps(value, ensure_ascii=False, indent=2)
    path.write_text(
        rendered + "\n",
        encoding="utf-8",
    )


def source_base(source_ref: str) -> str:
    return source_ref.split("#", 1)[0]


def portable_path(
    path: Path,
    *,
    quran_data: Path | None = None,
    latent_activation: Path | None = None,
) -> str:
    resolved = path.resolve()
    roots = [(REPO_ROOT.resolve(), "prose_generation")]
    if quran_data is not None:
        roots.append((quran_data.resolve(), "quran-data"))
    if latent_activation is not None:
        roots.append((latent_activation.resolve(), "latent_activation"))
    for root, label in roots:
        try:
            return f"{label}/{resolved.relative_to(root).as_posix()}"
        except ValueError:
            continue
    return str(resolved)


def require_keys(value: dict[str, Any], keys: set[str], context: str) -> list[str]:
    return [
        f"{context}: missing required key {key!r}"
        for key in sorted(keys - value.keys())
    ]


def unique_values(values: list[str], context: str) -> list[str]:
    seen: set[str] = set()
    errors: list[str] = []
    for value in values:
        if value in seen:
            errors.append(f"{context}: duplicate value {value!r}")
        seen.add(value)
    return errors
