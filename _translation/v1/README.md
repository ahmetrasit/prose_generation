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
Run _translation/v1/orchestrator.md for surah 1, language tr.
```

The controller prepares the bundle, renders the generic prompt with concrete
paths, sends only that prompt to one fresh linguistic writer, and mechanically
checks the returned file. It does not rewrite the translation.

Preparation alone:

```sh
python3 _translation/v1/tools/build_bundle.py --surah 1 --language tr
```

One agent authors occurrence glosses first, then the whole surah. Ayah-level
splitting would save little and would make repeated wording less consistent.

## Files

- `SCHEMA.md` — meaning of the fields, authored and assembled;
- `source/sNNN.primary-anchors.json` — the language-neutral branch selection;
- `tools/build_bundle.py` — joins live source data into an agent bundle;
- `tools/check_output.py` — checks identities, mapping references, and text
  assembly;
- `input/{language}/sNNN.json` — agent input;
- `output/{language}/sNNN.json` — production language layer;
- `orchestration.json` / `orchestrator.md` — the generic handoff and the
  controller's cold-start instructions.

---

## Decisions

### D1 — The writer authors only what is authored; the builder assembles the rest

**Decided 2026-07-27. Not yet implemented.**

Today the writer emits the full artifact, including `qacMorphemeRef`,
`qacWordRef`, `rootId`, and `branchIds` on every card, plus a formulaic
`glossId` (`{lang}:v1:{morphemeRef}`). All of these are fully derivable from QAC
morphology plus the anchor seed. `prompt.md` instructs the model to copy them
exactly, so the model is hand-transcribing identity data.

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

**Decided 2026-07-27. Not yet implemented.**

The artifact currently records only `quranDataReleaseId`. For a workflow to be
re-run across three languages over a year, "the same workflow" has to be a fact,
not an assertion. Each artifact additionally records: the anchor-file hash, the
prompt hash, the builder version, and the model id and parameters.

Note what reproducibility can and cannot mean here. The spine is deterministic.
The prose is a model call and will not be bit-identical. What is reproducible is
the spine plus a recorded, checkable authored file.

### D3 — `languagePolicy` is required for every language

**Decided 2026-07-27. Not yet implemented.**

`input/tr/*.json` carries a `languagePolicy` block; `input/en/s001.json` does
not. That drift means en and tr ran under different rules — precisely the failure
the shared workflow exists to prevent. The bundle builder emits a policy block
for every language or fails.

### D4 — Anchors record what was rejected

**Decided 2026-07-27. Not yet implemented.**

`source/sNNN.primary-anchors.json` records the selected `branchIds` and
`lexicalUnitIds` per rooted morpheme. It does not record what was considered and
not chosen, so layer 1's rejections are lost.

Add `consideredNotPrimary` alongside `branchIds`. It is language-neutral, so all
languages inherit it, and it turns layer 1's discards into layer 2 and 3 input
(`../../PRINCIPLES.md` §6).

The motivating case is `عَٰلَمِينَ`: layer 1 correctly takes `B003` (created
beings, worlds) and rejects `B002` (sign, landmark) as non-translational. `B002`
is exactly the branch the Fātiḥa path channel runs on. That rejection currently
survives only as a sentence in this README.

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

## Current artifacts

S1 has an English output and three Turkish test artifacts with no accepted
`output/tr/s001.json`; S103 has a Turkish draft. See [`../../STATUS.md`](../../STATUS.md).
