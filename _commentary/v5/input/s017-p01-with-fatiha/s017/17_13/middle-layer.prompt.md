# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:13**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.middle.claims.json`

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
- Refer to source paragraphs as `17:13 ¶N`.

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

`(17:13 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:13",
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
        "citation": "(17:13 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_13/17_13.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_13/17_13.middle.claims.json \
  --ayah-ref 17:13
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_13/17_13.prose.editorial.tr.md`

<source_prose>
## Her Kişinin Payı

17:13'te herkes kendi hesabının muhatabıdır: {ar:كُلَّ إِنسَٰنٍ, tr:kulla insānin, gloss:her bir insan} için {ar:طَٰٓئِرَهُۥ, tr:ṭā'irahu, gloss:kişinin payı} boynuna bağlanır; {ar:يَوْمَ ٱلْقِيَٰمَةِ, tr:yawma al-qiyāmati, gloss:Kıyamet gününde} onun için {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} çıkarılır, kişi onu {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} açık bulur ve {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} fiiliyle kayıtla karşılaşır. Payın sahibi, boyun, kaydın yöneldiği kişi ve karşılaşan aynı bireydir. Ayet herkesi kapsarken onları tek bir toplu muhataba dönüştürmez; hesap kişi kişi açılır.

Cümle başındaki belirtme durumundaki {ar:كُلَّ, tr:kulla, gloss:her birini} önce insan alanını nesne olarak kurar, ardından bağlama eylemi kapsamın her üyesine uygulanır. Yalın durum varyantı açılışı konu-yorum düzenine yaklaştırabilirdi; iki biçim başlangıçta farklı vurgu kurar, biri ötekine üstün gelmez. Ardındaki belirsiz tekil {ar:إِنسَٰنٍ, tr:insānin, gloss:bir insan}, adı konmuş bir kişiyi değil, her defasında herhangi bir insanı verir. {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} içindeki kişi eki, {ar:طَٰٓئِرَهُۥ, tr:ṭā'irahu, gloss:kişinin payı} ve {ar:عُنُقِهِۦ, tr:ʿunuqihi, gloss:onun boynu} üzerindeki iyelikler ve {ar:لَهُۥ, tr:lahu, gloss:onun için} aynı insanı bağlama, sahiplik, beden yeri ve kayıt tahsisi boyunca izler. Buna karşılık {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} içindeki nesne eki kitabı gösterir: kişi karşılaşmanın öznesidir, az önce çıkarılan kayıt nesnesi. {ar:لَهُۥ, tr:lahu, gloss:onun için} kaydın alıcısını, hedefini ya da kendisine ayrıldığı kişiyi belirtir; tek başına onun lehine veya aleyhine hüküm vermez.

Kişinin payını adlandıran {ar:طَٰٓئِرَهُۥ, tr:ṭā'irahu, gloss:kişinin payı} olağan anlamıyla nasip ya da yapılanların sonucudur; etken ortaç biçimi aynı anda uçan varlık ve uçuş hareketini duyurur. İyelik eki uçuşu başıboş bırakmaz, kişinin kendi payına bağlar. Aktarılmış somut kuş varyantı kuşu öne çıkarırken ayetteki biçim uçuşu payın içinde hareket halinde tutar. Sözcüğün hemzesi kısa bir ses kesintisi yaratır; ardından gelen bağlama ve boyun, hareketli payı bedende yakalayarak uçuş imgesine bir durak verir. Bu işitsel etki biçimbirim ya da anlam kanıtı değil, imgenin ses düzenindeki eşlikçisidir.

Bu yakalamayı kuran {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} dördüncü kalıpta tamamlanmış ettirgen bir eylemdir: kişiyi bir işaretle ilişkilendirmekle kalmaz, kendi payına bağlı ve ondan sorumlu kılar. l-z-m ailesinin iliştirme, ayrılmazlık ve gereklilik yönleri burada dışarıdan kurulan yükümlülüğü açıklar; fiil sorumluluğu kurar, cezanın türü ve kapsamını ise belirlemez. {ar:فِى عُنُقِهِۦ, tr:fī ʿunuqihi, gloss:onun boynunda} tamlaması bağın boyunda kurulmasına da payın orada taşınmasına da izin verir. Her iki okuyuşta da {ar:عُنُقِهِۦ, tr:ʿunuqihi, gloss:onun boynu} başla gövdeyi birleştiren gerçek beden yeridir ve iyelik aynı kişiyi gösterir. Bu beden yeri, uçuşu taşıyan payı boyun üzerinde taşınan tasma benzeri bir yüke çevirir; benzetme sorumluluğu somutlaştırır, ayet ise gerçek bir tasma ya da pranga betimlemez. Bağlama bitmiş eylemdir, kişide süren bağlılık onun sonucudur; fiilin sıkışık ünsüzleri de bu noktada kapalı bir basınç etkisi bırakır.

Uçuşu ve kişisel payı taşıyan bu biçimin başka çekimleri uğurlu ya da uğursuz sayılan işareti de adlandırır. Bu yan dal, bir topluluğun başına gelen kötülüğü Musa'ya ve yanındakilere yükleyip uğurun Allah katında olduğunun söylendiği sahnede (7:131), elçilerin uğursuz sayılıp tehdit edilmesinde (36:18) ve bu atfın uğurun Allah katında olduğu, topluluğun ise sınandığı cevabıyla geri çevrilmesinde (27:47) etkinleşir. Bu sahnelerde işaret belirli toplulukların başkasına yönelttiği bir suçlamadır; 17:13'te ise her insan kendi payını taşır. Kelime ailesi, dışarıya yüklenen uğursuzluktan kişiye ait hesaba doğru bir yön değişimini duyurur ve olağan nasip ya da sonuç anlamı bu karşılaştırmada yerinde kalır.

Kıyamet gününde taşınan ağır yük, boyna bağlanan payın ayrılmaz ve kaçınılmaz sonuç yönünü güçlendirir (20:100). Kendi yüklerine başkalarıyla ilişkili ek yüklerin eşlik edebilmesi de sorumluluğun bir kişide katmanlanmasını düşündürür (29:13). Bu bağlantı kişiye ait payı korur; 17:13 başka birinin kaydının devredildiğini ya da ek yüklerin nedenini belirlemez.

Zaman tamlaması bu kişisel hesabın ne zaman görünür olduğuna odaklanır: belirtme durumundaki {ar:يَوْمَ, tr:yawma, gloss:gün ya da zaman} çıkarma eyleminin zaman zarfıdır, ardından gelen belirli tamlayan {ar:ٱلْقِيَٰمَةِ, tr:al-qiyāmati, gloss:diriliş ve yargı günü} hangi günün kastedildiğini tamamlar. Çıkarılış böylece gündüz vaktinden ayrılıp diriliş ve yargının belirli olay zamanına yerleşir; gün sözü olağan anlamını korur, tamlama ise bu ayetteki şahsî hesap vaktini verir. Ayetin kitap ortaya çıkmadan önce Kıyamet gününü anması, boyna bağlanan payın daha sonra çıkarılan kayıtla karşılaşmasını hesap önünde durma gibi duyurur. Bağ, kitap ve karşılaşma diriltilip yargılanmak üzere kalkış yankısını taşır; sahne bunu belirli bir beden duruşuna sabitlemez.

İkinci {ar:وَ, tr:wa, gloss:ve} tamamlanmış bağlama eylemini şimdiki-geniş çekimdeki çıkarma eylemine ekler: bağ kurulduktan sonra kitap çıkarılır. {ar:وَنُخْرِجُ لَهُۥ, tr:wa-nukhriju lahu, gloss:ve onun için çıkarırız} çoğul öznenin gerçekleştirdiği etken dördüncü kalıp fiildir; biçim şimdiki-geniş olsa da Kıyamet gününün çerçevesinde gerçekleşecek çıkarılışı bildirir. Belirsiz {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} bu fiilin doğrudan nesnesidir. Etken çıkarma fiili kaydı kişi için görünür kılar; çıkarıldığı yer ve yöntem belirtilmez.

Bu çıkarılan {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} vahyedilmiş Kitap'ın özel adı değil, kişinin yazılı kaydıdır. k-t-b ailesi harfleri düzenleyerek metin kurma ya da var olan metni kopyalama eylemini de, o eylemin ürünü olan kitabı da adlandırabilir; ayette ayrıca bir yazma işi anlatılmaz. Belirtme durumundaki biçim kayıt sözcüğünü çıkarma fiilinin nesnesi yapar; aktarılan yalın durum varyantı onu konuya ya da özneye yaklaştırabilirdi. Bu fark cümlenin açılış düzenini değiştirir, biçimler arasında üstünlük kurmaz. {ar:إِنسَٰنٍ, tr:insānin, gloss:bir insan}, {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} ve {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} sonlarındaki tenvin tilavette işitsel bir çizgi kurar; ses yakınlığı bu sözcükleri aynı dilbilgisel göreve getirmez.

Kaydın karşılaşma anındaki durumu {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} edilgen ortaçla verilir. Biçim belirsizlik ve hâl bakımından {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} ile uyuşur: kişi kaydı karşılaşma anında açık bulur; açan fail ya da açılma zamanı belirtilmez. Kökün kitap, sayfa ya da kumaş gibi yüzeyleri açıp yayma kullanımı burada kitabı görünür ve incelenebilir kılar; nesne kitaptır, dolayısıyla ortaç sayfa sayısını bildirmez. Açılmış sayfalar aynı yayılma anlamını daha geniş ifşa sahnesine taşır (81:10). Aynı kelime ailesinin yükseltme ve yeniden diriltme kullanımı hemen önce belirtilen Kıyamet günüyle yankılanır; bu, açık kayıt imgesine diriliş çağrışımı katar ve kitabı yazılı kayıt olarak bırakır.

Uçuş imgesinin kayda varışı, cümlenin işlemleri izlendiğinde belirginleşir: {ar:طَٰٓئِرَهُۥ, tr:ṭā'irahu, gloss:kişinin payı} önce ettirgen bağlamayla {ar:فِى عُنُقِهِۦ, tr:fī ʿunuqihi, gloss:onun boynunda} kişiye sabitlenir; sonra etken çıkarma onu {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} olarak görünür kılar. {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} bu yazılı sonucu yayılmış ve karşılaşılabilir durumda verir; {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} ise aynı kişiyi kendi kaydıyla yüz yüze getirir. Böylece uçuş imgesi yön değiştirerek yeri belirsiz işaretten sahibine bağlı, okunabilir bir güzergâha varır: pay boyunda sabitlenir, sonra açık kayıt halinde kişinin önüne gelir. Bu çizgi imgeseldir; ayette gerçek bir kuş, uçan ışık ya da fiziksel yolculuk yoktur.

Karşılaşmayı adlandıran {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} fiilinde kişi özne, önceki {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} ise doğrudan nesnedir; zamir tam bu kayda döner. Kişi belgeyi başkasından haber almakla yetinmez, kendi kitabıyla karşılaşır. Bu birinci kalıp yüz yüze gelişi kurar; başka çekimler bir şeyin önüne getirilmesini ya da karşısına çıkarılmasını öne alabilirdi. Kimin bu karşılaşmayı ayrıca sunduğu söylenmez. İyilik ve kötülükle karşılaşma kullanımı, her nefsin yaptığı iyiliği ve kötülüğü hazır bulduğu sahnede etkinleşir (3:30); böylece kitaba rastlamak kişinin kendi eylemleriyle yüz yüze gelişini de düşündürür. 3:30'daki kötülükten uzak olma dileği o ayetin sahnesinde kalır; 17:13'te karşılaşmanın kişide uyandırdığı tepki ve kaydın ayrıntılı içeriği açık bırakılır.

Karşılaşma, kişiyi yalnız hesabın sahibi değil, kendi karşılığını algılayan özne gibi düşündürür. {ar:إِنسَٰنٍ, tr:insānin, gloss:bir insan} olağan anlamını korurken görerek seçip fark etmeye uzanan kullanımı, kitabın açık bulunması ve kişiyle doğrudan karşılaşmasıyla tetiklenir: yazılı kayıt kişinin kendi yaptıklarının sabitlenmiş karşılığı gibi görünür. Aynı sözcüğün göz bebeğinin karasında görülen küçük insan biçimli yansımayı adlandıran yan anlamı bu öz-imgeye somut bir görsel dal ekler. Böylece açık kitaptaki kayıt kişinin kendi eylemlerini yansıtan sabit karşılığa benzer; bu benzetmenin nesnesi yazılı kayıttır, ayet gerçek göz, ayna ya da portre sahnesi kurmaz. Ayet yüz yüze gelişi söyler; görme ya da okuma fiili ile unutkanlık iddiası bu bağlantıya eklenmez.

Kişisel kaydın okunurluğu, karşılaşmayı okuma eylemine genişletir: kişinin kendi kitabını okuması açıkça emredilir (17:14). {ar:اقْرَأْ كِتَابَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} buyruğu okuma ya da tilaveti ve {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:kendin} öz-gönderimi aynı kişiyi okur, kanıtla yüzleşen kişi ve hesap sahibi olarak bir araya getirir. Bağlamdaki emir kişinin kendi kitabını okumasına yönelir; öğretme ya da iki kişinin karşılıklı okuması bu okuma dalına girmez. Böylece 17:13'teki karşılaşma, kişinin kendi metnine dönük okuması olarak belirginleşir.

Bu kişisel kitap, Musa'ya verilen ve İsrailoğulları için hidayet kılınan yazılı kitapla aynı yazı ve sayfa düşüncesinde buluşur (17:2). 17:13'teki {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} ile 17:2'deki {ar:الْكِتَابَ, tr:al-kitāba, gloss:Kitap} yazılı ürünün farklı muhataplara yöneldiğini gösterir: biri topluluğa yol gösterir, öteki her kişinin kendi hesabıdır; 17:14'teki kendi kitabını okuma buyruğu bu ikinci işlevi görünür kılar (17:14). Ortak yazılı nesne karşılaştırmayı mümkün kılar; alıcı ve işlev farklı olduğundan iki kitabın içeriği, yetkisi ve statüsü özdeşleşmez.

Yazılı kaydın daha geniş hesapta neleri taşıyabileceği, eylemden geriye kalan izler ve bellekte unutulanlar üzerinden açılır. Yapılanların ve arkalarında bıraktıkları izlerin yazılması kaydı anlık eylemi aşan sonuçlara uzatır (36:12); unutulmuş işlerin sayılıp kişilere bildirilmesi belleğin gerisinde kalanları da hesaba getirir (58:6). Bu iki sahne kişisel kitabın kapsamını ve tutulma yöntemini açık bırakır. Ayrıca diller, eller ve ayaklar yapılanlara tanıklık edebilir (24:24): beden yazılı kaydın yanına ayrı bir kanıt biçimi ekler. Açık kitap böylece daha geniş hesap sahnesinde yer alır; bu bağlamlarda yazılı kayıt tek kanıt diye sunulmaz.

## Tarihsel Dönüş ve Hesap

Kişisel hesabın yanına topluluk ölçeğinde yazılmış bir tarih konduğunda, dönüşün kime ait olduğu değişir. İsrailoğulları için Kitap'taki yazılı hüküm ve hükme bağlanan sonuç (17:4), ilkinin belirlenmiş vaadi (17:5) ve Kıyamet gününde her kişi için çıkarılan {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} birlikte düşünüldüğünde, tarihsel sonuç kişisel hesapta yeniden görünür olur (17:13). Paralellik ölçek değişiminde kurulur: 17:4'teki yazılı hüküm, tarihsel olay ve topluluk hesabı 17:13'teki kişisel kayıtla özdeşleşmez; belirlenmiş vaat de bu bağı daha geniş bir takvime çevirmez.

Bu ölçek değişimi, iyilik ve zararın yapanlara dönmesiyle daha da belirginleşir. Kişilerin kendileri için iyilik ettiğini ve kötülüğün de eyleyene döndüğünü söyleyen anlatım, hesabı yaşayan kişiye bağlar (17:7); öz-gönderim, 17:13'te her kişinin kendi kaydıyla karşılaşmasına yakındır. “Dönerseniz biz de döneriz” şartı tarihsel dönüşü dile getirir (17:8) ve kişinin üzerinde kalan {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} bağıyla bir süreklilik yankısı kurar. Bu yankı, bağın kişi üzerindeki sonucunu tarihsel dönüşle birlikte duyurur; dilbilgisel dayanak yine 17:13'teki tamamlanmış IV. kalıptır. Böylece topluluk ve kuşaklar için anlatılan dönüş kişi ölçeğinde yeniden işitilir, iki sahne tek bir olay dizisine dönüşmez.

Tarihsel ölçekteki dönüşün ardından kayıt, aceleyle yaşananı sonradan okunur hale getirir. İnsanın aceleciliği (17:11), hesabın sayımı ve ayrıntılı ayrıştırılması (17:12), açık bulunan {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} kitap (17:13), “kitabını oku” buyruğu (17:14) ve hiçbir yük taşıyanın başkasının yükünü taşımayacağı ilkesi (17:15) bir okuma sırası kurar. {ar:الْحِسَابَ, tr:al-ḥisāba, gloss:hesap} sayılabilir eylemleri; {ar:فَصَّلْنَاهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:ayrıntısıyla ayırdık} ise bunların tek parça kalmayıp incelenmesini öne çıkarır (17:12). Böylece aceleyle geçilen işler sahibinin okuyacağı ayrıntılı hesaba dönüşür. Yavaş okuma bu sıranın kurduğu karşıtlıktır, {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} sözcüğünün anlamı değil. {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:kendin} okuyanı, kanıtla karşılaşanı ve hesabın sahibini aynı kişide toplar (17:14). Bu sıra her eylemin kasıtlı olduğunu ya da bir zaman kuramı sunduğunu gerektirmez; sayım, ayrıntı, okuma ve kişiye ait yük yargının ayrı öğeleri olarak da durabilir.

17:15 başkasının yükünü üstlenmeme ilkesini koyarken, kendi yüklerine başkalarıyla ilişkili ek yüklerin eşlik edebildiği birikimli sorumluluk katmanı da vardır (29:13). Bu yan yanalık {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} ile kurulan kişisel bağı derinleştirir; ek yükler başka birinin kaydının devredildiği anlamına gelmez ve 17:13 bunların nedenini belirlemez.

Kayıt, önceden bilinen davranışları sahibinin önünde açan bir karşılaşma olarak belirir. Hükmün gerçekleşmiş oluşu (17:16), Rabbin kullarını iç yüzleriyle bilmesi ve görmesi (17:17), {ar:خَبِيرًا بَصِيرًا, tr:khabīran baṣīran, gloss:iç yüzünden haberdar ve gören} nitelemesi ve kulların günahlarının anılması, kitabın bilinen davranışları Tanrı'ya aktarmak yerine sahibine açmasını destekler (17:17). {ar:نُخْرِجُ لَهُۥ, tr:nukhriju lahu, gloss:onun için çıkarırız} hesabı sahibine yöneltir; {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} kişiyi kitabıyla buluşturur, {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} ise önünde açık duran yüzeyi verir (17:13). Bu birleşim, kitabı hükme bağlanmış hesabın kişiye sunulan kanıtı gibi duyurabilir; ayet belirli bir mahkeme usulü ya da mühürlü veya mühürsüz resmî evrak türü tanımlamaz. Daha önce kişiye erişilemeyen içeriğin açığa çıkması bu sunuluşun olası etkisidir; çıkarma fiili tek başına gizli bir yer göstermez ve bağlam ilahî bilgisizlik düşündürmez.

## Yöneliş, Derece ve Yardım

Hesabın kişiye açılması, doğru yola yönelişle yan yana geldiğinde seyrin hangi ölçü karşısında göründüğü sorusunu doğurur. En doğru olana yöneltme ve iyi işler, uçuş imgesine başıboş olmayan bir yön verir (17:9); hesabın ayrıntılı ayrıştırılması da kaydı incelenebilir kılar (17:12). Üstünlük derecesindeki {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün ve dengeli} ile {ar:ٱلْقِيَٰمَةِ, tr:al-qiyāmati, gloss:diriliş ve yargı günü} aynı kelime ailesindendir, fakat biri düzgün ve doğru olana yönelişi, öteki diriliş ve yargı olayını adlandırır. Bu ses yakınlığı, kişisel seyrin yargı gününde doğruluk ölçüsü karşısında görünür olabileceği okumayı destekler; ortak kök bunu tek başına kanıtlamaz. İki sözcüğün olağan anlamları yerinde kalır; rehberlik, ayrıntılı hesap ve diriliş ayrı ayrı da okunabilir.

Bu yöneliş, yakın hayatı arama ile ahirete yönelme arasındaki farklılıkta bir güzergâh gibi genişler. Yakın olanı isteme hedefi ve onu hızlandıran eylem arzunun temposunu verir (17:18); ahireti isteyip ona yaraşır biçimde çaba gösterme, kat edilen yolu ve karşılık gören emeği öne çıkarır (17:19). {ar:طَٰٓئِرَهُۥ, tr:ṭā'irahu, gloss:kişinin payı} içindeki uçuş, hedef, hız ve çabayla birleşince kişinin seyrini taşıyan bir imge kazanır. Bu dal arzunun yönünü ve çabanın yolunu hesaba katan bir okuma açar; aynı kitap ayrı ayrı yapılan işleri kaydeden bir liste olarak da anlaşılabilir. Sonucun bütünüyle kişinin denetiminde olduğu bu okumadan çıkmaz.

İki yönelişin ikisine de rızık verilmesi, yolun sürmesini ve hesabın kişilere göre ayrışmasını birlikte duyurur (17:20). Dağıtıcı {ar:كُلًّا, tr:kullan, gloss:her birine} sözü bu rızkı iki topluluğa tek bir kitleymiş gibi değil, her birine yönelen bir veriş olarak okutur. Farklı dereceler (17:21), yalnızca son bir sıralamayı değil, varılan düzeylere doğru ilerleyişi de düşündürebilir; {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:kimini kimine üstün kıldık} karşılaştırmayı, {ar:دَرَجَاتٍ, tr:darajātin, gloss:dereceler} ise düzeyleri adlandırır. Bu farklılaşma Kıyamet gününde kişinin kitabıyla karşılaşmasıyla yan yana gelince, seyrin sonucunun dereceli olabileceği bir okumaya açılır (17:13, 17:21). {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} iyilik ya da kötülükle karşılaşma kullanımını bu güzergâha da yansıtabilir; ayetteki açık nesne kitaptır, sonucun olumlu ya da olumsuz yönü ise açık bırakılır.

Boyunda taşınan sorumluluk ve yazılı kayıt, şükreden kul imgesiyle birlikte okunduğunda hukukî bir yankı da kazanır (17:3). {ar:عَبْدًا شَكُورًا, tr:ʿabdan shakūran, gloss:şükreden bir kul} sözüyle tetiklenen keşifsel benzetme, özel hukukta köleleştirilmiş kişinin kendi özgürlük bedelini ödemesine dayanan yazılı sözleşmeyi çağrıştırabilir. Bu yankıda {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} kişiye dışarıdan yüklenen sorumluluğu, {ar:فِى عُنُقِهِۦ, tr:fī ʿunuqihi, gloss:onun boynunda} bedensel bağ yerini, {ar:كِتَٰبًۭا, tr:kitāban, gloss:yazılı kayıt} ise yazılı metni sağlar. Benzetmenin katkısı bu bağlı yük ile metni bir araya getiren sözleşme imgesidir; 17:13'te sözleşmenin kendisi kurulmaz, dolayısıyla bir sahip, köleleştirilmiş karşı taraf, taksit, ödeme ya da azat koşulu belirlenmez.

Bu kişisel hesap, topluca edilen yardım ve hidayet dileğiyle birlikte düşünüldüğünde sorumluluğun kendi kendine yeterlilik anlamına gelmediğini gösterir. “Yalnız Sana kulluk eder ve yalnız Senden yardım isteriz” çoğul kulluk ve yardım isteğini (1:5), “bizi dosdoğru yola ilet” ise ortak yön bulma duasını taşır (1:6). Her bireyin payını bağlayan ve onun için yazılı kayıt çıkaran ayet, bu ortak dilekle yan yana durduğunda her kişinin kendi hesabını korurken başkalarıyla birlikte yardıma yöneldiğini düşündürür. Böylece ortak dua bireysel sorumluluğu silmeden yardıma yönelişi taşır; başkasının kaydını devralmaz ve hesabın sonucunu tayin etmez.

</source_prose>
