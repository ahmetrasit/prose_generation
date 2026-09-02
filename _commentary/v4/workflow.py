#!/usr/bin/env python3
"""A fixed, Git-native commentary workflow with no persisted agent sessions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


V4_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V4_ROOT.parents[1]
V3_ROOT = V4_ROOT.parent / "v3"
V3_PROMPTS_ROOT = V3_ROOT / "prompts"
PROMPTS_ROOT = V4_ROOT / "prompts"
INPUT_ROOT = V4_ROOT / "input"
RAW_ROOT = V4_ROOT / "raw"
EDITORIAL_ROOT = V4_ROOT / "editorial"
LANES = ("micro", "macro", "global")
KINDS = ("prose", "evidence", "index", "friction")
MAX_JSON_BYTES = 128_000_000
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
AYAH_SELECTOR_RE = re.compile(
    r"([1-9][0-9]*):(0|[1-9][0-9]*)(?:-([1-9][0-9]*))?"
)
MAX_BATCH_UNITS = 512

# Reuse v3's evidence projection and exact request identity. The orchestration
# state machine is deliberately not imported or called.
sys.path.insert(0, str(V3_ROOT))
import render_authoring as v3  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402
from v3lib.prepare import validate_docket  # noqa: E402


class WorkflowError(RuntimeError):
    """Raised for a stale, mixed, or malformed v4 artifact set."""


@dataclass(frozen=True)
class Layout:
    ayah_ref: str
    stem: str
    input: Path
    raw: Path
    editorial: Path

    def packet(self, lane: str) -> Path:
        return self.input / f"{lane}.packet.json"

    def scope_prompt(self, lane: str) -> Path:
        return self.input / f"{lane}.prompt.md"

    def scope_review(self, lane: str) -> Path:
        return self.raw / f"{lane}.review.json"

    @property
    def source_bundle(self) -> Path:
        return self.input / "source.bundle.json"

    @property
    def docket(self) -> Path:
        return self.input / "docket.json"

    @property
    def manifest(self) -> Path:
        return self.input / "manifest.json"

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


def layout_for(ayah_ref: str) -> Layout:
    match = re.fullmatch(r"([1-9][0-9]*):([1-9][0-9]*)", ayah_ref)
    if match is None:
        if re.fullmatch(r"[1-9][0-9]*:0", ayah_ref):
            raise WorkflowError(
                "Prefatory basmala units require a versioned authoring protocol; "
                "v4 currently accepts numbered ayahs only"
            )
        raise WorkflowError(f"Invalid numbered ayah reference: {ayah_ref!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    folder = f"s{surah:03d}"
    stem = f"{surah}_{ayah}"
    return Layout(
        ayah_ref=ayah_ref,
        stem=stem,
        input=INPUT_ROOT / folder / stem,
        raw=RAW_ROOT / folder / stem,
        editorial=EDITORIAL_ROOT / folder / stem,
    )


def _expand_ayah_selectors(selectors: list[str] | str) -> list[str]:
    if isinstance(selectors, str):
        selectors = [selectors]
    refs: list[str] = []
    seen: set[str] = set()
    for raw_selector in selectors:
        for selector in raw_selector.split(","):
            selector = selector.strip()
            match = AYAH_SELECTOR_RE.fullmatch(selector)
            if match is None:
                raise WorkflowError(f"Invalid ayah selector: {selector!r}")
            surah, first, last_text = match.groups()
            first_number = int(first)
            if first_number == 0 and last_text is not None:
                raise WorkflowError(
                    f"Ayah ranges may not start at prefatory unit zero: {selector}"
                )
            last_number = int(last_text or first)
            if last_number < first_number:
                raise WorkflowError(f"Descending ayah range is not allowed: {selector}")
            for ayah in range(first_number, last_number + 1):
                ref = f"{int(surah)}:{ayah}"
                if ref not in seen:
                    refs.append(ref)
                    seen.add(ref)
                if len(refs) > MAX_BATCH_UNITS:
                    raise WorkflowError(
                        f"A batch may contain at most {MAX_BATCH_UNITS} ayahs"
                    )
    if not refs:
        raise WorkflowError("At least one numbered ayah is required")
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
    if layout != layout_for(layout.ayah_ref):
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


def _source_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--docket", type=Path)
    parser.add_argument("--source-bundle", type=Path)
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
        "--force-input",
        action="store_true",
        help="Replace changed generated input files; raw/editorial files are untouched.",
    )


def _input_manifest_base(
    layout: Layout,
    source_origin: Path,
    docket_origin: Path,
    source_bundle: dict[str, Any],
    docket: dict[str, Any],
    quran_coverage: dict[str, Any],
    inter_ayah_coverage: dict[str, Any],
    lane_records: dict[str, Any],
) -> dict[str, Any]:
    canonical_template = PROMPTS_ROOT / "canonical.md"
    editorial_instructions = V3_PROMPTS_ROOT / "editorial-followup.md"
    editorial_template = PROMPTS_ROOT / "editorial.md"
    return {
        "schema_version": "commentary-v4-unit-manifest-v1",
        "ayah_ref": layout.ayah_ref,
        "layout": {
            "input": _repo_path(layout.input),
            "raw": _repo_path(layout.raw),
            "editorial": _repo_path(layout.editorial),
        },
        "source": {
            "snapshot": _path_record(layout.source_bundle),
            "origin": v3._stable_source_path(source_origin),
            "canonical_sha256": v3._sha256_json(source_bundle),
        },
        "docket": {
            "snapshot": _path_record(layout.docket),
            "origin": v3._stable_source_path(docket_origin),
            "payload_sha256": docket["identity"]["docket_payload_sha256"],
        },
        "evidence_projection": {
            "quran_text": quran_coverage,
            "inter_ayah": inter_ayah_coverage,
            "implementation": "_commentary/v3/render_authoring.py",
        },
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
    layout = layout_for(args.ayah)
    _assert_layout(layout)
    source_origin = (args.source_bundle or v3._default_source_bundle(args.ayah))
    docket_origin = (args.docket or v3._default_docket(args.ayah))
    source_payload, source_bundle = _load_json_with_bytes(source_origin)
    docket_payload, docket = _load_json_with_bytes(docket_origin)
    try:
        validate_docket(docket)
    except ValidationError as exc:
        raise WorkflowError(f"Invalid docket {docket_origin}: {exc}") from exc
    if source_bundle.get("ayahRef") != args.ayah:
        raise WorkflowError("Source bundle ayah identity does not match --ayah")
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise WorkflowError("Docket ayah identity does not match --ayah")
    if (
        v3._sha256_json(source_bundle)
        != docket.get("identity", {}).get("source_canonical_sha256")
    ):
        raise WorkflowError("Source bundle canonical hash does not match docket")

    quran_evidence, quran_coverage = _quran_text_projection(args.quran_text)
    numbered_refs = {
        ref for ref in quran_evidence if ref.split(":", 1)[1] != "0"
    }
    inter_rows, reciprocal, inter_coverage = v3._inter_ayah_evidence_with_fallback(
        args.ayah,
        args.inter_ayah_dir,
        args.inter_ayah_parent_dir,
        numbered_refs,
    )
    hft_projection = v3._hft_authoring_projection(docket, source_bundle)

    layout.input.mkdir(parents=True, exist_ok=True)
    layout.raw.mkdir(parents=True, exist_ok=True)
    layout.editorial.mkdir(parents=True, exist_ok=True)
    _assert_layout(layout)
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
        template_path = V3_PROMPTS_ROOT / f"scope-{lane}.md"
        template = template_path.read_text(encoding="utf-8")
        template_sha256 = _sha256(template.encode("utf-8"))
        request_inputs = {
            "ayah_ref": args.ayah,
            "lane": lane,
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "template_sha256": template_sha256,
        }
        request_sha256 = v3._request_sha256(
            f"scope-{lane}-review", request_inputs
        )
        prompt = v3._render(
            template,
            {
                "@@AYAH_REF@@": args.ayah,
                "@@LANE_PACKET_SHA256@@": packet["identity"][
                    "lane_packet_sha256"
                ],
                "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
                "@@LANE_PACKET_JSON@@": v3._canonical_json(packet),
            },
            label=f"{lane} scope",
        )
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
            "request_sha256": request_sha256,
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "packet": _path_record(layout.packet(lane)),
            "prompt": _path_record(layout.scope_prompt(lane)),
            "template_source": _repo_path(template_path),
            "template_sha256": template_sha256,
            "expected_response": _repo_path(layout.scope_review(lane)),
        }

    manifest = _input_manifest_base(
        layout,
        source_origin,
        docket_origin,
        source_bundle,
        docket,
        quran_coverage,
        inter_coverage,
        lane_records,
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


def _load_unit_manifest(layout: Layout) -> dict[str, Any]:
    _assert_layout(layout)
    if not layout.manifest.is_file() or layout.manifest.is_symlink():
        raise WorkflowError(f"Unit manifest is missing or not regular: {layout.manifest}")
    manifest = _load_json(layout.manifest)
    if (
        manifest.get("schema_version") != "commentary-v4-unit-manifest-v1"
        or manifest.get("ayah_ref") != layout.ayah_ref
    ):
        raise WorkflowError("Unit manifest identity does not match --ayah")
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
        canonical_template = manifest["canonical_template"]
        editorial = manifest["editorial"]
    except (KeyError, TypeError) as exc:
        raise WorkflowError("Unit manifest is missing required records") from exc
    _verify_record(
        source_record,
        label="source snapshot",
        expected=layout.source_bundle,
    )
    _verify_record(
        docket_record,
        label="docket snapshot",
        expected=layout.docket,
    )
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
        _verify_record(
            packet_record,
            label=f"{lane} packet",
            expected=layout.packet(lane),
        )
        _verify_record(
            prompt_record,
            label=f"{lane} prompt",
            expected=layout.scope_prompt(lane),
        )
        if lane_record.get("expected_response") != _repo_path(
            layout.scope_review(lane)
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


def _load_review(
    layout: Layout, manifest: dict[str, Any], lane: str
) -> dict[str, Any] | None:
    path = layout.scope_review(lane)
    if not path.exists():
        return None
    if not path.is_file() or path.is_symlink():
        raise WorkflowError(f"{lane} response is not a regular file: {path}")
    review = _load_json(path)
    lane_record = manifest["lanes"][lane]
    identity = review.get("identity")
    if not isinstance(identity, dict):
        raise WorkflowError(f"{lane} response has no identity object")
    expected = {
        "ayah_ref": layout.ayah_ref,
        "lane": lane,
        "lane_packet_sha256": lane_record["lane_packet_sha256"],
        "authoring_request_sha256": lane_record["request_sha256"],
    }
    for field, value in expected.items():
        if identity.get(field) != value:
            raise WorkflowError(
                f"{lane} response has stale or mixed identity field {field!r}"
            )
    if review.get("ayah_ref") != layout.ayah_ref or review.get("lane") != lane:
        raise WorkflowError(f"{lane} response top-level identity is stale or mixed")
    return review


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
    reviews: dict[str, dict[str, Any]],
) -> tuple[str, dict[str, Any]]:
    governing = _canonical_inputs()
    template_path = PROMPTS_ROOT / "canonical.md"
    template = template_path.read_text(encoding="utf-8")
    replacements = {
        "@@AYAH_REF@@": layout.ayah_ref,
        "@@PROSE_OUTPUT_PATH@@": _repo_path(layout.first_pass("prose")),
        "@@EVIDENCE_OUTPUT_PATH@@": _repo_path(layout.first_pass("evidence")),
        "@@INDEX_OUTPUT_PATH@@": _repo_path(layout.first_pass("index")),
        "@@FRICTION_OUTPUT_PATH@@": _repo_path(layout.first_pass("friction")),
        "@@MICRO_PACKET_PATH@@": _repo_path(layout.packet("micro")),
        "@@MACRO_PACKET_PATH@@": _repo_path(layout.packet("macro")),
        "@@GLOBAL_PACKET_PATH@@": _repo_path(layout.packet("global")),
        "@@MICRO_PACKET_SHA256@@": manifest["lanes"]["micro"]["packet"][
            "sha256"
        ],
        "@@MACRO_PACKET_SHA256@@": manifest["lanes"]["macro"]["packet"][
            "sha256"
        ],
        "@@GLOBAL_PACKET_SHA256@@": manifest["lanes"]["global"]["packet"][
            "sha256"
        ],
        "@@PRINCIPLES_MD@@": governing["principles"],
        "@@COMMENTARY_SPEC_MD@@": governing["commentary_spec"],
        "@@CHANNELS_MD@@": governing["channels"],
        "@@CANONICAL_PROMPT_V2@@": governing["canonical_prompt_v2"],
        "@@MICRO_REVIEW_JSON@@": v3._canonical_json(reviews["micro"]),
        "@@MACRO_REVIEW_JSON@@": v3._canonical_json(reviews["macro"]),
        "@@GLOBAL_REVIEW_JSON@@": v3._canonical_json(reviews["global"]),
    }
    prompt = _render(template, replacements, label="canonical prompt")
    review_records = {
        lane: _path_record(layout.scope_review(lane)) for lane in LANES
    }
    request_inputs = {
        "ayah_ref": layout.ayah_ref,
        "template_sha256": _sha256(template.encode("utf-8")),
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
            f"{lane}_packet_sha256": manifest["lanes"][lane]["packet"][
                "sha256"
            ]
            for lane in LANES
        },
        **{
            f"{lane}_review_sha256": review_records[lane]["sha256"]
            for lane in LANES
        },
    }
    canonical_record = {
        "request_sha256": v3._request_sha256(
            "v4-canonical-write", request_inputs
        ),
        "prompt": {
            "path": _repo_path(layout.canonical_prompt),
            "bytes": len(prompt.encode("utf-8")),
            "sha256": _sha256(prompt.encode("utf-8")),
        },
        "inputs": request_inputs,
        "reviews": review_records,
        "expected_outputs": {
            kind: _repo_path(layout.first_pass(kind)) for kind in KINDS
        },
    }
    return prompt, canonical_record


def _ensure_canonical(
    layout: Layout,
    manifest: dict[str, Any],
    reviews: dict[str, dict[str, Any]],
    *,
    write: bool = True,
) -> dict[str, Any]:
    prompt, expected = _build_canonical_prompt(layout, manifest, reviews)
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
        "ayah_ref": layout.ayah_ref,
        "role": f"{lane}_scope_reviewer",
        "fresh_agent": True,
        "prompt": str(layout.scope_prompt(lane).resolve()),
        "expected_response": _handoff_output_path(
            layout.scope_review(lane),
            RAW_ROOT,
            label=f"{lane} response target",
        ),
        "workspace": str(REPO_ROOT),
        "request_sha256": manifest["lanes"][lane]["request_sha256"],
    }


def _canonical_handoff(layout: Layout, canonical: dict[str, Any]) -> dict[str, Any]:
    expected_outputs = {
        kind: _handoff_output_path(
            layout.first_pass(kind),
            RAW_ROOT,
            label=f"first-pass {kind} target",
        )
        for kind in KINDS
    }
    return {
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
                f"--ayah {layout.ayah_ref}"
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


def advance(args: argparse.Namespace) -> dict[str, Any]:
    layout = layout_for(args.ayah)
    _assert_layout(layout)
    if args.force_input or not layout.manifest.exists():
        prepare(args)
    manifest = _load_unit_manifest(layout)
    reviews: dict[str, dict[str, Any]] = {}
    missing_lanes: list[str] = []
    invalid_lanes: dict[str, str] = {}
    for lane in LANES:
        try:
            review = _load_review(layout, manifest, lane)
        except WorkflowError as exc:
            review = None
            invalid_lanes[lane] = str(exc)
        if review is None:
            missing_lanes.append(lane)
        else:
            reviews[lane] = review
    if invalid_lanes:
        details = "; ".join(
            f"{lane}: {issue}" for lane, issue in sorted(invalid_lanes.items())
        )
        raise WorkflowError(
            "Invalid scope response. V4 does not issue automated repair turns; "
            "inspect, remove, or replace the failed artifact explicitly before "
            f"advancing again. {details}"
        )
    if missing_lanes:
        return {
            "schema_version": "commentary-v4-status-v1",
            "ayah_ref": args.ayah,
            "status": "waiting_for_agents",
            "stage": "scope_review",
            "missing_lanes": missing_lanes,
            "handoffs": [
                _scope_handoff(layout, manifest, lane) for lane in missing_lanes
            ],
        }

    canonical = _ensure_canonical(layout, manifest, reviews)
    first_pass_paths = {kind: layout.first_pass(kind) for kind in KINDS}
    first_present, first_missing = _nonempty_outputs(first_pass_paths)
    if first_missing:
        return {
            "schema_version": "commentary-v4-status-v1",
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
            "ayah_ref": args.ayah,
            "status": "waiting_for_agent",
            "stage": "canonical_editorial",
            "present_outputs": editorial_present,
            "missing_outputs": editorial_missing,
            "handoff": _editorial_handoff(layout, editorial_turn),
        }
    return verify(args)


def verify(args: argparse.Namespace) -> dict[str, Any]:
    layout = layout_for(args.ayah)
    _assert_layout(layout)
    manifest = _load_unit_manifest(layout)
    reviews: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        review = _load_review(layout, manifest, lane)
        if review is None:
            raise WorkflowError(f"Missing {lane} scope response")
        reviews[lane] = review
    canonical = _ensure_canonical(layout, manifest, reviews, write=False)
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
            "--source-bundle and --docket are single-ayah options; use canonical "
            "v3 source paths for a multi-ayah batch"
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
            required=True,
            action="extend",
            nargs="+",
            metavar="REF_OR_RANGE",
            help=(
                "One or more refs or same-surah ranges, for example "
                "100:1-11 or 1:1 1:2. May be repeated."
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
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        ayah_refs = _expand_ayah_selectors(args.ayah)
        if len(ayah_refs) == 1:
            result = _execute_one(
                argparse.Namespace(**{**vars(args), "ayah": ayah_refs[0]})
            )
            has_errors = False
        else:
            result, has_errors = _batch_result(args, ayah_refs)
    except (WorkflowError, OSError, SystemExit) as exc:
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
