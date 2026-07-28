#!/usr/bin/env python3
"""Assemble ONE self-contained prompt file for a layer-1 stage.

Same contract as `scripts/instantiate.py` at layers 2 and 3 (PLAN.md D-e): the
task document, its governing documents, and the input are inlined in full, and
the agent is told it has no filesystem. That is what makes a cold agent runnable
and two models comparable on verifiably identical bytes.

Usage:
    python3 _translation/v1/tools/instantiate.py --surah 103 --stage anchors
    python3 _translation/v1/tools/instantiate.py --surah 103 --stage translation --language tr
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

V1_DIR = Path(__file__).resolve().parents[1]
ROOT = V1_DIR.parents[1]

WARN_BYTES = 900_000


@dataclass(frozen=True)
class StageSpec:
    name: str
    task_rel: str
    governing_rel: tuple[str, ...]
    needs_language: bool
    output_artifact: str
    response_instruction: str


STAGES: dict[str, StageSpec] = {
    "anchors": StageSpec(
        name="anchors",
        task_rel="_translation/v1/anchor_prompt.md",
        # Stage 0 is Turkish-assisted but emits one shared, root-scoped seed.
        governing_rel=("PRINCIPLES.md", "_translation/README.md"),
        needs_language=False,
        output_artifact="_translation/v1/source/{surah3}.primary-anchors.json",
        response_instruction=(
            "Write the complete `primary-anchor-seed-v4` JSON artifact and "
            "nothing else in the artifact itself."
        ),
    ),
    "translation": StageSpec(
        name="translation",
        task_rel="_translation/v1/prompt.md",
        # The translation writer is deliberately narrow: it sees its task, the
        # output shape, and its bundle. Withholding the commentary principles is
        # the design (`_translation/README.md`), not an omission — layer 1 holds
        # the primary reading still and does not reason about latent readings.
        governing_rel=("_translation/v1/SCHEMA.md",),
        needs_language=True,
        output_artifact="_translation/v1/authored/{language}/{surah3}.authored.json",
        response_instruction=(
            "Write the complete `translation-authored-v1` JSON artifact and "
            "nothing else in the artifact itself."
        ),
    ),
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"error: missing source document: {path}")
    return path.read_text(encoding="utf-8")


def stage_inputs(
    stage: StageSpec,
    surah: int,
    language: str | None,
    input_path: Path | None = None,
) -> list[tuple[str, Path]]:
    surah3 = f"s{surah:03d}"
    if stage.name == "anchors":
        path = input_path or V1_DIR / "anchors" / "input" / f"{surah3}.anchor-input.json"
        return [
            (
                str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                path,
            ),
            (
                "_translation/v1/schema/primary-anchor-seed-v4.schema.json",
                V1_DIR / "schema" / "primary-anchor-seed-v4.schema.json",
            ),
        ]
    bundle_path = input_path or V1_DIR / "input" / str(language) / f"{surah3}.json"
    return [
        (
            str(bundle_path.relative_to(ROOT))
            if bundle_path.is_relative_to(ROOT)
            else str(bundle_path),
            bundle_path,
        ),
        (
            "_translation/v1/schema/translation-authored-v1.schema.json",
            V1_DIR / "schema" / "translation-authored-v1.schema.json",
        ),
    ]


def build_prompt(
    stage: StageSpec,
    surah: int,
    language: str | None,
    run_date: str,
    input_path: Path | None = None,
    output_artifact: str | None = None,
) -> tuple[str, dict]:
    task_text = read_text(ROOT / stage.task_rel)
    governing = [(rel, read_text(ROOT / rel)) for rel in stage.governing_rel]

    inputs: list[tuple[str, str]] = []
    for label, path in stage_inputs(stage, surah, language, input_path):
        if not path.exists():
            raise SystemExit(
                f"error: input not found: {path}\n"
                "run the stage's builder first — see _translation/v1/orchestrator.md"
            )
        inputs.append((label, path.read_text(encoding="utf-8")))

    sources = [(stage.task_rel, len(task_text.encode("utf-8")))]
    sources += [(rel, len(text.encode("utf-8"))) for rel, text in governing]
    sources += [(label, len(text.encode("utf-8"))) for label, text in inputs]

    surah3 = f"s{surah:03d}"
    artifact = output_artifact or stage.output_artifact.format(
        surah3=surah3,
        language=language,
    )

    lines: list[str] = []
    lines.append("# Instantiated Translation-Layer Prompt")
    lines.append("")
    lines.append(f"- surah: {surah}")
    lines.append(f"- stage: {stage.name}")
    if stage.needs_language:
        lines.append(f"- target language: {language}")
    else:
        lines.append(
            "- target language: none - shared branch selection assisted by "
            "the ordinary Turkish baseline"
        )
    lines.append(f"- generated: {run_date}")
    lines.append("- sources (path — bytes):")
    for rel, nbytes in sources:
        lines.append(f"  - `{rel}` — {nbytes:,} bytes")
    lines.append("")
    lines.append(
        "**This file is self-contained.** Every document named above is inlined "
        "in full below, in the order listed. Do not read, fetch, or assume "
        "access to any file on disk or over a network. If a passage below "
        "references another filename, that document is either inlined further "
        "down this same file or deliberately withheld — treat the reference as "
        "an in-document pointer, never as an instruction to go find the file."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append(f"## Task document — `{stage.task_rel}`")
    lines.append("")
    lines.append(task_text.rstrip("\n"))
    lines.append("")
    lines.append("---")
    lines.append("")

    for rel, text in governing:
        lines.append(f"## Governing document — `{rel}`")
        lines.append("")
        lines.append(text.rstrip("\n"))
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Input")
    lines.append("")
    lines.append(
        "The documents below are the only evidence for this stage. Nothing "
        "outside them may be used, and no wording remembered from an existing "
        "translation may enter the output."
    )
    lines.append("")
    for label, text in inputs:
        lines.append(f"### `{label}`")
        lines.append("")
        lines.append("```json")
        lines.append(text.rstrip("\n"))
        lines.append("```")
        lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Your response")
    lines.append("")
    lines.append(f"1. Return the complete JSON artifact for the controller to save.")
    lines.append(f"   {stage.response_instruction}")
    lines.append(f"   The controller will save it exactly at `{artifact}`.")
    lines.append(
        "2. A section headed exactly `=== PROMPT FRICTION ===`, outside the "
        "JSON artifact, reporting where this specification was unclear, "
        "self-contradictory, underspecified, or impossible to follow, and any "
        "point where you had to invent a rule to proceed. Report it every time, "
        "even when the run went cleanly — say so explicitly if you found "
        "nothing. This is how the specification gets improved."
    )
    lines.append("")

    prompt_text = "\n".join(lines).rstrip("\n") + "\n"

    manifest = {
        "surah": surah,
        "stage": stage.name,
        "language": language if stage.needs_language else None,
        "generated": run_date,
        "task_document": {
            "path": stage.task_rel,
            "bytes": len(task_text.encode("utf-8")),
        },
        "governing_documents": [
            {"path": rel, "bytes": len(text.encode("utf-8"))} for rel, text in governing
        ],
        "input_files": [
            {"path": label, "bytes": len(text.encode("utf-8"))} for label, text in inputs
        ],
        "output_artifact": artifact,
        "output_bytes": len(prompt_text.encode("utf-8")),
    }
    return prompt_text, manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--stage", choices=sorted(STAGES), required=True)
    parser.add_argument("--language")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument(
        "--input",
        type=Path,
        help="override the stage input file, useful for chunk pilots",
    )
    parser.add_argument(
        "--artifact",
        help="override the intended output artifact path shown to the agent",
    )
    parser.add_argument(
        "--suffix",
        help="extra file-stem suffix for rendered prompt/manifest names, e.g. '1-5'",
    )
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    stage = STAGES[args.stage]
    if stage.needs_language and not args.language:
        raise SystemExit(f"error: --language is required for stage {stage.name}")
    if not stage.needs_language and args.language:
        raise SystemExit(
            f"error: stage {stage.name} has one shared Turkish-assisted input; "
            "--language does not select a separate anchor run"
        )

    prompt_text, manifest = build_prompt(
        stage,
        args.surah,
        args.language,
        args.date,
        args.input,
        args.artifact,
    )

    surah3 = f"s{args.surah:03d}"
    unit_suffix = f".{args.suffix}" if args.suffix else ""
    suffix = f".{args.language}" if stage.needs_language else ""
    out_dir = args.out or V1_DIR / "prompts"
    out_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = out_dir / f"{surah3}{unit_suffix}.{stage.name}{suffix}.prompt.md"
    manifest_path = out_dir / f"{surah3}{unit_suffix}.{stage.name}{suffix}.manifest.json"

    prompt_path.write_text(prompt_text, encoding="utf-8")
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    size = manifest["output_bytes"]
    print(f"{prompt_path}: {size:,} bytes")
    if size > WARN_BYTES:
        print(
            f"warning: {size:,} bytes is beyond a comfortable context window. "
            "Seed anchors in chunks with build_anchor_input.py --ayahs."
        )


if __name__ == "__main__":
    main()
