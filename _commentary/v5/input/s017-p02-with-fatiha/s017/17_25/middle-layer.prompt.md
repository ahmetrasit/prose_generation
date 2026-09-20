# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:25**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.middle.claims.json`

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
- Refer to source paragraphs as `17:25 ¶N`.

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

`(17:25 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:25",
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
        "citation": "(17:25 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_25/17_25.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_25/17_25.middle.claims.json \
  --ayah-ref 17:25
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_25/17_25.prose.editorial.tr.md`

<source_prose>
## İç Bilgi ve Yetiştirme

17:25'te söz, {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} içinizde ne varsa en iyi bilendir diye başlar; {ar:إِنْ تَكُونُوا صَٰلِحِينَ, tr:in takūnū ṣāliḥīn, gloss:eğer iyi ve düzgün olursanız} şartının ardından O'nun {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} için {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} olduğu bildirilir. İlk bölümdeki {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ve ardından gelen iç benlik öbeği, yerleşik bir isim cümlesi kurar; ayetin sonundaki şart ve cevap ise bu bilgi bildirimini iyi olma hâli ve bağışlayıcılıkla tamamlar. Hemen önceki merhamet duasından sonra yeni bir dua değil, Rabbin bilen ve bağışlayıcı oluşuna dair bir bildirim gelir.

{ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} tekil Rab unvanını çoğul muhataplara yöneltir. Unvandaki şedde söze ağırlık verir; ikinci çoğul iyelik eki topluluğa seslenirken her kişinin kendi iç alanını da görünür tutar. Rab unvanı mutlak sahiplik ve yönetme yetkisinin yanı sıra gözetip düzenlemeyi, besleyip büyütmeyi ve eksikten olgunluğa doğru yetiştirmeyi çağrıştırır. Bu bakım çağrışımı unvanın gözeten ve yetiştiren yönünü öne çıkarır; ayetin biçimi insanî mülkiyet ya da ettirgen fiil kurmaz. Bilen Rab, {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} ve {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} ile ayrı ayrı ilişki kurduğunda bu yetiştirme tonu da duyulur.

Bu yetiştirme çağrışımı, hemen önceki ebeveyn sahnesiyle somutlaşır. Ebeveynlerin çocuklarını büyütmesini anlatan {ar:رَبَّيَانِى, tr:rabbayānī, gloss:beni yetiştirdiler} ile {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} ayrı köklerden gelir; bu biçimler insanî bakım ile ilahî gözetimi bakım ve gelişim yankısında buluşturur (17:24). Çocuğun bir zamanlar küçük ve bağımlı oluşu ile yaşlanan ebeveyne yönelen bakım aile içi bir karşılıklılık örüntüsü kurar; bu, {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} sözündeki tekrarlı yönelişe de yankı verir. Aile bakımı bu kelimenin tanımı değil, onun çevresindeki bir ilişkisel çağrışımdır: {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} “sık sık dönenler” anlamını korur. Ebeveynlere merhametle alçak gönüllü davranma ve onlar için merhamet dileme buyruğu bu insani şefkati açıkça kurar (17:24).

Yetiştirme ile ilahî bilgi 53:32'de de yan yana gelir: insanın topraktan ve embriyonik aşamalardan oluşması, Allah'ın bilgisi ve kişinin kendini arı saymaması uyarısıyla birlikte anılır (53:32). Böylece {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} zaman içinde insanı oluşturan ve {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} hakkında bilgi sahibi olan Rab olarak duyulur. Furkân 25:6'nın gizliyi bilme ile bağışlanmayı birlikte anması, bu iç alanı dış görünüşe ya da kişinin kendi saflık iddiasına indirgememeyi sağlar (25:6). Oluş, bilgi ve bağışlanma yan yana durur; bu birliktelik kendi başına zorunlu bir ahlaki nedensellik kurmaz.

{ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen}, hemze ile başlayan üstünlük kalıbıdır. Cümlede karşılaştırılan başka biri bulunmadığı için bilgi rakipler arasında ölçülmez; en iyi bilme doğrudan Allah'a yüklenir. Bilme ailesindeki işaret edip seçerek ayırt etme çağrışımı da {ar:فِى, tr:fī, gloss:içinde} ve {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} ile buluşunca içeriği tanıma ve ayırdetme imgesi açar; sözcüğün temel anlamı yine bilmedir. Allah'ın insanların içlerindekini bildiğini söyleyen benzer bir kuruluş Bakara 2:235'te de görülür; 17:25'te bu bilgi, Rab unvanı ve ayetin sonundaki bağışlayıcılık niteliğiyle özelleşir (2:235).

İçeriğe geçişi {ar:بِ, tr:bi, gloss:hakkında} başlatır ve bilme iddiasını {ar:مَا, tr:mā, gloss:ne varsa} sözüne bağlar. Bi-mā yazıda ve tilavette tek bir giriş gibi duyulur; mîm'in nazal sesi biraz sonra gelen iç benlik sözüne ses köprüsü kurar. Buradaki mā soru değil, ilgi zamiridir; ardından gelen {ar:فِى, tr:fī, gloss:içinde} öbeğiyle tamamlanır. Bilinen içerik önce “ne varsa” diye açık bırakılır, düşünce ya da niyet diye erkenden daraltılmaz.

{ar:فِى, tr:fī, gloss:içinde}, ardından gelen {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} adını kendisine bağlar ve bilgiyi dışsal bir durumdan muhatapların iç alanına taşır. Yer bildiren içerilme burada soyut ve ahlaki bir alana uygulanır. Kırık çoğul adla ikinci çoğul iyelik eki, toplu hitabın içinde her kişinin kendi iç dünyasını korur. {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} olağan olarak düşünceleri, niyetleri, kişinin kendi farkındalığını ve ayırt etme gücünü taşıyan iç benliği anlatır. Çoğul biçim bu alanı kişinin iç varlığının bütününe doğru genişletebilir; bu genişleme kapsam yankısıdır, özdeşlik ya da pekiştirme yapısı değil. Aynı söz ailesindeki soluk alıp verme anlamı ise {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen}, {ar:فِى, tr:fī, gloss:içinde}, {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} ve {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} ile ayrı ayrı temas ederek içten dışa çıkan soluk ve yinelenen dönüş yankıları verir; cümlenin olağan “iç benlikler” anlamı yerinde kalır.

İçte bilinen alan, 17:23'teki söz davranışlarının yanına yerleşir. Anne babaya iyilik buyruğu, yaşlılığa erişen ebeveyne “of” bile dememeyi, azarlamaktan kaçınmayı ve gönül alıcı söz söylemeyi ister (17:23). Ebeveynlerin yaşlılık çağı bakımın yükünü görünür kılar; ardından gelen {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} ise dışarıdan duyulan sözle içte tutulan niyet ve sıkıntıyı yan yana getirir (17:23, 17:25). Bu yan yanalık söz ile iç hâl arasındaki mesafeyi gösterir; ayetlerden tek başına bir kişinin azarladığı ya da belirli bir duygu taşıdığı sonucu çıkarılmaz. Ebeveynlere iyilik ve merhamet sahnesi {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} niteliğine toplumsal bir bağlam sağlar; salihlik yalnız ebeveyne bakmaya indirgenmez, bakım da iç hâlin tek başına kanıtı değildir (17:23, 17:24). Dönüş ve bağışlanma buyrukların yerini almaz; aileye ilişkin sorumluluk kendi ağırlığını korur.

## Şart ve Onarım

{ar:إِنْ, tr:in, gloss:eğer}, önceki cümlede bilgisi bildirilen iç alanın ardından gelir ve şartı onun üzerine kurar. Edat, {ar:تَكُونُوا, tr:takūnū, gloss:olursanız} fiilini cezm ederek yönetir; böylece cümle tamamlanmış bir olayı anlatmak yerine açık bir şart ve ona bağlı cevap kurar. “Eğer” iyi olma hâlini önceden varsaymaz. İnsanın içi bilinir; hangi durumda olacağı ise şartın alanında kalır.

Buradaki {ar:تَكُونُوا, tr:takūnū, gloss:olursanız} şart altında yüklemini bekleyen oluş fiilidir; ikinci çoğul kişi özneyi ayrıca zamir koymadan taşır. Muzari biçim, {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} niteliğini tamamlanmış bir etiket yerine süren ve değerlendirmeye açık bir hâl olarak sunar. Fiille sıfatın ses akışı, İsrâ 17:44'teki ahlaki hâl söz varlığına sınırlı bir ritim ve tekrar yankısı verir; {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} sözü de cevaptan önce bu niteliği işittirir (17:44).

{ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler}, bozulma ve kötülüğün karşısındaki olumlu ahlaki sağlamlığı bildirir; nötr bir yeterlilikten daha güçlüdür. Çoğul etken ortaç, niteliği muhataplar arasında paylaştırır ve tek seferlik bir eylemden çok süren bir hâl olarak duyurur. Sözcüğün anlam alanında bozulmayı giderme ve iyi hâle getirme yanında kişiler arasındaki uzaklığı ya da çatışmayı azaltıp barıştırma imkânı da vardır. {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz}, {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ve {ar:تَكُونُوا, tr:takūnū, gloss:olursanız} ile kurulan bakım ve bilgi ilişkisi, sağlamlığı yetişmenin yöneldiği bir uygunluk olarak da düşündürür. I. bâb etken ortaç burada iyi ve sağlam durumda olanları niteler; onarıcı ettirgenlik, sözcüğün bu biçiminden değil, anlam alanındaki ayrı bir imkândan gelir. Şartta iyi olma, cevapta dönüş ve bağışlanma bulunması, yanlış sonrasında yeniden kurulma imkânını da duyurur.

Bu imkân, başka ayetlerde tövbe ve ıslahın yanlışın ardından gelmesiyle somutlaşır: Nûr 24:5 ve En'âm 6:54 tövbe ile düzelişi birlikte anar; Furkân 25:70 tövbe, iman ve iyi eylemi bağışlanmayla yan yana getirir (24:5, 6:54, 25:70). Böylece {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} baştan kusursuz bir geçmiş şartı değil, eylemle yeniden kurulabilen bir hâl olarak da duyulur. Nisâ 4:129'daki eşler arasındaki gerilimin ardından uzlaşmanın takva ve bağışlanmayla birlikte anılması, bu niteliğe ilişkisel onarım ve barışma yankısı katar (4:129). 17:25'in kişisel ve içsel odağı sürerken, iyi hâlin kişiler arasındaki bağı da onarabileceği görünür olur.

Şartın cevabını {ar:فَ, tr:fa, gloss:bunun üzerine} başlatır ve sonucu koşula bağlar; ardından gelen {ar:إِنَّ, tr:inna, gloss:şüphesiz} cevabı kesin bir bildirim olarak kurar. Kesinlik, şartın gerçekleştiği konusunda değil, cevabın bildirdiği {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} niteliğindedir. {ar:هُۥ, tr:hu, gloss:O}, inna'nın yönettiği isim ögesidir ve açılıştaki {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} hitabına döner; böylece Rab cevabın öznesi olur. İnsan için şartlı oluş bildiren {ar:تَكُونُوا, tr:takūnū, gloss:olursanız} ile Rabbin niteliğini bildiren {ar:كَانَ, tr:kāna, gloss:yerleşik olarak ...dır} aynı olma çekirdeğinde yankılanır; özneleri ve işlevleri ayrıdır. Kāna'nın mâzi biçimi burada geçmişte tamamlanmış tek bir bağışlama eylemini değil, Rabbin yerleşik niteliğini kurar. Oluş ailesinin bir yerde bulunma ya da konumlanma çağrışımı, insanın şart altındaki oluşuna karşı ilahî niteliğin yerleşik konumunu düşündürür; bu imge yer bildiren bir cümleye dönüşmez.

Furkân 25:70'te tövbe ve iyi eylemlerden sonra Allah'ın {ar:وَكَانَ اللَّهُ غَفُورًا رَحِيمًا, tr:wa-kāna llāhu ghafūran raḥīman, gloss:Allah çok bağışlayıcı ve esirgeyicidir} oluşu bildirilir (25:70). Buradaki {ar:تَكُونُوا, tr:takūnū, gloss:olursanız} ile {ar:كَانَ, tr:kāna, gloss:yerleşik olarak ...dır} karşılaştırması, insanın düzgün hâlinin dönüşle yeniden kurulabilmesi ile Allah'ın bağışlayıcılığının yerleşik oluşunu yan yana getirir. Paralellik anlam ve biçim yankısındadır: 25:70, 17:25'teki şart kuruluşunu yinelemez. Bu temas onarım imkânı ile ilahî niteliği birlikte düşündürür.

## Dönüş ve Bağışlanma

{ar:لِ, tr:li, gloss:için} edatı {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} adını yönetir; bağışlayıcılığın özellikle bu kişilere yöneldiğini, onlara dönük olduğunu bildirir. Bu alıcı sınıfının adı son yüklem {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} gelmeden önce verilir; böylece cümle, bağışlayıcılık niteliğini açıklamadan önce dönüş sahiplerini öne çıkarır.

{ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} soyut bir eylemden çok dönüşle nitelenen insanları adlandırır. Belirli çoğul ve akıl sahibi eril biçimi tanınabilir bir topluluk kurar; yoğunluk taşıyan etken sıfat ise bir defalık geri gelişten ziyade yinelenen yönelişi karaktere yerleştirir. Ayetin içinde bu topluluk, şarttaki {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} ile cevabın son niteliği {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} arasında durur: iyi olma hâli kusursuzlukta donmaz, dönüşle sürer. Olağan geri dönme anlamı korunur; li edatının alıcı ilişkisi ve çevredeki bağlam, bu yönelişi Allah'a dönüş olarak duyurur. Bu bağ, sözcüğün anlamını belirli bir ibadet programına daraltmaz.

Bu ilahî yönelişi, Allah'a dönüp teslim olma ve azap gelmeden önce yönelme çağrısı belirginleştirir (39:54). Sahici tövbe ve yanlışların silinmesi de Allah'a yönelişle birlikte anılır (66:8). Bu ayetler {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} sözündeki genel geri dönüş anlamını silmeden, yanlış davranıştan uzaklaşıp Allah'a tekrar yönelme tarafını görünür kılar.

Dönüşün varacağı yer de sözcüğün çevresinde duyulur. Sâd 38:25'te bağışlanma ve yakınlık sahnesinin ardından “güzel dönüş yeri” sözü gelir (38:25). Böylece {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} yinelenen yönelişi, bu ifade ise iyi varış noktasını öne çıkarır; 17:25'teki {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} ile dönüş sahiplerinin yan yanalığı da 38:25'in bağışlanma, yakınlık ve güzel varış sahnesini yankılar. Bu bağ 38:25'teki “güzel dönüş yeri” kullanımına özgüdür. Kuyu ve değirmen gibi anlamlar sözcüğün başka kullanımlarında geçerliliğini korur; yalnızca bu sahnedeki dönüş imgesine katılmaz.

Yinelenen yöneliş, sıkıntıdan sonra ferahlığa kavuşan kişinin önceki çağrısını unutmasını anlatan karşıt sahnede keskinleşir (39:8). Bu karşıtlık {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} için sürekliliği kusursuz sicil değil, sapmadan sonra yeniden alınabilen istikamet olarak açıklar. {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} niteliği de düşüşün kendisini otomatik olarak bağışlanmış saymaz.

Son nitelik {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı}, yalın etken ortaç yerine yoğunluk taşıyan feʿūl kalıbındadır; bu kalıp tek bir bağışlama eyleminden çok bol ve yerleşik bağışlayıcılığı öne çıkarır. Tövbe ve düzelişten sonra bağışlanmanın geldiği bağlamlar, bu niteliği dönüş sahiplerine yönelmiş geniş bir bağışlayıcılık olarak işittirir (24:5, 25:70). Kāna'nın mansup yüklemi ve ayetin son sözü olarak açılıştaki {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ile {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz}e yeniden ses verir: bilinen iç alan, dönüşle ve sonunda bağışlayıcı nitelikle karşılanır. Belirsiz mansup biçim son niteliğe sesçe genişlik ve açıklık katar.

Bağışlayıcılığın koruyucu yönü, dönüş sahipleri için bağışlanma ve ateş azabından korunmanın birlikte dilendiği Mü'min 40:7'de; bağışlanma ile cezalandırmanın Allah'ın iradesine bırakıldığı Âl-i İmrân 3:129'da görünür (40:7, 3:129). Bu örneklerde koruma, kusurun ve sonucunun bağışlanmasıdır; {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} genel bir beraat ilanı vermez ve sorumluluğu kendiliğinden kaldırmaz.

Örtme kök alanı, bilinen iç benliği bağışlayıcılıkla ilişkilendiren koruyucu bir imge sunar. {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ile {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} arasındaki temas, iç alanın bütünüyle bilinmesini açıkta kalma karşısında koruyucu örtü imgesiyle buluşturur. Miğfer başı açıkta kalmaktan korur; yağı baştan uzak tutan başörtüsü bezi, yayın çentiğine konan yama ve bulutu örten bulut aynı örtme alanını başka somut kullanımlarda gösterir. Bunlar ayette geçen nesneler değil, örtme ve koruma söz alanının örnekleridir. Ayetteki {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} bağışlayıcılık niteliğidir; bu örnekler ona koruma yankısı katar. İkinci temas, {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} ile {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} arasındadır: bu yakınlık, dönüş sahiplerinin kusura açık iç dünyasını ve kusurun sonucuna karşı korunmayı öne çıkarır. Böylece örtme alanı iki ayrı katkı verir: bilinen içeriğin açıklığına karşı siper imgesi ve dönüşle ilişkilenen kusur sonuçlarına karşı koruma.

Ayrı ve deneysel bir imge, içteki onarımı soluk, yürüyüş ve örtünün ardışık katkılarıyla duyurur. {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} olağan anlamında iç benliği bildirir; söz ailesindeki soluk alıp verme kullanımı, {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ve {ar:فِى, tr:fī, gloss:içinde} ile temas ederek içten dışa çıkan nefes imgesini verir. {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} yinelenen dönüş anlamını taşır; aynı ailede uzuvların gidip gelmesi ve el ayakların hızlı salınımıyla ilgili yürüyüş kullanımı bu tekrara bedensel ritim katar. {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} ile ilişkili örtü ise kırılgan iç sürece karşı korunma imgesini tamamlar. Bu katkılar birlikte ortaya çıkış, sapma, dönüş ve yeniden korunmayı tek bir süreç görüntüsünde buluşturur. İmge, her sözcüğün olağan anlamını korur: nufūsikum iç benlikleri, al-awwābīn sık dönüşü, ghafūran bağışlayıcılığı adlandırır. Yürüyüş kolunun bu imgedeki katkısı tekrara bedensel ritim vermektir; “eve varış” anlamı bu kola ait değildir.

## Yakın Ayetlerin Ölçüsü

Dönüşün yönü, yakınlarda beliren dağılma hareketinin karşısında belirginleşir. Yakınlara, yoksula ve yolda kalmışa haklarını verme buyruğunun ardından saçıp savurma yasağı gelir; sonraki ayet saçıp savuranları şeytanla kardeşlik ve Rabbine karşı nankörlükle niteler (17:26, 17:27). Kaynağın saçılması ve şeytanla ilişkilendirilen uzaklık, {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} sözündeki geri yönelişin karşı kutbu gibi duyulur. Bu yan yanalığın katkısı, dağılma ile dönüşü iki ayrı ahlaki yönelim olarak karşılaştırmaktır; dağılmış servetin dönüş sahiplerince toplandığını söylemez.

Ses yakınlığı, 17:27'deki {ar:كَفُورًا, tr:kafūran, gloss:çok nankör} ile 17:25'teki {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} arasında nankörlük ve bağışlanmayı karşıt yönlerde işittirir. Kafūran nimete karşı nankörlüğü niteler; nimeti gizleme ya da örtme çağrışımı kendi bağlamından gelir. Ghafūran ise başka bir kökten gelir ve dönüş sahiplerine yönelik bağışlayıcılığı bildirir (17:27, 17:25). Dolayısıyla karşıtlık ses ve bağlam düzeyindedir, ortak bir kök ya da eylem ilişkisi değildir. {ar:لِ, tr:li, gloss:için} edatının belirttiği {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler}, bağışlayıcı muamelenin alıcısıdır.

17:28'de maddi imkânı olmayan kişi, kendisine başvuranlardan görünürde geri çekilmek zorunda kalabilir. Yüz çevirmeyle birlikte Rabbin rahmetini arama ve umma da anılır; imkânsızlık içinde söylenebilecek kolay, erişilebilir söz ise ilişkiyi nazikçe sürdürür (17:28). Burada görünen geri çekilme ile içteki yöneliş aynı şey değildir: {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} ve {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} maddi yetersizliğin kişinin iç niyetini tek başına açıklamadığını düşündürür. Bu sahne, elde olmayan imkân ile söylenebilecek nazik sözü ayırarak {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} olma hâline somut bir davranış alanı açar.

Sonraki buyruklarda ölçü fikri belirginleşir. 17:29'da eli boyna bağlanmış gibi tutmakla onu sonuna kadar açmak iki uç olarak verilir; {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} olma hâli bu karşıtlığın ortasında ölçülü davranışla duyulur, ama sözcüğün kendisi “harcama” ya da “ölçü” demek değildir. 17:30'da rızkın genişletilip daraltılması verme imkânının insanın elinden bağımsızlığını; 17:35'te doğru teraziyle tartma buyruğu ise ölçünün somut uygulamasını gösterir (17:29, 17:30, 17:35). Ekonomik bağlamı özellikle rızık ve terazi ayetleri kurar; tek başına 17:29 belirli bir servet ya da el yorumu gerektirmez. Odaktaki sıfat muhatapları niteler, ölçülü davranış yankısı yakın buyruklardan gelir.

17:31, iç baskının davranışa değebildiği belirli bir korku sahnesi açar. Yoksulluk korkusu çocukları öldürmeme yasağından önce gelir; ardından rızkın Allah'tan olduğu bildirilir (17:31). Bu sıra, {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} sözündeki düşünce ve niyet alanına davranışı etkileyebilen somut bir korku örneği sunar. Sahne bu korkunun her durumda şiddete dönüştüğünü ya da her kişinin saiki olduğunu söylemez.

17:32'de sınır, tamamlanmış eylemden önceki yaklaşma noktasına çekilir: zinaya yaklaşmama buyruğu, yol ve varılan son nokta sözleriyle güzergâhı belirginleştirir (17:32). Bu sıra, {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} için yol tamamlanmadan yön değiştirme imkânını, {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} içinse iyi hâle yönelen yolu düşündürür. Bu benzetmenin katkısı 17:32'deki yaklaşma eşiğidir; al-awwābīn'in sözlük anlamı “sakınanlar” değildir ve bu bağ 17:25'e yeni bir yasaklar listesi yüklemez.

17:33'te öldürülmesi yasaklanan {ar:ٱلنَّفْسَ, tr:an-nafsa, gloss:can taşıyan kişi}, hayatı dokunulmaz kılınmış insandır; bu kullanım 17:25'teki {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} düşünce ve niyet alanından ayrılır (17:33, 17:25). Ortak söz ailesi iç benlik ile canlı kişi arasında yankı kurar; iki ayetteki anlam düzeyleri ayrı kalır. Öldürülenin velisine tanınan yetkinin yanına öldürmede aşırı gitmeme sınırı konur; hayatın dokunulmazlığı ve misillemedeki ölçü, {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyi ve düzgün kimseler} niteliğini hayatı gözeten eylemlerle buluşturur (17:33).

17:35'teki daha hayırlı sonuç, eylemin varacağı ufku adlandırır. {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} önceki ya da beklenen varış yerine dönüşü, 17:35 ise davranışın daha iyi sonucunu öne çıkarır; iki imge yöneliş ve varış temasında buluşur (17:35). Sonuç ile dönüş ayrı köklerden gelir; bu yakınlığın katkısı yön benzerliğidir, “iyi sonuca erişmek” awb sözcüğünün sözlük anlamı değildir.

Davranıştan iç dünyaya bakış, 17:36'da bilgiye konan sınırla açılır. Bilgin olmayan şeyin ardına düşmeme buyruğunun ardından işitme, görme ve gönlün sorgulanacağı söylenir (17:36). Buradaki bilgi sözü, 17:25'teki {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} ile aynı alanı paylaşır, fakat bilgi konumları farklıdır: Allah iç benlikleri bilir; insan ise iddiasını elindeki dayanakla sınar. {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} bu sahnede iddia konusu olan iç âlemdir; duyular ve gönül ona erişmenin sınırlı yollarıdır. Bu bağlantının katkısı kanıta dayalı ihtiyattır; 17:36'yı her yargıyı yasaklayan genel bir hükme genişletmez.

17:37'de iç eğilim bedende yön ve ölçek kazanır. Taşkınlıkla yürüme, yeri delemez ve boyca dağlara erişemez oluşla sınırlandırılır (17:37). {ar:نُفُوسِكُمْ, tr:nufūsikum, gloss:iç benlikleriniz} söz ailesinin gurur, onur, yüksek amaç ve özsaygıya uzanan ayrı görünümü, yürüyüş ve ulaşılamayan dağ yüksekliğiyle temas eder. Böylece yürüyüş sahnesi iç eğilimin beden duruşunda ve tasarladığı ölçüde görünmesini sağlar; bu bağlamdan gelen okuma, tek bir kişinin yürüyüşünden iç hâl teşhisi çıkarmaz.

Bu aile ve ahlaki sahnelerden ayrı, daha geniş bir Rab yankısı Fâtiha'nın “âlemlerin Rabbi Allah'a övgü” sözüyle açılır (1:2). Oradaki {ar:رَبِّ, tr:rabbi, gloss:Rabbi} ile 17:25'teki {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} aynı unvandır: muhataba yakın ve kişisel sesleniş, âlemlerin Rabb'inin evrensel kapsamı içinde duyulur. Sahiplik, buyruk yetkisi ve yönetip düzenleme çağrışımları bu ölçeği taşırken, içinizdekini bilen Rabbe yönelen yakın hitap korunur. Yankı Fâtiha 1:2 ile sınırlıdır; {ar:ٱلْعَٰلَمِينَ, tr:al-ʿālamīn, gloss:âlemler} ile {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi bilen} arasındaki ses benzerliği kelime oyunu kurmaz.

17:25'te {ar:ٱلْأَوَّٰبِينَ, tr:al-awwābīn, gloss:sık sık dönenler} hayat içinde yeniden alınan yönelişi adlandırırken, Ğâşiye 88:25 dönüşün Allah'a olduğunu bildirir (88:25). Yönelinen yer ortaktır, zaman ölçekleri ayrıdır: burada dönüş hayat boyunca yinelenen bir yöneliş, 88:25'te ise varışın kendisidir. Surenin çevresi bu varışı nihai ve kaçınılmaz biçimde duymaya elverir; ayetin kendi sözleri dönüşün Allah'a olduğunu söyler. Böylece hayat içindeki sık dönüş, beklenen son varışla özdeşleşmeden, o varıştan önce sürdürülen yöneliş olarak kalır.

</source_prose>
