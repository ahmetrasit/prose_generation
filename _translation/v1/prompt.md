# Target-language Quran translation layer

Translate the complete surah in the input bundle into its target language. Work
in two ordered stages: author the occurrence glosses first, then render the card
glosses and fluent translation from those locked glosses.

You author **only language**. Every identity — QAC refs, root ids, branch ids,
gloss ids — is assembled from the spine after you return, so none of it appears
in your output. Do not transcribe, restate, or invent any of it.

## What you author

For every rooted card in the bundle:

1. one concise, form-specific **occurrence gloss** — what this word means *here*,
   given its morphology and construction;
2. one short **card gloss** — an occurrence label, not morphology jargon,
   dictionary prose, or commentary.

For particles, articles, pronouns, and affixes: a card gloss only, the shortest
natural statement of the actual local contribution.

Per ayah: the fluent **translation text** and its **target tokens**.

## Using the supplied evidence

`branchCores` define the complete locked semantic boundary. `contextualSenses`
give compact wording for individual facets. `lexicalSenses`, when present,
identify the exact lexical unit used here, but their `fit` must be respected: a
`narrowing` lexical sense is not a complete occurrence gloss, and
`losesFacetIds` with `lossReason` tell you which facets the supplied morphology
and construction still activate. Restore those. Do not import another branch, and
do not reach for a remembered conventional Quran translation.

`glossSource.evidenceLanguage` says whether the dictionary evidence is already in
the target language or arrives through a bridge language. Either way the
occurrence gloss is written in the target language and adapted to
`languagePolicy`. Source gloss wording is semantic evidence, not approved target
prose. One source word may require several coordinated target-language clauses;
compactness must not erase a source-grounded dimension.

Obey `languagePolicy` throughout. Use natural, established target-language
vocabulary without etymological purism. Where a conventional religious label
would merely rename the source word while hiding its occurrence-specific meaning,
render that meaning with a short transparent phrase instead.

If the supplied semantic evidence cannot support a responsible policy-compliant
gloss, record that QAC morpheme in `missingGlosses` with a reason. Do not conceal
a gap with a conventional rendering.

## The fluent translation

Treat the ordered `primaryReading.alignmentGroups` as the selected reading
scaffold: preserve their grouping and sequence by default, reordering only where
target-language grammar requires it. They contain no approved target wording.

Apply `grammarSupport` when realizing scope, attachment, ellipsis, referents,
force, and cross-ayah continuity. Its `grammarUnitRefs` are local grammar-unit
anchors, not QAC identities; never copy them into your output.

Write `translation.text` as coherent, publishable target-language Quran prose,
rendered from the Arabic, your authored occurrence glosses, and the supplied
grammar. Preserve repeated expressions, referents, contrasts, and grammatical
force across the surah.

Segment normally by orthographic word. Map each target token to the smallest set
of QAC morphemes whose meaning or construction it realizes; many-to-many mappings
are allowed. **Concatenating every token's `text` and `separatorAfter` must
reproduce `translation.text` exactly** — this is checked mechanically and is the
one place a small slip fails the run.

## Output

One `translation-authored-v1` JSON artifact, matching the inlined schema:

```json
{
  "schemaVersion": "translation-authored-v1",
  "language": "tr",
  "surah": 103,
  "glosses": {
    "103:1:1:1": { "card": "…" },
    "103:1:1:3": { "card": "çağ", "occurrence": "sıkıştıran çağ" }
  },
  "ayat": {
    "103:1": {
      "text": "…",
      "targetTokens": [
        { "text": "…", "separatorAfter": " ", "qacMorphemeRefs": ["103:1:1:3"] }
      ]
    }
  },
  "missingGlosses": []
}
```

`glosses` carries exactly one entry for every card in the bundle, rooted or not,
keyed by its `qacMorphemeRef`. `ayat` carries exactly one entry for every ayah,
keyed by its `ayahRef`. Include no Arabic, no source gloss evidence, no grammar
evidence, no notes, and no fields beyond the schema.
