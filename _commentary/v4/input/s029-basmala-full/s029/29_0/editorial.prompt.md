# Commentary v4 editorial handoff

Continue as the same live canonical writer for **29:0**. Revise the
exact four first-pass files below under the unchanged editorial instructions
embedded verbatim in this handoff.

The explicit destination map below overrides the filename-location example in
the embedded instructions. Write exactly the four editorial files listed here
and modify nothing else.

## Semantic invariants

- Improve cadence, continuity, clarity, and repetition without deleting,
  combining, weakening, or genericizing any finding.
- Preserve every finding's top-level semantic `prose_statement` verbatim and
  exactly once. Its editorial landing-map `prose_quote` must equal that exact
  sentence, not merely point to nearby generic prose.
- Preserve every branch-activation sentence listed in the first-pass index's
  landing map verbatim and exactly once in editorial reader prose. Integrate
  these sentences fluently; they explain which carrier/root meaning meets which
  trigger and why the resulting reading becomes active.
- Keep internal root/branch IDs, finding IDs, evidence IDs, lane names, and
  QAC/analysis coordinates out of reader prose. They remain in the apparatus.
- Preserve each finding's context refs, evidence boundary, concrete semantic
  details, counter-readings, and epistemic qualification.
- Preserve each finding's exact single-line provenance-ledger JSON object from
  the first-pass evidence and index exactly once in each editorial apparatus
  file. Do not edit, reserialize, or duplicate it, and make each landing-map
  apparatus quote encompass the complete object.
- Replace the first-pass landing map with exactly one final fenced
  `commentary-v4-landing-map` JSON block at the end of the editorial findings
  index. Use schema `commentary-v4-canonical-landing-map-v1`, ayah `29:0`, and
  phase `editorial`. Keep the same finding order and exact activation quote
  arrays. Repeat each finding's exact semantic `prose_quote`; update its unique
  `evidence_quote` and `index_quote` to point to the editorial files. Evidence
  and index quotes must contain the exact finding ref and exact provenance
  ledger. Quotes for different findings may not overlap or contain one another.
  Write no text after the block.

## First-pass inputs

- prose (`sha256:1e7164712f955f8f13856e64bd1dec1af26f10a59f062abd86ccb6b0862adf7f`): `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.prose.tr.md`
- evidence (`sha256:f9a5302adfe7dd67504a572976d1f91b1c4fe73a4b0e0c100cc35f1378a6b28d`): `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.evidence.tr.md`
- findings index (`sha256:eebb75b00716e412e6d7009d992cebc8da10ec1a7891e39bceabdf0a826d95b7`): `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.index.tr.md`
- friction (`sha256:2e3985cf49fcafe3f6f903aba2ef45b8a819baa91ac756f35f005d42543e6032`): `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.friction.tr.md`

## Editorial outputs

- prose: `_commentary/v4/editorial/s029-basmala-full/s029/29_0/29_0.prose.editorial.tr.md`
- evidence: `_commentary/v4/editorial/s029-basmala-full/s029/29_0/29_0.evidence.editorial.tr.md`
- findings index: `_commentary/v4/editorial/s029-basmala-full/s029/29_0/29_0.index.editorial.tr.md`
- friction: `_commentary/v4/editorial/s029-basmala-full/s029/29_0/29_0.friction.editorial.tr.md`

## Unchanged editorial instructions - verbatim

<editorial_instructions>
Please revise your Layer 2 output editorially without reducing its interpretive yield or changing its evidentiary judgments.

Create exactly one new editorial counterpart for each of the four first-pass files: prose, evidence, findings index, and friction. Do not edit, replace, append to, or rename the first-pass files. Derive each new filename by inserting `.editorial` immediately before the target-language suffix when one is present, and otherwise immediately before `.md`. For example, `{unit}.prose.tr.md` becomes `{unit}.prose.editorial.tr.md`. Apply the same rule to evidence, index, and friction. Write exactly four new files and modify nothing else.

Preserve the ayah’s plain meaning and every accepted resonance with a distinct mechanism or reader payoff. Let compatible or countervailing resonances remain alive together; do not rank, disambiguate, or select among them. If the ayah has no earned local resonance, do not invent one: its linguistic, grammatical, formal, or acoustic force may carry the commentary. Do not introduce Layer 3, surah-wide channels, or network claims.

Use no length, paragraph, section, or heading quota. Do not compress merely to shorten the commentary. Merge material only when it performs the same work and gives the reader the same payoff.

Rewrite the prose as fluent, contemporary Turkish for a regular reader. Remove English expressions, analyst shorthand, workflow language, and stiff technical calques. Retain a linguistic term only when it genuinely helps the reader: first explain its concrete effect in natural Turkish, then name it if still useful. Preserve the underlying linguistic finding while naturalizing its expression.

Apply the structured Arabic span consistently:

{ar:<Arabic surface>, tr:<Turkish-readable transliteration>, gloss:<Turkish meaning>}

Give the full structured span when an Arabic ayah word first becomes active and when a later paragraph returns to it after the prose has moved elsewhere. Within one immediate movement, its Turkish meaning or a natural pronoun is enough across paragraph boundaries when the referent remains unmistakable. Never let bare transliteration be the only representation of an Arabic word in a paragraph.

Use short, reader-facing subtitles only where the reading genuinely changes movement. Let the ayah determine their number and placement. Subtitles should create an expectation about what becomes visible next; they must not name words, roots, findings, evidence categories, resonances, or workflow stages.

Create cinematic continuity without adding drama or interpretation. Each section should inherit a concrete image, question, tension, relation, or motion from the preceding section and carry it somewhere new. Use transitions to change the reader’s viewpoint or deepen what is already present. Avoid restarting every paragraph as an independent finding or repeatedly announcing another image. Hooks must arise from the ayah and its accepted findings.

Distinguish architecture from texture. A major move, where the reader's understanding genuinely changes, should arrive through its concrete image or scene and have room to land. A refinement that adds a facet, boundary, or comparison to an established reading should move faster, without rebuilding its setup or repeating an already absorbed Arabic span. Vary paragraph openings, and use an explicit boundary negation only when the positive statement would otherwise invite a likely misreading or lose essential containment. Rhetorical weight does not alter evidentiary status: every retained finding must remain recoverable.

Keep distinct findings recoverable even when they belong to one larger movement. Let the ending return naturally to the ayah’s plain force and show what has become newly visible, rather than listing all findings again.

Create the editorial evidence, findings index, and friction files so that they exactly match the editorial prose and every retained finding still has an identifiable landing.

</editorial_instructions>
