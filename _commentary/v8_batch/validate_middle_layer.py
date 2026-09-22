#!/usr/bin/env python3
"""Validate historical V2 middle-layer prose/ledger pairs."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys
from typing import Any

try:
    from _commentary.v8_batch import validate_concise
except ModuleNotFoundError:  # Direct script execution from the repository root.
    import validate_concise  # type: ignore[no-redef]


SCHEMA_VERSION = "commentary-v5-middle-claim-ledger-v2"
RELATION_CLASSES = {
    "unique",
    "exact_duplicate",
    "overlapping_complement",
    "related_distinct",
}
CLUSTER_KINDS = {"synthesis", "standalone"}
QURAN_INTERVAL_RE = re.compile(
    r"(?<![\w])\d{1,3}:\d{1,3}\s*[-‐‑‒–—−]\s*(?:\d{1,3}:)?\d{1,3}(?!\w)"
)
PROBLEM_AUDIT_KEYS = (
    "unassessed_source_paragraphs",
    "uncited_source_paragraphs",
    "unlanded_unit_refs",
    "unclustered_unit_refs",
    "units_with_nonunique_anchors",
    "unresolved_deduplication_questions",
    "unmerged_overlap_groups",
    "source_mirroring_findings",
    "polarity_or_modality_mismatches",
    "reader_paragraphs_without_detail_clues",
    "overdense_output_paragraphs",
)


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    unit_ref: str | None = None
    paragraph: int | None = None


def _words(text: str) -> int:
    return len(text.split())


def _finding(
    findings: list[Finding],
    code: str,
    message: str,
    *,
    unit_ref: str | None = None,
    paragraph: int | None = None,
) -> None:
    findings.append(Finding(code, message, unit_ref, paragraph))


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate(
    source_text: str,
    prose_text: str,
    ledger: dict[str, Any],
    *,
    ayah_ref: str,
    max_paragraph_words: int = 180,
) -> list[Finding]:
    """Return every mechanical middle-layer contract violation."""

    source = validate_concise.prose_paragraphs(source_text)
    prose = validate_concise.prose_paragraphs(prose_text)
    findings: list[Finding] = []

    for item in validate_concise.validate_pair(
        source_text, prose_text, ayah_ref=ayah_ref
    ):
        _finding(
            findings,
            f"prose_{item.code}",
            item.message,
            paragraph=item.output_paragraph,
        )

    if ledger.get("schema_version") != SCHEMA_VERSION:
        _finding(findings, "schema_version", f"Expected {SCHEMA_VERSION}.")
    if ledger.get("ayah_ref") != ayah_ref:
        _finding(findings, "ayah_ref", f"Expected {ayah_ref}.")
    if ledger.get("source_paragraph_count") != len(source):
        _finding(
            findings,
            "source_paragraph_count",
            f"Expected {len(source)} source paragraphs.",
        )
    if ledger.get("output_paragraph_count") != len(prose):
        _finding(
            findings,
            "output_paragraph_count",
            f"Expected {len(prose)} output paragraphs.",
        )

    source_rows = ledger.get("source_paragraphs")
    if not isinstance(source_rows, list):
        _finding(findings, "source_rows", "source_paragraphs must be a list.")
        source_rows = []
    row_numbers = [row.get("paragraph") for row in source_rows if isinstance(row, dict)]
    if row_numbers != list(range(1, len(source) + 1)):
        _finding(
            findings,
            "source_row_order",
            "source_paragraphs must contain exactly one ordered row per source paragraph.",
        )

    units = ledger.get("semantic_units")
    if not isinstance(units, list):
        _finding(findings, "semantic_units", "semantic_units must be a list.")
        units = []
    unit_ids = [unit.get("unit_ref") for unit in units if isinstance(unit, dict)]
    unit_counts = Counter(unit_ids)
    for unit_ref, count in unit_counts.items():
        if not isinstance(unit_ref, str) or not unit_ref:
            _finding(findings, "unit_ref", "Every semantic unit needs a unit_ref.")
        elif count != 1:
            _finding(
                findings,
                "duplicate_unit_ref",
                f"Unit ref occurs {count} times.",
                unit_ref=unit_ref,
            )
    unit_by_id = {
        unit["unit_ref"]: unit
        for unit in units
        if isinstance(unit, dict)
        and isinstance(unit.get("unit_ref"), str)
        and unit_counts[unit["unit_ref"]] == 1
    }

    for row in source_rows:
        if not isinstance(row, dict):
            _finding(findings, "source_row_type", "Each source row must be an object.")
            continue
        paragraph = row.get("paragraph")
        if not isinstance(paragraph, int) or not 1 <= paragraph <= len(source):
            _finding(findings, "source_row_paragraph", "Invalid source row paragraph.")
            continue
        declared = row.get("unit_refs")
        if not isinstance(declared, list):
            _finding(
                findings,
                "source_row_units",
                "unit_refs must be a list.",
                paragraph=paragraph,
            )
            declared = []
        actual = sorted(
            unit_ref
            for unit_ref, unit in unit_by_id.items()
            if unit.get("source_paragraph") == paragraph
        )
        if sorted(declared) != actual:
            _finding(
                findings,
                "source_row_unit_mismatch",
                "Source row unit_refs do not match semantic_units.",
                paragraph=paragraph,
            )

    for unit in units:
        if not isinstance(unit, dict):
            _finding(findings, "unit_type", "Each semantic unit must be an object.")
            continue
        unit_ref = unit.get("unit_ref")
        paragraph = unit.get("source_paragraph")
        if not isinstance(paragraph, int) or not 1 <= paragraph <= len(source):
            _finding(
                findings,
                "unit_source_paragraph",
                "Invalid source paragraph.",
                unit_ref=unit_ref,
            )
            continue

        source_anchor = unit.get("source_anchor")
        if not isinstance(source_anchor, str) or not source_anchor:
            _finding(
                findings,
                "missing_source_anchor",
                "source_anchor must be nonempty.",
                unit_ref=unit_ref,
            )
        elif source_anchor not in source[paragraph - 1]:
            _finding(
                findings,
                "source_anchor_not_exact",
                "source_anchor is not an exact contiguous source substring.",
                unit_ref=unit_ref,
                paragraph=paragraph,
            )

        if not isinstance(unit.get("truth_status"), str) or not unit["truth_status"]:
            _finding(
                findings,
                "truth_status",
                "truth_status must be nonempty.",
                unit_ref=unit_ref,
            )

        relation = unit.get("relation")
        if not isinstance(relation, dict):
            _finding(findings, "relation", "Missing relation object.", unit_ref=unit_ref)
        else:
            classification = relation.get("classification")
            if classification not in RELATION_CLASSES:
                _finding(
                    findings,
                    "relation_classification",
                    f"Unsupported classification: {classification!r}.",
                    unit_ref=unit_ref,
                )
            canonical = relation.get("canonical_unit_ref")
            if canonical not in unit_by_id:
                _finding(
                    findings,
                    "canonical_unit_ref",
                    f"Unknown canonical unit: {canonical!r}.",
                    unit_ref=unit_ref,
                )
            elif classification == "exact_duplicate" and canonical == unit_ref:
                _finding(
                    findings,
                    "duplicate_canonical_self",
                    "An exact duplicate must point to another canonical unit.",
                    unit_ref=unit_ref,
                )
            elif classification != "exact_duplicate" and canonical != unit_ref:
                _finding(
                    findings,
                    "nonduplicate_canonical_other",
                    "A nonduplicate unit must be its own canonical unit.",
                    unit_ref=unit_ref,
                )

        landing = unit.get("landing")
        if not isinstance(landing, dict):
            _finding(findings, "landing", "Missing landing object.", unit_ref=unit_ref)
            continue
        output_paragraph = landing.get("output_paragraph")
        anchor = landing.get("anchor")
        citation = landing.get("citation")
        if not isinstance(output_paragraph, int) or not 1 <= output_paragraph <= len(prose):
            _finding(
                findings,
                "landing_output_paragraph",
                "Invalid landing output paragraph.",
                unit_ref=unit_ref,
            )
            continue
        if not isinstance(anchor, str) or not anchor:
            _finding(
                findings,
                "missing_landing_anchor",
                "Landing anchor must be nonempty.",
                unit_ref=unit_ref,
            )
        else:
            occurrences = prose_text.count(anchor)
            if occurrences != 1:
                _finding(
                    findings,
                    "landing_anchor_not_unique",
                    f"Landing anchor occurs {occurrences} times.",
                    unit_ref=unit_ref,
                )
            if anchor not in prose[output_paragraph - 1]:
                _finding(
                    findings,
                    "landing_anchor_wrong_paragraph",
                    "Landing anchor is absent from its mapped output paragraph.",
                    unit_ref=unit_ref,
                    paragraph=output_paragraph,
                )
        if not isinstance(citation, str) or not citation:
            _finding(
                findings,
                "missing_landing_citation",
                "Landing citation must be nonempty.",
                unit_ref=unit_ref,
            )
        else:
            if citation not in prose[output_paragraph - 1]:
                _finding(
                    findings,
                    "landing_citation_wrong_paragraph",
                    "Landing citation is absent from its mapped output paragraph.",
                    unit_ref=unit_ref,
                    paragraph=output_paragraph,
                )
            cited = [
                number
                for cited_ayah, numbers in validate_concise.citation_groups(citation)
                if cited_ayah == ayah_ref
                for number in numbers
            ]
            if paragraph not in cited:
                _finding(
                    findings,
                    "landing_citation_omits_source",
                    f"Landing citation omits source paragraph {paragraph}.",
                    unit_ref=unit_ref,
                )

    clusters = ledger.get("synthesis_clusters")
    if not isinstance(clusters, list):
        _finding(findings, "synthesis_clusters", "synthesis_clusters must be a list.")
        clusters = []
    cluster_ids = [
        cluster.get("cluster_ref") for cluster in clusters if isinstance(cluster, dict)
    ]
    cluster_counts = Counter(cluster_ids)
    for cluster_ref, count in cluster_counts.items():
        if not isinstance(cluster_ref, str) or not cluster_ref:
            _finding(findings, "cluster_ref", "Every cluster needs a cluster_ref.")
        elif count != 1:
            _finding(
                findings,
                "duplicate_cluster_ref",
                f"Cluster ref occurs {count} times: {cluster_ref}.",
            )

    clustered_unit_ids: list[str] = []
    clustered_output_paragraphs: list[int] = []
    for cluster in clusters:
        if not isinstance(cluster, dict):
            _finding(findings, "cluster_type", "Each cluster must be an object.")
            continue
        cluster_ref = cluster.get("cluster_ref")
        refs = cluster.get("unit_refs")
        if not isinstance(refs, list):
            _finding(
                findings,
                "cluster_unit_refs",
                "Cluster unit_refs must be a list.",
            )
            refs = []
        clustered_unit_ids.extend(refs)
        unknown = [unit_ref for unit_ref in refs if unit_ref not in unit_by_id]
        if unknown:
            _finding(
                findings,
                "cluster_unknown_units",
                f"Unknown unit refs: {', '.join(unknown)}.",
            )
        expected_source = sorted(
            {
                unit_by_id[unit_ref]["source_paragraph"]
                for unit_ref in refs
                if unit_ref in unit_by_id
            }
        )
        declared_source = cluster.get("source_paragraphs")
        if not isinstance(declared_source, list) or sorted(declared_source) != expected_source:
            _finding(
                findings,
                "cluster_source_paragraphs",
                "Cluster source_paragraphs do not match its units.",
            )
        output_paragraphs = cluster.get("output_paragraphs")
        if not isinstance(output_paragraphs, list) or not output_paragraphs:
            _finding(
                findings,
                "cluster_output_paragraphs",
                "Cluster output_paragraphs must be a nonempty list.",
            )
            output_paragraphs = []
        for output_paragraph in output_paragraphs:
            if not isinstance(output_paragraph, int) or not 1 <= output_paragraph <= len(prose):
                _finding(
                    findings,
                    "cluster_output_paragraph",
                    f"Invalid output paragraph: {output_paragraph!r}.",
                )
            else:
                clustered_output_paragraphs.append(output_paragraph)
        for unit_ref in refs:
            if unit_ref in unit_by_id:
                landing_paragraph = unit_by_id[unit_ref].get("landing", {}).get(
                    "output_paragraph"
                )
                if landing_paragraph not in output_paragraphs:
                    _finding(
                        findings,
                        "cluster_omits_landing_paragraph",
                        f"Cluster omits landing paragraph {landing_paragraph}.",
                        unit_ref=unit_ref,
                    )
        kind = cluster.get("kind")
        if kind not in CLUSTER_KINDS:
            _finding(findings, "cluster_kind", f"Unsupported cluster kind: {kind!r}.")
        elif (kind == "synthesis") != (len(expected_source) > 1):
            _finding(
                findings,
                "cluster_kind_source_mismatch",
                "synthesis requires multiple source paragraphs; standalone requires one.",
            )
        reason = cluster.get("why_together_or_apart_tr")
        if not isinstance(reason, str) or not reason.strip():
            _finding(
                findings,
                "cluster_rationale",
                "Cluster requires a nonempty why_together_or_apart_tr.",
            )

    if Counter(clustered_unit_ids) != Counter(unit_ids):
        _finding(
            findings,
            "cluster_unit_coverage",
            "Clusters must contain every semantic unit exactly once.",
        )
    if Counter(clustered_output_paragraphs) != Counter(range(1, len(prose) + 1)):
        _finding(
            findings,
            "cluster_output_coverage",
            "Clusters must contain every output paragraph exactly once.",
        )

    multi_source = 0
    single_source = 0
    same_position_singleton = 0
    for output_number, paragraph_text in enumerate(prose, start=1):
        for match in QURAN_INTERVAL_RE.finditer(paragraph_text):
            _finding(
                findings,
                "quran_interval_shorthand",
                f"List every ayah explicitly instead of using {match.group(0)!r}.",
                paragraph=output_number,
            )
        cited_refs = {
            number
            for cited_ayah, numbers in validate_concise.citation_groups(paragraph_text)
            if cited_ayah == ayah_ref
            for number in numbers
        }
        if len(cited_refs) > 1:
            multi_source += 1
        elif len(cited_refs) == 1:
            single_source += 1
            if cited_refs == {output_number}:
                same_position_singleton += 1
        paragraph_words = _words(paragraph_text)
        if max_paragraph_words > 0 and paragraph_words > max_paragraph_words:
            _finding(
                findings,
                "overdense_output_paragraph",
                f"Paragraph has {paragraph_words} words; maximum is {max_paragraph_words}.",
                paragraph=output_number,
            )

    expected_metrics: dict[str, int | float] = {
        "source_word_count": _words(source_text),
        "output_word_count": _words(prose_text),
        "retained_word_ratio": _words(prose_text) / _words(source_text)
        if _words(source_text)
        else 0.0,
        "multi_source_output_paragraphs": multi_source,
        "single_source_output_paragraphs": single_source,
        "same_position_singleton_paragraphs": same_position_singleton,
        "output_to_source_paragraph_ratio": len(prose) / len(source) if source else 0.0,
    }
    metrics = ledger.get("metrics")
    if not isinstance(metrics, dict):
        _finding(findings, "metrics", "metrics must be an object.")
        metrics = {}
    for key, expected in expected_metrics.items():
        actual = metrics.get(key)
        if isinstance(expected, float):
            valid = _is_number(actual) and abs(float(actual) - expected) < 1e-9
        else:
            valid = actual == expected
        if not valid:
            _finding(
                findings,
                "metric_mismatch",
                f"{key}: expected {expected!r}, found {actual!r}.",
            )

    audit = ledger.get("audit")
    if not isinstance(audit, dict):
        _finding(findings, "audit", "audit must be an object.")
        audit = {}
    for key in PROBLEM_AUDIT_KEYS:
        if audit.get(key) != []:
            _finding(
                findings,
                "audit_not_clear",
                f"Audit field {key} must be present and empty.",
            )

    return findings


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a legacy V2 middle-layer prose/ledger pair."
    )
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--prose", required=True, type=Path)
    parser.add_argument("--ledger", required=True, type=Path)
    parser.add_argument("--ayah-ref", required=True)
    parser.add_argument("--max-paragraph-words", type=int, default=180)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    missing = [path for path in (args.source, args.prose, args.ledger) if not path.is_file()]
    if missing:
        for path in missing:
            print(f"missing_file: {path}", file=sys.stderr)
        return 1
    try:
        ledger = json.loads(_read(args.ledger))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"invalid_ledger_json: {error}", file=sys.stderr)
        return 1
    if not isinstance(ledger, dict):
        print("invalid_ledger_json: top level must be an object", file=sys.stderr)
        return 1

    findings = validate(
        _read(args.source),
        _read(args.prose),
        ledger,
        ayah_ref=args.ayah_ref,
        max_paragraph_words=args.max_paragraph_words,
    )
    if args.json:
        print(
            json.dumps(
                {
                    "status": "failed" if findings else "ok",
                    "findings": [asdict(finding) for finding in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif findings:
        for finding in findings:
            location = args.ayah_ref
            if finding.paragraph is not None:
                location += f" output ¶{finding.paragraph}"
            if finding.unit_ref is not None:
                location += f" {finding.unit_ref}"
            print(f"{location}: {finding.code}: {finding.message}", file=sys.stderr)
    else:
        print("ok")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
