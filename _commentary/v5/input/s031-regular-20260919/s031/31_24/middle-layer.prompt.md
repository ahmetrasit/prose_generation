# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:24**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.middle.claims.json`

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
- Refer to source paragraphs as `31:24 ¶N`.

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

`(31:24 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:24",
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
        "citation": "(31:24 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_24/31_24.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_24/31_24.middle.claims.json \
  --ayah-ref 31:24
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_24/31_24.prose.editorial.tr.md`

<source_prose>
## Yararlanmanın gerçekliği ve ölçüsü

31:24, aynı çoğul muhataplara önce gerçek bir yarar sunar, fakat bu yararı {ar:قَلِيلًا, tr:qalīlan, gloss:az bir ölçüde} ile sınırlar; {ar:ثُمَّ, tr:thumma, gloss:sonra} ile açılan sonraki evrede onları {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} ve {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} yöneltilmiş {ar:عَذَابٍ غَلِيظٍ, tr:ʿadhābin ghalīẓin, gloss:ağır bir azap} hedefine götürür. Ayetin hareketi, {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} arasındaki değişimde belirginleşir: yarar gerçektir, ama ceza yönelişinin yerini almaz.

Her iki fiildeki birinci çoğul özne eylemi muhataplara yöneltir. Form II biçimindeki {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ve ekli -hum, yararın onların kendi çabasıyla üretilmesinden çok onlara sunulduğunu gösterir; fiil ayrıca bir mülk devri anlatmaz. İkizlenen ünsüz bu sunuluşu dışarıdan gelen bir edim gibi işittirir, ancak bu ses izlenimi tek başına bir niyet kanıtı değildir. {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} içinde aynı kişi ve sayı özelliğiyle -hum yeniden görünür: yararı alanlarla zorlamanın muhatapları aynı gruptur; değişen kişiler değil, onlara yapılan eylemdir. Kişi ve sayı bu ortak muhataplığı belirler; grubun ayet dışındaki kimliği ise açık kalır.

Fiilden sonra gelen mansup ve belirsiz ölçü sözü {ar:قَلِيلًا, tr:qalīlan, gloss:az bir ölçüde}, ilk yararlandırma evresini sınırlar; sonraki cezanın derecesini ölçmez. Küçüklük miktarda, sürede ya da yararın değerinde hissedilebilir; bunlar kesinleşmiş ayrı ölçüler değil, sınırlı oluşun birbiriyle uyumlu yönleridir. Bu ölçü yararın kısılmış veya pay edilmiş gibi duyulmasına izin verir, fakat belirli bir tahsisat anlatmaz. Belirsiz biçim miktarı ve süreyi sayıyla sabitlemez; yararın sınırlı olduğunu yine de açıkça bildirir.

İki eylem arasındaki {ar:ثُمَّ, tr:thumma, gloss:sonra}, ilk evreden sonra ikinci eylemi getirir ve anlık bir dönüşten ziyade araya zaman giren bir geçiş duyurur; bekleyişin ne kadar sürdüğü belirtilmez. Şeddeli mîm, hafif ölçü sözünden {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} bitişik sesleriyle basınç taşıyan {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} fiiline geçerken işitilir bir eşik kurar. Böylece yararlandırma ve zorlama ayetin iki vuruşu olur; ses geçişi bu eşiği belirginleştirir.

Form II biçimindeki {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} aynı kelime ailesinde birini yaşatıp belli bir süre o yaşamdan yararlandırma kullanımını da taşır. Olağan yarar anlamı, bu süreli kullanım, {ar:قَلِيلًا, tr:qalīlan, gloss:kısa ölçü} sınırı ve ardından gelen zorlama birlikte düşünüldüğünde ilk evre gerçek, fakat geçici bir kullanım aralığı gibi duyulur. Fiilin yararı zamana yayma ve yükseltme yönleri, bu sınırlı aralığı açık uçlu sahiplikten çok sonraki bildirime dek tanınmış bir pay gibi işittirir. Yararlanmanın sürmesi, sonun ya da ölümün bir vakte ertelenmesine benzetilebilir; bu benzetme kesin beraat, fiilî ömür uzatma veya belirlenmiş bir ölüm tarihi anlamına gelmez. Süre sayıyla belirlenmez; {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} yine de mühletin kısa hissedilmesini destekler.

## Aralığın ufku

Yararlandırma, azlık ve ardından gelen mecburi azap sırası 2:126’da da aynı düzen içinde karşılaşır (2:126). Bu metin düzeyindeki tekrar, şimdiki payı gerçek bir yarar olarak korurken onu tek başına son durak olmaktan çıkarır (2:126). Tekrar böylece sıralamayı güçlendirir; {ar:قَلِيلًا, tr:qalīlan, gloss:azca}’nın miktarı mı, süreyi mi sınırladığı ve yararlanıcıların bu aralığı içeriden nasıl hissettiği açık kalır (2:126).

Hesap ufku 31:23’te belirginleşir: inkâr edenler Allah’a döner, yaptıkları kendilerine bildirilir ve Allah göğüslerin içindekini bilir (31:23). Bu dönüş ve bildirim, 31:24’teki gerçek yararın hesap öncesinde yaşanan bir aralık gibi duyulmasını sağlar; {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} fiilinin zamana yayılan ve yükselten yönü de {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} ile buluşarak açık uçlu sahiplikten ziyade sonrasındaki bildirime dek tanınmış sınırlı bir izin hissi verir (31:23). Aralığın takvimle ölçülen süresi belirtilmez; 31:23’ün ifadesi de her alıcıya bilinçli gizleme yüklemez (31:23). Sure başındaki {ar:الرَّحْمَٰنِ الرَّحِيمِ, tr:ar-Raḥmāni r-Raḥīm, gloss:Rahmân ve Rahîm} adları bu bağışı merhamet tonuyla çerçeveler (31:0): merhamet tonu yararın gerçekliğini korurken cezaya ilişkin hükmü hafifletmez.

31:29’da gece gündüze, gündüz geceye katılır; güneş ve ay belirlenmiş bir vadeye doğru akarken Allah insanların yaptıklarından haberdar olduğunu da bildirir (31:29). Bu döngü, {ar:ثُمَّ, tr:thumma, gloss:sonra} ile sıralanan yarar ve zorlamayı kopuk olaylardan çok birbirini izleyen evreler gibi duyurur (31:29). Göksel akışın {ar:أَجَلٍۢ مُّسَمًّۭى, tr:ajalin musamman, gloss:belirlenmiş bir vade} ufku, kısa yararı sonu uzaktan görünen bir dönem gibi düşünmeye elverir; 31:24’ün süresini bu göksel vadeyle özdeşleştirmeden, sonu olan bir dönem hissi verir (31:29).

Bu aralığın içeriden nasıl göründüğü 31:34’te açık kalır: hiçbir can yarın ne kazanacağını ya da hangi yerde öleceğini bilmez (31:34). {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} dışarıdan sınırlı bir dönem gösterirken, yaşayan kişi için en yakın gelecek ve hayatın nerede kesileceği örtük olabilir (31:34). Azlık sözü kendi başına bilgisizlik anlamına gelmez; elde edilen yarar da yarınki kazancı açığa çıkarmaz (31:34). Aralığın sayısal olarak ölçülebilmesi mümkündür, ancak 31:24 süreyi, tarihi, ölüm yerini veya ölüm sebebini bildirmez.

## Payın ölçüsü ve zamanın karşılığı

31:20’de nimetlerin görünür ve görünmez yönlerden tamamlanıp yayılması bolluğu ortaya koyar (31:20). 31:26’da Allah’ın kendine yeterli oluşu, verenin bu bolluğa muhtaç olmadığını belirtir (31:26). 31:27’de deniz başka denizlerle artırılsa bile Allah’ın sözlerinin tükenmemesi, bu bolluk ufkunu tükenmezlik yönünde genişletir (31:27). Bu ayrıntılar birlikte düşünüldüğünde, {ar:قَلِيلًا, tr:qalīlan, gloss:azca} ile verilen sınırlı pay kaynağın darlığını değil, alıcıya ayrılan ölçüyü gösterir (31:20, 31:26, 31:27). {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} fiilinin yaşam boyunca yararı sürdürme yönü de kaynağın eksilmesinden çok, alıcıya tanınan aralığı öne çıkarır (31:20, 31:26, 31:27). Bu bağlam, neden bu gruba bu payın verildiğini veya azlığın miktar mı süre mi olduğunu belirlemez (31:20, 31:26, 31:27).

Kaynağın bolluğu ile alıcıya ayrılan pay arasındaki fark, 31:8 ve 31:9’daki başka bir zaman ölçüsünün yanında daha belirginleşir (31:8, 31:9). 31:8’in nimet bahçeleri ve sevinçli iyi hâli, 31:9’daki kalıcılık ve gerçek vaatle birlikte uzun bir kalış açar (31:8, 31:9). Bunun yanında {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile verilen iyilik hakiki, {ar:قَلِيلًا, tr:qalīlan, gloss:azca} ile sınırlı bir pay olarak kalır; 31:8’deki nimet ile 31:24’teki yarar ayrı iyilik alanlarıdır (31:8, 31:9, 31:24). 31:9’un kalıcılığı bu ikisini eşitlemeden bir beklenti ufku ekler; 31:24’ün alıcıları 31:9’daki vaadin muhatabı olarak belirlenmez (31:9).

31:30’daki hak-batıl ayrımı, batıllığı Allah dışındaki yanlış yönelişe bağlar ve böylece odaktaki gerçek yararın niteliğinden ayırır (31:30). 31:31’deki nimet ve şükür sahnesi, dünya içindeki iyiliğe karşılık vermenin bir görünümünü sunar; oradaki sabırlı ve şükreden kişiler 31:24’ün alıcılarıyla özdeşleşmez (31:31). 31:33’ün dünya hayatının aldatıcılığına karşı uyarısı ise bu iki ayrımı bir beklenti sınırına taşır: gerçek yarar vardır, fakat onu tamamlanmış ve kalıcı güvence saymak tehlikelidir (31:33). Böylece {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile verilen iyilik batıl bir yönelişe indirgenmeden geçici kalır; {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} bu görünümü tamamlanmamış bir zaman aralığı gibi genişletir, fakat belirli bir eksik miktar göstermez (31:30, 31:31, 31:33). Uyarı genel kalır; her alıcıya aldanmışlık yüklemez (31:33).

## Mecburi varışın niteliği

{ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız}, {ar:ثُمَّ, tr:thumma, gloss:sonra} ile açılan ikinci yan cümlenin ilk fiilidir; yeni bir yarar değil, zorlayıcı eylem getirir. Form VIII biçiminde birinci çoğul özne ve aynı -hum nesnesiyle kurulur. Çekirdek anlamı zorlanmadır: fiil muhatapları mecbur bırakır, doğrudan yaralama veya karşılıklı zarar verme eylemi kurmaz. Peş peşe gelen ikizlenmiş sesleri bu zorlamayı işitilir bir basınçla taşır; bu, sözlü yüzeyin izlenimidir, bir ses yasası değildir. Aynı kelime ailesindeki zarar ve eksilme yönü, fiilin zorlanma anlamıyla ve {ar:إِلَىٰ عَذَابٍ, tr:ilā ʿadhābin, gloss:bir azaba doğru} sözlerinin bağımsızca adlandırdığı olumsuz hedefle birleşir; bu temas hareketi sıkıntı ve kayıp yönünde ağırlaştırır. Bu çağrışım fiile körlük ya da bedensel yaralanma anlamı eklemez. İlk yararın ardından gelen gecikmeli sonuç, sırayı uyarı yüklü bir taviz gibi duyurur: yararın gerçekliği korunurken cezalandırıcı devamı da yürürlükte kalır.

Küçük {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} edatı, zorlayıcı fiilden cezalandırıcı hedefe yönelişi tamamlar. Fiilden sonra gelip mecrur ismi yönettiği için burada zamansal “-e kadar” değil, hedef bildirir; kurduğu bağ dilbilgisel bir varış ilişkisidir, fiziksel bir yolculuk değil. Okunuşta edatın son ünlüsünün ardından hedef ismin gelmesi kulağı bu varışa taşır; ses akışı dilbilgisinin kurduğu yönü belirginleştirir, yeni bir hedef eklemez. Edatın yönettiği {ar:عَذَابٍ غَلِيظٍ, tr:ʿadhābin ghalīẓin, gloss:ağır bir azap} öbeğinin tamamı varış noktasıdır.

Edatın yönettiği konumu dolduran {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap/ceza}, mecrur, tekil ve belirsiz bir isimdir; zorlanmış hareketi ayrı bir eyleme değil, cezalandırıcı bir sonuca bağlar. Belirsiz biçim cezanın türünü ve miktarını açık bırakırken, olağan ceza anlamı varışı genel bir rahatsızlıktan daha belirgin kılar. Böylece cümle tek bir cezalandırıcı hedef kurar; özel bir hukukî usul tarif etmez, başka duyusal çağrışımlara da alan bırakır.

Ardından gelen {ar:غَلِيظٍ, tr:ghalīẓin, gloss:ağır} sıfatı isimle aynı belirsiz ve genitif uyumu taşır; azap ile niteliğini iki ayrı varış değil, tek bir nitelikli hedef yapar. Sıfat ayrı bir olay başlatmaz. Sondaki niteleme cümle kapanırken hedefin ağırlığını sabitler: azap yalnızca bir ceza adı olarak değil, ağır niteliğiyle tamamlanır. Belirsizlik ağırlığın derecesini sayıya bağlamaz, fakat niteliği ortadan kaldırmaz.

Olağan ağır ve çetin anlamı korunurken, {ar:غَلِيظٍ, tr:ghalīẓin, gloss:ağır} aynı kelime ailesindeki inceliğin karşıtı olan fiziksel kalınlık ve yoğunluk kullanımını da hedefe taşır; azap böylece dokunulur, kaba ve dirençli bir ağırlık kazanır. Açılıştaki {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} ile {ar:عَذَابٍ غَلِيظٍ, tr:ʿadhābin ghalīẓin, gloss:yoğun ve ağır bir azap} karşılaşınca hareket kısa ve hafif ilk evreden yoğun, ağır bir sona geçer; bu maddi kütle iddiası değil, ağırlık imgesidir. Bundan ayrı olarak, aynı kelime ailesinin insanın huyu, sözü veya davranışında sertlik ve kabalık bildiren kullanımı 31:22’deki iyi davranışla yan yana geldiğinde cezayı alıcıya yönelen sert muamele gibi duyurabilir (31:22). Bu ahlaki çağrışım cezayı niteleyen sıfata aittir, faili bir huyla tanımlamaz. İşin ya da cezanın olağanın üstünde güçlü ve çetin olması yönü de sertlik izlenimini artırır; cezanın nedeni ise açık kalır.

Azap ismiyle onu izleyen sıfatın belirsiz genitif sonlanışları birlikte işitilince tek nitelikli hedef gibi kapanır; ayette sıfattan sonra durulması da ağırlığı son vuruşa taşır. Boğazdan gelen ġaynın tınısı ve kalın ẓâ vurgusu, sıfatın anlamına bağlı bir kapanış izlenimi verir; bu işitsel etki tek başına sesbilimsel anlam kanıtı değildir. Daha önceki belirsiz mansup {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} sonlanışı genitif kapanışlarla yankılanır: iki ayrı evrenin uçları sesçe bağlanır, ölçüden ağıra geçiş belirginleşir. Bu ses yankısı sözlük anlamını değiştirmeden iki evrenin arasındaki geçişi duyurur.

## Yön, seçim ve hesap

Hedefe yönelme, komşu ayetlerdeki irade farkıyla da keskinleşir (31:22). 31:22’de kişi yüzünü Allah’a yöneltir: {ar:يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ, tr:yuslim wajhahu ilā llāh, gloss:yüzünü Allah’a teslim eder}. {ar:وَهُوَ مُحْسِنٌۭ, tr:wa-huwa muḥsin, gloss:iyilik ederken} bu yönelişin iyi davranışla birlikte olduğunu belirtir; {ar:فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:faqadi stamsaka bil-ʿurwati l-wuthqā, gloss:sağlam kulpa tutunmuştur} ise sağlam tutamağa bağlanmayı görünür kılar (31:22). Yüzün yönü, iyi davranış ve tutunma böylece seçilmiş, güvenli bir hareket oluşturur (31:22). Bunun yanında {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile sunulan gerçek yarar erişilebilir bir iyiliktir, fakat kendi başına sağlam kulpa tutunmaya dönüşmez (31:22). {ar:نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ, tr:naḍṭarruhum ilā ʿadhābin, gloss:azaba doğru mecbur bırakırız} ise yönü dayatır; son hareket seçimsizdir (31:24). {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} biçiminin başka bir kullanımındaki sıkıştıracak kadar yaklaşma, sağlam tutamak karşısındaki {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} yönelişi daralan bir eşiğe ilerleme gibi duyurabilir (31:22, 31:24). Bu karşılaştırma seçilmiş tutunma ile dayatılmış yönelişi yan yana getirir; neden-sonuç ilişkisi veya kişilerin özdeşliği ileri sürmez (31:22, 31:24).

31:23’te dönüş, yapılanların bildirimi ve Allah’ın göğüslerin içindekini bilmesi hesap ufkunu kurar; 31:25’te sorulan yaratma sorusuna “Allah” denmesiyle birlikte çoğunun bilmediğinin vurgulanması bu çevreye bilgi ve bilinç sınırını ekler (31:23, 31:25). Bu iki yakınlık, {ar:نَضْطَرُّهُمْ إِلَىٰ, tr:naḍṭarruhum ilā, gloss:onları bir yöne mecbur bırakırız} hareketini nötr değil, istenmeyen ve zararlı bir sona yöneliş gibi çerçeveler (31:23, 31:25). Bu hesap ufkunda {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap}, cezalandırıcı sonuç olarak belirir; türü açıklanmaz (31:23). Dönüş hesabın ufkunu açar, 31:24’teki zorunlu yöneliş ise ayrı bir varış kurar; ikisi aynı hedef değildir (31:23).

31:21’de şeytan insanları ateş azabına çağırır; bunu 31:22’nin gönüllü ve sağlam tutunması, 31:23’ün dönüşü ve 31:24’ün {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} ile kurduğu zorunlu hareket izler (31:21, 31:22, 31:23). Bu dizide 31:24’ün mecburi varışı, 31:21’de adı konmuş yıkıcı rotanın olası kapanışı gibi duyulabilir; ateş azabı ile odaktaki ceza hedefi aynı türden bir sonu işaret eder (31:21). Bağlantı varış türündeki yakınlıktır; çağrının kabulü ya da tek bir nedensel zincir bu sıradan çıkarılamaz (31:21).

31:15’te ebeveynin Allah’a ortak koşmaya yönelik şiddetli ve ısrarlı baskısı anlatılır; aynı ayet bu baskıya uyulmamasını buyurur ve Allah’a dönüşü anar (31:15). Bu insan zorlaması reddedilebilir; 31:24’teki {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} ise varış yönünü seçimsiz kılar (31:15). Karşılaştırma zorlamanın iki ayrı durumunu gösterir; olaylar nedensel olarak bağlanmaz, kişiler de özdeşleştirilmez; insan zorlaması, kaçınılmaz son ve doğrudan zarar arasındaki ağırlık dağılımı açık kalır (31:15). 31:15’teki dönüş ve hesap ufku, {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap/ceza} hedefinin cezalandırıcı tonunu bu ayrı yöneliş içinde keskinleştirir (31:15).

İrade karşılaştırmalarından ayrı olarak, 31:32 tehlike sonrasındaki yaşamı gösteren başka bir sahne açar (31:32). Üzerlerine gölgeler gibi kapanan dalgalar içinde insanlar dini yalnız Allah’a özgü kılarak O’na yakarır; karaya çıkarılmaları yaşamın yeniden sürmesini sağlarken içlerinden bazıları ölçülü davranır, bazılarıysa nankörleşip ayetleri inkâr eder (31:32). Bu kurtuluştan sonra süren yaşam, {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile verilen gerçek yararı kullanılabilir bir mühlet gibi düşündürür; kurtuluş son hesabı kapatmaz (31:32). Bu, 31:24’ten önce aynı kurtuluşun yaşandığı veya iki ayetteki insanların aynı olduğu iddiası değildir (31:32). Dalga örtüsünün yoğunluğu, {ar:غَلِيظٍ, tr:ghalīẓin, gloss:yoğun ve ağır} sıfatının kalınlık ve yoğunluk yönüne duyusal bir karşılık verir; böylece cezanın sert ve olağanın üstünde ağır oluşunu hissettirir, maddi biçimini ya da ölçüsünü belirlemez (31:32).

## Yararın somut çağrışımları

İhtiyaç anında işe yarayan somut bir şey düşüncesi, 31:22’deki sağlam kulpa tutunma imgesinden doğar (31:22). Bu imge, Form II biçimindeki {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} fiilinin kullanıma açık yarar yönünü bir süre işe yarayan pay gibi düşünmeye zemin verir (31:22). Bu yön {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} ve {ar:نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ, tr:naḍṭarruhum ilā ʿadhābin, gloss:onları bir azaba doğru mecbur bırakırız} ile kurulan hedefle buluşunca güvence altındaki bir mülkten çok, zorunlu geçişte işe yarayan sınırlı bir pay gibi görünür (31:22). Aynı kelime ailesindeki azık kullanımı bu payı, geçimi veya yolculuğu bir süre sürdüren yetersiz bir yol azığı gibi duyurur. Buradaki yol azığı, gerçek bir sefer ya da eşya dökümü değil, yararın sınırlı süre kullanılabilir oluşuna dair bir benzetmedir.

Yararlandırma ayrıca haz alma ve hoşnutluk yönü taşır. Form II biçimindeki {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile açılan erişilebilir ve hoş evreyi {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü}, ardından {ar:ثُمَّ, tr:thumma, gloss:sonra} ile gelen zorlama ve {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap} hedefi sınırlar; böylece son, önceki erişimin karşı kutbu olur. Aynı kelime ailesindeki tatlı ve kolay tüketilen yiyecek içecek kullanımı bu hoşluğu duyusal olarak açar. Karşıtlık, cezalandırıcı {ar:عَذَابٍ, tr:ʿadhābin, gloss:ceza} ismini önceki haz veren yararın karşısına koyar; ayet bir yiyecek ya da tat adı vermediğinden azap olağan ceza anlamında kalır.

Bu kelime ailesinin başka bir kullanımında birini bir işten alıkoyma vardır; sütten keser gibi uzaklaştırma da bu kullanımla ilişkilidir. Önce yararlandırıp ardından zorlamaya geçen ayet akışı, bu ailevi çağrışımı erişimin kesilmesi ve önceki nimetten uzak düşme yönünde etkinleştirir. Böylece alıkoyma veya sütten kesilme, yarardan kopuşu duyurur; odaktaki {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap} ise isim olarak cezayı bildirir, bir alıkoyma fiili değildir.

Başka bir bağlamda, 31:6’da oyalayıcı sözün satın alınması, Allah’ın yolundan saptırma ve ceza birlikte bulunur (31:6). {ar:لَهْوَ الْحَدِيثِ, tr:lahwa al-ḥadīth, gloss:oyalayıcı söz} dikkati başka bir yola çeker; 31:24’teki {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile verilen gerçek ama az pay da ardından gelen ceza ile birlikte kısa bir getiri-maliyet çizgisi düşündürür (31:6). 31:6’daki satın alma bilerek edinilmiş bir dikkat dağıtıcıdır; bu karşılaştırma odaktaki yarar ve cezanın da maliyetli bir kısa getiri gibi duyulmasını sağlar (31:6). 31:6’nın cezası ile 31:24’ün hedefi sonuç çizgisinde yan yana gelir, ancak odaktaki kişiler 31:6’daki alıcılarla bir tutulmaz ve odaktaki yarar o satın alımın karşılığı değildir (31:6).

Dikkat dağıtan sözden bu kez yeryüzünün hareketine geçilir. 31:10’da köklü dağlar yeryüzünün sallanmasını önler; böylece sarsılan yer ile dağların sabitliği yan yana durur (31:10). Bu bağımsız görüntü, {ar:قَلِيلًا, tr:qalīlan, gloss:az ölçü} ile belirtilen aralığı sallantı ile sabitlik arasındaki geçici bir evre gibi düşündürür; azlık sözü bu sahnede sallanma anlamı kazanmaz (31:10). {ar:نَضْطَرُّهُمْ إِلَىٰ, tr:naḍṭarruhum ilā, gloss:onları bir yöne mecbur bırakırız} fiilinin başka bir kullanımındaki sıkıştıracak kadar yaklaşma, bu kez sallanan zemin içinde daralan bir yaklaşma gibi canlanır (31:10). Hedefteki {ar:غَلِيظٍ, tr:ghalīẓin, gloss:yoğun ve ağır} sıfatının fiziksel yoğunluğu da zorunlu yönelişe dirençli bir kuşatılma duyusu ekler. Bu, 31:10’la kurulan keşifsel bir duyusal benzetmedir; kasıtlı yankı iddiası veya cezanın maddi biçimi hakkında hüküm değildir (31:10).

Yeryüzünün hareketinden farklı bir ölçeğe, yakın bir bakım ilişkisine geçildiğinde, 31:14’te emzirmenin ardından çocuğun sütten kesilmesini anlatan sahne aynı kelime ailesindeki kesilme çağrışımına somut bir tetik sağlar (31:14). Bu beslenme sahnesi {ar:نُمَتِّعُهُمْ, tr:numattiʿuhum, gloss:onlara yararlandırırız} ile açılan gerçek ve erişilebilir yararın ardından {ar:ثُمَّ, tr:thumma, gloss:sonra} ile gelen {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları mecbur bırakırız} geçişini seçilmemiş bir ayrılığa yaklaştırır (31:14). Böylece önceki besleyici nimete erişimin zorla sona ermesi, cezaya doğru geçişteki kopuş duyusunu belirginleştirir (31:14). Odaktaki {ar:عَذَابٍ, tr:ʿadhābin, gloss:azap/ceza} cezayı bildirir; 31:14 ile 31:24 ayrı sahnelerdir ve 31:14’ün bunu önceden haber verdiği söylenmez (31:14). Sütten kesilme imgesi cezanın anlamını değiştirmeden, önceki besleyici iyiliğe erişimin kesilmesini görünür kılar (31:14).

</source_prose>
