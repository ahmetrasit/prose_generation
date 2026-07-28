#!/usr/bin/env python3
"""Instantiate one lean combined Layer 3 + Layer 2.5 prompt."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

from check_channel_bundle import validate_data as validate_channel_bundle

WORK_ROOT = Path(__file__).resolve().parent.parent
ROOT = WORK_ROOT.parents[2]
INPUTS = WORK_ROOT / "generated" / "inputs"
OUTPUTS = ROOT / "_commentary" / "outputs"


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def source(path: Path, kind: str, text: str | None = None, ayah: int | None = None) -> dict:
    if not path.is_file():
        raise SystemExit(f"error: required input does not exist: {path}")
    file_content = path.read_text(encoding="utf-8")
    content = file_content if text is None else text
    if not content.strip():
        raise SystemExit(f"error: required input is empty: {path}")
    item = {
        "path": rel(path),
        "kind": kind,
        "ayah": ayah,
        "text": content,
        "bytes": len(content.encode("utf-8")),
        "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
    }
    if content != file_content:
        item["sourceFileBytes"] = len(file_content.encode("utf-8"))
        item["sourceFileSha256"] = hashlib.sha256(
            file_content.encode("utf-8")
        ).hexdigest()
    return item


def numbered_sections(path: Path, numbers: set[int]) -> str:
    text = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"(?m)^## ([0-9]+)\.", text))
    selected: list[str] = []
    found = {int(match.group(1)) for match in headings}
    for index, match in enumerate(headings):
        number = int(match.group(1))
        if number not in numbers:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        selected.append(text[match.start():end].rstrip())
    if found & numbers != numbers:
        raise SystemExit(f"error: missing numbered sections {sorted(numbers - found)} in {path}")
    return "\n\n".join(selected) + "\n"


def outputs_dir(surah: int, explicit: Path | None) -> Path:
    if explicit is not None:
        path = explicit if explicit.is_absolute() else ROOT / explicit
        if not path.is_dir():
            raise SystemExit(f"error: --layer2-dir is not a directory: {path}")
        return path
    for path in (
        OUTPUTS / f"s{surah:03d}-default",
        OUTPUTS / f"s{surah:03d}",
    ):
        if path.is_dir():
            return path
    raise SystemExit(f"error: no Layer-2 output directory found for surah {surah}")


def discover_ayahs(surah: int) -> list[int]:
    directory = ROOT / "bundles" / f"s{surah:03d}"
    ayahs = []
    for path in directory.glob(f"{surah}_*.ayah.json"):
        match = re.fullmatch(rf"{surah}_(\d+)\.ayah\.json", path.name)
        if match:
            ayahs.append(int(match.group(1)))
    if not ayahs:
        raise SystemExit(f"error: no ayah bundles found for surah {surah}")
    return sorted(set(ayahs))


def prose_match(directory: Path, surah: int, ayah: int, label: str | None) -> Path:
    if label:
        path = directory / f"{surah}_{ayah}.prose.{label}.md"
        if not path.is_file():
            raise SystemExit(f"error: expected labelled Layer-2 prose does not exist: {path}")
        return path
    exact = directory / f"{surah}_{ayah}.prose.md"
    matches = ([exact] if exact.is_file() else []) + sorted(
        directory.glob(f"{surah}_{ayah}.prose.*.md")
    )
    matches = list(dict.fromkeys(matches))
    if not matches:
        raise SystemExit(f"error: no Layer-2 prose for {surah}:{ayah} in {directory}")
    if len(matches) > 1:
        raise SystemExit(
            f"error: ambiguous Layer-2 prose for {surah}:{ayah}: "
            + ", ".join(path.name for path in matches)
        )
    return matches[0]


def layer2_prose_sources(
    surah: int, directory: Path, label: str | None
) -> list[dict]:
    result = []
    problems = []
    for ayah in discover_ayahs(surah):
        try:
            path = prose_match(directory, surah, ayah, label)
            result.append(source(path, "layer2-prose", ayah=ayah))
        except SystemExit as exc:
            problems.append(str(exc).removeprefix("error: "))
    if problems:
        raise SystemExit("error: unusable Layer-2 prose handoff:\n  " + "\n  ".join(problems))
    return result


def assemble(
    surah: int,
    language: str,
    run_date: str,
    bundle_path: Path,
    layer2_directory: Path | None = None,
    layer2_label: str | None = None,
) -> tuple[str, dict]:
    if language != "tr":
        raise SystemExit("error: Layer 3 commentary currently supports only tr")
    try:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"error: cannot read channel bundle {bundle_path}: {exc}")
    errors = validate_channel_bundle(bundle, surah)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: invalid channel bundle:\n{details}")

    layer2_directory = outputs_dir(surah, layer2_directory)
    prose_sources = layer2_prose_sources(surah, layer2_directory, layer2_label)
    channels_path = WORK_ROOT / "docs" / "CHANNELS.md"
    principles_path = WORK_ROOT / "PRINCIPLES.md"
    spec_path = WORK_ROOT / "COMMENTARY_SPEC.md"
    compact_bundle = json.dumps(bundle, ensure_ascii=False, separators=(",", ":"))
    fixed = [
        source(WORK_ROOT / "layer_3" / "PROMPT.md", "task"),
        source(
            channels_path,
            "governing-excerpt",
            numbered_sections(channels_path, {1, 2, 4}),
        ),
        source(
            principles_path,
            "governing-excerpt",
            numbered_sections(principles_path, {1, 4, 5, 8, 12}),
        ),
        source(
            spec_path,
            "governing-excerpt",
            numbered_sections(spec_path, {1, 2, 4}),
        ),
        source(
            WORK_ROOT / "schemas" / "surah-channel-integration-v1.schema.json",
            "channel-integration-schema",
        ),
        source(
            WORK_ROOT / "schemas" / "ayah-channel-overlays-v1.schema.json",
            "channel-overlay-schema",
        ),
        source(bundle_path, "combined-channel-bundle", compact_bundle),
    ]
    sources = fixed + prose_sources
    lines = [
        "# Instantiated Combined Layer 3 + Layer 2.5",
        "",
        f"- surah: {surah}",
        f"- target language: {language}",
        f"- generated: {run_date}",
        f"- Layer-2 directory: `{rel(layer2_directory)}`",
        f"- Layer-2 label: `{layer2_label or 'unlabelled/unique'}`",
        "- inlined sources (path - bytes - sha256):",
    ]
    for item in sources:
        lines.append(
            f"  - `{item['path']}` - {item['bytes']:,} - `{item['sha256']}`"
        )
    lines.extend(
        [
            "",
            "**Hermeticity rule:** use only the material inlined below. Paths are "
            "provenance and insertion identities, not readable inputs.",
            "",
            "---",
            "",
        ]
    )
    for item in fixed:
        fence = "json" if item["kind"] in {
            "channel-integration-schema",
            "channel-overlay-schema",
            "combined-channel-bundle",
        } else "markdown"
        lines.extend(
            [
                f"## {item['kind']} - `{item['path']}`",
                "",
                f"```{fence}",
                item["text"].rstrip("\n"),
                "```",
                "",
                "---",
                "",
            ]
        )
    lines.extend(
        [
            "## Layer-2 Cold Ayah Prose",
            "",
            "These files remain canonical. Each heading gives the exact "
            "`baseProse` value and required `baseProseSha256` for an overlay.",
            "",
        ]
    )
    for item in prose_sources:
        lines.extend(
            [
                (
                    f"### {surah}:{item['ayah']} - `{item['path']}` "
                    f"- sha256 `{item['sha256']}`"
                ),
                "",
                item["text"].rstrip("\n"),
                "",
            ]
        )

    expected = [
        f"{surah}.surah.prose.md",
        f"{surah}.surah.thesis.md",
        f"{surah}.surah.channels.integrated.json",
        f"{surah}.ayah-channel-overlays.json",
        f"{surah}.surah.exclusions.md",
        f"{surah}.surah.evidence.md",
        f"{surah}.channel.friction.md",
    ]
    lines.extend(
        [
            "---",
            "",
            "## Your Response",
            "",
            "Write exactly " + ", ".join(f"`{name}`" for name in expected) + ".",
            "",
        ]
    )
    prompt = "\n".join(lines)
    manifest = {
        "surah": surah,
        "lane": "combined-layer3-layer2.5",
        "language": language,
        "generated": run_date,
        "layer2Directory": rel(layer2_directory),
        "layer2Label": layer2_label,
        "sources": [
            {
                key: item[key]
                for key in (
                    "path",
                    "kind",
                    "ayah",
                    "bytes",
                    "sha256",
                    "sourceFileBytes",
                    "sourceFileSha256",
                )
                if key in item
            }
            for item in sources
        ],
        "outputBytes": len(prompt.encode("utf-8")),
        "expectedArtifacts": expected,
        "deferred": [],
    }
    return prompt, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", required=True, type=int)
    parser.add_argument("--language", choices=("tr",), default="tr")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--layer2-dir", type=Path)
    parser.add_argument("--layer2-label")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    bundle_path = args.bundle or (
        WORK_ROOT
        / "generated"
        / "bundles"
        / f"s{args.surah:03d}"
        / f"{args.surah}.channel.json"
    )
    if not bundle_path.is_absolute():
        bundle_path = ROOT / bundle_path
    out = args.out or INPUTS / f"s{args.surah:03d}"
    if not out.is_absolute():
        out = ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    prompt, manifest = assemble(
        args.surah,
        args.language,
        args.date,
        bundle_path,
        args.layer2_dir,
        args.layer2_label,
    )
    prompt_path = out / f"{args.surah}.channel.prompt.md"
    manifest_path = out / f"{args.surah}.channel.manifest.json"
    prompt_path.write_text(prompt, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{prompt_path} - {len(prompt.encode('utf-8')):,} bytes")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
