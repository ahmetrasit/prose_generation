# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:16**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.middle.claims.json`

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
- Refer to source paragraphs as `31:16 ¶N`.

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

`(31:16 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:16",
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
        "citation": "(31:16 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_16/31_16.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_16/31_16.middle.claims.json \
  --ayah-ref 31:16
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_16/31_16.prose.editorial.tr.md`

<source_prose>
## Hitabın Ölçüsü

{ar:يَا بُنَيَّ, tr:yā bunayya, gloss:ey oğulcuğum} diye seslenen Luqman, ağırlığı hardal tanesi kadar olan adı konmamış bir şeyin kayanın içinde, göklerde ya da yerde bulunmasını varsayar; ardından {ar:يَأْتِ بِهَا اللَّهُ, tr:yaʾti bihā Allāhu, gloss:Allah onu getirir} der ve Allah’ı {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīrun, gloss:Latîf ve Habîr} diye niteler. Koşul, saklanma yerlerinin en genişine dek uzanırken sesleniş bütün bu örneği tek bir oğula yöneltilmiş öğüt olarak tutar.

{ar:يَا, tr:yā, gloss:ey} muhatabı çağırır; {ar:بُنَيَّ, tr:bunayya, gloss:oğulcuğum} ise tekil iyelik eki ve küçültmeli şefkat tonuyla konuşanı belirli bir oğulla yakın ilişki içinde gösterir. Bu sıcak hitap geniş kozmik menzili kişisel bir derse dönüştürür; muhatap tek kişidir, öğüdün ciddiyeti korunur ve sesleniş daha geniş bir aile sahnesi kurmaz.

{ar:بُنَيَّ, tr:bunayya, gloss:oğulcuğum} için “ana bütünden ayrılan küçük dal” ya da “yerden çıkan küçük şey” yönünde bir uzantı da bulunur. Yanındaki {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane} bu küçük başlangıç anlamını bağımsızca uyandırır: oğul ile tane küçüklükte buluşur, fakat hitabın muhatabı insan olarak kalır. Böylece tanenin ölçüsü, oğula gösterilen öğretici bir örnek olur; tohumun ekilmesi ya da büyümesi gerçekleşmiş bir olay diye anlatılmaz.

{ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane}nin ekilebilir başlangıç yönü, kişisel öğüdü gündelik yetişmeye de bağlar. 31:5’teki {ar:رَبِّهِمْ, tr:rabbihim, gloss:onların Rabbi} adı aynı kökün yetiştirme ve gözetme yönünü; 31:13’teki öğüt ve 31:17’de tekrarlanan buyruklar ise bu yetişmenin söz ve davranışla sürmesini çağrıştırır (31:5, 31:13, 31:17). Küçük davranışlar böylece karaktere tohum gibi yerleşebilir; bu sure içi eğitim benzetmesi belirli alışkanlıklar listesi vermez.

Başlangıçtaki {ar:إِنَّهَا, tr:inna-hā, gloss:şüphesiz o} adı henüz açıklanmayan dişil bir göndergeyi öne çıkarır; ardından gelen {ar:إِنْ, tr:in, gloss:eğer} ayrı bir koşul açar. Güvence önce duyulur; ardından kurulan koşul ihtimali varsayım olarak tutar, yaşanmış bir olay diye bildirmez. {ar:تَكُ, tr:taku, gloss:olsun} ile başlayan tek koşul aynı göndergeyi önce ölçüye, {ar:فَتَكُنْ فِي, tr:fa-takun fī, gloss:öyleyse içinde bulunsun} ile de bir konuma yerleştirir; baştaki {ar:فَـ, tr:fa, gloss:öyleyse} bu yer cümlesini koşulun içine bağlayıp cevaptan önceki varsayımın parçası yapar.

Kısa {ar:تَكُ, tr:taku, gloss:olsun} biçimi, ölçüden hemen önce sıkı bir ses başlangıcı verir; daha tam {ar:تَكُنْ, tr:takun, gloss:bulunsun} biçimindeki {ar:ن, tr:nūn, gloss:nūn harfi} korununca ses uzar ve yerler sıralandıkça ritim genişler. Aynı fiilin bu iki biçimi ölçümden konuma ilerler; biçim ve tempo bu hareketi duyurur, koşulun anlamına yeni bir olay eklemez.

İlk “olma” cümlesinin haberi olan {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü}, adı açıkça konmamış varlığı tartılabilir miktara çevirir. Sözcüğün {ar:م, tr:mīm, gloss:mîm harfi}yle kurulan ölçü kalıbı gevşek bir “ağır” sıfatından çok ölçü standardı duyurur; ayet yine de belirli bir tartı birimi ya da kullanılan terazi vermez. Ağırlık öncelikle maddi ölçüdür: küçücük tanenin de değer taşıyabileceğini bildirir, taneye kendi başına güç yüklemez.

{ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane} belirsiz tekil biçimiyle sayılabilir bir örnek verir; dünyada yalnızca bir tane bulunduğunu değil, bu koşulda tek bir tanenin ölçü alındığını söyler. Ardındaki {ar:مِنْ, tr:min, gloss:türünden} kaynak ya da hareket değil, tanenin hangi bitkiden olduğunu belirtir. {ar:خَرْدَلٍ, tr:khardalin, gloss:hardal} soyut küçüklüğe somut bir beden verir: burada bitki ve tohum yönü iş başındadır, et kesmeyle ilgili ayrı kullanım taneye taşınmaz. Dört ünsüzlü bu belirgin bitki adı ölçüyü akılda kalır kılar.

{ar:حَبَّةٍ مِنْ, tr:ḥabbatin min, gloss:bir hardal tanesi} sözlerinde tanenin tenvini sonraki mîme genizli bir birleşmeyle bağlanır; ölçü tek ses akışında duyulur. Hardal adının belirgin, pürüzlü ünsüzleri de taneye dokunsal bir ses profili verir. Ses örgüsü küçük nesneyi maddileştirir; sözcüklerin olağan anlamları yerinde kalır.

{ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane}nin bitkisel anlamı sürerken, aynı kök ailesinin sevgi ve olumlu bağlılık yönü yakındaki şefkatli {ar:بُنَيَّ, tr:bunayya, gloss:oğulcuğum} sayesinde duyulabilir. 31:18’deki {ar:يُحِبُّ, tr:yuḥibbu, gloss:sever} fiili bu ailedeki sevgi anlamını başka biçimde taşır (31:18). Bu kök yankısı ahlaki öğüde sıcaklık ve değer boyutu katar; 31:18’deki kibirli kişi odak ayetin konusu olmaz, tane de sevgi sözcüğüne dönüşmez.

Tanenin {ar:فِي الْأَرْضِ, tr:fī al-arḍi, gloss:yerin içinde} bulunması ve ardından {ar:يَأْتِ, tr:yaʾti, gloss:gelir veya ulaşır} fiilinin gelmesi, ekilebilir tohumun saklı gelişme ihtimalini açar. Bu küçük birim bir başlangıç gibi duyulabilir; fiilin olağan gelme ve ulaşma anlamı korunurken aynı kökün ürün verme yönü de sonradan bu imgeye katılabilir. Koşul ekim ya da büyümeyi gerçekleşmiş bir olay olarak anlatmaz.

Yakındaki 31:13’te şirk büyük haksızlık diye nitelenir, 31:14’te dönüşün Allah’a olduğu söylenir; bu sözler {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü} ailesinin günah ve suçları kişinin taşıdığı ağır sorumluluk olarak kavrayan ayrı kullanımını uyandırır (31:13, 31:14). Maddi tartı anlamı korunurken bu sorumluluk yankısı küçük bir miktarın da ahlaki ağırlık taşıyabileceğini duyurur. Odak hangi günahı ya da ameli adlandırmaz; 31:14’teki dönüş sözü de hesap veya ceza biçimini tek başına belirlemez.

## Taşın İçinden Göklere

İlk yer olan {ar:فِي صَخْرَةٍ, tr:fī ṣakhratin, gloss:bir kayanın içinde}, taneyi yalnızca bir mekâna koymaz; iri ve sert taşın çevrelediği iç hacme yerleştirir. {ar:صَخْرَةٍ, tr:ṣakhratin, gloss:kaya} belirsiz biçimiyle herhangi bir kaya benzeri sert içi düşündürür; böylece taş somut bir engel ve saklanma yeri olur. Sert malzeme ile ünsüz dokusu bu kapalı iç mekânın direncini belirginleştirir; burada duyulan maddi direnç, egemenlik imgesi ya da belirli bir jeolojik olay değildir.

Ardından iki {ar:أَوْ, tr:aw, gloss:ya da} ayrı olasılık ekler: {ar:فِي ٱلسَّمَٰوَٰتِ, tr:fī al-samāwāti, gloss:göklerin içinde} ve {ar:فِي الْأَرْضِ, tr:fī al-arḍi, gloss:yerin içinde}. Üç kez yinelenen {ar:فِي, tr:fī, gloss:içinde} aynı iç-konum ilişkisini kaya, gökler ve yere uygular; farklı mekânlar tek koşul altında toplanır, fakat birbirine eşitlenmez. Sıra sert ve somut kayanın içinden tanınan üst alan olan belirli çoğul göklere, oradan belirli tekil alt alan olan yere iner; yerin içi yüzeyden fazlasını düşündürse de yeraltında belirli bir nesne gösterilmez.

Yinelenen {ar:أَوْ, tr:aw, gloss:ya da} saklanma aralığını çok genişletir; üç kısa {ar:فِي, tr:fī, gloss:içinde} vuruşu listeye ölçülü bir ritim verir. {ar:صَخْرَةٍ, tr:ṣakhratin, gloss:kaya} ilk örnek olarak kalırken {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} yüksekliği, {ar:الْأَرْضِ, tr:al-arḍi, gloss:yer} onun alt karşılığını ekler. Yükseklik erişim menzilini genişletir ama mutlak erişilmezlik iddiasına dönüşmez; üç yer geniş bir aralık kurar, bütün mekânları saymaz. Aynı gönderge koşul boyunca dilsel olarak sabit kalır; bu süreklilik fiziksel değişmezlik yasası değildir.

Uzun ölçü ve yer dizisinin ardından gelen kısa {ar:يَأْتِ بِهَا اللَّهُ, tr:yaʾti bihā Allāhu, gloss:Allah onu getirir} koşula cevap verir. {ar:يَأْتِ, tr:yaʾti, gloss:gelir veya ulaşır} geliş fiilini, içindeki bāʾ ve {ar:بِهَا, tr:bihā, gloss:onu} zamiriyle aynı dişil göndergeyi getirme eylemine bağlar: cevap, saklı şeyin bilindiğini bildirmenin ötesinde onu erişime getirir. Uzun saklanma dizisiyle kısa cevap arasındaki ritim farkı sonucu keskinleştirir; fiil getirmeyi söyler, fiziksel bir tekniği değil.

Cevapta fiil ve nesne {ar:اللَّهُ, tr:Allāhu, gloss:Allah} açık özne olarak söylenmeden önce gelir. Böylece dikkat önce neyin getirildiğine, sonra faili kimin oluşturduğuna yönelir. Bu cümlede eyleyen Allah’tır; yerel sözdizimi başka anlatılardaki ikincil nedenler hakkında hüküm kurmaz.

Ayetin başındaki {ar:إِنَّهَا, tr:inna-hā, gloss:şüphesiz o} ile kapanıştaki {ar:إِنَّ, tr:inna, gloss:şüphesiz} farklı iş görür: ilki adı konmamış dişil göndergeyi öne alırken sonuncusu {ar:إِنَّ اللَّهَ, tr:inna Allāha, gloss:şüphesiz Allah} biçiminde Allah’ı iki niteliğin taşıyıcısı yapar. Getirme cümlesindeki {ar:اللَّهُ, tr:Allāhu, gloss:Allah} merfûʿ özne, kapanıştaki {ar:اللَّهَ, tr:Allāha, gloss:Allah’ı} ise inna’dan sonraki mansûb addır; gönderge aynı kalır, sözdizimindeki rol değişir. Koşulda öne çıkan şey böylece adı açıkça anılan Allah’a ve onun niteliklerine bağlanarak kapanır.

{ar:لَطِيفٌ, tr:laṭīfun, gloss:Latîf} küçük, ince, hafif ve kaba olmayan yönleriyle hardal tanesinin ölçeğine, ayrıca kayanın ya da geniş alanların içindeki gizlenmeye uyar. Duyuların seçemeyeceği kadar ince olana uzanma çağrışımı, küçük ve saklı şeyin erişim dışında kalmadığını duyurur. Sıfatın yumuşaklık ve özen yönü de {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} eylemini incitmeden ve dikkatle yürütülen bir iş gibi duyurabilir; getirme fiilinin olağan anlamı korunur, ayrı bir çıkarma tekniği kurulmaz.

{ar:خَبِيرٌ, tr:khabīrun, gloss:iç yüzünden haberdar} bilgi alanını haber verilebilir şeyden bir işin görünüş ardındaki iç gerçeğini bilmeye kadar açar. Kelime ailesinin edinilmiş ve aktarılmış bilgiye, ayrıca deneyimle bir işin iç yüzünü tanımaya ilişkin kullanımları bulunsa da buradaki sıfat Allah’ın bilen niteliğini adlandırır. Önceki saklanma yerleri, dışarıdan görünmeyenin iç yüzüyle birlikte bilinmesine somut zemin verir; son sıfattaki `faʿīl` kalıbı da bu niteliği süreklilik taşıyan bir kapasite gibi duyurur. {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīrun, gloss:Latîf ve Habîr} aynı kapanışta ince erişim ile iç bilgiyi bir arada tutar: kapanış, getiren özneyi nitelikleriyle tanıtır ve bu iki niteliği birbirinden üstün kılmaz. {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü}yle ölçülmüş aynı {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane}, {ar:صَخْرَةٍ, tr:ṣakhratin, gloss:kaya} ya da geniş bir alanın içinde saklı kalırken {ar:بِهَا, tr:bihā, gloss:onu} ile getirme cevabının nesnesi olur; {ar:لَطِيفٌ, tr:laṭīfun, gloss:Latîf} ince ölçeğe uygun erişimi, {ar:خَبِيرٌ, tr:khabīrun, gloss:Habîr} gizli iç yüzün bilgisini ekler. Böylece okur aynı şeyin örtü ve uzaklık boyunca geri getirildiğini düşünür; ayet bu erişimi sağlayan fiziksel yöntemi tarif etmez.

## Tartı, Dönüş ve Açık Zamir

Buradaki tartılabilir küçük miktar, aynı hardal tanesinin adalet terazilerine getirildiği ve kimseye haksızlık edilmeyeceğinin söylendiği 21:47 ile somut bir karşılık kazanır (21:47). Bu terazide aynı tanenin sunulması, odaktaki {ar:بِهَا, tr:bihā, gloss:onu} yapısının getirme yönünü ve {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü}nın birimi belirleme işini ayrı ayrı görünür kılar; gizli şey tam ölçüsüyle karşılığa dönüşür (21:47). Göklerde ve yerde en küçük ağırlığın bile hesaptan düşmediği 10:61 ve 34:3, ayrıca 34:22’de aynı üst-alt alanlarda en küçük ölçünün kaybolmaması, odaktaki gök-yer çiftini erişimin sınırlarına dönüştürür (10:61, 34:3, 34:22). Karanlıklar içindeki tek tanenin de bilindiği 6:59, gizliliği görünmezlikle eş tutmaz ve {ar:لَطِيفٌ, tr:laṭīfun, gloss:ince erişen} niteliğin duyuların seçemediği ölçeğini belirginleştirir (6:59). Hardal bitki ve tohum örneği olarak kalır; 21:47’deki hedef biçimler burada belirlenmediğinden bu yankı zamiri belirli bir amele sabitlemez.

Bu ölçü ve getirme, sorumluluk imgesine de yaklaşır: 31:15’te yapılan işlerin haber verilmesi, 31:33’te ebeveynin çocuğu yerine karşılık verememesi ve 31:24’te kısa yararla ağır cezanın karşıtlığı, kasıtlı işin bildirilmesi, karşılık ve sorumluluk arasındaki bağı açar (31:15, 31:33, 31:24). {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü} ile {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} fiziksel tartı ve getirme anlamlarını korurken bir amelin kimliği ve karşılığıyla hesap sahnesine dönebilmesini düşündürür (31:15, 31:24, 31:33); bağlamdaki sözcüklerle kök ya da biçim ilişkisi doğrulanmış dilbilgisel çözümleme diye sunulmaz.

{ar:بِهَا, tr:bihā, gloss:onu} zamiri getirilen şeyi açıkça işaretler ama adını vermez. 31:15’te geri dönen işler, 21:47’de teraziye getirilen hardal tanesi, 31:23’te göğüslerde olan ve 31:28’de yeniden kaldırılan tek nefis farklı bağlamlar sunar (31:15, 21:47, 31:23, 31:28). Bu temaslar amel, iç yöneliş ya da bedensel bir varlık ihtimallerini birlikte açık tutar; sıradan tane ya da parça imgesi korunur ve bunlardan hiçbiri tek karşılık seçilmez (31:15, 21:47, 31:23, 31:28).

Taş, odak ayette güç erişilen gerçek saklanma yeri olmayı sürdürür. 31:6’daki yoldan saptırma ve kaybolma sahneleri iki ayrı yitme/sapma yolunu, 31:13’teki büyük haksızlık ise bir şeyi yanlış yere koyma imgesini getirir (31:6, 31:13). Bu farklı yollar, {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} eylemini ahlaken yanlış yerde kalanın geri çağrılması gibi de düşündürür; yanlış yerde kalmanın silinme olmadığı böylece belirginleşir. Bu yankı taşın fiziksel içini korur ve zamiri belirli bir kayıp şeyle özdeşleştirmez.

## Örtü, Gelişme ve Dönüş

{ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane veya tohum} ile {ar:فِي الْأَرْضِ, tr:fī al-arḍi, gloss:yerin içinde} sözleri, taneyi toprağın altında saklı bir başlangıç olarak da düşündürür. 31:23’teki örtme ve inkâr yönü bu tohum imgesiyle karşılaşınca saklılık, büyüme öncesindeki bir örtü gibi duyulabilir (31:23). {ar:يَأْتِ, tr:yaʾti, gloss:gelir veya ulaşır} ailesinin ürünün görünmesine açılan ayrı yönü imgeyi genişletir; böylece örtülmüş olanın yeniden görünmesi düşünülebilir, bu olasılık bütün inkârlar için hüküm vermez (31:23).

Ekolojik imge, odak fiilin olağan “gelmek/ulaşmak” anlamından ayrı kök kullanımlarını adım adım gösterir. {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane}, {ar:يَأْتِ, tr:yaʾti, gloss:gelir veya ulaşır} ve {ar:الْأَرْضِ, tr:al-arḍi, gloss:yer} 31:10’da yağmurun gökten inip yere ulaşması ve bitkinin çıkmasıyla, 31:34’te de yağmurun yeniden anılmasıyla buluşur (31:10, 31:34). Aynı kökün başka kullanımları suyu kanala alıp akışı yönlendirir ve ekinin ya da hurmanın gelişip ürün vermesini anlatır (31:10, 31:34). {ar:خَبِيرٌ, tr:khabīrun, gloss:Habîr} ailesindeki gevşek, su tutan arazi kullanımı da bu yolu tamamlar: su iner, yönlendirilir, toprağa işler ve bitki görünür olur (31:10, 31:34). Aynı ailedeki arazi kullanımı, burada Allah’a verilen sıfatın bilgi anlamından ayrıdır; {ar:الْأَرْضِ, tr:al-arḍi, gloss:yer} odakta olağan yer alanını korurken verimli toprağı düşündürebilir. Bu çağrışım belirli bir ekili tarla kurmaz, odaktaki fiili de “sulama” diye çevirmeyi gerektirmez.

Tohumdan görünür ürüne açılan yol, 31:27’de ağaç, kalem ve Allah’ın sözlerinin art arda gelişiyle başka bir üretim imgesine dönüşür (31:27). {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tohum} başlangıcı, {ar:يَأْتِ, tr:yaʾti, gloss:getirir veya ortaya çıkar} sonuç taşıyıcısını verir: tohum olgun ağacı, ağacın kesilmiş malzemesi kalemi, yazı da anlamlı söz ve tanıklığı düşündürür (31:27). Gizli potansiyel ifade edilebilir hâle gelir; bu dizi bir üretim imgesidir, odaktaki zamir için metin ya da söz karşılığı seçmez (31:27).

Tohumun gelişmesiyle geri getirmenin bedensel yankısı iki ayrı zamanı açık tutar. 31:14’te annenin gebelikte taşıması ve doğuma uzanan ayrılma, 31:34’te rahimlerde olanın bilinmesi {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane veya tohum} için oluşan hayatın başlangıcını düşündürür; {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü} ailesinin gebelik yüküyle ağırlaşmaya ilişkin ayrı kullanımı da bu gelişen potansiyeli ekler (31:14, 31:34). {ar:يَأْتِ, tr:yaʾti, gloss:ortaya getirir} ailesinin ürün verme yönü gelecekte biçim kazanmayı duyurur (31:14, 31:34). Gebelik bu okumada odak sözcüklerin anlamı değil, ağırlık ölçüsüne eşlik eden gelişme benzetmesidir.

Gelişen hayat imgesinden ayrı olarak, {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü}, {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} ve {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} 31:10’daki yaratma ve dağıtma, 31:28’deki yeniden diriltme ve tek canlı nefis, 31:34’te ise nerede ölüneceğinin bilinmemesiyle buluşur (31:10, 31:28, 31:34). Dağılmış bir kimliğin korunarak yeniden sunulması bu karşılaşmada mümkün bir okuma olur (31:10, 31:28, 31:34). Yaratılma ve saçılma, tek nefis, yeniden kaldırılma ve bilinmeyen ölüm yeri ayrı ayrıntılardır; doğumla dirilme tek mekanizmaya çevrilmez, zamirin beden ya da nefis olduğu da kesinleşmez (31:10, 31:28, 31:34).

31:29’da geceyle gündüzün birbirine girişi, süreğen akış, belirlenmiş vade ve adlandırılmış bitiş başka bir zaman ölçeği açar (31:29). Odaktaki {ar:تَكُ, tr:taku, gloss:bulunması}, {ar:تَكُنْ, tr:takun, gloss:olması}, {ar:يَأْتِ, tr:yaʾti, gloss:ulaşır} ve {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} saklı nesnenin bulunma ve varış çerçevesini kurar; aynı kökün tanıtıcı iz ya da işaret için kullanılan ayrı yönü de zaman içinde izlenebilirlik düşüncesini ekler (31:29). Bu karşılaşma gökleri işaret diye çevirmeden, odak ayete de belirli bir vade yüklemeden süreç benzetmesi kurar; söz konusu olan kozmik yolculuk değildir (31:29).

Ortak {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} taşıyıcısının bağlamlar arasında değişen katkıları da ayrı kalır. 31:15’te işlerin geri dönüşü, 21:47’de terazide sunulan tane, 31:28’de tek nefsin yeniden kaldırılması ve 31:29’daki zamanlı akış gelme/ulaşma yönünü açar; yağmurdan bitkiye ilerleyen 31:10 ve 31:34 ise aynı kökün ürün verme yönünü çağırır (31:15, 21:47, 31:28, 31:29, 31:10, 31:34). Böylece eylem, tane, nefis ve zamanlı çevrim bir katkı kümesi; yağmurdan çıkan bitki başka bir katkı olur, ama bu farklı süreçler zamirin tek karşılığını seçmez ve kapsamlı bir sure tezi kurmaz (31:15, 21:47, 31:28, 31:29, 31:10, 31:34).

## Görünür Alan ve İçte Kalan

Odaktaki {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane} ile {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} ve {ar:الْأَرْضِ, tr:al-arḍi, gloss:yer} saklanma alanı olurken aynı kapsam içindeki görünür ve içte kalanı düşünmeye de yer açar. 31:20’de göklerde ve yerdeki görünen ve gizli nimetlerden, ayrıca Allah hakkında bilgisizce tartışanlardan söz edilir; böylece 31:16’daki saklanma yalnız “nerede?” sorusunu değil, görünen dünyanın iç katmanlarını da düşündürür (31:20). {ar:خَبِيرٌ, tr:khabīrun, gloss:iç yüzünden haberdar} sıfatı bu bağlamda bilen niteliğiyle bilgisizce iddia eden bazı kişilerle karşıtlık kurar; bu karşıtlık her tartışmaya yayılmaz (31:20). 31:21’deki ayrı bulma iddiası bu okumaya taşınmaz (31:21).

{ar:حَبَّةٍ, tr:ḥabbatin, gloss:tane} 31:23’te göğüslerde olanın bilinmesiyle karşılaşınca gizlilik dışarıdaki kaya ya da uzaklıkla sınırlı kalmaz; görünür davranıştan önce içte taşınan küçük bir yöneliş de akla gelir (31:23). 31:18’deki {ar:يُحِبُّ, tr:yuḥibbu, gloss:sever veya yeğler} aynı kök ailesinin sevgi ve tercih yönünü, 31:23’teki göğüslerin eylem kaynağı oluşuyla buluşturur (31:18, 31:23). Böylece bitkisel tane henüz davranışa dönüşmemiş bağlılık ya da tercih için bir imge olabilir (31:18, 31:23); “kalbin içindeki kara öz” anlamı yalnız belirli bir kalp tamlamasında bulunduğundan burada tane kalp ya da kesin bir niyet diye çevrilmez.

{ar:خَبِيرٌ, tr:khabīrun, gloss:Habîr}in iç gerçeği bilme niteliği, 31:23’te göğüslerde olanla ve 31:34’te rahimlerde olan, yarının kazancı ve kişinin nerede öleceğiyle karşılaşınca bilgiyi salt konum bilgisinin ötesine taşır (31:23, 31:34). Oluşan ya da geleceğe uzanan gizli süreçler de bilinen alana girer (31:23, 31:34). Bu süreçlerin hiçbiri odaktaki taneyle aynı şey sayılmaz; 31:34’teki kelimelerle kesin biçim ilişkisi kurulmaz (31:34).

Sure başındaki {ar:بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ, tr:bismi llāhi r-raḥmāni r-raḥīmi, gloss:Rahman ve Rahim olan Allah’ın adıyla} besmelesi (S:0), Allah’ı Rahman ve Rahim diye anarak {ar:لَطِيفٌ, tr:laṭīfun, gloss:Latîf} sıfatının yumuşak, özenli erişim yönüne bakım tonu ekler. 42:19’da Latîf’in kullara rızık ve koruyucu özenle yan yana gelişi, yararı ulaştırma ve zarardan koruma çağrışımını belirginleştirir (42:19). 6:103’te insan görüşünün sınırını aşma, 67:14’te yaratanın yaratılmışı bilmesi ve 22:63’te yağmurun yeri yeşertmesi ince erişimin algı sınırını aşan ve yararı ulaştıran yönlerini ayrı ayrı genişletir (6:103, 67:14, 22:63). Bu bağlantılar Latîf’i rahmetle eşitlemez; belirli bir rızık, yağmur ya da yaratılış olayını 31:16’nın tek konusu da yapmaz (S:0, 42:19, 6:103, 67:14, 22:63).

31:17’deki doğru davranış çağrısı ile 31:33’teki korunma uyarısı, başka köklerdeki eşit ölçü ve koruma altındaki ağırlık kullanımlarını devreye sokar (31:17, 31:33). Bunlar {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü} sözcüğünün yeni sözlük anlamı değil, ölçü, denge ve korunma arasındaki analojik yakınlıktır (31:17, 31:33). Bu yakınlık sakınmayı küçük karşılıkları sıfıra yuvarlamayan bir dikkat ayarı gibi düşündürür (31:17, 31:33).

31:7’de ayetleri dinlemeyenin kulağındaki ağırlık imgesi, {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlık ölçüsü}nın ve küçük tanenin fark edilmeme ihtimalini alıcının dirençli, ağırlaşmış işitmesiyle de ilişkilendirir (31:7). {ar:لَطِيفٌ, tr:laṭīfun, gloss:ince erişen} ile birlikte düşünüldüğünde ince ama gerçek olanın duyulamaması belirginleşir; 31:16 işitmeden söz etmediği için bu çağrışım tartı anlamını değiştirmez (31:7).

Son olarak, getirme cümlesi failini açıkça {ar:اللَّهُ, tr:Allāhu, gloss:Allah} diye adlandırır; {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} ile {ar:الْأَرْضِ, tr:al-arḍi, gloss:yer} de bu eylemin geçtiği alanlardır. 31:10’da görünür bir dayanak olmadan yaratılmış kozmos, 31:11’de başkalarına yöneltilen “ne yarattılar?” meydan okuması yaratıcı ve olası rakipler alanını; 31:20’deki buyruğa verilmişlik ise yönetim ve egemenlik yönünü açar (31:10, 31:11, 31:20). Böylece gök-yer çifti yalnız saklanma yeri değil, yaratma, destek, rakiplik ve yönetimin sahası olarak da belirir. Tapınma ve tapınılan varlık alanındaki yankı Allah adını “tapınılan varlık” diye çevirmeden failin rakipsizliğini duyurur (31:11, 31:20); bu bağlam 31:16’yı rakiplerle bir tartışmaya dönüştürmez ve getirme cümlesinde Allah’ı tek fail olarak adlandıran sözdizimini korur.

</source_prose>
