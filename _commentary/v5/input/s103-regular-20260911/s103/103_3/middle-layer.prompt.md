# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **103:3**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.middle.claims.json`

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
- Refer to source paragraphs as `103:3 ¶N`.

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

`(103:3 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "103:3",
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
        "citation": "(103:3 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s103-regular-20260911/s103/103_3/103_3.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s103-regular-20260911/s103/103_3/103_3.middle.claims.json \
  --ayah-ref 103:3
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s103-regular-20260911/s103/103_3/103_3.prose.editorial.tr.md`

<source_prose>
Bu âyet, insanın kayıp içinde olduğunu bildiren hükmün hemen ardından, o hükmün dışında kalanları gösterir: inananlar, iyi ve onarıcı işler yapanlar, gerçeği ve sabrı birbirlerine tavsiye edenler. Başındaki {ar:إِلَّا, tr:illâ, gloss:ancak ve hariç}, önceki cümlenin durduğu yerden duyulur; sesli bir yeniden başlangıç yaparken hükme geri dönüp istisnanın kapısını açar. Ardından gelenler bağımsız bir nitelikler listesi olarak değil, kayıp teşhisine verilen cevap olarak görünür. İstisna, çıkışı belirsiz bir ihtimal halinde bırakmaz; güvenmekten sabra uzanan dört yüklemi aynı çatı altında tutarak kimlerin bu hükmün dışında kaldığını açıkça kurar.

{ar:ٱلَّذِينَ, tr:ellezîne, gloss:kimseler ki} belirli bir kabileyi veya önceden verilmiş sabit bir etiketi adlandırmaz; kimlerin istisnaya girdiğini ardından gelen fiillerin göstereceği bir ilgi cümlesi açar. Önceki genel insan teşhisi (103:2) tekil bir hava taşırken burada çoğul bir sınıfa açılır. Bu çoğulluk cevabı tek kişinin iç durumuna kapatmaz: her kişi kendi eylemini yaparken güven, iş ve iki karşılıklı yükleme ortak bir pratik alanında birleşir. İlk {ar:وَ, tr:ve, gloss:ve} güveni işle aynı düzeyde bağlar; ikinci {ar:وَ, tr:ve, gloss:ve} güven ve işten topluluk içinde yürüyen yüklemelere döner; son {ar:وَ, tr:ve, gloss:ve} dördüncü şartı ekleyip iki bāʾlı cümleyi birbirine eş bir çift olarak kapatır. Bu ilerleme bağlaçların kendi zaman anlamından değil, dört yüklemin cümle içindeki düzeninden doğar.

## Güvenin İşe Dönüşmesi

İlk fiil olan {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} açık bir nesne almadan gelir. Bu biçim, inanılan şeyin adını arka plana alıp güven ve emniyet hâlini öne çıkarır; bağlılık, adı konmamış bir nesneden çok yerleşmiş bir güven durumuna bağlanır. Geçmiş biçim ve çoğul sonu bu hâli gerçekleşmiş bir grubun ilk şartı yapar. Önceki kayıp hükmüne (103:2) ilk cevap burada verilir, fakat bu cevap sonraki iş ve karşılıklı yüklemelerle tamamlanır. Kelimenin güvenlik, güvenilirlik ve bağlanma yönü, tercümedeki “inanma”yı yerleşmiş bir güven taahhüdü olarak da duyurur. İsim hükmünden sonra gelen ilk tamamlanmış çoğul fiil olması kaçış zincirini başlatır; sesin açılıp kapanarak bu hâle yerleşmesi de başlangıcın işitsel ağırlığını artırır.

İlk bağlacın ardından gelen {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler}, güvenle eşlenen ayrı bir şart olarak hareketi dışarıya taşır. Geçmiş biçimde, çoğul özneyle ve nesne alarak gelen bu fiil, bilerek ortaya konan bir işi ve doğrudan işi yapan bir faili gösterir. Hemen arkasındaki {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} işi belirsiz bir faaliyetten iyi, düzgün ve onarıcı bir yöne çevirir. Bu kelime insanları değil, çalışmanın yöneldiği bilinen iyileştirici işler sınıfını adlandıran belirli dişil çoğul bir isimdir; sıfat kökenli oluşu “iyi olan” niteliğini yapılan işin doğrudan nesnesi haline getirir. Böylece güven dışarıdan görülen işe, iş de bozulmuş olanı düzeltmeye bağlanır. Belirlilik işareti biraz sonra gelecek belirli hak ve sabır adlarını biçimsel olarak hazırlar; üç ad aynı görevde değildir, fakat her biri sınırlı ve tanınabilir bir yük alanı açar. İman ile iyi eylemin birlikte durduğu paralel (95:6), bozuluşu önleyen kulluk (29:36) ve tamamlanan işten sonra sürdürülen çaba (94:7), bu güven-eylem-onarım temasını kendi bağlamlarında görünür kılar.

## Karşılıklılığın Kapanışı

Ortadaki ikinci bağlaç, {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilini iyi işlerin yalnızca açıklaması değil, kendi başına eklenmiş üçüncü bir şart olarak açar; bu şart, önceki güven ve iş hareketinin topluluk içinde nasıl sürdürüldüğünü görünür kılar. Cümlede böylece 2+2'lik bir hareket duyulur: önce güven ve iş, sonra birbirine yönelen iki uygulama. Fiilin karşılıklılık bildiren biçimi, öğüdü tek yönden aşağıya indiren bir buyruktan farklı olarak herkesin hem ilettiği hem de kendisine iletileni aldığı bir ilişki kurar. Bu seyrek biçimin başka bir aktarım biçimiyle sınırlı karşıtlığı yatay danışma çerçevesini belirginleştirir; kabul edilmiş varyantlar bu çerçeveyi aydınlatır ve kanonik yüzeyi korur. İlk tevâsav, ardından ikinci kez duyulacak fiilin yankısını hazırlar. Fiilin içine yerleşen karşılıklı taraflar ile arkasındaki {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} birbirinden ayrıdır: biri kimlerin birbirine yöneldiğini, bāʾlı tamlama ise aralarında taşınan şeyi gösterir. Tavsiye bu yüzden tek bir sesin pasifçe dinlenmesi değil, topluluğun yükü birlikte dolaştırmasıdır; bu ilişki 90:17'de iman, sabır ve merhametle birlikte görünür.

{ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} içindeki bāʾ, hakkı ilk karşılıklı yüklemenin içeriği ve ona ulaşmanın yolu olarak bağlar. Belirli artikel taşıyan bu ad, belirsiz bir kanaat yerine tanınan ve sınırları olan bir hakikat-hak alanı açar. {ar:حَقِّ, tr:hakk, gloss:gerçek, hak ve borç} yüzeyi doğruluğu taşırken aynı anda sahibine ait payı, yerine getirilmesi gereken hakkı ve bağlayıcı borcu da duyurabilir; bu genişleme “gerçek” anlamına bir yükümlülük ve hak ediş boyutu ekler. Bāʾ ile belirli adın birbirine sıkıca bağlanması bu yükü başlangıçtaki güvene geri bağlayan anlamsal ve işitsel bir halka kurar. Aynı bāʾlı kalıbın sabırla tekrarlanması, hakikat ile sabrı birbirine eritmeden eşlenmiş iki topluluk görevi olarak karşı karşıya getirir.

Son bağlaç ikinci {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilini yeniden tam biçimiyle kurar. Bu tekrar, hakikat için bir kez söylenmiş fiile iki nesne eklemekten çok, aynı karşılıklı mekanizmanın iki ayrı kez işletildiğini gösterir. {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} bu ikinci fiilin bāʾlı tamamlayıcısıdır; sabır ikinci karşılıklı yüklemenin taşınan içeriğidir. Son {ar:وَ, tr:ve, gloss:ve}, şartlar zincirinin üçüncü ve son sayım vuruşu olarak sabrı hakikatin içine saklamaz, ayrı bir toplumsal görev halinde ekler; iki bāʾlı cümleyi de sıkı bir eşleşme olarak tutar. Tekrarlanan fiilin sibilantlı sesi kulağı son ada kadar taşır ve kapanışı geciktirerek hazırlar; ağırlık salt ses gösterisinden değil, olağan tekrarın cümle içindeki işinden gelir.

{ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} son yük olarak sarsıntı ve yakınma dürtüsüne karşı kendini tutmayı, doğru çizgide kalmayı ve çözülmeyi önlemeyi somutlaştırır. Belirli fiilimsi isim biçimi, emredilen bir buyruğu değil, karşılıklı olarak taşınan bilinen bir niteliği anlatır; bāʾlı yapı onu doğrudan tevâsav fiiline bağlar. Kabul edilmiş farklı hareke aktarımı son ada sınanma ve baskı altında dayanma rengini katabilir; yerel tamlama sabır ve kendini tutma anlamını korur. Âyetin ve sûrenin son kelimesi olması, güven, iş, onarım ve hakikatten sonra diziyi dayanıklı bir tutunmayla yere bastırır; diğer şartlar da bu kapanışta yerini korur. Hakikatin yönü ve bağlayıcılığı ile sabrın bu yönü baskı altında sürdüren gücü aynı kalıpta kapanır, fakat iki ayrı yük olarak duyulmaya devam eder.

## Kayıptan Çıkışın İşleyen Biçimi

Bu dört şart, açık istisna anlamını koruyarak kendi kendini sürdüren bir düzenek gibi de işleyebilir. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} içindeki doğru sayıp kabul etme yönü, hemen yanındaki {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} fiilinin dışa dönük ve bilerek yapılan işiyle buluşur: güven uygulamaya giren bir taahhüt olur. {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} bu işi bozulmaya karşı onarıma çevirir. İki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiili {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} ile {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} yüklerini insanlar arasında dolaştırır; bakım tek kişinin içindeki bir özellik olmaktan çıkar. Hakikatin gerçeğe uygun ve sağlam olma yönü ortak düzenin ölçüsünü verir, sabrın kendini tutma yönü de hakikatin yön verdiği işi sarsıntı altında sürdürerek halkayı korur. Zaman ve kayıp zemini (103:1, 103:2), iman ve iyi eylem (95:6), sürdürülen çaba (94:7), ıslah (29:36), karşılıklı tavsiye (90:17), ölçü (42:17) ve pratik sabır (31:17) bu düzenekle ayrı ayrı temas eder. Bu, dört şartın açık anlamına eklenen keşifsel bir işleyiştir.

Fiillerin sırası sınırlı bir paralellik içinde nedensel bir uygulama devresi gibi de duyulabilir: kabul yön verir, bilinçli eylem bu yönü işletir, iyi ve onarıcı oluş yapılan işin niteliğini denetler, hakikat onu sağlam bir ölçüyle kalibre eder, karşılıklı tavsiye düzeltmeyi grup içinde dolaştırır, sabır ise gerilim altında sürdürür. Sözle eylem arasındaki hesap (61:2) {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} fiilinin işletici hareketini; bozuluşa karşı ıslah (29:36) {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} yüzeyinin kalite yönünü; iman, sabır, merhamet ve karşılıklı tavsiye (90:17) {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilinin dolaşımını; hak ile ölçünün birlikte anılması (42:17) {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yükünün ayarını; iyiye çağırma, kötülüğü engelleme ve sabır kümesi (31:17) ise son tutmayı görünür kılar. Sıralama böylece yalnız yan yana duran bir liste değil, kendini yeniden kuran bir işleyiş gibi okunabilir; tek bir cümle tek başına bütün neden ilan edilmez.

Bu işleyiş zaman içinde yinelenen bir aktarım olarak da açılır. {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin yaş ve ardışık zaman yönü, iki kez yinelenen {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilinin bağlama ve bitişik sürdürme yönüyle temas edince, istisna birbirine eklenen zaman aralıklarında taşınan bir bağlılık gibi görünür. Tavsiye bir anda sahip olunan bir sıfat olmaktan çıkıp kişiler arasında yeniden kurulan bir aktarım kazanır; aynı anda gerçekleşen öğütleşme de canlı bir ihtimal olarak yerini korur. Önceki zaman çerçevesi (103:1), aşamalı aktarım (17:106), başkasına bırakılan vasiyet (2:180) ve karşılıklı taşıma (90:17) bu sürekliliğe temas eder. Tekrar, bir kurum adı vermeden sorumluluğun kişiler arasında ileriye aktarılmasını görünür kılar; bu aktarım belirli bir grubun tüzüğünü değil, süreklilik kazanan sorumluluğu ifade eder.

Bu parçalar birlikte, güveni başlangıç koşulu, gerçeği sabit ölçü, sıkı kuruluşu taşıyıcı biçim, ağır sınavı dayanılacak zemin, işi çalışan hareket ve karşılığı emeğin somut payı yapan daha geniş bir kurtuluş düzeni de düşündürür. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} güvenilir bir alan açar; {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} hem kesin doğruluk hem de parçaların yük taşıyacak kadar sağlam bağlanması yönüyle bu alanı sınar; {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} ağır durumu (2:214) taşır; {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} işi sürdürür (94:7) ve emeğe karşılık kazandırır (2:195); tevâsav da parçaları toplumsal olarak etkin tutar (90:17). Bu bileşim zaman, baskı ve kayıp karşıtlığı (103:1, 103:2) içinde, hak, kuruluş, ağır sınav, iş, karşılık ve toplumsal tavsiye temaslarını bir araya getirir. Bu bağlantı, genel kayıp ya da sıkıştırma için ayrıca kurulmuş bir taşıyıcı sunmadığından bu alanların özgül mekanizmasını doğrudan adlandırmaz.

## Birbirini Taşıyan İnsanlar

İstisna grubu yalnız tek tek güvenli kişilerden oluşan bir sığınak değil, üyelerinin birbirleri için ürettiği bir toplumsal barınak olarak da duyulabilir. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} korkunun kalkması ve iç yatışıklığıyla güven koşulunu kurar; iki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilinin bağlama ve bitişik sürdürme yönü insanları ve yükümlülükleri tek bir sürekliliğe ekler; {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} içindeki başkasının yükümlülüğü için güvence verme yönü sabrı birbirinin yükünü üstlenmeye genişletir. İman, karşılıklı sabır ve merhametin birlikte anılması (90:17) bu görüntünün bağımsız dayanağıdır. Güven ve tevâsav böylece güvence üreten sığınak ilişkisini görünür kılar; bu ilişki kapalı bir kurum tanımlamaz.

Aynı topluluk, {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} yüzeyinin görünür, yabanıl olmayan ve yabancılığı gideren yakınlık yönüyle, yabancılaşmış tekil insandan güvenilir bir çoğulluğa yeniden kurulmuş olarak da görünebilir. {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} içindeki barışma ve uzlaşma yönü sosyal hasarı giderir; tevâsav insanların birbirine yapılacak şeyi bildirmesiyle bu onarımı dolaşıma sokar. Kardeşlik ve uzlaştırma (49:10), iman, sabır, merhamet ve karşılıklı tavsiye (90:17), en küçük kasıtlı işin görünür karşılığı (99:7) bu ilişki alanına ayrı ayrı temas eder. Buradaki ağ güven, amaçlı eylem, uzlaşma, kefalet, doğruluk ve bağlanma üzerinden çalışır; ayrı düşme için bağımsız bir taşıyıcı bulunmadığından bu bağlantı kopuşu ayrıca kurmaz. İnsan kelimesinin yalnızca tür adı olarak okunması da açık kalır.

İnsan ve yakınlık görüntüsü başka bir ihtiyatlı hatta geçmişten taşınan bir toplumsal konuma açılır. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} adının belirli bir Arap boyunu ayırt eden özel ad olarak duyulması, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin köken, soy, soylu kaynak ve alt bağlılık yönleriyle birleştiğinde topluluğu zaman boyunca taşınan bir aidiyet çizgisi gibi gösterir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} yüzeyinin yakın arkadaşta görünen mevcudiyeti bu çizgiye tanınabilir bir çevre verir. Böylece istisnaya giren insan hem güvenilir yakınlık içinde toplumsal bir konum, hem de miras alınmış bir aidiyet içinde duran biri olarak duyulabilir. Bu bağlamsal görüntü, toplumsal arka plan olarak soy, boy veya miras alınan konumu görünür kılar; bunlar istisnanın şartı veya belirli bir nesep üstünlüğünün dayanağı değildir.

## Hak, Emanet ve Ölçü

Hak ve tavsiye, bağlayıcı bir görevle korunacak payın birbirine bırakıldığı emanetli bir düzen olarak da okunabilir. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} içindeki bağlayıcı gereklilik ve sahibine bağlı pay yönü, başkasına ait bilinen hakkı ödenebilir bir borç gibi duyurur (70:24). {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin iş üzerinde görev ve yetki üstlenme yönü, vasiyetle birlikte idare edilen bir sorumluluğa dönüşür (2:180); {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilinin başkasına bırakılan talimat yönü bu sorumluluğu bir taşıyıcıdan diğerine geçirir. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} emanet taşıyan tarafın güvenilirliğini, {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} ise başkasının yükümlülüğü için güvence veren ve doğabilecek maddi yükü üstlenen kişiyi görünür kılar. Emanet sorumluluğu (33:72), hak ve borç (70:24), akrabalıkla çevrili vasiyet (2:180) bu hukuki ve vasiyetli analojinin temaslarıdır. Hesap verilebilirlik eklenir; belirli bir mahkeme, tereke, dava veya kurum kurulmaz.

Bu emanet duygusu önceki kaybın karşısında bir karşı-defter görüntüsü de alabilir. {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin iş karşılığı ücret ve çalışanın payı yönü, harcama ve ihsanın emeğe maddi-toplumsal bir karşılık vermesiyle buluşur (2:195). {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} içindeki bağlayıcılık, {ar:حَقِّ, tr:hakk, gloss:gerçek, hak ve borç} adının belirli sahibine ait istem payıyla birleşerek bu karşılığı hesapta tutar; tavsiyenin talimat yönü de vasiyet biçimiyle yükü başkasına bırakılabilir kılar (2:180). Kayıp baskısı (103:2), bilinen hak (70:24), maddi ihsan (2:195) ve karşılıklı taşıma (90:17) bu hesabın farklı yüzleridir. Ekonomik görüntü emeği, hakkı ve devredilen işi görünür kılar; bu bağlantıda belirli bir alacak, işlem veya kişi tayin edilmez.

İyi iş ile hak, eksik teslim sonrasında kişiler arasındaki ölçüyü yeniden kuran bağlama uygun bir onarım süreci olarak da duyulabilir. {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin karşılıklı işlem yönü, adil ölçü ve ahdi tamamlama çizgisiyle buluşarak işi eksik bırakılmış bir alışverişi onaran harekete çevirir (6:152). {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} içindeki barışma yönü gerilmiş ilişkiyi giderir (4:128); sana veya yöneldiği kişiye uygun olma yönü ise onarımın her duruma aynı biçimde uygulanmadığını gösterir (47:5). {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} neyin zorunlu olduğunu ve geri dönüşün hangi hak sahibine ait olduğunu belirler (70:24). Böylece ölçü soyut bir denge değil, ilişkide yerine ulaşan bir karşılık olur; bu çıkarımsal iadenin alıcısı ve miktarı açık bırakılır.

Hak aynı zamanda karşılıklı iddiaların dile getirildiği ve sınandığı disiplinli bir doğruluk süreci olarak açılabilir. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin tarafların kendi savını doğru sayarak çekişmesi yönü, adalet için şahitlik eden sorumlulukla buluşur (4:135); aynı yüzeyin doğruyu kanıtla gösterme yönü haberin doğrulanmasıyla somutlaşır (49:6). {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} bu sınamayı tek kişinin hükmü olmaktan çıkarıp grup içinde dolaştırır; {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} barışma ve uzlaşma yönüyle bağı onarır (4:128), {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} ise çekişmenin kopuşa dönüşmemesine katkı verir (31:17). Süreç, hakikati söyleme, iddiayı sınama ve bağı koruma hareketini birlikte taşır; anlaşma kendiliğinden garanti edilmez ve belirli bir davaya indirgenmez.

## İşlenen Zemin ve Karşılık

İstisna, sermayenin, mülkiyetin ve karşılığın kayıp ihtimali altında kaldığı güvenilir bir alışveriş gibi de duyulabilir. {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} ticari kayba, {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} sahibine bağlı paya, {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} karşılıklı işleme, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} verme, ürün ve çıkarılan kazanca temas eder. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} yüzeyinin sert taş ve taşlı arazi, ayrıca tadı acı ilaçlık öz görüntüleri bu değiş tokuşa zor zemin ve bedel duyusu katar. Başka bir atıflı okumada başkasının hakkının kişinin kazancına çevrilmediği, güvenilir ve onarıcı bir alışveriş düzeni belirir: güven işlemi sabitler, iyilik açığı düzeltir, hak payı sahibine bağlı tutar, tavsiye de akran denetimini açık tutar. Kayıp (103:2), maddi ihsan (2:195), başkasına ait hak (70:24), emanetli vasiyet (2:180) ve karşılıklı tavsiye (90:17) bu ekonomik benzetmenin temaslarıdır. Bu bağlantının kapsamı belirli bir ticaret sahnesi kurmaz.

Kayıp, orantılı bir karşılık isteyen hak edilmiş bir isteme olarak da görünür. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} içindeki bağlayıcı gereklilik, {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} ile birleşince mahrumiyet ile cevabı aynı sürecin iki aşaması yapar. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} yüzeyindeki öldürmeye karşılık ölüm cezası dalı, hak edilmiş karşılığın ölçülü ve denk olma görüntüsünü verir. Bu maddi-hukuki benzetme, önceki kayıp hükmünün cevabındaki basıncı, adil ölçüyü, uzlaşmayı, uygun ıslahı ve hak sahibini karşılığın çerçevesi olarak görünür kılar; sabrın tek anlamı veya âyetin hukuk hükmü olarak belirlenmez (6:152, 4:128, 47:5, 70:24).

Başka bir maddi sahnede {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} eksik ölçü ve tartı, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} sıvı çıkana kadar sıkıştırma ve baskı, {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} ise işe koşma ve kullanma olarak belirir. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} sofra yaygısı, yiyecek yığını ve bir bütünün üst veya yan sınırı görüntüleriyle sıkıştırılan şeyin ne kadar korunup tutulduğunu hissettirir. Emeğin üretken karşılığı hangi noktada mahrumiyete döndüğünü burada görünür kılar: çaba hak edilen paya ulaşmalı, başkasının payı kısalmamalıdır. Baskı altında yapılan iş, {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin doğruluğu kanıtla gösterme yönüyle görünür bir sonuca, onarılmış koşula ve ayakta duran bir hakikate dönüşebilir. Bu baskı görüntüsü, zamanın sıradan ardışıklığıyla birlikte tutulur; bu bağlantıda ölçü kişiler arasında yerine ulaşan bir karşılık olarak duyulur, fakat belirli miktarlar verilmez.

## Baskı Altında Dayanmak

Son yüklemde sabır, sarsıntı ve yakınma dürtüsüne karşı işi sürdüren etkin bir kendini tutma olarak belirir; böylece yalnız sakinlik veya sonucu beklemek olarak kalmaz. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin bineği gücünü aşacak biçimde sert sürme yönü, aşılması zor yokuşla birleşerek bedeli olan bir tırmanış görüntüsü verir (90:11). {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} içindeki kendini tutma yönü duygusal çekilmeyi etkin denetim olarak korur (31:17); çıkışsız ağır durum yönü rahatlamadan önceki sınavı (2:214), kış ayazı yönü zarara rağmen güvenerek dayanmanın dış rahatsızlığını (14:12), {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} içindeki zahmete girme yönü ise dayanmanın bizzat emek taşıdığını gösterir (94:7). Sıkıntı yanında kolaylık (94:5), sabrın taşlı ve dirençli bir zeminde ilerleme biçimini açar. Bu yüzler birleştiğinde beden ve irade işi sürdürecek biçimde tutulur; sabır böylece yalnız acıya veya yalnız beklemeye sığmaz.

Bu gönüllü kendini tutma, dışarıdan uygulanan alıkoymanın karşıt görüntüsü yanında daha da keskinleşir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} yüzeyinin görünür insan varlığıyla, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} yüzeyinin zorla alıkoyma yönü birleştiğinde bir kişi veya canlı dış güçle tutulmuş ve çıkışı engellenmiş olarak görünür; {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} içindeki alıkoyma, geri tutma ve geri alma yönleri bu bedensel tutulma dilini tamamlar. Bunun yanında âyetin sabrı kişinin baskı altında kendi yönünü koruması olarak taşınır. Bu bağlantı gönüllü dayanmanın anlamını görünür kılar; âyette zorlamanın gerçekleştiğine hükmetmez (103:1, 103:2).

Sabrın duyusal bir açılımında daralmış geçiş küçük ve ölçülü rahatlamalarla aşılır. {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin boğazdaki lokmayı geçirmek için küçük yudum alma ve susuzluktan kurumuş dil görüntüleri, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} içindeki acı ve ilaç olarak kullanılan özle temas eder. Dayanma böylece bir anda sonuç beklemekten çok, boğazı açan küçük dozlarla dar geçişi adım adım mümkün kılan zor bir araç gibi duyulur. Aynı sabır yüzeyinin acı ağaç özü, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin ise el-Asra adlı ağaçla buluştuğu başka bir görüntüde, keskin tatlı meyve ile ilaçlık öz aynı canlı kaynağın büyüme, ürün, acılık ve fayda geçmişine bağlanır. Bu sahneler, sabrın olağan dayanma anlamına duyusal bir çevre ekleyen bağlamsal, keşifsel ve deneyimsel benzetmelerdir; sabrın sözlük karşılığının yerine geçmez ve âyette gerçek bir boğaz, meyve veya ağaç sahnesi kurmaz.

Bu acı madde görüntüsü, tevâsav ile toplumsal bir uygulamaya dönüşür. {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} topluluk üyelerinin zor içeriği birbirine aldırmasını ve tekrar tekrar taşınabilir kılmasını sağlar; {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} ise hüküm gelene kadar izleme (10:109) ve pratik sabırla (31:17) birleşerek zor ama sürdürücü bir ilaç gibi duyulur. Karşılıklı tavsiye (90:17) bu ilacın topluluk içindeki taşıyıcısıdır. Bu özellikle şaşırtıcı sahne, tevâsavın zor içeriği toplulukta taşımasını ve sabrın bu içeriği sürdürmesini duyusal olarak bir araya getirir; biçim bilgisi veya öğreti yerine geçen bir açıklama değildir.

Gerçeğin bedene içerden ulaşması da ayrı bir ihtiyatlı görüntü açar. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin iç boşluğa ulaşan düz saplanış ve {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin mızrağın sivri ucuna yakın ön bölüm yönleri, sözün yüzeyde kalmadan sonucuna ulaştığını hissettirir. {ar:خُسْرٍ, tr:husr, gloss:kayıp ve eksilme} kayıp ve aşağılığın türemiş biçimleriyle bu etkinin karşısındaki düşüşü, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} ise kaçışı zor ağır duruma tutunmayı taşır. Böylece hakikatin etkisi ve sabrın baskı altında yönü koruması belirginleşir; maddi zarar ve darbe görüntüsü bu bağlantının sınırlı maddi biçimidir, hak ile sabrı şiddetin literal adlarına dönüştürmez.

## Biriken, Olgunlaşan ve Besleyen

Zaman ve sabır arasındaki temas biriken bir kapasite görüntüsü kurar. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} yüzeyinin katmanlı beyaz bulut yönü, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin yağmura dönüşen bulut yönüyle birleşince dayanma zaman içinde biriktirmek, yoğunlaştırmak ve sonunda çevresine besleyici bir sonuç bırakmak olarak görünür. Bulutun katman katman oluşması ve taşıdığı yağmuru bırakması kapasite ile salınan bereket arasındaki hareketi verir. Yağmur bulutu, dayanmanın zaman içinde birikip çevresine besleyici sonuç bırakmasını görünür kılan sınırlı bir ek görüntüdür; odakta bunun için yeterli bağımsız taşıyıcı kurulmadığı için sabrın sözlük karşılığının yerine geçmez (103:1).

Aynı yetişme hareketi uygunluk ve işe elverişlilik üzerinden açılır. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin üç yaşını tamamlayıp dördüncü yaşında yük taşımaya elverişli hale gelen deve yönü sonucu taşıyacak olgunluğu görünür kılar; yine aynı yüzeyin art ayağını ön ayak izine basan at yönü gelişmiş kapasitenin tekrarlanan uyumunu hissettirir. {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin gençliğe veya ergenliğe ulaşma yönü büyümenin eşiğini, {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin işe yatkınlık ve dayanıklılık yönü kullanılabilir çalışma gücünü, {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} ise kapasitenin iyi ve yerinde kullanılmasını taşır. Böylece iyi işler, olgunlaşmış bir imkânın uygun yerde işe koşulmasıyla kullanılabilir ve sonuç verebilir oluşunu görünür kılar; hesaba eklenmiş soyut ağırlıklar olarak değil, olağan iyi iş anlamını koruyan bir benzetme içinde duyulur (103:1, 94:7).

Yetişme aynı zamanda canlı ile çevresinin birbirine uymasıdır. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar ve güvene girdiler} güvenilirlik, {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin devenin veya sürünün beslenerek iyice semirmesi, {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} yüzeyinin uygunluk ve iyileşme, iki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} yüzeyinin ise otlağın sürüye elverişliliği ve topluluğun birbirine yapılacak şeyi bildirmesi yönleriyle bir araya gelir. Önceki zaman, bulut ve kolaylık görüntüleri (103:1, 94:5), uygun ıslah (47:5) ve sürdürülen iş (94:7) bu temasa ayrı ayrı katkı verir: canlıyı besleyen ortam, ortama uygun canlı ve bu ortamı sürdüren karşılıklı bakım aynı yetiştirme sahnesinde birleşir. Otlak, sürü, bulut ve ürün ayrıntıları, bu bağlantıda güven, uygunluk, beslenme ve karşılıklı hizmetin keşifsel ekolojik görüntülerini ayrı ayrı taşır; tek tek kelimelerin tercümesi olarak kurulmaz.

Korunan ürünün başka bir görünüşünde {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} kabuğuyla çevrili ekin, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} ise sofra yaygısı, yiyecek yığını ve dolma sınırı olarak duyulur. Uygulamalar büyürken korunur, sonra toplanıp sınırına kadar biriktirilir ve paylaşılabilir bir azığa dönüşür. Sabır bu süreçte değeri koruyup olgunlaşmasını sağlayan koşuldur. Kabuğun ürünü çevrelemesi, yaygının yiyeceği taşıması ve yığının sınıra kadar dolması ayrı maddi ayrıntılardır; bunlar önceki zaman görüntüsüyle (103:1) temas eden, odaktaki yüklemlerin olağan anlamını zemin alan bağlamsal bir benzetmedir.

## Uyumlanan Hareket ve Görünürlük

Çoğul özne, tekrarlanan eylemin açtığı birbirine bağlı adımlarla taşlı zemini geçen bir yolcu topluluğu gibi de görünebilir. {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin yürünmüş ve işlek hale gelmiş yol yönü, {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:ardışık zaman} yüzeyinin tek eylemden yolculuğa uzanan ardışık hareketiyle birleşir. {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} bir adımı başka adıma bağlar; {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} art ayağın ön ayak izine basan atı, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} sert, kalın ve düz taşlı araziyi görünür kılar. Böylece iyi iş ve sabır ayrı kişilerde duran özellikler olmaktan çıkıp koordineli ilerlemeyi mümkün kılan ortak bir pratiğe dönüşür. Bu maddi benzetme, ardışıklık, işlek yol, birleşen adım, iz ve taş ayrıntılarının koordineli ilerlemeye katkısını görünür kılar; odak kelimelerinin sözlük çevirisi değildir ve gerçek bir sefer kurmaz.

Bu hareket, yönü, bedeni, bineği ve aracı birbirine uyan bir çalışma düzeni olarak da duyulabilir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} yüzeyinin insana dönük veya yakın yan yönü, {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} yüzeyinin iş gören beden parçası ve mızrağın sivri ucuna yakın ön bölüm yönleriyle temas eder. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} atın ayak izini, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır ve dayanma} bütünün üst veya yan sınırını, {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} ise parçaların birbirine eklenmesini taşır. Uygulama böylece doğru yön, uygun birleşme ve tekrarlanan uyum sayesinde etkili olan bedensel bir koordinasyon kazanır; maddi sahne bu bağlantıda sefer anlatısı olarak kurulmaz.

İnsan kelimesinin görünürlük tarafı, eylem ve hakikati gören bir gözün görüntüsünü de açabilir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} yüzeyinin görme, duyma ve duyumsamayla bir şeyi fark edilir kılma yönü, göz bebeğindeki küçük insan sureti ve sınırlı ayna görüntüsüyle birlikte düşünülür. {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} burada çalışan bir beden parçası gibi, {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} ise doğruluğu kanıtla belirleyip gösteren bir hakikat gibi görünür. {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} bu algıyı ortak doğrulamaya çevirir: gerçek tek kişinin özel izlenimi olarak kalmayıp sınırlı insanların birbirine gösterdiği ve birlikte sınadığı görünürlük haline gelir. Bu görüntü insan ve kayıp zeminine (103:2) cevap verir; bu bağlantı gerçekliğin bütünüyle elde bulunan bir önerme olduğunu varsaymaz ve olağan hak anlamının yerini almaz.

## Birleşen Parçalar

İyi iş ile gerçek, işlenmiş malzemenin ve sağlam kurulmuş sözün gevşemeden bir arada durması gibi duyulabilir. {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} bozulmuş olanı onarır; {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} kapasiteyi işe koşar; {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} kumaş ipliklerinin sıkı ve düzgün dokunması, ayrıca iki parçanın birleştiği eklem görüntüsüyle yapılan işin taşıyıcı biçimini verir. Doğruluk böylece yalnız söylenen bir nitelik değil, emekle kurulmuş ve gevşemeden duran bir tutarlılık gibi hissedilir. Bu dokuma ve işçilik görüntüsü, eylem ile gerçek anlamların üzerine eklenen odak içi bir analojidir; onların yerini almaz.

Bu yapıda {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} yüzeyinin sana veya yöneldiği kişiye uygun olma yönü, ilk {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiilinin bağlama hareketiyle buluşunca her iyileştirici işin yöneldiği ihtiyaca oturan bir parça gibi görünür. İki tevâsav fiilinin başka şeyi başka şeye bağlama ve bitişik sürdürme yönü {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yükünü ortak eklem noktası yapar. {ar:حَقِّ, tr:hakk, gloss:gerçek, hak ve borç} sınırlı bir adlandırma kümesindeki eklem yeri gibi, iki parçanın döndüğü ve birbirini taşıdığı bir yer verir. {ar:صَبْرِ, tr:sabr, gloss:sabır ve dayanma} yüzeyinin üst veya yan sınır yönü bu birleşime bir çalışma kenarı, şişe ağzını kapatan tıkaç yönü ise bütünü taşırmadan kapatan bir mühür gibi eklenir. Bu malzeme ayrıntıları, hakikat ile sabrın olağan anlamlarının yanında duran imgesel bir yapı kurar; 90:17'deki karşılıklı taşıma yük paylaşımını, 94:5'teki sıkıntı yanında kolaylık ise yapının dayanmasını görünür kılar.

Başka bir malzeme okumasında hakkın eklem görüntüsü ilişkiye uygun birleşme noktasını, sabrın dağların orta kesimi görüntüsü ise büyük bir kütlenin merkezini belirler. Hak bu görüntüde ilişkiyi eklemde tutar; sabır ise bütünün merkezinde taşıyıcı ağırlık kazanır. İki görüntü aynı maddi açıklamaya indirgenmeden son iki yüklemin nerede birleşileceğini ve nerede durulacağını hissettirebildiğini gösterir. Bu iki yüz, 90:17'de iman, sabır, merhamet ve karşılıklı tavsiye ile 94:5'te sıkıntı yanında kolaylığın bağlanmış yapıya verdiği desteğe temas eder.

103:1'in baskı ufkunda bu parçalar, her biri ayrı iş görerek basınç altında dağılmayan bir düzenek gibi okunabilir: {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} yüzeyinin sıkı ve düzgün dokunmuş iplikleri ahlaki sıraya yük taşıyan kuruluş verir; {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} yüzeyinin sınır yönü basıncın dağıtacağı şeyi çevreler; {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyileştirici ve düzgün işler} her parçayı kendi kişisine ve durumuna uydurur; {ar:عَمِلُوا۟, tr:amilû, gloss:yaptılar ve iş gördüler} çalışan hareketi sağlar (94:7). Verilen dil ve dudakların kuruluşu (90:9), sıkıntı karşısındaki kolaylık (94:5), uygun ıslah (47:5) ve sürdürülen iş (94:7) bu düzenek görüntüsünün temaslarıdır. Sıkı kuruluş ve sınır, parçaların birbirine uyarak basınçta tutulmasını anlatan bir analoji olarak görünür.

Bu örme görüntüsünde tekrarlanan cümleler, hakikat ve sabır yüklerini birbirine bağlayan iplikler gibi duyulur. {ar:بِٱلْحَقِّ, tr:bi'l-hakk, gloss:gerçek ve hak} kumaş ipliklerinin sıkı dokunmuş biçimini, iki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine tavsiye ettiler} fiili başka şeyi başka şeye bağlayarak sürekliliği, {ar:بِٱلصَّبْرِ, tr:bi's-sabr, gloss:sabırla ve dayanmayla} ise başkasının yükümlülüğü için güvence veren ve yükü üstlenen kefil ipliğini görünür kılar. Karşılıklı iman, sabır ve merhamet (90:17) ile sıkıntı yanında kolaylık (94:5) bu örmenin bağımsız temaslarıdır. Güç tek tek bir iplikte değil, bağlanmış ve yükü paylaşan yapıda belirir; kumaş veya kap görüntüsü âyetin gerçek sahnesi değildir, açık istisna cümlesi bu maddi analoji içinde de karşılıklı taşıma olarak kalır.

</source_prose>
