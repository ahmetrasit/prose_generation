# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:6**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.middle.claims.json`

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
- Refer to source paragraphs as `17:6 ¶N`.

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

`(17:6 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:6",
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
        "citation": "(17:6 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_6/17_6.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_6/17_6.middle.claims.json \
  --ayah-ref 17:6
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_6/17_6.prose.editorial.tr.md`

<source_prose>
17:6, önceki bir evreden sonra dönüş sırasının karşı tarafa karşı muhataplara geri verildiğini; ardından onların mal ve oğullarla desteklenip daha büyük bir seferberlik gücüne ulaştırıldığını bildirir. Başlangıçtaki {ar:ثُمَّ, tr:thumma, gloss:sonra}, yeni aşamayı gecikerek açar; aradan ne kadar zaman geçtiğini ya da önceki sahnenin ne olduğunu söylemez. Kısa parçacığın ikiz m sesi bu aralığa işitsel bir ağırlık verir: ses, sözlük anlamını değiştirmeden bekleyişi duyurur.

Bu gecikmenin ardından üç geçmiş zamanlı fiil, ilahî konuşanın üç ayrı eylemini sıralar: {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik} dönüşü geri verir, {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:sizi destekledik} kaynak ekler, {ar:وَجَعَلْنَٰكُمْ, tr:wa-jaʿalnākum, gloss:ve sizi daha çok seferberlik gücü kıldık} ise topluluğu daha büyük bir kuvvet durumuna getirir. Son fiilin başındaki bağlayıcı yeni bir fiil cümlesi açar: mallar ve oğullar ikinci eylemin araçları, daha büyük seferberlik gücü üçüncü eylemin sonucudur. Böylece artış, destek listesine eklenmiş bir unsur değil, desteğin ardından gelen ayrı bir değişim olarak duyulur.

## Dönüşün Yönü

İlk eylemde dönüşü yapan muhataplar değil, ilahî konuşandır. Birinci fiil kalıbındaki geçişli geçmiş zaman biçimi {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik}, geri verilen şeyi {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:dönüş sırası} olarak belirler. Yararlanıcıyı bildiren {ar:لَكُمُ, tr:lakumu, gloss:sizin için} dönüş adından önce gelir; böylece okur önce kimin yararına olduğunu, sonra neyin geri verildiğini duyar. Dönüş adının belirli, tekil nesne biçimi bu olayda tek, ayırt edilebilir bir geri verilişi sınırlar. Ardından gelen {ar:عَلَيْهِمْ, tr:ʿalayhim, gloss:onlara karşı} karşı tarafı gösterir, ancak önceki anlatıdaki tarafı yeniden tanımlamaz. İki tamlamanın fiile ya da dönüş adına bağlanması mümkün olsa da birlikte yararlanan taraf ile karşı tarafı aynı olayın iki ucu yapar.

Bu iki uç boyunca muhataplar değişmez: {ar:لَكُمُ, tr:lakumu, gloss:sizin için} dönüşün yararlanıcısını, {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:sizi destekledik} içindeki -kum desteğin alıcısını, {ar:جَعَلْنَٰكُمْ, tr:jaʿalnākum, gloss:sizi bir duruma getirdik} içindeki -kum da sonucu yaşayan topluluğu belirtir. Dilbilgisel görevleri ayrı olsa da aynı topluluğun yararlanıcıdan destek alıcısına, oradan değişmiş sonucun öznesine ilerlemesi yerel bir restorasyon zinciri kurar.

Geri vermek anlamındaki {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik} önceki bir yer ya da duruma dönme yönünü taşır. Dönüş adı {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:dönüş sırası} uzaklaştıktan sonra yeniden gelmeyi anlatır; aynı kelime ailesindeki bazı kullanımları düşmana yeniden yönelme imgesini de taşır. Odaktaki {ar:عَلَيْهِمْ, tr:ʿalayhim, gloss:onlara karşı} bu yönelişi açıkça karşı tarafa çevirirken, geri verme eylemi kaybolan inisiyatifi muhataplara iade eder. Bu temas, sıradan geri dönüşü korurken ona bir karşı hamle tınısı katar. Bu yerel bağlantı belirli bir savaş ya da saldırıyı adlandırmaz.

Bu karşıya yönelişin tarihsel zemini hemen önceki hareketle belirginleşir. Konutların arasından geçen kuvvet 17:5'te {ar:فَجَاسُوا۟ خِلَٰلَ ٱلدِّيَارِ, tr:fa-jāsū khilāla d-diyār, gloss:konutların arasından geçip gittiler} diye anlatılır (17:5). Bu geçişi evlerin içinden ve aralıklarından nüfuz eden bir hareket olarak düşünmek, sahneye ihtiyatlı bir iç yarılma görüntüsü ekler. Ardından 17:6'daki dönüş aynı saldırganlara yönelir; mallar, oğullar ve büyüyen topluluk da bu karşı dönüşe maddi ve toplumsal dayanak verir. İki bozulmanın {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} diye sayılması ve ardından gelen büyük yükseliş (17:4), başlangıçtaki {ar:ثُمَّ, tr:thumma, gloss:sonra} ile birleşince 17:6'yı gecikerek gelen bir tarihsel evre yapar. Bu tarihsel çizgi 17:6'yı yönün çevrildiği bir menteşe gibi okumaya zemin verir: gücün geri kazanılması görünür, karşı girişin fiziksel biçimi bu bağlantıda belirlenmez.

Bu ara evrenin ardından anlatı dönüşü kalıcı bir sona bağlamaz. Yeniden giriş ve yıkım vaadi 17:7'de yer alır ({ar:وَلِيَدْخُلُوا۟ ٱلْمَسْجِدَ كَمَا دَخَلُوهُ أَوَّلَ مَرَّةٍ وَلِيُتَبِّرُوا۟ مَا عَلَوْا۟ تَتْبِيرًا, tr:wa-li-yadkhulū l-masjida kamā dakhalūhu awwala marratin wa-li-yutabbirū mā ʿalaw tatbīrā, gloss:ilk giriş gibi yeniden girip yükseldiklerini bütünüyle yıkmaları}). Bundan sonra merhamet ihtimali açılır ({ar:أَن يَرْحَمَكُمْ, tr:an yarḥamakum, gloss:size merhamet etmesi}) ve “dönerseniz biz de döneriz” koşulu gelir (17:8; {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:eğer dönerseniz biz de döneriz}). Bu sıralama, bu tarihsel anlatı içinde 17:6'yı önceki kayıp ile koşula bağlı yeni karşılık arasında geri çevrilebilir bir ara dönem olarak düşündürür. Bu bağlantı anlatının sınırlı bir imkânını gösterir; genel bir siyasal yasa ya da kaçınılmaz gelecek kurmaz. Buradaki yineleme duygusunu geçmiş zamanlı biçim tek başına kurmaz: {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik} ile {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:dönüş sırası} arasındaki ilişki ve 17:8'deki açık koşullu çift dönüş birlikte bu duyguyu taşır.

Başka kullanımlar geri gelişin sonucunu açık bırakır: aynı kelime ailesinden bir fiil 95:5'te aşağıya döndürmeyi anlatır ({ar:ثُمَّ رَدَدْنَٰهُ أَسْفَلَ سَٰفِلِينَ, tr:thumma radadnāhu asfala sāfilīn, gloss:sonra onu aşağıların aşağısına döndürdük}); dönüşle ilişkili ayrı bir biçim de 79:12'de kayıpla nitelenir ({ar:كَرَّةٌ خَاسِرَةٌۭ, tr:karratun khāsirah, gloss:kayıpla sonuçlanan dönüş}) (79:12). Bu karşılaştırma geri gelişin zorunlu olarak yükseliş ya da başarı olmadığını aydınlatır; 17:6'daki biçimlerin dilbilgisini veya tarihsel olayını belirlemez. Ardından gelen destek cümlesi ise dönüşün hangi kapasiteyle donatıldığını ayrıca gösterir.

## Kaynağın Topluluğa Ulaşması

Dönüşün ardından gelen {ar:وَأَمْدَدْنَٰكُم, tr:wa-amdadnākum, gloss:ve sizi destekledik}, alıcıya dışarıdan yardım ve kaynak ekleyen dördüncü fiil kalıbındaki destek eylemidir. Bu kelime ailesinin somut kullanımları asker, yardımcı kişi, yiyecek ya da mal sağlama gibi yardımları kapsayabilir; ayet ise araç olarak özellikle {ar:بِأَمْوَٰلٍۢ, tr:bi-amwālin, gloss:mallarla} ve {ar:بَنِينَ, tr:banīna, gloss:oğullarla} ifadelerini seçer. Böylece dönüşten sonraki kaynak artışı genel bir yardım düşüncesi olarak kalmaz; cümlenin kendisi neyin takviye edildiğini gösterir.

Mallarla anlamındaki {ar:بِأَمْوَٰلٍۢ, tr:bi-amwālin, gloss:mallarla} sözcüğünün başındaki bağ, varlıkları desteğin aracı yapar; fiildeki -kum ise yardımın alıcısını belirtir. {ar:أَمْوَٰلٍۢ, tr:amwālin, gloss:mallar} belirsiz çoğulu, sözcüğün iç biçimi değişerek kurulur; tek bir meta ya da kapalı bir miktar yerine sahip olunan ve aktarılabilen varlıkların geniş alanını açar. Önündeki bağla aynı araç dizisine giren {ar:وَبَنِينَ, tr:wa-banīna, gloss:ve oğullar} da bu takviyeye katılır. Oğulların gerçek insanî ve soy bağı, mallarla aynı dilbilgisel konumda sunulsa da mülkiyet anlamına gelmez: maddi kaynak ile yaşayan soy ayrı niteliklerini koruyarak topluluğa iki tür dayanak sağlar.

Kaynak ekleme anlamına bu kelime ailesinin çekerek uzatma ve yayılımı artırma çağrışımı eşlik eder. Odaktaki {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:sizi destekledik} dördüncü fiil kalıbında alıcıya yardım ekler; mallar ve oğulların ardından gelen daha büyük topluluk, desteği grubun erişimini genişletiyormuş gibi duyurur. Bu çağrışım desteğin kapsamına yayılım rengi verir; odaktaki fiilin temel anlamı kaynak eklemedir.

Üçüncü eylem bu büyümeyi sonuç hâline getirir. {ar:جَعَلْنَٰكُمْ, tr:jaʿalnākum, gloss:sizi bir duruma getirdik} mevcut muhatapları değişimin etkilenen tarafı yapar; {ar:أَكْثَرَ, tr:akthara, gloss:daha çok} {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü} ise ulaşılan durumu ve artışın ölçüldüğü alanı belirtir. Mevcut topluluk yeni bir kuvvet durumuna sokulur; yoktan başka bir topluluk kurulmaz. Belirsiz nesne biçimindeki {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü}, artışın ölçüldüğü alanı; {ar:عَلَيْهِمْ, tr:ʿalayhim, gloss:onlara karşı} ise karşı tarafı belirtir. Böylece sonuç bu rakibe karşı sayısal bir avantaj olarak belirir; bu bağlantının ölçüsü her bakımdan üstünlük ya da tamamlanmış zafer değildir.

Bu son kuvvet adı bir eylemi değil, topluluğu adlandıran isimdir. İlişkili söz varlığında çağrı üzerine yardım ya da mücadele için çıkma eylemi de bulunur. 9:41'de çıkış çağrısı mallar ve canlarla çaba gösterme sözüyle yan yana durur ({ar:ٱنفِرُوا۟, tr:infirū, gloss:çıkın, seferber olun}; {ar:وَجَٰهِدُوا۟ بِأَمْوَٰلِكُمْ وَأَنفُسِكُمْ, tr:wa-jāhidū bi-amwālikum wa-anfusikum, gloss:mallarınız ve canlarınızla çaba gösterin}) (9:41); 4:71'de ise insanlar gruplar hâlinde ya da hep birlikte çıkmaya çağrılır ({ar:فَٱنفِرُوا۟ ثُبَاتٍ أَوِ ٱنفِرُوا۟ جَمِيعًۭا, tr:fanifirū thubātin aw infirū jamīʿan, gloss:gruplar hâlinde ya da hep birlikte çıkın}) (4:71). İlki seferberlik eylemini maddi ve kişisel çabayla, ikincisi çıkışın grup düzeniyle ilişkilendirir; birlikte odaktaki ismin harekete geçiş yönünü aydınlatırlar. 17:6'daki isim topluluğu adlandırır, belirli bir çağrıyı ya da gerçekleşmiş seferi değil.

Aynı adla ilişkili bir topluluk kullanımı kimi sözlük açıklamalarında üç ile on erkeği kapsayan küçük gruba, kimi zaman da bir kişinin yanında durup onunla davranabilen yakın destek çevresine uzanır. 4:71'deki gruplar hâlinde çıkış bu çevrenin birlikte hareket etme yönünü, 18:34'teki “daha güçlü bir topluluğa sahip” olma sözü ise toplumsal konumunu öne çıkarır ({ar:أَعَزُّ نَفَرًا, tr:aʿazzu nafaran, gloss:daha güçlü bir topluluğa sahip}) (18:34). Bu destek grubu okuması çıkış eylemiyle akrabadır, fakat ondan ayrıdır: odaktaki kuvvet, eyleme katılabilecek ve destek verebilecek kişiler olarak görünür. Sözlükteki sayı aralığı odaktaki topluluğun kesin büyüklüğünü, çevre kullanımı da üyelerin akrabalığını belirlemez.

4:71'de çıkışın bölük bölük ya da birlikte düzenlenmesi, dönüş adına akraba ayrı bir topluluk imgesini de tetikler. Odaktaki {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:dönüş sırası} dönüş bildiren dişil addır; aynı kelime ailesindeki {ar:الكركرة, tr:al-karkarah, gloss:toplanmış insan topluluğu} bir araya gelmiş insanları adlandırabilir. Ailenin bir başka çoğul biçimi de düzenli atlı birlik kümeleri için kullanılabilir. Bu ayrı grup kullanımı geri gelişin olağan dönüş anlamının yanına yeniden toplanma imgesini getirir; odaktaki dönüş adının biçimi ya da anlamı değildir.

Topluluğun büyüklüğü hem kapasiteyi hem de toplumsal karşılaştırmayı taşır. 18:34'te mal ve insan çevresi üstünlük iddiası olur ({ar:أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا, tr:anā aktharu minka mālan wa-aʿazzu nafaran, gloss:malca senden daha çok, çevrece daha güçlü}); 17:6'daki {ar:أَكْثَرَ, tr:akthara, gloss:daha çok} da {ar:عَلَيْهِمْ, tr:ʿalayhim, gloss:onlara karşı} ile birlikte seferberlik gücünü rakibe göre ölçer. 9:25 ise çokluğun yarar sağlamadığı ve ardından yüz çevirip geri çekilmenin geldiği bir sonucu gösterir ({ar:كَثْرَتُكُمْ فَلَمْ تُغْنِ عَنكُمْ شَيْـًٔا, tr:kathratukum fa-lam tughni ʿankum shayʾan, gloss:çokluğunuz size hiçbir yarar sağlamadı}; {ar:ثُمَّ وَلَّيْتُم مُّدْبِرِينَ, tr:thumma wallaytum mudbirīn, gloss:sonra dönüp kaçtınız}) (9:25). Böylece 18:34 çokluğu toplumsal statüye, 9:25 ise başarısızlığa eşlik eden yetersizliğe bağlar; bu karşılaştırma 17:6'daki artışı pratik kapasite olarak bırakır, başarı güvencesi yapmaz.

Bu karşılaştırmanın sesi de ayetin sonunu biçimlendirir. {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü} son sözcüktür; belirsiz nesne biçimindeki tenvinli bitiş, dönüş ve destekten sonra cümleyi dışa yönelmiş toplu kapasiteyle kapatır. Bu sesli kapanış burada cümleyi toplu kapasiteyle tamamlar; sonraki bir geri çekilmeyi kendi başına öngörmez.

## Soyun Devamı

Kaynaklar ve seferberlik kapasitesi anlatılırken {ar:بَنِينَ, tr:banīna, gloss:oğullar} hem gerçek oğulları hem soy bağını taşır. Aynı kelime ailesinde parçaları birleştirerek düzenli ve ayakta duran bir bütün kurma çağrışımı bulunur. Bu inşa imgesi, son eylemin aynı muhatapları daha büyük bir {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü} durumuna getirmesiyle buluşur: oğullar genişleyen topluluğun kuşaklar arası insanî temeli gibi duyulur. Artış böylece soyut bir sayı olmanın yanı sıra kuşakların birleşmesiyle topluluğun sürmesi olarak da belirir. Bu bağlantıda inşa gerçek binaları ya da sabit bir aile büyüklüğünü anlatmaz; oğulların her birinin fiilen seferber edildiğini de söylemez.

Bu kuşak bağı, surenin önceki tarih çizgisine de açılır. Rehberliğin Beni İsrail'e verilmesi anılır (17:2; {ar:وَجَعَلْنَٰهُ هُدًۭى لِّبَنِىٓ إِسْرَٰٓءِيلَ, tr:wa-jaʿalnāhu hudan li-banī isrāʾīl, gloss:onu İsrailoğulları için rehber kıldık}); ardından Nuh'la birlikte taşınanların soyuna değinilir (17:3; {ar:ذُرِّيَّةَ مَنْ حَمَلْنَا مَعَ نُوحٍ, tr:dhurriyyata man ḥamalnā maʿa Nūḥ, gloss:Nuh'la birlikte taşıdıklarımızın soyu}); iki bozulma ve büyük yükseliş de bu devamı tarihsel sorumluluğa yerleştirir (17:4). Birlikte bu tarih çizgisi, 17:6'daki oğulları yalnızca artan insan gücü olarak değil, rehberlik geçmişi taşıyan topluluğun sonraki kuşağı olarak da duyurur; rehberlik yenilenmeye yön verir, bozulmalar ise sorumluluk boyutunu açık tutar. Nuh bağlantısı dolaylı kalır: 17:6 Nuh'u ya da taşınmayı anmaz; 17:2 rehberlik geçmişini sunar, dönüşün doğrudan açıklamasını değil. Bu yerel tarihsel çağrışım tam bir soy kütüğü kurmaz veya her kuşağa aynı davranışı yüklemez.

Aynı soy devamı bu kez kişisel bir hanenin geleceğinde görünür. Ardından kalacak yakınlardan kaygı duyma, eşinin kısır oluşuyla birlikte dile getirilir; ardından bir ardıl istenir (19:5; {ar:خِفْتُ ٱلْمَوَٰلِىَ مِن وَرَآءِى, tr:khiftu l-mawāliya min warāʾī, gloss:ardımdan kalacak yakınlardan kaygı duydum}; {ar:فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا, tr:fa-hab lī min ladunka waliyyā, gloss:bana katından bir veli ya da ardıl bağışla}). Bu kişisel hane örneği {ar:بَنِينَ, tr:banīna, gloss:oğullar} sözünü soyut insan gücünden çıkarıp kuşaklar boyunca süren hane imgesine yaklaştırır. Bu özel bağlantıda ardıl isteği oğulların sözlük anlamını “varis” diye belirlemez ve onlara kişisel sorumluluk yüklemez.

## Topluluk ve Hesap

Toplu kapasite ile kişisel hesap surenin iki ayrı ölçeğini kurar. Her insanın payının boynuna bağlanması ve ardından kitabının açılması anlatılır (17:13; {ar:وَكُلَّ إِنسَٰنٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:wa-kulla insānin alzam-nāhu ṭāʾirahu fī ʿunuqihi, gloss:her insanın payını boynuna bağladık}). Sonraki ayette {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:kendi nefsinle} kişiyi hesabın ayrılmaz birimi yapar, {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap görücü} hesabın kimin üzerinde durduğunu belirtir (17:14). Başkasının yükünü kimsenin taşımaması da bu sınırı açıkça koyar (17:15; {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz}). Bu nedenle 17:6'daki mal ve insan desteği birlikte hareket etme gücü verse de geniş topluluk tek bir ahlaki kişiye dönüşmez. Bu karşılaştırma devredilemeyen sorumluluğu aydınlatır; 17:15 tarihsel dönüşün nedenini ya da desteğin merhamet mi stratejik yardım mı olduğunu belirlemez.

Kişisel hesabın ardından surenin bakışı, desteğin kimlere ulaştığına döner. Yakın dünya menfaatini isteyenlere orada hızla verileceği söylenir (17:18; {ar:مَن كَانَ يُرِيدُ ٱلْعَاجِلَةَ عَجَّلْنَا لَهُۥ فِيهَا, tr:man kāna yurīdu l-ʿājilata ʿajjalnā lahu fīhā, gloss:yakın dünyayı isteyene orada çabuk veririz}); bu bağlam kaynakların geçici dünya ufkunda işleyebileceğini düşündürür, 17:6'daki topluluğun böyle bir istek taşıdığını değil. Destek eylemi daha sonra iki karşıt alıcıya birden uzanır: “şu gruba da ötekine de destek veririz” denir ve Rabbin bağışının esirgenmediği belirtilir (17:20; {ar:نُّمِدُّ هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ, tr:numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:şu gruba da ötekine de destek veririz}; {ar:مِنْ عَطَآءِ رَبِّكَ, tr:min ʿaṭāʾi rabbika, gloss:Rabbinin bağışından}; {ar:وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışı esirgenmiş değildir}). Böyle bir dağılım, 17:6'daki desteğin somut kapasitesini korurken onu tek başına seçilmişlik kanıtı olmaktan çıkarır.

Dünya içindeki bu kapasitenin yanında 17:21 daha büyük bir ölçü getirir: ahiret derece ve üstünlük bakımından daha büyüktür ({ar:وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًا, tr:wa-la-l-ākhiratu akbaru darajātin wa-akbaru tafḍīlā, gloss:ahiret derece ve üstünlük bakımından daha büyüktür}) (17:21). Bu karşılaştırma 17:6'daki belirli rakibe karşı sayısal üstünlüğü korurken onu nihai dereceyle ayırır. 17:21 tam bir insan sıralaması kurmaz; bu yerel karşılaştırma servetin etik kullanımını ya da desteğin merhamet mi stratejik yardım mı olduğunu belirlemez.

Başka bağlamlar mal ve oğul artışının tek başına iyi sonuca işaret etmediğini gösterir. 23:55'te mal ve oğullarla desteklenmeyi iyiliğin kendileri için acele edilmesi sanıp sanmadıkları sorulur ({ar:أَيَحْسَبُونَ أَنَّمَا نُمِدُّهُم بِهِۦ مِن مَّالٍۢ وَبَنِينَ, tr:a-yaḥsabūna annamā numidduhum bihi min mālin wa-banīna, gloss:mal ve oğullarla desteklenmelerini mi sanıyorlar}); 23:56 onların farkında olmadığını söyler ({ar:بَل لَّا يَشْعُرُونَ, tr:bal lā yashʿurūn, gloss:ama fark etmiyorlar}). 17:64'te mal ve çocuklar aldatıcı vaadin parçasıdır ({ar:وَشَارِكْهُمْ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ, tr:wa-shārik-hum fī l-amwāli wa-l-awlādi, gloss:mallara ve çocuklara ortak ol}); 18:34'te ise mal ve çevreyle övünme toplumsal üstünlük iddiasına dönüşür ({ar:أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا, tr:anā aktharu minka mālan wa-aʿazzu nafaran, gloss:malca senden daha çok, çevrece daha güçlü}). Bu ayrı biçim ve bağlamlar 17:6'daki sözleri dilbilgisel özdeşlik üzerinden açıklamaz; her biri maddi artışın farklı sonuçlara açık olduğunu gösterir. Bu karşılaştırmalar 17:20'nin iki gruba da destek verildiğini açıkça söyleyen ifadesini değiştirmez.

Fâtiha'daki “yalnız senden yardım dileriz” sözü yardım isteyenin bağımlılık duruşunu verir (1:5; {ar:وَإِيَّاكَ نَسْتَعِينُ, tr:wa-iyyāka nastaʿīnu, gloss:yalnız senden yardım dileriz}). Bu duruş, 17:6'daki {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:sizi destekledik} fiilinin dışarıdan alıcıya kaynak eklemesini, topluluk kapasitesinin kendi başına üretilmediği bir yönden duyurur. İki karşıt gruba desteğin uzandığı 17:20 ise kaynağın dağılımını kendi bağlamında ayrıca gösterir. Bu yakınlaştırma yalnızca alınan yardımı yardım isteyenin duruşuyla birlikte düşündürür; Fâtiha'daki istek 17:6'ya kronolojik bir neden ya da cevap kurmaz ve iki yerdeki konuşanları özdeşleştirmez.

## Yağmurdan Akışa

Bol yağmur (71:11; {ar:يُرْسِلِ ٱلسَّمَآءَ عَلَيْكُم مِّدْرَارًۭا, tr:yursili l-samāʾa ʿalaykum midrāran, gloss:üzerinize bolca yağmur yağdırır}) ile bahçeler ve ırmaklar (71:12; {ar:جَنَّٰتٍۢ, tr:jannātin, gloss:bahçeler}; {ar:أَنْهَٰرًۭا, tr:anhāran, gloss:ırmaklar}) su görüntüsünü kurar ve geri verme fiilinin taşıdığı doluluk çağrışımını bağımsız biçimde tetikler. Odaktaki {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik} önceki duruma dönüş anlamını korur; aynı kelime ailesindeki ayrı bir kullanım memede sütün dolmasını, bir başkası da {ar:كَثْرَةُ الْمَاءِ أَوِ الْمَوْجِ, tr:kathratu al-māʾi awi l-mawji, gloss:suyun ya da dalganın bolluğu} gibi suyun ya da dalganın çokluğunu anlatır. Bu ayrı sözlük imgeleri doluluğu belirginleştirir; 71:11'deki yağmur ve 71:12'deki ırmaklar içinde kaybolan inisiyatif yeniden dolan kaynak gibi duyulur. 71:12'de desteğe yakın biçimli bir fiil de önce mal ve oğullarla, ardından bahçe ve ırmaklarla yan yana gelir ({ar:وَيُمْدِدْكُم بِأَمْوَٰلٍۢ وَبَنِينَ, tr:wa-yumdidkum bi-amwālin wa-banīna, gloss:sizi mallar ve oğullarla desteklesin}). Bu sıra maddi ve ailevi desteği suyla beslenen genişleme imgesine yaklaştırır. Biçim yakınlığı odaktaki geçmiş zamanlı destek fiilinin dilbilgisini belirlemez; onun kaynak ekleme anlamını, aynı öğelerin su bereketiyle yan yana gelişinde genişletir.

Irmakların görünmesi, dönüş adına bağlı başka bir biçimi de devreye sokar. Odaktaki {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:dönüş sırası} dönüş bildiren dişil isimdir; aynı kelime ailesindeki ayrı {ar:الكر, tr:al-karr, gloss:doğal su gözü ya da havuz} biçimi doğal suyun toplandığı kaynak, çukur ya da küçük gölü anlatır. Bu biçim özel bir ırmak adı ya da ölçü birimi değildir. Irmakların bulunduğu 71:12 görüntüsü, dönüşün bir havza gibi doluluğu almasını düşündürürken, odaktaki adın kendi anlamı geri geliş olarak kalır.

Odaktaki IV kalıbın destek anlamından ayrı olarak, aynı kelime ailesindeki {ar:مد النهر, tr:madd al-nahr, gloss:nehrin akıp kabarması} kullanımı nehrin akması, dolması ve artmasını anlatır. 71:12'deki ırmaklar bu akış ve beslenme görüntüsünü tetikler. Böylece al-karr'ın havzası geri dönüşün dolan kabını, madd al-nahr ise bu kaba ulaşan akışı verir. Odaktaki mallar ve oğullar desteğin araçları, daha büyük {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü} ise kapasite artışının toplumsal sonucudur. Yağmurun sıvı doluluğu, ayrı su gözü biçiminin havzası ve ırmak kullanımının akışı birlikte yenilenme imgesini kurar. Bu okuma 17:6'daki sözcüklere doğrudan su anlamı yüklemez; benzetme yağmur, bahçe ve ırmakların verildiği 71:11 ile 71:12 bağlamıyla sınırlıdır ve Fâtiha'daki yardım isteğine taşınmaz.

## Hareket ve Alımlama

Dikkat şimdi maddi kapasiteden hatırlatmaya verilen karşılığa döner. Aynı suredeki bir söz, hatırlatmanın insanlarda yalnızca uzaklaşmayı artırdığını söyler (17:41; {ar:وَمَا يَزِيدُهُمْ إِلَّا نُفُورًۭا, tr:wa-mā yazīduhum illā nufūran, gloss:onlara yalnızca kaçınmayı artırır}). Bu ayetteki {ar:نُفُورًا, tr:nufūran, gloss:kaçınma ve uzaklaşma}, ses ve görünüş bakımından odaktaki {ar:نَفِيرًا, tr:nafīran, gloss:seferberlik gücü} ismine yaklaşsa da ayrı bir kelime biçimi ve ailesidir. Odaktaki isim birlikte harekete geçebilecek topluluğu taşırken, 17:41'deki söz hatırlatmadan uzaklaşmayı anlatır. Bu karşıt yön, seferber olabilme ile sözü almaya açıklığı birbirinden ayırır: topluluğun kapasitesi, hatırlatmaya açıklığını kendiliğinden sağlamaz.

</source_prose>
