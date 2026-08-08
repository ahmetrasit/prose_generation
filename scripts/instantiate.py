#!/usr/bin/env python3
"""
instantiate.py — assemble ONE self-contained prompt file per commentary unit.

Turns a bundle (for Layer 2, the required `scripts/tier_branch_payloads.py`
output derived from the full `scripts/build_bundle.py` bundle) plus its governing
documents into a single file a cold agent — Claude, GPT, anything — can execute without
general filesystem access or repo browsing. Explicit source manifests inside a
bundle may name extra files the agent can read if the run grants file access;
otherwise the prompt remains self-contained. This is what makes runs
reproducible and makes two different models comparable on verifiably identical
input. See `PLAN.md` decisions D-e and D-f, and action 3.

Usage:
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir bundles-layer2
    python3 scripts/instantiate.py --surah 100 --layer ayah --bundles-dir bundles-layer2
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir bundles-layer2 --profile v2.5.6-sol-high
    python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir _commentary/work/ablation-bundles
    python3 scripts/instantiate.py --surah 100 --layer surah
    python3 scripts/instantiate.py --surah 100 --layer surah --layer2-dir _commentary/outputs/s100-default
    python3 scripts/instantiate.py --surah 100 --layer ayah --bundles-dir bundles-layer2 --language tr --out DIR --date 2026-07-27

Layer 3 consumes layer 2's *outputs*, not the raw ayah bundles (`PLAN.md` D-c).
Inlining the raw bundles produced a 907k-token prompt for an 11-ayah surah;
inlining the layer-2 prose and evidence surfaces instead produces ~90k for the
same surah, and it is also the correct contract — layer 3 is supposed to read
commentary written in isolation, not re-derive it. `--inline-ayah-bundles`
restores the old behaviour for the shortest surahs.

Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
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
OUTPUTS_ROOT = ROOT / "_commentary" / "outputs"

# Set from the CLI; see the module docstring. LAYER2_DIR/LAYER2_LABEL pick which
# layer-2 run feeds layer 3, INLINE_AYAH_BUNDLES restores the raw-bundle path.
LAYER2_DIR: Path | None = None
LAYER2_LABEL: str | None = None
INLINE_AYAH_BUNDLES = False

# Governing documents shared by every layer, in the order they are inlined.
GOVERNING_DOCS: list[str] = [
    "PRINCIPLES.md",
    "COMMENTARY_SPEC.md",
    "docs/CHANNELS.md",
]

# Ayah bundles run ~300KB. A layer-3 prompt is the surah bundle plus every
# layer-2 output and is expected to be larger; S100 lands near 500KB.
WARN_BYTES = {"ayah": 500_000, "surah": 1_200_000}
DEFAULT_WARN_BYTES = 500_000


# ---------------------------------------------------------------------------
# Layer registry for source-to-commentary layers.
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
    # be inlined for this unit.
    upstream_docs: Callable[[int], tuple[list["UpstreamDoc"], dict]] | None = None
    # upstream_docs returns the authored outputs of the layer below, which are
    # this layer's evidence. Only layer 3 has one.


@dataclass(frozen=True)
class UpstreamDoc:
    """One authored output file from the layer below — layer-2 prose, evidence,
    or findings index. Inlined as markdown, not as a bundle."""
    rel: str          # display path, relative to ROOT
    path: Path
    ayah: int
    kind: str
    text: str


# Which layer-2 output kinds layer 3 reads, in the order they are inlined.
# `friction` is deliberately absent: it reports on the instructions, not on the
# ayah, and it is apparatus for the prompt author rather than evidence.
LAYER2_KINDS = ("prose", "evidence", "index")


def _ayah_bundle_path(surah: int, ayah: int) -> Path:
    return BUNDLES_DIR / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json"


def _bundle_label(path: Path) -> str:
    """Return the prompt-facing path for the actual configured bundle file."""
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _surah_bundle_path(surah: int) -> Path:
    return BUNDLES_DIR / f"s{surah:03d}" / f"{surah}.surah.json"


def _ayah_bundle_files(surah: int, ayah: int | None) -> list[tuple[str, Path]]:
    assert ayah is not None
    path = _ayah_bundle_path(surah, ayah)
    return [(_bundle_label(path), path)]


def _surah_bundle_files(surah: int, ayah: int | None) -> list[tuple[str, Path]]:
    """Surah-scope bundle only, unless --inline-ayah-bundles is passed.

    The surah bundle references its ayah bundles by filename rather than
    duplicating them (see scripts/README.md). Inlining them all is what made the
    S100 layer-3 prompt 907k tokens; layer 3's evidence is layer 2's *output*,
    which `_layer2_outputs` supplies. The raw path is kept for short surahs and
    for reproducing the measurement in `PLAN.md`."""
    surah_path = _surah_bundle_path(surah)
    files: list[tuple[str, Path]] = [
        (_bundle_label(surah_path), surah_path)
    ]
    if INLINE_AYAH_BUNDLES and surah_path.exists():
        with surah_path.open(encoding="utf-8") as fh:
            surah_bundle = json.load(fh)
        for fname in surah_bundle.get("ayah_bundle_files", []):
            ayah_path = BUNDLES_DIR / f"s{surah:03d}" / fname
            files.append((_bundle_label(ayah_path), ayah_path))
    return files


def _layer2_dir(surah: int) -> Path:
    if LAYER2_DIR is not None:
        if not LAYER2_DIR.is_dir():
            raise SystemExit(f"error: --layer2-dir is not a directory: {LAYER2_DIR}")
        return LAYER2_DIR
    candidates = [OUTPUTS_ROOT / f"s{surah:03d}-default", OUTPUTS_ROOT / f"s{surah:03d}"]
    for path in candidates:
        if path.is_dir():
            return path
    looked = "\n".join(f"  {p}" for p in candidates)
    raise SystemExit(
        f"error: no layer-2 output directory for surah {surah}. Looked for:\n"
        f"{looked}\nRun layer 2 first, or pass --layer2-dir."
    )


def _layer2_matches(dir_: Path, surah: int, ayah: int, kind: str) -> list[Path]:
    """Output files for one ayah and kind. Labelled comparative runs carry the
    label before `.md` (`100_1.prose.default.v2.5.6-sol-high.md`)."""
    if LAYER2_LABEL is not None:
        exact = dir_ / f"{surah}_{ayah}.{kind}.{LAYER2_LABEL}.md"
        return [exact] if exact.exists() else []
    # The literal dot after the ayah keeps 100_1 from matching 100_10.
    return sorted(dir_.glob(f"{surah}_{ayah}.{kind}.md")) + sorted(
        dir_.glob(f"{surah}_{ayah}.{kind}.*.md")
    )


def _layer2_outputs(surah: int) -> tuple[list[UpstreamDoc], dict]:
    """Every layer-2 output that feeds layer 3, plus a coverage record.

    Preflights like the builder does: enumerate every expected file and abort
    with the complete gap list, never the first failure. A file that exists but
    holds nothing is a hard failure, not an absence — that confusion is this
    repo's defining bug class (`_commentary/ORCHESTRATION.md`, stage 1)."""
    dir_ = _layer2_dir(surah)
    try:
        rel_dir = dir_.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        rel_dir = str(dir_)

    docs: list[UpstreamDoc] = []
    missing_required: list[str] = []
    missing_index: list[int] = []
    index_without_surprise: list[int] = []
    empty: list[str] = []
    ambiguous: list[str] = []

    for ayah in discover_ayahs(surah):
        for kind in LAYER2_KINDS:
            unit = f"{surah}_{ayah}.{kind}"
            matches = _layer2_matches(dir_, surah, ayah, kind)
            if len(matches) > 1:
                names = ", ".join(m.name for m in matches)
                ambiguous.append(f"{unit}: {names}")
                continue
            if not matches:
                if kind == "index":
                    missing_index.append(ayah)
                else:
                    missing_required.append(unit)
                continue
            path = matches[0]
            text = path.read_text(encoding="utf-8")
            if not text.strip():
                empty.append(path.name)
                continue
            if kind == "index" and not re.search(
                r"(?m)^\s*-\s+`surprise:[^`]+`\s+[—-]\s+",
                text,
            ):
                index_without_surprise.append(ayah)
            docs.append(
                UpstreamDoc(
                    rel=f"{rel_dir}/{path.name}",
                    path=path,
                    ayah=ayah,
                    kind=kind,
                    text=text,
                )
            )

    problems: list[str] = []
    if missing_required:
        problems.append(
            "missing layer-2 outputs (required):\n"
            + "\n".join(f"  {u}" for u in missing_required)
        )
    if empty:
        problems.append(
            "layer-2 outputs present but empty (never reported as absent):\n"
            + "\n".join(f"  {n}" for n in empty)
        )
    if ambiguous:
        problems.append(
            "several labelled runs match; pass --layer2-label to choose one:\n"
            + "\n".join(f"  {a}" for a in ambiguous)
        )
    if problems:
        raise SystemExit(
            f"error: layer-2 outputs under {dir_} are not usable as layer-3 input.\n"
            + "\n".join(problems)
        )

    coverage = {
        "directory": rel_dir,
        "label": LAYER2_LABEL,
        "kinds": list(LAYER2_KINDS),
        "ayahs": len(discover_ayahs(surah)),
        "index_absent_for_ayahs": missing_index,
        "surprise_rows_absent_for_ayahs": index_without_surprise,
    }
    return docs, coverage


LAYER_REGISTRY: dict[str, LayerSpec] = {
    "ayah": LayerSpec(
        name="ayah",
        task_prompt_rel="_ayah_commentary/v1/PROMPT.md",
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
        upstream_docs=_layer2_outputs,
    ),
    # Optional long-surah pericope compression is pass 2P, not Layer 2.5, and
    # remains unimplemented. Post-Layer-3 channel passes are instantiated by
    # scripts/instantiate_channel_workflow.py because they consume several
    # authored artifact families rather than one lower layer.
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
include a profile-specific style audit in friction confirming that there was no
live misconception, replacement risk, or counter-evidence requiring one.

Pass only if the evidence surface could be closed and the prose would still be
understandable to a Turkish reader with almost no Arabic grammar.""",
    ),
    "v2.5.6-sol-high": PromptProfile(
        name="v2.5.6-sol-high",
        layer="ayah",
        title="V2 Rendering Profile — 5.6 Sol High",
        body="""This run tests whether `5.6-sol-high` can increase lexical depth while preserving
reader-facing clarity.

Increase depth through semantic precision. Add as much prose as distinct,
significant reader payoffs require, but no bulk that merely repeats evidence.

Before drafting, silently build a coverage ledger:

- include every `must_integrate` topic;
- include every `candidate` with a reader payoff not already expressed;
- judge each candidate independently before synthesis. The number of words,
  roots, or already admitted findings must not raise its admission threshold;
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
- treat `root_lexicon` as identity-complete but payload-tiered by the required
  pre-Layer-2 transform. Every dominant/non-dominant root and dictionary
  `branch_ref` remains; inspect `payload_tier` and
  `coverage.root_lexicon.branch_policy`. `explicit_interest` is full except for
  the globally removed `what_is_not_ar` and boundary note; safety/compact tiers
  intentionally carry less detail and may use `semantic_fallback`. If multiple
  QAC roots map to the same Furuq root, use `qac_roots_ar` /
  `qac_root_mappings` for attribution. Branches remain evidence support, not
  independent prose obligations. Full field means all distinct reader payoffs
  from activated material, not every dictionary branch for the root. A payload
  tier controls storage only: it is neither prose priority nor permission to
  suppress a qualifying compact-branch finding.
- if `channel_generated_outputs` lists quran-data files and this run gives you
  file access, read only those listed files when channel-family/path detail is
  necessary. Treat them as candidate/family/path evidence, not as an adjudicated
  channel ledger. State B channel restrictions still apply.

For each critical word, preserve these distinct layers when available:

1. local grammatical work;
2. locally selected sense;
3. coherent pressure supplied by activated or cited root branches;
4. one form, sound, rarity, or variant observation with a unique payoff;
5. later contextual change, integrated into its reader-visible result without
   dropping a distinct surprise.

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

A paragraph may begin with the ayah's surface, a concrete image, or a
reader-facing claim. It may not begin with a bare grammar label or stacked
abstractions. Prefer "Âyet önce hamdi Allah'a verir; sabit ad cümlesi bu hamdi
yerleşik bir hüküm olarak taşır" over "Bu âyet, tek bir isim cümlesiyle yerleşik
bir hüküm kurar."

Keep the ayah's own wording as the grounding surface. There is no paragraph or
word-count ceiling: let the number of paragraphs follow the number of materially
distinct findings. Synthesize related later developments, but retain every
anchored latent activation or surprise with a significant reader payoff. Omit
fluff, repetition, and findings that do not change understanding.

Use `v12_cross_run_publication`, if present, only as a compact coverage/priority
check derived from regular and plus/minus-5 reader runs. Do not copy it as prose,
and do not let it override local bundle evidence.

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
Default ceiling for this ayah: three. Never stack two negatives in one sentence.
During final revision, rewrite all other negatives as positive predication.
Do not drive negation to zero by default: if no explicit negative is needed,
include a profile-specific style audit in friction confirming that there was no
live misconception, replacement risk, or counter-evidence requiring one.

Pass only if every paragraph has one distinct reader payoff and the prose remains
clear with the evidence surface closed.""",
    ),
    "v2.5.6-sol-max": PromptProfile(
        name="v2.5.6-sol-max",
        layer="ayah",
        title="V2 Rendering Profile — Focus-Aware Default",
        body="""This run uses the shared focus-aware rendering contract for every comparator
model. Preserve full lexical depth while keeping the prose reader-facing and
clear.

Preserve every non-equivalent lexical distinction and every materially distinct,
anchored surprise; do not preserve source-level repetition. "Full field" means
all distinct reader payoffs, not every available branch, stage, caveat, or
alternative formulation.

The evidence surface remains exhaustive. It carries stage history, alternative
causes, counter-evidence, identity problems, and inference qualifications.
Technical support may remain there, but a finding with a significant reader
payoff must remain intelligible in prose; apparatus is not a place to hide a
surprising reading merely to shorten the commentary.

Collapse:

- one `model_id` across all stages into one before/after trajectory;
- repeated reminders that the primary sense survives into one positive anchor;
- multiple branches into one concrete image only when they explain the same
  mechanism and have the same reader payoff.

The prose order is:

1. plain translation and speech act;
2. local grammar;
3. word-level lexical depth;
4. an explicit account of every distinct reading, synthesized only where no
   mechanism or reader payoff is lost;
5. integrated later illumination;
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
live anchored readings to express when they have a significant payoff rather
than audit away. Do not call it a
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
precision after it. Prefer one interpretive move per sentence. There is no
paragraph count or target word count. Length follows the distinct significant
findings; repetition, filler, and findings without a changed understanding do
not justify length.

Use an explicit negative predicate only to correct a likely misconception,
protect the primary sense from replacement, or preserve live counter-evidence.
Default ceiling for this ayah: three explicit negative predicates. Run a final
audit for `-maz/-mez`, `değil/değildir`, and `yok/yoktur`. Do not drive negation
to zero by default: if no explicit negative is needed, include a
profile-specific style audit in friction confirming that there was no live
misconception, replacement risk, or counter-evidence requiring one.

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
when `v12_reader_responses` and `v12_focus_trace_hermetic` are deliberately
absent. Do not infer a `stage_00` isolated response, a staged reveal sequence,
`changed_reading`, or model confidence movement. If those sources are absent
because of ablation, record the absence in evidence coverage, and mention it in
friction only if a live instruction depended on it. Do not mention the absence
in prose.

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
- `v12_focus_trace_hermetic` is deliberately absent in this ablation;
- `v12_cross_run_publication`, if present, only as a compact coverage/priority
  check derived from regular and plus/minus-5 reader runs; do not copy it as
  prose, and do not let it override local bundle evidence;
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

If those fields are absent because of ablation, record the absence in evidence
coverage, and mention it in friction only if a live instruction depended on it.
Do not mention the absence in prose.

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


_SHARED_FOCUS_AWARE_PROFILE = PROMPT_PROFILES["v2.5.6-sol-max"]
for _profile_name in ("v2.5.5-high", "v2.5.6-sol-high", "v2.5.6-sol-max"):
    PROMPT_PROFILES[_profile_name] = PromptProfile(
        name=_profile_name,
        layer=_SHARED_FOCUS_AWARE_PROFILE.layer,
        title=_SHARED_FOCUS_AWARE_PROFILE.title,
        body=_SHARED_FOCUS_AWARE_PROFILE.body,
    )


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"error: required document not found: {path}")
    return path.read_text(encoding="utf-8")


def compact_json_text(path: Path, text: str) -> str:
    """Render JSON without insignificant whitespace for agent-facing prompts."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: invalid JSON bundle {path}: {exc}") from exc
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


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
    require_focus_trace: bool = False,
) -> tuple[str, dict]:
    """Return (assembled prompt text, manifest dict) for one unit."""

    task_path = ROOT / layer.task_prompt_rel
    task_text = read_text(task_path)

    governing_rels = list(GOVERNING_DOCS)
    if layer.name == "surah":
        governing_rels.append("schemas/surah-channel-plan-v1.schema.json")
    governing: list[tuple[str, Path, str]] = []
    for rel in governing_rels:
        p = ROOT / rel
        governing.append((rel, p, read_text(p)))

    bundle_entries = layer.bundle_files(surah, ayah)
    bundles: list[tuple[str, Path, str, str, dict]] = []
    for label, path in bundle_entries:
        if not path.exists():
            raise SystemExit(f"error: bundle file not found: {path}")
        source_text = path.read_text(encoding="utf-8")
        try:
            bundle_json = json.loads(source_text)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"error: bundle file is not valid JSON: {path}: {exc}") from exc
        if require_focus_trace and layer.name == "ayah":
            hft_coverage = (bundle_json.get("coverage") or {}).get(
                "v12_focus_trace_hermetic"
            ) or {}
            hft_readers = (
                (bundle_json.get("v12_focus_trace_hermetic") or {}).get("readers")
                or {}
            )
            if not hft_coverage.get("present") or not hft_readers:
                raise SystemExit(
                    "error: --require-focus-trace requested, but bundle lacks "
                    f"HFT readers: {path}"
                )
        bundles.append(
            (label, path, source_text, compact_json_text(path, source_text), bundle_json)
        )

    upstream: list[UpstreamDoc] = []
    upstream_coverage: dict = {}
    if layer.upstream_docs is not None and not INLINE_AYAH_BUNDLES:
        upstream, upstream_coverage = layer.upstream_docs(surah)

    # --- sources table for the header ---------------------------------
    sources: list[tuple[str, int]] = []
    sources.append((layer.task_prompt_rel, len(task_text.encode("utf-8"))))
    for rel, _, text in governing:
        sources.append((rel, len(text.encode("utf-8"))))
    for label, _, source_text, prompt_text, _ in bundles:
        if source_text == prompt_text:
            sources.append((label, len(prompt_text.encode("utf-8"))))
        else:
            sources.append((
                f"{label} (compacted in prompt; source {len(source_text.encode('utf-8')):,} bytes)",
                len(prompt_text.encode("utf-8")),
            ))
    for doc in upstream:
        sources.append((doc.rel, len(doc.text.encode("utf-8"))))

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
    if layer.name == "surah" and not INLINE_AYAH_BUNDLES:
        lines.append(
            "The bundle below is **surah scope only** — the surah's text, its "
            "whole-surah reading, the first-pass channel review, the channel "
            "generated-output manifest, and its pericope spans. The per-ayah "
            "evidence is not here. It reaches you as the layer-2 commentary in "
            "the next section, which is what this level is specified to consume."
        )
    elif len(bundles) == 1:
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
    for label, path, _source_text, prompt_text, _bundle_json in bundles:
        lines.append(f"### Bundle file — `{label}`")
        lines.append("")
        lines.append("```json")
        lines.append(prompt_text)
        lines.append("```")
        lines.append("")
    lines.append("---")
    lines.append("")

    # --- layer-2 outputs, for layer 3 --------------------------------------
    if upstream:
        lines.append("## Layer-2 commentary — the ayah readings")
        lines.append("")
        lines.append(
            "Each ayah below was written by a separate cold agent that saw only "
            "that ayah's own bundle, in isolation, with no knowledge of this "
            "surah or of any argument about it. That isolation is what you "
            "depend on: these readings cannot have been retro-fitted to a "
            "thesis, including yours."
        )
        lines.append("")
        lines.append(
            "Per ayah you receive the **prose** (what the reading says), the "
            "**evidence surface** (what it traces to — bundle refs, branch IDs, "
            "counter-evidence, coverage, with inference marked as inference), "
            "and the **findings index** where one exists (one line per reading "
            "the prose carries, plus explicit `surprise:<id>` synthesis rows "
            "marked `[supports-primary]` or `[shifts-primary]`). Friction "
            "reports are deliberately excluded: "
            "they report on the instructions, not on the ayah."
        )
        lines.append("")
        lines.append(
            "**The raw ayah bundles are not inlined, and this is the contract, "
            "not a shortfall.** Layer 3 reads commentary, not source. Anything "
            "you cite at ayah level must appear in one of these files or in the "
            "surah-scope bundle above. If a reading you need is not here, it is "
            "not available to you — say so rather than reconstructing it "
            "(`PRINCIPLES.md` §1 and §7)."
        )
        lines.append("")
        if upstream_coverage.get("index_absent_for_ayahs"):
            absent = ", ".join(
                f"{surah}:{a}" for a in upstream_coverage["index_absent_for_ayahs"]
            )
            lines.append(
                f"Layer-2 coverage: no findings index exists for {absent}. For "
                "those ayahs the prose and evidence surface are the complete "
                "record of what layer 2 carried; there is no separate list of "
                "its readings to check your exclusions against."
            )
            lines.append("")
        if upstream_coverage.get("surprise_rows_absent_for_ayahs"):
            absent = ", ".join(
                f"{surah}:{a}"
                for a in upstream_coverage["surprise_rows_absent_for_ayahs"]
            )
            lines.append(
                f"Layer-2 local-surprise handoff gap: the findings indexes for "
                f"{absent} contain no explicit `surprise:<id>` synthesis row. "
                "This does not prove that their prose has no secondary "
                "resonance; it means layer 2 did not state whether such a "
                "resonance supports or shifts the primary. Inspect the prose "
                "and evidence, and record the missing explicit relation rather "
                "than silently inventing it."
            )
            lines.append("")
        for doc in sorted(upstream, key=lambda d: (d.ayah, LAYER2_KINDS.index(d.kind))):
            lines.append(f"### {surah}:{doc.ayah} — {doc.kind} — `{doc.rel}`")
            lines.append("")
            lines.append(doc.text.rstrip("\n"))
            lines.append("")
        lines.append("---")
        lines.append("")

    # --- final instruction section ---------------------------------------
    lines.append("## Your response")
    lines.append("")
    if layer.name == "surah":
        lines.append(
            f"Write in {language}. Produce the six separately named artifacts "
            "specified in `_surah_commentary/PROMPT.md`: prose, thesis, draft "
            "channel plan JSON, exclusions, evidence, and friction. Do not "
            "collapse them into a three-part response. The prose file has no "
            "wrapper label; the path already supplies it."
        )
    else:
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
            "per phrase, per `PRINCIPLES.md` §12."
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
        "bundle_files": [],
        "bundle_root": str(BUNDLES_DIR),
        "output_bytes": len(prompt_text.encode("utf-8")),
    }
    for label, _, source_text, inlined_text, bundle_json in bundles:
        hft_coverage = (bundle_json.get("coverage") or {}).get(
            "v12_focus_trace_hermetic"
        )
        hft_readers = (
            (bundle_json.get("v12_focus_trace_hermetic") or {}).get("readers")
            or {}
        )
        manifest["bundle_files"].append(
            {
                "path": label,
                "source_bytes": len(source_text.encode("utf-8")),
                "inlined_bytes": len(inlined_text.encode("utf-8")),
                "sha256": hashlib.sha256(source_text.encode("utf-8")).hexdigest(),
                "bundle_generated_at": bundle_json.get("generated_at"),
                "hft_present": bool(
                    isinstance(hft_coverage, dict) and hft_coverage.get("present")
                ),
                "hft_reader_keys": sorted(hft_readers),
                "rendering": "compact-json",
            }
        )

    if layer.upstream_docs is not None:
        manifest["upstream_layer"] = {
            "layer": "ayah",
            "inline_ayah_bundles": INLINE_AYAH_BUNDLES,
            "coverage": upstream_coverage,
            "files": [
                {
                    "path": doc.rel,
                    "ayah": doc.ayah,
                    "kind": doc.kind,
                    "bytes": len(doc.text.encode("utf-8")),
                }
                for doc in sorted(
                    upstream, key=lambda d: (d.ayah, LAYER2_KINDS.index(d.kind))
                )
            ],
        }

    return prompt_text, manifest


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def report_size(path: Path, layer: LayerSpec) -> None:
    nbytes = path.stat().st_size
    # Crude, and low for Arabic and Turkish, which run more tokens per byte.
    tokens_est = nbytes // 4
    limit = WARN_BYTES.get(layer.name, DEFAULT_WARN_BYTES)
    flag = (
        f"  *** WARNING: exceeds {limit // 1000}KB — check context-window fit ***"
        if nbytes > limit
        else ""
    )
    print(f"  {path} — {nbytes:,} bytes (~{tokens_est:,} tokens, low estimate){flag}")


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
    parser.add_argument(
        "--layer2-dir",
        type=Path,
        default=None,
        help="Layer 3 only. Directory of layer-2 outputs to feed layer 3. "
        "Defaults to _commentary/outputs/s{NNN}-default, then s{NNN}.",
    )
    parser.add_argument(
        "--layer2-label",
        default=None,
        help="Layer 3 only. Comparative-run label of the layer-2 outputs to "
        "use, e.g. `default.v2.5.6-sol-high`. Required when several labelled "
        "runs are present in the directory.",
    )
    parser.add_argument(
        "--inline-ayah-bundles",
        action="store_true",
        help="Layer 3 only. Inline every raw ayah bundle instead of reading "
        "layer-2 outputs. Reproduces the pre-2026-07-28 prompt; ~907k tokens "
        "for an 11-ayah surah, so viable only for the shortest surahs.",
    )
    parser.add_argument(
        "--require-focus-trace",
        action="store_true",
        help="Ayah prompts only. Refuse to instantiate unless each inlined "
        "bundle has v12_focus_trace_hermetic.present=true and at least one reader.",
    )
    args = parser.parse_args()

    global BUNDLES_DIR, LAYER2_DIR, LAYER2_LABEL, INLINE_AYAH_BUNDLES
    if args.bundles_dir is not None:
        BUNDLES_DIR = args.bundles_dir
    LAYER2_DIR = args.layer2_dir
    LAYER2_LABEL = args.layer2_label
    INLINE_AYAH_BUNDLES = args.inline_ayah_bundles

    layer = LAYER_REGISTRY[args.layer]
    profile = PROMPT_PROFILES[args.profile] if args.profile else None
    run_date = args.date or date.today().isoformat()

    if not layer.per_ayah and args.ayah is not None:
        raise SystemExit(f"error: --layer {layer.name} does not take --ayah")
    if layer.upstream_docs is None:
        for flag, value in (
            ("--layer2-dir", args.layer2_dir),
            ("--layer2-label", args.layer2_label),
            ("--inline-ayah-bundles", args.inline_ayah_bundles),
        ):
            if value:
                raise SystemExit(
                    f"error: {flag} applies to a layer that consumes the layer "
                    f"below it, not to --layer {layer.name}"
                )
    if profile is not None and profile.layer != layer.name:
        raise SystemExit(
            f"error: profile {profile.name!r} is for layer {profile.layer!r}, "
            f"not {layer.name!r}"
        )
    if args.require_focus_trace and layer.name != "ayah":
        raise SystemExit("error: --require-focus-trace applies only to --layer ayah")

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
            layer,
            args.surah,
            ayah,
            args.language,
            run_date,
            profile,
            args.require_focus_trace,
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

        report_size(prompt_path, layer)

    print("done.")


if __name__ == "__main__":
    main()
