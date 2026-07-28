# Translation layer v1 — the spine

Produces one language-specific surah file with three connected layers:

1. ordered QAC morpheme cards;
2. the selected root and primary branch on each rooted stem; and
3. a fluent translation segmented back to those morphemes.

The artifact is a **join spine**, not a content surface. Arabic, morphology,
reading alignment, attachment guidance, and selected-branch dictionary evidence
are supplied to the agents but are not copied into the final artifact.

Selected branch cores, contextual senses, and their complete available error
profiles are joined into the writer input through stable IDs. The evidence is
hoisted once per distinct root and selected branch set; occurrence cards refer
to it. Lexical senses, word analysis, and commentary remain outside Stage 1.

## Run it

Complete job through a cold controller — give it only this assignment:

```text
Run _translation/v1/orchestrator.md for surah 103, language tr, date 2026-07-27.
```

The controller runs two cold agents. Neither sees anything but its rendered
prompt, and the controller never rewrites what either one authored.

```
stage 0  anchors      once per surah, Turkish-assisted and shared
         build_anchor_input.py -> instantiate.py -> agent -> check_anchors.py
         => source/sNNN.primary-anchors.json

stage 1  translation  once per surah per language
         build_bundle.py -> instantiate.py -> agent -> assemble.py -> check_output.py
         => output/{language}/sNNN.json
```

Stage 0 is skipped when a `primary-anchor-seed-v4` file already exists and
passes. Older seeds remain readable by the Stage 1 builder for low-cost
compatibility, but new anchor work uses v4.

## Files

- `SCHEMA.md` — meaning of the fields, authored and assembled;
- `anchor_prompt.md` — the stage-0 task: select primary and resonant branches;
- `prompt.md` — the stage-1 task: author glosses and the fluent translation;
- `tools/build_anchor_input.py` — enumerates every rooted stem, every candidate
  root and branch, and the independently authored ordinary Turkish baseline;
- `tools/check_anchors.py` — checks coverage and root-scoped primary/resonance
  identities against the frozen input;
- `tools/build_bundle.py` — joins live source data into an agent bundle;
- `tools/instantiate.py` — renders a hermetic prompt for either stage;
- `tools/assemble.py` — joins the authored file to the spine and stamps
  provenance;
- `tools/check_output.py` — checks the assembled artifact against its bundle;
- `anchors/input/sNNN.anchor-input.json` — stage-0 agent input;
- `source/sNNN.primary-anchors.json` — the shared Turkish-assisted branch selection;
- `prompts/` — rendered prompts and their manifests, both stages;
- `input/{language}/sNNN.json` — stage-1 agent input;
- `authored/{language}/sNNN.authored.json` — what the writer returns;
- `output/{language}/sNNN.json` — production language layer;
- `orchestration.json` / `orchestrator.md` — the machine-readable stage
  contract and the controller's cold-start instructions.

---

## Decisions

### D1 — The writer authors only what is authored; the builder assembles the rest

**Decided 2026-07-27. Implemented 2026-07-27** — `tools/assemble.py`,
`schema/translation-authored-v1.schema.json`, and a rewritten `prompt.md`.
Verified by round-tripping the shipped `output/tr/s103.json` through the authored
form: the reassembled artifact is identical to it apart from the new provenance
block.

Before that, the writer emitted the full artifact, including `qacMorphemeRef`,
`qacWordRef`, `rootId`, and `branchIds` on every card, plus a formulaic
`glossId` (`{lang}:v1:{morphemeRef}`). All of these are fully derivable from QAC
morphology plus the anchor seed. `prompt.md` instructed the model to copy them
exactly, so the model was hand-transcribing identity data.

For S1 (48 morphemes) that is survivable. Al-Baqarah is roughly 6,000 morphemes —
tens of thousands of copied identity values through a model. `check_output.py`
currently exists in large part to catch the resulting corruption, which means the
checker is compensating for a design choice.

**The split.** Genuinely authored content is four things: `cardGloss`,
`occurrenceGloss.text`, `translation.text`, and `targetTokens`. Everything else
is derivable.

The writer returns an authored-only file keyed by ref:

```json
{
  "schemaVersion": "translation-authored-v1",
  "language": "tr",
  "surah": 103,
  "glosses": {
    "103:1:1:3": { "card": "çağ", "occurrence": "sıkıştıran çağ" }
  },
  "ayat": {
    "103:1": { "text": "…", "targetTokens": [ … ] }
  },
  "missingGlosses": []
}
```

`tools/assemble.py` then joins it to the spine (QAC morphology + anchors) and
emits `translation-layer-v1` unchanged. **The output schema and every downstream
consumer are unaffected.**

Consequences:

- transcription errors become structurally **impossible**, not merely detected;
- output tokens drop by roughly 60–70%, which is what makes long surahs viable;
- reproducibility becomes meaningful — the spine is deterministic given
  `(release, surah, anchors)`, and only the authored file is model output, small
  enough to diff and review by eye;
- `check_output.py` stops re-checking identities the builder now controls and
  checks only what is authored: gloss coverage, `targetTokens` concatenation
  reproducing `text`, and refs resolving;
- "rebuild because `quran-data` released" cleanly separates from "re-author
  because the Turkish was wrong".

`prompt.md` must be updated in the same change to stop asking for copied
metadata.

### D2 — Artifacts pin their own provenance

**Decided 2026-07-27. Implemented 2026-07-27** — `assemble.py` stamps the block,
the schema requires it, and `check_output.py` fails an artifact without it.

The artifact previously recorded only `quranDataReleaseId`. For a workflow to be
re-run across three languages over a year, "the same workflow" has to be a fact,
not an assertion. Each artifact additionally records: the anchor-file hash, the
prompt hash, the builder version, and the model id and parameters.

Note what reproducibility can and cannot mean here. The spine is deterministic.
The prose is a model call and will not be bit-identical. What is reproducible is
the spine plus a recorded, checkable authored file.

### D3 — `languagePolicy` is required for every language

**Decided 2026-07-27. Implemented 2026-07-27.**

`build_bundle.py` emits a policy block for every language. The drift the decision
named was a stale artifact rather than missing code: `input/en/s001.json` had
been built before the field existed. Rebuilt.

### D4 — Anchors record primary and resonance, not rejection prose

**Revised 2026-07-28.** `primary-anchor-seed-v4` records one root-scoped
`primary` selection and explicit root-scoped `resonances` per occurrence.
Stage 0 evaluates the exhaustive candidate inventory. Branches omitted from
both roles are implicitly excluded; it does not emit lexical-unit selections,
decision notes, or exhaustive rejection lists.

This preserves the distinction later layers need: a real secondary resonance
survives, while a branch that simply does not apply does not become downstream
content merely because Stage 0 inspected it.

The v4 seed preserves those resonances for downstream analysis. Stage 1
deliberately consumes only `primary`: resonances are omitted from
`translation-input-v2` so they cannot alter the primary translation.

### D5 — Glosses and error profiles stay out of the spine

**Standing decision.**

Branch cores, contextual glosses, and their complete available error profiles
are **joined**, not embedded in the anchor seed. Stage 1 intentionally omits
lexical senses. It receives evidence scoped to the selected branches and uses
the occurrence morphology and construction to realize the lexical form.

The bundle hoists each evidence package once per distinct `rootId` plus selected
branch set. Rooted cards carry only an `evidenceRef`; repeated occurrences do not
repeat dictionary prose. Multiple primary branch IDs are supported. When
evidence is in the target language, `evidenceLanguage` is omitted and defaults
to `targetLanguage`; bridge-language exceptions retain it explicitly.

This keeps layer 1 small, stable, and re-runnable, and keeps the selected primary
branch set as a fixed floor for layers 2 and 3 to perturb.

### D6 — Split QAC roots stay split until the anchor agent selects a Furuq root

**Decided 2026-07-28. Implemented 2026-07-28** — `build_anchor_input.py` and
`build_bundle.py` now read
`quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz`, the root-level QAC to
Furuq gateway. The builder preserves `mappingStatus` and every usable target
under `rootResolution.targets`. Every target carries its root-scoped `rootId`
and resolved Arabic `rootNormAr`, preferring the Furuq root norm and falling
back deterministically to frozen/source or dictionary root metadata. Target
order is never semantic evidence.

For both unique and split roots, `primary-anchor-seed-v4` writes the selected
`primary.rootId`; resonances carry their own root identity. `check_anchors.py`
validates every selected branch against the exhaustive frozen Stage 0 input.
The translation writer sees only the selected root and primary branches. Split
root alternatives, resonances, and repeated `rootResolution` do not enter its
bundle. Resonances remain in the seed for downstream analytical layers.

The root map is aggregate by QAC root. A small number of frozen/MASAQ
occurrences are more specific than that aggregate, including `100:3:1:3`
`مُغِيرَٰتِ`, where QAC has `غ ي ر` but the frozen audit records
`غ و ر / غ ي ر`. The builders overlay that occurrence audit, split the combined
frozen root into component roots, and resolve each component through the root
gateway. That preserves `root_001112` (`غ و ر`) beside `root_001119` (`غ ي ر`)
for the anchor agent instead of globally changing every QAC `غ ي ر` occurrence.

---

## Anchor decisions (S1)

The ordinary Turkish baseline is assistance, not authority. Arabic morphology
and branch boundaries determine the direct lexical floor, while genuine
secondary branch activation is recorded under `resonances`.

- `مَٰلِكِ` uses `root_001444/B002` because the V12 primary wording is "owner";
  its sovereignty branch is contextual.
- `عَٰلَمِينَ` uses `root_001040/B003`, the branch for created beings and worlds.
  That ordinary branch was absent from the older V12 packet, whose `B002` use was
  explicitly non-translational sign/landmark resonance. See D4.

## Current artifacts

S1 has an English output and three Turkish test artifacts with no accepted
`output/tr/s001.json`; S103 has a Turkish draft. See [`../../STATUS.md`](../../STATUS.md).

Two things measured 2026-07-27 that the artifacts do not say for themselves:

- `output/en/s001.json` predates the occurrence-gloss design entirely — it has no
  `occurrenceGloss` on any rooted card — and does not pass `check_output.py`. It
  is a legacy artifact, not a regression.
- `input/tr/s103.json` was stale against
  `dictionary/v2/gloss_generation/results/tr`; rebuilding changed branch and
  contextual gloss wording. The shipped `output/tr/s103.json` was authored
  against the older evidence. This is exactly the drift D2's provenance block
  exists to make visible, and it was invisible before.
