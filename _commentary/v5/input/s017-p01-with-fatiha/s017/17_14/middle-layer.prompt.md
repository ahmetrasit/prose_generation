# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:14**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.middle.claims.json`

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
- Refer to source paragraphs as `17:14 ¶N`.

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

`(17:14 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:14",
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
        "citation": "(17:14 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_14/17_14.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_14/17_14.middle.claims.json \
  --ayah-ref 17:14
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_14/17_14.prose.editorial.tr.md`

<source_prose>
## Buyruk ve Nesne

17:14 muhataba önce {ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:Kitabını oku} buyruğunu yöneltir; ardından {ar:كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā bi-nafsika al-yawma ʿalayka ḥasīban, gloss:Bugün kendi nefsin sana hesap görücü olarak yeter} hükmünü getirir: “Kitabını oku; bugün kendi nefsin sana hesap görücü olarak yeter.” Okunacak nesne kişinin kendi yazılı kaydıdır; onu okuyacak kişiyle hesabı görülen kişi de aynı muhataptır. Ayet böylece okuma işini hesaptan önce kurar ve iki önermeyi tek bir kişisel sahnede yan yana tutar.

{ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} ikinci tekil kişiye yönelmiş bir emirdir; muhatap doğrudan işe çağrılır. {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} sözcüğünün sonundaki ikinci kişi eki de kitabın sahibini bu muhatap olarak belirler. Emir muhatabı açıkça gösterir, konuşanı ise adlandırmaz. Ses bakımından hemze eşiğindeki kesikli başlangıç, hemen ardından gelen kitap sözüyle anlatımdan buyruğa sert dönüşü duyurur; bu işitsel etki ayetin kendi söyleyişine aittir, belli bir tilavet kaydını tarif etmez.

{ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} okuma, tilavet ve tilavet öğretme alanlarına uzanabilen geniş bir buyruktur. Belirtme hâlindeki iyelikli {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} açık nesne olarak bu eylemi muhatabın kendi yazılı kitabına yöneltir; geniş fiil alanı böylece bu cümlede somut bir hedef kazanır. Fiil-nesne birimi tamamlandığında {ar:كَفَىٰ, tr:kafā, gloss:yeter} yeni bir önerme başlatır. Kendi nefsini yeterli taraf olarak gösteren {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} tümlecinin bağlaçsız biçimde hemen ardından gelişi iki önermeyi yakınlaştırır, cümle sınırını ise korur.

Odaktaki {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} emri, aynı emir kipinin geçtiği 96:1 ve 96:3’le yankılanır: {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} (96:1, 96:3). Bu yankı kişisel kitabı daha geniş bir buyurulmuş okuma çerçevesine taşır; ortak emir okuma temasını genişletirken kitapların özdeşliğini ya da odaktaki biçimin biçimbilimini belirlemez (96:1, 96:3). Böylece 17:14’teki kişisel kayıt, sahibinin okuyacağı nesne olarak kendi sahnesinde kalır.

Bu sahiplik düzeninin toplu bir karşılığı 17:71’de görülür: herkese kendi kitabı verilir ve onlar {ar:يَقْرَءُونَ كِتَٰبَهُمْ, tr:yaqraʾūna kitābahum, gloss:Kitaplarını okurlar} diye anlatılır (17:71). Bu dağılım herkesi kendi kaydının okuyucusu yapar; başkasının kitabını okuma sahnesi burada kurulmaz (17:71). Böylece sahiplik yankısı kişisel buyruğu destekler, ancak 17:71 odaktaki {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} biçimbilimini ayrıca açıklamaz.

Sahiplik, başkalarına seslenerek okuma çağrısı yapmayla bağdaşır: 69:19’da kitabını alan kişi {ar:ٱقْرَءُوا۟ كِتَٰبِيَهْ, tr:iqraʾū kitābiyah, gloss:Kitabımı okuyun} diye başkalarını kendi kaydını okumaya çağırır (69:19). Bu tek sahne kişisel mülkiyetle kamusal okunabilirliği bir araya getirir (69:19). 69:25 ve 84:10’daki farklı karşılanışlar bu örneğin sınırını korur: buradaki çağrı her kitabı kamusal kılmaz ve odaktaki kişinin sonucunu önceden belirlemez.

Okunacak kitabın yakın anlatıdaki yeri, 17:13’te kişiye ait {ar:طَٰٓئِرَهُۥ, tr:ṭāʾirahu, gloss:kuşunu} {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} ve {ar:فِي عُنُقِهِۦ, tr:fī ʿunuqihi, gloss:boynunda} sözleriyle kişinin boynuna bağlandığında açılır (17:13). {ar:طَٰٓئِرَهُۥ, tr:ṭāʾirahu, gloss:kuşunu} kuş olarak okunabileceği gibi kişiye taşınmış bir işaret ya da kader alameti de olabilir; boyna bağlanma sorumluluğu bedene yakın ve kişisel kılar (17:13). Ardından {ar:نُخْرِجُ, tr:nukhriju, gloss:çıkarırız}, {ar:يَلْقَىٰهُ, tr:yalqāhu, gloss:onunla karşılaşır} ve {ar:مَنشُورًا, tr:manshūran, gloss:açılmış halde} bir hareket dizisi kurar: çıkarma kaydı görünür kılar, karşılaşma sahibini onun önüne getirir, açılmışlık da yazılı içeriği sergiler (17:13). Odaktaki okuma buyruğu bu açığa çıkan kayıtla karşılaşmayı incelemeye taşır (17:13, 17:14). 17:13’teki {ar:يَوْمَ الْقِيَٰمَةِ, tr:yawma al-qiyāma, gloss:diriliş gününde} hesabın belirleyici zamanını kurar. Bu bağlantı iki ayetin işaretlerini yan yana getirir; kuş ya da taşınan işaret ile kitap arasındaki ilişki aynı fiziksel nesnenin dönüşümü olarak belirlenmiş değildir (17:13, 17:14).

## Kayıt ve Hesap

Karşılaşmanın yazılı nesnesi olan {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını}, yazılmış ya da yazma ve kopyalama işleminin ürünü olan kişisel kitabı anlatır. Aynı kelime ailesinin başka bir kolu bir şeyi fiziksel ya da topluluk düzeyinde daha büyük bir bütüne katar. Bu birleştirme işlemi, odaktaki okuma, kişisel benlik ve {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayım kapasitesiyle temas ettiğinde dağınık eylemleri tek ve sayılabilir bir hesap halinde duyurur: okuma içeriği açar, birleştirme onu bütünleştirir, sayım ise düzene koyar. Bu katkı kitabın yazılı nesne anlamını ve {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} fiilinin okuma anlamını koruyarak hesabın nasıl bir araya geldiğini gösterir.

Bu birleşik hesabın yerel yeterliğini olağan {ar:كَفَىٰ, tr:kafā, gloss:yeter} hükmü kurar. Ardından gelen {ar:بِ, tr:bi, gloss:ile edatı}, genitif durumdaki {ar:نَفْسِكَ, tr:nafsika, gloss:nefsin} adını yönetir; bu işaretli tümleç kişiyi doğrudan nesne değil, failimsi bir vurguyla yeterli taraf olarak öne çıkarır, araçlık okuması ise ikincil kalır. “Bu sana yeter” kuruluşu bu bağlantıda muhatabın kendi hesabına gereksinimi karşılar; yeterlik bütün ihtiyaçlara genellenmez. Fiilin tamamlanmış biçimi ilişkiyi kurulmuş ve geçerli olarak sunar. Dolayısıyla burada {ar:كَفَىٰ, tr:kafā, gloss:yeter} hesabı görmeye yeterli oluşu taşır; koruma ya da uzaklaştırma yönü bu kullanıma katılmaz.

Bu ilişkinin zamanını {ar:ٱلْيَوْمَ, tr:al-yawma, gloss:bugün} belirler: sözcük “bugün” der ve belirli tanımlığıyla bağlamca bilinen güne işaret eder. Cümlede {ar:كَفَىٰ, tr:kafā, gloss:yeter} ile {ar:عَلَيْكَ حَسِيبًا, tr:ʿalayka ḥasīban, gloss:aleyhine hesap gören} arasına yerleşmesi yeterlik hükmünü hesap rolüyle aynı vakte bağlar, rolün adını da sona bırakır. 17:13’teki diriliş günü bu vakti hesabın belirleyici zamanı olarak duyurur (17:13). Ortak yawm yüzeyi ve hesap bağlamı, Fâtiha 1:4’teki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi d-dīn, gloss:Karşılık gününün sahibi} ifadesine doğru daha geniş bir karşılık günü ufku açar (1:4). Bu yankı ortak yüzey ve bağlamla sınırlıdır; doğrudan alıntı, özdeşlik ya da biçimbilim bağı kurmaz.

Geciken rol adı geldiğinde {ar:عَلَيْكَ, tr:ʿalayka, gloss:senin aleyhine} muhatabı hesabın sorumluluk hedefi olarak gösterir. Hedefin {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} rolünden önce gelişi, okura önce kimin hesaba çekildiğini, sonra hangi kapasitenin yeter sayıldığını duyurur; söz dizimindeki gerilim buradadır, yapının dilbilgisi açıktır. Son sözcük, faʿīl kalıbındaki belirsiz mansup niteleyici olarak tek bir sayma eyleminden çok hesap görebilen bir nitelik ve kapasiteyi belirtir. Böylece {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} yeterliğin hangi işte yeterli olduğunu adlandırırken, ayet bu noktada sonucun ne olacağını söylemez.

İkinci kişi eki {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını}, {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ve {ar:عَلَيْكَ, tr:ʿalayka, gloss:senin aleyhine} biçimlerinde aynı kişiyi üç rolde izler: kitabın sahibi, yeterli taraf ve hesabın hedefi. Bu ekler rollerin sürekliliğini kurar; tek başına ahlaki bir sonuç bildirmez. Buradaki {ar:نَفْسِكَ, tr:nafsika, gloss:nefsin}, kaydı taşıyan ve hesapta bulunan bütün kişidir; içsel yetinin yanı sıra nefes ya da bedenli yaşam hafifçe duyulur, kan ve nazar anlamları ise bu bağlantıda etkin değildir.

Bu zamir zincirinin sesi de cümleyi başından sonuna taşır. {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını}, {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ve {ar:عَلَيْكَ, tr:ʿalayka, gloss:senin aleyhine} aynı “-ka” sesini yineleyerek kitabın sahibini, yeterli tarafı ve hesabın hedefini birbirine bağlar; {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} kapanışı bu yeterliğin kapasitesini adlandırır. Böylece son rol adı ilk {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} buyruğuna cevap verir: okuyan kişi kendi kitabını okur ve kendi hesabında yer alır.

Bu dilbilgisel bağ, okumayı edilgin bir bakıştan öz-denetim ilişkisine taşır: muhatap kendi kaydını okur, kayıtta temsil edilen kişi yine kendisidir ve hesap ona yönelir. “Denetim” imgesi bu rollerin buluşmasından doğar; {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} fiilinin sözlük anlamı okumadır. {ar:كَفَىٰ, tr:kafā, gloss:yeter} bu kişisel kayıt-okur-hesap devresinde muhatabı yeterli taraf yapar; bu yerel yeterlik başka ihtiyaçlar hakkında genelleme getirmez. Devrede başka bir insan muhatabın yerine okuyucu ya da hesaplayıcı olarak geçmez, ilahî yargı da bu kişisel tanıklık içinde korunur.

Bu devrede okuma, yalnızca hazır bir fiil listesini gözden geçirmek değil, dağınık eylemleri düzenli ve sayılabilir bir hayat hesabı halinde yeniden kurmaya katılmaktır. {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayım kapasitesi kitabı ve bütün kişiyi aynı hesapta buluşturur; sayım da bu bütüne sıra verir. Bu yeniden kuruluş, her eylemin ayrı ayrı listelendiği iddiasını taşımaz ve “toplamak” anlamı {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} fiilinin sözlük anlamına değil, okuma, kayıt ve sayım rollerinin etkileşimine aittir.

Yazılı kişisel kitabın yanında, {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} ailesinin bir şeyi hükme ya da yükümlülüğe bağlayıp yazıyla geçerli kılan ayrı bir kullanım kolu bulunur. {ar:عَلَيْكَ, tr:ʿalayka, gloss:senin aleyhine} sorumluluğu, {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} ise hesap rolünü belirginleştirince bu kol kayda bağlayıcı ve yargısal bir doku katar. Buradaki temas yazılı kitabı gerçek bir hukukî hükme çevirmeden, onun çevresindeki karar ağırlığını artırır; yazılı oluş tek başına bu özel kullanımı etkinleştirmez.

Kişisel kaydın ayrıntılı biçimde yoklanması 18:49’daki kitap imgesiyle somutlaşır: kitap {ar:لَا يُغَادِرُ صَغِيرَةً وَلَا كَبِيرَةً, tr:lā yugādiru ṣaghīratan wa-lā kabīratan, gloss:Ne küçük ne büyük hiçbir şeyi atlamaz} diye nitelenir, insanlar da {ar:وَوَجَدُوا۟ مَا عَمِلُوا۟ حَاضِرًا, tr:wa-wajadū mā ʿamilū ḥāḍiran, gloss:Yaptıklarını hazır bulurlar} deneni hazır bulur (18:49). Odaktaki yazılı {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} ve {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayımı bu ayrıntı imgesiyle buluştuğunda kayıt incelenebilir bir içeriğe dönüşür (18:49). Bu bağlantının katkısı içerik düzeyinde yoklanabilirliktir; 18:49’dan tek başına zaman ölçümü, yük devri ya da derecelendirilmiş sonuç çıkmaz.

{ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} için bazı kullanımlarda işi dikkatle ele alıp iyi biçimde yürütme anlamı da vardır. Bu sınırlı kol, 18:49’un ayrıntılı kayıt imgesine özenli inceleme katkısı ekler; burada kişiyi resmî bir denetçi yapmaz (18:49). Yeterlik ve hesap görmenin birlikte duruşu 33:39’daki {ar:كَفَىٰ بِٱللَّهِ حَسِيبًا, tr:kafā bi-llāhi ḥasīban, gloss:Allah hesap görücü olarak yeter} kalıbında da görülür (33:39). Bu paralellik odaktaki sayma ile yeterlik yönlerinin birlikte duyulmasını destekler; biçimbilim kanıtı oluşturmaz ve kökün bütün kullanımlarını aynı anda etkinleştirmez (33:39).

Kişisel kayıt, yalnızca işlenmiş eylemleri değil, alınan yönelişin neye dönüştüğünü de düşündürür. {ar:ٱلْقُرْءَانَ, tr:al-qurʾāna, gloss:Kur’an} tilaveti 17:9’da {ar:يَهْدِي, tr:yahdī, gloss:yöneltir} eylemiyle insanı {ar:أَقْوَمُ, tr:aqwamu, gloss:en doğru} olana yöneltir; ayet salih işler yapanlardan da söz eder: {ar:يَعْمَلُونَ الصَّالِحَٰتِ, tr:yaʿmalūna al-ṣāliḥāt, gloss:salih işler yaparlar} (17:9). Bu rehberliğin ardından gelen {ar:ٱقْرَأْ, tr:iqraʾ, gloss:oku} buyruğu ile kişisel {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını}, yönelişe verilen cevabı sonradan inceleme imkânı açar (17:9, 17:14). Bu bağlantı 17:9’daki tilavet ile 17:14’teki kişisel kitabı ayrı nesneler olarak tutar ve odak kaydın içeriğini yalnızca salih işlerle sınırlamaz (17:9, 17:14).

Yönelişin sonuçları 17:7’de yapan kişiye geri döner: iyi davranış ile zarar ayrı yönler olarak verilir ve ikisinin sonucu da yapanların kendilerine ulaşır; ayet bunu {ar:لِأَنفُسِكُمْ, tr:li-anfusikum, gloss:Kendi benliklerinize} ifadesiyle belirginleştirir (17:7). Odaktaki {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ve {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} ile temasında hesap, dışarıdan eklenmiş bir kredi-borç hanesinden çok eylemlerin yapan kişiye dönen etkilerini izler (17:7). Bu karşılık benzetmesi eylem-sonuç ilişkisini aydınlatır; 17:7 sonuçların odaktaki kitaba yazıldığını ayrıca söylemez.

17:11’de insanın şerri hayır ister gibi çağırması ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} diye nitelenmesi ilk hükmün nasıl şaşabileceğini gösterir: {ar:وَيَدْعُ الْإِنسَٰنُ بِٱلشَّرِّ دُعَاءَهُۥ بِٱلْخَيْرِ, tr:wa-yadʿu al-insānu bi-l-sharri duʿāʾahu bi-l-khayri, gloss:İnsan şerri hayır ister gibi çağırır} (17:11). Aynı kökün bir fiil kullanımı belirsiz olanı doğru sanmayı, özel bir kullanımı ise seçeneklerden birini yeğlemeyi anlatır; 17:11’deki acele çağrı bu tercih kaymasının somut yüzünü verir (17:11). Odaktaki {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayma ve hesap görme kapasitesidir; bu biçim kökün sanma ya da yeğleme kullanımlarını taşımaz ve ilk yargıyı yanılmaz yapmaz. Kalıcı {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} böyle bir dönüşü okunabilir kılabilir, ancak 17:11’in genel insan tasviri odaktaki kişiye özel bir hata yüklemez ya da kitabı açıkça bu hatayı düzeltmek için tanımlamaz.

17:12, gece ile gündüzü {ar:ٱللَّيْلَ وَالنَّهَارَ آيَتَيْنِ, tr:al-layla wa-al-nahāra āyatayn, gloss:Geceyi ve gündüzü iki işaret} olarak gösterir; yıllar sayılır, {ar:وَالْحِسَابَ, tr:wa-al-ḥisāba, gloss:Ve hesabı} anılır ve ayrıntılar birbirinden seçilir (17:12). Odaktaki {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören}, aynı kökün başka biçimiyle buluşarak birimlerin sayılabilirliğini ve ayrıntıların ayrışmasını öne çıkarır (17:12). Bu karşılaşma hesabı tek bir toplamdan çok düzenli, incelenebilir bir sıraya açar; odaktaki kitabın sayısal yöntemini belirlemez. Böylece gece-gündüz sayımı ölçülebilir düzen örneği sunarken, 17:14’teki {ar:ٱلْيَوْمَ, tr:al-yawma, gloss:bugün} 17:13’ün diriliş gününe bağlı kalır, güneş çevrimine dönüşmez (17:12, 17:13).

Kişisel kayıttan topluluk ölçeğine geçişte 17:4’teki {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:kitap}, İsrailoğullarının seyrini taşır: {ar:قَضَيْنَا, tr:qaḍaynā, gloss:hükme bağladık} ile belirlenen {ar:لَتُفْسِدُنَّ فِي الْأَرْضِ مَرَّتَيْنِ, tr:la-tufsidunna fī al-arḍ marratayn, gloss:Yeryüzünde iki kez bozgunculuk edeceksiniz} iki tekrarı görünür kılar (17:4). Bu topluluk ölçeğindeki yazılı örüntü, tarihsel gidişatı ve onun sonucunu izlenebilir kılar (17:4). Odaktaki kişisel kayıtla bağlantısı bu ölçekteki örüntüyle sınırlıdır: iki toplu davranış bireye yazgı yüklemez ve onun kitabını gelecek eylemlerin kehanetine dönüştürmez (17:4).

## Kişisel Sorumluluk

17:15 sorumluluğu yeniden tek tek kişiye döndürür: doğru yolu {ar:ٱهْتَدَىٰ, tr:ihtadā, gloss:yolunu bulan} kendi yararına bulur, {ar:ضَلَّ, tr:ḍalla, gloss:yolunu şaşıran} ise zararını kendisi taşır (17:15). Bu fiiller yönünü bulma ile yolu kaybetmeyi somut bir güzergâha dönüştürür (17:15). {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:Hiçbir yük taşıyan başkasının yükünü taşımaz} yükün taşıyıcısını aynı kişide tutar; ceza öncesindeki {ar:نَبْعَثَ رَسُولًا, tr:nabʿatha rasūlan, gloss:Bir elçi gönderelim} adımı sorumluluk sırasına bildirimi de ekler (17:15). Elçinin bu yeri hesap öncesi bildirimdir; 17:15 onu odaktaki kitabın iç işleyişi ya da satırı olarak tanımlamaz (17:15). Odaktaki {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} bu bağlamda sorumluluğun sahibini belirginleştirir; sayısal bir yöntem ya da kişisel kitabın içeriğini ise tanımlamaz (17:15).

35:18 aynı kişisel sorumluluk alanını, arınmanın yararını da arınan kişiye döndürerek genişletir (35:18). {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:Hiçbir yük taşıyan başkasının yükünü taşımaz} yük devrini kapatırken, {ar:وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِ, tr:wa-man tazakkā fa-innamā yatazakkā li-nafsihi, gloss:Arınan ancak kendi nefsine yarar} kişisel yararı vurgular (35:18). Böylece 35:18’deki yük ve arınma iki ayrı yönden aynı kişiye bağlanır; odaktaki {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} hesabın yeterliliğini kurar, arınma eylemini kendisi ileri sürmez.

Vekil meselesi, 17:2’de Musa’ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:kitap} ve {ar:وَكِيلًا, tr:wakīlan, gloss:vekil} edinmeme buyruğuyla ayrı bir bağlamda görünür (17:2). Bu kitabın bağlayıcı talimat yönü, odaktaki kişisel kayıt ve {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ile buluşunca hesabı bir başkasına bırakmama okumasını açar (17:2). Bu bağlantı vekil olarak görevi üstlenecek birini sınırlar; 17:2’nin kitabı odaktaki kayıtla aynı nesne ya da vahiy değildir, buyruğu da genel yardım, tanıklık ve aracılık biçimlerine yayılmaz.

Kişinin kendi hesabı, daha geniş bir bilme alanı içinde yer alır (17:17). 17:17’deki {ar:كَفَىٰ بِرَبِّكَ, tr:kafā bi-rabbika, gloss:Rabbin yeter} odaktaki {ar:كَفَىٰ بِنَفْسِكَ, tr:kafā bi-nafsika, gloss:Kendi nefsin yeter} kuruluşuyla aynı yapıyı bu kez Rabbe bağlar; Rab kulların günahlarını {ar:خَبِيرًا, tr:khabīran, gloss:İç yüzünü bilen} ve {ar:بَصِيرًا, tr:baṣīran, gloss:Gören} olarak bilir ve görür (17:17). Odaktaki {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ile {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} kişinin kendi hesabındaki yeterli taraf oluşunu korurken, Rabbin bilgi ve görme alanı insanınkinden geniştir (17:17). İki güvence kendi kapsamlarında birlikte durur; paralellik aralarında bir üstünlük sırası kurmaz ve kişiyi Rabbe eşitlemez (17:17).

Bu geniş tanıklığın bedensel yönü, 75:14’te insanın kendi nefsine karşı delil oluşuyla ve 36:65’te ellerin konuşup ayakların yapılanlara tanıklık etmesiyle açılır (75:14, 36:65). Odaktaki {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} öz-tanıklığı kurarken bu ayetlerde beden de kanıtın taşıyıcısı olur; 33:39’daki {ar:كَفَىٰ بِٱللَّهِ حَسِيبًا, tr:kafā bi-llāhi ḥasīban, gloss:Allah hesap görücü olarak yeter} daha geniş yargı ufkunu korur (33:39). Böylece kişinin kendi deliliyle karşılaşması tanıklığın bir unsuru olarak belirginleşir, nihai ve yanılmaz yargıçlığa dönüşmez; bu yankılar odaktaki biçimin morfolojisini belirlemez (75:14, 36:65, 33:39).

## Yöneliş ve Karşılık

17:18 ve 17:19 hesabın yöneldiği amaçları ve bunlara eşlik eden çabayı ayırır: {ar:يُرِيدُ الْعَاجِلَةَ, tr:yurīdu al-ʿājilata, gloss:Yakın olanı ister} yakın olana yönelmeyi, {ar:أَرَادَ الْآخِرَةَ, tr:arāda al-ākhirata, gloss:Ahireti ister} ahirete yönelmeyi bildirir; ikinci yöneliş {ar:وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-saʿā lahā saʿyahā, gloss:Ona yaraşır biçimde çabaladı} diye çabayla açılır ve {ar:سَعْيُهُم مَّشْكُورًا, tr:saʿyuhum mashkūran, gloss:Çabaları takdir edilmiş} diye karşılanır (17:18, 17:19). Odaktaki {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} istekleri ve amaçla uyumlu çabayı hesaba katılabilir kılar; {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} ailesindeki hüküm ve yükümlülük belirleme kolu bu yönelişlere yargısal bir doku ekler (17:18, 17:19). Bu okuma fiillere amaç ve emek boyutunu katar; ayetler kitabın ölçütlerini, niyet için ayrı bir haneyi ya da kişiye yazgı verildiğini açıklamaz (17:18, 17:19).

17:20’de {ar:كُلًّا نُّمِدُّ هَٰؤُلَاءِ وَهَٰؤُلَاءِ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:Her iki gruba da ulaştırırız} sözü iki gruba uzanan desteği, {ar:مِنْ عَطَاءِ رَبِّكَ, tr:min ʿaṭāʾi rabbika, gloss:Rabbinin bağışından} ve {ar:وَمَا كَانَ عَطَاءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışı engellenmiş değildir} ise bu payın esirgenmediğini belirtir (17:20). Bu bağış sahnesi kişisel hükümden ayrı bir katkı sunar: her iki gruba ulaşan mevcut rızık hesap derecesi, hesabın sonucu ya da bu sonucun açıklaması olarak tanımlanmaz (17:20).

17:20’deki bağış anlatısından ayrı olarak, 17:21 bakışı karşılaştırmaya çevirir: {ar:ٱنظُرْ, tr:unẓur, gloss:Bak} buyruğu görüş alanını açar, {ar:فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:faḍḍalnā baʿḍahum ʿalā baʿḍ, gloss:Kimini kimine üstün kıldık} farklılaşmayı, {ar:أَكْبَرُ دَرَجَٰتٍ وَأَكْبَرُ تَفْضِيلًا, tr:akbaru darajātin wa-akbaru tafḍīlan, gloss:Dereceler bakımından daha büyük ve üstünlükçe daha fazla} ise basamak ve derece farkını belirginleştirir (17:21). Odaktaki {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayımı bu ayrımları silmeyen bir karşılaştırma imgesine katkı verir (17:21). Dereceler hesap sonrasındaki karşılıklar olabilir; 17:21 bunları odaktaki kitabın yöntemi ya da belirli bir aritmetik işlem olarak açıklamaz.

## Tartılan Kayıt

Karşılaştırmadan ayrı bu maddi imge, {ar:كَفَىٰ, tr:kafā, gloss:yeter} fiilinin olağan yeterlik anlamını koruyarak kelime ailesinin araç adlarındaki sınırlı koluna dayanır. Bu adlardan bazısı yuvarlak ya da çanak biçimli parçayı, içindekini taşıyan veya çevreleyen bir yeri anlatır; terazi kullanımında kefe tartılacak nesneyi tutar. Bu imgede her unsur ayrı bir iş görür: {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} tartılan kayıt nesnesini, {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sayımı ölçüyü, araç adı da içeriği taşıyan kefeyi sağlar. Böylece hesap, ölçülüp tutulan bir kayıt gibi tasavvur edilir; bu uzak ve atfedilmiş bağlantı ayette terazi bulunduğunu ya da {ar:كَفَىٰ, tr:kafā, gloss:yeter} fiilinin doğrudan “kefe” anlamına geldiğini ileri sürmez.

Terazi imgesinden ayrı bir kelime kolu, yalnız belirli ikilemeli söz öbeklerinde yüz yüze geliş anlamı taşır; odaktaki biçim bu kalıplardan biri değildir. Yine de {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin}, {ar:عَلَيْكَ, tr:ʿalayka, gloss:senin aleyhine} ve {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} ilişkisi kişinin kendi deliliyle karşılaşmasını ihtiyatlı bir imgeye dönüştürür. Benliğin tam kendilik yönü kişiyi hem hesaba giren içerik hem değerlendirilen kişi olarak tutar; beden ya da iç dünyanın başka anlamları bu özel bağlantıda etkin değildir. Ailedeki “bizzat kendisi, başka bir insan aracılığıyla değil” kullanımı bu sahnenin aracısızlığını belirginleştirirken ilahî yargı ufku da 33:39’la birlikte korunur (33:39).

## Gizli Aralıklar

Yüz yüze gelişten ayrı bir mekânsal arayışta, 17:5’teki {ar:جَاسُوا۟, tr:jāsū, gloss:Her yanı araştırdılar} geniş taramanın kapsamını, {ar:خِلَٰلَ الدِّيَارِ, tr:khilāla al-diyār, gloss:Konutların aralarından ve içlerinden} ise aramanın çevrili konutların aralarına ve içine ilerleyişini verir (17:5). Bu iki ayrıntı farklı işler görür: ilki araştırmanın yaygınlığını, ikincisi saklı ve kuşatılmış mekânların içine uzanmasını duyurur. {ar:كِتَٰبَكَ, tr:kitābaka, gloss:kitabını} okuma ve {ar:بِنَفْسِكَ, tr:bi-nafsika, gloss:bizzat kendin} ile kurulan kişisel sorumlulukla temasında, bu tarihsel tarama görünür satırların ötesindeki hayat aralıklarını yoklayan bir okuma imgesine dönüşür (17:5). Kayda taşınan taraf mekânsal araştırma benzetmesidir; 17:5’in tarihsel akını konutlarda geçer, kişi ev ya da kitap gerçek odalardan oluşan bir yer yapılmaz (17:5).

</source_prose>
