# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:27**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.middle.claims.json`

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
- Refer to source paragraphs as `17:27 ¶N`.

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

`(17:27 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:27",
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
        "citation": "(17:27 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_27/17_27.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_27/17_27.middle.claims.json \
  --ayah-ref 17:27
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_27/17_27.prose.editorial.tr.md`

<source_prose>
## Hükmün İki Yargısı

17:27 iki yargıyı peş peşe kurar: {ar:إِنَّ, tr:inna, gloss:şüphesiz} {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı ölçüsüzce savuranlar} {ar:كَانُوٓا۟ إِخْوَٰنَ ٱلشَّيَٰطِينِ, tr:kānū ikhwāna ash-shayāṭīni, gloss:şeytanların kardeşleridir}; ardından {ar:وَ, tr:wa, gloss:ve} {ar:كَانَ ٱلشَّيْطَٰنُ, tr:kāna ash-shayṭānu, gloss:Şeytan da} {ar:لِرَبِّهِۦ, tr:li-rabbihi, gloss:kendi Rabbine karşı} {ar:كَفُورًا, tr:kafūran, gloss:çok nankördür} der. İlk yargı savurganları şeytanların kardeşleri diye sınıflandırır; ikincisi Şeytan'ı kendi Rabbine karşı yoğun nankörlükle niteler. Bu iki yargı, bütün harcamalar için bir miktar kuralı koymaz; savurganlar sınıfının aidiyetini ve Şeytan'ın Rabbine karşı niteliğini bildirir.

İlk yargıda {ar:إِنَّ, tr:inna, gloss:şüphesiz} hem belirli çoğul sınıfı hem ona bağlanan kardeşlik yüklemini vurgular. Bu vurgu, ölçüsüz savurma niteliği taşıyan kişiler hakkında belirgin bir tasnif kurar. Vurgu ilk cümlecikte tamamlanır; bu tasnifin önceki buyruklarla ilişkisini ise yakın bağlam açar.

{ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı ölçüsüzce savuranlar} II. kalıbın etken ortaç çoğuludur: tek bir savurma anından çok, bu davranışla nitelenen kişileri adlandırır. Belirli çoğul biçim davranışı sınıf kimliği olarak belirginleştirir; yargı bu niteliğe odaklanır, tek tek harcamalar için genel bir mahkûmiyet kurmaz. Aktarılmış bir biçim karşılaştırmasının yüzeyi verilmediği için aşırı üretim ya da denetimsiz artış yönü ihtimalli bir ek baskı olarak kalır; odakta görünen ortaç ve savurganlar sınıfı ana okuma olarak belirgindir.

{ar:كَانُوٓا۟, tr:kānū, gloss:çoğul kopula} biçiminin kişi eki savurganlar sınıfına döner; kardeşlik yüklemi fiilin kendisine değil, o fiille nitelenen insanlara bağlanır. İlk kopulanın mansup haberi {ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşler} biçimidir; onu izleyen belirli genitif {ar:ٱلشَّيَٰطِينِ, tr:ash-shayāṭīni, gloss:şeytanlar sınıfının} kardeşliğin yöneldiği sınıfı tamamlar. Sözün aile ve doğum bağına dayanan olağan anlamı korunur; cümledeki kardeşlik biyolojik soy iddiası değil, insanlar ile şeytanlar arasındaki adlandırılmış aidiyettir.

{ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşlik} sözünün kökeni için aktarılan çözümlemeler arasında görüş ayrılığı bulunur; bu belirsizlik tamlamadaki genitif ilişkiyi ve yüklem görevini değiştirmez, başka bir köken açıklamasını seçmeye de izin vermez. Genitif {ar:ٱلشَّيَٰطِينِ, tr:ash-shayāṭīni, gloss:şeytanlar sınıfının} biçimi bu cümlede standart yüzeydir. Karşılaştırıldığı söylenen mansup biçimin yüzeyi verilmediği için genitifin yerini almaz; böylece kardeşlik tamlaması kendi cümle yapısında kalır.

İkinci cümleciğin başındaki {ar:وَ, tr:wa, gloss:ve} yeni bir kopulalı yargıya geçer. İlkinde çoğul {ar:كَانُوٓا۟, tr:kānū, gloss:çoğul kopula} insan sınıfını nitelerken, burada tekil {ar:كَانَ, tr:kāna, gloss:tekil kopula} açık özne {ar:ٱلشَّيْطَٰنُ, tr:ash-shayṭānu, gloss:Şeytan}ı kendi niteliğine bağlar. Böylece çoğul {ar:ٱلشَّيَٰطِينِ, tr:ash-shayāṭīni, gloss:şeytanlar sınıfı}ndan onu açıklayan tekil bir arketipe geçilir; bu sayı değişimi sınıfı tek bir varlığa indirmez, savurganları da Şeytan'la özdeşleştirmez. İki kopula tarih verilmiş olaylar dizisi anlatmaktan çok öznelerini birer durum içinde gösterir. Bu aynalık, tekrarlanan savurmanın tekil Şeytan'ın yerleşik nankörlük profilini yansıtarak sınıfsal aidiyeti açıklayabileceği bir okumaya açılır. Bu ilişki yorumlayıcı düzeydedir: {ar:وَ, tr:wa, gloss:ve} açık bir neden bildirmez ve tek eylem insanın kimliğini kesinleştirmez; ikinci yargı yine de ilk aidiyetin hangi örüntüye benzediğini gösterir.

{ar:لِرَبِّهِۦ, tr:li-rabbihi, gloss:kendi Rabbine} öbeğindeki iyelik eki Şeytan'ı kendi Rabbine bağlar; lâm da son sıfatın yöneldiği ilişkiyi bildirir. {ar:رَبِّهِۦ, tr:rabbihi, gloss:kendi Rabbi} sözü sahiplik ve yönetme alanını, ayrıca besleyip gözetme ve geliştirme çağrışımını taşır. Rab adının mutlak kullanımı Allah'a özgüdür; başka sahiplik kullanımları belirli bir şeye bağlanır. Burada zamir, ilişkiyi doğrudan öznenin kendi Rabbine yöneltir.

Son yüklem {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} belirsiz mansup yoğun bir sıfattır; Şeytan'ı tek tek sayılmış eylemlerle değil, güçlü bir nankörlük niteliğiyle tanımlar. Kökünün örtme imgesi de bu niteliğe eşlik eder: kendi kaynağından gelen yararı tanımamak, o kaynağın değerini örtmek gibi duyulur. Hedefi ve iyelik ilişkisini {ar:لِرَبِّهِۦ, tr:li-rabbihi, gloss:kendi Rabbine} öbeği sağlar; böylece örtme imgesi Rabb'e yönelmiş nankörlüğün nasıl işlediğini belirginleştirir.

## Saçılma ve Bakım

Olağan anlamı malı savurup ziyan edenler olan {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı ölçüsüzce savuranlar} biçimi, sözlük alanındaki ekimlik tohumu toprağa saçarak ekme kullanımını da çağrıştırır. Bu çağrışım, ayrı {ar:رَبِّهِۦ, tr:rabbihi, gloss:kendi Rabbi} sözündeki besleyip yetiştirme ve tamamlamaya uzanan yönle, {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} kökündeki örtme imgesiyle buluşunca belirli bir tarım benzetmesi kurar: gelişebilecek potansiyel bakımını görmeden dağılır; tohumu büyümeyi korumak için örten toprak imgesi ise kaynak değerini gizleyen nankörlüğe döner. Bu temkinli imge bitmiş malın tüketilmesi okumasını, verim verebilecek şeyin bakım ve tamamlanmadan kopuşuna doğru genişletir. Ayetin olağan anlamları bu okumada yerinde kalır; ekim gerçek bir olay, {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} da çiftçi adı değildir. Böylece dört söz, dağılma ile büyümeyi besleyecek kaynak arasındaki kaybı görünür kılar.

Dağıtma alanında üç kayıtlı kullanım birbirinden ayrılır: ekimlik tohumu saçarak ekme, bir şeyi parçalara ayırıp dağıtma ve hayvan topluluğunun her yana yayılmasını anlatan ikilemeli biçim. Bunlar aynı yüzey ya da aynı kullanım değildir; ikilemeli biçim 17:27'deki {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı ölçüsüzce savuranlar} da değildir. Bu ayrım maddi dağılma çağrışımını açarken odaktaki etken ortaç biçimini ve savurganlar sınıfını belirgin tutar.

Ekim için saçılan tohumun yanına ayrı bir bitki görüntüsü gelir (18:45): yetişip kuruyan bitki {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:hashīman tadhruhu r-riyāḥ, gloss:rüzgârların savurduğu kuru ufantı} hâline gelir. Buradaki savurma fiili 17:27'deki {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı saçıp savuranlar} sözcüğü değildir; temas ortak kökten değil, rüzgârın kuru parçaları dağıttığı sahneden doğar. Tohum imgesi büyüyebilecek potansiyelin bakım görmeden yayılışını, 18:45'teki bitki ise önce büyüyüp sonra kuruyarak parçalanmayı gösterir. Bu ikinci sahne mali savrulmaya verimsizleşen bir maddi karşılık kazandırır; odak ayetin konusu yine harcama olarak kalır.

Şeytan adları için aktarılan bir başka açıklama, uzaklaşma yönünü açar. {ar:ٱلشَّيَٰطِينِ ٱلشَّيْطَٰنُ, tr:ash-shayāṭīni ash-shayṭānu, gloss:şeytanlar ve Şeytan} ayette başkaldıran varlıkları adlandırır; bu adların niyet edilen iyilikten uzaklaşmayla ilişkilendirilmesi ve ayrı bir biçimin birini tuttuğu yönden ayırmayı anlatması ihtimalli bir etimolojik yankıdır. Bu ilişki tek sözlük anlamı ya da fiziksel yön değildir. Tohumun gelişeceği kaynaktan kopuş imgesiyle buluştuğunda, söz konusu uzaklaşma ölçüsüz savurmayı tamamlanmaya götürecek kaynaktan ayrılma gibi duyurur.

## Kardeşlik ve Bağ

Yakın bağlamda anne babaya iyilik, incitici sözden kaçınma ve güzel hitap buyurulur (17:23); sonraki ayette merhamet duası, ebeveynlerin {ar:رَبَّيَانِى صَغِيرًا, tr:rabbayānī ṣaghīran, gloss:beni küçükken yetiştirdiler} diye anılmasıyla alınmış bakımı somutlaştırır (17:24). {ar:ٱلرَّحْمَةِ, tr:ar-raḥmah, gloss:merhamet} ile {ar:رَحِم, tr:raḥim, gloss:rahim} ortak kökleriyle merhamet ve akrabalık alanlarını birbirine yaklaştırır. Bu zeminde 17:27'deki {ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşler} sözü, doğumla alınmış aile bağının karşısında seçilmiş asi bir aidiyet gibi duyulabilir. Ebeveynlerin yetiştirmesiyle {ar:لِرَبِّهِۦ, tr:li-rabbihi, gloss:kendi Rabbine} arasındaki temas bağlamsaldır: sözler aynı kökten gelmez, ebeveynliği Rablikle bir tutmaz ve ayet belirli bir ihmal bildirmez. Karşıtlık, alınmış bakım ile seçilmiş bağlılık arasındadır.

Tövbe, namaz ve zekâtın ardından {ar:فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ, tr:fa-ikhwānukum fī d-dīn, gloss:dinde kardeşleriniz} denmesi kardeşliğin davranışla kurulan yanını gösterir (9:11): somut edimler inananlar arasında ilişki kurar. Sözlüklerde {ar:الإخوان, tr:al-ikhwān, gloss:kardeşler} biçiminin arkadaşlar, {ar:الإخوة, tr:al-ikhwa, gloss:doğumdan kardeşler} biçiminin doğum kardeşleri için daha sık kullanıldığı yönünde bir eğilim vardır; bu değişmez bir biçim kuralı değildir. Ailedeki baba, oğul, kardeş ve aşiret adları 58:22'de gerçek akrabalık olarak kalırken, Allah'a ve elçisine karşı durana bağlılık bu soy ilişkisiyle gerekçelendirilmez (58:22). Bu karşılaşma aile anlamını koruyup edimlerle kurulan yakınlığı da açar.

Bu din kardeşliğinin (9:11) yanına, aynı sözlük ailesindeki ayrı {ar:الآخِيَّة, tr:al-ākhiyya, gloss:hayvan bağlama halkası} adı maddi bir benzetme koyar. Hayvanın sabitlendiği halka, gözetilen hak ve yükümlülük bağını düşündürür; sözlükteki bağlama kullanımı hayvanı o halkaya tutturma sahnesiyle sınırlıdır. Bu maddi dal, {ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşler} için doğrudan “halka” ya da genel “bağlamak” anlamı değil, davranışla kurulan yakınlığı sürdürülmesi gereken bir ilişki gibi duyuran benzetmedir.

Ayrı bir sözlük imgesi olarak {ar:ٱلشَّيَٰطِينِ ٱلشَّيْطَٰنُ, tr:ash-shayāṭīni ash-shayṭānu, gloss:şeytanlar ve Şeytan} adları, kuyudan su çekmeye yarayan uzun ve sıkı bükülmüş ipi çağrıştırır. Bu imgeyle birlikte kaydedilen bağlama eylemi bir şeyi ya da hayvanı sıkıca tutturur. Halka sabit bir tutturma noktası verirken kuyu ipi aradaki mesafeyi geçen ayrı bir bağ görüntüsü sunar; iki sözlük katkısı aynı anlama indirgenmeden ilişki düşüncesini maddileştirir.

Tohumun saçılması ve bir şeyi parçalara ayırarak dağıtma dağılmış etkileri verir; {ar:الآخِيَّة, tr:al-ākhiyya, gloss:hayvan bağlama halkası} sabit noktayı, {ar:ٱلشَّيَٰطِينِ ٱلشَّيْطَٰنُ, tr:ash-shayāṭīni ash-shayṭānu, gloss:şeytanlar ve Şeytan} çevresindeki kuyu ipi ise iki taraf arasındaki bağı sağlar. Sıkıca tutturma eylemi dağınık parçaları ilişkiye bağlar; iki yargıdaki {ar:كَانُوٓا۟, tr:kānū, gloss:çoğul kopula} ile {ar:كَانَ, tr:kāna, gloss:tekil kopula} da kardeşlik ve nankörlük yüklemlerini ayrı öznelerde bir arada tutar. Bu bileşik imge gerçek bir tarım ya da bağlama sahnesi değil, farklı sözlük dallarının kurduğu ilişkisel bir ağdır; böylece mal savurma yalnız tekil bir kayıp değil, süren bir aidiyet ağı gibi duyulur.

Yusuf'un {ar:نَّزَغَ ٱلشَّيْطَٰنُ بَيْنِى وَبَيْنَ إِخْوَتِىٓ, tr:nazagha ash-shayṭānu baynī wa-bayna ikhwatī, gloss:Şeytan benimle kardeşlerimin arasını açtı} sözü bu bağın kırılganlığını somutlaştırır (12:100). Aynı sahnede Yusuf anne babasıyla yeniden kavuşurken insan kardeşliği sürer, Şeytan'ın araya giren ve ayıran rolü görünür olur. Bu anlatı şeytanî ilişkinin aile içindeki ayırıcı etkisini görünür kılar; odaktaki savurgan sınıfı Yusuf'un kardeşleri değildir.

Şeytan'ın insana {ar:ٱكْفُرْ, tr:ukfur, gloss:inkâr et} diye seslenip insan inkâr edince {ar:إِنِّى بَرِىٓءٌۭ مِّنكَ, tr:innī barīʾun minka, gloss:ben senden uzağım} diyerek ilişiğini kesmesi, 59:16'daki sıradır (59:16). Bu ayrı anlatıda davetin ardından gelen terk ediş, şeytanî yakınlığın kendi başına güvence olmadığını gösterir; böylece odaktaki kardeşlik hükmünün yanına bozulabilir bir yoldaşlık örneği eklenir.

## Harcamanın Yönü ve Sınırı

Kardeşlik ve saçılma imgeleri hemen önceki ayette (17:26) somut bir dağıtım düzeniyle karşılaşır. Orada {ar:وَءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ, tr:wa-āti dhā al-qurbā ḥaqqahu wa-al-miskīna wa-ibna as-sabīl, gloss:yakına hakkını, yoksula ve yolcuya ver} buyruğu yakına hakkını vermeyi, miskini ve yoldaki yolcuyu ise ayrı alıcılar olarak anmayı öne çıkarır; ayetin sonundaki {ar:وَلَا تُبَذِّرْ تَبْذِيرًا, tr:wa-lā tubadhdhir tabdhīran, gloss:saçıp savurma} yasağının hemen ardından 17:27'de savurganlar gelir. Belirli alıcıya yöneltilen aktarım ile hedefsiz saçılma böylece karşı karşıya durur. Bu bağlamda tohum saçma imgesi malın adı konan alıcılara ulaşmadan dağılmasını belirginleştirir; 17:26 bir tarla ya da hasat sahnesi kurmaz. {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:onun hakkı} sözü malı yalnız sahibinin dilediği gibi kullanacağı bir şey olmaktan çıkarır: hakları ve ihtiyaçları gözetmeyen savurma aile bağını, ihtiyaç sahibine erişebilecek kaynağı ve yolcuya verilecek somut desteği ıskalayabilir. Bu hak yönelimi her harcamayı başkasına hukuken borç sayan eksiksiz bir kural kurmaz; miktar da ölçütün parçası olarak kalır. Cömert miktardaki aktarım dahi adı konan alıcıları ve hakları gözden kaçırabilir; bu yüzden ölçü, malın ne kadar çıktığı kadar kime ve hangi hakka yöneldiğidir.

Bu harcama uyarısı iki el imgesi arasına yerleştirilir (17:29): {ar:يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:yadaka maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlanmış tutma} vermeyi hareketsiz bırakan tutmayı, {ar:وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ, tr:wa-lā tabsuṭhā kulla al-basṭi, gloss:elini bütünüyle açıp saçma} ise eldeki kaynağı sonuna dek salmayı gösterir. Bütünüyle açılan elin ardından gelen {ar:فَتَقْعُدَ مَلُومًا مَّحْسُورًا, tr:fa-taqʿuda malūman maḥsūran, gloss:kınanmış ve tükenmiş kalma} sonucu aşırılığın tükenişini görünür kılar; bu sonuç her harcamaya genellenmez. Rızkın birilerine genişletilip başkalarına daraltılması da eklenir (17:30): {ar:يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ, tr:yabsuṭu al-rizqa li-man yashāʾu wa-yaqdiru, gloss:dilediğine rızkı genişletir, dilediğine daraltır}. Dar rızık bütünüyle tutmayı, geniş rızık da tükenene dek harcamayı gerektirmez. Her hane için tek hesap formülü çıkmaz; savurma uyarısı, eldeki farklı imkânı gözetirken hem verememeyi hem de sonuna dek salmayı hesaba katar.

Harcamayı ölçülü denge diye niteleyen {ar:قَوَامًا, tr:qawāman, gloss:ölçülü bir denge} sözü, iki el ucu arasına ayrı bir ölçü koyar (25:67): burada övülen tutum ne harcamayı sınırsızca çoğaltır ne bütünüyle keser. 17:29'daki el imgeleriyle birlikte miktar kadar alıkoymayı da hesaba katar; savurganlık sözcüğünün bütün sözlük kapsamını tanımlamaz. Böylece 25:67 harcama değerlendirmesine, savurma ve kısma karşısında dengeli bir ölçü ekler.

Dağıtımın yönü başka bir sahnede belirginleşir (59:7): servet yakınlara, yetimlere, yoksullara ve yolda kalmışlara yöneltilir ki {ar:كَىْ لَا يَكُونَ دُولَةًۢ بَيْنَ ٱلْأَغْنِيَآءِ مِنكُمْ, tr:kay lā yakūna dūlatan bayna l-aghniyāʾi minkum, gloss:aranızdaki zenginler arasında dolaşıp durmasın diye}. Bu karşılaştırma savurganlığı toplam miktarın yanı sıra malın hangi yöne aktığıyla da düşündürür. 59:7'nin alıcıları bu bağlantıda 17:27'ye taşınacak sabit bir hukuk listesi oluşturmaz; 17:26'nın hemen önündeki yerel bağlam kendi hak sahiplerini adlandırır.

İnsanlara gösteriş için mal harcayanların yanında {ar:ٱلشَّيْطَٰنُ لَهُۥ قَرِينًا فَسَآءَ قَرِينًا, tr:ash-shayṭānu lahu qarīnan fa-sāʾa qarīnan, gloss:Şeytan onun yoldaşıdır, ne kötü yoldaş} denir (4:38). Gösteriş kaydı karşılaştırmanın kapsamını belirler; bu sınır içinde sahne, mal kullanımı ile şeytanî yoldaşlığı birlikte gösterip 17:27'deki aidiyet hükmünü aydınlatır.

## Emanet ve Sorumluluk

Malın nereye yöneldiği sorusunun ardından, onu kimin yararı için ve ne kadar süreyle gözetmek gerektiği belirginleşir. Mallar {ar:أَمْوَٰلَكُمُ ٱلَّتِى جَعَلَ ٱللَّهُ لَكُمْ قِيَامًا, tr:amwālakumu allatī jaʿala llāhu lakum qiyāman, gloss:Allah'ın sizin geçim dayanağınız yaptığı mallar} diye anılır; 4:5'te gözetim altındaki kişilere rızık ve giysi sağlanması istenir. Bu geçim dayanağı, odaktaki {ar:لِرَبِّهِۦ, tr:li-rabbihi, gloss:kendi Rabbine} ilişkisinin kaynak ve yönetim yönüyle buluşunca, savurma sürdürücü kaynağın sorumlu yönetiminden sapmış bir akış gibi duyulur. Bu bağlamsal bağlantı 17:27'deki savurganlara yetim malı yöneticiliği yüklemez; 4:5'in bakım sahnesi malın hayatı sürdürme işlevini aydınlatarak kaynak yönetimi temasını somutlaştırır.

Kaynağa bağlı bakım sorusu kıtlık korkusu karşısında da sınanır. 17:31'de çocukları {ar:خَشْيَةَ إِمْلَٰقٍ, tr:khashyata imlāqin, gloss:yoksulluk korkusuyla} öldürmek yasaklanır; ardından {ar:نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:naḥnu narzuquhum wa-iyyākum, gloss:onları da sizi de biz rızıklandırırız} denerek hem çocuklar hem ebeveynler rızık alan kişiler olarak gösterilir (17:31). Çocuklar bu sahnede yalnızca gider hesabı değildir: bağımlıyı kıtlık hesabıyla gözden çıkarma, bollukta savurmadan farklı yönde bakımın tersine çevrilmesi ihtimalini açar. Çocukların öldürülmesi savurma sözcüğünün anlamı değil, ayrı bir yasaktır; rızık vaadi ise bu karşılaştırmayı kaynağa güven ve bağımlıyı gözetme yönünde sınırlar. Böylece odaktaki nankörlük ilişkisi bolluktaki savurmadan başka bir kıtlık sınavında da duyulur.

Haksız yere öldürülenin velisine tanınan {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki}, {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqq, gloss:hak üzere} kullanılacak bir kapasite olarak çerçevelenir; hemen ardından {ar:فَلَا يُسْرِف فِى ٱلْقَتْلِ, tr:fa-lā yusrif fī al-qatli, gloss:öldürmede aşırıya gitmesin} diye sınır konur (17:33). Bu ayrı karşılık sahnesi, imkân ya da yetkinin sınırsız kullanım izni vermediği noktasında sınırlı bir analojiyle mal savurma uyarısını aydınlatır. İki ayet ayrı fiil ve hükümleri korur: biri öldürme karşılığındaki aşırılığı, öteki malı savurmayı ele alır. Bu yetki benzetmesi, kaynağı kullanma kapasitesinin de hakla düzenlenebileceğini düşündürür.

Bu iki yakın buyruk kaynak kullanımını başkasının geleceğine karşı sorumlulukla somutlaştırır (17:34, 17:35). {ar:مَالَ ٱلْيَتِيمِ, tr:māla al-yatīmi, gloss:yetimin malı} için konan emir, ona ancak en iyi biçimde yaklaşmayı ve bu gözetimi sahibi olgunluğa erişinceye dek sürdürmeyi ister. Mal üzerindeki fiilî denetim, onu sınırsız kullanma hakkı vermez. {ar:أَوْفُوا۟ بِٱلْعَهْدِ, tr:awfū bi-l-ʿahdi, gloss:ahdi yerine getirin} yükümlülüğü zamana yayarken, {ar:أَوْفُوا ٱلْكَيْلَ, tr:awfū al-kayla, gloss:ölçüyü tam yapın} ve {ar:وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:wa-zinū bi-l-qisṭāsi al-mustaqīmi, gloss:doğru teraziyle tartın} kişisel tercihin dışındaki ölçüyü belirler. Bu ayrı buyruklar yan yana geldiğinde, Rabb adının yetiştirip tamamlamaya uzanan çağrışımı bağımlının geleceğini koruyan bir gözetim örneğiyle buluşur. Bağlamdan doğan emanet okuması her malın hukuken emanet olduğu iddiasına dönüşmeden, kırılgan hakkın sürekliliğini görünür kılar.

## Sözün Dolaşımı

Savurma alanının bir başka kolu malın değil, saklanması gereken sözün yayılmasını düşündürür. Sözlüklerde {ar:بذور, tr:badhūr, gloss:sırrını tutamayan kişi} kişi için, {ar:قوم بذر, tr:qawm badhar, gloss:söz saklamayan topluluk} ise topluluk için kaydedilir; 17:27'deki {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:malı saçıp savuranlar} doğrudan “sır taşıyamayanlar” diye çevrilmez. Anne babaya incitici söz söylememe ve güzel hitap buyruğu (17:23), bilmediğinin ardına düşmeme emriyle (17:36) birlikte bu söz koluna sınır çizer: {ar:فَلَا تَقُل لَّهُمَآ أُفٍّ وَقُل لَّهُمَا قَوْلًا كَرِيمًا, tr:fa-lā taqul lahumā uffin wa-qul lahumā qawlan karīman, gloss:ikisine bile of deme, güzel söz söyle} ve {ar:وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ, tr:wa-lā taqfu mā laysa laka bihi ʿilmun, gloss:bilmediğin şeyin ardına düşme}. Aynı ayette {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme} dahil yetilerin {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:hesap sorulacak} oluşu, içeriğin neye dayandığını ve nasıl aktarıldığını hesap verilebilir kılar. Böylece malî akışa eklenen bilgi akışı da bilinene, işitilene ve söze ilişkin sorumluluk içinde duyulur.

Bu akışın iki ayrı sahnesi vardır. Yusuf'a rüyasını kardeşlerine anlatmama öğüdü verilir (12:5); onların ona karşı tuzak kurabileceği ihtimali içeriği koruma gereğini doğurur, yaşanmış bir ifşa anlatılmaz. Buna karşılık insan ve cin şeytanlarının birbirlerine {ar:يُوحِى بَعْضُهُمْ إِلَىٰ بَعْضٍۢ زُخْرُفَ ٱلْقَوْلِ غُرُورًا, tr:yūḥī baʿḍuhum ilā baʿḍin zukhrufa l-qawli ghurūran, gloss:aldatmak için birbirlerine yaldızlı söz aktarırlar} diye süslü, aldatıcı söz aktarması 6:112'de tasvir edilir (6:112). İlki korunması gereken içeriğin dışarı çıkma riskini, ikincisi taraflar arasında gerçekten dolaşan aldatıcı sözü gösterir; böylece saçılma imgesi şeytanî bir iletişim ağına da uzanır.

Bu söz imgesi, ayetin mali anlamını değiştirmeden güven ilişkisini tersine çevirir. Önceki {ar:الآخِيَّة, tr:al-ākhiyya, gloss:hayvan bağlama halkası} benzetmesinin sabitlediği hak ve karşılıklı yükümlülük bağı, {ar:إِخْوَٰنَ, tr:ikhwāna, gloss:kardeşlik} ile de duyulur; {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} ise kabul edilmesi gereken nimetin değerini örten tutumu taşır. Sır yayma kolu gözetilen içeriği dışarı saçar. {ar:ٱلشَّيَٰطِينِ, tr:ash-shayāṭīni, gloss:şeytanlar sınıfı} adının yön saptırma çağrışımı bu katkıları tersine dönmüş bir emanet düzeninde buluşturur: korunması gereken söz yayılırken tanınması gereken kaynak örtülür. Bu, ayrı sözlük kullanımları ve bağlamlardan doğan ihtiyatlı bir yan imgedir: gizli haber ifşası bu bağlantının kapsamındadır, ayetin açık hükmü ise mali savurganlık ve nankörlüktür. Böylece yan imge, korunmuş sözün yayılmasıyla nimetin değerinin örtülmesini aynı güven ihlalinde karşılaştırır.

## Nimet ve Hesap

Kaynağa verilen cevabın başka bir görünümü açılır (14:34): sayılamayacak nimetlerin ardından insan {ar:لَظَلُومٌۭ كَفَّارٌۭ, tr:la-ẓalūmun kaffār, gloss:çok haksız ve çok nankör} diye nitelenir. Buradaki yüzey biçimi 17:27'deki {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} ile aynı değildir; iki ifade arasındaki temas biçim özdeşliğine değil, nimet karşısında verilen cevaba dayanır. Bu karşılaştırmada insan odaktaki Şeytan'la özdeşleştirilmez; 17:27'de hangi nimetin kastedildiği de belirlenmez. Kuruyup dağılmış bitki (18:45), büyüyen şeyin kuru ufantıya dönüşmesini; malın zenginler arasında kapanmayıp alıcılara yönelmesi (59:7), dağıtımın nereye gittiğini gösterir. 14:34 ise nimeti alanın kaynağa nasıl karşılık verdiğini gösterir. Bu farklı sahneler bir araya geldiğinde savurma yalnız verim ve yön meselesi olmaktan çıkar, verilen nimeti tanıma ya da yadsıma ilişkisini de içerir. Rabb'in besleyip büyüten çağrışımını 14:34'teki nimetler etkinleştirir; bu yankı odaktaki kaynak ilişkisini derinleştirir, gerçek bir besleme sahnesi ya da tek zorunlu sözlük karşılığı kurmaz.

Sûrenin kapanışında önceki buyruklar {ar:كُلُّ ذَٰلِكَ, tr:kullu dhālika, gloss:bütün bunlar} diye toplanır (17:38); {ar:سَيِّئُهُۥ, tr:sayyiʾuhu, gloss:kötü olanı} Rabbin hoş görmediği şey olarak nitelenir, {ar:ٱلْحِكْمَةِ, tr:al-ḥikmati, gloss:hikmet} ise buyrukları daha geniş bir düzene yerleştirir. Ardından Allah'ın yanında başka bir ilah edinmeme buyruğu ve {ar:مَدْحُورًا, tr:madhūran, gloss:kovulmuş} diye betimlenen son gelir (17:39). Bu kapanış, günlük kaynak kullanımıyla odaktaki kardeşlik ve Rabb'e nankörlük bağını daha geniş bir bağlılık düzeninde duyurur; malî uyarı ile tevhid buyruğu bu düzende kendi ayrı konularını korur.

Fâtiha'daki dışsal hamd ifadesi (1:2), {ar:ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:al-ḥamdu lillāhi rabbi al-ʿālamīna, gloss:hamd âlemlerin Rabbi Allah'a mahsustur} ile odaktaki {ar:لِرَبِّهِۦ كَفُورًا, tr:li-rabbihi kafūran, gloss:kendi Rabbine karşı çok nankör} ilişkisinin karşısına aynı Rabb'e yönelen övgüyü koyar. Yakın bağlamdaki ibadet ve merhamet dili yerinde kalır (17:23, 17:24); bu kıyas kasıtlı alıntı ya da gönderme değil, nankörlüğe karşılık gelen olumlu övgüyü gösterir.

Fâtiha'nın hesap günü ifadesi (1:4), {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi al-dīni, gloss:hesap gününün sahibi} kaynak kullanımı için geleceğe uzanan bir hesap ufku açar: yakın çevredeki hak, ahit ve ölçü yükümlülüklerinin ötesinde, malın nereye yöneldiği ileride de cevaplanabilir görünür. Bu zaman ufku dışarıdan gelir; 17:27 hesap gününü anmaz, 17:34 ve 17:35'teki yakın buyrukların yerine geçmez ve bütün sureyi tek başına çerçevelemez. Böylece Fâtiha karşılaştırması, odağın kendi sınırlarını koruyarak kaynak kullanımını daha sonraki hesapla ilişkilendirir.

</source_prose>
