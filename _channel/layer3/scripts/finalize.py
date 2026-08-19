#!/usr/bin/env python3
"""Publish validated Layer 3 prose, evidence, and friction artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from common import (
    REPO_ROOT,
    WORKFLOW_ROOT,
    immutable_write_json,
    immutable_write_text,
    load_json,
    normalize_language,
)
from validate import (
    publication_evidence,
    validate_briefs,
    validate_composition,
    validate_hypotheses,
    validate_packet,
    validate_publication_evidence,
)


def resolve_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def default_run_dir(packet: dict[str, Any]) -> Path:
    return (
        WORKFLOW_ROOT
        / "runs"
        / "v3"
        / f"s{packet['surah']:03d}"
        / packet["language"]
        / packet["runId"]
    )


def assert_valid(errors: list[str], context: str) -> None:
    if not errors:
        return
    rendered = "\n".join(f"  - {error}" for error in errors)
    raise SystemExit(f"error: invalid {context}:\n{rendered}")


def friction_markdown(composition: dict[str, Any]) -> str:
    lines = [
        f"# Surah {composition['surah']} Layer 3 Friction",
        "",
        f"- compositionId: `{composition['compositionId']}`",
        f"- sourceSetHash: `{composition['sourceSetHash']}`",
        "",
    ]
    friction = composition.get("friction", [])
    if not friction:
        lines.append("No unresolved publication friction was reported.")
        lines.append("")
        return "\n".join(lines)
    for item in friction:
        lines.append(f"- `{item['code']}` - {item['detail']}")
    lines.append("")
    return "\n".join(lines)


def write_publication(
    *,
    composition: dict[str, Any],
    packet: dict[str, Any],
    briefs: dict[str, Any],
    out_dir: Path,
) -> list[Path]:
    if composition.get("phase") != "editorial":
        raise SystemExit("error: only an editorial Layer-3 composition may be published")
    published_prelude = composition["prelude"].rstrip() + "\n"
    published_postlude = composition["postlude"].rstrip() + "\n"
    evidence = publication_evidence(composition, packet, briefs)
    assert_valid(
        validate_publication_evidence(
            evidence,
            published_prelude,
            published_postlude,
            composition,
        ),
        "publication evidence",
    )
    surah = composition["surah"]
    language = composition["language"]
    prelude_path = out_dir / f"{surah}.surah-reading.prelude.{language}.md"
    postlude_path = out_dir / f"{surah}.surah-reading.postlude.{language}.md"
    evidence_path = out_dir / f"{surah}.surah-reading.evidence.{language}.json"
    friction_path = out_dir / f"{surah}.surah-reading.friction.{language}.md"

    immutable_write_text(prelude_path, published_prelude)
    immutable_write_text(postlude_path, published_postlude)
    immutable_write_json(evidence_path, evidence, compact=False)
    immutable_write_text(friction_path, friction_markdown(composition))
    return [prelude_path, postlude_path, evidence_path, friction_path]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--composition", required=True, type=Path)
    parser.add_argument("--packet", required=True, type=Path)
    parser.add_argument("--hypotheses", required=True, type=Path)
    parser.add_argument("--briefs", required=True, type=Path)
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()

    packet = load_json(resolve_path(args.packet))
    hypotheses = load_json(resolve_path(args.hypotheses))
    briefs = load_json(resolve_path(args.briefs))
    composition = load_json(resolve_path(args.composition))
    language = normalize_language(str(composition.get("language", "")))
    if packet.get("language") != language or briefs.get("language") != language:
        raise SystemExit("error: packet, briefs, and composition languages must match")

    assert_valid(validate_packet(packet, verify_sources=True), "source packet")
    assert_valid(validate_hypotheses(hypotheses, packet), "discovery hypotheses")
    assert_valid(validate_briefs(briefs, packet, hypotheses), "channel briefs")
    assert_valid(
        validate_composition(
            composition,
            packet,
            briefs,
            required_phase="editorial",
        ),
        "editorial composition",
    )

    out_dir = resolve_path(args.out_dir) if args.out_dir else default_run_dir(packet) / "published"
    paths = write_publication(
        composition=composition,
        packet=packet,
        briefs=briefs,
        out_dir=out_dir,
    )
    for path in paths:
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
