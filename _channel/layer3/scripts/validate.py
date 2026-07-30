#!/usr/bin/env python3
"""Validate the functional contracts of Layer 3 workflow artifacts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from common import (
    load_json,
    require_keys,
    source_base,
    unique_values,
)


FORBIDDEN_PROSE = (
    re.compile(r"\broot_[0-9]{6}\b", re.IGNORECASE),
    re.compile(r"\bB[0-9]{3}\b"),
    re.compile(r"\b(?:C|F|PF)[0-9]{3,4}\b"),
    re.compile(r"\bnetwork[- ]?v3\b", re.IGNORECASE),
    re.compile(r"\bv1[12]\b", re.IGNORECASE),
    re.compile(r"\bLayer 2\b", re.IGNORECASE),
    re.compile(r"\b(?:schema|prompt|agent)\b", re.IGNORECASE),
)


def is_dict(value: Any) -> bool:
    return isinstance(value, dict)


def is_list(value: Any) -> bool:
    return isinstance(value, list)


def source_ids(packet: dict[str, Any]) -> set[str]:
    return {
        item.get("sourceId")
        for item in packet.get("sourceRegistry", [])
        if isinstance(item, dict) and isinstance(item.get("sourceId"), str)
    }


def check_source_refs(
    refs: Any, known_sources: set[str], context: str
) -> list[str]:
    if not is_list(refs) or not refs:
        return [f"{context}: sourceRefs must be a non-empty array"]
    errors = []
    for ref in refs:
        if not isinstance(ref, str):
            errors.append(f"{context}: source ref must be a string")
        elif source_base(ref) not in known_sources:
            errors.append(f"{context}: unknown source ref {ref!r}")
    return errors


def validate_packet(packet: dict[str, Any]) -> list[str]:
    errors = require_keys(
        packet,
        {
            "schemaVersion",
            "packetId",
            "surah",
            "language",
            "sourceRegistry",
            "primaryGround",
            "evidenceField",
            "coverage",
            "warnings",
        },
        "packet",
    )
    if packet.get("schemaVersion") != "layer3-source-packet-v2":
        errors.append("packet: unsupported schemaVersion")
    sources = packet.get("sourceRegistry")
    if not is_list(sources) or not sources:
        errors.append("packet: sourceRegistry must be a non-empty array")
        sources = []
    ids = [
        item.get("sourceId")
        for item in sources
        if is_dict(item) and isinstance(item.get("sourceId"), str)
    ]
    errors.extend(unique_values(ids, "packet sources"))
    required_source_keys = {
        "sourceId",
        "kind",
        "role",
        "path",
        "format",
        "projection",
    }
    for index, source in enumerate(sources):
        if not is_dict(source):
            errors.append(f"packet sourceRegistry[{index}]: must be an object")
            continue
        errors.extend(
            require_keys(
                source,
                required_source_keys,
                f"packet sourceRegistry[{index}]",
            )
        )
    known_sources = set(ids)
    primary = packet.get("primaryGround")
    if not is_dict(primary):
        errors.append("packet: primaryGround must be an object")
        primary = {}
    else:
        errors.extend(
            require_keys(primary, {"sourceRefs", "ayahs"}, "packet primaryGround")
        )
        errors.extend(
            check_source_refs(
                primary.get("sourceRefs"),
                known_sources,
                "packet primaryGround",
            )
        )
    ayahs = primary.get("ayahs")
    if not is_list(ayahs) or not ayahs:
        errors.append("packet primaryGround: ayahs must be a non-empty array")
        ayahs = []
    ayah_refs = []
    for index, ayah in enumerate(ayahs):
        if not is_dict(ayah):
            errors.append(f"packet primaryGround.ayahs[{index}]: must be an object")
            continue
        context = f"packet primaryGround.ayahs[{index}]"
        errors.extend(
            require_keys(
                ayah,
                {"ayahRef", "unitType", "arabic", "reading"},
                context,
            )
        )
        if isinstance(ayah.get("ayahRef"), str):
            ayah_refs.append(ayah["ayahRef"])
        reading = ayah.get("reading")
        if ayah.get("unitType") == "ayah" and not is_dict(reading):
            errors.append(f"{context}: numbered ayah requires a reading")
        if is_dict(reading):
            errors.extend(
                require_keys(reading, {"sourceRef", "text"}, f"{context}.reading")
            )
            source_ref = reading.get("sourceRef")
            if (
                not isinstance(source_ref, str)
                or source_base(source_ref) not in known_sources
            ):
                errors.append(
                    f"{context}.reading: unknown source reference {source_ref!r}"
                )
    errors.extend(unique_values(ayah_refs, "packet ayahs"))

    evidence = packet.get("evidenceField")
    if not is_dict(evidence):
        errors.append("packet: evidenceField must be an object")
        evidence = {}
    else:
        errors.extend(
            require_keys(
                evidence,
                {"localBoundaries", "reviewedChannels", "legacyIntegration"},
                "packet evidenceField",
            )
        )
    evidence_ids: list[str] = []
    evidence_groups = (
        ("localBoundaries", "boundaryId"),
        ("reviewedChannels", "synthesisId"),
        ("legacyIntegration", "sectionId"),
    )
    for group_name, id_key in evidence_groups:
        records = evidence.get(group_name)
        if not is_list(records):
            errors.append(f"packet evidenceField.{group_name}: must be an array")
            continue
        for index, record in enumerate(records):
            context = f"packet evidenceField.{group_name}[{index}]"
            if not is_dict(record):
                errors.append(f"{context}: must be an object")
                continue
            errors.extend(
                require_keys(record, {id_key, "sourceRefs", "text"}, context)
            )
            if isinstance(record.get(id_key), str):
                evidence_ids.append(record[id_key])
            errors.extend(
                check_source_refs(record.get("sourceRefs"), known_sources, context)
            )
    errors.extend(unique_values(evidence_ids, "packet evidence records"))

    coverage = packet.get("coverage")
    if not is_dict(coverage):
        errors.append("packet: coverage must be an object")
    else:
        errors.extend(
            require_keys(
                coverage,
                {"quranText", "layer2", "networkV3", "v11"},
                "packet coverage",
            )
        )
        for group_name, group in coverage.items():
            if not is_dict(group):
                errors.append(f"packet coverage.{group_name}: must be an object")
                continue
            for source_id in group.get("sourceIds", []):
                if source_id not in known_sources:
                    errors.append(
                        f"packet coverage.{group_name}: unknown sourceId {source_id!r}"
                    )
    return errors


def validate_hypotheses(
    hypotheses: dict[str, Any], packet: dict[str, Any]
) -> list[str]:
    errors = require_keys(
        hypotheses,
        {
            "schemaVersion",
            "packetId",
            "surah",
            "hypotheses",
        },
        "hypotheses",
    )
    if hypotheses.get("schemaVersion") != "layer3-discovery-hypotheses-v1":
        errors.append("hypotheses: unsupported schemaVersion")
    if hypotheses.get("packetId") != packet.get("packetId"):
        errors.append("hypotheses: packetId does not match packet")
    if hypotheses.get("surah") != packet.get("surah"):
        errors.append("hypotheses: surah does not match packet")
    records = hypotheses.get("hypotheses")
    if not is_list(records):
        errors.append("hypotheses: hypotheses must be an array")
        return errors
    hypothesis_ids = [
        record.get("hypothesisId")
        for record in records
        if is_dict(record) and isinstance(record.get("hypothesisId"), str)
    ]
    errors.extend(unique_values(hypothesis_ids, "discovery hypotheses"))
    for index, record in enumerate(records):
        context = f"hypotheses[{index}]"
        if not is_dict(record):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            require_keys(
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
    return errors


def validate_ledger(
    ledger: dict[str, Any],
    packet: dict[str, Any],
    hypotheses: dict[str, Any] | None,
) -> list[str]:
    errors = require_keys(
        ledger,
        {
            "schemaVersion",
            "ledgerId",
            "packetId",
            "surah",
            "architecture",
            "systems",
            "friction",
        },
        "ledger",
    )
    if ledger.get("schemaVersion") != "layer3-system-ledger-v2":
        errors.append("ledger: unsupported schemaVersion")
    if ledger.get("packetId") != packet.get("packetId"):
        errors.append("ledger: packetId does not match packet")
    if ledger.get("surah") != packet.get("surah"):
        errors.append("ledger: surah does not match packet")
    systems = ledger.get("systems")
    if not is_list(systems):
        errors.append("ledger: systems must be an array")
        return errors
    known_sources = source_ids(packet)
    known_hypotheses = {
        item.get("hypothesisId")
        for item in (hypotheses or {}).get("hypotheses", [])
        if is_dict(item)
    }
    system_ids = [
        system.get("systemId")
        for system in systems
        if is_dict(system) and isinstance(system.get("systemId"), str)
    ]
    errors.extend(unique_values(system_ids, "ledger systems"))
    known_systems = set(system_ids)
    claim_ids: list[str] = []
    for index, system in enumerate(systems):
        context = f"ledger systems[{index}]"
        if not is_dict(system):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            require_keys(
                system,
                {
                    "systemId",
                    "hypothesisIds",
                    "name",
                    "disposition",
                    "absorbedInto",
                    "governingOperation",
                    "primaryContainment",
                    "ayahRefs",
                    "trajectory",
                    "readerShifts",
                    "evidenceContributions",
                    "boundaries",
                },
                context,
            )
        )
        if hypotheses is not None:
            for hypothesis_id in system.get("hypothesisIds", []):
                if hypothesis_id not in known_hypotheses:
                    errors.append(
                        f"{context}: unknown hypothesisId {hypothesis_id!r}"
                    )
        for stage_index, stage in enumerate(system.get("trajectory", [])):
            if is_dict(stage):
                errors.extend(
                    check_source_refs(
                        stage.get("sourceRefs"),
                        known_sources,
                        f"{context}.trajectory[{stage_index}]",
                    )
                )
        for claim_index, claim in enumerate(system.get("evidenceContributions", [])):
            claim_context = f"{context}.evidenceContributions[{claim_index}]"
            if not is_dict(claim):
                errors.append(f"{claim_context}: must be an object")
                continue
            if isinstance(claim.get("claimId"), str):
                claim_ids.append(claim["claimId"])
            errors.extend(
                check_source_refs(claim.get("sourceRefs"), known_sources, claim_context)
            )
            if claim.get("upstreamStatus") == "rejected-predication":
                if claim.get("role") == "core":
                    errors.append(
                        f"{claim_context}: rejected predication cannot be core"
                    )
        for boundary_index, boundary in enumerate(system.get("boundaries", [])):
            boundary_context = f"{context}.boundaries[{boundary_index}]"
            if not is_dict(boundary):
                errors.append(f"{boundary_context}: must be an object")
                continue
            errors.extend(
                check_source_refs(
                    boundary.get("sourceRefs"),
                    known_sources,
                    boundary_context,
                )
            )
    errors.extend(unique_values(claim_ids, "ledger claims"))
    architecture = ledger.get("architecture", {})
    if is_dict(architecture):
        for system_id in architecture.get("orderedSystemIds", []):
            if system_id not in known_systems:
                errors.append(
                    f"ledger architecture: unknown ordered system {system_id!r}"
                )
    return errors


def validate_publication(
    packet: dict[str, Any],
    ledger: dict[str, Any],
    prose: str,
) -> list[str]:
    errors: list[str] = []
    for pattern in FORBIDDEN_PROSE:
        match = pattern.search(prose)
        if match:
            errors.append(
                f"prose: apparatus term {match.group(0)!r} must not appear"
            )
    prose_folded = prose.casefold()
    for system in ledger.get("systems", []):
        if not is_dict(system):
            continue
        for boundary in system.get("boundaries", []):
            if not is_dict(boundary):
                continue
            prohibited = boundary.get("prohibitedForm")
            if isinstance(prohibited, str) and prohibited.strip():
                if prohibited.casefold() in prose_folded:
                    errors.append(
                        f"prose: contains a prohibited claim form from "
                        f"system {system.get('systemId')!r}"
                    )
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

    hypotheses_parser = subparsers.add_parser("hypotheses")
    hypotheses_parser.add_argument("artifact", type=Path)
    hypotheses_parser.add_argument("--packet", required=True, type=Path)

    ledger_parser = subparsers.add_parser("ledger")
    ledger_parser.add_argument("artifact", type=Path)
    ledger_parser.add_argument("--packet", required=True, type=Path)
    ledger_parser.add_argument("--hypotheses", type=Path)

    publication_parser = subparsers.add_parser("publication")
    publication_parser.add_argument("--packet", required=True, type=Path)
    publication_parser.add_argument("--ledger", required=True, type=Path)
    publication_parser.add_argument("--prose", required=True, type=Path)

    args = parser.parse_args()
    if args.command == "packet":
        return report(validate_packet(load_json(args.artifact)))
    if args.command == "hypotheses":
        packet = load_json(args.packet)
        return report(validate_hypotheses(load_json(args.artifact), packet))
    if args.command == "ledger":
        packet = load_json(args.packet)
        hypotheses = load_json(args.hypotheses) if args.hypotheses else None
        return report(validate_ledger(load_json(args.artifact), packet, hypotheses))
    packet = load_json(args.packet)
    ledger = load_json(args.ledger)
    prose = args.prose.read_text(encoding="utf-8")
    return report(validate_publication(packet, ledger, prose))


if __name__ == "__main__":
    raise SystemExit(main())
