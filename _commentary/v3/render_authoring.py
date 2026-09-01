#!/usr/bin/env python3
"""Render and advance prose-first v3 authoring handoffs without running agents.

This is deliberately a prompt transport helper, not a prose validator. It
projects the complete candidate docket into isolated lane packets, inlines each
packet into one hermetic prompt, and later composes reconciliation, lane-prose,
canonical merge, editorial, and fresh invitation handoffs from explicit
response files. The main ``workflow.py authoring-advance`` command exposes this
state machine while model execution remains an inspectable path-only trust
boundary.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from v3lib.common import (
    WorkflowError,
    canonical_json_bytes,
    load_json_object_bounded,
    pretty_json_bytes,
)
from v3lib.prepare import validate_docket


V3_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V3_ROOT.parents[1]
PROMPTS_ROOT = V3_ROOT / "prompts"
DEFAULT_INTER_AYAH_DIR = (
    REPO_ROOT.parent
    / "quran-data"
    / "data"
    / "analysis"
    / "inter-ayah"
    / "reciprocal"
)
DEFAULT_INTER_AYAH_PARENT_DIR = DEFAULT_INTER_AYAH_DIR.parent
DEFAULT_QURAN_TEXT = (
    REPO_ROOT.parent / "quran-data" / "data" / "text" / "quran-uthmani.tsv"
)
LANES = ("micro", "macro", "global")
MAX_QURAN_AYAH_COUNT_PER_SURAH = 286
HFT_RECORD_FIELDS = (
    ("baseline_models", "baseline_model", "model_id"),
    ("context_deltas", "context_delta", "model_id"),
    ("surprising_valid_outliers", "surprising_outlier", "outlier_id"),
)
INTER_AYAH_LABELS = {
    "strong",
    "medium",
    "weak",
    "no value",
    "contrast",
    "reject",
}
MEANINGFUL_INTER_AYAH_LABELS = INTER_AYAH_LABELS - {"no value", "reject"}
INTER_AYAH_FILE_RE = re.compile(
    r"focus_([1-9][0-9]*)_([1-9][0-9]*)_cutoff_100\.tsv"
)
INTER_AYAH_SINGLE_REF_RE = re.compile(r"[1-9][0-9]*:[1-9][0-9]*")
INTER_AYAH_RANGE_REF_RE = re.compile(
    r"([1-9][0-9]*):([1-9][0-9]*)-([1-9][0-9]*)"
)
INTER_AYAH_RECORD_TYPES = {
    "directional_review",
    "reciprocal_nomination",
    "reciprocal_counterevidence",
    "self_reiteration",
}
INTER_AYAH_COLUMNS = (
    "record_type",
    "focus_ref",
    "target_ref",
    "focus_direction_label",
    "source_direction_label",
    "source_focus_ref",
    "source_target_ref",
    "source_target_component_ref",
    "relation_scope",
    "source_column_order",
    "source_row_role",
    "source_note",
    "source_file",
    "source_line",
    "source_row_sha256",
)
RECOVERABLE_TRANSPORT_PROVENANCE_KEYS = frozenset(
    {
        "json_pointer",
        "projection_pointer",
        "projection_pointers",
        "projection_record_sha256",
        "source_column_order",
        "source_file",
        "source_line",
        "source_pointer",
        "source_pointers",
        "source_row_sha256",
    }
)
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
AUTHORING_INPUTS_ROOT = (V3_ROOT / "inputs" / "authoring").resolve()
AUTHORING_OUTPUTS_ROOT = (V3_ROOT / "outputs" / "authoring").resolve()
MAX_AUTHORING_JSON_BYTES = 128_000_000
MAX_RECONCILIATION_ATTEMPTS = 16
MAX_SCOPE_PROSE_REPAIR_ATTEMPTS = 8
MAX_SCOPE_PROSE_REWRITE_ATTEMPTS = 4
# Locked finding refs are provenance tokens embedded in Markdown ledgers.  The
# alphabet is Unicode-aware; separators make refs readable while remaining
# unambiguous beside ordinary prose punctuation.  Reconciliation loading and
# canonical accounting share the exact same parser, so an accepted ref can
# never become uncountable later.
LOCKED_REF_PREFIX = "locked:"
LOCKED_REF_SEPARATORS = frozenset("_.:-/")
LOCKED_REF_SENTENCE_ENDINGS = frozenset(".:")
RECONCILIATION_SEMANTIC_FIELDS = (
    "title",
    "claim",
    "mechanism",
    "reader_payoff",
    "containment",
    "epistemic_status",
)
ATX_HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
SURPRISE_INDEX_ROW_RE = re.compile(
    r"^[ \t]*-[ \t]+(surprise:[a-z0-9][a-z0-9_.:-]*)(?:[ \t]|$)"
)
READER_CORE_REASONS = (
    "plain_reading",
    "architectural_move",
    "surprise_carrier",
    "surprise_payoff",
    "continuity",
    "closure",
)
READER_DETAIL_KINDS = (
    "language_and_structure",
    "nearby_context",
    "wider_connections",
    "exploratory_reading",
)
READER_LABEL_FORBIDDEN_RE = re.compile(
    r"\b(?:micro|macro|global|scope|workflow|candidate|finding|branch|support|"
    r"hft|qac)\b|locked:|surprise:|root_[0-9]+/b[0-9]+",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class AuthoringLayout:
    """Canonical, repository-tracked paths for one ayah's authoring run."""

    ayah_ref: str
    folder: str
    stem: str
    inputs: Path
    outputs: Path

    @property
    def workspace(self) -> Path:
        return REPO_ROOT


def _authoring_layout(ayah_ref: str) -> AuthoringLayout:
    _surah, _ayah, folder, stem = _ayah_parts(ayah_ref)
    inputs = (AUTHORING_INPUTS_ROOT / folder / stem).resolve(strict=False)
    outputs = (AUTHORING_OUTPUTS_ROOT / folder / stem).resolve(strict=False)
    try:
        inputs.relative_to(AUTHORING_INPUTS_ROOT)
        outputs.relative_to(AUTHORING_OUTPUTS_ROOT)
    except ValueError as exc:  # pragma: no cover - guarded by _ayah_parts
        raise SystemExit("Derived authoring path escaped its canonical root") from exc
    return AuthoringLayout(
        ayah_ref=ayah_ref,
        folder=folder,
        stem=stem,
        inputs=inputs,
        outputs=outputs,
    )


def _load_object(path: Path) -> dict[str, Any]:
    value, _raw = load_json_object_bounded(
        path, max_bytes=MAX_AUTHORING_JSON_BYTES
    )
    return value


def _canonical_json(value: Any) -> str:
    return canonical_json_bytes(value).decode("utf-8")


def _strip_recoverable_transport_provenance(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_recoverable_transport_provenance(item)
            for key, item in value.items()
            if key not in RECOVERABLE_TRANSPORT_PROVENANCE_KEYS
        }
    if isinstance(value, list):
        return [_strip_recoverable_transport_provenance(item) for item in value]
    return value


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(_canonical_json(value).encode("utf-8"))


def _pretty_json(value: Any) -> str:
    return pretty_json_bytes(value).decode("utf-8")


def _ayah_parts(ayah_ref: str) -> tuple[int, int, str, str]:
    match = re.fullmatch(r"([1-9][0-9]*):([1-9][0-9]*)", ayah_ref)
    if not match:
        raise SystemExit(f"Invalid ayah reference: {ayah_ref!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    return surah, ayah, f"s{surah:03d}", f"{surah}_{ayah}"


def _default_docket(ayah_ref: str) -> Path:
    _surah, _ayah, folder, stem = _ayah_parts(ayah_ref)
    return V3_ROOT / "inputs" / "adjudication" / folder / f"{stem}.docket.json"


def _default_source_bundle(ayah_ref: str) -> Path:
    _surah, _ayah, folder, stem = _ayah_parts(ayah_ref)
    return V3_ROOT / "inputs" / "source" / folder / f"{stem}.bundle.json"


def _stable_source_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT.parent))
    except ValueError:
        return path.name


def _quran_text_evidence(
    source_path: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    try:
        source_path = source_path.resolve(strict=True)
        lines = source_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise SystemExit(f"Cannot read Quran text source {source_path}: {exc}") from exc
    if not source_path.is_file():
        raise SystemExit(f"Quran text source is not a file: {source_path}")

    stable_path = _stable_source_path(source_path)
    evidence: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(lines, 1):
        if not line:
            continue
        parts = line.split("|", 1)
        if len(parts) != 2:
            raise SystemExit(
                f"Malformed Quran text row at {source_path}:{line_number}"
            )
        ayah_ref, arabic = parts[0].strip(), parts[1].lstrip("\ufeff").strip()
        if not re.fullmatch(
            r"[1-9][0-9]*:(?:0|[1-9][0-9]*)", ayah_ref
        ) or not arabic:
            raise SystemExit(
                f"Malformed Quran text identity at {source_path}:{line_number}"
            )
        if ayah_ref in evidence:
            raise SystemExit(f"Duplicate Quran text ayah reference: {ayah_ref}")
        row = {
            "ayah_ref": ayah_ref,
            "arabic_uthmani": arabic,
            "source_pointer": f"{stable_path}#L{line_number}",
        }
        row["source_row_sha256"] = _sha256_json(row)
        evidence[ayah_ref] = row
    if not evidence:
        raise SystemExit(f"Quran text source is empty: {source_path}")
    return evidence, {
        "source_id": "quran-data/quran-uthmani",
        "source_path": stable_path,
        "source_sha256": _sha256_bytes(source_path.read_bytes()),
        "ayah_count": len(evidence),
    }


def _source_target_components(source_target_ref: str) -> tuple[str, ...]:
    if INTER_AYAH_SINGLE_REF_RE.fullmatch(source_target_ref):
        return (source_target_ref,)
    match = INTER_AYAH_RANGE_REF_RE.fullmatch(source_target_ref)
    if match is None:
        return ()
    source_surah, first, last = map(int, match.groups())
    if (
        first > last
        or last - first + 1 > MAX_QURAN_AYAH_COUNT_PER_SURAH
    ):
        return ()
    return tuple(f"{source_surah}:{ayah}" for ayah in range(first, last + 1))


def _inter_ayah_projection(
    focus_ref: str,
    source_dir: Path,
    directional_source_dir: Path,
) -> tuple[
    list[dict[str, Any]],
    dict[str, list[dict[str, Any]]],
    dict[str, Any],
]:
    try:
        source_dir = source_dir.resolve(strict=True)
    except OSError as exc:
        raise SystemExit(
            f"Cannot resolve inter-ayah projection directory {source_dir}: {exc}"
        ) from exc
    if not source_dir.is_dir():
        raise SystemExit(f"Inter-ayah projection is not a directory: {source_dir}")
    directional_source_dir = Path(os.path.abspath(directional_source_dir))
    directional_source_available = directional_source_dir.is_dir()
    pointer_warnings = (
        []
        if directional_source_available
        else [
            "The manifest-bound projection is complete, but its configured "
            "directional parent is unavailable for source-pointer "
            f"dereferencing: {directional_source_dir}"
        ]
    )

    surah, ayah, _folder, _stem = _ayah_parts(focus_ref)
    path = source_dir / f"focus_{surah}_{ayah}_cutoff_100.tsv"
    try:
        payload = path.read_bytes()
        lines = payload.decode("utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit(f"Cannot read inter-ayah projection {path}: {exc}") from exc
    if not lines or tuple(lines[0].split("\t")) != INTER_AYAH_COLUMNS:
        raise SystemExit(f"Unexpected inter-ayah projection header at {path}:1")

    manifest_path = source_dir / "MANIFEST.json"
    if not manifest_path.is_file():
        raise SystemExit(f"Inter-ayah projection manifest is missing: {manifest_path}")
    manifest = _load_object(manifest_path)
    manifest_sha256 = _sha256_bytes(manifest_path.read_bytes())
    manifest_columns = manifest.get("columns")
    documents = manifest.get("documents")
    document_record = (
        documents.get(path.name) if isinstance(documents, dict) else None
    )
    if (
        manifest.get("schema_version")
        != "inter-ayah-reciprocal-manifest-v2"
        or manifest.get("corpus_id") != "inter-ayah-row-reciprocal-v2"
        or manifest.get("record_schema")
        != "inter-ayah-row-reciprocal-tsv-v2"
        or not isinstance(manifest_columns, list)
        or tuple(manifest_columns) != INTER_AYAH_COLUMNS
        or not isinstance(document_record, dict)
    ):
        raise SystemExit(
            f"Inter-ayah projection manifest does not describe {path.name}"
        )
    document_sha256 = _sha256_bytes(payload)
    if (
        document_record.get("sha256") != document_sha256
        or document_record.get("record_count") != len(lines) - 1
    ):
        raise SystemExit(
            f"Inter-ayah projection document does not match its manifest: {path}"
        )

    stable_projection_path = _stable_source_path(path)
    directional_rows: list[dict[str, Any]] = []
    reciprocal_by_target: dict[str, list[dict[str, Any]]] = {}
    self_reiterations: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines[1:], 2):
        fields = line.split("\t")
        if len(fields) != len(INTER_AYAH_COLUMNS):
            raise SystemExit(
                f"Expected {len(INTER_AYAH_COLUMNS)} inter-ayah fields at "
                f"{path}:{line_number}; found {len(fields)}"
            )
        raw = dict(zip(INTER_AYAH_COLUMNS, fields))
        record_type = raw["record_type"]
        target_ref = raw["target_ref"]
        source_label = raw["source_direction_label"]
        component_ref = raw["source_target_component_ref"]
        source_file = raw["source_file"]
        source_line = raw["source_line"]
        source_file_match = INTER_AYAH_FILE_RE.fullmatch(source_file)
        if (
            record_type not in INTER_AYAH_RECORD_TYPES
            or raw["focus_ref"] != focus_ref
            or INTER_AYAH_SINGLE_REF_RE.fullmatch(target_ref) is None
            or source_label not in INTER_AYAH_LABELS
            or INTER_AYAH_SINGLE_REF_RE.fullmatch(component_ref) is None
            or source_file_match is None
            or not source_line.isdigit()
            or int(source_line) < 1
            or re.fullmatch(r"[0-9a-f]{64}", raw["source_row_sha256"]) is None
            or raw["source_column_order"]
            not in {"label_target_note", "target_label_note"}
        ):
            raise SystemExit(f"Malformed inter-ayah projection at {path}:{line_number}")
        source_focus_ref = (
            f"{int(source_file_match.group(1))}:"
            f"{int(source_file_match.group(2))}"
        )
        expected_source_row_role = (
            "ranked_review"
            if int(source_line) <= 100
            else "missing_ayah_suggestion"
        )
        if raw["source_row_role"] != expected_source_row_role:
            raise SystemExit(
                f"Broken inter-ayah source row role at {path}:{line_number}"
            )
        source_target_components = _source_target_components(
            raw["source_target_ref"]
        )
        source_target_is_range = (
            INTER_AYAH_RANGE_REF_RE.fullmatch(raw["source_target_ref"])
            is not None
        )
        if (
            raw["source_focus_ref"] != source_focus_ref
            or component_ref not in source_target_components
        ):
            raise SystemExit(
                f"Broken inter-ayah source provenance at {path}:{line_number}"
            )
        expected_scope = (
            "same_surah"
            if source_focus_ref.split(":", 1)[0]
            == component_ref.split(":", 1)[0]
            else "cross_surah"
        )
        if raw["relation_scope"] != expected_scope:
            raise SystemExit(f"Broken inter-ayah scope at {path}:{line_number}")

        expected_type = (
            "self_reiteration"
            if source_focus_ref == component_ref
            else (
                "reciprocal_nomination"
                if source_label in MEANINGFUL_INTER_AYAH_LABELS
                else "reciprocal_counterevidence"
            )
        )
        if record_type == "directional_review":
            if (
                source_focus_ref != focus_ref
                or target_ref != component_ref
                or raw["focus_direction_label"] != source_label
            ):
                raise SystemExit(
                    f"Broken directional projection at {path}:{line_number}"
                )
        elif (
            record_type != expected_type
            or component_ref != focus_ref
            or target_ref != source_focus_ref
            or raw["focus_direction_label"]
        ):
            raise SystemExit(
                f"Broken reciprocal projection at {path}:{line_number}"
            )

        source_pointer = (
            f"{_stable_source_path(directional_source_dir / source_file)}"
            f"#L{source_line}"
        )
        projection_record_sha256 = _sha256_json(raw)
        common = {
            "record_type": record_type,
            "source_direction_label": source_label,
            "source_focus_ref": source_focus_ref,
            "source_target_ref": raw["source_target_ref"],
            "source_target_component_ref": component_ref,
            "source_target_is_range": source_target_is_range,
            "source_target_components": list(source_target_components),
            "source_target_range_boundary": (
                "The source note was authored for the complete target range. "
                "This record exposes one component for discovery; assign only "
                "features actually present in that component to it, and keep "
                "sequence-level material at range scope."
                if source_target_is_range
                else None
            ),
            "source_note": raw["source_note"],
            "source_column_order": raw["source_column_order"],
            "source_row_role": raw["source_row_role"],
            "source_file": source_file,
            "source_line": int(source_line),
            "source_pointer": source_pointer,
            "projection_pointer": f"{stable_projection_path}#L{line_number}",
            "source_row_sha256": raw["source_row_sha256"],
            "projection_record_sha256": projection_record_sha256,
            "relation_scope": raw["relation_scope"],
        }
        if record_type == "directional_review":
            directional_rows.append(
                {
                    "ref": target_ref,
                    "label": raw["focus_direction_label"],
                    "note": raw["source_note"],
                    **common,
                }
            )
        elif record_type == "self_reiteration":
            self_reiterations.append(
                {
                    "receiving_direction_label": None,
                    **common,
                }
            )
        else:
            reciprocal_by_target.setdefault(target_ref, []).append(
                {
                    "receiving_direction_label": None,
                    **common,
                }
            )

    focus_surah = focus_ref.split(":", 1)[0]
    reciprocal_rows = [
        row for rows in reciprocal_by_target.values() for row in rows
    ]
    if (
        document_record.get("directional_review_record_count")
        != len(directional_rows)
        or document_record.get("mirrored_record_count")
        != len(reciprocal_rows) + len(self_reiterations)
    ):
        raise SystemExit(
            f"Inter-ayah projection record types do not match its manifest: {path}"
        )
    ordered_reciprocal = dict(
        sorted(
            reciprocal_by_target.items(),
            key=lambda item: _ayah_parts(item[0])[:2],
        )
    )
    return directional_rows, ordered_reciprocal, {
        "source_id": "quran-data/inter-ayah-row-reciprocal-v2",
        "source_directory": _stable_source_path(source_dir),
        "directional_source_directory": _stable_source_path(
            directional_source_dir
        ),
        "source_document": stable_projection_path,
        "source_document_sha256": document_sha256,
        "manifest_available": True,
        "manifest_sha256": manifest_sha256,
        "manifest_document_record": document_record,
        "operational_fallback_used": False,
        "integrity_warnings": pointer_warnings,
        "directional_source_available_for_pointer_dereference": (
            directional_source_available
        ),
        "parent_directional_source_is_not_concatenated": True,
        "directional_review_row_count": len(directional_rows),
        "reciprocal_nomination_row_count": sum(
            row["record_type"] == "reciprocal_nomination"
            for row in reciprocal_rows
        ),
        "reciprocal_counterevidence_row_count": sum(
            row["record_type"] == "reciprocal_counterevidence"
            for row in reciprocal_rows
        ),
        "self_reiteration_row_count": len(self_reiterations),
        "self_reiterations_are_not_reciprocal_evidence": True,
        "incoming_origin_count": len(reciprocal_by_target),
        "incoming_cross_surah_origin_count": sum(
            target_ref.split(":", 1)[0] != focus_surah
            for target_ref in reciprocal_by_target
        ),
        "incoming_same_surah_origin_count": sum(
            target_ref.split(":", 1)[0] == focus_surah
            for target_ref in reciprocal_by_target
        ),
    }


def _fallback_projection_common(
    source: dict[str, Any],
    *,
    record_type: str,
    projected_focus_ref: str,
    projected_target_ref: str,
    focus_direction_label: str,
) -> dict[str, Any]:
    record = {
        "record_type": record_type,
        "focus_ref": projected_focus_ref,
        "target_ref": projected_target_ref,
        "focus_direction_label": focus_direction_label,
        "source_direction_label": source["label"],
        "source_focus_ref": source["origin_ref"],
        "source_target_ref": source["source_target_ref"],
        "source_target_component_ref": source["component_ref"],
        "relation_scope": source["relation_scope"],
        "source_column_order": source["source_column_order"],
        "source_row_role": source["source_row_role"],
        "source_note": source["note"],
        "source_file": source["source_file"],
        "source_line": str(source["source_line"]),
        "source_row_sha256": source["source_row_sha256"],
    }
    return {
        "record_type": record_type,
        "source_direction_label": source["label"],
        "source_focus_ref": source["origin_ref"],
        "source_target_ref": source["source_target_ref"],
        "source_target_component_ref": source["component_ref"],
        "source_target_is_range": source["source_target_is_range"],
        "source_target_components": list(source["component_refs"]),
        "source_target_range_boundary": (
            "The source note was authored for the complete target range. This "
            "record exposes one component for discovery; assign only features "
            "actually present in that component to it, and keep sequence-level "
            "material at range scope."
            if source["source_target_is_range"]
            else None
        ),
        "source_note": source["note"],
        "source_column_order": source["source_column_order"],
        "source_row_role": source["source_row_role"],
        "source_file": source["source_file"],
        "source_line": source["source_line"],
        "source_pointer": source["source_pointer"],
        "projection_pointer": (
            f"reconstructed:{source['stable_path']}:L{source['source_line']}:"
            f"{record_type}:{source['component_ref']}"
        ),
        "source_row_sha256": source["source_row_sha256"],
        "projection_record_sha256": _sha256_json(record),
        "relation_scope": source["relation_scope"],
    }


def _inter_ayah_parent_fallback(
    focus_ref: str,
    parent_dir: Path,
    numbered_refs: set[str],
    projection_failure: str,
) -> tuple[
    list[dict[str, Any]],
    dict[str, list[dict[str, Any]]],
    dict[str, Any],
]:
    configured_parent_dir = parent_dir
    parent_dir_is_symlink = configured_parent_dir.is_symlink()
    try:
        parent_dir = parent_dir.resolve(strict=True)
    except OSError as exc:
        raise SystemExit(
            f"Cannot resolve directional inter-ayah fallback {parent_dir}: {exc}"
        ) from exc
    if not parent_dir.is_dir():
        raise SystemExit(
            f"Directional inter-ayah fallback is not a directory: {parent_dir}"
        )
    if focus_ref not in numbered_refs:
        raise SystemExit(f"Fallback focus is not a numbered ayah: {focus_ref}")

    paths = sorted(parent_dir.glob("focus_*_cutoff_100.tsv"))
    non_file_names = [path.name for path in paths if not path.is_file()]
    if non_file_names:
        raise SystemExit(
            "Directional fallback entries must be readable files: "
            + ", ".join(non_file_names[:20])
        )
    symlink_names = [path.name for path in paths if path.is_symlink()]
    invalid_names = [
        path.name
        for path in paths
        if INTER_AYAH_FILE_RE.fullmatch(path.name) is None
    ]
    if invalid_names:
        raise SystemExit(
            "Malformed directional inter-ayah filenames: "
            + ", ".join(invalid_names[:20])
        )
    expected_names = {
        f"focus_{_ayah_parts(ref)[0]}_{_ayah_parts(ref)[1]}_cutoff_100.tsv"
        for ref in numbered_refs
    }
    actual_names = {path.name for path in paths}
    if actual_names != expected_names:
        raise SystemExit(
            "Directional inter-ayah fallback is incomplete; "
            f"missing={sorted(expected_names - actual_names)[:20]}, "
            f"extra={sorted(actual_names - expected_names)[:20]}"
        )

    directional_rows: list[dict[str, Any]] = []
    reciprocal_by_target: dict[str, list[dict[str, Any]]] = {}
    source_digest = hashlib.sha256()
    source_row_count = 0
    source_component_count = 0
    ranked_review_count = 0
    suggestion_count = 0
    nomination_count = 0
    counterevidence_count = 0
    self_reiteration_count = 0
    focus_source_sha256: str | None = None
    focus_source_path: str | None = None

    for path in paths:
        match = INTER_AYAH_FILE_RE.fullmatch(path.name)
        if match is None:
            raise SystemExit(f"Malformed directional inter-ayah file: {path}")
        origin_ref = f"{int(match.group(1))}:{int(match.group(2))}"
        try:
            payload = path.read_bytes()
            lines = payload.decode("utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            raise SystemExit(
                f"Cannot read directional inter-ayah fallback {path}: {exc}"
            ) from exc
        name_bytes = path.name.encode("utf-8")
        source_digest.update(len(name_bytes).to_bytes(4, "big"))
        source_digest.update(name_bytes)
        source_digest.update(len(payload).to_bytes(8, "big"))
        source_digest.update(payload)
        stable_path = _stable_source_path(path)
        if origin_ref == focus_ref:
            focus_source_sha256 = _sha256_bytes(payload)
            focus_source_path = stable_path

        for source_line, line in enumerate(lines, 1):
            fields = line.split("\t")
            if len(fields) != 3:
                raise SystemExit(
                    f"Expected three fallback TSV fields at {path}:{source_line}; "
                    f"found {len(fields)}"
                )
            first_raw, second_raw, note = fields
            first, second = first_raw.strip(), second_raw.strip()
            if first in INTER_AYAH_LABELS:
                label, source_target_ref = first, second
                source_column_order = "label_target_note"
            elif second in INTER_AYAH_LABELS:
                source_target_ref, label = first, second
                source_column_order = "target_label_note"
            else:
                raise SystemExit(
                    f"Cannot identify fallback label at {path}:{source_line}"
                )
            component_refs = _source_target_components(source_target_ref)
            if not component_refs or any(
                ref not in numbered_refs for ref in component_refs
            ):
                raise SystemExit(
                    f"Invalid fallback target at {path}:{source_line}: "
                    f"{source_target_ref}"
                )
            source_target_is_range = (
                INTER_AYAH_RANGE_REF_RE.fullmatch(source_target_ref) is not None
            )
            source_row_role = (
                "ranked_review"
                if source_line <= 100
                else "missing_ayah_suggestion"
            )
            source_row_count += 1
            ranked_review_count += int(source_row_role == "ranked_review")
            suggestion_count += int(
                source_row_role == "missing_ayah_suggestion"
            )
            source_row_sha256 = _sha256_bytes(line.encode("utf-8"))
            source_pointer = f"{stable_path}#L{source_line}"

            for component_ref in component_refs:
                source_component_count += 1
                relation_scope = (
                    "same_surah"
                    if origin_ref.split(":", 1)[0]
                    == component_ref.split(":", 1)[0]
                    else "cross_surah"
                )
                if origin_ref != focus_ref and component_ref != focus_ref:
                    continue
                source = {
                    "label": label,
                    "origin_ref": origin_ref,
                    "source_target_ref": source_target_ref,
                    "component_ref": component_ref,
                    "component_refs": component_refs,
                    "source_target_is_range": source_target_is_range,
                    "relation_scope": relation_scope,
                    "source_column_order": source_column_order,
                    "source_row_role": source_row_role,
                    "note": note,
                    "source_file": path.name,
                    "source_line": source_line,
                    "source_row_sha256": source_row_sha256,
                    "source_pointer": source_pointer,
                    "stable_path": stable_path,
                }

                if origin_ref == focus_ref:
                    common = _fallback_projection_common(
                        source,
                        record_type="directional_review",
                        projected_focus_ref=origin_ref,
                        projected_target_ref=component_ref,
                        focus_direction_label=label,
                    )
                    directional_rows.append(
                        {
                            "ref": component_ref,
                            "label": label,
                            "note": note,
                            **common,
                        }
                    )
                if component_ref != focus_ref:
                    continue
                if origin_ref == component_ref:
                    self_reiteration_count += 1
                    continue
                record_type = (
                    "reciprocal_nomination"
                    if label in MEANINGFUL_INTER_AYAH_LABELS
                    else "reciprocal_counterevidence"
                )
                nomination_count += int(
                    record_type == "reciprocal_nomination"
                )
                counterevidence_count += int(
                    record_type == "reciprocal_counterevidence"
                )
                common = _fallback_projection_common(
                    source,
                    record_type=record_type,
                    projected_focus_ref=component_ref,
                    projected_target_ref=origin_ref,
                    focus_direction_label="",
                )
                reciprocal_by_target.setdefault(origin_ref, []).append(
                    {
                        "receiving_direction_label": None,
                        **common,
                    }
                )

    if focus_source_sha256 is None or focus_source_path is None:
        raise SystemExit(
            f"Directional fallback did not encounter focus document {focus_ref}"
        )
    ordered_reciprocal = dict(
        sorted(
            reciprocal_by_target.items(),
            key=lambda item: _ayah_parts(item[0])[:2],
        )
    )
    focus_surah = focus_ref.split(":", 1)[0]
    projection_warning = (
        "Typed reciprocal projection failed integrity validation and was not "
        f"used: {projection_failure}. Reconstructed a complete replacement "
        "view from the parent directional corpus."
    )
    integrity_warnings = [projection_warning]
    if parent_dir_is_symlink or symlink_names:
        integrity_warnings.append(
            "The read-only fallback followed symlinked source material; "
            f"parent_symlink={parent_dir_is_symlink}, "
            f"symlinked_document_count={len(symlink_names)}. Exact consumed "
            "bytes are bound by source_corpus_sha256."
        )
    return directional_rows, ordered_reciprocal, {
        "source_id": "quran-data/inter-ayah-parent-lossless-fallback-v2",
        "source_directory": _stable_source_path(parent_dir),
        "directional_source_directory": _stable_source_path(parent_dir),
        "directional_source_available_for_pointer_dereference": True,
        "source_document": focus_source_path,
        "source_document_sha256": focus_source_sha256,
        "source_corpus_sha256": source_digest.hexdigest(),
        "manifest_available": False,
        "manifest_sha256": None,
        "manifest_document_record": None,
        "operational_fallback_used": True,
        "integrity_warnings": integrity_warnings,
        "reconstruction_complete": True,
        "scanned_document_count": len(paths),
        "scanned_source_row_count": source_row_count,
        "scanned_source_target_component_count": source_component_count,
        "ranked_review_source_row_count": ranked_review_count,
        "missing_ayah_suggestion_source_row_count": suggestion_count,
        "parent_directional_source_is_not_concatenated": True,
        "directional_review_row_count": len(directional_rows),
        "reciprocal_nomination_row_count": nomination_count,
        "reciprocal_counterevidence_row_count": counterevidence_count,
        "self_reiteration_row_count": self_reiteration_count,
        "self_reiterations_are_not_reciprocal_evidence": True,
        "incoming_origin_count": len(reciprocal_by_target),
        "incoming_cross_surah_origin_count": sum(
            target_ref.split(":", 1)[0] != focus_surah
            for target_ref in reciprocal_by_target
        ),
        "incoming_same_surah_origin_count": sum(
            target_ref.split(":", 1)[0] == focus_surah
            for target_ref in reciprocal_by_target
        ),
    }


def _inter_ayah_evidence_with_fallback(
    focus_ref: str,
    projection_dir: Path,
    parent_dir: Path,
    numbered_refs: set[str],
) -> tuple[
    list[dict[str, Any]],
    dict[str, list[dict[str, Any]]],
    dict[str, Any],
]:
    try:
        return _inter_ayah_projection(
            focus_ref,
            projection_dir,
            parent_dir,
        )
    except SystemExit as projection_error:
        try:
            return _inter_ayah_parent_fallback(
                focus_ref,
                parent_dir,
                numbered_refs,
                str(projection_error),
            )
        except SystemExit as fallback_error:
            raise SystemExit(
                "All inter-ayah evidence routes failed. "
                f"Typed projection failure: {projection_error}. "
                f"Lossless parent reconstruction failure: {fallback_error}"
            ) from fallback_error


def _read_prompt(name: str) -> str:
    path = PROMPTS_ROOT / name
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Cannot read prompt template {path}: {exc}") from exc


def _render(template: str, replacements: dict[str, str], *, label: str) -> str:
    template_markers = set(MARKER_RE.findall(template))
    replacement_markers = set(replacements)
    if template_markers != replacement_markers:
        raise SystemExit(
            f"{label} marker contract disagrees; "
            f"missing={sorted(template_markers - replacement_markers)}, "
            f"extra={sorted(replacement_markers - template_markers)}"
        )
    rendered = template
    for marker, replacement in replacements.items():
        rendered = rendered.replace(marker, replacement)
    return rendered


def _repo_relative_path(path: Path) -> str:
    """Return a checkout-stable path for persisted prompt metadata."""

    resolved = path.resolve(strict=False)
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        try:
            return str(resolved.relative_to(REPO_ROOT.parent))
        except ValueError:
            return str(resolved)


def _manifest_path(path: Path) -> str:
    resolved = path.resolve(strict=False)
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError as exc:
        raise SystemExit(
            f"Authoring artifact is outside the repository: {path}"
        ) from exc


def _absolute_manifest_path(value: Any, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise SystemExit(f"Missing {label} path in prompt manifest")
    path = Path(value)
    if path.is_absolute():
        raise SystemExit(f"Persisted {label} path must be repository-relative")
    resolved = (REPO_ROOT / path).resolve(strict=False)
    try:
        resolved.relative_to(V3_ROOT)
    except ValueError as exc:
        raise SystemExit(f"Persisted {label} path escapes commentary v3") from exc
    return resolved


def _assert_under(path: Path, root: Path, *, label: str) -> Path:
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise SystemExit(f"{label} escapes its canonical authoring root: {path}") from exc
    return resolved


def _assert_input_path(layout: AuthoringLayout, path: Path, *, label: str) -> Path:
    return _assert_under(path, layout.inputs, label=label)


def _assert_output_path(layout: AuthoringLayout, path: Path, *, label: str) -> Path:
    return _assert_under(path, layout.outputs, label=label)


def _prepare_output_parent(
    layout: AuthoringLayout, path: Path, *, label: str
) -> None:
    """Create one declared canonical output parent without following escapes."""

    _assert_output_path(layout, path, label=label)
    if path.is_symlink():
        raise SystemExit(f"{label} must not be a symlink: {path}")
    if path.exists() and not path.is_file():
        raise SystemExit(f"{label} is not a regular file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    _assert_under(path.parent, layout.outputs, label=f"{label} parent")


def _write(run_dir: Path, path: Path, text: str) -> None:
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing write outside run directory: {path}") from exc
    if path.is_symlink():
        raise SystemExit(f"Refusing to replace symlink: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        path.parent.resolve().relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing write through escaped parent: {path}") from exc
    if path.exists():
        if not path.is_file():
            raise SystemExit(f"Refusing to replace non-file: {path}")
        if path.read_text(encoding="utf-8") == text:
            return
        raise SystemExit(f"Refusing to replace changed generated file: {path}")
    path.write_text(text, encoding="utf-8")


def _ensure_directory(run_dir: Path, path: Path) -> None:
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing directory outside run directory: {path}") from exc
    if path.is_symlink():
        raise SystemExit(f"Refusing symlink directory: {path}")
    if path.exists() and not path.is_dir():
        raise SystemExit(f"Refusing non-directory path: {path}")
    path.mkdir(parents=True, exist_ok=True)
    try:
        path.resolve().relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing escaped directory: {path}") from exc


def _payload_hash_with_identity_field_removed(
    value: dict[str, Any], field: str
) -> str:
    payload = json.loads(_canonical_json(value))
    payload.get("identity", {}).pop(field, None)
    return _sha256_json(payload)


def _request_sha256(stage: str, inputs: dict[str, str]) -> str:
    return _sha256_json({"stage": stage, "inputs": inputs})


def _scope_review_paths(
    layout: AuthoringLayout, lane: str, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "scope" / lane / "review" / request_sha256
    output_dir = layout.outputs / "scope" / lane / "review" / request_sha256
    return {
        "packet": input_dir / "packet.json",
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "review.json",
    }


def _scope_repair_paths(
    layout: AuthoringLayout, lane: str, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "scope" / lane / "repair" / request_sha256
    output_dir = layout.outputs / "scope" / lane / "repair" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "review.json",
    }


def _reconcile_paths(
    layout: AuthoringLayout, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "reconcile" / request_sha256
    output_dir = layout.outputs / "reconcile" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "reconciled.json",
    }


def _scope_prose_paths(
    layout: AuthoringLayout, lane: str, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "scope" / lane / "prose" / request_sha256
    output_dir = layout.outputs / "scope" / lane / "prose" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "draft.json",
    }


def _scope_prose_repair_paths(
    layout: AuthoringLayout, lane: str, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "scope" / lane / "prose-repair" / request_sha256
    output_dir = layout.outputs / "scope" / lane / "prose-repair" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "draft.json",
    }


def _scope_prose_rewrite_paths(
    layout: AuthoringLayout, lane: str, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "scope" / lane / "prose-rewrite" / request_sha256
    output_dir = layout.outputs / "scope" / lane / "prose-rewrite" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "draft.json",
    }


def _merge_paths(
    layout: AuthoringLayout, request_sha256: str
) -> dict[str, Any]:
    input_dir = layout.inputs / "merge" / request_sha256
    output_dir = layout.outputs / "merge" / request_sha256
    outputs = {
        "prose": output_dir / f"{layout.stem}.prose.tr.md",
        "evidence": output_dir / f"{layout.stem}.evidence.tr.md",
        "index": output_dir / f"{layout.stem}.index.tr.md",
        "friction": output_dir / f"{layout.stem}.friction.tr.md",
    }
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "outputs": outputs,
        "receipt": output_dir / "turn-receipt.json",
    }


def _editorial_paths(
    layout: AuthoringLayout,
    request_sha256: str,
    first_pass_outputs: dict[str, Path],
) -> dict[str, Any]:
    input_dir = layout.inputs / "editorial" / request_sha256
    outputs = {
        key: _editorial_output_path(path) for key, path in first_pass_outputs.items()
    }
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "outputs": outputs,
        "receipt": (
            layout.outputs / "editorial" / request_sha256 / "turn-receipt.json"
        ),
    }


def _invitation_paths(
    layout: AuthoringLayout, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "invitation" / request_sha256
    output_dir = layout.outputs / "invitation" / request_sha256
    return {
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / f"{layout.stem}.invitation.tr.md",
    }


def _reader_map_paths(
    layout: AuthoringLayout, request_sha256: str
) -> dict[str, Path]:
    input_dir = layout.inputs / "reader-map" / request_sha256
    output_dir = layout.outputs / "reader-map" / request_sha256
    return {
        "inventory": input_dir / "paragraph-inventory.json",
        "prompt": input_dir / "prompt.md",
        "manifest": input_dir / "manifest.json",
        "response": output_dir / "reader-map.response.json",
        "view": output_dir / f"{layout.stem}.reader-view.json",
        "preview": output_dir / f"{layout.stem}.guided.preview.tr.md",
    }


def _session_receipt_path(
    layout: AuthoringLayout, conversation: str, generation: str
) -> Path:
    if conversation not in {
        "scope-micro",
        "scope-macro",
        "scope-global",
        "scope-reconciler",
        "canonical-writer",
        "reader-map-writer",
        "invitation-writer",
    }:
        raise SystemExit(f"Unknown authoring conversation: {conversation}")
    if not isinstance(generation, str) or not re.fullmatch(r"[0-9a-f]{64}", generation):
        raise SystemExit("Authoring conversation generation must be a SHA-256")
    return layout.outputs / "sessions" / conversation / f"{generation}.json"


def _conversation_key(
    layout: AuthoringLayout, conversation: str, generation: str
) -> str:
    return (
        f"commentary-v3-authoring:{layout.folder}:{layout.stem}:"
        f"{conversation}:{generation}"
    )


def _json_pointer_get(value: Any, pointer: str) -> Any:
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise SystemExit(f"Invalid source JSON pointer: {pointer!r}")
    current = value
    if not pointer:
        return current
    for raw_token in pointer[1:].split("/"):
        if re.search(r"~(?:[^01]|$)", raw_token):
            raise SystemExit(f"Invalid source JSON pointer escape: {pointer!r}")
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list) and re.fullmatch(r"0|[1-9][0-9]*", token):
            index = int(token)
            if index >= len(current):
                raise SystemExit(f"Source JSON pointer does not resolve: {pointer}")
            current = current[index]
        else:
            raise SystemExit(f"Source JSON pointer does not resolve: {pointer}")
    return current


ARABIC_ROOT_EQUIVALENTS = str.maketrans(
    {"آ": "ء", "أ": "ء", "إ": "ء", "ؤ": "ء", "ئ": "ء", "ى": "ي"}
)


def _normalized_ar(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"[\sـ]", "", value.translate(ARABIC_ROOT_EQUIVALENTS))


def _branch_semantic_detail(source_branch: Any) -> dict[str, Any]:
    if not isinstance(source_branch, dict):
        return {}
    detail: dict[str, Any] = {}
    for field in (
        "branch_image_ar",
        "what_is_ar",
        "what_is_not_ar",
        "image_ar",
        "image_en",
        "scope_ar",
        "scope_en",
        "source_phrase_ar",
        "neighbor_coverage_note",
        "source_note",
    ):
        value = source_branch.get(field)
        if isinstance(value, str) and value.strip():
            detail[field] = value.strip()

    # These source-side contrasts and attested gloss families can preserve the
    # difference between a vivid branch image and a merely neighboring sense.
    # Keep them losslessly available to discovery agents instead of projecting
    # only one compact branch gloss.
    for field in (
        "contextual_glosses",
        "lexical_glosses",
        "excluded_glosses",
        "neighbor_distinctions",
        "sources",
    ):
        value = source_branch.get(field)
        if isinstance(value, (list, dict)) and value:
            detail[field] = value

    identity = source_branch.get("identity_judgment")
    if isinstance(identity, dict):
        for source_field, target_field in (
            ("rationale", "identity_rationale"),
            ("boundary_note", "boundary_detail"),
        ):
            value = identity.get(source_field)
            if isinstance(value, str) and value.strip():
                detail[target_field] = value.strip()

    lexicalization = source_branch.get("lexicalization_scope")
    if isinstance(lexicalization, dict):
        note = lexicalization.get("note")
        if isinstance(note, str) and note.strip():
            detail["lexicalization_note"] = note.strip()

    concept_map = source_branch.get("concept_map")
    if isinstance(concept_map, dict):
        definition = concept_map.get("definition")
        if isinstance(definition, str) and definition.strip():
            detail["definition"] = definition.strip()
        facets = []
        for facet in concept_map.get("facets", []):
            if not isinstance(facet, dict):
                continue
            statement = facet.get("statement")
            if not isinstance(statement, str) or not statement.strip():
                continue
            facets.append(
                {
                    "facet_id": facet.get("facet_id"),
                    "role": facet.get("role"),
                    "statement": statement.strip(),
                }
            )
        if facets:
            detail["distinctive_facets"] = facets

    concept_gloss = source_branch.get("concept_gloss")
    if isinstance(concept_gloss, dict):
        text = concept_gloss.get("text")
        applicability = concept_gloss.get("applicability")
        if isinstance(text, str) and text.strip():
            detail["concept_gloss"] = text.strip()
        if isinstance(applicability, str) and applicability.strip():
            detail["applicability"] = applicability.strip()

    synthesis = source_branch.get("source_synthesis")
    if isinstance(synthesis, dict):
        summary = synthesis.get("common_summary")
        if isinstance(summary, str) and summary.strip():
            detail["source_summary"] = summary.strip()
        qualifications = []
        for item in synthesis.get("source_details", []):
            if not isinstance(item, dict):
                continue
            item_summary = item.get("summary")
            if not isinstance(item_summary, str) or not item_summary.strip():
                continue
            qualifications.append(
                {"kind": item.get("kind"), "summary": item_summary.strip()}
            )
        if qualifications:
            detail["source_qualifications"] = qualifications
    return detail


def _branch_review_facets(semantic_detail: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize every reviewable branch facet to one stable local identity."""

    distinctive = semantic_detail.get("distinctive_facets", [])
    if not isinstance(distinctive, list):
        raise SystemExit("Branch distinctive_facets is malformed")
    normalized: list[dict[str, Any]] = []
    supplied_ids: set[str] = set()
    for facet in distinctive:
        if not isinstance(facet, dict):
            raise SystemExit("Branch distinctive_facets contains a malformed row")
        facet_id = facet.get("facet_id")
        statement = facet.get("statement")
        if (
            not isinstance(facet_id, str)
            or not facet_id
            or not isinstance(statement, str)
            or not statement.strip()
        ):
            raise SystemExit("A numbered branch facet lacks an identity or statement")
        if facet_id in supplied_ids:
            raise SystemExit(f"A branch repeats facet identity {facet_id}")
        supplied_ids.add(facet_id)
        normalized.append(
            {
                "facet_id": facet_id,
                "source_fields": [f"distinctive_facets[{facet_id}]"],
                "role": facet.get("role"),
                "statements": {"statement": statement.strip()},
            }
        )
    if normalized:
        return normalized

    # Older branch inventories sometimes carry one source image instead of a
    # numbered concept map. Pair translations under one identity, while
    # retaining independently authored Arabic fields as separate facets.
    fallback_groups = (
        ("SOURCE_IMAGE", ("image_ar", "image_en")),
        ("SOURCE_BRANCH_IMAGE", ("branch_image_ar",)),
        ("SOURCE_WHAT_IS", ("what_is_ar",)),
    )
    for facet_id, fields in fallback_groups:
        statements = {
            field: semantic_detail[field]
            for field in fields
            if isinstance(semantic_detail.get(field), str)
            and semantic_detail[field].strip()
        }
        if statements:
            normalized.append(
                {
                    "facet_id": facet_id,
                    "source_fields": list(statements),
                    "role": "source_semantic_image",
                    "statements": statements,
                }
            )
    return normalized


def _focus_root_occurrences(
    docket: dict[str, Any], root_id: Any, root_ar: Any
) -> list[dict[str, Any]]:
    root_key = _normalized_ar(root_ar)
    if not root_key and not isinstance(root_id, str):
        return []
    carriers = []
    for morpheme in docket.get("focus", {}).get("qac_morphemes", []):
        if not isinstance(morpheme, dict):
            continue
        qac_root = morpheme.get("root_ar")
        mapped_root_ids = docket.get("focus_root_mappings", {}).get(qac_root, [])
        mapped_match = isinstance(root_id, str) and root_id in mapped_root_ids
        fallback_match = _normalized_ar(qac_root) == root_key
        if not mapped_match and not fallback_match:
            continue
        carriers.append(
            {
                field: morpheme.get(field)
                for field in (
                    "qac_ref",
                    "qac_word_ref",
                    "surface_ar",
                    "lemma_ar",
                    "morpheme_role",
                    "pos",
                    "morph_features",
                )
            }
        )
    return carriers


def _focus_surface_evidence(docket: dict[str, Any]) -> dict[str, Any]:
    focus = docket.get("focus", {})
    word_rows: list[dict[str, Any]] = []
    for support in docket.get("support_registry", []):
        if not isinstance(support, dict) or support.get("source_type") != "word_analysis":
            continue
        pointer = support.get("json_pointer")
        if not isinstance(pointer, str) or not re.fullmatch(
            r"/word_analysis/words/[0-9]+", pointer
        ):
            continue
        text = support.get("text")
        if not isinstance(text, str):
            continue
        try:
            detail = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(detail, dict):
            continue
        word_index = int(pointer.rsplit("/", 1)[1])

        def display_parts(value: Any) -> dict[str, str]:
            if not isinstance(value, str):
                return {}
            match = re.fullmatch(
                r"\{\{ar:(.*?)\}\}\s*\(\{\{tr:(.*?)\}\}\)", value.strip()
            )
            if match is None:
                return {"note": value.strip()} if value.strip() else {}
            return {"arabic": match.group(1), "transliteration": match.group(2)}

        qac_ref_rows = focus.get("word_analysis_qac_refs", [])
        qac_refs = (
            qac_ref_rows[word_index] if word_index < len(qac_ref_rows) else []
        )
        word_rows.append(
            {
                "analysis_record_ref": support.get("source_local_id"),
                "qac_refs": qac_refs,
                "source_pointer": pointer,
                "surface": display_parts(detail.get("surface_display")),
                "root": display_parts(detail.get("root_display")),
                "analytic_gloss_range_en": detail.get("gloss_range"),
                "analytic_root_gloss_range_en": detail.get("root_gloss_range"),
            }
        )
    word_rows.sort(
        key=lambda item: int(str(item["source_pointer"]).rsplit("/", 1)[1])
    )
    return {
        "arabic_uthmani": focus.get("arabic_uthmani"),
        "qac_morphemes": focus.get("qac_morphemes", []),
        "word_analysis_refs": focus.get("word_analysis_refs", []),
        "word_analysis_qac_refs": focus.get("word_analysis_qac_refs", []),
        "word_rows": word_rows,
        "qualification": (
            "These records preserve supplied Arabic, transliteration, analytic "
            "gloss boundaries, and morphology for accurate prose. Analysis and "
            "QAC coordinates are internal provenance and must not appear in reader "
            "prose. English gloss ranges require a natural Turkish rendering. "
            "These are surface evidence, not a finding list and not proof of any "
            "secondary branch activation."
        ),
    }


def _is_locked_ref_segment_character(character: str) -> bool:
    """Return whether one Unicode character may carry identifier content."""

    return unicodedata.category(character)[0] in {"L", "M", "N"}


def _locked_ref_suffix_is_valid(suffix: str) -> bool:
    """Accept Unicode identifier segments joined by one explicit separator."""

    if not suffix:
        return False
    expect_segment_character = True
    for character in suffix:
        if expect_segment_character:
            if not _is_locked_ref_segment_character(character):
                return False
            expect_segment_character = False
        elif _is_locked_ref_segment_character(character):
            continue
        elif character in LOCKED_REF_SEPARATORS:
            expect_segment_character = True
        else:
            return False
    return not expect_segment_character


def _locked_ref_is_valid(locked_ref: str) -> bool:
    return locked_ref.startswith(LOCKED_REF_PREFIX) and _locked_ref_suffix_is_valid(
        locked_ref[len(LOCKED_REF_PREFIX) :]
    )


def _validate_locked_ref_tokens(locked_refs: set[str] | list[str]) -> None:
    invalid_locked_refs = sorted(
        ref for ref in locked_refs if not _locked_ref_is_valid(ref)
    )
    if invalid_locked_refs:
        raise SystemExit(
            "Locked finding refs must be atomic Unicode tokens in the locked: "
            "namespace; use letter/mark/number segments joined singly by "
            f"_, ., :, -, or /: {invalid_locked_refs}"
        )


def _extract_locked_ref_tokens(text: str) -> list[str]:
    """Extract canonical locked refs with Unicode-aware token boundaries."""

    tokens: list[str] = []
    cursor = 0
    while True:
        start = text.find(LOCKED_REF_PREFIX, cursor)
        if start < 0:
            break
        previous = text[start - 1] if start else ""
        if previous and (
            _is_locked_ref_segment_character(previous)
            or previous in LOCKED_REF_SEPARATORS
        ):
            cursor = start + len(LOCKED_REF_PREFIX)
            continue

        end = start + len(LOCKED_REF_PREFIX)
        while end < len(text) and (
            _is_locked_ref_segment_character(text[end])
            or text[end] in LOCKED_REF_SEPARATORS
        ):
            end += 1
        raw_token = text[start:end]
        # A full stop or colon immediately after a ref is ordinary sentence or
        # list punctuation. They are never valid terminal ref separators.
        while raw_token[-1:] in LOCKED_REF_SENTENCE_ENDINGS:
            raw_token = raw_token[:-1]
        tokens.append(raw_token)
        cursor = max(end, start + len(LOCKED_REF_PREFIX))
    return tokens


def _locked_finding_assignments(
    reconciled: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    locked_findings = reconciled.get("locked_findings")
    if not isinstance(locked_findings, list) or any(
        not isinstance(finding, dict) for finding in locked_findings
    ):
        raise SystemExit("Reconciled findings lack a locked finding list")
    locked_refs = [
        finding.get("locked_finding_ref") for finding in locked_findings
    ]
    if any(not isinstance(ref, str) or not ref for ref in locked_refs):
        raise SystemExit("Every locked finding requires a nonempty reference")
    if len(set(locked_refs)) != len(locked_refs):
        raise SystemExit("Reconciled findings contain duplicate locked references")
    _validate_locked_ref_tokens(locked_refs)
    locked_by_ref = dict(zip(locked_refs, locked_findings, strict=True))
    member_refs = {
        member_ref
        for locked_ref, finding in locked_by_ref.items()
        for member_ref in _string_list(
            finding.get("member_finding_refs"),
            label=f"locked finding {locked_ref} member_finding_refs",
            allow_empty=False,
        )
    }
    namespace_collisions = sorted(set(locked_refs) & member_refs)
    if namespace_collisions:
        raise SystemExit(
            "Locked and member finding refs must be disjoint: "
            f"{namespace_collisions}"
        )

    assignments = reconciled.get("scope_assignments")
    if not isinstance(assignments, dict) or set(assignments) != set(LANES):
        raise SystemExit("Reconciled findings lack exact scope assignments")
    assigned_union: set[str] = set()
    for lane in LANES:
        assigned_refs = assignments[lane]
        if (
            not isinstance(assigned_refs, list)
            or any(
                not isinstance(item, str) or not item for item in assigned_refs
            )
            or len(set(assigned_refs)) != len(assigned_refs)
        ):
            raise SystemExit(f"Invalid {lane} scope assignment list")
        unknown = sorted(set(assigned_refs) - set(locked_by_ref))
        if unknown:
            raise SystemExit(
                f"{lane} assignments cite unknown locked findings: {unknown}"
            )
        assigned_union.update(assigned_refs)
    omitted = sorted(set(locked_by_ref) - assigned_union)
    if omitted:
        raise SystemExit(
            f"Locked findings omitted from all scope assignments: {omitted}"
        )
    for locked_ref, finding in locked_by_ref.items():
        owning_lane = finding.get("lane")
        if owning_lane not in LANES:
            raise SystemExit(
                f"Locked finding {locked_ref} has an invalid owning lane"
            )
        if locked_ref not in assignments[owning_lane]:
            raise SystemExit(
                f"Locked finding {locked_ref} is not assigned to its owning "
                f"{owning_lane} prose lane"
            )
    return locked_by_ref, assignments


def _flatten_branches(
    docket: dict[str, Any],
    source_bundle: dict[str, Any],
    candidates: list[dict[str, Any]],
    supports: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    candidate_links: dict[str, list[dict[str, Any]]] = {}
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        refs = {
            branch_ref
            for field in (
                "branch_refs",
                "focus_branch_refs",
                "nominated_branch_refs",
                "unresolved_branch_refs",
            )
            for branch_ref in candidate.get(field, [])
            if isinstance(branch_ref, str) and branch_ref
        }
        for branch_ref in refs:
            candidate_links.setdefault(branch_ref, []).append(
                {
                    "candidate_id": candidate.get("candidate_id"),
                    "lane": candidate.get("lane"),
                }
            )

    support_links: dict[str, list[str]] = {}
    for support in supports:
        if not isinstance(support, dict):
            continue
        support_id = support.get("support_id")
        for branch_ref in support.get("branch_refs", []):
            if isinstance(branch_ref, str) and branch_ref:
                support_links.setdefault(branch_ref, []).append(support_id)

    def record(
        *,
        branch: dict[str, Any],
        registry: str,
        root_id: Any,
        root_ar: Any,
        gloss: Any,
        boundary: Any,
        status: Any,
        branch_kind: Any,
    ) -> dict[str, Any]:
        branch_ref = branch.get("branch_ref")
        source_pointer = branch.get("source_pointer")
        source_branch = (
            _json_pointer_get(source_bundle, source_pointer)
            if isinstance(source_pointer, str) and source_pointer
            else None
        )
        if not isinstance(source_branch, dict):
            raise SystemExit(f"Branch source is not an object: {branch_ref}")
        if registry == "focus" and source_branch.get("branch_ref") != branch_ref:
            raise SystemExit(f"Focus branch source identity mismatch: {branch_ref}")
        if registry == "nominated" and source_branch.get("root_id") != root_id:
            raise SystemExit(
                f"Nominated branch source root identity mismatch: {branch_ref}"
            )
        source_detail = _branch_semantic_detail(source_branch)
        return {
            "branch_ref": branch_ref,
            "registry": registry,
            "root_id": root_id,
            "root_ar": root_ar,
            "lexicon_identity_status": status,
            "branch_kind": branch_kind,
            "gloss": gloss,
            "boundary": boundary,
            "source_pointer": source_pointer,
            "semantic_detail": source_detail,
            "review_facets": _branch_review_facets(source_detail),
            "focus_root_occurrences": _focus_root_occurrences(
                docket, root_id, root_ar
            ),
            "root_occurrence_qualification": (
                "These are focus-ayah occurrences mapped to the same root. "
                "They identify possible surface carriers but do not prove that "
                "this branch sense is active. Activation still requires an "
                "independent linguistic or contextual trigger."
            ),
            "candidate_links": candidate_links.get(branch_ref, []),
            "support_links": sorted(
                item
                for item in support_links.get(branch_ref, [])
                if isinstance(item, str) and item
            ),
        }

    flattened: list[dict[str, Any]] = []
    for root in docket.get("branch_registry", []):
        for branch in root.get("branches", []):
            flattened.append(
                record(
                    branch=branch,
                    registry="focus",
                    root_id=root.get("root_id"),
                    root_ar=root.get("root_ar"),
                    status=branch.get("status"),
                    branch_kind=branch.get("branch_kind"),
                    gloss=branch.get("gloss"),
                    boundary=branch.get("boundary"),
                )
            )
    for branch in docket.get("nominated_branch_registry", []):
        flattened.append(
            record(
                branch=branch,
                registry="nominated",
                root_id=str(branch.get("branch_ref", "")).split("/", 1)[0],
                root_ar=branch.get("root_ar"),
                status=None,
                branch_kind=None,
                gloss=branch.get("image_en") or branch.get("image_ar"),
                boundary=branch.get("scope_en") or branch.get("scope_ar"),
            )
        )
    return flattened


def _hft_authoring_projection(
    docket: dict[str, Any], source_bundle: dict[str, Any]
) -> dict[str, Any]:
    """Project every parseable HFT insight without inheriting legacy gates.

    The prepared docket may legitimately keep strict provenance and publication
    checks. Those checks are qualifications at the experimental authoring
    boundary: they must not make readable linguistic material disappear before
    a scope agent can assess it.
    """

    focus_ref = str(docket["identity"]["ayah_ref"])
    pericope_refs = {
        ref
        for ref in docket["scope"]["pericope"].get("refs", [])
        if isinstance(ref, str)
    }
    raw_hft = source_bundle.get("v12_focus_trace_hermetic")
    source_present = raw_hft is not None
    unstructured_hft = (
        raw_hft
        if raw_hft is not None and not isinstance(raw_hft, dict)
        else None
    )
    hft = raw_hft if isinstance(raw_hft, dict) else {}
    docket_assessment = docket.get("scope", {}).get("hft")
    diagnostics: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    reader_metadata: list[dict[str, Any]] = []

    policy = {
        "parseable_hft_is_always_visible_to_authoring": True,
        "provenance_affects_qualification_not_visibility": True,
        "scope_mismatch_affects_lane_assignment_not_visibility": True,
        "unresolved_branch_citations_do_not_suppress_records": True,
        "every_assigned_record_requires_explicit_review": True,
    }
    if not source_present:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic",
                "warning": "HFT payload is absent",
            }
        )
    elif unstructured_hft is not None:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic",
                "warning": (
                    "HFT payload is not an object; its raw value is preserved as "
                    "a global unstructured review record"
                ),
            }
        )

    packet_summary = hft.get("packet_summary")
    packet_window = (
        packet_summary.get("window")
        if isinstance(packet_summary, dict)
        and isinstance(packet_summary.get("window"), list)
        else []
    )
    valid_packet_window = {
        ref
        for ref in packet_window
        if isinstance(ref, str)
        and re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", ref)
    }
    if valid_packet_window == pericope_refs:
        packet_scope_relation = "exact_declared_pericope"
    elif pericope_refs and pericope_refs < valid_packet_window:
        packet_scope_relation = "broader_than_declared_pericope"
    elif valid_packet_window and valid_packet_window < pericope_refs:
        packet_scope_relation = "narrower_than_declared_pericope"
    else:
        packet_scope_relation = "different_or_unresolved"

    raw_readers = hft.get("readers")
    unstructured_readers = (
        raw_readers
        if raw_readers is not None and not isinstance(raw_readers, dict)
        else None
    )
    readers = raw_readers if isinstance(raw_readers, dict) else {}
    if unstructured_readers is not None:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic/readers",
                "warning": (
                    "HFT readers value is not an object; its raw value is "
                    "preserved as a global unstructured review record"
                ),
            }
        )

    def add_record(
        *,
        reader_id: str,
        kind: str,
        item_id: str,
        source_pointer: str,
        raw_item: Any,
        reader_identity_status: str,
        anchor_refs: list[str],
        branch_refs: list[str],
        item_warnings: list[str],
        anchor_scope_complete: bool = True,
    ) -> None:
        unique_anchors = sorted(set(anchor_refs))
        unique_branches = sorted(set(branch_refs))
        if not anchor_scope_complete:
            owning_lane = "global"
            lane_basis = (
                "one or more HFT anchors could not be resolved, so the record "
                "is conservatively visible in the widest lane"
            )
            evidence_scope = "wider_or_unresolved_record"
        elif unique_anchors and set(unique_anchors) == {focus_ref}:
            owning_lane = "micro"
            lane_basis = "all explicit HFT anchors are the focus ayah"
            evidence_scope = "focus_ayah"
        elif unique_anchors and set(unique_anchors) <= pericope_refs:
            owning_lane = "macro"
            lane_basis = "all explicit HFT anchors lie in the declared pericope"
            evidence_scope = "declared_pericope"
        else:
            owning_lane = "global"
            lane_basis = (
                "one or more explicit HFT anchors lie beyond the declared pericope"
                if unique_anchors
                else "unanchored reader synthesis is assigned to the widest lane"
            )
            evidence_scope = "wider_record"

        hft_ref = "hft_" + _sha256_json(
            {
                "reader_id": reader_id,
                "kind": kind,
                "item_id": item_id,
                "source_pointer": source_pointer,
            }
        )[:20]
        support_id = "sup_" + _sha256_json(
            {
                "hft_ref": hft_ref,
                "raw_payload": raw_item,
            }
        )[:20]
        candidate_id = "cand_" + _sha256_json(
            {
                "ayah_ref": focus_ref,
                "lane": owning_lane,
                "hft_ref": hft_ref,
            }
        )[:20]
        records.append(
            {
                "hft_ref": hft_ref,
                "reader_id": reader_id,
                "kind": kind,
                "item_id": item_id,
                "source_local_id": f"{reader_id}:{item_id}",
                "source_pointer": source_pointer,
                "anchor_refs": unique_anchors,
                "branch_refs": unique_branches,
                "owning_lane": owning_lane,
                "lane_basis": lane_basis,
                "evidence_scope": evidence_scope,
                "candidate_id": candidate_id,
                "support_id": support_id,
                "raw_item": raw_item,
                "qualification": {
                    "reader_identity_status": reader_identity_status,
                    "packet_scope_relation": packet_scope_relation,
                    "anchor_scope_complete": anchor_scope_complete,
                    "record_warnings": list(dict.fromkeys(item_warnings)),
                    "authoring_effect": (
                        "Source qualifications affect epistemic status and "
                        "containment, never visibility or presumptive outcome."
                    ),
                },
            }
        )

    if unstructured_hft is not None:
        add_record(
            reader_id="unstructured_hft",
            kind="unstructured_hft_payload",
            item_id="unstructured_hft_payload",
            source_pointer="/v12_focus_trace_hermetic",
            raw_item=unstructured_hft,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["top-level HFT payload is not an object"],
            anchor_scope_complete=False,
        )
    if unstructured_readers is not None:
        add_record(
            reader_id="unstructured_readers",
            kind="unstructured_hft_readers",
            item_id="unstructured_hft_readers",
            source_pointer="/v12_focus_trace_hermetic/readers",
            raw_item=unstructured_readers,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["HFT readers value is not an object"],
            anchor_scope_complete=False,
        )

    def pointer_token(value: Any) -> str:
        return str(value).replace("~", "~0").replace("/", "~1")

    for extension_key, extension_value in hft.items():
        if extension_key in {"packet_summary", "readers"}:
            continue
        extension_pointer = (
            "/v12_focus_trace_hermetic/" + pointer_token(extension_key)
        )
        diagnostics.append(
            {
                "source_pointer": extension_pointer,
                "warning": (
                    "Unrecognized HFT envelope field is preserved as a global "
                    "review record"
                ),
            }
        )
        add_record(
            reader_id="hft_envelope",
            kind="hft_envelope_extension",
            item_id=f"envelope_extension:{extension_key}",
            source_pointer=extension_pointer,
            raw_item=extension_value,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["unrecognized HFT envelope field"],
            anchor_scope_complete=False,
        )

    def summary_leaves(
        value: Any, source_pointer: str, path: tuple[str, ...] = ()
    ) -> list[tuple[tuple[str, ...], str, Any]]:
        leaves: list[tuple[tuple[str, ...], str, Any]] = []
        if isinstance(value, dict) and value:
            for key, child in value.items():
                leaves.extend(
                    summary_leaves(
                        child,
                        f"{source_pointer}/{pointer_token(key)}",
                        (*path, str(key)),
                    )
                )
        elif isinstance(value, list) and value:
            for index, child in enumerate(value):
                leaves.extend(
                    summary_leaves(
                        child,
                        f"{source_pointer}/{index}",
                        (*path, str(index)),
                    )
                )
        else:
            leaves.append((path, source_pointer, value))
        return leaves

    for reader_id in sorted(readers):
        raw_reader = readers[reader_id]
        reader_pointer = (
            "/v12_focus_trace_hermetic/readers/" + pointer_token(reader_id)
        )
        if not isinstance(reader_id, str) or not isinstance(raw_reader, dict):
            diagnostics.append(
                {
                    "source_pointer": reader_pointer,
                    "warning": (
                        "HFT reader response has invalid structure; its raw value "
                        "is preserved as a global unstructured review record"
                    ),
                }
            )
            add_record(
                reader_id=str(reader_id),
                kind="unstructured_hft_reader",
                item_id="unstructured_reader",
                source_pointer=reader_pointer,
                raw_item=raw_reader,
                reader_identity_status="unresolved",
                anchor_refs=[],
                branch_refs=[],
                item_warnings=["HFT reader response is not an object"],
                anchor_scope_complete=False,
            )
            continue
        packet_identity = raw_reader.get("packet_identity")
        reader_identity_status = (
            "identity_supplied_unverified"
            if isinstance(packet_identity, dict)
            else "legacy_unbound"
        )
        reader_metadata.append(
            {
                "reader_id": reader_id,
                "focus_ref": raw_reader.get("focus_ref"),
                "protocol": raw_reader.get("protocol"),
                "trace_kind": raw_reader.get("trace_kind"),
                "packet_identity": packet_identity,
                "identity_status": reader_identity_status,
                "source_pointer": reader_pointer,
            }
        )

        if "summary" in raw_reader:
            for summary_path, summary_pointer, summary_item in summary_leaves(
                raw_reader.get("summary"), f"{reader_pointer}/summary"
            ):
                path_label = "/".join(summary_path) or "value"
                add_record(
                    reader_id=reader_id,
                    kind="reader_summary_claim",
                    item_id=f"reader_summary:{path_label}",
                    source_pointer=summary_pointer,
                    raw_item=summary_item,
                    reader_identity_status=reader_identity_status,
                    anchor_refs=[],
                    branch_refs=[],
                    item_warnings=[
                        "Unanchored reader synthesis must be assessed as one "
                        "inventory item, not accepted as a surah thesis."
                    ],
                )

        recognized_reader_fields = {
            "reader_id",
            "focus_ref",
            "protocol",
            "trace_kind",
            "packet_identity",
            "summary",
            *(field for field, _kind, _id_field in HFT_RECORD_FIELDS),
        }
        for extension_key, extension_value in raw_reader.items():
            if extension_key in recognized_reader_fields:
                continue
            extension_pointer = (
                f"{reader_pointer}/{pointer_token(extension_key)}"
            )
            diagnostics.append(
                {
                    "source_pointer": extension_pointer,
                    "warning": (
                        "Unrecognized HFT reader field is preserved as a global "
                        "review record"
                    ),
                }
            )
            add_record(
                reader_id=reader_id,
                kind="hft_reader_extension",
                item_id=f"reader_extension:{extension_key}",
                source_pointer=extension_pointer,
                raw_item=extension_value,
                reader_identity_status=reader_identity_status,
                anchor_refs=[],
                branch_refs=[],
                item_warnings=["unrecognized HFT reader field"],
                anchor_scope_complete=False,
            )

        for field, kind, id_field in HFT_RECORD_FIELDS:
            raw_items = raw_reader.get(field)
            field_pointer = f"{reader_pointer}/{field}"
            if not isinstance(raw_items, list):
                diagnostics.append(
                    {
                        "source_pointer": field_pointer,
                        "warning": f"{field} is not an array",
                    }
                )
                if raw_items is not None:
                    add_record(
                        reader_id=reader_id,
                        kind=f"{kind}_unstructured_field",
                        item_id=f"{field}_unstructured",
                        source_pointer=field_pointer,
                        raw_item=raw_items,
                        reader_identity_status=reader_identity_status,
                        anchor_refs=[],
                        branch_refs=[],
                        item_warnings=[
                            f"{field} is not an array; raw JSON remains visible"
                        ],
                        anchor_scope_complete=False,
                    )
                continue
            for index, raw_item in enumerate(raw_items):
                source_pointer = f"{field_pointer}/{index}"
                item_warnings: list[str] = []
                if isinstance(raw_item, dict):
                    raw_item_id = raw_item.get(id_field)
                    item_id = (
                        raw_item_id.strip()
                        if isinstance(raw_item_id, str) and raw_item_id.strip()
                        else f"{field}_{index}"
                    )
                    if item_id == f"{field}_{index}":
                        item_warnings.append(
                            f"record has no nonempty {id_field}; fallback identity used"
                        )
                    activation_trace = raw_item.get("activation_trace")
                else:
                    item_id = f"{field}_{index}"
                    activation_trace = None
                    item_warnings.append(
                        "record is not an object; raw JSON remains visible"
                    )

                anchor_refs: list[str] = []
                branch_refs: list[str] = []
                anchor_scope_complete = True
                if not isinstance(activation_trace, list):
                    anchor_scope_complete = False
                    item_warnings.append(
                        "activation_trace is absent or is not an array"
                    )
                else:
                    for trace_index, trace in enumerate(activation_trace):
                        if not isinstance(trace, dict):
                            anchor_scope_complete = False
                            item_warnings.append(
                                f"activation_trace[{trace_index}] is not an object"
                            )
                            continue
                        source_ref = trace.get("source_ref")
                        if isinstance(source_ref, str) and re.fullmatch(
                            r"[1-9][0-9]*:[1-9][0-9]*", source_ref
                        ):
                            anchor_refs.append(source_ref)
                        else:
                            anchor_scope_complete = False
                            item_warnings.append(
                                f"activation_trace[{trace_index}] has no canonical "
                                "source_ref"
                            )
                        root_id = trace.get("mapped_root_id")
                        branch_id = trace.get("branch_id")
                        if (
                            isinstance(root_id, str)
                            and root_id
                            and isinstance(branch_id, str)
                            and branch_id
                        ):
                            branch_refs.append(f"{root_id}/{branch_id}")
                        elif root_id is not None or branch_id is not None:
                            item_warnings.append(
                                f"activation_trace[{trace_index}] has an incomplete "
                                "branch citation"
                            )
                add_record(
                    reader_id=reader_id,
                    kind=kind,
                    item_id=item_id,
                    source_pointer=source_pointer,
                    raw_item=raw_item,
                    reader_identity_status=reader_identity_status,
                    anchor_refs=anchor_refs,
                    branch_refs=branch_refs,
                    item_warnings=item_warnings,
                    anchor_scope_complete=anchor_scope_complete,
                )

    refs = [record["hft_ref"] for record in records]
    candidate_ids = [record["candidate_id"] for record in records]
    support_ids = [record["support_id"] for record in records]
    if len(refs) != len(set(refs)):
        raise SystemExit("HFT authoring projection produced duplicate record refs")
    if len(candidate_ids) != len(set(candidate_ids)):
        raise SystemExit("HFT authoring projection produced duplicate candidate IDs")
    if len(support_ids) != len(set(support_ids)):
        raise SystemExit("HFT authoring projection produced duplicate support IDs")

    manifest_fields = (
        "hft_ref",
        "reader_id",
        "kind",
        "item_id",
        "source_local_id",
        "source_pointer",
        "anchor_refs",
        "branch_refs",
        "owning_lane",
        "lane_basis",
        "candidate_id",
        "support_id",
        "qualification",
    )
    return {
        "policy": policy,
        "source_present": source_present,
        "packet_summary": packet_summary,
        "docket_assessment": docket_assessment,
        "reader_metadata": reader_metadata,
        "provenance": {
            "packet_scope_relation": packet_scope_relation,
            "legacy_docket_assessment": docket_assessment,
            "reader_identity": reader_metadata,
            "authoring_effect": (
                "This is one neutral source qualification. It controls "
                "epistemic status and containment, never evidence visibility "
                "or presumptive acceptance/rejection."
            ),
        },
        "records": records,
        "record_manifest": [
            {field: record[field] for field in manifest_fields}
            for record in records
        ],
        "lane_counts": {
            lane: sum(record["owning_lane"] == lane for record in records)
            for lane in LANES
        },
        "structured_insight_count": sum(
            record["kind"]
            in {"baseline_model", "context_delta", "surprising_outlier"}
            for record in records
        ),
        "reader_synthesis_count": sum(
            record["kind"] == "reader_summary_claim" for record in records
        ),
        "unstructured_record_count": sum(
            "unstructured" in record["kind"]
            or record["kind"].endswith("_extension")
            for record in records
        ),
        "diagnostics": diagnostics,
    }


def _connection_evidence_ref(
    connection_ref: str, direction: str, row: dict[str, Any]
) -> str:
    return "conn_ev_" + _sha256_json(
        {
            "connection_ref": connection_ref,
            "direction": direction,
            "source_row": row,
        }
    )[:20]


def _lane_packet(
    docket: dict[str, Any],
    lane: str,
    source_bundle: dict[str, Any],
    hft_projection: dict[str, Any],
    inter_ayah_rows: list[dict[str, Any]],
    reciprocal_evidence: dict[str, list[dict[str, Any]]],
    inter_ayah_source_coverage: dict[str, Any],
    quran_text_evidence: dict[str, dict[str, Any]],
    quran_text_coverage: dict[str, Any],
) -> dict[str, Any]:
    assigned_hft = [
        record
        for record in hft_projection.get("records", [])
        if record.get("owning_lane") == lane
    ]
    hft_candidates = [
        {
            "candidate_id": record["candidate_id"],
            "ayah_ref": docket["identity"]["ayah_ref"],
            "lane": lane,
            "source_type": "hft",
            "source_local_id": record["source_local_id"],
            "source_pointer": record["source_pointer"],
            "kind": record["kind"],
            "title": record["item_id"],
            "scope": record["evidence_scope"],
            "anchor_refs": record["anchor_refs"],
            "branch_refs": record["branch_refs"],
            "support_ids": [record["support_id"]],
            "trust": record["qualification"]["reader_identity_status"],
            "hft_ref": record["hft_ref"],
            "lane_assignment_basis": record["lane_basis"],
            "provenance_qualification": record["qualification"],
            "authoring_origin": "lossless_raw_hft_projection",
            "obligation": "review",
        }
        for record in assigned_hft
    ]
    hft_supports: list[dict[str, Any]] = []
    for record in assigned_hft:
        anchor_evidence: list[dict[str, Any]] = []
        missing_anchor_refs: list[str] = []
        for anchor_ref in record["anchor_refs"]:
            evidence = quran_text_evidence.get(anchor_ref)
            if isinstance(evidence, dict):
                anchor_evidence.append(evidence)
            else:
                missing_anchor_refs.append(anchor_ref)
        hft_supports.append(
            {
                "support_id": record["support_id"],
                "source_type": "hft",
                "source_local_id": record["source_local_id"],
                "scope": lane,
                "json_pointer": record["source_pointer"],
                "role": "hft_nomination_evidence",
                "branch_refs": record["branch_refs"],
                "payload": record["raw_item"],
                "anchor_evidence": anchor_evidence,
                "anchor_evidence_coverage": {
                    "cited_anchor_count": len(record["anchor_refs"]),
                    "supplied_anchor_count": len(anchor_evidence),
                    "missing_anchor_refs": missing_anchor_refs,
                    "exact_arabic_is_surface_evidence_only": True,
                    "target_morphology_supplied": False,
                    "boundary": (
                        "Exact Arabic verifies surface contact only. HFT-stated "
                        "segmentation, word indices, roots, branches, and roles "
                        "remain attributed nominations unless independently "
                        "supplied elsewhere in this packet."
                    ),
                },
                "trust": record["qualification"]["reader_identity_status"],
                "qualification": record["qualification"],
            }
        )
    replace_legacy_hft_candidates = bool(hft_projection.get("records"))
    raw_candidates = [
        candidate
        for candidate in docket.get("candidates", [])
        if candidate.get("lane") == lane
        and not (
            replace_legacy_hft_candidates
            and candidate.get("source_type") == "hft"
        )
    ] + hft_candidates
    transport_fields = {
        "mandatory",
        "selection_eligible",
        "selection_ineligibility_reasons",
        "adjudicable",
        "obligation",
    }
    candidates = [
        {
            **{
                key: value
                for key, value in candidate.items()
                if key not in transport_fields
            },
            "commentary_obligation": candidate.get("obligation"),
        }
        for candidate in raw_candidates
    ]
    candidate_refs = [candidate.get("candidate_id") for candidate in candidates]
    if len(candidate_refs) != len(set(candidate_refs)):
        raise SystemExit(f"{lane} packet contains duplicate candidate IDs")
    support_ids = {
        support_id
        for candidate in candidates
        for support_id in candidate.get("support_ids", [])
    }
    supports = [
        support
        for support in docket.get("support_registry", [])
        if support.get("support_id") in support_ids
    ] + hft_supports
    support_refs = [support.get("support_id") for support in supports]
    if len(support_refs) != len(set(support_refs)):
        raise SystemExit(f"{lane} packet contains duplicate support IDs")
    if {item.get("support_id") for item in supports} != support_ids:
        missing = sorted(support_ids - {item.get("support_id") for item in supports})
        raise SystemExit(f"{lane} packet is missing candidate supports: {missing}")

    candidate_branch_refs = {
        branch_ref
        for candidate in candidates
        for field in (
            "branch_refs",
            "focus_branch_refs",
            "nominated_branch_refs",
            "unresolved_branch_refs",
        )
        for branch_ref in candidate.get(field, [])
    }
    support_branch_refs = {
        branch_ref
        for support in supports
        for branch_ref in support.get("branch_refs", [])
    }
    relevant_branch_refs = candidate_branch_refs | support_branch_refs
    flattened_branches = _flatten_branches(
        docket, source_bundle, candidates, supports
    )
    known_branches: dict[str, dict[str, Any]] = {}
    for item in flattened_branches:
        branch_ref = item.get("branch_ref")
        if not isinstance(branch_ref, str) or not branch_ref:
            continue
        if branch_ref in known_branches:
            raise SystemExit(f"Duplicate branch reference in lane atlas: {branch_ref}")
        known_branches[branch_ref] = item
    # Every lane needs the complete focus-root atlas to discover an uncandidate
    # contact. Scope isolation is carried by each lane's evidence and decision
    # question, not by hiding local semantic facets from macro/global readers.
    included_refs = {
        branch_ref
        for branch_ref, item in known_branches.items()
        if item.get("registry") == "focus"
    } | (relevant_branch_refs & set(known_branches))
    branches = [known_branches[branch_ref] for branch_ref in sorted(included_refs)]
    unresolved_branch_refs = sorted(relevant_branch_refs - set(known_branches))
    hft_branch_citations: dict[str, list[dict[str, Any]]] = {}
    for record in assigned_hft:
        raw_item = record.get("raw_item")
        traces = raw_item.get("activation_trace") if isinstance(raw_item, dict) else []
        if not isinstance(traces, list):
            continue
        for trace in traces:
            if not isinstance(trace, dict):
                continue
            root_id = trace.get("mapped_root_id")
            branch_id = trace.get("branch_id")
            if not (
                isinstance(root_id, str)
                and root_id
                and isinstance(branch_id, str)
                and branch_id
            ):
                continue
            branch_ref = f"{root_id}/{branch_id}"
            hft_branch_citations.setdefault(branch_ref, []).append(
                {
                    "hft_ref": record["hft_ref"],
                    "source_ref": trace.get("source_ref"),
                    "root": trace.get("root"),
                    "source_word_indices": trace.get("source_word_indices"),
                    "role": trace.get("role"),
                    "qualification": (
                        "This is the HFT reader's exact attributed branch role, "
                        "not an independently supplied lexicon entry."
                    ),
                }
            )
    branches.extend(
        {
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "root_id": branch_ref.split("/", 1)[0],
            "root_ar": None,
            "lexicon_identity_status": "unresolved",
            "branch_kind": None,
            "gloss": None,
            "boundary": (
                "No separate registered branch descriptor is supplied. The exact "
                "HFT citation and attributed role remain reviewable, but they do "
                "not become independently verified lexicon evidence."
            ),
            "source_pointer": None,
            "semantic_detail": {},
            "review_facets": [],
            "focus_root_occurrences": [],
            "root_occurrence_qualification": (
                "No registered root occurrence is supplied; this unresolved "
                "citation cannot establish a branch carrier."
            ),
            "candidate_links": [
                {
                    "candidate_id": candidate.get("candidate_id"),
                    "lane": candidate.get("lane"),
                }
                for candidate in candidates
                if branch_ref
                in {
                    cited_ref
                    for field in (
                        "branch_refs",
                        "focus_branch_refs",
                        "nominated_branch_refs",
                        "unresolved_branch_refs",
                    )
                    for cited_ref in candidate.get(field, [])
                }
            ],
            "support_links": sorted(
                support.get("support_id")
                for support in supports
                if branch_ref in support.get("branch_refs", [])
                and isinstance(support.get("support_id"), str)
            ),
            "hft_citations": hft_branch_citations.get(branch_ref, []),
        }
        for branch_ref in unresolved_branch_refs
    )
    projected_refs = {item["branch_ref"] for item in branches}
    if not relevant_branch_refs <= projected_refs:
        raise SystemExit(f"{lane} packet failed to preserve every referenced branch")

    connection_registry: list[dict[str, Any]] = []
    focus_ref = str(docket["identity"]["ayah_ref"])
    focus_surah = focus_ref.split(":", 1)[0]
    pericope_refs = set(docket["scope"]["pericope"].get("refs", []))

    def target_evidence(target_ref: str) -> dict[str, Any]:
        evidence = quran_text_evidence.get(target_ref)
        if not isinstance(evidence, dict):
            raise SystemExit(f"Quran text source lacks connection target {target_ref}")
        return evidence

    def with_range_evidence(row: dict[str, Any]) -> dict[str, Any]:
        component_refs = row.get("source_target_components", [])
        if not isinstance(component_refs, list) or not all(
            isinstance(ref, str) for ref in component_refs
        ):
            raise SystemExit("Projected inter-ayah row has malformed range components")
        return {
            **row,
            "source_target_range_evidence": (
                [target_evidence(ref) for ref in component_refs]
                if row.get("source_target_is_range")
                else []
            ),
        }

    reciprocal_evidence_with_ranges = {
        target_ref: [with_range_evidence(row) for row in rows]
        for target_ref, rows in reciprocal_evidence.items()
    }

    for index, row in enumerate(inter_ayah_rows):
        if not isinstance(row, dict):
            raise SystemExit(f"Malformed projected inter-ayah row at index {index}")
        target_ref = row.get("ref")
        if not isinstance(target_ref, str) or not re.fullmatch(
            r"[1-9][0-9]*:[1-9][0-9]*", target_ref
        ):
            raise SystemExit(f"Malformed projected inter-ayah target at index {index}")
        if target_ref == focus_ref:
            owning_lane = "macro"
            relation_scope = "self_reference_source_row"
        elif target_ref in pericope_refs:
            owning_lane = "macro"
            relation_scope = "declared_pericope"
        else:
            owning_lane = "global"
            relation_scope = (
                "inter_surah"
                if target_ref.split(":", 1)[0] != focus_surah
                else "same_surah_beyond_pericope"
            )
        if lane != owning_lane:
            continue
        source_pointer = row.get("source_pointer")
        projection_pointer = row.get("projection_pointer")
        if not isinstance(source_pointer, str) or not isinstance(
            projection_pointer, str
        ):
            raise SystemExit(
                f"Projected inter-ayah row lacks provenance at index {index}"
            )
        connection_ref = "conn_" + _sha256_json(
            {
                "focus_ref": focus_ref,
                "target_ref": target_ref,
                "projection_record_sha256": row.get(
                    "projection_record_sha256"
                ),
            }
        )[:20]
        authored_evidence_ref = _connection_evidence_ref(
            connection_ref, "focus_to_target", row
        )
        reverse_rows = [
            {
                **item,
                "connection_evidence_ref": _connection_evidence_ref(
                    connection_ref, "target_to_focus", item
                ),
            }
            for item in reciprocal_evidence_with_ranges.get(target_ref, [])
        ]
        has_reciprocal_nomination = any(
            item.get("record_type") == "reciprocal_nomination"
            for item in reverse_rows
        )
        has_reciprocal_counterevidence = any(
            item.get("record_type") == "reciprocal_counterevidence"
            for item in reverse_rows
        )
        has_reciprocal_suggestion = any(
            item.get("source_row_role") == "missing_ayah_suggestion"
            for item in reverse_rows
        )
        is_self_reference = target_ref == focus_ref
        is_range_target = bool(row.get("source_target_is_range"))
        range_evidence = with_range_evidence(row)[
            "source_target_range_evidence"
        ]
        connection = {
            "connection_ref": connection_ref,
            "connection_evidence_ref": authored_evidence_ref,
            "target_ref": target_ref,
            "relation_scope": relation_scope,
            "origin": "authored_focus_row",
            "prior_label": row.get("label"),
            "note": row.get("note"),
            "source_pointer": source_pointer,
            "projection_pointer": projection_pointer,
            "source_row_sha256": row.get("source_row_sha256"),
            "source_file": row.get("source_file"),
            "source_line": row.get("source_line"),
            "source_column_order": row.get("source_column_order"),
            "source_row_role": row.get("source_row_role"),
            "source_target_ref": row.get("source_target_ref"),
            "source_target_component_ref": row.get(
                "source_target_component_ref"
            ),
            "source_target_is_range": is_range_target,
            "source_target_components": row.get("source_target_components"),
            "source_target_range_evidence": range_evidence,
            "source_target_range_boundary": row.get(
                "source_target_range_boundary"
            ),
            "target_evidence": target_evidence(target_ref),
            "reciprocal_evidence": reverse_rows,
            "qualification": {
                "prior_label_is_not_a_decision": True,
                "has_reciprocal_nomination": has_reciprocal_nomination,
                "has_reciprocal_counterevidence": (
                    has_reciprocal_counterevidence
                ),
                "has_reciprocal_missing_ayah_suggestion": (
                    has_reciprocal_suggestion
                ),
                "source_row_role_is_provenance_not_a_decision": True,
                "reciprocal_source_direction_labels_are_not_focus_decisions": (
                    bool(reverse_rows)
                ),
                "self_reference_is_source_emphasis_not_reciprocity": (
                    is_self_reference
                ),
                "source_note_is_range_level": is_range_target,
                "target_ayah_text_supplied": True,
                "target_morphology_supplied": False,
                "boundary": (
                    "This preserved source row points to the focus ayah itself. "
                    "Treat it as source emphasis or coverage, not an independent "
                    "contextual relation or reciprocal corroboration."
                    if is_self_reference
                    else (
                        "The source note was authored for the complete target "
                        "range, whose exact component Arabic is supplied. This "
                        "connection exposes one component for discovery. Assign "
                        "only features actually present in that component to it; "
                        "keep sequence-level claims at range scope."
                        if is_range_target
                        else
                        "Use this row to discover and assess the stated relation. "
                        "The exact target Arabic is supplied, but target morphology "
                        "and lexical analysis are not. Do not invent those missing "
                        "details. Opposite-direction nominations and counterevidence "
                        "remain visible, but neither is a focus-direction verdict."
                    )
                ),
            },
        }
        connection_registry.append(connection)

    if lane in {"macro", "global"}:
        authored_targets = {
            item["target_ref"]
            for item in connection_registry
        }
        for origin_ref, evidence_rows in reciprocal_evidence_with_ranges.items():
            origin_surah = origin_ref.split(":", 1)[0]
            if origin_ref == focus_ref:
                owning_lane = "macro"
                relation_scope = "self_reference_reciprocal_evidence"
            elif origin_ref in pericope_refs:
                owning_lane = "macro"
                relation_scope = "declared_pericope_reciprocal_evidence"
            else:
                owning_lane = "global"
                relation_scope = (
                    "inter_surah_reciprocal_evidence"
                    if origin_surah != focus_surah
                    else "same_surah_beyond_pericope_reciprocal_evidence"
                )
            if lane != owning_lane or origin_ref in authored_targets:
                continue
            evidence_hashes = [
                item["projection_record_sha256"] for item in evidence_rows
            ]
            has_nomination = any(
                item.get("record_type") == "reciprocal_nomination"
                for item in evidence_rows
            )
            has_counterevidence = any(
                item.get("record_type") == "reciprocal_counterevidence"
                for item in evidence_rows
            )
            has_ranked_review = any(
                item.get("source_row_role") == "ranked_review"
                for item in evidence_rows
            )
            has_missing_ayah_suggestion = any(
                item.get("source_row_role") == "missing_ayah_suggestion"
                for item in evidence_rows
            )
            derived_origin = (
                "derived_reciprocal_seed"
                if has_nomination
                else "derived_reciprocal_counterevidence"
            )
            connection_ref = "conn_" + _sha256_json(
                {
                    "focus_ref": focus_ref,
                    "target_ref": origin_ref,
                    "origin": derived_origin,
                    "projection_record_sha256": evidence_hashes,
                }
            )[:20]
            tagged_evidence_rows = [
                {
                    **item,
                    "connection_evidence_ref": _connection_evidence_ref(
                        connection_ref, "target_to_focus", item
                    ),
                }
                for item in evidence_rows
            ]
            boundary = (
                "At least one source-direction review meaningfully linked this "
                "target back to the focus ayah. Treat its note and label only "
                "as a discovery nomination. Reassess the relation from the "
                "focus ayah using the supplied exact target Arabic; do not "
                "invent missing target morphology or inherit the source label."
                if has_nomination
                else
                "The target's source-direction review recorded only `no value` "
                "or `reject` links back to the focus ayah. Keep that negative "
                "evidence visible as possible asymmetry or a failed edge, but "
                "do not let it veto a focus-direction reading without fresh "
                "assessment from the supplied exact target Arabic."
            )
            connection_registry.append(
                {
                    "connection_ref": connection_ref,
                    "target_ref": origin_ref,
                    "relation_scope": relation_scope,
                    "origin": derived_origin,
                    "prior_label": None,
                    "note": None,
                    "source_pointer": None,
                    "source_pointers": [
                        item["source_pointer"] for item in evidence_rows
                    ],
                    "projection_pointers": [
                        item["projection_pointer"] for item in evidence_rows
                    ],
                    "target_evidence": target_evidence(origin_ref),
                    "reciprocal_evidence": tagged_evidence_rows,
                    "qualification": {
                        "derived_reciprocal_seed": has_nomination,
                        "derived_reciprocal_counterevidence": (
                            not has_nomination and has_counterevidence
                        ),
                        "has_reciprocal_nomination": has_nomination,
                        "has_reciprocal_counterevidence": has_counterevidence,
                        "has_ranked_review_source_row": has_ranked_review,
                        "has_missing_ayah_suggestion_source_row": (
                            has_missing_ayah_suggestion
                        ),
                        "source_row_roles_are_provenance_not_decisions": True,
                        "source_direction_labels_are_not_focus_decisions": True,
                        "receiving_direction_requires_fresh_assessment": True,
                        "target_ayah_text_supplied": True,
                        "target_morphology_supplied": False,
                        "boundary": boundary,
                    },
                }
            )
    connection_refs = [item["connection_ref"] for item in connection_registry]
    if len(connection_refs) != len(set(connection_refs)):
        raise SystemExit(f"Duplicate {lane} connection references")

    publication = source_bundle.get("v12_cross_run_publication")
    primary_floor = (
        publication.get("baseline") if isinstance(publication, dict) else None
    )
    hft_anchor_refs = sorted(
        {
            anchor_ref
            for record in assigned_hft
            for anchor_ref in record.get("anchor_refs", [])
        }
    )
    supplied_hft_anchor_refs = sorted(
        {
            evidence["ayah_ref"]
            for support in hft_supports
            for evidence in support.get("anchor_evidence", [])
        }
    )
    missing_hft_anchor_refs = sorted(
        set(hft_anchor_refs) - set(supplied_hft_anchor_refs)
    )
    packet: dict[str, Any] = {
        "schema_version": "commentary-v3-lane-evidence-packet-v2",
        "identity": {
            "ayah_ref": docket["identity"]["ayah_ref"],
            "lane": lane,
            "source_canonical_sha256": docket["identity"][
                "source_canonical_sha256"
            ],
            "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
        },
        "focus": docket["focus"],
        "primary_floor": primary_floor,
        "focus_surface_evidence": _focus_surface_evidence(docket),
        "scope": {
            "pericope": docket["scope"]["pericope"],
            "lane_contract": docket["scope"]["lane_contract"].get(lane),
            "hft": {
                "authoring_status": "visible_with_provenance_qualification",
                "assigned_record_count": len(assigned_hft),
                "authoring_policy": hft_projection.get("policy"),
            },
            "readiness": {
                "docket_ready": docket["adjudication_gate"].get("ready"),
                "docket_mode": docket["adjudication_gate"].get("mode"),
                "authoring_effect": (
                    "Docket readiness is reported for source provenance. HFT "
                    "visibility is governed by the authoring policy above."
                ),
            },
        },
        "candidate_inventory": candidates,
        "support_registry": supports,
        "branch_registry": branches,
        "connection_registry": connection_registry,
        "hft_evidence": {
            "policy": hft_projection.get("policy"),
            "source_present": hft_projection.get("source_present"),
            "packet_summary": hft_projection.get("packet_summary"),
            "provenance": hft_projection.get("provenance"),
            "lane_counts": hft_projection.get("lane_counts", {}),
            "structured_insight_count": hft_projection.get(
                "structured_insight_count", 0
            ),
            "reader_synthesis_count": hft_projection.get(
                "reader_synthesis_count", 0
            ),
            "unstructured_record_count": hft_projection.get(
                "unstructured_record_count", 0
            ),
            "assigned_record_count": len(assigned_hft),
            "assigned_records": [
                {
                    key: value
                    for key, value in record.items()
                    if key != "raw_item"
                }
                for record in assigned_hft
            ],
            "diagnostics": hft_projection.get("diagnostics", []),
            "anchor_evidence_coverage": {
                "cited_unique_anchor_count": len(hft_anchor_refs),
                "supplied_unique_anchor_count": len(supplied_hft_anchor_refs),
                "missing_anchor_refs": missing_hft_anchor_refs,
            },
            "payload_location": (
                "Each assigned record's exact raw payload and exact available "
                "anchor Arabic are in support_registry under its support_id."
            ),
        },
        "source_coverage": {
            "docket": docket["coverage"],
            "lane_candidate_count": len(candidates),
            "lane_support_count": len(supports),
            "lane_branch_count": len(branches),
            "assigned_hft_record_count": len(assigned_hft),
            "total_hft_record_count": len(hft_projection.get("records", [])),
            "hft_anchor_evidence_count": len(supplied_hft_anchor_refs),
            "missing_hft_anchor_refs": missing_hft_anchor_refs,
            "connection_count": len(connection_registry),
            "connection_evidence_row_count": sum(
                (1 if item.get("connection_evidence_ref") else 0)
                + len(item.get("reciprocal_evidence", []))
                for item in connection_registry
            ),
            "authored_connection_count": sum(
                item["origin"] == "authored_focus_row"
                for item in connection_registry
            ),
            "derived_reciprocal_seed_count": sum(
                item["origin"] == "derived_reciprocal_seed"
                for item in connection_registry
            ),
            "derived_reciprocal_counterevidence_count": sum(
                item["origin"] == "derived_reciprocal_counterevidence"
                for item in connection_registry
            ),
            "authored_connections_with_reciprocal_evidence": sum(
                item["origin"] == "authored_focus_row"
                and bool(item["reciprocal_evidence"])
                for item in connection_registry
            ),
            "connection_scopes": {
                scope: sum(
                    item["relation_scope"] == scope
                    for item in connection_registry
                )
                for scope in sorted(
                    {item["relation_scope"] for item in connection_registry}
                )
            },
            "inter_ayah_source": inter_ayah_source_coverage,
            "quran_text_source": quran_text_coverage,
            "unresolved_branch_refs": unresolved_branch_refs,
            "source_types": sorted(
                {
                    candidate.get("source_type")
                    for candidate in candidates
                    if candidate.get("source_type")
                }
            ),
        },
        "contract": {
            "previous_model_decisions_are_not_supplied": True,
            "upstream_transport_decision_fields_are_omitted": True,
            "every_candidate_requires_one_decision": True,
            "new_grounded_findings_are_allowed": True,
            "noncanonical_findings_are_allowed": True,
            "uncertainty_changes_label_not_visibility": True,
            "hft_provenance_changes_qualification_not_visibility": True,
            "every_assigned_hft_record_is_exactly_one_candidate": True,
            "accepted_hft_candidates_must_retain_their_support_and_boundary": True,
            "unresolved_hft_branch_citations_do_not_erase_the_record": True,
            "branch_ids_do_not_count_as_semantic_coverage": True,
            "distinctive_branch_facets_must_be_explained": True,
            "accepted_branch_contributions_bind_one_tested_facet": True,
            "failed_edges_remain_in_coverage_ledgers_without_contact_refs": True,
            "prior_connection_labels_are_not_decisions": True,
            "reciprocal_source_labels_are_not_focus_direction_decisions": True,
            "reciprocal_counterevidence_is_visible_but_not_a_veto": True,
            "every_connection_evidence_row_requires_independent_review": (
                lane in {"macro", "global"}
            ),
            "connections_require_explicit_review": lane in {"macro", "global"},
            "conflict_is_not_a_rejection_reason": True,
            "prose_length_is_not_a_decision_criterion": True,
            "recoverable_source_provenance_is_omitted_from_agent_transport": (
                True
            ),
        },
    }
    packet = _strip_recoverable_transport_provenance(packet)
    packet["identity"]["lane_packet_sha256"] = (
        _payload_hash_with_identity_field_removed(packet, "lane_packet_sha256")
    )
    return packet


def _prompt_manifest(
    *,
    stage: str,
    ayah_ref: str,
    prompt: str,
    expected_response: Path | None,
    inputs: dict[str, Any],
    authoring_request_sha256: str,
    expected_outputs: dict[str, Path] | None = None,
) -> dict[str, Any]:
    prompt_payload = prompt.encode("utf-8")
    return {
        "schema_version": "commentary-v3-authoring-prompt-manifest-v1",
        "stage": stage,
        "ayah_ref": ayah_ref,
        "prompt_sha256": _sha256_bytes(prompt_payload),
        "prompt_bytes": len(prompt_payload),
        "authoring_request_sha256": authoring_request_sha256,
        "expected_response": (
            _manifest_path(expected_response) if expected_response else None
        ),
        "expected_outputs": (
            {key: _manifest_path(path) for key, path in expected_outputs.items()}
            if expected_outputs
            else None
        ),
        "inputs": inputs,
    }


def _render_scopes(args: argparse.Namespace) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    docket_path = args.docket or _default_docket(args.ayah)
    source_path = args.source_bundle or _default_source_bundle(args.ayah)
    docket = _load_object(docket_path)
    source_bundle = _load_object(source_path)
    try:
        validate_docket(docket)
    except ValidationError as exc:
        raise SystemExit(f"Invalid authoring docket {docket_path}: {exc}") from exc
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise SystemExit("Docket ayah identity does not match --ayah")
    if source_bundle.get("ayahRef") != args.ayah:
        raise SystemExit("Source bundle ayah identity does not match --ayah")
    if (
        _sha256_json(source_bundle)
        != docket.get("identity", {}).get("source_canonical_sha256")
    ):
        raise SystemExit("Source bundle canonical hash does not match docket")
    quran_text_evidence, quran_text_coverage = _quran_text_evidence(
        args.quran_text
    )
    numbered_refs = {
        ref
        for ref in quran_text_evidence
        if ref.split(":", 1)[1] != "0"
    }
    (
        inter_ayah_rows,
        reciprocal_evidence,
        inter_ayah_source_coverage,
    ) = _inter_ayah_evidence_with_fallback(
        args.ayah,
        args.inter_ayah_dir,
        args.inter_ayah_parent_dir,
        numbered_refs,
    )
    hft_projection = _hft_authoring_projection(docket, source_bundle)
    result: dict[str, Any] = {
        "ayah_ref": args.ayah,
        "inputs_root": str(layout.inputs),
        "outputs_root": str(layout.outputs),
        "inter_ayah_evidence": {
            "source_id": inter_ayah_source_coverage["source_id"],
            "operational_fallback_used": inter_ayah_source_coverage[
                "operational_fallback_used"
            ],
            "integrity_warnings": inter_ayah_source_coverage[
                "integrity_warnings"
            ],
        },
        "stages": {},
    }
    for lane in LANES:
        packet = _lane_packet(
            docket,
            lane,
            source_bundle,
            hft_projection,
            inter_ayah_rows,
            reciprocal_evidence,
            inter_ayah_source_coverage,
            quran_text_evidence,
            quran_text_coverage,
        )
        template = _read_prompt(f"scope-{lane}.md")
        template_sha256 = _sha256_bytes(template.encode("utf-8"))
        request_inputs = {
            "ayah_ref": args.ayah,
            "lane": lane,
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "template_sha256": template_sha256,
        }
        request_sha256 = _request_sha256(f"scope-{lane}-review", request_inputs)
        prompt = _render(
            template,
            {
                "@@AYAH_REF@@": args.ayah,
                "@@LANE_PACKET_SHA256@@": packet["identity"][
                    "lane_packet_sha256"
                ],
                "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
                "@@LANE_PACKET_JSON@@": _canonical_json(packet),
            },
            label=f"{lane} scope",
        )
        paths = _scope_review_paths(layout, lane, request_sha256)
        packet_path = paths["packet"]
        prompt_path = paths["prompt"]
        response_path = paths["response"]
        manifest_path = paths["manifest"]
        manifest = _prompt_manifest(
            stage=f"scope-{lane}-review",
            ayah_ref=args.ayah,
            prompt=prompt,
            expected_response=response_path,
            authoring_request_sha256=request_sha256,
            # Only functional prompt inputs belong in immutable stage content.
            # Source paths and raw formatting are provenance of the canonical
            # lane packet, not distinct authoring requests; the packet hash
            # already commits to every supplied semantic byte.
            inputs=request_inputs,
        )
        _write(V3_ROOT, packet_path, _canonical_json(packet) + "\n")
        _write(V3_ROOT, prompt_path, prompt)
        _write(V3_ROOT, manifest_path, _pretty_json(manifest))
        result["stages"][lane] = {
            "request_sha256": request_sha256,
            "packet": str(packet_path),
            "prompt": str(prompt_path),
            "manifest": str(manifest_path),
            "expected_response": str(response_path),
            "workspace": str(layout.workspace),
            "candidate_count": len(packet["candidate_inventory"]),
            "connection_count": len(packet["connection_registry"]),
            "assigned_hft_record_count": packet["hft_evidence"][
                "assigned_record_count"
            ],
        }
    return result


def _record_id_set(rows: Any, field: str, *, label: str) -> set[str]:
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise SystemExit(f"{label} must be a list of objects")
    values = [row.get(field) for row in rows]
    if any(not isinstance(value, str) or not value for value in values):
        raise SystemExit(f"{label} contains an invalid {field}")
    if len(set(values)) != len(values):
        raise SystemExit(f"{label} repeats {field}")
    return set(values)


def _string_list(value: Any, *, label: str, allow_empty: bool = True) -> list[str]:
    if (
        not isinstance(value, list)
        or any(not isinstance(item, str) or not item for item in value)
        or len(set(value)) != len(value)
        or (not allow_empty and not value)
    ):
        raise SystemExit(f"{label} must contain unique nonempty strings")
    return value


def _branch_facet_ids(branch: dict[str, Any]) -> set[str]:
    facets = branch.get("review_facets")
    if facets is None:
        # Historical packet support is intentionally read-only. New v2 packets
        # always carry review_facets, including an explicit empty list.
        semantic_detail = branch.get("semantic_detail")
        if not isinstance(semantic_detail, dict):
            return set()
        facets = semantic_detail.get("distinctive_facets", [])
        if not isinstance(facets, list):
            raise SystemExit("Branch distinctive_facets is malformed")
        return {
            facet["facet_id"]
            for facet in facets
            if isinstance(facet, dict)
            and isinstance(facet.get("facet_id"), str)
            and facet["facet_id"]
        }
    return _record_id_set(facets, "facet_id", label="branch review facets")


FACET_RESULTS = {"contact", "no_independent_trigger", "scope_referral"}
CONNECTION_RESULTS = ("accepted", "narrowed", "represented", "rejected")


def _connection_evidence_refs(connection: dict[str, Any], *, label: str) -> set[str]:
    refs: list[str] = []
    authored_ref = connection.get("connection_evidence_ref")
    if authored_ref is not None:
        if not isinstance(authored_ref, str) or not authored_ref:
            raise SystemExit(f"{label} has an invalid authored evidence ref")
        refs.append(authored_ref)
    reciprocal = connection.get("reciprocal_evidence", [])
    refs.extend(
        _record_id_set(
            reciprocal,
            "connection_evidence_ref",
            label=f"{label} reciprocal evidence",
        )
    )
    if not refs or len(refs) != len(set(refs)):
        raise SystemExit(f"{label} lacks unique connection evidence rows")
    return set(refs)


def _aggregate_connection_result(evidence_results: list[dict[str, Any]]) -> str:
    supplied = {row.get("result") for row in evidence_results}
    for result in CONNECTION_RESULTS:
        if result in supplied:
            return result
    raise SystemExit("Connection evidence rows have no valid aggregate result")


def _candidate_branch_refs(candidate: dict[str, Any], *, label: str) -> set[str]:
    return {
        branch_ref
        for field in (
            "branch_refs",
            "focus_branch_refs",
            "nominated_branch_refs",
            "unresolved_branch_refs",
        )
        for branch_ref in _string_list(
            candidate.get(field, []), label=f"{label} {field}"
        )
    }


def _coverage_finding_refs(
    row: dict[str, Any],
    accepted_refs: set[str],
    *,
    label: str,
    require: bool,
) -> list[str]:
    finding_refs = _string_list(
        row.get("finding_refs"), label=f"{label} finding_refs", allow_empty=not require
    )
    unknown = set(finding_refs) - accepted_refs
    if unknown:
        raise SystemExit(f"{label} cites unknown accepted findings: {sorted(unknown)}")
    if not require and finding_refs:
        raise SystemExit(f"{label} cannot cite findings for a negative disposition")
    return finding_refs


def _nonempty_aliased_text(
    row: dict[str, Any], names: tuple[str, ...], *, label: str
) -> str:
    values = [row.get(name) for name in names if row.get(name) is not None]
    if (
        not values
        or any(not isinstance(value, str) or not value.strip() for value in values)
        or len(set(values)) != 1
    ):
        raise SystemExit(
            f"{label} requires one consistent nonempty value across "
            f"{', '.join(names)}"
        )
    return values[0]


def _decision_finding_refs(decision: dict[str, Any], *, label: str) -> Any:
    primary = decision.get("accepted_finding_refs")
    descriptive = decision.get("related_accepted_finding_refs")
    if primary is not None and descriptive is not None and primary != descriptive:
        raise SystemExit(f"{label} carries conflicting finding-ref aliases")
    return primary if primary is not None else descriptive


def _tested_facets(row: dict[str, Any], *, label: str) -> Any:
    primary = row.get("tested_facets")
    descriptive = row.get("facets_tested")
    if primary is not None and descriptive is not None and primary != descriptive:
        raise SystemExit(f"{label} carries conflicting tested-facet aliases")
    return primary if primary is not None else descriptive


def _validate_scope_review(
    lane: str, packet: dict[str, Any], review: dict[str, Any]
) -> None:
    if packet.get("schema_version") != "commentary-v3-lane-evidence-packet-v2":
        raise SystemExit(f"{lane} lane packet does not use the v2 evidence contract")
    if review.get("schema_version") != "commentary-v3-scope-review-v2":
        raise SystemExit(f"{lane} review does not use the v2 scope contract")
    if review.get("coverage_complete") is not True:
        raise SystemExit(f"{lane} review does not attest complete coverage")

    candidate_ids = _record_id_set(
        packet.get("candidate_inventory"), "candidate_id", label=f"{lane} candidates"
    )
    decisions = review.get("candidate_decisions")
    decided_ids = _record_id_set(
        decisions, "candidate_id", label=f"{lane} candidate decisions"
    )
    if decided_ids != candidate_ids:
        raise SystemExit(
            f"{lane} candidate accounting mismatch; "
            f"missing={sorted(candidate_ids - decided_ids)}, "
            f"extra={sorted(decided_ids - candidate_ids)}"
        )

    accepted = review.get("accepted_findings")
    accepted_refs = _record_id_set(
        accepted, "finding_ref", label=f"{lane} accepted findings"
    )
    if any(not ref.startswith(f"{lane}:") for ref in accepted_refs):
        raise SystemExit(f"{lane} accepted finding refs must be lane-qualified")
    accepted_by_ref = {
        finding["finding_ref"]: finding for finding in accepted
    }
    packet_candidates_by_id = {
        candidate["candidate_id"]: candidate
        for candidate in packet.get("candidate_inventory", [])
    }
    support_ids = _record_id_set(
        packet.get("support_registry"), "support_id", label=f"{lane} supports"
    )
    branch_ids = _record_id_set(
        packet.get("branch_registry"), "branch_ref", label=f"{lane} branches"
    )
    branches_by_ref = {
        branch["branch_ref"]: branch
        for branch in packet.get("branch_registry", [])
    }
    branch_facets_by_ref = {
        branch_ref: _branch_facet_ids(branch)
        for branch_ref, branch in branches_by_ref.items()
    }
    connection_ids = _record_id_set(
        packet.get("connection_registry"),
        "connection_ref",
        label=f"{lane} connections",
    )
    decisions_by_id = {
        decision["candidate_id"]: decision for decision in decisions
    }
    selected_candidate_ids: set[str] = set()
    referral_origins: dict[str, tuple[str, dict[str, Any]]] = {}
    for candidate_id, decision in decisions_by_id.items():
        disposition = decision.get("decision")
        if disposition not in {"accept", "narrow", "reject", "scope_referral"}:
            raise SystemExit(f"{lane} candidate {candidate_id} has an invalid decision")
        if disposition == "reject":
            for field in ("reason", "failed_edge"):
                value = decision.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise SystemExit(
                        f"{lane} rejected candidate {candidate_id} requires a "
                        f"nonempty {field}"
                    )
        finding_refs = _string_list(
            _decision_finding_refs(
                decision, label=f"{lane} candidate {candidate_id}"
            ),
            label=f"{lane} candidate {candidate_id} accepted_finding_refs",
            allow_empty=disposition not in {"accept", "narrow"},
        )
        unknown = set(finding_refs) - accepted_refs
        if unknown:
            raise SystemExit(
                f"{lane} candidate {candidate_id} cites unknown accepted findings: "
                f"{sorted(unknown)}"
            )
        candidate_branch_refs = _candidate_branch_refs(
            packet_candidates_by_id[candidate_id],
            label=f"{lane} candidate {candidate_id}",
        )
        excluded_branch_refs = set(
            _string_list(
                decision.get("excluded_branch_refs"),
                label=f"{lane} candidate {candidate_id} excluded_branch_refs",
            )
        )
        unknown_exclusions = excluded_branch_refs - candidate_branch_refs
        if unknown_exclusions:
            raise SystemExit(
                f"{lane} candidate {candidate_id} excludes branches it never cited: "
                f"{sorted(unknown_exclusions)}"
            )
        exclusion_reasons = decision.get("branch_exclusion_reasons")
        reason_refs = _record_id_set(
            exclusion_reasons,
            "branch_ref",
            label=f"{lane} candidate {candidate_id} branch exclusion reasons",
        )
        if reason_refs != excluded_branch_refs:
            raise SystemExit(
                f"{lane} candidate {candidate_id} branch exclusions lack exact reasons"
            )
        if any(
            not isinstance(row.get("reason"), str) or not row["reason"].strip()
            for row in exclusion_reasons
        ):
            raise SystemExit(
                f"{lane} candidate {candidate_id} has an empty branch exclusion reason"
            )
        if disposition == "scope_referral":
            referral_origins[candidate_id] = ("candidate", decision)
        if disposition in {"accept", "narrow"}:
            selected_candidate_ids.add(candidate_id)
            for finding_ref in finding_refs:
                finding_candidate_ids = _string_list(
                    accepted_by_ref[finding_ref].get("candidate_ids"),
                    label=f"{lane} finding {finding_ref} candidate_ids",
                )
                if candidate_id not in finding_candidate_ids:
                    raise SystemExit(
                        f"{lane} finding {finding_ref} omits accepted candidate "
                        f"{candidate_id}"
                    )
            if packet_candidates_by_id[candidate_id].get("source_type") == "hft":
                cited_supports = {
                    support_id
                    for finding_ref in finding_refs
                    for support_id in _string_list(
                        accepted_by_ref[finding_ref].get("support_ids"),
                        label=f"{lane} finding {finding_ref} support_ids",
                    )
                }
                required_hft_supports = set(
                    _string_list(
                        packet_candidates_by_id[candidate_id].get("support_ids"),
                        label=f"{lane} HFT candidate {candidate_id} support_ids",
                        allow_empty=False,
                    )
                )
                if not required_hft_supports <= cited_supports:
                    raise SystemExit(
                        f"{lane} accepted HFT candidate {candidate_id} lost its "
                        "source support"
                    )
            retained_branch_refs = {
                branch_ref
                for finding_ref in finding_refs
                for branch_ref in _string_list(
                    accepted_by_ref[finding_ref].get("branch_refs"),
                    label=f"{lane} finding {finding_ref} branch_refs",
                )
            }
            unaccounted_branches = (
                candidate_branch_refs - retained_branch_refs - excluded_branch_refs
            )
            if unaccounted_branches:
                raise SystemExit(
                    f"{lane} accepted candidate {candidate_id} silently drops branches: "
                    f"{sorted(unaccounted_branches)}"
                )

    represented_candidates: set[str] = set()
    represented_proposals: set[str] = set()
    accepted_facet_uses: list[tuple[str, str, str]] = []
    for finding_ref, finding in accepted_by_ref.items():
        finding_candidates = _string_list(
            finding.get("candidate_ids"),
            label=f"{lane} finding {finding_ref} candidate_ids",
        )
        finding_proposals = _string_list(
            finding.get("proposal_keys"),
            label=f"{lane} finding {finding_ref} proposal_keys",
        )
        finding_supports = set(
            _string_list(
                finding.get("support_ids"),
                label=f"{lane} finding {finding_ref} support_ids",
            )
        )
        finding_branches = set(
            _string_list(
                finding.get("branch_refs"),
                label=f"{lane} finding {finding_ref} branch_refs",
            )
        )
        finding_connections = set(
            _string_list(
                finding.get("connection_refs"),
                label=f"{lane} finding {finding_ref} connection_refs",
            )
        )
        if finding_supports - support_ids:
            raise SystemExit(
                f"{lane} finding {finding_ref} cites unknown supports: "
                f"{sorted(finding_supports - support_ids)}"
            )
        if finding_branches - branch_ids:
            raise SystemExit(
                f"{lane} finding {finding_ref} cites unknown branches: "
                f"{sorted(finding_branches - branch_ids)}"
            )
        if finding_connections - connection_ids:
            raise SystemExit(
                f"{lane} finding {finding_ref} cites unknown connections: "
                f"{sorted(finding_connections - connection_ids)}"
            )
        branch_contributions = finding.get("branch_contributions")
        if not isinstance(branch_contributions, list) or any(
            not isinstance(item, dict) for item in branch_contributions
        ):
            raise SystemExit(
                f"{lane} finding {finding_ref} has malformed branch contributions"
            )
        contribution_branch_refs: set[str] = set()
        contribution_identities: set[tuple[str, ...]] = set()
        for contribution in branch_contributions:
            contribution_ref = contribution.get("branch_ref")
            if not isinstance(contribution_ref, str) or not contribution_ref.strip():
                raise SystemExit(
                    f"{lane} finding {finding_ref} has a branch contribution "
                    "without a branch_ref"
                )
            facet_id = contribution.get("facet_id")
            if not isinstance(facet_id, str) or not facet_id:
                raise SystemExit(
                    f"{lane} finding {finding_ref} contribution for "
                    f"{contribution_ref} lacks one facet_id"
                )
            if facet_id not in branch_facets_by_ref.get(contribution_ref, set()):
                raise SystemExit(
                    f"{lane} finding {finding_ref} contribution cites unknown facet "
                    f"{contribution_ref}:{facet_id}"
                )
            accepted_facet_uses.append((finding_ref, contribution_ref, facet_id))
            contribution_branch_refs.add(contribution_ref)
            facet = _nonempty_aliased_text(
                contribution,
                ("distinctive_facet",),
                label=f"{lane} contribution {finding_ref}:{contribution_ref} facet",
            )
            carrier = _nonempty_aliased_text(
                contribution,
                ("surface_carrier", "carrier"),
                label=f"{lane} contribution {finding_ref}:{contribution_ref} carrier",
            )
            anchor = _nonempty_aliased_text(
                contribution,
                ("independent_anchor",),
                label=f"{lane} contribution {finding_ref}:{contribution_ref} anchor",
            )
            effect = _nonempty_aliased_text(
                contribution,
                ("contribution", "actual_contribution"),
                label=f"{lane} contribution {finding_ref}:{contribution_ref} effect",
            )
            boundary = _nonempty_aliased_text(
                contribution,
                ("boundary",),
                label=f"{lane} contribution {finding_ref}:{contribution_ref} boundary",
            )
            identity = (
                contribution_ref,
                facet_id,
                facet,
                carrier,
                anchor,
                effect,
                boundary,
            )
            if identity in contribution_identities:
                raise SystemExit(
                    f"{lane} finding {finding_ref} repeats a branch contribution"
                )
            contribution_identities.add(identity)
        if contribution_branch_refs != finding_branches:
            raise SystemExit(
                f"{lane} finding {finding_ref} lacks exact branch-contribution "
                "coverage"
            )
        unknown_candidates = set(finding_candidates) - candidate_ids
        if unknown_candidates:
            raise SystemExit(
                f"{lane} finding {finding_ref} cites unknown candidates: "
                f"{sorted(unknown_candidates)}"
            )
        nonselected = {
            candidate_id
            for candidate_id in finding_candidates
            if decisions_by_id[candidate_id].get("decision")
            not in {"accept", "narrow"}
        }
        if nonselected:
            raise SystemExit(
                f"{lane} finding {finding_ref} carries nonselected candidates: "
                f"{sorted(nonselected)}"
            )
        represented_candidates.update(finding_candidates)
        represented_proposals.update(finding_proposals)
    if represented_candidates != selected_candidate_ids:
        raise SystemExit(
            f"{lane} accepted-finding candidate coverage mismatch; "
            f"missing={sorted(selected_candidate_ids - represented_candidates)}, "
            f"extra={sorted(represented_candidates - selected_candidate_ids)}"
        )

    for candidate_id, decision in decisions_by_id.items():
        if decision.get("decision") != "reject" or decision.get("duplicate_of") is None:
            continue
        duplicate_of = decision.get("duplicate_of")
        if not isinstance(duplicate_of, str) or duplicate_of not in accepted_by_ref:
            raise SystemExit(
                f"{lane} duplicate rejection {candidate_id} has no accepted target"
            )
        candidate = packet_candidates_by_id[candidate_id]
        target = accepted_by_ref[duplicate_of]
        evidence_pairs = (
            (
                set(
                    _string_list(
                        candidate.get("support_ids"),
                        label=f"{lane} candidate {candidate_id} support_ids",
                    )
                ),
                set(
                    _string_list(
                        target.get("support_ids"),
                        label=f"{lane} finding {duplicate_of} support_ids",
                    )
                ),
                "support_ids",
            ),
            (
                _candidate_branch_refs(
                    candidate, label=f"{lane} candidate {candidate_id}"
                ),
                set(
                    _string_list(
                        target.get("branch_refs"),
                        label=f"{lane} finding {duplicate_of} branch_refs",
                    )
                ),
                "branch_refs",
            ),
        )
        for required, retained, field in evidence_pairs:
            if not required <= retained:
                raise SystemExit(
                    f"{lane} duplicate target {duplicate_of} loses {candidate_id} "
                    f"{field}: {sorted(required - retained)}"
                )

    new_findings = review.get("new_findings")
    proposal_keys = _record_id_set(
        new_findings, "proposal_key", label=f"{lane} new findings"
    )
    if any(not ref.startswith(f"{lane}:") for ref in proposal_keys):
        raise SystemExit(f"{lane} proposal keys must be lane-qualified")
    mapped_new_refs: set[str] = set()
    for item in new_findings:
        finding_ref = item.get("accepted_finding_ref")
        if not isinstance(finding_ref, str) or finding_ref not in accepted_refs:
            raise SystemExit(f"{lane} new finding maps to an unknown accepted finding")
        if item["proposal_key"] not in _string_list(
            accepted_by_ref[finding_ref].get("proposal_keys"),
            label=f"{lane} finding {finding_ref} proposal_keys",
        ):
            raise SystemExit(
                f"{lane} accepted finding {finding_ref} omits proposal "
                f"{item['proposal_key']}"
            )
        mapped_new_refs.add(finding_ref)
    if represented_proposals != proposal_keys:
        raise SystemExit(
            f"{lane} accepted-finding proposal coverage mismatch; "
            f"missing={sorted(proposal_keys - represented_proposals)}, "
            f"extra={sorted(represented_proposals - proposal_keys)}"
        )
    for finding_ref, finding in accepted_by_ref.items():
        if not finding.get("candidate_ids") and finding_ref not in mapped_new_refs:
            raise SystemExit(
                f"{lane} accepted finding {finding_ref} is neither candidate-backed "
                "nor registered as new"
            )

    contacts = review.get("contact_opportunities")
    contact_refs = _record_id_set(
        contacts,
        "contact_ref",
        label=f"{lane} contact opportunities",
    )
    if any(not ref.startswith(f"{lane}:") for ref in contact_refs):
        raise SystemExit(f"{lane} contact refs must be lane-qualified")
    contacts_by_ref = {contact["contact_ref"]: contact for contact in contacts}
    contact_semantic_fields = {
        "micro": (
            "surface_carrier",
            "distinctive_facet",
            "independent_trigger",
            "changed_reading",
            "reader_payoff",
            "containment",
        ),
        "macro": (
            "focus_carrier",
            "context_anchor",
            "distinctive_facet",
            "local_before",
            "context_after",
            "mechanism",
            "reader_payoff",
            "containment",
        ),
        "global": (
            "focus_carrier",
            "wider_trigger",
            "relation",
            "isolated_before",
            "wider_after",
            "reader_payoff",
            "containment",
        ),
    }[lane]
    for contact in contacts:
        contact_ref = contact["contact_ref"]
        disposition = contact.get("disposition")
        if disposition not in {
            "accept",
            "narrow",
            "represented",
            "scope_referral",
        }:
            raise SystemExit(f"{lane} contact {contact_ref} has an invalid disposition")
        for field in contact_semantic_fields:
            value = contact.get(field)
            if not isinstance(value, str) or not value.strip():
                raise SystemExit(
                    f"{lane} contact {contact_ref} requires a nonempty {field}"
                )
        finding_refs = _coverage_finding_refs(
            contact,
            accepted_refs,
            label=f"{lane} contact {contact_ref}",
            require=disposition in {"accept", "narrow", "represented"},
        )
        for finding_ref in finding_refs:
            if contact_ref not in _string_list(
                accepted_by_ref[finding_ref].get("contact_refs"),
                label=f"{lane} finding {finding_ref} contact_refs",
            ):
                raise SystemExit(
                    f"{lane} finding {finding_ref} does not retain contact {contact_ref}"
                )
        if finding_refs:
            for field in ("support_ids", "branch_refs", "connection_refs"):
                contact_evidence = set(
                    _string_list(
                        contact.get(field, []),
                        label=f"{lane} contact {contact_ref} {field}",
                    )
                )
                finding_evidence = {
                    evidence_ref
                    for finding_ref in finding_refs
                    for evidence_ref in _string_list(
                        accepted_by_ref[finding_ref].get(field),
                        label=f"{lane} finding {finding_ref} {field}",
                    )
                }
                if not contact_evidence <= finding_evidence:
                    raise SystemExit(
                        f"{lane} accepted findings lose contact {contact_ref} "
                        f"{field}: {sorted(contact_evidence - finding_evidence)}"
                    )
        for field, supplied in (
            ("support_ids", support_ids),
            ("branch_refs", branch_ids),
            ("connection_refs", connection_ids),
        ):
            cited = set(
                _string_list(
                    contact.get(field, []),
                    label=f"{lane} contact {contact_ref} {field}",
                )
            )
            if cited - supplied:
                raise SystemExit(
                    f"{lane} contact {contact_ref} cites unknown {field}: "
                    f"{sorted(cited - supplied)}"
                )
        if disposition == "scope_referral":
            referral_origins[contact_ref] = ("contact", contact)

    for finding_ref, finding in accepted_by_ref.items():
        finding_contacts = set(
            _string_list(
                finding.get("contact_refs"),
                label=f"{lane} finding {finding_ref} contact_refs",
            )
        )
        if finding_contacts - contact_refs:
            raise SystemExit(
                f"{lane} finding {finding_ref} cites unknown contacts: "
                f"{sorted(finding_contacts - contact_refs)}"
            )

    for item in new_findings:
        finding_ref = item["accepted_finding_ref"]
        originating_contacts = set(
            _string_list(
                item.get("contact_refs"),
                label=f"{lane} proposal {item['proposal_key']} contact_refs",
                allow_empty=lane == "micro",
            )
        )
        if originating_contacts - contact_refs:
            raise SystemExit(
                f"{lane} proposal {item['proposal_key']} cites unknown contacts: "
                f"{sorted(originating_contacts - contact_refs)}"
            )
        retained_contacts = set(
            _string_list(
                accepted_by_ref[finding_ref].get("contact_refs"),
                label=f"{lane} finding {finding_ref} contact_refs",
            )
        )
        if not originating_contacts <= retained_contacts:
            raise SystemExit(
                f"{lane} new finding {finding_ref} loses its originating contacts"
            )

    referrals = review.get("scope_referrals")
    referral_refs = _record_id_set(
        referrals,
        "referral_ref",
        label=f"{lane} scope referrals",
    )
    if any(not ref.startswith(f"{lane}:") for ref in referral_refs):
        raise SystemExit(f"{lane} referral refs must be lane-qualified")

    tested_facet_results_by_branch: dict[str, dict[str, str]] = {}
    if lane == "micro":
        expected_surface = {
            row.get("analysis_record_ref")
            for row in packet.get("focus_surface_evidence", {}).get("word_rows", [])
        }
        actual_surface = _record_id_set(
            review.get("surface_coverage"),
            "analysis_record_ref",
            label="micro surface coverage",
        )
        if actual_surface != expected_surface:
            raise SystemExit("Micro surface coverage is not exact")
        for row in review.get("surface_coverage", []):
            treatment = row.get("treatment")
            if treatment not in {"develop", "integrate", "transparent"}:
                raise SystemExit(
                    f"Micro surface row {row['analysis_record_ref']} has an invalid treatment"
                )
            _coverage_finding_refs(
                row,
                accepted_refs,
                label=f"micro surface row {row['analysis_record_ref']}",
                require=treatment in {"develop", "integrate"},
            )
        expected_branches = {
            branch.get("branch_ref")
            for branch in packet.get("branch_registry", [])
            if branch.get("registry") == "focus"
        }
        actual_branches = _record_id_set(
            review.get("branch_screen"),
            "branch_ref",
            label="micro branch screen",
        )
        if actual_branches != expected_branches:
            raise SystemExit("Micro branch coverage is not exact")
        branches_by_ref = {
            branch["branch_ref"]: branch
            for branch in packet.get("branch_registry", [])
            if branch.get("registry") == "focus"
        }
        accepted_branch_refs = {
            branch_ref
            for finding in accepted
            for branch_ref in _string_list(
                finding.get("branch_refs"),
                label=f"micro finding {finding['finding_ref']} branch_refs",
            )
        }
        for row in review.get("branch_screen", []):
            branch_ref = row["branch_ref"]
            result = row.get("result")
            if result not in {
                "nominated",
                "no_independent_trigger",
                "scope_referral",
            }:
                raise SystemExit(f"Micro branch row {branch_ref} has an invalid result")
            row_contact_refs = set(
                _string_list(
                    row.get("contact_refs"),
                    label=f"micro branch row {branch_ref} contact_refs",
                )
            )
            if row_contact_refs - contact_refs:
                raise SystemExit(
                    f"Micro branch row {branch_ref} cites unknown contacts: "
                    f"{sorted(row_contact_refs - contact_refs)}"
                )
            if branch_ref in accepted_branch_refs and result != "nominated":
                raise SystemExit(
                    f"Micro accepted branch {branch_ref} lacks a nominated screen result"
                )
            linked_terminal_contact = any(
                contacts_by_ref[contact_ref].get("disposition")
                in {"accept", "narrow", "represented", "scope_referral"}
                and branch_ref
                in _string_list(
                    contacts_by_ref[contact_ref].get("branch_refs", []),
                    label=f"micro contact {contact_ref} branch_refs",
                )
                for contact_ref in row_contact_refs
            )
            if (
                result == "nominated"
                and branch_ref not in accepted_branch_refs
                and not linked_terminal_contact
            ):
                raise SystemExit(
                    f"Micro nominated branch {branch_ref} has no accepted or "
                    "referred landing"
                )
            if result == "scope_referral":
                referral_origins[branch_ref] = ("branch", row)
            supplied_facets = _branch_facet_ids(branches_by_ref[row["branch_ref"]])
            if not supplied_facets:
                continue
            tested = _tested_facets(
                row, label=f"micro branch row {row['branch_ref']}"
            )
            tested_ids = _record_id_set(
                tested,
                "facet_id",
                label=f"micro tested facets {row['branch_ref']}",
            )
            if tested_ids != supplied_facets:
                raise SystemExit(
                    f"Micro facet coverage is incomplete for {row['branch_ref']}"
                )
            if any(
                facet.get("result") not in FACET_RESULTS
                for facet in tested
            ):
                raise SystemExit(
                    f"Micro facet results are invalid for {row['branch_ref']}"
                )
            tested_facet_results_by_branch[branch_ref] = {
                facet["facet_id"]: facet["result"] for facet in tested
            }
    else:
        expected_connections = _record_id_set(
            packet.get("connection_registry"),
            "connection_ref",
            label=f"{lane} connections",
        )
        actual_connections = _record_id_set(
            review.get("connection_coverage"),
            "connection_ref",
            label=f"{lane} connection coverage",
        )
        if actual_connections != expected_connections:
            raise SystemExit(f"{lane} connection coverage is not exact")
        packet_connections_by_ref = {
            connection["connection_ref"]: connection
            for connection in packet.get("connection_registry", [])
        }
        for row in review.get("connection_coverage", []):
            connection_ref = row["connection_ref"]
            packet_connection = packet_connections_by_ref[connection_ref]
            if row.get("target_ref") != packet_connection.get("target_ref"):
                raise SystemExit(
                    f"{lane} connection {connection_ref} has a stale target_ref"
                )
            result = row.get("result")
            if result not in CONNECTION_RESULTS:
                raise SystemExit(
                    f"{lane} connection {connection_ref} has an invalid result"
                )
            reason = row.get("reason")
            if not isinstance(reason, str) or not reason.strip():
                raise SystemExit(
                    f"{lane} connection {connection_ref} requires a specific reason"
                )
            finding_refs = _coverage_finding_refs(
                row,
                accepted_refs,
                label=f"{lane} connection {connection_ref}",
                require=result in {"accepted", "narrowed", "represented"},
            )
            evidence_results = row.get("evidence_row_results")
            actual_evidence_refs = _record_id_set(
                evidence_results,
                "connection_evidence_ref",
                label=f"{lane} connection {connection_ref} evidence-row results",
            )
            expected_evidence_refs = _connection_evidence_refs(
                packet_connection,
                label=f"{lane} connection {connection_ref}",
            )
            if actual_evidence_refs != expected_evidence_refs:
                raise SystemExit(
                    f"{lane} connection {connection_ref} evidence-row coverage is "
                    "not exact"
                )
            evidence_finding_refs: set[str] = set()
            for evidence_result in evidence_results:
                evidence_ref = evidence_result["connection_evidence_ref"]
                row_result = evidence_result.get("result")
                if row_result not in CONNECTION_RESULTS:
                    raise SystemExit(
                        f"{lane} connection evidence {evidence_ref} has an invalid "
                        "result"
                    )
                row_reason = evidence_result.get("reason")
                if not isinstance(row_reason, str) or not row_reason.strip():
                    raise SystemExit(
                        f"{lane} connection evidence {evidence_ref} requires a "
                        "specific reason"
                    )
                evidence_finding_refs.update(
                    _coverage_finding_refs(
                        evidence_result,
                        accepted_refs,
                        label=f"{lane} connection evidence {evidence_ref}",
                        require=row_result
                        in {"accepted", "narrowed", "represented"},
                    )
                )
            derived_result = _aggregate_connection_result(evidence_results)
            if result != derived_result or set(finding_refs) != evidence_finding_refs:
                raise SystemExit(
                    f"{lane} connection {connection_ref} aggregate does not match "
                    "its evidence-row results"
                )
            for finding_ref in finding_refs:
                if connection_ref not in _string_list(
                    accepted_by_ref[finding_ref].get("connection_refs"),
                    label=f"{lane} finding {finding_ref} connection_refs",
                ):
                    raise SystemExit(
                        f"{lane} finding {finding_ref} does not retain connection "
                        f"{connection_ref}"
                    )

        branches_by_ref = {
            branch.get("branch_ref"): branch
            for branch in packet.get("branch_registry", [])
            if isinstance(branch, dict) and isinstance(branch.get("branch_ref"), str)
        }
        atlas_rows = review.get("atlas_facets_tested")
        atlas_refs = _record_id_set(
            atlas_rows, "branch_ref", label=f"{lane} atlas facet coverage"
        )
        unknown_atlas = atlas_refs - set(branches_by_ref)
        if unknown_atlas:
            raise SystemExit(
                f"{lane} atlas cites unknown branches: {sorted(unknown_atlas)}"
            )
        for row in atlas_rows:
            branch_ref = row["branch_ref"]
            result = row.get("result")
            if result not in {
                "nominated",
                "no_independent_trigger",
                "scope_referral",
            }:
                raise SystemExit(
                    f"{lane} atlas row {branch_ref} has an invalid result"
                )
            row_contact_refs = set(
                _string_list(
                    row.get("contact_refs"),
                    label=f"{lane} atlas row {branch_ref} contact_refs",
                )
            )
            if row_contact_refs - contact_refs:
                raise SystemExit(
                    f"{lane} atlas row {branch_ref} cites unknown contacts: "
                    f"{sorted(row_contact_refs - contact_refs)}"
                )
            if result == "scope_referral":
                referral_origins[branch_ref] = ("branch", row)
            supplied_facets = _branch_facet_ids(branches_by_ref[row["branch_ref"]])
            if not supplied_facets:
                continue
            tested = _tested_facets(
                row, label=f"{lane} atlas row {row['branch_ref']}"
            )
            tested_ids = _record_id_set(
                tested, "facet_id", label=f"{lane} tested facets {row['branch_ref']}"
            )
            if tested_ids != supplied_facets:
                raise SystemExit(
                    f"{lane} facet coverage is incomplete for {row['branch_ref']}"
                )
            if any(
                facet.get("result") not in FACET_RESULTS
                for facet in tested
            ):
                raise SystemExit(
                    f"{lane} facet results are invalid for {row['branch_ref']}"
                )
            tested_facet_results_by_branch[branch_ref] = {
                facet["facet_id"]: facet["result"] for facet in tested
            }
        accepted_branch_refs = {
            branch_ref
            for finding in accepted
            for branch_ref in _string_list(
                finding.get("branch_refs"),
                label=f"{lane} finding {finding['finding_ref']} branch_refs",
            )
        }
        candidate_cited_branch_refs = {
            branch_ref
            for candidate in packet.get("candidate_inventory", [])
            for branch_ref in _candidate_branch_refs(
                candidate,
                label=f"{lane} candidate {candidate.get('candidate_id')}",
            )
        }
        contact_cited_branch_refs = {
            branch_ref
            for contact in contacts
            for branch_ref in _string_list(
                contact.get("branch_refs", []),
                label=f"{lane} contact {contact['contact_ref']} branch_refs",
            )
        }
        required_atlas_refs = (
            candidate_cited_branch_refs
            | contact_cited_branch_refs
            | accepted_branch_refs
        )
        if not required_atlas_refs <= atlas_refs:
            raise SystemExit(
                f"{lane} atlas omits branches cited by candidates, contacts, or "
                f"accepted findings: {sorted(required_atlas_refs - atlas_refs)}"
            )
        atlas_by_ref = {row["branch_ref"]: row for row in atlas_rows}
        misclassified_accepted = sorted(
            branch_ref
            for branch_ref in accepted_branch_refs
            if atlas_by_ref[branch_ref].get("result") != "nominated"
        )
        if misclassified_accepted:
            raise SystemExit(
                f"{lane} accepted branches lack nominated atlas results: "
                f"{misclassified_accepted}"
            )
        for row in atlas_rows:
            if row.get("result") != "nominated":
                continue
            branch_ref = row["branch_ref"]
            if branch_ref in accepted_branch_refs:
                continue
            linked_terminal_contact = any(
                contacts_by_ref[contact_ref].get("disposition")
                in {"accept", "narrow", "represented", "scope_referral"}
                and branch_ref
                in _string_list(
                    contacts_by_ref[contact_ref].get("branch_refs", []),
                    label=f"{lane} contact {contact_ref} branch_refs",
                )
                for contact_ref in _string_list(
                    row.get("contact_refs"),
                    label=f"{lane} atlas row {branch_ref} contact_refs",
                )
            )
            if not linked_terminal_contact:
                raise SystemExit(
                    f"{lane} nominated branch {branch_ref} has no accepted or "
                    "referred landing"
                )

    for finding_ref, branch_ref, facet_id in accepted_facet_uses:
        if (
            tested_facet_results_by_branch.get(branch_ref, {}).get(facet_id)
            != "contact"
        ):
            raise SystemExit(
                f"{lane} finding {finding_ref} claims unactivated facet "
                f"{branch_ref}:{facet_id}"
            )

    if lane == "global":
        expected_supports = {
            support.get("support_id")
            for support in packet.get("support_registry", [])
            if support.get("source_type") != "hft"
        }
        actual_supports = _record_id_set(
            review.get("support_coverage"),
            "support_id",
            label="global support coverage",
        )
        if actual_supports != expected_supports:
            raise SystemExit("Global non-HFT support coverage is not exact")
        for row in review.get("support_coverage", []):
            support_id = row["support_id"]
            result = row.get("result")
            if result not in {"accepted", "narrowed", "represented", "rejected"}:
                raise SystemExit(f"Global support {support_id} has an invalid result")
            finding_refs = _coverage_finding_refs(
                row,
                accepted_refs,
                label=f"global support {support_id}",
                require=result in {"accepted", "narrowed", "represented"},
            )
            for finding_ref in finding_refs:
                if support_id not in _string_list(
                    accepted_by_ref[finding_ref].get("support_ids"),
                    label=f"global finding {finding_ref} support_ids",
                ):
                    raise SystemExit(
                        f"Global finding {finding_ref} does not retain support {support_id}"
                    )

    referral_origin_refs = _record_id_set(
        referrals, "origin_ref", label=f"{lane} scope referral origins"
    )
    known_referral_origins: dict[str, tuple[str, dict[str, Any]]] = {
        candidate_id: ("candidate", decision)
        for candidate_id, decision in decisions_by_id.items()
    }
    known_referral_origins.update(
        {
            contact_ref: ("contact", contact)
            for contact_ref, contact in contacts_by_ref.items()
        }
    )
    known_referral_origins.update(
        {
            branch["branch_ref"]: ("branch", branch)
            for branch in packet.get("branch_registry", [])
            if isinstance(branch, dict)
            and isinstance(branch.get("branch_ref"), str)
        }
    )
    known_referral_origins.update(referral_origins)
    missing_referrals = set(referral_origins) - referral_origin_refs
    unknown_referrals = referral_origin_refs - set(known_referral_origins)
    if missing_referrals or unknown_referrals:
        raise SystemExit(
            f"{lane} scope-referral origin accounting mismatch; "
            f"missing={sorted(missing_referrals)}, "
            f"unknown={sorted(unknown_referrals)}"
        )
    for referral in referrals:
        referral_ref = referral["referral_ref"]
        origin_ref = referral["origin_ref"]
        referred_lane = referral.get("referred_lane")
        if referred_lane not in set(LANES) - {lane}:
            raise SystemExit(
                f"{lane} referral {referral_ref} has an invalid receiving lane"
            )
        origin_kind, origin = known_referral_origins[origin_ref]
        required_evidence: dict[str, set[str]] = {
            "support_ids": set(),
            "branch_refs": set(),
            "connection_refs": set(),
            "contact_refs": set(),
        }
        if origin_kind == "candidate":
            candidate = packet_candidates_by_id[origin_ref]
            required_evidence["support_ids"] = set(
                _string_list(
                    candidate.get("support_ids"),
                    label=f"{lane} candidate {origin_ref} support_ids",
                )
            )
            required_evidence["branch_refs"] = _candidate_branch_refs(
                candidate, label=f"{lane} candidate {origin_ref}"
            )
        elif origin_kind == "branch":
            required_evidence["branch_refs"] = {origin_ref}
            required_evidence["contact_refs"] = set(
                _string_list(
                    origin.get("contact_refs"),
                    label=f"{lane} branch referral {origin_ref} contact_refs",
                )
            )
        else:
            required_evidence["contact_refs"] = {origin_ref}
            for field in ("support_ids", "branch_refs", "connection_refs"):
                required_evidence[field] = set(
                    _string_list(
                        origin.get(field, []),
                        label=f"{lane} contact referral {origin_ref} {field}",
                    )
                )

        supplied_by_field = {
            "support_ids": support_ids,
            "branch_refs": branch_ids,
            "connection_refs": connection_ids,
            "contact_refs": contact_refs,
        }
        for field, supplied in supplied_by_field.items():
            payload_refs = set(
                _string_list(
                    referral.get(field),
                    label=f"{lane} referral {referral_ref} {field}",
                )
            )
            if payload_refs - supplied:
                raise SystemExit(
                    f"{lane} referral {referral_ref} cites unknown {field}: "
                    f"{sorted(payload_refs - supplied)}"
                )
            missing_origin_evidence = required_evidence[field] - payload_refs
            if missing_origin_evidence:
                raise SystemExit(
                    f"{lane} referral {referral_ref} loses origin {field}: "
                    f"{sorted(missing_origin_evidence)}"
                )


_SCOPE_REVIEW_ROW_IDS = {
    "accepted_findings": "finding_ref",
    "atlas_facets_tested": "branch_ref",
    "branch_contributions": "branch_ref",
    "branch_exclusion_reasons": "branch_ref",
    "branch_screen": "branch_ref",
    "candidate_decisions": "candidate_id",
    "connection_coverage": "connection_ref",
    "contact_opportunities": "contact_ref",
    "evidence_row_results": "connection_evidence_ref",
    "facets_tested": "facet_id",
    "new_findings": "proposal_key",
    "scope_referrals": "referral_ref",
    "support_coverage": "support_id",
    "surface_coverage": "analysis_record_ref",
    "tested_facets": "facet_id",
}
_SCOPE_MERGEABLE_DUPLICATE_ROWS = set(_SCOPE_REVIEW_ROW_IDS) - {
    "branch_contributions",
    "facets_tested",
    "tested_facets",
}
_SCOPE_REVIEW_CONTROL_VALUES = {
    ("candidate_decisions", "decision"): {
        "accept",
        "narrow",
        "reject",
        "scope_referral",
    },
    ("contact_opportunities", "disposition"): {
        "accept",
        "narrow",
        "represented",
        "scope_referral",
    },
    ("surface_coverage", "treatment"): {
        "develop",
        "integrate",
        "transparent",
    },
    ("branch_screen", "result"): {
        "nominated",
        "no_independent_trigger",
        "scope_referral",
    },
    ("atlas_facets_tested", "result"): {
        "nominated",
        "no_independent_trigger",
        "scope_referral",
    },
    ("tested_facets", "result"): FACET_RESULTS,
    ("facets_tested", "result"): FACET_RESULTS,
    ("connection_coverage", "result"): {
        "accepted",
        "narrowed",
        "represented",
        "rejected",
    },
    ("evidence_row_results", "result"): {
        "accepted",
        "narrowed",
        "represented",
        "rejected",
    },
    ("support_coverage", "result"): {
        "accepted",
        "narrowed",
        "represented",
        "rejected",
    },
}
_SCOPE_REVIEW_CONTROL_FIELDS = {
    row_name: control_field
    for row_name, control_field in _SCOPE_REVIEW_CONTROL_VALUES
}


def _scope_record_rows(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list):
        return [row for row in value if isinstance(row, dict)]
    return []


def _scope_trusted_referral_origins(
    lane: str,
    packet: dict[str, Any],
    semantic_baseline: dict[str, Any],
) -> set[str]:
    """Return intrinsically stable origin values, independent of duplicate rows."""

    return {
        row.get("candidate_id")
        for row in packet.get("candidate_inventory", [])
        if isinstance(row, dict)
        and isinstance(row.get("candidate_id"), str)
        and row["candidate_id"]
    } | {
        row.get("branch_ref")
        for row in packet.get("branch_registry", [])
        if isinstance(row, dict)
        and isinstance(row.get("branch_ref"), str)
        and row["branch_ref"]
    } | {
        row.get("contact_ref")
        for row in _scope_record_rows(
            semantic_baseline.get("contact_opportunities")
        )
        if isinstance(row.get("contact_ref"), str)
        and row["contact_ref"].startswith(f"{lane}:")
    }


def _scope_exception_compatible_control(
    row_name: str, field: str, value: Any
) -> bool:
    """Whether a supplied control already satisfies a positive exception."""

    if row_name == "candidate_decisions" and field == "decision":
        return value in {"accept", "narrow"}
    if row_name in {"branch_screen", "atlas_facets_tested"} and field == "result":
        return value == "nominated"
    return False


def _scope_validation_exception_paths(
    lane: str,
    packet: dict[str, Any],
    semantic_baseline: dict[str, Any],
) -> set[str]:
    """Return exact row fields whose valid control value must be repaired."""

    exceptions: set[str] = set()
    positive_branch_refs: set[str] = set()
    baseline_findings = _scope_record_rows(
        semantic_baseline.get("accepted_findings")
    )
    for finding in baseline_findings:
        branch_refs = finding.get("branch_refs")
        if isinstance(branch_refs, str):
            branch_refs = [branch_refs]
        if isinstance(branch_refs, list):
            positive_branch_refs.update(
                branch_ref
                for branch_ref in branch_refs
                if isinstance(branch_ref, str) and branch_ref
            )
    packet_candidates_by_id = {
        row.get("candidate_id"): row
        for row in packet.get("candidate_inventory", [])
        if isinstance(row, dict) and isinstance(row.get("candidate_id"), str)
    }
    positive_candidate_ids: set[str] = set()
    for finding in baseline_findings:
        candidate_ids = finding.get("candidate_ids")
        if isinstance(candidate_ids, str):
            candidate_ids = [candidate_ids]
        if isinstance(candidate_ids, list):
            positive_candidate_ids.update(
                candidate_id
                for candidate_id in candidate_ids
                if isinstance(candidate_id, str)
                and candidate_id in packet_candidates_by_id
            )
    candidate_decisions = _scope_record_rows(
        semantic_baseline.get("candidate_decisions")
    )
    for finding in baseline_findings:
        contributions = finding.get("branch_contributions")
        if isinstance(contributions, dict):
            contributions = [contributions]
        if isinstance(contributions, list):
            positive_branch_refs.update(
                contribution["branch_ref"]
                for contribution in contributions
                if isinstance(contribution, dict)
                and isinstance(contribution.get("branch_ref"), str)
                and contribution["branch_ref"]
            )
    for decision in candidate_decisions:
        candidate_id = decision.get("candidate_id")
        if not isinstance(candidate_id, str):
            continue
        candidate = packet_candidates_by_id.get(candidate_id)
        if (
            candidate is None
            or decision.get("decision") not in {"accept", "narrow"}
        ):
            continue
        excluded_refs = decision.get("excluded_branch_refs")
        if not isinstance(excluded_refs, list):
            excluded_refs = []
        excluded = {
            branch_ref
            for branch_ref in excluded_refs
            if isinstance(branch_ref, str) and branch_ref
        }
        positive_branch_refs.update(
            _candidate_branch_refs(
                candidate, label=f"{lane} candidate {candidate_id}"
            )
            - excluded
        )
    for decision in candidate_decisions:
        candidate_id = decision.get("candidate_id")
        if (
            isinstance(candidate_id, str)
            and candidate_id in positive_candidate_ids
            and decision.get("decision") not in {"accept", "narrow"}
        ):
            exceptions.add(
                f"candidate_decisions[candidate_id={candidate_id}].decision"
            )
    for contact in _scope_record_rows(
        semantic_baseline.get("contact_opportunities")
    ):
        if contact.get("disposition") not in {
            "accept",
            "narrow",
            "represented",
        }:
            continue
        branch_refs = contact.get("branch_refs")
        if isinstance(branch_refs, str):
            branch_refs = [branch_refs]
        if isinstance(branch_refs, list):
            positive_branch_refs.update(
                branch_ref
                for branch_ref in branch_refs
                if isinstance(branch_ref, str) and branch_ref
            )
    result_section = "branch_screen" if lane == "micro" else "atlas_facets_tested"
    result_rows = _scope_record_rows(semantic_baseline.get(result_section))
    for row in result_rows:
        branch_ref = row.get("branch_ref")
        if (
            isinstance(branch_ref, str)
            and branch_ref in positive_branch_refs
            and row.get("result") != "nominated"
        ):
            exceptions.add(
                f"{result_section}[branch_ref={branch_ref}].result"
            )

    expected_ids: dict[str, tuple[str, set[str] | None, str | None]] = {
        "candidate_decisions": (
            "candidate_id",
            {
                row.get("candidate_id")
                for row in packet.get("candidate_inventory", [])
                if isinstance(row, dict)
                and isinstance(row.get("candidate_id"), str)
            },
            None,
        ),
        "accepted_findings": ("finding_ref", None, f"{lane}:"),
        "contact_opportunities": ("contact_ref", None, f"{lane}:"),
        "new_findings": ("proposal_key", None, f"{lane}:"),
        "scope_referrals": ("referral_ref", None, f"{lane}:"),
    }
    if lane == "micro":
        expected_ids.update(
            {
                "surface_coverage": (
                    "analysis_record_ref",
                    {
                        row.get("analysis_record_ref")
                        for row in packet.get("focus_surface_evidence", {}).get(
                            "word_rows", []
                        )
                        if isinstance(row, dict)
                        and isinstance(row.get("analysis_record_ref"), str)
                    },
                    None,
                ),
                "branch_screen": (
                    "branch_ref",
                    {
                        row.get("branch_ref")
                        for row in packet.get("branch_registry", [])
                        if isinstance(row, dict)
                        and row.get("registry") == "focus"
                        and isinstance(row.get("branch_ref"), str)
                    },
                    None,
                ),
            }
        )
    else:
        expected_ids.update(
            {
                "connection_coverage": (
                    "connection_ref",
                    {
                        row.get("connection_ref")
                        for row in packet.get("connection_registry", [])
                        if isinstance(row, dict)
                        and isinstance(row.get("connection_ref"), str)
                    },
                    None,
                ),
                "atlas_facets_tested": (
                    "branch_ref",
                    {
                        row.get("branch_ref")
                        for row in packet.get("branch_registry", [])
                        if isinstance(row, dict)
                        and isinstance(row.get("branch_ref"), str)
                    },
                    None,
                ),
            }
        )
    if lane == "global":
        expected_ids["support_coverage"] = (
            "support_id",
            {
                row.get("support_id")
                for row in packet.get("support_registry", [])
                if isinstance(row, dict)
                and row.get("source_type") != "hft"
                and isinstance(row.get("support_id"), str)
            },
            None,
        )
    for section, (id_field, expected, required_prefix) in expected_ids.items():
        rows = _scope_record_rows(semantic_baseline.get(section))
        values = [
            row.get(id_field)
            for row in rows
            if isinstance(row, dict)
            and isinstance(row.get(id_field), str)
            and row[id_field]
        ]
        repeated = {value for value in values if values.count(value) > 1}
        for row_id in set(values):
            if (
                row_id in repeated
                or (expected is not None and row_id not in expected)
                or (required_prefix is not None and not row_id.startswith(required_prefix))
            ):
                exceptions.add(f"{section}[{id_field}={row_id}].{id_field}")

    # Scope referrals are also a one-row-per-origin ledger. Preserve the first
    # stable row identity and permit only surplus rows for a repeated origin to
    # collapse losslessly into it.
    referrals_by_origin: dict[str, list[dict[str, Any]]] = {}
    referral_rows = _scope_record_rows(
        semantic_baseline.get("scope_referrals")
    )
    for row in referral_rows:
        origin_ref = row.get("origin_ref")
        if isinstance(origin_ref, str) and origin_ref:
            referrals_by_origin.setdefault(origin_ref, []).append(row)
    for rows in referrals_by_origin.values():
        for surplus in rows[1:]:
            referral_ref = surplus.get("referral_ref")
            if isinstance(referral_ref, str) and referral_ref:
                exceptions.add(
                    "scope_referrals"
                    f"[referral_ref={referral_ref}].referral_ref"
                )

    known_referral_origins = _scope_trusted_referral_origins(
        lane, packet, semantic_baseline
    )
    for row in _scope_record_rows(semantic_baseline.get("scope_referrals")):
        referral_ref = row.get("referral_ref")
        origin_ref = row.get("origin_ref")
        if (
            isinstance(referral_ref, str)
            and referral_ref
            and (
                not isinstance(origin_ref, str)
                or origin_ref not in known_referral_origins
            )
        ):
            exceptions.add(
                "scope_referrals"
                f"[referral_ref={referral_ref}].origin_ref"
            )
        referred_lane = row.get("referred_lane")
        if (
            isinstance(referral_ref, str)
            and referral_ref
            and (
                not isinstance(referred_lane, str)
                or referred_lane not in set(LANES) - {lane}
            )
        ):
            exceptions.add(
                "scope_referrals"
                f"[referral_ref={referral_ref}].referred_lane"
            )

    branch_facets = {
        row.get("branch_ref"): _branch_facet_ids(row)
        for row in packet.get("branch_registry", [])
        if isinstance(row, dict) and isinstance(row.get("branch_ref"), str)
    }
    facet_section = "branch_screen" if lane == "micro" else "atlas_facets_tested"
    for row in _scope_record_rows(semantic_baseline.get(facet_section)):
        branch_ref = row.get("branch_ref")
        if not isinstance(branch_ref, str) or not branch_ref:
            continue
        expected_facets = branch_facets.get(branch_ref, set())
        for alias in ("tested_facets", "facets_tested"):
            facets = row.get(alias)
            if isinstance(facets, dict):
                facets = [facets]
            if not isinstance(facets, list):
                continue
            facet_ids = [
                facet.get("facet_id")
                for facet in facets
                if isinstance(facet, dict)
                and isinstance(facet.get("facet_id"), str)
                and facet["facet_id"]
            ]
            repeated = {
                facet_id for facet_id in facet_ids if facet_ids.count(facet_id) > 1
            }
            for facet_id in set(facet_ids):
                if facet_id in repeated or facet_id not in expected_facets:
                    exceptions.add(
                        f"{facet_section}[branch_ref={branch_ref}]."
                        f"facet[facet_id={facet_id}].facet_id"
                    )

    packet_branch_ids = set(branch_facets)
    for finding in baseline_findings:
        finding_ref = finding.get("finding_ref")
        if not isinstance(finding_ref, str) or not finding_ref:
            continue
        contributions = finding.get("branch_contributions")
        if isinstance(contributions, dict):
            contributions = [contributions]
        if not isinstance(contributions, list):
            continue
        contribution_refs = [
            row.get("branch_ref")
            for row in contributions
            if isinstance(row, dict)
            and isinstance(row.get("branch_ref"), str)
            and row["branch_ref"]
        ]
        for branch_ref in set(contribution_refs):
            if branch_ref not in packet_branch_ids:
                exceptions.add(
                    f"accepted_findings[finding_ref={finding_ref}]."
                    f"branch_contributions[branch_ref={branch_ref}].branch_ref"
                )
        for contribution in contributions:
            if not isinstance(contribution, dict):
                continue
            branch_ref = contribution.get("branch_ref")
            facet_id = contribution.get("facet_id")
            if (
                isinstance(branch_ref, str)
                and branch_ref
                and isinstance(facet_id, str)
                and facet_id
                and facet_id not in branch_facets.get(branch_ref, set())
            ):
                exceptions.add(
                    f"accepted_findings[finding_ref={finding_ref}]."
                    f"branch_contributions[branch_ref={branch_ref}].facet_id"
                )

    if lane in {"macro", "global"}:
        packet_connections = {
            row.get("connection_ref"): row
            for row in packet.get("connection_registry", [])
            if isinstance(row, dict)
            and isinstance(row.get("connection_ref"), str)
        }
        for coverage in _scope_record_rows(
            semantic_baseline.get("connection_coverage")
        ):
            connection_ref = coverage.get("connection_ref")
            if not isinstance(connection_ref, str) or not connection_ref:
                continue
            connection = packet_connections.get(connection_ref)
            if connection is None:
                continue
            expected_evidence = _connection_evidence_refs(
                connection, label=f"{lane} connection {connection_ref}"
            )
            results = _scope_record_rows(coverage.get("evidence_row_results"))
            supplied_refs = [
                row.get("connection_evidence_ref")
                for row in results
                if isinstance(row.get("connection_evidence_ref"), str)
                and row["connection_evidence_ref"]
            ]
            repeated_refs = {
                row_ref
                for row_ref in supplied_refs
                if supplied_refs.count(row_ref) > 1
            }
            for row_ref in set(supplied_refs):
                if row_ref in repeated_refs or row_ref not in expected_evidence:
                    exceptions.add(
                        "connection_coverage"
                        f"[connection_ref={connection_ref}]."
                        "evidence_row_results"
                        f"[connection_evidence_ref={row_ref}]."
                        "connection_evidence_ref"
                    )

    packet_candidates = {
        row.get("candidate_id"): row
        for row in packet.get("candidate_inventory", [])
        if isinstance(row, dict) and isinstance(row.get("candidate_id"), str)
    }
    for decision in _scope_record_rows(
        semantic_baseline.get("candidate_decisions")
    ):
        candidate_id = decision.get("candidate_id")
        if (
            not isinstance(candidate_id, str)
            or candidate_id not in packet_candidates
        ):
            continue
        allowed_branches = _candidate_branch_refs(
            packet_candidates[candidate_id],
            label=f"{lane} candidate {candidate_id}",
        )
        reasons = decision.get("branch_exclusion_reasons")
        if isinstance(reasons, dict):
            reasons = [reasons]
        if not isinstance(reasons, list):
            continue
        reason_refs = [
            row.get("branch_ref")
            for row in reasons
            if isinstance(row, dict)
            and isinstance(row.get("branch_ref"), str)
            and row["branch_ref"]
        ]
        for branch_ref in set(reason_refs):
            if branch_ref not in allowed_branches:
                exceptions.add(
                    f"candidate_decisions[candidate_id={candidate_id}]."
                    f"branch_exclusion_reasons[branch_ref={branch_ref}].branch_ref"
                )
    return exceptions


def _scope_validation_fallback_identity_paths(
    lane: str,
    packet: dict[str, Any],
    semantic_baseline: dict[str, Any],
) -> set[str]:
    """Identify malformed IDs whose prose may need another stable receiver."""

    expected_by_section: dict[str, tuple[str, set[str]]] = {
        "candidate_decisions": (
            "candidate_id",
            {
                row.get("candidate_id")
                for row in packet.get("candidate_inventory", [])
                if isinstance(row, dict)
                and isinstance(row.get("candidate_id"), str)
            },
        ),
    }
    if lane == "micro":
        expected_by_section.update(
            {
                "surface_coverage": (
                    "analysis_record_ref",
                    {
                        row.get("analysis_record_ref")
                        for row in packet.get("focus_surface_evidence", {}).get(
                            "word_rows", []
                        )
                        if isinstance(row, dict)
                        and isinstance(row.get("analysis_record_ref"), str)
                    },
                ),
                "branch_screen": (
                    "branch_ref",
                    {
                        row.get("branch_ref")
                        for row in packet.get("branch_registry", [])
                        if isinstance(row, dict)
                        and row.get("registry") == "focus"
                        and isinstance(row.get("branch_ref"), str)
                    },
                ),
            }
        )
    else:
        expected_by_section.update(
            {
                "connection_coverage": (
                    "connection_ref",
                    {
                        row.get("connection_ref")
                        for row in packet.get("connection_registry", [])
                        if isinstance(row, dict)
                        and isinstance(row.get("connection_ref"), str)
                    },
                ),
                "atlas_facets_tested": (
                    "branch_ref",
                    {
                        row.get("branch_ref")
                        for row in packet.get("branch_registry", [])
                        if isinstance(row, dict)
                        and isinstance(row.get("branch_ref"), str)
                    },
                ),
            }
        )
    if lane == "global":
        expected_by_section["support_coverage"] = (
            "support_id",
            {
                row.get("support_id")
                for row in packet.get("support_registry", [])
                if isinstance(row, dict)
                and row.get("source_type") != "hft"
                and isinstance(row.get("support_id"), str)
            },
        )

    fallback_paths: set[str] = set()
    for section, (id_field, expected_ids) in expected_by_section.items():
        for row in _scope_record_rows(semantic_baseline.get(section)):
            row_id = row.get(id_field)
            if (
                isinstance(row_id, str)
                and row_id
                and row_id not in expected_ids
            ):
                fallback_paths.add(
                    f"{section}[{id_field}={row_id}].{id_field}"
                )

    for section, id_field in {
        "accepted_findings": "finding_ref",
        "contact_opportunities": "contact_ref",
        "new_findings": "proposal_key",
        "scope_referrals": "referral_ref",
    }.items():
        for row in _scope_record_rows(semantic_baseline.get(section)):
            row_id = row.get(id_field)
            if (
                isinstance(row_id, str)
                and row_id
                and not row_id.startswith(f"{lane}:")
            ):
                fallback_paths.add(
                    f"{section}[{id_field}={row_id}].{id_field}"
                )

    referrals_by_origin: dict[str, list[dict[str, Any]]] = {}
    referral_rows = _scope_record_rows(
        semantic_baseline.get("scope_referrals")
    )
    referral_ref_values = [
        row.get("referral_ref")
        for row in referral_rows
        if isinstance(row.get("referral_ref"), str) and row["referral_ref"]
    ]
    for referral_ref in set(referral_ref_values):
        if referral_ref_values.count(referral_ref) > 1:
            # Duplicate referral IDs may belong to distinct trusted origins.
            # Their origin-bound merge requirements prevent cross-origin prose
            # reassignment while permitting the rows to receive unique IDs.
            fallback_paths.add(
                "scope_referrals"
                f"[referral_ref={referral_ref}].referral_ref"
            )
    for row in referral_rows:
        origin_ref = row.get("origin_ref")
        if isinstance(origin_ref, str) and origin_ref:
            referrals_by_origin.setdefault(origin_ref, []).append(row)
    for rows in referrals_by_origin.values():
        for surplus in rows[1:]:
            referral_ref = surplus.get("referral_ref")
            if isinstance(referral_ref, str) and referral_ref:
                fallback_paths.add(
                    "scope_referrals"
                    f"[referral_ref={referral_ref}].referral_ref"
                )

    branch_facets = {
        row.get("branch_ref"): _branch_facet_ids(row)
        for row in packet.get("branch_registry", [])
        if isinstance(row, dict) and isinstance(row.get("branch_ref"), str)
    }
    facet_section = "branch_screen" if lane == "micro" else "atlas_facets_tested"
    for row in _scope_record_rows(semantic_baseline.get(facet_section)):
        branch_ref = row.get("branch_ref")
        if not isinstance(branch_ref, str) or not branch_ref:
            continue
        expected_facets = branch_facets.get(branch_ref, set())
        for alias in ("tested_facets", "facets_tested"):
            facets = row.get(alias)
            if isinstance(facets, dict):
                facets = [facets]
            if not isinstance(facets, list):
                continue
            for facet in facets:
                if not isinstance(facet, dict):
                    continue
                facet_id = facet.get("facet_id")
                if (
                    isinstance(facet_id, str)
                    and facet_id
                    and facet_id not in expected_facets
                ):
                    fallback_paths.add(
                        f"{facet_section}[branch_ref={branch_ref}]."
                        f"facet[facet_id={facet_id}].facet_id"
                    )

    packet_branch_ids = set(branch_facets)
    for finding in _scope_record_rows(
        semantic_baseline.get("accepted_findings")
    ):
        finding_ref = finding.get("finding_ref")
        if not isinstance(finding_ref, str) or not finding_ref:
            continue
        contributions = finding.get("branch_contributions")
        if isinstance(contributions, dict):
            contributions = [contributions]
        if not isinstance(contributions, list):
            continue
        for contribution in contributions:
            if not isinstance(contribution, dict):
                continue
            branch_ref = contribution.get("branch_ref")
            if (
                isinstance(branch_ref, str)
                and branch_ref
                and branch_ref not in packet_branch_ids
            ):
                fallback_paths.add(
                    f"accepted_findings[finding_ref={finding_ref}]."
                    f"branch_contributions[branch_ref={branch_ref}].branch_ref"
                )
            facet_id = contribution.get("facet_id")
            if (
                isinstance(branch_ref, str)
                and branch_ref
                and isinstance(facet_id, str)
                and facet_id
                and facet_id not in branch_facets.get(branch_ref, set())
            ):
                fallback_paths.add(
                    f"accepted_findings[finding_ref={finding_ref}]."
                    f"branch_contributions[branch_ref={branch_ref}].facet_id"
                )

    if lane in {"macro", "global"}:
        packet_connections = {
            row.get("connection_ref"): row
            for row in packet.get("connection_registry", [])
            if isinstance(row, dict)
            and isinstance(row.get("connection_ref"), str)
        }
        for coverage in _scope_record_rows(
            semantic_baseline.get("connection_coverage")
        ):
            connection_ref = coverage.get("connection_ref")
            if not isinstance(connection_ref, str) or not connection_ref:
                continue
            connection = packet_connections.get(connection_ref)
            if connection is None:
                continue
            expected_evidence = _connection_evidence_refs(
                connection, label=f"{lane} connection {connection_ref}"
            )
            supplied_refs = [
                row.get("connection_evidence_ref")
                for row in _scope_record_rows(
                    coverage.get("evidence_row_results")
                )
                if isinstance(row.get("connection_evidence_ref"), str)
                and row["connection_evidence_ref"]
            ]
            repeated_refs = {
                row_ref
                for row_ref in supplied_refs
                if supplied_refs.count(row_ref) > 1
            }
            for row_ref in set(supplied_refs):
                if row_ref in repeated_refs or row_ref not in expected_evidence:
                    fallback_paths.add(
                        "connection_coverage"
                        f"[connection_ref={connection_ref}]."
                        "evidence_row_results"
                        f"[connection_evidence_ref={row_ref}]."
                        "connection_evidence_ref"
                    )

    packet_candidates = {
        row.get("candidate_id"): row
        for row in packet.get("candidate_inventory", [])
        if isinstance(row, dict) and isinstance(row.get("candidate_id"), str)
    }
    for decision in _scope_record_rows(
        semantic_baseline.get("candidate_decisions")
    ):
        candidate_id = decision.get("candidate_id")
        if not isinstance(candidate_id, str) or candidate_id not in packet_candidates:
            continue
        allowed_branches = _candidate_branch_refs(
            packet_candidates[candidate_id],
            label=f"{lane} candidate {candidate_id}",
        )
        reasons = decision.get("branch_exclusion_reasons")
        if isinstance(reasons, dict):
            reasons = [reasons]
        if not isinstance(reasons, list):
            continue
        for reason in reasons:
            if not isinstance(reason, dict):
                continue
            branch_ref = reason.get("branch_ref")
            if (
                isinstance(branch_ref, str)
                and branch_ref
                and branch_ref not in allowed_branches
            ):
                fallback_paths.add(
                    f"candidate_decisions[candidate_id={candidate_id}]."
                    f"branch_exclusion_reasons[branch_ref={branch_ref}].branch_ref"
                )
    return fallback_paths


def _scope_review_row_field_path(
    path: tuple[str, ...], row: dict[str, Any], field: str
) -> str | None:
    if not path:
        return None
    row_name = path[-1]
    id_field = _SCOPE_REVIEW_ROW_IDS.get(row_name)
    if id_field is None:
        return None
    row_id = row.get(id_field)
    if not isinstance(row_id, str) or not row_id:
        return None
    return f"{row_name}[{id_field}={row_id}].{field}"


def _scope_control_value_is_invalid(
    path: tuple[str, ...], field: str, value: Any
) -> bool:
    if not path:
        return False
    row_name = path[-1]
    allowed = _SCOPE_REVIEW_CONTROL_VALUES.get((row_name, field))
    return allowed is not None and (
        not isinstance(value, str) or value not in allowed
    )


def _scope_exception_path_matches(
    field_path: str | None, exception_paths: frozenset[str]
) -> bool:
    return field_path is not None and field_path in exception_paths


def _semantic_text_values(value: Any) -> set[str]:
    if isinstance(value, dict):
        return {
            text
            for item in value.values()
            for text in _semantic_text_values(item)
        }
    if isinstance(value, list):
        return {text for item in value for text in _semantic_text_values(item)}
    if isinstance(value, str) and value.strip():
        return {value}
    return set()


def _scope_validation_semantic_projection(
    value: Any,
    *,
    path: tuple[str, ...] = (),
    exception_paths: frozenset[str] = frozenset(),
    fallback_identity_paths: frozenset[str] = frozenset(),
    trusted_referral_origins: frozenset[str] = frozenset(),
    source_lane: str | None = None,
    identity_context: tuple[str, ...] = (),
) -> Any:
    """Return the linguistic content that a shape-only repair must preserve.

    Structural validation repairs may repair identities, reference mappings, and
    coverage-ledger shape.  Everything else is prose-bearing evidence for later
    authoring.  Empty values are intentionally omitted so a repair can fill a
    required field that was absent or blank.
    """

    field = path[-1] if path else ""
    structural_fields = {
        "accepted_finding_ref",
        "coverage_complete",
        "duplicate_of",
        "identity",
        "lane",
        "origin_ref",
        "proposal_key",
        "proposal_keys",
        "receiving_finding_ref",
        "referred_lane",
        "refs",
        "schema_version",
        "suggested_lane",
    }
    if (
        field in structural_fields
        or field == "ref"
        or field.endswith("_id")
        or field.endswith("_ids")
        or field.endswith("_ref")
        or field.endswith("_refs")
    ):
        return None
    if isinstance(value, dict):
        projected: dict[str, Any] = {}
        contribution_aliases = (
            ("semantic_carrier", ("surface_carrier", "carrier")),
            ("semantic_contribution", ("contribution", "actual_contribution")),
        )
        aliased_fields = {
            alias for _canonical, aliases in contribution_aliases for alias in aliases
        }
        is_contribution = (
            field == "branch_contributions"
            or "branch_contributions" in path
            or (
                ("independent_anchor" in value or "boundary" in value)
                and any(alias in value for alias in aliased_fields)
            )
        )
        facet_shape_fields = {
            "facet_ids",
            "facet_ids_tested",
            "facets_tested",
            "tested_facets",
        }
        facet_results_by_alias: dict[str, dict[str, set[str]]] = {}
        facet_occurrence_count: dict[str, int] = {}
        facet_occurrences: list[dict[str, Any]] = []
        pending_facet_detail_records: list[
            tuple[str | None, str | None, dict[str, Any]]
        ] = []
        facet_text_records: list[dict[str, Any]] = []
        branch_ref = value.get("branch_ref")
        for key, item in value.items():
            # Internal projection sentinels are derived here, never trusted
            # when supplied by an agent inside the raw review JSON.
            if key.startswith("__commentary_v3_"):
                continue
            if is_contribution and key in aliased_fields:
                continue
            if key in facet_shape_fields:
                facet_items = [item] if isinstance(item, dict) else item
                if isinstance(facet_items, list):
                    for facet in facet_items:
                        if (
                            isinstance(facet, str)
                            and facet.strip()
                            and re.fullmatch(r"F[0-9]+", facet) is None
                        ):
                            facet_text_records.append(
                                {
                                    "__commentary_v3_facet_text__": {
                                        "facet_id": None,
                                        "text": facet,
                                    }
                                }
                            )
                            continue
                        if not isinstance(facet, dict):
                            continue
                        result = facet.get("result")
                        facet_id = facet.get("facet_id")
                        if not isinstance(facet_id, str) or not facet_id:
                            facet_id = None
                        if facet_id is not None:
                            facet_occurrence_count[facet_id] = (
                                facet_occurrence_count.get(facet_id, 0) + 1
                            )
                        validated_facet_ledger = key in {
                            "tested_facets",
                            "facets_tested",
                        }
                        facet_locator = f"facet[facet_id={facet_id}]"
                        facet_identity_path = ".".join(
                            (*identity_context, facet_locator, "facet_id")
                        ) if identity_context else (
                            f"{field}[branch_ref={branch_ref}]."
                            f"{facet_locator}.facet_id"
                        )
                        semantic_facet_id = (
                            facet_id
                            if validated_facet_ledger
                            and facet_id is not None
                            and not (
                                _scope_exception_path_matches(
                                    facet_identity_path, exception_paths
                                )
                                and facet_identity_path
                                in fallback_identity_paths
                            )
                            else None
                        )
                        extras = {
                            extra_key: extra_value
                            for extra_key, extra_value in facet.items()
                            if extra_key not in {"facet_id", "result"}
                        }
                        extra_projection = _scope_validation_semantic_projection(
                            extras,
                            path=(*path, "semantic_facet_detail"),
                            exception_paths=exception_paths,
                            fallback_identity_paths=fallback_identity_paths,
                            trusted_referral_origins=trusted_referral_origins,
                            source_lane=source_lane,
                            identity_context=(*identity_context, facet_locator),
                        )
                        if extra_projection is not None:
                            detail_record: dict[str, Any] = {
                                "detail": extra_projection
                            }
                            if semantic_facet_id is not None:
                                detail_record["facet_id"] = semantic_facet_id
                            pending_facet_detail_records.append(
                                (facet_id, semantic_facet_id, detail_record)
                            )
                        facet_texts = sorted(
                            _semantic_text_values(
                                {
                                    "result": result,
                                    "extras": extra_projection,
                                }
                            )
                        )
                        facet_occurrences.append(
                            {
                                "alias": key,
                                "validated_ledger": validated_facet_ledger,
                                "facet_id": facet_id,
                                "identity_path": facet_identity_path,
                                "semantic_facet_id": semantic_facet_id,
                                "result": result,
                                "texts": facet_texts,
                            }
                        )
                        for text_value in facet_texts:
                            facet_text_records.append(
                                {
                                    "__commentary_v3_facet_text__": {
                                        "facet_id": semantic_facet_id,
                                        "text": text_value,
                                    }
                                }
                            )
                continue
            field_path = (
                ".".join((*identity_context, key))
                if identity_context
                else _scope_review_row_field_path(path, value, key)
            )
            if (
                _scope_exception_path_matches(field_path, exception_paths)
                and not _scope_exception_compatible_control(field, key, item)
            ):
                continue
            if _scope_control_value_is_invalid(path, key, item):
                continue
            normalized_item = (
                [item]
                if key in _SCOPE_REVIEW_ROW_IDS and not isinstance(item, list)
                else item
            )
            child = _scope_validation_semantic_projection(
                normalized_item,
                path=(*path, key),
                exception_paths=exception_paths,
                fallback_identity_paths=fallback_identity_paths,
                trusted_referral_origins=trusted_referral_origins,
                source_lane=source_lane,
                identity_context=identity_context,
            )
            if child is not None:
                projected[key] = child
        if field == "scope_referrals":
            referral_ref = value.get("referral_ref")
            origin_ref = value.get("origin_ref")
            if (
                isinstance(referral_ref, str)
                and referral_ref
                and isinstance(origin_ref, str)
                and origin_ref
                and origin_ref in trusted_referral_origins
            ):
                projected["__commentary_v3_referral_origin__"] = origin_ref
            referred_lane = value.get("referred_lane")
            if (
                isinstance(referral_ref, str)
                and referral_ref
                and isinstance(referred_lane, str)
                and referred_lane
                and source_lane in LANES
                and referred_lane in set(LANES) - {source_lane}
            ):
                projected["__commentary_v3_referral_lane__"] = referred_lane
        for occurrence in facet_occurrences:
            result = occurrence["result"]
            semantic_facet_id = occurrence["semantic_facet_id"]
            if (
                occurrence["validated_ledger"]
                and isinstance(result, str)
                and result.strip()
                and isinstance(semantic_facet_id, str)
            ):
                facet_results_by_alias.setdefault(
                    occurrence["alias"], {}
                ).setdefault(semantic_facet_id, set()).add(result)
        semantic_facet_results: list[dict[str, Any]] = []
        all_facet_ids = sorted(
            {
                facet_id
                for by_id in facet_results_by_alias.values()
                for facet_id in by_id
            }
        )
        for facet_id in all_facet_ids:
            result_sets = [
                by_id[facet_id]
                for by_id in facet_results_by_alias.values()
                if facet_id in by_id
            ]
            results = set().union(*result_sets)
            if len(results) > 1:
                # A valid primary result may be selected, while every supplied
                # result remains required through semantic_facet_texts below.
                results_value: Any = {
                    "__commentary_v3_one_of__": sorted(results)
                }
            elif len(results) == 1:
                results_value = next(iter(results))
            else:
                results_value = None
            facet_record: dict[str, Any] = {}
            facet_locator = f"facet[facet_id={facet_id}]"
            facet_identity_path = ".".join(
                (*identity_context, facet_locator, "facet_id")
            ) if identity_context else (
                f"{field}[branch_ref={branch_ref}]."
                f"{facet_locator}.facet_id"
            )
            if not _scope_exception_path_matches(
                facet_identity_path, exception_paths
            ):
                facet_record["facet_id"] = facet_id
            if results_value is not None:
                facet_record["result"] = results_value
            if facet_record:
                semantic_facet_results.append(facet_record)
        if semantic_facet_results:
            projected["semantic_facet_results"] = semantic_facet_results
        validated_facet_rows = [
            {
                **(
                    {"facet_id": occurrence["semantic_facet_id"]}
                    if occurrence["semantic_facet_id"] is not None
                    else {}
                ),
                "result": occurrence["result"],
                "texts": occurrence["texts"],
            }
            for occurrence in facet_occurrences
            if occurrence["validated_ledger"]
            and isinstance(occurrence["result"], str)
            and occurrence["result"].strip()
        ]
        if validated_facet_rows:
            projected["__commentary_v3_validated_facet_rows__"] = [
                json.loads(encoded)
                for encoded in sorted(
                    {_canonical_json(record) for record in validated_facet_rows}
                )
            ]
        all_supplied_facet_results = {
            result_text
            for occurrence in facet_occurrences
            for result_text in _semantic_text_values(occurrence["result"])
        }
        facet_merge_requirements: list[dict[str, Any]] = []
        for occurrence in facet_occurrences:
            result = occurrence["result"]
            if (
                occurrence["validated_ledger"]
                and occurrence["semantic_facet_id"] is not None
                and isinstance(result, str)
                and result.strip()
            ):
                continue
            if not occurrence["texts"] and not all_supplied_facet_results:
                continue
            semantic_facet_id = occurrence["semantic_facet_id"]
            raw_facet_id = occurrence["facet_id"]
            if semantic_facet_id is not None:
                primary_choices = {
                    result_text
                    for peer in facet_occurrences
                    if peer["semantic_facet_id"] == semantic_facet_id
                    for result_text in _semantic_text_values(peer["result"])
                }
            elif (
                occurrence["validated_ledger"]
                and occurrence["identity_path"]
                not in fallback_identity_paths
                and raw_facet_id is not None
                and facet_occurrence_count.get(raw_facet_id, 0) > 1
            ):
                primary_choices = {
                    result_text
                    for peer in facet_occurrences
                    if peer["facet_id"] == raw_facet_id
                    for result_text in _semantic_text_values(peer["result"])
                }
            else:
                primary_choices = all_supplied_facet_results
            requirement: dict[str, Any] = {
                "texts": occurrence["texts"],
                "primary_choices": sorted(primary_choices),
            }
            if semantic_facet_id is not None:
                requirement["facet_id"] = semantic_facet_id
            facet_merge_requirements.append(requirement)
        if facet_merge_requirements:
            projected["__commentary_v3_facet_merge_requirements__"] = [
                json.loads(encoded)
                for encoded in sorted(
                    {
                        _canonical_json(requirement)
                        for requirement in facet_merge_requirements
                    }
                )
            ]
        # A unique, valid facet row can retain a strict recursive association.
        # Duplicate/alias-conflicting rows may have to merge; their exact prose
        # is instead protected by the facet-attached text requirements below,
        # which allow lossless `preserved_validation_alternatives`.
        facet_detail_records = [
            detail_record
            for facet_id, semantic_facet_id, detail_record
            in pending_facet_detail_records
            if semantic_facet_id is not None
            and facet_id is not None
            and facet_occurrence_count.get(facet_id) == 1
        ]
        if facet_detail_records:
            projected["semantic_facet_details"] = [
                json.loads(encoded)
                for encoded in sorted(
                    {_canonical_json(record) for record in facet_detail_records}
                )
            ]
        if facet_text_records:
            projected["semantic_facet_texts"] = [
                json.loads(encoded)
                for encoded in sorted(
                    {_canonical_json(record) for record in facet_text_records}
                )
            ]
        if is_contribution:
            contribution_facet_id = value.get("facet_id")
            contribution_facet_path = (
                ".".join((*identity_context, "facet_id"))
                if identity_context
                else None
            )
            if (
                isinstance(contribution_facet_id, str)
                and contribution_facet_id
                and not (
                    _scope_exception_path_matches(
                        contribution_facet_path, exception_paths
                    )
                    and contribution_facet_path in fallback_identity_paths
                )
            ):
                projected["semantic_facet_id"] = contribution_facet_id
            for canonical, aliases in contribution_aliases:
                values = {
                    text_value
                    for alias in aliases
                    for text_value in _semantic_text_values(value.get(alias))
                }
                if len(values) == 1:
                    projected[canonical] = next(iter(values))
                elif len(values) > 1:
                    # A valid repair must select one supplied reading; it may not
                    # replace an alias conflict with unrelated generic prose or
                    # discard the unselected supplied reading.
                    projected[canonical] = {
                        "__commentary_v3_one_of__": sorted(values)
                    }
                    projected[
                        f"__commentary_v3_{canonical}_texts__"
                    ] = sorted(values)
        return projected or None
    if isinstance(value, list):
        projected: list[Any] = []
        seen: set[str] = set()
        merge_indexes: set[int] = set()
        control_field = _SCOPE_REVIEW_CONTROL_FIELDS.get(field)

        def row_identity_context(row: dict[str, Any]) -> tuple[str, ...]:
            id_field = _SCOPE_REVIEW_ROW_IDS.get(field)
            if id_field is None:
                return identity_context
            row_id = row.get(id_field)
            if not isinstance(row_id, str) or not row_id:
                return identity_context
            return (
                *identity_context,
                f"{field}[{id_field}={row_id}]",
            )

        def trusted_referral_value(
            row: dict[str, Any], value_field: str
        ) -> str | None:
            if field != "scope_referrals":
                return None
            referral_ref = row.get("referral_ref")
            if not isinstance(referral_ref, str) or not referral_ref:
                return None
            item = row.get(value_field)
            if not isinstance(item, str) or not item:
                return None
            if value_field == "origin_ref":
                return item if item in trusted_referral_origins else None
            if value_field == "referred_lane":
                return (
                    item
                    if source_lane in LANES
                    and item in set(LANES) - {source_lane}
                    else None
                )
            return None

        def valid_control_choices(
            rows: list[tuple[int, dict[str, Any]]],
        ) -> set[str]:
            if control_field is None:
                return set()
            choices: set[str] = set()
            for _index, row in rows:
                control_value = row.get(control_field)
                row_context = row_identity_context(row)
                control_path = (
                    ".".join((*row_context, control_field))
                    if row_context
                    else _scope_review_row_field_path(
                        path, row, control_field
                    )
                )
                if (
                    isinstance(control_value, str)
                    and not _scope_control_value_is_invalid(
                        (field,), control_field, control_value
                    )
                    and (
                        not _scope_exception_path_matches(
                            control_path, exception_paths
                        )
                        or _scope_exception_compatible_control(
                            field, control_field, control_value
                        )
                    )
                ):
                    choices.add(control_value)
            return choices

        all_rows = [
            (index, item)
            for index, item in enumerate(value)
            if isinstance(item, dict)
        ]
        all_control_choices = valid_control_choices(all_rows)

        def append_lossless_merge(
            rows: list[tuple[int, dict[str, Any]]],
            *,
            primary_choices: set[str],
            forced_referral_origin: str | None = None,
        ) -> None:
            texts: set[str] = set()
            for _index, row in rows:
                row_projection = _scope_validation_semantic_projection(
                    row,
                    path=path,
                    exception_paths=exception_paths,
                    fallback_identity_paths=fallback_identity_paths,
                    trusted_referral_origins=trusted_referral_origins,
                    source_lane=source_lane,
                    identity_context=row_identity_context(row),
                )
                if isinstance(row_projection, dict):
                    row_projection = {
                        key: item
                        for key, item in row_projection.items()
                        if not key.startswith("__commentary_v3_")
                    }
                texts.update(_semantic_text_values(row_projection))
            requirement: dict[str, Any] = {
                "allow_parent_fallback": bool(identity_context),
            }
            actual_primaries = valid_control_choices(rows)
            if control_field is not None and actual_primaries:
                requirement["actual_primaries"] = sorted(actual_primaries)
            if control_field is not None and primary_choices:
                requirement["control_field"] = control_field
                requirement["primary_choices"] = sorted(primary_choices)
            if field == "scope_referrals":
                actual_origins = {
                    trusted_referral_value(row, "origin_ref")
                    for _index, row in rows
                    if trusted_referral_value(row, "origin_ref") is not None
                }
                if actual_origins:
                    requirement["actual_referral_origins"] = sorted(
                        actual_origins
                    )
                if forced_referral_origin is not None:
                    requirement["required_referral_origin"] = (
                        forced_referral_origin
                    )
                elif len(actual_origins) == 1:
                    requirement["required_referral_origin"] = next(
                        iter(actual_origins)
                    )
                actual_lanes = {
                    trusted_referral_value(row, "referred_lane")
                    for _index, row in rows
                    if trusted_referral_value(row, "referred_lane") is not None
                }
                if actual_lanes:
                    requirement["actual_referral_lanes"] = sorted(actual_lanes)
                    texts.update(actual_lanes)
                    receiver_origins = (
                        {forced_referral_origin}
                        if forced_referral_origin is not None
                        else actual_origins
                    )
                    peer_lanes = {
                        trusted_referral_value(peer, "referred_lane")
                        for _peer_index, peer in all_rows
                        if (
                            not receiver_origins
                            or trusted_referral_value(peer, "origin_ref")
                            in receiver_origins
                        )
                        and trusted_referral_value(peer, "referred_lane")
                        is not None
                    }
                    requirement["allowed_referral_lanes"] = sorted(
                        peer_lanes or actual_lanes
                    )
            if not texts and len(requirement) == 1:
                return
            requirement["texts"] = sorted(texts)
            marker = {"__commentary_v3_lossless_row_merge__": requirement}
            encoded = _canonical_json(marker)
            if encoded not in seen:
                seen.add(encoded)
                projected.append(marker)

        if field in _SCOPE_MERGEABLE_DUPLICATE_ROWS:
            id_field = _SCOPE_REVIEW_ROW_IDS[field]
            groups: dict[str, list[tuple[int, dict[str, Any]]]] = {}
            for index, item in enumerate(value):
                if not isinstance(item, dict):
                    continue
                row_id = item.get(id_field)
                if isinstance(row_id, str) and row_id:
                    groups.setdefault(row_id, []).append((index, item))
            for group in groups.values():
                if len(group) < 2:
                    continue
                merge_indexes.update(index for index, _item in group)
                if field == "scope_referrals":
                    by_origin: dict[str | None, list[tuple[int, dict[str, Any]]]] = {}
                    for indexed_row in group:
                        origin_ref = indexed_row[1].get("origin_ref")
                        origin_key = (
                            origin_ref
                            if isinstance(origin_ref, str) and origin_ref
                            else None
                        )
                        by_origin.setdefault(origin_key, []).append(indexed_row)
                    if len(by_origin) > 1:
                        for origin_ref, origin_group in by_origin.items():
                            append_lossless_merge(
                                origin_group,
                                primary_choices=valid_control_choices(origin_group),
                                forced_referral_origin=(
                                    trusted_referral_value(
                                        origin_group[0][1], "origin_ref"
                                    )
                                    if origin_ref is not None
                                    else None
                                ),
                            )
                        continue
                group_row = group[0][1]
                group_context = row_identity_context(group_row)
                group_identity_path = (
                    ".".join((*group_context, id_field))
                    if group_context
                    else None
                )
                append_lossless_merge(
                    group,
                    primary_choices=(
                        all_control_choices
                        if group_identity_path in fallback_identity_paths
                        else valid_control_choices(group)
                    ),
                )

        if field in _SCOPE_REVIEW_ROW_IDS:
            id_field = _SCOPE_REVIEW_ROW_IDS[field]
            for index, item in all_rows:
                if index in merge_indexes:
                    continue
                row_id = item.get(id_field)
                row_context = row_identity_context(item)
                identity_path = (
                    ".".join((*row_context, id_field))
                    if row_context
                    else None
                )
                if (
                    isinstance(row_id, str)
                    and row_id
                    and not _scope_exception_path_matches(
                        identity_path, exception_paths
                    )
                ):
                    continue
                merge_indexes.add(index)
                # An invalid/surplus row may need to merge into any stable row
                # in this ledger. Its new primary may therefore use any valid
                # primary already supplied in the same ledger, never an
                # invented value; every displaced phrase remains row-local.
                append_lossless_merge(
                    [(index, item)], primary_choices=all_control_choices
                )

        for index, item in enumerate(value):
            if index in merge_indexes:
                continue
            if (
                field in _SCOPE_REVIEW_ROW_IDS
                and isinstance(item, str)
                and item.strip()
            ):
                child = {"__commentary_v3_contains_text__": item}
            elif field in _SCOPE_REVIEW_ROW_IDS and not isinstance(item, dict):
                child = None
            else:
                child = _scope_validation_semantic_projection(
                    item,
                    path=path,
                    exception_paths=exception_paths,
                    fallback_identity_paths=fallback_identity_paths,
                    trusted_referral_origins=trusted_referral_origins,
                    source_lane=source_lane,
                    identity_context=(
                        row_identity_context(item)
                        if isinstance(item, dict)
                        else identity_context
                    ),
                )
            if child is None:
                continue
            encoded = _canonical_json(child)
            if encoded in seen:
                continue
            seen.add(encoded)
            projected.append(child)
        return projected or None
    if isinstance(value, str):
        return value if value.strip() else None
    if value is None:
        return None
    return value


def _semantic_projection_weight(value: Any) -> int:
    if isinstance(value, dict):
        return 1 + sum(_semantic_projection_weight(item) for item in value.values())
    if isinstance(value, list):
        return 1 + sum(_semantic_projection_weight(item) for item in value)
    return 1


def _semantic_projection_has_value(value: Any, wanted: Any) -> bool:
    if isinstance(value, dict):
        return any(
            _semantic_projection_has_value(item, wanted) for item in value.values()
        )
    if isinstance(value, list):
        return any(_semantic_projection_has_value(item, wanted) for item in value)
    return value == wanted


def _semantic_projection_has_facet_text(
    value: Any, required: dict[str, Any]
) -> bool:
    if isinstance(value, dict):
        candidate = value.get("__commentary_v3_facet_text__")
        if isinstance(candidate, dict) and candidate.get("text") == required.get("text"):
            required_id = required.get("facet_id")
            if required_id is None or candidate.get("facet_id") == required_id:
                return True
        return any(
            _semantic_projection_has_facet_text(item, required)
            for item in value.values()
        )
    if isinstance(value, list):
        return any(
            _semantic_projection_has_facet_text(item, required) for item in value
        )
    return False


def _semantic_projection_has_lossless_row_merge(
    value: Any, required: dict[str, Any]
) -> bool:
    """Find one repaired row that retains a collapsed row/group losslessly."""

    if isinstance(value, dict):
        texts = required.get("texts")
        if not isinstance(texts, list) or any(
            not isinstance(text_value, str) for text_value in texts
        ):
            return False
        repaired_marker = value.get("__commentary_v3_lossless_row_merge__")
        if isinstance(repaired_marker, dict):
            repaired_texts = repaired_marker.get("texts")
            retains_texts = isinstance(repaired_texts, list) and all(
                text_value in repaired_texts for text_value in texts
            )
        else:
            retains_texts = all(
                _semantic_projection_has_value(value, text_value)
                for text_value in texts
            )
        control_field = required.get("control_field")
        primary_choices = required.get("primary_choices")
        primary_is_supplied = True
        if control_field is not None or primary_choices is not None:
            primary_is_supplied = (
                isinstance(control_field, str)
                and isinstance(primary_choices, list)
                and value.get(control_field) in primary_choices
            )
            if not primary_is_supplied and isinstance(repaired_marker, dict):
                repaired_field = repaired_marker.get("control_field")
                repaired_actuals = repaired_marker.get("actual_primaries")
                primary_is_supplied = (
                    repaired_field == control_field
                    and isinstance(repaired_actuals, list)
                    and any(
                        actual in primary_choices for actual in repaired_actuals
                    )
                )
        required_origin = required.get("required_referral_origin")
        retains_origin = True
        if required_origin is not None:
            retains_origin = (
                isinstance(required_origin, str)
                and value.get("__commentary_v3_referral_origin__")
                == required_origin
            )
            if not retains_origin and isinstance(repaired_marker, dict):
                repaired_origins = repaired_marker.get(
                    "actual_referral_origins"
                )
                retains_origin = (
                    isinstance(repaired_origins, list)
                    and required_origin in repaired_origins
                )
        allowed_lanes = required.get("allowed_referral_lanes")
        retains_lane = True
        if allowed_lanes is not None:
            retains_lane = (
                isinstance(allowed_lanes, list)
                and value.get("__commentary_v3_referral_lane__")
                in allowed_lanes
            )
            if not retains_lane and isinstance(repaired_marker, dict):
                repaired_lanes = repaired_marker.get("actual_referral_lanes")
                retains_lane = (
                    isinstance(allowed_lanes, list)
                    and isinstance(repaired_lanes, list)
                    and any(lane in allowed_lanes for lane in repaired_lanes)
                )
        if (
            retains_texts
            and primary_is_supplied
            and retains_origin
            and retains_lane
        ):
            return True
        return False
    if isinstance(value, list):
        return any(
            _semantic_projection_has_lossless_row_merge(item, required)
            for item in value
        )
    return False


def _semantic_projection_has_facet_merge(
    repaired: Any, required: dict[str, Any]
) -> bool:
    """Find one repaired facet that carries a malformed row's full prose."""

    if not isinstance(repaired, dict):
        return False
    validated_rows = repaired.get("__commentary_v3_validated_facet_rows__")
    if not isinstance(validated_rows, list):
        return False
    texts = required.get("texts")
    choices = required.get("primary_choices")
    required_id = required.get("facet_id")
    if (
        not isinstance(texts, list)
        or any(not isinstance(text_value, str) for text_value in texts)
        or not isinstance(choices, list)
        or any(not isinstance(choice, str) for choice in choices)
        or (required_id is not None and not isinstance(required_id, str))
    ):
        return False
    for facet_row in validated_rows:
        if not isinstance(facet_row, dict):
            continue
        candidate_id = facet_row.get("facet_id")
        candidate_result = facet_row.get("result")
        candidate_texts = facet_row.get("texts")
        if required_id is not None and candidate_id != required_id:
            continue
        if not isinstance(candidate_result, str) or (
            choices and candidate_result not in choices
        ):
            continue
        if isinstance(candidate_texts, list) and all(
            text_value in candidate_texts for text_value in texts
        ):
            return True
    return False


def _semantic_projection_contains(repaired: Any, baseline: Any) -> bool:
    """Whether repaired contains every baseline semantic value in place."""

    if isinstance(baseline, dict):
        if set(baseline) == {"__commentary_v3_one_of__"}:
            choices = baseline["__commentary_v3_one_of__"]
            return isinstance(choices, list) and repaired in choices
        if set(baseline) == {"__commentary_v3_contains_text__"}:
            return _semantic_projection_has_value(
                repaired, baseline["__commentary_v3_contains_text__"]
            )
        if set(baseline) == {"__commentary_v3_facet_text__"}:
            required = baseline["__commentary_v3_facet_text__"]
            return isinstance(required, dict) and _semantic_projection_has_facet_text(
                repaired, required
            )
        if set(baseline) == {"__commentary_v3_duplicate_row_texts__"}:
            texts = baseline["__commentary_v3_duplicate_row_texts__"]
            return isinstance(texts, list) and all(
                _semantic_projection_has_value(repaired, text_value)
                for text_value in texts
            )
        if set(baseline) == {"__commentary_v3_lossless_row_merge__"}:
            required = baseline["__commentary_v3_lossless_row_merge__"]
            return isinstance(
                required, dict
            ) and _semantic_projection_has_lossless_row_merge(repaired, required)
        contribution_text_keys = {
            key
            for key in baseline
            if key.startswith("__commentary_v3_semantic_")
            and key.endswith("_texts__")
        }
        for key in contribution_text_keys:
            texts = baseline[key]
            if not isinstance(texts, list) or not all(
                isinstance(text_value, str)
                and _semantic_projection_has_value(repaired, text_value)
                for text_value in texts
            ):
                return False
        facet_merge_requirements = baseline.get(
            "__commentary_v3_facet_merge_requirements__", []
        )
        if not isinstance(facet_merge_requirements, list) or any(
            not isinstance(requirement, dict)
            or not _semantic_projection_has_facet_merge(repaired, requirement)
            for requirement in facet_merge_requirements
        ):
            return False
        ignored_derived_keys = contribution_text_keys | {
            "__commentary_v3_validated_facet_rows__",
            "__commentary_v3_facet_merge_requirements__",
        }
        if not isinstance(repaired, dict):
            return False
        for key, baseline_value in baseline.items():
            if key in ignored_derived_keys:
                continue
            if key in repaired and _semantic_projection_contains(
                repaired[key], baseline_value
            ):
                continue
            if (
                isinstance(baseline_value, list)
                and baseline_value
                and all(
                    isinstance(item, dict)
                    and set(item) == {"__commentary_v3_lossless_row_merge__"}
                    and item["__commentary_v3_lossless_row_merge__"].get(
                        "allow_parent_fallback"
                    )
                    is True
                    for item in baseline_value
                )
                and all(
                    _semantic_projection_contains(repaired, item)
                    for item in baseline_value
                )
            ):
                # A malformed nested ledger can have zero valid row capacity.
                # In that case its prose may move only to alternatives on the
                # same parent row, never to a sibling parent.
                continue
            return False
        return True
    if isinstance(baseline, list):
        if not isinstance(repaired, list):
            return False
        nonconsuming_requirements = [
            item
            for item in baseline
            if isinstance(item, dict)
            and set(item)
            in (
                {"__commentary_v3_contains_text__"},
                {"__commentary_v3_lossless_row_merge__"},
            )
        ]
        if any(
            not _semantic_projection_contains(repaired, requirement)
            for requirement in nonconsuming_requirements
        ):
            return False
        # Lossless-merge requirements may share a structurally valid repaired
        # row with its retained primary, so they do not consume that row.
        # Ordinary distinct semantic rows still consume distinct matches.
        structured_baseline = [
            item for item in baseline if item not in nonconsuming_requirements
        ]
        adjacency = {
            baseline_index: [
                repaired_index
                for repaired_index, repaired_item in enumerate(repaired)
                if _semantic_projection_contains(repaired_item, baseline_item)
            ]
            for baseline_index, baseline_item in enumerate(structured_baseline)
        }
        if any(not candidates for candidates in adjacency.values()):
            return False
        repaired_matches: dict[int, int] = {}

        def assign_distinct_row(
            baseline_index: int, visited_repaired: set[int]
        ) -> bool:
            for repaired_index in adjacency[baseline_index]:
                if repaired_index in visited_repaired:
                    continue
                visited_repaired.add(repaired_index)
                prior_baseline = repaired_matches.get(repaired_index)
                if prior_baseline is None or assign_distinct_row(
                    prior_baseline, visited_repaired
                ):
                    repaired_matches[repaired_index] = baseline_index
                    return True
            return False

        matching_order = sorted(
            range(len(structured_baseline)),
            key=lambda index: (
                len(adjacency[index]),
                -_semantic_projection_weight(structured_baseline[index]),
            ),
        )
        for baseline_index in matching_order:
            if not assign_distinct_row(baseline_index, set()):
                return False
        return True
    return repaired == baseline


def _validate_scope_semantic_row_associations(
    lane: str,
    baseline: Any,
    repaired: Any,
    *,
    path: tuple[str, ...],
    exception_paths: frozenset[str],
    fallback_identity_paths: frozenset[str],
    trusted_referral_origins: frozenset[str],
    source_lane: str,
    identity_context: tuple[str, ...] = (),
) -> None:
    """Keep prose attached to every unchanged, valid stable row identity."""

    if isinstance(baseline, dict) and isinstance(repaired, dict):
        for key, baseline_value in baseline.items():
            repaired_value = repaired.get(key)
            if key in _SCOPE_REVIEW_ROW_IDS:
                normalized_baseline = (
                    [baseline_value]
                    if isinstance(baseline_value, dict)
                    else baseline_value
                )
                normalized_repaired = (
                    [repaired_value]
                    if isinstance(repaired_value, dict)
                    else (
                        repaired_value
                        if isinstance(repaired_value, list)
                        else []
                    )
                )
            else:
                normalized_baseline = baseline_value
                normalized_repaired = repaired_value
            if isinstance(normalized_baseline, (dict, list)) and isinstance(
                normalized_repaired, type(normalized_baseline)
            ):
                _validate_scope_semantic_row_associations(
                    lane,
                    normalized_baseline,
                    normalized_repaired,
                    path=(*path, key),
                    exception_paths=exception_paths,
                    fallback_identity_paths=fallback_identity_paths,
                    trusted_referral_origins=trusted_referral_origins,
                    source_lane=source_lane,
                    identity_context=identity_context,
                )
        return
    if not isinstance(baseline, list) or not isinstance(repaired, list) or not path:
        return
    row_name = path[-1]
    id_field = _SCOPE_REVIEW_ROW_IDS.get(row_name)
    if id_field is None:
        return
    if row_name in {"tested_facets", "facets_tested"}:
        # Both aliases are normalized to canonical (facet_id, result) records in
        # the parent row projection, including exact wrong-ID exceptions.
        return
    baseline_groups: dict[str, list[dict[str, Any]]] = {}
    repaired_groups: dict[str, list[dict[str, Any]]] = {}
    for rows, groups in ((baseline, baseline_groups), (repaired, repaired_groups)):
        for row in rows:
            if not isinstance(row, dict):
                continue
            row_id = row.get(id_field)
            if isinstance(row_id, str) and row_id:
                groups.setdefault(row_id, []).append(row)
    for row_id, rows in baseline_groups.items():
        if row_id in repaired_groups:
            continue
        row_locator = f"{row_name}[{id_field}={row_id}]"
        identity_path = ".".join(
            (*identity_context, row_locator, id_field)
        )
        if not (
            identity_path in exception_paths
            and identity_path in fallback_identity_paths
        ):
            raise SystemExit(
                f"{lane} scope_validation repair changes valid stable identity "
                f"{'.'.join((*identity_context, row_locator))}; retain that "
                "identity and repair only the exact malformed row IDs named in "
                "the repair record"
            )
    for row_id in sorted(set(baseline_groups) & set(repaired_groups)):
        row_locator = f"{row_name}[{id_field}={row_id}]"
        identity_path = ".".join(
            (*identity_context, row_locator, id_field)
        )
        if (
            identity_path in exception_paths
            and identity_path in fallback_identity_paths
        ):
            continue
        baseline_rows = baseline_groups[row_id]
        repaired_rows = repaired_groups[row_id]
        baseline_projection = _scope_validation_semantic_projection(
            baseline_rows,
            path=path,
            exception_paths=exception_paths,
            fallback_identity_paths=fallback_identity_paths,
            trusted_referral_origins=trusted_referral_origins,
            source_lane=source_lane,
            identity_context=identity_context,
        )
        repaired_projection = _scope_validation_semantic_projection(
            repaired_rows,
            path=path,
            exception_paths=exception_paths,
            fallback_identity_paths=fallback_identity_paths,
            trusted_referral_origins=trusted_referral_origins,
            source_lane=source_lane,
            identity_context=identity_context,
        )
        if baseline_projection is not None and not _semantic_projection_contains(
            repaired_projection, baseline_projection
        ):
            raise SystemExit(
                f"{lane} scope_validation repair reassigns linguistic content "
                f"attached to {row_name} {row_id}; restore that row's semantic "
                "baseline verbatim"
            )
        if len(baseline_rows) != 1 or len(repaired_rows) != 1:
            continue
        baseline_row = baseline_rows[0]
        repaired_row = repaired_rows[0]
        _validate_scope_semantic_row_associations(
            lane,
            baseline_row,
            repaired_row,
            path=path,
            exception_paths=exception_paths,
            fallback_identity_paths=fallback_identity_paths,
            trusted_referral_origins=trusted_referral_origins,
            source_lane=source_lane,
            identity_context=(
                *identity_context,
                f"{row_name}[{id_field}={row_id}]",
            ),
        )


def _validate_scope_validation_repair_preserves_semantics(
    lane: str,
    baseline_review: dict[str, Any],
    repaired_review: dict[str, Any],
    exception_paths: set[str],
    fallback_identity_paths: set[str] | None = None,
    trusted_referral_origins: set[str] | None = None,
) -> None:
    """Prevent a shape-only validation repair from losing linguistic content."""

    frozen_exceptions = frozenset(exception_paths)
    frozen_fallbacks = frozenset(fallback_identity_paths or set())
    frozen_referral_origins = frozenset(trusted_referral_origins or set())
    baseline = _scope_validation_semantic_projection(
        baseline_review,
        exception_paths=frozen_exceptions,
        fallback_identity_paths=frozen_fallbacks,
        trusted_referral_origins=frozen_referral_origins,
        source_lane=lane,
    )
    repaired = _scope_validation_semantic_projection(
        repaired_review,
        exception_paths=frozen_exceptions,
        fallback_identity_paths=frozen_fallbacks,
        trusted_referral_origins=frozen_referral_origins,
        source_lane=lane,
    )
    if not isinstance(baseline, dict) or not isinstance(repaired, dict):
        raise SystemExit(f"{lane} validation repair has no semantic review content")
    for section, baseline_content in baseline.items():
        repaired_content = repaired.get(section)
        if _semantic_projection_contains(repaired_content, baseline_content):
            continue
        detail = _canonical_json(baseline_content)
        if len(detail) > 360:
            detail = detail[:357] + "..."
        raise SystemExit(
            f"{lane} scope_validation repair loses or rewrites pre-existing "
            f"linguistic content in {section}; restore the semantic baseline "
            f"verbatim and change only required shape/accounting paths. "
            f"Baseline semantic fragment: {detail}"
        )
    _validate_scope_semantic_row_associations(
        lane,
        baseline_review,
        repaired_review,
        path=(),
        exception_paths=frozen_exceptions,
        fallback_identity_paths=frozen_fallbacks,
        trusted_referral_origins=frozen_referral_origins,
        source_lane=lane,
    )


def _load_bound_scope_artifacts(
    args: argparse.Namespace,
    scope_result: dict[str, Any],
    review_paths: dict[str, Path] | None = None,
    review_manifest_paths: dict[str, Path] | None = None,
    *,
    validate_reviews: bool = True,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, Path]]:
    packets = {
        lane: _load_object(Path(scope_result["stages"][lane]["packet"]))
        for lane in LANES
    }
    review_paths = review_paths or {
        lane: Path(scope_result["stages"][lane]["expected_response"])
        for lane in LANES
    }
    review_manifest_paths = review_manifest_paths or {
        lane: Path(scope_result["stages"][lane]["manifest"])
        for lane in LANES
    }
    reviews = {lane: _load_object(review_paths[lane]) for lane in LANES}
    for lane in LANES:
        identity = packets[lane].get("identity", {})
        if (
            packets[lane].get("schema_version")
            != "commentary-v3-lane-evidence-packet-v2"
        ):
            raise SystemExit(f"{lane} packet does not use the v2 evidence contract")
        if identity.get("ayah_ref") != args.ayah or identity.get("lane") != lane:
            raise SystemExit(f"{lane} packet identity does not match this run")
        expected_packet_hash = _payload_hash_with_identity_field_removed(
            packets[lane], "lane_packet_sha256"
        )
        if identity.get("lane_packet_sha256") != expected_packet_hash:
            raise SystemExit(f"{lane} packet payload hash is stale or tampered")
        review_identity = reviews[lane].get("identity", {})
        manifest = _load_object(review_manifest_paths[lane])
        if reviews[lane].get("ayah_ref") != args.ayah or reviews[lane].get("lane") != lane:
            raise SystemExit(f"{lane} review identity does not match this run")
        if (
            review_identity.get("ayah_ref") != args.ayah
            or review_identity.get("lane") != lane
            or review_identity.get("lane_packet_sha256") != expected_packet_hash
            or review_identity.get("authoring_request_sha256")
            != manifest.get("authoring_request_sha256")
        ):
            raise SystemExit(f"{lane} review is stale or not bound to its prompt")
        if validate_reviews:
            _validate_scope_review(lane, packets[lane], reviews[lane])
    return packets, reviews, review_paths


def _reconciliation_audit_packet(
    packets: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    branches_by_ref: dict[str, dict[str, Any]] = {}
    branch_lane_links: dict[str, list[dict[str, Any]]] = {}
    lanes: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        packet = packets[lane]
        lane_branches = packet.get("branch_registry", [])
        if not isinstance(lane_branches, list):
            raise SystemExit(f"{lane} packet has no branch registry")
        for branch in lane_branches:
            if not isinstance(branch, dict):
                raise SystemExit(f"{lane} packet has a malformed branch record")
            branch_ref = branch.get("branch_ref")
            if not isinstance(branch_ref, str) or not branch_ref:
                raise SystemExit(f"{lane} packet has a branch without an identity")
            semantic_record = dict(branch)
            candidate_links = semantic_record.pop("candidate_links", [])
            support_links = semantic_record.pop("support_links", [])
            hft_citations = semantic_record.pop("hft_citations", [])
            existing = branches_by_ref.get(branch_ref)
            if existing is not None and _canonical_json(existing) != _canonical_json(
                semantic_record
            ):
                raise SystemExit(
                    f"Conflicting cross-lane branch semantics: {branch_ref}"
                )
            branches_by_ref[branch_ref] = semantic_record
            branch_lane_links.setdefault(branch_ref, []).append(
                {
                    "lane": lane,
                    "candidate_links": candidate_links,
                    "support_links": support_links,
                    "hft_citations": hft_citations,
                }
            )
        lanes[lane] = {
            key: value for key, value in packet.items() if key != "branch_registry"
        }

    branch_registry = []
    for branch_ref in sorted(branches_by_ref):
        branch_registry.append(
            {
                **branches_by_ref[branch_ref],
                "lane_links": branch_lane_links[branch_ref],
            }
        )
    return {
        "schema_version": "commentary-v3-reconciliation-audit-packet-v2",
        "ayah_ref": packets["micro"].get("identity", {}).get("ayah_ref"),
        "encoding_note": (
            "Every lane packet is preserved in full except branch_registry. "
            "Cross-lane branch semantics are stored once; lane-specific candidate, "
            "support, and HFT-citation links remain losslessly attached in lane_links."
        ),
        "lanes": lanes,
        "branch_registry": branch_registry,
    }


def _render_reconcile(
    args: argparse.Namespace,
    scope_result: dict[str, Any] | None = None,
    review_paths: dict[str, Path] | None = None,
    review_manifest_paths: dict[str, Path] | None = None,
    repair_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    scope_result = scope_result or _render_scopes(args)
    active_review_manifest_paths = review_manifest_paths or {
        lane: Path(scope_result["stages"][lane]["manifest"])
        for lane in LANES
    }
    packets, reviews, review_paths = _load_bound_scope_artifacts(
        args, scope_result, review_paths, active_review_manifest_paths
    )
    audit_packet = _reconciliation_audit_packet(packets)

    template = _read_prompt("scope-reconcile.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        **{
            f"{lane}_packet_sha256": packets[lane]["identity"][
                "lane_packet_sha256"
            ]
            for lane in LANES
        },
        **{
            f"{lane}_review_sha256": _sha256_json(reviews[lane])
            for lane in LANES
        },
        "audit_packet_sha256": _sha256_json(audit_packet),
    }
    wrapper_template: str | None = None
    if repair_context is not None:
        prior_reconciliation = repair_context.get("prior_reconciliation")
        validation_issue = repair_context.get("validation_issue")
        repair_iteration = repair_context.get("repair_iteration")
        if (
            not isinstance(prior_reconciliation, dict)
            or not isinstance(validation_issue, str)
            or not validation_issue
            or not isinstance(repair_iteration, int)
            or repair_iteration < 1
        ):
            raise SystemExit("Malformed reconciliation repair context")
        wrapper_template = _read_prompt("scope-reconcile-repair-followup.md")
        request_inputs |= {
            "repair_wrapper_template_sha256": _sha256_bytes(
                wrapper_template.encode("utf-8")
            ),
            "prior_reconciliation_sha256": _sha256_json(prior_reconciliation),
            "validation_issue_sha256": _sha256_bytes(
                validation_issue.encode("utf-8")
            ),
            "repair_iteration": repair_iteration,
        }
    stage = (
        "scope-reconcile-repair"
        if repair_context is not None
        else "scope-reconcile"
    )
    request_sha256 = _request_sha256(stage, request_inputs)
    complete_prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@RECONCILIATION_AUDIT_PACKET_JSON@@": _canonical_json(audit_packet),
            "@@MICRO_REVIEW_JSON@@": _canonical_json(reviews["micro"]),
            "@@MACRO_REVIEW_JSON@@": _canonical_json(reviews["macro"]),
            "@@GLOBAL_REVIEW_JSON@@": _canonical_json(reviews["global"]),
        },
        label="scope reconciliation",
    )
    prompt = complete_prompt
    if repair_context is not None:
        assert wrapper_template is not None
        prompt = _render(
            wrapper_template,
            {
                "@@AYAH_REF@@": args.ayah,
                "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
                "@@COMPLETE_RECONCILIATION_PROMPT@@": complete_prompt,
                "@@PRIOR_RECONCILIATION_JSON@@": _canonical_json(
                    repair_context["prior_reconciliation"]
                ),
                "@@VALIDATION_ISSUE_JSON@@": _canonical_json(
                    {"issue": repair_context["validation_issue"]}
                ),
            },
            label="scope reconciliation repair",
        )
    paths = _reconcile_paths(layout, request_sha256)
    prompt_path = paths["prompt"]
    response_path = paths["response"]
    manifest_path = paths["manifest"]
    manifest = _prompt_manifest(
        stage=stage,
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=response_path,
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, prompt_path, prompt)
    _write(V3_ROOT, manifest_path, _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "request_sha256": request_sha256,
        "prompt": str(prompt_path),
        "manifest": str(manifest_path),
        "expected_response": str(response_path),
        "workspace": str(layout.workspace),
        "review_paths": {lane: str(review_paths[lane]) for lane in LANES},
        "review_manifest_paths": {
            lane: str(active_review_manifest_paths[lane])
            for lane in LANES
        },
    }


def _without_arabic_vocalization_marks(value: str) -> str:
    """Ignore only Quranic vocalization marks and dagger/full-alif spelling."""

    output: list[str] = []
    for character in value:
        if character == "\u0670":
            # Quranic dagger alif and a full orthographic alif are the one
            # permitted spelling-level substitution in repair comparison.
            output.append("\u0627")
            continue
        codepoint = ord(character)
        if (
            0x064B <= codepoint <= 0x0652
            or 0x0656 <= codepoint <= 0x065F
            or 0x06D6 <= codepoint <= 0x06DC
            or 0x06DF <= codepoint <= 0x06E4
            or 0x06E7 <= codepoint <= 0x06E8
            or 0x06EA <= codepoint <= 0x06ED
        ):
            continue
        output.append(character)
    return "".join(output)


def _reconciliation_semantic_values_equivalent(before: Any, after: Any) -> bool:
    if before == after:
        return True
    return (
        isinstance(before, str)
        and isinstance(after, str)
        and _without_arabic_vocalization_marks(before)
        == _without_arabic_vocalization_marks(after)
    )


def _reconciliation_semantics_by_member(
    reconciled: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    """Project prose-bearing reconciliation content onto every accepted member."""

    locked_findings = reconciled.get("locked_findings")
    if not isinstance(locked_findings, list) or any(
        not isinstance(finding, dict) for finding in locked_findings
    ):
        raise SystemExit("Reconciled findings lack a locked finding list")
    semantics: dict[str, dict[str, Any]] = {}
    for finding in locked_findings:
        locked_ref = finding.get("locked_finding_ref")
        if not isinstance(locked_ref, str) or not locked_ref:
            raise SystemExit("Every locked finding requires a nonempty reference")
        for field in RECONCILIATION_SEMANTIC_FIELDS[:-1]:
            value = finding.get(field)
            if not isinstance(value, str) or not value.strip():
                raise SystemExit(
                    f"Locked finding {locked_ref} requires nonempty {field}"
                )
        if "epistemic_status" not in finding:
            raise SystemExit(
                f"Locked finding {locked_ref} must retain epistemic_status; "
                "a null source value is allowed"
            )
        member_refs = _string_list(
            finding.get("member_finding_refs"),
            label=f"locked finding {locked_ref} member_finding_refs",
            allow_empty=False,
        )
        projected = {
            field: finding.get(field)
            for field in RECONCILIATION_SEMANTIC_FIELDS
        }
        for member_ref in member_refs:
            if member_ref in semantics:
                raise SystemExit(
                    "Locked findings repeat accepted member ref "
                    f"{member_ref}"
                )
            semantics[member_ref] = projected
    return semantics


def _available_reconciliation_semantics_by_member(
    reconciled: dict[str, Any],
    accepted_member_refs: set[str],
) -> dict[str, dict[str, Any]]:
    """Keep every usable member/field baseline despite partial malformed rows."""

    locked_findings = reconciled.get("locked_findings")
    if not isinstance(locked_findings, list):
        return {}
    semantics: dict[str, dict[str, Any]] = {}
    for finding in locked_findings:
        if not isinstance(finding, dict):
            continue
        member_refs = finding.get("member_finding_refs")
        if not isinstance(member_refs, list):
            continue
        projected = {
            field: finding[field]
            for field in RECONCILIATION_SEMANTIC_FIELDS[:-1]
            if isinstance(finding.get(field), str) and finding[field].strip()
        }
        if "epistemic_status" in finding:
            # Presence is substantive even when the supplied status is null.
            projected["epistemic_status"] = finding["epistemic_status"]
        for member_ref in member_refs:
            if member_ref not in accepted_member_refs:
                # Structural identifier typos must remain repairable. They do
                # not become semantic-baseline identities until they name an
                # accepted scope finding.
                continue
            member_semantics = semantics.setdefault(member_ref, {})
            for field, value in projected.items():
                if field in member_semantics and not (
                    _reconciliation_semantic_values_equivalent(
                        member_semantics[field], value
                    )
                ):
                    raise SystemExit(
                        "Reconciliation repeats accepted member "
                        f"{member_ref} with conflicting usable {field}; "
                        "automatic validation repair would lose linguistic content"
                    )
                member_semantics[field] = value
    return semantics


def _validate_reconciliation_repair_preserves_semantics(
    baseline_by_member: dict[str, dict[str, Any]],
    repaired_by_member: dict[str, dict[str, Any]],
) -> None:
    """Reject repair turns that rewrite already supplied linguistic substance."""

    missing_members = sorted(set(baseline_by_member) - set(repaired_by_member))
    if missing_members:
        raise SystemExit(
            "Reconciliation validation repair removed previously supplied "
            f"linguistic content for members: {missing_members}"
        )
    for member_ref in sorted(set(baseline_by_member) & set(repaired_by_member)):
        baseline = baseline_by_member[member_ref]
        repaired = repaired_by_member[member_ref]
        for field in baseline:
            before = baseline[field]
            if field not in repaired:
                raise SystemExit(
                    "Reconciliation validation repair removed previously supplied "
                    f"linguistic content for {member_ref}.{field}"
                )
            after = repaired[field]
            if _reconciliation_semantic_values_equivalent(before, after):
                continue
            raise SystemExit(
                "Reconciliation validation repair changed linguistic content "
                f"for {member_ref}.{field}"
            )


def _validate_reconciled_findings(
    ayah_ref: str,
    reconciled: dict[str, Any],
    reconcile_manifest: dict[str, Any],
    reviews: dict[str, dict[str, Any]],
    packets: dict[str, dict[str, Any]],
) -> None:
    identity = reconciled.get("identity")
    if (
        reconciled.get("schema_version")
        != "commentary-v3-reconciled-findings-v2"
        or not isinstance(identity, dict)
        or identity.get("ayah_ref") != ayah_ref
        or reconciled.get("ayah_ref") != ayah_ref
        or identity.get("authoring_request_sha256")
        != reconcile_manifest.get("authoring_request_sha256")
    ):
        raise SystemExit("Reconciled findings are stale or not prompt-bound")

    ready = reconciled.get("ready_for_prose")
    if not isinstance(ready, bool):
        raise SystemExit("Reconciled findings require a boolean ready_for_prose")
    repair_requests = reconciled.get("repair_requests")
    if not isinstance(repair_requests, dict) or set(repair_requests) != set(LANES):
        raise SystemExit("Reconciled findings require exact per-lane repair_requests")
    for lane in LANES:
        rows = repair_requests[lane]
        _record_id_set(rows, "repair_ref", label=f"{lane} repair requests")

    accepted_refs: set[str] = set()
    accepted_by_ref: dict[str, tuple[str, dict[str, Any]]] = {}
    referral_refs: set[str] = set()
    referrals_by_ref: dict[str, tuple[str, dict[str, Any]]] = {}
    rejected_by_origin: dict[tuple[str, str], tuple[dict[str, Any], dict[str, Any]]] = {}
    for lane in LANES:
        lane_accepted = _record_id_set(
            reviews[lane].get("accepted_findings"),
            "finding_ref",
            label=f"{lane} accepted findings",
        )
        collisions = accepted_refs & lane_accepted
        if collisions:
            raise SystemExit(
                "Accepted finding refs must be globally unique across lanes: "
                f"{sorted(collisions)}"
            )
        accepted_refs.update(lane_accepted)
        accepted_by_ref.update(
            {
                finding["finding_ref"]: (lane, finding)
                for finding in reviews[lane].get("accepted_findings", [])
            }
        )
        lane_referrals = _record_id_set(
            reviews[lane].get("scope_referrals"),
            "referral_ref",
            label=f"{lane} scope referrals",
        )
        collisions = referral_refs & lane_referrals
        if collisions:
            raise SystemExit(
                "Scope referral refs must be globally unique across lanes: "
                f"{sorted(collisions)}"
            )
        referral_refs.update(lane_referrals)
        referrals_by_ref.update(
            {
                referral["referral_ref"]: (lane, referral)
                for referral in reviews[lane].get("scope_referrals", [])
            }
        )
        packet_candidates = {
            candidate["candidate_id"]: candidate
            for candidate in packets[lane].get("candidate_inventory", [])
        }
        for decision in reviews[lane].get("candidate_decisions", []):
            if decision.get("decision") != "reject":
                continue
            candidate_id = decision["candidate_id"]
            rejected_by_origin[(lane, candidate_id)] = (
                decision,
                packet_candidates[candidate_id],
            )

    rejections = reconciled.get("rejections")
    if not isinstance(rejections, list) or any(
        not isinstance(item, dict) for item in rejections
    ):
        raise SystemExit("Reconciled rejections must be a list of objects")
    actual_rejection_origins: set[tuple[str, str]] = set()
    for rejection in rejections:
        lane = rejection.get("lane")
        candidate_id = rejection.get("candidate_id")
        if lane not in LANES or not isinstance(candidate_id, str) or not candidate_id:
            raise SystemExit("A reconciled rejection has an invalid origin")
        origin = (lane, candidate_id)
        if origin in actual_rejection_origins:
            raise SystemExit(f"Reconciled rejections repeat {lane}:{candidate_id}")
        actual_rejection_origins.add(origin)
        if origin not in rejected_by_origin:
            raise SystemExit(f"Reconciled rejection invents {lane}:{candidate_id}")
        decision, candidate = rejected_by_origin[origin]
        if (
            rejection.get("reason") != decision.get("reason")
            or rejection.get("failed_edge") != decision.get("failed_edge")
            or rejection.get("duplicate_of") != decision.get("duplicate_of")
            or rejection.get("excluded_branch_refs")
            != decision.get("excluded_branch_refs")
            or rejection.get("branch_exclusion_reasons")
            != decision.get("branch_exclusion_reasons")
        ):
            raise SystemExit(
                f"Reconciled rejection does not preserve {lane}:{candidate_id} exactly"
            )
        if set(
            _string_list(
                rejection.get("support_ids"),
                label=f"rejection {lane}:{candidate_id} support_ids",
            )
        ) != set(
            _string_list(
                candidate.get("support_ids"),
                label=f"candidate {lane}:{candidate_id} support_ids",
            )
        ):
            raise SystemExit(
                f"Reconciled rejection loses support for {lane}:{candidate_id}"
            )
        if set(
            _string_list(
                rejection.get("branch_refs"),
                label=f"rejection {lane}:{candidate_id} branch_refs",
            )
        ) != _candidate_branch_refs(
            candidate, label=f"candidate {lane}:{candidate_id}"
        ):
            raise SystemExit(
                f"Reconciled rejection loses branches for {lane}:{candidate_id}"
            )
    if actual_rejection_origins != set(rejected_by_origin):
        raise SystemExit(
            "Reconciliation rejection accounting mismatch; "
            f"missing={sorted(set(rejected_by_origin) - actual_rejection_origins)}, "
            f"extra={sorted(actual_rejection_origins - set(rejected_by_origin))}"
        )

    resolved_referrals = reconciled.get("resolved_referrals")
    unresolved_referrals = reconciled.get("unresolved_referrals")
    resolved_refs = _record_id_set(
        resolved_referrals, "referral_ref", label="resolved referrals"
    )
    unresolved_refs = _record_id_set(
        unresolved_referrals, "referral_ref", label="unresolved referrals"
    )
    if resolved_refs & unresolved_refs:
        raise SystemExit("A scope referral cannot be both resolved and unresolved")
    if resolved_refs | unresolved_refs != referral_refs:
        raise SystemExit(
            "Reconciliation referral accounting mismatch; "
            f"missing={sorted(referral_refs - resolved_refs - unresolved_refs)}, "
            f"extra={sorted((resolved_refs | unresolved_refs) - referral_refs)}"
        )
    for item in [*resolved_referrals, *unresolved_referrals]:
        referral_ref = item["referral_ref"]
        origin_lane, origin_payload = referrals_by_ref[referral_ref]
        if item.get("referral_payload") != origin_payload:
            raise SystemExit(
                f"Reconciliation does not preserve referral payload {referral_ref} exactly"
            )
        if not referral_ref.startswith(f"{origin_lane}:"):
            raise SystemExit(f"Referral {referral_ref} has stale lane identity")
    for item in resolved_referrals:
        referral_ref = item["referral_ref"]
        _origin_lane, origin_payload = referrals_by_ref[referral_ref]
        receiving_ref = item.get("receiving_finding_ref")
        assigned_lane = item.get("assigned_prose_lane")
        if not isinstance(receiving_ref, str) or receiving_ref not in accepted_by_ref:
            raise SystemExit(
                f"Resolved referral {referral_ref} names no accepted receiving finding"
            )
        receiving_lane, _receiving_finding = accepted_by_ref[receiving_ref]
        if receiving_lane != origin_payload.get("referred_lane"):
            raise SystemExit(
                f"Resolved referral {referral_ref} was not accepted by its referred lane"
            )
        receiving_finding = accepted_by_ref[receiving_ref][1]
        available_evidence = {
            "support_ids": {
                row.get("support_id")
                for row in packets[receiving_lane].get("support_registry", [])
            },
            "branch_refs": {
                row.get("branch_ref")
                for row in packets[receiving_lane].get("branch_registry", [])
            },
            "connection_refs": {
                row.get("connection_ref")
                for row in packets[receiving_lane].get("connection_registry", [])
            },
            "contact_refs": {
                row.get("contact_ref")
                for row in reviews[receiving_lane].get("contact_opportunities", [])
            },
        }
        for field, available_refs in available_evidence.items():
            referred_refs = set(
                _string_list(
                    origin_payload.get(field),
                    label=f"referral {referral_ref} {field}",
                )
            )
            retained_refs = set(
                _string_list(
                    receiving_finding.get(field),
                    label=f"receiving finding {receiving_ref} {field}",
                )
            )
            missing_available = (referred_refs & available_refs) - retained_refs
            if missing_available:
                raise SystemExit(
                    f"Resolved referral {referral_ref} loses {field} available "
                    f"to receiving finding {receiving_ref}: {sorted(missing_available)}"
                )
        if assigned_lane not in LANES:
            raise SystemExit(
                f"Resolved referral {referral_ref} has an invalid assigned prose lane"
            )

    disputed = reconciled.get("disputed_decisions")
    if not isinstance(disputed, list) or any(
        not isinstance(item, dict) for item in disputed
    ):
        raise SystemExit("Reconciled disputed_decisions must be a list of objects")

    if ready:
        if unresolved_referrals or disputed or any(repair_requests[lane] for lane in LANES):
            raise SystemExit(
                "ready_for_prose requires no unresolved referrals, disputes, or repairs"
            )
        locked_findings = reconciled.get("locked_findings")
        _reconciliation_semantics_by_member(reconciled)
        locked_refs = _record_id_set(
            locked_findings, "locked_finding_ref", label="locked findings"
        )
        _validate_locked_ref_tokens(locked_refs)
        member_refs: list[str] = []
        for finding in locked_findings:
            member_refs.extend(
                _string_list(
                    finding.get("member_finding_refs"),
                    label=(
                        f"locked finding {finding['locked_finding_ref']} "
                        "member_finding_refs"
                    ),
                    allow_empty=False,
                )
            )
        if len(set(member_refs)) != len(member_refs):
            raise SystemExit("Locked findings do not partition accepted finding refs")
        namespace_collisions = sorted(locked_refs & set(member_refs))
        if namespace_collisions:
            raise SystemExit(
                "Locked and member finding refs must be disjoint: "
                f"{namespace_collisions}"
            )
        if set(member_refs) != accepted_refs:
            raise SystemExit(
                "Locked member coverage does not equal the accepted-finding set; "
                f"missing={sorted(accepted_refs - set(member_refs))}, "
                f"extra={sorted(set(member_refs) - accepted_refs)}"
            )
        conserved_fields = (
            "candidate_ids",
            "proposal_keys",
            "support_ids",
            "branch_refs",
            "connection_refs",
            "contact_refs",
        )
        for locked in locked_findings:
            locked_ref = locked["locked_finding_ref"]
            members = locked["member_finding_refs"]
            for field in conserved_fields:
                expected_union = {
                    item
                    for member_ref in members
                    for item in _string_list(
                        accepted_by_ref[member_ref][1].get(field),
                        label=f"accepted finding {member_ref} {field}",
                    )
                }
                actual = set(
                    _string_list(
                        locked.get(field),
                        label=f"locked finding {locked_ref} {field}",
                    )
                )
                if actual != expected_union:
                    raise SystemExit(
                        f"Locked finding {locked_ref} loses or invents {field}; "
                        f"missing={sorted(expected_union - actual)}, "
                        f"extra={sorted(actual - expected_union)}"
                    )

            expected_contributions = {
                _canonical_json(item)
                for member_ref in members
                for item in accepted_by_ref[member_ref][1].get(
                    "branch_contributions", []
                )
                if isinstance(item, dict)
            }
            actual_contributions = locked.get("branch_contributions")
            if not isinstance(actual_contributions, list) or any(
                not isinstance(item, dict) for item in actual_contributions
            ):
                raise SystemExit(
                    f"Locked finding {locked_ref} has malformed branch contributions"
                )
            actual_contribution_set = {
                _canonical_json(item) for item in actual_contributions
            }
            if actual_contribution_set != expected_contributions:
                raise SystemExit(
                    f"Locked finding {locked_ref} does not preserve the exact "
                    "member branch-contribution union"
                )

            expected_referral_payloads = {
                _canonical_json(item["referral_payload"])
                for item in resolved_referrals
                if item.get("receiving_finding_ref") in members
            }
            actual_referral_payloads = locked.get("referral_payloads")
            if not isinstance(actual_referral_payloads, list) or any(
                not isinstance(item, dict) for item in actual_referral_payloads
            ):
                raise SystemExit(
                    f"Locked finding {locked_ref} has malformed referral payloads"
                )
            if {
                _canonical_json(item) for item in actual_referral_payloads
            } != expected_referral_payloads:
                raise SystemExit(
                    f"Locked finding {locked_ref} does not preserve its exact "
                    "resolved-referral payloads"
                )

            movements = locked.get("scope_movements")
            movement_member_refs = _record_id_set(
                movements,
                "member_finding_ref",
                label=f"locked finding {locked_ref} scope movements",
            )
            if movement_member_refs != set(members):
                raise SystemExit(
                    f"Locked finding {locked_ref} scope movements do not cover members"
                )
            for movement in movements:
                member_ref = movement["member_finding_ref"]
                member_lane, member = accepted_by_ref[member_ref]
                if movement.get("lane") != member_lane:
                    raise SystemExit(
                        f"Locked finding {locked_ref} movement lane is stale for "
                        f"{member_ref}"
                    )
                movement_fields = {
                    "macro": ("local_before", "context_after"),
                    "global": (
                        "isolated_before",
                        "wider_after",
                        "wider_trigger",
                    ),
                }.get(member_lane, ())
                for field in movement_fields:
                    if movement.get(field) != member.get(field):
                        raise SystemExit(
                            f"Locked finding {locked_ref} movement does not preserve "
                            f"{member_ref}.{field} exactly"
                        )
        locked_by_ref, assignments = _locked_finding_assignments(reconciled)
        member_to_locked = {
            member_ref: locked_ref
            for locked_ref, locked in locked_by_ref.items()
            for member_ref in locked["member_finding_refs"]
        }
        for item in resolved_referrals:
            receiving_ref = item["receiving_finding_ref"]
            assigned_lane = item["assigned_prose_lane"]
            locked_ref = member_to_locked[receiving_ref]
            if locked_ref not in assignments[assigned_lane]:
                raise SystemExit(
                    f"Resolved referral {item['referral_ref']} is absent from its "
                    f"assigned {assigned_lane} prose lane"
                )
    elif not any(repair_requests[lane] for lane in LANES):
        raise SystemExit(
            "A non-ready reconciliation must emit at least one concrete lane repair"
        )


def _render_scope_repair(
    args: argparse.Namespace,
    lane: str,
    packet: dict[str, Any],
    prior_review: dict[str, Any],
    reconciled: dict[str, Any],
    repair_requests: list[dict[str, Any]],
    *,
    repair_phase: str,
    repair_iteration: int,
    scope_validation_exception_paths: list[str] | None = None,
) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    wrapper_template = _read_prompt("scope-repair-followup.md")
    wrapper_template_sha256 = _sha256_bytes(wrapper_template.encode("utf-8"))
    scope_template = _read_prompt(f"scope-{lane}.md")
    scope_template_sha256 = _sha256_bytes(scope_template.encode("utf-8"))
    packet_sha256 = packet.get("identity", {}).get("lane_packet_sha256")
    request_inputs = {
        "ayah_ref": args.ayah,
        "lane": lane,
        "lane_packet_sha256": packet_sha256,
        "prior_review_sha256": _sha256_json(prior_review),
        "reconciled_sha256": _sha256_json(reconciled),
        "repair_requests_sha256": _sha256_json(repair_requests),
        "repair_phase": repair_phase,
        "repair_iteration": repair_iteration,
        "wrapper_template_sha256": wrapper_template_sha256,
        "scope_template_sha256": scope_template_sha256,
    }
    if repair_phase == "scope_validation":
        request_inputs["scope_validation_exception_paths"] = sorted(
            scope_validation_exception_paths or []
        )
    request_sha256 = _request_sha256(f"scope-{lane}-repair", request_inputs)
    full_scope_contract = _render(
        scope_template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@LANE_PACKET_SHA256@@": packet_sha256,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@LANE_PACKET_JSON@@": _canonical_json(packet),
        },
        label=f"{lane} repair scope contract",
    )
    prompt = _render(
        wrapper_template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@LANE@@": lane,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@COMPLETE_SCOPE_CONTRACT_MD@@": full_scope_contract,
            "@@PRIOR_REVIEW_JSON@@": _canonical_json(prior_review),
            "@@RECONCILED_JSON@@": _canonical_json(reconciled),
            "@@REPAIR_REQUESTS_JSON@@": _canonical_json(repair_requests),
        },
        label=f"{lane} scope repair",
    )
    paths = _scope_repair_paths(layout, lane, request_sha256)
    manifest = _prompt_manifest(
        stage=f"scope-{lane}-repair",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=paths["response"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["prompt"], prompt)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "lane": lane,
        "request_sha256": request_sha256,
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "expected_response": str(paths["response"]),
        "workspace": str(layout.workspace),
    }


def _reconciled_path(args: argparse.Namespace) -> Path:
    value = getattr(args, "reconciled", None)
    if value is None:
        raise SystemExit("A content-addressed reconciliation path is required")
    return value


def _render_scope_prose(
    args: argparse.Namespace,
    scope_result: dict[str, Any] | None = None,
    review_paths: dict[str, Path] | None = None,
    review_manifest_paths: dict[str, Path] | None = None,
    reconcile_result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    scope_result = scope_result or _render_scopes(args)
    packets, reviews, _review_paths = _load_bound_scope_artifacts(
        args, scope_result, review_paths, review_manifest_paths
    )
    reconciled_path = (
        Path(reconcile_result["expected_response"])
        if reconcile_result is not None
        else _reconciled_path(args)
    )
    reconciled = _load_object(reconciled_path)
    if reconciled.get("ayah_ref") != args.ayah:
        raise SystemExit("Reconciled finding identity does not match --ayah")
    if reconciled.get("ready_for_prose") is not True:
        raise SystemExit("Reconciled finding set is not ready for prose")
    reconcile_manifest_path = (
        Path(reconcile_result["manifest"])
        if reconcile_result is not None
        else getattr(args, "reconcile_manifest", None)
    )
    if reconcile_manifest_path is None:
        raise SystemExit("A content-addressed reconciliation manifest is required")
    reconcile_manifest = _load_object(reconcile_manifest_path)
    _validate_reconciled_findings(
        args.ayah, reconciled, reconcile_manifest, reviews, packets
    )
    locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    assigned_refs = assignments.get(args.lane)
    locked = [
        locked_by_ref[finding_ref]
        for finding_ref in assigned_refs
    ]
    packet = packets[args.lane]
    review = reviews[args.lane]
    assigned_member_refs = {
        member_ref
        for finding in locked
        for member_ref in finding.get("member_finding_refs", [])
    }
    relevant_resolved_referrals = [
        item
        for item in reconciled.get("resolved_referrals", [])
        if item.get("assigned_prose_lane") == args.lane
        or item.get("receiving_finding_ref") in assigned_member_refs
    ]
    relevant_referral_refs = {
        item.get("referral_ref") for item in relevant_resolved_referrals
    }
    originating_referral_records = [
        {**item, "source_lane": source_lane}
        for source_lane in LANES
        for item in reviews[source_lane].get("scope_referrals", [])
        if item.get("referral_ref") in relevant_referral_refs
    ]
    if {
        item.get("referral_ref") for item in originating_referral_records
    } != relevant_referral_refs:
        raise SystemExit("Resolved referral payload is missing from its origin ledger")

    def locked_refs(field: str) -> set[str]:
        refs: set[str] = set()
        for finding in locked:
            refs.update(
                _string_list(
                    finding.get(field),
                    label=(
                        f"locked finding {finding['locked_finding_ref']} {field}"
                    ),
                )
            )
        return refs

    def referral_refs(field: str) -> set[str]:
        refs: set[str] = set()
        for item in relevant_resolved_referrals:
            referral_ref = item.get("referral_ref")
            payload = item.get("referral_payload")
            if not isinstance(payload, dict):
                raise SystemExit(
                    f"Resolved referral {referral_ref} has no payload for prose"
                )
            if field not in payload:
                continue
            refs.update(
                _string_list(
                    payload.get(field),
                    label=f"referral {referral_ref} {field}",
                )
            )
        return refs

    support_ids = locked_refs("support_ids") | referral_refs("support_ids")
    branch_refs = locked_refs("branch_refs") | referral_refs("branch_refs")
    connection_refs = locked_refs("connection_refs") | referral_refs(
        "connection_refs"
    )
    contact_refs = locked_refs("contact_refs") | referral_refs("contact_refs")
    candidate_ids = locked_refs("candidate_ids") | referral_refs("candidate_ids")

    # A referral's origin may itself be a candidate, branch, or contact.  Its
    # complete evidence arrays are already required on the referral payload,
    # but the origin record must also remain visible to the assigned prose lane
    # so its raw HFT payload, facet definition, decision boundary, or contact
    # qualification cannot collapse into an unexplained ID.
    referral_origin_refs: set[str] = set()
    for item in relevant_resolved_referrals:
        payload = item.get("referral_payload")
        if not isinstance(payload, dict):
            raise SystemExit(
                f"Resolved referral {item.get('referral_ref')} has no payload "
                "for prose"
            )
        origin_ref = payload.get("origin_ref")
        if not isinstance(origin_ref, str) or not origin_ref:
            raise SystemExit(
                f"Resolved referral {item.get('referral_ref')} has no valid "
                "origin for prose"
            )
        referral_origin_refs.add(origin_ref)
    all_candidate_ids = {
        item.get("candidate_id")
        for source_lane in LANES
        for item in packets[source_lane].get("candidate_inventory", [])
        if isinstance(item, dict) and isinstance(item.get("candidate_id"), str)
    }
    all_branch_refs = {
        item.get("branch_ref")
        for source_lane in LANES
        for item in packets[source_lane].get("branch_registry", [])
        if isinstance(item, dict) and isinstance(item.get("branch_ref"), str)
    }
    all_contact_refs = {
        item.get("contact_ref")
        for source_lane in LANES
        for item in reviews[source_lane].get("contact_opportunities", [])
        if isinstance(item, dict) and isinstance(item.get("contact_ref"), str)
    }
    missing_origin_records = sorted(
        referral_origin_refs
        - all_candidate_ids
        - all_branch_refs
        - all_contact_refs
    )
    if missing_origin_records:
        raise SystemExit(
            "Resolved referrals cite missing origin records for prose: "
            f"{missing_origin_records}"
        )
    candidate_ids.update(referral_origin_refs & all_candidate_ids)
    branch_refs.update(referral_origin_refs & all_branch_refs)
    contact_refs.update(referral_origin_refs & all_contact_refs)

    origin_branch_pairs = {
        (item["source_lane"], item["origin_ref"])
        for item in originating_referral_records
        if isinstance(item.get("origin_ref"), str)
        and item["origin_ref"]
        in {
            branch.get("branch_ref")
            for branch in packets[item["source_lane"]].get(
                "branch_registry", []
            )
            if isinstance(branch, dict)
        }
    }
    for source_lane, origin_branch_ref in origin_branch_pairs:
        origin_records = [
            branch
            for branch in packets[source_lane].get("branch_registry", [])
            if isinstance(branch, dict)
            and branch.get("branch_ref") == origin_branch_ref
        ]
        if len(origin_records) != 1:
            raise SystemExit(
                f"Referral origin branch {source_lane}:{origin_branch_ref} "
                "does not resolve to exactly one record"
            )
        origin_record = origin_records[0]
        candidate_ids.update(
            link["candidate_id"]
            for link in origin_record.get("candidate_links", [])
            if isinstance(link, dict)
            and isinstance(link.get("candidate_id"), str)
            and link["candidate_id"]
        )
        support_ids.update(
            support_id
            for support_id in origin_record.get("support_links", [])
            if isinstance(support_id, str) and support_id
        )

    def unique_cross_lane_records(
        registry_name: str, ref_field: str, wanted_refs: set[str]
    ) -> list[dict[str, Any]]:
        by_ref: dict[str, dict[str, Any]] = {}
        source_lanes: dict[str, list[str]] = {}
        for source_lane in LANES:
            for item in packets[source_lane].get(registry_name, []):
                item_ref = item.get(ref_field)
                if item_ref not in wanted_refs:
                    continue
                if item_ref in by_ref and _canonical_json(by_ref[item_ref]) != (
                    _canonical_json(item)
                ):
                    raise SystemExit(
                        f"Conflicting cross-lane {registry_name} record: {item_ref}"
                    )
                by_ref[item_ref] = item
                source_lanes.setdefault(item_ref, []).append(source_lane)
        missing = sorted(wanted_refs - set(by_ref))
        if missing:
            raise SystemExit(
                f"Locked findings cite missing {registry_name} records: {missing}"
            )
        return [
            {
                **by_ref[item_ref],
                "available_in_lanes": sorted(set(source_lanes[item_ref])),
            }
            for item_ref in sorted(by_ref)
        ]

    cited_support_records = unique_cross_lane_records(
        "support_registry", "support_id", support_ids
    )
    cited_connection_records = unique_cross_lane_records(
        "connection_registry", "connection_ref", connection_refs
    )
    cited_candidate_records = [
        {**item, "source_lane": source_lane}
        for source_lane in LANES
        for item in packets[source_lane].get("candidate_inventory", [])
        if item.get("candidate_id") in candidate_ids
    ]
    missing_candidate_ids = sorted(
        candidate_ids
        - {item.get("candidate_id") for item in cited_candidate_records}
    )
    if missing_candidate_ids:
        raise SystemExit(
            f"Locked findings or referrals cite missing candidate records: "
            f"{missing_candidate_ids}"
        )
    cited_contact_records = [
        {**item, "source_lane": source_lane}
        for source_lane in LANES
        for item in reviews[source_lane].get("contact_opportunities", [])
        if item.get("contact_ref") in contact_refs
    ]
    missing_contact_refs = sorted(
        contact_refs
        - {item.get("contact_ref") for item in cited_contact_records}
    )
    if missing_contact_refs:
        raise SystemExit(
            f"Locked findings cite missing contact records: {missing_contact_refs}"
        )
    selected_hft_refs = {
        item.get("hft_ref")
        for item in cited_candidate_records
        if isinstance(item.get("hft_ref"), str) and item["hft_ref"]
    }
    branch_records_by_ref: dict[str, dict[str, Any]] = {}
    branch_record_lanes: dict[str, set[str]] = {}
    branch_candidate_links: dict[str, dict[str, dict[str, Any]]] = {}
    branch_support_links: dict[str, set[str]] = {}
    branch_hft_citations: dict[str, dict[str, dict[str, Any]]] = {}
    for source_lane in LANES:
        for item in packets[source_lane].get("branch_registry", []):
            branch_ref = item.get("branch_ref")
            if branch_ref not in branch_refs:
                continue
            semantic_record = {
                key: value
                for key, value in item.items()
                if key not in {"candidate_links", "support_links", "hft_citations"}
            }
            existing = branch_records_by_ref.get(branch_ref)
            if existing is not None and _canonical_json(existing) != (
                _canonical_json(semantic_record)
            ):
                raise SystemExit(
                    f"Conflicting cross-lane branch semantic record: {branch_ref}"
                )
            branch_records_by_ref[branch_ref] = semantic_record
            branch_record_lanes.setdefault(branch_ref, set()).add(source_lane)
            for link in item.get("candidate_links", []):
                if (
                    isinstance(link, dict)
                    and link.get("candidate_id") in candidate_ids
                ):
                    branch_candidate_links.setdefault(branch_ref, {})[
                        _canonical_json(link)
                    ] = link
            branch_support_links.setdefault(branch_ref, set()).update(
                support_id
                for support_id in item.get("support_links", [])
                if isinstance(support_id, str) and support_id in support_ids
            )
            for citation in item.get("hft_citations", []):
                if (
                    isinstance(citation, dict)
                    and (
                        citation.get("hft_ref") in selected_hft_refs
                        or (source_lane, branch_ref) in origin_branch_pairs
                    )
                ):
                    branch_hft_citations.setdefault(branch_ref, {})[
                        _canonical_json(citation)
                    ] = citation
    cited_branch_records = [
        {
            **branch_records_by_ref[branch_ref],
            "candidate_links": [
                branch_candidate_links[branch_ref][key]
                for key in sorted(branch_candidate_links.get(branch_ref, {}))
            ],
            "support_links": sorted(branch_support_links.get(branch_ref, set())),
            "hft_citations": [
                branch_hft_citations[branch_ref][key]
                for key in sorted(branch_hft_citations.get(branch_ref, {}))
            ],
            "available_in_lanes": sorted(branch_record_lanes[branch_ref]),
        }
        for branch_ref in sorted(branch_records_by_ref)
    ]
    missing_branch_refs = sorted(
        branch_refs - {item.get("branch_ref") for item in cited_branch_records}
    )
    if missing_branch_refs:
        raise SystemExit(
            f"Locked findings cite missing branch records: {missing_branch_refs}"
        )
    accepted_record_index = {
        finding["finding_ref"]: (source_lane, finding)
        for source_lane in LANES
        for finding in reviews[source_lane].get("accepted_findings", [])
    }
    missing_member_records = sorted(
        assigned_member_refs - set(accepted_record_index)
    )
    if missing_member_records:
        raise SystemExit(
            f"Locked findings cite missing accepted records: {missing_member_records}"
        )
    member_finding_records = [
        {
            **accepted_record_index[member_ref][1],
            "source_lane": accepted_record_index[member_ref][0],
        }
        for member_ref in sorted(assigned_member_refs)
    ]

    def row_refs(row: dict[str, Any], *fields: str) -> set[str]:
        refs: set[str] = set()
        for field in fields:
            value = row.get(field)
            if isinstance(value, str) and value:
                refs.add(value)
            elif isinstance(value, list):
                refs.update(
                    item for item in value if isinstance(item, str) and item
                )
        return refs

    def selected_review_rows(
        section: str, predicate: Any
    ) -> list[dict[str, Any]]:
        return [
            {**row, "source_lane": source_lane}
            for source_lane in LANES
            for row in reviews[source_lane].get(section, [])
            if isinstance(row, dict) and predicate(row)
        ]

    relevant_friction_refs = (
        set(assigned_refs)
        | assigned_member_refs
        | relevant_referral_refs
        | referral_origin_refs
        | candidate_ids
        | support_ids
        | branch_refs
        | connection_refs
        | contact_refs
        | locked_refs("proposal_keys")
        | {
            branch_ref.split("/", 1)[0]
            for branch_ref in branch_refs
            if "/" in branch_ref
        }
    )
    friction_ref_fields = (
        "refs",
        "inspect",
        "finding_refs",
        "candidate_ids",
        "support_ids",
        "branch_refs",
        "connection_refs",
        "contact_refs",
        "referral_refs",
    )
    contributing_lanes = (
        {args.lane}
        | {
            item["source_lane"]
            for item in member_finding_records
            if item.get("source_lane") in LANES
        }
        | {
            item["source_lane"]
            for item in originating_referral_records
            if item.get("source_lane") in LANES
        }
    )
    selected_friction_notes: list[dict[str, Any]] = []
    for source_lane in LANES:
        for note in reviews[source_lane].get("friction_notes", []):
            if not isinstance(note, dict):
                if source_lane in contributing_lanes:
                    selected_friction_notes.append(
                        {"source_lane": source_lane, "note": note}
                    )
                continue
            explicit_refs = row_refs(note, *friction_ref_fields)
            if explicit_refs:
                include = bool(explicit_refs & relevant_friction_refs)
            else:
                # Unindexed prose-level qualifications follow every lane that
                # contributes a member finding or referral origin to this
                # prose assignment, without importing unrelated lanes.
                include = source_lane in contributing_lanes
            if include:
                selected_friction_notes.append(
                    {**note, "source_lane": source_lane}
                )

    selected_review_context = {
        "surface_coverage": selected_review_rows(
            "surface_coverage",
            lambda row: bool(
                row_refs(row, "finding_refs", "related_finding_refs")
                & assigned_member_refs
            ),
        ),
        "branch_screen": selected_review_rows(
            "branch_screen",
            lambda row: row.get("branch_ref") in branch_refs
            or bool(row_refs(row, "contact_refs") & contact_refs),
        ),
        "connection_coverage": selected_review_rows(
            "connection_coverage",
            lambda row: row.get("connection_ref") in connection_refs,
        ),
        "support_coverage": selected_review_rows(
            "support_coverage",
            lambda row: row.get("support_id") in support_ids,
        ),
        "atlas_facets_tested": selected_review_rows(
            "atlas_facets_tested",
            lambda row: row.get("branch_ref") in branch_refs
            or bool(row_refs(row, "contact_refs") & contact_refs),
        ),
        "candidate_decisions": selected_review_rows(
            "candidate_decisions",
            lambda row: row.get("candidate_id") in candidate_ids,
        ),
        "friction_notes": selected_friction_notes,
    }
    prose_context = {
        "lane": args.lane,
        "locked_findings": locked,
        "member_finding_records": member_finding_records,
        "primary_floor": packet.get("primary_floor"),
        "focus_surface_evidence": packet.get("focus_surface_evidence"),
        "review_context": selected_review_context,
        "cited_support_records": cited_support_records,
        "cited_candidate_records": cited_candidate_records,
        "cited_branch_records": cited_branch_records,
        "cited_connection_records": cited_connection_records,
        "cited_contact_records": cited_contact_records,
        "resolved_referrals": relevant_resolved_referrals,
        "originating_referral_records": originating_referral_records,
        "instruction": (
            "This context preserves exact surface values, decision coverage, "
            "friction, and cited evidence across all origin lanes. HFT support "
            "payloads retain their source containment and exact anchor Arabic. "
            "It is for faithful prose preparation only; do not reopen decisions "
            "or add findings."
        ),
    }
    template = _read_prompt(f"scope-{args.lane}-prose-followup.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    reconciled_sha256 = _sha256_json(reconciled)
    request_inputs = {
        "ayah_ref": args.ayah,
        "lane": args.lane,
        "template_sha256": template_sha256,
        "reconciled_sha256": reconciled_sha256,
        "assigned_finding_refs_sha256": _sha256_json(assigned_refs),
        "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
        "lane_review_sha256": _sha256_json(review),
        "prose_context_sha256": _sha256_json(prose_context),
    }
    request_sha256 = _request_sha256(
        f"scope-{args.lane}-prose", request_inputs
    )
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@RECONCILED_SHA256@@": reconciled_sha256,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@LANE_PROSE_CONTEXT_JSON@@": _canonical_json(prose_context),
        },
        label=f"{args.lane} prose follow-up",
    )
    paths = _scope_prose_paths(layout, args.lane, request_sha256)
    prompt_path = paths["prompt"]
    response_path = paths["response"]
    manifest_path = paths["manifest"]
    manifest = _prompt_manifest(
        stage=f"scope-{args.lane}-prose",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=response_path,
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, prompt_path, prompt)
    _write(V3_ROOT, manifest_path, _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "lane": args.lane,
        "request_sha256": request_sha256,
        "prompt": str(prompt_path),
        "manifest": str(manifest_path),
        "expected_response": str(response_path),
        "locked_finding_count": len(locked),
    }


def _render_scope_prose_repair(
    args: argparse.Namespace,
    lane: str,
    base_prose_result: dict[str, Any],
    prior_prose_result: dict[str, Any],
    validation_issue: str,
    reconciled: dict[str, Any],
    repair_iteration: int,
) -> dict[str, Any]:
    """Render a hermetic same-agent repair for a malformed scope prose draft."""

    layout = _authoring_layout(args.ayah)
    template = _read_prompt("scope-prose-repair-followup.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    base_prompt_path = Path(base_prose_result["prompt"])
    base_manifest_path = Path(base_prose_result["manifest"])
    base_response_path = Path(base_prose_result["expected_response"])
    prior_prompt_path = Path(prior_prose_result["prompt"])
    prior_manifest_path = Path(prior_prose_result["manifest"])
    prior_response_path = Path(prior_prose_result["expected_response"])
    _assert_input_path(layout, base_prompt_path, label=f"{lane} base prose prompt")
    _assert_input_path(
        layout, base_manifest_path, label=f"{lane} base prose manifest"
    )
    _assert_output_path(
        layout, base_response_path, label=f"{lane} base prose draft"
    )
    _assert_input_path(
        layout, prior_prompt_path, label=f"{lane} prior prose prompt"
    )
    _assert_input_path(
        layout, prior_manifest_path, label=f"{lane} prior prose manifest"
    )
    _assert_output_path(
        layout, prior_response_path, label=f"{lane} prior prose draft"
    )
    base_prompt_payload = _required_confined_file(
        layout.inputs, base_prompt_path, label=f"{lane} base prose prompt"
    ).read_bytes()
    base_manifest = _load_object(
        _required_confined_file(
            layout.inputs,
            base_manifest_path,
            label=f"{lane} base prose manifest",
        )
    )
    if (
        base_manifest.get("stage") != f"scope-{lane}-prose"
        or base_manifest.get("ayah_ref") != args.ayah
        or base_manifest.get("authoring_request_sha256")
        != base_prose_result.get("request_sha256")
        or base_manifest.get("expected_response")
        != _manifest_path(base_response_path)
        or base_manifest.get("prompt_sha256")
        != _sha256_bytes(base_prompt_payload)
        or base_manifest.get("prompt_bytes") != len(base_prompt_payload)
    ):
        raise SystemExit(f"{lane} base prose prompt lineage is stale or invalid")

    prior_prompt_payload = _required_confined_file(
        layout.inputs, prior_prompt_path, label=f"{lane} prior prose prompt"
    ).read_bytes()
    prior_manifest = _load_object(
        _required_confined_file(
            layout.inputs,
            prior_manifest_path,
            label=f"{lane} prior prose manifest",
        )
    )
    if (
        prior_manifest.get("stage")
        not in {
            f"scope-{lane}-prose",
            f"scope-{lane}-prose-repair",
            f"scope-{lane}-prose-rewrite",
        }
        or prior_manifest.get("ayah_ref") != args.ayah
        or prior_manifest.get("authoring_request_sha256")
        != prior_prose_result.get("request_sha256")
        or prior_manifest.get("expected_response")
        != _manifest_path(prior_response_path)
        or prior_manifest.get("prompt_sha256")
        != _sha256_bytes(prior_prompt_payload)
        or prior_manifest.get("prompt_bytes") != len(prior_prompt_payload)
    ):
        raise SystemExit(f"{lane} prior prose prompt lineage is stale or invalid")
    prior_draft = _load_object(
        _required_confined_file(
            layout.outputs,
            prior_response_path,
            label=f"{lane} prior prose draft",
        )
    )
    locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    locked_ref_map = [
        {
            "locked_finding_ref": locked_ref,
            "member_finding_refs": locked_by_ref[locked_ref][
                "member_finding_refs"
            ],
        }
        for locked_ref in assignments[lane]
    ]
    request_inputs = {
        "ayah_ref": args.ayah,
        "lane": lane,
        "template_sha256": template_sha256,
        "base_prompt_sha256": base_manifest["prompt_sha256"],
        "base_request_sha256": base_prose_result["request_sha256"],
        "prior_request_sha256": prior_prose_result["request_sha256"],
        "prior_draft_sha256": _sha256_json(prior_draft),
        "reconciled_sha256": _sha256_json(reconciled),
        "locked_ref_map_sha256": _sha256_json(locked_ref_map),
        "validation_issue": validation_issue,
        "repair_iteration": repair_iteration,
    }
    request_sha256 = _request_sha256(
        f"scope-{lane}-prose-repair", request_inputs
    )
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@LANE@@": lane,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@RECONCILED_SHA256@@": _sha256_json(reconciled),
            "@@VALIDATION_ISSUE_JSON@@": _canonical_json(
                {"issue": validation_issue}
            ),
            "@@PRIOR_PROSE_DRAFT_JSON@@": _canonical_json(prior_draft),
            "@@LOCKED_REF_MAP_JSON@@": _canonical_json(locked_ref_map),
        },
        label=f"{lane} scope prose repair",
    )
    paths = _scope_prose_repair_paths(layout, lane, request_sha256)
    manifest = _prompt_manifest(
        stage=f"scope-{lane}-prose-repair",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=paths["response"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["prompt"], prompt)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "lane": lane,
        "request_sha256": request_sha256,
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "expected_response": str(paths["response"]),
    }


def _render_scope_prose_rewrite(
    args: argparse.Namespace,
    lane: str,
    base_prose_result: dict[str, Any],
    prior_prose_result: dict[str, Any],
    validation_issue: str,
    reconciled: dict[str, Any],
    rewrite_iteration: int,
) -> dict[str, Any]:
    """Render a genuine same-agent prose turn when normalization is unsafe."""

    layout = _authoring_layout(args.ayah)
    template = _read_prompt("scope-prose-rewrite-followup.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    base_prompt_path = Path(base_prose_result["prompt"])
    base_manifest_path = Path(base_prose_result["manifest"])
    base_response_path = Path(base_prose_result["expected_response"])
    prior_prompt_path = Path(prior_prose_result["prompt"])
    prior_manifest_path = Path(prior_prose_result["manifest"])
    prior_response_path = Path(prior_prose_result["expected_response"])
    _assert_input_path(layout, base_prompt_path, label=f"{lane} base prose prompt")
    _assert_input_path(
        layout, base_manifest_path, label=f"{lane} base prose manifest"
    )
    _assert_output_path(
        layout, base_response_path, label=f"{lane} base prose draft"
    )
    _assert_input_path(
        layout, prior_prompt_path, label=f"{lane} prior prose prompt"
    )
    _assert_input_path(
        layout, prior_manifest_path, label=f"{lane} prior prose manifest"
    )
    _assert_output_path(
        layout, prior_response_path, label=f"{lane} prior prose draft"
    )
    base_prompt_payload = _required_confined_file(
        layout.inputs, base_prompt_path, label=f"{lane} base prose prompt"
    ).read_bytes()
    base_manifest = _load_object(
        _required_confined_file(
            layout.inputs,
            base_manifest_path,
            label=f"{lane} base prose manifest",
        )
    )
    if (
        base_manifest.get("stage") != f"scope-{lane}-prose"
        or base_manifest.get("ayah_ref") != args.ayah
        or base_manifest.get("authoring_request_sha256")
        != base_prose_result.get("request_sha256")
        or base_manifest.get("expected_response")
        != _manifest_path(base_response_path)
        or base_manifest.get("prompt_sha256")
        != _sha256_bytes(base_prompt_payload)
        or base_manifest.get("prompt_bytes") != len(base_prompt_payload)
    ):
        raise SystemExit(f"{lane} base prose prompt lineage is stale or invalid")

    prior_prompt_payload = _required_confined_file(
        layout.inputs, prior_prompt_path, label=f"{lane} prior prose prompt"
    ).read_bytes()
    prior_manifest = _load_object(
        _required_confined_file(
            layout.inputs,
            prior_manifest_path,
            label=f"{lane} prior prose manifest",
        )
    )
    if (
        prior_manifest.get("stage")
        not in {
            f"scope-{lane}-prose",
            f"scope-{lane}-prose-repair",
            f"scope-{lane}-prose-rewrite",
        }
        or prior_manifest.get("ayah_ref") != args.ayah
        or prior_manifest.get("authoring_request_sha256")
        != prior_prose_result.get("request_sha256")
        or prior_manifest.get("expected_response")
        != _manifest_path(prior_response_path)
        or prior_manifest.get("prompt_sha256")
        != _sha256_bytes(prior_prompt_payload)
        or prior_manifest.get("prompt_bytes") != len(prior_prompt_payload)
    ):
        raise SystemExit(f"{lane} prior prose prompt lineage is stale or invalid")
    prior_draft = _load_object(
        _required_confined_file(
            layout.outputs,
            prior_response_path,
            label=f"{lane} prior prose draft",
        )
    )
    locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    assigned_locked_findings = [
        locked_by_ref[locked_ref] for locked_ref in assignments[lane]
    ]
    request_inputs = {
        "ayah_ref": args.ayah,
        "lane": lane,
        "template_sha256": template_sha256,
        "base_prompt_sha256": base_manifest["prompt_sha256"],
        "base_request_sha256": base_prose_result["request_sha256"],
        "prior_request_sha256": prior_prose_result["request_sha256"],
        "prior_draft_sha256": _sha256_json(prior_draft),
        "reconciled_sha256": _sha256_json(reconciled),
        "assigned_locked_findings_sha256": _sha256_json(
            assigned_locked_findings
        ),
        "validation_issue": validation_issue,
        "rewrite_iteration": rewrite_iteration,
    }
    request_sha256 = _request_sha256(
        f"scope-{lane}-prose-rewrite", request_inputs
    )
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@LANE@@": lane,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@RECONCILED_SHA256@@": _sha256_json(reconciled),
            "@@VALIDATION_ISSUE_JSON@@": _canonical_json(
                {"issue": validation_issue}
            ),
            "@@PRIOR_PROSE_DRAFT_JSON@@": _canonical_json(prior_draft),
            "@@ASSIGNED_LOCKED_FINDINGS_JSON@@": _canonical_json(
                assigned_locked_findings
            ),
        },
        label=f"{lane} scope prose rewrite",
    )
    paths = _scope_prose_rewrite_paths(layout, lane, request_sha256)
    manifest = _prompt_manifest(
        stage=f"scope-{lane}-prose-rewrite",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=paths["response"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["prompt"], prompt)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "lane": lane,
        "request_sha256": request_sha256,
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "expected_response": str(paths["response"]),
    }


def _scope_prose_issue_is_accounting_only(issue: str) -> bool:
    """Return whether a prose defect can be repaired without rewriting prose."""

    accounting_markers = (
        "prose draft schema version is stale or invalid",
        "prose movement has malformed finding refs",
        "prose movement uses non-locked finding refs",
        "prose draft lacks a finding landing list",
        "prose draft has an invalid finding landing",
        "prose draft repeats a finding landing",
        "prose draft finding landings do not cover its locked set",
        "prose draft has a detached finding landing",
    )
    return any(marker in issue for marker in accounting_markers)


def _scope_prose_lossless_ref_normalization(
    lane: str,
    prior: dict[str, Any],
    locked_by_ref: dict[str, dict[str, Any]],
    assigned_refs: list[str],
) -> tuple[dict[str, list[str]], dict[str, str]]:
    """Derive the only safe member-to-locked accounting normalization."""

    assigned = set(assigned_refs)
    member_to_locked = {
        member_ref: locked_ref
        for locked_ref, finding in locked_by_ref.items()
        for member_ref in _string_list(
            finding.get("member_finding_refs"),
            label=f"locked finding {locked_ref} member_finding_refs",
            allow_empty=False,
        )
    }
    movements = prior.get("movements")
    if not isinstance(movements, list) or any(
        not isinstance(movement, dict) for movement in movements
    ):
        raise SystemExit(
            f"{lane} draft has no movement structure that can be normalized"
        )

    normalized_by_movement: dict[str, list[str]] = {}
    movement_by_locked_ref: dict[str, str] = {}
    for movement in movements:
        movement_key = movement.get("movement_key")
        if (
            not isinstance(movement_key, str)
            or not movement_key
            or movement_key in normalized_by_movement
        ):
            raise SystemExit(
                f"{lane} draft has no unique movement keys for lossless normalization"
            )
        prior_refs = movement.get("finding_refs")
        if (
            not isinstance(prior_refs, list)
            or not prior_refs
            or any(not isinstance(ref, str) or not ref for ref in prior_refs)
        ):
            raise SystemExit(
                f"{lane} movement {movement_key} has no usable prior finding refs"
            )
        normalized_refs: list[str] = []
        for prior_ref in prior_refs:
            if prior_ref in assigned:
                locked_ref = prior_ref
            else:
                locked_ref = member_to_locked.get(prior_ref)
            if locked_ref not in assigned:
                raise SystemExit(
                    f"{lane} movement {movement_key} cites unmappable prior ref "
                    f"{prior_ref}"
                )
            if locked_ref not in normalized_refs:
                normalized_refs.append(locked_ref)
        normalized_by_movement[movement_key] = normalized_refs
        for locked_ref in normalized_refs:
            prior_movement = movement_by_locked_ref.get(locked_ref)
            if prior_movement is not None and prior_movement != movement_key:
                raise SystemExit(
                    f"{lane} locked finding {locked_ref} occurs in multiple prior "
                    "movements"
                )
            movement_by_locked_ref[locked_ref] = movement_key

    missing = sorted(assigned - set(movement_by_locked_ref))
    extra = sorted(set(movement_by_locked_ref) - assigned)
    if missing or extra:
        raise SystemExit(
            f"{lane} prior prose has no lossless full finding normalization; "
            f"missing={missing}, extra={extra}"
        )
    return normalized_by_movement, movement_by_locked_ref


def _validate_scope_prose_repair_preserves_semantics(
    lane: str,
    prior: dict[str, Any],
    repaired: dict[str, Any],
    expected_movement_refs: dict[str, list[str]],
    expected_landing_movements: dict[str, str],
) -> None:
    """Permit accounting repair while making prose preservation an invariant."""

    if repaired.get("friction_notes") != prior.get("friction_notes"):
        raise SystemExit(
            f"{lane} scope prose repair changed friction_notes"
        )
    for field in ("ayah_ref", "lane", "coverage_complete"):
        if repaired.get(field) != prior.get(field):
            raise SystemExit(
                f"{lane} scope prose repair changed prior {field}"
            )
    prior_identity = prior.get("identity")
    repaired_identity = repaired.get("identity")
    if not isinstance(prior_identity, dict) or not isinstance(
        repaired_identity, dict
    ):
        raise SystemExit(f"{lane} scope prose repair has malformed identity")
    prior_identity_semantics = dict(prior_identity)
    repaired_identity_semantics = dict(repaired_identity)
    prior_identity_semantics.pop("authoring_request_sha256", None)
    repaired_identity_semantics.pop("authoring_request_sha256", None)
    if repaired_identity_semantics != prior_identity_semantics:
        raise SystemExit(
            f"{lane} scope prose repair changed identity fields other than "
            "the repair request hash"
        )

    prior_movements = prior.get("movements")
    repaired_movements = repaired.get("movements")
    if (
        not isinstance(prior_movements, list)
        or any(not isinstance(item, dict) for item in prior_movements)
        or not isinstance(repaired_movements, list)
        or any(not isinstance(item, dict) for item in repaired_movements)
    ):
        raise SystemExit(
            f"{lane} scope prose repair cannot preserve a malformed movement list"
        )
    prior_semantics = [
        {key: value for key, value in movement.items() if key != "finding_refs"}
        for movement in prior_movements
    ]
    repaired_semantics = [
        {key: value for key, value in movement.items() if key != "finding_refs"}
        for movement in repaired_movements
    ]
    if repaired_semantics != prior_semantics:
        raise SystemExit(
            f"{lane} scope prose repair changed movement order, keys, prose, "
            "or non-accounting movement content"
        )
    repaired_movement_refs = {
        movement["movement_key"]: movement.get("finding_refs")
        for movement in repaired_movements
    }
    if repaired_movement_refs != expected_movement_refs:
        raise SystemExit(
            f"{lane} scope prose repair changed or invented a finding-to-prose "
            "relationship instead of losslessly normalizing member refs"
        )

    repaired_landings = repaired.get("finding_landings")
    if not isinstance(repaired_landings, list) or any(
        not isinstance(landing, dict) for landing in repaired_landings
    ):
        raise SystemExit(f"{lane} scope prose repair has malformed landings")
    repaired_landing_movements: dict[str, str] = {}
    for landing in repaired_landings:
        finding_ref = landing.get("finding_ref")
        movement_key = landing.get("movement_key")
        if (
            not isinstance(finding_ref, str)
            or not finding_ref
            or not isinstance(movement_key, str)
            or not movement_key
            or finding_ref in repaired_landing_movements
        ):
            raise SystemExit(
                f"{lane} scope prose repair has ambiguous finding landings"
            )
        repaired_landing_movements[finding_ref] = movement_key
    if repaired_landing_movements != expected_landing_movements:
        raise SystemExit(
            f"{lane} scope prose repair changed or invented a finding landing "
            "relationship"
        )

    accounting_top_level = {
        "schema_version",
        "identity",
        "ayah_ref",
        "lane",
        "coverage_complete",
        "movements",
        "finding_landings",
        "friction_notes",
    }
    prior_other = {
        key: value
        for key, value in prior.items()
        if key not in accounting_top_level
    }
    repaired_other = {
        key: value
        for key, value in repaired.items()
        if key not in accounting_top_level
    }
    if repaired_other != prior_other:
        raise SystemExit(
            f"{lane} scope prose repair changed non-accounting top-level content"
        )


def _validate_scope_prose_draft(
    ayah_ref: str,
    lane: str,
    draft: dict[str, Any],
    draft_manifest: dict[str, Any],
    reconciled: dict[str, Any],
    assignments: dict[str, list[str]],
) -> None:
    if draft.get("ayah_ref") != ayah_ref or draft.get("lane") != lane:
        raise SystemExit(f"{lane} prose draft identity does not match this run")
    draft_identity = draft.get("identity")
    if (
        not isinstance(draft_identity, dict)
        or draft_identity.get("ayah_ref") != ayah_ref
        or draft_identity.get("lane") != lane
        or draft_identity.get("reconciled_sha256") != _sha256_json(reconciled)
        or draft_identity.get("authoring_request_sha256")
        != draft_manifest.get("authoring_request_sha256")
    ):
        raise SystemExit(f"{lane} prose draft is stale or not prompt-bound")
    if draft.get("coverage_complete") is not True:
        raise SystemExit(f"{lane} prose draft does not attest complete coverage")
    friction_notes = draft.get("friction_notes")
    if not isinstance(friction_notes, list):
        raise SystemExit(f"{lane} prose draft lacks a friction_notes list")
    movements = draft.get("movements")
    if not isinstance(movements, list) or any(
        not isinstance(movement, dict) for movement in movements
    ):
        raise SystemExit(f"{lane} prose draft lacks a movement list")
    movement_keys = [movement.get("movement_key") for movement in movements]
    if any(not isinstance(key, str) or not key for key in movement_keys):
        raise SystemExit(f"{lane} prose draft has an invalid movement key")
    if len(set(movement_keys)) != len(movement_keys):
        raise SystemExit(f"{lane} prose draft repeats a movement key")
    movements_by_key = dict(zip(movement_keys, movements, strict=True))
    for movement in movements:
        if (
            not isinstance(movement.get("draft_prose"), str)
            or not movement["draft_prose"].strip()
        ):
            raise SystemExit(f"{lane} prose draft has an empty movement")

    # Only after every lineage and prose-bearing precondition passes may a
    # schema/ref/landing defect enter the accounting-only repair route.
    if draft.get("schema_version") != "commentary-v3-scope-prose-draft-v1":
        raise SystemExit(
            f"{lane} prose draft schema version is stale or invalid"
        )
    assigned = set(assignments[lane])
    for movement in movements:
        finding_refs = movement.get("finding_refs")
        malformed = (
            not isinstance(finding_refs, list)
            or not finding_refs
            or any(not isinstance(ref, str) or not ref for ref in finding_refs)
            or len(set(finding_refs)) != len(finding_refs)
        )
        if malformed:
            raise SystemExit(f"{lane} prose movement has malformed finding refs")
        invalid_refs = sorted(set(finding_refs) - assigned)
        if invalid_refs:
            raise SystemExit(
                f"{lane} prose movement uses non-locked finding refs: "
                f"{invalid_refs}; allowed locked refs={sorted(assigned)}"
            )
    landings = draft.get("finding_landings")
    if not isinstance(landings, list) or any(
        not isinstance(landing, dict) for landing in landings
    ):
        raise SystemExit(f"{lane} prose draft lacks a finding landing list")
    landing_refs = [landing.get("finding_ref") for landing in landings]
    if any(not isinstance(ref, str) or not ref for ref in landing_refs):
        raise SystemExit(f"{lane} prose draft has an invalid finding landing")
    if len(set(landing_refs)) != len(landing_refs):
        raise SystemExit(f"{lane} prose draft repeats a finding landing")
    if set(landing_refs) != assigned:
        raise SystemExit(
            f"{lane} prose draft finding landings do not cover its locked set; "
            f"missing={sorted(assigned - set(landing_refs))}, "
            f"extra={sorted(set(landing_refs) - assigned)}"
        )
    for landing in landings:
        movement_key = landing.get("movement_key")
        if (
            not isinstance(movement_key, str)
            or movement_key not in movements_by_key
            or landing["finding_ref"]
            not in movements_by_key[movement_key]["finding_refs"]
        ):
            raise SystemExit(
                f"{lane} prose draft has a detached finding landing: {landing}"
            )


def _render_merge(
    args: argparse.Namespace,
    scope_result: dict[str, Any] | None = None,
    reconcile_result: dict[str, Any] | None = None,
    prose_results: dict[str, dict[str, Any]] | None = None,
    reviews: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    scope_result = scope_result or _render_scopes(args)
    if reconcile_result is None or prose_results is None:
        raise SystemExit(
            "Canonical merge requires content-addressed reconciliation and prose stages"
        )
    reconciled = _load_object(Path(reconcile_result["expected_response"]))
    if reconciled.get("ayah_ref") != args.ayah:
        raise SystemExit("Reconciled finding identity does not match --ayah")
    if reconciled.get("ready_for_prose") is not True:
        raise SystemExit("Reconciled finding set is not ready for prose")
    reconcile_manifest = _load_object(Path(reconcile_result["manifest"]))
    packets = {
        lane: _load_object(Path(scope_result["stages"][lane]["packet"]))
        for lane in LANES
    }
    if reviews is not None:
        _validate_reconciled_findings(
            args.ayah, reconciled, reconcile_manifest, reviews, packets
        )
    _locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    micro_packet = packets["micro"]
    micro_packet_identity = micro_packet.get("identity", {})
    expected_micro_packet_hash = _payload_hash_with_identity_field_removed(
        micro_packet, "lane_packet_sha256"
    )
    if (
        micro_packet_identity.get("ayah_ref") != args.ayah
        or micro_packet_identity.get("lane") != "micro"
        or micro_packet_identity.get("lane_packet_sha256")
        != expected_micro_packet_hash
    ):
        raise SystemExit("Micro surface packet is stale or not bound to this run")
    if (
        reconcile_manifest.get("inputs", {}).get("micro_packet_sha256")
        != expected_micro_packet_hash
    ):
        raise SystemExit(
            "Micro surface packet differs from the packet used for reconciliation"
        )
    focus_surface_evidence = micro_packet.get("focus_surface_evidence")
    if not isinstance(focus_surface_evidence, dict):
        raise SystemExit("Micro packet lacks exact focus-surface evidence")
    focus_surface_evidence = {
        "primary_floor": micro_packet.get("primary_floor"),
        **focus_surface_evidence,
    }
    drafts = {
        lane: _load_object(Path(prose_results[lane]["expected_response"]))
        for lane in LANES
    }
    for lane in LANES:
        draft_manifest = _load_object(Path(prose_results[lane]["manifest"]))
        _validate_scope_prose_draft(
            args.ayah,
            lane,
            drafts[lane],
            draft_manifest,
            reconciled,
            assignments,
        )

    principles_path = REPO_ROOT / "PRINCIPLES.md"
    commentary_spec_path = REPO_ROOT / "COMMENTARY_SPEC.md"
    channels_path = REPO_ROOT / "docs" / "CHANNELS.md"
    canonical_prompt_path = REPO_ROOT / "_ayah_commentary" / "v2" / "PROMPT.md"
    principles = principles_path.read_text(encoding="utf-8")
    commentary_spec = commentary_spec_path.read_text(encoding="utf-8")
    channels = channels_path.read_text(encoding="utf-8")
    canonical_prompt = canonical_prompt_path.read_text(encoding="utf-8")
    template = _read_prompt("scope-merge.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    editorial_template = _read_prompt("editorial-followup.md")
    editorial_template_sha256 = _sha256_bytes(
        editorial_template.encode("utf-8")
    )
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        "editorial_template_sha256": editorial_template_sha256,
        "principles_sha256": _sha256_bytes(principles.encode("utf-8")),
        "commentary_spec_sha256": _sha256_bytes(
            commentary_spec.encode("utf-8")
        ),
        "channels_sha256": _sha256_bytes(channels.encode("utf-8")),
        "canonical_prompt_sha256": _sha256_bytes(
            canonical_prompt.encode("utf-8")
        ),
        "reconciled_sha256": _sha256_json(reconciled),
        "focus_surface_evidence_sha256": _sha256_json(focus_surface_evidence),
        **{
            f"{lane}_draft_sha256": _sha256_json(drafts[lane])
            for lane in LANES
        },
    }
    request_sha256 = _request_sha256("canonical-merge", request_inputs)
    paths = _merge_paths(layout, request_sha256)
    outputs = paths["outputs"]
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@PROSE_OUTPUT_PATH@@": _manifest_path(outputs["prose"]),
            "@@EVIDENCE_OUTPUT_PATH@@": _manifest_path(outputs["evidence"]),
            "@@INDEX_OUTPUT_PATH@@": _manifest_path(outputs["index"]),
            "@@FRICTION_OUTPUT_PATH@@": _manifest_path(outputs["friction"]),
            "@@PRINCIPLES_MD@@": principles,
            "@@COMMENTARY_SPEC_MD@@": commentary_spec,
            "@@CHANNELS_MD@@": channels,
            "@@CANONICAL_PROMPT_V2@@": canonical_prompt,
            "@@RECONCILED_FINDINGS_JSON@@": _canonical_json(reconciled),
            "@@FOCUS_SURFACE_EVIDENCE_JSON@@": _canonical_json(
                focus_surface_evidence
            ),
            "@@MICRO_DRAFT_JSON@@": _canonical_json(drafts["micro"]),
            "@@MACRO_DRAFT_JSON@@": _canonical_json(drafts["macro"]),
            "@@GLOBAL_DRAFT_JSON@@": _canonical_json(drafts["global"]),
        },
        label="canonical merge",
    )
    prompt_path = paths["prompt"]
    manifest_path = paths["manifest"]
    manifest = _prompt_manifest(
        stage="canonical-merge",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=None,
        expected_outputs=outputs,
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, prompt_path, prompt)
    _write(V3_ROOT, manifest_path, _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "request_sha256": request_sha256,
        "prompt": str(prompt_path),
        "manifest": str(manifest_path),
        "workspace": str(layout.workspace),
        "outputs": {key: str(path) for key, path in outputs.items()},
        "receipt": str(paths["receipt"]),
    }


def _optional_confined_file(root: Path, path: Path, *, label: str) -> Path | None:
    resolved_missing = path.resolve(strict=False)
    try:
        resolved_missing.relative_to(root.resolve())
    except ValueError as exc:
        raise SystemExit(f"{label} escapes its canonical root: {path}") from exc
    if path.is_symlink():
        raise SystemExit(f"Refusing symlink {label}: {path}")
    if not path.exists():
        return None
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root.resolve())
    except (OSError, ValueError) as exc:
        raise SystemExit(f"{label} escapes its canonical root: {path}") from exc
    if not resolved.is_file():
        raise SystemExit(f"Expected {label} to be a regular file: {path}")
    try:
        payload = resolved.read_bytes()
    except OSError as exc:
        raise SystemExit(f"Cannot read {label} {path}: {exc}") from exc
    if not payload or not payload.strip():
        raise SystemExit(f"{label} is empty: {path}")
    return resolved


def _required_confined_file(root: Path, path: Path, *, label: str) -> Path:
    resolved = _optional_confined_file(root, path, label=label)
    if resolved is None:
        raise SystemExit(f"Missing {label}: {path}")
    return resolved


def _load_session_receipt(
    layout: AuthoringLayout, conversation: str, generation: str
) -> tuple[dict[str, Any] | None, Path]:
    receipt_path = _session_receipt_path(layout, conversation, generation)
    resolved = _optional_confined_file(
        layout.outputs, receipt_path, label=f"{conversation} session receipt"
    )
    if resolved is None:
        return None, receipt_path
    receipt = _load_object(resolved)
    expected_key = _conversation_key(layout, conversation, generation)
    if (
        receipt.get("schema_version")
        != "commentary-v3-authoring-session-receipt-v1"
        or receipt.get("ayah_ref") != layout.ayah_ref
        or receipt.get("conversation_key") != expected_key
        or receipt.get("conversation_generation") != generation
        or not isinstance(receipt.get("session_id"), str)
        or not receipt["session_id"].strip()
        or not isinstance(receipt.get("started_prompt_sha256"), str)
        or not re.fullmatch(r"[0-9a-f]{64}", receipt["started_prompt_sha256"])
        or not isinstance(receipt.get("started_prompt_manifest"), str)
    ):
        raise SystemExit(f"Invalid {conversation} session receipt: {resolved}")
    started_manifest_path = _absolute_manifest_path(
        receipt["started_prompt_manifest"], label="started prompt manifest"
    )
    _assert_input_path(layout, started_manifest_path, label="started prompt manifest")
    started_manifest = _load_object(
        _required_confined_file(
            layout.inputs,
            started_manifest_path,
            label="started prompt manifest",
        )
    )
    expected_start_stage = {
        "scope-micro": "scope-micro-review",
        "scope-macro": "scope-macro-review",
        "scope-global": "scope-global-review",
        "scope-reconciler": "scope-reconcile",
        "canonical-writer": "canonical-merge",
        "reader-map-writer": "reader-map",
        "invitation-writer": "invitation-summary",
    }[conversation]
    if (
        started_manifest.get("prompt_sha256")
        != receipt["started_prompt_sha256"]
        or started_manifest.get("stage") != expected_start_stage
        or started_manifest.get("ayah_ref") != layout.ayah_ref
        or started_manifest.get("authoring_request_sha256") != generation
    ):
        raise SystemExit(f"Stale {conversation} session receipt: {resolved}")
    return receipt, resolved


def _git_output(*arguments: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", *arguments],
            cwd=REPO_ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = ""
        if isinstance(exc, subprocess.CalledProcessError):
            detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise SystemExit(
            f"Cannot audit canonical-writer workspace state: {detail or exc}"
        ) from exc
    return result.stdout


def _workspace_repo_relative_path(path: Path, *, label: str) -> str:
    try:
        return str(path.resolve(strict=False).relative_to(REPO_ROOT))
    except ValueError as exc:
        raise SystemExit(f"{label} escapes the repository workspace: {path}") from exc


def _workspace_path_state(relative_path: str) -> dict[str, Any]:
    path = REPO_ROOT / relative_path
    if path.is_symlink():
        return {
            "kind": "symlink",
            "target": os.readlink(path),
        }
    if not path.exists():
        return {"kind": "missing"}
    if path.is_file():
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise SystemExit(
                f"Cannot hash workspace path {relative_path}: {exc}"
            ) from exc
        return {
            "kind": "file",
            "bytes": len(payload),
            "sha256": _sha256_bytes(payload),
        }
    if path.is_dir():
        return {"kind": "directory"}
    raise SystemExit(f"Unsupported workspace path type: {relative_path}")


def _workspace_git_visible_state(
    *, excluded_paths: set[str], excluded_prefix: str | None = None
) -> list[dict[str, Any]]:
    raw = _git_output(
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
        "--no-renames",
    )
    records: list[dict[str, Any]] = []
    for raw_record in raw.split(b"\0"):
        if not raw_record:
            continue
        if len(raw_record) < 4 or raw_record[2:3] != b" ":
            raise SystemExit("Cannot parse Git workspace status for writer audit")
        try:
            status = raw_record[:2].decode("ascii")
            relative_path = raw_record[3:].decode("utf-8")
        except UnicodeDecodeError as exc:
            raise SystemExit(
                "Canonical writer audit requires UTF-8 repository paths"
            ) from exc
        lexical_path = Path(relative_path)
        if lexical_path.is_absolute() or ".." in lexical_path.parts:
            raise SystemExit(
                f"Git reported an unsafe workspace path: {relative_path}"
            )
        if relative_path in excluded_paths or (
            excluded_prefix is not None
            and relative_path.startswith(f"{excluded_prefix}/")
        ):
            continue
        records.append(
            {
                "path": relative_path,
                "status": status,
                "state": _workspace_path_state(relative_path),
            }
        )
    records.sort(key=lambda item: item["path"])
    return records


def _workspace_output_states(
    outputs: dict[str, Path],
) -> dict[str, dict[str, Any] | None]:
    states: dict[str, dict[str, Any] | None] = {}
    for key, path in outputs.items():
        relative_path = _workspace_repo_relative_path(
            path, label=f"{key} output"
        )
        state = _workspace_path_state(relative_path)
        states[key] = None if state["kind"] == "missing" else state
    return states


def _workspace_guard_directory(manifest_path: Path) -> Path:
    return manifest_path.parent / "workspace-guards"


def _canonical_guard_auxiliary_paths(
    layout: AuthoringLayout, manifest_path: Path
) -> tuple[Path, Path]:
    manifest = _load_object(
        _required_confined_file(
            layout.inputs, manifest_path, label="canonical prompt manifest"
        )
    )
    stage = manifest.get("stage")
    request_sha256 = manifest.get("authoring_request_sha256")
    if not isinstance(request_sha256, str) or not re.fullmatch(
        r"[0-9a-f]{64}", request_sha256
    ):
        raise SystemExit("Canonical prompt manifest has an invalid request hash")
    if stage == "canonical-merge":
        conversation_generation = request_sha256
        turn_receipt = (
            layout.outputs / "merge" / request_sha256 / "turn-receipt.json"
        )
    elif stage == "canonical-editorial":
        conversation_generation = manifest.get("inputs", {}).get(
            "merge_request_sha256"
        )
        if not isinstance(conversation_generation, str) or not re.fullmatch(
            r"[0-9a-f]{64}", conversation_generation
        ):
            raise SystemExit(
                "Editorial manifest has an invalid writer conversation generation"
            )
        turn_receipt = (
            layout.outputs / "editorial" / request_sha256 / "turn-receipt.json"
        )
    else:
        raise SystemExit("Workspace guards are only valid for canonical turns")
    session_receipt = _session_receipt_path(
        layout, "canonical-writer", conversation_generation
    )
    return session_receipt, turn_receipt


def _validate_workspace_guard_shape(
    layout: AuthoringLayout,
    guard: dict[str, Any],
    guard_path: Path,
    manifest_path: Path,
    expected_outputs: dict[str, Path],
) -> None:
    expected_output_paths = {
        key: _manifest_path(path) for key, path in expected_outputs.items()
    }
    session_receipt, turn_receipt = _canonical_guard_auxiliary_paths(
        layout, manifest_path
    )
    expected_exclusions = sorted(
        {
            *(
                _workspace_repo_relative_path(path, label=f"{key} output")
                for key, path in expected_outputs.items()
            ),
            _workspace_repo_relative_path(
                session_receipt, label="canonical session receipt"
            ),
            _workspace_repo_relative_path(
                turn_receipt, label="canonical turn receipt"
            ),
        }
    )
    initial_outputs = guard.get("initial_outputs")
    initial_auxiliary_states = guard.get("initial_auxiliary_states")
    if (
        guard.get("schema_version")
        != "commentary-v3-canonical-workspace-guard-v1"
        or guard.get("ayah_ref") != layout.ayah_ref
        or guard.get("prompt_manifest") != _manifest_path(manifest_path)
        or guard.get("expected_outputs") != expected_output_paths
        or not isinstance(initial_outputs, dict)
        or set(initial_outputs) != set(expected_outputs)
        or not isinstance(initial_auxiliary_states, dict)
        or set(initial_auxiliary_states)
        != {"session_receipt", "turn_receipt"}
        or guard.get("initial_present_count")
        != sum(value is not None for value in initial_outputs.values())
        or guard.get("guard_directory")
        != _manifest_path(_workspace_guard_directory(manifest_path))
        or guard.get("excluded_write_paths") != expected_exclusions
        or not isinstance(guard.get("baseline_git_visible_state"), list)
        or not isinstance(guard.get("head_commit"), str)
        or not re.fullmatch(r"[0-9a-f]{40,64}", guard["head_commit"])
        or guard_path.parent.resolve(strict=False)
        != _workspace_guard_directory(manifest_path).resolve(strict=False)
        or guard_path.name != f"{_sha256_json(guard)}.json"
    ):
        raise SystemExit(f"Malformed canonical workspace guard: {guard_path}")


def _verify_workspace_guard(
    layout: AuthoringLayout,
    guard_path: Path,
    manifest_path: Path,
    expected_outputs: dict[str, Path],
) -> dict[str, Any]:
    guard_path = _required_confined_file(
        layout.inputs, guard_path, label="canonical workspace guard"
    )
    guard = _load_object(guard_path)
    _validate_workspace_guard_shape(
        layout, guard, guard_path, manifest_path, expected_outputs
    )
    head_commit = _git_output("rev-parse", "HEAD").decode("ascii").strip()
    if head_commit != guard["head_commit"]:
        raise SystemExit("Repository HEAD changed during canonical writer turn")
    excluded_paths = set(guard["excluded_write_paths"])
    excluded_paths.add(
        _workspace_repo_relative_path(
            guard_path, label="canonical workspace guard"
        )
    )
    current_state = _workspace_git_visible_state(
        excluded_paths=excluded_paths,
    )
    if _canonical_json(current_state) != _canonical_json(
        guard["baseline_git_visible_state"]
    ):
        before = {
            item.get("path"): item for item in guard["baseline_git_visible_state"]
            if isinstance(item, dict)
        }
        after = {item["path"]: item for item in current_state}
        changed = sorted(
            path
            for path in set(before) | set(after)
            if before.get(path) != after.get(path)
        )
        raise SystemExit(
            "Canonical writer changed Git-visible workspace paths outside its "
            f"declared outputs: {changed}"
        )
    current_outputs = _workspace_output_states(expected_outputs)
    changed_initial_outputs = sorted(
        key
        for key, initial_state in guard["initial_outputs"].items()
        if initial_state is not None and current_outputs[key] != initial_state
    )
    if changed_initial_outputs:
        raise SystemExit(
            "Canonical writer changed outputs already present before its current "
            f"handoff: {changed_initial_outputs}"
        )
    session_receipt, turn_receipt = _canonical_guard_auxiliary_paths(
        layout, manifest_path
    )
    current_auxiliary_states = _workspace_output_states(
        {
            "session_receipt": session_receipt,
            "turn_receipt": turn_receipt,
        }
    )
    changed_initial_auxiliary = sorted(
        key
        for key, initial_state in guard["initial_auxiliary_states"].items()
        if initial_state is not None
        and current_auxiliary_states[key] != initial_state
    )
    if changed_initial_auxiliary:
        raise SystemExit(
            "Canonical writer turn changed a pre-existing session/turn "
            f"receipt: {changed_initial_auxiliary}"
        )
    return guard


def _workspace_guard_candidates(manifest_path: Path) -> list[Path]:
    guard_directory = _workspace_guard_directory(manifest_path)
    if not guard_directory.exists():
        return []
    return sorted(guard_directory.glob("*.json"))


def _active_workspace_guard(
    layout: AuthoringLayout,
    manifest_path: Path,
    expected_outputs: dict[str, Path],
    *,
    verify_current: bool = True,
) -> tuple[dict[str, Any], Path] | None:
    candidates: list[tuple[dict[str, Any], Path]] = []
    for guard_path in _workspace_guard_candidates(manifest_path):
        guard = _load_object(
            _required_confined_file(
                layout.inputs, guard_path, label="canonical workspace guard"
            )
        )
        _validate_workspace_guard_shape(
            layout, guard, guard_path, manifest_path, expected_outputs
        )
        candidates.append((guard, guard_path))
    if not candidates:
        return None
    if len(candidates) != 1:
        raise SystemExit(
            "A canonical turn must have exactly one externally anchored "
            "workspace guard"
        )
    guard, guard_path = candidates[0]
    if verify_current:
        _verify_workspace_guard(
            layout, guard_path, manifest_path, expected_outputs
        )
    return guard, guard_path


def _ensure_workspace_guard(
    layout: AuthoringLayout,
    manifest_path: Path,
    expected_outputs: dict[str, Path],
    session_receipt_path: Path,
    turn_receipt: Path,
) -> Path:
    expected_session_receipt, expected_turn_receipt = (
        _canonical_guard_auxiliary_paths(layout, manifest_path)
    )
    if (
        session_receipt_path.resolve(strict=False)
        != expected_session_receipt.resolve(strict=False)
        or turn_receipt.resolve(strict=False)
        != expected_turn_receipt.resolve(strict=False)
    ):
        raise SystemExit("Canonical workspace guard received stale auxiliary paths")
    active = _active_workspace_guard(
        layout, manifest_path, expected_outputs, verify_current=True
    )
    if active is not None:
        _active_guard, active_path = active
        return active_path

    guard_directory = _workspace_guard_directory(manifest_path)
    _assert_input_path(layout, guard_directory, label="workspace guard directory")
    expected_output_paths = {
        key: _manifest_path(path) for key, path in expected_outputs.items()
    }
    excluded_write_paths = sorted(
        {
            *(
                _workspace_repo_relative_path(path, label=f"{key} output")
                for key, path in expected_outputs.items()
            ),
            _workspace_repo_relative_path(
                session_receipt_path, label="canonical session receipt"
            ),
            _workspace_repo_relative_path(
                turn_receipt, label="canonical turn receipt"
            ),
        }
    )
    current_outputs = _workspace_output_states(expected_outputs)
    current_present = sum(value is not None for value in current_outputs.values())
    guard = {
        "schema_version": "commentary-v3-canonical-workspace-guard-v1",
        "ayah_ref": layout.ayah_ref,
        "prompt_manifest": _manifest_path(manifest_path),
        "expected_outputs": expected_output_paths,
        "excluded_write_paths": excluded_write_paths,
        "guard_directory": _manifest_path(guard_directory),
        "head_commit": _git_output("rev-parse", "HEAD").decode("ascii").strip(),
        "initial_outputs": current_outputs,
        "initial_present_count": current_present,
        "initial_auxiliary_states": _workspace_output_states(
            {
                "session_receipt": session_receipt_path,
                "turn_receipt": turn_receipt,
            }
        ),
        "baseline_git_visible_state": _workspace_git_visible_state(
            excluded_paths=set(excluded_write_paths),
        ),
    }
    guard_sha256 = _sha256_json(guard)
    guard_path = guard_directory / f"{guard_sha256}.json"
    _write(V3_ROOT, guard_path, _pretty_json(guard))
    return guard_path


def _generated_prompt_handoff(
    layout: AuthoringLayout,
    *,
    role: str,
    conversation: str,
    conversation_generation: str,
    prompt_path: Path,
    manifest_path: Path,
    expected_response: Path | None = None,
    expected_outputs: dict[str, Path] | None = None,
    workspace_access: str = "read_only",
    require_resume: bool = False,
    turn_receipt: Path | None = None,
) -> dict[str, Any]:
    _assert_input_path(layout, prompt_path, label=f"{role} prompt")
    _assert_input_path(layout, manifest_path, label=f"{role} prompt manifest")
    prompt_path = _required_confined_file(
        layout.inputs, prompt_path, label=f"{role} prompt"
    )
    manifest_path = _required_confined_file(
        layout.inputs, manifest_path, label=f"{role} prompt manifest"
    )
    manifest = _load_object(manifest_path)
    prompt_payload = prompt_path.read_bytes()
    try:
        prompt_text = prompt_payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"{role} prompt is not UTF-8") from exc
    if (
        manifest.get("prompt_sha256") != _sha256_bytes(prompt_payload)
        or manifest.get("prompt_bytes") != len(prompt_payload)
    ):
        raise SystemExit(f"{role} prompt does not match its manifest")
    if expected_response is not None:
        _assert_output_path(layout, expected_response, label=f"{role} response")
        if manifest.get("expected_response") != _manifest_path(expected_response):
            raise SystemExit(f"{role} response path does not match its manifest")
        _prepare_output_parent(
            layout, expected_response, label=f"{role} response"
        )
    if expected_outputs is not None:
        for key, path in expected_outputs.items():
            _assert_output_path(layout, path, label=f"{role} {key} output")
            _prepare_output_parent(
                layout, path, label=f"{role} {key} output"
            )
    if expected_outputs is not None and manifest.get("expected_outputs") != {
        key: _manifest_path(path) for key, path in expected_outputs.items()
    }:
        raise SystemExit(f"{role} output paths do not match their manifest")
    if turn_receipt is not None:
        _assert_output_path(layout, turn_receipt, label=f"{role} turn receipt")
        _prepare_output_parent(
            layout, turn_receipt, label=f"{role} turn receipt"
        )
    session_receipt, session_receipt_path = _load_session_receipt(
        layout, conversation, conversation_generation
    )
    if require_resume and session_receipt is None:
        raise SystemExit(
            f"Cannot issue {role} follow-up without persisted {conversation} session"
        )
    conversation_action = "resume" if session_receipt is not None else "start"
    workspace_guard_path: Path | None = None
    workspace_guard_bytes_sha256: str | None = None
    preexisting_output_states: dict[str, dict[str, Any] | None] | None = None
    preexisting_auxiliary_states: dict[str, dict[str, Any] | None] | None = None
    if expected_outputs is not None:
        if turn_receipt is None:
            raise SystemExit(
                f"{role} requires a declared turn receipt for workspace audit"
            )
        workspace_guard_path = _ensure_workspace_guard(
            layout,
            manifest_path,
            expected_outputs,
            session_receipt_path,
            turn_receipt,
        )
        workspace_guard_bytes_sha256 = _sha256_bytes(
            workspace_guard_path.read_bytes()
        )
        preexisting_output_states = _workspace_output_states(expected_outputs)
        preexisting_auxiliary_states = _workspace_output_states(
            {
                "session_receipt": session_receipt_path,
                "turn_receipt": turn_receipt,
            }
        )
    return {
        "role": role,
        "conversation_key": _conversation_key(
            layout, conversation, conversation_generation
        ),
        "conversation_generation": conversation_generation,
        "conversation_action": conversation_action,
        "session_id": (
            session_receipt["session_id"] if session_receipt is not None else None
        ),
        "session_receipt": str(session_receipt_path),
        "session_record_command": (
            [
                "python3",
                "_commentary/v3/workflow.py",
                "authoring-record-session",
                "--ayah",
                layout.ayah_ref,
                "--conversation",
                conversation,
                "--session-id",
                "<returned-session-id>",
                "--prompt-manifest",
                str(manifest_path),
            ]
            if session_receipt is None
            else None
        ),
        "prompt_delivery": "absolute_path_only",
        "prompt_path": str(prompt_path),
        "prompt_sha256": manifest["prompt_sha256"],
        "prompt_bytes": manifest["prompt_bytes"],
        "prompt_characters": len(prompt_text),
        "estimated_tokens_chars_div_4": (len(prompt_text) + 3) // 4,
        "embedded_json_encoding": "canonical-minified-utf8",
        "prompt_manifest": str(manifest_path),
        "expected_response": (
            str(expected_response.resolve(strict=False))
            if expected_response is not None
            else None
        ),
        "expected_outputs": (
            {
                key: str(path.resolve(strict=False))
                for key, path in expected_outputs.items()
            }
            if expected_outputs is not None
            else None
        ),
        "working_directory": str(layout.workspace),
        "workspace_access": workspace_access,
        "declared_output_enforcement": (
            "git_visible_pre_post_guard"
            if workspace_guard_path is not None
            else None
        ),
        "workspace_guard": (
            str(workspace_guard_path)
            if workspace_guard_path is not None
            else None
        ),
        "workspace_guard_bytes_sha256": workspace_guard_bytes_sha256,
        "preexisting_output_states": preexisting_output_states,
        "preexisting_auxiliary_states": preexisting_auxiliary_states,
        "turn_receipt": str(turn_receipt) if turn_receipt is not None else None,
        "session_persistence_required": True,
        "ephemeral_session_forbidden": True,
        "operator_instruction": (
            "Give the agent only this absolute prompt path and instruct it to "
            "read the file completely. Do not pipe or inline prompt contents. "
            "When starting, persist the returned session ID at the declared "
            "session-receipt path before accepting model output. When resuming, "
            "use exactly the persisted session ID."
            + (
                " For this workspace-write turn, permit changes only at the "
                "declared output paths; turn recording will enforce the "
                "returned pre-turn workspace guard. Retain the guard path, "
                "guard byte hash, and preexisting output/auxiliary states "
                "outside the worker session and compare them before recording "
                "the turn."
                if workspace_guard_path is not None
                else ""
            )
        ),
    }


def _editorial_output_path(path: Path) -> Path:
    name = path.name
    if name.endswith(".tr.md"):
        return path.with_name(f"{name[:-6]}.editorial.tr.md")
    if name.endswith(".md"):
        return path.with_name(f"{name[:-3]}.editorial.md")
    raise SystemExit(f"Cannot derive editorial output path from: {path}")


def _output_records(
    layout: AuthoringLayout, outputs: dict[str, Path], *, label: str
) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for key, path in outputs.items():
        _assert_output_path(layout, path, label=f"{label} {key} output")
        resolved = _required_confined_file(
            layout.outputs, path, label=f"{label} {key} output"
        )
        payload = resolved.read_bytes()
        records[key] = {
            "path": _manifest_path(resolved),
            "bytes": len(payload),
            "sha256": _sha256_bytes(payload),
        }
    return records


def _active_locked_refs_for_canonical_manifest(
    layout: AuthoringLayout,
    manifest: dict[str, Any],
) -> set[str]:
    """Resolve the locked ledger by its merge-bound canonical JSON hash."""

    merge_manifest = manifest
    if manifest.get("stage") == "canonical-editorial":
        merge_request = manifest.get("inputs", {}).get("merge_request_sha256")
        if not isinstance(merge_request, str) or not re.fullmatch(
            r"[0-9a-f]{64}", merge_request
        ):
            raise SystemExit("Editorial manifest lacks a valid merge request")
        merge_manifest_path = layout.inputs / "merge" / merge_request / "manifest.json"
        merge_manifest = _load_object(
            _required_confined_file(
                layout.inputs,
                merge_manifest_path,
                label="editorial merge prompt manifest",
            )
        )
    if (
        merge_manifest.get("stage") != "canonical-merge"
        or merge_manifest.get("ayah_ref") != layout.ayah_ref
    ):
        raise SystemExit("Canonical outputs are not bound to a valid merge manifest")
    reconciled_sha256 = merge_manifest.get("inputs", {}).get(
        "reconciled_sha256"
    )
    if not isinstance(reconciled_sha256, str) or not re.fullmatch(
        r"[0-9a-f]{64}", reconciled_sha256
    ):
        raise SystemExit("Canonical merge manifest lacks a reconciliation hash")

    matches: list[dict[str, Any]] = []
    reconcile_root = layout.outputs / "reconcile"
    if reconcile_root.exists():
        for candidate_path in sorted(reconcile_root.glob("*/reconciled.json")):
            try:
                candidate_path = _required_confined_file(
                    layout.outputs,
                    candidate_path,
                    label="candidate reconciled finding ledger",
                )
                candidate = _load_object(candidate_path)
            except SystemExit:
                # Obsolete malformed generations are not active lineage. The
                # active hash still has to resolve exactly below.
                continue
            if _sha256_json(candidate) == reconciled_sha256:
                matches.append(candidate)
    if not matches:
        raise SystemExit(
            "Cannot resolve the canonical merge's active reconciled finding ledger"
        )
    reconciled = matches[0]
    if reconciled.get("ayah_ref") != layout.ayah_ref:
        raise SystemExit("Canonical merge resolves a stale reconciliation")
    locked_by_ref, _assignments = _locked_finding_assignments(reconciled)
    return set(locked_by_ref)


def _locked_ref_occurrence_counts(
    text: str, expected_refs: set[str]
) -> dict[str, int]:
    extracted = _extract_locked_ref_tokens(text)
    return {locked_ref: extracted.count(locked_ref) for locked_ref in expected_refs}


def _validate_canonical_locked_finding_accounting(
    layout: AuthoringLayout,
    manifest: dict[str, Any],
    outputs: dict[str, Path],
) -> None:
    """Require complete index/evidence ledgers without judging reader prose."""

    expected_refs = _active_locked_refs_for_canonical_manifest(layout, manifest)
    texts: dict[str, str] = {}
    for key in ("index", "evidence"):
        path = _required_confined_file(
            layout.outputs,
            outputs[key],
            label=f"canonical {key} output",
        )
        try:
            texts[key] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise SystemExit(f"Cannot read canonical {key} output: {exc}") from exc
        actual_tokens = set(_extract_locked_ref_tokens(texts[key]))
        unknown = sorted(actual_tokens - expected_refs)
        if unknown:
            raise SystemExit(
                f"Canonical {key} output invents locked finding refs: {unknown}"
            )

    index_counts = _locked_ref_occurrence_counts(texts["index"], expected_refs)
    missing_index = sorted(ref for ref, count in index_counts.items() if count == 0)
    repeated_index = sorted(ref for ref, count in index_counts.items() if count > 1)
    if missing_index or repeated_index:
        raise SystemExit(
            "Canonical index must name every active locked finding exactly once; "
            f"missing={missing_index}, repeated={repeated_index}"
        )

    evidence_counts = _locked_ref_occurrence_counts(
        texts["evidence"], expected_refs
    )
    missing_evidence = sorted(
        ref for ref, count in evidence_counts.items() if count == 0
    )
    if missing_evidence:
        raise SystemExit(
            "Canonical evidence must account for every active locked finding; "
            f"missing={missing_evidence}"
        )


def record_authoring_session(args: argparse.Namespace) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    manifest_path = _assert_input_path(
        layout, args.prompt_manifest, label="session-start prompt manifest"
    )
    manifest_path = _required_confined_file(
        layout.inputs, manifest_path, label="session-start prompt manifest"
    )
    manifest = _load_object(manifest_path)
    expected_start_stage = {
        "scope-micro": "scope-micro-review",
        "scope-macro": "scope-macro-review",
        "scope-global": "scope-global-review",
        "scope-reconciler": "scope-reconcile",
        "canonical-writer": "canonical-merge",
        "reader-map-writer": "reader-map",
        "invitation-writer": "invitation-summary",
    }[args.conversation]
    generation = manifest.get("authoring_request_sha256")
    if (
        manifest.get("ayah_ref") != args.ayah
        or manifest.get("stage") != expected_start_stage
        or not isinstance(generation, str)
        or not re.fullmatch(r"[0-9a-f]{64}", generation)
    ):
        raise SystemExit(
            f"{args.conversation} must start from its exact {expected_start_stage} "
            "manifest for this ayah"
        )
    prompt_path = manifest_path.with_name("prompt.md")
    prompt_path = _required_confined_file(
        layout.inputs, prompt_path, label="session-start prompt"
    )
    prompt_payload = prompt_path.read_bytes()
    if manifest.get("prompt_sha256") != _sha256_bytes(prompt_payload):
        raise SystemExit("Session-start prompt does not match its manifest")
    session_id = args.session_id.strip()
    if not session_id:
        raise SystemExit("--session-id must be nonempty")
    conversation_key = _conversation_key(
        layout, args.conversation, generation
    )
    if AUTHORING_OUTPUTS_ROOT.exists():
        for existing_path in AUTHORING_OUTPUTS_ROOT.rglob("sessions/*/*.json"):
            existing = _load_object(
                _required_confined_file(
                    AUTHORING_OUTPUTS_ROOT,
                    existing_path,
                    label="existing authoring session receipt",
                )
            )
            if (
                existing.get("session_id") == session_id
                and existing.get("conversation_key") != conversation_key
            ):
                raise SystemExit(
                    "One executor session cannot back independent authoring "
                    "conversations"
                )
    receipt = {
        "schema_version": "commentary-v3-authoring-session-receipt-v1",
        "ayah_ref": args.ayah,
        "conversation_key": conversation_key,
        "conversation_generation": generation,
        "session_id": session_id,
        "started_prompt_manifest": _manifest_path(manifest_path),
        "started_prompt_sha256": manifest["prompt_sha256"],
    }
    receipt_path = _session_receipt_path(
        layout, args.conversation, generation
    )
    _write(V3_ROOT, receipt_path, _pretty_json(receipt))
    return {
        "status": "recorded",
        "ayah_ref": args.ayah,
        "conversation_key": receipt["conversation_key"],
        "session_receipt": str(receipt_path),
    }


def _expected_turn_receipt(
    layout: AuthoringLayout,
    manifest_path: Path,
    conversation: str,
    *,
    prior_receipt: Path | None = None,
    require_workspace_guard: bool = False,
) -> tuple[dict[str, Any], Path]:
    manifest_path = _required_confined_file(
        layout.inputs, manifest_path, label="turn prompt manifest"
    )
    manifest = _load_object(manifest_path)
    if manifest.get("stage") not in {"canonical-merge", "canonical-editorial"}:
        raise SystemExit("Turn receipts are only valid for canonical prose phases")
    prompt_path = _required_confined_file(
        layout.inputs,
        manifest_path.with_name("prompt.md"),
        label="turn prompt",
    )
    prompt_payload = prompt_path.read_bytes()
    if (
        manifest.get("ayah_ref") != layout.ayah_ref
        or manifest.get("prompt_sha256") != _sha256_bytes(prompt_payload)
        or manifest.get("prompt_bytes") != len(prompt_payload)
    ):
        raise SystemExit("Canonical turn prompt does not match its manifest")
    if manifest["stage"] == "canonical-merge" and prior_receipt is not None:
        raise SystemExit("Canonical merge must not carry a prior turn receipt")
    if manifest["stage"] == "canonical-editorial" and prior_receipt is None:
        raise SystemExit("Canonical editorial requires its exact merge receipt")
    outputs_value = manifest.get("expected_outputs")
    if not isinstance(outputs_value, dict) or set(outputs_value) != {
        "prose",
        "evidence",
        "index",
        "friction",
    }:
        raise SystemExit("Canonical prompt manifest lacks exact declared outputs")
    outputs = {
        key: _absolute_manifest_path(value, label=f"{key} output")
        for key, value in outputs_value.items()
    }
    conversation_generation = (
        manifest.get("authoring_request_sha256")
        if manifest.get("stage") == "canonical-merge"
        else manifest.get("inputs", {}).get("merge_request_sha256")
    )
    session, _session_path = _load_session_receipt(
        layout, conversation, conversation_generation
    )
    if session is None:
        raise SystemExit("Cannot record a turn without a persisted session receipt")
    prior_record: dict[str, Any] | None = None
    if prior_receipt is not None:
        prior_path = _required_confined_file(
            layout.outputs, prior_receipt, label="prior turn receipt"
        )
        prior_payload = prior_path.read_bytes()
        prior = _load_object(prior_path)
        if (
            prior.get("schema_version")
            != "commentary-v3-authoring-turn-receipt-v1"
            or prior.get("stage") != "canonical-merge"
            or prior.get("ayah_ref") != layout.ayah_ref
            or prior.get("authoring_request_sha256")
            != manifest.get("inputs", {}).get("merge_request_sha256")
            or _sha256_bytes(prior_payload)
            != manifest.get("inputs", {}).get("merge_receipt_sha256")
            or _sha256_json(prior.get("outputs"))
            != manifest.get("inputs", {}).get("first_pass_outputs_sha256")
        ):
            raise SystemExit("Editorial manifest is not bound to its exact merge receipt")
        prior_outputs = prior.get("outputs")
        if not isinstance(prior_outputs, dict) or set(prior_outputs) != set(outputs):
            raise SystemExit("Merge receipt has malformed first-pass outputs")
        expected_editorial_paths: dict[str, Path] = {}
        for key, record in prior_outputs.items():
            if not isinstance(record, dict):
                raise SystemExit("Merge receipt output record is malformed")
            first_path = _absolute_manifest_path(
                record.get("path"), label=f"first-pass {key} output"
            )
            first_payload = _required_confined_file(
                layout.outputs, first_path, label=f"first-pass {key} output"
            ).read_bytes()
            if (
                record.get("bytes") != len(first_payload)
                or record.get("sha256") != _sha256_bytes(first_payload)
            ):
                raise SystemExit(
                    "First-pass output changed after its immutable merge receipt"
                )
            expected_editorial_paths[key] = _editorial_output_path(first_path)
        if {
            key: path.resolve(strict=False) for key, path in outputs.items()
        } != {
            key: path.resolve(strict=False)
            for key, path in expected_editorial_paths.items()
        }:
            raise SystemExit(
                "Editorial output paths are not the canonical first-pass counterparts"
            )
        prior_record = {
            "path": _manifest_path(prior_path),
            "sha256": _sha256_bytes(prior_payload),
        }
    _validate_canonical_locked_finding_accounting(layout, manifest, outputs)
    active_workspace_guard = _active_workspace_guard(
        layout,
        manifest_path,
        outputs,
        verify_current=require_workspace_guard,
    )
    if require_workspace_guard and active_workspace_guard is None:
        raise SystemExit(
            "Cannot notarize a new canonical turn without its pre-turn "
            "workspace guard"
        )
    receipt = {
        "schema_version": "commentary-v3-authoring-turn-receipt-v1",
        "ayah_ref": layout.ayah_ref,
        "stage": manifest["stage"],
        "conversation_key": session["conversation_key"],
        "conversation_generation": session["conversation_generation"],
        "session_id": session["session_id"],
        "authoring_request_sha256": manifest["authoring_request_sha256"],
        "prompt_manifest": _manifest_path(manifest_path),
        "prompt_sha256": manifest["prompt_sha256"],
        "prior_turn_receipt": prior_record,
        "outputs": _output_records(layout, outputs, label=manifest["stage"]),
    }
    if active_workspace_guard is not None:
        _guard, guard_path = active_workspace_guard
        guard_payload = guard_path.read_bytes()
        receipt["workspace_guard"] = {
            "path": _manifest_path(guard_path),
            "sha256": _sha256_bytes(guard_payload),
        }
    if manifest["stage"] == "canonical-merge":
        receipt_path = (
            layout.outputs
            / "merge"
            / manifest["authoring_request_sha256"]
            / "turn-receipt.json"
        )
    else:
        receipt_path = (
            layout.outputs
            / "editorial"
            / manifest["authoring_request_sha256"]
            / "turn-receipt.json"
        )
    return receipt, receipt_path


def record_authoring_turn(args: argparse.Namespace) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    manifest_path = _assert_input_path(
        layout, args.prompt_manifest, label="turn prompt manifest"
    )
    prior_receipt = getattr(args, "prior_receipt", None)
    receipt, receipt_path = _expected_turn_receipt(
        layout,
        manifest_path,
        "canonical-writer",
        prior_receipt=prior_receipt,
        require_workspace_guard=True,
    )
    if args.session_id != receipt["session_id"]:
        raise SystemExit("--session-id does not match the canonical writer receipt")
    _write(V3_ROOT, receipt_path, _pretty_json(receipt))
    return {
        "status": "recorded",
        "ayah_ref": args.ayah,
        "stage": receipt["stage"],
        "turn_receipt": str(receipt_path),
        "outputs": receipt["outputs"],
    }


def _legacy_completions_attesting_guardless_receipt(
    layout: AuthoringLayout, receipt_path: Path
) -> list[Path]:
    """Return every old completion that sealed a guardless receipt."""

    completion_root = layout.outputs / "completion"
    if not completion_root.exists():
        return []
    receipt_payload = _required_confined_file(
        layout.outputs, receipt_path, label="legacy canonical turn receipt"
    ).read_bytes()
    receipt_record = {
        "path": _manifest_path(receipt_path),
        "bytes": len(receipt_payload),
        "sha256": _sha256_bytes(receipt_payload),
    }
    attesting_paths: list[Path] = []
    for completion_path in sorted(completion_root.glob("*/COMPLETION.json")):
        completion_path = _required_confined_file(
            layout.outputs,
            completion_path,
            label="legacy authoring completion manifest",
        )
        completion = _load_object(completion_path)
        if (
            completion.get("schema_version")
            != "commentary-v3-authoring-completion-v2"
            or completion.get("ayah_ref") != layout.ayah_ref
            or completion_path.parent.name != _sha256_json(completion)
        ):
            continue
        lineage = completion.get("lineage")
        if not isinstance(lineage, list) or receipt_record not in lineage:
            continue
        phase_receipts = completion.get("phase_receipts")
        if (
            not isinstance(phase_receipts, dict)
            or set(phase_receipts)
            != {"canonical_merge", "canonical_editorial"}
            or receipt_record["path"] not in set(phase_receipts.values())
        ):
            continue
        lineage_by_path = {
            item.get("path"): item
            for item in lineage
            if isinstance(item, dict) and isinstance(item.get("path"), str)
        }
        phase_receipts_valid = True
        for phase_path_value in phase_receipts.values():
            phase_path = _absolute_manifest_path(
                phase_path_value, label="legacy phase receipt"
            )
            phase_payload = _required_confined_file(
                layout.outputs,
                phase_path,
                label="legacy phase receipt",
            ).read_bytes()
            if lineage_by_path.get(phase_path_value) != {
                "path": phase_path_value,
                "bytes": len(phase_payload),
                "sha256": _sha256_bytes(phase_payload),
            }:
                phase_receipts_valid = False
                break
        if not phase_receipts_valid:
            continue
        outputs = completion.get("outputs")
        if not isinstance(outputs, dict) or len(outputs) != 8:
            continue
        outputs_valid = True
        for key, record in outputs.items():
            if not isinstance(key, str) or not isinstance(record, dict):
                outputs_valid = False
                break
            output_path = _absolute_manifest_path(
                record.get("path"), label="legacy completed output"
            )
            output_payload = _required_confined_file(
                layout.outputs,
                output_path,
                label="legacy completed output",
            ).read_bytes()
            if (
                record.get("bytes") != len(output_payload)
                or record.get("sha256") != _sha256_bytes(output_payload)
            ):
                outputs_valid = False
                break
        if outputs_valid:
            attesting_paths.append(completion_path)
    return attesting_paths


def _load_verified_turn_receipt(
    layout: AuthoringLayout,
    manifest_path: Path,
    receipt_path: Path,
    *,
    prior_receipt: Path | None = None,
    legacy_completion_paths: list[Path] | None = None,
) -> dict[str, Any] | None:
    resolved = _optional_confined_file(
        layout.outputs, receipt_path, label="canonical turn receipt"
    )
    if resolved is None:
        return None
    expected, expected_path = _expected_turn_receipt(
        layout,
        manifest_path,
        "canonical-writer",
        prior_receipt=prior_receipt,
    )
    if expected_path.resolve(strict=False) != resolved:
        raise SystemExit("Canonical turn receipt path is inconsistent")
    actual = _load_object(resolved)
    if _canonical_json(actual) != _canonical_json(expected):
        raise SystemExit("Canonical turn receipt is stale or output hashes changed")
    if "workspace_guard" not in actual:
        attesting_paths = _legacy_completions_attesting_guardless_receipt(
            layout, resolved
        )
        if not attesting_paths:
            raise SystemExit(
                "A guardless canonical receipt is admissible only as an immutable "
                "pre-guard completed lineage"
            )
        if legacy_completion_paths is not None:
            legacy_completion_paths.extend(attesting_paths)
    return actual


def _render_editorial(
    args: argparse.Namespace,
    merge_result: dict[str, Any],
    merge_receipt: dict[str, Any],
) -> dict[str, Any]:
    layout = _authoring_layout(args.ayah)
    template = _read_prompt("editorial-followup.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    merge_receipt_path = Path(merge_result["receipt"])
    merge_receipt_payload = merge_receipt_path.read_bytes()
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        "merge_request_sha256": merge_result["request_sha256"],
        "merge_receipt_sha256": _sha256_bytes(merge_receipt_payload),
        "first_pass_outputs_sha256": _sha256_json(merge_receipt["outputs"]),
    }
    request_sha256 = _request_sha256("canonical-editorial", request_inputs)
    first_pass_outputs = {
        key: Path(value) for key, value in merge_result["outputs"].items()
    }
    paths = _editorial_paths(
        layout, request_sha256, first_pass_outputs
    )
    manifest = _prompt_manifest(
        stage="canonical-editorial",
        ayah_ref=args.ayah,
        prompt=template,
        expected_response=None,
        expected_outputs=paths["outputs"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["prompt"], template)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "request_sha256": request_sha256,
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "workspace": str(layout.workspace),
        "outputs": {key: str(path) for key, path in paths["outputs"].items()},
        "receipt": str(paths["receipt"]),
        "prior_receipt": str(merge_receipt_path),
    }


def _editorial_surprise_rows(index_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for line in index_text.splitlines():
        match = SURPRISE_INDEX_ROW_RE.match(line)
        if match is None:
            continue
        surprise_ref = match.group(1)
        if surprise_ref in seen:
            raise SystemExit(
                f"Editorial index repeats surprise ref: {surprise_ref}"
            )
        seen.add(surprise_ref)
        rows.append({"surprise_ref": surprise_ref, "index_row": line.strip()})
    return rows


def _editorial_paragraph_inventory(
    *,
    ayah_ref: str,
    editorial_prose: str,
    editorial_index: str,
    editorial_prose_sha256: str,
    editorial_index_sha256: str,
) -> dict[str, Any]:
    """Assign stable movement and paragraph keys without rewriting Markdown."""

    document_heading: dict[str, Any] | None = None
    movements: list[dict[str, Any]] = []
    paragraphs: list[dict[str, Any]] = []
    current_movement: dict[str, Any] | None = None
    paragraph_lines: list[str] = []

    def start_movement(heading_match: re.Match[str] | None) -> dict[str, Any]:
        movement_key = f"m{len(movements) + 1:03d}"
        heading = (
            None
            if heading_match is None
            else {
                "level": len(heading_match.group(1)),
                "text": heading_match.group(2).strip(),
                "markdown": heading_match.group(0).strip(),
            }
        )
        movement = {
            "movement_key": movement_key,
            "heading": heading,
            "paragraph_keys": [],
        }
        movements.append(movement)
        return movement

    def flush_paragraph() -> None:
        nonlocal current_movement, paragraph_lines
        if not paragraph_lines:
            return
        paragraph_text = "\n".join(paragraph_lines)
        if not paragraph_text.strip():
            paragraph_lines = []
            return
        if current_movement is None:
            current_movement = start_movement(None)
        paragraph_key = f"p{len(paragraphs) + 1:03d}"
        current_movement["paragraph_keys"].append(paragraph_key)
        paragraphs.append(
            {
                "paragraph_key": paragraph_key,
                "movement_key": current_movement["movement_key"],
                "ordinal": len(paragraphs) + 1,
                "text": paragraph_text,
            }
        )
        paragraph_lines = []

    for line in editorial_prose.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            raise SystemExit(
                "Editorial prose contains a fenced block that cannot be mapped "
                "as reader paragraphs"
            )
        heading_match = ATX_HEADING_RE.match(line.strip())
        if heading_match is not None:
            flush_paragraph()
            is_document_heading = (
                document_heading is None
                and not movements
                and not paragraphs
                and len(heading_match.group(1)) == 1
            )
            if is_document_heading:
                document_heading = {
                    "level": 1,
                    "text": heading_match.group(2).strip(),
                    "markdown": heading_match.group(0).strip(),
                }
                continue
            if (
                current_movement is not None
                and not current_movement["paragraph_keys"]
            ):
                raise SystemExit(
                    "Editorial prose has a movement heading without prose"
                )
            current_movement = start_movement(heading_match)
            continue
        if not line.strip():
            flush_paragraph()
            continue
        paragraph_lines.append(line)
    flush_paragraph()
    if current_movement is not None and not current_movement["paragraph_keys"]:
        raise SystemExit("Editorial prose ends with an empty movement")
    if not paragraphs:
        raise SystemExit("Editorial prose has no mappable paragraphs")

    return {
        "schema_version": "commentary-v3-editorial-paragraph-inventory-v1",
        "identity": {
            "ayah_ref": ayah_ref,
            "editorial_prose_sha256": editorial_prose_sha256,
            "editorial_index_sha256": editorial_index_sha256,
        },
        "document_heading": document_heading,
        "movements": movements,
        "paragraphs": paragraphs,
        "surprise_rows": _editorial_surprise_rows(editorial_index),
    }


def _render_reader_map(
    args: argparse.Namespace,
    editorial_result: dict[str, Any],
    editorial_receipt: dict[str, Any],
) -> dict[str, Any]:
    """Render a fresh presentation-mapping handoff from editorial artifacts."""

    layout = _authoring_layout(args.ayah)
    editorial_outputs = {
        key: Path(value) for key, value in editorial_result["outputs"].items()
    }
    prose_path = _required_confined_file(
        layout.outputs,
        editorial_outputs["prose"],
        label="editorial prose reader-map source",
    )
    index_path = _required_confined_file(
        layout.outputs,
        editorial_outputs["index"],
        label="editorial index reader-map source",
    )
    try:
        prose_payload = prose_path.read_bytes()
        index_payload = index_path.read_bytes()
        editorial_prose = prose_payload.decode("utf-8")
        editorial_index = index_payload.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit(f"Cannot read reader-map source artifacts: {exc}") from exc

    prose_sha256 = _sha256_bytes(prose_payload)
    index_sha256 = _sha256_bytes(index_payload)
    inventory = _editorial_paragraph_inventory(
        ayah_ref=args.ayah,
        editorial_prose=editorial_prose,
        editorial_index=editorial_index,
        editorial_prose_sha256=prose_sha256,
        editorial_index_sha256=index_sha256,
    )
    inventory_sha256 = _sha256_json(inventory)
    template = _read_prompt("reader-map.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    editorial_receipt_path = Path(editorial_result["receipt"])
    editorial_receipt_payload = _required_confined_file(
        layout.outputs,
        editorial_receipt_path,
        label="editorial receipt reader-map source",
    ).read_bytes()
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        "editorial_request_sha256": editorial_result["request_sha256"],
        "editorial_receipt_sha256": _sha256_bytes(editorial_receipt_payload),
        "editorial_outputs_sha256": _sha256_json(editorial_receipt["outputs"]),
        "editorial_prose_sha256": prose_sha256,
        "editorial_index_sha256": index_sha256,
        "paragraph_inventory_sha256": inventory_sha256,
    }
    request_sha256 = _request_sha256("reader-map", request_inputs)
    paths = _reader_map_paths(layout, request_sha256)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@EDITORIAL_PROSE_SHA256@@": prose_sha256,
            "@@EDITORIAL_INDEX_SHA256@@": index_sha256,
            "@@PARAGRAPH_INVENTORY_SHA256@@": inventory_sha256,
            "@@PARAGRAPH_INVENTORY_JSON@@": _canonical_json(inventory),
            "@@EDITORIAL_INDEX@@": editorial_index,
        },
        label="reader map",
    )
    manifest = _prompt_manifest(
        stage="reader-map",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=paths["response"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["inventory"], _canonical_json(inventory) + "\n")
    _write(V3_ROOT, paths["prompt"], prompt)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "request_sha256": request_sha256,
        "inventory": str(paths["inventory"]),
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "expected_response": str(paths["response"]),
        "view": str(paths["view"]),
        "preview": str(paths["preview"]),
    }


def _reader_exact_fields(
    value: Any, expected: set[str], *, label: str
) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != expected:
        actual = sorted(value) if isinstance(value, dict) else type(value).__name__
        raise SystemExit(
            f"{label} fields disagree with contract; expected={sorted(expected)}, "
            f"actual={actual}"
        )
    return value


def _reader_string_list(
    value: Any, *, allowed: tuple[str, ...] | None = None, label: str
) -> list[str]:
    if (
        not isinstance(value, list)
        or any(not isinstance(item, str) for item in value)
        or len(set(value)) != len(value)
        or (allowed is not None and any(item not in allowed for item in value))
    ):
        raise SystemExit(f"{label} must be a unique list of contracted strings")
    return value


def _validated_reader_map_response(
    layout: AuthoringLayout,
    reader_map_result: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    inventory_path = _required_confined_file(
        layout.inputs,
        Path(reader_map_result["inventory"]),
        label="reader-map paragraph inventory",
    )
    manifest_path = _required_confined_file(
        layout.inputs,
        Path(reader_map_result["manifest"]),
        label="reader-map prompt manifest",
    )
    response_path = _required_confined_file(
        layout.outputs,
        Path(reader_map_result["expected_response"]),
        label="reader-map response",
    )
    inventory = _load_object(inventory_path)
    manifest = _load_object(manifest_path)
    response = _load_object(response_path)
    if (
        manifest.get("stage") != "reader-map"
        or manifest.get("ayah_ref") != layout.ayah_ref
        or manifest.get("authoring_request_sha256")
        != reader_map_result["request_sha256"]
        or manifest.get("expected_response") != _manifest_path(response_path)
    ):
        raise SystemExit("Reader-map response is not bound to its exact manifest")
    prompt_path = _required_confined_file(
        layout.inputs,
        manifest_path.with_name("prompt.md"),
        label="reader-map prompt",
    )
    prompt_payload = prompt_path.read_bytes()
    if (
        manifest.get("prompt_sha256") != _sha256_bytes(prompt_payload)
        or manifest.get("prompt_bytes") != len(prompt_payload)
    ):
        raise SystemExit("Reader-map prompt does not match its manifest")
    request_inputs = manifest.get("inputs")
    if not isinstance(request_inputs, dict):
        raise SystemExit("Reader-map manifest lacks bound inputs")
    if _sha256_json(inventory) != request_inputs.get(
        "paragraph_inventory_sha256"
    ):
        raise SystemExit("Reader-map paragraph inventory hash is stale")

    _reader_exact_fields(
        response,
        {"schema_version", "identity", "blocks"},
        label="reader-map response",
    )
    if response.get("schema_version") != "commentary-v3-reader-map-response-v1":
        raise SystemExit("Reader-map response schema version is stale or invalid")
    identity = _reader_exact_fields(
        response.get("identity"),
        {
            "ayah_ref",
            "editorial_prose_sha256",
            "editorial_index_sha256",
            "paragraph_inventory_sha256",
            "prompt_sha256",
        },
        label="reader-map identity",
    )
    expected_identity = {
        "ayah_ref": layout.ayah_ref,
        "editorial_prose_sha256": request_inputs.get(
            "editorial_prose_sha256"
        ),
        "editorial_index_sha256": request_inputs.get(
            "editorial_index_sha256"
        ),
        "paragraph_inventory_sha256": request_inputs.get(
            "paragraph_inventory_sha256"
        ),
        "prompt_sha256": manifest["prompt_sha256"],
    }
    if identity != expected_identity:
        raise SystemExit("Reader-map response identity is stale or inconsistent")

    paragraphs = inventory.get("paragraphs")
    movements = inventory.get("movements")
    surprise_rows = inventory.get("surprise_rows")
    if (
        not isinstance(paragraphs, list)
        or not paragraphs
        or any(not isinstance(item, dict) for item in paragraphs)
        or not isinstance(movements, list)
        or not movements
        or any(not isinstance(item, dict) for item in movements)
        or not isinstance(surprise_rows, list)
        or any(not isinstance(item, dict) for item in surprise_rows)
    ):
        raise SystemExit("Reader-map paragraph inventory is malformed")
    paragraph_keys = [item.get("paragraph_key") for item in paragraphs]
    if any(not isinstance(key, str) for key in paragraph_keys) or len(
        set(paragraph_keys)
    ) != len(paragraph_keys):
        raise SystemExit("Reader-map paragraph inventory has invalid keys")
    paragraph_movements = {
        item["paragraph_key"]: item.get("movement_key") for item in paragraphs
    }
    movement_keys = [item.get("movement_key") for item in movements]
    if any(not isinstance(key, str) for key in movement_keys) or len(
        set(movement_keys)
    ) != len(movement_keys):
        raise SystemExit("Reader-map paragraph inventory has invalid movements")
    surprise_refs = [item.get("surprise_ref") for item in surprise_rows]
    if any(not isinstance(ref, str) for ref in surprise_refs) or len(
        set(surprise_refs)
    ) != len(surprise_refs):
        raise SystemExit("Reader-map paragraph inventory has invalid surprises")

    blocks = response.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        raise SystemExit("Reader-map response has no blocks")
    flattened_paragraphs: list[str] = []
    mapped_surprises: set[str] = set()
    first_block_by_movement: dict[str, str] = {}
    roles: list[str] = []
    for index, raw_block in enumerate(blocks, 1):
        block = _reader_exact_fields(
            raw_block,
            {
                "block_key",
                "movement_key",
                "paragraph_keys",
                "role",
                "core_reasons",
                "detail_kinds",
                "label_tr",
                "surprise_refs",
            },
            label=f"reader-map block {index}",
        )
        expected_block_key = f"b{index:03d}"
        if block.get("block_key") != expected_block_key:
            raise SystemExit(
                f"Reader-map block order is not canonical at {expected_block_key}"
            )
        movement_key = block.get("movement_key")
        if movement_key not in movement_keys:
            raise SystemExit(f"Reader-map block cites unknown movement: {movement_key}")
        block_paragraphs = block.get("paragraph_keys")
        if (
            not isinstance(block_paragraphs, list)
            or not block_paragraphs
            or any(not isinstance(key, str) for key in block_paragraphs)
            or len(set(block_paragraphs)) != len(block_paragraphs)
        ):
            raise SystemExit(f"Reader-map {expected_block_key} has invalid paragraphs")
        if any(
            paragraph_movements.get(key) != movement_key
            for key in block_paragraphs
        ):
            raise SystemExit(
                f"Reader-map {expected_block_key} crosses movements or cites "
                "unknown paragraphs"
            )
        flattened_paragraphs.extend(block_paragraphs)
        role = block.get("role")
        core_reasons = _reader_string_list(
            block.get("core_reasons"),
            allowed=READER_CORE_REASONS,
            label=f"Reader-map {expected_block_key} core reasons",
        )
        detail_kinds = _reader_string_list(
            block.get("detail_kinds"),
            allowed=READER_DETAIL_KINDS,
            label=f"Reader-map {expected_block_key} detail kinds",
        )
        block_surprises = _reader_string_list(
            block.get("surprise_refs"),
            label=f"Reader-map {expected_block_key} surprise refs",
        )
        label_tr = block.get("label_tr")
        if (
            role not in {"core", "detail"}
            or any(ref not in surprise_refs for ref in block_surprises)
        ):
            raise SystemExit(f"Reader-map {expected_block_key} has invalid roles")
        roles.append(role)
        first_block_by_movement.setdefault(movement_key, role)
        if role == "core":
            if not core_reasons or detail_kinds or label_tr is not None:
                raise SystemExit(
                    f"Reader-map core block {expected_block_key} has detail fields"
                )
            if block_surprises and not (
                {"surprise_carrier", "surprise_payoff"} & set(core_reasons)
            ):
                raise SystemExit(
                    f"Reader-map {expected_block_key} maps a surprise without a "
                    "surprise core reason"
                )
            mapped_surprises.update(block_surprises)
        else:
            if core_reasons or not detail_kinds or block_surprises:
                raise SystemExit(
                    f"Reader-map detail block {expected_block_key} has core fields"
                )
            if (
                not isinstance(label_tr, str)
                or label_tr != label_tr.strip()
                or not label_tr
                or "\n" in label_tr
                or len(label_tr) > 160
                or READER_LABEL_FORBIDDEN_RE.search(label_tr)
            ):
                raise SystemExit(
                    f"Reader-map detail block {expected_block_key} has an invalid label"
                )
    if flattened_paragraphs != paragraph_keys:
        raise SystemExit(
            "Reader-map blocks do not preserve exact paragraph coverage and order"
        )
    if any(first_block_by_movement.get(key) != "core" for key in movement_keys):
        raise SystemExit("Every reader-map movement must begin with a core block")
    if roles[0] != "core" or roles[-1] != "core":
        raise SystemExit("Reader-map opening and closing blocks must be core")
    all_core_reasons = {
        reason
        for block in blocks
        if block["role"] == "core"
        for reason in block["core_reasons"]
    }
    if "plain_reading" not in all_core_reasons or "closure" not in all_core_reasons:
        raise SystemExit("Reader-map core must preserve plain reading and closure")
    if mapped_surprises != set(surprise_refs):
        raise SystemExit(
            "Reader-map core surprise coverage is not exact; "
            f"missing={sorted(set(surprise_refs) - mapped_surprises)}"
        )
    return response, inventory


def _reader_view_artifact(
    response: dict[str, Any], inventory: dict[str, Any]
) -> dict[str, Any]:
    paragraph_by_key = {
        item["paragraph_key"]: item for item in inventory["paragraphs"]
    }
    blocks_by_movement: dict[str, list[dict[str, Any]]] = {
        item["movement_key"]: [] for item in inventory["movements"]
    }
    for block in response["blocks"]:
        blocks_by_movement[block["movement_key"]].append(
            {
                **block,
                "paragraphs": [
                    {
                        "paragraph_key": paragraph_key,
                        "text": paragraph_by_key[paragraph_key]["text"],
                    }
                    for paragraph_key in block["paragraph_keys"]
                ],
            }
        )
    core_blocks = [block for block in response["blocks"] if block["role"] == "core"]
    detail_blocks = [
        block for block in response["blocks"] if block["role"] == "detail"
    ]
    surprise_refs = [
        item["surprise_ref"] for item in inventory["surprise_rows"]
    ]
    return {
        "schema_version": "commentary-v3-reader-view-v1",
        "identity": {
            **response["identity"],
            "reader_map_response_sha256": _sha256_json(response),
        },
        "document_heading": inventory["document_heading"],
        "movements": [
            {
                "movement_key": movement["movement_key"],
                "heading": movement["heading"],
                "blocks": blocks_by_movement[movement["movement_key"]],
            }
            for movement in inventory["movements"]
        ],
        "coverage": {
            "movement_count": len(inventory["movements"]),
            "paragraph_count": len(inventory["paragraphs"]),
            "block_count": len(response["blocks"]),
            "core_block_count": len(core_blocks),
            "detail_block_count": len(detail_blocks),
            "core_paragraph_count": sum(
                len(block["paragraph_keys"]) for block in core_blocks
            ),
            "detail_paragraph_count": sum(
                len(block["paragraph_keys"]) for block in detail_blocks
            ),
            "available_detail_kinds": [
                kind
                for kind in READER_DETAIL_KINDS
                if any(kind in block["detail_kinds"] for block in detail_blocks)
            ],
            "surprise_refs": surprise_refs,
            "all_surprises_land_in_core": True,
        },
    }


def _reader_view_preview(view: dict[str, Any]) -> str:
    rendered: list[str] = []
    document_heading = view.get("document_heading")
    if isinstance(document_heading, dict):
        rendered.append(document_heading["markdown"])
    for movement in view["movements"]:
        heading = movement.get("heading")
        if isinstance(heading, dict):
            rendered.append(heading["markdown"])
        for block in movement["blocks"]:
            paragraphs = [item["text"] for item in block["paragraphs"]]
            if block["role"] == "core":
                rendered.extend(paragraphs)
                continue
            label = html.escape(block["label_tr"], quote=False)
            rendered.append(
                "<details>\n"
                f"<summary>{label}</summary>\n\n"
                + "\n\n".join(paragraphs)
                + "\n\n</details>"
            )
    return "\n\n".join(rendered) + "\n"


def _materialize_reader_view(
    layout: AuthoringLayout, reader_map_result: dict[str, Any]
) -> dict[str, Path]:
    response, inventory = _validated_reader_map_response(
        layout, reader_map_result
    )
    view = _reader_view_artifact(response, inventory)
    view_path = Path(reader_map_result["view"])
    preview_path = Path(reader_map_result["preview"])
    _assert_output_path(layout, view_path, label="reader view")
    _assert_output_path(layout, preview_path, label="guided preview")
    _write(V3_ROOT, view_path, _pretty_json(view))
    _write(V3_ROOT, preview_path, _reader_view_preview(view))
    return {"structured": view_path, "guided_preview": preview_path}


def _render_invitation(
    args: argparse.Namespace,
    editorial_result: dict[str, Any],
    editorial_receipt: dict[str, Any],
) -> dict[str, Any]:
    """Render the fresh reader-invitation handoff from editorial artifacts only."""

    layout = _authoring_layout(args.ayah)
    editorial_outputs = {
        key: Path(value) for key, value in editorial_result["outputs"].items()
    }
    prose_path = _required_confined_file(
        layout.outputs,
        editorial_outputs["prose"],
        label="editorial prose invitation source",
    )
    index_path = _required_confined_file(
        layout.outputs,
        editorial_outputs["index"],
        label="editorial index invitation source",
    )
    try:
        editorial_prose = prose_path.read_text(encoding="utf-8")
        editorial_index = index_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit(f"Cannot read invitation source artifacts: {exc}") from exc

    template = _read_prompt("invitation-summary.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    editorial_receipt_path = Path(editorial_result["receipt"])
    editorial_receipt_payload = _required_confined_file(
        layout.outputs,
        editorial_receipt_path,
        label="editorial receipt invitation source",
    ).read_bytes()
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        "editorial_request_sha256": editorial_result["request_sha256"],
        "editorial_receipt_sha256": _sha256_bytes(editorial_receipt_payload),
        "editorial_outputs_sha256": _sha256_json(editorial_receipt["outputs"]),
        "editorial_prose_sha256": _sha256_bytes(prose_path.read_bytes()),
        "editorial_index_sha256": _sha256_bytes(index_path.read_bytes()),
    }
    request_sha256 = _request_sha256("invitation-summary", request_inputs)
    paths = _invitation_paths(layout, request_sha256)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@EDITORIAL_PROSE@@": editorial_prose,
            "@@EDITORIAL_INDEX@@": editorial_index,
        },
        label="invitation summary",
    )
    manifest = _prompt_manifest(
        stage="invitation-summary",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=paths["response"],
        authoring_request_sha256=request_sha256,
        inputs=request_inputs,
    )
    _write(V3_ROOT, paths["prompt"], prompt)
    _write(V3_ROOT, paths["manifest"], _pretty_json(manifest))
    return {
        "ayah_ref": args.ayah,
        "request_sha256": request_sha256,
        "prompt": str(paths["prompt"]),
        "manifest": str(paths["manifest"]),
        "workspace": str(layout.workspace),
        "expected_response": str(paths["response"]),
    }


def _validate_invitation_summary(layout: AuthoringLayout, path: Path) -> None:
    """Reject recognizable apparatus leakage without imposing a style gate."""

    resolved = _required_confined_file(
        layout.outputs, path, label="invitation summary"
    )
    try:
        text = resolved.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise SystemExit(f"Cannot read invitation summary: {exc}") from exc
    lowered = text.casefold()
    forbidden_markers = (
        LOCKED_REF_PREFIX,
        "surprise:",
        "[supports-primary]",
        "[shifts-primary]",
        "[inference]",
        "candidate_id",
        "candidate_ref",
        "finding_ref",
        "branch_ref",
        "contact_ref",
        "connection_ref",
        "atlas_facets_tested",
        "support_id",
        "support_ref",
        "scope-micro",
        "scope-macro",
        "scope-global",
        "json_pointer",
        "source_pointer",
        "analysis_record_ref",
        "qac_ref",
    )
    forbidden_patterns = (
        (
            "stable internal ID",
            r"\b(?:sup|cand|conn|contact|referral)_[a-z0-9]"
            r"[a-z0-9_.:-]*\b",
        ),
        (
            "internal apparatus token",
            r"\b(?:hft|qac|scope|canonical|invitation|authoring|workflow|lane|"
            r"candidate|finding|branch|support|contact|connection|referral|"
            r"proposal|atlas)(?:[-_][a-z0-9]+)+\b",
        ),
        ("branch ID", r"\broot_[a-z0-9]+/b[a-z0-9]+\b|\bb[0-9]{3,}\b"),
        ("source record ID", r"\b(?:qi|qg|qs|qt|mg|ms)-[0-9a-f]{8}\b"),
        ("scope label", r"\b(?:micro|macro|global)\b"),
        (
            "workflow label",
            r"\b(?:authoring|workflow|scope|lane|candidate|finding|branch|"
            r"reconcile|reconciler|reconciliation)\b|\bi[sş] ak[ıi][sş][ıi]\b",
        ),
        ("HFT/QAC label", r"\b(?:hft|qac)\b"),
        (
            "analysis coordinate",
            r"\b[0-9]+:[0-9]+:[0-9]+(?::[0-9]+)?\b|#l[0-9]+\b",
        ),
        (
            "JSON pointer",
            r"(?<![a-z0-9_])/[a-z][a-z0-9_-]*(?:/[a-z0-9_.:-]+)+",
        ),
        ("content hash", r"\b[0-9a-f]{64}\b"),
    )
    leaked = [marker for marker in forbidden_markers if marker in lowered]
    leaked.extend(
        label for label, pattern in forbidden_patterns if re.search(pattern, lowered)
    )
    if leaked:
        raise SystemExit(
            "Invitation summary exposes internal editorial apparatus: "
            f"{sorted(set(leaked))}"
        )


def _output_presence(
    run_dir: Path, outputs: dict[str, Path], *, label: str
) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    for key, path in outputs.items():
        if _optional_confined_file(
            run_dir, path, label=f"{label} {key} output"
        ) is None:
            missing.append(key)
        else:
            present.append(key)
    return present, missing


def _authoring_completion(
    layout: AuthoringLayout,
    ayah_ref: str,
    lineage_paths: list[Path],
    first_pass_outputs: dict[str, Path],
    editorial_outputs: dict[str, Path],
    reader_view_outputs: dict[str, Path],
    reader_map_session_path: Path,
    invitation_output: Path,
    invitation_session_path: Path,
    merge_receipt_path: Path,
    editorial_receipt_path: Path,
) -> tuple[dict[str, Any], Path]:
    lineage: list[dict[str, Any]] = []
    seen_paths: set[Path] = set()
    for path in lineage_paths + [merge_receipt_path, editorial_receipt_path]:
        path = path.resolve(strict=False)
        if path in seen_paths:
            continue
        seen_paths.add(path)
        if not (
            path.is_relative_to(layout.inputs)
            or path.is_relative_to(layout.outputs)
        ):
            raise SystemExit(f"Completion lineage escapes canonical ayah roots: {path}")
        root = layout.inputs if path.is_relative_to(layout.inputs) else layout.outputs
        resolved = _required_confined_file(
            root, path, label="authoring lineage artifact"
        )
        payload = resolved.read_bytes()
        lineage.append(
            {
                "path": _manifest_path(resolved),
                "bytes": len(payload),
                "sha256": _sha256_bytes(payload),
            }
        )
    lineage.sort(key=lambda item: item["path"])

    output_records: dict[str, dict[str, Any]] = {}
    for phase, outputs in (
        ("first_pass", first_pass_outputs),
        ("editorial", editorial_outputs),
        ("reader_view", reader_view_outputs),
        ("invitation", {"summary": invitation_output}),
    ):
        for key, path in outputs.items():
            resolved = _required_confined_file(
                layout.outputs, path, label=f"{phase} {key} output"
            )
            payload = resolved.read_bytes()
            output_records[f"{phase}.{key}"] = {
                "path": _manifest_path(resolved),
                "bytes": len(payload),
                "sha256": _sha256_bytes(payload),
            }

    completion = {
        "schema_version": "commentary-v3-authoring-completion-v4",
        "ayah_ref": ayah_ref,
        "transport": {
            "prompt_delivery": "absolute_path_only",
            "prompt_content_was_not_required_in_the_initial_message": True,
        },
        "lineage": lineage,
        "phase_receipts": {
            "canonical_merge": _manifest_path(merge_receipt_path),
            "canonical_editorial": _manifest_path(editorial_receipt_path),
        },
        "reader_map": {
            "fresh_session_receipt": _manifest_path(reader_map_session_path),
            "semantic_authority": "presentation_mapping_only",
            "may_change_editorial_prose": False,
            "may_change_findings": False,
        },
        "invitation_summary": {
            "fresh_session_receipt": _manifest_path(invitation_session_path),
            "semantic_authority": "reader_invitation_only",
            "locked_finding_coverage_required": False,
        },
        "outputs": output_records,
    }
    completion_sha256 = _sha256_json(completion)
    completion_path = (
        layout.outputs / "completion" / completion_sha256 / "COMPLETION.json"
    )
    _write(V3_ROOT, completion_path, _pretty_json(completion))
    return completion, completion_path


def advance_authoring(args: argparse.Namespace) -> dict[str, Any]:
    """Advance the canonical, content-addressed prose-first workflow."""

    layout = _authoring_layout(args.ayah)
    scope_result = _render_scopes(args)
    common = {
        "schema_version": "commentary-v3-authoring-workflow-status-v4",
        "ayah_ref": args.ayah,
        "canonical_paths": {
            "inputs": str(layout.inputs),
            "outputs": str(layout.outputs),
            "temporary_paths_allowed": False,
            "artifacts_are_git_stageable": True,
        },
        "transport": {
            "prompt_delivery": "absolute_path_only",
            "pipe_or_inline_prompt_contents": False,
            "embedded_json": "canonical-minified-utf8",
        },
        "canonical_workspace_policy": {
            "new_turn_recording_requires_guard": True,
            "guardless_receipt_loading": "preexisting_completed_lineage_only",
            "legacy_guard_is_not_inferred": True,
        },
        "inter_ayah_evidence": scope_result["inter_ayah_evidence"],
    }
    lineage_paths: list[Path] = []
    legacy_completion_paths: list[Path] = []
    base_review_paths: dict[str, Path] = {}
    base_review_manifests: dict[str, Path] = {}
    missing_reviews: list[str] = []
    handoffs: list[dict[str, Any]] = []
    for lane in LANES:
        stage = scope_result["stages"][lane]
        packet_path = Path(stage["packet"])
        prompt_path = Path(stage["prompt"])
        manifest_path = Path(stage["manifest"])
        response_path = Path(stage["expected_response"])
        lineage_paths.extend([packet_path, prompt_path, manifest_path])
        base_review_paths[lane] = response_path
        base_review_manifests[lane] = manifest_path
        if _optional_confined_file(
            layout.outputs, response_path, label=f"{lane} scope review"
        ) is None:
            missing_reviews.append(lane)
            handoffs.append(
                _generated_prompt_handoff(
                    layout,
                    role=f"{lane}_scope_reviewer",
                    conversation=f"scope-{lane}",
                    conversation_generation=stage["request_sha256"],
                    prompt_path=prompt_path,
                    manifest_path=manifest_path,
                    expected_response=response_path,
                )
            )
        else:
            session, session_path = _load_session_receipt(
                layout, f"scope-{lane}", stage["request_sha256"]
            )
            if session is None:
                raise SystemExit(
                    f"{lane} review exists without its persisted agent session"
                )
            lineage_paths.extend([response_path, session_path])
    if missing_reviews:
        return {
            **common,
            "status": "waiting_for_agents",
            "stage": "scope_review",
            "missing_lanes": missing_reviews,
            "handoffs": handoffs,
        }

    active_review_paths = dict(base_review_paths)
    active_review_manifests = dict(base_review_manifests)
    semantic_baselines = {
        lane: _load_object(base_review_paths[lane]) for lane in LANES
    }
    semantic_exception_paths: dict[str, set[str]] = {
        lane: set() for lane in LANES
    }
    reconcile_result: dict[str, Any] | None = None
    reconciled: dict[str, Any] | None = None
    reconciler_generation: str | None = None
    for attempt in range(1, MAX_RECONCILIATION_ATTEMPTS + 1):
        packets, reviews, _ = _load_bound_scope_artifacts(
            args,
            scope_result,
            active_review_paths,
            active_review_manifests,
            validate_reviews=False,
        )
        active_repair_phases: dict[str, str | None] = {}
        for lane in LANES:
            active_manifest = _load_object(active_review_manifests[lane])
            manifest_inputs = active_manifest.get("inputs")
            repair_phase = (
                manifest_inputs.get("repair_phase")
                if isinstance(manifest_inputs, dict)
                else None
            )
            if repair_phase not in {None, "scope_validation", "reconciliation_requested"}:
                raise SystemExit(
                    f"{lane} review manifest has unknown repair phase: {repair_phase!r}"
                )
            active_repair_phases[lane] = repair_phase
            if repair_phase == "reconciliation_requested":
                # A reconciler-requested turn is allowed to change the analysis.
                # Its complete result becomes the semantic baseline for any
                # subsequent shape-only validation-repair chain.
                semantic_baselines[lane] = reviews[lane]
                semantic_exception_paths[lane] = set()
            elif repair_phase == "scope_validation":
                stored_exceptions = manifest_inputs.get(
                    "scope_validation_exception_paths"
                )
                if (
                    not isinstance(stored_exceptions, list)
                    or any(
                        not isinstance(field, str) or not field
                        for field in stored_exceptions
                    )
                    or len(set(stored_exceptions)) != len(stored_exceptions)
                ):
                    raise SystemExit(
                        f"{lane} validation-repair manifest has malformed "
                        "semantic exceptions"
                    )
                semantic_exception_paths[lane] = set(stored_exceptions)
        validation_errors: dict[str, str] = {}
        for lane in LANES:
            try:
                _validate_scope_review(lane, packets[lane], reviews[lane])
                if active_repair_phases[lane] == "scope_validation":
                    _validate_scope_validation_repair_preserves_semantics(
                        lane,
                        semantic_baselines[lane],
                        reviews[lane],
                        semantic_exception_paths[lane],
                        _scope_validation_fallback_identity_paths(
                            lane,
                            packets[lane],
                            semantic_baselines[lane],
                        ),
                        _scope_trusted_referral_origins(
                            lane,
                            packets[lane],
                            semantic_baselines[lane],
                        ),
                    )
            except SystemExit as exc:
                validation_errors[lane] = str(exc)
        if not validation_errors:
            pass
        else:
            repair_results: dict[str, dict[str, Any]] = {}
            repair_handoffs: list[dict[str, Any]] = []
            missing_repairs: list[str] = []
            for lane, issue in validation_errors.items():
                repair_exception_paths = semantic_exception_paths[lane] | (
                    _scope_validation_exception_paths(
                        lane, packets[lane], semantic_baselines[lane]
                    )
                )
                repair_request = {
                    "repair_ref": (
                        "scope_validation_"
                        + _sha256_json(
                            {
                                "lane": lane,
                                "review": reviews[lane],
                                "issue": issue,
                                "iteration": attempt,
                            }
                        )[:24]
                    ),
                    "issue": issue,
                    "required_action": (
                        "Return a complete replacement review that preserves all "
                        "meaningful prior findings while repairing this exact "
                        "loss-prevention accounting gap."
                    ),
                }
                validation_record = {
                    "schema_version": "commentary-v3-scope-validation-repair-v1",
                    "ayah_ref": args.ayah,
                    "lane": lane,
                    "repair_requests": [repair_request],
                    "baseline_scope_review": semantic_baselines[lane],
                    "scope_validation_exception_paths": sorted(
                        repair_exception_paths
                    ),
                }
                repair_result = _render_scope_repair(
                    args,
                    lane,
                    packets[lane],
                    reviews[lane],
                    validation_record,
                    [repair_request],
                    repair_phase="scope_validation",
                    repair_iteration=attempt,
                    scope_validation_exception_paths=sorted(
                        repair_exception_paths
                    ),
                )
                repair_results[lane] = repair_result
                repair_prompt = Path(repair_result["prompt"])
                repair_manifest = Path(repair_result["manifest"])
                repair_response = Path(repair_result["expected_response"])
                lineage_paths.extend([repair_prompt, repair_manifest])
                if _optional_confined_file(
                    layout.outputs,
                    repair_response,
                    label=f"{lane} scope validation repair",
                ) is None:
                    missing_repairs.append(lane)
                    repair_handoffs.append(
                        _generated_prompt_handoff(
                            layout,
                            role=f"{lane}_scope_repairer",
                            conversation=f"scope-{lane}",
                            conversation_generation=scope_result["stages"][lane][
                                "request_sha256"
                            ],
                            prompt_path=repair_prompt,
                            manifest_path=repair_manifest,
                            expected_response=repair_response,
                            require_resume=True,
                        )
                    )
                else:
                    lineage_paths.append(repair_response)
            if missing_repairs:
                return {
                    **common,
                    "status": "waiting_for_agents",
                    "stage": "scope_validation_repair",
                    "attempt": attempt,
                    "validation_errors": validation_errors,
                    "missing_lanes": missing_repairs,
                    "handoffs": repair_handoffs,
                }
            for lane, repair_result in repair_results.items():
                active_review_paths[lane] = Path(repair_result["expected_response"])
                active_review_manifests[lane] = Path(repair_result["manifest"])
            continue

        accepted_member_refs = {
            finding_ref
            for lane in LANES
            for finding_ref in _record_id_set(
                reviews[lane].get("accepted_findings"),
                "finding_ref",
                label=f"{lane} accepted findings",
            )
        }
        reconciliation_repair_context: dict[str, Any] | None = None
        reconciliation_semantic_baseline: dict[str, dict[str, Any]] = {}
        last_semantically_trusted_reconciliation: dict[str, Any] | None = None
        for reconciliation_validation_attempt in range(
            1, MAX_RECONCILIATION_ATTEMPTS + 1
        ):
            first_reconciliation_turn = reconciler_generation is None
            reconcile_result = _render_reconcile(
                args,
                scope_result,
                active_review_paths,
                active_review_manifests,
                reconciliation_repair_context,
            )
            reconcile_prompt = Path(reconcile_result["prompt"])
            reconcile_manifest_path = Path(reconcile_result["manifest"])
            reconcile_response = Path(reconcile_result["expected_response"])
            if reconciler_generation is None:
                reconciler_generation = reconcile_result["request_sha256"]
            lineage_paths.extend([reconcile_prompt, reconcile_manifest_path])
            if _optional_confined_file(
                layout.outputs,
                reconcile_response,
                label=(
                    f"reconciliation attempt {attempt}, validation turn "
                    f"{reconciliation_validation_attempt}"
                ),
            ) is None:
                is_repair = reconciliation_repair_context is not None
                return {
                    **common,
                    "status": "waiting_for_agent",
                    "stage": (
                        "reconciliation_validation_repair"
                        if is_repair
                        else "reconciliation"
                    ),
                    "attempt": attempt,
                    "validation_attempt": reconciliation_validation_attempt,
                    "handoffs": [
                        _generated_prompt_handoff(
                            layout,
                            role=(
                                "scope_reconciler_repairer"
                                if is_repair
                                else "scope_reconciler"
                            ),
                            conversation="scope-reconciler",
                            conversation_generation=reconciler_generation,
                            prompt_path=reconcile_prompt,
                            manifest_path=reconcile_manifest_path,
                            expected_response=reconcile_response,
                            require_resume=not first_reconciliation_turn,
                        )
                    ],
                }
            reconciler_session, reconciler_session_path = _load_session_receipt(
                layout, "scope-reconciler", reconciler_generation
            )
            if reconciler_session is None:
                raise SystemExit(
                    "Reconciliation response exists without its persisted agent session"
                )
            lineage_paths.extend([reconcile_response, reconciler_session_path])
            reconciled = _load_object(reconcile_response)
            reconcile_manifest = _load_object(reconcile_manifest_path)
            validation_issue: str | None = None
            current_semantics = _available_reconciliation_semantics_by_member(
                reconciled,
                accepted_member_refs,
            )
            try:
                _validate_reconciliation_repair_preserves_semantics(
                    reconciliation_semantic_baseline,
                    current_semantics,
                )
            except SystemExit as exc:
                validation_issue = str(exc)
            else:
                for member_ref, semantics in current_semantics.items():
                    baseline = reconciliation_semantic_baseline.setdefault(
                        member_ref, {}
                    )
                    for field, value in semantics.items():
                        baseline.setdefault(field, value)
                last_semantically_trusted_reconciliation = reconciled
                try:
                    _validate_reconciled_findings(
                        args.ayah,
                        reconciled,
                        reconcile_manifest,
                        reviews,
                        packets,
                    )
                except SystemExit as exc:
                    validation_issue = str(exc)
            if validation_issue is not None:
                reconciliation_repair_context = {
                    "prior_reconciliation": (
                        last_semantically_trusted_reconciliation or reconciled
                    ),
                    "validation_issue": validation_issue,
                    "repair_iteration": reconciliation_validation_attempt,
                }
                continue
            break
        else:
            raise SystemExit(
                "Reconciliation validation exceeded the bounded repair chain"
            )
        if reconciled["ready_for_prose"]:
            break

        repair_results: dict[str, dict[str, Any]] = {}
        missing_repairs: list[str] = []
        repair_handoffs: list[dict[str, Any]] = []
        for lane in LANES:
            requested = reconciled["repair_requests"][lane]
            if not requested:
                continue
            repair_result = _render_scope_repair(
                args,
                lane,
                packets[lane],
                reviews[lane],
                reconciled,
                requested,
                repair_phase="reconciliation_requested",
                repair_iteration=attempt,
            )
            repair_results[lane] = repair_result
            repair_prompt = Path(repair_result["prompt"])
            repair_manifest = Path(repair_result["manifest"])
            repair_response = Path(repair_result["expected_response"])
            lineage_paths.extend([repair_prompt, repair_manifest])
            if _optional_confined_file(
                layout.outputs,
                repair_response,
                label=f"{lane} scope repair",
            ) is None:
                missing_repairs.append(lane)
                repair_handoffs.append(
                    _generated_prompt_handoff(
                        layout,
                        role=f"{lane}_scope_repairer",
                        conversation=f"scope-{lane}",
                        conversation_generation=scope_result["stages"][lane][
                            "request_sha256"
                        ],
                        prompt_path=repair_prompt,
                        manifest_path=repair_manifest,
                        expected_response=repair_response,
                        require_resume=True,
                    )
                )
            else:
                lineage_paths.append(repair_response)
        if missing_repairs:
            return {
                **common,
                "status": "waiting_for_agents",
                "stage": "scope_repair",
                "reconciliation_attempt": attempt,
                "missing_lanes": missing_repairs,
                "handoffs": repair_handoffs,
            }
        for lane, repair_result in repair_results.items():
            active_review_paths[lane] = Path(repair_result["expected_response"])
            active_review_manifests[lane] = Path(repair_result["manifest"])
        packets, reviews, _ = _load_bound_scope_artifacts(
            args,
            scope_result,
            active_review_paths,
            active_review_manifests,
            validate_reviews=False,
        )
    else:
        raise SystemExit(
            f"Reconciliation exceeded {MAX_RECONCILIATION_ATTEMPTS} repair attempts"
        )

    assert reconcile_result is not None and reconciled is not None
    prose_results: dict[str, dict[str, Any]] = {}
    missing_drafts: list[str] = []
    prose_handoffs: list[dict[str, Any]] = []
    for lane in LANES:
        lane_args = argparse.Namespace(**vars(args))
        lane_args.lane = lane
        prose_result = _render_scope_prose(
            lane_args,
            scope_result,
            active_review_paths,
            active_review_manifests,
            reconcile_result,
        )
        prose_results[lane] = prose_result
        prompt_path = Path(prose_result["prompt"])
        manifest_path = Path(prose_result["manifest"])
        response_path = Path(prose_result["expected_response"])
        lineage_paths.extend([prompt_path, manifest_path])
        if _optional_confined_file(
            layout.outputs, response_path, label=f"{lane} prose draft"
        ) is None:
            missing_drafts.append(lane)
            prose_handoffs.append(
                _generated_prompt_handoff(
                    layout,
                    role=f"{lane}_scope_prose_writer",
                    conversation=f"scope-{lane}",
                    conversation_generation=scope_result["stages"][lane][
                        "request_sha256"
                    ],
                    prompt_path=prompt_path,
                    manifest_path=manifest_path,
                    expected_response=response_path,
                    require_resume=True,
                )
            )
        else:
            lineage_paths.append(response_path)
    if missing_drafts:
        return {
            **common,
            "status": "waiting_for_agents",
            "stage": "scope_prose",
            "missing_lanes": missing_drafts,
            "handoffs": prose_handoffs,
        }

    base_prose_results = dict(prose_results)
    active_prose_results = dict(prose_results)
    _locked_by_ref, prose_assignments = _locked_finding_assignments(reconciled)
    accounting_attempts = {lane: 0 for lane in LANES}
    rewrite_attempts = {lane: 0 for lane in LANES}
    for _validation_turn in range(
        MAX_SCOPE_PROSE_REPAIR_ATTEMPTS
        + MAX_SCOPE_PROSE_REWRITE_ATTEMPTS
        + 1
    ):
        prose_validation_errors: dict[str, str] = {}
        active_prose_drafts: dict[str, dict[str, Any]] = {}
        for lane in LANES:
            active_result = active_prose_results[lane]
            draft = _load_object(Path(active_result["expected_response"]))
            active_prose_drafts[lane] = draft
            draft_manifest = _load_object(Path(active_result["manifest"]))
            try:
                _validate_scope_prose_draft(
                    args.ayah,
                    lane,
                    draft,
                    draft_manifest,
                    reconciled,
                    prose_assignments,
                )
            except SystemExit as exc:
                prose_validation_errors[lane] = str(exc)
        if not prose_validation_errors:
            break
        rewrite_issues: dict[str, str] = {
            lane: issue
            for lane, issue in prose_validation_errors.items()
            if not _scope_prose_issue_is_accounting_only(issue)
        }
        repair_expectations: dict[
            str, tuple[dict[str, list[str]], dict[str, str]]
        ] = {}
        for lane, issue in prose_validation_errors.items():
            if lane in rewrite_issues:
                continue
            try:
                repair_expectations[lane] = (
                    _scope_prose_lossless_ref_normalization(
                        lane,
                        active_prose_drafts[lane],
                        _locked_by_ref,
                        prose_assignments[lane],
                    )
                )
            except SystemExit as exc:
                rewrite_issues[lane] = (
                    f"{issue}; accounting-only normalization is unsafe: {exc}"
                )

        prose_repair_results: dict[str, dict[str, Any]] = {}
        missing_prose_repairs: list[str] = []
        prose_repair_handoffs: list[dict[str, Any]] = []
        for lane in repair_expectations:
            issue = prose_validation_errors[lane]
            if accounting_attempts[lane] >= MAX_SCOPE_PROSE_REPAIR_ATTEMPTS:
                raise SystemExit(
                    f"{lane} scope prose accounting repair exceeded its "
                    "bounded same-agent chain"
                )
            accounting_attempts[lane] += 1
            prose_repair_attempt = accounting_attempts[lane]
            repair_result = _render_scope_prose_repair(
                args,
                lane,
                base_prose_results[lane],
                active_prose_results[lane],
                issue,
                reconciled,
                prose_repair_attempt,
            )
            prose_repair_results[lane] = repair_result
            repair_prompt = Path(repair_result["prompt"])
            repair_manifest = Path(repair_result["manifest"])
            repair_response = Path(repair_result["expected_response"])
            lineage_paths.extend([repair_prompt, repair_manifest])
            if _optional_confined_file(
                layout.outputs,
                repair_response,
                label=f"{lane} scope prose validation repair",
            ) is None:
                missing_prose_repairs.append(lane)
                prose_repair_handoffs.append(
                    _generated_prompt_handoff(
                        layout,
                        role=f"{lane}_scope_prose_repairer",
                        conversation=f"scope-{lane}",
                        conversation_generation=scope_result["stages"][lane][
                            "request_sha256"
                        ],
                        prompt_path=repair_prompt,
                        manifest_path=repair_manifest,
                        expected_response=repair_response,
                        require_resume=True,
                    )
                )
            else:
                repaired_draft = _load_object(repair_response)
                lineage_paths.append(repair_response)
                try:
                    _validate_scope_prose_repair_preserves_semantics(
                        lane,
                        active_prose_drafts[lane],
                        repaired_draft,
                        *repair_expectations[lane],
                    )
                except SystemExit as exc:
                    rewrite_issues[lane] = (
                        "The accounting repair response changed or could not "
                        f"safely preserve prose semantics: {exc}"
                    )
        if missing_prose_repairs:
            return {
                **common,
                "status": "waiting_for_agents",
                "stage": "scope_prose_validation_repair",
                "attempt": prose_repair_attempt,
                "validation_errors": prose_validation_errors,
                "missing_lanes": missing_prose_repairs,
                "handoffs": prose_repair_handoffs,
            }
        active_prose_results.update(
            {
                lane: result
                for lane, result in prose_repair_results.items()
                if lane not in rewrite_issues
            }
        )
        if not rewrite_issues:
            continue

        prose_rewrite_results: dict[str, dict[str, Any]] = {}
        missing_prose_rewrites: list[str] = []
        prose_rewrite_handoffs: list[dict[str, Any]] = []
        for lane, issue in rewrite_issues.items():
            if rewrite_attempts[lane] >= MAX_SCOPE_PROSE_REWRITE_ATTEMPTS:
                raise SystemExit(
                    f"{lane} scope prose rewrite exceeded its bounded "
                    "same-agent chain"
                )
            rewrite_attempts[lane] += 1
            rewrite_result = _render_scope_prose_rewrite(
                args,
                lane,
                base_prose_results[lane],
                active_prose_results[lane],
                issue,
                reconciled,
                rewrite_attempts[lane],
            )
            prose_rewrite_results[lane] = rewrite_result
            rewrite_prompt = Path(rewrite_result["prompt"])
            rewrite_manifest = Path(rewrite_result["manifest"])
            rewrite_response = Path(rewrite_result["expected_response"])
            lineage_paths.extend([rewrite_prompt, rewrite_manifest])
            if _optional_confined_file(
                layout.outputs,
                rewrite_response,
                label=f"{lane} genuine scope prose rewrite",
            ) is None:
                missing_prose_rewrites.append(lane)
                prose_rewrite_handoffs.append(
                    _generated_prompt_handoff(
                        layout,
                        role=f"{lane}_scope_prose_rewriter",
                        conversation=f"scope-{lane}",
                        conversation_generation=scope_result["stages"][lane][
                            "request_sha256"
                        ],
                        prompt_path=rewrite_prompt,
                        manifest_path=rewrite_manifest,
                        expected_response=rewrite_response,
                        require_resume=True,
                    )
                )
            else:
                lineage_paths.append(rewrite_response)
        if missing_prose_rewrites:
            return {
                **common,
                "status": "waiting_for_agents",
                "stage": "scope_prose_rewrite",
                "validation_errors": rewrite_issues,
                "missing_lanes": missing_prose_rewrites,
                "handoffs": prose_rewrite_handoffs,
            }
        active_prose_results.update(prose_rewrite_results)
    else:
        raise SystemExit("Scope prose validation exceeded the bounded repair chain")
    prose_results = active_prose_results

    merge_result = _render_merge(
        args,
        scope_result,
        reconcile_result,
        prose_results,
        reviews,
    )
    merge_prompt = Path(merge_result["prompt"])
    merge_manifest = Path(merge_result["manifest"])
    first_pass_outputs = {
        key: Path(value) for key, value in merge_result["outputs"].items()
    }
    lineage_paths.extend([merge_prompt, merge_manifest])
    present_first, missing_first = _output_presence(
        layout.outputs, first_pass_outputs, label="first-pass"
    )
    if missing_first:
        partial_merge_requires_resume = bool(present_first)
        if partial_merge_requires_resume:
            canonical_session, _canonical_session_path = _load_session_receipt(
                layout, "canonical-writer", merge_result["request_sha256"]
            )
            if canonical_session is None:
                raise SystemExit(
                    "Partial first-pass outputs exist without their persisted "
                    "canonical-writer session; a fresh writer may not inherit them"
                )
        return {
            **common,
            "status": "waiting_for_agent",
            "stage": "canonical_merge",
            "present_outputs": present_first,
            "missing_outputs": missing_first,
            "handoffs": [
                _generated_prompt_handoff(
                    layout,
                    role="canonical_merge_writer",
                    conversation="canonical-writer",
                    conversation_generation=merge_result["request_sha256"],
                    prompt_path=merge_prompt,
                    manifest_path=merge_manifest,
                    expected_outputs=first_pass_outputs,
                    workspace_access="workspace_write",
                    require_resume=partial_merge_requires_resume,
                    turn_receipt=Path(merge_result["receipt"]),
                )
            ],
        }

    merge_receipt_path = Path(merge_result["receipt"])
    merge_receipt = _load_verified_turn_receipt(
        layout,
        merge_manifest,
        merge_receipt_path,
        legacy_completion_paths=legacy_completion_paths,
    )
    if merge_receipt is None:
        canonical_session, _ = _load_session_receipt(
            layout, "canonical-writer", merge_result["request_sha256"]
        )
        if canonical_session is None:
            raise SystemExit(
                "First-pass outputs exist without a canonical-writer session receipt"
            )
        return {
            **common,
            "status": "execution_receipt_required",
            "stage": "canonical_merge",
            "turn_receipt": str(merge_receipt_path),
            "record_command": [
                "python3",
                "_commentary/v3/workflow.py",
                "authoring-record-turn",
                "--ayah",
                args.ayah,
                "--session-id",
                canonical_session["session_id"],
                "--prompt-manifest",
                str(merge_manifest),
            ],
        }

    editorial_result = _render_editorial(args, merge_result, merge_receipt)
    editorial_prompt = Path(editorial_result["prompt"])
    editorial_manifest = Path(editorial_result["manifest"])
    editorial_outputs = {
        key: Path(value) for key, value in editorial_result["outputs"].items()
    }
    lineage_paths.extend([editorial_prompt, editorial_manifest])
    present_editorial, missing_editorial = _output_presence(
        layout.outputs, editorial_outputs, label="editorial"
    )
    if missing_editorial:
        return {
            **common,
            "status": "waiting_for_agent",
            "stage": "canonical_editorial_followup",
            "present_outputs": present_editorial,
            "missing_outputs": missing_editorial,
            "handoffs": [
                _generated_prompt_handoff(
                    layout,
                    role="canonical_editorial_writer",
                    conversation="canonical-writer",
                    conversation_generation=merge_result["request_sha256"],
                    prompt_path=editorial_prompt,
                    manifest_path=editorial_manifest,
                    expected_outputs=editorial_outputs,
                    workspace_access="workspace_write",
                    require_resume=True,
                    turn_receipt=Path(editorial_result["receipt"]),
                )
            ],
        }

    editorial_receipt_path = Path(editorial_result["receipt"])
    editorial_receipt = _load_verified_turn_receipt(
        layout,
        editorial_manifest,
        editorial_receipt_path,
        prior_receipt=merge_receipt_path,
        legacy_completion_paths=legacy_completion_paths,
    )
    if editorial_receipt is None:
        canonical_session, _ = _load_session_receipt(
            layout, "canonical-writer", merge_result["request_sha256"]
        )
        assert canonical_session is not None
        return {
            **common,
            "status": "execution_receipt_required",
            "stage": "canonical_editorial_followup",
            "turn_receipt": str(editorial_receipt_path),
            "record_command": [
                "python3",
                "_commentary/v3/workflow.py",
                "authoring-record-turn",
                "--ayah",
                args.ayah,
                "--session-id",
                canonical_session["session_id"],
                "--prompt-manifest",
                str(editorial_manifest),
                "--prior-receipt",
                str(merge_receipt_path),
            ],
        }

    reader_map_result = _render_reader_map(
        args, editorial_result, editorial_receipt
    )
    reader_map_inventory = Path(reader_map_result["inventory"])
    reader_map_prompt = Path(reader_map_result["prompt"])
    reader_map_manifest = Path(reader_map_result["manifest"])
    reader_map_response = Path(reader_map_result["expected_response"])
    lineage_paths.extend(
        [reader_map_inventory, reader_map_prompt, reader_map_manifest]
    )
    if _optional_confined_file(
        layout.outputs, reader_map_response, label="reader-map response"
    ) is None:
        return {
            **common,
            "status": "waiting_for_agent",
            "stage": "reader_map",
            "handoffs": [
                _generated_prompt_handoff(
                    layout,
                    role="reader_presentation_mapper",
                    conversation="reader-map-writer",
                    conversation_generation=reader_map_result[
                        "request_sha256"
                    ],
                    prompt_path=reader_map_prompt,
                    manifest_path=reader_map_manifest,
                    expected_response=reader_map_response,
                )
            ],
        }
    reader_map_session, reader_map_session_path = _load_session_receipt(
        layout, "reader-map-writer", reader_map_result["request_sha256"]
    )
    if reader_map_session is None:
        raise SystemExit(
            "Reader-map response exists without its persisted fresh-agent session"
        )
    reader_view_outputs = _materialize_reader_view(layout, reader_map_result)
    lineage_paths.extend([reader_map_response, reader_map_session_path])

    invitation_result = _render_invitation(
        args, editorial_result, editorial_receipt
    )
    invitation_prompt = Path(invitation_result["prompt"])
    invitation_manifest = Path(invitation_result["manifest"])
    invitation_output = Path(invitation_result["expected_response"])
    lineage_paths.extend([invitation_prompt, invitation_manifest])
    if _optional_confined_file(
        layout.outputs, invitation_output, label="invitation summary"
    ) is None:
        return {
            **common,
            "status": "waiting_for_agent",
            "stage": "invitation_summary",
            "handoffs": [
                _generated_prompt_handoff(
                    layout,
                    role="invitation_summary_writer",
                    conversation="invitation-writer",
                    conversation_generation=invitation_result["request_sha256"],
                    prompt_path=invitation_prompt,
                    manifest_path=invitation_manifest,
                    expected_response=invitation_output,
                )
            ],
        }
    invitation_session, invitation_session_path = _load_session_receipt(
        layout, "invitation-writer", invitation_result["request_sha256"]
    )
    if invitation_session is None:
        raise SystemExit(
            "Invitation summary exists without its persisted fresh-agent session"
        )
    _validate_invitation_summary(layout, invitation_output)
    lineage_paths.extend([invitation_session_path])

    lineage_paths.extend(
        [
            _session_receipt_path(
                layout,
                f"scope-{lane}",
                scope_result["stages"][lane]["request_sha256"],
            )
            for lane in LANES
        ]
    )
    lineage_paths.extend(
        [
            _session_receipt_path(
                layout, "scope-reconciler", reconciler_generation
            ),
            _session_receipt_path(
                layout, "canonical-writer", merge_result["request_sha256"]
            ),
        ]
    )
    for turn_receipt in (merge_receipt, editorial_receipt):
        guard_record = turn_receipt.get("workspace_guard")
        if guard_record is None:
            continue
        if not isinstance(guard_record, dict):
            raise SystemExit("Canonical turn receipt has a malformed workspace guard")
        guard_path = _absolute_manifest_path(
            guard_record.get("path"), label="canonical workspace guard"
        )
        _assert_input_path(layout, guard_path, label="canonical workspace guard")
        guard_payload = _required_confined_file(
            layout.inputs, guard_path, label="canonical workspace guard"
        ).read_bytes()
        if guard_record.get("sha256") != _sha256_bytes(guard_payload):
            raise SystemExit("Canonical workspace guard changed after notarization")
        lineage_paths.append(guard_path)
    lineage_paths.extend(legacy_completion_paths)
    completion, completion_path = _authoring_completion(
        layout,
        args.ayah,
        lineage_paths,
        first_pass_outputs,
        editorial_outputs,
        reader_view_outputs,
        reader_map_session_path,
        invitation_output,
        invitation_session_path,
        merge_receipt_path,
        editorial_receipt_path,
    )
    guarded_turn_count = sum(
        "workspace_guard" in receipt
        for receipt in (merge_receipt, editorial_receipt)
    )
    workspace_guard_status = (
        "enforced"
        if guarded_turn_count == 2
        else "legacy_pre_guard_completed_lineage"
        if guarded_turn_count == 0
        else "mixed_guard_lineage"
    )
    return {
        **common,
        "status": "complete",
        "stage": "complete",
        "completion_manifest": str(completion_path),
        "canonical_workspace_guard_status": workspace_guard_status,
        "production_workspace_guard_enforced": guarded_turn_count == 2,
        "outputs": completion["outputs"],
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    advance = subparsers.add_parser(
        "advance",
        help=(
            "Advance the complete prose-first authoring workflow until an "
            "agent path handoff is needed or final outputs are complete"
        ),
    )
    advance.add_argument("--ayah", required=True)
    advance.add_argument("--docket", type=Path)
    advance.add_argument("--source-bundle", type=Path)
    advance.add_argument(
        "--inter-ayah-dir",
        type=Path,
        default=DEFAULT_INTER_AYAH_DIR,
        help=(
            "Directory containing the typed reciprocal-expanded per-ayah "
            "inter-ayah TSV projection"
        ),
    )
    advance.add_argument(
        "--inter-ayah-parent-dir",
        type=Path,
        default=DEFAULT_INTER_AYAH_PARENT_DIR,
        help=(
            "Complete directional parent corpus used for automatic lossless "
            "reconstruction if projection integrity validation fails"
        ),
    )
    advance.add_argument(
        "--quran-text",
        type=Path,
        default=DEFAULT_QURAN_TEXT,
        help=(
            "Complete ayah-text TSV used to attach exact target Arabic to every "
            "macro/global connection"
        ),
    )
    advance.set_defaults(func=advance_authoring)

    scopes = subparsers.add_parser("scopes", help="Render three lane review prompts")
    scopes.add_argument("--ayah", required=True)
    scopes.add_argument("--docket", type=Path)
    scopes.add_argument("--source-bundle", type=Path)
    scopes.add_argument(
        "--inter-ayah-dir",
        type=Path,
        default=DEFAULT_INTER_AYAH_DIR,
        help=(
            "Directory containing the typed reciprocal-expanded per-ayah "
            "inter-ayah TSV projection"
        ),
    )
    scopes.add_argument(
        "--inter-ayah-parent-dir",
        type=Path,
        default=DEFAULT_INTER_AYAH_PARENT_DIR,
        help=(
            "Complete directional parent corpus used for automatic lossless "
            "reconstruction if projection integrity validation fails"
        ),
    )
    scopes.add_argument(
        "--quran-text",
        type=Path,
        default=DEFAULT_QURAN_TEXT,
        help=(
            "Complete ayah-text TSV used to attach exact target Arabic to every "
            "macro/global connection"
        ),
    )
    scopes.set_defaults(func=_render_scopes)

    record_session = subparsers.add_parser(
        "record-session",
        help="Bind a persistent executor session to a canonical authoring conversation",
    )
    record_session.add_argument("--ayah", required=True)
    record_session.add_argument(
        "--conversation",
        required=True,
        choices=(
            "scope-micro",
            "scope-macro",
            "scope-global",
            "scope-reconciler",
            "canonical-writer",
            "reader-map-writer",
            "invitation-writer",
        ),
    )
    record_session.add_argument("--session-id", required=True)
    record_session.add_argument("--prompt-manifest", required=True, type=Path)
    record_session.set_defaults(func=record_authoring_session)

    record_turn = subparsers.add_parser(
        "record-turn",
        help="Bind a completed canonical writer turn to exact output hashes",
    )
    record_turn.add_argument("--ayah", required=True)
    record_turn.add_argument("--session-id", required=True)
    record_turn.add_argument("--prompt-manifest", required=True, type=Path)
    record_turn.add_argument("--prior-receipt", type=Path)
    record_turn.set_defaults(func=record_authoring_turn)
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    try:
        result = args.func(args)
        if result is not None:
            print(_pretty_json(result), end="")
        return 0
    except WorkflowError as exc:
        print(
            _pretty_json(
                {
                    "status": "error",
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                }
            ),
            file=sys.stderr,
            end="",
        )
        return 2
    except SystemExit as exc:
        if exc.code in (None, 0):
            return 0
        message = exc.code if isinstance(exc.code, str) else str(exc)
        print(
            _pretty_json(
                {
                    "status": "error",
                    "error_type": "SystemExit",
                    "message": message,
                }
            ),
            file=sys.stderr,
            end="",
        )
        return exc.code if isinstance(exc.code, int) else 2


if __name__ == "__main__":
    raise SystemExit(main())
