# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:33**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.middle.claims.json`

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
- Refer to source paragraphs as `31:33 ¶N`.

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

`(31:33 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:33",
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
        "citation": "(31:33 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_33/31_33.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_33/31_33.middle.claims.json \
  --ayah-ref 31:33
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_33/31_33.prose.editorial.tr.md`

<source_prose>
Bu ayet bütün insanlara Rablerine karşı kendilerini korumalarını ve babanın çocuğu adına, çocuğun da babası adına hiçbir şeyi karşılayamayacağı bir günden sakınmalarını buyurur. Allah’ın vaadi gerçektir; yakın dünya hayatı ya da Allah hakkında veya Allah’ın adı kullanılarak kurulan aldatıcı güvence bu çağrıyı boşa çıkarmasın.

## Herkese seslenen buyruk

{ar:يَا, tr:yā, gloss:ey} kısa bir seslenme durağı açar; {ar:أَيُّهَا, tr:ayyuhā, gloss:ey hitabı}, belirli insan topluluğunu bildiren {ar:النَّاسُ, tr:al-nāsu, gloss:insanlar} sözüne bağlanan dilbilgisel köprüdür. Bu tanınan hitap kalıbı, önceki anlatıdan doğrudan buyruklara geçirir. Çağrı bir alt gruba değil bütün insanlara yönelir. Bu sözcük ailesinin yabancılığı ve ürkekliği gidererek yakınlık, rahatlık ya da sevinç doğuran ayrı kullanımı da vardır. Evrensel sesleniş, birazdan anılacak {ar:وَالِدٌ, tr:wālidun, gloss:baba}, {ar:وَلَدِهِۦ, tr:waladihi, gloss:onun çocuğu}, {ar:مَوْلُودٌ, tr:mawlūdun, gloss:doğmuş kişi} ve {ar:وَالِدِهِۦ, tr:wālidihi, gloss:babası} bağlarıyla, ayrıca {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} ile {ar:جَازٍ, tr:jāzin, gloss:karşılık veren} biçimlerinin bir başkasının yerini tutma kullanımıyla temas edince, yalnız kalabalığa değil ilişki arayan insana da seslenir. Bu yakınlık yankısı ayrı bir sözlük kullanımından gelir; toplumsal bağı, hesabı başkasına devretmekle bir tutmaz.

İlk emir çoğul hâliyle herkese yönelir: {ar:ٱتَّقُوا۟, tr:ittaqū, gloss:kendinizi koruyun}. Sözcüğün olağan koruyucu gücü, korkulan zararla insan arasına önlem koyan etkin bir tutum çağırır; ayetin sonundaki aldanmama yasakları bu önlemin hangi baskılara karşı gerektiğini gösterir. Emir, {ar:رَبَّكُمْ, tr:rabbakum, gloss:Rabbiniz} diyerek korunmayı bir ilişki içine yerleştirir: muhataplar kendi Rablerine karşı sorumludur. Ardından gelen {ar:وَ, tr:wa, gloss:ve}, ikinci buyruğu ilkine eşit bir yükümlülük olarak ekler. {ar:ٱخْشَوْا۟, tr:ikhshawū, gloss:haşyet edin} emrinin nesnesi Rab değil, belirsiz ve mansup gelen {ar:يَوْمًا, tr:yawman, gloss:bir gün}dır. Bu “gün” hem haşyetin nesnesi olur hem de ardından onu tanımlayan olumsuz cümleye kapı açar; sıradan bir gündüz çevriminden çok kritik hesap vaktini duyurur. Böylece ilk emir kişinin tutumunu, ikincisi bu tutumun karşısındaki vakti belirler; bilgili bir ürperti gelişigüzel paniğe indirgenmez.

31:22’de Allah’a yüzünü yöneltme, sağlam kulpa sımsıkı tutunma ve işlerin sonunun Allah’a varması bir arada anılır. Bu sıra, {ar:ٱتَّقُوا۟, tr:ittaqū, gloss:kendinizi koruyun} buyruğunu zarardan korunmanın yanına, sonuç gelene dek güvenilir desteğe bağlı kalma imgesini ekleyerek genişletebilir. Bu, önceki ayetteki tutuşun odaktaki buyrukla özel bağ kurmayan genel bir iman imgesi olarak da okunabildiği temkinli bir yankıdır; sakınmanın olağan koruyucu anlamını yerinden etmez (31:22).

## Akrabalığın sınırı

Haşyet edilen vakit önce bir imkânsızlıkla tanımlanır: standart okuyuşta {ar:لَا يَجْزِى, tr:lā yajzī, gloss:karşılık veremez} ile başlayan cümle, hiçbir {ar:وَالِدٌ, tr:wālidun, gloss:babanın} kendi {ar:وَلَدِهِۦ, tr:waladihi, gloss:çocuğu} adına karşılık veremeyeceğini söyler. Olumsuzluk tek bir başarısız olayı değil kategorik bir sınırı kurar. {ar:يَجْزِى, tr:yajzī, gloss:karşılığını verir} karşılık ödeme ve yeterli olma anlamlarını taşırken, yanındaki {ar:عَنْ, tr:ʿan, gloss:adına} edatı çocuğu baba tarafından yerine geçilmesi düşünülen taraf yapar. Sözcüklerin yerel sırası önce fiili, sonra babayı, ardından “adına” ilişkisini ve onun kendi çocuğunu gösterir. Belirsiz {ar:وَالِدٌ, tr:wālidun, gloss:baba} tek bir kişiyi değil her babayı kapsar; erkek ebeveyni adlandırır, buna karşılık iyelikli {ar:وَلَدِهِۦ, tr:waladihi, gloss:onun çocuğu} cinsiyet belirtmeyen evlat anlamını korur. Aynı doğum ailesinden gelen bu adlar akrabalığı dilde birbirine bağlar, fakat karşılık aktarma imkânı vermez. Bir kıraat varyantı karşı taraf adına yerine geçememeyi de teyit eder; bu, alıcı yönündeki sınırı görünür kılar ama standart okuyuşun yerel kuruluşunu değiştirmez. “Adına” işlevindeki {ar:عَنْ, tr:ʿan, gloss:adına} edatının ayrılma ve uzaklık bildiren ayrı kullanımı da yakın bağın içinde temsil etme isteğiyle mesafe yankısını birlikte duyurur; ilk edat, birazdan ters yönde yinelenecek yapıyı hazırlar, gerçek bir vekâlet kurmaz.

Bağlaçla yön tersine döner: {ar:وَ, tr:wa, gloss:ve} ikinci olumsuz kolu aynı hükme bağlar, fakat ilişki eksenini ebeveynden çocuğa değil çocuktan ebeveyne çevirir. İkinci {ar:لَا, tr:lā, gloss:olmaz}, ilk bölümdeki eylem yasağından farklı olarak bir durum bildiren nominal yüklemi reddeder. Edilgen ortaç {ar:مَوْلُودٌ, tr:mawlūdun, gloss:doğmuş kişi} doğurulmuş, dünyaya getirilmiş kişiyi özne yapar; böylece insanın başlangıcına bağımlılığı, kökenine geri yardım edememesiyle yan yana gelir. Etken {ar:وَالِدٌ, tr:wālidun, gloss:baba} ile edilgen {ar:مَوْلُودٌ, tr:mawlūdun, gloss:doğmuş kişi} ayetin akrabalık merkezini ayna düzeninde kurar. Ayırıcı {ar:هُوَ, tr:huwa, gloss:bizzat o} zamiri özneyle yüklemi belirginleştirir ve karşılık verme sınavının öznesi olarak doğmuş kişinin kendisini öne çıkarır. {ar:جَازٍ, tr:jāzin, gloss:karşılık veren} de önceki {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} fiilinin eyleminden bir yeterlik ya da durum bildirimine geçer: söylenen, geçici bir başarısızlıktan çok babası adına yetme gücünün bulunmadığıdır. Bu, ayet içindeki fiil-ortaç karşıtlığıdır; daha özel bir fiil kalıbı varsaymayı gerektirmez.

İkinci {ar:عَنْ, tr:ʿan, gloss:adına} aynı eşleşme yerinde yinelenir ama bu kez amaçlanan taraf babadır. {ar:وَالِدِهِۦ, tr:wālidihi, gloss:babasının} sözü babayı yükümlü özneden yardımın yöneldiği kişiye çevirir; aile bağı kalırken onun vekâlet gücü sınırlanır. İki “adına” öbeğinin benzerliği temsil etme isteğiyle ayrılığı birlikte duyurur; bu çift yankı iki aile ilişkisiyle sınırlı kalır. Son sözcük {ar:شَيْـًٔا, tr:shayʾan, gloss:herhangi bir şey}, belirsiz ve mansup biçimiyle olumsuzluğun kapsamını mümkün olan her nesneye, en küçüğüne kadar genişletir. İki yönde tasarlanan karşılıklar önce kapanır, sonra “herhangi bir şey” bütün telafi alanını mühürler: akrabalık sürer, fakat hesap devredilemez.

31:14–15 aile içindeki bakım ve iyilik yükümlülüğünü sürdürür: annenin çocuğu taşıması ve “güçlük üstüne güçlük” çekmesi bedensel emeği görünür kılar; bu anlatının ardından gelen şükür çağrısı bakımı sürdürür (31:14). Yanlış bir isteğe itaat reddedilebilirken anne babaya dünyada iyilikle eşlik etme buyruğu da devam eder (31:15). Odaktaki {ar:رَبَّكُمْ, tr:rabbakum, gloss:Rabbiniz} adı gözetme ve besleme yönünü hatırlatır; Rab sözcüğünün ayrı kullanımlarıysa eksikten tamamlanmaya, büyüyenin beslenip geliştirilmesine açılır. Bu bakım alanı biyolojik ebeveyn ve doğmuş çocuk adlarıyla buluşunca, alınan özen kişinin kendini koruma ve cevap verme yetisini besleyebilir. Yakınlık yabancılaşma buyurmaz, bakım da vekâlet sağlamaz. 31:14–15'in bakım etiğiyle 31:33'teki kişisel sorumluluk arasında kurulan bağ bir çıkarımdır; 31:33 önceki aile etiğini yeniden yorumlamadan yalnızca son hesabın devredilemeyeceğini de söylüyor olabilir (31:14, 31:15).

31:23'te kişisel dönüş ve yapılanların bildirilmesi aile sınırını bireysel hesap ufkuna taşır. {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} ile {ar:جَازٍ, tr:jāzin, gloss:karşılık veren} için eyleme uygun iyilik ya da kötülükle karşılık verme kullanımı burada öne çıkar: kişi kendi davranışının karşılığıyla yüzleşir. Bu kullanım ebeveynin ya da çocuğun diğeri adına iş görme anlamıyla birlikte okunabilir; her amelin sonucunu tek tek belirlemez. Aynı biçimlere bağlanan alacak talebi, alacaklının borçludan borcunu istemesini anlatır; olumsuzluk altındaki {ar:شَيْـًٔا, tr:shayʾan, gloss:herhangi bir şey} bütün olası nesneleri kapsayınca, başka birinin borcunu hiçbir şeyin kapatamayacağı sınırlı bir hesap benzetmesi doğar. Açılıştaki {ar:ٱتَّقُوا۟, tr:ittaqū, gloss:kendinizi koruyun} buyruğu bu ufukta hazırlığı her muhatabın kendisine döndürür. Bu benzetme 31:23'teki kişisel dönüş ve amellerin bildirilmesiyle sınırlıdır; ayet gerçek bir alacaklıyı, parayı ya da hukukî işlemi anlatmaz (31:23).

31:16'daki hardal tanesi ağırlığındaki nesne sahnesi, küçüklük ve gizlilik bakımından “herhangi bir şey” sözüyle yankılanır: nesne kaya içinde, göklerde ya da yerde bulunsa da ortaya çıkarılır; {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīrun, gloss:en inceyi bilen ve iç yüzünden haberdar olan} oluşu gizli ve küçüğü kapsayan bilgiyi öne çıkarır (31:16). Odaktaki {ar:مَوْلُودٌ, tr:mawlūdun, gloss:doğmuş kişi} başka birinden doğmuş olma bağını, {ar:شَيْـًٔا, tr:shayʾan, gloss:herhangi bir şey} ise karşılık verilemeyen nesneyi taşır; bu temas, ne soy bağının ne de en küçük, saklı nesnenin bilgi ve karşılık alanının dışında kalmayacağı ihtimalini açar. “Bilinebilir ya da bildirilebilir şey” burada {ar:شَيْـًٔا, tr:shayʾan, gloss:bir şeyi} için doğrulanmış yeni bir sözlük karşılığı değil, bağlamsal bir okumadır; isteme ya da irade anlamındaki ayrı biçimi nesne sözüne taşımaz. 31:16 Allah’ın bilgisi ve gücünü gösteriyor, nihai hesabı doğrudan anlatmıyor da olabilir (31:16).

Karşılık ve hesap anlamındaki {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} ile {ar:جَازٍ, tr:jāzin, gloss:karşılık veren} biçimlerine yakın sesli, fakat ayrı bir biçim olan {ar:جَزَّ, tr:jazza, gloss:kırkmak ya da biçmek} yün gibi lifleri kesmeyi, ekin ya da ağaç ürününü toplamayı ve hasat vaktini anlatır. Aile büyümesini adlandıran doğum sözcükleriyle kritik {ar:يَوْمًا, tr:yawman, gloss:gün} yan yana geldiğinde, kesim ve hasat imgesi ayrı ayrı toplanan hesapların bir hasat vaktinde buluşmasını düşündürür. Bu, yakın sesli ama ayrı biçimlerin açtığı keşifsel bir benzetmedir; ayetin çevirisi ya da tercih edilen biçim değildir.

## Vaat ve vade

Akrabalıkla karşılık verememe cümlesinden sonra {ar:إِنَّ, tr:inna, gloss:şüphesiz} vurgulu bir geçiş açar. Mastar olan {ar:وَعْدَ ٱللَّهِ, tr:waʿda Allāhi, gloss:Allah’ın vaadi}, gelecekte iyi ya da kötü bir şeyin sözle bildirilip gerçekleşme beklentisi doğurmasını taşır ve gelecek taahhüdünü ilahî kaynağına bağlayan tek bir izafet öbeği kurar; {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah’ın} tamlayan, {ar:حَقٌّ, tr:ḥaqqun, gloss:gerçek} ise belirsiz isim yüklemidir ve vaadi doğru, gerçek olanla özdeşleştirir. İlahi kaynak vaadin kesinliğini temellendirir; bu kesinlik insanın vaadin bütün ufkunu kuşattığı anlamına gelmez. Vaadin olağan güvence anlamı, korkulan {ar:يَوْمًا, tr:yawman, gloss:gün}, haşyet buyruğu ve vekâletsizlik sahnesiyle yan yana gelince, gelecekte zarar verileceğini bildirip muhatabı uyaran ayrı kullanımı da etkinleşir. Böylece vaat güvence verirken uyarı tonu da taşır; bu uyarı kolu her vaadi tehdit anlamına getirmez.

{ar:حَقٌّ, tr:ḥaqqun, gloss:gerçek} vaadin gerçeğe uygunluğunu bildirir; korkulan gün ve karşılık verememe bağlamı, sözcüğün ayrı “gerekli, artık kaçınılamaz” kullanımını da yankılayabilir. Aynı kökün {ar:الْحَاقَّةُ, tr:al-ḥāqqah, gloss:Son Gün adı} biçimi insanların yaptıklarıyla yüzleştiği günü adlandırır; önceki {ar:يَوْمًا, tr:yawman, gloss:gün} ve vekâletsiz hesap bu özel adı odak ayette geçirmeden yalnızca temkinli bir yankı olarak çağırır. Sıkı dokunmuş kumaş ya da sağlam kurulmuş söz çağrışımını etkinleştirecek bir taşıyıcı burada bulunmadığından, {ar:حَقٌّ, tr:ḥaqqun, gloss:gerçek} yüklemi dokuma anlamı almaz. Belirli bir gün, gerçek bir vaat ve kesinlik bildiren yüklem yan yana geldiğinde {ar:ٱخْشَوْا۟, tr:ikhshawū, gloss:haşyet edin} için beklenen sonucu gerçekleşmeden sabit gerçek olarak tanıma yönü de açılabilir; bu, olağan haşyet anlamının yerine geçmeyen temkinli bir genişlemedir.

Sonuç bildiren {ar:فَ, tr:fa, gloss:öyleyse} vaadin doğruluğunu hemen eyleme bağlar: sakınma ve aldanmama şimdi gereklidir. Açılıştaki iki emir, son bölümde dünya hayatı ve aldatıcı için gelen iki yasakla çerçevelenir. Bu nedenle vaadin söz konusu oluşu yalnız gelecek hakkında haber vermekle kalmaz; bugünkü tutumu da düzenler.

31:9'da vaat ve doğruluk sözlerinin kalıcı bahçelerle birlikte yer alması ödül umudunu açar; oradaki {ar:خَالِدِينَ فِيهَا وَعْدَ ٱللَّهِ حَقًّا, tr:khālidīna fīhā waʿda Allāhi ḥaqqan, gloss:orada kalıcı olarak; Allah’ın vaadi gerçektir} formülü bu ufku somutlaştırır. Aynı vaat-doğruluk formülü dünya hayatı ve Allah hakkında aldanma uyarılarında da görünür (35:5). Ayrım gününün hepsi için belirlenmiş vaktinden söz edilmesi, odaktaki {ar:يَوْمًا, tr:yawman, gloss:gün}ı takvim gününden çok hükmün toplandığı belirleyici olay olarak duyurur (44:40). Bu temaslar güvenilir ve zamanlı bir geleceği bugünkü davranışa bağlar; belirli bir takvim günü vermez. Tekrarların bilinçli alıntı olması gerekmez: her ayet kendi bağlamındaki önermeyi ayrıca doğrulayabilir. Umutla hesap aynı gelecek ufkunda buluşurken, bu ayetlerdeki {ar:حَقٌّ, tr:ḥaqqun, gloss:gerçek} sözüne kumaş ya da sağlam kurulmuş söz için gereken taşıyıcı bulunmadığından dokuma anlamı eklenmez (31:9, 35:5, 44:40).

31:29 geceyi gündüze, gündüzü geceye sokan devir ve her şeyin belirlenmiş vadeye akışıyla hareket eden zaman imgesi sunar. Bu akış, {ar:يَوْمًا, tr:yawman, gloss:gün}ı saatlerle sınırlı gündüzden daha geniş süreye, {ar:وَعْدَ, tr:waʿda, gloss:vaat}ı ise gelecek sözünün yanı sıra gerçekleşme vaktine doğru açar. Devir, devam eden akış ve sabit vade korkulan günü zamanın içindeki bir sınıra dönüştürür. Bu kişisel bir mesafe hissi değil, evrensel düzenin sağladığı temkinli bir genişlemedir (31:29).

Vaat sözüyle ilişkilendirilen başka bir kullanım, insanın ya da canlının suda ilerlemesi, yüzmeye benzer akış anlamı taşır; gemi, deve ve yıldızların akıcı hareketini anlatan bu kullanım denizde yol alan gemiyle bağımsız bir temas bulur (31:31). Deniz, geminin içinden geçtiği geniş ve belirsiz ortamdır; bu hareket vaat sözünü bilinmeyen şimdiden görünmeyen sınıra taşıyan bir geçiş gibi tasarlamaya imkân verir. Aynı söz alanındaki kışı ve yazı kapsayan “yıl” kullanımı geminin denizde ilerleyişiyle kurulan akışı bir zaman aralığı boyunca uzatır; gece-gündüz devri ve belirli vade de bu süreye sınır verir (31:29). Yüzme ve yıl karşılıkları etimoloji iddiası değildir: ayet Allah’ın vaadinin doğru olduğunu söyler, gerçek bir yüzme ya da yıllık yolculuk bildirmez (31:29, 31:31).

46:17 aile yakınlığının uyarıyı taşıdığını, inanç ve cevabınsa kişiye ait kaldığını gösteren bir sahne sunar. Çocuk, ana babasının diriliş uyarısına {ar:أَتَعِدَانِنِي أَنْ أُخْرَجَ, tr:a-taʿidāninī an ukhraja, gloss:bana yeniden çıkarılacağımı mı vaat ediyorsunuz} diyerek karşı çıkar; aynı sahnede {ar:إِنَّ وَعْدَ ٱللَّهِ حَقٌّ, tr:inna waʿda Allāhi ḥaqqun, gloss:Allah’ın vaadi gerçektir} sözü de yer alır (46:17). Bu yankı aileyle vaat-doğruluk çiftini yan yana getirir: ebeveyn uyarıyı iletebilir, çocuğun inancını ya da cevabını onun yerine üstlenemez. İki ayetin bilinçli alıntı ilişkisi ya da her aile anlaşmazlığının aynı sonuca varacağı ileri sürülmez; ebeveyn uyarıyı taşır, çocuğun cevabı kendisine aittir (46:17).

## Yakın hayat ve aldanma

İlk yasak, gerçek hayatı aldatabilen bir fail olarak öne çıkar: {ar:فَلَا تَغُرَّنَّكُمُ ٱلْحَيَوٰةُ ٱلدُّنْيَا, tr:fa-lā taghurrannakumu al-ḥayātu al-dunyā, gloss:yakın dünya hayatı sizi aldatmasın}. Sonuç bildiren {ar:فَ, tr:fa, gloss:öyleyse} vaatten davranışa geçirir; {ar:لَا, tr:lā, gloss:sakın} güçlü bir engel koyar, pekiştirmeli {ar:تَغُرَّنَّكُمُ, tr:taghurrannakumu, gloss:sizi aldatmasın} biçimi ise muhatapları doğrudan alıcı yapar. Standart okuyuşta dişil tekil özne olan belirli {ar:ٱلْحَيَوٰةُ, tr:al-ḥayātu, gloss:yaşam} ilk uyarının failidir; yaşam edilgen bir fon değil, çekici görünüşüyle yanıltabilen etkendir. Kıraat varyantları fail ve pekiştirme üzerinde başka bir baskı kurabilse de standart okuyuşun bu vurgusunu ortadan kaldırmaz. Aldatma kökünün yalan haber ya da gerçeğe uymayan görünüşle bilerek yanıltma kullanımı da bu hayat ve yakın dünya tamlamasıyla buluşur; tehlike yalnız yanlış söz değil, çekici hayatın ayartmasıdır.

Buradaki {ar:ٱلْحَيَوٰةُ, tr:al-ḥayātu, gloss:yaşam} olağan anlamıyla gerçek hayattır; kökün yarar, iyilik ve yok oluştan korunma yönünü anlatan ayrı kullanımları bu hayatın gerçek çekimini duyurur. Kökün canlı varlığı adlandıran isim anlamından ayrı olan bitmeyen gerçek hayat kullanımı da hesap ve vaat ufkunda daha uzun bir gelecek yankısı açar; odaktaki tamlama ise yakın dünyanın hayatıdır. {ar:ٱلدُّنْيَا, tr:al-dunyā, gloss:yakın dünya} sıfatı bu hayatı belirli bir ufka daraltır; karşılaştırmadaki “daha yakın” ya da “ilk” kutbu vaat edilen güne karşı zamansal yakınlığı hissettirir. “Daha küçük, aşağı, güçsüz ya da eksik” olma kullanımları bu karşıtlıkta temkinli bir yankı olarak kalır, doğrudan çeviriye dönüşmez. Uyarının odağı hayatın kendisi ya da sağladığı yarar değil, yakın ufkun bütün gelecek sanılmasıdır: bugünün gerçek kazancı sonucun tamamını ölçen değere dönüşebilir.

31:24'te az süreli yararlanmanın ardından daha ağır bir sona zorlanma gelir. Yararlanma gerçektir, fakat “az” diye sınırlandırılır; zorunlu geçiş, bugünkü çekimin tüm dizinin yerini tutamayacağını gösterir ve yakın hayatın aldatma uyarısını zaman ufkuna taşır: şimdiki yararı kabul ederken onu sonucun güvencesi sayma riski belirir. Zorunlu ağır son, vaadin gelecekte zarar bildiren ayrı kullanımına da bir uyarı kenarı verir; bu bağlantı her vaadi tehdit anlamına getirmez (31:24). Ayet kısa yararı ve cezayı art arda koyuyor da olabilir; bu sıra her insanda aynı psikolojik döngüyü kanıtlamaz, dünya hayatını özünde kötü ya da hazzı sahte ilan etmez. Böylece kısa yarar gerçek kalırken onu daha uzun sonucun yerine koymama uyarısı belirir (31:24).

31:20'de açık ve gizli nimetlerin birlikte anılması görünür yararın yanına göz önünde olmayan nimetleri de koyar; bir nimetin görünmemesi onun yok olduğu anlamına gelmez. {ar:ظَاهِرَةً وَبَاطِنَةً, tr:ẓāhiratan wa-bāṭinatan, gloss:açık ve gizli} nimetlerle {ar:كِتَابٍ مُنِيرٍ, tr:kitābin munīrin, gloss:aydınlatan kitap} yan yana geldiğinde daha geniş görme imkânı belirir. Tartışanın bilgi, hidayet ve aydınlatıcı kitaptan yoksun gösterilmesi de görünür katmanın ötesine bakma gereğini belirginleştirir: {ar:بِغَيْرِ عِلْمٍ وَلَا هُدًى وَلَا كِتَابٍ مُنِيرٍ, tr:bi-ghayri ʿilmin wa-lā hudan wa-lā kitābin munīrin, gloss:bilgi, hidayet ve aydınlatıcı kitaptan yoksun} (31:20). Böylece görünür yarar gerçek kalırken onu bütün saymanın yanıltıcı bir yüzey seçimi olabileceği görülür. Bu bağlantı temkinli kalır: ayetin eleştirisi öncelikle temelsiz tartışmaya yöneliyor olabilir, dolayısıyla yüzey okuması tek açıklama değildir (31:20).

87:16–17'de dünya hayatının yeğlenmesi ile sonraki hayatın daha hayırlı ve kalıcı sayılması, yakın ya da ilk kutbu zamansal olarak belirginleştirir. 57:20'deki yağmur bitkisi önce hayranlık uyandırır, sonra solar, sararır ve kırıntıya döner. Bu maddi dönüşüm, aynı kök ailesindeki “başlangıç” ve “eksik kalma” kullanımlarını ayrı çağrışımlar olarak harekete geçirir: ilk çekim sonucun güvencesi değildir, görünen evre bütün hikâye sayılmaz. Bu çağrışımlar odaktaki aldatma fiili ya da fail adının doğrudan sözlük karşılığı değil, yağmurun dönüşümü ve daha kalıcı gelecek ufkuyla kurulan bağlantılardır (57:20, 87:17).

Sonucu belirsiz tehlike bildiren aldatma ailesi {ar:غَرَر, tr:gharar, gloss:sonucu belirsiz tehlike}, özellikle konusu ya da sonucu bilinmeyen bir satışı anlatır. Bu kullanım, yakın hayatın gerçek yararı ile vaat edilen gelecek arasındaki farkı görünür kılar: dünya hayatı gizli şartları olan, sonucu yüzeyinden okunamayan bir teklif gibi duyulabilir; bugünkü rahatlık bilinmeyen sonu örtebilir. Benzetme bu bağlantıyla sınırlıdır; ayet bir satıcıyı, sözleşmeyi ya da sahte vaadi anlatmaz. Allah’ın vaadi ise gerçekliği bildirilen, güvenilir gelecek sözüdür; kalıcı bahçeler ve aynı vaat-doğruluk formülünün uyarı bağlamında görünmesi, gerçek dünya yararını silmeden son güvenceyi daha uzun ufka taşır (31:9, 35:5). Yakınlığın değer hesabını şaşırtabilmesi, görünür yararı reddetmeden ona son güvence yüklememe çağrısını açıklar.

İkinci yasak ilkinden ayrı bir aldatma yolunu engeller: {ar:وَلَا يَغُرَّنَّكُم بِٱللَّهِ ٱلْغَرُورُ, tr:wa-lā yaghurrannakum bi-Allāhi al-gharūru, gloss:aldatıcı sizi Allah hakkında ya da Allah’ın adıyla aldatmasın}. {ar:وَ, tr:wa, gloss:ve} iki yasağı eşgüdümler; dünya hayatı ve son fail olan aldatıcı ayrı tehlikeler olarak kalır. {ar:بِ, tr:bi, gloss:ile ya da hakkında} edatı {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} adını aldatma yapısına bağlayıp onu fail {ar:ٱلْغَرُورُ, tr:al-gharūru, gloss:aldatıcı} adlandırılmadan önce getirir; böylece aldatmanın neye değdiği failden önce duyulur. İlk kullanımda Allah adı vaadin kaynağıdır; buradaki söz dizimi ise Allah hakkında aldatma ile adının araç edilmesi olasılıkları arasında seçim yapmaz. İnsanların Allah’a yönelen bağlılığı gerçek kalır, Allah’a dayandırılan bir iddia da bu güveni kullanabilir. İkinci olumsuzluk ayrı ve güçlü bir engel kurar; yinelenen aldatma fiili önceki dişil yaşam failinden erkek biçimli yoğun aldatıcıya geçer, cümlenin sonundaki kesin tanımlı fail adı da süreci kişileştirir. Standart okuyuş bu kişileşmiş aldatıcıyı öne çıkarırken kıraat farklılığı aldatma sürecinin gölgesini de korur; ilk yasağın faili olan yaşamla bu son fail aynı tehlike değildir. İki fiilin olağan anlamı, yalan haber ya da gerçeğe uymayan görünüşle bilerek yanıltmayı korur.

Bu iki yol arasındaki ayrımı iki örnek somutlaştırır. Birinde “ateş bize sayılı günlerden başka dokunmayacak” güvencesinden sonra, uydurdukları şeylerin insanları dinleri hakkında aldattığı söylenir (3:24). Diğerinde aldatıcının Allah hakkında aldatması açıkça anılır (57:14). Böylece gündelik dünyanın güvenli görünen çekimiyle Allah adına ya da Allah hakkında kurulan yanlış güvence yakın, ama ayrı tehlikeler olarak kalır. Fiillerdeki “sizi” eki aldatmanın bir alıcıya yöneldiğini gösterir; deneyimsizlik ya da kötülüğü sezememe, örneklerin açtığı kırılganlık olasılığıdır, aldatıcının sözlük anlamı değil. Bu okuma herkesi saf saymaz ve dinî güvenin tümünü aldatıcı ilan etmez (3:24, 57:14).

31:6–7'deki işitme dizisi, yanıltıcı görünüşün nasıl sınanmadan kalabileceğine dair bir dikkat imgesi sunar. {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahw al-ḥadīth, gloss:oyalayıcı meşguliyet ve söz} ifadesindeki oyalayıcı uğraş insanı başka şeyden alıkoyar, yenilenen söz ise her seferinde yeni bir haber taşır; böylece dikkat başka yöne çekilebilir (31:6). Ardından {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onu işitmemiş gibi} yüz çevirme ve {ar:وَقْرًا فِيٓ أُذُنَيْهِ, tr:waqran fī udhunayhi, gloss:kulaklarında ağırlık} sesle anlama arasındaki eşiği kapatır (31:7). Bu sırayı odaktaki {ar:تَغُرَّنَّكُمُ, tr:taghurrannakumu, gloss:sizi aldatmasın} ve {ar:ٱلْغَرُورُ, tr:al-gharūru, gloss:aldatıcı} uyarılarıyla ilişkilendirmek, dikkatin inanıştan önce yönetilmesi ve aldatıcı görünüşün sınanmadan kalması ihtimalini açar. Bu bağlantı ihtimal düzeyindedir: sıralanış tek başına neden-sonuç kanıtı değildir, sahne inatçı bir reddi de anlatıyor olabilir (31:6, 31:7).

31:32'de dalga, örtülme, sarsıntı ve kurtuluştan sonraki nankörlük sırası, aldanmama uyarısının kriz sonrasına da uzanabileceği bir imge kurar. {ar:غَشِيَهُم مَّوْجٌ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-ẓ-ẓulal, gloss:gölgelikler gibi dalgalar onları bürüyünce} ifadesinde dalga insanları örter ve sarsar; ardından {ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā al-barr, gloss:onları kurtarıp karaya çıkardığında} tehlikeden ayrılışı bildirir (31:32). Kurtuluşun ardından {ar:خَتَّارٍ كَفُورٍ, tr:khattārin kafūrin, gloss:vefasız ve nankör} nitelemesi belirir; nimetin üzerini örtme yankısı, rahatlığın kurtuluş kaynağını görünmez kılıp yakın güveni geri getirebileceğini düşündürür. Bu bağlantı ihtimal düzeyinde kalır: her kurtulan aynı ruhsal döngüyü yaşamaz, ayet kurtuluş sonrasındaki farklı tepkileri sıralıyor olabilir ve dalga, örtülme, sarsıntı ile nankörlük arasındaki bağlam ilişkisi kesin değildir. Bu sıra, bu yüzden, aldanmama uyarısının yalnız kriz anına değil, tehlike geçince geri dönebilen çekime de uygulanabileceğini gösterir (31:32).

10:23'te kurtuluşun ardından insanların yeryüzünde haksızlık etmesi, dünya hayatının geçici yararı, dönüş ve yapılanların bildirilmesi art arda gelir. Odaktaki {ar:ٱلدُّنْيَا, tr:al-dunyā, gloss:yakın dünya} ile {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} bu dizide yakın yararla son hesabı yan yana getirir; kurtuluş ve nimet gerçektir, fakat yakın hayatın yararı son dönüşün yerini tutmaz ve hesabı başkasına devretmez. Bu bağlantı gizli bir aldatma mekanizması ya da unutulmuş bir hatıra ileri sürmez (10:23).

31:34 Allah’ın rahimlerde olanı bildiğinden ve insanın yarın ne kazanacağını ya da nerede öleceğini bilememesinden söz eder. Odaktaki {ar:وَالِدٌ, tr:wālidun, gloss:ebeveyn} ve {ar:وَلَدِهِۦ, tr:waladihi, gloss:çocuğu} adları kimin ebeveyn, kimin çocuk olduğunu bildirir; doğum olayını açıklamaz, ama aile bağı kişinin bilinçli bilgisinden önce kurulmuştur. Aynı ayette yinelenen “nefis” her özneyi ayrı tutar: kimse yarınki kazancını bilemez, fakat bu kazanç olağan bir yarar arayışıdır, aldatma değildir. Ölüm yerinin bilinmemesi kişinin son sınırını da ailenin denetimi dışına koyar; aile köken verebilir ve eşlik edebilir, ama yarını ya da ölüm yerini onun yerine bilemez veya taşıyamaz. Aile bağıyla bu bilgi sınırı arasındaki bağlantı temkinli kalır: 31:34 yalnızca ilahî bilginin sınırlarını sıralıyor ve odaktaki vekâletsizliği sürdürmüyor da olabilir; yarınla ölüm yeri son günle özdeş değildir. Böylece aile kişiye köken ve eşlik verse de onun yarınını ya da ölüm yerini onun adına bilemez veya taşıyamaz (31:34).

</source_prose>
