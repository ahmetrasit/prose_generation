# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:38**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.middle.claims.json`

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
- Refer to source paragraphs as `17:38 ¶N`.

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

`(17:38 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:38",
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
        "citation": "(17:38 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_38/17_38.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_38/17_38.middle.claims.json \
  --ayah-ref 17:38
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_38/17_38.prose.editorial.tr.md`

<source_prose>
## Hükmün Alanı

17:38, önceki yönlendirmeleri yeniden sıralamak yerine onların toplamına ilişkin hükmü bildirir. {ar:كُلُّ ذَٰلِكَ, tr:kullu dhālika, gloss:bütün bunlar} önceki söyleme dönerek alanı bir bütün olarak kapsar; içindeki {ar:ذَٰلِكَ, tr:dhālika, gloss:işaret edilen} bu geriye dönük göndermeyi kurar. Buna karşılık {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} iyelik bağıyla toplamın kendisini değil, onun içindeki kötü niteliği seçer. Böylece kapsam bütünüyle değerlendirmeye girer, fakat her öge kötü diye nitelenmez: farklı davranışlar düz bir sayımda kalmayıp Rabbin hükmünde buluşur. Olağan gönderge, 17:23'te başlayan ve 17:37'ye uzanan yönlendirme dizisidir (17:23, 17:37); alt sınır ayrıca belirtilmediğinden yalnızca en yakın yasaklar da olası gönderge olarak kalır. Uzak işaretin katkısı aynı toplamı geriye dönüp değerlendirme önüne getirmektir: bu söyleyiş etkisi fiziksel uzaklık ya da kişiye yöneltilmiş duygusal itham bildirmez.

Toplam alana dönen işaretin ardından {ar:كَانَ, tr:kāna, gloss:oldu}, buyruklardan davranış hakkındaki yerel bildirim hükmüne geçişi kurar. Bu, önceki yönlendirmelerin nasıl değerlendirildiğini söyleyen yerel bir dönüş; yeni bir buyruk ya da sûre çapında yinelenen bir kalıp değildir. Özne konumundaki isimleşmiş nitelik {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı}, iyelikle belirlenmiş kötü yönü yargının konusu yapar ve göndergenin tamamına eşitlemez. Eril tekil mansup yüklem {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} edilgen ortaç olarak bu niteliği reddedilmiş bir statüye koyar; faili adlandırmaz ve hoşnutsuzluğu duygu ile iradi uzak durma arasında belirlemez. Yüklemin eril tekil uyumu cümleyi tamamlar; kötülük, ret ve değerlendirme arasındaki ilişkinin tümünü tek başına tayin etmez. Mazi biçimli {ar:كَانَ, tr:kāna, gloss:oldu}, oluş ve bulunma bağını bu yükleme taşıyarak reddi anlık bir tepki yerine hüküm içinde yerleşmiş durum gibi duyurur. Bu yerleşiklik zamansızlık iddiası değildir ve hükmü bir insanın geçici duygusuna indirgemez.

İki odak sözcük farklı katkı yapar. {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} kötü, çirkin ya da niteliği bozuk yönü seçer; {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} bu niteliği reddedilmiş kılar. Kusur önce tanınır, ardından onay dışı bırakılır; bu temas sınırlı bir ayıplama çağrışımı taşır, ancak isim açık bir eleştiri fiili ya da eleştireni adlandırmaz. Böylece burada ahlaken sakıncalı ve sonuç doğurabilecek bir nitelik belirir; başka kullanımların bütün zarar çağrışımları bu isme taşınmaz. Hemzenin tilavetteki işitilebilir kesintisi kötü niteliğin keskinliğine ses yoluyla eşlik eder. Bu işitsel katkı sözlük anlamını kanıtlamaz ve tek başına 17:7 ya da 17:32 ile özel bir yankı ilişkisi kurmaz (17:7, 17:32).

## Rabbin Katında

Hükmün ilişkilendirildiği çerçeveyi {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbinin katında} kurar. {ar:عِندَ, tr:ʿinda, gloss:katında} olağan olarak yakınlık ya da huzurda bulunmayı taşır; {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} bu huzurun makamını adlandırır. Öbek yüklemden önce geldiği için değerlendirme bütün yargıyı da özellikle son reddedilmiş statüyü de kapsayabilir; sözdizimi bu kapsamı kesinleştirmez. Yakınlık çekirdeği korunarak Rabbin huzurunda olma, {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} hükmünü ahlaki değerlendirme alanına taşır ve reddin güçlü niteliğini belirginleştirir. Dayanak doğal tiksinme, akli değerlendirme ya da dinî-ahlaki sakınca olabilir; bağlam sonuncusunu öne çıkarır, fakat retin belirli bir duyguya veya teknik hukuk sınıfına bağlanmasını ve reddeden failin adlandırılmasını sağlamaz. Böylece yakınlık dili ahlaki yargıyı kuvvetlendirir; ilişki fiziksel bir mahkeme sahnesi olarak kurulmaz.

Bu ilişkide {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin}, {ar:عِندَ, tr:ʿinda, gloss:katında} tarafından yönetilen tamlayandır. Unvanın düzenleme ve gözetme yönü, {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbinin katında} bağıyla son ret hükmüne katılır: kötü davranış başıboş bir etiket değil, Rabbin yönetimi altındaki bir yargı olarak duyulur. Bu yakın bağlam sahiplik ve buyurma çağrışımlarına da ihtiyatlı yer açar; tek başına kök ortaklığı unvanın bütün anlamlarını yüklemez. {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} içindeki ikinci tekil şahıs eki muhatabı ilişkiye kişisel olarak dahil eder; hitabın bu kişiselliği ayrı bir kural ya da başka bir nitelik getirmez.

Bu kişisel yargı, 17:23'te {ar:قَضَىٰ, tr:qaḍā, gloss:kesin hüküm verdi} ile açılan buyruk düzeni ile 17:39'da görünen vahiy, hikmet, sonuç uyarısı ve nihai dışlanma ufkuna bağlanır (17:23, 17:39). 17:39'daki {ar:أَوْحَىٰٓ, tr:awḥā, gloss:vahyetti}, {ar:حِكْمَةِ, tr:ḥikma, gloss:hikmet}, {ar:تُلْقَىٰ, tr:tulqā, gloss:atılırsın} ve {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} ifadeleri sırasıyla vahiy kaynağını, hikmetli yönetimi, sonucu ve dışlanmayı belirginleştirir. Bu çerçevede 17:38 ayrı yönlendirmelerin pratik sonuçlarını bir toplu kapanışta mühürler; gönderge geniş buyruk dizisi yerine yalnızca en yakın yasaklarla da sınırlı olabilir.

Hitabın kişisel Rablik ufku 1:2'deki {ar:رَبِّ الْعَالَمِينَ, tr:rabb al-ʿālamīn, gloss:âlemlerin Rabbi} unvanıyla genişler (1:2). 17:38'in muhatabına dönük {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} hitabı korunurken değerlendiren otorite bütün âlemlere uzanan bir Rablik alanında duyulur. Bu Fâtiha bağlantısı, 17:38'de söylenmeyen kapsamı ekler; önceki yönlendirmelerin açıklaması ya da odak ayetin sözlerinin değişmesi değildir.

Rab unvanının yönetme anlamı yanında, aşama aşama yetiştirip tamamlamaya dönük bir yankısı da düşünülebilir. 17:24'te merhamet {ar:رَّحْمَةِ, tr:raḥma, gloss:merhamet} ve {ar:ٱرْحَمْ, tr:irḥam, gloss:merhamet et} sözleriyle dile gelir; aynı ayetteki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni büyütüp yetiştirdiler} fiili çocukken yetiştirilmenin somut imgesini verir (17:24). Bu fiil {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} ile aynı köktendir, fakat ayrı bir biçimdir; aralarındaki temas eşdeğerlik değil, dilsel bir yakınlıktır. Etik yönlendirmelerin toplanması ve ardından gelen ret, 17:24'teki merhamet ve yetiştirme diliyle birlikte düşünüldüğünde, Rabbin koruyup olgunlaştıran yönetimini de hissettirir; bu biçimlendirici yankı egemen hükmün yanında durur. İlahi Rablik insan ebeveynliğiyle özdeşleştirilmez ve bu bağlantı tam bir ıslah programı sunmaz. Ayrıca 17:24'teki güvence ebeveynlik bağlamına özgü kalabilir; bu nedenle yetiştirme yankısı olası ve sınırlı bir katkıdır.

## Yönlendirmelerin İçindeki Ayrımlar

Rab unvanının yetiştirme yankısından ayrı olarak, toplayıcı {ar:كُلُّ, tr:kullu, gloss:bütün} mevcut yönlendirme alanının hiçbir parçasını dışarıda bırakmaz; zamana yayılan bir yetiştirme sürecini anlatmaz. Toplanan alanın her ögesi kötü değildir: 17:23'te {ar:إِحْسَٰنًا, tr:iḥsānan, gloss:iyilikle davranma} ve {ar:كَرِيمًا, tr:karīman, gloss:değerli ve saygın} söz, 17:35'te {ar:خَيْرٌ, tr:khayrun, gloss:iyilik} anılır (17:23, 17:35). Böylece {ar:كُلُّ, tr:kullu, gloss:bütün} bütün alanı kapsarken iyelikli {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} yalnızca içindeki kötü niteliği seçer, {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} da o payı reddeder. Gönderge yalnız yasaklarla sınırlı olabilir ve ayrı yönlendirmeler tek bir gerekçeyi paylaşmak zorunda değildir.

İyelikli kötü nitelik kusuru kişinin sabit kimliği yerine fiil ve niteliğe yöneltir; 17:25 bu ayrımın kişiyi onarıma açık tutan tarafını belirginleştirir (17:25). Oradaki {ar:أَعْلَمُ, tr:aʿlamu, gloss:daha iyi bilen} ve {ar:نُفُوسِ, tr:nufūsi, gloss:içsel benlikler} kişinin içini bilen değerlendirmeyi, {ar:صَٰلِحِينَ, tr:ṣāliḥīna, gloss:ıslah olanlar} ve {ar:أَوَّٰبِينَ, tr:awwābīna, gloss:dönenler} onarılma ile dönüş olanağını, {ar:غَفُورًا, tr:ghafūran, gloss:bağışlayıcı} ise bağışlanma ihtimalini açar (17:25). Böylece {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} hükmü fiili reddedebilirken kişiyi değişmez bir kötü sınıfına kapatmaz. Bu imkân koşulludur: bağışlanma şartsız vaat edilmez ve 17:25'teki güvence ebeveynlere ilişkin buyruk bağlamında kalabilir (17:25).

Tek bir harcamadan tekrarlanan pratiğe ve onun toplumsal anlamına geçişi 17:26 ve 17:27'deki ifadeler birlikte görünür kılar (17:26, 17:27). 17:26'daki {ar:تُبَذِّرْ, tr:tubadhdhir, gloss:savurursun} ve {ar:تَبْذِيرًا, tr:tabdhīran, gloss:savurganlık} maddi saçılmayı, yinelenen davranışı adlandırır (17:26). 17:27'deki {ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşler} ve {ar:شَّيَٰطِينِ, tr:shayāṭīni, gloss:şeytanlar} bu pratiğin ilişki ve aidiyet boyutunu; {ar:شَّيْطَٰنُ, tr:shayṭānu, gloss:şeytan} ile {ar:كَفُورًا, tr:kafūran, gloss:nankör} ise şeytanî yakınlığı nankörlükle bağlayan niteliği belirginleştirir (17:27). {ar:كُلُّ, tr:kullu, gloss:bütün} tekrarlanan pratiği de kapsayınca toplu hüküm, maddi saçılmanın zaman içinde ilişki ve aidiyeti biçimlendirebileceğini düşündürür. Bu genişleme yinelenen davranışa ilişkindir: 17:27'de kardeşlik benzetme düzeyinde kaldığı için tek bir harcama kişiye sabit şeytanî kimlik vermez (17:26, 17:27).

Aidiyet imgesinden sonra 17:29'daki iki el hareketi ölçü sorununu somutlaştırır: {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} boyna bağlanmış eli, {ar:تَبْسُطْ, tr:tabsuṭ, gloss:uzatırsın}, {ar:بَسْطِ, tr:basṭi, gloss:uzatma} ve {ar:كُلَّ, tr:kulla, gloss:bütünüyle} ise elin tümüyle açılmasını gösterir; birlikte tutma ile aşırı açma uçlarını kurarlar (17:29). 17:30 başka bir ölçek ekler: {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçülü kılar} rızkı genişletme ve daraltmayı ilahi takdire bağlar (17:30). Bu iki uçla ölçü fikri yan yana gelince, {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} ve {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} bakımından reddedilenin eli tutmak ya da vermek değil, kullanımda ölçüyü yitirmek olabileceği belirir. El imgesi insanın harcamasında, rızkın genişleyip daralması ilahi takdirde kalır; bu temas tek bir bütçe formülü vermez.

17:32 eylemden önceki yaklaşmayı sakınılacak bir yolla anlatır: {ar:تَقْرَبُ, tr:taqrabu, gloss:yaklaşırsın} yaklaşma hareketini, {ar:سَبِيلًا, tr:sabīlan, gloss:yol} güzergâhı, {ar:سَآءَ, tr:sāʾa, gloss:kötü oldu} ise o yolun kötülüğünü belirtir (17:32). 17:33 ayrı bir eşik kurar: öldürme ve {ar:حَقِّ, tr:ḥaqqi, gloss:hak} üzerinden yetki sahibinin karşılık verirken {ar:يُسْرِف, tr:yusrif, gloss:sınırı aşar} ile ölçüyü taşırmaması istenir (17:33). Bu iki imge bir arada, {ar:كُلُّ, tr:kullu, gloss:bütün} ile toplanan davranış alanını yaklaşma anından zarar sonrasındaki karşılığa kadar genişletebilir. Bağlantı bir neden-sonuç zinciri değildir: 17:32 zarar gören bir kişiyi belirtmez, 17:33'teki öldürme de o yasak yolun sonucu olarak sunulmaz (17:32, 17:33).

Bu davranış çizgisinde {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} için ayrı bir sözlüksel kullanım da araştırılabilir: birini istemediği bir eylemi yapmaya zorlama. Bu olası sözlük anlamı odaktaki edilgen ret hükmünün yerini almaz; onun çevresinde istenmeyen yükün kime aktarıldığı sorusunu açar. 17:29'daki boyna bağlanmış el kendi kendini tutma imgesini, 17:33'te hakkın sınırlandırılması yetkinin ölçüsünü, 17:39'daki {ar:حِكْمَةِ, tr:ḥikma, gloss:hikmet} ise düzeltici yönelişi sunar (17:29, 17:33, 17:39). Bu ayrı katkılar zorlamanın toplumsal maliyetini düşündürür; ayetler bir zorlayıcıyı doğrudan göstermediğinden bağlantı keşifseldir.

Yaklaşma ve hak sınırının ardından 17:34 ve 17:35'te iki ayrı hesap dayanağı belirir (17:34, 17:35). 17:34'te {ar:عَهْدِ, tr:ʿahdi, gloss:ahdi} ile verilen söz ve {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır} ile ondan beklenen cevap hesap verilebilirliği kurar (17:34). 17:35'te {ar:أَوْفُ, tr:awfū, gloss:eksiksiz yerine getirin}, {ar:كَيْلَ, tr:kayla, gloss:ölçü}, {ar:زِنُ, tr:zinū, gloss:tartın}, {ar:قِسْطَاسِ, tr:qisṭāsi, gloss:ölçü aleti} ve {ar:مُسْتَقِيمِ, tr:mustaqīmi, gloss:doğru} eksiksizliği, tartıyı ve doğru standardı elle tutulur kılar (17:35). 17:38'deki {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbinin katında} bu yargı huzuruyla temas edince kötü davranış, Rabbin katında hesabı verilecek bir davranış olarak da okunabilir. Bu, bağlamlar arası bir çıkarımdır: 17:38 defter ya da ticaretten söz etmez; 17:34'teki ahit ve 17:35'teki ölçü kendi ayetlerinin konusu olarak kalır (17:34, 17:35).

Hesap verilebilirliğin hemen öncesinde 17:36 davranışı bilgi sınırı ve hesap verme içinde gösterir (17:36). {ar:تَقْفُ, tr:taqfu, gloss:izini sürersin} bilgi olmadan izlemeyi, {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} bilginin eşiğini; {ar:السَّمْعَ, tr:al-samʿa, gloss:işitme}, {ar:بَصَرَ, tr:baṣara, gloss:görme} ve {ar:فُؤَادَ, tr:fuʾāda, gloss:kalp} ise davranışa yön veren yetileri adlandırır; bunların sorgulanacağını {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır} tamamlar (17:36). Bu sıra, işitme, görme ve kalbin yön verdiği davranışın sorumluluğunu 17:38'deki toplu hükme bağlar. Ayrıca odaktaki {ar:كُلُّ, tr:kullu, gloss:bütün}, {ar:ذَٰلِكَ, tr:dhālika, gloss:işaret edilen}, {ar:كَانَ, tr:kāna, gloss:oldu} yapısı ve {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} hükmü, 17:36'nın kendi {ar:كُلُّ, tr:kullu, gloss:bütün} ve {ar:كَانَ, tr:kāna, gloss:oldu} tekrarlarıyla biçimsel bir yankı kurar (17:36). Tamamlayıcılar farklı olduğu için bu temas davranış sorumluluğunu güçlendirir; kasıtlı alıntı olup olmadığı açık kalır.

17:37 kibirli iç durumu yürüyüşe, oradan da bedenin erişemediği sınırlara taşır (17:37). {ar:مَرَحًا, tr:maraḥan, gloss:kibirli sevinçle} taşkın iç hâli, {ar:تَمْشِ, tr:tamshi, gloss:yürürsün} görünür hareketi kurar; {ar:تَخْرِقَ الْأَرْضَ, tr:taḵriqa al-arḍa, gloss:yeri yararsın} yeri yarma girişimini, {ar:الْجِبَالَ طُولًا, tr:al-jibāla ṭūlan, gloss:dağların yüksekliği} ise erişilemeyen yüksekliği ekler (17:37). Bu görüntü dizisi insanın kendi gücünü aşırı büyütmesini somutlaştırır. 17:38'deki {ar:عِندَ, tr:ʿinda, gloss:katında} değerlendirme ve {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} unvanının yönetme-egemenlik boyutuyla temas edince, kibir görgü kusurunun ötesinde yaratılmış gücün ölçüsünü aşma olarak da okunabilir. Dağlar bu bağlantıda 17:37'nin ölçek imgesidir; 17:38'in kendisi onlardan söz etmez (17:37).

## Yol ve Hesap Ufku

{ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyen} için sert, kaba arazi anlamı, reddedilen davranışın pürüzlü güzergâh gibi duyulmasına ayrı bir sözlüksel dayanak sağlar. 17:32'deki {ar:سَبِيلًا, tr:sabīlan, gloss:yol} güzergâhı adlandırır; 17:37'de yürüme imgesi hareketi, yeri yarma girişimi ve erişilmez dağ yüksekliği ise arazinin direncini somutlaştırır (17:32, 17:37). Bu iki bağımsız bağlam bir araya gelince, olağan “hoş görülmeyen” hüküm korunarak davranış aşılması güç, pürüzlü bir rota gibi belirir. Fâtiha 1:6'daki {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} isteği ile 1:7'deki yön karşıtlığı, bu pürüzlü rotanın yanına talep edilen doğrultuyu koyar (1:6, 1:7). Bu karşılaştırmanın katkısı yön farkını belirginleştirmektir; 1:7'deki gruplarla özdeşlik kurmaz ve Fâtiha'yı S17'nin açıklaması yapmaz.

Yol ve yön ilişkisinden ayrı olarak, Fâtiha 1:4'teki {ar:مَالِكِ يَوْمِ الدِّينِ, tr:māliki yawmi al-dīn, gloss:hesap gününün sahibi} Rabbin değerlendirmesine hesap ve karşılık için bir zaman ufku ekler (1:4). Bu bağlantı yerel hükmü hesap gününe dönük bir ufukta duyurur; zaman çerçevesi Fâtiha'dan gelir, çünkü 17:38 hesap gününü ya da gelecekteki bir olayı adlandırmaz.

43:35'te dünya hayatının geçici yararları ahiret ufkuyla karşılaştırılır; aynı ayetteki {ar:كُلُّ ذَٰلِكَ, tr:kullu dhālika, gloss:bütün bunlar} ve {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbinin katında} kalıpları bu karşılaştırmayı 17:38'e biçimsel olarak bağlar (43:35). Böylece odaktaki Rabbin değerlendirmesi daha geniş bir dünya-ahiret ufkunda duyulur. Kalıp benzerliği bu özel bağlantıyı destekler; 43:35'in göndergesi kendi bağlamında kalır ve 17:38'in öncül listesini belirlemez.

6:132 yapılan işlere göre farklı dereceler bulunduğunu bildirir (6:132). Bu katkı, {ar:كُلُّ, tr:kullu, gloss:bütün} ile toplanan alanı herkese aynı ağırlık ya da sonucun verildiği tek bir ölçek gibi okumamayı sağlar: ameller derecelere göre farklılaşır. 6:132 bu temasla kapsamlı değerlendirmenin derece farklılıklarını açık tutar, fakat 17:38'in hangi yönlendirmeleri topladığını belirlemez.

## Hak, Yakınlık ve Dönüş

2:282 hak ve ölçüyü vadeli borcun adaletle yazılması içinde somutlaştırır (2:282). Hakkın eksiltilmemesi ve şahitlerin bulunması koruma düzenini kurar; yazdıramayan ya da güçsüz olan kişinin işinin vekil aracılığıyla adil yürütülmesi bu korumayı ona da taşır. Ayet bu usulü {ar:ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ, tr:dhālikum aqsaṭu ʿinda Allāh, gloss:bu Allah katında daha adildir} diye niteler (2:282). Borçlunun {ar:رَبَّهُۥ, tr:rabbahū, gloss:onun Rabbi} diye anılması da 17:38'deki {ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin} ile sahiplik ve düzenleyici yetke çağrışımını hakların korunmasına bağlar. Bu temas, odaktaki Rabbin katını hak ve ölçünün değerlendirildiği bir ufuk olarak duyurur; 17:38'in konusu borç usulü değildir.

42:40 kötülüğe denk karşılığı ve bağışlayıp düzeltme yolunu yan yana getirir (42:40). {ar:وَجَزَٰٓؤُا۟ سَيِّئَةٍۢ سَيِّئَةٌۭ مِّثْلُهَا, tr:wa-jazāʾu sayyiʾatin sayyiʾatun mithluhā, gloss:kötülüğün karşılığı onun dengi bir kötülüktür} karşılığın ölçüsünü korur; {ar:فَمَنْ عَفَا وَأَصْلَحَ, tr:faman ʿafā wa-aṣlaḥa, gloss:kim bağışlar ve düzeltirse} ise af ve onarımı açık tutar (42:40). Bu iki hareket, {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} çevresinde hem hak ve ölçüyü bozan davranışın reddini hem de düzeltme imkânını düşündürür. Bağlantı bu iki katkı arasındadır; 17:38'in ayrı yönlendirmelerini tek bir kategoriye indirmez.

{ar:عِندَ, tr:ʿinda, gloss:katında} hem fiziksel yakınlığı hem değerlendirme konumunu taşıyabilir; 8:35 ilk kullanımı somutlaştırır. Orada {ar:صَلَاتُهُمْ عِندَ ٱلْبَيْتِ, tr:ṣalātuhum ʿinda al-bayt, gloss:Evin yanındaki namazları} Kâbe yakınındaki fiziksel yeri belirtirken namazın ıslık ve el çırpmadan ibaret sayılması, yere yakınlığın uygulamayı kendiliğinden doğrulamadığını gösterir (8:35). Değerlendirme kullanımı ise 2:282'de {ar:أَقْسَطُ عِندَ ٱللَّهِ, tr:aqsaṭu ʿinda Allāh, gloss:Allah katında daha adil} ile adalete, 61:3'te {ar:مَقْتًا عِندَ ٱللَّهِ, tr:maqtan ʿinda Allāh, gloss:Allah katında büyük nefret} ile söz-eylem uyuşmazlığına bağlanır (2:282, 61:3). 61:3'teki {ar:أَن تَقُولُوا۟ مَا لَا تَفْعَلُونَ, tr:an taqūlū mā lā tafʿalūn, gloss:yapmadığınızı söylemeniz} o ayetin kendi örneğidir; buradaki karşılaştırma onu 17:38'e taşımaz (61:3). Bu örnekler, 17:38'deki {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbinin katında} için yakınlık çekirdeğini korurken, özel bağlantının fiziksel koordinat değil Rabbin değerlendirme huzuru olduğunu belirginleştirir.

{ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} için açılan kuşatma imgesi, önce sözcük türlerini ayırt etmeyi gerektirir. {ar:سَاءَهُ, tr:sāʾahu, gloss:onun üzüntü duymasına yol açtı} sıkıntı doğuran bir eylemi anlatan fiildir; odaktaki {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} ise iyelik eki taşıyan isimdir ve bu fiilin anlamını almaz. 2:81'deki {ar:مَن كَسَبَ سَيِّئَةًۭ وَأَحَٰطَتْ بِهِۦ خَطِيٓـَٔتُهُۥ, tr:man kasaba sayyiʾatan wa-aḥāṭat bihi khaṭīʾatuhū, gloss:kim bir kötülük kazanır ve günahı onu kuşatır} başka bir sonuç imgesi sunar: kazanılmış kötülüğün günahı faili sarar (2:81). Buradaki kuşatma {ar:أَحَٰطَتْ, tr:aḥāṭat, gloss:kuşattı} fiiliyle kurulur; odaktaki isimden ayrı bu sözcük, reddedilen kötü niteliğin faili saran bir zarara dönüşebileceğini düşündüren benzetme zeminidir, odağın sözlük anlamı değildir.

2:81'deki kuşatmadan farklı olarak 9:98, önce başkalarının başına felaket gelmesini bekleyenleri, ardından kötülüğün onlara dönmesini anlatır (9:98). {ar:وَيَتَرَبَّصُ بِكُمُ ٱلدَّوَآئِرَ, tr:wa-yatarabbaṣu bikumu d-dawāʾir, gloss:başınıza felaket gelmesini bekler} beklentiyi başkalarına yöneltir; {ar:عَلَيْهِمْ دَآئِرَةُ ٱلسَّوْءِ, tr:ʿalayhim dāʾiratu s-sawʾ, gloss:kötülük çemberi onların üzerine döner} ise yönelişi bekleyene geri çevirir (9:98). Böylece bu imge kuşatmaya değil, zararın geri dönüşüne katkı verir ve {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} çevresinde böyle bir sonucu düşünmeye izin verir. Bu, bu bağlantıya özgü bir olasılıktır: 9:98'deki dönüş her önceki fiilin faili için zorunlu sonuç sayılmaz.

Bu iki sonuç imgesi sözcüklerin sınırları korununca odaktaki hükme katkılarını gösterir. 17:38'de {ar:كُلُّ ذَٰلِكَ, tr:kullu dhālika, gloss:bütün bunlar} olağan biçimde “hepsi” demektir; kuşatma anlamı taşımaz. {ar:الإِكْلِيل, tr:al-iklīl, gloss:taç veya başı saran süslü kuşak} gibi kuşak ya da taç anlamındaki sözlük örnekleri odaktaki {ar:كُلُّ, tr:kullu, gloss:bütün} sözcüğünün anlamını belirlemez; 2:81'deki kuşatma başka kökten gelen {ar:أَحَٰطَتْ بِهِۦ خَطِيٓـَٔتُهُۥ, tr:aḥāṭat bihi khaṭīʾatuhū, gloss:günahı onu kuşatmıştır} ifadesine dayanır (2:81). Bu ayrım, kuşatma ile geri dönüşü {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:onun kötü yanı} için olası sonuç benzetmeleri olarak tutar. Bu özel bağlantı önceki davranışları tek kusura indirmez, fail için belirli sonuç vaat etmez ve 17:39'daki {ar:حِكْمَةِ, tr:ḥikma, gloss:hikmet} temasını bu benzetmeye taşımaz (17:39).

</source_prose>
