# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:28**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.middle.claims.json`

Write exactly those two files and modify nothing else.

The prose is the reader surface. The ledger is accountability metadata. A
source-paragraph citation proves provenance only; the atomic claim ledger must
prove semantic coverage.

## Source paragraph numbering

Number the source prose before analysing it.

- Split the complete Markdown source at blank lines into nonempty blocks.
- Exclude Markdown headings beginning with `#` from the count.
- Number every other block from `1` in reader order, including a multiline
  block as one paragraph.
- Paragraph numbering is local to this ayah and must remain stable throughout
  the task.
- Refer to source paragraphs as `31:28 ¶N`.

Do not let headings, output paragraphs, sentences, or visual line wraps alter
the source numbering.

## Governing distinction

Compression may remove repeated expression, but it may not remove semantic
content.

A distinct semantic unit is the smallest independently preservable assertion
or interpretive movement whose omission would erase or weaken something a
careful reader could recover from the source. It may include:

- a focus carrier and its ordinary meaning;
- a lexical or contextual branch, including a form or referent restriction;
- an independent trigger or contextual anchor;
- the contact or mechanism connecting carrier and trigger;
- the particular contribution made by one branch in a multi-branch reading;
- a changed reading, consequence, contrast, sequence, or interaction;
- a concrete image, action, pathology, material feature, spatial relation, or
  before/after shift;
- an inter-ayah relation or the particular role of a cited ayah;
- modality, attribution, confidence, scope, qualification, boundary, or live
  alternative.

Do not fragment a relation into meaningless labels. If an assertion depends on
the contact between a carrier and a trigger, retain that contact inside the
same unit. In a multi-branch construction, inventory each branch-specific
contribution separately and inventory the composite interaction separately
when the source gives that interaction an additional meaning.

One source paragraph can contain many units. Never treat one citation as
coverage of the whole paragraph without identifying all of its units.

## Required working sequence

Complete these stages in order. Do not draft the reader prose before stages
1–3 are complete.

### 1. Atomic inventory

Read every numbered source paragraph and extract all of its distinct semantic
units. Assign stable references in source order:

- `p001.u01`, `p001.u02`, ... for source paragraph 1;
- `p002.u01`, ... for source paragraph 2; and so on.

For each unit, record a faithful Turkish statement of the complete assertion,
not merely a topic label. Also record every applicable carrier, trigger,
mechanism, changed reading, concrete detail, boundary, alternative, and
contextual ayah reference. Record a short exact source anchor that includes any
word carrying negation, uncertainty, restriction, comparison, or attribution.
Also classify the unit's truth status—for example asserted, negated, possible,
attributed, conditional, or presented as a live alternative. Use `null` or an
empty list where a field genuinely does not apply; do not invent missing
components.

An exact source anchor is a contiguous verbatim substring of its numbered
source paragraph. Copy its Unicode characters and complete display tags
exactly. Do not paraphrase it, remove a tag, normalize punctuation, or insert an
ellipsis. Prefer the shortest substring that still identifies the assertion
and preserves its controlling polarity or modality.

If a source paragraph is wholly transitional or wholly repeats earlier
content, record that disposition explicitly and identify the exact unit or
units it restates. Do not use “transition” or “duplicate” as a loophole for a
paragraph containing even one new detail, restriction, example, or change of
emphasis.

### 2. Equivalence and overlap audit

Compare units across the whole ayah before deciding what can be said once.
Classify their relation as one of:

- `unique`: no other unit makes the same assertion;
- `exact_duplicate`: the same semantic assertion is repeated with no new
  carrier, trigger, mechanism, effect, detail, modality, boundary, alternative,
  or contextual role;
- `overlapping_complement`: the units share a conclusion or setup but each
  contributes some distinct content;
- `related_distinct`: they concern the same theme but perform different
  semantic work.

Two units may be deduplicated only as `exact_duplicate`. Test equivalence on all
of the following dimensions:

1. carrier or referent;
2. trigger, source relation, or contextual anchor;
3. contact, operation, or mechanism;
4. contribution, changed reading, or reader consequence;
5. concrete details and examples;
6. modality, attribution, scope, boundary, and live alternatives.

If any material dimension differs, the units are not duplicates. A broad claim
and a narrower claim are not duplicates. The same conclusion reached through
different mechanisms is not a duplicate. Different branches contributing to
one composite image are not duplicates. A qualification is not a duplicate of
the claim it limits. When uncertain, preserve the distinction.

An exact duplicate may receive one prose landing, but that landing must retain
the paragraph references of every duplicate occurrence. Overlapping
complements should normally enter the same synthesis cluster when their shared
setup can be stated once and their distinct contributions can still be
followed. Keep them in separate clusters only when combining them would blur a
different mechanism, effect, modality, boundary, sequence, or object of
attention; record that reason rather than defaulting to source order.

### 3. Synthesis clustering and coverage plan

Do not use the source paragraphs as the output outline. Build synthesis
clusters before drafting. A cluster is one developing reader question or
semantic movement whose units can form a continuous explanation.

For each cluster, do this explicitly:

1. Name the dominant question, carrier, image, contrast, or consequence.
2. Gather units from every source paragraph that helps answer that question.
3. Identify the setup or conclusion those units repeat. Plan to state it once.
4. List what remains unique: each trigger, mechanism, branch contribution,
   concrete detail, change, qualification, and alternative.
5. Order those unique contributions so that the reader can follow the
   construction—normally carrier or foreground, then trigger, contact or
   mechanism, changed reading, and boundary. Use another order when the source
   supplies a meaningful temporal, causal, spatial, or argumentative sequence.
6. Decide whether the cluster fits one readable paragraph or needs two or more
   connected paragraphs. Split when the operations would otherwise become an
   inventory or require the reader to remember too many unresolved branches.
7. Assign every unit one exact planned landing and every source paragraph the
   citations that will expose where its contribution is used.

Several source paragraphs may therefore become one output paragraph, and one
complex source paragraph may contribute to several output paragraphs. A
single-source output paragraph is permitted when its movement is genuinely
standalone, not merely because it appeared separately in the source.

A synthesis cluster is not required to equal one output paragraph. When a
cluster contains several steps, give it two or more connected paragraphs and
list all of them in the cluster ledger. Preserve the shared setup by stating it
once, then let the following paragraph carry forward a named object or question
instead of repeating that setup.

Arrange clusters in a reader-facing order rather than source paragraph order,
while preserving a supported sequence where order itself carries meaning.
Adjacent clusters should either carry forward a specific object, action,
question, contrast, or consequence, or make an honest change of perspective.

Treat source mirroring as a diagnostic failure, not a neutral default. If the
output retains nearly the same paragraph count and order as the source and
most output paragraphs cite only the same-position source paragraph, stop and
redo the clustering. Accept that pattern only when a unit-by-unit audit shows
that the source was already irreducibly organized and the ledger gives a
specific non-merging reason for every standalone cluster. Do not manufacture
mergers merely to improve a metric; semantic coherence governs the decision.

For every unit, choose one substantive prose landing. A landing must be an
exact sentence or clause that expresses the unit's actual content. A heading,
topic label, vague thematic sentence, citation, or general conclusion is not a
landing.

Before drafting, confirm privately that:

- every source paragraph has been assessed;
- every substantive unit has a planned landing;
- every exact duplicate is mapped to a canonical unit;
- every overlapping complement either shares a synthesis cluster or has a
  specific semantic reason to remain apart;
- every boundary remains attached to the interpretation it limits;
- every branch in a composite reading remains distinguishable;
- the planned structure is not simply the source paragraph sequence with
  shorter sentences.

### 4. Reader prose

Write fluent Turkish commentary that is materially shorter than the source
because duplicated exposition, repeated setup, repeated conclusions, and
repeated defensive phrasing have been removed.

Do not optimize for the smallest possible word count and do not impose a fixed
compression ratio. If a reduction cannot be made without deleting a semantic
unit, keep the unit. Unusually large compression is acceptable only when the
ledger demonstrates that repetition—not omitted content—accounts for it.

Make the prose shorter through composition:

- establish an ordinary meaning or shared setup once where the subsequent
  movement can clearly carry it forward;
- combine exact duplicates and accumulate all of their source references;
- integrate compatible complementary units into one developing explanation;
- state repeated qualifications once, precisely, beside every claim they
  jointly limit;
- replace repeated previews and recaps with the explanation itself;
- use compact parallel construction for genuinely parallel examples while
  preserving what differs among them;
- omit verbal padding, not semantic operations.

Do not merely shorten each source paragraph in place. Synthesis means that a
shared premise is stated once, contributions from different source paragraphs
are made to interact in one intelligible development, and their paragraph
references appear beside the particular claims they supply.

Do not create one sentence or paragraph per ledger unit. Conversely, do not
hide many units beneath a broad thematic label, an inventory of nouns, or an
unexplained conclusion. If a sentence becomes too dense for the separate
operations to remain intelligible, distribute it across connected sentences or
paragraphs.

Do not let citation placement turn the prose back into a claim ledger. Avoid a
serial rhythm of tiny assertion, citation, tiny assertion, citation when the
assertions belong to one movement. Join them with explicit logical or
grammatical relations, using clause-local citations where their sources differ.
Every sentence must read as part of a continuous Turkish explanation even when
all citations are temporarily hidden.

Each paragraph must advance the reading. Avoid restarting an established
point, re-explaining the same ordinary meaning, announcing what the next
paragraph will say, or adding a closing recap. End by completing the last
consequential movement.

## Reader trace-clue contract

Every output paragraph must give the reader enough semantic clues to decide
whether to open its cited editorial paragraphs for more detail. A citation by
itself is not a clue.

At the paragraph's beginning, make the object of attention recoverable without
requiring the reader to reconstruct a vague pronoun such as “bu”, “böylece”, or
“aynı imge” from a distant passage. Across the paragraph, make these elements
visible whenever the source supplies them:

- the relevant Arabic carrier, expression, contextual ayah, or concrete image;
- the independent trigger or comparison that activates the reading;
- the operative contact or mechanism, not only a shared topic;
- what this changes, clarifies, complicates, or leaves open in the ayah;
- the concrete detail that distinguishes this movement from its neighbours;
- the qualification, uncertainty, live alternative, or stopping boundary.

These elements need not appear as a formula or in one sentence. They must form
a short, natural Turkish explanation with one dominant movement. A reader
should be able to summarize why each cited source paragraph matters before
opening it. If the paragraph offers only a theme, a conclusion, or a list of
images, revise it.

Prefer a small number of well-shaped sentences over one overloaded sentence.
When several sources contribute parallel examples, state their common work
once and name the discriminating detail of each. When they contribute different
steps, let the paragraph show what the next step adds or changes.

Treat 180 whitespace-delimited words as a mechanical upper bound for one
reader-prose paragraph. This is a readability boundary, not a compression
target: split an overlong paragraph into connected paragraphs without deleting
units or repeating their shared setup. Also split a shorter paragraph when it
contains too many independent operations to follow comfortably.
Never write toward the 180-word ceiling. During the final reader pass, inspect
paragraphs near it and retain them only when their movement remains easy to
follow without rereading.

## Source-paragraph citation contract

Attach citations where source content is actually used. Use exactly this
syntax:

`(31:28 ¶12, ¶15, ¶16, ¶17)`

Apply these rules:

- Write every paragraph number explicitly; never use a range such as `¶12–17`.
- Place a citation immediately after the smallest sentence or clause supported
  by those paragraphs. Do not use one blanket citation for a paragraph whose
  sentences draw on different sources.
- Citation locality does not require sentence fragments or one sentence per
  source paragraph. When several clauses form one movement, keep the syntax
  continuous and place each citation after the clause it supports.
- A citation may contain several paragraph numbers only when the immediately
  preceding assertion genuinely synthesizes all of them.
- When one sentence contains separately sourced clauses, cite the clauses
  separately.
- Cite every source paragraph at least once. For an exact duplicate, include
  all duplicate paragraph numbers at the shared landing. For a purely
  transitional paragraph, attach its number only to the proposition it
  actually restates; do not invent a contribution for it.
- Every reader-prose paragraph must contain at least one source-paragraph
  citation.
- Do not cite a paragraph merely because it is topically related.
- Keep source-paragraph citations distinct from Qur'an references such as
  `(29:41)`.

The citation must remain reader-visible, but citations do not replace
explanation and do not count as semantic landings.

## Reader-prose language and format

- Write in fluent Turkish Markdown.
- Use short level-2 headings (`##`) only for substantial developments; headings
  do not carry source citations. When an output has more than roughly twelve
  prose paragraphs or clearly contains at least three major movements, use a
  small set of headings—normally three to seven—to expose those transitions.
  Do not leave a long multi-movement commentary as an undifferentiated stream,
  and do not create a heading for every paragraph.
- Preserve the ordinary foreground reading while explaining any secondary
  resonance.
- Preserve truth conditions, agency, referents, sequence, negation, modality,
  confidence, and scope.
- Preserve polarity morpheme by morpheme. A source statement such as “cannot
  be inferred,” “does not establish,” or “is not necessary” must not become
  “can be inferred,” “establishes,” or “is necessary” through shortening,
  suffix loss, or sentence fusion. The same applies to possibility,
  attribution, comparison, and conditionality.
- Keep uncertainty and live alternatives visible without resolving or ranking
  them unless the source does so.
- Retain every concrete detail that distinguishes one unit from another.
- Preserve each non-focus ayah reference beside the contextual role it performs.
- When one movement depends on several ayat, write every reference explicitly,
  for example `(1:1, 1:2, 1:3)`. Never use Quran interval shorthand such as
  `(1:1–3)`, `(1:1-3)`, `(1:1–1:3)`, or `(1:1-1:3)`, whether parenthesized or
  embedded in a sentence. Do not replace a concrete reference with a vague
  location such as “önceki âyetlerde” unless the explicit references remain
  visible there.
- Do not expose ledger IDs, lane names, branch IDs, QAC coordinates, workflow
  language, or this consolidation process in reader prose.
- Do not add information from memory or external sources.

When an Arabic word, phrase, carrier, or anchor performs interpretive work,
preserve the project display-tag syntax:

`{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`

Tags are paragraph-local. Repeat a complete tag when the same Arabic item does
interpretive work in a later output paragraph. Use one consistent
Turkish-readable transliteration for the same surface. Keep tag glosses short;
put mechanisms, qualifications, and consequences in the surrounding prose. Do
not leave Arabic script outside valid tags.

## Atomic claim ledger

Write the reader prose first, then write one valid UTF-8 JSON object to
`_commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:28",
  "source_paragraph_count": 0,
  "output_paragraph_count": 0,
  "metrics": {
    "source_word_count": 0,
    "output_word_count": 0,
    "retained_word_ratio": 0.0,
    "multi_source_output_paragraphs": 0,
    "single_source_output_paragraphs": 0,
    "same_position_singleton_paragraphs": 0,
    "output_to_source_paragraph_ratio": 0.0
  },
  "source_paragraphs": [
    {
      "paragraph": 1,
      "disposition": "substantive",
      "unit_refs": ["p001.u01"],
      "restates_unit_refs": [],
      "note": null
    }
  ],
  "synthesis_clusters": [
    {
      "cluster_ref": "c001",
      "movement_tr": "Okurun izlediği baskın soru veya anlam hareketi",
      "unit_refs": ["p001.u01"],
      "source_paragraphs": [1],
      "output_paragraphs": [1],
      "kind": "standalone",
      "why_together_or_apart_tr": "Neden bu birimler birlikte işlendi veya neden tek başına kaldı"
    }
  ],
  "semantic_units": [
    {
      "unit_ref": "p001.u01",
      "source_paragraph": 1,
      "unit_order_in_paragraph": 1,
      "source_anchor": "Olumsuzluk veya kiplik dahil kısa tam alıntı",
      "assertion_tr": "Eksiksiz ve sadık Türkçe önerme",
      "truth_status": "asserted",
      "role": "branch_contribution",
      "carrier": null,
      "trigger_or_context": null,
      "contact_or_mechanism": null,
      "changed_reading_or_contribution": null,
      "concrete_details": [],
      "boundaries_and_qualifications": [],
      "live_alternatives": [],
      "contextual_ayah_refs": [],
      "relation": {
        "classification": "unique",
        "canonical_unit_ref": "p001.u01",
        "related_unit_refs": [],
        "rationale": "Neden ayrı tutulduğu veya gerçekten eşdeğer olduğu"
      },
      "landing": {
        "output_paragraph": 1,
        "anchor": "Çıktıdaki benzersiz tam cümle veya anlamlı yan cümle",
        "citation": "(31:28 ¶1)"
      }
    }
  ],
  "audit": {
    "unassessed_source_paragraphs": [],
    "uncited_source_paragraphs": [],
    "unlanded_unit_refs": [],
    "unclustered_unit_refs": [],
    "units_with_nonunique_anchors": [],
    "unresolved_deduplication_questions": [],
    "unmerged_overlap_groups": [],
    "source_mirroring_findings": [],
    "polarity_or_modality_mismatches": [],
    "reader_paragraphs_without_detail_clues": [],
    "overdense_output_paragraphs": [],
    "notes": []
  }
}
```

Use these ledger rules:

- `source_paragraphs` contains exactly one row for every numbered source
  paragraph, in order.
- `disposition` is `substantive`, `duplicate_only`, or `transitional_only`.
- A `substantive` paragraph has at least one unit. A `duplicate_only` paragraph
  still has its own `pNNN.uNN` unit rows, marks them as exact duplicates, and
  names their canonical units in `restates_unit_refs`. A `transitional_only`
  paragraph may have no unit rows, but it names the exact earlier or later
  units it restates. Both non-substantive dispositions explain the
  classification in `note`.
- `synthesis_clusters` contains every semantic unit exactly once. Use `kind`
  `synthesis` when a cluster draws substantive contributions from more than one
  source paragraph and `standalone` when it does not. A standalone cluster must
  give a concrete semantic reason in `why_together_or_apart_tr`; “separate
  source paragraph” and “different topic” are not sufficient reasons.
- `movement_tr` is one concise sentence identifying the reader-facing movement,
  not a list of its units. Cluster fields are planning accountability, not a
  second commentary.
- `semantic_units` contains every extracted unit in source order. Do not omit a
  duplicate unit; mark it `exact_duplicate` and point
  `canonical_unit_ref` to the canonical occurrence.
- `source_anchor` is a short exact phrase from the numbered source paragraph.
  It must contain the word or suffix that controls negation, modality,
  attribution, conditionality, or restriction when one is present. It must be
  a contiguous verbatim substring; ellipses, stripped display tags,
  punctuation normalization, and paraphrase are invalid.
- `truth_status` is a short controlled description such as `asserted`,
  `negated`, `possible`, `conditional`, `attributed`, or `live_alternative`;
  combine labels only when the source genuinely combines them.
- Recommended `role` values are `foreground`, `lexical_branch`,
  `contextual_trigger`, `mechanism`, `branch_contribution`,
  `composite_interaction`, `changed_reading`, `concrete_detail`,
  `sequence_or_contrast`, `boundary`, `qualification`, `live_alternative`, and
  `contextual_relation`. Use a more precise value only when necessary.
- `classification` is exactly `unique`, `exact_duplicate`,
  `overlapping_complement`, or `related_distinct`.
- For `unique`, `overlapping_complement`, and `related_distinct`, set
  `canonical_unit_ref` to the unit itself. For `exact_duplicate`, set it to the
  earliest fully equivalent unit.
- Every unit, including a duplicate, points to the exact substantive landing
  that preserves it. Duplicate units may share their canonical unit's landing.
- `anchor` is copied exactly from the reader prose and must occur there once.
  It must express the unit, not merely mention its topic.
- `citation` records the source-paragraph citation visible beside that landing.
- Compute `metrics` using whitespace-delimited words in the complete source and
  reader-prose files. The ratio is diagnostic, not a quota and not evidence of
  completeness.
- Derive the structural metrics from non-heading output prose paragraphs.
  `multi_source_output_paragraphs` counts paragraphs whose valid citations name
  more than one distinct source paragraph. `same_position_singleton_paragraphs`
  counts output paragraph N when its citations name only source paragraph N.
  `output_to_source_paragraph_ratio` is output paragraph count divided by
  source paragraph count. These metrics diagnose source mirroring; they never
  authorize unrelated mergers.
- Keep the ledger compact. Write `assertion_tr` as one complete concise
  proposition, `relation.rationale` as one discriminating clause, and anchors
  as the shortest unique substantive clause. Do not paste whole source or
  output paragraphs and do not repeat identical explanations across fields.
- All problem arrays in `audit` must be empty before completion. `notes` may
  document preserved source tensions or other nonblocking facts. If a
  deduplication question remains unresolved, classify the units as distinct
  and preserve both.

The ledger may repeat source language for accountability, but none of its
technical fields or IDs may leak into the reader prose.

## Final semantic audit

Audit the finished prose against the source and ledger—not merely against the
paragraph citations.

For every source paragraph, ask: what would disappear if this paragraph were
removed from the source? Confirm that every such item appears in a semantic
unit or is demonstrably an exact duplicate. For every semantic unit, locate the
exact prose anchor and verify that the anchor retains its carrier, mechanism,
effect, details, and limit rather than only its general topic.

Then perform four separate passes:

1. **Synthesis pass:** inspect every overlap group and cluster. Confirm that
   repeated setup is said once, complementary contributions interact, and each
   standalone cluster has a real semantic reason. Compute the structural
   metrics and investigate any near one-to-one source/output pattern.
2. **Truth-condition pass:** compare each unit's `source_anchor`,
   `truth_status`, and prose landing word by word for negation, possibility,
   attribution, conditionality, agency, referent, and scope. Do not infer that
   fluent prose has preserved polarity; verify the actual Turkish suffixes and
   auxiliaries.
3. **Reader-clue pass:** read only the finished prose and citations, without the
   ledger. For each paragraph, verify that a reader can identify the carrier or
   image under discussion, why the cited sources are relevant, what changes in
   the ayah reading, and where the claim stops. Record and repair any paragraph
   that requires the ledger to answer those questions.
4. **Turkish prose pass:** hide the citations temporarily and read the prose as
   continuous Turkish. Repair broken coordination, case-suffix attachment,
   subject-predicate mismatch, dangling or ambiguous pronouns, repeated
   locatives, overloaded sentences, and citation-driven fragments. Confirm that
   each paragraph has one dominant movement and that adjacent sentences state
   how their ideas relate. Restore and recheck every citation afterward; if an
   edit changes a landing, update its exact ledger anchor and all metrics.

Specifically reject the draft if any of the following is true:

- a source paragraph is cited but one of its units has no landing;
- several branches have been collapsed into their shared conclusion;
- a contextual ayah remains named but its particular role has disappeared;
- a concrete example or image has been replaced by a general category;
- a qualification or live alternative has become implicit;
- different modalities or scopes have been equalized;
- a negative, possibility, attribution, or condition has changed polarity;
- an output anchor is too vague to prove the unit assigned to it;
- compatible source movements remain as same-position singleton paragraphs
  merely because they were separate in the source;
- an output paragraph lacks enough discriminating clues to guide the reader
  into its cited source paragraphs;
- Quran references use interval shorthand instead of naming every ayah;
- the prose reads as a citation-separated inventory when citations are hidden,
  or a Turkish sentence has broken coordination or an unclear grammatical
  subject;
- shortening depends on removing content rather than repeated expression.

Revise until the prose is both materially easier to read and semantically
complete. Do not describe it as “lossless” merely because every source
paragraph is cited; that conclusion is warranted only when every atomic unit
has a valid substantive landing and every problem audit array is empty.

## Mechanical validation

After writing both outputs, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_28/31_28.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_28/31_28.middle.claims.json \
  --ayah-ref 31:28
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_28/31_28.prose.editorial.tr.md`

<source_prose>
Âyet, muhatapların yaratılmasını ve diriltilmesini bir tek canın yaratılışıyla aynı ölçüde anlatır: {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ve {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz}, {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi}. Muhataplar çoğul, ölçü alınan can tektir. Böylece kıyas, kişileri birbirine katmadan iki eylemin ölçeğini insanın tanıdığı bir birimle görünür kılar.

## İki Eylem, Tek Ölçü

İlk cümlede {ar:مَّا, tr:mā, gloss:olumsuzluk edatı} yaratılma adından, {ar:لَا, tr:lā, gloss:olumsuzluk edatı} diriltilme adından önce gelir. Bu olumsuzluk dizisi iki eylem adını önde tutup büyüklüklerini ölçmeye hazırlar. Ardından {ar:إِلَّا, tr:illā, gloss:ancak} kıyası açar: {ar:كَ, tr:ka, gloss:gibi} edatı, ilgi durumu biçimindeki {ar:نَفْسٍۢ وَٰحِدَةٍ, tr:nafsin wāḥidatin, gloss:bir tek can} öbeğini iki eylemin ortak standardı yapar. Kısa öbek karşılaştırmayı tamamlar; ikinci, söylenmemiş bir cümle varsaymaya gerek bırakmaz.

Yaratılma ve diriltilme sonlu anlatı fiilleriyle değil, eylemleri adlandıran iki mastarla söylenir: {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ve {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz}. İki mastar da özne konumunda ve merfûʿ biçimdedir; diriltme, yaratılmanın yanındaki eşlenik ikinci özne olarak aynı kıyasa girer. İkisinin de sonundaki çoğul iyelik eki eylemleri muhataplara bağlar; diriltilecek olanların yine onlar olduğu belirginleşir. Bu ilişki onları diriltme eyleminin muhatapları olarak, kendi kendine harekete geçen faillerden ayrı bir konuma yerleştirir. Bu alıcı okuması bağlamdan gelir: iyelik eki edilgen fiil biçimi kurmaz ve faili adlandırmaz. Yinelenen ekler bu eşleşmeyi pekiştirir. Aradaki {ar:وَ, tr:wa, gloss:ve} ikinci eylemi ilkinin yanına ekler; yaratılmadan ölüm sonrasındaki dönüşe uzanan bir insan hayatı yayı da bu sıradan duyulur.

Yaratma anlamını taşıyan {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} sözü, var etmenin yanı sıra sözlükte işe başlamadan önce sınırları belirlemeye ve dış biçimi tamamlayıp görünür kılmaya da açılır. Yanındaki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} eylemi ve {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} standardı bu anlamları yaratılmanın çevresinde toplar: başlangıcı ölçülü, biçimi tamamlanmış bir oluşum duyulur. Bu yankı, olağan yaratma anlamını ölçülü oluşum imgesiyle genişletir; ayetin söz diziminde ayrı bir ölçme işlemi ya da ölçen bir fail yer almaz. Mastar ile çoğul ekinin birleştiği yakın ses sınırı da kulağa çarpabilir; başka bir okuyuş verilmediğinden bu ses ayrıntısı sözcüğün çözümlemesini değiştirmeden ölçülü oluşum imgesini renklendirir.

Diriltme anlamındaki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} sözü, sözlükte dışarıdaki bir etkenin durgun olanı yeniden faal kılmasını da anlatır. {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ve {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ölçüsü bu kullanımı diriltmeye yaklaştırır: ölümden sonra kaldırılma, durgunluktan etkinliğe geçiş gibi duyulur. Böylece eylemin adı ve olağan anlamı kalırken kıyasın içindeki hareket belirginleşir.

Aynı {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} adının ayrı bir sözlük dalı, bir katılımcıyı ihtiyaç, görev, yön ya da hedef doğrultusunda bir yere yollamaktır. Ölçüsü önceden belirlenmiş {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ile {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} standardı, çokların tek bir yöne sevk edilmesi imgesini tetikler. Bu, durgunluktan uyanma yankısından ayrı bir gönderme imgesidir; belirli bir gönderici, görev ya da hedef adı verilmediği için yönelmiş hareket olarak kalır ve diriltilme eylemi cümlenin olağan anlamını taşımayı sürdürür.

Karşılaştırmanın standardı olan {ar:نَفْسٍۢ, tr:nafsin, gloss:bir can}, soyut bir sayıdan fazlasıdır: bedene hayat veren, bedenden ayrılması ölüm sayılan canlı kendiliği ve tek tek insanı anlatabilir. {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız}, {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} ve {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} sıfatı bu yaşayan kişi anlamını öne çıkarır; kıyasın odağı da beden parçalarının kuruluşundan çok hayat taşıyan kişidir. Sözcük kişinin bütün öz varlığını, bizzat kendisini de gösterebildiğinden, benzetme parçaların toplamından daha geniş, kişiye dönük bir ölçü sunar. Belirsiz biçimi belirli bir kişiyi seçmez: ölçü, herkesin anlayabileceği ve yeniden uygulanabileceği bir insan birimi olarak kalır.

{ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} biçimi, {ar:نَفْسٍۢ, tr:nafsin, gloss:bir can} ismiyle dişil tekil uyum kurar; sayı dilbilgisel olarak birdir, uyum da biyolojik cinsiyeti değil bu dilbilgisel ilişkiyi gösterir. Benzetmenin sonunda gelen bu sözcük standardı ilahî niteliklere geçmeden tamamlar. Belirsiz biçimi adı konmuş bir kişiyi değil, saymanın başlangıcı ve ilk birimi olan bir sayısını duyurur. Buradaki “bir”, benzetmenin sayısal ölçüsüdür; {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} hakkında ilahî teklik ya da eşsizlik yüklemi değildir. Onu sayısal ölçü yapan {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} sözcüğü, {ar:كَ, tr:ka, gloss:gibi} benzetmesi ve {ar:نَفْسٍۢ, tr:nafsin, gloss:bir can} adının birlikteliğidir.

{ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} sözü burada çokluğu bir kişiye dönüştürmek yerine, birden çok şeyi ortak bir bakımdan tek bütün sayma olanağı da taşır. {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ve {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} mastarlarının aynı kıyas içinde buluşması bu ortak yönü etkinleştirir: işlemin ölçüsü birdir, muhataplar ayrı ve çoğuldur. Bu ölçekte bir canı var etmek ve onu yeniden etkinleştirmek, çoklara da aynı ölçüyle yönelen eylemin düşünsel karşılığı olur. Böylece sözcüklerin olağan anlamı korunurken kıyas yalnızca “çoğul bir topluluk” demekten çıkar, tek insan ölçüsünde gerçekleşen kudretin çoklara erişmesini de duyurur.

## İşitmenin ve Görmenin Açtığı Kapanış

Ölçü tamamlanınca {ar:إِنَّ, tr:inna, gloss:şüphesiz} ile yeni ve vurgulu bir yargı başlar. İlk cümle yaratılma ve diriltilmeyi adlandırır, fakat failini orada bir adla belirtmez; şimdi {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adı görünür. Dilbilgisel olarak Allah, {ar:إِنَّ, tr:inna, gloss:şüphesiz} edatının ardından gelen ad öğesidir; {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} ve {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} ona bağlanan iki yüklemdir. Eylemlerin kaynağı da okuyucunun zihninde bu kapanışta belirginleşir. Duyuların tek özne altında toplanması, ölçek kıyasına algı bakımından dayanak verir; bu ilişki ayetin kendi cümle düzeninden doğar.

Buradaki {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adı Yaratıcıyı başkalarından ayıran belirli özel addır. Bu ad için aktarılan bir köken açıklaması, tapınılan varlığı bildiren genel addan bir sesin düşmesini ve belirleyici unsurun eklenmesini anlatır. İşitme ile görmenin açıkça bu ada bağlanması, bu köken açıklamasından tapınmayla ilgili hafif bir gölgeyi de duyurabilir. Köken gölgesi yakarış, şaşma sözü ya da ant kalıbı oluşturmaz; ad, iki yüklemin bağlandığı özel ad işlevini korurken tapınma nüansını hafifçe taşır.

{ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} önce sesi kulakla fark edip işitsel algıya dönüştürür. Yanındaki {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} ikinci duyu olarak bu alanı dikkatini sese veren bir dinlemeye doğru genişletebilir; böylece edilgin duymaya ince bir amaçlılık tonu katılır. Cümle belirli bir ses, söz, cevap ya da buyruk seçmez; dinleme gölgesi çift algılı kapanışın içinde kalır. {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} biçimi tek seferlik bir duymadan ziyade süren ve kapsamlı bir işitme niteliği de taşır. Sonraki görme yüklemi bu sürekliliği belirginleştirir; iki sıfat birlikte, ölçek savının ardından iki duyuya yayılan bir fark ediş sunar.

Son yüklem olan {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören}, belirli bir nesneye yönelmiş anlık bakıştan daha kapsamlı ve süren bir görme niteliği olarak da duyulur. Sözlükte aynı anlam alanı, gözle görmenin yanında kalbe nüfuz eden kavrayışı ve doğrulanmış anlayışı taşır. {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} sıfatı ile {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ölçüsü bu iç kavrayışı kişilere yöneltir: çokluk yalnız sayı olarak değil, tek tek tanınabilir kişiler olarak belirir. Bu açılım olağan görme anlamını korur; cümle belirli bir görülen nesne bildirmeden her canın fark edilişini sezdirir.

Yüklemlerin sırası bu algı çizgisini kulağa da taşır: önce {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} işitme alanını açar, son sözcük {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} ayeti görmeyle tamamlar. İki sıfatın ortak ses bitişi ve ölçülü ritmi dengeli bir iniş kurar. Son yüklem yeni bir yargı başlatmaz; aynı özneye bağlı duyu çiftini kapatır ve son vuruşta görsel fark edişi öne çıkarır.

Görme sözü {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} için daha uzak bir sözlük alanı da nesnenin kalın dış yanını, kenarını, yüzeyini ya da yönünü anlatır. Yaratmayı adlandıran {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} tamamlanan ve görünür olan biçimi düşündürdüğünde, bu kenar anlamı biçimin dış çizgisini de algılanır kılar. Böylece olağan görme niteliğinin çevresine sınırları seçen bir malzeme görüntüsü eklenir.

Aynı görme kökünün başka bir sözlük kullanımı, deri, kumaş ya da kap parçalarını ek yerinden dikerek birleştirmektir. Tamamlanmış biçim anlamındaki {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} ile durgun olanı yeniden etkinleştiren {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} bu malzeme dalına ayrı katkı verir: dikiş yerinde birleştirilen parçalar biçimi tamamlar, ardından oluşan şey yeniden işler hâle gelir. Ek yeri böylece yaratma ile diriltme sırasını uzak bir onarım imgesi gibi duyurur; ayet gerçek beden onarımı sahnesi kurmadan, bu sözlük ayrıntısı görme niteliğinin yanına parçaların birleşip yeniden işe yaradığı bir malzeme görüntüsü ekler.

## Çokluğun Erişimi, Kişinin Ayrılığı

Bu ölçünün çoklara nasıl eriştiği, hemen önceki ayetteki bitimsizlik imgesiyle de düşünülebilir. (31:27)’de deniz yazı aracını sürekli besler; {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:onu sürekli besler} sözü bu yenilenen kaynağı, {ar:مَا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mā nafidat kalimātu llāh, gloss:Allah’ın sözleri tükenmedi} ifadesi de sözlerin tükenmeyişini anlatır. Bu bağlam, odaktaki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} eylemini durgun olanın yeniden etkinleşmesi ve {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} sözünü çokları ortak ölçüde tutmasıyla buluşturur: sayı artsa da eylemin kudreti eksilmez. (31:27) kendi başına ayrı bir kudret imgesi olarak da durur; iki ayetin teması komşuluklarının kurduğu bağlamsal okumadır. Böyle okunduğunda, tükenmeyen kaynak imgesi 31:28’deki tek-can ölçüsünü çoklara ulaşan ama sayıyla azalmayan bir eylem gibi duyurur.

Kozmik ölçeğe başka bir açı da (31:29)’da belirir: gece ile gündüz birbirine girer, karanlık birikir, aydınlık açılır, güneşle ay belirlenmiş süreye dek akar. Bu döngü, odaktaki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} sözünün durgun olanı dışarıdan bir etkenle yeniden etkinleştirmesiyle yan yana gelince, diriltme çevrim içinde tek bir yeniden etkinleşme atımı gibi duyulur. (31:29)’daki {ar:ٱلنَّهَارَ, tr:al-nahāra, gloss:gündüz} gündüzü adlandırır; odaktaki {ar:نَفْسٍۢ, tr:nafsin, gloss:can} ise olağan anlamıyla kişiyi ve insan ölçüsünü korur. Bu iki sözcük ortak kökten gelmez: temas sözcükler arasında değil, (31:29)’un gece-gündüz geçişi, açılan ışığı ve belirlenmiş süreyi bir araya getiren zaman çizgisindedir. Bu yüzden doğuşa benzeyen yeniden etkinleşme analojik ve keşifseldir; gündüz odağın diriltme sözüne dönüşmeden, döngüsel ritim diriltme imgesini genişletir.

Zaman çevriminden ayrı bir somut görüntü (31:32)’deki deniz sahnesidir. Dalga insanları örter ve birbirine karışan hareket içinde seçilmez kılar: {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örttü} ve {ar:مَّوْجٌۭ, tr:mawjun, gloss:dalga} bu örtülme ile karışmayı taşır. Ardından {ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā al-barri, gloss:onları karaya kurtardı} ifadesi onları ayırıp güvenli, sabit yere çıkarır; {ar:ٱلْبَرِّ, tr:al-barri, gloss:kara} örtülü ve hareketli denizden farklı zemini verir. Bu örtülme ile yeniden seçilebilir olma sırası, 31:28’deki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} ve {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ölçüsünün çoklara erişmesini görünür kılan bir kurtuluş benzetmesi sunar.

Bu deniz krizinin kendi içindeki sıkıntı, {ar:نَفْسٍۢ, tr:nafsin, gloss:kişi} sözüne bağlı ayrı bir sözlük dalını da etkinleştirir: bu kök, sıkıntı içindeki kişinin yükünü hafifletip rahatlatmayı da anlatabilir. Dalganın altında kalma ile kurtarılma (31:32), önceden var olan sıkıntıyı ve ardından gelen ferahlığı sahne içinde sağlar; böylece odaktaki {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} kişi ölçüsüne ortak bir rahatlama imgesi eklenir. Bu bağlam (31:32)’nin denizden kurtuluş anlatısı olarak kalırken 31:28’deki eylemin seçilmez durumdaki çoklara erişmesini düşünmeye yardım eder.

Deniz sahnesindeki ayırt edilme görüntüsünden ayrı olarak, (31:33) en yakın aile bağında bile kişilerin birbirinin yerine geçemeyişine bakar. Âyet, {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lā yajzī wālidun ʿan waladihi wa-lā mawlūdun huwa jāzin ʿan wālidihi shayʾan, gloss:ebeveyn evladı adına, evlat da ebeveyn adına hiçbir şey yapamaz} diyerek ebeveyn ile evladı iki yönde de ayrı ayrı anar. Aynı karşılık verme fiilinin daha keşifçi bir sözlük yankısı kesip ayırmaktır; karşılıklı tekrar ve {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ortak ölçü bu çağrışımı kişiler arasındaki sınır çizgisine taşır. En yakın soy bağı bile diğerinin yerine geçirmez. (31:33)’ün doğrudan konusu hesap günündeki ebeveyn-evlat ilişkisidir; bu sınırın 31:28’deki kıyasa uzanması bağlamsal bir okumadır ve ortak eylemin kişileri birleştirmediğini belirginleştirir.

(31:34) aynı ayrılığı bu kez her kişinin geleceği üzerinden kurar: her bir {ar:نَفْسٌۭ, tr:nafsun, gloss:kişi} yarın ne kazanacağını ve nerede öleceğini bilmez; Allah ise her şeyi ve iç yüzünü bilir. Ayrı gelecekler ve ölüm yerleri, 31:28’deki çoğul yaratılma ile diriltilmenin {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ölçüsüne sığarken kişisel hayat çizgilerinin silinmediğini gösterir. Odaktaki {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} ve {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} bu ayrılığı algı bakımından da açar: işitme her kişinin sesine, görme ve iç kavrayış her birinin ayrı varlığına yönelmiş gibi duyulur. (31:34)’ün kişisel bilgi sahnesi diriltmenin işleyişini tarif etmez; bu bağlantı, ortak ölçü içinde her bir kişinin ayrı ayrı bilinebilmesini aydınlatır.

## Daha Geniş Ölçekler

Kişisel ayrıntıyı koruyan bu ölçüye daha geniş bir yaratılış sahnesinden de bakılabilir. (31:10)’da önce göklerin ve yerin yaratılması, sonra canlıların yeryüzüne yayılması anlatılır. Odaktaki {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} bu sahneyle birlikte daha geniş bir yaratılmış dünya ufkuna açılır; {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} sözünün durgun olanı harekete geçirme kullanımı da yayılmış hayatın dönüşü gibi duyulabilir. {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} bu çokluğu ortak bir ölçüde toplar. Dağılmış canlıların bir eylemle geri dönüşü, 31:28’de toplama fiili söylenmemesi ve dağılma-diriltme ses benzerliğinin tesadüf olabilmesi nedeniyle bağlamsal bir imge olarak kalır. Böylece (31:10)’un gökleri, yeri ve canlıların yayılışını kapsayan yaratılış sahnesi, odaktaki tek ölçüye dağılma ile dönüşü birlikte düşündüren bir çerçeve sunar.

Kozmik ölçüden insan bedeninin zamanına geçince (31:14)’te gebelik henüz görünür olmayan oluşumu, sütten ayrılma ise ayrı yaşama geçişi gösterir. Odaktaki {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız}, yaşayan kendilik anlamındaki {ar:نَفْسٍۢ, tr:nafsin, gloss:can}, {ar:وَٰحِدَةٍ, tr:wāḥidatin, gloss:bir} ve {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} bu sırayla buluşunca ilk belirişten sonraki bir yeniden beliriş duyulur. Arapçada aynı sözcüğün kadının doğurmasını ve doğum sonrasındaki kanamalı dönemi karşılayan başka bir kullanımı da vardır; odaktaki dişil biçim bu kullanıma biçimsel yakınlık sağlar, tek başına o anlamı seçmez. (31:14)’teki gebelik ve sütten ayrılma sahnesi bu olasılığı etkinleştirerek tek-can ölçüsünü sayısal birimden bedenlenmiş belirme örüntüsüne genişletir. (31:14) ebeveyn sorumluluğu sahnesi olarak da okunabilir; iki ayetin de diriltmeyi doğum diye adlandırmadığı bu bağlamda, odaktaki eylem olağan diriltme anlamını korurken yenilenmiş bir beliriş gibi duyulur.

Gizli oluşumdan daha küçük bir ölçeğe geçince, (31:16)’da hardal tanesi ağırlığınca bir şeyin kaya, gökler ya da yeryüzünde saklı kalıp sonunda getirilmesi anlatılır. {ar:مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ, tr:mithqāla ḥabbatin min khardalin, gloss:hardal tanesi ağırlığınca} tam ve bilinen bir ağırlığı, belirsiz bir yığın yerine ölçüsü belirli bir parçayı gösterir. Bu kesin kütle, odaktaki {ar:خَلْقُكُمْ, tr:ḫalqukum, gloss:sizin yaratılmanız} için ölçü ve sınır yankısı açar; ancak bu isim biçiminin tek başına zorladığı anlam değil, (31:16)’nın ağırlık ayrıntısının etkinleştirdiği bağlamsal bir çağrışımdır. Böylece kıyasın ölçülü oluşum imgesi en küçük parçaya dek taşınır.

(31:16)’daki tane saklı kaldığı yerden getirildiğinde, odaktaki {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} olağan erişimin ötesindeki gizliliğe temas eder. Aynı tanenin saklıyken kimliğini koruması, {ar:نَفْسٍۢ, tr:nafsin, gloss:can} sözüyle taşınan bütün benlik anlamını da belirginleştirir: geri dönen kişi adsız bir örnek değil, kendi öz varlığıyla belirli biridir. (31:16)’nın gizli işlerin bilinmesi bağlamı, {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} için gözle görmenin yanına iç yüzü kavrayan anlayışı ekler. Bu bağlam ahlaki hesap ve saklı olanın bilinmesidir; tane diriltmenin işleyişini açıklamadan, en ince gizlilikte bile kişinin tanınabilir kaldığını düşündürerek 31:28’deki kişi ölçüsünü keskinleştirir.

(31:16)’daki küçücük tane gizliyken de aynı tane kalır; başka bir ayette kişiye özgü ayrıntı daha elle tutulur biçimde belirir. (75:4)’te ölümden sonra yeniden düzenlenen {ar:بَنَانَهُ, tr:banānahu, gloss:parmak uçları}, {ar:كَ نَفْسٍۢ وَٰحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:bir tek can gibi} ölçüsünü tek bedenin ayrıntısına taşır. Parmak ucu her bedene özgü olduğundan, ortak eylem ölçüsünün kişileri birbirinin yerine koymadığını somutlaştırır: geri dönen kişi adsız bir örnek değil, kendi bütünlüğünü taşıyan kişidir.

Beden ayrıntısından algının kişisel sorumluluğuna geçen (17:36)’da {ar:السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ, tr:as-samʿa wa-l-baṣara wa-l-fuʾāda, gloss:işitme, görme ve yürek} yetileri kişiye hesap vereceği alanlar olarak bağlanır. Bu bağlam, 31:28’deki {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} niteliğinin her kişinin duyduğu ayrıntıya, {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} niteliğinin de yüreğe nüfuz eden kavrayışa açılmasını destekler. Odak ayetin kendi kapanışı iki olağan duyu niteliğini bildirir; kişisel sorumluluk ve yetilerin hesabı (17:36)’nın bağlamından gelir. Böylece ortak ölçünün altında tek tek duyulan ve görülen kişiler belirir.

(17:36)’da kişisel algı sorumlulukla görünürken (31:7) insanın bu alımlamayı reddedebileceğini gösterir: okunan işaretlerden yüz çeviren dinleyici sanki duymamış gibi davranır. İnsan işitilen anlamı geri çevirebilir; (31:28)’deki {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} ise erişimi sürdüren işitme, {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} da kaçınmanın diriltilen kişiyi tanınmaz kılmadığı içgörü gibi duyulur. (31:7) ile (31:28) arasında bu nedenle erişim bakımından bir karşıtlık kurulabilir, ancak (31:28)’in önceki dinleyiciye doğrudan cevap verdiği söylenemez; tematik yankı da olasılığını korur. Bu karşıtlık itaat zorunluluğu getirmeden, işiten-gören çiftinin her kişiye açık kalışını belirginleştirir.

Reddedilen işaretten farklı bir kişisel ses (58:1)’de duyulur: bir kadın eşi hakkındaki çekişmesini Allah’a açar, konuşmalarının işitildiği bildirilir ve ardından {ar:إِنَّ اللَّهَ سَمِيعٌ بَصِيرٌ, tr:inna llāha samīʿun baṣīrun, gloss:Allah işitendir, görendir} sözü gelir. Bu sahne, (31:28)’deki {ar:سَمِيعٌۢ, tr:samīʿun, gloss:işiten} niteliğinin geniş bir kıyas içindeki kalabalığa değil, tek bir kişinin sesine de ulaşabildiğini gösterir; aynı formüldeki {ar:بَصِيرٌ, tr:baṣīrun, gloss:gören} yüklemi kapanışın çiftini sürdürür. Kadının sözleri (31:28)’in sahnesi değildir; (58:1)’in sunduğu tekil ses, ortak ölçünün içinde bireysel bir sesin de kaybolmadığını duyurur.

</source_prose>
