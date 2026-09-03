"""Ordered context compositions for the commentary v5 workflow."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "commentary-v5-analysis-composition-v2"
CONTEXT_MEMBER_PROTOCOL = "commentary-v5-native-context-member-v1"
ANALYSIS_ID_RE = re.compile(r"[a-z0-9](?:[a-z0-9._-]{0,79})")
SEGMENT_ID_RE = re.compile(r"[a-z0-9](?:[a-z0-9._-]{0,63})")
REF_RE = re.compile(r"([1-9][0-9]*):(0|[1-9][0-9]*)")
SELECTOR_RE = re.compile(
    r"([1-9][0-9]*):(0|[1-9][0-9]*)(?:-([1-9][0-9]*))?"
)
QAC_REF_RE = re.compile(r"([1-9][0-9]*):([1-9][0-9]*):[1-9][0-9]*:[1-9][0-9]*")
MAX_COMPOSITION_UNITS = 512
MAX_SOURCE_JSON_BYTES = 128_000_000
BASMALA_LINGUISTIC_SOURCE_REF = "1:1"
BASMALA_NORMALIZED_SURFACE = "بسماللهالرحمنالرحيم"
BASMALA_EXCLUDED_SURAHS = {1, 9}

class CompositionError(RuntimeError):
    """Raised when an analysis composition or selected unit is invalid."""


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json_bytes(value)).hexdigest()


def normalize_arabic_surface(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    normalized = "".join(
        char
        for char in normalized
        if unicodedata.category(char) not in {"Mn", "Cf"}
        and not char.isspace()
    )
    return normalized.translate(str.maketrans({
        "ٱ": "ا",
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ى": "ي",
    }))


def _stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}_{canonical_sha256(value)[:20]}"


def _validate_ref(ref: str) -> str:
    match = REF_RE.fullmatch(ref)
    if match is None:
        raise CompositionError(f"Invalid Quran unit reference: {ref!r}")
    surah, ayah = (int(item) for item in match.groups())
    if not 1 <= surah <= 114:
        raise CompositionError(f"Surah is outside 1-114: {ref}")
    if ayah == 0 and surah in BASMALA_EXCLUDED_SURAHS:
        reason = "S1 uses numbered 1:1" if surah == 1 else "S9 has no basmala"
        raise CompositionError(f"Invalid prefatory unit {ref}: {reason}")
    return f"{surah}:{ayah}"


def expand_selectors(selectors: str | Iterable[str]) -> list[str]:
    if isinstance(selectors, str):
        selectors = [selectors]
    refs: list[str] = []
    seen: set[str] = set()
    for raw_group in selectors:
        if not isinstance(raw_group, str):
            raise CompositionError("Ayah selectors must be strings")
        for raw_selector in raw_group.split(","):
            selector = raw_selector.strip()
            match = SELECTOR_RE.fullmatch(selector)
            if match is None:
                raise CompositionError(f"Invalid ayah selector: {selector!r}")
            surah_text, first_text, last_text = match.groups()
            surah = int(surah_text)
            first = int(first_text)
            if first == 0 and last_text is not None:
                raise CompositionError(
                    f"Ranges may not start at prefatory unit zero: {selector}"
                )
            last = int(last_text or first_text)
            if last < first:
                raise CompositionError(f"Descending range is not allowed: {selector}")
            for ayah in range(first, last + 1):
                ref = _validate_ref(f"{surah}:{ayah}")
                if ref not in seen:
                    refs.append(ref)
                    seen.add(ref)
                if len(refs) > MAX_COMPOSITION_UNITS:
                    raise CompositionError(
                        f"A composition may contain at most {MAX_COMPOSITION_UNITS} units"
                    )
    if not refs:
        raise CompositionError("At least one Quran unit is required")
    return refs


def expand_explicit_refs(selectors: str | Iterable[str]) -> list[str]:
    """Expand comma-separated refs while rejecting ranges and duplicates."""
    if isinstance(selectors, str):
        selectors = [selectors]
    refs: list[str] = []
    seen: set[str] = set()
    for raw_group in selectors:
        if not isinstance(raw_group, str):
            raise CompositionError("Added ayat must be strings")
        for raw_ref in raw_group.split(","):
            ref = raw_ref.strip()
            if REF_RE.fullmatch(ref) is None:
                raise CompositionError(
                    f"Invalid added ayah reference {ref!r}; list each S:A ref explicitly"
                )
            ref = _validate_ref(ref)
            if ref in seen:
                raise CompositionError(f"Duplicate added ayah reference: {ref}")
            refs.append(ref)
            seen.add(ref)
            if len(refs) > MAX_COMPOSITION_UNITS:
                raise CompositionError(
                    f"A composition may contain at most {MAX_COMPOSITION_UNITS} units"
                )
    if not refs:
        raise CompositionError("surah_membership.added_ayat_refs cannot be empty")
    return refs


@dataclass(frozen=True)
class Segment:
    segment_id: str
    refs: tuple[str, ...]


@dataclass(frozen=True)
class Composition:
    analysis_id: str
    segments: tuple[Segment, ...]
    focus_refs: tuple[str, ...]
    description: str | None = None
    member_surah: int | None = None
    added_ayat_refs: tuple[str, ...] = ()

    @property
    def ordered_refs(self) -> tuple[str, ...]:
        return tuple(ref for segment in self.segments for ref in segment.refs)

    @property
    def canonical_payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "analysis_id": self.analysis_id,
            "segments": [
                {"id": segment.segment_id, "refs": list(segment.refs)}
                for segment in self.segments
            ],
            "focus_refs": list(self.focus_refs),
        }
        if self.description is not None:
            payload["description"] = self.description
        if self.member_surah is not None:
            payload["surah_membership"] = {
                "target_surah": self.member_surah,
                "added_ayat_refs": list(self.added_ayat_refs),
            }
        return payload

    @property
    def canonical_sha256(self) -> str:
        return canonical_sha256(self.canonical_payload)

    def segment_for(self, ref: str) -> Segment:
        for segment in self.segments:
            if ref in segment.refs:
                return segment
        raise CompositionError(f"Reference {ref} is outside analysis {self.analysis_id}")

    def context_refs(self, focus_ref: str) -> tuple[str, ...]:
        if focus_ref not in self.focus_refs:
            raise CompositionError(
                f"Focus {focus_ref} is not declared by analysis {self.analysis_id}"
            )
        added = set(self.added_ayat_refs)
        refs = [
            ref for ref in self.ordered_refs if ref != focus_ref and ref not in added
        ]
        refs.extend(ref for ref in self.added_ayat_refs if ref != focus_ref)
        return tuple(refs)

    def context_rows(
        self,
        focus_ref: str,
    ) -> list[dict[str, Any]]:
        if focus_ref not in self.focus_refs:
            raise CompositionError(
                f"Focus {focus_ref} is not declared by analysis {self.analysis_id}"
            )
        focus_segment = self.segment_for(focus_ref).segment_id
        focus_surah = focus_ref.split(":", 1)[0]
        host_basmala_ref = f"{focus_surah}:0"
        added = set(self.added_ayat_refs)
        rows: list[dict[str, Any]] = []
        context_index = 0
        for segment_index, segment in enumerate(self.segments):
            for unit_index, ref in enumerate(segment.refs):
                if ref == focus_ref or ref in added:
                    continue
                lane = (
                    "macro"
                    if ref == host_basmala_ref
                    or (
                        segment.segment_id == focus_segment
                        and ref.split(":", 1)[0] == focus_surah
                    )
                    else "global"
                )
                rows.append({
                    "ref": ref,
                    "segment_id": segment.segment_id,
                    "segment_index": segment_index,
                    "unit_index": unit_index,
                    "composition_order": context_index,
                    "source_pointer": (
                        "/scope/analysis_composition/context_refs/"
                        f"{context_index}"
                    ),
                    "lane": lane,
                })
                context_index += 1
        for added_index, ref in enumerate(self.added_ayat_refs):
            rows.append({
                "ref": ref,
                "segment_id": "external-ayat",
                "segment_index": -1,
                "unit_index": added_index,
                "composition_order": context_index + added_index,
                "source_pointer": (
                    "/scope/analysis_composition/surah_membership/"
                    f"added_ayat_refs/{added_index}"
                ),
                "lane": "macro",
                "membership_target_surah": self.member_surah,
                "membership_added_ayah": True,
                "focus_eligible": False,
            })
        return rows


def composition_from_payload(payload: dict[str, Any]) -> Composition:
    if not isinstance(payload, dict):
        raise CompositionError("Composition must be one JSON object")
    allowed = {
        "schema_version",
        "analysis_id",
        "segments",
        "focus_refs",
        "description",
        "surah_membership",
    }
    unknown = set(payload) - allowed
    if unknown:
        raise CompositionError(f"Unknown composition fields: {sorted(unknown)}")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise CompositionError(f"Expected schema_version {SCHEMA_VERSION}")
    analysis_id = payload.get("analysis_id")
    if not isinstance(analysis_id, str) or ANALYSIS_ID_RE.fullmatch(analysis_id) is None:
        raise CompositionError(f"Invalid analysis_id: {analysis_id!r}")
    if analysis_id == "native":
        raise CompositionError("analysis_id 'native' is reserved for the default workflow")

    raw_segments = payload.get("segments")
    if not isinstance(raw_segments, list) or not raw_segments:
        raise CompositionError("segments must be a nonempty array")
    segments: list[Segment] = []
    segment_ids: set[str] = set()
    all_refs: list[str] = []
    for index, raw_segment in enumerate(raw_segments):
        if not isinstance(raw_segment, dict) or set(raw_segment) != {"id", "refs"}:
            raise CompositionError(
                f"segments[{index}] must contain exactly id and refs"
            )
        segment_id = raw_segment.get("id")
        if not isinstance(segment_id, str) or SEGMENT_ID_RE.fullmatch(segment_id) is None:
            raise CompositionError(f"Invalid segment id: {segment_id!r}")
        if segment_id in segment_ids:
            raise CompositionError(f"Duplicate segment id: {segment_id}")
        raw_refs = raw_segment.get("refs")
        if not isinstance(raw_refs, (str, list, tuple)):
            raise CompositionError(f"segments[{index}].refs must be selectors")
        refs = expand_selectors(raw_refs)
        segment_ids.add(segment_id)
        segments.append(Segment(segment_id, tuple(refs)))
        all_refs.extend(refs)
        if len(all_refs) > MAX_COMPOSITION_UNITS:
            raise CompositionError(
                f"A composition may contain at most {MAX_COMPOSITION_UNITS} units"
            )
    duplicates = sorted({ref for ref in all_refs if all_refs.count(ref) > 1})
    if duplicates:
        raise CompositionError(
            f"A unit may appear in only one composition segment: {duplicates}"
        )

    raw_focus_refs = payload.get("focus_refs")
    if not isinstance(raw_focus_refs, (str, list, tuple)):
        raise CompositionError("focus_refs must be selectors")
    focus_refs = expand_selectors(raw_focus_refs)
    outside = sorted(set(focus_refs) - set(all_refs))
    if outside:
        raise CompositionError(f"Focus refs are outside the composition: {outside}")
    description = payload.get("description")
    if description is not None and not isinstance(description, str):
        raise CompositionError("description must be a string")
    member_surah = None
    added_ayat_refs: tuple[str, ...] = ()
    membership = payload.get("surah_membership")
    if membership is not None:
        if not isinstance(membership, dict):
            raise CompositionError("surah_membership must be an object")
        if set(membership) != {"target_surah", "added_ayat_refs"}:
            raise CompositionError(
                "surah_membership must contain target_surah and added_ayat_refs"
            )
        member_surah = membership.get("target_surah")
        if not isinstance(member_surah, int) or not 1 <= member_surah <= 114:
            raise CompositionError("surah_membership.target_surah must be 1-114")
        raw_added = membership.get("added_ayat_refs")
        if not isinstance(raw_added, (str, list, tuple)):
            raise CompositionError(
                "surah_membership.added_ayat_refs must be explicit refs"
            )
        if (isinstance(raw_added, str) and not raw_added.strip()) or (
            not isinstance(raw_added, str) and not raw_added
        ):
            raise CompositionError(
                "surah_membership.added_ayat_refs cannot be empty"
            )
        added_ayat_refs = tuple(expand_explicit_refs(raw_added))
        overlap = sorted(set(all_refs) & set(added_ayat_refs))
        if len(set(all_refs) | set(added_ayat_refs)) > MAX_COMPOSITION_UNITS:
            raise CompositionError(
                f"A composition may contain at most {MAX_COMPOSITION_UNITS} units"
            )
        target_refs = [
            ref for ref in all_refs if ref.startswith(f"{member_surah}:")
        ]
        if not target_refs:
            raise CompositionError(
                "surah_membership requires at least one target-surah unit"
            )
        outside_focus = sorted(set(focus_refs) - set(target_refs))
        if outside_focus:
            raise CompositionError(
                "Added ayat are context-only; every focus must belong to "
                f"target surah {member_surah}: {outside_focus}"
            )
        added_focuses = sorted(set(focus_refs) & set(added_ayat_refs))
        if added_focuses:
            raise CompositionError(
                f"Added ayat are context-only and cannot be focuses: {added_focuses}"
            )
        if overlap:
            raise CompositionError(
                "Added ayat must not also appear in composition segments: "
                f"{overlap}"
            )
    contextual_refs = set(all_refs) | set(added_ayat_refs)
    for focus_ref in focus_refs:
        if not contextual_refs - {focus_ref}:
            raise CompositionError(f"Focus {focus_ref} has no contextual unit")
    return Composition(
        analysis_id=analysis_id,
        segments=tuple(segments),
        focus_refs=tuple(focus_refs),
        description=description,
        member_surah=member_surah,
        added_ayat_refs=added_ayat_refs,
    )


def composition_from_cli(
    analysis_id: str,
    segment_specs: list[str],
    focus_selectors: list[str],
    *,
    member_surah: int | None = None,
    added_ayat_selectors: list[str] | None = None,
) -> Composition:
    segments: list[dict[str, Any]] = []
    for spec in segment_specs:
        segment_id, separator, selectors = spec.partition("=")
        if not separator or not segment_id or not selectors:
            raise CompositionError(
                f"Invalid --segment {spec!r}; expected ID=REFS"
            )
        segments.append({"id": segment_id, "refs": [selectors]})
    payload: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "analysis_id": analysis_id,
        "segments": segments,
        "focus_refs": focus_selectors,
    }
    if member_surah is not None or added_ayat_selectors:
        payload["surah_membership"] = {
            "target_surah": member_surah,
            "added_ayat_refs": added_ayat_selectors or [],
        }
    return composition_from_payload(payload)


def load_composition(path: Path) -> Composition:
    try:
        payload_bytes = path.read_bytes()
    except OSError as exc:
        raise CompositionError(f"Cannot read composition {path}: {exc}") from exc
    if len(payload_bytes) > MAX_SOURCE_JSON_BYTES:
        raise CompositionError(f"Composition JSON is too large: {path}")
    try:
        payload = json.loads(payload_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CompositionError(f"Invalid composition JSON {path}: {exc}") from exc
    return composition_from_payload(payload)


def unit_bundle_path(bundle_root: Path, ref: str) -> Path:
    canonical_ref = _validate_ref(ref)
    surah, ayah = (int(item) for item in canonical_ref.split(":"))
    direct = bundle_root / f"{surah}_{ayah}.ayah.json"
    nested = bundle_root / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json"
    direct_present = direct.exists() or direct.is_symlink()
    nested_present = nested.exists() or nested.is_symlink()
    if direct_present and nested_present:
        raise CompositionError(
            f"Ambiguous bundle layout for {canonical_ref}: both {direct} and {nested} exist"
        )
    if direct_present:
        return direct
    return nested


def load_unit_bundle(bundle_root: Path, ref: str) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    path = unit_bundle_path(bundle_root, ref)
    if not path.is_file() or path.is_symlink():
        raise CompositionError(f"Selected context bundle is missing or not regular: {path}")
    payload = path.read_bytes()
    if len(payload) > MAX_SOURCE_JSON_BYTES:
        raise CompositionError(f"Selected context bundle is too large: {path}")
    try:
        bundle = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CompositionError(f"Invalid context bundle JSON {path}: {exc}") from exc
    if not isinstance(bundle, dict):
        raise CompositionError(f"Context bundle must be one JSON object: {path}")
    identity = validate_unit_bundle(bundle, expected_ref=ref)
    identity["source_sha256"] = hashlib.sha256(payload).hexdigest()
    identity["canonical_sha256"] = canonical_sha256(bundle)
    identity["bytes"] = len(payload)
    return path, bundle, identity


def validate_unit_bundle(bundle: dict[str, Any], *, expected_ref: str) -> dict[str, Any]:
    expected_ref = _validate_ref(expected_ref)
    if bundle.get("bundle_type") != "ayah" or bundle.get("ayahRef") != expected_ref:
        raise CompositionError(f"Bundle identity does not match selected unit {expected_ref}")
    surah, ayah = (int(item) for item in expected_ref.split(":"))
    if bundle.get("surah") != surah or bundle.get("ayah") != ayah:
        raise CompositionError(f"Bundle numeric identity does not match {expected_ref}")
    unit_kind = bundle.get("unit_kind", "numbered_ayah")
    text = bundle.get("text")
    if not isinstance(text, dict) or not isinstance(text.get("arabic_uthmani"), str):
        raise CompositionError(f"{expected_ref} has no Arabic surface")
    if ayah == 0:
        if unit_kind != "prefatory_basmala":
            raise CompositionError(f"{expected_ref} must be a prefatory_basmala bundle")
        if bundle.get("surface_ref") != expected_ref:
            raise CompositionError(f"{expected_ref} surface_ref mismatch")
        linguistic_source_ref = bundle.get("linguistic_source_ref")
        if linguistic_source_ref != BASMALA_LINGUISTIC_SOURCE_REF:
            raise CompositionError(f"{expected_ref} must use linguistic source 1:1")
        alias = bundle.get("coverage", {}).get("basmala_alias", {})
        if (
            alias.get("normalized_surface_equivalent") is not True
            or alias.get("target_normalized") != alias.get("source_normalized")
            or alias.get("target_normalized")
            != normalize_arabic_surface(text["arabic_uthmani"])
            or alias.get("source_normalized") != BASMALA_NORMALIZED_SURFACE
        ):
            raise CompositionError(f"{expected_ref} lacks verified surface equivalence")
    else:
        if unit_kind != "numbered_ayah":
            raise CompositionError(f"{expected_ref} must be a numbered_ayah bundle")
        surface_ref = bundle.get("surface_ref", expected_ref)
        if surface_ref != expected_ref:
            raise CompositionError(
                f"Numbered unit {expected_ref} has aliased surface ref {surface_ref!r}"
            )
        linguistic_source_ref = bundle.get("linguistic_source_ref", expected_ref)
        if linguistic_source_ref != expected_ref:
            raise CompositionError(f"Numbered unit {expected_ref} has aliased linguistic refs")

    qac_rows = bundle.get("qac_morphemes")
    if not isinstance(qac_rows, list) or not qac_rows:
        raise CompositionError(f"{expected_ref} has no QAC morphology")
    for row in qac_rows:
        qac_ref = row.get("qac_ref") if isinstance(row, dict) else None
        match = QAC_REF_RE.fullmatch(qac_ref) if isinstance(qac_ref, str) else None
        if match is None or f"{int(match.group(1))}:{int(match.group(2))}" != linguistic_source_ref:
            raise CompositionError(
                f"{expected_ref} contains QAC ref outside linguistic source {linguistic_source_ref}"
            )
    word_analysis = bundle.get("word_analysis")
    if not isinstance(word_analysis, dict) or word_analysis.get("ref") != linguistic_source_ref:
        raise CompositionError(
            f"{expected_ref} word analysis does not belong to {linguistic_source_ref}"
        )
    return {
        "unit_kind": unit_kind,
        "ayah_ref": expected_ref,
        "surface_ref": bundle.get("surface_ref", expected_ref),
        "linguistic_source_ref": linguistic_source_ref,
        "schema_version": bundle.get("schema_version"),
    }


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _rooted_qac_rows(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    rows = bundle.get("qac_morphemes")
    if not isinstance(rows, list):
        return []
    return [
        row
        for row in rows
        if isinstance(row, dict)
        and isinstance(row.get("root_ar"), str)
        and bool(row["root_ar"].strip())
    ]


def _bundle_roots(bundle: dict[str, Any]) -> list[str]:
    return _ordered_unique(str(row["root_ar"]).strip() for row in _rooted_qac_rows(bundle))


def _qac_word_index(row: dict[str, Any]) -> str:
    value = row.get("word_index")
    if isinstance(value, int) and value > 0:
        return str(value)
    if isinstance(value, str) and value.isdigit() and int(value) > 0:
        return str(int(value))
    qac_ref = row.get("qac_ref")
    match = QAC_REF_RE.fullmatch(qac_ref) if isinstance(qac_ref, str) else None
    if match is None:
        raise CompositionError(f"Cannot recover QAC word index from {qac_ref!r}")
    return str(int(qac_ref.split(":", 3)[2]))


def _lean_context_ayah(bundle: dict[str, Any]) -> dict[str, Any]:
    context_ref = str(bundle["ayahRef"])
    rows = _rooted_qac_rows(bundle)
    root_sequence = [str(row["root_ar"]).strip() for row in rows]
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row["root_ar"]).strip(), []).append(row)
    root_occurrences = []
    for root in _ordered_unique(root_sequence):
        occurrences = grouped[root]
        root_occurrences.append({
            "root": root,
            "occurrence_count": len(occurrences),
            "word_indices": [_qac_word_index(row) for row in occurrences],
            "surfaces_ar": [
                str(row.get("surface_ar") or row.get("stem_ar") or "")
                for row in occurrences
            ],
            "lemmas_ar": [str(row.get("lemma_ar") or "") for row in occurrences],
            "pos_tags": [
                str(row.get("source_pos") or row.get("pos") or "")
                for row in occurrences
            ],
        })
    ayah = {
        "ref": context_ref,
        "text_ar": bundle["text"]["arabic_uthmani"],
        "root_sequence": root_sequence,
        "root_occurrences": root_occurrences,
    }
    if not rows:
        ayah.update({
            "rootless": True,
            "rootless_reason": "QAC has no rooted morphemes for this ayah",
        })
    return ayah


def _root_target_metadata(
    bundle: dict[str, Any], qac_root: str
) -> dict[str, dict[str, Any]]:
    coverage = bundle.get("coverage")
    root_coverage = coverage.get("root_lexicon") if isinstance(coverage, dict) else None
    per_root = root_coverage.get("per_root") if isinstance(root_coverage, dict) else None
    row = per_root.get(qac_root) if isinstance(per_root, dict) else None
    mapping = row.get("root_mapping") if isinstance(row, dict) else None
    raw_targets = mapping.get("targets") if isinstance(mapping, dict) else None
    result: dict[str, dict[str, Any]] = {}
    if isinstance(raw_targets, list):
        for index, target in enumerate(raw_targets):
            if not isinstance(target, dict):
                continue
            root_id = target.get("furuq_root_id")
            root_norm = target.get("furuq_root_norm")
            if isinstance(root_id, str) and root_id and isinstance(root_norm, str) and root_norm:
                result[root_id] = {
                    "mapped_root_norm": root_norm,
                    "target_rank": target.get("target_rank", index + 1),
                }

    root_lexicon = bundle.get("root_lexicon")
    if isinstance(root_lexicon, dict):
        for root_id, record in root_lexicon.items():
            if not isinstance(root_id, str) or not isinstance(record, dict):
                continue
            qac_roots = record.get("qac_roots_ar")
            if not isinstance(qac_roots, list):
                qac_roots = [record.get("root_ar")]
            if qac_root not in qac_roots:
                continue
            mappings = record.get("qac_root_mappings")
            rank = None
            if isinstance(mappings, list):
                match = next(
                    (
                        item
                        for item in mappings
                        if isinstance(item, dict) and item.get("root_ar") == qac_root
                    ),
                    None,
                )
                if match is not None:
                    rank = match.get("target_rank")
            result.setdefault(root_id, {
                "mapped_root_norm": str(record.get("root_ar") or qac_root),
                "target_rank": rank if isinstance(rank, int) else len(result) + 1,
            })
    return result


def _context_root_cues(
    bundle: dict[str, Any], *, focus_roots: set[str]
) -> list[dict[str, Any]]:
    packet = bundle.get("branch_inventories")
    packet = packet.get("full_context_packet") if isinstance(packet, dict) else None
    inventories = packet.get("branch_inventories") if isinstance(packet, dict) else None
    if not isinstance(inventories, list):
        return []
    inventories_by_root = {
        inventory.get("root"): inventory
        for inventory in inventories
        if isinstance(inventory, dict) and isinstance(inventory.get("root"), str)
    }
    result: list[dict[str, Any]] = []
    for qac_root in _bundle_roots(bundle):
        if qac_root in focus_roots:
            continue
        inventory = inventories_by_root.get(qac_root)
        if not isinstance(inventory, dict):
            continue
        target_metadata = _root_target_metadata(bundle, qac_root)
        targets: dict[str, dict[str, Any]] = {}
        for branch in inventory.get("branches", []):
            if not isinstance(branch, dict):
                continue
            branch_id = branch.get("branch_id")
            if not isinstance(branch_id, str) or not branch_id:
                continue
            variants = branch.get("variants")
            if not isinstance(variants, list) or not variants:
                variants = [branch]
            for variant in variants:
                if not isinstance(variant, dict):
                    continue
                root_id = variant.get("root_id") or branch.get("root_id")
                if not isinstance(root_id, str) or not root_id:
                    if len(target_metadata) == 1:
                        root_id = next(iter(target_metadata))
                    else:
                        continue
                metadata = target_metadata.get(root_id, {})
                root_norm = metadata.get("mapped_root_norm")
                if not isinstance(root_norm, str) or not root_norm:
                    root_norm = qac_root
                image = (
                    variant.get("image_ar")
                    or variant.get("branch_image_ar")
                    or branch.get("image_ar")
                    or branch.get("branch_image_ar")
                )
                if not isinstance(image, str) or not image:
                    continue
                target = targets.setdefault(root_id, {
                    "mapped_root_id": root_id,
                    "mapped_root_norm": root_norm,
                    "target_rank": metadata.get("target_rank", len(targets) + 1),
                    "branches": [],
                })
                branch_item = {"branch_id": branch_id, "branch_image_ar": image}
                if branch_item not in target["branches"]:
                    target["branches"].append(branch_item)
        root_lexicon = bundle.get("root_lexicon")
        if isinstance(root_lexicon, dict):
            for root_id, metadata in target_metadata.items():
                if root_id in targets:
                    continue
                record = root_lexicon.get(root_id)
                dictionary = (
                    record.get("dictionary_entry") if isinstance(record, dict) else None
                )
                dictionary_branches = (
                    dictionary.get("branches") if isinstance(dictionary, dict) else None
                )
                if not isinstance(dictionary_branches, list):
                    continue
                compact_branches = []
                for branch in dictionary_branches:
                    if not isinstance(branch, dict):
                        continue
                    branch_ref = branch.get("branch_ref")
                    image = branch.get("branch_image_ar")
                    if (
                        not isinstance(branch_ref, str)
                        or not branch_ref.startswith(f"{root_id}/")
                        or not isinstance(image, str)
                        or not image
                    ):
                        continue
                    compact_branches.append({
                        "branch_id": branch_ref.split("/", 1)[1],
                        "branch_image_ar": image,
                    })
                if compact_branches:
                    targets[root_id] = {
                        "mapped_root_id": root_id,
                        "mapped_root_norm": metadata["mapped_root_norm"],
                        "target_rank": metadata.get("target_rank", len(targets) + 1),
                        "branches": compact_branches,
                    }
        for target in targets.values():
            target["branches"].sort(
                key=lambda branch: (
                    int(branch["branch_id"][1:])
                    if branch["branch_id"].startswith("B")
                    and branch["branch_id"][1:].isdigit()
                    else 10**9,
                    branch["branch_id"],
                )
            )
        ordered_targets_with_rank = sorted(
            (target for target in targets.values() if target["branches"]),
            key=lambda target: (target["target_rank"], target["mapped_root_id"]),
        )
        ordered_targets = [
            {key: value for key, value in target.items() if key != "target_rank"}
            for target in ordered_targets_with_rank
        ]
        if ordered_targets:
            result.append({"root": qac_root, "targets": ordered_targets})
    return result


def context_member_payload(
    bundle: dict[str, Any], *, focus_bundle: dict[str, Any]
) -> dict[str, Any]:
    """Return the same lean evidence categories used for an HFT context ayah."""
    context_ref = str(bundle["ayahRef"])
    return {
        "protocol": CONTEXT_MEMBER_PROTOCOL,
        "context_order": [context_ref],
        "context_ayat": [_lean_context_ayah(bundle)],
        "context_root_cues": _context_root_cues(
            bundle, focus_roots=set(_bundle_roots(focus_bundle))
        ),
    }


def project_context_unit(
    *,
    composition: Composition,
    focus_ref: str,
    context_row: dict[str, Any],
    source_path: Path,
    bundle: dict[str, Any],
    focus_bundle: dict[str, Any],
    identity: dict[str, Any],
    projects_root: Path,
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    """Project one full bundle at native non-focus context depth."""
    context_ref = context_row["ref"]
    lane = context_row["lane"]
    try:
        stable_source_file = str(
            source_path.resolve(strict=False).relative_to(
                projects_root.resolve(strict=False)
            )
        )
    except ValueError:
        stable_source_file = str(source_path)
    unit_provenance = {
        **identity,
        "source_file": stable_source_file,
        "segment_id": context_row["segment_id"],
        "composition_order": context_row["composition_order"],
    }
    payload = context_member_payload(bundle, focus_bundle=focus_bundle)
    projection_sha256 = canonical_sha256(payload)
    support_id = _stable_id("sup_ctx", {
        "context_ref": context_ref,
        "source_bundle_canonical_sha256": identity["canonical_sha256"],
        "projection_sha256": projection_sha256,
        "lane": lane,
    })
    supports = [{
        "support_id": support_id,
        "source_type": "selected_context_native_depth",
        "source_local_id": f"{context_ref}:native_context_member",
        "scope": lane,
        "json_pointer": f"/selected_context/{context_ref}/native_context_member",
        "role": "context_unit_native_depth_evidence",
        "branch_refs": [],
        "payload": payload,
        "context_refs": [context_ref],
        "trust": "canonical_bundle_hash_bound",
        "qualification": {
            "context_unit_is_not_the_focus": True,
            "projection_depth": "hft_non_focus_context",
            "standalone_focus_material_excluded": True,
            "source_bundle_canonical_sha256": identity["canonical_sha256"],
            "context_projection_sha256": projection_sha256,
        },
    }]
    support_ids = [support_id]

    candidate_id = _stable_id("cand_ctx", {
        "analysis_sha256": composition.canonical_sha256,
        "focus_ref": focus_ref,
        "context_ref": context_ref,
        "lane": lane,
    })
    candidate = {
        "candidate_id": candidate_id,
        "ayah_ref": focus_ref,
        "lane": lane,
        "source_type": "selected_context_unit",
        "source_local_id": context_ref,
        "source_pointer": context_row["source_pointer"],
        "kind": "ordered_context_unit",
        "title": f"Selected context {context_ref}",
        "scope": "analysis_composition",
        "anchor_refs": [context_ref],
        "branch_refs": [],
        "support_ids": support_ids,
        "trust": "canonical_bundle_hash_bound",
        "analysis_id": composition.analysis_id,
        "segment_id": context_row["segment_id"],
        "composition_order": context_row["composition_order"],
        "commentary_obligation": "review",
    }
    inventory = {
        **unit_provenance,
        "context_projection_protocol": CONTEXT_MEMBER_PROTOCOL,
        "context_projection_sha256": projection_sha256,
        "context_projection_bytes": len(_canonical_json_bytes(payload)),
        "lane": lane,
        "candidate_id": candidate_id,
        "support_ids": support_ids,
    }
    if context_row.get("membership_added_ayah") is True:
        target_surah = context_row["membership_target_surah"]
        candidate.update({
            "source_type": "external_ayah_member",
            "kind": "external_ayah_member",
            "scope": "host_surah_membership",
            "title": f"External ayah {context_ref} in S{target_surah} context",
            "membership_target_surah": target_surah,
            "membership_added_ayah": True,
            "focus_eligible": False,
        })
        for support in supports:
            support.setdefault("qualification", {}).update({
                "host_surah_membership": True,
                "membership_target_surah": target_surah,
                "membership_added_ayah": True,
                "focus_eligible": False,
            })
        inventory.update({
            "host_surah_membership": True,
            "membership_target_surah": target_surah,
            "membership_added_ayah": True,
            "focus_eligible": False,
        })
    return candidate, supports, inventory
