#!/usr/bin/env python3
"""Prepare the three hermetic scope prompts for commentary v5."""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sqlite3
import sys
import tempfile
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any


V5_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V5_ROOT.parents[1]
V3_ROOT = V5_ROOT.parent / "v3"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
PROMPTS_ROOT = V5_ROOT / "prompts"
GUIDANCE_ROOT = V5_ROOT / "guidance"
INPUT_ROOT = V5_ROOT / "input"
RAW_ROOT = V5_ROOT / "raw"
EDITORIAL_ROOT = V5_ROOT / "editorial"
DEFAULT_CONTEXT_BUNDLES_DIR = REPO_ROOT / "bundles"
LANES = ("micro", "macro", "global")
LANE_RANK = {lane: index for index, lane in enumerate(LANES)}
MAX_BATCH_UNITS = 512
MAX_JSON_BYTES = 128_000_000
MAX_SCOPE_PROMPT_BYTES = 16_000_000
MAX_EDITORIAL_PROSE_BYTES = 900_000
SCOPE_DISCOVERY_SCHEMA_VERSION = "commentary-v5-scope-discovery-v1"
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
QURAN_REF_IN_TEXT_RE = re.compile(
    r"(?<![0-9:])([1-9][0-9]*):(0|[1-9][0-9]*)(?![0-9:])"
)
QURAN_REF_CONTINUATION_RE = re.compile(
    r"\s*(?P<separator>[-\u2013\u2014,\u060c])\s*"
    r"(?:(?P<surah>[1-9][0-9]*):)?(?P<ayah>0|[1-9][0-9]*)(?![0-9:])"
)
QURAN_COORDINATE_RE = re.compile(
    r"([1-9][0-9]*):(0|[1-9][0-9]*)(?::[1-9][0-9]*){1,2}"
)
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
from _commentary.v5 import packet_evidence  # noqa: E402
from _commentary.v5 import reviewed_supplements  # noqa: E402
import render_authoring as v3  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402
from v3lib.prepare import (  # noqa: E402
    PrepareOptions,
    build_prepared_artifacts,
    validate_docket,
)


PREPARE_OPTIONS = PrepareOptions(
    hft_policy="quarantine",
    expand_ambiguous_native_branches=True,
    demote_unresolved_mandatory_candidates=True,
    max_optional_candidates=80,
    max_support_chars=8_000,
    max_docket_bytes=4_800_000,
)
DEFAULT_QAC_MORPHOLOGY = REPO_ROOT.parent / "quran-data/data/morphology/qac.sqlite.gz"


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

    def scope_ledger(self, lane: str) -> Path:
        return self.raw / f"{lane}.scope.ledger.json"

    def editorial_prose(self) -> Path:
        return self.editorial / f"{self.stem}.prose.editorial.tr.md"

    def invitation_prompt(self) -> Path:
        return self.input / "invitation.prompt.md"

    def invitation_output(self) -> Path:
        return self.editorial / f"{self.stem}.invitation.tr.md"


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


def _record_line_json(value: dict[str, Any]) -> str:
    """Render valid JSON with large registry records on separate lines."""
    lines = ["{"]
    keys = sorted(value)
    for key_index, key in enumerate(keys):
        prefix = _canonical_json(key) + ":"
        item = value[key]
        comma = "," if key_index < len(keys) - 1 else ""
        if isinstance(item, list) and item:
            lines.append(prefix + "[")
            for row_index, row in enumerate(item):
                row_comma = "," if row_index < len(item) - 1 else ""
                lines.append(_canonical_json(row) + row_comma)
            lines.append("]" + comma)
        else:
            lines.append(prefix + _canonical_json(item) + comma)
    lines.append("}")
    return "\n".join(lines)


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
    """Extract canonical ayah refs, including refs in serialized JSON text."""
    refs: set[str] = set()

    def add_range(surah: int, first: int, last: int) -> None:
        if (
            last < first
            or _canonical_extracted_ref(surah, first) is None
            or _canonical_extracted_ref(surah, last) is None
        ):
            return
        refs.update(
            ref
            for ayah in range(first, last + 1)
            if (ref := _canonical_extracted_ref(surah, ayah)) is not None
        )

    def visit(item: Any) -> None:
        if isinstance(item, str):
            stripped = item.strip()
            if coordinate_ref := _coordinate_ayah_ref(stripped):
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
            # Consume a whole reference expression once: later ayah numbers
            # inherit the current surah, while explicit S:A resets it.
            end = 0
            for match in QURAN_REF_IN_TEXT_RE.finditer(item):
                if match.start() < end:
                    continue
                surah, previous = map(int, match.groups())
                add_range(surah, previous, previous)
                end = match.end()
                while continuation := QURAN_REF_CONTINUATION_RE.match(item, end):
                    next_surah = int(continuation["surah"] or surah)
                    ayah = int(continuation["ayah"])
                    if continuation["separator"] in {",", "\u060c"}:
                        add_range(next_surah, ayah, ayah)
                    elif next_surah == surah:
                        add_range(surah, previous, ayah)
                    elif (surah < next_surah
                          and _canonical_extracted_ref(surah, previous)
                          and _canonical_extracted_ref(next_surah, ayah)):
                        for chapter in range(surah, next_surah + 1):
                            add_range(
                                chapter,
                                previous if chapter == surah else 1,
                                ayah if chapter == next_surah else QURAN_AYAH_COUNTS[chapter - 1],
                            )
                    surah, previous = next_surah, ayah
                    end = continuation.end()
        elif isinstance(item, list):
            for child in item:
                visit(child)
        elif isinstance(item, dict):
            for key, child in item.items():
                visit(key)
                visit(child)

    visit(value)
    return sorted(refs, key=_quran_ref_sort_key)


def _candidate_linked_supports(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    return [
        support_map[support_id]
        for support_id in candidate.get("support_ids", [])
        if isinstance(support_id, str) and support_id in support_map
    ]


def _candidate_specific_supports(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Return supports that define this candidate rather than its shared word."""
    linked = _candidate_linked_supports(candidate, support_map)
    source_local_id = candidate.get("source_local_id")
    if not isinstance(source_local_id, str):
        return linked
    specific = [
        support
        for support in linked
        if support.get("source_local_id") == source_local_id
    ]
    return specific or linked


def _context_refs_for_support(
    support: dict[str, Any], *, focus_ref: str, linguistic_source_ref: str
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
    if linguistic_source_ref != focus_ref:
        context_refs.discard(linguistic_source_ref)
        context_refs.update(explicit_context - {focus_ref, linguistic_source_ref})
    return (
        sorted(quran_refs, key=_quran_ref_sort_key),
        sorted(context_refs, key=_quran_ref_sort_key),
    )


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
        if coordinate_ref := _coordinate_ayah_ref(anchor):
            refs.add(coordinate_ref)
        refs.update(_extract_quran_refs(anchor))
    for support in _candidate_specific_supports(candidate, support_map):
        refs.update(support.get("context_refs", []))
    refs.discard(focus_ref)
    refs.discard(linguistic_source_ref)
    return sorted(refs, key=_quran_ref_sort_key)


ROOT_DISPLAY_RE = re.compile(r"\{\{ar:([^}]+)\}\}")


def _candidate_source_roots(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> set[str]:
    roots: set[str] = set()
    for support in _candidate_linked_supports(candidate, support_map):
        text = support.get("text")
        if not isinstance(text, str):
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        root_display = payload.get("root_display") if isinstance(payload, dict) else None
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
    if candidate.get("source_type") != "word_analysis":
        return
    if isinstance(candidate.get("root_ids"), list) and candidate["root_ids"]:
        return
    source_roots = _candidate_source_roots(candidate, support_map)
    candidate["root_ids"] = sorted({
        str(branch["root_id"])
        for branch in branch_map.values()
        if branch.get("root_ar") in source_roots
        and isinstance(branch.get("root_id"), str)
    })


def _candidate_semantic_obligations(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Create compact pointers for every candidate-authored semantic claim."""
    obligations: list[dict[str, Any]] = []

    def append(
        support_id: str,
        kind: str,
        source_pointer: str,
        semantic_claim: Any = None,
    ) -> None:
        identity = {
            "candidate_id": candidate.get("candidate_id"),
            "support_id": support_id,
            "kind": kind,
            "source_pointer": source_pointer,
        }
        row = {
            "obligation_ref": "obl_" + v3._sha256_json(identity)[:20],
            "support_id": support_id,
            "kind": kind,
            "source_pointer": source_pointer,
        }
        if semantic_claim not in (None, "", [], {}):
            row["semantic_claim"] = copy.deepcopy(semantic_claim)
        if row not in obligations:
            obligations.append(row)

    for support in _candidate_specific_supports(candidate, support_map):
        support_id = support.get("support_id")
        if not isinstance(support_id, str):
            continue
        text = support.get("text")
        if isinstance(text, str) and text.strip():
            try:
                decoded = json.loads(text)
            except json.JSONDecodeError:
                decoded = None
            if isinstance(decoded, dict):
                semantic_fields = (
                    "headline",
                    "reason",
                    "reader_payoff",
                    "blocking_evidence",
                    "gloss_range",
                    "root_gloss_range",
                    "prose",
                    "text",  # cross-run published findings
                )
                for field in semantic_fields:
                    value = decoded.get(field)
                    if value in (None, "", [], {}):
                        continue
                    append(
                        support_id,
                        f"candidate_{field}",
                        f"/support_registry/{support_id}/text/{field}",
                        value if field != "prose" else None,
                    )
            else:
                append(
                    support_id,
                    "candidate_support_text",
                    f"/support_registry/{support_id}/text",
                    text if len(text) <= 1_000 else None,
                )

        payload = support.get("payload")
        if isinstance(payload, list):
            for index, claim in enumerate(payload):
                if claim not in (None, "", [], {}):
                    append(
                        support_id, "hft_claim",
                        f"/support_registry/{support_id}/payload/{index}", claim,
                    )
            continue
        if isinstance(payload, str) and payload.strip():
            append(
                support_id,
                "hft_claim",
                f"/support_registry/{support_id}/payload",
                payload if len(payload) <= 1_000 else None,
            )
            continue
        if not isinstance(payload, dict):
            continue
        trace = payload.get("activation_trace")
        if isinstance(trace, list):
            for index, row in enumerate(trace):
                if isinstance(row, dict):
                    append(
                        support_id,
                        "activation_trace",
                        f"/support_registry/{support_id}/payload/activation_trace/{index}",
                        {
                            key: copy.deepcopy(row.get(key))
                            for key in ("branch_ref", "mapped_root_id", "branch_id", "source_ref", "role")
                            if row.get(key) not in (None, "", [], {})
                        },
                    )
        changed = payload.get("changed_reading")
        if isinstance(changed, dict) and changed:
            append(
                support_id,
                "changed_reading",
                f"/support_registry/{support_id}/payload/changed_reading",
                changed,
            )
        for field in (
            "mechanism", "reader_inference", "containment", "rendering_caution",
            "why_still_valid", "why_surprising", "ablation", "limitations",
        ):
            value = payload.get(field)
            if isinstance(value, str) and value.strip():
                append(
                    support_id,
                    field,
                    f"/support_registry/{support_id}/payload/{field}",
                    value,
                )
        for field in ("structural_cues", "abductive_moves", "minimal_triggers", "trigger_refs"):
            cues = payload.get(field)
            if isinstance(cues, list):
                for index, cue in enumerate(cues):
                    if cue in (None, "", [], {}):
                        continue
                    append(
                        support_id,
                        "structural_cue" if field == "structural_cues" else field,
                        f"/support_registry/{support_id}/payload/{field}/{index}",
                        cue,
                    )
    return obligations


def _branch_review_pairs(branches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for branch in branches:
        branch_ref = branch.get("branch_ref")
        facets = branch.get("review_facets")
        if isinstance(facets, list) and facets:
            pairs.extend(
                {"branch_ref": branch_ref, "facet_id": facet.get("facet_id")}
                for facet in facets
                if isinstance(facet, dict) and isinstance(facet.get("facet_id"), str)
            )
        else:
            pairs.append({"branch_ref": branch_ref, "facet_id": None})
    return pairs


def _required_candidate_branch_facets(
    candidate: dict[str, Any], branch_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    available = {
        (row["branch_ref"], row["facet_id"])
        for row in _branch_review_pairs(list(branch_map.values()))
    }
    return [
        {"branch_ref": row["branch_ref"], "facet_id": row.get("facet_id")}
        for row in candidate.get("nominated_branch_facets", [])
        if isinstance(row, dict)
        and (row.get("branch_ref"), row.get("facet_id")) in available
    ]


def _candidate_root_branch_options(
    candidate: dict[str, Any], branch_map: dict[str, dict[str, Any]]
) -> list[str]:
    if candidate.get("source_type") != "word_analysis":
        return []
    root_ids = {
        root_id
        for root_id in candidate.get("root_ids", [])
        if isinstance(root_id, str)
    }
    return sorted(
        branch_ref
        for branch_ref, branch in branch_map.items()
        if branch.get("registry") == "focus" and branch.get("root_id") in root_ids
    )


def _candidate_branch_alternatives(
    candidate: dict[str, Any], branch_map: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []
    for diagnostic in candidate.get("unresolved_branch_citations", []):
        if not isinstance(diagnostic, dict):
            continue
        reason = diagnostic.get("reason")
        if not isinstance(reason, str) or "ambiguous root mapping" not in reason:
            continue
        options = sorted({
            ref
            for ref in re.findall(r"root_[0-9]+/B[0-9]+", reason)
            if ref in branch_map
        })
        if len(options) > 1:
            groups.append({
                "citation": diagnostic.get("citation"),
                "branch_options": options,
                "status": "alternatives_not_established",
            })
    return groups


def _merge_branch_record(
    current: dict[str, Any] | None, addition: dict[str, Any]
) -> dict[str, Any]:
    if current is None:
        return copy.deepcopy(addition)
    dynamic = {"candidate_links", "support_links", "hft_citations"}
    if ({k: v for k, v in current.items() if k not in dynamic}
            != {k: v for k, v in addition.items() if k not in dynamic}):
        raise WorkflowError(
            f"Branch semantics differ across lanes: {addition.get('branch_ref')}"
        )
    merged = copy.deepcopy(current)
    for field in dynamic:
        rows: list[Any] = []
        seen: set[str] = set()
        for source in (current, addition):
            for row in source.get(field, []) or []:
                key = _canonical_json(row)
                if key not in seen:
                    seen.add(key)
                    rows.append(copy.deepcopy(row))
        if rows or field in current or field in addition:
            merged[field] = rows
    return merged


def _finalize_lane_packet_contract(packet: dict[str, Any]) -> dict[str, Any]:
    """Annotate the packet without removing or rewriting evidence records."""
    contract = packet.setdefault("evidence_contract", {})
    contract["focus_root_occurrences_do_not_prove_branch_activation"] = True
    contract["connection_labels_are_nominations_not_decisions"] = True
    contract["evidence_records_are_lossless"] = True
    return packet


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
        if source_bundle.get("coverage", {}).get("word_morpheme_spans", {}).get(
            "alignment_version") == "qac-analysis-bridge-v1":
            from _commentary.qac_analysis_bridge import validate_bundle
            try:
                validate_bundle(source_bundle, source_ref=source_bundle.get(
                    "linguistic_source_ref", args.ayah))
            except (OSError, ValueError, RuntimeError) as exc:
                raise WorkflowError(f"Invalid accepted word/QAC bridge mapping: {exc}") from exc
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


def _effective_lane_for_refs(
    refs: list[str],
    *,
    source_lane: str,
    focus_ref: str,
    pericope_refs: set[str],
    composition_lanes: dict[str, str] | None,
    empty_lane: str | None = None,
    empty_basis: str = "upstream_lane",
) -> tuple[str, str]:
    if not refs:
        return empty_lane or source_lane, empty_basis
    lanes: list[str] = []
    for ref in refs:
        if composition_lanes is not None:
            lanes.append(composition_lanes.get(ref, "global"))
        elif ref in pericope_refs:
            lanes.append("macro")
        else:
            lanes.append("global")
    resolved = max(lanes, key=LANE_RANK.__getitem__)
    if composition_lanes is not None:
        basis = "declared_composition"
    elif resolved == "macro":
        basis = "native_pericope_reference"
    else:
        basis = "beyond_native_pericope_reference"
    return resolved, basis


def _candidate_empty_ref_route(
    candidate: dict[str, Any], source_lane: str
) -> tuple[str, str]:
    if (
        candidate.get("source_type")
        in {"v12_reader_walks", "v12_reader_walks_wide"}
        and candidate.get("kind") == "reader_walk_activation"
    ):
        return "micro", "focus_only_reader_activation"
    if candidate.get("source_type") == "cross_run_publication":
        return "micro", "focus_only_published_finding"
    return source_lane, "upstream_lane"


def _normalize_and_route_lane_packets(
    packets: dict[str, dict[str, Any]],
    source_bundle: dict[str, Any],
    composition: compositions.Composition | None,
) -> dict[str, dict[str, Any]]:
    """Legacy expanded packet assembly; prepare uses the compact contract."""
    focus_ref = str(source_bundle["ayahRef"])
    linguistic_source_ref = str(
        source_bundle.get("linguistic_source_ref", focus_ref)
    )
    pericope_refs = {
        ref
        for packet in packets.values()
        for ref in packet.get("scope", {}).get("pericope", {}).get("refs", [])
        if isinstance(ref, str) and ref != focus_ref
    }
    composition_lanes = None
    if composition is not None:
        composition_lanes = {
            row["ref"]: row["lane"]
            for row in composition.context_rows(focus_ref)
        }
        for unit in packets['macro'].get('selected_context_units', []):
            if unit.get('automatic_prefatory_basmala_membership'):
                composition_lanes[unit['ayah_ref']] = 'macro'

    support_map: dict[str, dict[str, Any]] = {}
    support_order: list[str] = []
    branch_map: dict[str, dict[str, Any]] = {}
    original_branch_refs: dict[str, set[str]] = {lane: set() for lane in LANES}
    all_candidates: list[tuple[str, dict[str, Any]]] = []
    all_connections: list[tuple[str, dict[str, Any]]] = []
    hft_records: dict[str, dict[str, Any]] = {}

    for lane in LANES:
        packet = packets[lane]
        for raw_support in packet.get("support_registry", []):
            if not isinstance(raw_support, dict):
                raise WorkflowError(f"{lane} packet contains malformed support")
            support = copy.deepcopy(raw_support)
            support_id = support.get("support_id")
            if not isinstance(support_id, str) or not support_id:
                raise WorkflowError(f"{lane} packet support has no ID")
            quran_refs, context_refs = _context_refs_for_support(
                support,
                focus_ref=focus_ref,
                linguistic_source_ref=linguistic_source_ref,
            )
            support["quran_refs"] = quran_refs
            support["context_refs"] = context_refs
            if support_id in support_map and support_map[support_id] != support:
                raise WorkflowError(f"Support ID differs across lanes: {support_id}")
            if support_id not in support_map:
                support_map[support_id] = support
                support_order.append(support_id)
        for raw_branch in packet.get("branch_registry", []):
            if not isinstance(raw_branch, dict):
                raise WorkflowError(f"{lane} packet contains malformed branch")
            branch_ref = raw_branch.get("branch_ref")
            if not isinstance(branch_ref, str) or not branch_ref:
                raise WorkflowError(f"{lane} packet branch has no ref")
            original_branch_refs[lane].add(branch_ref)
            branch_map[branch_ref] = _merge_branch_record(
                branch_map.get(branch_ref), raw_branch
            )
        for candidate in packet.get("candidate_inventory", []):
            if not isinstance(candidate, dict):
                raise WorkflowError(f"{lane} packet contains malformed candidate")
            all_candidates.append((lane, candidate))
        for connection in packet.get("connection_registry", []):
            if not isinstance(connection, dict):
                raise WorkflowError(f"{lane} packet contains malformed connection")
            all_connections.append((lane, connection))
        hft = packet.get("hft_evidence")
        if isinstance(hft, dict):
            for record in hft.get("assigned_records", []):
                if isinstance(record, dict) and isinstance(record.get("hft_ref"), str):
                    hft_records[record["hft_ref"]] = copy.deepcopy(record)

    candidate_ids = [
        candidate.get("candidate_id") for _lane, candidate in all_candidates
    ]
    if not all(isinstance(candidate_id, str) for candidate_id in candidate_ids):
        raise WorkflowError("A lane packet candidate has no ID")
    if len(candidate_ids) != len(set(candidate_ids)):
        raise WorkflowError("A candidate appears in more than one source lane")
    if source_bundle.get("coverage", {}).get("word_morpheme_spans", {}).get(
        "alignment_version") == "qac-analysis-bridge-v1":
        expected_topics = {topic["topic_id"]
                           for word in source_bundle["word_analysis"]["words"]
                           for topic in word.get("topics", [])}
        delivered_topics = {candidate["source_local_id"]
                            for _lane, candidate in all_candidates
                            if candidate.get("source_type") == "word_analysis"}
        if expected_topics != delivered_topics:
            raise WorkflowError("Word-analysis topic delivery is incomplete: "
                                f"missing={sorted(expected_topics - delivered_topics)}, "
                                f"unexpected={sorted(delivered_topics - expected_topics)}")

    routed_candidates: dict[str, list[dict[str, Any]]] = {
        lane: [] for lane in LANES
    }
    for source_lane, raw_candidate in all_candidates:
        candidate = copy.deepcopy(raw_candidate)
        _normalize_word_analysis_root_ids(candidate, support_map, branch_map)
        candidate_specific_supports = _candidate_specific_supports(
            candidate, support_map
        )
        candidate["candidate_specific_support_ids"] = [
            support["support_id"] for support in candidate_specific_supports
        ]
        required_refs = _candidate_required_context_refs(
            candidate,
            support_map,
            focus_ref=focus_ref,
            linguistic_source_ref=linguistic_source_ref,
        )
        empty_lane, empty_basis = _candidate_empty_ref_route(
            candidate, source_lane
        )
        target_lane, basis = _effective_lane_for_refs(
            required_refs,
            source_lane=source_lane,
            focus_ref=focus_ref,
            pericope_refs=pericope_refs,
            composition_lanes=composition_lanes,
            empty_lane=empty_lane,
            empty_basis=empty_basis,
        )
        for support_id in candidate.get("support_ids", []):
            if support_id not in support_map:
                raise WorkflowError(
                    f"Candidate {candidate.get('candidate_id')} cites unknown "
                    f"support {support_id}"
                )
        candidate["lane"] = target_lane
        candidate["required_context_refs"] = required_refs
        candidate["semantic_obligations"] = _candidate_semantic_obligations(
            candidate, support_map
        )
        candidate["required_branch_facets"] = _required_candidate_branch_facets(
            candidate, branch_map
        )
        candidate["root_branch_options"] = _candidate_root_branch_options(
            candidate, branch_map
        )
        alternatives = _candidate_branch_alternatives(candidate, branch_map)
        if alternatives:
            candidate["branch_alternative_groups"] = alternatives
        candidate["v5_routing"] = {
            "source_lane": source_lane,
            "resolved_lane": target_lane,
            "basis": basis,
        }
        if "lane_assignment_basis" in candidate:
            candidate["upstream_lane_assignment_basis"] = candidate["lane_assignment_basis"]
            candidate["lane_assignment_basis"] = basis
        candidate["upstream_scope"] = candidate.get("scope")
        candidate["scope"] = target_lane
        if basis == "focus_only_reader_activation":
            candidate["v5_routing"]["constraint"] = (
                "Only the assembled focus-local claim is in scope; an unstated "
                "wider context cannot support acceptance or rejection."
            )
        routed_candidates[target_lane].append(candidate)

    connection_ids = [
        connection.get("connection_ref") for _lane, connection in all_connections
    ]
    if not all(isinstance(connection_id, str) for connection_id in connection_ids):
        raise WorkflowError("A lane packet connection has no ref")
    if len(connection_ids) != len(set(connection_ids)):
        raise WorkflowError("A connection appears in more than one source lane")

    routed_connections: dict[str, list[dict[str, Any]]] = {
        lane: [] for lane in LANES
    }
    for source_lane, raw_connection in all_connections:
        connection = copy.deepcopy(raw_connection)
        refs = set(_extract_quran_refs(connection.get("target_ref")))
        refs.update(_extract_quran_refs(connection.get("source_target_components", [])))
        refs.discard(focus_ref)
        refs.discard(linguistic_source_ref)
        required_refs = sorted(refs, key=_quran_ref_sort_key)
        target_lane, basis = _effective_lane_for_refs(
            required_refs,
            source_lane=source_lane,
            focus_ref=focus_ref,
            pericope_refs=pericope_refs,
            composition_lanes=composition_lanes,
        )
        connection["required_context_refs"] = required_refs
        connection["upstream_relation_scope"] = connection.get("relation_scope")
        connection["relation_scope"] = target_lane
        connection["v5_routing"] = {
            "source_lane": source_lane,
            "resolved_lane": target_lane,
            "basis": basis,
        }
        routed_connections[target_lane].append(connection)

    hft_lane_counts = {
        lane: sum(isinstance(c.get('hft_ref'), str) for c in candidates)
        for lane, candidates in routed_candidates.items()
    }
    for lane in LANES:
        packet = packets[lane]
        candidates = routed_candidates[lane]
        connections = routed_connections[lane]
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

        needed_branch_refs = set(original_branch_refs[lane])
        for candidate in candidates:
            for field in (
                "branch_refs",
                "focus_branch_refs",
                "nominated_branch_refs",
                "unresolved_branch_refs",
                "root_branch_options",
            ):
                needed_branch_refs.update(
                    ref
                    for ref in candidate.get(field, [])
                    if isinstance(ref, str)
                )
        for support in supports:
            needed_branch_refs.update(
                ref
                for ref in support.get("branch_refs", [])
                if isinstance(ref, str)
            )
        missing_branches = needed_branch_refs - set(branch_map)
        if missing_branches:
            raise WorkflowError(
                f"{lane} packet lacks routed branches: {sorted(missing_branches)}"
            )

        lane_candidate_ids = {candidate["candidate_id"] for candidate in candidates}
        lane_support_ids = {support["support_id"] for support in supports}
        lane_hft_refs = {
            candidate.get("hft_ref")
            for candidate in candidates
            if isinstance(candidate.get("hft_ref"), str)
        }
        branches: list[dict[str, Any]] = []
        for branch_ref in sorted(needed_branch_refs):
            branch = copy.deepcopy(branch_map[branch_ref])
            branch["candidate_links"] = [
                {**link, "lane": lane}
                for link in branch.get("candidate_links", [])
                if isinstance(link, dict)
                and link.get("candidate_id") in lane_candidate_ids
            ]
            branch["support_links"] = [
                support_id
                for support_id in branch.get("support_links", [])
                if support_id in lane_support_ids
            ]
            branch["hft_citations"] = [
                citation
                for citation in branch.get("hft_citations", [])
                if isinstance(citation, dict)
                and citation.get("hft_ref") in lane_hft_refs
            ]
            branches.append(branch)

        packet["candidate_inventory"] = candidates
        packet["support_registry"] = supports
        packet["branch_registry"] = branches
        packet["connection_registry"] = connections
        packet["review_inventory"] = {
            "context_refs": sorted({
                ref
                for candidate in candidates
                for ref in candidate.get("required_context_refs", [])
            } | {
                ref
                for connection in connections
                for ref in connection.get("required_context_refs", [])
            } | {
                unit["ayah_ref"]
                for unit in packet.get("selected_context_units", [])
                if isinstance(unit, dict) and isinstance(unit.get("ayah_ref"), str)
            }, key=_quran_ref_sort_key),
            "candidate_ids": [candidate["candidate_id"] for candidate in candidates],
            "support_ids": [support["support_id"] for support in supports],
            "connection_refs": [
                connection["connection_ref"] for connection in connections
            ],
            "available_branch_facets": _branch_review_pairs(branches),
        }
        packet["evidence_contract"] = {
            "candidate_context_refs_are_exact": True,
            "candidate_specific_supports_drive_routing": True,
            "support_quran_refs_are_structured": True,
            "composition_routing_is_authoritative": composition is not None,
            "focus_only_reader_activations_are_micro": True,
            "root_branch_options_are_non_nominating": True,
            "branch_alternative_groups_are_non_cumulative": True,
        }
        hft = packet.get("hft_evidence")
        if isinstance(hft, dict):
            assigned = [
                copy.deepcopy(hft_records[ref])
                for ref in sorted(lane_hft_refs)
                if ref in hft_records
            ]
            for record in assigned:
                record["upstream_owning_lane"] = record.get("owning_lane")
                record["owning_lane"] = lane
                for field in ("lane_basis", "evidence_scope"):
                    if field in record:
                        record[f"upstream_{field}"] = record[field]
                record["evidence_scope"] = lane
                record["lane_basis"] = next(
                    candidate["v5_routing"]["basis"]
                    for candidate in candidates
                    if candidate.get("hft_ref") == record["hft_ref"]
                )
            hft["assigned_records"] = assigned
            hft["assigned_record_count"] = len(assigned)
            hft["lane_counts"] = hft_lane_counts
            scope_hft = packet.get("scope", {}).get("hft")
            if isinstance(scope_hft, dict):
                scope_hft["assigned_record_count"] = len(assigned)
        scope = packet.get("scope", {})
        if composition is not None and "pericope" in scope:
            scope["upstream_pericope"] = scope.pop("pericope")
        if "lane_contract" in scope:
            scope["upstream_lane_contract"] = scope.pop("lane_contract")
        packet["schema_version"] = "commentary-v5-hermetic-scope-packet-v4"
        _finalize_lane_packet_contract(packet)
    return packets


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

    if source_bundle.get("coverage", {}).get("word_morpheme_spans", {}).get(
        "alignment_version") == "qac-analysis-bridge-v1":
        topic_links = {}
        source_ref = source_bundle.get("linguistic_source_ref", source_bundle["ayahRef"])
        for word, span in zip(source_bundle["word_analysis"]["words"],
                              source_bundle["word_morpheme_spans"]):
            link = {
                "analysis_ref": f"{source_ref}:{word['critical_w']}",
                "qac_refs": list(span["qac_refs"]) if span else [],
                "status": "accepted" if span else "excluded-source-defect",
            }
            for topic in word.get("topics", []):
                if topic["topic_id"] in topic_links:
                    raise WorkflowError("Word-analysis topic identities are duplicated")
                topic_links[topic["topic_id"]] = link
        for candidate in packet["candidate_inventory"]:
            if candidate.get("source_type") == "word_analysis":
                candidate["word_alignment"] = copy.deepcopy(topic_links[candidate["source_local_id"]])
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


def _finalize_compact_lane_packets(
    packets: dict[str, dict[str, Any]], source_bundle: dict[str, Any]
) -> None:
    """Keep early V5 ownership and evidence shape, with correctness checks.

    Do not derive review inventories, obligations, or additional context here.
    Source supports already carry those claims. QAC links are attached by
    _build_lane_packet; root identities can be repaired without moving topics.
    """
    candidates: list[dict[str, Any]] = []
    seen: set[str] = set()
    all_supports: dict[str, dict[str, Any]] = {}
    all_branches: dict[str, dict[str, Any]] = {}
    connection_ids: set[str] = set()
    for lane in LANES:
        packet = packets[lane]
        support_map: dict[str, dict[str, Any]] = {}
        branch_map: dict[str, dict[str, Any]] = {}
        for support in packet["support_registry"]:
            if not isinstance(support, dict) or not isinstance(support.get("support_id"), str):
                raise WorkflowError(f"{lane} packet contains malformed support")
            support_id = support["support_id"]
            if not support_id or support_id in support_map:
                raise WorkflowError(f"{lane} packet has an empty or duplicate support ID")
            if support_id in all_supports and all_supports[support_id] != support:
                raise WorkflowError(f"Support ID differs across lanes: {support_id}")
            support_map[support_id] = all_supports[support_id] = support
        for branch in packet["branch_registry"]:
            if not isinstance(branch, dict) or not isinstance(branch.get("branch_ref"), str):
                raise WorkflowError(f"{lane} packet contains malformed branch")
            branch_ref = branch["branch_ref"]
            if not branch_ref or branch_ref in branch_map:
                raise WorkflowError(f"{lane} packet has an empty or duplicate branch ref")
            all_branches[branch_ref] = _merge_branch_record(all_branches.get(branch_ref), branch)
            branch_map[branch_ref] = branch
            if branch.get("registry") == "unresolved" and branch.get("hft_citations"):
                branch["boundary"] = (
                    "No registered branch descriptor is supplied. An exact HFT "
                    "trace may support an attributed contextual activation, but it "
                    "does not establish a gloss, facet, or verified lexical identity."
                )
                branch["root_occurrence_qualification"] = (
                    "No registered focus occurrence is supplied. Use only the "
                    "HFT-cited context coordinate, root, and role for an attributed "
                    "activation whose contact returns to the focus."
                )
                for citation in branch["hft_citations"]:
                    if isinstance(citation, dict):
                        citation["qualification"] = (
                            "Exact HFT-attributed role; eligible as attributed "
                            "contextual evidence, not verified lexicon evidence."
                        )
        for connection in packet.get("connection_registry", []):
            if not isinstance(connection, dict) or not isinstance(connection.get("connection_ref"), str):
                raise WorkflowError(f"{lane} packet contains malformed connection")
            connection_ref = connection["connection_ref"]
            if not connection_ref or connection_ref in connection_ids:
                raise WorkflowError("A connection ref is empty or duplicated across source lanes")
            connection_ids.add(connection_ref)
        for candidate in packet["candidate_inventory"]:
            if not isinstance(candidate, dict):
                raise WorkflowError(f"{lane} packet contains malformed candidate")
            candidate_id = candidate.get("candidate_id")
            if not isinstance(candidate_id, str) or not candidate_id:
                raise WorkflowError("A lane packet candidate has no ID")
            if candidate_id in seen:
                raise WorkflowError("A candidate appears in more than one source lane")
            seen.add(candidate_id)
            candidates.append(candidate)
            for support_id in candidate.get("support_ids", []):
                if support_id not in support_map:
                    raise WorkflowError(
                        f"Candidate {candidate_id} cites unknown support {support_id}"
                    )
            _normalize_word_analysis_root_ids(candidate, support_map, branch_map)

    alignment = source_bundle.get("coverage", {}).get("word_morpheme_spans", {})
    if alignment.get("alignment_version") == "qac-analysis-bridge-v1":
        expected_topics = {
            topic["topic_id"]
            for word in source_bundle["word_analysis"]["words"]
            for topic in word.get("topics", [])
        }
        delivered_topics = [
            candidate["source_local_id"] for candidate in candidates
            if candidate.get("source_type") == "word_analysis"
        ]
        if (expected_topics != set(delivered_topics)
                or len(delivered_topics) != len(expected_topics)):
            raise WorkflowError(
                "Word-analysis topic delivery is incomplete or duplicated: "
                f"missing={sorted(expected_topics - set(delivered_topics))}, "
                f"unexpected={sorted(set(delivered_topics) - expected_topics)}"
            )


def _canonical_inputs() -> dict[str, str]:
    """Load the governing documents frozen with the early V5 input contract."""
    paths = {
        "principles": GUIDANCE_ROOT / "PRINCIPLES.md",
        "commentary_spec": GUIDANCE_ROOT / "COMMENTARY_SPEC.md",
        "channels": GUIDANCE_ROOT / "CHANNELS.md",
        "canonical_prompt_v2": GUIDANCE_ROOT / "PROMPT_V2.md",
    }
    try:
        return {key: path.read_text(encoding="utf-8") for key, path in paths.items()}
    except OSError as exc:
        raise WorkflowError(f"Cannot read governing instructions: {exc}") from exc


def _lane_specific_procedure(lane: str, packet: dict[str, Any]) -> str:
    if lane == "micro" and packet.get("reference_evidence"):
        return (
            "- reference_evidence is additive reviewed evidence for its nominated "
            "cross-ayah comparisons, not a complete registry or whitelist. Its "
            "absence is not evidence against another candidate whose own supplied "
            "supports establish a comparison. morpheme_columns defines the added "
            "QAC rows. Evidence availability does not establish activation."
        )
    procedure = _context_overlay_procedure(lane, packet)
    if lane == "macro" and packet.get("lexical_evidence"):
        procedure += (
            "\n- Match lexical_evidence by branch_ref. Its dictionary quotations "
            "and form restrictions qualify the nominated meaning; they do not "
            "establish activation."
        )
    return procedure


def _context_overlay_procedure(lane: str, packet: dict[str, Any]) -> str:
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


def prepare_invitation(args: argparse.Namespace) -> dict[str, Any]:
    """Render the post-editorial invitation prompt from the final prose alone."""
    layout = layout_for(args.ayah, _analysis_id(args))
    editorial_path = layout.editorial_prose()
    try:
        editorial_payload = editorial_path.read_bytes()
    except OSError as exc:
        raise WorkflowError(f"Cannot read final editorial prose {editorial_path}: {exc}") from exc
    if not editorial_payload:
        raise WorkflowError(f"Final editorial prose is empty: {editorial_path}")
    if len(editorial_payload) > MAX_EDITORIAL_PROSE_BYTES:
        raise WorkflowError(
            f"Final editorial prose exceeds {MAX_EDITORIAL_PROSE_BYTES} bytes: {editorial_path}"
        )
    try:
        editorial_prose = editorial_payload.decode("utf-8")
        template = (PROMPTS_ROOT / "invitation.md").read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise WorkflowError(f"Cannot prepare invitation prompt: {exc}") from exc
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@EDITORIAL_PROSE@@": editorial_prose,
            "@@INVITATION_OUTPUT_PATH@@": _repo_path(layout.invitation_output()),
        },
        label="invitation prompt",
    )
    _atomic_write(
        layout.invitation_prompt(), prompt.encode("utf-8"), root=INPUT_ROOT
    )
    return {
        "schema_version": "commentary-v5-invitation-prepared-v1",
        "status": "prepared",
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "handoff": {
            "role": "invitation",
            "prompt": str(layout.invitation_prompt().resolve(strict=False)),
            "output": str(layout.invitation_output().resolve(strict=False)),
            "launch": "fresh_agent",
            "model": "gpt-5.6-luna",
            "reasoning_effort": "max",
        },
        "generated_files": [str(layout.invitation_prompt().resolve(strict=False))],
    }


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

    packets: dict[str, dict[str, Any]] = {}
    for lane in LANES:
        packets[lane] = _build_lane_packet(
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
    _finalize_compact_lane_packets(packets, source_bundle)
    alignment = source_bundle.get("coverage", {}).get("word_morpheme_spans", {})
    for packet in packets.values():
        packet["focus_word_alignment"] = {
            key: alignment[key] for key in (
                "alignment_version", "words_total", "words_resolved",
                "words_unresolved", "unresolved", "note",
                "source_namespace", "target_namespace", "bridge", "shared_morphemes",
            ) if key in alignment
        }
    def load_lexical_source(ref: str) -> dict[str, Any]:
        path = compositions.unit_bundle_path(context_root, ref)
        root = context_root if path.is_file() else member_root
        return compositions.load_unit_bundle(root, ref)[1]

    try:
        supplements = reviewed_supplements.attach(
            packets, quran_evidence,
            Path(getattr(args, "qac_morphology", DEFAULT_QAC_MORPHOLOGY)),
            Path(getattr(args, "qac_cache_dir", packet_evidence.DEFAULT_CACHE_DIR)),
            load_lexical_source,
        )
    except (reviewed_supplements.SupplementError, compositions.CompositionError) as exc:
        raise WorkflowError(str(exc)) from exc
    context_morphology_status = (
        "targeted" if supplements["micro_reference_refs"] else "not_requested"
    )
    prompts = {
        lane: _build_scope_prompt(layout, lane, packets[lane]) for lane in LANES
    }

    if getattr(args, "check_only", False):
        return {
            "schema_version": "commentary-v5-preparation-check-v1",
            "status": "checked",
            "analysis_id": layout.analysis_id,
            "ayah_ref": layout.ayah_ref,
            "agent_input_contract": "early-v5-compact",
            "context_morphology_status": context_morphology_status,
            "missing_context_morphology_refs": [],
            "reviewed_supplements": supplements,
            "prompt_bytes": {lane: len(prompt.encode("utf-8")) for lane, prompt in prompts.items()},
            "word_alignment": source_bundle.get("coverage", {}).get("word_morpheme_spans", {}),
        }

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
        "agent_input_contract": "early-v5-compact",
        "context_morphology_status": context_morphology_status,
        "missing_context_morphology_refs": [],
        "reviewed_supplements": supplements,
        "focus_word_alignment": packets["micro"]["focus_word_alignment"],
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
                "scope_ledger_output": str(
                    layout.scope_ledger(lane).resolve(strict=False)
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
                "live agent to write its scope prose and landing ledger"
            ),
            "consolidation": (
                "close scope agents, then give the three scope prose texts, "
                "the pinned project guidance, and a short focus/context brief "
                "to one fresh consolidator"
            ),
            "editorial": (
                "ask that same consolidator for the editorial rewrite, then close"
            ),
            "invitation": (
                "after editorial completion, run prepare-invitation and launch its "
                "fresh Luna max handoff as a monitored invitation stage"
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
        "--qac-morphology", type=Path, default=DEFAULT_QAC_MORPHOLOGY,
        help="Local QAC SQLite gzip source checked by the preparation preflight.",
    )
    parser.add_argument(
        "--qac-cache-dir", type=Path, default=packet_evidence.DEFAULT_CACHE_DIR,
        help="Reusable local directory for the streamed, source-hashed QAC database.",
    )
    parser.add_argument(
        "--allow-missing-qac-morphology", action="store_true",
        help="Exploratory runs only: skip the QAC source preflight; focus bridge validation still applies.",
    )
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
        "--check-only", action="store_true",
        help="Assemble and validate all prompts without writing prompts or creating handoffs.",
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
    invitation_parser = subparsers.add_parser(
        "prepare-invitation",
        help="Render fresh-agent invitation prompts from completed editorial prose.",
    )
    invitation_parser.add_argument(
        "--ayah",
        action="extend",
        nargs="+",
        required=True,
        metavar="REF_OR_RANGE",
        help="One or more refs or same-surah ranges; may be repeated.",
    )
    invitation_parser.add_argument("--analysis-id", default="native")
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
                {**handoff, "ayah_ref": ref} for handoff in result.get("handoffs", [])
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
            "status": ("checked" if getattr(args, "check_only", False) else "prepared") if not errors else "error",
            "units": units,
            "parallel_handoffs": handoffs if not errors else [],
        },
        bool(errors),
    )


def _preflight_qac(args: argparse.Namespace) -> None:
    """Fail once before a production batch if its local QAC source is unusable."""
    if getattr(args, "allow_missing_qac_morphology", False):
        return
    try:
        with packet_evidence.open_database(
            Path(args.qac_morphology), Path(args.qac_cache_dir)
        ) as (connection, _source_hash):
            columns = ", ".join((*packet_evidence.MORPHEME_COLUMNS,
                                 "surah", "ayah", "word_index", "morpheme_index"))
            connection.execute(f"SELECT {columns} FROM qac_morphemes LIMIT 0")
    except (OSError, EOFError, sqlite3.Error, ValueError, zlib.error) as exc:
        raise WorkflowError(
            f"QAC source preflight failed: {exc}. Check --qac-morphology and "
            "--qac-cache-dir; --allow-missing-qac-morphology is for exploratory runs only."
        ) from exc


def main() -> int:
    args = _parser().parse_args()
    try:
        if args.command == "prepare-invitation":
            refs = _expand_ayah_selectors(args.ayah)
            units: list[dict[str, Any]] = []
            errors = 0
            for ref in refs:
                try:
                    units.append(
                        prepare_invitation(
                            argparse.Namespace(ayah=ref, analysis_id=args.analysis_id)
                        )
                    )
                except (WorkflowError, OSError) as exc:
                    errors += 1
                    units.append({"ayah_ref": ref, "status": "error", "error": str(exc)})
            result = units[0] if len(units) == 1 else {
                "schema_version": "commentary-v5-invitation-prepared-batch-v1",
                "status": "prepared" if not errors else "error",
                "units": units,
                "parallel_handoffs": [
                    unit["handoff"] | {"ayah_ref": unit["ayah_ref"]}
                    for unit in units if unit.get("status") == "prepared"
                ] if not errors else [],
            }
            print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
            return 1 if errors else 0
        refs, composition = _resolve_request(args)
        _preflight_qac(args)
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
