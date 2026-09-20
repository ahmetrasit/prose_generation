# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:15**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.middle.claims.json`

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
- Refer to source paragraphs as `17:15 ¶N`.

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

`(17:15 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:15",
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
        "citation": "(17:15 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_15/17_15.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_15/17_15.middle.claims.json \
  --ayah-ref 17:15
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_15/17_15.prose.editorial.tr.md`

<source_prose>
## Yönelişin Kişisel Sonucu

17:15, {ar:مَّنِ, tr:man, gloss:kim} ile belirli bir kişiyi değil, doğru yola yönelme koşuluna giren herkesi açar; {ar:وَمَن, tr:wa-man, gloss:ve kim} aynı açıklığı sapma ihtimaline taşır. Aradaki {ar:وَ, tr:wa, gloss:ve} bu iki yönü yan yana getirir, birini ötekinin nedeni ya da sonucu yapmaz. Her koşulun ardından gelen {ar:فَ, tr:fa, gloss:öyleyse} kendi cevabını başlatır; böylece iki cümle biçimce paralel, fakat ayrı ihtimaller olarak ilerler. Sonuçlardaki {ar:إِنَّمَا, tr:innamā, gloss:ancak} yararı ve zararı koşulu yaşayan kişiye bağlar: {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendisi için} yararı özneye yöneltirken {ar:عَلَيْهَا, tr:ʿalayhā, gloss:kendi aleyhine} zararı aynı kişiye yükler. Buradaki dişil zamir, Arapçada dişil biçimli olan nefs sözüne döner; iki sonuç aynı öznenin çevresinde kurulur. Yarar ve zararın özneye dönmesi, kişiler arası etkilerin de sürebileceği bir çerçevede her kişinin kendi payını belirginleştirir.

Koşuldaki {ar:ٱهْتَدَىٰ, tr:ihtadā, gloss:doğru yola yöneldi} tamamlanmış görünümlü VIII. bâb biçimiyle kişinin doğru yönü benimseyip ona katılmasını anlatır; sonuçtaki {ar:يَهْتَدِى, tr:yahtadī, gloss:yol bulur} aynı fiil ailesini geniş zamanda sürdürür. Böylece yöneliş tek bir giriş anında kalmaz, kişinin yararına devam eden bir yol bulma hâline dönüşür. Hidayet ailesinin doğru yönü ya da gerçeği gösterme, açıklama ve tanıtma kullanımları da bu gidişe eşlik eder: gösterilen doğrultu, onu benimseyerek izleyen özneyle buluşur. Ayet yönün ilk kaynağını açık bırakırken, yararın kime ulaştığını belirginleştirir.

Yararlanıcıyı gösteren {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendisi için}, yönelişin getirisini kişinin bütününe ulaşan bir kazanç olarak kurar. Yakınlık duyulan birine incelikle sunulan armağan çağrışımı bu kazancın değerini duyurur: doğru yönelişin getirisi yine kişiye ulaşır. Nefs burada kişinin bütünü ve bizzat kendisidir; beden, nefes ya da metafizik ruhla ayrı bir karşıtlık kurmaz. Armağan benzetmesi bu bağlantıda yararın kişiye dönüşünü anlatır; somut bir armağanı, vereni ya da sevgi sahnesini kurmaz. Böylece kişisel kazanç, yönün dışarıdan gösterilmesi ve başkalarının desteğiyle birlikte kalır.

Karşı koşuldaki {ar:ضَلَّ, tr:ḍalla, gloss:saptı} Form I’de tamamlanmış ve geçişsiz bir ahlaki sapmayı, sonuçtaki {ar:يَضِلُّ, tr:yaḍillu, gloss:sapmaya devam eder} ise süren karşılığını bildirir. {ar:فَ, tr:fa, gloss:öyleyse} sonucu bu koşula bağlar; {ar:إِنَّمَا, tr:innamā, gloss:ancak} ve {ar:عَلَيْهَا, tr:ʿalayhā, gloss:kendi aleyhine} devam eden zararı aynı özneye döndürür. Fiiller öznenin kendi yönünden ayrılmasını söyler, başkasını saptıran ettirgen bir eylemi değil. Hidayetle kurulan yön karşıtlığı, sapmayı doğru yolu, amacı ya da uygun doğrultuyu yitirme duyumuna açar.

Form I’deki {ar:ضَلَّ, tr:ḍalla, gloss:saptı} ailesinin sahibinden kopmuş, yeri bilinmeyen şey kullanımı kaybı somutlaştırır; kimi kullanımlarındaki karşılığı aranmayan kan da bu imgeye karşılıksız kalma boyutunu ekler. {ar:ٱهْتَدَىٰ, tr:ihtadā, gloss:doğru yola yöneldi} ile belirginleşen doğru yön ve {ar:عَلَيْهَا, tr:ʿalayhā, gloss:kendi aleyhine} ile kişiye dönen zarar birleşince bu sözlük kolları, kişinin kendi yolunu ve kazancını yitirmesi şeklinde nitelikli bir benzetme kurar. Bu bağlantıda ayetin olayı kayıp eşya ya da karşılıksız bırakılmış kan değil, bu iki kullanımın yön kaybına sağladığı çağrışımdır.

Ḍ-l-l ailesinin bir başka kullanımı kişinin evini, ibadet yerini ya da sabit bir konumu bulamaması ve oraya varamamasıdır; bu, sapma imgesine varılacak yer boyutunu ekler. {ar:ضَلَّ, tr:ḍalla, gloss:saptı} ile {ar:ٱهْتَدَىٰ, tr:ihtadā, gloss:doğru yola yöneldi} arasındaki yön karşıtlığı ve {ar:عَلَيْهَا, tr:ʿalayhā, gloss:kendi aleyhine} ile kişiye dönen zarar, bu yerde bulamama imgesini ayetin kendi yönelişine bağlar. Katkısı, doğru yoldan ayrılmayı varılacak yeri bulamama duyumuyla somutlaştırmasıdır; bu bağlantı gerçek bir arama ya da yolculuk değil, rota benzetmesidir.

Kişiye dönen yarar, dışarıdan gösterilen rehberliğin kişinin kendi sonucuna dönüşmesiyle birlikte okunabilir. 17:1’deki gece yolculuğu sırasında ayetlerin gösterilmesi görünür işaretlerle izlenen bir yönü sahneye getirir (17:1); 17:2’de Musa’ya verilen kitap İsrailoğulları için rehber kılınır (17:2). Bu sahnelerin katkısı, 17:15’teki kişisel yönelişten önce görünür işaret ve verilmiş rehberlik sunmalarıdır; 17:1’deki yolculuğun benzetme olarak da duyulabilmesi bağı bağlamsal tutar (17:1, 17:2). Fâtiha 1:7 dosdoğru yolun karşısındaki sapanları ortak bir yol isteği içinde anar (1:7); 34:50 rehberliği Rabbin vahyine, sapmayı kişinin kendi aleyhine bağlar (34:50); 16:89 ise kitabı açıklama ve hidayetle, toplulukları tanıklıkla ilişkilendirir (16:89). Bu temaslarda dışarıdan gösterilen yön ile kişinin onu benimsemesi birlikte durur; 17:15 yararlanıcıyı belirler, rehberliğin kaynağını değil (17:1, 17:2, 1:7, 34:50, 16:89).

17:9 Kur’an’ı {ar:يَهْدِي, tr:yahdī, gloss:yol gösterir} diye niteler ve {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün olana} yöneltir; böylece seçimin önüne dışarıdan bir doğrultu koyar (17:9). 17:11’de insanın {ar:يَدْعُ بِالشَّرِّ دُعَاءَهُ بِالْخَيْرِ, tr:yadʿu bi-sharri duʿāʾahu bi-l-khayr, gloss:kötülüğü iyilik ister gibi istemesi} ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} oluşu, arzu edilenle gerçekten yararlı olanın ayrışabileceğini gösterir (17:11). Bu tek örnek, aceleyle dilekte bulunurken kişinin yararını ayırt etmesinin nasıl zorlaşabileceğini düşündürür; kapsamı yalnız aceleci isteklere ilişkin de olabilir, dolayısıyla her seçenin yararını yanlış tanıdığına dair genel bir kural kurmaz (17:11). 17:12’de geceyle gündüzün işaret kılınması, gündüzün görünür hâle getirilmesi ve {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:ayrıntısıyla açıkladık} sözü seçenin önündeki ayrımları görünür kılar (17:12). Bu ayetler, dışarıdan sunulan doğrultu ile öznenin kendi arzusunu tartma ihtiyacını birlikte öne çıkarır; böylece yönelişin kişisel sonucu dış ölçülerin varlığını silmez (17:9, 17:11, 17:12).

## Yükün Sahibi ve Desteğin Sınırı

Kişisel sonucun {ar:عَلَيْهَا, tr:ʿalayhā, gloss:kendi aleyhine} sözüyle bitmesinin ardından gelen {ar:وَ, tr:wa, gloss:ve} iki koşullu sonuçtan ayrı, genel bir ilkeye geçirir. Yeni cümle üçüncü bir koşulun cevabı değildir. {ar:وَلَا, tr:wa-lā, gloss:ve ... etmez} ile olumsuzlanan {ar:تَزِرُ, tr:taziru, gloss:taşır} bir yasak buyruğu değil, yükün taşınması hakkında olumsuz bir bildirim kurar: kimse başkasının yükünü üstlenmez. Yardım, tanıklık ve bakım yükün sahipliğini devralmadan mümkün kalır; cümlenin sınırı bu ilişkilerin biçimlerini değil, başka birinin yükünü üstlenmeyi belirler.

Bu bildirimin dilbilgisi, taşıma ilişkisini üç rolde görünür kılar: {ar:تَزِرُ, tr:taziru, gloss:taşır} eylemi, {ar:وَازِرَةٌۭ, tr:wāziratun, gloss:yük taşıyan} taşıyanı, {ar:وِزْرَ, tr:wizra, gloss:yük} taşınanı adlandırır. Olumsuzlama altındaki belirsiz dişil etken ortaç, özel bir sınıfı değil genel olarak yük taşıyanı bildirir; {ar:أُخْرَىٰ, tr:ukhrā, gloss:başkasının} ise sahiplik ilişkisi içinde ayrı bir kişiyi gösterir. Bu taşıma ve iyelik bağı, ukhrā’yı başka bir yük sahibine sabitler; “sonraki” zaman, son kişi ya da ahiret okuması bu cümlenin bağlantısı değildir. Eylem, taşıyan ve yükün aynı kelime ailesinden biçimlerle kurulması, başkasına ait yükün devrini kapatan bir zincir oluşturur; kişi başka birinin yükümlülüğüyle karşılaşsa da onun sahibi hâline gelmez.

Taşımanın olağan somut yüzü, bedene ağırlık ve güçlük veren fiziksel yüktür. Eylem, taşıyan ve nesnenin aynı kökten kurulması bu maddi ağırlığı ahlaki sorumluluğa taşır; sonuç, kişinin üzerinde kalan bedensel bir güçlük gibi duyulur. Bu bağlantı yük imgesini sorumluluğu anlatmak için kullanır; ayet gerçek eşya taşımayı ya da her yükü suç sayan eksiksiz bir yargı kuramını anlatmaz. 35:18’de ağır yükün yakın akrabaya bile geçmemesi, ayrı sahibin sınırını aile bağına kadar uzatır (35:18).

Taşıyıcıyla yükün ayrı kişilere bağlanması, surenin sonraki kişisel kayıt sahnesinde başka bir imgeyle sürer. 17:13’te kişinin kendi payı ve izi boynuna bağlanır; ardından karşısına açılmış bir kitap çıkarılır (17:13). 17:14’te kişiye kendi kitabını okuması söylenir ve kendi nefsi o gün kendisine hesap görücü olmaya yeter (17:14). Bağlanma, açılma ve okuma eylemleri kayıtla karşılaşan kişi ile hesabı taşıyan kişinin aynılığını görünür kılar (17:13, 17:14). 17:14’teki {ar:كَفَىٰ, tr:kafā, gloss:yeterli oldu} sözü, kişinin kendi hesabına tanık oluşunu güçlendiren bağlamsal bir yankı sunar; bu temas 17:15’teki yük sözcüğünün anlamını değiştirmez (17:14). Böylece sahne hesap verilebilirliği görünür kılarken, kayıtların teknik işleyişini açık bırakır (17:13, 17:14).

Bundan ayrı ve keşifsel, zayıf bir kök ayrımıyla anılan {ar:يزور كلاما, tr:yazūru kalāman, gloss:sözü önceden düzenlemek} kullanımı sözün söylenmeden önce hazırlanması, düzeltilmesi ve biçimlendirilmesi imgesini taşır. Bu kullanım, 17:13’te kişiye bağlanıp açılan kayıt ve 17:14’te sahibine okutulan kitapla yan yana geldiğinde, kişinin hesabının başka bir anlatımla değiştirilemeyeceği düşüncesine benzetilebilir (17:13, 17:14). Bu temas zayıf ve keşifseldir: w-z-r yükünün sözlük anlamı değildir, belirli bir aldatma eylemi ya da teknik denetim iddiası da taşımaz. Benzetmenin katkısı, hesabın sahibini onu okuyacak kişiyle aynı yerde tutmasıdır (17:13, 17:14).

Yükü devretmeme ilkesi desteği ortadan kaldırmaz. Aynı kökün ayrı bir kullanımı olan {ar:وَزِير, tr:wazīr, gloss:başyardımcı}, güvenilir bir yöneticinin ağır işini paylaşan ve görüşüyle destek olan yardımcının adıdır; odaktaki {ar:وَازِرَةٌۭ, tr:wāziratun, gloss:yük taşıyan} ise genel taşıyıcıyı bildiren dişil etken ortaçtır. Bu kelimelerin yakınlığı, iş paylaşımı ve danışmanlık desteğini başkasının sorumluluğunu üstlenmekten ayırır; 17:15’teki biçim bir makamı adlandırmaz. 17:3’te Nuh’la birlikte taşınan topluluk bedenlerin fiziksel taşınışını getirir (17:3); bu kolektif sahne kişisel yük ya da önceden uyarı hakkında doğrudan bir paralel kurmaz. 17:6’da mal ve çocuklarla verilen destek, yardımın maddi imkân boyutunu ekler (17:6). 17:7 ise iyilik ve kötülüğün yapan kişiye dönmesini daha doğrudan gösterir (17:7). Bu örnekler eksiksiz bir yardım sınıflandırması değil, fiziksel taşıma, maddi destek ve kişisel ahlaki sonucu ayrı düzlemlerde tutan üç katkıdır. Yan yana gelişleri, destek mümkünken eylemin sonucunun da failine ait kalabildiğini belirginleştirir (17:3, 17:6, 17:7).

Fâtiha’nın 1:5’teki çoğul yardım isteği, 1:6’daki dosdoğru yola iletilme duasıyla sürer; 1:7’de yolun karşısındaki sapanlar anılır (1:5, 1:6, 1:7). Bu dua, {ar:إِيَّاكَ نَسْتَعِينُ, tr:iyyāka nastaʿīnu, gloss:yalnız senden yardım dileriz} sözüyle ortak yardım isteğini, {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} sözüyle ortak yönelişi dile getirir; {ar:وَلَا ٱلضَّآلِّينَ, tr:wa-lā aḍ-ḍāllīn, gloss:sapanlar değil} karşıt yolu görünür tutar. {ar:وَزِير, tr:wazīr, gloss:başyardımcı} biçiminin destek çağrışımı bu ortak yardım isteğiyle buluşur; bu yakınlık yardım talebiyle sınırlıdır, dua bir yönetici yardımcısından söz etmez (1:5, 1:6). Fâtiha’nın çoğul duası 17:15’in koşullarını çoğul bir duaya dönüştürmez: ortak yardım ve yön isteme mümkünken sonuç her özneye ait kalır; kişisel sorumluluk tek başına yeterli olmayı gerektirmez (1:5, 1:6, 1:7).

Yük anlamından ayrı olarak {ar:الوزر الملجأ, tr:al-wazr al-maljaʾ, gloss:sığınılan yer ve korunma dayanağı} kullanımı güvenli bir sığınak imgesi taşır. Bu sözlük kolu 17:2’de başka bir vekil edinmeme uyarısıyla karşılaşır (17:2); 17:22’de başka bir ilah edinme yasağı, kişinin sonunda yerilmiş ve yardımsız kalmış hâlde oturmasıyla sonuçlanır (17:22). Bu temas, yükü devredilemez hesap karşısında ikame bir sığınak arayışını düşündüren sınırlı bir bağlamsal benzetmedir. 17:2 ve 17:22 güven ya da ibadet ilişkilerini anlatır; buradaki yankı w-z-r yük sözcüğüne sığınak anlamı vermez, insanlardan yardım almayı da dışlamaz (17:2, 17:22). Böylece sığınak kolu hesabın vekile bırakılamayışını aydınlatırken, insani destek kendi yerinde kalır (17:2, 17:22).

Kişisel yük sınırı, insanlar arasındaki etkinin sonuçsuz kaldığı anlamına gelmez. 17:15’teki {ar:ضَلَّ, tr:ḍalla, gloss:saptı} ve {ar:يَضِلُّ, tr:yaḍillu, gloss:sapmaya devam eder} Form I’de öznenin kendi sapışını anlatır; 16:25 ise bilgisizce başkalarını saptıranları ayrı bir eylem olarak gösterir (16:25). Orada yanıltanlar kendi yüklerini bütünüyle taşır ve saptırdıkları kişilerin yüklerinden de pay alır (16:25). Bu karşılaştırma odaktaki geçişsiz Form I fiilini ettirgenleştirmez ve her toplumsal etkiyi aynı sonuçla ölçmez (16:25, 17:15); katkısı, izleyenin aslî yükü yerinde kalırken yanıltanın kendi saptırma eyleminden ek sorumluluk almasını göstermesidir (16:25).

## Elçi ve Bildirim Eşiği

İnsanların yükü hakkındaki ilkenin ardından gelen bir başka {ar:وَ, tr:wa, gloss:ve} yeni bir usule geçirir: son cümle önceki yük hükmünün sonucu değil, elçi gönderilene kadarki cezalandırma eşiğidir. “Bir elçi gönderene kadar azap eden olmadık” bildirimi, {ar:وَمَا, tr:wa-mā, gloss:ve ... değil} ile {ar:كُنَّا, tr:kunnā, gloss:olmadık} üzerinden tek bir eylemi değil, cezalandıran olma hâlini olumsuzlar. {ar:مُعَذِّبِينَ, tr:muʿadhdhibīna, gloss:azap edenler} ağır acı veren ve cezayı uygulayan etkin özneyi adlandıran II. bâb çoğul etken ortaçtır. {ar:حَتَّىٰ, tr:ḥattā, gloss:-e kadar} olumsuzlanan hâli {ar:نَبْعَثَ, tr:nabʿatha, gloss:gönderelim} eylemine dek uzatır; bekleme “alıkoymak” anlamındaki bir fiilden değil, olumsuz yüklemle gönderim sınırının kuruluşundan doğar. Buradaki ortaç ağır acı verme ve cezalandırmayı anlatır; ayet adlandırmayı her güçlüğe yaymaz. Kurulan eşik cezadan önceki bildirimdir; elçinin içeriği, yeterlilik ölçüsü ve daha geniş bir hukuk düzeni bu cümlede açılmaz.

{ar:نَبْعَثَ, tr:nabʿatha, gloss:göndermek} I. bâbın birinci çoğul, muzari mansub biçimidir; burada bir elçiyi belirli bir görev ya da hedef doğrultusunda yollamayı anlatır. Aynı gönderme ailesinin durgun olanı dışarıdan bir etkiyle harekete geçirme kullanımı da vardır. Elçinin uyarı ve açıklama taşımasıyla birleşince bu kullanım, muhatabın dikkatini cevaba açan bir çağrı imgesi ekleyebilir; bu olası yankı gerçek uyanma ya da dirilme anlamı taşımaz. Belirsiz ve mansub {ar:رَسُولًۭا, tr:rasūlan, gloss:bir elçi} gönderilen insanı adlandırır; böylece ayet soyut bir ileti yerine gönderenden alıcıya bildirim taşıyan kişiyi öne çıkarır. Bu taşıyıcılık, elçinin kimliğini, sözün içeriğini ya da yeterlilik ölçüsünü belirlemez; 17:54’te de peygamberin gözetici olmadığı belirtilir (17:54). Elçinin katkısı, sonucu yöneten bir vekil değil, ceza öncesi kamusal bildirim kanalı olmasıdır.

Çevredeki ayetler bildirimin erişimini dil, kitap açıklaması, ayet okuyuşu ve topluluk tanıklığı üzerinden somutlaştırır; bu sahneler kamusal kanalı görünür kılar, muhatapların aynı biçimde anlayıp izleyeceğini garanti etmez (14:4, 16:89, 28:59). 14:4 elçinin kendi kavminin diliyle açıklama yaptığını söyler (14:4); 16:89 kitabı açıklama ve hidayetle, toplulukları tanıklıkla ilişkilendirir (16:89). 28:59’da ayetleri okuyan bir elçi beldelerin yıkımından önce gönderilir (28:59). 17:54 rahmet ya da azabı Allah’ın iradesine bırakır ve peygamberi gözetici saymaz (17:54). Daha önceki 17:9’daki yol gösterme ve 17:11’deki aceleci istek örneği, elçiyle ulaşan bildirimin düzeltici olabileceğini düşündürür; bu bağlam elçinin özel mesajını tayin etmez (17:9, 17:11). 20:134 ve 28:47’de “daha önce elçi gelseydi işaretleri izlerdik” türü sözler aşağılanma ya da musibet öncesinde kurulmuş karşı-olgusal yakınmalardır; bunlar gerçekleşmiş itaati kanıtlamaz (20:134, 28:47).

Gönderme ailesinin surenin yakın çevresindeki kullanımları, cezalandırma eşiğinden farklı gönderim rollerini gösterir. 17:5’teki {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik}, kudretli kulların bir beldenin üzerine yollanmasını anlatır; aynı gönderme ailesi burada bildirim taşıyan elçiden çok yaptırım gücüyle birleşir (17:5, 17:15). 17:16’da ileri gelenlere buyruk verilir, onlar taşkınlık eder, ardından hüküm sözü gerçekleşir ve belde yıkılır (17:16). Bu sahne hitap, karşılık ve hüküm hareketini görünür kılar; bağlantı elçinin o buyruğu verdiğini söylemez ve sabit bir bekleme süresi ya da hukuk kuralı kurmaz (17:16, 17:15). Bu yakınlık, {ar:حَتَّىٰ, tr:ḥattā, gloss:-e kadar} ile açılan eşikte bildirim ve karşılık aşamasını düşünmeye imkân verir; 17:15’in açıkça belirlediği sınır elçi gönderilene kadardır.

## Öteki Ufuk ve Kişisel Ölçü

Yük cümlesindeki {ar:أُخْرَىٰ, tr:ukhrā, gloss:başkasının} sahiplik bağı başka bir kişiyi gösterir. Aynı kelime ailesi, 17:18 ve 17:19’daki hemen gelen dünya ile sonraki hayat karşıtlığında zaman ufkunu da açar (17:18, 17:19). Bu yankı iki ayrı işi korur: 17:15’te yükün öteki sahibi belirlenir, sonraki ayetlerdeki karşıtlık ise zaman ufkunu genişletir. 17:18’de {ar:يُرِيدُ ٱلْعَاجِلَةَ, tr:yurīdu al-ʿājilata, gloss:hemen geleni ister} diyenlerin payı {ar:عَجَّلْنَا, tr:ʿajjilnā, gloss:hemen veririz} sözüyle hızlandırılır, fakat Allah’ın dilemesine ve dilediği kişiye bağlıdır (17:18); 17:19’da {ar:أَرَادَ ٱلْآخِرَةَ, tr:arāda al-ākhirata, gloss:sonraki hayatı ister} diyerek iman eden, {ar:وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-saʿā lahā saʿyahā, gloss:onun için gereken çabayı gösterir} ve {ar:سَعْيُهُم مَّشْكُورًا, tr:saʿyuhum mashkūran, gloss:çabaları takdir edilmiş} olanların çabası takdir edilir (17:19). Bu zaman yankısı 17:15’teki sahiplik anlamını değiştirmeden ufku genişletir: yöneliş, arzuya ek olarak imanla gösterilen ve takdir edilen bir çabayı da içerir.

Bu çabanın gerçekleştiği imkân alanı da kişinin kendi ürettiği bir kaynağa indirgenmez. 17:20’de {ar:كُلًّا نُّمِدُّ هَٰٓؤُلَاءِ وَهَٰٓؤُلَاءِ مِنْ عَطَاءِ رَبِّكَ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi min ʿaṭāʾi rabbika, gloss:her iki gruba da Rabbinin bağışından veririz} sözü iki gruba da destek verildiğini, {ar:وَمَا كَانَ عَطَاءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūran, gloss:Rabbinin bağışı engellenmiş değildir} ise bu bağışın kapatılmadığını söyler (17:20). Bu sahne, yöneliş ve çabanın kişinin kendi sonucuyla ilişkili kalırken önündeki imkânın dışarıdan geldiğini gösterir (17:20). Bağış maddi ve dünyevi payları da kapsayabilir; bu karşılaştırma derecelerin nasıl dağıtıldığını açıklayan tam bir formül kurmaz (17:20). 17:21’de {ar:فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:faḍḍalnā baʿḍahum ʿalā baʿḍ, gloss:kimini kimine üstün kıldık} ve {ar:أَكْبَرُ دَرَجَاتٍ, tr:akbaru darajāt, gloss:dereceler bakımından daha büyük} ifadeleri derecelerin farklılaştığını belirtir (17:21). Böylece ortak bağış eşit sonuç demek değildir; kişinin yönelişi, kendisinden gelmeyen imkân ve değişen dereceler birlikte duyulur (17:20, 17:21).

Kişiye ait hesabın ölçüsü de herkes için özdeş değildir. 65:7 yükümlülüğü kişiye verilene ve kapasitesine göre sınırlar (65:7); 46:19 yapılan işlere göre derece ve karşılıktan söz eder (46:19). 99:7 ve 99:8 zerre ağırlığında iyilik ya da kötülüğün görüleceğini bildirir (99:7, 99:8). Böylece sorumluluk belirli kişiye ait kalırken kapasiteyle sınırlanır, yapılanlara göre farklılaşır ve en küçük fiilin bile görünürlüğüne kadar uzanır (65:7, 46:19, 99:7, 99:8).

</source_prose>
