"""Lossless evidence stores and deterministic discovery packets."""

from __future__ import annotations

import copy
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .common import (
    BudgetError,
    ScopeError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    json_pointer_escape,
    parse_json_object_bytes,
    sha256_bytes,
)


CONTEXT_SCHEMA = "commentary-v3-discovery-context-v1"
STORE_SCHEMA = "commentary-v3-discovery-store-v1"
RECORD_SCHEMA = "commentary-v3-evidence-record-v1"
ATOM_SCHEMA = "commentary-v3-evidence-atom-v1"
PACKET_SCHEMA = "commentary-v3-discovery-packet-v1"
PACKET_SET_SCHEMA = "commentary-v3-discovery-packet-set-v1"
REHYDRATION_REQUEST_SCHEMA = "commentary-v3-rehydration-request-v1"
REHYDRATION_RESPONSE_SCHEMA = "commentary-v3-rehydration-response-v1"
LANES = ("micro", "macro", "global")
AYAH_REF_RE = re.compile(r"^([1-9][0-9]*):([1-9][0-9]*)$")
WORD_REF_RE = re.compile(
    r"^([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*)$"
)
QAC_REF_RE = re.compile(
    r"^([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*):([1-9][0-9]*)$"
)
BRANCH_REF_RE = re.compile(r"^root_[0-9]+/B[0-9]+$")
MAX_PERICOPE_AYAHS = 512
ROOT_GAP_STATUSES = {"no_frozen_rooted_surface_match"}

MICRO_EXACT_FIELDS = (
    "text",
    "qac_morphemes",
    "word_analysis",
    "word_morpheme_spans",
)
MACRO_EXACT_FIELDS = MICRO_EXACT_FIELDS
GLOBAL_HYPOTHESIS_FIELDS = (
    "butuncul_okuma_line",
    "v12_focus_trace_hermetic",
    "v12_reader_walks",
    "v12_reader_walks_wide",
    "v12_cross_run_publication",
    "v12_reader_responses",
)


@dataclass(frozen=True)
class DiscoveryOptions:
    max_record_bytes: int = 4_000_000
    max_packet_bytes: int = 4_000_000
    max_store_bytes: int = 64_000_000

    def validate(self) -> None:
        for name in ("max_record_bytes", "max_packet_bytes", "max_store_bytes"):
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValidationError(f"{name} must be a positive integer")


PACKET_CONTRACT = {
    "atomic_dispositions_required": True,
    "branch_neutral_findings_allowed": True,
    "hypotheses_are_not_evidence": True,
    "rehydration_requests_allowed": True,
}


def _dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def _list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    return value


def _ayah_ref(value: Any, label: str) -> tuple[int, int, str]:
    if not isinstance(value, str) or not (match := AYAH_REF_RE.fullmatch(value)):
        raise ValidationError(f"{label} must be a canonical ayah ref")
    surah = int(match.group(1))
    ayah = int(match.group(2))
    canonical = f"{surah}:{ayah}"
    if canonical != value:
        raise ValidationError(f"{label} must be unpadded")
    return surah, ayah, canonical


def _canonical_anchor_ref(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"{label} must be a canonical typed ref")
    match = QAC_REF_RE.fullmatch(value) or WORD_REF_RE.fullmatch(value)
    if match is None:
        _surah, _ayah, canonical = _ayah_ref(value, label)
        return canonical
    canonical = ":".join(str(int(part)) for part in match.groups())
    if value != canonical:
        raise ValidationError(f"{label} must be unpadded")
    return canonical


def _json_pointer_get(value: Any, pointer: str, *, label: str) -> Any:
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise ValidationError(f"{label} is not an RFC 6901 JSON pointer")
    current = value
    if not pointer:
        return current
    for raw_token in pointer[1:].split("/"):
        if re.search(r"~(?:[^01]|$)", raw_token):
            raise ValidationError(f"{label} contains an invalid escape")
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict):
            if token not in current:
                raise ValidationError(f"{label} does not resolve")
            current = current[token]
        elif isinstance(current, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", token):
                raise ValidationError(f"{label} has an invalid array index")
            index = int(token)
            if index >= len(current):
                raise ValidationError(f"{label} does not resolve")
            current = current[index]
        else:
            raise ValidationError(f"{label} traverses a scalar")
    return current


def _source_snapshot_from_parsed(
    parsed: dict[str, Any], *, raw: bytes, source_path: str
) -> dict[str, Any]:
    surah, ayah, ayah_ref = _ayah_ref(parsed.get("ayahRef"), "source ayahRef")
    if parsed.get("surah") != surah or parsed.get("ayah") != ayah:
        raise ValidationError("Source surah/ayah fields disagree with ayahRef")
    if not isinstance(source_path, str) or not source_path:
        raise ValidationError("Source path must be nonempty")
    return {
        "ayah_ref": ayah_ref,
        "surah": surah,
        "ayah": ayah,
        "source_path": source_path,
        "raw_sha256": sha256_bytes(raw),
        "canonical_sha256": canonical_sha256(parsed),
        "raw_bytes": len(raw),
        "raw": raw,
        "bundle": copy.deepcopy(parsed),
    }


def _source_binding(
    source: dict[str, Any], pointer: str
) -> dict[str, Any]:
    return {
        "ayah_ref": source["ayah_ref"],
        "source_raw_sha256": source["raw_sha256"],
        "source_canonical_sha256": source["canonical_sha256"],
        "json_pointer": pointer,
    }


def source_snapshot(
    bundle: dict[str, Any], *, raw: bytes, source_path: Path
) -> dict[str, Any]:
    bundle = _dict(bundle, "source bundle")
    if not isinstance(raw, bytes):
        raise ValidationError("Source raw payload must be bytes")
    parsed = parse_json_object_bytes(raw, label=str(source_path))
    if canonical_json_bytes(parsed) != canonical_json_bytes(bundle):
        raise ValidationError("Parsed raw source does not equal supplied bundle")
    return _source_snapshot_from_parsed(
        parsed, raw=raw, source_path=str(source_path)
    )


def _validate_source_snapshot(source: dict[str, Any]) -> None:
    source = _dict(source, "source snapshot")
    raw = source.get("raw")
    if not isinstance(raw, bytes):
        raise ValidationError("Source snapshot must retain exact raw bytes")
    parsed = parse_json_object_bytes(raw, label=str(source.get("source_path")))
    expected = _source_snapshot_from_parsed(
        parsed,
        raw=raw,
        source_path=source.get("source_path"),
    )
    if set(source) != set(expected) or source["raw"] != expected["raw"]:
        raise ValidationError("Source snapshot does not rederive from retained raw bytes")
    json_keys = sorted(set(expected) - {"raw"})
    if canonical_json_bytes({key: source[key] for key in json_keys}) != canonical_json_bytes(
        {key: expected[key] for key in json_keys}
    ):
        raise ValidationError("Source snapshot does not rederive from retained raw bytes")


def _ordered_sources(sources: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    materialized = list(sources)
    for source in materialized:
        _validate_source_snapshot(source)
    ordered = sorted(materialized, key=lambda item: (item["surah"], item["ayah"]))
    refs = [source["ayah_ref"] for source in ordered]
    if len(refs) != len(set(refs)):
        raise ValidationError("Discovery sources contain duplicate ayah refs")
    return ordered


def _pericope_scope(source: dict[str, Any]) -> dict[str, Any]:
    pericope = _dict(source["bundle"].get("pericope"), "source pericope")
    required = ("surah", "pericope", "ayah_from", "ayah_to", "label")
    if any(field not in pericope for field in required):
        raise ValidationError("Source pericope metadata is incomplete")
    for field in ("surah", "pericope", "ayah_from", "ayah_to"):
        if (
            not isinstance(pericope[field], int)
            or isinstance(pericope[field], bool)
            or pericope[field] <= 0
        ):
            raise ValidationError(f"Pericope {field} must be a positive integer")
    if pericope["surah"] != source["surah"]:
        raise ValidationError("Pericope surah disagrees with source")
    if pericope["ayah_from"] > pericope["ayah_to"]:
        raise ValidationError("Pericope interval is reversed")
    width = pericope["ayah_to"] - pericope["ayah_from"] + 1
    if width > MAX_PERICOPE_AYAHS:
        raise ScopeError(
            f"Pericope spans {width} ayahs; hard limit is {MAX_PERICOPE_AYAHS}"
        )
    if not isinstance(pericope["label"], str) or not pericope["label"].strip():
        raise ValidationError("Pericope label must be nonempty")
    refs = [
        f"{source['surah']}:{ayah}"
        for ayah in range(pericope["ayah_from"], pericope["ayah_to"] + 1)
    ]
    return {
        "id": (
            f"s{source['surah']:03d}-p{pericope['pericope']:02d}-"
            f"{pericope['ayah_from']:03d}-{pericope['ayah_to']:03d}"
        ),
        "surah": source["surah"],
        "number": pericope["pericope"],
        "ayah_from": pericope["ayah_from"],
        "ayah_to": pericope["ayah_to"],
        "label": pericope["label"],
        "refs": refs,
    }


def build_context_manifest(
    sources: Iterable[dict[str, Any]], *, focus_ayah_ref: str
) -> dict[str, Any]:
    ordered = _ordered_sources(sources)
    if not ordered:
        raise ValidationError("Discovery context requires source snapshots")
    _surah, _ayah, focus_ayah_ref = _ayah_ref(
        focus_ayah_ref, "context focus ayah"
    )
    scopes = [_pericope_scope(source) for source in ordered]
    first_scope = scopes[0]
    if any(scope != first_scope for scope in scopes[1:]):
        raise ValidationError("Context sources do not share one exact pericope")
    source_refs = [source["ayah_ref"] for source in ordered]
    if source_refs != first_scope["refs"]:
        missing = sorted(set(first_scope["refs"]) - set(source_refs))
        extra = sorted(set(source_refs) - set(first_scope["refs"]))
        raise ValidationError(
            f"Context sources do not exactly cover pericope; missing={missing}, extra={extra}"
        )
    if focus_ayah_ref not in source_refs:
        raise ValidationError("Context focus ayah is outside source pericope")
    manifest = {
        "schema_version": CONTEXT_SCHEMA,
        "identity": {
            "focus_ayah_ref": focus_ayah_ref,
            "pericope_id": first_scope["id"],
        },
        "scope": first_scope,
        "sources": [
            {
                key: source[key]
                for key in (
                    "ayah_ref",
                    "source_path",
                    "raw_sha256",
                    "canonical_sha256",
                    "raw_bytes",
                )
            }
            for source in ordered
        ],
    }
    manifest["identity"]["source_set_sha256"] = canonical_sha256(
        manifest["sources"]
    )
    manifest["identity"]["context_payload_sha256"] = canonical_sha256(manifest)
    return manifest


def validate_context_manifest(
    manifest: dict[str, Any], sources: Iterable[dict[str, Any]]
) -> None:
    identity = _dict(manifest.get("identity"), "context identity")
    payload = copy.deepcopy(manifest)
    claimed = _dict(payload.get("identity"), "context identity").pop(
        "context_payload_sha256", None
    )
    if manifest.get("schema_version") != CONTEXT_SCHEMA:
        raise ValidationError("Unexpected discovery context schema")
    if not isinstance(claimed, str) or claimed != canonical_sha256(payload):
        raise ValidationError("Discovery context payload hash is invalid")
    rebuilt = build_context_manifest(
        sources, focus_ayah_ref=identity.get("focus_ayah_ref")
    )
    if canonical_json_bytes(rebuilt) != canonical_json_bytes(manifest):
        raise ValidationError("Discovery context does not rederive from sources")


def _validate_bundle_shape(source: dict[str, Any]) -> None:
    bundle = _dict(source.get("bundle"), "source bundle")
    text = _dict(bundle.get("text"), "text")
    if not text:
        raise ValidationError("text must not be empty")

    qac = _list(bundle.get("qac_morphemes"), "qac_morphemes")
    if not qac:
        raise ValidationError("qac_morphemes must not be empty")
    seen_qac_refs: set[str] = set()
    for index, raw_row in enumerate(qac):
        row = _dict(raw_row, f"qac_morphemes[{index}]")
        for field in (
            "qac_ref",
            "qac_word_ref",
            "surface_ar",
            "lemma_ar",
            "root_ar",
            "pos",
            "morpheme_role",
            "morph_features",
        ):
            if not isinstance(row.get(field), str):
                raise ValidationError(
                    f"qac_morphemes[{index}].{field} must be a string"
                )
        qac_ref = _canonical_anchor_ref(
            row["qac_ref"], f"qac_morphemes[{index}].qac_ref"
        )
        word_ref = _canonical_anchor_ref(
            row["qac_word_ref"], f"qac_morphemes[{index}].qac_word_ref"
        )
        if not QAC_REF_RE.fullmatch(qac_ref) or not WORD_REF_RE.fullmatch(word_ref):
            raise ValidationError("QAC row refs use the wrong typed form")
        if ":".join(qac_ref.split(":")[:3]) != word_ref:
            raise ValidationError("QAC morpheme ref disagrees with its QAC word ref")
        if not qac_ref.startswith(f"{source['ayah_ref']}:") or not word_ref.startswith(
            f"{source['ayah_ref']}:"
        ):
            raise ValidationError("QAC row refs disagree with source ayah")
        if qac_ref in seen_qac_refs:
            raise ValidationError("qac_morphemes contains duplicate qac_ref values")
        seen_qac_refs.add(qac_ref)

    analysis = _dict(bundle.get("word_analysis"), "word_analysis")
    words = _list(analysis.get("words"), "word_analysis.words")
    if not words:
        raise ValidationError("word_analysis.words must not be empty")
    for index, raw_word in enumerate(words):
        word = _dict(raw_word, f"word_analysis.words[{index}]")
        word_ref = _canonical_anchor_ref(
            word.get("aligned_qac_word_ref"),
            f"word_analysis.words[{index}].aligned_qac_word_ref",
        )
        if not WORD_REF_RE.fullmatch(word_ref) or not word_ref.startswith(
            f"{source['ayah_ref']}:"
        ):
            raise ValidationError("Word-analysis ref disagrees with source ayah")
        if "topics" in word:
            topics = _list(word["topics"], f"word_analysis.words[{index}].topics")
            for topic_index, topic in enumerate(topics):
                _dict(topic, f"word_analysis.words[{index}].topics[{topic_index}]")

    qac_by_ref = {row["qac_ref"]: row for row in qac}
    qac_position = {row["qac_ref"]: index for index, row in enumerate(qac)}
    spans = _list(bundle.get("word_morpheme_spans"), "word_morpheme_spans")
    if len(spans) != len(words):
        raise ValidationError("word_morpheme_spans must align one-for-one with words")
    expected_span_fields = {
        "word_index",
        "surface_ar",
        "word_ids",
        "qac_refs",
        "morpheme_ids",
        "aligned_qac_word_ref_upstream",
        "morpheme_skip_count",
    }
    seen_span_qac_refs: set[str] = set()
    for index, raw_span in enumerate(spans):
        if raw_span is None:
            continue
        span = _dict(raw_span, f"word_morpheme_spans[{index}]")
        if set(span) != expected_span_fields:
            raise ValidationError(f"word_morpheme_spans[{index}] has invalid fields")
        if type(span.get("word_index")) is not int or span["word_index"] != index:
            raise ValidationError(
                f"word_morpheme_spans[{index}] has an invalid word index"
            )
        if not isinstance(span.get("surface_ar"), str) or not span["surface_ar"]:
            raise ValidationError(
                f"word_morpheme_spans[{index}] has an invalid surface"
            )
        word_ids = _list(
            span.get("word_ids"), f"word_morpheme_spans[{index}].word_ids"
        )
        refs = _list(span.get("qac_refs"), f"word_morpheme_spans[{index}].qac_refs")
        morpheme_ids = _list(
            span.get("morpheme_ids"),
            f"word_morpheme_spans[{index}].morpheme_ids",
        )
        if not refs or any(not isinstance(ref, str) for ref in refs):
            raise ValidationError("word_morpheme_spans qac refs must be strings")
        if (
            not word_ids
            or any(not isinstance(item, str) or not item for item in word_ids)
            or len(word_ids) != len(set(word_ids))
            or len(refs) != len(set(refs))
            or seen_span_qac_refs.intersection(refs)
            or len(morpheme_ids) != len(refs)
            or any(not isinstance(item, str) or not item for item in morpheme_ids)
            or len(morpheme_ids) != len(set(morpheme_ids))
        ):
            raise ValidationError(
                f"word_morpheme_spans[{index}] has invalid or reused QAC lineage"
            )
        for ref in refs:
            canonical = _canonical_anchor_ref(
                ref, f"word_morpheme_spans[{index}].qac_refs"
            )
            if not QAC_REF_RE.fullmatch(canonical) or canonical not in seen_qac_refs:
                raise ValidationError("word_morpheme_spans cites an unknown QAC ref")
        substantive_word_refs = {
            qac_by_ref[ref]["qac_word_ref"]
            for ref in refs
            if any(
                qac_by_ref[ref][field]
                for field in ("surface_ar", "lemma_ar", "root_ar")
            )
        }
        if (
            len(substantive_word_refs) != 1
            or [qac_position[ref] for ref in refs]
            != sorted(qac_position[ref] for ref in refs)
        ):
            raise ValidationError(
                f"word_morpheme_spans[{index}] crosses substantive QAC words or reorders refs"
            )
        upstream_ref = span.get("aligned_qac_word_ref_upstream")
        if (
            not isinstance(upstream_ref, str)
            or upstream_ref != words[index].get("aligned_qac_word_ref")
        ):
            raise ValidationError(
                f"word_morpheme_spans[{index}] disagrees with its word-analysis row"
            )
        skip_count = span.get("morpheme_skip_count")
        if type(skip_count) is not int or skip_count < 0:
            raise ValidationError(
                f"word_morpheme_spans[{index}] has an invalid skip count"
            )
        seen_span_qac_refs.update(refs)

    pericope_refs = set(_pericope_scope(source)["refs"])
    for field in ("channel_subchannels_anchored_here", "inter_ayah_rows"):
        if field not in bundle:
            continue
        values = _list(bundle[field], field)
        for index, value in enumerate(values):
            item = _dict(value, f"{field}[{index}]")
            if field == "channel_subchannels_anchored_here":
                refs = _list(item.get("ayah_refs"), f"{field}[{index}].ayah_refs")
                if not refs or len(refs) != len(set(refs)):
                    raise ValidationError(f"{field}[{index}].ayah_refs is empty or duplicated")
                canonical_refs = [
                    _ayah_ref(ref, f"{field}[{index}].ayah_refs")[2] for ref in refs
                ]
                if (
                    any(ref not in pericope_refs for ref in canonical_refs)
                    or source["ayah_ref"] not in canonical_refs
                ):
                    raise ValidationError(
                        f"{field}[{index}].ayah_refs is outside its pericope anchor scope"
                    )
            else:
                _ayah_ref(item.get("ref"), f"{field}[{index}].ref")
    if "branch_inventories" in bundle:
        _dict(bundle["branch_inventories"], "branch_inventories")
    _root_entries(bundle)
    _validate_qac_root_coverage(source)


def _mapped_root_values(payload: dict[str, Any], *, label: str) -> set[str]:
    root_ar = payload.get("root_ar")
    if not isinstance(root_ar, str) or not root_ar:
        raise ValidationError(f"{label}.root_ar must be a nonempty string")
    qac_roots = _list(payload.get("qac_roots_ar"), f"{label}.qac_roots_ar")
    if not qac_roots or any(not isinstance(item, str) or not item for item in qac_roots):
        raise ValidationError(f"{label}.qac_roots_ar contains invalid values")
    if len(qac_roots) != len(set(qac_roots)):
        raise ValidationError(f"{label}.qac_roots_ar contains duplicates")
    return {root_ar, *qac_roots}


def _validate_qac_root_coverage(source: dict[str, Any]) -> None:
    roots = {
        row["root_ar"]
        for row in _list(source["bundle"]["qac_morphemes"], "qac_morphemes")
        if row["root_ar"]
    }
    mapped: set[str] = set()
    for root_id, payload, _pointer in _root_entries(source["bundle"]):
        mapped.update(_mapped_root_values(payload, label=root_id))
        _branch_items(payload)
    missing = sorted(roots - mapped)
    unresolved = _root_grounding_gaps(source)
    unrecorded = sorted(set(missing) - set(unresolved))
    if unrecorded:
        raise ValidationError(
            f"QAC roots lack exact root records or grounding gaps: {unrecorded}"
        )
    unexpected = sorted(set(unresolved) - set(missing))
    if unexpected:
        raise ValidationError(
            f"Root grounding gaps conflict with available root records: {unexpected}"
        )


def _root_grounding_gaps(source: dict[str, Any]) -> dict[str, tuple[dict[str, Any], str]]:
    coverage = source["bundle"].get("coverage")
    if not isinstance(coverage, dict):
        return {}
    root_coverage = coverage.get("root_lexicon")
    if not isinstance(root_coverage, dict):
        return {}
    per_root = root_coverage.get("per_root")
    if not isinstance(per_root, dict):
        return {}
    gaps: dict[str, tuple[dict[str, Any], str]] = {}
    for root_ar, raw_entry in sorted(per_root.items()):
        if not isinstance(root_ar, str) or not isinstance(raw_entry, dict):
            raise ValidationError("coverage.root_lexicon.per_root is malformed")
        root_ids = raw_entry.get("root_ids")
        if root_ids != [] or raw_entry.get("root_id") is not None:
            continue
        mapping = _dict(raw_entry.get("root_mapping"), f"root gap {root_ar}.root_mapping")
        status = mapping.get("mapping_status")
        if status not in ROOT_GAP_STATUSES or raw_entry.get("dictionary_present") is not False:
            raise ValidationError(f"Root grounding gap {root_ar} is not explicit")
        pointer = f"/coverage/root_lexicon/per_root/{json_pointer_escape(root_ar)}"
        gaps[root_ar] = (raw_entry, pointer)
    return gaps


def _add_root_gap_records(
    records: list[dict[str, Any]],
    *,
    source: dict[str, Any],
    lane: str,
    options: DiscoveryOptions,
) -> None:
    mapped: set[str] = set()
    for root_id, payload, _pointer in _root_entries(source["bundle"]):
        mapped.update(_mapped_root_values(payload, label=root_id))
    qac_roots = {
        row["root_ar"] for row in source["bundle"]["qac_morphemes"] if row["root_ar"]
    }
    for root_ar in sorted(qac_roots - mapped):
        payload, pointer = _root_grounding_gaps(source)[root_ar]
        records.append(
            _record(
                lane=lane,
                role="root_grounding_gap",
                payload=payload,
                source_bindings=[_source_binding(source, pointer)],
                citable=False,
                hypothesis=False,
                options=options,
            )
        )


def _root_entries(bundle: dict[str, Any]) -> list[tuple[str, dict[str, Any], str]]:
    root_lexicon = bundle.get("root_lexicon")
    entries: list[tuple[str, dict[str, Any], str]] = []
    if isinstance(root_lexicon, dict):
        raw_items = [
            (str(key), value, f"/root_lexicon/{json_pointer_escape(str(key))}")
            for key, value in sorted(root_lexicon.items())
        ]
    elif isinstance(root_lexicon, list):
        raw_items = [
            (str(index), value, f"/root_lexicon/{index}")
            for index, value in enumerate(root_lexicon)
        ]
    else:
        raise ValidationError("root_lexicon must be an object or array")
    for key, raw, pointer in raw_items:
        root = _dict(raw, f"root_lexicon {key}")
        root_id = root.get("root_id")
        if not isinstance(root_id, str) or not root_id:
            raise ValidationError(f"root_lexicon {key} lacks root_id")
        entries.append((root_id, root, pointer))
    return entries


def _record(
    *,
    lane: str,
    role: str,
    payload: Any,
    source_bindings: list[dict[str, Any]],
    citable: bool,
    hypothesis: bool,
    options: DiscoveryOptions,
) -> dict[str, Any]:
    if lane not in LANES:
        raise ValidationError(f"Unknown discovery lane: {lane}")
    if not isinstance(role, str) or not role:
        raise ValidationError("Evidence record role must be nonempty")
    if type(citable) is not bool or type(hypothesis) is not bool:
        raise ValidationError("Evidence trust flags must be booleans")
    if hypothesis and citable:
        raise ValidationError("Hypothesis evidence cannot be citable")
    if not source_bindings:
        raise ValidationError("Evidence record requires source bindings")
    envelope = {
        "schema_version": RECORD_SCHEMA,
        "lane": lane,
        "role": role,
        "citable": citable,
        "hypothesis": hypothesis,
        "source_bindings": sorted(
            source_bindings,
            key=lambda item: (
                item["ayah_ref"],
                item["source_canonical_sha256"],
                item["json_pointer"],
            ),
        ),
        "payload": copy.deepcopy(payload),
    }
    record = {
        "record_id": f"rec_{canonical_sha256(envelope)[:24]}",
        **envelope,
    }
    size = len(canonical_json_bytes(record))
    if size > options.max_record_bytes:
        raise BudgetError(
            f"Exact evidence record {role} is {size} bytes; limit is "
            f"{options.max_record_bytes}. Nothing was projected or truncated."
        )
    return record


def _atom(
    *,
    lane: str,
    kind: str,
    scope: str,
    anchor_refs: list[str],
    branch_refs: list[str],
    evidence_refs: list[dict[str, Any]],
    hypothesis: bool,
) -> dict[str, Any]:
    if lane not in LANES:
        raise ValidationError("Atom lane is invalid")
    if type(hypothesis) is not bool:
        raise ValidationError("Atom hypothesis flag must be boolean")
    if len(anchor_refs) != len(set(anchor_refs)):
        raise ValidationError("Atom anchor refs must not contain duplicates")
    if len(branch_refs) != len(set(branch_refs)):
        raise ValidationError("Atom branch refs must not contain duplicates")
    if len({canonical_sha256(edge) for edge in evidence_refs}) != len(evidence_refs):
        raise ValidationError("Atom evidence refs must not contain duplicates")
    envelope = {
        "schema_version": ATOM_SCHEMA,
        "lane": lane,
        "kind": kind,
        "scope": scope,
        "anchor_refs": sorted(anchor_refs),
        "branch_refs": sorted(branch_refs),
        "evidence_refs": sorted(
            evidence_refs,
            key=lambda item: (
                item["record_id"],
                item["pointer"],
                canonical_sha256(item.get("span")),
            ),
        ),
        "hypothesis": hypothesis,
    }
    return {"atom_id": f"atom_{canonical_sha256(envelope)[:24]}", **envelope}


def _add_exact_field_record(
    records: list[dict[str, Any]],
    record_by_key: dict[tuple[str, str], str],
    *,
    source: dict[str, Any],
    lane: str,
    field: str,
    role: str | None = None,
    citable: bool = True,
    hypothesis: bool = False,
    options: DiscoveryOptions,
) -> str | None:
    bundle = source["bundle"]
    if field not in bundle:
        return None
    record = _record(
        lane=lane,
        role=role or field,
        payload=bundle[field],
        source_bindings=[_source_binding(source, f"/{json_pointer_escape(field)}")],
        citable=citable,
        hypothesis=hypothesis,
        options=options,
    )
    records.append(record)
    record_by_key[(source["ayah_ref"], field)] = record["record_id"]
    return record["record_id"]


def _aggregate_root_records(
    sources: list[dict[str, Any]],
    *,
    lane: str,
    allowed_roots: set[str] | None,
    options: DiscoveryOptions,
) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    for source in sources:
        for root_id, payload, pointer in _root_entries(source["bundle"]):
            mapped = _mapped_root_values(payload, label=root_id)
            if allowed_roots is not None and not (mapped & allowed_roots):
                continue
            payload_hash = canonical_sha256(payload)
            entry = grouped.setdefault(
                (root_id, payload_hash),
                {"payload": payload, "bindings": []},
            )
            entry["bindings"].append(_source_binding(source, pointer))
    records: list[dict[str, Any]] = []
    root_records: dict[str, list[str]] = {}
    for (root_id, _payload_hash), entry in sorted(grouped.items()):
        record = _record(
            lane=lane,
            role="root_lexicon",
            payload=entry["payload"],
            source_bindings=entry["bindings"],
            citable=True,
            hypothesis=False,
            options=options,
        )
        records.append(record)
        root_records.setdefault(root_id, []).append(record["record_id"])
    return records, root_records


def _branch_items(root: dict[str, Any]) -> list[tuple[str, int]]:
    dictionary = root.get("dictionary_entry")
    if dictionary is None:
        return []
    branches = _list(_dict(dictionary, "dictionary_entry").get("branches"), "branches")
    result: list[tuple[str, int]] = []
    for index, raw in enumerate(branches):
        branch = _dict(raw, f"branch {index}")
        branch_ref = branch.get("branch_ref")
        if not isinstance(branch_ref, str) or not BRANCH_REF_RE.fullmatch(branch_ref):
            raise ValidationError(f"Branch {index} lacks branch_ref")
        if branch_ref in {item[0] for item in result}:
            raise ValidationError("Root dictionary contains duplicate branch refs")
        if branch_ref.split("/", 1)[0] != root.get("root_id"):
            raise ValidationError("Branch ref disagrees with its root record")
        result.append((branch_ref, index))
    return result


def _binding_anchors(record: dict[str, Any]) -> list[str]:
    return sorted({binding["ayah_ref"] for binding in record["source_bindings"]})


def _parent_atom(
    record: dict[str, Any], *, scope: str, kind: str | None = None
) -> dict[str, Any]:
    return _atom(
        lane=record["lane"],
        kind=kind or f"{record['role']}_record",
        scope=scope,
        anchor_refs=_binding_anchors(record),
        branch_refs=[],
        evidence_refs=[{"record_id": record["record_id"], "pointer": ""}],
        hypothesis=record["hypothesis"],
    )


def _exact_record_atoms(record: dict[str, Any], *, scope: str) -> list[dict[str, Any]]:
    if record["role"] == "root_grounding_gap":
        return [
            _atom(
                lane=record["lane"],
                kind="diagnostic:root_grounding_gap",
                scope=scope,
                anchor_refs=_binding_anchors(record),
                branch_refs=[],
                evidence_refs=[{"record_id": record["record_id"], "pointer": ""}],
                hypothesis=True,
            )
        ]
    atoms = [_parent_atom(record, scope=scope)]
    record_id = record["record_id"]
    lane = record["lane"]
    role = record["role"]
    payload = record["payload"]
    fallback_anchors = _binding_anchors(record)
    if role == "qac_morphemes":
        for index, raw_row in enumerate(_list(payload, role)):
            row = _dict(raw_row, f"{role}[{index}]")
            atoms.append(
                _atom(
                    lane=lane,
                    kind="morpheme",
                    scope=scope,
                    anchor_refs=[row["qac_ref"], row["qac_word_ref"]],
                    branch_refs=[],
                    evidence_refs=[{"record_id": record_id, "pointer": f"/{index}"}],
                    hypothesis=False,
                )
            )
    elif role == "word_analysis":
        words = _list(_dict(payload, role).get("words"), f"{role}.words")
        for word_index, raw_word in enumerate(words):
            word = _dict(raw_word, f"{role}.words[{word_index}]")
            anchors = [word["aligned_qac_word_ref"]]
            atoms.append(
                _atom(
                    lane=lane,
                    kind="word",
                    scope=scope,
                    anchor_refs=anchors,
                    branch_refs=[],
                    evidence_refs=[
                        {"record_id": record_id, "pointer": f"/words/{word_index}"}
                    ],
                    hypothesis=False,
                )
            )
            for topic_index, _topic in enumerate(word.get("topics", [])):
                atoms.append(
                    _atom(
                        lane=lane,
                        kind="word_topic",
                        scope=scope,
                        anchor_refs=anchors,
                        branch_refs=[],
                        evidence_refs=[
                            {
                                "record_id": record_id,
                                "pointer": f"/words/{word_index}/topics/{topic_index}",
                            }
                        ],
                        hypothesis=False,
                    )
                )
    elif role == "word_morpheme_spans":
        for index, raw_span in enumerate(_list(payload, role)):
            anchor_groups = [fallback_anchors]
            if raw_span is not None:
                span = _dict(raw_span, f"{role}[{index}]")
                refs = _list(span.get("qac_refs"), f"{role}[{index}].qac_refs")
                grouped: dict[str, list[str]] = {}
                for ref in refs:
                    grouped.setdefault(":".join(ref.split(":")[:3]), []).append(ref)
                anchor_groups = list(grouped.values())
            for anchors in anchor_groups:
                atoms.append(
                    _atom(
                        lane=lane,
                        kind="morpheme_span",
                        scope=scope,
                        anchor_refs=anchors,
                        branch_refs=[],
                        evidence_refs=[{"record_id": record_id, "pointer": f"/{index}"}],
                        hypothesis=False,
                    )
                )
    elif role == "root_lexicon":
        for branch_ref, branch_index in _branch_items(_dict(payload, role)):
            atoms.append(
                _atom(
                    lane=lane,
                    kind="root_branch",
                    scope=scope,
                    anchor_refs=fallback_anchors,
                    branch_refs=[branch_ref],
                    evidence_refs=[
                        {
                            "record_id": record_id,
                            "pointer": f"/dictionary_entry/branches/{branch_index}",
                        }
                    ],
                    hypothesis=False,
                )
            )
    return atoms


def _branch_inventory_atoms(
    record: dict[str, Any], *, scope: str
) -> list[dict[str, Any]]:
    atoms = [_parent_atom(record, scope=scope, kind="hft_branch_inventory_record")]
    payload = _dict(record["payload"], "branch_inventories")
    packet = payload.get("full_context_packet")
    if packet is None:
        return atoms
    packet = _dict(packet, "branch_inventories.full_context_packet")
    inventories = _list(
        packet.get("branch_inventories"),
        "branch_inventories.full_context_packet.branch_inventories",
    )
    for root_index, raw_inventory in enumerate(inventories):
        inventory = _dict(raw_inventory, f"branch inventory {root_index}")
        branches = _list(inventory.get("branches"), f"branch inventory {root_index}.branches")
        for branch_index, raw_branch in enumerate(branches):
            branch = _dict(raw_branch, "branch inventory branch")
            branch_id = branch.get("branch_id")
            if not isinstance(branch_id, str) or not re.fullmatch(r"B[0-9]+", branch_id):
                raise ValidationError("HFT branch inventory has an invalid branch_id")
            variants = _list(branch.get("variants"), "branch inventory variants")
            branch_refs: list[str] = []
            for variant_index, raw_variant in enumerate(variants):
                variant = _dict(raw_variant, f"branch inventory variant {variant_index}")
                root_id = variant.get("root_id")
                branch_ref = f"{root_id}/{branch_id}"
                if not isinstance(root_id, str) or not BRANCH_REF_RE.fullmatch(branch_ref):
                    raise ValidationError("HFT branch inventory has an invalid root_id")
                branch_refs.append(branch_ref)
            if len(branch_refs) != len(set(branch_refs)):
                raise ValidationError("HFT branch inventory contains duplicate variants")
            atoms.append(
                _atom(
                    lane=record["lane"],
                    kind="hft_branch_inventory_branch",
                    scope=scope,
                    anchor_refs=_binding_anchors(record),
                    branch_refs=branch_refs,
                    evidence_refs=[
                        {
                            "record_id": record["record_id"],
                            "pointer": (
                                "/full_context_packet/branch_inventories/"
                                f"{root_index}/branches/{branch_index}"
                            ),
                        }
                    ],
                    hypothesis=True,
                )
            )
    return atoms


def _micro_atoms(
    source: dict[str, Any], records: list[dict[str, Any]], *, lane: str = "micro"
) -> list[dict[str, Any]]:
    del source
    scope = "focus_ayah" if lane == "micro" else "global"
    atoms: list[dict[str, Any]] = []
    for record in records:
        if record["hypothesis"]:
            continue
        atoms.extend(_exact_record_atoms(record, scope=scope))
    return atoms


def _macro_atoms(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    atoms: list[dict[str, Any]] = []
    for record in records:
        role = record["role"]
        if role == "branch_inventories":
            atoms.extend(_branch_inventory_atoms(record, scope="pericope"))
        elif role == "inter_ayah_row":
            anchors = sorted(
                set(_binding_anchors(record) + [record["payload"]["ref"]])
            )
            atoms.append(
                _atom(
                    lane="macro",
                    kind="inter_ayah_hypothesis",
                    scope="pericope",
                    anchor_refs=anchors,
                    branch_refs=[],
                    evidence_refs=[{"record_id": record["record_id"], "pointer": ""}],
                    hypothesis=True,
                )
            )
        else:
            atoms.extend(_exact_record_atoms(record, scope="pericope"))
    return atoms


def _markdown_spans(value: str) -> list[tuple[int, int]]:
    if not value:
        return []
    marker_starts = [
        match.start() for match in re.finditer(r"(?m)^(?:\d+\.\s+|[-*]\s+)", value)
    ]
    boundaries = sorted(set([0, *marker_starts, len(value)]))
    return [
        (start, end)
        for start, end in zip(boundaries, boundaries[1:])
        if start < end
    ]


def _span_edge(record_id: str, pointer: str, value: str, start: int, end: int) -> dict[str, Any]:
    return {
        "record_id": record_id,
        "pointer": pointer,
        "span": {
            "start": start,
            "end": end,
            "sha256": sha256_bytes(value[start:end].encode("utf-8")),
        },
    }


def _global_atoms(source: dict[str, Any], records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    atoms = _micro_atoms(source, records, lane="global")
    for record in records:
        if not record["hypothesis"]:
            continue
        payload = record["payload"]
        role = record["role"]
        anchors = _binding_anchors(record)
        if role == "inter_ayah_row":
            anchors = sorted(set(anchors + [payload["ref"]]))
            atoms.append(
                _atom(
                    lane="global",
                    kind="hypothesis:inter_ayah_row",
                    scope="global",
                    anchor_refs=anchors,
                    branch_refs=[],
                    evidence_refs=[{"record_id": record["record_id"], "pointer": ""}],
                    hypothesis=True,
                )
            )
        else:
            atoms.append(
                _parent_atom(record, scope="global", kind=f"hypothesis:{role}")
            )
        if role in {"v12_reader_walks", "v12_reader_walks_wide"} and isinstance(
            payload, dict
        ):
            for reader_id, raw_reader in sorted(payload.items()):
                if not isinstance(raw_reader, dict):
                    continue
                for field in ("activated_readings_md", "retrospective_surprises_md"):
                    value = raw_reader.get(field)
                    if not isinstance(value, str):
                        continue
                    pointer = f"/{json_pointer_escape(str(reader_id))}/{field}"
                    for start, end in _markdown_spans(value):
                        atoms.append(
                            _atom(
                                lane="global",
                                kind=f"hypothesis:{role}:retained_segment",
                                scope="global",
                                anchor_refs=anchors,
                                branch_refs=[],
                                evidence_refs=[
                                    _span_edge(record["record_id"], pointer, value, start, end)
                                ],
                                hypothesis=True,
                            )
                        )
        elif role == "v12_focus_trace_hermetic" and isinstance(payload, dict):
            readers = payload.get("readers")
            if isinstance(readers, dict):
                for reader_id, raw_reader in sorted(readers.items()):
                    if not isinstance(raw_reader, dict):
                        continue
                    for field in (
                        "baseline_models",
                        "context_deltas",
                        "surprising_valid_outliers",
                    ):
                        values = raw_reader.get(field)
                        if not isinstance(values, list):
                            continue
                        for index in range(len(values)):
                            atoms.append(
                                _atom(
                                    lane="global",
                                    kind=f"hypothesis:{role}:{field}",
                                    scope="global",
                                    anchor_refs=anchors,
                                    branch_refs=[],
                                    evidence_refs=[
                                        {
                                            "record_id": record["record_id"],
                                            "pointer": (
                                                "/readers/"
                                                f"{json_pointer_escape(str(reader_id))}/"
                                                f"{field}/{index}"
                                            ),
                                        }
                                    ],
                                    hypothesis=True,
                                )
                            )
        elif role == "v12_cross_run_publication" and isinstance(payload, dict):
            findings = payload.get("findings")
            if isinstance(findings, list):
                for index in range(len(findings)):
                    atoms.append(
                        _atom(
                            lane="global",
                            kind=f"hypothesis:{role}:finding",
                            scope="global",
                            anchor_refs=anchors,
                            branch_refs=[],
                            evidence_refs=[
                                {
                                    "record_id": record["record_id"],
                                    "pointer": f"/findings/{index}",
                                }
                            ],
                            hypothesis=True,
                        )
                    )
    return atoms


def _build_lane_store_unvalidated(
    sources: Iterable[dict[str, Any]],
    *,
    lane: str,
    focus_ayah_ref: str,
    target_refs: list[str] | None = None,
    options: DiscoveryOptions | None = None,
) -> dict[str, Any]:
    options = options or DiscoveryOptions()
    options.validate()
    if lane not in LANES:
        raise ValidationError(f"Unknown discovery lane: {lane}")
    _surah, _ayah, focus_ayah_ref = _ayah_ref(focus_ayah_ref, "focus ayah")
    ordered = _ordered_sources(sources)
    for source in ordered:
        _validate_bundle_shape(source)
    context = build_context_manifest(ordered, focus_ayah_ref=focus_ayah_ref)
    if lane != "macro" and target_refs is not None:
        raise ValidationError("target_refs are accepted only for the reusable macro lane")
    source_by_ref = {source["ayah_ref"]: source for source in ordered}
    focus = source_by_ref[focus_ayah_ref]
    records: list[dict[str, Any]] = []
    record_by_key: dict[tuple[str, str], str] = {}
    root_records: dict[str, list[str]] = {}

    if lane == "micro":
        for field in MICRO_EXACT_FIELDS:
            _add_exact_field_record(
                records,
                record_by_key,
                source=focus,
                lane=lane,
                field=field,
                options=options,
            )
        qac_roots = {
            item["root_ar"]
            for item in focus["bundle"]["qac_morphemes"]
            if item["root_ar"]
        }
        root_items, root_records = _aggregate_root_records(
            [focus], lane=lane, allowed_roots=qac_roots, options=options
        )
        records.extend(root_items)
        _add_root_gap_records(records, source=focus, lane=lane, options=options)
        atoms = _micro_atoms(focus, records)
        targets = [focus_ayah_ref]
    elif lane == "macro":
        for source in ordered:
            for field in MACRO_EXACT_FIELDS:
                _add_exact_field_record(
                    records,
                    record_by_key,
                    source=source,
                    lane=lane,
                    field=field,
                    options=options,
                )
            bundle = source["bundle"]
            for index, channel in enumerate(
                bundle.get("channel_subchannels_anchored_here", [])
            ):
                record = _record(
                    lane=lane,
                    role="channel",
                    payload=channel,
                    source_bindings=[
                        _source_binding(
                            source, f"/channel_subchannels_anchored_here/{index}"
                        )
                    ],
                    citable=True,
                    hypothesis=False,
                    options=options,
                )
                records.append(record)
            pericope_refs = set(context["scope"]["refs"])
            for index, row in enumerate(bundle.get("inter_ayah_rows", [])):
                if row.get("ref") in pericope_refs:
                    records.append(
                        _record(
                            lane=lane,
                            role="inter_ayah_row",
                            payload=row,
                            source_bindings=[
                                _source_binding(source, f"/inter_ayah_rows/{index}")
                            ],
                            citable=False,
                            hypothesis=True,
                            options=options,
                        )
                    )
            if "branch_inventories" in bundle:
                _add_exact_field_record(
                    records,
                    record_by_key,
                    source=source,
                    lane=lane,
                    field="branch_inventories",
                    citable=False,
                    hypothesis=True,
                    options=options,
                )
            _add_root_gap_records(records, source=source, lane=lane, options=options)
        root_items, root_records = _aggregate_root_records(
            ordered, lane=lane, allowed_roots=None, options=options
        )
        records.extend(root_items)
        atoms = _macro_atoms(records)
        expected_targets = context["scope"]["refs"]
        targets = expected_targets if target_refs is None else target_refs
        if targets != expected_targets:
            raise ValidationError(
                "Reusable macro target_refs must exactly equal ordered pericope refs"
            )
    else:
        for field in MICRO_EXACT_FIELDS:
            _add_exact_field_record(
                records,
                record_by_key,
                source=focus,
                lane=lane,
                field=field,
                options=options,
            )
        pericope_refs = set(context["scope"]["refs"])
        for index, row in enumerate(focus["bundle"].get("inter_ayah_rows", [])):
            if row.get("ref") in pericope_refs:
                continue
            records.append(
                _record(
                    lane=lane,
                    role="inter_ayah_row",
                    payload=row,
                    source_bindings=[
                        _source_binding(focus, f"/inter_ayah_rows/{index}")
                    ],
                    citable=False,
                    hypothesis=True,
                    options=options,
                )
            )
        for field in GLOBAL_HYPOTHESIS_FIELDS:
            _add_exact_field_record(
                records,
                record_by_key,
                source=focus,
                lane=lane,
                field=field,
                citable=False,
                hypothesis=True,
                options=options,
            )
        qac_roots = {
            item["root_ar"]
            for item in focus["bundle"]["qac_morphemes"]
            if item["root_ar"]
        }
        root_items, root_records = _aggregate_root_records(
            [focus], lane=lane, allowed_roots=qac_roots, options=options
        )
        records.extend(root_items)
        _add_root_gap_records(records, source=focus, lane=lane, options=options)
        atoms = _global_atoms(focus, records)
        targets = [focus_ayah_ref]

    if not isinstance(targets, list):
        raise ValidationError("Discovery target refs must be an array")
    for index, ref in enumerate(targets):
        _ayah_ref(ref, f"target_refs[{index}]")
    if len(targets) != len(set(targets)):
        raise ValidationError("Discovery target refs must be duplicate-free")

    records = sorted(records, key=lambda item: item["record_id"])
    atoms = sorted(atoms, key=lambda item: item["atom_id"])
    if len({item["record_id"] for item in records}) != len(records):
        raise ValidationError("Discovery store contains duplicate record IDs")
    if len({item["atom_id"] for item in atoms}) != len(atoms):
        raise ValidationError("Discovery store contains duplicate atom IDs")
    record_ids = {item["record_id"] for item in records}
    for atom in atoms:
        unknown = {
            edge["record_id"]
            for edge in atom["evidence_refs"]
            if edge["record_id"] not in record_ids
        }
        if unknown:
            raise ValidationError(f"Discovery atom cites unknown records: {sorted(unknown)}")
    store = {
        "schema_version": STORE_SCHEMA,
        "identity": {
            "focus_ayah_ref": focus_ayah_ref,
            "target_refs": targets,
            "lane": lane,
            "context_payload_sha256": context["identity"]["context_payload_sha256"],
            "source_set_sha256": context["identity"]["source_set_sha256"],
        },
        "scope": context["scope"],
        "records": records,
        "atoms": atoms,
        "coverage": {
            "record_count": len(records),
            "atom_count": len(atoms),
            "record_ids_sha256": canonical_sha256(
                [item["record_id"] for item in records]
            ),
            "atom_ids_sha256": canonical_sha256([item["atom_id"] for item in atoms]),
            "exact_payloads_only": True,
        },
    }
    store["identity"]["store_payload_sha256"] = canonical_sha256(store)
    store_size = len(canonical_json_bytes(store))
    if store_size > options.max_store_bytes:
        raise BudgetError(
            f"Discovery store is {store_size} bytes; limit is "
            f"{options.max_store_bytes}. Nothing was projected or truncated."
        )
    return store


def build_lane_store(
    sources: Iterable[dict[str, Any]],
    *,
    lane: str,
    focus_ayah_ref: str,
    target_refs: list[str] | None = None,
    options: DiscoveryOptions | None = None,
) -> dict[str, Any]:
    options = options or DiscoveryOptions()
    ordered = _ordered_sources(sources)
    store = _build_lane_store_unvalidated(
        ordered,
        lane=lane,
        focus_ayah_ref=focus_ayah_ref,
        target_refs=target_refs,
        options=options,
    )
    validate_lane_store(store, ordered, options=options)
    return store


def _allowed_anchor_refs(sources: list[dict[str, Any]]) -> set[str]:
    refs: set[str] = set()
    for source in sources:
        refs.add(source["ayah_ref"])
        bundle = source["bundle"]
        for row in bundle["qac_morphemes"]:
            refs.update((row["qac_ref"], row["qac_word_ref"]))
        for word in bundle["word_analysis"]["words"]:
            refs.add(word["aligned_qac_word_ref"])
        for span in bundle["word_morpheme_spans"]:
            if span is not None:
                refs.update(span["qac_refs"])
        for row in bundle.get("inter_ayah_rows", []):
            if "ref" in row:
                refs.add(row["ref"])
        for channel in bundle.get("channel_subchannels_anchored_here", []):
            channel_refs = channel.get("ayah_refs")
            if isinstance(channel_refs, list):
                for ref in channel_refs:
                    refs.add(_ayah_ref(ref, "channel ayah_refs")[2])
    return refs


def _inventory_branch_refs(payload: Any) -> set[str]:
    refs: set[str] = set()
    if not isinstance(payload, dict):
        return refs
    packet = payload.get("full_context_packet")
    if not isinstance(packet, dict):
        return refs
    inventories = packet.get("branch_inventories")
    if not isinstance(inventories, list):
        return refs
    for inventory in inventories:
        if not isinstance(inventory, dict) or not isinstance(inventory.get("branches"), list):
            continue
        for branch in inventory["branches"]:
            if not isinstance(branch, dict) or not isinstance(branch.get("branch_id"), str):
                continue
            variants = branch.get("variants")
            if not isinstance(variants, list):
                continue
            for variant in variants:
                if isinstance(variant, dict) and isinstance(variant.get("root_id"), str):
                    refs.add(f"{variant['root_id']}/{branch['branch_id']}")
    return refs


def _validate_evidence_edge(
    edge: dict[str, Any], record: dict[str, Any], *, label: str
) -> None:
    if set(edge) not in ({"record_id", "pointer"}, {"record_id", "pointer", "span"}):
        raise ValidationError(f"{label} has unexpected fields")
    if edge.get("record_id") != record["record_id"]:
        raise ValidationError(f"{label} record identity is inconsistent")
    selected = _json_pointer_get(record["payload"], edge.get("pointer"), label=label)
    if "span" not in edge:
        return
    span = _dict(edge["span"], f"{label}.span")
    if set(span) != {"start", "end", "sha256"} or not isinstance(selected, str):
        raise ValidationError(f"{label}.span is invalid")
    start = span.get("start")
    end = span.get("end")
    if (
        not isinstance(start, int)
        or isinstance(start, bool)
        or not isinstance(end, int)
        or isinstance(end, bool)
        or start < 0
        or end <= start
        or end > len(selected)
    ):
        raise ValidationError(f"{label}.span bounds are invalid")
    if span.get("sha256") != sha256_bytes(selected[start:end].encode("utf-8")):
        raise ValidationError(f"{label}.span hash is invalid")


def validate_lane_store(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    *,
    options: DiscoveryOptions | None = None,
) -> None:
    options = options or DiscoveryOptions()
    options.validate()
    ordered_sources = _ordered_sources(sources)
    for source in ordered_sources:
        _validate_bundle_shape(source)
    if store.get("schema_version") != STORE_SCHEMA:
        raise ValidationError("Unexpected discovery store schema")
    identity = _dict(store.get("identity"), "discovery store identity")
    claimed = identity.get("store_payload_sha256")
    payload = copy.deepcopy(store)
    _dict(payload["identity"], "discovery store identity").pop(
        "store_payload_sha256", None
    )
    if not isinstance(claimed, str) or claimed != canonical_sha256(payload):
        raise ValidationError("Discovery store payload hash is invalid")
    lane = identity.get("lane")
    if lane not in LANES:
        raise ValidationError("Discovery store lane is invalid")
    _surah, _ayah, focus_ref = _ayah_ref(
        identity.get("focus_ayah_ref"), "discovery focus ayah"
    )
    context = build_context_manifest(ordered_sources, focus_ayah_ref=focus_ref)
    expected_identity_binding = {
        "context_payload_sha256": context["identity"]["context_payload_sha256"],
        "source_set_sha256": context["identity"]["source_set_sha256"],
    }
    if any(identity.get(key) != value for key, value in expected_identity_binding.items()):
        raise ValidationError("Discovery store identity is not source-bound")
    if canonical_json_bytes(store.get("scope")) != canonical_json_bytes(context["scope"]):
        raise ValidationError("Discovery store scope is not source-bound")
    targets = _list(identity.get("target_refs"), "discovery target_refs")
    for index, ref in enumerate(targets):
        _ayah_ref(ref, f"discovery target_refs[{index}]")
    if len(targets) != len(set(targets)):
        raise ValidationError("Discovery target refs contain duplicates")
    expected_targets = context["scope"]["refs"] if lane == "macro" else [focus_ref]
    if targets != expected_targets:
        raise ValidationError("Discovery target refs violate lane scope")
    records = _list(store.get("records"), "discovery records")
    atoms = _list(store.get("atoms"), "discovery atoms")
    if any(not isinstance(item, dict) for item in records):
        raise ValidationError("Discovery records must be objects")
    if records != sorted(records, key=lambda item: item.get("record_id", "")):
        raise ValidationError("Discovery records are not canonically ordered")
    source_by_ref = {source["ayah_ref"]: source for source in ordered_sources}
    record_ids: set[str] = set()
    records_by_id: dict[str, dict[str, Any]] = {}
    branch_registry: set[str] = set()
    for index, raw_record in enumerate(records):
        record = _dict(raw_record, f"discovery record {index}")
        if set(record) != {
            "record_id",
            "schema_version",
            "lane",
            "role",
            "citable",
            "hypothesis",
            "source_bindings",
            "payload",
        } or record.get("schema_version") != RECORD_SCHEMA:
            raise ValidationError("Discovery record shape is invalid")
        record_id = record.get("record_id")
        envelope = {key: value for key, value in record.items() if key != "record_id"}
        expected = f"rec_{canonical_sha256(envelope)[:24]}"
        if record_id != expected or record_id in record_ids:
            raise ValidationError("Discovery record identity is invalid or duplicated")
        if record.get("lane") != lane:
            raise ValidationError("Discovery record lane disagrees with store")
        if not isinstance(record.get("role"), str) or not record["role"]:
            raise ValidationError("Discovery record role is invalid")
        if type(record.get("citable")) is not bool or type(record.get("hypothesis")) is not bool:
            raise ValidationError("Discovery record trust flags are invalid")
        if record["hypothesis"] and record["citable"]:
            raise ValidationError("Hypothesis records cannot be citable")
        bindings = _list(record.get("source_bindings"), "record source_bindings")
        if not bindings or any(not isinstance(item, dict) for item in bindings):
            raise ValidationError("Discovery record source bindings are invalid")
        if bindings != sorted(
            bindings,
            key=lambda item: (
                item.get("ayah_ref", ""),
                item.get("source_canonical_sha256", ""),
                item.get("json_pointer", ""),
            ),
        ) or len({canonical_sha256(item) for item in bindings}) != len(bindings):
            raise ValidationError("Discovery record source bindings are invalid")
        for binding_index, raw_binding in enumerate(bindings):
            binding = _dict(raw_binding, f"record binding {binding_index}")
            if set(binding) != {
                "ayah_ref",
                "source_raw_sha256",
                "source_canonical_sha256",
                "json_pointer",
            }:
                raise ValidationError("Discovery record source binding shape is invalid")
            source = source_by_ref.get(binding.get("ayah_ref"))
            if source is None or binding["source_raw_sha256"] != source["raw_sha256"] or binding[
                "source_canonical_sha256"
            ] != source["canonical_sha256"]:
                raise ValidationError("Discovery record binding is not source-bound")
            selected = _json_pointer_get(
                source["bundle"],
                binding.get("json_pointer"),
                label=f"record binding {binding_index}",
            )
            if canonical_json_bytes(selected) != canonical_json_bytes(record["payload"]):
                raise ValidationError("Discovery record payload differs from bound source")
        if len(canonical_json_bytes(record)) > options.max_record_bytes:
            raise BudgetError("Discovery record exceeds configured exact-record limit")
        record_ids.add(record_id)
        records_by_id[record_id] = record
        if record["role"] == "root_lexicon":
            branch_registry.update(ref for ref, _index in _branch_items(record["payload"]))
        elif record["role"] == "branch_inventories":
            branch_registry.update(_inventory_branch_refs(record["payload"]))
    allowed_anchors = _allowed_anchor_refs(ordered_sources)
    atom_ids: set[str] = set()
    records_with_atoms: set[str] = set()
    if any(not isinstance(item, dict) for item in atoms):
        raise ValidationError("Discovery atoms must be objects")
    if atoms != sorted(atoms, key=lambda item: item.get("atom_id", "")):
        raise ValidationError("Discovery atoms are not canonically ordered")
    for index, raw_atom in enumerate(atoms):
        atom = _dict(raw_atom, f"discovery atom {index}")
        if set(atom) != {
            "atom_id",
            "schema_version",
            "lane",
            "kind",
            "scope",
            "anchor_refs",
            "branch_refs",
            "evidence_refs",
            "hypothesis",
        } or atom.get("schema_version") != ATOM_SCHEMA:
            raise ValidationError("Discovery atom shape is invalid")
        atom_id = atom.get("atom_id")
        envelope = {key: value for key, value in atom.items() if key != "atom_id"}
        expected = f"atom_{canonical_sha256(envelope)[:24]}"
        if atom_id != expected or atom_id in atom_ids:
            raise ValidationError("Discovery atom identity is invalid or duplicated")
        if atom.get("lane") != lane:
            raise ValidationError("Discovery atom lane disagrees with store")
        if type(atom.get("hypothesis")) is not bool:
            raise ValidationError("Discovery atom hypothesis flag is invalid")
        anchors = _list(atom.get("anchor_refs"), "atom anchor_refs")
        branches = _list(atom.get("branch_refs"), "atom branch_refs")
        if any(not isinstance(ref, str) for ref in anchors):
            raise ValidationError("Discovery atom anchor refs must be strings")
        if any(not isinstance(ref, str) for ref in branches):
            raise ValidationError("Discovery atom branch refs must be strings")
        if anchors != sorted(anchors) or len(anchors) != len(set(anchors)):
            raise ValidationError("Discovery atom anchor refs are not canonical")
        if branches != sorted(branches) or len(branches) != len(set(branches)):
            raise ValidationError("Discovery atom branch refs are not canonical")
        if any(
            _canonical_anchor_ref(ref, "atom anchor ref") not in allowed_anchors
            for ref in anchors
        ):
            raise ValidationError("Discovery atom cites an unregistered anchor ref")
        if any(
            not isinstance(ref, str)
            or not BRANCH_REF_RE.fullmatch(ref)
            or ref not in branch_registry
            for ref in branches
        ):
            raise ValidationError("Discovery atom cites an unregistered branch ref")
        edges = _list(atom.get("evidence_refs"), "atom evidence_refs")
        if not edges or len({canonical_sha256(edge) for edge in edges}) != len(edges):
            raise ValidationError("Discovery atom has invalid evidence edges")
        for edge_index, raw_edge in enumerate(edges):
            edge = _dict(raw_edge, f"atom evidence edge {edge_index}")
            record = records_by_id.get(edge.get("record_id"))
            if record is None:
                raise ValidationError("Discovery atom cites an unknown record")
            _validate_evidence_edge(edge, record, label=f"atom evidence edge {edge_index}")
            if not atom["hypothesis"] and (
                record["hypothesis"] or not record["citable"]
            ):
                raise ValidationError("Supported atom cites non-citable evidence")
            records_with_atoms.add(record["record_id"])
        atom_ids.add(atom_id)
    if records_with_atoms != record_ids:
        missing = sorted(record_ids - records_with_atoms)
        raise ValidationError(f"Discovery records lack atomic obligations: {missing}")
    coverage = _dict(store.get("coverage"), "discovery coverage")
    expected_coverage = {
        "record_count": len(records),
        "atom_count": len(atoms),
        "record_ids_sha256": canonical_sha256(
            [item["record_id"] for item in records]
        ),
        "atom_ids_sha256": canonical_sha256([item["atom_id"] for item in atoms]),
        "exact_payloads_only": True,
    }
    if canonical_json_bytes(coverage) != canonical_json_bytes(expected_coverage):
        raise ValidationError("Discovery store coverage is inconsistent")
    if len(canonical_json_bytes(store)) > options.max_store_bytes:
        raise BudgetError("Discovery store exceeds configured byte limit")
    expected = _build_lane_store_unvalidated(
        ordered_sources,
        lane=lane,
        focus_ayah_ref=focus_ref,
        target_refs=targets if lane == "macro" else None,
        options=options,
    )
    if canonical_json_bytes(store) != canonical_json_bytes(expected):
        raise ValidationError("Discovery store does not exactly rederive from sources")


def _record_catalog(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "record_id": record["record_id"],
            "role": record["role"],
            "citable": record["citable"],
            "hypothesis": record["hypothesis"],
            "source_bindings": record["source_bindings"],
        }
        for record in records
    ]


def _packet(
    store: dict[str, Any],
    *,
    chunk_kind: str,
    chunk_index: int,
    chunk_count: int,
    records: list[dict[str, Any]],
    atoms: list[dict[str, Any]],
) -> dict[str, Any]:
    ordered_record_ids = [item["record_id"] for item in records]
    ordered_atom_ids = [item["atom_id"] for item in atoms]
    coverage_root = canonical_sha256(
        {
            "ordered_record_ids": ordered_record_ids,
            "ordered_atom_ids": ordered_atom_ids,
        }
    )
    packet = {
        "schema_version": PACKET_SCHEMA,
        "identity": {
            **store["identity"],
            "chunk_kind": chunk_kind,
            "chunk_index": chunk_index,
            "chunk_count": chunk_count,
            "coverage_root_sha256": coverage_root,
        },
        "scope": store["scope"],
        "record_catalog": _record_catalog(store["records"]),
        "records": records,
        "atoms": atoms,
        "coverage": {
            "ordered_record_ids": ordered_record_ids,
            "ordered_atom_ids": ordered_atom_ids,
            "record_count": len(records),
            "atom_count": len(atoms),
            "coverage_root_sha256": coverage_root,
            "exact_payloads_only": True,
        },
        "contract": {
            **PACKET_CONTRACT,
        },
    }
    packet["identity"]["packet_payload_sha256"] = canonical_sha256(packet)
    return packet


def _estimated_packet_size(
    base_size: int,
    records: list[dict[str, Any]],
    atoms: list[dict[str, Any]],
    record_costs: dict[str, int],
    atom_costs: dict[str, int],
) -> int:
    record_delta = sum(record_costs[record["record_id"]] for record in records)
    atom_delta = sum(atom_costs[atom["atom_id"]] for atom in atoms)
    if records:
        record_delta += 2 * (len(records) - 1)
    if atoms:
        atom_delta += 2 * (len(atoms) - 1)
    count_delta = len(str(len(records))) - 1 + len(str(len(atoms))) - 1
    return base_size + record_delta + atom_delta + count_delta


def _packet_units(
    store: dict[str, Any],
) -> list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]]:
    records = store["records"]
    records_by_id = {record["record_id"]: record for record in records}
    atoms_by_primary: dict[str, list[dict[str, Any]]] = {}
    for atom in store["atoms"]:
        primary = atom["evidence_refs"][0]["record_id"]
        atoms_by_primary.setdefault(primary, []).append(atom)
    shared_context = (
        [record for record in records if record["role"] in MACRO_EXACT_FIELDS]
        if store["identity"]["lane"] == "macro"
        else []
    )
    units: list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]] = []
    for record in records:
        kind = (
            "root"
            if store["identity"]["lane"] == "macro" and record["role"] == "root_lexicon"
            else "structural"
            if store["identity"]["lane"] == "macro"
            else "evidence"
        )
        atoms = atoms_by_primary.get(record["record_id"], [])
        required_ids = {
            edge["record_id"] for atom in atoms for edge in atom["evidence_refs"]
        }
        unit_records = [
            *(shared_context if kind == "root" else []),
            *[records_by_id[record_id] for record_id in sorted(required_ids)],
        ]
        deduplicated = {
            item["record_id"]: item for item in unit_records
        }
        units.append(
            (
                kind,
                [deduplicated[key] for key in sorted(deduplicated)],
                sorted(atoms, key=lambda item: item["atom_id"]),
            )
        )
    return sorted(units, key=lambda item: (item[0], item[1][-1]["record_id"]))


def _merge_packet_units(
    units: list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]],
) -> tuple[str, list[dict[str, Any]], list[dict[str, Any]]]:
    kind = units[0][0]
    if any(unit[0] != kind for unit in units):
        raise ValidationError("Packet units of different kinds cannot be merged")
    records_by_id = {
        record["record_id"]: record for _kind, records, _atoms in units for record in records
    }
    atoms_by_id = {
        atom["atom_id"]: atom for _kind, _records, atoms in units for atom in atoms
    }
    return (
        kind,
        [records_by_id[key] for key in sorted(records_by_id)],
        [atoms_by_id[key] for key in sorted(atoms_by_id)],
    )


def _packet_groups(
    store: dict[str, Any], options: DiscoveryOptions
) -> list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]]:
    units = _packet_units(store)
    kinds = sorted({unit[0] for unit in units})
    base_sizes = {
        kind: len(
            canonical_json_bytes(
                _packet(
                    store,
                    chunk_kind=kind,
                    chunk_index=999_999,
                    chunk_count=999_999,
                    records=[],
                    atoms=[],
                )
            )
        )
        for kind in kinds
    }
    record_costs = {
        record["record_id"]: len(canonical_json_bytes(record))
        + len(canonical_json_bytes(record["record_id"]))
        for record in store["records"]
    }
    atom_costs = {
        atom["atom_id"]: len(canonical_json_bytes(atom))
        + len(canonical_json_bytes(atom["atom_id"]))
        for atom in store["atoms"]
    }
    groups: list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]] = []
    pending: list[tuple[str, list[dict[str, Any]], list[dict[str, Any]]]] = []
    for unit in units:
        if pending and unit[0] != pending[0][0]:
            groups.append(_merge_packet_units(pending))
            pending = []
        candidate = [*pending, unit]
        kind, records, atoms = _merge_packet_units(candidate)
        candidate_size = _estimated_packet_size(
            base_sizes[kind], records, atoms, record_costs, atom_costs
        )
        if pending and candidate_size > options.max_packet_bytes:
            groups.append(_merge_packet_units(pending))
            pending = [unit]
        else:
            pending = candidate
        single_kind, single_records, single_atoms = _merge_packet_units(pending)
        single_size = _estimated_packet_size(
            base_sizes[single_kind],
            single_records,
            single_atoms,
            record_costs,
            atom_costs,
        )
        if single_size > options.max_packet_bytes:
            raise BudgetError(
                f"Lossless {single_kind} packet unit exceeds "
                f"{options.max_packet_bytes} bytes. Increase the limit; nothing was "
                "split, projected, or truncated."
            )
    if pending:
        groups.append(_merge_packet_units(pending))
    if not groups or len(groups) > 999_999:
        raise BudgetError("Discovery packet count exceeds the deterministic safety limit")
    return groups


def _build_discovery_packets_unvalidated(
    store: dict[str, Any], options: DiscoveryOptions
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    groups = _packet_groups(store, options)
    packets = [
        _packet(
            store,
            chunk_kind=kind,
            chunk_index=index,
            chunk_count=len(groups),
            records=records,
            atoms=atoms,
        )
        for index, (kind, records, atoms) in enumerate(groups)
    ]
    if any(len(canonical_json_bytes(packet)) > options.max_packet_bytes for packet in packets):
        raise BudgetError("A lossless discovery packet exceeds the configured limit")
    atom_appearances = {item["atom_id"]: 0 for item in store["atoms"]}
    record_appearances = {item["record_id"]: 0 for item in store["records"]}
    for packet in packets:
        local_record_ids = {record["record_id"] for record in packet["records"]}
        for atom in packet["atoms"]:
            if any(edge["record_id"] not in local_record_ids for edge in atom["evidence_refs"]):
                raise ValidationError("Packet atom lacks packet-local exact evidence")
            atom_appearances[atom["atom_id"]] += 1
        for record in packet["records"]:
            record_appearances[record["record_id"]] += 1
    if any(count != 1 for count in atom_appearances.values()):
        raise ValidationError("Discovery atoms are not assigned exactly once")
    if any(count < 1 for count in record_appearances.values()):
        raise ValidationError("A discovery record is not model-visible")
    manifest = {
        "schema_version": PACKET_SET_SCHEMA,
        "identity": {
            **store["identity"],
            "packet_payload_sha256s": [
                packet["identity"]["packet_payload_sha256"] for packet in packets
            ],
        },
        "coverage": {
            "packet_count": len(packets),
            "store_record_count": len(store["records"]),
            "store_atom_count": len(store["atoms"]),
            "atom_assignment_sha256": canonical_sha256(atom_appearances),
            "record_visibility_sha256": canonical_sha256(record_appearances),
            "all_atoms_assigned_once": True,
            "all_records_visible": True,
            "packet_local_evidence": True,
            "exact_payloads_only": True,
        },
    }
    manifest["identity"]["packet_set_payload_sha256"] = canonical_sha256(manifest)
    return packets, manifest


def build_discovery_packets(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    *,
    options: DiscoveryOptions | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    options = options or DiscoveryOptions()
    ordered_sources = _ordered_sources(sources)
    validate_lane_store(store, ordered_sources, options=options)
    packets, manifest = _build_discovery_packets_unvalidated(store, options)
    validate_discovery_packets(
        store, ordered_sources, packets, manifest, options=options
    )
    return packets, manifest


def validate_discovery_packets(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    packets: list[dict[str, Any]],
    manifest: dict[str, Any],
    *,
    options: DiscoveryOptions | None = None,
) -> None:
    options = options or DiscoveryOptions()
    ordered_sources = _ordered_sources(sources)
    validate_lane_store(store, ordered_sources, options=options)
    expected_packets, expected_manifest = _build_discovery_packets_unvalidated(
        store, options
    )
    if canonical_json_bytes(packets) != canonical_json_bytes(expected_packets):
        raise ValidationError("Discovery packets do not exactly rederive from the store")
    if canonical_json_bytes(manifest) != canonical_json_bytes(expected_manifest):
        raise ValidationError("Discovery packet manifest does not exactly rederive")


def build_rehydration_request(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    packets: list[dict[str, Any]],
    manifest: dict[str, Any],
    *,
    requester_packet_sha256: str,
    record_ids: list[str],
    options: DiscoveryOptions | None = None,
) -> dict[str, Any]:
    options = options or DiscoveryOptions()
    ordered_sources = _ordered_sources(sources)
    validate_discovery_packets(
        store, ordered_sources, packets, manifest, options=options
    )
    packet_hashes = manifest["identity"]["packet_payload_sha256s"]
    if requester_packet_sha256 not in packet_hashes:
        raise ValidationError("Rehydration requester is not in the packet set")
    if (
        not isinstance(record_ids, list)
        or not record_ids
        or any(not isinstance(record_id, str) for record_id in record_ids)
        or record_ids != sorted(record_ids)
        or len(record_ids) != len(set(record_ids))
    ):
        raise ValidationError("Rehydration record_ids must be sorted, unique, and nonempty")
    available = {record["record_id"] for record in store["records"]}
    if any(record_id not in available for record_id in record_ids):
        raise ValidationError("Rehydration request cites an unknown record")
    requester = next(
        packet
        for packet in packets
        if packet["identity"]["packet_payload_sha256"] == requester_packet_sha256
    )
    local_ids = {record["record_id"] for record in requester["records"]}
    if any(record_id in local_ids for record_id in record_ids):
        raise ValidationError("Rehydration may request only records absent from the packet")
    request = {
        "schema_version": REHYDRATION_REQUEST_SCHEMA,
        "identity": {
            "store_payload_sha256": store["identity"]["store_payload_sha256"],
            "packet_set_payload_sha256": manifest["identity"][
                "packet_set_payload_sha256"
            ],
            "requester_packet_sha256": requester_packet_sha256,
        },
        "record_ids": record_ids,
    }
    request["identity"]["request_payload_sha256"] = canonical_sha256(request)
    return request


def fulfill_rehydration_request(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    packets: list[dict[str, Any]],
    manifest: dict[str, Any],
    request: dict[str, Any],
    *,
    options: DiscoveryOptions | None = None,
) -> dict[str, Any]:
    options = options or DiscoveryOptions()
    identity = _dict(request.get("identity"), "rehydration request identity")
    expected_request = build_rehydration_request(
        store,
        sources,
        packets,
        manifest,
        requester_packet_sha256=identity.get("requester_packet_sha256"),
        record_ids=request.get("record_ids"),
        options=options,
    )
    if canonical_json_bytes(request) != canonical_json_bytes(expected_request):
        raise ValidationError("Rehydration request does not exactly rederive")
    records_by_id = {record["record_id"]: record for record in store["records"]}
    records = [records_by_id[record_id] for record_id in request["record_ids"]]
    response = {
        "schema_version": REHYDRATION_RESPONSE_SCHEMA,
        "identity": {
            "store_payload_sha256": store["identity"]["store_payload_sha256"],
            "packet_set_payload_sha256": manifest["identity"][
                "packet_set_payload_sha256"
            ],
            "request_payload_sha256": request["identity"]["request_payload_sha256"],
        },
        "records": records,
        "coverage": {
            "ordered_record_ids": request["record_ids"],
            "records_payload_sha256": canonical_sha256(records),
            "exact_store_records": True,
        },
    }
    response["identity"]["response_payload_sha256"] = canonical_sha256(response)
    if len(canonical_json_bytes(response)) > options.max_packet_bytes:
        raise BudgetError(
            "Rehydration response exceeds the packet byte limit. Nothing was "
            "projected or truncated."
        )
    return response


def validate_rehydration_response(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    packets: list[dict[str, Any]],
    manifest: dict[str, Any],
    request: dict[str, Any],
    response: dict[str, Any],
    *,
    options: DiscoveryOptions | None = None,
) -> None:
    expected = fulfill_rehydration_request(
        store,
        sources,
        packets,
        manifest,
        request,
        options=options,
    )
    if canonical_json_bytes(response) != canonical_json_bytes(expected):
        raise ValidationError("Rehydration response is not exact store material")


def rehydrate_packet_records(
    store: dict[str, Any],
    sources: Iterable[dict[str, Any]],
    packets: list[dict[str, Any]],
    manifest: dict[str, Any],
    request: dict[str, Any],
    packet: dict[str, Any],
    response: dict[str, Any],
    *,
    options: DiscoveryOptions | None = None,
) -> list[dict[str, Any]]:
    options = options or DiscoveryOptions()
    validate_rehydration_response(
        store,
        sources,
        packets,
        manifest,
        request,
        response,
        options=options,
    )
    packet_hash = packet.get("identity", {}).get("packet_payload_sha256")
    if not any(
        canonical_json_bytes(packet) == canonical_json_bytes(expected)
        for expected in packets
    ) or request["identity"]["requester_packet_sha256"] != packet_hash:
        raise ValidationError("Rehydration packet does not match its bound requester")
    records_by_id: dict[str, dict[str, Any]] = {}
    for record in [*packet["records"], *response["records"]]:
        existing = records_by_id.get(record["record_id"])
        if existing is not None and canonical_json_bytes(existing) != canonical_json_bytes(record):
            raise ValidationError("Rehydration attempted conflicting record replacement")
        records_by_id[record["record_id"]] = record
    records = [records_by_id[key] for key in sorted(records_by_id)]
    if len(canonical_json_bytes(records)) > options.max_packet_bytes:
        raise BudgetError(
            "Rehydrated record set exceeds the packet byte limit. Nothing was "
            "projected or truncated."
        )
    return records
