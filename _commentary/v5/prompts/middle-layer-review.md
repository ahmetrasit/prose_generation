# Commentary V5 independent middle-layer reviewer

You are the fresh, independent final reviewer for the **@@AYAH_REF@@**
middle-layer prose. Another agent wrote the current draft, but you have no
authoring context and must not trust its citations, validation report, or
implicit decisions.

Compare the complete editorial source below directly with the current prose at:

`@@MIDDLE_PROSE_OUTPUT_PATH@@`

Repair that prose in place until it is materially shorter and easier to read
than the editorial source while preserving every distinct finding, mechanism,
concrete detail, contextual role, qualification, boundary, uncertainty, and
live alternative. The source is the complete evidence boundary. Do not inspect
upstream materials or add outside knowledge.

Write only the repaired prose file. Do not create or modify a claim ledger,
inventory, audit report, metrics file, span map, manifest, scratch file, source
file, prompt, validator, test, or other ayah. Any inventory or audit checklist
you need is temporary and must not be persisted.

Your only semantic inputs are the embedded editorial source and the current
prose at the stated path. Do not read or rely on a legacy
`*.middle.claims.json` file, the author's prompt, an earlier review, or another
artifact even if one is present.

Complete this entire review in one turn. There will be no output-derived hint,
repair message, retry, or replacement from the orchestrator.

## Stable source numbering

Split the Markdown source at blank lines into nonempty blocks, exclude headings
beginning with `#`, and number every other block from `1` in reader order. A
multiline block is one paragraph. Citations must use these stable numbers as
`@@AYAH_REF@@ ¶N`.

## Independent semantic audit

First read the whole source and the whole current prose. Then perform both
directions of comparison without treating paragraph-number coverage as proof.

### Source to prose

For every source paragraph, identify all independently meaningful carriers,
triggers, mechanisms, branch contributions, composite effects, changed
readings, contextual-ayah roles, concrete details, examples, sequences,
contrasts, modalities, qualifications, boundaries, and live alternatives.

Locate explicit substantive wording for every contribution in the prose. A
heading, theme, broad conclusion, vague allusion, or citation is not a landing.
One source paragraph may require several landings. Pay particular attention to
details that disappear easily during compression:

- different mechanisms leading to a similar conclusion;
- the distinct role of each branch in a composite reading;
- concrete material, spatial, bodily, temporal, or causal detail;
- the particular work performed by each non-focus ayah;
- negation, uncertainty, attribution, conditions, scope, and stopping limits;
- alternatives that the source leaves unresolved.

Restore any missing or weakened contribution without restoring repetitive
exposition.

### Prose to source

For every substantive prose claim, identify its actual support in the source.
Remove additions, overstatement, falsely settled alternatives, and unsupported
causal links. Correct citations that are merely topically related. Check fused
sentences word by word for changed polarity, modality, agency, referent,
sequence, attribution, and scope.

## Independent synthesis audit

The desired result is synthesis, not paragraph-by-paragraph abridgement. Group
source contributions across the ayah by the carrier, question, image,
mechanism, contrast, sequence, or consequence they jointly develop. A good
movement states shared setup once, makes complementary findings interact, and
keeps their distinguishing details and limits explicit.

Challenge every repeated opening, setup, recap, conclusion, defensive
qualification, and run of output paragraphs that follows source order or cites
only the same-position source paragraph. Privately formulate the strongest
continuous merged alternative. Adopt it only when:

- every distinct carrier, trigger, mechanism, effect, detail, contextual role,
  qualification, boundary, and alternative remains explicit;
- citations remain local to the claims they support;
- the result becomes easier to follow rather than merely shorter; and
- the sentence or paragraph does not become overloaded.

Keep movements separate when merging would blur a different mechanism, object,
modality, scope, sequence, boundary, or alternative. Do not optimize for a
paragraph count, multi-source percentage, or retained-word ratio. Those numbers
cannot determine semantic quality.

## Reader and citation audit

Every prose paragraph must have one dominant movement and enough clues for the
reader to decide whether to open the cited editorial paragraphs. Where the
source provides them, the paragraph should reveal the carrier or image, its
trigger, the operative contact or mechanism, what changes in the reading, the
distinguishing detail, and the relevant qualification or boundary. A citation
alone is never sufficient.

Use citations exactly as follows:

`(@@AYAH_REF@@ ¶12, ¶15, ¶16, ¶17)`

- Write every number explicitly and never use a range.
- Cite the smallest complete clause or sentence actually supported.
- Use a multi-paragraph citation only for a genuinely shared synthesis.
- Cite separately sourced clauses locally even inside one sentence.
- Cite every source paragraph at least once and every output paragraph at
  least once.
- Do not use a citation to conceal absent content or uncertain provenance.
- Keep these citations distinct from Quran references such as `(29:41)`.

Read the prose once with citations mentally hidden. It must remain continuous,
natural Turkish rather than a claim list. Repair vague pronouns, citation-led
fragments, broken coordination, repeated locatives, subject-predicate mismatch,
and overloaded sentences. A paragraph may contain no more than 180
whitespace-delimited words, but this is a readability boundary rather than a
compression target.

Use only short level-2 headings (`##`) for genuine major transitions. Preserve
project display tags exactly as
`{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`; tags are paragraph-local,
and Arabic script may not appear outside them. List every Quran reference
explicitly: never write intervals such as `(1:1–3)`, `(1:1-3)`, `(1:1–1:3)`,
or `(1:1-1:3)`.

## Final validation

After completing the independent semantic, synthesis, reader, and Turkish
audits, run:

```bash
python3 _commentary/v5/validate_prose.py @@MIDDLE_PROSE_OUTPUT_PATH@@
python3 -B _commentary/v5/validate_middle_prose.py \
  --source @@SOURCE_PROSE_PATH@@ \
  --prose @@MIDDLE_PROSE_OUTPUT_PATH@@ \
  --ayah-ref @@AYAH_REF@@
```

Within this single review turn, repair every mechanical finding and rerun the
affected command until both report `ok`. Mechanical success does not replace
the direct semantic comparison. Finish only after the prose itself passes all
four audits and no unresolved concern remains.

## Inputs

Editorial source path: `@@SOURCE_PROSE_PATH@@`

<source_prose>
@@SOURCE_PROSE@@
</source_prose>
