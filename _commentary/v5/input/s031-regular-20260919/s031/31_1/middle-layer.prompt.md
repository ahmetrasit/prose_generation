# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:1**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.middle.claims.json`

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
- Refer to source paragraphs as `31:1 ¶N`.

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

`(31:1 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:1",
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
        "citation": "(31:1 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_1/31_1.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_1/31_1.middle.claims.json \
  --ayah-ref 31:1
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_1/31_1.prose.editorial.tr.md`

<source_prose>
## Harf adlarından söze

31:1’de {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} işitilir: elif, lâm ve mîm’in adları. Yüzeyde bir kök sözcüğün türevleri değil, harf adları vardır; okur bunları zorla bir sözlük karşılığına bağlamadan söylenişi koruyabilir. Ardından yüklem gelmediği için bu üç ad başka bir isim ya da fiil cümlesini beklemez; işitilen dizi ayeti kendi başına tamamlar. Sözdizimsel bütünlük, harflerin başka işlevlerini de açık bırakır.

Yazıda {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} tek bir işarette toplanır; tilavette harf adları uzatma ve duraklarla tek tek açılır. Göz sıkı bir biçim görürken kulak aynı işaretin üç adını sırayla duyar. Sesin ağızdaki yolu da bu sırayı belirginleştirir: {ar:ا, tr:elif, gloss:elif} açık bir başlangıç yapar, {ar:ل, tr:lâm, gloss:lâm} dilin yanından akar, {ar:م, tr:mîm, gloss:mîm} dudaklar kapanırken burun sesine yerleşir. Okur anlamdan önce bu kısa ses yolunu izler; duyduğu, harf adlarının telaffuzudur.

{ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} üç ayrı ad olarak bir ayetin içinde birlikte durur. Bu biçim, iki başka sahneyle biçimsel olarak karşılaştırılabilir. Çocuğun iki yılda sütten kesilmesini anlatan {ar:وَفِصَٰلُهُۥ, tr:ve fisâluhu, gloss:ve onun sütten kesilmesi}, ayrılığı ölçülü bir zamana yayar (31:14). {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:diriltilmeniz} yaratılışla birlikte anılır; ikisi {ar:كَـنَفْسٍۢ وَٰحِدَةٍ, tr:ke-nefsin vâhide, gloss:tek bir can gibi} diye anlatılır (31:28). İlk sahne ayrılığın zamana yayılmasını, ikincisi ayrı olguların tek can benzetmesi içinde birlikte anılmasını öne çıkarır. Bu temasların yanında Elif Lâm Mîm’in adları, ayrılıkları silmeden tek bir kıraat eylemi oluşturur. Sütten kesilme ile yaratma ve diriltme kendi ayetlerinin konusudur (31:14, 31:28); açılışa aktarılan, bu sahnelerle kurulan biçimsel benzetmedir.

Kıraat eyleminin ritmi, {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} dizisini bedensel bir ölçü içinde de duyurabilir. Sesten söz eden 31:19, {ar:صَوْتِكَ, tr:ṣawtika, gloss:sesin} ifadesini seslerin en çirkini eşeklerin sesiyle karşılaştırır (31:19). Aynı ayette {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:ve'ġḍuḍ min ṣawtika, gloss:sesini alçalt} sesi denetlemeyi; {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:ve'ḳṣid fî meşyike, gloss:yürüyüşünde ölçülü ol} yürüyüşte orta ölçüyü ister (31:19). Bu öğütlerin Elif Lâm Mîm’in kıraatine taşınması, harf adlarını acele etmeden ve gösterişsizce söyleme benzetmesini doğurur: açılış yalnız gözle seçilen bir biçim değil, ölçülü bir ses temposudur. 31:19 yürüyüş ve konuşma adabını konu edinir; bu kıraat temposu o öğütten açılışa taşınan bir benzetmedir.

Ses temposunun ardından ayetin başlangıçtaki konumu, işitilen harflere bir eşik işi verir. Yazının sıkılığı, tilavetteki ayrılık, kökten türememiş harf adları ve açılış ayetindeki tek öğe oluşu bir araya gelince {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} cümle anlamından önce karşılanan bir girişe dönüşür. Hemen bir önerme gelmediğinden alışılmış kelime anlamı arayışı bir an durabilir; dinleyici önce sesi karşılamaya yönelir. Bu, her dinleyicinin zorunlu tepkisi değil, sözlü önerme taşımayan biçimin açtığı olası işitsel aralıktır. Başlık benzetmesi şifre ya da talimat değil, açılış konumunun adıdır; bu konum okura cümle öncesi bir karşılanma noktası verir.

Eşik işlevi, {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} dizisinin başka işlev ihtimallerini de açık bırakır. Ayrı söylenen adlar baş harflerden kurulacak bir açılıma elverir; ancak ayet hangi ilahî adın ya da sıfatın seçildiğini belirlemez. Harf adları üzerine yemin edilen dil malzemesi olarak da düşünülebilir; ayette yemini kuran bir bağ bulunmadığından bu ihtimal açık kalır. Başka bir okuma, dikkati önermeden sese çevirir. Böylece açılım ihtimali, yemin malzemesi benzetmesi ve sese yönelen dikkat aynı harf adlarının çevresinde yer alır; okur bunları harf adlarının işitildiği zemini koruyarak birlikte düşünebilir.

## İşaret, ses ve karşılanma

Harf adlarının çevresindeki ilk ilişki, sure girişindeki adlandırma biçiminden gelir. Besmele’deki {ar:بِسْمِ, tr:bismi, gloss:adıyla} sözü ad verme ve gösterme alanı açar (31:0); hemen ardından gelen {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} bu yakınlık içinde adı konmuş bir eşik gibi duyulabilir. Yan yanalık adlandırma sürekliliği kurarken harf adları kendi yüzeyinde kalır; böylece açılış, besmelenin ad verme alanını sürdürür.

Aynı dizi başka surelerin başlangıçlarında da yinelenir: {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} 2:1, 29:1, 30:1 ve 32:1’de açılıştadır (2:1, 29:1, 30:1, 32:1). 7:1’de Sâd’ın eklenmesiyle {ar:الٓمٓصٓ, tr:elif lâm mîm sâd, gloss:Elif Lâm Mîm’e eklenen Sâd} dizisi genişler ve ardından {ar:كِتَٰبٌ أُنزِلَ إِلَيْكَ, tr:kitābun unzila ilayka, gloss:sana indirilen bir kitap} sözü gelir (7:1). Bu tekrar, kapalı duran diziyi metne açılan tanınabilir bir başlangıç kalıbı hâline getirir. Kalıbı tanımak biçimsel işlevi görünür kılar; Elif Lâm Mîm’in anlamı açık kalır ve başka ayrık harf başlangıçlarına ortak bir sözlük karşılığı taşıdığı sonucunu doğurmaz.

Bu başlangıç kalıbının ardından gelen işaret ve kitap dili, 31:1’in harflerini cümleden önce duran bir işaret yüzeyi olarak duyurabilir. {ar:ءَايَٰتُ, tr:âyât, gloss:işaretler} işaretleri, {ar:ٱلْكِتَٰبِ, tr:el-kitâb, gloss:kitap} yazılı bütünü adlandırır (31:2); önlerindeki {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} da bu bütünün anlamı çözülmemiş başlangıcı gibi düşünülebilir. Aynı ayette kitap, bilgelik bildiren sıfat biçimiyle {ar:ٱلْحَكِيمِ, tr:el-hakîm, gloss:bilge} diye nitelenir (31:2); Luqmân’a verilen {ar:ٱلْحِكْمَةَ, tr:el-hikme, gloss:hikmet} ise aynı anlam ailesinin başka bir biçimidir (31:12). Biri kitabı niteler, öteki Luqmân’a verilen hikmeti adlandırır; biçim yakınlığı, sabit harf dizisini dağınık kırıntı yerine özenle kurulmuş bir durak gibi duyurabilir. Kitap ve hikmet kendi ayetlerinin konusudur (31:2, 31:12); açılışa taşınan, söze geçmeden önceki ölçülü zamanlama benzetmesidir.

Görünür işaretin yanına bu kez ses gelir. 31:7’de {ar:تُتْلَىٰ, tr:tutlâ, gloss:tilavet edilir} art arda gelen bir okuyuşu anlatır; {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} dizisinin sabit sırası, bu tilavet sahnesinin yanında küçük bir ses geçidi gibi işitilebilir (31:7). Aynı ayette {ar:يَسْمَعْهَا, tr:yesmaʿuhâ, gloss:onları işitir} “sanki işitmemiş gibi” ifadesinde geçer (31:7). Buradaki işitme, sesi duymanın ötesinde anlama ve karşılık vermeye uzanır; böylece açılışın sıralı sesi, nasıl karşılanacağı sorusunu da açar. Bu sahne harflere özel bir mesaj yüklemeden görünür işaretle duyulabilir sırayı birlikte tutar.

Karşılanma sorusu, 31:6 ile 31:7’deki iki ayrı konuşma akışı yan yana geldiğinde belirginleşir. 31:6’daki {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı eğlence} dikkati başka yöne çeker; aynı ifadede {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söz ve haber} yenilenen bir konuşma akışını getirir (31:6). Bu akışın karşısında, içeriği henüz açılmamış {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} dizisinin sabit sesi durur. 31:7’de {ar:تُتْلَىٰ, tr:tutlâ, gloss:tilavet edilir} fiilinin izlediği sıra, tilaveti yönsüz gürültüden ayıran bir düzen kurar; {ar:يَسْمَعْهَا, tr:yesmaʿuhâ, gloss:onları işitir} işitmeyi basit ses alımının ötesinde anlama ve karşılığa uzatır (31:7). Aynı ayetteki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} kulaktaki ağırlığı getirir: ses kulağa ulaşsa bile alımlanma tıkanabilir (31:7). Böylece açılış, dikkati dağıtan söz ile karşılanabilecek tilavet arasında bir dinleme sorusu doğurur; ağırlık imgesi de sesin varlığını alımlanmanın güvencesi saymamayı sağlar. Bu karşıtlık yalnızca sonraki kişilerin tutumunu anlatıyor olabilir; bu olasılık dinleme karşıtlığını bu pasajlar arasındaki bağlantı olarak sınırlar, harflerin başka okumalarını geçersiz kılmaz (31:6, 31:7).

İşitme sorusu, sesin bedende nasıl başladığını da görünür kılar. 31:7’de {ar:تُتْلَىٰ, tr:tutlâ, gloss:tilavet edilir} fiilinin olağan anlamı tilavettir; {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} gerçekten ağızda söylenirken oluşan ses, ağız çalışması ve kulağa ulaşan iz olarak düşünülebilir (31:7). Bu uzak bedensel benzetme ağızda kalan hafif nem ya da iz imgesine kadar uzanır. {ar:يَسْمَعْهَا, tr:yesmaʿuhâ, gloss:onları işitir} fiilinin “işitmemiş gibi” ifadesindeki kullanımı da sesi duyma ile anlamı alımlama arasındaki mesafeyi korur (31:7). Ağızdan kulağa uzanan iz, içerik çözülmeden söylenişin kendisini fark ettirir. Hafif nem imgesi 31:7’nin sözcüksel anlamı değil, harf adlarının bedensel söylenişini somutlaştıran uzak benzetmedir.

## Görünen biçim ve açık kalan anlam

Söylenişin ağızdan kulağa uzanan çizgisinden ayrı bir karşılaştırma, küçük biçimin taşıyabileceği bütünün ölçeğine döner. Göklerin görülebilir direkler olmadan yaratıldığını anlatan bağlamda {ar:عَمَدٍۢ, tr:ʿamadin, gloss:direkler} destek fikrini çağırır (31:10). Bu destek imgesiyle yan yana duran görünür {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı}, aradaki bağ açıklanmamış olsa da daha büyük bir yazılı bütüne açılan küçük bir eşik gibi düşünülebilir. Görünür hacim taşıdığı yapının ölçeğini tek başına belirlemez; bu okumada üç birim daha büyük metni düzenleyen sürdürücü bir merkez imgesi kazanır. {ar:تَرَوْنَهَا, tr:tarawnahâ, gloss:onları görürsünüz} görme fiili gözle seçilen harf yüzeyiyle gözle seçilmeyen taşıyıcı ilişkiyi ayırır (31:10). 31:10’un konusu göklerin yaratılışıdır; açılışa taşınan, harflerin anlamını açıklayan genel bir hüküm değil, görünür yüzey ile görünmeyen destek arasındaki bu benzetmedir (31:10).

Taşıyıcı benzetmesinden ayrı olarak, görünür yüzeyin içte kalanla ilişkisini 31:20 ve 31:16’daki ayrımlar kurar. 31:20 nimetlerin {ar:بَاطِنَةًۭ, tr:bâtıne, gloss:içte kalan} ve {ar:ظَٰهِرَةًۭ, tr:zâhire, gloss:açıkça görünen} yönlerini adlandırır (31:20). 31:16’daki {ar:مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:misḳāle ḥabbatin min ḫardal, gloss:hardal tanesi ağırlığınca} ifadesi küçüklüğün ölçeğini verir; kayanın, göklerin ya da yerin içinde saklı oluşu gizliliği belirginleştirir. {ar:خَبِيرٌۭ, tr:habîr, gloss:her şeyden haberdar} niteliği bu küçücük ve gizli olanı bilgi alanında tutar, {ar:لَطِيفٌ, tr:latîf, gloss:ince ve lütufkâr} ise ondaki inceliği öne çıkarır (31:16). Böylece bir ayet nimetlerin içte kalan ve açıkça görünen yönlerini, diğeri küçüklük ve gizlilik içindeki inceliği sunar. Birlikte düşünüldüklerinde, bütünüyle seçilen yazı ve ses biçimiyle açılmamış bir iç anlamın Elif Lâm Mîm’de yan yana kalabileceğini düşündürür (31:16, 31:20). Bu bağlantı harfler için gizli bir sözlük anlamı belirlemez; görünür biçimin anlam derinliğini tüketmediğini düşündürür.

Görünür biçimi söyleyebilmekle anlamın tümüne sahip olmak arasındaki fark, 31:34’te insan bilgisinin sınırı ile Allah’ın bilgisinin yan yana gelişiyle başka bir karşılık bulur. Allah {ar:خَبِيرٌۭ, tr:habîr, gloss:her şeyden haberdar} diye nitelenirken aynı ayet hiçbir nefsin yarın ne kazanacağını ve hangi yerde öleceğini bilmediğini iki kez söyler ({ar:وَمَا تَدْرِى نَفْسٌۭ مَّاذَا تَكْسِبُ غَدًۭا, tr:wa-mâ tadrî nefsun mâzâ teksibu ġaden, gloss:hiçbir nefis yarın ne kazanacağını bilmez}; {ar:وَمَا تَدْرِى نَفْسٌۢ بِأَىِّ أَرْضٍۢ تَمُوتُ, tr:wa-mâ tadrî nefsun bi-eyyi arḍin temûtu, gloss:hiçbir nefis hangi yerde öleceğini bilmez}) (31:34). Bu iki bilinmeyen kişinin kendi geleceğine dair bilgi sınırını somutlaştırır; ayetin başındaki {ar:عِلْمُ ٱلسَّاعَةِ, tr:ilmu's-sâa, gloss:saatin bilgisi} Allah katındaki bilgiye, sonundaki {ar:عَلِيمٌ, tr:alîm, gloss:her şeyi bilen} niteliği tam bilmeye işaret eder (31:34). Bu bağlam, {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} biçiminin tanınıp söylenebilmesiyle bütün anlamının bilinmesini ayrı tutmaya imkân verir: okur harfleri doğru söyleyebilir, açık kalan anlamı da bir bilgi sınırı olarak taşıyabilir. Tanıma ile anlamın tümüne sahip olma arasında üçüncü bir okuma tutumu belirir. 31:34 insan bilgisinin sınırlarını ve Allah’ın bilgisini anlatır; açılışla kurulan sure içi yankı, doğru söyleyiş ile tam anlam bilgisi arasındaki mesafeyi düşündüren bir okuma benzetmesidir (31:34).

Bilmenin sınırından başka bir ölçeğe geçince, {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} sonlu bir malzeme gibi görünür. 31:27’nin koşullu sahnesinde yerdeki ağaçların {ar:أَقْلَٰمٌۭ, tr:aḳlâm, gloss:kalemler} olması, sınırlı harf maddesini uzayan sözün yazılmasına bağlayan kalem imgesini kurar (31:27). Denizin ardından yedi denizin daha gelmesi bu yazı kaynağını sürekli besler ({ar:وَٱلْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:ve'l-baḥru yemudduhu min baʿdihî sebʿate abḥur, gloss:denizin ardından yedi deniz daha gelmesi}) (31:27). Ayetin sonundaki {ar:مَّا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mâ nefidet kelimâtu'llâh, gloss:Allah’ın sözleri tükenmez} ifadesi bu beslenmenin karşısına tükenmeyen sözleri koyar (31:27). Bu koşullu sahne 31:27’nin kendi konusudur; 31:1’le kurulan bağın tasarlanmış bir ölçek mi yoksa okurun benzetmesi mi olduğu açık kalır (31:27). Bu açıklık içinde, az sayıdaki harf genişlemenin yoksul karşıtı değil, tükenmeyen sözlere açılan bir başlangıç gibi düşünülebilir.

Bu az malzemenin açtığı alan, okurun {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} dizisini nasıl karşıladığını da ölçebilir. 31:12’deki {ar:أَنِ ٱشْكُرْ لِلَّهِ, tr:ani shkuri li-llâh, gloss:Allah’a şükret} buyruğu ve {ar:يَشْكُرُ, tr:yeşkuru, gloss:şükreder} fiilinin yinelenmesi, şükrü görünür bir karşılık olarak öne çıkar (31:12); bu yankı küçük bir girdinin etkisinin açığa çıkmasını düşündürür. Aynı ayette {ar:كَفَرَ, tr:kefere, gloss:nankörlük etti} Allah’a nankörlüğü anlatır; bu kullanıma eşlik eden örtme yankısı, görünür işaretin yüzeyini değiştirmeden üstünün kapanması benzetmesini açar (31:12). Böylece karşıtlık az malzemenin yetersizliğinden okurun işareti nasıl karşıladığına döner: belirsizlik açılmaya ya da görünen yüzeyi aceleyle boşluk sayıp örtmeye yöneltebilir. 31:12’de şükredenin yararı kendisine döner, nankörlük Allah’a eksiklik getirmez (31:12). Sure içi karşıtlık böylece harflerin anlamını değil, okurun açık işaret karşısındaki tepkisini görünür kılan bir benzetmeye dönüşür.

Okurun bu tepkisinin yanında, kısa biçim anlam ilerlerken elde tutulabilecek bir başlangıç noktası da sunar. Allah’a yönelip iyi davranan kişinin {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:sımsıkı tutundu} diye anlatılması tutma eylemini öne çıkarır; devamındaki {ar:بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:bi'l-ʿurveti'l-vuṯḳâ, gloss:sağlam kulpa} bu eylemin dayandığı güvenilir tutamağı adlandırır (31:22). Tekrar söylenebilen {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} da metnin anlamı büyürken dönülüp tutulabilecek sabit bir giriş noktası gibi duyulabilir. 31:22’deki tutuş Allah’a teslimiyet ve iyilik bağlamındadır; açılışa taşınan gizli bir ad ya da çözülme vaadi değil, okuma duruşudur (31:22). Böylece kısa harf dizisi metnin anlamı büyürken dönülebilecek bir tutamak verir.

Bu tutamağın yanına, sabit bir noktadan hareketli bir geçide uzanan başka bir mekânsal benzetme gelir. 31:31’de denizde ilerleyen {ar:ٱلْفُلْكَ, tr:el-fulk, gloss:gemi} Allah’ın işaretlerini gösterir ({ar:ءَايَٰتِهِۦٓ, tr:âyâtihî, gloss:O’nun işaretleri}; {ar:لَءَايَٰتٍۢ, tr:le-âyât, gloss:elbette işaretler}); {ar:تَجْرِى, tr:tecrî, gloss:akar, ilerler} fiili bu sahneye hareket verir (31:31). Dalgaların {ar:كَٱلظُّلَلِ, tr:ke-zulal, gloss:gölgelikler gibi} oluşu çevreleyen bir basınç kurar; {ar:مَّوْجٌۭ, tr:mevc, gloss:dalga} geminin yoluna çalkantı katar (31:32). Böylece gemi ve akış hareketli yolu, Allah’ın işaretleri bu yolun içinden geçilen alanını, gölgelik ve dalgalar ise yolu çalkantılı ve koşulları değişken kılan çevreyi sunar. Birlikte düşünüldüklerinde, bu imgeler kısa {ar:الٓمٓ, tr:elif lâm mîm, gloss:üç harf adı} biçimini daha geniş bir işaret alanına okuru taşıyan küçük bir gemi gibi duyurur; sabit eşik hareketli bir geçide dönüşür (31:31, 31:32). Bu ilişki 31:1’le kurulan hareketli geçit benzetmesinin kapsamıdır: deniz sahneleri kendi bağlamlarında kalır, harflerin sözlük anlamı “gemi” olmaz; bağlantı okuru değişken işaret alanından geçiren mekânsal benzetmedir (31:31, 31:32).

</source_prose>
