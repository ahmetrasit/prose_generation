#!/usr/bin/env python3
"""A fixed, Git-native commentary workflow with no persisted agent sessions."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


V4_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V4_ROOT.parents[1]
V3_ROOT = V4_ROOT.parent / "v3"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
V3_PROMPTS_ROOT = V3_ROOT / "prompts"
PROMPTS_ROOT = V4_ROOT / "prompts"
INPUT_ROOT = V4_ROOT / "input"
RAW_ROOT = V4_ROOT / "raw"
EDITORIAL_ROOT = V4_ROOT / "editorial"
LANES = ("micro", "macro", "global")
KINDS = ("prose", "evidence", "index", "friction")
MAX_JSON_BYTES = 128_000_000
MAX_LANE_PACKET_BYTES = 32_000_000
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
MAX_BATCH_UNITS = 512
DEFAULT_CONTEXT_BUNDLES_DIR = REPO_ROOT / "bundles"
PROJECTS_ROOT = REPO_ROOT.parent
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

# Reuse v3's evidence projection and exact request identity. The orchestration
# state machine is deliberately not imported or called.
sys.path.insert(0, str(V4_ROOT))
sys.path.insert(0, str(V3_ROOT))
sys.path.insert(0, str(SCRIPTS_ROOT))
import composition as compositions  # noqa: E402
import pericope_bundle_manifest as pericope_manifests  # noqa: E402
import render_authoring as v3  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402
from v3lib.prepare import (  # noqa: E402
    PrepareOptions,
    build_prepared_artifacts,
    validate_docket,
)


V4_PREPARE_OPTIONS = PrepareOptions(
    hft_policy="quarantine",
    max_support_chars=8_000,
)
UNIT_MANIFEST_SCHEMA_VERSION = "commentary-v4-unit-manifest-v5"
SCOPE_CONTRIBUTION_SCHEMA_VERSION = "commentary-v4-scope-contribution-v1"


class WorkflowError(RuntimeError):
    """Raised for a stale, mixed, or malformed v4 artifact set."""


@dataclass(frozen=True)
class Layout:
    ayah_ref: str
    stem: str
    input: Path
    raw: Path
    editorial: Path
    analysis_id: str = "native"

    def packet(self, lane: str) -> Path:
        return self.input / f"{lane}.packet.json"

    def scope_prompt(self, lane: str) -> Path:
        return self.input / f"{lane}.prompt.md"

    def scope_contribution(self, lane: str) -> Path:
        return self.raw / f"{lane}.contribution.json"

    @property
    def source_bundle(self) -> Path:
        return self.input / "source.bundle.json"

    @property
    def prefatory_basmala_bundle(self) -> Path:
        return self.input / "prefatory_basmala.bundle.json"

    @property
    def docket(self) -> Path:
        return self.input / "docket.json"

    @property
    def manifest(self) -> Path:
        return self.input / "manifest.json"

    @property
    def composition(self) -> Path:
        return self.input / "analysis.json"

    @property
    def canonical_prompt(self) -> Path:
        return self.input / "canonical.prompt.md"

    @property
    def editorial_prompt(self) -> Path:
        return self.input / "editorial.prompt.md"

    def first_pass(self, kind: str) -> Path:
        return self.raw / f"{self.stem}.{kind}.tr.md"

    def editorial_output(self, kind: str) -> Path:
        return self.editorial / f"{self.stem}.{kind}.editorial.tr.md"


def layout_for(ayah_ref: str, analysis_id: str = "native") -> Layout:
    if compositions.ANALYSIS_ID_RE.fullmatch(analysis_id) is None:
        raise WorkflowError(f"Invalid analysis ID: {analysis_id!r}")
    match = re.fullmatch(r"([1-9][0-9]*):(0|[1-9][0-9]*)", ayah_ref)
    if match is None:
        raise WorkflowError(f"Invalid Quran unit reference: {ayah_ref!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    if not 1 <= surah <= 114:
        raise WorkflowError(f"Surah is outside 1-114: {ayah_ref}")
    if ayah == 0 and surah in compositions.BASMALA_EXCLUDED_SURAHS:
        reason = "S1 uses 1:1" if surah == 1 else "S9 has no prefatory basmala"
        raise WorkflowError(f"Invalid prefatory unit {ayah_ref}: {reason}")
    folder = f"s{surah:03d}"
    stem = f"{surah}_{ayah}"
    return Layout(
        ayah_ref=ayah_ref,
        stem=stem,
        input=INPUT_ROOT / analysis_id / folder / stem,
        raw=RAW_ROOT / analysis_id / folder / stem,
        editorial=EDITORIAL_ROOT / analysis_id / folder / stem,
        analysis_id=analysis_id,
    )


def _expand_ayah_selectors(selectors: list[str] | str) -> list[str]:
    try:
        refs = compositions.expand_selectors(selectors)
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if len(refs) > MAX_BATCH_UNITS:
        raise WorkflowError(f"A batch may contain at most {MAX_BATCH_UNITS} units")
    return refs


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_json_bytes(value: Any, *, newline: bool = False) -> bytes:
    suffix = "\n" if newline else ""
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + suffix
    ).encode("utf-8")


def _pretty_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")


def _decode_json_object(payload: bytes, path: Path) -> dict[str, Any]:
    if len(payload) > MAX_JSON_BYTES:
        raise WorkflowError(f"JSON artifact exceeds {MAX_JSON_BYTES} bytes: {path}")
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WorkflowError(f"Invalid JSON object in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise WorkflowError(f"Expected one JSON object in {path}")
    return value


def _load_json_with_bytes(path: Path) -> tuple[bytes, dict[str, Any]]:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read {path}: {exc}") from exc
    return payload, _decode_json_object(payload, path)


def _load_json(path: Path) -> dict[str, Any]:
    return _load_json_with_bytes(path)[1]


def _quran_text_projection(
    source_path: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    try:
        resolved = source_path.resolve(strict=True)
        before = resolved.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot snapshot Quran text source {source_path}: {exc}") from exc
    evidence, coverage = v3._quran_text_evidence(resolved)
    stable_path = _manifest_source_path(resolved)
    if coverage.get("source_path") != stable_path:
        for row in evidence.values():
            pointer = row.get("source_pointer")
            if not isinstance(pointer, str) or "#L" not in pointer:
                raise WorkflowError("Quran text projection has a malformed source pointer")
            line_suffix = pointer.rsplit("#L", 1)[1]
            row["source_pointer"] = f"{stable_path}#L{line_suffix}"
            row.pop("source_row_sha256", None)
            row["source_row_sha256"] = v3._sha256_json(row)
        coverage = {**coverage, "source_path": stable_path}
    try:
        after = resolved.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot recheck Quran text source {resolved}: {exc}") from exc
    before_hash = _sha256(before)
    after_hash = _sha256(after)
    if not (
        before_hash == after_hash == coverage.get("source_sha256")
    ):
        raise WorkflowError(
            "Quran text source changed during packet projection; rerun prepare"
        )
    return evidence, coverage


def _verified_quran_text_projection(
    record: Any,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    if not isinstance(record, dict):
        raise WorkflowError("Manifest Quran text record is missing or malformed")
    source_value = record.get("source_path")
    if not isinstance(source_value, str) or not source_value:
        raise WorkflowError("Manifest Quran text record has no source path")
    source_path = _resolve_manifest_source_path(source_value, label="Quran text")
    evidence, current = _quran_text_projection(source_path)
    for field in ("source_id", "source_path", "source_sha256", "ayah_count"):
        if record.get(field) != current.get(field):
            raise WorkflowError(f"Manifest Quran text field is stale: {field}")
    return evidence, current


def _manifest_source_path(path: Path) -> str:
    resolved = path.resolve(strict=False)
    try:
        return str(resolved.relative_to(PROJECTS_ROOT.resolve(strict=False)))
    except ValueError:
        return str(resolved)


def _resolve_manifest_source_path(value: Any, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise WorkflowError(f"Manifest {label} source path is missing or malformed")
    path = Path(value)
    if not path.is_absolute():
        path = PROJECTS_ROOT / path
    return path.resolve(strict=False)


def _inter_ayah_input_record(
    projection_dir: Path, parent_dir: Path
) -> dict[str, str]:
    return {
        "projection_dir": _manifest_source_path(projection_dir),
        "parent_dir": _manifest_source_path(parent_dir),
    }


def _verified_inter_ayah_projection(
    coverage_record: Any,
    input_record: Any,
    *,
    focus_ref: str,
    numbered_refs: set[str],
    prefatory_focus: bool,
) -> None:
    if prefatory_focus:
        expected = {
            "status": "not_applicable",
            "reason": "inter-ayah evidence is defined on numbered focus ayahs only",
            "focus_ref": focus_ref,
        }
        if coverage_record != expected or input_record is not None:
            raise WorkflowError("Manifest inter-ayah not-applicable record is stale")
        return
    if not isinstance(coverage_record, dict):
        raise WorkflowError("Manifest inter-ayah coverage is missing or malformed")
    if not isinstance(input_record, dict) or set(input_record) != {
        "projection_dir",
        "parent_dir",
    }:
        raise WorkflowError("Manifest inter-ayah input record is missing or malformed")
    projection_dir = _resolve_manifest_source_path(
        input_record["projection_dir"], label="inter-ayah projection"
    )
    parent_dir = _resolve_manifest_source_path(
        input_record["parent_dir"], label="inter-ayah parent"
    )
    try:
        _rows, _reciprocal, current = v3._inter_ayah_evidence_with_fallback(
            focus_ref,
            projection_dir,
            parent_dir,
            numbered_refs,
        )
    except SystemExit as exc:
        raise WorkflowError(f"Cannot revalidate inter-ayah evidence: {exc}") from exc
    if coverage_record != current:
        raise WorkflowError("Manifest inter-ayah evidence or provenance is stale")


def _absolute(path: Path) -> Path:
    return Path(os.path.abspath(path))


def _assert_confined(path: Path, root: Path, *, label: str) -> None:
    absolute_path = _absolute(path)
    absolute_root = _absolute(root)
    try:
        relative = absolute_path.relative_to(absolute_root)
        absolute_root.relative_to(V4_ROOT)
    except ValueError as exc:
        raise WorkflowError(f"{label} escapes its v4 artifact root: {path}") from exc

    candidate = absolute_root
    for part in ("", *relative.parts):
        if part:
            candidate /= part
        if candidate.is_symlink():
            raise WorkflowError(f"{label} crosses a symlink: {candidate}")

    try:
        absolute_path.resolve(strict=False).relative_to(
            absolute_root.resolve(strict=False)
        )
    except ValueError as exc:
        raise WorkflowError(f"{label} resolves outside its v4 artifact root") from exc


def _assert_layout(layout: Layout) -> None:
    if layout != layout_for(layout.ayah_ref, layout.analysis_id):
        raise WorkflowError("Unit layout does not match the fixed v4 paths")
    for label, path, root in (
        ("input directory", layout.input, INPUT_ROOT),
        ("raw directory", layout.raw, RAW_ROOT),
        ("editorial directory", layout.editorial, EDITORIAL_ROOT),
    ):
        _assert_confined(path, root, label=label)


def _handoff_output_path(path: Path, root: Path, *, label: str) -> str:
    _assert_confined(path, root, label=label)
    if path.exists() and not path.is_file():
        raise WorkflowError(
            f"{label} exists but is not a regular file; clear or relocate it: {path}"
        )
    return str(_absolute(path))


def _repo_path(path: Path) -> str:
    try:
        return str(path.resolve(strict=False).relative_to(REPO_ROOT))
    except ValueError as exc:
        raise WorkflowError(f"Artifact path escapes the repository: {path}") from exc


def _path_record(path: Path) -> dict[str, Any]:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read generated artifact {path}: {exc}") from exc
    return {
        "path": _repo_path(path),
        "bytes": len(payload),
        "sha256": _sha256(payload),
    }


def _atomic_write(path: Path, payload: bytes, *, root: Path | None = None) -> None:
    if root is not None:
        _assert_confined(path, root, label="generated artifact")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise WorkflowError(f"Refusing to replace symlink: {path}")
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


def _write_generated(
    path: Path,
    payload: bytes,
    *,
    replace_changed: bool = False,
    root: Path | None = None,
) -> None:
    if path.exists():
        if not path.is_file() or path.is_symlink():
            raise WorkflowError(f"Generated artifact is not a regular file: {path}")
        if path.read_bytes() == payload:
            return
        if not replace_changed:
            raise WorkflowError(
                f"Generated input changed: {path}. Commit or inspect the current "
                "state, then rerun prepare with --force-input."
            )
    _atomic_write(path, payload, root=root)


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


def _analysis_id(args: argparse.Namespace) -> str:
    value = getattr(args, "analysis_id", None) or "native"
    if compositions.ANALYSIS_ID_RE.fullmatch(value) is None:
        raise WorkflowError(f"Invalid analysis ID: {value!r}")
    return value


def _layout_for_args(args: argparse.Namespace) -> Layout:
    return layout_for(args.ayah, _analysis_id(args))


def _is_prefatory_ref(ref: str) -> bool:
    return bool(re.fullmatch(r"[1-9][0-9]*:0", ref))


def _numbered_surah_refs(
    quran_evidence: dict[str, dict[str, Any]], surah: int
) -> tuple[str, ...]:
    prefix = f"{surah}:"
    numbers = sorted(
        int(ref.split(":", 1)[1])
        for ref in quran_evidence
        if ref.startswith(prefix) and ref.split(":", 1)[1] != "0"
    )
    expected_count = QURAN_AYAH_COUNTS[surah - 1]
    expected = list(range(1, expected_count + 1))
    if numbers != expected:
        missing = sorted(set(expected) - set(numbers))
        extra = sorted(set(numbers) - set(expected))
        raise WorkflowError(
            f"Quran text lacks the complete canonical numbered ayat for surah "
            f"{surah}; missing={missing}, extra={extra}"
        )
    return tuple(f"{surah}:{ayah}" for ayah in expected)


def _automatic_basmala_composition(
    focus_ref: str, quran_evidence: dict[str, dict[str, Any]]
) -> compositions.Composition:
    if not _is_prefatory_ref(focus_ref):
        raise WorkflowError("Automatic basmala composition requires an S:0 focus")
    surah = int(focus_ref.split(":", 1)[0])
    if focus_ref not in quran_evidence:
        raise WorkflowError(f"Quran text is missing prefatory focus {focus_ref}")
    numbered_refs = _numbered_surah_refs(quran_evidence, surah)
    return compositions.composition_from_cli(
        f"s{surah:03d}-basmala-full",
        [f"host={focus_ref},{surah}:1-{len(numbered_refs)}"],
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
        if focus_ref not in quran_evidence:
            raise WorkflowError(f"Quran text is missing prefatory focus {focus_ref}")
        required = (focus_ref, *_numbered_surah_refs(quran_evidence, surah))
        focus_segment = composition.segment_for(focus_ref)
        actual = tuple(
            ref for ref in focus_segment.refs if ref.startswith(f"{surah}:")
        )
        if actual != required:
            missing = [ref for ref in required if ref not in actual]
            extra = [ref for ref in actual if ref not in required]
            raise WorkflowError(
                f"Prefatory focus {focus_ref} requires the complete numbered host "
                "surah in canonical order in its own segment; "
                f"missing={missing}, extra={extra}"
            )


def _composition_for_prepare(
    args: argparse.Namespace, layout: Layout
) -> compositions.Composition | None:
    if layout.analysis_id == "native":
        if _is_prefatory_ref(layout.ayah_ref):
            raise WorkflowError(
                f"Prefatory focus {layout.ayah_ref} cannot use a basmala-only native "
                "analysis; invoke the CLI without --analysis-id to derive its full "
                "host-surah composition"
            )
        return None
    supplied = getattr(args, "composition", None)
    if isinstance(supplied, compositions.Composition):
        composition = supplied
    elif layout.composition.is_file() and not layout.composition.is_symlink():
        try:
            composition = compositions.load_composition(layout.composition)
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
    else:
        raise WorkflowError(
            f"Analysis {layout.analysis_id!r} has no composition definition. "
            "Supply --segment definitions (or --analysis) on the first prepare."
        )
    if composition.analysis_id != layout.analysis_id:
        raise WorkflowError("Composition analysis ID does not match the unit path")
    if layout.ayah_ref not in composition.focus_refs:
        raise WorkflowError(
            f"{layout.ayah_ref} is not a focus of analysis {layout.analysis_id}"
        )
    return composition


def _docket_payload_hash(docket: dict[str, Any]) -> str:
    payload = copy.deepcopy(docket)
    payload.get("identity", {}).pop("docket_payload_sha256", None)
    return v3._sha256_json(payload)


def _adapt_basmala_docket(
    source_bundle: dict[str, Any], template_docket: dict[str, Any]
) -> dict[str, Any]:
    target_ref = str(source_bundle.get("ayahRef"))
    try:
        unit_identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=target_ref
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if unit_identity["unit_kind"] != "prefatory_basmala":
        raise WorkflowError("Basmala docket adapter requires prefatory_basmala")
    if template_docket.get("identity", {}).get("ayah_ref") != "1:1":
        raise WorkflowError("Basmala linguistic docket template must be 1:1")

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
        candidate["ayah_ref"] = target_ref
        candidate["surface_ref"] = target_ref
        candidate["linguistic_source_ref"] = "1:1"
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
    docket["focus"]["arabic_uthmani"] = source_bundle["text"]["arabic_uthmani"]
    docket["focus"]["surface_ref"] = target_ref
    docket["focus"]["linguistic_source_ref"] = "1:1"
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
    coverage_by_source: dict[str, int] = {}
    for candidate in candidates:
        source_type = str(candidate.get("source_type"))
        coverage_by_source[source_type] = coverage_by_source.get(source_type, 0) + 1
    docket["coverage"] = {
        **docket.get("coverage", {}),
        "docket_candidate_count": len(candidates),
        "mandatory_candidate_count": sum(
            candidate.get("mandatory") is True for candidate in candidates
        ),
        "optional_candidate_count": sum(
            candidate.get("mandatory") is not True for candidate in candidates
        ),
        "by_source_type": coverage_by_source,
    }
    docket["identity"]["docket_payload_sha256"] = _docket_payload_hash(docket)
    return docket


def _derive_docket(
    source_origin: Path,
    source_payload: bytes,
    source_bundle: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        _prepared, docket = build_prepared_artifacts(
            source_bundle,
            source_path=source_origin,
            source_raw=source_payload,
            options=V4_PREPARE_OPTIONS,
        )
    except ValidationError as exc:
        raise WorkflowError(
            f"Cannot derive the V4 docket from {source_origin}: {exc}"
        ) from exc
    return docket, {
        "kind": "derived_in_memory",
        "implementation": "_commentary/v3/v3lib/prepare.py",
        "source": v3._stable_source_path(source_origin),
        "prepare_options": asdict(V4_PREPARE_OPTIONS),
    }


def _basmala_docket_template(source_bundle: dict[str, Any]) -> dict[str, Any]:
    """Expose an S:0 bundle through V3's positive-ayah preparation contract."""
    template = copy.deepcopy(source_bundle)
    template.update({
        "unit_kind": "numbered_ayah",
        "surah": 1,
        "ayah": 1,
        "ayahRef": "1:1",
        "surface_ref": "1:1",
        "linguistic_source_ref": "1:1",
        "v12_reader_responses": {},
        "v12_focus_trace_hermetic": {},
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


def _focus_bundle_origin(
    args: argparse.Namespace,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> Path:
    explicit = getattr(args, "source_bundle", None)
    if explicit is not None:
        return Path(explicit)

    if _is_prefatory_ref(args.ayah):
        return compositions.unit_bundle_path(member_bundles_dir, args.ayah)
    return compositions.unit_bundle_path(context_bundles_dir, args.ayah)


def _load_focus_inputs(
    args: argparse.Namespace,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> tuple[
    Path,
    bytes,
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
]:
    source_origin = _focus_bundle_origin(
        args, context_bundles_dir, member_bundles_dir
    )
    source_payload, source_bundle = _load_json_with_bytes(source_origin)
    try:
        unit_identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=args.ayah
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc

    explicit_docket = getattr(args, "docket", None)
    if explicit_docket is not None:
        docket_origin = Path(explicit_docket)
        _docket_payload, docket = _load_json_with_bytes(docket_origin)
        try:
            validate_docket(docket)
        except ValidationError as exc:
            raise WorkflowError(f"Invalid docket {docket_origin}: {exc}") from exc
        docket_lineage = {
            "kind": "provided",
            "path": v3._stable_source_path(docket_origin),
        }
    else:
        template_origin = source_origin
        template_payload = source_payload
        template_bundle = source_bundle
        if unit_identity["unit_kind"] == "prefatory_basmala":
            template_bundle = _basmala_docket_template(source_bundle)
            template_payload = _canonical_json_bytes(template_bundle)
        docket, docket_lineage = _derive_docket(
            template_origin,
            template_payload,
            template_bundle,
        )

    if unit_identity["unit_kind"] == "prefatory_basmala":
        docket = _adapt_basmala_docket(source_bundle, docket)
        docket_lineage = {
            **docket_lineage,
            "adapter": "prefatory_basmala_linguistic_alias_v1",
            "template_identity_adapter": "s0_bundle_as_positive_1_1_v1",
            "surface_ref": args.ayah,
            "linguistic_source_ref": "1:1",
        }
    return (
        source_origin,
        source_payload,
        source_bundle,
        docket,
        docket_lineage,
    )


def _merge_context_supports(
    existing: list[dict[str, Any]], additions: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    by_id = {
        support.get("support_id"): support
        for support in existing
        if isinstance(support, dict) and isinstance(support.get("support_id"), str)
    }
    for addition in additions:
        support_id = addition["support_id"]
        current = by_id.get(support_id)
        if current is None:
            existing.append(addition)
            by_id[support_id] = addition
            continue
        for field in ("source_type", "role", "payload"):
            if current.get(field) != addition.get(field):
                raise WorkflowError(f"Context support ID collision: {support_id}")
        current["context_refs"] = sorted(set(
            current.get("context_refs", []) + addition.get("context_refs", [])
        ))
    return existing


def _composition_projection(
    composition: compositions.Composition,
    focus_ref: str,
    focus_bundle: dict[str, Any],
    package_bundle_root: Path,
    member_bundle_root: Path,
) -> dict[str, Any]:
    by_lane: dict[str, dict[str, list[dict[str, Any]]]] = {
        lane: {"candidates": [], "supports": [], "units": []}
        for lane in LANES
    }
    all_units: list[dict[str, Any]] = []
    loaded: dict[str, tuple[Path, dict[str, Any], dict[str, Any]]] = {}
    for context_row in composition.context_rows(focus_ref):
        try:
            context_ref = context_row["ref"]
            if context_ref not in loaded:
                if context_row.get("membership_added_ayah") is True:
                    loaded[context_ref] = _load_added_ayah_bundle(
                        package_bundle_root,
                        member_bundle_root,
                        context_ref,
                    )
                elif _is_prefatory_ref(context_ref):
                    loaded[context_ref] = compositions.load_unit_bundle(
                        member_bundle_root, context_ref
                    )
                else:
                    loaded[context_ref] = compositions.load_unit_bundle(
                        package_bundle_root, context_ref
                    )
            path, bundle, identity = loaded[context_ref]
            candidate, supports, inventory = compositions.project_context_unit(
                composition=composition,
                focus_ref=focus_ref,
                context_row=context_row,
                source_path=path,
                bundle=bundle,
                focus_bundle=focus_bundle,
                identity=identity,
                projects_root=PROJECTS_ROOT,
            )
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        lane_projection = by_lane[context_row["lane"]]
        lane_projection["candidates"].append(candidate)
        _merge_context_supports(lane_projection["supports"], supports)
        lane_projection["units"].append(inventory)
        all_units.append(inventory)
    return {"by_lane": by_lane, "units": all_units}


def _bundle_path_is_present(bundle_root: Path, ref: str) -> bool:
    path = compositions.unit_bundle_path(bundle_root, ref)
    return path.exists() or path.is_symlink()


def _load_added_ayah_bundle(
    package_bundle_root: Path,
    member_bundle_root: Path,
    ref: str,
) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    try:
        package_present = _bundle_path_is_present(package_bundle_root, ref)
        same_root = (
            package_bundle_root.resolve(strict=False)
            == member_bundle_root.resolve(strict=False)
        )
        member_present = (
            package_present
            if same_root
            else _bundle_path_is_present(member_bundle_root, ref)
        )
        if not package_present and not member_present:
            raise WorkflowError(
                f"Added ayah {ref} is unavailable in both the package and member roots"
            )
        package_loaded = (
            compositions.load_unit_bundle(package_bundle_root, ref)
            if package_present
            else None
        )
        member_loaded = (
            package_loaded
            if same_root
            else (
                compositions.load_unit_bundle(member_bundle_root, ref)
                if member_present
                else None
            )
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if package_loaded is not None and member_loaded is not None:
        if (
            package_loaded[2]["canonical_sha256"]
            != member_loaded[2]["canonical_sha256"]
        ):
            raise WorkflowError(
                f"Added ayah {ref} differs between package and member roots"
            )
        return package_loaded
    if package_loaded is not None:
        return package_loaded
    if member_loaded is not None:
        return member_loaded
    raise WorkflowError(f"Added ayah {ref} could not be loaded")


def _load_prefatory_basmala_context(
    source_bundle: dict[str, Any],
    member_bundles_dir: Path,
    composition: compositions.Composition | None,
) -> tuple[Path, bytes, dict[str, Any], dict[str, Any]] | None:
    if source_bundle.get("unit_kind", "numbered_ayah") != "numbered_ayah":
        return None
    source_surah = source_bundle.get("surah")
    ayah = source_bundle.get("ayah")
    if not isinstance(source_surah, int) or not isinstance(ayah, int) or ayah <= 0:
        return None
    surah = composition.member_surah if composition is not None else None
    if surah is None:
        surah = source_surah
    if source_surah != surah:
        raise WorkflowError(
            f"Focus {source_bundle.get('ayahRef')} does not belong to host surah {surah}"
        )
    if surah in compositions.BASMALA_EXCLUDED_SURAHS:
        return None
    ref = f"{surah}:0"
    try:
        path = compositions.unit_bundle_path(member_bundles_dir, ref)
        payload, bundle = _load_json_with_bytes(path)
        identity = compositions.validate_unit_bundle(bundle, expected_ref=ref)
    except (WorkflowError, compositions.CompositionError) as exc:
        raise WorkflowError(
            f"Prefatory basmala bundle is required for numbered unit "
            f"{source_bundle.get('ayahRef')} but could not be loaded from "
            f"{member_bundles_dir}: {exc}"
        ) from exc
    identity["canonical_sha256"] = v3._sha256_json(bundle)
    identity["bytes"] = len(payload)
    return path, payload, bundle, identity


def _append_basmala_focus_evidence(
    packet: dict[str, Any], source_bundle: dict[str, Any], lane: str
) -> None:
    if lane != "global":
        return
    payload = {
        field: source_bundle.get(field)
        for field in (
            "v12_reader_responses",
            "v12_reader_walks",
            "v12_reader_walks_wide",
            "v12_cross_run_publication",
            "butuncul_okuma_line",
            "channel_subchannels_anchored_here",
            "channel_generated_outputs",
        )
        if source_bundle.get(field) not in (None, {}, [], "")
    }
    payload["not_applicable_states"] = {
        "hft": source_bundle.get("coverage", {}).get("v12_focus_trace_hermetic"),
        "inter_ayah": source_bundle.get("coverage", {}).get("inter_ayah"),
        "pericope": source_bundle.get("coverage", {}).get("pericope"),
    }
    support_id = "sup_basmala_" + v3._sha256_json(payload)[:20]
    candidate_id = "cand_basmala_" + v3._sha256_json({
        "focus_ref": source_bundle["ayahRef"],
        "support_id": support_id,
    })[:20]
    packet["support_registry"].append({
        "support_id": support_id,
        "source_type": "prefatory_basmala_focus_evidence",
        "source_local_id": source_bundle["ayahRef"],
        "scope": "global",
        "json_pointer": "/prefatory_basmala_focus_evidence",
        "role": "surah_conditioned_prefatory_evidence",
        "branch_refs": [],
        "payload": payload,
        "trust": "canonical_bundle_hash_bound",
        "qualification": {
            "surface_ref": source_bundle["surface_ref"],
            "linguistic_source_ref": source_bundle["linguistic_source_ref"],
            "hft_and_inter_ayah_are_not_applicable": True,
        },
    })
    packet["candidate_inventory"].append({
        "candidate_id": candidate_id,
        "ayah_ref": source_bundle["ayahRef"],
        "lane": "global",
        "source_type": "prefatory_basmala_focus_evidence",
        "source_local_id": source_bundle["ayahRef"],
        "source_pointer": "/prefatory_basmala_focus_evidence",
        "kind": "surah_conditioned_prefatory_evidence",
        "title": "Prefatory basmala evidence in its target surah",
        "scope": "wider_record",
        "anchor_refs": [source_bundle["ayahRef"]],
        "branch_refs": [],
        "support_ids": [support_id],
        "trust": "canonical_bundle_hash_bound",
        "commentary_obligation": "review",
    })


def _append_numbered_ayah_basmala_context(
    packet: dict[str, Any],
    *,
    focus_ref: str,
    basmala_path: Path,
    basmala_bundle: dict[str, Any],
    focus_bundle: dict[str, Any],
    basmala_identity: dict[str, Any],
    lane: str,
) -> dict[str, Any]:
    surah = focus_ref.split(":", 1)[0]
    basmala_ref = basmala_identity["ayah_ref"]
    existing_units = packet.setdefault("selected_context_units", [])
    if not isinstance(existing_units, list):
        raise WorkflowError(f"{lane} packet selected_context_units must be a list")
    source_file = None
    for existing in existing_units:
        if isinstance(existing, dict) and existing.get("ayah_ref") == basmala_ref:
            expected_identity = {
                "canonical_sha256": basmala_identity["canonical_sha256"],
                "surface_ref": basmala_identity["surface_ref"],
                "linguistic_source_ref": basmala_identity["linguistic_source_ref"],
            }
            mismatched = {
                field: (existing.get(field), expected)
                for field, expected in expected_identity.items()
                if existing.get(field) != expected
            }
            if mismatched:
                raise WorkflowError(
                    f"Explicit basmala context {basmala_ref} conflicts with the "
                    f"mandatory host-surah bundle: {mismatched}"
                )
            existing["automatic_prefatory_basmala_membership"] = True
            source_file = existing.get("source_file")
            packet["scope"]["prefatory_basmala"] = {
                "status": "included_as_surah_preface_context",
                "ayah_ref": basmala_identity["ayah_ref"],
                "surface_ref": basmala_identity["surface_ref"],
                "linguistic_source_ref": basmala_identity["linguistic_source_ref"],
                "source_bundle_canonical_sha256": basmala_identity["canonical_sha256"],
                "source_file": source_file or v3._stable_source_path(basmala_path),
                "via": "explicit_composition_context",
            }
            return existing
    automatic_composition = compositions.Composition(
        analysis_id=f"native-prefatory-basmala-s{int(surah):03d}",
        segments=(
            compositions.Segment(
                segment_id="surah-with-prefatory-basmala",
                refs=(basmala_ref, focus_ref),
            ),
        ),
        focus_refs=(focus_ref,),
        description=(
            "Automatic target-surah prefatory basmala membership for native "
            "numbered-ayah packets."
        ),
    )
    candidate, supports, inventory = compositions.project_context_unit(
        composition=automatic_composition,
        focus_ref=focus_ref,
        context_row={
            "ref": basmala_ref,
            "segment_id": "surah-with-prefatory-basmala",
            "segment_index": 0,
            "unit_index": 0,
            "composition_order": 0,
            "source_pointer": "/scope/prefatory_basmala",
            "lane": lane,
        },
        source_path=basmala_path,
        bundle=basmala_bundle,
        focus_bundle=focus_bundle,
        identity=basmala_identity,
        projects_root=PROJECTS_ROOT,
    )
    candidate.update({
        "source_type": "automatic_prefatory_basmala_surah_member",
        "source_pointer": "/scope/prefatory_basmala",
        "kind": "surah_prefatory_basmala",
        "title": "Prefatory basmala as surah member",
        "scope": "surah_preface",
        "commentary_obligation": "review",
    })
    for support in supports:
        qualification = support.setdefault("qualification", {})
        qualification.update({
            "context_unit_is_the_surah_preface": True,
            "numbered_ayah_focus_is_unchanged": True,
            "automatic_prefatory_basmala_membership": True,
        })
    inventory["automatic_prefatory_basmala_membership"] = True
    packet["candidate_inventory"].append(candidate)
    _merge_context_supports(packet["support_registry"], supports)
    existing_units.append(inventory)
    packet["scope"]["prefatory_basmala"] = {
        "status": "included_as_surah_preface_context",
        "ayah_ref": basmala_identity["ayah_ref"],
        "surface_ref": basmala_identity["surface_ref"],
        "linguistic_source_ref": basmala_identity["linguistic_source_ref"],
        "source_bundle_canonical_sha256": basmala_identity["canonical_sha256"],
        "source_file": inventory["source_file"],
        "via": "automatic_surah_membership",
    }
    return inventory


def _augment_lane_packet(
    packet: dict[str, Any],
    *,
    layout: Layout,
    composition: compositions.Composition | None,
    projection: dict[str, Any] | None,
    source_bundle: dict[str, Any],
    prefatory_basmala_context: tuple[Path, dict[str, Any], dict[str, Any]] | None,
    lane: str,
) -> dict[str, Any]:
    if source_bundle.get("unit_kind") == "prefatory_basmala":
        _append_basmala_focus_evidence(packet, source_bundle, lane)
        packet["identity"].update({
            "unit_kind": "prefatory_basmala",
            "surface_ref": source_bundle["surface_ref"],
            "linguistic_source_ref": source_bundle["linguistic_source_ref"],
        })
        packet["scope"]["prefatory_basmala"] = {
            "hft": "not_applicable",
            "inter_ayah": "not_applicable",
            "native_pericope": "not_applicable",
        }
    if composition is not None and projection is not None:
        lane_projection = projection["by_lane"][lane]
        packet["candidate_inventory"].extend(lane_projection["candidates"])
        _merge_context_supports(
            packet["support_registry"], lane_projection["supports"]
        )
        packet["selected_context_units"] = lane_projection["units"]
        packet["scope"]["analysis_composition"] = {
            **composition.canonical_payload,
            "canonical_sha256": composition.canonical_sha256,
            "current_focus_ref": layout.ayah_ref,
            "context_refs": list(composition.context_refs(layout.ayah_ref)),
            "lane_context_refs": [
                unit["ayah_ref"] for unit in lane_projection["units"]
            ],
        }
        packet["identity"].update({
            "analysis_id": composition.analysis_id,
            "analysis_composition_sha256": composition.canonical_sha256,
        })
        added_units = [
            unit
            for unit in lane_projection["units"]
            if unit.get("membership_added_ayah") is True
        ]
        if composition.member_surah is not None:
            packet["scope"]["surah_membership"] = {
                "mode": "host_surah_with_external_ayat",
                "analysis_id": composition.analysis_id,
                "current_focus_ref": layout.ayah_ref,
                "target_surah": composition.member_surah,
                "added_ayat_refs": list(composition.added_ayat_refs),
                "lane_context_refs": [
                    unit["ayah_ref"] for unit in added_units
                ],
            }
    if prefatory_basmala_context is not None:
        basmala_path, basmala_bundle, basmala_identity = prefatory_basmala_context
        basmala_ref = basmala_identity["ayah_ref"]
        explicit_here = any(
            isinstance(unit, dict) and unit.get("ayah_ref") == basmala_ref
            for unit in packet.get("selected_context_units", [])
        )
        composition_has_basmala = (
            composition is not None
            and basmala_ref in composition.context_refs(layout.ayah_ref)
        )
        if explicit_here or (not composition_has_basmala and lane == "macro"):
            _append_numbered_ayah_basmala_context(
                packet,
                focus_ref=layout.ayah_ref,
                basmala_path=basmala_path,
                basmala_bundle=basmala_bundle,
                focus_bundle=source_bundle,
                basmala_identity=basmala_identity,
                lane=lane,
            )
    candidate_ids = [
        candidate.get("candidate_id") for candidate in packet["candidate_inventory"]
    ]
    support_ids = [support.get("support_id") for support in packet["support_registry"]]
    if len(candidate_ids) != len(set(candidate_ids)):
        raise WorkflowError(f"{lane} packet contains duplicate candidate IDs")
    if len(support_ids) != len(set(support_ids)):
        raise WorkflowError(f"{lane} packet contains duplicate support IDs")
    packet["identity"]["lane_packet_sha256"] = (
        v3._payload_hash_with_identity_field_removed(packet, "lane_packet_sha256")
    )
    packet_bytes = len(_canonical_json_bytes(packet))
    if packet_bytes > MAX_LANE_PACKET_BYTES:
        raise WorkflowError(
            f"{lane} packet is {packet_bytes} bytes; context budget is "
            f"{MAX_LANE_PACKET_BYTES}. Reduce the composition explicitly."
        )
    return packet


def _source_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--docket",
        type=Path,
        help="Optional legacy docket override for one unit; normally derived in memory.",
    )
    parser.add_argument(
        "--source-bundle",
        type=Path,
        help="Optional focus-bundle override for one unit.",
    )
    parser.add_argument(
        "--inter-ayah-dir", type=Path, default=v3.DEFAULT_INTER_AYAH_DIR
    )
    parser.add_argument(
        "--inter-ayah-parent-dir",
        type=Path,
        default=v3.DEFAULT_INTER_AYAH_PARENT_DIR,
    )
    parser.add_argument("--quran-text", type=Path, default=v3.DEFAULT_QURAN_TEXT)
    parser.add_argument(
        "--context-bundles-dir",
        type=Path,
        default=DEFAULT_CONTEXT_BUNDLES_DIR,
        help=(
            "Root containing canonical sNNN/S_A.ayah.json files used "
            "for focus and selected-context package units."
        ),
    )
    parser.add_argument(
        "--member-bundles-dir",
        type=Path,
        default=DEFAULT_CONTEXT_BUNDLES_DIR,
        help=(
            "Root containing mandatory host basmala and explicitly added "
            "out-of-package ayat."
        ),
    )
    parser.add_argument(
        "--force-input",
        action="store_true",
        help="Replace changed generated input files; raw/editorial files are untouched.",
    )


def _context_package_record(
    context_bundles_dir: Path,
    composition: compositions.Composition | None,
    focus_ref: str,
) -> dict[str, Any] | None:
    manifest_path = context_bundles_dir / "pericope.bundle-manifest.json"
    direct_bundles = list(context_bundles_dir.glob("*.ayah.json"))
    if not manifest_path.exists() and not manifest_path.is_symlink():
        if direct_bundles:
            raise WorkflowError(
                "A flat context bundle root must carry "
                f"pericope.bundle-manifest.json: {context_bundles_dir}"
            )
        return None
    try:
        manifest = pericope_manifests.validate_manifest(
            manifest_path,
            repo_root=REPO_ROOT,
            expected_builder=SCRIPTS_ROOT / "build_pericope_bundles.py",
            expected_lower_level_builder=SCRIPTS_ROOT / "build_bundle.py",
        )
    except pericope_manifests.PericopeManifestError as exc:
        raise WorkflowError(str(exc)) from exc

    required_refs: set[str] = set()
    if not _is_prefatory_ref(focus_ref):
        required_refs.add(focus_ref)
    if composition is not None:
        for row in composition.context_rows(focus_ref):
            if (
                row.get("membership_added_ayah") is not True
                and not _is_prefatory_ref(row["ref"])
            ):
                required_refs.add(row["ref"])
    missing = sorted(required_refs - set(manifest["ayah_refs"]))
    if missing:
        raise WorkflowError(
            f"Pericope package does not bind required package ayat: {missing}"
        )
    return {
        "manifest": _path_record(manifest_path),
        "schema_version": manifest["schema_version"],
        "canonical_sha256": v3._sha256_json(manifest),
        "surah": manifest["surah"],
        "pericope": manifest["pericope"],
        "ayah_refs": manifest["ayah_refs"],
    }


def _dedupe_context_units(units: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduped: list[dict[str, Any]] = []
    by_ref: dict[str, dict[str, Any]] = {}
    for unit in units:
        if not isinstance(unit, dict):
            continue
        ayah_ref = unit.get("ayah_ref")
        canonical_sha256 = unit.get("canonical_sha256")
        if not isinstance(ayah_ref, str) or not isinstance(canonical_sha256, str):
            raise WorkflowError("Context-unit lineage lacks ayah/hash identity")
        normalized = copy.deepcopy(unit)
        lane = normalized.pop("lane", None)
        lanes = normalized.pop("lanes", [])
        normalized.pop("candidate_id", None)
        normalized.pop("support_ids", None)
        binding = {
            field: normalized.pop(field)
            for field in ("segment_id", "composition_order", "unit_index")
            if field in normalized
        }
        if isinstance(lane, str):
            lanes = [*lanes, lane] if isinstance(lanes, list) else [lane]
            if binding:
                normalized["lane_bindings"] = {lane: binding}
        elif binding:
            raise WorkflowError(
                f"Context-unit lineage for {ayah_ref} has an unscoped lane binding"
            )
        if not isinstance(lanes, list) or not all(
            isinstance(item, str) for item in lanes
        ):
            raise WorkflowError(f"Context-unit lanes are malformed for {ayah_ref}")
        normalized["lanes"] = list(dict.fromkeys(lanes))
        existing = by_ref.get(ayah_ref)
        if existing is None:
            by_ref[ayah_ref] = normalized
            deduped.append(normalized)
            continue
        for field in (
            "canonical_sha256",
            "unit_kind",
            "surface_ref",
            "linguistic_source_ref",
            "context_projection_protocol",
            "context_projection_sha256",
            "context_projection_bytes",
        ):
            if existing.get(field) != normalized.get(field):
                raise WorkflowError(
                    f"Conflicting context-unit lineage for {ayah_ref}: {field}"
                )
        if existing.get("source_file") != normalized.get("source_file"):
            raise WorkflowError(
                f"Conflicting context source paths for {ayah_ref}"
            )
        existing["lanes"] = list(dict.fromkeys(
            [*existing.get("lanes", []), *normalized.get("lanes", [])]
        ))
        existing_bindings = existing.setdefault("lane_bindings", {})
        for bound_lane, lane_binding in normalized.get("lane_bindings", {}).items():
            if (
                bound_lane in existing_bindings
                and existing_bindings[bound_lane] != lane_binding
            ):
                raise WorkflowError(
                    f"Conflicting lane binding for {ayah_ref} in {bound_lane}"
                )
            existing_bindings[bound_lane] = lane_binding
        for field, value in normalized.items():
            if field in {"lanes", "lane_bindings"}:
                continue
            if field not in existing:
                existing[field] = value
            elif existing[field] != value:
                raise WorkflowError(
                    f"Conflicting context-unit metadata for {ayah_ref}: {field}"
                )
    return deduped


def _expected_context_lanes(
    composition: compositions.Composition | None,
    focus_ref: str,
    prefatory_ref: str | None,
) -> dict[str, list[str]]:
    expected: dict[str, list[str]] = {}
    if composition is not None:
        for row in composition.context_rows(focus_ref):
            lanes = expected.setdefault(row["ref"], [])
            if row["lane"] in lanes:
                raise WorkflowError(
                    f"Composition routes {row['ref']} to {row['lane']} more than once"
                )
            lanes.append(row["lane"])
    if prefatory_ref is not None:
        expected.setdefault(prefatory_ref, ["macro"])
    return expected


def _expected_lane_context_refs(
    composition: compositions.Composition | None,
    focus_ref: str,
    prefatory_ref: str | None,
    lane: str,
) -> list[str]:
    refs = []
    if composition is not None:
        refs.extend(
            row["ref"]
            for row in composition.context_rows(focus_ref)
            if row["lane"] == lane
        )
    if prefatory_ref is not None and prefatory_ref not in refs:
        composition_refs = (
            set(composition.context_refs(focus_ref))
            if composition is not None
            else set()
        )
        if prefatory_ref not in composition_refs and lane == "macro":
            refs.append(prefatory_ref)
    return refs


def _build_scope_prompt(
    layout: Layout,
    lane: str,
    packet: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    if lane not in LANES:
        raise WorkflowError(f"Unknown scope lane: {lane}")
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "scope.md"
    template = template_path.read_text(encoding="utf-8")
    template_sha256 = _sha256(template.encode("utf-8"))
    governing_hashes = {
        f"{key}_sha256": _sha256(value.encode("utf-8"))
        for key, value in governing.items()
    }
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
        "template_sha256": template_sha256,
        **governing_hashes,
    }
    request_sha256 = v3._request_sha256(
        "v4-one-pass-scope-author", request_inputs
    )
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@LANE_PACKET_SHA256@@": packet["identity"][
                "lane_packet_sha256"
            ],
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@CONTRIBUTION_OUTPUT_PATH@@": _repo_path(
                layout.scope_contribution(lane)
            ),
            "@@SCOPE_CONTRIBUTION_SCHEMA_VERSION@@": (
                SCOPE_CONTRIBUTION_SCHEMA_VERSION
            ),
            "@@PRINCIPLES_MD@@": governing["principles"],
            "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
            "@@CHANNELS_MD@@": governing["channels"],
            "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
            "@@LANE_PACKET_JSON@@": v3._canonical_json(packet),
        },
        label=f"{lane} scope author",
    )
    return prompt, {
        "request_sha256": request_sha256,
        "request_inputs": request_inputs,
        "response_schema_version": SCOPE_CONTRIBUTION_SCHEMA_VERSION,
        "template_source": _repo_path(template_path),
        "template_sha256": template_sha256,
    }


def _input_manifest_base(
    layout: Layout,
    source_origin: Path,
    docket_lineage: dict[str, Any],
    source_bundle: dict[str, Any],
    prefatory_basmala_record: dict[str, Any] | None,
    docket: dict[str, Any],
    quran_coverage: dict[str, Any],
    inter_ayah_coverage: dict[str, Any],
    inter_ayah_inputs: dict[str, str] | None,
    lane_records: dict[str, Any],
    composition: compositions.Composition | None,
    composition_projection: dict[str, Any] | None,
    context_package_record: dict[str, Any] | None,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> dict[str, Any]:
    canonical_template = PROMPTS_ROOT / "canonical.md"
    editorial_instructions = V3_PROMPTS_ROOT / "editorial-followup.md"
    editorial_template = PROMPTS_ROOT / "editorial.md"
    prefatory_context_units = []
    if isinstance(prefatory_basmala_record, dict):
        units = prefatory_basmala_record.get("selected_context_units")
        if isinstance(units, list):
            prefatory_context_units = [
                unit for unit in units if isinstance(unit, dict)
            ]
    selected_context_units = _dedupe_context_units([
        *(
            composition_projection["units"]
            if composition_projection is not None
            else []
        ),
        *prefatory_context_units,
    ])
    return {
        "schema_version": UNIT_MANIFEST_SCHEMA_VERSION,
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "layout": {
            "input": _repo_path(layout.input),
            "raw": _repo_path(layout.raw),
            "editorial": _repo_path(layout.editorial),
        },
        "source": {
            "snapshot": _path_record(layout.source_bundle),
            "origin": _manifest_source_path(source_origin),
            "canonical_sha256": v3._sha256_json(source_bundle),
        },
        "prefatory_basmala": prefatory_basmala_record,
        "context_package": context_package_record,
        "docket": {
            "snapshot": _path_record(layout.docket),
            "origin": docket_lineage,
            "payload_sha256": docket["identity"]["docket_payload_sha256"],
        },
        "evidence_projection": {
            "quran_text": quran_coverage,
            "inter_ayah": inter_ayah_coverage,
            "inter_ayah_inputs": inter_ayah_inputs,
            "implementation": {
                "workflow": _path_record(Path(__file__)),
                "composition": _path_record(Path(compositions.__file__)),
                "v3_projection": _path_record(V3_ROOT / "render_authoring.py"),
            },
        },
        "analysis": (
            {
                "mode": "native",
                "analysis_id": "native",
                "composition": None,
                "context_bundles_dir": None,
                "member_bundles_dir": None,
                "selected_context_units": selected_context_units,
            }
            if composition is None
            else {
                "mode": "ordered_composition",
                "analysis_id": composition.analysis_id,
                "composition": _path_record(layout.composition),
                "composition_canonical_sha256": composition.canonical_sha256,
                "context_bundles_dir": _manifest_source_path(context_bundles_dir),
                "member_bundles_dir": _manifest_source_path(member_bundles_dir),
                "selected_context_units": selected_context_units,
                "surah_membership": (
                    None
                    if composition.member_surah is None
                    else {
                        "target_surah": composition.member_surah,
                        "added_ayat_refs": list(composition.added_ayat_refs),
                        "context_units": _dedupe_context_units(
                            [
                                unit
                                for unit in composition_projection["units"]
                                if unit.get("membership_added_ayah") is True
                            ]
                        ),
                    }
                ),
            }
        ),
        "lanes": lane_records,
        "canonical_template": {
            "path": _repo_path(canonical_template),
            "sha256": _sha256(canonical_template.read_bytes()),
        },
        "editorial": {
            "instructions_source": _repo_path(editorial_instructions),
            "instructions_sha256": _sha256(editorial_instructions.read_bytes()),
            "handoff_template_source": _repo_path(editorial_template),
            "handoff_template_sha256": _sha256(editorial_template.read_bytes()),
            "expected_outputs": {
                kind: _repo_path(layout.editorial_output(kind)) for kind in KINDS
            },
        },
        "canonical": None,
        "editorial_turn": None,
    }


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    layout = _layout_for_args(args)
    _assert_layout(layout)
    composition = _composition_for_prepare(args, layout)
    context_bundles_dir = Path(
        getattr(args, "context_bundles_dir", DEFAULT_CONTEXT_BUNDLES_DIR)
    ).resolve(strict=False)
    member_bundles_dir = Path(
        getattr(args, "member_bundles_dir", DEFAULT_CONTEXT_BUNDLES_DIR)
    ).resolve(strict=False)
    context_package_record = _context_package_record(
        context_bundles_dir, composition, args.ayah
    )
    (
        source_origin,
        source_payload,
        source_bundle,
        docket,
        docket_lineage,
    ) = _load_focus_inputs(args, context_bundles_dir, member_bundles_dir)
    try:
        unit_identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=args.ayah
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    docket_payload = _canonical_json_bytes(docket, newline=True)
    if source_bundle.get("ayahRef") != args.ayah:
        raise WorkflowError("Source bundle ayah identity does not match --ayah")
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise WorkflowError("Docket ayah identity does not match --ayah")
    if (
        v3._sha256_json(source_bundle)
        != docket.get("identity", {}).get("source_canonical_sha256")
    ):
        raise WorkflowError("Source bundle canonical hash does not match docket")
    prefatory_basmala_loaded = _load_prefatory_basmala_context(
        source_bundle, member_bundles_dir, composition
    )
    prefatory_basmala_packet_context = None
    prefatory_basmala_record = None
    if prefatory_basmala_loaded is not None:
        (
            basmala_origin,
            basmala_payload,
            basmala_bundle,
            basmala_identity,
        ) = prefatory_basmala_loaded
        _write_generated(
            layout.prefatory_basmala_bundle,
            basmala_payload,
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
        prefatory_basmala_record = {
            "snapshot": _path_record(layout.prefatory_basmala_bundle),
            "origin": v3._stable_source_path(basmala_origin),
            "canonical_sha256": basmala_identity["canonical_sha256"],
            "ayah_ref": basmala_identity["ayah_ref"],
            "surface_ref": basmala_identity["surface_ref"],
            "linguistic_source_ref": basmala_identity["linguistic_source_ref"],
            "mode": "included_as_ordinary_context_member",
        }
        prefatory_basmala_packet_context = (
            basmala_origin,
            basmala_bundle,
            basmala_identity,
        )

    quran_evidence, quran_coverage = _quran_text_projection(args.quran_text)
    if composition is not None:
        _validate_basmala_focus_context(composition, quran_evidence)
    numbered_refs = {
        ref for ref in quran_evidence if ref.split(":", 1)[1] != "0"
    }
    if unit_identity["unit_kind"] == "prefatory_basmala":
        inter_rows: list[dict[str, Any]] = []
        reciprocal: dict[str, list[dict[str, Any]]] = {}
        inter_coverage = {
            "status": "not_applicable",
            "reason": "inter-ayah evidence is defined on numbered focus ayahs only",
            "focus_ref": args.ayah,
        }
        inter_ayah_inputs = None
    else:
        inter_ayah_inputs = _inter_ayah_input_record(
            args.inter_ayah_dir, args.inter_ayah_parent_dir
        )
        inter_rows, reciprocal, inter_coverage = v3._inter_ayah_evidence_with_fallback(
            args.ayah,
            args.inter_ayah_dir,
            args.inter_ayah_parent_dir,
            numbered_refs,
        )
    hft_projection = v3._hft_authoring_projection(docket, source_bundle)
    composition_projection = (
        _composition_projection(
            composition,
            args.ayah,
            source_bundle,
            context_bundles_dir,
            member_bundles_dir,
        )
        if composition is not None
        else None
    )

    layout.input.mkdir(parents=True, exist_ok=True)
    layout.raw.mkdir(parents=True, exist_ok=True)
    layout.editorial.mkdir(parents=True, exist_ok=True)
    _assert_layout(layout)
    if composition is not None:
        _write_generated(
            layout.composition,
            _pretty_json_bytes(composition.canonical_payload),
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
    _write_generated(
        layout.source_bundle,
        source_payload,
        replace_changed=args.force_input,
        root=INPUT_ROOT,
    )
    _write_generated(
        layout.docket,
        docket_payload,
        replace_changed=args.force_input,
        root=INPUT_ROOT,
    )

    lane_records: dict[str, Any] = {}
    prefatory_basmala_context_units: list[dict[str, Any]] = []
    for lane in LANES:
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
        packet = _augment_lane_packet(
            packet,
            layout=layout,
            composition=composition,
            projection=composition_projection,
            source_bundle=source_bundle,
            prefatory_basmala_context=prefatory_basmala_packet_context,
            lane=lane,
        )
        if prefatory_basmala_record is not None:
            units = packet.get("selected_context_units")
            if isinstance(units, list):
                for unit in units:
                    if (
                        isinstance(unit, dict)
                        and unit.get("ayah_ref")
                        == prefatory_basmala_record["ayah_ref"]
                    ):
                        prefatory_basmala_context_units.append(copy.deepcopy(unit))
                        break
        prompt, scope_record = _build_scope_prompt(layout, lane, packet)
        _write_generated(
            layout.packet(lane),
            _canonical_json_bytes(packet, newline=True),
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
        _write_generated(
            layout.scope_prompt(lane),
            prompt.encode("utf-8"),
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
        lane_records[lane] = {
            **scope_record,
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "packet": _path_record(layout.packet(lane)),
            "prompt": _path_record(layout.scope_prompt(lane)),
            "expected_response": _repo_path(layout.scope_contribution(lane)),
        }
    if prefatory_basmala_record is not None:
        prefatory_basmala_record["selected_context_units"] = (
            _dedupe_context_units(prefatory_basmala_context_units)
        )

    manifest = _input_manifest_base(
        layout,
        source_origin,
        docket_lineage,
        source_bundle,
        prefatory_basmala_record,
        docket,
        quran_coverage,
        inter_coverage,
        inter_ayah_inputs,
        lane_records,
        composition,
        composition_projection,
        context_package_record,
        context_bundles_dir,
        member_bundles_dir,
    )
    if layout.manifest.exists():
        if layout.manifest.is_symlink() or not layout.manifest.is_file():
            raise WorkflowError(
                f"Unit manifest is not a regular file: {layout.manifest}"
            )
        previous = _load_json(layout.manifest)
        previous_base = {
            **previous,
            "canonical": None,
            "editorial_turn": None,
        }
        if previous_base == manifest:
            manifest["canonical"] = previous.get("canonical")
            manifest["editorial_turn"] = previous.get("editorial_turn")
        elif not args.force_input:
            raise WorkflowError(
                "The unit manifest changed. Commit or inspect the current state, "
                "then rerun prepare with --force-input."
            )
    _write_generated(
        layout.manifest,
        _pretty_json_bytes(manifest),
        replace_changed=True,
        root=INPUT_ROOT,
    )
    return {
        "schema_version": "commentary-v4-status-v1",
        "analysis_id": layout.analysis_id,
        "ayah_ref": args.ayah,
        "status": "prepared",
        "input": str(layout.input),
        "raw": str(layout.raw),
        "editorial": str(layout.editorial),
        "manifest": str(layout.manifest),
    }


def _record_path(record: dict[str, Any], *, label: str) -> Path:
    if not isinstance(record, dict):
        raise WorkflowError(f"Manifest {label} is not an object")
    value = record.get("path")
    if not isinstance(value, str) or not value:
        raise WorkflowError(f"Manifest {label} has no path")
    path = (REPO_ROOT / value).resolve(strict=False)
    try:
        path.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise WorkflowError(f"Manifest {label} path escapes repository") from exc
    return path


def _verify_record(
    record: dict[str, Any], *, label: str, expected: Path | None = None
) -> Path:
    if expected is not None and (
        not isinstance(record, dict)
        or record.get("path") != _repo_path(expected)
    ):
        raise WorkflowError(f"Manifest {label} does not name its fixed unit path")
    path = _record_path(record, label=label)
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"Manifest {label} is missing or not regular: {path}")
    payload = path.read_bytes()
    if record.get("bytes") != len(payload) or record.get("sha256") != _sha256(payload):
        raise WorkflowError(f"Manifest {label} is stale: {path}")
    return path


def _verify_source_binding(
    record: dict[str, Any],
    *,
    path_field: str,
    hash_field: str,
    expected: Path,
    label: str,
) -> None:
    if not isinstance(record, dict):
        raise WorkflowError(f"Manifest {label} is not an object")
    if record.get(path_field) != _repo_path(expected):
        raise WorkflowError(f"Manifest {label} does not name its fixed source")
    try:
        payload = expected.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read {label} {expected}: {exc}") from exc
    if record.get(hash_field) != _sha256(payload):
        raise WorkflowError(f"Manifest {label} source changed: {expected}")


def _verify_context_package_record(record: Any) -> dict[str, Any] | None:
    if record is None:
        return None
    if not isinstance(record, dict):
        raise WorkflowError("Manifest context_package record is malformed")
    manifest_path = _verify_record(
        record.get("manifest"), label="pericope package manifest"
    )
    try:
        package = pericope_manifests.validate_manifest(
            manifest_path,
            repo_root=REPO_ROOT,
            expected_builder=SCRIPTS_ROOT / "build_pericope_bundles.py",
            expected_lower_level_builder=SCRIPTS_ROOT / "build_bundle.py",
        )
    except pericope_manifests.PericopeManifestError as exc:
        raise WorkflowError(str(exc)) from exc
    expected = {
        "schema_version": package["schema_version"],
        "canonical_sha256": v3._sha256_json(package),
        "surah": package["surah"],
        "pericope": package["pericope"],
        "ayah_refs": package["ayah_refs"],
    }
    for field, value in expected.items():
        if record.get(field) != value:
            raise WorkflowError(f"Manifest context package field is stale: {field}")
    return package


def _required_prefatory_ref(source_bundle: dict[str, Any]) -> str | None:
    ref = source_bundle.get("ayahRef")
    if not isinstance(ref, str):
        raise WorkflowError("Source snapshot has no ayahRef")
    try:
        identity = compositions.validate_unit_bundle(source_bundle, expected_ref=ref)
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if identity["unit_kind"] != "numbered_ayah":
        return None
    surah = source_bundle["surah"]
    if surah in compositions.BASMALA_EXCLUDED_SURAHS:
        return None
    return f"{surah}:0"


def _verify_prefatory_basmala_record(
    manifest: dict[str, Any],
    layout: Layout,
    source_bundle: dict[str, Any],
) -> dict[str, Any] | None:
    expected_ref = _required_prefatory_ref(source_bundle)
    record = manifest.get("prefatory_basmala")
    if expected_ref is None:
        if record is not None:
            raise WorkflowError("Manifest carries an inapplicable prefatory basmala")
        return None
    if not isinstance(record, dict):
        raise WorkflowError(
            f"Manifest is missing mandatory prefatory basmala {expected_ref}"
        )
    snapshot_path = _verify_record(
        record.get("snapshot"),
        label="prefatory basmala snapshot",
        expected=layout.prefatory_basmala_bundle,
    )
    bundle = _load_json(snapshot_path)
    try:
        identity = compositions.validate_unit_bundle(bundle, expected_ref=expected_ref)
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    identity["canonical_sha256"] = compositions.canonical_sha256(bundle)
    identity["bytes"] = snapshot_path.stat().st_size
    for field in (
        "ayah_ref",
        "surface_ref",
        "linguistic_source_ref",
        "canonical_sha256",
    ):
        if record.get(field) != identity[field]:
            raise WorkflowError(f"Prefatory basmala manifest field is stale: {field}")
    if record.get("mode") != "included_as_ordinary_context_member":
        raise WorkflowError("Prefatory basmala manifest mode is stale")
    selected = record.get("selected_context_units")
    if not isinstance(selected, list):
        raise WorkflowError("Prefatory basmala context lineage is malformed")
    deduped = _dedupe_context_units(selected)
    if len(deduped) != 1:
        raise WorkflowError("Prefatory basmala context lineage must contain one unit")
    selected_unit = deduped[0]
    selected_lanes = selected_unit.get("lanes")
    if (
        selected_unit.get("ayah_ref") != expected_ref
        or selected_unit.get("canonical_sha256") != identity["canonical_sha256"]
        or not isinstance(selected_lanes, list)
        or selected_lanes != ["macro"]
    ):
        raise WorkflowError("Prefatory basmala context lineage is stale")
    return identity


def _load_unit_manifest(layout: Layout) -> dict[str, Any]:
    _assert_layout(layout)
    if not layout.manifest.is_file() or layout.manifest.is_symlink():
        raise WorkflowError(f"Unit manifest is missing or not regular: {layout.manifest}")
    manifest = _load_json(layout.manifest)
    if manifest.get("schema_version") != UNIT_MANIFEST_SCHEMA_VERSION:
        raise WorkflowError(
            f"Unit manifest uses legacy or stale schema "
            f"{manifest.get('schema_version')!r}; expected "
            f"{UNIT_MANIFEST_SCHEMA_VERSION}. Preserve the current Git state, "
            "relocate legacy raw/editorial artifacts, and rerun advance with "
            "--force-input."
        )
    if (
        manifest.get("analysis_id") != layout.analysis_id
        or manifest.get("ayah_ref") != layout.ayah_ref
    ):
        raise WorkflowError("Unit manifest identity does not match analysis/focus")
    expected_layout = {
        "input": _repo_path(layout.input),
        "raw": _repo_path(layout.raw),
        "editorial": _repo_path(layout.editorial),
    }
    if manifest.get("layout") != expected_layout:
        raise WorkflowError("Unit manifest layout does not match the fixed v4 paths")
    try:
        source_record = manifest["source"]["snapshot"]
        docket_record = manifest["docket"]["snapshot"]
        context_package_record = manifest["context_package"]
        canonical_template = manifest["canonical_template"]
        editorial = manifest["editorial"]
    except (KeyError, TypeError) as exc:
        raise WorkflowError("Unit manifest is missing required records") from exc
    source_path = _verify_record(
        source_record,
        label="source snapshot",
        expected=layout.source_bundle,
    )
    docket_path = _verify_record(
        docket_record,
        label="docket snapshot",
        expected=layout.docket,
    )
    source_bundle = _load_json(source_path)
    try:
        source_identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=layout.ayah_ref
        )
    except compositions.CompositionError as exc:
        raise WorkflowError(str(exc)) from exc
    if manifest["source"].get("canonical_sha256") != v3._sha256_json(source_bundle):
        raise WorkflowError("Manifest source canonical hash is stale")
    docket = _load_json(docket_path)
    if (
        manifest["docket"].get("payload_sha256") != _docket_payload_hash(docket)
        or docket.get("identity", {}).get("docket_payload_sha256")
        != _docket_payload_hash(docket)
    ):
        raise WorkflowError("Manifest docket payload hash is stale")
    evidence_projection = manifest.get("evidence_projection")
    if not isinstance(evidence_projection, dict):
        raise WorkflowError("Manifest evidence projection is missing or malformed")
    implementation = evidence_projection.get("implementation")
    if not isinstance(implementation, dict):
        raise WorkflowError("Manifest evidence implementation record is malformed")
    for key, expected in (
        ("workflow", Path(__file__)),
        ("composition", Path(compositions.__file__)),
        ("v3_projection", V3_ROOT / "render_authoring.py"),
    ):
        _verify_record(
            implementation.get(key),
            label=f"{key} implementation",
            expected=expected,
        )
    quran_evidence, quran_coverage = _verified_quran_text_projection(
        evidence_projection.get("quran_text")
    )
    inter_ayah_coverage = evidence_projection.get("inter_ayah")
    _verified_inter_ayah_projection(
        inter_ayah_coverage,
        evidence_projection.get("inter_ayah_inputs"),
        focus_ref=layout.ayah_ref,
        numbered_refs={
            ref for ref in quran_evidence if ref.split(":", 1)[1] != "0"
        },
        prefatory_focus=source_identity["unit_kind"] == "prefatory_basmala",
    )
    prefatory_identity = _verify_prefatory_basmala_record(
        manifest, layout, source_bundle
    )
    context_package = _verify_context_package_record(context_package_record)
    analysis = manifest.get("analysis")
    if not isinstance(analysis, dict) or analysis.get("analysis_id") != layout.analysis_id:
        raise WorkflowError("Manifest analysis record is missing or stale")
    composition: compositions.Composition | None = None
    if layout.analysis_id == "native":
        if analysis.get("mode") != "native" or analysis.get("composition") is not None:
            raise WorkflowError("Native unit carries a non-native composition")
        if source_identity["unit_kind"] == "prefatory_basmala":
            raise WorkflowError(
                f"Legacy native input for {layout.ayah_ref} has no complete "
                "host-surah context; rerun the CLI to derive the full basmala analysis"
            )
    else:
        if analysis.get("mode") != "ordered_composition":
            raise WorkflowError("Custom analysis lacks ordered composition metadata")
        composition_path = _verify_record(
            analysis.get("composition"),
            label="analysis composition",
            expected=layout.composition,
        )
        try:
            composition = compositions.load_composition(composition_path)
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        if (
            composition.analysis_id != layout.analysis_id
            or composition.canonical_sha256
            != analysis.get("composition_canonical_sha256")
            or layout.ayah_ref not in composition.focus_refs
        ):
            raise WorkflowError("Analysis composition identity is stale")
        if (
            composition.member_surah is not None
            and source_bundle.get("surah") != composition.member_surah
        ):
            raise WorkflowError("Analysis focus does not belong to its host surah")
        _validate_basmala_focus_context(composition, quran_evidence)
    if context_package is not None:
        required_package_refs: set[str] = set()
        if not _is_prefatory_ref(layout.ayah_ref):
            required_package_refs.add(layout.ayah_ref)
        if composition is not None:
            required_package_refs.update(
                row["ref"]
                for row in composition.context_rows(layout.ayah_ref)
                if row.get("membership_added_ayah") is not True
                and not _is_prefatory_ref(row["ref"])
            )
        missing = sorted(required_package_refs - set(context_package["ayah_refs"]))
        if missing:
            raise WorkflowError(
                f"Manifest pericope package omits required ayat: {missing}"
            )
    selected_units = analysis.get("selected_context_units")
    if selected_units is None:
        selected_units = []
    if not isinstance(selected_units, list):
        raise WorkflowError("Analysis context-unit lineage is malformed")
    deduped_selected_units = _dedupe_context_units(selected_units)
    if deduped_selected_units != selected_units:
        raise WorkflowError("Analysis context-unit lineage is duplicated or noncanonical")
    expected_context_lanes = _expected_context_lanes(
        composition,
        layout.ayah_ref,
        prefatory_identity["ayah_ref"] if prefatory_identity is not None else None,
    )
    selected_by_ref = {
        str(unit.get("ayah_ref")): unit
        for unit in selected_units
        if isinstance(unit, dict)
    }
    if set(selected_by_ref) != set(expected_context_lanes):
        missing = sorted(set(expected_context_lanes) - set(selected_by_ref))
        extra = sorted(set(selected_by_ref) - set(expected_context_lanes))
        raise WorkflowError(
            "Analysis context-unit lineage disagrees with its composition; "
            f"missing={missing}, extra={extra}"
        )
    for context_ref, expected_lanes in expected_context_lanes.items():
        actual_lanes = selected_by_ref[context_ref].get("lanes")
        if not isinstance(actual_lanes, list) or set(actual_lanes) != set(expected_lanes):
            raise WorkflowError(
                f"Analysis context-unit lane binding is stale for {context_ref}"
            )
    expected_context_projections: dict[str, dict[str, Any]] = {}
    for unit in selected_units:
        if not isinstance(unit, dict):
            raise WorkflowError("Analysis context-unit lineage contains a non-object")
        source_file = unit.get("source_file")
        if not isinstance(source_file, str) or not source_file:
            raise WorkflowError("Analysis context unit has no source_file")
        source_path = Path(source_file)
        if not source_path.is_absolute():
            source_path = PROJECTS_ROOT / source_path
        if not source_path.is_file() or source_path.is_symlink():
            raise WorkflowError(f"Analysis context source is unavailable: {source_path}")
        source_bytes = source_path.read_bytes()
        if len(source_bytes) != unit.get("bytes"):
            raise WorkflowError(f"Analysis context source size changed: {source_path}")
        try:
            source_value = json.loads(source_bytes)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise WorkflowError(f"Invalid analysis context source {source_path}: {exc}") from exc
        if compositions.canonical_sha256(source_value) != unit.get(
            "canonical_sha256"
        ):
            raise WorkflowError(f"Analysis context source changed: {source_path}")
        try:
            compositions.validate_unit_bundle(
                source_value, expected_ref=str(unit.get("ayah_ref"))
            )
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        expected_projection = compositions.context_member_payload(
            source_value, focus_bundle=source_bundle
        )
        expected_projection_sha256 = compositions.canonical_sha256(
            expected_projection
        )
        if (
            unit.get("context_projection_protocol")
            != compositions.CONTEXT_MEMBER_PROTOCOL
            or unit.get("context_projection_sha256")
            != expected_projection_sha256
            or unit.get("context_projection_bytes")
            != len(_canonical_json_bytes(expected_projection))
        ):
            raise WorkflowError(
                f"Analysis context projection is stale: {source_path}"
            )
        expected_context_projections[str(unit["ayah_ref"])] = expected_projection
    _verify_source_binding(
        canonical_template,
        path_field="path",
        hash_field="sha256",
        expected=PROMPTS_ROOT / "canonical.md",
        label="canonical template",
    )
    _verify_source_binding(
        editorial,
        path_field="instructions_source",
        hash_field="instructions_sha256",
        expected=V3_PROMPTS_ROOT / "editorial-followup.md",
        label="editorial instructions",
    )
    _verify_source_binding(
        editorial,
        path_field="handoff_template_source",
        hash_field="handoff_template_sha256",
        expected=PROMPTS_ROOT / "editorial.md",
        label="editorial handoff template",
    )
    expected_editorial_outputs = {
        kind: _repo_path(layout.editorial_output(kind)) for kind in KINDS
    }
    if editorial.get("expected_outputs") != expected_editorial_outputs:
        raise WorkflowError("Manifest editorial outputs do not match fixed unit paths")
    for lane in LANES:
        lane_record = manifest.get("lanes", {}).get(lane)
        if not isinstance(lane_record, dict):
            raise WorkflowError(f"Manifest is missing {lane} lane")
        try:
            packet_record = lane_record["packet"]
            prompt_record = lane_record["prompt"]
        except KeyError as exc:
            raise WorkflowError(f"Manifest {lane} lane is incomplete") from exc
        packet_path = _verify_record(
            packet_record,
            label=f"{lane} packet",
            expected=layout.packet(lane),
        )
        prompt_path = _verify_record(
            prompt_record,
            label=f"{lane} prompt",
            expected=layout.scope_prompt(lane),
        )
        packet = _load_json(packet_path)
        packet_source_coverage = packet.get("source_coverage")
        if not isinstance(packet_source_coverage, dict):
            raise WorkflowError(f"Manifest {lane} packet source coverage is malformed")
        if packet_source_coverage.get("quran_text_source") != quran_coverage:
            raise WorkflowError(
                f"Manifest {lane} packet Quran text provenance is stale"
            )
        if packet_source_coverage.get("inter_ayah_source") != inter_ayah_coverage:
            raise WorkflowError(
                f"Manifest {lane} packet inter-ayah provenance is stale"
            )
        packet_hash = v3._payload_hash_with_identity_field_removed(
            packet, "lane_packet_sha256"
        )
        if (
            packet.get("identity", {}).get("lane_packet_sha256") != packet_hash
            or lane_record.get("lane_packet_sha256") != packet_hash
        ):
            raise WorkflowError(f"Manifest {lane} packet identity hash is stale")
        expected_prompt, expected_scope_record = _build_scope_prompt(
            layout, lane, packet
        )
        for field in (
            "request_sha256",
            "request_inputs",
            "response_schema_version",
            "template_source",
            "template_sha256",
        ):
            if lane_record.get(field) != expected_scope_record[field]:
                raise WorkflowError(
                    f"Manifest {lane} scope author record is stale: {field}"
                )
        if prompt_path.read_text(encoding="utf-8") != expected_prompt:
            raise WorkflowError(f"Manifest {lane} scope prompt content is stale")
        packet_units = packet.get("selected_context_units", [])
        if not isinstance(packet_units, list):
            raise WorkflowError(f"Manifest {lane} packet context units are malformed")
        if not all(isinstance(unit, dict) for unit in packet_units):
            raise WorkflowError(
                f"Manifest {lane} packet contains a malformed context unit"
            )
        expected_lane_refs = _expected_lane_context_refs(
            composition,
            layout.ayah_ref,
            prefatory_identity["ayah_ref"] if prefatory_identity is not None else None,
            lane,
        )
        actual_lane_refs = [str(unit.get("ayah_ref")) for unit in packet_units]
        if actual_lane_refs != expected_lane_refs:
            raise WorkflowError(
                f"Manifest {lane} packet context membership is stale; "
                f"expected={expected_lane_refs}, actual={actual_lane_refs}"
            )
        packet_supports = packet.get("support_registry", [])
        if not isinstance(packet_supports, list):
            raise WorkflowError(f"Manifest {lane} packet supports are malformed")
        for packet_unit in packet_units:
            context_ref = packet_unit.get("ayah_ref")
            expected_projection = expected_context_projections.get(str(context_ref))
            if expected_projection is None:
                raise WorkflowError(
                    f"Manifest {lane} packet has unbound context unit {context_ref}"
                )
            matching_supports = [
                support
                for support in packet_supports
                if isinstance(support, dict)
                and support.get("role") == "context_unit_native_depth_evidence"
                and support.get("context_refs") == [context_ref]
            ]
            if (
                len(matching_supports) != 1
                or matching_supports[0].get("payload") != expected_projection
                or packet_unit.get("context_projection_sha256")
                != compositions.canonical_sha256(expected_projection)
            ):
                raise WorkflowError(
                    f"Manifest {lane} packet context projection is stale for "
                    f"{context_ref}"
                )
        if prefatory_identity is not None and lane in expected_context_lanes.get(
            prefatory_identity["ayah_ref"], []
        ):
            matching_units = [
                unit
                for unit in packet.get("selected_context_units", [])
                if isinstance(unit, dict)
                and unit.get("ayah_ref") == prefatory_identity["ayah_ref"]
            ]
            prefatory_scope = packet.get("scope", {}).get("prefatory_basmala")
            if (
                len(matching_units) != 1
                or matching_units[0].get("canonical_sha256")
                != prefatory_identity["canonical_sha256"]
                or not isinstance(prefatory_scope, dict)
                or prefatory_scope.get("source_bundle_canonical_sha256")
                != prefatory_identity["canonical_sha256"]
            ):
                raise WorkflowError(
                    f"Manifest {lane} packet lacks its mandatory prefatory basmala"
                )
        if lane_record.get("expected_response") != _repo_path(
            layout.scope_contribution(lane)
        ):
            raise WorkflowError(
                f"Manifest {lane} response does not match its fixed unit path"
            )
    if manifest.get("canonical") is not None and not isinstance(
        manifest["canonical"], dict
    ):
        raise WorkflowError("Manifest canonical record is malformed")
    if manifest.get("editorial_turn") is not None and not isinstance(
        manifest["editorial_turn"], dict
    ):
        raise WorkflowError("Manifest editorial turn record is malformed")
    return manifest


def _required_text(value: Any, *, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise WorkflowError(f"{label} must be a nonempty string")
    return value


def _string_list(value: Any, *, label: str) -> list[str]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise WorkflowError(f"{label} must be an array of nonempty strings")
    if len(value) != len(set(value)):
        raise WorkflowError(f"{label} contains duplicates")
    return value


def _packet_id_set(
    packet: dict[str, Any], registry: str, field: str, *, lane: str
) -> set[str]:
    rows = packet.get(registry)
    if not isinstance(rows, list):
        raise WorkflowError(f"{lane} packet {registry} is malformed")
    values = {
        row.get(field)
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(field), str)
    }
    if len(values) != len(rows):
        raise WorkflowError(f"{lane} packet {registry} has missing or duplicate IDs")
    return values


def _packet_quran_refs(packet: dict[str, Any]) -> set[str]:
    refs: set[str] = set()

    def visit(value: Any) -> None:
        if isinstance(value, str):
            if compositions.REF_RE.fullmatch(value) is not None:
                refs.add(value)
            return
        if isinstance(value, list):
            for item in value:
                visit(item)
            return
        if isinstance(value, dict):
            for item in value.values():
                visit(item)

    visit(packet)
    return refs


def _validate_scope_contribution(
    contribution: dict[str, Any],
    *,
    layout: Layout,
    manifest: dict[str, Any],
    lane: str,
    packet: dict[str, Any],
) -> None:
    expected_top_level = {
        "schema_version",
        "identity",
        "ayah_ref",
        "lane",
        "coverage_complete",
        "candidate_decisions",
        "findings",
        "movements",
        "friction_notes",
    }
    if set(contribution) != expected_top_level:
        raise WorkflowError(
            f"{lane} contribution fields are malformed; "
            f"missing={sorted(expected_top_level - set(contribution))}, "
            f"extra={sorted(set(contribution) - expected_top_level)}"
        )
    if contribution.get("schema_version") != SCOPE_CONTRIBUTION_SCHEMA_VERSION:
        raise WorkflowError(f"{lane} contribution schema_version is stale")
    lane_record = manifest["lanes"][lane]
    expected_identity = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": lane_record["lane_packet_sha256"],
        "authoring_request_sha256": lane_record["request_sha256"],
    }
    if contribution.get("identity") != expected_identity:
        raise WorkflowError(f"{lane} contribution identity is stale or mixed")
    if (
        contribution.get("ayah_ref") != layout.ayah_ref
        or contribution.get("lane") != lane
    ):
        raise WorkflowError(f"{lane} contribution top-level identity is stale or mixed")
    if contribution.get("coverage_complete") is not True:
        raise WorkflowError(f"{lane} contribution must declare coverage_complete=true")

    candidate_ids = _packet_id_set(
        packet, "candidate_inventory", "candidate_id", lane=lane
    )
    support_ids = _packet_id_set(
        packet, "support_registry", "support_id", lane=lane
    )
    branch_refs = _packet_id_set(
        packet, "branch_registry", "branch_ref", lane=lane
    )
    connection_refs = _packet_id_set(
        packet, "connection_registry", "connection_ref", lane=lane
    )
    quran_refs = _packet_quran_refs(packet)

    raw_decisions = contribution.get("candidate_decisions")
    if not isinstance(raw_decisions, list):
        raise WorkflowError(f"{lane} candidate_decisions must be an array")
    decisions: dict[str, dict[str, Any]] = {}
    expected_decision_fields = {
        "candidate_id",
        "decision",
        "reason",
        "finding_refs",
    }
    for index, decision in enumerate(raw_decisions):
        label = f"{lane} candidate_decisions[{index}]"
        if not isinstance(decision, dict) or set(decision) != expected_decision_fields:
            raise WorkflowError(f"{label} fields are malformed")
        candidate_id = _required_text(decision.get("candidate_id"), label=f"{label}.candidate_id")
        if candidate_id in decisions:
            raise WorkflowError(f"{lane} candidate decision is duplicated: {candidate_id}")
        disposition = decision.get("decision")
        if disposition not in {"accept", "narrow", "represented", "reject"}:
            raise WorkflowError(f"{label}.decision is invalid")
        _required_text(decision.get("reason"), label=f"{label}.reason")
        finding_refs = _string_list(
            decision.get("finding_refs"), label=f"{label}.finding_refs"
        )
        if disposition == "reject" and finding_refs:
            raise WorkflowError(f"{label} rejects a candidate but names findings")
        if disposition != "reject" and not finding_refs:
            raise WorkflowError(f"{label} must name at least one finding")
        decisions[candidate_id] = decision
    if set(decisions) != candidate_ids:
        raise WorkflowError(
            f"{lane} candidate accounting is incomplete; "
            f"missing={sorted(candidate_ids - set(decisions))}, "
            f"extra={sorted(set(decisions) - candidate_ids)}"
        )

    raw_findings = contribution.get("findings")
    if not isinstance(raw_findings, list):
        raise WorkflowError(f"{lane} findings must be an array")
    expected_finding_fields = {
        "finding_ref",
        "title",
        "claim",
        "mechanism",
        "reader_payoff",
        "containment",
        "epistemic_status",
        "candidate_ids",
        "support_ids",
        "branch_refs",
        "connection_refs",
        "context_refs",
    }
    findings: dict[str, dict[str, Any]] = {}
    finding_ref_re = re.compile(
        rf"{re.escape(lane)}:[A-Za-z0-9][A-Za-z0-9._-]{{0,95}}"
    )
    for index, finding in enumerate(raw_findings):
        label = f"{lane} findings[{index}]"
        if not isinstance(finding, dict) or set(finding) != expected_finding_fields:
            raise WorkflowError(f"{label} fields are malformed")
        finding_ref = _required_text(
            finding.get("finding_ref"), label=f"{label}.finding_ref"
        )
        if finding_ref_re.fullmatch(finding_ref) is None:
            raise WorkflowError(f"{label}.finding_ref is invalid")
        if finding_ref in findings:
            raise WorkflowError(f"{lane} finding is duplicated: {finding_ref}")
        for field in (
            "title",
            "claim",
            "mechanism",
            "reader_payoff",
            "containment",
            "epistemic_status",
        ):
            _required_text(finding.get(field), label=f"{label}.{field}")
        cited_candidates = _string_list(
            finding.get("candidate_ids"), label=f"{label}.candidate_ids"
        )
        cited_supports = _string_list(
            finding.get("support_ids"), label=f"{label}.support_ids"
        )
        cited_branches = _string_list(
            finding.get("branch_refs"), label=f"{label}.branch_refs"
        )
        cited_connections = _string_list(
            finding.get("connection_refs"), label=f"{label}.connection_refs"
        )
        cited_context = _string_list(
            finding.get("context_refs"), label=f"{label}.context_refs"
        )
        if not (cited_supports or cited_branches or cited_connections):
            raise WorkflowError(
                f"{label} must cite at least one support, branch, or connection ID"
            )
        for cited, available, field in (
            (set(cited_candidates), candidate_ids, "candidate_ids"),
            (set(cited_supports), support_ids, "support_ids"),
            (set(cited_branches), branch_refs, "branch_refs"),
            (set(cited_connections), connection_refs, "connection_refs"),
            (set(cited_context), quran_refs, "context_refs"),
        ):
            unknown = sorted(cited - available)
            if unknown:
                raise WorkflowError(f"{label}.{field} cites unknown IDs: {unknown}")
        findings[finding_ref] = finding

    for candidate_id, decision in decisions.items():
        decision_refs = set(decision["finding_refs"])
        unknown = sorted(decision_refs - set(findings))
        if unknown:
            raise WorkflowError(
                f"{lane} decision {candidate_id} cites unknown findings: {unknown}"
            )
        actual_refs = {
            finding_ref
            for finding_ref, finding in findings.items()
            if candidate_id in finding["candidate_ids"]
        }
        if decision["decision"] == "reject":
            if actual_refs:
                raise WorkflowError(
                    f"{lane} rejected candidate {candidate_id} appears in findings"
                )
        elif actual_refs != decision_refs:
            raise WorkflowError(
                f"{lane} candidate-to-finding links disagree for {candidate_id}"
            )

    raw_movements = contribution.get("movements")
    if not isinstance(raw_movements, list):
        raise WorkflowError(f"{lane} movements must be an array")
    expected_movement_fields = {"movement_key", "draft_prose", "finding_refs"}
    movement_keys: set[str] = set()
    landed_refs: list[str] = []
    for index, movement in enumerate(raw_movements):
        label = f"{lane} movements[{index}]"
        if not isinstance(movement, dict) or set(movement) != expected_movement_fields:
            raise WorkflowError(f"{label} fields are malformed")
        movement_key = _required_text(
            movement.get("movement_key"), label=f"{label}.movement_key"
        )
        if movement_key in movement_keys:
            raise WorkflowError(f"{lane} movement key is duplicated: {movement_key}")
        movement_keys.add(movement_key)
        _required_text(movement.get("draft_prose"), label=f"{label}.draft_prose")
        movement_refs = _string_list(
            movement.get("finding_refs"), label=f"{label}.finding_refs"
        )
        if not movement_refs:
            raise WorkflowError(f"{label} must land at least one finding")
        unknown = sorted(set(movement_refs) - set(findings))
        if unknown:
            raise WorkflowError(f"{label} cites unknown findings: {unknown}")
        landed_refs.extend(movement_refs)
    if len(landed_refs) != len(set(landed_refs)):
        raise WorkflowError(f"{lane} findings land in more than one movement")
    if set(landed_refs) != set(findings):
        raise WorkflowError(
            f"{lane} finding-to-movement coverage is incomplete; "
            f"missing={sorted(set(findings) - set(landed_refs))}, "
            f"extra={sorted(set(landed_refs) - set(findings))}"
        )
    _string_list(contribution.get("friction_notes"), label=f"{lane} friction_notes")


def _load_contribution(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any] | None:
    path = layout.scope_contribution(lane)
    if not path.exists():
        return None
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"{lane} contribution is not a regular file: {path}")
    contribution = _load_json(path)
    packet = _load_json(layout.packet(lane))
    _validate_scope_contribution(
        contribution,
        layout=layout,
        manifest=manifest,
        lane=lane,
        packet=packet,
    )
    return contribution


def _canonical_inputs() -> dict[str, str]:
    paths = {
        "principles": REPO_ROOT / "PRINCIPLES.md",
        "commentary_spec": REPO_ROOT / "COMMENTARY_SPEC.md",
        "channels": REPO_ROOT / "docs" / "CHANNELS.md",
        "canonical_prompt_v2": REPO_ROOT / "_ayah_commentary" / "v2" / "PROMPT.md",
    }
    return {key: path.read_text(encoding="utf-8") for key, path in paths.items()}


def _build_canonical_prompt(
    layout: Layout,
    manifest: dict[str, Any],
    contributions: dict[str, dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "canonical.md"
    template = template_path.read_text(encoding="utf-8")
    packets = {lane: _load_json(layout.packet(lane)) for lane in LANES}
    focus_surface = packets["micro"].get("focus_surface_evidence")
    if not isinstance(focus_surface, dict) or not focus_surface:
        raise WorkflowError("Micro packet has no focus-surface evidence")
    if any(
        packet.get("focus_surface_evidence") != focus_surface
        for packet in packets.values()
    ):
        raise WorkflowError("Lane packets disagree on focus-surface evidence")
    focus_surface_bytes = _canonical_json_bytes(focus_surface)
    focus_surface_sha256 = _sha256(focus_surface_bytes)
    replacements = {
        "@@AYAH_REF@@": layout.ayah_ref,
        "@@PROSE_OUTPUT_PATH@@": _repo_path(layout.first_pass("prose")),
        "@@EVIDENCE_OUTPUT_PATH@@": _repo_path(layout.first_pass("evidence")),
        "@@INDEX_OUTPUT_PATH@@": _repo_path(layout.first_pass("index")),
        "@@FRICTION_OUTPUT_PATH@@": _repo_path(layout.first_pass("friction")),
        "@@PRINCIPLES_MD@@": governing["principles"],
        "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
        "@@CHANNELS_MD@@": governing["channels"],
        "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
        "@@FOCUS_SURFACE_SHA256@@": focus_surface_sha256,
        "@@FOCUS_SURFACE_JSON@@": focus_surface_bytes.decode("utf-8"),
        "@@MICRO_CONTRIBUTION_JSON@@": v3._canonical_json(
            contributions["micro"]
        ),
        "@@MACRO_CONTRIBUTION_JSON@@": v3._canonical_json(
            contributions["macro"]
        ),
        "@@GLOBAL_CONTRIBUTION_JSON@@": v3._canonical_json(
            contributions["global"]
        ),
    }
    prompt = _render(template, replacements, label="canonical prompt")
    contribution_records = {
        lane: _path_record(layout.scope_contribution(lane)) for lane in LANES
    }
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "template_sha256": _sha256(template.encode("utf-8")),
        "focus_surface_sha256": focus_surface_sha256,
        "editorial_instructions_sha256": manifest["editorial"][
            "instructions_sha256"
        ],
        "editorial_handoff_template_sha256": manifest["editorial"][
            "handoff_template_sha256"
        ],
        **{
            f"{key}_sha256": _sha256(text.encode("utf-8"))
            for key, text in governing.items()
        },
        **{
            f"{lane}_contribution_sha256": contribution_records[lane]["sha256"]
            for lane in LANES
        },
    }
    canonical_record = {
        "request_sha256": v3._request_sha256(
            "v4-canonical-merge", request_inputs
        ),
        "prompt": {
            "path": _repo_path(layout.canonical_prompt),
            "bytes": len(prompt.encode("utf-8")),
            "sha256": _sha256(prompt.encode("utf-8")),
        },
        "inputs": request_inputs,
        "contributions": contribution_records,
        "expected_outputs": {
            kind: _repo_path(layout.first_pass(kind)) for kind in KINDS
        },
    }
    return prompt, canonical_record


def _ensure_canonical(
    layout: Layout,
    manifest: dict[str, Any],
    contributions: dict[str, dict[str, Any]],
    *,
    write: bool = True,
) -> dict[str, Any]:
    prompt, expected = _build_canonical_prompt(
        layout, manifest, contributions
    )
    current = manifest.get("canonical")
    all_output_paths = (
        *(layout.first_pass(kind) for kind in KINDS),
        *(layout.editorial_output(kind) for kind in KINDS),
    )
    if current != expected:
        existing_outputs = [
            path for path in all_output_paths if path.exists() or path.is_symlink()
        ]
        if existing_outputs:
            raise WorkflowError(
                "Canonical inputs changed after prose output was written. Preserve "
                "the current Git state, clear or relocate the stale v4 outputs, and "
                "rerun the canonical writer."
            )
        if not write:
            raise WorkflowError(
                "Canonical prompt record is missing or stale; run advance first"
            )
        _write_generated(
            layout.canonical_prompt,
            prompt.encode("utf-8"),
            replace_changed=True,
            root=INPUT_ROOT,
        )
        manifest["canonical"] = expected
        manifest["editorial_turn"] = None
        _write_generated(
            layout.manifest,
            _pretty_json_bytes(manifest),
            replace_changed=True,
            root=INPUT_ROOT,
        )
    else:
        existing_outputs = [
            path for path in all_output_paths if path.exists() or path.is_symlink()
        ]
        if not existing_outputs and write:
            _write_generated(
                layout.canonical_prompt,
                prompt.encode("utf-8"),
                replace_changed=True,
                root=INPUT_ROOT,
            )
        elif not layout.canonical_prompt.exists():
            raise WorkflowError(
                "Canonical prompt is missing after prose output was written. "
                "Preserve or inspect the current Git state before recovery."
            )
    _verify_record(
        expected["prompt"],
        label="canonical prompt",
        expected=layout.canonical_prompt,
    )
    return expected


def _build_editorial_prompt(
    layout: Layout,
    canonical: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    first_pass: dict[str, dict[str, Any]] = {}
    for kind in KINDS:
        path = layout.first_pass(kind)
        if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
            raise WorkflowError(f"Missing or empty first-pass {kind}: {path}")
        first_pass[kind] = _path_record(path)

    instructions_path = V3_PROMPTS_ROOT / "editorial-followup.md"
    template_path = PROMPTS_ROOT / "editorial.md"
    instructions = instructions_path.read_text(encoding="utf-8")
    template = template_path.read_text(encoding="utf-8")
    replacements = {
        "@@AYAH_REF@@": layout.ayah_ref,
        "@@PROSE_INPUT_PATH@@": _repo_path(layout.first_pass("prose")),
        "@@EVIDENCE_INPUT_PATH@@": _repo_path(layout.first_pass("evidence")),
        "@@INDEX_INPUT_PATH@@": _repo_path(layout.first_pass("index")),
        "@@FRICTION_INPUT_PATH@@": _repo_path(layout.first_pass("friction")),
        "@@PROSE_INPUT_SHA256@@": first_pass["prose"]["sha256"],
        "@@EVIDENCE_INPUT_SHA256@@": first_pass["evidence"]["sha256"],
        "@@INDEX_INPUT_SHA256@@": first_pass["index"]["sha256"],
        "@@FRICTION_INPUT_SHA256@@": first_pass["friction"]["sha256"],
        "@@PROSE_OUTPUT_PATH@@": _repo_path(layout.editorial_output("prose")),
        "@@EVIDENCE_OUTPUT_PATH@@": _repo_path(
            layout.editorial_output("evidence")
        ),
        "@@INDEX_OUTPUT_PATH@@": _repo_path(layout.editorial_output("index")),
        "@@FRICTION_OUTPUT_PATH@@": _repo_path(
            layout.editorial_output("friction")
        ),
        "@@EDITORIAL_INSTRUCTIONS@@": instructions,
    }
    prompt = _render(template, replacements, label="editorial handoff")
    prompt_bytes = prompt.encode("utf-8")
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "canonical_request_sha256": canonical["request_sha256"],
        "template_sha256": _sha256(template.encode("utf-8")),
        "instructions_sha256": _sha256(instructions.encode("utf-8")),
        **{
            f"{kind}_input_sha256": first_pass[kind]["sha256"]
            for kind in KINDS
        },
    }
    record = {
        "request_sha256": v3._request_sha256(
            "v4-canonical-editorial", request_inputs
        ),
        "canonical_request_sha256": canonical["request_sha256"],
        "prompt": {
            "path": _repo_path(layout.editorial_prompt),
            "bytes": len(prompt_bytes),
            "sha256": _sha256(prompt_bytes),
        },
        "inputs": request_inputs,
        "first_pass": first_pass,
        "expected_outputs": {
            kind: _repo_path(layout.editorial_output(kind)) for kind in KINDS
        },
    }
    return prompt, record


def _ensure_editorial(
    layout: Layout,
    manifest: dict[str, Any],
    canonical: dict[str, Any],
    *,
    write: bool = True,
) -> dict[str, Any]:
    prompt, expected = _build_editorial_prompt(layout, canonical)
    current = manifest.get("editorial_turn")
    editorial_outputs = [layout.editorial_output(kind) for kind in KINDS]
    existing_outputs = [
        path for path in editorial_outputs if path.exists() or path.is_symlink()
    ]
    if current != expected:
        if existing_outputs:
            raise WorkflowError(
                "First-pass inputs changed after editorial output was written. "
                "Preserve the current Git state, clear or relocate the stale "
                "editorial outputs, and rerun the same canonical writer."
            )
        if not write:
            raise WorkflowError(
                "Editorial handoff record is missing or stale; run advance first"
            )
        _write_generated(
            layout.editorial_prompt,
            prompt.encode("utf-8"),
            replace_changed=True,
            root=INPUT_ROOT,
        )
        manifest["editorial_turn"] = expected
        _write_generated(
            layout.manifest,
            _pretty_json_bytes(manifest),
            replace_changed=True,
            root=INPUT_ROOT,
        )
    else:
        if not existing_outputs and write:
            _write_generated(
                layout.editorial_prompt,
                prompt.encode("utf-8"),
                replace_changed=True,
                root=INPUT_ROOT,
            )
        elif not layout.editorial_prompt.exists():
            raise WorkflowError(
                "Editorial handoff is missing after editorial output was written. "
                "Preserve or inspect the current Git state before recovery."
            )

    for kind in KINDS:
        _verify_record(
            expected["first_pass"][kind],
            label=f"editorial {kind} input",
            expected=layout.first_pass(kind),
        )
    _verify_record(
        expected["prompt"],
        label="editorial handoff",
        expected=layout.editorial_prompt,
    )
    return expected


def _scope_handoff(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any]:
    return {
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "role": f"{lane}_scope_author",
        "fresh_agent": True,
        "prompt": str(layout.scope_prompt(lane).resolve()),
        "expected_response": _handoff_output_path(
            layout.scope_contribution(lane),
            RAW_ROOT,
            label=f"{lane} contribution target",
        ),
        "workspace": str(REPO_ROOT),
        "request_sha256": manifest["lanes"][lane]["request_sha256"],
    }


def _canonical_handoff(
    layout: Layout, canonical: dict[str, Any]
) -> dict[str, Any]:
    expected_outputs = {
        kind: _handoff_output_path(
            layout.first_pass(kind),
            RAW_ROOT,
            label=f"first-pass {kind} target",
        )
        for kind in KINDS
    }
    return {
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "role": "canonical_writer",
        "fresh_agent": True,
        "prompt": str(layout.canonical_prompt.resolve()),
        "expected_outputs": expected_outputs,
        "workspace": str(REPO_ROOT),
        "request_sha256": canonical["request_sha256"],
        "after_first_pass": {
            "same_live_agent": True,
            "command": (
                f"python3 _commentary/v4/workflow.py advance "
                f"--analysis-id {layout.analysis_id} --ayah {layout.ayah_ref}"
            ),
        },
    }


def _editorial_handoff(
    layout: Layout, editorial_turn: dict[str, Any]
) -> dict[str, Any]:
    expected_outputs = {
        kind: _handoff_output_path(
            layout.editorial_output(kind),
            EDITORIAL_ROOT,
            label=f"editorial {kind} target",
        )
        for kind in KINDS
    }
    return {
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "role": "canonical_writer",
        "same_live_agent": True,
        "prompt": str(layout.editorial_prompt.resolve()),
        "first_pass_inputs": {
            kind: str(layout.first_pass(kind).resolve()) for kind in KINDS
        },
        "expected_outputs": expected_outputs,
        "workspace": str(REPO_ROOT),
        "request_sha256": editorial_turn["request_sha256"],
        "restart_if_agent_unavailable": str(layout.canonical_prompt.resolve()),
    }


def _nonempty_outputs(paths: dict[str, Path]) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    for kind, path in paths.items():
        if path.is_file() and not path.is_symlink() and path.stat().st_size > 0:
            present.append(kind)
        else:
            missing.append(kind)
    return present, missing


def _assert_fixed_output_names(layout: Layout) -> None:
    expected_by_root = {
        layout.raw: {
            *(layout.scope_contribution(lane).name for lane in LANES),
            *(layout.first_pass(kind).name for kind in KINDS),
        },
        layout.editorial: {
            layout.editorial_output(kind).name for kind in KINDS
        },
    }
    for root, expected_names in expected_by_root.items():
        if not root.exists():
            continue
        if not root.is_dir() or root.is_symlink():
            raise WorkflowError(f"Output root is not a regular directory: {root}")
        unexpected = sorted(
            child.name
            for child in root.iterdir()
            if not child.name.startswith(".") and child.name not in expected_names
        )
        if unexpected:
            raise WorkflowError(
                f"Unexpected v4 output artifacts in {root}: {unexpected}. "
                "Preserve, remove, or relocate them explicitly before advancing."
            )


def advance(args: argparse.Namespace) -> dict[str, Any]:
    layout = _layout_for_args(args)
    _assert_layout(layout)
    if args.force_input or not layout.manifest.exists():
        prepare(args)
    manifest = _load_unit_manifest(layout)
    _assert_fixed_output_names(layout)
    contributions: dict[str, dict[str, Any]] = {}
    missing_lanes: list[str] = []
    invalid_lanes: dict[str, str] = {}
    for lane in LANES:
        try:
            contribution = _load_contribution(layout, manifest, lane)
        except WorkflowError as exc:
            contribution = None
            invalid_lanes[lane] = str(exc)
        if contribution is None:
            missing_lanes.append(lane)
        else:
            contributions[lane] = contribution
    if invalid_lanes:
        details = "; ".join(
            f"{lane}: {issue}" for lane, issue in sorted(invalid_lanes.items())
        )
        raise WorkflowError(
            "Invalid scope contribution. V4 does not issue automated repair turns; "
            "inspect, remove, or replace the failed artifact explicitly before "
            f"advancing again. {details}"
        )
    if missing_lanes:
        return {
            "schema_version": "commentary-v4-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agents",
            "stage": "scope_authoring",
            "missing_lanes": missing_lanes,
            "handoffs": [
                _scope_handoff(layout, manifest, lane) for lane in missing_lanes
            ],
        }

    canonical = _ensure_canonical(layout, manifest, contributions)
    first_pass_paths = {kind: layout.first_pass(kind) for kind in KINDS}
    first_present, first_missing = _nonempty_outputs(first_pass_paths)
    if first_missing:
        return {
            "schema_version": "commentary-v4-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agent",
            "stage": "canonical_write",
            "present_outputs": first_present,
            "missing_outputs": first_missing,
            "handoff": _canonical_handoff(layout, canonical),
        }

    editorial_turn = _ensure_editorial(layout, manifest, canonical)
    editorial_paths = {kind: layout.editorial_output(kind) for kind in KINDS}
    editorial_present, editorial_missing = _nonempty_outputs(editorial_paths)
    if editorial_missing:
        return {
            "schema_version": "commentary-v4-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agent",
            "stage": "canonical_editorial",
            "present_outputs": editorial_present,
            "missing_outputs": editorial_missing,
            "handoff": _editorial_handoff(layout, editorial_turn),
        }
    return verify(args)


def verify(args: argparse.Namespace) -> dict[str, Any]:
    layout = _layout_for_args(args)
    _assert_layout(layout)
    manifest = _load_unit_manifest(layout)
    _assert_fixed_output_names(layout)
    contributions: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        contribution = _load_contribution(layout, manifest, lane)
        if contribution is None:
            raise WorkflowError(f"Missing {lane} scope contribution")
        contributions[lane] = contribution
    canonical = _ensure_canonical(
        layout, manifest, contributions, write=False
    )
    _ensure_editorial(layout, manifest, canonical, write=False)
    outputs: dict[str, dict[str, Any]] = {}
    for phase, paths in (
        ("raw", {kind: layout.first_pass(kind) for kind in KINDS}),
        ("editorial", {kind: layout.editorial_output(kind) for kind in KINDS}),
    ):
        outputs[phase] = {}
        for kind, path in paths.items():
            if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
                raise WorkflowError(f"Missing or empty {phase} {kind}: {path}")
            outputs[phase][kind] = _path_record(path)
    return {
        "schema_version": "commentary-v4-status-v1",
        "analysis_id": layout.analysis_id,
        "ayah_ref": args.ayah,
        "status": "complete",
        "semantic_validation": "agent_owned",
        "outputs": outputs,
    }


def _execute_one(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "prepare":
        return prepare(args)
    if args.command == "advance":
        return advance(args)
    return verify(args)


def _batch_result(
    args: argparse.Namespace, ayah_refs: list[str]
) -> tuple[dict[str, Any], bool]:
    if len(ayah_refs) > 1 and (
        getattr(args, "source_bundle", None) is not None
        or getattr(args, "docket", None) is not None
    ):
        raise WorkflowError(
            "--source-bundle and --docket are single-unit options; use the "
            "canonical bundle root for a multi-unit batch"
        )

    units: list[dict[str, Any]] = []
    parallel_handoffs: list[dict[str, Any]] = []
    stage_counts: dict[str, int] = {}
    error_count = 0
    for ayah_ref in ayah_refs:
        unit_args = argparse.Namespace(**{**vars(args), "ayah": ayah_ref})
        try:
            result = _execute_one(unit_args)
        except (WorkflowError, OSError, SystemExit) as exc:
            error_count += 1
            result = {
                "schema_version": "commentary-v4-error-v1",
                "analysis_id": _analysis_id(args),
                "ayah_ref": ayah_ref,
                "status": "error",
                "error": str(exc),
            }
        units.append(result)
        stage = result.get("stage")
        if isinstance(stage, str):
            stage_counts[stage] = stage_counts.get(stage, 0) + 1
        handoffs = result.get("handoffs")
        if isinstance(handoffs, list):
            for handoff in handoffs:
                if isinstance(handoff, dict):
                    parallel_handoffs.append(
                        {**handoff, "ayah_ref": ayah_ref, "stage": stage}
                    )
        handoff = result.get("handoff")
        if isinstance(handoff, dict):
            parallel_handoffs.append(
                {**handoff, "ayah_ref": ayah_ref, "stage": stage}
            )

    completed = sum(result.get("status") == "complete" for result in units)
    if error_count:
        status = "error" if error_count == len(units) else "partial_error"
    elif args.command == "prepare":
        status = "prepared"
    elif completed == len(units):
        status = "complete"
    else:
        status = "waiting_for_agents"
    return (
        {
            "schema_version": "commentary-v4-batch-status-v1",
            "command": args.command,
            "analysis_id": _analysis_id(args),
            "status": status,
            "ayah_refs": ayah_refs,
            "summary": {
                "units": len(units),
                "complete": completed,
                "errors": error_count,
                "stages": stage_counts,
                "ready_handoffs": len(parallel_handoffs),
            },
            "parallel_handoffs": parallel_handoffs,
            "units": units,
        },
        error_count > 0,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare and advance the simple commentary v4 workflow."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command, help_text in (
        ("prepare", "Build one self-contained unit input."),
        ("advance", "Return the next fixed agent handoff or completion status."),
    ):
        subparser = subparsers.add_parser(command, help=help_text)
        subparser.add_argument(
            "--ayah",
            action="extend",
            nargs="+",
            metavar="REF_OR_RANGE",
            help=(
                "One or more refs or same-surah ranges, for example "
                "100:1-11 or 1:1 1:2. May be repeated."
            ),
        )
        subparser.add_argument(
            "--analysis-id",
            default="native",
            help=(
                "Stable human-readable analysis namespace. 'native' preserves "
                "the default numbered-ayah evidence scope; a lone S:0 focus "
                "derives sNNN-basmala-full automatically."
            ),
        )
        subparser.add_argument(
            "--segment",
            action="append",
            default=[],
            metavar="ID=REFS",
            help=(
                "Ordered composition segment, for example "
                "fatiha=1:1-7. Repeat to define the full recitation sequence."
            ),
        )
        subparser.add_argument(
            "--analysis",
            type=Path,
            help="JSON composition file; its focus_refs are used when --ayah is omitted.",
        )
        subparser.add_argument(
            "--member-surah",
            type=int,
            help=(
                "Host surah for explicitly added context-only ayat. Focus refs "
                "must belong to this surah."
            ),
        )
        subparser.add_argument(
            "--add-ayat",
            "--add-member",
            dest="add_ayat",
            action="append",
            default=[],
            metavar="REF[,REF...]",
            help=(
                "Explicit comma-separated ayat to add as context-only members of "
                "--member-surah. Repeatable; ranges are not accepted. "
                "--add-member is a deprecated alias."
            ),
        )
        _source_options(subparser)
    verify_parser = subparsers.add_parser(
        "verify", help="Check lineage identity and the presence of all eight outputs."
    )
    verify_parser.add_argument(
        "--ayah",
        required=True,
        action="extend",
        nargs="+",
        metavar="REF_OR_RANGE",
    )
    verify_parser.add_argument("--analysis-id", default="native")
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        composition: compositions.Composition | None = None
        analysis_path = getattr(args, "analysis", None)
        segment_specs = getattr(args, "segment", [])
        added_ayat_specs = getattr(args, "add_ayat", [])
        member_surah = getattr(args, "member_surah", None)
        if analysis_path is not None and (member_surah is not None or added_ayat_specs):
            raise WorkflowError(
                "--analysis cannot be combined with --member-surah/--add-ayat"
            )
        if added_ayat_specs and member_surah is None:
            raise WorkflowError("--add-ayat requires --member-surah")
        if member_surah is not None and not added_ayat_specs:
            raise WorkflowError("--member-surah requires at least one --add-ayat")
        if member_surah is not None and not segment_specs:
            raise WorkflowError("--member-surah requires --segment definitions")
        if analysis_path is not None and segment_specs:
            raise WorkflowError("--analysis cannot be combined with --segment")
        if analysis_path is not None:
            try:
                composition = compositions.load_composition(analysis_path)
            except compositions.CompositionError as exc:
                raise WorkflowError(str(exc)) from exc
            if args.analysis_id not in {"native", composition.analysis_id}:
                raise WorkflowError("--analysis-id disagrees with the composition file")
            args.analysis_id = composition.analysis_id
            ayah_refs = (
                _expand_ayah_selectors(args.ayah)
                if args.ayah
                else list(composition.focus_refs)
            )
        elif segment_specs:
            if args.analysis_id == "native":
                raise WorkflowError("--segment requires a non-native --analysis-id")
            if not args.ayah:
                raise WorkflowError("--segment requires --ayah focus selectors")
            try:
                composition = compositions.composition_from_cli(
                    args.analysis_id,
                    segment_specs,
                    args.ayah,
                    member_surah=member_surah,
                    added_ayat_selectors=added_ayat_specs,
                )
            except compositions.CompositionError as exc:
                raise WorkflowError(str(exc)) from exc
            ayah_refs = list(composition.focus_refs)
        else:
            if not args.ayah:
                raise WorkflowError("--ayah is required without --analysis")
            ayah_refs = _expand_ayah_selectors(args.ayah)
        prefatory_focuses = [ref for ref in ayah_refs if _is_prefatory_ref(ref)]
        quran_evidence_for_policy: dict[str, dict[str, Any]] | None = None
        if (
            composition is None
            and args.analysis_id == "native"
            and prefatory_focuses
        ):
            if len(ayah_refs) != 1:
                raise WorkflowError(
                    "An implicit S:0 full-surah analysis must be invoked as a "
                    "single-focus command"
                )
            quran_evidence_for_policy, _coverage = _quran_text_projection(
                Path(getattr(args, "quran_text", v3.DEFAULT_QURAN_TEXT))
            )
            composition = _automatic_basmala_composition(
                prefatory_focuses[0], quran_evidence_for_policy
            )
            args.analysis_id = composition.analysis_id
        if composition is not None:
            outside = sorted(set(ayah_refs) - set(composition.focus_refs))
            if outside:
                raise WorkflowError(
                    f"Selected focuses are outside analysis {composition.analysis_id}: {outside}"
                )
            if any(_is_prefatory_ref(ref) for ref in composition.focus_refs):
                if quran_evidence_for_policy is None:
                    quran_evidence_for_policy, _coverage = _quran_text_projection(
                        Path(getattr(args, "quran_text", v3.DEFAULT_QURAN_TEXT))
                    )
                _validate_basmala_focus_context(
                    composition, quran_evidence_for_policy
                )
        args.composition = composition
        if len(ayah_refs) == 1:
            result = _execute_one(
                argparse.Namespace(**{**vars(args), "ayah": ayah_refs[0]})
            )
            has_errors = False
        else:
            result, has_errors = _batch_result(args, ayah_refs)
    except (WorkflowError, compositions.CompositionError, OSError, SystemExit) as exc:
        print(
            json.dumps(
                {
                    "schema_version": "commentary-v4-error-v1",
                    "status": "error",
                    "error": str(exc),
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
