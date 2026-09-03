#!/usr/bin/env python3
"""A fixed, Git-native two-stage commentary workflow."""

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


V5_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V5_ROOT.parents[1]
V3_ROOT = V5_ROOT.parent / "v3"
V3_PREPARE_PATH = V3_ROOT / "v3lib" / "prepare.py"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
V3_PROMPTS_ROOT = V3_ROOT / "prompts"
PROMPTS_ROOT = V5_ROOT / "prompts"
INPUT_ROOT = V5_ROOT / "input"
RAW_ROOT = V5_ROOT / "raw"
EDITORIAL_ROOT = V5_ROOT / "editorial"
LANES = ("micro", "macro", "global")
KINDS = ("prose", "evidence", "index", "friction")
LANE_RANK = {lane: index for index, lane in enumerate(LANES)}
MAX_JSON_BYTES = 128_000_000
MAX_LANE_PACKET_BYTES = 4_800_000
MAX_DISCOVERY_JSON_BYTES = 2_000_000
MAX_COMPOSITION_JSON_BYTES = 1_000_000
MAX_DISCOVERY_PROMPT_BYTES = 5_000_000
MAX_COMPOSITION_PROMPT_BYTES = 4_000_000
MAX_CANONICAL_PROMPT_BYTES = 4_000_000
MAX_EDITORIAL_PROMPT_BYTES = 512_000
MAX_SEMANTIC_RECORD_BYTES = 32_000
CANONICAL_OUTPUT_BYTE_LIMITS = {
    "prose": 512_000,
    "evidence": 512_000,
    "index": 768_000,
    "friction": 256_000,
}
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
QURAN_REF_IN_TEXT_RE = re.compile(
    r"(?<![0-9:])([1-9][0-9]*):(0|[1-9][0-9]*)"
    r"(?:-([1-9][0-9]*))?(?![0-9:])"
)
QURAN_COORDINATE_RE = re.compile(
    r"([1-9][0-9]*):(0|[1-9][0-9]*)(?::[1-9][0-9]*){1,2}"
)
LANDING_MAP_BLOCK_RE = re.compile(
    r"```commentary-v5-landing-map\s*\n(?P<payload>.*?)\n```",
    re.DOTALL,
)
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
sys.path.insert(0, str(V5_ROOT))
sys.path.insert(0, str(V3_ROOT))
sys.path.insert(0, str(SCRIPTS_ROOT))
sys.path.insert(0, str(REPO_ROOT))
from _commentary.v5 import composition as compositions  # noqa: E402
import pericope_bundle_manifest as pericope_manifests  # noqa: E402
import render_authoring as v3  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402
from v3lib.prepare import (  # noqa: E402
    PrepareOptions,
    build_prepared_artifacts,
    validate_docket,
)


V5_PREPARE_OPTIONS = PrepareOptions(
    hft_policy="quarantine",
    max_optional_candidates=80,
    max_support_chars=8_000,
)
UNIT_MANIFEST_SCHEMA_VERSION = "commentary-v5-unit-manifest-v1"
LANE_PACKET_SCHEMA_VERSION = "commentary-v5-lane-evidence-packet-v1"
SCOPE_DISCOVERY_SCHEMA_VERSION = "commentary-v5-scope-discovery-v1"
SCOPE_COMPOSITION_SCHEMA_VERSION = "commentary-v5-scope-composition-v1"
CANONICAL_LANDING_MAP_SCHEMA_VERSION = "commentary-v5-canonical-landing-map-v1"
FINDING_PROVENANCE_SCHEMA_VERSION = "commentary-v5-finding-provenance-v1"
MIN_LANDING_QUOTE_CHARS = 24
EPISTEMIC_STATUSES = frozenset({
    "grounded",
    "qualified",
    "exploratory",
})
BRANCH_APPLICATION_MODES = frozenset({
    "lexical",
    "intrinsic_cross_root",
    "contextual_resonance",
    "analogical",
    "attributed",
})
INTERNAL_PROSE_ID_RE = re.compile(
    r"(?:root_[0-9]+(?:/B[0-9]+)?|"
    r"\b[BF][0-9]{3,}\b|"
    r"(?:cand|sup|conn|conn_ev|hft)_[A-Za-z0-9_]+|"
    r"hft(?::[A-Za-z0-9._-]+)+|"
    r"(?:micro|macro|global):[A-Za-z0-9][A-Za-z0-9._-]*)"
)


class WorkflowError(RuntimeError):
    """Raised for a stale, mixed, or malformed v5 artifact set."""


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

    def discovery_prompt(self, lane: str) -> Path:
        return self.input / f"{lane}.discovery.prompt.md"

    def composition_prompt(self, lane: str) -> Path:
        return self.input / f"{lane}.composition.prompt.md"

    def scope_discovery(self, lane: str) -> Path:
        return self.raw / f"{lane}.discovery.json"

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


def _assert_byte_limit(payload: bytes, *, limit: int, label: str) -> None:
    if len(payload) > limit:
        raise WorkflowError(f"{label} exceeds {limit} bytes")


def _decode_json_object(
    payload: bytes, path: Path, *, max_bytes: int = MAX_JSON_BYTES
) -> dict[str, Any]:
    if len(payload) > max_bytes:
        raise WorkflowError(f"JSON artifact exceeds {max_bytes} bytes: {path}")
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise WorkflowError(f"Invalid JSON object in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise WorkflowError(f"Expected one JSON object in {path}")
    return value


def _load_json_with_bytes(
    path: Path, *, max_bytes: int = MAX_JSON_BYTES
) -> tuple[bytes, dict[str, Any]]:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read {path}: {exc}") from exc
    return payload, _decode_json_object(payload, path, max_bytes=max_bytes)


def _load_json(path: Path, *, max_bytes: int = MAX_JSON_BYTES) -> dict[str, Any]:
    return _load_json_with_bytes(path, max_bytes=max_bytes)[1]


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


def _source_path_record(path: Path) -> dict[str, Any]:
    resolved = path.resolve(strict=False)
    if not resolved.is_file() or resolved.is_symlink():
        raise WorkflowError(f"Provenance source is missing or not regular: {resolved}")
    try:
        payload = resolved.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read provenance source {resolved}: {exc}") from exc
    return {
        "path": _manifest_source_path(resolved),
        "bytes": len(payload),
        "sha256": _sha256(payload),
    }


def _resolve_manifest_source_path(value: Any, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise WorkflowError(f"Manifest {label} source path is missing or malformed")
    path = Path(value)
    if not path.is_absolute():
        path = PROJECTS_ROOT / path
    return path.resolve(strict=False)


def _verify_source_path_record(record: Any, *, label: str) -> tuple[Path, bytes]:
    if not isinstance(record, dict) or set(record) != {"path", "bytes", "sha256"}:
        raise WorkflowError(f"Manifest {label} provenance record is malformed")
    path = _resolve_manifest_source_path(record.get("path"), label=label)
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"Manifest {label} source is unavailable: {path}")
    payload = path.read_bytes()
    if record.get("bytes") != len(payload) or record.get("sha256") != _sha256(payload):
        raise WorkflowError(f"Manifest {label} source changed: {path}")
    return path, payload


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
        absolute_root.relative_to(V5_ROOT)
    except ValueError as exc:
        raise WorkflowError(f"{label} escapes its v5 artifact root: {path}") from exc

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
        raise WorkflowError(f"{label} resolves outside its v5 artifact root") from exc


def _assert_layout(layout: Layout) -> None:
    if layout != layout_for(layout.ayah_ref, layout.analysis_id):
        raise WorkflowError("Unit layout does not match the fixed v5 paths")
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
            options=V5_PREPARE_OPTIONS,
        )
    except ValidationError as exc:
        raise WorkflowError(
            f"Cannot derive the V5 docket from {source_origin}: {exc}"
        ) from exc
    return docket, {
        "kind": "derived_in_memory",
        "implementation": _path_record(V3_PREPARE_PATH),
        "source": _source_path_record(source_origin),
        "prepare_options": asdict(V5_PREPARE_OPTIONS),
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
            "source": _source_path_record(docket_origin),
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


def _quran_ref_sort_key(ref: str) -> tuple[int, int]:
    surah, ayah = ref.split(":", 1)
    return int(surah), int(ayah)


def _canonical_extracted_ref(surah: int, ayah: int) -> str | None:
    if not 1 <= surah <= len(QURAN_AYAH_COUNTS):
        return None
    if ayah == 0:
        if surah in compositions.BASMALA_EXCLUDED_SURAHS:
            return None
    elif not 1 <= ayah <= QURAN_AYAH_COUNTS[surah - 1]:
        return None
    return f"{surah}:{ayah}"


def _coordinate_ayah_ref(value: str) -> str | None:
    match = QURAN_COORDINATE_RE.fullmatch(value)
    if match is None:
        return None
    return _canonical_extracted_ref(int(match.group(1)), int(match.group(2)))


def _extract_quran_refs(value: Any) -> list[str]:
    """Extract canonical ayah refs, including refs inside serialized JSON text."""
    refs: set[str] = set()

    def add_range(surah_text: str, first_text: str, last_text: str | None) -> None:
        surah = int(surah_text)
        first = int(first_text)
        last = int(last_text or first_text)
        if (
            last < first
            or _canonical_extracted_ref(surah, first) is None
            or _canonical_extracted_ref(surah, last) is None
        ):
            return
        for ayah in range(first, last + 1):
            ref = _canonical_extracted_ref(surah, ayah)
            if ref is not None:
                refs.add(ref)

    def visit(item: Any) -> None:
        if isinstance(item, str):
            stripped = item.strip()
            coordinate_ref = _coordinate_ayah_ref(stripped)
            if coordinate_ref is not None:
                refs.add(coordinate_ref)
            if stripped.startswith(("{", "[")):
                try:
                    decoded = json.loads(stripped)
                except json.JSONDecodeError:
                    decoded = None
                if isinstance(decoded, (dict, list)):
                    visit(decoded)
                    return
            for match in QURAN_COORDINATE_RE.finditer(item):
                coordinate_ref = _canonical_extracted_ref(
                    int(match.group(1)), int(match.group(2))
                )
                if coordinate_ref is not None:
                    refs.add(coordinate_ref)
            for match in QURAN_REF_IN_TEXT_RE.finditer(item):
                add_range(*match.groups())
            return
        if isinstance(item, list):
            for child in item:
                visit(child)
            return
        if isinstance(item, dict):
            for key, child in item.items():
                visit(key)
                visit(child)

    visit(value)
    return sorted(refs, key=_quran_ref_sort_key)


def _context_refs_for_support(
    support: dict[str, Any],
    *,
    focus_ref: str,
    linguistic_source_ref: str,
) -> tuple[list[str], list[str]]:
    source = {
        key: value
        for key, value in support.items()
        if key not in {"quran_refs", "context_refs"}
    }
    quran_refs = set(_extract_quran_refs(source))
    quran_refs.update(_extract_quran_refs(support.get("quran_refs", [])))
    explicit_context = {
        ref
        for ref in support.get("context_refs", [])
        if isinstance(ref, str) and compositions.REF_RE.fullmatch(ref) is not None
    }
    quran_refs.update(explicit_context)
    context_refs = quran_refs - {focus_ref}
    payload = support.get("payload")
    if isinstance(payload, dict):
        payload_surface_ref = payload.get("surface_ref")
        payload_linguistic_ref = payload.get("linguistic_source_ref")
        if (
            isinstance(payload_surface_ref, str)
            and payload_surface_ref in explicit_context
            and isinstance(payload_linguistic_ref, str)
            and payload_linguistic_ref != payload_surface_ref
            and payload_linguistic_ref not in explicit_context
        ):
            context_refs.discard(payload_linguistic_ref)
    if linguistic_source_ref != focus_ref:
        context_refs.discard(linguistic_source_ref)
        context_refs.update(
            explicit_context - {focus_ref, linguistic_source_ref}
        )
    return (
        sorted(quran_refs, key=_quran_ref_sort_key),
        sorted(context_refs, key=_quran_ref_sort_key),
    )


def _candidate_is_context_member(candidate: dict[str, Any]) -> bool:
    return candidate.get("source_type") in {
        "external_ayah_member",
        "automatic_prefatory_basmala_surah_member",
    } or candidate.get("membership_added_ayah") is True


def _candidate_specific_supports(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    support_ids = candidate.get("support_ids", [])
    supports = [
        support_map[support_id]
        for support_id in support_ids
        if isinstance(support_id, str) and support_id in support_map
    ]
    return supports


def _candidate_required_context_refs(
    candidate: dict[str, Any],
    support_map: dict[str, dict[str, Any]],
    *,
    focus_ref: str,
    linguistic_source_ref: str,
) -> list[str]:
    refs: set[str] = set()
    for anchor in candidate.get("anchor_refs", []):
        if not isinstance(anchor, str):
            continue
        coordinate_ref = _coordinate_ayah_ref(anchor)
        if coordinate_ref is not None:
            refs.add(coordinate_ref)
        refs.update(_extract_quran_refs(anchor))
    for support in _candidate_specific_supports(candidate, support_map):
        refs.update(support.get("context_refs", []))
    refs.discard(focus_ref)
    if (
        linguistic_source_ref != focus_ref
        and not _candidate_is_context_member(candidate)
    ):
        refs.discard(linguistic_source_ref)
    return sorted(refs, key=_quran_ref_sort_key)


ROOT_DISPLAY_RE = re.compile(r"\{\{ar:([^}]+)\}\}")


def _candidate_source_roots(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> set[str]:
    roots: set[str] = set()
    for support in _candidate_specific_supports(candidate, support_map):
        text = support.get("text")
        if not isinstance(text, str):
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(payload, dict):
            continue
        root_display = payload.get("root_display")
        if not isinstance(root_display, str):
            continue
        match = ROOT_DISPLAY_RE.search(root_display)
        if match is not None:
            roots.update(
                " ".join(part.split())
                for part in match.group(1).split("/")
                if part.strip()
            )
    return roots


def _normalize_word_analysis_root_ids(
    candidate: dict[str, Any],
    support_map: dict[str, dict[str, Any]],
    branch_map: dict[str, dict[str, Any]],
) -> None:
    """Expose exact source/QAC root identity without nominating a branch."""
    if candidate.get("source_type") != "word_analysis":
        return
    existing = candidate.get("root_ids")
    if isinstance(existing, list) and existing:
        return
    source_roots = _candidate_source_roots(candidate, support_map)
    if not source_roots:
        return
    candidate["root_ids"] = sorted({
        str(branch.get("root_id"))
        for branch in branch_map.values()
        if branch.get("root_ar") in source_roots
        and isinstance(branch.get("root_id"), str)
    })


def _candidate_semantic_obligations(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Name candidate-authored semantics so a decision cannot drop them silently."""
    obligations: list[dict[str, Any]] = []
    candidate_id = candidate.get("candidate_id")
    candidate_supports = _candidate_specific_supports(candidate, support_map)

    def append_obligation(
        support_id: str, kind: str, payload: dict[str, Any]
    ) -> None:
        body = {
            "candidate_id": candidate_id,
            "support_id": support_id,
            "kind": kind,
            **payload,
        }
        obligation = {
            "obligation_ref": "obl_" + v3._sha256_json(body)[:20],
            "support_id": support_id,
            "kind": kind,
            **copy.deepcopy(payload),
        }
        if obligation not in obligations:
            obligations.append(obligation)

    for support in candidate_supports:
        semantic_claim = support.get("text")
        support_id = support.get("support_id")
        support_role = support.get("role")
        if (
            isinstance(semantic_claim, str)
            and semantic_claim.strip()
            and isinstance(support_id, str)
            and support_role not in {
                "context_only",
                "context_unit_native_depth_evidence",
                "focus_occurrence",
                "source_semantic_image",
            }
        ):
            append_obligation(
                support_id,
                (
                    "candidate_evidence"
                    if support_role == "candidate_evidence"
                    else "candidate_support_text"
                ),
                {
                    "support_role": support_role,
                    "semantic_claim": semantic_claim,
                },
            )

    for support in candidate_supports:
        payload = support.get("payload")
        support_id = support.get("support_id")
        if not isinstance(support_id, str):
            continue
        if (
            support.get("source_type") == "hft"
            and isinstance(payload, str)
            and payload.strip()
        ):
            append_obligation(
                support_id,
                "hft_claim",
                {"semantic_claim": payload},
            )
            continue
        if not isinstance(payload, dict):
            continue
        trace = payload.get("activation_trace")
        if isinstance(trace, list):
            for index, row in enumerate(trace):
                if not isinstance(row, dict):
                    continue
                append_obligation(
                    support_id,
                    "activation_trace",
                    {
                        "trace_index": index,
                        "branch_ref": _trace_row_branch_ref(row),
                        "source_ref": row.get("source_ref"),
                        "source_word_indices": copy.deepcopy(
                            row.get("source_word_indices", [])
                        ),
                        "semantic_claim": row.get("role"),
                    },
                )
        changed = payload.get("changed_reading")
        if isinstance(changed, dict) and (
            isinstance(changed.get("before"), str)
            or isinstance(changed.get("after"), str)
        ):
            append_obligation(
                support_id,
                "changed_reading",
                {
                    "before": changed.get("before"),
                    "after": changed.get("after"),
                },
            )
        for field in ("mechanism", "reader_inference", "containment"):
            value = payload.get(field)
            if isinstance(value, str) and value.strip():
                append_obligation(
                    support_id,
                    field,
                    {"semantic_claim": value},
                )
        structural_cues = payload.get("structural_cues")
        if isinstance(structural_cues, list):
            for index, cue in enumerate(structural_cues):
                if isinstance(cue, str) and cue.strip():
                    append_obligation(
                        support_id,
                        "structural_cue",
                        {"cue_index": index, "semantic_claim": cue},
                    )
        if support.get("role") == "surah_conditioned_prefatory_evidence":
            for field in sorted(payload):
                value = payload[field]
                if field == "not_applicable_states" or value in (None, {}, [], ""):
                    continue
                append_obligation(
                    support_id,
                    "prefatory_evidence_section",
                    {"section": field, "semantic_payload": value},
                )
    return obligations


def _widest_lane_for_refs(
    refs: list[str], *, focus_ref: str, default_lane: str
) -> str:
    focus_surah = focus_ref.split(":", 1)[0]
    inferred = default_lane
    if refs:
        inferred = (
            "global"
            if any(ref.split(":", 1)[0] != focus_surah for ref in refs)
            else "macro"
        )
    return max((default_lane, inferred), key=LANE_RANK.__getitem__)


def _branch_review_pairs(branches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for branch in branches:
        branch_ref = branch.get("branch_ref")
        facets = branch.get("review_facets")
        if isinstance(facets, list) and facets:
            for facet in facets:
                if not isinstance(facet, dict):
                    raise WorkflowError(
                        f"Branch {branch_ref} contains a malformed review facet"
                    )
                facet_id = facet.get("facet_id")
                if not isinstance(facet_id, str) or not facet_id:
                    raise WorkflowError(
                        f"Branch {branch_ref} contains a facet without an ID"
                    )
                pairs.append({"branch_ref": branch_ref, "facet_id": facet_id})
        else:
            pairs.append({"branch_ref": branch_ref, "facet_id": None})
    return pairs


def _required_candidate_branch_facets(
    candidate: dict[str, Any], branch_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    required = candidate.get("nominated_branch_facets", [])
    if not isinstance(required, list):
        return []
    normalized: list[dict[str, Any]] = []
    for row in required:
        if not isinstance(row, dict):
            continue
        branch_ref = row.get("branch_ref")
        facet_id = row.get("facet_id")
        branch = branch_map.get(branch_ref)
        if branch is None:
            continue
        if {"branch_ref": branch_ref, "facet_id": facet_id} in (
            _branch_review_pairs([branch])
        ):
            normalized.append({"branch_ref": branch_ref, "facet_id": facet_id})
    return normalized


def _candidate_root_branch_options(
    candidate: dict[str, Any], branch_map: dict[str, dict[str, Any]]
) -> list[str]:
    """Index focus branches for a word candidate without nominating them."""
    if candidate.get("source_type") != "word_analysis":
        return []
    root_ids = candidate.get("root_ids")
    if not isinstance(root_ids, list):
        return []
    root_id_set = {root_id for root_id in root_ids if isinstance(root_id, str)}
    return sorted(
        branch_ref
        for branch_ref, branch in branch_map.items()
        if branch.get("registry") == "focus"
        and branch.get("root_id") in root_id_set
    )


def _focus_surface_refs(packet: dict[str, Any]) -> list[str]:
    focus_surface = packet.get("focus_surface_evidence")
    if not isinstance(focus_surface, dict):
        return []
    refs = focus_surface.get("word_analysis_refs")
    if isinstance(refs, list) and all(
        isinstance(ref, str) and ref for ref in refs
    ):
        return list(dict.fromkeys(refs))
    qac_refs = [
        row.get("qac_word_ref")
        for row in focus_surface.get("qac_morphemes", [])
        if isinstance(row, dict) and isinstance(row.get("qac_word_ref"), str)
    ]
    return list(dict.fromkeys(qac_refs))


def _connection_evidence_refs(connection: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    own_ref = connection.get("connection_evidence_ref")
    if isinstance(own_ref, str) and own_ref:
        refs.append(own_ref)
    reciprocal = connection.get("reciprocal_evidence")
    if isinstance(reciprocal, list):
        refs.extend(
            row["connection_evidence_ref"]
            for row in reciprocal
            if isinstance(row, dict)
            and isinstance(row.get("connection_evidence_ref"), str)
            and row["connection_evidence_ref"]
        )
    if len(refs) != len(set(refs)):
        raise WorkflowError(
            f"Connection {connection.get('connection_ref')} has duplicate evidence refs"
        )
    return refs


def _context_branch_descriptor(
    bundle: dict[str, Any], branch_ref: str
) -> dict[str, Any] | None:
    root_id = branch_ref.split("/", 1)[0]
    root_lexicon = bundle.get("root_lexicon")
    if not isinstance(root_lexicon, dict):
        return None
    root_record = root_lexicon.get(root_id)
    if not isinstance(root_record, dict):
        return None
    dictionary = root_record.get("dictionary_entry")
    if not isinstance(dictionary, dict):
        return None
    source_branches = dictionary.get("branches")
    if not isinstance(source_branches, list):
        return None
    matching = [
        (index, branch)
        for index, branch in enumerate(source_branches)
        if isinstance(branch, dict) and branch.get("branch_ref") == branch_ref
    ]
    if len(matching) != 1:
        return None
    branch_index, source_branch = matching[0]
    semantic_detail = v3._branch_semantic_detail(source_branch)
    try:
        review_facets = v3._branch_review_facets(semantic_detail)
    except SystemExit as exc:
        raise WorkflowError(
            f"Context branch {branch_ref} has malformed semantic facets"
        ) from exc
    concept_gloss = source_branch.get("concept_gloss")
    gloss = (
        concept_gloss.get("text") if isinstance(concept_gloss, dict) else None
    )
    identity = source_branch.get("identity_judgment")
    lexicalization = source_branch.get("lexicalization_scope")
    qac_roots = {
        v3._normalized_ar(root)
        for root in root_record.get("qac_roots_ar", [])
        if isinstance(root, str)
    }
    context_occurrences = [
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
        for morpheme in bundle.get("qac_morphemes", [])
        if isinstance(morpheme, dict)
        and v3._normalized_ar(morpheme.get("root_ar")) in qac_roots
    ]
    return {
        "branch_ref": branch_ref,
        "registry": "context",
        "root_id": root_id,
        "root_ar": root_record.get("root_ar"),
        "lexicon_identity_status": (
            identity.get("status") if isinstance(identity, dict) else None
        ),
        "branch_kind": (
            lexicalization.get("branch_kind")
            if isinstance(lexicalization, dict)
            else None
        ),
        "gloss": gloss,
        "boundary": (
            identity.get("boundary_note") if isinstance(identity, dict) else None
        ),
        "source_pointer": (
            f"/root_lexicon/{root_id}/dictionary_entry/branches/{branch_index}"
        ),
        "semantic_detail": semantic_detail,
        "review_facets": review_facets,
        "focus_root_occurrences": [],
        "context_root_occurrences": context_occurrences,
        "root_occurrence_qualification": (
            "These are occurrences in the cited context unit, not the focus. "
            "A finding must still name its independent trigger and focus return."
        ),
    }


_CONTEXT_BRANCH_SEMANTIC_FIELDS = (
    "branch_ref",
    "registry",
    "root_id",
    "root_ar",
    "lexicon_identity_status",
    "branch_kind",
    "gloss",
    "boundary",
    "semantic_detail",
    "review_facets",
    "focus_root_occurrences",
)


def _combined_context_branch_descriptor(
    sources: list[tuple[str, dict[str, Any]]], branch_ref: str
) -> dict[str, Any] | None:
    """Combine one branch's exact occurrences across its cited context units."""
    descriptors: list[tuple[str, dict[str, Any]]] = []
    for context_ref, bundle in sorted(sources, key=lambda row: _quran_ref_sort_key(row[0])):
        descriptor = _context_branch_descriptor(bundle, branch_ref)
        if descriptor is None or not descriptor["context_root_occurrences"]:
            continue
        descriptors.append((context_ref, descriptor))
    if not descriptors:
        return None

    first_ref, first = descriptors[0]
    first_semantics = {
        field: first.get(field) for field in _CONTEXT_BRANCH_SEMANTIC_FIELDS
    }
    for context_ref, descriptor in descriptors[1:]:
        semantics = {
            field: descriptor.get(field)
            for field in _CONTEXT_BRANCH_SEMANTIC_FIELDS
        }
        if semantics != first_semantics:
            raise WorkflowError(
                f"Context branch semantics differ between {first_ref} and "
                f"{context_ref}: {branch_ref}"
            )

    combined = copy.deepcopy(first)
    combined.pop("source_pointer", None)
    combined["context_source_refs"] = [ref for ref, _ in descriptors]
    combined["context_source_pointers"] = {
        ref: descriptor["source_pointer"] for ref, descriptor in descriptors
    }
    combined["context_root_occurrence_refs_by_source"] = {
        ref: list(dict.fromkeys(
            occurrence[field]
            for occurrence in descriptor["context_root_occurrences"]
            for field in ("qac_ref", "qac_word_ref")
            if isinstance(occurrence.get(field), str) and occurrence[field]
        ))
        for ref, descriptor in descriptors
    }
    occurrences: list[dict[str, Any]] = []
    seen_occurrences: set[str] = set()
    for _context_ref, descriptor in descriptors:
        for occurrence in descriptor["context_root_occurrences"]:
            key = v3._canonical_json(occurrence)
            if key in seen_occurrences:
                continue
            seen_occurrences.add(key)
            occurrences.append(copy.deepcopy(occurrence))
    combined["context_root_occurrences"] = occurrences
    combined["root_occurrence_qualification"] = (
        "These are exact occurrences in the branch-linked context units, not "
        "the focus. A finding must still name an independent trigger and an "
        "exact focus-surface return."
    )
    return combined


def _trace_row_branch_ref(row: dict[str, Any]) -> str | None:
    direct = row.get("branch_ref")
    if isinstance(direct, str) and direct:
        return direct
    root_id = row.get("mapped_root_id")
    branch_id = row.get("branch_id")
    if isinstance(root_id, str) and isinstance(branch_id, str):
        return f"{root_id}/{branch_id}"
    return None


def _candidate_branch_context_refs(
    candidate: dict[str, Any],
    branch_ref: str,
    support_map: dict[str, dict[str, Any]],
    branch: dict[str, Any] | None,
    *,
    focus_ref: str,
    linguistic_source_ref: str,
) -> tuple[list[str], bool]:
    """Return context refs explicitly attached to this candidate/branch pair."""
    refs: set[str] = set()
    matched_branch_evidence = False
    candidate_hft_ref = candidate.get("hft_ref")
    if isinstance(branch, dict) and isinstance(candidate_hft_ref, str):
        for citation in branch.get("hft_citations", []):
            if (
                isinstance(citation, dict)
                and citation.get("hft_ref") == candidate_hft_ref
            ):
                matched_branch_evidence = True
                refs.update(_extract_quran_refs(citation.get("source_ref")))

    def visit(item: Any) -> None:
        nonlocal matched_branch_evidence
        if isinstance(item, list):
            for child in item:
                visit(child)
            return
        if not isinstance(item, dict):
            return
        if _trace_row_branch_ref(item) == branch_ref:
            matched_branch_evidence = True
            for field in ("source_ref", "ayah_ref", "context_ref"):
                refs.update(_extract_quran_refs(item.get(field)))
        for child in item.values():
            if isinstance(child, (dict, list)):
                visit(child)

    for support in _candidate_specific_supports(candidate, support_map):
        visit(support)

    refs.discard(focus_ref)
    if linguistic_source_ref != focus_ref:
        refs.discard(linguistic_source_ref)
    return sorted(refs, key=_quran_ref_sort_key), matched_branch_evidence


def _optional_context_bundle(
    ref: str,
    *,
    package_bundle_root: Path,
    member_bundle_root: Path,
    loaded: dict[str, tuple[Path, dict[str, Any], dict[str, Any]]],
) -> tuple[Path, dict[str, Any], dict[str, Any]] | None:
    if ref in loaded:
        return loaded[ref]
    package_present = _bundle_path_is_present(package_bundle_root, ref)
    same_root = (
        package_bundle_root.resolve(strict=False)
        == member_bundle_root.resolve(strict=False)
    )
    member_present = package_present if same_root else _bundle_path_is_present(
        member_bundle_root, ref
    )
    if not package_present and not member_present:
        return None
    value = _load_added_ayah_bundle(
        package_bundle_root, member_bundle_root, ref
    )
    loaded[ref] = value
    return value


def _auxiliary_context_source_record(
    ref: str, loaded: tuple[Path, dict[str, Any], dict[str, Any]]
) -> dict[str, Any]:
    path, bundle, identity = loaded
    payload = path.read_bytes()
    return {
        "ayah_ref": ref,
        "source_file": _manifest_source_path(path),
        "bytes": len(payload),
        "sha256": _sha256(payload),
        "canonical_sha256": identity["canonical_sha256"],
        "schema_version": identity["schema_version"],
        "unit_kind": identity["unit_kind"],
    }


def _merge_branch_record(
    current: dict[str, Any] | None,
    addition: dict[str, Any],
) -> dict[str, Any]:
    """Merge lane-local branch links without allowing semantic drift."""
    if current is None:
        return copy.deepcopy(addition)
    dynamic_fields = {"candidate_links", "support_links", "hft_citations"}
    current_semantics = {
        key: value for key, value in current.items() if key not in dynamic_fields
    }
    addition_semantics = {
        key: value for key, value in addition.items() if key not in dynamic_fields
    }
    if current_semantics != addition_semantics:
        raise WorkflowError(
            f"Branch semantics differ across lanes: {addition.get('branch_ref')}"
        )
    merged = copy.deepcopy(current)
    for field in dynamic_fields:
        values: list[Any] = []
        seen: set[str] = set()
        for source in (current, addition):
            rows = source.get(field, [])
            if rows is None:
                rows = []
            if not isinstance(rows, list):
                raise WorkflowError(
                    f"Branch {addition.get('branch_ref')} has malformed {field}"
                )
            for row in rows:
                key = v3._canonical_json(row)
                if key in seen:
                    continue
                seen.add(key)
                values.append(copy.deepcopy(row))
        if values or field in current or field in addition:
            merged[field] = values
    return merged


def _normalize_and_route_lane_packets(
    packets: dict[str, dict[str, Any]],
    source_bundle: dict[str, Any],
    *,
    package_bundle_root: Path,
    member_bundle_root: Path,
    preloaded_context: dict[
        str, tuple[Path, dict[str, Any], dict[str, Any]]
    ] | None = None,
) -> dict[str, dict[str, Any]]:
    """Bind Quran refs to supports/candidates and route wider evidence once."""
    focus_ref = str(source_bundle["ayahRef"])
    linguistic_source_ref = str(
        source_bundle.get("linguistic_source_ref", focus_ref)
    )
    support_map: dict[str, dict[str, Any]] = {}
    support_order: list[str] = []
    support_source_lanes: dict[str, set[str]] = {}
    branch_map: dict[str, dict[str, Any]] = {}
    branch_context_refs: dict[tuple[str, str], set[str]] = {}
    hydrated_branches: dict[str, dict[str, dict[str, Any]]] = {
        lane: {} for lane in LANES
    }
    hydrated_sources: dict[str, dict[str, Any]] = {}
    loaded_context = dict(preloaded_context or {})
    routed_candidates: dict[str, list[dict[str, Any]]] = {
        lane: [] for lane in LANES
    }

    def candidate_branch_bindings(
        candidate: dict[str, Any],
        base_context_refs: list[str],
    ) -> dict[str, list[str]]:
        bindings: dict[str, list[str]] = {}
        for branch_ref in candidate.get("branch_refs", []):
            if not isinstance(branch_ref, str) or not branch_ref:
                continue
            exact_refs, has_branch_binding = _candidate_branch_context_refs(
                candidate,
                branch_ref,
                support_map,
                branch_map.get(branch_ref),
                focus_ref=focus_ref,
                linguistic_source_ref=linguistic_source_ref,
            )
            if not exact_refs and not has_branch_binding and len(base_context_refs) == 1:
                exact_refs = list(base_context_refs)
            bindings[branch_ref] = exact_refs
        return bindings

    def register_branch_bindings(
        bindings: dict[str, list[str]], target_lane: str
    ) -> None:
        for branch_ref, exact_refs in bindings.items():
            if exact_refs:
                branch_context_refs.setdefault((target_lane, branch_ref), set()).update(
                    exact_refs
                )

    for lane in LANES:
        packet = packets[lane]
        for raw_support in packet.get("support_registry", []):
            if not isinstance(raw_support, dict):
                raise WorkflowError(f"{lane} packet contains a malformed support")
            support = copy.deepcopy(raw_support)
            support_id = support.get("support_id")
            if not isinstance(support_id, str) or not support_id:
                raise WorkflowError(f"{lane} packet contains a support without an ID")
            quran_refs, context_refs = _context_refs_for_support(
                support,
                focus_ref=focus_ref,
                linguistic_source_ref=linguistic_source_ref,
            )
            support["quran_refs"] = quran_refs
            support["context_refs"] = context_refs
            current = support_map.get(support_id)
            if current is not None and current != support:
                raise WorkflowError(f"Support ID differs across lanes: {support_id}")
            if current is None:
                support_map[support_id] = support
                support_order.append(support_id)
            support_source_lanes.setdefault(support_id, set()).add(lane)
        for branch in packet.get("branch_registry", []):
            if not isinstance(branch, dict):
                raise WorkflowError(f"{lane} packet contains a malformed branch")
            branch_ref = branch.get("branch_ref")
            if not isinstance(branch_ref, str) or not branch_ref:
                raise WorkflowError(f"{lane} packet contains a branch without a ref")
            branch_map[branch_ref] = _merge_branch_record(
                branch_map.get(branch_ref), branch
            )

    for source_lane in LANES:
        for raw_candidate in packets[source_lane].get("candidate_inventory", []):
            if not isinstance(raw_candidate, dict):
                raise WorkflowError(
                    f"{source_lane} packet contains a malformed candidate"
                )
            candidate = copy.deepcopy(raw_candidate)
            _normalize_word_analysis_root_ids(candidate, support_map, branch_map)
            candidate["semantic_obligations"] = _candidate_semantic_obligations(
                candidate, support_map
            )
            candidate["required_branch_facets"] = (
                _required_candidate_branch_facets(candidate, branch_map)
            )
            base_context_refs = _candidate_required_context_refs(
                candidate,
                support_map,
                focus_ref=focus_ref,
                linguistic_source_ref=linguistic_source_ref,
            )
            branch_bindings = candidate_branch_bindings(
                candidate, base_context_refs
            )
            provisional_branch_refs = {
                ref for refs in branch_bindings.values() for ref in refs
            }
            required_context_refs = sorted(
                set(base_context_refs) | provisional_branch_refs,
                key=_quran_ref_sort_key,
            )
            if _candidate_is_context_member(candidate):
                target_lane = "macro"
                routing_basis = "explicit_host_context_membership"
            else:
                target_lane = _widest_lane_for_refs(
                    required_context_refs,
                    focus_ref=focus_ref,
                    default_lane=source_lane,
                )
                routing_basis = (
                    "wider_quran_reference"
                    if target_lane == "global" and source_lane != "global"
                    else (
                        "same_surah_quran_reference"
                        if target_lane == "macro" and source_lane == "micro"
                        else "upstream_lane"
                    )
                )
            retained_support_ids: list[str] = []
            for support_id in candidate.get("support_ids", []):
                if support_id not in support_map:
                    raise WorkflowError(
                        f"Candidate {candidate.get('candidate_id')} cites unknown "
                        f"support {support_id}"
                    )
                retained_support_ids.append(support_id)
            candidate["lane"] = target_lane
            candidate["support_ids"] = retained_support_ids
            candidate["required_context_refs"] = required_context_refs
            candidate["v5_routing"] = {
                "source_lane": source_lane,
                "resolved_lane": target_lane,
                "basis": routing_basis,
                "excluded_broader_support_ids": [],
            }
            candidate["branch_context_refs"] = branch_bindings
            register_branch_bindings(branch_bindings, target_lane)
            routed_candidates[target_lane].append(candidate)

    carried_support_context: dict[tuple[str, str], set[str]] = {}
    for lane in LANES:
        for candidate in routed_candidates[lane]:
            required = set(candidate["required_context_refs"])
            for support_id in candidate.get("support_ids", []):
                carried_support_context.setdefault((lane, support_id), set()).update(
                    required
                )
    for support_id in support_order:
        support = support_map[support_id]
        context_refs = support["context_refs"]
        if not context_refs:
            continue
        membership_support = support.get("qualification", {}).get(
            "host_surah_membership"
        ) is True or support.get("qualification", {}).get(
            "automatic_prefatory_basmala_membership"
        ) is True
        source_lane = min(
            support_source_lanes[support_id], key=LANE_RANK.__getitem__
        )
        target_lane = (
            "macro"
            if membership_support
            else _widest_lane_for_refs(
                context_refs, focus_ref=focus_ref, default_lane=source_lane
            )
        )
        if set(context_refs) <= carried_support_context.get(
            (target_lane, support_id), set()
        ):
            continue
        candidate_id = "cand_ref_" + v3._sha256_json({
            "focus_ref": focus_ref,
            "support_id": support_id,
            "context_refs": context_refs,
            "lane": target_lane,
        })[:20]
        probe = {
            "candidate_id": candidate_id,
            "ayah_ref": focus_ref,
            "lane": target_lane,
            "source_type": "support_quran_reference_probe",
            "source_local_id": support.get("source_local_id", support_id),
            "source_pointer": support.get(
                "json_pointer", f"/support_registry/{support_id}"
            ),
            "kind": "explicit_quran_reference_probe",
            "title": f"Explicit Quran reference in {support.get('source_local_id', support_id)}",
            "scope": "host_context" if target_lane == "macro" else "wider_record",
            "anchor_refs": context_refs,
            "branch_refs": support.get("branch_refs", []),
            "support_ids": [support_id],
            "required_context_refs": context_refs,
            "trust": support.get("trust", "unclassified"),
            "commentary_obligation": "review",
            "v5_routing": {
                "source_lane": source_lane,
                "resolved_lane": target_lane,
                "basis": "unrepresented_support_quran_reference",
                "excluded_broader_support_ids": [],
            },
        }
        probe["branch_context_refs"] = candidate_branch_bindings(
            probe, context_refs
        )
        probe["semantic_obligations"] = _candidate_semantic_obligations(
            probe, support_map
        )
        probe["required_branch_facets"] = _required_candidate_branch_facets(
            probe, branch_map
        )
        register_branch_bindings(probe["branch_context_refs"], target_lane)
        routed_candidates[target_lane].append(probe)

    for (target_lane, branch_ref), context_refs in branch_context_refs.items():
        existing = branch_map.get(branch_ref)
        if existing is None or (
            existing.get("lexicon_identity_status") != "unresolved"
            and existing.get("review_facets")
        ):
            continue
        branch_sources: list[tuple[str, dict[str, Any]]] = []
        branch_loaded: dict[
            str, tuple[Path, dict[str, Any], dict[str, Any]]
        ] = {}
        for context_ref in sorted(context_refs, key=_quran_ref_sort_key):
            loaded = _optional_context_bundle(
                context_ref,
                package_bundle_root=package_bundle_root,
                member_bundle_root=member_bundle_root,
                loaded=loaded_context,
            )
            if loaded is None:
                continue
            descriptor = _context_branch_descriptor(loaded[1], branch_ref)
            if descriptor is None or not descriptor["context_root_occurrences"]:
                continue
            branch_sources.append((context_ref, loaded[1]))
            branch_loaded[context_ref] = loaded
        descriptor = _combined_context_branch_descriptor(
            branch_sources, branch_ref
        )
        if descriptor is None:
            continue
        descriptor["candidate_links"] = copy.deepcopy(
            existing.get("candidate_links", []) if existing else []
        )
        descriptor["support_links"] = copy.deepcopy(
            existing.get("support_links", []) if existing else []
        )
        descriptor["hft_citations"] = copy.deepcopy(
            existing.get("hft_citations", []) if existing else []
        )
        source_records = {
            context_ref: _auxiliary_context_source_record(
                context_ref, branch_loaded[context_ref]
            )
            for context_ref in descriptor["context_source_refs"]
        }
        descriptor["context_source_canonical_sha256s"] = {
            context_ref: source_records[context_ref]["canonical_sha256"]
            for context_ref in descriptor["context_source_refs"]
        }
        hydrated_branches[target_lane][branch_ref] = descriptor
        hydrated_sources.update(source_records)

    all_candidate_ids: set[str] = set()
    for lane in LANES:
        packet = packets[lane]
        candidates = routed_candidates[lane]
        candidate_ids = [candidate.get("candidate_id") for candidate in candidates]
        if not all(isinstance(candidate_id, str) for candidate_id in candidate_ids):
            raise WorkflowError(f"{lane} packet contains a candidate without an ID")
        if len(candidate_ids) != len(set(candidate_ids)):
            raise WorkflowError(f"{lane} packet contains duplicate candidate IDs")
        duplicate_across_lanes = set(candidate_ids) & all_candidate_ids
        if duplicate_across_lanes:
            raise WorkflowError(
                f"Candidates are routed to multiple lanes: "
                f"{sorted(duplicate_across_lanes)}"
            )
        all_candidate_ids.update(candidate_ids)
        needed_support_ids = {
            support_id
            for candidate in candidates
            for support_id in candidate.get("support_ids", [])
        }
        supports: list[dict[str, Any]] = []
        for support_id in support_order:
            if support_id not in needed_support_ids:
                continue
            support = copy.deepcopy(support_map[support_id])
            if support.get("scope") != lane:
                support["upstream_scope"] = support.get("scope")
                support["scope"] = lane
            supports.append(support)
        available_support_ids = {support["support_id"] for support in supports}
        if needed_support_ids != available_support_ids:
            raise WorkflowError(f"{lane} packet lost candidate support records")

        candidate_id_set = set(candidate_ids)
        lane_hft_refs = {
            candidate.get("hft_ref")
            for candidate in candidates
            if isinstance(candidate.get("hft_ref"), str)
        }
        branch_refs = {
            branch.get("branch_ref")
            for branch in packet.get("branch_registry", [])
            if isinstance(branch, dict)
            and isinstance(branch.get("branch_ref"), str)
        }
        branch_refs.update(
            branch_ref
            for candidate in candidates
            for branch_ref in candidate.get("branch_refs", [])
        )
        branches: list[dict[str, Any]] = []
        for branch_ref in sorted(branch_refs):
            branch = copy.deepcopy(
                hydrated_branches[lane].get(branch_ref, branch_map.get(branch_ref))
            )
            if branch is None:
                raise WorkflowError(
                    f"{lane} routed candidate cites unavailable branch {branch_ref}"
                )
            links = branch.get("candidate_links")
            if isinstance(links, list):
                branch["candidate_links"] = [
                    {**link, "lane": lane}
                    for link in links
                    if isinstance(link, dict)
                    and link.get("candidate_id") in candidate_id_set
                ]
            links = branch.get("support_links")
            if isinstance(links, list):
                branch["support_links"] = [
                    support_id
                    for support_id in links
                    if support_id in available_support_ids
                ]
            citations = branch.get("hft_citations")
            if isinstance(citations, list):
                branch["hft_citations"] = [
                    citation
                    for citation in citations
                    if isinstance(citation, dict)
                    and citation.get("hft_ref") in lane_hft_refs
                ]
            branches.append(branch)

        final_branch_map = {
            branch["branch_ref"]: branch for branch in branches
        }
        for candidate in candidates:
            candidate["required_branch_facets"] = (
                _required_candidate_branch_facets(candidate, final_branch_map)
            )
            candidate["root_branch_options"] = _candidate_root_branch_options(
                candidate, final_branch_map
            )

        connections = packet.get("connection_registry", [])
        if not isinstance(connections, list) or not all(
            isinstance(connection, dict) for connection in connections
        ):
            raise WorkflowError(f"{lane} packet connection registry is malformed")
        connection_refs = [connection.get("connection_ref") for connection in connections]
        if not all(isinstance(ref, str) and ref for ref in connection_refs):
            raise WorkflowError(f"{lane} packet contains a connection without a ref")
        if len(connection_refs) != len(set(connection_refs)):
            raise WorkflowError(f"{lane} packet contains duplicate connection refs")
        context_refs = {
            ref
            for candidate in candidates
            for ref in candidate["required_context_refs"]
        }
        context_refs.update(
            str(unit.get("ayah_ref"))
            for unit in packet.get("selected_context_units", [])
            if isinstance(unit, dict) and isinstance(unit.get("ayah_ref"), str)
        )
        for connection in connections:
            context_refs.update(_extract_quran_refs(connection.get("target_ref")))
            context_refs.update(
                _extract_quran_refs(connection.get("source_target_components", []))
            )
        context_refs.discard(focus_ref)
        if linguistic_source_ref != focus_ref:
            context_refs.discard(linguistic_source_ref)

        packet["schema_version"] = LANE_PACKET_SCHEMA_VERSION
        packet["candidate_inventory"] = candidates
        packet["support_registry"] = supports
        packet["branch_registry"] = branches
        packet["auxiliary_context_sources"] = [
            hydrated_sources[context_ref]
            for branch in branches
            for context_ref in branch.get("context_source_refs", [])
            if context_ref in hydrated_sources
        ]
        packet["auxiliary_context_sources"] = list({
            record["ayah_ref"]: record
            for record in packet["auxiliary_context_sources"]
        }.values())
        packet["review_inventory"] = {
            "surface_refs": _focus_surface_refs(packet),
            "context_refs": sorted(context_refs, key=_quran_ref_sort_key),
            "support_ids": [support["support_id"] for support in supports],
            "connection_refs": connection_refs,
            "connection_evidence_refs": {
                connection["connection_ref"]: _connection_evidence_refs(connection)
                for connection in connections
            },
            "available_branch_facets": _branch_review_pairs(branches),
        }
        packet_contract = packet.setdefault("contract", {})
        packet_contract.pop("independent_discovery_audit_is_required", None)
        packet_contract.update({
            "candidate_context_refs_are_exact": True,
            "support_quran_refs_are_structured": True,
            "accepted_candidates_require_dedicated_findings": True,
            "independent_discovery_is_required": True,
            "candidate_semantics_require_explicit_accounting": True,
            "root_branch_options_are_non_nominating": True,
        })
        coverage = packet.get("source_coverage")
        if isinstance(coverage, dict):
            coverage["lane_candidate_count"] = len(candidates)
            coverage["lane_support_count"] = len(supports)
            coverage["lane_branch_count"] = len(branches)
        packet["identity"]["lane_packet_sha256"] = (
            v3._payload_hash_with_identity_field_removed(
                packet, "lane_packet_sha256"
            )
        )
        packet_bytes = len(_canonical_json_bytes(packet))
        if packet_bytes > MAX_LANE_PACKET_BYTES:
            raise WorkflowError(
                f"{lane} packet is {packet_bytes} bytes; context budget is "
                f"{MAX_LANE_PACKET_BYTES}. Reduce the composition explicitly."
            )
    return packets


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
    return {"by_lane": by_lane, "units": all_units, "loaded": loaded}


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


def _verify_added_ayah_root_agreement(
    analysis: dict[str, Any], selected_units: list[dict[str, Any]]
) -> None:
    added_units = [
        unit
        for unit in selected_units
        if isinstance(unit, dict) and unit.get("membership_added_ayah") is True
    ]
    if not added_units:
        return
    package_root = _resolve_manifest_source_path(
        analysis.get("context_bundles_dir"), label="context bundle root"
    )
    member_root = _resolve_manifest_source_path(
        analysis.get("member_bundles_dir"), label="member bundle root"
    )
    for unit in added_units:
        ref = str(unit.get("ayah_ref"))
        _path, _bundle, identity = _load_added_ayah_bundle(
            package_root, member_root, ref
        )
        if identity["canonical_sha256"] != unit.get("canonical_sha256"):
            raise WorkflowError(
                f"Added ayah {ref} no longer agrees with its manifest lineage"
            )


def _verify_analysis_bundle_roots(
    analysis: dict[str, Any], selected_units: list[dict[str, Any]]
) -> None:
    package_root = _resolve_manifest_source_path(
        analysis.get("context_bundles_dir"), label="context bundle root"
    )
    member_root = _resolve_manifest_source_path(
        analysis.get("member_bundles_dir"), label="member bundle root"
    )
    for unit in selected_units:
        ref = str(unit.get("ayah_ref"))
        source_file = unit.get("source_file")
        source_path = _resolve_manifest_source_path(
            source_file, label=f"selected context {ref}"
        )
        try:
            if unit.get("membership_added_ayah") is True:
                expected_path = _load_added_ayah_bundle(
                    package_root, member_root, ref
                )[0]
            elif _is_prefatory_ref(ref):
                expected_path = compositions.unit_bundle_path(member_root, ref)
            else:
                expected_path = compositions.unit_bundle_path(package_root, ref)
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        if source_path != expected_path.resolve(strict=False):
            raise WorkflowError(
                f"Analysis bundle roots do not resolve {ref} to its recorded source"
            )


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
    identity["source_sha256"] = _sha256(payload)
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
            "source_sha256",
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


def _build_discovery_prompt(
    layout: Layout,
    lane: str,
    packet: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    if lane not in LANES:
        raise WorkflowError(f"Unknown scope lane: {lane}")
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "discovery.md"
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
    request_sha256 = v3._request_sha256("v5-scope-discovery", request_inputs)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@LANE_PACKET_SHA256@@": packet["identity"][
                "lane_packet_sha256"
            ],
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@DISCOVERY_OUTPUT_PATH@@": _repo_path(
                layout.scope_discovery(lane)
            ),
            "@@SCOPE_DISCOVERY_SCHEMA_VERSION@@": (
                SCOPE_DISCOVERY_SCHEMA_VERSION
            ),
            "@@PRINCIPLES_MD@@": governing["principles"],
            "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
            "@@CHANNELS_MD@@": governing["channels"],
            "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
            "@@LANE_PACKET_JSON@@": v3._canonical_json(packet),
        },
        label=f"{lane} scope discovery",
    )
    _assert_byte_limit(
        prompt.encode("utf-8"),
        limit=MAX_DISCOVERY_PROMPT_BYTES,
        label=f"{lane} discovery prompt",
    )
    return prompt, {
        "request_sha256": request_sha256,
        "request_inputs": request_inputs,
        "response_schema_version": SCOPE_DISCOVERY_SCHEMA_VERSION,
        "template_source": _repo_path(template_path),
        "template_sha256": template_sha256,
    }


def _build_composition_prompt(
    layout: Layout,
    lane: str,
    packet: dict[str, Any],
    discovery: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    if lane not in LANES:
        raise WorkflowError(f"Unknown scope lane: {lane}")
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "composition.md"
    template = template_path.read_text(encoding="utf-8")
    template_sha256 = _sha256(template.encode("utf-8"))
    discovery_sha256 = v3._sha256_json(discovery)
    discovery_findings = {
        "ayah_ref": discovery["ayah_ref"],
        "lane": discovery["lane"],
        "findings": copy.deepcopy(discovery["findings"]),
        "friction_notes": copy.deepcopy(discovery["friction_notes"]),
    }
    discovery_findings_json = v3._canonical_json(discovery_findings)
    semantic_inventory = [
        {
            "finding_ref": finding["finding_ref"],
            "semantic_inventory": _finding_semantic_inventory(finding, packet),
        }
        for finding in discovery.get("findings", [])
    ]
    semantic_inventory_json = v3._canonical_json(semantic_inventory)
    semantic_requirements = [
        {
            "finding_ref": row["finding_ref"],
            "semantic_requirements": [
                _agent_semantic_requirement(item)
                for item in row["semantic_inventory"]
            ],
        }
        for row in semantic_inventory
    ]
    semantic_requirements_json = v3._canonical_json(semantic_requirements)
    governing_hashes = {
        f"{key}_sha256": _sha256(value.encode("utf-8"))
        for key, value in governing.items()
    }
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
        "discovery_sha256": discovery_sha256,
        "discovery_findings_sha256": _sha256(
            discovery_findings_json.encode("utf-8")
        ),
        "semantic_inventory_sha256": _sha256(
            semantic_inventory_json.encode("utf-8")
        ),
        "semantic_requirements_sha256": _sha256(
            semantic_requirements_json.encode("utf-8")
        ),
        "template_sha256": template_sha256,
        **governing_hashes,
    }
    request_sha256 = v3._request_sha256("v5-scope-composition", request_inputs)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@LANE_PACKET_SHA256@@": packet["identity"][
                "lane_packet_sha256"
            ],
            "@@DISCOVERY_SHA256@@": discovery_sha256,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@CONTRIBUTION_OUTPUT_PATH@@": _repo_path(
                layout.scope_contribution(lane)
            ),
            "@@SCOPE_COMPOSITION_SCHEMA_VERSION@@": (
                SCOPE_COMPOSITION_SCHEMA_VERSION
            ),
            "@@PRINCIPLES_MD@@": governing["principles"],
            "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
            "@@CHANNELS_MD@@": governing["channels"],
            "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
            "@@DISCOVERY_FINDINGS_JSON@@": discovery_findings_json,
            "@@SEMANTIC_REQUIREMENTS_JSON@@": semantic_requirements_json,
        },
        label=f"{lane} scope composition",
    )
    _assert_byte_limit(
        prompt.encode("utf-8"),
        limit=MAX_COMPOSITION_PROMPT_BYTES,
        label=f"{lane} composition prompt",
    )
    return prompt, {
        "request_sha256": request_sha256,
        "request_inputs": request_inputs,
        "response_schema_version": SCOPE_COMPOSITION_SCHEMA_VERSION,
        "template_source": _repo_path(template_path),
        "template_sha256": template_sha256,
        "discovery_sha256": discovery_sha256,
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
            "origin": _source_path_record(source_origin),
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
            "origin": _source_path_record(basmala_origin),
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

    packets: dict[str, dict[str, Any]] = {}
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
        packets[lane] = packet

    preloaded_context = (
        dict(composition_projection["loaded"])
        if composition_projection is not None
        else {}
    )
    if prefatory_basmala_packet_context is not None:
        preloaded_context[prefatory_basmala_packet_context[2]["ayah_ref"]] = (
            prefatory_basmala_packet_context
        )
    packets = _normalize_and_route_lane_packets(
        packets,
        source_bundle,
        package_bundle_root=context_bundles_dir,
        member_bundle_root=member_bundles_dir,
        preloaded_context=preloaded_context,
    )
    lane_records: dict[str, Any] = {}
    prefatory_basmala_context_units: list[dict[str, Any]] = []
    for lane in LANES:
        packet = packets[lane]
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
        prompt, discovery_record = _build_discovery_prompt(layout, lane, packet)
        _write_generated(
            layout.packet(lane),
            _canonical_json_bytes(packet, newline=True),
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
        _write_generated(
            layout.discovery_prompt(lane),
            prompt.encode("utf-8"),
            replace_changed=args.force_input,
            root=INPUT_ROOT,
        )
        lane_records[lane] = {
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "packet": _path_record(layout.packet(lane)),
            "discovery": {
                **discovery_record,
                "prompt": _path_record(layout.discovery_prompt(lane)),
                "expected_response": _repo_path(layout.scope_discovery(lane)),
            },
            "composition": None,
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
        previous_base = copy.deepcopy(previous)
        previous_base["canonical"] = None
        previous_base["editorial_turn"] = None
        for lane in LANES:
            lane_record = previous_base.get("lanes", {}).get(lane)
            if isinstance(lane_record, dict):
                lane_record["composition"] = None
        if previous_base == manifest:
            manifest["canonical"] = previous.get("canonical")
            manifest["editorial_turn"] = previous.get("editorial_turn")
            for lane in LANES:
                previous_lane = previous.get("lanes", {}).get(lane, {})
                if isinstance(previous_lane, dict):
                    manifest["lanes"][lane]["composition"] = (
                        previous_lane.get("composition")
                    )
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
        "schema_version": "commentary-v5-status-v1",
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
    if set(record) != {
        "snapshot",
        "origin",
        "canonical_sha256",
        "ayah_ref",
        "surface_ref",
        "linguistic_source_ref",
        "mode",
        "selected_context_units",
    }:
        raise WorkflowError("Manifest prefatory basmala record fields are malformed")
    snapshot_path = _verify_record(
        record.get("snapshot"),
        label="prefatory basmala snapshot",
        expected=layout.prefatory_basmala_bundle,
    )
    _origin_path, origin_payload = _verify_source_path_record(
        record.get("origin"), label="prefatory basmala origin"
    )
    if origin_payload != snapshot_path.read_bytes():
        raise WorkflowError(
            "Prefatory basmala origin no longer matches its fixed snapshot"
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


def _verify_docket_lineage(
    lineage: Any,
    *,
    source_origin: dict[str, Any],
    source_bundle: dict[str, Any],
    docket: dict[str, Any],
) -> None:
    if not isinstance(lineage, dict):
        raise WorkflowError("Manifest docket lineage is malformed")
    prefatory = source_bundle.get("unit_kind") == "prefatory_basmala"
    adapter = {
        "adapter": "prefatory_basmala_linguistic_alias_v1",
        "template_identity_adapter": "s0_bundle_as_positive_1_1_v1",
        "surface_ref": source_bundle.get("ayahRef"),
        "linguistic_source_ref": "1:1",
    }
    kind = lineage.get("kind")
    if kind == "derived_in_memory":
        expected_fields = {
            "kind", "implementation", "source", "prepare_options"
        } | (set(adapter) if prefatory else set())
        if set(lineage) != expected_fields:
            raise WorkflowError("Manifest derived docket lineage fields are stale")
        if lineage.get("source") != source_origin:
            raise WorkflowError("Manifest docket source lineage differs from focus origin")
        _verify_record(
            lineage.get("implementation"),
            label="docket preparation implementation",
            expected=V3_PREPARE_PATH,
        )
        if lineage.get("prepare_options") != asdict(V5_PREPARE_OPTIONS):
            raise WorkflowError("Manifest docket preparation options are stale")
    elif kind == "provided":
        expected_fields = {"kind", "source"} | (
            set(adapter) if prefatory else set()
        )
        if set(lineage) != expected_fields:
            raise WorkflowError("Manifest provided docket lineage fields are stale")
        _path, payload = _verify_source_path_record(
            lineage.get("source"), label="provided docket"
        )
        try:
            provided = json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise WorkflowError(f"Provided docket source is invalid JSON: {exc}") from exc
        expected_docket = (
            _adapt_basmala_docket(source_bundle, provided)
            if prefatory
            else provided
        )
        if expected_docket != docket:
            raise WorkflowError("Provided docket no longer matches its snapshot")
    else:
        raise WorkflowError(f"Manifest docket lineage kind is invalid: {kind!r}")
    if prefatory:
        if any(lineage.get(key) != value for key, value in adapter.items()):
            raise WorkflowError("Manifest basmala docket adapter lineage is stale")
    elif any(key in lineage for key in adapter):
        raise WorkflowError("Numbered docket carries basmala adapter lineage")


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
        raise WorkflowError("Unit manifest layout does not match the fixed v5 paths")
    try:
        source_record = manifest["source"]["snapshot"]
        docket_record = manifest["docket"]["snapshot"]
        context_package_record = manifest["context_package"]
        canonical_template = manifest["canonical_template"]
        editorial = manifest["editorial"]
    except (KeyError, TypeError) as exc:
        raise WorkflowError("Unit manifest is missing required records") from exc
    if set(manifest["source"]) != {"snapshot", "origin", "canonical_sha256"}:
        raise WorkflowError("Manifest source record fields are malformed")
    if set(manifest["docket"]) != {"snapshot", "origin", "payload_sha256"}:
        raise WorkflowError("Manifest docket record fields are malformed")
    source_path = _verify_record(
        source_record,
        label="source snapshot",
        expected=layout.source_bundle,
    )
    _source_origin_path, source_origin_payload = _verify_source_path_record(
        manifest["source"].get("origin"), label="focus bundle origin"
    )
    if source_origin_payload != source_path.read_bytes():
        raise WorkflowError("Focus bundle origin no longer matches its snapshot")
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
    _verify_docket_lineage(
        manifest["docket"].get("origin"),
        source_origin=manifest["source"]["origin"],
        source_bundle=source_bundle,
        docket=docket,
    )
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
        if (
            set(analysis) != {
                "mode",
                "analysis_id",
                "composition",
                "context_bundles_dir",
                "member_bundles_dir",
                "selected_context_units",
            }
            or analysis.get("mode") != "native"
            or analysis.get("composition") is not None
            or analysis.get("context_bundles_dir") is not None
            or analysis.get("member_bundles_dir") is not None
        ):
            raise WorkflowError("Native unit carries a non-native composition")
        if source_identity["unit_kind"] == "prefatory_basmala":
            raise WorkflowError(
                f"Legacy native input for {layout.ayah_ref} has no complete "
                "host-surah context; rerun the CLI to derive the full basmala analysis"
            )
    else:
        if set(analysis) != {
            "mode",
            "analysis_id",
            "composition",
            "composition_canonical_sha256",
            "context_bundles_dir",
            "member_bundles_dir",
            "selected_context_units",
            "surah_membership",
        } or analysis.get("mode") != "ordered_composition":
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
        if _sha256(source_bytes) != unit.get("source_sha256"):
            raise WorkflowError(f"Analysis context source changed: {source_path}")
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
    if composition is not None:
        _verify_analysis_bundle_roots(analysis, selected_units)
    _verify_added_ayah_root_agreement(analysis, selected_units)
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
            discovery_record = lane_record["discovery"]
            prompt_record = discovery_record["prompt"]
        except (KeyError, TypeError) as exc:
            raise WorkflowError(f"Manifest {lane} lane is incomplete") from exc
        packet_path = _verify_record(
            packet_record,
            label=f"{lane} packet",
            expected=layout.packet(lane),
        )
        prompt_path = _verify_record(
            prompt_record,
            label=f"{lane} discovery prompt",
            expected=layout.discovery_prompt(lane),
        )
        packet = _load_json(packet_path)
        _validate_packet_review_inventory(packet, lane=lane)
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
        expected_prompt, expected_discovery_record = _build_discovery_prompt(
            layout, lane, packet
        )
        for field in (
            "request_sha256",
            "request_inputs",
            "response_schema_version",
            "template_source",
            "template_sha256",
        ):
            if discovery_record.get(field) != expected_discovery_record[field]:
                raise WorkflowError(
                    f"Manifest {lane} discovery record is stale: {field}"
                )
        if prompt_path.read_text(encoding="utf-8") != expected_prompt:
            raise WorkflowError(f"Manifest {lane} discovery prompt content is stale")
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
        if discovery_record.get("expected_response") != _repo_path(
            layout.scope_discovery(lane)
        ):
            raise WorkflowError(
                f"Manifest {lane} discovery response path is stale"
            )
        composition_record = lane_record.get("composition")
        if composition_record is not None:
            if not isinstance(composition_record, dict):
                raise WorkflowError(
                    f"Manifest {lane} composition record is malformed"
                )
            try:
                composition_prompt_record = composition_record["prompt"]
                discovery_snapshot_record = composition_record["discovery"]
            except KeyError as exc:
                raise WorkflowError(
                    f"Manifest {lane} composition record is incomplete"
                ) from exc
            composition_prompt_path = _verify_record(
                composition_prompt_record,
                label=f"{lane} composition prompt",
                expected=layout.composition_prompt(lane),
            )
            discovery_path = _verify_record(
                discovery_snapshot_record,
                label=f"{lane} discovery response",
                expected=layout.scope_discovery(lane),
            )
            discovery = _load_json(discovery_path)
            _validate_scope_discovery(
                discovery,
                layout=layout,
                manifest=manifest,
                lane=lane,
                packet=packet,
            )
            expected_composition_prompt, expected_composition_record = (
                _build_composition_prompt(layout, lane, packet, discovery)
            )
            for field in (
                "request_sha256",
                "request_inputs",
                "response_schema_version",
                "template_source",
                "template_sha256",
                "discovery_sha256",
            ):
                if composition_record.get(field) != expected_composition_record[field]:
                    raise WorkflowError(
                        f"Manifest {lane} composition record is stale: {field}"
                    )
            if (
                composition_prompt_path.read_text(encoding="utf-8")
                != expected_composition_prompt
            ):
                raise WorkflowError(
                    f"Manifest {lane} composition prompt content is stale"
                )
            if composition_record.get("expected_response") != _repo_path(
                layout.scope_contribution(lane)
            ):
                raise WorkflowError(
                    f"Manifest {lane} composition response path is stale"
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
    return set(_extract_quran_refs(packet))


def _validate_packet_review_inventory(
    packet: dict[str, Any], *, lane: str
) -> dict[str, Any]:
    if packet.get("schema_version") != LANE_PACKET_SCHEMA_VERSION:
        raise WorkflowError(f"{lane} packet schema_version is stale")
    packet_identity = packet.get("identity")
    if not isinstance(packet_identity, dict) or packet_identity.get("lane") != lane:
        raise WorkflowError(f"{lane} packet identity is malformed")
    contract = packet.get("contract")
    required_contract = {
        "candidate_context_refs_are_exact",
        "support_quran_refs_are_structured",
        "accepted_candidates_require_dedicated_findings",
        "independent_discovery_is_required",
        "candidate_semantics_require_explicit_accounting",
        "root_branch_options_are_non_nominating",
    }
    if not isinstance(contract, dict) or any(
        contract.get(key) is not True for key in required_contract
    ):
        raise WorkflowError(f"{lane} packet V5 contract is incomplete")

    _packet_id_set(packet, "support_registry", "support_id", lane=lane)
    _packet_id_set(packet, "candidate_inventory", "candidate_id", lane=lane)
    _packet_id_set(packet, "connection_registry", "connection_ref", lane=lane)
    _packet_id_set(packet, "branch_registry", "branch_ref", lane=lane)

    auxiliary_sources = packet.get("auxiliary_context_sources")
    if not isinstance(auxiliary_sources, list) or not all(
        isinstance(record, dict) for record in auxiliary_sources
    ):
        raise WorkflowError(f"{lane} packet auxiliary context sources are malformed")
    auxiliary_by_ref: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    expected_source_fields = {
        "ayah_ref",
        "source_file",
        "bytes",
        "sha256",
        "canonical_sha256",
        "schema_version",
        "unit_kind",
    }
    for record in auxiliary_sources:
        if set(record) != expected_source_fields:
            raise WorkflowError(f"{lane} packet auxiliary source fields are malformed")
        ref = record.get("ayah_ref")
        if not isinstance(ref, str) or ref in auxiliary_by_ref:
            raise WorkflowError(f"{lane} packet auxiliary source identity is malformed")
        path = _resolve_manifest_source_path(
            record.get("source_file"), label=f"{lane} auxiliary context {ref}"
        )
        if not path.is_file() or path.is_symlink():
            raise WorkflowError(f"{lane} auxiliary context source is unavailable: {path}")
        payload = path.read_bytes()
        if len(payload) != record.get("bytes") or _sha256(payload) != record.get(
            "sha256"
        ):
            raise WorkflowError(f"{lane} auxiliary context source changed: {path}")
        try:
            bundle = json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise WorkflowError(f"Invalid auxiliary context source {path}: {exc}") from exc
        try:
            identity = compositions.validate_unit_bundle(bundle, expected_ref=ref)
        except compositions.CompositionError as exc:
            raise WorkflowError(str(exc)) from exc
        current_identity = {
            **identity,
            "canonical_sha256": compositions.canonical_sha256(bundle),
        }
        for field in ("canonical_sha256", "schema_version", "unit_kind"):
            if record.get(field) != current_identity.get(field):
                raise WorkflowError(
                    f"{lane} auxiliary context source identity is stale: {field}"
                )
        auxiliary_by_ref[ref] = (record, bundle)

    inventory = packet.get("review_inventory")
    expected_fields = {
        "surface_refs",
        "context_refs",
        "support_ids",
        "connection_refs",
        "connection_evidence_refs",
        "available_branch_facets",
    }
    if not isinstance(inventory, dict) or set(inventory) != expected_fields:
        raise WorkflowError(f"{lane} packet review inventory is malformed")

    support_ids = [
        support.get("support_id")
        for support in packet.get("support_registry", [])
        if isinstance(support, dict)
    ]
    if inventory.get("support_ids") != support_ids:
        raise WorkflowError(f"{lane} packet support review inventory is stale")
    support_map = {
        support["support_id"]: support
        for support in packet.get("support_registry", [])
        if isinstance(support, dict) and isinstance(support.get("support_id"), str)
    }
    candidates = packet.get("candidate_inventory")
    if not isinstance(candidates, list) or not all(
        isinstance(candidate, dict) for candidate in candidates
    ):
        raise WorkflowError(f"{lane} packet candidate inventory is malformed")
    obligation_owners: dict[str, str] = {}
    for candidate in candidates:
        candidate_id = candidate.get("candidate_id")
        branch_refs = candidate.get("branch_refs", [])
        required_context_refs = candidate.get("required_context_refs", [])
        branch_context_refs = candidate.get("branch_context_refs")
        required_branch_facets = candidate.get("required_branch_facets")
        semantic_obligations = candidate.get("semantic_obligations")
        root_branch_options = candidate.get("root_branch_options", [])
        if (
            not isinstance(branch_refs, list)
            or not all(isinstance(ref, str) and ref for ref in branch_refs)
            or len(branch_refs) != len(set(branch_refs))
            or not isinstance(required_context_refs, list)
            or not all(
                isinstance(ref, str)
                and compositions.REF_RE.fullmatch(ref) is not None
                for ref in required_context_refs
            )
            or required_context_refs
            != sorted(set(required_context_refs), key=_quran_ref_sort_key)
            or not isinstance(branch_context_refs, dict)
            or set(branch_context_refs) != set(branch_refs)
            or required_branch_facets
            != _required_candidate_branch_facets(
                candidate,
                {
                    str(branch.get("branch_ref")): branch
                    for branch in packet.get("branch_registry", [])
                    if isinstance(branch, dict)
                },
            )
            or root_branch_options
            != _candidate_root_branch_options(
                candidate,
                {
                    str(branch.get("branch_ref")): branch
                    for branch in packet.get("branch_registry", [])
                    if isinstance(branch, dict)
                },
            )
            or not isinstance(semantic_obligations, list)
            or not all(isinstance(row, dict) for row in semantic_obligations)
            or semantic_obligations
            != _candidate_semantic_obligations(candidate, support_map)
        ):
            raise WorkflowError(
                f"{lane} candidate branch-context binding is malformed: {candidate_id}"
            )
        obligation_refs = [
            row.get("obligation_ref") for row in semantic_obligations
        ]
        if (
            not all(isinstance(ref, str) and ref for ref in obligation_refs)
            or len(obligation_refs) != len(set(obligation_refs))
        ):
            raise WorkflowError(
                f"{lane} candidate semantic obligations are duplicated or malformed: "
                f"{candidate_id}"
            )
        for obligation_ref in obligation_refs:
            previous_owner = obligation_owners.setdefault(
                str(obligation_ref), str(candidate_id)
            )
            if previous_owner != candidate_id:
                raise WorkflowError(
                    f"{lane} semantic obligation {obligation_ref} has multiple owners"
                )
        for branch_ref, refs in branch_context_refs.items():
            if (
                not isinstance(refs, list)
                or not all(
                    isinstance(ref, str)
                    and compositions.REF_RE.fullmatch(ref) is not None
                    for ref in refs
                )
                or refs != sorted(set(refs), key=_quran_ref_sort_key)
                or not set(refs) <= set(required_context_refs)
            ):
                raise WorkflowError(
                    f"{lane} candidate branch-context refs are stale: "
                    f"{candidate_id}/{branch_ref}"
                )
    surface_refs = _focus_surface_refs(packet)
    if inventory.get("surface_refs") != surface_refs:
        raise WorkflowError(f"{lane} packet surface review inventory is stale")
    context_refs = inventory.get("context_refs")
    if (
        not isinstance(context_refs, list)
        or len(context_refs) != len(set(context_refs))
        or not all(
            isinstance(ref, str) and compositions.REF_RE.fullmatch(ref) is not None
            for ref in context_refs
        )
    ):
        raise WorkflowError(f"{lane} packet context review inventory is malformed")
    non_context_refs = {
        ref
        for ref in (
            packet_identity.get("ayah_ref"),
            packet_identity.get("linguistic_source_ref"),
        )
        if isinstance(ref, str) and ref
    }
    misclassified = set(context_refs) & non_context_refs
    if misclassified:
        raise WorkflowError(
            f"{lane} packet context review inventory includes its focus identity: "
            f"{sorted(misclassified, key=_quran_ref_sort_key)}"
        )
    candidate_context_refs = {
        ref
        for candidate in candidates
        for ref in candidate.get("required_context_refs", [])
    }
    unreviewed_candidate_context = candidate_context_refs - set(context_refs)
    if unreviewed_candidate_context:
        raise WorkflowError(
            f"{lane} packet candidate context is missing from its review inventory: "
            f"{sorted(unreviewed_candidate_context, key=_quran_ref_sort_key)}"
        )

    connections = packet.get("connection_registry")
    if not isinstance(connections, list) or not all(
        isinstance(connection, dict) for connection in connections
    ):
        raise WorkflowError(f"{lane} packet connection registry is malformed")
    connection_refs = [connection.get("connection_ref") for connection in connections]
    if inventory.get("connection_refs") != connection_refs:
        raise WorkflowError(f"{lane} packet connection review inventory is stale")
    expected_evidence_refs = {
        connection["connection_ref"]: _connection_evidence_refs(connection)
        for connection in connections
    }
    if inventory.get("connection_evidence_refs") != expected_evidence_refs:
        raise WorkflowError(
            f"{lane} packet connection-evidence review inventory is stale"
        )

    branches = packet.get("branch_registry")
    if not isinstance(branches, list) or not all(
        isinstance(branch, dict) for branch in branches
    ):
        raise WorkflowError(f"{lane} packet branch registry is malformed")
    if inventory.get("available_branch_facets") != _branch_review_pairs(branches):
        raise WorkflowError(f"{lane} packet available branch-facet inventory is stale")
    used_auxiliary_refs: set[str] = set()
    for branch in branches:
        legacy_context_fields = {
            "context_source_ref",
            "context_source_canonical_sha256",
        } & set(branch)
        if legacy_context_fields:
            raise WorkflowError(
                f"{lane} context branch uses legacy singular source metadata"
            )
        context_refs = branch.get("context_source_refs")
        if context_refs is None:
            if "context_source_pointers" in branch or (
                "context_source_canonical_sha256s" in branch
            ):
                raise WorkflowError(
                    f"{lane} context branch has orphaned source metadata"
                )
            continue
        if (
            not isinstance(context_refs, list)
            or not context_refs
            or not all(
                isinstance(ref, str)
                and compositions.REF_RE.fullmatch(ref) is not None
                for ref in context_refs
            )
            or context_refs
            != sorted(set(context_refs), key=_quran_ref_sort_key)
        ):
            raise WorkflowError(
                f"{lane} context branch source refs are malformed"
            )
        missing_sources = set(context_refs) - set(auxiliary_by_ref)
        if missing_sources:
            raise WorkflowError(
                f"{lane} context branch has no bound sources: "
                f"{sorted(missing_sources, key=_quran_ref_sort_key)}"
            )
        expected_descriptor = _combined_context_branch_descriptor(
            [
                (context_ref, auxiliary_by_ref[context_ref][1])
                for context_ref in context_refs
            ],
            str(branch.get("branch_ref")),
        )
        dynamic_fields = {
            "candidate_links",
            "support_links",
            "hft_citations",
            "context_source_canonical_sha256s",
        }
        if (
            expected_descriptor is None
            or set(branch) != set(expected_descriptor) | dynamic_fields
            or any(
                branch.get(field) != value
                for field, value in expected_descriptor.items()
            )
        ):
            raise WorkflowError(
                f"{lane} hydrated context branch is stale: {branch.get('branch_ref')}"
            )
        expected_hashes = {
            context_ref: auxiliary_by_ref[context_ref][0]["canonical_sha256"]
            for context_ref in context_refs
        }
        if branch.get("context_source_canonical_sha256s") != expected_hashes:
            raise WorkflowError(
                f"{lane} hydrated context branch source hashes are stale"
            )
        used_auxiliary_refs.update(context_refs)
    if used_auxiliary_refs != set(auxiliary_by_ref):
        raise WorkflowError(f"{lane} packet has unused auxiliary context sources")
    return inventory


def _assert_reader_prose_has_no_internal_ids(value: str, *, label: str) -> None:
    match = INTERNAL_PROSE_ID_RE.search(value)
    if match is not None:
        raise WorkflowError(f"{label} exposes internal ID {match.group(0)!r}")
    coordinate = QURAN_COORDINATE_RE.search(value)
    if coordinate is not None:
        raise WorkflowError(
            f"{label} exposes analysis/QAC coordinate {coordinate.group(0)!r}"
        )


def _exclusion_map(
    value: Any, *, label: str, ref_field: str
) -> dict[str, dict[str, Any]]:
    if not isinstance(value, list):
        raise WorkflowError(f"{label} must be an array")
    rows: dict[str, dict[str, Any]] = {}
    expected_fields = {ref_field, "reason"}
    for index, row in enumerate(value):
        row_label = f"{label}[{index}]"
        if not isinstance(row, dict) or set(row) != expected_fields:
            raise WorkflowError(f"{row_label} fields are malformed")
        ref = _required_text(row.get(ref_field), label=f"{row_label}.{ref_field}")
        _required_text(row.get("reason"), label=f"{row_label}.reason")
        if ref in rows:
            raise WorkflowError(f"{label} duplicates {ref}")
        rows[ref] = row
    return rows


def _branch_source_values(
    branch: dict[str, Any], facet_id: str | None
) -> tuple[Any, Any]:
    facets = branch.get("review_facets")
    if facet_id is None:
        if isinstance(facets, list) and facets:
            raise WorkflowError(
                f"Resolved branch {branch.get('branch_ref')} requires a facet ID"
            )
        return branch.get("gloss"), None
    if not isinstance(facets, list):
        raise WorkflowError(f"Branch {branch.get('branch_ref')} has no facets")
    matching = [
        facet
        for facet in facets
        if isinstance(facet, dict) and facet.get("facet_id") == facet_id
    ]
    if len(matching) != 1:
        raise WorkflowError(
            f"Branch {branch.get('branch_ref')} has no unique facet {facet_id}"
        )
    statements = matching[0].get("statements")
    statement = statements.get("statement") if isinstance(statements, dict) else None
    if not isinstance(statement, str) or not statement.strip():
        raise WorkflowError(
            f"Branch {branch.get('branch_ref')} facet {facet_id} has no statement"
        )
    return branch.get("gloss"), statement


def _packet_grounding_refs(packet: dict[str, Any]) -> tuple[set[str], set[str]]:
    all_refs = _packet_quran_refs(packet)
    focus_refs: set[str] = set()
    focus_surface = packet.get("focus_surface_evidence")
    if isinstance(focus_surface, dict):
        for ref in focus_surface.get("word_analysis_refs", []):
            if isinstance(ref, str) and ref:
                all_refs.add(ref)
                focus_refs.add(ref)
        for row in focus_surface.get("qac_morphemes", []):
            if not isinstance(row, dict):
                continue
            for field in ("qac_ref", "qac_word_ref"):
                ref = row.get(field)
                if isinstance(ref, str) and ref:
                    all_refs.add(ref)
                    focus_refs.add(ref)
    branches = packet.get("branch_registry")
    if isinstance(branches, list):
        for branch in branches:
            if not isinstance(branch, dict):
                continue
            for occurrence_field in (
                "focus_root_occurrences",
                "context_root_occurrences",
            ):
                occurrences = branch.get(occurrence_field)
                if not isinstance(occurrences, list):
                    continue
                for occurrence in occurrences:
                    if not isinstance(occurrence, dict):
                        continue
                    for field in ("qac_ref", "qac_word_ref"):
                        ref = occurrence.get(field)
                        if not isinstance(ref, str) or not ref:
                            continue
                        all_refs.add(ref)
                        if occurrence_field == "focus_root_occurrences":
                            focus_refs.add(ref)
            citations = branch.get("hft_citations")
            if not isinstance(citations, list):
                continue
            for citation in citations:
                if not isinstance(citation, dict):
                    continue
                source_refs = _extract_quran_refs(citation.get("source_ref"))
                all_refs.update(source_refs)
                if len(source_refs) != 1:
                    continue
                for word_index in citation.get("source_word_indices", []):
                    if (
                        isinstance(word_index, str)
                        and word_index.isdigit()
                        and int(word_index) > 0
                    ):
                        all_refs.add(f"{source_refs[0]}:{int(word_index)}")
    return all_refs, focus_refs


def _branch_occurrence_refs(
    branch: dict[str, Any], field: str
) -> set[str]:
    return {
        ref
        for occurrence in branch.get(field, [])
        if isinstance(occurrence, dict)
        for ref in (
            occurrence.get("qac_ref"),
            occurrence.get("qac_word_ref"),
        )
        if isinstance(ref, str) and ref
    }


def _branch_attributed_carrier_refs(branch: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for citation in branch.get("hft_citations", []):
        if not isinstance(citation, dict):
            continue
        source_refs = _extract_quran_refs(citation.get("source_ref"))
        refs.update(source_refs)
        if len(source_refs) != 1:
            continue
        for word_index in citation.get("source_word_indices", []):
            if (
                isinstance(word_index, str)
                and word_index.isdigit()
                and int(word_index) > 0
            ):
                refs.add(f"{source_refs[0]}:{int(word_index)}")
    return refs


def _context_branch_carriers_for_finding(
    branch: dict[str, Any],
    branch_ref: str,
    finding_candidate_ids: list[str],
    candidates: dict[str, dict[str, Any]],
) -> set[str]:
    all_carriers = _branch_occurrence_refs(branch, "context_root_occurrences")
    if not finding_candidate_ids:
        return all_carriers

    bound_sources: set[str] = set()
    matching_candidate = False
    for candidate_id in finding_candidate_ids:
        candidate = candidates[candidate_id]
        if branch_ref not in candidate.get("branch_refs", []):
            continue
        matching_candidate = True
        bindings = candidate.get("branch_context_refs")
        if not isinstance(bindings, dict) or branch_ref not in bindings:
            raise WorkflowError(
                f"Finding candidate {candidate_id} lacks exact context binding for "
                f"{branch_ref}"
            )
        refs = bindings[branch_ref]
        if not isinstance(refs, list):
            raise WorkflowError(
                f"Finding candidate {candidate_id} has malformed context binding for "
                f"{branch_ref}"
            )
        bound_sources.update(refs)
    if not matching_candidate:
        raise WorkflowError(
            f"Candidate-owned finding activates unrelated context branch {branch_ref}; "
            "use a dedicated discovered finding"
        )
    carrier_map = branch.get("context_root_occurrence_refs_by_source")
    if not isinstance(carrier_map, dict):
        raise WorkflowError(f"Context branch {branch_ref} lacks per-source carriers")
    unknown_sources = bound_sources - set(carrier_map)
    if unknown_sources:
        raise WorkflowError(
            f"Context branch {branch_ref} lacks candidate-bound sources: "
            f"{sorted(unknown_sources, key=_quran_ref_sort_key)}"
        )
    return {
        ref
        for source_ref in bound_sources
        for ref in carrier_map[source_ref]
        if isinstance(ref, str) and ref
    }


def _grounding_anchor(ref: str) -> str:
    parts = ref.split(":")
    if len(parts) >= 3 and all(part.isdigit() for part in parts[:3]):
        return ":".join(parts[:3])
    return ref


OBVIOUS_ENGLISH_PROSE_RE = re.compile(
    r"\b(?:discernment|salience|adversarial|nominative|accusative|definite|"
    r"indefinite|carrier|trigger|branch|finding|reader\s+payoff|changed\s+reading|"
    r"scope\s+review|semantic\s+obligation|lexical\s+activation)\b",
    re.IGNORECASE,
)
ENGLISH_FUNCTION_WORDS = frozenset({
    "a", "an", "and", "are", "as", "be", "because", "but", "by", "for",
    "from", "has", "have", "in", "into", "is", "it", "its", "not", "of",
    "on", "only", "or", "that", "the", "their", "these", "they", "this",
    "those", "through", "to", "was", "were", "which", "while", "with",
})
ENGLISH_CONTENT_WORDS = frozenset({
    "action", "actions", "beauty", "branch", "branches", "candidate",
    "candidates", "carrier", "carriers", "claim", "claims", "context",
    "contexts", "disease", "evidence", "finding", "findings", "friction", "guide",
    "guides", "insight", "knowledge", "meaning", "meanings", "memory",
    "mechanism", "path", "paths", "payoff", "reading", "readings", "road",
    "roads", "root", "roots", "semantic", "semantics", "sentence",
    "sentences", "support", "supports", "trigger", "triggers", "vision",
    "word", "words",
})
TURKISH_MARKER_WORDS = frozenset({
    "ama", "ancak", "ayet", "ayette", "baska", "bir", "bu", "bunu",
    "cunku", "da", "daha", "de", "degil", "diye", "gibi", "hem", "icin",
    "ile", "ise", "kadar", "kendi", "ki", "mi", "ne", "olarak", "olan",
    "oldugu", "okur", "sonra", "su", "ve", "veya", "yalniz", "yine",
})
TURKISH_SUFFIXES = (
    "acak", "ecek", "arak", "erek", "daki", "deki", "dir", "dur", "iyor",
    "lar", "ler", "lik", "luk", "mek", "mak", "mis", "mus",
    "nin", "nun", "yla", "yle",
)


def _assert_no_obvious_english(value: str, *, label: str) -> None:
    """Reject obvious English leakage without policing Arabic/transliteration."""
    match = OBVIOUS_ENGLISH_PROSE_RE.search(value)
    if match is not None:
        raise WorkflowError(
            f"{label} contains reader-facing English {match.group(0)!r}"
        )
    cleaned = re.sub(r"\{\{(?:ar|tr):[^}]+\}\}", " ", value)
    for sentence in re.split(r"[.!?\n]+", cleaned):
        words = re.findall(r"[A-Za-z]+", sentence.lower())
        markers = [word for word in words if word in ENGLISH_FUNCTION_WORDS]
        if len(markers) >= 4 and len(set(markers)) >= 3:
            raise WorkflowError(
                f"{label} contains an apparently English reader-facing sentence"
            )
        if len(words) < 3:
            continue
        has_turkish_signal = bool(
            re.search(r"[\u00c7\u00d6\u00dc\u011e\u0130\u015e\u00e7\u011f\u0131\u00f6\u015f\u00fc]", sentence)
        ) or any(
            word in TURKISH_MARKER_WORDS
            or (len(word) >= 6 and word.endswith(TURKISH_SUFFIXES))
            for word in words
        )
        english_signals = sum(
            word in ENGLISH_FUNCTION_WORDS
            or word in ENGLISH_CONTENT_WORDS
            or (
                len(word) >= 6
                and word.endswith(
                    ("ing", "tion", "ment", "ness", "ously", "ively")
                )
            )
            for word in words
        )
        if not has_turkish_signal and english_signals >= 2:
            raise WorkflowError(
                f"{label} contains an apparently English reader-facing sentence"
            )


def _assert_reader_prose_is_turkish(value: str, *, label: str) -> None:
    _assert_reader_prose_has_no_internal_ids(value, label=label)
    _assert_no_obvious_english(value, label=label)


def _pair_exclusion_map(value: Any, *, label: str) -> dict[tuple[str, str | None], dict[str, Any]]:
    if not isinstance(value, list):
        raise WorkflowError(f"{label} must be an array")
    rows: dict[tuple[str, str | None], dict[str, Any]] = {}
    expected_fields = {"branch_ref", "facet_id", "reason"}
    for index, row in enumerate(value):
        row_label = f"{label}[{index}]"
        if not isinstance(row, dict) or set(row) != expected_fields:
            raise WorkflowError(f"{row_label} fields are malformed")
        branch_ref = _required_text(
            row.get("branch_ref"), label=f"{row_label}.branch_ref"
        )
        facet_id = row.get("facet_id")
        if facet_id is not None and (
            not isinstance(facet_id, str) or not facet_id.strip()
        ):
            raise WorkflowError(f"{row_label}.facet_id is malformed")
        _required_text(row.get("reason"), label=f"{row_label}.reason")
        key = (branch_ref, facet_id)
        if key in rows:
            raise WorkflowError(f"{label} duplicates {key}")
        rows[key] = row
    return rows


def _grounding_context_refs(
    refs: list[str], *, focus_ref: str, linguistic_source_ref: str
) -> set[str]:
    result: set[str] = set()
    for ref in refs:
        coordinate_ref = _coordinate_ayah_ref(ref)
        if coordinate_ref is not None:
            result.add(coordinate_ref)
        else:
            result.update(_extract_quran_refs(ref))
    result.discard(focus_ref)
    result.discard(linguistic_source_ref)
    return result


def _validate_scope_discovery(
    discovery: dict[str, Any],
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
        "friction_notes",
    }
    if set(discovery) != expected_top_level:
        raise WorkflowError(f"{lane} discovery top-level fields are malformed")
    if discovery.get("schema_version") != SCOPE_DISCOVERY_SCHEMA_VERSION:
        raise WorkflowError(f"{lane} discovery schema_version is stale")
    identity = discovery.get("identity")
    expected_identity = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": packet.get("identity", {}).get(
            "lane_packet_sha256"
        ),
        "authoring_request_sha256": manifest["lanes"][lane]["discovery"][
            "request_sha256"
        ],
    }
    if identity != expected_identity:
        raise WorkflowError(f"{lane} discovery identity is stale or mixed")
    if (
        discovery.get("ayah_ref") != layout.ayah_ref
        or discovery.get("lane") != lane
        or discovery.get("coverage_complete") is not True
    ):
        raise WorkflowError(f"{lane} discovery focus/lane/coverage is malformed")

    review_inventory = _validate_packet_review_inventory(packet, lane=lane)
    candidate_rows = packet.get("candidate_inventory", [])
    candidates = {row["candidate_id"]: row for row in candidate_rows}
    supports = {
        row["support_id"]: row for row in packet.get("support_registry", [])
    }
    branches = {
        row["branch_ref"]: row for row in packet.get("branch_registry", [])
    }
    connection_refs = _packet_id_set(
        packet, "connection_registry", "connection_ref", lane=lane
    )
    all_grounding_refs, focus_grounding_refs = _packet_grounding_refs(packet)
    packet_quran_refs = _packet_quran_refs(packet)
    linguistic_source_ref = str(
        packet.get("identity", {}).get("linguistic_source_ref", layout.ayah_ref)
    )

    raw_decisions = discovery.get("candidate_decisions")
    if not isinstance(raw_decisions, list):
        raise WorkflowError(f"{lane} candidate_decisions must be an array")
    decisions: dict[str, dict[str, Any]] = {}
    decision_fields = {
        "candidate_id",
        "decision",
        "reason",
        "finding_refs",
        "branch_exclusions",
        "facet_exclusions",
        "context_exclusions",
        "semantic_obligation_exclusions",
    }
    for index, decision in enumerate(raw_decisions):
        label = f"{lane} candidate_decisions[{index}]"
        if not isinstance(decision, dict) or set(decision) != decision_fields:
            raise WorkflowError(f"{label} fields are malformed")
        candidate_id = _required_text(
            decision.get("candidate_id"), label=f"{label}.candidate_id"
        )
        if candidate_id in decisions:
            raise WorkflowError(f"{lane} candidate decision is duplicated: {candidate_id}")
        if decision.get("decision") not in {"accept", "narrow", "represented", "reject"}:
            raise WorkflowError(f"{label}.decision is invalid")
        _required_text(decision.get("reason"), label=f"{label}.reason")
        _string_list(decision.get("finding_refs"), label=f"{label}.finding_refs")
        decisions[candidate_id] = decision
    if set(decisions) != set(candidates):
        raise WorkflowError(f"{lane} candidate decision accounting is incomplete")

    raw_findings = discovery.get("findings")
    if not isinstance(raw_findings, list):
        raise WorkflowError(f"{lane} findings must be an array")
    findings: dict[str, dict[str, Any]] = {}
    finding_fields = {
        "finding_ref",
        "origin_candidate_id",
        "represented_candidate_ids",
        "title",
        "claim",
        "mechanism",
        "reader_payoff",
        "containment",
        "epistemic",
        "support_ids",
        "branch_activations",
        "connection_refs",
        "context_refs",
        "semantic_obligation_refs",
    }
    activation_fields = {
        "branch_ref",
        "facet_id",
        "branch_gloss",
        "facet_statement",
        "application_mode",
        "carrier_refs",
        "trigger_refs",
        "focus_return_refs",
        "carrier",
        "independent_trigger",
        "activation",
        "resulting_reading",
        "boundary",
    }
    global_obligations = {
        row["obligation_ref"]
        for candidate in candidates.values()
        for row in candidate.get("semantic_obligations", [])
    }
    finding_activation_context: dict[str, set[str]] = {}
    finding_activation_pairs: dict[str, set[tuple[str, str | None]]] = {}
    for index, finding in enumerate(raw_findings):
        label = f"{lane} findings[{index}]"
        if not isinstance(finding, dict) or set(finding) != finding_fields:
            raise WorkflowError(f"{label} fields are malformed")
        finding_ref = _required_text(
            finding.get("finding_ref"), label=f"{label}.finding_ref"
        )
        if not finding_ref.startswith(f"{lane}:") or finding_ref in findings:
            raise WorkflowError(f"{label}.finding_ref is invalid or duplicated")
        origin = finding.get("origin_candidate_id")
        represented = _string_list(
            finding.get("represented_candidate_ids"),
            label=f"{label}.represented_candidate_ids",
        )
        if origin is not None and origin not in candidates:
            raise WorkflowError(f"{label} has an unknown origin candidate")
        if set(represented) - set(candidates) or origin in represented:
            raise WorkflowError(f"{label} represented candidates are malformed")
        for field in ("title", "claim", "mechanism", "reader_payoff", "containment"):
            _required_text(finding.get(field), label=f"{label}.{field}")
        cited_supports = _string_list(
            finding.get("support_ids"), label=f"{label}.support_ids"
        )
        cited_connections = _string_list(
            finding.get("connection_refs"), label=f"{label}.connection_refs"
        )
        cited_context = _string_list(
            finding.get("context_refs"), label=f"{label}.context_refs"
        )
        obligation_refs = _string_list(
            finding.get("semantic_obligation_refs"),
            label=f"{label}.semantic_obligation_refs",
        )
        if set(cited_supports) - set(supports):
            raise WorkflowError(f"{label}.support_ids cites unknown evidence")
        if set(cited_connections) - connection_refs:
            raise WorkflowError(f"{label}.connection_refs cites unknown connections")
        if set(cited_context) - set(review_inventory["context_refs"]):
            raise WorkflowError(f"{label}.context_refs cites unavailable context")
        if set(obligation_refs) - global_obligations:
            raise WorkflowError(f"{label} cites unknown semantic obligations")

        candidate_ids = [candidate_id for candidate_id in [origin, *represented] if candidate_id]
        allowed_obligations = {
            row["obligation_ref"]
            for candidate_id in candidate_ids
            for row in candidates[candidate_id].get("semantic_obligations", [])
        }
        if set(obligation_refs) - allowed_obligations:
            raise WorkflowError(f"{label} borrows another candidate's semantic obligation")

        raw_activations = finding.get("branch_activations")
        if not isinstance(raw_activations, list):
            raise WorkflowError(f"{label}.branch_activations must be an array")
        activation_context: set[str] = set()
        activation_pairs: set[tuple[str, str | None]] = set()
        unresolved_activation = False
        for activation_index, activation in enumerate(raw_activations):
            activation_label = f"{label}.branch_activations[{activation_index}]"
            if not isinstance(activation, dict) or set(activation) != activation_fields:
                raise WorkflowError(f"{activation_label} fields are malformed")
            branch_ref = _required_text(
                activation.get("branch_ref"), label=f"{activation_label}.branch_ref"
            )
            if branch_ref not in branches:
                raise WorkflowError(f"{activation_label} cites an unknown branch")
            facet_id = activation.get("facet_id")
            branch_gloss, facet_statement = _branch_source_values(
                branches[branch_ref], facet_id
            )
            if (
                activation.get("branch_gloss") != branch_gloss
                or activation.get("facet_statement") != facet_statement
            ):
                raise WorkflowError(f"{activation_label} changes packet branch semantics")
            pair = (branch_ref, facet_id)
            if pair in activation_pairs:
                raise WorkflowError(f"{label} duplicates a branch facet")
            activation_pairs.add(pair)
            mode = activation.get("application_mode")
            if mode not in BRANCH_APPLICATION_MODES:
                raise WorkflowError(f"{activation_label}.application_mode is invalid")
            carrier_refs = _string_list(
                activation.get("carrier_refs"), label=f"{activation_label}.carrier_refs"
            )
            trigger_refs = _string_list(
                activation.get("trigger_refs"), label=f"{activation_label}.trigger_refs"
            )
            focus_return_refs = _string_list(
                activation.get("focus_return_refs"),
                label=f"{activation_label}.focus_return_refs",
            )
            if (
                set(carrier_refs) - all_grounding_refs
                or set(trigger_refs) - all_grounding_refs
                or set(focus_return_refs) - focus_grounding_refs
                or layout.ayah_ref in focus_return_refs
            ):
                raise WorkflowError(f"{activation_label} uses unavailable grounding refs")
            branch = branches[branch_ref]
            registry = branch.get("registry")
            if registry == "focus":
                allowed_carriers = _branch_occurrence_refs(
                    branch, "focus_root_occurrences"
                )
            elif registry == "context":
                allowed_carriers = _context_branch_carriers_for_finding(
                    branch, branch_ref, candidate_ids, candidates
                )
            else:
                if mode != "attributed":
                    raise WorkflowError(
                        f"{activation_label} is unresolved and must remain attributed"
                    )
                allowed_carriers = _branch_attributed_carrier_refs(branch)
            if not allowed_carriers or not set(carrier_refs) <= allowed_carriers:
                raise WorkflowError(f"{activation_label} substitutes a non-carrier")
            carrier_anchors = {_grounding_anchor(ref) for ref in carrier_refs}
            if not any(
                _grounding_anchor(ref) not in carrier_anchors
                and ref != layout.ayah_ref
                for ref in trigger_refs
            ):
                raise WorkflowError(f"{activation_label} has no independent trigger")
            for field in (
                "carrier",
                "independent_trigger",
                "activation",
                "resulting_reading",
                "boundary",
            ):
                _required_text(activation.get(field), label=f"{activation_label}.{field}")
            activation_context.update(
                _grounding_context_refs(
                    [*carrier_refs, *trigger_refs],
                    focus_ref=layout.ayah_ref,
                    linguistic_source_ref=linguistic_source_ref,
                )
            )
            unresolved_activation = unresolved_activation or (
                branch.get("lexicon_identity_status") == "unresolved"
            )
        if not activation_context <= set(cited_context):
            raise WorkflowError(f"{label}.context_refs omits activation context")
        if not set(cited_context) <= packet_quran_refs:
            raise WorkflowError(f"{label}.context_refs is outside the packet")
        finding_activation_context[finding_ref] = activation_context
        finding_activation_pairs[finding_ref] = activation_pairs
        for activated_branch_ref in {pair[0] for pair in activation_pairs}:
            branch = branches[activated_branch_ref]
            core_pairs = {
                (activated_branch_ref, facet.get("facet_id"))
                for facet in branch.get("review_facets", [])
                if isinstance(facet, dict) and facet.get("role") == "core"
            }
            landed_for_branch = {
                pair for pair in activation_pairs
                if pair[0] == activated_branch_ref
            }
            if core_pairs and not (landed_for_branch & core_pairs):
                raise WorkflowError(
                    f"{label} retains a branch specialization without its core facet"
                )

        epistemic = finding.get("epistemic")
        if not isinstance(epistemic, dict) or set(epistemic) != {
            "status", "source_trust", "reason"
        }:
            raise WorkflowError(f"{label}.epistemic fields are malformed")
        if epistemic.get("status") not in EPISTEMIC_STATUSES:
            raise WorkflowError(f"{label}.epistemic.status is invalid")
        _required_text(epistemic.get("reason"), label=f"{label}.epistemic.reason")
        source_trust = _string_list(
            epistemic.get("source_trust"), label=f"{label}.epistemic.source_trust"
        )
        expected_trust = sorted({
            trust
            for trust in [
                *(candidates[candidate_id].get("trust") for candidate_id in candidate_ids),
                *(supports[support_id].get("trust") for support_id in cited_supports),
            ]
            if isinstance(trust, str) and trust
        })
        if source_trust != expected_trust:
            raise WorkflowError(f"{label}.epistemic.source_trust is incomplete")
        if epistemic.get("status") == "grounded" and (
            "legacy_unbound" in source_trust or unresolved_activation
        ):
            raise WorkflowError(f"{label} cannot be grounded from qualified evidence")
        if not (cited_supports or raw_activations or cited_connections):
            raise WorkflowError(f"{label} has no cited evidence")
        findings[finding_ref] = finding

    for candidate_id, decision in decisions.items():
        disposition = decision["decision"]
        decision_refs = set(decision["finding_refs"])
        if decision_refs - set(findings):
            raise WorkflowError(f"{lane} decision {candidate_id} cites unknown findings")
        origin_refs = {
            ref for ref, finding in findings.items()
            if finding["origin_candidate_id"] == candidate_id
        }
        represented_refs = {
            ref for ref, finding in findings.items()
            if candidate_id in finding["represented_candidate_ids"]
        }
        if disposition == "reject":
            if decision_refs or origin_refs or represented_refs:
                raise WorkflowError(f"{lane} rejected candidate {candidate_id} survives")
        elif disposition in {"accept", "narrow"}:
            if decision_refs != origin_refs or represented_refs:
                raise WorkflowError(
                    f"{lane} candidate {candidate_id} lacks dedicated origin findings"
                )
        elif len(decision_refs) != 1 or decision_refs != represented_refs or origin_refs:
            raise WorkflowError(
                f"{lane} represented candidate {candidate_id} lacks one duplicate finding"
            )

        candidate = candidates[candidate_id]
        target_refs = decision_refs
        branch_exclusions = _exclusion_map(
            decision["branch_exclusions"],
            label=f"{lane} decision {candidate_id}.branch_exclusions",
            ref_field="branch_ref",
        )
        facet_exclusions = _pair_exclusion_map(
            decision["facet_exclusions"],
            label=f"{lane} decision {candidate_id}.facet_exclusions",
        )
        context_exclusions = _exclusion_map(
            decision["context_exclusions"],
            label=f"{lane} decision {candidate_id}.context_exclusions",
            ref_field="context_ref",
        )
        obligation_exclusions = _exclusion_map(
            decision["semantic_obligation_exclusions"],
            label=(
                f"{lane} decision {candidate_id}.semantic_obligation_exclusions"
            ),
            ref_field="obligation_ref",
        )
        candidate_branches = set(candidate.get("branch_refs", []))
        candidate_pairs = {
            (row["branch_ref"], row.get("facet_id"))
            for row in candidate.get("required_branch_facets", [])
        }
        if set(branch_exclusions) - candidate_branches:
            raise WorkflowError(f"{lane} decision {candidate_id} excludes unknown branches")
        if set(facet_exclusions) - candidate_pairs:
            raise WorkflowError(f"{lane} decision {candidate_id} excludes unknown facets")
        if any(pair[0] in branch_exclusions for pair in facet_exclusions):
            raise WorkflowError(f"{lane} decision {candidate_id} double-excludes facets")
        landed_candidate_pairs = {
            pair
            for ref in target_refs
            for pair in finding_activation_pairs[ref]
            if pair[0] in candidate_branches
        }
        landed_branches = {pair[0] for pair in landed_candidate_pairs}
        if landed_branches & set(branch_exclusions):
            raise WorkflowError(f"{lane} decision {candidate_id} lands excluded branches")
        if landed_branches | set(branch_exclusions) != candidate_branches:
            raise WorkflowError(
                f"{lane} candidate {candidate_id} branch accounting is incomplete"
            )
        landed_pairs = landed_candidate_pairs & candidate_pairs
        branch_excluded_pairs = {
            pair for pair in candidate_pairs if pair[0] in branch_exclusions
        }
        if landed_pairs & (branch_excluded_pairs | set(facet_exclusions)):
            raise WorkflowError(f"{lane} decision {candidate_id} lands excluded facets")
        if landed_pairs | branch_excluded_pairs | set(facet_exclusions) != candidate_pairs:
            raise WorkflowError(
                f"{lane} candidate {candidate_id} branch-facet accounting is incomplete"
            )
        required_context = set(candidate.get("required_context_refs", []))
        if set(context_exclusions) - required_context:
            raise WorkflowError(f"{lane} decision {candidate_id} excludes unknown context")
        landed_context = {
            ref
            for finding_ref in target_refs
            for ref in finding_activation_context[finding_ref]
            if ref in required_context
        }
        if landed_context & set(context_exclusions):
            raise WorkflowError(f"{lane} decision {candidate_id} lands excluded context")
        if landed_context | set(context_exclusions) != required_context:
            raise WorkflowError(
                f"{lane} candidate {candidate_id} context accounting is incomplete; "
                "a retained context ref must be an activation carrier or trigger"
            )

        candidate_obligations = {
            row["obligation_ref"] for row in candidate.get("semantic_obligations", [])
        }
        if set(obligation_exclusions) - candidate_obligations:
            raise WorkflowError(
                f"{lane} decision {candidate_id} excludes unknown semantic obligations"
            )
        landed_obligations = {
            obligation_ref
            for finding_ref in target_refs
            for obligation_ref in findings[finding_ref]["semantic_obligation_refs"]
            if obligation_ref in candidate_obligations
        }
        if landed_obligations & set(obligation_exclusions):
            raise WorkflowError(f"{lane} decision {candidate_id} lands excluded obligations")
        if landed_obligations | set(obligation_exclusions) != candidate_obligations:
            raise WorkflowError(
                f"{lane} candidate {candidate_id} semantic-obligation accounting is incomplete"
            )
        obligations_by_ref = {
            row["obligation_ref"]: row
            for row in candidate.get("semantic_obligations", [])
        }
        for finding_ref in target_refs:
            finding_pairs = finding_activation_pairs[finding_ref]
            finding_context = finding_activation_context[finding_ref]
            for obligation_ref in findings[finding_ref]["semantic_obligation_refs"]:
                obligation = obligations_by_ref.get(obligation_ref)
                if obligation is None or obligation.get("kind") != "activation_trace":
                    continue
                branch_ref = obligation.get("branch_ref")
                if isinstance(branch_ref, str) and not any(
                    pair[0] == branch_ref for pair in finding_pairs
                ):
                    raise WorkflowError(
                        f"{lane} candidate {candidate_id} lands an activation-trace "
                        "obligation without its named branch"
                    )
                source_ref = obligation.get("source_ref")
                if (
                    isinstance(source_ref, str)
                    and source_ref not in {layout.ayah_ref, linguistic_source_ref}
                    and source_ref not in finding_context
                ):
                    raise WorkflowError(
                        f"{lane} candidate {candidate_id} lands an activation-trace "
                        "obligation without its context carrier or trigger"
                    )
        if disposition in {"accept", "represented"} and any((
            branch_exclusions,
            facet_exclusions,
            context_exclusions,
            obligation_exclusions,
        )):
            raise WorkflowError(
                f"{lane} {disposition} candidate {candidate_id} has exclusions"
            )
        if (
            disposition == "narrow"
            and candidate_obligations
            and not landed_obligations
        ):
            raise WorkflowError(
                f"{lane} narrowed candidate {candidate_id} has no retained "
                "semantic obligation"
            )
        if disposition != "reject":
            landed_supports = {
                support_id
                for finding_ref in target_refs
                for support_id in findings[finding_ref]["support_ids"]
            }
            if set(candidate.get("support_ids", [])) - landed_supports:
                raise WorkflowError(
                    f"{lane} candidate {candidate_id} loses supporting evidence"
                )

    _string_list(discovery.get("friction_notes"), label=f"{lane} friction_notes")


def _semantic_inventory_record(
    semantic_ref: str,
    kind: str,
    source: Any,
    *,
    source_summary: Any | None = None,
) -> dict[str, Any]:
    record = {
        "semantic_ref": semantic_ref,
        "kind": kind,
        "source_sha256": v3._sha256_json(source),
        "source_summary": copy.deepcopy(
            source if source_summary is None else source_summary
        ),
    }
    _assert_byte_limit(
        _canonical_json_bytes(record),
        limit=MAX_SEMANTIC_RECORD_BYTES,
        label=f"semantic record {semantic_ref}",
    )
    return record


def _finding_semantic_inventory(
    finding: dict[str, Any], packet: dict[str, Any]
) -> list[dict[str, Any]]:
    """Carry every prose-relevant source through each rewrite boundary."""
    inventory = [
        _semantic_inventory_record(f"discovery:{field}", "discovery_field", {
            "field": field,
            "value": finding[field],
        })
        for field in ("claim", "mechanism", "reader_payoff", "containment")
    ]
    obligation_map = {
        row["obligation_ref"]: row
        for candidate in packet.get("candidate_inventory", [])
        if isinstance(candidate, dict)
        for row in candidate.get("semantic_obligations", [])
        if isinstance(row, dict) and isinstance(row.get("obligation_ref"), str)
    }
    for obligation_ref in finding.get("semantic_obligation_refs", []):
        obligation = obligation_map.get(obligation_ref)
        if obligation is None:
            raise WorkflowError(
                f"Finding {finding.get('finding_ref')} cites unavailable semantic "
                f"obligation {obligation_ref}"
            )
        inventory.append(
            _semantic_inventory_record(
                f"obligation:{obligation_ref}",
                "semantic_obligation",
                obligation,
            )
        )
    for index, activation in enumerate(finding.get("branch_activations", [])):
        inventory.append(
            _semantic_inventory_record(
                f"activation:{index}", "branch_activation", activation
            )
        )
    connection_map = {
        row["connection_ref"]: row
        for row in packet.get("connection_registry", [])
        if isinstance(row, dict) and isinstance(row.get("connection_ref"), str)
    }
    for connection_ref in finding.get("connection_refs", []):
        connection = connection_map.get(connection_ref)
        if connection is None:
            raise WorkflowError(
                f"Finding {finding.get('finding_ref')} cites unavailable connection "
                f"{connection_ref}"
            )
        inventory.append(
            _semantic_inventory_record(
                f"connection:{connection_ref}",
                "connection",
                connection,
                source_summary={
                    key: copy.deepcopy(connection.get(key))
                    for key in (
                        "connection_ref",
                        "prior_label",
                        "note",
                        "relation_scope",
                        "target_ref",
                    )
                    if connection.get(key) not in (None, "", [], {})
                },
            )
        )
    context_support_hashes = {
        ref: v3._sha256_json(support.get("payload"))
        for support in packet.get("support_registry", [])
        if isinstance(support, dict)
        and support.get("role") == "context_unit_native_depth_evidence"
        for ref in support.get("context_refs", [])
        if isinstance(ref, str)
    }
    for context_ref in finding.get("context_refs", []):
        inventory.append(
            _semantic_inventory_record(
                f"context:{context_ref}",
                "context",
                {
                    "context_ref": context_ref,
                    "native_depth_sha256": context_support_hashes.get(context_ref),
                },
            )
        )
    semantic_refs = [row["semantic_ref"] for row in inventory]
    if len(semantic_refs) != len(set(semantic_refs)):
        raise WorkflowError(
            f"Finding {finding.get('finding_ref')} has duplicate semantic records"
        )
    return inventory


def _validate_semantic_landings(
    value: Any,
    *,
    inventory: list[dict[str, Any]],
    prose: str,
    label: str,
) -> None:
    if not isinstance(value, list) or not value:
        raise WorkflowError(f"{label} must be a nonempty array")
    expected_order = [row["semantic_ref"] for row in inventory]
    expected_refs = set(expected_order)
    actual_order: list[str] = []
    spans: list[tuple[int, int, str, str, str]] = []
    seen_quotes: set[str] = set()
    for index, landing in enumerate(value):
        row_label = f"{label}[{index}]"
        if not isinstance(landing, dict) or set(landing) != {
            "semantic_refs", "prose_quote"
        }:
            raise WorkflowError(f"{row_label} fields are malformed")
        refs = _string_list(
            landing.get("semantic_refs"), label=f"{row_label}.semantic_refs"
        )
        if any(ref not in expected_refs for ref in refs):
            raise WorkflowError(f"{row_label} cites an unknown semantic record")
        actual_order.extend(refs)
        quote = _assert_unique_quote(
            prose,
            landing.get("prose_quote"),
            label=f"{row_label}.prose_quote",
        )
        _assert_reader_prose_is_turkish(
            quote, label=f"{row_label}.prose_quote"
        )
        if quote in seen_quotes:
            raise WorkflowError(f"{label} reuses a prose quote")
        seen_quotes.add(quote)
        start = prose.index(quote)
        spans.append((start, start + len(quote), label, "semantic", quote))
    if actual_order != expected_order:
        raise WorkflowError(f"{label} semantic coverage is incomplete or reordered")
    _assert_disjoint_quote_spans(spans, label=label)


def _validate_scope_composition(
    contribution: dict[str, Any],
    *,
    layout: Layout,
    manifest: dict[str, Any],
    lane: str,
    discovery: dict[str, Any],
    packet: dict[str, Any],
) -> None:
    expected_top_level = {
        "schema_version", "identity", "ayah_ref", "lane", "findings", "friction_notes"
    }
    if set(contribution) != expected_top_level:
        raise WorkflowError(f"{lane} composition top-level fields are malformed")
    if contribution.get("schema_version") != SCOPE_COMPOSITION_SCHEMA_VERSION:
        raise WorkflowError(f"{lane} composition schema_version is stale")
    record = manifest["lanes"][lane].get("composition")
    if not isinstance(record, dict):
        raise WorkflowError(f"Manifest has no {lane} composition request")
    expected_identity = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": manifest["lanes"][lane]["lane_packet_sha256"],
        "discovery_sha256": v3._sha256_json(discovery),
        "authoring_request_sha256": record["request_sha256"],
    }
    if contribution.get("identity") != expected_identity:
        raise WorkflowError(f"{lane} composition identity is stale or mixed")
    if contribution.get("ayah_ref") != layout.ayah_ref or contribution.get("lane") != lane:
        raise WorkflowError(f"{lane} composition focus/lane is malformed")
    raw_rows = contribution.get("findings")
    if not isinstance(raw_rows, list):
        raise WorkflowError(f"{lane} composition findings must be an array")
    discovery_rows = discovery["findings"]
    if [row.get("finding_ref") for row in raw_rows if isinstance(row, dict)] != [
        row["finding_ref"] for row in discovery_rows
    ]:
        raise WorkflowError(f"{lane} composition finding order/identity is incomplete")
    expected_fields = {
        "finding_ref",
        "prose",
        "semantic_landings",
    }
    for index, (row, source) in enumerate(zip(raw_rows, discovery_rows, strict=True)):
        label = f"{lane} composition findings[{index}]"
        if not isinstance(row, dict) or set(row) != expected_fields:
            raise WorkflowError(f"{label} fields are malformed")
        prose = _required_text(row.get("prose"), label=f"{label}.prose")
        _assert_reader_prose_is_turkish(prose, label=f"{label}.prose")
        _validate_semantic_landings(
            row.get("semantic_landings"),
            inventory=_finding_semantic_inventory(source, packet),
            prose=prose,
            label=f"{label}.semantic_landings",
        )
    _string_list(contribution.get("friction_notes"), label=f"{lane} friction_notes")


def _load_discovery(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any] | None:
    path = layout.scope_discovery(lane)
    if not path.exists():
        return None
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"{lane} discovery is not a regular file: {path}")
    discovery = _load_json(path, max_bytes=MAX_DISCOVERY_JSON_BYTES)
    packet = _load_json(layout.packet(lane))
    _validate_scope_discovery(
        discovery,
        layout=layout,
        manifest=manifest,
        lane=lane,
        packet=packet,
    )
    return discovery


def _ensure_scope_composition(
    layout: Layout,
    manifest: dict[str, Any],
    lane: str,
    packet: dict[str, Any],
    discovery: dict[str, Any],
    *,
    write: bool = True,
) -> dict[str, Any]:
    discovery_bytes, on_disk_discovery = _load_json_with_bytes(
        layout.scope_discovery(lane), max_bytes=MAX_DISCOVERY_JSON_BYTES
    )
    if on_disk_discovery != discovery:
        raise WorkflowError(f"{lane} discovery changed while composing its handoff")
    discovery_record = {
        "path": _repo_path(layout.scope_discovery(lane)),
        "bytes": len(discovery_bytes),
        "sha256": _sha256(discovery_bytes),
    }
    prompt, base_record = _build_composition_prompt(
        layout, lane, packet, discovery
    )
    existing_output = layout.scope_contribution(lane).exists()
    current = manifest["lanes"][lane].get("composition")
    if current is None:
        if existing_output:
            raise WorkflowError(
                f"{lane} composition exists without a hash-bound request"
            )
        if not write:
            raise WorkflowError(f"Manifest has no {lane} composition request")
        _write_generated(
            layout.composition_prompt(lane),
            prompt.encode("utf-8"),
            replace_changed=True,
            root=INPUT_ROOT,
        )
        current = {
            **base_record,
            "prompt": _path_record(layout.composition_prompt(lane)),
            "discovery": discovery_record,
            "expected_response": _repo_path(layout.scope_contribution(lane)),
        }
        manifest["lanes"][lane]["composition"] = current
        _write_generated(
            layout.manifest,
            _pretty_json_bytes(manifest),
            replace_changed=True,
            root=INPUT_ROOT,
        )
    elif not isinstance(current, dict):
        raise WorkflowError(f"Manifest {lane} composition request is malformed")
    expected = {
        **base_record,
        "prompt": _path_record(layout.composition_prompt(lane)),
        "discovery": discovery_record,
        "expected_response": _repo_path(layout.scope_contribution(lane)),
    }
    if current != expected:
        raise WorkflowError(f"Manifest {lane} composition request is stale")
    if layout.composition_prompt(lane).read_text(encoding="utf-8") != prompt:
        raise WorkflowError(f"{lane} composition prompt content is stale")
    return current


def _load_contribution(
    layout: Layout,
    manifest: dict[str, Any],
    lane: str,
    discovery: dict[str, Any] | None = None,
    packet: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    path = layout.scope_contribution(lane)
    if not path.exists():
        return None
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"{lane} contribution is not a regular file: {path}")
    if discovery is None:
        discovery = _load_discovery(layout, manifest, lane)
    if discovery is None:
        raise WorkflowError(f"{lane} composition exists without discovery")
    if packet is None:
        packet = _load_json(layout.packet(lane))
    contribution = _load_json(path, max_bytes=MAX_COMPOSITION_JSON_BYTES)
    _validate_scope_composition(
        contribution,
        layout=layout,
        manifest=manifest,
        lane=lane,
        discovery=discovery,
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


def _merge_scope_results(
    discoveries: dict[str, dict[str, Any]],
    compositions_by_lane: dict[str, dict[str, Any]],
    packets: dict[str, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        discovery = discoveries[lane]
        composition = compositions_by_lane[lane]
        prose_by_ref = {
            row["finding_ref"]: row for row in composition["findings"]
        }
        merged_findings = []
        for finding in discovery["findings"]:
            composition_row = prose_by_ref[finding["finding_ref"]]
            merged_findings.append({
                **copy.deepcopy(finding),
                "prose": composition_row["prose"],
                "semantic_inventory": _finding_semantic_inventory(
                    finding, packets[lane]
                ),
                "composition_semantic_landings": copy.deepcopy(
                    composition_row["semantic_landings"]
                ),
            })
        merged[lane] = {
            "lane": lane,
            "candidate_decisions": copy.deepcopy(
                discovery["candidate_decisions"]
            ),
            "findings": merged_findings,
            "friction_notes": list(dict.fromkeys([
                *discovery["friction_notes"],
                *composition["friction_notes"],
            ])),
        }
    return merged


def _ordered_findings(
    contributions: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    seen: set[str] = set()
    for lane in LANES:
        lane_findings = contributions.get(lane, {}).get("findings")
        if not isinstance(lane_findings, list):
            raise WorkflowError(f"{lane} contribution findings are malformed")
        for finding in lane_findings:
            if not isinstance(finding, dict):
                raise WorkflowError(f"{lane} contribution contains a malformed finding")
            finding_ref = finding.get("finding_ref")
            if not isinstance(finding_ref, str) or finding_ref in seen:
                raise WorkflowError(
                    f"Canonical finding identity is missing or duplicated: {finding_ref}"
                )
            seen.add(finding_ref)
            findings.append(finding)
    return findings


def _finding_apparatus_ledger(
    contributions: dict[str, dict[str, Any]], finding: dict[str, Any]
) -> dict[str, Any]:
    finding_ref = finding["finding_ref"]
    decisions = [
        copy.deepcopy(decision)
        for lane in LANES
        for decision in contributions[lane].get("candidate_decisions", [])
        if isinstance(decision, dict)
        and finding_ref in decision.get("finding_refs", [])
    ]
    source_record = {
        "finding": {
            key: copy.deepcopy(value)
            for key, value in finding.items()
            if key != "prose"
        },
        "candidate_decisions": decisions,
    }
    inventory = finding.get("semantic_inventory", [])
    return {
        "schema_version": FINDING_PROVENANCE_SCHEMA_VERSION,
        "finding_ref": finding_ref,
        "lane": finding_ref.split(":", 1)[0],
        "source_record_sha256": v3._sha256_json(source_record),
        "candidate_decision_sha256s": [
            v3._sha256_json(decision) for decision in decisions
        ],
        "support_ids": copy.deepcopy(finding.get("support_ids", [])),
        "branch_facets": [
            {
                "branch_ref": row.get("branch_ref"),
                "facet_id": row.get("facet_id"),
            }
            for row in finding.get("branch_activations", [])
            if isinstance(row, dict)
        ],
        "connection_refs": copy.deepcopy(finding.get("connection_refs", [])),
        "context_refs": copy.deepcopy(finding.get("context_refs", [])),
        "semantic_records": [
            {
                "semantic_ref": row.get("semantic_ref"),
                "source_sha256": row.get("source_sha256"),
            }
            for row in inventory
            if isinstance(row, dict)
        ],
    }


def _prune_empty_semantic_values(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: compacted
            for key, item in value.items()
            if item not in (None, "", [], {})
            for compacted in [_prune_empty_semantic_values(item)]
            if compacted not in (None, "", [], {})
        }
    if isinstance(value, list):
        return [
            compacted
            for item in value
            for compacted in [_prune_empty_semantic_values(item)]
            if compacted not in (None, "", [], {})
        ]
    return copy.deepcopy(value)


def _compact_prefatory_semantic_payload(section: Any, value: Any) -> Any:
    """Remove metadata only where the prefatory evidence schema defines it."""
    compacted = copy.deepcopy(value)
    if section in {"v12_reader_walks", "v12_reader_walks_wide"} and isinstance(
        compacted, dict
    ):
        for reader in compacted.values():
            if isinstance(reader, dict):
                reader.pop("source_file", None)
    elif section == "v12_cross_run_publication" and isinstance(compacted, dict):
        for field in ("language", "protocol", "source_file"):
            compacted.pop(field, None)
    elif section == "channel_generated_outputs" and isinstance(compacted, dict):
        for field in ("files", "source_dir"):
            compacted.pop(field, None)
    return _prune_empty_semantic_values(compacted)


def _agent_semantic_requirement(row: dict[str, Any]) -> dict[str, Any]:
    """Strip rewrite-irrelevant provenance while retaining exact semantics."""
    semantic_ref = row["semantic_ref"]
    kind = row["kind"]
    source = row["source_summary"]
    if kind == "discovery_field":
        requirement = source.get("value") if isinstance(source, dict) else source
    elif kind == "semantic_obligation" and isinstance(source, dict):
        requirement = {
            field: copy.deepcopy(source[field])
            for field in (
                "kind",
                "section",
                "semantic_claim",
                "before",
                "after",
                "branch_ref",
                "source_ref",
                "source_word_indices",
            )
            if source.get(field) not in (None, "", [], {})
        }
        if source.get("semantic_payload") not in (None, "", [], {}):
            requirement["semantic_payload"] = _compact_prefatory_semantic_payload(
                source.get("section"),
                source["semantic_payload"],
            )
    elif kind == "branch_activation" and isinstance(source, dict):
        requirement = {
            field: copy.deepcopy(source[field])
            for field in (
                "branch_gloss",
                "facet_statement",
                "application_mode",
                "carrier_refs",
                "trigger_refs",
                "focus_return_refs",
                "carrier",
                "independent_trigger",
                "activation",
                "resulting_reading",
                "boundary",
            )
            if source.get(field) not in (None, "", [], {})
        }
    elif kind == "connection" and isinstance(source, dict):
        requirement = {
            field: copy.deepcopy(source[field])
            for field in (
                "prior_label",
                "note",
                "relation_scope",
                "target_ref",
            )
            if source.get(field) not in (None, "", [], {})
        }
    elif kind == "context" and isinstance(source, dict):
        requirement = {"context_ref": source.get("context_ref")}
    else:
        raise WorkflowError(
            f"Unsupported canonical semantic requirement kind: {kind!r}"
        )
    return {
        "semantic_ref": semantic_ref,
        "kind": kind,
        "requirement": requirement,
    }


def _canonical_lane_payload(
    contribution: dict[str, Any],
) -> dict[str, Any]:
    """Project only prose-relevant findings into the canonical handoff."""
    return {
        "lane": contribution["lane"],
        "findings": [
            {
                "finding_ref": finding["finding_ref"],
                "title": copy.deepcopy(finding.get("title")),
                "epistemic": copy.deepcopy(finding.get("epistemic")),
                "prose": finding["prose"],
                "semantic_requirements": [
                    _agent_semantic_requirement(row)
                    for row in finding["semantic_inventory"]
                ],
            }
            for finding in contribution["findings"]
        ],
        "friction_notes": copy.deepcopy(contribution.get("friction_notes", [])),
    }


def _validate_semantic_statement_set(
    contributions: dict[str, dict[str, Any]],
) -> None:
    for finding in _ordered_findings(contributions):
        finding_ref = finding["finding_ref"]
        prose = _required_text(
            finding.get("prose"), label=f"{finding_ref}.prose"
        )
        _assert_reader_prose_is_turkish(prose, label=f"{finding_ref}.prose")
        inventory = finding.get("semantic_inventory")
        if not isinstance(inventory, list) or not inventory or any(
            not isinstance(row, dict)
            or set(row) != {
                "semantic_ref", "kind", "source_sha256", "source_summary"
            }
            for row in inventory
        ):
            raise WorkflowError(f"{finding_ref} semantic inventory is malformed")
        semantic_refs = [row.get("semantic_ref") for row in inventory]
        if (
            not all(isinstance(ref, str) and ref for ref in semantic_refs)
            or len(semantic_refs) != len(set(semantic_refs))
        ):
            raise WorkflowError(
                f"{finding_ref} semantic inventory identity is malformed"
            )
        _validate_semantic_landings(
            finding.get("composition_semantic_landings"),
            inventory=inventory,
            prose=prose,
            label=f"{finding_ref}.composition_semantic_landings",
        )


def _parse_landing_map(
    index_text: str, *, ayah_ref: str, phase: str
) -> tuple[dict[str, Any], str]:
    matches = list(LANDING_MAP_BLOCK_RE.finditer(index_text))
    if len(matches) != 1:
        raise WorkflowError(
            f"{phase} findings index must contain exactly one landing-map block"
        )
    match = matches[0]
    if index_text[match.end():].strip():
        raise WorkflowError(f"{phase} landing-map block must be last in the index")
    try:
        landing_map = json.loads(match.group("payload"))
    except json.JSONDecodeError as exc:
        raise WorkflowError(f"{phase} landing map is invalid JSON: {exc}") from exc
    expected_fields = {"schema_version", "ayah_ref", "phase", "findings"}
    if not isinstance(landing_map, dict) or set(landing_map) != expected_fields:
        raise WorkflowError(f"{phase} landing map fields are malformed")
    if (
        landing_map.get("schema_version") != CANONICAL_LANDING_MAP_SCHEMA_VERSION
        or landing_map.get("ayah_ref") != ayah_ref
        or landing_map.get("phase") != phase
    ):
        raise WorkflowError(f"{phase} landing map identity is stale or mixed")
    index_without_map = index_text[:match.start()] + index_text[match.end():]
    return landing_map, index_without_map


def _assert_unique_quote(
    text: str,
    quote: Any,
    *,
    label: str,
    minimum_length: int = MIN_LANDING_QUOTE_CHARS,
) -> str:
    value = _required_text(quote, label=label)
    if len(value.strip()) < minimum_length:
        raise WorkflowError(f"{label} is too short to be a stable landing anchor")
    if text.count(value) != 1:
        raise WorkflowError(f"{label} must occur exactly once in its output")
    return value


def _assert_disjoint_quote_spans(
    spans: list[tuple[int, int, str, str, str]], *, label: str
) -> None:
    for index, left in enumerate(spans):
        left_start, left_end, left_finding, left_role, left_value = left
        for right in spans[index + 1:]:
            right_start, right_end, right_finding, right_role, right_value = right
            if left_end <= right_start or right_end <= left_start:
                continue
            same_finding_dual_role = (
                left_value == right_value
                and left_finding == right_finding
                and {left_role, right_role} == {"finding", "activation"}
            )
            if same_finding_dual_role:
                continue
            raise WorkflowError(
                f"{label} reuses an overlapping span for "
                f"{left_finding}/{left_role} and {right_finding}/{right_role}"
            )


def _validate_canonical_outputs(
    layout: Layout,
    contributions: dict[str, dict[str, Any]],
    *,
    phase: str,
) -> None:
    if phase == "raw":
        paths = {kind: layout.first_pass(kind) for kind in KINDS}
    elif phase == "editorial":
        paths = {kind: layout.editorial_output(kind) for kind in KINDS}
    else:
        raise WorkflowError(f"Unknown canonical output phase: {phase}")
    texts: dict[str, str] = {}
    for kind, path in paths.items():
        if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
            raise WorkflowError(f"Missing or empty {phase} {kind}: {path}")
        limit = CANONICAL_OUTPUT_BYTE_LIMITS[kind]
        if path.stat().st_size > limit:
            raise WorkflowError(
                f"{phase} {kind} exceeds the {limit}-byte output budget: {path}"
            )
        try:
            texts[kind] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise WorkflowError(f"{phase} {kind} is not UTF-8: {path}") from exc
    _assert_reader_prose_is_turkish(
        texts["prose"], label=f"{phase} reader prose"
    )

    _validate_semantic_statement_set(contributions)
    findings = _ordered_findings(contributions)
    expected_refs = [finding["finding_ref"] for finding in findings]
    landing_map, index_without_map = _parse_landing_map(
        texts["index"], ayah_ref=layout.ayah_ref, phase=phase
    )
    rows = landing_map.get("findings")
    if not isinstance(rows, list):
        raise WorkflowError(f"{phase} landing map findings must be an array")
    expected_row_fields = {
        "finding_ref",
        "semantic_landings",
        "evidence_quote",
        "index_quote",
        "provenance_sha256",
    }
    actual_refs = [
        row.get("finding_ref") if isinstance(row, dict) else None for row in rows
    ]
    if actual_refs != expected_refs:
        raise WorkflowError(
            f"{phase} landing map finding order or coverage is incomplete"
        )

    evidence_quotes: set[str] = set()
    index_quotes: set[str] = set()
    evidence_spans: list[tuple[int, int, str, str, str]] = []
    index_spans: list[tuple[int, int, str, str, str]] = []
    evidence_without_ledgers = texts["evidence"]
    for finding, row in zip(findings, rows):
        finding_ref = finding["finding_ref"]
        label = f"{phase} landing map {finding_ref}"
        if not isinstance(row, dict) or set(row) != expected_row_fields:
            raise WorkflowError(f"{label} fields are malformed")
        inventory = finding.get("semantic_inventory")
        if not isinstance(inventory, list):
            raise WorkflowError(f"{label} has no validated semantic inventory")
        _validate_semantic_landings(
            row.get("semantic_landings"),
            inventory=inventory,
            prose=texts["prose"],
            label=f"{label}.semantic_landings",
        )
        evidence_quote = _assert_unique_quote(
            texts["evidence"],
            row.get("evidence_quote"),
            label=f"{label}.evidence_quote",
        )
        index_quote = _assert_unique_quote(
            index_without_map,
            row.get("index_quote"),
            label=f"{label}.index_quote",
        )
        evidence_start = texts["evidence"].index(evidence_quote)
        index_start = index_without_map.index(index_quote)
        evidence_spans.append((
            evidence_start,
            evidence_start + len(evidence_quote),
            finding_ref,
            "apparatus",
            evidence_quote,
        ))
        index_spans.append((
            index_start,
            index_start + len(index_quote),
            finding_ref,
            "apparatus",
            index_quote,
        ))
        if finding_ref not in evidence_quote or finding_ref not in index_quote:
            raise WorkflowError(
                f"{label} apparatus quotes must include the exact finding_ref"
            )
        provenance_ledger = _finding_apparatus_ledger(contributions, finding)
        expected_ledger = v3._canonical_json(provenance_ledger)
        provenance_sha256 = provenance_ledger["source_record_sha256"]
        if row.get("provenance_sha256") != provenance_sha256:
            raise WorkflowError(f"{label}.provenance_sha256 is stale")
        if expected_ledger not in evidence_quote:
            raise WorkflowError(
                f"{label} evidence omits or alters the compact provenance ledger"
            )
        if provenance_sha256 not in index_quote:
            raise WorkflowError(f"{label} index omits the provenance hash")
        if (
            texts["evidence"].count(expected_ledger) != 1
            or expected_ledger in index_without_map
            or index_without_map.count(provenance_sha256) != 1
        ):
            raise WorkflowError(
                f"{label} compact provenance must occur once in evidence and "
                "only its hash once in the index"
            )
        evidence_without_ledgers = evidence_without_ledgers.replace(
            expected_ledger, ""
        )
        for quote, seen, quote_label in (
            (evidence_quote, evidence_quotes, "evidence_quote"),
            (index_quote, index_quotes, "index_quote"),
        ):
            if quote in seen:
                raise WorkflowError(f"{phase} landing map reuses a {quote_label}")
            seen.add(quote)

    _assert_disjoint_quote_spans(evidence_spans, label=f"{phase} evidence")
    _assert_disjoint_quote_spans(index_spans, label=f"{phase} findings index")
    _assert_no_obvious_english(
        evidence_without_ledgers, label=f"{phase} evidence prose"
    )
    _assert_no_obvious_english(
        index_without_map, label=f"{phase} findings-index prose"
    )
    _assert_no_obvious_english(
        texts["friction"], label=f"{phase} friction prose"
    )


def _build_canonical_prompt(
    layout: Layout,
    manifest: dict[str, Any],
    contributions: dict[str, dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    _validate_semantic_statement_set(contributions)
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
    apparatus_ledgers = [
        _finding_apparatus_ledger(contributions, finding)
        for finding in _ordered_findings(contributions)
    ]
    apparatus_ledgers_json = v3._canonical_json(apparatus_ledgers)
    canonical_lane_payloads = {
        lane: _canonical_lane_payload(contributions[lane]) for lane in LANES
    }
    canonical_lane_json = {
        lane: v3._canonical_json(canonical_lane_payloads[lane]) for lane in LANES
    }
    replacements = {
        "@@AYAH_REF@@": layout.ayah_ref,
        "@@PROSE_OUTPUT_PATH@@": _repo_path(layout.first_pass("prose")),
        "@@EVIDENCE_OUTPUT_PATH@@": _repo_path(layout.first_pass("evidence")),
        "@@INDEX_OUTPUT_PATH@@": _repo_path(layout.first_pass("index")),
        "@@FRICTION_OUTPUT_PATH@@": _repo_path(layout.first_pass("friction")),
        "@@LANDING_MAP_SCHEMA_VERSION@@": CANONICAL_LANDING_MAP_SCHEMA_VERSION,
        "@@PRINCIPLES_MD@@": governing["principles"],
        "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
        "@@CHANNELS_MD@@": governing["channels"],
        "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
        "@@FOCUS_SURFACE_SHA256@@": focus_surface_sha256,
        "@@FOCUS_SURFACE_JSON@@": focus_surface_bytes.decode("utf-8"),
        "@@APPARATUS_LEDGERS_JSON@@": apparatus_ledgers_json,
        "@@MICRO_FINDINGS_JSON@@": canonical_lane_json["micro"],
        "@@MACRO_FINDINGS_JSON@@": canonical_lane_json["macro"],
        "@@GLOBAL_FINDINGS_JSON@@": canonical_lane_json["global"],
    }
    prompt = _render(template, replacements, label="canonical prompt")
    prompt_bytes = prompt.encode("utf-8")
    _assert_byte_limit(
        prompt_bytes,
        limit=MAX_CANONICAL_PROMPT_BYTES,
        label="canonical prompt",
    )
    contribution_records = {
        lane: _path_record(layout.scope_contribution(lane)) for lane in LANES
    }
    discovery_records = {
        lane: _path_record(layout.scope_discovery(lane)) for lane in LANES
    }
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "template_sha256": _sha256(template.encode("utf-8")),
        "focus_surface_sha256": focus_surface_sha256,
        "apparatus_ledgers_sha256": _sha256(
            apparatus_ledgers_json.encode("utf-8")
        ),
        **{
            f"{lane}_canonical_projection_sha256": _sha256(
                canonical_lane_json[lane].encode("utf-8")
            )
            for lane in LANES
        },
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
        **{
            f"{lane}_discovery_sha256": discovery_records[lane]["sha256"]
            for lane in LANES
        },
    }
    canonical_record = {
        "request_sha256": v3._request_sha256(
            "v5-canonical-merge", request_inputs
        ),
        "prompt": {
            "path": _repo_path(layout.canonical_prompt),
            "bytes": len(prompt_bytes),
            "sha256": _sha256(prompt_bytes),
        },
        "inputs": request_inputs,
        "contributions": contribution_records,
        "discoveries": discovery_records,
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
                "the current Git state, clear or relocate the stale v5 outputs, and "
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
        "@@LANDING_MAP_SCHEMA_VERSION@@": CANONICAL_LANDING_MAP_SCHEMA_VERSION,
        "@@EDITORIAL_INSTRUCTIONS@@": instructions,
    }
    prompt = _render(template, replacements, label="editorial handoff")
    prompt_bytes = prompt.encode("utf-8")
    _assert_byte_limit(
        prompt_bytes,
        limit=MAX_EDITORIAL_PROMPT_BYTES,
        label="editorial handoff",
    )
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
            "v5-canonical-editorial", request_inputs
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


def _discovery_handoff(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any]:
    return {
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "role": f"{lane}_scope_discoverer",
        "fresh_agent": True,
        "prompt": str(layout.discovery_prompt(lane).resolve()),
        "expected_response": _handoff_output_path(
            layout.scope_discovery(lane),
            RAW_ROOT,
            label=f"{lane} discovery target",
        ),
        "workspace": str(REPO_ROOT),
        "request_sha256": manifest["lanes"][lane]["discovery"][
            "request_sha256"
        ],
    }


def _composition_handoff(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any]:
    record = manifest["lanes"][lane]["composition"]
    return {
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "role": f"{lane}_scope_composer",
        "same_live_agent": True,
        "replacement_agent_allowed": True,
        "prompt": str(layout.composition_prompt(lane).resolve()),
        "discovery": str(layout.scope_discovery(lane).resolve()),
        "expected_response": _handoff_output_path(
            layout.scope_contribution(lane),
            RAW_ROOT,
            label=f"{lane} composition target",
        ),
        "workspace": str(REPO_ROOT),
        "request_sha256": record["request_sha256"],
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
                f"python3 _commentary/v5/workflow.py advance "
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
            *(layout.scope_discovery(lane).name for lane in LANES),
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
                f"Unexpected v5 output artifacts in {root}: {unexpected}. "
                "Preserve, remove, or relocate them explicitly before advancing."
            )


def advance(args: argparse.Namespace) -> dict[str, Any]:
    layout = _layout_for_args(args)
    _assert_layout(layout)
    if args.force_input or not layout.manifest.exists():
        prepare(args)
    manifest = _load_unit_manifest(layout)
    _assert_fixed_output_names(layout)
    discoveries: dict[str, dict[str, Any]] = {}
    missing_discoveries: list[str] = []
    invalid_lanes: dict[str, str] = {}
    for lane in LANES:
        try:
            discovery = _load_discovery(layout, manifest, lane)
        except WorkflowError as exc:
            discovery = None
            invalid_lanes[lane] = str(exc)
        if discovery is None:
            missing_discoveries.append(lane)
        else:
            discoveries[lane] = discovery
    if invalid_lanes:
        details = "; ".join(
            f"{lane}: {issue}" for lane, issue in sorted(invalid_lanes.items())
        )
        raise WorkflowError(
            "Invalid scope discovery. V5 does not issue automated repair turns; "
            "inspect, remove, or replace the failed artifact explicitly before "
            f"advancing again. {details}"
        )
    if missing_discoveries:
        return {
            "schema_version": "commentary-v5-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agents",
            "stage": "scope_discovery",
            "missing_lanes": missing_discoveries,
            "handoffs": [
                _discovery_handoff(layout, manifest, lane)
                for lane in missing_discoveries
            ],
        }

    compositions_by_lane: dict[str, dict[str, Any]] = {}
    packets: dict[str, dict[str, Any]] = {}
    missing_compositions: list[str] = []
    invalid_lanes = {}
    for lane in LANES:
        packet = _load_json(layout.packet(lane))
        packets[lane] = packet
        _ensure_scope_composition(
            layout, manifest, lane, packet, discoveries[lane]
        )
        try:
            contribution = _load_contribution(
                layout, manifest, lane, discoveries[lane], packet
            )
        except WorkflowError as exc:
            contribution = None
            invalid_lanes[lane] = str(exc)
        if contribution is None:
            missing_compositions.append(lane)
        else:
            compositions_by_lane[lane] = contribution
    if invalid_lanes:
        details = "; ".join(
            f"{lane}: {issue}" for lane, issue in sorted(invalid_lanes.items())
        )
        raise WorkflowError(
            "Invalid scope composition. V5 does not issue automated repair turns; "
            "inspect, remove, or replace the failed artifact explicitly before "
            f"advancing again. {details}"
        )
    if missing_compositions:
        return {
            "schema_version": "commentary-v5-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agents",
            "stage": "scope_composition",
            "missing_lanes": missing_compositions,
            "handoffs": [
                _composition_handoff(layout, manifest, lane)
                for lane in missing_compositions
            ],
        }

    contributions = _merge_scope_results(
        discoveries, compositions_by_lane, packets
    )

    canonical = _ensure_canonical(layout, manifest, contributions)
    first_pass_paths = {kind: layout.first_pass(kind) for kind in KINDS}
    first_present, first_missing = _nonempty_outputs(first_pass_paths)
    if first_missing:
        return {
            "schema_version": "commentary-v5-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agent",
            "stage": "canonical_write",
            "present_outputs": first_present,
            "missing_outputs": first_missing,
            "handoff": _canonical_handoff(layout, canonical),
        }

    _validate_canonical_outputs(layout, contributions, phase="raw")
    editorial_turn = _ensure_editorial(layout, manifest, canonical)
    editorial_paths = {kind: layout.editorial_output(kind) for kind in KINDS}
    editorial_present, editorial_missing = _nonempty_outputs(editorial_paths)
    if editorial_missing:
        return {
            "schema_version": "commentary-v5-status-v1",
            "analysis_id": layout.analysis_id,
            "ayah_ref": args.ayah,
            "status": "waiting_for_agent",
            "stage": "canonical_editorial",
            "present_outputs": editorial_present,
            "missing_outputs": editorial_missing,
            "handoff": _editorial_handoff(layout, editorial_turn),
        }
    _validate_canonical_outputs(layout, contributions, phase="editorial")
    return verify(args)


def verify(args: argparse.Namespace) -> dict[str, Any]:
    layout = _layout_for_args(args)
    _assert_layout(layout)
    manifest = _load_unit_manifest(layout)
    _assert_fixed_output_names(layout)
    discoveries: dict[str, dict[str, Any]] = {}
    compositions_by_lane: dict[str, dict[str, Any]] = {}
    packets: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        discovery = _load_discovery(layout, manifest, lane)
        if discovery is None:
            raise WorkflowError(f"Missing {lane} scope discovery")
        discoveries[lane] = discovery
        packet = _load_json(layout.packet(lane))
        packets[lane] = packet
        _ensure_scope_composition(
            layout, manifest, lane, packet, discovery, write=False
        )
        contribution = _load_contribution(
            layout, manifest, lane, discovery, packet
        )
        if contribution is None:
            raise WorkflowError(f"Missing {lane} scope contribution")
        compositions_by_lane[lane] = contribution
    contributions = _merge_scope_results(
        discoveries, compositions_by_lane, packets
    )
    canonical = _ensure_canonical(
        layout, manifest, contributions, write=False
    )
    _validate_canonical_outputs(layout, contributions, phase="raw")
    _ensure_editorial(layout, manifest, canonical, write=False)
    _validate_canonical_outputs(layout, contributions, phase="editorial")
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
        "schema_version": "commentary-v5-status-v1",
        "analysis_id": layout.analysis_id,
        "ayah_ref": args.ayah,
        "status": "complete",
        "mechanical_validation": "candidate_accounting_and_hash_bound_quote_mapping",
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
                "schema_version": "commentary-v5-error-v1",
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
            "schema_version": "commentary-v5-batch-status-v1",
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
        description="Prepare and advance the two-stage commentary v5 workflow."
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
        "verify", help="Check complete lineage and all final output artifacts."
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
                    "schema_version": "commentary-v5-error-v1",
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
