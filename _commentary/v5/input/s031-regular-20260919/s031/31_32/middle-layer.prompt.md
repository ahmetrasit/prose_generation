# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:32**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.middle.claims.json`

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
- Refer to source paragraphs as `31:32 ¶N`.

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

`(31:32 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:32",
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
        "citation": "(31:32 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_32/31_32.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_32/31_32.middle.claims.json \
  --ayah-ref 31:32
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_32/31_32.prose.editorial.tr.md`

<source_prose>
## Dalganın örttüğü sahne

Başlangıçtaki {ar:وَإِذَا, tr:wa-idhā, gloss:ve ne zaman} önceki söz akışını yeni bir kriz sahnesine bağlar. {ar:إِذَا, tr:idhā, gloss:ne zaman} dalga bastığında çağrının beklendiği anı açar; ardından gelen {ar:لَمَّا, tr:lammā, gloss:olduğunda} kurtuluşun gerçekleştiği eşiği gösterir. Böylece bu ayetin kendi akışı—kuşatan dalga, çağrı, karaya çıkarılış ve kurtuluştan sonra farklılaşan karşılıklar—belirginleşir; anlatı önceki sahneyi yeniden kurmadan onun içinden ilerler. Bu zaman çizgisi tek bir olayın ayette nasıl geliştiğini gösterir; krizin kaç kez yaşandığına dair bir sayı vermez.

Belirsiz tekil {ar:مَوْجٌۭ, tr:mawjun, gloss:bir dalga kütlesi} sahneyi başlatan tek bir kabarıştır. Onu özne alan {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örttü} fiilinde örtücü kuvvet tek, dalganın kapladığı grup çoğuldur; kurtuluş anlatısındaki aynı çoğul grup daha sonra yeniden görünür. Bu tek dalganın çalkantısı, örtme fiili ve {ar:كَـ, tr:ka, gloss:gibi} benzetmesiyle birleşince olağan hareketi kesen düzensiz bir baskı duyulur. Benzetme hemen ardından gelen belirli çoğul {ar:ٱلظُّلَلِ, tr:al-ẓulal, gloss:saçaklar ve örtüler} adına bağlanır: dalga gerçek bir su kütlesi olarak kalırken üstten kapanan bir örtüye benzer. Böylece tehdit yolcuları çevrelediği gibi yukarıdan da kapanır; saçak benzetmesi bu ilk kuşatma eşiğinde kalır, kıyıdaki kurtuluş ayrı bir hareket olarak kurulur. Belirli bir fırtınanın adı verilmeden fiziksel deniz tehlikesi öne çıkar.

{ar:ٱلظُّلَلِ, tr:al-ẓulal, gloss:saçaklar ve örtüler} adının gölgeleyen yanı, {ar:مَوْجٌۭ, tr:mawjun, gloss:dalga} ve grubu örten {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örttü} ile birleşince denizin ışığını da keser. 24:40’taki dalga üstüne dalga ve kat kat karanlıklar, bu üstten örtüyü deniz içindeki daha yoğun bir kuşatmaya genişletir. 31:29’da geceyle gündüzün birbirine sokulması aynı gölgeye gece tonu verir; bu renk, yerel sahnenin ayrı bir gece tasviri değil, komşu âyetten gelen bir nüanstır. Örtülen su karşısında karaya varışın suyun erişemediği yüksek zemin gibi duyulması da deniz-kara karşıtlığının açtığı ayrı bir benzetmedir; yükseklik {ar:الْبَرِّ, tr:al-barri, gloss:kara} sözcüğünün anlamı değil, suyla kıyının ilişkisinden doğar. 31:33’te yakınların hesap gününde birbirine yetememesi, sahnenin sonrasına sınırlı bir hesap ufku ekler; bu bağlam deniz örtüsünü hesap günüyle özdeşleştirmek yerine iki alanı ayrı tutar.

31:31’in kısa deniz tasvirinde gemi ilahî lütufla yol alır; 31:32’de aynı deniz üstten kapanan, denetim dışı bir tehdide döner. Önceki tasvirin burada yalnızca özet düzeyinde bulunması, bu karşıtlığın ihtiyatla okunmasını gerektirir. 31:31 gemi, işaret, sabır ve şükür bağını kurarken, odaktaki {ar:مَوْجٌۭ, tr:mawjun, gloss:dalga} sabrı somut bir güçlüğe, karaya eriş de şükrün sınanacağı sonraki evreye taşır. Ahlaki ağırlık denize değil, kurtulanların farklı karşılıklarına aittir; fiziksel tehlike ve şükür sınaması aynı deniz akışının ayrı aşamalarıdır.

## Örtünün altındaki yöneliş

Dalga üzerlerine kapanınca çoğul geçmiş fiil {ar:دَعَوُا, tr:daʿawū, gloss:çağırdılar} yolcuları seslenen özne yapar. Doğrudan nesne olan {ar:ٱللَّهَ, tr:Allāha, gloss:Allah'ı} çağrının muhatabını açıkça adlandırır; kriz tepkisi böylece adı belli birine yönelen sesli bir eylem olur. Fiilin ses ve sözle muhatabı konuşana yöneltme kullanımı, Allah’ın adı ve ardından gelen yönelişle birleşince çağrıyı o ilahî muhatapta toplar. Bu yerel sözdizimi muhatabı belirler; adın tartışmalı türeyişi hakkında ayrıca bir çıkarım sağlamaz.

Allah’a dönen {ar:لَهُ, tr:lahu, gloss:O'nun için, O'na ya da O'na ait} sözü, nesnesi olan {ar:ٱلدِّينَ, tr:al-dīna, gloss:din ve bağlılık düzeni} söylenmeden önce gelir; bağlılığın yönü böylece erkenden duyulur. Yerel biçim “O’nun için”, “O’na” ya da “O’na ait” ilişkilerine açıktır ve zamir bu yön ilişkisini taşır. Çağrı yapanların hâlini anlatan mansub durumdaki IV. bâb etken ortaç {ar:مُخْلِصِينَ, tr:mukhliṣīna, gloss:bağlılığı arındıranlar}, dini Allah’a özgü kılmayı seslenişle eşzamanlı verir. Bu ortaç çağrı anındaki yönelişi niteler; kurtuluştan sonraki tutum için ayrı bir güvence kurmaz.

{ar:مُخْلِصِينَ, tr:mukhliṣīna, gloss:bağlılığı arındıranlar} inanç ve kulluğu yalnız Allah’a yöneltir; aynı sözcük ailesinin karışımı giderme kullanımı da {ar:لَهُ, tr:lahu, gloss:O'na yönelme} ile {ar:ٱلدِّينَ, tr:al-dīna, gloss:din ve bağlılık düzeni} nesnesinin birlikteliğinde açılır. Böylece kriz içindeki bağlılık, yönelişteki bulanıklığın giderilmesi gibi duyulur; imge bağlılık ilişkisinin yönünü anlatır, fiziksel bir kirleticiyi değil. 98:5’te kullukla dini Allah’a özgü kılma, 40:65’te ise O’na çağırma ve dini özgüleme aynı yapıda birleşir; bu iki âyet buradaki arındırma okumasına ayrı dilsel dayanaklar verir.

{ar:مُخْلِصِينَ, tr:mukhliṣīna, gloss:bağlılığı arındıranlar} biçiminin bağdan sıyrılıp kurtulma yankısı, aynı grubun dışarıdaki kurtarılışıyla iç yönelişini yan yana getirir: önce {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örttü} dalga onları kuşatır, sonra {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} aynı grubu tehlikeden çıkarır. Bu sıra, iç bağlılığın tek muhataba yönelmesini dışarıdaki ayrılışın ön imgesi gibi duyurur; metinde arındırma ve bedensel kurtarılma iki ayrı eylemdir. {ar:مَوْجٌۭ, tr:mawjun, gloss:dalganın} baskısı, {ar:دَعَوُا, tr:daʿawū, gloss:çağırdılar} eylemi, {ar:ٱللَّهَ, tr:Allāha, gloss:Allah'ı} adı, {ar:لَهُ, tr:lahu, gloss:O'na yöneliş} yönü ve {ar:ٱلدِّينَ, tr:al-dīna, gloss:din} nesnesi birlikte krizi korkuyla söylenen duanın ötesinde, bölünmüş bağlılığı o an için tek muhataba süzen bir eşik olarak gösterir. Bu yöneliş çağrı anını niteler; karaya çıktıktan sonraki davranış hakkında hüküm vermez.

Buradaki {ar:ٱلدِّينَ, tr:al-dīna, gloss:bağlılık ve yükümlülük düzeni}, tanınmış bir bağlılık ve yükümlülük düzeni olarak kişisel duygudan geniştir. Allah’ın adı, O’na yöneliş ve dalganın baskısı buyruğa uyma ile boyun eğmeyi kriz anında öne çıkarır. 31:22’de Allah’a teslimiyetin iyi davranışla birlikte sunulması daha yerleşik bir bağlılık örneği verir; acil çağrı bu örnekle karşılaştırılırken kurtulanların kıyıdan sonra aynı yönelişi sürdürdüğü sonucu çıkmaz.

Din sözü ayrıca hesap ve karşılık ufkunu açar: 31:23’te Allah’a dönüş, 31:33’te yakınların hesap gününde birbirine yardım edemeyişi bağlılığa hesap boyutu ekler. Bu çevre, yerel anlamı yalnızca ahiret yargısına indirgemeden genişletir. Sözcüğün borç verip geri ödeme yükümlülüğü doğurma kullanımı, kurtarılıştan sonra gelen nankörlükle buluşarak alınmış iyiliğe karşılık verme borcunu hissettirir; bu çağrışım ahlaki karşılıklılık alanındadır, kurtuluşu mali bir işlem olarak sunmaz.

Bu belirli muhataba yöneliş, daha geniş söz akışındaki çağrı çekişmesiyle de yankılanır. 31:21’de Allah’ın indirdiğine uyma çağrısı ataların yolunu izleme cevabıyla ve şeytanın azaba çağırmasıyla karşılaşır; 31:30’da Allah’ın gerçek oluşu, O’ndan başkasına yöneltilen çağrının asılsızlığıyla karşı karşıya gelir. Denizdeki {ar:دَعَوُا, tr:daʿawū, gloss:çağırdılar} eylemi {ar:ٱللَّهَ, tr:Allāha, gloss:Allah'ı} adlandırırken {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:mukhliṣīna lahu al-dīna, gloss:dini yalnız O'na özgü kılarak} sözü yönelişi tekleştirir; basınç altındaki çağrı, bu daha geniş karşıtlık içinde geçici bir hizalanma kurar. Bu çevre âyetler gemide belirli bir rakip çağıranın bulunduğunu ya da kıyıdaki sonraki tutumun bu çekişmeden kaynaklandığını göstermez.

## Kurtuluş ve kıyı

İlk {ar:فَـ, tr:fa, gloss:bunun üzerine}, çağrıdan kurtuluş anlatısına geçişi kurar ve kurtuluşu sonraki anlatı adımı olarak sunar; bu bağlaç nedenin ayrıntısını belirtmez. {ar:لَمَّا, tr:lammā, gloss:olunca} tamamlanmış kurtuluşu eşiğe koyar; farklı karşılıklar dalga sırasında değil, güvenliğe geçişten sonra belirir. {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} fiilindeki çoğul zamir, {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örten} dalganın kapladığı aynı gruba döner; önceki çağrı Allah’ı kurtarıcı fail olarak anlaşılır kılar. Böylece anlatı, korku ve kırılganlığın tümüyle silindiğini ileri sürmeden, tehlikeden çıkarılanların yanıtlarını kıyıda görünür kılar.

{ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} fiili, grubu kuşatan zararlı durumdan çıkarılmasını bildirir; yön bildiren {ar:إِلَى, tr:ilā, gloss:-e doğru} edatı bu kurtuluşu {ar:الْبَرِّ, tr:al-barri, gloss:denizin karşısındaki kara} varışında tamamlar. Dolayısıyla hareket hem dalgadan uzaklaşmayı hem karaya erişi içerir. Bu bedenî çıkarılış dış dünyada, {ar:مُخْلِصِينَ, tr:mukhliṣīna, gloss:bağlılığı arındıranlar}daki arınma ise iç bağlılık düzleminde yer alır; ikisi aynı kriz dizisinde birbirini aydınlatan ayrı süreçlerdir.

Buradaki {ar:الْبَرِّ, tr:al-barri, gloss:kara} somut kıyı ve denizin karşısındaki kuru zemindir; adın kendisi ıssız çöl ya da yüksek yer gerektirmez. Aynı kökün iyilik ve doğruluk alanı ise ardından beliren {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçüsünü koruyan}, {ar:خَتَّارٍ, tr:khattārin, gloss:güveni bozan} ve {ar:كَفُورٍ, tr:kafūrin, gloss:nankör} karşılıklarıyla temas ederek güvenliğin ahlaki seçimi görünür kıldığı bir zemin düşündürür; coğrafi anlam korunur. Dalga ile kara arasındaki karşıtlık kıyıyı suyun erişemediği yüksek yer gibi de duyurabilir, ancak bu yükseklik varış yerinin açtığı imgedir, kurtarma fiilinin anlamı değil.

Kıyıya varış gerçek bir rahatlamadır; çevredeki zaman ve hesap söylemi onu son durak yapmaz. 31:23 dönüşü, 31:24 kısa yararlanmanın ardından gelen zorlamayı, 31:29 belirlenmiş süreyi hatırlatır. 31:33’ün dünya hayatının aldatmasına karşı uyarısı, güvene dönüşten sonra {ar:خَتَّارٍ, tr:khattārin, gloss:güveni bozan} biçiminde sadakati bozma veya {ar:كَفُورٍ, tr:kafūrin, gloss:nankör} biçiminde nimetin değerini örtme ihtimalini kıyı sahnesine taşır; kıyının kendisi aldatıcı değildir. 31:31’deki nimet ve işaretlerle 31:22’de teslimiyetin iyi davranışla birleşmesi yan yana düşünüldüğünde, {ar:الْبَرِّ, tr:al-barri, gloss:kara} sonraki karşılığın açığa çıkacağı bir alan olur. {ar:مِنْهُمْ, tr:minhum, gloss:onlardan} diye ayrılan {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü kişi} de bu farklılaşmayı gösterir; bu karşılaştırma kurtulanların hepsine aynı sonucu yüklemez.

31:34’teki {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} sıkıntıdakine yardım ve ferahlık getiren suyu anarken, buradaki dalga yolcuları kuşatan tehlikeyi gösterir; su imgesi bu iki sahnede farklı işler görür. {ar:دَعَوُا, tr:daʿawū, gloss:seslenip çağırdılar} çağrısı ile {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} kurtarışı yakarış ve ferahlığı aynı kriz çizgisinde buluşturur. Bu paralellik yağmurun duayla meydana geldiği yönünde bir neden bağı kurmaz ve iki su imgesini tek imgeye dönüştürmez.

## Karada ayrışan ölçü

Kurtuluşu izleyen ikinci {ar:فَـ, tr:fa, gloss:bunun üzerine}, {ar:مِنْهُمْ, tr:minhum, gloss:onlardan} sözüyle kurtarılanların içinden bir karşılığı seçer. Ardından gelen tekil ve belirsiz {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçüsünü koruyan} bir tutumu bu alt grupta görünür kılar. Ayet bu kişinin davranışını adlandırır; adı verilmeyenlerin her birinin ne yaptığını açıklamaz.

{ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü davranan} sözcüğünün olağan anlamı karşıt aşırılıklar arasında ölçü tutturmaktır. Kriz çağrısının yoğunluğu ve ardından gelen {ar:خَتَّارٍ, tr:khattārin, gloss:güveni tekrar tekrar bozan} profili yanında bu kişi, o anki yoğunluğu sürdürmeyen ve güven ihlaline indirgenmeyen ara bir tutumla belirir. Daha sonra gelen {ar:كُلُّ, tr:kullu, gloss:her biri ve tümü}, son ahlaki tipin bütün örneklerini kapsar; {ar:مِنْهُمْ, tr:minhum, gloss:onlardan} ile ayrılan ölçülü kişi bu sınıfa girmez. Ayetin burada verdiği, davranışa ilişkin bir ölçü tarifidir; kişi hakkında tam bir övgü ya da mahkûmiyet hükmü değildir.

Aynı {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü kişi} biçiminin VIII. bâbdaki etken ortaç olarak hedefe yönelme ve düzgün bir çizgiyi izleme çağrışımı da vardır. Kurtuluşun somut hedefi olan {ar:الْبَرِّ, tr:al-barri, gloss:kara}, değişen zeminde yönünü koruyan biri imgesine dayanak verir; sözcüğün ölçülülük anlamı da sürer. 16:9 doğru yolu eğrilen yollardan ayırır, 31:19 yürüyüşte ölçüyü buyurur, 35:32 ise farklı ahlaki karşılıklar içindeki ölçülü profili anar. Luqmân sûresinin kendi akışında 31:3’ün hidayet ve rahmeti, 31:6’nın Allah’ın yolundan saptırma uyarısı ve 31:19’un bedensel yürüyüşü yönü önceleyen, davranışta görünür kılan ipuçlarıdır. Bu bağlar ölçülü tutumu karadan sonra da sürdürülebilecek bir istikamet olarak okumayı destekler. Karşılaştırılan âyetlerdeki topluluklar birbirinden ayrıdır; odaktaki kişilerin kısa bir kara yolculuğu yaptığı da söylenmez.

Kelime ailesinin kırma ve parçalanma kullanımı ayrı bir yankı oluşturabilir. Mevcut {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü kişi} biçimi bu kırılma anlamını taşımaz ve “kırık parça” diye çevrilmez. Bununla birlikte, dalganın {ar:غَشِيَهُم, tr:ghashiyahum, gloss:grubu örttü} ile büyük bir kütleyi kuşatması, aynı grubun {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} ile çıkarılması, ardından {ar:مِنْهُمْ, tr:minhum, gloss:onlardan} ile alt grubun seçilmesi ve {ar:كُلُّ, tr:kullu, gloss:bütün} ile son tipin kapsanması, ölçülü kişiyi kuşatmadan sağ çıkan bir kalıntı gibi düşündürebilir. Bu imge kurtuluş ile bütün-parça ilişkisi arasındadır; ayet fiziksel parçalanma bildirmez ve ölçülülüğü kişiye verilmiş bir derece olarak sunmaz.

Kıyıdaki farklı karşılıklar 29:65’in deniz sıkıntısı sırasıyla karşılaştırılabilir: orada Allah’a çağırma ve dini O’na özgü kılmayı karaya kurtarılma, ardından yeniden ortak koşma izler. Burada {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:mukhliṣīna lahu al-dīna, gloss:dini yalnız O'na özgü kılarak} iç yönelişi, kurtarılma ise bedenin dışarı çıkarılmasını anlatır. 17:67 kurtuluş sonrasındaki yüz çevirme karşılığını ekler. Bu sahneler bedenin dışarı çıkarılmasıyla bağlılığın yönünü aynı kriz çizgisinde buluşturur; iki düzlemden biri ötekinin anlamı ya da nedeni değildir. Buradaki {ar:مِنْهُمْ, tr:minhum, gloss:onlardan} sözüyle ayrılan {ar:مُقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü kişi}, kurtulanların tümüne aynı sonraki yönelişi yüklememeyi gerektirir.

## İşaretler ve örtünün yön değiştirmesi

Ölçülü kişiden sonraki ikinci {ar:وَ, tr:wa, gloss:ve}, sahne anlatısını genel hükme çevirir. {ar:مَا, tr:mā, gloss:olumsuzluk edatı} ile {ar:إِلَّا, tr:illā, gloss:ancak} yadsımayı ahlaki tipin önünde sınırlar; ardından gelen {ar:كُلُّ, tr:kullu, gloss:her biri ve tümü}, {ar:خَتَّارٍ, tr:khattārin, gloss:güveni bozan} ve {ar:كَفُورٍ, tr:kafūrin, gloss:nankör} nitelikleriyle kurulan tipin bütün örneklerini kapsar. Bu hüküm yalnızca söz konusu sınıfa ilişkindir; bütün insanları ya da kurtulanların tamamını kapsamaz.

Şimdiki-geniş {ar:يَجْحَدُ, tr:yajhadu, gloss:bilerek yadsır}, tanınmış bir şeyi geri çeviren genel tutumu bildirir. {ar:بِ, tr:bi, gloss:-e karşı} edatı yadsımayı belirli nesneye, çoğul {ar:ءَايَاتِنَا, tr:āyātinā, gloss:işaretlerimize} bağlar; “-imiz” eki hükmün sesini ilahî konuşana çevirir. 31:31’de işaretlerin iki kez anılması bu sözü gemi ve lütuf sahnesinden devralınan görünür kanıtla buluşturur; 31:23 inkâr ile Allah’a dönüşü yan yana getirir, 29:49’daki açık işaretler de kanıt boyutunu görünür kılar. Kurtuluş, yaşanmış bir deneyim olarak bu sahnede kanıt fikrine karşılık verir; âyet kurtuluşu doğrudan “işaret” diye adlandırmaz ve kastedilen işaretleri tek tek saymaz. Fiilin tanınmışı yadsıma gücü inkârı bilgisizlikten ayırır; bu dilsel ayrım kişiye ayrıca bir zihinsel geçmiş ya da güdü yüklemez.

31:7’de işaretler okununca kişinin yüz çevirmesi, sanki duymamış gibi davranması ve kulağında ağırlık varmışçasına tasvir edilmesi, dışarıdaki örtüyle algının kapanmasını ayrı bir sahnede buluşturur. Buradaki {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örten} dalga fiziksel örtüdür; oradaki yön çevirme ve işitme imgeleriyle yan yana gelişi, bedenin kurtuluşu ile {ar:ءَايَاتِنَا, tr:āyātinā, gloss:işaretlerimizi} kabulünün ayrı sonuçlar olduğunu gösterir. 31:32’deki {ar:يَجْحَدُ, tr:yajhadu, gloss:bilerek yadsır} fiili bu ayrımı genel hükme bağlar. 31:7’deki “duymamış gibi” benzetmesi gerçek sağırlığı anlatmaz; kibir vurgusu o sahneye aittir ve her reddi aynı bilinçli kaçış olarak nitelemeye izin vermez.

Kapanıştaki {ar:خَتَّارٍ, tr:khattārin, gloss:güveni tekrar tekrar bozan}, tek bir hatadan çok güveni alışkanlıkla çiğneyen bir tipi niteler. Denizdeki {ar:دَعَوُا, tr:daʿawū, gloss:çağırdılar} çağrı ve {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:mukhliṣīna lahu al-dīna, gloss:dini yalnız O'na özgü kılarak} yönelişiyle kurulan bağlılığı {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} kurtuluşu izler; bu sıra {ar:خَتَّارٍ, tr:khattārin, gloss:güveni tekrar tekrar bozan} hükmünü kriz anındaki bağlılığın sonradan bozulması olarak okutabilir. Metin burada yemin ya da verilmiş söz bildirmez. Aynı konum için sunulan {ar:جَبَّارٍ, tr:jabbārin, gloss:zorba ve baskıcı} karşı okuması profili zorbalığa kaydırır ve yazılı biçimin bildirdiği güven ihlalinden ayrı bir olasılık olarak kalır. {ar:كُلُّ, tr:kullu, gloss:her biri ve tümü} bu tipin her örneğini kapsar. 22:38 güveni bozanla nankörü birlikte anar, 17:67 kurtuluş sonrasındaki yüz çevirmeyi, 29:65 karaya çıkınca yeniden ortak koşmayı, 29:49 ise belirgin işaretleri gösterir. Bunlar tek bir psikolojik zincir değil, güven ihlali, dönüş, ortaklaşma ve kanıt karşısındaki ret için ayrı karşılaştırmalardır. 17:67’de yüz çevirmek ve 29:65’te başkasına yönelmek ilişkiyi reddetme yankısı da taşır; nankörlüğü bildiren {ar:كَفُورٍ, tr:kafūrin, gloss:çok nankör} ise “yüz çevirmek” anlamına gelmez.

Son sıfat {ar:كَفُورٍ, tr:kafūrin, gloss:çok nankör ve nimeti örten}, alınmış iyiliğin değerini örten nankörlüğü yoğunlaştırır; bu sahnede nimetin açık karşılığı {ar:نَجَّاهُمْ, tr:najjāhum, gloss:kurtardı} kurtuluşudur. Dalgada {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örten} dışarıdan kapanır ve kurtuluş bu örtüyü kaldırır; nankörlükte örtme insanın karşılığına döner, alınan iyiliği görünmez kılma imgesi doğurur. 31:31’in nimet, işaret ve şükür dili bu imgesel geçişi destekler. İki sözcük ayrı tutulur: dalganın örtme fiili suyun eylemini, {ar:كَفُورٍ, tr:kafūrin, gloss:çok nankör} ise olağan anlamıyla nankörlüğü bildirir; örtme kökü insanın yanıtına imge katar, yeni bir fiil anlatmaz.

31:20 nimetleri {ar:ظَٰهِرَةًۭ وَبَاطِنَةًۭ, tr:ẓāhiratan wa-bāṭinatan, gloss:açık ve gizli} diye anarak dış-iç hareketi okumaya bir çerçeve sunar. Bu çerçevede {ar:غَشِيَهُم, tr:ghashiyahum, gloss:üstlerini örten} dalga dış yüzeyi kapatır; {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:mukhliṣīna lahu al-dīna, gloss:dini yalnız O'na özgü kılarak} iç yönelişin arınmasını anlatır. {ar:نَجَّاهُمْ, tr:najjāhum, gloss:onları kurtardı} ile {ar:الْبَرِّ, tr:al-barri, gloss:karaya} varış dış dünyayı yeniden açar, {ar:ءَايَاتِنَا, tr:āyātinā, gloss:işaretlerimiz} görünür kanıtı adlandırır; sondaki {ar:كَفُورٍ, tr:kafūrin, gloss:nankör ve nimeti örten} örtme imgesini insanın iç karşılığına taşır. Bu benzetme 31:20’nin açık-gizli nimet çiftinden beslenir. 31:32 kurtuluşu açıkça işaret diye adlandırmaz; eşleştirme de tasarlanmış çapraz düzen iddiası değil, ayetin olağan zaman sırası içinde okunan bir imgedir.

</source_prose>
