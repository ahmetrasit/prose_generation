# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:21**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.middle.claims.json`

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
- Refer to source paragraphs as `31:21 ¶N`.

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

`(31:21 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:21",
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
        "citation": "(31:21 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_21/31_21.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_21/31_21.middle.claims.json \
  --ayah-ref 31:21
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_21/31_21.prose.editorial.tr.md`

<source_prose>
## Buyruğun nesnesi ve miras

31:21, söylemi yinelenebilir bir buyruk-cevap karşılaşmasına taşıyan {ar:وَإِذَا, tr:wa-idhā, gloss:ve ne zaman ki} ile açılır. Bu çerçeve tekrarların sayısını ya da önceki tartışmanın içeriğini belirlemeden, her sunuluşta cevabın nasıl geldiğini öne çıkarır. {ar:قِيلَ, tr:qīla, gloss:söylendi} sözü muhataplara yöneltirken yakın insanî söyleyeni dilbilgisel olarak adlandırmaz; {ar:لَهُمُ, tr:lahum, gloss:onlara} alıcı grubu açıkça gösterir. Buyruğun kaynağı da açık kalır: izlenmesi istenen şey {ar:مَآ أَنزَلَ ٱللَّهُ, tr:mā anzala Allāhu, gloss:Allah’ın indirdiği şey}dir. Ardından {ar:قَالُوا۟, tr:qālū, gloss:dediler} etkin çoğuluyla cevap sözü grubun ağzına geçer; dilbilgisel sahiplenmenin kapsamı bu cevap veren grupla sınırlıdır, her ferdi ya da bütün ataları kapsamaz. İki fiilin ortak söyleme kökü, bildirilen buyruktan sahiplenilmiş cevaba geçişi duyurup söz sahiplerini birbirinden ayırır.

Değişen, izleme eyleminden çok onun nesnesidir. {ar:ٱتَّبِعُوا۟, tr:ittabiʿū, gloss:izleyin} çoğul buyruğu ile {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} birinci çoğul cevabı, VIII. biçimde aynı takip ve bağlanma eylemini taşır: ilki yöneltilmiş emir, ikincisi grubun şimdiki ortak beyanıdır. Bu biçimlerde doğrudan izleme ve bilinçli hizalanma öne çıkar. İki {ar:مَآ, tr:mā, gloss:neyi} tümcesi fiillerin paralel nesne yerlerinde durur: ilki Allah’ın indirdiği şeyi, ikincisi ataların üzerinde buldukları şeyi gösterir. İlk nesnenin kapsamı açık başlar, ardından gelen ilahî gönderme gönderilmiş içeriğe yönelen çağrıyı belirler. Aradaki {ar:بَلْ, tr:bal, gloss:aksine}, nesneyi ataların uygulamasına çeviren bir ikame eşiğidir; buyruğa ek açıklama getirmez. Kısa sözün kapalı lâmı tam bu dönüşte kulakta bir durak yaratır; ses izlenimi, nesne değişiminin sözlü eşiğiyle sınırlıdır. Cevap, vahyi izleme buyruğunun yerine atalarla bulunmuş uygulamayı izleme iddiasını koyar. Birinci çoğul şimdiki zaman bunu grubun paylaşılan yönelişi gibi duyurur, kişilerin bu yönelişe katılım derecesini açık bırakır. Aynı takip fiilinin Allah’tan indirilmiş mesajla atalar arasında bulunmuş uygulamaya yönelmesi, iki ayrı dayanak çizgisini görünür kılar; biçimsel paralellik bu çizgileri karşılaştırılabilir yaparken yetki ve doğruluk kararını açık bırakır.

I. biçimin geçmiş zaman birinci çoğul kipi {ar:وَجَدْنَا, tr:wajadnā, gloss:bulduk}, bulma ya da karşılaşma eylemini kurar; {ar:ءَابَآءَنَا, tr:ābāʾanā, gloss:atalarımız} doğrudan nesne, {ar:عَلَيْهِ, tr:ʿalayhi, gloss:üzerinde oldukları hâl} ise onların bulunduğu durumu gösterir. Böylece konuşanlar, gerekçelerini doğrulanmış hükümden değil, karşılaştıklarını söyledikleri önceki bağlılıktan kurar; yapı onların kanıt diye sunduğu şeyi gösterir, ataların davranışını dışarıdan doğrulamaz. “Bulduk”taki birinci çoğul eki keşfeden grubu, “atalarımız”daki kırık çoğul ve iyelik eki ortak soyu aynı sese toplar. Bu kolektif yakınlık bir hafıza etkisi yaratır; burada yinelenen Kur’anî bir formüle dönüşmez. “Bizim” ataları öne çıkaran iyelik toplumsal ağırlık kurarken, {ar:بَلْ, tr:bal, gloss:aksine} onların durumunu buyruğun yerine geçirilen dayanak yapar; ret gölgesi parçacığın sözlük anlamından değil bu söylem ilişkisinden doğar. Atalar anılmadan önce gelen {ar:عَلَيْهِ, tr:ʿalayhi, gloss:üzerinde oldukları hâl}, miras alınmış duruşu öne alıp sonra sahiplerini gösterir. Bu yerel edat-zamir kuruluşu pratiği ayak basılan zemin gibi duyurur; {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} da o zemini grubun sürdürdüğü yola taşır. Gelenek böylece hem hatırlanan bir geçmiş hem içinde durulup devam edilen bir tutum olarak görünür.

Yol imgesi, takip fiilinin olağan “ardından gitme” anlamı sürerken örnek ya da öğreti doğrultusunda davranmayı da taşımasıyla açılır. {ar:وَجَدْنَا, tr:wajadnā, gloss:bulduk} kökünün ayrı bir çizgi-iz kullanımı, {ar:عَلَيْهِ, tr:ʿalayhi, gloss:üzerinde oldukları hâl} konumu ve {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} takip ilişkisiyle tetiklenince, bulunmuş uygulama önceden yürünmüş bir patika gibi duyulur. Aynı kökün ayrı üst-kuşak kullanımı, açık atalar nesnesiyle birleşerek izi soya bağlar; bu iki ayrı sözlük dalı odaktaki fiilin olağan bulma anlamının yerini almaz, gerçek izlerin tek tek arandığını da bildirmez. Bağlantı, bakım verme ya da nedensel kaynak olmayı atalara yüklemez; patika imgesinin katkısı, miras alınmış uygulamayı değerlendirilebilir bir iz gibi göstermesidir. 43:23’te bu bağ {ar:إِنَّا وَجَدْنَآ ءَابَآءَنَا عَلَىٰٓ أُمَّةٍۢ وَإِنَّا عَلَىٰٓ ءَاثَٰرِهِم مُّقْتَدُونَ, tr:innā wajadnā ābāʾanā ʿalā ummatin wa-innā ʿalā āthārihim muqtadūn, gloss:atalarımızı bir yol üzerinde bulduk, onların izlerinden gidiyoruz} sözleriyle yinelenir; 43:24’te {ar:بِأَهْدَىٰ مِمَّا وَجَدتُّمْ عَلَيْهِ ءَابَآءَكُمْ, tr:bi-ahdā mimmā wajadtum ʿalayhi ābāʾakum, gloss:atalarınızı üzerinde bulduğunuzdan daha doğru bir rehberlik} sorusu izi daha doğru rehberlik karşısında sınanabilir kılar. Bu karşılaştırma, “izlemek” fiilini sözlükçe araştırmak ya da bulmayı ata olmak diye çevirmeden, bulunmuş yolun kendi başına yetki taşımadığını duyurur.

## Aile bağı ve yönün dayanağı

Soy sözü, aile içindeki bakım ve yön verme bağını da çağrıştırır. Luqman oğluna {ar:يَٰبُنَىَّ لَا تُشْرِكْ بِٱللَّهِ, tr:yā-bunayya lā tushrik bi-llāh, gloss:ey oğulcuğum, Allah’a ortak koşma} diye öğüt verir (31:13). Ardından {ar:وَوَصَّيْنَا ٱلْإِنسَٰنَ بِوَٰلِدَيْهِ, tr:wa-waṣṣaynā al-insāna bi-wālidayhi, gloss:insana anne babasına karşı sorumluluk yükledik} kuşaklar arasında taşınan yükümlülüğü bildirir; {ar:وَٰلِدَيْهِ, tr:wālidayhi, gloss:anne babası} bağı doğumla kurulmuş ilişkiye bağlar (31:14). Annenin {ar:حَمَلَتْهُ أُمُّهُۥ وَهْنًا عَلَىٰ وَهْنٍۢ, tr:ḥamalat-hu ummuhu wahnan ʿalā wahn, gloss:onu güçlük üstüne güçlükle taşıdı} diye anılan emeği ve {ar:وَفِصَٰلُهُۥ فِى عَامَيْنِ, tr:wa-fiṣāluhu fī ʿāmayn, gloss:iki yılda sütten ayrılması} çocuğun büyütülmesini somutlaştırır (31:14). Bu yakın bağlam, {ar:ءَابَآءَنَا, tr:ābāʾanā, gloss:atalarımız} sözünü yaşayan ebeveyn ilişkisiyle de duyurur: miras yalnızca bir soy etiketi değil, bakımın aktarılabildiği insanî bağdır. Yön tayiniyle ilgili sınırsa belirli bir koşula ilişir: anne baba Allah’a ortak koşmaya zorlarsa {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:ikisine itaat etme} denir; hemen ardından {ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī al-dunyā maʿrūfan, gloss:dünyada ikisine iyilikle eşlik et} emri yakınlığı ve iyi muameleyi sürdürür (31:15). Aynı ayette {ar:وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ إِلَىَّ, tr:wa-ttabiʿ sabīla man anāba ilayya, gloss:bana yönelen kişinin yolunu izle} buyruğu, takip eylemini koruyup örneği Allah’a yönelen kişiye çevirir. Böylece bakım borcu sürerken yönelişin örneği değişebilir; bu ayrım özellikle şirk baskısıyla sınırlıdır ve bütün miras alınmış öğretilere genellenmez. Bu aile sahnesi 31:21’deki konuşanların kimliğini belirlemez; onun katkısı soy bağının gerçekliğini korurken bakım yükümlülüğüyle yön seçme yetkisini ayırmaktır (31:13, 31:14, 31:15).

31:20, Allah hakkında tartışan kimi insanların önünde bulunmayan dayanakları adlandırır: {ar:بِغَيْرِ عِلْمٍۢ وَلَا هُدًۭى وَلَا كِتَٰبٍۢ مُّنِيرٍۢ, tr:bi-ghayri ʿilmin wa-lā hudan wa-lā kitābin munīrin, gloss:bilgi, yol gösteren rehberlik ve aydınlatıcı kitap olmadan}. Bilgi, izlenecek yönü gösteren rehberlik ve açıklığa çıkaran düzenli yazılı dayanak ayrı ayrı belirir; {ar:هُدًۭى, tr:hudan, gloss:yol gösteren rehberlik} izlenecek yöne ölçü getirirken {ar:كِتَٰبٍۢ مُّنِيرٍۢ, tr:kitābin munīrin, gloss:aydınlatıcı kitap} açıklık sağlayan düzenli kayıt gibi duyulur. Hemen ardından 31:21’de konuşanlar {ar:وَجَدْنَا, tr:wajadnā, gloss:bulduk} ile atalarının üzerinde bulundukları konumu bulma gerekçesi, {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} ile de sürdürülen örnek olarak sunar. Bu yakınlık, karşılaşılmış aile pratiğinin önceki ayette adı geçen bilgi ve yön dayanaklarının yerine geçirildiği yorumunu destekler; gerekçenin ağırlığı geleneğin yalnızca eski oluşunda değil, konuşanların onu bulduklarını söylemesindedir. Bağlantı yorumlayıcıdır ve resmî üç maddeli bir sınama kurmaz; ayetler aynı bağlamdaki ayrı itirazları da anlatıyor olabilir. Bu sınırlar içinde komşuluk, bulunan aile pratiğini bilgi ve yön ölçütlerinin karşısına konan bir dayanak olarak görünür kılar (31:20, 31:21).

31:21’de {ar:قَالُوا۟, tr:qālū, gloss:dediler} sözü {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} ile izlenen yola bağlandığında, sıradan söz davranışa yön veren benimsenmiş bir görüş gibi işler. Bu dönüşüm, işitme ve karşılık vermenin başka sahnelerde nasıl kesilebildiğini düşündürür. 31:6’da {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahw al-ḥadīth, gloss:oyalayıcı söz} insanı meşgul eder ve {ar:لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ, tr:li-yuḍilla ʿan sabīli Allāh, gloss:Allah’ın yolundan saptırmak için} onu yoldan çevirebilir. Ayrı bir sahnede, ayetler okunurken birinin {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:onları işitmemiş gibi} yüz çevirmesi ve {ar:كَأَنَّ فِىٓ أُذُنَيْهِ وَقْرًا, tr:ka-anna fī udhunayhi waqran, gloss:sanki kulaklarında bir ağırlık var} diye tasvir edilmesi, işitmeyi anlama ve karşılık vermeyle, kulak ağırlığını da alımlamanın önündeki engel imgesiyle buluşturur (31:7). Bu iki bağlam ayrı sahneler ve ayrı muhataplar sunar; 31:21’deki konuşanlarla özdeşlik kurmadan, oyalama ile işitmeme ayrıntılarını bir araya getirerek odak yanıttaki yerleşik görüşün başka bir mesajı duymayı zorlaştıran olası bir savunma gibi işleyişini duyururlar (31:6, 31:7).

İşitme sahnesinden ayrı olarak, buyruğun kaynağını anlatan {ar:أَنزَلَ ٱللَّهُ, tr:anzala Allāhu, gloss:Allah’ın indirdiği} ifadesi başka bir iniş imgesi açar. {ar:أَنزَلَ, tr:anzala, gloss:indirdi} IV. biçimdeki etken geçmiş fiildir, II. biçim değildir; {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} açık faildir ve eylem bir şeyi aşağı gönderip ulaştırmayı bildirir. Bu biçim kendi başına aşamalı ya da yinelenen bir iniş anlatmaz; odak ayette indirilenin içeriği açık bırakılır ve vahiy olabilir. Allah’ın indirmesi, insanlara bildiriyi, iyiliği ya da cezayı ulaştıran ilahî kaynak olarak da belirir. 31:10’da gökten suyun indirilip ardından bitkilerin bitirilmesi ({ar:أَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا فِيهَا, tr:anzalnā mina al-samāʾi māʾan fa-anbatnā fīhā, gloss:gökyüzünden su indirdik ve onda bitkiler bitirdik}) inişi, ulaştığı ortamda görünen büyümeyle birleştirir; 31:34’te {ar:يُنَزِّلُ ٱلْغَيْثَ, tr:yunazzilu al-ghayth, gloss:yağmuru indirir} yağmuru hayat veren bir iniş ve rızık olarak öne çıkarır. Bu iki ayrı bağlam, odaktaki indirmeye üretken bir varış ve büyüme katmanı ekler. Yağmur örnekleri fiziksel özdeşlikten çok ulaştırmanın çevresinde beliren hayatı duyurur; odak nesnesi vahiy olabilir (31:10, 31:34).

## Seçilmiş yön ve sınanması

İlahi kaynağın karşısında ataların üzerinde bulunulan konumu yer alırken, 31:22 bağlılığın eylemle seçilen başka bir biçimini yanına koyar. Yüzünü Allah’a yöneltip iyi davranan kişi ({ar:وَمَن يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ وَهُوَ مُحْسِنٌۭ, tr:wa-man yuslim wajhahu ilā Allāhi wa-huwa muḥsin, gloss:yüzünü Allah’a teslim eden ve iyilik yapan kimse}) yönelişi eylemle birleştirir; {ar:ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:istamsaka bi-l-ʿurwati l-wuthqā, gloss:en sağlam kulpa sıkıca tutundu} etkin biçimde kavranan güvenilir dayanağı, {ar:وَإِلَى ٱللَّهِ عَٰقِبَةُ ٱلْأُمُورِ, tr:wa-ilā Allāhi ʿāqibatu l-umūr, gloss:işlerin sonu Allah’a varır} ise bu dayanağın verdiği güven ve sükûneti öne çıkarır. Odak ayetteki {ar:وَجَدْنَا عَلَيْهِ ءَابَآءَنَا, tr:wajadnā ʿalayhi ābāʾanā, gloss:atalarımızı üzerinde bulduk}, {ar:ٱتَّبِعُوا۟, tr:ittabiʿū, gloss:izleyin} ve {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} biçimleri de bulunmuş konumu, ardından gitmeyi ve örnek ya da öğreti doğrultusunda davranmayı taşır. Yan yana geliş, mirasla bulunmuş yerin yanına seçilmiş yöneliş, iyi eylem ve sağlam tutuşu koyar; iki bağlılık biçimi birbirini tamamlayan bir ilişki olarak da okunabilir (31:22).

Bu etkin yönelişin yanına, 31:24’te başka bir türden ve biçimce uzak bir yankı düşer. Oradaki {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre ya da az miktarda} kısa yararlanmanın ardından gelen ağır cezayı anlatır. “Az” sözü {ar:قَالُوا۟, tr:qālū, gloss:dediler} ya da {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} ile aynı kökten gelmez; yine de 31:21’deki {ar:بَلْ, tr:bal, gloss:aksine} karşı çıkışı ve atalar dayanağının yanına geldiğinde küçük ölçü ile uzak ses benzerliği, bu desteği az ya da sallantılı hissettirebilir. Bu yalnızca keşifsel bir temas: odaktaki söz “küçük” veya “kararsız” anlamı taşımaz, 31:24’teki azlık da cevapla ilgisiz kalabilir. Yankının katkısı, miras iddiasını kesin bir hükme çevirmeden kırılgan bir dayanak gibi yeniden duyurmaktır (31:24).

Biçimsel yankıdan daha doğrudan bir soru, doğru sözün gündelik bağlılığı yönetip yönetmediğidir. 31:25’te gökleri ve yeri kimin yarattığı sorulsa {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:elbette Allah diyecekler} cevabı verilir; ardından {ar:بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ, tr:bal aktharuhum lā yaʿlamūn, gloss:aksine çoğu bilmez} denir. Yaratıcıyı Allah diye adlandıran bu ikrar, 31:21’deki {ar:قَالُوا۟ بَلْ نَتَّبِعُ, tr:qālū bal nattabiʿu, gloss:dediler ki, izlemeyi sürdürüyoruz} beyanıyla yan yana gelince, doğru bir cevabın miras alınmış pratiği kendiliğinden yönetmediği görünür; {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} davranışa yön veren izleyişi taşımaya devam eder. Bu geriye dönük karşılaştırma iki sahnenin muhataplarını aynı saymaz; 31:25’teki “bilmemek” şükür ya da sonuçları bilmeyle ilgili olabilir, dolayısıyla samimiyetsizlik kanıtı değildir. Böylece 31:22’nin yöneliş ve tutuşu bağlılığın eylem yanını, 31:25’in ikrarı ise söz ile pratik arasındaki mesafeyi görünür kılar; miras alınmış yol hem davranış hem ikrarın gücü bakımından sınanır (31:22, 31:25).

Söylenen cevap sona erince ayet bu bağlılık iddiasını yeni bir koşulda sınayan soruya geçer. {ar:أَوَلَوْ, tr:ʾa-wa-law, gloss:öyle olsa bile} soru ile koşulu birleştirir: Şeytan çağırsa bile ataların izini sürmeyi sürdürecekler mi? Cevap ayrıca seslendirilmez; okur önceki {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} iddiasının bu uç koşulda da geçerli olup olmadığını düşünerek eksik sonucu tamamlar. Böylece grubun alıntılanan savunmasından değerlendiren hitaba geçilir; yeni bir karşılıklı konuşma ya da gerçekleşmiş olay anlatılmaz. {ar:كَانَ, tr:kāna, gloss:oluyordu} ile muzari {ar:يَدْعُوهُمْ, tr:yadʿūhum, gloss:onları çağırıyor} birleşince çağrı tek seferlik olmaktan çok süren bir koşul gibi çerçevelenir, ancak bu süre ölçülmez. Başlangıçtaki {ar:لَهُمُ, tr:lahum, gloss:onlara} ile buyruk alan topluluk konuşurken, {ar:قَالُوا۟, tr:qālū, gloss:dediler} ve {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} biçimleri iddiayı onlara bağlar; son fiildeki “onları” zamiri yine bu grubu çağrının hedefi yapar. Zamir zinciri, önce buyruğu alanları, sonra cevap verenleri ve nihayet çağrılanları aynı ayet içindeki güzergâhta buluşturur.

{ar:ٱلشَّيْطَٰنُ, tr:al-shayṭānu, gloss:Şeytan} ayette belirli tekil çağıranı, {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} ise indirme eyleminin açık failini adlandırır; böylece iki eylem ve yön aynı sahnede ayrışır. Şeytan adının olağan göndergesi değişmeden kalırken, uzaklık, ayrılık ve başkaldırıyla ilişkilendirilen kullanımı bu yerel karşıtlıkta ihtiyatlı bir yan tını kazanır. Çağrının azaba yönelmesi, 31:15’te Allah’a yönelenlerin başka yolu ve 31:20’de rehberlik eksikliğinin anılmasıyla birlikte bu tınıyı karşı-güzergâh gibi duyurabilir (31:15, 31:20). Bu bağlantı adı literal “uzaklık” anlamına çevirmeden ya da belirli bir etimolojiyi kesinleştirmeden, çağrının sapma yönünü belirginleştirir.

Çağrının olağan sözlü hareketi muhatabı çağırana doğru çeker; {ar:يَدْعُوهُمْ, tr:yadʿūhum, gloss:onları çağırıyor} bu seslenişi, {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} ise çağrının varış yönünü verir. Aynı Arapça kökün ayrı kullanımındaki uzun, sıkı bükülmüş kuyu ipi bu iki ucu ve aradaki çekişi görünür kılan bir benzetme sunar: çağıran bir uçta, ondan ayrı hedef ötekinde kalır. İp kullanımı çağrının yönünü somutlaştırır; ayette gerçek ip, fiziksel bağlama ya da zorla sürükleme bildirilmez. 14:22’de çağıran muhatapları üzerinde yetkisi olmadığını, onları çağırdığını ve onların karşılık verdiğini söyler; ardından kınamayı kendilerine yöneltir ({ar:وَمَا كَانَ لِىَ عَلَيْكُم مِّن سُلْطَٰنٍ إِلَّآ أَن دَعَوْتُكُمْ فَٱسْتَجَبْتُمْ لِى, tr:wa-mā kāna lī ʿalaykum min sulṭānin illā an daʿawtukum fa-stajabtum lī, gloss:üzerinizde yetkim yoktu; çağırdım, siz karşılık verdiniz}; {ar:فَلَا تَلُومُونِى وَلُومُوٓا۟ أَنفُسَكُم, tr:fa-lā talūmūnī wa-lūmū anfusakum, gloss:beni değil kendinizi kınayın}). Bu ayrı karşılık sahnesi, muhatapları 31:21’deki grupla özdeşleştirmeden, odak ayetteki daveti cevaplanabilir çağrı olarak duyurur; sorumluluk çağrının yönü kadar ona verilen karşılıkta da kalır (14:22).

## Çağrının hedefi ve yankıları

Bu davetin yönü, aynı öbekte adlandırılmış varış yeriyle tamamlanır: {ar:إِلَىٰ عَذَابِ ٱلسَّعِيرِ, tr:ilā ʿadhābi al-saʿīri, gloss:Alevli Ateş azabına}. {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} yönü, {ar:عَذَابِ, tr:ʿadhābi, gloss:azap} ceza ilişkisini, tamlayanındaki belirli {ar:ٱلسَّعِيرِ, tr:al-saʿīri, gloss:Alevli Ateş} ise son noktayı verir; öbek böylece adı konmuş eskatolojik bir hedefi gösterir. Yön bildiren edat çağrının varacağı yeri belirler, muhatapların çoktan ulaştığını değil. {ar:ٱلسَّعِيرِ, tr:al-saʿīri, gloss:Alevli Ateş} isim olarak hedefi adlandırır; aynı kökün ayrı kullanımındaki harlanıp tutuşan ateş imgesi ceza tamlamasında yakıcı sıcaklık, yakıt ve yayılan ısıyla bu varış yerini maddeleştirir. Bu imge ateş yakma eylemine geçmez; delilik ve fiyat gibi başka sözlük dalları da bu adlandırılmış hedeften ayrı kalır.

Ateşin yanındaki rahatlık karşı-imge başka bir sözlük dalından gelir. Aynı sözcük ailesinin ayrı kullanımındaki tatlı, kolay içilen su, {ar:ٱلسَّعِيرِ, tr:al-saʿīri, gloss:Alevli Ateş} hedefiyle karşılaşınca rahatlığın yitimi gibi duyulur; bu çağrı ayetinde su ya da susuzluk ayrıca adlandırılmaz. 14:22’deki {ar:عَذَابٌ أَلِيمٌۭ, tr:ʿadhābun alīmun, gloss:acı veren azap} ile kurulan ayrı temas ise sıcak rüzgârın ya da şiddetli açlık ve susuzluğun bedeni kavurmasına benzer bir acı imgesi ekler; bunlar burada ayrıca bildirilmiş ceza türleri değildir (14:22). İki çağrışımın katkısı farklıdır: su karşı-imgesi rahatlığın yitimini, 14:22 bağlantısı bedenin hissedeceği ağır acıyı düşündürür; ikisi de adlandırılmış hedefin yakıcılığını derinleştirir.

Önceki {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} fiili olağan izleme anlamını korur; {ar:عَذَابِ ٱلسَّعِيرِ, tr:ʿadhābi al-saʿīri, gloss:Alevli Ateş azabı} ise seçilen nesnenin sonucunu ve sorumluluk yükünü görünür kılar. Bu ilişki izleme eyleminin kendisini cezalandırma anlamına çevirmediği gibi, her izleyeni de suçlu saymaz. Önceki söyleyişe göre kapanışın boğazdan gelen ʿayn’ı ile ıslıklı sīn’i sesi ağırlaştırır; baştaki şīn {ar:ٱلشَّيْطَٰنُ, tr:al-shayṭānu, gloss:Şeytan} ile sīn {ar:ٱلسَّعِيرِ, tr:al-saʿīri, gloss:Alevli Ateş} iki ayrı ıslıklı ses olarak hafifçe yankılanır. Bu ses bağı iki adı aynı kökten ya da gizli bir kodla birleştirmez; katkısı, çağıran addan hedef adına uzanan kapanışta ritmi sertleştirmesidir.

Bu adlandırılmış hedef odak ayetteki cümleyi kapatırken, yakın bağlamdaki iki ayrı çağrı sahnesi çağıranla çağrılanın rolünü değiştirir. 31:30’da insanlar Allah’tan başka şeylere seslenir ve {ar:مَا يَدْعُونَ مِن دُونِهِ ٱلْبَٰطِلُ, tr:mā yadʿūna min dūnihi al-bāṭilu, gloss:O’ndan başka çağırdıkları şey batıldır} denerek bu nesnelerin hakikat ve istikrar taşımadığı belirtilir. Burada insanlar çağıran, çağrılanlar batıl nesnelerdir; 31:21’deyse Şeytan çağırır, insanlar çağrının hedefidir. 31:32’de üstlerini gölgelikler gibi dalga kaplayınca ({ar:غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-l-ẓulali, gloss:üstlerini gölgelikler gibi dalga kapladı}) dua Allah’a yönelir ve {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu al-dīn, gloss:dini yalnız O’na arındırarak Allah’a yalvardılar} diye anlatılır. Kurtuluşun ardından kimi şükreder, kimi yüz çevirir. Bu ayrı sahneler tek bir toplumsal devre dayatmaz; 31:30’daki batıl nesneye yönelen çağrıyla 31:32’de kriz anında Allah’a dönen duayı birlikte düşünmek, çağıranın ve yöneliş hedefinin değişebilirliğini görünür kılar (31:30, 31:32).

Dalganın iç içe yükselen, gölgelikler gibi üstlerini örten baskısı çağrı sahnelerindeki rol değişiminden ayrı olarak izleyişin dayanıklılığına yeni bir ölçü ekler. 31:32’de sahne dalga tehdidini, Allah’a yöneltilen duayı, O’na özgü kılınan bağlılığı, kurtarılmayı ve kurtuluş sonrasındaki farklı karşılıkları art arda verir. Bu sıra, 31:21’de {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} diye savunulan yolun baskı altındayken sürüp sürmediğini, rahatlığa kavuşunca korunup korunmadığını düşündürür. İki sahnenin muhatapları özdeş değildir; 31:32 yalnızca kriz duası ile kurtuluş sonrası nankörlük arasındaki karşıtlığı da anlatabilir. Bu ihtiyatlı karşılaştırma, bağlılığın hangi koşulda sürdüğünü sınayan olası bir ölçü sunar (31:32).

Yolun kimden devralındığı sorusunun yanında, sonucun kimin üzerinde kaldığı da belirir. 31:33’te {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lā yajzī wālidun ʿan waladihī wa-lā mawlūdun huwa jāzin ʿan wālidihī shayʾan, gloss:ne baba çocuk yerine bir şey öder ne de çocuk baba yerine} denir. Baba çocuk yerine, çocuk da baba yerine hiçbir şey ödeyemez; yakın soy bağı zararı uzaklaştıran bir kalkan ya da birbirinin yerine geçme imkânı sağlamaz. Atalar bir yolu aktarabilir, fakat takip eden kişi o yolun sonucunu onlara yükleyemez: soy başlangıç ve aktarım kanalı olarak gerçekliğini korurken sorumluluk kişide kalır. 31:33’ün genel sorumluluk hitabı olması da mümkündür; bu yüzden uyarı, 31:21’deki konuşanları özel olarak hedeflemeden, devralınmış yolun kaynağıyla onun sonucunu taşıyan kişiyi birbirinden ayırır (31:33).

</source_prose>
