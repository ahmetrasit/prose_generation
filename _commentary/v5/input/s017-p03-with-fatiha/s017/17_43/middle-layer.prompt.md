# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:43**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.middle.claims.json`

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
- Refer to source paragraphs as `17:43 ¶N`.

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

`(17:43 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:43",
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
        "citation": "(17:43 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_43/17_43.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_43/17_43.middle.claims.json \
  --ayah-ref 17:43
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_43/17_43.prose.editorial.tr.md`

<source_prose>
## Tenzihin Söyleyişi

17:43, Allah'ı insanların dile getirdiği sözlerden tenzih eder ve aynı özneye yücelik yüklemini bağlar. {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} ile açılan övgünün hedefini {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} belirler; ardından gelen {ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} bu ilahi göndergeyi yücelik bildirimine taşır. Açılışta geçen {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} bir mastardır: örtük bir fiili taşıyan kalıplaşmış ünlem gibi kullanılır ve ayrı bir olay anlatmaktan çok, söylenişiyle tenzih eylemini gerçekleştirir. {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} bu tenzihin yöneldiği söz alanını gösterir, fakat sözlerin tam içeriğini ya da konuşanların kimliğini açıklamaz.

Bu tenzih formülünün kök ailesindeki başka kullanımlar suda yüzmeyi ve su ya da hava içinde akıcı, hızlı ilerlemeyi de anlatır. Ayette {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} ile {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} arasındaki uzaklık ilişkisi, bu akış imgesini isnatların kısıtlarından özgür oluşa doğru açar: tenzih, Allah'ı eksiklikten uzak tutarken bu söz alanından da serbest bırakır. Buradaki akış fiziksel bir hareket değil, olağan tenzih anlamını derinleştiren bir çağrışımdır.

Açılıştaki {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} biçiminin yumuşak, nefesimsi tınısı salıverilme hissini işitilebilir kılabilir: ses, zaten kurulan tenzihin isnatlardan özgür oluş yönünü duyurur. Bu katkı ses çağrışımı düzeyinde kalır; yeni bir sözlük anlamı ya da gerçek bir nefes veya hareket bildirmez.

{ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} sonundaki üçüncü tekil eril zamir ile hemen ardından gelen {ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} fiilinin üçüncü tekil öznesi aynı ilahi göndergeye bağlanır. Bitişiklik ve ortak yüklemleme, açılıştaki övgüyü sonraki yücelik bildirimine taşır; bu yerel bağ için önceki ayetten özel bir öncül gerekmez. Aradaki {ar:وَ, tr:wa, gloss:ve}, tilavette iki sözü durakla ayırmadan bir ses köprüsü kurarken bağlaç olarak iki bildirimi biriktirir; tek başına yeni bir anlam eklemez.

{ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} Kalıp VI'da, üçüncü tekil eril özneye bağlı geçmiş zaman biçimindedir. Allah bu biçimde yücelik yükleminin öznesidir; yüklem yüceliği tamamlanmış olarak sunar, başka bir öznenin O'nu yukarı kaldırdığı bir eylemi değil. Verilen sözdiziminde fiil geçişsizdir ve {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} öbeğini tümleç olarak kendine bağlar, doğrudan nesne almaz. Çekim yüceliği yerleşik ve tamamlanmış duyurur; bu gramatik sunuş kendi başına teolojik bir nedensellik açıklamaz. Fiildeki uzun ünlüler de yukarı yön duygusunu okunuş boyunca uzatır.

Fiilin dikey rengi, bağlandığı söz öbeğinin verdiği soyut alanda yeniden yön bulur: {ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} yukarıda olmayı, {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} ise insanların dile getirdiklerini gösterir. Bu ikisinin teması, yüksekliği bir konumdan çok onların sözlerini aşan ilişkisel yücelik olarak duyurur.

Fiilden sonra aynı kökten gelen {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} mastarı gelir. Mef'ûl-i mutlak denen bu kullanım, fiilin anlamını kendi adıyla yineleyerek yüceliğin ölçüsünü belirginleştirir; ölçü nitelikseldir, sayısal ya da fiziksel birim değildir. Belirsiz mansup {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} ile ona durum ve belirsizlik bakımından uyan {ar:كَبِيرًا, tr:kabīran, gloss:büyük} tek bir ölçü öbeği kurar; sıfat yüceliğin kendisini niteler. Buradaki büyüklük fiziksel kütle ya da ağırlık değil, derece ve önemdir; insanın kendini yüceltme eylemi de kurulmaz.

Yücelik fiiliyle onu adlandıran mastarın arasına önce {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} girer: bu sıralama, söz alanını ölçüden önce duyurur; ardından {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} fiilden kopmadan yüceliği hem yüklem hem adı konmuş ölçü olarak sunar. Söyleme fiilinin {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} sonundaki uzun ū, {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} biçimindeki şeddeli vav ve iki biçimin -an kadansı kapanışı işitilir biçimde yoğunlaştırır. Sondaki sıfat büyüklüğü sona saklayıp ölçü öbeğini kapatır; yeni bir yüklem değil, dizilişin kadansıdır. Bu ses sırası önce söz alanını, ardından ölçülmüş yüceliği öne çıkarır; okumalar arasında hiyerarşi kurmaz ve tenvin sözlük anlamına yeni bir öğe eklemez.

Son sıfat okuru yeniden ölçülmüş yüceliğe döndürerek 17:43'ün yerel dizilişini kapatır; bu kapanış sonraki ayetleri ya da sureyi sonuçlandıran bir yargı değildir. Yalın mastar biçimi başka yücelik biçimlerinden ayrılarak seyrek bir profil çizer, ancak buna ilişkin sıklık sayımı verilmez. Başka bir biçim ihtimali, ayetteki mevcut yüzeyi değiştirmez.

Bu yerel kapanışın yankısı, 17:43'teki {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} söyleyişinin surenin 17:1'deki {ar:سُبْحَٰنَ, tr:subḥāna, gloss:tenzih ederek yüceltme} başlangıcını yeniden duyurmasıyla genişler. 17:43'te tenzih, insanların sözlerinden uzaklık bildiren cümlede yer alır; böylece 17:1'deki açılış övgüsü burada dile getirilen isnatların yanına gelir. Bu yankı söyleyiş düzeyinde kalır: iki ayetin sözdizimini ortaklaştırmaz ve sure geneline ilişkin bir sonucu kendi başına belirlemez.

41:38'de Allah'a yakın olanların gece gündüz O'nu tesbih etmesi, insan kibrine karşı olumlu bir kulluk eylemi sunar. Bu karşıtlık, 17:43'teki tenzih ve yüceltmenin üstünlük taslayan isnatların karşısında bir övgü olarak da duyulmasına imkân verir. Buradan 17:43'e taşınan ilişki tesbih ile kibir arasındaki karşıtlıktır; 41:38'deki özneler ve süre kendi bağlamında kalır.

Hemen sonraki 17:44, övgü alanını yaratılmışların ortak fiiline açar: gökler, yer ve içlerindekiler Allah'ı {ar:تُسَبِّحُ, tr:tusabbiḥu, gloss:yüceltip anar}; hiçbir şey O'nu {ar:يُسَبِّحُ, tr:yusabbiḥu, gloss:yüceltip anmadan kalmaz} ve bunu {ar:بِحَمْدِهِۦ, tr:bi-ḥamdihi, gloss:hamdiyle} yapar. 17:44'te aynı tesbih kökü üç biçimde döner; yaratılmışlar söz, eylem ya da niyetle Allah'ı yüceltip anar, hamdi de ayrıca dile getirir. Hamd tesbihe eşlik eder ve onunla aynı anlama gelmez. İnsanların bu tesbihin tarzını bütünüyle kavrayamaması, {ar:لَا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:lā tafqahūna tasbīḥahum, gloss:onların tesbihini tam kavrayamıyorsunuz} sözünde insan bilgisinin sınırını çizer. 17:44'ün yaratılmışların ibadet içindeki tesbihi ile 17:43'teki {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} söyleyişi aynı övgü ufkunda buluşur; birinde yaratılmışların yüceltme eylemi, ötekinde Allah'ı eksiklikten uzak tutan tenzih öne çıkar.

Fâtiha'nın hamdi Allah'a nispet eden açılışı (1:2) ile doğrudan kulluk ve yardım duası (1:5), 17:44'teki kozmik övgünün yanına insan sesini getirir. Okur, kendi hamdi ve kulluğuyla yaratılmışların tesbihine katılıyormuş gibi duyabilir: bu yakınlık insanın hamdini ve duasını tesbih ufkuna taşırken, Fâtiha'daki bu sözler kendi başlarına ibadet olarak kalır; 17:43'teki {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:tenzih ederek yüceltme} ise Allah'ı eksiklikten uzak tutan söyleyiştir. Hemen sonraki 17:44'ü tamamlanan tenzih bildiriminin ardından yeni bir örnek olarak okumak mümkündür; bu okumada da iki ayetin övgü yakınlığı korunur.

## Sözün Çerçevesi

Cümlenin ortasındaki {ar:عَمَّا, tr:ʿammā, gloss:-den/-dan ne}, bir edatla {ar:مَا, tr:mā, gloss:ne / olan} parçacığının birleşimidir ve ardından gelen söyleme cümlesini {ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} yüklemine bağlar. Böylece söylenenler bağımsız bir alıntı olarak durmak yerine yüklemin tümleci olur. {ar:مَا, tr:mā, gloss:ne / olan} ilgi zamiri olarak okunursa dile getirilen içeriği gösterir; mastariye okumasında söyleme eylemini adlaştırır. İlgi zamiri okuması öne çıkar, mastariye ihtimali de açık kalır; fiilin nesnesiz oluşu hem iddianın sözlerine hem sürmekte olan söyleme eylemine yer verir. Edatın ayrılma katkısıyla “onların söylediklerinden yücedir” okuması öne gelirken “onların söyledikleri hakkında” yönelimi de mümkündür. Bu sözdizimi iki Türkçe yönelime izin verir, tek bir çeviriyi zorunlu kılmaz.

{ar:عَمَّا, tr:ʿammā, gloss:-den/-dan ne} içindeki genizsi m, ardından gelen yönetimli fiile ses akışı kurar ve öbeğin yücelik yüklemine tek parça bağlanmasını duyurur; katkısı ses düzeyindedir. Açılıştaki tenzih ile sondaki yücelik ölçüsü cümlenin sınırlarını kurarken sonlu söyleme fiili aradaki bağımlı tümceyi oluşturur. Bu yerleşim insanların sözlerine ayetin ortasında belirgin bir yer verir; içeriği ise kendi başına belirlemez.

{ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} şimdiki-geniş zamanda sürmekte olan söylemeyi bildirir. Açık bir nesne taşımaz; fakat {ar:مَا, tr:mā, gloss:ne / olan} söylenen içeriğe yer verir, böylece hem söylenen önerme hem onu söyleme eylemi yücelik bildirimine bağlanabilir. Üçüncü çoğul eril sonundaki -ūna, ayrı bir özne adı olmadan konuşanlar grubunu gösterir: çoğulluk bellidir, konuşanların kimliği ve grubun kapsamı açık bırakılır. Verilen şahıs değişimli kıraat bu söz alanını doğrudan hitaba yaklaştırabilir; temel biçimdeki üçüncü çoğul anlatım yerinde kalır ve bu değişim belirli bir muhatap tayin etmez.

Odağa daha önceki tartışmadan somut bir bağlam sağlayan 17:40'ta “Rabbiniz sizi oğullarla mı seçip ayırdı?” sorusu {ar:أَفَأَصْفَىٰكُمْ, tr:afa-aṣfākum, gloss:sizi seçip ayırdı mı} ve {ar:بِٱلْبَنِينَ, tr:bi-l-banīna, gloss:oğullarla} sözleriyle kurulur; aynı pasaj melekleri dişi sayma isnadını da dile getirir. Ardından iddia {ar:تَقُولُونَ, tr:taqūlūna, gloss:söylüyorsunuz} diye adlandırılır ve {ar:قَوْلًا عَظِيمًا, tr:qawlan ʿaẓīman, gloss:büyük bir söz} diye nitelenir (17:40). Bu ayet, 17:43'te tenzih edilen söz için yakın ve somut bir bağlam sunar; odağın tam göndergesi ise açık kalır. İki kapanıştaki büyüklük farklı ögelere bağlanır: 17:40'ta sıfat söylenen iddiayı, 17:43'te {ar:كَبِيرًا, tr:kabīran, gloss:büyük} {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} mastarını niteler. Bu ortak büyüklük alanı sözden yüceliğe bir aktarımı mümkün kılar; her sıfat kendi cümlesini de bağımsız biçimde kuvvetlendirdiğinden aktarım zorunlu değildir.

18:5'te Allah'a çocuk isnadı “büyük bir söz” diye nitelenir ve bu sözü söyleyenlerin yalan söylediği belirtilir. Buradaki büyüklük sözün niteliğidir; 17:43'te {ar:كَبِيرًا, tr:kabīran, gloss:büyük}, {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} mastarının derecesini bildirir. Bu karşılaştırma söyleme ile yanlış isnadı yan yana getirir; odaktaki söyleme fiili “yalan söylemek” anlamına gelmez ve 18:5'teki çocuk isnadı 17:43'ün tam göndergesi olarak belirlenmez.

5:73'te üçlü ilahlık iddiasının yanında {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} ifadesi geçer; 6:100'de Allah'a ortaklar ve çocuklar yakıştırılması benzer bir arındırma çerçevesi kurar. Bu iki bağlam, sözlerin dile getirilen önermeler olmanın yanı sıra benimsenmiş inanç iddiaları olarak da duyulmasına imkân verir; böylece yorum, söylenen cümleden onu benimseyen tutuma uzanır. Bu bağlamsal geçiş belirli bir öğretiyi, mezhebi ya da bütüncül dünya görüşünü teşhis etmez. Odaktaki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} yine konuşmayı bildirir; burada “inanmak” anlamını almaz.

Söyleme taşıyıcısına ilişkin uzak bir sözlük imgesinde aynı kök ailesinin başka bir kullanımı yükü kaldıracak gücü bulmayı, taşımayı ya da üstlenmeyi anlatır. Odaktaki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} söyleme anlamını korur; yük imgesi ayrı ve biçimce uzaktır. Bu yan anlam, söz alanını hayalen taşınan bir yük gibi düşünmeye imkân verir; bir işin ağır ve güç gelmesine ilişkin kullanım da bu imgeye zorluk ve çaba boyutunu ekler. Bu yük imgesi {ar:تَعَٰلَىٰ, tr:taʿālā, gloss:yücedir} ve {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} ile açılan yükseklik, {ar:كَبِيرًا, tr:kabīran, gloss:büyük} ile genişleyen ölçü yanına geldiğinde, yüceliği hem yükü hem onu kaldırma çabasını aşar gibi duyurabilir. Bu keşif düzeyinde mecazi bir çağrışımdır: ayet yük ya da üstlenilen iş kurmadığından gerçek ağırlık veya konuşanların fiilen yük taşıması söz konusu değildir.

## Söylemek ve Karşılanmak

17:41'de Kur'an'ın çeşitli örnekleri farklı biçimlerde sunması {ar:صَرَّفْنَا فِى هَٰذَا ٱلْقُرْءَانِ, tr:ṣarrafnā fī hādhā al-qurʾāni, gloss:bu Kur'an'da türlü biçimlerde sunduk}, hatırlatma amacı taşısa da {ar:لِيَذَّكَّرُوا۟, tr:li-yadhakkarū, gloss:hatırlasınlar diye}, muhataplardaki uzaklaşmayı artırır {ar:نُفُورًا, tr:nufūran, gloss:uzaklaşma ve kaçınma} (17:41). Bu karşıtlık hatırlatma amacıyla muhatapların tepkisini yan yana getirir. Söyleme kök ailesinin bağımsız bir kullanımı da sözsüz bir hâlin bir şeyi belli etmesini anlatır; bu çağrışım, 17:43'teki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} sözlerin önermelerini dile getirmenin yanı sıra konuşanların tutumunu açığa çıkarabileceği biçimde işitilmesine imkân verir. Bu, bağlamın düşündürdüğü bir genişlemedir; odaktaki fiilin olağan anlamı “söylemek” olarak kalır.

17:45'te Kur'an okunduğunda inanmayanlarla araya {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde} konması, perde imgesini sözün alınışındaki engele dönüştürür (17:45). 17:46 bu engeli kalpler üzerindeki {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler}, Kur'an'ı {ar:أَن يَفْقَهُوهُ, tr:an yafqahūhu, gloss:kavramaları} önündeki güçlük ve kulaklardaki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} ile ayrıntılandırır (17:46). Perde bir sınır koyar, kalp örtüleri kavrayışı zorlaştırır, kulaktaki ağırlık ise işitmeyi güçleştirir; bu ağırlık işitmenin yokluğunu değil, zorluğunu somutlaştırır.

Bu engeller arasında 17:47'de anlatılan {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} dinlemesi sürer (17:47). Dinleme, sözün işitildiğini gösterir; kavrayış ya da kabulü kendiliğinden içermez. Zalimlerin kendi aralarında {ar:يَقُولُ, tr:yaqūlu, gloss:diyor} oluşu da konuşmanın devam ettiğini gösterir (17:47). Böylece odaktaki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} sözlerin sürmesi, onların işitilmesi ve anlaşılması birbirinden ayrılır.

17:48'de Peygamber için kurulan benzetmeler ve örnekler {ar:ضَرَبُوا۟ لَكَ ٱلْأَمْثَالَ, tr:ḍarabū laka al-amthāla, gloss:senin için benzetmeler ve örnekler kurdular}, önce olağan benzerlik kurma anlamını taşır; bunları dayatılmış bir eşitleme saymak daha ihtiyatlı bir bağlam okumasıdır (17:48). Ardından anlatılan sapma ve {ar:فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-lā yastaṭīʿūna sabīlan, gloss:bir yol bulamıyorlar} sözü, karşılaştırmaların yol göstermek yerine yön kaybıyla sonuçlanabileceğini düşündürür (17:48). Bu ayrıntılar, kabulün farklı yüzlerini açar: 17:41'de hatırlatmaya karşı artan uzaklaşma, 17:45'te perde ve 17:46'da kavrayış/işitme engelleri, 17:47'de engellere rağmen dinleme, 17:48'de ise benzetmelerin ardından yol bulamama görünür (17:41, 17:45, 17:46, 17:47, 17:48). Bu bağlamlar 17:43'teki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} sözlerin nasıl karşılandığı sorusunu genişletir; aralarında kanıtlanmış bir sebep-sonuç zinciri ya da bütün dinleyiciler için geçerli bir psikoloji kurmaz. Tutumu açığa çıkarma ihtimali, bu bağlamın odak fiile kattığı genişlemedir.

17:53'te kullara {ar:يَقُولُوا۟ ٱلَّتِى هِىَ أَحْسَنُ, tr:yaqūlū allati hiya aḥsanu, gloss:en güzel olanı söylesinler} buyurulması, odaktaki {ar:يَقُولُونَ, tr:yaqūlūna, gloss:onlar söylüyorlar} biçiminin olağan söyleme anlamını korurken bu kez sözün içeriğini ve insanlar arasındaki etkisini ölçüye alır; daha iyisini söylemek kötülüğü gidermeye dönük yapıcı bir yön açar (17:53). Aynı ayette {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaghu baynahum, gloss:aralarına kışkırtma sokar} fiilindeki araya saplanan darbe imgesi kışkırtmanın yönünü, {ar:عَدُوًّا مُبِينًا, tr:ʿaduwwan mubīnan, gloss:açık bir düşman} ise düşmanlık doğuran sonucu belirginleştirir (17:53). Bu iki hareket, sözün ilişkiyi onarma yönüyle şeytanın kışkırtmasının açtığı ayrışmayı karşı karşıya getirir; ayrılık ve kopuş bağlantısı pasajın etkisidir, fiilin temel karşılığı değildir. 17:53 kendi başına ayrı bir ahlaki öğüt olarak kalır; bu karşılaştırma 17:43'teki her sözü düşmanlık saymaz, sözün yönü ve etkisini öne çıkarır.

Konuşmanın karşılanışında söz alanı belirginleşince, cümlenin aynı alanı yükseklik ve ölçüyle nasıl ilişkilendirdiğine dönüyoruz.

## Yüksekliğin Mertebesi

17:43'ten hemen önceki 17:42, koşullu bir tasavvurla odaktaki yüceliğe yeni bir yön açar: Allah'la birlikte başka ilahlar bulunsaydı, Arş'ın sahibine doğru yol ararlardı (17:42). {ar:ءَالِهَةٌ, tr:ʾālihatun, gloss:ilahlar} iddia edilen ilahları ve tapılan varlıkları düşündürebilir; {ar:لَٱبْتَغَوْا۟, tr:labtaghaw, gloss:yol ararlardı} onları bağımsız hüküm sahipleri değil, arayan özneler olarak kurar. Aranan {ar:سَبِيلًا, tr:sabīlan, gloss:yol} uzayıp geçilecek bir güzergâhtır; bu yol arayışı yolcuların hedefe bağımlılığını gösterir. {ar:ذِي ٱلْعَرْشِ, tr:dhī al-ʿarsh, gloss:Arş'ın sahibi} yükseltilmiş hükümdarlık tahtını çağrıştırırken, dayanak imgesi iktidarı ayakta tutan merkezi duyurur (17:42). Bu ikinci çağrışım ayrı bir ilahi nesne ya da mekân ileri sürmek yerine egemenliğin dayanağını belirginleştirir.

Bu koşullu sahnede {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} dikey yüksekliği taşırken, bir şeyin üst konuma geçip ötekini yenmesi ya da bastırması anlamını da duyurabilir. İnsanların sözleri karşılaştırma alanını verir {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden}; {ar:كَبِيرًا, tr:kabīran, gloss:büyük} ise ölçeği büyüterek üstünlük asimetrisini belirginleştirir. 17:42'de varsayımsal eşitlerin başka bir otoriteye yol araması bu mertebe ilişkisini somutlar: arayanların bağımlılığı, dikey yüksekliğin bu koşul içindeki üstünlük yönünü açar (17:42). Yol, arayanların katetmek istediği güzergâh olarak kalır; Allah'ın fiziksel yolculuğu değildir. Koşul sahici rakipler ya da gerçek bir mücadele ileri sürmez, ortak egemenlik iddiasının tutarlılığını sınar. Böylece üstünlük okuması bu ilişkiyle sınırlı kalırken yüceliğin dikey rengi korunur.

Ortak {ar:عُلُوًّا كَبِيرًا, tr:ʿuluwwan kabīran, gloss:büyük yücelik} ifadesi iki farklı yüksekliği karşılaştırmaya açar. 17:4'te bu çift yeryüzünde bozgunculuk yapan insanların yükselişini niteler; orada yükselme kınanan kibirli üstünlük taslamadır (17:4). 17:43'te özne Allah'tır ve {ar:عَمَّا يَقُولُونَ, tr:ʿammā yaqūlūna, gloss:onların söylediklerinden} bağı O'nu sözlerden uzak tutar; böylece ortak ifade insanın kendini yukarı koyuşundan ayrılan ilahi yüksekliği duyurur. Hakikat ile bâtılın ayrıldığı 22:62'de Allah'ın Yüce ve Büyük diye anılması, yüksekliği saygın mevki anlamıyla da buluşturur (22:62). {ar:كَبِيرًا, tr:kabīran, gloss:büyük} küçüğün karşıtı olan dereceyi taşırken 17:4'teki bozguncu taşkınlık ile 22:62'deki ilahi ululuk büyüklüğe ayrı yönler verir. Bu karşıtlık ortak ifadenin sağladığı yankıyla sınırlıdır: tek başına kasıtlı gönderme ya da sözdizimsel özdeşlik kanıtlamaz, 17:4'teki insan davranışını da Allah'a taşımaz.

53:7'deki {ar:ٱلْأُفُقِ ٱلْأَعْلَىٰ, tr:al-ufuq al-aʿlā, gloss:en yüksek ufuk}, 17:43'teki {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} için dikey yönü gözde canlandıran daha ihtiyatlı bir imge sunar (53:7). Bu benzetim yüksekliği analojik olarak görünür kılar; belirli bir göksel konum ya da fiziksel yükseliş ileri sürmez ve insanların sözlerinden uzaklığı temel okuma olarak tutar.

74:3'teki {ar:وَرَبَّكَ فَكَبِّرْ, tr:wa rabbaka fa-kabbir, gloss:Rabbini yücelt, O'nu büyükle} emri, Rabbin büyüklüğünü söylemeyi bir yüceltme ve ibadet eylemi olarak kurar (74:3). 17:43'teyse {ar:كَبِيرًا, tr:kabīran, gloss:büyük} emir değil, {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} ölçüsünü niteleyen sıfattır. Bu ortak büyüklük alanı 17:43'te betimlenen yüceliğe ibadet yönlü bir yankı katar; iki biçim arasındaki ilişki analojik kalır.

Yükselme ve üstün gelme imgesi, yeniden dirilişi imkânsız görenlerin tasavvur ettiği dirençle yan yana düşünülebilir. 17:49 kemikleri ve ufalanmış kalıntıları {ar:عِظَٰمًا وَرُفَاتًا, tr:ʿiẓāman wa-rufātan, gloss:kemikler ve ufalanmış kalıntılar} diye anar; 17:50'de taş ya da demire dönüşme ihtimali itirazın maddi direncini daha da sertleştirir {ar:حِجَارَةً أَوْ حَدِيدًا, tr:ḥijāratan aw ḥadīdan, gloss:taş ya da demir} (17:49, 17:50). 17:51'de odak kalıntılardan göğüslerinde büyük görünen şeye geçer: {ar:مِمَّا يَكْبُرُ فِي صُدُورِكُمْ, tr:mimmā yakbaru fī ṣudūrikum, gloss:göğüslerinizde büyüyen şeylerden} olağan anlamıyla içlerinde büyüyen şeyi anlatır; bir işin ağır ve güç gelmesine ilişkin kullanım da bu içsel büyüklüğe yük ve çaba boyutu katar (17:51). Cevap {ar:فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:faṭarakum awwala marratin, gloss:sizi ilk kez yaratmış olan} diyerek ilk yaratılışı gerekçe gösterir (17:51). Böylece karşı çıkışın maddi direnç imgeleri içsel ağırlığa, oradan ilk yaratılışı hatırlatan cevaba ilerler; 17:43 için düşünülen aşma yönü bu tartışmayla temas edebilir. {ar:كَبِيرًا, tr:kabīran, gloss:büyük} ile {ar:يَكْبُرُ, tr:yakbaru, gloss:büyür} aynı kökün farklı biçimleridir; bu yakınlık kasıtlı yankıyı tek başına kanıtlamaz, diriliş tartışması da yücelik dilinden bağımsız okunabilir.

Fâtiha'nın dosdoğru yola iletilme duası (1:6), 17:42'de aranan {ar:سَبِيلًا, tr:sabīlan, gloss:yol} ve 17:48'de bulunamayan yolla yan yana gelince, yönelişin üç ayrı hâlini görünür kılar: dua, varsayımsal arayış ve yol kaybı (17:42, 17:48). Fâtiha'daki dosdoğru yol ile bu iki ayetteki yol sözü aynı biçim ya da anlama sahip değildir. Odaktaki {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} ise duanın yöneldiği muhatabın yüksek konumunu belirtir; hidayet anlamı Fâtiha'nın duasında kalır, 17:43'teki yüceliğin karşılığı olmaz. Bu karşılaştırmanın katkısı sözlükçe özdeşlik değil, yöneliş ve muhatap ortaklığıdır.

17:42'deki koşullu sahneden sonra, 17:56 ve 17:57 bakışı Allah'tan başka çağrılanların bağımlılığına çevirir (17:42, 17:56, 17:57). 17:56'da insanların ileri sürdüğü iddiaların tersine, O'ndan başka çağrılanlar {ar:فَلَا يَمْلِكُونَ, tr:fa-lā yamlikūna, gloss:güç yetiremezler}; {ar:كَشْفَ ٱلضُّرِّ, tr:kashfa al-ḍurri, gloss:zararı gidermeye} ve {ar:وَلَا تَحْوِيلًا, tr:wa-lā taḥwīlan, gloss:başka hâle aktarmaya da} güçleri yetmez (17:56). 17:57'de insanların çağırdığı aynı özneler Rablerine {ar:يَبْتَغُونَ, tr:yabtaghūna, gloss:arıyor ve yöneliyorlar}; aradıkları {ar:ٱلْوَسِيلَةَ, tr:al-wasīlata, gloss:yakınlık vesilesini}, hangisinin daha yakın olacağı sorusuyla yön kazanır {ar:أَيُّهُمْ أَقْرَبُ, tr:ayyuhum aqrabu, gloss:hangisi daha yakın} (17:57). Vesile onları yaklaştıracak şeydir; burada fiziksel güzergâhtan çok yakınlığa erişim önemlidir. Aynı özneler Allah'ın rahmetini umar {ar:وَيَرْجُونَ رَحْمَتَهُۥ, tr:wa-yarjūna raḥmatahu, gloss:rahmetini umarlar} ve azabından korkar {ar:وَيَخَافُونَ عَذَابَهُۥ, tr:wa-yakhāfūna ʿadhābahu, gloss:azabından korkarlar} (17:57). Zararı gideremeyişin ardından gelen yakınlık arayışı ve rahmet umudu, onları ihtiyaç içindeki kullar olarak gösterir; yücelik de bağımsız rakiplerden çok yönelenlerin bağlı olduğu otoriteyle ilişkili duyulur. Bu okumanın sınırı çağrılan varlıkların bağımlılığıdır: ne 17:56 ne de 17:57 şefaat iddiasını tek başına çürütür, yüceliğin sözlük anlamını sabitlemez ya da bu varlıkların kimliğini genelleştirir.

Fâtiha'nın Rahmân ve Rahîm nitelemesi (1:3), 17:57'de umulan rahmetle yan yana gelerek 17:43'teki {ar:وَتَعَٰلَىٰ, tr:wa-taʿālā, gloss:ve yücedir} yüksek konuma merhamet tonu ekler: otorite hem yönelinen hem rahmeti umulan olur (17:57). Bu bağlantıda yücelik yüksek konum bildirmeyi sürdürür; “rahmet” anlamına dönüşmez. Fâtiha'nın açılış nitelemesi de 17:43'ün tek açıklaması değildir; yan yana geliş, birinde umulan, ötekinde ilahi nitelik olarak anılan merhameti görünür kılar.

17:60'taki Allah'ın insanları kuşatması, odaktaki yukarı yönlü {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} imgesini insanlardan uzaklıkla eşitlemeden düşünmeye yardım eder. {ar:أَحَاطَ بِٱلنَّاسِ, tr:aḥāṭa bi-l-nāsi, gloss:insanları kuşattı} kapsamlı ilişkiyi gösterir ve bilgi bakımından kavrayış olarak da anlaşılabilir (17:60). Aynı ayette Allah'ın Peygambere gösterdiği {ar:ٱلرُّءْيَا ٱلَّتِىٓ أَرَيْنَٰكَ, tr:al-ruʾyā allatī araynāka, gloss:sana gösterdiğimiz rüya}, insanlara yönelik {ar:فِتْنَةً لِّلنَّاسِ, tr:fitnatan li-l-nāsi, gloss:insanlar için bir sınama} diye nitelenir (17:60). Kuşatma, gösterilen rüya ve sınanma 17:60 içindeki ardışık hareketlerdir; bu sınama 17:43'ün anlattığı bir olay değildir.

Aynı 17:60 insan taşkınlığını {ar:طُغْيَٰنًا كَبِيرًا, tr:ṭughyānan kabīran, gloss:büyük bir azgınlık} diye adlandırır. Sözcüğün olağan anlamı azgınlık ve sınır aşmadır; taşan su gibi yükselip süpürme imgesi bu taşkınlığa ihtiyatlı bir karşı-görüntü ekler. {ar:عُلُوًّا كَبِيرًا, tr:ʿuluwwan kabīran, gloss:büyük yücelik} ile paylaşılan büyüklük ölçüsü ilahi yücelik ile insan taşkınlığını karşılaştırabilir ve aralarındaki yön farkını belirginleştirebilir. Su imgesi sözlük anlamının yerini almaz; bu ortak ölçü de kasıtlı bir benzetmeyi kanıtlamaz.

</source_prose>
