# Target-language Quran translation layer

Read only `<input-bundle>` and `<output-schema>`; do not inspect any existing
translation or other project file. Write the complete JSON artifact to
`<output-path>` and nothing else.

Translate the complete surah into the bundle's target language. Work in two
ordered stages: author the occurrence glosses first, then render the cards and
fluent translation from those locked glosses.

For every rooted card:

1. Keep its QAC, root, and branch identities unchanged.
2. Author one concise, form-specific `occurrenceGloss.text`.
3. Copy the input `glossId` to `occurrenceGloss.glossId` and
   `selectedGlossId`.
4. Use that occurrence gloss as the lexical basis of both the card and fluent
   translation.

`branchCores` define the complete locked semantic boundary.
`contextualSenses` provide compact wording for its individual facets.
`lexicalSenses`, when present, identify the exact lexical unit used here, but
their `fit` must be respected. A `narrowing` lexical sense is not a complete
occurrence gloss: use `losesFacetIds` and `lossReason` to restore any facets
activated by the supplied morphology and construction. Do not import another
branch or a remembered conventional Quran translation.

`glossSource.evidenceLanguage` identifies whether the dictionary evidence is
already in the target language or supplied through a bridge language. In both
cases, produce the occurrence gloss in the target language and adapt all
wording to `languagePolicy`; source gloss wording is semantic evidence, not
approved target prose. One source word may require several coordinated
target-language clauses. Compactness must not erase a source-grounded
dimension.

For particles, articles, pronouns, and affixes, write the shortest natural
card gloss for their actual local contribution. Do not invent root or branch
identities.

Obey `languagePolicy` throughout. If a single permitted word is inadequate,
use a short transparent phrase. Never use a prohibited loanword merely because
it is familiar in published translations. If the supplied semantic evidence
cannot support a responsible policy-compliant gloss, record that QAC morpheme
in `missingGlosses`; do not conceal the gap with a conventional rendering.

Treat the ordered `primaryReading.alignmentGroups` as the selected V12 reading
scaffold: preserve their grouping and sequence by default, reordering only
where target-language grammar requires it. They contain no approved target
wording. Apply `grammarSupport` when realizing scope, attachment, ellipsis,
referents, force, and cross-ayah continuity. Its optional `grammarUnitRefs`
are local grammar-unit anchors, not QAC identities; never copy them into the
output.

Write exactly one card for every input card in the original order.
`cardGloss` must be a short occurrence label, not morphology jargon,
dictionary prose, or commentary.

Write `translation.text` as coherent, publishable target-language Quran prose.
Render from the Arabic, the authored occurrence glosses, and supplied grammar;
do not default to wording remembered from standard translations. Preserve
repeated expressions, referents, contrasts, and grammatical force across the
surah.

Segment the translation normally by orthographic word. Map each target token
to the smallest set of QAC morphemes whose meaning or construction it realizes.
Many-to-many mappings are allowed. Concatenating every token's `text` and
`separatorAfter` must reproduce `translation.text` exactly.

Copy release, language, surah, ayah, QAC, root, and branch metadata exactly.
Include no Arabic, source gloss evidence, grammar evidence, notes, or extra
fields in the output.
