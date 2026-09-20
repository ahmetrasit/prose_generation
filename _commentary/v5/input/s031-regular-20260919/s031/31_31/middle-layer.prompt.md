# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:31**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.middle.claims.json`

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
- Refer to source paragraphs as `31:31 ¶N`.

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

`(31:31 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:31",
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
        "citation": "(31:31 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_31/31_31.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_31/31_31.middle.claims.json \
  --ayah-ref 31:31
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_31/31_31.prose.editorial.tr.md`

<source_prose>
Âyet, “Gemilerin denizde Allah’ın nimetiyle yol aldığını görmedin mi?” diye sorar. Bu seyrin Allah’ın işaretlerinden bir bölümünü insanlara göstermeye yöneldiğini, bu olayda çok sabredenler ve çok şükredenler için işaretler bulunduğunu bildirir.

Olumsuz soru, gemilerin geçişini yadsımak yerine muhatabın dikkatini göz önündeki olaya çevirir. {ar:أَلَمْ تَرَ, tr:ʾa-lam tara, gloss:görmedin mi} sorusu, {ar:أَنَّ, tr:ʾanna, gloss:ki} ile gemilerin denizde yol alışını görme fiilinin önüne koyar. Böylece {ar:تَرَ, tr:tara, gloss:görmek} hem seyri gözle fark etmeye hem de bu olayın neyi gösterdiğini kavramaya açılır; ardından gelen gösterme fiili bu düşünme payını genişletir.

{ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} su üstünde yol alan gerçek gemileri adlandırır; gövde, yolculuğun maddi merkezidir. Sözcük tek bir gemiyi, birden fazlasını ya da gemileri topluca gösterebilir; sayı kesinleştirilmez. Ardından gelen dişil tekil {ar:تَجْرِى, tr:tajrī, gloss:yol alır}, olası gemileri tek bir seyir sahnesinde toplar. Muzâri biçim, tamamlanmış bir yolculuk sonucundan çok deniz güzergâhında süren hareketi öne çıkarır. İlk {ar:فِى, tr:fī, gloss:içinde} fiziksel ortamı kurar: gemiler geniş bir su kütlesinin içinden geçer. Deniz adı seyrin fiziksel ufkunu geniş bir su kütlesi olarak kurar; ayet geminin türünü ya da denizin derinlik, direnç ve tehlike gibi niteliklerini ayrıca belirlemez.

## Güzergâhın çevresi

Gemi anlamı korunurken gemi adının daha uzak bir sözlük çağrışımı da açılır: daire, dönüş ve göksel yörünge hareketi (31:29). Bu çağrışımı geceyle gündüzün birbirine geçmesini ve güneşle ayın belirlenmiş bir süreye doğru akışını anlatan sahne tetikler (31:29): {ar:ٱلشَّمْسَ وَٱلْقَمَرَ كُلٌّ يَجْرِىٓ إِلَىٰٓ أَجَلٍ مُّسَمًّى, tr:ash-shams wa-l-qamar kullun yajrī ilā ajalin musamman, gloss:güneş ile ayın belirlenmiş bir süreye doğru akışı}. Odaktaki {ar:تَجْرِى, tr:tajrī, gloss:yol alır} da güzergâh boyunca akıp ilerlemeyi anlatır. Buradaki bağ sözlük çağrışımıdır: iki ayetteki sözcükler arasında kök ya da biçim özdeşliği kurulmaz (31:29). Gemi kendi deniz rotasında kalırken, bu süreli göksel devinim onu daha geniş bir düzen içindeki yerel ve sınırlı rota gibi duyurur (31:29).

Bu düzen, değişen hareketi yıkıcı savrulmaya bırakmayan bir istikrar düşüncesi de açar. Yeryüzünü sarsılmaktan koruyan dağlar sabit dayanaklardır (31:10); gece-gündüz değişimi ve güneşle ayın süreli devinimi de göksel hareketi bir düzene bağlar (31:29). Böylece {ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} koşullar içinde ilerleyen, hareketi sınır ve dayanaklarla çevrili bir taşıyıcı olarak duyulur. Bu ilişki gemiye demir atmışlık veya gök cisimleriyle özdeşlik yüklemez; odak ayet geminin sallandığını da anlatmaz.

Odaktaki deniz sözü ({ar:ٱلْبَحْرِ, tr:al-baḥri, gloss:deniz}) sonraki sahnede yalnızca güzergâhın zemini olarak kalmaz (31:32). Dalgaların yolcuları gölgelikler gibi örtmesi, onu hem taşıyan hem tehdit edebilen hareketli bir ortama dönüştürür (31:32): {ar:وَإِذَا غَشِيَهُم مَّوْجٌ كَٱلظُّلَلِ, tr:wa-idhā ghashiyahum mawjun ka-l-ẓulal, gloss:dalgalar onları gölgelikler gibi kapladığında}. Odaktaki {ar:تَجْرِى, tr:tajrī, gloss:yol alır} geminin süren rotasını anlatırken, bu dalga sahnesi yanına bağımsız bir su devinimi ekler (31:32). İki hareket aynı deniz ritminde duyulur; odak fiilinin katılımcısı gemi, dalgalar ise ayrı sahnenin devinimidir (31:32). {ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} sözcüğünün kökten ayrı bir kullanımı da kabaran, çalkalanan ve ileri geri devinen suyu adlandırır; dalga imgesi bu uzak anlamı çağırır (31:32). Böylece gemi deniz taşıyıcısı, dalga da onu kuşatan su hareketi olarak kendi anlamında kalır. 31:32'deki kriz odaktaki seyrin parçası değildir; bu temas nimetle sürdürülen geçişi tehlikesizliğin garantisi değil, tehlike olasılığıyla birlikte duyurur (31:32).

Bu geçişi Allah’ın nimetine bağlayan {ar:بِ, tr:bi, gloss:ile} edatı hem sebep/vasıta ilişkisine hem de nimetle nitelenen bir duruma elverir. Bu iki bağlantı açık kalır; yelken gibi tek bir fiziksel araca sabitlenmez. Tekil {ar:نِعْمَتِ ٱللَّهِ, tr:niʿmati Allāhi, gloss:Allah’ın nimeti}, Allah’ı iyiliğin kaynağı olarak adlandırır ve süren hareketi tek bir işleyen nimet altında toplar. Elverişli yaşam ve iyi oluş anlamı, seyrin önünü açan koşulu duyurur; nimet taşınan nesne değil, geçişi mümkün kılan yarardır. Ayet bu yararın yolcuya ulaştığını ve seyrin sürdüğünü gösterir; yardımları rüzgâr, kaldırma kuvveti, ustalık ya da güvenlik gibi fiziksel mekanizmalara ayırmaz. Nimet sözü bağış veya faydayı da adlandırır; yolculuğun nimete bağlanması ve sonraki şükür alıcısı geçişi alınan iyilik gibi duyurur, ancak geminin kendisi açıkça alıcı gösterilmez. Ardından gelen {ar:ءَايَٰتِهِۦٓ, tr:āyātihi, gloss:O’nun ayetleri} üzerindeki iyelik eki aynı kaynağa döner: geçişi mümkün kılan nimetle gösterilen işaretler aynı ilahî ilişki içindedir.

İki uzak sözlük kullanımı hareketi ve nimeti başka yönlerden renklendirir. {ar:تَجْرِى, tr:tajrī, gloss:yol alır} sürekli verilen geçimlik ya da kalıcı yarar anlamıyla seyrin süren iyilik imgesini açar; {ar:نِعْمَتِ, tr:niʿmati, gloss:nimet} sözü ise güneyden esen, yumuşak ve nem taşıyan belirli bir rüzgâr için ayrı ve uzak bir kullanıma sahiptir. Bu ikinci temas nazikçe taşıyan görünmez bir kuvvet imgesi verir. Geçimlik çağrışımı gerçek ücret veya ödeme bildirmez; rüzgâr çağrışımı da nimeti hava olayına dönüştürmez. Odak ayet rüzgârın yönünü, nemi, hava durumunu ya da belirli bir fiziksel sebebi tanımlamaz.

## Görmek ve işaretler

Soru önce tek bir muhataba yönelirken amaç bildiren {ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} ettirgen fiili Allah’ın çoğul bir insan grubuna görme imkânı açtığını söyler. Böylece bakış gemi seyrinden, onun açığa çıkardığını kavramaya uzanır. Bu amaç her bir kişinin aynı kavrayışa erişeceğini garanti etmez. {ar:مِّنْ, tr:min, gloss:bir kısmını} edatı ilahî işaretlerin bir bölümünü seçer. {ar:ءَايَٰتِهِۦٓ, tr:āyātihi, gloss:O’nun ayetleri} görünen belirti, delil veya alamet anlamıyla deniz sahnesini yalnız seyredilen manzara olmaktan çıkarıp okunabilir bir işarete dönüştürür. Yolculuk, işaretlerin tamamını tüketmeyen gerçek bir örnek olarak kalır.

{ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} gösterme bağı, odaktan bağımsız iki sahneyle de karşılaşır: Musa’ya büyük işaretlerin gösterilmesi bu ilişkiyi başka bir bağlamda belirginleştirir (20:23); denizde ilerleyen gemilerin ilahî lütfu arama ve şükretmeyle yan yana gelişi ise ayrı bir seyir sahnesi kurar (45:12). Bu iki bağlam görme ve lütufla ilgili farklı amaçlar taşır (20:23) (45:12). Birlikte, gemi seyrini yalnız yer değiştirme değil, işarete ve nimete yönelen bir görünüş olarak okumaya alan açarlar (20:23) (45:12). Bu görünüş her yolcunun işaretleri tanımasını ya da her yolculuğun bakışını değiştirmesini zorunlu kılmaz (20:23) (45:12).

Gemi ve deniz anlatımından sonra gelen {ar:فِى ذَٰلِكَ, tr:fī dhālika, gloss:bunda} ifadesindeki ikinci “içinde”, fiziksel deniz ortamından farklı, soyut bir içerme ilişkisi kurar: işaretler gemi, deniz, nimet ve gösterme dizisinin bütününde bulunur. {ar:ذَٰلِكَ, tr:dhālika, gloss:bunda} bu olayları tek bir bakış nesnesi olarak toplar. Ardından {ar:إِنَّ, tr:ʾinna, gloss:şüphesiz} yeni bir ana cümle açarak işaretlerin bu olayda bulunduğunu bildirir. Gecikmiş isimdeki vurgu lâmı {ar:لَءَايَٰتٍ, tr:la-āyātin, gloss:elbette işaretler} bu bildirimi güçlendirir; iyelik eki taşımayan belirsiz çoğul da işaretlerin çeşitli yönlerini açık bırakır. Daha önceki {ar:مِّنْ ءَايَٰتِهِۦٓ, tr:min āyātihi, gloss:O’nun işaretlerinden bir kısmı} belirli ilahî işaretlerin bir bölümünü seçerken, sondaki ifade sahnedeki hareket, deniz ortamı ve nimetin farklı yönlerini işaret olarak düşündürür. Bu farklı yönler tam bir liste halinde sabitlenmez; işaret kümesinin sonsuz olduğu ya da herkesçe aynı biçimde okunduğu da ileri sürülmez.

İşaretlerin alıcısına yönelen son lâm, gösterme amacındaki lâm’dan farklı olarak hedefi belirtir. {ar:لِّكُلِّ, tr:li-kulli, gloss:her biri için} içindeki {ar:كُلِّ, tr:kulli, gloss:her}, {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} ve {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} nitelemelerinin ayrı ayrı çizdiği alıcı sınıflarındaki her kişiyi kapsar. Böylece ayetin kapsamı koşulsuz bütün insanlara değil, bu niteliklerle tarif edilenlere yönelir. Yoğun biçimli ṣabbār, sarsılma ve yakınma dürtüsüne karşı kendini tutup sebatı sürdürmeyi anlatır. Süren deniz geçişi ve onun gösterdiği işaretler dikkati korumaya zemin sağlar; bu sabır belirli bir kriz ya da deniz tehlikesine bağlanmaz. Shakūr ise iyiliği ve kaynağını tanıyıp kabul eden süreğen karşılığı taşır. Allah’ın nimeti şükrü alınan iyiliğin tanınmasına bağlar; ayet belirli bir sözlü karşılık ya da nimet miktarı belirlemez. Böylece fiziksel görme, işaretin anlamını tanımaya açılır; bu sahne başkalarının gemiyi göremediğini söylemez.

## Karşılığın zamanı

Sabır ve şükür alıcısının hangi koşullarda durduğunu, ayrı deniz sahnesinde birbirine eklenen dalgaların yolcuları gölgelikler gibi örtmesi belirginleştirir (31:32). Tehlike içindekiler Allah’a yönelip dini O’na özgüleyerek yalvarır; güvenli kıyıya kurtarılmalarının ardından işaretleri inkâr eden vefasız ve nankörlerden söz edilir (31:32): {ar:فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:fa-lammā najjāhum ilā l-barr, gloss:onları karaya kurtardığında}. Bu sıra, odaktaki {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} niteliğini sarsıntı ve yakınma dürtüsüne karşı sebat; {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} niteliğini ise ihtiyaç geçtikten sonra da nimeti ve kaynağını tanıma yönünde duyurabilir (31:32). Şükrün sözde ve davranışta görünme imkânı da bu karşılaşmada belirir (31:32). Sabır ve şükür böylece tehlike sürerken dayanma ve güvenlik geri geldiğinde iyiliği tanıma boyunca duyulabilir (31:32). Bu bağlamsal okuma iki niteliği bu anlara hapsetmez; belirli bir karşılık buyurmaz ve herkesin böyle bir kurtuluş yaşadığını varsaymaz (31:32).

Başka bir yolculukta elverişli rüzgârın ardından fırtına çıkar, dalgalar yolcuları çevreler, onlar içtenlikle Allah’a yönelir, sonra kurtarılıp şükrederler (10:22). Bu sahne odaktaki {ar:ٱلْبَحْرِ, tr:al-baḥri, gloss:deniz} ve {ar:تَجْرِى, tr:tajrī, gloss:yol alır} fiiline değişen koşullar boyutunu ekler: deniz yalnızca yol değil, şartları tersine dönebilen ortamdır; {ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} de kendi ortamını yönetmeyen, güvenli geçişi sürdüren koşullara bağlı bir taşıyıcıdır (10:22). İşaret ve {ar:بِنِعْمَتِ ٱللَّهِ, tr:bi-niʿmati Allāhi, gloss:Allah’ın nimetiyle} ilişki, böylece yalnız kesintisiz güvenli harekette değil, tehlikeden esenliğe dönüşte de okunabilir (10:22). Bu karşılaşma odaktaki geminin fırtına yaşadığını ileri sürmez ve nimeti belirli bir rüzgârla özdeşleştirmez (10:22).

Başa gelene karşı sabır ile kararlılık isteyen eylemlerin yan yana gelişi, sabrı edilgin bekleyişten daha etkin bir duruş olarak da düşündürür (31:17). {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} sözcüğündeki yoğun faʿʿāl biçimi baskı altında yönünü koruyup davranmayı sürdürme yönünü açar (31:17). Hikmetle birlikte gelen şükür buyruğu, şükredenin yararının kendisine döndüğünü ve nimeti örtenin karşıtlığını belirtir (31:12). {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} sözcüğünün süreklilik taşıyan faʿūl biçimi şükrü bilinçli ve içten olduğu kadar sonuç doğuran bir karşılık olarak duyurur (31:12). Bu iki bağlam, etkilenme altında davranış sürdürme ile alınan nimetin kişiyi dönüştürmesi arasında olası bir geri besleme düşündürür (31:17) (31:12). Bu bağlantı ihtiyatlı bir çıkarımdır, sabit zaman sırası değildir; şükrü kişisel kazanca indirgemez ve odak ayetin muhataplarını nankör diye nitelemez (31:17) (31:12).

Odaktaki {ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} gösterme amacı görünür işaretleri tanımaya açar; alımlama farklı karşılıklar alabilir. Oyalayıcı söz dikkati başka yöne çeker (31:6); ayetler okunurken yüz çevirme, sanki işitmemiş gibi kalma ve kulaklarda ağırlık imgesi yönelişin kesilmesini, kavrayışın kapanmasını ve duyusal engeli anlatır (31:7). Bu sahneler görmeyi sağlama amacının kendiliğinden tanımayı zorunlu kılmadığını gösterir (31:6) (31:7). Dalgadan kurtuluşun ardından işaretleri reddeden vefasız nankörlerden de söz edilir (31:32). Odaktaki {ar:كُلّ, tr:kull, gloss:her} ile bu ayrı sahnedeki “her” (31:32) kapsam ve dilbilgisel yapı bakımından farklıdır; bunlar birbirini dışlayan insan sınıfları değildir, işaretleri gören herkesin ret gösterdiği de söylenmez. Karşılıkların nedenleri açıklanmaz (31:6) (31:7) (31:32). {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} dikkati açık tutabilecek bir karşılık sunar; sabır yalnız dikkatle eşitlenmez, şükür de nimeti tanıma olarak kalır.

Şükür alıcısına dair uzak ve biçimce farklı bir sözlük çağrışımı, kısmi gösterimle buluşur. {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} sözcüğünün ayrı bir kullanımı, az bir girdiyi yeterli bulup onunla belirgin biçimde gelişmeyi çağrıştırabilir. {ar:نِعْمَتِ ٱللَّهِ, tr:niʿmati Allāhi, gloss:Allah’ın nimeti} ve {ar:مِّنْ ءَايَٰتِهِۦٓ, tr:min āyātihi, gloss:O’nun işaretlerinden bir kısmı} ifadesiyle kurulan temas, sınırlı bir görünüşün tanıma için yeterli olabileceğini düşündürür. Bu uzak imge, işaretleri küçük ya da eksik göstermez; beslenme, yağmur veya fiziksel büyüme sahnesi de kurmaz. Tanıma, iyiliğin miktarını küçültmek değil, onu ve kaynağını fark etmektir.

Deniz bolluğu da miktar ile gerçekten alınan yararın ayrımını görünür kılan uzak bir çağrışım açar. {ar:ٱلْبَحْرِ, tr:al-baḥri, gloss:deniz} geniş su kütlesini adlandırırken aynı söz ailesindeki başka bir kullanım, sudan içse bile kanmamayı anlatır. Görme ve gösterme fiilleri içme eylemi değil, işaretle karşılaşmadır. Böylece geniş suyun çevrede bulunmasıyla yararın alınıp tanınması ayrışır. {ar:نِعْمَتِ ٱللَّهِ, tr:niʿmati Allāhi, gloss:Allah’ın nimeti}, deniz ve {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} alıcısı birlikte okunduğunda, iyi oluş çevredeki bolluğun yanı sıra tanınıp alınan fayda olarak duyulur. Bu uzak imge odak sahnesine gerçek susuzluk ya da yoksunluk yüklemez, nimeti su veya besinle özdeşleştirmez ve herhangi bir kişiyi işaretten yoksun saymaz.

## Geniş anlam alanı

Odaktaki deniz gerçek su ortamı olarak kalırken başka bir maddi sahneyle anlam alanı genişler (31:27). Ağaçlar kalem, deniz yazıyı besleyen bir uzantı ve yedi deniz daha eklense bile Allah’ın sözlerinin tükenmeyeceği anlatılır (31:27): {ar:أَقْلَٰمٌ, tr:aqlām, gloss:kalemler}, {ar:ٱلْبَحْرُ يَمُدُّهُۥ, tr:al-baḥru yamudduhu, gloss:deniz onu artırıp beslese}, {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥur, gloss:yedi deniz} ve {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu Allāh, gloss:Allah’ın sözleri}. Kalem, söz ve çoğaltılan su, anlamın maddi ortamını kurar (31:27). Bu ayrı yazı sahnesi geniş su ve görünür işaretlerle buluşunca gemi yolculuğu, karşılaşılabilen ama tek bir geçişte tüketilemeyen daha geniş bir işaret alanından geçer (31:27). Böylece odaktaki deniz metne dönüşmeden, bu sahne Allah’ın sözlerinin tükenmezliği vurgusuyla yan yana durur (31:27). Tek bir sefer bu anlam alanını tüketmez (31:27).

Gemi seyrinin gösterdiğiyle bilinemeyen gelecek arasındaki sınır, Saat’in bilgisi, yağmurun inişi, rahimlerde olan ve kişinin yarın ne kazanacağı ya da nerede öleceği üzerinden çizilir (31:34): {ar:وَمَا تَدْرِى نَفْسٌ مَّاذَا تَكْسِبُ غَدًا, tr:wa-mā tadrī nafsun mādhā taksibu ghadan, gloss:hiçbir kişi yarın ne kazanacağını bilmez} ve {ar:وَمَا تَدْرِى نَفْسٌۢ بِأَىِّ أَرْضٍ تَمُوتُ, tr:wa-mā tadrī nafsun bi-ayyi arḍin tamūtu, gloss:hiçbir kişi hangi yerde öleceğini bilmez}. Allah bu gizli gerçeklikleri bütünüyle bilir (31:34). Odaktaki {ar:تَرَ, tr:tara, gloss:görmek} ve {ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} görünür işaretleri fark etmeye ve düşünmeye yöneltir; yarını öngörme, kazancı denetleme ya da ölüm yerini bilme kudreti vermez (31:34). Bu işaretler yön gösterir, gelecek hakkında tahmin sunmaz (31:34). Belirsiz gelecek, {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} için beklerken kendini tutma yönünü de çağrıştırabilir (31:34); bu çağrışım sabrı beklemeye indirgemez, özdenetimli duruşu genişletir.

Denizde yol alan {ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} kendisi de işaretler arasında sayılır (42:32). Odaktaki seyir gemiyi görmeye açılan taşıt olarak kurar; bu ayrı sahnede gemi ayrıca gösterilen işarettir (42:32). {ar:تَجْرِى, tr:tajrī, gloss:yol alır} süren rotayı, {ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} görme amacını anlatır; iki bağlantı birlikte gemiyi hem taşıt hem işaret taşıyan nesne olarak duyurur (42:32). Rüzgârın durup gemilerin deniz yüzünde hareketsiz kaldığı sahnede de aynı {ar:صَبَّارٍ, tr:ṣabbārin, gloss:çok sabreden} ve {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} çiftiyle işaretlerden söz edilir (42:33). Böylece gemi hareket ederken de dururken de görünür işaret olarak kalır (42:33). Bu paralellik odaktaki gemiler için bir öngörü sunmaz (42:33).

Görünen seyir, onu taşıyan bütün destekleri tek başına açığa çıkarmaz (31:20). Göklerde ve yerde olanların insan için kullanıma verilişiyle birlikte, odaktaki {ar:نِعْمَتِ ٱللَّهِ, tr:niʿmati Allāhi, gloss:Allah’ın nimeti} sözüyle aynı kelime ailesinden gelen nimetlerin kuşatıcı biçimde ulaştırılması, hem görünür hem gizli yanlarıyla anılır (31:20). Odaktaki {ar:لِيُرِيَكُم, tr:li-yuriyukum, gloss:size göstermesi için} yapısı geminin görünür hareketini yüzeyinden fazlasını düşündüren bir olaya açar; {ar:بِنِعْمَتِ ٱللَّهِ, tr:bi-niʿmati Allāhi, gloss:Allah’ın nimetiyle} seyir de geçişi mümkün kılan yararı görünür hareketin altındaki destek gibi duyurur (31:20). Bu paralellik gemiyi daha geniş bir düzenin görünür yüzü ve gizli koşullara bağlı taşıyıcısı olarak konumlandırır (31:20); hangi gizli nedenlerin işlediğini tek tek belirlemez.

Başka bir taşıma görüntüsünde anne çocuğunu zayıflık üstüne zayıflık içinden taşır; ardından Allah’a ve anne-babaya şükür gelir (31:14). {ar:ٱلْفُلْكَ, tr:al-fulka, gloss:gemi/gemiler} denizde başkalarını taşıyan aracı adlandırır; anne imgesi bu geçişi yolcunun tek başına kurmadığı bir taşınma ve destek ilişkisi olarak duyurur (31:14). Zayıflık üstüne zayıflık taşıyanın üstlendiği maliyeti, gemi-yolcu benzetmesi de yolculuğun altındaki emek ve bağımlılığı görünür kılar (31:14). {ar:شَكُورٍ, tr:shakūrin, gloss:çok şükreden} niteliği böylece varışın yanı sıra geçişi mümkün kılan desteğe yönelen şükrü de açar (31:14). Bu benzerlik gemiyi anneyle özdeşleştirmez, yolcuları zayıf diye nitelemez ve şükrü aile ilişkisine daraltmaz (31:14).

</source_prose>
