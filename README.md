# Prose Generation

This is a linguistic and editorial project for turning the project's Quranic
research into clear, trustworthy, user-facing content. Code helps gather and
connect the evidence, but linguistic judgment governs the outputs.

Its primary outputs are:

1. translations;
2. words and word analysis;
3. ayah commentary;
4. surah commentary; and
5. Arabic curriculum content.

Audio is an associated delivery asset, but it is not currently treated as a
sixth prose output.

This document records the repository review and data snapshot made on
2026-07-26. Counts for jobs that are still running are a dated snapshot, not a
completion claim.

## Repository role

The project is distributed across several sibling repositories:

```text
quran-roots ───────┐
dictionary ────────┤
latent_activation ─┼─> prose_generation ─> quran-data ─> quran-apps
quran-slm ─────────┘
```

- [`quran-roots`](../quran-roots/README.md) is the research and evidence
  factory. It contains the Quran/QAC foundations, V4 lexicon and Furuq work,
  contextual attachments, activation history, commentary experiments,
  curriculum research, and legacy product artifacts.
- [`dictionary`](../dictionary/README.md) develops root and branch dictionary
  entries and target-language gloss projections.
- `latent_activation` contains the current Turkish V12 ayah publication,
  production word-analysis work, and earlier prose-planning work.
- [`quran-slm`](../quran-slm/README.md) develops Quran-scale semantic networks,
  channel candidates, and inter-ayah relation reviews.
- [`quran-data`](../quran-data/README.md) is the canonical release authority for
  reviewed, accepted, immutable data.
- [`quran-apps`](../quran-apps/README.md) is the product monorepo for the web and
  iOS readers and tafsir surfaces. It consumes pinned content releases through
  explicit contracts.
- `prose_generation` integrates these sources, adjudicates evidence, authors
  prose, records provenance and review state, and prepares releasable content.

This repository must not become:

- a second canonical Quran or QAC store;
- an unreviewed dump of upstream model output;
- a replacement for `quran-data`;
- an application implementation repository; or
- a place where graph similarity is silently converted into exegetical fact.

Stable artifacts become canonical only after validation, review, and promotion
to `quran-data`. Applications should consume pinned releases rather than live
working directories.

## Core production principles

### Analyze once, render per language

Arabic source analysis should be language-neutral wherever possible. A target
language then receives its own fluent prose, lexical choices, tokenization,
QAC mappings, loss/addition disclosures, and editorial review.

A Turkish token mapping cannot simply be reused for English or another
language.

### Evidence before prose

Every user-facing claim should be traceable to typed evidence. Relevant sources
include:

- Quran text and QAC morphology;
- V4 lexical identities and Furuq branch distinctions;
- contextual profiles and grammatical attachments;
- V12 occurrence-level activation;
- production word analysis;
- reviewed dictionary glosses;
- adjudicated inter-ayah relations; and
- accepted channel or surah-structure findings.

Prose is a rendering of accepted claims, not the place where claims first
become true.

### Preserve uncertainty and rejection

Rejected senses, weak alternatives, collisions, omissions, additions, and
review notes are part of the production record. They should not be discarded
merely because the default reader surface is concise.

### Candidate systems nominate; review establishes

Semantic networks, embeddings, retrieval ranks, and inter-ayah similarity
systems can nominate useful evidence. They do not independently establish:

- a word sense;
- an ayah relation;
- a surah channel;
- a theological claim; or
- publication-ready commentary.

### Stable identities are mandatory

The main identities are:

- `ayahRef`: `S:A`
- `qacWordRef`: `S:A:W`
- `qacMorphemeRef`: `S:A:W:M`
- word-analysis identity: `(releaseId, ayahRef, analysisIndex)`
- native lexicon identities: `rootId` and scoped `branchId`

QAC words, QAC morphemes, and word-analysis records are different layers.
Similar-looking records must not be merged by position or surface form.
Cross-layer joins require explicit, versioned crosswalks. The application-side
identity rules are documented in
[`canonical-identities.md`](../quran-apps/packages/contracts/canonical-identities.md).

## Canonical data currently available

The current validated `quran-data` release is `2026.07.21`. Its checksum-valid
coverage includes:

| Dataset | Coverage |
| --- | ---: |
| Numbered ayahs | 6,236 |
| Prefatory basmalahs | 112 |
| Total Quran records | 6,348 |
| QAC words | 77,429 |
| QAC morphemes | 128,219 |
| QAC ayah windows | 6,236 |
| V4/Furuq roots | 3,470 |
| Furuq branch images | 19,590 |
| Dictionary entries in the released lexicon | 21,329 |
| Lexical-unit senses | 37,263 |
| Production word-analysis ayahs | 6,236 |
| Contextual-profile surahs | 114 |
| Final attachment surahs | 114 |

See [`quran-data/STATUS.md`](../quran-data/STATUS.md) and
[`quran-data/RELEASE.json`](../quran-data/RELEASE.json) for the release
authority and exact manifest.

The following important datasets exist upstream but are not yet canonical
`quran-data` products:

- Turkish V12 activation/publication;
- accepted inter-ayah relation releases;
- accepted surah-channel ledgers;
- translations and commentary;
- dictionary gloss projections;
- Arabic curriculum selections; and
- application-specific prose exports.

## Live upstream data snapshot

### Turkish V12

The Turkish V12 publication is complete upstream for all 114 surahs:

- 6,348 publication rows, including prefatory basmalahs;
- 12,807 occurrence-level findings; and
- 114 finalized source files.

It is suitable as an input to the prose workflow, but it still needs a formal
import and release contract before applications should treat it as canonical.

### Word analysis

Production word analysis covers all 6,236 numbered ayahs and is already
released through `quran-data` using `word-analysis-output-v2`.

Word analysis supplies reader-facing lexical and contextual explanation. It
does not by itself activate a V4/Furuq sense.

### Dictionary gloss generation

At the snapshot date:

- 872 Turkish dictionary entry files exist and remain marked `draft`;
- 105 English gloss results exist;
- all 105 English results are marked `reviewed`; and
- no other target language currently has durable gloss results.

The gloss output records branch-concept, contextual, and lexical glosses,
facet coverage, semantic error classification, losses, additions, collisions,
and review provenance. See the
[`gloss_generation` README](../dictionary/v2/gloss_generation/README.md).

These are controlled lexical projections, not fluent ayah translations. Their
review status also does not override the draft status of their Turkish source
entries.

### Inter-ayah review

All 6,236 ayah input dossiers exist. At the snapshot date, 723 reviewed TSV
outputs exist:

| Batch | Complete outputs |
| --- | ---: |
| S1 | 7 / 7 |
| S2 | 286 / 286 |
| S3 | 200 / 200 |
| S4 | 176 / 176 |
| S5 | 54 and running |

The first 100 rows of an output review the retrieval budget; appended rows may
nominate omitted relations. Labels express the marginal usefulness of the
candidate to the focus ayah. They do not perform word-sense disambiguation or
constitute accepted commentary.

The governing rules are in
[`ORCHESTRATION_SPEC.md`](../quran-slm/inter-ayah/ORCHESTRATION_SPEC.md).

### Networks and channels

Quran/QAC, Furuq, baseline, and Neo network views exist across the Quran.
Network-v3 and local channel work provide useful structural hypotheses, but
review and acceptance coverage is not yet uniform.

Channel prose must be based on an accepted channel ledger, not directly on
edge scores.

## S1 pilot readiness

Surah 1 is currently the strongest end-to-end production pilot.

| Component | S1 status |
| --- | --- |
| Quran/QAC | Canonical |
| Numbered ayahs | 7 |
| QAC words | 29 |
| QAC morphemes | 48 |
| Production word-analysis records | 33 |
| QAC-to-analysis crosswalk | Explicit v2 crosswalk exists |
| Turkish V12 publication | 7 rows |
| V12 findings | 21 strong, 13 weak, 2 reject |
| Activated/root anchors | 18 |
| Turkish dictionary coverage | All 18 roots |
| Reviewed English gloss coverage | All 18 roots |
| Inter-ayah outputs | 7 / 7 |
| Inter-ayah reviewed rows | 1,096 |
| Grammar evidence | 94 rows in the S1 app evidence pack |
| Furuq evidence | 18 roots and 151 branch records in the app evidence pack |
| Reader integration | Working web and iOS contract demo |

The inter-ayah S1 labels currently total:

- 267 `strong`;
- 521 `medium`;
- 220 `weak`; and
- 88 `no value`.

The application pilot already demonstrates:

- a shared reader contract;
- explicit QAC-to-analysis and QAC-to-Furuq crosswalks;
- fluent Turkish target-token-to-QAC-morpheme mappings; and
- the use of a pinned source lock.

It remains a demo rather than a production multilingual release. In
particular, the catalog is unsigned, the final multilingual-pack contract is
not frozen, English does not yet have a canonical fluent ayah translation, and
audio publication is incomplete.

The S1 basmalah reference difference is already handled explicitly by mapping
reader `1:1` to V12 publication `1:0`. It should remain an explicit boundary
mapping, not be repaired through hidden renumbering.

## Follow-on pilot candidates

S96, S100, and S103 already have useful V12, word-analysis, and network
coverage. They are reasonable follow-on pilots, but currently have much less
dictionary-gloss and inter-ayah coverage than S1.

- S96 offers a larger, more varied curriculum and lexical test.
- S100 is a compact second pilot with prior prose-planning and channel work.
- S103 is the shortest vertical slice and was previously selected for that
  reason, but it no longer has better overall readiness than S1.

The earlier layered prose direction remains useful:

- **Dinle:** a 30–60 second ayah orientation;
- **Derinleş:** expanded ayah explanation;
- **Kanallar:** reviewed pericope and surah channels; and
- **İzini Sür:** the inspectable evidence ledger.

See [`latent_activation/_prose/README.md`](../latent_activation/_prose/README.md)
and the
[`S1/S100/S103 plan`](../latent_activation/_prose/tr/PLAN-s001-s100-s103.md).
Those documents are design inputs; this repository should become the active
home for the production workflows.

## Output families

### 1. Translation

Translation should combine:

- a fluent target-language ayah line;
- the complete ordered QAC morpheme card spine;
- the direct primary root and branch on each rooted stem;
- occurrence-specific card glosses informed by reviewed dictionary glosses;
  and
- target-language words mapped explicitly to QAC morphemes.

The Turkish V12 baseline supplies the primary reading scaffold. Other V12
resonances, alternatives, and commentary remain separate products rather than
being embedded in this core layer. Dictionary glosses constrain lexical scope
but do not replace fluent translation. The focused process and working S1
English pilot are under [`_translation`](_translation/README.md).

### 2. Words and word analysis

The word product should integrate:

- ordered QAC words and morphemes;
- production word-analysis records;
- explicit QAC-to-analysis crosswalks;
- grammar and contextual attachments;
- activated V4/Furuq senses;
- branch-safe target-language glosses; and
- concise and expanded reader renderings.

The UI may group these layers for readability, but storage and provenance must
preserve their distinct identities.

### 3. Ayah commentary

Ayah commentary should be assembled from typed, reviewed claims:

- V12 primary, secondary, and rejected findings;
- word-analysis insights;
- grammar and contextual evidence;
- dictionary meaning boundaries;
- accepted inter-ayah relations; and
- relevant accepted surah-channel claims.

The default rendering should support a short orientation, a deeper
explanation, and an evidence view. Existing commentary in `quran-roots` is
valuable migration and style material, but it must be revalidated rather than
copied as authority.

### 4. Surah commentary

Surah commentary requires a reviewed channel ledger containing:

- channel title and thesis;
- ayah scope and order;
- each ayah's contribution;
- supporting claim and evidence IDs;
- competing or rejected structures; and
- review and publication status.

Accepted channels can then produce pericope commentary and a surah-level
synthesis. Similarity, network, and SLM outputs remain nominations until this
adjudication occurs.

### 5. Arabic curriculum

The current curriculum direction is an adaptive, language-neutral selection
layer rather than prewritten lessons. It should choose a small concept or
learning flag for an ayah encounter; commentary and word cards then render that
selection in the user's language.

The upstream curriculum infrastructure contains 205,255 raw candidates across
all 6,236 ayahs and a 998-ayah whole-surah learning path. Before production use
it still needs:

- QAC and V4-native identities;
- a fine-grained concept registry;
- deterministic pruning informed by word analysis;
- `qacRef` and audio anchors;
- a flag-to-commentary interface; and
- a versioned application export contract.

The intended experience is “invisible learning”: normally one useful learning
mark per ayah event, without requiring a separate lesson or progress UI. See
the [`curriculum plan`](../quran-roots/curriculum/PLAN.md).

## Common working method

Each output follows a simple linguistic process:

1. Gather the relevant evidence.
2. Form a compact understanding of what the passage is doing.
3. Write the user-facing content as a coherent whole.
4. Test it against lexical, grammatical, contextual, and structural evidence.
5. Revise it through informed editorial review.
6. Prepare the accepted text for `quran-data` and the applications.

Automation should reduce repetitive work and prevent mismatched references. It
should not multiply process or substitute mechanical validation for linguistic
judgment.

## Repository layout

```text
_translation/       Translation integration and rendering (see `_translation/README.md`)
_words/             Word and word-analysis integration
_ayah_commentary/   Ayah claim ledgers and commentary
_surah_commentary/  Channel ledgers and surah synthesis
_curriculum/        Adaptive Arabic curriculum selections
_audio/             Audio manifests and prose/audio alignment
```

Each output directory will receive a focused linguistic workflow and only the
supporting tools needed to assemble evidence and prepare the final content.

## Documentation authority

The main architectural sources reviewed for this understanding are:

- [`quran-roots/METHODOLOGY.md`](../quran-roots/METHODOLOGY.md)
- [`quran-roots/MIGRATION_PLAN.md`](../quran-roots/MIGRATION_PLAN.md)
- [`quran-roots/PIPELINE_CRITICAL_PATH.md`](../quran-roots/PIPELINE_CRITICAL_PATH.md)
- [`quran-roots/_corpus/ARCHITECTURE.md`](../quran-roots/_corpus/ARCHITECTURE.md)
- [`quran-data/README.md`](../quran-data/README.md)
- [`quran-data/STATUS.md`](../quran-data/STATUS.md)
- [`quran-data/ROADMAP.md`](../quran-data/ROADMAP.md)
- [`quran-apps/README.md`](../quran-apps/README.md)
- [`quran-apps` contracts](../quran-apps/packages/contracts/README.md)
- [`quran-apps` multilingual pack rules](../quran-apps/packages/contracts/multilingual-reader-packs.md)
- [`dictionary` gloss-generation documentation](../dictionary/v2/gloss_generation/README.md)
- [`quran-slm` inter-ayah protocol](../quran-slm/inter-ayah/ORCHESTRATION_SPEC.md)

When documents disagree, prefer the newest validated artifact and its release
manifest over older planning documents or legacy app fixtures. Record any such
decision explicitly in the relevant output workflow.
