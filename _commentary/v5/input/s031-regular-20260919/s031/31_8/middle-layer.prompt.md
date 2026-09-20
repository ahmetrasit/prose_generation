# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:8**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.middle.claims.json`

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
- Refer to source paragraphs as `31:8 ¶N`.

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

`(31:8 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:8",
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
        "citation": "(31:8 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_8/31_8.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_8/31_8.middle.claims.json \
  --ayah-ref 31:8
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_8/31_8.prose.editorial.tr.md`

<source_prose>
31:8, iman eden ve salih işler yapanlar için nimet bahçeleri bulunduğunu tek ve vurgulu bir önerme olarak bildirir. Başındaki {ar:إِنَّ, tr:inna, gloss:kuşkusuz} hükmü sıkıca kurar; kısa sesi cümlenin vurgusunu toparlar, bu işitsel sıkılık da parçacığa ayrı bir sözlük anlamı eklemez. {ar:ٱلَّذِينَ, tr:alladhīna, gloss:o kimseler ki} ile açılan topluluk iman ve amel fiilleriyle tanımlanır; {ar:لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ, tr:lahum jannātu an-naʿīm, gloss:onlara nimet bahçeleri vardır} bu tanımın yargısını aynı cümlede tamamlar. Böylece ayet kendine özgü yerel bir iman–amel–karşılık düzeni kurar; önceki uyarı bu önermenin parçası değildir ve buradan sûrede yinelenen genel bir formül iddiası çıkmaz.

Göreli zamirin ardından gelen {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} ile {ar:وَعَمِلُوا۟, tr:wa-ʿamilū, gloss:ve yaptılar} fiillerinde çoğul özne sürer: bahçelerin alıcıları, aynı iman edip iş yapan gruptur. Eylemler birbirine indirgenmeden yan yana durur; topluluk miras alınan bir adla değil, yaptıklarıyla belirlenir. {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} Form IV’te geçmiş zamanlıdır ve bağlılığı başlayacak bir süreçten çok gerçekleşmiş bir tutum olarak sunar. Bu kullanımda fiilin nesnesi belirtilmez; cümle bağlılıktan işe nesne adlandırmadan geçer ve bu sessizlik iman nesnesini reddeden bir hüküm taşımaz. İki fiilin ortak -ū çoğul sonu ve aradaki kısa {ar:وَ, tr:wa, gloss:ve}, ayrı eylemleri hafif bir ses köprüsüyle birbirine bağlar.

Bağlacın ikinci fiile tutunmasıyla tanım inançtan yapılan işe döner; eylemler eş düzeyde kalır ve biri ötekine değer bakımından üstün kılınmaz. {ar:وَعَمِلُوا۟, tr:wa-ʿamilū, gloss:ve yaptılar} işi aynı çoğul öznenin doğrudan yaptığını gösterir; başkasına gördürülen bir görev değil, öznenin kendi eylemidir. Geçişli {ar:عَمِلُوا۟, tr:ʿamilū, gloss:yaptılar} nesne yuvasını ardından gelen belirli çoğul {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler} ile doldurur; bu sözcük tanınabilir bir iş sınıfını adlandırır, kapalı bir envanter saymaz. Biçimce etken ortaç olan kelime burada isimleşir ve işi yapan kişileri değil, iyi, düzgün ve yararlı; bozulmanın karşıtı niteliğe sahip işleri gösterir. Böylece onarma yönü bir “düzeltici” kişinin adı olarak değil, yapılan işin niteliği içinde duyulur.

İş ve niteliği tamamlanınca ayet alıcılara döner. Öne alınan {ar:لَهُمْ, tr:lahum, gloss:onlar için} önce kimin için olduğunu duyurur, gecikmiş {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} neyin onlara ayrıldığını açıklar; bitişik {ar:هُمْ, tr:hum, gloss:onlar} önceki göreli zamirin açtığı aynı gruba döner. Bir dilbilgisi çözümünde {ar:لَهُمْ, tr:lahum, gloss:onlar için} öne alınmış haber, {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} ardından gelen merfu özne olarak okunabilir. Lâm yarar ve aidiyet bağını kurar: işi yapanlar bu kez alıcı olarak görünür; söz dizimi bu bağı katı, bire bir alışveriş hesabına daraltmaz.

{ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} çoğul bir baş addır; ödül soyut bir iyilikten çok bahçe mekânları olarak görünür, biçim ise bahçelerin sayısını ve yerleşim düzenini açık bırakır. Ardından gelen {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk}, izafetin belirli tamlayanıdır ve bahçeleri ayrı bir sıfat olarak değil, tamlamanın içinden niteler. Arapçadaki belirli artikel Türkçede ayrıca gösterilmese de tanınan bir nimet ve esenlik niteliği kurar. Masdar biçimi tek tek armağanlardan çok yaşanan iyi hâli öne çıkarır: mutluluk bahçelerin niteliği ve içinde yaşanan hâldir; iki adın ilişkisi yakınlaşır, sözlük anlamları birleşmez. Bahçe adındaki ikiz n ödülün gelişine işitsel ağırlık verir, tamlamanın uzun ünlüleri ise ayeti nimet sözcüğünde dinlendirir; bu ritim yaşanan hâlin sesini taşır, süresini belirlemez.

## Sözcüklerin açtığı yakınlıklar

Olağan anlamıyla {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} “inandılar” demektir; güven, korkunun kalkması ve kalbin yatışmasıyla ilgili kullanımı, vaat edilen {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} ve {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} sonucuna değince imana iç emniyet tonu verir. Bahçe adının örtme yönü, ağaçlarla kaplı zemine ilişkin kullanımıyla bu güvene yaşanabilir bir çevre sağlar. Bu korunaklı çevrede {ar:وَعَمِلُوا۟, tr:wa-ʿamilū, gloss:ve yaptılar} bağlılığı amaçlı eyleme taşır; {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler} işin niteliğini kurar ve bozukluğu giderme, onarma yönüyle iyi oluşu somutlaştırır. {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} rahatlık, geçim genişliği ve iyi yaşayışla bahçenin nasıl bir yer olduğunu belirginleştirir. {ar:لَهُمْ, tr:lahum, gloss:onlar için} içindeki lâm da iyi hâlin kime ulaştığını gösterir; nimet o topluluğun yararına yönelir.

Aynı iş–alıcı dizisi uygunluk imgesini açar: {ar:وَعَمِلُوا۟, tr:wa-ʿamilū, gloss:ve yaptılar} işleri, {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler} niteliği, {ar:لَهُمْ, tr:lahum, gloss:onlar için} ise yapanları alıcı olarak verir; iyi işin niteliği böylece onu yapanlara uygun düşen bir ilişki gibi duyulur. Bahçenin olağan mekân anlamına koruyucu örtü, hatta tehlikeyi kesen siper çağrışımı eklenir; bu korunak imgesi bahçeyi gruba uygun gösterirken bahçe anlamı da sürer. {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} iyi hâli, bahçe mekânı, {ar:هُمْ, tr:hum, gloss:onlar} ise orada ağırlanacak kişileri sağladığında, kişinin durumuna ve isteğine uygun bir yer düşüncesi belirir. Bu uygunlukla birlikte yerde kalmayı sürdürme çağrışımı da doğar; ayet bunu ayrı bir fiille değil, tamlamanın analojik yankısıyla hissettirir.

İşi yapanların ve alıcıların aynı cümlede görünmesi, emek ile pay arasında ihtiyatlı bir ücret yankısı açar. {ar:عَمِلُوا۟, tr:ʿamilū, gloss:yaptılar} yapılan işi, {ar:لَهُمْ, tr:lahum, gloss:onlar için} alıcıları, {ar:جَنَّٰتُ ٱلنَّعِيمِ, tr:jannātu an-naʿīm, gloss:mutluluk bahçeleri} sonucu verir; bahçeler bu topluluğa ayrılmış bir dönüş gibi işitilir. {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler} bu benzetmedeki emeği iyi ve düzgün işlerle sınırlar; bozukluğu giderme yönü karşılığın niteliğine eklenir. Ağaç örtüsü dönüşü yaşanabilir, elle tutulur bir çevreye; nimet adı rahatlık ve geçim genişliğine taşır. Lâm de faydanın alıcıya yöneldiğini açık tutar. Bu, iş–alıcı–karşılık arasında kurulan bir ücret benzetmesidir; para, sözleşme, belirli miktarda ödeme ya da katı değiş tokuş düzeni önermez.

Başlangıçtaki {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} ile duanın sonunda kullanılan {ar:آمِينَ, tr:āmīn, gloss:kabul dileğini bildiren amin} arasında biçimce uzak bir ses yankısı duyulabilir; {ar:نَعَم, tr:naʿam, gloss:evet} olumlaması da bu yankıya hafif bir cevap tonu ekler. Aradaki {ar:وَعَمِلُوا۟, tr:wa-ʿamilū, gloss:ve yaptılar} kabul ve onay izini eyleme taşır; yanıt sözde değil amelde duyulur. Bu, olağan iman anlamını koruyan işitsel bir yakınlıktır; metin bunu dua formülüne, açık soru–cevap olayına ya da etimolojik özdeşliğe dönüştürmez. Son tamlamadaki {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} mutluluk anlamında kalır; kökün ayrı “evet” dalı ise iman ve amel tarafından tetiklenen silik bir tasdik rengi bırakır.

Bahçe adı somut {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} anlamını korur. İman ve amel tanımından sonra {ar:لَهُمْ, tr:lahum, gloss:onlar için} ile topluluğa ayrılması ve {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} ile nitelenmesi, fiziksel bahçeyi ölümden sonra varılacak nimetli bir ödül yurdu olarak da işittirir. Bu yankı varışın zamanını ve görünmeyen ayrıntılarını açık bırakırken, somut bahçe ile vaat edilen yurdu birlikte tutar.

## İşitme, sığınak ve süren nimet

Bahçenin barınak oluşu belirginleşince, 31:6 ve 31:7’deki işitme ve yöneliş sahneleriyle karşıtlık daha net duyulur. 31:6’da Allah’ın yolundan saptıran {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahwa al-ḥadīthi, gloss:dikkati dağıtan söylem} ile ona bağlanan {ar:لَهُمْ عَذَابٌۭ مُّهِينٌۭ, tr:lahum ʿadhābun muhīnun, gloss:onlara aşağılayıcı azap vardır} (31:6), 31:8’deki {ar:لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ, tr:lahum jannātu an-naʿīm, gloss:onlara nimet bahçeleri vardır} ile alıcıları aynı söz düzeninde karşı karşıya getirir. 31:7’de ayetler okununca {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} sahnesi ve sanki hiç işitmemiş gibi davranma (31:7) farkı açar. {ar:وَقْرًۭا, tr:waqran, gloss:kulakta ağırlık} işitme önündeki tıkanmayı maddi bir ağırlıkla duyurur; {ar:لَّمْ يَسْمَعْهَا, tr:lam yasmaʿhā, gloss:sanki onları işitmedi} ise işitmeyi ses almaktan karşılık vermeye uzanan bir alımlayış olarak belirginleştirir. Buna karşılık {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} bildiriyi alan, kalbi yatıştıran bir tasdik; {ar:عَمِلُوا۟, tr:ʿamilū, gloss:iş yaptılar} da kabulün amaçlı davranışa geçişi gibi okunur. Bu bağlamsal karşıtlık iman ve amel fiillerinin olağan anlamlarını korur.

İşitme karşıtlığının açtığı soru bu kez vaadin ne kadar sürdüğüne döner. 31:9’daki {ar:خَٰلِدِينَ فِيهَا, tr:khālidīna fīhā, gloss:orada kalıcı olarak kalanlar} sözü 31:8’in {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} vaadini içinde kalınan bir yurt olarak genişletir; {ar:وَعْدَ ٱللَّهِ حَقًّۭا, tr:waʿda Allāhi ḥaqqan, gloss:Allah’ın gerçek olan vaadi} bu sürenin gerçekliğini de vurgular (31:9). Buna karşılık 31:24, kısa süre yararlandırmanın ardından ağır azaba zorlanma sahnesini verir; bu geçici yarar {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} için zaman ölçüsünü keskinleştirir. {ar:نُمَتِّعُهُمْ قَلِيلًۭا, tr:numattiʿuhum qalīlan, gloss:onları kısa bir süre yararlandırırız} sınırlı zamanı, {ar:ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ, tr:thumma naḍṭarruhum ilā ʿadhābin ghalīẓ, gloss:sonra onları ağır bir azaba zorlarız} zorunlu dönüşü ve duyusal sertliği öne çıkarır (31:24). İki sahne yan yana gelince, rahatlık, bolluk ve incelik 31:9’daki kalıcılık ve gerçek vaatle derinleşir; 31:24’teki haz ise sahici fakat kısa süreli kalır.

Bahçenin örtme ve korunak olma yönü, 31:32’deki fırtınalı deniz sahnesine temas edince tehditten güvenli yere geçişi duyurur. {ar:غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-ẓ-ẓulal, gloss:örtüler gibi dalgalar üzerlerini kapladı} sözü insanları üstten kaplayan dalgayı ve çalkantının kararsızlığını verir; {ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā al-barri, gloss:onları kurtarıp karaya çıkardı} ise kurtuluşu sağlam karaya varış olarak gösterir (31:32). Dalganın tehditkâr örtüsü bahçenin ağaç örtüsüyle ortak bir kaplanma imgesi taşır: denizde örtü tehlikeyi yoğunlaştırırken, bahçede örtü korunaklı ve yaşanabilir çevreyi kurar. Karaya çıkarılma bu karşıtlığı güvenli yere varışa taşır; 31:9’daki {ar:خَٰلِدِينَ فِيهَا, tr:khālidīna fīhā, gloss:orada kalıcı olarak kalanlar} sözü de bahçedeki güvenli yaşamın süresini düşündürür (31:9). Bu temas, farklı sahneleri aynılaştırmadan korunak çağrışımını genişletir.

Aynı deniz sahnesi iman fiiline kurtuluş sonrasında da süren vefa tonunu ekler. İnsanlar dalgaların ortasında {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu al-dīna, gloss:dini yalnız Allah’a yönelterek dua ettiler} der; karaya çıkarılınca bazılarının {ar:مُّقْتَصِدٌۭ, tr:muqtaṣidun, gloss:ölçülü davranan}, bazılarınınsa {ar:خَتَّارٍۢ كَفُورٍۢ, tr:khattārin kafūrin, gloss:hain ve nankör} kesilmesi tehlike içindeki samimiyetle sonraki tutum arasındaki değişimi görünür kılar (31:32). Olağan “inanma” anlamını koruyan {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} bu sahneyle, tehlike geçtikten sonra da sürdürülen sadakat olarak genişleyebilir. Bu 31:32 bağlantısı iman fiiline bir vefa tonu katar; kurtuluştan sonraki farklı tutumları 31:8’in vaadine ek bir koşula dönüştürmez.

## Emek, yetişme ve alıcıya dönen yarar

Tehlike ve sığınak görüntülerinden şimdi işin nasıl yetişen bir emek gibi duyulduğuna geçilir. 31:3’te {ar:هُدًۭى وَرَحْمَةًۭ لِّلْمُحْسِنِينَ, tr:hudan wa raḥmatan lil-muḥsinīna, gloss:iyilik yapanlar için rehberlik ve merhamet} yol gösteren yönelişi verir (31:3). 31:4’te namaz, {ar:ٱلزَّكَوٰةَ, tr:az-zakāta, gloss:zekât} ve ahirete kesinlik birlikte anılır; düzenli pratik devamlılığı, zekâtın artış ve büyüme çağrışımı ise üretkenliği katar (31:4). 31:5’te hidayet ve felah öne çıkar; {ar:ٱلْمُفْلِحُونَ, tr:al-mufliḥūna, gloss:başarıya erenler} başarıya ulaşanları bildirirken toprağı yarıp işleyen çiftçi imgesini de açar (31:5). Yön gösterme, sürdürülmüş pratik ve toprağı işleme böylece ayrı katkılar verir: birlikte, 31:8’deki amaçlı {ar:عَمِلُوا۟, tr:ʿamilū, gloss:iş yaptılar}, iyi ve düzgün {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler} ile {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} arasında yetiştirme imgesi kurar. Bahçe ödül mekânı olarak kalırken bakım görüp olgunlaşan iş gibi de duyulur; bu bağlantı tarımsal bir neden–sonuç önermesi değil, önceki ayetlerin vaade kattığı imgedir.

Bu yetişme imgesine 31:10’da yağmurun ardından çeşitli güzel bitkilerin çıkması somut bir gelişme sahnesi ekler (31:10). {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} için ağaçlarla örtülü zemin kullanımı bitki örtüsünü, biçimce dişil çoğul etken ortaç olan {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:iyi ve yararlı işler}deki düzgünlük ve sağlamlık ise işin niteliğini taşır; yağmurla yeşeren bitkiler bu iki niteliği görünür gelişim imgesinde yan yana getirir. Bu, işlerle bitki büyümesi arasında neden-sonuç bağı değil, gelişme biçimlerinin benzerliğidir; birlikte vaat edilen iyiliği yaşanan, yetişen bir çevre gibi duyururlar.

Yetişen çevrenin ardından dikkat, yararın kime döndüğüne çevrilir. 31:12’de şükreden kişinin kendisi için şükrettiği söylenir ({ar:يَشْكُرْ فَإِنَّمَا يَشْكُرُ لِنَفْسِهِۦ, tr:yashkur fa-innamā yashkuru li-nafsihi, gloss:şükreden ancak kendi iyiliği için şükreder}); Allah’ın hiçbir şeye muhtaç ve övgüye layık oluşu da yararın alıcıda kaldığını belirginleştirir ({ar:ٱللَّهَ غَنِىٌّ حَمِيدٌۭ, tr:Allāha ghaniyyun ḥamīd, gloss:Allah hiçbir şeye muhtaç ve övgüye layıktır}) (31:12). Bu vurgu, {ar:لَهُمْ جَنَّٰتُ ٱلنَّعِيمِ, tr:lahum jannātu an-naʿīm, gloss:onlara nimet bahçeleri vardır} bağını verende eksikliği gideren bir paydan çok alıcıya yönelen bir dönüş gibi duyurur. Bu, 31:12’nin şükür ve kişinin kendi yararı vurgusuyla sınırlı bağlamsal bir yankıdır; {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} için sözlük tanımı ya da 31:8’in geriye dönük açıklaması değildir. Buradaki dönüş bir ücret adı değildir; {ar:عَمِلُوا۟, tr:ʿamilū, gloss:iş yaptılar} ise isim değil, geçmiş zamanlı eylem fiilidir.

31:20’de nimetlerin açık ve gizli diye anılması, bahçe ve nimet sözlerinin açtığı alanı görünenin ötesine taşır (31:20). {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} kelimesinin örtme-gizleme yönü vaat edilen iyi hâle içte kalan bir boyut, {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} kelimesinin alıcıya ulaşan iyilik yönü ise bu boyutun kime yarar sağladığını ekler. 31:20’deki {ar:نِعَمَهُۥ ظَٰهِرَةًۭ وَبَاطِنَةًۭ, tr:niʿamahu ẓāhiratan wa-bāṭinatan, gloss:nimetlerini açık ve gizli olarak} çifti görünenle içte kalanı birlikte getirir; nimet adının yinelenmesi de iyiliğin tamlığını duyurur (31:20). Aynı ayette Allah hakkında bilgisiz, hidayetsiz ve aydınlatıcı kitapsız tartışanlardan söz edilmesi ({ar:وَمِنَ ٱلنَّاسِ مَن يُجَٰدِلُ فِى ٱللَّهِ بِغَيْرِ عِلْمٍۢ وَلَا هُدًۭى وَلَا كِتَٰبٍۢ مُّنِيرٍۢ, tr:wa-mina al-nāsi man yujādilu fī Allāhi bi-ghayri ʿilmin wa-lā hudan wa-lā kitābin munīr, gloss:insanlardan kimi Allah hakkında bilgisiz, hidayetsiz ve aydınlatıcı kitapsız tartışır}) bu nimetleri tanıyan {ar:ءَامَنُوا۟, tr:āmanū, gloss:inandılar} imanıyla karşı karşıya gelir (31:20). Böylece tartışma sahnesi 31:20’nin kendi iman ve bilgisizlik karşıtlığını kurar; bahçe okumasına yalnızca yerel bir karşıtlık taşır.

Yetişen çevre imgesi 31:16’da daha küçük bir ölçeğe iner. 31:8’deki amaçlı {ar:عَمِلُوا۟, tr:ʿamilū, gloss:bilerek işler yaptılar} eylemi işin iradesini, sağlamlık taşıyan {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:iyi ve yararlı işler} biçimi niteliğini verir; {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler}in örtme yönüyle güçlenip boy atarak sıklaşan bitki imgesi ise yaşanan çevreyi kurar. 31:10’daki {ar:فَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍۢ, tr:fa-anbatnā fīhā min kulli zawjin karīm, gloss:orada her güzel türü bitirdik} sözü bu çevredeki görünür yetişmeyi sağlar (31:10). Birlikte bu ayrıntılar amaçlı iş, sağlam nitelik ve örtülü çevre arasında bir yetişme imgesi hazırlar.

31:16’daki {ar:حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:ḥabbatin min khardalin, gloss:bir hardal tanesi} bu imgeyi en küçük ölçeğe taşır: tane kaya, gökler ya da yer içinde gizlense de Allah onu getirir ({ar:فَتَكُن فِى صَخْرَةٍ أَوْ فِى ٱلسَّمَٰوَٰتِ أَوْ فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ, tr:fa-takun fī ṣakhratin aw fī al-samāwāti aw fī al-arḍi yaʾti bihā Allāh, gloss:kayada, göklerde ya da yerde bulunsa da Allah onu getirir}) (31:16). Küçük tane, sert kuşatılma ve gizli yerden çıkarılma, örtülü çevre ve yetişen bitkilerle ayrı ayrı buluşarak görünür gelişme imgesini tamamlar. Sonundaki {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌۭ, tr:inna Allāha laṭīfun khabīr, gloss:Allah latif ve haberdardır} en ince ve gizli olana erişimi vurgular (31:16). Bu temas küçük potansiyelin ortaya çıkışını 31:8’in amaçlı işiyle yan yana duyurur; insan işlerinin bitki büyümesine neden olduğu bir yasa ileri sürmez.

Aynı saklı gelişme bu kez tohumdan değil, taşınan çocuktan düşünülünce ayrı bir imge kazanır. {ar:جَنَّٰتُ, tr:jannātu, gloss:bahçeler} için açılan “gizlenmiş rahimdeki cenin” kullanımı, {ar:عَمِلُوا۟, tr:ʿamilū, gloss:iş yaptılar} ve {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler}i korunmuş bir gelişimin görünür hâle gelişi gibi duyurabilir; bahçe ve işin olağan anlamları bu imgeyi taşır. Evreleri ayrı ayetler sağlar: 31:14’te {ar:حَمَلَتْهُ أُمُّهُۥ, tr:ḥamalat-hu ummuhu, gloss:annesi onu taşıdı} taşınma sürecini, {ar:وَفِصَٰلُهُۥ فِى عَامَيْنِ, tr:wa-fiṣāluhu fī ʿāmayn, gloss:iki yılda sütten kesilmesi} ayrılma sınırını verir (31:14). 31:34’teki {ar:ٱلْأَرْحَامِ, tr:al-arḥāmi, gloss:rahimler} rahim imgesini, 31:16’daki {ar:حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:ḥabbatin min khardalin, gloss:bir hardal tanesi} ise küçük potansiyelin görünür gelişimini ekler (31:34, 31:16). 31:3’teki {ar:رَحْمَةًۭ, tr:raḥmatan, gloss:merhamet} “rahim” değil “merhamet” anlamındadır; burada yalnızca dikkatli bir kök ailesi yankısı sağlar (31:3). Bu özel benzetme korunaklı gelişim imgesini bahçe ve işe ekler; bahçeler vaadedilen bahçeler, işler de eylemler olarak kalır.

Yetişme imgesinden ilişkilerdeki davranışa geçince 31:15, iyi işin çatışan bağlılıklar arasında nasıl görünebileceğini örnekler (31:15). Anne baba baskı uygulasa da itaat etmeme sınırı konur ({ar:جَٰهَدَاكَ, tr:jāhadāka, gloss:seni zorlarlarsa}; {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:ikisine itaat etme}); dünyada onlarla iyilik üzere beraberlik sürer ({ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًۭا, tr:wa-ṣāḥibhumā fī al-dunyā maʿrūfan, gloss:dünyada onlarla iyilik üzere geçin}) ve Allah’a yönelenlerin yolu izlenir ({ar:وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ إِلَىَّ, tr:wa-ttabiʿ sabīla man anāba ilayya, gloss:bana yönelenin yolunu izle}) (31:15). Bu özel aile örneği, bağlılık sınırını korurken ilişkiyi iyi biçimde sürdürmenin mümkün olduğunu gösterir; {ar:ٱلصَّٰلِحَٰتِ, tr:aṣ-ṣāliḥāt, gloss:salih işler}teki sağlamlık ve onarma yönü de bu beraberliğe yankılanır. Bağlamsal kapsamı aile baskısıdır, her iyi işi uzlaşmaya indirgemez; dişil çoğul ortaç da kişiye değil, yapılan işlere aittir.

Bu toplumsal doku 31:18 ve 31:19’da yüz, yürüyüş ve ses ölçüsüne geçer. İnsanlara karşı yanağı kibirle çevirmeme buyruğu {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-l-nāsi, gloss:insanlara karşı yanağını kibirle çevirme}, yürüyüşte ölçü {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-qṣid fī mashyika, gloss:yürüyüşünde ölçülü ol}, sesi alçaltma ve sesin kendisi de {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtika, gloss:sesini alçalt} ile belirir (31:18, 31:19). {ar:ٱلنَّعِيمِ, tr:an-naʿīm, gloss:nimet ve mutluluk} kelimesinin rahatlık ve esenlik anlamı bu beden tavırlarıyla buluşunca, iyi yaşamın yumuşak ve ölçülü toplumsal dokusu görünür. Buradaki katkı, bu davranış ölçülerinin mutluluk ve esenlik imgesiyle birlikte duyulmasıdır; davranış buyruğu kelimenin tanımına dönüşmez.

## Kişisel karşılık ve tasvirin sınırı

Bedensel ve toplumsal tavırdan şimdi vaadin kişiye nasıl bağlandığına geçilir. 31:33’te ne baba çocuğunun ne çocuk babasının yerine karşılık verebilir; akrabalık iki yönde de başkasının yükünü üstlenemez ({ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lā yajzī wālidun ʿan waladihī wa-lā mawlūdun huwa jāzin ʿan wālidihī shayʾā, gloss:ne baba çocuğunun ne çocuk babasının yerine karşılık verebilir}) (31:33). 31:34’te hiçbir canın yarın ne kazanacağını ve hangi yerde öleceğini bilmediği belirtilir ({ar:وَمَا تَدْرِى نَفْسٌۭ مَّاذَا تَكْسِبُ غَدًۭا, tr:wa-mā tadrī nafsun mādhā taksibu ghadan, gloss:hiçbir can yarın ne kazanacağını bilmez}; {ar:وَمَا تَدْرِى نَفْسٌۢ بِأَىِّ أَرْضٍۢ تَمُوتُ, tr:wa-mā tadrī nafsun bi-ayyi arḍin tamūtu, gloss:hiçbir can hangi yerde öleceğini bilmez}) (31:34). Bu iki sınır {ar:لَهُمْ, tr:lahum, gloss:onlara} bağını kişiye yöneltir: vaadin alıcısı kendi sorumluluğunu taşır, aktarılma ve önceden hesaplanan zaman ise bu ilişkinin kapsamı değildir. Böylece ödül–emek yakınlığı ücret imgesinden daha geniş kalır; 31:8’deki {ar:عَمِلُوا۟, tr:ʿamilū, gloss:iş yaptılar} ücret adı değil, geçmiş zamanlı eylem fiilidir.

Kişisel hesap ufkundan bahçe sözcüğünün ağaç imgesine geçince 31:27’de başka bir sahne açılır (31:27). Ağaçların kaleme dönüşmesi {ar:مِن شَجَرَةٍ أَقْلَٰمٌۭ, tr:min shajaratin aqlāmun, gloss:ağaçlar kalem olsaydı} yazı aracını sağlar; deniz onu destekler ve yedi deniz daha eklenince mürekkep kaynağı yenilenir ({ar:وَٱلْبَحْرُ يَمُدُّهُۥ, tr:wa-l-baḥru yamudduhu, gloss:deniz onu destekleyip çoğaltır}) (31:27). Bu genişletilmiş yazı imkânına rağmen {ar:مَّا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mā nafidat kalimātu Allāh, gloss:Allah’ın sözleri tükenmez}; 31:27’de sonlu araçlarla tükenmeyen sözler arasındaki karşılaştırma ayetin kendi düşüncesini taşır (31:27). 31:8’deki bahçelerin ağaç örtüsü ve canlı bitki gelişimi, bu imgeye malzeme ve ölçek sağlar: bahçe yaşanır çevre olarak kalır, ağaçlı örtü ise sonlu yazı araçları imgesine geçişi mümkün kılar. Böylece bahçe, yaşanan mekândan ağaçlı çevresi aracılığıyla yazı imgesine açılır.

</source_prose>
