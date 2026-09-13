#!/usr/bin/env python3
"""Instantiate one hermetic prompt for the Layer 3 v3 workflow."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from common import (
    REPO_ROOT,
    WORKFLOW_ROOT,
    immutable_write_text,
    load_json,
    normalize_language,
    resolve_portable_path,
    sha256_file,
)
from validate import (
    validate_briefs,
    validate_composition,
    validate_hypotheses,
    validate_packet,
)


STAGES: dict[str, dict[str, str]] = {
    "discover": {
        "prompt": "01-discover.md",
        "schema": "discovery-hypotheses-v3.schema.json",
        "output": "{surah}.discovery-hypotheses.{language}.json",
    },
    "review": {
        "prompt": "02-review.md",
        "schema": "channel-briefs-v3.schema.json",
        "output": "{surah}.channel-briefs.{language}.json",
    },
    "compose": {
        "prompt": "03-compose.md",
        "schema": "surah-composition-v2.schema.json",
        "output": "{surah}.surah-composition.draft.{language}.json",
    },
    "edit": {
        "prompt": "04-edit.md",
        "schema": "surah-composition-v2.schema.json",
        "output": "{surah}.surah-composition.{language}.json",
    },
}


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def block(label: str, text: str) -> str:
    token = label.upper().replace(" ", "_").replace("-", "_")
    return f"<BEGIN_{token}>\n{text.rstrip()}\n<END_{token}>"


def resolve_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def run_dir(packet: dict[str, Any]) -> Path:
    return (
        WORKFLOW_ROOT
        / "runs"
        / "v3"
        / f"s{packet['surah']:03d}"
        / packet["language"]
        / packet["runId"]
    )


def find_default_packet(surah: int, language: str) -> Path:
    root = WORKFLOW_ROOT / "runs" / "v3" / f"s{surah:03d}" / language
    pattern = f"{surah}.source-packet.{language}.json"
    matches = sorted(root.glob(f"*/{pattern}"))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        historical = (
            WORKFLOW_ROOT
            / "packets"
            / f"s{surah:03d}"
            / f"{surah}.source-packet.json"
        )
        raise SystemExit(
            f"error: no v3 source packet found under {root}; run build_packet.py "
            f"or pass --packet. Historical packet path is not v3: {historical}"
        )
    rendered = "\n".join(f"  {match}" for match in matches)
    raise SystemExit(
        "error: multiple v3 source packets exist; pass --packet explicitly:\n"
        + rendered
    )


def source_excerpt(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "packetId": packet.get("packetId"),
        "runId": packet.get("runId"),
        "sourceSetHash": packet.get("sourceSetHash"),
        "coverage": packet.get("coverage"),
        "warnings": packet.get("warnings", []),
    }


def discovery_input(packet: dict[str, Any]) -> dict[str, Any]:
    surface_anchors = []
    for item in packet.get("primaryGround", {}).get("ayahs", []):
        if not isinstance(item, dict):
            continue
        floor = item.get("floor")
        surface_anchors.append(
            {
                "ayahRef": item.get("ayahRef"),
                "unitType": item.get("unitType"),
                "arabic": item.get("arabic"),
                "floor": floor.get("text") if isinstance(floor, dict) else None,
                "floorSourceRef": floor.get("sourceRef") if isinstance(floor, dict) else None,
            }
        )
    return {
        "schemaVersion": "layer3-discovery-input-v3",
        "packetId": packet.get("packetId"),
        "sourceSetHash": packet.get("sourceSetHash"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "surfaceAnchors": surface_anchors,
        "activationCards": packet.get("evidenceField", {}).get("activationCards", []),
        "coverage": {
            "quranText": packet.get("coverage", {}).get("quranText"),
            "primaryFloor": packet.get("coverage", {}).get("primaryFloor"),
            "networkV3": packet.get("coverage", {}).get("networkV3"),
        },
        "warnings": [
            warning
            for warning in packet.get("warnings", [])
            if "network" in warning.casefold()
        ],
    }


def review_context(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "schemaVersion": "layer3-review-context-v3",
        "packetId": packet.get("packetId"),
        "sourceSetHash": packet.get("sourceSetHash"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "lineage": source_excerpt(packet),
        "sourceRegistry": packet.get("sourceRegistry", []),
        "primaryGround": packet.get("primaryGround"),
        "layer2Handoff": packet.get("layer2Handoff"),
        "evidenceField": packet.get("evidenceField"),
    }


def selected_layer2_reader_prose(
    packet: dict[str, Any], briefs: dict[str, Any]
) -> list[dict[str, str]]:
    selected_ayahs = {
        member.get("ayahRef")
        for channel in briefs.get("channels", [])
        if isinstance(channel, dict)
        for member in channel.get("memberLandings", [])
        if isinstance(member, dict) and isinstance(member.get("ayahRef"), str)
    }
    registry = {
        source.get("sourceId"): source
        for source in packet.get("sourceRegistry", [])
        if isinstance(source, dict) and isinstance(source.get("sourceId"), str)
    }
    excerpts: list[dict[str, str]] = []
    for ayah in packet.get("layer2Handoff", {}).get("ayahs", []):
        if not isinstance(ayah, dict) or ayah.get("ayahRef") not in selected_ayahs:
            continue
        source_id = ayah.get("artifactRefs", {}).get("prose")
        source = registry.get(source_id)
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise SystemExit(
                f"error: no registered Layer-2 prose source for {ayah.get('ayahRef')}"
            )
        path = resolve_portable_path(source["path"])
        if not path.is_file():
            raise SystemExit(f"error: selected Layer-2 prose is missing: {path}")
        if sha256_file(path) != source.get("sha256"):
            raise SystemExit(f"error: selected Layer-2 prose changed after packet build: {path}")
        prose = path.read_text(encoding="utf-8").strip()
        if not prose:
            raise SystemExit(f"error: selected Layer-2 prose is empty: {path}")
        excerpts.append(
            {
                "ayahRef": ayah["ayahRef"],
                "sourceRef": source_id,
                "text": prose,
            }
        )
    missing = selected_ayahs - {item["ayahRef"] for item in excerpts}
    if missing:
        raise SystemExit(
            "error: no Layer-2 reader prose could be projected for admitted "
            "member ayahs: " + ", ".join(sorted(missing))
        )
    return excerpts


def composition_input(
    packet: dict[str, Any], briefs: dict[str, Any]
) -> dict[str, Any]:
    return {
        "schemaVersion": "layer3-composition-input-v2",
        "packetId": packet.get("packetId"),
        "sourceSetHash": packet.get("sourceSetHash"),
        "surah": packet.get("surah"),
        "language": packet.get("language"),
        "lineage": source_excerpt(packet),
        "primaryGround": packet.get("primaryGround"),
        "selectedLayer2ReaderProse": selected_layer2_reader_prose(packet, briefs),
    }


def stage_output_path(packet: dict[str, Any], stage: str) -> Path:
    config = STAGES[stage]
    filename = config["output"].format(
        surah=packet["surah"],
        language=packet["language"],
    )
    return run_dir(packet) / "outputs" / filename


def prompt_output_path(packet: dict[str, Any], stage: str, attempt: int) -> Path:
    return (
        run_dir(packet)
        / "inputs"
        / f"{packet['surah']}.{stage}.attempt-{attempt:02d}.{packet['language']}.prompt.md"
    )


def assert_valid(errors: list[str], context: str) -> None:
    if not errors:
        return
    rendered = "\n".join(f"  - {error}" for error in errors)
    raise SystemExit(f"error: invalid {context}:\n{rendered}")


def assemble(
    *,
    stage: str,
    surah: int,
    packet_path: Path,
    hypotheses_path: Path | None,
    briefs_path: Path | None,
    draft_path: Path | None = None,
) -> str:
    config = STAGES[stage]
    packet = load_json(packet_path)
    if packet.get("surah") != surah:
        raise SystemExit(
            f"error: packet surah is {packet.get('surah')}, expected {surah}"
        )
    assert_valid(validate_packet(packet, verify_sources=False), "source packet")

    prompt_path = WORKFLOW_ROOT / "prompts" / config["prompt"]
    schema_path = WORKFLOW_ROOT / "schemas" / config["schema"]
    expected_output = stage_output_path(packet, stage)
    sections = [
        "# Hermetic Layer 3 v3 Run",
        "",
        f"- stage: `{stage}`",
        f"- surah: `{surah}`",
        f"- target language: `{packet.get('language')}`",
        f"- packet: `{packet.get('packetId')}`",
        f"- write: `{expected_output}`",
        "",
        "Use only the material between the inlined boundary markers below. "
        "Paths inside JSON are provenance labels, not permission to read files.",
        "Do not call tools, read files, browse, or edit any path other than the exact output file.",
        "",
        block("task", prompt_path.read_text(encoding="utf-8")),
        "",
        block("output schema json", schema_path.read_text(encoding="utf-8")),
    ]

    if stage == "discover":
        sections.extend(
            [
                "",
                block("discovery input json", json_text(discovery_input(packet))),
            ]
        )
    if stage == "review":
        if hypotheses_path is None:
            hypotheses_path = stage_output_path(packet, "discover")
        hypotheses = load_json(hypotheses_path)
        assert_valid(validate_hypotheses(hypotheses, packet), "discovery hypotheses")
        sections.extend(
            [
                "",
                block("discovery hypotheses json", json_text(hypotheses)),
                "",
                block("review context json", json_text(review_context(packet))),
            ]
        )
    if stage == "compose":
        if hypotheses_path is None:
            hypotheses_path = stage_output_path(packet, "discover")
        if briefs_path is None:
            briefs_path = stage_output_path(packet, "review")
        hypotheses = load_json(hypotheses_path)
        briefs = load_json(briefs_path)
        assert_valid(validate_hypotheses(hypotheses, packet), "discovery hypotheses")
        assert_valid(validate_briefs(briefs, packet, hypotheses), "channel briefs")
        sections.extend(
            [
                "",
                block("composition input json", json_text(composition_input(packet, briefs))),
                "",
                block("channel briefs json", json_text(briefs)),
            ]
        )
    if stage == "edit":
        if hypotheses_path is None:
            hypotheses_path = stage_output_path(packet, "discover")
        if briefs_path is None:
            briefs_path = stage_output_path(packet, "review")
        if draft_path is None:
            draft_path = stage_output_path(packet, "compose")
        hypotheses = load_json(hypotheses_path)
        briefs = load_json(briefs_path)
        draft = load_json(draft_path)
        assert_valid(validate_hypotheses(hypotheses, packet), "discovery hypotheses")
        assert_valid(validate_briefs(briefs, packet, hypotheses), "channel briefs")
        assert_valid(
            validate_composition(draft, packet, briefs, required_phase="draft"),
            "draft composition",
        )
        sections.extend(
            [
                "",
                block("composition input json", json_text(composition_input(packet, briefs))),
                "",
                block("channel briefs json", json_text(briefs)),
                "",
                block("draft composition json", json_text(draft)),
            ]
        )

    response = (
        f"For this run, `N` in the task means `{surah}`. Write "
        f"`{expected_output}` as a JSON object conforming to the inlined schema. "
        "Write no additional files."
    )
    sections.extend(["", "# Response", "", response, ""])
    return "\n".join(sections)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=sorted(STAGES))
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--packet", type=Path)
    parser.add_argument("--hypotheses", type=Path)
    parser.add_argument("--briefs", type=Path)
    parser.add_argument("--draft", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()

    language = normalize_language(args.language)
    packet = resolve_path(args.packet) if args.packet else find_default_packet(args.surah, language)
    hypotheses = resolve_path(args.hypotheses) if args.hypotheses else None
    briefs = resolve_path(args.briefs) if args.briefs else None
    draft = resolve_path(args.draft) if args.draft else None

    packet_json = load_json(packet)
    if packet_json.get("language") != language:
        raise SystemExit(
            f"error: packet language is {packet_json.get('language')!r}, expected {language!r}"
        )
    output = resolve_path(args.out) if args.out else prompt_output_path(
        packet_json, args.stage, args.attempt
    )

    prompt = assemble(
        stage=args.stage,
        surah=args.surah,
        packet_path=packet,
        hypotheses_path=hypotheses,
        briefs_path=briefs,
        draft_path=draft,
    )
    wrote = immutable_write_text(output, prompt)
    verb = "wrote" if wrote else "unchanged"
    print(f"{verb} {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(
        "error: this historical v2 script is disabled for active runs; "
        "use _surah_commentary/v2/scripts/workflow.py instantiate"
    )
