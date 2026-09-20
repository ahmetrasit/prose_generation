# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:22**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.middle.claims.json`

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
- Refer to source paragraphs as `31:22 ¶N`.

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

`(31:22 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:22",
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
        "citation": "(31:22 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_22/31_22.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_22/31_22.middle.claims.json \
  --ayah-ref 31:22
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_22/31_22.prose.editorial.tr.md`

<source_prose>
## Şartın Kurduğu Eylem

31:22, yüzünü Allah’a teslim edip iyilik yapan her kimsenin en sağlam kulpa tutunduğunu söyler. Başındaki {ar:وَ, tr:wa-, gloss:ve} önceki söze bağlanır; hemen ardından gelen {ar:مَن, tr:man, gloss:her kim} ise bu ayette yeni bir şart açar, önceki sahne hakkında ayrıca hüküm vermez. Koşulun öznesi belirli bir kişi ya da topluluk değildir: onu kim yerine getirirse söz ona açıktır. Bu açıklık, yüzünü Allah’a teslim edip iyilik yapma şartını gevşetmez.

Şarttaki {ar:يُسْلِمْ, tr:yuslim, gloss:teslim ederse} cezmli muzari fiil, teslimi olmuş bitmiş bir olay gibi anlatmaz; yerine getirilmesi gereken eylem olarak kurar. Ardından gelen {ar:وَهُوَ مُحْسِنٌۭ, tr:wa-huwa muḥsinun, gloss:o iyilik yapan biri olarak} aynı özneye dönen bir hâl cümlesidir. Buradaki {ar:وَ, tr:wa-, gloss:ve}, iyiliği ayrı bir etiket olarak eklemek yerine teslimin gerçekleştiği hâle katar; açık zamir {ar:هُوَ, tr:huwa, gloss:o} da yargıyı aynı kişi hakkında tamamlar. IV. bâbdan etkin ortaç {ar:مُحْسِنٌۭ, tr:muḥsinun, gloss:iyilik yapan}, güzelleştirme ve iyi yapma alanını güzel görünüşte değil, iyilik eyleyen kişide gerçekleştirir. Belirli bir davranış, yararlanıcı ya da bu hâlin süresi seçilmez; teslim ve iyilik, aynı öznenin şart içindeki eylemini birlikte kurar.

Yanıtı başlatan {ar:فَ, tr:fa-, gloss:bunun üzerine} doğrudan bu şartın sonucuna geçer: {ar:قَدِ ٱسْتَمْسَكَ, tr:qadi istamsaka, gloss:gerçekten tutunmuştur} yapısındaki qad ve mâzî fiil, koşul yerine geldiğinde tutuşun gerçekleşmiş olduğunu bildirir. Bu sonuç şartı ortadan kaldırmaz; koşuldan bağımsız bir güvence ya da her kişinin akıbetine ilişkin ayrıntılar da sunmaz. Açık özne ve tamamlanmamış eylem şart bölümünde, tamamlanmış tutuş ise yanıt bölümündedir. Böylece kişi, belirtilen eylem yerine geldiğinde kulpu gerçekten kavramış görünür.

## Yüzün Taşıdığı Yön

Şartın ilk nesnesi bedenin somut yüzüdür. {ar:وَجْهَهُۥٓ, tr:wajhahu, gloss:yüzünü} iyelik ekiyle koşul öznesine bağlıdır; Form IV {ar:يُسْلِمْ, tr:yuslim, gloss:teslim eder} bu yüzü nesne alır, ardından gelen {ar:إِلَى, tr:ilā, gloss:-e doğru} ise yönelişin ucunu gösterir. Yüz böylece bedenin ön tarafı olarak kalırken kişiye bir yön ve amaç da verir; ayet yüzün bedenen hangi hareketi yaptığını ayrıca anlatmaz. {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah’a} adı genel bir dinî sınıf, yemin ya da seslenme değil, yönelişin belirli muhatabıdır. Cümle yapılan eylemin bütün sonuçlarını açıklamaz; yönelişin ucu böylece açıkça Allah olarak adlandırılır.

{ar:يُسْلِمْ, tr:yuslim, gloss:teslim eder} için verilen bir kullanım, buyruğu kabul edip ona boyun eğmeyi içerir. Allah’a yöneliş ve aynı öznenin etkin iyilik hâliyle birleşince bu kullanım, ilahî yönlendirmeyi kabul etme tonunu duyurur; ayette ayrıca alıntılanmış bir buyruk yoktur. Fiilin bir şeyi başkasının eline ve denetimine verme kullanımı da yüzün özneye ait bir nesne, Allah’ın açık yöneliş hedefi olmasıyla birleşir. Terk edip bırakma anlamı bu cümleye taşınmaz; bu temas teslimi Allah’a emanet ediş gibi derinleştirir.

Allah adının tapma eylemi ve tapınılan varlıkla ilgili kullanımları, yönelişin muhatabını kulluğun da muhatabı olarak duyurur; bu çağrışım Allah’ı genel bir “tapınılan varlık” adına dönüştürmez, özel ad olarak tutar. Buradan yeni bir türetme, sığınak ya da şaşkınlık anlamı da çıkmaz. Bu ilişki, 31:32’de yolcuların {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu d-dīn, gloss:dini yalnız O’na özgüleyerek Allah’a yakardılar} diye anlatıldığı sahnede bağlamsal olarak belirginleşir (31:32). 31:25’te Allah’ı yaratıcı olarak tanımanın çoğunlukta bilgiye dönüşmemesi, 31:32’deki korku anı duası ve kurtuluş sonrasındaki farklı tutumlarla birlikte düşünüldüğünde, odaktaki yönelişi yalın tanıma ve acil yakarışın ötesine taşır. Kurtuluş sonrasındaki ayrışma herkesin bağlılıktan vazgeçtiğini göstermez; ölçülü davranışı sürdürenlerin varlığı, kişisel emanet edişin eylem içinde devam edebileceğini görünür kılar.

{ar:وَجْهَهُۥٓ, tr:wajhahu, gloss:yüzünü} üzerindeki iyelik eki yüzü koşul öznesine bağladığından, bu somut taşıyıcı bütün kişiyi de temsil edebilir. Bu, yüzün kişi yerine geçtiği anlamına değil, kişiye açılan bir yorum katmanına gelir; yüzün kendisi bütün hayatın sözlük karşılığı olmaz. Yüzün kumaşın iki yanı için kullanılan anlamı dış ve iç ilişkisinin somut bir modelini sunar; kişinin içindekinden farklı bir yüz göstermesine dair ayrı kullanım da bu karşıtlığı keskinleştirir. Bu iki benzetme dış/iç karşılaştırmasını zenginleştirir, ancak kumaş ayette yer almaz ve tutarsız yüz sunumu yalnız belirli bir söz öbeğine bağlıdır; odak kişisini iki yüzlü biri diye tanımlamaz. Görünen yüz tek başına içtenliği kanıtlamaz; beden yüzü dış yönelişin taşıyıcısı olarak kalırken iç hâl ayrı bir boyut olarak korunur.

Yüzle açılan bu dış ve iç ilişki, komşu bağlamlarda davranışa taşınır. 31:18’de {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-n-nās, gloss:insanlara karşı yanağını böbürlenerek çevirme} uyarısı kibirli beden yönelişini karşıya koyar; 31:19’da {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-qṣid fī mashyika, gloss:yürüyüşünde ölçülü ol} ve {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtika, gloss:sesini alçalt} çağrıları hareket ile sözü ölçülü kılar (31:18; 31:19). 31:20’de nimetlerin {ar:ظَٰهِرَةًۭ وَبَاطِنَةًۭ, tr:ẓāhiratan wa-bāṭinatan, gloss:görünür ve içsel} diye çiftlenmesi dış ve iç hâli birlikte düşündürür; 3:134’te rahatlıkta da sıkıntıda da verme, öfkeyi tutma ve insanları bağışlama örnekleri buna kişiler arası iyilikleri ekler (31:20; 3:134). Bu sahneler {ar:مُحْسِنٌۭ, tr:muḥsinun, gloss:iyilik yapan} niteliğini ölçülü hareket, kamusal söz ve kişiler arası eylem içinde görünür kılar; örnekler iyiliğin bütün biçimlerini tüketmez ve muhsin’i belirli bir yürüyüş ya da konuşma buyruğuna dönüştürmez. S-l-m kökünün kusur ve zarardan uzak bütünlük alanı da dışta görünen yüz ile iç bağlılığın aynı kişide buluşmasıyla bir esenlik tonu kazanır. 2:112’de teslimin ardından korku ile hüznün kalkması bu tona bağlamsal dayanak verir; bu yankı odak fiilin teslim anlamını koruyarak dış ve iç bütünlük yönelişini zenginleştirir (2:112).

Bu yüzün Allah’a yönelmesi, izlenecek yolun nasıl seçildiği sorusuna açılır. 31:21’de {ar:ٱتَّبِعُوا۟ مَآ أَنزَلَ ٱللَّهُ, tr:ittabiʿū mā anzala Allāh, gloss:Allah’ın indirdiğine uyun} çağrısına {ar:بَلْ نَتَّبِعُ مَا وَجَدْنَا عَلَيْهِ ءَابَاءَنَا, tr:bal nattabiʿu mā wajadnā ʿalayhi ābāʾanā, gloss:hayır, atalarımızı üzerinde bulduğumuz şeye uyarız} cevabı verilir; vahiy ile hazır bulunmuş ve devralınmış toplumsal pratik ayrı izleme gerekçeleridir (31:21). 4:125’te dosdoğru İbrahim’in yolunu izlemek de başka bir yöneliş örneği sunar (4:125). Bu karşılaştırma her mirasın reddini değil, izleme gerekçelerinin tartılmasını gösterir; yüz seçilmiş bağlılığın yönünü taşır.

Yol imgesi, bu seçimin karşılaştığı çekişi de belirginleştirir. 31:6’da Allah’ın yolundan saptırma sözü bir yolu ve ondan uzaklaştırılmayı sahneye koyar; 2:256’da doğru yolun sapmadan ayrılmasıyla kopmayan kulp yan yana gelir (31:6; 2:256). Yüzün yönelişi böylece gerçek bir güzergâh gibi düşünülebilir, fakat mekânsal yolculuk anlatılmaz. 31:7’de böbürlenerek sırt çevirme ve kulaklarda ağırlık varmış gibi işitmeye kapanma, yönelmiş yüze bedensel bir karşılık ekler (31:7). Bu karşıtlık fiziksel sağırlık tanısı koymaz ve odak fiil her fiziksel dönüşü yasaklayan bir buyruk değildir. Tutunma sözü şimdi bu rakip güzergâhların çekişine karşı seçilen yönün nasıl korunduğunu gösterir.

## Tutulan Dayanak

Yanıttaki Form X {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:sıkıca tutundu}, öznenin iradesini ve çabasını işe katan etkin bir kavrayıştır: bir dayanağı yalnızca bulmayı değil, ona bağlanıp elde tutmayı anlatır. Kökün verilen kullanımı, bir şeyi elinde tutarak kaybolmasını ya da serbest kalmasını önlemeyi de kapsar; bu yüzden kavrayış sürdürülmüş bir eylem olarak duyulur. {ar:بِٱلْعُرْوَةِ, tr:bi-l-ʿurwah, gloss:kulptan tutunarak} yapısındaki bā, belirli kulpu hem temas noktası hem tutuşun aracı yapar; nesne ve temas yolu böylece açıkça gösterilir. Bā’nın isme bitişik yazılması bu dilbilgisel bağı görünür kılar, ancak yazıdaki bitişme yeni bir kök anlamı üretmez; edat da kulpun sözlük anlamını ya da tek başına bir güvenceyi belirlemez. Kulp, tutuşun açık nesnesi ve somut dayanağı olarak belirir.

Tutulan şey {ar:ٱلْعُرْوَةِ, tr:al-ʿurwah, gloss:kulp} ile adlandırılmış somut bir kulp ya da halkadır. Belirli tekil isim, ardından gelen dişil üstünlük biçimiyle uyum içindedir: {ar:ٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:al-ʿurwah al-wuthqā, gloss:en sağlam kulp}. Bu biçim en yüksek sağlamlığı tek, tanınabilir tutamağa bağlar; başka dayanakları dışlamaz. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} için verilen kullanımlar güvenilir bulmayı ve fiziksel dayanıklılığı birlikte taşır: etkin tutuş güvenilir olana dayanma rengini, sıfat ise sağlamlığı eldeki desteğe verir. Burada sözcük kulpu niteleyen sıfattır; dışarıdan eklenmiş garanti, ahit ya da belge adı değildir. Böylece destek hem elle kavranan sağlamlık hem de güvenilirlik taşır.

Bağlama ve bir şeyi sıkıca bağlayan araç kullanımları, tutulan nesneyle birleşerek ayrı bir halat ya da bağ imgesi sunar; dalga baskısı bu tutuşun niçin önemli olduğunu belirginleştirir (31:32). Bu bağlantı, {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} sözcüğünü ipin adına dönüştürmez: odak ayette o, kulpu niteleyen sıfattır. Aynı şekilde tutuşun kaybolmayı ya da serbest kalmayı önleme kullanımı sürekliliği desteklerken, kokuyu üzerinde tutma kullanımı için gereken koku taşıyıcısı bu sahnede yoktur. Halat imgesi böylece temel kulp anlamının yerini almadan, baskı altında sürdürülen tutuşa bağlanır.

22:11’de kenar üzerinde ibadet eden kişinin iyilik gelince güvenip sınama gelince yüz çevirmesi, tutunma noktasının karşısındaki maruz kalma imgesini verir; 2:256’daki kopmayan kulp ise dayanmanın karşı kutbudur (22:11; 2:256). Bu iki sahne, {ar:ٱلْعُرْوَةِ, tr:al-ʿurwah, gloss:kulp} sözcüğünün anlamını değiştirmeden, tutuş ile sağlamlığın baskı altındaki ilişkisini açar. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} içindeki güvenip dayanma yankısı da burada duyulur: tutuş sahip olmaktan çok koşullar değişirken dayanağı sürdürmeye yaklaşır. Bu karşılaştırma sınanmayı ortadan kaldırmaz; güvenilir desteğin değerini sınamanın içinden görünür kılar.

Eldeki kulptan başka bir ölçekte, dayanak yük taşıyan yapı gibi görünür. 31:10’da görülen sütunlar olmaksızın kurulan gökler görünmeyen desteği, savrulmayı önleyen sabit dağlar ise ağırlık ve sabitlemeyi öne çıkarır; 9:109’da sağlam temel, çökmekte olan bir uçta kurulan yapıyla karşılaştırılır (31:10; 9:109). Bu ayrı sahneler, el kavrayışını tekrarlamadan tutunmayı öznel güven duygusundan yük taşıyan yapısal desteğe genişletir. Bu bağlantı odak ayetin fiziksel açıklaması ya da genel bir koruma vaadi değildir; görünmeyen desteğin tümünü tarif etmek yerine, destekleme ile çöküş arasındaki karşıtlığı tutuşun yanına getirir.

## Değişen Koşullarda Tutuş

Yapı imgelerinden sonra bağlam bu kez hareket hâlindeki bir yolculuğa geçer. 31:31’de gemi {ar:تَجْرِي فِي ٱلْبَحْرِ, tr:tajrī fī l-baḥri, gloss:denizde akıp gider}; bu, krizden önceki olağan yol alışını verir. 31:32’de deniz çalkalanır ve {ar:غَشِيَهُم مَّوْجٌۭ, tr:ghashiyahum mawjun, gloss:bir dalga onları örter}; örtücü dalga alışılmış yön duygusunu sarsar. Yolcular bu kuşatılmışlıkta {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu d-dīn, gloss:dini yalnız O’na özgüleyerek Allah’a yakardılar}, ardından karaya çıkarılarak kurtarılır (31:32). Kurtuluş sonrasında {ar:فَمِنْهُم مُّقْتَصِدٌۭ, tr:fa-minhum muqtaṣidun, gloss:içlerinden ölçülü davrananlar oldu}: bazıları ölçülü tutumu sürdürürken başkaları sözünden döner ve nankörleşir (31:32). Böylece yolculuk, dalga, dua, karaya çıkış ve sonrasındaki ayrışma ayrı aşamalar olarak görünür.

Bu aşamalar, {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:tutundu} fiilini sakin yol alıştan krize ve kurtuluş sonrasına uzanan bir tutuş olarak da duyurur. Dalga güvenilir dayanağın değerini istikrarsızlıkta açar; karaya çıkış krizden sonraki koşulu belirler; ölçülü ve nankör tutumların ayrılması ise bağlılığın sürdürülüp sürdürülmediğini görünür kılar. Bu karşılaştırma odak kişisini gemicilerle özdeşleştirmez, ayrıca 31:32’deki kriz duası ile sonrasındaki ayrışma gemi sahnesini tutarsız davranışa örnek olarak okumaya da izin verir. Bu ikinci okuma, dizilimi zorunlu bir zaman sınaması saymayı ya da herkesin kurtuluşla birlikte yön değiştirdiğini ileri sürmeyi gerektirmez. Yolculuk sahnesi böylece tutuşu yalnız acil anda edinilen bir sığınak olmaktan çıkarıp değişen koşullara yayılan bir yöneliş olarak genişletir.

Dalga örtmesi kuşatılmışlığı, çalkantı yön duygusunun sarsılmasını, karaya çıkarılmak ise tehlikeden çıkışı belirginleştirir; bunlar aynı koşulun tekrarları değil, güvenilir tutamağın hangi değişim içinden okunabildiğini gösteren ayrı aşamalardır. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} niteliği bu sahnede bedensel sarsılmazlık değil, kırılganlık içinde de dayanılabilirlik verir. Bu karşılaştırma odak kişisini denizci ya da yaralı diye tanımlamaz. Arapça biçimler de burada eylem bildirir: Form IV {ar:يُسْلِمْ, tr:yuslim, gloss:teslim eder} yüzü nesne alan teslim fiilidir, “ısırılmış kişi” adı değil; Form X {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:tutundu} dayanağı kavrama eylemidir, artakalan yiyecek ya da kuvvet miktarını adlandırmaz. Böylece sağlam tutuş, etkilenmemiş bir özne varsaymadan istikrarsızlıkta dayanılabilirliği taşır.

Dalga dış koşulların tutuşu nasıl sınadığını gösterirken, 31:17 aynı sürdürme sorusunu gündelik eyleme taşır: namaz kılmak, iyiliği emretmek, kötülükten sakındırmak ve başına gelene sabretmek birlikte anılır (31:17). 22:41’deki kamusal iyi davranışlar, {ar:مُحْسِنٌۭ, tr:muḥsinun, gloss:iyilik yapan} kişiyi devam eden eylem çizgisine bağlar; 11:49’da sabırla akıbetin yan yana gelişi de tutuşu sınama altındaki özdenetime yaklaştırır (22:41; 11:49). 31:17’deki {ar:إِنَّ ذَٰلِكَ مِنْ عَزْمِ ٱلْأُمُورِ, tr:inna dhālika min ʿazmi l-umūr, gloss:bu kararlılık isteyen işlerdendir} sözü işe yüreğini kesin biçimde bağlamayı ve amaçta kalarak sürdürmeyi düşündürebilir; iki katkı, tutuşu kararlı devam yönünden derinleştirir. Sabır ve kararlılık odak fiilin sözlük anlamı değildir; bu bağlamlar dünyevi sonuç garantilemez ve okur adına tek bir yol seçmez. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} sıfatının en sağlam olanı seçme yankısı, bu eylem çizgisini baskının zaman içindeki sınamasıyla buluşturur.

## İşlerin Sonucu

Bu devam eden yöneliş, son cümlede işlerin bütününe genişler. Yanıtın ardından gelen {ar:وَ, tr:wa-, gloss:ve}, önceki tutuşu kesmeden yeni bir isim cümlesi açar. {ar:وَإِلَى ٱللَّهِ, tr:wa-ilā Allāhi, gloss:ve Allah’a doğru} ifadesinde yönelme başa alınarak hedef çerçevelenir. Açılıştaki {ar:إِلَى ٱللَّهِ, tr:ilā Allāhi, gloss:Allah’a doğru} ile kapanıştaki aynı Allah adı iki ucu buluşturur: önce kişinin yüzü Allah’a yönelir, sonunda bütün işlerin sonucu ona bağlanır. Bu kişi ölçeğinden bütün işlerin alanına uzanan halka 31:22’nin yerel yapısıdır, surenin tümüne yayılan mimari bir sav değildir. Allah özel adı her iki uçta da aynı kalır ve verilen tapma eylemi ile tapınılan varlık ilişkisi kapanıştaki hedefi kulluğun da yöneldiği yer olarak duyurur.

Hedef öne geldikten sonra tekil sonuç başı {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} ve onu tamamlayan belirli çoğul {ar:ٱلْأُمُورِ, tr:al-umūri, gloss:işler ve durumlar} gelir. Tekil sonuç pek çok meseleyi ve hâli toplar; bu çoğul açık emirlerin ya da adı konmuş bir makamın listesi değildir. Tamlamadaki ilişki iki yönde açık kalır: işlere ait bir sonuç da, işleri izleyip onlardan doğan sonuç da duyulabilir. Sözcük ailesindeki topuk ve geride kalan iz kullanımlarından hemen ardından gelmeye uzanan bir yankı vardır; 22:41’de eylemlerin ardından aynı sonuç cümlesinin gelmesi bunu bir sonraki eşiğe yaklaştırır (22:41). Bu yankı genel bir zaman kuralı, dönüşümlü nöbetleşme ya da yalnızca ceza anlamı kurmaz. {ar:عَٰقِبَةُ ٱلْأُمُورِ, tr:ʿāqibatu al-umūri, gloss:işlerin nihai sonucu} böylece işlerin vardığı son durumu adlandırır.

22:41’de namaz, zekât, iyiliği emretme ve kötülükten sakındırma sıralandıktan sonra aynı “işlerin sonucu Allah’a aittir” cümlesi gelir; 65:9’da ise bir işin yıkıcı karşılığı tadılır (22:41; 65:9). Bu iki sahne, {ar:ٱلْأُمُورِ, tr:al-umūri, gloss:işler} alanının iyi ve kötü eylemleri kapsadığını, {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} sözünün de önceki işlerin ardından gelen eşiğe temas edebildiğini gösterir. Sonuç böylece eylemlerin izini taşır; her karşılığın hemen görüneceği, bütünüyle bilinebileceği ya da belirli bir kişide nasıl sonuçlanacağı seçilmez. Tutulan dayanakla sonucun Allah’a yönelmesi yan yana durduğunda, bugünkü eylemden nihai sonuca uzanan çizgi görünür olur; son yine Allah’a aittir.

31:22’nin sonuç sözü, çevresindeki somut sahnelerle de açılır. 31:24’te kısa bir yararlanmanın ardından ağır azap gelir; 31:26’da göklerde ve yerde olanların Allah’a ait olduğu bildirilir. 31:29’da gece gündüze, gündüz geceye geçirilir, güneş ve ay belirlenmiş bir süreye kadar akar; yapılanlar da bilinir. 31:34 ise yarın ne kazanılacağıyla ölümün hangi yerde gerçekleşeceğinin bilinmediğini söyler (31:24; 31:26; 31:29; 31:34). Bu bağlamlar “işler”i soyut bir buyruklar listesi olmaktan çıkarıp yaşanan eylemler, ilahî yönetim ve henüz bilinmeyen gelecekler içine yerleştirir.

Bu sıralamadan, tek bir dönüş anından çok değişen evreler boyunca uzanan bir güzergâh sezen yakın ama ayrı, ihtimalli bir okuma da çıkar. {ar:وَجْهَهُۥٓ, tr:wajhahu, gloss:yüzünü} burada yön tutan insan yüzüdür, zaman sözcüğü değildir; {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:tutundu} fiilinin elde tutma anlamı sağlam kulpu sonraki sonuca bağlar. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} için verilen güvenilirlik anlamı bu iki uç arasındaki dayanağı duyurur. Ayette ayrıca bir zaman adı bulunmaz; önce-sonra duygusu eylemlerin ve sonucun sırasından doğar. Bu, süreklilik hakkında ihtimalli bir okuma olup daha geniş bir gelecek vaadi kurmaz. Yöneliş, eylem ile sonucun sırasını izleyen bir devamlılık ihtimali olarak kalır.

31:29’daki karşılıklı geçiş, bu zaman okumasına ayrı bir göksel imge ekler. Gece gündüze, gündüz geceye girer; güneş ile ay belirlenmiş bir süreye kadar akar. Bu değişim, {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} sözünü birinin ardından ötekinin gelmesi ve yerini alması olarak da duyurabilir (31:29). Süre göksel akışı sınırlar; tutamağı niteleyen {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} tekrarlanan geçişle birlikte değişim içinde güven duygusu verir. Gecenin evresindeki koyulaşma karanlık imgesini ekleyebilir, ancak {ar:يُولِجُ, tr:yūliju, gloss:içine geçirir} “karartmak” demek değildir. Aynı ayetteki {ar:وَجْهُ ٱلنَّهَارِ, tr:wajhu n-nahār, gloss:günün başı ve ilk saatleri} kuruluşu her gündüz evresini yeni bir başlangıca benzetmeye yarar; 31:22’deki {ar:وَجْهَهُۥٓ, tr:wajhahu, gloss:yüzünü} sabah ya da şafak anlamına gelmez. 31:29’un başlıca tanıklığı Allah’ın kudretidir; yapılanları bilme teması da cümlede yer alır. Bu döngü okuması her işin döngüsel olduğunu ya da teslimiyetin geleceği önceden bildirdiğini ileri sürmez. Gece ile gündüzün karşılıklı geçişi, yine de sonucun yalnız evreler tamamlandıktan sonra değil, geçiş sürerken de karşılaşılan bir ufuk gibi duyulmasını sağlar.

## Genişleyen Benzetmeler

Göksel geçişten ayrı bir bakışta, sonuçla tutuş arasındaki mesafe keşifsel bir ticari benzetmeye izin verir. Önce yüzün şimdi Allah’a yöneltilmesi, elde sağlam kulpun tutulması ve işlerin sonucunun daha sonra gelmesi bir araya gelir; bu sıra, ileride sonuçlanacak güvence altındaki bir taahhüt gibi duyulabilir. {ar:يُسْلِمْ, tr:yuslim, gloss:teslim eder} için verilen, bedelin önceden ödendiği vadeli satış kullanımı benzetmeye yalnızca bağlamdan katılır: sözcüğün satış anlamı ayette etkin değildir; şimdiki teslim, güvenilir tutuş ve sonraki sonuç ayrı ayrı temas eder. Fiilin bir şeyi başkasının eline ve denetimine verme kullanımıyla Allah’ın hedef ve alıcı olması, {ar:ٱلْأُمُورِ, tr:al-umūri, gloss:bütün işler} kapsamını kişinin kendisini ve işlerini Allah’a emanet ediş gibi de duyurur.

Bu benzetmede Allah özel adıyla kalır; tapma eylemi ile tapınılan varlık ilişkisi taahhüdün yöneldiği muhatabı kulluğun da muhatabı kılar. Tapma ticari bir sözlük anlamına dönüşmez. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} için verilen kullanımlar arasında tarafları bağlayan güvence altındaki anlaşma da vardır; etkin tutuş ve yüzü teslim etme bu çağrışımı taşır, fakat sözcük anlaşma adı değil, kulpu niteleyen sıfattır. Aynı ticari alanda {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} bir karşılık ya da başka bir bedelin yerine geçen ödeme gibi düşünülebilir. Verilen kullanım alanı, kusurlu mal için satıcıdan sonradan karşılık istemeyi ve mal ödeme alınana kadar satıcıda durup bu sırada kaybolursa zararın satıcıya ait olmasını da çağrıştırır. Ayette alıcı, satıcı, mal, kusur ya da kayıp adlandırılmaz; bu benzetmenin sınırı burada belirir ve odak cümle bütün işlerin sonucunu Allah’a yöneltir.

Başka bir maddi birleşim, ticari ilişkiden değil kulp ile elde tutuşun alet hâline gelmesinden doğar. Somut {ar:ٱلْعُرْوَة, tr:al-ʿurwah, gloss:kulp} ile {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:tutundu} kavrayışı, tek kulplu bir kovayı elde tutup çekme imgesine açılır; ayette kova yoktur. {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} için verilen bağlama aracı kullanımı, tutulan desteği sabit bir çizgi ya da ip gibi düşündürebilir; kelime burada sıfattır, ipin adı değil. Merdiven imgesini {ar:يُسْلِمْ, tr:yuslim, gloss:teslim eder} tek başına doğurmaz; açık tutuş, kulp ve daha sonra gelen sarp yol düşüncesi basamaklarla yukarı taşıyan aracı birlikte kurar. Bu öğeler bir araya geldiğinde durgun kulp çekme, çekilme ve yükselme hareketine katılır; {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} sarp geçişin sonu ya da kayalık bir çıkıntı gibi duyulabilir. Bu imge zorunlu olarak dağ geçidi ya da gerçek bir tırmanış anlatmaz; durağan kulpu hareket içindeki bir temas noktasına dönüştürür.

## Devredilemeyen Eylem ve Bilinmeyen Gelecek

Bu uzak benzetmeler ihtimalli kalırken, 31:33 kişinin eylemini ve sonucunu başkasına devredememesini somut bir aile ilişkisi üzerinden gösterir. Bir ebeveyn çocuğunun, çocuk da ebeveyninin yerine geçemez; ardından Allah’ın vaadinin gerçek olduğu ve dünya hayatıyla aldatıcının yanıltmasına karşı uyarı gelir (31:33). Aile, tek tek durumları kapsayan {ar:ٱلْأُمُورِ, tr:al-umūri, gloss:işler ve meseleler} alanındaki somut bir meseledir, bütün işleri tüketen örnek değil. Kişinin {ar:يُسْلِمْ وَجْهَهُۥٓ, tr:yuslim wajhahu, gloss:yüzünü teslim etmesi} başkasının onun adına yapabileceği bir eylem değildir; {ar:عَٰقِبَةُ, tr:ʿāqibatu, gloss:sonuç} da bir başkasının taşıyacağı sona dönüşmez. Karşılıklı yerine geçememe, vekâlet yolunun kesilmesine ancak temkinli bir benzetme sunar; bu gerçek bir kesme ya da aile bağlarını koparma değildir. Geçici dünya hayatı ve aldatan kişi, sonrası bilinmezken kurulan yanlış güveni gösterir; geçici görünüş nihai sonucu güvenceye alamaz. Böylece yakın aile bağı korunurken kişinin kendi hesabını devredemeyeceği belirginleşir.

Kendi hesabını devredememenin ufkunda 31:34 yarın ne kazanılacağı ve hangi yerde ölüneceği sorularını somutlaştırır. {ar:وَمَا تَدْرِي نَفْسٌ, tr:wa-mā tadrī nafsun, gloss:hiçbir nefis bilmez} ifadesinin tekrarı, kişinin bu konuda bilgi edinme sınırını vurgular. {ar:تَدْرِي, tr:tadrī, gloss:bilir} fiilinin olağan anlamı bilmek ya da tanımaktır; “hangi toprakta öleceği” sorusunun yanında yolun doğrultusu veya rüzgâr yönüyle ilgili uzak bir rota benzetmesi düşünülebilir, ama bu fiilin sözlük anlamı yol çizmek değildir. {ar:مَاذَا تَكْسِبُ غَدًۭا, tr:mādhā taksibu ghadan, gloss:yarın ne kazanacağını} yakın gelecekteki kazancı, {ar:بِأَىِّ أَرْضٍۢ تَمُوتُ, tr:bi-ayy arḍin tamūtu, gloss:hangi yerde öleceğini} ise ölümün yerini sorar; ikisi de “işler” alanına girer, fakat belirli bir gelecek ya da ölüm yeri vermez (31:34). {ar:ٱلْوُثْقَىٰ, tr:al-wuthqā, gloss:en sağlam} kulpa tutunmak ve {ar:عَٰقِبَةُ ٱلْأُمُورِ, tr:ʿāqibatu al-umūri, gloss:işlerin nihai sonucu}na yönelmek, henüz bilinmeyen yarının kazancı ve ölüm yeri ufkunda da güvenilir yönelişin anlamını korur.

</source_prose>
