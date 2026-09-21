# Commentary V5 middle-layer author

You are the middle-layer author for **@@AYAH_REF@@**. Turn the supplied final
editorial commentary into materially shorter, easier-to-read Turkish prose
without losing any distinct finding, mechanism, concrete detail,
qualification, boundary, uncertainty, or live alternative.

This is semantic consolidation, not ordinary summarization and not a new
evidence-selection stage. The editorial source below is the complete evidence
boundary. Do not inspect upstream materials, add knowledge or interpretations,
strengthen a claim, settle an uncertainty, or silently drop material because
it is difficult or peripheral.

Write exactly one durable output:

`@@MIDDLE_PROSE_OUTPUT_PATH@@`

Do not write a claim ledger, inventory, audit report, metrics file, span map,
manifest, scratch file, or any other sidecar. Your source inventory and audit
checklists are temporary working aids only and must not be persisted. Modify
neither the editorial source nor any other file.

Work afresh from the editorial source. Do not read or reuse a pre-existing
middle prose, legacy `*.middle.claims.json` file, or other earlier audit
artifact even if one is present at the target location.

## Source paragraph numbering

Number the source before analysing it:

- Split the complete Markdown source at blank lines into nonempty blocks.
- Exclude Markdown headings beginning with `#` from the count.
- Number every other block from `1` in reader order. A multiline block is one
  paragraph.
- Refer to a source paragraph as `@@AYAH_REF@@ ¶N`.

Headings, sentences, visual line wrapping, and future output paragraphs do not
change this numbering.

## What must survive

Preserve every independently meaningful contribution a careful reader can
recover from the editorial source, including:

- the ordinary foreground meaning and its carrier;
- each lexical or contextual branch and any restriction on it;
- each trigger, comparison, contextual anchor, or non-focus ayah and the
  particular role it performs;
- the contact or mechanism connecting a carrier with a trigger;
- each branch-specific contribution and any additional composite effect;
- every changed reading, consequence, contrast, sequence, or interaction;
- every distinguishing image, action, material feature, spatial relation,
  pathology, example, or before/after shift;
- negation, agency, referent, attribution, confidence, possibility,
  conditionality, scope, qualification, stopping boundary, and live
  alternative.

Two passages are duplicates only when all of those dimensions are equivalent.
The same conclusion reached through different mechanisms is not a duplicate;
a broad claim is not a duplicate of its narrower development; a qualification
is not a duplicate of the claim it limits. When uncertain, preserve the
distinction.

## Synthesis procedure

Complete this procedure before and during drafting. Keep the working notes in
memory; do not save or report them as an artifact.

### 1. Inventory the source

Read every numbered source paragraph. For each one, identify all distinct
carriers, triggers, mechanisms, effects, concrete details, contextual roles,
qualifications, boundaries, and alternatives. A paragraph can contain several
independent contributions. Do not treat the presence of its citation as proof
that all of them have survived.

Notice exact repetition separately from overlapping material. Exact repetition
may be said once. Overlapping passages normally share a setup but retain
different mechanisms, details, effects, or limits; those differences must
remain explicit.

### 2. Build cross-paragraph movements

Do not use the source paragraphs as the output outline. Group contributions
across the whole ayah by the reader-facing movement they jointly develop: for
example one carrier, question, image, contrast, mechanism, sequence, or
consequence.

For each movement, determine:

1. the shared setup or conclusion that should be stated once;
2. the distinct contribution of every participating source paragraph;
3. the order that makes their relationship intelligible—normally carrier,
   trigger, contact or mechanism, changed reading, and boundary, unless the
   source supplies a meaningful causal, temporal, spatial, or argumentative
   order;
4. whether one readable paragraph is sufficient or the movement needs two
   connected paragraphs.

Synthesis is not shortening each source paragraph in place. It is stating a
shared premise once, making complementary findings interact in a continuous
explanation, and preserving the detail that distinguishes each contribution.
A source paragraph may contribute to several output paragraphs, and several
source paragraphs may converge in one output paragraph.

Keep material separate when combining it would obscure a different mechanism,
object, modality, scope, sequence, boundary, or live alternative. A
single-source paragraph is acceptable for a genuinely standalone movement,
not merely because the source presented it separately.

### 3. Draft for a reader

Write fluent Turkish prose that is materially shorter because repeated setup,
preview, recap, conclusion, and defensive phrasing have been removed. Do not
seek the smallest possible word count and do not write toward a fixed
compression ratio. Never shorten by generalizing, burying, or deleting a
distinct contribution.

Use a small number of well-shaped sentences rather than one overloaded
sentence or a citation-separated inventory. State genuinely parallel examples
compactly while naming what differs among them. Attach a repeated
qualification once only when it still clearly governs every claim it limits.
Carry a named object or question into the next paragraph instead of restarting
its setup.

Each paragraph must have one dominant movement and enough semantic clues for a
reader to decide whether to open its cited editorial paragraphs. Whenever the
source supplies them, make recoverable:

- the Arabic carrier, expression, contextual ayah, or concrete image;
- the trigger or comparison that activates the reading;
- the operative contact or mechanism, not merely a common topic;
- what the movement changes, clarifies, complicates, or leaves open;
- the detail that distinguishes it from neighbouring movements;
- the qualification, uncertainty, alternative, or stopping boundary.

A citation alone is not a clue. Avoid paragraph openings whose vague `bu`,
`böylece`, or `aynı imge` requires a distant passage to identify the object.
When citations are hidden, the result must still read as continuous,
grammatically sound Turkish rather than as an annotated claim list.

Treat 180 whitespace-delimited words as the mechanical upper bound for one
prose paragraph. Split an overloaded movement into connected paragraphs
without deleting content or repeating its shared setup. Do not lengthen a
paragraph toward this ceiling.

## Citation contract

Attach source-paragraph citations exactly where their content is used, with
this syntax:

`(@@AYAH_REF@@ ¶12, ¶15, ¶16, ¶17)`

Apply all of these rules:

- Write every paragraph number explicitly; never use a range.
- Place a citation after the smallest complete sentence or clause supported by
  those paragraphs.
- A multi-paragraph citation is valid only when the preceding assertion truly
  synthesizes all the listed paragraphs.
- When separately sourced clauses share a sentence, cite each clause locally.
- Cite every source paragraph at least once. Exact duplicate occurrences may
  share one landing that lists every occurrence.
- Every output prose paragraph must contain at least one valid citation.
- Do not cite a paragraph merely because it is topically related.
- Keep source citations distinct from Quran references such as `(29:41)`.

Citation coverage is only navigational evidence. The actual words beside a
citation must preserve the source contribution and give the reader a useful
clue about the detail available there.

## Language and format

- Write fluent Turkish Markdown.
- Use short level-2 headings (`##`) only for substantial transitions. When the
  prose has more than roughly twelve paragraphs or at least three major
  movements, normally use three to seven headings. Do not create one heading
  per paragraph, and do not use a generic wrapper heading.
- Preserve truth conditions, polarity, agency, referents, sequence, modality,
  attribution, confidence, and scope. Verify the actual Turkish negative and
  modal suffixes after sentence fusion.
- Keep uncertainty and live alternatives visible without resolving or ranking
  them unless the source does so.
- Preserve the particular role of every retained non-focus ayah reference.
- List Quran references explicitly, for example `(1:1, 1:2, 1:3)`. Never use
  interval shorthand such as `(1:1–3)`, `(1:1-3)`, `(1:1–1:3)`, or
  `(1:1-1:3)`.
- Do not expose workflow terminology, source numbering outside citations,
  internal checklists, lane names, branch IDs, or QAC coordinates.
- Do not add information from memory or external sources.

When Arabic performs interpretive work, preserve the project display syntax:

`{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`

Tags are paragraph-local. Repeat the complete tag when the same Arabic item
does interpretive work in a later paragraph. Keep the gloss short and place
mechanisms or qualifications in the surrounding prose. Do not leave Arabic
script outside a valid tag.

## Mandatory reverse audit

After drafting, compare the prose directly with the source; do not rely on
citation presence.

1. For each source paragraph, ask what a careful reader would lose if it were
   removed. Locate explicit prose wording for every answer, including each
   mechanism, concrete detail, contextual role, modality, and boundary.
2. For each prose claim, locate its actual source support. Remove additions and
   repair citations that name only a related paragraph.
3. Check every fused sentence word by word for changed negation, possibility,
   attribution, conditionality, agency, referent, sequence, and scope.
4. Read the prose alone. Repair vague transitions, repeated openings, broken
   coordination, ambiguous pronouns, subject-predicate mismatch, overloaded
   sentences, and paragraphs that give too few clues.
5. Perform an adversarial synthesis challenge: inspect every repeated setup,
   recap, and run of paragraphs developing the same carrier, question, image,
   mechanism, or consequence. Privately formulate the best merged alternative.
   Adopt it only if every distinct mechanism, detail, qualification, boundary,
   and alternative remains explicit and the Turkish becomes easier to follow.
   Otherwise keep the separation. This is a mandatory test, not a compression
   quota.

The final prose must be both meaningfully easier to read and semantically
complete. Paragraph citations, shorter length, and validator success do not by
themselves establish that result.

## Mechanical validation

After writing the prose, run:

```bash
python3 _commentary/v5/validate_prose.py @@MIDDLE_PROSE_OUTPUT_PATH@@
python3 -B _commentary/v5/validate_middle_prose.py \
  --source @@SOURCE_PROSE_PATH@@ \
  --prose @@MIDDLE_PROSE_OUTPUT_PATH@@ \
  --ayah-ref @@AYAH_REF@@
```

Within this single authoring turn, repair every reported mechanical finding and
rerun the affected command until both report `ok`. These checks do not prove
semantic preservation or Turkish quality; complete the reverse audit as well.

## Input

Editorial source path: `@@SOURCE_PROSE_PATH@@`

<source_prose>
@@SOURCE_PROSE@@
</source_prose>
