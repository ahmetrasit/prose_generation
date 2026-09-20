# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:49**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.middle.claims.json`

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
- Refer to source paragraphs as `17:49 ¶N`.

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

`(17:49 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:49",
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
        "citation": "(17:49 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_49/17_49.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_49/17_49.middle.claims.json \
  --ayah-ref 17:49
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_49/17_49.prose.editorial.tr.md`

<source_prose>
## Alıntının Kurduğu Koşul

Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} doğrudan {ar:قَالُوا, tr:qālū, gloss:söylediler} fiiline bağlanarak alıntıyı önceki söylemin devamına yerleştirir. Hemen önceki örnekler ve düşünsel çıkmaz (17:48) bu devamın yakın zeminini oluşturur. Bağ, söylemler arasında süreklilik kurar; hangi iddianın devralındığını ve hangi yanıtın beklendiğini açık bırakır. Anlatıcı topluluğu “onlar” diye aktarırken alıntıdaki {ar:كُنَّا, tr:kunnā, gloss:olduğumuzda} aynı topluluğu birinci çoğul özne, “biz” olarak konuşturur. Tamamlanmış fiille kaydedilen söz kamusal bir beyan olarak işitilir; aktarımın süresi ve özel güdüsü belirtilmez.

Bu doğrudan söz iki basamaklı bir soruya dönüşür. {ar:أَءِذَا, tr:a-idhā, gloss:ne zaman olduğunda} koşulu açar, {ar:أَءِنَّا, tr:a-innā, gloss:gerçekten biz mi} ise kemik hâlinden kalıntı hâline uzanan öncülü yenilenmiş yaratılışın sorusuna bağlar. {ar:كُنَّا, tr:kunnā, gloss:olduğumuzda} fiil ailesinin bulunma, gerçekleşme ve ortaya çıkma kullanımları bu maddi durumlarla temas eder; burada konuşanların bu hâlde bulunmasını bildirir, dışarıdan oldurma eylemi kurmaz. Mâzî biçimi oluşu tamamlanmış bir noktadan düşündürür; tek başına çürümenin ne zaman ya da ne kadar sürede gerçekleştiğini belirlemez. Böylece çürüme, ayetin ayrı bir bildirimi olarak değil, konuşanların soruda kurduğu öncül olarak kalır.

İlk öncül, kemik anlamındaki {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler}ı belirtme hâlli yüklem yapar: topluluk “kemik hâlindeydik” der. Kırık çoğul, kemikleri sayılabilir maddi parçalar olarak gösterir. Yanındaki kalıntı sözcüğü, bu noktada büyüklük yankısından çok somut iskelet çerçevesini belirginleştirir. Kalın ẓ sesi, kemiklerin sertlik ve dayanıklılık imgesiyle işitsel olarak da uyuşur.

Bu iskelet çerçevesine aynı bağ-fiilin yönettiği ikinci belirtme hâlli durum eklenir: {ar:وَ, tr:wa, gloss:ve} + {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}. {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}, kırılıp ufalanmış kalıntıları adlandırır; sayılabilir kemiklerden kütle gibi duyulan bir artığa geçiş, iki imgeyi birikimli bir çözülme tablosunda buluşturur. Dilbilgisi bu iki durumu aynı bağ-fiil altında yan yana tutar, dolayısıyla ardışıklık mümkün olsa da zorunlu bir zaman çizgisi kurmaz. Kalıntı adı maddenin türünü belirlemez; artığın yalnızca toz olduğunu ya da her parçanın sınırının silindiğini de gerektirmez. {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler}daki sert ẓ’nin ardından {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}ın daha yumuşak, yayılan sesi gelir; koşul bu noktada kapanırken ikinci soru öncülden sonuca geçer.

İkinci sorunun ağırlığı, hemen ardından gelen {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} yükleminde toplanır. {ar:أَءِنَّا, tr:a-innā, gloss:gerçekten biz mi} içindeki soru hemzesi ve pekiştirme, birinci çoğul “biz”i bu yüke yöneltir; böylece önceki zaman koşulunun sonucu açıkça sorulur. Dilbilgisel olarak {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecekler}, {ar:إِنَّا, tr:innā, gloss:gerçekten biz} yapısının edilgen yüklemidir; ardından gelen {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış} bu kaldırılma hâlini yeni yaratılış olarak özelleştirir. Yüklemin başındaki {ar:لَ, tr:la-, gloss:pekiştirme lâmı}, edilgen {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecekler} ortaçtan hemen önce bitişir. Lâmın başlangıçtaki vurgusu ile çoğul ortaçtaki uzun ses, diriltilme yüklemini işitmede belirginleştirir; böylece pekiştirme sorunun ağırlığını tam bu yüklemde toplar.

Edilgen çoğul, bütün topluluğu kaldırılma eyleminin alıcısı yapar; fail dilbilgisel olarak belirtilmez, bu yüzden yüklem yapanı adlandırmadan eylemi alan tarafı öne çıkarır. Sözcük ailesindeki dış etkiyle uyandırma ya da kaldırma kullanımı, kemik ve kalıntı durumlarının ardından hareketsizlikten etkinliğe geçiş imgesi ekler. Bu bağlantıda yeniden etkinleşme, konuşanların sorusundaki maddi diziye eşlik eder; failin varlığı hakkında olumsuz hüküm vermez. Yüklem burada bir görev ya da varış yeri belirtmez; bu okumaya kattığı şey hareket ve etkinliktir.

Sözü aktaran fiilin olağan karşılığı “dediler”dir. Soru kuruluşlarında görülen daha sınırlı “varsaydılar” yönü, burada yan yana duran iki soruyla birlikte düşünülebilir: konuşanlar çürüme öncülünden yeni yaratılış sonucuna geçişi sorgular. Bu soru biçimi söz konusu ihtiyatlı varsayım okumasına alan açar; fiilin genel anlamını değiştirmez ve alıntıyı soru olarak bırakır.

## Yeni Yaratılışın Biçimi

{ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} yükleminin ardından gelen {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış}, soruyu kaldırılma ihtimalinden bunun nasıl bir yaratılış olacağına taşır. {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} belirsiz, belirtme hâlli masdar olduğundan birkaç yakın çözümleme alanı açar: yeni bir hâlde kaldırılma, kaldırılmanın türü ya da onu gerçekleştiren yaratma eylemi. Sözdizimi bu yakın çözümlemeleri açık tutar. {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} biçim ve belirsizlik bakımından masdarla uyuşur; yenilik doğrudan yaratılışı niteler. Tekil masdar, yaratma süreciyle ortaya çıkacak hâli tek kavramda buluşturur; sayılabilir birden çok yaratılışı bildirmez. Sıfatın olağan sınırı burada “yeni” ya da yeniden yeni olmuş olmaktır; kök ailesinin başka çağrışımları bu görevdeki anlamını değiştirmez.

Bu tamlama, kemikten kalıntıya uzanan maddi öncülü yeni yaratılış sorusuna taşır: konuşanlar çözülmeyi ve yeniliği aynı soruda karşı karşıya getirir. {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} ile {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}ın tanvinli belirtme sonları, {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış}a işitsel bir hat çeker; bu ses uyumu anlam farklarını eritmez. Cümle kadansını “yeni” anlamındaki {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} ile kapatır; yenilik öne çıkar, sorulan olayın gerçekleşip gerçekleşmeyeceği açık kalır.

Yaratma adının olağan anlamı, {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} ile varlığa çıkarmaktır. Kök ailesindeki daha sınırlı bir kullanım, kesme ya da uygulamadan önce biçimin ölçüsünü ve sınırını belirlemeye ilişkindir. Ufalanmış kalıntı ({ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}) imgesiyle yeni yaratılış ({ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış}) yan yana gelince bu kullanım, parçalanmanın ardından sınırları belirli bir beden biçimi düşünmeye açılır. Bu benzetme biçim öncesi sınır fikrini taşır; belirli bir ölçü, plan ya da fiziksel işleyiş tarif etmez.

Ayrı bir kullanım, {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} ailesinde tamamlanmış bedenin dış biçimini adlandırır. Bu sözlük kolu, önceki ölçü benzetmesinin yanında ortaya çıkmış biçimi sunar: {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} ve {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} dağılmış maddeyi, {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} yeniliği duyurur. Böylece sorunun imgesi görünür beden biçimine ulaşır; görünüş burada güzellik ya da denge ölçütü içermez.

Yaratma anlamındaki {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} ailesinin söz ve anlatı kurmaya bağlı ayrı bir kullanımı, gerçeği olmayan bir şeyi tasarlayıp ortaya atmayı anlatabilir. Art arda gelen {ar:أَءِذَا, tr:a-idhā, gloss:ne zaman ... olduğunda} ve {ar:أَءِنَّا, tr:a-innā, gloss:gerçekten biz mi} soruları ile {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} yüklemindeki pekiştirme bu dalı tetikler; yeni yaratılış konuşanların gözünde inanılmaz bir iddia gibi duyulur. Bu bağlantıda kuşkunun tınısı sözcüğe eşlik etse de sözcük doğrudan “yalan” anlamına geçmez.

Yeniliği bildiren {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} sözcüğü genellikle yeni yapılmış ya da yeniden yeni olmuş durumu niteler. Kaynaklardaki dar ve tarihsel açıklamalardan biri, yeni kumaşın kesilerek elde edilmesiyle ilgilidir; kalıntı sözcüğünün bağımsız kırılma imgesi bu açıklamayla buluşunca yenilik bir kopuştan sonra düşünülebilir. Kök ailesinin bütünü kesip ayırma kullanımı da aynı süreksizlik imgesine katkı verir. Ayrıca {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} için ipin kopup devamlılığını yitirmesi ve parça parça kopmuş iplikler anlamındaki özel kaynak kullanımları aktarılır. Kumaşın kesilmesi ile kopmuş ip parçaları, yeni biçimi kesintiye uğramış bir sürekliliğin ardından düşünmeye açar; bu sınırlı benzetme kopuştan sonra biçimlenmeye katkı verir, bedenin kumaş ya da ip olduğunu veya yeniden yapımın yöntemini ileri sürmez.

Sözün maddi dönüşüm çevresindeki sesine daha ihtiyatlı bir benzetme eşlik eder. {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} olağan olarak söylenmiş sözü bildirir; aynı sözcük ailesinde sallanma, yerinde duramama ve hareket sırasında çıkan sesle ilişkili kullanımlar da bulunur. {ar:كُنَّا, tr:kunnā, gloss:olduğumuzda} ile açılan hâlin {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} ve {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} çevresinde değişmesi, bu hareket ve ses çağrışımlarına söz ediminin ötesinde bir dayanak sağlar. İtiraz, maddi süreksizlik içinde titreşen bir ses gibi işitilebilir; bu düşük kesinlikli benzetme sözün tınısıyla sınırlıdır, konuşanların fiziksel olarak sallandığını ileri sürmez.

## Çevredeki Söylem ve Dinleme

Bu açık sözün çevresindeki kök yankısı, “büyük bir söz” anlamındaki {ar:قَوْلًا عَظِيمًا, tr:qawlan ʿaẓīman, gloss:büyük bir söz} ile kemik anlamındaki {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} arasında duyulur (17:40, 17:49). İlkinde büyüklük sıfatla söze, odaktaki sözcükte kemik ise bedensel yapıya aittir; biçim ve anlam farkı korunurken ortak kök hafif bir ölçek yankısı verir (17:40, 17:49). Ardından hatırlatma için çeşitli biçimlerde sunumdan söz edilirken uzaklaşmanın arttığı anlatılır (17:41): {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitli biçimlerde sunduk} ile {ar:نُفُورًا, tr:nufūran, gloss:uzaklaşma} arasındaki gerilim içinde 17:49'daki {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} maddi sorusu olası bir sözlü karşılık gibi duyulabilir. Bu yakınlık bir yanıt ilişkisine alan açar; konuşmacıların kimliği ve nedensel bağ açık kalır.

Sorunun duyulması ile anlamının kavranması arasındaki mesafe, daha geniş bir diziyle görünür (17:44, 17:45, 17:46, 17:47). Her şeyin tesbih ettiği hâlde insanların bunu kavrayamaması (17:44), {ar:وَلَٰكِن لَّا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:wa-lākin lā tafqahūna tasbīḥahum, gloss:ama onların tesbihini kavrayamazsınız} sözünde işitilen ile kavranılan arasındaki açıklığı kurar. Kur'an'ın okunmasıyla inkârcılar arasındaki gizli perde (17:45), kalplerdeki örtüler ve kulaklardaki ağırlıkla (17:46) birlikte kavrayışın hem içsel hem işitsel yönünü gösterir: {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:gizli bir perde}, {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} ve {ar:وَقْرًا, tr:waqran, gloss:ağırlık}. Dinleme ile gizli konuşmanın yan yana geldiği sahne (17:47), açık işitmenin yanına özel fısıltıyı koyar: {ar:يَسْتَمِعُونَ إِلَيْكَ, tr:yastamiʿūna ilayka, gloss:seni dinlemeleri} ve {ar:نَجْوَىٰ, tr:najwā, gloss:gizli konuşma}. Birlikte bu imgeler sözün duyulması ile alınışını ayıran bir bağlam sunar; odaktaki {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} sözü aktarmaya devam eder, bu bağlam tek başına konuşanların iç durumunu teşhis etmez. Fiil kendi başına “varsaydılar” anlamını taşımaz; çevredeki sahneler başka bir ahlaki reddi de anlatabilir.

Bu dinleme çerçevesinin hemen öncesinde örnek kurma şaşma ve yol bulamamaya bağlanır (17:48): {ar:ضَرَبُوا لَكَ الْأَمْثَالَ, tr:ḍarabū laka al-amthāl, gloss:sana örnekler verdiler} ve {ar:فَضَلُّوا, tr:fa-ḍallū, gloss:şaştılar}. Buradaki yol düşünsel bir çıkmazdır. Odaktaki {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}, bu örnek verme sahnesinde bedenin maddi koşulunu gelecekteki dirilmeye ilişkin çıkarımın önünü kapatmaya çalışan bir kıyas dayanağına dönüştürebilir. Bu bağlantı olası bir okumadır: (17:48) başka iddiaları da hedefliyor olabilir ve konuşanların öncülünün doğruluğu bu yakınlıktan kesinleşmez.

## Yakın Yanıtların Açtığı Ölçek

Örnek ve çıkmazın ardından maddi sınama, kırıntının karşı ucuna taşınır: “Taş ya da demir olun” buyruğu (17:50), {ar:كُونُوا حِجَارَةً أَوْ حَدِيدًا, tr:kūnū ḥijārah aw ḥadīdan, gloss:taş ya da demir olun} ile direnci, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}ın dağılmışlığının karşısına koyar. Böylece kırılgan kemik ve kalıntı ({ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler}; {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}) en dayanıklı maddelerle birlikte edilgen {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecekler} sorusunun sınamasına girer. Retorik abartıdaki karşı-örnek, maddi direnci yükseltilmeye sınır koyamayacak uca taşır; taş ve demir itirazın uç imgeleridir, gerçek bir mineral dönüşümü ya da yeniden kurma malzemesi değildir.

Yanıt, maddenin direncinden ilk başlangıca geçer: “Gönüllerinizde büyük görünen bir yaratılış” seçeneği ve “bizi kim geri döndürecek?” sorusu, “sizi ilk kez var eden” karşılığıyla buluşur (17:51): {ar:أَوْ خَلْقًا مِّمَّا يَكْبُرُ فِي صُدُورِكُمْ, tr:aw khalqan mimmā yakburu fī ṣudūrikum, gloss:gönüllerinizde büyük görünen bir yaratılış}, {ar:مَن يُعِيدُنَا, tr:man yuʿīdunā, gloss:bizi kim geri döndürecek} ve {ar:فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:faṭarakum awwala marratin, gloss:sizi ilk kez var eden}. İlk var ediliş, odaktaki {ar:خَلْقًا جَدِيدًا, tr:khalqan jadīdan, gloss:yeni bir yaratılış}ı önceki başlangıçla ilişkilendirip var edeni öne çıkarır; maddi işleyişi ya da kişisel özdeşlik sorununu çözmez. Yaratılış sözcüğünün ölçü ve sınır belirleme kullanımı yanıtla buluşunca, yeni biçimi önceden belirlenmiş ölçüyle düşünmeye açar; bu benzetme belirli bir plan veya beden ölçüsü vermez. {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etmek} olağan olarak ilk kez başlatmayı anlatır; ayrıca aktarılan açılma ya da yarılma kolu {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} imgesiyle buluşabilir. Böyle bir yakınlık, ilk başlangıcın parçalanmış olana da eriştiğini düşündürebilir; fiilin olağan anlamı ve bu bağlantının imgesel niteliği korunur.

İlk başlangıç yanıtının ardından başların elçiye doğru sallanması, kuşkuyu sözden bedensel harekete geçirir (17:51): {ar:فَسَيُنْغِضُونَ إِلَيْكَ رُءُوسَهُمْ, tr:fa-sayunghiḍūna ilayka ruʾūsahum, gloss:başlarını sana doğru sallayacaklar}. Bu jest, odaktaki edilgen {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecekler} çevresinde hareketsiz bedene hareketin geri gelişiyle olası bir imgesel yankı kurar. Baş sallama burada kuşkunun bedensel ifadesidir; benzerlik jest düzeyindedir, onay ya da diriliş olayı değildir.

Bu bedensel tepkinin ardından çağrıya karşılık verme sahnesi açılır (17:52): {ar:يَوْمَ يَدْعُوكُمْ, tr:yawma yadʿūkum, gloss:sizi çağırdığı gün} ve {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:karşılık vereceksiniz}; karşılığın ardından hamd gelir. Odaktaki {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} olağan edilgen diriltilme anlamını korurken, aynı kelime ailesindeki yöneltme ya da gönderme kullanımı çağrıya ayrı bir yöneliş katkısı sunar. Böylece kaldırılma, dışarıdan gelen çağrıya yönelip cevap veren bir gelecekle yankılanır; bu bağ gerçekleşme mekanizmasını açıklamaz. {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} ile başlayan sesli soru da insan sözünü bu çağrı-yanıt ufkuna getirir. Daha iyi sözü seçme buyruğu bu konuşma alanına ayrı bir ahlaki ölçü ekler (17:53): {ar:يَقُولُوا الَّتِي هِيَ أَحْسَنُ, tr:yaqūlū allātī hiya aḥsan, gloss:en güzel sözü söylesinler}. Bu öğüt, diriltilmenin tek amacı ya da maddi gerçekleşme yolu olarak sunulmaz.

İnsanların birlikte cevap verişinden bakış daha geniş topluluğu taşıyan yerleşime kayar: bir yerleşimin kıyamet gününden önce yok edileceği bildirilir (17:58); {ar:قَرْيَةٍ, tr:qaryatin, gloss:yerleşim} ve {ar:مُهْلِكُوهَا, tr:muhlikūhā, gloss:onu yok edecek} sözleri toplumsal ölçeği açar. Bireysel bedenin {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} hâline gelmesi ve {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} diye kaldırılma sorusu, yerleşimin yıkımıyla daha geniş toplumsal ölçekte yan yana gelir; yerleşim ortak topluluğun taşıyıcısıdır. Bu ölçek benzetmesi iki olayı özdeşleştirmez ve yerleşimin diriltilmesini ileri sürmez. İşaretlere ilişkin uyarının ardından büyük azgınlıkta artıştan söz edilmesi (17:60), hatırlatma sunumundan sonra gelen uzaklaşma artışına (17:41) ayrı bir tepki imgesi ekler. Yankı artış biçimindedir: 17:60'ın tetikleyicisi işaretlere dair uyarıdır; bu ayet diriltilme sorusunu ya da iki sahnenin aynı kişilerini ve nedenini belirtmez.

## Dönüş, Oluşum ve Toplu Kaldırılış

Yerleşim ölçeğinden insanın daha uzun oluş ve dönüş tarihine geçince, topraktan yaratılma, toprağa dönme ve yeniden çıkarılma dizisi görünür (20:55). Bu sıra, {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} ile {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}ı son durumdan çok yaratılma ve dönüş içindeki maddi hâller olarak düşündürür; edilgen {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} da dönüşten sonra dışarı çıkarılma imgesiyle buluşur. İlk yaratılış ile yeni yaratılışı karşılaştıran bağlam (50:15), soruyu başlangıç ve yenilik ilişkisine açar. Bu bağlantıda {ar:خَلْقًا, tr:khalqan, gloss:yaratılış}ın ölçü ve sınır belirleme kullanımı biçime sınır, {ar:جَدِيدًا, tr:jadīdan, gloss:yeni}nin kesip ayırma yönü kopuş, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} ise parçalanma imgesi katar. Birlikte bu çağrışımlar, kırılmadan sonra yeni biçimi düşünmeye ve yaratmanın kapsamını kırıntıları tek tek toplamaktan öteye taşımaya yarar; her parçanın nasıl döndürüldüğünü belirlemez. Edilgen kaldırılma bu bağlamda dışarı çıkarılma gibi duyulur, göreve gönderilme anlamı almaz.

Parçalanma-yenilik ilişkisi bu kez alaycı bir nakilde daha toptan kurulur: bütünüyle parçalanma yeni yaratılış sorusunun önüne konur (34:7). Odaktaki {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} ile {ar:جَدِيدًا, tr:jadīdan, gloss:yeni}, kopuşun yeni biçimin imkânsızlığına dayanak yapıldığı bu alaycı itirazla yankılanır. Bu bağ kırılmadan sonra yeniliği düşünmeye açar; parçaların akıbeti ve yeniden oluşum yöntemi ayette belirtilmez.

Kalıntıdan geriye, kemiğin oluştuğu aşamaya bakıldığında başka bir zaman dizisi belirir: kemikler oluşur, etle örtülür, ardından başka bir yaratılış anılır (23:14). Bu sahne {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} sözcüğünü oluşumdan geçmiş yapısal madde olarak gösterir; {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} da burada varlığa çıkarma anlamıyla oluşum dizisine bağlanır. (23:14) kendi bedensel oluşum sahnesidir; burada kemiklerin yapısal oluşumuna katkı verir, odaktaki ölüm sonrası diriltilmenin işleyişini açıklamaz ya da maddi itirazın yerini almaz.

Oluşum sahnesinden eylemin ölçeğine geçiş, toplu yaratma ve diriltmenin tek bir canınkine benzetilmesiyle kurulur (31:28). Bu karşılaştırma edilgen {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} çoğulundaki toplu kaldırılışı öne çıkarır; tekil benzetme eylemin ölçeğini anlatırken kaldırılanlar topluluğunu tek kişiye indirmez ve bedenin niteliği hakkında hüküm vermez.

Toplu ölçeğin ardından dış işarete karşı hareket sahneleri gelir: ikinci sûr üflendikten sonra insanlar ayağa kalkıp bakar (39:68); sûrün ardından herkes bir araya toplanır (18:99). Önce kalkış ve bakış, sonra toplu toplanma görünür; bu sıra odaktaki edilgen {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecekler} için dış işaretten sonra hareket kazanan bir topluluk yankısı kurar. Bu bağlamsal benzerlik kaldırılma imgesini genişletir; odak ayetin sûrü anmaması, bu yankının zorunlu bir mekanizma olarak okunmasını engeller.

## Sorunun Başka Bağlamlarda Dönüşü

Aynı {ar:عِظَٰمًا, tr:ʿiẓāman, gloss:kemikler} ve {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} sorusu, edilgen {ar:لَمَبْعُوثُونَ, tr:la-mabʿūthūna, gloss:kesinlikle diriltilecekler} yüklemiyle birlikte {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} ile yeniden söze dökülür (17:98); bu kez ayetleri ve karşılığı inkâr çerçevesindedir. Tekrar maddi soruyu korurken sûre içindeki ret söylemine taşır; bağlam değişimi sözün duyuluşuna ilişkisellik katar, kişisel bir güdü bildirmez. Duyusal dönüş ve bedensel biçimlenme anlatısı 17:97'de kalır, bu tekrara aktarılmaz.

Bu ret çerçevesi başka bir paralel soruda daha açık bir ilişki kazanır: yeryüzünde kaybolduktan sonra yeni bir yaratılışla mı karşılaşılacağı {ar:وَقَالُوا۟, tr:wa-qālū, gloss:ve dediler} ile sorulur ve ayetin devamında Rableriyle buluşmayı inkâr açıkça belirtilir (32:10). Bu paralel, 17:49'daki maddi sorunun yanına reddedilen karşılaşmaya ilişkin bir katman ekler; {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} varlığa getirmeyi, {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} yeniliği bildirmeyi sürdürür. İlişki kişisel güdüyü teşhis etmez ve sözcüklerin anlamını yeniden tanımlamaz.

Yeniliğin kapsamı, yaşayanların ortadan kaldırılmasının ardından yeni bir yaratılış getirilmesiyle başka bir ihtimale açılır (35:16). Bu sıra, {ar:خَلْقًا, tr:khalqan, gloss:yaratılış}ı varlığa getirme olarak tutarken, yeni oluşumun önceki kalıntıları yeniden biçimlendirmenin yanı sıra başka bir varlığın onların yerini alması ihtimalini de düşündürür. Bu olasılık {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} sıfatının tek başına taşıdığı bir anlam değil, (35:16)'daki kaldırılma ve ardından yeni yaratılış sırasının katkısıdır; 17:49'un bedensel diriltilme sorusu açık kalır.

</source_prose>
