#!/usr/bin/env python3
"""Prepare the three hermetic scope prompts for commentary v5."""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


V5_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V5_ROOT.parents[1]
V3_ROOT = V5_ROOT.parent / "v3"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
PROMPTS_ROOT = V5_ROOT / "prompts"
INPUT_ROOT = V5_ROOT / "input"
RAW_ROOT = V5_ROOT / "raw"
EDITORIAL_ROOT = V5_ROOT / "editorial"
DEFAULT_CONTEXT_BUNDLES_DIR = REPO_ROOT / "bundles"
LANES = ("micro", "macro", "global")
MAX_BATCH_UNITS = 512
MAX_JSON_BYTES = 128_000_000
MAX_SCOPE_PROMPT_BYTES = 16_000_000
SCOPE_DISCOVERY_SCHEMA_VERSION = "commentary-v5-scope-discovery-v1"
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
INTER_AYAH_FILE_RE = re.compile(
    r"focus_([1-9][0-9]*)_([1-9][0-9]*)_cutoff_100\.tsv"
)
INTER_AYAH_SINGLE_REF_RE = re.compile(r"[1-9][0-9]*:[1-9][0-9]*")
INTER_AYAH_RANGE_REF_RE = re.compile(
    r"([1-9][0-9]*):([1-9][0-9]*)-([1-9][0-9]*)"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}")
INTER_AYAH_LABELS = frozenset({
    "strong",
    "medium",
    "weak",
    "no value",
    "contrast",
    "reject",
})
MEANINGFUL_INTER_AYAH_LABELS = INTER_AYAH_LABELS - {"no value", "reject"}
INTER_AYAH_RECORD_TYPES = frozenset({
    "directional_review",
    "reciprocal_nomination",
    "reciprocal_counterevidence",
    "self_reiteration",
})
INTER_AYAH_ALIAS_SOURCE_TYPES = {
    "surface_alias_directional_evidence": "directional_review",
    "surface_alias_reciprocal_nomination": "reciprocal_nomination",
    "surface_alias_reciprocal_counterevidence": "reciprocal_counterevidence",
    "surface_alias_self_reiteration": "self_reiteration",
}
INTER_AYAH_NUMBERED_COLUMNS = (
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
INTER_AYAH_PREFATORY_COLUMNS = INTER_AYAH_NUMBERED_COLUMNS + (
    "source_record_type",
    "linguistic_source_ref",
    "projection_basis",
    "source_relation_scope",
    "host_authored",
)
INTER_AYAH_PREFATORY_PROJECTION_BASIS = (
    "normalized_prefatory_basmala_surface_equivalence_v1"
)
QURAN_AYAH_COUNTS = (
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109,
    123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60,
    34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45,
    60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44,
    28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20,
    15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3,
    5, 4, 5, 6,
)

sys.path.insert(0, str(V5_ROOT))
sys.path.insert(0, str(V3_ROOT))
sys.path.insert(0, str(SCRIPTS_ROOT))
sys.path.insert(0, str(REPO_ROOT))
from _commentary.v5 import composition as compositions  # noqa: E402
import render_authoring as v3  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402
from v3lib.prepare import (  # noqa: E402
    PrepareOptions,
    build_prepared_artifacts,
    validate_docket,
)


PREPARE_OPTIONS = PrepareOptions(
    hft_policy="quarantine",
    max_optional_candidates=80,
    max_support_chars=8_000,
)


class WorkflowError(RuntimeError):
    """Raised when required inputs cannot form hermetic scope prompts."""


@dataclass(frozen=True)
class Layout:
    ayah_ref: str
    analysis_id: str
    stem: str
    input: Path
    raw: Path
    editorial: Path

    def scope_prompt(self, lane: str) -> Path:
        return self.input / f"{lane}.discovery.prompt.md"

    def scope_discovery(self, lane: str) -> Path:
        return self.raw / f"{lane}.discovery.json"

    def scope_prose(self, lane: str) -> Path:
        return self.raw / f"{lane}.scope.tr.md"


def layout_for(ayah_ref: str, analysis_id: str = "native") -> Layout:
    if compositions.ANALYSIS_ID_RE.fullmatch(analysis_id) is None:
        raise WorkflowError(f"Invalid analysis ID: {analysis_id!r}")
    match = re.fullmatch(r"([1-9][0-9]*):(0|[1-9][0-9]*)", ayah_ref)
    if match is None:
        raise WorkflowError(f"Invalid Quran unit reference: {ayah_ref!r}")
    surah, ayah = (int(value) for value in match.groups())
    if not 1 <= surah <= 114:
        raise WorkflowError(f"Surah is outside 1-114: {ayah_ref}")
    if ayah == 0 and surah in compositions.BASMALA_EXCLUDED_SURAHS:
        reason = "S1 uses 1:1" if surah == 1 else "S9 has no prefatory basmala"
        raise WorkflowError(f"Invalid prefatory unit {ayah_ref}: {reason}")
    folder = f"s{surah:03d}"
    stem = f"{surah}_{ayah}"
    return Layout(
        ayah_ref=ayah_ref,
        analysis_id=analysis_id,
        stem=stem,
        input=INPUT_ROOT / analysis_id / folder / stem,
        raw=RAW_ROOT / analysis_id / folder / stem,
        editorial=EDITORIAL_ROOT / analysis_id / folder / stem,
    )


def _expand_ayah_selectors(selectors: list[str] | str) -> list[str]:
    try:
        refs = compositions.expand_selectors(selectors)
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if len(refs) > MAX_BATCH_UNITS:
        raise WorkflowError(f"A batch may contain at most {MAX_BATCH_UNITS} units")
    return refs


def _is_prefatory_ref(ref: str) -> bool:
    return bool(re.fullmatch(r"[1-9][0-9]*:0", ref))


def _analysis_id(args: argparse.Namespace) -> str:
    value = getattr(args, "analysis_id", None) or "native"
    if compositions.ANALYSIS_ID_RE.fullmatch(value) is None:
        raise WorkflowError(f"Invalid analysis ID: {value!r}")
    return value


def _repo_path(path: Path) -> str:
    try:
        return str(path.resolve(strict=False).relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve(strict=False))


def _assert_confined(path: Path, root: Path) -> None:
    absolute_path = Path(os.path.abspath(path))
    absolute_root = Path(os.path.abspath(root))
    if absolute_root.is_symlink():
        raise WorkflowError(f"Generated root is a symlink: {absolute_root}")
    try:
        relative = absolute_path.relative_to(absolute_root)
    except ValueError as exc:
        raise WorkflowError(f"Generated path escapes {absolute_root}: {path}") from exc
    candidate = absolute_root
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            raise WorkflowError(f"Generated path crosses a symlink: {candidate}")


def _atomic_write(path: Path, payload: bytes, *, root: Path) -> None:
    _assert_confined(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise WorkflowError(f"Refusing to replace non-regular artifact: {path}")
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _load_json_object(path: Path) -> tuple[bytes, dict[str, Any]]:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read {path}: {exc}") from exc
    if len(payload) > MAX_JSON_BYTES:
        raise WorkflowError(f"JSON input exceeds {MAX_JSON_BYTES} bytes: {path}")
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WorkflowError(f"Invalid JSON object in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise WorkflowError(f"Expected one JSON object in {path}")
    return payload, value


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _render(template: str, replacements: dict[str, str], *, label: str) -> str:
    expected = set(MARKER_RE.findall(template))
    supplied = set(replacements)
    if expected != supplied:
        raise WorkflowError(
            f"{label} marker mismatch; missing={sorted(expected - supplied)}, "
            f"extra={sorted(supplied - expected)}"
        )
    rendered = template
    for marker, replacement in replacements.items():
        rendered = rendered.replace(marker, replacement)
    return rendered


def _quran_text_projection(
    source_path: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    try:
        return v3._quran_text_evidence(source_path)
    except SystemExit as exc:
        raise WorkflowError(str(exc)) from exc


def _numbered_surah_refs(
    quran_evidence: dict[str, dict[str, Any]], surah: int
) -> tuple[str, ...]:
    expected = tuple(
        f"{surah}:{ayah}" for ayah in range(1, QURAN_AYAH_COUNTS[surah - 1] + 1)
    )
    missing = [ref for ref in expected if ref not in quran_evidence]
    if missing:
        raise WorkflowError(
            f"Quran text lacks the complete numbered ayat for surah {surah}: {missing}"
        )
    return expected


def _automatic_basmala_composition(
    focus_ref: str, quran_evidence: dict[str, dict[str, Any]]
) -> compositions.Composition:
    surah = int(focus_ref.split(":", 1)[0])
    numbered = _numbered_surah_refs(quran_evidence, surah)
    return compositions.composition_from_cli(
        f"s{surah:03d}-basmala-full",
        [f"host={focus_ref},{surah}:1-{len(numbered)}"],
        [focus_ref],
    )


def _validate_basmala_focus_context(
    composition: compositions.Composition,
    quran_evidence: dict[str, dict[str, Any]],
) -> None:
    for focus_ref in composition.focus_refs:
        if not _is_prefatory_ref(focus_ref):
            continue
        surah = int(focus_ref.split(":", 1)[0])
        required = (focus_ref, *_numbered_surah_refs(quran_evidence, surah))
        actual = tuple(
            ref
            for ref in composition.segment_for(focus_ref).refs
            if ref.startswith(f"{surah}:")
        )
        if actual != required:
            raise WorkflowError(
                f"Prefatory focus {focus_ref} requires its complete numbered host "
                "surah, in canonical order, in the same segment"
            )


def _docket_payload_hash(docket: dict[str, Any]) -> str:
    payload = copy.deepcopy(docket)
    payload.get("identity", {}).pop("docket_payload_sha256", None)
    return v3._sha256_json(payload)


def _basmala_docket_template(source_bundle: dict[str, Any]) -> dict[str, Any]:
    template = copy.deepcopy(source_bundle)
    template.update({
        "unit_kind": "numbered_ayah",
        "surah": 1,
        "ayah": 1,
        "ayahRef": "1:1",
        "surface_ref": "1:1",
        "linguistic_source_ref": "1:1",
        "v12_reader_responses": {},
        "v12_reader_walks": {},
        "v12_reader_walks_wide": {},
        "v12_cross_run_publication": None,
        "butuncul_okuma_line": None,
        "inter_ayah_rows": [],
        "channel_subchannels_anchored_here": [],
        "channel_generated_outputs": {},
        "pericope": {
            "surah": 1,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 1,
            "label": "Canonical basmala linguistic template",
            "synthesized": True,
        },
    })
    template.pop("v12_focus_trace_hermetic", None)
    return template


def _adapt_basmala_docket(
    source_bundle: dict[str, Any], template_docket: dict[str, Any]
) -> dict[str, Any]:
    target_ref = str(source_bundle.get("ayahRef"))
    docket = copy.deepcopy(template_docket)
    intrinsic_types = {"qac_morpheme", "word_analysis"}
    candidates = [
        candidate
        for candidate in docket.get("candidates", [])
        if isinstance(candidate, dict)
        and candidate.get("source_type") in intrinsic_types
    ]
    support_ids = {
        support_id
        for candidate in candidates
        for support_id in candidate.get("support_ids", [])
        if isinstance(support_id, str)
    }
    for candidate in candidates:
        candidate.update({
            "ayah_ref": target_ref,
            "surface_ref": target_ref,
            "linguistic_source_ref": "1:1",
        })
    docket["candidates"] = candidates
    docket["support_registry"] = [
        support
        for support in docket.get("support_registry", [])
        if isinstance(support, dict) and support.get("support_id") in support_ids
    ]
    docket["identity"] = {
        "ayah_ref": target_ref,
        "source_canonical_sha256": v3._sha256_json(source_bundle),
        "docket_payload_sha256": "",
    }
    docket["focus"].update({
        "arabic_uthmani": source_bundle["text"]["arabic_uthmani"],
        "surface_ref": target_ref,
        "linguistic_source_ref": "1:1",
    })
    docket["scope"]["pericope"] = {
        "id": f"s{int(target_ref.split(':', 1)[0]):03d}-prefatory-basmala",
        "number": 0,
        "label": "Prefatory basmala focus",
        "ayah_from": 0,
        "ayah_to": 0,
        "refs": [target_ref],
    }
    docket["scope"]["hft"] = {
        "status": "not_applicable",
        "adjudicable": False,
        "reasons": ["prefatory basmala has no native HFT focus run"],
        "packet": None,
        "readers": [],
    }
    docket["adjudication_gate"] = {
        **docket.get("adjudication_gate", {}),
        "ready": True,
        "mode": "prefatory_basmala_linguistic_alias",
    }
    docket["identity"]["docket_payload_sha256"] = _docket_payload_hash(docket)
    return docket


def _focus_bundle_path(
    args: argparse.Namespace,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> Path:
    if args.source_bundle is not None:
        return Path(args.source_bundle)
    root = member_bundles_dir if _is_prefatory_ref(args.ayah) else context_bundles_dir
    return compositions.unit_bundle_path(root, args.ayah)


def _load_focus_inputs(
    args: argparse.Namespace,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    source_path = _focus_bundle_path(args, context_bundles_dir, member_bundles_dir)
    source_payload, source_bundle = _load_json_object(source_path)
    try:
        identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=args.ayah
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc

    if args.docket is not None:
        _payload, docket = _load_json_object(Path(args.docket))
        try:
            validate_docket(docket)
        except ValidationError as exc:
            raise WorkflowError(f"Invalid docket {args.docket}: {exc}") from exc
    else:
        template = (
            _basmala_docket_template(source_bundle)
            if identity["unit_kind"] == "prefatory_basmala"
            else source_bundle
        )
        template_payload = (
            _canonical_json(template).encode("utf-8")
            if template is not source_bundle
            else source_payload
        )
        try:
            _prepared, docket = build_prepared_artifacts(
                template,
                source_path=source_path,
                source_raw=template_payload,
                options=PREPARE_OPTIONS,
            )
        except ValidationError as exc:
            raise WorkflowError(
                f"Cannot prepare focus bundle {source_path}: {exc}"
            ) from exc

    if identity["unit_kind"] == "prefatory_basmala":
        docket = _adapt_basmala_docket(source_bundle, docket)
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise WorkflowError("Docket ayah identity does not match the focus")
    if docket.get("identity", {}).get("source_canonical_sha256") != v3._sha256_json(
        source_bundle
    ):
        raise WorkflowError("Docket does not belong to the selected focus bundle")
    return source_bundle, docket


def _inter_ayah_source_target_components(source_target_ref: str) -> tuple[str, ...]:
    if INTER_AYAH_SINGLE_REF_RE.fullmatch(source_target_ref):
        return (source_target_ref,)
    match = INTER_AYAH_RANGE_REF_RE.fullmatch(source_target_ref)
    if match is None:
        return ()
    surah, first, last = map(int, match.groups())
    if first > last or last - first + 1 > max(QURAN_AYAH_COUNTS):
        return ()
    return tuple(f"{surah}:{ayah}" for ayah in range(first, last + 1))


def _load_inter_ayah_projection(
    focus_ref: str,
    source_dir: Path,
    directional_source_dir: Path,
    quran_evidence: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]], dict[str, Any]]:
    surah, ayah = (int(value) for value in focus_ref.split(":"))
    prefatory = ayah == 0
    name = f"focus_{surah}_{ayah}_cutoff_100.tsv"
    path = source_dir / "prefatory" / name if prefatory else source_dir / name
    columns = INTER_AYAH_PREFATORY_COLUMNS if prefatory else INTER_AYAH_NUMBERED_COLUMNS
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"Static inter-ayah document is missing: {path}")
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise WorkflowError(f"Cannot read static inter-ayah document {path}: {exc}") from exc
    if not lines or tuple(lines[0].split("\t")) != columns:
        raise WorkflowError(f"Static inter-ayah document has an invalid header: {path}")

    numbered_refs = {
        ref for ref in quran_evidence if ref.split(":", 1)[1] != "0"
    }
    directional_rows: list[dict[str, Any]] = []
    reciprocal: dict[str, list[dict[str, Any]]] = {}
    self_reiteration_count = 0
    for line_number, line in enumerate(lines[1:], 2):
        fields = line.split("\t")
        if len(fields) != len(columns):
            raise WorkflowError(
                f"Malformed static inter-ayah row at {path}:{line_number}"
            )
        raw = dict(zip(columns, fields))
        target_ref = raw["target_ref"]
        component_ref = raw["source_target_component_ref"]
        source_file_match = INTER_AYAH_FILE_RE.fullmatch(raw["source_file"])
        components = _inter_ayah_source_target_components(raw["source_target_ref"])
        if (
            raw["focus_ref"] != focus_ref
            or target_ref not in numbered_refs
            or component_ref not in numbered_refs
            or component_ref not in components
            or any(ref not in numbered_refs for ref in components)
            or raw["source_direction_label"] not in INTER_AYAH_LABELS
            or source_file_match is None
            or not raw["source_line"].isdigit()
            or int(raw["source_line"]) < 1
            or SHA256_RE.fullmatch(raw["source_row_sha256"]) is None
            or raw["source_column_order"]
            not in {"label_target_note", "target_label_note"}
        ):
            raise WorkflowError(
                f"Malformed static inter-ayah row at {path}:{line_number}"
            )
        source_focus_ref = (
            f"{int(source_file_match.group(1))}:{int(source_file_match.group(2))}"
        )
        if source_focus_ref not in numbered_refs:
            raise WorkflowError(
                f"Unknown source focus in static inter-ayah row at {path}:{line_number}"
            )
        source_line = int(raw["source_line"])
        expected_row_role = (
            "ranked_review" if source_line <= 100 else "missing_ayah_suggestion"
        )
        source_scope = (
            "same_surah"
            if source_focus_ref.split(":", 1)[0]
            == component_ref.split(":", 1)[0]
            else "cross_surah"
        )
        host_scope = (
            "same_surah"
            if str(surah) == target_ref.split(":", 1)[0]
            else "cross_surah"
        )
        if (
            raw["source_focus_ref"] != source_focus_ref
            or raw["source_row_role"] != expected_row_role
        ):
            raise WorkflowError(
                f"Broken inter-ayah source provenance at {path}:{line_number}"
            )
        projection_type = raw["record_type"]
        source_label = raw["source_direction_label"]
        expected_reciprocal_type = (
            "self_reiteration"
            if source_focus_ref == component_ref
            else (
                "reciprocal_nomination"
                if source_label in MEANINGFUL_INTER_AYAH_LABELS
                else "reciprocal_counterevidence"
            )
        )
        if prefatory:
            source_type = raw["source_record_type"]
            source_shape_valid = (
                source_type == "directional_review"
                and source_focus_ref == "1:1"
                and target_ref == component_ref
            ) or (
                source_type == expected_reciprocal_type
                and component_ref == "1:1"
                and target_ref == source_focus_ref
            )
            if (
                INTER_AYAH_ALIAS_SOURCE_TYPES.get(projection_type) != source_type
                or not source_shape_valid
                or raw["linguistic_source_ref"] != "1:1"
                or raw["projection_basis"]
                != INTER_AYAH_PREFATORY_PROJECTION_BASIS
                or raw["host_authored"] != "false"
                or raw["focus_direction_label"]
                or raw["relation_scope"] != host_scope
                or raw["source_relation_scope"] != source_scope
            ):
                raise WorkflowError(
                    f"Malformed prefatory inter-ayah row at {path}:{line_number}"
                )
            effective_type = (
                "self_reiteration"
                if source_type == "self_reiteration"
                else (
                    "reciprocal_nomination"
                    if source_label in MEANINGFUL_INTER_AYAH_LABELS
                    else "reciprocal_counterevidence"
                )
            )
        else:
            if projection_type not in INTER_AYAH_RECORD_TYPES:
                raise WorkflowError(
                    f"Unknown inter-ayah row type at {path}:{line_number}"
                )
            directional_shape = (
                projection_type == "directional_review"
                and source_focus_ref == focus_ref
                and target_ref == component_ref
                and raw["focus_direction_label"] == source_label
            )
            reciprocal_shape = (
                projection_type == expected_reciprocal_type
                and component_ref == focus_ref
                and target_ref == source_focus_ref
                and not raw["focus_direction_label"]
            )
            if not (directional_shape or reciprocal_shape):
                raise WorkflowError(
                    f"Broken inter-ayah row direction at {path}:{line_number}"
                )
            if raw["relation_scope"] != source_scope:
                raise WorkflowError(
                    f"Broken inter-ayah relation scope at {path}:{line_number}"
                )
            effective_type = projection_type

        is_range = len(components) > 1
        common = {
            "record_type": effective_type,
            "projection_record_type": projection_type,
            "source_direction_label": source_label,
            "source_focus_ref": source_focus_ref,
            "source_target_ref": raw["source_target_ref"],
            "source_target_component_ref": component_ref,
            "source_target_is_range": is_range,
            "source_target_components": list(components),
            "source_target_range_boundary": (
                "The source note applies to the complete range; assess this "
                "component only for features present in its supplied Arabic."
                if is_range
                else None
            ),
            "source_note": raw["source_note"],
            "source_column_order": raw["source_column_order"],
            "source_row_role": raw["source_row_role"],
            "source_file": raw["source_file"],
            "source_line": int(raw["source_line"]),
            "source_pointer": (
                f"{_repo_path(directional_source_dir / raw['source_file'])}"
                f"#L{raw['source_line']}"
            ),
            "projection_pointer": f"{_repo_path(path)}#L{line_number}",
            "source_row_sha256": raw["source_row_sha256"],
            "projection_record_sha256": v3._sha256_json(raw),
            "relation_scope": raw["relation_scope"],
        }
        if prefatory:
            common.update({
                "surface_alias_projection": True,
                "host_authored": False,
                "source_record_type": raw["source_record_type"],
                "linguistic_source_ref": "1:1",
                "projection_basis": raw["projection_basis"],
                "source_relation_scope": raw["source_relation_scope"],
            })
            if effective_type == "self_reiteration":
                self_reiteration_count += 1
            else:
                reciprocal.setdefault(target_ref, []).append({
                    "receiving_direction_label": None,
                    **common,
                })
        elif projection_type == "directional_review":
            directional_rows.append({
                "ref": target_ref,
                "label": raw["focus_direction_label"],
                "note": raw["source_note"],
                **common,
            })
        elif projection_type == "self_reiteration":
            self_reiteration_count += 1
        else:
            reciprocal.setdefault(target_ref, []).append({
                "receiving_direction_label": None,
                **common,
            })

    reciprocal = dict(
        sorted(
            reciprocal.items(),
            key=lambda item: tuple(int(value) for value in item[0].split(":")),
        )
    )
    coverage = {
        "source_id": "quran-data/static-reciprocal-selected-document",
        "source_document": _repo_path(path),
        "document_family": (
            "prefatory_surface_alias" if prefatory else "numbered_reciprocal"
        ),
        "directional_review_row_count": len(directional_rows),
        "reciprocal_row_count": sum(len(rows) for rows in reciprocal.values()),
        "self_reiteration_row_count": self_reiteration_count,
        "surface_alias_projection": prefatory,
    }
    return directional_rows, reciprocal, coverage


def _load_added_ayah_bundle(
    package_root: Path, member_root: Path, ref: str
) -> tuple[Path, dict[str, Any]]:
    package_path = compositions.unit_bundle_path(package_root, ref)
    member_path = compositions.unit_bundle_path(member_root, ref)
    package_present = package_path.is_file() and not package_path.is_symlink()
    member_present = member_path.is_file() and not member_path.is_symlink()
    if not package_present and not member_present:
        raise WorkflowError(
            f"Added ayah {ref} is unavailable in both package and member roots"
        )
    try:
        package = (
            compositions.load_unit_bundle(package_root, ref)
            if package_present
            else None
        )
        member = (
            package
            if package_root.resolve(strict=False) == member_root.resolve(strict=False)
            else (
                compositions.load_unit_bundle(member_root, ref)
                if member_present
                else None
            )
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if package is not None and member is not None:
        if package[2]["canonical_sha256"] != member[2]["canonical_sha256"]:
            raise WorkflowError(
                f"Added ayah {ref} differs between package and member roots"
            )
        return package[0], package[1]
    selected = package or member
    assert selected is not None
    return selected[0], selected[1]


def _composition_context(
    composition: compositions.Composition | None,
    focus_ref: str,
    focus_bundle: dict[str, Any],
    package_root: Path,
    member_root: Path,
) -> dict[str, list[dict[str, Any]]]:
    by_lane: dict[str, list[dict[str, Any]]] = {lane: [] for lane in LANES}
    if composition is None:
        return by_lane
    loaded: dict[str, tuple[Path, dict[str, Any]]] = {}
    for row in composition.context_rows(focus_ref):
        ref = row["ref"]
        if ref not in loaded:
            try:
                if row.get("membership_added_ayah") is True:
                    loaded[ref] = _load_added_ayah_bundle(
                        package_root, member_root, ref
                    )
                else:
                    root = member_root if _is_prefatory_ref(ref) else package_root
                    path, bundle, _identity = compositions.load_unit_bundle(root, ref)
                    loaded[ref] = (path, bundle)
            except compositions.CompositionError as exc:
                raise WorkflowError(str(exc)) from exc
        _path, bundle = loaded[ref]
        by_lane[row["lane"]].append(
            compositions.project_context_unit(
                context_row=row,
                bundle=bundle,
                focus_bundle=focus_bundle,
            )
        )
    return by_lane


def _required_host_basmala(
    focus_bundle: dict[str, Any],
    member_root: Path,
    composition: compositions.Composition | None,
) -> tuple[Path, dict[str, Any], dict[str, Any]] | None:
    if focus_bundle.get("unit_kind", "numbered_ayah") != "numbered_ayah":
        return None
    surah = composition.member_surah if composition is not None else None
    if surah is None:
        surah = int(focus_bundle["surah"])
    if int(focus_bundle["surah"]) != surah:
        raise WorkflowError("Focus does not belong to the declared host surah")
    if surah in compositions.BASMALA_EXCLUDED_SURAHS:
        return None
    ref = f"{surah}:0"
    try:
        return compositions.load_unit_bundle(member_root, ref)
    except compositions.CompositionError as exc:
        raise WorkflowError(
            f"Mandatory host basmala {ref} could not be loaded: {exc}"
        ) from exc


def _append_host_basmala(
    units: list[dict[str, Any]],
    *,
    focus_bundle: dict[str, Any],
    basmala: tuple[Path, dict[str, Any], dict[str, Any]] | None,
) -> None:
    if basmala is None:
        return
    _path, bundle, identity = basmala
    ref = identity["ayah_ref"]
    for unit in units:
        if unit.get("ayah_ref") == ref:
            unit["context_kind"] = "host_prefatory_basmala"
            unit["automatic_prefatory_basmala_membership"] = True
            return
    unit = compositions.project_context_unit(
        context_row={
            "ref": ref,
            "lane": "macro",
            "membership_added_ayah": False,
        },
        bundle=bundle,
        focus_bundle=focus_bundle,
    )
    unit["context_kind"] = "host_prefatory_basmala"
    unit["automatic_prefatory_basmala_membership"] = True
    units.insert(0, unit)


def _prefatory_focus_evidence(source_bundle: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "v12_reader_responses",
        "v12_reader_walks",
        "v12_reader_walks_wide",
        "v12_cross_run_publication",
        "butuncul_okuma_line",
        "channel_subchannels_anchored_here",
        "channel_generated_outputs",
    )
    return {
        "ayah_ref": source_bundle["ayahRef"],
        "surface_ref": source_bundle["surface_ref"],
        "linguistic_source_ref": source_bundle["linguistic_source_ref"],
        "payload": {
            field: source_bundle[field]
            for field in fields
            if source_bundle.get(field) not in (None, {}, [], "")
        },
    }


def _strip_audit_fields(value: Any) -> Any:
    if isinstance(value, list):
        return [_strip_audit_fields(item) for item in value]
    if not isinstance(value, dict):
        return value
    return {
        key: _strip_audit_fields(item)
        for key, item in value.items()
        if not key.endswith("_sha256")
    }


def _build_lane_packet(
    *,
    lane: str,
    docket: dict[str, Any],
    source_bundle: dict[str, Any],
    hft_projection: dict[str, Any],
    inter_rows: list[dict[str, Any]],
    reciprocal: dict[str, list[dict[str, Any]]],
    inter_coverage: dict[str, Any],
    quran_evidence: dict[str, dict[str, Any]],
    quran_coverage: dict[str, Any],
    composition: compositions.Composition | None,
    context_by_lane: dict[str, list[dict[str, Any]]],
    host_basmala: tuple[Path, dict[str, Any], dict[str, Any]] | None,
) -> dict[str, Any]:
    try:
        packet = v3._lane_packet(
            docket,
            lane,
            source_bundle,
            hft_projection,
            inter_rows,
            reciprocal,
            inter_coverage,
            quran_evidence,
            quran_coverage,
        )
    except SystemExit as exc:
        raise WorkflowError(str(exc)) from exc

    units = copy.deepcopy(context_by_lane[lane])
    if lane == "macro":
        _append_host_basmala(
            units,
            focus_bundle=source_bundle,
            basmala=host_basmala,
        )
    packet["selected_context_units"] = units
    if composition is not None:
        packet["analysis_context"] = {
            "analysis_id": composition.analysis_id,
            "focus_ref": source_bundle["ayahRef"],
            "ordered_context_refs": list(
                composition.context_refs(source_bundle["ayahRef"])
            ),
            "lane_context_refs": [unit["ayah_ref"] for unit in units],
            "host_surah": composition.member_surah,
            "external_ayat_refs": list(composition.added_ayat_refs),
        }
    if source_bundle.get("unit_kind") == "prefatory_basmala" and lane == "global":
        packet["prefatory_focus_evidence"] = _prefatory_focus_evidence(source_bundle)
    packet["schema_version"] = "commentary-v5-hermetic-scope-packet-v1"
    packet["identity"] = {
        "ayah_ref": source_bundle["ayahRef"],
        "lane": lane,
        "unit_kind": source_bundle.get("unit_kind", "numbered_ayah"),
        "surface_ref": source_bundle.get("surface_ref", source_bundle["ayahRef"]),
        "linguistic_source_ref": source_bundle.get(
            "linguistic_source_ref", source_bundle["ayahRef"]
        ),
    }
    packet.pop("source_coverage", None)
    packet.pop("contract", None)
    return _strip_audit_fields(packet)


def _canonical_inputs() -> dict[str, str]:
    paths = {
        "principles": REPO_ROOT / "PRINCIPLES.md",
        "commentary_spec": REPO_ROOT / "COMMENTARY_SPEC.md",
        "channels": REPO_ROOT / "docs" / "CHANNELS.md",
        "canonical_prompt_v2": REPO_ROOT / "_ayah_commentary" / "v2" / "PROMPT.md",
    }
    try:
        return {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
    except OSError as exc:
        raise WorkflowError(f"Cannot read governing instructions: {exc}") from exc


def _lane_specific_procedure(lane: str, packet: dict[str, Any]) -> str:
    if lane != "macro":
        return "- No additional lane-specific procedure."

    analysis_context = packet.get("analysis_context") or {}
    external_refs = [
        ref for ref in analysis_context.get("external_ayat_refs", []) if isinstance(ref, str)
    ]
    if not external_refs:
        return (
            "- Macro has no explicitly added external ayat. Assess the declared "
            "pericope or host-surah context, including any automatic host basmala, "
            "as ordinary non-focus context."
        )

    external_display = ", ".join(external_refs)
    return "\n".join(
        [
            (
                "- Macro has explicitly added external ayat: "
                f"{external_display}. Treat them as an overlay, not as the "
                "starting frame."
            ),
            (
                "- Phase 1: assess the focus against the declared pericope or "
                "host-surah context and any automatic host basmala. During this "
                "phase, quarantine explicitly added external ayat: do not let them "
                "nominate, rank, suppress, or reframe native/pericope findings."
            ),
            (
                "- Phase 2: review only the explicitly added external ayat and ask "
                "what genuine delta they add beyond Phase 1. Retain an external "
                "overlay finding only when it creates a specific carrier, trigger, "
                "contact, changed reading, semantic detail, and boundary. Reject "
                "external material that only restates a native/pericope finding or "
                "imports a whole-surah theme without a local contact."
            ),
            (
                "- If all ayat of a surah were supplied externally, still treat "
                "them as individually listed ayat, not as an implicit whole-surah "
                "reading. Cite and land only the individual external ayat that "
                "actually trigger the finding."
            ),
        ]
    )


def _build_scope_prompt(layout: Layout, lane: str, packet: dict[str, Any]) -> str:
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "discovery.md"
    try:
        template = template_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise WorkflowError(f"Cannot read scope prompt template: {exc}") from exc
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@DISCOVERY_OUTPUT_PATH@@": _repo_path(layout.scope_discovery(lane)),
            "@@SCOPE_DISCOVERY_SCHEMA_VERSION@@": SCOPE_DISCOVERY_SCHEMA_VERSION,
            "@@PRINCIPLES_MD@@": governing["principles"],
            "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
            "@@CHANNELS_MD@@": governing["channels"],
            "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
            "@@LANE_SPECIFIC_PROCEDURE@@": _lane_specific_procedure(lane, packet),
            "@@LANE_PACKET_JSON@@": _canonical_json(packet),
        },
        label=f"{lane} scope prompt",
    )
    if len(prompt.encode("utf-8")) > MAX_SCOPE_PROMPT_BYTES:
        raise WorkflowError(
            f"{lane} hermetic scope prompt exceeds {MAX_SCOPE_PROMPT_BYTES} bytes"
        )
    return prompt


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    layout = layout_for(args.ayah, _analysis_id(args))
    composition = getattr(args, "composition", None)
    context_root = Path(args.context_bundles_dir).resolve(strict=False)
    member_root = Path(args.member_bundles_dir).resolve(strict=False)
    source_bundle, docket = _load_focus_inputs(args, context_root, member_root)
    quran_evidence, quran_coverage = _quran_text_projection(Path(args.quran_text))
    if composition is not None:
        _validate_basmala_focus_context(composition, quran_evidence)
    inter_rows, reciprocal, inter_coverage = _load_inter_ayah_projection(
        args.ayah,
        Path(args.inter_ayah_dir),
        Path(args.inter_ayah_parent_dir),
        quran_evidence,
    )
    try:
        hft_projection = v3._hft_authoring_projection(docket, source_bundle)
    except SystemExit as exc:
        raise WorkflowError(str(exc)) from exc
    context_by_lane = _composition_context(
        composition,
        args.ayah,
        source_bundle,
        context_root,
        member_root,
    )
    host_basmala = _required_host_basmala(
        source_bundle, member_root, composition
    )

    prompts: dict[str, str] = {}
    for lane in LANES:
        packet = _build_lane_packet(
            lane=lane,
            docket=docket,
            source_bundle=source_bundle,
            hft_projection=hft_projection,
            inter_rows=inter_rows,
            reciprocal=reciprocal,
            inter_coverage=inter_coverage,
            quran_evidence=quran_evidence,
            quran_coverage=quran_coverage,
            composition=composition,
            context_by_lane=context_by_lane,
            host_basmala=host_basmala,
        )
        prompts[lane] = _build_scope_prompt(layout, lane, packet)

    _assert_confined(layout.raw, RAW_ROOT)
    _assert_confined(layout.editorial, EDITORIAL_ROOT)
    layout.raw.mkdir(parents=True, exist_ok=True)
    layout.editorial.mkdir(parents=True, exist_ok=True)
    for lane, prompt in prompts.items():
        _atomic_write(
            layout.scope_prompt(lane),
            prompt.encode("utf-8"),
            root=INPUT_ROOT,
        )

    return {
        "schema_version": "commentary-v5-prepared-v1",
        "status": "prepared",
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "focus_context_brief": {
            "focus_ref": layout.ayah_ref,
            "analysis_id": layout.analysis_id,
            "context_refs": (
                list(composition.context_refs(layout.ayah_ref))
                if composition is not None
                else [
                    ref
                    for ref in docket.get("scope", {}).get("pericope", {}).get(
                        "refs", []
                    )
                    if ref != layout.ayah_ref
                ]
            ),
            "automatic_host_basmala_ref": (
                host_basmala[2]["ayah_ref"] if host_basmala is not None else None
            ),
            "external_ayat_refs": (
                list(composition.added_ayat_refs)
                if composition is not None
                else []
            ),
        },
        "handoffs": [
            {
                "lane": lane,
                "prompt": str(layout.scope_prompt(lane).resolve(strict=False)),
                "discovery_output": str(
                    layout.scope_discovery(lane).resolve(strict=False)
                ),
                "scope_prose_output": str(
                    layout.scope_prose(lane).resolve(strict=False)
                ),
                "composition_template": str(
                    (PROMPTS_ROOT / "composition.md").resolve(strict=False)
                ),
                "launch": "fresh_agent",
                "keep_session_open": True,
            }
            for lane in LANES
        ],
        "orchestration": {
            "scope_launch": "launch all three handoffs in parallel",
            "scope_follow_up": (
                "after nomination, fill prompts/composition.md and ask each same "
                "live agent to write its scope prose"
            ),
            "consolidation": (
                "close scope agents, then give the three scope prose texts and a "
                "short focus/context brief to one fresh consolidator"
            ),
            "editorial": (
                "ask that same consolidator for the editorial rewrite, then close"
            ),
            "post_launch_gates": [],
        },
        "generated_files": [
            str(layout.scope_prompt(lane).resolve(strict=False)) for lane in LANES
        ],
    }


def _source_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--docket", type=Path, help="Optional focus docket override.")
    parser.add_argument(
        "--source-bundle", type=Path, help="Optional focus bundle override."
    )
    parser.add_argument(
        "--inter-ayah-dir",
        type=Path,
        default=v3.DEFAULT_INTER_AYAH_DIR,
        help="Static reciprocal directory; only the selected focus TSV is read.",
    )
    parser.add_argument(
        "--inter-ayah-parent-dir",
        type=Path,
        default=v3.DEFAULT_INTER_AYAH_PARENT_DIR,
        help="Directional source root used for inline evidence pointers.",
    )
    parser.add_argument("--quran-text", type=Path, default=v3.DEFAULT_QURAN_TEXT)
    parser.add_argument(
        "--context-bundles-dir",
        type=Path,
        default=DEFAULT_CONTEXT_BUNDLES_DIR,
        help="Focus and ordered-context bundle root.",
    )
    parser.add_argument(
        "--member-bundles-dir",
        type=Path,
        default=DEFAULT_CONTEXT_BUNDLES_DIR,
        help="Mandatory host-basmala and external-ayah bundle root.",
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare three hermetic scope prompts for commentary v5."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser(
        "prepare", help="Run all preflight checks and write three scope prompts."
    )
    prepare_parser.add_argument(
        "--ayah",
        action="extend",
        nargs="+",
        metavar="REF_OR_RANGE",
        help="One or more refs or same-surah ranges; may be repeated.",
    )
    prepare_parser.add_argument("--analysis-id", default="native")
    prepare_parser.add_argument(
        "--segment",
        action="append",
        default=[],
        metavar="ID=REFS",
        help="Ordered composition segment; repeat for the complete sequence.",
    )
    prepare_parser.add_argument(
        "--analysis", type=Path, help="JSON composition file."
    )
    prepare_parser.add_argument(
        "--member-surah",
        type=int,
        help="Host surah for explicit context-only external ayat.",
    )
    prepare_parser.add_argument(
        "--add-ayat",
        "--add-member",
        dest="add_ayat",
        action="append",
        default=[],
        metavar="REF[,REF...]",
        help="Explicit comma-separated external ayat; ranges are not accepted.",
    )
    _source_options(prepare_parser)
    return parser


def _resolve_request(
    args: argparse.Namespace,
) -> tuple[list[str], compositions.Composition | None]:
    if args.analysis is not None and (args.segment or args.member_surah or args.add_ayat):
        raise WorkflowError(
            "--analysis cannot be combined with --segment/--member-surah/--add-ayat"
        )
    if args.add_ayat and args.member_surah is None:
        raise WorkflowError("--add-ayat requires --member-surah")
    if args.member_surah is not None and not args.add_ayat:
        raise WorkflowError("--member-surah requires at least one --add-ayat")
    if args.member_surah is not None and not args.segment:
        raise WorkflowError("--member-surah requires --segment definitions")

    composition: compositions.Composition | None = None
    if args.analysis is not None:
        try:
            composition = compositions.load_composition(args.analysis)
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        if args.analysis_id not in {"native", composition.analysis_id}:
            raise WorkflowError("--analysis-id disagrees with the composition file")
        args.analysis_id = composition.analysis_id
        refs = (
            _expand_ayah_selectors(args.ayah)
            if args.ayah
            else list(composition.focus_refs)
        )
    elif args.segment:
        if args.analysis_id == "native":
            raise WorkflowError("--segment requires a non-native --analysis-id")
        if not args.ayah:
            raise WorkflowError("--segment requires --ayah focus selectors")
        try:
            composition = compositions.composition_from_cli(
                args.analysis_id,
                args.segment,
                args.ayah,
                member_surah=args.member_surah,
                added_ayat_selectors=args.add_ayat,
            )
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        refs = list(composition.focus_refs)
    else:
        if not args.ayah:
            raise WorkflowError("--ayah is required without --analysis")
        refs = _expand_ayah_selectors(args.ayah)

    prefatory_refs = [ref for ref in refs if _is_prefatory_ref(ref)]
    if composition is None and prefatory_refs:
        if len(refs) != 1:
            raise WorkflowError("An S:0 focus must be prepared by itself")
        quran_evidence, _coverage = _quran_text_projection(Path(args.quran_text))
        composition = _automatic_basmala_composition(
            prefatory_refs[0], quran_evidence
        )
        args.analysis_id = composition.analysis_id
    if composition is not None:
        outside = sorted(set(refs) - set(composition.focus_refs))
        if outside:
            raise WorkflowError(
                f"Selected focuses are outside analysis {composition.analysis_id}: {outside}"
            )
    if len(refs) > 1 and (args.source_bundle is not None or args.docket is not None):
        raise WorkflowError(
            "--source-bundle and --docket may only be used for one focus"
        )
    return refs, composition


def _prepare_batch(
    args: argparse.Namespace,
    refs: list[str],
    composition: compositions.Composition | None,
) -> tuple[dict[str, Any], bool]:
    units: list[dict[str, Any]] = []
    handoffs: list[dict[str, Any]] = []
    errors = 0
    for ref in refs:
        unit_args = argparse.Namespace(
            **{**vars(args), "ayah": ref, "composition": composition}
        )
        try:
            result = prepare(unit_args)
            handoffs.extend(
                {**handoff, "ayah_ref": ref} for handoff in result["handoffs"]
            )
        except (WorkflowError, compositions.CompositionError, OSError) as exc:
            errors += 1
            result = {"ayah_ref": ref, "status": "error", "error": str(exc)}
        units.append(result)
    if errors:
        for unit in units:
            unit.pop("handoffs", None)
            unit.pop("orchestration", None)
            unit.pop("generated_files", None)
            if unit.get("status") == "prepared":
                unit["status"] = "withheld_due_to_batch_error"
    return (
        {
            "schema_version": "commentary-v5-prepared-batch-v1",
            "status": "prepared" if not errors else "error",
            "units": units,
            "parallel_handoffs": handoffs if not errors else [],
        },
        bool(errors),
    )


def main() -> int:
    args = _parser().parse_args()
    try:
        refs, composition = _resolve_request(args)
        if len(refs) == 1:
            result = prepare(
                argparse.Namespace(
                    **{**vars(args), "ayah": refs[0], "composition": composition}
                )
            )
            has_errors = False
        else:
            result, has_errors = _prepare_batch(args, refs, composition)
    except (WorkflowError, compositions.CompositionError, OSError) as exc:
        print(
            json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
