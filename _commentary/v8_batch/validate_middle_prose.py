#!/usr/bin/env python3
"""Validate ledger-free V5 middle-layer prose against its editorial source."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys

try:
    from _commentary.v8_batch import validate_concise
except ModuleNotFoundError:  # Direct execution from the repository root.
    import validate_concise  # type: ignore[no-redef]


QURAN_INTERVAL_RE = re.compile(
    r"(?<![\w])\d{1,3}:\d{1,3}\s*[-‐‑‒–—−]\s*(?:\d{1,3}:)?\d{1,3}(?!\w)"
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+")


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    output_paragraph: int | None = None
    line: int | None = None


def _words(text: str) -> int:
    return len(text.split())


def structural_metrics(
    source_text: str, prose_text: str, *, ayah_ref: str
) -> dict[str, int | float]:
    """Derive transient synthesis diagnostics without a persisted ledger."""

    source = validate_concise.prose_paragraphs(source_text)
    prose = validate_concise.prose_paragraphs(prose_text)
    source_words = _words(source_text)
    output_words = _words(prose_text)
    multi_source = 0
    single_source = 0
    same_position_singleton = 0
    for output_number, paragraph in enumerate(prose, start=1):
        cited = {
            number
            for cited_ayah, numbers in validate_concise.citation_groups(paragraph)
            if cited_ayah == ayah_ref
            for number in numbers
        }
        if len(cited) > 1:
            multi_source += 1
        elif len(cited) == 1:
            single_source += 1
            if cited == {output_number}:
                same_position_singleton += 1
    return {
        "source_word_count": source_words,
        "output_word_count": output_words,
        "retained_word_ratio": output_words / source_words if source_words else 0.0,
        "source_paragraph_count": len(source),
        "output_paragraph_count": len(prose),
        "output_to_source_paragraph_ratio": len(prose) / len(source) if source else 0.0,
        "multi_source_output_paragraphs": multi_source,
        "single_source_output_paragraphs": single_source,
        "same_position_singleton_paragraphs": same_position_singleton,
        "multi_source_output_paragraph_ratio": (
            multi_source / len(prose) if prose else 0.0
        ),
    }


def _malformed_citation_present(paragraph: str) -> bool:
    """Return true when any paragraph marker is outside a valid citation."""

    masked = list(paragraph)
    for match in validate_concise.CITATION_RE.finditer(paragraph):
        if validate_concise.PARAGRAPH_LIST_RE.fullmatch(match.group("body")):
            masked[match.start() : match.end()] = " " * (match.end() - match.start())
    return "¶" in "".join(masked)


def validate(
    source_text: str,
    prose_text: str,
    *,
    ayah_ref: str,
    max_paragraph_words: int = 180,
) -> list[Finding]:
    """Return every deterministic prose-only contract violation."""

    findings: list[Finding] = []
    for item in validate_concise.validate_pair(
        source_text, prose_text, ayah_ref=ayah_ref
    ):
        code = "empty_prose" if item.code == "empty_concise" else item.code
        message = item.message.replace("Concise edition", "Middle prose").replace(
            "concise prose", "middle prose"
        )
        findings.append(Finding(code, message, item.output_paragraph))

    prose_paragraphs = validate_concise.prose_paragraphs(prose_text)
    existing = {(item.code, item.output_paragraph) for item in findings}
    for paragraph_number, paragraph in enumerate(prose_paragraphs, start=1):
        if (
            _malformed_citation_present(paragraph)
            and ("malformed_citation", paragraph_number) not in existing
        ):
            findings.append(
                Finding(
                    "malformed_citation",
                    "Citation must use `(S:A ¶N, ¶N)` with explicit paragraph numbers.",
                    paragraph_number,
                )
            )

        for match in validate_concise.CITATION_RE.finditer(paragraph):
            if not validate_concise.PARAGRAPH_LIST_RE.fullmatch(match.group("body")):
                continue
            numbers = [
                int(item.group("number"))
                for item in validate_concise.PARAGRAPH_REF_RE.finditer(
                    match.group("body")
                )
            ]
            if len(numbers) != len(set(numbers)):
                findings.append(
                    Finding(
                        "duplicate_paragraph_citation",
                        "A citation must not repeat the same source paragraph number.",
                        paragraph_number,
                    )
                )

        for match in QURAN_INTERVAL_RE.finditer(paragraph):
            findings.append(
                Finding(
                    "quran_interval_shorthand",
                    f"List every ayah explicitly instead of using {match.group(0)!r}.",
                    paragraph_number,
                )
            )

        paragraph_words = _words(paragraph)
        if max_paragraph_words > 0 and paragraph_words > max_paragraph_words:
            findings.append(
                Finding(
                    "overdense_output_paragraph",
                    f"Paragraph has {paragraph_words} words; maximum is "
                    f"{max_paragraph_words}.",
                    paragraph_number,
                )
            )

    for line_number, line in enumerate(prose_text.splitlines(), start=1):
        heading = HEADING_RE.match(line)
        if heading is not None and len(heading.group("marks")) != 2:
            findings.append(
                Finding(
                    "heading_level",
                    "Middle prose headings must use level 2 (`##`).",
                    line=line_number,
                )
            )

    return findings


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate ledger-free V5 middle prose against editorial prose."
    )
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--prose", required=True, type=Path)
    parser.add_argument("--ayah-ref", required=True)
    parser.add_argument("--max-paragraph-words", type=int, default=180)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    missing = [path for path in (args.source, args.prose) if not path.is_file()]
    if missing:
        findings = [Finding("missing_file", f"Missing file: {path}") for path in missing]
        if args.json:
            print(
                json.dumps(
                    {
                        "status": "failed",
                        "findings": [asdict(item) for item in findings],
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            for finding in findings:
                print(f"{finding.code}: {finding.message}", file=sys.stderr)
        return 1

    source_text = _read(args.source)
    prose_text = _read(args.prose)
    findings = validate(
        source_text,
        prose_text,
        ayah_ref=args.ayah_ref,
        max_paragraph_words=args.max_paragraph_words,
    )
    metrics = structural_metrics(source_text, prose_text, ayah_ref=args.ayah_ref)
    if args.json:
        print(
            json.dumps(
                {
                    "status": "failed" if findings else "ok",
                    "metrics": metrics,
                    "findings": [asdict(item) for item in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif findings:
        for finding in findings:
            location = args.ayah_ref
            if finding.output_paragraph is not None:
                location += f" output ¶{finding.output_paragraph}"
            if finding.line is not None:
                location += f" line {finding.line}"
            print(f"{location}: {finding.code}: {finding.message}", file=sys.stderr)
    else:
        print(
            "ok: "
            f"{metrics['source_word_count']} -> {metrics['output_word_count']} words; "
            f"{metrics['source_paragraph_count']} -> "
            f"{metrics['output_paragraph_count']} paragraphs; "
            f"{metrics['multi_source_output_paragraphs']} multi-source; "
            f"{metrics['same_position_singleton_paragraphs']} same-position "
            "singletons"
        )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
