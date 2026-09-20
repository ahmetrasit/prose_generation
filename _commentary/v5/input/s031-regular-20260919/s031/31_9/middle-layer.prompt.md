# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:9**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.middle.claims.json`

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
- Refer to source paragraphs as `31:9 ¶N`.

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

`(31:9 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:9",
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
        "citation": "(31:9 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_9/31_9.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_9/31_9.middle.claims.json \
  --ayah-ref 31:9
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_9/31_9.prose.editorial.tr.md`

<source_prose>
## Bahçede kalış

Bu âyet, Allah’ın iman edip iyi işler yapanlara nimet bahçelerini vaat ettiğini ve onların orada kalacağını bildirir. (31:8)’de açılan bahçe sahnesi sürerken {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} akuzatifte duran etkin ortaç biçimiyle sakinleri yeni bir olaya girenler olarak değil, kalıcı hâlde bulunanlar olarak gösterir. Ardından gelen {ar:فِيهَا, tr:fīhā, gloss:onların içinde} ifadesinin dişil tekil -hā eki, bahçe adını yinelemeden o bahçelere döner; en yakın karşılık burasıdır, ancak zamir daha geniş nimet hâline de uzanabilir. Böylece süre, soyut bir zaman ölçüsü olmaktan çıkıp içinde yaşanan ikamete bağlanır. {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} ile {ar:فِيهَا, tr:fīhā, gloss:onların içinde} kelimelerindeki uzun ī sesleri bu yer bağını işitilir kılar. Sözlükte âhiret yurdunda kesintisiz kalış için verilen örnek de bu yakın bahçe ve ses birlikteliğinde yankılanır.

Bu yerleşik ikametin niteliğini (31:8)’deki iman, salih işler ve nimet bahçeleri birlikte boyar. {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} olağan iman anlamını korurken güven ve emniyet yönü de açılır; salih işler ve bahçe vaadiyle buluşunca güven, kalıcı bir sonuca yönelen esenlik gibi duyulur. Güvenin bu bağlamda esenlik gibi duyulması, kelimeyi tek başına fiziksel koruma bildiren bir anlama dönüştürmez. {ar:جَنَّٰتُ ٱلنَّعِيمِ, tr:jannāt al-naʿīm, gloss:nimet bahçeleri} gerçek bahçeleri adlandırır; örtme ve gizleme kullanımı, {ar:فِيهَا, tr:fīhā, gloss:onların içinde} ile kurulan iç mekâna ve {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} ile süren kalışa bir çevre verir. Aynı kelimenin ağaçlarla örtülü bahçe kullanımı bu çevreyi yaşanan bir yere dönüştürür. Örtü ve içeride kalışın birleşmesi bahçeyi sığınak gibi duyurur; bu benzetim belirli bir tehdidi ya da gerçek bir kalkanı varsaymaz, bitkiler de metinde ayrıca sayılmaz. Nimet ve hoşluk anlamındaki naʿīm’in esenlik ve ihsan yönü, bu kalışı uygun ve huzurlu bir konaklama gibi niteler; yeni duyusal ayrıntılar eklemez.

## Sözün kaynağı ve doğruluğu

Bahçede sürüp giden hâlin ardından {ar:وَعْدَ, tr:waʿda, gloss:vaat} bu kalışı güvenceye alan sözü getirir. Buradaki akuzatif maṣdar, yani fiilden türemiş ad, hem söz verme eylemini hem vaat edilen içeriği adlandırır. Waʿda’nın anlam alanı gelecekte iyi ya da kötü bir şeyin sözle bildirilmesini kapsar; olumlu yönü kelime tek başına seçmez. (31:8)’deki nimet bahçeleri vaadin neyi içerdiğini açıklar; {ar:وَعْدَ ٱللَّهِ, tr:waʿda Allāhi, gloss:Allah’ın vaadi} tamlamasında genitif {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah’ın} ise sözün sahibini ve kaynağını gösterir. Böylece 31:9’un vaadi adsız bir gelecek beklentisi değil, bu bahçelerde kalışa ilişkin Allah’ın sözü olur.

Vaadin ardından gelen {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} ikinci maṣdar, doğruluk durumunu sözün yanına koyar. Kelimenin bir şeyi doğru diye belirleyip onaylama kullanımı da burada duyulur: ikamet yalnızca umut edilen değil, vaadin kendi söylenişinde doğrulanan sonuçtur. Hakk kelime ailesinin bağlayıcı gereklilik ya da birine düşen pay anlamı, sözün yerine getirilmesi gerektiği yönünde bir bağlılık tonu ekler; bu çağrışım yararlanıcının ödülü hak ettiğini veya belirli bir hukukî alacağının doğduğunu saptamaz. {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} sonundaki tenvin, {ar:وَهُوَ, tr:wa-huwa, gloss:ve O}ya geçerken doğrulama vuruşunu sesçe kapatır.

Bu ses kapanışının ardından {ar:وَ, tr:wa, gloss:ve} ya güvence cümlesini sürdürür ya da bir hâl ilişkisi kurar; her iki okumada da {ar:هُوَ, tr:huwa, gloss:O} ile ilahî nitelemelere geçilir. Yazıda bitişik duran wa-huwa, tek akışta işitilse de bağlaç ile bağımsız zamiri birleştirmez: huwa özne olarak kalır ve iki yüklemi kendisine bağlar. Buradaki {ar:فِيهَا, tr:fīhā, gloss:onların içinde} içindeki dişil tekil zamir bahçelere, huwa’daki eril tekil zamir ise {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah’ın} adına döner; bu ayrım son sıfatların kime ait olduğunu gösterir. Allah adının vaad ile doğruluk arasında, sonra da huwa’nın önünde yer alması, doğrulanmış sözü onu verenin kimliğine bağlar. Burada Allah, Yaratıcıya özgü özel addır. “Tapınılan varlık” yönündeki ayrı kullanım, vaadin sahibi oluşu ve ardından gelen kudret-hikmet nitelemeleriyle birleşince otoriteyi de duyurur; bu çağrışım özel adı genel bir tür adına dönüştürmez ve kelimeye korku ya da dehşet anlamı yüklemez.

Bu kaynak adı, okumanın başındaki (31:0) besmeleyle de aynı ilahî göndergeye yönelir: {ar:بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:bismi llāhi al-Raḥmāni al-Raḥīm, gloss:Rahmân ve Rahîm olan Allah’ın adıyla}. Besmeledeki {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:al-Raḥmān al-Raḥīm, gloss:Rahmân ve Rahîm} adları ile (31:8)’de hemen sunulan bahçeler, (31:9)’daki {ar:وَعْدَ ٱللَّهِ, tr:waʿda Allāhi, gloss:Allah’ın vaadi}ni rahmetle çerçevelenmiş bir güvence gibi duyurabilir; bu yakınlığın katkısı vaat ile bahçe ödülünü rahmet bağlamında yan yana getirmektir. Besmele sıfatları vaadin dilbilgisel niteleyicisi olmaz; rahmet ile bahçe ödülü arasındaki bağ burada bağlamsal bir çağrışım olarak kalır.

Vaadi verenin kimliği açık zamirden sonra iki yerleşik nitelemeyle tamamlanır: {ar:ٱلْعَزِيزُ, tr:al-ʿazīzu, gloss:yenilmez kudret sahibi} ilk, {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:hikmetle hükmeden} ikinci nominatif yüklemdir. Belirlilik takısı ve faʿīl biçimi ikisini de geçici bir olay değil, Allah’a ait övülen nitelikler olarak kurar. İlk sıradaki ʿazīz kudreti, yenilmezliği ve izzeti verir; vaadin yanında bu, sözün yerine gelmesini taşıyacak kapasiteyi duyurur. Kelime ailesindeki birine ya da şeye güç kazandıran geçişli kullanım bu kapasiteyi pekiştiren bir yankı verir; burada ʿazīz ayrı bir güçlendirme eylemini değil, yenilmez bir unvanı niteler. Ardından gelen ḥakīm bilgiyi ve usla doğru sonuca ulaşmayı, ayrıca düzeni sağlamlaştırıp kusursuz tamamlamayı taşır. Ḥakīm’in zarardan koruma ve bu koruma altında durumu düzeltme yönündeki ayrı kullanımı sağlam tertip fikrine koruyucu bir ton ekler; bu çağrışım burada bir hekim ya da onarım sahnesi kurmaz. Kudret önce imkânı, hikmet sonra doğru tertibi verir; bu sıra nitelikler arasında üstünlük kurmaz. İki adın uzun ī sesleri ve aynı nominatif u sonları da kapanışta dengeli bir ses çifti oluşturur. Böylece bahçede kalıcı kalış vaat edilen içerik, ḥaqqan onun doğruluğu, ʿazīz onu gerçekleştirme gücü, ḥakīm ise yerinde ve sağlam düzeni olarak birbirini tamamlar.

## Vaadin yeri ve bugünkü izi

Vaadin içeriği bahçede kalış olarak belirince, {ar:وَعْدَ, tr:waʿda, gloss:vaat} için başka ve sınırlı bir sözlük kullanımı da sözün ya da anlaşmanın gerçekleşeceği yeri düşündürür. Burada {ar:فِيهَا, tr:fīhā, gloss:onların içinde} bahçeyi varış yeri yapar. {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} kelimesinin başka ve sınırlı kullanımı, iki kemiğin birleştiği eklemdir; eklem parçaların uyumsuzluk ya da sızıntı olmadan buluşmasını, böylece vaat, alıcı ve varış yerinin uygun biçimde birleşmesini düşündürür. {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} için sert ve sıkı zemin anlamı da taş olmayı gerektirmeden varış yerinin tutunmasını duyurur; {ar:ٱلْعَزِيزُ, tr:al-ʿazīzu, gloss:yenilmez kudret sahibi}nin tutan gücü ve {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:hikmetle hükmeden}in düzeni bu sağlamlık benzetimini taşır. Uygun kap ya da eklem ilişkisi anlamındaki başka kullanım içerik ile yerin uyuşmasını tamamlar. Böylece eklem parçaların sızıntısız birleşmesine, zemin varış yerinin sağlamlığına, kap da uygunluğa katkı verir; bu imgeler vaadin gerçek çevirisine dönüşmez ve burada belirli bir gerçekleşme tarihi verilmez.

Vaadin yeri belirli olabilse de (31:34)’te saatin bilgisi Allah’ın yanında tutulur; insan yarın ne kazanacağını ve nerede öleceğini bilmez. Bu karşılaşma, waʿda için belirli bir vakit ya da yer taşıyabilen ayrı kullanımı açar: söz doğru kalırken vakti ve takvimi insana kapalı olabilir. {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} doğruluğu zaman açıklığına bağlamaz. (31:34)’ün vaadin tali ayrıntılarını sınırlıyor olma ihtimali açıktır; bu karşılaşma kesinliği takvim bilgisine dönüştürmez.

Takvimi bilinemeyen gelecek, vaadin bugünkü etkisini ortadan kaldırmaz. Waʿda’nın ayrı bir kullanımı mevcut belirtilerin gelecekteki durum hakkında beklenti doğurmasını anlatır; hemen ardından gelen {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} bu beklentiyi doğrulanmış bir işaret gibi duyurur. {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar}ın düşüncenin yerleştiği alanı ya da orada kalan düşünceyi anlatan ayrı kullanımları, işaretin zihinde yer tutması yönünü ekler. Bu iki yankı gelecek vaadini şimdi güvenilir bir beklenti gibi düşündürür; bağlantı bilişsel düzeyde kalır, fiziksel kehanet kurmaz ve khālidīna burada “zihin” ya da “kalp” diye çevrilmez.

Bu zihinde yer eden işaretten ayrı bir sözlük resmi, waʿda’yı doğal biçimde toplanmış suya ya da o suyun bulunduğu yere bağlar; daha dar kullanımda, su çekildikçe tükenmeyen bir kaynağı anlatır. Bu su imgesinde kaynağın tükenmemesi süre boyunca beslenmeyi, {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar}ın sürekliliği kalıcı ikameti, {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak}ın eklem ya da uygun kap çağrışımı ise parçaların sızıntısız uyuşmasını verir. Birlikte bu ayrıntılar vaadi bahçe ikametini süre boyunca besleyen bir kaynak gibi duyurur. Maddi imge sözü genişletir; vaadi doğrudan suya çevirmeden ikametin nasıl beslendiğini düşündürür.

## Kalıcılığın ilişkisi ve ölçüsü

Bu kalışın ilişki yönü (31:22)’deki teslimiyet sahnesiyle belirginleşir. {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} kelime ailesinin yalnız belirli kalıplarda görülen “bir şeye yönelip bağlanma, ayrılmadan kalma” kullanımı, Allah’a güvenle teslim olma ve O’na yönelme ile temas eder. (31:22)’de tutulan güvenilir kulp bağı sürdürür, tutuşun sağlamlığı kopmayı önler, son hedef ise yönelişe varış verir. Önceki bahçeyi gösteren {ar:فِيهَا, tr:fīhā, gloss:onların içinde} ve tek taraflı {ar:وَعْدَ, tr:waʿda, gloss:vaat} ile {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak}ın bağlayıcılık tonu bu bağlılığın hedefini belirginleştirir. Bu bağlantının katkısı kalıcılığı sonuca kadar sürdürülen ilişki gibi genişletmektir; (31:22)’deki tutuşun yalnız bugünkü imanı anlatıyor olması da mümkündür, bu olasılık ilişki yankısını sınırlar ve olağan “orada kalma” anlamının yerini almaz.

Bağın ilahî iradeyle ilişkisi (11:107)’de başka bir kalış üzerinden görünür. {ar:إِلَّا مَا شَاءَ رَبُّكَ, tr:illā mā shāʾa rabbuka, gloss:Rabbinin dilemesi dışında} kaydı o başka son ve bağlamda kalışın Rabbin dilemesine bağlı olduğunu gösterir. Bu karşılaştırmanın katkısı, {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} kalışını kendi kendine uzayan süre değil, ilahî iradeyle tutulan hâl gibi duyurmaktır; (11:107)’deki istisna kendi bağlamında kalır ve 31:9’un bahçe vaadine aktarılmaz.

Kalıcılığın yeri ile güvenlik arasındaki farkı (31:32)’deki fırtına sahnesi açar. Gölge gibi üzerlerine kapanan dalgalar insanları çalkantıyla tehdit eder; kurtarılmaları onları örtünün içinden ayırıp kuru, açık karaya çıkarır. Bu sahnenin katkısı tehlikeli kuşatma ile kurtuluşun açık yerini karşı karşıya getirmektir. Odaktaki {ar:خَٰلِدِينَ فِيهَا, tr:khālidīna fīhā, gloss:orada kalıcı olanlar} için “içinde kalma” bahçeye ait bir ikametken, fırtınanın içinde kalma tehlikeli kuşatmadır. Bu ters görüntü, içeride bulunmayı kendiliğinden güvenlik saymayan mekânsal bir benzetim sunar; bu bağlantı iki “içinde” kullanımını dilbilgisel olarak özdeşleştirmez.

Mekânın ardından sürenin sınırına bakınca (31:24)’te haz için ayrılan kısa dönem belirir; ardından zorunlu geçiş ve sıkıntının şiddetlenmesi gelir. Az miktar ve kısa aralık hazzın sınırlı payını, kaçınılmaz dönüş ve sonradan ağırlaşma ise bu sürenin sonunu görünür kılar; bunlar {ar:خَٰلِدِينَ, tr:khālidīna, gloss:kalıcı kalanlar} sözünün uzun ya da kesintisiz sürme anlamı karşısında zaman sınırını kurar. Böylece kalıcılık biten hazdan ayrılır; bu karşılaştırma iki ayrı zaman türünü tanımlamaz.

Bu kısa aralığın aksine, geceyle gündüzün birbirine girişi ve gökcisimlerinin belirlenmiş sona akışı (31:29)’da ölçülü çevrimleri kurar. {ar:يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ, tr:yūliju al-layla fī al-nahār, gloss:geceyi gündüzün içine sokar} karşılıklı devri, {ar:كُلٌّ يَجْرِىٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:kullun yajrī ilā ajalin musamman, gloss:her biri belirlenmiş bir sona kadar akar} ise akışı ve bitişi gösterir. Bu çevrimler khālidīna’daki sürekliliği sayılmış döngülerin ötesinde düşündürürken olağan uzun ya da kesintisiz kalma anlamını korur. Waʿda’nın bir kışla bir yazı kapsayan yılı adlandıran ayrı kullanımı bu çevrime uzaktan bir yıllık ölçü katar; 31:9 yılı adlandırmadığı için bu kullanım vaadin anlamına dönüşmez.

## Hikmetin görünür ölçekleri

Zamanın ölçülmesinden başka bir ölçeğe, yaratılışın ayakta duruşuna geçince (31:10)’da gökler gözle görülen sütunlar olmadan yaratılır; yeryüzüne sabit dağlar yerleştirilip sallanması önlenir. {ar:عَمَدٍۢ, tr:ʿamadin, gloss:sütunlar/dayanaklar} için “göremediğiniz sütunlar olmadan” sözü yalnız ihtiyatlı bir yük taşıma ya da dayanak benzetimine izin verir; {ar:رَوَٰسِىَ, tr:rawāsī, gloss:sabitlenmiş dağlar} sabitlemeyi, {ar:تَمِيدَ, tr:tamīda, gloss:sallanıp yalpalaması} engellenen yana salınımı verir. Bu ayrıntılar taşıma, sabitleme ve yalpalamayı önleme yönleriyle yapısal duruşu kurar. Odaktaki {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} için sıkı dokunmuş kumaş ve iyi kurulmuş söz kullanımları bu dayanaklarla buluşunca doğruluğu tutarlı, ayakta duran bütünlük gibi duyurur. Mansup doğrulama biçimi “dokunmuş” sıfatı değildir; kumaş ve söz imgesi biçimden değil, bu ayrı kullanımlardan gelir. {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:hikmetle hükmeden}in olağan hikmeti sağlam tertip ve bozulmaya direnç imgesiyle genişler; {ar:ٱلْعَزِيزُ, tr:al-ʿazīzu, gloss:yenilmez kudret sahibi}nin korunmuşluk ve yenilmezlik anlamı da dünyayı istikrarsızlığa karşı ayakta tutabilme kapasitesi olarak belirir. Bu sahne vaadin anlamına düzen benzetimi ekler; sallanması önlenen yeryüzüdür, vaat edilen cennet değil. Bu bağlantı vaadi güvenceye alan özel bir sebep-sonuç mekanizması kurmaz; (31:10)’un genel kudret gösterisi olarak okunması da mümkündür.

Yapı imgesinin yanına (31:12)’de başka bir hikmet ilişkisi gelir: Lokman’a {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:hikmet} verilir, ardından şükretmesi istenir ve şükredenin yararının kendisine döneceği söylenir. Odaktaki {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:hikmetle hükmeden}in doğruyu bilgi ve usla bulup sonuca ulaştırma yönü burada şükürle etik bir bağ kurar; bu sahnenin katkısı hikmeti şükürle ilişkilendirmektir, 31:9’daki vaade yeni bir emir yüklemek değil.

Hikmetin ulaştığı ölçü bu kez küçülür: (31:16)’da hardal tanesi ağırlığınca şey alt sınırı, hardal tanesi en küçük öğeyi verir. {ar:مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:miṯqāla ḥabbatin min ḫardalin, gloss:bir hardal tanesi ağırlığınca} ölçüsü, {ar:فِى صَخْرَةٍ, tr:fī ṣakhrah, gloss:bir kayanın içinde} saklı oluşuyla birleşince küçüklük, engel ve gizlilik görünmezliği artırır. Bilginin bu gizli içe ulaşması, odaktaki {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:hikmetle hükmeden} için doğru sonuca erişmeyi en küçük ölçekte duyurur. Bu görüntünün katkısı gizli en küçük ölçüye erişimi düşündürmektir; (31:16)’nın ahlaki gözetimi anlatıyor olması da açık kalır ve bu bağlantı vaat mekanizmasını açıklamaz.

Ölçü ters yönde büyüdüğünde (31:28) tek bir canı bütün yaratılış ve diriltmeyle karşılaştırır. {ar:ٱلْعَزِيزُ, tr:al-ʿazīzu, gloss:üstün gelen} için üstün gelip boyun eğdirme kullanımı kudreti, {ar:ٱلْحَكِيمُ, tr:al-ḥakīmu, gloss:düzeni sağlamlaştırıp tamamlayan} için yapıyı kusursuz tamamlama kullanımı ise bütün içindeki tertibi gösterir. Birlikte bu iki yön, tekten bütüne geçerken kudretin azalmadığını ve çoğunluk içinde tekil hayatın ayrıntısının da düzen içinde kaldığını düşündürür. Bu karşılaştırma dirilişin mümkünlüğünü düşündürür; (31:28)’in katkısı dirilişin imkânını göstermeyle sınırlı olabilir.

İnsan ve yaratılış ölçeğinden sözün kapsamına geçince (31:27)’de ağaçlar kalem, denizler ve ardından gelen denizler mürekkep olsa da Allah’ın sözleri tükenmez ve anlamını yitirmez. Bu yazı imgesi sözlerin büyüklüğünü sınar; odaktaki {ar:وَعْدَ, tr:waʿda, gloss:gerçekleşmesi beklenen söz} eksilmeyen söz kaynağının yanında duyulur. Bu yakınlık tek vaadin maddi işleyişini anlatmaz; katkısı vaadi tükenmeyen sözlerin kaynağıyla yan yana düşündürmektir. (31:27)’nin sonunda {ar:ٱللَّهُ عَزِيزٌ حَكِيمٌ, tr:Allāhu ʿazīzun ḥakīmun, gloss:Allah üstün ve hikmet sahibidir} kapanışı 31:9’daki kapanışı yineler; tükenmeyen sözlerin ardından kudretin düzenle birlikte anılması, odağın vaadini yeniden verenin kimliğine bağlar.

## Gerçeklik ve hesap

Vaadi verenin kimliği kadar doğruluğun kaynağı da (31:30)’da görünür: 31:9’daki {ar:حَقًّا, tr:ḥaqqan, gloss:gerçeğe uygun ve kesin olarak} sözün doğru olduğunu bildirirken, bu başka âyette Allah {ar:ٱلْحَقُّ, tr:al-ḥaqqu, gloss:gerçek olan}, başka çağrılanlar {ar:ٱلْبَٰطِلُ, tr:al-bāṭilu, gloss:gerçeklikten uzak olan} diye karşılaştırılır. Bu karşılaştırma vaadin doğruluğunu Allah’ın gerçek oluşuyla kaynağına bağlama imkânı sunar; iki kullanım aynı gramer anlamına gelmez ve 31:9’daki ifade doğru bir vaat olarak kalır.

(9:68)’de benzer vaat ve kalış ifadelerinin başka muhataplar için {ar:نَارَ جَهَنَّمَ, tr:nāra jahannama, gloss:cehennem ateşi} ile birlikte kullanılması, olumlu yönü bağlamın belirlediğini gösterir; {ar:خَٰلِدِينَ فِيهَا, tr:khālidīna fīhā, gloss:orada kalıcı olanlar} orada başka kişilere bağlanır. Bu karşılaştırmanın katkısı, vaat ve kalış kelimelerinin kendi başlarına sonucu seçmediğini göstermektir; 31:9’un olumlu içeriğini (31:8)’deki nimet bahçeleri verir. İki karşı-söz de kalıcılığın tek başına güvence olmadığını görünür kılar: (4:120)’de şeytanın vaadi {ar:غُرُورًا, tr:ghurūran, gloss:aldanış} diye nitelenerek aldatıcı yönü açığa çıkar; (20:120)’de {ar:شَجَرَةِ ٱلْخُلْدِ, tr:shajarati l-khuldi, gloss:ölümsüzlük ağacı} ve {ar:مُلْكٍ لَّا يَبْلَىٰ, tr:mulkin lā yablā, gloss:yok olmayacak hükümranlık} bir teklif olarak sunularak uzun kalış arzusunu görünür kılar. Bu örnekler 31:9’daki vaadin içeriğini değiştirmez, onunla karşıt bağlamları gösterir; güven, sürenin uzunluğundan çok kimin neyi vaat ettiğine bağlanır.

(31:33)’te {ar:إِنَّ وَعْدَ ٱللَّهِ حَقٌّ, tr:inna waʿda llāhi ḥaqqun, gloss:Allah’ın vaadi gerçektir} formülü, ebeveynin çocuğunun ya da çocuğun ebeveyninin hesabını üstlenemediği uyarıda yinelenir; insanı aldatan dünya hayatına karşı sakındırma da aynı sahneyi çevreler. Hakkın bağlayıcı gereklilik ve kişiye düşen sonuç anlamı burada kişisel hesapla buluşur: güvence devredilmez, ancak bu bağlantı belirli bir borç ya da hukukî yükümlülük saptamaz. Bu tekrarın yalnız yargı sahnesini yönetiyor olması da mümkündür. (31:30)’daki gerçeklik-kaynak teması vaadin doğruluğunu kaynağına bağlarken, (31:33)’teki devredilemeyen hesap kişinin sonucunu başkasına aktaramayacağını gösterir; iki katkı ayrı kalır. (31:27)’de yinelenen kudret-hikmet kapanışıyla birlikte okunduklarında odağın mühründe sözü taşıyan düzenli kudreti ve sonuçları başkasına bırakılamayan sorumluluğu bir araya getirirler. Akrabalık bağı hesabı üstlenmez; vaat edilmiş kalışın güveni kişisel sorumluluğu da ortadan kaldırmaz.

</source_prose>
