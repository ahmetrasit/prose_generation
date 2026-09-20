# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:19**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.middle.claims.json`

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
- Refer to source paragraphs as `31:19 ¶N`.

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

`(31:19 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:19",
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
        "citation": "(31:19 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_19/31_19.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_19/31_19.middle.claims.json \
  --ayah-ref 31:19
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_19/31_19.prose.editorial.tr.md`

<source_prose>
## Adım ve ses

31:19 muhatabına iki ayrı davranışı ölçülü kılmasını söyler: yürüyüşünde doğrultuyu gözetmek ve kendi sesini kısmak. {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğrultuyu ve ölçüyü gözet} gerçek yürüyüşü, {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesinden bir miktar kıs} ise muhatabın işitilebilir çıkışını düzenler. İki buyruğu bağlayan {ar:وَ, tr:wa, gloss:ve} onları eş düzeyde yan yana getirir; ses öğüdü yürüyüş emrinin eki değildir. Aynı kişiye yönelseler de ölçüler farklı kurulur: {ar:فِى مَشْيِكَ, tr:fī mashyika, gloss:yürüyüşünde} davranışın alanını, {ar:مِن صَوْتِكَ, tr:min ṣawtika, gloss:sesinden} mevcut bir kaynaktan azaltmayı gösterir. Görünür beden hareketiyle kulağa ulaşan ses böylece aynı kısa öğütte buluşur.

Yürüyüş emrindeki {ar:ٱقْصِدْ, tr:iqṣid, gloss:yönel ve ölçüyü gözet} sözcüğü, birinci fiil kalıbındaki emir biçimiyle muhatabı kendi adımını şimdi düzenlemeye çağırır. Sözcük ailesinin hedef seçip ona doğru gitme anlamı, ayrı bir taşıyıcı olan gerçek yürüyüşle temas edince amaçlı bir öz-yönlendirmeye dönüşür: adım bir yön kazanır, varış yeri ise belirtilmez. Yol ve yönteme ilişkin doğru çizgi anlamı yalın biçimde kullanılır; düzgün yürüme ise bu belirli fiil kalıbında belirir. Ayrıca aynı ailenin iki aşırılık arasında ölçü ve adaleti koruma anlamı sözlüklerde çoğunlukla geçim ve harcama örnekleriyle açıklanır. Yürüyüşe taşındığında bu ölçü, hedefe yönelme ile doğru çizgiyi bir arada tutar. Belirgin emir biçimi yürüyüş yargısını taşıyan fiili öne çıkarır; bu biçimsel vurgu kullanım sıklığına ilişkin kanıt sunmaz ve sabit bir rota ya da hız belirlemez.

Buyruğun {ar:مَشْيِكَ, tr:mashyika, gloss:senin yürüyüşün} dediği, bir soyut yol değil, kişinin kendi iradesiyle yaptığı gerçek yürüyüştür; ikinci tekil iyelik de çevredeki yolu değil muhatabın hareketini ona bağlar. Yürüyüş adı davranışı tek bir adımın ötesine taşır; süreyi ya da davranışın her anını ayrıca belirlemez. Emir doğrudan nesne almaz; {ar:فِى, tr:fī, gloss:içinde} yürüyüşün icrasını davranış alanı olarak verir. Böylece hedefe yönelme, düzgün çizgi ve aşırılıktan kaçınma bedensel adımda birleşirken yürümek kendi gerçek anlamını korur.

Söyleniş de bu hareketten sese geçişi duyurur. Kısa ve keskin {ar:ٱقْصِدْ, tr:iqṣid, gloss:yönel ve ölçüyü gözet} buyruğunun ardından kısa {ar:فِى مَشْيِكَ, tr:fī mashyika, gloss:yürüyüşünde} tamamlayıcısı gelir; sonra ikinci kısa emir başlar. {ar:مَشْيِكَ, tr:mashyika, gloss:yürüyüşün} daha hafif akışından çift ünsüzlü {ar:وَٱغْضُضْ, tr:wa-ighḍuḍ, gloss:ve kıs} biçimine geçiş, bedensel yürüyüşten işitilebilir çıkışa doğru sıkışan bir ritim hissettirebilir. Bu sıkışma okunuşta bir izlenim sunar; köklerin değişmez anlamı ya da ses taklidi olarak kullanılmaz.

Ses buyruğundaki {ar:وَٱغْضُضْ, tr:wa-ighḍuḍ, gloss:ve kıs} birinci fiil kalıbındaki belirgin azaltma emridir. Sözlüklerde {ar:غَضَّ مِنْ صَوْتِهِ, tr:ghaḍḍa min ṣawtihi, gloss:sesini alçalttı} kuruluşu da bu fiili genel bir sessizlik çağrısından ayırır: {ar:مِن صَوْتِكَ, tr:min ṣawtika, gloss:sesinden} mevcut ses kaynağından bir miktar kısmayı gösterir, mutlak bir düzey koymaz. Edatın ses adına doğrudan dayanması, eksiltme ilişkisini söyleyiş sınırında da duyulur kılar; bu, yeni bir dilbilgisel çözümleme değil, sesleniş düzeyinde bir etkidir. {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin} iyeliği buyruğu bu kişinin kendi işitilebilir sesiyle sınırlar. Aynı ses kısma ailesinde, uzun süre beklememiş ve canlı görünen şeyler için kullanılan tazelik-körpelik anlamı ayrı bir sözlüksel kullanımdır. Bu anlam burada emredilen işleme dönüşmez; yine de sesten bir bölüm alma yapısı, fazlalık inerken sesin canlı kalabileceğine ince bir yankı taşır.

Yalın {ar:صَوْتِكَ, tr:ṣawtika, gloss:duyulur sesin} adı insanın da hayvanın da çıkarabildiği işitilebilir sesi kapsar; şarkı, bağırma ve seslenme anlamlarıysa yalnızca belirli biçim ve söz öbeklerinde görülür. Ses ailesindeki {ar:الْإِنْصَات, tr:al-inṣāt, gloss:konuşmayı bırakıp dinleme} kimi sözlüklerde çağrıya cevap verip yönelmeyi, kimilerinde konuşmayı kesip dinlemeyi anlatır; bir kaynak ilk açıklamayı kabul etmez, ayrıca bu anlam belirli türemiş biçime özgüdür. Bu aile yankısı, 31:19’da ayrıca adlandırılmayan dinleyiciye, söz sürerken dinleme alanı açma ihtimalini düşündürür; alıcıya ilişkin bu bağlantı sınırlı bir olasılık olarak kalır.

İki emirden sonra gelen isim cümlesi ses hakkında bir yargı kurar: {ar:إِنَّ أَنكَرَ ٱلْأَصْوَٰتِ لَصَوْتُ ٱلْحَمِيرِ, tr:inna ankara al-aṣwāt la-ṣawtu al-ḥamīr, gloss:eşeklerin sesi seslerin en iticisidir}. Başlangıçtaki {ar:إِنَّ, tr:inna, gloss:kuşkusuz} ile yüklemdeki {ar:لَصَوْتُ, tr:la-ṣawtu, gloss:kesinlikle sestir} lâmı birlikte hükmü vurgular; lâmın yüklemdeki isimden ayrılmaması, ağırlığı tanımlanan sese yerleştirir. Bu ses karşılaştırması iki buyruğa işitilebilir bir gerekçe verir. Yargının önce gelip eşeklerin sesinin cümle sonunda duyulması kısa bir beklenti yaratır; emirlerden nominal hükme geçiş de okunuşta öğütten kesin yargıya keskin bir dönüş sağlar. Burada tek bir anda gerçekleşen anırma değil, ses hakkında süreklilik taşıyan bir değerlendirme dile gelir.

Karşılaştırmanın alanını çoğul {ar:ٱلْأَصْوَٰتِ, tr:al-aṣwāt, gloss:sesler} açar; elatif biçimdeki {ar:أَنكَرَ, tr:ankara, gloss:en itici olan} bu duyulur sesler içinde sıralama kurar. Ses çoğulu ile elatif biçim karşılaştırmayı tek bir örnekten önce bütün işitilebilir seslere açar; yargı bu alan içinde üstünlük kurar, ayrı bir ses türleri cetveli çıkarmaz. Elatifin belirginliği karşılaştırmayı keskinleştirir. Başka türetimlerdeki bir şeyi tanınmaz kılma anlamı bu cümlenin fiil biçimi değildir; yine de aynı aileden gelen bu yankı sese yabancılık ve tanınması güç olma nüansı katabilir. Çetin ve yadırgatıcı olana ilişkin sözlüksel kullanımlar kendi ad ve sıfat kalıplarına bağlıdır; sesin sertlik ve tuhaflık hissi bu sınır içinde belirir. Sese özgü “en çirkin” kullanımı da elatif ile sesler çoğulunun birleştiği bu özel kuruluşa aittir. Böylece olağan iticilik yargısı korunurken sesin yabancı ve yadırgatıcı yüzü de duyulur.

Yargının kaynağı {ar:ٱلْحَمِيرِ, tr:al-ḥamīr, gloss:eşekler}dir: belirli kırık çoğul tek bir rastlantısal hayvanı değil, evcil ya da yaban eşeği olarak bilinen sınıfı sunar; sözlüklerdeki dişi biçim de aynı sınıfa bağlıdır. Eşek sınıfı sesin kaynağını belirler; bu ad tek başına ses yüksekliği bildirmez. Sözlüklerdeki uzak renk kullanımları bu sahnenin kapsamına girmez. {ar:صَوْتُ, tr:ṣawtu, gloss:ses} ile kurulan tamlama eşeği sesin kaynağı yapar. Canlı hayvanın kaynak olarak belirlenmesi yalın ses adını bir anırma gibi duyurabilir; isim cümlesi ise anlık bir anırma değil, ses hakkında süreklilik taşıyan bir değerlendirme sunar. Eşeğin çağrısı işitilebilir karşılaştırma örneğidir; bu benzetme her eşeğin aynı sesi çıkardığını ya da yüksek insan seslerinin eşek sesine dönüştüğünü söylemez.

Ses adı üç biçimde geri döner: önce muhatabın tekil ve iyelikli {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin}, ardından {ar:ٱلْأَصْوَٰتِ, tr:al-aṣwāt, gloss:sesler} çoğulu, en sonda tekil {ar:صَوْتُ ٱلْحَمِيرِ, tr:ṣawtu al-ḥamīr, gloss:eşeklerin sesi}. Çoğul halka kişinin sesini geniş işitilebilir alana bağlar; sondaki tekil de bu alanı eşek sınıfından bir ses örneğinde toplar. İnsan ve hayvan sesi ortak duyulabilirlikte karşılaşır, anlamca özdeşleşmez; bildirilen çoğul çözümleme de tekil örnekle birlikte olasılık olarak kalır. Son eşek tamlamasının yinelenen ses adlarından sonra daha ağır, pürüzlü bir iniş bırakması ve {ar:أَنكَرَ, tr:ankara, gloss:en itici} sözcüğünün sesler alanından önce sert bir kontur vermesi kıraat izlenimleridir; seslerin gerçek anlamını belirlemez. Bu yerel yankı muhatabın sesini eşek sesiyle bir tutmadan, öğütte düzenlenen sesi hükmün sonundaki örneğe bağlar.

## Görünür hareket, duyulur ses

Bir önceki sahnede (31:18) insanlara küçümseyerek yüz çevirme ve yeryüzünde taşkın sevinçle yürüme uyarıları yan yana gelir: {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-n-nās, gloss:insanlara küçümseyerek yüzünü çevirme} bedensel uzaklaşmayı, {ar:وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī l-arḍi maraḥan, gloss:yeryüzünde taşkın sevinçle yürüme} taşkın ve huzursuz devinimi görünür kılar. {ar:مُخْتَالٍ, tr:mukhtālin, gloss:kibirle gösteriş yapan} kibirli yürüyüş gösterisini, {ar:فَخُورٍ, tr:fakhūrin, gloss:övüngen} kendini övüp büyütmeyi adlandırır. Odaktaki {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğrultuyu ve ölçüyü gözet} aynı iradeli yürüyüşe yönelince gösteriş, doğru çizgi ve orantı kazanır. Kibirli gösteri bu yön değiştirmeyi; ayrı bir taşıyıcı olan {ar:مَرَحًا, tr:maraḥan, gloss:taşkın neşe ve huzursuz devinim} ise karşıt aşırılıklar arasında orta ölçüyü tetikler. Bu bağlam yürüyüşteki düzeltmeyi görünür kılar; bedensel hareket sürer ve öğüt yalnızca tevazu anlamına daralmaz.

31:18’deki yüz çevirme ve övünme sahnesinden sonra (31:18), {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesinden bir miktar kıs} söze işitilebilir bir karşılık verir. {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin} muhatabın kendi çıkışını, {ar:ٱلْأَصْوَٰتِ, tr:al-aṣwāt, gloss:sesler} geniş işitme alanını, eşeklerin çağrısı ise bu alanın somut ses örneğini belirler. Kamusal kendini öne çıkarma bedenin yanında sesle de duyulur; azaltma sözü sürdürürken düzeyini indirir. Bu iki ayet birlikte okunduğunda bedenin ve sesin ölçülü kamusal varlığına dair ihtiyatlı bir yorum açılır: ortak alanı kaplama iddiası küçülürken amaçlı hareket ve duyulur konuşma sürer. Eşeğin adı bu karşılaştırmada işitsel örneği sağlar; insan karakteri hakkında hüküm ya da kesin bir ses eşiği vermez.

Bu beden ve söz birlikteliği, 25:63’te alçakgönüllü yürüyüşün bilgisizce söylenene barışla cevap vermenin yanında yer almasıyla başka bir görünüm kazanır. Odaktaki {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünü doğru ölçüde tut} ile {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} birlikte düşünüldüğünde ölçülü beden ve sözü tırmandırmayan cevap kamusal sükûnet oluşturabilir. 25:63 cevabın içeriğini gösterir; sesin fısıltı düzeyinde olduğunu değil.

Bu öğüdün bir önceki basamağında (31:17) iyiliği emretme, yanlışı engelleme ve sabretme vardır: {ar:وَأْمُرْ بِالْمَعْرُوفِ, tr:waʾmur bil-maʿrūf, gloss:iyiliği emret}, {ar:وَانْهَ عَنِ الْمُنْكَرِ, tr:wanha ʿan al-munkar, gloss:yanlışı engelle} ve {ar:وَاصْبِرْ, tr:waṣbir, gloss:sabret}. Tanınıp iyi sayılanla geri çevrilen yanlış arasındaki bu sözlü düzeltmenin ardından, odaktaki ses yargısı aynı kelime ailesinden bir yankı taşır: {ar:الْمُنْكَرِ, tr:al-munkar, gloss:tanınmayan ya da geri çevrilen yanlış} ile {ar:أَنكَرَ, tr:ankara, gloss:en itici ve yadırgatıcı} aynı aileden gelse de farklı biçim ve görevlerdedir. Odaktaki {ar:أَنكَرَ, tr:ankara, gloss:en itici} seslere üstünlük yargısı getirir; komşu {ar:الْمُنْكَرِ, tr:al-munkar, gloss:geri çevrilen yanlış} sözcüğüyle biçim ve görev ayrılığı, onu yanlış anlamından ayırır. Bununla birlikte, tanımama ve geri çevirme çağrışımı yanlışı dile getiren sözün de itici ya da anlaşılmaz olabileceğini düşündürür. Böylece sesin azaltılması, konuşmayı sürdürürken düzeltmenin nasıl iletildiğine de dikkat çeker; bu komşu bağlamdaki yankı belirli bir ton ya da güçsüz konuşma buyurmaz.

## Sesi işitmek, sözü tanımak

20:108’de insanlar çağırana sapmadan uyar, sesler alçalır ve sonunda yalnız fısıltı duyulur. Bu ayrıntılar, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde yönü ve ölçüyü gözet} içindeki hedefe sapmadan yönelme ile {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} içindeki ses azaltmayı dikkatli yöneliş bakımından buluşturur: çağrıyı izleyen hareket ve işitilebilir sesin kısılması birbirine alan açar, böylece alçak ses dinlemeyi de kolaylaştırabilir. 31:17’deki düzeltme ve 31:18’deki yürüyüş uyarısı da 31:19’un komşu bağlamıdır; 20:108’deki çağrı, odaktaki iki talimatın aynısı değildir.

Sese ulaşmakla onu anlamlı bir hitap olarak tanımak ayrı şeylerdir. 31:6’daki dikkati başka yöne çeken konuşma ve rehberlikten sapma, 31:7’deki kibirle yüz çevirme ve kulağa ağırlık çökmüş gibi işitmeme ayrı ayrı bu ayrımı görünür kılar. Bu iki sahne, {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin} ve {ar:ٱلْأَصْوَٰتِ, tr:al-aṣwāt, gloss:sesler}in duyulur alanı ile {ar:أَنكَرَ ٱلْأَصْوَٰتِ, tr:ankara al-aṣwāt, gloss:seslerin en iticisi} karşılaştırmasını yeni bir açıdan buluşturur: ses kulağa fiziksel olarak ulaşsa da anlamlı söz olarak tanınmayabilir. Bir şeyi tanınmaz kılma, kabul etmeme ve zor yadırgatıcı bulma yönündeki sözlüksel kullanımlar bu ihtimali beslerken, elatif biçim ses karşılaştırması olarak kalır. Eşekler bu karşılaştırmada sesin hayvansal kaynağıdır; toplumsal anlam ve işitmeme sahnesi insana aittir. Bu temas ses yargısına sözün toplumsal etkisi bakımından ahlaki bir kenar ekler, akustik değerlendirmeyi de korur.

Bu sahnelerde dinleyenin anlaması ve uyması kendi seçimi olarak kalır; bu çerçevede sesi kısmak, konuşanın etkisini kendi üzerinde sınırlayan bir iletişim biçimi olarak okunabilir. Böylece öğüt, sessizliğe çekilmeden ve daha yüksek sesle kabul zorlamadan dinleyiciye cevap alanı bırakır. Bu bağlamsal çıkarım görgü ve ses düzeyi anlamlarını korur; her dinleyicinin dirençli olduğunu varsaymaz.

Bir sesin etkisinin şiddete bağlı olmadığını düşündüren iki ayrı dayanak vardır: 31:16’da kayanın, göğün ya da yerin içinde gizli kalabilecek hardal tanesi kadar küçük şey bilgiden kaçmaz; 31:28’de işitme açıkça anılır. İlki gizli küçüklüğün de bilinebildiğini, ikincisi işitmeyi doğrudan öne çıkarır. Bu sahneler, {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} ve işitilebilir {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin} ile buluşunca, dışarıdan gösterilen ses yüksekliğinin etki ve duyulmanın tek ölçüsü olmadığı bir analoji kurar: kısık söz de sonuç doğurabilir. İlahî incelik ve işitmeden insan konuşmasına uzanan bu benzetme, her alçak sözün aynı sonucu vereceği anlamına gelmez; odaktaki doğrudan emir yine ses düzeyini kısmaktır.

Ses azaltmanın duyulur aralıkta kalması, dua için 17:110’da getirilen iki sınırda açıkça görünür: sesi aşırı yükseltmemek ve bütünüyle kısmamak. Bu üst ve alt sınır, {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} buyruğunu sessizliğe değil, duyulabilir bir orta kayda yerleştirir. Dua sahnesi 31:19’daki öğütten ayrıdır; burada kısmanın işitilebilirliği sıfırlamadığını gösteren bir karşılaştırma sunar.

Ses düzeyine ilişkin başka bir ilişki, saygı ve içtenlikle ilgilidir. Elçi’nin yanında sesin yükseltilip alçaltılması saygıyı, alçak sesin takva sahibi kalplerle ilişkisi ise içsel niteliği görünür kılar (49:2, 49:3); 7:205’te anma, içten alçakgönüllülük ve sesi yükseltmeme yan yana gelir. Bu ayrı bağlar, {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} buyruğunu akustik ayara ek olarak muhataba hürmet çağrışımıyla duyurur. Bu temas 31:19’un muhatabını Elçi olarak belirlemez ve öğüdü ibadet sahnesiyle sınırlandırmaz.

Yumuşak hitabın ses düzeyiyle aynı şey olmadığını, Musa ile Harun’a Firavun’a yumuşak söz söylemelerinin emredildiği sahne gösterir; amaç, belki onun öğüt alması ya da sakınmasıdır (20:44). Bu yumuşaklık bir ses ölçümü değildir. Yine de {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ighḍuḍ min ṣawtika, gloss:sesini alçalt} ile {ar:صَوْتِكَ, tr:ṣawtika, gloss:senin sesin} yan yana düşünülünce, ses denetimi zor bir muhataba etkin ve nazikçe yöneltilen hitabı da genişletir; 31:19’un muhatabını Firavun olarak belirlemez.

## Yürüyüşün yönü ve sınırı

Ölçülü dış tutumla iç bağlılık arasındaki ilişki, 31:22’de Allah’a bütünüyle yönelme ve en sağlam kulpa sarılma imgesiyle birlikte düşünülebilir. Bu geniş etik bağlam, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde düzgün doğrultuyu gözet} buyruğundaki itidalin iç bağlılık zayıflığı anlamına gelmediğini düşündürür. 31:22 yürüyüşten söz etmediğinden, bu bağ 31:19’a geriye dönük kurulur; 31:24’teki ölçek kıyası bu özel ilişkiye ek bir dayanak sağlamaz.

İnsan bedeninin sınırları, böbürlenerek yürümenin yasaklandığı ve insanın yeryüzünü yarıp geçemeyeceği, dağlara da erişemeyeceğinin hatırlatıldığı sahnede belirginleşir (17:37). Bu bağımsız beden sınırı, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğru çizgiyi tut} buyruğundaki iradeli hareketle buluşunca ölçüyü insanın gerçek kapasitesine uydurur. Bu benzetme, ölçülülüğü yalnızca tevazuya indirgemez.

Yön ve duruş, yüzüstü ve yolunu şaşırmış ilerleyenle dimdik, düz yolda yürüyenin karşılaştırıldığı başka bir sahnede belirginleşir (67:22). {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğru yönü izle} hem gerçek yürüyüşü hem doğru çizgiyi taşıdığı için, bu karşılaştırma hızı aşarak bedenin hangi yöne ve nasıl döndüğünü görünür kılar. 67:22 böylece 31:19’a yönün bedendeki görünüşünü ekleyen ayrı bir benzetmedir; onu 31:19’un örtük konusu yapmaz.

Yürüyen bedenin duruşundan ayrı bir ölçekte, yeryüzüne sağlam dağların yerleştirilip onun insanlarla birlikte salınmasının önlendiği sahne vardır (31:10). Bu sabitlik, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğrultuyu koru} ile buluşunca durgunluktan çok dinamik dengeyi düşündürür: yürürken çizgiden sapmayı düzeltmek. Yeryüzünün istikrarı ile insanın adımları arasındaki çapraz ölçekli ilişki bir benzetmedir, kozmolojik eşdeğerlik değil.

Sürekli gidişin başka ölçekleri Güneş ile Ay’ın belirlenmiş bir sona doğru akışında ve denizin dirençli ortamında ilerleyen gemide görülür (31:29, 31:31). Güneş ile Ay’ın akışı hedefli ve sonlu gidişi, geminin denizde ilerleyişi ise dirençli bir ortamda sürdürülen güzergâhı öne çıkarır. Bu iki ayrı hareket, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde amaçlı ve düzgün ilerle} buyruğundaki hedefe yönelmeyi, doğru çizgiyi ve iradeli yürüyüşü tek adımın ötesinde sınırları olan bir güzergâh gibi düşündürür. Göksel ve denizci hareketler insan yürüyüşünü tanımlamaz; olağan davranış öğüdünü genişleten analojiler olarak katkı sunar.

Bu sürekli güzergâhlardan ayrı olarak, 31:32’de birbirine karışan dalgaların çalkantısından kurtarılıp karaya çıkarılma sahnesinin ardından biri {ar:مُّقْتَصِدٌ, tr:muqtaṣidun, gloss:aşırılıklar arasında ölçülü kalan} diye nitelenir. Aynı kelime ailesinin bu sonraki biçimi, {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-iqṣid fī mashyika, gloss:yürüyüşünde doğru ve ölçülü ilerle} ile buluşunca düz yürüyüşü krizden sonra yeniden kazanılan bir seyir gibi düşündürür. 31:32’deki niteleme bedensel hareket olmadan da bir tutumu sınıflandırır; bu bağlantı çalkantıdan sonra ölçülü yön tutma imgesi sunar, fiziksel yürüyüşü tanımlamaz.

</source_prose>
