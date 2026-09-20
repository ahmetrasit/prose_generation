# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:7**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.middle.claims.json`

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
- Refer to source paragraphs as `31:7 ¶N`.

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

`(31:7 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:7",
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
        "citation": "(31:7 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_7/31_7.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_7/31_7.middle.claims.json \
  --ayah-ref 31:7
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_7/31_7.prose.editorial.tr.md`

<source_prose>
## Okunan İşaretlerin Karşısında

Âyet, {ar:إِذَا, tr:idhā, gloss:her ne zaman} ile yinelenebilir bir sahne kurar: {ar:تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا, tr:tutlā ʿalayhi āyātunā, gloss:ayetlerimiz kendisine okunduğunda} kişi {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi}, {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:büyüklük taslayarak} davranır; önce {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onları duymamış gibi}, sonra {ar:كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًا, tr:ka-anna fī udhunayhi waqran, gloss:sanki iki kulağının içinde bir ağırlık varmış gibi} olur. Son buyruk ona {ar:فَبَشِّرْهُ بِعَذَابٍ أَلِيمٍ, tr:fa-bashshirhu bi-ʿadhābin alīmin, gloss:acı verici azabı müjdele} der. Böylece okunan işaretler, yüz çeviren bir muhatap ve acı verici ceza haberi aynı karşılaşmada yer alır.

{ar:إِذَا, tr:idhā, gloss:her ne zaman} okunuşu koşul olarak sunar; cevap her gerçekleşişte verilen karşılık gibi görünür, sınırsız bir geçmiş anlatısı gibi değil. Edilgen geniş zaman {ar:تُتْلَىٰ, tr:tutlā, gloss:tilavet edilir} okuyanın adını söylemeden eylemi kurar; failin söylenmemesi, okuyan bulunmadığı anlamına gelmez. Cümlenin öznesi Allah’a nispet edilen {ar:ءَايَٰتُنَا, tr:āyātunā, gloss:ayetlerimiz}, {ar:عَلَيْهِ, tr:ʿalayhi, gloss:ona} ise tilavetin yöneltildiği muhataptır. Biraz sonra {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:ayetleri işitir} içindeki “-hā” da aynı işaretlere döner; ardından kulakları ve son buyruktaki muhatap aynı tekil kişiyi izler. Okunuş, kulak imgesi ve emir böylece ortak bir hedef çevresinde birbirine bağlanır.

{ar:ءَايَٰتُنَا, tr:āyātunā, gloss:ayetlerimiz} hem ayetleri hem işaretleri adlandırır. Allah’a nispet edilen bu işaretlerin okunması ve ardından duyulmamış gibi gösterilmesi, reddedilen sözü kanıt değeri taşıyan bir belirti olarak duyurur; cümle bu işaret etkisini öne çıkarırken hangi iddiayı kanıtladığını açmaz. Buradaki kullanım okunan ayet ve işaret alanında kalır; aynı söz ailesindeki sığınma imgesi bu bağlantıya katılmaz.

Okunma eylemi kendi sırasında da hissedilir. {ar:تُتْلَىٰ, tr:tutlā, gloss:tilavet edilir} burada “okunur” anlamındadır; aynı söz ailesinin bazı kullanımlarında birinin ardından gelme ve izleme sırası da bulunur. Çoğul işaretler, {ar:إِذَا, tr:idhā, gloss:her ne zaman} ile kurulan koşul ve ardından gelen tamamlanmış {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} dönüş, okunanların birer birer geldiği bir akış açar. Burada kesilen tilavet sesi değil, anlatının alımlanmaya varan sırasıdır; sesin fiziksel olarak durması bu bağlantıdan çıkarılmaz.

{ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} koşula cevap olarak tamamlanmış bir Form II eylemdir: sahnenin hareket imgesi ağır ağır uzaklaşma değil, belirgin bir dönüşle kapanır. Bu tamamlanmış görünüş o anki karşılığı kapatır. Aynı söz ailesindeki işi üstlenip yürütme kullanımı başka bir anlam alanında kalır; burada bu kullanıma geçilmez. Dönüşe hâl olan {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:büyüklük taslayarak} ise kişinin kendini büyük görmesini hareketten ayrı, sonradan eklenen bir yorum olmaktan çıkarıp dönüşün yapılış tarzına taşır. Böylece muhatap, neyin dinlenmeye değer olduğuna kendi karar veriyormuş gibi görünür. Bu tavır sahnedeki öz-atıflı üstünlük izlenimidir; gerçek bir görev, meşru yetki ya da toplumsal makam bildirmez. Eylemin tamamlanışı da yalnız bu karşılığı kapatır, kişinin bütün geleceği hakkında hüküm vermez.

## Kulakta Kurulan Eşik

Dönüşün ardından gelen ilk benzetme, {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onları duymamış gibi} sözleriyle, okunan işaretlerden sonra beliren görünüşü anlatır. Olumsuzluk, Form I işitme fiilini geçmiş kuvveti taşıyan cezmli biçime sokar; biraz önce sunulmuş işaretlerle hiç algılanmamış gibi duran tavır arasındaki uyumsuzluk burada belirginleşir. {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:ayetleri işitir} olağan olarak kişinin kendi ses algısını anlatır; bazı kullanımlarda duyulanı anlamaya, kimi bağlamlarda da kabul edip gereğine uymaya uzanır. İşaretlerin nesne olması, kulak içindeki ağırlık ve kendini üstün tutan dönüş, bu daha ileri alımlama yüzünü açar: işitme, anlamı alma ve karşılık verme eşiğine dönüşür. Benzetme bu eşiğin kapanışını gösterirken sesin fiziksel olarak kulağa ulaşıp ulaşmadığını açık bırakır.

İkinci benzetme ilkinden farklı bir ayrıntı ekler. Daha kısa {ar:كَأَن, tr:ka-an, gloss:sanki} davranış gibi görünen duymamayı kurarken, daha dolu {ar:كَأَنَّ, tr:ka-anna, gloss:sanki} kulakların içine yerleşmiş bir durumu resmeder. Sıra, görünür işitmeme tavrından bedensel ağırlığa doğru yerel bir yoğunlaşma yaratır. {ar:فِىٓ, tr:fī, gloss:içinde} edatı ağırlığı kulakların içine yerleştirir; öne alınan yer öbeği okura önce alıcı organı, sonra onun içindeki durumu gösterir. İyelikli ikil {ar:أُذُنَيْهِ, tr:udhunayhi, gloss:onun iki kulağı} bu ağırlığı kişinin kendi iki kulağında kurar.

{ar:وَقْرًا, tr:waqran, gloss:ağırlık} olağan anlamıyla ağırlığı, kulak yanında işitmeyi ağırlaştıran kullanımıyla duyusal bir engel imgesine taşır; kulağın yeri ve hemen önceki duymama bu özel çağrışımı etkinleştirir. Seyrek sözcüğün bu konumdaki seçimi tanınabilir bir kulak-tıkanması kalıbı kurar: ret, duyusal bir sahneye dönüşür. Sözcüğün hafifletilmiş okunuşu ile çevresindeki diş, geniz ve küçük dil ünsüzleri de imgeye sıkışık, boğuk bir ses dokusu katar; kanonik biçim değişmez, bu işitsel doku benzetmenin etkisini artırır. İşaretler okunurken dönen ve kendini büyük gösteren kişiyle birlikte düşünüldüğünde, ağırlık sahnede etkili sağırlıktan çok sergilenen ret zincirini kurar. Bu görüntü tıbbi tanı ya da iç niyet hakkında hüküm vermez.

Somut kulak imgesi alımlamanın kapısını görünür kılar: {ar:أُذُنَيْهِ, tr:udhunayhi, gloss:onun iki kulağı} işitme organını adlandırır; aynı söz ailesinin başka fiil ve kalıpları söze dikkatle kulak vermeyi, kimi durumlarda duyulanı benimseyip buyruğa uymayı anlatabilir. Organ adı, {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:ayetleri işitir} fiilinin anlama ve kabul yönüyle buluştuğunda, sesin alınmasından benimsenmesine uzanan eşiği hissettirir. Bu bağlantı, isimde “izin” anlamı bulunduğu iddiası değildir; eşik imgesi organ adıyla fiilin alımlama yönünden kurulur.

Bu eşikteki ağırlık, söz ailesindeki iki ayrı biçimle iki imgesel katkı kazanır. Taşınan yükü anlatan {ar:الوِقْر, tr:al-wiqr, gloss:taşınan ağır yük}, kulaklardaki ağırlıkla birleşince birikmiş baskının dikkati aşağı bastırması imgesini ekler. Sakin, ölçülü ağırbaşlılığı anlatan {ar:الوقار, tr:al-waqār, gloss:ağırbaşlılık} başka bir biçim ve kullanımdır; {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:büyüklük taslayarak} ile buluştuğunda kişinin kendine yakıştırdığı üstünlüğe sergilenen bir ağırbaşlılık yüzü katar. Bu söz ailesinin ayrı ad ve kişi kullanımları toplumsal şeref ya da önderlik konumunu da anlatır; bu bağlantıda açılan ise gerçek makam değil, prestij izlenimidir. Kulak konumunun çağırdığı yük ile kendini büyük görmenin çağırdığı ağırbaşlılık, alımlama eşiğine bindirilen bir balast imgesinde birleşir; odaktaki kulak ağırlığı benzetmesi bu birliktelikte merkezde kalır.

Bu işitme eşiğinin farklı yönleri başka ayetlerde belirginleşir. 45:8’de {ar:يَسْمَعُ آيَاتِ اللَّهِ تُتْلَىٰ عَلَيْهِ ثُمَّ يُصِرُّ مُسْتَكْبِرًا كَأَن لَّمْ يَسْمَعْهَا, tr:yasmaʿu āyāti llāhi tutlā ʿalayhi thumma yuṣirru mustakbiran ka-an lam yasmaʿhā, gloss:Allah’ın ayetleri kendisine okunurken duyar, sonra kibirle direnip sanki işitmemiş gibi olur} okunan ayetlerle kibirli reddi yan yana getirir ve 31:7’deki işaret-kanıt yankısını güçlendirir; bu ortaklık hangi iddianın kanıtlandığını belirtmez. 67:10’da {ar:لَوْ كُنَّا نَسْمَعُ أَوْ نَعْقِلُ, tr:law kunnā nasmaʿu aw naʿqilu, gloss:keşke işitseydik ya da akletseydik} işitme ile akletme ayrı ayrı anılır; bu ikilik sesin alınmasından anlamı kavramaya geçişi aydınlatırken işitmeyi tek başına itaatle özdeşleştirmez. 18:57’de Rabbinin ayetleri hatırlatılan kişinin yüz çevirmesi ve kulak ağırlığı, dönüşü kapalı alımlamayla buluşturur. Bu üç temas, 31:7’yle yapısal karşılaştırma kurar; 31:7’deki kişi, olay ya da ortak dinleyici için özdeşlik veya doğrudan alıntı kurmaz.

17:46’da Kur’an anılınca arkalarını dönme, 18:57’de ise hatırlatılan ayetlerden yüz çevirme ve kulak ağırlığı, işitme imgesini eyleme geçmiş reddin yönüne taşır. Buna karşılık 9:61’de Peygamber için {ar:قُلْ أُذُنُ خَيْرٍ لَكُمْ يُؤْمِنُ بِاللَّهِ وَيُؤْمِنُ لِلْمُؤْمِنِينَ, tr:qul udhunu khayrin lakum yuʾminu bi-llāhi wa-yuʾminu lil-muʾminīn, gloss:sizin için hayırlı bir kulak de, Allah’a ve müminlere inanır} denmesi, aynı organ imgesine hayra açık, alıcı bir yön kazandırır. Bu karşıtlık kulağın ret ve kabulü anlatabilen imge alanını genişletir; 31:7’deki kişinin kimliğini ya da ağırlığın fiziksel nedenini belirlemez. Bir işin ağır gelmesini anlatan {ar:كَبُرَ عَلَيْنَا, tr:kabura ʿalaynā, gloss:bize ağır ve güç geldi} ayrı bir fiil yapısıdır; {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:büyüklük taslayarak} ise Form X etkin ortaçtır. Dolayısıyla kabul güçlüğüyle kurulan temas biçim özdeşliği değil, kulak ağırlığı ile hayra açık kulağın sunduğu benzetmeli karşılaştırmadır.

## Dikkatin Başka Yönleri

31:6 sahneye, 31:7’deki işitme eşiğinin yanına edinilmiş başka bir dikkat akışı ekler. {ar:يَشْتَرِى, tr:yashtarī, gloss:satın alır} ile {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahwa l-ḥadīth, gloss:oyalayıcı konuşma}, dikkati uzaklaştırıp kulağı doldurabilecek bir akışı gösterir: satın alma onu rastlantısal gürültü değil edinilmiş girdi yapar; {ar:لَهْوَ, tr:lahwa, gloss:oyalayıcı söz} dikkati başka yöne çekerken {ar:ٱلْحَدِيثِ, tr:al-ḥadīth, gloss:konuşma} süren söz akışını taşır. {ar:لِيُضِلَّ, tr:liyuḍilla, gloss:saptırmak için} bu akışa uzaklaştırıcı bir yön verir, {ar:هُزُوًا, tr:huzuwan, gloss:alay konusu ederek} ise ayetleri dinlenecek söz olmaktan çıkarıp alay nesnesi yapar. Bu işlemler 31:7’deki {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:ayetleri işitir} fiilinin anlamı alıp kabule uzanan yüzüyle ve {ar:وَقْرًا, tr:waqran, gloss:ağırlık} imgesiyle birleşince, dikkat önceden edinilmiş başka bir akışla dolmuş ve ağırlık bu karşı-akışı bastırmış gibi okunabilir. Böylece yakınlık, seçilmiş başka bir söz akışı ile yüz çevirmeyi aynı ret düzleminde buluşturur; bu okuma 31:6 ile 31:7’deki kişileri özdeşleştirmez ve aralarında kesin bir neden-sonuç ilişkisi kurmaz.

31:21, dikkatin hangi kaynağı izlediğini bir diyalogla görünür kılar. Bir topluluğa {ar:ٱتَّبِعُوا۟ مَآ أَنزَلَ ٱللَّهُ, tr:ittabiʿū mā anzala llāh, gloss:Allah’ın indirdiğini izleyin} denir; cevap aynı izleme eylemini başka kaynağa çevirir: {ar:بَلْ نَتَّبِعُ, tr:bal nattabiʿu, gloss:aksine izliyoruz}, yani {ar:مَا وَجَدْنَا عَلَيْهِ ءَابَاءَنَا, tr:mā wajadnā ʿalayhi ābāʾanā, gloss:atalarımızı üzerinde bulduğumuz şeyi}. Atalar, önceden bulunmuş yolu taşıyan toplumsal kaynak olur. Bu izleme dizisi, 31:7’deki {ar:تُتْلَىٰ, tr:tutlā, gloss:tilavet edilir} ile hissedilen ardışıklığa temas eder; böylece yüz çevirme, mesaj yokluğundan ziyade devralınmış başka bir bağlılığa yönelme olarak da düşünülebilir. Bu izleme düşünsel taklit olabilir; benzerliğin işitsel bir karşı-akış olması gerekmez. 31:21’deki çoğul topluluk ile 31:7’nin tekil muhatabı özdeş değildir; temas, ortak kimlik değil, izleme ve bağlılık imgesi düzeyindedir. Aynı ayette şeytanın onları {ar:يَدْعُوهُمْ إِلَىٰ عَذَابِ السَّعِيرِ, tr:yadʿūhum ilā ʿadhābi al-saʿīr, gloss:alevli azaba çağırması} da devralınan yolun sonuna yönelen ayrı bir çağrı kurar.

31:18, yüz ve yürüyüş üzerinden toplumsal gösterişi sahneye taşır: {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-n-nās, gloss:yanağını insanlardan yana çevirme}, {ar:وَلَا تَمْشِ فِى الْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī l-arḍi maraḥan, gloss:yeryüzünde böbürlenerek yürüme} ve {ar:كُلَّ مُخْتَالٍ فَخُورٍ, tr:kulla mukhtālin fakhūr, gloss:kibirli ve övüngen kişi} yüzü, adımı ve övüngen duruşu birlikte görünür kılar. 31:19, buna ölçülü yürüyüş ve kısılmış ses buyruğunu ekler: {ar:وَٱقْصِدْ فِى مَشْيِكَ وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-qṣid fī mashyika wa-ghḍuḍ min ṣawtika, gloss:yürüyüşünde ölçülü ol ve sesini kıs}. Seslerin en çirkini eşeklerin sesidir karşılaştırması {ar:إِنَّ أَنكَرَ ٱلْأَصْوَٰتِ لَصَوْتُ ٱلْحَمِيرِ, tr:inna ankara l-aṣwāti la-ṣawtu l-ḥamīr, gloss:seslerin en çirkini eşeklerin sesidir} dışarı çıkan sesi belirginleştirir. Bu beden ve ses imgeleri, 31:7’de içeri alınan sesi reddeden kulakla dışarıya sunulan yüz, adım ve ses arasında aynı etik yönelimin iki tarafı gibi bir karşılaştırma kurar. Bu okumada 31:18’deki yüz ve yürüyüş öğütleri ile 31:19’daki ses buyruğu, 31:7’deki sahneyle imgesel düzeyde karşılaştırılır; öğütler 31:7’deki kişinin beden tarifi ya da davranış kaydı değildir. Özellikle 31:19’daki sesi alçaltma buyruğu onun yüksek sesle konuştuğunu göstermez.

## Müjdenin ve Cezanın Sözü

Tasvirden sonra gelen {ar:فَ, tr:fa, gloss:bunun üzerine} önceki dönüşle son emri yerel bir sonuç ilişkisine bağlar: anlatı gözlemden yöneltilmiş eyleme geçer. {ar:بَشِّرْهُ, tr:bashshirhu, gloss:ona müjdele} aynı kişiye seslenir; tilavetteki {ar:عَلَيْهِ, tr:ʿalayhi, gloss:ona}, kulaklardaki {ar:أُذُنَيْهِ, tr:udhunayhi, gloss:onun iki kulağı} ve emrin sonundaki “-hu” tekil hedefi korur. Okunan işaretlerin söz olayıyla son duyurunun haber olayı böylece ayetin yerel ses çerçevesini kapatır. {ar:فَ, tr:fa, gloss:bunun üzerine} davranışın ardından gelen karşılığı bildirir; cezanın uygulanış biçimini belirlemez.

{ar:بَشِّرْهُ, tr:bashshirhu, gloss:ona müjdele} olağan olarak sevindirici haber verme emridir; 36:11’de {ar:فَبَشِّرْهُ بِمَغْفِرَةٍ وَأَجْرٍ كَرِيمٍ, tr:fa-bashshirhu bi-maghfiratin wa-ajrin karīm, gloss:ona bağışlanma ve cömert bir ödülü müjdele} olumlu beklentiyi gerçekleştirir. 31:7’de aynı haber verme biçimi açıkça adlandırılan {ar:عَذَابٍ أَلِيمٍ, tr:ʿadhābin alīmin, gloss:acı verici azap} içeriğine yönelir; bu içerik beklenen iyi haberi acı habere çevirir, emir ise haber verme olarak kalır. Yakın bir reddediş sahnesi olan 45:8’de ceza içeriğinin yinelenmesi bu terslemeyi destekler; karşılaştırma iki ayeti aynı olay yapmaz. Böylece 31:7’deki ironi, iyi haber kalıbını koruyup açıkça adlandırılmış kötü içeriğe yöneltmesinden doğar.

{ar:بِعَذَابٍ, tr:bi-ʿadhābin, gloss:bir azapla} içindeki edat cezayı duyurunun içeriği yapar; belirsiz soyut ad {ar:عَذَابٍ, tr:ʿadhābin, gloss:bir ceza} cezanın türünü bildirirken süresini, ölçüsünü ve uygulanış biçimini açık bırakır. {ar:أَلِيمٍ, tr:alīmin, gloss:acı verici} sıfatı azabın acı oluşturan niteliğini verir; acıyı yaşayacak kişi emirdeki aynı muhataptır. Aynı söz ailesinin yiyecek ve içecek için tatlı, hoş ve kolay tüketilir olmayı anlatan ayrı biçimleri, burada yalnızca lezzet karşıtlığı için bir yankı sağlar. Odaktaki {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap} cezalandırma anlamını korur; bu karşılaştırma gerçek tat ya da söz kökeni iddiası kurmaz.

Tilavetin sürekliliği ile cezanın duyurusu, burada iki temkinli söz ailesi yankısı açar. {ar:تُتْلَىٰ, tr:tutlā, gloss:tilavet edilir} edilgen “okunur” anlamını korur; aynı söz ailesinin bazı ad ve kalıpları kişiye bağlı kalan sorumluluk, güvence ya da talep edilebilir hakkı anlatır. Bu çağrışım, okunan işaretlerin kalıcı bir iddia gibi de duyulmasını mümkün kılar; bu yerel imge içinde {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} ile uzaklaşma, iddiayı ortadan kaldırmayan bir hareket olarak düşünülebilir. Benzer biçimde {ar:بَشِّرْهُ, tr:bashshirhu, gloss:ona haber ver} haber verme emri olarak kalırken, aynı söz ailesinin belirli ad ve kalıplarındaki “tamamlanmadan önce görünen ilk iz” anlamı acı azap içeriğine eşlik eder; duyuru yaklaşan sonucun ilk belirtisi gibi hissedilebilir. Bu iki ilişki söz oyunu düzeyinde kalır: buradaki bağlantı bir borç veya hukuk hükmü, kehanet ya da zaman çizelgesi kurmaz; {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} de bu ayette yüz çevirme anlamını korur.

Cezanın hemen ardından 31:8’de iman edip iyi işler yapanlara {ar:إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ, tr:inna lladhīna āmanū wa-ʿamilū ṣ-ṣāliḥāti lahum jannātu n-naʿīm, gloss:iman edip iyi işler yapanlara nimet bahçeleri} verileceği söylenir. Bu olumlu karşılık, 31:7’deki ceza duyurusunu ödül eksenine yerleştirir; komşuluk kişileri özdeşleştirmez ve bu iki sahneyi bütün olasılıkları tüketen bir ikilik saymaz.

## Yükün ve Yönelişin Ölçeği

31:24, kulak ağırlığı ile ceza arasında maddi bir ölçü benzerliği açar. Orada kısa bir yararlandırmanın ardından zorunlu yöneliş gelir: {ar:نُمَتِّعُهُمْ قَلِيلًا ثُمَّ نَضْطَرُّهُمْ, tr:numattiʿuhum qalīlan thumma naḍṭarruhum, gloss:onları kısa süre yararlandırır, sonra zorunlu olarak sürükleriz}; ardından {ar:إِلَىٰ عَذَابٍ غَلِيظٍ, tr:ilā ʿadhābin ghalīẓ, gloss:yoğun ve sert bir azaba} denir. 31:7’deki acı azapla aynı {ar:عَذَابٍ, tr:ʿadhābin, gloss:ceza} adının yinelenmesi iki ceza sözünü bağlar. Kısa yararlandırmadan zorlamaya geçiş, 31:7’deki görünür dönüşün karşısında eylem gücünü dışarıdan dayatılan harekete çevirir; {ar:غَلِيظٍ, tr:ghalīẓ, gloss:yoğun ve kalın} ise cezaya maddi bir yoğunluk verir. Bu nitelik, {ar:وَقْرًا, tr:waqran, gloss:kulak ağırlığı} ile yük ve yoğunluk arasında benzetmeli bir yankı kurar. Bu bağlantı cezaların nitelemelerini özdeşleştirmez; 31:7’deki tekil muhatapla 31:24’teki çoğul topluluk da aynı kişiler olarak sunulmaz.

31:30, kendini büyük görme imgesinin karşısına kozmik bir yücelik ve büyüklük ölçüsü koyar. Hak ile bâtıl karşıtlığının sonunda {ar:وَأَنَّ اللَّهَ هُوَ الْعَلِىُّ الْكَبِيرُ, tr:wa-anna llāha huwa l-ʿaliyyu l-kabīr, gloss:Allah yücedir ve büyüktür} denir. Bu dil 31:7’deki {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:kendini büyüten} ile aynı ölçeğe dokunur; yücelik dikey bir ölçü kurduğunda, kişinin kendine mal ettiği üstünlük gerçek yüksekliğe göre ölçü yanılgısı gibi görünebilir. Bu olası geri dönüş, 31:30’un kesin hedefi olarak sunulmaz: ayet kendi kozmolojik sonucunu tamamlıyor olabilir ve sözcüklerin buluşması tek başına geriye dönük gönderme kurmaz.

31:32, kulak ağırlığının sabit bir yeti kaybı sayılıp sayılamayacağı sorusuna, baskı ve güvenlik arasında değişen bir çoğul sahne ekler. Dalgalar gölgelikler gibi üzerlerine çöktüğünde insanlar {ar:دَعَوُا اللَّهَ مُخْلِصِينَ لَهُ الدِّينَ, tr:daʿawū llāha mukhliṣīna lahu d-dīn, gloss:dini yalnız O’na özgü kılarak Allah’a yalvardılar}; kurtarılıp karaya çıkarılınca {ar:فَلَمَّا نَجَّىٰهُمْ إِلَى الْبَرِّ, tr:fa-lammā najjāhum ilā l-barr, gloss:onları karaya çıkarıp kurtarınca} güvenliğe geçilir. Tehlikedeki bu yöneliş, 31:7’deki {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:ayetleri işitir} fiilinin ses almaktan anlamaya ve karşılığa uzanan eşiğini görünür kılar; {ar:وَقْرًا, tr:waqran, gloss:kulaklardaki ağırlık} ise kapalı alımlama imgesini taşır. Kurtarılanlardan bazılarının ölçülü davranması, ardından ayetleri inkâr ve vefasızlığın anılması, baskıda açılan yönelişin güvenlikte her zaman sürmediğini düşündürür. Ayetler ortadayken {ar:وَمَا يَجْحَدُ بِآيَاتِنَا, tr:wa-mā yajḥadu bi-āyātinā, gloss:ayetlerimizi ancak inkâr eder} denmesi inkârı salt işitememeye indirgemez; {ar:خَتَّارٍ, tr:khattārin, gloss:vefasız ve hain} nitelemesi de kurtuluş sonrasındaki ihaneti ekler. Böylece sahne, baskı altında ve güvenlikte alımlamanın değişebildiğini gösterir; bu çoğul grubun 31:7’deki tekil muhatabın hayat öyküsü olduğunu söylemez.

</source_prose>
