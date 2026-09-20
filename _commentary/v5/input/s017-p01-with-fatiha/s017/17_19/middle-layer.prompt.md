# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:19**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.middle.claims.json`

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
- Refer to source paragraphs as `17:19 ¶N`.

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

`(17:19 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:19",
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
        "citation": "(17:19 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_19/17_19.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_19/17_19.middle.claims.json \
  --ayah-ref 17:19
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_19/17_19.prose.editorial.tr.md`

<source_prose>
## Koşul ve Sonuç

Ayetin başındaki {ar:وَ, tr:wa, gloss:ve}, söyleyişi önceki metne bağlayıp {ar:مَنْ, tr:man, gloss:her kim} ile açılan koşula geçirir; bu bağ önceki sözün hangi özel karşıtlığını sürdürdüğünü belirlemez. Koşul kimliği verilmeyen her bir kişiye seslenir: {ar:أَرَادَ, tr:arāda, gloss:diledi} ile ahireti istemek, {ar:وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-saʿā lahā saʿyahā, gloss:ona yaraşır biçimde çabaladı} ile o hedefe yönelik emek vermek ve {ar:وَهُوَ مُؤْمِنٌ, tr:wa-huwa muʾminun, gloss:o inanmış haldeyken} bulunmak koşulu birlikte kurar. İsteme ve çaba fiillerinin tamamlanmışlık bildiren biçimleri gerçekleşmiş nitelikleri öne çıkarır; zaman karşıtlığını ayrıca kurmazlar. Fiiller arasındaki {ar:وَ, tr:wa, gloss:ve} çabayı isteğe ekler: dilek, emek ve inanma koşulun ayrı bileşenleridir; istek tek başına onun yerini tutmaz.

İstenen hedef, {ar:أَرَادَ, tr:arāda, gloss:diledi} fiilinin doğrudan nesnesi olan {ar:ٱلْءَاخِرَةَ, tr:al-ākhira, gloss:ahiret} ile açıkça belirtilir. IV. kalıp olağan biçimde istemeyi ve yönelmeyi anlatırken sözlüklerdeki arama, peşinden gitme kullanımı niyete bir arayış tonu katabilir. Ayetin ayrı hareket fiili {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} ve hedefi gösteren {ar:لَهَا, tr:lahā, gloss:ona doğru, onun için} bu tonu amaçlı bir işe bağlar: adlandırılmış sona yönelen emek, isteği belirgin bir başlangıca dönüştürür. Bu sözlük rengi istemenin yönünü derinleştirir; çekimli {ar:أَرَادَ, tr:arāda, gloss:diledi} ise isteyen kişinin olağan dileme anlamını korur. {ar:ٱلْءَاخِرَةَ, tr:al-ākhira, gloss:ahiret} ölümden sonraki hayatı adlandırırken “sonra gelen” ufku da şimdiki emekle gelecekteki hedefi aynı yöne yerleştirir; bu gelecek boyutu işi ertelemek anlamına gelmez.

Hedef, {ar:لَهَا, tr:lahā, gloss:ona doğru, onun için} zamiriyle çabanın içinde de kalır; dişil zamir önceki {ar:ٱلْءَاخِرَةَ, tr:al-ākhira, gloss:ahiret} adına döner ve {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona ait çaba} sözcüğünün sonunda yeniden duyulur. Böylece dileğin nesnesi, işin yöneldiği yer ve çabanın ölçüsüne adını veren son aynı çizgide tutulur. {ar:لَهَا, tr:lahā, gloss:ona doğru, onun için} içindeki lam amacı öne çıkarır; fiille mastar arasına girdiği için okur önce emeğin ne için olduğunu, ardından hedefe uygun çabanın nasıl ölçülüp adlandırıldığını duyar. {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona ait çaba}daki ek, hedefi çabanın sahibi ya da ölçü alınan standart olarak düşündürebilir. Bu iki değer olası okumalar olarak yan yana durur; sahiplik ve ölçü burada genel bir kurala dönüşmez. Arama çağrışımı yönelişi keskinleştirir; sahnenin odağı bir av değil, adı konmuş hedef için yapılan iştir. Zamir zinciri ahireti hedef olarak belirginleştirir; daha geniş bir ahiret öğretisi kurmaz.

Bu hedefe giden iş hem hareket hem emektir. {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} sözlüklerde bir yere doğru amaçlı hareketi, yürüme ve gitmeyi, hızlı yürümeyi ya da hafif koşmayı; ayrıca çalışma, kazanç uğruna uğraşma ve ciddi emek vermeyi kapsar. {ar:لَهَا, tr:lahā, gloss:ona doğru, onun için} hareketin amacını belirler; saʿā'nın sözlük aralığı hız türlerini içerse de ayet belirli bir yolculuk, ibadet yürüyüşü ya da hız şartı koymaz. Burada hareket ve çalışma anlamları birlikte emeğin hem gidişini hem harcanışını duyurur.

Eylemin ardından gelen {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona ait çaba}, aynı kökten mastar olarak fiilin türünü ve ölçüsünü belirginleştirir. Mef'ul-i mutlak kullanımı ilk eylemi yeniden adlandırarak çabanın niteliğini açar; ikinci bir çekimli eylem ya da sayısal kota eklemez. Son hükümdeki {ar:سَعْيُهُمْ, tr:saʿyuhum, gloss:onların çabası} ise aynı emeği cümlenin konusu yapar. Böylece üç kullanım hareketten hedefe uygun ölçüye, oradan değerlendirilen emeğe ilerler: orta halka ilk eylemin ölçüsünü hedefle ilişkilendirir, son halka çabayı yeniden adlandırıp yargıya taşır. {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} diye nitelenen emek bu hat üzerinde okunur; hedef ölçüyü belirler, koşul dilek ve inanmışlığı da birlikte ister.

Koşul, işi yapan kişinin halini de işin yanında tutar. Durum bildiren {ar:وَ, tr:wa, gloss:iken} ile açılan {ar:وَهُوَ مُؤْمِنٌ, tr:wa-huwa muʾminun, gloss:o inanmış haldeyken} cümlesindeki {ar:هُوَ, tr:huwa, gloss:o}, {ar:مَنْ, tr:man, gloss:her kim} ile başlayan aynı kişiye döner. Fiil olmayan {ar:مُؤْمِنٌ, tr:muʾminun, gloss:inanmış}, tekil özneyi niteleyen etkin ortacı olarak inanmayı çabayla aynı anda bulunan bir hal yapar; ayetteki biçim bu halin süresini belirtmez. Sözcüğün olağan anlamı inanmış kişidir; aynı sözlük alanındaki güven, iç yatışıklık ve emniyet tonları ahirete dönük işle birleşebilir. Daha yorumlayıcı okumada inanma hali, gelecekteki ahiret ufkuna duyulan güven ve tasdiki şimdiki emek boyunca taşır, böylece işe devam etme imkânını açıklar. Ayet bu okuma için belirli bir inanç nesnesi ya da açık bir vaat belirtmediğinden, güven tonu olağan inanmışlık anlamını genişleten mümkün bir katman olarak kalır.

Koşuldaki üç nitelik, {ar:فَ, tr:fa, gloss:böylece} ile gelen {ar:فَأُو۟لَٰٓئِكَ, tr:fa-ulāʾika, gloss:işte onlar} sonucuna birlikte taşınır. Başlangıçtaki tekil-genel {ar:مَنْ, tr:man, gloss:her kim}, koşulu her bir kişiye uygular; çoğul gösterme sözü de onu karşılayanları bir sınıf halinde gösterir. Bu sınıf önceden var olan isimsiz bir kurum olarak kurulmaz ve tek tek kişilerin çabasını ortak bir emeğe dönüştürmez: koşulları karşılayanlar sonuçta birlikte anılırken çaba her birinin kendi çabası olarak kalır. Yüklemden önceki {ar:أُو۟لَٰٓئِكَ, tr:ulāʾika, gloss:işte onlar} grubu işaretleyip sonuca retorik ağırlık verir; uzak gösterme biçimi fiziksel mesafe ya da sıralamadaki birincilik anlamı kurmaz. Sözcüğün uzayan okunuşunun sonuç edatıyla {ar:كَانَ, tr:kāna, gloss:oldu} arasında işitsel ağırlık yaratması mümkündür; bu olası ses etkisi zorunlu duraklama ya da tek biçimli bir icra kuralı değildir.

Son yargının konusu doğrudan {ar:سَعْيُهُمْ, tr:saʿyuhum, gloss:onların çabası}dır: mastar kāna'nın öznesi, edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} ise yüklemidir. Böylece emek, onu yapanlardan kopmadan değerlendirmenin odağında durur. {ar:كَانَ, tr:kāna, gloss:oldu}nun olma, bulunma ve gerçekleşme alanı çabayı takdir edilmiş halde sunar ve daha sonra gelebilecek bir karşılıkla bağdaşır. Edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş}, {ar:شُكْر, tr:shukr, gloss:iyiliği tanıma} ailesinin iyiliği bilme, değerini kabul etme ve görünür kılma renkleriyle emeğin kıymetinin tanındığını bildirir. Tanıyan fail açıkta kalır; sözcüğün kendisi bolluk ya da artış imgesi taşımaz. Son konumu ve tenvinli kapanışı çabayı bu tanınmış halde bırakan bir kadans kurar; bu ses etkisi cümle düzeyinde kalır.

## Yön, İnanç ve İstek

Kur'an en dosdoğru olana yol gösterdiğini bildirirken {ar:يَهْدِي لِلَّتِي هِيَ أَقْوَمُ, tr:yahdī li-llatī hiya aqwam, gloss:en doğru olana yol gösterir} der; ardından inananları ve uygun işleri anar (17:9). {ar:أَقْوَمُ, tr:aqwamu, gloss:daha dosdoğru ve dengeli} yönü sağlamlaştırır; bağlamdaki {ar:يَعْمَلُونَ, tr:yaʿmalūna, gloss:iş yaparlar} ile {ar:ٱلصَّٰلِحَٰتِ, tr:al-ṣāliḥāti, gloss:iyi ve uygun işler} ise yönelişin somut işe dönüşmesini ve işin uygunluğunu görünür kılar (17:9). Böylece odaktaki {ar:مُؤْمِنٌ, tr:muʾminun, gloss:inanmış}, rehberlik ve iyi iş birlikteliğiyle yan yana okunabilir; çabanın miktarının yanında nereye yöneldiği ve nasıl bir işe dönüştüğü de belirir (17:9). Bu temas {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi}ya yalnız hız değil yön de ekler. Bağlam 17:19'un koşulunu tanımlamaz ve odaktaki güzergâhın tek başına doğru olduğunu kanıtlamaz; inanma, doğru yön ve eylemin birlikte görülebildiği bir çerçeve sunar (17:9).

İnanmışlığın güven rengi, sorumluluğu gözetme çağrısıyla da temas eder. İnananlara emanetlere ihanet etmemeleri söylenir; {ar:أَمَٰنَٰتِكُمْ, tr:amānātikum, gloss:emanetleriniz} sözcüğü inanmayı güvenilirlik ve kendisine bırakılanı koruma tonuyla duyurabilir (8:27). Başka bir bağlamda inanan kişi iyi iş yapar ve çabası yadsınmayıp kayda geçirilir; bu, inanmışlığı davranışın yanına koyar (21:94). Bu iki temas odaktaki emeği sorumluluk taşıyan bir uygulamayla ilişkilendirir; 17:19 belirli bir emanet, görev ya da inanma nesnesi tayin etmez (8:27, 21:94). Benzerliğin dayanağı 21:94'teki inanma, iyi iş ve kayda geçen çabadır; ayetin diğer biçimleri burada ayrıca çekim çözümlemesine konu edilmez (21:94).

Musa'nın Rabbine hoşnutluk vermek için acele ettiğini söylemesi, amaç ile hızı ayrı ayrı görünür kılar: {ar:وَعَجِلْتُ إِلَيْكَ رَبِّ لِتَرْضَىٰ, tr:wa-ʿajiltu ilayka rabbi li-tarḍā, gloss:razı olman için sana acele ettim} (20:84). Bu karşılaştırmada hızın ayrıca belirtilmesi amaçlı yönelişin hızla aynı ölçü olmadığını gösterir; Musa'nın özgül durumu odağa taşınmaz (20:84). Fâtiha'daki kulluk ve yardım isteme birlikteliği, amaçlı yönelişin yardım arayışına açık boyutunu düşündürür; bu benzetme amaçlı işi kendi kendine yeterli bir çaba saymaz: {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} ve {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} (1:5). Bu, benzetme düzeyinde bir temastır; {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} fiilinin sözlük anlamı ya da 17:19'un alıntısı değildir (1:5).

İman ile ahiret arasındaki yakınlık karşıt bir bağlamda da duyulur: {ar:لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:lā yuʾminūna bi-l-ākhira, gloss:ahirete inanmazlar} diyenlerin yanında acı veren azap anılır ({ar:عَذَابًا أَلِيمًا, tr:ʿadhāban alīman, gloss:acı veren azap}) (17:10). Odakta ise {ar:مُؤْمِنٌ, tr:muʾminun, gloss:inanmış} kişi ahireti isteyen ve ona yönelik çaba gösteren kişiyle aynı koşulda yer alır; karşıt bağlam inanmayı ahirete dönük tutumun eşlikçisi gibi duyurur (17:10). Bu yankı, odak cümlesinde ayrıca belirtilmeyen inanç nesnesini dilbilgisel olarak tamamlamaz; dilek ve emek de koşulun açık bileşenleridir (17:10).

İsteğin yönü belirgin olsa bile istenen şey kendiliğinden iyi seçilmiş olmaz; bu yanılabilirlik insanın kötülüğü de iyiliği çağırır gibi istemesiyle görünür (17:11). {ar:يَدْعُ, tr:yadʿu, gloss:çağırır ve dua eder} eyleminin yanında {ar:ٱلشَّرِّ, tr:al-sharr, gloss:kötülük} ile {ar:ٱلْخَيْرِ, tr:al-khayr, gloss:iyilik} karşı karşıya gelir (17:11). Sonundaki {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} niteliği öne atılma ve acele imgesini ekler; iyi bir şey isteyen kişi kendi yararını yanlış tanıyabilir (17:11). Örnek isteğin yanılabilirliğini keskinleştirir; bu yerel uyarı her insanın niyetine dair eksiksiz bir psikolojiye dönüşmez (17:11).

Yakın hedefi isteyen kişi, isteme yapısı bakımından odağa yaklaşır: {ar:يُرِيدُ ٱلْعَاجِلَةَ, tr:yurīdu al-ʿājila, gloss:hemen olanı ister} (17:18). Ardından {ar:عَجَّلْنَا لَهُ فِيهَا, tr:ʿajjelnā lahu fīhā, gloss:orada aceleyle verdik} ile bu hayattaki pay erkene alınır; alıcı ve payın içeriği isteyen kişinin seçimine değil ilahî dilemeye bağlıdır (17:18). Böylece 17:18, odaktaki ahireti yalnız hızlı varışla ölçülemeyen sonraki bir ufuk olarak düşünmeye açar (17:18). Ayrı bir sözlük kullanımı {ar:أَرَادَ, tr:arāda, gloss:diledi} ailesine işi yumuşakça, yavaşça ya da acele etmeden yapma tonu katabilir; 17:11'deki aceleci insan ve 17:18'deki hızlandırılan pay bu tempo nüansını isteme çevresinde işittirir, ancak odaktaki IV. kalıp olağan biçimde istemek demektir (17:11, 17:18). İki ayet yalnız yakın ve sonraki ufukları karşılaştırıyor da olabilir; bu ilişki tek ve belirleyici bir acele şeması ya da genel bir insan psikolojisi kurmaz (17:11, 17:18).

Hedef ufku, verilecek sonucu tek başına tayin etmez. 11:15 dünya hayatını ve süsünü isteyenlere yaptıklarının karşılığının orada eksiksiz verildiğini bildirir; 42:20'nin ahiret ve dünya hasadı karşılaştırması bu iki sonuç ufkunu ayrı ayrı görünür kılar (11:15, 42:20). Bu temas her dünya arzusunu aynı sonuca bağlamaz ya da kişiler arasında sıralama kurmaz (11:15, 42:20). İyi iş yaptıklarını sananların emeklerinin yitip gidebildiği örnek, çabanın tek başına başarı ölçüsü olmadığını gösterir; başka bir bağlamda inananın iyi işiyle birlikte çabasının yadsınmayıp kayda geçirildiği bildirilir (18:104, 21:94). Biri yanılabilen öz güveni, diğeri korunup kayda geçen emeği gösterir; birlikte okunduklarında hedef, iş ve inanma hali sonuç için önemli yönleri görünür kılar, her çabanın boşa çıkacağına ya da kabul edileceğine dair genel bir dağılım vermez (18:104, 21:94).

17:6 ve 17:8'deki dönüş imgeleri, yönelişin bir dönüşten sonra yeniden başlayabileceği bir tekrar çerçevesi verir (17:6, 17:8). Bir bağlamda {ar:رَدَدْنَا, tr:radadnā, gloss:geri döndürdük} önceki konuma dönüşü, {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:yeni dönüş ve tur} yeniden başlayan bir devri anlatır; ilk fiilin kökü odaktaki {ar:أَرَادَ, tr:arāda, gloss:diledi} ile aynı değildir (17:6). Başka bir yerde {ar:عُدتُّمْ عُدْنَا, tr:ʿudtum ʿudnā, gloss:dönerseniz biz de döneriz} sözü çevrimi koşullu biçimde yeniden açar (17:8). {ar:أَرَادَ, tr:arāda, gloss:diledi} ailesinin ayrı sözlük kullanımları da bir işi yeniden yapmayı ya da aynı iki yer ve yön arasında gidip gelmeyi anlatabilir; kararsızlık bu yinelenen hareketin olası bir uzantısıdır. Temas ortak köke değil, tekrarlanabilir dönüşe dayanır: {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} ve {ar:سَعْيُهُمْ, tr:saʿyuhum, gloss:onların çabası} tek, kesintisiz bir hamle olmak zorunda değildir; dönüşten sonra yeniden ilerleyebilir (17:6, 17:8). Sözlükteki kararsızlık odağın anlamı değil olası bir uzantıdır; bu bağlantı topluluğun anlatısını her bireyin hayatına eksiksiz bir çevrim olarak da taşımaz (17:6, 17:8).

## Tanınma, Kayıt ve Karşılık

17:3'te aynı {ar:شُكْر, tr:shukr, gloss:iyiliği tanıma} ailesinde kişi önce {ar:عَبْدًا, tr:ʿabdan, gloss:kul ve hizmet eden}, ardından {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} diye anılır; ikinci niteleme iyiliği tanıyıp minnettarlık gösteren kişiyi görünür kılar (17:3). Odaktaki edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} yönü tanıyan kişiden emeğin kendisine çevirerek sonuçtan önce işin değerini öne çıkarır (17:3). Bu yön değişimi etkin şükür ile emeğin tanınması arasında yankı kurar; iki sözcük ayrı nitelemelerdir ve 17:3'teki fail ilişkisini odağa aktarmaz (17:3).

İnsanların {ar:شُكْر, tr:shukr, gloss:iyiliği tanıma} göstermesiyle Allah'ın {ar:شَاكِرًا, tr:shākiran, gloss:şükrü tanıyan ve karşılık veren} diye anılması, takdiri karşılıklı ilişki olarak düşünmeye açan olası bir yankı kurar (4:147). Buradaki sözcüğün biçimsel işleyişi ayrıca açıklanmadığından bu okuma morfolojik kesinlik taşımaz (4:147). Odağın edilgen yapısı takdir edeni açık bırakır; 4:147'deki paralellik bu faili 17:19 için adlandırmaz ve iki biçim tek bir olayın kanıtlanmış tersine dönüşünü kurmaz (4:147, 17:3).

76:22, {ar:جَزَآءًۭ, tr:jazāʾan, gloss:karşılık ve ödül} ile {ar:سَعْيُكُم مَّشْكُورًا, tr:saʿyukum mashkūran, gloss:çabanız takdir edilmiştir} ifadelerini ayrı ayrı yan yana getirir; böylece alınan ödülün yanında emeğin kendisinin tanınması da duyulur (76:22). 21:94'te çabanın yadsınmayıp kayda geçirilmesi emeğin değerini korur, bu tanınmayı alınan karşılığın eşanlamlısı yapmaz (21:94). Çoğul hitaptaki {ar:سَعْيُكُم, tr:saʿyukum, gloss:çabanız}, odağın tekil-genel koşuldan çoğul gruba geçişini aynı sa'y sözcüğünün yankısıyla hatırlatır; bağlantı sözcük ortaklığına dayanır, hedef biçimlerinin çözümlemesine değil (76:22). Ödül ihtimali açık kalırken bu yan yanalık insanlar arasında bir rütbe dizisi kurmaz (76:22, 21:94).

Emeğin korunması üç ayrı işlemle görünür: yapılan işin karşılığı eksiksiz verilir (11:15), kişinin çabası ileride görülecektir (53:40), çaba ise yadsınmayıp kayda geçirilir (21:94). Ödeme, görme ve yazma birbirine indirgenmeyen bu işlemler olarak emeği icra anından sonra da görünür ve korunur tutar (11:15, 53:40, 21:94). Yazıya geçirme, {ar:فَلَا كُفْرَانَ لِسَعْيِهِۦ وَإِنَّا لَهُۥ كَٰتِبُونَ, tr:fa-lā kufrāna li-saʿyihi wa-innā lahu kātibūn, gloss:çabası yadsınmaz ve kayda geçirilir} sözlerinde açıkça yer alır (21:94). Bu paraleller {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} sözcüğünü tanımlamaz; odaktaki edilgen takdirin faili ve maddi ödülün biçimi açıkta kalır (11:15, 53:40, 21:94).

Kişiye bağlı emeğin kayda dönüşmesi beden ve yazı imgelerinde somutlaşır (17:13, 17:14). Kişinin payı {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} ve {ar:عُنُقِهِۦ, tr:ʿunuqihi, gloss:onun boynu} sözleriyle boynuna bağlanır; aynı ayette {ar:كِتَٰبًا, tr:kitāban, gloss:yazılı kayıt} çıkarılıp {ar:مَنشُورًا, tr:manshūran, gloss:açılmış ve yayılmış} halde karşısına gelir (17:13). Sonraki ayette kişiye kitabını okuması söylenir; kendi hesabını görmeye yeteceği {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sözüyle belirtilir (17:14). Boyna bağlanan payın yazılıp açılması, ardından kişinin kendi kaydını okuması, işin bitince yok olmayıp sahibi için okunabilir ve geri döndürülebilir kalmasını düşündürür (17:13, 17:14). Sahne genel hesap fikri taşır; 21:94'teki yazıya geçirme korunmuşluk temasını güçlendirirken, 17:19'un edilgen yüklemi belirli bir kitap ya da hesap defterini, kaydın ayrıntılarını ya da failini belirtmez (17:13, 17:14, 21:94).

Üç bağlam kişinin emeğiyle aldığı payı, çabasının kayda geçmesini ve hesapsız rızkı ayrı ilişkiler olarak gösterir (53:39, 21:94, 40:40). Kişinin kendi çabasından aldığı pay {ar:مَا سَعَىٰ, tr:mā saʿā, gloss:çabalayıp çalıştığı} diye anılır (53:39); başka birinde müminin çabası yadsınmaz ve yazılır: {ar:فَلَا كُفْرَانَ لِسَعْيِهِۦ وَإِنَّا لَهُۥ كَٰتِبُونَ, tr:fa-lā kufrāna li-saʿyihi wa-innā lahu kātibūn, gloss:çabası yadsınmaz ve kayda geçirilir} (21:94). Cennette hesapsız rızıklandırılma ise {ar:يُرْزَقُونَ فِيهَا بِغَيْرِ حِسَابٍۢ, tr:yurzaqūna fīhā bi-ghayri ḥisāb, gloss:orada hesapsız rızıklandırılırlar} sözüyle üçüncü bir ilişki kurar (40:40). Sözlüklerdeki çalışma, kazanç ve ciddi uğraş anlamındaki {ar:سَعْي, tr:saʿy, gloss:çalışma ve çaba}, odakta {ar:سَعْيُهُمْ, tr:saʿyuhum, gloss:onların çabası} olarak sahiplik kazanır; çabadan alınan pay ve kayda geçirilen emek kişiyi yaptığı işe bağlar (53:39, 21:94). Hesapsız rızık bu kişisel bağın karşıtı değil, emeğin tanınmasından ayrı bir ilişkidir (40:40).

17:18 ile 17:20, yakın payın dağıtımıyla emeğin takdirini ayrı ölçüler olarak yan yana getirir (17:18, 17:20). Hemen olanı isteyen kişiye bu hayatta payı erkene alınır: {ar:يُرِيدُ ٱلْعَاجِلَةَ, tr:yurīdu al-ʿājila, gloss:hemen olanı ister} ve {ar:عَجَّلْنَا لَهُ فِيهَا, tr:ʿajjelnā lahu fīhā, gloss:orada aceleyle verdik} (17:18). Ardından iki grup birlikte anılır: {ar:هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ, tr:hāʾulāʾi wa-hāʾulāʾi, gloss:bu iki grubun ikisi} için {ar:نُّمِدُّ, tr:numiddu, gloss:uzatır ve destekleriz} denir; kaynak {ar:عَطَآءِ رَبِّكَ, tr:ʿaṭāʾi rabbika, gloss:Rabbinin bağışı}dır ve bu bağış {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} değildir (17:20). İki gruba da uzanan destek, bir grubun emeğine verilmiş özel onay ya da eşit tür ve miktarda pay anlamına gelmez; odaktaki takdir ise bu dağıtımdan ayrı olarak emeğin değerini konu edinir (17:20).

Derece karşılaştırması başka bir ölçüyü görünür kılar: {ar:ٱنظُرْ, tr:unẓur, gloss:bak ve incele} çağrısı, {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:bir kısmını diğerine üstün kıldık} ve {ar:أَكْبَرُ دَرَجَٰتٍ, tr:akbaru darajātin, gloss:dereceler bakımından daha büyük} ile {ar:أَكْبَرُ تَفْضِيلًا, tr:akbaru tafḍīlan, gloss:üstünlük bakımından daha büyük} ifadelerinin ahiretteki derece farklarını göstermesine yöneltir (17:21). Ortak ahiret ufkunda bu farklar belirir; karşılaştırma çabayı rütbeye dönüştüren bir hesap formülü vermez (17:21).

## Verim, Yük ve Tarz

Dağıtım ve dereceyi çabanın takdirinden ayırmak, emeğin değerinin nasıl görünür olacağı sorusunu açar (17:20, 17:21). Bereketli çevre ile uzatılan destek bu görünürlük için iki ayrı büyüme tetikleyicisi sunar: {ar:بَٰرَكْنَا حَوْلَهُۥ, tr:bāraknā ḥawlahu, gloss:çevresini bereketli kıldık} çevredeki bereketi, {ar:نُّمِدُّ, tr:numiddu, gloss:uzatır ve destekleriz} iki gruba doğru süren desteği duyurur (17:1, 17:20). Birincisi ortamı, ikincisi devam eden yardımı öne çıkarır; bunlar ayrı katkılardır, tek bir nedensel dizi oluşturmaz (17:1, 17:20). Bu büyüme imgesinde {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} işi başlatan emek, edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} ise emeğin değerinin görünür olduğu alımlanış gibi duyulabilir (17:1, 17:20). Aynı sözlük ailesindeki ayrı bir kullanım ağacın gövdesinden ya da dibinden çıkan körpe sürgünü ve küçük dalı adlandırır; bu sözcüksel dal, çabanın ardından beliren etkiyi görünür kılar.

Verim imgesinin bir karşılığı, ahiret hasadının artırılmasıdır: {ar:حَرْثَ ٱلْءَاخِرَةِ, tr:ḥartha al-ākhirati, gloss:ahiret hasadı} isteyen için {ar:نَزِدْ لَهُۥ فِي حَرْثِهِۦ, tr:nazid lahu fī ḥarthihi, gloss:hasadını artırırız} denir (42:20). Hedefle ölçüsü belirlenen {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona ait çaba} bu artan hasadın yanında görünür bir verime benzetilebilir (42:20). Aynı sözlük ailesinin ayrı biçimleri az yemle semiren atı {ar:شَكُور, tr:shakūr, gloss:az yemle semiren}, az yağmurla yeşeren bitkiyi ise {ar:أَشْكَر, tr:ashkar, gloss:az yağmurla yeşeren} diye niteler; her biri küçük girdinin belirgin gelişmeye dönüşmesini kendi imgesiyle düşündürür. Bu iki niteleme odaktaki edilgen ortacı {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} ile aynı sözcük ya da çekim değildir. Hasat, at ve bitki çağrışımları emeği görünür verim imgesiyle genişletirken, odaktaki sözcük takdir edilmiş emek anlamını korur; yiyeceğin, yağmurun, bitkinin ya da maddi getirinin biçimi açıkta kalır (42:20).

Verim imgesinden ayrı olarak, {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi} sözlük ailesinin bir başka kolu bağlı kişinin özgürlük bedelini çalışarak kazanıp ödemesine uzanır. Bu dal, kişiye bağlanan pay ve başkasının taşıyamadığı yük imgeleriyle temas eder: {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık}, {ar:عُنُقِهِۦ, tr:ʿunuqihi, gloss:onun boynu} ve {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz} (17:13, 17:15). Boyna bağlanan pay kişinin kendi yükünü, başkasının yükünün üstlenilememesi ise sorumluluğun devredilemeyişini öne çıkarır; bu sözlük dalının ışığında {ar:سَعَىٰ, tr:saʿā, gloss:çaba gösterdi}, kişinin kendi yükünden çıkışına yönelen emek gibi düşünülebilir (17:13, 17:15). Edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} bu serbestleşmeye yönelen işin tanınmasını düşündürür. Bu sözlük imgesi boyna bağlanan payı hukuken silinmiş borç ya da gerçek azat sözleşmesi yapmaz; {ar:فَتَحْرِيرُ رَقَبَةٍۢ مُّؤْمِنَةٍۢ, tr:fa-taḥrīru raqabatin muʾminatin, gloss:mümin bir köleyi özgürlüğe kavuşturma} ise ayrı bir hukuki azat yükümlülüğüdür, ücretli emekle kişinin kendini özgürleştirdiği anlaşma değildir (4:92).

17:22, çalışan yönelişin karşısına oturup kalma ve desteksiz bırakılma görüntüsünü koyar (17:22). Başka ilah edinmeme yasağını {ar:لَّا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhar, gloss:Allah ile birlikte başka bir ilah edinme} izler; ardından kişi {ar:فَتَقْعُدَ, tr:fataqʿuda, gloss:sonunda oturup kalırsın} ve {ar:مَذْمُومًا مَّخْذُولًا, tr:madhmūman makhdhūlan, gloss:kınanmış ve terk edilmiş} diye nitelenir (17:22). Oturuş eylemden çekilmeyi, hatta ayağa kalkamaz hale gelmeyi düşündürebilir; {ar:مَخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} sözü desteksizliği keskinleştirir (17:22). Bu görüntü odaktaki hedefe yönelen emeğe karşı bir duruş kurar; oturuş mahkûmiyetin deyimsel anlatımı da olabileceğinden bu bağlantı bedensel bir zayıflık teşhisi koymaz (17:22). İnanmışlığın güven ve iç dayanak tonu karşıtlığı derinleştirir; dilek ve emek de odaktaki koşulun ayrı bileşenleri olarak kalır (17:22).

17:84, herkesin kendi tarzına göre iş gördüğünü ve Rabbin kimin daha doğru yolda olduğunu daha iyi bildiğini söyler: {ar:كُلٌّ يَعْمَلُ عَلَىٰ شَاكِلَتِهِۦ, tr:kullun yaʿmalu ʿalā shākilatihi, gloss:herkes kendi tarzına göre davranır} (17:84). Bu paralel, {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona ait çaba}nın kişiden kişiye değişen tarzlarda gerçekleşebileceğini düşündürür; kullandığı eylem odaktaki sa'y sözcüğü ya da onun biçim çözümlemesi değildir (17:84). Ortak yöneliş kişisel biçimleri düzleştirmez: tarzlar çeşitlenebilirken kimin daha doğru yolda olduğunu bilme hükmü Rabbe bırakılır (17:84).

</source_prose>
