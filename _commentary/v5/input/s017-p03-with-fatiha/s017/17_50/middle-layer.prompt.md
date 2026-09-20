# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:50**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.middle.claims.json`

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
- Refer to source paragraphs as `17:50 ¶N`.

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

`(17:50 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:50",
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
        "citation": "(17:50 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_50/17_50.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_50/17_50.middle.claims.json \
  --ayah-ref 17:50
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_50/17_50.prose.editorial.tr.md`

<source_prose>
## Söylenen Hâl

Âyetin kısa buyruğu, “De ki: {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ya da {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} olun” sözleriyle açılır. {ar:قُلْ, tr:qul, gloss:söyle} ile {ar:كُونُوا۟, tr:kūnū, gloss:olun} emirleri arasındaki kısa durak, söyleme eylemini ardından gelecek maddi hâl sözüne bağlar. Kemik ve ufalanmış kalıntılardan sonra yeni yaratılışın nasıl olacağı sorusuna verilen cevap (17:49), böylece işitilebilir, muhataplara dönük bir bildiriye dönüşür. Sözün içeriği taş ya da demir hâlidir; söyleme buyruğu bu maddeleri meydana getiren bir güç isnat etmez.

Bu hitapta tekil {ar:قُلْ, tr:qul, gloss:söyle} ile çoğul {ar:كُونُوا۟, tr:kūnū, gloss:olun} arasındaki kişi değişimi duyulur: söyleme emri hitabı taşıyan muhataba, hâl buyruğu ise itirazı dile getiren topluluğa yönelir (17:49). Söyleme kökünün burada öne çıkan yanı, sözü sesli biçimde dışarı çıkarıp kamusal bildiriyi kurmasıdır. Bu yerel kullanım iç kanaat ya da suçlama değil, dışa yöneltilmiş sözlü hitaptır; çoğul hitabın kapsamı da bu karşılaşmayla sınırlıdır.

{ar:كُونُوا۟, tr:kūnū, gloss:olun}, olağan “olmak, bir hâlde bulunmak” anlamındaki fiilin Form I çoğul emiridir. Tek bir fiil iki belirtme durumundaki isim yüklemini yönetir: önce {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}, ardından {ar:أَوْ, tr:aw, gloss:ya da} ile ayrılan {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}. İki ad aynı fiile bağlanır; ayrıca bir dönüşüm fiili ya da işlem gören nesne kurulmaz. Form I çoğul emir, ettirgen dönüşüm değil, bu hâllerde bulunma çağrısıdır: muhataplardan taş ya da demir yaratmaları değil, bu hâlleri üstlenmeleri istenir. Belirsiz adlar tek bir kaya veya demir parçasından çok madde sınıflarını gösterir. Bu iki madde, itiraza karşı bir sığınak gibi tasarlanarak meydan okumayı en dirençli hâllere kadar taşır; yine de bu tasavvur dirilişin önünü kesmez ve ilahi kudrete sınır koymaz.

Bu cevap, kemiklerden ufalanmış kalıntılara uzanan itirazın maddi ufkunu değiştirir (17:49). {ar:عِظَامًا, tr:ʿiẓāman, gloss:kemikler} bedenin sert kalıntılarını, {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} da dağılmış parçaları öne çıkarırken; {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ile {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} aynı diriltilme sorusunda daha dirençli iki madde hâli olur (17:49). {ar:مَبْعُوثُونَ, tr:mabʿūthūna, gloss:diriltilecek} sözü bütünlüğünü yitirmiş kalıntıları da sorunun içinde tutar. Bu sıra yalın bir sertlik yükselişi olarak okunabilir; ayrıca dağılmış kalıntılarla yoğun ve dirençli maddeleri karşı uçlara yerleştirip bütünlüğün azalmasının dönüş imkânını belirlemediği bir yelpaze açar. Bu ikinci çizgi yorumlayıcıdır; yalın sertlik okuması da yerinde kalır. Yakınlık, 17:49'daki kalıntı itirazını, odaktaki maddi buyruğu ve ilk var ediş cevabını tek dönüş sorusunda buluşturur (17:49, 17:51), ancak aralarında fiziksel bir yeniden-birleşme süreci tarif etmez.

İtirazdaki {ar:خَلْقًا, tr:khalqan, gloss:yaratılış} olağan anlamıyla yaratılıştır (17:49). {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ile {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} gibi ayrı maddi biçimlerin yan yana gelişi, bu sözcüğün ölçü ve oran vererek biçimleme imgesini etkinleştirir: dönüş, başka biçimlerde var edilebilme açısından da duyulur. Aynı sözcüğün varlığa getirme yönü, ilk var ediş cevabına bağlandığında ikinci bir katkı sunar (17:51). {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} yaratmanın başlangıcını, {ar:أَوَّلَ مَرَّةٍ, tr:awwala marratin, gloss:ilk kez} ise bu başlangıcın önceliğini öne çıkarır. Böylece bir yanda biçimlenebilirlik imgesi, öte yanda mevcut biçimleri var eden ilk başlangıç belirir; ölçü-biçimleme çağrışımı fiziksel bir yaratma yöntemi tarif etmez.

Yeni yaratılış itirazındaki {ar:جَدِيدًا, tr:jadīdan, gloss:yeni} olağan “yeni” anlamını korurken kesinti sonrasındaki yenilik düşüncesini de çağırır (17:49). Bu çağrışım, taş ve demir karşısındaki dönüşü yenilenme yönünden duyulur kılar; burada söz konusu olan yeni oluşun imgesidir, kesme ya da yeniden birleştirme sahnesi değil. Ardından gelen {ar:أَوْ خَلْقًا مِّمَّا يَكْبُرُ فِي صُدُورِكُمْ, tr:aw khalqan mimmā yakburu fī ṣudūrikum, gloss:ya da göğüslerinizde büyüttüğünüz başka bir yaratılış} seçeneği, açıkça anılan {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} maddelerinden daha geniş bir tasavvura geçer (17:51). {ar:كُونُوا۟, tr:kūnū, gloss:olun} buyruğu bu devamda da bir hâle girme anlamını taşır: taş ve demir, muhatapların göğüslerinde büyüttükleri başka bir yaratılış ihtimaline açılır. Bu ek seçenek abartılı bir vurgu olarak da okunabilir; somut ilk seçenekler yine taş ve demirdir.

İlk var ediliş cevabı geri dönüş sorusunu yanıtlar: {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek} sorusunun karşısına {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti} ve {ar:أَوَّلَ مَرَّةٍ, tr:awwala marratin, gloss:ilk kez} çıkar (17:51). {ar:فَطَرَكُمْ, tr:faṭarakum, gloss:sizi ilk kez var etti}nin başlangıç anlamına eşlik eden açma ya da yarma imgesi, dönüşü önceki biçimin ötesinde yeniden başlangıç olarak duyurur; bu bağlantıda imge, somut bir kesme eylemi değil, ilk var edişin nasıl işitildiğine dair bir yankıdır. Cevabın ardından başların hareketi {ar:يُنْغِضُونَ, tr:yunghiḍūna, gloss:hareket ettirirler} ve {ar:رُءُوسَهُمْ, tr:ruʾūsahum, gloss:başlarını} sözleriyle görünür olur (17:51). Jest şaşkınlık ya da kuşku gösterebilir, ayrıca itirazın bedensel yankısı olarak okunabilir; böylece dönüş tartışmasına insanın verdiği tepkiyi ekler, dönüşü gerçekleştirmez.

## Taş ile Demirin Direnci

İki yüklemin ilki olan {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}, buyruğun ilk somut maddi hâlini kurar. Belirsiz biçimi tek bir kaya parçasını değil, taş türünü açık bırakır. Taşın önce gelişi doğal kayanın sertliğini başlangıç noktası yaparken, ardından gelen {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} işlenmiş metal imgesini açar. Taş sözcüğünün pürüzlü ve ağır duyulabilen tınısı bu maddi ağırlığa işitsel bir karşılık ekler; ses izlenimi temkinlidir ve sözlük anlamından ayrı bir izlenim olarak kalır.

{ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ın kök ailesindeki kapalı alan ve erişimi kısıtlama kullanımları, ilk yüklem oluşunu hemen ardından gelen {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} seçeneğiyle birleştirerek kapanma basıncı yaratabilir. Bu yankı, taş ve demiri itiraza karşı sığınak gibi tasarlanan dirençli hâller olarak duyurur. Kapanma burada taş sözcüğünün maddi anlamına eklenen kök-aile çağrışımıdır; taş yine somut madde adıdır ve bu bağlantı aşağıdaki bileşik engel imgesinden ayrıdır.

Taştan sonra gelen {ar:أَوْ, tr:aw, gloss:ya da}, aynı {ar:كُونُوا۟, tr:kūnū, gloss:olun} buyruğunun ikinci hâli olan {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}i ilk seçenekten ayırır. İki ağır ad arasındaki parçacık işitilir bir vuruş ve kısa bir durak yaratırken, doğal kaya imgesinden işlenmiş metale geçiş dirençte bir yükseliş gibi duyulabilir. Bu yön duygusu sıralamanın olası etkisidir; {ar:أَوْ, tr:aw, gloss:ya da} iki ayrı seçeneği sunar, zorunlu derece ölçeği kurmaz. Belirsiz tekil {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} belirli bir parça değil madde türüdür. Demir yerel ikilinin doruğunu oluşturur; dönüş söyleyişi ise sürer ve yeni bir yaratılış ihtimaline açılır (17:51).

{ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ın çoğul biçimiyle {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}in belirsiz tekil biçimi, ikiliye farklı işitsel ve görsel ağırlıklar verir. Demir adındaki diş ünsüzleri keskinlik izlenimi yaratabilir; bu ses katmanı temkinli bir duyumdur ve kendi başına bir direnç derecesi belirlemez. Bundan ayrı olarak, demirin kök ailesindeki kenar ve sınır kullanımları son konumunu ölçülü biçimde renklendirir. Bu sözlüksel yankı demir sözcüğünü bıçak ya da soyut sınır anlamına taşımaz; maddi demir imgesiyle yan yana durur.

Aynı {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} kök ailesindeki bir kişiye ya da buyruğa karşı çıkma ve boyun eğmeme anlamları, maddi direncin yanına sosyal bir karşı koyuş duruşu ekler. Yeni yaratılış kuşkusu ile çoğul muhataplara yönelen buyruk bu benzetmeyi etkinleştirebilir (17:49). Bu bağlantıda odaktaki demir maddi seçenek olmayı sürdürür; karşı koyuş, demirin iradesi değil, itirazın çağırdığı sosyal yankıdır.

Kök ailesindeki ayrı engelleme kullanımları, atfedilmiş bileşik bir imge içinde birbirini tamamlar. {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ın erişmeyi, yararlanmayı ya da üzerinde işlem yapmayı kısıtlayan yanı önce yaklaşma ve kullanım imkânını keser. {ar:أَوْ, tr:aw, gloss:ya da} ile seçilen {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} iki şeyi ayırıp karışmalarını önleyen sınır çizgisini ekler; bu çizgi bir alanın kapsamını ya da son noktasını da belirleyebilir. Demirin kök ailesindeki başka bir engelleme kullanımı giriş ve çıkışı veya bir eylemi durdurmayı kapsar. Böylece taş erişimi keserken demir ayırır, sınırlandırır ve geçişi önler: katkılar tek bir geniş engel imgesinde birleşse de ayrı işlemler olarak kalır. Bu özel kök-aile okumasında taş ve metal somut maddelerdir, demir hukukî yasak ya da soyut terime dönüşmez ve tasarlanan engel dirilişi fiilen durdurmaz.

Aynı ikili, bileşik engel okumasından ayrı, iki direnme tarzını yan yana getiren keşifsel bir imge de açabilir. {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} yoğun, künt ve yerinden oynamayan bir kütle olarak ağırlığıyla karşı koyar; {ar:أَوْ, tr:aw, gloss:ya da} ile seçilen {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} ise kök ailesindeki kesici veya delici aracın ince, keskin ağzını çağrıştırarak nüfuz eden direnç biçimini ekler. Böylece {ar:أَوْ, tr:aw, gloss:ya da} yalnız iki maddeyi değil, kütleyle keskin kenar arasında iki ayrı direnme tarzını da yan yana duyurabilir. Bu imgesel temas demiri bıçak anlamına getirmez; daha yalın sertlik yükselişi de geçerliliğini korur.

Taşın sertliğine açılma ve tepki ihtimali de eşlik eder: bazı taşlardan ırmaklar fışkırır, bazıları yarılıp içlerinden su çıkar, bazıları Allah korkusuyla aşağı iner (2:74). Bu görüntüler odaktaki {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ı yalnızca kapalı kütle olarak düşünmeyi zorlaştırır; direnç, her bağlamda tepkisizlik anlamına gelmez. Yankı bu bağlantıyla sınırlıdır: 2:74'teki taşların odaktaki taşlarla aynı nesneler olduğu ya da bütün taşların akışkan ve duyarlı bulunduğu ileri sürülmez; ilişki biçimbilgisel değil bağlamsaldır.

Taş yüzeyine uzak bir pürüzsüzlük imgesi de eklenebilir. {ar:أَصْفَىٰ, tr:aṣfā, gloss:seçip ayırdı} fiilinin olağan seçme ve ayırma anlamı, aynı söz ailesinde toprağından ya da kilinden arındırılmış pürüzsüz taş imgesiyle yan yana durur (17:40). Odaktaki {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} bu yüzey yankısını tetikleyince sertliğe kısa süreli bir pürüzsüzlük dokusu eklenir. Bu uzak, keşifsel bağlantı söz ailesine aittir; çekimli fiil seçip ayırmayı anlatır, pürüzsüz taşı değil (17:40).

Demirin iki başka bağlamdaki görüntüsü direnç imgesine birbirini dengeleyen iki katkı verir. Parçalar iki yamacın arasına yerleştirilip ısıtıldığında, odaktaki {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} için sınırın maddi biçimini kuran bir set belirir (18:96). Davud için demirin yumuşatılması ise aynı maddenin işlenebilirliğini öne çıkarır (34:10). Birlikte okunduklarında, demirin sınır oluşturabilmesiyle şekil alabilmesi yan yana gelir: sertlik, mutlak işlenemezlik değildir. Bu yakınlık odak sözcükle biçimbilgisel eşleşme ya da diriliş kanıtı değil, iki ayrı bağlamdan kurulan bir karşılaştırmadır. Yumuşatmayı direnç okumasına karşı örnek saymak da, bağlantıyı anlamlı bulmamak da mümkün; değerlendirme açık kalır.

## Alımlama, Yetki ve Ölçek

Maddi dirençten alımlama sorusuna geçildiğinde, {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ile {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} de her şeyin tesbih ettiği bildirimin kapsamına girer (17:44). {ar:شَىْءٍ, tr:shayʾin, gloss:bir şey}in genişliği bu iki maddeyi de içerir; insanların tesbihi kavrayamaması, anlaşılmazlığın sınırını insanın idrakine yerleştirir (17:44). {ar:يُسَبِّحُ, tr:yusabbiḥu, gloss:tesbih eder} ve {ar:لَا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:lā tafqahūna tasbīḥahum, gloss:tesbihlerini kavrayamazsınız} birlikte okunduğunda, maddenin tesbihinin insan için kavranamaz olduğu belirginleşir; taş ve demir insan gibi konuşan özneler hâline gelmez. Bu bağlam, dirençli maddeleri de evrensel bildirimin içinde tutar, fakat diriltilmenin fiziksel mekanizmasını açıklamaz (17:44).

Alımlama sahnesindeki kapanma basamak basamak derinleşir: dıştaki {ar:حِجَابًا, tr:ḥijāban, gloss:örtü} perdeyi kurar (17:45); kalplerin üzerindeki {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} ve kulaklardaki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} kapanmayı alıcının içine taşır (17:46); {ar:سَبِيلًا, tr:sabīlan, gloss:yol} bulamama ise yönelişin kesildiği sonucu verir (17:48). Bu aşamalar, odaktaki {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ın erişimi kısıtlayan ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}in geçişi önleyen çağrışımlarıyla paralel okunabilir; muhatapların alımlamayı kendini koruyan bir kapanışla daraltması da bu temasa eşlik edebilir. Bu, belirli bir bağlamsal paralelliktir, nedensellik iddiası değil; iki sahnenin ayrı kalması da mümkündür.

Önceki {ar:قُلْ, tr:qul, gloss:söyle} ve {ar:كُونُوا۟, tr:kūnū, gloss:olun} buyruklarının sesli hitabı, çağrı ile karşılık sahnesinde yankılanır. {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırdığı} çağrısına {ar:فَتَسْتَجِيبُونَ, tr:fatastajībūna, gloss:karşılık verirsiniz} cevabı gelir; {ar:إِلَّا قَلِيلًا, tr:illā qalīlan, gloss:ancak kısa bir süre} bu karşılaşmanın süresini kısaltır (17:52). Böylece {ar:كُونُوا۟, tr:kūnū, gloss:olun} buyruğundaki maddi hâl, kısa süreli bir yaşantı olarak zamansal ölçü kazanır. Yankı iki ayrı insan hitabı arasındadır; madde konuşan özne olmaz. Komşu akışta kalıntı itirazından buyruğa, oradan çağrı-cevaba uzanan bir çizgi duyulabilir (17:49, 17:51, 17:52); bu olası devamlılık nedensel bir bağ kurmaz.

En güzel sözü söyleme ölçüsü, odaktaki {ar:قُلْ, tr:qul, gloss:söyle} buyruğunun sesli karşılığına hitabın niteliği yönünden temas eder (17:53). {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} sözü ölçüyü kurarken, araya giren {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtma çıkarır} sözlü kışkırtmanın riskini görünür kılar (17:53). Söyleme ailesiyle ilişkilendirilen müzakere imgesi de iki taraflı konuşma ihtimalini açar; bu olasılık iyi söz ölçüsüyle yan yana duyulabilir. Bu bağlantı ayrı bağlama ait bir yankıdır: odak âyette karşılıklı konuşma yapısı yoktur, o bağlamın toplumsal durumu da farklı olabilir; iyi söz ölçüsü odak âyetin tek amacı diye sunulmaz.

Kapanma imgesi, engeli kaldırma ve hâli değiştirme yetkisinin kimde olduğu sorusuna geçiş sağlar. Kendilerine yönelinen varlıkların {ar:يَمْلِكُونَ, tr:yamlikūna, gloss:güç yetirirler} sözüyle güç sahibi olmadıkları belirtilir; {ar:كَشْفَ, tr:kashfa, gloss:giderme} zararı ya da engeli kaldırmayı, {ar:تَحْوِيلًا, tr:taḥwīlan, gloss:dönüştürme} ise hâli değiştirmeyi adlandırır (17:56). Bu ayrım, {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş}ın erişimi kısıtlayan ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}in geçişi durduran imgelerini bir fail sorusuna bağlar: engeli tasarlamak, onu kaldırma ya da biçimi değiştirme yetkisini vermiyor. Bu yankı yalnızca bu karşılaştırmaya aittir; 17:56'nın güçsüz varlıklardan söz ettiği ve dönüşü doğrudan açıklamayabileceği sınırı korunur (17:56).

Yetki ile kuşatmanın kapsamı farklı yönler açar. İnsanları kuşattığını bildiren {ar:أَحَاطَ بِالنَّاسِ, tr:aḥāṭa bi-n-nāsi, gloss:insanları kuşattı} ifadesi, erişimi {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} ve {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} ile ölçülen maddi direncin ötesine taşır (17:60). Böylece odaktaki kapanma imgesi daha geniş bir insan kuşatması karşısında yerini bulur. Aynı bağlamdaki {ar:فِتْنَةً, tr:fitnatan, gloss:sınama} ise insanlara yönelmiş sınamayı adlandırır (17:60); bu ayrı çağrışım demiri imgesel olarak sınanan bir malzeme hâline getirir. Kuşatma kapsamı genişletirken, sınama demire yeni bir rol verir; bu temas gerçek bir metal deneyi, dövme ya da fırın sahnesi değildir.

Başka yaratılış karşılaştırmaları aynı itirazı farklı ölçülerde sürdürür. Kemik ve ufalanmış kalıntılardan dönüş sorusu yeniden belirir (17:98), toprağa karışma da yenilenmeye yöneltilen kuşkunun zeminidir (32:10). Gökleri ve yeri yaratanın benzerlerini yaratabilmesi (17:99), yaratmayı başlatıp yinelemesi (30:27) ve ilk yaratılışta acizlik bulunmadığı cevabı (50:15), dönüş sorusunu ilk var edişin kudretiyle birlikte düşünmeye açar. Bu ilişkiler odak sözcüklerle biçimbilgisel eşleşme değil, yaratma ve yeniden yaratma çevresindeki anlam yakınlıklarıdır. Bu geniş karşılaştırmada {ar:حِجَارَةً, tr:ḥijāratan, gloss:taş} itirazın tahayyül ettiği engeli, {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir} ise direnç çizgisinin sonunu gösterebilir. Sınır, yaratılışın gerçek kudretine değil, itirazın tasarlayabildiği maddi dirence aittir.

Taşın hem dayanıklı hem parçalanabilir oluşu, bedensel kalıntıdan göğe uzanan bir ölçek yankısı kurabilir: göğün parça parça düşürülmesi talebi bu maddi karşıtlıkla yan yana düşünülebilir (17:92). Böylece meydan okumanın tasavvur ölçeği bedenden göğe genişler. Bu yalnızca keşifsel bir karşılaştırmadır; Arapça ifade veya açık metin işareti bulunmadığından (17:92), ortak sözcük ya da kasıtlı gönderme ileri sürülmez.

</source_prose>
