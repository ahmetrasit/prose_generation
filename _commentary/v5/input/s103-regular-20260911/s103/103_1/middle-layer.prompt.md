# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **103:1**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.middle.claims.json`

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
- Refer to source paragraphs as `103:1 ¶N`.

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

After the first complete prose draft, compute the ledger metrics and return to
this clustering stage for a mandatory diagnostic pass when the source has at
least ten prose paragraphs and any of these warning signals appears:

- `retained_word_ratio` is greater than `0.80`;
- `output_to_source_paragraph_ratio` is greater than `0.75`;
- fewer than `0.40` of the output prose paragraphs are multi-source paragraphs.

These are review triggers, not compression targets, quality scores, or
validator limits. Do not shorten until a number crosses a boundary. A
semantically irreducible commentary may remain beyond one or all of these
signals after the required pass.

For that pass, challenge every repeated setup, recap, defensive qualification,
and run of single-source paragraphs that develops the same carrier, question,
image, mechanism, or consequence. Privately draft the best continuous merged
formulation, then compare it unit by unit with the current version. Adopt the
merge only when every distinct unit still has an explicit substantive landing,
every modality and boundary remains visible, citations remain locally
meaningful, and the Turkish becomes easier rather than merely shorter. If the
merge fails any test, keep the material separate and give the relevant
standalone clusters concrete semantic non-merging reasons. Never delete,
generalize, or bury a unit merely to improve a diagnostic metric.

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

`(103:1 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "103:1",
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
        "citation": "(103:1 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s103-regular-20260911/s103/103_1/103_1.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s103-regular-20260911/s103/103_1/103_1.middle.claims.json \
  --ayah-ref 103:1
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s103-regular-20260911/s103/103_1/103_1.prose.editorial.tr.md`

<source_prose>
## Yemin Edilen Zaman

Âyetin açık anlamı şudur: Zamana yemin olsun. Başındaki {ar:وَ, tr:wa-, gloss:yemin edatı}, ardından gelen {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesini yemin çerçevesine alır; ilk ses burada önceki bir söze bağlanan sıradan bir “ve” gibi değil, bir tanık çağrısı gibi iş görür. Yemin etme fiili ayrıca söylenmediği için iki kelime, sıkıştırılmış bir açılışta yemin eylemini birlikte taşır. Cevap hemen gelmez: bu başlangıç, gelecek sözün neyi açıklayacağını bekleten bir nefes aralığı açar. {ar:وَ, tr:wa-, gloss:yemin edatı}nın kendisine bağımlı ön ek olarak {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit}a yazıda ve seste yapışması da yemin ilişkisini açıklanmadan önce tek ve sıkı bir birim hâline getirir.

Bu birimin zaman alanını nasıl topladığı, {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin biçiminde görünür. Başındaki “el-” belirli artikeli, tekil oluşu ve soyut isim yapısı birlikte çalışarak herhangi bir anı saymak yerine devir, çağ, vakit veya günün belirli bir geç bölümünü tek bir yemin alanında toplar. Sonundaki çekim, kelimeyi olayın ne zaman olduğunu bildiren bir zarf olmaktan çıkarıp yeminle çağrılan nesne ve tanık konumuna yerleştirir. Bu isim biçimi, sıkma ya da işlem bildiren biçimlerden ayrılarak burada zamanı adlandırır. Bu biçimin taşıdığı açık okuma belirli bir zaman kesitine edilen yemindir; cümle, ikindi namazını veya gecikmiş bir gelişi ayrıca seçmeden zamanın tanıklığını açık ve geri dönülebilir bırakır.

Bu kısa yüzeyin sesi de tanığı yoğunlaştırır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} içindeki sıkı ünsüz akışı ve kısa kapanış, sözü genişletmeden bir arada tutan kapalı bir ses etkisi verir; yardımcı ünlülerle değişen telaffuzlar, akışın nasıl gevşeyebileceğini karşılaştırmalı olarak duyurur. Başka bir seslendirmede görülen {ar:وَالْعِصْرِ, tr:wa-l-ʿiṣri, gloss:bağ veya ahit çağrışımı}, küçük bir ses değişiminin bağ ya da ahit yönünü açabildiğini gösterir; alınmış {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} biçiminin zamansal yemin alanı ise yerinde durur. Genişletilmiş, alışılmadık bir ifade zamanın darbelerini açıkça dile getirirken, bu kısa biçim aynı baskı hissini tek bir isimde katlı tutar.

Bu baskı renginin kaynağı, aynı kelime ailesinde sıkma, yağmur üretimi ve döner rüzgâr için görülen kullanımlarda belirir. Zaman, içinde bulunanı bastırıp ondan öz, pay veya sonuç çıkaran; böylece verimi ve verimsizliği görünür kılan bir alan gibi hissedilebilir. Yerel biçim soyut bir zaman adı olarak kaldığı için pres, sıvı ve ürün görüntüsü bu bağlantıda zamanın içinden sonucu görünür kılan yorumlayıcı renklere dönüşür. Yemin edatı tanığı çağırır, belirli tekil isim zamanı bütünlük hâlinde toplar, aileden gelen basınç bu alanı sınayıcı kılar, ses de yoğunluğu işitilir hâle getirir. Sıfat veya açıklama almadan tek başına duran son isim, yemin çerçevesini sınırda asılı bırakır; açılışın bütün ağırlığı tek tanığın üzerinde toplanır.

## Tanıklığın İçinden Geçen İnsan

İsim tek başına askıda kaldığı için okuyucu, bu zaman alanının hangi hayatı görünür kılacağını bekler. 103:3'te iki kez geçen {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:karşılıklı öğütleştiler} ile temas kurulduğunda bekleyiş bir akışa dönüşür: iki öğüt, bir aralığın ötekine eklenmesini ve bir sonraki parçaya geçmesini düşündürür. 103:2'deki kayıp ile 103:3'teki istisna da bu çerçevede yemin dışından getirilmiş iki tablo gibi değil, yeminle açılan zaman içinde ilerleyen bir ilişki gibi duyulur. Değişim ve dönüş, geçen zamanı içinden geçenleri tekrar tekrar açığa çıkaran bir tanık hâline getirir.

Bu tanıklığın insan yüzü 103:2'deki {ar:إِنسَٰنَ, tr:insân, gloss:insan} kelimesiyle belirir. İnsan burada yalnızca kayıp cümlesinin öznesi olarak kalmaz; görme, duyma veya sezme yoluyla fark eden, göz bebeğinde beliren bir suret gibi de düşünülebilir. Böylece zaman dışarıdan olaylara bakan soyut bir seyirci olmaktan çıkar, insan hâlinin içinde belirginleştiği bir alana dönüşür. İnsan eylemlerini kayda geçiren meleklerle ilgili temas (82:10) ve başka bir zamansal yemin (93:1), bu alanı davranışın yönünü görünür kılan bir kayıt gibi açar. Dünya hayatının büyüme, solma ve yok oluş döngüsünü karşılaştıran (57:20) temas ise zaman içinde biriken kaybı ölçülebilir kılar. 45:24'te dehrin helaki kendi başına yapan fail gibi gösterildiğinde buna karşı çıkan söz, zamanı işleyen bağımsız bir özne yerine yorumlayıcı bir tanıklık alanı olarak tutar.

Tanığın gösterdiği şey, yalnızca geçen süre değil, o sürede neyin çıktığıdır. 103:3'teki {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} ile buluşan ürün veya kazanç yönü, çalışan bir topluluğun malzemeye el vermesini ve emeğin ürüne dönüşmesini düşündürür. Karşılığını alan işçinin geçim payı da bu dönüşe eklenir; 103:2'deki {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} ise çıktının eksik kalan tarafını yanında tutar. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:hak} bu dönüşe bir ölçü getirir: iş veya ürün, birinin hak ettiği ve borçlu olunan bir paya bağlanır. Yağmur basıncını ve üretken bir döngüyü birlikte düşündüren (78:14, 12:49) temaslar, zamanın hayat içinde ne üretildiğini sınayan bir aralık gibi duyulmasına yardım eder. Bu emek, ücret ve karşılık görüntüsü ayeti genişletir; işçi, sözleşme ve ticari taraflar bu bağlantının bağlamsal ayrıntıları olarak kalır, ayetin açık yüzü ise belirli zamana edilen yemin olarak durur.

Ürün ortaya çıkmadan önce korunarak gelişir. {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:düzgün ve ıslah edici işler} ile yan yana gelen ürün yönü, başağın kılıfı içinde tutulan şeyi görünür kılar. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} burada pasif bekleyişten ayrılan niyetli ve yönelmiş çalışmayı taşır; eldeki malzemeye yapılan iş, ürünün oluşmasına katılır. İşin karşılığı ve işçinin geçim payı, yetiştirmenin emeği destekleyen bir dönüşe bağlanır. {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:düzgün ve ıslah edici işler} bozulmanın karşısına sağlamlık, onarma ve eylemin amacına uygun düşme ölçüsünü koyar. Zamanın ürün alanı böylece emek, uygunluk ve korunma içinde gelişen bir verime açılır.

Bu gelişme, zamanın yalnız yaş sayan bir cetvel olmadığını da düşündürür. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin genç kızın çocukluktan ergenlik eşiğine ulaşmasını anlatan yönü, 103:3'teki iş ve sağlamlıkla buluştuğunda işe yarar bir işleve ulaşma aralığı belirir. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:hak} içindeki görüntü, taşıma veya çiftleşme yaşına varıp beklenen işi kaldırabilecek deveyi; aynı kelimenin başka bir yönü, atın adımını denk tutmasını veya bedenen sertleşmesini hatırlatır. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} bu eşiği görünür davranışa ve iş görmeye yatkınlığa bağlar; {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:düzgün ve ıslah edici işler} kapasitenin bozulmadan ve yerli yerinde oluşmasını taşır. Bu gelişme alanı ergenlik eşiğini, hayvanın taşıma yaşını, denk adımı ve sağlam iş görmeyi aynı zaman aralığında canlı tutar; okuma böylece tek bir biyolojik olaya kapanmaz.

Korunmuş ürünün sonraki hâli 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} kelimesinin üst, kenar ve sınırla ilgili görüntülerinde açılır. Başağın kılıfı gelişen şeyi ilk aşamada sarar; geniş bir sergi veya sofra yüzeyi, yığın ve dolmuş kenar ise onu tutulabilir bir erzak hâline getirir. Ürün böylece kapalı gelişmeden sınırı görülen bir birikime doğru ilerler. Bu hareket, zamana edilen yeminin yanında duran ürün ve saklama görüntüsünü somutlaştırır.

Ürünün bir başka yüzü, aynı 103:3 bağlamındaki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} çevresinde beliren ekşi meyve ve acı ilaç özsuyudur. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin yalın bir ağaç kullanımıyla birleşen bu temas, yalnız yiyecek veren değil, tadı zor fakat tedavi edici bir özsuyu da çıkaran canlı bir kaynak düşündürür. Ekşi, buruk meyve ve kırmızı çekirdek görüntüsü bu kaynaktan gelen ayrı bir ürünü belirginleştirir; ekşilik ile acılık aynı bitkisel kaynaktan çıkan ürünleri birbirinden ayırır. Burada taşınan ayrıntı ağacın varlığı ve ürün çeşitliliğidir; ağacın türü, görünüşü ve kesin botanik kimliği açık bırakılır.

## Ölçülen Çıktı, Tutulan Pay

Sıkma görüntüsü 103:2'deki eksik ölçü ve kayıpla birleştiğinde, zamanın içinden çıkarılan sonuç ölçülebilen bir basınç ürünü gibi görünür. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin bastırıp öz çıkaran yönü, {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} kelimesinin soyut eksilmesini eksik doldurulmuş bir miktara çevirir; 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} yığını bu miktara görünür bir kütle verir. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} kelimesinin bir aracı veya şeyi işe koşma yönü, basıncın bir işleme sokulmuş malzeme üzerinden gerçekleştiğini düşündürür. Biriktirmenin insanı oyalayıp tükettiğini hatırlatan (102:1) ve tartıyla başarı ile kaybı ayıran (7:8) temaslar, beklenen getiri ile elde edilen miktarı karşılaştırır. Eksik teslim böylece görünür, kayıp da yalnız bir duygu olmaktan çıkıp bastırılmış ve ölçülebilen bir sonuç hâline gelir.

Bu ölçü, değerin dolaşıma girip geri dönmesi olarak da duyulur. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin elde edilen ürün veya getiri yönü, ortaya konan değerin korunmuş bir değer ya da zararla geri dönmesini bekleyen bir dönüş açar. 103:2'deki {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} bu değerin kazanca dönüşmeyen tarafını, 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} ise sert taşlı zeminde zor çıkarılan dönüşü hissettirir. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:hak} bu dönüşü belirli bir sahibin alacağına bağlar; acı ilaç özsuyu da bu zorluğa hoş olmayan fakat işe yarayabilecek bir tat ekler. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} işi insanlar arasındaki alışveriş ve riskle yan yana getirir. Bu ticari ve duyusal görüntü, beklenen dönüşü somutlaştıran bu bağlantının sınırında kalır; ayetin asli adlandırması yine zamandır.

Sıkma alanı kaybın yönünü de belirginleştirir. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin alıkoyma, geri alma ve elde tutma yönü, bir yararın dolaşıma girmesi gerekirken tutulmasını, geri çevrilmesini veya karşı tarafa ulaşmadan kesilmesini düşündürür. 103:2'deki {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} bu işlemin azalttığı kalanı gösterir; kısa ölçü görüntüsü beklenen miktardan eksilen parçaya sınır çizer. 103:3'teki {ar:ٱلْحَقِّ, tr:el-hakk, gloss:hak} ise bunun karşısına borçlu olunan ve sahibine ait payı koyar. Zaman, eksik ölçüyü ortaya çıkaran ve birinin hakkına ait olan şeyi geri çağıran bir hesap aralığı gibi düşünülebilir. Bu hesap görüntüsü failini ve olayın ticari ya da hukuki biçimini belirlemeden, eksiklik ile hakkı aynı zaman çerçevesinde görünür kılar.

Ürün, ölçü ve hak arasındaki gerilim, kaybın içinden çıkabilecek iyi sonucu da açık bırakır. Uyarının ardından kurtuluşu düşündüren (10:103), birikmiş ürünün açığa çıkışını gösteren (12:49) ve sonucu tartıyla görünür kılan (7:8) temaslar, {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesindeki baskıyı birine ulaşan iyiliği, bir kaynaktan çıkan payı veya işlenmiş ürünü açığa çıkaran bir sınama gibi duyurur. Birikim insanı oyalayıp tüketirken, bastırılan süreç neyin gerçekten çıkarıldığını ve neyin karşılıksız kaldığını ayırır. Böylece kayıp tek başına bırakılmaz; değerlendirilebilir bir yarar ve sahibine ulaşan pay ihtimali onun yanında belirir. Bu katkı, zaman kelimesinin asli adlandırmasını korurken kaybın tek sonuç olmasını düzeltir; teknik muhasebe ve ticaret, yalnızca bu bağlantıyı açıklayan bağlamsal görüntüler olarak kalır.

## Aidiyet ve Sığınma

Ölçülen eksik yalnızca maddi bir miktar olarak kalmaz; insan ve toplulukla birleştiğinde sosyal bir süreklilik de kazanır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin soy kökü ve köken yönü, 103:2'deki insanla 103:3'teki topluluk arasında bireysel ömrü aşan bir aidiyet zinciri düşündürür. İnsan, görünür varlık olarak gizli veya yabanıl olanın karşısında bu zinciri taşır; {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} kelimesinin topluluk adı gibi duyulan yönü ona kolektif bir beden verir. Bağlılar arasındaki göreli alt konumla ilgili temas, bu zincirde farklı mevkilerin bulunduğunu gösterir; bu, genel bir değersizlik hükmü değildir. Zamanın tanıklığı böylece köken, topluluk ve bağlılık içinden geçen bir sosyal sürekliliği görünür kılar.

Buna yakın fakat ayrı bir görüntüde {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} soylu kökeni, 103:2'deki insanı yakın bir öz veya yoldaş; {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} ise miras alınmış bir topluluk veya klan gibi düşündürür. Burada vurgu, bağlılar arasındaki alt konumdan çok, kişinin ortak bir köke ve seçkin bir soya yerleşmesindedir. İnsan kelimesinin yakınlık ve kişinin kendi çevresi görüntüsü bu mirası soyut bir soyağacından yaşanan bir aidiyete taşır; klan, bireyin çevresindeki kalabalığı ve miras alınan duruşu tamamlar. Bu görüntünün katkısı ortak köke yerleşen bir aidiyeti görünür kılmaktır; evrensel üstünlük iddiası taşımadan, köken ve topluluk temel zaman tanıklığının yanında ayrı bir sosyal okuma olarak kalır.

Aidiyetin yanında baskı altında dayanılacak bir yer de belirir. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin tutunarak sığınma ve kurtuluş arama yönü, 103:3'teki {ar:ءَامَنُوا۟, tr:âmenû, gloss:güvene erdiler} ile buluştuğunda aynı zaman alanında bir güvenlik bölgesi açar. Güven, kalbin emniyet içinde yerleşmesini ve tutunmanın korkuyla savrulan bir kavrayış yerine güvenilen bir dayanak olmasını sağlar. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} kelimesinin birinin yanında durma ve kefil olma yönü, sığınağı ilişkiye açar; korunma, bir kişi veya grubun yanında durmasıyla sürer. Karşılıklı iyilik ve sabrı hatırlatan (90:17), uyarı sonrasında kurtuluşu gösteren (10:103) ve kendine yeterlik yolunda alıkoymayı düşündüren (92:8) temaslar bu dayanmayı belirginleştirir. Güvenlik burada dışarıdan hazır bir nesne değil, baskı altında tutunulan ve kaybolmaması için elde tutulan bir imkândır.

Bu sığınma, imanın güven veren ve tasdikle kalbi yatıştıran yönüyle daha dar bir biçimde de açılır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin tutunarak kurtuluş arama yönü, güvenilen bir dayanağa bağlanır; {ar:ءَامَنُوا۟, tr:âmenû, gloss:güvene erdiler} bu bağlanmayı ürkek bir kavrayıştan emanet edilmiş bir karara çevirir. Bu ikinci katkı, topluluk içinde yanında durma görüntüsüne iç huzur ve güvenilir karar boyutunu ekler; iki katkı aynı sığınma alanında ayrı hareketler olarak kalır. (90:17, 10:103) ile açılan kurtuluş imgesi burada acı bir ilaç veya tıbbi tedavi önermek için değil, sıkışmış alandan çıkışın niteliğini görünür kılmak için çalışır.

Yemin çerçevesi alıkoyma ve insan görüntüsüyle birleştiğinde daha sert bir tutulma sahnesi de açılır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} burada insanı sabitleyen bir zaman aralığı, {ar:وَ, tr:wa-, gloss:yemin edatı} ise sözü bağlayan bir başlangıç gibi duyulur. 103:2'deki {ar:إِنسَٰنَ, tr:insân, gloss:insan} bu tutulmanın bedensel hedefini veren görünen varlık olarak belirir; 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} kelimesinin zorla tutma veya ettirilmiş yemin yönü, bedeni yerinde tutma ve konuşmayı dış baskı altında sabitleme görüntüsünü ekler. Bu ihtimal yemin cümlesini gerçekten zorla ettirilmiş bir söz diye hükme bağlamaz; olağan zaman yeminine, tutulmuş beden ve baskı altında sabitlenmiş sözün sınırlı yankısını ekler.

İki kez gelen {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:karşılıklı öğütleştiler}, sığınağı tek kişinin tutunmasından kişiler arasında gidip gelen bir aktarıma çevirir. Zaman ardışık aralıkları, sığınma taşınan güveni, karşılıklı öğüt ise aktarımın iki yönünü sağlar: bir kişi ötekine bağlanır, sonra destek geri döner. Tek yönlü emir yerine iki temas noktasının tekrarlanması, güvenli alanı birlikte kurulan bir dayanışma gibi düşündürür; 90:17, 10:103 ve 92:8'deki öğüt, kurtuluş ve alıkoyma temasları bu hareketi destekler. Tekrarın yalnızca iki görevi güçlendiren bir yapı olarak kalması ihtimali de bu görüntünün yanında açıktır.

Bu karşılıklı aktarım basınçla birleştiğinde, içerideki kuvveti taşıyan bir kap görüntüsü belirir. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin bastırıp öz çıkaran yönü, {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:karşılıklı öğütleştiler} ile paylaşılmış bir tutulma işlemi gibi duyulur; yük tek kişinin omzunda kalmaz. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} kelimesinin içten kendini tutma, şişe veya kuyunun tıpası gibi duyulan yönleri, içerideki şeyin gerilim altında dışarı kaçmasını engelleyen bir sınır verir. Basınç, bu sınır sayesinde taşkınlığa değil verime doğru tutulabilir. Kap görüntüsü, sabrın kuvveti paylaşarak ve sınırda tutarak taşımasını anlatan ihtiyatlı maddi bir benzetme olarak çalışır.

## Salınan ve Savrulan Kuvvet

Tutulan kuvvetin bedendeki karşılığı, bir kerede aşılması zor bir sıkışmanın küçük ve tekrarlanan rahatlamalarla geçmesidir. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin boğaza takılan lokmayı küçük yudumlarla geçirme yönü, kurumuş dilin ve susuzluğun bedensel darlığını görünür kılar. Acı ilaç özsuyu rahatlamanın hoş olmayan fakat işe yarayabilecek bir araçla gelmesini ekler; 103:3'teki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:karşılıklı öğütleştiler} ise yudumları tek seferlik bir kurtarıştan kişiler arasında tekrarlanan bir aktarım hâline getirir. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:hak} bu küçük aktarımın gerçeklikle örtüşen sabit içeriğini, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} ise panikten kendini alıkoyan temposunu taşır. Böylece sıkışan şey, gerçeklik ve ölçülü dayanma küçük dozlar hâlinde geldikçe geçebilir. Bu bedenî görüntü keşifsel bir benzetmedir; öğüdün kelime anlamını küçük dozlar hâlinde vermek üzere genişletmez.

Basınç birikmiş olanı salıverme biçimi de kazanır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} yağmur taşıyan ve yağışını boşaltmaya hazırlanan bulut görüntüsüyle, biriken nemin hayat veren bir yarara dönüşebileceği bir kutup açar. (78:14) yağmur ile basıncın kesiştiği malzeme benzetmesini sağlar; 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} ise beyaz ve kat kat bir bulut gibi üst üste biriken kütleyi düşündürür. Birikimden sonra yağmurun boşalması, sıkışmış kuvvetin faydaya salınmasını görünür kılar. Aynı yağmur imgesi, ekinin kılıfları içinde korunması ve büyümenin ardından ani azalma temasıyla (78:14, 10:24) birleştiğinde, baskı alanı ürünü olgunlaşana kadar tutan, sonucunu ise hasada veya kayba açık bırakan koruyucu bir döngü gibi görünür. Bu hava ve büyüme görüntüsü, zaman yeminine gecikmiş verim ve salıveriş duygusu ekleyen sınırlı, keşifsel bir yankıdır; bulut ve büyüme ayrıntıları bu bağlantının içinde kalır.

Bu dört katkı aynı odakta buluştuğunda, her biri kaybın içinden çıkan ayrı bir şeyi taşır. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin kaydı ve yinelenmesi, bastırılan süreçte ürün ile açığı ayırır. Basınç, birine ulaşan iyiliği veya bir kaynaktan çıkan payı içinden çıkarıp görünür kılar; yağmur imgesi, birikmiş faydanın salınacağı boşluğu açar. Tutunma ve karşılıklı öğüt ise kaybolmaması gereken şeyi ilişki içinde elde tutar. (82:10, 93:1, 78:14, 12:49, 90:17, 10:103) bu temasları desteklerken, biriktirme ve tartı ilişkileri (102:1, 7:8) neyin çıkarıldığı ile neyin karşılıksız tüketildiğini keskinleştirir. Böylece 103:3'teki istisna, açığı inkâr ederek değil, baskı içinden bağlılık ve değerlendirilebilir bir iyi sonuç çıkararak kaybın tek sonuç olmasını düzeltir. Bu katkılar, asli zaman yemini ve her görüntünün kendi kapsamını koruyan yorumlayıcı ilişkilerdir; ticari ölçü ve bulut, kelimenin doğrudan karşılığına dönüşmez.

Basınç yıkıcı bir biçim de alabilir. {ar:ٱلْعَصْرِ, tr:el-ʿaṣr, gloss:devir ve vakit} kelimesinin rüzgârın kaldırdığı, döne döne sütun gibi yükselen toz görüntüsü, ekili büyümeyi vuran ateşli döner rüzgâr sahnesiyle (2:266) yan yana gelir. Kuvvet yetiştirilen şeyi de savurup kaybı görünür kılabilir; çıkarma, salıverme, sığınma ve tutma imgelerinin yanında bu yan basınç, olgunlaşanın korunmasının her zaman sonuçlanmadığını duyurur. Bu yıkıcı katkı, kelimenin biçimini rüzgâr adına genişletmeden, zamana edilen yeminin içinde açılan keşifsel bir ihtimal olarak tamamlanır.

</source_prose>
