# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:12**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.middle.claims.json`

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
- Refer to source paragraphs as `31:12 ¶N`.

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

`(31:12 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:12",
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
        "citation": "(31:12 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_12/31_12.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_12/31_12.middle.claims.json \
  --ayah-ref 31:12
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_12/31_12.prose.editorial.tr.md`

<source_prose>
## Armağanın Alıcısı

Âyet önce gerçekleşmiş bir bağışı bildirir. Açılıştaki {ar:وَلَقَدْ, tr:wa-laqad, gloss:vurgulu başlangıç} içindeki wa anlatım akışını sürdürür; önceki âyetin ne anlattığını tek başına belirlemez. Vurgu lâmı {ar:لَ, tr:la, gloss:vurgu lâmı} ile {ar:قَدْ, tr:qad, gloss:gerçekleşmişliği pekiştiren edat}, geçmiş biçimli {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} fiilini birlikte kuvvetlendirir; bu birleşim yeni bir nesne ya da katılımcı eklemez. Luqman’a verilen armağan, insanın sonraki karşılığından önce tamamlanmıştır. Ne miktarı ne de daha sonra nasıl kullanılacağı bu cümlede belirlenir. Açılıştaki lâm ile ileride göreceğimiz {ar:لِ, tr:li, gloss:yönelme ya da yarar edatı} aynı harftir ama aynı işi yapmaz: ilki qad ile bildirimi vurgular, ötekiler isimlerle yönelme veya yarar ilişkisi kurar.

{ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} IV. bâbın tamamlanmış biçimidir ve iki aktarım ilişkisi kurar: Allah verendir, {ar:لُقْمَٰنَ, tr:Luqmān, gloss:Luqman} alıcıdır, {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} ise verilen içeriktir. Belirli tanımlık, bu olayda verilen içeriği hikmet olarak belirler; hikmetin bütün kapsamı açık kalır. Luqman adı, belirsiz ve önceden var olan bir payeden çok armağanın gerçek alıcısını gösterir. Fiilin olağan anlamı “vermek” olarak kalır. Aynı söz ailesindeki ayrı geliş ve ulaşma alanı, alıcının Luqman ve taşınan şeyin hikmet oluşuyla birleşerek armağanın alıcıya eriştiğini duyurur; yankı yalnız bu erişimi belirginleştirir, ayrı bir yolculuk ya da kolaylık anlatısına dönüşmez. Adın kulağa dayalı lokma ve yutma çağrışımı, hikmeti içe alınan bir içerik gibi hissettirir; bu ses oyunu adı “lokma” diye çevirmeden ve hikmeti gerçek yiyecek saymadan çalışır. Âyet Luqman’ı burada armağanın alıcısı olarak tanıtır; ötesinde bir yaşamöyküsü vermez.

Odaktaki {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} sözü olağan anlamıyla bilgeliktir; arkasındaki {ar:أَنِ, tr:ani, gloss:açıklama ya da mastar bağlacı}, bu bağışı birinci bâbın {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} emir biçimine bağlar. Bağlacın açıklayıcı veya mastar biçiminde okunması, hikmetten emre geçişi korur; kıraatteki sesli bağlanma değişikliği iki okumada da cümle yapısını ve hedefi korur, fark ilişkinin duyuluşundadır. Böylece verilmiş hikmet, adlandırılmış bir paye olarak kalmayıp Allah’a yöneltilen şükürle uygulanır. Bu yakınlık, emrin hikmetin yaşama geçen yönünü gösterir ama hikmetin bütün anlamını tüketmez; metin burada önceden yaşanmış tartışmayı değil, armağanın yöneldiği buyruğu öne çıkarır.

## Hikmetin Yönü

{ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} bilgi ve usla doğruyu yanlıştan ayırıp doğru olana ulaşma anlamıyla, hemen arkasındaki bağımsız emirle birlikte eylemi yöneten bir ayırt etme yetisi gibi belirir. {ar:ح ك م, tr:ḥ-k-m, gloss:hüküm ve yönetme alanı} alanındaki ayrı bir kullanım zararlı yönelişi alıkoyup geri çevirerek ıslah etmeyi anlatır; bu temas, {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} emriyle karşısına çıkan {ar:كَفَرَ, tr:kafara, gloss:nankörlük etti} arasında seçme ve yanlış yönü tutma işini görünür kılar. Aynı alandaki gem, hayvanın çenesini kuşatıp koşmasını ve denetimsiz ilerlemesini sınırlar; bu bedensel tutuş özdenetimi duyulur kılar. Gem imgesi hikmetin sözlük anlamını değiştirmez: odaktaki katkısı hayvan ya da yargı sahnesi kurmak değil, ayırt etmenin taşıdığı sınırı bedende hissettirmektir.

Bu ayırt etme 31:13’te aile içindeki öğütte somutlaşır. {ar:يَٰبُنَىَّ, tr:yā bunayya, gloss:ey oğulcuğum} hitabı baba-oğul bağını kurar; Luqman oğluna {ar:لَا تُشْرِكْ بِٱللَّهِ, tr:lā tushrik bi-llāh, gloss:Allah’a ortak koşma} der. {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik}nin doğru yönü seçen yanı, bağlılığın bölünmesine karşı sınır çizer. {ar:لِلَّهِ, tr:li-llāhi, gloss:Allah’a} ile yasağın bağlandığı Allah adı aynı özel addır; bu yankı bağlılığı ibadete yöneltir, sözcüğün kökenini açıklamaz ya da onu genel “ilah” karşılığına çevirmez. Hitap öğüdü ve baba-oğul bağını kurar; oğlun sonraki düşüncesi ve cevabı açık bırakılır.

Oğula seslenen {ar:يَٰبُنَىَّ, tr:yā bunayya, gloss:ey oğulcuğum} hitabı, aynı kökle ilişkili parçaları birleştirip bina etmeyi anlatan ayrı bir kullanımı çağrıştırarak öğüdün biçim verici yönünü duyurur; oğul sözcüğünün olağan anlamı bu çağrışımla değişmez. 31:13’teki {ar:لَظُلْمٌ عَظِيمٌ, tr:la-ẓulmun ʿaẓīm, gloss:büyük bir haksızlık} büyük bir haksızlığı adlandırır; zulmün başka bir kaynak kullanımındaki “yanlış yere ya da zamana koyma” imgesi, ortak öğüt yapısına yönün bozulduğunu düşündüren bir benzetme ekler, âyetin sözlük anlamı olmaz. {ar:وَهُوَ يَعِظُهُۥ, tr:wa-huwa yaʿiẓuhu, gloss:ona öğüt verirken} olağan anlamıyla Luqman’ın oğluna öğüdünü verir; bu uyarı içindeki hatırlatma ve kalbi yumuşatma yönü, sözü daha içten işittirir. Bu bağlam için söz konusu yankının ötesinde doğrulanmış bir kök ve biçim çözümlemesi yoktur.

{ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} yön verme imgesiyle 31:18 ve 31:19’da yüz, yürüyüş ve sesin düzenlenişine uzanır. {ar:وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:wa-lā tuṣaʿʿir khaddaka li-l-nās, gloss:insanlara yanağını çevirip yüzünü ekşitme} ile {ar:وَلَا تَمْشِ فِى ٱلْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī al-arḍi maraḥā, gloss:yeryüzünde böbürlenerek yürüme} önce yüzün ve boynun yönelişini, sonra böbürlenen yürüyüşü düzenler. {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-qṣid fī mashyik, gloss:yürüyüşünde ölçülü ol} adımı durdurmak yerine aşırılıklar arasında ölçer; {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtik, gloss:sesini alçalt} ise sesi kısmayı ister ve {ar:إِنَّ أَنكَرَ ٱلْأَصْوَٰتِ لَصَوْتُ ٱلْحَمِيرِ, tr:inna ankara al-aṣwāti la-ṣawtu al-ḥamīr, gloss:seslerin en çirkini eşeklerin sesidir} sözü bu ölçünün duyulur sonucunu verir. Yüzün yönü, adımın dengesi ve sesin alçaltılması, gem imgesindeki sınırlandırmayı üç gündelik kanala taşır: bedenin duruşu, hareketi ve işitilen etkisi. Bu aktarım hikmetin soyut yönünü gündelik ölçüye çevirir; gemle beden arasında ayrıntılı kök-konum eşleştirmesi kurmaz ve bu buyruklar hikmetin tek, tam mekanizması değildir.

## Şükrün Adresi ve Karşılığı

Az önce gündelik davranışta yönünü gördüğümüz hikmetin ilk açık karşılığı, {ar:أَنِ ٱشْكُرْ لِلَّهِ, tr:ani ushkur li-llāhi, gloss:Allah’a şükret} buyruğunda Allah’a yönelir. Buyruktaki {ar:لِلَّهِ, tr:li-llāhi, gloss:Allah’a} içindeki li, Allah adını mecrur biçimde şükrün açık hedefi yapar. Böylece şükür adsız bir iç hâl değil, yöneltilmiş karşılıktır; edat tek başına ibadetin bütün boyutlarını anlatmaz. Allah, Yaratıcı’yı başkalarından ayıran özel addır. Bu adın şükür emriyle ve 31:13’teki ortak koşma yasağıyla buluşması, aynı hedefteki bağlılığı bölünmez kılar; bu yerel yankı adı türetmez.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğunun kaynağı tanıma yönü başka alıcılara ve karşılıklara bakınca belirginleşir. Davut ile Süleyman’a bilgi verildikten sonra 27:15’te {ar:ٱلْحَمْدُ لِلَّهِ, tr:al-ḥamdu li-llāh, gloss:hamd Allah’adır} denir. Süleyman 27:19’da kendisine ve anne babasına verilen nimeti anarak {ar:أَنْ أَشْكُرَ نِعْمَتَكَ, tr:an ashkura niʿmataka, gloss:nimetine şükretmem} ve {ar:أَنْ أَعْمَلَ صَٰلِحًا, tr:an aʿmala ṣāliḥan, gloss:salih iş yapmam} diye dua eder. 27:40’ta {ar:أَشْكُرُ أَمْ أَكْفُرُ, tr:ashkuru am akfuru, gloss:şükredeyim mi nankörlük mü edeyim} sorusu alınan nimeti sınav olarak kurar; yarar şükredene döner, veren ihtiyaçsız kalır. Karşıt örnekte 2:258’de Allah’ın hükümranlık verdiği hükümdar kudreti kendine mal edip {ar:أَنَا۠ أُحْىِۦ وَأُمِيتُ, tr:anā uḥyī wa-umītu, gloss:ben yaşatır ve öldürürüm} der. {ar:ح ك م, tr:ḥ-k-m, gloss:hüküm ve yönetme alanı} içindeki zararlı yönelişi alıkoyup geri çevirme kullanımıyla, şükrün verilmiş gücü kendine mal etmeyi frenleyişi arasındaki bağ benzetme düzeyindedir; bu, sözcüğün doğrudan anlamı değildir. Bu örnekler doğru kaynağı tanıyıp uygun karşılık verme yönünü açar; 2:258’deki hükümdar, verilen kudreti kendine mal etmenin karşı örneği olarak kalır. Karşılaştırma Luqman hakkında hüküm vermez: başka alıcılara verilen bilgi Luqman’ın hikmeti değildir ve Luqman Süleyman’la özdeşleşmez.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğu iyiliği ve iyilik yapanı tanımayla başlar; bu tanıma sözle duyurulabilir, övgüde görünür olabilir veya alınan nimete uygun bir işe dönüşebilir. Süleyman’ın 27:19’daki duası tanımayı salih iş dileğiyle yan yana getirir; 34:13’te Davut ailesine {ar:ٱعْمَلُوٓا۟ ءَالَ دَاوُۥدَ شُكْرًۭا, tr:iʿmalū āla dāwūda shukrā, gloss:ey Davut ailesi, şükür olarak çalışın} buyurulur. Böylece şükür etkin karşılık olarak da okunur. 31:12’deki yalın emir bu örneklerle çalışmaya daralmaz: içten tanıma ve sözle şükür de karşılık olarak kalır; emir doğrudan şükür çağrısıdır, sebep bildiren bir fiil ya da kendiliğinden büyüme vaadi değildir.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğu etkin bir karşılık taşır; aynı söz ailesindeki körpe sürgün kullanımı ise gövdenin ya da ağacın dibinden yeni oluşun belirmesini anlatır. Verilmiş hikmet ve yararın şükredene dönmesiyle bu sürgün imgesi buluştuğunda, alınan iyiliğin alıcıda görünür gelişmesini duyurur; ağaç ve ürün odağın sahnesine değil, yankıya aittir. Başka bir kullanım az girdiden belirgin gelişmeyi—az yemle gelişen hayvanı ya da az yağmurla yeşeren filizi—gösterir. Ayrı bir dal da ürünün veya içeriğin bollaşmasını öne çıkarır. İlki az girdiyle gelişmeyi, ikincisi çıkan ürünün çokluğunu anlatır; böylece yararın iki ayrı yönü duyulur, tek ve genel bir büyüme anlamına kapanmaz.

31:10 bu gelişme imgesinin işlemlerini görünür kılar: {ar:أَنزَلْنَا, tr:anzalnā, gloss:indirdik} suyu aşağıya gönderir, {ar:مَاءً, tr:māʾan, gloss:su} bitkinin gelişeceği ortamı sağlar ve {ar:فَأَنۢبَتْنَا, tr:fa-anbatnā, gloss:bitkileri yeşerttik} gözle görülen yeşermeyi başlatır. Bu iniş, su ve bitki sırası az girdiden belirgin gelişme kolunu somutlaştırırken, 14:7’deki {ar:لَأَزِيدَنَّكُمْ, tr:la-azīdannakum, gloss:sizi elbette artıracağım} vaadi artış kolunu açar. Odaktaki {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} yararın alıcısını bildirir; nefsin yaşayan bireyi de adlandırabilmesi, verimin kendisine ulaştığı kişiyi belirginleştirir. “Az girdi” buradaki gelişme imgesinin karşılaştırma eksenidir, yağış miktarına ilişkin bir ölçü değildir; 31:10 yağmurun miktarını vermez. Bitki, su ve artış sahneleri yaşayan alıcıya ulaşan etkiyi görünür kılar; biyolojik bir açıklama sunmaz.

## Yararın Kendine Dönüşü

Yararın hangi alıcıya döndüğü, koşul cümlelerinde genel bir kurala bağlanır. Luqman belirli armağanın alıcısıdır; ardından gelen {ar:وَمَن يَشْكُرْ, tr:wa-man yashkur, gloss:kim şükrederse} içindeki man, karşılık kuralını herkese açar. İkinci dalı başlatan wa ile {ar:وَمَن كَفَرَ, tr:wa-man kafara, gloss:kim nankörlük ederse} aynı çerçeveye eklenir: şükür ve nankörlük birbirine karşıt iki seçimdir, biri ötekinin ardından gelen aşama değildir. Şükür fiili {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} emrinden {ar:يَشْكُرْ, tr:yashkur, gloss:şükrederse} koşul biçimine, oradan {ar:يَشْكُرُ, tr:yashkuru, gloss:şükreder} yanıtının bildirici, merfû biçimine ilerler. Man’dan sonra ilk fiil cezm alarak seçilebilir eylemi gösterir; yanıt biçimi onu sonuç diye bildirir. Bu basamaklar aynı köke ait olsa da dilbilgisel görevleri ayrıdır ve sonuç şükrün miktarını ölçmez.

İlk koşulun yanıtını başlatan {ar:فَ, tr:fa, gloss:sonuç bağlacı}, “şükreden olursa ne olur?” sorusunu kendi sonucuna bağlar. {ar:إِنَّمَا يَشْكُرُ لِنَفْسِهِۦ, tr:innamā yashkuru li-nafsihi, gloss:ancak kendi nefsi için şükreder} şükrün yararını aynı eyleyene sınırlar: “kim şükrederse” diye açılan kişi yanıtta da eyleyen kalır, nefse eklenen iyelik eki de bu dönüşün yerini onun kendi benliği yapar. Odaktaki {ar:لِلَّهِ, tr:li-llāhi, gloss:Allah’a} içindeki ilk li şükrü Allah’a yöneltirken ikinci li, nefsin önünde yararın vardığı yeri gösterir. Aynı edatın bu iki işlevi dışa yönelen karşılık ile içe dönen yarar arasında bir ayna kurar; böylece yarar şükreden kişide kalır, Allah’a geri ödeme ilişkisi kurulmaz. İlk olumlu koşulun son içerik sözcüğü olan nefsihi, ardından gelen {ar:وَمَن كَفَرَ, tr:wa-man kafara, gloss:kim nankörlük ederse} yeni genel koşulu açmadan önce bu yerel düşünceyi kapatır. Bu gözlem ilk koşuldaki nefsihi'nin yerel işleviyle sınırlıdır; tek başına daha geniş bir Kur’anî benlik örüntüsünü kanıtlamaz.

Buradaki {ar:نَفْسِهِۦ, tr:nafsihi, gloss:kendi nefsi} için öne çıkan anlam kişinin kendisi, benliği veya iç yaşamıdır. Aynı söz ailesindeki nefes alıp verme ve sıkıntıyı hafifletme kullanımları, {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğuyla alınmış iyiliği tanımanın ve yararın benliğe dönmesinin yanına gelince içeri girip çıkan nefes ve yükü hafifleten ferahlık imgesi verir. Böylece yararın kendine dönüşü bedensel bir açılma gibi hissedilebilir. Bu yankı odakta somut bir solunum, içecek ya da klinik durum sahnesi kurmaz; nefsin ve şükrün olağan anlamını koruyarak bedensel ferahlık hissiyle sınırlı kalır.

{ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} ile ifade edilen kendine dönüş, özel çıkar yerine kendi eyleminin karşılığını üstlenme olarak da genişleyebilir. 29:6’da çabanın kişinin kendi nefsi için olduğu ve Allah’ın âlemlerden müstağni kaldığı belirtilir; 41:46 ve 45:15’te iyi işin yapanına, kötülüğün de kendi failine döndüğü söylenir. Bu paraleller, 31:12’deki öz-yarar ilkesini sorumluluk içinde konumlandırır; şükür çabayla özdeşleşmez, her eylem için de tek tip sonuç çıkarılmaz. Nefsin daha içsel ahlaki boyutu keşifsel bir genişlemedir: odakta ifade önce eyleyen kişinin kendisini gösterirken, 59:19’daki Allah’ı unutup kendilerini unutanlar ve 75:2’deki kendini kınayan nefis, bu yararı vicdan ve öz-farkındalıkla düşünmeye açar. Bu temas nefsin odakta doğrudan “düşünce” olduğu anlamına gelmez; düşünce, niyet veya kişiye özgü bilgi, kişinin kendine dönen karşılığının iç boyutları olarak olasılık düzeyinde ilişkiye eklenir.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} çağrısının {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} yararı kişiye dönerken onu ilişkilerinden koparmaz. 31:14 annesinin çocuğu {ar:حَمَلَتْهُ أُمُّهُ وَهْنًا عَلَىٰ وَهْنٍۢ, tr:ḥamalathu ummuhu wahnan ʿalā wahn, gloss:annesi onu güçlük üstüne güçlükle taşıdı} diye taşımasını, ardından {ar:وَفِصَالُهُۥ فِى عَامَيْنِ, tr:wa-fiṣāluhu fī ʿāmayn, gloss:iki yılda sütten kesilmesini} anlatır. Taşımaya eşlik eden yinelenen zayıflık ve güçlük bakımın bedensel yükünü, sütten kesilme ise taşınmadan ayrılmaya geçişi gösterir. Ardından gelen {ar:أَنِ ٱشْكُرْ لِى وَلِوَٰلِدَيْكَ, tr:ani ushkur lī wa-li-wālidayk, gloss:bana ve anne-babana şükret} buyruğundaki li, Allah’ı ve anne-babayı ayrı hedefler olarak şükrün kapsamına katar. Bu yakın sahne, odaktaki şükrü alınmış bakımın ve bakım verenin tanınmasına genişletir; ebeveynler 31:12’nin kendi sahnesinde değil, 31:14’ün bağlamındadır. Allah’ın {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} oluşu şükrün O’ndaki bir eksiği kapatmadığını, yararın ise alıcıya döndüğünü açıklar; Allah ile anne-baba ayrı muhataplardır.

31:14’teki bakım anlatısı, odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğunun ailede yöneldiği karşılığı gösterir; şükür burada gerçekleşmiş sonuç değil, istenen eylemdir. Odaktaki {ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık} Allah’ı övgüye layık niteler. Hamdın yermenin karşıtı olma yönü Allah hakkındaki bu olumlu niteliği, iyilik için teşekkür etme yönü ise 31:14’te bakımın ardından gelen emri aydınlatır; sıfat, insanın şükür eylemiyle aynı şey değildir. Odaktaki {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} ile kişinin kendisine dönen yarar, bağımlılığını hatırlayan, ilkesini koruyan ve bakım ilişkisini sürdüren bir benlik olarak duyulur. Taşıma, güçlük, sütten kesilme ve şükür buyruğu birlikte bağımlılığın biçim değiştirişini gösterir; bu anlatı dizisi ayrıca kök eşleştirmesi kurmaz.

31:15 bu yakınlığın içindeki sınırı belirginleştirir. {ar:فَلَا تُطِعْهُمَا أَن تُشْرِكَ بِى, tr:fa-lā tuṭiʿhumā an tushrika bī, gloss:bana ortak koşma çağrısında ikisine itaat etme} zararlı isteğe uymamayı söyler; ardından {ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī al-dunyā maʿrūfan, gloss:dünyada onlarla uygun ve güzel biçimde geçin} iyi muameleyi ve refakati sürdürür. Bu iki buyruk ilişkiyi birlikte düzenler: şirk çağrısına sınır konurken iyi arkadaşlık korunur. {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik}deki geri çevirme yönüyle bu örnek arasında ölçülü sadakat bağı kurulabilir; ebeveynin yasağı odaktaki hikmetin bir uygulaması da, daha genel bir ilkenin örneği de olabilir. 31:14’ün bakım anlatısı ile 31:15’in sınır ve refakat buyruğu iki ayrı yakın bağlamdır; aralarındaki ilişki bağlamsaldır, bu yüzey ayrıntıları için ayrıca kök eşleştirmesi ileri sürülmez.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} çağrısının {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} yararı aile içinde yaşansa da kişinin karşılığı başkasına devredilemez. 31:33’te ne ebeveyn çocuğun yerine ne çocuk ebeveynin yerine karşılık verebilir; {ar:يَجْزِى, tr:yajzī, gloss:karşılık verir} ile {ar:جَازٍ, tr:jāzin, gloss:karşılık veren} aynı kökün ayrı biçimleridir. Yanlarındaki daha keşifsel “kesme” kullanımı, gerçek bir kesme eyleminden çok, vekâletin aktarım kanalını kapatan bir imge sağlar. {ar:وَالِدٌ, tr:wālidun, gloss:ebeveyn} ile {ar:وَلَدٌ, tr:waladun, gloss:çocuk} doğum ve soy bağının iki yönünü gösterir; yakınlık vekâlet yerine geçmez. 46:15’teki dua Allah’a nimeti için şükretmeyi, ebeveynlere iyiliği, salih işi ve sonraki kuşak için iyilik dilemeyi bir araya getirir; kişisel sorumluluk böylece ilişki içinde kalır. 31:33 genel bir yargı günü uyarısı da olabilir; 46:15 burada ayrı bir dua olarak yankılanır, doğrudan bir bağ kurulmuş değildir.

## Örtülen ve Gizli Kalan

Aile bağındaki vekâletsizlikten sonra, 31:12’deki ikinci koşulun birinci bâbdaki geçmiş biçimi {ar:كَفَرَ, tr:kafara, gloss:nankörlük etti} alınmış nimeti yadsıma ve değerini örtme yönünde işler; karşısındaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} ayrı bir eylemdir. Bu ahlaki zıtlık 31:12’nin kendi koşullarında kurulur; 14:7’deki artış vaadi onun kaynağı değildir. Kafara’nın başka bir kullanımında çiftçi tohumu toprağa koyup üzerini örter; bu örtme, görünür gelişmenin gömülü yanını düşündürerek nimetin değerini örtme imgesine katkı verir. Odak âyetin sahnesi tarım değil, karşıt iki tutumdur. 31:14’te alınan anne bakımını reddetme bu yankıyla düşünülebilir; benzetme her itaatsizliği bakımın reddi saymaz.

{ar:كَفَرَ, tr:kafara, gloss:nankörlük etti} ile açılan örtülme imgesi, 31:16’daki hardal tanesiyle gizli nesnenin küçücük ölçeğine taşınır. {ar:حَبَّةٍۢ مِّنْ خَرْدَلٍۢ فِى صَخْرَةٍ, tr:ḥabbatin min khardalin fī ṣakhratin, gloss:kayanın içindeki hardal tanesi} sert kayanın içindeki küçücük taneyi gösterir; {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā Allāhu, gloss:Allah onu getirir} gizli kalanın silinmediğini ve Allah’ın onu ortaya getirdiğini söyler. Bu görüntü, {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} ile anlatılan yararın hemen görünmeyip çok küçük ölçekte saklı kalabilmesini düşündürür. 31:16 genel hesap verebilirliği de anlatıyor olabilir; hardal tanesi doğrudan şükür ya da nankörlük diye adlandırılmaz. {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīr, gloss:Latif ve her şeyden haberdar} nitelemesi, kayanın içindeki küçücük şeyin de bilinebilirliğini vurgular. 31:14’te bakım alanın şükre çağrılması ile Allah’ın {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} oluşu, alan ile karşılığa muhtaç olmayan vereni ayırır; 31:16’da gizli taneyi bilip ortaya çıkarma bu asimetriyi başka ölçekte duyurur, taneyi bakımın gizli karşılığına dönüştürmeden. Tanenin canlı oluşu küçük ama canlı bir potansiyeli de taşır; bu ayrıntı ayrıca bir kök yorumu getirmez.

31:16’daki gizli tane ile 31:10’daki gelişme iki ayrı işlemi görünür kılar: ilkinde Allah kayanın içindeki şeyi ortaya getirir, ikincisinde su inişi ve bitki yeşermesi büyümeyi kurar. Hardal tanesi kendi sahnesinde gizli kalan nesnedir; bu görüntü odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğunun ya da yağmurun yerine geçmez. Bunun yanında odağın verme fiiliyle bir varış yankısı oluşur: 31:12’deki {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} IV. bâb biçimi {ar:لُقْمَٰنَ, tr:Luqmān, gloss:Luqman} alıcısına {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} armağanını aktarırken, 31:16’daki {ar:يَأْتِ بِهَا, tr:yaʾti bihā, gloss:onu getirir} aynı kökün ayrı biçimiyle gizli olanı ulaştırır. Ortak kök armağan ile ortaya çıkarma arasında bu erişim temasını kurar; odaktaki fiilin olağan “vermek” anlamı yerinde kalır.

Veriş yönünü tersine çeviren deneysel bir ekonomik karşı-imge de belirir. {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} olağan anlamıyla Allah’tan Luqman’a hikmet aktarır; aynı söz ailesindeki vergi veya haraç kullanımı ise kişi ya da topluluğun yönetime para ödemesiyle akışı tersine çevirir. Bu imgeyi bağımsız olarak {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğu, {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} yararın kişiye dönmesi ve Allah’ın {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} oluşu tetikler: ödeme otoriteye geri dönecekmiş gibi görünürken âyet kazancı alıcıda bırakır ve vereni karşılığa muhtaç kılmaz. Böylece şükür bedel değil, alınmış iyiliğin tanınması olarak duyulur. Karşı-imge yalnız akış yönünü karşılaştırır; 31:12’de gerçek vergi, rüşvet, hukukî ödeme ya da Allah’a sunulan bir karşılık ilişkisi kurulmaz.

## İhtiyaçsız Kaynak

İki koşulun yanıtı fa ile başlar, fakat farklı sonuçları öne çıkarır. Şükür kolundaki {ar:فَإِنَّمَا, tr:fa-innamā, gloss:öyleyse ancak} yararın şükredene dönüşünü sınırlar; nankörlük kolundaki {ar:فَإِنَّ, tr:fa-inna, gloss:öyleyse gerçekten} ise Allah’ın niteliğini bildiren vurgulu cümleyi açar. Böylece ilk yanıt insanın karşılığını, ikincisi veren hakkındaki beyanı taşır. Allah adı önce {ar:لِلَّهِ, tr:li-llāhi, gloss:Allah’a} içinde şükrün hedefi olarak mecrur, sonra {ar:إِنَّ ٱللَّهَ, tr:inna Allāha, gloss:şüphesiz Allah} içinde inna’dan sonra mansub ve iki kapanış yükleminin açık öznesi olur. Görev ve çekim konumu değişirken merci aynı kalır. İnna’nın vurgusu cümlenin iki yüklemine yönelir; koşuldaki kişinin eylemi bu vurgunun nedeni değildir. Koşul insanı olası eyleyen olarak kurarken, ardından gelen ad cümlesi Allah’ın süreğen niteliğini bildirir; bu sıfatlar tek bir koşul öznesine bağlı kalmaz. Allah, hem {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} hem {ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık} sıfatının açık öznesidir.

İlk sıfat, Allah’ın insan şükründen önce de var olan ihtiyaçsızlığını bildirir ve nankörlük karşısında da aynı kalır; insanın seçimi ise kendisi için sonuç taşımayı sürdürür: şükreden yarar görür, nankörlük eden kendi seçiminin sonucunu üstlenir. {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} söz ailesi bolluk ile ihtiyaçtan uzaklığı kapsayabilir; burada nefsin yararı ve nankörlük koşuluna verilen cevap, maddî zenginlikten çok hiçbir karşılığa muhtaç olmama yönünü öne çıkarır. Cümle bu ihtiyaçsızlığı vurgular; ne maddî bolluk ne de armağanın niceliği hakkında hüküm verir.

Odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğu ile {ar:غَنِىٌّ, tr:ghaniyyun, gloss:hiçbir şeye muhtaç olmayan} niteliği arasındaki ödeme ayrımı, verişin yönüyle belirginleşir: Allah hikmeti Luqman’a verir, {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} ile bildirilen yarar şükredenin nefsine döner; ihtiyaçsız verene geri ödeme gerekmez. Şükür söz ailesindeki ayrı “yeterli olma, yarar sağlama” kullanımı hediyenin alıcı için faydasını öne çıkarır; burada anlatılan, zenginleştirme ya da başka bir şeyin yerini tutma değil, alınan nimetin yararıdır. Önceki haraç karşı-imgesinde para otoriteye giderken, odaktaki akış Allah’tan Luqman’a, yararı da alıcıya yöneltir; bu nedenle karşı-imge gerçek ödeme değil, yön farkını görünür kılan benzetmedir.

Son sıfat {ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık}, {ar:غَنِىٌّ حَمِيدٌ, tr:ghaniyyun ḥamīdun, gloss:muhtaç olmayan ve övülmeye layık} çiftinde ikinci yüklem olarak gelir. Kapanış hem nankörlüğün Allah’ı eksiltmediğini hem O’nun övgüye layık niteliğini bildirir. İki belirsiz, merfû sıfatın benzer sonluğu ses ve sözdizimi bakımından cümleyi birlikte mühürler; bu ses düzeni ayrı bir kıraat varyantı değildir. Şükür alınan iyiliği ve vereni tanır; hamd ise Allah’ta karşılaşılan övgüye değer niteliği adlandırır, insanın sunduğu bir bedel değildir. Başlangıçta {ar:لِلَّهِ, tr:li-llāhi, gloss:Allah’a} içinde şükrün hedefi olan ad, burada {ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık} ile yeniden buluşur; bu yankı özel ada köken açıklaması getirmez. İnsan şükretsin ya da nankörlük etsin, Allah hamid kalır.

{ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık} ile ilişkili hamdın ayrı “deneyim veya sınamadan sonra övülesi bulunma” kullanımı, iki insan karşılığının ardından gelen sıfatla ihtiyatlı bir temas kurar; bu temas odağa tarihsel bir sınama sahnesi eklemez. “Övülmüş kişi” kullanımı, birine övgü yöneltildiğinde onun övülmüş diye nitelenmesini açıklar. Cümlede nicelik işareti bulunmadığından bu kullanımlar sıfatı çok sayıda övülesi niteliğin sayımına dönüştürmez. Allah’ın övgüye layıklığı insanın seçtiği karşılıklardan bağımsız kalır.

Odaktaki {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} ile {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} armağanının ve {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} karşılığının düşündürdüğü bağımsızlık, 31:26 ve 31:27’deki tükenmeme görüntüsüyle genişler. Tek alıcıya verilen hikmet ilk bakışta sınırlı aktarım gibi duyulabilir; 31:26’da her şeyin Allah’a ait oluşu {ar:ٱلْغَنِىُّ, tr:al-ghaniyy, gloss:ihtiyaçtan bağımsız} niteliğini maddî bolluktan çok ihtiyaçsızlık olarak öne çıkarır, {ar:ٱلْحَمِيدُ, tr:al-ḥamīd, gloss:övülmeye layık} da övgüye değer oluşu bildirir. 31:27’de denizi uzatan {ar:يَمُدُّهُ, tr:yamudduhu, gloss:onu uzatır} imgesi yedi denizi mürekkep kaynağına ekler; {ar:مَا نَفِدَتْ كَلِمَاتُ ٱللَّهِ, tr:mā nafidat kalimātu Allāh, gloss:Allah’ın sözleri tükenmez} sözü bu sözlerin tükenmediğini belirtir. Aynı âyetin sonundaki {ar:حَكِيمٌ, tr:ḥakīm, gloss:hikmet sahibi}, sağlam ve kusursuz kılma yönündeki ayrı kök kullanımıyla odaktaki hikmete yeniden temas eder. Bu bağ tükenmeyen kaynak karşısındaki alıcıyı düşünmeye açar; sonlu alıcıya verilen hikmet ilahî sözlerle özdeşleşmez ve 31:27 özellikle Allah’ın sözlerinin tükenmezliğini anlatıyor olabilir. Böylece şükür kaynağı yenileyen bir ödeme değil, o kaynağa yönelen karşılık olarak kalır.

## Değişen Geçişler

Tükenmeyen kaynağın karşısındaki alıcıya dönünce, odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğunun açtığı şükür, geçmişte alınmış tek bir nimeti kaydetmekten, zaten kuşatan desteğe bağlı kalmayı sürdüren bir yönelişe genişleyebilir. 31:20’deki {ar:أَسْبَغَ عَلَيْكُمْ, tr:asbagha ʿalaykum, gloss:üzerinize bolca yaydı} ifadesi nimetlerin üzerinize bolca yayılmasını, {ar:نِعَمَهُ, tr:niʿamahu, gloss:nimetlerini} ifadesi ise bu iyiliklerin O’na ait oluşunu bildirir. 31:22’de {ar:ٱسْتَمْسَكَ, tr:istamsaka, gloss:sımsıkı tutundu} tutup bırakmamayı, {ar:بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:bil-ʿurwati al-wuthqā, gloss:en sağlam kulpa} ise dayanağın sağlamlığını gösterir. Kuşatan nimet ile tutulan sağlam kulp, şükrü mevcut desteğe bağlanan bir tutuş gibi düşündürür; bu tutunma genel teslimiyet ve iyi davranış için de geçerli olabilir.

31:31’deki gemi, odaktaki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} buyruğunun yönelişini değişen koşullardaki tanımaya taşır. {ar:ٱلْفُلْكُ, tr:al-fulk, gloss:gemi} denizde {ar:تَجْرِى, tr:tajrī, gloss:akar} ve {ar:بِنِعْمَتِ ٱللَّهِ, tr:bi-niʿmati Allāh, gloss:Allah’ın nimetiyle} geçişi mümkün kılarak işaretleri görünür eder. Sabır, paniğe kapılmamak için nefsi tutar; {ar:صَبَّارٍ شَكُورٍ, tr:ṣabbārin shakūr, gloss:çok sabreden ve çok şükreden} bu işaretleri seçebilen tanığı niteler. Böylece odaktaki şükür bir nimetten hemen sonra verilen anlık teşekkürden, hareket sürerken nimeti tanımayı sürdüren bir yöne genişler. 31:31 bu nitelikleri aynı gözlemcide birleştirebilir; farklı gözlemciler arasında da dağıtabilir, dolayısıyla tek kişilik bir zaman dizisi zorunlu değildir.

Denizdeki hareket 31:32’de tehlikeye dönüşür: {ar:غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ, tr:ghashiyahum mawjun kaẓ-ẓulal, gloss:üstlerini gölgelikler gibi dalga kaplar} dışarıdan örten tehlikeyi, {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ, tr:daʿaw Allāha mukhliṣīn, gloss:Allah’a içtenlikle yalvardılar} sıkışma içindeki samimi çağrıyı verir. Dalganın dıştan örtmesi, nankörlüğün bilinen nimeti örtmesinden ayrı bir harekettir. {ar:نَجَّىٰهُمْ, tr:najjāhum, gloss:onları kurtardı} koşulları değiştirince, ardından gelen {ar:يَجْحَدُ, tr:yajḥadu, gloss:bildiğini inkâr eder} bilerek reddetmeyi, {ar:خَتَّارٍ, tr:khattār, gloss:ahdini bozan} sadakati bozmayı, {ar:كَفُورٍ, tr:kafūr, gloss:çok nankör} nimeti örtmeyi adlandırır. Böylece 31:12’deki {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret}–{ar:كَفَرَ, tr:kafara, gloss:nankörlük etti} karşıtlığı, kurtuluştan sonra bilinen iyiliğin yeniden örtülebilme ihtimaline açılır; ayet bu davranışı aynı dua eden kişilere tek tek bağlamaz. 64:6’da elçilerin reddedilmesinin ardından Allah’ın ihtiyaçsız ve övgüye layık olduğunun söylenmesi de bu karşıtlığı açar: değişen veren değil, alıcının nimete ilişkisidir.

Gemi ve kurtuluş bağlamlarından ayrı bir soru açılır: odaktaki {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:bilgelik} belirsizlik içinde yön gösterebilir; katkısı yarının bilgisini vermek değil, eldeki yönelişe rehberlik etmektir. 31:34’te hiçbir nefsin yarın ne kazanacağını ve hangi yerde öleceğini bilmediği söylenir: {ar:نَفْسٌ مَّاذَا تَكْسِبُ غَدًا, tr:nafsun mādhā taksibu ghadan, gloss:hiçbir nefis yarın ne kazanacağını bilmez} yakın kazancı, {ar:بِأَىِّ أَرْضٍ تَمُوتُ, tr:bi-ayyi arḍin tamūtu, gloss:hangi yerde öleceğini bilmez} ise yaşamın son yerini bilinmez bırakır. Buradaki {ar:تَدْرِى, tr:tadrī, gloss:bilirsin} olağan anlamıyla “bilmek”tir. Aynı biçimle ilgili daha keşifsel kök yankısı yol ve rüzgârla hizalanma imgesi taşır; bu temas bilme anlamını koruyup yöneliş ile tahmini ayırır. Bu okuma hikmetin belirsizlikte yön bulma işlevini genişletebilir; 31:34 yalnızca ilahî bilgiyi anlatıyor da olabilir, bu durumda 31:12’deki {ar:لِنَفْسِهِۦ, tr:li-nafsihi, gloss:kendi nefsi için} yararın pratik anlamı olduğu gibi kalır.

Burada bakış ölçeği değişir: insanın bilemediği yarından, insanı da aşan övgü ufkuna geçilir. 17:44’te gökler, yer ve içindekiler Allah’ı tesbih eder; {ar:يُسَبِّحُ بِحَمْدِهِۦ, tr:yusabbiḥu bi-ḥamdihi, gloss:O’nu hamdiyle tesbih eder} ifadesi 31:12’deki {ar:حَمِيدٌ, tr:ḥamīdun, gloss:övülmeye layık} niteliğini bütün varlığa yayılan bir övgü ufkuna açar. İnsanların bu tesbihi kavrayamadığının söylenmesi, yaratılmışların tesbihini odaktaki insanî {ar:ٱشْكُرْ, tr:ushkur, gloss:şükret} ile özdeşleştirmeden, Allah’ın övgüye değer oluşunun insan karşılığından bağımsız genişliğini duyurur.

</source_prose>
