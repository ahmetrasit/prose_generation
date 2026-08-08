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

Layer 2 does not select among activated readings. Its production input is made
by running `scripts/tier_branch_payloads.py` on the full `build_bundle.py`
output before prompt instantiation. The transport payload is tiered, but every
dominant/non-dominant root and every dictionary branch identity remains present;
all non-branch evidence remains unchanged. Payload tiering is not permission to
drop an activated reading or reader payoff.

The tier labels impose no prose length or priority ranking. Layer 2 remains free
to develop every materially distinct, anchored surprise that changes the
reader's understanding, while omitting repetition, fluff, and available lexical
material with no significant payoff.

The projection fails on malformed citations and unresolved citations for roots
present in its resolution surfaces. Valid Arabic citations to contextual roots
absent from both the ayah root lexicon and branch inventory are recorded under
`coverage.root_lexicon.branch_policy.resolution` as out of scope; they are never
silently treated as resolved interest.

That admission threshold is density-invariant: a qualifying finding receives the
same voice whether its ayah has three roots or twenty-six. Longer ayat do not get
a fixed prose budget divided among more findings.

### Layer 3 — the whole image (`_channel/layer3/`)

What becomes visible only when the surah is read as an assembly: the recurring
semantic operations through which distant ayahs explain one another.

The active cold-agent runbook is
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).
Mechanical scripts build stage-specific hermetic prompts. Fresh agents then
perform blind discovery, latent-dependence review into channel briefs, and
composition as one developing argument for a reader with no Arabic or
linguistic knowledge.

The result is not a summary and does not proceed ayah by ayah. A finding belongs
here only when secondary semantic material changes the reader's model in a way
the ordinary translation cannot produce, while making something specific in
the surah newly intelligible. Reviewed Network V3 and V11 inputs are optional;
their absence produces warnings and does not stop the run. The runbook defines
the exact source projections, agent boundaries, commands, and output paths.

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
scripts/              base builder, pre-L2 branch tierer, and instantiators
bundles/              generated base and tiered commentary input bundles
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
  [`scripts/README.md`](scripts/README.md) documents the required
  `build_bundle.py` -> `tier_branch_payloads.py` -> `instantiate.py` sequence.
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
