# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:10**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.middle.claims.json`

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
- Refer to source paragraphs as `17:10 ¶N`.

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

`(17:10 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:10",
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
        "citation": "(17:10 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_10/17_10.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_10/17_10.middle.claims.json \
  --ayah-ref 17:10
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_10/17_10.prose.editorial.tr.md`

<source_prose>
17:10, ahirete inanmayan bir grubu ve bu grup için hazırlanmış acı verici karşılığı aynı duyuruda birleştirir: {ar:لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:lā yuʾminūna bi-l-ākhirati, gloss:ahirete inanmazlar} diye nitelenenlere {ar:أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًا, tr:aʿtadnā lahum ʿadhāban alīman, gloss:onlara acı veren bir azap hazırladık} denir. Böylece bildirim hem grubun tutumunu hem de onun için hazır tutulan sonucun niteliğini öne çıkarır.

## Duyurunun Bağı

Başlangıçtaki {ar:وَأَنَّ, tr:wa-anna, gloss:ve şu da} birimi önceki duyuruya bağlanır (17:9, 17:10). Yazıda ve ses akışında birlikte duran anna'nın çift n'si hafif bir işitsel ağırlık yaratır; bu yerel izlenim belirli bir okuma süresi göstermez. Birimin yönettiği içerikte {ar:ٱلَّذِينَ, tr:alladhīna, gloss:o kimseler ki} önce, {ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} yüklemi sonra gelir; kapsam {ar:أَلِيمًا, tr:alīman, gloss:acı veren} sıfatına kadar uzanır. Dinleyici böylece sonucun açıklanmasından önce uyarının kime ilişkin olduğunu öğrenir.

17:9'da Kur'an'ın {ar:يَهْدِي, tr:yahdī, gloss:yol gösterir} ve {ar:يُبَشِّرُ, tr:yubashshiru, gloss:müjdeler} oluşu bildirilir; {ar:ٱلْمُؤْمِنِينَ, tr:al-muʾminīn, gloss:inananlar} için {ar:يَعْمَلُونَ ٱلصَّٰلِحَٰتِ, tr:yaʿmalūna al-ṣāliḥāt, gloss:iyi ve onarıcı işler yaparlar} denir ve {ar:أَجْرًا كَبِيرًا, tr:ajran kabīran, gloss:büyük bir karşılık} vaat edilir (17:9). 17:10'daki {ar:وَأَنَّ, tr:wa-anna, gloss:ve şu da} bu duyuruya, ahirete inanmayanlar için hazırlanmış acı azabı ekler (17:9, 17:10). Böylece iki ayet bilinçli, onarıcı işler için vaat edilen ödülle inkârcı gruba hazırlanan cezayı karşı karşıya getirir; bu bir tam simetri kurmaz ve 17:9'daki iyi işler 17:10'da tanımlanan grubun koşulu olmaz (17:9, 17:10). İnanma ile inanmama aynı kabul ekseninin karşıt yönleri olarak duyulur.

17:10'un hedefi daha geniş bir sınıf adı değil, {ar:ٱلَّذِينَ, tr:alladhīna, gloss:o kimseler ki} ile açılıp {ar:لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:lā yuʾminūna bi-l-ākhirati, gloss:ahirete iman etmeyenler} diye tamamlanan eylem tanımıyla belirlenen gruptur (17:10). Göreli zamirin ve şimdiki fiilin çoğulu, sonuçtaki {ar:لَهُمْ, tr:lahum, gloss:onlara} zamirinde aynı grubu sürdürür. Şimdiki fiil süren ya da alışılmış bir tutumu düşündürür, süresini belirlemez; özneler reddedişin etkin failleridir, bilgisizlikleri yüzünden edilgenleştirilmiş kişiler değil. Bağımsız {ar:لَا, tr:lā, gloss:olumsuzluk} parçacığı fiilden önce kısa bir işitsel dönüş, fiildeki hamza küçük bir gırtlak kesintisi duyurur. Dıştaki anna bildirim kurar; içteki olumsuzluk yalnızca ahirete iman ilişkisini kapsar, ahiretin varlığı ve grubun bu tutumunun nedeni bu cümlede belirlenmez. Göreli cümle {ar:بِٱلْءَاخِرَةِ, tr:bi-l-ākhirati, gloss:ahirete} ile kapanır; ana yüklem ardından başlar ve {ar:لَهُمْ, tr:lahum, gloss:onlara} grubu bu kez sonucun alıcısı olarak yeniden gösterir. Bu sıra cümlenin sözdizimsel ilerleyişini gösterir, tarihsel ya da nedensel bir zaman çizelgesini değil.

{ar:يُؤْمِنُونَ, tr:yuʾminūna, gloss:inanırlar} fiili olağan inanma anlamını korur; Form IV biçimi doğru sayıp kabul etme ve güvenme yönlerine de sınırlı ağırlık verebilir. {ar:بِٱلْءَاخِرَةِ, tr:bi-l-ākhirati, gloss:ahirete} tamlayıcısı hedefi belirlediğinden burada genel bir inançsızlıktan değil, ahirete dönük tutumdan söz edilir. Olumsuzluk, ahireti doğru kabul etme, içten benimseme ve boyun eğme yönlerini esirgemeyi düşündürür; bu nüans yalnızca hedefi belirlenmiş iman ilişkisine aittir, bütün dinî kimliği tarif etmez. Güven, inanma fiilinin bir yönüdür; burada ahireti güvenli kılma, koruma ya da sığınak edinme eylemi anlatılmaz.

17:2, iman fiilindeki güven yönüne ayrı bir bağlam yankısı ekler: Kitap için {ar:هُدًى, tr:hudan, gloss:yol gösterme} kullanılırken hemen ardından {ar:وَكِيلًا, tr:wakīlan, gloss:vekil, işi üstlenen dayanak} edinme yasağı gelir (17:2). İlki yol gösterir, ikincisi işi başkasına bırakma ya da gözetene dayanma ilişkisini düşündürür; bu yan yanalık güvenin ve emanet etmenin nereye yöneldiği sorusunu açar. Yankı, İsrailoğullarına dönük ayrı buyrukla sınırlıdır: buyruk ibadeti veya yetkiyi başkasına bırakmama biçiminde de okunabilir, ancak 17:10'daki grubun güdüsünü açıklamaz ve vekil sözü ahiret inancının adı değildir (17:2, 17:10).

## Ahiret Ufku

Belirli ve soyut {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:ahiret} adı tek bir son gerçekliğe gönderme yapar; yaşam, hâl, yurt ve varış bu aynı göndergenin boyutlarıdır, ayrı yerler ya da olaylar değil. Olağan ahiret anlamına ek olarak duyulabilen “sonra gelen ya da başka olan” yönü, reddedilen iman ilişkisinin hemen ardından gelen tamamlanmış {ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} fiiliyle şimdiki hayat ile sonraki ufuk arasındaki karşıtlığı belirginleştirir (17:10). Bu çağrışım ahiret göndergesinin yerini almaz; sözcüklerin yan yanalığı takvimsel veya metafizik bir kronoloji ya da azabın deneyimlendiği iddiasını da vermez. Adın hamzalı başlangıcı işitilebilir bir ses izi bırakır.

Bu sonraki ufukla ilgili tarihsel sıra ve kişiye dönen sonuçlar, odaktaki hazırlık için iki ayrı bağlam katkısı sunar. 17:4 iki aşamayı {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} diye sayar; 17:5 bunlardan ilkini {ar:أُولَىٰهُمَا, tr:ūlāhumā, gloss:ikisinin ilki} diye ayırır (17:4, 17:5). 17:7'de {ar:وَعْدُ ٱلْءَاخِرَةِ, tr:waʿdu al-ākhirati, gloss:sonraki vaadin gelişi} anılır ve iyilik ya da kötülüğün kişiye döndüğü belirtilir: {ar:إِنْ أَحْسَنتُمْ أَحْسَنتُمْ لِأَنفُسِكُمْ وَإِنْ أَسَأْتُمْ فَلَهَا, tr:in aḥsantum aḥsantum li-anfusikum wa-in asaʾtum fa-lahā, gloss:iyilik ederseniz kendiniz için, kötülük ederseniz yine kendinize} (17:7). 17:8'de {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:siz dönerseniz biz de döneriz} şartı dönüşe dönüşle karşılık verir; Cehennem {ar:حَصِيرًا, tr:ḥaṣīran, gloss:kuşatıcı bir kapanış} diye nitelenir (17:8). Birlikte bu ayrıntılar tarihsel aşamaları ve kişiye dönen karşılığı gösterir, hazırlanmış azabı da daha geniş bir geri dönüş dizisine yerleştirir (17:4, 17:5, 17:7, 17:8). Bu bağlam karşılaştırması vaatleri ahiretle ya da İsrailoğullarının tarihini odaktaki grupla özdeşleştirmez; azabın belli aralıklarla yineleneceğini de ileri sürmez.

Yakın bağlamdaki 17:11, insanın aceleciliğine şimdiki zaman yönünden bir baskı ekler: aynı sesleniş biçimi karşıt isteklere yönelir, insan kötülüğü iyiliği çağırır gibi çağırır {ar:وَيَدْعُ ٱلْإِنسَٰنُ بِٱلشَّرِّ دُعَآءَهُۥ بِٱلْخَيْرِ, tr:wa-yadʿu al-insānu bi-l-sharri duʿāʾahu bi-l-khayri, gloss:insan kötülüğü iyiliği çağırır gibi çağırır} ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} diye nitelenir (17:11). Böylece şimdiki arzu sonraki değerlendirmeyi geride bırakabilir; bu sahne 17:10'daki ahiret reddine zamansal bir baskı bağlamı sağlar (17:10, 17:11). Aynı ayet düşüncesiz bir yakarışı da anlatıyor olabilir; acelecilik olası bir bağlam katkısıdır, tek neden olarak verilmez (17:11). Buluşmayı beklememe ile dünya hayatına razı oluş 10:7'de yan yana gelir: {ar:لَا يَرْجُونَ لِقَاءَنَا وَرَضُوا بِٱلْحَيَاةِ ٱلدُّنْيَا, tr:lā yarjūna liqāʾanā wa-raḍū bi-l-ḥayāti d-dunyā, gloss:buluşmayı beklemez ve dünya hayatına razı olurlar} (10:7); 16:107 ise dünya hayatını ahirete yeğleme tercihini açıkça adlandırır: {ar:ٱسْتَحَبُّوا ٱلْحَيَاةَ ٱلدُّنْيَا عَلَى ٱلْـَٔاخِرَةِ, tr:istaḥabbū l-ḥayāta d-dunyā ʿalā l-ākhirati, gloss:dünya hayatını ahirete yeğlediler} (16:107). Bu iki örnek “sonra gelen ya da başka olan” yönünü şimdiki tercihle ilişkilendirir; ahiret göndergesi olağan anlamını korur ve bağlantı 17:10'daki her kişinin dünyayı seçtiğini ileri sürmez (17:10, 10:7, 16:107).

23:74, ahirete inanmayan aynı grubu yoldan sapmış olarak niteler: {ar:عَنِ ٱلصِّرَاطِ لَنَاكِبُونَ, tr:ʿani ṣ-ṣirāṭi la-nākibūn, gloss:yoldan sapmış olanlar} (17:10, 23:74). Bu yol imgesi, iman fiilindeki doğru sayıp kabul etme yönüyle temas ederek reddedişi şimdiki yönelişe bağlar; belirli bir davranışı ya da neden-sonuç kuralını belirlemez (17:10, 23:74). 27:4 aynı inkâr tanımına işlerin çekici görünmesi ve ardından bocalama ayrıntısını ekler: {ar:زَيَّنَّا لَهُمْ أَعْمَٰلَهُمْ فَهُمْ يَعْمَهُونَ, tr:zayyanā lahum aʿmālahum fahum yaʿmahūn, gloss:işlerini onlara çekici gösterdik ve onlar bocalayıp dururlar} (27:4). 17:45 ise bu grup tanımını Kur'an tilaveti sahnesine taşır; okuyanla onlar arasına {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:gizli bir perde} konur: {ar:وَإِذَا قَرَأْتَ ٱلْقُرْآنَ, tr:wa-idhā qaraʾta l-qurʾāna, gloss:Kur'an'ı okuduğunda} (17:45). Böylece ayetler reddedişi sırasıyla şimdiki yöneliş, eylemlerin algılanışı ve tilavetin karşılanışıyla ilişkilendirir; bu yerel yankılar muhatapların ya da güdülerin aynı olduğunu ve evrensel bir nedensellik kuralını göstermez (17:10, 23:74, 27:4, 17:45).

## Hazır Tutulan Karşılık

{ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} fiili hazırlığı tamamlanmış olarak bildirir; bu zaman görünüşü azabın deneyimlendiğini değil, hazırlığın tamamlandığını söyler (17:10). Süren olumsuzluk taşıyan tutumdan tamamlanmış hazırlığa geçiş, reddediş ile grup için kurulmuş hazır oluşu karşı karşıya getirir. IV. bâbdaki geçmiş zaman birinci çoğul kişi biçimi, üçüncü şahısla tanımlanan gruptan “hazırladık” diyen doğrudan ilahî bildirime geçer; ek konuşanı dilbilgisel olarak gösterir, başkaca bir teolojik açıklama taşımaz. Sıkı ünsüz dizisinin ardından gelen kısa {ar:لَهُمْ, tr:lahum, gloss:onlara} sözü yerel bir ses ağırlığı yaratabilir; bu izlenim sözlük anlamı ya da her okuyuş için süre ölçüsü değildir.

{ar:لَهُمْ, tr:lahum, gloss:onlara}, lam ekiyle grubu hazırlığın alıcısı yapar ve fiil ile {ar:عَذَابًا, tr:ʿadhāban, gloss:bir azap} nesnesi arasında yer alır (17:10). Li ile birleşen çoğul zamir, uzun grup tanımını kısa bir gönderime toplar; sondaki nazal ses kapanışa hafifçe yaklaşır. Bu sıkıştırma aynı grubu alıcı olarak korur, onu küçültmez ya da kişilerin tek tek paylarını bölüştürmez. Ses etkisi yerel bir izlenimdir; gerçek hız ölçüsü değildir.

{ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} hazırlık için birbirini tamamlayan iki imge taşır: sonuç ihtiyaç anında el altında ve kullanılabilir durumdadır; ayrıca belirli bir gereksinimden önce o işe uygun biçimde hazırlanmıştır (17:10). İkinci yön, türetilmiş hazırlama biçiminin amaçlılığından gelir; yeni bir kök anlamı ya da fazladan yoğunluk eklemez. Çoğul alıcı ile sayılabilir nesne birimleri ve toplamı sayma düşüncesini çağrıştırabilir; mal, silah veya başka bir gereci ihtiyaç için ayırıp elde tutma imgesi de yedeklik yönünü somutlaştırır. Bu imgeler hazırlığın düzenini anlatır, fiziksel ambarı ya da envanteri, kesin miktarı, kişiler arasında dağıtımı veya kullanım zamanını bildirmez; temel bildirim grup için önceden hazırlanmış azaptır.

4:18'in ölüm eşiği, hazırlığın ne zaman el altında duyulduğuna somut bir bağlam verir: ölüm gelip çatınca sahne {ar:حَضَرَ أَحَدَهُمُ ٱلْمَوْتُ, tr:ḥaḍara aḥadahumu l-mawtu, gloss:ölüm onlardan birine gelip çatınca} sözüyle açılır, kişinin yanıtı {ar:إِنِّي تُبْتُ ٱلْآنَ, tr:innī tubtu l-āna, gloss:şimdi tövbe ettim} olur; kâfir olarak ölenler için aynı {ar:أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًا, tr:aʿtadnā lahum ʿadhāban alīman, gloss:onlara acı veren bir azap hazırladık} bildirimi yinelenir (4:18). Ortak formül, hazırlığı ihtiyaçtan önce kurulmuş ve ölüm eşiğinde el altında bulunan bir karşılık gibi duyurur; böylece ahiretin sonraki ufkunu da ölüm anında somutlaştırır (4:18). {ar:أَلِيمًا, tr:alīman, gloss:acı veren} hissedilen acıyı niteler, ancak yineleme fazladan yoğunluk ya da bedensel ayrıntı eklemez. Bu bağlantı formülün yinelenişiyle sınırlıdır: grupları özdeşleştirmez, 4:18'in tüm sahnesini 17:10'a taşımaz, kesin bir tarih ya da tek senaryo belirlemez (4:18, 17:10).

## Azabın Niteliği

{ar:عَذَابًا, tr:ʿadhāban, gloss:bir azap} bir masdar olarak eylem ya da durumu adlandırır ve fiilin doğrudan nesnesidir; bu yüzden hazırlanan sonucu maddi bir nesneye çevirmez. Belirsiz mansup biçim azabın kapsamını, miktarını ve biçimini açık bırakır, sınırsız ceza anlamına gelmez. Ceza ve ağır acı yönü, ardından gelen {ar:أَلِيمًا, tr:alīman, gloss:acı veren} sıfatıyla belirginleşir. Aynı anlam ailesindeki tatlı, hoş ve kolay tüketilen yiyecek ya da içecek imgesi ise acının karşısına kolaylık ve hoşluk koyar; bu sözlüksel karşıtlık benzetme düzeyindedir, gerçek bir yiyecek, içecek, tat veya besinden yoksun bırakılma sahnesi değildir.

{ar:أَلِيمًا, tr:alīman, gloss:acı veren} hâl ve belirlilik bakımından başındaki {ar:عَذَابًا, tr:ʿadhāban, gloss:bir azap} ile uyuşur ve aynı isim öbeğini tamamlar; ikinci yüklem ya da ayrı bir incitme eylemi kurmaz. Faʿīl kalıbının etkin-edilgen yönleri, sıfatın azabı acı veren nitelikte sunmasına ve {ar:لَهُمْ, tr:lahum, gloss:onlara} ile gösterilen alıcıların acıyı yaşayanlar olarak duyulmasına imkân verir. Bunlar tek yerel ilişkinin iki yönüdür; ayrı bir dilbilgisel çözümleme, bedensel olay ya da süre belirtilmez. Sıfatın ayet sonundaki yeri bildirimi acı niteliğinde kapatır, kasıtlı bir gerilim iddiasında bulunmaz. Uzun ī sesi ve iki sözcüğün belirsiz mansup sonlukları bağlı bir ses öbeği oluşturabilir; bu, yerel kapanışın ses etkisidir, daha geniş bir uyak düzeni ya da simgesel anlam değil.

## Kişisel Hesap ve Yöneliş

17:12, hazırlıkla ilgili sayma ve hesap yönüne yılların sayısını ve hesabı bildiren {ar:عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:ʿadada al-sinīna wa-l-ḥisāb, gloss:yılların sayısı ve hesap} sözünü, ardından da {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:onu ayrıntısıyla açıkladık} ifadesini ekler (17:12). Yıl sayımı ve hesap, birimleri ve toplamı; ayrıntılandırma ise hesabın açılımını düşündürür. Bu bağlam kök ailesindeki sayma yönünü canlandırır, ancak odaktaki {ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} IV. bâbın geçmiş zaman birinci çoğul kişisi olarak “hazırladık” der, sayma fiiline dönüşmez (17:10, 17:12).

17:13, her insanın payını boynuna bağlayarak kişisel sorumluluğu görünür kılar: {ar:كُلَّ إِنسَانٍ أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:kulla insānin alzamnahu ṭāʾirahu fī ʿunuqihi, gloss:her insanın payını boynuna bağladık}. Diriliş gününde bunun karşısına açık bir kitap çıkar: {ar:يَوْمَ ٱلْقِيَٰمَةِ, tr:yawma al-qiyāmati, gloss:diriliş günü}, {ar:كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:kitāban yalqāhu manshūran, gloss:kişinin açık halde bulacağı kitap} (17:13). 17:14'teki {ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} buyruğu kaydı kişinin okumasına açar; kendi nefsinin hesap görücü olarak yeterli olduğu da eklenir: {ar:كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā bi-nafsika al-yawma ʿalayka ḥasīban, gloss:bugün hesap görücü olarak nefsin yeter} (17:14). Böylece boyna bağlanan kişisel pay, açık kayıt ve kişinin kendi hesabıyla yüzleşmesi birbirini izler (17:13, 17:14).

17:15, bu kişisel hesabın sonuçlarını açıklar: doğru yolu bulan kendi lehine, sapan kendi aleyhine olur {ar:مَنِ ٱهْتَدَىٰ فَإِنَّمَا يَهْتَدِى لِنَفْسِهِۦ وَمَن ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا, tr:mani ihtadā fa-innamā yahtadī li-nafsihi wa-man ḍalla fa-innamā yaḍillu ʿalayhā, gloss:doğru yolu bulan kendi lehine bulur, sapan da kendi aleyhine sapar}; kimse başkasının yükünü taşımaz {ar:وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz}. Elçi gönderilinceye dek azap edilmeyeceği de belirtilir: {ar:وَمَا كُنَّا مُعَذِّبِينَ حَتَّىٰ نَبْعَثَ رَسُولًا, tr:wa-mā kunnā muʿadhdhibīna ḥattā nabʿatha rasūlan, gloss:bir elçi gönderinceye kadar azap etmeyiz} (17:15). Bu, 17:10'u kişisel ve devredilemez sorumluluk çerçevesinde okumaya imkân verir; hangi grup üyesinin hangi bildirimi aldığı belirtilmez. Elçi koşulu ayrıca bir adalet sınırı olarak okunabilir, hazırlığın tek açıklaması olarak değil (17:10, 17:15).

82:5 hesabın zaman kapsamını genişletir: her canın öne gönderdiğini ve geride bıraktığını bileceği bildirilir {ar:عَلِمَتْ نَفْسٌ مَّا قَدَّمَتْ وَأَخَّرَتْ, tr:ʿalimat nafsun mā qaddamat wa-akhkharat, gloss:her can öne gönderdiğini ve geride bıraktığını bilir} (82:5). Böylece kayıt önceki ve sonraki eylemleri kuşatır; ayet odaktaki grubu ya da azabı adlandırmaz ve 17:10'un biçimine yeni bir özellik aktarmaz (17:10, 82:5). 17:5 ve 17:7'de vaatlerin gerçekleşmesi, 17:13 ve 17:14'te kaydın sunulup okunması, 17:15'te yükün devredilmemesi bu geniş hesap çerçevesine bağlanabilir (17:5, 17:7, 17:13, 17:14, 17:15, 82:5). Bu okumada {ar:أَعْتَدْنَا, tr:aʿtadnā, gloss:hazırladık} yargı anında doğan ani tepki yerine kayda geçen eylemlerle uyumlu, önceden hazırlanmış bir karşılık gibi görünür (17:10, 17:13, 17:14, 17:15, 82:5). Bağlantı anlatı sırasına dayanır: kayıt sonucu mekanik olarak doğuran neden diye kurulmaz ve azaba kesin bir tarih verilmez (17:5, 17:7, 17:13, 17:14, 17:15).

17:16'nın toplumsal sahnesinde refah koşulu belirler, ardından sınır aşımı gelir, hüküm kesinleşir ve şehir bütünüyle yıkılır: {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:refah içindekiler}, {ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:orada sınırı aştılar}, {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawl, gloss:hüküm sözü üzerine kesinleşti}, {ar:فَدَمَّرْنَٰهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık} (17:16). {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aştılar} olağan olarak sınır aşmayı bildirir; olgun meyvenin koruyucu kabuğundan çıkmasıyla ilişkili kök imgesi bu geçişi somutlaştırır, ancak sözcüğün tek ya da olağan anlamı değildir (17:16). Bu sıra, 17:10'daki hazırlığa yalnızca benzetme yoluyla bağlanır: toplumsal sürecin sonunda sonuç hazır hâle gelmiş gibi görünür (17:10, 17:16). Bağlantı refahı cezanın mekanik nedeni yapmaz ve topluluğun yıkımını ahiret azabıyla özdeşleştirmez (17:16).

17:18, 17:19 ve 17:21 yöneliş karşılaştırmasına ayrı katkılar sunar. 17:18'de hemen olanı isteyen için karşılık yalnızca istenen kimselere, dilenen ölçüde hızlandırılır: {ar:مَّن كَانَ يُرِيدُ ٱلْعَاجِلَةَ, tr:man kāna yurīdu al-ʿājilata, gloss:hemen olanı isteyen kimse}, {ar:عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ, tr:ʿajjalnā lahu fīhā mā nashāʾu li-man nurīdu, gloss:orada dilediğimizi istediğimiz kimseye çabuklaştırırız}; ardından Cehennem ve yerilme gelir (17:18). 17:19 sonraki hayatı isteyen, ona yaraşır çabayla çalışan ve inanmış olan kişiyi tanımlar {ar:وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا وَهُوَ مُؤْمِنٌ, tr:wa-man arāda al-ākhirata wa-saʿā lahā saʿyahā wa-huwa muʾmin, gloss:ahireti isteyen, ona yaraşır çabayla çalışan ve inanmış olan kimse} ve bu çabanın takdir edildiğini bildirir {ar:كَانَ سَعْيُهُم مَّشْكُورًا, tr:kāna saʿyuhum mashkūran, gloss:çabaları takdir edildi} (17:19). 17:21 ise ahireti derece ve üstünlük bakımından daha büyük bir ölçekte konumlandırır: {ar:وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًا, tr:wa-la-l-ākhiratu akbaru darajātin wa-akbaru tafḍīlan, gloss:ahiret derece ve üstünlük bakımından daha büyüktür} (17:21). Birlikte bu ayetler ödülün seçici hızlandırılmasını, sonraki ufka yöneltilen çabanın şart ve takdirini, ahiretin daha büyük ölçeğini gösterir; 17:10'la bağlantı çabanın yönünü sorgulatır, her inkârcının dünyayı seçtiğini ileri sürmez (17:10, 17:18, 17:19, 17:21).

17:20 iki yönelişe de şimdiki zamanda destek verildiğini ve Rabbin bağışının esirgenmediğini bildirir: {ar:كُلًّا نُّمِدُّ هَٰٓؤُلَاءِ وَهَٰٓؤُلَاءِ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:şu iki gruba da vermeyi sürdürürüz}, {ar:وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūran, gloss:Rabbinin bağışı engellenmiş değildir} (17:20). Bu, şimdiki yararın sonraki sonucu tek başına belirlemediğini ve mevcut nimetle 17:10'daki hazırlığın yan yana bulunabildiğini gösterir (17:10, 17:20). Ayet eşit miktarı ya da nimetin yanıltma amacı taşıdığını belirtmez; hazırlanan sonucun fiziksel biçimini de açıklamaz (17:20).

17:20'deki esirgenmeyen bağış, azabın anlam ailesindeki tatlılık ve kolay tüketim yönüyle ayrı bir duyusal karşıtlık kurar (17:20). Odaktaki {ar:عَذَابًا, tr:ʿadhāban, gloss:azap} ceza anlamını, {ar:أَلِيمًا, tr:alīman, gloss:acı veren} yaşanan acıyı taşır; aynı ailedeki hoş ve kolay tüketilen nimetle, ayrıca vazgeçme ya da alıkoyma yönüyle karşılaştırıldığında, mevcut bir iyilikten yoksun kalmak acının olası bir yaşantısı olarak düşünülebilir (17:10, 17:20). Bu yalnızca anlam ailesinin sunduğu bir benzetmedir: odaktaki ad azaptır, gerçek yiyecek ya da tat yoksunluğunu ve gelecekteki nimetin geri çekilmesini bildirmez (17:10, 17:20).

</source_prose>
