# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:13**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.middle.claims.json`

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
- Refer to source paragraphs as `31:13 ¶N`.

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

`(31:13 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:13",
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
        "citation": "(31:13 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_13/31_13.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_13/31_13.middle.claims.json \
  --ayah-ref 31:13
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_13/31_13.prose.editorial.tr.md`

<source_prose>
## Hatırlanan sözden yüz yüze öğüde

Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} bağlacı 31:13’ü süren anlatı akışına bağlar; önceki düşüncenin içeriği burada açılmaz. {ar:وَإِذْ, tr:wa-idh, gloss:ve o vakit} hatırlanan bir anı sahneye getirir. İçindeki {ar:إِذْ, tr:idh, gloss:o vakit} neden bildirmez; sözü geçmişteki belirli bir vakte yerleştirir ve akışı {ar:قَالَ, tr:qāla, gloss:söyledi} ile açılacak konuşmaya geçirir. Bu tamamlanmış söyleme ediminde yalın {ar:لُقْمَٰنُ, tr:luqmānu, gloss:Lokman} adı konuşanı, hemen ardından gelen {ar:لِٱبْنِهِۦ, tr:li-ibnihī, gloss:oğluna} yönelmesi de sözün alıcısını belirler. {ar:ق و ل, tr:q-w-l, gloss:sesli söz söylemek} kökü olağan sesli söyleyişi taşır; fiilin sözlük anlamı değişmez, öğüt gücü yasağın ve gerekçenin içeriğinden doğar. Bu hatırlama çerçevesi ayetin yerel açılışıdır; başka anlatılar için ortak bir söz kalıbı çıkarmaz.

Yönelme öbeğindeki {ar:لِ, tr:li, gloss:yönelme edatı} sözü oğula alıcı ve yarar gören olarak ulaştırır; {ar:ٱبْنِهِۦ, tr:ibnihī, gloss:onun oğlu} içindeki {ar:هِۦ, tr:-hī, gloss:onun} eki de bu çocuğun Lokman’ın gerçek oğlu olduğunu gösterir. Böylece alıntı başlamadan öğüdün kime yöneldiği bellidir. Anlatım önce {ar:قَالَ لُقْمَٰنُ لِٱبْنِهِۦ, tr:qāla luqmānu li-ibnihī, gloss:Lokman oğluna söyledi} diyerek oğulu üçüncü kişide anar; ardından {ar:يَٰ, tr:yā, gloss:ey} seslenme parçacığıyla gelen {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} aynı oğula doğrudan döner. Aile bağı anlatılan bir ilişkiden yüz yüze hitaba geçer.

Bu konuşmanın nasıl bir öğüt olduğunu {ar:وَهُوَ يَعِظُهُۥ, tr:wa-huwa yaʿiẓuhu, gloss:o ona öğüt verirken} hâl cümleciği açar: öğüt verme söylenen sözden sonra gelen ayrı bir iş değil, konuşma anına eşlik eden durumdur. Açık {ar:هُوَ, tr:huwa, gloss:o} zamiri öğüt veren Lokman’ı, {ar:يَعِظُهُۥ, tr:yaʿiẓuhu, gloss:ona öğüt verir} fiilinin sonundaki {ar:هُۥ, tr:-hu, gloss:ona} nesne eki oğlunu gösterir. I. bâbın muzari biçimi öğüdü hatırlanan sahne içinde sürdürür. {ar:و ع ظ, tr:w-ʿ-ẓ, gloss:yararı gözeten öğüt} kökü iyiyi ve davranışların sonuçlarını hatırlatır; oğula yönelen {ar:لَا تُشْرِكْ, tr:lā tushrik, gloss:Allah’a ortak koşma} buyruğu ile {ar:ظُلْمٌ عَظِيمٌۭ, tr:ẓulmun ʿaẓīmun, gloss:büyük haksızlık} gerekçesi bu öğüdü onu yasaktan çevirmeyi amaçlayan yarar gözetici uyarıya genişletir. Yasak ve gerekçe, tamamlanmış söyleyişi sürmekte olan öğütle birleştirerek oğula yönelmiş ilişkisel müdahale hâline getirir. Bu özel hitapta şefkat uyarının tonunu belirler; bu yerel ton başka öğütlere kural olarak genellenmez. Kalbe sesleniş öğüdün amaçlanan yönelişidir; ayet oğlun fiilî duygusal karşılığını ayrıca bildirmez.

{ar:يَٰبُنَىَّ, tr:yā bunayya, gloss:ey oğulcuğum} birinci tekil iyelikli küçültme biçimiyle gerçek oğula yakınlık ve şefkat katar; biçimin küçültmesi fiziksel boydan çok hitabın sıcaklığını taşır. Şeddeli bitiş, hemen ardından gelen kısa {ar:لَا تُشْرِكْ بِٱللَّهِ, tr:lā tushrik bi-Allāhi, gloss:Allah’a ortak koşma} yasağının eşiğinde bu yakınlığı işitilir kılar. Kabul edilen okuyuşlara ilişkin ses bilgisi bu etkiyi destekler; varyant biçimleri verilmediği için yorum ses etkisiyle sınırlı kalır.

Oğul biçimlerinin bağlı olduğu {ar:ب ن ي, tr:b-n-y, gloss:yapı kurmak} kökünün ayrı bir kullanımında parçalar birleştirilip ayakta duran bir bütün kurulur. Bu yapı kurma kolu, gerçek oğul anlamını taşıyan {ar:ٱبْنِهِۦ / بُنَىَّ, tr:ibnihī / bunayya, gloss:onun oğlu / oğulcuğum} biçimlerini değiştirmeden, öğüt ve yasakla birlikte çocuğun sorumluluk içinde ahlaken biçimlenmesini düşündürür; imge sözün gerçek bir oğula yöneldiği anlamını korur. Bundan ayrı olarak, 31:12’deki {ar:ٱلْحِكْمَةَ, tr:el-ḥikme, gloss:bilgelik} için aktarılan dizgin parçası imgesi {ar:يَعِظُهُۥ, tr:yaʿiẓuhu, gloss:ona öğüt verir} öğüdüyle ve {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} yasağıyla buluşur: bilgece yönlendirme ortaklığa doğru giden yönelişi dizginleyen bir söz gibi duyulur. Yapı imgesi çocuğun biçimlenmesini, dizgin imgesi yönelişin tutulmasını anlatır; ikisi de bu bağlamdaki benzetmelerdir ve dizgin çağrışımı 31:12 ile 31:13 arasındaki temasa özgüdür.

## Yasağın gerekçesi ve açtığı pay

Şefkatli seslenişin içinden gelen {ar:لَا, tr:lā, gloss:olumsuz emir parçacığı} hitabı doğrudan yasağa taşır; yakınlık buyruğun içinde sürer. {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma}, IV. bâbda ikinci tekil eril ve cezmli muzari fiildir; eylem böylece anlatıcının betimi değil, oğula yöneltilmiş talimattır. Fiile eklenen {ar:بِ, tr:bi, gloss:ile} edatı ortaklık ilişkisini tamamlayıp hedefi belirtir. Bu hedef {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} özel adıyla verilir: Allah genel bir tanrı kategorisi değil, edatın yönettiği isim ve yasağın belirli hedefidir. Yapı hedefi gösterir; cümle Allah’a sesleniş, dua ya da ant işlevi taşımaz.

Doğrudan yasağın ardından {ar:إِنَّ, tr:inna, gloss:gerçekten} vurgulu açıklamayı açar; bu açıklama buyruğun gücünü sürdürüp ona ayetin içinden gerekçe verir. Eylem bildiren {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} bu kez {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} biçimindeki belirli soyut adla konu edilir: ad, {ar:إِنَّ, tr:inna, gloss:gerçekten} cümlesinin ismidir ve ortak koşma kavramını gösterir. {ar:ش ر ك, tr:sh-r-k, gloss:ortaklık} kökünün paylaşım ve kapan kullanımları bu kavrama arka plan tonu verir; burada ad bir ortağı ya da fiziksel ağı değil, kategoriyi belirtir. {ar:لَ, tr:la, gloss:vurgulayıcı lâm} vurguyu yükleme taşır; belirsiz {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} cümlenin yüklemi olarak şirki doğrudan haksızlık diye sınıflandırır. Böylece fiil aynı dinî anlamla isim görevine döner ve belirli davranışı yargılanan kavrama açar. Bu ilke ayetin kendi içinde kurulur; önceki bir bağlama dayanmaz ve ilerleyen aile sahnelerine yinelenen hazır formül olarak taşınmaz. {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} eril, tekil ve belirsiz uyumuyla aynı haksızlığın ölçeğini verir; {ar:ظُلْمٌ عَظِيمٌۭ, tr:ẓulmun ʿaẓīmun, gloss:büyük haksızlık} ayetin sonundaki hükmü toplar. Burada sıfat “büyük” anlamını taşır; felaket ya da övgü unvanı değildir, 31:10’da beliren kemik imgesi ise başka bir kök kolundaki benzetmedir. {ar:يَعِظُهُۥ, tr:yaʿiẓuhu, gloss:ona öğüt verir} ile {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} ayrı köklere ait olsa da ʿayn ve kalın ẓâ sesleri bu öğütle hüküm arasında yerel bir yankı kurar; bu yakınlık daha geniş bir ses düzeni iddiasına dönüşmez.

Haksızlık yargısı ahlaki anlamını korur; {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} birini hakkı olan paydan alıkoyma ya da bir şeyi hak ettiği yer ve sınırdan çıkarma anlamlarını da taşır. Ayrı bir kullanım, somut bir işte uygun zamanın, yerin ya da koşulun bozulmasını anlatabilir. Allah’ı hedef gösteren {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} ile yüklem arasındaki temas, sınırlı ve atfedilmiş bu okumada yanlış pay verme imgesine açılır: Allah’a ait ibadet ve yetki payını başkasına ayırmak, O’na düşen payı esirgemek gibi duyulur. {ar:ش ر ك, tr:sh-r-k, gloss:ortaklık} kökünün dinî kullanımı, başka bir varlığı yalnız Allah’a ait yetki ya da nitelikte ortak saymayı anlatır. {ar:ء ل ه, tr:ʾ-l-h, gloss:ibadet etmek} kökünün ibadet etme ve kendini ibadete verme yönü bu alanı belirginleştirir; aynı kökün türemiş bir kullanımı tapınılan varlığı adlandırabildiğinden Allah özel adı bu yasakta tapınılan hedef olarak da işitilebilir, yine özel ad kalır. Bu pay okuması ibadet ve yetki ilişkisine özgüdür; ayette ayrıca bir ibadet fiili söylenmez. Bu okuma ibadet payıyla sınırlıdır: ẓulmün yer, zaman ve koşul kullanımları gerçek bir taşınma ya da yanlış vakitte yapılan iş sahnesine; ortaklık da insanlar arası mülkiyete dönüşmez. Karanlık imgesi bu ilişkide etkin değildir.

Bu pay ilişkisinden ayrı bir sözlük kolu, {ar:ش ر ك, tr:sh-r-k, gloss:ortaklık} köküne yol oluğu, iz ve geçiş şeritleri anlamları verir. Bu yol imgesi, {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} hükmündeki yanlış payla temas edince güzergâhın yanlış yöne çevrilmesini düşündürür. Aynı kökün avı dolaştırıp yakalayan bağ ya da ağ biçimli kapan kullanımı farklı bir işlem ekler: {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} olağan dinî anlamını korurken {ar:بِٱللَّهِ, tr:bi-Allāhi, gloss:Allah ile} tamamlayıcısı ortaklığın hedefini Allah olarak sabitler ve bu ilişkiye bağlayıcılık verir. Kapanın insanı yakalayıp kendine bağlayan dünya için kullanılan benzetmeli uzantısı da bu bağlanıp kalma hissini derinleştirir. Yol kullanımından yönelişin gidişi, kapan kullanımından ise içinden çıkmanın güçleşmesi gelir; birlikte, dinî yasağın yanlış yöne giden ve bağlayıcı hâle gelen bir ilişki olarak duyulmasına katkı verirler. {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} bu haksızlığın ölçeğini büyütür. Bu atfedilmiş imge yolu ya da kapanı ayette yaşanan olay yapmaz; olağan ortak koşma anlamı taşıyıcıda kalır.

Payın otoriteyle ilişkisi 39:29’daki karşılaştırmada insan ilişkisi üzerinden somutlaşır: çekişen birkaç efendi arasında paylaşılan kişi ile tek efendiye hizmet eden kişi karşı karşıya getirilir. Bu örnek, odaktaki {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} fiili ve {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} adının Allah’a ait yetki payını birden çok çelişen otorite arasında bölünmüş ibadet gibi duyurmasına katkı verir. {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} yetki payını ceza geldikten sonra değil, baştan yanlış yere vermekte gösterir; {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} bu yargının ölçeğini korur. Sahiplik imgesi ibadet ve egemenlik alanıyla sınırlı bir benzetmedir; her beşerî ortaklığı kapsamaz ve fiziksel bir yer değiştirme ileri sürmez.

## Akrabalığın içindeki bakım ve sınır

Oğula yöneltilen yasağın ailede neyi sürdürüp neyi sınırladığını 31:14 ve 31:15 birlikte açar. 31:14’te {ar:حَمَلَتْهُ أُمُّهُۥ, tr:ḥamalathu ummuhu, gloss:onu annesi taşıdı} ve {ar:وَهْنًا عَلَىٰ وَهْنٍۢ, tr:wahnan ʿalā wahnin, gloss:güçlük üstüne güçlük} annenin doğum emeğini; {ar:فِصَٰلُهُۥ فِى عَامَيْنِ, tr:fiṣāluhu fī ʿāmayn, gloss:sütten kesilmesi iki yılda} bakımın süresini gösterir. {ar:أَنِ ٱشْكُرْ لِى وَلِوَٰلِدَيْكَ, tr:ani shkur lī wa-liwālidayka, gloss:bana ve anne babana şükret} çağrısı bağı emek ve şükür borcu içinde kurar. 31:15’te {ar:جَٰهَدَاكَ, tr:jāhadāka, gloss:ikisi seni zorladığında} ve {ar:أَن تُشْرِكَ بِى, tr:an tushrika bī, gloss:bana ortak koşmanı} ebeveyn talebinin sınırını gösterir: şirke itaati {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:ikisine itaat etme} reddederken {ar:وَصَاحِبْهُمَا, tr:wa-ṣāḥibhuma, gloss:ikisiyle beraber ol} ve {ar:مَعْرُوفًا, tr:maʿrūfan, gloss:iyilikle} iyi beraberliği sürdürür. Böylece belirli talep reddedilir, gerçek akrabalık ve bakım borcu kalır. 31:12’deki hikmeti 31:14’ün emeği ve 31:15’in sınırı izlemesi öğüdü aile bağının içine ve sınırına yerleştirir; hikmet arka planı verir, baba-oğul ilişkisi bakım ile düzeltmenin birlikte işlediği yer olur. Babalık bu okumada salt statüden çok çocuğu zararlı talepten koruyan bakım olarak duyulur. 31:15’in doğruya yönelten ebeveynle yanlış talepte bulunan ebeveyni ayırdığı daha dar okuma da açık kalır.

Bu aile sınırı 29:8’de başka bir ebeveyn sahnesinde görünür: anne-babaya iyilik sürerken onların şirk baskısına uyulmaz. Odaktaki {ar:يَٰبُنَىَّ, tr:yā bunayya, gloss:ey oğulcuğum} gerçek baba-oğul bağını korur; {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} için sağlanan ayrı kullanım ise görüşlerin tek çizgide birleşmemesini, yani bağlılıkların ayrışmasını adlandırır. Böylece 29:8 aile içindeki sadakat çatışmasını gösterirken ilişkiyi sürdürür ve ibadet yetkisini sınırlar. Kapan imgesi bu bölünmüş bağlılığı toplumsal bir düğüm gibi derinleştirir; bu çağrışım 29:8’deki aile baskısına aittir ve Lokman’ın babalık sahnesine aktarılmaz.

Akrabalık bağı sorumluluğu birinden ötekine aktarmaya yetmez. 31:33’te ne ebeveyn çocuğun yükünü ne çocuk ebeveynin yükünü üstlenebilir; aldatıcı bir güvence de insanı kendi hesabından kurtarmaz. Odaktaki {ar:بُنَيَّ, tr:bunayya, gloss:oğulcuğum} gerçek soy ve yakınlık bağını korurken, {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} yasağına ilişkin sorumluluk başkasına aktarılamaz. Babanın öğüdü oğula yol gösterebilir, onun hesabını üstlenemez. 31:33 bireysel sorumluluğu genel olarak anlatıyor olabilir; bu nedenle 31:13’le kurulan aile bağı ve şirk ilişkisi bağlamsal bir temas olarak kalır.

## Büyüklük, gizlilik ve taşıyıcı yapı

Oğula sesleniş 31:16’da yeniden gelir; dikkati bu kez yasağın içeriğinden küçük ve gizli eylemin ölçeğine çevirir. {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} hitabının ardından {ar:مِثْقَالَ, tr:miṯqāla, gloss:ağırlık ölçüsü} kadar bir {ar:حَبَّةٍۢ, tr:ḥabba, gloss:tane}, hatta {ar:خَرْدَلٍۢ, tr:ḫardal, gloss:hardal} tanesi gelir. Bu ölçülebilir küçüklük, 31:13’teki {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} haksızlığın olağan büyüklük, güç, değer ya da mevki anlamını korurken görünür hacmi ahlaki ağırlığa doğru genişletir. Tanenin filizlenme ihtimali gizil kalabilecek bir sonucu düşündürür; bu katkı taneyi ayrıca bir tohum alegorisine dönüştürmez. Tane {ar:صَخْرَةٍ, tr:ṣakhra, gloss:kaya} içinde, {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} ya da {ar:ٱلْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} üzerinde bulunsa da {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā llāhu, gloss:Allah onu ortaya çıkarır}. Kayanın kütlesi tanenin küçüklüğüyle karşı karşıya gelir; gizlenme onun önemini azaltmaz. {ar:لَطِيفٌ, tr:laṭīf, gloss:ince ve gizliye nüfuz eden} küçük ve gizli olana ulaşmayı, {ar:خَبِيرٌۭ, tr:ḫabīr, gloss:iç yüzü bilen} işin iç yüzünü bilmeyi ekler; birlikte, insanlar görmese de küçük eylemin hesaba açık kaldığını duyururlar. Bu bağlantıyı kök benzerliği değil, küçüklük-büyüklük ve gizlilik-bilinirlik karşıtlığı taşır. 31:16’nın yalnızca ilahî bilgiyi örneklediği okuma da mümkündür.

Bu küçük ve gizli olanın ölçeğinden ayrı bir soru, yükü hangi yapının taşıdığıdır. 31:10’da dağların yerleştirilip sağlamlaştırılması ve yeryüzünün sarsılmaması taşıyıcı çerçeve görüntüsü verir. {ar:ب ن ي, tr:b-n-y, gloss:yapı kurmak} kök ailesinin kurma kullanımı bedeni taşıyan kaburgaları ve evi ayakta tutan direkleri çerçeveye ekler; {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} için aktarılan yanlış yerleştirme yönü kusurlu desteği, {ar:عَظِيمٌۭ, tr:ʿaẓīmun, gloss:büyük} kök ailesindeki kemik imgesi ise yapısal sertliği düşündürür. Bir desteğin yanlış konması yükün aktarım çizgisini bozabilir; dağların sabitlenmesi doğru desteğin işlevini, sarsılmayan yer de bozulma ihtimalini somutlaştırır. Bu temas yük taşıma benzetmesi olarak kalır: 31:10’un kendisi dağları ve yeryüzünü anlatır, oğul ya da şirk anlatmaz; direk ve kaburga sözcükleri benzetmenin ayrıntısıdır, odaktaki sıfat ise “büyük” anlamını korur.

## Öğüdün karşılaştığı yollar

Bu yapı imgesinden ayrı olarak, aileden aktarılan sözün içeriği 31:21’de miras alınan inançla karşılaştırılır. Oradaki çağrı insanları {ar:ٱتَّبِعُوا۟, tr:ittabiʿū, gloss:izleyin} diyerek {ar:مَآ أَنزَلَ ٱللَّهُ, tr:mā anzala llāhu, gloss:Allah’ın indirdiği şeyi} izlemeye çağırır; cevap {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} {ar:مَا وَجَدْنَا, tr:mā wajadnā, gloss:bulduğumuz şeyi} diyerek {ar:ءَابَآءَنَآ, tr:ābāʾanā, gloss:atalarımız} üzerinde bulunmuş yolu öne çıkarır. İzleme fiilinin tekrarı bağlılığı, “bulmuş olma” gerekçesi hazır devralınmış yolu, atalar sözü de bu yolun soy kaynağını gösterir. Odaktaki {ar:قَالَ, tr:qāla, gloss:dedi}, gerçek oğlu {ar:ٱبْنِهِۦ, tr:ibnihī, gloss:oğlu} ve {ar:بُنَىَّ, tr:bunayya, gloss:oğulcuğum} için söylenen tamamlanmış sözdür; 31:21’deki {ar:قَالُوا۟, tr:qālū, gloss:dediler} de olağan “dediler” anlamını korurken, ardından gelen içerikle benimsenmiş bir görüş bildirir. Burada soy bağı öğüdün kime yöneldiğini belirler; inancın doğruluğunu ise içeriği tartmak belirler. Karşılaştırma, çocuğa yalnızca taklit etmek yerine izlediği yolu değerlendirmeyi öğreten bir öğüt gibi duyulabilir. 31:21’in eleştirisi yanlış miras alınan içeriğe yöneliyor olabilir; bu temas her soy aktarımını geçersiz sayan bir hüküm kurmaz.

Miras alınan içeriğin tartılmasından ayrı olarak, 31:6 ve 31:7 dikkatin nasıl başka yöne çekildiğini gösterir. 31:6’da satın alınan dikkat dağıtıcı söylem insanı yoldan çevirir; 31:7’de işaretler okunup duyulur, fakat dinleyici yüz çevirir ve kulaklarında ağırlık taşır. Odaktaki {ar:قَالَ, tr:qāla, gloss:dedi} sözü başlatan olağan fiildir; {ar:يَعِظُهُۥ, tr:yaʿiẓuhu, gloss:ona öğüt verir} ise muhatabın yararını gözeten uyarıyı bildirir. Bu iki işlev, başka yere çekilmiş dikkati geri çağıran bir karşı-söz etkisi yaratabilir. 31:6 ve 31:7’deki topluluk başka olabilir; benzerlik Lokman’ın bilinçli bir yanıt verdiğini kanıtlamaz.

Dikkat ve aktarım sorularından ayrı olarak, 31:11 ve 31:12 yasağın gerekçesini yaratma ve şükürle buluşturur. 31:11 Allah dışındakilerin ne yarattığını sorar; 31:12 şükrün kişiye döndüğünü ve Allah’ın hiçbir şeye muhtaç olmadığını bildirir. Bu çerçevede {ar:تُشْرِكْ, tr:tushrik, gloss:ortak koşma} paylaşım ilişkisiyle, {ar:ظُلْمٌ, tr:ẓulmun, gloss:haksızlık} yanlış payın yerini gösterir: yaratıcıya ait kredi başka yere yazılır ve şükür yanlış yöne çevrilir; bundan doğan yarar ya da zarar ilahî kudrete değil, bunu yapan insana döner. Yaratıcıyla ortak yazarlık burada bir benzetmedir; haksızlık sözcüğü ahlaki ve hukuki yargısını korur.

Yaratıcıyı doğru adlandırmak ile bağlılığı fiilen bölmek arasındaki mesafe 31:25 ve 31:26’da başka bir soruyla açılır. 31:25’te “gökleri ve yeri kim yarattı?” sorusuna {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} diye doğru cevap verilir; ardından çoğunun bilmediği söylenir. 31:26 göklerde ve yerde olanların Allah’a ait olduğunu ve O’nun hiçbir şeye muhtaç olmadığını bildirir. Odaktaki {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} ile {ar:بِٱللَّهِ, tr:bi-Allāhi, gloss:Allah’a} hedef ilişkisi, sözlü yaratıcı itirafının yanında bağlılığın fiilen bölünüp bölünmediğini de sorar. Bu temas doğru cevabın tek başına ibadetteki bağlılığı açıklamaya yetmediğini gösterir; yaratıcıyı doğru adlandıran herkese gizli bir şirk ithamı yöneltmez. “Bilmemek” şükürle ilgili de olabilir.

Yaratılmışlar arasındaki eşgüdüm, yasağın kapsamını başka bir açıdan belirginleştirir. 31:29’da güneşle ay birlikte hareket eder, bir düzene tâbi tutulur ve belirlenmiş bir vadeye doğru gider. Bu düzenli birliktelik, odaktaki {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} paylaşım ilişkisi ile {ar:بِٱللَّهِ, tr:bi-Allāhi, gloss:Allah’a} hedefinin Allah’a ait ibadet ve egemenlik payını belirlediği okumasını keskinleştirir: yaratılmışların birlikte işlemesi yasaklanan ortak koşma kapsamına girmez. 31:29’u yalnızca ilahî kudretin göstergesi olarak okuma olasılığı da sürer.

Eşgüdüm sahnesinden ayrı olarak, 31:32 kriz anındaki yönelişi gösterir. Dalgalar insanları örter, çalkantı üstüne çalkantı gelir ve bulut gibi bir gölgelik üzerlerine kapanır. O sırada dini Allah’a has kılarak O’na yalvarırlar; kurtulanlar karaya çıkar. Dalgalar ile gölgelik insanın örtülüp kuşatılmasını, yakarış ve karaya çıkış ise tehlike içindeki yöneliş ve kurtuluşu görünür kılar. 6:41’de darlık başka bir kısa sahnede Allah’a yönelişi ve ortak koştuklarını unutmayı açığa çıkarır.

29:8’de aile baskısı, 31:21’de ise atalar yoluna tutunma ayrı bağlamlarda görünür. İlki bağlılık çatışmasını aile ilişkisinin içine yerleştirir; ikincisi miras alınmış yönelişi görünür kılar. Odaktaki {ar:ٱلشِّرْكَ, tr:al-shirka, gloss:şirk} için aktarılan paydaşlık ve bölünmüş görüş anlamları bu iki sahnenin ayrı katkılarını bir arada duymayı sağlar; kapan kullanımı bağlılığın nasıl kuşatıcı olabileceğini ekler. Böylece yanlış ibadet nesnelerinin sabit listesi değil, baskı altında açığa çıkan ve çözülebilen bir dayanma düzeni belirir. 31:21’le kurulan bağ ihtiyatlıdır; 31:32 geçici bir samimiyet anlatıyor olabilir ve kapan katkısı benzetme düzeyinde kalır.

Daha uzak bir ses ve süre teması dikkati kısa dünya nimetine çevirir. {ar:قَالَ, tr:qāla, gloss:dedi} Lokman’ın sözünü başlatan olağan anlamını taşır; bu sözcükle ilişkilendirilen ayrı ve daha uzak bir kök çağrışımı yerinde durmayıp sallanma ya da oynama imgesi verir. 31:24’teki {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} kısa dünya nimetini belirtir. Bu iki bağlantı farklı söz köklerine aittir; bu yüzden sallanma imgesi {ar:قَالَ, tr:qāla, gloss:dedi} fiilinin anlamı olmaz. 31:24 yalnızca geçici nimetten de söz ediyor olabilir. Sınırlı yankı, Lokman’ın sözünü kısa ömürlü haz içinde bağlılığı yerinde tutmaya çalışan bir müdahale gibi duyurur.

</source_prose>
