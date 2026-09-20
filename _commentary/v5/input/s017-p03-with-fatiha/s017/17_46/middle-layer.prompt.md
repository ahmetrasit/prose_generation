# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:46**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.middle.claims.json`

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
- Refer to source paragraphs as `17:46 ¶N`.

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

`(17:46 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:46",
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
        "citation": "(17:46 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_46/17_46.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_46/17_46.middle.claims.json \
  --ayah-ref 17:46
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_46/17_46.prose.editorial.tr.md`

<source_prose>
## İki Alıcı

Ayetin başındaki {ar:وَ, tr:wa, gloss:ve}, önceki akışa eklenerek kalp ve kulak engellerine geçiş sağlar. Bu, sonraki fiile tutunan bir bağlaçtır; kendi başına kök anlamlı bir sözcük gibi önceki sözün ne olduğunu belirlemez. Ardından gelen {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik}, var olan alıcıları tamamlanmış bir eylemle başka bir duruma sokar. Aynı fiil hem kalplerin üzerindeki örtüye hem kulakların içindeki ağırlığa uzanır: tek yerleştirme, iki ayrı alım yolunu engeller; burada yoktan yaratma anlatılmaz.

{ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik} fiilinin bir durumu meydana getirme yönü, diriliş tartışmasındaki ayrı bir buyrukla ihtiyatlı bir yankı kurar. İnsanlara taş ya da demir olmalarını söyleyen {ar:كُونُوا۟, tr:kunu, gloss:olun} sözü (17:50), örtüleri de kişiyi hareket alanı daralmış, boyun eğdirilmiş bir hâle getirilmiş gibi duyurmaya izin verir. Bu uzak benzerlik, örtünün sözlük anlamını değiştirmeden yerleştirmenin sonuçlarını genişletir; iki fiil ayrı köklerdendir, örtüler boyun eğme demek olmaz ve (17:50) kendi bağlamındaki bağımsız buyruk olarak kalır.

Örtü ile ağırlığın yerleşimi aynı değildir: {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} {ar:عَلَىٰ قُلُوبِهِمْ, tr:ala qulubihim, gloss:kalplerinin üzerine} ile kalbin üstünde bir kaplamayı, {ar:فِيٓ ءَاذَانِهِمْ, tr:fi adhanihim, gloss:kulaklarının içinde} yer alan {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} ise işitme organının içindeki ağırlığı gösterir. Kalp ve örtünün çoğul biçimleri, iki kanalı da aynı grubun alıcıları olarak dağıtır; engel tek bir kişinin yalıtılmış hâline indirgenmez. Çoğulluk örtülerin sayısını, kişi başına örtü miktarını ya da kalp üstündeki katman sayısını vermez; örtünün maddesi de belirtilmemiştir. Tek fiilin yönettiği iki nesne böylece paralel kalır, etkileri ise biri iç kavrayışı, öteki işitmeyi sınırlandıracak biçimde ayrışır.

Kalbin üstüne gelen örtünün olağan işi kaplamak, gizlemek ve dış etkiden korumaktır. Burada {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler}, {ar:عَلَىٰ, tr:ala, gloss:üzerine} ilişkisiyle {ar:قُلُوبِهِمْ, tr:qulubihim, gloss:kalpleri} örter; hemen ardından gelen kavrayış tümcesi bu kaplamanın erişimi nerede kestiğini gösterir. Kalp önce bedensel organdır; {ar:يَفْقَهُوهُ, tr:yafqahuhu, gloss:onu kavramaları} ile anılan anlama, onu iç kavrayışın merkezi olarak da etkinleştirir. Dinleyip ardından inanmama ve tartışmanın birlikte görüldüğü karşılaşma (6:25), sözün kulağa ulaşmasıyla kalpte kavranıp benimsenmesi arasındaki ayrımı da açar. Böylece örtü imgesi, olağan kaplamayı korurken engelin bedenin üstünden mesaja erişime uzanan etkisini belirginleştirir.

Bu erişim bağımlı tümcede açıkça kavrama eylemidir: {ar:أَنْ يَفْقَهُوهُ, tr:an yafqahuhu, gloss:onu kavramaları}. {ar:أَنْ, tr:an, gloss:-mesini}, anlamayı örtüye bağlar ve bunun engelin amacı ya da sonucu olarak okunmasına izin verir; yerel yapı bu iki ilişkiyi tek seçeneğe indirmez. {ar:يَفْقَهُوهُ, tr:yafqahuhu, gloss:onu kavramaları}, nasb hâlindeki muzari fiil ve I. bâbın çekimli biçimi olarak burada bir şeyi anlayıp bilme eylemini adlandırır; bu biçim gözlemi bu tümceyle sınırlıdır. Fiildeki nesne zamiri açıktır, fakat “onu”nun yerel biçimden hangi söze döndüğü kesinleşmez. Aynı ayetteki {ar:ٱلْقُرْءَانِ, tr:al-qur'ani, gloss:Kur'an}, iletilen sözün anlaşılacağı alanı açar; dolayısıyla engel yalnız sesi duymaya değil, anlamı kavramaya ilişkindir.

Bu kavrayış güçlüğü sessiz bir dünyadan doğmaz. Yaratılmışların tamamının hamd ile Allah'ı tesbih ettiği ve hiçbir şeyin O'nu övgüyle anmaktan ayrı kalmadığı geniş sahnede (17:44), {ar:تَسْبِيحَهُمْ, tr:tasbihahum, gloss:onların tesbihi} övgünün yaygınlığını, {ar:لَا تَفْقَهُونَ, tr:la tafqahuna, gloss:kavrayamıyorsunuz} ise aynı f-q-h sözcük ailesinden kavrayamama durumunu taşır. Bu sahnede (17:44) hitap edilen “siz” yaratılmışların tesbihini kavrayamaz; odaktaki {ar:يَفْقَهُوهُ, tr:yafqahuhu, gloss:onu kavramaları} ise üçüncü çoğul öznenin açık nesne zamiriyle kurulan kavrama eylemidir. Zamirin gönderimi yerel biçimden kesinleşmez; Kur'an'ın anılması iletilen söz bağlamını verir. Özne ve nesne biçimleri farklıdır; bu yakınlık aynı dinleyicileri ya da aynı içeriği göstermez, kavrayamama imgesini sessizlikten anlamlı sözün bolluğuna genişletir.

Bir önceki ayetin önündeki {ar:حِجَابًا مَّسْتُورًا, tr:hijaban masturan, gloss:gizli bir perde} dışarıda, Elçi ile ahirete inanmayanlar arasındaki karşılaşmayı örter (17:45); sıfat perdenin gizli oluşunu belirtir. Odakta {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} {ar:عَلَىٰ قُلُوبِهِمْ, tr:ala qulubihim, gloss:kalplerinin üzerine} kalbin alımını, {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} kulağın alımını sınırlar; engel böylece kişiler arasındaki temastan iç kavrayışa ve işitmeye, {ar:يَفْقَهُوهُ, tr:yafqahuhu, gloss:onu kavramaları} ile anılan mesaja erişime taşınır. Ardından aynı kişilerin Elçi'yi dinlediği bildirilir (17:47): {ar:يَسْتَمِعُونَ إِلَيْكَ, tr:yastami'una ilayka, gloss:seni dinlerler} sözü, hiç ses ulaşmadığı yorumunu sınırlar. Bu üç imgeyi ayrı gerçek aracılar ya da tek bir fiziksel neden zinciri saymak yerine, dış temasın, iç kavrayışın ve işitmenin farklı sınırlarını paralel biçimde görünür kılan resimler olarak okumak da mümkündür.

Örtülerin {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} gizleyen ve koruyan yönü, başka çağrı sahnelerinde mesajdan yalıtılma biçimini kazanır. Hatırlatmalardan yüz çevirmenin ardından kalp örtüsüyle {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} kulak ağırlığının anılması (18:57), çağrılanların örtüler ve aralarındaki perdeyle uzaklıklarını dile getirmesi (41:5) ve tekrarlanan çağrılara karşı parmaklarını kulaklarına koyup giysilerine bürünmeleri (71:7), kaplama imgesinin hem gizleme hem dış temastan korunma tarafını somutlaştırır. Bu temas, anlamanın dışarıda kalıp iç merkezde erişilmeden durmasını düşündürür; odaktaki sözcük korumayı amaçlayan bir eylem değil, örtü adıdır. Odak engelleri Allah'ın yerleştirdiğini ve kavrayışı kestiğini söyler. Bu karşılaştırmalar, ilahî yerleştirmenin önceki reddin sonucu olup olmadığını ya da toplulukların özdeşliğini seçmeden, örtü imgesini mesajdan yalıtılma yönünde genişletir.

Örtü kavrayışı sınırlandırırken, {ar:ءَاذَانِهِمْ, tr:adhanihim, gloss:kulakları} sözü öncelikle işitme organını, aracı bir kişiyi değil; {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} ise kulağın içinde işitmeyi ağırlaştırıp ses alımını aksatabilen bir durumu, hatta sözlükteki işitme bozukluğu anlamını gösterir; burada belirli bir tıbbi tanı konmaz. Dinleyip inanmayan ve tartışanların bulunduğu sahne (6:25), okunan ayetler yanında kulak ağırlığıyla kibirli yüz çevirmenin belirdiği sahne (31:7) ve yinelenen çağrıya parmakları kulaklara tıkama hareketinin eşlik ettiği sahne (71:7), ağırlığı mesaj karşısında aksayan alımlama olarak somutlaştırır. Taşıyıcı üstündeki belirgin yük anlamı da aynı sözcük ailesinde yankılanır (31:7): işitme yalnızca engellenmez, mecazi olarak bir yüke dönüşür.

Karşılaştırmalı sahneler, odaktaki {ar:ءَاذَانِهِمْ, tr:adhanihim, gloss:kulakları} sözüyle kurulan işitme yolunun başka bağlamlarda da güvene ve korunmaya açılabildiğini gösterir: elçinin iyilik ve inançla ilişkilendirilen bir “kulak” diye nitelenmesi (9:61), dinlemenin alımlayıcı yönünü; mağara ehlinin kulaklarının koruyucu biçimde kapatılması (18:11) ise başka bir bağlamdaki korumayı görünür kılar. Odaktaki {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} bu olasılıklardan birine indirgenmez; kulağa yerleşip işitmeyi ağırlaştıran, sesi almayı aksatabilen bir engel olarak kalır. Böylece karşıt kullanımlar onun amacını odaktaki kavrayış ve ardından gelen kaçınma tepkisiyle sınırlar.

Kulakları adlandıran {ar:ءَاذَانِهِمْ, tr:adhanihim, gloss:kulakları} sözü organ anlamını korurken dikkatle dinleme yönünü de açar. Burada bağımsız tetikleyiciler {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} ile {ar:ٱلْقُرْءَانِ, tr:al-qur'ani, gloss:Kur'an}dır: ağırlık alımı zorlaştırır, Kur'an ise dinlenen sözü belirginleştirir. Dinlemenin kimi kullanımlarda duyulanı benimsemeye uzanması, Rabbin anılmasının ardından gelen {ar:وَلَّوْا۟, tr:wallaw, gloss:yüz çevirdiler} tepkisiyle kabulün de aksayabileceğini düşündürür; bu, her dinlemeyi itaatle eşitlemez. Kulak sözcüğünün aynı ailesindeki bilme ve başkasına bildirme yönü de {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} ile Kur'an'da anılan sözün ayrı tetikleyicileriyle iletişim yankısı kurar. Bu yankı işitme organını duyuru ya da izin anlamına dönüştürmez; iki kanallı sahnede kalp iç kavrayışı, kulak ise sesi almayı ve olası kabulü taşır.

Odaktaki {ar:ءَاذَانِهِمْ, tr:adhanihim, gloss:kulakları} üzerindeki {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} sürerken bile sesle karşılaşmanın devamı, ardından gelen toplumsal sahnede belirginleşir. Dinleyenler özel konuşma hâlindeyken (17:47), “büyülenmiş bir adamdan başkasına uymuyorsunuz” suçlamasıyla sözü yeniden adlandırırlar: {ar:وَإِذْ هُمْ نَجْوَىٰ, tr:wa-idh hum najwa, gloss:özel konuşma hâlindeyken} ve {ar:مَّسْحُورًا, tr:mashuran, gloss:büyülenmiş}. Sonraki ayette Elçi için benzetmeler kurdukları, ardından sapıp yol bulamadıkları anlatılır (17:48): {ar:ضَرَبُوا۟ لَكَ ٱلْأَمْثَالَ, tr:darabu laka al-amthala, gloss:sana benzetmeler kurdular} ve {ar:فَضَلُّوا۟ فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-dallu fa-la yastati'una sabilan, gloss:sapıp yol bulamadılar}. Odakta {ar:يَفْقَهُوهُ, tr:yafqahuhu, gloss:onu kavramaları} ile belirtilen kavrayıştan toplumsal etiketlemeye, ardından yön bulamamaya uzanan akışta özel konuşmanın suçlamayı doğurduğu ya da suçlamanın sonraki yön kaybına yol açtığı ileri sürülmez.

Bu kişilerden daha ileride Rabbin çağırdığı gün insanların O'nu hamd ile anarak karşılık vermesi anlatılır (17:52): {ar:يَدْعُوكُمْ, tr:yad'ukum, gloss:sizi çağırdığı} ve {ar:تَسْتَجِيبُونَ بِحَمْدِهِ, tr:tastajibuna bi-hamdihi, gloss:O'nu överek karşılık verirsiniz}. Bu gelecek cevap, odaktaki {ar:ءَاذَانِهِمْ, tr:adhanihim, gloss:kulakları} ve {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} ile kurulan işitme engelinin, {ar:نُفُورًا, tr:nufuran, gloss:ürkerek uzaklaşma} ile görünen geri çekiliş gibi, her çağrıya ve zamana genellenemeyeceğini gösterir. Başka zamandaki olumlu karşılık odaktaki dinleyicilerin şimdi aynı biçimde yanıt vereceğini, aynı ahlaki ilişkiyi paylaşacağını ya da gönüllü olarak değişeceğini belirlemez; odaktaki an için işitme, kavrayış ve kabul ayrı kalır.

## Tek Başına Anılma

Kalp ve kulaktaki engellerden sonra {ar:وَإِذَا, tr:wa-idha, gloss:ve ne zaman} ile cümle alıcıların durumundan davranışa döner. {ar:إِذَا, tr:idha, gloss:ne zaman} koşulu, {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} eyleminin {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini} {ar:فِي ٱلْقُرْءَانِ, tr:fi al-qur'ani, gloss:Kur'an'da} {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} anılmasını içerir; ardından {ar:وَلَّوْا۟, tr:wallaw, gloss:yüz çevirdiler} bu koşulun cevabı olur. “Ne zaman … olursa” yapısı bu karşılaşmanın yeniden yaşanabilmesine elverişlidir; dilbilgisi bir sıklık sayısı vermez. Koşul, genel olarak Kur'an sesini duymaktan ibaret değildir: Rabbin Kur'an'da tek başına anılmasına kadar daralır.

Bu koşulun eylemini {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} verir: tekil ikinci kişiye yönelerek sözle anmayı o muhataba yükler, fakat muhatabın kimliğini çekim biçimi tek başına açıklamaz. Önce birinci çoğul ilahî eylem {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik}, ardından tekil muhatabın sözü gelir; kişi kayması yerleştirilen engellerden tepkinin koşuluna geçişi duyurur. Anma kulluk amacı taşıyabilir; belirli bir dua ya da ritüel adı verilmediği için bu yönelim, hemen ardından gelen Rab nesnesiyle somutlaşır.

Anmanın nesnesi {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini}dir; iyelik eki Rab ile tekil muhatap arasındaki bağı kurar. Rab sözü sahip olma ve yönetmenin yanı sıra gözetip beslemeyi de taşır, böylece bu ilişki yalnızca bir adın söylenmesine indirgenmez. {ar:فِي ٱلْقُرْءَانِ, tr:fi al-qur'ani, gloss:Kur'an'da} içindeki edat anmayı tilavet edilen Kur'an alanına yerleştirir; belirli artikel bu alanı yerel olarak tanımlar ve bu belirginlik başka ayetlerden kurulacak bir zincire bağlı değildir. Rab, Kur'an alanı ve {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} kaydı birlikte tepkinin önündedir; tetikleyici genel bir ses değil, sınırları belirtilmiş bir anmadır. Kur'an adının okuma ve tilavet, hatta toplama yönündeki kök yankısı {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} ve yalnızlık ifadesiyle temas edebilir; çağrışım hafif ve belirsiz kalsa da okunan alan ile sözlü anma arasında bir yankı kurar, Kur'an adının olağan anlamı da yerinde kalır.

{ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına}, hâl konumunda {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini} ile ilişkilidir: koşul Rab anılırken onun yalnız oluşunu da içerir. “Tek başına” olağan anlamını korurken, Rab adıyla kurduğu bağ ortaksız ilahî birliğin eşsizliğini de duyurur; bu katman koşuldaki anmanın neden belirleyici olduğunu derinleştirir ve yerel dilbilgisel ilişkiye dayanır, dışarıdan alınan bir formül kıyasına değil. Allah'ın tek başına anılmasıyla kalbin daralması, başkaları anıldığında sevinç belirmesi karşıtlığı (39:45), bu münhasırlığın duygusal karşılığını başka bir sahnede görünür kılar; odaktaki kişileri ya da nedenleri aynılaştırmaz.

Kulaktaki {ar:وَقْرًا, tr:waqran, gloss:işitme ağırlığı} anlamı yerinde kalırken, Rabbin {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini} {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} anılışına aynı sözcük ailesinin ağırbaşlılık ve vakur duruş bildiren ayrı kolu ihtiyatlı bir karşı ton ekler. Ardından gelen {ar:وَلَّوْا۟, tr:wallaw, gloss:yüz çevirdiler}, böyle bir hitap karşısında ters bir ton yaratır: işitme ağırlığının maddi imgesi sürer, vakur söyleyişin karşısına yüz çevirme çıkar. Bu karşıtlık dinleyenlere ağırbaşlılık erdemi yüklemeden tepkideki sertliği duyurur.

Rabbin tek başına anılışı, {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini} ve {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} ile kurulan koşul, çağrılan varlıkların kimin yanında durduğuna ilişkin daha geniş ilişkiyi de düşündürür. O'nun yanında başka ilahlar bulunsaydı, onlar da Arş sahibine bir yol arardı (17:42); insanların çağırdıkları varlıkların kendileri de Rablerine yakınlaşmanın vesilesini arar (17:57). Çağrılanların zararı giderme ya da başka bir hâle çevirme gücüne sahip olmadığını söyleyen ayet (17:56), bu arayışın bağımlı oluşunu tamamlar. Böylece odaktaki geri çekiliş, himaye ve erişim ağına yönelmiş bir tepki olarak okunabilir: bu ağdaki varlıklar bağımsız son duraklar değil, kendileri de arayıcılardır. Bu olasılık her tarihsel aracının rolünü ya da her dinleyicinin güdüsünü belirlemez; yalnızca sayısal çokluğa karşı çıkma açıklaması da daha dar bir seçenek olarak kalır.

Fatiha bu münhasırlık ilişkisini olumlu bir sesle açar. Allah'ın “âlemlerin Rabbi” diye anılması (1:2), odaktaki {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbini} ve {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} ile kurulan ilişkiyi Rab unvanında karşılar; ardından çoğul konuşan ses {ar:إِيَّاكَ نَعْبُدُ, tr:iyyaka na'budu, gloss:yalnız Sana kulluk ederiz} ve {ar:وَإِيَّاكَ نَسْتَعِينُ, tr:wa-iyyaka nasta'in, gloss:yalnız Senden yardım isteriz} der (1:5). Böylece Rabbin yalnız anıldığı koşula gelen geri çekilmenin yanında, aynı münhasırlık ibadet ve yardım talebiyle olumlu biçimde dile gelir. Bu karşılaştırma 17:46'nın Fatiha'dan alıntı yaptığını ya da iki yerde aynı kişilerin konuştuğunu ileri sürmez; yerel koşul kendi başına anlaşılır.

Odaktaki sözlü anma ile hatırlama amacı arasındaki ayrım, aynı sözcük ailesinin başka bir Kur'an sunumundaki kullanımında belirir. {ar:ٱلْقُرْءَانِ, tr:al-qur'ani, gloss:Kur'an}'ın çeşitli biçimlerde sunulmasının amacı “hatırlasınlar” diye anlatılırken (17:41), {ar:صَرَّفْنَا, tr:sarrafna, gloss:çeşit çeşit sunduk} sunumları, {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakaru, gloss:hatırlasınlar diye} ise zihinsel hatırlama amacını bildirir. {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} aynı dh-k-r ailesindendir ama Rabbin sözle anılmasıdır; bu biçim kendi başına hatırlamak demek değildir. Aynı ayette (17:41) değişen sunumların yanında odaktakiyle aynı {ar:نُفُورًا, tr:nufuran, gloss:ürkerek uzaklaşma} sözü de artar. Bu yankı tekil tepkiyi değişen sunumlarla tekrarlanan karşılaşmaların parçası olarak duyurur; aynı dinleyicileri ya da sunumun kaçışı doğurduğunu belirlemeden, daha önceden var olabilecek bir yönelişin açığa çıkması olasılığını korur.

Başka bir karşılaşmada görünen işaret insanlar için sınama olur ve uyarıp korkutmaya rağmen büyük taşkınlık artar (17:60): {ar:فِتْنَةً, tr:fitnatan, gloss:sınama}, {ar:نُخَوِّفُهُمْ, tr:nukhawwifuhum, gloss:onları uyarıp korkuttuğumuz}, {ar:يَزِيدُهُمْ, tr:yaziduhum, gloss:onları artırır}, {ar:طُغْيَانًا كَبِيرًا, tr:tughyanan kabiran, gloss:büyük bir taşkınlık}. Önceki sahnedeki (17:41) artan kaçışla burada artış dili buluşur, ancak taşkınlık ile uzaklaşma ayrı tepkilerdir. Aynı ayette Rabbin insanları kuşattığı da söylenir: {ar:رَبَّكَ أَحَاطَ بِٱلنَّاسِ, tr:rabbaka ahata bi-n-nasi, gloss:Rabbin insanları kuşatmıştır}. Odaktaki sırtlarını dönme hareketi gerçek mesafe yaratır, ama kuşatılan ilişkiden kaçış olmaz; bu karşılaştırma ne fiziksel olarak durdurulduklarını ne de iki ayetin aynı anı anlattığını söyler.

## Yüz Çevirip Uzaklaşmak

Anma koşulunun ardından {ar:وَلَّوْا۟, tr:wallaw, gloss:yüz çevirdiler}, yüzlerini çevirip ilişkiden uzaklaşmayı koşulun cevabı yapar. Kalp örtüsü ve kulak ağırlığından sonra bu tepkinin bedende görünmesi iki hareketi aynı ayet akışında birleştirir; sıralanışları iç engellerin kaçışa mekanik olarak neden olduğunu göstermez. Bu fiilin sözcük ailesinde kesintisiz yakınlığı anlatan ayrı bir kol da bulunur. {ar:أَدْبَٰرِهِمْ, tr:adbarihim, gloss:sırtları} ve {ar:نُفُورًا, tr:nufuran, gloss:ürkerek uzaklaşma} ile gelen açık geri çekilme, yakınlıkla mesafe arasında ihtiyatlı bir karşıtlık kurar; sahne önceden yaşanmış bir yakınlığı varsaymaz.

İçteki alım ile dıştaki dönüş, kalp adının açtığı kök yankısında buluşur. {ar:قُلُوبِهِمْ, tr:qulubihim, gloss:kalpleri} bedensel kalplerdir; q-l-b ailesinde bir şeyi bir yüzünden ötekine çevirme, tersine döndürme ve kişiyi yöneldiği taraftan saptırma anlamları da vardır. Bu yankıyı {ar:وَحْدَهُۥ, tr:wahdahu, gloss:tek başına} koşulu, ayrı dönüş fiili {ar:وَلَّوْا۟, tr:wallaw, gloss:yüz çevirdiler} ve sırt imgesi birlikte harekete geçirir. Allah tek başına anıldığında kalplerin daralması da bu iç tepkiyi başka bir bağlamda görünür kılar (39:45). İki sahneyi aynı kişilere ya da aynı nedene bağlamadan, bu okuma psikolojik bir tanıya dönüşmeden kalbin yön değiştirme yankısını içteki geri tepkiyle bedenin dışa dönüşü arasında duyurur; kalp adı yine organ olarak kalır.

Dışa dönüşün yüzeyi {ar:أَدْبَٰرِهِمْ, tr:adbarihim, gloss:sırtları} ile somutlaşır: sözcük bedenin arka tarafını adlandırır ve çoğul iyelikle bu sırtları aynı gruba bağlar. İlk {ar:عَلَىٰ, tr:ala, gloss:üzerine} kalplerin üzerindeki örtüyü, son {ar:عَلَىٰٓ, tr:ala, gloss:üzerine} sırtlara yönelen hareketi çerçeveler; içteki kaplamadan dışa dönmüş bedene uzanan çizgi bu tekrarın ayet içindeki katkısıdır. Okunan ayetlerin yanında kibirli dönüşün belirdiği sahne (31:7) ve tek başına anılınca kalplerin çekildiği sahne (39:45), sırtın soyut bir yön tarifinden çok alımlamanın görünür bedensel ucu oluşunu aydınlatır; bu paralellik katılımcıları özdeşleştirmez. Son {ar:نُفُورًا, tr:nufuran, gloss:ürkerek uzaklaşma}, yönü değil ürküp mesafe koyma tarzını belirtir; kavrayış fiilinden ürküntüye geçiş odaktaki yerel sırada gerçekleşir, askerî seferberlik ya da savaş hareketi olarak okunmaz. Böylece anmadan yüz çevirmeye, oradan sırt göstermeye ve kaçınmaya uzanan hareket ayetin kendi sahnesinde tamamlanır; sözcüğün ayet sonundaki işitilen izi konumundan ve yerel anlamından gelir, kullanım sıklığına ilişkin bir iddia taşımaz.

</source_prose>
