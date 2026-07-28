#!/usr/bin/env python3
"""Render a deterministic human-review preview from validated Layer-2.5 JSON."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from check_channel_overlays import ROOT, paragraphs, resolve, validate


def ayah_sort_key(item: dict) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+):(\d+)", str(item.get("ayahRef", "")))
    return (int(match.group(1)), int(match.group(2))) if match else (999, 999)


def render(overlay_path: Path, integration_path: Path) -> str:
    errors = validate(overlay_path, integration_path)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: overlay validation failed:\n{details}")
    overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
    lines = [
        f"# Surah {overlay['surah']} - Layer 2 with Layer 2.5 Channel Additions",
        "",
        "> Generated deterministically from validated overlay JSON. "
        "Layer 2.5 additions are delimited; base prose is unchanged.",
        "",
    ]
    for ayah in sorted(overlay["ayahs"], key=ayah_sort_key):
        lines.extend([f"## {ayah['ayahRef']}", ""])
        base_path = resolve(ayah["baseProse"], overlay_path.parent)
        base_parts = paragraphs(base_path.read_text(encoding="utf-8"))
        by_paragraph: dict[int, list[dict]] = {}
        for insertion in ayah["insertions"]:
            after = insertion["placement"]["afterParagraph"]
            by_paragraph.setdefault(after, []).append(insertion)
        for number, paragraph in enumerate(base_parts, 1):
            lines.extend([paragraph, ""])
            for insertion in by_paragraph.get(number, []):
                lines.extend(
                    [
                        (
                            "<!-- layer-2.5 "
                            f"id={insertion['insertionId']} "
                            f"channel={insertion['channelId']} "
                            f"stage={insertion['stage']} -->"
                        ),
                        insertion["prose_tr"].strip(),
                        "<!-- /layer-2.5 -->",
                        "",
                    ]
                )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("overlays", type=Path)
    parser.add_argument("--integration", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    overlay_path = (
        args.overlays if args.overlays.is_absolute() else ROOT / args.overlays
    )
    integration_path = (
        args.integration
        if args.integration.is_absolute()
        else ROOT / args.integration
    )
    output = args.out or overlay_path.with_name(
        overlay_path.name.removesuffix(".json") + ".preview.md"
    )
    if not output.is_absolute():
        output = ROOT / output
    text = render(overlay_path, integration_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(f"{output} - {len(text.encode('utf-8')):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
