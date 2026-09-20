# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:23**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.middle.claims.json`

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
- Refer to source paragraphs as `31:23 ¶N`.

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

`(31:23 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:23",
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
        "citation": "(31:23 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_23/31_23.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_23/31_23.middle.claims.json \
  --ayah-ref 31:23
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_23/31_23.prose.editorial.tr.md`

<source_prose>
## Kederin Sebebi ve Sınırı

31:23’ün düz cümlesi, inkâr edenlerin Allah’a dönüşünü, yaptıklarının kendilerine bildirileceğini ve Allah’ın göğüslerde olanı bildiğini kurar: {ar:وَمَن كَفَرَ, tr:wa-man kafara, gloss:kim inkâr ederse} için {ar:إِلَيْنَا, tr:ilaynā, gloss:bize} {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} gelir; ardından {ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:onlara bildiririz} ile {ar:بِمَا عَمِلُوا, tr:bi-mā ʿamilū, gloss:yaptıklarını} bildirilir ve kapanışta {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} niteliği {ar:بِذَاتِ ٱلصُّدُورِ, tr:bi-dhāti ṣ-ṣudūr, gloss:göğüslerde olanı} kapsar. Ortadaki {ar:فَلَا يَحْزُنْكَ كُفْرُهُۥٓ, tr:fa-lā yaḥzunka kufruhu, gloss:onun inkârı seni üzmesin} öğüdü, başkasının reddinin muhataba gerçekten ağır gelebileceğini kabul ederken sonucun yükünü ona vermez; keder silinmez, hesabın kime ait olduğu belirginleşir.

Başındaki {ar:وَ, tr:wa, gloss:ve}, önceki söyleyişle bağı sürdürür; tek başına bu örneğe özel bir karşıtlık kurmaz. Ardından gelen {ar:مَنْ, tr:man, gloss:kim}, faili açık bir koşul olarak bırakırken tamamlanmış {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} bu koşulun gerçekleştiğini bildirir. Böylece ifade, gerçekleşmiş bir eylemle nitelenen ama bütün insanlara yayılmayan ve failin tüm hayatını tek başına tanımlamayan bir sınıf açar.

Koşulun ilk karşılığı {ar:فَ, tr:fa, gloss:öyleyse} ile başlar: {ar:لَا, tr:lā, gloss:yapma} olumsuzluğu, “seni üzmesin” anlamındaki {ar:يَحْزُنْكَ, tr:yaḥzunka, gloss:seni üzsün} fiilini yönetir. İkinci tekil nesne eki muhatabı adı anılmadan doğrudan kişiselleştirir; kederin sebebi muhatabın kendisi değil, sahibine iyelik ekiyle bağlanan {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı}dır. Koşuldaki fiil sonra bu sahiplik eki taşıyan ad biçiminde yinelenince, eylem sahibine ait bir hâl olarak kalır ve sorumluluk dilbilgisel düzeyde ona bağlanır. Hitabın sonundaki k ile hemen arkasındaki inkâr adının başındaki k’nin teması, kederin muhatabını ve sebebini işitmede birbirine yaklaştırır; ses yakınlığı bu iki sözü birleştirmese de ilk karşılığın kişiye yönelmiş öğüt olduğunu duyurur. Ceza ya da bütün sonucun dökümü bu öğüdün konusu değildir; ilk karşılık, kederin sebebi ile muhatabını birbirinden ayırır.

Buradaki {ar:يَحْزُنْكَ, tr:yaḥzunka, gloss:seni üzsün}, Arapça I. kalıptaki keder fiilidir ve olağan anlamıyla “onun inkârı seni üzmesin” öğüdünü taşır; kabul edilen IV. kalıp okuyuşu kedere yol açma ilişkisini daha açık kurar. Aynı sözlük alanındaki ayrı bir kullanım, öfke ve kederin gönülde kemirici bir acı bırakmasını anlatır; bu aşınma burada duygusal bir imgedir, bedensel yaralanma tarifi değildir. Bu iç rahatsızlık imgesini, inkârı sebep yapan {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} ile engellenen etkiyi belirleyen {ar:لَا, tr:lā, gloss:yapma} birlikte etkinleştirir. Olağan keder öğüdü böylece korunurken, başkasının reddinin muhatabın içinde tırmalayıcı bir üzüntüye dönüşmesi de duyulur; yasak, duygunun varlığını silmekten çok bu aktarımın muhatabın içine yerleşip onu kemirmesini durduran bir sınır çizer.

İnkârın bu açık anlamı, yakın ayetlerdeki dikkat ve işitme imgeleriyle bir başka basınç kazanır. Oyalayıcı sözü satın alma (31:6) ve ayetler okununca büyüklük taslayarak yüz çevirme (31:7), reddi rehberi almamaya dönük sürdürülmüş bir tutum olarak da gösterebilir: {ar:يَشْتَرِي لَهْوَ الْحَدِيثِ, tr:yaštarī lahwa al-ḥadīth, gloss:oyalayıcı sözü satın alır}, ardından {ar:وَلَّىٰ مُسْتَكْبِرًا, tr:wallā mustakbiran, gloss:büyüklük taslayarak döndü} gelir. Buradaki {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için “örtmek, kapatmak” kullanımı bu yöneliş ve yüz çevirme ile temas eder; {ar:يَحْزُنْكَ, tr:yaḥzunka, gloss:seni üzsün} fiilinin taşıdığı ağır keder de dikkatin saptırılmasına verilen karşılık olarak duyulabilir. “Sanki hiç işitmemiş gibi” sözüyle iki kulakta ağırlık imgesi (31:7), uzaklaşmayı ve anlayıp uymayı reddetmeyi maddi bir işitme imgesiyle yan yana getirir: {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onları işitmemiş gibi} ve {ar:فِي أُذُنَيْهِ وَقْرًا, tr:fī udhunayhi waqran, gloss:iki kulağında ağırlık}. Bu işaretler kibir çevresinde yan yana duran göstergeler olabilir; tek bir neden zinciri kurmaları gerekmez, 31:23’teki inkâr da gerçek işitme engeli değildir. Yine de birlikte okunduklarında, reddi rehberi almama yönünde süren bir tutum olarak görmeye ve kederi bunun muhataptaki bedeli saymaya imkân verir.

Benzer keder hitabı 36:76’da {ar:فَلَا يَحْزُنْكَ قَوْلُهُمْ, tr:fa-lā yaḥzunka qawluhum, gloss:onların sözü seni üzmesin} biçiminde yer alır; çevresindeki {ar:مَا يُسِرُّونَ وَمَا يُعْلِنُونَ, tr:mā yusirrūna wa-mā yuʿlinūn, gloss:gizledikleri ve açıkladıkları}, saklı olanla açığa çıkan arasındaki ayrımı görünür kılar (36:76). 31:23’teki bu yankı, {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için örtme imgesini olağan reddin yanına ekler; açık söz de gizlenen de Allah’ın {ar:إِلَيْنَا, tr:ilaynā, gloss:bize} dönüşü ve {ar:فَنُنَبِّئُهُمْ بِمَا عَمِلُوا, tr:fa-nunabbiʾuhum bi-mā ʿamilū, gloss:yaptıklarını onlara bildiririz} bildirimi ufkunda kalır. Bu bağlantı her kederi yasaklayan bir kurala genişlemez, her reddedişe aynı gizli güdüyü yüklemez ve saklananı çözme yetkisini muhataba vermez. Böylece 36:76’daki saklı-açık ayrımı, 31:23’teki inkârın görünen ve gizli yanlarını ilahî hesap ufkunda birlikte düşündürür.

Şükürle inkârın yan yana gelişi bu örtme imgesine nimet boyutunu ekler. 31:12’de {ar:أَنِ اشْكُرْ لِلَّهِ, tr:ani ushkur li-llāh, gloss:Allah’a şükret} buyruğunu, şükredenin kendisi için şükrettiğini belirten {ar:وَمَن يَشْكُرُ فَإِنَّمَا يَشْكُرُ لِنَفْسِهِۦ, tr:wa-man yashkuru fa-innamā yashkuru li-nafsihi, gloss:kim şükrederse kendisi için şükreder} izler; karşısında {ar:وَمَن كَفَرَ, tr:wa-man kafara, gloss:kim inkâr ederse} vardır ve Allah {ar:غَنِيٌّ حَمِيدٌ, tr:ghaniyyun ḥamīd, gloss:muhtaç olmayan ve övülen} diye nitelenir (31:12). Bu ayrı nimet bağlamı her inkârı nankörlük diye adlandırmadan, 31:23’teki {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için nimeti örtme ve şükrü esirgeme çağrışımı açar. Kayıp onu örten kişide kalır; bu, muhatabın kaygısını telafi borcuna dönüştürmeden nimet kaynağının eksilmediğini duyurur.

31:23’te {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} fiiliyle {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} ismi olağan reddedişi taşır; sözlükteki örtme kullanımı bu anlama bir içeriği kapatma imgesi ekler. Örtme kullanımına {ar:ذَاتِ ٱلصُّدُورِ, tr:dhāti ṣ-ṣudūr, gloss:göğüslere ait olan} iç alanı, tamamlanmış {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptılar} işler ve {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} bildirme eylemi ayrı ayrı temas eder; inkâr böylece {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} sırasında açığa çıkacak gizli içeriğin üstündeki örtü gibi duyulur. Bu örtü fiziksel değildir; 31:12’deki nimet çağrışımı ayrı bir bağlamsal uzanım, kefaret anlamları ise ayrı bir türetimdir. Böylece sözlükteki örtme imgesi olağan inkârı değiştirmeden, dönüşte açığa çıkacak içeriğe bağlar.

## Dönüş ve Bildirim

Keder öğüdünden sonra varışın yönü ve eyleyen değişir. Öne alınan {ar:إِلَيْنَا, tr:ilaynā, gloss:bize}, önce varış yerini duyurur; ardından {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ile topluluk gelir. Tekil {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} biçiminden çoğul dönüşe ve {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} biçimine geçiş, alanı tekil inkâr eyleminden dönüşü ve işleri bildirilecek topluluğa genişletir; bu geçiş sahibini silmez ya da topluluktaki herkese aynı işi yüklemez. İkinci tekil muhatabın ardından birinci çoğul yönelme ve bildirme biçimleri gelince, yerel fail ve varış odağı ilahî tarafa geçer; muhatabın kendi eylem alanı ve hissedebileceği keder sürerken cümle topluluğun dönüşü ile bildirimine açılır.

{ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} dönüş eylemini, varış yerini ya da vaktini adlandırabilen bir isimdir; çoğul biçim dönüşün öznesini korur, ifadeyi edilgen bir “döndürülme” fiiline çevirmez. Ölümden sonraki son varışın Tanrı huzuruna dönüş diye anıldığı kullanım da burada bir ufuk açar: öne alınmış ilahî varışla hemen ardından gelen bildirim, dönüşü son-varış ve hesap bağlamında duyurur. Âyet belirli bir ölüm-sonrası olay, yol ya da diriliş takvimi vermez. Önce yönün, sonra dönenlerin duyulması, hesabın kime varacağını cümlenin başında görünür kılar.

Dönüşten sonraki ikinci {ar:فَ, tr:fa, gloss:ardından}, bildirmeyi içeriğiyle sıraya koyar: {ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:sonra bildiririz} ve {ar:بِمَا عَمِلُوا, tr:bi-mā ʿamilū, gloss:yaptıklarını}. İlk {ar:فَ, tr:fa, gloss:öyleyse} koşuldan keder öğüdüne geçerken bu ikinci fa dönüşten eylemlerin bildirilmesine geçirir; okur iki karşılığı tek olay saymadan izler. Keder yasağıyla dönüşün art arda gelişi, çözümlenmemiş sonucu muhatabın iç yükünden Allah’a varan hesaba bırakır. Bu bir duygusal emanet benzetmesidir: dönüş sözcüğü yeni bir sözlük anlamı kazanmaz, ama art arda gelen yön ve bildirim kedere zamansal bir ufuk verir.

{ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} sözlükte bir söze ya da iletiye dönen yanıtla ilişkilendirilen kullanımlara da temas eder; burada ad yine dönüşü bildirir. Ardından gelen {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} ile {ar:بِمَا عَمِلُوا, tr:bi-mā ʿamilū, gloss:yaptıklarını} bağımsız olarak bir haber ve içeriğini sağladığı için dönüş, reddin ertelenmiş cevabı gibi duyulabilir. Bildirme fiilinin sözlük alanındaki yerden yere geçme kullanımı bu çekimli II. kalıp fiilin olağan anlamı değildir; burada II. kalıp sonuç taşıyan bir haber vermeyi anlatır, aynı kökten peygamberlik mertebesi bildiren türetimler bu kullanımı yeniden adlandırmaz. Dönen topluluk ve önceden verilen varış yeri, haberin dönüşle birlikte varışa ulaşması için sınırlı bir imge kurar; bilginin kendisi yolculuk etmez. Bu, insanlarla gerçek bir konuşma, belirli bir bekleme süresi ya da gelecekte bütün kederin silinmesi vaadi değildir; bildirimin konusu âyetin söylediği işlerdir. Bu bağlantı, dönüşe bağlanan bildirimi gündelik bir nottan daha ağır ve bilgi verici duyurur.

{ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:sonra bildiririz} bildirim fiili birinci çoğul kişiyle ilahî özneyi, üçüncü çoğul nesne ekiyle daha önce anılan topluluğu gösterir; dönenler bildirimin doğrudan alıcısıdır. İlk {ar:بِمَا, tr:bi-mā, gloss:yaptıklarıyla}, bildirimi {ar:مَا عَمِلُوا, tr:mā ʿamilū, gloss:yaptıkları} içeriğine bağlar. {ar:مَا, tr:mā, gloss:ne} daha dar bir eylem türü seçmeden alanı açar; tamamlanmış çoğul {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptılar} bu alanı bitmiş işlerle doldurur. Sözlükteki iş, emek ve bilinçli icra yönü bu biçime amaçlı yapma basıncı ekler; âyet eylemleri başka bir sınıfa ayırmaz, gramer kapsamı da her eylemin tek tek sayıldığını göstermez. Böylece hesap ayrı bir fiziksel defter ya da ek bir hüküm sonucu değil, yapılan işlerin kişilere bildirim yoluyla bağlanması olarak belirir.

İki “kim” kalıbı, 31:22 ile 31:23’ün bugünkü yönelişlerini yan yana getirir: {ar:وَمَن يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ, tr:wa-man yuslim wajhahu ilā Allāh, gloss:yüzünü Allah’a yönelterek teslim olan} ile {ar:وَمَن كَفَرَ, tr:wa-man kafara, gloss:kim inkâr ederse}. 31:22’de teslim olan kişi {ar:فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:fa-qadi-stamsaka bi-l-ʿurwati l-wuthqā, gloss:sağlam kulpa tutundu} diye anlatılır ve {ar:وَإِلَى ٱللَّهِ عَٰقِبَةُ ٱلْأُمُورِ, tr:wa-ilā Allāhi ʿāqibatu l-umūr, gloss:işlerin sonu Allah’a varır} sözüyle tamamlanır (31:22). Şimdiki teslimiyet ile inkâr yönelişleri ayrıdır; 31:22 yalnızca teslim olanların yolunu anlatıyor olabilir ve 31:23’teki örtme çağrışımı inkâr uyarısının yerini almaz. Bununla birlikte {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ortak son varış ufkunu Allah’a yöneltir; ayetlerin yakınlığı, farklı şimdiki yönelişlerden aynı ilahî varışa uzanan çizgiyi görünür kılar.

Dönüşün sonucu yokmuş gibi duyulmasını 31:24’teki sıra önler: önce {ar:مَتَٰعٌ قَلِيلٌ, tr:matāʿun qalīl, gloss:az bir yararlanma}, ardından {ar:ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍ, tr:thumma naḍṭarruhum ilā ʿadhābin ghalīẓ, gloss:sonra onları ağır azaba zorlarız} gelir (31:24). 31:24 dönüşün tam zamanını ya da mekanizmasını değil, dönüşten sonrasını anlatıyor da olabilir. Bu dizi, 31:23’teki {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} yanına konduğunda kısa bir mühletin ağır bir sonuca açılabileceğini düşündürür; keder yasağı bugünkü gecikmenin sonsuz olmadığını duyurur.

Bu bildirim ufkunda söylenen söz ile içteki tanıma da ayrışabilir. Gökleri ve yeri kimin yarattığı sorulunca “Allah” diyeceklerini belirten {ar:وَلَئِن سَأَلْتَهُم مَّنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:wa-la-in saʾaltahum man khalaqa as-samāwāti wa-l-arḍ, gloss:gökleri ve yeri kimin yarattığını sorarsan} ve {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāh, gloss:Allah diyecekler} sözlerinin ardından {ar:قُلِ ٱلْحَمْدُ لِلَّهِ, tr:quli l-ḥamdu li-llāh, gloss:de ki övgü Allah’a} denir; yine de “çoğu bilmez” ifadesi eklenir (31:25): {ar:بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ, tr:bal aktharuhum lā yaʿlamūn, gloss:çoğu bilmez}. Konuşanların niyeti ya da çoğunluğun tam olarak neyi bilmediği bu yan yanalıktan belirlenemez. Yine de 31:23’teki {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} ve Allah’ın {ar:عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ, tr:ʿalīmun bi-dhāti ṣ-ṣudūr, gloss:göğüslerde olanı bilen} oluşuyla birlikte düşünüldüğünde, söylenen doğru cevabın içten tanıma ve boyun eğişle her zaman örtüşmediği görünür.

Sahiplik ekiyle belirlenen inkâr ve çoğul dönüş, keder öğüdünü başka bir sorumluluk benzetmesine açar. Keder alanındaki ayrı bir isim kullanımı, durumu için kaygı duyulan aileyi ve yükümlülük doğuran yakınları adlandırabilir; âyetin taşıyıcısı ise bu isim değil, olağan anlamıyla muhatabı üzen {ar:يَحْزُنْكَ, tr:yaḥzunka, gloss:seni üzsün} fiilidir. Aile ve bağımlı yükü bu fiilin düz karşılığı değil, benzetmenin kaynağıdır. İkinci tekil hitap, sahibine bağlanan {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} ve çoğul {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ile temas ederek muhatabın başkasının hesabını bir yakınının yükü gibi taşımasından serbest kalabileceğini duyurur. Muhatapla reddeden grup dilbilgisel olarak ayrıdır; bu benzetme aile bağı ya da hukuk kuralı ileri sürmez ve kederi yükümlülük saymaz. Bu sınır içinde hitap, muhatabın başkasına duyduğu kaygı ile o kişinin hesabını taşıma yükünü birbirinden ayırır.

Bu sınırın yanında 31:15, şimdiki ilişkinin nasıl sürebileceğine dair özel bir ebeveyn-evlat örneği verir. Allah’a ortak koşmaya çağıran anne babaya {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:ikisine itaat etme} denirken hemen ardından {ar:وَصَاحِبْهُمَا فِي الدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī d-dunyā maʿrūfan, gloss:dünyada onlarla iyilikle yoldaşlık et} buyurulur; aynı ayette {ar:ثُمَّ إِلَيَّ مَرْجِعُكُمْ فَأُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ, tr:thumma ilayya marjiʿukum fa-unabbiʾukum bi-mā kuntum taʿmalūn, gloss:sonra dönüşünüz bana, yaptıklarınızı size bildiririm} dizisi gelir (31:15). 31:23’te de {ar:إِلَيْنَا, tr:ilaynā, gloss:bize} {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ve ardından {ar:فَنُنَبِّئُهُمْ بِمَا عَمِلُوا, tr:fa-nunabbiʾuhum bi-mā ʿamilū, gloss:yaptıklarını onlara bildiririz} gelir. Bu çıkarım ebeveyn-evlat örneğiyle sınırlıdır; her anlaşmazlığa yayılmaz. Yine de son hesabı Allah’a bırakmak bu özel ilişkide iyi beraberliği terk etmek değildir: yoldaşlık istenen inanca onay vermez, iyilikle davranışın sınırını korur ve bildirimi şimdi zorla kapanışa çevirmeden nihai hesabı erteler.

Yakınlığın hesap yerine geçmediği sınır 31:33’te daha kesin çizilir: ağır günde ne ebeveyn çocuğu adına ne çocuk ebeveyni adına bir şey ödeyebilir; ayrıca dünya hayatı ve aldatıcının Allah hakkında aldatmasına karşı uyarı gelir (31:33). Aynı kişisel sorumluluk, hiçbir yük taşıyanın başkasının yükünü taşımadığını söyleyen ilkeyle de belirginleşir (39:7): {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra uḫrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz}. 31:23’teki {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ve {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} dizisi, 39:7’deki {ar:مَرْجِعُكُمْ, tr:marjiʿukum, gloss:dönüşünüz} ile {ar:فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ, tr:fa-yunabbiʾukum bi-mā kuntum taʿmalūn, gloss:yaptıklarınızı size bildirir} biçiminde kişisel bağı görünür kılar: kişinin kendi bilerek yaptığı iş kendisine döner. Bildirim Allah’ın bilinmeyen bir soruya cevap vermesi ya da yeni bilgi edinmesi değildir; muhatabın kederi de suç veya vekâleten taşınan bir yük sayılmaz. Bu yan yanalık, yakınlığı başkasının hesabını üstlenmekten ayırır: herkes kendi dönüş ve hesabını taşırken başkası için keder duyabilir.

{ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:sonra bildiririz} bildirme fiilinin bilinen içeriği aktarması, önceden bilmeyi bildiren {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} niteliğinden ayrılır; Allah’ın bildirmesi yeni bilgi edinmesi değildir. Bu ayrım, yakın ayetlerdeki iki büyük görüntüyle başka ölçekte duyulur. Ağaçların kalem, denizin ardından yedi denizin daha mürekkep olduğu imgesi (31:27), Allah’ın sözlerinin tükenmediği hükmüne varır: {ar:مِن شَجَرَةٍ أَقْلَٰمٌۭ, tr:min shajaratin aqlām, gloss:ağaçtan kalemler}, {ar:وَالْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:wa-l-baḥru yamudduhu min baʿdihi sabʿatu abḥur, gloss:denizin ardından yedi deniz daha}, {ar:مَا نَفِدَتْ كَلِمَاتُ ٱللَّهِ, tr:mā nafidat kalimātu Allāh, gloss:Allah’ın sözleri tükenmez}. 31:28’de yaratma ve diriltme tek bir canla benzetilir: {ar:مَا خَلْقُكُمْ وَلَا بَعْثُكُمْ إِلَّا كَنَفْسٍۢ وَٰحِدَةٍ, tr:mā khalqukum wa-lā baʿthukum illā ka-nafsin wāḥidah, gloss:yaratılışınız ve diriltilmeniz tek bir can gibi}. Bu iki benzetme kişisel bildirimin gerekçesi olarak değil, ayrı iddialar olarak durur: 31:27 Allah’ın sözlerinin tükenmezliğini, 31:28 yaratma ve diriltme kudretini bildirir; tek can benzetmesi kolaylığı da vurguluyor olabilir. Yine de kalem-mürekkep çokluğu ile tek can ölçüsünün yan yana gelişi, çokluğun kişiye ait bildirim önünde engel olmadığını düşündürür.

Bu genişlikten ayrı bir zaman görüntüsü 31:29’da geceyle gündüzün birbirine girişi, güneş ve ayın belirlenmiş bir vadeye doğru akışı ve insanların yaptıklarıyla tamamlanır: {ar:يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ, tr:yūliju al-layla fī an-nahāri wa-yūliju an-nahāra fī al-layli, gloss:geceyi gündüze, gündüzü geceye sokar}, {ar:وَسَخَّرَ ٱلشَّمْسَ وَٱلْقَمَرَ, tr:wa-sakhkhara ash-shamsa wa-l-qamar, gloss:güneşi ve ayı buyruğa verdi}, {ar:كُلٌّۭ يَجْرِىٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:kullun yajrī ilā ajalin musamman, gloss:her biri belirlenmiş bir süreye akar}, {ar:بِمَا تَعْمَلُونَ, tr:bi-mā taʿmalūn, gloss:yaptıklarınızla} (31:29). Gizlenme-görünme evreleri, {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için “örtücü karanlık ya da enginlik” kullanımını da harekete geçirir; gece, deniz, büyük akarsu, gün batımı veya bulut bu örtücülük alanına girebilir. Bu keşifsel zaman benzetmesi, {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} fiilinin sözlük anlamını “gece”ye çevirmez; 31:29 gök cisimlerinin seyrini ayrıca anlatıyor olabilir, odağın muhatabını belirlemez ve hesap için takvim vermez. Bu sınırlar içinde inkâr ve {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri}, tek bir uzak kesintiden çok sınırlı bir gidişin gizlenme-görünme evreleri gibi okunabilir.

31:32 ise bu gök döngüsünden ayrı olarak denizdeki krizle karaya çıkış arasındaki hareketi gösterir. İnsanları gölgelikler gibi örten dalgaların baskısı altında Allah’a dini yalnız O’na has kılarak yakarırlar (31:32): {ar:غَشِيَهُم مَّوْجٌ, tr:ghashiyahum mawjun, gloss:bir dalga onları bürüdü}, {ar:كَٱلظُّلَلِ, tr:ka-ẓ-ẓulal, gloss:gölgelikler gibi}, {ar:دَعَوُا ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu d-dīn, gloss:dini yalnız O’na has kılarak Allah’a yakardılar}. Fiziksel örtü, {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için örtme çağrışımını somutlaştırırken kriz de açığa çıkan bağımlılığı gösterir; dalga sözcüğün kendisinin anlamı değildir. Kurtuluşla karaya çıkarılmaları anlık, {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ise son hesaba ilişkin varıştır (31:32). Karaya çıkanların bir bölümü ölçülü davranır; buna rağmen ayet, yadsımayı hainlik ve nankörlükle niteler (31:32): {ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā al-barr, gloss:onları karaya çıkardı}, {ar:فَمِنْهُم مُّقْتَصِدٌۭ, tr:fa-minhum muqtaṣid, gloss:aralarından ölçülü olanlar}, {ar:وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا كُلُّ خَتَّارٍۢ كَفُورٍۢ, tr:wa-mā yajḥadu bi-āyātinā illā kullu khattārin kafūr, gloss:ayetlerimizi ancak hain ve nankör olanlar yadsır}. Kurtuluştan sonra bilinçle yapılan bu davranışlar, 31:23’te {ar:بِمَا عَمِلُوا, tr:bi-mā ʿamilū, gloss:yaptıklarıyla} bildirilecek işlere somut içerik olabilir; herkesin niyetini tüketmez. Kriz duası geçici olabilir ve tek başına ihanet kanıtı değildir; bu kişiler de 31:23’teki muhataplarla özdeş ilan edilmez. Dalga ile sonraki davranış arasındaki değişim, örtülme ve açığa çıkmayı silinme yerine aynı hesap ufkunda izlenebilir kılar.

## Göğüslerde Olan ve İlahi Bilgi

Son cümledeki {ar:إِنَّ, tr:inna, gloss:şüphesiz}, vurgulu isim cümlesini açar; {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adı, dönüş ve bildirimde zaten görünen ilahî özneyi {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} niteliğine bağlayarak önceki akışı çerçeveler. Bu bilme dönüşün ya da bildirimin sebebi diye sunulmaz. Özel ad, bilgiyi soyut bir ilah etiketine değil, daha önce {ar:إِلَيْنَا, tr:ilaynā, gloss:bize} varışla, {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ve {ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:onlara bildiririz} eylemiyle görünen aynı özneye bağlar. Adın tapılmaya layık olma, sığınak olma ya da şaşma gibi köken açıklamaları ihtimal olarak kalır; hiçbiri özel adın yerine geçmez. {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} sözcüğünün faʿīl kalıbı yeni edinilmiş bir öğrenme olayından çok süreklilik taşıyan yoğun bilme niteliği verir; bu nitelik bilgi derecesini ölçmeden ve önceden bilgisizlik varsaymadan, dönüş ve bildirimde görünen öznenin bilgisini pekiştirir.

İlk {ar:بِمَا, tr:bi-mā, gloss:yaptıklarıyla} bildirilecek işleri içeriğe bağlarken kapanıştaki {ar:بِذَاتِ ٱلصُّدُورِ, tr:bi-dhāti ṣ-ṣudūr, gloss:göğüslerde olana} bilmenin alanını belirtir. Dışa vurulan eylem kaydıyla içte kalan alan yan yana durur; ikincisi {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} niteliğini yalnız o alana indirgemez. {ar:ذَاتِ ٱلصُّدُورِ, tr:dhāti ṣ-ṣudūr, gloss:göğüslere ait olan} tamlaması serbest bir nesne listesi değil, göğüslere ait olanı bir arada kuran yapıdır; ilk öğe aidiyet ve öz çağrışımlarını aynı alan içinde taşır, bağımsız bir benlik öğretisi kurmaz. Belirli çoğul göğüs sözü, dönüşü ve işleri bildirilen topluluğun iç alanını kapsar; çoğul kapsamı genişletir, herkesin iç dünyasını tek bir şey ilan etmez. Tamlamanın başındaki vurgulu ṣ sesi, saklı iç alanın işitilişine yerel bir ağırlık katar; bu vurgu burada ses imgesini derinleştirir, sözcüğün anlamını ya da genel bir ses yasasını değiştirmez.

{ar:ٱلصُّدُورِ, tr:al-ṣudūr, gloss:göğüsler}, olağan anlamıyla boynun altındaki gövdenin ön bölgesini adlandırır. Göğüslere ait olanı bildiren tamlama ve onları bilen {ar:عَلِيمٌۢ, tr:ʿalīmun, gloss:bilen} yüklemi bu bedensel sözü gizli iç hayatın taşıyıcısı olarak duyurur; göğüs sözü bedensel adını korur, içinde fiziksel nesneler sayılmaz. Aynı çoğul adın bir şeyin ortaya çıktığı yer ya da zamanı bildiren ayrı bir sözlük kullanımı da vardır. Bu kaynak çağrışımına burada üç ayrı unsur temas eder: {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptılar} ile eylemler, {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} ile bildirim, {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ile varış. Bu çağrışım kesin bir organı ya da niyeti tarif etmez ve insana saklı niyeti görme imkânı vermez. Böylece göğüslerin iç alanı, eylemlerin dışa çıkan gizli kaynağı gibi de duyulur; bedensel sözcüğün iç hayatı anlatması sürer, kaynak anlamı ise eylemlerin hesabına içten bir katman ekler.

Bu iç kaynak çağrışımını 29:10’daki baskı altındaki söz belirginleştirir: eziyet görenler {ar:ءَامَنَّا بِاللَّهِ, tr:āmannā bi-llāh, gloss:Allah’a inandık} der, sonra {ar:إِنَّا كُنَّا مَعَكُمْ, tr:innā kunnā maʿakum, gloss:biz de sizinleydik} diye kamusal söz söyler; hemen ardından Allah’ın insanların göğüslerindekini en iyi bilip bilmediği sorulur (29:10): {ar:أَوَلَيْسَ اللَّهُ بِأَعْلَمَ بِمَا فِي صُدُورِ الْعَالَمِينَ, tr:a-wa-laysa llāhu bi-aʿlama bimā fī ṣudūri l-ʿālamīn, gloss:Allah insanların göğüslerindekini en iyi bilen değil mi}. 31:20’de nimetlerin hem görünür hem gizli diye çiftlenmesi, dışarı söylenenle içte kalan arasındaki farkı başka bir yönden açar: Allah nimetlerini üzerlerine yaymış, onları {ar:ظَاهِرَةً وَبَاطِنَةً, tr:ẓāhiratan wa-bāṭinatan, gloss:görünen ve gizli} kılmıştır (31:20): {ar:أَسْبَغَ عَلَيْكُمْ نِعَمَهُ, tr:asbagha ʿalaykum niʿamahu, gloss:nimetlerini üzerinize yaydı}. Bu iki ayrı temas, 31:23’teki {ar:ٱلصُّدُورِ, tr:al-ṣudūr, gloss:göğüsler} sözünün bedenî anlamını ve {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptıkları} işlerin {ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:onlara bildiririz} ile Allah tarafından bildirilmesini yan yana tutar. Bu nimet alanı {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} ile silinmez; görünenle gizli olan, göğüsleri bilen ilahî hesabın iki yanında kalır. Bu bağlamlar insana saklı niyete erişim vermez; eylemin yalnız dış sonucunu değil, iç kaynağından oluşumunu da Allah’ın bilip bildirdiği okumasını güçlendirir.

Bu görünür nimet alanından sonra bilgisizce tartışma ve ataların izine uyma sözü gelir (31:20, 31:21). {ar:مَن يُجَادِلُ فِي اللَّهِ بِغَيْرِ عِلْمٍ, tr:man yujādilu fī llāhi bi-ghayri ʿilm, gloss:Allah hakkında bilgisizce tartışan} kişiye karşı {ar:بَلْ نَتَّبِعُ مَا وَجَدْنَا عَلَيْهِ آبَاءَنَا, tr:bal nattabiʿu mā wajadnā ʿalayhi ābāʾanā, gloss:atalarımızı üzerinde bulduğumuz şeye uyarız} denir. {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} için örtme, {ar:ٱلصُّدُورِ, tr:al-ṣudūr, gloss:göğüsler} için iç kaynak çağrışımı bu sözlerle birlikte duyulur. Tartışma, iç kaynağın üzerini örten bir dış söz olabilir; ataların izinden gitmek önceden alınmış toplumsal yolu taşır, atalara gönderme de bu yolun taşıyıcısını gösterir. Bu sözler kişinin {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptıkları} amelinin tümü ya da başkasının üstlendiği bir iş değildir. Bu okuma her tartışmayı örtü saymaz; atalara başvuru da tek başına gizli niyeti kanıtlamaz veya eyleyeni sorumluluktan çıkarmaz. Böylece olağan inkâr ve bedensel göğüs anlamları yerinde kalırken, kamusal ya da miras alınmış sözün altındaki iç kaynak hesapla ilişkilendirilir.

Küçük ve saklı bir işin bu hesaba erişmesi 31:16’daki hardal tanesiyle elle tutulur hâle gelir. Ağırlığı hardal tanesi kadar olan filiz taşıyan tane bir kayanın, göklerin ya da yerin içinde gizli kalsa da Allah onu getirir (31:16): {ar:مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ, tr:miṯqāla ḥabbatin min ḫardal, gloss:hardal tanesi ağırlığınca}, {ar:فِي صَخْرَةٍ أَوْ فِي السَّمَاوَاتِ أَوْ فِي الْأَرْضِ, tr:fī ṣaḫratin aw fī s-samāwāti aw fī l-arḍ, gloss:kayada, göklerde ya da yerde}, {ar:يَأْتِ بِهَا اللَّهُ, tr:yaʾti bihā llāhu, gloss:Allah onu getirir}. Bu gerçek tohum, 31:23’teki {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} örtme çağrışımıyla, {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptıkları} ile anlatılan amellerin {ar:فَنُنَبِّئُهُمْ, tr:fa-nunabbiʾuhum, gloss:onlara bildiririz} ile haber verilmesi ve {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} ile buluşunca, kaya gibi kapalı yerde kalan küçük bir işin dönüş ve bildirim hesabından silinmediğini gösterir; bilme pasif farkındalıkta kalmaz, gizli yerdekine erişir. 31:16’daki {ar:لَطِيفٌ, tr:laṭīf, gloss:ince ve gizliye erişen} niteliği ölçek ve örtünün altına ulaşma imgesini besler. Bu bağlantı bağlamsal kalır; 31:16 Allah’ın kudretini daha genel olarak da anlatır. Hardal tanesi imgesi böylece küçük ve gizli bir işin dönüşte bildirim hesabına erişmesini elle tutulur kılar.

Aynı küçük tane, örtme çağrışımının biçim sınırını da gösterir. Sözlük ailesindeki ayrı bir fail adı, tohumu toprağa yerleştirip üstünü örten çiftçiyi anlatabilir; bu anlam yalnız o fail adına aittir. 31:23’teki çekimli {ar:كَفَرَ, tr:kafara, gloss:inkâr etti} fiili ve sahiplik eki almış {ar:كُفْرُهُۥٓ, tr:kufruhu, gloss:onun inkârı} biçimi çiftçi diye çevrilmez, olağan reddediş anlamını taşır. Bildirme fiili filizlenmek anlamına dönüşmez; bu benzetme 31:16’daki genel kudret okumasını da kaldırmaz. Yine de 31:16’da yerde ya da kayada saklı kalan tohumun Allah tarafından ortaya çıkarılmasıyla 31:23’te {ar:عَمِلُوا, tr:ʿamilū, gloss:yaptıkları} amellerin {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri} sırasında {ar:نُنَبِّئُهُمْ, tr:nunabbiʾuhum, gloss:onlara bildiririz} diye bildirilmesi arasında sınırlı bir gömülme ve görünür hâle gelme benzetmesi kurulur: örtülmüş iş hesapta belirir.

Son olarak 31:34, insanın kendi geleceği hakkındaki sınırını ilahî bilginin yanına koyar. {ar:وَمَا تَدْرِى نَفْسٌ, tr:wa-mā tadrī nafsun, gloss:hiçbir özne bilemez} sözü iki kez yinelenir: kişi {ar:مَاذَا تَكْسِبُ غَدًا, tr:mādhā taksibu ghadan, gloss:yarın ne kazanacağını} ve {ar:بِأَىِّ أَرْضٍ تَمُوتُ, tr:bi-ayyi arḍin tamūtu, gloss:hangi yerde öleceğini} bilmez (31:34). Bu sınır, 31:23’teki {ar:مَرْجِعُهُمْ, tr:marjiʿuhum, gloss:dönüşleri}, {ar:فَنُنَبِّئُهُمْ بِمَا عَمِلُوا, tr:fa-nunabbiʾuhum bi-mā ʿamilū, gloss:yaptıklarını onlara bildireceğiz} ve {ar:عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ, tr:ʿalīmun bi-dhāti ṣ-ṣudūr, gloss:göğüslerde olanı bilen} vaadiyle karşılaşınca, hesabın kişinin kendi gelecek öngörüsünü aştığını ve yalnızca hatırladığı geçmişin tekrarı olmadığını düşündürür. 31:34’te sayılan bilinmezler bildirilecek eylemler hâline gelmez; 31:23’te göğüslerde olana ilişkin açık anlam sürer, iç kaynak çağrışımı ise nitelikli kalır. 31:34’ün başındaki ilahî bilgi ve kapanıştaki {ar:إِنَّ ٱللَّهَ عَلِيمٌ خَبِيرٌ, tr:inna Allāha ʿalīmun khabīr, gloss:Allah bilendir, haberdardır} bu farkı çerçeveler: kişinin kendi yarınına dair öngörüsünün ötesinde, ona ait ameller Allah’ın bildirimine konu olur.

</source_prose>
