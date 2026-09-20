# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:26**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.middle.claims.json`

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
- Refer to source paragraphs as `31:26 ¶N`.

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

`(31:26 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:26",
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
        "citation": "(31:26 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_26/31_26.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_26/31_26.middle.claims.json \
  --ayah-ref 31:26
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_26/31_26.prose.editorial.tr.md`

<source_prose>
## Önce sahibi

31:26 önce sahipliği, sonra sahibin niteliğini bildirir: {ar:لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:lillāhi mā fī es-semāwāti wa-l-arḍi, gloss:göklerde ve yerde ne varsa Allah’ındır}; ardından {ar:إِنَّ ٱللَّهَ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:inna Allāha huwa el-Ghaniyy el-Hamīd, gloss:Allah hiçbir şeye muhtaç olmayan ve övülmeye layık olandır} der. İlk cümle Allah’a ait olan alanı, ikincisi O’nun ihtiyaçsız ve övülmeye layık oluşunu öne çıkarır. İkisi de bir olay dizisi değil, kalıcı bir ilişki ve nitelik kurar.

{ar:لِلَّهِ, tr:lillāhi, gloss:Allah’a ait} sözü, neyin ait olduğunu söyleyen {ar:مَا, tr:mā, gloss:ne varsa} içeriğinden önce gelir; okur önce sahibini, sonra sahip olunanı duyar. Aitlik edatı {ar:لِ, tr:li, gloss:aitlik edatı}, özel ad {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} ile bitişerek okunuşta tek bir söz birimi oluşturur; bu, kök anlamı değil yüzeydeki morfolojik birleşmedir. Allah adı burada belirli ilahî göndergiyi gösterir, genel bir ilah sınıfı açmaz. Sahiplik ilişkisi, edatın cer yönetimiyle ve sahibin içerikten önce gelmesiyle kurulur; adın etimolojisine ya da ayrı bir ibadet eylemine uzanmaz.

Geniş ilgi zamiri {ar:مَا, tr:mā, gloss:ne varsa}, gökler ile yerde bulunan akıllı ve akılsız varlıkları sınıflara ayırmadan kapsar. {ar:فِى, tr:fī, gloss:içinde} bunları iki alanın içinde konumlandırır; kaynak ya da yüzey ilişkisi kurmaz. {ar:وَٱلْأَرْضِ, tr:wa-l-arḍi, gloss:ve yeryüzü} aynı “içinde” öbeğini tamamlayıp sahip olunan alana katılır, ikinci bir yer yargısı açmaz. Böylece kapsam, belirtilen gök ve yer alanlarının içindekileri bir araya getirir.

Belirli çoğul {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} üst kozmik alanı taşır; yükseklik çağrışımı bu alanı katmanlı duyurabilir, fakat kat sayısı belirlemez. Tekil ve belirli {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} ise karşı kutup olarak yeryüzünü tek bir geniş kütle halinde toplar; yayılım ve sağlamlık çağrışımı alt zemini duyulur kılar. Her iki ad da {ar:فِى, tr:fī, gloss:içinde} edatına bağlandığı için aynı sesli sonu alır; belirli biçimleri ve {ar:وَ, tr:wa, gloss:ve} bağlacıyla eşgüdümlenmeleri, onları tek bir işitilir üst-alt çiftine dönüştürür. Bu merizm bütün kozmik alanı kapsar: burada gökler buluta, yağmura, bitkiye ya da sayısı verilmiş katlara; yeryüzü siyasi bir ülkeye veya bir nesnenin altı, hayvan ayağı gibi başka bir tamlamaya dönüşmez.

Baştaki {ar:لِلَّهِ, tr:lillāhi, gloss:Allah’a ait} içindeki cerli {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} adı, ikinci cümlede {ar:إِنَّ, tr:inna, gloss:şüphesiz} tarafından yönetilen mansub {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} öznesi olarak aynı göndergiyi koruyarak döner; hâl ve cümle rolündeki bu değişim sahiplik bildirimini kimlik hükmüne bağlar. Eril tekil {ar:هُوَ, tr:huwa, gloss:O} zamiri de bu ada döner; ardından gelen {ar:ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:el-Ghaniyy el-Hamīd, gloss:ihtiyaçsız ve övülmeye layık} çiftini göklerde ve yerde bulunanlara değil Allah’a bağlar. İsim ile yüklemler arasındaki bu kısa zamir, bir ayırma ve ritmik duraklama işlevi görür; geciken iki nitelik odaklı bir kimlik hükmü olarak iner. Tek bir “şüphesiz” iki yüklemi de kapsar; fiilsiz cümle onları olay değil, aynı özneye bağlı kalıcı vasıflar olarak sunar.

Sahiplik bildiriminden hemen önce aynı {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} ve {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} çifti 31:25’te {ar:مَنۡ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:man khalaqa es-semāwāti wa-l-arḍa, gloss:gökleri ve yeri kim yarattı?} sorusuna konu olur; cevap da {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāh, gloss:elbette Allah derler} diye sesle verilir (31:25). Bu çiftteki yeryüzü, yaşadığımız alt alanı Allah’a ait olanların içinde tutar (31:25). Ardından {ar:قُلِ ٱلْحَمْدُ لِلَّهِ, tr:quli l-ḥamdu li-llāh, gloss:de ki, hamd Allah’a mahsustur} buyruğu gelir (31:25). Sesle verilen yaratıcı cevabı, 31:26’da varlığın kime ait olduğu ve sahibin neden övgüye layık bulunduğu bildirimine bağlanır: {ar:لِلَّهِ مَا فِى, tr:lillāhi mā fī, gloss:içinde olanlar Allah’a aittir} sahipliği söylerken, {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} övgüyü Allah’ın kalıcı niteliği yapar. Cevabın ve hamd buyruğunun sesle dile getirilişi, övgüyü 31:25’teki talimattan odaktaki son nitelik olan {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} sıfata taşır; hamd buyruğundaki eylem bu sıfatın kendisi değildir (31:25). Çoğunluğun {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūn, gloss:bilmiyorlar} diye anılması, doğru cevabı dillendirmekle onu tam kavramak arasında mesafe bırakır (31:25); bu sahnede {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliği de insanın söyleyişine veya kavrayışına bağlı olmayan bir özellik olarak belirir (31:25). Yaratma, söyleme ve bilmeme çevresindeki daha ince kelime temasları, 31:25’in soru-cevap ve övgü bağlamından gelen ihtiyatlı yankılardır; bağımsız sözlük anlamları olarak doğrulanmış değildir. 31:26 ise kendi başına sahiplik ve nitelik bildirir (31:25).

## İhtiyaçsızlık ve övgü

İlk belirli merfû yüklem {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız}, Allah’ın hiçbir şeye muhtaç olmadığını bildirir; sözcük maddi bolluk alanına da değse de buradaki anlamı sıradan servet sahibi olmaktan çok içkin yeterliliktir. Göklerin ve yerin O’na ait oluşu, sahibin bu toplam sayesinde zenginleştiği bir edinim değildir: sahiplik zaten ihtiyaçsız olanın sahipliği olarak kurulur. Arapçadaki faʿīl sıfat kuruluşu bu niteliği geçici değil kalıcı kılar; kullanılan biçimin kendisi başkasını yeterli yapan ettirgen bir eylem anlatmaz. Hemen gelen {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık}, bağımsız bir tetikleyici olarak, ihtiyaçsızlığa başkalarının ihtiyacını gideren ve beklenen işlevi yerine getirip yarar sağlayan yeterlik yönünü de açabilir; bu, Allah’a ihtiyaç yüklemeden yerel yüklem çiftinden çıkan mümkün bir ilişkisel okumadır. İkinci nitelik, sağlanan yararın deneyim ya da sınamadan sonra övülesi bulunmasını da duyurabilir; ayet yararlanıcıyı, övgüde bulunanı veya açık bir sınamayı adlandırmadığından bu bağlantılar ihtimal sınırında kalır.

İkinci belirli merfû yüklem {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık}, Allah’ı övgüye layık diye niteler; bir övme eylemi veya yalnızca övgü almış edilgen bir durum anlatmaz. İki kelime de aynı faʿīl sıfat kuruluşunda, aynı özneye bağlı kalıcı niteliklerdir; bu ikinci yüklem son işitilen niteliğe dönüşür ve cümleyi tamamlar, sonradan eklenmiş bir süs değildir. Övülmeye layıklık elindeki varlıklardan doğmaz; fiilen övgü söylenmesine ya da sağlanan yararın karşılık olarak geri dönmesine de bağlı değildir. Sözcük, övgüye layık çok sayıda niteliğe sahip olma yönünü de açar; ayet bunların listesini vermez. Ayetin başındaki {ar:لِلَّهِ, tr:lillāhi, gloss:Allah’a ait} ile sonundaki {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık}, 31:26’yı sahiplikten övgüye layıklığa çerçeveler; bu bağ sözcük sırasıyla sınırlıdır.

Bu çiftin sesi de kapanışta iş görür: {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} sonundaki çift ses, daha uzun {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} biçimini hazırlar ve bitişi sıkılaştırır; bu tını ilişkisi iki sözcüğün yerel ses düzeniyle sınırlıdır. Aynı kök ailesinde insan sesiyle ezgi söyleme ve dinleme kullanımı da bulunur; buradaki belirli sıfat biçimi ise ihtiyaçsızlık niteliğidir. Yanındaki {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} ve eşleşen tını, o ayrı kullanımı ancak hafif, keşifsel bir ses yankısı olarak duyurur; cümle bir şarkı söyleme olayı anlatmaz.

İhtiyaçsızlık ve övgü, insanın verdiği karşılıktan bağımsız kalır. 31:12’de {ar:يَشْكُرُ, tr:yashkuru, gloss:şükreder} iyiliği tanıyıp sahibine teşekkür etmeyi, {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi lehine} ise şükrün yararının özneye dönmesini gösterir; {ar:كَفَرَ, tr:kafara, gloss:nankörlük eder ve iyiliği örter} iyiliğin örtülmesini verende bir azalma değil, alan kişinin tanımasının kapanması olarak duyurur. Ardından gelen {ar:غَنِيٌّ حَمِيدٌۭ, tr:ghaniyyun ḥamīdun, gloss:ihtiyaçsız ve övülmeye layık} çifti iki yanıt boyunca da yerinde kalır (31:12). Aynı çift bütün yeryüzünün inkârı sonrasında da sürer (14:8); şükür sınamasında yararın yine şükredene dönmesi ve Rabbin ihtiyaçsız oluşu da bu yönü tamamlar (27:40). Bu ayetlerdeki bağ, şükür sözcüğünün ayrı bir sözlük tanımından değil yararın kime döndüğünden kurulur; 31:12’de kapanış çifti uyarı işlevini de korur (31:12, 14:8, 27:40). Böylece insanın şükrü insanın kendi lehine işlerken Allah’ın niteliği insan karşılığına bağlı kalmaz (31:12, 14:8, 27:40): {ar:ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:el-Ghaniyy el-Hamīd, gloss:ihtiyaçsız ve övülmeye layık}.

Bu bağımlılık farkı 35:15’te açıkça kurulur: {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ, tr:antumu al-fuqarāʾu ilā Allāh, gloss:Allah’a muhtaçsınız} denir, ardından {ar:وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:wa-Allāhu huwa el-Ghaniyy el-Hamīd, gloss:Allah ihtiyaçsız ve övülmeye layıktır} gelir (35:15). Bu açık karşıtlıkta insanlar O’na muhtaç, O ise onlara muhtaç değildir; {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliği bağımlı insanlarla ilişki içinde derinleşir (35:15). Bu, 31:26’daki her varlığın ayrıca muhtaç olduğu sonucunu taşımaz (35:15). 22:64’teki {ar:لَّهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ, tr:lahu mā fī s-samāwāti wa-mā fī l-arḍi, gloss:göklerde ve yerde olanlar O’nundur} ifadesi, odaktaki {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} ile {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} üst-alt sahipliğini yineler ve hemen {ar:ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:el-Ghaniyy el-Hamīd, gloss:ihtiyaçsız ve övülmeye layık} çiftine geçer (22:64). Bu yüzey tekrarı ihtiyaçsızlık ve övgüyü kozmik sahipliğin yorumlayıcı kapanışı yapar; tek bir paralel türeme ya da kapsamlı bir sistem iddiası kurmaz (22:64).

## Gizli olan ve sağlanan yarar

Gökler ve yeryüzü kapsamı, küçük ve saklı bir nesnenin nerede bulunabileceğiyle somutlaşır (31:16). {ar:مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:mithqāla ḥabbatin min khardalin, gloss:bir hardal tanesi ağırlığınca} ölçüsü belirsiz küçüklüğü belirli bir ölçüye indirir; söz konusu {ar:حَبَّةٍ, tr:ḥabbatin, gloss:tohum}, sert bir örtü gibi duran {ar:فِى صَخْرَةٍ, tr:fī ṣakhratin, gloss:bir kayanın içinde}, göklerde veya yeryüzünde bulunabilir (31:16). Böylece kayanın sertliğiyle üst ve alt kozmik kutuplar, küçücük nesnenin saklanabildiği ayrı somut yerler olur (31:16). {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā Allāh, gloss:Allah onu getirir} gizli olanın geri çıkışına yön ve son nokta verir; {ar:لَطِيفٌ, tr:laṭīfun, gloss:ince ve gizli olana nüfuz eden} neredeyse algılanmayan inceliği, {ar:خَبِيرٌۭ, tr:khabīr, gloss:her şeyin içyüzünden haberdar} ise içten bilgiyi bu erişim imgesine katar (31:16). Bu sahne, sahip olunan alanın içindeki gizliyi bulup geri getirebilme imkânını da duyurur; “geri getirmek” sahiplik sözünün anlamına dönüşmez ve 31:16’nın yalnız kuşatıcı bilgiyi anlatan okuması da açık kalır (31:16).

Gizlinin erişilebilir oluşundan ayrı bir bağlamda, gökler ve yeryüzü insan kullanımına açılır (31:20). {ar:سَخَّرَ لَكُم, tr:sakhkhara lakum, gloss:sizin kullanımınıza sundu} üst alanı ve yeryüzünü amaca yöneltilmiş kullanıma verir; odaktaki {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} ile {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} bu hizmet ilişkisinin iki kutbudur (31:20). Ardından nimetlerin bolca tamamlanması ({ar:أَسْبَغَ عَلَيْكُمْ نِعَمَهُۥ, tr:asbagha ʿalaykum niʿamahu, gloss:nimetlerini üzerinize bolca tamamladı}) ve görünürle içte kalanın birlikte anılması ({ar:ظَاهِرَةًۭ وَبَاطِنَةًۭ, tr:ẓāhiratan wa-bāṭinatan, gloss:açık ve gizli}) yararın tamamlandığını ve görünene indirgenmediğini gösterir (31:20). Bu kullanım ve nimet sahnesi sahipliği alıcıya dönük kapsamlı bir yarar olarak da duyurur; {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliğinin ihtiyacı karşılayan, yeterli olma yönüyle teması, 31:20’de egemenliğin öne çıktığı okumayla birlikte durur (31:20).

Sınırlı kaynakların karşısındaki tükenmeyen kelimeler başka bir ölçeğe taşır (31:27). Yeryüzündeki ağaçlar {ar:أَقْلَٰمٌۭ, tr:aqlām, gloss:kalemler} olur; odaktaki {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} bu sahnede yaşadığımız alt alan ve yazı araçlarının maddi zemini olarak belirir (31:27). Kalem, hazırlanmış bir yazı aracını, hatta sazdan yapılmış kalemi çağrıştırabilir (31:27). Deniz ve arkasından gelen yedi deniz, bu kez çok büyük ama yine maddi bir yazı ortamı sağlar ({ar:وَٱلْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:wa-l-baḥru yamudduhu min baʿdihi sabʿatu abḥur, gloss:denizi ardından yedi deniz daha beslese}) (31:27). Ağaçların kalemleriyle denizin çoğalan mürekkebi karşısında Allah’ın {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu-llāh, gloss:Allah’ın kelimeleri} benzetmenin maddi olmayan çıktısıdır; bunlar tükenmez ({ar:مَّا نَفِدَتْ, tr:mā nafidat, gloss:tükenmez}) (31:27). Araçlar çoğalıp deniz yeniden beslense bile yaratılmış yazı düzeninin bir sınırı vardır; bu karşıtlık {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliğini sonlu bir ifade kaynağına bağımlı olmama yönünde genişletir (31:27). Bu yazı imgesi, Allah’ın kelimelerinin ölçüsünü özellikle görünür kılıyor olabilir; {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} ile bu ölçü arasında kurulan imgesel bağ sıfatın olağan anlamını değiştirmez (31:27). Kalem, su ve tükeniş çevresindeki daha ince kelime temasları bağımsız sözlük karşılıkları değil, aynı yazı imgesinin uzantılarıdır (31:27).

## Görünür iz ve büyüme

Büyüme sahnesi yazı araçlarının maddi sınırından ayrı bir imge açar: gökten gelen su yerde bitki yetiştirir ve yaratılıştaki yararı görünür kılar (31:10). Yağmurun bitkiyi yerde görünür kılması, odaktaki {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} için biçimce uzak ve araştırıcı “başka nesnelerden ayıran görünür fiziksel iz” çağrışımını tetikleyebilir; gökler olağan üst âlemler anlamını korur (31:10). Bu su ve büyüme bağlamı, {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} sözcüğünü yumuşak, verimli ve bitki yetiştiren alıcı toprak olarak belirginleştirir; olağan yeryüzü anlamı sürer ve bu özellik genel bir sözlük anlamına dönüşmez (31:10). Gökten su ve ardından bitki yetişmesi dizisi ({ar:ٱلسَّمَآءِ, tr:es-samāʾi, gloss:gökten}; {ar:مَاءًۭ فَأَنبَتْنَا فِيهَا, tr:māʾan fa-anbatnā fīhā, gloss:su ve ardından orada bitki yetiştirdik}) bu biçimce uzak okumada toprağı bitkilendiren yılın ilk yağmurunu ve yerde bıraktığı görünür izi düşündürür; bu ilk-yağmur çağrışımı da her bağlam için sözlük anlamı değil, bağlama özgü bir imgedir (31:10). Büyüme deneyiminin ardından {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} niteliğinin övülesi bulunma yönü de duyulur; bu yankı bir sınama fiiline dönüşmez (31:10). Gök ve yeryüzü olağan anlamlarını korur; biçimlerinden ayrıca bir eşleştirme çıkarılmaz ve 31:10 ek imge olmaksızın da yaratılış işaretlerini anlatır (31:10).

## Göklerin çevrimi ve hakikat

Büyüme sahnesinden ayrı bir ölçekte, odaktaki {ar:ٱلسَّمَٰوَٰتِ, tr:es-semāwāti, gloss:gökler} 31:29’da gece, gündüz, güneş ve ayın hareket ettiği üst alanı bildirir (31:29). Güneş ile ayın belirlenmiş bir süreye kadar akıp gitmesi ({ar:كُلٌّۭ يَجْرِىٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:kullun yajrī ilā ajalin musammā, gloss:her biri belirlenmiş bir süreye kadar akıp gider}) gökleri durağan bir liste olmaktan çıkarır ve devreleri belirli bir sona bağlar (31:29). Gök sözcüğünün olağan üst-âlem anlamı sürerken, sözlük alanındaki ad ve adlandırma yüzü de yalnız dil düzeyinde duyulabilir; “adı konmuş, belirlenmiş süre” ifadesi bu yüzü tetikleyerek çevrimi adsız değil belirlenmiş kılar (31:29). Bu, göğün olağan ya da fiziksel yükselme anlamını değiştirmeyen ihtiyatlı bir dilsel yankıdır (31:29). Gece karanlık, gündüz ışığın açıldığı karşılıklı fazdır; gecenin gündüzün, gündüzün gecenin içine sokulması ({ar:يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ, tr:yūliju al-layla fī an-nahār wa-yūliju an-nahāra fī al-layl, gloss:geceyi gündüzün içine, gündüzü gecenin içine sokar}) iki fazı süren bir sürece dönüştürür (31:29). Böylece odaktaki üst alan sonlu çevrimler içinde canlılaşır; 31:29 Allah’ın kozmik yönetimini de bağımsız olarak anlatırken, gökler ile belirlenmiş süre arasındaki adlandırma bağı ihtiyatlı bir yankı olarak kalır (31:29).

Hareketli göklerden başka bir soruya geçilir: ne gerçektir, kime yönelinir? Allah {ar:ٱلْحَقُّ, tr:el-Haqq, gloss:gerçek ve sabit olan}, O’ndan başka çağrılanlar ise {ar:ٱلْبَٰطِلُ, tr:el-bāṭil, gloss:boş ve geçersiz olan} diye karşılaştırılır (31:30). {ar:مَا يَدْعُونَ مِن دُونِهِ, tr:mā yadʿūna min dūnihi, gloss:O’ndan başka çağırdıkları} hem çağrılma eylemini hem de Allah’tan ayrı tutulmayı gösterir; böylece karşılaştırma rakip iddianın hem çağrılışını hem Allah’tan ayrılışını görünür kılar (31:30). Kapanıştaki {ar:ٱلْعَلِىُّ ٱلْكَبِيرُ, tr:el-ʿAliyy el-Kabīr, gloss:yüce ve büyük olan} aşkın üstünlüğü vurgular. Odaktaki sahiplik ve {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliği bu Hak-bâtıl karşıtlığında mülkiyet bildiriminden Allah’ın bağımsız gerçeklikte rakipsiz oluşuna doğru genişler; O tek bağımsız malik olarak duyulur (31:30). Bu, açık Hak-bâtıl ve aşkınlık karşıtlığından doğan ihtiyatlı bir ilişkisel yankıdır; 31:30’un putlara yöneltilen çağrıyı ele alan açık anlamı da sürer (31:30).

## Nimetten krize

Gerçeklik karşıtlığından sonra dikkat denizde ilerleyen gemilere döner: Allah’ın nimetiyle yol alırlar ve işaretleri çok sabreden, şükreden kişiler görür ({ar:بِنِعْمَتِ ٱللَّهِ, tr:bi-niʿmati-llāh, gloss:Allah’ın nimetiyle}; {ar:صَبَّارٍۢ شَكُورٍۢ, tr:ṣabbārin shakūr, gloss:çok sabreden ve şükreden}, 31:31). Bu sahne, odaktaki {ar:ٱلْحَمِيدُ, tr:el-Hamīd, gloss:övülmeye layık} için somut bir şükür zemini sunar (31:31). Hamd, yerginin karşıtı olan övgüdür ve iyilik karşısında teşekkürü de kapsayabilir. Gemi sahnesi minneti somutlaştırır; bu bağlamda sıfat “teşekkür edilen” anlamına daralmaz ve her övgü de teşekkür değildir (31:31).

Deniz imgesi bu kez yolcuları üstten kuşatan dalgaya dönüşür: örtüler gibi yükselen {ar:مَوْجٌۭ كَٱلظُّلَلِ, tr:mawjun ka-ẓ-ẓulal, gloss:örtüler gibi dalgalar} bir tavan hissi verir, birbirine karışan hareketi alışılmış denetimi dağıtır (31:32). Bu tehlike, odaktaki {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliğini korurken yaratılmışların kendi başlarına yetemeyişini karşısına koyar (31:32). Yolcular ortaklık ihtimallerini bırakıp yalnız Allah’a yönelirler ({ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu d-dīn, gloss:dini yalnız O’na özgü kılarak Allah’a yalvardılar}); ardından kurtarılıp karaya çıkarılmaları ({ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā al-barr, gloss:onları karaya çıkararak kurtardı}) ihtiyacın karşılanmasının olumlu yüzünü gösterir (31:32). Bu yeterlik ilişkisi, kendi başına yetemeyen yolcuların kriz ve kurtuluş sahnesinden doğan bağlamsal bir karşıtlıktır; {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} için doğrudan sözlük karşılığı değildir (31:32). Güvenliğe çıkanların bir kısmı sonradan işareti inkâr edebilir; kriz anındaki yönelişin sonradan örtülmesi, herkesin daima samimi kaldığı anlamına gelmediğini de gösterir (31:32).

## Kişinin sınırı

Krizde açığa çıkan bağımlılığın yanına, bir başkasının en yakın bağda bile kişinin yerini alamaması gelir (31:33). Ayet, bir babanın evladı adına, bir evladın da babası adına {ar:شَيْـًٔا, tr:shayʾan, gloss:hiçbir şeyi} karşılayamayacağını iki yönde bildirir; en yakın ebeveyn-çocuk bağı bile birinin ötekine yetmesine veya onun yükünü devralmasına imkân vermez (31:33). Bu en yakın ebeveyn-çocuk bağı, {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} ile başkası için yeterli olma ya da onun yerini tutma arasında ilişkisel bir yankı kurabilir; Arapçada bu anlamlar ilişki kuran kullanımlarda görünür. {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} 31:26’da olağan anlamıyla ihtiyaçsızlığı bildirir ve böyle bir tamamlayıcı almaz; bu nedenle yeterlik yönü 31:33’ün bağlamından duyulur (31:33). Başkası için yeterli olma yankısı en yakın bağda sınırını gösterir; 31:33 aynı zamanda hesap sorumluluğuna dair bir uyarı olarak okunabilir ve bağlamsal ilişki bu anlamın yerini almaz (31:33).

Ardından soru, bir başkasının senin yerine ne yapabileceğinden insanın kendi yarınını bilip bilemeyeceğine kayar (31:34). Her kişi yarın ne kazanacağını ve hangi yerde öleceğini bilmez ({ar:مَاذَا تَكْسِبُ غَدًۭا, tr:mādhā taksibu ghadan, gloss:yarın ne kazanacağı}; {ar:بِأَىِّ أَرْضٍۢ تَمُوتُ, tr:bi-ayyi arḍin tamūt, gloss:hangi yerde öleceğini}) (31:34). Buradaki yeryüzü, odaktaki {ar:ٱلْأَرْضِ, tr:el-arḍi, gloss:yeryüzü} gibi Allah’a ait kozmik alanın içindedir; burada ise insanın bilmediği belirli ölüm yerini, ölüm de son olayı gösterir (31:34). Her bir {ar:نَفْسٌۭ, tr:nafs, gloss:her bir benlik} öznesinin iki paralel cümlede yinelenmesi, yarınki kazanç ve ölüm yeri sınırını topluluğa değil tek tek kişilere bağlar (31:34). Saatin bilgisi Allah’ın katındadır ({ar:عِندَهُۥ عِلْمُ ٱلسَّاعَةِ, tr:ʿindahu ʿilmu s-sāʿa, gloss:saatin bilgisi O’nun katındadır}); insan kendi yararını önceden bilemezken odaktaki {ar:ٱلْغَنِىُّ, tr:el-Ghaniyy, gloss:ihtiyaçsız} niteliğiyle bu sınır arasında bir karşıtlık kurulur (31:34). Odaktaki yeryüzü, Allah’a ait kozmik alan anlamını koruyarak 31:34’te insanın bilmediği yarınki kazanç ve ölümün son mekânıyla temas eder; bu zamansal ve bilgisel genişleme ihtiyatlı bir bağlamsal okumadır, ayetin bilinen ve bilinmeyenleri ayrı ayrı sayan uyarısı da sürer (31:34).

</source_prose>
