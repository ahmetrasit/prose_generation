#!/usr/bin/env python3
"""Mechanical downstream-safety validator for V6 prose files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
import unicodedata


BRACE_CANDIDATE_RE = re.compile(r"\{[^{}\n]*\}")
PLACEHOLDER_RE = re.compile(r"@@[^@\n]+@@")
ARABIC_SCRIPT_PATTERN = (
    r"[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufefc]"
)
ARABIC_SCRIPT_RE = re.compile(ARABIC_SCRIPT_PATTERN)
ARABIC_SPAN_RE = re.compile(f"{ARABIC_SCRIPT_PATTERN}+")
STRICT_TAG_RE = re.compile(
    r"\{\s*ar\s*:\s*(?P<ar>[^{},\n]*?)\s*,\s*"
    r"tr\s*:\s*(?P<tr>[^{},\n]*?)\s*,\s*"
    r"gloss\s*:\s*(?P<gloss>[^{}\n]*?)\s*\}"
)
FIELD_MARKER_RE = re.compile(
    r"(?:^|,)\s*(?P<prefix>:?)\s*(?P<name>[A-Za-z_][A-Za-z0-9_-]*)\s*:"
)
FIELD_CONTENT_MARKER_RE = re.compile(r"(?P<name>[A-Za-z_][A-Za-z0-9_-]*)\s*:")
WRAPPER_LABEL_RE = re.compile(r"^\s*={3,}\s*[^=\n]*\s*={3,}\s*$")
MARKDOWN_WRAPPER_LABEL_RE = re.compile(
    r"^\s*#{1,6}\s*(?:the\s+)?prose\s*$", re.IGNORECASE
)
XML_WRAPPER_LABEL_RE = re.compile(r"^\s*</?prose>\s*$", re.IGNORECASE)
FENCE_OPEN_RE = re.compile(r"^\s{0,3}(?P<marker>`{3,}|~{3,}).*$")


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    line: int
    code: str
    message: str


def _finding(path: Path, line: int, code: str, message: str) -> Finding:
    return Finding("error", str(path), line, code, message)


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _short(value: str, limit: int = 32) -> str:
    value = " ".join(value.split())
    if len(value) <= limit:
        return value
    return f"{value[: limit - 1]}..."


def _field_is_empty(value: str) -> bool:
    marker = FIELD_CONTENT_MARKER_RE.search(value)
    if marker:
        value = value[: marker.start()]
    return not value.strip().strip(",").strip()


def _has_arabic_letter(text: str) -> bool:
    return any(
        ARABIC_SCRIPT_RE.fullmatch(character)
        and (
            unicodedata.category(character).startswith("L")
            or unicodedata.category(character) == "So"
        )
        for character in text
    )


def _parse_tag_fields(token: str) -> tuple[dict[str, str], list[str], list[str]]:
    inner = token[1:-1]
    strict = STRICT_TAG_RE.fullmatch(token)
    if strict:
        return (
            {
                "ar": strict.group("ar").strip(),
                "tr": strict.group("tr").strip(),
                "gloss": strict.group("gloss").strip(),
            },
            ["ar", "tr", "gloss"],
            [],
        )

    matches = list(FIELD_MARKER_RE.finditer(inner))
    if not matches or inner[: matches[0].start()].strip():
        return {}, [], ["malformed_tag"]

    names = [match.group("name") for match in matches]
    values: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(inner)
        name = match.group("name")
        if name not in values:
            values[name] = inner[start:end].strip()
    errors: list[str] = ["malformed_tag"]
    if len(set(names)) != len(names):
        errors.append("duplicate_tag_field")
    return values, names, errors


def _validate_tag(path: Path, line_number: int, token: str) -> list[Finding]:
    errors: list[Finding] = []
    fields, names, parse_errors = _parse_tag_fields(token)
    unknown = sorted(set(names) - {"ar", "tr", "gloss"})
    missing = [name for name in ("ar", "tr", "gloss") if name not in names]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    hidden_names = sorted(
        {
            match.group("name")
            for value in fields.values()
            for match in FIELD_CONTENT_MARKER_RE.finditer(value)
        }
    )
    hidden_unknown = [name for name in hidden_names if name not in {"ar", "tr", "gloss"}]
    hidden_duplicates = [name for name in hidden_names if name in {"ar", "tr", "gloss"}]
    delimiter_residue = any(
        value.startswith(",") or value.endswith(",") or ",," in value
        for value in fields.values()
    )

    if unknown or hidden_unknown:
        errors.append(
            _finding(
                path,
                line_number,
                "unknown_tag_field",
                f"Unsupported field(s): {', '.join([*unknown, *hidden_unknown])}",
            )
        )
    if duplicates or hidden_duplicates:
        errors.append(
            _finding(
                path,
                line_number,
                "duplicate_tag_field",
                f"Duplicate field(s): {', '.join([*duplicates, *hidden_duplicates])}",
            )
        )
    if hidden_names and "malformed_tag" not in parse_errors:
        parse_errors.append("malformed_tag")
    if delimiter_residue and "malformed_tag" not in parse_errors:
        parse_errors.append("malformed_tag")
    if missing:
        errors.append(
            _finding(
                path,
                line_number,
                "missing_tag_field",
                f"Missing field(s): {', '.join(missing)}",
            )
        )
    if parse_errors:
        errors.append(
            _finding(
                path,
                line_number,
                "malformed_tag",
                "Malformed annotation",
            )
        )

    for name, code in (
        ("ar", "empty_arabic"),
        ("tr", "empty_transliteration"),
        ("gloss", "empty_gloss"),
    ):
        if name in fields and _field_is_empty(fields[name]):
            errors.append(
                _finding(path, line_number, code, f"Empty {name} field in annotation")
            )
    if "ar" in fields and not _has_arabic_letter(fields["ar"]):
        errors.append(
            _finding(
                path,
                line_number,
                "ar_field_not_arabic",
                "Tag ar field has no Arabic script",
            )
        )
    return errors


def _has_renderable_prose(text: str) -> bool:
    lines = text.lstrip("\ufeff").splitlines()
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                lines = lines[index + 1 :]
                break
        else:
            lines = []

    fence_marker: tuple[str, int] | None = None
    in_comment = False
    for line in lines:
        stripped = line.strip()
        if fence_marker:
            marker_char, marker_length = fence_marker
            close_re = rf"^\s{{0,3}}{re.escape(marker_char)}{{{marker_length},}}\s*$"
            if re.match(close_re, line):
                fence_marker = None
            continue
        if in_comment:
            if "-->" in stripped:
                in_comment = False
                stripped = stripped.split("-->", 1)[1].strip()
            else:
                continue
        if not stripped:
            continue
        if stripped.startswith("<!--"):
            if "-->" in stripped:
                stripped = stripped.split("-->", 1)[1].strip()
                if not stripped:
                    continue
            else:
                in_comment = True
                continue
        if line.startswith(("    ", "\t")):
            continue
        fence_match = FENCE_OPEN_RE.match(line)
        if fence_match:
            marker = fence_match.group("marker")
            fence_marker = (marker[0], len(marker))
            continue
        if re.match(r"^#{1,6}\s+.+$", stripped):
            continue
        if re.fullmatch(r"(?:[-*_]\s*){3,}", stripped):
            continue
        if XML_WRAPPER_LABEL_RE.match(stripped):
            continue
        return True
    return False


def validate_text(text: str, *, path: Path) -> list[Finding]:
    errors: list[Finding] = []
    if not text.strip().strip("\ufeff"):
        errors.append(_finding(path, 1, "empty_file", "Prose file is empty"))
        return errors

    for line_number, line in enumerate(text.splitlines(), start=1):
        if (
            WRAPPER_LABEL_RE.match(line)
            or MARKDOWN_WRAPPER_LABEL_RE.match(line)
            or XML_WRAPPER_LABEL_RE.match(line)
        ):
            errors.append(
                _finding(
                    path,
                    line_number,
                    "wrapper_label",
                    "Wrapper label",
                )
            )
        for placeholder in PLACEHOLDER_RE.finditer(line):
            errors.append(
                _finding(
                    path,
                    line_number,
                    "unresolved_placeholder",
                    f"Placeholder: {_short(placeholder.group(0))}",
                )
            )
        if "{{" in line or "}}" in line:
            errors.append(
                _finding(
                    path,
                    line_number,
                    "double_curly_tag",
                    "Double-curly tag",
                )
            )

    if text.count("{") != text.count("}"):
        errors.append(_finding(path, 1, "unbalanced_braces", "Unbalanced braces"))

    candidates = list(BRACE_CANDIDATE_RE.finditer(text))
    if len(candidates) != text.count("{"):
        errors.append(
            _finding(
                path,
                1,
                "malformed_or_nested_braces",
                "Malformed/nested/multiline braces",
            )
        )

    cleaned_parts: list[str] = []
    renderable_parts: list[str] = []
    cursor = 0
    for match in candidates:
        cleaned_parts.append(text[cursor : match.start()])
        renderable_parts.append(text[cursor : match.start()])
        line_number = _line_for_offset(text, match.start())
        token = match.group(0)
        tag_errors = _validate_tag(path, line_number, token)
        errors.extend(tag_errors)
        nested_candidate = (
            (match.start() > 0 and text[match.start() - 1] == "{")
            or (match.end() < len(text) and text[match.end()] == "}")
        )
        if tag_errors or nested_candidate:
            cleaned_parts.append(token)
            renderable_parts.append(token)
        else:
            cleaned_parts.append(" ")
            renderable_parts.append(" annotation ")
        cursor = match.end()
    cleaned_parts.append(text[cursor:])
    renderable_parts.append(text[cursor:])
    text_without_tags = "".join(cleaned_parts)
    text_for_renderability = "".join(renderable_parts)

    for match in ARABIC_SPAN_RE.finditer(text_without_tags):
        errors.append(
            _finding(
                path,
                _line_for_offset(text_without_tags, match.start()),
                "arabic_outside_tag",
                f"Arabic outside tag: {_short(match.group(0))}",
            )
        )

    if not _has_renderable_prose(text_for_renderability):
        errors.append(
            _finding(
                path,
                1,
                "no_renderable_prose",
                "No renderable prose",
            )
        )

    return errors


def validate_path(path: Path) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [_finding(path, 1, "missing_file", "Prose file does not exist")]
    except UnicodeDecodeError:
        return [_finding(path, 1, "invalid_utf8", "File is not valid UTF-8")]
    except OSError as exc:
        return [_finding(path, 1, "read_error", f"Cannot read prose file: {exc}")]
    return validate_text(text, path=path)


def _format_text(findings: list[Finding]) -> str:
    return "\n".join(
        f"{item.path}:{item.line}: {item.severity}: {item.code}: {item.message}"
        for item in findings
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="V6 prose file(s) to validate")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable findings")
    args = parser.parse_args(argv)

    findings: list[Finding] = []
    for path in args.paths:
        findings.extend(validate_path(path))

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
        print(_format_text(findings), file=sys.stderr)
    else:
        print("ok")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
