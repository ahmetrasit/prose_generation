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
        for item in packet.get("sources", [])
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
            "ayahs",
            "sources",
            "coverage",
            "warnings",
        },
        "packet",
    )
    if packet.get("schemaVersion") != "layer3-source-packet-v1":
        errors.append("packet: unsupported schemaVersion")
    sources = packet.get("sources")
    if not is_list(sources) or not sources:
        errors.append("packet: sources must be a non-empty array")
        sources = []
    ids = [
        item.get("sourceId")
        for item in sources
        if is_dict(item) and isinstance(item.get("sourceId"), str)
    ]
    errors.extend(unique_values(ids, "packet sources"))
    required_source_keys = {"sourceId", "kind", "role", "path", "format", "content"}
    for index, source in enumerate(sources):
        if not is_dict(source):
            errors.append(f"packet sources[{index}]: must be an object")
            continue
        errors.extend(
            require_keys(source, required_source_keys, f"packet sources[{index}]")
        )
    ayahs = packet.get("ayahs")
    if not is_list(ayahs) or not ayahs:
        errors.append("packet: ayahs must be a non-empty array")
        ayahs = []
    ayah_refs = []
    known_sources = set(ids)
    for index, ayah in enumerate(ayahs):
        if not is_dict(ayah):
            errors.append(f"packet ayahs[{index}]: must be an object")
            continue
        errors.extend(
            require_keys(
                ayah,
                {"ayahRef", "unitType", "arabic", "sourceRefs"},
                f"packet ayahs[{index}]",
            )
        )
        if isinstance(ayah.get("ayahRef"), str):
            ayah_refs.append(ayah["ayahRef"])
        for ref in ayah.get("sourceRefs", []):
            if ref not in known_sources:
                errors.append(
                    f"packet ayahs[{index}]: unknown source reference {ref!r}"
                )
    errors.extend(unique_values(ayah_refs, "packet ayahs"))
    coverage = packet.get("coverage")
    if not is_dict(coverage):
        errors.append("packet: coverage must be an object")
    else:
        errors.extend(
            require_keys(
                coverage,
                {"quranText", "layer2", "networkV3", "v12", "v11"},
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


def validate_candidates(
    candidates: dict[str, Any], packet: dict[str, Any]
) -> list[str]:
    errors = require_keys(
        candidates,
        {
            "schemaVersion",
            "packetId",
            "surah",
            "primaryMovement",
            "primaryTensions",
            "systems",
            "friction",
        },
        "candidates",
    )
    if candidates.get("schemaVersion") != "layer3-system-candidates-v1":
        errors.append("candidates: unsupported schemaVersion")
    if candidates.get("packetId") != packet.get("packetId"):
        errors.append("candidates: packetId does not match packet")
    if candidates.get("surah") != packet.get("surah"):
        errors.append("candidates: surah does not match packet")
    systems = candidates.get("systems")
    if not is_list(systems) or not systems:
        errors.append("candidates: systems must be a non-empty array")
        return errors
    known_sources = source_ids(packet)
    system_ids = [
        system.get("systemId")
        for system in systems
        if is_dict(system) and isinstance(system.get("systemId"), str)
    ]
    errors.extend(unique_values(system_ids, "candidate systems"))
    contribution_ids: list[str] = []
    for index, system in enumerate(systems):
        context = f"candidates systems[{index}]"
        if not is_dict(system):
            errors.append(f"{context}: must be an object")
            continue
        errors.extend(
            require_keys(
                system,
                {
                    "systemId",
                    "workingName",
                    "governingOperation",
                    "primaryContainment",
                    "wholeSurahShift",
                    "ayahRefs",
                    "trajectory",
                    "evidenceContributions",
                    "ahaMoments",
                    "counterpressure",
                    "coherence",
                },
                context,
            )
        )
        if len(set(system.get("ayahRefs", []))) < 2:
            errors.append(f"{context}: system must span at least two ayahs")
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
            if isinstance(claim.get("contributionId"), str):
                contribution_ids.append(claim["contributionId"])
            errors.extend(
                check_source_refs(claim.get("sourceRefs"), known_sources, claim_context)
            )
            if claim.get("upstreamStatus") == "rejected-predication":
                if claim.get("role") == "core":
                    errors.append(
                        f"{claim_context}: rejected predication cannot be core"
                    )
                if not claim.get("prohibitedInference"):
                    errors.append(
                        f"{claim_context}: rejected predication needs "
                        "prohibitedInference"
                    )
    errors.extend(unique_values(contribution_ids, "candidate contributions"))
    return errors


def validate_ledger(
    ledger: dict[str, Any],
    packet: dict[str, Any],
    candidates: dict[str, Any] | None,
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
            "globalBoundaries",
            "friction",
        },
        "ledger",
    )
    if ledger.get("schemaVersion") != "layer3-system-ledger-v1":
        errors.append("ledger: unsupported schemaVersion")
    if ledger.get("packetId") != packet.get("packetId"):
        errors.append("ledger: packetId does not match packet")
    if ledger.get("surah") != packet.get("surah"):
        errors.append("ledger: surah does not match packet")
    systems = ledger.get("systems")
    if not is_list(systems) or not systems:
        errors.append("ledger: systems must be a non-empty array")
        return errors
    known_sources = source_ids(packet)
    known_candidates = {
        system.get("systemId")
        for system in (candidates or {}).get("systems", [])
        if is_dict(system)
    }
    system_ids = [
        system.get("systemId")
        for system in systems
        if is_dict(system) and isinstance(system.get("systemId"), str)
    ]
    errors.extend(unique_values(system_ids, "ledger systems"))
    known_systems = set(system_ids)
    render_count = 0
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
                    "candidateSystemIds",
                    "name",
                    "disposition",
                    "governingOperation",
                    "readerStatement",
                    "primaryContainment",
                    "wholeSurahShift",
                    "ayahRefs",
                    "trajectory",
                    "ahaMoments",
                    "claimDecisions",
                    "failureTests",
                },
                context,
            )
        )
        if system.get("disposition") == "render":
            render_count += 1
            if not system.get("ahaMoments"):
                errors.append(f"{context}: rendered system requires an ahaMoment")
        if len(set(system.get("ayahRefs", []))) < 2:
            errors.append(f"{context}: system must span at least two ayahs")
        if candidates is not None:
            for candidate_id in system.get("candidateSystemIds", []):
                if candidate_id not in known_candidates:
                    errors.append(
                        f"{context}: unknown candidateSystemId {candidate_id!r}"
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
        for claim_index, claim in enumerate(system.get("claimDecisions", [])):
            claim_context = f"{context}.claimDecisions[{claim_index}]"
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
                if not claim.get("prohibitedForm"):
                    errors.append(
                        f"{claim_context}: rejected predication needs prohibitedForm"
                    )
    errors.extend(unique_values(claim_ids, "ledger claims"))
    if render_count == 0:
        errors.append("ledger: at least one system must have disposition 'render'")
    architecture = ledger.get("architecture", {})
    if is_dict(architecture):
        for system_id in architecture.get("orderedSystemIds", []):
            if system_id not in known_systems:
                errors.append(
                    f"ledger architecture: unknown ordered system {system_id!r}"
                )
    return errors


def prose_paragraphs(markdown: str) -> list[str]:
    blocks = [
        block.strip()
        for block in re.split(r"\n\s*\n", markdown.strip())
        if block.strip()
    ]
    return [block for block in blocks if not block.startswith("#")]


def validate_publication(
    evidence: dict[str, Any],
    packet: dict[str, Any],
    ledger: dict[str, Any],
    prose: str,
) -> list[str]:
    errors = require_keys(
        evidence,
        {
            "schemaVersion",
            "packetId",
            "ledgerId",
            "surah",
            "proseFile",
            "paragraphs",
            "ahaCoverage",
            "limitations",
        },
        "publication evidence",
    )
    if evidence.get("schemaVersion") != "layer3-prose-evidence-v1":
        errors.append("publication evidence: unsupported schemaVersion")
    if evidence.get("packetId") != packet.get("packetId"):
        errors.append("publication evidence: packetId does not match packet")
    if evidence.get("ledgerId") != ledger.get("ledgerId"):
        errors.append("publication evidence: ledgerId does not match ledger")
    known_sources = source_ids(packet)
    known_systems = {
        system.get("systemId")
        for system in ledger.get("systems", [])
        if is_dict(system)
    }
    paragraphs = prose_paragraphs(prose)
    rows = evidence.get("paragraphs")
    if not is_list(rows):
        errors.append("publication evidence: paragraphs must be an array")
        rows = []
    if len(paragraphs) != len(rows):
        errors.append(
            "publication evidence: prose paragraph count "
            f"({len(paragraphs)}) does not match evidence ({len(rows)})"
        )
    paragraph_ids: list[str] = []
    for index, row in enumerate(rows):
        context = f"publication paragraphs[{index}]"
        if not is_dict(row):
            errors.append(f"{context}: must be an object")
            continue
        if isinstance(row.get("paragraphId"), str):
            paragraph_ids.append(row["paragraphId"])
        for system_id in row.get("systemIds", []):
            if system_id not in known_systems:
                errors.append(f"{context}: unknown systemId {system_id!r}")
        for claim_index, claim in enumerate(row.get("claims", [])):
            if is_dict(claim):
                errors.extend(
                    check_source_refs(
                        claim.get("sourceRefs"),
                        known_sources,
                        f"{context}.claims[{claim_index}]",
                    )
                )
        if index < len(paragraphs) and isinstance(row.get("openingText"), str):
            normalized = re.sub(r"\s+", " ", paragraphs[index]).casefold()
            opening = re.sub(r"\s+", " ", row["openingText"]).casefold()
            if not normalized.startswith(opening):
                errors.append(f"{context}: openingText does not match prose")
    errors.extend(unique_values(paragraph_ids, "publication paragraphs"))
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
        for claim in system.get("claimDecisions", []):
            if not is_dict(claim):
                continue
            prohibited = claim.get("prohibitedForm")
            if isinstance(prohibited, str) and prohibited.strip():
                if prohibited.casefold() in prose_folded:
                    errors.append(
                        f"prose: contains prohibited claim form from "
                        f"{claim.get('claimId')!r}"
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

    candidates_parser = subparsers.add_parser("candidates")
    candidates_parser.add_argument("artifact", type=Path)
    candidates_parser.add_argument("--packet", required=True, type=Path)

    ledger_parser = subparsers.add_parser("ledger")
    ledger_parser.add_argument("artifact", type=Path)
    ledger_parser.add_argument("--packet", required=True, type=Path)
    ledger_parser.add_argument("--candidates", type=Path)

    publication_parser = subparsers.add_parser("publication")
    publication_parser.add_argument("artifact", type=Path)
    publication_parser.add_argument("--packet", required=True, type=Path)
    publication_parser.add_argument("--ledger", required=True, type=Path)
    publication_parser.add_argument("--prose", required=True, type=Path)

    args = parser.parse_args()
    if args.command == "packet":
        return report(validate_packet(load_json(args.artifact)))
    if args.command == "candidates":
        packet = load_json(args.packet)
        return report(validate_candidates(load_json(args.artifact), packet))
    if args.command == "ledger":
        packet = load_json(args.packet)
        candidates = load_json(args.candidates) if args.candidates else None
        return report(validate_ledger(load_json(args.artifact), packet, candidates))
    packet = load_json(args.packet)
    ledger = load_json(args.ledger)
    prose = args.prose.read_text(encoding="utf-8")
    return report(validate_publication(load_json(args.artifact), packet, ledger, prose))


if __name__ == "__main__":
    raise SystemExit(main())
