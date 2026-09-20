# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:7**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.middle.claims.json`

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
- Refer to source paragraphs as `17:7 ¶N`.

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

`(17:7 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:7",
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
        "citation": "(17:7 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_7/17_7.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_7/17_7.middle.claims.json \
  --ayah-ref 17:7
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_7/17_7.prose.editorial.tr.md`

<source_prose>
## Eylem ve Karşılık

Âyet, iki açık şartı yan yana kurar: {ar:إِنْ أَحْسَنتُمْ, tr:in aḥsantum, gloss:iyilik ederseniz} iyilik ederseniz, cevaptaki {ar:أَحْسَنتُمْ, tr:aḥsantum, gloss:iyilik ettiniz} aynı eylemi yineler ve yararı onu yapanlara bağlar. {ar:وَإِنْ أَسَأْتُمْ, tr:wa-in asāʾtum, gloss:ve kötülük ederseniz} ise karşı ihtimali aynı koşul düzenine yerleştirir. Bu paralel kuruluş iki ayrı sonucu aynı açık koşul çerçevesinde karşılaştırır; hangi yolun seçileceğini önceden bildirmez.

İyilik cevabındaki {ar:أَحْسَنتُمْ, tr:aḥsantum, gloss:iyilik ettiniz} IV. bâbın ikinci çoğul geçmiş biçimidir: muhataplar iyiliği etkin biçimde yapar, güzelleştirir. Fiilin tekrarı yapılan işi yararın kendisi hâline getirirken {ar:لِأَنفُسِكُمْ, tr:li-anfusikum, gloss:kendiniz için} içindeki lâm bu yararı yapanlara yöneltir; dışarıdan verilmiş ayrı bir ödül adlandırılmaz. Karşıdaki {ar:أَسَأْتُمْ, tr:asāʾtum, gloss:kötülük ettiniz} de IV. bâbın etkin eylemidir: zarar edilgin bir kazaya değil, muhatapların yaptığı işe bağlanır.

Bu yönelişin taşıyıcısı {ar:لِأَنفُسِكُمْ, tr:li-anfusikum, gloss:kendiniz için} içindeki {ar:أَنفُس, tr:anfus, gloss:nefisler} çoğul adıdır; {ar:كُمْ, tr:-kum, gloss:sizin} ikinci çoğul iyelik eki, şart fiillerindeki {ar:تُمْ, tr:-tum, gloss:siz} de aynı muhatap grubunu korur. Nefis burada kişilerin kendilerini ve bütün öz varlıklarını adlandırır; böylece yapanlar ile yararı görenler aynı kişiler olarak kalır. İyilik ve kötülüğün yapanın kendisi için ya da aleyhine olması bu kendine dönüşü pekiştirir (45:15); bir topluluğun içindekiler değiştiğinde hâlinin de değişmesi, kendiliği değişimin öznesi olarak duyurur (13:11). Bu içsel yankı, nefsi düşünce ya da niyet gibi dar bir zihinsel içerikten çok, yararın döndüğü kişinin bütün öz varlığı ve iç değişiminin öznesi olarak duyurur.

Zarar cevabındaki {ar:فَلَهَا, tr:fa-lahā, gloss:öyleyse sonuç onundur} önceki lâmı daha kısa ve ani bir dönüşle yeniden duyurur. Dişil zamirin gönderimi yapılan kötülük ile muhatapların kendileri arasında açık kaldığından, bu kısa cevap sonucu onların ortak ahlaki alanına döndürülebilir bırakır. Biçim farkı geri dönüşü keskinleştirir; zamirin gönderimini seçmediği gibi eylem-sonuç ilişkisini kaçınılmaz yazgı ya da ruhun mahiyeti hakkında bir hüküm olarak da sabitlemez.

{ar:لِأَنفُسِكُمْ, tr:li-anfusikum, gloss:kendiniz için} yönelişinin daha geniş bir yankısında, kötü azabın Firavun’un çevresindeki kötülük tasarlayanları kuşatması zararın faili çevresini saran bir sıkıntıya dönüşmesini gösterir (40:45). Âhireti amaç edinip onun için çabalayan kişinin karşılık bulması ise aynı eylem-fail bağını sürdürülen çabaya ve daha uzak sorumluluğa taşır (17:19). Bu iki örnek odağın kişilerini ya da olaylarını teşhis etmez; biri kuşatan sıkıntıyı, öteki çabanın kişisel karşılığını ekleyerek kendine dönüşün ufkunu genişletir.

Kendine yarar sağlayan iyilik, rehberliğin eyleme dönüşmesi olarak da okunabilir. Odaktaki {ar:أَحْسَنتُمْ, tr:aḥsantum, gloss:iyilik ettiniz} IV. bâbın ikinci çoğul geçmiş biçimidir ve iyilikle güzelleştirmeyi muhatapların etkin işi olarak kurar. Kur’an insanları en doğru ve dengeli olana yöneltir; ardından yapılan işler ve sağlam iyilikler büyük bir karşılıkla buluşur (17:9). Bu sırada {ar:يَهْدِي, tr:yahdī, gloss:yol gösterir} yön verir, {ar:أَقْوَمُ, tr:aqwamu, gloss:en doğru ve dengeli} hedefi belirler; insanlar {ar:يَعْمَلُونَ, tr:yaʿmalūna, gloss:iş yaparlar} ve {ar:الصَّالِحَاتِ, tr:aṣ-ṣāliḥāt, gloss:iyi ve sağlam işler} ortaya koyar, sonra {ar:أَجْرًا كَبِيرًا, tr:ajran kabīran, gloss:büyük bir karşılık} alırlar (17:9). Rehberlik yönü belirler, çalışma onu eyleme taşır, sağlam işler de bozulmaya karşı kurulan ürünü ve büyük karşılık emeğin sonucunu gösterir. Bu akış iyiliği düzen kuran bir eylem olarak genişletir. Onarım, bu 17:9 bağlantısından çıkarılan yorumdur; ayet komşu bir ödül önermesi olarak da okunabildiğinden onarım her iyi davranışın sözlük anlamı yapılmaz.

{ar:لِأَنفُسِكُمْ, tr:li-anfusikum, gloss:kendiniz için} ile kurulan kişisel dönüş, 17:13’te amelin kişinin boynuna bağlanıp açılmış bir kitap olarak bulunmasıyla kayda dönüşür: {ar:أَلْزَمْنَاهُ طَائِرَهُ فِي عُنُقِهِ, tr:alzamnāhu ṭāʾirahu fī ʿunuqihi, gloss:amelini boynuna bağladık} (17:13). Bağlama eylemi kaydın kişiye aitliğini gösterir; kitabın açılmış bulunması onu görünür ve okunabilir kılar. Kişiye kendi kitabını okuması söylenir; {ar:حَسِيبًا, tr:ḥasīban, gloss:hesap gören} hesap görmeyi, {ar:اقْرَأْ كِتَابَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} emri ise bu kaydın incelenmesini belirginleştirir. Kişinin kendi nefsinin hesap için yeterli oluşu aynı sorumluluğu ona sabitler (17:14). Ardından hiç kimsenin başkasının yükünü taşımadığı bildirilir (17:15): {ar:لَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:lā taziru wāziratun wizra ukhrā, gloss:hiç kimse başkasının yükünü taşımaz} (17:15). Defter ve hesap odağın sözlük anlamı değil, yakın ayetlerin kurduğu somut sorumluluk görüntüsüdür; bu görüntü kişisel yarar-zarar önermesini değiştirmek yerine onu kaydın sahibi, okuru ve yükünü taşıyan kişinin aynı oluşuna doğru genişletir (17:13, 17:14, 17:15).

## Vaat ve Vakit

Zarar cevabındaki {ar:فَلَهَا, tr:fa-lahā, gloss:öyleyse sonuç onundur} ilk fâsından sonra gelen {ar:فَإِذَا, tr:fa-idhā, gloss:derken ne zaman} ikinci fâ, dikkati koşullu sonuçtan zaman dizisine çevirir. İlk iki {ar:إِنْ, tr:in, gloss:eğer} açık bir ihtimali kurarken {ar:إِذَا, tr:idhā, gloss:-dığında / ne zaman} beklenen bir eşiğe açılır. Tamamlanmış biçimdeki {ar:جَاءَ, tr:jāʾa, gloss:geldi} fiilinin öznesi {ar:وَعْدُ, tr:waʿdu, gloss:vaat}tır: vaat, biri tarafından getirilen nesne gibi değil, vakti gelince sahneye varan olay gibi kurulur. Bu geçiş bir takvim günü ya da belirli bir tarihsel fail vermez.

{ar:وَعْدُ الْآخِرَةِ, tr:waʿdu l-ākhira, gloss:sonraki vaat} yerel sırada 17:5’teki ilk vaatten sonra gelen vaadi belirtir (17:5). Buradaki {ar:الْآخِرَةِ, tr:al-ākhira, gloss:sonraki olan}, {ar:أَوَّلَ مَرَّةٍ, tr:awwala marratin, gloss:ilk sefer} karşısında yerel dizinin sonraki ya da öteki vaadini belirtir; âhiret ufku ise daha geniş bağlamlardan doğar. Yüzlere yönelen {ar:لِيَسُوءُوا, tr:li-yasūʾū, gloss:yüzlere zarar vermeleri için} ve {ar:وَلِيُتَبِّرُوا, tr:wa-li-yutabbirū, gloss:ve yıkmaları için} amaçları bu gelişe gözdağı tonu katar; bu tehdit rengi 17:7’deki amaç dizisine aittir, “vaat” sözcüğünün genel anlamına değil (17:7). Yerel anlatıda ikinci tarihsel olay ve ilk girişten sonraki tekrar böylece bir arada duyulur.

Her topluluğun vadesinin öne alınamayacağını ya da ertelenemeyeceğini söyleyen ayet, vaadin gelişini belirlenmiş bir eşik gibi duymaya imkân verir (7:34). Firavun’un halkı sürme girişiminin boğulmayla tersine dönmesi bu eşiğe tarihsel bir dönüş örneği katar (17:103); aynı vaat ifadesinin toplu getirilmeden önce yinelenmesi ise dönüşün bir araya gelişle tamamlanmasını gösterir (17:104). Bu bağlantı ikinci vaadi tayin edilmiş bir vade gibi genişletir, kesin gününü belirtmez; yerel sıradaki tarihsel yeri korunur.

Aynı sonralık ufku, odaktaki {ar:وَعْدُ الْآخِرَةِ, tr:waʿdu l-ākhira, gloss:sonraki vaat} sözünü yerel sıranın ötesine de açar. Âhirete inanmayanlara yönelik azap bu sonraki hayatı sorumluluk ufku yapar (17:10). Hemen gelen dünya hayatı ve hızlandırılmış karşılık, yakın sonuçla bu sonralık arasındaki karşıtlığı kurar (17:18); âhireti amaç edinip onun için çabalama sürdürülen yönelişi, derecelerin farklılaşması ise sonuçların ayrımını ekler (17:19, 17:21). {ar:الْآخِرَةِ, tr:al-ākhira, gloss:sonraki olan} bu bağlamlarda ölümden sonraki hayatı da çağrıştırır: yeniden yaratılma sorusuna ilk yaratılış ve yakınlıkla cevap verilir (17:51), insanlar Rablerinin huzuruna ilk yaratılmış gibi çıkarılır (18:48). Bu sahneler odaktaki sonraki vaadin tarihsel sırasını korurken âhiret için ayrı bir ufuk açar. Yılları sayan ifade 17:12’de geçer; {ar:وَعْدُ, tr:waʿdu, gloss:vaat} ile aynı kökten olmadığı için bu sayma vaade takvim aralığı eklemez (17:12).

Daha uzak ve zayıf bir benzetmede, iyilik ve kötülüğün ayrı sonuçları ile ilk ve sonraki seferin sayılabilirliği dönüşümlü verimler gibi düşünülebilir: aynı hurma ağacı bir yıl ürün verir, ertesi yıl vermez. {ar:أَوَّلَ مَرَّةٍ, tr:awwala marratin, gloss:ilk sefer} ve {ar:مَرَّةٍ, tr:marratin, gloss:bir sefer} tek tek sayılmış dönüşleri sağlar; ağaç imgesi bu karşıt sonuçlara bir yıllık verim ritmi yakıştırır. Bu yalnızca benzetmenin ritmidir: ayette hurma veya hasat geçmez ve gerçek bir yıllık döngü öngörülmez. İlk ve tekil sefer aradaki süreyi ya da acılı bir geçişi belirlemediğinden, benzetme karşıt verim imgesi olarak kalır.

## Yüzden İçeri

Vaatten sonra gelen ilk amaç, {ar:لِيَسُوءُوا, tr:li-yasūʾū, gloss:yüzlere zarar vermeleri için} fiilinin doğrudan nesnesi olan {ar:وُجُوهَكُمْ, tr:wujūhakum, gloss:yüzlerinizi} bedenin öne bakan, görünür yüzeyi olarak hedef alır. Fiil çoğul bir yapan grubunu gösterir; kim oldukları ve zararın kesin fiziksel biçimi bu ifadede açıklanmaz. Amaç lâmı yüzlere yönelen zararı kurar, ardından gelen vavlı iki amaç yapısı da onu aynı dizinin başlangıcı yapar.

Şarttaki {ar:أَسَأْتُمْ, tr:asāʾtum, gloss:kötülük ettiniz} ile amaçtaki {ar:لِيَسُوءُوا, tr:li-yasūʾū, gloss:yüzlere zarar vermeleri için} aynı kökün farklı biçimleridir: ilki muhatapların kötülük eylemini, ikincisi yüzlerdeki olumsuz sonucu kurar. Bu bağlantı, 17:11’de çağırma fiilinin {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} çağrı adı {ar:دُعَاءَهُ, tr:duʿāʾahu, gloss:çağrısı} ile yinelenmesiyle keskinleşir: aynı çağrı hem {ar:الشَّرِّ, tr:ash-sharr, gloss:kötülüğe} hem {ar:الْخَيْرِ, tr:al-khayr, gloss:iyiliğe} yönelir (17:11). Ardından gelen {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} insan niteliği, istenen şeyi iyi tartmadan çağırma ihtimalini ekler; arzu edilen şeyin yararlı olduğu böylece güvenceye alınmaz (17:11). Bu temas, odaktaki zararı tersine çevirmekten çok, insanın değer verme biçiminin de aceleyle bulanabileceğini düşündürür. Genel ahlaki bozulma daha geniş bir yorumdur; yalnızca düşünmeden söylenen çağrıya yönelik uyarı olarak okumak da mümkündür (17:11).

Odaktaki {ar:وُجُوهَكُمْ, tr:wujūhakum, gloss:yüzlerinizi} somut yüzü, daha sonraki toplanma sahnesinde yüzleri üzerinde bir araya getirilen ve görme, konuşma, işitme duyularından yoksun bırakılan bedenlerle yankılanır (17:97). Bu ortak bedensel görüntü yerel yarayı daha geniş bir son ufkuna taşır; bağlantı 17:97’deki topluluğu aynı kişiler ya da yüz zararının sonucu olarak tanımlamaz.

İkinci amaç, {ar:وَلِيَدْخُلُوا, tr:wa-li-yadkhulū, gloss:ve girmeleri için} ile yüzlere yönelen ilk amaca bağlanır. Giriş lâmı hareketi amaçlı kılar; {ar:الْمَسْجِدَ, tr:al-masjida, gloss:mescidi} secde ve toplu ibadet için ayrılmış yeri, ortak kutsal iç alanı adlandırır. Dışarıdan içeri geçiş bu ortak mekânın sınırını aşar; okuma bu fiziksel eşiğe dayanır, gizli bir iç dünya ya da belirtilmemiş mimari biçim ileri sürmez. Ayet bu kutsal yerin hangi tarihî mescit olduğunu açık bırakır.

Bu girişi geçmiş örneğe bağlayan {ar:كَمَا, tr:kamā, gloss:... gibi} karşılaştırması, gelecek {ar:يَدْخُلُوا, tr:yadkhulū, gloss:girsinler} fiilini tamamlanmış {ar:دَخَلُوهُ, tr:dakhalūhu, gloss:onun içine girdiler} geçişle yan yana getirir. Zamir aynı mescide döner; önceki giriş yeni girişin yerel örneği olur. Karşılaştırmadaki {ar:مَا, tr:mā, gloss:ne / olan} hem giriş olayına hem de gerçekleşme biçimine açık kalır; iki okuma da mümkün olduğundan biri ötekini dışlamaz. {ar:أَوَّلَ مَرَّةٍ, tr:awwala marratin, gloss:ilk sefer} bu örneği sayılabilir ilk geçiş yapar; tekil {ar:مَرَّةٍ, tr:marratin, gloss:bir sefer} bir sayım birimidir. Böylece geçmiş giriş yerel ve sayılabilir bir örnek olur; daha geniş döngü, kozmik başlangıç, takvim aralığı ya da acılı geçiş bu karşılaştırmanın kapsamına girmez.

Bu kutsal eşiğin başka bir görünümü, işaretleri görmeye yönelen gece yolculuğudur: {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} iki mescit arasında, çevresi bereketli kılınmış alana doğru hareketi kurar (17:1). {ar:الْمَسْجِدِ الْحَرَامِ, tr:al-masjid al-ḥarām, gloss:kutsal mescid} ile {ar:الْمَسْجِدِ الْأَقْصَى, tr:al-masjid al-aqṣā, gloss:uzak mescid}, 17:7’deki {ar:الْمَسْجِدَ, tr:al-masjida, gloss:mescidi} ile secde ve ortak ibadet yerini paylaşır. Yolculuğun {ar:لِنُرِيَهُ مِنْ آيَاتِنَا, tr:li-nuriyahu min āyātinā, gloss:ayetlerimizden gösterelim diye} amacı işaretleri göstermektir (17:1). Bu korunaklı, yönelmiş geçişte kutsal mekân işaretlere açılır; 17:7’de aynı mekân yüzlerin hedef alındığı zorla girişin iç tarafıdır (17:1, 17:7). Bağlantının katkısı, kutsal eşiğe yönelişin iki karşıt kullanımını görünür kılmasıdır; faillerin ya da tarihsel olayların özdeşliğini ve görme ile incitme arasında ortak bir kökü ileri sürmez.

17:5’teki ilk vaadin yerine gelmesinden sonra {ar:أُولِي بَأْسٍ شَدِيدٍ, tr:ulī baʾsin shadīd, gloss:şiddetli güce sahip olanlar} diye nitelenen bir kuvvet gönderilir (17:5). {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik} bu kuvvetin gönderilip yöneltildiğini bildirir; yola çıkarılıp ileri sürülme imgesi harekete ivme katar. Ardından {ar:فَجَاسُوا, tr:fa-jāsū, gloss:dolaşıp geçtiler} evlerin arasında dolaşır; {ar:خِلَالَ الدِّيَارِ, tr:khilāla d-diyār, gloss:evlerin aralarından} bu dolaşmanın içinden geçtiği boşlukları güzergâha çevirir (17:5). Olağan dolaşma fiili ile evler arasındaki geçitler birlikte, yerleşik zemine karışma, basma ve içeri sızma görüntüsünü kurar. Bu yol odaktaki {ar:لِيَدْخُلُوا الْمَسْجِدَ, tr:li-yadkhulū al-masjida, gloss:mescide girmeleri için} amacına uzanınca kutsal iç mekân, evler arasından geçmiş hareketin geri dönen ucu gibi duyulur (17:5, 17:7). Bu, iki bağlam arasındaki güzergâh bağlantısıdır; tarihsel fail kimliğini belirlemez ve her vaat ya da girişi saldırı saymaz.

Güzergâhtaki yenilgi ve geri geliş, kesintisiz bir çöküş yerine davranışla değişebilen bir topluluk döngüsü açar. {ar:رَدَدْنَا لَكُمُ الْكَرَّةَ, tr:radadnā lakumu l-karrata, gloss:dönüşü size geri verdik} ilk yenilgiyi kesip gücü topluluğa geri verir (17:6); {ar:يَرْحَمَكُمْ, tr:yarḥamakum, gloss:size merhamet eder} ihtimali ve {ar:وَإِنْ عُدْتُمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:dönerseniz Biz de döneriz} koşulu yeni bir dönüşe yer açar (17:8). 17:4’te yeryüzündeki bozulma ve yükselmenin iki kez anılması bu tarihsel tekrarın arka planını kurar; odaktaki {ar:أَحْسَنتُمْ, tr:aḥsantum, gloss:iyilik ettiniz} ve {ar:أَسَأْتُمْ, tr:asāʾtum, gloss:kötülük ettiniz} şartlarıysa davranışı karşılık döngüsüne katar (17:4, 17:7). {ar:مَرَّةٍ, tr:marratin, gloss:bir sefer} tek bir sayılabilir olayı, 17:4’teki {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} iki bozulmayı sayar; geniş döngü tekil biçimi çoğullaştırmadan kurulur (17:4, 17:7). Bu topluluk ölçeğindeki bağlantı, kişisel eylem ilkesinin yerine geçmez ve tarihsel tekrarın kaçınılmaz bir yasa olduğunu ileri sürmez; gösterdiği, yenilgi ile toparlanmanın davranışa bağlı yeni bir karşılığa açık oluşudur (17:5, 17:6, 17:8).

## Yıkımın Alanı

Son amaç, {ar:وَلِيُتَبِّرُوا, tr:wa-li-yutabbirū, gloss:ve yıkmaları için} ile aynı vav ve lâm dizisine katılır; böylece yüzlere zarar ve mescide girişin ardından hedeflenen bir yıkım gelir. Fiil II. bâbdadır ve yok etme, etkisini boşa çıkarma gücü taşır. Ardından gelen {ar:تَتْبِيرًا, tr:tatbīran, gloss:yıkım} aynı kökten isim-fiil olarak eylemi yeniden adlandırıp yoğunlaştırır; kapanışa yıkımın kendisini getirir, ayrı bir nesne eklemez. Sonuncu amaç yerel bir doruk kurar, yorumlar arasında değer sıralaması oluşturmaz.

{ar:مَا عَلَوْا, tr:mā ʿalaw, gloss:üstün geldikleri şey} yıkımın nesnesini açık bırakırken {ar:عَلَوْا, tr:ʿalaw, gloss:yükseldiler} bu alanı onların yükseldiği, üstün geldiği ya da egemenlik kurduğu ilişkiyle sınırlar. Hedef böylece rastgele her şey değil, üzerinde güç kurdukları alandır; maddi hasar veya enkaz bunun olası gerçekleşmesidir. İlişki hedefi belirlerken yıkılacak nesnelerin dökümü açık kalır.

{ar:لِيُتَبِّرُوا, tr:li-yutabbirū, gloss:yıkmaları için} fiili ve {ar:تَتْبِيرًا, tr:tatbīran, gloss:yıkım} isim-fiili yok etme anlamını korurken kırılıp parçalara ayrılma görüntüsünü de açar. Yapılan ve yükseltilen işlerin yıkılmasıyla ezilenlerin mirasçı olması, yok oluşa kurulu gücün el değiştirmesini ekler (7:137). Putların parça parça edilmesi yıkımın maddi biçimini somutlaştırır (21:58). Kemikler, taş ve demir gibi maddi örnekler ile “kim yeniden yaratacak?” sorusu ise parçalanmış maddenin geri dönmesi ihtimalini daha uzak bir ufukta açar (17:49, 17:50, 17:51). Bu yankılar yıkımın olası biçimlerini ve yeniden yaratılma sorusunu genişletir; 17:7’deki hedefi Firavun’un işleriyle ya da putlarla özdeşleştirmez ve onun maddesini belirlemez.

Bu toplumsal okumanın dayanağı, yükselme ile baskı ve güç değişimini birlikte gösteren iki sahnedir: Firavun’un kendini yüceltip halkı bölmesi ve bir kesimi ezmesi (28:4), ardından ezilenlerin mirasçı olurken yükseltilmiş işlerin yıkılması (7:137). Bu tersine dönüş {ar:مَا عَلَوْا, tr:mā ʿalaw, gloss:üstün geldikleri şey} hedefini egemen olunan bir düzen olarak da duyurur; tek tek nesneler yine belirtilmez. Odaktaki {ar:عَلَوْا, tr:ʿalaw, gloss:yükseldiler} fiilinin olağan yükselme ve üstün gelme anlamı temel kalır; bu bağlamda kibir tonu eklenebilir, ancak bu özel ilişki kelimenin tek ya da zorunlu anlamı değildir.

Yüzün bedensel hedef oluşu, başkaları önündeki görünürlüğü sayesinde kamusal saygınlık yankısını da taşır. Firavun’un yükselişi ve ezmesiyle ezilenlerin sonradan mirasçı olması, bu tersine dönüşün bedensel incinmeye aşağılanma ve itibar kaybı eklemesine zemin verir (28:4, 7:137). Böylece {ar:وُجُوهَكُمْ, tr:wujūhakum, gloss:yüzlerinizi}, {ar:الْمَسْجِدَ, tr:al-masjida, gloss:mescidi} ve {ar:مَا عَلَوْا, tr:mā ʿalaw, gloss:üstün geldikleri şey} hedefleri bedendeki görünür yüzden ortak kutsal iç mekâna, oradan egemen olunan alana uzanır; amaç dizisi cezanın ölçeğini bedenden toplumsal düzene genişletir. Buradaki itibar çağrışımı yüzün beden oluşunu değiştirmez ve onu önder ya da toplumsal rütbe diye adlandırmaz. {ar:أَسَأْتُمْ, tr:asāʾtum, gloss:kötülük ettiniz} ile {ar:لِيَسُوءُوا, tr:li-yasūʾū, gloss:yüzlere zarar vermeleri için} arasındaki zarar kökü, yüzün görünürlüğü ve {ar:عَلَوْا, tr:ʿalaw, gloss:yükseldiler} ilişkisinin yan yana gelişi, güç yıkılmadan önce yapılan işin ayıplanmasını da düşündürebilir; bu özel yankıda kınayanın sesi belirtilmez.

Üstte duran ya da sonradan eklenen parça anlamı, odaktaki {ar:مَا عَلَوْا, tr:mā ʿalaw, gloss:üstün geldikleri şey} için daha dolaylı bir benzetme açar. Sonlu {ar:عَلَوْا, tr:ʿalaw, gloss:yükseldiler} fiilinin kendi anlamı yükselmek ya da üstün gelmektir; üst parça imgesi kelimenin doğrudan karşılığı değildir. Bu benzetmenin üç ayrı dayanağı vardır: 17:5’te hareket evler arasındaki geçitlerden içeri ilerler, 17:12’de olaylar ayrıntılandırılır, 7:137’de yapılan ve yükseltilen işler yıkılır (17:5, 17:12, 7:137). Geçitlerden içeri yöneliş mekânsal yolu, ayrıntılandırma parçalanabilirliği, yükseltilmiş işlerin yıkımı ise kurulu yapıyı sağlar; birlikte, egemen olunan düzenin üst katmanının içeriden sökülmesi imgesini kurabilirler. Bu yalnızca bu bağlamlar arasındaki bileşik benzetmedir; odaktaki hedefin hangi yapılar olduğunu belirlemez.

17:16’daki ayrıcalık ve taşkınlık dizisi, odaktaki {ar:لِيُتَبِّرُوا, tr:li-yutabbirū, gloss:yıkmaları için} yıkımını ve {ar:مَا عَلَوْا, tr:mā ʿalaw, gloss:üstün geldikleri şey} hedefini içeriden çözülme ihtimaliyle buluşturur. {ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:refah içindekiler} bolluk içindeki kişileri öne çıkarır; bu rahatlık sınır aşmaya elveren iç koşula dönüşür, ardından {ar:فَفَسَقُوا فِيهَا, tr:fa-fasaqū fīhā, gloss:orada sınırı aşıp taşkınlık ettiler} olağan anlamıyla başkaldırı ve ihlali bildirir (17:16). Aynı kökün iç kabuğundan çıkma imgesi, eylemin o yerde gerçekleşmesi ve hemen ardından gelen yıkımla sınır kırılmasını da duyurur; helâk fiili ve onu izleyen {ar:فَدَمَّرْنَاهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık} bu ihlalin ardından gelen kapsamlı sonu belirginleştirir (17:16). Nuh’tan sonraki kuşakların {ar:بِذُنُوبِ عِبَادِهِ, tr:bi-dhunūbi ʿibādihi, gloss:kullarının günahları sebebiyle} helâk edilmesi davranış ve hesap bağını ekler (17:17); 17:4’teki iki bozulma ve yükselme uyarısı da iç kırılma okumasına ayrı bir bağlam sağlar (17:4). Bu ilişki, 17:16’nın hukuki bildirim olarak okunmasını dışlamaz ve odaktaki grubu ya da saldırganları tanımlamaz; yalnızca yıkımın dışarıdan gelen darbeye ek olarak, ayrıcalıkla gevşeyip sınır aşmış bir düzenin sona erişi gibi de duyulmasını sağlar.

</source_prose>
