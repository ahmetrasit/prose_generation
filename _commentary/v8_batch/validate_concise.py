#!/usr/bin/env python3
"""Validate paragraph-traceable concise editions of V5 editorial prose."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
import re
import sys


CITATION_RE = re.compile(r"\((?P<surah>\d+):(?P<ayah>\d+) (?P<body>[^()]*)\)")
PARAGRAPH_REF_RE = re.compile(r"¶(?P<number>\d+)")
PARAGRAPH_LIST_RE = re.compile(r"¶\d+(?:, ¶\d+)*")


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    output_paragraph: int | None = None


def prose_paragraphs(text: str) -> list[str]:
    """Return non-heading Markdown blocks in reader order."""

    return [
        block.strip()
        for block in re.split(r"\n\s*\n", text.strip())
        if block.strip() and not re.match(r"^#{1,6}\s", block.strip())
    ]


def citation_groups(text: str) -> list[tuple[str, list[int]]]:
    groups: list[tuple[str, list[int]]] = []
    for match in CITATION_RE.finditer(text):
        body = match.group("body")
        if not PARAGRAPH_LIST_RE.fullmatch(body):
            continue
        groups.append(
            (
                f"{int(match.group('surah'))}:{int(match.group('ayah'))}",
                [int(item.group("number")) for item in PARAGRAPH_REF_RE.finditer(body)],
            )
        )
    return groups


def validate_pair(
    source_text: str,
    concise_text: str,
    *,
    ayah_ref: str,
) -> list[Finding]:
    source = prose_paragraphs(source_text)
    concise = prose_paragraphs(concise_text)
    findings: list[Finding] = []
    cited: set[int] = set()

    if not source:
        findings.append(Finding("empty_source", "Editorial source has no prose paragraphs."))
    if not concise:
        findings.append(Finding("empty_concise", "Concise edition has no prose paragraphs."))

    for output_number, paragraph in enumerate(concise, start=1):
        groups = citation_groups(paragraph)
        if not groups:
            findings.append(
                Finding(
                    "uncited_output_paragraph",
                    "Every concise prose paragraph must end in or contain a paragraph citation.",
                    output_number,
                )
            )
        if "¶" in paragraph and not groups:
            findings.append(
                Finding(
                    "malformed_citation",
                    "Citation must use `(S:A ¶N, ¶N)` with explicit paragraph numbers.",
                    output_number,
                )
            )
        for cited_ayah, numbers in groups:
            if cited_ayah != ayah_ref:
                findings.append(
                    Finding(
                        "wrong_ayah_citation",
                        f"Expected {ayah_ref}, found {cited_ayah}.",
                        output_number,
                    )
                )
                continue
            for number in numbers:
                if number < 1 or number > len(source):
                    findings.append(
                        Finding(
                            "paragraph_out_of_range",
                            f"{ayah_ref} ¶{number} is outside 1..{len(source)}.",
                            output_number,
                        )
                    )
                else:
                    cited.add(number)

    missing = [number for number in range(1, len(source) + 1) if number not in cited]
    if missing:
        findings.append(
            Finding(
                "source_coverage",
                "Uncited source paragraph(s): "
                + ", ".join(f"{ayah_ref} ¶{number}" for number in missing),
            )
        )

    source_words = len(source_text.split())
    concise_words = len(concise_text.split())
    if source_words and concise_words >= source_words:
        findings.append(
            Finding(
                "not_shorter",
                f"Concise edition has {concise_words} words; source has {source_words}.",
            )
        )
    return findings


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _pair_paths(
    *, repo_root: Path, analysis_id: str, surah: int, ayah: int, language: str
) -> tuple[Path, Path]:
    stem = f"{surah}_{ayah}"
    surah_dir = f"s{surah:03d}"
    source = (
        repo_root
        / "_commentary"
        / "v5"
        / "editorial"
        / analysis_id
        / surah_dir
        / stem
        / f"{stem}.prose.editorial.{language}.md"
    )
    concise = (
        repo_root
        / "_commentary"
        / "v5"
        / "concise"
        / analysis_id
        / surah_dir
        / stem
        / f"{stem}.prose.concise.{language}.md"
    )
    return source, concise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate source-paragraph coverage in V5 concise prose."
    )
    parser.add_argument("--analysis-id", required=True)
    parser.add_argument("--surah", required=True, type=int)
    parser.add_argument("--ayah-count", required=True, type=int)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    repo_root = args.repo_root or Path(__file__).resolve().parents[2]
    reports: list[dict[str, object]] = []
    failed = False

    for ayah in range(1, args.ayah_count + 1):
        ayah_ref = f"{args.surah}:{ayah}"
        source_path, concise_path = _pair_paths(
            repo_root=repo_root,
            analysis_id=args.analysis_id,
            surah=args.surah,
            ayah=ayah,
            language=args.language,
        )
        missing_paths = [path for path in (source_path, concise_path) if not path.is_file()]
        if missing_paths:
            failed = True
            reports.append(
                {
                    "ayah_ref": ayah_ref,
                    "source_path": str(source_path),
                    "concise_path": str(concise_path),
                    "findings": [
                        asdict(Finding("missing_file", f"Missing file: {path}"))
                        for path in missing_paths
                    ],
                }
            )
            continue

        source_text = _read(source_path)
        concise_text = _read(concise_path)
        findings = validate_pair(source_text, concise_text, ayah_ref=ayah_ref)
        if findings:
            failed = True
        source_paragraph_count = len(prose_paragraphs(source_text))
        source_words = len(source_text.split())
        concise_words = len(concise_text.split())
        reports.append(
            {
                "ayah_ref": ayah_ref,
                "source_path": str(source_path.relative_to(repo_root)),
                "concise_path": str(concise_path.relative_to(repo_root)),
                "source_sha256": _sha256(source_text),
                "concise_sha256": _sha256(concise_text),
                "source_paragraphs": source_paragraph_count,
                "cited_source_paragraphs": source_paragraph_count
                if not any(item.code == "source_coverage" for item in findings)
                else None,
                "source_words": source_words,
                "concise_words": concise_words,
                "retained_word_ratio": round(concise_words / source_words, 4)
                if source_words
                else None,
                "findings": [asdict(item) for item in findings],
            }
        )

    result = {
        "schema_version": "commentary-v5-concise-validation-v1",
        "analysis_id": args.analysis_id,
        "surah": args.surah,
        "ayah_count": args.ayah_count,
        "language": args.language,
        "status": "failed" if failed else "ok",
        "reports": reports,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif failed:
        for report in reports:
            for finding in report.get("findings", []):
                location = report["ayah_ref"]
                if finding.get("output_paragraph"):
                    location += f" output ¶{finding['output_paragraph']}"
                print(f"{location}: {finding['code']}: {finding['message']}", file=sys.stderr)
    else:
        total_source = sum(int(report["source_words"]) for report in reports)
        total_concise = sum(int(report["concise_words"]) for report in reports)
        total_paragraphs = sum(int(report["source_paragraphs"]) for report in reports)
        print(
            f"ok: {total_paragraphs} source paragraphs cited; "
            f"{total_source} -> {total_concise} words "
            f"({total_concise / total_source:.1%})"
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
