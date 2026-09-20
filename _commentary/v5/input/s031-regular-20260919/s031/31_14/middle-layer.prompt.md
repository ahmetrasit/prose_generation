# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:14**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.middle.claims.json`

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
- Refer to source paragraphs as `31:14 ¶N`.

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

`(31:14 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:14",
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
        "citation": "(31:14 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_14/31_14.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_14/31_14.middle.claims.json \
  --ayah-ref 31:14
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_14/31_14.prose.editorial.tr.md`

<source_prose>
## Sözün Bağı ve Muhatabı

31:14'te insan, Allah'a ve {ar:وَٰلِدَيْكَ, tr:wālidayka, gloss:anne babana} şükretmeye çağrılır; bu emrin içeriği açıklanmadan önce annenin {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} eylemi, {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnan ʿalā wahnin, gloss:güçsüzlük üstüne güçsüzlük} ve {ar:فِصَالُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi} anlatılır. Sütten kesilme {ar:عَامَيْنِ, tr:ʿāmayni, gloss:iki yıl} içindedir; ancak bu uzun kanıttan sonra {ar:أَنِ, tr:ani, gloss:şunu} ile buyruk yeniden açılıp {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} denir. Sonda {ar:إِلَىَّ, tr:ilayya, gloss:bana doğru} yönüyle {ar:ٱلْمَصِيرُ, tr:al-maṣīru, gloss:dönüş} son varışı adlandırır. Böylece anneye ait bakım, emrin arasına sıkıştırılmış bir yan bilgi değil, muhatabın neye karşılık vereceğini görünür kılan cümlenin parçası olur.

Ayetin başındaki {ar:وَ, tr:wa, gloss:ve}, yazıda hemen ardından gelen {ar:وَصَّيْنَا, tr:waṣṣaynā, gloss:yükümlü kıldık} fiiline bitişir. Bu eklemleniş, Luqman'ın öğüdünden (31:13) ebeveyn sorumluluğunu bildiren ilahî söze geçerken hem sürekliliği hem yeni bir beyanın açılışını taşır. Bağlacın ve fiilin başındaki iki /w/ ile fiildeki şeddeli ṣ, bu başlangıca işitsel bir vurgu verebilir; bu, yazılı biçimden çıkarılan bir izlenimdir, ölçülmüş bir tilavet etkisi değildir.

Fiildeki şeddeli kalıp ve içine aldığı ilahî özne, yükümlülüğün kaynağını baştan belirginleştirir. {ar:وَصَّيْنَا, tr:waṣṣaynā, gloss:yükümlü kıldık} önce {ar:ٱلْإِنسَٰنَ, tr:al-insāna, gloss:insanı} yükümlü kılar; anneye ait kanıt araya girdikten sonra gelen {ar:أَنِ, tr:ani, gloss:şunu} ise yükümlülüğün içeriğini şükür emrine bağlar. Böylece buyruğu veren, yükümlülüğü alan ve emrin içeriği cümlede ayrı ayrı seçilir. Öğütleme ya da yükümlü kılma alanındaki fiil burada ciddi bir ilahî yönergeyi bildirir. Aynı kelime ailesindeki bağlama ve bitiştirme kullanımı, bağımsız {ar:بِ, tr:bi, gloss:hakkında} edatı ve ebeveyn çiftiyle temas ederek insanı ebeveynlerine karşı bir yükümlülüğe bağlanmış gibi duyurur; bu bağ imgesi olağan buyruk anlamını taşımayı sürdürür. Fiilin başkasına talimat bırakma, vasiyet etme kullanımı da {ar:أَنِ, tr:ani, gloss:şunu} ve emirle etkinleşir: burada talimat şükürdür; bu okuma, ölümle ilgili bir vasiyet değil, başkasına bırakılan bir yönerge imgesidir. Anneye ait bedenî kanıt gelmeden kurulan yükümlülük ebeveyn hakkını baştan bağlayıcı bir çerçeveye alır; şeddeli ṣ'nin sıkı vurgusu da biçimden duyulabilecek ihtiyatlı bir sestir.

Yükümlülüğü alan {ar:ٱلْإِنسَٰنَ, tr:al-insāna, gloss:insanı}, belirli tekil biçimiyle yalnız Luqman'ın oğlunu değil insan türünü genel bir sınıf olarak öne çıkarır. Ebeveynler yükümlülüğün konusudur; onu yerine getirmesi istenen ise insandır. İnsan sözcüğünün yakınlık, tanışıklık ve algıyla ilişkili çağrışımları, ebeveyn bağı içindeki borcu fark etme düşüncesini açar; burada odak bir unutma olayı değil, ilişkinin ve sorumluluğun tanınmasıdır. Yükümlülüğe bitişen {ar:بِ, tr:bi, gloss:hakkında} de ebeveynleri doğrudan nesne değil, insanın hangi konuda yükümlü kılındığını belirten unsur yapar ve söz diziminde hemen {ar:وَٰلِدَيْهِ, tr:wālidayhi, gloss:iki ebeveyni}ni yönetir. Bu ikil biçim doğumla bağlı iki biyolojik ebeveyni birlikte adlandırır; ebeveyn adının tekil kullanımı erkek ebeveyni, yani babayı da belirtebildiğinden çift ve gebelik kanıtı babayı da bu doğum bağı içinde tutar. Edatın geniş alanında nedensel bir tını duyulabilse de buradaki temel işi ebeveynleri yükümlülüğün konusu yapmaktır. Açıkça anılacak anne, bu ikil adı tüketmez; çift babayı da kapsarken taşıma eylemi özellikle anneye verilir.

## Taşınan Beden ve Ölçülen Süre

Taşıma cümleye bir eylem ve onu yapanı birlikte getirir: dişil tekil {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} biçimi insanı taşınan kişi olarak gösterir, ardından {ar:أُمُّهُۥ, tr:ummuhu, gloss:annesi} taşıyanı açıkça adlandırır. Taşıma fiilinin yük altında dayanmayı anlatan başka kullanımları da vardır; anne ve arkasından gelen {ar:وَهْنًا, tr:wahnan, gloss:zayıflıkla} bu sahnedeki anlamı gebeliğin bedenî taşımasına sınırlar. Meyve ya da emanet yükü imgeleri burada taşımanın ana okuması değildir; başka bağlamlar onları benzetme olarak çağırabilir. “Anne” adının bağlı olduğu sözlük alanındaki başlangıç ve varlık kaynağı çağrışımı, {ar:وَٰلِدَيْهِ, tr:wālidayhi, gloss:iki ebeveyni}nin doğum bağıyla birleşince anneyi insanî başlangıç çizgisinde yakın bir kaynak gibi gösterir; bu yakınlık onu nihai kaynak yapmaz. Taşıma ile güçsüzlüğün yazıdaki yakınlığı da bir ses çizgisi kurabilir; bu, ölçülmüş akustik sonuç değil metin yüzeyinden edinilen bir izlenimdir.

İlk {ar:وَهْنًا, tr:wahnan, gloss:zayıflıkla} belirsiz biçimiyle taşıma eylemini bir güçsüzlük hâli içinde niteler. Hemen arkasındaki {ar:عَلَىٰ, tr:ʿalā, gloss:üzerine} ve ikinci {ar:وَهْنٍۢ, tr:wahnin, gloss:zayıflık}, bu hâlin üzerine bir katman daha koyar: edatın mekânsal yönü, bir güçsüzlüğün ötekinin üstüne binmesi imgesini taşır. İkinci adın edatın altına bağlanan biçimi katmanları kurar, ama miktarını belirlemez; iki ayrı tanıdan çok birbirine eklenen bedensel yükler duyulur. Az kullanılan sözcüğün kısa öbekte yinelenmesi annenin kırılganlığını yoğunlaştırabilir; yinelenen ünsüzler de bu çizgiyi sesçe örebilir. Uzun ā'lı edat iki katman arasında eşik gibi hissedilebilir. Bu biçim izlenimleri ne ölçülmüş bir okuyuşu ne de tıbbî bir teşhisi bildirir.

Önceki dizinin başına eklenen ikinci {ar:وَ, tr:wa, gloss:ve}, {ar:فِصَالُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi}ni taşıma ve güçsüzlüğe bağlayarak anneye ilişkin kanıta ikinci biyolojik olguyu ekler. Kelime, anneden ve emme ilişkisinden ayrılma sürecini adlandırır; kesme, ayırma ve ayırt etme alanındaki başka kullanımları da bu bakım aşamasının sınırını belirginleştirir. Okuma varyantları ayrılma vurgusunu keskinleştirirken temel okuma sütten kesilme sürecini korur. Bu geçiş emme ilişkisinden ayrılmayı anlatır; akrabalık ve sevgi bağı sürer. Bağlaçtan isim öbeğine uzanan yazılı akış, sütten kesilmeyi önceki kanıtın devamı gibi duyurur; iki yıllık ölçüyle uzayan sesler de süreç ile süre arasında ihtiyatlı bir ritim yankısı kurabilir.

Kısa {ar:فِى, tr:fī, gloss:içinde} öbeği sütten kesilmeyi zaman çerçevesine yerleştirir: fiilsiz ama tamamlanmış ad cümlesi, “onun sütten kesilmesi iki yıl içindedir” der. Edatın geniş kullanımları arasından burada süreyi kapsayan zamansal değer öne çıkar. {ar:عَامَيْنِ, tr:ʿāmayni, gloss:iki yıl} belirsiz bir dönem değil, ikil biçimiyle tam iki yıllık ölçüdür; bir kışla bir yazı içine alan yıl çevrimi böylece iki tam döngü halinde hissedilir. Bu ölçü anneye ilişkin sahnenin süresini belirler ve bütün çocuklar için evrensel gelişim kuralı ya da hukukî hüküm kurmaz. Sürenin kapanışı, biraz sonra açıklanacak emir için uzun bir ara oluşturur.

Uzun anne anlatısının ardından {ar:أَنِ, tr:ani, gloss:şunu} baştaki yükümlülüğe döner ve onun ne istediğini açıklar: {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret}. Parçacık, taşıma, katman katman gelen güçsüzlük ve iki yıllık sütten kesilme boyunca ertelenmiş emir içeriğini açar. Varyant okumalardaki seslendirme farkları emirden hemen önce bir kıraat basıncı yaratabilir; parçacığın açıklayıcı bağı ise yerinde kalır. Tekil emir muhataba yönelir. Şükür yalnızca duygu değil, alınan iyiliği ve onun kaynağını tanıyan bir yanıttır; bakım dizisi bu tanımanın neye yöneldiğini somutlaştırır.

## Şükürden Son Varışa

Emrin ilk alıcısı {ar:لِى, tr:lī, gloss:bana} ile, birinci tekil kişi eki sayesinde ilahî konuşana yöneltilir; bu yön, cümlenin sonundaki {ar:إِلَىَّ, tr:ilayya, gloss:bana doğru} ile de yankılanır. Ardından gelen {ar:وَ, tr:wa, gloss:ve}, ayrı bir {ar:لِ, tr:li, gloss:için} edatının yönettiği {ar:وَٰلِدَيْكَ, tr:wālidayka, gloss:anne babana} öbeğini ekler. Tekrarlanan edatlar iki alıcıyı dengeli ama ayrı biçimde işaretler: ebeveynlere şükür de buyruğun içindedir, Allah ile ebeveynler ise ayrı kaynak ve rollerde kalır. Başlangıçtaki genel insan böylece doğrudan “senin anne baban” diye hitap edilen kişiye yaklaşır; ilk ebeveyn adı {ar:وَٰلِدَيْهِ, tr:wālidayhi, gloss:iki ebeveyni} iken buradaki {ar:وَٰلِدَيْكَ, tr:wālidayka, gloss:anne babana} biçiminde -hi'den -ka'ya geçiş aynı çifti yakına getirir. Bu biçimsel yankı yazılı-sesli dizilişten çıkarılır, belirli bir okuyuş kaydı değildir. İki ebeveyn birlikte anılırken taşıma eylemi yalnız anneye ait kalır. Bir zamanlar annesinin taşıdığı kişinin şimdi buyruğu alması, taşıma fiilini ahlaki sorumluluğu üstlenme benzetmesine açar; bu, sözcüğün anlamını değiştirmeyen bağlamsal bir imgedir. Taşıma ve sütten kesme, bakımın iki ayrı kanıtı olarak şükrü alınan iyiliği ve kaynağını tanımaya derinlik katar; böylece şükür geri ödeme zorunluluğuna indirgenmez ve yalnız ebeveynlere yönelmez.

Kapanışta öne alınan {ar:إِلَىَّ, tr:ilayya, gloss:bana doğru}, sonda gelen {ar:ٱلْمَصِيرُ, tr:al-maṣīru, gloss:dönüş} ile tamamlanır. Fiilsiz cümlede yön öne alınmış yüklem, sonda gelen belirli ve merfû isim ise gecikmiş özne olarak son varışı adlandırır; dönüş tahmin edilen bir hareket değil, sabit bir sonuç olarak bildirilir. {ar:ٱلْمَصِيرُ, tr:al-maṣīru, gloss:dönüş} olağan dönüş ya da varış anlamını korurken hâle gelme ve sonuca ulaşma kullanımlarının ufkunu da taşır. Anne ve ebeveyn adlarının açtığı insanî başlangıç çizgisi böylece ilahî konuşana yönelir; bakım cümlenin merkezinde kalır, insanî kaynak ile son varış da ayrı düzlemlerde anlaşılır. Kelimenin ayrı bir varış yeri ya da konak anlamı, {ar:إِلَىَّ, tr:ilayya, gloss:bana doğru} ve önceki anne-kaynak sahnesiyle birleşince eve doğru yerleşme benzetmesini de açabilir. Bu benzetme, ilahî konuşana fiziksel mekân niteliği yüklemeden dönüşün yerleşme hissini duyurur. Cümle sonundaki belirli isim, hareketli dizinin ardından yerleşik bir kapanış hissi verebilir; bu, ölçülmüş ses değil biçimden çıkan bir izlenimdir.

## Merhametin Beden Ölçeği

Sûrenin başındaki {ar:الرَّحْمَٰنِ الرَّحِيمِ, tr:ar-Raḥmān ar-Raḥīm, gloss:Rahmân ve Rahîm} ifadesi (31:0) genel bir merhamet çerçevesi açar; annenin {ar:أُمُّهُۥ, tr:ummuhu, gloss:annesi} diye adlandırılması ve taşıma eylemi ise bu çerçeveyi insan ölçeğinde bedenî bakıma yaklaştırır (31:14). Böylece gebeliğin görünmeyen emeği somutlaşır. Allah'a şükür çağrısı {ar:أَنِ ٱشْكُرْ لِلَّهِ, tr:ani ushkur lillāh, gloss:Allah'a şükret} (31:12) da {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnan ʿalā wahnin, gloss:güçsüzlük üstüne güçsüzlük}i bakımın bedensel bedeli, şükrü ise yaşanmış bir iyiliğe yönelen yanıt olarak görmeye imkân verir. Bu, 31:0'ın anne bakımını doğrudan saydığı anlamına gelmez; merhamet çerçevesi genel kalırken 31:14'teki bedenî sahne ona somut bir insanî ölçek kazandırır.

Nimetler hem {ar:ظَٰهِرَةًۭ وَبَاطِنَةًۭ, tr:ẓāhiratan wa-bāṭinah, gloss:açık ve gizli} yönleriyle anılır hem de {ar:نِعَمَهُۥ, tr:niʿamahu, gloss:O'nun nimetleri} diye adlandırılır (31:20). Oradaki {ar:وَبَاطِنَةًۭ, tr:wa-bāṭinatan, gloss:gizli ve içte olan}, {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} ile anlatılan gebeliği gizli bir bakım evresi gibi düşündürebilir; ardından gelen {ar:فِصَالُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi} bu gizliliğin arkasından görünürleşen başka bir bakım aşamasıdır (31:14, 31:20). Nimetlerin kuşatıcı biçimde verilişini çağrıştıran {ar:وَأَسْبَغَ, tr:wa-asbagha, gloss:ve bolca verdi} de bu iki evreyi genel nimetin somut bir örneği olarak duyurur (31:20). Allah'a ve ebeveynlere ayrı ayrı yönelen şükür, böylece her iki bakım evresine de yanıt olur. Bu eşleme anne bakımını 31:20'nin doğrudan konusu yapmaz; oradaki nimetler geneldir ve gebelikle sütten kesme nimetlerin tümünü tüketmez.

Hidayet ve {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}ten söz edilen bağlamın yanına konduğunda (31:3), {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} fiilinin gebe bir kadının gelişen çocuğu rahminde taşımasını anlatan ayrı kullanımı, rahmeti insan hayatına ulaşan somut bakım gibi duyurabilir. Bu okuma 31:3'ün ebeveyn bakımını ayrıca açıkladığını ileri sürmez; rahim, 31:14'te doğrulanmış yeni bir anlam değil, fiilin ayrı gebelik kullanımının çağrışımıdır. Aynı bedenî sahnede {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnan ʿalā wahnin, gloss:güçsüzlük üstüne güçsüzlük} için doğum sonrası rahim ağrısı da olası bir yankıdır; temel anlam yine bedensel güçsüzlüktür. Sözcüğün boynun iki yanı, üst kol ya da omuz başı çevresindeki bir ağrı veya hastalığı anlatan daha özel bir kullanımı da, tekrarlanan güçsüzlük ve çevresindeki bedenî bağlamla çağrışabilir. Bu ayrı dal ek bir ağrı imgesi sunar; 31:14 bölgeyi belirtmediğinden yeri teşhis etmez.

## Bakımın Büyüme Yankısı

Bakım, 31:14'te şükür buyruğundan önce gelir. Şükredenin yararının kendisine döndüğünü bildiren {ar:يَشْكُرْ, tr:yashkur, gloss:şükreder} ile yağmurdan sonra bitkilerin yetişmesini anlatan {ar:فَأَنۢبَتْنَا, tr:fa-anbatnā, gloss:yetiştirdik} ayrı bağlamlarda yer alır (31:12, 31:10). Birincisi şükrün yararını kişiye döndürür, ikincisi yağmurla gelen büyümeyi gösterir; bu iki çizgi yan yana bakımın gelişime katkısını ve şükredenin kendisinin de biçimlenmesini düşündürür. {ar:أُمُّهُۥ, tr:ummuhu, gloss:annesi} olağan anlamıyla anne adıdır; besleyip büyütme kullanımı da {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} ve {ar:فِصَالُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi}nin kurduğu sahnede bakımın gelişen çocuk için maddi kaynak oluşunu görünür kılar. {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} alınan iyiliği ve kimden geldiğini tanımayı sürdürür; şükredenin yararının kendisine dönmesi de bu yanıtın insanı biçimlendiren yönünü ekler (31:12).

Şükretme sözcüğünün az bir girdiyi yeterli bulup onunla gelişmeyi anlatan ayrı kullanımı, şükredenin yararının kendisine dönmesiyle (31:12) ve 31:14'teki beslenme-sütten kesilme ilişkisiyle benzetmeli bir beslenme çizgisi açar. Ayet belirli bir az miktar vermez. Aynı sözlük alanındaki doluluk ve ürünün bollaşması kullanımı memenin sütle dolmasını da düşündürür; anne, taşıma ve sütten kesilme bu bedensel sağlama imgesini birbirinden bağımsız biçimde çağırır. Bu kollar şükrü alınan besinin gelişime dönüşmesiyle genişletir; süt ayette açıkça adlandırılmaz ve çocuğun şükrü gerçek süt üretimi olarak anlatılmaz. Böylece beslenme yankısı, iyiliği ve kaynağını tanıma anlamını zenginleştirir.

Şükür sözcüğüne bağlanan bir başka kullanım gövde ya da dipten çıkan körpe sürgündür. {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} ile taşınan çocuk ve {ar:فِصَالُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi} ile belirginleşen gelişim geçişi bu dalı ayrı ayrı tetikleyerek bakım içinden yeni büyümenin filizlenmesi görüntüsünü kurar. Sözcük alanındaki taze saç, ince tüy ve küçük çocuk benzetmeleri bu filizlenme imgesini genişletir; şükür, böylece bakım içinden büyüyen bir yanıt gibi duyulur. Çocuk bitkiyle özdeşleşmez ve bu görüntü ölçülmüş bir gelişim sonucu bildirmez; 31:14'te bitkiden söz edilmediğinden bitki imgesi ayrı bir yankı olarak kalır. Bitkilerin yağmurdan sonra yetişmesi bu dala bağımsız bağlam sağlar (31:10). Sütten kesmenin hemen ardından gelen şükür, buyruğu somut bakım ve gelişim geçişinin içine yerleştirir; şükrün tamamı yalnızca bu ayrılıktan kaynaklanmaz.

## Sütten Kesmenin Sınırı

Sütten kesmeyi adlandıran {ar:فِصَٰلُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi}nin ayırma ve sınır açma çağrışımı, anne babayla ilişkinin sürdüğü sırada belirli bir aile gerilimini aydınlatabilir (31:15). Anne babanın {ar:جَٰهَدَاكَ, tr:jāhadāka, gloss:sana baskı kurmak için çabalarlarsa} diye anlatılan çabası, hakkında bilgi bulunmayan bir şeyi Allah'a ortak koşma talebi üzerindedir: {ar:تُشْرِكَ بِى مَا لَيْسَ لَكَ بِهِۦ عِلْمٌۭ, tr:tushrika bī mā laysa laka bihi ʿilm, gloss:hakkında bilgin olmayanı bana ortak koşman}. Buna {ar:فَلَا تُطِعْهُمَا, tr:falā tuṭiʿhumā, gloss:ikisine itaat etme} buyruğu karşılık verir; aynı yerde {ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًۭا, tr:wa-ṣāḥibhumā fī d-dunyā maʿrūfan, gloss:dünyada onlarla iyi geçin} denerek beraberlik sürdürülür. {ar:مَعْرُوفًۭا, tr:maʿrūfan, gloss:uygun ve iyi sayılan}, ilişki içinde tanınan ve doğru kabul edilen iyiliğe uygun davranışın ölçüsünü verir. Ardından {ar:وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ إِلَىَّ, tr:wa-ttabiʿ sabīla man anāba ilayya, gloss:bana yönelen kişinin yolunu izle} çağrısı baskıdan ayrı bir rehberlik yolu açar. Bu sahnede sütten kesilmenin ayrılık imgesi, şükür ve iyi beraberlik korunurken dinî baskıya karşı sınırı belirginleştirir. Sınır özellikle 31:15'teki şirk talebine ilişkindir: bedenî ayrılık itaatsizlik ya da yetişkinliğe geçişin nedeni diye sunulmaz ve bu özel reddi her ebeveyn isteğine yaymaz. Merhamet ve Allah'a şükür ebeveyne minneti hazırlar (31:0, 31:12); 31:15 ise minnetin şirk baskısına boyun eğmek olmadığını aynı ilişki içinde gösterir.

## Kişisel Hesap ve Açık Gelecek

Ebeveyn ile evladın rolleri ters yönlerde yeniden adlandırılırken, {ar:يَجْزِي, tr:yajzī, gloss:karşılığını verir} fiili birinin ötekinin yerine karşılık veremeyeceğini bildirir (31:33). 31:14'teki {ar:وَٰلِدَيْكَ, tr:wālidayka, gloss:anne babana}, öz anneyle öz babayı tek aile bağı içinde iki kişi olarak tutar; iki ebeveyn terimini eşanlamlı yapmaz. {ar:أُمُّهُۥ, tr:ummuhu, gloss:annesi} ve taşıma sahnesi annenin bakımını özellikle görünür kılar, babaya ise annesinin taşıma eylemini yüklemez. Böylece gerçek bakım ve ona yönelen şükür korunurken, 31:33 her kişinin kendi hesabını başkasının yerine üstlenilemeyecek biçimde ayırır. Sütten kesilme ayrılığı bu kişisel sorumluluk eşiğini düşündürebilir; burada belirli bir gelişim takvimi kurulmaz.

Karşılık verme fiiline kesme ve olgunlaşma imgeleriyle bağlanan ayrı kullanım, sütten kesilme ile iki yıllık ölçünün yanında kesme-hesap arasında olası bir yankı açar (31:14, 31:33). Özellikle kesme yönündeki biçim bağlantısı uzak ve tartışmalıdır; bu bağlantıda kesme ve olgunlaşma, fiilin “karşılığını verir” sözlük anlamını değiştirmeden bağlılık ve sorumluluk sınırına ihtiyatlı bir çağrışım ekler.

Rahimlerde olan, yarının kazancı ve ölüm insanların bilmedikleri arasında sayılır (31:34). {ar:مَا فِي ٱلْأَرْحَامِ, tr:mā fī l-arḥāmi, gloss:rahimlerde olan} sözü, 31:14'te annenin taşımasıyla başlayan bakımın başlangıcını, insan denetiminin bütünüyle kuşatmadığı gizli bir bedensel sürece açar. Bu okuma, rahimlerde olana ilişkin ifadeyle {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} arasında bağlamsal bir yankı kurar; fiilin sözlük anlamını değiştirmez ve ebeveynlerin her gebelikte ne bildiğine ilişkin iddia taşımaz (31:34). Aynı bilinmeyen ufuk iki yıllık bakım ölçüsünün ötesindeki yarına ve son varışa uzanır (31:34). Tam iki yıllık süre, {ar:ٱلْمَصِيرُ, tr:al-maṣīru, gloss:dönüş} ile bildirilen son varışla yan yana geldiğinde, yaşamın tamamı değil geleceği açık bir hayat içindeki sınırlı emanet gibi görünür (31:34). Bakım önemini korur, fakat ebeveyne çocuğun geleceği üzerinde sahiplik vermez; bu ilişki hukukî sonuç ya da belirli bir gelecek tahmini kurmaz.

Sağlam kulpa tutunan kişi ve işlerin sonu ufku birlikte belirir (31:22): {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:sıkıca tutundu}, {ar:ٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:al-ʿurwati l-wuthqā, gloss:sağlam kulpa}ya tutunmayı; {ar:عَٰقِبَةُ ٱلْأُمُورِ, tr:ʿāqibatu l-umūr, gloss:işlerin sonu} ise sonuca yönelmeyi adlandırır. Bu etkin tutunmanın yanında, bir zamanlar {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı} ile taşınan çocuk sonradan tutunan özne gibi düşünülebilir. {ar:فِصَٰلُهُۥ, tr:fiṣāluhu, gloss:sütten kesilmesi}nin ayrı bir kullanımı beden üyelerinin ya da kemiklerin birleştiği anatomik eklem noktasıdır. 31:22'deki sağlam bağ, bu eklem görüntüsünü bedensel ayrılık ile seçilmiş bağlılık arasında benzetmeli bir buluşma noktası yapar. Bu anatomik dal, sütten kesilme anlamını değiştirmez; taşıma ile tutunma arasındaki ilişki de sözlük açıklaması değil, iki sahne arasında bağlamsal bir benzetmedir. Görüntü bakım sonrasında bağın etkin biçimde seçilebileceğini düşündürür; bu yankı çocuğu 31:22'deki kişiyle özdeşleştirmez ve açık bir kronoloji kurmaz.

Seçilmiş sağlam bağ ile bilinmeyen yarın, kazanç ve ölüm ufku yan yana geldiğinde, sütten kesilme bedenî bakımdan hesap verebilir bir seçime olası geçiş gibi duyulabilir (31:22, 31:34). Bir sahne seçilen ilişkiyi, öteki sonucu açık kalan geleceği taşır; bu bağımsız görüntüler bakım sonrasındaki yönelişi düşündürür. Bu bağlantı olasılık düzeyindedir: çocuğun geleceğini ya da 31:22'deki aktörün kimliğini belirlemez, açık bir zaman çizelgesi de kurmaz.

## Bakımın Geçidi

Aynı kelime ailesinin yüzme ve suda ilerleme için kullanılan ayrı dalı, denizde yol alan {ar:الْفُلْكَ, tr:al-fulka, gloss:gemi} ile buluşunca iki yıllık {ar:عَامَيْنِ, tr:ʿāmayni, gloss:iki yıl} takvimini içinden geçilen bir ortam gibi duyurabilir (31:31). Bu dal geminin yanı sıra deve ve yıldızların yüzmeye benzer akıcı ilerleyişini de kapsar; yılın takvim anlamı korunurken bakım süresi hareketli bir geçit imgesine açılır.

Gebelikte çocuğu taşıyan {ar:حَمَلَتْهُ, tr:ḥamalat-hu, gloss:onu taşıdı}, başka bir kullanımında yükü kaldırıp bir taşıt üzerinde götürmeyi anlatır. Denizde ilerleyen gemi bu ikinci taşıma dalını tetikler; selin bir şeyi sürüklemesi ve bir taşıtın içindekileri götürmesi gibi başka kullanımlar da taşıyıp ilerletme görüntüsünü genişletir (31:31). Böylece annenin bedenî taşımasıyla yolcuları taşıyan gemi arasında ortak bir taşıma işlemi görünür, fakat benzetme çocuğu gerçek bir gemi yolcusu yapmaz. Gemi sözcüğünün olağan anlamı geçit sahnesini kurar; gebelik, iki yıl ve sütten kesilmeyle bağı anlam özdeşliği değil, bu sahneler arasındaki bağlamsal benzetmedir. Aynı sahnedeki {ar:تَجْرِي, tr:tajrī, gloss:akar ve ilerler}, geminin denizde akıp gidişini bildirir (31:31); bu hareket bakım aralığını sabit bir kap yerine içinden geçilen güzergâh gibi duyurabilir. Bu güzergâh okuması biçim bakımından ihtiyatlıdır.

İnsanları örtüler gibi yükselerek kuşatan {ar:مَوْجٌ, tr:mawjun, gloss:dalga}, ardından gelen {ar:نَجَّىٰهُمْ, tr:najjāhum, gloss:onları kurtardı} ile kurtulma ve karaya çıkma hareketi kazanır (31:32). {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnan ʿalā wahnin, gloss:güçsüzlük üstüne güçsüzlük} bedensel güçsüzlük anlamını korurken dalgalar bu katmanlı yükün taşınan bedenin üstündeki çalkantı gibi duyulmasına izin verir. Sütten kesmenin emme ilişkisinden ayrılma çizgisi ile dalgaların ardından zemine varış çizgisi yan yana düşünülebilir; bu yan yanalık birini ötekinin nedeni yapmaz, iki imge arasında benzetme kurar. {ar:الْبَرِّ, tr:al-barri, gloss:kara} (31:32) olağan anlamıyla kıyıdaki karadır. Evlatlık-iyilik kullanımı ayrı bir sözlük dalı olarak kendi bağlamlarında geçerliliğini korur; kıyı anlamıyla bu bağlantısı kesin olmadığından burada yalnızca varışta ebeveyn bağını hatırlatan ihtiyatlı bir yankı kurar.

Yolcu sabırlı ve {ar:شَكُورٍ, tr:shakūrin, gloss:çokça şükreden} diye nitelenir (31:31); kurtuluştan sonra nankörlük de görülebilir (31:32). Şükredenle nankörün bu farklı sonuçları, kıyıya varışın şükrü kendiliğinden güvence altına almadığını gösterir. Taşıyan gemi bakımın yükünü, akıp giden hareket sürenin güzergâhını, dalgalar bedenin üstündeki çalkantıyı, kurtuluş ve kara ise kuşatılmadan çıkış yönünü verir. Bu işlemler birleşince bakım süresi aşılmış bir yol, sütten kesilme de kıyıya eriş gibi duyulur. Bu ilişki benzetme düzeyindedir: 31:14'teki bakım sahnesi deniz yolculuğuna ya da gerçek bir gelişim anlatısına dönüşmez.

## Gecenin Ritmi

Son zamansal yankıda {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnan ʿalā wahnin, gloss:güçsüzlük üstüne güçsüzlük} bedenî güçsüzlük olarak kalır; iki yıllık {ar:عَامَيْنِ, tr:ʿāmayni, gloss:iki yıl} sürenin içine {ar:ٱلَّيْلَ, tr:al-layla, gloss:gece} ile {ar:ٱلنَّهَارَ, tr:an-nahāra, gloss:gündüz} döngüsü yerleştiğinde bakımın yinelenen geceleri de düşünülebilir (31:29). Her biri bir kışla bir yazı kapsayan yıl çevrimi, gece-gündüz tekrarını uzun bakım süresine taşır; katman katman gelen güçsüzlükle buluşması bakımın ritmini duyurur. Güçsüzlük sözcüğünün biçimce uzak bir başka kullanımı gecenin ortasına ya da çekilmeye başladığı vakte denk gelen belirli bir saati anlatır; gece-gündüz döngüsüyle temas eden bu kullanım zaman yankısını genişletirken bedenî güçsüzlük anlamını korur (31:29). Göksel düzen böylece bakım gecelerinin yinelenen ritmini düşündürür; annenin gecelerine ilişkin kesin bir anlatı kurmaz.

</source_prose>
