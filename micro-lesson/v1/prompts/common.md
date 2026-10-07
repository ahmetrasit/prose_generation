# Shared authoring instruction

Teach a Turkish-speaking reader with almost no Arabic through an existing Quran
commentary. Keep its text unchanged. Attach each lesson to the paragraph that
makes it useful, using only the supplied passage and relevant linguistic evidence.

## Teaching

- Discover every distinct worthwhile opportunity, not only the first displayed one.
  There is no lesson quota or whole-page length budget.
- Teach one coherent observation in one or two short Turkish sentences. Roughly
  15–45 words is a useful aim, never a word-count gate. Explain before naming terms.
- One observation can integrate multiple concepts. Split only when the second
  lesson enables a different recognition or understanding. A necessary explanation
  of the first observation can stay in its second sentence.
- Point to the actual Arabic feature with a Turkish reading. Give the reader a
  reusable way to notice it without turning a local example into an exceptionless rule.
- Each lesson stands alone when cycled to. No “as explained above.” Use local verse
  comparisons when they help; dictionary illustrations remain dictionary illustrations.
- Commentary is the teaching occasion, not proof. Do not inherit an etymology,
  historical claim or syntactic inference merely because the commentary asserts it.
- Root meanings do not all enter one occurrence. Morphological patterns are not
  fixed semantic formulas. Preserve source qualifications and branch boundaries.

## Multiple ontology annotations

Read ONTOLOGY.md and the complete catalog index. Consult full concept definitions
and boundaries for actual attachments. Return `concepts: [{id, role}, ...]`.
Roles are `teaches`, `reinforces`, and `contrasts`. Include at least one `teaches`;
several are welcome when the same observation teaches them together. There is no
primary-objective field, category limit, or engine-to-category restriction.

Annotate what the wording actually teaches. A grammar lesson can teach a Turkish
mapping distinction; a mapping lesson can teach a grammatical construction. Choose
the most precise applicable concepts. Do not add parents merely because a child
was annotated. A parent can also be attached if its general principle is explicitly
taught. Give each concept at most one role, preferring the role best supported by
the wording: teaches over reinforces when newly explained. `contrasts` means the
concept itself is contrasted, not that two words happened to be compared.

Keywords are lookup handles, not invented free tags. Emit stable concept IDs.
Root, branch, lexical-unit and gloss identities stay in evidence/branch references.
Knowing a general concept never means knowing all lexical instances of it.

## Prerequisites and difficulty

Inspect the relations of all annotated concepts, then retain only knowledge that
this wording assumes. Catalog prerequisites can be omitted when explained within
the lesson. Do not require script literacy when the reading and prose suffice.
Simplify wording before asking for more prior knowledge. An introduced concept
cannot also be a required prerequisite. Merely mentioning a concept is not a reason
to annotate or require it.

Use shared `reminder_ids`, never warning prose or a duplicate prerequisite list.
C017 resolves to `ML:R017:requires` or `ML:R017:helped_by`, with the same convention
for every concept. Emit no more than one relation per concept. Author without
learner state; the application resolves templates, mastery and dismissal.

Levels describe the actual explanation: 0 no assumed Arabic; 1 a simple recognition;
2 a construction or comparison; 3 combined concepts or alternative analyses;
4 advanced nuance with substantial prior knowledge. Do not derive level from the
number of tags or graph depth. There is no separate required depth classification.

## Arabic and Turkish readings

Copy Arabic from the supplied source. Preserve meaningful long vowels and consonant
distinctions in the supplied Turkish reading; use a consistent style within the page.
Do not introduce Turkish vowel harmony as a rule of Arabic pronunciation. Preserve
the source's supported pronunciation rather than guessing from unvowelled spelling.
Show boundaries with a hyphen when explaining a particle or suffix. Explain any
connected/pause reading difference that matters; an anchor may carry `reading_note_tr`.
Transliteration is a reading aid, not evidence of root identity. Dictionary examples
get their dictionary source locator, never a fabricated ayah label.

## Output and unresolved opportunities

Return JSON following `schemas/engine-output.schema.json`. Include every assigned
paragraph, including empty lists with a brief note. Use compact, resolvable evidence
locators. `anchors[].source_ref` identifies the exact verse or dictionary phrase;
add a word locator when an expression is repeated or its exact location matters.
Optional fields are omitted when unused, not filled with boilerplate.

Choose a semantic `key` unique within paragraph and engine. The assembler builds
`<page_id>:<paragraph_id>:<engine>:<key>`. Retain supplied keys for wording edits;
changed teaching points get new keys. Annotations and rank are not identities.

Use `deferred` for missing evidence, unresolved conflicts, or an exceptional ontology
gap. Keep anchors, the opportunity, and the exact question whose answer would unblock
it. Keep any supported draft for a catalog gap. Propose a definition and parents,
never an ID. Do not put an unresolved claim in both `lessons` and `deferred`.
If evidence disproves the idea, record a short rejection note rather than leaving
an unsupported claim as a permanent future task.
