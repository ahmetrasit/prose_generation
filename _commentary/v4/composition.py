"""Ordered context compositions for the simple commentary v4 workflow."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "commentary-v4-analysis-composition-v1"
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
BASMALA_EXCLUDED_SURAHS = {1, 9}

DERIVED_FIELDS = (
    "v12_reader_responses",
    "v12_reader_walks",
    "v12_reader_walks_wide",
    "v12_cross_run_publication",
    "butuncul_okuma_line",
    "inter_ayah_rows",
    "channel_subchannels_anchored_here",
    "channel_generated_outputs",
)


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
    added_member_refs: tuple[str, ...] = ()

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
                "added_refs": list(self.added_member_refs),
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

    def context_rows(self, focus_ref: str) -> list[dict[str, Any]]:
        if focus_ref not in self.focus_refs:
            raise CompositionError(
                f"Focus {focus_ref} is not declared by analysis {self.analysis_id}"
            )
        focus_segment = self.segment_for(focus_ref).segment_id
        focus_surah = focus_ref.split(":", 1)[0]
        rows: list[dict[str, Any]] = []
        order = 0
        for segment_index, segment in enumerate(self.segments):
            for unit_index, ref in enumerate(segment.refs):
                if ref == focus_ref:
                    continue
                lane = (
                    "macro"
                    if segment.segment_id == focus_segment
                    and ref.split(":", 1)[0] == focus_surah
                    else "global"
                )
                rows.append({
                    "ref": ref,
                    "segment_id": segment.segment_id,
                    "segment_index": segment_index,
                    "unit_index": unit_index,
                    "composition_order": order,
                    "lane": lane,
                })
                order += 1
        return rows

    def surah_membership_refs(self) -> tuple[str, ...]:
        if self.member_surah is None:
            return ()
        target_prefix = f"{self.member_surah}:"
        refs = [
            ref
            for ref in self.ordered_refs
            if ref.startswith(target_prefix) or ref in self.added_member_refs
        ]
        seen: set[str] = set()
        return tuple(ref for ref in refs if not (ref in seen or seen.add(ref)))

    def surah_membership_rows(
        self, focus_ref: str, lanes: Iterable[str]
    ) -> list[dict[str, Any]]:
        if self.member_surah is None:
            return []
        if focus_ref not in self.focus_refs:
            raise CompositionError(
                f"Focus {focus_ref} is not declared by analysis {self.analysis_id}"
            )
        member_refs = self.surah_membership_refs()
        if focus_ref not in member_refs:
            raise CompositionError(
                f"Focus {focus_ref} is outside augmented surah membership"
            )
        target_prefix = f"{self.member_surah}:"
        focus_is_added = focus_ref in self.added_member_refs
        rows: list[dict[str, Any]] = []
        order = 0
        for ref in member_refs:
            if ref == focus_ref:
                continue
            if not focus_is_added and ref not in self.added_member_refs:
                continue
            for lane in lanes:
                rows.append({
                    "ref": ref,
                    "segment_id": "augmented-surah-membership",
                    "segment_index": -1,
                    "unit_index": order,
                    "composition_order": order,
                    "lane": lane,
                    "membership_target_surah": self.member_surah,
                    "membership_added_ref": ref in self.added_member_refs,
                    "membership_focus_is_added_ref": focus_is_added,
                    "membership_ref_is_target_surah": ref.startswith(target_prefix),
                })
            order += 1
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
    if len(all_refs) < 2:
        raise CompositionError("A contextual composition requires at least two units")
    for focus_ref in focus_refs:
        if len(set(all_refs) - {focus_ref}) == 0:
            raise CompositionError(f"Focus {focus_ref} has no contextual unit")
    description = payload.get("description")
    if description is not None and not isinstance(description, str):
        raise CompositionError("description must be a string")
    member_surah = None
    added_member_refs: tuple[str, ...] = ()
    membership = payload.get("surah_membership")
    if membership is not None:
        if not isinstance(membership, dict):
            raise CompositionError("surah_membership must be an object")
        if set(membership) != {"target_surah", "added_refs"}:
            raise CompositionError(
                "surah_membership must contain target_surah and added_refs"
            )
        member_surah = membership.get("target_surah")
        if not isinstance(member_surah, int) or not 1 <= member_surah <= 114:
            raise CompositionError("surah_membership.target_surah must be 1-114")
        raw_added = membership.get("added_refs")
        if not isinstance(raw_added, (str, list, tuple)):
            raise CompositionError("surah_membership.added_refs must be selectors")
        added_member_refs = tuple(expand_selectors(raw_added))
        if not added_member_refs:
            raise CompositionError("surah_membership.added_refs cannot be empty")
        outside = sorted(set(added_member_refs) - set(all_refs))
        if outside:
            raise CompositionError(
                f"Added surah members are outside the composition: {outside}"
            )
        target_refs = [
            ref for ref in all_refs if ref.startswith(f"{member_surah}:")
        ]
        if not target_refs:
            raise CompositionError(
                "surah_membership requires at least one target-surah unit"
            )
        member_refs = set(target_refs) | set(added_member_refs)
        outside_focus = sorted(set(focus_refs) - member_refs)
        if outside_focus:
            raise CompositionError(
                f"Focus refs are outside augmented surah membership: {outside_focus}"
            )
    return Composition(
        analysis_id=analysis_id,
        segments=tuple(segments),
        focus_refs=tuple(focus_refs),
        description=description,
        member_surah=member_surah,
        added_member_refs=added_member_refs,
    )


def composition_from_cli(
    analysis_id: str,
    segment_specs: list[str],
    focus_selectors: list[str],
    *,
    member_surah: int | None = None,
    added_member_selectors: list[str] | None = None,
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
    if member_surah is not None or added_member_selectors:
        payload["surah_membership"] = {
            "target_surah": member_surah,
            "added_refs": added_member_selectors or [],
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
    if direct.exists() or direct.is_symlink():
        return direct
    return bundle_root / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json"


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
        ):
            raise CompositionError(f"{expected_ref} lacks verified surface equivalence")
    else:
        if unit_kind != "numbered_ayah":
            raise CompositionError(f"{expected_ref} must be a numbered_ayah bundle")
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


def _load_hft_source_packet(
    bundle: dict[str, Any], *, projects_root: Path, context_ref: str
) -> dict[str, Any] | None:
    hft = bundle.get("v12_focus_trace_hermetic")
    if not isinstance(hft, dict) or not hft:
        return None
    summary = hft.get("packet_summary")
    if not isinstance(summary, dict):
        return None
    source_file = summary.get("source_file")
    if not isinstance(source_file, str) or not source_file:
        raise CompositionError(f"{context_ref} HFT summary has no source_file")
    source_path = (projects_root / source_file).resolve(strict=False)
    try:
        source_path.relative_to(projects_root.resolve(strict=False))
    except ValueError as exc:
        raise CompositionError(f"{context_ref} HFT packet path escapes projects root") from exc
    if not source_path.is_file() or source_path.is_symlink():
        raise CompositionError(
            f"{context_ref} HFT packet is unavailable for hermetic projection: {source_path}"
        )
    payload = source_path.read_bytes()
    if len(payload) > MAX_SOURCE_JSON_BYTES:
        raise CompositionError(f"{context_ref} HFT packet is too large")
    try:
        packet = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise CompositionError(f"Invalid HFT packet for {context_ref}: {exc}") from exc
    if not isinstance(packet, dict) or packet.get("focus_ref") != context_ref:
        raise CompositionError(f"HFT packet focus does not match {context_ref}")
    return {
        "source_file": source_file,
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "canonical_sha256": canonical_sha256(packet),
        "packet": packet,
    }


def _nonempty(value: Any) -> bool:
    return value is not None and value != {} and value != [] and value != ""


def project_context_unit(
    *,
    composition: Composition,
    focus_ref: str,
    context_row: dict[str, Any],
    source_path: Path,
    bundle: dict[str, Any],
    identity: dict[str, Any],
    projects_root: Path,
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    """Project every semantic field into existing candidate/support shapes."""
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
    supports: list[dict[str, Any]] = []

    def add_support(role: str, payload: Any, *, source_type: str) -> str:
        stable_payload = {
            "context_ref": context_ref,
            "source_bundle_canonical_sha256": identity["canonical_sha256"],
            "role": role,
            "payload": payload,
        }
        support_id = _stable_id("sup_ctx", stable_payload)
        supports.append({
            "support_id": support_id,
            "source_type": source_type,
            "source_local_id": f"{context_ref}:{role}",
            "scope": lane,
            "json_pointer": f"/selected_context/{context_ref}/{role}",
            "role": role,
            "branch_refs": [],
            "payload": payload,
            "context_refs": [context_ref],
            "trust": "canonical_bundle_hash_bound",
            "qualification": {
                "context_unit_is_not_the_focus": True,
                "derived_focus_readings_keep_original_provenance": True,
                "source_bundle_canonical_sha256": identity["canonical_sha256"],
            },
        })
        return support_id

    support_ids: list[str] = []
    support_ids.append(add_support(
        "context_unit_intrinsic_linguistic_evidence",
        {
            "identity": unit_provenance,
            "text": bundle.get("text"),
            "qac_morphemes": bundle.get("qac_morphemes"),
            "word_analysis": bundle.get("word_analysis"),
            "word_morpheme_spans": bundle.get("word_morpheme_spans"),
            "pericope": bundle.get("pericope"),
            "coverage": bundle.get("coverage"),
        },
        source_type="selected_context_intrinsic",
    ))
    branch_inventories = bundle.get("branch_inventories")
    if _nonempty(branch_inventories):
        support_ids.append(add_support(
            "context_unit_branch_inventories",
            branch_inventories,
            source_type="selected_context_branches",
        ))
    root_lexicon = bundle.get("root_lexicon")
    if isinstance(root_lexicon, dict):
        for root_id in sorted(root_lexicon):
            support_ids.append(add_support(
                "context_root_lexicon",
                {"root_id": root_id, "record": root_lexicon[root_id]},
                source_type="selected_context_root",
            ))

    hft = bundle.get("v12_focus_trace_hermetic")
    if _nonempty(hft):
        support_ids.append(add_support(
            "prior_focus_hft_evidence",
            {
                "original_focus_ref": context_ref,
                "bundle_evidence": hft,
                "source_packet": _load_hft_source_packet(
                    bundle, projects_root=projects_root, context_ref=context_ref
                ),
                "boundary": (
                    "This HFT run analyzed the context unit as its own focus in "
                    "its original packet window. It is prior focus-conditioned "
                    "evidence, not an intrinsic fact and not a custom-composition run."
                ),
            },
            source_type="selected_context_prior_hft",
        ))
    for field in DERIVED_FIELDS:
        value = bundle.get(field)
        if not _nonempty(value):
            continue
        support_ids.append(add_support(
            "prior_focus_derived_evidence",
            {
                "field": field,
                "original_focus_ref": context_ref,
                "payload": value,
                "boundary": (
                    "This material was generated with the selected context unit "
                    "as its original focus. Preserve that direction and provenance."
                ),
            },
            source_type="selected_context_prior_reading",
        ))

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
        "source_pointer": (
            "/scope/analysis_composition/context_refs/"
            f"{context_row['composition_order']}"
        ),
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
        "lane": lane,
        "candidate_id": candidate_id,
        "support_ids": support_ids,
    }
    return candidate, supports, inventory
