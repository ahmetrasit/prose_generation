# Available data

What evidence exists to draw on, and what it can and cannot support. Paths and
formats are in [`SOURCES.md`](SOURCES.md); per-surah production state is in
[`../STATUS.md`](../STATUS.md).

**Snapshot date: 2026-07-26.** Counts for jobs that were still running are a
dated observation, not a completion claim. Re-derive before relying on any
number here.

---

## Canonical release

The validated `quran-data` release is `2026.07.21`. Checksum-valid coverage:

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

Authority: `quran-data/STATUS.md` and `quran-data/RELEASE.json`.

The morphology, text, lexicon, and word analysis needed for **layer 1 on any
surah** are therefore complete. Layer 1 is not evidence-limited anywhere.

Not yet canonical `quran-data` products, though they exist upstream: Turkish V12
activation, accepted inter-ayah relation releases, accepted channel ledgers,
translations and commentary, dictionary gloss projections, curriculum
selections, and application prose exports.

---

## Turkish V12 activation

Complete upstream for all 114 surahs: 6,348 publication rows including prefatory
basmalahs, 12,807 occurrence-level findings, 114 finalized source files.

Usable as workflow input; still needs a formal import and release contract
before any application treats it as canonical.

Within the v12 runs, three artifacts have very different coverage:

| artifact | coverage | what it gives |
| --- | --- | --- |
| `full_context_packet.json` | **114 / 114** | branch inventories, surah scope |
| reader ayah walks | **111 / 114** | activated readings, retrospective surprises |
| whole-surah reading (`butuncul-okuma`) | **30 / 114** | per-ayah primary + expansion, Turkish |
| per-ayah focus runs | **6 ayahs total** | staged before/after with neighbours revealed |

The focus runs are a method-development pilot — s100 ×1, s103 ×3, s112 ×1,
s113 ×1, with a different reader on almost every run. So the "ayah before its
neighbours" trajectory that layer 2 treats as a section exists for five ayahs.
Either the protocol is rebuilt at scale or that section becomes occasional.

**Caveat that matters for layer 1.** The live V12 v3 publication *flattens
primary and resonance roles*, so a `strong` finding is not automatically a
translation branch. Branch selection keeps the direct lexical floor instead. Two
S1 cases make this concrete:

- `مَٰلِكِ` takes `root_001444/B002` because the V12 primary wording is "owner";
  its sovereignty branch is contextual.
- `عَٰلَمِينَ` takes `root_001040/B003` (created beings, worlds). That ordinary
  branch was absent from the older V12 packet, whose `B002` use was explicitly
  non-translational sign/landmark resonance.

`عَٰلَمِينَ` B002 is also the case that motivates recording rejections rather than
discarding them — it is a member of the Fātiḥa path channel
([`CHANNELS.md`](CHANNELS.md)).

---

## Word analysis

Covers all 6,236 numbered ayahs, released through `quran-data` as
`word-analysis-output-v2`.

This is the main source for **layer 2's function job** — what each word
contributes structurally. `topics[].status` distinguishes `used` from `narrowed`;
`narrowed` is the non-disambiguating marker. Grammar attachment evidence is
already folded into its `prose` and `topics[]` via `evidence_checked` tags.

Word analysis supplies lexical and contextual explanation. It does not by itself
activate a V4/Furuq sense.

---

## Dictionary gloss generation

Measured 2026-07-27, superseding an earlier snapshot that reported 872 Turkish
draft entries and no durable Turkish gloss results:

- **1,233 Turkish gloss results, every one `status: reviewed`**;
- 127 English gloss results;
- no other target language has gloss results.

The gloss output records branch-concept, contextual, and lexical glosses, facet
coverage, semantic error classification, losses, additions, collisions, and
review provenance.

**This is where error profiles come from**, and the shape is exactly what layer 1
needs. Every contextual and lexical gloss carries:

```json
"error": {"fit": "narrowing", "loses_facet_ids": ["F002","F003"],
          "adds": null, "collision": null, "reason": "Bu gloss yalnız…"}
```

`fit` plus `loses_facet_ids` **is** the "the least-disorienting gloss is
materially wrong about the core concept, check the others" flag — computable at
join time from the error profile against the selected occurrence gloss, with no
authoring required. They join to the layer-1 spine by
`(rootId, branchId, language)`; they are not embedded in it.

Coverage is the binding constraint for German — there is no German gloss result
at all, so a German run of layer 1 would have no controlled lexical evidence.

---

## Inter-ayah review

All 6,236 ayah input dossiers exist. Measured 2026-07-27: **5,276 reviewed TSV
outputs across 88 surahs** — roughly 85% of the corpus. This supersedes an
earlier snapshot reporting 723 outputs across S1–S5; the job has run far ahead of
it.

Every surah in the production plan is complete:

| Surah | Outputs |
| --- | ---: |
| S1 | 7 / 7 |
| S96 | 19 / 19 |
| S100 | 11 / 11 |
| S103 | 3 / 3 |

Inter-ayah coverage is therefore **not** a constraint on any planned work.
Re-measure before treating any surah outside that list as covered.

The first 100 rows of an output review the retrieval budget; appended rows may
nominate omitted relations. Labels express marginal usefulness to the focus ayah
— they do not perform word-sense disambiguation and do not constitute accepted
commentary. See `PRINCIPLES.md` §9 before filtering anything.

Governing rules: `quran-slm/inter-ayah/ORCHESTRATION_SPEC.md`.

---

## Networks and channels

`latent_activation/network/v3` treats channel detection as **discovery rather
than classification**: a branch-level graph mined from the surah-local SLM
affinity matrix, with Qnet labels attached only after clustering.

**Candidate generation is complete** (2026-07-23): 89,199 dense candidates,
11,572 families, 4,157,715 sparse paths, 457,281 path families, across 111
eligible surahs. S103, S108, and S110 were excluded from the corpus run — three
canonical ayahs each, below the minimum span policy.

**Review exists for 110 surahs**, one `reader_a_pilot.md` each. Missing: S108,
S110, S113, S114. Note that S103 *does* have a review despite being excluded from
the corpus run.

Quality is high — both Fātiḥa reference channels were recovered at finer
resolution than the hand sketch ([`CHANNELS.md`](CHANNELS.md) §5). But it is
**first-pass, single-reader output, not an adjudicated ledger**: no accept/reject,
no second reader, no per-ayah maturity, and no machine-readable form. Layer 3 is
gated on that adjudication, not on discovery.

Older Quran/QAC, Furuq, baseline, and Neo network views also exist; channel prose
must rest on a reviewed ledger, never on edge scores.

The surah **argument** still has no source artifact analogous to the per-ayah
reader walk. That remains the gap, and the reason structural claims at layer 3
are marked as inference.

---

## Prior design inputs

The earlier layered prose direction remains useful and named the same problem
this repository's three layers now address:

- **Dinle** — a 30–60 second ayah orientation;
- **Derinleş** — expanded ayah explanation;
- **Kanallar** — reviewed pericope and surah channels;
- **İzini Sür** — the inspectable evidence ledger.

See `latent_activation/_prose/README.md` and
`latent_activation/_prose/tr/PLAN-s001-s100-s103.md`. Those are design inputs;
this repository is the active home for the production workflows.

---

## Documentation authority

Architectural sources reviewed for this understanding:

- `quran-roots/METHODOLOGY.md`, `MIGRATION_PLAN.md`, `PIPELINE_CRITICAL_PATH.md`,
  `_corpus/ARCHITECTURE.md`
- `quran-data/README.md`, `STATUS.md`, `ROADMAP.md`
- `quran-apps/README.md`, `packages/contracts/README.md`,
  `packages/contracts/multilingual-reader-packs.md`,
  `packages/contracts/canonical-identities.md`
- `dictionary/v2/gloss_generation/README.md`
- `quran-slm/inter-ayah/ORCHESTRATION_SPEC.md`

When documents disagree, prefer the newest validated artifact and its release
manifest over older planning documents or legacy app fixtures. Record any such
decision explicitly in the relevant workflow.
