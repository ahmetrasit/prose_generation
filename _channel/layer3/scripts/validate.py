#!/usr/bin/env python3
"""Validate Layer 3 v3 lineage, references, review coverage, and publication."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from common import (
    content_hash,
    load_json,
    resolve_portable_path,
    sha256_file,
    sha256_text,
    source_base,
)


SHA256 = re.compile(r"^[0-9a-f]{64}$")
ID = re.compile(r"^[a-z][a-z0-9-]*$")
AYAH_REF = re.compile(r"^[1-9][0-9]{0,2}:(?:0|[1-9][0-9]*)$")
FORBIDDEN_PROSE = (
    re.compile(r"\broot_[0-9]{6}\b", re.IGNORECASE),
    re.compile(r"\bB[0-9]{3}\b"),
    re.compile(r"\b(?:finding|resonance|activation):[a-z0-9:-]+", re.IGNORECASE),
    re.compile(r"\b(?:channelId|hingeId|sourceSetHash|packetId)\b", re.IGNORECASE),
    re.compile(r"\bLayer [23]\b", re.IGNORECASE),
    re.compile(r"\b(?:schema|prompt|agent)\b", re.IGNORECASE),
)


def is_dict(value: Any) -> bool:
    return isinstance(value, dict)


def is_list(value: Any) -> bool:
    return isinstance(value, list)


def required(value: dict[str, Any], keys: set[str], context: str) -> list[str]:
    return [
        f"{context}: missing required key {key!r}"
        for key in sorted(keys - value.keys())
    ]


def exact_keys(value: dict[str, Any], keys: set[str], context: str) -> list[str]:
    errors = required(value, keys, context)
    errors.extend(
        f"{context}: unsupported key {key!r}"
        for key in sorted(value.keys() - keys)
    )
    return errors


def duplicate_errors(values: list[str], context: str) -> list[str]:
    seen: set[str] = set()
    errors: list[str] = []
    for value in values:
        if value in seen:
            errors.append(f"{context}: duplicate value {value!r}")
        seen.add(value)
    return errors


def source_ids(packet: dict[str, Any]) -> set[str]:
    return {
        item.get("sourceId")
        for item in packet.get("sourceRegistry", [])
        if is_dict(item) and isinstance(item.get("sourceId"), str)
    }


def packet_ayah_refs(packet: dict[str, Any], *, numbered_only: bool = False) -> set[str]:
    refs: set[str] = set()
    for item in packet.get("primaryGround", {}).get("ayahs", []):
        if not is_dict(item) or not isinstance(item.get("ayahRef"), str):
            continue
        if numbered_only and item.get("unitType") != "ayah":
            continue
        refs.add(item["ayahRef"])
    return refs


def primary_refs(packet: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for item in packet.get("primaryGround", {}).get("ayahs", []):
        floor = item.get("floor") if is_dict(item) else None
        if is_dict(floor) and isinstance(floor.get("sourceRef"), str):
            refs.add(floor["sourceRef"])
    return refs


def local_resonance_refs(packet: dict[str, Any]) -> set[str]:
    return {
        record.get("resonanceRef")
        for ayah in packet.get("layer2Handoff", {}).get("ayahs", [])
        if is_dict(ayah)
        for record in ayah.get("localResonances", [])
        if is_dict(record) and isinstance(record.get("resonanceRef"), str)
    }


def activation_refs(packet: dict[str, Any]) -> set[str]:
    return {
        card.get("activationRef")
        for card in packet.get("evidenceField", {}).get("activationCards", [])
        if is_dict(card) and isinstance(card.get("activationRef"), str)
    }


def evidence_refs(packet: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for ayah in packet.get("layer2Handoff", {}).get("ayahs", []):
        if not is_dict(ayah):
            continue
        groups = (
            ("findings", "findingRef"),
            ("localResonances", "resonanceRef"),
            ("boundaries", "boundaryRef"),
        )
        for group, key in groups:
            for record in ayah.get(group, []):
                if is_dict(record) and isinstance(record.get(key), str):
                    refs.add(record[key])
    refs.update(activation_refs(packet))
    refs.update(
        record.get("secondaryRef")
        for record in packet.get("evidenceField", {}).get("secondaryMaterial", [])
        if is_dict(record) and isinstance(record.get("secondaryRef"), str)
    )
    return refs


def known_source_ref(ref: Any, known_sources: set[str]) -> bool:
    return isinstance(ref, str) and source_base(ref) in known_sources


def validate_packet(
    packet: dict[str, Any], *, verify_sources: bool = False
) -> list[str]:
    errors: list[str] = []
    top_keys = {
        "schemaVersion",
        "packetId",
        "runId",
        "packetHash",
        "sourceSetId",
        "sourceSetHash",
        "surah",
        "language",
        "sourceRegistry",
        "primaryGround",
        "layer2Handoff",
        "evidenceField",
        "coverage",
        "warnings",
    }
    errors.extend(exact_keys(packet, top_keys, "packet"))
    if packet.get("schemaVersion") != "layer3-source-packet-v3":
        errors.append("packet: schemaVersion must be layer3-source-packet-v3")
    surah = packet.get("surah")
    language = packet.get("language")
    if not isinstance(surah, int) or not 1 <= surah <= 114:
        errors.append("packet: surah must be an integer from 1 through 114")
    if not isinstance(language, str) or not language:
        errors.append("packet: language must be a non-empty string")
    for key in ("packetHash", "sourceSetHash"):
        if not SHA256.fullmatch(str(packet.get(key, ""))):
            errors.append(f"packet: {key} must be a lowercase SHA-256 digest")

    registry = packet.get("sourceRegistry")
    if not is_list(registry) or not registry:
        errors.append("packet: sourceRegistry must be a non-empty array")
        registry = []
    ids: list[str] = []
    source_set_sources: list[dict[str, Any]] = []
    for index, source in enumerate(registry):
        context = f"packet.sourceRegistry[{index}]"
        if not is_dict(source):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(
                source,
                {
                    "sourceId",
                    "kind",
                    "role",
                    "path",
                    "format",
                    "sha256",
                    "bytes",
                    "projection",
                },
                context,
            )
        )
        source_id = source.get("sourceId")
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{context}: sourceId must be a non-empty string")
            continue
        ids.append(source_id)
        if not SHA256.fullmatch(str(source.get("sha256", ""))):
            errors.append(f"{context}: sha256 must be a lowercase SHA-256 digest")
        if not isinstance(source.get("bytes"), int) or source.get("bytes", -1) < 0:
            errors.append(f"{context}: bytes must be a non-negative integer")
        if source_id in {"quran-text", "primary-floor", "layer2-contract"} or source_id.startswith(
            "layer2-"
        ):
            source_set_sources.append(
                {
                    "sourceId": source_id,
                    "path": source.get("path"),
                    "sha256": source.get("sha256"),
                    "bytes": source.get("bytes"),
                }
            )
        if verify_sources and isinstance(source.get("path"), str):
            path = resolve_portable_path(source["path"])
            if not path.is_file():
                errors.append(f"{context}: source file is missing: {path}")
            else:
                if path.stat().st_size != source.get("bytes"):
                    errors.append(f"{context}: source byte count changed: {path}")
                if sha256_file(path) != source.get("sha256"):
                    errors.append(f"{context}: source hash changed: {path}")
    errors.extend(duplicate_errors(ids, "packet sources"))
    known_sources = set(ids)

    if isinstance(surah, int) and isinstance(language, str):
        expected_source_hash = content_hash(
            {
                "contract": "layer2-handoff-v1",
                "surah": surah,
                "language": language,
                "sources": source_set_sources,
            }
        )
        if packet.get("sourceSetHash") != expected_source_hash:
            errors.append("packet: sourceSetHash does not match the required source manifest")
        expected_packet_hash = content_hash(
            {
                "contract": "layer3-source-packet-v3",
                "surah": surah,
                "language": language,
                "sourceSetHash": packet.get("sourceSetHash"),
                "sources": [
                    {
                        "sourceId": source.get("sourceId"),
                        "sha256": source.get("sha256"),
                        "projection": source.get("projection"),
                    }
                    for source in registry
                    if is_dict(source)
                ],
            }
        )
        if packet.get("packetHash") != expected_packet_hash:
            errors.append("packet: packetHash does not match the packet source manifest")
        expected_run = f"s{surah:03d}-{language}-l3v3-{expected_packet_hash[:16]}"
        if packet.get("packetId") != expected_run or packet.get("runId") != expected_run:
            errors.append("packet: packetId/runId do not match packetHash lineage")

    primary = packet.get("primaryGround")
    if not is_dict(primary):
        errors.append("packet.primaryGround: must be an object")
        primary = {}
    else:
        errors.extend(
            exact_keys(
                primary,
                {"quranSourceRef", "floorSourceRef", "ayahs"},
                "packet.primaryGround",
            )
        )
        for key in ("quranSourceRef", "floorSourceRef"):
            if not known_source_ref(primary.get(key), known_sources):
                errors.append(f"packet.primaryGround: unknown {key}")
    ayahs = primary.get("ayahs")
    if not is_list(ayahs) or not ayahs:
        errors.append("packet.primaryGround.ayahs: must be a non-empty array")
        ayahs = []
    ayah_refs: list[str] = []
    numbered_refs: set[str] = set()
    for index, ayah in enumerate(ayahs):
        context = f"packet.primaryGround.ayahs[{index}]"
        if not is_dict(ayah):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(ayah, {"ayahRef", "unitType", "arabic", "floor"}, context)
        )
        ayah_ref = ayah.get("ayahRef")
        if not isinstance(ayah_ref, str) or not AYAH_REF.fullmatch(ayah_ref):
            errors.append(f"{context}: invalid ayahRef")
        else:
            ayah_refs.append(ayah_ref)
        unit_type = ayah.get("unitType")
        floor = ayah.get("floor")
        if unit_type == "ayah":
            if isinstance(ayah_ref, str):
                numbered_refs.add(ayah_ref)
            if not is_dict(floor):
                errors.append(f"{context}: numbered ayah requires a typed floor")
            else:
                errors.extend(exact_keys(floor, {"text", "sourceRef"}, f"{context}.floor"))
                if not str(floor.get("text", "")).strip():
                    errors.append(f"{context}.floor: text must be non-empty")
                if not known_source_ref(floor.get("sourceRef"), known_sources):
                    errors.append(f"{context}.floor: unknown sourceRef")
        elif unit_type == "basmala":
            if floor is not None:
                errors.append(f"{context}: basmala floor must be null")
        else:
            errors.append(f"{context}: unsupported unitType {unit_type!r}")
    errors.extend(duplicate_errors(ayah_refs, "packet primary ayahs"))

    handoff = packet.get("layer2Handoff")
    if not is_dict(handoff):
        errors.append("packet.layer2Handoff: must be an object")
        handoff = {}
    else:
        errors.extend(
            exact_keys(
                handoff,
                {
                    "schemaVersion",
                    "sourceSetId",
                    "sourceSetHash",
                    "contractSourceRef",
                    "ayahs",
                },
                "packet.layer2Handoff",
            )
        )
        if handoff.get("schemaVersion") != "layer2-handoff-v1":
            errors.append("packet.layer2Handoff: unsupported schemaVersion")
        if handoff.get("sourceSetId") != packet.get("sourceSetId"):
            errors.append("packet.layer2Handoff: sourceSetId lineage mismatch")
        if handoff.get("sourceSetHash") != packet.get("sourceSetHash"):
            errors.append("packet.layer2Handoff: sourceSetHash lineage mismatch")
        if not known_source_ref(handoff.get("contractSourceRef"), known_sources):
            errors.append("packet.layer2Handoff: unknown contractSourceRef")
    handoff_ayahs = handoff.get("ayahs")
    if not is_list(handoff_ayahs):
        errors.append("packet.layer2Handoff.ayahs: must be an array")
        handoff_ayahs = []
    handoff_refs: list[str] = []
    record_refs: list[str] = []
    for index, ayah in enumerate(handoff_ayahs):
        context = f"packet.layer2Handoff.ayahs[{index}]"
        if not is_dict(ayah):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(
                ayah,
                {
                    "ayahRef",
                    "artifactSetLabel",
                    "artifactRefs",
                    "findings",
                    "localResonances",
                    "boundaries",
                },
                context,
            )
        )
        ayah_ref = ayah.get("ayahRef")
        if isinstance(ayah_ref, str):
            handoff_refs.append(ayah_ref)
        artifacts = ayah.get("artifactRefs")
        expected_artifacts = {"prose", "evidence", "index", "friction"}
        if not is_dict(artifacts):
            errors.append(f"{context}.artifactRefs: must be an object")
        else:
            errors.extend(exact_keys(artifacts, expected_artifacts, f"{context}.artifactRefs"))
            for kind, ref in artifacts.items():
                if not known_source_ref(ref, known_sources):
                    errors.append(f"{context}.artifactRefs.{kind}: unknown source")
        findings = ayah.get("findings")
        if not is_list(findings) or not findings:
            errors.append(f"{context}.findings: must be a non-empty array")
            findings = []
        finding_refs: set[str] = set()
        for finding_index, finding in enumerate(findings):
            finding_context = f"{context}.findings[{finding_index}]"
            if not is_dict(finding):
                errors.append(f"{finding_context}: must be an object")
                continue
            errors.extend(
                exact_keys(
                    finding,
                    {"findingRef", "indexKey", "text", "inference", "sourceRefs"},
                    finding_context,
                )
            )
            finding_ref = finding.get("findingRef")
            if isinstance(finding_ref, str):
                record_refs.append(finding_ref)
                finding_refs.add(finding_ref)
            if not str(finding.get("text", "")).strip():
                errors.append(f"{finding_context}: text must be non-empty")
            refs = finding.get("sourceRefs")
            if not is_list(refs) or not refs or any(
                not known_source_ref(ref, known_sources) for ref in refs
            ):
                errors.append(f"{finding_context}: sourceRefs must resolve")
        resonances = ayah.get("localResonances")
        if not is_list(resonances):
            errors.append(f"{context}.localResonances: must be an array")
            resonances = []
        for resonance_index, resonance in enumerate(resonances):
            resonance_context = f"{context}.localResonances[{resonance_index}]"
            if not is_dict(resonance):
                errors.append(f"{resonance_context}: must be an object")
                continue
            errors.extend(
                exact_keys(
                    resonance,
                    {
                        "resonanceRef",
                        "findingRef",
                        "text",
                        "primaryRelation",
                        "sourceRefs",
                    },
                    resonance_context,
                )
            )
            resonance_ref = resonance.get("resonanceRef")
            if isinstance(resonance_ref, str):
                record_refs.append(resonance_ref)
            if resonance.get("findingRef") not in finding_refs:
                errors.append(f"{resonance_context}: findingRef does not resolve locally")
            if resonance.get("primaryRelation") not in {
                "supports-primary",
                "shifts-primary",
            }:
                errors.append(f"{resonance_context}: invalid primaryRelation")
        boundaries = ayah.get("boundaries")
        if not is_list(boundaries):
            errors.append(f"{context}.boundaries: must be an array")
            boundaries = []
        for boundary_index, boundary in enumerate(boundaries):
            boundary_context = f"{context}.boundaries[{boundary_index}]"
            if not is_dict(boundary):
                errors.append(f"{boundary_context}: must be an object")
                continue
            errors.extend(
                exact_keys(
                    boundary,
                    {"boundaryRef", "ayahRefs", "text", "sourceRefs"},
                    boundary_context,
                )
            )
            if isinstance(boundary.get("boundaryRef"), str):
                record_refs.append(boundary["boundaryRef"])
    errors.extend(duplicate_errors(handoff_refs, "Layer-2 handoff ayahs"))
    if set(handoff_refs) != numbered_refs:
        errors.append("packet.layer2Handoff: must contain exactly one record per numbered ayah")
    errors.extend(duplicate_errors(record_refs, "Layer-2 handoff records"))

    evidence = packet.get("evidenceField")
    if not is_dict(evidence):
        errors.append("packet.evidenceField: must be an object")
        evidence = {}
    else:
        errors.extend(
            exact_keys(
                evidence,
                {"activationCards", "secondaryMaterial"},
                "packet.evidenceField",
            )
        )
    other_refs: list[str] = []
    for group, key in (("activationCards", "activationRef"), ("secondaryMaterial", "secondaryRef")):
        records = evidence.get(group)
        if not is_list(records):
            errors.append(f"packet.evidenceField.{group}: must be an array")
            continue
        for index, record in enumerate(records):
            context = f"packet.evidenceField.{group}[{index}]"
            if not is_dict(record):
                errors.append(f"{context}: must be an object")
                continue
            ref = record.get(key)
            if isinstance(ref, str):
                other_refs.append(ref)
            refs = record.get("sourceRefs")
            if not is_list(refs) or not refs or any(
                not known_source_ref(item, known_sources) for item in refs
            ):
                errors.append(f"{context}: sourceRefs must resolve")
            if group == "activationCards":
                ayah_values = record.get("ayahRefs")
                if not is_list(ayah_values) or not ayah_values:
                    errors.append(f"{context}: ayahRefs must be non-empty")
                elif any(item not in numbered_refs for item in ayah_values):
                    errors.append(f"{context}: ayahRefs leave this surah")
    errors.extend(duplicate_errors(other_refs, "packet evidence records"))

    coverage = packet.get("coverage")
    if not is_dict(coverage):
        errors.append("packet.coverage: must be an object")
    else:
        expected_coverage = {"quranText", "primaryFloor", "layer2", "networkV3", "v11"}
        errors.extend(exact_keys(coverage, expected_coverage, "packet.coverage"))
        for key in ("quranText", "primaryFloor", "layer2"):
            if is_dict(coverage.get(key)) and coverage[key].get("status") != "complete":
                errors.append(f"packet.coverage.{key}: required coverage must be complete")
    return errors


def validate_hypotheses(
    hypotheses: dict[str, Any], packet: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    errors.extend(
        exact_keys(
            hypotheses,
            {
                "schemaVersion",
                "packetId",
                "sourceSetHash",
                "surah",
                "language",
                "hypotheses",
            },
            "hypotheses",
        )
    )
    if hypotheses.get("schemaVersion") != "layer3-discovery-hypotheses-v2":
        errors.append("hypotheses: unsupported schemaVersion")
    for key in ("packetId", "sourceSetHash", "surah", "language"):
        if hypotheses.get(key) != packet.get(key):
            errors.append(f"hypotheses: {key} does not match packet")
    records = hypotheses.get("hypotheses")
    if not is_list(records):
        errors.append("hypotheses: hypotheses must be an array")
        return errors
    known_ayahs = packet_ayah_refs(packet, numbered_only=True)
    known_cards = activation_refs(packet)
    hypothesis_ids: list[str] = []
    for index, record in enumerate(records):
        context = f"hypotheses.hypotheses[{index}]"
        if not is_dict(record):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(
                record,
                {
                    "hypothesisId",
                    "proposedOperation",
                    "readerShift",
                    "rhetoricalReach",
                    "activationCardRefs",
                },
                context,
            )
        )
        hypothesis_id = record.get("hypothesisId")
        if not isinstance(hypothesis_id, str) or not ID.fullmatch(hypothesis_id):
            errors.append(f"{context}: invalid hypothesisId")
        else:
            hypothesis_ids.append(hypothesis_id)
        shift = record.get("readerShift")
        if not is_dict(shift):
            errors.append(f"{context}.readerShift: must be an object")
        else:
            errors.extend(
                exact_keys(shift, {"before", "hinge", "after"}, f"{context}.readerShift")
            )
            if any(not str(shift.get(key, "")).strip() for key in ("before", "hinge", "after")):
                errors.append(f"{context}.readerShift: all fields must be non-empty")
        reach = record.get("rhetoricalReach")
        reached_ayahs: set[str] = set()
        if not is_list(reach) or not reach:
            errors.append(f"{context}.rhetoricalReach: must be a non-empty array")
        else:
            for movement_index, movement in enumerate(reach):
                movement_context = f"{context}.rhetoricalReach[{movement_index}]"
                if not is_dict(movement):
                    errors.append(f"{movement_context}: must be an object")
                    continue
                errors.extend(
                    exact_keys(movement, {"movement", "ayahRefs"}, movement_context)
                )
                refs = movement.get("ayahRefs")
                if not is_list(refs) or not refs:
                    errors.append(f"{movement_context}.ayahRefs: must be non-empty")
                    continue
                for ref in refs:
                    if ref not in known_ayahs:
                        errors.append(f"{movement_context}: unknown ayahRef {ref!r}")
                    elif isinstance(ref, str):
                        reached_ayahs.add(ref)
        if len(reached_ayahs) < 2:
            errors.append(f"{context}: a Layer-3 hypothesis must cross at least two ayahs")
        cards = record.get("activationCardRefs")
        if not is_list(cards):
            errors.append(f"{context}.activationCardRefs: must be an array")
        else:
            for ref in cards:
                if ref not in known_cards:
                    errors.append(f"{context}: unknown activationCardRef {ref!r}")
    errors.extend(duplicate_errors(hypothesis_ids, "discovery hypotheses"))
    return errors


def required_review_input_refs(
    packet: dict[str, Any], hypotheses: dict[str, Any]
) -> set[str]:
    refs = {
        f"hypothesis:{record.get('hypothesisId')}"
        for record in hypotheses.get("hypotheses", [])
        if is_dict(record) and isinstance(record.get("hypothesisId"), str)
    }
    refs.update(local_resonance_refs(packet))
    return refs


def validate_briefs(
    briefs: dict[str, Any],
    packet: dict[str, Any],
    hypotheses: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    errors.extend(
        exact_keys(
            briefs,
            {
                "schemaVersion",
                "briefId",
                "packetId",
                "sourceSetHash",
                "surah",
                "language",
                "primaryArgument",
                "requiredReviewInputRefs",
                "channels",
                "nonChannelDispositions",
            },
            "briefs",
        )
    )
    if briefs.get("schemaVersion") != "layer3-channel-briefs-v2":
        errors.append("briefs: unsupported schemaVersion")
    for key in ("packetId", "sourceSetHash", "surah", "language"):
        if briefs.get(key) != packet.get(key):
            errors.append(f"briefs: {key} does not match packet")
    expected_brief_id = f"{packet.get('runId')}-briefs-v2"
    if briefs.get("briefId") != expected_brief_id:
        errors.append("briefs: briefId does not match packet run lineage")

    known_primary = primary_refs(packet)
    argument = briefs.get("primaryArgument")
    if not is_dict(argument):
        errors.append("briefs.primaryArgument: must be an object")
    else:
        errors.extend(
            exact_keys(
                argument,
                {"thesis", "development", "surfaceFloorRefs"},
                "briefs.primaryArgument",
            )
        )
        if not str(argument.get("thesis", "")).strip() or not str(
            argument.get("development", "")
        ).strip():
            errors.append("briefs.primaryArgument: thesis and development must be non-empty")
        refs = argument.get("surfaceFloorRefs")
        if not is_list(refs) or not refs:
            errors.append("briefs.primaryArgument.surfaceFloorRefs: must be non-empty")
        elif any(ref not in known_primary for ref in refs):
            errors.append("briefs.primaryArgument.surfaceFloorRefs: unknown primary ref")

    required_inputs = required_review_input_refs(packet, hypotheses)
    echoed_inputs = briefs.get("requiredReviewInputRefs")
    if not is_list(echoed_inputs):
        errors.append("briefs.requiredReviewInputRefs: must be an array")
        echoed_inputs = []
    errors.extend(duplicate_errors([str(item) for item in echoed_inputs], "review input refs"))
    if set(echoed_inputs) != required_inputs:
        errors.append("briefs.requiredReviewInputRefs: must exactly echo all hypotheses and local resonances")

    known_evidence = evidence_refs(packet)
    channels = briefs.get("channels")
    if not is_list(channels):
        errors.append("briefs.channels: must be an array")
        channels = []
    channel_ids: list[str] = []
    hinge_ids: list[str] = []
    used_inputs: set[str] = set()
    channel_evidence: dict[str, set[str]] = {}
    hinge_evidence: dict[str, set[str]] = {}
    for index, channel in enumerate(channels):
        context = f"briefs.channels[{index}]"
        if not is_dict(channel):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(
                channel,
                {
                    "channelId",
                    "readerName",
                    "inputRefs",
                    "surfaceFloorRefs",
                    "surfaceFloor",
                    "hinges",
                    "crossAyahOperation",
                    "readerShift",
                    "indispensableGain",
                },
                context,
            )
        )
        channel_id = channel.get("channelId")
        if not isinstance(channel_id, str) or not ID.fullmatch(channel_id):
            errors.append(f"{context}: invalid channelId")
            channel_id = f"invalid-{index}"
        else:
            channel_ids.append(channel_id)
        for key in ("readerName", "surfaceFloor", "crossAyahOperation", "indispensableGain"):
            if not str(channel.get(key, "")).strip():
                errors.append(f"{context}.{key}: must be non-empty")
        inputs = channel.get("inputRefs")
        if not is_list(inputs) or not inputs:
            errors.append(f"{context}.inputRefs: must be non-empty")
            inputs = []
        for ref in inputs:
            if ref not in required_inputs:
                errors.append(f"{context}: unknown inputRef {ref!r}")
            elif isinstance(ref, str):
                used_inputs.add(ref)
        floor_refs = channel.get("surfaceFloorRefs")
        if not is_list(floor_refs) or not floor_refs:
            errors.append(f"{context}.surfaceFloorRefs: must be non-empty")
        elif any(ref not in known_primary for ref in floor_refs):
            errors.append(f"{context}.surfaceFloorRefs: unknown primary ref")
        shift = channel.get("readerShift")
        if not is_dict(shift):
            errors.append(f"{context}.readerShift: must be an object")
        else:
            errors.extend(exact_keys(shift, {"before", "after"}, f"{context}.readerShift"))
            if any(not str(shift.get(key, "")).strip() for key in ("before", "after")):
                errors.append(f"{context}.readerShift: fields must be non-empty")
        hinges = channel.get("hinges")
        if not is_list(hinges) or not hinges:
            errors.append(f"{context}.hinges: must be non-empty")
            hinges = []
        reached_ayahs: set[str] = set()
        channel_refs: set[str] = set()
        for hinge_index, hinge in enumerate(hinges):
            hinge_context = f"{context}.hinges[{hinge_index}]"
            if not is_dict(hinge):
                errors.append(f"{hinge_context}: must be an object")
                continue
            errors.extend(
                exact_keys(
                    hinge,
                    {
                        "hingeId",
                        "contribution",
                        "inputRefs",
                        "ayahRefs",
                        "evidenceRefs",
                        "claimPolicy",
                    },
                    hinge_context,
                )
            )
            hinge_id = hinge.get("hingeId")
            if not isinstance(hinge_id, str) or not ID.fullmatch(hinge_id):
                errors.append(f"{hinge_context}: invalid hingeId")
                hinge_id = f"invalid-hinge-{index}-{hinge_index}"
            else:
                hinge_ids.append(hinge_id)
            if not str(hinge.get("contribution", "")).strip():
                errors.append(f"{hinge_context}.contribution: must be non-empty")
            hinge_inputs = hinge.get("inputRefs")
            if not is_list(hinge_inputs) or not hinge_inputs:
                errors.append(f"{hinge_context}.inputRefs: must be non-empty")
                hinge_inputs = []
            elif any(ref not in inputs for ref in hinge_inputs):
                errors.append(f"{hinge_context}.inputRefs: must be channel inputRefs")
            ayah_values = hinge.get("ayahRefs")
            if not is_list(ayah_values) or not ayah_values:
                errors.append(f"{hinge_context}.ayahRefs: must be non-empty")
            else:
                for ref in ayah_values:
                    if ref not in packet_ayah_refs(packet, numbered_only=True):
                        errors.append(f"{hinge_context}: unknown ayahRef {ref!r}")
                    elif isinstance(ref, str):
                        reached_ayahs.add(ref)
            refs = hinge.get("evidenceRefs")
            if not is_list(refs) or not refs:
                errors.append(f"{hinge_context}.evidenceRefs: must be non-empty")
                refs = []
            for ref in refs:
                if ref not in known_evidence:
                    errors.append(f"{hinge_context}: unknown evidenceRef {ref!r}")
                elif isinstance(ref, str):
                    channel_refs.add(ref)
            resonance_values = [
                ref for ref in refs if isinstance(ref, str) and ref.startswith("resonance:")
            ]
            for resonance_ref in resonance_values:
                parts = resonance_ref.split(":")
                prefix = f"finding:{parts[1]}:{parts[2]}:" if len(parts) >= 4 else ""
                if not prefix or not any(
                    isinstance(ref, str) and ref.startswith(prefix) for ref in refs
                ):
                    errors.append(
                        f"{hinge_context}: local resonance {resonance_ref!r} requires "
                        "an exact supporting finding from the same ayah"
                    )
            policy = hinge.get("claimPolicy")
            if not is_dict(policy):
                errors.append(f"{hinge_context}.claimPolicy: must be an object")
            else:
                errors.extend(
                    exact_keys(
                        policy,
                        {
                            "scope",
                            "permittedForm",
                            "counterpressureRefs",
                            "prohibitedClaims",
                        },
                        f"{hinge_context}.claimPolicy",
                    )
                )
                if policy.get("scope") not in {"direct", "bounded"}:
                    errors.append(f"{hinge_context}.claimPolicy: invalid scope")
                if not str(policy.get("permittedForm", "")).strip():
                    errors.append(f"{hinge_context}.claimPolicy: permittedForm is required")
                counter_refs = policy.get("counterpressureRefs")
                if not is_list(counter_refs):
                    errors.append(f"{hinge_context}.claimPolicy.counterpressureRefs: must be an array")
                elif any(ref not in known_evidence for ref in counter_refs):
                    errors.append(f"{hinge_context}.claimPolicy: unknown counterpressureRef")
                if not is_list(policy.get("prohibitedClaims")):
                    errors.append(f"{hinge_context}.claimPolicy.prohibitedClaims: must be an array")
            hinge_evidence[hinge_id] = set(refs)
        if len(reached_ayahs) < 2:
            errors.append(f"{context}: an accepted channel must span at least two ayahs")
        channel_evidence[channel_id] = channel_refs
    errors.extend(duplicate_errors(channel_ids, "channel briefs"))
    errors.extend(duplicate_errors(hinge_ids, "channel hinges"))

    dispositions = briefs.get("nonChannelDispositions")
    if not is_list(dispositions):
        errors.append("briefs.nonChannelDispositions: must be an array")
        dispositions = []
    disposition_inputs: list[str] = []
    allowed_reasons = {
        "local-only",
        "primary-derived",
        "duplicate",
        "fails-latent-dependence",
        "fails-reader-payoff",
        "unsupported",
    }
    for index, disposition in enumerate(dispositions):
        context = f"briefs.nonChannelDispositions[{index}]"
        if not is_dict(disposition):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(disposition, {"inputRef", "reason", "explanation"}, context)
        )
        input_ref = disposition.get("inputRef")
        if input_ref not in required_inputs:
            errors.append(f"{context}: unknown inputRef {input_ref!r}")
        elif isinstance(input_ref, str):
            disposition_inputs.append(input_ref)
        if disposition.get("reason") not in allowed_reasons:
            errors.append(f"{context}: invalid non-channel reason")
        if not str(disposition.get("explanation", "")).strip():
            errors.append(f"{context}.explanation: must be non-empty")
    errors.extend(duplicate_errors(disposition_inputs, "non-channel dispositions"))
    disposed = set(disposition_inputs)
    overlap = used_inputs & disposed
    if overlap:
        errors.append(
            "briefs: inputs used by a channel cannot also receive a non-channel "
            f"disposition: {', '.join(sorted(overlap))}"
        )
    unaccounted = required_inputs - used_inputs - disposed
    if unaccounted:
        errors.append(
            "briefs: every discovery hypothesis and local resonance must be used "
            "or receive one non-channel disposition: " + ", ".join(sorted(unaccounted))
        )
    return errors


def validate_unique_span(prose: str, span: Any, context: str) -> list[str]:
    if not isinstance(span, str) or not span.strip():
        return [f"{context}: span must be a non-empty string"]
    count = prose.count(span)
    if count != 1:
        return [f"{context}: span must occur exactly once in prose; found {count}"]
    return []


def validate_composition(
    composition: dict[str, Any],
    packet: dict[str, Any],
    briefs: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    errors.extend(
        exact_keys(
            composition,
            {
                "schemaVersion",
                "compositionId",
                "packetId",
                "briefId",
                "sourceSetHash",
                "surah",
                "language",
                "prose",
                "evidenceMap",
                "friction",
            },
            "composition",
        )
    )
    if composition.get("schemaVersion") != "layer3-surah-composition-v1":
        errors.append("composition: unsupported schemaVersion")
    for key in ("packetId", "sourceSetHash", "surah", "language"):
        if composition.get(key) != packet.get(key):
            errors.append(f"composition: {key} does not match packet")
    if composition.get("briefId") != briefs.get("briefId"):
        errors.append("composition: briefId does not match channel briefs")
    expected_id = f"{packet.get('runId')}-composition-v1"
    if composition.get("compositionId") != expected_id:
        errors.append("composition: compositionId does not match packet lineage")
    prose = composition.get("prose")
    if not isinstance(prose, str) or not prose.strip():
        errors.append("composition.prose: must be non-empty")
        prose = ""
    for pattern in FORBIDDEN_PROSE:
        match = pattern.search(prose)
        if match:
            errors.append(f"composition.prose: apparatus term {match.group(0)!r} is forbidden")

    channels = {
        item.get("channelId"): item
        for item in briefs.get("channels", [])
        if is_dict(item) and isinstance(item.get("channelId"), str)
    }
    hinges = {
        hinge.get("hingeId"): hinge
        for channel in briefs.get("channels", [])
        if is_dict(channel)
        for hinge in channel.get("hinges", [])
        if is_dict(hinge) and isinstance(hinge.get("hingeId"), str)
    }
    evidence_map = composition.get("evidenceMap")
    if not is_dict(evidence_map):
        errors.append("composition.evidenceMap: must be an object")
        evidence_map = {}
    else:
        errors.extend(
            exact_keys(
                evidence_map,
                {"primaryClaims", "channelLandings", "hingeLandings"},
                "composition.evidenceMap",
            )
        )
    primary_claims = evidence_map.get("primaryClaims")
    if not is_list(primary_claims):
        errors.append("composition.evidenceMap.primaryClaims: must be an array")
        primary_claims = []
    claim_ids: list[str] = []
    known_primary = primary_refs(packet)
    for index, claim in enumerate(primary_claims):
        context = f"composition.evidenceMap.primaryClaims[{index}]"
        if not is_dict(claim):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(claim, {"claimId", "ayahRefs", "span", "sourceRefs"}, context)
        )
        if isinstance(claim.get("claimId"), str):
            claim_ids.append(claim["claimId"])
        errors.extend(validate_unique_span(prose, claim.get("span"), f"{context}.span"))
        refs = claim.get("sourceRefs")
        if not is_list(refs) or not refs or any(ref not in known_primary for ref in refs):
            errors.append(f"{context}.sourceRefs: must resolve to the typed primary floor")
    errors.extend(duplicate_errors(claim_ids, "composition primary claims"))

    channel_landings = evidence_map.get("channelLandings")
    if not is_list(channel_landings):
        errors.append("composition.evidenceMap.channelLandings: must be an array")
        channel_landings = []
    landed_channels: list[str] = []
    for index, landing in enumerate(channel_landings):
        context = f"composition.evidenceMap.channelLandings[{index}]"
        if not is_dict(landing):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            exact_keys(
                landing,
                {"channelId", "operationSpan", "gainSpan", "evidenceRefs"},
                context,
            )
        )
        channel_id = landing.get("channelId")
        if channel_id not in channels:
            errors.append(f"{context}: unknown channelId {channel_id!r}")
            continue
        landed_channels.append(channel_id)
        errors.extend(
            validate_unique_span(prose, landing.get("operationSpan"), f"{context}.operationSpan")
        )
        errors.extend(validate_unique_span(prose, landing.get("gainSpan"), f"{context}.gainSpan"))
        allowed = {
            ref
            for hinge in channels[channel_id].get("hinges", [])
            if is_dict(hinge)
            for ref in hinge.get("evidenceRefs", [])
            if isinstance(ref, str)
        }
        refs = landing.get("evidenceRefs")
        if not is_list(refs) or not refs or any(ref not in allowed for ref in refs):
            errors.append(f"{context}.evidenceRefs: must resolve within the channel")
    errors.extend(duplicate_errors(landed_channels, "composition channel landings"))
    if set(landed_channels) != set(channels):
        errors.append("composition: every admitted channel needs exactly one reader-visible landing")

    hinge_landings = evidence_map.get("hingeLandings")
    if not is_list(hinge_landings):
        errors.append("composition.evidenceMap.hingeLandings: must be an array")
        hinge_landings = []
    landed_hinges: list[str] = []
    for index, landing in enumerate(hinge_landings):
        context = f"composition.evidenceMap.hingeLandings[{index}]"
        if not is_dict(landing):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(exact_keys(landing, {"hingeId", "span", "evidenceRefs"}, context))
        hinge_id = landing.get("hingeId")
        if hinge_id not in hinges:
            errors.append(f"{context}: unknown hingeId {hinge_id!r}")
            continue
        landed_hinges.append(hinge_id)
        errors.extend(validate_unique_span(prose, landing.get("span"), f"{context}.span"))
        allowed = set(hinges[hinge_id].get("evidenceRefs", []))
        refs = landing.get("evidenceRefs")
        if not is_list(refs) or not refs or any(ref not in allowed for ref in refs):
            errors.append(f"{context}.evidenceRefs: must resolve within the hinge")
        policy = hinges[hinge_id].get("claimPolicy", {})
        for prohibited in policy.get("prohibitedClaims", []):
            if isinstance(prohibited, str) and prohibited.strip() and prohibited.casefold() in prose.casefold():
                errors.append(f"composition.prose: contains prohibited claim from hinge {hinge_id!r}")
    errors.extend(duplicate_errors(landed_hinges, "composition hinge landings"))
    if set(landed_hinges) != set(hinges):
        errors.append("composition: every admitted hinge needs exactly one reader-visible landing")

    friction = composition.get("friction")
    if not is_list(friction):
        errors.append("composition.friction: must be an array")
    else:
        for index, item in enumerate(friction):
            context = f"composition.friction[{index}]"
            if not is_dict(item):
                errors.append(f"{context}: must be an object")
                continue
            errors.extend(exact_keys(item, {"code", "detail"}, context))
            if not str(item.get("code", "")).strip() or not str(item.get("detail", "")).strip():
                errors.append(f"{context}: code and detail must be non-empty")
    return errors


def publication_evidence(
    composition: dict[str, Any], packet: dict[str, Any], briefs: dict[str, Any]
) -> dict[str, Any]:
    return {
        "schemaVersion": "layer3-surah-reading-evidence-v1",
        "packetId": packet["packetId"],
        "briefId": briefs["briefId"],
        "compositionId": composition["compositionId"],
        "sourceSetHash": packet["sourceSetHash"],
        "surah": packet["surah"],
        "language": packet["language"],
        "proseSha256": sha256_text(composition["prose"]),
        **composition["evidenceMap"],
    }


def validate_publication_evidence(
    evidence: dict[str, Any], prose: str, composition: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    if evidence.get("schemaVersion") != "layer3-surah-reading-evidence-v1":
        errors.append("publication evidence: unsupported schemaVersion")
    if evidence.get("proseSha256") != sha256_text(prose):
        errors.append("publication evidence: proseSha256 does not match prose")
    for key in ("packetId", "briefId", "compositionId", "sourceSetHash", "surah", "language"):
        if evidence.get(key) != composition.get(key):
            errors.append(f"publication evidence: {key} lineage mismatch")
    for key in ("primaryClaims", "channelLandings", "hingeLandings"):
        if evidence.get(key) != composition.get("evidenceMap", {}).get(key):
            errors.append(f"publication evidence: {key} differs from composition")
    return errors


def report(errors: list[str]) -> int:
    if not errors:
        print("ok")
        return 0
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    packet_parser = subparsers.add_parser("packet")
    packet_parser.add_argument("artifact", type=Path)
    packet_parser.add_argument("--verify-sources", action="store_true")
    hypotheses_parser = subparsers.add_parser("hypotheses")
    hypotheses_parser.add_argument("artifact", type=Path)
    hypotheses_parser.add_argument("--packet", required=True, type=Path)
    briefs_parser = subparsers.add_parser("briefs")
    briefs_parser.add_argument("artifact", type=Path)
    briefs_parser.add_argument("--packet", required=True, type=Path)
    briefs_parser.add_argument("--hypotheses", required=True, type=Path)
    composition_parser = subparsers.add_parser("composition")
    composition_parser.add_argument("artifact", type=Path)
    composition_parser.add_argument("--packet", required=True, type=Path)
    composition_parser.add_argument("--briefs", required=True, type=Path)
    args = parser.parse_args()

    if args.command == "packet":
        return report(validate_packet(load_json(args.artifact), verify_sources=args.verify_sources))
    packet = load_json(args.packet)
    if args.command == "hypotheses":
        return report(validate_hypotheses(load_json(args.artifact), packet))
    if args.command == "briefs":
        return report(
            validate_briefs(
                load_json(args.artifact), packet, load_json(args.hypotheses)
            )
        )
    return report(
        validate_composition(
            load_json(args.artifact), packet, load_json(args.briefs)
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
