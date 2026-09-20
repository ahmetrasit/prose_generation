# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:51**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.middle.claims.json`

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
- Refer to source paragraphs as `17:51 ¶N`.

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

`(17:51 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:51",
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
        "citation": "(17:51 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_51/17_51.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_51/17_51.middle.claims.json \
  --ayah-ref 17:51
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_51/17_51.prose.editorial.tr.md`

<source_prose>
## Açık Bırakılan Yaratılmış

Ayetin başındaki {ar:أَوْ, tr:aw, gloss:ya da} sözü yeni bir ihtimali açık tutar. Ardından gelen belirsiz {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey}, ne tür olduğu söylenmeyen bir yaratılmışı seçenek yapar; {ar:مِّمَّا, tr:mimmā, gloss:her ne ise} bu türü adlandırmadan bırakır. Ayet, aynı şeyi {ar:يَكْبُرُ فِى صُدُورِكُمْ, tr:yakburu fī ṣudūrikum, gloss:göğüslerinizde büyür} diye niteler: yaratılmış seçenek muhatapların göğüslerinde büyür. Böylece ihtimal açık kalırken, onun içlerinde aldığı büyüklük ve yer belirginleşir.

Bu açık ihtimal, hemen önceki maddî itirazla birlikte duyulur. Konuşanlar kemik ve ufalanmış parçalar olduktan sonra diriltilmeyi sorar (17:49); taş ya da demir olmayı da eklerler (17:50). {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler}, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar}, {ar:حِجَارَةً, tr:ḥijārah, gloss:taş} ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} birlikte dağılmadan dirençli sertliğe uzanan bir madde aralığı kurar. Ardından gelen {ar:مَن يُعِيدُنَا, tr:man yuʿīdunā, gloss:bizi kim geri getirecek} sorusuna ilk {ar:قُلِ, tr:quli, gloss:de} buyruğuyla verilen {ar:ٱلَّذِى فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:alladhī faṭarakum awwala marratin, gloss:sizi ilk kez var eden} cevap, dikkati hangi maddenin dayanacağı sorusundan onu ilk kez var edene çevirir. Bu yerel bağ, kırıntıdan taşa ve demire uzanan her hâli geri getirilebilir yaratılmışlar arasında düşünmeye açar; aynı madde dizisi 17:49 ve 17:50'nin art arda imkânsızlık itirazı olarak okunmasını da korur. Sertlik de ilk yaratma ve geri getirme kudretinin dışında kalmaz; bedenin yeniden kuruluş yolu açık bırakılır ve cevap ilk var edişe dayanır.

Bu dönüş ihtimali, 17:49'daki {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış} ifadesindeki {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} sözüyle başka bir ton kazanır. “Yeni” olağan yeni oluş anlamını korurken, ona ait sözlük kullanımlarından biri kesilme sonrasındaki yeniliği de anlatır; burada bu çağrışımı bağımsız olarak harekete geçiren, aynı ayetteki {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar} sözcüğüdür (17:49). Parçalanma ile yeni oluş yan yana geldiğinde dönüş, dağılmadan sonra yeniden biçimlenme imkânı edinir; kesilme sonrası yenilik de bu ayette ufalanmanın açtığı bağlamsal yankı olarak kalır.

Kırıntı ile sert maddenin kurduğu aralık, {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} için aktarılan üç ayrı sözlük kullanımını da anlaşılır kılar. Ölçü ve sınır kullanımı, değişen maddeleri ölçülü bir yaratılmışlık çerçevesinde tutar: {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusu geri dönüşü kurarken, {ar:يَكْبُرُ فِى صُدُورِكُمْ, tr:yakburu fī ṣudūrikum, gloss:göğüslerinizde büyür} diye göğüste büyüyen yaratılmış yine sınırları olan bir nesne olarak kalır. Deri ölçme örneği bu malzeme sahnesine taşınmaz; bu kolda teması kuran, {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler}, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar}, {ar:حِجَارَةً, tr:ḥijārah, gloss:taş} ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} arasındaki değişkenliktir (17:49, 17:50). Sözcüğün var etme kullanımı dağılmış parçaları ve dirençli maddeleri ayrı ayrı tetikleyici yapar; ikisi de {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} ilk yaratılış cevabına bağlanır. Tamamlanmış, gözle seçilebilen dış biçim kullanımı ise kemik ve kırıntıdan, geri gelişin yalnız bir kütleyi değil tanınabilir bir bedeni de kapsayabileceğini düşündürür (17:49). Bedenin ayrıntıları açık bırakıldığından bu son kol tanınabilir biçimin geri gelişini düşündüren bir ufuk olarak kalır.

Bu biçim ufkunda {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar} dağılmayı, {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler} ise bedenî kalıntıyı açıkça adlandırır (17:49). Bu kalıntıların ardından gelen {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:elbette diriltilecek olanlar} sözü diriltilmeyi sorar ve bedenin yeniden kuruluş yolunu açık bırakır. 17:51'deki {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusu ile {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} cevabı bu kalıntılara ilk var edilişi ekler; birlikte, dağılmış durgunluktan yeniden harekete geçiş belirir.

İlk yaratılışın dönüşe dayanak olması, bir sözlük yankısıyla başlangıcı da açılış gibi duyurur. {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} olağan anlamıyla ilk kez var etmeyi söyler; aynı kökün bir bütünü yarıp içini ya da ardındakini görünür kılma kullanımı da vardır. Bu açılma imgesini {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} sözcüğünün yaratıma açık oluşu, 17:49'daki {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar} ile {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler} ve 17:50'deki {ar:حِجَارَةً, tr:ḥijārah, gloss:taş} ile {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} yüzeyleri harekete geçirir (17:49, 17:50). Ayrıca {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} dönüş sorusu ile {ar:أَوَّلَ مَرَّةٍۢ, tr:awwala marratin, gloss:ilk defa} ifadesinin kurduğu önce-sonra sırası ilk var edilişi dönüşe açılan başlangıç gibi duyurur. Bu sözlük yankısı, ilk kez var etme cevabına açılış hissi ekler; cevabın olağan anlamı ilk kez var etmektir.

{ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusundaki geri getirme, ayrılınan şeye dönmeyi ya da başlangıçtan sonra aynı işe yeniden yönelmeyi de çağrıştırabilir. {ar:أَوَّلَ, tr:awwala, gloss:ilk} başlangıç ve önceliği, {ar:مَرَّةٍۢ, tr:marratin, gloss:bir defa} sayılabilir bir gerçekleşmeyi verdiğinden, ilk var ediliş dönüşün yerel bir öncülü olur. Bu sayılabilirlik, bilinen aralıklarla yinelenen eylem kullanımına da döngü yankısı ekler; sözlükte {ar:أَوَّلَ, tr:awwala, gloss:ilk} için aktarılan “geri dönmek ya da sonunda belirli bir duruma varmak” kullanımıysa başlangıca bir varış ucu ekleyebilir. Birlikte düşünüldüklerinde ilk açılıştan dönüşe, oradan son cevaptaki {ar:عَسَىٰٓ أَن يَكُونَ قَرِيبًا, tr:ʿasā an yakūna qarīban, gloss:umulur ki yakın olsun} ifadesine uzanan tarihsiz bir yol belirir. Aynı geri-dönüş fiilinin başka bir çekimi, {ar:أَن يُعِيدَكُمْ فِيهِ تَارَةً أُخْرَىٰ, tr:an yuʿīdakum fīhi tāratan ukhrā, gloss:sizi oraya bir kez daha döndürmesi} sözüyle denize yeniden giriş sahnesinde kullanılır (17:69); bu sahne aynı fiilin başka bağlamdaki dönüş kullanımına karşılaştırma sağlar, 17:51'deki diriliş için açıklayıcı bir mekanizma kurmaz. Odak ayetteyse ilk var ediliş dönüş sorusuna yerel dayanak verir.

Madde aralığının ötesindeki yaratılmışlık ufkunu evrensel tesbih sözü genişletir: {ar:وَإِن مِّن شَيْءٍ إِلَّا يُسَبِّحُ بِحَمْدِهِ, tr:wa-in min shayʾin illā yusabbiḥu bi-ḥamdih, gloss:hiçbir şey yoktur ki O'nu hamdiyle tesbih etmesin} hiçbir şeyi bu karşılıktan dışarı bırakmaz (17:44). {ar:مِّن شَيْءٍ, tr:min shayʾin, gloss:hiçbir şey} diye sınırsız tutulan alan yaratılmış maddeleri de var edilmişler dünyasına alır; {ar:وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:wa-lākin lā tafqahūna tasbīḥahum, gloss:fakat onların tesbihini kavrayamazsınız} insanın bu tesbihi kavrayışını sınırlar (17:44). Bu çerçevede kemik, taş ve demir insanın anlamadığı bir karşılık veren yaratılmışlar olarak düşünülebilir. 17:44 bu temasta özel bir madde açıklamasına ek olarak genel bir kozmik arka plan sağlar; kavrayış sınırının nedeni ayette açıklanmaz. 17:51'in kendi {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} ve {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} biçimleri işitilen insan sözlerini korur; bu bağlantıda yaratılmışların tesbihi ile insan konuşması ayrı düzlemlerde işler.

Bu açık bırakılan {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} seçeneği daha ileride kemik ve ufalanmış parçalarla yeniden belirir: {ar:عِظَٰمًۭا وَرُفَاتًا, tr:ʿiẓāman wa-rufātan, gloss:kemikler ve ufalanmış parçalar} sorusunun ardından {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış} ifadesini anması, geniş ihtimali somut bir maddî itiraza çevirir (17:98). Bu tekrar, 17:51'deki {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} cevabını değiştirmez; 17:98'in sonraki sorusundan ayrı bir bağlantı olarak kalır ve hedef kelimelerin biçim çözümlemesine dokunmaz. Açık kalan yaratılmış şeyin türünden sonra ayetin dikkati, onun muhatapların içinde nasıl büyüdüğüne döner.

## Göğüste Büyüyen Ölçü

İçteki büyüklüğün yeri, {ar:مِّمَّا, tr:mimmā, gloss:her ne ise} ile açılan ilgi alanında belirginleşir: {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} seçenek olarak durur, {ar:يَكْبُرُ, tr:yakburu, gloss:büyür} onu niteler, {ar:فِى صُدُورِكُمْ, tr:fī ṣudūrikum, gloss:göğüslerinizde} ise büyüklüğün yaşandığı yeri verir. Bitmemiş geçişsiz fiil büyümeyi öznesinin içinde sürdürür; onu dışarıdan büyüten ayrı bir fail kurmaz. {ar:صُدُورِكُمْ, tr:ṣudūrikum, gloss:göğüslerinizde} boynun altındaki ön beden bölgesini, gerçek göğüsleri adlandırır. Bu seçim anatomik göğsü öne çıkarır; kalple ilgili karşıt bir hüküm vermez.

Belirsiz ve mansup {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey}, adı verilmeyen yaratılmışı seçenek yapar; cümledeki yeri ilgi yapısı ve sözdizimiyle anlaşılır. Aynı sözcüğün var etme ve ortaya çıkarma anlamı, {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusu ile {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} cevabının temasında yeniden duyulur; bu sözlük yankısı ismin mansup biçiminin gerekçesi değildir. Böylece adlandırılmamış seçenek dilbilgisel olarak yerinde kalırken, yaratılmışlık anlamı dönüş cevabına bağlanır.

Ölçü ve iç büyüklük yan yana gelince, yaratılmış şey konuşanların gözünde büyüse bile sınırları olan bir nesne olarak kalır. {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} için kaydedilen, nesnenin ölçü ve sınırlarını işten önce belirleme kullanımı; {ar:يَكْبُرُ, tr:yakburu, gloss:büyür} ile {ar:فِى صُدُورِكُمْ, tr:fī ṣudūrikum, gloss:göğüslerinizde} yerinin birlikte kurduğu ölçeğe temas eder. Deri ölçme örneği bu malzeme ve beden sahnesine taşınmaz. Büyüklüğün bir şeyi zihinde olağandan önemli sayma kullanımı ise aynı göğüsleri iç değerlendirme alanı, yaratılmış şeyi de değerlendirilen nesne yapar: maddî itiraz sürerken, göğüste aldığı öznel ölçü de görünür olur. Nesnenin sınırıyla konuşanların ona verdikleri iç ölçü böylece iki ayrı ölçek olarak birlikte kalır.

Bu iç ölçü, geri dönüşün nasıl göründüğünden başka, konuşanlara nasıl ağır gelebileceğine de dokunur. {ar:يَكْبُرُ, tr:yakburu, gloss:büyür} için aktarılan bir başka kullanım bir işin kişiye ağır ya da güç gelmesini anlatır; kemik ve ufalanmış parçalarla taş ve demir arasındaki bağımsız karşıtlık bu dalı etkinleştirir (17:49, 17:50). Böylece dönüş imkânı hem göğüste büyüyen bir tasarı hem de güç gelebilecek bir iş olarak duyulur. Bu sözlüksel dal, ayetteki geçişsiz büyüme anlamından ayrı durduğu için konuşanların kişiliğine dair bir teşhis yüklemez.

Göğüste büyüyen tasarı, çevresindeki büyüklük diline de açılır. 17:40'taki büyük söz, 17:59'daki ayetler ve korkutucu uyarı, 17:60'taki büyük taşkınlık iç ölçüyü ortak bir büyüklük diliyle kuşatır. {ar:يَكْبُرُ فِى صُدُورِكُمْ, tr:yakburu fī ṣudūrikum, gloss:göğüslerinizde büyür} olağan büyümeyi korurken, “bir şeyi zihinde olağandan üstün ve önemli sayma” dalı bu bağlamda kendini üstün görme ihtimalini de duyurabilir. 17:60'taki {ar:كَبِيرًا, tr:kabīran, gloss:büyük} büyüme fiilinin başka bir çekimi değil, çerçeveyi kapatan bağımsız nitelemedir; {ar:قَوْلًا عَظِيمًا, tr:qawlan ʿaẓīman, gloss:büyük bir söz}, {ar:بِالْآيَاتِ, tr:bi-l-āyāt, gloss:ayetlerle}, {ar:تَخْوِيفًا, tr:takhwīfan, gloss:korkutucu uyarı} ve {ar:طُغْيَانًا كَبِيرًا, tr:ṭughyānan kabīran, gloss:büyük bir taşkınlık} bu teması taşır (17:40, 17:59, 17:60). Bu yerel büyüklük yankısı kendini üstün görme ihtimalini besler; konuşanların güdüsünü teşhis etmez.

Uyarı, sınama, artış ve taşkınlık sırası, iç ölçünün dışarıdaki karşılıkla nasıl yan yana gelebileceğini belirginleştirir. 17:60'ta {ar:يَكْبُرُ فِى صُدُورِكُمْ, tr:yakburu fī ṣudūrikum, gloss:göğüslerinizde büyür} ifadesini izleyen {ar:يَزِيدُهُمْ, tr:yazīdūhum, gloss:onları artırır}, {ar:طُغْيَانًا, tr:ṭughyānan, gloss:taşkınlık} ile birlikte bir artış bildirir; bu sıra, göğüste büyüyen itirazla dış davranıştaki yükseliş arasında ihtimalli bir geri-bildirim okumasına izin verir (17:60). Bu bağlantıda sınama, düzeltmekten çok verilmiş karşılığı açığa çıkarıyor olabilir; olası ilişki kanıtlanmış bir nedensellik ya da psikoloji yasası değildir. Tekrarlanan büyük sözler ayrıca retorik bir çerçeve kurabilir; bu çerçevenin içinde maddî yaratılmış ihtimali yine ayetin önündedir.

İç ölçünün karşısında daha geniş bir yaratma kudreti belirir. Gökleri ve yeri yaratanın muhatapların benzerlerini yaratmaya da gücü yettiği söylenir (17:99); {ar:خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:khalaqa al-samāwāti wa-l-arḍ, gloss:gökleri ve yeri yarattı} ile {ar:قَادِرٌ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُمْ, tr:qādirun ʿalā an yakhluqa mithlahum, gloss:onların benzerlerini yaratmaya gücü yeter} yaratma ölçeğini göklerden insan benzerlerine taşır. Bu kudret, göğüste büyütülen yaratılmışın ölçüsünü aşan bir dayanak olarak, {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} cevabını yeniden duyurur. 17:99'daki kuşku götürmeyen vade ({ar:أَجَلًا لَّا رَيْبَ فِيهِ, tr:ajalan lā rayba fīhi, gloss:kuşku duyulmayan bir süre}) bu yaratma ufkuna zaman boyutunu ekler; bu karşılaştırma 17:51'in yakınlık cevabına takvim vermez. Buna karşı yalnız dünya hayatının bulunduğunu ve insanları zamanın yok ettiğini savunan söz, yaratma ve vade ufkuna karşı çıkar (45:24); böylece iki zaman tasavvuru yan yana kalır.

## İçeriden Dışarıya

Bu iç alan, hemen önceki kapanma imgeleriyle daha uzun bir bedenî güzergâha yerleşir. 17:45'teki dış {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde} engeli kurar; 17:46'da kalpler üzerindeki örtüler ile kulaklardaki ağırlık duyusal kapanmayı, arkalarını dönme ise bedensel geri çekilmeyi kurar: {ar:عَلَىٰ قُلُوبِهِمْ أَكِنَّةً, tr:ʿalā qulūbihim akinnatan, gloss:kalpleri üzerine örtüler}, {ar:وَفِي آذَانِهِمْ وَقْرًا, tr:wa-fī ādhānihim waqran, gloss:kulaklarında ağırlık} ve {ar:وَلَّوْا عَلَىٰ أَدْبَارِهِمْ نُفُورًا, tr:wallaw ʿalā adbārihim nufūran, gloss:uzaklaşarak arkalarını döndüler}. Bu katkılar, 17:51'deki anatomik {ar:فِى صُدُورِكُمْ, tr:fī ṣudūrikum, gloss:göğüslerinizde} ile buluşunca iç mekânı aynı beden içinde belirginleştirir. {ar:صَدْر, tr:ṣadr, gloss:göğüs} için aktarılan eylemin çıktığı yeri ya da zamanını anlatan ayrı kullanım da güzergâha sözün çıkış imgesini ekler: kapanmış algıdan sonra itiraz göğüste biçimlenip söz olarak oradan çıkıyormuş gibi duyulur. {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} ve {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} biçimleri bu imgeyi ayrı ayrı harekete geçirir; bu sözlük yolu göğsün anatomik anlamını değiştirmez.

Göğüs adındaki ikinci çoğul iyelik eki {ar:صُدُورِكُمْ, tr:ṣudūrikum, gloss:göğüslerinizde} iç sahneyi tek bir kişiye değil hitap edilen gruba yayar; hitap edilen çoğuldan üçüncü çoğul konuşanlara geçiş de {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} ve {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} ile içeride büyüyen itirazı işitilen söze taşır. Yaratma kudretinin eyleyeni bu bedensel çıkış yerinden ayrıdır: {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} ilk-var-etme cevabında gerçek var etme kudretini önceki faile bağlar; {ar:خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:khalaqa al-samāwāti wa-l-arḍ, gloss:gökleri ve yeri yarattı} ile {ar:قَادِرٌ عَلَىٰٓ أَن يَخْلُقَ مِثْلَهُمْ, tr:qādirun ʿalā an yakhluqa mithlahum, gloss:onların benzerlerini yaratmaya gücü yeter} bu ayrımı genişletir (17:99). Bu güzergâhtaki iki başka imge grubu da ayrı katkı sağlar: {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde} ile {ar:عَلَىٰ قُلُوبِهِمْ أَكِنَّةً, tr:ʿalā qulūbihim akinnatan, gloss:kalpleri üzerine örtüler} duyuların kapanmasını kurar (17:45, 17:46); {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler}, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış parçalar}, {ar:حِجَارَةً, tr:ḥijārah, gloss:taş} ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} ise maddî sorudaki kalıntı ile sertlik karşıtlığını taşır (17:49, 17:50). Bunlar ayrı tetikleyicilerdir: ilki güzergâha duyusal kapanmayı, ikincisi maddî soruya kalıntı ve sertliği katar.

Arkalarını dönüp uzaklaşma (17:46), 17:51'de hareket ettirilen gerçek başlarla dışarıdan görülebilir hâle gelir: {ar:وَلَّوْا عَلَىٰ أَدْبَارِهِمْ نُفُورًا, tr:wallaw ʿalā adbārihim nufūran, gloss:uzaklaşarak arkalarını döndüler} imgesinin ardından {ar:فَسَيُنْغِضُونَ إِلَيْكَ رُءُوسَهُمْ, tr:fa-sayunghiḍūna ilayka ruʾūsahum, gloss:başlarını sana doğru oynatacaklar} görünür baş hareketini getirir. İçerideki itiraz böylece beden yüzeyine de ulaşır.

17:99'un sonundaki {ar:فَأَبَى ٱلظَّٰلِمُونَ إِلَّا كُفُورًا, tr:fa-abā al-ẓālimūna illā kufūrā, gloss:zalimler inkârdan başkasını kabul etmedi} açık inkâr, odaktaki jestin yanında sözlü ret işareti sağlar. Çağrıdan sonra baş çevirme (63:5), {ar:لَوَّوْا۟ رُءُوسَهُمْ, tr:lawwaw ruʾūsahum, gloss:başlarını çevirdiler} hareketiyle ona yakın bir bedensel paralel ekler; bu, iki ayrı ret sahnesi arasındaki karşılaştırmadır. 17:52'deki {ar:يَوْمَ يَدْعُوكُمْ, tr:yawma yadʿūkum, gloss:sizi çağıracağı gün} çağrısına cevap ise jestin sürmesi değil, soru-cevap alışverişine açılan ayrı bir karşılık sahnesidir. Böylece ret jesti ile çağrıya cevap konuşma önünde iki ayrı yön açar, tek bir bedenî zincir kurmaz.

## Dört Tur, İki Soru

Bu bedensel çıkış ayetin konuşma sırasını da görünür kılar. İlk {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} içindeki gelecek işareti, hemen ardından gelen {ar:مَن يُعِيدُنَا, tr:man yuʿīdunā, gloss:bizi kim geri getirecek} sorusunu önceden bildirilen ilk söz yapar. Bitmemiş IV. bâb biçimindeki {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} beklenen geri getirme eylemini sorar ama vaktini belirlemez; birinci çoğul nesne eki de soranları geri getirileceklerin arasına koyar. İlk {ar:قُلِ, tr:quli, gloss:de} buyruğu yanıtı yönlendirir; {ar:ٱلَّذِى, tr:alladhī, gloss:o ki} eyleyeni, hitap edilen çoğulu doğrudan nesne alan tamamlanmış {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} işiyle tanıtır. {ar:أَوَّلَ مَرَّةٍۢ, tr:awwala marratin, gloss:ilk defa} gerçekleşmiş, sayılabilir başlangıcı belirginleştirince “kim?” sorusu ilk var edilişe bağlanır; bu, iki söz arasındaki yerel dayanak olarak kalır.

Yanıtın ardından {ar:فَسَيُنْغِضُونَ, tr:fa-sayunghiḍūna, gloss:başlarını oynatacaklar} baş hareketini öngörür. Gelecek zamanlı IV. bâb ettirgen fiil doğrudan {ar:رُءُوسَهُمْ, tr:ruʾūsahum, gloss:başlarını} nesne alır; {ar:إِلَيْكَ, tr:ilayka, gloss:sana doğru} yönü vererek hareketi soyut bir duruştan çıkarıp konuşulan kişiye yönelen gerçek baş jesti yapar. Fiilin alışılmadık, sesçe belirgin kullanımı sallama, oynatma ve kararsız hareket arasında bir aralık bırakır; bu ses jestin hareket niteliğini belirginleştirir, gizli anlamını tek başına belirlemez. Jestin duygusu hayretle reddediş arasında açık kalır. Hemen önceki {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} ve hemen sonraki {ar:مَتَىٰ هُوَ, tr:matā huwa, gloss:o ne zaman} soruları dönüş ile vakit talebini jestin çevresine yerleştirir; birlikte itirazı bedenselleştirir. Bu yerel yankı kuşku ya da reddi taşıyabilir, beklenen dönüşün gerçekleşeceğini ispatlamaz; baş burada fiziksel baştır.

Jestin ardından ikinci {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} biçimi sözü yeniden başlatır: beden hareketi işitilen {ar:مَتَىٰ هُوَ, tr:matā huwa, gloss:o ne zaman} sorusuna geçer. İlk söyleyişteki {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} gelecek işareti ikinci söyleyişten önce yinelenmez; bu yerel fark ikinci sözün her bakımdan öngörüsüz olduğunu göstermez. {ar:هُوَ, tr:huwa, gloss:o} aradaki soru ve cevapla konuşmada öne çıkan dönüş olayına döner, adını yeniden söylemez. Ardından gelen ikinci {ar:قُلْ, tr:qul, gloss:de} buyruğu zaman sorusuna yanıtı yönlendirir. İlk emrin sonraki söze bağlanan {ar:قُلِ, tr:quli, gloss:de} ses biçimiyle ikincinin yalın {ar:قُلْ, tr:qul, gloss:de} biçimi arasındaki fark ses çevresindedir; iki buyruk aynı yönlendirme işini görür.

İki soru, “demek” anlamındaki söyleyişleri karşılıklı konuşmaya da yaklaştırır. {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler}, {ar:قُلِ, tr:quli, gloss:de}, {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} ve {ar:قُلْ, tr:qul, gloss:de} biçimlerinin sözlük alanındaki karşılıklı konuşma kullanımı, soru-cevap sırasına bir müzakere yankısı verir: “kim?”den “ne zaman?”a değişen iki soru, aradaki cevaplar ve 17:52'deki {ar:يَوْمَ يَدْعُوكُمْ, tr:yawma yadʿūkum, gloss:sizi çağıracağı gün} çağrısıyla {ar:فَتَسْتَجِيبُونَ بِحَمْدِهِ, tr:fa-tastajībūna bi-ḥamdih, gloss:O'na hamd ederek karşılık vereceksiniz} karşılığı bu yankıyı harekete geçirir (17:52). Dönüş meselesi ortak kalırken soru ekseni değişir; bu okuma tarafların eşit yetkide ya da uzlaşmış olduğunu göstermez. “Söylemek” için aktarılan “varsaymak” kullanımı da iki itirazda varsayımsal bir direnç duyurabilir; sorular ise gerçek soru niteliğini korur. Daha geniş lehçe örnekleri bulunduğundan, bu temas bağlamsal bir kullanım olasılığıdır, katı biçim kuralı değil.

Bu sözlü alışverişin yanında biçimce uzak, başka bir kök altında kaydedilmiş “oynatmak, kararsızca sallanmak” kullanımı belirir. Olağan “demek” anlamını taşıyan {ar:فَسَيَقُولُونَ, tr:fa-sayaqūlūna, gloss:böylece diyecekler} ve {ar:وَيَقُولُونَ, tr:wa-yaqūlūna, gloss:ve diyecekler} biçimleri, açık {ar:فَسَيُنْغِضُونَ, tr:fa-sayunghiḍūna, gloss:başlarını oynatacaklar} hareketi ve onun {ar:رُءُوسَهُمْ, tr:ruʾūsahum, gloss:başlarını} nesnesiyle karşılaşınca bu ayrı kullanımı konuşmaya ses ve beden yankısı olarak taşır: söz sanki jestin kararsız salınımına eşlik eder. Söyleme fiilleri yine söz söylemeyi bildirir; bu yankı başka kökten gelen keşifsel bir temas olarak işitilir.

Bu soru-cevap dizisinin yanına 17:52'de çağrı ve karşılık sahnesi eklenir. {ar:يَوْمَ يَدْعُوكُمْ, tr:yawma yadʿūkum, gloss:sizi çağıracağı gün} çağrıyı başlatır; {ar:فَتَسْتَجِيبُونَ بِحَمْدِهِ, tr:fa-tastajībūna bi-ḥamdih, gloss:O'na hamd ederek karşılık vereceksiniz} soranları yanıt verenlere dönüştürür (17:52). Aynı ayette kalışın {ar:قَلِيلًا, tr:qalīlan, gloss:az} diye nitelenmesi, bekleme süresini geriye dönük kısa yaşatır (17:52). {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusundaki ayrılınan şeye dönme ya da işe yeniden yönelme kullanımı, bu çağrı-karşılık sırasına beklenen dönüş olayını ekleyebilir. Bu bağlantının yanında 17:52, ayetin yalın kronolojik devamı olarak da okunabilir.

## Yakınlığın Açtığı Ufuk

İkinci yanıt, “ne zaman?” sorusunu bir tarihle değil, {ar:عَسَىٰٓ أَن يَكُونَ قَرِيبًا, tr:ʿasā an yakūna qarīban, gloss:umulur ki yakın olsun} yapısıyla karşılar. {ar:عَسَىٰٓ, tr:ʿasā, gloss:belki ve umulur} ile başlayan {ar:أَن, tr:an, gloss:-mesi} yapısı {ar:يَكُونَ, tr:yakūna, gloss:olmak} yan cümlesini ona bağlar; {ar:هُوَ, tr:huwa, gloss:o} ile konuşmada anlaşılan dönüş olayı özne olarak sürer, {ar:قَرِيبًا, tr:qarīban, gloss:yakın} ise onun yüklemidir. Olay hareket ediyormuş gibi değil, yakın olma hâlinde sunulur. Belirsiz mansup biçim yakınlığı kesin bir noktaya bağlamaz; takvim günü sorusuna tarihsiz bir zaman cevabı verir.

Bu zaman cevabında {ar:عَسَىٰٓ, tr:ʿasā, gloss:belki ve umulur} iki aktarılmış açıklamayı birlikte taşır: ilahî bildirimde sonucun kesin sayılabileceği okuma da, kelimenin muhatapta umut uyandırdığı okuma da mümkündür. “Ne zaman?” talebi ve yakınlıkla verilen cevap bu seçeneklerden birini ötekine üstün kılmaz. {ar:قَرِيبًا, tr:qarīban, gloss:yakın} sözcüğünün geniş alanı yer ya da anlam bakımından yakınlığı da kapsar; fakat {ar:مَتَىٰ, tr:matā, gloss:ne zaman} sorusu ile modal yanıt zaman eksenini öne çıkarır, sözlükteki olay vaktinin yaklaşması kullanımı da bu bağlamda etkinleşir. Bu ayetteki yakınlık böylece zamansaldır; ilişkisel yakınlık başka bir bağlamdan gelecektir.

Zamansal yaklaşma, aynı sözlük alanındaki daha maddî bir görüntüyü de keşifsel olarak açar. Kökün bir başka kullanımı devenin köpek dişinin sürüp görünmesini anlatır; {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} ifadesinin ilk ortaya çıkarma anlamı, {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} ve sayılabilir {ar:مَرَّةٍۢ, tr:marratin, gloss:bir defa} ile yan yana gelince bu görünür olma görüntüsünü tetikler. {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusundaki ayrılınan şeye geri dönme kullanımı da henüz görünür olmayan kapasitenin yeniden belirivermesine alan açar. Dişin görünmesi ilk yaratılış anlamını değiştirmez; başlangıçla dönüş arasındaki sözcüksel yolun yanında ayrı bir organik benzetme kurar.

Beklenti dalı bu görüntüye geri-geliş ve yakınlaşma katkılarını ekler. {ar:عَسَىٰٓ, tr:ʿasā, gloss:belki ve umulur} olağan umut ve beklenti anlamını korurken, aynı sözlük alanında sütü kesilmiş ya da süt verip vermediği belirsiz bir dişiye ve kesilince sütün geri gelmesi umuduna ilişkin bir kullanım vardır. {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} ile {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} sözleri bu geri-geliş imgesini harekete geçirince, kaybolmuş ya da kesilmiş olanın yeniden belirmesi beklentinin somut bir yüzü olur. {ar:قَرِيبًا, tr:qarīban, gloss:yakın} için doğum vakti yaklaşmış gebe dişiyi anlatan kullanım da bulunur; {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} ifadesinin ortaya çıkışıyla {ar:عَسَىٰٓ, tr:ʿasā, gloss:belki ve umulur} sözünün beklentisi bu kez doğuma yaklaşmayı tetikler. Bu üç katkı farklı ayrıntıları taşır: {ar:خَلْقًا, tr:khalqan, gloss:yaratılmış şey} ve {ar:مَرَّةٍۢ, tr:marratin, gloss:bir defa} ile tetiklenen dişin görünmesi kapasitenin belirmesini; {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} ile duyulan süt dönüşü umudu geri gelişi; {ar:قَرِيبًا, tr:qarīban, gloss:yakın} sözcüğünün yaklaşan doğum kullanımı ise yakınlaşmayı somutlaştırır. Yan yana geldiklerinde, henüz görünmeyen kapasitenin geri dönüp belirmeye yaklaşması görüntüsünü kurarlar. Bu hayvanlar ayetin sahnesinde değil, sözlük benzetmesinde kalır; olağan dönüş cevabı ilk var edilişe dayanır.

17:57, zamansal {ar:قَرِيبًا, tr:qarīban, gloss:yakın} sözünün yanına ayrı bir ilişkisel yakınlık ekseni koyar. “Hangisi daha yakındır?” sorusu {ar:أَيُّهُمْ أَقْرَبُ, tr:ayyuhum aqrabu, gloss:hangisi daha yakındır} bu ekseni kurar (17:57). Rabbe {ar:يَبْتَغُونَ إِلَىٰ رَبِّهِمُ الْوَسِيلَةَ, tr:yabtaghūna ilā rabbihimu al-wasīlah, gloss:Rablerine yaklaşmaya vesile ararlar} diye yönelme bedensel mesafeyi değil, anlam ve yöneliş yakınlığını verir (17:57). Oradaki {ar:يَرْجُونَ رَحْمَتَهُ وَيَخَافُونَ عَذَابَهُ, tr:yarjūna raḥmatahu wa-yakhāfūna ʿadhābah, gloss:rahmetini umar, azabından korkarlar} umudu ve korkusu da {ar:عَسَىٰٓ, tr:ʿasā, gloss:belki ve umulur} çevresindeki beklentiye temas eder (17:57). Çağrılanların {ar:فَلَا يَمْلِكُونَ كَشْفَ الضُّرِّ عَنكُمْ وَلَا تَحْوِيلًا, tr:fa-lā yamlikūna kashfa al-ḍurri ʿankum wa-lā taḥwīlan, gloss:sıkıntıyı sizden gidermeye veya değiştirmeye güç yetiremezler} oluşu onları güçsüz gösterir (17:56); bu karşıtlık Rabbe yönelişin ilişkisel eksenini belirginleştirir. Zamansal yaklaşma ile Rabbe yakınlık yan yana duyulur, aynı ölçekte birleşmez; bu karşılaştırma ʿasā'nın kesinlik derecesini tek başına belirlemez.

Yakın vakit ufku, daha geniş zaman sorularında da tarihsiz kalır. {ar:لَعَلَّ ٱلسَّاعَةَ قَرِيبٌۭ, tr:laʿalla al-sāʿata qarīb, gloss:belki Saat yakındır} sözü 17:51'deki {ar:قَرِيبًا, tr:qarīban, gloss:yakın} cevabının yanına Saat ufkunu ekler (42:17); vaat edilen şeyin ne zaman olacağını soran {ar:مَتَىٰ هَٰذَا ٱلْوَعْدُ, tr:matā hādhā al-waʿd, gloss:bu vaat ne zaman} sözü zaman talebini yeniden açar (67:25). Odaktaki {ar:فَسَيُنْغِضُونَ إِلَيْكَ رُءُوسَهُمْ, tr:fa-sayunghiḍūna ilayka ruʾūsahum, gloss:başlarını sana doğru oynatacaklar} hareketiyle hemen ardından gelen {ar:مَتَىٰ هُوَ, tr:matā huwa, gloss:o ne zaman} sorusu bedensel ve sözlü meydan okumayı birlikte duyurur. 63:5'te başların çağrıya karşı çevrilmesi ({ar:لَوَّوْا۟ رُءُوسَهُمْ, tr:lawwaw ruʾūsahum, gloss:başlarını çevirdiler}) bu jest için yakın bir bedensel paralel, 67:25'te vaat hakkında sorulan söz ise ayrı bir sözlü meydan okumadır. Bu bağlamlar yaklaşan vakti geniş duyurur, belirli bir gün vermez.

17:52'deki {ar:يَوْمَ يَدْعُوكُمْ, tr:yawma yadʿūkum, gloss:sizi çağıracağı gün}, Fâtiha 1:4'teki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi al-dīn, gloss:hesap ve karşılık gününün sahibi} ile birlikte düşünüldüğünde, 17:51'in {ar:قَرِيبًا, tr:qarīban, gloss:yakın} cevabı hesap ve karşılık ufkuna doğru da duyulabilir. Çağrı günüyle hesap günü arasındaki bu temas dış bağlamın açtığı bir okumadır: 17:51 yaklaşanı kendi içinde yargı günü diye adlandırmaz ve Fâtiha'nın bütünü hakkında bir sav kurmaz. Yakınlık cevabı tarihsiz kalırken, 17:52'nin çağrı günü hesap ufkunu yanında taşır (1:4).

</source_prose>
