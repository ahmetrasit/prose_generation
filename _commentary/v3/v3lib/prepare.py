"""Prepare a trusted, compact adjudication docket from one ayah bundle."""

from __future__ import annotations

import copy
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .common import (
    BudgetError,
    INPUTS_ROOT,
    ScopeError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    json_pointer_escape,
    load_json_object,
    parse_json_object_bytes,
    preflight_confined_writes,
    pretty_json_bytes,
    sha256_bytes,
    write_bytes_confined,
)


DOCKET_SCHEMA = "commentary-v3-candidate-docket-v2"
PREPARED_SCHEMA = "commentary-v3-prepared-v1"
PERICOPE_HFT_PROTOCOL = "focus-trace-pericope-lean-v1"
SURAH_HFT_PROTOCOL = "focus-trace-surah-lean-v1"
HFT_RESPONSE_PROTOCOL = "focus-trace-hermetic-response-v4"
MAX_PERICOPE_AYAHS_CAP = 512
BRANCH_REF_RE = re.compile(r"root_[0-9]+[/ :]B[0-9]+")
ROOT_ID_RE = re.compile(r"^root_[0-9]+$")
CANONICAL_BRANCH_REF_RE = re.compile(r"^root_[0-9]+/B[0-9]+$")
REF_RE = re.compile(r"^([0-9]+):([0-9]+)$")
WORD_REF_RE = re.compile(r"^([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*)$")
QAC_REF_RE = re.compile(
    r"^([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*)$"
)
WORD_TOPIC_SOURCE_POINTER_RE = re.compile(
    r"^/word_analysis/words/([0-9]+)/topics/[0-9]+$"
)
BRANCH_ID_RE = re.compile(r"^B[0-9]+$")
AYAH_REF_SCAN_RE = re.compile(r"(?<![0-9])([0-9]+):([0-9]+)(?![0-9])")
ARABIC_ROOT_SCAN_RE = re.compile(
    r"(?P<root>[\u0621-\u064a](?:\s+[\u0621-\u064a]){2,3})"
    r"(?P<tail>[^.;\n]{0,160})"
)
IMMEDIATE_BRANCH_RE = re.compile(r"^[`'\"،,\s:/-]*(B[0-9]+)")
FOLLOWUP_BRANCH_RE = re.compile(
    r"(?P<joiner>and|ve)\s+`?(?P<branch>B[0-9]+)`?", re.IGNORECASE
)
ARABIC_ROOT_EQUIVALENTS = str.maketrans(
    {
        "آ": "ء",
        "أ": "ء",
        "إ": "ء",
        "ؤ": "ء",
        "ئ": "ء",
        "ى": "ي",
    }
)
SUPPORT_ROLE_OCCURRENCE = "focus_occurrence"
SUPPORT_ROLE_EVIDENCE = "candidate_evidence"
SUPPORT_ROLE_NOMINATION = "branch_nomination"
SUPPORT_ROLE_CONTEXT = "context_only"
WORD_SUPPORT_POINTER_RE = re.compile(r"^/word_analysis/words/[0-9]+$")
WORD_TOPIC_POINTER_RE = re.compile(
    r"^/word_analysis/words/[0-9]+/topics/[0-9]+$"
)
QAC_MORPHEME_POINTER_RE = re.compile(r"^/qac_morphemes/[0-9]+$")
CHANNEL_SUPPORT_POINTER_RE = re.compile(
    r"^/channel_subchannels_anchored_here/[0-9]+/"
    r"(scene_or_process|synthesis|active_motifs|ayah_anchors|parent_semantic_invariant)$"
)
HFT_SUPPORT_POINTER_RE = re.compile(
    r"^/v12_focus_trace_hermetic/readers/[^/]+/"
    r"(?:baseline_models|context_deltas|surprising_valid_outliers)/[0-9]+"
    r"(?:/(activation_trace|structural_cues))?$"
)
READER_WALK_SUPPORT_POINTER_RE = re.compile(
    r"^/v12_reader_walks(?:_wide)?/[^/]+/"
    r"(?:activated_readings_md|retrospective_surprises_md)$"
)
CROSS_RUN_SUPPORT_POINTER_RE = re.compile(
    r"^/v12_cross_run_publication/findings/[0-9]+$"
)
LEGACY_RESPONSE_SUPPORT_POINTER_RE = re.compile(
    r"^/v12_reader_responses/[^/]+$"
)
WORD_TOPIC_OBLIGATIONS = {"must_integrate", "candidate", "ledger_only"}
CANDIDATE_SOURCE_TYPES = {
    "word_analysis",
    "qac_morpheme",
    "channel",
    "hft",
    "v12_reader_walks",
    "v12_reader_walks_wide",
    "cross_run_publication",
    "legacy_reader_response",
}
LEDGER_DISPOSITIONS = {
    "docket_mandatory",
    "docket_optional",
    "quarantined",
    "duplicate",
    "parse_failed",
    "out_of_scope",
}
SELECTION_INELIGIBILITY_REASONS = {
    "legacy_unbound",
    "ledger_only",
    "no_candidate_evidence",
    "not_adjudicable",
    "occurrence_only",
}


def support_role_for(source_type: str, json_pointer: str) -> str:
    if source_type == "word_analysis":
        if WORD_SUPPORT_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_EVIDENCE
        if WORD_TOPIC_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_EVIDENCE
    elif source_type == "qac_morpheme":
        if QAC_MORPHEME_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_OCCURRENCE
    elif source_type == "channel":
        match = CHANNEL_SUPPORT_POINTER_RE.fullmatch(json_pointer)
        if match:
            field = match.group(1)
            if field == "active_motifs":
                return SUPPORT_ROLE_NOMINATION
            if field in ("scene_or_process", "synthesis"):
                return SUPPORT_ROLE_EVIDENCE
            return SUPPORT_ROLE_CONTEXT
    elif source_type == "hft":
        match = HFT_SUPPORT_POINTER_RE.fullmatch(json_pointer)
        if match:
            return (
                SUPPORT_ROLE_NOMINATION
                if match.group(1) == "activation_trace"
                else SUPPORT_ROLE_EVIDENCE
            )
    elif source_type in ("v12_reader_walks", "v12_reader_walks_wide"):
        if READER_WALK_SUPPORT_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_EVIDENCE
    elif source_type == "cross_run_publication":
        if CROSS_RUN_SUPPORT_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_EVIDENCE
    elif source_type == "legacy_reader_response":
        if LEGACY_RESPONSE_SUPPORT_POINTER_RE.fullmatch(json_pointer):
            return SUPPORT_ROLE_CONTEXT
    raise ValidationError(
        f"Unsupported support provenance: {source_type} {json_pointer}"
    )


def _selection_eligibility(
    candidate: dict[str, Any], support_map: dict[str, dict[str, Any]]
) -> tuple[bool, list[str]]:
    """Classify whether a source candidate may consume an adjudication decision."""
    reasons: set[str] = set()
    if not candidate["adjudicable"]:
        reasons.add("not_adjudicable")
    if candidate["trust"] != "trusted":
        reasons.add("legacy_unbound")
    if candidate["obligation"] == "ledger_only":
        reasons.add("ledger_only")
    if (
        candidate["source_type"] == "qac_morpheme"
        or candidate["kind"] == "focus_root_occurrence"
    ):
        reasons.add("occurrence_only")
    if not any(
        support_id in support_map
        and support_map[support_id]["trust"] == "trusted"
        and support_map[support_id]["citable"] is True
        and support_map[support_id]["role"] == SUPPORT_ROLE_EVIDENCE
        and set(support_map[support_id]["branch_refs"])
        <= set(candidate["branch_refs"])
        for support_id in candidate["support_ids"]
    ):
        reasons.add("no_candidate_evidence")
    normalized = sorted(reasons)
    return not normalized, normalized


@dataclass(frozen=True)
class PrepareOptions:
    hft_policy: str = "strict"
    allow_legacy_hft_response: bool = False
    allow_incomplete_branch_coverage: bool = False
    max_optional_candidates: int = 40
    max_support_chars: int = 1_600
    max_support_per_candidate: int = 5
    max_branch_bytes_per_root: int = 32_000
    max_pericope_ayahs: int = 512
    max_docket_bytes: int = 500_000

    def validate(self) -> None:
        if not isinstance(self.hft_policy, str) or self.hft_policy not in (
            "strict",
            "quarantine",
        ):
            raise ValidationError(
                "hft_policy must be one of: strict, quarantine"
            )
        if not isinstance(self.allow_legacy_hft_response, bool):
            raise ValidationError("allow_legacy_hft_response must be boolean")
        if not isinstance(self.allow_incomplete_branch_coverage, bool):
            raise ValidationError(
                "allow_incomplete_branch_coverage must be boolean"
            )
        for name in (
            "max_optional_candidates",
            "max_support_chars",
            "max_support_per_candidate",
            "max_branch_bytes_per_root",
            "max_pericope_ayahs",
            "max_docket_bytes",
        ):
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValidationError(f"{name} must be a positive integer")
        if self.max_pericope_ayahs > MAX_PERICOPE_AYAHS_CAP:
            raise ValidationError(
                f"max_pericope_ayahs may not exceed {MAX_PERICOPE_AYAHS_CAP}"
            )


def _require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def _optional_dict(container: dict[str, Any], key: str, label: str) -> dict[str, Any]:
    value = container.get(key)
    if value is None:
        return {}
    return _require_dict(value, label)


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    return value


def _require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        raise ValidationError(
            f"{label} fields disagree with contract; missing={missing}, extra={extra}"
        )


def _require_canonical_branch_ref(value: Any, label: str) -> str:
    if not isinstance(value, str) or not CANONICAL_BRANCH_REF_RE.fullmatch(value):
        raise ValidationError(f"{label} is not a canonical branch ref")
    return value


def _compact_text(value: Any) -> str:
    if isinstance(value, str):
        return " ".join(value.split())
    return canonical_json_bytes(value).decode("utf-8")


def _stable_id(prefix: str, payload: dict[str, Any]) -> str:
    return f"{prefix}_{canonical_sha256(payload)[:20]}"


def _canonical_arabic_root(value: str) -> str:
    """Normalize orthographic root variants without changing stored evidence."""
    return " ".join(value.translate(ARABIC_ROOT_EQUIVALENTS).split())


def _normalize_branch_ref(value: str) -> str:
    match = re.fullmatch(r"(root_[0-9]+)[/ :](B[0-9]+)", value.strip())
    if not match:
        raise ValidationError(f"Invalid branch ref: {value!r}")
    return f"{match.group(1)}/{match.group(2)}"


def _is_identifier_continuation(char: str) -> bool:
    category = unicodedata.category(char)
    return category[0] in ("L", "M", "N") or category in ("Pc", "Cf")


def _match_is_token_bounded(
    text: str, match: re.Match[str], *, group: int | str = 0
) -> bool:
    start, end = match.span(group)
    return not (
        (start and _is_identifier_continuation(text[start - 1]))
        or (end < len(text) and _is_identifier_continuation(text[end]))
    )


def _extract_branch_refs(value: Any) -> list[str]:
    text = value if isinstance(value, str) else _compact_text(value)
    refs = {
        _normalize_branch_ref(match.group(0))
        for match in BRANCH_REF_RE.finditer(text)
        if _match_is_token_bounded(text, match)
    }
    return sorted(refs)


def _activation_branch_refs(value: Any) -> list[str]:
    if not isinstance(value, list):
        raise ValidationError("activation_trace must be an array")
    refs: set[str] = set()
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValidationError(f"activation_trace[{index}] must be an object")
        root_id = item.get("mapped_root_id")
        branch_id = item.get("branch_id")
        if not isinstance(root_id, str) or not ROOT_ID_RE.fullmatch(root_id):
            raise ValidationError(
                f"activation_trace[{index}].mapped_root_id must be canonical"
            )
        if not isinstance(branch_id, str) or not BRANCH_ID_RE.fullmatch(branch_id):
            raise ValidationError(
                f"activation_trace[{index}].branch_id must be canonical"
            )
        refs.add(f"{root_id}/{branch_id}")
    return sorted(refs)


class BranchResolver:
    """Resolve root-id and legacy Arabic-root branch citations deterministically."""

    def __init__(
        self,
        *,
        root_ids_by_arabic: dict[str, list[str]],
        available_branch_refs: set[str],
        grounding_root_ids_by_arabic: dict[str, list[str]] | None = None,
    ) -> None:
        def canonicalize(
            mappings: dict[str, list[str]],
        ) -> dict[str, list[str]]:
            canonical_mappings: dict[str, set[str]] = {}
            for root, root_ids in mappings.items():
                canonical_mappings.setdefault(
                    _canonical_arabic_root(root), set()
                ).update(root_ids)
            return {
                root: sorted(root_ids)
                for root, root_ids in sorted(canonical_mappings.items())
            }

        self.root_ids_by_arabic = canonicalize(root_ids_by_arabic)
        grounding_mappings = (
            root_ids_by_arabic
            if grounding_root_ids_by_arabic is None
            else grounding_root_ids_by_arabic
        )
        self.grounding_root_ids_by_arabic = canonicalize(grounding_mappings)
        self.available_branch_refs = available_branch_refs

    def resolve_text(
        self, value: Any
    ) -> tuple[list[str], list[dict[str, str]]]:
        text = value if isinstance(value, str) else _compact_text(value)
        explicit_refs = set(_extract_branch_refs(text))
        resolved = explicit_refs & self.available_branch_refs
        unresolved: list[dict[str, str]] = []
        for branch_ref in sorted(explicit_refs - self.available_branch_refs):
            unresolved.append(
                {
                    "citation": branch_ref,
                    "reason": "no registered branch match",
                }
            )
        for match in ARABIC_ROOT_SCAN_RE.finditer(text):
            if not _match_is_token_bounded(text, match, group="root"):
                continue
            root_ar = " ".join(match.group("root").split())
            canonical_root = _canonical_arabic_root(root_ar)
            tail = match.group("tail")
            immediate = IMMEDIATE_BRANCH_RE.match(tail)
            branch_ids = {
                follow.group("branch")
                for follow in FOLLOWUP_BRANCH_RE.finditer(tail)
                if _match_is_token_bounded(tail, follow, group="joiner")
                and _match_is_token_bounded(tail, follow, group="branch")
            }
            if immediate and _match_is_token_bounded(tail, immediate, group=1):
                branch_ids.add(immediate.group(1))
            for branch_id in branch_ids:
                candidates = [
                    f"{root_id}/{branch_id}"
                    for root_id in self.root_ids_by_arabic.get(canonical_root, [])
                    if f"{root_id}/{branch_id}" in self.available_branch_refs
                ]
                citation = f"{root_ar}/{branch_id}"
                if len(candidates) == 1:
                    resolved.add(candidates[0])
                elif not candidates:
                    unresolved.append(
                        {"citation": citation, "reason": "no registered branch match"}
                    )
                else:
                    unresolved.append(
                        {
                            "citation": citation,
                            "reason": "ambiguous root mapping: " + ", ".join(candidates),
                        }
                    )
        return sorted(resolved), sorted(
            unresolved, key=lambda item: (item["citation"], item["reason"])
        )

    def root_ids_in_text(self, value: Any) -> list[str]:
        text = value if isinstance(value, str) else _compact_text(value)
        root_ids: set[str] = set()
        for match in ARABIC_ROOT_SCAN_RE.finditer(text):
            if not _match_is_token_bounded(text, match, group="root"):
                continue
            canonical_root = _canonical_arabic_root(match.group("root"))
            root_ids.update(
                self.grounding_root_ids_by_arabic.get(canonical_root, [])
            )
        return sorted(root_ids)


class SupportBuilder:
    def __init__(self, *, max_chars: int) -> None:
        self.max_chars = max_chars
        self._items: dict[str, dict[str, Any]] = {}

    def add(
        self,
        *,
        source_type: str,
        source_local_id: str,
        scope: str,
        json_pointer: str,
        value: Any,
        branch_refs: Iterable[str] = (),
        citable: bool = True,
        trust: str = "trusted",
    ) -> str | None:
        if value is None or value == "" or value == [] or value == {}:
            return None
        text = _compact_text(value)
        if len(text) > self.max_chars:
            raise BudgetError(
                f"Support snippet exceeds {self.max_chars} characters at "
                f"{json_pointer}: {len(text)}"
            )
        normalized_branches = sorted(
            {_normalize_branch_ref(ref) for ref in branch_refs}
        )
        role = support_role_for(source_type, json_pointer)
        identity = {
            "source_type": source_type,
            "source_local_id": source_local_id,
            "scope": scope,
            "json_pointer": json_pointer,
            "role": role,
            "citable": citable,
            "trust": trust,
            "branch_refs": normalized_branches,
            "text_sha256": sha256_bytes(text.encode("utf-8")),
        }
        support_id = _stable_id("sup", identity)
        self._items[support_id] = {
            "support_id": support_id,
            "source_type": source_type,
            "source_local_id": source_local_id,
            "scope": scope,
            "json_pointer": json_pointer,
            "role": role,
            "citable": citable,
            "trust": trust,
            "branch_refs": normalized_branches,
            "text": text,
        }
        return support_id

    def values(self) -> list[dict[str, Any]]:
        return [self._items[key] for key in sorted(self._items)]


def _candidate(
    *,
    ayah_ref: str,
    lane: str,
    source_type: str,
    source_local_id: str,
    source_pointer: str,
    kind: str,
    title: str,
    mandatory: bool,
    obligation: str,
    scope: str,
    branch_refs: Iterable[str],
    anchor_refs: Iterable[str],
    support_ids: Iterable[str | None],
    root_ids: Iterable[str] = (),
    unresolved_branch_citations: Iterable[dict[str, str]] = (),
    trust: str = "trusted",
) -> dict[str, Any]:
    normalized_branches = sorted({_normalize_branch_ref(ref) for ref in branch_refs})
    normalized_supports = sorted({item for item in support_ids if item})
    normalized_roots = sorted(set(root_ids))
    unresolved = sorted(
        unresolved_branch_citations,
        key=lambda item: (item.get("citation", ""), item.get("reason", "")),
    )
    normalized_anchors = sorted(set(anchor_refs))
    identity = {
        "ayah_ref": ayah_ref,
        "lane": lane,
        "source_type": source_type,
        "source_local_id": source_local_id,
        "source_pointer": source_pointer,
        "kind": kind,
        "title": title,
        "mandatory": mandatory,
        "obligation": obligation,
        "scope": scope,
        "trust": trust,
        "branch_refs": normalized_branches,
        "root_ids": normalized_roots,
        "unresolved_branch_citations": unresolved,
        "anchor_refs": normalized_anchors,
        "support_ids": normalized_supports,
    }
    return {
        "candidate_id": _stable_id("cand", identity),
        "lane": lane,
        "kind": kind,
        "source_type": source_type,
        "source_local_id": source_local_id,
        "source_pointer": source_pointer,
        "title": title,
        "mandatory": mandatory,
        "obligation": obligation,
        "scope": scope,
        "trust": trust,
        "branch_refs": normalized_branches,
        "root_ids": normalized_roots,
        "unresolved_branch_citations": unresolved,
        "anchor_refs": normalized_anchors,
        "support_ids": normalized_supports,
    }


def _ledger_entry(
    *,
    source_type: str,
    source_local_id: str,
    source_pointer: str,
    disposition: str,
    candidate_id: str | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    return {
        "source_type": source_type,
        "source_local_id": source_local_id,
        "source_pointer": source_pointer,
        "disposition": disposition,
        "candidate_id": candidate_id,
        "reason": reason,
    }


def _parse_ayah_ref(value: Any, label: str) -> tuple[int, int, str]:
    if not isinstance(value, str):
        raise ValidationError(f"{label} must be an ayah ref string")
    match = REF_RE.fullmatch(value)
    if not match:
        raise ValidationError(f"Invalid {label}: {value!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    if surah <= 0 or ayah <= 0:
        raise ValidationError(f"Invalid {label}: {value!r}")
    return surah, ayah, f"{surah}:{ayah}"


def _parse_canonical_ayah_ref(value: Any, label: str) -> tuple[int, int, str]:
    surah, ayah, normalized = _parse_ayah_ref(value, label)
    if value != normalized:
        raise ValidationError(f"{label} must be canonical unpadded form: {value!r}")
    return surah, ayah, normalized


def _validated_qac_inventory(
    bundle: dict[str, Any], *, ayah_ref: str
) -> list[dict[str, Any]]:
    """Reject malformed model-visible QAC rows before any docket construction."""
    qac = _require_list(bundle.get("qac_morphemes"), "qac_morphemes")
    if not qac:
        raise ValidationError("qac_morphemes must not be empty")
    text_fields = {
        "surface_ar",
        "lemma_ar",
        "root_ar",
        "pos",
        "morpheme_role",
        "morph_features",
    }
    seen_refs: set[str] = set()
    for index, raw_row in enumerate(qac):
        label = f"qac_morphemes[{index}]"
        row = _require_dict(raw_row, label)
        qac_ref = row.get("qac_ref")
        word_ref = row.get("qac_word_ref")
        qac_match = QAC_REF_RE.fullmatch(qac_ref) if isinstance(qac_ref, str) else None
        word_match = (
            WORD_REF_RE.fullmatch(word_ref) if isinstance(word_ref, str) else None
        )
        if (
            qac_match is None
            or word_match is None
            or ":".join(qac_match.groups()[:3]) != word_ref
            or ":".join(qac_match.groups()[:2]) != ayah_ref
            or qac_ref in seen_refs
        ):
            raise ValidationError(f"{label} has invalid or duplicate canonical refs")
        if any(not isinstance(row.get(field), str) for field in text_fields):
            raise ValidationError(
                f"{label} model-visible linguistic fields must all be strings"
            )
        seen_refs.add(qac_ref)
    return qac


def _validated_word_ref(
    value: Any,
    *,
    ayah_ref: str,
    word_count: int,
    label: str,
) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"{label} must be a word ref string")
    match = WORD_REF_RE.fullmatch(value)
    if not match or f"{int(match.group(1))}:{int(match.group(2))}" != ayah_ref:
        raise ValidationError(f"{label} must belong to focus ayah {ayah_ref}")
    if int(match.group(3)) > word_count:
        raise ValidationError(
            f"{label} word index exceeds the {word_count} word-analysis rows"
        )
    return value


def _qac_word_root_ids(
    qac_morphemes: list[Any],
    root_mappings: dict[str, list[str]],
) -> dict[str, set[str]]:
    """Bind each QAC word ref to root IDs carried by that exact word."""
    mapped_by_root = {
        _canonical_arabic_root(root_ar): set(root_ids)
        for root_ar, root_ids in root_mappings.items()
    }
    result: dict[str, set[str]] = {}
    for row in qac_morphemes:
        if not isinstance(row, dict):
            continue
        word_ref = row.get("qac_word_ref")
        root_ar = row.get("root_ar")
        if not isinstance(word_ref, str) or not isinstance(root_ar, str) or not root_ar:
            continue
        result.setdefault(word_ref, set()).update(
            mapped_by_root.get(_canonical_arabic_root(root_ar), set())
        )
    return result


def _validated_publication_anchors(
    anchors: Any,
    *,
    ayah_ref: str,
    qac_morphemes: list[Any],
    root_mappings: dict[str, list[str]],
    known_branch_refs: set[str],
    label: str,
) -> tuple[list[str], list[str]]:
    """Validate structured publication anchors against exact QAC occurrences."""
    if not isinstance(anchors, list) or not anchors:
        raise ValidationError(f"{label} must be a nonempty array")
    roots_by_word = _qac_word_root_ids(qac_morphemes, root_mappings)
    anchor_refs: list[str] = []
    branch_refs: list[str] = []
    for index, anchor in enumerate(anchors):
        anchor_label = f"{label}[{index}]"
        if not isinstance(anchor, list) or len(anchor) != 3:
            raise ValidationError(
                f"{anchor_label} must be an exact [word_ref, root_id, branch_ids] tuple"
            )
        word_ref, root_id, branch_ids = anchor
        word_match = WORD_REF_RE.fullmatch(word_ref) if isinstance(word_ref, str) else None
        if not word_match or ":".join(word_match.groups()[:2]) != ayah_ref:
            raise ValidationError(
                f"{anchor_label} word_ref must identify a word in focus ayah {ayah_ref}"
            )
        if word_ref not in roots_by_word:
            raise ValidationError(f"{anchor_label} word_ref is absent from the QAC inventory")
        if not isinstance(root_id, str) or not ROOT_ID_RE.fullmatch(root_id):
            raise ValidationError(f"{anchor_label} root_id is invalid")
        if root_id not in roots_by_word[word_ref]:
            raise ValidationError(
                f"{anchor_label} root_id is not carried by QAC word {word_ref}"
            )
        if (
            not isinstance(branch_ids, list)
            or not branch_ids
            or any(
                not isinstance(branch_id, str)
                or not BRANCH_ID_RE.fullmatch(branch_id)
                for branch_id in branch_ids
            )
            or len(branch_ids) != len(set(branch_ids))
        ):
            raise ValidationError(
                f"{anchor_label} branch_ids must be a nonempty unique array of "
                "canonical branch IDs"
            )
        resolved_refs = [f"{root_id}/{branch_id}" for branch_id in branch_ids]
        unknown = set(resolved_refs) - known_branch_refs
        if unknown:
            raise ValidationError(
                f"{anchor_label} cites branches outside the QAC word's registered root: "
                f"{sorted(unknown)}"
            )
        anchor_refs.append(word_ref)
        branch_refs.extend(resolved_refs)
    return sorted(set(anchor_refs)), sorted(set(branch_refs))


def _scope_contract(
    bundle: dict[str, Any], *, max_pericope_ayahs: int
) -> dict[str, Any]:
    surah, ayah, ayah_ref = _parse_ayah_ref(bundle.get("ayahRef"), "bundle ayahRef")
    if bundle.get("ayahRef") != ayah_ref:
        raise ValidationError("bundle ayahRef must use canonical unpadded notation")
    bundle_surah = bundle.get("surah")
    if bundle_surah is not None and (
        not isinstance(bundle_surah, int)
        or isinstance(bundle_surah, bool)
        or bundle_surah != surah
    ):
        raise ValidationError("bundle surah disagrees with ayahRef")
    bundle_ayah = bundle.get("ayah")
    if bundle_ayah is not None and (
        not isinstance(bundle_ayah, int)
        or isinstance(bundle_ayah, bool)
        or bundle_ayah != ayah
    ):
        raise ValidationError("bundle ayah disagrees with ayahRef")

    pericope = _require_dict(bundle.get("pericope"), "bundle pericope")
    p_number = pericope.get("pericope")
    p_surah = pericope.get("surah")
    p_from = pericope.get("ayah_from")
    p_to = pericope.get("ayah_to")
    if (
        not isinstance(p_number, int)
        or isinstance(p_number, bool)
        or p_number <= 0
    ):
        raise ValidationError("pericope number must be a positive integer")
    if not all(
        isinstance(item, int) and not isinstance(item, bool)
        for item in (p_surah, p_from, p_to)
    ):
        raise ValidationError("pericope surah/ayah_from/ayah_to must be integers")
    if p_surah != surah or not p_from <= ayah <= p_to:
        raise ScopeError(
            f"Focus {ayah_ref} is outside declared pericope {p_surah}:{p_from}-{p_to}"
        )
    pericope_width = p_to - p_from + 1
    if pericope_width > max_pericope_ayahs:
        raise ScopeError(
            f"Declared pericope has {pericope_width} ayahs; limit is "
            f"{max_pericope_ayahs}"
        )
    refs = [f"{surah}:{number}" for number in range(p_from, p_to + 1)]
    return {
        "ayah_ref": ayah_ref,
        "surah": surah,
        "ayah": ayah,
        "pericope": {
            "id": f"s{surah:03d}-p{p_number:02d}-{p_from:03d}-{p_to:03d}",
            "number": p_number,
            "label": pericope.get("label"),
            "ayah_from": p_from,
            "ayah_to": p_to,
            "refs": refs,
        },
    }


def _audit_hft(
    bundle: dict[str, Any],
    scope: dict[str, Any],
    *,
    allow_legacy_response: bool,
) -> dict[str, Any]:
    if "v12_focus_trace_hermetic" not in bundle:
        return {
            "status": "absent",
            "adjudicable": False,
            "reasons": [],
            "packet": None,
            "readers": [],
        }
    hft = bundle["v12_focus_trace_hermetic"]
    hft = _require_dict(hft, "v12_focus_trace_hermetic")
    summary = _require_dict(hft.get("packet_summary"), "HFT packet_summary")
    readers = _require_dict(hft.get("readers"), "HFT readers")
    integrity_reasons: list[str] = []

    focus_ref = summary.get("focus_ref")
    protocol = summary.get("protocol")
    window_scope = summary.get("window_scope")
    window = summary.get("window")
    ayah_count = summary.get("ayah_count")
    if focus_ref != scope["ayah_ref"]:
        integrity_reasons.append(
            f"packet focus_ref {focus_ref!r} != bundle focus {scope['ayah_ref']!r}"
        )
    if window_scope is not None and not isinstance(window_scope, str):
        integrity_reasons.append("packet window_scope must be null or text")
    if protocol == PERICOPE_HFT_PROTOCOL and (
        window_scope is None or window_scope == "pericope"
    ):
        evidence_scope = "pericope"
        evidence_lane = "macro"
    elif protocol == SURAH_HFT_PROTOCOL and window_scope == "surah":
        evidence_scope = "surah"
        evidence_lane = "global"
    else:
        evidence_scope = "invalid"
        evidence_lane = None
        integrity_reasons.append(
            f"unsupported HFT protocol/scope pair: {protocol!r}/{window_scope!r}"
        )
    if not isinstance(window, list) or not all(isinstance(ref, str) for ref in window):
        integrity_reasons.append("packet window must be an array of ayah refs")
        window = []
    elif evidence_scope == "pericope":
        if window != scope["pericope"]["refs"]:
            integrity_reasons.append(
                "packet window does not exactly match declared pericope "
                f"({len(window)} refs vs {len(scope['pericope']['refs'])})"
            )
    elif evidence_scope == "surah":
        for number, ref in enumerate(window, start=1):
            try:
                ref_surah, ref_ayah, _normalized = _parse_canonical_ayah_ref(
                    ref, "surah HFT window ref"
                )
            except ValidationError as exc:
                integrity_reasons.append(str(exc))
                break
            if ref_surah != scope["surah"] or ref_ayah != number:
                integrity_reasons.append(
                    "surah HFT window must be contiguous from the first ayah"
                )
                break
        if scope["ayah_ref"] not in window:
            integrity_reasons.append("surah HFT window omits focus ayah")
    if ayah_count != len(window):
        integrity_reasons.append(
            f"packet ayah_count {ayah_count!r} != window length {len(window)}"
        )
    window_sha256 = canonical_sha256(window)
    expected_packet_identity = {
        "focus_ref": focus_ref,
        "protocol": protocol,
        "window_sha256": window_sha256,
    }

    reader_reports: list[dict[str, Any]] = []
    unbound_readers: list[str] = []
    if not readers:
        integrity_reasons.append("HFT packet has no reader responses")
    if any(not isinstance(reader_id, str) for reader_id in readers):
        raise ValidationError("HFT reader IDs must be strings")
    for reader_id in sorted(readers):
        response = readers[reader_id]
        if not isinstance(response, dict):
            integrity_reasons.append(
                f"reader {reader_id!r} response must be an object"
            )
            reader_reports.append(
                {"reader_id": reader_id, "identity_status": "invalid"}
            )
            continue
        response_reasons: list[str] = []
        if not reader_id:
            response_reasons.append("reader ID must be nonempty")
        if response.get("focus_ref") != scope["ayah_ref"]:
            response_reasons.append("focus_ref mismatch")
        if response.get("protocol") != HFT_RESPONSE_PROTOCOL:
            response_reasons.append("unexpected response protocol")
        for field in (
            "baseline_models",
            "context_deltas",
            "surprising_valid_outliers",
        ):
            if not isinstance(response.get(field), list):
                response_reasons.append(f"{field} must be an array")
        packet_identity = response.get("packet_identity")
        if packet_identity is None:
            identity_status = "legacy_unbound"
            unbound_readers.append(reader_id)
        elif not isinstance(packet_identity, dict):
            identity_status = "invalid"
            response_reasons.append("packet_identity must be an object")
        else:
            if set(packet_identity) != set(expected_packet_identity):
                response_reasons.append(
                    "packet_identity fields must exactly match the packet identity contract"
                )
            echoed_identity = {
                "focus_ref": packet_identity.get("focus_ref"),
                "protocol": packet_identity.get("protocol"),
                "window_sha256": packet_identity.get("window_sha256"),
            }
            if echoed_identity != expected_packet_identity:
                identity_status = "invalid"
                response_reasons.append("packet_identity echo mismatch")
            else:
                identity_status = "bound"
        if response_reasons:
            integrity_reasons.extend(
                f"reader {reader_id}: {reason}" for reason in response_reasons
            )
        reader_reports.append(
            {
                "reader_id": reader_id,
                "focus_ref": response.get("focus_ref"),
                "protocol": response.get("protocol"),
                "identity_status": (
                    "invalid" if response_reasons else identity_status
                ),
                "packet_identity": packet_identity,
                "reasons": response_reasons,
                "note": (
                    "Response matches focus/protocol but carries no packet hash echo."
                    if not response_reasons and identity_status == "legacy_unbound"
                    else None
                ),
            }
        )

    binding_reasons = [
        f"reader {reader_id}: response is not bound to packet identity"
        for reader_id in unbound_readers
    ]
    if integrity_reasons:
        status = "invalid"
        adjudicable = False
    elif unbound_readers and allow_legacy_response:
        status = f"valid_{evidence_scope}_legacy"
        adjudicable = True
    elif unbound_readers:
        status = f"valid_{evidence_scope}_packet_unbound_response"
        adjudicable = False
    else:
        status = f"valid_{evidence_scope}_bound"
        adjudicable = True
    return {
        "status": status,
        "adjudicable": adjudicable,
        "reasons": integrity_reasons + (
            [] if allow_legacy_response else binding_reasons
        ),
        "legacy_response_allowed": allow_legacy_response,
        "evidence_scope": evidence_scope,
        "evidence_lane": evidence_lane,
        "packet": {
            "source_file": summary.get("source_file"),
            "protocol": protocol,
            "window_scope": window_scope,
            "focus_ref": focus_ref,
            "window": window,
            "ayah_count": ayah_count,
            "window_sha256": window_sha256,
        },
        "readers": reader_reports,
    }


def _branch_registry(
    bundle: dict[str, Any],
    *,
    max_bytes_per_root: int,
) -> tuple[
    list[dict[str, Any]],
    set[str],
    dict[str, list[str]],
    list[dict[str, Any]],
]:
    qac = _require_list(bundle.get("qac_morphemes"), "qac_morphemes")
    focus_roots = {
        row.get("root_ar")
        for row in qac
        if isinstance(row, dict) and isinstance(row.get("root_ar"), str)
        and row.get("root_ar")
    }
    focus_roots_by_canonical: dict[str, set[str]] = {}
    for root in focus_roots:
        focus_roots_by_canonical.setdefault(_canonical_arabic_root(root), set()).add(
            root
        )
    lexicon = _require_dict(bundle.get("root_lexicon"), "root_lexicon")
    roots: list[dict[str, Any]] = []
    known_refs: set[str] = set()
    mappings: dict[str, list[str]] = {root: [] for root in sorted(focus_roots)}
    dictionary_gaps: list[dict[str, Any]] = []

    for root_id in sorted(lexicon):
        root = _require_dict(lexicon[root_id], f"root_lexicon.{root_id}")
        root_ar = root.get("root_ar")
        qac_roots = root.get("qac_roots_ar")
        mapped_roots = {
            item for item in ([root_ar] + (qac_roots if isinstance(qac_roots, list) else []))
            if isinstance(item, str) and item
        }
        matching_focus_roots = {
            focus_root
            for mapped_root in mapped_roots
            for focus_root in focus_roots_by_canonical.get(
                _canonical_arabic_root(mapped_root), set()
            )
        }
        if not matching_focus_roots:
            continue
        for mapped in sorted(matching_focus_roots):
            mappings[mapped].append(root_id)

        if "dictionary_entry" not in root:
            raise ValidationError(
                f"root_lexicon.{root_id} lacks dictionary_entry"
            )
        dictionary = root["dictionary_entry"]
        if dictionary is None:
            branches: list[Any] = []
            dictionary_gaps.append(
                {
                    "root_id": root_id,
                    "root_ar": root_ar,
                    "qac_roots_ar": sorted(matching_focus_roots),
                    "reason": "dictionary_entry is explicitly null in the source bundle",
                }
            )
        else:
            dictionary = _require_dict(
                dictionary, f"root_lexicon.{root_id}.dictionary_entry"
            )
            branches = _require_list(
                dictionary.get("branches"),
                f"root_lexicon.{root_id}.dictionary_entry.branches",
            )
            if not branches:
                raise ValidationError(
                    f"root_lexicon.{root_id}.dictionary_entry.branches must not be empty"
                )
        compact_branches: list[dict[str, Any]] = []
        for index, raw_branch in enumerate(branches):
            branch = _require_dict(raw_branch, f"{root_id} branch {index}")
            raw_ref = branch.get("branch_ref")
            if not isinstance(raw_ref, str):
                raise ValidationError(f"{root_id} branch {index} lacks branch_ref")
            branch_ref = _normalize_branch_ref(raw_ref)
            if not branch_ref.startswith(f"{root_id}/"):
                raise ValidationError(
                    f"Branch {branch_ref} is stored under mismatched root {root_id}"
                )
            if branch_ref in known_refs:
                raise ValidationError(f"Duplicate branch ref: {branch_ref}")
            known_refs.add(branch_ref)
            concept_gloss = branch.get("concept_gloss")
            gloss = (
                concept_gloss.get("text")
                if isinstance(concept_gloss, dict)
                else concept_gloss
            )
            concept_map = branch.get("concept_map")
            if concept_map is None:
                concept_map = {}
            else:
                concept_map = _require_dict(
                    concept_map, f"{root_id} branch {index}.concept_map"
                )
            if not gloss:
                gloss = (
                    branch.get("semantic_fallback")
                    or branch.get("branch_image_ar")
                    or branch.get("what_is_ar")
                    or concept_map.get("definition")
                )
            identity = branch.get("identity_judgment")
            if identity is None:
                identity = {}
            else:
                identity = _require_dict(
                    identity, f"{root_id} branch {index}.identity_judgment"
                )
            lexicalization = branch.get("lexicalization_scope")
            if lexicalization is None:
                lexicalization = {}
            else:
                lexicalization = _require_dict(
                    lexicalization,
                    f"{root_id} branch {index}.lexicalization_scope",
                )
            compact_branches.append(
                {
                    "branch_ref": branch_ref,
                    "status": identity.get("status"),
                    "branch_kind": lexicalization.get("branch_kind"),
                    "gloss": _compact_text(gloss) if gloss else None,
                    "boundary": (
                        _compact_text(identity.get("boundary_note"))
                        if identity.get("boundary_note")
                        else None
                    ),
                    "source_pointer": (
                        f"/root_lexicon/{json_pointer_escape(root_id)}"
                        f"/dictionary_entry/branches/{index}"
                    ),
                }
            )
        root_record = {
            "root_id": root_id,
            "root_ar": root_ar,
            "qac_roots_ar": sorted(mapped_roots),
            "mapping_role": root.get("root_mapping_role"),
            "branches": compact_branches,
        }
        size = len(canonical_json_bytes(root_record))
        if size > max_bytes_per_root:
            raise BudgetError(
                f"Compact branch registry for {root_id} is {size} bytes; "
                f"limit is {max_bytes_per_root}"
            )
        roots.append(root_record)

    missing = [root for root, root_ids in mappings.items() if not root_ids]
    if missing:
        raise ValidationError(
            "No root_lexicon mapping for focus roots: " + ", ".join(missing)
        )
    return roots, known_refs, mappings, dictionary_gaps


def _nominatable_branch_inventory(
    bundle: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    """Index compact pericope branch evidence that nominations may cite."""
    container = _optional_dict(bundle, "branch_inventories", "branch_inventories")
    packet = _optional_dict(
        container,
        "full_context_packet",
        "branch_inventories.full_context_packet",
    )
    raw_records = packet.get("branch_inventories")
    records = (
        []
        if raw_records is None
        else _require_list(raw_records, "full_context_packet.branch_inventories")
    )
    source_file = packet.get("source_file")
    registry: dict[str, dict[str, Any]] = {}
    roots_by_arabic: dict[str, set[str]] = {}
    for root_index, raw_root in enumerate(records):
        root = _require_dict(raw_root, f"branch inventory root {root_index}")
        root_ar = root.get("root")
        if not isinstance(root_ar, str) or not root_ar:
            raise ValidationError(
                f"branch inventory root {root_index} lacks Arabic root"
            )
        branches = _require_list(
            root.get("branches"), f"branch inventory root {root_index}.branches"
        )
        for branch_index, raw_branch in enumerate(branches):
            branch = _require_dict(
                raw_branch,
                f"branch inventory root {root_index} branch {branch_index}",
            )
            branch_id = branch.get("branch_id")
            variants = _require_list(
                branch.get("variants"),
                f"branch inventory root {root_index} branch {branch_index}.variants",
            )
            if not isinstance(branch_id, str):
                raise ValidationError("branch inventory item lacks branch_id")
            for variant_index, raw_variant in enumerate(variants):
                variant = _require_dict(
                    raw_variant,
                    "branch inventory variant",
                )
                root_id = variant.get("root_id")
                if not isinstance(root_id, str):
                    raise ValidationError("branch inventory variant lacks root_id")
                branch_ref = _normalize_branch_ref(f"{root_id}/{branch_id}")
                roots_by_arabic.setdefault(root_ar, set()).add(root_id)
                compact = {
                    "branch_ref": branch_ref,
                    "root_ar": root_ar,
                    "image_ar": variant.get("image_ar") or branch.get("image_ar"),
                    "image_en": variant.get("image_en") or branch.get("image_en"),
                    "scope_ar": variant.get("scope_ar") or branch.get("scope_ar"),
                    "scope_en": variant.get("scope_en") or branch.get("scope_en"),
                    "source_file": variant.get("source_path") or source_file,
                    "source_pointer": (
                        "/branch_inventories/full_context_packet/branch_inventories/"
                        f"{root_index}/branches/{branch_index}/variants/{variant_index}"
                    ),
                }
                if not any(
                    isinstance(compact[field], str) and compact[field].strip()
                    for field in ("image_ar", "image_en")
                ):
                    raise ValidationError(
                        f"Nominated branch {branch_ref} lacks a nonempty image descriptor"
                    )
                previous = registry.get(branch_ref)
                if previous is not None and canonical_sha256(previous) != canonical_sha256(
                    compact
                ):
                    raise ValidationError(
                        f"Conflicting nominated branch inventory: {branch_ref}"
                    )
                registry[branch_ref] = compact
    return registry, {
        root: sorted(root_ids) for root, root_ids in sorted(roots_by_arabic.items())
    }


def _word_analysis_qac_refs(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    words: list[Any],
    qac: list[dict[str, Any]],
) -> list[list[str]]:
    """Build the lossless word-analysis-to-QAC join used for root contact."""
    qac_by_ref = {row["qac_ref"]: row for row in qac}
    qac_position = {row["qac_ref"]: index for index, row in enumerate(qac)}
    if "word_morpheme_spans" not in bundle:
        # Upstream aligned word numbers are preserved observations, not a trusted
        # join. Missing explicit spans therefore cannot ground branch contact.
        return [[] for _word in words]
    spans = bundle["word_morpheme_spans"]
    if not isinstance(spans, list) or len(spans) != len(words):
        raise ValidationError(
            "word_morpheme_spans must align one-for-one with word_analysis.words"
        )
    expected_fields = {
        "word_index",
        "surface_ar",
        "word_ids",
        "qac_refs",
        "morpheme_ids",
        "aligned_qac_word_ref_upstream",
        "morpheme_skip_count",
    }
    seen_qac_refs: set[str] = set()
    result: list[list[str]] = []
    for index, raw_span in enumerate(spans):
        if raw_span is None:
            result.append([])
            continue
        span = _require_dict(raw_span, f"word_morpheme_spans[{index}]")
        _require_exact_keys(
            span, expected_fields, f"word_morpheme_spans[{index}]"
        )
        if type(span.get("word_index")) is not int or span["word_index"] != index:
            raise ValidationError(
                f"word_morpheme_spans[{index}].word_index is not the exact row index"
            )
        if not isinstance(span.get("surface_ar"), str) or not span["surface_ar"]:
            raise ValidationError(
                f"word_morpheme_spans[{index}].surface_ar is invalid"
            )
        word_ids = _require_list(
            span.get("word_ids"), f"word_morpheme_spans[{index}].word_ids"
        )
        qac_refs = _require_list(
            span.get("qac_refs"), f"word_morpheme_spans[{index}].qac_refs"
        )
        morpheme_ids = _require_list(
            span.get("morpheme_ids"),
            f"word_morpheme_spans[{index}].morpheme_ids",
        )
        if (
            not word_ids
            or any(not isinstance(item, str) or not item for item in word_ids)
            or len(word_ids) != len(set(word_ids))
            or not qac_refs
            or any(
                not isinstance(ref, str)
                or ref not in qac_by_ref
                or not ref.startswith(f"{ayah_ref}:")
                for ref in qac_refs
            )
            or len(qac_refs) != len(set(qac_refs))
            or len({qac_by_ref[ref]["qac_word_ref"] for ref in qac_refs}) != 1
            or [qac_position[ref] for ref in qac_refs]
            != sorted(qac_position[ref] for ref in qac_refs)
            or seen_qac_refs.intersection(qac_refs)
            or len(morpheme_ids) != len(qac_refs)
            or any(
                not isinstance(item, str) or not item for item in morpheme_ids
            )
            or len(morpheme_ids) != len(set(morpheme_ids))
        ):
            raise ValidationError(
                f"word_morpheme_spans[{index}] has invalid or reused QAC lineage"
            )
        word = words[index]
        upstream_ref = span.get("aligned_qac_word_ref_upstream")
        if (
            not isinstance(word, dict)
            or not isinstance(upstream_ref, str)
            or upstream_ref != word.get("aligned_qac_word_ref")
        ):
            raise ValidationError(
                f"word_morpheme_spans[{index}] disagrees with its upstream word ref"
            )
        skip_count = span.get("morpheme_skip_count")
        if type(skip_count) is not int or skip_count < 0:
            raise ValidationError(
                f"word_morpheme_spans[{index}].morpheme_skip_count is invalid"
            )
        seen_qac_refs.update(qac_refs)
        result.append(list(qac_refs))
    return result


def _focus_packet(bundle: dict[str, Any], *, ayah_ref: str) -> dict[str, Any]:
    qac = _validated_qac_inventory(bundle, ayah_ref=ayah_ref)
    morphemes: list[dict[str, Any]] = []
    for row in qac:
        if not isinstance(row, dict):
            raise ValidationError("Every qac_morphemes item must be an object")
        morphemes.append(
            {
                "qac_ref": row.get("qac_ref"),
                "qac_word_ref": row.get("qac_word_ref"),
                "surface_ar": row.get("surface_ar"),
                "lemma_ar": row.get("lemma_ar"),
                "root_ar": row.get("root_ar"),
                "pos": row.get("pos"),
                "morpheme_role": row.get("morpheme_role"),
                "morph_features": row.get("morph_features"),
            }
        )
    text = bundle.get("text")
    if isinstance(text, dict):
        arabic = text.get("arabic_uthmani")
    else:
        arabic = text
    analysis = bundle.get("word_analysis")
    words = analysis.get("words") if isinstance(analysis, dict) else None
    word_analysis_refs: list[str | None] = []
    word_analysis_qac_refs: list[list[str]] = []
    if isinstance(words, list):
        for index, word in enumerate(words):
            try:
                word_analysis_refs.append(
                    _validated_word_ref(
                        word.get("aligned_qac_word_ref")
                        if isinstance(word, dict)
                        else None,
                        ayah_ref=ayah_ref,
                        word_count=len(words),
                        label=f"word_analysis.words[{index}].aligned_qac_word_ref",
                    )
                )
            except ValidationError:
                word_analysis_refs.append(None)
        word_analysis_qac_refs = _word_analysis_qac_refs(
            bundle,
            ayah_ref=ayah_ref,
            words=words,
            qac=qac,
        )
    return {
        "arabic_uthmani": arabic,
        "qac_morphemes": morphemes,
        "word_analysis_refs": word_analysis_refs,
        "word_analysis_qac_refs": word_analysis_qac_refs,
    }


def _qac_root_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    root_mappings: dict[str, list[str]],
    supports: SupportBuilder,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Create one source-bound occurrence carrier for every QAC focus root."""
    qac = _validated_qac_inventory(bundle, ayah_ref=ayah_ref)
    occurrences: dict[str, tuple[int, dict[str, Any]]] = {}
    for index, raw_row in enumerate(qac):
        if not isinstance(raw_row, dict):
            raise ValidationError("Every qac_morphemes item must be an object")
        root_ar = raw_row["root_ar"]
        if root_ar:
            occurrences.setdefault(_canonical_arabic_root(root_ar), (index, raw_row))

    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    for root_ar, root_ids in sorted(root_mappings.items()):
        occurrence = occurrences.get(_canonical_arabic_root(root_ar))
        if occurrence is None:
            raise ValidationError(f"Mapped focus root {root_ar} lacks a QAC occurrence")
        index, row = occurrence
        qac_ref = row.get("qac_ref")
        qac_word_ref = row.get("qac_word_ref")
        if not isinstance(qac_ref, str) or not isinstance(qac_word_ref, str):
            raise ValidationError(f"QAC occurrence for {root_ar} lacks canonical refs")
        pointer = f"/qac_morphemes/{index}"
        support_id = supports.add(
            source_type="qac_morpheme",
            source_local_id=qac_ref,
            scope="micro",
            json_pointer=pointer,
            value={
                "qac_ref": qac_ref,
                "qac_word_ref": qac_word_ref,
                "surface_ar": row.get("surface_ar"),
                "lemma_ar": row.get("lemma_ar"),
                "root_ar": root_ar,
                "pos": row.get("pos"),
                "morpheme_role": row.get("morpheme_role"),
                "morph_features": row.get("morph_features"),
            },
        )
        candidate = _candidate(
            ayah_ref=ayah_ref,
            lane="micro",
            source_type="qac_morpheme",
            source_local_id=qac_ref,
            source_pointer=pointer,
            kind="focus_root_occurrence",
            title=f"QAC root occurrence: {root_ar}",
            mandatory=False,
            obligation="ledger_only",
            scope="focus_ayah",
            branch_refs=[],
            anchor_refs=[qac_word_ref],
            support_ids=[support_id],
            root_ids=root_ids,
        )
        candidates.append(candidate)
        ledger.append(
            _ledger_entry(
                source_type="qac_morpheme",
                source_local_id=qac_ref,
                source_pointer=pointer,
                disposition="docket_optional",
                candidate_id=candidate["candidate_id"],
            )
        )
    return candidates, ledger


def _word_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    resolver: BranchResolver,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    analysis = _require_dict(bundle.get("word_analysis"), "word_analysis")
    words = _require_list(analysis.get("words"), "word_analysis.words")
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    word_count = len(words)
    for word_index, raw_word in enumerate(words):
        if not isinstance(raw_word, dict):
            local_id = f"word-{word_index}:invalid"
            ledger.append(
                _ledger_entry(
                    source_type="word_analysis",
                    source_local_id=local_id,
                    source_pointer=f"/word_analysis/words/{word_index}",
                    disposition="parse_failed",
                    reason="word record is not an object",
                )
            )
            continue
        try:
            word_ref = _validated_word_ref(
                raw_word.get("aligned_qac_word_ref"),
                ayah_ref=ayah_ref,
                word_count=word_count,
                label=f"word_analysis.words[{word_index}].aligned_qac_word_ref",
            )
        except ValidationError as exc:
            ledger.append(
                _ledger_entry(
                    source_type="word_analysis",
                    source_local_id=f"word-{word_index}:invalid-ref",
                    source_pointer=f"/word_analysis/words/{word_index}",
                    disposition="parse_failed",
                    reason=str(exc),
                )
            )
            continue
        word_pointer = f"/word_analysis/words/{word_index}"
        topics = raw_word.get("topics")
        if not isinstance(topics, list):
            ledger.append(
                _ledger_entry(
                    source_type="word_analysis",
                    source_local_id=f"{word_ref}:topics",
                    source_pointer=f"{word_pointer}/topics",
                    disposition="parse_failed",
                    reason="topics is not an array",
                )
            )
            continue
        for topic_index, raw_topic in enumerate(topics):
            fallback_id = f"{word_ref}:topic-{topic_index}"
            if not isinstance(raw_topic, dict) or not isinstance(
                raw_topic.get("topic_id"), str
            ):
                ledger.append(
                    _ledger_entry(
                        source_type="word_analysis",
                        source_local_id=fallback_id,
                        source_pointer=f"{word_pointer}/topics/{topic_index}",
                        disposition="parse_failed",
                        reason="topic is not an object with topic_id",
                    )
                )
                continue
            topic_id = raw_topic["topic_id"]
            obligation = raw_topic.get("commentary_obligation")
            if not isinstance(obligation, str) or obligation not in WORD_TOPIC_OBLIGATIONS:
                ledger.append(
                    _ledger_entry(
                        source_type="word_analysis",
                        source_local_id=topic_id,
                        source_pointer=f"{word_pointer}/topics/{topic_index}",
                        disposition="parse_failed",
                        reason=(
                            "commentary_obligation must be one of: "
                            + ", ".join(sorted(WORD_TOPIC_OBLIGATIONS))
                        ),
                    )
                )
                continue
            mandatory = obligation in ("must_integrate", "candidate")
            word_evidence = {
                "surface_display": raw_word.get("surface_display"),
                "root_display": raw_word.get("root_display"),
                "gloss_range": raw_word.get("gloss_range"),
                "root_gloss_range": raw_word.get("root_gloss_range"),
                "prose": raw_word.get("prose"),
            }
            topic_evidence = {
                "headline": raw_topic.get("headline"),
                "status": raw_topic.get("status"),
                "reader_payoff": raw_topic.get("reader_payoff"),
                "reason": raw_topic.get("reason"),
                "blocking_evidence": raw_topic.get("blocking_evidence"),
                "representative_source_ids": raw_topic.get(
                    "representative_source_ids"
                ),
            }
            word_branch_refs, word_unresolved = resolver.resolve_text(word_evidence)
            topic_branch_refs, topic_unresolved = resolver.resolve_text(raw_topic)
            unresolved = [
                {"citation": citation, "reason": reason}
                for citation, reason in sorted(
                    {
                        (item["citation"], item["reason"])
                        for item in word_unresolved + topic_unresolved
                    }
                )
            ]
            word_support = supports.add(
                source_type="word_analysis",
                source_local_id=str(word_ref),
                scope="micro",
                json_pointer=word_pointer,
                value=word_evidence,
                branch_refs=word_branch_refs,
            )
            topic_support = supports.add(
                source_type="word_analysis",
                source_local_id=topic_id,
                scope="micro",
                json_pointer=f"{word_pointer}/topics/{topic_index}",
                value=topic_evidence,
                branch_refs=topic_branch_refs,
            )
            candidate = _candidate(
                ayah_ref=ayah_ref,
                lane="micro",
                source_type="word_analysis",
                source_local_id=topic_id,
                source_pointer=f"{word_pointer}/topics/{topic_index}",
                kind="word_topic",
                title=raw_topic.get("headline") or topic_id,
                mandatory=mandatory,
                obligation=obligation,
                scope="focus_ayah",
                branch_refs=topic_branch_refs,
                anchor_refs=[str(word_ref)],
                support_ids=[word_support, topic_support],
                root_ids=[],
                unresolved_branch_citations=unresolved,
            )
            candidates.append(candidate)
            ledger.append(
                _ledger_entry(
                    source_type="word_analysis",
                    source_local_id=topic_id,
                    source_pointer=f"{word_pointer}/topics/{topic_index}",
                    disposition=(
                        "docket_mandatory" if mandatory else "docket_optional"
                    ),
                    candidate_id=candidate["candidate_id"],
                )
            )
    return candidates, ledger


def _channel_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    resolver: BranchResolver,
    allowed_refs: set[str],
    focus_branch_refs: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    channels = _require_list(
        bundle.get("channel_subchannels_anchored_here"),
        "channel_subchannels_anchored_here",
    )
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    for index, raw_channel in enumerate(channels):
        if not isinstance(raw_channel, dict):
            ledger.append(
                _ledger_entry(
                    source_type="channel",
                    source_local_id=f"channel-{index}",
                    source_pointer=f"/channel_subchannels_anchored_here/{index}",
                    disposition="parse_failed",
                    reason="channel record is not an object",
                )
            )
            continue
        name = raw_channel.get("name")
        key = raw_channel.get("key")
        local_id = f"{key or index}:{name or 'unnamed'}"
        refs = raw_channel.get("ayah_refs")
        raw_anchors = raw_channel.get("ayah_anchors")
        anchors_text = raw_anchors if isinstance(raw_anchors, str) else ""
        normalized_refs: list[str] = []
        invalid_ref_reason: str | None = None
        if refs is not None and not isinstance(refs, list):
            invalid_ref_reason = "channel ayah_refs is not an array"
        elif isinstance(refs, list):
            for raw_ref in refs:
                try:
                    _surah, _ayah, normalized = _parse_ayah_ref(
                        raw_ref, "channel ayah_refs item"
                    )
                except ValidationError as exc:
                    invalid_ref_reason = str(exc)
                    break
                if normalized not in allowed_refs:
                    invalid_ref_reason = (
                        f"channel ref {normalized} is outside declared pericope"
                    )
                    break
                normalized_refs.append(normalized)
        if raw_anchors is not None and not isinstance(raw_anchors, str):
            invalid_ref_reason = (
                invalid_ref_reason or "channel ayah_anchors is not a string"
            )
        exact_anchor_refs = {
            f"{int(match.group(1))}:{int(match.group(2))}"
            for match in AYAH_REF_SCAN_RE.finditer(anchors_text)
        }
        outside_text_refs = exact_anchor_refs - allowed_refs
        if invalid_ref_reason is None and outside_text_refs:
            invalid_ref_reason = (
                "channel ayah_anchors contains out-of-pericope refs: "
                + ", ".join(sorted(outside_text_refs))
            )
        if invalid_ref_reason:
            ledger.append(
                _ledger_entry(
                    source_type="channel",
                    source_local_id=local_id,
                    source_pointer=f"/channel_subchannels_anchored_here/{index}",
                    disposition="parse_failed",
                    reason=invalid_ref_reason,
                )
            )
            continue
        anchored = (ayah_ref in normalized_refs) or (
            ayah_ref in exact_anchor_refs
        )
        if not anchored:
            ledger.append(
                _ledger_entry(
                    source_type="channel",
                    source_local_id=local_id,
                    source_pointer=f"/channel_subchannels_anchored_here/{index}",
                    disposition="out_of_scope",
                    reason=f"channel does not anchor focus {ayah_ref}",
                )
            )
            continue
        pointer = f"/channel_subchannels_anchored_here/{index}"
        channel_fields = (
            "scene_or_process",
            "synthesis",
            "active_motifs",
            "ayah_anchors",
            "parent_semantic_invariant",
        )
        resolved_by_field: dict[str, list[str]] = {}
        unresolved_by_field: dict[str, list[dict[str, str]]] = {}
        support_ids: list[str | None] = []
        nominated_refs, nominated_unresolved = resolver.resolve_text(
            raw_channel.get("active_motifs")
        )
        retained_support_refs = focus_branch_refs | set(nominated_refs)
        for field in channel_fields:
            if field == "active_motifs":
                field_refs, field_unresolved = nominated_refs, nominated_unresolved
            else:
                resolved_refs, field_unresolved = resolver.resolve_text(
                    raw_channel.get(field)
                )
                field_refs = sorted(set(resolved_refs) & retained_support_refs)
            resolved_by_field[field] = field_refs
            unresolved_by_field[field] = field_unresolved
            support_ids.append(supports.add(
                source_type="channel",
                source_local_id=local_id,
                scope="macro",
                json_pointer=f"{pointer}/{field}",
                value=raw_channel.get(field),
                branch_refs=field_refs,
            ))
        # Only active_motifs is a nomination field. Explanatory prose is retained,
        # but its branch metadata cannot exceed focus plus exact nominations.
        branch_refs = resolved_by_field["active_motifs"]
        unresolved = [
            {"citation": citation, "reason": reason}
            for citation, reason in sorted(
                {
                    (item["citation"], item["reason"])
                    for field_unresolved in unresolved_by_field.values()
                    for item in field_unresolved
                }
            )
        ]
        candidate = _candidate(
            ayah_ref=ayah_ref,
            lane="macro",
            source_type="channel",
            source_local_id=local_id,
            source_pointer=pointer,
            kind="resonance_nomination",
            title=name or local_id,
            mandatory=True,
            obligation="review",
            scope="pericope",
            branch_refs=branch_refs,
            anchor_refs=normalized_refs or sorted(exact_anchor_refs),
            support_ids=support_ids,
            unresolved_branch_citations=unresolved,
        )
        candidates.append(candidate)
        ledger.append(
            _ledger_entry(
                source_type="channel",
                source_local_id=local_id,
                source_pointer=pointer,
                disposition="docket_mandatory",
                candidate_id=candidate["candidate_id"],
            )
        )
    return candidates, ledger


def _hft_seed_records(
    hft: dict[str, Any],
    *,
    allowed_refs: set[str] | None = None,
    allowed_branch_refs: set[str] | None = None,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    readers = _require_dict(hft.get("readers"), "HFT readers")
    if any(not isinstance(reader_id, str) for reader_id in readers):
        raise ValidationError("HFT reader IDs must be strings")
    fields = (
        ("baseline_models", "baseline_model", "model_id"),
        ("context_deltas", "context_delta", "model_id"),
        ("surprising_valid_outliers", "surprising_outlier", "outlier_id"),
    )
    for reader_id in sorted(readers):
        raw_reader = readers[reader_id]
        if not isinstance(raw_reader, dict):
            records.append(
                {
                    "reader_id": reader_id,
                    "source_local_id": f"{reader_id}:structure",
                    "kind": "reader_structure",
                    "pointer": (
                        "/v12_focus_trace_hermetic/readers/"
                        f"{json_pointer_escape(reader_id)}"
                    ),
                    "parse_error": "reader response must be an object",
                }
            )
            continue
        reader = raw_reader
        for field, kind, id_field in fields:
            raw_items = reader.get(field)
            if not isinstance(raw_items, list):
                records.append(
                    {
                        "reader_id": reader_id,
                        "source_local_id": f"{reader_id}:{field}:structure",
                        "kind": kind,
                        "pointer": (
                            "/v12_focus_trace_hermetic/readers/"
                            f"{json_pointer_escape(reader_id)}/{field}"
                        ),
                        "parse_error": f"{field} must be an array",
                    }
                )
                continue
            items = raw_items
            for index, item in enumerate(items):
                pointer = (
                    f"/v12_focus_trace_hermetic/readers/"
                    f"{json_pointer_escape(reader_id)}/{field}/{index}"
                )
                item_id = item.get(id_field) if isinstance(item, dict) else None
                if (
                    not isinstance(item, dict)
                    or not isinstance(item_id, str)
                    or not item_id.strip()
                ):
                    records.append(
                        {
                            "reader_id": reader_id,
                            "source_local_id": f"{reader_id}:{field}:{index}",
                            "kind": kind,
                            "pointer": pointer,
                            "item": item if isinstance(item, dict) else None,
                            "anchor_refs": [],
                            "branch_refs": [],
                            "scope_error": None,
                            "branch_error": None,
                            "parse_error": f"missing or empty {id_field}",
                        }
                    )
                    continue
                activation_trace = item.get("activation_trace")
                parse_error: str | None = None
                scope_error: str | None = None
                branch_error: str | None = None
                anchor_refs: list[str] = []
                if not isinstance(activation_trace, list):
                    parse_error = "activation_trace must be an array"
                elif not activation_trace:
                    parse_error = "activation_trace must not be empty"
                else:
                    for trace_index, trace in enumerate(activation_trace):
                        if not isinstance(trace, dict):
                            parse_error = (
                                f"activation_trace[{trace_index}] is not an object"
                            )
                            break
                        try:
                            _surah, _ayah, source_ref = _parse_canonical_ayah_ref(
                                trace.get("source_ref"),
                                f"HFT activation_trace[{trace_index}].source_ref",
                            )
                        except ValidationError as exc:
                            parse_error = str(exc)
                            break
                        anchor_refs.append(source_ref)
                        if allowed_refs is not None and source_ref not in allowed_refs:
                            scope_error = (
                                f"trace ref {source_ref} is outside packet window"
                            )
                branch_refs: list[str] = []
                if parse_error is None:
                    try:
                        branch_refs = _activation_branch_refs(activation_trace)
                    except ValidationError as exc:
                        parse_error = str(exc)
                if parse_error is None and allowed_branch_refs is not None:
                    unknown_branch_refs = sorted(
                        set(branch_refs) - allowed_branch_refs
                    )
                    if unknown_branch_refs:
                        branch_error = (
                            "activation trace cites branches outside the retained "
                            f"focus/pericope registries: {unknown_branch_refs}"
                        )
                records.append(
                    {
                        "reader_id": reader_id,
                        "source_local_id": f"{reader_id}:{item_id}",
                        "kind": kind,
                        "pointer": pointer,
                        "item": item,
                        "anchor_refs": sorted(set(anchor_refs)),
                        "parse_error": parse_error,
                        "scope_error": scope_error,
                        "branch_error": branch_error,
                        "branch_refs": branch_refs,
                    }
                )
    return records


def _hft_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    audit: dict[str, Any],
    allowed_branch_refs: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    hft = _require_dict(
        bundle.get("v12_focus_trace_hermetic"),
        "v12_focus_trace_hermetic",
    )
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    reader_trust = {
        reader["reader_id"]: (
            "trusted"
            if reader.get("identity_status") == "bound"
            else "legacy_unbound"
        )
        for reader in audit.get("readers", [])
        if isinstance(reader, dict) and isinstance(reader.get("reader_id"), str)
    }
    allowed_refs = set(audit.get("packet", {}).get("window") or [])
    lane = audit["evidence_lane"]
    evidence_scope = audit["evidence_scope"]
    for record in _hft_seed_records(
        hft,
        allowed_refs=allowed_refs,
        allowed_branch_refs=allowed_branch_refs,
    ):
        local_id = record["source_local_id"]
        if record.get("parse_error"):
            ledger.append(
                _ledger_entry(
                    source_type="hft",
                    source_local_id=local_id,
                    source_pointer=record["pointer"],
                    disposition="parse_failed",
                    reason=record["parse_error"],
                )
            )
            continue
        if record.get("scope_error"):
            ledger.append(
                _ledger_entry(
                    source_type="hft",
                    source_local_id=local_id,
                    source_pointer=record["pointer"],
                    disposition="out_of_scope",
                    reason=record["scope_error"],
                )
            )
            continue
        if record.get("branch_error"):
            ledger.append(
                _ledger_entry(
                    source_type="hft",
                    source_local_id=local_id,
                    source_pointer=record["pointer"],
                    disposition="parse_failed",
                    reason=record["branch_error"],
                )
            )
            continue
        item = record["item"]
        trust = reader_trust.get(record["reader_id"], "legacy_unbound")
        support_ids = [
            supports.add(
                source_type="hft",
                source_local_id=local_id,
                scope=lane,
                json_pointer=record["pointer"],
                value={
                    "focus_anchor": item.get("focus_anchor"),
                    "mechanism": item.get("mechanism"),
                    "changed_reading": item.get("changed_reading"),
                    "reader_inference": item.get("reader_inference"),
                    "containment": item.get("containment"),
                    "confidence": item.get("confidence"),
                },
                trust=trust,
            ),
            supports.add(
                source_type="hft",
                source_local_id=local_id,
                scope=lane,
                json_pointer=f"{record['pointer']}/activation_trace",
                value=item.get("activation_trace"),
                branch_refs=record["branch_refs"],
                trust=trust,
            ),
            supports.add(
                source_type="hft",
                source_local_id=local_id,
                scope=lane,
                json_pointer=f"{record['pointer']}/structural_cues",
                value=item.get("structural_cues"),
                trust=trust,
            ),
        ]
        mandatory = trust == "trusted"
        candidate = _candidate(
            ayah_ref=ayah_ref,
            lane=lane,
            source_type="hft",
            source_local_id=local_id,
            source_pointer=record["pointer"],
            kind=record["kind"],
            title=local_id,
            mandatory=mandatory,
            obligation="review" if mandatory else "optional_review",
            scope=evidence_scope,
            branch_refs=record["branch_refs"],
            anchor_refs=record["anchor_refs"],
            support_ids=support_ids,
            trust=trust,
        )
        candidates.append(candidate)
        ledger.append(
            _ledger_entry(
                source_type="hft",
                source_local_id=local_id,
                source_pointer=record["pointer"],
                disposition="docket_mandatory" if mandatory else "docket_optional",
                candidate_id=candidate["candidate_id"],
            )
        )
    return candidates, ledger


def _quarantined_hft(
    bundle: dict[str, Any],
    audit: dict[str, Any],
    *,
    allowed_branch_refs: set[str],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    raw_hft = bundle.get("v12_focus_trace_hermetic")
    seeds: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    structural_error = next(
        (
            reason.removeprefix("malformed HFT structure: ")
            for reason in audit.get("reasons", [])
            if isinstance(reason, str)
            and reason.startswith("malformed HFT structure: ")
        ),
        None,
    )
    try:
        hft = _require_dict(raw_hft, "v12_focus_trace_hermetic")
        packet = audit.get("packet")
        allowed_refs = (
            set(packet.get("window") or []) if isinstance(packet, dict) else None
        )
        records = _hft_seed_records(
            hft,
            allowed_refs=allowed_refs,
            allowed_branch_refs=allowed_branch_refs,
        )
    except ValidationError as exc:
        structural_error = str(exc)
        records = []
    if structural_error is None:
        structural_error = next(
            (
                f"{record['source_local_id']}: {record['parse_error']}"
                for record in records
                if record.get("parse_error")
            ),
            None,
        )
    if (
        structural_error is None
        and not records
        and audit.get("status") == "invalid"
    ):
        reasons = [
            reason
            for reason in audit.get("reasons", [])
            if isinstance(reason, str) and reason
        ]
        structural_error = "; ".join(reasons) or "invalid HFT has no enumerable seeds"
    if structural_error is not None and not records:
        ledger.append(
            _ledger_entry(
                source_type="hft",
                source_local_id="hft-structure",
                source_pointer="/v12_focus_trace_hermetic",
                disposition="parse_failed",
                reason=structural_error,
            )
        )
    for record in records:
        local_id = record["source_local_id"]
        if record.get("parse_error"):
            disposition = "parse_failed"
            reason = record["parse_error"]
        elif record.get("scope_error"):
            disposition = "out_of_scope"
            reason = record["scope_error"]
        elif record.get("branch_error"):
            disposition = "parse_failed"
            reason = record["branch_error"]
        else:
            disposition = "quarantined"
            reason = "HFT packet failed scope/identity audit"
        item = record.get("item")
        if not isinstance(item, dict):
            item = {}
        seeds.append(
            {
                "source_local_id": local_id,
                "kind": record["kind"],
                "branch_refs": record.get("branch_refs", []),
                "anchor_refs": record.get("anchor_refs", []),
                "focus_anchor": item.get("focus_anchor"),
                "changed_reading": item.get("changed_reading"),
                "source_pointer": record["pointer"],
                "adjudicable": False,
                "quarantine_reason": reason,
            }
        )
        ledger.append(
            _ledger_entry(
                source_type="hft",
                source_local_id=local_id,
                source_pointer=record["pointer"],
                disposition=disposition,
                reason=reason,
            )
        )
    return {
        "audit": audit,
        "seeds": sorted(seeds, key=lambda item: item["source_local_id"]),
        "structural_error": structural_error,
        "malformed_payload": raw_hft if structural_error is not None else None,
        "visible_to_adjudication": False,
    }, ledger


def _split_markdown_items(value: str) -> list[str]:
    text = value.strip()
    if not text:
        return []
    starts = list(re.finditer(r"(?m)^(?:\d+\.\s+|[-*]\s+)(?=\*\*)", text))
    if len(starts) <= 1:
        return [text]
    return [
        text[match.start() : starts[index + 1].start()].strip()
        if index + 1 < len(starts)
        else text[match.start() :].strip()
        for index, match in enumerate(starts)
    ]


def _walk_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    resolver: BranchResolver,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    sources = (
        ("v12_reader_walks", "surah_legacy"),
        ("v12_reader_walks_wide", "wide_context_legacy"),
    )
    for source_type, scope_name in sources:
        readers = _optional_dict(bundle, source_type, source_type)
        for reader_id in sorted(readers):
            reader = readers[reader_id]
            if not isinstance(reader, dict):
                ledger.append(
                    _ledger_entry(
                        source_type=source_type,
                        source_local_id=reader_id,
                        source_pointer=(
                            f"/{source_type}/{json_pointer_escape(reader_id)}"
                        ),
                        disposition="parse_failed",
                        reason="reader walk is not an object",
                    )
                )
                continue
            for field in ("activated_readings_md", "retrospective_surprises_md"):
                value = reader.get(field)
                if value is None or value == "":
                    continue
                if not isinstance(value, str):
                    ledger.append(
                        _ledger_entry(
                            source_type=source_type,
                            source_local_id=f"{reader_id}:{field}",
                            source_pointer=(
                                f"/{source_type}/{json_pointer_escape(reader_id)}/{field}"
                            ),
                            disposition="parse_failed",
                            reason=f"{field} is not text",
                        )
                    )
                    continue
                for index, item in enumerate(_split_markdown_items(value), start=1):
                    local_id = f"{reader_id}:{field}:{index}"
                    pointer = (
                        f"/{source_type}/{json_pointer_escape(reader_id)}/{field}"
                    )
                    branch_refs, unresolved = resolver.resolve_text(item)
                    support_id = supports.add(
                        source_type=source_type,
                        source_local_id=local_id,
                        scope="global",
                        json_pointer=pointer,
                        value=item,
                        branch_refs=branch_refs,
                        citable=False,
                        trust="legacy_unbound",
                    )
                    candidate = _candidate(
                        ayah_ref=ayah_ref,
                        lane="global",
                        source_type=source_type,
                        source_local_id=local_id,
                        source_pointer=f"{pointer}#item-{index}",
                        kind=(
                            "reader_walk_activation"
                            if field == "activated_readings_md"
                            else "reader_walk_retrospective"
                        ),
                        title=local_id,
                        mandatory=False,
                        obligation="optional_review",
                        scope=scope_name,
                        branch_refs=branch_refs,
                        anchor_refs=[ayah_ref],
                        support_ids=[support_id],
                        unresolved_branch_citations=unresolved,
                        trust="legacy_unbound",
                    )
                    candidates.append(candidate)
                    ledger.append(
                        _ledger_entry(
                            source_type=source_type,
                            source_local_id=local_id,
                            source_pointer=f"{pointer}#item-{index}",
                            disposition="docket_optional",
                            candidate_id=candidate["candidate_id"],
                        )
                    )
    return candidates, ledger


def _publication_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    root_mappings: dict[str, list[str]],
    known_branch_refs: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    publication = _optional_dict(
        bundle, "v12_cross_run_publication", "v12_cross_run_publication"
    )
    if not publication:
        return [], []
    findings = _require_list(
        publication.get("findings"), "v12_cross_run_publication.findings"
    )
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    identity_error: str | None = None
    parsed_refs: list[str] = []
    for field in ("ayah_ref", "canonical_ayah_ref"):
        if field not in publication:
            continue
        try:
            _surah, _ayah, normalized = _parse_canonical_ayah_ref(
                publication[field], f"v12_cross_run_publication.{field}"
            )
            parsed_refs.append(normalized)
        except ValidationError as exc:
            identity_error = str(exc)
            break
    if identity_error is None and not parsed_refs:
        identity_error = "publication must declare ayah_ref or canonical_ayah_ref"
    if identity_error is None and len(set(parsed_refs)) != 1:
        identity_error = "publication ayah_ref and canonical_ayah_ref disagree"
    publication_ref = parsed_refs[0] if parsed_refs else None
    if identity_error is None and "surah" in publication:
        publication_surah = publication["surah"]
        ref_surah = int(publication_ref.split(":", 1)[0])
        if (
            not isinstance(publication_surah, int)
            or isinstance(publication_surah, bool)
            or publication_surah <= 0
            or publication_surah != ref_surah
        ):
            identity_error = "publication surah disagrees with its ayah identity"
    for index, finding in enumerate(findings):
        local_id = f"finding-{index + 1}"
        pointer = f"/v12_cross_run_publication/findings/{index}"
        if identity_error is not None:
            ledger.append(
                _ledger_entry(
                    source_type="cross_run_publication",
                    source_local_id=local_id,
                    source_pointer=pointer,
                    disposition="parse_failed",
                    reason=identity_error,
                )
            )
            continue
        if publication_ref != ayah_ref:
            ledger.append(
                _ledger_entry(
                    source_type="cross_run_publication",
                    source_local_id=local_id,
                    source_pointer=pointer,
                    disposition="out_of_scope",
                    reason=f"publication ref {publication_ref!r} != {ayah_ref!r}",
                )
            )
            continue
        if not isinstance(finding, dict) or not isinstance(
            finding.get("text"), str
        ):
            ledger.append(
                _ledger_entry(
                    source_type="cross_run_publication",
                    source_local_id=local_id,
                    source_pointer=pointer,
                    disposition="parse_failed",
                    reason="finding must be an object with text",
                )
            )
            continue
        try:
            anchor_refs, branch_refs = _validated_publication_anchors(
                finding.get("anchors"),
                ayah_ref=ayah_ref,
                qac_morphemes=_require_list(bundle.get("qac_morphemes"), "qac_morphemes"),
                root_mappings=root_mappings,
                known_branch_refs=known_branch_refs,
                label="finding anchors",
            )
        except ValidationError as exc:
            ledger.append(
                _ledger_entry(
                    source_type="cross_run_publication",
                    source_local_id=local_id,
                    source_pointer=pointer,
                    disposition="parse_failed",
                    reason=str(exc),
                )
            )
            continue
        support_id = supports.add(
            source_type="cross_run_publication",
            source_local_id=local_id,
            scope="global",
            json_pointer=pointer,
            value={
                "text": finding.get("text"),
                "grade": finding.get("grade"),
                "anchors": finding.get("anchors"),
            },
            branch_refs=branch_refs,
        )
        candidate = _candidate(
            ayah_ref=ayah_ref,
            lane="global",
            source_type="cross_run_publication",
            source_local_id=local_id,
            source_pointer=pointer,
            kind="published_finding",
            title=finding["text"],
            mandatory=False,
            obligation="optional_review",
            scope="cross_run",
            branch_refs=branch_refs,
            anchor_refs=anchor_refs,
            support_ids=[support_id],
        )
        candidates.append(candidate)
        ledger.append(
            _ledger_entry(
                source_type="cross_run_publication",
                source_local_id=local_id,
                source_pointer=pointer,
                disposition="docket_optional",
                candidate_id=candidate["candidate_id"],
            )
        )
    return candidates, ledger


def _legacy_response_candidates(
    bundle: dict[str, Any],
    *,
    ayah_ref: str,
    supports: SupportBuilder,
    resolver: BranchResolver,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    responses = _optional_dict(
        bundle, "v12_reader_responses", "v12_reader_responses"
    )
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []
    for reader_id in sorted(responses):
        value = responses[reader_id]
        local_id = str(reader_id)
        pointer = f"/v12_reader_responses/{json_pointer_escape(local_id)}"
        if value is None or value == "" or value == [] or value == {}:
            continue
        branch_refs, unresolved = resolver.resolve_text(value)
        support_id = supports.add(
            source_type="legacy_reader_response",
            source_local_id=local_id,
            scope="global",
            json_pointer=pointer,
            value=value,
            branch_refs=branch_refs,
            citable=False,
            trust="legacy_unbound",
        )
        candidate = _candidate(
            ayah_ref=ayah_ref,
            lane="global",
            source_type="legacy_reader_response",
            source_local_id=local_id,
            source_pointer=pointer,
            kind="legacy_reader_response",
            title=local_id,
            mandatory=False,
            obligation="optional_review",
            scope="legacy_unknown",
            branch_refs=branch_refs,
            anchor_refs=[ayah_ref],
            support_ids=[support_id],
            unresolved_branch_citations=unresolved,
            trust="legacy_unbound",
        )
        candidates.append(candidate)
        ledger.append(
            _ledger_entry(
                source_type="legacy_reader_response",
                source_local_id=local_id,
                source_pointer=pointer,
                disposition="docket_optional",
                candidate_id=candidate["candidate_id"],
            )
        )
    return candidates, ledger


def _deduplicate_candidates(
    candidates: list[dict[str, Any]], ledger: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for candidate in candidates:
        candidate_id = candidate["candidate_id"]
        if candidate_id not in seen:
            seen[candidate_id] = candidate
            continue
        for entry in ledger:
            if (
                entry.get("candidate_id") == candidate_id
                and entry["disposition"].startswith("docket_")
                and entry["source_local_id"] == candidate["source_local_id"]
            ):
                entry["disposition"] = "duplicate"
                entry["reason"] = "deterministic candidate identity collision"
                entry["candidate_id"] = None
                break
    return sorted(
        seen.values(),
        key=lambda item: (
            0 if item["mandatory"] else 1,
            {"micro": 0, "macro": 1, "global": 2}.get(item["lane"], 9),
            item["source_type"],
            item["source_local_id"],
            item["candidate_id"],
        ),
    )


def _accounting(
    ledger: list[dict[str, Any]], candidates: list[dict[str, Any]]
) -> dict[str, Any]:
    candidate_records: dict[str, dict[str, Any]] = {}
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise ValidationError(f"Candidate accounting record {index} must be an object")
        candidate_id = candidate.get("candidate_id")
        if (
            not isinstance(candidate_id, str)
            or not re.fullmatch(r"cand_[0-9a-f]{20}", candidate_id)
            or candidate_id in candidate_records
            or not isinstance(candidate.get("source_type"), str)
            or candidate["source_type"] not in CANDIDATE_SOURCE_TYPES
            or not isinstance(candidate.get("source_local_id"), str)
            or not candidate["source_local_id"]
            or not isinstance(candidate.get("mandatory"), bool)
        ):
            raise ValidationError(f"Candidate accounting record {index} is invalid")
        candidate_records[candidate_id] = candidate

    dispositions: dict[str, int] = {}
    source_types: dict[str, int] = {}
    docket_ledger_ids: list[str] = []
    seed_identities: set[tuple[str, str]] = set()
    for index, raw_entry in enumerate(ledger):
        entry = _require_dict(raw_entry, f"candidate_ledger[{index}]")
        _require_exact_keys(
            entry,
            {
                "source_type",
                "source_local_id",
                "source_pointer",
                "disposition",
                "candidate_id",
                "reason",
            },
            f"candidate_ledger[{index}]",
        )
        disposition = entry["disposition"]
        source_type = entry["source_type"]
        source_local_id = entry["source_local_id"]
        source_pointer = entry["source_pointer"]
        candidate_id = entry["candidate_id"]
        reason = entry["reason"]
        if (
            not isinstance(disposition, str)
            or disposition not in LEDGER_DISPOSITIONS
            or not isinstance(source_type, str)
            or source_type not in CANDIDATE_SOURCE_TYPES
            or not isinstance(source_local_id, str)
            or not source_local_id
            or not isinstance(source_pointer, str)
            or not source_pointer.startswith("/")
            or (reason is not None and (not isinstance(reason, str) or not reason))
        ):
            raise ValidationError(f"candidate_ledger[{index}] fields are invalid")
        seed_identity = (source_type, source_pointer)
        if seed_identity in seed_identities:
            raise ValidationError("Candidate-ledger source identities must be unique")
        seed_identities.add(seed_identity)
        docket_disposition = disposition in ("docket_mandatory", "docket_optional")
        if docket_disposition:
            if (
                not isinstance(candidate_id, str)
                or not re.fullmatch(r"cand_[0-9a-f]{20}", candidate_id)
                or candidate_id not in candidate_records
            ):
                raise ValidationError(
                    f"candidate_ledger[{index}] has an invalid docket candidate binding"
                )
            candidate = candidate_records[candidate_id]
            if (
                source_type != candidate["source_type"]
                or source_local_id != candidate["source_local_id"]
                or source_pointer != candidate["source_pointer"]
                or (disposition == "docket_mandatory") is not candidate["mandatory"]
            ):
                raise ValidationError(
                    f"candidate_ledger[{index}] provenance or disposition is inconsistent"
                )
            docket_ledger_ids.append(candidate_id)
        elif candidate_id is not None:
            raise ValidationError(
                f"candidate_ledger[{index}] non-docket row must not bind a candidate"
            )
        dispositions[disposition] = dispositions.get(disposition, 0) + 1
        source_types[source_type] = source_types.get(source_type, 0) + 1
    discovered = len(ledger)
    accounted = sum(dispositions.values())
    if discovered != accounted:
        raise ValidationError(
            f"Candidate accounting mismatch: discovered={discovered}, accounted={accounted}"
        )
    docket_ids = set(candidate_records)
    ledger_ids = set(docket_ledger_ids)
    if len(docket_ledger_ids) != len(ledger_ids) or docket_ids != ledger_ids:
        raise ValidationError("Candidate ledger and docket IDs disagree")
    return {
        "discovered_seed_count": discovered,
        "accounted_seed_count": accounted,
        "by_disposition": dict(sorted(dispositions.items())),
        "by_source_type": dict(sorted(source_types.items())),
        "docket_candidate_count": len(candidates),
        "mandatory_candidate_count": sum(
            1 for candidate in candidates if candidate["mandatory"]
        ),
        "optional_candidate_count": sum(
            1 for candidate in candidates if not candidate["mandatory"]
        ),
        "selection_eligible_candidate_count": sum(
            1 for candidate in candidates if candidate["selection_eligible"]
        ),
        "selection_ineligible_candidate_count": sum(
            1 for candidate in candidates if not candidate["selection_eligible"]
        ),
    }


def _source_inventory(
    bundle: dict[str, Any], ledger: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    source_keys = {
        "qac_morphemes": ("qac_morpheme",),
        "word_analysis": ("word_analysis",),
        "channel_subchannels_anchored_here": ("channel",),
        "v12_focus_trace_hermetic": ("hft",),
        "v12_reader_walks": ("v12_reader_walks",),
        "v12_reader_walks_wide": ("v12_reader_walks_wide",),
        "v12_cross_run_publication": ("cross_run_publication",),
        "v12_reader_responses": ("legacy_reader_response",),
    }
    inventory: dict[str, dict[str, Any]] = {}
    for bundle_key, ledger_types in source_keys.items():
        if bundle_key not in bundle:
            state = "absent"
        elif bundle[bundle_key] in (None, "", [], {}):
            state = "present_empty"
        else:
            state = "present_nonempty"
        entries = [
            item for item in ledger if item["source_type"] in ledger_types
        ]
        inventory[bundle_key] = {
            "state": state,
            "policy": "candidate_source",
            "seed_count": len(entries),
            "dispositions": dict(
                sorted({
                    disposition: sum(
                        1
                        for item in entries
                        if item["disposition"] == disposition
                    )
                    for disposition in {item["disposition"] for item in entries}
                }.items())
            ),
        }
    excluded_sources = {
        "inter_ayah_rows": (
            "Raw inter-ayah rows are not model-visible in v1; adjudicable relations "
            "must arrive through bounded word, channel, HFT, walk, or publication seeds."
        ),
        "butuncul_okuma_line": (
            "Whole-reading prose is excluded to avoid importing a prior synthesis as evidence."
        ),
        "channel_generated_outputs": (
            "Generated channel prose is excluded; reviewed anchored channel nominations are used."
        ),
    }
    for bundle_key, reason in excluded_sources.items():
        if bundle_key not in bundle:
            state = "absent"
        elif bundle[bundle_key] in (None, "", [], {}):
            state = "present_empty"
        else:
            state = "present_nonempty_excluded"
        inventory[bundle_key] = {
            "state": state,
            "policy": "excluded",
            "reason": reason,
            "seed_count": 0,
            "dispositions": {},
        }
    return inventory


def _branch_review_grounding_gaps(
    *,
    ayah_ref: str,
    branch_registry: list[dict[str, Any]],
    nominated_branch_registry: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    support_registry: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Prove that every required branch review has admissible source grounding."""
    support_map = {
        support["support_id"]: support
        for support in support_registry
        if isinstance(support, dict) and isinstance(support.get("support_id"), str)
    }
    gaps: list[dict[str, Any]] = []
    for root in branch_registry:
        branches = root.get("branches") or []
        if not branches:
            continue
        root_id = root.get("root_id")
        grounded = any(
            candidate.get("lane") == "micro"
            and root_id in (candidate.get("root_ids") or [])
            and any(
                anchor == ayah_ref or anchor.startswith(f"{ayah_ref}:")
                for anchor in (candidate.get("anchor_refs") or [])
            )
            and any(
                support_id in support_map
                and support_map[support_id].get("role") == SUPPORT_ROLE_OCCURRENCE
                and support_map[support_id].get("trust") == "trusted"
                and support_map[support_id].get("citable") is True
                for support_id in (candidate.get("support_ids") or [])
            )
            for candidate in candidates
        )
        if not grounded:
            gaps.append(
                {
                    "kind": "focus_occurrence_missing",
                    "root_id": root_id,
                    "branch_refs": sorted(
                        branch["branch_ref"] for branch in branches
                    ),
                    "reason": (
                        "No QAC occurrence candidate owns trusted, citable "
                        "focus_occurrence support for this mapped root."
                    ),
                }
            )
    for branch in nominated_branch_registry:
        branch_ref = branch.get("branch_ref")
        owners = [
            candidate
            for candidate in candidates
            if branch_ref in (candidate.get("branch_refs") or [])
        ]
        if not owners:
            gaps.append(
                {
                    "kind": "nominated_owner_missing",
                    "root_id": branch_ref.split("/", 1)[0],
                    "branch_refs": [branch_ref],
                    "reason": "No docket candidate owns this nominated branch.",
                }
            )
            continue
        grounded = any(
            owner.get("trust") == "trusted"
            and support_id in support_map
            and support_map[support_id].get("trust") == "trusted"
            and support_map[support_id].get("citable") is True
            and support_map[support_id].get("role") == SUPPORT_ROLE_NOMINATION
            and branch_ref in (support_map[support_id].get("branch_refs") or [])
            for owner in owners
            for support_id in (owner.get("support_ids") or [])
        )
        if not grounded:
            gaps.append(
                {
                    "kind": "nominated_grounding_missing",
                    "root_id": branch_ref.split("/", 1)[0],
                    "branch_refs": [branch_ref],
                    "reason": (
                        "The nominated branch has no candidate-owned trusted, "
                        "citable branch_nomination support."
                    ),
                }
            )
    return sorted(
        gaps,
        key=lambda item: (
            item["kind"],
            item["root_id"],
            tuple(item["branch_refs"]),
        ),
    )


def _docket_payload_hash(docket: dict[str, Any]) -> str:
    payload = copy.deepcopy(docket)
    payload.get("identity", {}).pop("docket_payload_sha256", None)
    return canonical_sha256(payload)


def validate_docket(docket: dict[str, Any]) -> None:
    if docket.get("schema_version") != DOCKET_SCHEMA:
        raise ValidationError("Unexpected docket schema_version")
    _require_exact_keys(
        docket,
        {
            "schema_version",
            "identity",
            "scope",
            "focus",
            "focus_root_mappings",
            "branch_registry",
            "nominated_branch_registry",
            "candidates",
            "support_registry",
            "coverage",
            "adjudication_gate",
            "adjudication_rules",
            "limits",
        },
        "docket",
    )
    identity = _require_dict(docket.get("identity"), "docket identity")
    _require_exact_keys(
        identity,
        {"ayah_ref", "source_canonical_sha256", "docket_payload_sha256"},
        "docket identity",
    )
    if not isinstance(identity["ayah_ref"], str) or not re.fullmatch(
        r"[1-9][0-9]*:[1-9][0-9]*", identity["ayah_ref"]
    ):
        raise ValidationError("Docket ayah identity is invalid")
    if any(
        not isinstance(identity[field], str)
        or not re.fullmatch(r"[0-9a-f]{64}", identity[field])
        for field in ("source_canonical_sha256", "docket_payload_sha256")
    ):
        raise ValidationError("Docket hash identity is invalid")
    limits = _require_dict(docket.get("limits"), "docket limits")
    expected_limit_fields = {
        "max_optional_candidates",
        "max_support_chars",
        "max_support_per_candidate",
        "max_branch_bytes_per_root",
        "max_pericope_ayahs",
        "max_docket_bytes",
    }
    _require_exact_keys(limits, expected_limit_fields, "docket limits")
    if any(
        not isinstance(value, int) or isinstance(value, bool) or value <= 0
        for value in limits.values()
    ):
        raise ValidationError("Docket limits must be positive integers")
    if limits["max_pericope_ayahs"] > MAX_PERICOPE_AYAHS_CAP:
        raise ValidationError("Docket pericope limit exceeds the hard safety cap")
    candidates = _require_list(docket.get("candidates"), "docket candidates")
    supports = _require_list(
        docket.get("support_registry"), "docket support_registry"
    )
    support_ids: set[str] = set()
    support_by_id: dict[str, dict[str, Any]] = {}
    for item in supports:
        if not isinstance(item, dict):
            raise ValidationError("Every support record must be an object")
        required = {
            "support_id",
            "source_type",
            "source_local_id",
            "scope",
            "json_pointer",
            "role",
            "citable",
            "trust",
            "branch_refs",
            "text",
        }
        _require_exact_keys(item, required, "support record")
        if (
            not isinstance(item["support_id"], str)
            or not isinstance(item["source_type"], str)
            or not item["source_type"]
            or not isinstance(item["source_local_id"], str)
            or not item["source_local_id"]
            or not isinstance(item["scope"], str)
            or item["scope"] not in ("micro", "macro", "global")
            or not isinstance(item["json_pointer"], str)
            or not item["json_pointer"].startswith("/")
            or not isinstance(item["role"], str)
            or item["role"]
            not in (
                SUPPORT_ROLE_OCCURRENCE,
                SUPPORT_ROLE_EVIDENCE,
                SUPPORT_ROLE_NOMINATION,
                SUPPORT_ROLE_CONTEXT,
            )
            or not isinstance(item["citable"], bool)
            or not isinstance(item["trust"], str)
            or item["trust"] not in ("trusted", "legacy_unbound")
            or not isinstance(item["text"], str)
            or not item["text"]
        ):
            raise ValidationError("Support record fields are invalid")
        if item["role"] != support_role_for(
            item["source_type"], item["json_pointer"]
        ):
            raise ValidationError("Support role disagrees with canonical provenance")
        support_branch_refs = _require_list(
            item["branch_refs"], "support record branch_refs"
        )
        if (
            any(
                not isinstance(branch_ref, str)
                or not CANONICAL_BRANCH_REF_RE.fullmatch(branch_ref)
                for branch_ref in support_branch_refs
            )
            or support_branch_refs != sorted(set(support_branch_refs))
        ):
            raise ValidationError("Support branch_refs are invalid or noncanonical")
        expected_support_id = _stable_id(
            "sup",
            {
                "source_type": item["source_type"],
                "source_local_id": item["source_local_id"],
                "scope": item["scope"],
                "json_pointer": item["json_pointer"],
                "role": item["role"],
                "citable": item["citable"],
                "trust": item["trust"],
                "branch_refs": support_branch_refs,
                "text_sha256": sha256_bytes(item["text"].encode("utf-8")),
            },
        )
        if item["support_id"] != expected_support_id:
            raise ValidationError("Support identity hash mismatch")
        support_ids.add(item["support_id"])
        support_by_id[item["support_id"]] = item
    if len(support_ids) != len(supports):
        raise ValidationError("Support IDs must be present and unique")
    focus = _require_dict(docket.get("focus"), "docket focus")
    _require_exact_keys(
        focus,
        {
            "arabic_uthmani",
            "qac_morphemes",
            "word_analysis_refs",
            "word_analysis_qac_refs",
        },
        "docket focus",
    )
    if not isinstance(focus.get("arabic_uthmani"), str) or not focus[
        "arabic_uthmani"
    ].strip():
        raise ValidationError("Docket focus Arabic text is missing")
    focus_morphemes = _require_list(
        focus.get("qac_morphemes"), "docket focus qac_morphemes"
    )
    if not focus_morphemes:
        raise ValidationError("Docket focus qac_morphemes must not be empty")
    qac_fields = {
        "qac_ref",
        "qac_word_ref",
        "surface_ar",
        "lemma_ar",
        "root_ar",
        "pos",
        "morpheme_role",
        "morph_features",
    }
    seen_qac_refs: set[str] = set()
    qac_by_pointer: dict[str, dict[str, Any]] = {}
    for index, raw_morpheme in enumerate(focus_morphemes):
        morpheme = _require_dict(raw_morpheme, f"focus qac_morphemes[{index}]")
        _require_exact_keys(morpheme, qac_fields, f"focus qac_morphemes[{index}]")
        qac_ref = morpheme.get("qac_ref")
        qac_word_ref = morpheme.get("qac_word_ref")
        if (
            not isinstance(qac_ref, str)
            or not isinstance(qac_word_ref, str)
            or not QAC_REF_RE.fullmatch(qac_ref)
            or not WORD_REF_RE.fullmatch(qac_word_ref)
            or not qac_ref.startswith(f"{qac_word_ref}:")
            or not qac_word_ref.startswith(f"{identity['ayah_ref']}:")
            or qac_ref in seen_qac_refs
            or any(
                not isinstance(morpheme.get(field), str)
                for field in qac_fields - {"qac_ref", "qac_word_ref"}
            )
        ):
            raise ValidationError("Docket focus QAC identities are invalid")
        seen_qac_refs.add(qac_ref)
        qac_by_pointer[f"/qac_morphemes/{index}"] = morpheme
    word_analysis_refs = _require_list(
        focus.get("word_analysis_refs"), "docket focus word_analysis_refs"
    )
    for index, word_ref in enumerate(word_analysis_refs):
        if word_ref is None:
            continue
        _validated_word_ref(
            word_ref,
            ayah_ref=identity["ayah_ref"],
            word_count=len(word_analysis_refs),
            label=f"docket focus word_analysis_refs[{index}]",
        )
    word_analysis_qac_refs = _require_list(
        focus.get("word_analysis_qac_refs"),
        "docket focus word_analysis_qac_refs",
    )
    if len(word_analysis_qac_refs) != len(word_analysis_refs):
        raise ValidationError(
            "Docket word-analysis QAC lineage does not align with word rows"
        )
    qac_order = {
        morpheme["qac_ref"]: index
        for index, morpheme in enumerate(focus_morphemes)
    }
    qac_words = {
        morpheme["qac_ref"]: morpheme["qac_word_ref"]
        for morpheme in focus_morphemes
    }
    for index, raw_refs in enumerate(word_analysis_qac_refs):
        refs = _require_list(
            raw_refs, f"docket focus word_analysis_qac_refs[{index}]"
        )
        if (
            any(not isinstance(ref, str) or ref not in qac_order for ref in refs)
            or len(refs) != len(set(refs))
            or len({qac_words[ref] for ref in refs}) > 1
            or [qac_order[ref] for ref in refs]
            != sorted(qac_order[ref] for ref in refs)
        ):
            raise ValidationError(
                "Docket word-analysis QAC lineage is invalid"
            )
    expected_focus_roots = {
        item["root_ar"]
        for item in focus_morphemes
        if isinstance(item, dict)
        and isinstance(item.get("root_ar"), str)
        and item["root_ar"]
    }
    root_mappings = _require_dict(
        docket.get("focus_root_mappings"), "focus_root_mappings"
    )
    if set(root_mappings) != expected_focus_roots:
        raise ValidationError("Focus-root mappings do not cover exact QAC roots")
    branch_roots = _require_list(docket.get("branch_registry"), "branch_registry")
    root_records: dict[str, dict[str, Any]] = {}
    focus_refs: set[str] = set()
    for raw_root in branch_roots:
        root = _require_dict(raw_root, "branch_registry root")
        _require_exact_keys(
            root,
            {"root_id", "root_ar", "qac_roots_ar", "mapping_role", "branches"},
            "branch_registry root",
        )
        root_id = root.get("root_id")
        if (
            not isinstance(root_id, str)
            or not ROOT_ID_RE.fullmatch(root_id)
            or root_id in root_records
        ):
            raise ValidationError("Branch-registry root IDs must be present and unique")
        if root.get("root_ar") is not None and not isinstance(root["root_ar"], str):
            raise ValidationError(f"{root_id} root_ar is invalid")
        if root.get("mapping_role") is not None and not isinstance(
            root["mapping_role"], str
        ):
            raise ValidationError(f"{root_id} mapping_role is invalid")
        qac_roots = _require_list(root.get("qac_roots_ar"), f"{root_id} qac_roots_ar")
        if (
            any(not isinstance(item, str) or not item for item in qac_roots)
            or len(qac_roots) != len(set(qac_roots))
        ):
            raise ValidationError(f"{root_id} qac_roots_ar contains invalid values")
        root_records[root_id] = root
        for raw_branch in _require_list(root.get("branches"), f"{root_id} branches"):
            branch = _require_dict(raw_branch, f"{root_id} branch")
            _require_exact_keys(
                branch,
                {"branch_ref", "status", "branch_kind", "gloss", "boundary", "source_pointer"},
                f"{root_id} branch",
            )
            branch_ref = _require_canonical_branch_ref(
                branch.get("branch_ref"), f"{root_id} branch_ref"
            )
            if branch_ref.split("/", 1)[0] != root_id or branch_ref in focus_refs:
                raise ValidationError("Focus branch refs must be valid and unique")
            if not isinstance(branch["gloss"], str) or not branch["gloss"].strip():
                raise ValidationError(f"{branch_ref} gloss is missing")
            if any(
                branch[field] is not None and not isinstance(branch[field], str)
                for field in ("status", "branch_kind", "boundary")
            ):
                raise ValidationError(f"{branch_ref} metadata fields are invalid")
            if not isinstance(branch["source_pointer"], str) or not branch[
                "source_pointer"
            ].startswith("/"):
                raise ValidationError(f"{branch_ref} source pointer is invalid")
            focus_refs.add(branch_ref)
    mapped_root_ids: set[str] = set()
    for root_ar, raw_ids in root_mappings.items():
        root_ids = _require_list(raw_ids, f"focus_root_mappings.{root_ar}")
        if (
            not root_ids
            or any(
                not isinstance(root_id, str) or not ROOT_ID_RE.fullmatch(root_id)
                for root_id in root_ids
            )
            or len(root_ids) != len(set(root_ids))
        ):
            raise ValidationError(f"Focus root {root_ar} lacks unique root mappings")
        for root_id in root_ids:
            if not isinstance(root_id, str) or root_id not in root_records:
                raise ValidationError(f"Focus root {root_ar} maps to unknown root record")
            if _canonical_arabic_root(root_ar) not in {
                _canonical_arabic_root(item)
                for item in root_records[root_id]["qac_roots_ar"]
            }:
                raise ValidationError(f"Focus root {root_ar} mapping is inconsistent")
            mapped_root_ids.add(root_id)
    if mapped_root_ids != set(root_records):
        raise ValidationError("Branch registry contains unmapped focus-root records")
    scope = _require_dict(docket.get("scope"), "docket scope")
    _require_exact_keys(
        scope,
        {"pericope", "lane_contract", "hft", "branch_coverage"},
        "docket scope",
    )
    pericope = _require_dict(scope.get("pericope"), "scope.pericope")
    _require_exact_keys(
        pericope,
        {"id", "number", "ayah_from", "ayah_to", "label", "refs"},
        "scope.pericope",
    )
    if (
        not isinstance(pericope["id"], str)
        or not pericope["id"]
        or not isinstance(pericope["number"], int)
        or isinstance(pericope["number"], bool)
        or pericope["number"] <= 0
        or not isinstance(pericope["ayah_from"], int)
        or isinstance(pericope["ayah_from"], bool)
        or not isinstance(pericope["ayah_to"], int)
        or isinstance(pericope["ayah_to"], bool)
        or pericope["ayah_from"] <= 0
        or pericope["ayah_to"] < pericope["ayah_from"]
        or (
            pericope["label"] is not None
            and not isinstance(pericope["label"], str)
        )
    ):
        raise ValidationError("Pericope metadata is invalid")
    pericope_width = pericope["ayah_to"] - pericope["ayah_from"] + 1
    if pericope_width > limits["max_pericope_ayahs"]:
        raise ValidationError("Pericope exceeds the docket's bound width")
    pericope_refs = _require_list(pericope["refs"], "scope.pericope.refs")
    surah = int(identity["ayah_ref"].split(":", 1)[0])
    expected_pericope_refs = [
        f"{surah}:{ayah}"
        for ayah in range(pericope["ayah_from"], pericope["ayah_to"] + 1)
    ]
    if pericope_refs != expected_pericope_refs or identity["ayah_ref"] not in pericope_refs:
        raise ValidationError("Pericope refs are not the exact contiguous focus window")
    lane_contract = _require_dict(scope.get("lane_contract"), "scope.lane_contract")
    _require_exact_keys(
        lane_contract, {"micro", "macro", "global"}, "scope.lane_contract"
    )
    if any(
        not isinstance(lane_contract[lane], str) or not lane_contract[lane]
        for lane in ("micro", "macro", "global")
    ):
        raise ValidationError("Lane contract is invalid")
    branch_coverage = _require_dict(
        scope.get("branch_coverage"), "scope.branch_coverage"
    )
    gaps = _require_list(
        branch_coverage.get("missing_dictionary_roots"),
        "scope.branch_coverage.missing_dictionary_roots",
    )
    gap_ids: set[str] = set()
    for raw_gap in gaps:
        gap = _require_dict(raw_gap, "missing dictionary root")
        if set(gap) != {"root_id", "root_ar", "qac_roots_ar", "reason"}:
            raise ValidationError("Missing-dictionary root fields drifted")
        root_id = gap.get("root_id")
        if root_id not in root_records or root_id in gap_ids:
            raise ValidationError("Missing-dictionary root IDs are invalid")
        if root_records[root_id]["branches"]:
            raise ValidationError("Missing-dictionary root unexpectedly carries branches")
        if gap.get("root_ar") != root_records[root_id].get("root_ar"):
            raise ValidationError("Missing-dictionary root Arabic identity drifted")
        expected_gap_qac_roots = sorted(
            root_ar
            for root_ar, mapped_ids in root_mappings.items()
            if root_id in mapped_ids
        )
        if gap.get("qac_roots_ar") != expected_gap_qac_roots:
            raise ValidationError("Missing-dictionary QAC mappings drifted")
        if not isinstance(gap.get("reason"), str) or not gap["reason"]:
            raise ValidationError("Missing-dictionary root lacks a reason")
        gap_ids.add(root_id)
    zero_branch_root_ids = {
        root_id for root_id, root in root_records.items() if not root["branches"]
    }
    if zero_branch_root_ids != gap_ids:
        raise ValidationError(
            "Zero-branch focus roots and missing-dictionary gaps disagree"
        )
    expected_branch_coverage = {
        "complete": not gaps,
        "focus_root_count": len(expected_focus_roots),
        "mapped_root_record_count": len(root_records),
        "registered_branch_count": len(focus_refs),
        "missing_dictionary_roots": gaps,
    }
    if branch_coverage != expected_branch_coverage:
        raise ValidationError("Focus-root branch coverage accounting is inconsistent")
    nominated_refs: set[str] = set()
    nominated_fields = {
        "branch_ref",
        "root_ar",
        "image_ar",
        "image_en",
        "scope_ar",
        "scope_en",
        "source_file",
        "source_pointer",
    }
    for raw_branch in _require_list(
        docket.get("nominated_branch_registry"), "nominated_branch_registry"
    ):
        branch = _require_dict(raw_branch, "nominated branch")
        _require_exact_keys(branch, nominated_fields, "nominated branch")
        branch_ref = _require_canonical_branch_ref(
            branch.get("branch_ref"), "nominated branch_ref"
        )
        if branch_ref in nominated_refs:
            raise ValidationError("Nominated branch refs must be unique")
        if not isinstance(branch.get("root_ar"), str) or not branch["root_ar"]:
            raise ValidationError(f"{branch_ref} nominated root_ar is invalid")
        if any(
            branch[field] is not None and not isinstance(branch[field], str)
            for field in (
                "image_ar",
                "image_en",
                "scope_ar",
                "scope_en",
                "source_file",
            )
        ):
            raise ValidationError(f"{branch_ref} nominated metadata is invalid")
        if not any(
            isinstance(branch.get(field), str) and branch[field].strip()
            for field in ("image_ar", "image_en")
        ):
            raise ValidationError(
                f"{branch_ref} nominated branch lacks an image descriptor"
            )
        if not isinstance(branch["source_pointer"], str) or not branch[
            "source_pointer"
        ].startswith("/"):
            raise ValidationError(f"{branch_ref} nominated source pointer is invalid")
        nominated_refs.add(branch_ref)
    if focus_refs & nominated_refs:
        raise ValidationError("Focus and nominated branch registries overlap")
    registered_refs = focus_refs | nominated_refs
    for support in supports:
        if support["trust"] != "trusted":
            continue
        unknown_support_refs = sorted(set(support["branch_refs"]) - registered_refs)
        if unknown_support_refs:
            raise ValidationError(
                "Trusted support cites branches outside the retained registries: "
                f"{unknown_support_refs}"
            )
    candidate_ids: set[str] = set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise ValidationError("Every docket candidate must be an object")
        candidate_id = candidate.get("candidate_id")
        if not isinstance(candidate_id, str) or candidate_id in candidate_ids:
            raise ValidationError("Candidate IDs must be present and unique")
        required = {
            "candidate_id",
            "lane",
            "kind",
            "source_type",
            "source_local_id",
            "source_pointer",
            "title",
            "mandatory",
            "obligation",
            "scope",
            "trust",
            "branch_refs",
            "root_ids",
            "anchor_refs",
            "support_ids",
            "focus_branch_refs",
            "nominated_branch_refs",
            "unresolved_branch_refs",
            "unresolved_branch_citations",
            "adjudicable",
            "selection_eligible",
            "selection_ineligibility_reasons",
        }
        _require_exact_keys(candidate, required, f"candidate {candidate_id}")
        if not re.fullmatch(r"cand_[0-9a-f]{20}", candidate_id):
            raise ValidationError(f"Candidate {candidate_id} has invalid ID syntax")
        if not isinstance(candidate["lane"], str) or candidate["lane"] not in (
            "micro",
            "macro",
            "global",
        ):
            raise ValidationError(f"Candidate {candidate_id} has invalid lane")
        if (
            not isinstance(candidate["source_type"], str)
            or candidate["source_type"] not in CANDIDATE_SOURCE_TYPES
        ):
            raise ValidationError(f"Candidate {candidate_id} has invalid source type")
        if not isinstance(candidate["trust"], str) or candidate["trust"] not in (
            "trusted",
            "legacy_unbound",
        ):
            raise ValidationError(f"Candidate {candidate_id} has invalid trust")
        for field in (
            "kind",
            "source_type",
            "source_local_id",
            "source_pointer",
            "title",
            "obligation",
            "scope",
        ):
            if not isinstance(candidate[field], str):
                raise ValidationError(f"Candidate {candidate_id} {field} is invalid")
        if not candidate["source_pointer"].startswith("/"):
            raise ValidationError(f"Candidate {candidate_id} source pointer is invalid")
        if not isinstance(candidate["mandatory"], bool) or not isinstance(
            candidate["adjudicable"], bool
        ):
            raise ValidationError(f"Candidate {candidate_id} flags are invalid")
        for field in (
            "branch_refs",
            "root_ids",
            "anchor_refs",
            "support_ids",
            "focus_branch_refs",
            "nominated_branch_refs",
            "unresolved_branch_refs",
        ):
            values = _require_list(candidate[field], f"candidate {candidate_id} {field}")
            if any(not isinstance(item, str) or not item for item in values) or len(
                values
            ) != len(set(values)) or values != sorted(values):
                raise ValidationError(
                    f"Candidate {candidate_id} {field} is invalid or noncanonical"
                )
        if not candidate["support_ids"]:
            raise ValidationError(f"Candidate {candidate_id} lacks support")
        missing = set(candidate["support_ids"]) - support_ids
        if missing:
            raise ValidationError(
                f"Candidate {candidate_id} references unknown supports: {sorted(missing)}"
            )
        candidate_supports = [
            support_by_id[support_id] for support_id in candidate["support_ids"]
        ]
        if any(
            support["source_type"] != candidate["source_type"]
            for support in candidate_supports
        ):
            raise ValidationError(
                f"Candidate {candidate_id} support provenance does not match its source"
            )
        if any(
            support["trust"] != candidate["trust"] for support in candidate_supports
        ) or (
            candidate["trust"] == "trusted"
            and any(not support["citable"] for support in candidate_supports)
        ):
            raise ValidationError(
                f"Candidate {candidate_id} support trust does not match its contract"
            )
        if candidate["source_type"] != "word_analysis" and any(
            support["source_local_id"] != candidate["source_local_id"]
            for support in candidate_supports
        ):
            raise ValidationError(
                f"Candidate {candidate_id} support provenance does not match its source"
            )
        for branch_ref in (
            candidate["branch_refs"]
            + candidate["focus_branch_refs"]
            + candidate["nominated_branch_refs"]
            + candidate["unresolved_branch_refs"]
        ):
            _require_canonical_branch_ref(
                branch_ref, f"candidate {candidate_id} branch ref"
            )
        if any(not ROOT_ID_RE.fullmatch(root_id) for root_id in candidate["root_ids"]):
            raise ValidationError(f"Candidate {candidate_id} root IDs are invalid")
        if not set(candidate["root_ids"]) <= set(root_records):
            raise ValidationError(f"Candidate {candidate_id} cites unknown focus roots")
        if candidate["source_type"] == "word_analysis":
            pointer_match = WORD_TOPIC_SOURCE_POINTER_RE.fullmatch(
                candidate["source_pointer"]
            )
            if (
                candidate["lane"] != "micro"
                or candidate["kind"] != "word_topic"
                or candidate["scope"] != "focus_ayah"
                or candidate["trust"] != "trusted"
                or candidate["obligation"] not in WORD_TOPIC_OBLIGATIONS
                or candidate["mandatory"]
                is not (candidate["obligation"] in ("must_integrate", "candidate"))
                or candidate["root_ids"]
                or pointer_match is None
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} violates the word-topic contract"
                )
            word_index = int(pointer_match.group(1))
            if (
                word_index >= len(word_analysis_refs)
                or word_analysis_refs[word_index] is None
                or candidate["anchor_refs"] != [word_analysis_refs[word_index]]
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} has an invalid word-analysis anchor"
                )
            word_pointer = f"/word_analysis/words/{word_index}"
            if not any(
                support["source_type"] == "word_analysis"
                and support["json_pointer"] == word_pointer
                and support["source_local_id"] == candidate["anchor_refs"][0]
                and support["role"] == SUPPORT_ROLE_EVIDENCE
                for support in candidate_supports
            ) or not any(
                support["source_type"] == "word_analysis"
                and support["json_pointer"] == candidate["source_pointer"]
                and support["source_local_id"] == candidate["source_local_id"]
                and support["role"] == SUPPORT_ROLE_EVIDENCE
                for support in candidate_supports
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} lacks its exact word/topic supports"
                )
        elif candidate["source_type"] == "qac_morpheme":
            morpheme = qac_by_pointer.get(candidate["source_pointer"])
            if (
                candidate["lane"] != "micro"
                or candidate["kind"] != "focus_root_occurrence"
                or candidate["scope"] != "focus_ayah"
                or candidate["trust"] != "trusted"
                or candidate["obligation"] != "ledger_only"
                or candidate["mandatory"]
                or candidate["branch_refs"]
                or morpheme is None
                or candidate["source_local_id"] != morpheme["qac_ref"]
                or candidate["anchor_refs"] != [morpheme["qac_word_ref"]]
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} violates the QAC occurrence contract"
                )
            mapped_ids = {
                root_id
                for root_ar, root_ids in root_mappings.items()
                if _canonical_arabic_root(root_ar)
                == _canonical_arabic_root(morpheme.get("root_ar") or "")
                for root_id in root_ids
            }
            if set(candidate["root_ids"]) != mapped_ids or not mapped_ids:
                raise ValidationError(
                    f"Candidate {candidate_id} QAC root ownership is invalid"
                )
            if len(candidate_supports) != 1 or not (
                candidate_supports[0]["source_type"] == "qac_morpheme"
                and candidate_supports[0]["json_pointer"]
                == candidate["source_pointer"]
                and candidate_supports[0]["role"] == SUPPORT_ROLE_OCCURRENCE
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} lacks its exact QAC occurrence support"
                )
        elif candidate["source_type"] == "cross_run_publication":
            pointer_match = CROSS_RUN_SUPPORT_POINTER_RE.fullmatch(
                candidate["source_pointer"]
            )
            if (
                pointer_match is None
                or candidate["lane"] != "global"
                or candidate["kind"] != "published_finding"
                or candidate["scope"] != "cross_run"
                or candidate["trust"] != "trusted"
                or candidate["obligation"] != "optional_review"
                or candidate["mandatory"]
                or candidate["root_ids"]
                or candidate["source_local_id"]
                != f"finding-{int(candidate['source_pointer'].rsplit('/', 1)[1]) + 1}"
                or len(candidate_supports) != 1
                or candidate_supports[0]["source_type"]
                != "cross_run_publication"
                or candidate_supports[0]["source_local_id"]
                != candidate["source_local_id"]
                or candidate_supports[0]["json_pointer"]
                != candidate["source_pointer"]
                or candidate_supports[0]["role"] != SUPPORT_ROLE_EVIDENCE
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} violates the publication contract"
                )
            try:
                publication_payload = json.loads(candidate_supports[0]["text"])
            except (TypeError, json.JSONDecodeError) as exc:
                raise ValidationError(
                    f"Candidate {candidate_id} publication support is not structured JSON"
                ) from exc
            if not isinstance(publication_payload, dict) or set(
                publication_payload
            ) != {"text", "grade", "anchors"}:
                raise ValidationError(
                    f"Candidate {candidate_id} publication support fields drifted"
                )
            if (
                not isinstance(publication_payload.get("text"), str)
                or candidate["title"] != publication_payload["text"]
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} publication title is not source-bound"
                )
            expected_anchors, expected_branches = _validated_publication_anchors(
                publication_payload.get("anchors"),
                ayah_ref=identity["ayah_ref"],
                qac_morphemes=focus_morphemes,
                root_mappings=root_mappings,
                known_branch_refs=focus_refs,
                label=f"candidate {candidate_id} publication anchors",
            )
            if (
                candidate["anchor_refs"] != expected_anchors
                or candidate["branch_refs"] != expected_branches
            ):
                raise ValidationError(
                    f"Candidate {candidate_id} publication anchors are not exact"
                )
        unresolved_citations = _require_list(
            candidate["unresolved_branch_citations"],
            f"candidate {candidate_id} unresolved_branch_citations",
        )
        normalized_unresolved: list[tuple[str, str]] = []
        for citation in unresolved_citations:
            citation = _require_dict(citation, "unresolved branch citation")
            _require_exact_keys(citation, {"citation", "reason"}, "unresolved branch citation")
            if any(
                not isinstance(citation[field], str) or not citation[field]
                for field in ("citation", "reason")
            ):
                raise ValidationError("Unresolved branch citation is invalid")
            normalized_unresolved.append((citation["citation"], citation["reason"]))
        if normalized_unresolved != sorted(set(normalized_unresolved)):
            raise ValidationError(
                f"Candidate {candidate_id} unresolved citations are noncanonical"
            )
        expected_candidate_id = _stable_id(
            "cand",
            {
                "ayah_ref": docket["identity"]["ayah_ref"],
                "lane": candidate["lane"],
                "source_type": candidate["source_type"],
                "source_local_id": candidate["source_local_id"],
                "source_pointer": candidate["source_pointer"],
                "kind": candidate["kind"],
                "title": candidate["title"],
                "mandatory": candidate["mandatory"],
                "obligation": candidate["obligation"],
                "scope": candidate["scope"],
                "trust": candidate["trust"],
                "branch_refs": candidate["branch_refs"],
                "root_ids": candidate["root_ids"],
                "unresolved_branch_citations": candidate[
                    "unresolved_branch_citations"
                ],
                "anchor_refs": candidate["anchor_refs"],
                "support_ids": candidate["support_ids"],
            },
        )
        if candidate_id != expected_candidate_id:
            raise ValidationError(f"Candidate {candidate_id} identity hash mismatch")
        candidate_ids.add(candidate_id)
        branch_refs = set(candidate["branch_refs"])
        if set(candidate["focus_branch_refs"]) != branch_refs & focus_refs:
            raise ValidationError(f"Candidate {candidate_id} focus branch split is wrong")
        if set(candidate["nominated_branch_refs"]) != branch_refs & nominated_refs:
            raise ValidationError(
                f"Candidate {candidate_id} nominated branch split is wrong"
            )
        expected_unresolved = branch_refs - focus_refs - nominated_refs
        if set(candidate["unresolved_branch_refs"]) != expected_unresolved:
            raise ValidationError(
                f"Candidate {candidate_id} unresolved branch split is wrong"
            )
        expected_adjudicable = not expected_unresolved and not candidate[
            "unresolved_branch_citations"
        ]
        if candidate["adjudicable"] is not expected_adjudicable:
            raise ValidationError(f"Candidate {candidate_id} readiness is wrong")
        expected_eligible, expected_ineligibility_reasons = _selection_eligibility(
            candidate, support_by_id
        )
        if (
            candidate["selection_eligible"] is not expected_eligible
            or candidate["selection_ineligibility_reasons"]
            != expected_ineligibility_reasons
        ):
            raise ValidationError(
                f"Candidate {candidate_id} selection eligibility is wrong"
            )
        if candidate["mandatory"] and not candidate["adjudicable"]:
            raise ValidationError(
                f"Mandatory candidate {candidate_id} has unresolved branch evidence"
            )
        if candidate["mandatory"] and not candidate["selection_eligible"]:
            raise ValidationError(
                f"Mandatory candidate {candidate_id} is not selection eligible: "
                f"{candidate['selection_ineligibility_reasons']}"
            )
        if candidate.get("source_type") == "hft" and docket.get(
            "scope", {}
        ).get("hft", {}).get("status") not in (
            "valid_pericope_bound",
            "valid_pericope_legacy",
            "valid_surah_bound",
            "valid_surah_legacy",
        ):
            raise ValidationError("Invalid or quarantined HFT leaked into docket")
    owned_support_ids = {
        support_id
        for candidate in candidates
        for support_id in candidate["support_ids"]
    }
    if owned_support_ids != support_ids:
        raise ValidationError(
            "Docket support registry contains records with no candidate owner: "
            f"{sorted(support_ids - owned_support_ids)}"
        )
    branch_specific_nominated_refs = {
        branch_ref
        for candidate in candidates
        if candidate["trust"] == "trusted"
        for branch_ref in candidate["branch_refs"]
        if any(
            support_id in support_by_id
            and support_by_id[support_id]["role"] == SUPPORT_ROLE_NOMINATION
            and support_by_id[support_id]["trust"] == "trusted"
            and support_by_id[support_id]["citable"] is True
            and branch_ref in support_by_id[support_id]["branch_refs"]
            for support_id in candidate["support_ids"]
        )
    }
    ungrounded_nominated_refs = nominated_refs - branch_specific_nominated_refs
    if ungrounded_nominated_refs:
        raise ValidationError(
            "Nominated branch registry contains refs without exact nomination support: "
            f"{sorted(ungrounded_nominated_refs)}"
        )
    branch_review_grounding_gaps = _branch_review_grounding_gaps(
        ayah_ref=identity["ayah_ref"],
        branch_registry=branch_roots,
        nominated_branch_registry=docket["nominated_branch_registry"],
        candidates=candidates,
        support_registry=supports,
    )
    coverage = _require_dict(docket.get("coverage"), "docket coverage")
    _require_exact_keys(
        coverage,
        {
            "discovered_seed_count",
            "accounted_seed_count",
            "by_disposition",
            "by_source_type",
            "docket_candidate_count",
            "mandatory_candidate_count",
            "optional_candidate_count",
            "selection_eligible_candidate_count",
            "selection_ineligible_candidate_count",
        },
        "docket coverage",
    )
    for field in (
        "discovered_seed_count",
        "accounted_seed_count",
        "docket_candidate_count",
        "mandatory_candidate_count",
        "optional_candidate_count",
        "selection_eligible_candidate_count",
        "selection_ineligible_candidate_count",
    ):
        value = coverage[field]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValidationError(f"Docket coverage {field} must be a nonnegative integer")
    actual_mandatory = sum(1 for item in candidates if item["mandatory"])
    actual_optional = len(candidates) - actual_mandatory
    expected_counts = {
        "docket_candidate_count": len(candidates),
        "mandatory_candidate_count": actual_mandatory,
        "optional_candidate_count": actual_optional,
        "selection_eligible_candidate_count": sum(
            1 for item in candidates if item["selection_eligible"]
        ),
        "selection_ineligible_candidate_count": sum(
            1 for item in candidates if not item["selection_eligible"]
        ),
    }
    for field, expected in expected_counts.items():
        if coverage.get(field) != expected:
            raise ValidationError(f"Docket coverage {field} is inconsistent")
    dispositions = _require_dict(
        coverage.get("by_disposition"), "coverage.by_disposition"
    )
    if set(dispositions) - LEDGER_DISPOSITIONS or any(
        not isinstance(value, int) or isinstance(value, bool) or value <= 0
        for value in dispositions.values()
    ):
        raise ValidationError("Coverage disposition counts are invalid")
    source_type_counts = _require_dict(
        coverage.get("by_source_type"), "coverage.by_source_type"
    )
    if set(source_type_counts) - CANDIDATE_SOURCE_TYPES or any(
        not isinstance(value, int) or isinstance(value, bool) or value <= 0
        for value in source_type_counts.values()
    ):
        raise ValidationError("Coverage source-type counts are invalid")
    if dispositions.get("docket_mandatory", 0) != actual_mandatory:
        raise ValidationError("Mandatory disposition count is inconsistent")
    if dispositions.get("docket_optional", 0) != actual_optional:
        raise ValidationError("Optional disposition count is inconsistent")
    accounted = sum(dispositions.values())
    if coverage.get("accounted_seed_count") != accounted:
        raise ValidationError("Accounted seed total is inconsistent")
    if coverage.get("discovered_seed_count") != accounted:
        raise ValidationError("Discovered seed total is inconsistent")
    if sum(source_type_counts.values()) != accounted:
        raise ValidationError("Source-type seed total is inconsistent")
    gate = _require_dict(docket.get("adjudication_gate"), "adjudication_gate")
    _require_exact_keys(
        gate,
        {
            "ready",
            "mode",
            "branch_coverage_complete",
            "incomplete_branch_coverage_authorized",
            "degraded_reasons",
            "blockers",
            "blocker_counts",
            "warnings",
        },
        "adjudication_gate",
    )
    if not isinstance(gate.get("ready"), bool):
        raise ValidationError("Adjudication gate ready must be boolean")
    if gate.get("mode") not in (
        "blocked",
        "strict_clean",
        "legacy_hft_allowed",
        "without_hft",
        "quarantine_without_hft",
    ):
        raise ValidationError("Adjudication gate mode is invalid")
    blockers = _require_list(gate.get("blockers"), "adjudication_gate.blockers")
    warnings = _require_list(gate.get("warnings"), "adjudication_gate.warnings")
    degraded_reasons = _require_list(
        gate.get("degraded_reasons"), "adjudication_gate.degraded_reasons"
    )
    blocker_counts = _require_dict(
        gate.get("blocker_counts"), "adjudication_gate.blocker_counts"
    )
    if any(
        not isinstance(item, str) or not item
        for item in blockers + warnings + degraded_reasons
    ) or len(degraded_reasons) != len(set(degraded_reasons)):
        raise ValidationError("Adjudication gate messages must be nonempty strings")
    if gate.get("branch_coverage_complete") is not branch_coverage["complete"]:
        raise ValidationError("Adjudication gate branch coverage flag drifted")
    if not isinstance(gate.get("incomplete_branch_coverage_authorized"), bool):
        raise ValidationError("Incomplete branch-coverage authorization must be boolean")
    hft_scope = _require_dict(scope.get("hft"), "scope.hft")
    _require_exact_keys(hft_scope, {"status", "adjudicable", "packet"}, "scope.hft")
    if (
        not isinstance(hft_scope.get("status"), str)
        or not hft_scope["status"]
        or not isinstance(hft_scope.get("adjudicable"), bool)
        or (
            hft_scope["adjudicable"]
            and not isinstance(hft_scope.get("packet"), dict)
        )
        or (not hft_scope["adjudicable"] and hft_scope.get("packet") is not None)
    ):
        raise ValidationError("Docket HFT scope is invalid")
    expected_degraded_reasons: list[str] = []
    if hft_scope.get("status") in ("valid_pericope_bound", "valid_surah_bound"):
        expected_ready_mode = "strict_clean"
    elif hft_scope.get("adjudicable"):
        expected_ready_mode = "legacy_hft_allowed"
        expected_degraded_reasons.append("legacy_unbound_hft")
    elif hft_scope.get("status") == "absent":
        expected_ready_mode = "without_hft"
        expected_degraded_reasons.append("missing_hft")
    else:
        expected_ready_mode = "quarantine_without_hft"
        expected_degraded_reasons.append("quarantined_hft")
    if gaps:
        expected_degraded_reasons.append("incomplete_focus_root_branch_coverage")
    if degraded_reasons != expected_degraded_reasons:
        raise ValidationError("Adjudication gate degraded reasons are inconsistent")
    if gate["ready"] and gate["mode"] != expected_ready_mode:
        raise ValidationError("Ready adjudication gate mode is inconsistent")
    gap_warning_present = any(
        "branch surprise coverage is incomplete" in item for item in warnings
    )
    if bool(gaps) != gap_warning_present:
        raise ValidationError(
            "Missing focus-root dictionaries are not reflected in readiness warnings"
        )
    if any(
        not isinstance(key, str)
        or not isinstance(value, int)
        or isinstance(value, bool)
        or value <= 0
        for key, value in blocker_counts.items()
    ):
        raise ValidationError("Adjudication gate blocker counts are invalid")
    branch_blocker_count = blocker_counts.get("branch_coverage/incomplete", 0)
    if gaps and not gate["incomplete_branch_coverage_authorized"]:
        if gate["ready"] or branch_blocker_count != len(gaps):
            raise ValidationError(
                "Incomplete branch coverage lacks its required adjudication block"
            )
    elif branch_blocker_count:
        raise ValidationError("Branch-coverage blocker is inconsistent")
    expected_focus_grounding_count = sum(
        item["kind"] == "focus_occurrence_missing"
        for item in branch_review_grounding_gaps
    )
    expected_nominated_grounding_count = len(branch_review_grounding_gaps) - (
        expected_focus_grounding_count
    )
    if blocker_counts.get("branch_review/focus_occurrence_missing", 0) != (
        expected_focus_grounding_count
    ):
        raise ValidationError("Focus branch-review grounding blocker is inconsistent")
    if blocker_counts.get("branch_review/nominated_grounding_missing", 0) != (
        expected_nominated_grounding_count
    ):
        raise ValidationError(
            "Nominated branch-review grounding blocker is inconsistent"
        )
    grounding_blocker_present = any(
        item.startswith("branch-review grounding gate failed:")
        for item in blockers
    )
    if bool(branch_review_grounding_gaps) != grounding_blocker_present:
        raise ValidationError(
            "Branch-review grounding gaps are not reflected in gate blockers"
        )
    if branch_review_grounding_gaps and gate["ready"]:
        raise ValidationError("Unsatisfiable branch review cannot be model-ready")
    if gate["ready"] and (gate["mode"] == "blocked" or blockers or blocker_counts):
        raise ValidationError("Ready adjudication gate carries blockers")
    if not gate["ready"] and (gate["mode"] != "blocked" or not blockers):
        raise ValidationError("Blocked adjudication gate lacks blocker detail")
    rules = _require_dict(docket.get("adjudication_rules"), "adjudication_rules")
    _require_exact_keys(
        rules,
        {
            "mandatory_candidates_require_exactly_one_disposition",
            "available_focus_branches_require_exactly_one_review",
            "new_candidates_must_use_registered_branches_and_existing_supports",
            "quarantined_material_visible",
        },
        "adjudication_rules",
    )
    if any(not isinstance(value, bool) for value in rules.values()):
        raise ValidationError("Adjudication rules must be boolean")
    expected_rules = {
        "mandatory_candidates_require_exactly_one_disposition": True,
        "available_focus_branches_require_exactly_one_review": True,
        "new_candidates_must_use_registered_branches_and_existing_supports": True,
        "quarantined_material_visible": False,
    }
    if rules != expected_rules:
        raise ValidationError("Adjudication rules are inconsistent")
    expected_hash = docket.get("identity", {}).get("docket_payload_sha256")
    if expected_hash != _docket_payload_hash(docket):
        raise ValidationError("Docket payload hash mismatch")


def validate_prepared(
    prepared: dict[str, Any],
    docket: dict[str, Any],
    *,
    source_bundle: dict[str, Any],
    source_raw: bytes,
    options: PrepareOptions,
) -> None:
    if not isinstance(source_bundle, dict):
        raise ValidationError("Prepared validation requires a source bundle object")
    if not isinstance(source_raw, bytes):
        raise ValidationError("Prepared validation requires exact source bytes")
    parsed_source = parse_json_object_bytes(source_raw, label="prepared source_raw")
    if canonical_json_bytes(parsed_source) != canonical_json_bytes(source_bundle):
        raise ValidationError("Prepared source_raw does not encode source_bundle")
    if not isinstance(options, PrepareOptions):
        raise ValidationError("Prepared validation requires caller-bound options")
    options.validate()
    validate_docket(docket)
    if prepared.get("schema_version") != PREPARED_SCHEMA:
        raise ValidationError("Unexpected prepared schema_version")
    _require_exact_keys(
        prepared,
        {
            "schema_version",
            "identity",
            "scope_audit",
            "diagnostics",
            "candidate_ledger",
            "source_inventory",
            "coverage",
            "budget",
            "artifacts",
            "readiness",
            "mandatory_candidates_ready",
        },
        "prepared artifact",
    )
    identity = _require_dict(prepared.get("identity"), "prepared identity")
    _require_exact_keys(identity, {"ayah_ref", "source"}, "prepared identity")
    source_identity = _require_dict(identity.get("source"), "prepared source identity")
    _require_exact_keys(
        source_identity,
        {
            "path",
            "raw_sha256",
            "canonical_sha256",
            "schema_version",
            "ayah_ref",
        },
        "prepared source identity",
    )
    if (
        not isinstance(source_identity["path"], str)
        or not source_identity["path"]
        or any(
            not isinstance(source_identity[field], str)
            or not re.fullmatch(r"[0-9a-f]{64}", source_identity[field])
            for field in ("raw_sha256", "canonical_sha256")
        )
        or (
            source_identity["schema_version"] is not None
            and not isinstance(source_identity["schema_version"], str)
        )
    ):
        raise ValidationError("Prepared source identity fields are invalid")
    if identity.get("ayah_ref") != docket.get("identity", {}).get("ayah_ref"):
        raise ValidationError("Prepared and docket ayah identities disagree")
    if source_identity.get("ayah_ref") != identity.get("ayah_ref"):
        raise ValidationError("Prepared source ayah identity disagrees")
    source_hash = source_identity.get("canonical_sha256")
    if source_hash != docket.get("identity", {}).get("source_canonical_sha256"):
        raise ValidationError("Prepared and docket source hashes disagree")
    ayah_ref = prepared["identity"]["ayah_ref"]
    match = REF_RE.fullmatch(ayah_ref)
    if not match:
        raise ValidationError("Prepared ayah identity is invalid")
    surah, ayah = (int(item) for item in match.groups())
    artifacts = _require_dict(prepared.get("artifacts"), "prepared artifacts")
    _require_exact_keys(
        artifacts,
        {"source_bundle", "prepared", "docket", "docket_payload_sha256"},
        "prepared artifacts",
    )
    expected_paths = {
        "source_bundle": f"inputs/source/s{surah:03d}/{surah}_{ayah}.bundle.json",
        "prepared": f"inputs/prepared/s{surah:03d}/{surah}_{ayah}.prepared.json",
        "docket": f"inputs/adjudication/s{surah:03d}/{surah}_{ayah}.docket.json",
    }
    if any(artifacts.get(key) != value for key, value in expected_paths.items()):
        raise ValidationError("Prepared artifact paths disagree with ayah identity")
    if artifacts.get(
        "docket_payload_sha256"
    ) != docket.get("identity", {}).get("docket_payload_sha256"):
        raise ValidationError("Prepared artifact hash does not bind docket")
    budget = _require_dict(prepared.get("budget"), "prepared budget")
    expected_budget = {
        "docket_bytes": len(canonical_json_bytes(docket)),
        "estimated_tokens_chars_div_4": (len(canonical_json_bytes(docket)) + 3) // 4,
        "support_count": len(docket["support_registry"]),
        "branch_count": sum(
            len(root["branches"]) for root in docket["branch_registry"]
        ),
        "nominated_branch_count": len(docket["nominated_branch_registry"]),
    }
    if budget != expected_budget:
        raise ValidationError("Prepared budget does not match docket")
    ledger = _require_list(
        prepared.get("candidate_ledger"), "prepared candidate_ledger"
    )
    recomputed = _accounting(ledger, docket["candidates"])
    if prepared.get("coverage") != recomputed or docket.get("coverage") != recomputed:
        raise ValidationError("Prepared/docket coverage does not match ledger")
    inventory = _require_dict(
        prepared.get("source_inventory"), "prepared source_inventory"
    )
    candidate_source_seed_count = sum(
        item.get("seed_count", 0)
        for item in inventory.values()
        if isinstance(item, dict) and item.get("policy") == "candidate_source"
    )
    if candidate_source_seed_count != len(ledger):
        raise ValidationError("Source inventory seed count does not match ledger")
    diagnostics = _require_dict(prepared.get("diagnostics"), "prepared diagnostics")
    _require_exact_keys(
        diagnostics,
        {
            "quarantined_hft",
            "blocking_seed_failures",
            "focus_root_dictionary_gaps",
            "branch_review_grounding_gaps",
        },
        "prepared diagnostics",
    )
    if diagnostics.get("focus_root_dictionary_gaps") != docket.get("scope", {}).get(
        "branch_coverage", {}
    ).get("missing_dictionary_roots"):
        raise ValidationError("Prepared focus-root dictionary gaps drifted from docket")
    expected_branch_review_gaps = _branch_review_grounding_gaps(
        ayah_ref=docket["identity"]["ayah_ref"],
        branch_registry=docket["branch_registry"],
        nominated_branch_registry=docket["nominated_branch_registry"],
        candidates=docket["candidates"],
        support_registry=docket["support_registry"],
    )
    if diagnostics.get("branch_review_grounding_gaps") != expected_branch_review_gaps:
        raise ValidationError(
            "Prepared branch-review grounding gaps drifted from docket"
        )
    readiness = _require_dict(prepared.get("readiness"), "prepared readiness")
    if readiness != docket.get("adjudication_gate"):
        raise ValidationError("Prepared readiness does not bind docket gate")
    mandatory_candidates_ready = prepared.get("mandatory_candidates_ready")
    if not isinstance(mandatory_candidates_ready, bool):
        raise ValidationError("Prepared mandatory_candidates_ready must be boolean")
    if readiness.get("ready") and not mandatory_candidates_ready:
        raise ValidationError("Prepared readiness exceeds mandatory evidence readiness")
    scope_audit = _require_dict(prepared.get("scope_audit"), "prepared scope_audit")
    _require_exact_keys(
        scope_audit,
        {
            "pericope",
            "hft",
            "hft_policy",
            "allow_legacy_hft_response",
            "allow_incomplete_branch_coverage",
        },
        "prepared scope_audit",
    )
    if scope_audit.get("pericope") != docket.get("scope", {}).get("pericope"):
        raise ValidationError("Prepared pericope audit drifted from docket")
    audited_hft = _require_dict(scope_audit.get("hft"), "prepared scope_audit.hft")
    expected_docket_hft = {
        "status": audited_hft.get("status"),
        "adjudicable": audited_hft.get("adjudicable"),
        "packet": audited_hft.get("packet") if audited_hft.get("adjudicable") else None,
    }
    if docket.get("scope", {}).get("hft") != expected_docket_hft:
        raise ValidationError("Prepared HFT audit drifted from docket")
    if scope_audit.get("hft_policy") not in ("strict", "quarantine"):
        raise ValidationError("Prepared HFT policy is invalid")
    if not isinstance(scope_audit.get("allow_legacy_hft_response"), bool):
        raise ValidationError("Prepared legacy HFT policy is invalid")
    if scope_audit.get("allow_incomplete_branch_coverage") is not readiness.get(
        "incomplete_branch_coverage_authorized"
    ):
        raise ValidationError(
            "Prepared incomplete branch-coverage policy drifted from docket"
        )
    if sha256_bytes(source_raw) != source_identity["raw_sha256"]:
        raise ValidationError("Prepared source raw hash does not bind retained bytes")
    if canonical_sha256(source_bundle) != source_identity["canonical_sha256"]:
        raise ValidationError("Prepared source hash does not bind retained bundle")
    expected_prepared, expected_docket = build_prepared_artifacts(
        source_bundle,
        source_path=Path(source_identity["path"]),
        source_raw=source_raw,
        options=options,
        _validate_result=False,
    )
    if docket != expected_docket:
        raise ValidationError("Docket does not exactly rederive from source")
    if prepared != expected_prepared:
        raise ValidationError(
            "Prepared audit does not exactly rederive from source"
        )


def build_prepared_artifacts(
    bundle: dict[str, Any],
    *,
    source_path: Path,
    source_raw: bytes | None = None,
    options: PrepareOptions | None = None,
    _validate_result: bool = True,
) -> tuple[dict[str, Any], dict[str, Any]]:
    options = options or PrepareOptions()
    options.validate()
    if not isinstance(bundle, dict):
        raise ValidationError("Source bundle must be an object")
    if source_raw is not None:
        parsed_source = parse_json_object_bytes(source_raw, label="source_raw")
        if canonical_json_bytes(parsed_source) != canonical_json_bytes(bundle):
            raise ValidationError("source_raw does not encode the supplied bundle")
    scope = _scope_contract(
        bundle, max_pericope_ayahs=options.max_pericope_ayahs
    )
    _validated_qac_inventory(bundle, ayah_ref=scope["ayah_ref"])
    try:
        hft_audit = _audit_hft(
            bundle,
            scope,
            allow_legacy_response=options.allow_legacy_hft_response,
        )
    except ValidationError as exc:
        hft_audit = {
            "status": "invalid",
            "adjudicable": False,
            "reasons": [f"malformed HFT structure: {exc}"],
            "legacy_response_allowed": options.allow_legacy_hft_response,
            "evidence_scope": "invalid",
            "evidence_lane": None,
            "packet": None,
            "readers": [],
        }
    if hft_audit["adjudicable"]:
        try:
            seed_records = _hft_seed_records(
                _require_dict(
                    bundle.get("v12_focus_trace_hermetic"),
                    "v12_focus_trace_hermetic",
                ),
                allowed_refs=set(hft_audit.get("packet", {}).get("window") or []),
            )
            seed_parse_errors = [
                f"{record['source_local_id']}: {record['parse_error']}"
                for record in seed_records
                if record.get("parse_error")
            ]
            seed_scope_errors = [
                f"{record['source_local_id']}: {record['scope_error']}"
                for record in seed_records
                if record.get("scope_error")
            ]
        except ValidationError as exc:
            seed_parse_errors = [str(exc)]
            seed_scope_errors = []
        if seed_parse_errors or seed_scope_errors:
            reasons: list[str] = []
            if seed_parse_errors:
                reasons.append(
                    "malformed HFT structure: " + "; ".join(seed_parse_errors)
                )
            if seed_scope_errors:
                reasons.append(
                    "HFT seed scope violation: " + "; ".join(seed_scope_errors)
                )
            hft_audit = {
                **hft_audit,
                "status": "invalid",
                "adjudicable": False,
                "reasons": reasons,
            }
    (
        branch_registry,
        known_branch_refs,
        root_mappings,
        focus_root_dictionary_gaps,
    ) = _branch_registry(
        bundle,
        max_bytes_per_root=options.max_branch_bytes_per_root,
    )
    inventory_registry, inventory_root_mappings = _nominatable_branch_inventory(
        bundle
    )
    allowed_hft_branch_refs = known_branch_refs | set(inventory_registry)
    if hft_audit["adjudicable"]:
        seed_records = _hft_seed_records(
            _require_dict(
                bundle.get("v12_focus_trace_hermetic"),
                "v12_focus_trace_hermetic",
            ),
            allowed_refs=set(hft_audit.get("packet", {}).get("window") or []),
            allowed_branch_refs=allowed_hft_branch_refs,
        )
        seed_branch_errors = [
            f"{record['source_local_id']}: {record['branch_error']}"
            for record in seed_records
            if record.get("branch_error")
        ]
        if seed_branch_errors:
            hft_audit = {
                **hft_audit,
                "status": "invalid",
                "adjudicable": False,
                "reasons": [
                    "HFT seed branch violation: " + "; ".join(seed_branch_errors)
                ],
            }
    if (
        hft_audit["status"] != "absent"
        and not hft_audit["adjudicable"]
        and options.hft_policy == "strict"
    ):
        raise ScopeError(
            "HFT scope/identity audit failed: " + "; ".join(hft_audit["reasons"]),
            report=hft_audit,
        )
    resolver_root_mappings = {
        root: sorted(
            set(root_mappings.get(root, []))
            | set(inventory_root_mappings.get(root, []))
        )
        for root in sorted(set(root_mappings) | set(inventory_root_mappings))
    }
    resolver = BranchResolver(
        root_ids_by_arabic=resolver_root_mappings,
        available_branch_refs=known_branch_refs | set(inventory_registry),
        grounding_root_ids_by_arabic=root_mappings,
    )
    supports = SupportBuilder(max_chars=options.max_support_chars)
    candidates: list[dict[str, Any]] = []
    ledger: list[dict[str, Any]] = []

    extracted, entries = _qac_root_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        root_mappings=root_mappings,
        supports=supports,
    )
    candidates.extend(extracted)
    ledger.extend(entries)
    extracted, entries = _word_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        supports=supports,
        resolver=resolver,
    )
    candidates.extend(extracted)
    ledger.extend(entries)
    extracted, entries = _channel_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        supports=supports,
        resolver=resolver,
        allowed_refs=set(scope["pericope"]["refs"]),
        focus_branch_refs=known_branch_refs,
    )
    candidates.extend(extracted)
    ledger.extend(entries)

    quarantined_hft: dict[str, Any] | None = None
    if hft_audit["adjudicable"]:
        extracted, entries = _hft_candidates(
            bundle,
            ayah_ref=scope["ayah_ref"],
            supports=supports,
            audit=hft_audit,
            allowed_branch_refs=allowed_hft_branch_refs,
        )
        candidates.extend(extracted)
        ledger.extend(entries)
    elif hft_audit["status"] != "absent":
        quarantined_hft, entries = _quarantined_hft(
            bundle,
            hft_audit,
            allowed_branch_refs=allowed_hft_branch_refs,
        )
        ledger.extend(entries)

    extracted, entries = _walk_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        supports=supports,
        resolver=resolver,
    )
    candidates.extend(extracted)
    ledger.extend(entries)
    extracted, entries = _publication_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        supports=supports,
        root_mappings=root_mappings,
        known_branch_refs=known_branch_refs,
    )
    candidates.extend(extracted)
    ledger.extend(entries)
    extracted, entries = _legacy_response_candidates(
        bundle,
        ayah_ref=scope["ayah_ref"],
        supports=supports,
        resolver=resolver,
    )
    candidates.extend(extracted)
    ledger.extend(entries)

    candidates = _deduplicate_candidates(candidates, ledger)
    optional_count = sum(1 for candidate in candidates if not candidate["mandatory"])
    if optional_count > options.max_optional_candidates:
        raise BudgetError(
            f"Optional candidate count {optional_count} exceeds limit "
            f"{options.max_optional_candidates}; no candidates were truncated"
        )
    support_registry = supports.values()
    support_map = {item["support_id"]: item for item in support_registry}
    cited_nominated_refs = {
        ref
        for candidate in candidates
        if candidate["trust"] == "trusted"
        for ref in candidate["branch_refs"]
        if any(
            support_id in support_map
            and support_map[support_id]["trust"] == "trusted"
            and support_map[support_id]["citable"]
            and support_map[support_id]["role"] == SUPPORT_ROLE_NOMINATION
            and ref in support_map[support_id]["branch_refs"]
            for support_id in candidate["support_ids"]
        )
        if ref not in known_branch_refs and ref in inventory_registry
    }
    nominated_branch_registry = [
        inventory_registry[ref] for ref in sorted(cited_nominated_refs)
    ]
    all_registered_refs = known_branch_refs | cited_nominated_refs
    for candidate in candidates:
        if len(candidate["support_ids"]) > options.max_support_per_candidate:
            raise BudgetError(
                f"Candidate {candidate['candidate_id']} has "
                f"{len(candidate['support_ids'])} supports; limit is "
                f"{options.max_support_per_candidate}"
            )
        candidate["focus_branch_refs"] = sorted(
            set(candidate["branch_refs"]) & known_branch_refs
        )
        candidate["nominated_branch_refs"] = sorted(
            set(candidate["branch_refs"]) & cited_nominated_refs
        )
        candidate["unresolved_branch_refs"] = sorted(
            set(candidate["branch_refs"]) - all_registered_refs
        )
        candidate["adjudicable"] = not candidate["unresolved_branch_refs"] and not (
            candidate["unresolved_branch_citations"]
        )
        (
            candidate["selection_eligible"],
            candidate["selection_ineligibility_reasons"],
        ) = _selection_eligibility(candidate, support_map)
        if candidate["mandatory"] and not candidate["adjudicable"]:
            raise ValidationError(
                f"Mandatory candidate {candidate['candidate_id']} has unresolved "
                "branch evidence"
            )
        if candidate["mandatory"] and not candidate["selection_eligible"]:
            raise ValidationError(
                f"Mandatory candidate {candidate['candidate_id']} is not selection "
                f"eligible: {candidate['selection_ineligibility_reasons']}"
            )

    branch_review_grounding_gaps = _branch_review_grounding_gaps(
        ayah_ref=scope["ayah_ref"],
        branch_registry=branch_registry,
        nominated_branch_registry=nominated_branch_registry,
        candidates=candidates,
        support_registry=support_registry,
    )

    ledger = sorted(
        ledger,
        key=lambda item: (
            item["source_type"],
            item["source_pointer"],
            item["source_local_id"],
            item["disposition"],
        ),
    )
    accounting = _accounting(ledger, candidates)
    source_inventory = _source_inventory(bundle, ledger)
    blocking_parse_failures = [
        item
        for item in ledger
        if item["source_type"] == "word_analysis"
        and item["disposition"] in ("parse_failed", "out_of_scope")
    ] + [
        item
        for item in ledger
        if item["source_type"] == "hft"
        and hft_audit["adjudicable"]
        and item["disposition"] in ("parse_failed", "out_of_scope")
    ] + [
        item
        for item in ledger
        if item["source_type"] == "channel"
        and item["disposition"] == "parse_failed"
    ]
    mandatory_ready = not blocking_parse_failures and all(
        candidate["support_ids"]
        and candidate["adjudicable"]
        and candidate["selection_eligible"]
        for candidate in candidates
        if candidate["mandatory"]
    )
    blocker_counts: dict[str, int] = {}
    for item in blocking_parse_failures:
        key = f"{item['source_type']}/{item['disposition']}"
        blocker_counts[key] = blocker_counts.get(key, 0) + 1
    blockers: list[str] = []
    if not mandatory_ready:
        if not blocker_counts:
            blocker_counts["mandatory_evidence/unresolved"] = 1
        detail = ", ".join(
            f"{key}={count}" for key, count in sorted(blocker_counts.items())
        )
        blockers.append(f"mandatory evidence gate failed: {detail}")

    focus_grounding_gap_count = sum(
        item["kind"] == "focus_occurrence_missing"
        for item in branch_review_grounding_gaps
    )
    nominated_grounding_gap_count = len(branch_review_grounding_gaps) - (
        focus_grounding_gap_count
    )
    if focus_grounding_gap_count:
        blocker_counts["branch_review/focus_occurrence_missing"] = (
            focus_grounding_gap_count
        )
    if nominated_grounding_gap_count:
        blocker_counts["branch_review/nominated_grounding_missing"] = (
            nominated_grounding_gap_count
        )
    if branch_review_grounding_gaps:
        blockers.append(
            "branch-review grounding gate failed: every focus root and nominated "
            "branch needs admissible candidate-owned evidence"
        )

    branch_coverage_complete = not focus_root_dictionary_gaps
    if (
        not branch_coverage_complete
        and not options.allow_incomplete_branch_coverage
    ):
        blocker_counts["branch_coverage/incomplete"] = len(
            focus_root_dictionary_gaps
        )
        blockers.append(
            "focus-root branch coverage is incomplete; rerun preparation with "
            "explicit incomplete-coverage authorization to continue"
        )

    degraded_reasons: list[str] = []
    warnings: list[str] = []
    if hft_audit["status"] in ("valid_pericope_bound", "valid_surah_bound"):
        clean_readiness_mode = "strict_clean"
    elif hft_audit["adjudicable"]:
        clean_readiness_mode = "legacy_hft_allowed"
        degraded_reasons.append("legacy_unbound_hft")
        warnings.append("HFT response is not bound to its packet identity")
    elif hft_audit["status"] == "absent":
        clean_readiness_mode = "without_hft"
        degraded_reasons.append("missing_hft")
        warnings.append("No HFT evidence is available")
    else:
        clean_readiness_mode = "quarantine_without_hft"
        degraded_reasons.append("quarantined_hft")
        warnings.append("HFT failed trust checks and is excluded from adjudication")
    if focus_root_dictionary_gaps:
        degraded_reasons.append("incomplete_focus_root_branch_coverage")
        labels = ", ".join(
            f"{item['root_id']} ({item['root_ar']})"
            for item in focus_root_dictionary_gaps
        )
        warnings.append(
            "Focus-root branch dictionaries are unavailable for "
            f"{labels}; branch surprise coverage is incomplete"
        )
    ready = (
        mandatory_ready
        and not branch_review_grounding_gaps
        and (
            branch_coverage_complete
            or options.allow_incomplete_branch_coverage
        )
    )
    adjudication_gate = {
        "ready": ready,
        "mode": clean_readiness_mode if ready else "blocked",
        "branch_coverage_complete": branch_coverage_complete,
        "incomplete_branch_coverage_authorized": (
            options.allow_incomplete_branch_coverage
        ),
        "degraded_reasons": degraded_reasons,
        "blockers": blockers,
        "blocker_counts": dict(sorted(blocker_counts.items())),
        "warnings": warnings,
    }
    raw = source_raw if source_raw is not None else canonical_json_bytes(bundle)
    retained_source_path = (
        Path("inputs")
        / "source"
        / f"s{scope['surah']:03d}"
        / f"{scope['surah']}_{scope['ayah']}.bundle.json"
    )
    source_identity = {
        "path": str(retained_source_path),
        "raw_sha256": sha256_bytes(raw),
        "canonical_sha256": canonical_sha256(bundle),
        "schema_version": bundle.get("schema_version"),
        "ayah_ref": scope["ayah_ref"],
    }
    docket = {
        "schema_version": DOCKET_SCHEMA,
        "identity": {
            "ayah_ref": scope["ayah_ref"],
            "source_canonical_sha256": source_identity["canonical_sha256"],
        },
        "scope": {
            "pericope": scope["pericope"],
            "lane_contract": {
                "micro": (
                    "focus ayah morphology, word analysis, and every available "
                    "focus-root branch; unavailable dictionaries are explicit"
                ),
                "macro": "pericope-anchored channels and exactly matching HFT only",
                "global": "reader walks and cross-run publications with explicit trust labels",
            },
            "hft": {
                "status": hft_audit["status"],
                "adjudicable": hft_audit["adjudicable"],
                "packet": hft_audit["packet"] if hft_audit["adjudicable"] else None,
            },
            "branch_coverage": {
                "complete": not focus_root_dictionary_gaps,
                "focus_root_count": len(root_mappings),
                "mapped_root_record_count": len(branch_registry),
                "registered_branch_count": sum(
                    len(root["branches"]) for root in branch_registry
                ),
                "missing_dictionary_roots": focus_root_dictionary_gaps,
            },
        },
        "focus": _focus_packet(bundle, ayah_ref=scope["ayah_ref"]),
        "focus_root_mappings": root_mappings,
        "branch_registry": branch_registry,
        "nominated_branch_registry": nominated_branch_registry,
        "candidates": candidates,
        "support_registry": support_registry,
        "coverage": accounting,
        "adjudication_gate": adjudication_gate,
        "adjudication_rules": {
            "mandatory_candidates_require_exactly_one_disposition": True,
            "available_focus_branches_require_exactly_one_review": True,
            "new_candidates_must_use_registered_branches_and_existing_supports": True,
            "quarantined_material_visible": False,
        },
        "limits": {
            "max_optional_candidates": options.max_optional_candidates,
            "max_support_chars": options.max_support_chars,
            "max_support_per_candidate": options.max_support_per_candidate,
            "max_branch_bytes_per_root": options.max_branch_bytes_per_root,
            "max_pericope_ayahs": options.max_pericope_ayahs,
            "max_docket_bytes": options.max_docket_bytes,
        },
    }
    docket["identity"]["docket_payload_sha256"] = _docket_payload_hash(docket)
    docket_bytes = canonical_json_bytes(docket)
    if len(docket_bytes) > options.max_docket_bytes:
        raise BudgetError(
            f"Docket is {len(docket_bytes)} bytes; limit is "
            f"{options.max_docket_bytes}. Nothing was truncated."
        )
    validate_docket(docket)

    surah = scope["surah"]
    ayah = scope["ayah"]
    prepared_rel = Path("prepared") / f"s{surah:03d}" / f"{surah}_{ayah}.prepared.json"
    source_rel = Path("source") / f"s{surah:03d}" / f"{surah}_{ayah}.bundle.json"
    docket_rel = (
        Path("adjudication") / f"s{surah:03d}" / f"{surah}_{ayah}.docket.json"
    )
    prepared = {
        "schema_version": PREPARED_SCHEMA,
        "identity": {
            "ayah_ref": scope["ayah_ref"],
            "source": source_identity,
        },
        "scope_audit": {
            "pericope": scope["pericope"],
            "hft": hft_audit,
            "hft_policy": options.hft_policy,
            "allow_legacy_hft_response": options.allow_legacy_hft_response,
            "allow_incomplete_branch_coverage": (
                options.allow_incomplete_branch_coverage
            ),
        },
        "diagnostics": {
            "quarantined_hft": quarantined_hft,
            "blocking_seed_failures": blocking_parse_failures,
            "focus_root_dictionary_gaps": focus_root_dictionary_gaps,
            "branch_review_grounding_gaps": branch_review_grounding_gaps,
        },
        "candidate_ledger": ledger,
        "source_inventory": source_inventory,
        "coverage": accounting,
        "budget": {
            "docket_bytes": len(docket_bytes),
            "estimated_tokens_chars_div_4": (len(docket_bytes) + 3) // 4,
            "support_count": len(docket["support_registry"]),
            "branch_count": sum(
                len(root["branches"]) for root in branch_registry
            ),
            "nominated_branch_count": len(nominated_branch_registry),
        },
        "artifacts": {
            "source_bundle": str(Path("inputs") / source_rel),
            "prepared": str(Path("inputs") / prepared_rel),
            "docket": str(Path("inputs") / docket_rel),
            "docket_payload_sha256": docket["identity"][
                "docket_payload_sha256"
            ],
        },
        "readiness": adjudication_gate,
        "mandatory_candidates_ready": mandatory_ready,
    }
    if _validate_result:
        validate_prepared(
            prepared,
            docket,
            source_bundle=bundle,
            source_raw=raw,
            options=options,
        )
    return prepared, docket


def prepare_bundle_file(
    bundle_path: Path,
    *,
    options: PrepareOptions | None = None,
    write: bool = True,
    force: bool = False,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, str]]:
    bundle, raw = load_json_object(bundle_path)
    prepared, docket = build_prepared_artifacts(
        bundle,
        source_path=bundle_path,
        source_raw=raw,
        options=options,
    )
    ayah_ref = prepared["identity"]["ayah_ref"]
    surah, ayah = (int(item) for item in ayah_ref.split(":"))
    source_rel = Path("source") / f"s{surah:03d}" / f"{surah}_{ayah}.bundle.json"
    prepared_rel = Path("prepared") / f"s{surah:03d}" / f"{surah}_{ayah}.prepared.json"
    docket_rel = (
        Path("adjudication") / f"s{surah:03d}" / f"{surah}_{ayah}.docket.json"
    )
    paths = {
        "source_bundle": str(INPUTS_ROOT / source_rel),
        "prepared": str(INPUTS_ROOT / prepared_rel),
        "docket": str(INPUTS_ROOT / docket_rel),
    }
    if write:
        payloads = {
            source_rel: raw,
            docket_rel: pretty_json_bytes(docket),
            prepared_rel: pretty_json_bytes(prepared),
        }
        preflight_confined_writes(INPUTS_ROOT, payloads, replace=force)
        for relative in (source_rel, docket_rel, prepared_rel):
            write_bytes_confined(
                INPUTS_ROOT,
                relative,
                payloads[relative],
                replace=force,
            )
    return prepared, docket, paths
