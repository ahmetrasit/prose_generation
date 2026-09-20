# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:30**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.middle.claims.json`

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
- Refer to source paragraphs as `31:30 ¶N`.

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

`(31:30 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:30",
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
        "citation": "(31:30 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_30/31_30.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_30/31_30.middle.claims.json \
  --ayah-ref 31:30
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_30/31_30.prose.editorial.tr.md`

<source_prose>
## İşaretin kurduğu neden

{ar:ذَٰلِكَ, tr:dhalika, gloss:bu / şu} daha önce konuşulan malzemeye döner; neyi gösterdiği burada yeniden adlandırılmadığından, ayet yeni ve bağımsız bir başlangıçtan çok o malzemenin açıklamasını açar. Ardından gelen {ar:بِأَنَّ, tr:bi-anna, gloss:çünkü / ... olduğu için} sebep bildiren bi’yi vurgulu anna’yla birleştirir ve ilk kimlik bildirimini gerekçenin içine alır: {ar:ٱللَّهَ هُوَ ٱلْحَقُّ, tr:Allāha huwa el-Hakk, gloss:Allah gerçeğin ta kendisidir}. İlk cümleyi izleyen iki {ar:وَأَنَّ, tr:wa-anna, gloss:ve ... olduğunu} da çağrılanlar ve Allah’ın yüce-büyük oluşu hakkındaki hükümleri aynı neden zincirine bağlar. Böylece üç tam önerme tek açıklama içinde ilerler; son önermenin ortadakiyle biçimsel paralelliği bu ayetin yerel düzenidir, işaretin önceki dayanağı ise açık kalır.

İlk cümlede {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} anna’ya bağlı öznedir; eril tekil uyumlu {ar:هُوَ, tr:huwa, gloss:O / O’dur} zamiri özneyi belirginleştirir ve {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} yüklemi gevşek bir niteleme değil, kimlik bildirimi yapar. El-Hakk’ın doğruluk, gerçeğe uygunluk, sağlamlık ve hak olma alanları bu belirli, isimleşmiş yüklemde birlikte duyulur: Allah yalnız doğru bir sözün sahibi değil, hakikat kategorisinin kendisi olarak sunulur. Karşıdaki {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} da çağrılan sınıfa belirli bir yüklem verir; böylece ana karşıtlık doğruyla yanlışın yanı sıra ayakta duran gerçeklikle temelsiz olan arasında kurulur, bu anlam gölgelerinden biri ötekileri dışlamaz.

Bu yüklem karşıtlığını cümlenin çerçevesi taşır. İlk {ar:ٱللَّهَ هُوَ ٱلْحَقُّ, tr:Allāha huwa el-Hakk, gloss:Allah gerçeğin ta kendisidir} bildiriminin ardından çağrılanlara ilişkin orta hüküm gelir; sonra {ar:ٱللَّهَ هُوَ ٱلْعَلِىُّ ٱلْكَبِيرُ, tr:Allāha huwa el-Aliyy el-Kebîr, gloss:Allah yüce ve büyüktür} ile Allah yeniden açık özne olur. Adın ve huwa’nın bu iki uçta yinelenmesi, orta cümleyi iki ilahî kimlik bildirimi arasında tutar. İlk ve son cümledeki huwa eril tekil özneyle uyumludur; ortadaki cümlede zamirin bulunmaması yerel bir sözdizimsel asimetri yaratır, fakat orta hükmü eksik bırakmaz. İlk yüklemin sonundaki sıkı qāf kısa bir işitsel durak verir; orta {ar:وَ, tr:wa, gloss:ve} aynı gerekçeyi sürdürürken yönü karşıt {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} yüklemine çevirir. Böylece olumsuz hüküm ayrı bir ek değil, ilk olumlu kutbun karşısına yerleşen tam bir önerme olur.

## Çağrının yönü

Orta hüküm, önce {ar:مَا, tr:mā, gloss:her ne / ... şeyler} ile kimliği tek tek sayılmayan açık bir çağrılanlar sınıfı kurar, ardından {ar:يَدْعُونَ, tr:yadʿūna, gloss:çağırıyorlar} ile bu sınıfı eylemi üzerinden tanımlar. Fiilin muzari gövdesi ve üçüncü çoğul eki tek seferlik geçmiş bir çağrıdan çok süren toplu bir yöneliş duyurur; ayetin söyleyişi de Allah-huwa kimlik bildiriminden çağıranlar grubunun tasvirine geçer. Çağırmanın olağan çekirdeği sesle ya da sözle birini veya bir şeyi çağırmak, burada ise hedefe çevrilmiş sesleniş ve yakarıştır. Yüzeydeki özne üçüncü çoğuldur; dinleyiciye ikinci çoğulla seslenildiği düşünülebilir, ama başka bir Arapça biçim verilmediğinden okur bu bakış açısını yeni bir lafız saymadan çağrının kime yöneltildiğini düşünebilir.

Bu eylemin hedefe nasıl yöneldiğini {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} açıklar. Min’in yönettiği dūnihi, çağırma fiiline bağlı tümleçtir; dışlama, {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} yüklemi gelmeden önce çağrının içine yerleşir. Dūnihi’deki -hi ilişkiyi Allah’a bağlar; “O’ndan başka” olağan anlamını korurken yakınlık, aşağıda kalma ve hedefin gerisinde olma yönlerini de Allah’a göre düşündürür. Bu yakınlık ve dikeylik çağrının Allah’a göre kurduğu yön ilişkisini belirginleştirir; burada fiziksel koordinat kurulmaz. Ayetin yerel bileşimi çağrının yönünü tek başına açıklar: belirli bir güç ya da önceki kozmik sahne adlandırılmaz, Kur’an geneline yayılan sabit bir formüle de başvurulmaz. Öbeğin sonundaki uzayan ū, hüküm duyulana dek yönelişi işitsel olarak sürdürür; böylece çağrının kaynağı, adresi ve yönü olumsuz yüklemden önce görünür olur.

Bu açık sınıfın yüklemi {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} biçimidir: belirli, etken ortaç, ileride yapılacak bir iptali değil çağrılanların durumunu bildirir. Hüküm mā ile açılan sınıfın tamamına yönelir; tek tek nesne ya da kişiler seçilmez. {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} karşısında yanlışlık, boşluk, normatif haktan yoksunluk ve gerçek bir temele dayanmama gölgeleri birlikte duyulabilir. Belirli yüklem konumu bu geçersizliği tek anlık bir yanlıştan çok kalıcı dayanak yoksunluğu olarak da duyurur. Vurgulu ṭ orta hükme sert bir işitsel iniş verir; ardından gelen wa-anna hem bu yargıyı tam bir önerme olarak nedensel zincirde tutar hem de son ilahî cümleye ritmik geçişi hazırlar.

Olağan okuma açıktır: {ar:ٱللَّهَ هُوَ ٱلْحَقُّ, tr:Allāha huwa el-Hakk, gloss:Allah gerçeğin ta kendisidir}; {ar:يَدْعُونَ مِن دُونِهِ, tr:yadʿūna min dūnihi, gloss:O’ndan başkasına çağırıyorlar} çağrısının hedefleri {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan}dır. Bunun yanında, Allah’ın hakikat ve sağlamlık olarak bildirilmesiyle yöneltilmiş çağrının tapınma alanına değmesi, ayakta duran ve tapınılmaya değer gerçekliği kalıcı temelden yoksun rakip yönelişlerle karşılaştırabilir. Bu ek okumada çağrılan alternatiflerin görünür veya toplumsal etkisi yerinde kalır; etki, kalıcı hakikatin ölçüsü değildir. Böylece odaktaki karşıtlık deneyimlenen yönelişi silmeden, ayakta duran hakikatle kalıcı temelden yoksun olanı ayırır.

Allah adıyla çağrılanlar sınıfı arasındaki fark, eylemin tapınma çevresindeki sözlük kullanımlarını da duyurur. {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} bu cümlede özel addır; {ar:مَا يَدْعُونَ, tr:mā yadʿūna, gloss:çağırdıkları şeyler} ise çağrılan nesneleri açık bir sınıf olarak bırakır. Çağırma ailesinde bir varlığa tapınma eylemi ve bu eylemden türeyen “tapınılan varlık” anlamı da bulunur; {ar:يَدْعُونَ مِن دُونِهِ, tr:yadʿūna min dūnihi, gloss:O’ndan başkasına çağırıyorlar} yönelişi Allah’ı tapınılan varlık, öteki hedefleri çağrılan alternatifler olarak karşı karşıya getirir. Olağan seslenme ve dua çekirdeği bu karşılaştırmanın tabanıdır; tapınma yönü ona eklenir. Bu bağlantı Allah adının kökenini veya sığınma anlamını kesinleştirmez; seslenme, ant, yemek daveti ve belli bir yere yöneltme özel biçimleri de odaktaki çağrıyı belirlemez.

Çağrının bir hak ileri sürme gibi duyulması ise ayrı ve kalıba bağlı bir sözlük koludur. {ar:يَدْعُونَ, tr:yadʿūna, gloss:çağırıyorlar} bazı belirli yapılarda hak ya da aidiyet talep etmeyi; {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} sahibine bağlı istenebilir payı anlatabilir. Aynı ailedeki {ar:حَقّ, tr:ḥaqq, gloss:sahibine bağlı pay veya hak} kullanımı bu payın kime ait olduğunu belirginleştirir; burada duyulan hak, genel bir yükümlülükten çok sahibine bağlı paydır. Buradaki çağrı, karşıt {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} yüklemi ve {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} ilişkisiyle birlikte düşünüldüğünde tapınma hakkının Allah’a ait olduğu ve rakip yönelişlerin bu hak karşısında dayanıksız iddialar gibi kaldığı ihtimalini açar. El-Hakk’ın karşılıklı haklılık iddialarının çekiştiği anlamı bu hak/aidiyet okumasına tartışma görüntüsü katar. Bu bağlantı bir hak ve aidiyet tartısı olarak kalır: ayet belirli mal üzerindeki davayı ya da devri, insan davacıları, mahkemeyi, tarihsel tarafları, soy veya savaş düzenini kurmaz. Son {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} sıfatının yüksekliği bu olası hak iddialarını derece bakımından aşağıda duyurabilir; “O’ndan başkası” olağan anlamı da yerinde kalır. Bu yan okuma olağan yakarışı bir hak ve aidiyet tartısına doğru genişletir.

## Yücelik ve büyüklüğe dönüş

Son {ar:وَ, tr:wa, gloss:ve} orta bâtıl hükmünde durmayıp yönü ilahî tasdike çevirir; peşinden gelen {ar:وَأَنَّ, tr:wa-anna, gloss:ve ... olduğunu} Allah adını yeniden özne olarak kurar. Tekil {ar:هُوَ, tr:huwa, gloss:O / O’dur} zamiri araya yeni bir özne ya da bağlaç girmeden hem {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} hem {ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} yüklemini aynı Allah kimliğine bağlar. Başlangıçta {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan}, kapanışta el-Aliyy ve el-Kebîr olarak görünen aynı Allah, son çiftle ilk yüklemin anlam alanını silmeden yücelik ve büyüklüğe açar. Orta cümleden sonra gelen bu dönüş, daha uzun çağrı bölümünün ardından anna ritmini geri getirip baştaki bi-anna ile açılan üçlü neden dizisini tamamlar; son Allah-huwa sesi ilk cümleyi anımsatırken orta hüküm de yerinde kalır.

{ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} ile {ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} aynı belirli sıfat kalıbında, faʿīl ölçüsünde yan yana duran yerleşik niteliklerdir. Bu yan yana geliş ayetin kendi ikili kapanışıdır: başka sûrelerden taşınmış bir formüle dayanmaz, sıfatları da geçici yükselme ya da büyüme olayı değil yerleşik nitelikler olarak duyurur. İlk sıfatın burada Allah’a yüklenmesi bir yükselme eylemini veya insanın yükseklik iddiasını anlatmaz. El-Kebîr’in son sözcük oluşu kapanışı mühürler; Aliyy’nin önce gelmesi duyulan sıradır, üstünlük sırası değil. Aynı nedensel çerçevedeki bu son çift, çağrılan rakiplerin bâtıllığına zemin olarak okunabilir; bu, ayetin içindeki dönüşün açtığı yerel bir ilişkidir. Çağrıda Allah’a bağlanan tapınma yönü de özel adın kökenini açıklamadan son öznenin aynı tapınılan varlık olarak dönmesini sağlar.

Çağrının {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} yönü, {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} ile karşılaşınca hem dikey imgeyi hem saygın mevkiyi açar. Dūn’un bazı kullanımları yakınlık, aşağıda kalma ya da hedefin gerisinde olma ilişkisi kurar; burada çağrı fiili, {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} hükmü ve el-Aliyy’nin yüksek kutbuyla birleşince bu ilişkileri rakip hedeflerin değer ve derece bakımından geride kalmasına taşıyabilir. “O’ndan başkası” olağan anlamı da bu okuma içinde yerini korur. Bu dikeylik ve mevki Allah’a göre kurulmuş ilişkidir; fiziksel konum bildirmez. El-Aliyy’nin bazı özel yapılardaki üstün gelip bastırma anlamı burada eylem olarak değil, çağrı–dūnihi–bâtıllık bileşiminin kurduğu otorite yankısı olarak duyulur. Böylece yücelik olağan yükseklikle birlikte değerli mevkiyi de taşır.
{ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} dikey imgeyi ölçü, miktar, sayı ve göreli derece anlamlarıyla daha geniş bir ölçeğe taşır; {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} ise ayrı yükseklik kutbunu korur. Böylece beden hacmine sığmayan genel derece ve ululuk da çiftte duyulur. El-Kebîr’in saygınlık ve önderlik mevkii anlamı, el-Aliyy ve dūnihi’nin açtığı ilişkiyle birlikte düşünülebilir; insan önderliği, toplumsal rütbe ve kuşaktan aktarılan kıdem burada Allah’a yüklenmez. İnsanın kendini büyük gösterdiği kibir başka biçimlerde anlatılır. Son çift böylece ölçü, mevki ve süreklilik eksenlerini aynı özneye taşırken her sıfatın ayrı anlamını korur.

## Bölümün açtığı ölçüler

Çağrının adresi, bölümdeki yaratıcı tanımasıyla pratik sınamaya girer. Gökleri ve yeri kimin yarattığı sorulduğunda muhatapların {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāh, gloss:kesinlikle Allah diyecekler} diyecekleri bildirilir (31:25); bu yanıt, yaratıcıyı Allah diye tanıma ile {ar:يَدْعُونَ مِن دُونِهِ, tr:yadʿūna min dūnihi, gloss:O’ndan başkasına çağırıyorlar} yönelişini başka hedeflere çevirme arasındaki uyuşmazlığı görünür kılar. Bağlamdaki bu gerilim yeni bir sözlük anlamına dayanmaz; 31:25 odaktaki {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} sözcüğünü kullanmaz, fakat sözle tanınan yaratıcı ile eylemdeki yönelişi karşı karşıya getirir. Ardından göklerde ve yerde olanların Allah’a ait olduğu {ar:لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:li-llāhi mā fī as-samāwāti wa-l-arḍ, gloss:göklerde ve yerde olanlar Allah’ındır} bildirimiyle (31:26), her şeyin sahibine göre çağrı adresi belirginleşir. Böylece yaratıcıyı tanıyan söz ile başka yöne çevrilen eylem, odaktaki hak-bâtıl karşıtlığını pratik bir gerilim olarak görünür kılar.

31:26’daki sahiplik, el-Hakk’ın sahibine bağlı pay ve otorite anlamını etkinleştirir. {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} ile {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} çağrının hedefiyle hakkın sahibini ayırırken, {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} ve {ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} bu yönelişi otorite ilişkisi içinde duyurur. Saatin bilgisi Allah’a ayrılır; yağmurun indirilmesi ve rahimlerde olanın bilinmesi, hiçbir nefsin yarın ne kazanacağını ya da hangi yerde öleceğini bilmemesiyle yan yana gelir (31:34). Böylece sahiplik ve insanın erişemediği bilgi, çağrının adresine otorite ağırlığı katar. Bu bağlamdaki hak-pay okuması belirli mal üzerindeki dava ya da devir değildir; buradaki katkı çağrının başarısızlığı değil, yönü ve adresinin ağırlığıdır.

Bu nihai yöneliş yanında insanlara karşı borçlar da yerinde kalır. Şirk uyarısı Allah’a ortak koşmayı dışarıda bırakır (31:13); anne babaya teşekkür ve bakım görevi sürer (31:14). Şirk yönünde itaat sınırlandırılırken ebeveynle iyi beraberlik ve onlara iyilik de korunur (31:15). Ebeveynin çocuk, çocuğun da ebeveyn adına son sorumluluğu üstlenememesi (31:33), en yakın bağın bile nihai hesabı devredemediğini gösterir. Odaktaki {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} ilişkisi nihai çağrıya yön verirken insanî bağları kendi yerinde bırakır. Bu aile örnekleri {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} sözcüğünün bütün anlam alanını tüketmez; Allah’a özgü ibadet ve son hesap ile insanlara karşı minnettarlık ve görev farklı, birlikte taşınan sorumluluklar olarak belirir.

Bölüm daha sonra ilahî sıfatların ölçüsünü genişletir. Yeryüzündeki ağaçlar kalem, deniz mürekkep ve yedi deniz de ona eklenmiş olsa Allah’ın sözleri tükenmez (31:27); çokların yaratılması da yeniden diriltilmesi de tek bir nefisle karşılaştırılır, bu iki eylem ayrı kalır (31:28). Gece gündüze, gündüz geceye katılır; güneş ve ay tabi kılınır, her biri belirlenmiş bir süreye doğru akar (31:29). Bu imgeler sayısal büyüklükten süreli döngüye uzanan farklı ölçekleri görünür kılarken, hiçbir ölçü değişen süreçleri tüketmez; insanın yarını ve ölüm yerini bilememesi de bu yönetimin bilgi ufkunu gösterir (31:34). Bu sahneler {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} ve {ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} sıfatlarını kozmik düzeni yöneten otorite olarak da düşündürür; olağan yücelik ve büyüklük anlamları da bu geniş okumayla birlikte duyulur.

Gerçeklik ve dayanıklılık çizgisi üretimle somutlaşır. Gökler direksiz yaratılır; yere sarsıntıya karşı sabit dağlar konur, canlılar orada yayılır ve yerden büyüme çıkar (31:10). Bu sahne, {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} sözcüğünün sağlamlık yönünü hareket içindeki dayanıklılıkla ve düzenin sonuç vermesiyle duyurur. Ardından “başkaları ne yarattı?” sorusu rakiplerin üretici çıktısını sınar (31:11); {ar:مِن دُونِهِ, tr:min dūnihi, gloss:O’ndan başka / O’nun aşağısında} ilişkisinin “başka/aşağı” yönü de bu bağlamda onları yaratma eşiğinin gerisinde bırakabilir. Bu sınamada {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} yüklemi işe yaramazlık yönünü de görünür kılar: rakipler üretici bir çıktı gösteremez. Sağlam bir kulpa tutunma ise ayrı bir işlemdir: güvenilir zemini elle tutulur kılar (31:22); burada da dayanağı olmayan çağrılar tutunulacak bir kulp vermez. Yaratım sorusu üretme yeterliğini, kulp tutunulacak dayanağı sınar; yük taşıyan düzen doğrudan sözlük karşılığı değil, iki işlemin el-Hakk çevresinde kurduğu imgedir. Bu birleşimde el-Hakk güvenilir bir dayanak gibi duyulur, el-Bâtıl ise ne üretim ne tutunma için sağlam zemin sağlayabilir.

{ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} ailesinin iki kalıpla sınırlı kullanımı bu maddi imgeyi keskinleştirir. {ar:ثَوْبٌ مُحَقَّقٌ, tr:thawbun muḥaqqaq, gloss:sıkı ve düzgün dokunmuş kumaş} iplikleri sıkı ve düzgün dokunmuş kumaşı, {ar:كَلَامٌ مُحَقَّقٌ, tr:kalāmun muḥaqqaq, gloss:sağlam ve iyi kurulmuş söz} ise tutarlı, sağlam kurulmuş ifadeyi anlatır. Odak ayetinde (31:30) kumaş bulunmadığından dokuma, {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} yükleminin temelsiz karşıtlığıyla beliren bir sağlamlık benzetmesidir; {ar:يَدْعُونَ, tr:yadʿūna, gloss:çağırıyorlar} çağrısının söz oluşu ise iyi kurulmuş söz kullanımına temas eder. Ayetlerin, hikmetli kitabın ve hikmetin birlikte anılması (31:2), el-Hakk’ı parçaları birbirine oturan güvenilir bir bütün gibi de duyurabilir; bu niteleme yalnız kitaba ait de olabilir. Aynı bağlam genişlemesi, tükenmeyen ilahî sözleri (31:27), çokların yaratılışıyla diriltilişinin tek bir nefisle karşılaştırılmasını (31:28) ve belirlenmiş süreye akan göksel döngüleri (31:29) ölçeğe bağlı olmayan bir düzen imgesinde buluşturur; bu süreçlerin her biri kendi işlevini korurken 31:30’daki sağlam kurulmuşluk benzetmesine bağlamsal yankı verir. Allah’ın vaadinin {ar:وَعْدَ ٱللَّهِ حَقٌّۭ, tr:waʿda Allāhi ḥaqq, gloss:Allah’ın vaadi haktır} diye anılması (31:33), konuşmanın güvenilirliğini bu iki kalıpla buluşturur; odaktaki el-Hakk böylece bir söylem adına dönüşmeden doğruluk alanını korur.

Vaadin kendisi süre içinde tutunma sınamasını getirir. {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} ile {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} karşıtlığına zaman boyutu eklenir: vaat “hak” diye nitelenir (31:9, 31:33); özellikle {ar:وَعْدَ ٱللَّهِ حَقٌّۭ, tr:waʿda Allāhi ḥaqq, gloss:Allah’ın vaadi haktır} sözü (31:33), gecikse de yerine gelen taahhüt olarak okunabilir. Bu zaman ölçüsü, 31:24’teki kısa hazzı ve 31:33’teki aldatıcı parıltıyı kalıcı vaat iddiasıyla karşılaştırır: anlık haz yaşanabilir, parıltı çekici görünebilir, fakat güvenilirlik süre içinde sınanır. Burada el-Bâtıl’ın süreklilikten yoksunluk yönü belirginleşir; bu karşılaştırmada geçici her haz bâtıl sayılmaz ve el-Hakk vaade indirgenmez. Her vaadin kendi bağlamındaki doğrulanması bu okumanın parçası olarak kalır.

Sağlamlık ile temelsizlik karşıtlığı görünür olanı da aşar. Kaya içindeki hardal tanesi kadar küçük şeyin bulunup çıkarılması (31:16), dirençli kabuğu gizli ama erişilebilir hedefle bir araya getirir; görünen ve gizli nimetlerin birlikte anılması (31:20) görünmezliğin yokluk olmadığını gösterir. Bu ayetlerin başlıca konusu ilahî bilgi ve nimettir: gizlilik bâtıllığın ölçüsü olmaz, fakat her gizli şey de otomatik olarak doğru sayılmaz. Bu bağlamda {ar:ٱلْحَقُّ, tr:el-Hakk, gloss:gerçek ve hak olan} sözcüğünün gerçeklik alanı gizli hedefe erişebilen bir şey gibi de duyulabilir. Sözlük ailesinin uzak, fiziksel bir kolu iç boşluğa nüfuz edip oradakine ulaşmayı anlatır; kayanın içindeki tanecik bu malzeme imgesini çağırır. Bu özel çağrışım gerçeğin görünenden ibaret kalmadığını düşündürür; odaktaki sözcük “delmek” diye çevrilmez ve fiziksel nitelik kazanmaz.

Çağrı yönü, toplumsal izleme ve kriz içinde yeniden sınanır. Atalarının izinden gidenler, kendilerini azaba çağıran şeytanın da çağrısına muhatap olur (31:21); böylece takip eden kişi çağrılan hedefin peşinden giderken kendisi de başka bir çağrı tarafından yönlendirilir. Çağıran, çağrılan ve izleyen bu zincirde buluşur. {ar:يَدْعُونَ, tr:yadʿūna, gloss:çağırıyorlar} fiilinin baskın olmayan fiziksel itme kullanımı burada, miras alınan izleme yönünün toplumsal baskıyla yayılmasını düşündürebilir; odaktaki çağırma ise olağan seslenme ve dua anlamını korur. Yanlış çağrı toplumsal etki yaratabilir; {ar:ٱلْبَٰطِلُ, tr:el-Bâtıl, gloss:asılsız ve geçersiz olan} hükmü bu etkinin haklılık ölçüsüne dönüşmesini önler. Böylece izleme zinciri toplumsal etkinin yanı sıra çağrının dayanak iddiasını da görünür kılar.

Üstlerini gölgelik gibi örten dalgalar ve kuşatıcı tehlike (31:32), baskının örten ve saran niteliğini kurarak yönelişi kriz içinde sınar. Tehlikedekiler {ar:دَعَوُا۟ ٱللَّهَ, tr:daʿaw Allāha, gloss:Allah’a seslendiler} ve {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:mukhliṣīna lahu d-dīn, gloss:dini O’na özgü kılarak} dua eder; çağrı böylece seslenişle birlikte ortaklıktan arındırılmış bağlılığı taşır. Allah onları karaya çıkarıp kurtarır; sonrasında bazıları ölçülü kalırken hıyanet ve nankörlük kriz duasının sonraki bağlılığı tek başına belirlemediğini gösterir. Bu sahne, ataları izleme ve karşı-çağrı zincirinden (31:21) farklı bir baskı koşulunda {ar:يَدْعُونَ مِن دُونِهِ, tr:yadʿūna min dūnihi, gloss:O’ndan başkasına çağırıyorlar} ilişkisinin neyi açtığını gösterir: çağrı tek başına hedefin etiketi değil, çağıran, izleyen ve yönelinen uçları bağlayan yöndür.

Son olarak, ilahî mevki ile insanın kendini büyütmesi arasındaki mesafe davranış imgelerinde belirir. Kendini yüceltme (31:7) çizgisinde, kibirli yürüyüş bedensel gösterişi, övünme ise toplumsal iddiayı taşır (31:18); ölçülü adım ve alçak ses bu iki gösteriyi karşılayan ölçülerdir (31:19). Bir arada düşünüldüklerinde, {ar:ٱلْعَلِىُّ, tr:el-Aliyy, gloss:yüce ve yüksek olan} sıfatının yüksek mevkii ile {ar:ٱلْكَبِيرُ, tr:el-Kebîr, gloss:büyük ve ulu olan} sıfatının büyüklük ve derece alanı insanın bedeni ya da toplumsal itibarıyla kendini şişirmesinden ayrılır. Bu karşılaştırma hak edilmiş yüceliğin insan gösterişinden başka temele dayandığını düşündürebilir; aynı buyruklar yaratılmışların kusurunu düzeltmeye de yönelmiş olabilir. Ölçülü adım bedensel gösterişi dizginler, alçaltılan ses ise ses hacmini etik ölçüye çevirir.

</source_prose>
