#!/usr/bin/env python3
"""Validate a V5 scope landing ledger against discovery and Markdown prose."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
from typing import Any


SCHEMA_VERSION = "commentary-v5-scope-landing-ledger-v1"
MAX_JSON_BYTES = 4_000_000


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


def _movement_refs(finding: dict[str, Any]) -> list[str]:
    refs = [
        "discovery:claim",
        "discovery:mechanism",
        "discovery:reader_payoff",
        "discovery:containment",
    ]
    refs.extend(
        f"obligation:{ref}"
        for ref in finding.get("semantic_obligation_refs", [])
        if isinstance(ref, str)
    )
    refs.extend(
        f"activation:{index}"
        for index, _activation in enumerate(finding.get("branch_activations", []))
    )
    refs.extend(
        f"connection:{ref}"
        for ref in finding.get("connection_refs", [])
        if isinstance(ref, str)
    )
    refs.extend(
        f"context:{ref}"
        for ref in finding.get("context_refs", [])
        if isinstance(ref, str)
    )
    return refs


def _paragraphs(text: str) -> list[str]:
    return [
        block.strip()
        for block in re.split(r"(?:\r?\n[ \t]*){2,}", text.strip())
        if block.strip()
    ]


def _load_json(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return None, [Finding("missing_file", f"File does not exist: {path}")]
    except OSError as exc:
        return None, [Finding("read_error", f"Cannot read {path}: {exc}")]
    if len(raw) > MAX_JSON_BYTES:
        return None, [Finding("file_too_large", f"JSON exceeds {MAX_JSON_BYTES} bytes: {path}")]
    try:
        value = json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError:
        return None, [Finding("invalid_utf8", f"File is not valid UTF-8: {path}")]
    except json.JSONDecodeError as exc:
        return None, [Finding("invalid_json", f"Invalid JSON in {path}: {exc}")]
    if not isinstance(value, dict):
        return None, [Finding("invalid_object", f"Expected one JSON object: {path}")]
    return value, []


def validate(
    discovery: dict[str, Any], ledger: dict[str, Any], prose: str
) -> list[Finding]:
    errors: list[Finding] = []
    expected_top = {"schema_version", "ayah_ref", "lane", "findings"}
    if set(ledger) != expected_top:
        errors.append(Finding("ledger_fields", "Ledger top-level fields are malformed"))
        return errors
    if ledger.get("schema_version") != SCHEMA_VERSION:
        errors.append(Finding("schema_version", "Ledger schema_version is stale"))
    for field in ("ayah_ref", "lane"):
        if ledger.get(field) != discovery.get(field):
            errors.append(Finding("identity_mismatch", f"Ledger {field} disagrees with discovery"))

    discovery_rows = discovery.get("findings")
    ledger_rows = ledger.get("findings")
    if not isinstance(discovery_rows, list) or not all(
        isinstance(row, dict) for row in discovery_rows
    ):
        errors.append(Finding("discovery_findings", "Discovery findings are malformed"))
        return errors
    if not isinstance(ledger_rows, list) or not all(
        isinstance(row, dict) for row in ledger_rows
    ):
        errors.append(Finding("ledger_findings", "Ledger findings are malformed"))
        return errors

    expected_ids = [row.get("finding_ref") for row in discovery_rows]
    actual_ids = [row.get("finding_ref") for row in ledger_rows]
    if actual_ids != expected_ids:
        errors.append(
            Finding("finding_order", "Ledger finding identity or order differs from discovery")
        )
        return errors

    paragraphs = _paragraphs(prose)
    if not paragraphs:
        errors.append(Finding("empty_prose", "Scope prose has no nonempty Markdown blocks"))
        return errors

    used_spans: list[tuple[int, int, str]] = []
    for index, (source, row) in enumerate(zip(discovery_rows, ledger_rows, strict=True)):
        label = source.get("finding_ref") or f"findings[{index}]"
        if set(row) != {"finding_ref", "landings"}:
            errors.append(Finding("finding_fields", f"{label}: ledger fields are malformed"))
            continue
        landings = row.get("landings")
        if not isinstance(landings, list) or not landings:
            errors.append(Finding("missing_landings", f"{label}: landings must be nonempty"))
            continue
        actual_refs: list[str] = []
        for landing_index, landing in enumerate(landings):
            landing_label = f"{label}.landings[{landing_index}]"
            if not isinstance(landing, dict) or set(landing) != {
                "movement_refs",
                "paragraph",
                "anchor",
            }:
                errors.append(Finding("landing_fields", f"{landing_label}: malformed landing"))
                continue
            movement_refs = landing.get("movement_refs")
            if not isinstance(movement_refs, list) or not movement_refs or not all(
                isinstance(ref, str) and ref for ref in movement_refs
            ):
                errors.append(
                    Finding("movement_refs", f"{landing_label}: movement_refs are malformed")
                )
                continue
            actual_refs.extend(movement_refs)
            paragraph = landing.get("paragraph")
            if not isinstance(paragraph, int) or isinstance(paragraph, bool) or not (
                1 <= paragraph <= len(paragraphs)
            ):
                errors.append(
                    Finding("paragraph", f"{landing_label}: paragraph is outside the prose")
                )
                continue
            anchor = landing.get("anchor")
            if not isinstance(anchor, str) or "\n" in anchor or len(anchor.strip()) < 12:
                errors.append(
                    Finding("anchor", f"{landing_label}: anchor must be a substantive single-line passage")
                )
                continue
            anchor = anchor.strip()
            if prose.count(anchor) != 1:
                errors.append(
                    Finding("anchor_unique", f"{landing_label}: anchor must occur exactly once in prose")
                )
                continue
            block = paragraphs[paragraph - 1]
            if block.count(anchor) != 1:
                errors.append(
                    Finding("anchor_paragraph", f"{landing_label}: anchor is not in the declared paragraph")
                )
                continue
            start = prose.index(anchor)
            end = start + len(anchor)
            if any(start < prior_end and prior_start < end for prior_start, prior_end, _ in used_spans):
                errors.append(
                    Finding("anchor_overlap", f"{landing_label}: anchor overlaps another landing")
                )
            used_spans.append((start, end, landing_label))

        expected_refs = _movement_refs(source)
        if actual_refs != expected_refs:
            errors.append(
                Finding(
                    "movement_coverage",
                    f"{label}: movement coverage is incomplete, duplicated, unknown, or reordered",
                )
            )
    return errors


def validate_paths(discovery_path: Path, prose_path: Path, ledger_path: Path) -> list[Finding]:
    discovery, errors = _load_json(discovery_path)
    ledger, ledger_errors = _load_json(ledger_path)
    errors.extend(ledger_errors)
    try:
        prose = prose_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(Finding("missing_file", f"File does not exist: {prose_path}"))
        prose = ""
    except UnicodeDecodeError:
        errors.append(Finding("invalid_utf8", f"File is not valid UTF-8: {prose_path}"))
        prose = ""
    except OSError as exc:
        errors.append(Finding("read_error", f"Cannot read {prose_path}: {exc}"))
        prose = ""
    if errors or discovery is None or ledger is None:
        return errors
    return validate(discovery, ledger, prose)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discovery", required=True, type=Path)
    parser.add_argument("--prose", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    findings = validate_paths(args.discovery, args.prose, args.ledger)
    if args.json:
        print(
            json.dumps(
                {
                    "status": "ok" if not findings else "error",
                    "findings": [item.__dict__ for item in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif findings:
        for item in findings:
            print(f"error: {item.code}: {item.message}", file=sys.stderr)
    else:
        print("ok")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
