# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:17**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.middle.claims.json`

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
- Refer to source paragraphs as `17:17 ¶N`.

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

`(17:17 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:17",
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
        "citation": "(17:17 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_17/17_17.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_17/17_17.middle.claims.json \
  --ayah-ref 17:17
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_17/17_17.prose.editorial.tr.md`

<source_prose>
Âyet önce Nuh’tan sonra nice kuşağı yok ettiğimizi bildirir. Ardından muhatabına döner: Rabbin, kullarının günahlarını bilip görmede yeterlidir. İlk hareket tarihteki toplulukları ve onları yok eden eylemi, ikincisi bu kulları bilen ve gören Rabbin yeterliliğini öne çıkarır. {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} ile kurulan yıkım ve {ar:كَفَىٰ, tr:kafā, gloss:yeter} ile kurulan yeterlilik kendi olağan anlamlarını korur; âyet tarihî bildirimden doğrudan hitaba geçer.

## Kuşakları Saymak

Başlangıçtaki {ar:وَ, tr:wa, gloss:ve}, öne alınan {ar:كَمْ, tr:kam, gloss:nice} ve ardından gelen {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik}, eylemden önce sayıyı kurar. Fiilin nesnesi olarak öne çıkan {ar:كَمْ, tr:kam, gloss:nice}, tek bir yıkımdan geniş ve kesin rakama kapanmayan bir tarih ölçeğine geçirir. İlk {ar:وَ, tr:wa, gloss:ve} yerel bağlaç öneki olarak bu nicelikli taramayı açar; tek başına önceki âyetin içeriğini taşımaz. Yıkım cümlesinden sonraki ikinci {ar:وَ, tr:wa, gloss:ve}, {ar:كَفَىٰ, tr:kafā, gloss:yeter} hükmüne hem bağlanır hem yeni bir bildirim hareketi başlatır; bu iki ilişki birlikte duyulur. Aynı bağlacın iki açılışta tekrarı da yazılı ses akışında onları eşler.

İlk {ar:مِنَ, tr:mina, gloss:-den; arasından}, {ar:ٱلْقُرُونِ, tr:al-qurūni, gloss:kuşaklar} adını sayılan sınıf olarak belirler. Belirli çoğul isim olan {ar:ٱلْقُرُونِ, tr:al-qurūni, gloss:kuşaklar}, bu edattan sonra onun yönettiği mecrur biçimde gelir. {ar:قَرْن, tr:qarn, gloss:kuşak} aynı dönemde yaşayan topluluğu da o topluluğun yaşadığı zaman dilimini de anlatabilir; {ar:كَمْ, tr:kam, gloss:nice} ve Nuh sonrasına yerleştiren zaman öbeği iki anlamı da duyurur. İlk {ar:مِنَ, tr:mina, gloss:-den; arasından} miktarla sınıf arasındaki ilişkiyi kurar ve sınıftan bir payı akla getirir: nice kuşak, bu sınıfın içinden sayılır. Böylece {ar:قَرْن, tr:qarn, gloss:kuşak} ortak çağdaki toplulukla onun yaşadığı dönemi birlikte taşıyan bir tarih birimi olur; bu birim için sabit bir yıl ölçüsü verilmez.

İkinci {ar:مِنۢ, tr:min, gloss:-den başlayarak}, ilk edat gibi bir sayım sınıfı kurmaz; ayrı bir zaman öbeği açar. {ar:بَعْدِ, tr:baʿdi, gloss:sonra} tek başına tamamlanmayan bir zaman adıdır; {ar:نُوحٍۢ, tr:Nūḥin, gloss:Nuh} onun tamlayıcısı olarak mecrur gelir ve sonralığı adlandırılmış bir kronolojik noktaya bağlar. Böylece {ar:مِنۢ بَعْدِ نُوحٍۢ, tr:min baʿdi Nūḥin, gloss:Nuh’tan sonra} kuşakları sıraya dizer, aradaki süreyi ölçmez. İlk {ar:مِنَ, tr:mina, gloss:-den; arasından} ile onu izleyen isim kısa bir ses birimi kurar; bu yazılı ritim belirli bir tilavet biçimini varsaymaz. {ar:مِنۢ بَعْدِ نُوحٍۢ, tr:min baʿdi Nūḥin, gloss:Nuh’tan sonra} ise kesintisiz bir zaman öbeğidir; kısa {ar:بَعْدِ, tr:baʿdi, gloss:sonra}, kuşaklarla Nuh adı arasında bir menteşe gibi işitilir.

Kuşak anlamının yanında, {ar:قَرْن, tr:qarn, gloss:kuşak} aynı kelime ailesindeki birleştirme ve bağlama kullanımını da yankılayabilir. {ar:كَمْ, tr:kam, gloss:nice} ile açılan çokluk, {ar:بَعْدِ, tr:baʿdi, gloss:sonra} ile kurulan tarih sırası ve {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} ile bildirilen yıkım, toplulukları kopuk olaylar yerine birbirini izleyen bir geçmiş içinde duyurur. 6:6’da bir kuşağın yok edilmesinin ardından başka birinin gelişi bu ardışıklığı görünür kılar ({ar:قَرْنًا آخَرِينَ, tr:qarnan ākharīn, gloss:başka bir kuşak}). Bu olası bağlama yankısı olağan “kuşak” anlamını genişletir: tarihî çizgide toplulukları birbirini izleyen ve birbirine bağlanan bir geçmiş içinde duyurur. Bu bağlantı her kuşağın aynı biçimde kurulduğunu ileri sürmez.

17:3’te Nuh’la birlikte taşınanların soyundan gelenler ve Nuh’un çok şükreden bir kul oluşu anılır ({ar:ذُرِّيَّةَ مَنْ حَمَلْنَا مَعَ نُوحٍ, tr:dhurriyyata man ḥamalnā maʿa Nūḥ, gloss:Nuh’la taşınanların soyu}; {ar:عَبْدًا شَكُورًا, tr:ʿabdan shakūrā, gloss:çok şükreden bir kul}). Bu korunmuş başlangıç, Nuh’u yalnızca sonralığın takvimsel eşiği değil, sonraki kuşaklarda davranışın yeniden mümkün olduğu tarihî bir eşik olarak da duyurabilir. 17:3 muhatapların kimliğini belirtiyor da olabilir; bu bağlantı kesintisiz biyolojik soy, belirli bir kuşak süresi, lanet ya da ahlaki miras tayin etmez.

Bu tarih çizgisinin yanında 17:4, 17:6, 17:7 ve 17:8’de İsrailoğullarına özgü bir tekrar ve dönüş dizisi açılır. 17:4’te bozgunculuğun iki kez yapılacağının söylenmesi, kuşakların sayımına belirli bir tarihî tekrar ekler ({ar:لَتُفْسِدُنَّ, tr:latufsidunna, gloss:bozgunculuk edeceksiniz}; {ar:مَرَّتَيْنِ, tr:marratayn, gloss:iki kez}). 17:6’daki geri çevirme ve yeniden dönüş, diziyi karşılıkla ilerletir ({ar:رَدَدْنَا, tr:radadnā, gloss:geri çevirdik}; {ar:الْكَرَّةَ, tr:al-karrata, gloss:yeniden dönüş}); 17:7’de ikinci vaat ve yıkıp etkisizleştirme, belirlenmiş ikinci vakti ve sonucunu yan yana getirir ({ar:وَعْدُ الْآخِرَةِ, tr:waʿdu l-ākhirati, gloss:ikinci vaat}; {ar:لِيُتَبِّرُوا, tr:li-yutabbirū, gloss:yıkıp ortadan kaldırmaları}; {ar:تَتْبِيرًا, tr:tatbīran, gloss:bütünüyle yıkım}). 17:8 ise dönüş halinde merhamet ve karşılık ihtimalini açık tutar ({ar:يَرْحَمَكُمْ, tr:yarḥamakum, gloss:size merhamet etmesi}; {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:dönerseniz biz de döneriz}). Bu İsrailoğullarına özgü tarihî sıra bozulma, dönüş, yıkım ve şartlı merhamet hareketlerini birbirine bağlar; bu bağlantı bütün kuşaklar için değişmez bir çevrim ya da her dönüşte merhamet güvencesi kurmaz.

## Yıkımın ve Hesabın Ölçeği

Sayımın ardından gelen {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik}, IV. bâbın etkin ettirgen perfect biçimidir; sonundaki {ar:نَا, tr:nā, gloss:biz} birinci çoğul özneyi taşır. Böylece kuşakların başına gelen, faili belirsiz edilgen bir kayboluş değil, belirli bir öznenin onları yok oluşa ya da ağır bozulmaya sürüklediği tamamlanmış bir eylem olarak kurulur. Fiilin çekirdeği yok etmedir; ölüm, dağılma ve işlev kaybı bu yıkımın eşlik eden alanlarıdır. Kısa gövdenin ses etkisi yazılı yüzeyle sınırlıdır, özel bir okuyuş biçimini varsaymaz; nicelikten sonra inişi yıkım eyleminin kuvvetini duyurur.

17:12’de geceyle gündüz işaret, yıllar sayım ve hesap konusu olur; ayrıntılı açıklama da bu ölçüye eklenir ({ar:عَدَدَ السِّنِينَ وَالْحِسَابَ, tr:ʿadada as-sinīna wa-l-ḥisāb, gloss:yılların sayısı ve hesap}; {ar:فَصَّلْنَاهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:ayrıntısıyla açıkladık}). 17:13’te her insanın kendi yaptığının karşılığı boynuna bağlanır ve önüne açık bir kayıt konur ({ar:أَلْزَمْنَاهُ طَائِرَهُ فِي عُنُقِهِ, tr:alzamnāhu ṭāʾirahu fī ʿunuqihi, gloss:kendi payını boynuna bağladık}; {ar:كِتَابًا يَلْقَاهُ مَنْشُورًا, tr:kitāban yalqāhu manshūran, gloss:açık bulacağı bir kitap}). 17:14’te kişiye kendi kitabını okuması söylenir ({ar:اقْرَأْ كِتَابَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku}). Böylece kuşakların toplu yıkımının yanında, her kişinin kendi eylemini okuyacağı ayrı bir hesap ölçeği belirir.

17:14’teki “hesap sorucu olarak bugün kendin yeterlisin” sözü, odaktaki {ar:كَفَىٰ بِرَبِّكَ, tr:kafā bi-rabbika, gloss:Rabbin yeter} kuruluşundaki yeterlilik fiilini kişisel hesaba taşır ({ar:كَفَىٰ بِنَفْسِكَ الْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā binafsika al-yawma ʿalayka ḥasīban, gloss:hesap sorucu olarak kendin yeterlisin}). Öz-hesap ile Rabbin kulların günahları hakkında yeterli oluşu yan yana gelir, fakat iki kayıt aynı deftere dönüşmez. 17:15’te kimsenin başkasının yükünü taşımaması ve elçi gönderilmeden azap edilmemesi, sorumluluğun ve yargının sınırını koyar ({ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz}); bu karşılaştırma her kuşak için aynı elçinin bulunduğunu ileri sürmez. Bu sınırlar toplu tarih anlatısının bireysel hesabı silmesini önler ve kişiyi kendi eyleminin muhatabı olarak bırakır.

Bu kişisel kayıt ölçeğinin ardından 17:16’da şehir ihtimaliyle toplumsal sahne genişler ({ar:نُهْلِكَ قَرْيَةً, tr:nuhlika qaryatan, gloss:bir şehri helak etmek}). Emir fiili refah içindeki ileri gelenlere bağlanır ({ar:أَمَرْنَا مُتْرَفِيهَا, tr:amarnā mutrafīhā, gloss:varlıklılara ilişkin emir}; {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:refah içindeki ileri gelenleri}); bolluk ve lüks anlamı, insanın salıverilmesi ya da gevşemesi yönünü de taşır. Bu yapıda emrin gücü ve nasıl anlaşılacağı açık kalır. Ardından gelen bozgunculuk sınır aşımını bildirir ({ar:فَفَسَقُوا, tr:fafasaqū, gloss:sınırı aştılar}); aynı kökün hurmanın kabuğundan dışarı çıkma imgesi bu eşiğin maddi yankısını verir ve ayrıcalık sonrasındaki sınır aşımını görünür bir çıkış olarak düşündürür. Bu, gerçek bir meyve olayı değil, sınır aşımına ilişkin bir imgedir.

17:16’daki sınır aşımından sonra hak edilmiş talep ya da yükümlülüğün bağlayıcı hale gelişi, ardından da işaret eden bir bildirim duyulur ({ar:حَقَّ, tr:ḥaqqa, gloss:hak oldu}; {ar:الْقَوْلُ, tr:al-qawlu, gloss:söz veya bildirim}). Bildirimin içeriği verilmez ve şehir konuşturulmaz; sonucu, şehrin bütünüyle yıkımında görünür ({ar:فَدَمَّرْنَاهَا تَدْمِيرًا, tr:fadammarnāhā tadmīran, gloss:şehri bütünüyle yıktık}). Aynı ayetteki {ar:نُهْلِكَ, tr:nuhlika, gloss:helak etmek} odaktaki {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} ile aynı helak etme ailesindedir; şehrin sonunu bildiren {ar:فَدَمَّرْنَاهَا تَدْمِيرًا, tr:fadammarnāhā tadmīran, gloss:şehri bütünüyle yıktık} ise başka bir fiille tam yıkımı tamamlar. Böylece kent sahnesi, güçlü ve varlıklı bir kesimin toplumsal çöküşe aracılık edebildiği somut bir örnek sunar. Bu özel bağlantı odak âyetin bütün kullarını ileri gelenlerle özdeşleştirmez, suçu yalnız onlara yüklemez ya da her kuşak için aynı nedeni vermez.

## Günah, Kul ve Geride Kalan İz

Odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} yeterlilik bildiriminin hangi alanla ilgili olduğunu belirtir. {ar:بِذُنُوبِ, tr:bi-dhunūbi, gloss:günahlar hakkında}, bi edatının mecrur kıldığı çoğul isimdir; {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:kulları} ile kurduğu tamlayan bağı günahları kullara nispet eder. Olağan anlam ahlaken yanlış işler ve kusurlardır. 6:6’da günahlar bir topluluğun yok edilişiyle yan yana gelir; 47:19’da ise günah için bağışlanma istenir ve aynı âyette inananlar için de bağışlanma dileği yer alır ({ar:وَاسْتَغْفِرْ لِذَنْبِكَ, tr:wa-staghfir li-dhanbika, gloss:günahın için bağışlanma dile}). Bu iki ayrı sonuç günahın olağan ahlaki anlamını ve bağışlanma yönelişini yıkım anlatısının yanında tutar; bu karşılaştırma her yanlışın kaçınılmaz biçimde ve hemen yıkımla biteceği bir kural kurmaz.

Günah adının yanında, aynı kelime ailesinin sonuçtan alınan payı düşündüren bir yankısı da vardır. 51:59’da haksızlık edenlerin payı yoldaşlarınınkine benzetilir ({ar:ذَنُوبًا مِثْلَ ذَنُوبِ أَصْحَابِهِمْ, tr:dhunūban mithla dhunūbi aṣḥābihim, gloss:yoldaşlarının payı gibi bir pay}); burada özellikle azap payı düşünülebilir. Bu temas, odaktaki {ar:ذُنُوبِ, tr:dhunūbi, gloss:günahlar} çoğul adının eylem anlamını koruyarak onu önceki topluluklarla örüntülenen olası bir sonuç payı yankısına yaklaştırır. 51:59’daki biçimin sözcüksel çözümlemesi kesinleşmediğinden, bu yalnızca bağlamsal bir yankıdır: “pay” odaktaki günahın çevirisi değildir; bu bağlantı miras alınmış suç ya da herkes için kaçınılmaz ceza da ileri sürmez.

Odaktaki {ar:ذُنُوبِ, tr:dhunūbi, gloss:günahlar} biçimi günah adıdır, hayvan kuyruğunun doğrudan adı değildir; aynı kelime ailesindeki {ar:ذَنَب, tr:dhanab, gloss:kuyruk} kuyruğu anlatır, genişletilmiş kullanımda arka ucu ya da son bölümü de belirtir. Ailenin bir başka kullanımı “ardından gidenler”i ve birinin izini sürenleri anlatır. Biçimler ayrı kalır: {ar:ٱلْقُرُونِ, tr:al-qurūni, gloss:kuşaklar} ve {ar:بَعْدِ, tr:baʿdi, gloss:sonra} tarihî ardışıklığı kurarken, {ar:قَرْن, tr:qarn, gloss:kuşak} için duyulan bağlama yankısı eylemleri, kulları ve dönemleri aynı tarih çizgisinde bir araya getirir. Bu kelime ailesi odağın olağan günah anlamını değiştirmeden, eylemi işleyenler geçtikten sonra da okunabilen bir arka-iz imgesi ekler.

Bu {ar:ذَنَب, tr:dhanab, gloss:kuyruk} arka-iz imgesi odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} ile farklı ölçekleri bir araya getirir. 17:3’teki taşınmış soy çizgisi ve Nuh’tan sonraki kuşaklar tarihî gövdeyi kurar. 17:13’te kişinin boynuna bağlanan ve önüne açık konan kayıt ile 17:14’teki okuma buyruğu bireysel izi görünür kılar; 17:15’te başkasının yükünü taşımama ilkesi bu izi sahibine bağlı tutar. 17:16’daki kent yıkımı toplumsal sonucu, 17:18’de hemen istenen dünya hayatına yönelişe verilecek karşılık arzu ile sonucu arasındaki bağı ekler; 6:6’da yıkılmış kuşağın ardından yenisinin gelmesi ardışıklığı sürdürür. Bir arada düşünüldüğünde, kişi ve topluluklar geçtikten sonra da sonuçların okunabilirliği kalır. Bu bağlantı kuşaklar arası suç aktarımını ya da kanıtlanmış tek bir nedensellik zincirini ileri sürmez; kişisel sorumluluk ile toplulukların ardışık akıbetini aynı geçmişte farklı ölçekler olarak duyurur.

## Rab ve Kullar

{ar:بِرَبِّكَ, tr:bi-rabbika, gloss:senin Rabbin} tek bir yazı biriminde bi edatını, Rab adını ve muhataba yönelen {ar:كَ, tr:ka, gloss:senin} hitap ekini buluşturur. Biçimce edattan dolayı mecrur olsa da Rab, {ar:كَفَىٰ, tr:kafā, gloss:yeter} fiilinin yeterli öznesidir; hitap eki de yeterlilik sözünün içinde kalır. {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:kulları} içindeki iyelik eki aynı Rabbe döner; {ar:بِذُنُوبِ, tr:bi-dhunūbi, gloss:günahlar hakkında} ise bu kullara bağlanan tamlamayı kurar. Bu ses gözlemi yazılı biçimle sınırlıdır, belirli bir tilavet icrası varsaymaz; hitap ve iyelik ekleri aynı Rab-kul ilişkisini metnin içinde tutar.

{ar:رَبّ, tr:rabb, gloss:Rab} adı sahiplik, buyruk yetkisi ve yönetip düzenleme anlamlarını taşır; gözetileni adım adım yetiştirip geliştirme kullanımı da bu adın yanında duyulabilir. Bu yetiştirme yankısı yönetimin gelişim yönünü ekler. {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} ile {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:kulları} aynı âyette karşılaşınca, yıkım süreklilik taşıyan Rab-kul ilişkisi içinde okunur; bu yankı yok etmeyi onarım, merhamet ya da açıklanmış bir adalet hükmü olarak yeniden adlandırmaz. {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:kulları} üçüncü şahıs iyelik eki taşıyan çoğul bir isimdir, fiil değildir; buradaki kulluk hukuki kölelik iddiası kurmaz. Kulların tâbiyet ve alçalma yönü sözcüğü yalnız biçimsel ibadet eyleminden daha geniş bir Rabbe bağlılık ilişkisi olarak duyurur.

17:1’de gece yolculuğuna çıkarılan tekil kul, işaretlerin kendisine gösterilmesiyle anılır ve âyet gören sıfatıyla kapanır ({ar:عَبْدِهِ, tr:ʿabdihi, gloss:O’nun kulu}; {ar:لِنُرِيَهُ آيَاتِنَا, tr:linuriyahu āyātinā, gloss:ayetlerimizden ona göstermemiz}; {ar:الْبَصِيرُ, tr:al-baṣīr, gloss:gören}). 17:3’te ise Nuh şükreden kuldur ({ar:عَبْدًا شَكُورًا, tr:ʿabdan shakūrā, gloss:çok şükreden bir kul}); odaktaki {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:O’nun kulları} çoğuldur. Nuh’un şükrüyle kulların günahları ayrı davranışlardır ve kişiler aynı değildir; ortak Rabbe aidiyet bu farklı insanları aynı ilişki içinde buluşturur.

Fâtiha’nın 1:5’teki “Yalnız Sana kulluk ederiz” çoğul ikrarı da aynı kulluk ailesine katılır ({ar:إِيَّاكَ نَعْبُدُ, tr:iyyāka naʿbudu, gloss:Yalnız Sana kulluk ederiz}). Paylaşılan kulluk dili, dua eden “biz”in odaktaki {ar:عِبَادِهِۦ, tr:ʿibādihi, gloss:O’nun kulları} sınıfına dahil olabileceği ihtimalini açar; böylece tarihî uyarı okurun kendi ikrarına da değebilir. Bu olası bağ dua edenleri belirli bir günahla ya da helak edilmiş kuşaklarla özdeşleştirmez.

## Yeterlilik, Bilgi ve Görme

İkinci bağlaçtan sonra gelen {ar:كَفَىٰ, tr:kafā, gloss:yeter}, geçmişte tamamlanmış fiil biçimiyle yeterlilik hükmünü kurar; kendinden önceki ettirgen yok etme fiilinden ayrılır. Ardından gelen {ar:بِرَبِّكَ, tr:bi-rabbika, gloss:senin Rabbin} yeter özneyi, ikinci edatlı öbek {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları hakkında} bu yeterliliğin alanını belirtir. Olağan anlam, bir ihtiyacı karşılayacak kadar yeterli olmaktır. {ar:كَفَىٰ, tr:kafā, gloss:yeter} aynı zamanda bir işi, yükü ya da sorumluluğu üstlenip yerine getirme; bir açığı kapatarak ihtiyacı karşılayıp sonuca erişme yönlerinde yankılanabilir. Bu yan yankılar, {ar:رَبّ, tr:rabb, gloss:Rab} adının yönetim anlamı ve önceki {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} fiiliyle temas ederek yeterlilik hükmünü Rabbin yönetim ve hesap ilişkisi içinde duyurur. Bu özel temas her felaketin nedenini açıklamaz; yıkımı adil ya da zorunlu da kılmaz.

Rabbin yeterliliğinin nasıl gerçekleştiğini iki niteleme açar: {ar:خَبِيرًا, tr:khabīran, gloss:iç yüzünü bilen} ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören}. İkisi de belirsiz mansub biçimdedir; ilk niteleme iç yüzü bilme ve uzmanlığı, bir olay hakkındaki bilgiyi ve görünüşün gerisindeki gerçek niteliği öne çıkarır, ikincisi doğrudan görmeyi ekleyerek hükmü tamamlar. Odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları}nın açıkça adlandırılması, dışarıdan algılanan eylemle iç niteliği aynı bilgi alanına getirir. {ar:خَبِير, tr:khabīr, gloss:iç yüzünü bilen} için sınama ya da tecrübe ederek bilme kullanımı, burada Allah’ın olaylardan bilgi edinmesini değil, okurun 6:6’daki tarihî örüntüyü tanımasını çağrıştırır. Bu yazılı ses gözlemi özel bir okuyuş biçimi ileri sürmez. İki nitelemenin benzer sonlanışı eşleşir; ilk niteleme bir çift açar, {ar:بَصِيرًا, tr:baṣīran, gloss:gören} ise ayetin son sıfatı ve son kelimesi olarak hem çifti hem yeterlilik bildirimini kapatır.

6:6’da bir topluluğun yeryüzünde güçlendirilmesi, bol yağmur ve altlarından akan ırmaklarla desteklenmesi, ardından günahları yüzünden yok edilip yerine başka kuşağın getirilmesi anlatılır ({ar:مَكَّنَّاهُمْ فِي الْأَرْضِ, tr:makkannāhum fī l-arḍ, gloss:onları yeryüzünde güçlendirmiştik}; {ar:فَأَهْلَكْنَاهُمْ بِذُنُوبِهِمْ, tr:fa-ahlaknāhum bi-dhunūbihim, gloss:günahları yüzünden onları yok ettik}). Bu sahne odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} ile {ar:خَبِيرًا, tr:khabīran, gloss:iç yüzünü bilen} birlikteliğini aydınlatır: dışarıdan görülen kudret ve bolluk topluluğun iç ahlaki hâlinden ayrıdır. Bu özel örnekte bolluk aldatıcı sayılmaz ve her güçlü topluluğun helak olacağı ileri sürülmez. 25:58’deki yakın kapanış, yeterlilik, kulların günahları ve derin bilgiyi aynı yapıda buluşturur ({ar:وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا, tr:wa-kafā bihi bi-dhunūbi ʿibādihi khabīran, gloss:kullarının günahlarını bilen olarak O yeter}); bu lafız yankısı odaktaki {ar:خَبِيرًا, tr:khabīran, gloss:iç yüzünü bilen} hükmünü tarihî örüntüyü tanıma imkânıyla ilişkilendirir.

{ar:بَصِير, tr:baṣīr, gloss:gören} olağan kullanımda gözle görmeyi ve görünür olanı algılamayı öne çıkarır; {ar:خَبِيرًا, tr:khabīran, gloss:iç yüzünü bilen} ile yan yana geldiğinde bu görme içe nüfuz eden ve doğrulanmış bir anlayış yankısı da kazanır. Böylece odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları}nın dışarıya yansıyan yanı ile iç niteliği iki ayrı bilgi kanalı gibi belirir. Burada tek tek gözlemlenmiş sahneler sunulmaz.

17:1’deki gören sıfatının tekrarı, odaktaki görme hükmünü gece yolculuğunda işaretlerin gösterildiği daha geniş sahneye taşır ({ar:الْبَصِيرُ, tr:al-baṣīr, gloss:gören}; {ar:لِنُرِيَهُ آيَاتِنَا, tr:linuriyahu āyātinā, gloss:ayetlerimizi ona göstermemiz}). Sıfatın kalıplaşmış bir ifade olması da mümkündür; bu özel yankı açılıştaki tekil kulu odaktaki çoğul kullarla özdeşleştirmez ve görmeyi vahiy diye yeniden tanımlamaz. Böylece görme yalnızca cezalandırıcı bir teftiş gibi daralmaz; kulların günahlarına ilişkin doğrudan hüküm işaretlerin gösterildiği daha geniş sahnede duyulur.

27:52’de haksızlıkları yüzünden boş kalan evler, bilen bir topluluk için işaret sayılır ({ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةً بِمَا ظَلَمُوا, tr:fa-tilka buyūtuhum khāwiyatan bimā ẓalamū, gloss:haksızlıkları yüzünden boş kalan evleri}; {ar:إِنَّ فِي ذَٰلِكَ لَآيَةً لِقَوْمٍ يَعْلَمُونَ, tr:inna fī dhālika la-āyatan li-qawmin yaʿlamūn, gloss:bilen bir topluluk için bunda ibret vardır}). Yıkım sonrasındaki bu görünür boşluk, insan okurun tarihî sonucu okunabilir bir işaret olarak kavramasına izin verir. 17:16’daki kent yıkımından ayrı bu sahne, odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} sonrasında kalabilen izi başka bir açıdan görünür kılar ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören} kapanışına tarihî sonuçları okuma imkânı ekler. Bu bağlantı 27:52’deki özel sahneyle sınırlıdır; her günahın görünür olduğunu ya da her harabenin tek başına suç kanıtı sayılacağını ileri sürmez.

Bu bilgi ve görme çizgisinin yanında 17:18’de hemen istenen dünya hayatına, 17:19’da sonraki hayata yönelen çaba ayrılır ({ar:الْعَاجِلَةَ, tr:al-ʿājilah, gloss:hemen istenen dünya}; {ar:الْآخِرَةَ, tr:al-ākhirah, gloss:sonraki hayat}). 17:20’de iki gruba da uzatılan bağışın kaynağı Rabbin armağanıdır ve bu armağan engellenmiş değildir ({ar:نُمِدُّ, tr:numiddu, gloss:uzatıp veririz}; {ar:عَطَاءِ رَبِّكَ, tr:ʿaṭāʾi rabbika, gloss:Rabbinin bağışı}; {ar:وَمَا كَانَ عَطَاءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışı engellenmiş değildir}). Bu ortak sunuş, odağın {ar:بِرَبِّكَ, tr:bi-rabbika, gloss:senin Rabbin} adıyla duyulan yetiştirip geliştirme yankısını yeniden taşır: iki grup da engellenmemiş armağan alır. {ar:أَهْلَكْنَا, tr:ahlaknā, gloss:yok ettik} yıkımı bu bağıştan ayrı kalır; bu bağlantı daha önce yok edilen kuşakların nedenini açıklamaz ya da hepsinin aynı payı aldığını ileri sürmez. Böylece helak genel bir rızık yoksunluğuna indirgenmeden iki gruba da verilen armağan görünür olur.

Yeterlilik tanıklık yönünde de yankılanabilir. 17:96’da “Allah şahit olarak yeter” denerek tanık açıkça adlandırılır ({ar:كَفَىٰ بِاللَّهِ شَهِيدًا, tr:kafā bi-llāhi shahīdan, gloss:Allah şahit olarak yeter}); bu kullanım odaktaki {ar:كَفَىٰ, tr:kafā, gloss:yeter} hükmüne yargı için yeterli tanıklık yankısı ekleyebilir. Odak âyette şahit sözü yer almaz ve bağlamlar aynı değildir; bu bağlantı lafız ve bağlamın sınırlı paralelliğidir. 17:30’da aynı bilen-gören kapanışı rızkı genişletme ifadesinin yanında yer alır ({ar:يَبْسُطُ الرِّزْقَ, tr:yabsuṭu r-rizq, gloss:rızkı genişletir}; {ar:خَبِيرًا بَصِيرًا, tr:khabīran baṣīran, gloss:iç yüzünü bilen ve gören}). Böylece bu bilgi yalnız cezalandırma sahnesinde kalmaz; tanıklık yankısı da Rabbin bilen-gören niteliğiyle birlikte duyulur.

25:58’in yakın kuruluşu {ar:كَفَىٰ, tr:kafā, gloss:yeter} fiilini kulların günahları ve derin bilgiyle yeniden buluşturur ({ar:وَكَفَىٰ بِهِۦ بِذُنُوبِ عِبَادِهِۦ خَبِيرًا, tr:wa-kafā bihi bi-dhunūbi ʿibādihi khabīran, gloss:kullarının günahlarını bilen olarak O yeter}). Bu benzer yapı, odaktaki {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} çoğul alanını adı geçen kulların günahlarının yeterli bilginin dışında kalmadığı yönünde keşifsel bir erişim yankısına bağlar. Bu yankı keşifseldir; sözlük dalının buradaki biçime geçişi kesinleşmediğinden odak “kuşatır” diye çevrilmez ve evrensel niceleyici ya da mümkün bütün fiillerin sayımı eklenmez. Olağan yeterlilik anlamı yerinde kalır.

Uzak bir sözlük dalında {ar:كَفَىٰ, tr:kafā, gloss:yeter} yuvarlak ya da çanak biçimli, içindekini taşıyan bir araç bölümünü de akla getirebilir. Bu imge içinde {ar:خَبِيرًا, tr:khabīran, gloss:iç yüzünü bilen} önce iç niteliği, ardından {ar:بَصِيرًا, tr:baṣīran, gloss:gören} dışarıdan algılananı belirler; {ar:بِذُنُوبِ عِبَادِهِۦ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları} ise kabın değil, bilginin ve görmenin konusu olan alanı adlandırır. Böylece yeterlilik, adı geçen kulların günahları için artakalan bırakmayan tek bir kanıt alanı gibi düşünülebilir. Bu, gerçek bir kap betimi değil, belirlenmiş hesabı iç bilgi ve dış görmeyle aynı kapanışta buluşturan bir imgedir; evrensel önerme kurmaz.

</source_prose>
