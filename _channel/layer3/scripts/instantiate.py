#!/usr/bin/env python3
"""Instantiate one hermetic prompt for the Layer 3 workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import REPO_ROOT, WORKFLOW_ROOT, load_json


STAGES: dict[str, dict[str, str]] = {
    "discover": {
        "prompt": "01-discover.md",
        "schema": "system-candidates-v1.schema.json",
        "output": "{surah}.system-candidates.json",
    },
    "review": {
        "prompt": "02-review.md",
        "schema": "system-ledger-v1.schema.json",
        "output": "{surah}.system-ledger.json",
    },
    "compose": {
        "prompt": "03-compose.md",
        "schema": "prose-evidence-v1.schema.json",
        "output": "{surah}.surah-reading.md, "
        "{surah}.surah-reading.evidence.json, "
        "{surah}.surah-reading.friction.md",
    },
}


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def block(label: str, text: str) -> str:
    token = label.upper().replace(" ", "_").replace("-", "_")
    return f"<BEGIN_{token}>\n{text.rstrip()}\n<END_{token}>"


def assemble(
    *,
    stage: str,
    surah: int,
    packet_path: Path,
    candidates_path: Path | None,
    ledger_path: Path | None,
) -> str:
    config = STAGES[stage]
    packet = load_json(packet_path)
    if packet.get("surah") != surah:
        raise SystemExit(
            f"error: packet surah is {packet.get('surah')}, expected {surah}"
        )
    prompt_path = WORKFLOW_ROOT / "prompts" / config["prompt"]
    schema_path = WORKFLOW_ROOT / "schemas" / config["schema"]
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
        "",
        block("output schema json", schema_path.read_text(encoding="utf-8")),
        "",
        block("source packet json", json_text(packet)),
    ]
    if stage == "review":
        if candidates_path is None:
            raise SystemExit("error: review stage requires --candidates")
        sections.extend(
            [
                "",
                block("discovered candidates json", json_text(load_json(candidates_path))),
            ]
        )
    if stage == "compose":
        if ledger_path is None:
            raise SystemExit("error: compose stage requires --ledger")
        sections.extend(
            [
                "",
                block("reviewed system ledger json", json_text(load_json(ledger_path))),
            ]
        )
    sections.extend(
        [
            "",
            "# Response",
            "",
            f"For this run, `N` in the task means `{surah}`. Write exactly "
            f"`{config['output'].format(surah=surah)}` and no additional files.",
            "",
        ]
    )
    return "\n".join(sections)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=sorted(STAGES))
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--packet", type=Path)
    parser.add_argument("--candidates", type=Path)
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    packet = args.packet or (
        WORKFLOW_ROOT
        / "packets"
        / f"s{args.surah:03d}"
        / f"{args.surah}.source-packet.json"
    )
    candidates = args.candidates
    if args.stage == "review" and candidates is None:
        candidates = (
            WORKFLOW_ROOT
            / "outputs"
            / f"s{args.surah:03d}"
            / f"{args.surah}.system-candidates.json"
        )
    ledger = args.ledger
    if args.stage == "compose" and ledger is None:
        ledger = (
            WORKFLOW_ROOT
            / "outputs"
            / f"s{args.surah:03d}"
            / f"{args.surah}.system-ledger.json"
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
    if ledger is not None and not ledger.is_absolute():
        ledger = REPO_ROOT / ledger
    if not output.is_absolute():
        output = REPO_ROOT / output

    prompt = assemble(
        stage=args.stage,
        surah=args.surah,
        packet_path=packet,
        candidates_path=candidates,
        ledger_path=ledger,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(prompt, encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
