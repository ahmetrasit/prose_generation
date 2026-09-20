# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:21**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.middle.claims.json`

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
- Refer to source paragraphs as `17:21 ¶N`.

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

`(17:21 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:21",
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
        "citation": "(17:21 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_21/17_21.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_21/17_21.middle.claims.json \
  --ayah-ref 17:21
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_21/17_21.prose.editorial.tr.md`

<source_prose>
17:21 bakışı önce dünyadaki bir kıyasa, sonra âhirete yöneltir: {ar:ٱنظُرْ, tr:unẓur, gloss:bak} emri kimilerinin kimilerinden {ar:كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ, tr:kayfa faḍḍalnā baʿḍahum ʿalā baʿḍin, gloss:kimini kiminden nasıl üstün tuttuğumuzu} incelemeye çağırır; ardından {ar:أَكْبَرُ دَرَجَٰتٍۢ, tr:akbaru darajātin, gloss:dereceler bakımından daha büyük} ve {ar:وَأَكْبَرُ تَفْضِيلًا, tr:wa-akbaru tafḍīlan, gloss:üstün tutma bakımından daha büyük} ölçüleriyle âhiretin daha büyük olduğunu bildirir. İlk fark gerçektir, fakat hangi ölçüte göre kurulduğu adlandırılmaz; ikinci cümle kıyası iki ayrı ölçüyle sonraki ufka taşır.

{ar:ٱنظُرْ, tr:unẓur, gloss:bak} gözle görmeyi de dikkati zihnen bir şeye verip incelemeyi de anlatır. Ardından gelen {ar:كَيْفَ, tr:kayfa, gloss:nasıl}, {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} eyleminin nedenini değil, nasıl kurulduğunu sorar. Geçmiş zamanlı Form II fiili ve birinci çoğul öznesi tercihi “Biz”e bağlayıp tamamlanmış bir eylem olarak sunar. Böylece emir yalnız iki grubu görmeye değil, aralarındaki tercihin nasıl kurulduğunu izlemeye yönelir; kıyasın ölçütü ise açık bırakılır.

İlk {ar:بَعْضَهُمْ, tr:baʿḍahum, gloss:onların bir kısmını} içindeki zamirle çoğul bir alana bağlanır, ama hangi topluluğu adlandırmaz. Ardındaki {ar:بَعْضٍۢ, tr:baʿḍin, gloss:başka bir kısım} zamirsiz ve belirsizdir; {ar:عَلَىٰ, tr:ʿalā, gloss:karşılaştırmada diğerine göre} edatından sonra mecrur gelir ve kıyasın dayanağı olur. Tam bir topluluk öteki tam toplulukla değil, aynı alanın bir kesimi başka bir kesimle karşılaştırılır. Buradaki {ar:عَلَىٰ, tr:ʿalā, gloss:karşılaştırmada diğerine göre} fiziksel olarak üstte durmayı değil, bir payı ötekine göre tartan ilişkiyi kurar.

“Bir kısım” adları parçaları gösterir; kelime ailesindeki başka bir fiil biçiminin parçalara ayırma anlamı burada bir dilbilgisi eylemi değildir. Yine de {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} fiilinin iki {ar:بَعْضَ, tr:baʿḍa, gloss:bir kısım} payını {ar:عَلَىٰ, tr:ʿalā, gloss:karşılaştırmada diğerine göre} altında kıyaslaması, ortak bir bütünün bölüşülmüş kesimleri gibi duyulur. Bu ortak-bütün imgesi paylaştırmayı sezdirir; gerçek bir bölme işlemi ya da payların hangi kaynaktan geldiğini bildirmez.

Buradaki {ar:ٱنظُرْ, tr:unẓur, gloss:bak} emri bakmayı ve dikkati yöneltmeyi anlatır; kelime ailesinin “denk karşılık” anlamı yalın eş adlarında ve belirli eşitleme ya da ikişerli sayma yapılarında görülür. Bu kıyas, eşitlik bildiren o kullanımlardan ayrılır: {ar:عَلَىٰ, tr:ʿalā, gloss:karşılaştırmada diğerine göre} altında paylar birbirine göre ölçülebilir hale gelir, fakat bu ölçülebilirlik payları eşit kılmaz.

Gösterilme ile bakma arasındaki temas bu incelemeye bir sahne kazandırır. 17:1'de {ar:لِنُرِيَهُۥ مِنْ ءَايَٰتِنَا, tr:linuriyahu min āyātinā, gloss:ayetlerimizden bir kısmını ona göstermek için} ifadesi gösterilen işaretlerden söz eder; 17:21'deki {ar:ٱنظُرْ, tr:unẓur, gloss:bak} ve {ar:كَيْفَ, tr:kayfa, gloss:nasıl} ise görünen farkı incelemeye açar. Böylece üstünlük, gösterilmiş işaretler düzeni içinde araştırılan bir karşıtlık olarak da duyulur; emir açık farkı doğrudan görmeye de çağırır. İnsanın {ar:عَجُولًا, tr:ʿajūlā, gloss:aceleci} diye nitelenmesi bu inceleme çağrısına hemen hüküm vermeyi yavaşlatan bir tempo katar (17:11): dikkat tercihin nasıl kurulduğunda kalır. Bu bağ okura özel bir azarlama kurmaz ve üstünlük farkını kendi başına ilahî onay diye açıklamaz.

Yanıltıcı karşılaştırmalar ve yoldan çıkmayla birlikte geçen {ar:ٱنظُرْ, tr:unẓur, gloss:bak} ve {ar:كَيْفَ, tr:kayfa, gloss:nasıl} kuruluşu, inceleme buyruğunun onay anlamına gelmediğini gösterir (17:48). Bu ayrı sahne 17:21'deki bakma çağrısını keskinleştirir, fakat iki ayeti aynı olay ya da sure geneline yayılan tek bir program haline getirmez. Pay kıyasının başkasına verileni istememe uyarısıyla yan yana gelişi (4:32), 17:21'deki {ar:بَعْضَهُمْ عَلَىٰ بَعْضٍۢ, tr:baʿḍahum ʿalā baʿḍin, gloss:kimini kiminden} ilişkisini hasede kapılmadan incelenebilecek toplumsal paylar olarak duyurur. Bu temas payları kopuk bütünler ya da sabit oranlar olarak kurmaz.

## Ölçü ve Ufuk

İlk ölçü olan {ar:أَكْبَرُ دَرَجَٰتٍۢ, tr:akbaru darajātin, gloss:dereceler bakımından daha büyük}, derece ve ölçekte daha önde oluşu anlatır; büyüklük burada hacim ya da karakter üstünlüğü değildir. {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} belirsiz çoğuluyla birden çok düzey açar, sayılarını, kimlere ait olduklarını ve tek tek yerlerini belirlemez. {ar:عَلَىٰ, tr:ʿalā, gloss:karşılaştırmada üstte} edatının dikey çağrışımıyla derece sözü birlikte sıralı konum ve basamak imgesi kurar. Bu, göreli yeri gösteren bir benzetmedir; gerçek merdiven ya da çıkış eylemi anlatmaz. Aşama aşama ilerleme kelime ailesinin başka biçimine aittir, çoğulun açıklığı da sonsuz sayıda derece ileri sürmez.

{ar:وَ, tr:wa, gloss:ve} bakma buyruğundan âhiret hakkındaki yeni cümleye geçerken önceki kıyasla bağı korur. {ar:وَلَلْءَاخِرَةُ, tr:wa-lal-ākhiratu, gloss:ve âhiret ise} yapısındaki belirli özne ve pekiştirme lâmı, iki yüklemin de kapsamındadır: {ar:أَكْبَرُ دَرَجَٰتٍۢ, tr:akbaru darajātin, gloss:dereceler bakımından daha büyük} ve {ar:وَأَكْبَرُ تَفْضِيلًا, tr:wa-akbaru tafḍīlan, gloss:üstün tutma bakımından daha büyük}. Böylece tek özne, birbirinin yerine geçmeyen iki eş düzeyli ölçü alır; bağlaçla yeniden başlayan ikinci “daha büyük” ifadesi dengeli, eklemeli bir duraklama yaratır. Bu ritmik denge belirli bir vezin ya da tilavet ölçüsü ileri sürmez.

İkinci yüklemdeki {ar:تَفْضِيلًا, tr:tafḍīlan, gloss:üstün tutma} serbest bir etiket değil, {ar:أَكْبَرُ, tr:akbaru, gloss:daha büyük} yargısını tamamlayan Form II mastarıdır. Tercih ve farklılaştırma işlemini, derece ölçeğini yinelemeden ikinci bir eksen olarak adlandırır. Belirsiz ve mansup mastar işlemin kapsamını açık bırakır; biçim kendi başına ne sınırsızlık ne de yoğunlaştırma bildirir. Aktarılan başka bir yorum, üstün tutulanların sayıca artmasını da düşünür; seslendirme ve ayrıntı verilmediğinden bu yorumun ölçü bakımından büyüklükle ilişkisi açık kalır.

{ar:ٱلْءَاخِرَةُ, tr:al-ākhirah, gloss:âhiret} olağan okumada dünya hayatından sonraki ufuktur; sözcüğün “ilkten sonra gelen, öteki” ilişkisi de iki {ar:أَكْبَرُ, tr:akbaru, gloss:daha büyük} yargısıyla buluşur. Sonraki ufuk hem {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} sıralamasında hem tercih ilişkisinde daha büyük görünür. Bu ardıllık, dünya ile âhiret arasındaki yönü kurar; tek başına daha aşağıda oluşu ya da aralarındaki belirli bir zaman aralığını söylemez. Başlangıçtaki {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} ile kapanıştaki {ar:تَفْضِيلًا, tr:tafḍīlan, gloss:üstün tutma} aynı kelime ailesini çerçeveye alır: fiil tercih eylemini başlatır, mastar ise onu ikinci ölçünün adı olarak yeniden duyurur.

Yalın biçimlerin çağrışımı kıyasa ikinci bir renk verir: eksikliğin karşıtı olan yüksek değer fikrinin yanı sıra, gereksinim ya da ölçüyü aşan fazlalık ve bölüşme sonrası kalan pay da bu ailede yer alır. {ar:بَعْضَهُمْ عَلَىٰ بَعْضٍۢ, tr:baʿḍahum ʿalā baʿḍin, gloss:kimini kiminden} paylarının {ar:أَكْبَرُ, tr:akbaru, gloss:daha büyük} ölçüsüyle karşılaştırılması, eşit dağılmayan bir artış imgesini çağırabilir. Bu, yalın biçimlerin katkısıdır; Form II {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} ve {ar:تَفْضِيلًا, tr:tafḍīlan, gloss:üstün tutma} biçimleri karşılaştırmalı tercih anlamını korur. Yiyecek, su, gelir ve ganimet gibi kullanımlar belirli nesnelere bağlıdır; 17:21 böyle bir nesne adlandırmadığından bu imge gerçek bir aktarım, artan nesne ya da maddi miktar hesabı vermez.

## Payların Dünyadaki Hareketi

Yükseliş ve dönüş anlatısı, dünyadaki konumların değişebilirliğini görünür kılar. Büyük yükseliş 17:4'te adlandırılır: {ar:تَعْلُنَّ عُلُوًّا كَبِيرًا, tr:taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle yükselirsiniz}. Yıkım ve yenilginin ardından geri dönüş ve yeniden destek 17:5 ve 17:6'da anlatılır. 17:6'da {ar:رَدَدْنَا, tr:radadnā, gloss:geri döndürdük} dönüşü, {ar:وَأَمْدَدْنَاكُم, tr:wa-amdadnākum, gloss:size yeniden destek verdik} mal ve çocuklardaki artışla desteğin yenilenmesini bildirir; ardından {ar:أَكْثَرَ نَفِيرًا, tr:akthara nafīran, gloss:sayıca daha kalabalık bir topluluk} sözü gelir. Yeni yıkım 17:7'de, dönüş olursa karşılığın yineleneceği koşulu 17:8'de görünür: {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:yeniden dönerseniz biz de döneriz}. Bu sıra, 17:21'deki {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} ilişkisini değişebilir dünyevî konumlar içinde duyurur. 17:7'deki {ar:وَعْدُ ٱلْءَاخِرَةِ, tr:waʿdu al-ākhirati, gloss:sonraki vaat} de 17:21'deki {ar:ٱلْءَاخِرَةُ, tr:al-ākhirah, gloss:âhiret} ile sonraki ufuk sözünü yankılar. Bu tarihsel temas değişebilirliği aydınlatır; topluluk tarihindeki koşullu dönüş, bu bağlantı içinde her dünya farkının mutlaka tersine döneceği ya da kişinin âhiret derecesini belirlediği sonucunu taşımaz.

Bu iki sahne üstün tutulmayı verilmiş imkân ve kapasiteyle birlikte düşünmeye açar. Peygamberlerden kimilerinin kimilerine göre üstün tutulmasının ardından Davud'a Zebur verilir (17:55). İnsanın onurlandırılması, karada ve denizde taşınması, iyi rızıklarla beslenmesi ve birçok varlığa göre üstün kılınmasıyla birlikte anılır (17:70). Böylece 17:21'deki {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} karşılaştırması kişinin kendi ürettiği liyakatten çok kendisine verilmiş koşullar boyutunu da kazanır. Bu bağlamda Zebur, taşınma ve rızık odak fiilin sözlük karşılığı değildir; bu örnekler de her tercihi ahlaki üstünlük ya da her dereceyi görev yapmaz.

Yakın bağlam, pay farkının yanına zaman ve yönelişi koyar. İvedi dünyayı isteyen için {ar:عَجَّلْنَا لَهُ, tr:ʿajjalnā lahu, gloss:onun için çabuklaştırırız} denir; hızlandırılacak olanın ne ve kimin için olduğu Allah'ın dilemesine bağlanır: {ar:مَا نَشَاءُ لِمَن نُرِيدُ, tr:mā nashāʾu li-man nurīdu, gloss:dilediğimizi dilediğimiz kimseye} (17:18). Buna karşılık âhireti isteyen ve onun için gereğince çabalayan kişinin çabası takdir edilir (17:19): {ar:وَمَنْ أَرَادَ الْآخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-man arāda al-ākhirata wa-saʿā lahā saʿyahā, gloss:âhireti isteyen ve onun için gereğince çabalayan}, {ar:كَانَ سَعْيُهُم مَّشْكُورًا, tr:kāna saʿyuhum mashkūrā, gloss:çabası takdir edilir}. Bu iki yöneliş ve onlara eşlik eden eylem, 17:21'deki derece farkının zaman ve davranışla birlikte okunmasına imkân verir; bu bağlam tek tek dereceleri ölçen bir çaba puanı kurmaz.

İki yönelişin tümüne uzanan destek 17:20'de sürdürülür: {ar:كُلًّا, tr:kullan, gloss:her birine} ve {ar:نُمِدُّ, tr:numiddu, gloss:desteği sürdürürüz}; Rabbin bağışı da {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} değildir. Bu ortak erişimin hemen ardından 17:21'de {ar:فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍۢ, tr:faḍḍalnā baʿḍahum ʿalā baʿḍin, gloss:kimini kiminden üstün tuttuk} payları farklılaştırır; ortak destekle farklı paylar aynı bağlamda yan yana durur. 17:19'daki amaçlı çaba ile 17:20'deki devamlı destek, kelime ailesinin aşamalı ilerleme bildiren başka biçimini de yankılayabilir: çaba ve süren destek, süreç imgesini birlikte açar. Odaktaki {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} ise bu süreçten değil düzeylerden söz eder. Böylece âhiret ölçüsü zaman, yöneliş ve eylemle birlikte duyulur; bağlantı her dereceyi doğrudan çaba puanına ya da insanları değişmez iki sınıfa çevirmez.

Rab'den {ar:فَضْلًا, tr:faḍlan, gloss:lütuf, bağış} istenmesi (17:12) ve Rabbin {ar:عَطَاءِ رَبِّكَ, tr:ʿaṭāʾi rabbika, gloss:Rabbinin bağışı} olarak anılan sunumu (17:20), ortak desteğe bir bağış yankısı ekler. Bu temas, kişinin elindeki imkândan gönüllü yarar sunma ve borçlu olmadığı bir şeyi verme nüanslarını çağırabilir; aynı sunum yaratılmış hayata genel destek olarak da okunabilir. Bu iki olasılık bağlamsal yankılardır: ortak erişimin miktarını, süresini, ilahî onayla ya da nihai konumla ilişkisini belirlemezler. Form II {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} fiili karşılaştırmalı tercih anlamını korur; “bağışlamak” onun doğrudan sözlük karşılığı değildir.

Payların toplumsal işlevi üç ayrı ayrıntıyla belirginleşir. Geçimin bölüştürülmesi derecelerle ve insanların birbirinden yararlanmasıyla birlikte görünür (43:32). Daha geniş pay alanların ellerindekini eşitleyecek biçimde aktarmaması, bu paylaşımın eşitlenmediğini somutlaştırır (16:71). Derecelerin verilen nimetler aracılığıyla sınanması ise pay farkına sorumluluk boyutu ekler (6:165). Birlikte okunduklarında bu sahneler 17:21'deki {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} ilişkisini ortak işlev, emanet ve sınanmayla ilişkilendirir; dünyevi refahı kalıcı onur ya da kişinin toplam değeri olarak belirlemez.

İnsanlar arası paylardan farklı olarak tarımsal görüntü, komşu topraklar, bağlar ve bahçelerin tek suyla sulanırken farklı ürün vermesini öne çıkarır (13:4). Bu sahne 17:21'deki {ar:بَعْضَهُمْ عَلَىٰ بَعْضٍۢ, tr:baʿḍahum ʿalā baʿḍin, gloss:kimini kiminden} kıyasını insan rütbesinin dışına taşır: ortak bir kaynak farklı sonuçlarla buluşabilir. Aynı su, bütün yetişme koşullarının özdeş olduğunu ya da bu tarımsal farkın insan topluluklarının nedenini ve değerini açıkladığını göstermez; katkısı ortak kaynak ile farklı ürün arasındaki görüntüdür.

## Derecelerden Kişisel Hesaba

Kişisel hesap görüntüsü sayımdan kişinin kendi kaydını okumasına doğru aşama aşama kurulur. Hesap ve ayrıntılandırma birlikte anılır (17:12): {ar:وَالْحِسَابَ, tr:wa-l-ḥisāba, gloss:hesabı, sayımı} ile {ar:فَصَّلْنَا تَفْصِيلًا, tr:faṣṣalnā tafṣīlan, gloss:ayrıntısıyla açıkladık}. Ardından kayıt sahibine bağlanıp açık halde önüne konur (17:13): {ar:أَلْزَمْنَاهُ, tr:alzamnāhu, gloss:ona bağladık}, {ar:كِتَابًا, tr:kitāban, gloss:yazılı kayıt}, {ar:مَنْشُورًا, tr:manshūran, gloss:açılmış, yayılmış}. Kişi kendi kitabını kendisi okur (17:14): {ar:اقْرَأْ كِتَابَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} ve {ar:بِنَفْسِكَ, tr:binafsika, gloss:kendin, kendi nefsinle}; hiçbir yük taşıyanın başkasının yükünü taşımaması bu kaydı kişisel sorumlulukta tutar (17:15). Sayımın ayrıntıya, kişiye bağlanmış kayda, okumaya ve devredilemez yüke uzanması, 17:21'deki {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} ölçeğini kişiye ait aşamalarla birlikte düşünmeye açar. Bu pasaj ölçeğinde bir benzetmedir: arada 17:16, 17:17, 17:18, 17:19 ve 17:20 bulunur.

Odaktaki {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} sıralı düzeyleri adlandırırken, kelime ailesinin başka bir biçimi katlama ve bir şeyi belge katlarının arasına yerleştirme işlemini çağrıştırır. Kişinin kaydının {ar:مَنْشُورًا, tr:manshūran, gloss:açılmış, yayılmış} halde önüne çıkması bu iki görüntüyü buluşturur (17:13): katlarda saklı ayrımlar açılan kayıtla görünür olur. Böylece kişisel hesap, açıldıkça içindeki ayrımları gösteren katlı bir belge gibi düşünülebilir. Katlanma başka biçimin katkısıdır; odaktaki isim düzeyleri anlatır, gerçek sayfaları ya da bir derece tablosunu değil.

Başka dereceler eylem, zaman ve bilgi boyutlarını ayrı ayrı görünür kılar. Her kişiye ait dereceler yapılanlarla ilişkilendirilir ve haksızlık edilmeyeceği belirtilir (46:19). Fetih öncesiyle sonrası arasında verenlerin ve mücadele edenlerin dereceleri farklıdır; her iki gruba da güzeli vaat edilir (57:10). Mecliste yer açma ve ilim ise yükseltilen derecelere katılım ve bilgi boyutunu ekler (58:11). Bu örnekler 17:21'deki âhiret ölçeğini dünya malından daha geniş, eyleme, eylemin zamanına ve bilgiyle ilişkili davranışa duyarlı kılar. Bu bağlamlar ölçüyü aydınlatır; odak ayet tek bir puanlama ya da bütün dereceleri açıklayan tek metrik vermez.

Fâtiha'da lütuf verilenlerin yolu, gazaba uğrayanlar ve sapmışların yolundan ayrılır (1:7). Bu bağımsız yol imgesi 17:21'deki {ar:دَرَجَٰتٍۢ, tr:darajātin, gloss:dereceler} ve {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün tuttuk} ile buluşunca dereceye yön ve nitelik de ekler; üstünlük böylece yalnız durulan yer gibi duyulmaz. Bu temas iki ayetteki grupları özdeşleştirmez; dünyadaki tercih de tek başına ilahî lütfun kanıtı olmaz.

Hareket eden basamak imgesinin karşısında, 17:22 başka bir ilah edinmeme uyarısının ardından suçlanmış ve desteksiz kalma duruşunu kurar: {ar:فَتَقْعُدَ, tr:fa-taqʿuda, gloss:oturup kalırsın}, {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış}, {ar:مَخْذُولًا, tr:makhdhūlan, gloss:yardımsız, terk edilmiş}. Buradaki oturuş dinlenme değil, kınanmış ve yardımsız bırakılmış bir konumdur; bu karşıtlık basamakların hareketini belirginleştirir, dağılımın kuralını açıklamaz. 7:182'deki fark ettirmeden ve kişinin bilmediği yönden adım adım götürülme ise ayrı bir hareket görüntüsüdür. Bu yankı ilerlemenin yönünün örtük kalabileceğini ekler, fakat 17:21'deki derece ilişkisini aynı sürece dönüştürmez.

Son bakış başkalarının konumundan kişinin kendi işlerine döner. İnsan kendi ellerinin önceden gönderdiği işleri görür (78:40); bu sahne 17:21'deki {ar:ٱنظُرْ, tr:unẓur, gloss:bak} buyruğuyla buluşunca karşılaştırmalı bakışı kişinin kendi yaptıklarını incelemesine doğru genişletir. Böylece odak emirdeki dikkat, kişisel sorumluluk ve öz inceleme yönü kazanır. Bu temas, kayıt biçimini, sayım yöntemini ya da her eylemle derece arasında sabit bir formülü açıklamaz.

</source_prose>
