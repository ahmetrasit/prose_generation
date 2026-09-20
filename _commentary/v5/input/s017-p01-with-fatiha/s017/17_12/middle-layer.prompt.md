# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:12**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.middle.claims.json`

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
- Refer to source paragraphs as `17:12 ¶N`.

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

`(17:12 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:12",
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
        "citation": "(17:12 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_12/17_12.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_12/17_12.middle.claims.json \
  --ayah-ref 17:12
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_12/17_12.prose.editorial.tr.md`

<source_prose>
## İki İşaretin Kuruluşu

17:11'de insanın aceleci oluşu anılır; 17:12, başındaki {ar:وَ, tr:wa, gloss:ve} ile bu sözün ardından odağı gece ve gündüzün düzenine çevirir. Bağlaç geçişi kurar, nesneyi ya da eylemi kendisi sağlamaz. Düzeni kuran fiil {ar:جَعَلْنَا, tr:jaʿalnā, gloss:kıldık}: yalın anlamıyla bir şeyi belirli bir duruma getirmek veya yerleştirmektir. Gece ile gündüz bu kuruluşta iki nesne, {ar:ءَايَتَيْنِ, tr:āyatayni, gloss:iki işaret} ise onları birlikte niteleyen ikil yüklemdir. Böylece aceleci insanın kısa tepkisinden, birbirini izleyen ve ölçülebilen gök düzenine geçilir; değişim bağlacın değil fiilin taşıdığı bir değişimdir.

İkil biçim işaret sayısını tam ikiyle sınırlar; ardından gelen tekil tamlamalar çifti gecenin ve gündüzün ayrı işaretlerine açar. {ar:ءَايَةَ, tr:āyata, gloss:işaret} burada tanıtan, görülebilir belirti anlamındadır. Gece işaretinin silinmesiyle gündüz işaretinin görmeye açılması bu çekirdeği etkinleştirir; 17:59'da işaret ve görme bağı yeniden kurularak görsel niteliği güçlendirir. Kişi ya da topluluk, metin bölümü ve güneş ışığı anlamları kendi kalıplarına bağlı kalır; sığınma veya dönüş çağrışımı bu bağlantıda ikincildir, çünkü onu ayrıca açan bir tetikleyici yoktur.

Yunus 10:5'te güneş ve ayın düzenlenmesi, işaretleri bilme amacıyla bir araya getirir; bu paralel 17:12'deki gök düzeninin bilmeye açılan yönünü belirginleştirir. 17:11'deki acele karşısında gece ve gündüzün ölçülü kuruluşu da fiilin düzenleyici katkısını duyurur. Bu bağlamda {ar:جَعَلْنَا, tr:jaʿalnā, gloss:kıldık} bir şeyi varlığa ya da yeni bir duruma getirme anlamıyla okunabilir; iki nesne ve {ar:ءَايَتَيْنِ, tr:āyatayni, gloss:iki işaret} yüklemi ise onları işaret diye adlandırma ihtimalini öne çıkarır. Fiilin ad ya da nitelik verme kullanımı sözlükte bulunsa da bu yapıya aitliği kesinleşmemiştir. Bağlamlar düzen ve bilme ilişkisini güçlendirir, fakat “kılmak” ile “öyle adlandırmak” arasındaki tercihi kapatmaz.

17:22'deki {ar:لَا تَجْعَلْ مَعَ اللَّهِ إِلَهًا آخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhar, gloss:Allah'la başka ilah edinme} yasağı ve ardından gelen {ar:فَتَقْعُدَ مَذْمُومًا مَخْذُولًا, tr:fa-taqʿuda madhmūman makhdhūlan, gloss:kınanmış ve terk edilmiş kalırsın} sonucu, atama fiiline etik bir yankı katar: yanlış bir ilah ataması oturup kalma, kınanma ve terk edilmişlikle ilişkilendirilir. Bu bağ, 17:12'deki düzenleyici {ar:جَعَلْنَا, tr:jaʿalnā, gloss:kıldık} eylemini etik bir ufukta duyurur. Yasağın kendisi 17:22'nin bağlamına aittir; bu özel karşılaştırma odak ayeti bir buyruğa dönüştürmez ve fiilin adlandırma mı, durum kurma mı olduğu konusunu çözmez.

## Gecenin İzi

İki üyeli çiftten ayrıntıya geçişi {ar:فَ, tr:fa, gloss:derken} hemen kurar. İlk belirli nesne {ar:ٱلَّيْلَ, tr:al-layla, gloss:gece}, gündüzün karşısındaki yinelenen zaman dilimidir; silme fiili bu zamanın karanlık ve örtülme yönünü de çağırır. Silmenin nesnesini ise {ar:آيَةَ ٱلَّيْلِ, tr:āyata al-layli, gloss:gecenin işareti} tamlaması sınırlar: genitif, gecenin kendisini değil ona ait tekil işareti gösterir. Çetinlik ya da uzunluk bildiren gece anlamları özel tamlamalara bağlıdır; burada zaman çevrimi ve ona ait işaret öndedir.

Bu işarete yönelen {ar:مَحَوْنَآ, tr:maḥawnā, gloss:sildik}, seyrek kullanılan, tamamlanmış ve geçişli bir eylemdir. Birinci çoğul özne silme işini etkin biçimde üstlenir; sözcüğün temel imgesi, yazıdan silinebilen iz gibi bir belirtiyi görünmez kılmaktır. Araçla silme ve adlandırma anlamları başka kuruluşlara bağlıdır. 13:39'daki silme-sağlamlaştırma karşıtlığı da burada silmenin etkin bir işlem oluşunu güçlendirir; bu yankı iki ayetteki nesneleri özdeşleştirmez. Böylece gece işaretinin kayboluşu, aynı öznenin düzen içinde gerçekleştirdiği bir eylem olarak duyulur.

17:78'de gece kıraati, 17:79'da geceye verilen yüksek değer, silme anlatımına karşı gecenin işlevini ve önemini koruyan bir yankı sunar. Böylece {ar:مَحَوْنَآ, tr:maḥawnā, gloss:sildik} fiilinin kapsamı gecenin tamamı değil, geceye ait işaret olarak duyulur. Bu bağlamlar silinen fiziksel belirtinin kimliğini belirlemez; gece ışığının silinmesi mümkün okumalardan biri olarak kalır.

17:1, gecenin başka bir işlevini göstererek silinmenin kapsamını belirginleştirir: {ar:أَسْرَىٰ بِعَبْدِهِ لَيْلًا, tr:asrā bi-ʿabdihi laylan, gloss:kulunu geceleyin yürüttü} sözündeki {ar:لَيْلًا, tr:laylan, gloss:geceleyin} yolculuğun zamanını bildiren zarftır; yol alma imgesi bu kuruluşta doğar. Yolculuğun {ar:لِنُرِيَهُ مِنْ آيَاتِنَا, tr:li-nuriyahu min āyātinā, gloss:ayetlerimizden gösterelim diye} amacına yönelmesi ve {ar:الْبَصِير, tr:al-baṣīr, gloss:her şeyi gören} nitelemesi, gece vakti işaretlerin görülebildiğini de vurgular. Bu bağ gece adını kendi başına yolculuk anlamına taşımaz; odaktaki genitif tamlamanın gösterdiği gece işaretinin kimliği yine açık kalır.

## Gündüzün Görüşü

Silme eylemini izleyen {ar:وَ, tr:wa, gloss:ve}, gündüz işaretinin yapılmasını aynı düzene bağlar, fakat iki işlemi eşitlemez. İlk cümlede {ar:ٱلنَّهَارَ, tr:al-nahāra, gloss:gündüzü} gecenin yanındaki ikinci nesnedir; yeni kuruluşta ise {ar:جَعَلْنَا, tr:jaʿalnā, gloss:kıldık} nesnesi {ar:آيَةَ ٱلنَّهَارِ, tr:āyata al-nahāri, gloss:gündüzün işareti} olur. {ar:مُبْصِرَةًۭ, tr:mubṣiratan, gloss:görmeyi sağlayan} bu işarete verilen niteliktir. Gündüz adı genitif tamlayan olarak işaretin kime ait olduğunu bildirir. Yinelenen fiil böylece başka nesne ve nitelikle işler: gecenin tekil işareti silinirken gündüzün tekil işareti görmeyi sağlar.

Gündüzün olağan anlamı şafaktan gün batımına uzanan aydınlık zaman bölümüdür. 10:67'de {ar:ٱلَّيْلَ لِتَسْكُنُوا۟ فِيهِ وَٱلنَّهَارَ مُبْصِرًا, tr:al-layla li-taskunū fīhi wa-al-nahāra mubṣiran, gloss:gecede dinlenme ve gündüzün görünür olması} gece dinlenmesini gündüz görünürlüğüyle eşler; oradaki eril sıfat gündüzü niteler. 27:86 ve 40:61 de görünür gündüz temasını destekler. Bu formüller 17:12'deki dilbilgisel katkıyı seçik kılar: gündüz görünürlüğünün yanında odak, dişil {ar:ءَايَةَ, tr:āyata, gloss:işaret} ve onunla uyumlu dişil niteliktedir. 10:67'nin dinlenme-görünürlük eşleşmesi de 17:12'de silinenin gecenin kendisi değil ona ait işaret olduğunu belirginleştirir.

Form IV etken ortaç olan {ar:مُبْصِرَةًۭ, tr:mubṣiratan, gloss:görmeyi sağlayan} gözle algılamayı mümkün kılan bir işareti anlatır. Dişil tekil uyum, niteliği eril {ar:ٱلنَّهَارَ, tr:al-nahāra, gloss:gündüz} adına değil, dişil {ar:ءَايَةَ, tr:āyata, gloss:işaret} adına bağlar; böylece işaret yalnız görünür değil, görmeyi mümkün kılan öğe olur. 17:59'da görmeyi sağlayan işaretin yeniden belirmesi bu etkin işlevi pekiştirir. Yoğun biçimde bakma ve yavrunun gözünün açılması anlamları ise başka özel kalıplara aittir.

## Lütuf ve Kaynağı

Görmeye açılan işaretin ardından ilk amaç gelir: {ar:لِّتَبْتَغُوا۟, tr:li-tabtaghū, gloss:arayasınız diye}. Amaç lâmı ve ikinci çoğul kişiye yönelmiş muzari biçim, arayışı yan sonuç değil açık hedef yapar; Form VIII çabalı yönelişi yalın isteme çekirdeğine ekler. Cümledeki nesne ve kaynak bu çabayı belirli lütfa yöneltir. 2:198 ve 17:66'daki lütuf arayışları bu yönelişe yakınlık kurarken, 17:11'deki aceleci isteme karşıt bir ufuk sunar. Bu ayetler aynı sahneyi kurmaz; odaktaki arayışın niteliğini aydınlatır.

Arayışın nesnesi belirsiz ve belirtme durumundaki {ar:فَضْلًۭا, tr:faḍlan, gloss:lütuf}: gereken ya da ölçülü miktarı aşan yarardır. Belirtme durumu lütfu aranan somut şey yapar; sözlük alanındaki gönüllü yarar ulaştırma ve sunanın yükümlü olmadığı bağış anlamları, {ar:مِّن, tr:min, gloss:-den} ile kurulan kaynak ilişkisinde duyulur. Böylece lütuf kazanılmış bir ücretten çok, kaynaktan sunulan bir imkân olarak okunabilir. Neyin verildiği ve miktarı belirtilmediğinden, arayışın amacı genel bir nasip düzeyinde kalır.

Bu kaynak {ar:رَّبِّكُمْ, tr:rabbikum, gloss:Rabbiniz} tamlamasıyla muhataplara bağlanır: genitif ilişki ve ikinci çoğul iyelik eki `-kum`, “sizin Rabbiniz” der. `Min` kaynağı, `rabbikum` ise sahiplik ve düzenleyici yönetim ilişkisini taşır; mutlak Rab adı Tanrı'ya özgüyken bu kullanım muhataplarla ilişkilidir. Lütfun sağlanması ve bilmenin mümkün kılınması, yönetimi sürdürme ve öğretme yönlerini duyurur. Aynı söz ailesindeki gözetileni eksiklikten tamamlanmaya doğru yetiştirme ve bakım anlamı da bu ilişkiye yakın bir imge katar; büyüyen varlık ve ona sunulan bakım kendi nesneleriyle bu imgeyi kurar, Rabbin düzenleyici anlamını değiştirmez.

Gece ve gündüzün insanlara açtığı yarara Kasas 28:73 üç katkı sunar: {ar:جَعَلَ لَكُمُ ٱلَّيْلَ وَٱلنَّهَارَ لِتَسْكُنُوا۟ فِيهِ وَلِتَبْتَغُوا۟ مِن فَضْلِهِۦ, tr:jaʿala lakumu al-layla wa-al-nahāra li-taskunū fīhi wa-li-tabtaghū min faḍlihi, gloss:geceyi dinlenme ve lütuf arayışı için kıldı} ifadesi dinlenmeyi ve {ar:فَضْلًۭا, tr:faḍlan, gloss:lütuf} arayışını eşler, ardından şükür yönünü ekler. Bu eşleşme 17:12'deki gece-gündüz çiftinin gündelik geçimle ilişkisini genişletir. Odak ayet ise işaretlerin arayış ve bilme amaçlarına açılmasını vurgular; iki bağlam birlikte, gece-gündüz düzeninden yararlanmanın işlevlerini belirginleştirir. (28:73)

Lütfun geniş erişimi 17:20'de, Rabbin bağışının iki gruba da ulaşması ve {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} olmamasıyla belirginleşir. {ar:كُلًّا نُّمِدُّ هَٰؤُلَاءِ وَهَٰؤُلَاءِ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:bunlara da şunlara da veririz} kapsamı iki tarafa açar; {ar:عَطَاءِ رَبِّكَ, tr:ʿaṭāʾi rabbika, gloss:Rabbinin bağışı} vereni ve tasarrufunu bildirir, fakat miktarların eşitliğini kurmaz. Bu nedenle arayış tek başına alıcının ahlaki belgesi değildir; lütfun değeri korunur ve insanın çabasına yer kalır. Başlangıç besmelesindeki {ar:الرَّحْمَٰنِ الرَّحِيمِ, tr:al-raḥmāni al-raḥīm, gloss:Rahman ve Rahim} niteliği bu geniş bağış ufkuna eşlik eder `(S:0)`; bu temas 17:12'deki her bir geçimlik yararı ayrı ayrı rahmet diye adlandırmaz. (17:20)

Fātiḥa 1:2'deki {ar:رَبِّ الْعَالَمِينَ, tr:rabb al-ʿālamīn, gloss:bütün âlemlerin Rabbi} kaynağın kapsamını bütün âlemlere açarak 17:12'deki {ar:رَّبِّكُمْ, tr:rabbikum, gloss:Rabbiniz} ilişkisini geniş bir yönetim ufkuna yerleştirir `(1:2)`. Odak ayet muhataplara bağlı kaynağı ve gece-gündüz düzeninin pratik yararını korur; temas tek ayet düzeyindedir ve Fātiḥa'nın bütününü 17:12'ye taşımaz.

Fātiḥa 1:5'teki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:yalnız Sana kulluk eder ve yalnız Senden yardım dileriz}, lütuf arayışına münhasır ilahi yardım yönünü ekler `(1:5)`. Odaktaki {ar:تَبْتَغُوا فَضْلًا مِّن رَّبِّكُمْ, tr:tabtaghū faḍlan min rabbikum, gloss:Rabbinizin lütfunu arayasınız} ile bu temas ayrı kalır: aramak, yardım istemek ve kulluk etmek farklı söz edimleridir. Böylece geçim arayışı ibadetle özdeşleşmeden, insanın yönelişi ve işbirliği korunur.

Ardından 17:21'deki {ar:انْظُرْ, tr:unẓur, gloss:bak} buyruğu lütuf ve ayrıntı dilini karşılaştırmalı bir ufka açar. {ar:فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:faḍḍalnā baʿḍahum ʿalā baʿḍ, gloss:kimini kiminden üstün kıldık} ile {ar:دَرَجَاتٍ, tr:darajātin, gloss:dereceler} sözü kimilerinin kimilerinden ayrılmasını, ahiretteki derecelerin daha büyük oluşu da karşılaştırmanın yönünü gösterir. {ar:فَضْلًۭا, tr:faḍlan, gloss:lütuf} ile üstün kılma aynı sözcük ailesindedir; aranan bağış isim, üstün kılma ise karşılaştırmalı eylemdir. {ar:تَفْصِيلًا, tr:tafṣīlan, gloss:ayrıntılı açıklama} başka bir kök ailesindedir. Bu yankı lütfun bağış değerini koruyarak farklılaştırmayı duyurur; 17:21 odaktaki arayıcıları kendi aralarında derecelendirmez. (17:21)

## Yılları Bilmek

Arayıştan sonra gelen {ar:وَلِتَعْلَمُوا۟, tr:wa-li-taʿlamū, gloss:ve bilesiniz diye}, amaç dizisine ikinci bir yön ekler: insanlar hem lütfu arar hem de bilir. Amaç lâmı ve ikinci çoğul muzari biçim, bilmenin tasarlanmış bir sonuç olduğunu gösterir. Bilmek, burada bir şeyi tanıyıp gerçeğine uygun kavramaktır; öğretme ve haber verme gibi sözlük dalları başka kuruluşlara bağlıdır. İki amaç aynılaştırılmaz: biri aranan yarara yöneliş, öteki gece-gündüz işaretlerinden çıkarılacak bilgidir.

Bu ikinci amaç, gündüz işaretinin görme niteliğini iç kavrayışa doğru genişletir. {ar:مُبْصِرَةًۭ, tr:mubṣiratan, gloss:görmeyi sağlayan} Form IV biçiminin olağan görsel anlamı sürer; ardından gelen bilme amacı ve Yunus 10:5'teki {ar:لِقَوْمٍۢ يَعْلَمُونَ, tr:li-qawmin yaʿlamūn, gloss:bilen bir topluluk için} ifadesi görünürlüğü anlamaya da açar. Aydınlatıcı açıklık, bu işaretin insana görme veya kavrama imkânı vermesi diye de duyulur; ikinci amaç bu etkiyi belirginleştirir. Bilmenin ayırt etme ve yol gösterme çağrışımı, tekrar eden işaret adlarıyla buluşur; işaret ile bilgi yine kendi ayrı katkılarını korur. (10:5)

İki insan amacı, {ar:ٱلنَّهَارَ, tr:al-nahāra, gloss:gündüz} için ayrı bir sözlük dalını da çağırır: başka kuruluşlarda sözcük akarsu yatağını adlandırır. Bu maddi imgede bol suyun taşınması ve akışın toprağı yarıp kanal yatağını belirginleştirmesi birbirinden ayrı katkılardır. {ar:لِّتَبْتَغُوا۟, tr:li-tabtaghū, gloss:arayasınız diye} ve {ar:لِتَعْلَمُوا۟, tr:li-taʿlamū, gloss:bilesiniz diye} amaçları bu taşıma ve yol açma işlemlerini, gündüzün insan eylemlerine sunduğu imkânın imgesi olarak düşündürür. Bu bağlantı odaktaki aydınlık zaman anlamını korur; arayış ve kavrayışın açıldığı yolu maddi bir süreçle görünür kılar, gündüzü akarsuya dönüştürmez.

Bilginin ilk nesnesi {ar:عَدَدَ, tr:ʿadada, gloss:sayısını} olur: birimleri tek tek belirleyip toplam miktara ulaşmak. Belirtme durumundaki sayım, bilme fiilinin nesnesidir; yan zaman zarfı değildir. Sözcüğün topluluğa ekleme ya da belirli bir sayıyı aşma gibi kullanımları başka kuruluşlara aittir. Buradaki sayılan birimler {ar:ٱلسِّنِينَ, tr:al-sinīna, gloss:yılları}: yıllar gece-gündüz çevrimlerini daha geniş zaman birimlerinde toplar. Yıllık çevrim, sayılabilir bir takvim yılı anlamını taşır; hangi takvim veya çağın seçildiği belirtilmez.

Gece ile gündüzün dönüşü ve yılların birikmesi sayımın yanına yineleme hissi getirir; Yunus 10:5'teki ölçülü {ar:مَنَازِلَ, tr:manāzila, gloss:menziller} ise bu göksel döngü için ayrı bir dayanak sunar. Belirli aralıklarla geri gelme anlamı sayma biçiminden tek başına çıkmaz, zaman ve tekrar bildiren özel kuruluşlarda açılır. Aynı kök ailesinin özel kuruluşlarında izlenen yol ya da yerleşik alışkanlık anlamları da döngülerin sürekliliğine yakınlık kurar. Bu yankılar örüntüyü duyururken odakta sayılan şey yıllar olarak kalır; belirli olayların düzenli aralıklarla geliştiği ileri sürülmez. (10:5)

Yunus 10:5 bu yıl hesabını göksel ölçülerle birlikte kurar: güneşin aydınlığı, ayın nuru ve ona belirlenen {ar:مَنَازِلَ, tr:manāzila, gloss:ölçülü menziller} önce gelir; ardından {ar:لِتَعْلَمُوا۟ عَدَدَ ٱلسِّنِينَ وَالْحِسَابَ, tr:li-taʿlamū ʿadada al-sinīna wa-al-ḥisāba, gloss:yılların sayısını ve hesabı bilmeniz için} amacı gelir. Aynı ayetin sonundaki {ar:يُفَصِّلُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ, tr:yufaṣṣilu al-āyāti li-qawmin yaʿlamūn, gloss:işaretleri bilen topluluk için ayrıntılandırır} ifadesi ayrıntılandırmayı işaretleri bilenlere bağlar; 17:12'deki yıllar sayımını gök menzilleriyle, son açıklamayı bilmeyle buluşturur. 6:96 göksel devinimi hesapla, 23:112 ise yerde geçirilen zamanı başka bir ölçekle ilişkilendirir. (10:5, 6:96, 23:112)

Müzzemmil 73:20 gece ve gündüzün ölçüsünü gece nöbetinin insan için taşıdığı sınırla birlikte sunar: {ar:عَلِمَ أَن لَّن تُحْصُوهُ, tr:ʿalima an lan tuḥṣūhu, gloss:onu bütünüyle sayamayacağınızı bildi} nöbetin bölümlerini bütünüyle sayamamayı dile getirir. Bu sınır gece ibadetinin tam ölçüsüne aittir; 17:12'deki yılların sayılabilirliğini daraltmaz. (73:20)

17:4, 17:5, 17:6, 17:7 ve 17:8'deki tarihsel akış sayılmış yıllara başka bir zaman yankısı katar. İki bozulma anlatının tekrar sayısını, ilkinin vaadinin vakti tarihsel sıralamayı, {ar:الْكَرَّةَ, tr:al-karrata, gloss:geri dönüş} ve {ar:وَإِن عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:siz dönerseniz biz de döneriz} ise dönüşü ve koşulunu belirginleştirir; {ar:مَرَّتَيْنِ, tr:marratayn, gloss:iki kez} ile {ar:جَاءَ وَعْدُ أُولَاهُمَا, tr:jāʾa waʿdu ūlāhumā, gloss:ikisinin ilkinin vakti geldi} bu sırayı açıkça kurar. Yılların sayısı tarihsel sonuçları zamana yerleştirmeye yardım eder; iki anlatı arasında ortak bir nedensel saat ya da olayların düzenli aralıklarla tekrarı ileri sürülmez. (17:4, 17:5, 17:6, 17:7, 17:8)

Bu uzun ölçü ufku, 17:11'deki aceleci insan ve 17:18'deki hemen olanı isteyen yönelimle karşılaştırılınca belirginleşir. {ar:عَدَدَ, tr:ʿadada, gloss:sayım} birimleri sayar, {ar:ٱلْحِسَابَ, tr:al-ḥisāba, gloss:hesap} miktarı belirler; acele bu sözcüklerin anlamı değil, ayetlerdeki ayrı karşıtlıktır. {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:her şeyi ayrıntılı biçimde açıkladık} ifadesinin parçalara ayırıp açık etme yönü, aceleyle tekleştirilen zaman ufuklarını yeniden ayırt etmeyi düşündürür. Böylece daha uzun değerlendirme imkânı belirir; karşılaştırma betimleyicidir, bir tedavi yöntemi önermez. (17:11, 17:18)

Yılların sayısına {ar:وَٱلْحِسَابَ, tr:wa-al-ḥisāba, gloss:ve hesabı} eklenince bilmenin ikinci nesnesi açılır. Sayım birimleri tek tek verir, hesap niceliği bulur; ikisi bağlı ama ayrı işlemlerdir. 6:96 ve 10:5 göksel ölçüleri aritmetik hesapla buluşturur; bu nedenle 17:12'de öncelikli anlam zamansal nicelik hesabıdır. Hesabın işi gözetme, davranışı sorgulama ve kamusal düzeni denetleme yönleri de vardır. 17:14'te hesabın kişiye dönmesi bu sorumluluk yankısını etkinleştirir; bu komşu okuma 17:12'deki yılların yerel hesabını değiştirmez. (6:96, 10:5, 17:14)

Hemen ardından 17:13'te her kişinin kendi payı kendisine bağlanır ve açılmış bir kitapla karşılaşır; 17:14'te {ar:اقْرَأْ كِتَابَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} buyruğu kişiden kendi kaydını okumasını ister, kendi nefsinin de ona hesap görücü olarak yeterli olduğu söylenir. Böylece 17:12'nin sayılabilir zamanı ve ayrıntılı açıklaması, kişiye ait okunabilir kayıtla retorik bir süreklilik kurar: ölçülebilen düzenin ardından kişi kendi hesabıyla yüzleşir. Bu, kozmik hesaptan bireysel sorumluluğa geçiştir; gece ve gündüzün amelleri fiziksel olarak yazdığı anlamına gelmez. (17:13, 17:14)

17:15 kişisel hesaba yargısal bir yankı ekler: kişinin kendi sonucu, başkasının yükünün devredilememesi ve elçi gönderilmeden ceza verilmemesi sorumluluğu kişiye ve bildirime bağlar. {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:her şeyi ayrıntılı biçimde açıkladık} odakta parçaları ve anlamları ayırt edip açıklamayı sürdürür; aynı sözlük alanındaki doğruyla yanlışı ayırarak uyuşmazlığı kesin karara bağlama kullanımı 17:15 komşuluğunda yankılanır. Bu yargısal temas o bağlama aittir ve 17:12'deki olağan ayrıntılı açıklama anlamını değiştirmez. (17:15)

Kişisel kayıt ve devredilmeyen yük, {ar:رَّبِّكُمْ, tr:rabbikum, gloss:Rabbiniz} sözündeki yetiştirme imgesine sorumluluk bağlamında bir yankı verir: Rabb, gözetileni eksiklikten tamamlanmaya doğru adım adım büyüten yönetici olarak düşünülebilir. {ar:فَصَّلْنَاهُ, tr:faṣṣalnāhu, gloss:onu ayrıntılandırdık} Form II kuruluşunda parçaları ayırıp açık eder; aynı kökün Form I kuruluşu yavrunun anneden ve emme ilişkisinden ayrılması, yani sütten kesilmedir. 17:13, 17:14 ve 17:15'te kaydın kişiye bağlanması ve sorumluluğun devredilmemesi bu ayrılma imgesini hesap verebilir özerklikle ilişkilendirir. Ayetler anne, çocuk ya da emzirmeden söz etmez; bu, Form II açıklama eyleminin yerine geçen bir anlam değil, olgunlaşma benzetmesidir. (17:13, 17:14, 17:15)

## Her Şeyin Ayrıntısı

İki amaçtan sonra son {ar:وَ, tr:wa, gloss:ve} kapsamı genişleten kapanışı başlatır. Öne alınan {ar:كُلَّ شَىْءٍۢ, tr:kulla shayʾin, gloss:her şeyi} nesnesi odağı gece-gündüz işaretleri ve yıllardan bütün şeyler alanına taşır; belirsiz “şey” olağan geniş anlamını korur, göksel örneklerle sınırlanmaz. Aynı kapsayıcı dil 17:20 ve 17:36'da duyulur, oradaki eylemler kendi bağlamlarında kalır. 6:154 ve 7:145'teki benzer “her şeyi ayrıntılandırma” formülleri bu kapsamı kozmik düzene bağlar. Odak ayette gece ile gündüzün farklı işlevleri ve yılların birimlere ayrılarak sayılması, ayrımların görünür oluşuna somut örnekler verir; buradan bütün gerçekliğin bilinebilir ve bildirilebilir oluşuna uzanan yöntem okuması doğar. Bu okuma “şey”e iradeye özgü yeni bir sözlük anlamı yüklemez. (17:20, 17:36, 6:154, 7:145)

Fiil, öne alınmış nesneyi zamir ekiyle yeniden tutar: {ar:فَصَّلْنَٰهُ, tr:faṣṣalnāhu, gloss:ayrıntılandırdık}. Birinci çoğul özne eylemi tamamlanmış olarak sunar; sonundaki `-hu` nesne eki öne alınmış bütüne döner. Form II, bütünü oluşturan parçaları ve aralarındaki anlam sınırlarını açıklığa kavuşturur. Evrensel nesne ve ardından gelen açıklama adı, fiziksel kesip koparma yerine farkları okunur kılan ayrıntılandırmayı öne çıkarır. 6:97 ve 6:98'de işaretlerin yol göstermesi bu okunabilirliği, 17:11'deki acele ise ayrımları gözeten açıklamanın karşıt ufkunu belirginleştirir. (6:97, 6:98, 17:11)

Sonundaki {ar:تَفْصِيلًۭا, tr:tafṣīlan, gloss:ayrıntılı açıklama}, fiille aynı kökten gelen masdardır; fiile bağlı bu biçim tek açıklama eylemini kuvvetlendirir, ikinci bir eylem eklemez. Böylece evrensel nesne, onu geri tutan zamir ve açıklamayı pekiştiren masdar, bütünün ayrımlarını izlenebilir kılar.

</source_prose>
