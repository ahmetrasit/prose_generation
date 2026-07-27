#!/usr/bin/env python3
"""
instantiate.py — assemble ONE self-contained prompt file per commentary unit.

Turns a bundle (`scripts/build_bundle.py` output) plus its governing documents
into a single file a cold agent — Claude, GPT, anything — can execute with no
filesystem access and no repo paths to follow. This is what makes runs
reproducible and makes two different models comparable on verifiably
identical input. See `PLAN.md` decisions D-e and D-f, and action 3.

Usage:
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah
    python3 scripts/instantiate.py --surah 100 --layer ayah     # every ayah
    python3 scripts/instantiate.py --surah 100 --layer surah
    python3 scripts/instantiate.py --surah 100 --layer ayah --language tr --out DIR --date 2026-07-27

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Callable

# ---------------------------------------------------------------------------
# Repo layout
# ---------------------------------------------------------------------------

SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parent.parent  # .../prose_generation

BUNDLES_DIR = ROOT / "bundles"
DEFAULT_OUT_ROOT = ROOT / "_commentary" / "inputs"

# Governing documents shared by every layer, in the order they are inlined.
GOVERNING_DOCS: list[str] = [
    "PRINCIPLES.md",
    "COMMENTARY_SPEC.md",
    "docs/CHANNELS.md",
]

WARN_BYTES = 500_000  # ayah bundles run ~300KB; warn loudly above this


# ---------------------------------------------------------------------------
# Layer registry — adding a layer (e.g. pericope) is registering one entry
# here plus writing its PROMPT.md. Nothing else in this file is layer-specific.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LayerSpec:
    name: str
    task_prompt_rel: str          # path to the task document, relative to ROOT
    per_ayah: bool                # True if a unit is one ayah; False if one surah
    output_stem: Callable[[int, int | None], str]
    bundle_files: Callable[[int, int | None], list[tuple[str, Path]]]
    # bundle_files returns [(label, path), ...] of every bundle JSON that must
    # be inlined for this unit — for layer "surah" this includes every ayah
    # bundle the surah bundle only references by filename.


def _ayah_bundle_path(surah: int, ayah: int) -> Path:
    return BUNDLES_DIR / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json"


def _surah_bundle_path(surah: int) -> Path:
    return BUNDLES_DIR / f"s{surah:03d}" / f"{surah}.surah.json"


def _ayah_bundle_files(surah: int, ayah: int | None) -> list[tuple[str, Path]]:
    assert ayah is not None
    path = _ayah_bundle_path(surah, ayah)
    return [(f"bundles/s{surah:03d}/{path.name}", path)]


def _surah_bundle_files(surah: int, ayah: int | None) -> list[tuple[str, Path]]:
    """The surah bundle references its ayah bundles by filename rather than
    duplicating them (see scripts/README.md). To keep the instantiated prompt
    self-contained, every referenced ayah bundle must be inlined too."""
    surah_path = _surah_bundle_path(surah)
    files: list[tuple[str, Path]] = [
        (f"bundles/s{surah:03d}/{surah_path.name}", surah_path)
    ]
    if surah_path.exists():
        with surah_path.open(encoding="utf-8") as fh:
            surah_bundle = json.load(fh)
        for fname in surah_bundle.get("ayah_bundle_files", []):
            files.append((f"bundles/s{surah:03d}/{fname}", BUNDLES_DIR / f"s{surah:03d}" / fname))
    return files


LAYER_REGISTRY: dict[str, LayerSpec] = {
    "ayah": LayerSpec(
        name="ayah",
        task_prompt_rel="_ayah_commentary/PROMPT.md",
        per_ayah=True,
        output_stem=lambda surah, ayah: f"{surah}_{ayah}.ayah",
        bundle_files=_ayah_bundle_files,
    ),
    "surah": LayerSpec(
        name="surah",
        task_prompt_rel="_surah_commentary/PROMPT.md",
        per_ayah=False,
        output_stem=lambda surah, ayah: f"{surah}.surah",
        bundle_files=_surah_bundle_files,
    ),
    # "pericope": layer 2.5 (PLAN.md D-c). Not registered — its prompt does
    # not exist yet (_pericope_commentary/PROMPT.md). Registering it once that
    # file exists is a matter of adding one more LayerSpec entry above; no
    # other code in this script is layer-specific.
}


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"error: required document not found: {path}")
    return path.read_text(encoding="utf-8")


def discover_ayahs(surah: int) -> list[int]:
    """Every ayah with a bundle file for this surah, in ayah order."""
    surah_dir = BUNDLES_DIR / f"s{surah:03d}"
    if not surah_dir.exists():
        raise SystemExit(f"error: no bundle directory for surah {surah}: {surah_dir}")
    pattern = re.compile(rf"^{surah}_(\d+)\.ayah\.json$")
    found = []
    for p in surah_dir.iterdir():
        m = pattern.match(p.name)
        if m:
            found.append(int(m.group(1)))
    if not found:
        raise SystemExit(f"error: no ayah bundles found under {surah_dir}")
    return sorted(found)


def build_prompt(
    layer: LayerSpec,
    surah: int,
    ayah: int | None,
    language: str,
    run_date: str,
) -> tuple[str, dict]:
    """Return (assembled prompt text, manifest dict) for one unit."""

    task_path = ROOT / layer.task_prompt_rel
    task_text = read_text(task_path)

    governing: list[tuple[str, Path, str]] = []
    for rel in GOVERNING_DOCS:
        p = ROOT / rel
        governing.append((rel, p, read_text(p)))

    bundle_entries = layer.bundle_files(surah, ayah)
    bundles: list[tuple[str, Path, str]] = []
    for label, path in bundle_entries:
        if not path.exists():
            raise SystemExit(f"error: bundle file not found: {path}")
        bundles.append((label, path, path.read_text(encoding="utf-8")))

    # --- sources table for the header ---------------------------------
    sources: list[tuple[str, int]] = []
    sources.append((layer.task_prompt_rel, len(task_text.encode("utf-8"))))
    for rel, _, text in governing:
        sources.append((rel, len(text.encode("utf-8"))))
    for label, _, text in bundles:
        sources.append((label, len(text.encode("utf-8"))))

    unit_label = f"{surah}:{ayah}" if layer.per_ayah else f"{surah} (whole surah)"

    lines: list[str] = []
    lines.append("# Instantiated Commentary Prompt")
    lines.append("")
    lines.append(f"- surah: {surah}")
    lines.append(f"- ayah: {ayah if ayah is not None else '(all — this file covers the whole surah)'}")
    lines.append(f"- unit: {unit_label}")
    lines.append(f"- layer: {layer.name}")
    lines.append(f"- target language: {language}")
    lines.append(f"- generated: {run_date}")
    lines.append("- sources (path — bytes):")
    for rel, nbytes in sources:
        lines.append(f"  - `{rel}` — {nbytes:,} bytes")
    lines.append("")
    lines.append(
        "**This file is self-contained.** Every document named above, and every "
        "cross-reference inside them (e.g. \"see `docs/CHANNELS.md` §3.1\"), is "
        "inlined in full below, in the order listed. Do not read, fetch, or "
        "assume access to any file on disk or over a network. If a passage "
        "below references another filename, that document is the one you will "
        "find further down this same file — treat the reference as an "
        "in-document pointer, not an instruction to go find the file."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- task document ---------------------------------------------------
    lines.append(f"## Task document — `{layer.task_prompt_rel}`")
    lines.append("")
    lines.append(task_text.rstrip("\n"))
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- governing documents ---------------------------------------------
    for rel, _, text in governing:
        lines.append(f"## Governing document — `{rel}`")
        lines.append("")
        lines.append(text.rstrip("\n"))
        lines.append("")
        lines.append("---")
        lines.append("")

    # --- bundle(s) ---------------------------------------------------------
    lines.append("## Input bundle")
    lines.append("")
    if len(bundles) == 1:
        lines.append(
            "The bundle below is the data for this unit. It is the only source "
            "of ayah-specific evidence; nothing outside it may be cited."
        )
    else:
        lines.append(
            "This surah's bundle references its ayah bundles by filename rather "
            "than duplicating their content, so every ayah bundle it references "
            "is inlined below in full, alongside the surah-scope bundle. "
            "Together they are the only source of evidence; nothing outside "
            "them may be cited."
        )
    lines.append("")
    for label, path, text in bundles:
        lines.append(f"### Bundle file — `{label}`")
        lines.append("")
        lines.append("```json")
        lines.append(text.rstrip("\n"))
        lines.append("```")
        lines.append("")
    lines.append("---")
    lines.append("")

    # --- final instruction section ---------------------------------------
    lines.append("## Your response")
    lines.append("")
    lines.append(
        f"Write in {language}. Produce your response as three parts, in this "
        "order, and label each clearly:"
    )
    lines.append("")
    lines.append(
        "1. **The prose** — per the output contract in `COMMENTARY_SPEC.md` §5 "
        "and the task document above: continuous, single voice, no provenance "
        "markers, no headers named after evidence layers."
    )
    lines.append(
        "2. **The evidence surface** — separate from the prose, addressable "
        "per phrase, per `PRINCIPLES.md` §12"
        + (
            " and, for this layer, also the thesis, channel candidates, and "
            "exclusions required by `COMMENTARY_SPEC.md` §5 and "
            "`_surah_commentary/PROMPT.md`."
            if layer.name == "surah"
            else "."
        )
    )
    lines.append(
        "3. A section headed exactly `=== PROMPT FRICTION ===` reporting "
        "honestly where the specification above was unclear, "
        "self-contradictory, underspecified, or impossible to follow, and any "
        "point where you had to invent a rule to proceed. Report this "
        "section every time, even if the run went cleanly — say so explicitly "
        "if you found nothing. This is how the specification gets improved."
    )
    lines.append("")

    prompt_text = "\n".join(lines).rstrip("\n") + "\n"

    manifest = {
        "surah": surah,
        "ayah": ayah,
        "layer": layer.name,
        "language": language,
        "generated": run_date,
        "task_document": {
            "path": layer.task_prompt_rel,
            "bytes": len(task_text.encode("utf-8")),
        },
        "governing_documents": [
            {"path": rel, "bytes": len(text.encode("utf-8"))} for rel, _, text in governing
        ],
        "bundle_files": [
            {"path": label, "bytes": len(text.encode("utf-8"))} for label, _, text in bundles
        ],
        "output_bytes": len(prompt_text.encode("utf-8")),
    }

    return prompt_text, manifest


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def report_size(path: Path) -> None:
    nbytes = path.stat().st_size
    tokens_est = nbytes // 4
    flag = "  *** WARNING: exceeds 500KB — check context-window fit ***" if nbytes > WARN_BYTES else ""
    print(f"  {path} — {nbytes:,} bytes (~{tokens_est:,} tokens){flag}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah", type=int, default=None)
    parser.add_argument("--layer", choices=sorted(LAYER_REGISTRY), required=True)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument(
        "--date",
        default=None,
        help="Generation date stamped in the header (YYYY-MM-DD). Defaults to "
        "today. Pass explicitly to reproduce an earlier file byte-for-byte.",
    )
    args = parser.parse_args()

    layer = LAYER_REGISTRY[args.layer]
    run_date = args.date or date.today().isoformat()

    if not layer.per_ayah and args.ayah is not None:
        raise SystemExit(f"error: --layer {layer.name} does not take --ayah")

    out_dir = args.out or (DEFAULT_OUT_ROOT / f"s{args.surah:03d}")
    out_dir.mkdir(parents=True, exist_ok=True)

    if layer.per_ayah:
        ayahs = [args.ayah] if args.ayah is not None else discover_ayahs(args.surah)
    else:
        ayahs = [None]

    print(f"instantiate.py — surah {args.surah}, layer {layer.name}, language {args.language}, date {run_date}")
    for ayah in ayahs:
        prompt_text, manifest = build_prompt(layer, args.surah, ayah, args.language, run_date)
        stem = layer.output_stem(args.surah, ayah)
        prompt_path = out_dir / f"{stem}.prompt.md"
        manifest_path = out_dir / f"{stem}.manifest.json"

        prompt_path.write_text(prompt_text, encoding="utf-8")
        manifest["output_file"] = prompt_path.name
        with manifest_path.open("w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=False)
            fh.write("\n")

        report_size(prompt_path)

    print("done.")


if __name__ == "__main__":
    main()
