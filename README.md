# Prose Generation

This repository authors the reader-facing content for the Quran reader: the
translation spine, ayah commentary, and surah commentary. Upstream repositories
produce evidence; this one adjudicates it and writes prose.

## Who this is for

One reader, concretely: a curious Turkish speaker with almost no Arabic grammar,
whose Arabic vocabulary arrives through loanwords — and whose theological
loanwords have **shifted, narrowed, or lost** their Arabic meaning on the way
into Turkish. `oku`, `ibadet`, `alem`, `salât` all feel known and are all
pre-narrowed.

That reader is not served by a fluent translation, and not served by a catalogue
of alternative meanings either. A fluent translation hides the loss. A catalogue
hands over ingredients that only someone who reads Arabic could assemble.

## What success means

Someone who already knows an ayah well reads the prose and learns something they
could not have got from a translation plus a dictionary — and does not feel
unmoored while learning it.

Two failures, equally bad:

- **flat** — a correct primary reading that reveals nothing;
- **disorienting** — a true latent reading delivered without ground under it.

Everything in [`PRINCIPLES.md`](PRINCIPLES.md) exists to hold both at once.

## The three layers

### Layer 1 — the spine (`_translation/`)

A fluent target-language ayah where **every target token is anchored to a QAC
morpheme**, plus the selected primary root and branch on each rooted stem.

Layer 1 is a join key, not a content surface. It carries no gloss alternatives,
no error profiles, no commentary. Those join later through stable IDs: dictionary
content by `(rootId, branchId, language)`, word analysis by QAC crosswalk,
commentary by `qacRef`/`ayahRef`.

It deliberately selects **one** branch per rooted stem, so that the primary
reading is a fixed, non-negotiable floor. Layers 2 and 3 perturb that floor; they
can only do so because it holds still. What layer 1 rejects is recorded and
handed forward — see [`PRINCIPLES.md`](PRINCIPLES.md) §6.

### Layer 2 — function and resonance, per ayah (`_ayah_commentary/`)

Active work continues in [`_ayah_commentary/v1/`](_ayah_commentary/v1/). The
incompatible v2 experiment has been removed from the active workflow tree and
archived under [`archive/_commentary/v2/`](archive/_commentary/v2/).

Two jobs.

**Function.** What each word contributes to building the ayah, written for
someone with no grammar. This includes everything the reader's languages cannot
render: Turkish has no definite article at all, English cannot double one, and
`الصِّرَاطَ الْمُسْتَقِيمَ` has two. That doubling is invisible in every translation
the reader will ever see, and it is doing work.

**Resonance.** Intra-ayah and near inter-ayah resonance, *explained rather than
catalogued*. If the output is a list of activated readings, the work has not been
done — the reader already has the catalogue and cannot use it. Readings must be
shown connecting. When secondary resonances cohere, the prose states the
resulting local surprise clearly: what it makes newly visible and whether it
supports the primary reading or shifts its frame.

Layer 2 does not select. It carries the full field, including readings no thesis
could use.

### Layer 3 — the whole image (`_channel/layer3/`)

What becomes visible only when the surah is read as an assembly: the recurring
semantic operations through which distant ayahs explain one another.

S100 is the case that requires this layer to exist. Under the primary reading the
running horses have nothing to do with the rest of the surah. Only the resonances
attach them — and that attachment is a surprise, which is the point.

The active workflow is
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md). It runs
three hermetic passes:

1. blind, uncapped discovery from Quran surface rows and mechanically stripped
   reviewed activation cards;
2. direct review against the complete packet, where hypotheses may be merged,
   absorbed, narrowed, rendered, or rejected;
3. composition as one developing argument for a reader with no Arabic or
   linguistic knowledge.

The result is not a summary and does not proceed ayah by ayah. It begins inside
the primary reading and makes every earned reader-model shift available without
a system or length target. The evidence packet contains completed Layer-2 prose
and explicit boundaries, the reviewed network-v3 synthesis when present, and
selected V11 integration sections when present. V12 is not repeated because it
is already upstream of completed Layer 2. Missing network-v3 or V11 inputs
produce warnings but do not stop the run.

The retired root-level `_channel` prompt/plan and the old Layer 2.5 overlay lane
are retained only for historical reproducibility. They are not inputs to the
active workflow.

## Layout

```text
PRINCIPLES.md         rules governing every layer
COMMENTARY_SPEC.md    rules specific to commentary (both levels)
PLAN.md               numbered actions, in execution order — start here
STATUS.md             per-surah coverage
docs/                 sources, available data, channels, open questions
scripts/              shared bundle builder for both commentary levels
bundles/              generated commentary input bundles
_commentary/          hermetic Layer-2 prompts and authored ayah outputs
_translation/         layer 1 — the spine
_ayah_commentary/v1/  layer 2 — function and resonance, per ayah
_channel/layer3/      active layer 3 — surah-wide resonance systems
_channel/*.md         retired combined layer 3 + 2.5 experiment
_channel_review/      retired review experiment
_channel_integration/ retired layer-2.5 experiment
_surah_commentary/    retired separate layer-3 experiment
_surah_final/         retired final reconciliation experiment
_words/               not started
_curriculum/          not started
_audio/               not started
```

`_words/`, `_curriculum/`, and `_audio/` are empty. They are named here because
they are planned, not because they exist.

## Where to start

- Rules first: [`PRINCIPLES.md`](PRINCIPLES.md), then
  [`COMMENTARY_SPEC.md`](COMMENTARY_SPEC.md).
- Running layer 1: [`_translation/v1/README.md`](_translation/v1/README.md).
- Running ayah commentary Layer 2: [`_ayah_commentary/v1/`](_ayah_commentary/v1/)
  is the active authoring path. [`_commentary/ORCHESTRATION.md`](_commentary/ORCHESTRATION.md)
  remains the run contract for existing ayah prompts and agent-authored outputs;
  [`scripts/README.md`](scripts/README.md) documents the bundle builder behind
  those prompts.
- Running surah commentary Layer 3:
  [`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).
- What evidence exists: [`docs/SOURCES.md`](docs/SOURCES.md) for paths and
  formats, [`docs/DATA_AVAILABILITY.md`](docs/DATA_AVAILABILITY.md) for coverage.

## Repository role

```text
quran-roots ───────┐
dictionary ────────┤
latent_activation ─┼─> prose_generation ─> quran-data ─> quran-apps
quran-slm ─────────┘
```

Upstream repositories are a machine for producing **nominations** — activation
runs, branch inventories, inter-ayah retrieval, word analysis. None of them
establishes a reading. This repository is where nominations are adjudicated and
written, and where provenance and review state are recorded.

This repository must not become a second canonical Quran or QAC store, an
unreviewed dump of model output, a replacement for `quran-data`, an application
implementation, or a place where graph similarity is silently converted into
exegetical fact.

Stable artifacts become canonical only after validation, review, and promotion to
`quran-data`. Applications consume pinned releases, not working directories.
