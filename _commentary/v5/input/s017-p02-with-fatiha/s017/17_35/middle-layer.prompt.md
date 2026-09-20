# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:35**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.middle.claims.json`

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
- Refer to source paragraphs as `17:35 ¶N`.

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

`(17:35 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:35",
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
        "citation": "(17:35 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_35/17_35.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_35/17_35.middle.claims.json \
  --ayah-ref 17:35
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_35/17_35.prose.editorial.tr.md`

<source_prose>
## Ölçünün İki Usulü

Âyet, ölçtüğünüzde ölçüyü tam yapmayı ve düzgün terazide tartmayı buyurur: {ar:إِذَا, tr:idhā, gloss:ne zaman} {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçüyü} eksiksiz tamamlayın; {ar:وَ, tr:wa, gloss:ve} tartma buyruğuna da uyun. Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} önceki söylemle bağı açık tutar; bu kesit hangi önceki buyruğun sürdürüldüğünü belirlemez. Hemen ardından gelen {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} somut ölçme işini başlatır; ortadaki {ar:وَ, tr:wa, gloss:ve} ise {ar:زِنُوا, tr:zinū, gloss:tartın} emrini yanına getirir. İki emir ritimde eşleşir, hacim ölçüsü ile tartmayı ayrı usuller olarak düzenler.

Ölçüyü tamamlama buyruğunun biçimi, eylemi doğrudan ölçünün kendisine bağlar. {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} bir şeyi gereği gibi ve eksiksiz yerine getirmeyi bildirir; IV. bâbın çoğul muhataplara yöneltilmiş emridir. Doğrudan nesnesi {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçme} sözcüğüdür: bu isim-mastar hem hacim ölçüsünü hem ölçme işini adlandırır, dolayısıyla tamamlanması istenen şey belirli bir mal değil ölçme eyleminin kendisidir. Aynı ölçme ailesi {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} fiilinde yeniden duyulur. Fiilin ortasındaki zayıf yâ görünür biçimde düşerek şeklini kısaltsa da isimle fiil arasındaki bağ sürer; bu yerel yankı biçim bağını duyurur, yeni bir sözlük anlamı kurmaz. {ar:إِذَا, tr:idhā, gloss:ne zaman} yükümlülüğü her ölçme gerçekleştiğinde devreye sokar. Çoğul hitap eylemi muhataplara verir; böylece genel eksiksizlik, her ölçümde tamamlanması gereken fiilî göreve dönüşür. Uygulamanın yeri ve sıklığı, herkesin aynı anda davranacağı kurumsal düzen, ölçü birimi ve alışverişin tarafları açık kalır.

Tartma buyruğu, tartılacak nesneyi ayrıca adlandırmadan farklı mallara açık bir işlem alanı bırakır. {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} öbeği tartma aracını gösterir. {ar:زِنُوا, tr:zinū, gloss:tartın} fiilinin tartma işiyle ve araç bildiren bi- ile kurduğu ilişki, qistās’ı tartılan ikinci nesne değil fiziksel terazi yapar. Böylece terazi, dürüst niyetin yanında miktarı özel tahmine bırakmadan sınamaya elverişli ölçülebilir bir dayanak sağlar. Ayet terazinin modelini ve ölçü birimini belirtmez. Qistās sözcüğünün kökeni ve seslendirilmesi, ödünçleme olup olmadığı ve adalet köküyle ilişkisi kesin değildir; bu etimolojik belirsizlik, buradaki tartı aracı anlamını değiştirmez.

Terazinin niteliği, ölçümün doğrultusunu da belirginleştirir. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} sözcüğü dik durma ve düzgünlük imgesini aracın hizasına taşır. Form X ortaç biçimindeki sıfat {ar:ٱلْقِسْطَاسِ, tr:al-qisṭāsi, gloss:terazi} sözcüğüne dilbilgisel olarak bağlanır; bu uyum düzgünlüğü yalnız tartan kişinin niyetine değil terazinin kendisine yükler. Fiziksel ölçümde şaşmayan doğrultu böylece işlemin parçası olur. Burada sıfat terazinin fiziksel hizasını niteler; yol çağrışımı Fâtiha 1:6’nın ayrı bağlamında belirir. Terazinin yapısı ve ölçü birimi belirtilmez.

Ölçü ile tartma ayrı yöntemler olarak ilerler; yan yana gelişleri tam teslimi yeniden sınanabilir kılar. {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} ölçülen miktarın tam karşılanmasını ister; {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} bu işi yinelenen her ölçme anına bağlar. Ardından {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} ayrı bir tartma denetimi getirir ve {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} bu ikinci işlemi bağımsız bir standarda bağlar. Ölçü sözcüğünün yiyeceği standart bir kapla belirleyen kullanımı, hacim ölçüsünü tanıdık bir alışveriş işlemine yaklaştırır; yiyecek örneği işlemi somutlaştırır, ayet belirli bir malı tayin etmez. Hacimce ölçülen miktar, tartılan ağırlık ve dış standart birlikte tam teslimi sınanabilir kılar; miktar ile ağırlık özel tahminden bağımsız karşılaştırılır. Mal, ölçü birimi ve alışverişin tarafları belirtilmez.

## İşlemin Vardığı Yer

İki ayrı emir tamamlandığında kapanış sözü okuru uygulamanın bütününe döndürür. {ar:ذَٰلِكَ, tr:dhālika, gloss:işte bu} her iki buyruğu birlikte gösterir ve ardından gelen iki yargının ortak konusu yapar. Uzak işaret biçimi, tamamlanan işe geriye dönüp dikkatle bakma etkisi verebilir; bu, biçimin sağladığı sınırlı vurgudur. Dhālika yeni bir talimat eklemek yerine iki işlemi birlikte değerlendirmeye açan geriye bakış noktası olarak iş görür.

Bu bütünün ilk niteliği olumlu bir değer yargısıdır. {ar:خَيْرٌ, tr:khayrun, gloss:iyi ve arzu edilir}, ölçüyü tamamlamayı ve doğru tartmayı iyi bir davranış olarak niteler; bu olumlu yargı belirli bir hile ya da kötü eylemle karşıtlık kurmaz. Aradaki {ar:وَ, tr:wa, gloss:ve}, {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} yargısını aynı uygulamaya ekler. İkinci değerlendirme ilkinin yerini almaz: khayr’ın olumlu değerini korurken karşılaştırmalı yeni bir nitelik getirir. Aḥsanu’nun “daha iyi” oluşu, sondaki {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} ile birlikte düşünüldüğünde değerlendirmeyi işlem doğruluğundan uygulamanın varacağı sonuca da taşır. Bu güzellik görünüşe değil davranışın değerine aittir; belirli bir ödül ya da karşılık vaat edilmez.

Sonuç sözcüğünün cümledeki görevi, değerlendirmeyi işlem anından varış noktasına taşır. {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} mansup mastar olarak {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} yargısının hangi yönden daha iyi olduğunu belirtir. Böylece doğruluk hem tartma anında hem işlemin varacağı yerde değerlendirilir. Sözcüğün buradaki baş anlamı sonuç veya akıbettir; bir işin dönüp vardığı yere ilişkin sınırlı yankı bu anlamı derinleştirir. Bu bağlamda yorumlama anlamını öne çıkaran bir söylem işareti yoktur ve belirli bir dünyevî ya da uhrevî netice adlandırılmaz.

Ortak fiziksel standart, sonuç yargısına değerleri kıyaslama yönünde başka bir çağrışım ekleyebilir. {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçme} ve {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} hacmi; {ar:زِنُوا, tr:zinū, gloss:tartın}, {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} ve {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} miktarları aynı fiziksel eksende karşılaştırmayı taşır. Düzlük sıfatının bağlı olduğu kelime ailesinde bedel biçmeye uzanan bir kullanımın bulunması, bu ortak ölçüyü alışveriş değerinin ağırlıkla kıyaslanması yönünde düşündürebilir. Yerel sıfat terazinin düz ve şaşmayan oluşunu anlatırken {ar:خَيْرٌ, tr:khayrun, gloss:iyi} ile {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} değer yargıları kıyaslama boyutunu ekler. Bu özel bağ, fiyat belirleyen veya gerçek bir pazarlık sahnesi kuran okuma değil, değer kıyasına açılan bir çağrışımdır; ayet fiyatı, parayı, tarafların ne verip aldığını ya da üçüncü bir denetçiyi adlandırmaz.

Değer kıyasından ayrı olarak, tartma ilişkisi denk ağırlıkta bir sikke benzetmesini düşündürebilir. {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} buyruğu ile {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} ve {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} standardı, miktarın fazla ya da eksik kalmamasını görünür kılar; “denk sikke” bu eşitliği eşit ağırlık imgesiyle somutlaştırır, ayette para birimi belirtilmez. Hacim ölçüsünün {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçme} ve {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} biçimlerinde yinelenmesi, {ar:خَيْرٌ, tr:khayrun, gloss:iyi} ile {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} yargılarının seçenekler arasında kıyaslama olarak da okunmasına alan açar. Seçeneklerin hangileri olduğu ya da bir seçim yapıldığı belirtilmez; bu ikinci çağrışım fiziksel tartma buyruğunun yanına eklenen bir imge olarak kalır.

Emirlerin sırası, ölçme anından değerlendirilen sonuca uzanan zamansal bir okuma getirir. {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} ile başlayan görev, {ar:إِذَا, tr:idhā, gloss:ne zaman} {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} koşulunda her ölçüm anında tamamlanacak bir edimdir. Doğruluğun sonradan düzeltmeden çok işlem anında gerekli oluşu, atfedilmiş bir buluşma benzetmesi doğurur; bu zamanlama gerçek bir randevu sahnesi kurmaz. {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} sıralı işi sürdürür ve {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} ile {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç} değerlendirmelerinden önce gelir; tartma böylece sonuca varmadan önceki aşama olur. Taʾwīlan’ın bağlı olduğu anlam alanındaki başlangıç yönü bu sırayla buluşunca âyete başlangıçtan sonuca uzanan bir yay imgesi ekleyebilir; sözcüğün kendisi başlangıç demek değildir. Sonuç ve geri varış yönü ilk işlemi vardığı yerden değerlendirmeyi düşündürür; standart da işlem boyunca sonuca dek ne ölçüde gerçekleştiği bakımından kıyaslanabilir. Bu okuma belirli bir netice vaat etmez ve azami çaba buyruğu kurmaz.

Zamansal okumaya ek olarak, yinelenen ölçme koşulu standardı işlem boyunca sürdürme sorumluluğu için başka bir benzetme sunar. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} terazinin sabit hizasını niteler; {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} ve {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} emirlerinin her {ar:إِذَا, tr:idhā, gloss:ne zaman} {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} tekrarında uygulanması bu hizayı işlem boyunca koruma düşüncesini açar. Ölçüyü tamamlama ile ayrı tartı standardı, dürüst niyetin yanında gereken miktarın eksiksiz teslimini öne çıkarır. Taʾwīlan için sağlanan işi üstlenip yürütme yönü, süreci sonuna dek gözetme benzetmesini besler; sonuç adı, alıcının kimliğini değil işi yürüten muhatapların vardığı yeri anlatır. Bu görev imgesi belirli bir gözetmeni, sahiplik ya da emanet kaydını, belirli bir alıcıyı veya sonraki alıcıyı, yeniden satışı kurmaz; fiyat ve sonraki devir de belirtilmez.

Sorumluluk benzetmesinden ayrı olarak, yinelenen tam ölçüler ile {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} standardının tutarlılığı, alışverişlerde güvenin zamanla yerleşebileceği bir birikme imgesi sunar. {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} sonuç anlamını korurken, sözcüğün bağlı olduğu alandaki koyulaşma ve pıhtılaşma yönü bu maddi yoğunlaşma imgesine katkı verir. Her tam ölçü, tekrarlanan işlemlerin ardından gelen birikmenin somut dayanağı olur. Bu bağlantı sıvıdan ya da toplumsal bir kurumdan söz etmez; güvenin kesinlikle birikeceğini de vaat etmez.

## Payın Ölçülebilirliği

Bu yerel işlem, başkasına ayrılmış hakların da adlandırıldığı bir dizi içinde ölçülebilir etik karşılık kazanır. Yakına, yoksula ve yolda kalana düşen pay (17:26) hakların kime ayrıldığını; elin bağlanmasıyla bütünüyle açılması (17:29) harcamanın iki ucunu gösterir. Bu bağlamda {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın}, {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hakkını} eksiltmeme sorumluluğuyla buluşur: ölçüyü tam yapmak başkasına düşen payı korumanın somut biçimidir. {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçü} hacmi, {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} ağırlığı sınayarak soyut hakka ölçülebilir miktar kazandırır. {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} buyruğu kapalı el ile bütünüyle açılmış el arasındaki aktarımda miktarı kıyaslamayı düşündürür; terazi sayısal eksiltmeyi görünür kılarken başkasının payına gösterilen özeni de sınar.

Payı gözetme bağı, yetim malına en iyi biçimde yaklaşma ve ahdi yerine getirme buyruklarıyla güçlenir (17:34). {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} değerlendirmesinin bu koruma bağlamında da geçmesi, terazide doğru miktarı gözetmeyi iyi korumanın elle tutulur karşılığı olarak düşündürür. Aynı ayette iki kez anılan {ar:ٱلْعَهْدَ, tr:al-ʿahda, gloss:üstlenilmiş ahdi}, {ar:أَوْفُوا, tr:awfū, gloss:eksiksiz yerine getirin} ile tamamlama yönünü paylaşır. Davranışların hoş karşılanmayan diye nitelenmesi de ölçülü alışverişi olumlu davranışlar dizisine yerleştirir (17:38); {ar:خَيْرٌ, tr:khayrun, gloss:iyi} yargısı hakkı teslim etmenin ahlaki değerini taşır. Komşu buyruklar bu etik bağı kurar; para birimi veya biçimsel kurum ayrıntısı vermez.

Bu ahlaki sorumluluğun bir sonraki yönü, yerine getirilişinin görünür olmasıdır. Kesin buyruk (17:23), başkasına ait hak (17:26) ve sorulacağı bildirilen ahit (17:34) yan yana geldiğinde, 17:35’teki {ar:أَوْفُوا, tr:awfū, gloss:eksiksiz yerine getirin} ile {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} yükümlülüğü ölçülebilir ifaya bağlar. Terazi teslim edilen miktarı görünür ve karşılaştırılabilir kılar; hak sahibine gereken pay böylece yalnız satıcının iyi niyetine bırakılmaz. Buyruktan hak sahibine, oradan sorulabilir ahde uzanan dizi tam teslimi öne çıkarır. Bu görünürlük fiş, kayıtlı sözleşme, dava ya da resmî çözüm yolu tarif etmez.

Kaynak baskısı altında terazi, yığma ile telaşla tükenme arasında ölçüyü koruyan bir karar referansı olarak okunabilir. Bağlanmış el ile bütünüyle açılan el (17:29) harcamanın iki ucunu; rızkın genişleyip daralması (17:30) ile yoksulluk korkusu (17:31) kararın verildiği baskıyı gösterir. Bu okuma, fiziksel tartma anlamındaki {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} buyruğunu korur; benzetmeye kattığı şey sükûnet değil, baskı altındaki değerlendirmeye ölçülü bir dayanak sağlamasıdır. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} terazi aktarımda korunacak denk bir sınır, açık elin imgesine karşı bir ölçü sunar. Rızkı daraltan ilahî takdir anlatımı (17:30) kendi anlamındadır; uygun miktar ve orta sınırın insan kararına uygulanması bağlamsal bir benzetmedir. Yoksulluk korkusu aktarım kararını çarpıtabilir (17:31), ancak bu sahne herkesin fiilen yoksul olduğunu söylemez. Bu bağlantı kaynak baskısı altında ölçüyü korumayla sınırlıdır; sikke ya da para birimi belirtilmez.

Terazinin sınır fikri, alışveriş dışındaki davranışlarla da her birinin kendi bağlamında ilişkilendirilebilir. Savurgan harcama (17:26), izin verilmiş karşılığı aşma (17:33) ve böbürlenerek yürüme (17:37), sırasıyla harcama, karşılık ve bedensel gösteriş alanlarında sınır meselesini açar. {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} ile {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve şaşmayan} her alan için ortak bir kalibrasyon benzetmesi sunabilir. Bu davranışlar terazide tartılan nesnelere dönüşmez ve tek bir hükümde birleşmez; özellikle böbürlenme ticari hileyle özdeşleşmez. Böbürlü yürüyüşe eşlik eden yeri delecekmiş gibi davranma ve dağlara erişememe görüntüsü (17:37), kişinin kendini ölçü sayma iddiasına sınır çizer.

Bu dış standardın koruyucu katkısı, yetim payının nasıl gözetileceğine ilişkin bir benzetme açmasıdır. Hakkı gözetmekle yükümlü veli (17:33) ve malı korunan yetim (17:34), her işlemi bizzat izleyemeyen kişi adına payın karşılaştırılabilir olduğu bir koruma bağlamı kurar. {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} gelen dış ölçü kişisel takibi ikame etmez, ona bağımsız bir kıyas sunarak yetimin payının kişisel gözetimden bağımsız karşılaştırılmasını sağlar. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve doğru} terazinin niteliğidir; gözetip korumaya uzanan anlam yönü burada benzetme olarak işler. {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} için sağlanan işi üstlenip yürütme yönü görev bakımından veli rolüne benzetilebilir. Veli ile terazinin sıfatı ayrı sözcükler ve ayrı köklerdir; bu işlev benzerliği sözlük özdeşliği kurmaz ve terazi veliyi ikame etmez. Koruma imgesinin bu bağlantısı biçimsel bir emanet düzeni kurmaz.

Tek tek işlemi gözeten bu örnek, tekrarlanabilir ortak ölçü fikrine açılır. Emirlerin hikmet çerçevesinde toplandığı bağlamda (17:39), {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} buyruğu, {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve doğru} standardı ve {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} dili her işlemde uygulanabilir ortak bir ölçütü düşündürür. Hikmet, bozulmayı önleyen koruyucu sınırın yanı sıra insanlar arasında adil karşılaştırma ve yargı fikrini de çağırabilir; bu okumada standart anlaşmazlıktan önce işleyen bir model olabilir. Taʾwīlan için sağlanan iyi yönetme ve düzene koyma yönü fiziksel araçla buluştuğunda, alışverişi ölçülü bir sonuca bağlama imgesine katkı verir. Kamusal düzen bağlantısı çıkarım olarak kalır: bu okuma yinelenebilir ölçünün ortak yaşama katkısını düşündürür, ancak 17:35 bir devlet aygıtı veya merkezî yargı mercii tanımlamaz.

Ortak ölçünün görünürlüğü, işlemin ileride sorulması fikrine bağlanınca hesap halkası belirir. Ahit sözü iki kez anılır, yerine getirilmesi istenir ve sonunda sorulacağı belirtilir (17:34); bilinmeyenin ardına düşmeme ve işlerin sorulması bu hesap bağlamını sürdürür (17:36). Bu iki ayet arasında duran 17:35, {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} ile tam teslimi, {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} ile dış ölçüyü, {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} ile varış noktasını bir araya getirerek miktarın sonradan izlenebilmesi imgesine katkı verir. Ardından gitmeyi anlatan {ar:تَقْفُ, tr:taqfu, gloss:ardına düşme} (17:36) yeniden kurma ve iz sürme yönünü güçlendirir. Ölçülü teslimin sonradan sorulabilir edim olması bağlamsal bir benzetmedir, awfū’nun sözlük anlamı değil; yakın ayetler fiş ya da ticari defter tarif etmez ve hesap dili yalnız alışverişe özgü değildir.

Aynı bilgi ve sorumluluk çevresi, terazinin fiziksel miktarın ötesinde kanıtı sınama modeli olarak okunmasına imkân verir. Bilinmeyenin ardına düşmeme buyruğu ile işitme, görme ve gönlün sorumluluğu birlikte anılır (17:36). Miktarı özel kanaatten bağımsız karşılaştıran {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} ve dışarıdan incelenebilir sonuç veren {ar:ٱلْقِسْطَاسِ, tr:al-qisṭāsi, gloss:terazi}, iddiaları dayanaklarıyla sınamak için bir model sunabilir. İzlenebilirliği anlatan {ar:تَقْفُ, tr:taqfu, gloss:ardına düşme} iddianın izini, destekli yargının eşiği olan {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} ise bu yargının dayanağını öne çıkarır. {ar:ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ, tr:as-samʿa wa-l-baṣara wa-l-fuʾāda, gloss:işitme, görme ve gönül} ayrı ayrı hesaba katılan algı ve yargı kanallarıdır: terazi işitme izleniminden bağımsız kıyas, gözlem için ortakça incelenebilir bir sonuç, iç kanaat için de kişinin tahminini sınayacağı dayanak sağlar. Böylece dış ölçü kanıtla yargılama için bir benzetme sunar; bu özel bağlantı 17:35’i genel bir bilgi kuramına dönüştürmez, 17:36’daki sorumluluğu da ticari hesaba indirgemez.

## Düzlük ve Yön

Kanıtı sınayan dış ölçü imgesi, 17:37’de insanın kendi duruşunu ölçü sayma arzusuyla karşılaşır. Böbürlü yürüyüş, yeri delecekmiş gibi davranma ve dağlara boyca erişememe (17:37), terazinin {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve doğru} niteliği karşısında kişisel yücelik iddiasını görünür kılar. Sözcük terazide fiziksel düzlüğü ve hizayı anlatırken komşu sahne, insanın duruşunu ve boyunu üstünlük ölçüsü yapma arzusunu açar. Ayağa kalkma ve dik durma imgesi bu karşılaşmada üstün duruşun ölçüsünü kendini yukarı koyan kişiden alıp kişisel olmayan standarda taşır. {ar:مَرَحًا, tr:maraḥan, gloss:böbürlenerek} yürüme ile terazi arasındaki ilişki sözlük bağı değil, bağlamsal karşıtlıktır: insan boyu sıfatın anlamına, terazi de yüksek bir nesneye dönüşmez. Düz standardın imgesi kişinin kendini ölçü saymasına sınır çizer.

Yol yönündeki çağrışım, fiziksel düzlüğün yanında ayrı bir bağlamda belirir. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve doğru}, Fâtiha’daki hidayet isteğinde de yolun niteliğidir: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭa l-mustaqīma, gloss:bizi dosdoğru yola ilet} (1:6). 17:35’te sıfat düzgün teraziyi, 1:6’da doğru yola yönelme isteğini niteler; bu temas, ortak ölçüyle adil alışverişin istenen yönelişin gündelik bir uygulaması gibi okunmasına imkân verir. Bu bağlantı teraziyi yolla özdeşleştirmez ve Fâtiha’nın bütün anlamını buraya taşımaz. 17:35’in ölçme buyruğu kendi başına da ayakta durur; yol yankısı ayrı yöneliş isteğinden gelir.

## Karşılıklı Ölçü

Karşılıklı alışverişte ölçünün neyi görünür kıldığı 83:2 ve 83:3’te belirginleşir: kişi kendisi için alırken tam ister (83:2), başkasına ölçüp tartarken eksiltir (83:3). Bu karşıtlık, 17:35’teki {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçü} ve {ar:أَوْفُوا, tr:awfū, gloss:tamamlayın} buyruklarının neden ortak bir kıyas noktası sağladığını gösterir; standart kapla hacim belirlemek iki tarafın payını karşılaştırır. {ar:وَزِنُوا, tr:wa-zinū, gloss:tartın} ile {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} kişinin kendisi için istediğiyle başkasına verdiği arasındaki farkı görünür kılar. Yusuf’un düş yorumunun gerçekleşmesi, bir işin vardığı yere dış örnek verir (12:100); emanetin sahibine verilmesi ve insanlar arasında adil hüküm, hakkın doğru kişiye ulaşması yönünü ekler (4:58). Bu ayrı katkılar birlikte tam ve karşılıklı teslimin zamanla güven kurabileceği bir alışveriş resmi oluşturabilir. Güven tekrarlanan ilişkinin olası sonucudur; tek bir doğru tartı bunu kendiliğinden garanti etmez ve ayet bir para düzeni belirlemez.

Ölçüyü eksiksiz tamamlama, alışveriş dışındaki tam karşılık düşüncesine de yankı verir. {ar:أَوْفُوا, tr:awfū, gloss:eksiksiz yerine getirin} doğrudan {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçüyü} nesne alırken, her canın yaptığının karşılığını tam alması (39:70) ve herkesin kazandığıyla karşılanıp haksızlığa uğramaması (40:17) daha geniş bir eksiksiz karşılık düzenini hatırlatır. Tam ölçü böylece karşılığın da eksilmeden teslim edildiği düzenin gündelik örneği gibi duyulur. Bu yankı 17:35’in alışveriş anlamını korur; dış hesap sahneleri belirli bir uhrevî sonucu tayin etmez.

Terazinin dış standardı, başka ayetlerle birlikte ölçülebilir haktan kamusal adil karşılaştırmaya uzanır. Ölçüde haddi aşmama çağrısı sınırı koyar (55:8); insanlar arasında adaleti ayakta tutmak için terazinin kullanılması bu sınırı kamusal haklara taşır (57:25). Emanetlerin sahiplerine verilmesi ve insanlar arasında adil hüküm de standardı hakların teslimiyle ilişkilendirir (4:58). {ar:بِٱلْقِسْطَاسِ, tr:bi-l-qisṭāsi, gloss:teraziyle} 17:35’te fiziksel tartı aracıdır ve ayet ölçü birimini belirtmez. Bu bağlantılar kamusal adalet fikrini genişletir; 17:35’in kendisi bir yargılama usulü tanımlamaz.

Terazideki denge, çıkar çatışması karşısında tarafsız değerlendirme için bir imge sunar. Adaleti kişinin kendisine, anne-babasına ve yakınlarına karşı, zengin-yoksul ayrımı gözetmeden ayakta tutma buyruğu (4:135) bu bağlamda sağlam ve ağırbaşlı yargıyı öne çıkarır. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīmi, gloss:düz ve sapmayan} fiziksel çizginin sapmamasını anlatır; ölçüde haddi aşmama (55:8) ile insanlar arası adalet (57:25) bu düzlüğü yargıda sapmama yönünde genişletir. İzin verilmiş karşılığın sınırını (17:33) ve kanıt sorumluluğunu (17:36) bu çizgiye bağlamak ihtiyatlı, atfedilmiş bir okumadır; bu bağlantılar sıfatın doğrudan anlamı değildir. Terazi tarafsız kıyas örneği verir, yargı merciinin yerini almaz.

Sonuç değerlendirmesi, hesap sorulabilir davranışla da buluşabilir. İşitme, görme ve gönlün sorumluluk taşıması (17:36), {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve akıbet} için düşünülen varış noktasını cevap verilebilir edimle ilişkilendirir. Bu temas, iyi ölçünün sonucunun yalnız miktar değil, bilgi ve kanıt karşısında da sorumluluk taşıyan davranışın bir parçası olarak okunmasına imkân verir. İki ayet arasındaki bu ihtiyatlı bağ doğrudan kelime eşleşmesine dayanmaz; algı kanalları terazinin kendisi değildir.

Bu sonuç düşüncesi, uyuşmazlığı ortak bir merciye döndürme bağlamında da yankılanır. İhtilafların Allah’a ve Elçi’ye götürülmesini buyuran 4:59, iyi olana ve daha iyi sonuca ilişkin benzer bir kapanışla biter (4:59). 17:35’teki {ar:خَيْرٌ, tr:khayrun, gloss:iyi}, {ar:أَحْسَنُ, tr:aḥsanu, gloss:daha iyi} ve {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç} işlemin vardığı yeri değerlendirir; 4:59’un uyuşmazlık bağlamı bu değerlendirmeyi alışveriş dışındaki haklı çözüm olanağına açar. Aynı dil böylece çekişmenin ortak adalet ölçüsüne döndürülmesinde yankılanır. Bu bağlantı 4:59’un kendi bağlamında kalır ve 17:35’e yeni bir yargılama usulü yüklemez.

</source_prose>
