# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:2**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.middle.claims.json`

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
- Refer to source paragraphs as `17:2 ¶N`.

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

`(17:2 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:2",
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
        "citation": "(17:2 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_2/17_2.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_2/17_2.middle.claims.json \
  --ayah-ref 17:2
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_2/17_2.prose.editorial.tr.md`

<source_prose>
Ayet, Musa'ya Kitap verildiğini, bu Kitap'ın İsrailoğulları için yol gösterici kılındığını ve ardından “Benden başka bir vekil edinmeyin” buyruğunun geldiğini söyler. Tamamlanmış iki ilahi eylemi, topluluğun önünde duran henüz gerçekleşmemiş bir tercih izler.

## Verilişten Yönelişe

Başlangıçtaki bağlı {ar:وَ, tr:wa, gloss:ve}, sesçe {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} fiiline tutunur. Bu bağ ilişkiyi ve kapsamı açar; kendi başına yeni bir olay, özne ya da nesne getirmez. Böylece ayet yerel bir eylem birimi olarak başlar, önceki sahne hakkında hüküm vermez. {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} tamamlanmış etkin birinci çoğuldur; veren özne fiilin içindedir. İki nesneli kuruluşta {ar:مُوسَى, tr:Mūsā, gloss:Musa} alıcı, {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} verilen şeydir. Musa özel addır; Arapça içinde bir kök anlamından türetilmez. Sözcük sırası ve adın uzun son ünlüsü, Kitap nesnesine geçilmeden önce alıcının konumunu duyurur. Musa ne kitabın yazarı ne de adı ardından gelen topluluğun nihai yararlanıcısıdır. Fiilin olağan “vermek” anlamı sürerken, aynı söz ailesindeki “gelmek, ulaşmak” kullanımı bu alıcı-nesne yapısıyla buluşup Kitap'ı alıcıya erişen bir armağan gibi duyurur; “vermek, sunmak” anlamı da bu verilmişliği pekiştirir.

Belirtili tekil {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}, herhangi bir yazıyı değil tanınabilir bir vahiy kitabını gösterir ve ilk eylemin verilen nesnesi olarak cümleyi kapatır. Ardından gelen ikinci {ar:وَ, tr:wa, gloss:ve}, sesçe {ar:وَجَعَلْنَٰهُ, tr:wa-jaʿalnāhu, gloss:ve onu kıldık} fiiline bağlanırken yeni bir eşgüdümlü eylem açar. Aynı ilahi özne iki tamamlanmış fiilde sürer: Kitap önce verilir, sonra bir işleve kılınır. {ar:وَجَعَلْنَٰهُ, tr:wa-jaʿalnāhu, gloss:ve onu kıldık} içindeki “onu” için en yakın eril tekil öncül Kitap'tır; sonraki yol gösterme işlevi de bu okumayı güçlendirir. {ar:مُوسَى, tr:Mūsā, gloss:Musa} biçimce mümkün bir gönderge olarak kalır, zamir bu olasılığı kapatmaz. Fiilin söz ailesindeki mevcut bir varlığı yeni bir duruma getirme kullanımı, verilen Kitap'ı topluluk için işleyen bir yöne dönüştürür.

Bu ikinci fiilin sonuç tümleci olan {ar:هُدًۭى, tr:hudan, gloss:yol gösterme}, belirsiz bir mastardır: {ar:وَجَعَلْنَٰهُ, tr:wa-jaʿalnāhu, gloss:ve onu kıldık} eyleminin işlevini verir; önceki {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} fiilinin ikinci nesnesi değildir. Rehberliği özel bir unvan ya da sabit sınıftan çok Kitap'a verilmiş bir görev gibi duyurur. Olağan anlamı doğru yönü, yolu ya da gerçeği göstermektir; Kitap'ın işi alıcılarını yöneltir. Aynı söz ailesinin hedef, izlenen doğrultu ve tutum anlamları bu işlevi adlandırılmış toplulukla buluşturunca, yön tekrar tekrar yaşanabilecek bir gidiş ya da yönteme doğru genişler. Bu genişleme rehberliğin yerini almaz; verilen yönün topluluğun yaşayacağı yola dönüşmesini düşündürür.

Yönün kime yarar sağladığını {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} içindeki yarar bildiren bağ kurar. En yakın {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevine bağlanabilir; verişe ya da yapma eylemine ilişmesi de mümkün olduğundan yararlanıcının kapsamı bunlardan birine daralmaz. Uzun ünlüler ve tamlama kuruluşu {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} ile {ar:إِسْرَٰٓءِيلَ, tr:Isrāʾīl, gloss:İsrail} adını tek bir ses ve anlam öbeğinde birleştirir. Tamlama içindeki ilk öğe “çocuklar, torunlar, soyundan gelenler” anlamını taşır; İsrail bu yapıyı tamamlayan özel addır, serbest bir seslenme değildir. Topluluk adı rehberlikten sonra, buyruğa geçmeden önce yararlanıcının kimliğini sabitler. Bildirilen kıraat farklılıkları ses çizgisini değiştirse de özel adı ve göndergeyi değiştirmez.

Topluluk adının olağan soy anlamı korunurken, {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} tamlamasının ilk öğesinin söz ailesindeki parçaları birleştirip ayakta duran yapı imgesi topluluğu biçimlenmiş bir sosyal bütün olarak düşündürür. {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} ile {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} bu adlandırılmış gruba yönelince, topluluk yön alan bir bütün gibi görünür. Soy bağı aynı zamanda kaynaktan türeyerek ya da yetişerek süren kuşakları çağırır; bu iki katkı verilen yönü hem adlandırılmış gruba hem de adlandırmanın taşıdığı, nesiller boyunca sürebilecek ilişkiye bağlar. Yapı imgesi topluluk adıyla sınırlıdır ve her üyenin davranışı hakkında hüküm vermez.

Bu gruba ulaşan {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}, söz ailesinin hem harfleri düzenleyip yazı hâline getirme eylemini hem de bunun ürünü olan yazılı metni kapsar. Burada verilen ve rehberlik işlevi kazanan nesne, belirli bir nüsha ya da maddi tarih varsaymaksızın yazılı vahiy metni olarak kalır. Aynı söz ailesindeki parçaları birleştirip bağlı bütün kurma kullanımı ise {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevinin {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} topluluğuna yönelmesiyle canlanır: yazılı metin, grubun uygulayacağı yönü bir arada tutan bir düzen gibi duyulur. Bu birleştirme imgesi ortak yönelişin nasıl taşındığını görünür kılar; Kitap'ın yazılı metin anlamını değiştirmez.

## Buyruğun Eşiği

Topluluğun adından sonra gelen {ar:أَلَّا, tr:allā, gloss:ki ... -mesin} biçimi, olumsuz buyruğa geçerken duyulur bir eşik kurar. Bağlayan unsurla olumsuzluğu birlikte taşır ve sonraki {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} fiilini sonundaki {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} rolüne kadar yönetir; bağımlı içeriği serbest yeni bir cümleye açmaz. Kuruluş, rehberliğin içeriği ya da amacı olarak “edinmeme”yi de, topluluğa yöneltilmiş gerçek bir “edinmeyin” yasağını da taşır. İki kuvvet birlikte kalır: verilmiş ve işlev kazanmış yönün karşısına tamamlanmış değil, önü alınan bir insan tercihi çıkar.

Son buyruğun temasında {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} söz ailesinin bir başka kullanımı belirir: yapılması gereken işi bağlayıcı kılmak ve yazılı kaydı yürürlükte tutmak. Bu anlamı son {ar:أَلَّا, tr:allā, gloss:ki ... -mesin}, {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} ve {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} birlikte etkinleştirir. Bu temas rehberliğe bağlayıcı bir ağırlık katar; Kitap yazılı metin olarak kalır, bu bağlantı ayrı bir hüküm ya da hukuk kararı getirmez.

{ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} bir şeyi yalnızca tutmak değil, kendisi için benimseyip dayanak olarak yerleştirmektir. Form VIII'deki bu biçim, {ar:أَلَّا, tr:allā, gloss:ki ... -mesin} sonrasındaki mansup muzari olarak henüz gerçekleşmemiş, yasaklanan olası bir seçimi gösterir. Tamamlanmış {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} ve {ar:وَجَعَلْنَٰهُ, tr:wa-jaʿalnāhu, gloss:ve onu kıldık} eylemlerine karşılık insanın yapması engellenen eylem öne çıkar; fiildeki ikizleşme de işitilir ağırlığı bu benimseme üzerine koyar. Yüzeydeki ikinci çoğul sesleniş topluluğu muhatap alır, aktarılan üçüncü çoğul okuma ise onlar hakkında söyleyişi canlı bir olasılık olarak bırakır. Benimsenecek kişinin kendisi söylenmez; sona yerleşen {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} kimin değil, hangi rolün edinilmesinin yasaklandığını belirginleştirir.

Bu benimsemenin dışlama yönünü ayrı edat {ar:مِن, tr:min, gloss:-den} ile onun yönettiği {ar:دُونِى, tr:dūnī, gloss:benden başka} kurar. Bu edat burada bütünden parça seçmez; edinme eyleminin dışlama ilişkisini bildirir. İyelikli ilişkisel ad yalın bir zarf değildir; birinci tekil eki “Ben”i doğrudan ilahi konuşana bağlar ve ifade edinme eylemini niteler. Edatın burun ünsüzü sonraki ada sesçe bağlanırken sözcükler ayrı kalır. Sözdizimi önce “Benden başka” diye bir dış alan açar, sonra son {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} ile o alandaki rolü adlandırır.

“Benden başka” temel anlamı korunurken, {ar:دُونِى, tr:dūnī, gloss:benden başka} söz ailesindeki yakınlık ve yaklaşma kullanımları {ar:مِن, tr:min, gloss:-den} ile son {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} rolüyle karşılaşınca ifadeye mekânsal bir yakınlık katar. Aynı ailede aşağıda ya da dışarıda kalma, düzende geride bulunma ve hedeflenen sona erişememe yönleri de vardır. Birinci kişi eki, dışlama edatı ve yetki taşıyan vekâlet rolü bu kullanımları yerel bir hiyerarşik gölgeye çevirir: rakip merci ilahi referans noktasının dışında, hatta altında duyulabilir. Bu basınç bu cümledeki “Benden başka” ilişkisini genişletir; bu adın her kullanımına aşağılık anlamı yüklemez.

Sondaki belirsiz tekil {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil}, belirli bir kişiyi değil vekâlet rolünü geneller. Söz ailesi bir işin sorumluluğunu başkasına bırakmayı ve o kişinin devreden adına yetkili temsilci olarak hareket etmesini kapsar; üstlenilen işte koruma ve güvence beklentisi de bulunur. Benimseme fiiliyle ve “Benden başka” dışlamasıyla buluşunca rol, nihai yetki devri ve rakip vekâlet olarak belirginleşir. Bu cümledeki bağlantı gündelik yardımın bütün biçimlerine değil, nihai yetki devri ve rakip vekâlete odaklanır. {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} güvenme fiili değil, yetki ve güven devredilen kişi ya da rolü bildiren isimdir. Onu doğrudan nesne sayan çözümlemede de edinilen kişinin rolünü bildiren hâl çözümlemesinde de rol açık, üstlenecek kişi belirsiz kalır.

Aynı söz ailesinin kişinin bir işte yetersiz kalıp başkasına dayanmasını anlatan kullanımı da bu eylem dizisine katılır. Verilmiş {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ile {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} tarafından anlatılan kendine vekil edinme ve {ar:مِن, tr:min, gloss:-den} {ar:دُونِى, tr:dūnī, gloss:benden başka} diye dışlama yan yana gelince, sunulan yönü izlemek yerine işi başka bir mercie bırakma ihtimali karşı hareket olarak görünür. Buradaki gerilim rehberlik ile devredilmiş temsil arasındadır; olağan güveni ya da yardımlaşmayı mahkûm etmez. Bu ayet içi zincir yetkinin kaynağından sınırına uzanır: {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} verişi kurar, {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} ile anılan topluluğa yön kazandırır, son yerde dışlanan {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} ise yetki sınırını belirginleştirir. {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ile {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} arasındaki bu yerel kadans, 17:2'yi verilen yön ile başkasına bırakılan temsil yetkisini karşı karşıya getirerek kapatır; buradaki işlev ayrımı bu bağlantıyla sınırlıdır ve iki sözü eş anlamlı ya da mutlak karşıt kılmaz.

## Duyulan Yol

Bu ayrı sözlük imgesi, rehberlik yönünü önde izlenen bir yol, vekil edinmeyi ise geride kalıp başkasının adımına dayanma olarak karşı karşıya getirir. {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} biçiminin olağan “verdik” anlamı korunur; bağlı olduğu söz ailesindeki işlek ya da yürünmüş ana yol kullanımı ayrı bir çağrışım açar. {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ailesinin önde bulunan parça ve önden ilerleyerek yol gösteren kılavuz kullanımları yönü yolun başına taşır. Buna karşılık {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} ailesindeki eski ve seyrek bir kullanım kötü yürüyen hayvanı anlatır: hayvan geride kalır ya da kendi adımıyla ilerlemek yerine yanındakinin adımına dayanır. {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} ile işleyen vekil edinme eylemi bu ikinci görüntüyü, öndeki kılavuzun ters yönünde duran yasaklı bir yaslanma olarak harekete geçirir. Bu sözlük imgesinde veriş “yürünmüş yol”, vekil de harfi anlamıyla “hayvan” olmaz; armağan, yön gösterme ve vekâlet okumaları korunur. İmge, 17:1'in gerçek gece yolculuğundan ayrı bir temas olarak kalır.

Hareketi gerçekten sahneye koyan yakın bağlam 17:1'dir. Odaktaki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} yön ve hedefi bildirirken, gece yürüyüşü, gösterme ve görünür işaretler güzergâhın hareket sırasında nasıl izlenebileceğini sağlar. {ar:أَسْرَىٰ بِعَبْدِهِۦ لَيْلًا, tr:asrā bi-ʿabdihi laylan, gloss:kulunu geceleyin yürüttü} gerçek gece yolculuğunu, {ar:لِنُرِيَهُۥ, tr:linuriyahu, gloss:ona gösterelim diye} görünür kılmayı, {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:ayetlerimiz} ise okunabilir alametleri getirir (17:1). Bu temas Musa'ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}'ın hidayetini yalnızca varılacak doğru yönün adı değil, hareket boyunca algılanıp izlenebilen bir açıklık gibi duyurur. Gece yolculuğu ilahi kudreti de vurgulayabilir; {ar:ٱلسَّمِيعُ, tr:al-samīʿ, gloss:işiten} ve {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:gören} Allah'ın nitelikleridir. Bu yakınlık yolcunun işbirliğine dayanmaz; hareket sırasında görünen alametlerin rehberliği algılanabilir kılmasına dayanır.

## Kuşaklar ve Tarih

Güzergâh imgesinden ayrı olarak, 17:3'teki {ar:ذُرِّيَّةَ, tr:dhurriyyata, gloss:soy} sözü Nuh'la birlikte taşınanların ardından gelen kuşakları adlandırır. Musa'ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} ve onun {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işleviyle bu sözün yakınlığı, 17:2'deki {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} adının olağan soy anlamını nesillerin açıkça anıldığı başka bir hitapla somutlaştırır. Buradaki kuşaklar 17:3'ün kendi hitabının konusu olan Nuh'la taşınanların soyudur; bu paralellik onları İsrailoğullarıyla özdeşleştirmez ya da Tevrat aktarımı kurmaz.

17:3'teki {ar:حَمَلْنَا مَعَ نُوحٍ, tr:ḥamalnā maʿa Nūḥin, gloss:Nuh'la birlikte taşıdık} fiziksel taşımayı söyler; bu hareket soyun sürmesini sağlayan zemindir (17:3). Aynı taşıma sözü yük ve emanet yönünü de açınca, Musa'nın aldığı {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}'ı kuşaklar boyunca koruyup aktarma sorumluluğu bir benzetme olarak belirir. Böylece armağanı alan {ar:مُوسَى, tr:Mūsā, gloss:Musa} ile onu kuşaklar arasında taşıyan soy ayrı konumlarda kalır; insan soyu, {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} rolünün taşıdığı nihai güvenceyi üstlenmez. Nuh'a ait tekil {ar:عَبْدًا, tr:ʿabdan, gloss:kul} ve {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} nitelemeleri de bu ayrımı derinleştirir: kulluk ve nimeti tanıyıp verene şükür, taşıyıcının hizmet ve minnettarlığını düşündürür; sonraki kuşaklara aktarılmış bir sıfat ya da soyun koruyuculuğu iddiası kurmaz.

Kitap'ın topluluğa yön vermesi, başka bir yakın bağlamda tarihin nasıl okunacağı sorusuna döner. 17:4'te {ar:فِي ٱلْكِتَٰبِ, tr:fī al-kitābi, gloss:Kitap'ta} sözüne {ar:وَقَضَيْنَآ, tr:wa-qadaynā, gloss:karara bağladık} eşlik eder; iki bozulma {ar:لَتُفْسِدُنَّ, tr:la-tufsidunna, gloss:bozgunculuk edeceksiniz} ve {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} ile sayılır (17:4). Ardından kuvvetli görevliler {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik} ile gönderilir, üstünlük de {ar:رَدَدْنَا, tr:radadnā, gloss:geri verdik} ile geri verilir (17:5, 17:6). {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:dönerseniz biz de döneriz} koşulu insanın dönüşünü ilahi karşılığın eşiğine koyar (17:8). Olumsuz yönde kapanış ihtimali aynı ayetin {ar:حَصِيرًا, tr:ḥaṣīran, gloss:kuşatıcı} sözüyle kuşatan bir sınıra varır (17:8). Böylece {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:Kitap'ta} yalnız hedefi gösteren metin değil, sapma, karşılık ve dönüşün tarihte izlenebildiği ölçü gibi duyulur; {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} tekrarlanan sonuçları okumaya ve dönüş olanağını görmeye yardım eder. Bu sıra dönüş imkânını açık tutar, davranışı mekanik biçimde sabitlemez. Gönderilen yakın görevliler işi icra düzeyinde yürütür; son {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} rolünün taşıdığı nihai güvenceyi üstlenmez.

Bu tarihsel ölçüden dikkat 17:9'da rehberliğin sürdüğü hayata geçer. {ar:ٱلْقُرْءَانَ, tr:al-qurʾān, gloss:Kur'an} insanları {ar:يَهْدِي, tr:yahdī, gloss:yol gösterir} “en doğru olana” {ar:لِلَّتِي هِيَ أَقْوَمُ, tr:li-llatī hiya aqwamu, gloss:en doğru olana} yöneltir; {ar:لِلْمُؤْمِنِينَ, tr:li-l-muʾminīna, gloss:iman edenlere} müjde ve {ar:يَعْمَلُونَ ٱلصَّٰلِحَٰتِ, tr:yaʿmalūna al-ṣāliḥāti, gloss:iyi işler yaparlar} sözü de bu yönelişin davranışta sürmesini gösterir (17:9). Daha geniş muhatap kitlesine yönelen bu rehberlik, hidayeti bir kitaba verilmiş nitelikten okuma, içten benimseme ve eylemde süren bir ilişkiye taşır. Musa'ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} ile bu ayette anılan Kur'an ayrı metinler ve tarihsel uğraklardır; yakınlık, her birinin sürdürdüğü {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevinde kurulur. Kitap adı yazma eylemini değil yazılı ürünü adlandırır; Kur'an'ın tilaveti bu ürünü etkin metin olarak duyurur. Böylece iki metin arasında özdeşlik değil, süren rehberlik işlevi ve yazılı metin alanında bir yakınlık kurulur.

Rehberliğin neye yön vereceği sorusu, 17:11'de insanın dileğine döner. {ar:وَيَدْعُ ٱلْإِنسَٰنُ, tr:wa-yadʿu al-insānu, gloss:insan dua eder} aynı çağrıda hem {ar:بِٱلشَّرِّ, tr:bi-l-sharri, gloss:kötülükle} hem {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilikle} birleşir; kapanıştaki {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} nitelemesi aceleciliği açık eder (17:11). Ayetin doğrudan eleştirisi zarar ve iyilik için aceleyle istemektir. Odaktaki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevini ve vekil edinme seçimini bu dileğin yanına koymak, rehberliğin henüz yol ya da dayanak seçilmeden istenen sonucu sınayabileceği ihtiyatlı bir okuma açar. {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} ve {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} arzudan güven kaynağına geçişte düşünme payını görünür kılar. Bu, 17:11'in açık acele dua eleştirisine eklenen ihtiyatlı bir katmandır; ayet odak sözcüklerini kendisi açıklamadığından doğrudan okuma da geçerlidir.

## Kişinin Karşılığı

İsteğin ve yönelişin kişiye ne bıraktığı, kamusal ölçüden kişinin önüne açılan kayda geçişte belirginleşir. Musa'ya verilmiş {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}'ın {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevi ortak yönü bildirirken, ayrıntıları ayıran {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:ayrıntısıyla açıkladık} ölçüyü görünür kılar (17:12). Kişisel kayıt {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} sözüyle öznesine iliştirilir; {ar:كِتَٰبًا, tr:kitāban, gloss:yazılı kayıt} olarak önüne konup {ar:مَنشُورًا, tr:manshūran, gloss:açılmış} hâle gelir (17:13). Bu, Musa'ya verilmiş Kitap'la aynı işlevde bir metin değil, kişinin kendi hesabını göreceği kayıttır. İki metin arasındaki bağ yazı ve metin alanıyla sınırlı kalır.

Kayıt açıldıktan sonra {ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} buyruğu kişiyi kendi kitabının okuru yapar; {ar:كَفَىٰ بِنَفْسِكَ, tr:kafā bi-nafsika, gloss:kişinin kendisi yeter} ve {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} sözü yedek bir hesapçıya duyulan ihtiyacı kaldırır (17:14). Okuma böylece başkasının kendisi adına vereceği bir karara değil, kişinin kendi hesabıyla karşılaşmasına bağlanır. Kitabın açılmış olmasıyla okurun bizzat kendisi olması, sorumluluğun kime ait olduğunu birlikte belirginleştirir.

Bu kişisel okumanın sınırı {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:kimse başkasının yükünü taşımaz} ilkesiyle konur; aynı ayetteki {ar:رَسُولًا, tr:rasūlan, gloss:elçi} sonuçtan önce bildirimi hatırlatır (17:15). {ar:أَمَرْنَا, tr:amarnā, gloss:buyurduk} emri ile {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawlu, gloss:hüküm kesinleşti} sonucu davranışla hükmü karşı karşıya getirir (17:16). {ar:خَبِيرًا, tr:khabīran, gloss:her şeyden haberdar} oluş da yargının görünür kayıttan öte haberin ve iç gerçekliğin bilgisine dayandığını gösterir (17:17). Burada başka işi üstlenebilen {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil}, kişinin ahlaki yükünü üzerine alamaz; devredilemezlik açıkça yük için söylenir, vekâletin gündelik işlerdeki bütün biçimleri için değil.

Kişinin verdiği sonucun başkasına aktarılamaması, ayrı bir bağlamda daha doğrudan söylenir. Doğru yolu izleyenin yararı kendisine, sapmanın zararı da sapana döner; elçi insanlar üzerinde vekil değildir (10:108). Bu paralellik odaktaki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme}nin kişisel karşılığa uzanmasını, {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil}in ise başkasının verdiği cevabı güvenceye alamamasını düşündürür. Böylece 17:2'deki rehberliğe verilecek cevap başkasına havale edilmez. Bu alıntı olmayan, bağlamsal ve nitelikli paralellik kişisel cevabın devredilemezliğini aydınlatır; kişisel kitap ya da okunabilir sicil imgesi bu bağlantının parçası değildir.

## Bağışın Sınırı

Kişinin cevabından sonra yakın ve sonraki ufuk farklı yönelişlerle belirir: {ar:يُرِيدُ, tr:yurīdu, gloss:ister} yakın dünya olan {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilata, gloss:yakın dünya}yı ister, {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:çabuklaştırdık} bu ufku hızlandırır (17:18); {ar:ٱلْءَاخِرَةَ, tr:al-ākhirata, gloss:sonraki hayat} için {ar:سَعْيَهَا, tr:saʿyahā, gloss:ona yönelik çaba} ise bilinçli yürüyüşü gösterir (17:19). Ardından {ar:نُّمِدُّ هَٰٓؤُلَاءِ وَهَٰٓؤُلَاءِ, tr:numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:her iki gruba da uzatırız} imkânı iki gruba da uzatıp bağışın erişimini gösterir; {ar:عَطَاءُ رَبِّكَ, tr:ʿaṭāʾu rabbika, gloss:Rabbinin bağışı} verişi adlandırır, {ar:مَحْظُورًا, tr:maḥẓūran, gloss:esirgenmiş} ise nimetin kısıtlanmadığını söyler (17:20). {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün kıldık} ve {ar:دَرَجَاتٍ, tr:darajātin, gloss:dereceler} kademeli farkı görünür kılar (17:21). Bu ayrıntılar {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ışığında okunduğunda, iki gruba da ulaşan maddi imkân tek başına gidişin doğruluğunu göstermez. Odaktaki {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} armağanı vermek ve ulaştırmak olarak kalır; bolluk ne bir yolun ne de {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} ile kurulmuş vekâletin onayıdır. Pasajın açık vurgusu ilahi cömertliktir; nimet aldatıcı diye nitelenmez ve ayetler vekilden söz etmez.

## Dayanağın Yönü

Odaktaki {ar:تَتَّخِذُوا۟, tr:tattakhidhū, gloss:edinmeyin} ve {ar:مِن, tr:min, gloss:-den} {ar:دُونِى, tr:dūnī, gloss:benden başka} kuruluşu, başka bir ilahı Allah'ın yanında bir konuma yerleştirme yasağıyla yapısal bir yankı kazanır (17:22). Oradaki {ar:تَجْعَلْ, tr:tajʿal, gloss:yerleştir} ile {ar:إِلَٰهًا ءَاخَرَ, tr:ilāhan ākhar, gloss:başka bir ilah} kurma eylemini {ar:فَتَقْعُدَ مَذْمُومًا مَّخْذُولًا, tr:fa-taqʿuda madhmūman makhdhūlan, gloss:kınanmış ve yüzüstü bırakılmış kal} sonucu, eylemsiz kalma, kınanma ve desteksiz bırakılma izler (17:22). Bu yapısal yankı, pratik temsilci edinme yasağını nihai güvenin yönüyle ilişkilendirir; ortak nokta rakip bir merciyi konuma yerleştirmektir. Bağlantının alanı sınırlıdır: 17:2 vekâlet ve dayanmayı, 17:22 ibadeti hedefler; bu nedenle 17:22'deki sözler {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} rolünü tanımlamaz.

Yakın bağlamın ötesindeki uyarılar, rakip dayanakların üstlenebileceği işleri ayrı ayrı sınar. Başka ilah edinme kınanma ve terk edilmeyle ilişkilendirilir (17:39); çağrılan varlıkların sıkıntıyı gideremediği ya da başka yere aktaramadığı bildirilir (17:56). Aynı varlıklar kendileri Rablerine yakınlık arar, rahmet umar ve azaptan korkar (17:57). Tehlike anında işi üstlenecek bir vekil bulunup bulunamayacağı sorulur (17:68). Allah'ın mülkünde ortağı ve zaaftan ötürü koruyucu bir dosta ihtiyacı bulunmadığı da bildirilir (17:111). Son ayetteki koruyucu dost sözü, odaktaki {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} ile aynı kelime ya da kök değildir. Birlikte bu sahneler bağımsız koruma ve güvence kapasitesini sınar; 17:57 çağrılan varlıkların kendilerinin rahmete muhtaç olduğunu gösterir. Özneler her sahnede ayrı kalır ve bu bağlamsal yankı tüm varlıkları vekil rolüne yerleştirmez.

Güvencenin kaynağı sorusu vahye döner: Allah dilerse vahyi ortadan kaldırabilir ve O'na karşı hiçbir vekil bulunamaz (17:86). Odaktaki {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} işin üstlenilmesi ve korunması beklentisini taşır; 17:86'da hiçbir aracı vahyi verenden bağımsız biçimde güvenceye alamaz. Böylece {ar:مُوسَى, tr:Mūsā, gloss:Musa}'ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap}'ın {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} işlevi, kaynağının elinde tuttuğu bir armağan olarak duyulur: verilmişliği sürer, güvence verenden başkasına devredilmez. 17:86 daha sonraki elçiye indirilen vahyi konu alır; bu paralellik Musa'nın Kitabı'nı tanımlamaz ya da 17:2'den geleceğe dair haber çıkarmaz, iki ayet arasındaki kaynak-güvence temasını aydınlatır. Bu temas biçim çözümlemesine değil, bağlamsal paralelliğe dayanan nitelikli bir çıkarım olarak kalır.

Bu kaynak ilişkisine olumlu karşılık veren iki ayrı bağlam vardır: 14:12'de kendilerine yollar gösterilmişken Allah'a güvenme sorulur, 73:9'da tek ilah olarak anılan Allah'ı vekil edinme çağrısı gelir. İlk bağ, {ar:هُدًۭى, tr:hudan, gloss:yol gösterme}nin açıkladığı doğru yön ve izlenecek doğrultuyu Allah'a güvenmeyle ilişkilendirir; ikincisi {ar:وَكِيلًا, tr:wakīlan, gloss:vekil} rolünün üstlenme ve koruma beklentisini aynı kaynağa bağlar. Birlikte okunduklarında yasağın olumlu karşılığı, rehberliği verene dayanmak olarak duyulur. Bu, alıntı değil bağlamsal paralelliktir; dış ayetlerin hedef biçimleri çözümlenmediğinden çıkarım nitelikli kalır, belirsiz tekil vekil biçimi de karşılıklı bağımlılık kurmaz. Paralellik odaktaki {ar:وَجَعَلْنَٰهُ, tr:wa-jaʿalnāhu, gloss:ve onu kıldık} içindeki “onu” zamirini çözmez: en yakın öncül {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} olarak kalır, {ar:مُوسَى, tr:Mūsā, gloss:Musa} ise biçimce mümkündür. Dış temas Kitap'ı yazılı metin alanında tutar; birleştirici benzetme, ayetin {ar:لِّبَنِىٓ, tr:li-banī, gloss:İsrailoğullarına} ile adlandırdığı toplulukla rehberlik ilişkisine dayanan ayrı bir yerel okumadır.

Gösterilen yönün alıcıdan nasıl bir karşılık beklediği, bir Kitap isteyenlerin önüne gelmiş kanıt, hidayet ve rahmetin konduğu, ardından işaretlerin yalanlandığı başka bir bağlamda belirir (6:157). Buradaki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} hem gösterilen doğrultuyu hem de sunulduğunda kabul ya da retle karşılanan rehberliği duyurur; alıcının yönelimi tutulan yolu ve sonucu birlikte görünür kılar. Böylece bu temas bir tanılama haritası değil, sunulan yönün alıcıda karşılık bulmasıdır. 6:157'de istenen Kitap ve onun muhatapları odaktakilerden ayrıdır; 14:12 ise odak ayetin alıntısı değil, başka bir bağlamdır. Dış ayetlerin biçimleri çözümlenmediğinden bu okuma nitelikli bir paralellik olarak kalır.

## Duada İstenen Yön

Alıcının cevabı Fatiha'da iki ayrı istekle eyleme dönüşür. {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa iyyāka nastaʿīn, gloss:Sana kulluk ve yardım} ibadeti ve istenen yardımı yalnız Allah'a yöneltir (1:5). Bu, başka bir dayanak edinmeme buyruğuyla uyumlu eylem benzerliğidir; {ar:وَكِيلًۭا, tr:wakīlan, gloss:vekil} sözcüğünün karşılığı değildir.

Ardından {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:dosdoğru yola ilet} duasında topluluk kendisi için dosdoğru yola iletilmeyi ister (1:6). Bu emir, {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ile aynı yönelme kökünden gelir ve 17:2'de Musa'nın topluluğuna verilmiş yönü birlikte talep eder. Fatiha'da bu isteğin öznesi birlikte yön arayan topluluktur; Musa, Kitap ve İsrailoğulları bu ayette anılmaz. Böylece bağ, metinsel bir anının aktarımında değil, topluca talep edilen rehberlik ilişkisinde kurulur.

</source_prose>
