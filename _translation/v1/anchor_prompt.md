# Primary branch selection - layer 1, stage 0

Select the primary branch boundary and any real non-primary resonances for every
rooted stem in the input. The input is exhaustive: every candidate Furuq root is
listed in `rootResolution.targets`, and `roots[rootId].branches` contains every
branch under that root. Each target's `rootNormAr` identifies its resolved Arabic
Furuq/frozen root; target array order carries no semantic preference.

This stage is **Turkish-assisted**, not language-neutral. Its output remains the
shared branch seed used by later target languages, but the supplied ordinary
Turkish baseline is one independent witness to the ordinary reading.

## Evidence Priority

For each `ayat[].rootedStems[]`, decide from:

1. the Arabic occurrence and full `arabicText`;
2. lemma, morphology, construction, and candidate root resolution;
3. each candidate branch's Arabic `what_is_ar`;
4. `ordinaryTurkishBaseline` as non-authoritative assistance.

Arabic morphology and context win whenever the baseline and Arabic evidence
pull differently. The baseline may help identify the ordinary lexical floor,
but it is not an approved translation and it must not suppress a real resonance.
Its `targetTokens[].qacWordRefs` are alignment evidence only.

## Selection

`primary` contains the root and normally one branch governing the direct,
ordinary reading of the occurrence. Select more than one primary branch only
when the occurrence lexically realizes both at the floor.

`resonances` contains branch meanings genuinely activated by the local or surah
context but not governing the ordinary lexical floor. Every resonance is
root-scoped. Group multiple resonant branches from the same root in one object.
A merely imaginable relation is not a resonance.

Evaluate every branch under every candidate root before deciding. Branch IDs are
root-scoped: `B002` has no identity without its `rootId`. The dominant or first
root target is not a shortcut. For split roots, use `rootNormAr` together with
the occurrence form and context; do not break a tie by target order.

Candidate branches omitted from `primary` and `resonances` are implicitly
excluded after exhaustive evaluation. Do not output rejection lists, lexical
unit IDs, decision notes, baseline wording, or other prose.

If the evidence cannot support a responsible primary selection, put the stem in
`unresolved` and do not also include it in `anchors`. An unresolved stem blocks
the surah.

## Output

Return only one `primary-anchor-seed-v4` JSON artifact:

```json
{
  "schemaVersion": "primary-anchor-seed-v4",
  "surah": 103,
  "anchors": [
    {
      "qacMorphemeRef": "103:1:1:3",
      "primary": {
        "rootId": "root_001019",
        "branchIds": ["B001"]
      },
      "resonances": [
        {
          "rootId": "root_001019",
          "branchIds": ["B004"]
        }
      ]
    }
  ],
  "unresolved": []
}
```

Emit exactly one anchor per resolved rooted stem, in input order. `resonances`
is required and may be empty. Each unresolved entry is
`{"qacMorphemeRef": "...", "reason": "..."}`.
