# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:16**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.middle.claims.json`

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
- Refer to source paragraphs as `17:16 ¶N`.

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

`(17:16 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:16",
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
        "citation": "(17:16 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_16/17_16.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_16/17_16.middle.claims.json \
  --ayah-ref 17:16
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_16/17_16.prose.editorial.tr.md`

<source_prose>
## İradenin Kapsamı

17:16'da yok edilmesi istenen hedef, adı verilmeyen tekil bir yerleşimdir: {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşim}. Buyruk {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} bu yerleşimin {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı}na yönelir; onlar {ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:yerleşmenin içinde itaat sınırını aştılar}. Ardından {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:söz yerleşme aleyhine bağlayıcı oldu} ve {ar:فَدَمَّرْنَٰهَا تَدْمِيرًۭا, tr:fa-dammarnāhā tadmīran, gloss:yerleşimi büsbütün yıktık} gelir. {ar:وَإِذَآ, tr:wa-idhā, gloss:ne zaman ki} açılışı bu diziyi bir zaman koşuluna bağlar: koşul sonraki dönüşleri de kapsadığında buyruk, ihlal, hüküm ve yıkım, böyle bir irade ortaya çıktığında işleyen bir örüntü gibi okunabilir. Koşulun yalnızca ilk irade cümlesini çerçevelemesi de mümkündür; bu kapsamda zincir tek bir gerçekleşme olarak kalır.

Koşul içindeki ilk çekimli fiil {ar:أَرَدْنَآ, tr:aradnā, gloss:diledik}, tamamlanmış bir irade bildirimidir; neyin istendiğini ardından gelen {ar:أَن, tr:an, gloss:-meyi} ile {ar:نُّهْلِكَ, tr:nuhlika, gloss:yok etmeyi} üzerinden açıklar. {ar:أَن, tr:an, gloss:-meyi}, doğrudan {ar:نُّهْلِكَ, tr:nuhlika, gloss:yok etmeyi} biçimini yönetir; IV. bâbın ettirgen ve mansub muzari yapısı {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşimi} helâke götürmeyi iradenin içeriği, yerleşimi de fiilin doğrudan nesnesi yapar. Bu sözdizimi istenen içeriği belirler; iradenin zamanı ve mahiyeti ayrıca belirlenmez. Sonraki {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} yeni çekimli cümleyi başlatır; dolayısıyla helâk, eşgüdümlü başka bir olay değil, dilemenin tamamlayıcısıdır. Kapanıştaki {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} aynı yerleşimi ayrı bir yıkım fiiliyle hedef alır: tasarlanan helâk icrada karşılığını bulur, iki kök eşanlamlılaşmaz ve aradaki süre ölçülmez.

Tamamlayıcısı açık olan bu irade, boşta kalan bir özlemden çok belirli bir sonuca yönelir; burada verilen yerleşim hedefi, kök alanında anılan hayvanı ehlileştirme çağrışımını bu bağlantıda etkinleştirmez. {ar:أَرَدْنَآ, tr:aradnā, gloss:diledik} sonundaki uzun â açılışta sesi tutarken, {ar:أَن نُّهْلِكَ, tr:an nuhlika, gloss:yok etmeyi} ve ardından gelen {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler}, {ar:فَحَقَّ, tr:fa-ḥaqqa, gloss:bağlayıcı hâle geldi}, {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} dönüşleri akışı hızlandırır. Bu ses hareketi, açılıştaki tutulmuş iradeden yanıt ve yıkıma geçişi işittirir; bu, ayetin yerel işitme izlenimidir, vezin kuralı ya da her okuyuşa genellenen etki değildir.

Bu belirli hedef, çevresindeki insan istemeleriyle birlikte daha geniş bir seçim ufkunda duyulur. 17:11 insanın aceleciliğini anar; 17:18'de hemen elde edileni isteyenlerle 17:19'da sonraki hayatı isteyen ve onun için çaba gösterenler yan yana gelir. Bu iki insan hedefindeki {ar:يُرِيدُ, tr:yurīdu, gloss:istiyor} ve {ar:أَرَادَ, tr:arāda, gloss:istedi}, odaktaki {ar:أَرَدْنَآ, tr:aradnā, gloss:diledik} ile aynı isteme ailesindendir. Yakın ve uzak hedeflerle amaçlı çaba, ilahi iradeyi insanın tercih ufku içinde okunur kılar; bu yan yana geliş odak yerleşiminin yıkımını açıklayan zorunlu bir neden bağı kurmaz.

## Yerleşim ve Muhatapları

İstenen helâkin hedefi olan {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşim}, mansub ve belirsiz tekil bir nesnedir: adı verilmeyen bir kent örnek olayın yeri olur. Sözcüğün olağan anlamı insanların toplandığı yerleşimdir; burada eylem değil yer bildirir. Belirsiz tekil biçim, koşullu anlatı içinde örnek bir hedef açar; kapsamı bütün kentlere zorunlu bir yasa olarak yaymaz. Ona bağlanan {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı} ve eylemi içine yerleştiren {ar:فِيهَا, tr:fīhā, gloss:onun içinde}, haritadaki yeri toplumsal hayatı olan bir mekân hâline getirir. Aynı dişil gönderim, sınıfı yerleşime bağlayan -hā'da, eylemin içini kuran {ar:فِيهَا, tr:fīhā, gloss:onun içinde}da, hükmü yerleşime yönelten {ar:عَلَيْهَا, tr:ʿalayhā, gloss:onun aleyhine}da ve yıkım fiilindeki -hā'da sürer. Dilbilgisi aynı kenti farklı ilişkiler boyunca izletir; bu süreklilik dilbilgiseldir, yerleşimin her ilişkide aynı fiziksel sınırla kavrandığını göstermez.

Buyruk fiili {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} tamamlanmıştır; açık alıcısı {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı}dır ve bu isim fiilin nesne konumundaki muhatabını bildirir. Alıcı böylece belirgindir; emredilen eylemi söyleyen bir tümleç verilmediğinden buyruk içeriği açık kalır. Ardından gelen tamamlanmış çoğul {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler}, dizideki tek açık insan eylemidir: geçişsiz fiil itaat sınırından çıkışı bildirir, ayrı bir suç nesnesi adlandırmaz. Bu bağ, ihlali buyruğa yanıt olarak okutur; ilahi buyruk bağlamı karşı gelme yönünü de açar. Bitişik {ar:فَ, tr:fa, gloss:ardından} buyruğu yanıta yaklaştırır; bu yakınlık söyleyiş içindeki sıralamayı sıkılaştırır, aradaki sürenin yokluğunu belirlemez. Böyle bir düzen bir sınama sahnesi açar; eylem sıralaması bir insan aracısı belirtmez.

Bu buyruğun çevresindeki kıraat aktarımları buyruk, çoğaltma, yetki ve danışma yönlerini anar; böylece aynı sahne çevresinde farklı nedensellik yolları açılır. Varyantların tam metinleri verilmediği için bu yönler görünen {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} biçiminin yerini almaz ve birbirine üstünlük kurmaz.

Buyruğun alıcısı olan {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı}, edilgen ortaçlı çoğul bir sınıf adıdır; sonundaki -hā grubu onu yerleşime bağlar. Sözcük bolluk, geniş imkân ve rahat yaşayış içindeki kişileri anlatır. Aynı kelime ailesindeki kullanımlar, bolluğun kişiyi küstahlaştırıp elindekinin değerini unutturabileceğini ve sınır aşmaya sürükleyebileceğini; şımartılan kişinin de dilediğini yapmasına engel olunmadan bırakılabildiğini taşır. Odakta bu yan anlamları, buyruğun ardından gelen bağımsız {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler} eylemi ve onu buyruğa bağlayan {ar:فَ, tr:fa, gloss:ardından} etkinleştirir: bolluk içindeki konum ihlalin toplumsal zeminini ve geniş hareket alanını görünür kılar. Sınıfı durumuyla adlandıran ortaç ile tamamlanmış ihlal eyleminin ayrılığı, davranışı kişilerin bütün kimliğiyle özdeşleştirmez. 34:34'te başka bir kentin varlıklıları uyarıcıyı reddeder; 29:34'te başka bir kent halkı itaatsizliği yüzünden cezalanır. Bu ayrı sahneler benzer bir tepkinin farklı yerleşimlerde yinelenmesini düşündürür; bu bağlantıda bolluk tek neden, kanıtlanmış saik, mazeret ya da resmî izin değildir ve örüntü her varlıklı gruba genellenmez.

Bu sınıfın konumu, eldeki malın yanı sıra nimet ve derece dağılımı içinde de belirir. 17:6'da mallar ve oğullarla desteklenme, 17:20'de iki gruba da ulaşan nimet, 17:21'de insanlar arasındaki derece farkları anılır. Bu bağlamlar {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı}nı imkân ve etkileri farklılaşan bir konuma yerleştirir; risk servetin kendisinden çok bu konumun eyleme kazandırabildiği geniş etkide belirir. 43:32'de geçimliklerin dağıtılması ve bazı insanların derece bakımından yükseltilmesi aynı toplumsal zemine ayrı bir bağlamdan ışık tutar.

Olağan emir anlamının yanında, aynı sözlük alanındaki {ar:أَمْر, tr:amr, gloss:emir} yetkiyi, makamı, yetki taşıyan kişiyi ya da birini o makama getirmeyi de anlatabilir. 17:21'deki derece farkları ve 43:32'deki geçim ile rütbe dili, bu yetki yankısını kentin işleyişini etkileyebilecek ayrıcalıklı sınıfa taşır. Odaktaki {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} buyruğunun bu sınıfa yönelmesi ve sonucun {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşime} dönmesi, muhatapla hedef arasında sınırlı bir yönetişim boyutu hissettirir; bu temas içinde sınıf, yalnız emri alan değil, buyurma gücüne yakın duran kişiler gibi de algılanabilir. Bu, 43:32'nin odak kentini betimlemesi ya da ayetin sınıfa resmî makam vermesi değildir; olağan buyruk anlamı korunurken bağlamsal bir yetki yankısı eklenir.

Dilbilgisi önce eyleyenlerle sonucu taşıyan kentin ölçeklerini ayırır: {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı} buyruğu alır, {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler} çoğul eylemi bu gruba verir; {ar:عَلَيْهَا, tr:ʿalayhā, gloss:onun aleyhine} ve {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} ise sonucu tekil yerleşime döndürür. Yerleşim adı sakinlerini topluca kapsayabilir; aynı metonimik kullanım yalnız ihlalde bulunan nüfusu da gösterebilir. Böylece açık fail çoğul zümre olarak kalırken sonuç, daha geniş bir toplumsal gövdeye ulaşır; dilbilgisi her sakini eyleyen ilan etmez. 17:2'de Musa'ya verilen rehberlik, 17:7'de iyilik ve kötülüğün kişinin kendisine dönmesi, 17:15'te kimsenin başkasının yükünü taşımaması ve elçi gönderilmeden azap edilmemesi, bireysel sorumluluğu bu toplumsal sonuçla birlikte görünür kılar.

## İç Mekânın İmgeleri

{ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşim}in olağan anlamı, insanların bir araya geldiği yerdir; kök alanındaki kap ya da oyuk kullanımı ise suyu veya yiyeceği içinde toplama imgesini sağlar. {ar:فِيهَا, tr:fīhā, gloss:onun içinde} yerleşimin içini belirler, {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:onun bolluk içindeki sınıfı} oraya bağlı topluluğu gösterir, {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler} bu iç mekânda gerçekleşen ihlali bildirir. İçlik, sakinler ve içerideki eylem bir araya gelince yerleşim, ortak hayatı tutan bir hazne gibi görünür: kök yankısı kentin toplumsal mekânını genişletir, sözün olağan yerleşim anlamını devralmaz. İhlal ise anlatılan sınıfın eylemidir; hazne imgesi onu bütün sakinlere yaymaz.

Hazne imgesinin çizdiği toplumsal mekândan ayrı olarak, {ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:yerleşmenin içinde itaat sınırını aştılar} fiildeki sınır aşımını somutlaştırır. Olağan ahlaki anlam itaatten çıkıştır; aynı kök alanındaki taze hurma tanesinin kendi kabuğundan çıkışı, bu eyleme içeriden dışarı doğru bir hareket biçimi verir. Buyruğun ardından gelen ihlal, yerleşmenin içini bildiren {ar:فِيهَا, tr:fīhā, gloss:onun içinde} ve bitişik {ar:فَ, tr:fa, gloss:ardından} ile temas eder; 29:34'teki kent, itaatsizlik ve ceza bağı da bu kabuk imgesini tetikler. Böylece hazne kentin toplumsal ortamını, kabuğundan çıkan tane ise ihlalin sınırını aşan hareketini görünür kılar. Bu bağlantıda hurma fiilin sözlük anlamı değil, itaatten çıkışı biçimlendiren bir imgedir.

17:4'te yeryüzündeki bozulmanın iki kez yaşanacağı söylenir; 17:5 ise gönderilenlerin evlerin içinden ve aralarından geçtiği somut güzergâhı verir. Odaktaki {ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:yerleşmenin içinde itaat sınırını aştılar} ihlali yerleşmenin içine koyar, {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} yıkımın hedefini kentte tutar. Bu iki ayrıntı 17:5'teki ev arası geçişle yan yana gelince, içeriden açılan toplumsal sınırdan yerleşimin içine uzanan bir erişim yolu olarak duyulabilir. 17:5'te hareket edenler odaktaki varlıklı sınıftan bağımsız olabilir; ortak mekânsal imge, aynı fail ya da zorunlu neden bağı kurmaz.

Odaktaki {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} olağan anlamıyla yıkımı bildirir; kök ailesindeki ayrı bir dal ise bir evin ya da topluluğun bulunduğu yere girmeyi anlatır. {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşimi} yıkımın hedefini, {ar:فِيهَا, tr:fīhā, gloss:onun içinde} iç mekânı, fiildeki dişil nesne eki de aynı kenti gösterir; bu ilişkiler giriş dalına yerleşimin içine doğru bir yön verir. 17:5'te evlerin arasından geçen hareket güzergâhı, 27:52'de kötülükleri yüzünden boş kalan evler ise görünür sonucu ekler. Birlikte, iç düzeni açılmış toplumsal gövdeye girip kentin bütününe yayılan bir yıkım tasavvuru oluşturabilirler. Dışarıdan gelen darbe, olağan yıkım okuması olarak açık kalır; içeri girme bu fiilin çevirisi ya da yıkımın fiziksel mekanizması değil, bu bağlantıya özgü mekânsal yankıdır.

Bu iç mekân anlatısı, 17:4, 17:5, 17:6, 17:7 ve 17:8'deki dönüş çizgisi içinde zamansal bir karşılık bulur. 17:4'teki iki bozulmanın ardından 17:6'da geri verilen güç ve {ar:الْكَرَّةَ, tr:al-karrata, gloss:yeniden dönüş}, 17:7'de üstün gelinen şeylerin yeniden yıkılması, 17:8'de ise dönülürse karşılık olarak dönüleceği bildirilir. Bu ayrıntılar tekrarlanan bozulma, yenilenen kapasite, yıkım ve karşılıklı dönüşü aynı tarih içinde birbirine bağlar. Odaktaki {ar:وَإِذَآ أَرَدْنَآ, tr:wa-idhā aradnā, gloss:dilediğimizde} koşulu ile eklenen sonuçlar, 17:16'yı yenilenebilir toplumsal tarihin bir yıkım evresi gibi duyurabilir. 17:6'daki dönüş adı odak iradesiyle farklı köktendir; bu nedenle geri gelme yönü sözcüğün anlamı değil, bağlamın eklediği yankıdır. Bu çevrim okuması İsrail anlatısının tarihsel çerçevesinde kalır; bütün kentlere yönelik bir yasa kurmaz.

## Sözün Bağlanması

Dönüşlerin geniş tarih içindeki yankısından ayetin cümle hareketine gelince, üç fâ buyruk, yanıt, hüküm ve icra basamaklarını birbirine bağlar. {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} sonrasındaki {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler} yanıtı başlatır; sonraki {ar:فَحَقَّ, tr:fa-ḥaqqa, gloss:bağlayıcı hâle geldi} hükmü getirir, onun ardından {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} icraya geçer. Böylece hüküm, yanıt ile yıkım arasında ayrı bir orta aşama olarak belirir. Fâlar sıralama ve sonuç bağını taşır; her geçişin nedensel payı, aradaki sürenin miktarı ve yıkımın fiziksel yolu ayrıca belirtilmez.

Bu orta aşamanın öznesi belirli biçimiyle {ar:ٱلْقَوْلُ, tr:al-qawlu, gloss:söz ve hüküm}dur: {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:söz yerleşme aleyhine bağlayıcı oldu} cümlesinde {ar:عَلَيْهَا, tr:ʿalayhā, gloss:onun aleyhine} hükmün yöneldiği yerleşimi gösterir. {ar:فَحَقَّ, tr:fa-ḥaqqa, gloss:bağlayıcı hâle geldi} zorunluluk ve bağlayıcılık taşır; önceki çoğul ihlalin ardından sözü tekil kentin aleyhine hüküm hâline getirir. Böylece hedef ayrıcalıklı sınıftan yerleşimin bütününe kayar. Bu cümledeki bağlayıcılık, kişisel mülkiyet ya da hak sahipliği değil, kente yönelen hükmün zorunlu oluşudur; fiilin doğruluk ve sabitlik yönü ise ayrı bir yankı olarak kalır. Sözün belirli biçimi cümledeki özneyi tanımlar; odak dışında daha önce söylendiğini, içeriğini ya da konuşanını belirlemez.

Bağlayıcılık anlamını koruyan {ar:فَحَقَّ, tr:fa-ḥaqqa, gloss:bağlayıcı hâle geldi}, doğru, sabit ve yerleşik olanı bildiren kullanımıyla da işitilebilir. Önceki {ar:فَفَسَقُوا۟, tr:fa-fasaqū, gloss:sınırı aşıp karşı geldiler} eylemi kentin hâlini açığa çıkarır; belirli {ar:ٱلْقَوْلُ, tr:al-qawlu, gloss:söz ve hüküm} bu hâli adlandırınca karar doğruluğu sabitlenmiş gibi görünür. Geçişsiz fiil bu okuma içinde kanıtlayan ayrı bir fail kurmaz. Böylece doğru ve sabit olma yankısı, bağlayıcı hükmü kaldırmadan kentin görünen hâlini kararın okunabilir dayanağına dönüştürür.

{ar:ٱلْقَوْلُ, tr:al-qawlu, gloss:söz ve hüküm} olağan anlamıyla söylenmiş sözdür. Buyruktan çoğul yanıta, bağlayıcı sözden yıkımın icrasına uzanan yerel zincirde bu söz, yalnız bilgi aktarmakla kalmayıp hükmü yürürlüğe koyan bir söz edimi gibi de duyulur. Bu işlev cümlenin kendi sıralamasından doğar; konuşanı ve sözün içeriği verilmez.

{ar:ٱلْقَوْلُ, tr:al-qawlu, gloss:söz ve hüküm}un başka bir kullanımı, konuşma olmadan bir durumu belli etmektir. Bu yankı, önceki ihlalin yerleşimin hâlini göstermesi, {ar:فَحَقَّ, tr:fa-ḥaqqa, gloss:bağlayıcı hâle geldi}nın bu hâli sabit ve hükme değer kılması, yıkımın da sonucu görünür kılmasıyla işler: olayların kendisi sözsüz bildirim gibi duyulur. Bu, söylenmiş söz anlamına eklenen bir olasılıktır; qawl'u mutlaka sessiz işarete dönüştürmez.

17:5'te ilk İsrail olayı için {ar:وَكَانَ وَعْدًا مَفْعُولًا, tr:wa-kāna waʿdan mafʿūlan, gloss:yerine getirilmiş bir vaat idi} denmesi, odaktaki {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:söz yerleşme aleyhine bağlayıcı oldu} ve yıkımın ardından gerçekleşmesiyle ayrı bir tarihsel paralellik kurar. Bu temas, bağlayıcı sözün olayda gerçekleşip doğrulanması yönünü belirginleştirir; iki sahnenin sözü ya da yerleşimi özdeş değildir ve paralellik belirli bir önceki tehdidi adlandırmaz.

17:13'te her insanın payının kendi boynuna bağlanması ve açılmış kitabın karşısına gelmesi, 17:14'te kişinin kendi kitabını okumasıyla sürer. Payın bağlanması, kaydın açılması ve okunması, odaktaki {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:söz yerleşme aleyhine bağlayıcı oldu} hükmünün yanına bireysel eylemlerin geçmişini koyar; böylece kentin görünen hâli birikmiş eylemler karşısında okunabilir olur. Kişisel kayıt kent aleyhine bağlanan sözden ayrı kalır; daha önce söylenmiş bir tehdidin gerçekleşmesini doğrulaması da olasıdır.

Kişisel kayıttan yerleşimlerin sonuna geçince iki ölçek yan yana gelir: 17:58'de her yerleşim için yıkım ya da ağır azap ufku yazılıdır; 27:85'te yanlış yapanların işlerinden ötürü üzerlerine söz düşer. İlki kentlerin yazılı son ufkunu, ikincisi eylem sonrasında gelen hükmü verir; odaktaki {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:söz yerleşme aleyhine bağlayıcı oldu} bu ikisi arasında ihlalden hükme giden sırayı korur. Bu bağlantı sözün önceden yazıldığını ya da söylendiğini ve hükmün tam zamanını belirlemez; 17:58 de kişisel sicili değil yerleşimlerin sonunu konu eder.

## Yıkımın Kapsamı

İradenin başındaki {ar:أَرَدْنَآ, tr:aradnā, gloss:diledik} ile kapanıştaki {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} aynı birinci çoğul özneyi ve baştaki {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşimi} hedefinde kalan dişil nesne ekini taşır; bu dilbilgisel halka iradeyi aynı kente yönelen icraya bağlar. Kişi ekleri anlatıdaki özne ve hedef sürekliliğini gösterir; failin mahiyeti hakkında ayrıca hüküm kurmaz. İrade içindeki {ar:نُّهْلِكَ, tr:nuhlika, gloss:yok etmeyi} IV. bâbın ettirgen biçimiyken, {ar:فَدَمَّرْنَٰهَا, tr:fa-dammarnāhā, gloss:onu yıktık} ikinci bâbın geçişli yıkım fiilidir; iki ayrı kök niyet ile icrayı birbirinden ayırır. Ardındaki {ar:تَدْمِيرًۭا, tr:tadmīran, gloss:yıkım}, aynı kökten mansub mastar ve mef'ul mutlak olarak yıkım eylemini yeniden adlandırıp pekiştirir: tek tamamlanmış eylemin ağırlığını artırır, sayısını ya da ölçüsüz miktarını değil. İkiz mîm ve mastarın uzayan sonu bu kapanışa yerel bir işitsel mühür verebilir; izlenim ses akışına aittir, vezin kuralı veya seyrek kullanım iddiası taşımaz.

Bu yerel niyet-icra halkası 17:17'de Nuh'tan sonra nice kuşakların helâk edildiğinin bildirilmesiyle daha uzun bir tarihsel ölçeğe açılır: odaktaki {ar:أَن نُّهْلِكَ قَرْيَةً, tr:an nuhlika qaryatan, gloss:bir yerleşimi helâk etmeyi} ile 17:17'deki {ar:أَهْلَكْنَا مِنَ الْقُرُونِ مِنْ بَعْدِ نُوحٍ, tr:ahlaknā mina l-qurūni min baʿdi Nūḥ, gloss:Nuh'tan sonra nice kuşakları helâk ettik} aynı helâk kökünü farklı yapılarda taşır. Bu yankı tek yerleşim sahnesini kuşaklar boyu uzanan kayıtla birlikte duyurur; hedef kentin o önceki topluluklardan biri olduğunu söylemez ve bu tarihsel ilişkiyi bütün sureye yaymaz.

Farklı kent sahneleri ortak bir hüküm örüntüsüne ayrı katkılar verir: 34:34'te varlıklı kesimin uyarıcıyı reddi ve 29:34'te kent halkının itaatsizlik yüzünden cezalanması, ihlal ile sonucu yan yana getirir; 27:51'de topluluk ve halkının birlikte yok edilmesi yıkımın kapsamını, 27:52'de yanlışlar yüzünden boş kalan evler sonucun görünür izini, 46:27'de çevre kentlerin yıkılması ise ölçeğin başka yerleşimlere uzanışını gösterir. Odaktaki {ar:فَدَمَّرْنَٰهَا تَدْمِيرًۭا, tr:fa-dammarnāhā tadmīran, gloss:yerleşimi büsbütün yıktık} bu ayrı sahnelerle birlikte tam yıkım ve toplumsal sonuç temasını güçlendirir. Bağlantı yinelenen bir uyarı örüntüsüdür, ortak olay ya da mekanizma değildir; varlığı tek suç nedeni yapmaz ve her sakinin aynı eylemi üstlendiğini söylemez.

Odaktaki {ar:قَرْيَةً, tr:qaryatan, gloss:bir yerleşim} ve {ar:فَدَمَّرْنَٰهَا تَدْمِيرًۭا, tr:fa-dammarnāhā tadmīran, gloss:yerleşimi büsbütün yıktık} taşıyıcılarının yanında 17:103 başka bir mekânsal tersine dönüş sunar: Firavun halkı ülkeden çıkarmayı tasarlarken kendisi ve yanındakiler boğulur. Bu ayrı fail ve olay, toprak üzerindeki denetimin geçiciliğini duyurur; odak kentinin yıkımını açıklamaz. 17:58'de yazılı yerleşim sonu, 46:27'de çevre kentlerin yıkılması ve belki dönsünler diye verilen işaretlerle yan yana gelir; yazılı son ufku içinde geri dönüş ihtimalini açan bu işaretlerin kapsamı açık kalır. 46:27'deki dönüş fiziksel yeniden kurulma mı, yoksa toplumsal onarım mı demektir?

</source_prose>
