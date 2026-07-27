# Translation layer v1

This workflow produces one language-specific surah file with three connected
layers:

1. ordered QAC morpheme cards;
2. the selected root and primary branch on each rooted stem; and
3. a fluent translation segmented back to the QAC morphemes.

The final record stays small. Arabic, morphology, V12 reading alignment,
compact attachment guidance, and dictionary evidence are supplied to the
writing agent but are not copied into the final language layer. V12 target
wording is deliberately withheld.

## S1 pilot

To run the complete job through a cold controller, give it only this
assignment:

```text
Run _translation/v1/orchestrator.md for surah 1, language tr.
```

The controller prepares the bundle, renders the generic prompt with concrete
paths, sends only that prompt to one fresh linguistic writer, and mechanically
checks the returned file. It does not rewrite the translation.

For preparation alone, run:

```sh
python3 _translation/v1/tools/build_bundle.py --surah 1 --language tr
```

The isolated GPT-5.5/high test artifact generated from the reviewed gloss
results is `output/tr/s001.v3-gloss-test.json`. The generic handoff is described by
`orchestration.json`; the controller's complete cold-start instructions are in
`orchestrator.md`.

## S1 anchor decisions

The live V12 v3 publication flattens primary and resonance roles, so a `strong`
finding is not automatically a translation branch. The S1 seed keeps the
direct lexical floor instead.

Two cases make the distinction concrete:

- `مَٰلِكِ` uses `root_001444/B002` because the V12 primary wording is
  “owner”; its sovereignty branch is contextual.
- `عَٰلَمِينَ` uses the current dictionary's `root_001040/B003`, the branch
  for created beings/worlds. That ordinary branch was absent from the older
  V12 packet, whose `B002` use was explicitly non-translational sign/landmark
  resonance.

## Files

- `SCHEMA.md` — meaning of the final fields;
- `source/s001.primary-anchors.json` — the compact primary-branch selection;
- `tools/build_bundle.py` — joins live source data into an agent bundle;
- `tools/check_output.py` — checks identities, mapping references, and text
  assembly;
- `input/{language}/sNNN.json` — agent input;
- `output/{language}/sNNN.json` — production language layer.

One agent authors occurrence glosses first and then handles the whole surah.
Ayah-level splitting would save little for S1 and would make repeated wording
less consistent.
