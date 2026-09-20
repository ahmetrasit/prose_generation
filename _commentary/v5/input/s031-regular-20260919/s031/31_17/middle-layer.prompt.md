# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:17**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.middle.claims.json`

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
- Refer to source paragraphs as `31:17 ¶N`.

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

`(31:17 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:17",
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
        "citation": "(31:17 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_17/31_17.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_17/31_17.middle.claims.json \
  --ayah-ref 31:17
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_17/31_17.prose.editorial.tr.md`

<source_prose>
Luqman’ın {ar:يَٰ, tr:yā, gloss:ey} çağrısı, hemen ardından gelen {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} hitabıyla tamamlanır. Önce çağrının, sonra oğulun duyulması ilk buyruğa varmadan muhatabı işittirir; bu ses sırası 31:17’nin kendi akışında ilk buyruğa hazırlayan bir ritim oluşturur. Şefkatli küçültme ve iyelik gerçek baba-oğul bağını taşır. Yakınlık yükümlülüğü hafifletmez: tekil emirler aynı oğula yönelir ve doğrudan güçlerini korur. Zincir, {ar:أَقِمِ ٱلصَّلَوٰةَ, tr:aqimiṣ-ṣalāta, gloss:namazı kur}, {ar:وَأْمُرْ بِٱلْمَعْرُوفِ, tr:waʾmur bi-l-maʿrūf, gloss:iyiliği emret}, {ar:وَٱنْهَ عَنِ ٱلْمُنكَرِ, tr:wa-nha ʿani-l-munkar, gloss:kötülükten sakındır} ve {ar:وَٱصْبِرْ عَلَىٰ مَآ أَصَابَكَ, tr:waṣbir ʿalā mā aṣābaka, gloss:başına gelene sabret} buyruklarıyla ilerler; her bağlayıcı yeni ve tamamlanmış bir eylem ekler, sonuncu ilk üçünün tâbii olmaz.

Bu oğul hitabı, görev zinciriyle birlikte bir yetişme imgesi de taşır. {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} sözcüğünün aynı kök alanındaki parçaları bir araya getirip ayakta duran bir bütün kurma kullanımı, namazı kurma, iyiliği yöneltme, yanlışı durdurma ve geleni taşıma görevleriyle etkinleşir: şefkatli sesleniş ile talepkâr eğitim yan yana gelir. Hitap gerçek çocuğa yönelir; böylece biçimlenme çağrışımı, sözcüğün “oğulcuğum” anlamını koruyarak bu aile yakınlığının içine yerleşir.

## Namazı kurmak ve sürdürmek

İlk buyrukta ettirgen çekimdeki {ar:أَقِمِ, tr:aqim, gloss:ikame et} fiili belirli nesnesi {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz} olan bir eylem kurar. Muhatap yalnızca dik durmaya değil, ayakta durma, eğilme, yere kapanma, dua ve yüceltme bölümleri bulunan düzenli tapınmayı kurup sürdürmeye çağrılır. Nesnenin belirliliği adı konmuş bu uygulamayı öne çıkarır. Buradaki ses bağı yeni bir buyruk değil, nesneye geçiştir: buyruğun sonundaki kesra ardından gelen adın başındaki ünsüz kümesini tilavette açar ve namazı ses akışı içinde emre bağlar.

Namaz nesnesi, {ar:أَقِمِ, tr:aqim, gloss:ikame et} fiilinin kök alanındaki doğrultuyu koruma, denge ve sapmama kullanımlarını da harekete geçirir. Böylece kurulan ibadet, yönünü koruyan ve zaman içinde sürdürülen bir disiplin gibi duyulur; fiilin işi gözetip devam ettirme kullanımı da namazı muhataba emanet edilmiş bir pratik olarak gösterir. Belirli bir nesneyle başlaması zincire soyut bir iyi dilekten çok, kararlılıkla girişilen somut bir iş tonu verir. Bu bakım yankısı, burada namaz pratiğinin gözetilip sürdürülmesine katkı verir; kişileri yönetme buyruğu kurmaz. Aynı namazı ikame etme yapısının bir topluluk için yeniden kullanılması, kişisel buyruğu daha geniş bir ibadet pratiğine bağlar: {ar:يُقِيمُونَ ٱلصَّلَوٰةَ, tr:yuqīmūna aṣ-ṣalāta, gloss:namazı ikame ederler} ve {ar:وَيُؤْتُونَ ٱلزَّكَاةَ, tr:wa-yuʾtūna al-zakāh, gloss:zekâtı verirler} toplulukla birlikte anılır (31:4). Zekât verme bu namazdan ayrı bir eylemdir; zekâtın artış ve yararın dışa taşması çağrışımı, namaz pratiğine ancak benzetme düzeyinde eşlik eder. Bu topluluk tasviri, namaz pratiğinin daha geniş toplulukta yinelendiğini aydınlatır; 31:17’deki sonraki görevlerin veya sabrın nedeni olarak okunmaz.

## Tanınan iyi, geri çevrilen yanlış

Namaz buyruğundan sonra gelen {ar:وَأْمُرْ بِٱلْمَعْرُوفِ, tr:waʾmur bi-l-maʿrūf, gloss:iyiliği emret} ayrı ve aynı düzeyde bir tam emirdir. {ar:وَ, tr:wa, gloss:ve} bağlayıcısı onu önceki eyleme tâbi kılmaz; sonraki emirlerde yinelenerek dört buyruğu bir zincirde tutar, her birini kendi işi olarak bırakır. İlk fiil kalıbındaki {ar:أْمُرْ, tr:uʾmur, gloss:emret} doğrudan yapmaya yönelten bir istem taşır; ardından gelen {ar:بِ, tr:bi, gloss:ile} harfi bu yöneltmeyi belirli içeriğe, {ar:ٱلْمَعْرُوفِ, tr:al-maʿrūf, gloss:tanınan iyilik}e bağlar. Böylece buyruk, açık uçlu bir söyleme değil, adı konmuş iyiliği öne çıkarmaya yönelir. Namazla başlayan zincir, burada kişinin ibadetinden başkasına dönük kamusal ahlaki göreve açılır; bu anlamlı genişleme buyrukların sebep-sonuç sırası değil, okuyuş yönüdür.

Edilgen ortaç biçimindeki {ar:ٱلْمَعْرُوفِ, tr:al-maʿrūf, gloss:tanınan iyilik} konuşanın o anda icat ettiği bir tercihten çok tanınabilir ve benimsenebilir bir ahlaki içeriği anlatır. İz ya da belirti aracılığıyla tanıma yankısı, bu iyiyi ortak davranış içinde okunabilir bir ölçü gibi duyurur; bu bağlantı fiziksel bir işaret aramaz. İyiliğin düşünerek ya da bağlayıcı ölçülerce iyi sayılması da emretme görevine bilinçli bir yön verir. Bu bağlantıda tanınabilirlik ortak beğeniye indirgenmez; bu ölçü bütün ahlaki ihtilafları çözen kapsamlı bir kuralname olarak da sunulmaz. {ar:أْمُرْ, tr:uʾmur, gloss:emret} fiilinin öğüt alma ve karşılıklı danışma yönündeki kullanımı bu düşünülmüşlüğü artırır: eylem mekanik bir tepki gibi kalmaz; buyruk tanımadan eyleme geçişi düşünülmüş kılar.

Karşı kutuptaki {ar:ٱلْمُنكَرِ, tr:al-munkar, gloss:yadırganan kötülük} de belirli edilgen ortaçtır ve ahlaken reddedilen davranışı adlandırır. Tanınan iyinin karşısındaki bu yanlış, ortak etik düzenin dışında kalmış gibi duyulabilir; kökün tanınmama, kabul etmeme ve yabancılaşma yankısı bu karşıtlığı derinleştirir. Bu yankı ahlaki kötülük anlamına eşlik eder; sözcüğü bilgisizliğe ya da fiziksel tanınmazlığa indirgemez. {ar:ٱنْهَ, tr:anha, gloss:yasakla} fiilinin olağan işi durdurmak ve yasaklamaktır; ardından gelen {ar:عَن, tr:ʿan, gloss:-den uzak} harfi yanlış davranıştan ayrılma yönünü kurar. İyiliği emretmedeki {ar:بِ, tr:bi, gloss:ile} yaklaşmayı, kötülükten sakındırmadaki {ar:عَن, tr:ʿan, gloss:-den uzak} uzaklaşmayı belirginleştirir; yapıcı teşvik ile koruyucu sınır aynı kamusal sorumluluğa katılır, fakat tek eyleme erimez.

Nehyin son nokta ya da sınır bildiren kullanımı, {ar:ٱنْهَ عَنِ ٱلْمُنكَرِ, tr:anha ʿani-l-munkar, gloss:kötülükten men et} yapısındaki uzaklaşma ilişkisiyle buluşunca yasağı kötülüğe karşı çizilmiş bir çizgi gibi duyurur. Sınır fiziksel bir uç değil, adı konmuş davranıştan alıkoyan ahlaki ayrımdır. Tanınan iyiyle reddedilen yanlış arasındaki seçme ve kötüyü fark edip ondan sakındırma anlamı da nehyin sağduyulu yargı yönünü açar. Buradaki yankı ahlaki ayırımı anlatır; ayette akıl ayrı bir özne olarak adlandırılmaz ve nehy fiili “akletmek” anlamına gelmez.

Bu ölçünün tanınması kendiliğinden gerçekleşmez. {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahw al-ḥadīth, gloss:oyalayıcı söz} dikkati başka yöne çeker; yinelenen söylem dağılmanın kanalına dönüşür ve Allah’ın yolundan saptırma amacı açıkça belirtilir: {ar:لِيُضِلَّ عَن سَبِيلِ ٱللَّهِ, tr:li-yuḍilla ʿan sabīli Allāh, gloss:Allah’ın yolundan saptırmak için} (31:6). Ayetler okunurken kişinin {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onları duymamış gibi} davranması, {ar:كَأَنَّ فِيٓ أُذُنَيْهِ وَقْرًا, tr:ka-anna fī udhunayhi waqran, gloss:sanki kulaklarında ağırlık varmış gibi} benzetmesiyle genişler (31:7). İşitme burada sesin kulağa ulaşmasından öte, anlayıp karşılık vermeyi de içerir. Bu yüzden {ar:ٱلْمَعْرُوفِ, tr:al-maʿrūf, gloss:tanınan iyilik}in tanınıp benimsenmesi dikkat ve kabulün yarıştığı bir alanda gerçekleşir; {ar:ٱلْمُنكَرِ, tr:al-munkar, gloss:yadırganan kötülük}in reddedilme yönü de bu sahneye temas eder, fakat yanlış salt bilgisizlik değildir. Bu iki sahne odaktaki buyrukların nedeni değil, kamusal yöneltmenin karşılaşabileceği sınırlı örneklerdir: doğru içeriğin kabulü dikkat ve dirençle yarışır. Bu bağ yanlışı bütünüyle söze bağlamaz ve her dinleyici için tek bir yöntem belirlemez. Doğru içerik tek başına kabulü güvenceye almadığından, {ar:وَٱصْبِرْ, tr:waṣbir, gloss:sabret} kamusal iyiyi dile getirme çabasını sürdürmenin parçası olarak da okunabilir.

## Yakınlık içinde ahlaki sınır

Kabul ve direnç sorusu, aile ilişkisi içinde somutlaşır. Anne-babanın oğullarını Allah’a ortak koşmaya zorlaması karşısında bu isteğe uyulmaz; ardından gelen iyilikle yoldaşlık buyruğu ilişkiyi sürdürür (31:15). Odaktaki {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} hitabı ve babadan oğula öğüt de bu kuşak bağını taşır (31:13, 31:17). {ar:وَإِنْ جَاهَدَاكَ عَلَىٰ أَنْ تُشْرِكَ بِي, tr:wa-in jāhadāka ʿalā an tushrika bī, gloss:seni Bana ortak koşmaya zorlarlarsa} baskıyı, {ar:وَصَاحِبْهُمَا فِي الدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī d-dunyā maʿrūfan, gloss:dünyada onlarla iyilikle yoldaşlık et} ise devam eden beraberliği adlandırır (31:15). Yanlış isteği reddetmek ilişkiyi terk etmeyi gerektirmez; {ar:ٱلْمَعْرُوفِ, tr:al-maʿrūf, gloss:tanınan iyilik} bu sahnede yalnız başkasını düzeltme değil, ilişkiyi iyilikle sürdürme ölçüsü olarak da görünür. Bu temas aile bağında belirgindir; burada görülen ilişki ölçüsünü diğer bütün ilişkilere genellemek ihtiyat ister ve odaktaki emirlerin kendi yükümlülüğünü kaldırmaz. Burada direnç ve devam eden bakım aynı ahlaki çizginin iki parçası olarak yan yana durur.

İyiliği yöneltmenin tarzı da ölçü altındadır. Yanağı insanlardan kibirle çevirmeme uyarısı (31:18), ölçülü yürüme ve sesi alçaltma öğütleriyle sürer (31:19). {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-n-nās, gloss:insanlara yanağını kibirle çevirme}, {ar:وَاقْصِدْ فِي مَشْيِكَ, tr:waqṣid fī mashyika, gloss:yürüyüşünde ölçülü ol} ve {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghuḍḍ min ṣawtika, gloss:sesini alçalt} farklı davranışlara ayrı sınırlar koyar. {ar:أَقِمِ, tr:aqim, gloss:dosdoğru kıl} fiilindeki doğrultuyu koruma ve denge yankısı gerçek yürüyüşte bedensel bir karşılık bulur; bu bağ, namazı yürüme talimatı olarak değil, ibadetteki yönelişin gündelik davranışta sürmesi olarak düşündürür. Bu buyruklar bir makam sahibini adlandırmaz ve ayrı görgü öğütleri olarak da okunabilir; bu okuma her kararlı düzeltmeyi tahakküm saymaz. Bedenin ve sesin ölçülmesi ahlaki yöneltmenin nasıl uygulanacağına sınır çizer.

Ses öğüdü bu ölçüyü işitilen alana taşır. Seslerin en çirkini olarak eşek sesi gösterilir (31:19): {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghuḍḍ min ṣawtika, gloss:sesini alçalt} buyruğunun yanındaki {ar:أَنْكَرَ الْأَصْوَاتِ لَصَوْتُ الْحَمِيرِ, tr:ankara al-aṣwāti la-ṣawtu al-ḥamīr, gloss:seslerin en çirkini eşeklerin sesidir} karşılaştırması, {ar:ٱلْمُنكَرِ, tr:al-munkar, gloss:reddedilen yanlış} ile aynı kelime ailesindeki çirkinlik ve reddedilme yankısını ses alanına taşır. Bu karşılaştırma ahlaki yöneltmenin ses tonunu ve işitilen tarzını da değerlendirmeye katar. Buradaki bağ seslere ilişkin özel üstünlük karşılaştırmasıyla sınırlıdır; yanlış eylemleri konuşmaya indirgemez ya da her yüksek ses için genel yasak kurmaz.

## Başa geleni taşımak

Zincirin son buyruğu genel bir erdem adını somut bir duruma bağlar: {ar:وَٱصْبِرْ عَلَىٰ مَآ أَصَابَكَ, tr:waṣbir ʿalā mā aṣābaka, gloss:başına gelene sabret}. Buradaki {ar:مَآ, tr:mā, gloss:her ne} sabrın konusunu açık bırakır; geçmiş biçimindeki {ar:أَصَابَكَ, tr:aṣābaka, gloss:sana erişti} olmuş bir erişme ya da çarpma olayını bildirir, sonundaki {ar:كَ, tr:ka, gloss:seni} ise muhatabı alıcı ve hedef yapar. {ar:عَلَىٰ, tr:ʿalā, gloss:üzerine} bu olayı sabrın yöneldiği dış yük gibi kurar; olayın faili, nedeni ve ahlaki değeri açık bırakılır ve yükün ortadan kalkacağı vaat edilmez. Böylece sabır bekleyip hiçbir şey yapmamak değil, sarsıntı ve yakınma dürtüsüne karşı kendini tutarak başa gelene dayanmaktır.

Üç edat bu görevleri nesnelerine göre somutlaştırır: {ar:بِ, tr:bi, gloss:ile} iyiliğe yönelme ilişkisini, {ar:عَن, tr:ʿan, gloss:-den uzak} kötülükten ayrılmayı, {ar:عَلَىٰ, tr:ʿalā, gloss:üzerine} ise geleni taşımayı kurar. Bunlar birbirinin basamağı ya da üstünlük sırası değildir. {ar:أَصَابَكَ, tr:aṣābaka, gloss:sana erişti} fiilinin hedefe yönelip varma kullanımı, kişi ekinin gösterdiği hedefle birleşince olayı kişiye ulaşan bir darbe gibi duyurur; {ar:عَلَىٰ, tr:ʿalā, gloss:üzerine} ilişkisinin yük hissi de bu gelişin sabır üzerindeki ağırlığını verir. Fiilin aşağı inen yağış için kullanılan yönü, aynı sahneye yukarıdan iniş yankısı ekler. Hedefe varış, yük ve iniş başa gelen sıkıntının şiddetini duyurur; bu benzetme nişan alınıp yollanmış bir oku ya da gerçek yağışı değil, gerçekleşmiş erişmeyi anlatır.

Sabrın sözcük alanındaki iki yan kullanım bu basınç imgesini derinleştirir: sabır sözcüğünün başka kullanımlarındaki acı ve ilaçta da kullanılan ağaç özü zorluğa duyusal sertlik ve ısı katar; aynı sözcük ailesindeki yükümlülük üstlenme ya da kefil olma yönü ise sonuç geldikten sonra sorumluluğa bağlı kalma tonunu açar. Bu çağrışımlar ayette sabrı bir bitki adı ya da mali kefalet olarak kullanmaz; duyusal sertlik ve sorumluluk tonu katar. Bir işin ardından sonucun kişiye ulaşması bu tutumu bazen maruz kalınan bir bedel gibi duyurabilir; bu olası bir tondur, her sıkıntının kişinin eyleminden doğduğu ya da misilleme olduğu kuralı değildir. Bu iki yan kullanım, sabrı olaydan kaçış değil, etkisi sürerken yöneltilmiş işi taşımak olarak derinleştirir.

Erişmenin ölçeği ve görünürlüğü 31:16’da bir arada açılır. {ar:مِثْقَالَ, tr:mithqāla, gloss:ağırlığınca} ölçüyü, {ar:حَبَّةٍ مِنْ خَرْدَلٍ, tr:ḥabbatin min khardal, gloss:hardal tanesi} küçüklüğü, {ar:فِي صَخْرَةٍ, tr:fī ṣakhra, gloss:kayanın içinde} kaya içinde saklı kalmayı somutlaştırır; gökler ya da yer içinde gizlenme de aynı görünmezliği geniş ölçekte kurar. Allah’ın onu ortaya çıkarması sahneyi tamamlar (31:16). {ar:مَآ أَصَابَكَ, tr:mā aṣābaka, gloss:başına gelen şey} içindeki erişme fiili, {ar:يَأْتِ بِهَا اللَّهُ, tr:yaʾti bihā Allāh, gloss:Allah onu getirip ortaya çıkarır} ifadesindeki varıp görünür kılmayla buluşunca, kişiye ulaşan etkinin başlangıçta görünür ya da büyük olması gerekmediği hissini verir. Hardal tanesi burada küçüklüğün ölçüsüdür; bu okumada tane bir yaralanma imgesine dönüşmez. Aynı sahnedeki {ar:لَطِيفٌ, tr:laṭīf, gloss:ince ve lütufkâr} gizliye ince bir yoldan erişmeyi, {ar:خَبِيرٌ, tr:khabīr, gloss:içyüzü bilen} ise onun içinden haberdar olmayı düşündürür (31:16). Bu sahne ilahi hesapla ilgili olabilir; bu ihtimal belirli bir gizli cezayı, yarayı ya da zamanlamayı adlandırmaz. Böylece 31:16’nın küçük ve saklı ölçüsü, sabrı yalnız göz önündeki darbeyle sınırlamadan düşünmeye açar.

## Kararlılığın adı

Dört eylemin ardından gelen {ar:إِنَّ, tr:inna, gloss:kuşkusuz} yazı ve sesletimdeki ikizleşmesiyle değerlendirmeyi belirginleştirir. {ar:ذَٰلِكَ, tr:dhālika, gloss:işte bu} önceki zincire dönerek dört buyruğu tek bir değerlendirme konusu yapar; uzak işaret biçimi fiziksel ayrılık değil, geriye bakıp eylemleri birlikte görme hareketidir. {ar:مِنْ, tr:min, gloss:-den, arasında} bu eylemleri {ar:عَزْمِ ٱلْأُمُورِ, tr:ʿazmi-l-umūr, gloss:kararlılık gerektiren işler} sınıfına yerleştirir: hafif bir “-den” tonu duyulabilse de temel ilişki sınıflandırmadır; buyruklar bu tür işlerden biridir, sınıfın tek örneği değildir. {ar:عَزْمِ, tr:ʿazmi, gloss:kararlılık} isteği kesin karara ve uygulamaya bağlayan sağlam yönelişi, {ar:ٱلْأُمُورِ, tr:al-umūr, gloss:işler} ise tek olaydan geniş pratik işler alanını adlandırır. Karara bağlanma yönü gerçek bir kesme ya da maddi bağlama işlemi değildir; isteğin eyleme yönelmesini duyurur. Başta {ar:أَقِمِ, tr:aqim, gloss:namazı kur} ile açılan uygulanış, burada kararlılık gerektiren işler olarak sınıflanır: kapanış dört eylemin yerini almaz, onları kararlılıkla yürütülecek işler diye çerçeveler.

Bu kapanıştaki işler adı, önceki {ar:أْمُرْ, tr:uʾmur, gloss:emret} buyruğuyla aynı kök alanında yankılanır. Bir kişiye yöneltilen somut emir, daha geniş pratik işler alanına bağlanır; son isim ikinci bir emir olmaz. Öğüt alma ve karşılıklı danışma yönündeki kullanım da tanımadan eyleme geçişe düşünülmüşlük katar. İsimde belirlenen yolda dönmeden ilerleme çağrışımı, gerçek yürüyüş öğüdüyle temas eder (31:19); bu bağ, kararlılığı bir yolculuk diye değil, kararlılık gerektiren işler alanında sebat olarak duyurur. Bu doğrudan davranış buyrukları, “kararlılık” sözünün bağlayıcı görev yankısını da duyurabilir (31:18, 31:19). Böylece olağan sebat anlamı korunurken görevlerin uygulamadaki ağırlığı belirir; bu temas tek bir hukuk düzeni ya da tüm yönergeler için aynı bağlayıcılık derecesini kurmaz.

Gerçek yürüyüşün yönü, kararlılığın nasıl sürdürüldüğünü daha da belirginleştirir: {ar:وَاقْصِدْ فِي مَشْيِكَ, tr:waqṣid fī mashyika, gloss:yürüyüşünde ölçülü ol} bedensel ilerleyişte ölçü ister (31:19). Bu yürüyüş, belirlenen yolda yönünü bozmadan sürme çağrışımıyla kararlılığın sürekliliğini aydınlatır; cümlenin odağındaki {ar:عَزْمِ, tr:ʿazmi, gloss:kararlılık} yine bir sebat niteliğidir. Ardından, sağlam tutamağa sarılıp bırakmama ve işlerin sonunun Allah’a varması anlatılır (31:22): {ar:ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:istamsaka bi-l-ʿurwati al-wuthqā, gloss:sapasağlam tutamağa sarıldı} devam eden bir tutunmayı, {ar:وَإِلَى ٱللَّهِ عَٰقِبَةُ ٱلْأُمُورِ, tr:wa-ilā Allāhi ʿāqibatu al-umūr, gloss:işlerin sonu Allah’a varır} ise nihai sonucun kişinin denetimini aştığını gösterir. Aynı {ar:ٱلْأُمُورِ, tr:al-umūr, gloss:işler} adının yinelenişi (31:22) güvenilir desteği ve sonucun insan denetimini aşan sınırını birlikte açar; bu yankı 31:17’yi gelecek haberi yapmaz. Tutunma genel bir güven ilişkisini de anlatabilir; bu bağlamda kararlı eylem sürer, edilgenliğe dönüşmez.

Kararlılığın kriz boyunca sürmesi, ayrı bir deniz sahnesinde sınanır. Allah’ın nimetiyle denizde ilerleyen gemi bir işaret olur; aynı sahnede sabredip şükredenler anılır (31:31): {ar:ٱلْفُلْكَ تَجْرِي فِي ٱلْبَحْرِ بِنِعْمَتِ ٱللَّهِ, tr:al-fulka tajrī fī al-baḥri bi-niʿmati Allāh, gloss:gemi Allah’ın nimetiyle denizde seyreder} ve {ar:لِكُلِّ صَبَّارٍ شَكُورٍ, tr:li-kulli ṣabbārin shakūr, gloss:çok sabreden ve çok şükreden herkes için}. Sonra gölgeler gibi dalgalar yolcuları örter (31:32): {ar:غَشِيَهُم مَّوْجٌ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-al-ẓulal, gloss:üstlerini gölgeler gibi dalga örttü}. Gölgeler gibi örtülme olağan ufuklarını ve denetimlerini siler; iç içe, yinelenen dalgalar tek bir çarpmayı süreğen istikrarsızlığa dönüştürür. Yolcular dinlerini Allah’a özgüleyerek O’na yakarır ve kurtarılıp karaya çıkarılır (31:32): {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu al-dīn, gloss:dinlerini O’na özgüleyerek Allah’a yakardılar}. Bu benzerlik, {ar:مَآ أَصَابَكَ, tr:mā aṣābaka, gloss:başına gelen şey} ifadesini denetim dışı baskı altında görünür kılar: fırtına sabrın yaşandığı ayrı bir deniz görüntüsüdür, 31:17’deki ahlaki çağrının sonucu olarak sunulmaz.

Karaya çıkışla sınama bitmez: kimi ölçülü davranır, başkaları Allah’ın işaretlerini yadsır (31:32). {ar:فَمِنْهُم مُّقْتَصِدٌ, tr:fa-minhum muqtaṣid, gloss:onlardan ölçülü davrananlar vardır} ve {ar:يَجْحَدُ بِـَٔايَٰتِنَآ, tr:yajḥadu bi-āyātinā, gloss:işaretlerimizi yadsır} kurtuluş sonrasının herkeste aynı olmadığını gösterir. Bu ayrı işaret, sabrın tanımını ya da bütün güçlüklerin örneğini vermek yerine, sabır ve şükrün tehlikeden rahatlamaya ve sonraki hayata uzanıp uzanmadığını yalnızca kısmen sınar.

## Destek ve biçim

Başka bir ölçeğe geçince, göklerin görülen direkler olmadan kurulması, yeryüzüne sabit dağların yerleştirilmesi ve onun insanlarla birlikte sarsılmasının önlenmesi bir destek düzeni gösterir (31:10): {ar:بِغَيْرِ عَمَدٍ تَرَوْنَهَا, tr:bi-ghayri ʿamadin tarawnahā, gloss:görebileceğiniz direkler olmaksızın}, {ar:رَوَاسِيَ, tr:rawāsiya, gloss:sabit dağlar ve dayanaklar} ve {ar:أَن تَمِيدَ بِكُمْ, tr:an tamīda bikum, gloss:sizinle birlikte sarsılmasın diye}. Bu ayrıntılar destek imgesine ayrı katkılar sunar: görünür direklerin yokluğu taşıyıcıyı gözden saklar, dağlar zemine dayanak olur, salınımın önlenmesi de düzenin sürmesini görünür kılar. {ar:أَقِمِ, tr:aqim, gloss:ikame et} fiilinin ayrı “destek ya da temel olma” kullanımı namazı sürdürülen bir dayanak gibi duyurur; {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} hitabının aynı kök alanındaki yapı ve taşıyıcı parçaları birleştirme kullanımı biçimlenme ve taşıma yankısıyla görüntüye katılır. Bu bağlantı muhataba kozmik sarsıntı vaadi çıkarmaz; {ar:أَقِمِ, tr:aqim, gloss:ikame et} ile {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} gerçek sütun adları değil, dayanak ve yapı çağrışımlarıyla sahneye katılır. Namaz, toplumsal sınır, sabır ve kararlılık birlikte, baskı altında hayatı taşıyan birden çok destek imgesi kurar.

Bu mimari görüntüden ayrı olarak, bir malzeme benzetmesi biçimin baskı altında nasıl korunduğunu düşündürür. {ar:أَقِمِ, tr:aqim, gloss:ikame et} fiilinin doğrultuyu koruma ve denge yönü zincirin çizgisini verir; {ar:أَصَابَكَ, tr:aṣābaka, gloss:sana erişti} hedefe ulaşıp temas eden etkiyi, {ar:ٱصْبِرْ, tr:iṣbir, gloss:sabret} ise acının içinden kendini tutmayı getirir. Sabır için aktarılan acı ve ilaçta da kullanılan ağaç özü bu basınca sertlik ve ısı verir; {ar:عَزْمِ, tr:ʿazmi, gloss:kararlılık} isteği karar ve uygulamaya bağlayarak iradenin çizgisini sürdürür. Değneğin ateşte çevrilmesi ısıyı, yumuşatılması biçimlenebilirliği, doğrultulması ise sürdürülen çizgiyi imgeye ekler; bu katkılar birlikte görev zincirini baskı altında biçimini bulan bir iradeye benzetir. Bu sınırlı malzeme benzetmesi sözcüklerin köken açıklaması değildir; odaktaki namaz düzenli ibadet olarak kalır.

Akış benzetmesi, yasağın sınır koyması, başa gelenin basınç, sabrın tutma ve ikamenin dayanak olma katkılarını birleştirir. {ar:ٱنْهَ, tr:anha, gloss:yasakla} olağan durdurma buyruğunu taşır; suyun akış sonunda durulup biriktiği gölcük kullanımı yasağı akışa sınır koyan bir duruş gibi düşündürür. {ar:أَصَابَكَ, tr:aṣābaka, gloss:sana erişti} başa gelen olayı bildirirken aşağı inen yağış kullanımı onu içeri ulaşan basınç gibi kurar. Bu basınca karşı {ar:ٱصْبِرْ, tr:iṣbir, gloss:sabret} şişe ya da kuyu ağzını tutan tıkaç benzetmesini alır; {ar:أَقِمِ, tr:aqim, gloss:ikame et} fiilinin varlığı ve düzeni sürdüren temel olma kullanımı ise yapıyı işler halde tutar. Bu sistem imgesinde dere ya da kuyu ayetin anlatısı değil; benzetme ayrı sözlük kullanımlarının birleşmesiyle kurulur. Sınır akışı kısıtlar, tutma basıncın taşmasını önler, dayanak düzeni taşır; birlikte suyun taşma ya da çökme olmadan yönetildiği bir sistem imgesi kurarlar.

Akış benzetmesinden sonra oğul hitabına dönünce, biçimlenme çağrışımı sorumluluğun devredilememesiyle de derinleşir. Bir ebeveyn çocuk yerine, çocuk da ebeveyn yerine hiçbir şeyi karşılayamaz (31:33): {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِ شَيْـًٔا, tr:lā yajzī wālidun ʿan waladihī wa-lā mawlūdun huwa jāzin ʿan wālidihī shayʾan, gloss:ne ebeveyn çocuk yerine ne çocuk ebeveyn yerine karşılık verebilir}. Ebeveyn de ahlaki görevini çocuğun üzerinden devredemez. Dünya hayatının aldatması ve {ar:ٱلْغَرُورُ, tr:al-gharūr, gloss:aldatıcı} uyarısı görünüşün verdiği sahte güvene karşı kişinin kendi yargısını gerekli kılar (31:33). Bu okuma, 31:33’ün odaktaki namaz, kamusal buyruk ya da sabrın özel içeriğini belirlediği iddiası değil, komşu sahneden çıkarılan bir oluşum yorumudur. Böylece şefkatli {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} hitabı, kendi sorumluluğunu taşıyacak bir kişinin yetişmesi yönünde de duyulur.

## Geleceğin bilinmezliği

Aile sorumluluğundan sonra 31:34 düşünceyi geleceğin bilinmezliğine taşır. Gökten inen, hayat veren yağmur burada {ar:وَيُنَزِّلُ ٱلْغَيْثَ, tr:wa-yunazzilu al-ghayth, gloss:yağmuru indirir} ifadesiyle ve 31:17’deki {ar:أَصَابَكَ, tr:aṣābaka, gloss:sana erişti} fiilinden farklı bir sözcük ailesiyle anılır (31:34). İki sahne, sözlük eşitliğiyle değil, aşağı inen yararla kişiye varan şeyin benzetme yoluyla buluşmasıyla bağlanır; böylece gelişlerin yalnız zarar değil yarar da taşıyabileceği açılır. İnsan yarın ne kazanacağını ve hangi yerde öleceğini bilmez (31:34): {ar:مَاذَا تَكْسِبُ غَدًا, tr:mādhā taksibu ghadan, gloss:yarın ne kazanacağını} ve {ar:بِأَيِّ أَرْضٍ تَمُوتُ, tr:bi-ayyi arḍin tamūtu, gloss:hangi yerde öleceğini}. Böylece planın ve eylemin son sınırıyla olası kazanç aynı bilinmez ufka girer. {ar:وَٱصْبِرْ, tr:waṣbir, gloss:sabret} buyruğu gerçekleşmiş sıkıntıya etkin karşılık vermeyi sürdürürken neyin, ne zaman geleceğinin bilinmediği bu ufka da yer açar.

</source_prose>
