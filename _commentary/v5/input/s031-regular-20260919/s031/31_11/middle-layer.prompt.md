# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:11**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.middle.claims.json`

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
- Refer to source paragraphs as `31:11 ¶N`.

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

`(31:11 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:11",
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
        "citation": "(31:11 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_11/31_11.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_11/31_11.middle.claims.json \
  --ayah-ref 31:11
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_11/31_11.prose.editorial.tr.md`

<source_prose>
## Düzen ve istenen karşılık

31:10’da gökler görünür sütunlar olmadan yükselir; yeryüzü savrulmasın diye dağlar yerleştirilir, canlılar bu alana yayılır, gökten su iner, yerden bitkiler biter ve çeşitler çiftler hâlinde belirir. {ar:عَمَدٍۢ, tr:ʿamadin, gloss:sütunlar} yokluğu desteği tek başına görünen bir sütunla özdeşleştirmeyi zorlaştırırken {ar:رَوَٰسِىَ, tr:rawāsiya, gloss:sağlam dağlar} ve {ar:تَمِيدَ, tr:tamīda, gloss:sallanmak} çevresindeki ifade yeryüzünün hareketini sınırlayan ilişkiyi belirginleştirir. {ar:بَثَّ, tr:baththa, gloss:yaydı} canlıların bu alana dağılışını, {ar:مَآءًۭ, tr:māʾan, gloss:su} ile {ar:فَأَنۢبَتْنَا, tr:fa-anbatnā, gloss:yetiştirdik} suyun ulaşmasını ve büyümeyi, {ar:زَوْجٍۢ, tr:zawjin, gloss:çift, tür} ise çeşitlerin ilişkili belirişini gösterir. Böylece yaratılış, etkileyici nesnelerin toplamından çok sabitleme, sınırlanmış devinim, yayılma ve büyüme içeren bir düzen olarak okunur; bütün adımların tek bir mekanizma ve koordineli bir yönetim oluşturması ise sıralamadan çıkarılan bir yorumdur.

31:10’daki {ar:تَرَوْنَهَا, tr:tarawnahā, gloss:onu ya da onları görürsünüz} sözü de 31:11’deki gösterme buyruğuna ayrı bir görsel zemin açar. Zamirin göklere mi, yokluğu belirtilen sütunlara mı döndüğü açık değildir; göklere dönüyorsa görünmeyen destek karşıtlığı zayıflar. Yine de 31:10’daki görme ile 31:11’deki gösterme ardışık kalır: dağların sabitleyici etkisi, onu taşıyan ilişkinin ayrı bir sütun gibi görünmesi gerekmeden de gözlenebilir. Bu belirsizlik her nedenin görünmez sayılmasını gerektirmez.

Bu dizinin ardından 31:11’deki {ar:هَٰذَا, tr:hādhā, gloss:bu}, hemen yanındaki {ar:خَلْقُ ٱللَّهِ, tr:khalqu llāhi, gloss:Allah’ın yaratışı} tamlamasını gösterir; tek bir nesneyi seçmekten çok yaratılış iddiasının bütününü toplar. Tamlamadaki {ar:ٱللَّهِ, tr:allāhi, gloss:Allah} adı yaratışın sahibini karşılaştırma başlamadan belirler, böylece önce sergilenen düzen ile onu kime nispet eden ifade arasında yerel bir bağ kurulur. Bu isnat yaratıcıyı tanımlar; her nedensel sürecin nasıl işlediğine dair kapsamlı bir kuramı belirlemez.

Bu başlangıç noktasından {ar:فَ, tr:fa, gloss:bu yüzden} ile gösterme buyruğuna geçilir: yaratış Allah’a nispet edildiğine göre karşı taraftan da bir eser göstermesi beklenir. Başka bir yaratıcı ileri sürülüyorsa onun ürününü gösterme koşulu da bu bağda örtükçe duyulur; bu koşul, bağlacın açık sonuç işlevinin yanına eklenir. {ar:خَلْقُ, tr:khalqu, gloss:yaratılış} olağan anlamıyla var etmeyi ve yaratılmış düzeni taşırken, söz ailesindeki ölçü ve sınırları işe başlamadan önce belirleme kullanımı 31:10’daki ayrı işlemlerle temas eder. Böylece yaratılış ölçüsü belirlenmiş ve incelenebilir bir eser olarak da duyulur; bu okuma belirli bir zanaat süreci çizmez ve yaratmayı yalnızca ölçmeye indirgemez. İsimdeki yaratılış ile {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} fiilindeki eylem, soruyu aynı isnada yöneltir; karşılaştırma kapsam ve sonuçları eşitlemeden o isnadı sınar.

İşaret edilen eser böylece istenen karşı-ürüne dönüşür. Çoğul muhataba yöneltilen {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} buyruğundaki “bana” eki, gösterimin alıcısını konuşan olarak belirler; söz önce görsel bir sunum ister. Öne alınmış {ar:مَاذَا, tr:mādhā, gloss:ne} sorusu dikkati faillerin kimliğinden önce gösterecekleri ürüne çeker. Bu öğe tek bir soru sözcüğü ya da “mā + dhā” diye iki parçalı bir kuruluş olarak çözümlenebilir; ikisi de aynı yaratma fiilinin nesnesini sorar, ikinci çözüm yalnızca şaşkınlığı biraz daha duyulur kılabilir.

Sorudaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} tamamlanmış bir eylemi sorar: gelecekte ne yapabilecekleri değil, şimdi gösterebilecekleri bir eser istenir. Bu perfekt biçim talebi tamamlanmış bir ürüne yöneltir; tek başına böyle bir ürünün bulunmadığı sonucunu vermez. Tekil fiil, çoğul ilgi zamiri {ar:ٱلَّذِينَ, tr:alladhīna, gloss:kimseler} tamamlanmadan önce geldiği için okur önce eylem ve nesne sorusunu, sonra failleri öğrenir; fiilin dilbilgisel öznesi yine bu çoğul sınıftır. Böylece cümle, önce karşılaştırmanın ölçüsünü ve istenen ürünü kurar, ardından o ürünü göstermesi beklenenleri tanıtır.

## Faillerin sınırı ve hükmün yönü

Failler özel bir ad ya da sabit bir listeyle değil, {ar:ٱلَّذِينَ, tr:alladhīna, gloss:kimseler} ile hemen arkasındaki {ar:مِن دُونِهِۦ, tr:min dūnihī, gloss:O’ndan başkası} ilişkisinde kurulur. İlk tamlamadaki Allah adı, bu öbekteki zamirin dayanağıdır: yaratılış Allah’a nispet edilirken sınanan sınıf da aynı referansa göre belirlenir. {ar:مِن, tr:min, gloss:-den} ile {ar:دُونِهِۦ, tr:dūnihī, gloss:O’nun dışı} Allah’a göre ayrılma ve dışlama ilişkisi kurar; bu öbekte rakipleri O’ndan türemiş bir kaynak saymaz, işlevi de her {ar:مِن, tr:min, gloss:-den} kullanımına genellenmez. Yerleşik bu dışlama öbeği faili ilişkiden koparmadan tanımlar; okur sınıfın hangi ilişkiyle kurulduğunu görürken üyelerin kimliğini açık bırakır.

{ar:دُونِهِۦ, tr:dūnihī, gloss:O’ndan başkası} olağan olarak Allah’tan başkasını bildirir; yakınlık ya da alt konum tınısı da Allah’ın yaratılış tamlamasındaki ölçü yeriyle etkinleşebilir. Bu, rakiplerin eylemini ayrı bir iddia olmanın yanında o ölçütün gerisinde kalma ihtimali olarak duyurur; fiziksel mesafe veya değer sıralaması kurmaz. Bu ilişki, ölçülebilir işlemler yapan yakın ya da tâli faillerden de gösterilebilir ürün isteyebilirken yaratmanın başlangıç kaynağını sınar. Belirli bir aracı neden ya da tam nedensellik hiyerarşisi koymadan ve her doğal süreci rakip saymadan, yaratmanın kaynağıyla düzenleme işlemlerini ayıran sınırlı bir soru olarak kalır.

{ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} IV. babın çoğul muhataba yöneltilmiş ettirgen buyruğudur; görsel sunumu isterken bir şeyi görüşe ya da yargıya sunma yönünü de taşır. Ardından gelen yaratma sorusu görülen ürünü değerlendirilebilir kanıta çevirir; konuşan hem sunulanın alıcısı hem de onu değerlendiren kişi konumuna yaklaşır. Bu yargı yönü görsel isteğin önüne geçmez ve bir düş ya da özel görü sahnesine dönüşmez. Adı konmuş bir insan yargıç veya biçimsel bir mahkeme olmadan da konuşanın istediği esere verdiği ölçü belirgindir.

İstenen sergiden sonra gelen {ar:بَلِ, tr:bal, gloss:bilakis}, rakiplerden bir ürün sunulacağı beklentisini kesip sözü hükme çevirir. Talep açık kalırken ayet kendi teşhisini ekler; bir karşılık verildiğini varsaymadan soru kanıt isteği olarak sürer. Emrin “bana” dediği alıcı şimdi hükmün değerlendirdiği konuma da yaklaşır ve konuşma sınıflandırıcı bir yargıya yönelir.

Hükmün öznesi olan belirli tanımlıklı etken ortaç {ar:ٱلظَّٰلِمُونَ, tr:aẓ-ẓālimūna, gloss:zulmedenler}, tek bir eylemi değil, tanımlanabilir bir sorumlu yanlış yapanlar sınıfını adlandırır; kişileri tek tek saymaz. Çoğul muhataba yöneltilen emirden üçüncü kişi öznesine geçiş, dinleyicileri hükmün karşısında duran bir sınıf olarak duyurur. Sözcüğün belirli tanımlıkla başlayan vurgulu sesi de yeni çerçeveyi işitsel olarak ayırır; muhataplarla hükmedilenlerin aynı ya da ayrı kişiler olması bu geçişten çıkarılamaz. Böylece cümle, kimlik eşitlemeden sorumlu sınıfı görünür kılar.

31:13’te ortak koşmanın büyük haksızlık diye adlandırılması, yaratıcı payesinin yanlış yere verilmesini somutlaştırabilir: başkasına ait yaratma işi başka bir varlığa aktarılmış, ona uygun olmayan bir pay tanınmıştır. {ar:ٱلظَّٰلِمُونَ, tr:aẓ-ẓālimūna, gloss:zulmedenler} ailesindeki şeyi kendine uygun yer, pay ya da sınırdan çıkarma imgesi bu atfı anlaşılır kılar; bu, belirli bir hukuk kuralından çok yanlış paylaştırmanın imgesidir. Aynı söz ailesinin ışığın sönmesi ya da görünür olanın örtülmesi benzetmesi, son yüklemdeki {ar:مُّبِينٍۢ, tr:mubīnin, gloss:apaçık} ile buluşunca yanlış atfın ahlaki ve düşünsel bulanıklığını belirginleştirebilir; bu bağ mecazidir, fiziksel gece anlatmaz. 29:17’de Allah’tan başkasına tapınma asılsız söz üretmeyle, 46:32’de koruyuculara dayanma apaçık sapmayla birlikte anılır. Bu temaslar yanlış atfın ahlaki ağırlığını gösterirken ortak koşmanın daha geniş inanç yanlışı içindeki yerini de korur.

Son yüklemde {ar:فِى, tr:fī, gloss:içinde} soyut {ar:ضَلَٰلٍۢ, tr:ḍalālin, gloss:sapma} adını ikinci bir etiket hâline getirmek yerine zulmedenleri bir durumun içine yerleştirir. Bu, dilbilgisel bir mekân imgesidir; gerçek bir yolculuk ya da fiziksel yer anlatmaz. {ar:ضَلَٰلٍۢ, tr:ḍalālin, gloss:sapma} doğru yoldan, amaçtan veya uygun yönden ayrılmayı taşır; yaratılışın yanlış yere nispet edilmesi böylece hem ahlaki bir yanlış hem de yön ve kavrayış kaybı olarak görünür. Ayet failleri yeniden tanımlamak yerine onları bu teşhis edilmiş durumun içinde bırakır.

Belirsiz tekil biçim, sapmayı belirli tek bir hataya indirmez ve kapsamını ölçmez; belirsizlik de tek başına sınırsız büyüklük bildirmez. Kökün bir başka yönü, bir şeyin gizlenip algıdan yitmesini düşündürebilir. Gizli kalan güzergâh bu tınıyla kendiliğinden açığa çıkmaz; daha önce var olmuş belirli bir nesnenin fiziksel olarak kaybolduğu da söylenmez. Sergiye gelmeyen ürünle bu yankı birleştiğinde, yanlış atıf ile gözden kaçan doğru kaynak arasındaki gerilim duyulur.

Kapanıştaki {ar:مُّبِينٍۢ, tr:mubīnin, gloss:apaçık}, IV. bab etken ortaç biçimiyle olağan olarak açık ve anlaşılır olanı niteler; eril tekil, belirsiz ve mecrur uyumuyla {ar:ضَلَٰلٍۢ, tr:ḍalālin, gloss:sapma} adına bağlanır, zulmedenlere değil. İkisinin sonundaki “-in” ses ritmi teşhisi tek bir kapanış gibi duyurur. {ar:مُّبِينٍۢ, tr:mubīnin, gloss:apaçık} bir şeyi açığa çıkarma yönünü de taşır: ürün istenip sergi yerine hüküm geldiğinde sapma teşhisi ve karşılaştırmada açığa çıkan boşluk okur için anlaşılır hâle gelir. Bu açıklık yeni bir konuşan ya da ayrı bir ifşa olayı eklemez. Kökün ayırma ve iki uç arasındaki aralık tınısı, Allah’a nispet edilen yaratılışla rakiplerin eylemini birbirinden ayrı tutan {ar:دُونِهِۦ, tr:dūnihī, gloss:O’ndan başkası} ilişkisine de temas edebilir; bu ayetteki temel karşılık “apaçık”tır, ayırma tınısı ise ikincil kalır. Başlangıçtaki işaret, gösterme buyruğu ve bu son sıfat görünür eserden istenen karşı-ürüne, oradan anlaşılır hâle gelen teşhise uzanır.

## Ürünün sınanması ve sözün dolaşımı

Bu gösterme sınaması 35:40 ve 46:4’te benzer yaratma çağrılarıyla, 22:73’te ise bir sineği bile yaratma ölçüsüyle başka yerlerde somutlaşır. 46:4’te kitap ya da bilgiye dayalı bir iz de istenir; yaratıcı iddia böylece addan gösterilebilir ürüne ve dayanağı sorulabilir kanıta taşınır. Bu bağımsız çağrılar, {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} buyruğunun kamusal karşılaştırma ölçüsünü belirginleştirir, 31:11’de istenen ürünün ne olduğunu değiştirmez. Eserin gösterilmemesi gerçeği olmayan bir sözün riskini açığa çıkarabilir; bu sınama ürün ve dayanak ister, konuşanın kasıtlı yalan söylediğini tek başına belirlemez.

{ar:خَلَقَ, tr:khalaqa, gloss:yarattı} olağan anlamıyla yaratmayı ve var etmeyi sürdürürken, aynı söz ailesi gerçeği olmayan bir söz ya da anlatıyı tasarlayıp üretmeyi de kapsar. Öne alınan {ar:مَاذَا, tr:mādhā, gloss:ne} ve istenen {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} sergisinin ardından gelen {ar:بَلِ, tr:bal, gloss:bilakis} hükmü, karşılıksız yaratıcı isnadını eser yerine kurulmuş anlatı gibi duyurabilir. 29:17’de Allah’tan başkasına tapınmanın asılsız sözle yan yana gelişi bu sözel çağrışıma ayrı bir zemin verir. Yankı, yaratma fiilinin olağan anlamını ve gösterilebilir işe yönelen soruyu korur; fiile “uydurmak” ya da “yazmak” karşılığı vermez, konuşana da belirli bir yalan veya kasıt yüklemez.

31:6’da {ar:يَشْتَرِى, tr:yashtarī, gloss:satın alır} fiiliyle edinilen {ar:لَهْوَ, tr:lahwa, gloss:oyalayıcı meşguliyet} ve {ar:ٱلْحَدِيثِ, tr:al-ḥadīthi, gloss:söz, anlatı}, dikkati Allah’ın yolundan uzaklaştırabilen ve bilgiye dayanmayan bir söylem ortamı kurar. Satın alma bu sözü isteyerek edinilmiş bir ikame gibi duyurur; 31:6 bu konuşmayı başka yaratıcıların dünyayı kurduğu iddiası diye adlandırmaz, dolayısıyla ikame gösterme talebine cevap olmaz. Oyalayıcı meşguliyet dikkati istenen üründen başka yöne çekerek delil baskısını dağıtabilir; bu olasılık her dinleyene yüklenmez. Söz ve anlatı, yenilenip dolaşabilen bir söyleme zemin sağlarken odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} için sahte-üretim tınısını da etkinleştirebilir: eser gösterilmediğinde iddia, eser yerine dolaşan bir anlatı gibi kalır. 31:6’daki {ar:لِيُضِلَّ, tr:li-yuḍilla, gloss:saptırmak için} ile odaktaki {ar:ضَلَٰلٍۢ, tr:ḍalālin, gloss:sapma} aynı yön kaybı imgesinde buluşur; {ar:بِغَيْرِ عِلْمٍۢ, tr:bi-ghayri ʿilmin, gloss:bilgi olmaksızın} bu satın alınan söylemin dayanağını sınırlar, konuşanların her alandaki bilgisini değil. Böylece bu ayrı sahne, ürün gösteremeyen bir iddianın dikkati nasıl başka yere çekebileceğine dair sınırlı bir okuma sunar.

Söylemin dolaşımından ayrı bir alımlama sorusu 31:7’de açılır: kendisine ayetler okunan tekil bir dinleyen kibirle yüz çevirir ve işitmemiş gibi davranır. {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} bedensel geri çekilişi, {ar:مُسْتَكْبِرًا, tr:mustakbiran, gloss:büyüklenerek} bu harekete kendini üstün tutma yönünü katar. {ar:يَسْمَعْهَا, tr:yasmaʿhā, gloss:onları işitir} olağan işitmeyi korurken ayetleri alıp anlamaya açıklığı da düşündürebilir; kulaktaki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} alımlama direncini somutlaştırır. Ardından gelen {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} buyruğu, nesnenin yokluğu kadar kanıtı almaya gönüllü olmayı da yoklayabilir. Önceki sahnenin tekil dinleyeni ile odaktaki çoğul muhataplar özdeşleştirilmez; bu olası direnç de bütün muhataplara yüklenmez. Kulaktaki ağırlık alımlama direncini taşıyan bir algı benzetmesidir, fiziksel hastalık tanısı değil; bu işitme sahnesi, gösterme isteğinin kanıtı alma açıklığını da sınayabileceğini düşündürür.

İşitme sahnesinden ayrı bir maddi imge 31:27’de açılır: ağaçlar kalemlere, deniz mürekkebe dönüşür ve denize başka denizler eklense de sözler tükenmez. Bu yazı imgesi, uydurulmuş bir anlatı tınısını başka bir ölçekte düşündürür. Kalem yazar, geniş deniz mürekkebi besler; yine de maddi yazı düzeni sonludur, anlam taşıyan sözlerse bu araçlarla tüketilemez. 31:27 yakındaki bir yücelik imgesidir; odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} yazmak anlamına gelmez ve bu karşılaştırma yaratma sınamasının doğrudan kanıtı değildir. Bu ayrım, sınırlı yazı aracını tükenmeyen sözlerle yan yana tutarken istenen yaratma eserini de kendi ölçüsünde bırakır.

## Görünürlük, gizlilik ve ölçek

İstenen ürünün görünürlüğü, onun hemen göz önünde seçilmesiyle sınırlı kalmaz. 31:16’da ölçüsü belirlenmiş küçücük bir ağırlık, filiz verebilen bir hardal tanesi ve kayanın içinde saklı olanın bulunup çıkarılması anılır. {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} buyruğunun talep ettiği görünür sonuç böylece küçük ve örtülü olana kadar genişler: incelik ya da saklılık yokluk demek değildir. Odak ayet belirli bir kayıp nesnenin izini sürmez; bu sahne saklı olanın bulunabileceğini göstererek görünürlük ölçüsünü genişletir.

31:20’de dışarıda beliren nimetler içeride kalanlarla yan yana gelir; tartışanların bilgi sahibi olmadıkları da belirtilir. Bu karşıtlık görünür kanıt talebini korurken insanın göremediği şeyi kendiliğinden kanıtsızlıkla eşitlemeyi önler. İstenen eser belirgin bir karşılaştırma ölçüsü olmaya devam eder, ancak görme alanı bütün bilginin sınırı sayılmaz.

31:34’te hiçbir canın ertesi gün ne kazanacağını ya da nerede öleceğini bilmediği hatırlatılır. Bu yakın öğüt insan bilgisinin sınırını ekleyerek gösterme talebinin yalnızca yüzeyde hemen seçilebilenlere kapanmadığını düşündürür; yaratma meydan okumasının kanıtı değildir. Bu sınır 31:13’teki ortaklığın haksız atıf diye teşhisini geri çekmez. 31:16’da kayanın içinden çıkarılan şey saklının bulunabilirliğini, 31:20’de dışla içteki nimetlerin yan yanalığı görünün ötesini, 31:34’te bilinmeyen yarın ve ölüm yeri ise insan bilgisinin sınırını belirginleştirir. Bu ayrı sahneler, görüş ve bilgi insanı sınırlasa da yanlış nispetin teşhis edilebildiğini gösterir; tek bir düzenek kurmaz ve 31:11’de istenen yaratma ürününe kanıt oluşturmaz.

31:10’da suyun ulaştırılması ve ardından bitkinin büyümesi, 31:34’teki yağmur imgesiyle buluşunca nimetin görünür büyümedeki etkisini düşündürür. Bu temas {ar:أَرُونِى, tr:arūnī, gloss:bana gösterin} buyruğuna beslenmenin görülebilir sonucu yönünde bir yankı ekler; buyruğun anlamı suyu taşımak değil, bir şeyi başkasına göstermektir. 31:34’ün yağmur ve gayb bilgisi bağlamı bu çağrışımın sınırını çizer: odaktaki meydan okumanın kanıtı değil, beslenmenin görünür etkisidir.

Bu su ve kaya imgeleri, {ar:خَلْقُ, tr:khalqu, gloss:yaratılış} sözünün olağan karşılığından uzak, aynı söz ailesindeki su tutan oyuk anlamıyla keşifsel bir benzetme kurar. 31:10’daki su aktarımı ile 31:16’daki kaya ve filizlenen tohum ayrı sahnelerdir; yan yana geldiklerinde suyu saklayıp daha sonra yaşamı besleyebilen küçük bir hazne imgesi belirir. Bu imge odaktaki yaratılış sözünün olağan karşılığı değil; ayrı sahnelerin uzak yankısı, görünür varlıkların yanında koşulları saklayan bir zemini duyurur.

## Kabul, baskı ve devredilmeyen rol

Hazne benzetmesinden ayrı bir soru, yaratma iddiasını söylenmiş kabul üzerinden sınar. 31:25’te muhataplara gökleri ve yeri kimin yarattığı sorulur; “Allah” derler, ardından çoğunun bilmediği belirtilir. 31:30’da Allah’tan başkasına yöneltilen çağrı gerçekliği bulunmayan bir iddiayla ilişkilendirilir. Odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} ve {ar:دُونِهِۦ, tr:dūnihī, gloss:O’ndan başkası} böylece ilk soruyu verilmiş cevaba karşı bir çapraz sorgu gibi duyurabilir: Allah yaratıcı diye kabul edilmişken başkasına hangi yaratma nispet edilmektedir? Sözlü kabulün bilgi ve kavrayışa bütünüyle yerleşmediği de bu karşılaşmada görünür. 31:30’un hükmü ibadet ve ortaklık hakkında daha geniş olabilir; böylece çapraz sorgu yaratma nispetini sınarken o ayetin daha geniş hükmünü korur.

31:28’de yaratma ile yeniden diriltmenin tek bir can gibi kolay oluşu karşılaştırmaya kişisel bir ölçek ekler. Odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} anlamı yerinde kalırken her muhatabın kendi başlangıcı ve yeniden kaldırılışı çevrede görülen eserin yanına gelir; okur artık yalnızca dışındaki düzeni değil, kendi canlandırılışını da düşünür. Tek canı bu karşılaştırmanın ölçek modeli saymak bir çıkarımdır; yakın bağlam ilahi kudretin kolaylığını da vurgular. Bu kişisel ölçek, görünür ürün talebinin yerine geçmeden okurun kendi yaratılışına da bakmasını sağlar.

{ar:دُونِهِۦ, tr:dūnihī, gloss:O’ndan başkası} ilişkisinin baskı altındaki karşılığı 31:32’de üst üste binip üzerlerini örten dalgalarla belirir. Tehlike içindeyken çağrı ortaklardan ayrılarak yalnız Allah’a yönelir; kurtuluşun ardından kimi ölçülü davranır, kimi de işaretleri bilerek yalanlar. Olağan dayanaklar örtülünce kime seslenildiği ve bu yönelişin kurtuluş sonrasında sürüp sürmediği bir atıf sınamasına dönüşür. Bu sahne yaratma ürününü göstermese de atıf sınamasını bildirilen kapasiteden baskı altındaki yönelişe taşır.

Krizdeki atıf sınamasından ayrı olarak 31:33 aile bağını bir karşılaştırmaya açar: anne-baba çocuk yerine, çocuk da anne-baba yerine hesap konusu olanı üstlenemez; her can kendi hesabını taşır. Bu yakın ilişki bile sorumluluğu devretmediği için {ar:دُونِهِۦ, tr:dūnihī, gloss:O’ndan başkası} ile açılan olası ikameyi sınırlar. Bu sahnenin katkısı yaratıcı yetkinliği kanıtlamak değil, birinin varlığının başkasına ait rolü kendiliğinden üstlenmediğini düşündürmektir.

</source_prose>
