# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:10**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.middle.claims.json`

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
- Refer to source paragraphs as `31:10 ¶N`.

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

`(31:10 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:10",
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
        "citation": "(31:10 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_10/31_10.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_10/31_10.middle.claims.json \
  --ayah-ref 31:10
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_10/31_10.prose.editorial.tr.md`

<source_prose>
## Göklerin kuruluşu

Ayet göklerin yaratılışından yeryüzündeki yaşama iner: dağlar, yer sizinle sarsılmasın diye ona konur; canlılar yeryüzüne yayılır; gökten gelen su, topraktan değerli ve çoğalan bitkiler çıkarır. Önce yukarıdaki düzen görünür, sonra bu düzenin içinde hareket eden hayat.

Yaratma fiili {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} gökleri tamamlanmış bir ilahî eylemin nesnesi yapar. Kökün ölçüyü ve sınırları belirleyerek var etme çağrışımı, yaratılmış gökler ve onların {ar:بِغَيْرِ عَمَدٍ, tr:bi-ghayri ʿamadin, gloss:direkler olmaksızın} kuruluşuyla buluşunca, sahne bir imalat tarifinden çok ölçülü bir düzen olarak belirir. Belirli çoğul {ar:السَّمَاوَاتِ, tr:as-samāwāti, gloss:gökler} tanıdık üst âlemi yükseltilmiş, katmanlı bir mimari gibi duyurur; biraz sonra suyun kaynağı olacak tekil {ar:السَّمَاءِ, tr:as-samāʾi, gloss:gökyüzü} bu çoğul göklerle aynılaştırılmaz. Göklerle yeryüzü birlikte tek bir doğa görüntüsünden daha geniş, yaratılmış bir alan açar. Hikmetli kitapla birlikte anılan kesinlik ve sağlam kuruluş vurgusu da bu ölçülü yaratılış okumasını destekler (31:2); hemen sonraki meydan okuma sahneyi “Allah’ın yaratışı” diye adlandırıp başkalarının ne yarattığının gösterilmesini ister (31:11), başka bir ayet de gökleri ve yeri kimin yarattığını sorar (31:25). Böylece yaratılışın olağan anlamı korunurken görünür düzen, yaratıcı kudret üzerine karşılaştırılabilir bir sorunun parçası olur; bağlamın odağı belirli bir rakibin eylemleri değil, yaratıcı kudret sorusudur.

Direklerin anlatımında {ar:بِ, tr:bi, gloss:ile / -sız} kuruluş tarzını, {ar:غَيْرِ, tr:ghayri, gloss:başka / olmaksızın} ise sıradan destek kategorisinin dışında kalışı belirtir. {ar:عَمَدٍ, tr:ʿamadin, gloss:direkler} adı kulağa da ağır gelen taşıyıcıları düşündürür; ardından gelen {ar:تَرَوْنَهَا, tr:tarawnahā, gloss:onu görürsünüz} desteğin varlığıyla görülürlüğünü birbirinden ayıran bir soru açar. Buradaki kuruluş sonradan gerçekleşen bir değişimi değil, direksiz olma niteliğini bildirir. Sondaki {ar:هَا, tr:hā, gloss:onu} zamiri hem göklere hem direklere dönebilir: göklerin gerçekten direksiz olmasıyla gözün eriştiği yerde direk görülmemesi iki dilbilgisel okuma olarak birlikte kalır. Görme fiili muhatabı şimdi bakmaya çağırır; gözle algıyı da içsel kavrayışı da taşıyabildiği için sahnede hem neyin bulunduğu hem de neye erişilebildiği önem kazanır.

Bu çağrı gerçek bir görüş alanı açar; bakışın sınırı da aynı anda hissedilir. Görünür ve bâtın nimetleri aynı gök-yer alanında birlikte anan, onları bolca tamamlayan ayet (31:20), dağların göz önündeki sabitlemesine görünmeyen bir etkinlik ihtimali ekler. Bu bağlantı saklı fiziksel sütunları kanıtlamaz; zamirin iki dilbilgisel gönderimi, göklerin gerçekten sütunsuz olduğu okumasını ve göz önünde direk seçilmediği okumasını birlikte açık tutar. Yerin yutulup sarsılması tehdidi (67:16), bu sabitliğin taşıdığı sonucu belirginleştirir.

Görme sözü yaratılmış sahneye bir okuma boyutu da katabilir. İşaret ve düzen vurgusu taşıyan ayetle (31:2), okunan söz karşısında işitmeye yüz çeviren kişinin anlatımı (31:7) yan yana gelince, burada görülen gök, yer, canlı, su ve bitki dizisi okunmuş işaretlerin göz önündeki karşılığı gibi düşünülebilir. {ar:تُتْلَىٰ, tr:tutlā, gloss:okunup aktarılır} okunan ayetleri, {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:onları işitir} ise sesi işitmenin yanında anlamaya ve uymaya açıklığı da taşır; görülen düzen böylece yalnızca bakılan bir sahne olmaktan çıkıp kavranması beklenen bir sunuma dönüşebilir. Bu yankı fiziksel yaratılış okumasını olduğu gibi korur; bağlantının kapsamı sahnenin okunmuş işaretler gibi kavranmasıdır, metnin kendisiyle özdeşleştirilmesi değildir. Muhatapların bu çağrıya verdiği karşılık da 31:10’da açılmaz.

## Yerin dayanağı ve hareket

Gökleri görme çağrısı tamamlanınca {ar:وَأَلْقَىٰ, tr:wa-alqā, gloss:ve yerleştirdi} yeryüzündeki yeni eylemi başlatır. Bağlaç, dağların konmasını göklerin yaratılışının yanına eklenen ayrı bir eylem olarak bağlar; iki iş arasında doğrudan nedensellik kurmaz. Tekil ve belirli {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü}, çoğul göklerin karşısında aşağıdaki alıcı zemindir; {ar:فِي, tr:fī, gloss:içine / içinde} dağlar adlandırılmadan önce yerleştirme yönünü kurar. {ar:أَلْقَىٰ, tr:alqā, gloss:yerleştirdi / attı} fiilinin örtük faili yaratma fiilinden taşınır; {ar:رَوَاسِيَ, tr:rawāsiya, gloss:sabit dağlar} yeryüzüne konan nesnelerdir. Atma ve bırakma kullanımları dağları etkin biçimde yerleştirilmiş unsurlar olarak duyurur.

Dağları adlandıran {ar:رَوَاسِيَ, tr:rawāsiya, gloss:sabit dağlar}, yerinde sağlam duruşu taşır; aynı sözcük ailesinin geminin suda durma noktasına varıp hareketini bitirmesini anlatan kullanımı yeryüzünün salınmasını önleme amacıyla buluşunca, dağlar çıpa gibi görünür. Kökün kök salmış duruş ve ayağın yere sağlam basması çağrışımı bu çıpa imgesine bedensel bir sağlamlık da katar; gemi örneği ayrı bir sahne açmadan dağın çıpa gibi duruşunu dilsel olarak destekler. {ar:أَن, tr:an, gloss:-mesi için} ile kurulan amaç yapısında gizli özne yeryüzüdür: {ar:تَمِيدَ, tr:tamīda, gloss:sallansın}, dağların önlediği yana salınma ihtimalini adlandırır; anlatılan hareket, yeryüzünün üzerindekilerle birlikte dengesini yitirebileceği özel bir sarsıntıdır. {ar:بِ, tr:bi, gloss:ile} ve {ar:كُمْ, tr:kum, gloss:siz} muhatapları sarsıntının nedeni olarak değil, yerle birlikte tehlikeyi paylaşanlar olarak konumlandırır. Fiilin tilavette uzayan sesi de yana salınma görüntüsünü kapanışa varmadan bir an gerer.

Dağların dengeleyici duruşu hareketi durdurmak yerine ona sınır ve yön kazandırır. Ölçülü adım (31:19) insan yürüyüşündeki ritmi, güneşle ayın belirlenmiş vadeye akışı (31:29) kozmik devinimdeki ölçüyü, denizde yol alan gemi (31:31) hareket içinde izlenen yolu, yerin sarsılması tehdidi (67:16) ise bu düzenin kırılgan sonucunu görünür kılar. Birlikte düşünüldüklerinde sabitleme, hareketli dünyanın içinde işleyen bir koşul gibi belirir. Fiziksel dengeyle yürüyüşteki etik ölçü arasında bir kontrol ilkesi sezilebilir; bu temas iki alanı tek bir fizik yasasına indirgemeden, ayrı düzeylerde kurulur.

Bu sarsıntı ihtimalinin ardından gelen {ar:وَ, tr:wa, gloss:ve}, jeolojik sahneden canlıların dağıtılmasına geçirir. Bağlaç önceki bir vaadin yerine gelişini değil, canlıların yayılışını yeni bir eylem olarak ekler. {ar:بَثَّ, tr:baththa, gloss:dağıttı / yaydı} canlıları yeryüzüne etkin biçimde dağıtır; sözcüğün sıkışık, çift ünsüzlü sesi de sabit zemin görüntüsünden hareketli yaşam alanına geçişe eşlik eder. {ar:فِيهَا, tr:fīhā, gloss:onda / onun içinde} dağılımın mekânını, {ar:مِن كُلِّ دَابَّةٍ, tr:min kulli dābbatin, gloss:her hareketli canlıdan} ise canlı sınıflarının aralığını verir: {ar:مِنْ, tr:min, gloss:-den / arasından} ile {ar:كُلِّ, tr:kulli, gloss:her} her sınıftan örnekleri kapsar. Yer ve sınıf, aynı dağıtma eyleminin iki ayrı tamamlayıcısıdır. {ar:دَابَّةٍ, tr:dābbatin, gloss:hareketli canlı} yerde kendi gücüyle ilerleyen hayatı adlandırır; çift ünsüzlü ad, dağıtma fiilinden sonra canlı adımına dokunsal bir ağırlık verir. Sözcüğün yerde hafif ya da yavaş sürünerek ilerlemeyi anlatan kullanımı da bu sahneye ayrı bir hareket niteliği katar; bu, bütün canlıları yavaş ya da sürüngen sayan bir sınıflama değildir. Niceleyici tüm canlı sınıflarını kapsar; türler tek tek sayılmaz ve dağılımın miktarı verilmez.

Tekrar eden {ar:فِيهَا, tr:fīhā, gloss:onda / onun içinde}, canlıların yayılışını daha sonra bitkilerin yetişmesiyle aynı yeryüzüne bağlar. Dağların sabit zemini ile {ar:بَثَّ, tr:baththa, gloss:dağıtıp yaydı} fiilinin yaydığı hayat aynı yeryüzünün iki ölçeğini açar: dağlar durağan dayanağı, baththa canlıların o zemindeki dağılımını görünür kılar. Böylece bağlantı ortak mekân ve ölçek üzerinden kurulur; dağlar hayvanların hareketini başlatan fiziksel neden olarak sunulmaz. Yaratılışa yapılan atıf (31:11) bu iki işi aynı sahnenin parçaları olarak birbirine bağlar. Yağmurla canlanan yeryüzündeki hayat (2:164) canlıların yayılışına yaşanabilir bir ekoloji zemini verir. Daha küçük ölçekte, kayanın, göklerin ya da yerin içinde gizli hardal tanesinin bulunup çıkarılması (31:16), sert kayanın olağan görüşü örttüğü yerde bile filizlenme imkânını açar ve {ar:أَنْبَتْنَا, tr:anbatnā, gloss:bitki çıkardık / yetiştirdik} ile taşınan büyüme düzenine temas eder. Her canlı ve yetişen türün kapsamı, küçücük ve saklı ayrıntıyı da düşünmeye açar; hardal tanesi bu bağda hayvanla özdeşleşmeden bitki gelişimine katılır, 31:16 ise ahlaki hesap bakımından da okunabilir. Yerin yutulup sarsılma tehdidi (67:16) bu çoğul hayat alanının dayandığı zeminin riskini görünür kılar.

## Su ve büyüme

Canlıların sayıldığı cümleye eklenen {ar:وَ, tr:wa, gloss:ve}, failin sesini de değiştirir. Yaratma, yerleştirme ve yayma eylemlerinde örtük kalan fail, {ar:أَنْزَلْنَا, tr:anzalnā, gloss:indirdik} ile birinci çoğul kişi olarak duyulur; aynı “biz” bitkiyi de yetiştirecektir. {ar:مِنَ السَّمَاءِ, tr:mina s-samāʾi, gloss:gökyüzünden} inişin kaynağını bildirir. Biraz önceki çoğul göklerden ayrı duran tekil gökyüzü, yukarıdan aşağı ulaşan suyun işlevsel kaynağıdır. Nesnenin {ar:مَاءً, tr:māʾan, gloss:su} diye açıkça adlandırılması, gönderilen şeyi gerçek su olarak belirler; boğazda kapanan sesi de gökten iniş ile büyüme arasında kısa bir işitsel eşik oluşturur.

Yukarıdan gelen su, yeryüzüne ulaşan kaynak olarak fiziksel yarar taşır; Rahmet diliyle başlayan besmele (31:0) ve hemen sonraki yaratılış atfı (31:11), bitkiyi beslemesini yaratılmış hayata sunulan ikram olarak düşündürür. {ar:أَنْزَلْنَا, tr:anzalnā, gloss:indirdik} iyilik, ceza ya da bildiriyi de aşağı ulaştırabilen geniş bir fiildir; burada açıkça adlandırılan {ar:مَاءً, tr:māʾan, gloss:su}, gökten iniş ve bitki büyümesine katkısıyla fiziksel sahneyi kurar. Su bir isim olarak, {ar:أَنْزَلْنَا, tr:anzalnā, gloss:indirdik} ise onu aşağı ulaştıran fiil olarak belirir; bu seçim suyun amaçlı biçimde birine sunulması çağrışımına da yer açar. Ayet kuyu ya da insan eliyle sulama, su düzeyi, yağışın miktarı ve hızı veya meyvenin olgunlaşması gibi ayrıntıları vermez; odağı suyun aşağı gönderilip bitkiyi beslemesidir.

Suyun gelişi, daha önce duyduğumuz görme fiiline su sağlama yönünde bir yankı kazandırır. {ar:تَرَوْنَهَا, tr:tarawnahā, gloss:onu görürsünüz} olağan anlamıyla görmeyi sürdürür; aynı sözcüğün başkaları için su çekip getirmeyi anlatan kullanımı, ardından gelen {ar:أَنْزَلْنَا, tr:anzalnā, gloss:indirdik}, gerçek {ar:مَاءً, tr:māʾan, gloss:su} ve büyümeyi sağlayan {ar:أَنْبَتْنَا, tr:anbatnā, gloss:yetiştirdik} ile temas eder. Görünen yapıdan yeryüzüne ulaştırılan suya uzanan bu temas, kısa bir su sağlama köprüsü kurar. Bu bağlantıda ikinci çoğul kişi eki {ar:وْنَ, tr:-ūna, gloss:ikinci çoğul kişi eki} biçimsel sınırı belirler: eki su taşıma anlamıyla yüklemeyiz, fiilin olağan çevirisi “görürsünüz” olarak kalır. Böylece su sağlama yankısı, temel anlamı değiştirmeyen ve ayetin içinde sınanabilen bir köprü olarak işler.

Göklerin karşısında aşağıdaki alanı kuran aynı {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü}, şimdi suyun alındığı ve bitkinin yetiştiği zemindir. Tekrarlanan {ar:فِيهَا, tr:fīhā, gloss:onda} önce canlıların, sonra bitkilerin bu yerde bulunduğunu gösterir. Geniş yeryüzü anlamı korunurken su ve büyüme bu bağlamda yumuşak, verimli bir alt zemin niteliği de duyurur; bu nitelik her arazinin işlenmiş ya da aynı ölçüde verimli olduğunu ileri sürmez.

İnişle büyüme arasındaki sonucu {ar:فَ, tr:fa, gloss:böylece} bağlacı kurar: su gelir ve ardından bitki yetişir. Ettirgen {ar:أَنْبَتْنَا, tr:anbatnā, gloss:bitki çıkardık / yetiştirdik} biçiminde aynı birinci çoğul fail önce suyu indirir, sonra gelişmeyi gerçekleştirir; bitkinin topraktan filizlenmesi ilahî eylemin görünür çıktısı olur. {ar:فِيهَا, tr:fīhā, gloss:onda} zamiri yeri büyümenin gerçekleştiği ortam yapar. Filizlenme fiilinin yetiştirme ya da ekimin başlangıcını düşündüren yanı, doğadaki gelişimle ekim arasındaki sınırlı benzetmeyi açar; bu sahnenin faili aynı ilahî çoğuldur, insan çiftçi, tohum ve sürme işi anlatıya girmez.

Yetişen ürünlerin kapsamını açan {ar:مِنْ, tr:min, gloss:-den / arasından}, {ar:كُلِّ زَوْجٍ كَرِيمٍ, tr:kulli zawjin karīmin, gloss:her değerli çift ya da tür} ifadesine bağlanır; buradaki min suyun kaynağını değil, ürünlerin aralığını belirler. Canlılar için kullanılan ilk {ar:كُلِّ, tr:kulli, gloss:her / bütün} şimdi bitkiler için yeniden gelir; biçimce tekil bu niceleyici her sınıfı kapsar. {ar:زَوْجٍ, tr:zawjin, gloss:çift / tür}, birbirine bağlı iki öğeyi bir bütün ve karşılıklı eşler halinde anlatabildiği gibi ortak bir özellikle ayrılan tür ya da sınıfı da gösterebilir. “Her” kapsamının açtığı çeşitlilik ve hemen ardından gelen {ar:كَرِيمٍ, tr:karīmin, gloss:değerli} sıfatı tür ya da ürün okumasını öne çıkarır; eşleşmiş çift okuması da canlı kalır, ancak sözcük biyolojik cinsiyet ya da katı bir taksonomi seçmez. {ar:كَرِيمٍ, tr:karīmin, gloss:değerli} doğrudan kendinden önceki çifti ya da türü niteler. Kendi alanında üstün ve övgüye değer sayılma anlamı bitki bağlamında gür, yararlı ve nitelikli ürüne ulaşır. Aynı sözcüğün yağmur getirip suyunu bol veren bulut kullanımında su bolluğu, bitkisi iyi yetişen verimli yer kullanımında ise yetişme niteliği öne çıkar; bu iki yankı odaktaki su, büyüme ve ürün bağını bitkinin verimliliğine taşırken övgüye değer niteliği de korur. Su, çift ve niteliği bildiren sıfatın peş peşe gelen tenvinli kapanışı ürünü işitsel olarak belirginleştirir.

Yetişen ürün başka ayetlerdeki yaşam ve kaynak imgeleriyle buluşunca, her biri okumanın ayrı bir boyutunu açar. Yeryüzünün bitirdiklerinden çiftleri ve bilinmeyen türleri anan ayet (36:36), {ar:زَوْجٍ, tr:zawjin, gloss:çift / tür} için iki kullanımı da destekler; su çekilirse onu kimin geri getireceğini soran ayet büyümenin kaynağa bağımlılığını öne çıkarır (67:30). Çocuğun taşınması ve sütten kesilmesi anlatısı (31:14), alıcı bir girdinin gelişen hayatı sürdürmesine beden üzerinden sınırlı bir benzerlik ekler; suyun bitkiye ulaştırılmasıyla çocuğun taşınması ayrı süreçlerdir. Bu katkılar birlikte, odaktaki su, toprak, büyüme ve ilişkili türleri birbirine bağlı bir yaşam alanı olarak duyurur.

Bu alandaki {ar:كَرِيمٍ, tr:karīmin, gloss:değerli}, ürünün değerini tek bir niteliğe kapatmaz. Şükür ve anne-babaya iyilik çağrısı sözcüğün övgüye değer ve soylu niteliğini belirginleştirir (31:14); yeryüzünün yetiştirdiklerini ve bilinmeyen türleri anan bağlam ile suyun geri getirilmesine dair soru gür ve verimli yetişme kullanımını canlı tutar (36:36, 67:30). Rahmet dili (31:0) ve yaratılış atfı (31:11), maddi verimliliği yaratılmış nimet çerçevesinde duyurur. Ürün böylece hem iyi yetişmişliği hem övgüye değer oluşu taşıyabilir; 31:10’daki bu nitelendirme ayrı bir ahlak buyruğuna dönüşmez.

Az bir su girdisinin taze sürgünde görünür artışa dönüşmesi şükür için bir benzetme kurar; ayet bu artışı ölçülebilir bir su miktarına bağlamaz. {ar:أَنْبَتْنَا, tr:anbatnā, gloss:filizlendirdik / yetiştirdik} alıcı yerde büyümeyi, {ar:كَرِيمٍ, tr:karīmin, gloss:bereketli / övgüye değer} iyi yetişmiş ürünü taşır. Şükrün yararının şükredene dönmesi (31:12) ve işaretleri alımlayan şükredenlerin anılması (31:31), artışı verene ödenen bedelden çok alıcıda beliren bir karşılık gibi düşündürür. Bu benzetme yağmurla bitki gelişmesinden şükür ilişkisine uzanır, 31:10’a ayrıca bir şükür buyruğu eklemez.

Dağıtılan canlılarla yerden çıkan bitkiler, çokluğun yeniden harekete geçmesini iki ayrı imgeyle düşündürür. {ar:بَثَّ, tr:baththa, gloss:dağıtıp yaydı} dağılmış hayatı, {ar:أَنْبَتْنَا, tr:anbatnā, gloss:filizlendirdik / yetiştirdik} topraktan yeniden beliren hayatı verir. Toplu yaratılış ve diriltmenin tek bir canınki gibi anlatılması (31:28) çokluğu tek can ölçüsünde kavramaya, yağmurla dirilen yerin insan yaratılışıyla yan yana getirilmesi (22:5) ekolojik yenilenmeyi insanın yaratılışıyla ilişkilendirmeye, dağılmış canlıların sonradan toplanması (42:29) ise yayılmış hayattan yeniden toplanmaya geçişi düşünmeye imkân verir. Birlikte, dağınık çokluğun tek bir can ölçüsünde yeniden işleyebileceği temasını genişletirler. Ekolojik belirme diriliş için maddi bir alıştırma sunabilir; 31:28’in diriltmenin kolaylığını vurgulayan okuması da bu çağrışımın yanında açık kalır.

Yeryüzünde beliren bitki izi, ağaçların kalem ve çoğaltılan denizin mürekkep olduğu, sözlerin tükenmediği anlatımla başka bir yönden kesişir (31:27). Odak ayetteki çoğul {ar:السَّمَاوَاتِ, tr:as-samāwāti, gloss:gökler} ile su kaynağı olan tekil {ar:السَّمَاءِ, tr:as-samāʾi, gloss:gökyüzü} ayrı biçimlerdir; tekil biçimin aynı söz ailesi yılın ilk yağmurunu da adlandırabilir. Bu yağmur anlamı “gökyüzü” çevirisinin yerine geçmez; ağaç-kalem ve yenilenen deniz imgeleri (31:27) onu etkinleştirir. {ar:أَنْبَتْنَا, tr:anbatnā, gloss:bitki çıkardık / yetiştirdik} ile büyüyen bitki yağmurun bıraktığı izi görünür kılar ve ileride yazı aracı olabilecek malzemeyi verir. Aynı bağlam büyüklük benzetmesi olarak da okunabilir; bu yazı malzemesi yankısı 31:10’u zorunlu olarak metin yazımı hakkında yapmaz.

Bitkiyi besleyen su gökten yeryüzüne inerken, 31:32’de denizden yükselen karışık, kabaran dalga insanları örter ve göğe benzeyen gölgelikler gibi üstlerine kapanır (31:32). {ar:السَّمَاوَاتِ, tr:as-samāwāti, gloss:gökler} ile tekil {ar:السَّمَاءِ, tr:as-samāʾi, gloss:gökyüzü / üst örtü} yukarıdaki örtüyü, {ar:أَنْزَلْنَا, tr:anzalnā, gloss:aşağı indirdik} odak sahnenin iniş yönünü, {ar:مَاءً, tr:māʾan, gloss:su} ise hayat girdisini taşır. İki imge aynı su temasını ayrı yön ve etkilerle kurar: gökten inen su bitkiyi besler, denizden yükselen su insanı örter ve görüşü kapatan bir kütleye dönüşür. Böylece yararlı kaynak yön ve şiddet değişince tehdide ulaşabilir; 31:32’deki fırtına imgesi odaktaki yağmurun faydalı niteliğini geriye dönük değiştirmez.

Görünür su ve büyüme sırası gözle izlenebilen bir düzen sunar; gelişimin bütün zamanı ve gizli içeriğine dair bilgi başka bir alandır. {ar:تَرَوْنَهَا, tr:tarawnahā, gloss:onları görürsünüz} gerçek algıyı açar; {ar:أَنْزَلْنَا, tr:anzalnā, gloss:indirdik} suyu indirir, {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü / toprak} onu alıp bitkiyi yetiştirir ve {ar:زَوْجٍ, tr:zawjin, gloss:eş / çift} ilişkili üretimi görünür kılar. Yağmurla yeri yeniden anan ayet, aynı yerde rahimlerin gizli içeriğini, yarınki kazancı ve ölümün nerede olacağını insan bilgisinin kuşatamadığı alanlar olarak sıralar (31:34). Oradaki {ar:ٱلْغَيْثَ, tr:al-ghayth, gloss:yağmur / yardıma yetişen yağmur} yağmuru hayata yetişen bir yardım olarak da duyurur; suyun çekilmesi halinde onu kimin getireceğini soran ayet bu bağımlılığı öne çıkarır (67:30). Bitkinin gelişimi gözle izlenirken zamanı, saklı içeriği ve insanın kendi sonucuna dair bilgi sınırda kalır. Bu karşılaştırmanın sınırı, görünür büyümeyi bütün gizli süreçleri kuşatan bilgiyle bir tutmamaktır; 31:34’ün ilahi bilgi vurgusu, 31:10’daki görme çağrısının yaratılış düzenine dönük okumasını ortadan kaldırmaz.

Rahimlerde saklı olandan söz edilmesi, yeryüzünü girdi alan bir gelişme ortamı olarak düşünmeye kapı aralar. Çocuğun içeride taşınması ve sütten kesilmesi anlatısı (31:14), rahimlerin gizli içeriğine ilişkin bilgiyle birlikte (31:34), beden içinde taşınan ve zamanla gelişen hayatı örnekler. Odak ayette {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} suyu alan zemini, {ar:فَأَنۢبَتْنَا, tr:fa-anbatnā, gloss:bitki çıkardık / yetiştirdik} yerden beliren gelişmeyi, {ar:زَوْجٍ, tr:zawjin, gloss:çift / tür} ise ilişkili ürünleri gösterir; bu öğeler yeryüzünün bağımlı gelişimi barındırıp görünür kılmasıyla sınırlı bir beden benzetmesi kurar. Taşıma imgesi ayrıca meyve taşıyan bir dalı da düşündürebilir; dal çağrışımı rahim benzetmesinden ayrı bir görüntü olarak kalır. Gizli rahim, görünür hale gelen gelişmenin içte kalan yanını belirler. Bu keşifsel benzetmede toprak insan annesiyle, bitki de gebelik süreciyle özdeşleşmez.

</source_prose>
