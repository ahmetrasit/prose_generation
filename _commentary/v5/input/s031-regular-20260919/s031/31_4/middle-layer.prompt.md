# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:4**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.middle.claims.json`

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
- Refer to source paragraphs as `31:4 ¶N`.

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

`(31:4 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:4",
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
        "citation": "(31:4 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_4/31_4.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_4/31_4.middle.claims.json \
  --ayah-ref 31:4
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_4/31_4.prose.editorial.tr.md`

<source_prose>
## Tanınan kimseler

31:4, önceki söylemde tanınan bir topluluğu {ar:ٱلَّذِينَ, tr:alladhīna, gloss:o kimseler ki} diye niteler: bu kimseler namazı sürdürür, zekâtı verir ve ahirete kesin inanırlar. Belirli eril çoğul ilgi zamiri, önceki söylemde kurulmuş bir sınıfa bağlanır; sınıfın ilk tanıtıldığı yer bu ayetin sözdiziminde yinelenmez. Üç özellik aynı ilgi cümlesinde aynı topluluğa yüklenir; dışa dönük iki pratikle içte taşınan kesinlik birlikte bu kimlik çerçevesini kurar.

Bu geri bağlama yakın çevrede belirginleşir. 31:2’de hikmetli Kitabın ayetleri anılır; 31:3’te {ar:هُدًى وَرَحْمَةً لِّلْمُحْسِنِينَ, tr:hudan wa-raḥmatan lil-muḥsinīn, gloss:iyilik edenler için hidayet ve rahmet} denir. 31:4’teki tanınan topluluk, 31:5’te {ar:أُو۟لَٰٓئِكَ عَلَىٰ هُدًى مِّن رَّبِّهِمْ, tr:ulāʾika ʿalā hudan min rabbihim, gloss:işte onlar Rablerinden bir hidayet üzeredir} diye yeniden gösterilir ve {ar:ٱلْمُفْلِحُونَ, tr:al-mufliḥūn, gloss:başarıya erenler} diye nitelenir. Böylece 31:4, hidayetle ilişkilendirilen bu kimselerin davranış profilini doldurur; ilgi zamirinin geri bağı önceki tanıtımı devralırken üçlü bu yakın bağlamdaki profili tamamlar. Profilin kapsamı tanınan bu gruptur; başka hidayet sahipleri hakkında tüketici bir hüküm vermez.

Bu topluluğun ahiret yönelişi de yakındaki vaatle somutlaşır. 31:8’de iman edip iyi işler yapanlara {ar:جَنَّٰتِ ٱلنَّعِيمِ, tr:jannāti n-naʿīm, gloss:nimet bahçeleri} verilir; 31:9 orada kalışlarını {ar:خَٰلِدِينَ فِيهَا, tr:khālidīna fīhā, gloss:orada kalıcı olanlar} diye niteler ve bunu {ar:وَعْدَ ٱللَّهِ حَقًّا, tr:waʿda Allāhi ḥaqqan, gloss:Allah’ın gerçek vaadi} olarak sunar. Bu devam 31:4’te kesinlikle inanılan ahirete kalıcı bir varış ve gerçek vaat ufku kazandırır. 31:8 ve 31:9’un katkısı bu son ufkun somutluğudur; ödülün bütün ayrıntıları ve grubun tek güdüsü bu bağlamda açılmaz.

## Dışa yönelen pratikten kesinliğe

{ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler}, IV. kalıptaki etken muzari fiilidir ve ardından doğrudan nesnesi {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz} gelir. Fiilin bağlı olduğu söz alanındaki “ayakta tutmak, sürdürmek, işler durumda bırakmak ve gereğini yerine getirmek” yönü bu nesneyle temas edince belirli namaz ibadetinin gereklerini koruma anlamında daralır. Bu fiil-nesne eşleşmesi, topluluğun namazı sürdürmesini yerleşik ve somut bir pratik olarak duyurur.

Belirli {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz}, ayakta durma, rükû, secde, yakarış ve yüceltme aşamalarını taşıyan yükümlü ritüeli adlandırır. Bu bedenli biçim, “namazı ayakta tutma”nın neyi koruduğunu elle tutulur kılar. Fiilin belirgin başlangıcı ile uzayan ünlüsü eyleme işitsel ağırlık verir; ardından gelen kısa namaz adı bu ses akışında bir çıpa olur, sonraki “ve” ise cümleyi yeni eyleme yeniden bağlar.

Bu bağ, {ar:وَيُؤْتُونَ, tr:wa-yuʾtūna, gloss:ve verirler} ile aynı çoğul özne ve ilgi cümlesi içinde sürer. Etken özne olan topluluk, zekâtın alıcısı değil, onu açık nesne olarak veren ve hak sahibine ulaştıran taraftır. Fiilin olağan “vermek, sunmak” anlamına, bağlı olduğu söz alanındaki “gelmek, ulaşmak” kullanımı da {ar:ٱلزَّكَوٰةَ, tr:az-zakāta, gloss:zekât} nesnesiyle temas edince eklenir; yükümlü pay böylece varacağı yere teslim edilen şey olarak duyulur. İki paralel fiilden biri namazı sürdürür, öteki zekâtı ulaştırır; muzari biçim bu verişi topluluğun süreğen niteliği yapar. “Verirler” biçiminin içindeki hemze, ikinci dışa dönük eylemin gelişine kısa bir gırtlak kapanmasıyla işitsel işaret koyar.

Zekâtın bu doğrudan nesne konumu, onu soyut bir arınma başlığı olmaktan çıkarır. {ar:ٱلزَّكَوٰةَ, tr:az-zakāta, gloss:zekât}, yoksula verilmesi gereken ve dinen onun hakkı sayılan mal payıdır; fiil bu payı hak sahibine ödemeyi anlatır. Namazla yan yana gelişi de zekâtı tek başına gönüllü bir hayır bağışına indirmez: yükümlü aktarım anlamı yerinde kalır. Bunun yanında adın söz alanındaki “büyüyüp artma” ile “ahlaken ya da mânen temiz ve düzgün olma” yönlerini burada etkinleştiren şey verme eylemidir. Payın aktarılması böylece arınma ve düzeltme, aynı zamanda iyilikle gelişme olarak da duyulabilir; yankı, mali yükümlülüğün yanına üretkenlik anlamı ekler. Kısa zekât adı, uzun verme fiilinden sonra sıkışık bir ses çekirdeği oluşturur; basık başlangıcı küçük bir işitsel vurgu verir. Eylem dizisinin sonunda ve ahiret cümlesinin hemen önünde durması da maddi aktarımı son ufka bağlayan bir eşik kurar.

Eylem dizisinin ardından gelen {ar:وَهُم, tr:wa-hum, gloss:ve onlar}, yeni bir eylem eklemeden isim cümlesiyle topluluğun hâlini açar; bu yapı aynı çerçevede üçüncü bir nitelik olarak da okunabilir. Bağımsız {ar:هُمْ, tr:hum, gloss:onlar} zamiri aynı çoğul topluluğu yeniden öne alır. İlk “ve onlar” ile sonraki “onlar” arasına alınan {ar:بِٱلْءَاخِرَةِ, tr:bi-l-ākhirati, gloss:ahirete} öbeği iki özne belirtimi arasında çerçevelenir; sonekli fiillerden sonra bağımsız zamirin gelişi de fiil dizisinden isim cümlesine geçişi belirginleştirip son yükleme odak verir. Tekrarlanan zamir bu topluluğun kesinliğini vurgular; başkalarının kesinliği konusunda hüküm kurmaz. “Hum” sesinin yinelenmesi özneden yükleme bağı sıkılaştırır; ikinci zamirin ardından gelen burunlu çoğul sonlanışı cümleyi sesçe kapatır.

Kesinliğin yöneldiği {ar:بِٱلْءَاخِرَةِ, tr:bi-l-ākhirati, gloss:ahirete} öbeği, {ar:بِ, tr:bi, gloss:-e/-a} edatından sonra gelen belirli adıyla mecrurdur ve son {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar} fiiline bağlanır. “Ahiret” en doğrudan anlamı verir; dişil etkin ortaç biçiminden isimleşen bu adın “öncekinden sonra gelen” ya da “başka olan” yönü bilinen ahiret ufkuna sonralık ve ayrılık basıncı ekler. Öbeğin fiilden önce gelişi, okurun önce hedefi duymasını, özne zamirleri arasındaki çerçeveden sonra da yüklemin bu hedefle bağını tamamlamasını sağlar. Namazı sürdürme ile kesinlik “sonraki/başka” ufkunu; zekâtı verme ile kesinlik gecikme ve ertelenmiş sonuç düşüncesini tetikler. Bu bağ, ertelemeyi zekât payının kendisine değil, verişin hemen görünmeyen sonucuna yerleştirir; payın mali niteliği korunurken şimdiki pratikler son ufka yönelir.

Son yüklem {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar}, ilk iki dış pratiğin ardından gelen IV. kalıpta çekilmiş muzari bir fiildir. Kuşkunun giderilmesiyle yerleşen bilgi genel bir inançtan daha belirgin bir kesinlik taşır; biçim bu kesinliğin derecesini sayısallaştırmaz. Fiilin sonda gelişi üçlüyü tamamlar: namazı sürdürme ve zekâtı verme aynı grubun sürmekte olan kesinlik hâlinden kopuk eylemler olarak kalmaz. Öne alınmış ahiret öbeği zamir çerçevesi boyunca bekler ve bu son yüklemle tamamlanır. Bu yerel sıralama tanıdık topluluk tasvirlerine bir sözdizim yankısı verir; burada ileri sürülen bağ ayetin kendi yüklem ve sıra ilişkisidir, ayetler arası bir formüle üyelik iddiası değildir. Hafif {ar:بِ, tr:bi, gloss:-e/-a} edatından sonra gelen ahiret adının başlangıcındaki gırtlak kapanması kısa bir ses eşiği yaratır; öne alınmış öbek bu eşiği geçer ve cümle son fiilin uzayan çoğul sonlanışıyla kapanır. Bu ses konturu vurguyu destekler, anlamın yerini almaz.

## Üç yerel okuma

Bu üç öğeyi birlikte düşünmenin ilk yolu, tekrar eden bakımla kesinliğin birbirini düzenlediğini görmektir. {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} fiilinin gözetme, koruma ve işler durumda tutma yönü, {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz}ın belirli ritüeliyle birleşince tek seferlik bir edimden çok sürekli bakım gibi duyulur. {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} ve {ar:ٱلزَّكَوٰةَ, tr:az-zakāta, gloss:zekât} bu bakımı dışarıya yönelen mal payına taşır; büyüme ve arınma yankıları aktarımı iyilikle gelişme olarak da duyurur. Son olarak {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:ahiret} ufku ile {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar}ın kuşkuyu gideren bilgisi bugünkü tekrarları sonrasına göre düzenler. Bu okuma ayetteki ritüel, mali yükümlülük ve ahiret kesinliğini koruyarak onları birbirine bağlı bir disiplin olarak duyurur.

Aynı eylem dizisi ayrı bir dolaşım imgesine de açılır. Namazı sürdürme, diğer iki kelimenin tetiklemesiyle, bütün devreyi işler tutan temel ya da hayatı ayakta tutan geçim zemini gibi okunabilir. Bu zemine {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} fiilinin olağan aktarımı eklenir; onun suyun geçeceği yolu açıp akışı yönlendirme biçimindeki ayrı sözlük kullanımı da, zekâtın hak sahibine ulaştırılmasını bir kanal boyunca ilerleyen kaynak gibi tasvir eder. Fiilin burada olağan “vermek, ulaştırmak” anlamı sürer; kanal imgesi aktarımın nasıl yön bulduğunu canlandıran ek bir kullanımdır.

Kanal imgesinden ayrı bir taşkın sahnesi aktarımın bölgeler arası hareketini canlandırır: yağmur almış bir yerden gelen su, yağmur almamış başka bir yere ulaşır ve oradan geçer. Bu görüntü kaynağın uzak yere varmasını ve akışın sürmesini somutlaştırır; 31:4’te anlatılmış bir su olayı değil, aktarımı görünür kılan bağımsız bir malzeme imgesidir. Suyun ardından ekinin ya da hurmanın gelişip bol ürün vermesini anlatan, {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} ile aynı söz alanındaki ayrı kullanım bitkinin görünür oluşuyla tetiklenir. Zekâtın artış yönü bu ürünü gelişme ve çoğalma olarak duyurur; ahiretin sonralığı ile kesinlik de bugünkü verişle daha sonra beklenen artış arasına zaman koyar. Bu gecikme imgenin beklenti ufkudur, her aktarım için ölçülebilir bir dünya karşılığı vaadi değildir.

Bedeni hizalayan yerel okuma, bakım ve dolaşım imgelerinden farklı olarak ritüel tekrarın yönelişi bedende prova etmesine odaklanır. {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} fiilinin sürdürme yönü ile {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz}ın ayakta durma, rükû ve secdeyi içeren tekrarlı ritüeli dik duruşu ve bedenin yineleyen hareketlerini öne çıkarır. Son {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar} kararlılıkla işe girişmeyi düşündürür; ritüel, kesin yönelişin tekrar tekrar prova edilmesi gibi duyulabilir. Fiilin bağlı olduğu söz alanının doğrultuyu koruma çağrışımı, ahiret ve kesinlik tetikleyicileriyle çizgiyi sürdürme, denge ve sapmama; doğru yolda kalma, inanç düzeni ve adil söz imgelerine açılır. Sonraki ufuk bedene anlık koşulları aşan bir yön verir, kesinlik bu yönelişi davranışta kararlı kılar. Bu olasılıklı beden okumasında namaz, doğrultu ve dengeyi prova eden pratik olarak belirginleşir.

## Başarı, dikkat ve ekolojik ölçek


Bu üretkenlik, 31:5’teki başarı sözüyle daha geniş bir ufka bağlanır. {ar:ٱلْمُفْلِحُونَ, tr:al-mufliḥūn, gloss:başarıya erenler} sözcüğünün açık anlamı başarıya ulaşanlardır; bir sözlük geleneği başarı alanını sert toprağı yarıp açma ve sürme imgesiyle de ilişkilendirir. 31:5’teki biçim-kök bağlantısı bu toprak imgesini bağımsız olarak doğrulamadığından, bu özel ilişki atfedilmiş bir sözlük yankısı olarak kalır. Zekâtın artış yönü ve yinelenen namaz-veriş pratiğiyle temasında yankı ekinin gelişmesi, çoğalma ve canlıların dolgunlaşması gibi verimli emek imgeleri açar; başarı da kalıcı iyiliğe dönük ürün ufkuna bağlanır. Bu ilişki amelleri zorunlu bir başarı nedeni olarak tanımlamaz.

Verimli emek ufkunun yanı başında, 31:6 ve 31:7 dikkat ile kaynağın ters yöne çevrildiği bir sahne kurar. 31:6’da kişi {ar:يَشْتَرِي, tr:yashtarī, gloss:satın alır} fiiliyle yoldan alıkoyan {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahwa l-ḥadīth, gloss:oyalayıcı söz}ü satın alır; 31:7’de ise {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onu hiç işitmemiş gibi} davranır ve kulağındaki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} anılır. Bu komşu sahnenin 31:4’le kurduğu karşılaştırma, namazın dikkati ibadete çağıran tekrarını ve zekâtın hak sahibine yönelen mal payını, dikkat ile servetin başka yöne ayrılması karşısına koyar. Karşılaştırmanın odağı metinde adı geçen oyalayıcı sözün satın alınmasıdır; satın alanın güdüsü açıklanmaz ve bu örnek her alışverişi zorunlu zekâtla aynı tür ödeme yapmaz.

Bu sahnede {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar}ın yerleşik kesinliği, kısa süreli oyalanmaya karşı istikrarlı bir yöneliş olarak duyulabilir. “İşitmeme”yi sesi duymanın ötesinde hitabı anlayıp ona karşılık verme ilişkisi olarak okuyan bağlam önerisi, kulak ağırlığını hitapla cevap arasındaki tıkanıklığın maddi resmi hâline getirir; 31:6’daki satın alma ile 31:7’deki ağırlık bu okumaya komşu bağlam sağlar. Bu imgeler 31:6 ve 31:7’de açıkça bulunur; 31:4’e dikkat ve kaynak yönüyle bağlanmaları olasılıklı bir yorumdur, bu özel kelime-görev eşlemesi bağımsız biçimbilimsel doğrulama taşımaz. Komşu ayetler kendi başlarına ahlaki bir karşıtlık olarak da okunabilir.

31:10’un yaratılış sahnesi, dağları sarsıntıyı önleyen dayanaklar olarak sunar: {ar:رَوَاسِيَ, tr:rawāsiya, gloss:sağlam yerleşmiş dağlar} için {ar:أَن تَمِيدَ بِكُمْ, tr:an tamīda bikum, gloss:sizinle sarsılıp savrulmaması} ifadesi bu işlevi belirgin kılar. Ardından gökten su inişi, akış ve sulama, bitkilerin yetişmesi ve eşli türler gelir. Dağların desteği, {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} fiilinin işi ya da topluluğu gözetip ayakta tutma yönüyle buluşunca namaz toplumsal hayatı taşıyan altyapı gibi duyulur. Bu bağlantının katkısı dağ imgesindeki dayanak işlevini namazın sürdürülme yönüne taşımaktır; 31:10’un yaratılış odağı sürer ve benzerlik fiilin sözlük açıklaması değil, işlev temelli bir analojidir.

Su ve bitki dizisi dağ dayanağından ayrı iki aktarım kolu açar. 31:10’daki {ar:وَأَنزَلْنَا مِنَ ٱلسَّمَاءِ مَاءً, tr:wa-anzalnā mina s-samāʾi māʾan, gloss:gökten su indirdik} gökten inişi verir; sonraki akış ve sulama, kaynağın yönlendirilmesini görünür kılar. Bu sahne {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} fiilinin su yolunu açıp akışı belirli yöne çeviren ayrı kullanımını tetikler; böylece zekâtın olağan “ulaştırma” anlamına kaynak için açılan bir rota imgesi eklenir. Bitkinin ortaya çıkışı ise başka bir kolu, ekinin ya da hurmanın gelişip bol ürün vermesi kullanımını etkinleştirir; 31:10’daki {ar:فَأَنۢبَتْنَا, tr:fa-anbatnā, gloss:derken bitkileri yetiştirdik} bu verim kolunun somut tetikleyicisidir. Bitkiyi yetiştirme görevinin odak fiile eşlenmesi atfedilmiş bir okumadır; su rotasıyla aynı işlem değildir.

Bitkinin görünür oluşu, zekât adının büyüme ve artış yönünü somutlaştırır: ekin gelişir, canlılar çoğalır ve dolgunlaşır; mali yükümlülük anlamı bu yankıyla birlikte sürer. Bundan ayrı bir sözlük kolu “çift ya da iki öğeli olma”dır. 31:4’te namazla zekâtı bağlayan {ar:وَ, tr:wa, gloss:ve} ve 31:10’daki {ar:زَوْجٍ كَرِيمٍ, tr:zawjin karīmin, gloss:güzel veya soylu bir çift ya da tür} eşli oluşu bu kol için tetikleyici olur. Bu okumanın katkısı tekil büyümeden eşlik ve karşılıklılık ilişkisine geçmesidir; büyüme ve arınma kolundan ayrı tutulur. Eşli tür imgesi 31:10’da açıktır; bunu zekât adındaki özel kullanıma bağlamak ise bağlamsal, atfedilmiş bir eşlemedir ve bağımsız biçimbilimsel doğrulama taşımaz. Bu çağrışım 31:4’e yaratılış anlatısından dönerken 31:10’un başlıca odağı olan yaratılış tasvirini korur.

Bu geniş ekolojinin içinden daha dar bir bileşim de kurulabilir: 31:4’te “ve” ile eşlenen namaz ve zekât, 31:10’un imgeleriyle namazın yapıyı ayakta tuttuğu dayanak ve zekâtın akışa yol veren aktarım olarak okunur; eşli tür imgesi de bu iki işi tamamlayıcı bir çift hâline getirir. Böylece dağ desteği namazın sürdürme yönüyle, suyun inişi ve yönlendirilmesi zekâtın verme yönüyle, {ar:زَوْجٍ كَرِيمٍ, tr:zawjin karīmin, gloss:güzel veya soylu bir çift ya da tür} ise ikisinin karşılıklı tamamlayıcılığıyla buluşur. Bu dar bileşimin özgün katkısı iki uygulama arasındaki tamamlayıcılıktır; geniş yaratılış ekolojisi ve taşkın dolaşımı kendi ayrı katkılarıyla kalır. Zekâtın mali yükümlülük anlamı da yerinde durur; 31:10’daki bu özel görev eşleşmesi keşfedici bir bağdır ve bağımsız biçimbilimsel doğrulama taşımaz.


## Kamusal sorumluluk ve ahlaki yön

Dağ desteği ile kaynak akışı, namaz ve zekâtın toplumsal hayatta hangi ilişkilere değdiğini sormaya açılır. Tevbe 9:71’de kadın ve erkek müminler birbirlerinin velileri olarak sunulur; iyiliği emretmeleri ve kötülüğü engellemeleri karşılıklı gözetim ve sorumluluğu görünür kılar. Bu çerçeve, {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} fiilinin bağlı olduğu söz alanındaki işi ya da topluluğu yönetip koruma yönünü etkinleştirir. 9:71’de namazın bu ortak sorumlulukla yan yana gelişi, ayakta durma, eğilme, secde, dua ve yüceltmeyi taşıyan {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz}ı kamusal etik hayatın içine yerleştirir. Bu karşılıklı gözetim, Tevbe 9:103’te maldan alınan sadakanın alıcılara yönelmesiyle başka bir düzleme geçer: 31:4’teki {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} böylece bakımın hak sahibine ulaşan maddi yüzüyle ilişki kurar.

Tevbe 9:103’te verilen sadaka, {ar:تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا, tr:tuṭahhiruhum wa-tuzakkīhim bihā, gloss:onları bununla arındırır ve geliştirirsin} ifadesinde alıcıları arındırma ve geliştirme yönüyle anlatılır. Zekât adının büyüme, gelişme ve arınma söz alanı burada alıcıya bağlanır; böylece yoksulun hakkı olan zorunlu mal payı ahlaki gelişme boyutuyla birlikte görünür. Bu 9:103 bağlantısı, söz alanının alıcıda beliren yüzünü gösterir; arınmayı zekâtın bütün anlamı ya da her alıcı için değişmez bir sonuç saymaz. Aynı ayette {ar:وَصَلِّ عَلَيْهِمْ, tr:wa-ṣalli ʿalayhim, gloss:onlar için dua et} buyruğu ve duanın {ar:سَكَنٌ لَّهُمْ, tr:sakanun lahum, gloss:onlar için bir ferahlık} oluşu, maddi aktarımın yanına alıcıya yönelmiş manevi desteği koyar. 31:4’teki kurallı {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz}ın yanında, namaz sözcüğünün bağlı olduğu söz alanında başkası için iyilik ve esenlik dileme de duyulur. 9:103’teki sözlü iyilik dileğiyle arındırıcı sadaka, iki bakım biçimini ilişkilendirir; özel muhataba yönelen bu dua 9:103’e aittir, 31:4’teki namazı alıcıya dönük bir buyruk olarak tanımlamaz ve her namaza belirli bir muhatap atamaz.

Maddi aktarımın ve ritüelin bu bakım çevrimi, Nûr 24:37’de gündelik işlerin baskısı içinde görünür. 24:37’de {ar:رِجَالٌ لَّا تُلْهِيهِمْ تِجَٰرَةٌ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَاءِ ٱلزَّكَوٰةِ, tr:rijālun lā tulhīhim tijāratun wa-lā bayʿun ʿan dhikri llāhi wa-iqāmi ṣ-ṣalāti wa-ītāʾi z-zakāti, gloss:ticaretin onları Allah’ı anmaktan, namazdan ve zekâttan alıkoymadığı kimseler} diye nitelenen kişiler, {ar:يَخَافُونَ يَوْمًا, tr:yakhāfūna yawman, gloss:bir günden korkarlar}. Sonraki gün ufku ticaret ve satış sürerken bugünkü yönelişi biçimlendirir; 31:4’teki {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} iş baskısı altında doğrultuyu koruma, {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:ahiret} sonraki ufuk, {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar} ise yargıyı sabitleyen bilgi olarak okunabilir. Bu benzer portre, kesinliğin gündelik davranışta nasıl yaşanabileceğini gösterir; metinler arasında doğrudan bir neden-sonuç bağı ileri sürmez.

Bakara 2:177’deki {ar:الْبِرَّ, tr:al-birra, gloss:iyilik ve doğruluk} anlatısı ahiret inancını, mal vermeyi, namazı ve zekâtı; akraba, yetim ve yoksula bakımı; söze bağlılığı ve sabrı geniş bir iyilik çerçevesinde toplar. 2:177’de {ar:وَأَقَامَ ٱلصَّلَوٰةَ وَءَاتَى ٱلزَّكَوٰةَ, tr:wa-aqāma ṣ-ṣalāta wa-ātā z-zakāta, gloss:namazı ikame etti ve zekâtı verdi} bu pratikleri o çerçeveye yerleştirir. Bu bağlam 31:4’ün namaz, zekât ve ahiret kesinliği üçlüsünü daha geniş ahlaki hayatın kısa bir profili olarak duyurur; 2:177’nin tüm unsurları 31:4’ün her sözcüğüne dağıtılmaz. Zekâtın yoksulun hakkı olan mal payı oluşu, gönüllü yardımla zorunlu payı ayırırken iki metindeki ibadet ve ahiret ufkunu ortak pratik çevresinde buluşturur.

Bu pratik çevresinin davranışa uzanması Lokmân 31:17 ve 31:19 ile Ankebût 29:45’te daha belirginleşir. 31:17’de {ar:أَقِمِ ٱلصَّلَوٰةَ, tr:aqimi ṣ-ṣalāta, gloss:namazı ikame et} buyruğu, {ar:وَأْمُرْ بِٱلْمَعْرُوفِ وَٱنْهَ عَنِ ٱلْمُنكَرِ وَٱصْبِرْ عَلَىٰ مَآ أَصَابَكَ, tr:waʾmur bi-l-maʿrūfi wa-nha ʿani l-munkari waṣbir ʿalā mā aṣābaka, gloss:iyiliği emret kötülüğü engelle ve başına gelene sabret} ile yan yana gelir. 31:19’da {ar:وَٱقْصِدْ فِى مَشْيِكَ وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-qṣid fī mashyika wa-ghḍuḍ min ṣawtika, gloss:yürüyüşünde ölçülü ol ve sesini alçalt} yürüyüşte ölçü ve seste alçaklık ister. 31:4’teki {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler}in ayakta tutma ve doğrultuyu koruma yönü, ritüel tekrarını bedensel ve işitsel dengeyle ilişkilendirebilir; 31:17 ile 31:19’un tek bir öğüt dizisi olup olmadığı açık kalır. Ankebût 29:45’te {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inna ṣ-ṣalāta tanhā ʿani l-faḥshāʾi wa-l-munkar, gloss:namaz hayasızlık ve kötülükten alıkoyar} sözü namazın davranışla ilişkisini ayrıca belirtir. Bu katkı, ritüelin ahlaki etkisini görünür kılar; 29:45 her namaz edimi için otomatik sonuç garantisi vermez.


## Zamanın sınırı, kriz ve gizli karşılık

Lokmân 31:29’da gecenin gündüze, gündüzün geceye katılması ve güneşle ayın {ar:إِلَىٰٓ أَجَلٍ مُّسَمًّۭى, tr:ilā ajalin musamman, gloss:belirlenmiş bir süreye kadar} akması, tekrarlanan namazı hareketli fakat sınırları bulunan zaman içinde düşündürür. {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler}in sürekliliği gece-gündüz döngüsüne değince namaz tekrarları zamanın işaretlerinden biri gibi duyulur; {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:sonraki hayat ve ahiret} ise döngü içindeki henüz gelmemiş son ufku taşır. 31:30’da {ar:ٱللَّهَ هُوَ ٱلْحَقُّ, tr:Allāhu huwa l-ḥaqqu, gloss:Allah hakkın kendisidir} ve O’ndan başkasının {ar:ٱلْبَٰطِلُ, tr:al-bāṭilu, gloss:batıl ve geçersiz} oluşu devinim içinde değişmeyen yönelişi sunar; 31:4’teki {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar}la birlikte bakım, ahiret ve kesinlik zamana bağlı bir ilişki kurar. Bu ilişki 31:29 ve 31:30’un kozmik işaretler anlatımını koruyan bir zaman benzetmesidir; ayetler ayrıca güneş ve ayın hareketini ibadet takvimi olarak düzenlemez.

Lokmân 31:34, bu yönelişin geleceğe ait bütün ayrıntıları bilmek anlamına gelmediğini gösterir. Ayet saatin bilgisi, yağmurun inişi ve rahimlerde olanı Allah’a bağlar; {ar:وَمَا تَدْرِى نَفْسٌ مَّاذَا تَكْسِبُ غَدًا, tr:wa-mā tadrī nafsun mādhā taksibu ghadan, gloss:hiç kimse yarın ne kazanacağını bilmez} sözü yarının kazancını, {ar:وَمَا تَدْرِى نَفْسٌ بِأَىِّ أَرْضٍ تَمُوتُ, tr:wa-mā tadrī nafsun bi-ayyi arḍin tamūtu, gloss:hiç kimse hangi yerde öleceğini bilmez} ise ölüm yerini bilinmez bırakır. 31:4’teki {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:ahiret ve sonraki ufuk} ve {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kuşkudan arınmış kesin bilgiye sahip olurlar} geleceğin bütün verilerine değil, son ufka dönük sabit yönelişe işaret eder. 31:34’ün başlıca odağı ilahi bilginin sınırları olabilir; bu bağlamda 31:4’teki kesinlik yarının kazancını ya da ölüm yerini bilme iddiası değil, son ufka dönük güvendir.

Kesinlik çevresindeki daha uzak bir sözlük yankısı, görünür ile gizlinin yan yana gelişiyle açılır. {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar} olağan anlamıyla yerleşik bilgiyi taşırken, aynı söz alanındaki çok uzak bir kullanım gözlerden sakınıp korunan genç kadını anlatır. Lokmân 31:20’de nimetlerin {ar:ظَٰهِرَةً وَبَاطِنَةً, tr:ẓāhiratan wa-bāṭinatan, gloss:açık ve gizli} diye eşlenmesi, bu saklılık imgesi için tetikleyici olur; kesinlik dış koşullar içinde korunmuş bir iç alan gibi hayal edilebilir. Lokmân 31:32’de {ar:مَّوْجٌ كَٱلظُّلَلِ, tr:mawjun ka-ẓ-ẓulal, gloss:gölgelikler gibi örten dalgalar}ın üstte kurduğu örtü dışarıdan kuşatan basıncı ekler. Nimetlerin görünür-gizli oluşu ile dalganın örtücülüğü ayrı katkılardır; birlikte, koşullar kapandığında da korunan yöneliş imgesi kurarlar. Genç kadına ilişkin uzak kullanım burada kesinliğin sözlük anlamı değil, korunmuş iç alan benzetmesidir; 31:20 nimetleri, 31:32 ise tehlikeyi kendi düz anlamlarında anlatmayı sürdürür.

31:32’deki dalga örtüsüne bu kez gizli iç alan benzetmesinden ayrı bir zaman sahnesinde dönülür. Lokmân 31:31’de gemi Allah’ın nimetiyle denizde seyreder ve sabredenlerle şükredenler anılır; bu sakin yolculuk kriz öncesi akışı kurar. 31:32’de üst üste gelen, gölgelikler gibi örten dalgalar krizi belirginleştirir: insanlar dini yalnız Allah’a yönelterek O’na yalvarır, kurtarıldıklarında ise bazıları ölçülü kalır. Bu değişim, 31:4’teki namazı sürdürmeyi koşullar değişirken devam eden pratik gibi düşündürür; zekâtı verme ise olağan aktarımın deniz akışı ve yön değişimiyle kurulan malzeme benzetmesini ekler. Bu deniz bağlantısı fiilin sözlük anlamı değil, aktarımın hareketini görünür kılan bir imgedir. {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar}ın sabit yönelişi tehlike ve ferahlama karşısında düşünülebilir. Sakin seyirden dalga baskısına geçiş bağlılığın kriz içinde sınanmasını gösterir; kurtuluş sonrasında bazılarının ölçülü kalması, krizin herkeste aynı kalıcılığı üretmediğini de açık tutar. Bu nedenle sahne kriz anındaki bağlılığa yönelik bir uyarı olarak okunabilir.

Lokmân 31:21’deki {ar:عَذَابِ ٱلسَّعِيرِ, tr:ʿadhābi s-saʿīri, gloss:yakıcı alev azabı}, namaz ve doğrultu imgesine ateş çevresinde uzak bir yankı açar. 31:4’te {ar:ٱلصَّلَوٰةَ, tr:aṣ-ṣalāta, gloss:namaz} kurallı ibadeti, {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:namazı sürdürürler} ayakta tutma ve yönü korumayı taşır; namaz sözcüğünün bağlı olduğu söz alanında yakıcı ısıya maruz kalma kullanımı da bulunur. 31:21’deki alev bu ayrı kullanımı tetikler. Aynı alandaki, değneği ateş üzerinde döndürerek yumuşatıp düzeltme kullanımı da bu temasa biçim verme imgesi ekler; böylece tekrarın kişiyi biçimlendirdiği bir temperleme benzetmesi kurulur. Bu uzak yankı namazın ritüel anlamını korur; katkısı biçimlenme imgesidir, kelimeyi ateş diye çevirmek ya da belirli bir ceza öğretisi kurmak değildir.

Bakım imgesi Lokmân 31:14’te ebeveyn ile çocuk arasındaki zamana yayılmış emeğe taşınır. 31:14’ün {ar:حَمَلَتْهُ أُمُّهُۥ وَهْنًا عَلَىٰ وَهْنٍۢ وَفِصَالُهُۥ فِى عَامَيْنِ, tr:ḥamalathu ummuhu wahnan ʿalā wahnin wa-fiṣāluhu fī ʿāmayn, gloss:annesi onu güçlük üstüne güçlükle taşır ve sütten kesilmesi iki yıldadır} ifadesi görünmeyen taşıma yükünü, annenin güçlük üstüne güçlük içindeki emeğini ve iki yıl sonunda sütten kesilmeyle gelen ayrışmayı belirginleştirir. 31:4’teki verme, zekâtın büyüme yönü ve namazı sürdürmenin gözetme çağrışımı bir araya gelince destek, anlık eksiği gidermenin yanında zamanla gelişmeye ve ayrışmaya imkân veren bakım olarak duyulur. Bu bağlantının katkısı desteğin zaman boyutudur; 31:14’ün başlıca odağı ebeveyne minnettir, zekâtın sözlük tanımı ya da her alıcı için değişmez gelişme sonucu değildir.

Lokmân 31:33, aynı bakım ilişkisinin taşıyamayacağı sorumluluk sınırını belirtir: {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِۦ شَيْـًٔا, tr:lā yajzī wālidun ʿan waladihī wa-lā mawlūdun huwa jāzin ʿan wālidihī shayʾā, gloss:ne ebeveyn çocuk adına bir şey karşılayabilir ne çocuk ebeveyn adına} der. Zekâtın maddi desteği gerçek ve değerlidir; son sorumluluk ise bir yakınlık bağıyla başkasına devredilmez. 31:33’teki {ar:وَعْدَ ٱللَّهِ حَقٌّ, tr:waʿda llāhi ḥaqqun, gloss:Allah’ın vaadi gerçektir} ve {ar:فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا, tr:fa-lā taghurrannakumu l-ḥayātu d-dunyā, gloss:dünya hayatı sizi aldatmasın} sözü, yakınlığın son ufukta vekâleten kurtuluş sayılamayacağı sınırını kurar. Buraya eklenen hasat-zamanı yankısı her gelişmenin kendi olgunlaşma eşiğine erişmesini düşündürebilir; bu ek imge 31:33’ün açık tarımsal anlamı değildir. Ayetin temel katkısı, yakın bağlar sürerken bile herkesin kendi sorumluluğunu taşıdığını göstermesidir.

Verme ile son ufuk arasındaki görünmeyen ilişki Lokmân 31:16 ve Müzzemmil 73:20’de iki ayrı fiil biçiminin temasıyla açılır. 31:4’teki {ar:يُؤْتُونَ, tr:yuʾtūna, gloss:verirler} alıcıya doğru aktarımı anlatır; 31:16’daki {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā llāhu, gloss:Allah onu getirir} başka bir biçim ve başka bir özneyle Allah’ın saklı şeyi ortaya çıkarmasını söyler. Biçim ve özne farkı, bağın sınırını da belirler: 31:4’teki fiilin anlamı “vermek”tir, 31:16’daki farklı çekim ise görünmeyenin erişilebilir hâle gelişine kök düzeyinde yankı verir. Müzzemmil 73:20’de {ar:وَمَا تُقَدِّمُوا لِأَنفُسِكُم مِّنْ خَيْرٍ تَجِدُوهُ عِندَ ٱللَّهِ, tr:wa-mā tuqaddimū li-anfusikum min khayrin tajidūhu ʿinda llāh, gloss:kendiniz için önden gönderdiğiniz iyiliği Allah katında bulursunuz} denmesi, önceden gönderilen iyiliğin sonradan bulunabileceği ufku ekler.

Lokmân 31:16’da {ar:مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ, tr:mithqāla ḥabbatin min khardalin, gloss:hardal tanesi ağırlığınca} küçüklüğündeki şey kaya, gökler ya da yer içinde saklı olabilir; {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā llāhu, gloss:Allah onu getirir} ifadesi bu ölçüde küçüğü de erişilebilir kılar. Ayetin sonundaki {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīr, gloss:ince lütuf sahibi ve haberdar} nitelemesi en ince ve gizli olanın gözden kaçmadığını tamamlar. 31:4’te zekâtın büyüme yönü bu küçücük ölçüyle, {ar:يُوقِنُونَ, tr:yūqinūna, gloss:kesin olarak inanırlar} ise gizli kalanın da hesaba katılacağına güvenle buluşabilir. Müzzemmil 73:20’de Allah katında bulunan önden gönderilmiş iyilik bu bağ için somut bir karşılık ufku sağlar; 31:16’nın başlıca odağı yine ilahi bilgidir ve 73:20 belirli bir dünya karşılığını garanti etmez. Bu okumanın katkısı verilenin görünen ölçeği ile sonradan ortaya çıkışı arasındaki aralığı düşündürmektir; aralık belirli ya da ölçülebilir bir dünya geri dönüşü vaat etmez.


</source_prose>
