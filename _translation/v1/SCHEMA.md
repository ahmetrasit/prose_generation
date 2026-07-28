# Translation layer v1

The final artifact contains occurrence glosses, cards, and fluent prose while
keeping source evidence in the input bundle.

## Stage 0 contracts

`anchor-input-v2` is exhaustive but compact. Each rooted occurrence carries
Arabic, morphology, a compact root resolution, and an independently authored
ordinary Turkish baseline with QAC-word alignment. Every candidate root appears
under `roots`, and every branch contains only `branchId` and `what_is_ar`.
Each `rootResolution.targets[]` entry contains both root-scoped `rootId` and
`rootNormAr`, the resolved Arabic Furuq/frozen root norm. Split target order has
no selection meaning.

`primary-anchor-seed-v4` is branch-only:

```json
{
  "qacMorphemeRef": "87:6:1:2",
  "primary": { "rootId": "root_001210", "branchIds": ["B002"] },
  "resonances": [
    { "rootId": "root_001210", "branchIds": ["B001"] }
  ]
}
```

All branch IDs are root-scoped. Omitted branches are implicit exclusions.
Lexical senses are not part of the Stage 1 writer contract.
`resonances` remain in the v4 seed for downstream analysis, but Stage 1
deliberately omits them and builds `translation-input-v2` from `primary` only.

## Stage 1 input

`translation-input-v2.selectedBranchEvidence` stores one evidence package per
distinct selected `rootId` and primary branch set. A rooted card carries
`rootId`, `branchIds`, and `evidenceRef`; it does not repeat the evidence.
Registry entries contain `branchCores`, `contextualSenses`, and every available
error-profile field. They contain no `lexicalSenses`.

An omitted registry `evidenceLanguage` means `targetLanguage`. An explicit
different value identifies bridge-language evidence and must be preserved.
`qacWordRef` and the occurrence `glossId` are absent from agent-visible cards;
the assembler derives them from `qacMorphemeRef` and `language`.

## Authored vs. assembled

Per decision D1 in [`README.md`](README.md), the writer authors only four kinds
of content; everything else is derived by the builder from QAC morphology and
`source/sNNN.primary-anchors.json`.

| field | origin |
| --- | --- |
| `qacMorphemeRef` | assembled — copied from the deterministic input card |
| `qacWordRef` | assembled — `qacMorphemeRef` without its final component |
| `rootId` | assembled — QAC/Furuq root resolution plus the anchor seed's selected root for split roots |
| `branchIds` | assembled — anchor seed |
| `occurrenceGloss.glossId`, `selectedGlossId` | assembled — formula `{lang}:v1:{qacMorphemeRef}` |
| `schemaVersion`, `language`, `quranDataReleaseId`, `surah`, `ayahRef` | assembled |
| `cardGloss` | **authored** |
| `occurrenceGloss.text` | **authored** |
| `translation.text` | **authored** |
| `translation.targetTokens` | **authored** |
| `missingGlosses` | **authored** |

The writer's return value is `translation-authored-v1`, keyed by ref:

```json
{
  "schemaVersion": "translation-authored-v1",
  "language": "tr",
  "surah": 103,
  "glosses": { "103:1:1:3": { "card": "çağ", "occurrence": "sıkıştıran çağ" } },
  "ayat": { "103:1": { "text": "…", "targetTokens": [] } },
  "missingGlosses": []
}
```

`tools/assemble.py` joins it to the spine and emits the artifact below
unchanged. Downstream consumers see only `translation-layer-v1`.

```json
{
  "schemaVersion": "translation-layer-v1",
  "language": "tr",
  "quranDataReleaseId": "2026.07.21",
  "surah": 1,
  "missingGlosses": [],
  "ayat": [
    {
      "ayahRef": "1:1",
      "cards": [
        {
          "qacMorphemeRef": "1:1:4:2",
          "qacWordRef": "1:1:4",
          "rootId": "root_000552",
          "branchIds": ["B001"],
          "occurrenceGloss": {
            "glossId": "tr:v1:1:1:4:2",
            "text": "çok esirgeyip bol bol iyilik eden"
          },
          "selectedGlossId": "tr:v1:1:1:4:2",
          "cardGloss": "bol bol iyilik eden"
        }
      ],
      "translation": {
        "text": "…",
        "targetTokens": [
          {
            "text": "…",
            "separatorAfter": "",
            "qacMorphemeRefs": ["1:1:4:2"]
          }
        ]
      }
    }
  ]
}
```

## Occurrence glosses

Each rooted QAC morpheme receives one language- and occurrence-specific gloss
ID. The writer authors only its `occurrenceGloss.text`; the assembler creates
the ID and copies it to `selectedGlossId`.

The root and branch remain the shared semantic anchor. When a QAC root maps to
multiple Furuq roots, the stage-0 anchor seed selects the `rootId`. The writer
bundle contains only that root and its primary branches; alternate roots remain
in the Stage 0 input/seed. Seed resonances likewise remain available to
downstream analysis but never enter the translation writer bundle. The
occurrence gloss may change across ayahs when form, voice, valency,
construction, or context changes.

`missingGlosses` records semantic evidence gaps. A nonempty list prevents the
artifact from passing the completion check.

## Cards and fluent translation

`cards` preserves the complete ordered QAC morpheme sequence. Unrooted
particles and affixes receive contextual card glosses but no invented lexical
identity.

`targetTokens` are target-language words mapped to the smallest relevant QAC
morpheme set. Concatenating every token's `text` and `separatorAfter` must
exactly reproduce `translation.text`.

Future word analysis joins through QAC IDs. Dictionary content joins through
root and branch IDs, while gloss alternatives can join through the stable
occurrence gloss ID.

## Provenance

Per decision D2, each artifact records what produced it, so that a re-run is a
checkable claim rather than an assertion:

```json
"provenance": {
  "quranDataReleaseId": "2026.07.21",
  "anchorsSha256": "…",
  "promptSha256": "…",
  "builderVersion": "translation-v1-builder-…",
  "model": { "id": "…", "params": {} }
}
```

The spine is deterministic given `(release, surah, anchors)`. The authored file
is a model call and will not be bit-identical between runs; it is small enough to
diff and review directly.
