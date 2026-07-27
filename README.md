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

Two jobs.

**Function.** What each word contributes to building the ayah, written for
someone with no grammar. This includes everything the reader's languages cannot
render: Turkish has no definite article at all, English cannot double one, and
`الصِّرَاطَ الْمُسْتَقِيمَ` has two. That doubling is invisible in every translation
the reader will ever see, and it is doing work.

**Resonance.** Intra-ayah and near inter-ayah resonance, *explained rather than
catalogued*. If the output is a list of activated readings, the work has not been
done — the reader already has the catalogue and cannot use it. Readings must be
shown connecting.

Layer 2 does not select. It carries the full field, including readings no thesis
could use.

### Layer 3 — the whole image (`_surah_commentary/`)

What the surah is doing as an assembly: its argument, its channels, and how each
ayah and each particular word feeds them.

S100 is the case that requires this layer to exist. Under the primary reading the
running horses have nothing to do with the rest of the surah. Only the resonances
attach them — and that attachment is a surprise, which is the point.

Layer 3 selects. A thesis excludes, and what it excludes is handed down to layer
2, which is obliged to carry it.

## The layer 2 / layer 3 problem

Layer 3 is where disorientation risk peaks: a full channel argument delivered
cold will unmoor a reader with no Arabic.

The mechanism that solves it — **channel maturity gating disclosure** — is
specified in [`docs/CHANNELS.md`](docs/CHANNELS.md). In short: a channel surfaces
in layer 2 only once enough of its members are in place that naming it explains
rather than mystifies, and it always enters through *this ayah's own word*, never
as an announcement from above. By the time the reader reaches layer 3, they have
been walked into it.

## Layout

```text
PRINCIPLES.md         rules governing every layer
COMMENTARY_SPEC.md    rules specific to commentary (both levels)
PLAN.md               numbered actions, in execution order — start here
STATUS.md             per-surah coverage
docs/                 sources, available data, channels, open questions
scripts/              shared bundle builder for both commentary levels
bundles/              generated commentary input bundles
_translation/         layer 1 — the spine
_ayah_commentary/     layer 2 — function and resonance, per ayah
_surah_commentary/    layer 3 — the whole image
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
- Running layers 2–3: [`scripts/README.md`](scripts/README.md) builds the
  bundle; `_ayah_commentary/PROMPT.md` and `_surah_commentary/PROMPT.md` are the
  tasks.
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
