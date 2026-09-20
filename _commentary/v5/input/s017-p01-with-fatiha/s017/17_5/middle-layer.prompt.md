# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:5**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.middle.claims.json`

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
- Refer to source paragraphs as `17:5 ¶N`.

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

`(17:5 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:5",
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
        "citation": "(17:5 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_5/17_5.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_5/17_5.middle.claims.json \
  --ayah-ref 17:5
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_5/17_5.prose.editorial.tr.md`

<source_prose>
İkisinden ilkinin vaadi vakti geldiğinde ({ar:وَعْدُ أُولَىٰهُمَا, tr:waʿdu ūlāhumā, gloss:ikisinin ilkinin vaadi}), üzerinize bize ait kullardan çetin kuvvet sahibi bir topluluk gönderdik ({ar:بَعَثْنَا عَلَيْكُمْ عِبَادًا لَنَا, tr:baʿathnā ʿalaykum ʿibādan lanā, gloss:üzerinize bize ait kullar gönderdik}); onlar evlerin arasına girip dolaştılar ({ar:فَجَاسُوا۟ خِلَٰلَ ٱلدِّيَارِ, tr:fa-jāsū khilāla ad-diyāri, gloss:evlerin arasından geçip dolaştılar}). Son cümlecik, yaşananı yerine getirilmiş bir vaat diye niteler ({ar:وَكَانَ وَعْدًۭا مَّفْعُولًۭا, tr:wa-kāna waʿdan mafʿūlan, gloss:ve bu yerine getirilmiş bir vaat oldu}).

## Sözün Vakti

Açılıştaki {ar:فَإِذَا, tr:fa-idhā, gloss:ardından, vakti geldiğinde} önceki söyleyişe bağlanır; {ar:إِذَا, tr:idhā, gloss:ne zaman} koşulun zaman eşiğini açar, bu bağlantı önceki sözün içeriğini yeniden kurmaz. Ardından gelen geçmiş biçimli {ar:جَآءَ, tr:jāʾa, gloss:geldi}, bu eşiği sevkten önce beklenen ve sonuç doğuracak bir ana çevirir. Nominatif {ar:وَعْدُ, tr:waʿdu, gloss:vaat} ise birinci bâbın geçişsiz {ar:جَاءَ, tr:jāʾa, gloss:geldi} fiilinin öznesidir; bu cümlede geliş eylemini taşıyan başka bir fail değil, vaat edilen olayın kendisidir. Böylece soyut bildirim sahneye girecek bir olaya dönüşür, koşul da belirli bir tarih ya da dış olayların takvimini vermez.

{ar:أُولَىٰهُمَا, tr:ūlāhumā, gloss:ikisinin ilki} biçimindeki dişil sıra gövdesi ilkliği, ekli ikil zamir iki üyeli göndergeyi taşır. Yakın bağlam bu ilkliği ayrı dönüşlerle çevreler: ilk olayın ardından verilen karşı hamle (17:6), sonraki vaat (17:7) ve davranışa bağlanan dönüş koşulu (17:8). Bu yan yanalık vaadi bir karşılıklar dizisinin açılışı gibi duyurur; dönüş ilişkisini çevredeki olaylar kurarken {ar:أُولَىٰهُمَا, tr:ūlāhumā, gloss:ikisinin ilki} ilk olayı sıra içinde adlandırır. İkil yapı iki üyeli göndergeyi kurar; sonraki vaadin zamanı ve içeriğiyle iki olay arasındaki süre, kesintisiz bir tarih çizgisi olarak belirlenmez.

Bu beklenen olayın tehdit tonu, önceki uyarıyla birlikte belirginleşir. Hüküm diliyle iki bozulmayı ve büyük taşkınlığı bildiren sözler (17:4), yeryüzünde bozgunculuk çıkarılacağını açıkça söyler ({ar:وَقَضَيْنَآ, tr:wa-qaḍaynā, gloss:hükme bağladık}; {ar:عُلُوًّا كَبِيرًا, tr:ʿuluwwan kabīran, gloss:büyük bir taşkınlık}; {ar:لَتُفْسِدُنَّ فِي الْأَرْضِ, tr:la-tufsidunna fī l-arḍ, gloss:yeryüzünde bozgunculuk çıkaracaksınız}). Ardından gelen {ar:وَعْدُ, tr:waʿdu, gloss:vaat} ile {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik}, hedefe yönelen kuvvetle birleşince önceden bildirilen sonucun gerçekleşmesini duyurur. Geleceğe bakan vaat anlamı korunur; {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} yönelimi, çetin kuvvet ve hemen sonraki içeri giriş de söze bu bağlamda tehdit tonu verir. Bu yakınlık, önceki uyarının hedefe yöneltilen sevk içinde nasıl işitildiğini açıklar; topluluğun kimliği ve olayın tüm tarihsel açıklaması bu bağlantının kapsamına girmez.

Vaat için açılan bu zaman eşiği, insanın zamanı kullanışıyla da karşıtlık kurar. İnsan kötülüğü bile aceleyle isteyebilir (17:11; {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci}); geceyle gündüz, yılların sayısı ve hesap ise zamanın ölçülebilir yanını öne çıkarır (17:12; {ar:ٱلَّيْلَ وَالنَّهَارَ, tr:al-layla wa-n-nahāra, gloss:gece ile gündüz}; {ar:عَدَدَ السِّنِينَ, tr:ʿadada s-sinīna, gloss:yılların sayısı}; {ar:وَالْحِسَابَ, tr:wa-l-ḥisāba, gloss:ve hesap}). {ar:وَعْدُ, tr:waʿdu, gloss:vaat} sözcüğünün anlam ailesinde belli aralıklarla yinelenen gelişler de bulunduğundan, sayım ve hesap vaadi ölçülebilir zaman içinde düşünmeye açar; acele ise buna daha gevşek bir karşıtlık ekler. İlk ve sonraki vaat, dönüş koşulu ve sayılı yıllar yinelenebilir bir ritim sezdirir (17:6, 17:7, 17:8, 17:12); bu ritim belirli tarih, süre ya da sayılı kök tekrarları düzeni kurmaz. Aynı anlam ailesindeki bir yıl meyve verip ötekinde vermeyen ağaç kullanımı ürün bağlamına aittir; burada taşıyıcı vaat olduğundan ve ürün söz konusu olmadığından, bu ağaç imgesiyle kurulan bağlantı etkinleşmez.

## Gönderilenler

Vaat vakte bağlandıktan sonra cümle önce hedefi, ardından gönderilenleri gösterir. Geçmiş zamanlı birinci çoğul {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik} sevk eylemini kurar; hemen ardından gelen {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} edatla ikinci çoğul zamirini birleştirip yönelinen tarafı, {ar:عِبَادًا, tr:ʿibādan, gloss:kullar} grubu tanıtılmadan önce görünür kılar. Bu sıra kuvvetle birleşince önce hedefte hissedilen bir baskı yönü kurar; fiilin kendisi güzergâhı değil, yer bildiren sonraki tamlama hareketin yolunu gösterir. Belirsiz çoğul kullar önce sevkin nesnesi, sonra {ar:جَاسُوا, tr:jāsū, gloss:içeride dolaştılar} fiilinin anlaşılan öznesi olur: gönderilen topluluk aynı olayda eyleyene dönüşür. Böylece toplu fail belirginleşirken kişilerin tek tek kimliği açık kalır; hareketin nesnesi de söylenmez.

Gönderilen topluluğun kimle bağı, kapasitesinden önce açıklanır. {ar:لَنَا, tr:lanā, gloss:bize ait} önündeki kullara eklenerek konuşanla aidiyet ilişkisi kurar; başka bağlamlarda amaç da bildirebilen lām burada önceki isimle yakın bağından ötürü aidiyet okumasını öne çıkarır, amaç anlamının dilbilgisel imkânını tümden kapatmadan. Kulluk adı yaratılmışlık ve Tanrı'ya bağlılığı taşır; hizmet ve boyun eğme yönü de bu ilişkiye eşlik eder. Bu ilahî bağlılık insan hukukundaki mülkiyet kategorisine çevrilmez. Böylece kişiler topluca ve belirsiz kalırken, konuşanla aralarındaki ilişki belirginleşir.

“Kul” adının taşıdığı bağlılık, başka ayetlerde farklı vasıflarla yan yana gelince daha seçikleşir. İbrahim, İshak ve Yakub “kullarımız” diye anılır, ardından ayrıca kuvvet ve basiret sahipleri olarak nitelenir (38:45; {ar:عِبَٰدَنَآ إِبْرَٰهِيمَ وَإِسْحَٰقَ وَيَعْقُوبَ, tr:ʿibādanā Ibrāhīm wa-Isḥāq wa-Yaʿqūb, gloss:kullarımız İbrahim, İshak ve Yakub}; {ar:أُو۟لِى ٱلْأَيْدِى وَٱلْأَبْصَٰرِ, tr:ulī l-aydī wa-l-abṣār, gloss:kuvvet ve basiret sahipleri}). Nuh “şükreden bir kul” diye anılır (17:3; {ar:عَبْدًا شَكُورًا, tr:ʿabdan shakūran, gloss:şükreden bir kul}); kulların günahlarından da söz edilir (17:17; {ar:بِذُنُوبِ عِبَادِهِ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahlarıyla}). 17:1'de başka bir kişiye “kulu” denir ({ar:بِعَبْدِهِ, tr:bi-ʿabdihi, gloss:kulu}). Bu karşılaştırmalar, “kul” adının bağlılık ilişkisini, ona eşlik eden nitelemelerin ise profili kurduğunu gösterir. Bu yankı gönderilenleri anılan kişilerle özdeşleştirmez; 17:5'teki topluluğun ahlaki portresini de tek başına tamamlamaz.

Bu aidiyet sözü okurun kendi kulluk diliyle de temas eder. Fâtiha'da dua eden kişi “yalnız sana kulluk ederiz” der (1:5; {ar:إِيَّاكَ نَعْبُدُ, tr:iyyāka naʿbudu, gloss:yalnız sana kulluk ederiz}). Oradaki {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} fiili, burada topluluğu adlandıran {ar:عِبَادًا لَنَا, tr:ʿibādan lanā, gloss:bize ait kullar} ismiyle aynı kulluk anlam ailesine başka bir biçimde katılır. Bu yankı okurun dua dilini gönderilenlerin ilahî aidiyetiyle yan yana getirir; dua edenlerin zamiriyle ayetteki tarihsel topluluk ayrı özneler olarak kalır.

Görevlendirilmekle ahlaki onay arasındaki ayrım, yakındaki dünya ve ahiret yönelişlerinde de görünür olur. Yakın dünyayı isteyen ile ahireti isteyen ayrı ayrı anılır (17:18, 17:19; {ar:يُرِيدُ الْعَاجِلَةَ, tr:yurīdu l-ʿājilata, gloss:yakın dünyayı isteyen}; {ar:أَرَادَ الْءَاخِرَةَ, tr:arāda l-ākhirata, gloss:ahireti isteyen}); ardından her iki tarafa da Rabbin bağışından verildiği belirtilir (17:20; {ar:نُّمِدُّ كُلًّا هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ مِنْ عَطَآءِ رَبِّكَ, tr:numiddu kullan hāʾulāʾi wa-hāʾulāʾi min ʿaṭāʾi rabbika, gloss:şunlara da bunlara da Rabbinin bağışından veririz}). Bu karşılaştırma görevin işlevini nihai ahlaki yargıdan ayırır: dünya imkânının iki tarafa da verilmesi onayla özdeş değildir. Gönderilen kuvvetin bu iki yönelişten hangisiyle ilişkili olduğu açık bırakılır; kulluk adı ve görev tek başına nihai hükmü kurmaz.

Bu bağı kurduktan sonra topluluğun niteliği üç basamakta yoğunlaşır: {ar:عِبَادًا لَنَا, tr:ʿibādan lanā, gloss:bize ait kullar} aidiyeti, {ar:أُو۟لِى بَأْسٍ, tr:ulī baʾsin, gloss:güç sahipleri} taşınan kapasiteyi, {ar:شَدِيدٍ, tr:shadīdin, gloss:çetin} ise bu kapasitenin yoğunluğunu verir. Çoğul {ar:أُو۟لِى, tr:ulī, gloss:sahipleri} ile ardından gelen mecrur {ar:بَأْسٍ, tr:baʾsin, gloss:kuvvet} izafet kurar; {ar:شَدِيدٍ, tr:shadīdin, gloss:çetin} doğrudan kuvveti niteler. Sertlik ve direnç böylece ajanların taşıdığı çetin güçte toplanır. Sıfat bu kuvvete yerleşik bir yoğunluk verir; terkibin içinde rakip ölçüsü veya zaman süresi kurulmaz. Şeddeli d'nin sıkı tınısı yoğunluğu işitsel olarak yankılayabilir; {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} yönelimi ve ardından gelen dolaşma bu niteliği hedefe dönük cezalandırıcı basınç olarak duyurur. Buradaki basınç imgesi kuvvetin etkisini belirginleştirir, belirli bir keder ya da geçim kaybı sahnesi kurmaz.

Sevk eyleminin hareket tonu, aynı grubun hemen sonraki fiilde etkin görünmesiyle belirginleşir. {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik} bir topluluğu gönderir; ardından {ar:جَاسُوا, tr:jāsū, gloss:dolaşıp ilerlediler} onu hareket halinde gösterir. Bu temas, “göndermek” anlamına durgun olanı etkinleştirme, harekete geçirme yankısı ekleyebilir; topluluğun bundan önceki hali cümlede belirtilmez. Daha uzaktaki bir kullanımda aynı kök ailesinin başka çekimli biçimi uyanma ve dirilme bağlamında geçer, hemen ardından vaadin doğruluğu anılır (36:52; {ar:مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا, tr:man baʿathanā min marqadinā, gloss:bizi yattığımız yerden kim kaldırdı}). Bu yankı gönderme fiiline bir kaldırılış ufku katar; 17:5'teki topluluğun durumunu uykuya ya da ölüme taşımaz, çünkü iki ayetteki biçim ve sahne ayrıdır.

Gönderme fiilinin görevlendirme yönünü başka bir ayet, gönderilişi izleyen tepki ve sonuçla birlikte görünür kılar. Musa'nın Firavun'a ayetlerle gönderilmesi, ardından ayetlere haksızlık edilmesi ve bozguncuların akıbeti anılır (7:103; {ar:ثُمَّ بَعَثْنَا مِنۢ بَعْدِهِم مُّوسَىٰ بِـَٔايَٰتِنَآ إِلَىٰ فِرْعَوْنَ, tr:thumma baʿathnā min baʿdihim Mūsā bi-āyātinā ilā Firʿawn, gloss:sonra Musa'yı ayetlerimizle Firavun'a gönderdik}; {ar:فَظَلَمُوا۟ بِهَا, tr:fa-ẓalamū bihā, gloss:ayetlere haksızlık ettiler}; {ar:عَٰقِبَةُ ٱلْمُفْسِدِينَ, tr:ʿāqibatu l-mufsidīn, gloss:bozguncuların akıbeti}). Odaktaki {ar:بَعَثْنَا عَلَيْكُمْ, tr:baʿathnā ʿalaykum, gloss:üzerinize gönderdik} ile bu gönderme böylece görev-haksızlık-sonuç örüntüsünü uzaktan yankılar. Bu yankı görevlendirme boyutunu ekler; kişiler ve tarihsel olaylar kendi bağlamlarında kalır, 17:4'e özel bir yanıt ilişkisi kurulmaz.

Toplu sevkin yanında bölüm, her kişinin kendi sorumluluğunun sınırını da çizer. Kişinin kaydı kendisine bağlanır ve açılmış halde karşısına çıkar (17:13; {ar:أَلْزَمْنَٰهُ, tr:alzamnahu, gloss:ona bağladık}; {ar:كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:kitāban yalqāhu manshūran, gloss:açılmış halde karşısına çıkan kitap}); kimse başkasının yükünü taşımaz (17:15; {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz}). Cezanın başlaması da bir elçinin gönderilmesine kadar ertelenir (17:15; {ar:حَتَّىٰ نَبْعَثَ رَسُولًا, tr:ḥattā nabʿatha rasūlan, gloss:bir elçi gönderinceye kadar}). Elçi eşiği gönderme motifini sürdürürken bu bildirimin görevini ayırır: odaktaki silahlı toplulukla elçilik aynı görev değildir. Böylece kişisel sorumlulukla kamusal kuvvet yan yana görünür; bu karşılaştırma baskının özel tarihini veya işleyişini açıklayan bir bağ kurmaz.

## Evlerin İçinden

Hedef ve eyleyen belirlendikten sonra ikinci {ar:فَ, tr:fa, gloss:ardından ve bunun sonucu olarak}, geçmiş zamanlı çoğul {ar:جَاسُوا, tr:jāsū, gloss:evlerin içinde dolaştılar} fiilini sevke bağlar. Grup gönderildikten sonra harekete geçer; bu yerel bağ sıra ile sonucu birlikte duyurur, anlatıdaki dış zaman aralığını ya da tüm tarihsel nedeni değil. Açılıştaki {ar:فَإِذَا, tr:fa-idhā, gloss:ardından, vakti geldiğinde} ile {ar:فَجَاسُوا۟, tr:fa-jāsū, gloss:ardından dolaştılar} içindeki yinelenen ses de koşuldan sonuca geçişi işittirir; katkısı bu cümle hareketini pekiştirmektir, genel bir ses yasası kurmak değil. Fiilin çoğul öznesi gönderilen kullardan anlaşılır; nesne belirtilmediğinden hareketin neyi arama amacı taşıdığı bu cümlede açık kalır.

Buradaki {ar:جَاسُوا, tr:jāsū, gloss:içeride ilerlediler}, evlerin arasında dolaşmayı doğrudan bildirir; Kur'an'daki tek kullanımı geçmiş zamanlı çoğul I. bâb biçimidir. Yanındaki yer tamlaması anlam alanını daraltır: mansup {ar:خِلَٰلَ, tr:khilāla, gloss:aralarından} “nereden?” sorusuna cevap veren yer zarfıdır, eksik bir nesne değildir; belirli, çoğul ve tamlayan biçimdeki {ar:ٱلدِّيَارِ, tr:ad-diyāri, gloss:evler ve meskenler} güzergâhı yaşanan yerlere taşır. Böylece hareketin alanı açık arazi değil, evlerin arasındaki geçitlerdir; buradaki açıklık mekânsal geçişi anlatır. Her meskenin dolu olup olmadığı ve yerleşimin dış sınırı ise belirtilmez.

İç güzergâh bedensel bir giriş hissi de taşır. {ar:جَاسُوا, tr:jāsū, gloss:içeride ilerlediler} burada ayak basıp çiğnemeye açılan bir görüntü verebilir; evlerin arasıyla ve daha sonraki giriş-yıkım sahnesiyle temas bu çağrışımı güçlendirir (17:7). Bu çağrışım hareketin sertliğini artırır; 17:5'te ayrıca bir çiğneme veya yıkım eylemi bildirilmez. Fiilin sert başlangıcı da içeri yönelen rotayla birleşince pürüzlü giriş hissi verir; sesin katkısı duyusal tondadır, niyeti ya da belirli bir zararı saptamaz. {ar:ٱلدِّيَارِ, tr:ad-diyāri, gloss:meskenler} sözcük ailesindeki dönme ve çevreleme imgesi, geçişe çevrili bir yerleşimin içinden dolaşma yankısı ekler. Bu analojide odak sözcük yine meskenleri adlandırır; çevrenin gerçek sınırları ayette çizilmez.

İçeri giriş, sonraki ayette açıkça karşılaştırılan girişe doğru bir mekânsal öncül gibi duyulur. Mescide ilk kez girdikleri gibi girme çağrısı ve ardından üzerinde yükseldiklerini bütünüyle yıkma ifadesi birlikte verilir (17:7; {ar:وَلِيَدْخُلُوا الْمَسْجِدَ كَمَا دَخَلُوهُ أَوَّلَ مَرَّةٍ, tr:wa-li-yadkhulū l-masjida kamā dakhalūhu awwala marratin, gloss:mescide ilk kez girdikleri gibi girmeleri}; {ar:وَلِيُتَبِّرُوا مَا عَلَوْا تَتْبِيرًا, tr:wa-li-yutabbirū mā ʿalaw tatbīran, gloss:üzerinde yükseldiklerini bütünüyle yıkmaları}). Böylece evlerin aralarından geçen güzergâh, sonraki mescit girişinin mekânsal öncülü olur; hareket, yıkım temasının da yer aldığı bir giriş örüntüsü içinde duyulur. Bu yankı iki sahnenin faillerini, hedeflerini ve tarihlerini kendi bağlamlarında bırakır; 17:7'deki yıkımı 17:5'te ayrıca gerçekleşmiş bir eylem olarak aktarmaz.

Güzergâhın “aralıklar” boyunca uzanması, aynı anlam ailesindeki düzenin sağlamlığını yitirme çağrışımını da açabilir. Bozulma ve büyük taşkınlık sözleri bu yankıyı tetikler (17:4): {ar:خِلَٰلَ ٱلدِّيَارِ, tr:khilāla ad-diyāri, gloss:evlerin aralarından} fizikî geçitleri anlatmayı sürdürürken, zayıflamış düzenin içinden geçilebilen açıklıklarını da düşündürür. Bu benzerlik, siyasal bozulmanın içeri sızma imgesiyle duyulmasını sağlar; kelimenin cümledeki yer işlevi yine aralıklardan geçen güzergâhtır. İlişki anlamsal bir yankıdır, belirli sokakların fiziksel olarak açıldığına dair bir olay anlatımı değildir.

Meskenlerden kamusal yerleşime uzanan ölçek, daha geniş bir eşikle karşılaşır. Bir taşkınlığın ardından yerleşim yeri üzerine hükmün gerçekleşmesi ve onun bütünüyle yıkılması anlatılır (17:16; {ar:قَرْيَةً, tr:qaryatan, gloss:yerleşim yeri}; {ar:فَحَقَّ عَلَيْهَا الْقَوْلُ, tr:fa-ḥaqqa ʿalayhā l-qawlu, gloss:hüküm onun üzerine gerçekleşti}; {ar:فَدَمَّرْنَٰهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık}). Bu bağlam, evler arasındaki hareketin ölçeğini yerleşim çapındaki kamusal sonuca doğru genişletir; tek tek meskenlerle bir yerleşimin bütünü arasındaki farkı görünür kılar. Odaktaki çoğul mesken adı evleri ve yaşanan alanı adlandırmaya devam eder; 17:16 ile kurulan bu ölçek benzerliği tek başına iki anlatının tarihsel özdeşliğini kurmaz.

Meskenlerin anlamı, yurtlarından edilme bağlamında konuttan topluluğun yaşadığı alana doğru genişler. Odaktaki {ar:ٱلدِّيَارِ, tr:ad-diyāri, gloss:meskenler} evleri ve yerleşim alanını belirtirken, bir topluluğun yurtlarından çıkarılması bu konut çekirdeğini ortak yurda taşır (59:2; {ar:مِن دِيَٰرِهِمْ, tr:min diyārihim, gloss:yurtlarından}). Başka bir yerde ülkeden çıkarılma girişimi toprak kaybı tehdidini açık eder (17:76; {ar:لَيَسْتَفِزُّونَكَ مِنَ ٱلْأَرْضِ لِيُخْرِجُوكَ مِنْهَا, tr:la-yastafizzūnaka mina l-arḍi li-yukhrijūka minhā, gloss:seni ülkeden çıkarıp sürmek istiyorlar}). Bu iki bağlam, evlerin arasındaki güzergâha yurt ve toprak kaybı yönünde toplumsal bir ölçek ekler. Bu genişleme diyār'ı doğrudan “ülke” diye çevirmeyi ya da önceki bozulmayı sürgünün nedeni saymayı gerektirmez; bağlantı, konuttan ortak yurda uzanan anlam yankısıyla sınırlıdır.

Yerleşim içindeki erişim, yapılı çevrenin kırılganlığına dair iki ayrı sahneyle genişler. Bir topluluk kalelerinin kendilerini koruyacağını sanır; ummadıkları yönden gelen saldırı bu güveni boşa çıkarır ve evleri kendi elleriyle, ayrıca müminlerin elleriyle yıkılır (59:2; {ar:وَظَنُّوٓا أَنَّهُم مَّانِعَتُهُمْ حُصُونُهُمْ, tr:wa-ẓannū annahum māniʿatuhum ḥuṣūnuhum, gloss:kalelerinin onları koruyacağını sandılar}; {ar:فَأَتَىٰهُمُ ٱللَّهُ مِنْ حَيْثُ لَمْ يَحْتَسِبُوا۟, tr:fa-atāhumu llāhu min ḥaythu lam yaḥtasibū, gloss:Allah onlara ummadıkları yönden geldi}; {ar:يُخْرِبُونَ بُيُوتَهُم بِأَيْدِيهِمْ وَأَيْدِى ٱلْمُؤْمِنِينَ, tr:yukhribūna buyūtahum bi-aydīhim wa-aydī l-muʾminīn, gloss:evlerini kendi elleriyle ve müminlerin elleriyle yıkıyorlar}). Bu sahne vaadin tehdit tonuna, korunaklı sayılan yerleşimin aşılması ve evlerin somut zarara uğraması üzerinden yankı verir. Ayrı bir yapısal imge, yıkımın temellerden başlayıp çatının üzerlerine düşmesine kadar uzanışını gösterir (16:26; {ar:فَأَتَى ٱللَّهُ بُنْيَٰنَهُم مِّنَ ٱلْقَوَاعِدِ فَخَرَّ عَلَيْهِمُ ٱلسَّقْفُ مِن فَوْقِهِمْ, tr:fa-atā llāhu bun'yānahum mina l-qawāʿidi fa-kharra ʿalayhimu s-saqfu min fawqihim, gloss:yapılarına temellerinden gelindi ve çatı üzerlerine çöktü}). İlki kale korumasının bozulmasıyla ev zararını, ikincisi temelden çatıya yayılan çöküşü taşır; iki sahne birlikte iç güzergâhın yanına yapılı çevrenin kırılganlığını ekler, ortak bir tarihsel ya da nedensel dizi kurmaz.

İç güzergâh, fiilin dikkatle arama ve bir alanı kapsamlıca tarama yönünü de mümkün kılar. Yinelenen giriş ve yıkım hareketi (17:7), ayrıca kentlerin kıyamet öncesi yıkım ya da ağır ceza ufkuna alınması (17:58), ev içinden kent ölçeğine uzanan tarama imgesini besler. Kentler için bu akıbetin Kitap'ta yazılmış olduğu da belirtilir (17:58; {ar:كَانَ ذَٰلِكَ فِى ٱلْكِتَٰبِ مَسْطُورًا, tr:kāna dhālika fī l-kitābi masṭūran, gloss:bu Kitap'ta yazılmıştı}). {ar:جَاسُوا, tr:jāsū, gloss:içeride ilerlediler} fiili evlerin arasında dolaşma anlamını korurken, {ar:خِلَٰلَ ٱلدِّيَارِ, tr:khilāla ad-diyāri, gloss:evlerin aralarından} bu olası aramaya yerleşimin içine yayılan bir rota verir. Tarama böylece hareketin kapsamını genişletir; aranan nesne ve askerlerin araştırma niyeti ise bu bağlantıda açık kalır.

Bu olası tarama, kişilerle ilgili kayıt çevresinden de bir açığa çıkış yankısı alır. Her kişinin önüne açılmış halde çıkan kayıt (17:13; {ar:كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:kitāban yalqāhu manshūran, gloss:açılmış halde karşısına çıkan kitap}) ile kulların günahları hakkındaki bilgi (17:17; {ar:بِذُنُوبِ عِبَادِهِ خَبِيرًا بَصِيرًا, tr:bi-dhunūbi ʿibādihi khabīran baṣīran, gloss:kullarının günahlarından haberdar ve gören}) içeride olanın görünür hale gelmesi fikrini ayrı ayrı besler. Bu çağrışım fizikî dolaşımın yanına saklı davranışın açığa çıkacağı bir ufuk ekler; denetleme bilgisi veya amacı askerlerin kendilerine yüklemez. Kent akıbetinin Kitap'ta yazılı oluşu ise topluluk ölçeğinde kalır (17:58); kişi başına açılan kayıtla karışmaz ve bireysel sorumluluğu başkasına aktarmayı gerektirmez.

## Yerine Gelmiş Vaat

Evlerin içinden geçen güzergâhın ardından kapanış, dikkati yeniden vaadin nasıl adlandırıldığına çevirir. Başta nominatif {ar:وَعْدُ, tr:waʿdu, gloss:vaat} geçişsiz fiilin öznesiyken, sonda mansup {ar:وَعْدًا, tr:waʿdan, gloss:vaat} geçmiş biçimdeki kopula {ar:كَانَ, tr:kāna, gloss:oldu} altında yaşananı adlandıran yüklem olur. Böylece ayetin başındaki geliş, aradaki sevk ve girişin ardından yerine gelmiş vaat olarak kapanır. Edilgen ortaç {ar:مَّفْعُولًۭا, tr:mafʿūlan, gloss:gerçekleştirilmiş} tamamlanmış eylem niteliğini verir; bu cümlede faili açıkça adlandırmaz. Bağlayıcı {ar:وَ, tr:wa, gloss:ve} ile kopula kapanışı önceki eyleme bağlayıp onun gerçekleşmiş durumunu bildirir, yeni bir gönderme eylemi başlatmaz. {ar:كَانَ, tr:kāna, gloss:oldu} önceki eylemi geriye dönük mühürleyebilir ya da eylemle birlikte onun gerçekleşmiş durumunu bildirebilir; iki bağlanış da tamamlanmışlığı öne çıkarır. Doğrudan hitap {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} boyunca sürer; bu kapanışta önceki uyarı ayrıca yeni bir suçlamaya dönüşmez (17:4).

“Vaat” sözcüğünün kendisi bir gerçekleşme garantisi taşımaz: başka bir ayette şeytanın vaadi aldatma diye nitelenir (17:64; {ar:وَمَا يَعِدُهُمُ ٱلشَّيْطَٰنُ إِلَّا غُرُورًا, tr:wa-mā yaʿiduhumu sh-shayṭānu illā ghurūrā, gloss:şeytanın vaadi aldatmadan başka değildir}). Bu karşılaştırma, yalnızca “vaat” adından doğruluk sonucu çıkarılamayacağını gösterir; 17:5'teki gerçekleşme ise vakit koşulunu izleyen sevk, içeri giriş ve kapanış hükmünden anlaşılır. Sonraki vaadin vakti anlatının zaman ufkunu genişletir, kendi olayını bu ilk vaatle birleştirmez (17:104; {ar:فَإِذَا جَآءَ وَعْدُ ٱلْءَاخِرَةِ, tr:fa-idhā jāʾa waʿdu l-ākhirati, gloss:sonraki vaadin vakti gelince}); Rabbin vaadinin yerine getirilmiş olduğunu bildiren formül ise kapanışla yankılanır (17:108; {ar:وَعْدُ رَبِّنَا لَمَفْعُولًا, tr:waʿdu rabbinā la-mafʿūlan, gloss:Rabbimizin vaadi yerine getirilmiştir}). Sondaki {ar:مَّفْعُولًۭا, tr:mafʿūlan, gloss:gerçekleştirilmiş} üzerindeki tanvin yüklemi sesçe kapatır ve tamamlanmış olayın durumunu son vurguya taşır.

</source_prose>
