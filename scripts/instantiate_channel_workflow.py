#!/usr/bin/env python3
"""Instantiate channel review, Layer-2.5 integration, and final reconciliation.

These passes run after Layer 3 or the review-led channel draft. They stay
separate from `instantiate.py` because their inputs are authored artifacts, not
one lower-layer output family:

    python3 scripts/instantiate_channel_workflow.py --surah 87 --stage review
    python3 scripts/instantiate_channel_workflow.py --surah 87 --stage integrate
    python3 scripts/instantiate_channel_workflow.py --surah 87 --stage finalize

All prompts are hermetic. They inline the applicable task, governing documents,
schema, surah bundle, Layer-2 outputs, and Layer-3/channel-plan artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from check_channel_plan import validate as validate_channel_plan
from check_channel_overlays import validate as validate_channel_overlays

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_ROOT = ROOT / "_commentary" / "outputs"
INPUTS_ROOT = ROOT / "_commentary" / "inputs"
LAYER2_KINDS = ("prose", "evidence", "index")
GOVERNING = ("PRINCIPLES.md", "COMMENTARY_SPEC.md", "docs/CHANNELS.md")


@dataclass(frozen=True)
class Source:
    label: str
    path: Path
    text: str
    kind: str
    ayah: int | None = None


def relative_label(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def read_source(path: Path, kind: str, ayah: int | None = None) -> Source:
    if not path.is_file():
        raise SystemExit(f"error: required input does not exist: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit(f"error: required input is present but empty: {path}")
    return Source(relative_label(path), path, text, kind, ayah)


def outputs_dir(surah: int, explicit: Path | None) -> Path:
    if explicit is not None:
        path = explicit if explicit.is_absolute() else ROOT / explicit
        if not path.is_dir():
            raise SystemExit(f"error: --outputs-dir is not a directory: {path}")
        return path
    for path in (
        OUTPUTS_ROOT / f"s{surah:03d}-default",
        OUTPUTS_ROOT / f"s{surah:03d}",
    ):
        if path.is_dir():
            return path
    raise SystemExit(f"error: no output directory found for surah {surah}")


def one_match(directory: Path, stem: str, suffix: str, label: str | None) -> Path:
    if label:
        exact = (
            directory / f"{stem}.{suffix[:-3]}.{label}.md"
            if suffix.endswith(".md")
            else directory / f"{stem}.{suffix}.{label}"
        )
        if exact.is_file():
            return exact
        raise SystemExit(f"error: expected labelled input does not exist: {exact}")
    exact = directory / f"{stem}.{suffix}"
    matches = ([exact] if exact.is_file() else []) + sorted(
        directory.glob(f"{stem}.{suffix[:-3]}.*.md")
        if suffix.endswith(".md")
        else directory.glob(f"{stem}.{suffix}.*")
    )
    unique = list(dict.fromkeys(matches))
    if not unique:
        raise SystemExit(f"error: no input matches {directory / (stem + '.' + suffix)}")
    if len(unique) > 1:
        names = ", ".join(path.name for path in unique)
        raise SystemExit(f"error: ambiguous inputs ({names}); pass the relevant label or path")
    return unique[0]


def discover_ayahs(surah: int) -> list[int]:
    directory = ROOT / "bundles" / f"s{surah:03d}"
    ayahs = []
    for path in directory.glob(f"{surah}_*.ayah.json"):
        try:
            ayahs.append(int(path.name.split("_", 1)[1].split(".", 1)[0]))
        except ValueError:
            continue
    if not ayahs:
        raise SystemExit(f"error: no ayah bundles found for surah {surah}")
    return sorted(set(ayahs))


def layer2_sources(directory: Path, surah: int, label: str | None) -> list[Source]:
    sources: list[Source] = []
    problems: list[str] = []
    for ayah in discover_ayahs(surah):
        for kind in LAYER2_KINDS:
            stem = f"{surah}_{ayah}"
            try:
                path = one_match(directory, stem, f"{kind}.md", label)
                sources.append(read_source(path, f"layer2-{kind}", ayah))
            except SystemExit as exc:
                problems.append(str(exc).removeprefix("error: "))
    if problems:
        raise SystemExit("error: unusable Layer-2 handoff:\n  " + "\n  ".join(problems))
    return sources


def explicit_or_default(
    explicit: Path | None,
    directory: Path,
    default_name: str,
    kind: str,
) -> Source:
    path = explicit if explicit is not None else directory / default_name
    if not path.is_absolute():
        path = ROOT / path
    return read_source(path, kind)


def assemble(
    stage: str,
    surah: int,
    language: str,
    run_date: str,
    directory: Path,
    layer2_label: str | None,
    draft_plan: Path | None,
    reviewed_plan: Path | None,
    surah_prose: Path | None,
    surah_evidence: Path | None,
    surah_thesis: Path | None,
    overlays: Path | None,
    overlay_preview: Path | None,
) -> tuple[str, dict]:
    channel_only_review = False
    if stage == "review":
        task_rel = "_channel_review/PROMPT.md"
        schema_rel = "schemas/surah-channel-plan-v1.schema.json"
        plan_source = explicit_or_default(
            draft_plan,
            directory,
            f"{surah}.surah.channels.draft.json",
            "draft-channel-plan",
        )
        try:
            plan_data = json.loads(plan_source.text)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"error: draft channel plan is invalid JSON: {exc}")
        channel_only_review = plan_data.get("sourceLane") == "channel-only"
        authored = [
            plan_source,
            explicit_or_default(
                surah_evidence,
                directory,
                (
                    f"{surah}.channel.adjudication.md"
                    if channel_only_review
                    else f"{surah}.surah.evidence.md"
                ),
                (
                    "channel-draft-adjudication"
                    if channel_only_review
                    else "surah-evidence"
                ),
            ),
        ]
        response = (
            f"Write `{surah}.surah.channels.reviewed.json` and "
            f"`{surah}.surah.channels.review.md` exactly as the task specifies."
        )
    elif stage == "integrate":
        task_rel = "_channel_integration/PROMPT.md"
        schema_rel = "schemas/ayah-channel-overlays-v1.schema.json"
        authored = [
            explicit_or_default(
                reviewed_plan,
                directory,
                f"{surah}.surah.channels.reviewed.json",
                "reviewed-channel-plan",
            ),
            explicit_or_default(
                surah_prose,
                directory,
                f"{surah}.surah.prose.md",
                "surah-prose",
            ),
        ]
        response = (
            f"Write `{surah}.ayah-channel-overlays.json`, "
            f"`{surah}.ayah-channel-overlays.preview.md`, and "
            f"`{surah}.ayah-channel-overlays.friction.md` exactly as the task specifies."
        )
    else:
        task_rel = "_surah_final/PROMPT.md"
        schema_rel = "schemas/ayah-channel-overlays-v1.schema.json"
        authored = [
            explicit_or_default(
                reviewed_plan,
                directory,
                f"{surah}.surah.channels.reviewed.json",
                "reviewed-channel-plan",
            ),
            explicit_or_default(
                surah_prose,
                directory,
                f"{surah}.surah.prose.md",
                "surah-draft-prose",
            ),
            explicit_or_default(
                surah_thesis,
                directory,
                f"{surah}.surah.thesis.md",
                "surah-thesis",
            ),
            explicit_or_default(
                surah_evidence,
                directory,
                f"{surah}.surah.evidence.md",
                "surah-evidence",
            ),
            explicit_or_default(
                overlays,
                directory,
                f"{surah}.ayah-channel-overlays.json",
                "channel-overlays",
            ),
            explicit_or_default(
                overlay_preview,
                directory,
                f"{surah}.ayah-channel-overlays.preview.md",
                "channel-overlay-preview",
            ),
        ]
        response = (
            f"Write `{surah}.surah.final.prose.md`, "
            f"`{surah}.surah.final.validation.md`, and "
            f"`{surah}.surah.final.friction.md` exactly as the task specifies."
        )

    plan_source = authored[0]
    plan_errors = validate_channel_plan(
        plan_source.path,
        "draft" if stage == "review" else "reviewed",
    )
    if plan_errors:
        details = "\n".join(f"  {error}" for error in plan_errors)
        raise SystemExit(
            f"error: {stage} cannot consume an invalid channel plan:\n{details}"
        )
    if stage == "finalize":
        overlay_errors = validate_channel_overlays(
            authored[4].path,
            authored[0].path,
        )
        if overlay_errors:
            details = "\n".join(f"  {error}" for error in overlay_errors)
            raise SystemExit(
                f"error: finalize cannot consume invalid overlays:\n{details}"
            )

    governing = (
        ("PRINCIPLES.md", "docs/CHANNELS.md")
        if channel_only_review
        else GOVERNING
    )
    bundle_path = (
        ROOT / "bundles" / f"s{surah:03d}" / f"{surah}.channel.json"
        if channel_only_review
        else ROOT / "bundles" / f"s{surah:03d}" / f"{surah}.surah.json"
    )
    fixed = [
        read_source(ROOT / task_rel, "task"),
        *(read_source(ROOT / rel, "governing") for rel in governing),
        read_source(ROOT / schema_rel, "schema"),
        read_source(
            ROOT / "schemas" / "surah-channel-plan-v1.schema.json",
            "channel-plan-schema",
        )
        if stage in {"integrate", "finalize"}
        else None,
        read_source(
            bundle_path,
            "channel-draft-bundle" if channel_only_review else "surah-bundle",
        ),
    ]
    fixed = [source for source in fixed if source is not None]
    layer2 = (
        []
        if stage == "finalize" or channel_only_review
        else layer2_sources(directory, surah, layer2_label)
    )
    sources = fixed + authored + layer2

    lines = [
        "# Instantiated Channel Workflow Prompt",
        "",
        f"- surah: {surah}",
        f"- stage: {stage}",
        f"- target language: {language}",
        f"- generated: {run_date}",
        "- sources (path - bytes - sha256):",
    ]
    for source in sources:
        digest = hashlib.sha256(source.text.encode("utf-8")).hexdigest()
        lines.append(
            f"  - `{source.label}` - {len(source.text.encode('utf-8')):,} bytes - `{digest}`"
        )
    lines.extend(
        [
            "",
            "**This prompt is hermetic.** Use only the material inlined below.",
            "",
            "---",
            "",
        ]
    )
    for source in fixed + authored:
        lines.extend(
            [
                f"## {source.kind} - `{source.label}`",
                "",
                "```json" if source.path.suffix == ".json" else "",
                source.text.rstrip("\n"),
                "```" if source.path.suffix == ".json" else "",
                "",
                "---",
                "",
            ]
        )
    if layer2:
        lines.extend(
            [
                "## Layer-2 cold ayah commentaries",
                "",
                "Each ayah was written in isolation. Preserve that independence. "
                "Paths shown in headings are the canonical `baseProse` values for overlays.",
                "",
            ]
        )
        for source in sorted(
            layer2,
            key=lambda item: (
                item.ayah or 0,
                LAYER2_KINDS.index(item.kind.removeprefix("layer2-")),
            ),
        ):
            lines.extend(
                [
                    f"### {surah}:{source.ayah} - {source.kind.removeprefix('layer2-')} - `{source.label}`",
                    "",
                    source.text.rstrip("\n"),
                    "",
                ]
            )
    lines.extend(["---", "", "## Your response", "", response, ""])
    prompt = "\n".join(line for line in lines if line is not None).rstrip() + "\n"
    manifest = {
        "surah": surah,
        "stage": stage,
        "language": language,
        "generated": run_date,
        "outputs_directory": relative_label(directory),
        "layer2_label": layer2_label,
        "source_lane": "channel-only" if channel_only_review else "layer3",
        "sources": [
            {
                "path": source.label,
                "kind": source.kind,
                "ayah": source.ayah,
                "bytes": len(source.text.encode("utf-8")),
                "sha256": hashlib.sha256(source.text.encode("utf-8")).hexdigest(),
            }
            for source in sources
        ],
        "output_bytes": len(prompt.encode("utf-8")),
    }
    return prompt, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--stage", choices=("review", "integrate", "finalize"), required=True)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--outputs-dir", type=Path, default=None)
    parser.add_argument("--layer2-label", default=None)
    parser.add_argument("--draft-plan", type=Path, default=None)
    parser.add_argument("--reviewed-plan", type=Path, default=None)
    parser.add_argument("--surah-prose", type=Path, default=None)
    parser.add_argument("--surah-evidence", type=Path, default=None)
    parser.add_argument("--surah-thesis", type=Path, default=None)
    parser.add_argument("--overlays", type=Path, default=None)
    parser.add_argument("--overlay-preview", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    invalid = []
    if args.stage == "review":
        invalid = [
            flag
            for flag, value in (
                ("--reviewed-plan", args.reviewed_plan),
                ("--surah-prose", args.surah_prose),
                ("--surah-thesis", args.surah_thesis),
                ("--overlays", args.overlays),
                ("--overlay-preview", args.overlay_preview),
            )
            if value is not None
        ]
    elif args.stage == "integrate":
        invalid = [
            flag
            for flag, value in (
                ("--draft-plan", args.draft_plan),
                ("--surah-evidence", args.surah_evidence),
                ("--surah-thesis", args.surah_thesis),
                ("--overlays", args.overlays),
                ("--overlay-preview", args.overlay_preview),
            )
            if value is not None
        ]
    else:
        invalid = [
            flag
            for flag, value in (("--draft-plan", args.draft_plan),)
            if value is not None
        ]
    if invalid:
        raise SystemExit(f"error: {', '.join(invalid)} do not apply to stage {args.stage}")

    directory = outputs_dir(args.surah, args.outputs_dir)
    out = args.out or INPUTS_ROOT / f"s{args.surah:03d}"
    if not out.is_absolute():
        out = ROOT / out
    out.mkdir(parents=True, exist_ok=True)
    prompt, manifest = assemble(
        args.stage,
        args.surah,
        args.language,
        args.date,
        directory,
        args.layer2_label,
        args.draft_plan,
        args.reviewed_plan,
        args.surah_prose,
        args.surah_evidence,
        args.surah_thesis,
        args.overlays,
        args.overlay_preview,
    )
    suffix = {
        "review": "channel-review",
        "integrate": "channel-integration",
        "finalize": "surah-final",
    }[args.stage]
    stem = f"{args.surah}.{suffix}"
    prompt_path = out / f"{stem}.prompt.md"
    manifest_path = out / f"{stem}.manifest.json"
    prompt_path.write_text(prompt, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{prompt_path} - {len(prompt.encode('utf-8')):,} bytes")
    print(f"{manifest_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
