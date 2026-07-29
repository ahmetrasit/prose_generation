#!/usr/bin/env python3
"""
instantiate.py — assemble ONE self-contained prompt file per commentary unit.

Turns a bundle (`scripts/build_bundle.py` output) plus its governing documents
into a single file a cold agent — Claude, GPT, anything — can execute without
general filesystem access or repo browsing. Explicit source manifests inside a
bundle may name extra files the agent can read if the run grants file access;
otherwise the prompt remains self-contained. This is what makes runs
reproducible and makes two different models comparable on verifiably identical
input. See `PLAN.md` decisions D-e and D-f, and action 3.

Usage:
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah
    python3 scripts/instantiate.py --surah 100 --layer ayah     # every ayah
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.6-sol-high
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir /tmp/ablation-bundles
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
# Prompt profiles
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PromptProfile:
    name: str
    layer: str
    title: str
    body: str


PROMPT_PROFILES: dict[str, PromptProfile] = {
    "v2.5.5-high": PromptProfile(
        name="v2.5.5-high",
        layer="ayah",
        title="V2 Rendering Profile — 5.5 High",
        body="""This run tests whether `5.5-high` can meet the `5.6-sol-high` reader-facing
quality bar while preserving enough lexical depth for this workflow.

Before drafting, silently build one matrix:

`word -> grammar -> local sense -> root pressure -> unique payoff -> later change`

Render every row exactly once in Turkish. Do not expose the matrix as a list.

Required checks before writing:

- include every `must_integrate` topic;
- include every `candidate` that adds a unique reader payoff;
- collapse all revisions of one v12 `model_id` into one before/after trajectory;
- use branch inventories only when they clarify a word's local effect;
- if `channel_generated_outputs` lists quran-data files and this run gives you
  file access, read only those listed files when channel-family/path detail is
  necessary; they are candidate evidence, not an adjudicated channel ledger;
- keep all artifacts in Turkish;
- explain every technical term in the same sentence.

At first mention of an ayah word, use a structured Arabic surface span:
`{ar:surface_form, tr:Turkish-readable transliteration, gloss:target-language meaning}`.
Use the same full span again when the prose returns to that word after moving to
another word or another paragraph. Inside one short local sequence, after a full
span has just been given, a Turkish label or transliteration is enough. Use
stable terminology for the same word across prose and evidence. Keep raw roots,
root skeletons, letter-by-letter root transliterations, and branch IDs in the
evidence surface. In prose, attach root discussion to the surface word:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-v kökü...`.

The prose should stay reader-facing: one main movement per paragraph, concrete
meaning first, technical precision second. Do not open a paragraph with a
grammar label before the reader knows what is happening. Do not let later ayahs
take over the commentary for 100:1.

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
Default ceiling for this ayah: three. Never stack two negatives in one sentence.
During final revision, rewrite all other negatives as positive predication.
Do not drive negation to zero by default: if no explicit negative is needed,
confirm in friction that there was no live misconception, replacement risk, or
counter-evidence requiring one.

Pass only if the evidence surface could be closed and the prose would still be
understandable to a Turkish reader with almost no Arabic grammar.""",
    ),
    "v2.5.6-sol-high": PromptProfile(
        name="v2.5.6-sol-high",
        layer="ayah",
        title="V2 Rendering Profile — 5.6 Sol High",
        body="""This run tests whether `5.6-sol-high` can increase lexical depth while preserving
reader-facing clarity.

Increase depth through semantic precision, not additional bulk.

Before drafting, silently build a coverage ledger:

- include every `must_integrate` topic;
- include every `candidate` with a reader payoff not already expressed;
- if `v12_reader_responses` is absent because the default workflow retired
  per-ayah focus runs, do not infer a `stage_00` isolated response or
  confidence movement;
- if `v12_focus_trace_hermetic` is present, use its `baseline_models`,
  `context_deltas`, and `surprising_valid_outliers` as reconstructed
  before/after evidence. Do not call it a staged reveal transcript. Preserve
  surprising outliers when they remain anchored in this ayah, especially
  secondary split-root activations;
- include a regular reader-walk, plus/minus-5 reader-walk, whole-surah reading,
  or cross-run-publication item only when it adds a distinct retrospective
  insight or coverage check;
- use branch inventories to support explanations; they create no standalone
  prose obligation. When fallback inventories are present, treat them as
  restricted to this ayah's roots and anchored citations, not as a whole-surah
  obligation.
- if `channel_generated_outputs` lists quran-data files and this run gives you
  file access, read only those listed files when channel-family/path detail is
  necessary. Treat them as candidate/family/path evidence, not as an adjudicated
  channel ledger. State B channel restrictions still apply.

For each critical word, preserve these distinct layers when available:

1. local grammatical work;
2. locally selected sense;
3. coherent pressure supplied by related root branches;
4. one form, sound, rarity, or variant observation with a unique payoff;
5. later contextual change, compressed to its final reader-visible result.

Do not flatten these layers into a general metaphor. Deepen generic summaries by
naming the exact lexical mechanism. Ordering grammar and local meaning first is
grounding, not truth-ranking.

At first mention of an ayah word, use a structured Arabic surface span:
`{ar:surface_form, tr:Turkish-readable transliteration, gloss:target-language meaning}`.
Use the same full span again when the prose returns to that word after moving to
another word or another paragraph. Inside one short local sequence, after a full
span has just been given, a Turkish label or transliteration is enough. Explain
every technical term in the same sentence. Keep raw roots, root skeletons,
letter-by-letter root transliterations, and branch IDs in the evidence surface.
In prose, attach root discussion to the surface word:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-v kökü...`.

Start each paragraph with reader meaning before grammar. Prefer "Âyet önce hamdi
Allah'a verir; bunu fiille değil, sabit bir ad cümlesiyle yapar" over "Bu âyet,
tek bir isim cümlesiyle yerleşik bir hüküm kurar."

For this short ayah, keep at least two-thirds of the prose on its own wording.
Compress all later developments into at most three paragraphs and end with one
plain synthesis paragraph.

Use `v12_cross_run_publication`, if present, only as a compact coverage/priority
check derived from regular and plus/minus-5 reader runs. Do not copy it as prose,
and do not let it override local bundle evidence.

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
Default ceiling for this ayah: three. Never stack two negatives in one sentence.
During final revision, rewrite all other negatives as positive predication.
Do not drive negation to zero by default: if no explicit negative is needed,
confirm in friction that there was no live misconception, replacement risk, or
counter-evidence requiring one.

Pass only if every paragraph has one distinct reader payoff and the prose remains
clear with the evidence surface closed.""",
    ),
    "v2.5.6-sol-max": PromptProfile(
        name="v2.5.6-sol-max",
        layer="ayah",
        title="V2 Rendering Profile — 5.6 Sol Max",
        body="""This run tests whether `5.6-sol-max` can preserve full lexical depth while
meeting or exceeding the reader-facing clarity of the high-effort runs.

Preserve every non-equivalent lexical distinction; do not preserve source-level
repetition. "Full field" means all distinct reader payoffs, not every branch,
stage, caveat, or alternative formulation.

The evidence surface remains exhaustive. It carries stage history, alternative
causes, counter-evidence, identity problems, and inference qualifications.
Moving those details out of prose is compression, not selection.

Collapse:

- one `model_id` across all stages into one before/after trajectory;
- repeated reminders that the primary sense survives into one positive anchor;
- multiple branches that explain one mechanism into one concrete image.

The prose order is:

1. plain translation and speech act;
2. local grammar;
3. word-level lexical depth;
4. one integrated account of the distinct readings;
5. compressed later illumination;
6. plain concluding synthesis.

Later ayahs may deepen the focus ayah but may not become a sequential retelling
of the surah.

If `channel_generated_outputs` lists quran-data files and this run gives you file
access, read only those listed files when channel-family/path detail is
necessary. Treat them as candidate/family/path evidence, not as an adjudicated
channel ledger. State B channel restrictions still apply.

If `v12_focus_trace_hermetic` is present, treat it as a reconstructed focus
trace: baseline models show what the ayah can yield on its own, context deltas
show changed reading after later context, and `surprising_valid_outliers` are
live anchored readings to compress rather than audit away. Do not call it a
`stage_00` / `stage_01` staged run.

At first mention of an ayah word, use a structured Arabic surface span:
`{ar:surface_form, tr:Turkish-readable transliteration, gloss:target-language meaning}`.
Use the same full span again when the prose returns to that word after moving to
another word or another paragraph. Inside one short local sequence, after a full
span has just been given, a Turkish label or transliteration is enough. Keep raw
roots, root skeletons, letter-by-letter root transliterations, and branch IDs in
the evidence surface. In prose, attach root discussion to the surface word:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-v kökü...`.

Lead each paragraph with reader meaning before grammar; place technical
precision after it. Prefer one interpretive move per sentence. For this ayah,
target 900-1050 words, paragraphs under 100 words, and sentences under 32 words.

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
Default ceiling for this ayah: three explicit negative predicates. Run a final
audit for `-maz/-mez`, `değil/değildir`, and `yok/yoktur`. Do not drive
negation to zero by default: if no explicit negative is needed, confirm in
friction that there was no live misconception, replacement risk, or
counter-evidence requiring one.

Before submitting, perform a semantic checksum: every distinct reading remains,
but no sentence merely repeats coverage, containment, or uncertainty already
expressed elsewhere.""",
    ),
    "v2.5.6-sol-high-no-focus": PromptProfile(
        name="v2.5.6-sol-high-no-focus",
        layer="ayah",
        title="Ablation Profile — 5.6 Sol High, No Focus Responses",
        body="""This ablation tests the current default `5.6-sol-high` prose lane without
per-ayah focus-run staged reader responses.

This profile supersedes the task document's normal before/after requirement
when `v12_reader_responses` is deliberately absent. Do not infer a `stage_00`
isolated response, a staged reveal sequence, `changed_reading`, or model
confidence movement. If `v12_focus_trace_hermetic` is also absent because of
ablation, report that absence in evidence coverage and friction, not in prose.

Still write full ayah commentary. Use the remaining sources normally:

- local Quran surface, QAC, `word_morpheme_spans`, and `word_analysis`;
- branch inventories, including surah-fallback inventories when the bundle says
  they were scoped from `full_context_packet.json`; when fallback inventories
  are present, treat them as restricted to this ayah's roots and anchored
  citations, not as a whole-surah obligation;
- dictionary entries and gloss records;
- inter-ayah rows;
- reader walks, plus/minus-5 reader walks, and whole-surah reading, if present,
  only as full-context or retrospective material, never as a substitute for
  missing staged focus responses;
- `v12_cross_run_publication`, if present, only as a compact coverage/priority
  check derived from regular and plus/minus-5 reader runs; do not copy it as
  prose, and do not let it override local bundle evidence;
- `v12_focus_trace_hermetic` is deliberately absent in this ablation;
- `channel_generated_outputs`, if present, only as a file-access manifest for
  generated candidate/family/path evidence; read only listed files when needed,
  and do not treat them as an adjudicated channel ledger;
- channel review material under the normal State B limits.

Keep the normal v2 reader-facing controls: structured Arabic spans at first
mention and again after paragraph/word shifts when the word does fresh work, no
raw roots in prose, positive predication, meaning before grammar, no wrapper
label in prose, and every paragraph with one clear reader payoff.""",
    ),
    "v2.5.6-sol-high-no-reader": PromptProfile(
        name="v2.5.6-sol-high-no-reader",
        layer="ayah",
        title="Ablation Profile — 5.6 Sol High, No Reader-Derived Evidence",
        body="""This ablation tests whether the current default `5.6-sol-high` prose lane can
produce useful commentary from lexical, grammatical, and relation data after
reader-derived material has been deliberately removed.

This profile supersedes every instruction that requires reader-derived sources.
Do not infer or simulate:

- per-ayah focus reader responses;
- Hermetic Focus Trace responses;
- staged before/after reveal trajectories;
- reader walks;
- retrospective surprises;
- whole-surah Turkish reader synthesis;
- first-pass channel-review connections.
- channel generated-output files listed in `channel_generated_outputs`.

If those fields are absent because of ablation, report the absence in evidence
coverage and friction, not in prose.

Write a different kind of output from the normal focus run: a lexical-grammar
commentary anchored in the ayah's own words. Use only the remaining bundle
evidence: Quran surface, QAC, `word_morpheme_spans`, `word_analysis`, branch
inventories, dictionary entries, gloss records, and inter-ayah rows. Later ayahs
may illuminate the focus ayah only when that link is carried by non-reader data
inside `inter_ayah_rows` or by the ayah's own lexical field.

Keep the normal v2 reader-facing controls: structured Arabic spans at first
mention and again after paragraph/word shifts when the word does fresh work, no
raw roots in prose, positive predication, meaning before grammar, no wrapper
label in prose, and every paragraph with one clear reader payoff. Because the
late-arriving reader trajectory is removed, prefer a tighter commentary over
compensating with speculative breadth.""",
    ),
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
    profile: PromptProfile | None = None,
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
        "**This file is self-contained by default.** Every document named above, and every "
        "cross-reference inside them (e.g. \"see `docs/CHANNELS.md` §3.1\"), is "
        "inlined in full below, in the order listed. Do not read, fetch, or "
        "assume access to any file on disk or over a network unless the inlined "
        "bundle contains an explicit source manifest naming that exact file, "
        "such as `channel_generated_outputs.files[]`. If a passage below "
        "references another filename without such a manifest entry, that "
        "document is the one you will find further down this same file — treat "
        "the reference as an in-document pointer, not an instruction to go find "
        "the file."
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
        "order. If you return one combined response, label the parts clearly. "
        "If an orchestrator asks you to write the parts into separate files, "
        "omit wrapper labels from the prose and evidence files; the file path "
        "already supplies the label."
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

    if profile is not None:
        lines.append("---")
        lines.append("")
        lines.append(f"## {profile.title}")
        lines.append("")
        lines.append(profile.body.rstrip("\n"))
        lines.append("")

    prompt_text = "\n".join(lines).rstrip("\n") + "\n"

    manifest = {
        "surah": surah,
        "ayah": ayah,
        "layer": layer.name,
        "language": language,
        "generated": run_date,
        "profile": profile.name if profile is not None else None,
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
        "bundle_root": str(BUNDLES_DIR),
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
        "--bundles-dir",
        type=Path,
        default=None,
        help="Bundle root containing s{NNN}/ directories. Defaults to ./bundles.",
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PROMPT_PROFILES),
        default=None,
        help="Optional prompt rendering profile. The profile name is appended "
        "to the output filename before `.prompt.md`.",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Generation date stamped in the header (YYYY-MM-DD). Defaults to "
        "today. Pass explicitly to reproduce an earlier file byte-for-byte.",
    )
    args = parser.parse_args()

    global BUNDLES_DIR
    if args.bundles_dir is not None:
        BUNDLES_DIR = args.bundles_dir

    layer = LAYER_REGISTRY[args.layer]
    profile = PROMPT_PROFILES[args.profile] if args.profile else None
    run_date = args.date or date.today().isoformat()

    if not layer.per_ayah and args.ayah is not None:
        raise SystemExit(f"error: --layer {layer.name} does not take --ayah")
    if profile is not None and profile.layer != layer.name:
        raise SystemExit(
            f"error: profile {profile.name!r} is for layer {profile.layer!r}, "
            f"not {layer.name!r}"
        )

    out_dir = args.out or (DEFAULT_OUT_ROOT / f"s{args.surah:03d}")
    out_dir.mkdir(parents=True, exist_ok=True)

    if layer.per_ayah:
        ayahs = [args.ayah] if args.ayah is not None else discover_ayahs(args.surah)
    else:
        ayahs = [None]

    profile_note = f", profile {profile.name}" if profile else ""
    print(
        f"instantiate.py — surah {args.surah}, layer {layer.name}, "
        f"language {args.language}, date {run_date}{profile_note}"
    )
    for ayah in ayahs:
        prompt_text, manifest = build_prompt(
            layer, args.surah, ayah, args.language, run_date, profile
        )
        stem = layer.output_stem(args.surah, ayah)
        output_stem = f"{stem}.{profile.name}" if profile else stem
        prompt_path = out_dir / f"{output_stem}.prompt.md"
        manifest_path = out_dir / f"{output_stem}.manifest.json"

        prompt_path.write_text(prompt_text, encoding="utf-8")
        manifest["output_file"] = prompt_path.name
        with manifest_path.open("w", encoding="utf-8") as fh:
            json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=False)
            fh.write("\n")

        report_size(prompt_path)

    print("done.")


if __name__ == "__main__":
    main()
