#!/usr/bin/env python3
"""Instantiate one hermetic prompt for the Layer 3 workflow."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from common import REPO_ROOT, WORKFLOW_ROOT, load_json


STAGES: dict[str, dict[str, str | None]] = {
    "discover": {
        "prompt": "01-discover.md",
        "schema": "discovery-hypotheses-v1.schema.json",
        "output": "{surah}.discovery-hypotheses.json",
    },
    "review": {
        "prompt": "02-review.md",
        "schema": "channel-briefs-v1.schema.json",
        "output": "{surah}.channel-briefs.json",
    },
    "compose": {
        "prompt": "03-compose.md",
        "schema": None,
        "output": "{surah}.surah-reading.md",
    },
}


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def block(label: str, text: str) -> str:
    token = label.upper().replace(" ", "_").replace("-", "_")
    return f"<BEGIN_{token}>\n{text.rstrip()}\n<END_{token}>"


def network_activation_cards(markdown: str) -> list[dict[str, Any]]:
    """Project reviewed subchannels without their prewritten syntheses."""
    cards: list[dict[str, Any]] = []
    parent_number: int | None = None
    current: dict[str, Any] | None = None

    def finish() -> None:
        nonlocal current
        if current is None:
            return
        required = ("ayahAnchors", "activeMotifs")
        missing = [key for key in required if not current.get(key)]
        if missing:
            raise SystemExit(
                f"error: reviewed activation card {current['cardId']} is "
                f"missing {', '.join(missing)}"
            )
        current["ayahRefs"] = list(
            dict.fromkeys(
                re.findall(r"\b[1-9][0-9]{0,2}:[1-9][0-9]*\b", current["ayahAnchors"])
            )
        )
        current["signalRefs"] = re.findall(r"`([^`]+)`", current["activeMotifs"])
        cards.append(current)
        current = None

    for line in markdown.splitlines():
        parent_match = re.match(r"^###\s+([0-9]+)\.\s+", line)
        if parent_match:
            finish()
            parent_number = int(parent_match.group(1))
            continue

        standalone_match = re.match(r"^###\s+S([0-9]+)\.\s+", line)
        if standalone_match:
            finish()
            standalone = int(standalone_match.group(1))
            parent_number = None
            current = {
                "cardId": f"network-s{standalone:02d}",
                "ayahAnchors": None,
                "activeMotifs": None,
                "sourceRefs": [f"network-review#standalone-{standalone}"],
            }
            continue

        subchannel_match = re.match(r"^####\s+Subchannel\s+([A-Z]+)\.\s+", line)
        if subchannel_match:
            finish()
            if parent_number is None:
                raise SystemExit("error: reviewed subchannel has no parent")
            letter = subchannel_match.group(1).lower()
            current = {
                "cardId": f"network-p{parent_number:02d}-{letter}",
                "ayahAnchors": None,
                "activeMotifs": None,
                "sourceRefs": [
                    f"network-review#parent-{parent_number}/subchannel-{letter}"
                ],
            }
            continue

        if current is None:
            continue

        fields = {
            "- Active motifs:": "activeMotifs",
            "- Ayah anchors:": "ayahAnchors",
        }
        for prefix, key in fields.items():
            if line.startswith(prefix):
                current[key] = line[len(prefix) :].strip()
                break

    finish()
    return cards


def discovery_input(packet: dict[str, Any]) -> dict[str, Any]:
    primary = packet.get("primaryGround", {})
    surface_anchors = [
        {
            "ayahRef": item.get("ayahRef"),
            "unitType": item.get("unitType"),
            "arabic": item.get("arabic"),
        }
        for item in primary.get("ayahs", [])
        if isinstance(item, dict)
    ]
    cards: list[dict[str, Any]] = []
    for reviewed in packet.get("evidenceField", {}).get("reviewedChannels", []):
        if not isinstance(reviewed, dict) or not isinstance(reviewed.get("text"), str):
            continue
        cards.extend(network_activation_cards(reviewed["text"]))
    return {
        "schemaVersion": "layer3-discovery-input-v1",
        "packetId": packet.get("packetId"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "surfaceAnchors": surface_anchors,
        "activationCards": cards,
        "coverage": {
            "quranText": packet.get("coverage", {}).get("quranText"),
            "networkV3": packet.get("coverage", {}).get("networkV3"),
        },
        "warnings": [
            warning
            for warning in packet.get("warnings", [])
            if "network" in warning.casefold()
        ],
    }


def review_context(packet: dict[str, Any]) -> dict[str, Any]:
    evidence = packet.get("evidenceField", {})
    return {
        "schemaVersion": "layer3-review-context-v1",
        "packetId": packet.get("packetId"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "sourceRegistry": packet.get("sourceRegistry", []),
        "primaryGround": packet.get("primaryGround"),
        "localBoundaries": evidence.get("localBoundaries", []),
        "secondaryMaterial": evidence.get("secondaryMaterial", []),
        "coverage": packet.get("coverage"),
        "warnings": packet.get("warnings", []),
    }


def composition_input(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "schemaVersion": "layer3-composition-input-v1",
        "packetId": packet.get("packetId"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "primaryGround": packet.get("primaryGround"),
    }


def assemble(
    *,
    stage: str,
    surah: int,
    packet_path: Path,
    candidates_path: Path | None,
    briefs_path: Path | None,
) -> str:
    config = STAGES[stage]
    packet = load_json(packet_path)
    if packet.get("surah") != surah:
        raise SystemExit(
            f"error: packet surah is {packet.get('surah')}, expected {surah}"
        )
    prompt_path = WORKFLOW_ROOT / "prompts" / config["prompt"]
    schema_name = config["schema"]
    schema_path = WORKFLOW_ROOT / "schemas" / schema_name if schema_name else None
    sections = [
        "# Hermetic Layer 3 Run",
        "",
        f"- stage: `{stage}`",
        f"- surah: `{surah}`",
        f"- target language: `{packet.get('language')}`",
        f"- write: `{config['output'].format(surah=surah)}`",
        "",
        "Use only the material between the inlined boundary markers below. "
        "Paths inside the packet are provenance labels, not permission to read files.",
        "",
        block("task", prompt_path.read_text(encoding="utf-8")),
    ]
    if schema_path is not None:
        sections.extend(
            [
                "",
                block("output schema json", schema_path.read_text(encoding="utf-8")),
                "",
            ]
        )
    if stage == "discover":
        sections.extend(
            [
                "",
                block("discovery input json", json_text(discovery_input(packet))),
            ]
        )
    if stage == "review":
        if candidates_path is None:
            raise SystemExit("error: review stage requires --hypotheses")
        discovery = discovery_input(packet)
        sections.extend(
            [
                "",
                block(
                    "discovery hypotheses json",
                    json_text(load_json(candidates_path)),
                ),
                "",
                block(
                    "activation cards json",
                    json_text(discovery["activationCards"]),
                ),
                "",
                block("review context json", json_text(review_context(packet))),
            ]
        )
    if stage == "compose":
        if briefs_path is None:
            raise SystemExit("error: compose stage requires --briefs")
        sections.extend(
            [
                "",
                block(
                    "composition input json",
                    json_text(composition_input(packet)),
                ),
                "",
                block("channel briefs json", json_text(load_json(briefs_path))),
            ]
        )
    if stage == "compose":
        response = (
            f"For this run, `N` in the task means `{surah}`. Write exactly "
            f"`{config['output'].format(surah=surah)}` and no additional files."
        )
    else:
        response = (
            f"For this run, `N` in the task means `{surah}`. Write "
            f"`{config['output'].format(surah=surah)}` as a JSON object "
            "conforming to the inlined schema. Write no additional files."
        )
    sections.extend(["", "# Response", "", response, ""])
    return "\n".join(sections)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=sorted(STAGES))
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--packet", type=Path)
    parser.add_argument("--hypotheses", type=Path)
    parser.add_argument("--briefs", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    packet = args.packet or (
        WORKFLOW_ROOT
        / "packets"
        / f"s{args.surah:03d}"
        / f"{args.surah}.source-packet.json"
    )
    candidates = args.hypotheses
    if args.stage == "review" and candidates is None:
        candidates = (
            WORKFLOW_ROOT
            / "outputs"
            / f"s{args.surah:03d}"
            / f"{args.surah}.discovery-hypotheses.json"
        )
    briefs = args.briefs
    if args.stage == "compose" and briefs is None:
        briefs = (
            WORKFLOW_ROOT
            / "outputs"
            / f"s{args.surah:03d}"
            / f"{args.surah}.channel-briefs.json"
        )
    output = args.out or (
        WORKFLOW_ROOT
        / "inputs"
        / f"s{args.surah:03d}"
        / f"{args.surah}.{args.stage}.prompt.md"
    )
    if not packet.is_absolute():
        packet = REPO_ROOT / packet
    if candidates is not None and not candidates.is_absolute():
        candidates = REPO_ROOT / candidates
    if briefs is not None and not briefs.is_absolute():
        briefs = REPO_ROOT / briefs
    if not output.is_absolute():
        output = REPO_ROOT / output

    prompt = assemble(
        stage=args.stage,
        surah=args.surah,
        packet_path=packet,
        candidates_path=candidates,
        briefs_path=briefs,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(prompt, encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
