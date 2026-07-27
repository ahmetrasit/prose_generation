# Translation layer v1

The final artifact contains occurrence glosses, cards, and fluent prose while
keeping source evidence in the input bundle.

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
ID. The writer authors its `occurrenceGloss.text` before rendering and copies
the same ID to `selectedGlossId`.

The root and branch remain the shared semantic anchor. The occurrence gloss may
change across ayahs when form, voice, valency, construction, or context changes.
Identical forms in identical constructions should normally reuse wording.

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
