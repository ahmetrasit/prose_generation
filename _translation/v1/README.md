# Translation layer v1 — the spine

Produces one language-specific surah file with three connected layers:

1. ordered QAC morpheme cards;
2. the selected root and primary branch on each rooted stem; and
3. a fluent translation segmented back to those morphemes.

The artifact is a **join spine**, not a content surface. Arabic, morphology, V12
reading alignment, attachment guidance, and dictionary evidence are supplied to
the writing agent but are not copied into it. V12 target wording is deliberately
withheld.

Glosses, error profiles, word analysis, and commentary join later through stable
IDs. See [Decisions](#decisions) for why, and what that costs.

## Run it

Complete job through a cold controller — give it only this assignment:

```text
Run _translation/v1/orchestrator.md for surah 103, language tr, date 2026-07-27.
```

The controller runs two cold agents. Neither sees anything but its rendered
prompt, and the controller never rewrites what either one authored.

```
stage 0  anchors      once per surah, language-neutral
         build_anchor_input.py -> instantiate.py -> agent -> check_anchors.py
         => source/sNNN.primary-anchors.json

stage 1  translation  once per surah per language
         build_bundle.py -> instantiate.py -> agent -> assemble.py -> check_output.py
         => output/{language}/sNNN.json
```

Stage 0 is skipped when a `primary-anchor-seed-v2` file already exists and
passes. A `v1` seed does not pass — see D4.

## Files

- `SCHEMA.md` — meaning of the fields, authored and assembled;
- `anchor_prompt.md` — the stage-0 task: select one primary branch per rooted
  stem and record what was rejected;
- `prompt.md` — the stage-1 task: author glosses and the fluent translation;
- `tools/build_anchor_input.py` — enumerates every rooted stem and its complete
  candidate space, language-neutral;
- `tools/check_anchors.py` — checks coverage, root-scoped ids, and that no
  activated branch was dropped unrecorded;
- `tools/build_bundle.py` — joins live source data into an agent bundle;
- `tools/instantiate.py` — renders a hermetic prompt for either stage;
- `tools/assemble.py` — joins the authored file to the spine and stamps
  provenance;
- `tools/check_output.py` — checks the assembled artifact against its bundle;
- `anchors/input/sNNN.anchor-input.json` — stage-0 agent input;
- `source/sNNN.primary-anchors.json` — the language-neutral branch selection;
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

### D4 — Anchors record what was rejected

**Decided 2026-07-27. Implemented 2026-07-27** — `primary-anchor-seed-v2` adds
`consideredNotPrimary`, `anchor_prompt.md` requires it, and `check_anchors.py`
fails any seed that drops a V12-activated branch without recording it.

`source/sNNN.primary-anchors.json` records the selected `branchIds` and
`lexicalUnitIds` per rooted morpheme. Before v2 it did not record what was
considered and not chosen, so layer 1's rejections were lost.

`consideredNotPrimary` is language-neutral, so all languages inherit it, and it
turns layer 1's discards into layer 2 and 3 input (`../../PRINCIPLES.md` §6).

The motivating case is `عَٰلَمِينَ`: layer 1 correctly takes `B003` (created
beings, worlds) and rejects `B002` (sign, landmark) as non-translational. `B002`
is exactly the branch the Fātiḥa path channel runs on.

**Both existing seeds are still v1 and therefore fail the check.** Measured
against the current candidate space, re-seeding recovers up to 83 recorded
rejections for S1 and 62 for S103 — including the seven `ع ص ر` branches at
`103:1:1:3` that `PRINCIPLES.md` §8 builds its flagship *retention under
compression* finding on. Until they are re-seeded at v2, that material is being
discarded at stage 0 every run.

### D5 — Glosses and error profiles stay out of the spine

**Standing decision.**

Up to three candidate glosses per word, their error profiles (what each loses,
adds, narrows, collides with), and the "the least-disorienting gloss is
materially wrong about the core concept" flag are all **joined**, not embedded.
They attach by `(rootId, branchId, language)` from
`dictionary/v2/gloss_generation/results/{language}`, with occurrence-level
narrowing by `qacWordRef`.

The flag is computable at join time from the branch's error profile against the
selected occurrence gloss. Nothing about it needs authoring in the spine.

This keeps layer 1 small, stable, and re-runnable, and keeps one branch selected
per rooted stem so that the primary reading is a fixed floor for layers 2 and 3
to perturb.

---

## Anchor decisions (S1)

The live V12 v3 publication flattens primary and resonance roles, so a `strong`
finding is not automatically a translation branch. The S1 seed keeps the direct
lexical floor instead.

- `مَٰلِكِ` uses `root_001444/B002` because the V12 primary wording is "owner";
  its sovereignty branch is contextual.
- `عَٰلَمِينَ` uses `root_001040/B003`, the branch for created beings and worlds.
  That ordinary branch was absent from the older V12 packet, whose `B002` use was
  explicitly non-translational sign/landmark resonance. See D4.

**Both cases are quoted in `anchor_prompt.md`** as the worked example of the
flattening trap. That is deliberate few-shot teaching of the selection rule, and
it has the same consequence it has at layer 2: **S1 cannot be used to evaluate
the anchor agent.** Evaluate on a surah whose answers are not in the prompt.

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
