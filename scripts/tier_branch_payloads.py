#!/usr/bin/env python3
"""Create a Layer-2 bundle with interest-tiered root lexicon branches.

The source bundle is never modified. Every root and every dictionary branch
identity remains present; only the payload carried by dictionary/gloss branch
records is projected. All non-branch bundle evidence is preserved unchanged.

Usage:
    python3 scripts/tier_branch_payloads.py bundles/s012/12_100.ayah.json \
        --output /tmp/12_100.ayah.tiered.json
    python3 scripts/tier_branch_payloads.py bundles/s012/12_100.ayah.json --check
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


POLICY_MODE = "interest_tiered_v1"
TIERS = ("explicit_interest", "local_low_branch_safety", "compact_rest")

TEXT_INTEREST_FIELDS = {
    "reader_walks": "v12_reader_walks",
    "reader_walks_wide": "v12_reader_walks_wide",
    "channel_review_blocks": "channel_subchannels_anchored_here",
    "word_analysis": "word_analysis",
    "inter_ayah": "inter_ayah_rows",
    "butuncul": "butuncul_okuma_line",
}

SOURCE_COVERAGE_KEYS = {
    "word_analysis": "word_analysis",
    "v12_focus_trace_hermetic": "v12_focus_trace_hermetic",
    "v12_reader_walks": "v12_reader_walks",
    "v12_reader_walks_wide": "v12_reader_walks_wide",
    "v12_cross_run_publication": "v12_cross_run_publication",
    "channel_subchannels_anchored_here": "channel_review",
    "inter_ayah_rows": "inter_ayah",
    "butuncul_okuma_line": "butuncul_okuma",
    "branch_inventories": "branch_inventories",
}

BRANCH_ID = r"B\d{3}"
BRANCH_LIST = rf"{BRANCH_ID}(?:\s*/\s*{BRANCH_ID})*"
ROOT_ID_CITATION_RE = re.compile(
    rf"(?:quranic:)?(?P<root_id>root_\d{{6}})\s*[:/]\s*"
    rf"(?P<branches>{BRANCH_LIST})(?:\s*/\s*m\d+)?"
)
ARABIC_ROOT_CITATION_RE = re.compile(
    rf"(?<![\u0621-\u064A])"
    rf"(?P<root>[\u0621-\u064A](?:\s+[\u0621-\u064A]){{2,3}})"
    rf"\s*(?::|\s)\s*(?P<branches>{BRANCH_LIST})"
    rf"(?:\s*/\s*m\d+)?"
)


class TieringError(RuntimeError):
    pass


def normalize_root(value: str) -> str:
    return "".join((value or "").split())


def iter_objects(value: Any) -> Iterable[dict]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_objects(child)


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from iter_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_strings(child)


def split_branch_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split("/") if part.strip()]


def without_none(value: Any) -> Any:
    """Recursively drops None-valued object fields, retaining list positions."""
    if isinstance(value, dict):
        return {
            key: without_none(child)
            for key, child in value.items()
            if child is not None
        }
    if isinstance(value, list):
        return [without_none(child) for child in value]
    return value


@dataclass
class InterestLedger:
    refs_by_source: dict[str, set[str]] = field(
        default_factory=lambda: defaultdict(set)
    )
    mentions_by_source: dict[str, int] = field(
        default_factory=lambda: defaultdict(int)
    )
    ambiguous: list[dict] = field(default_factory=list)
    unresolved: list[dict] = field(default_factory=list)

    def add(self, source: str, root_id: str, branch_id: str, raw_token: str) -> None:
        ref = f"{root_id}/{branch_id}"
        self.refs_by_source[source].add(ref)
        self.mentions_by_source[source] += 1

    @property
    def refs(self) -> set[str]:
        result: set[str] = set()
        for refs in self.refs_by_source.values():
            result.update(refs)
        return result


@dataclass(frozen=True)
class ResolutionMaps:
    branch_refs: set[str]
    root_lexicon_ids: set[str]
    inventory_root_ids: set[str]
    inventory_by_arabic_branch: dict[tuple[str, str], set[str]]
    root_lexicon_by_qac_root: dict[str, set[str]]


def build_resolution_maps(bundle: dict) -> ResolutionMaps:
    root_lexicon = bundle.get("root_lexicon") or {}
    branch_refs: set[str] = set()
    by_qac: dict[str, set[str]] = defaultdict(set)
    for root_id, root in root_lexicon.items():
        for qac_root in root.get("qac_roots_ar", []) or []:
            by_qac[normalize_root(qac_root)].add(root_id)
        dictionary_entry = root.get("dictionary_entry") or {}
        for branch in dictionary_entry.get("branches", []) or []:
            ref = branch.get("branch_ref")
            if not ref:
                raise TieringError(f"dictionary branch under {root_id} has no branch_ref")
            if ref in branch_refs:
                raise TieringError(f"duplicate dictionary branch_ref: {ref}")
            branch_refs.add(ref)

    inventory_by_branch: dict[tuple[str, str], set[str]] = defaultdict(set)
    inventory_ids: set[str] = set()
    packet = (
        (bundle.get("branch_inventories") or {}).get("full_context_packet") or {}
    )
    for inventory in packet.get("branch_inventories", []) or []:
        root_key = normalize_root(inventory.get("root") or "")
        for branch in inventory.get("branches", []) or []:
            branch_id = branch.get("branch_id")
            if not root_key or not branch_id:
                continue
            for variant in branch.get("variants", []) or []:
                root_id = variant.get("root_id")
                if root_id:
                    inventory_by_branch[(root_key, branch_id)].add(root_id)
                    inventory_ids.add(root_id)

    return ResolutionMaps(
        branch_refs=branch_refs,
        root_lexicon_ids=set(root_lexicon),
        inventory_root_ids=inventory_ids,
        inventory_by_arabic_branch=dict(inventory_by_branch),
        root_lexicon_by_qac_root=dict(by_qac),
    )


def validate_source_contract(bundle: dict) -> None:
    """Reject missing fields and present/payload contradictions in one report."""
    errors: list[str] = []
    required_fields = {
        "coverage": dict,
        "root_lexicon": dict,
        "branch_inventories": dict,
        "word_analysis": dict,
        "qac_morphemes": list,
        "word_morpheme_spans": list,
        "v12_focus_trace_hermetic": dict,
        "v12_reader_walks": dict,
        "v12_reader_walks_wide": dict,
        "v12_cross_run_publication": dict,
        "channel_subchannels_anchored_here": list,
        "inter_ayah_rows": list,
        "butuncul_okuma_line": (str, type(None)),
    }
    for field_name, expected_type in required_fields.items():
        if field_name not in bundle:
            errors.append(f"missing required bundle field: {field_name}")
        elif not isinstance(bundle[field_name], expected_type):
            expected = (
                "/".join(t.__name__ for t in expected_type)
                if isinstance(expected_type, tuple)
                else expected_type.__name__
            )
            errors.append(
                f"bundle field {field_name} has type "
                f"{type(bundle[field_name]).__name__}; expected {expected}"
            )

    coverage = bundle.get("coverage")
    if isinstance(coverage, dict):
        for field_name, coverage_key in SOURCE_COVERAGE_KEYS.items():
            source_coverage = coverage.get(coverage_key)
            if not isinstance(source_coverage, dict):
                errors.append(f"missing coverage object: coverage.{coverage_key}")
                continue
            if "present" not in source_coverage:
                errors.append(f"missing presence flag: coverage.{coverage_key}.present")
                continue
            present = source_coverage["present"]
            if not isinstance(present, bool):
                errors.append(
                    f"coverage.{coverage_key}.present must be boolean, got "
                    f"{type(present).__name__}"
                )
                continue
            payload = bundle.get(field_name)
            # Empty anchored channel blocks are valid even when the surah-level
            # review source exists. Other present sources must carry a payload.
            may_be_empty = field_name == "channel_subchannels_anchored_here"
            if present and not payload and not may_be_empty:
                errors.append(
                    f"coverage.{coverage_key}.present is true but {field_name} is empty"
                )
            if not present and payload:
                errors.append(
                    f"coverage.{coverage_key}.present is false but {field_name} has payload"
                )

    word_analysis = bundle.get("word_analysis")
    if isinstance(word_analysis, dict) and not isinstance(word_analysis.get("words"), list):
        errors.append("word_analysis.words is missing or is not an array")

    hft_coverage = (coverage or {}).get("v12_focus_trace_hermetic", {})
    if isinstance(hft_coverage, dict) and not hft_coverage.get("present"):
        errors.append(
            "HFT is explicitly absent; interest-tiered Layer 2 bundles require "
            "coverage.v12_focus_trace_hermetic.present=true"
        )
    hft = bundle.get("v12_focus_trace_hermetic")
    if isinstance(hft, dict) and hft_coverage.get("present"):
        readers = hft.get("readers")
        if not isinstance(readers, dict) or not readers:
            errors.append("v12_focus_trace_hermetic.readers is missing or empty")

    packet = (bundle.get("branch_inventories") or {}).get("full_context_packet")
    if not isinstance(packet, dict):
        errors.append("branch_inventories.full_context_packet is missing")
    elif not isinstance(packet.get("branch_inventories"), list):
        errors.append(
            "branch_inventories.full_context_packet.branch_inventories is missing "
            "or is not an array"
        )

    root_coverage = (coverage or {}).get("root_lexicon")
    if not isinstance(root_coverage, dict):
        errors.append("missing coverage object: coverage.root_lexicon")

    root_lexicon = bundle.get("root_lexicon")
    if isinstance(root_lexicon, dict):
        for root_id, root in root_lexicon.items():
            location = f"root_lexicon.{root_id}"
            if not isinstance(root, dict):
                errors.append(f"{location} is not an object")
                continue
            if root.get("root_id") != root_id:
                errors.append(
                    f"{location}.root_id is {root.get('root_id')!r}; expected {root_id!r}"
                )
            dictionary_entry = root.get("dictionary_entry")
            dictionary_source = root.get("dictionary_source_file")
            if dictionary_entry is None:
                if dictionary_source is not None:
                    errors.append(
                        f"{location}.dictionary_entry is absent but "
                        "dictionary_source_file is set"
                    )
            elif not isinstance(dictionary_entry, dict):
                errors.append(f"{location}.dictionary_entry is not an object or null")
            else:
                if not isinstance(dictionary_source, str) or not dictionary_source:
                    errors.append(
                        f"{location}.dictionary_entry is present but "
                        "dictionary_source_file is missing"
                    )
                branches = dictionary_entry.get("branches")
                if not isinstance(branches, list):
                    errors.append(f"{location}.dictionary_entry.branches is not an array")
                else:
                    for index, branch in enumerate(branches):
                        branch_location = (
                            f"{location}.dictionary_entry.branches[{index}]"
                        )
                        if not isinstance(branch, dict):
                            errors.append(f"{branch_location} is not an object")
                            continue
                        if not isinstance(branch.get("branch_ref"), str):
                            errors.append(f"{branch_location}.branch_ref is missing")

            gloss = root.get("gloss")
            gloss_source = root.get("gloss_source_file")
            if gloss is None:
                if gloss_source is not None:
                    errors.append(
                        f"{location}.gloss is absent but gloss_source_file is set"
                    )
            elif not isinstance(gloss, dict):
                errors.append(f"{location}.gloss is not an object or null")
            else:
                if not isinstance(gloss_source, str) or not gloss_source:
                    errors.append(
                        f"{location}.gloss is present but gloss_source_file is missing"
                    )
                if not isinstance(gloss.get("branches"), list):
                    errors.append(f"{location}.gloss.branches is not an array")

    if errors:
        raise TieringError("source contract failed:\n- " + "\n- ".join(errors))


def collect_structured_hft(bundle: dict, ledger: InterestLedger) -> None:
    for value in iter_objects(bundle.get("v12_focus_trace_hermetic") or {}):
        root_id = value.get("mapped_root_id")
        branch_id = value.get("branch_id")
        if root_id is None and branch_id is None:
            continue
        if not isinstance(root_id, str) or not re.fullmatch(r"root_\d{6}", root_id):
            ledger.unresolved.append({
                "source": "hft_activation_trace",
                "token": repr(value),
                "reason": "invalid_or_missing_mapped_root_id",
            })
            continue
        if not isinstance(branch_id, str) or not re.fullmatch(BRANCH_ID, branch_id):
            ledger.unresolved.append({
                "source": "hft_activation_trace",
                "token": repr(value),
                "reason": "invalid_or_missing_branch_id",
            })
            continue
        if root_id and branch_id:
            ledger.add(
                "hft_activation_trace",
                root_id,
                branch_id,
                f"{root_id}/{branch_id}",
            )


def collect_cross_run_anchors(bundle: dict, ledger: InterestLedger) -> None:
    publication = bundle.get("v12_cross_run_publication") or {}
    if not publication:
        return
    findings = publication.get("findings")
    if not isinstance(findings, list):
        ledger.unresolved.append({
            "source": "cross_run_anchors",
            "token": repr(findings),
            "reason": "missing_or_invalid_findings_array",
        })
        return
    for finding_index, finding in enumerate(findings):
        if not isinstance(finding, dict) or not isinstance(finding.get("anchors"), list):
            ledger.unresolved.append({
                "source": "cross_run_anchors",
                "token": repr(finding),
                "reason": "missing_or_invalid_anchors_array",
                "location": f"findings[{finding_index}]",
            })
            continue
        for anchor_index, anchor in enumerate(finding.get("anchors", []) or []):
            if (
                not isinstance(anchor, list)
                or len(anchor) < 3
                or not isinstance(anchor[1], str)
                or not isinstance(anchor[2], list)
            ):
                ledger.unresolved.append({
                    "source": "cross_run_anchors",
                    "token": repr(anchor),
                    "reason": "malformed_structured_anchor",
                    "location": f"findings[{finding_index}].anchors[{anchor_index}]",
                })
                continue
            root_id = anchor[1]
            if not re.fullmatch(r"root_\d{6}", root_id):
                ledger.unresolved.append({
                    "source": "cross_run_anchors",
                    "token": repr(anchor),
                    "reason": "invalid_structured_root_id",
                    "location": f"findings[{finding_index}].anchors[{anchor_index}]",
                })
                continue
            if not anchor[2]:
                ledger.unresolved.append({
                    "source": "cross_run_anchors",
                    "token": repr(anchor),
                    "reason": "empty_structured_branch_ids",
                    "location": f"findings[{finding_index}].anchors[{anchor_index}]",
                })
                continue
            for branch_id in anchor[2]:
                if isinstance(branch_id, str) and re.fullmatch(BRANCH_ID, branch_id):
                    ledger.add(
                        "cross_run_anchors",
                        root_id,
                        branch_id,
                        f"{root_id}/{branch_id}",
                    )
                else:
                    ledger.unresolved.append({
                        "source": "cross_run_anchors",
                        "token": repr(anchor),
                        "reason": "invalid_structured_branch_id",
                        "location": f"findings[{finding_index}].anchors[{anchor_index}]",
                    })


def resolve_arabic_citation(
    root: str,
    branch_id: str,
    maps: ResolutionMaps,
) -> set[str]:
    root_key = normalize_root(root)
    candidates = set(maps.inventory_by_arabic_branch.get((root_key, branch_id), set()))
    if not candidates:
        candidates = {
            root_id
            for root_id in maps.root_lexicon_by_qac_root.get(root_key, set())
            if f"{root_id}/{branch_id}" in maps.branch_refs
        }
    return candidates


def collect_text_citations(
    source: str,
    value: Any,
    maps: ResolutionMaps,
    ledger: InterestLedger,
) -> None:
    seen: set[tuple[str, str]] = set()
    for text in iter_strings(value):
        for match in ROOT_ID_CITATION_RE.finditer(text):
            root_id = match.group("root_id")
            for branch_id in split_branch_ids(match.group("branches")):
                key = (root_id, branch_id)
                if key in seen:
                    continue
                seen.add(key)
                ledger.add(source, root_id, branch_id, match.group(0))

        for match in ARABIC_ROOT_CITATION_RE.finditer(text):
            root = match.group("root")
            for branch_id in split_branch_ids(match.group("branches")):
                key = (normalize_root(root), branch_id)
                if key in seen:
                    continue
                seen.add(key)
                candidates = resolve_arabic_citation(root, branch_id, maps)
                if not candidates:
                    ledger.unresolved.append({
                        "source": source,
                        "token": match.group(0),
                        "reason": "unresolved_arabic_root_branch",
                    })
                    continue
                if len(candidates) > 1:
                    ledger.ambiguous.append({
                        "source": source,
                        "token": match.group(0),
                        "resolution": "promote_all_candidates",
                        "candidates": sorted(
                            f"{root_id}/{branch_id}" for root_id in candidates
                        ),
                    })
                for root_id in candidates:
                    ledger.add(source, root_id, branch_id, match.group(0))


def collect_branch_interest(bundle: dict) -> tuple[InterestLedger, ResolutionMaps]:
    maps = build_resolution_maps(bundle)
    ledger = InterestLedger()
    collect_structured_hft(bundle, ledger)
    collect_cross_run_anchors(bundle, ledger)
    for source, field_name in TEXT_INTEREST_FIELDS.items():
        collect_text_citations(source, bundle.get(field_name), maps, ledger)
    return ledger, maps


def project_identity(branch: dict) -> dict:
    return without_none({
        "branch_ref": branch.get("branch_ref"),
        "branch_image_ar": branch.get("branch_image_ar"),
        "what_is_ar": branch.get("what_is_ar"),
        "identity_judgment": {
            "status": (branch.get("identity_judgment") or {}).get("status")
        },
    })


def remove_rejected_fields(branch: dict) -> dict:
    """Copy a full branch while removing only explicitly rejected fields."""
    projected = copy.deepcopy(branch)
    projected.pop("what_is_not_ar", None)
    identity = projected.get("identity_judgment")
    if isinstance(identity, dict):
        identity.pop("boundary_note", None)
    return projected


def semantic_fallback(dictionary_branch: dict, reviewed_branch: dict | None) -> str | None:
    """Return the smallest available non-Arabic semantic fallback."""
    candidates = (
        ((reviewed_branch or {}).get("concept_gloss") or {}).get("text"),
        (dictionary_branch.get("concept_gloss") or {}).get("text"),
        (dictionary_branch.get("concept_map") or {}).get("definition"),
    )
    return next(
        (value for value in candidates if isinstance(value, str) and value.strip()),
        None,
    )


def project_gloss_texts(branch: dict) -> dict:
    concept_gloss = branch.get("concept_gloss") or {}
    return without_none({
        "branch_ref": branch.get("branch_ref"),
        "concept_gloss": {"text": concept_gloss.get("text")},
        "contextual_glosses": [
            {"text": gloss.get("text")}
            for gloss in branch.get("contextual_glosses", []) or []
            if gloss.get("text")
        ],
    })


def project_excluded_glosses(branch: dict) -> list[dict]:
    projected = []
    for gloss in branch.get("excluded_glosses", []) or []:
        error = gloss.get("error_profile") or {}
        projected.append(without_none({
            "text": gloss.get("text"),
            "category": gloss.get("category"),
            "error_profile": {
                "fit": error.get("fit"),
                "loses": error.get("loses"),
                "adds": error.get("adds"),
                "collision": error.get("collision"),
            },
        }))
    return projected


def project_dictionary_branch(
    branch: dict,
    tier: str,
    reviewed_branch: dict | None,
) -> dict:
    if tier == "explicit_interest":
        projected = remove_rejected_fields(branch)
        projected["payload_tier"] = tier
        return projected

    projected = project_identity(branch)
    projected["payload_tier"] = tier
    if tier == "local_low_branch_safety":
        projected["lexicalization_scope"] = without_none({
            "branch_kind": (branch.get("lexicalization_scope") or {}).get("branch_kind")
        })
        if reviewed_branch is None:
            projected.update(project_gloss_texts(branch))

    has_arabic_semantics = any(
        isinstance(projected.get(field_name), str)
        and projected[field_name].strip()
        for field_name in ("branch_image_ar", "what_is_ar")
    )
    if not has_arabic_semantics:
        fallback = semantic_fallback(branch, reviewed_branch)
        if fallback is None:
            raise TieringError(
                f"branch {branch.get('branch_ref')} has no branch_image_ar, what_is_ar, "
                "reviewed/dictionary concept_gloss.text, or concept_map.definition"
            )
        projected["semantic_fallback"] = fallback
    return without_none(projected)


def project_reviewed_gloss(branch: dict, tier: str) -> dict:
    if tier == "explicit_interest":
        projected = remove_rejected_fields(branch)
        projected["payload_tier"] = tier
        return projected
    if tier == "local_low_branch_safety":
        projected = project_gloss_texts(branch)
        projected["payload_tier"] = tier
        return without_none(projected)
    return {
        "branch_ref": branch["branch_ref"],
        "payload_tier": tier,
    }


def branch_tier(branch_ref: str, explicit_refs: set[str]) -> str:
    if branch_ref in explicit_refs:
        return "explicit_interest"
    branch_id = branch_ref.rsplit("/", 1)[-1]
    if branch_id in {"B001", "B002"}:
        return "local_low_branch_safety"
    return "compact_rest"


def classify_resolution(ledger: InterestLedger, maps: ResolutionMaps) -> dict:
    resolved = sorted(ref for ref in ledger.refs if ref in maps.branch_refs)
    missing_payload = sorted(
        ref
        for ref in ledger.refs
        if ref not in maps.branch_refs and ref.split("/", 1)[0] in maps.root_lexicon_ids
    )
    inventory_only = sorted(
        ref
        for ref in ledger.refs
        if ref not in maps.branch_refs
        and ref.split("/", 1)[0] not in maps.root_lexicon_ids
        and ref.split("/", 1)[0] in maps.inventory_root_ids
    )
    out_of_scope = sorted(
        ref
        for ref in ledger.refs
        if ref not in maps.branch_refs
        and ref.split("/", 1)[0] not in maps.root_lexicon_ids
        and ref.split("/", 1)[0] not in maps.inventory_root_ids
    )
    return {
        "resolved_to_root_lexicon_count": len(resolved),
        "resolved_inventory_only": inventory_only,
        "out_of_root_lexicon_scope": out_of_scope,
        "missing_dictionary_payload": missing_payload,
        "ambiguous_multi_target": ledger.ambiguous,
        "unresolved_citations": ledger.unresolved,
    }


def source_coverage(bundle: dict, ledger: InterestLedger) -> dict:
    source_fields = {
        "hft_activation_trace": (
            "v12_focus_trace_hermetic",
            "v12_focus_trace_hermetic",
        ),
        "cross_run_anchors": (
            "v12_cross_run_publication",
            "v12_cross_run_publication",
        ),
        "reader_walks": ("v12_reader_walks", "v12_reader_walks"),
        "reader_walks_wide": ("v12_reader_walks_wide", "v12_reader_walks_wide"),
        "channel_review_blocks": (
            "channel_subchannels_anchored_here",
            "channel_review",
        ),
        "word_analysis": ("word_analysis", "word_analysis"),
        "inter_ayah": ("inter_ayah_rows", "inter_ayah"),
        "butuncul": ("butuncul_okuma_line", "butuncul_okuma"),
    }
    declared_coverage = bundle["coverage"]
    return {
        source: {
            "present": declared_coverage[coverage_key]["present"],
            "mentions": ledger.mentions_by_source.get(source, 0),
            "unique_branch_refs": len(ledger.refs_by_source.get(source, set())),
        }
        for source, (_field_name, coverage_key) in source_fields.items()
    }


def tier_bundle(source_bundle: dict) -> tuple[dict, dict]:
    if not isinstance(source_bundle, dict):
        raise TieringError("input JSON must be an object")
    if source_bundle.get("bundle_type") != "ayah":
        raise TieringError("only ayah bundles are supported")
    if not isinstance(source_bundle.get("root_lexicon"), dict):
        raise TieringError("bundle has no root_lexicon object")

    validate_source_contract(source_bundle)
    source_policy = copy.deepcopy(
        source_bundle["coverage"]["root_lexicon"].get("branch_policy")
    )
    if isinstance(source_policy, dict) and source_policy.get("mode") == POLICY_MODE:
        raise TieringError(
            f"bundle already uses {POLICY_MODE}; tier from the full source bundle instead"
        )

    bundle = copy.deepcopy(source_bundle)
    ledger, maps = collect_branch_interest(source_bundle)
    if ledger.unresolved:
        details = "\n- ".join(
            f"{item.get('source')}: {item.get('reason')}: {item.get('token')}"
            for item in ledger.unresolved
        )
        raise TieringError(f"unresolved or malformed branch citations:\n- {details}")
    tier_counts = {tier: 0 for tier in TIERS}
    gloss_counts = {
        "source_total": 0,
        "text_projected": 0,
        "detail_trimmed": 0,
    }

    original_refs = set(maps.branch_refs)
    projected_refs: set[str] = set()
    for root_id, root in bundle["root_lexicon"].items():
        dictionary_entry = root.get("dictionary_entry")
        if not dictionary_entry:
            gloss_branches = ((root.get("gloss") or {}).get("branches") or [])
            if gloss_branches:
                raise TieringError(
                    f"{root_id} has reviewed gloss branches but no dictionary entry"
                )
            continue
        gloss_record = root.get("gloss")
        reviewed_by_ref: dict[str, dict] = {}
        for index, branch in enumerate((gloss_record or {}).get("branches", []) or []):
            if not isinstance(branch, dict):
                raise TieringError(
                    f"{root_id} gloss branch at index {index} is not an object"
                )
            branch_ref = branch.get("branch_ref")
            if not branch_ref:
                raise TieringError(
                    f"{root_id} gloss branch at index {index} has no branch_ref"
                )
            if branch_ref in reviewed_by_ref:
                raise TieringError(f"duplicate reviewed gloss branch_ref: {branch_ref}")
            reviewed_by_ref[branch_ref] = branch
        gloss_counts["source_total"] += len(reviewed_by_ref)

        projected_dictionary = []
        projected_glosses = []
        dictionary_branches = dictionary_entry.get("branches", []) or []
        dictionary_refs = {branch.get("branch_ref") for branch in dictionary_branches}
        gloss_only_refs = sorted(set(reviewed_by_ref) - dictionary_refs)
        if gloss_only_refs:
            raise TieringError(
                f"{root_id} has gloss-only branch refs with no dictionary payload: "
                f"{gloss_only_refs}"
            )
        for branch in dictionary_branches:
            branch_ref = branch.get("branch_ref")
            if not branch_ref:
                raise TieringError(f"dictionary branch under {root_id} has no branch_ref")
            status = (branch.get("identity_judgment") or {}).get("status")
            if not isinstance(status, str) or not status.strip():
                raise TieringError(
                    f"dictionary branch {branch_ref} has no identity_judgment.status"
                )
            tier = branch_tier(branch_ref, ledger.refs)
            tier_counts[tier] += 1
            projected_refs.add(branch_ref)
            reviewed = reviewed_by_ref.get(branch_ref)
            projected = project_dictionary_branch(branch, tier, reviewed)
            semantic_values = (
                projected.get("branch_image_ar"),
                projected.get("what_is_ar"),
                projected.get("semantic_fallback"),
                ((projected.get("concept_gloss") or {}).get("text")),
                ((projected.get("concept_map") or {}).get("definition")),
            )
            if not any(
                isinstance(value, str) and value.strip() for value in semantic_values
            ):
                raise TieringError(
                    f"projected branch {branch_ref} has no non-empty semantic field"
                )
            projected_dictionary.append(projected)
            if reviewed is not None:
                projected_glosses.append(project_reviewed_gloss(reviewed, tier))

        dictionary_entry["branches"] = projected_dictionary
        if gloss_record is not None:
            gloss_record["branches"] = projected_glosses
        gloss_counts["text_projected"] += sum(
            tier != "compact_rest"
            for tier in (
                branch_tier(branch["branch_ref"], ledger.refs)
                for branch in projected_glosses
            )
        )

    gloss_counts["detail_trimmed"] = (
        gloss_counts["source_total"] - gloss_counts["text_projected"]
    )
    if original_refs != projected_refs:
        missing = sorted(original_refs - projected_refs)
        added = sorted(projected_refs - original_refs)
        raise TieringError(
            f"branch identity invariant failed; missing={missing}, added={added}"
        )

    coverage = bundle.setdefault("coverage", {}).setdefault("root_lexicon", {})
    coverage["branch_policy"] = {
        "mode": POLICY_MODE,
        "source_policy": source_policy,
        "sources": source_coverage(source_bundle, ledger),
        "dictionary_branches_total": len(original_refs),
        "dictionary_branches_kept": len(projected_refs),
        "dictionary_branches_dropped": 0,
        "counts_by_tier": tier_counts,
        "reviewed_gloss_branches": gloss_counts,
        "resolution": classify_resolution(ledger, maps),
        "tier_contracts": {
            "explicit_interest": (
                "Full source branch payload, except fields removed from all tiers."
            ),
            "local_low_branch_safety": (
                "branch_ref, payload_tier, branch_image_ar, what_is_ar, status, "
                "branch_kind, and reviewed/dictionary concept/context gloss text."
            ),
            "compact_rest": (
                "branch_ref, payload_tier, branch_image_ar, what_is_ar, status; "
                "a semantic fallback is added only when both Arabic fields are empty."
            ),
        },
        "removed_from_all_branch_tiers": [
            "what_is_not_ar",
            "identity_judgment.boundary_note",
        ],
        "compact_gloss_policy": (
            "Reviewed gloss branches remain as branch_ref/payload_tier stubs; "
            "their branch records are trimmed, not filtered out."
        ),
        "note": (
            "Every root target and dictionary branch identity is retained. "
            "Branch payload detail is tiered from generation-time citations; "
            "non-full branches and reviewed gloss records are trimmed, not absent. "
            "Root lexicon and branch inventory availability never create interest."
        ),
    }
    return bundle, coverage["branch_policy"]


def compact_size(value: Any) -> int:
    return len(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="source ayah bundle JSON")
    output = parser.add_mutually_exclusive_group(required=True)
    output.add_argument("--output", type=Path, help="write the tiered bundle here")
    output.add_argument(
        "--check",
        action="store_true",
        help="validate and report projected size without writing",
    )
    parser.add_argument(
        "--compact-output",
        action="store_true",
        help="write compact JSON instead of review-friendly indented JSON",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing output file; never permits replacing the input",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    input_path = args.input.resolve()
    if not input_path.is_file():
        raise SystemExit(f"error: input bundle does not exist: {args.input}")
    source = json.loads(input_path.read_text(encoding="utf-8"))
    tiered, policy = tier_bundle(source)

    source_bytes = compact_size(source)
    tiered_bytes = compact_size(tiered)
    reduction = source_bytes - tiered_bytes
    percent = (100 * reduction / source_bytes) if source_bytes else 0.0
    report = {
        "ayahRef": source.get("ayahRef"),
        "policy": policy["mode"],
        "source_compact_bytes": source_bytes,
        "tiered_compact_bytes": tiered_bytes,
        "reduction_bytes": reduction,
        "reduction_percent": round(percent, 2),
        "counts_by_tier": policy["counts_by_tier"],
    }

    if args.output:
        output_path = args.output.resolve()
        if output_path == input_path:
            raise SystemExit("error: refusing to overwrite the source bundle")
        if output_path.exists() and not args.force:
            raise SystemExit(f"error: output exists; pass --force to replace: {args.output}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if args.compact_output:
            text = json.dumps(tiered, ensure_ascii=False, separators=(",", ":")) + "\n"
        else:
            text = json.dumps(tiered, ensure_ascii=False, indent=2) + "\n"
        output_path.write_text(text, encoding="utf-8")
        report["output"] = str(output_path)

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, json.JSONDecodeError, TieringError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
