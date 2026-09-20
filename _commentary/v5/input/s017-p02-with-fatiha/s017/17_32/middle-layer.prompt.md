# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:32**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.middle.claims.json`

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
- Refer to source paragraphs as `17:32 ¶N`.

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

`(17:32 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:32",
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
        "citation": "(17:32 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_32/17_32.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_32/17_32.middle.claims.json \
  --ayah-ref 17:32
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_32/17_32.prose.editorial.tr.md`

<source_prose>
“Zinaya yaklaşmayın; çünkü o ağır bir çirkinliktir ve ne kötü bir yoldur” diyen ayet (17:32), önce yasağı, ardından onu gerekçelendiren iki yargıyı kurar: {ar:وَلَا تَقْرَبُوا۟ ٱلزِّنَىٰٓ, tr:wa-lā taqrabū az-zinā, gloss:zinaya yaklaşmayın} buyruğu, {ar:إِنَّهُۥ كَانَ فَٰحِشَةًۭ وَسَآءَ سَبِيلًۭا, tr:innahu kāna fāḥishatan wa-sāʾa sabīlan, gloss:çünkü o ağır bir çirkinliktir ve ne kötü bir yoldur} gerekçesine bağlanır. Başlangıçtaki {ar:وَ, tr:wa, gloss:ve}, sözü sürmekte olan söyleme ekler; cümle böylece kopuk değil, devam eden bir talimat gibi duyulur. Bağlaç bu devamlılığı kurar ama önceki sözün içeriğini açıklamaz.

Yasağın biçimi de bu yönelişi belirginleştirir. {ar:لَا, tr:lā, gloss:yasaklama edatı}, {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşmak} fiilini cezmli muzari biçimde kullanarak yaklaşmayı yasaklar. Fiildeki ikinci çoğul hitap buyruğu birden çok muhataba yöneltir; onları tek kişiyle sınırlamaz, fakat belli bir tarihî topluluğu da adlandırmaz. Yaklaşmak, temas kurma ya da bir işe dâhil olma eşiğine varmayı anlatır ve burada doğrudan {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki} hedefine yönelir.

Bu ad, tek bir olayın veya failin değil, bilinen bir eylem kategorisinin adıdır; mastar biçimi yasağı kişiye değil eyleme yöneltir. {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki}, {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşmak} fiilinin doğrudan nesnesidir. Sonundaki elif-i maksûre olağan çekim işaretini görünür kılmasa da cümledeki nesne işlevi açıktır; bu ilişki yasağın kapsamını kendi başına genişletip daraltmaz. Belirli tanımlık tek bir kişiyi ya da ithamı değil, geçerli evlilik bağı dışındaki cinsel ilişki kategorisini hedefte tutar. Söylenişte tanımlığın lâmı zâya özümlenir, son ā uzar; bu ses özellikleri yeni bir anlam eklemeden adın cinsel hedef olarak işitilmesini sağlar.

Yaklaşmanın temas ve yakınlık eşiği cinsel bağlamda ayrıca bir yankı kazanır: “eşe yaklaşmak” sözü bazı kullanımlarda cinsel ilişkiyi dolaylı biçimde anlatır ve bu kullanım eşe özgüdür. Burada yakınlık çağrışımını açan, fiilin nesnesi olan {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki}dır; olağan “yaklaşmayın” buyruğu da yerinde kalır. Böylece yasak tamamlanmış eylemden önceki eşiğe uzanır, ancak o eşikteki davranışları tek tek sıralamaz.

Buyruğun ardından {ar:إِنَّهُۥ, tr:innahu, gloss:kuşkusuz o} gerekçe cümlesini başlatır; vurgulu {ar:إِنَّ, tr:inna, gloss:kuşkusuz} açıklamayı emre ekler. Zamir doğrudan önceki {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki} adına dönebilir, ya da bütün yaklaşma yasağını geri alabilir. Her iki gönderim de yasağı gerekçenin konusu olarak tuttuğundan bağlantı korunur ve iki imkândan biri seçilmez. Çoğul muhataplara seslenen buyruktan sonra {ar:كَانَ, tr:kāna, gloss:olmak} ile tekil yargıya geçiş dikkati muhataplardan yasaklanan meseleye çevirir; yeni bir konuşucu ya da fail ortaya çıkarmaz. {ar:سَآءَ, tr:sāʾa, gloss:kötü diye yermek} fiilinin gizli öznesi de aynı konuyu sürdürür.

{ar:كَانَ, tr:kāna, gloss:olmak ve bulunmak} ile {ar:فَٰحِشَةًۭ, tr:fāḥishatan, gloss:ağır çirkinlik} birlikte, adı konan meseleye ahlaki bir nitelik yükler. Fāḥishatan, kāna’nın mansup haberidir; gerekli yüklem yerini doldurup eylemi ağır bir sınıfa koyar. Tekil ve belirsiz biçimi bu nitelemeyi bütün kötülüklerin adı hâline getirmez. Olma ve gerçekleşme değeri taşıyan kāna hükmü yalnızca geçmişte kalmış tek bir olaya kapatmaz; biçimin taşıdığı zaman nüansları da bu okumada silinmez.

Fāḥishatanın ağır çirkinlik yargısına, yaklaşma buyruğunun hedefe varmadan eşiği kesmesi sınır aşımı ve ölçüyü taşırma yönünde ihtimalli bir okuma ekler; bu bağlantı ayette genel bir ahlak cetveli ya da adlandırılmış hukuk sınıfı kurmaz. Yakın ölçü imgeleri bu temaya ayrı karşılıklar sağlar: elin bütünüyle açılmaması (17:29), rızkın daraltılması (17:30), öldürmede haddi aşmanın frenlenip kısasın sınırlandırılması (17:33) ve doğru teraziyle tartma (17:35). Bu bağlamlarda {ar:وَلَا تَبْسُطْهَا كُلَّ الْبَسْطِ, tr:wa-lā tabsuṭhā kulla l-basṭ, gloss:elini bütünüyle açıp saçma}, {ar:وَيَقْدِرُ, tr:wa-yaqdiru, gloss:rızkı daraltır}, {ar:فَلَا يُسْرِفْ فِي الْقَتْلِ, tr:fa-lā yusrif fī l-qatli, gloss:öldürmede haddi aşmasın} ve {ar:وَزِنُوا بِالْقِسْطَاسِ الْمُسْتَقِيمِ, tr:wa-zinū bi-l-qisṭāsi l-mustaqīm, gloss:doğru teraziyle tartın} kendi alanlarında ölçünün farklı yönlerini görünür kılar: elin sonuna kadar açılmasıyla rızkın kısılması karşıt uçlardadır; cana kıyma ve tartı da kendi hükümlerini korur. Bu örnekler odak ayetin erken sınır temasına ışık tutar, ayrı hükümleri tek bir kurala dönüştürmez.

Gerekçedeki ikinci {ar:وَ, tr:wa, gloss:ve}, ilkine eşit ağırlıkta yeni bir yargı açar: {ar:فَٰحِشَةًۭ, tr:fāḥishatan, gloss:ağır çirkinlik} eylemi sınıflandırır, {ar:وَسَآءَ سَبِيلًۭا, tr:wa-sāʾa sabīlan, gloss:ne kötü bir yoldur} ise onun gidişini yargılar. {ar:إِنَّهُۥ, tr:innahu, gloss:kuşkusuz o} iki yüklemi birlikte gerekçe yapar; biri ötekinin yerine geçmez ve sıraları bir doğruluk derecesi bildirmez. Başka bir yasak cinsel ilişkinin de çirkinlik ve kötü yol diye nitelenmesi (4:22), bu ikili yargının eylemi sınıflandırma ve gidişi değerlendirme işlevini aydınlatır. Bu paralellik yalnızca yargıların işleyişini karşılaştırır: iki ilişkiyi özdeşleştirmez ve yaklaşmama buyruğunu 4:22’ye taşımaz.

{ar:سَآءَ, tr:sāʾa, gloss:kötü diye yermek} burada birinci bâbın geçmiş biçimiyle kurulan kalıplaşmış “ne kötü!” yergisidir. Fiil hükmü yerleşik bir değerlendirme gibi verir; gizli tekil öznesi {ar:إِنَّهُۥ, tr:innahu, gloss:kuşkusuz o} ve {ar:كَانَ, tr:kāna, gloss:olmak} ile sürdürülen konuya döner, yeni bir insan failini ya da ona yönelen zararı anlatmaz. {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol}, mansup tamyīz olarak “ne yönden kötü?” sorusunu yanıtlar ve belirli bir güzergâhtan çok kötü bulunan gidiş türünü niteler. Bu tekil-belirsiz niteleme başka yollarla teolojik bir karşılaştırma kurmaz.

Sabīlanın yürünebilir yol anlamı, {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşmak} fiilinin verdiği yönü {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki}nin hedefiyle buluşturur; böylece eylem ilerlenebilir bir güzergâh gibi görünür. Yöntem anlamıysa aynı eyleme götüren gidiş biçimini ve ayetin son yargısını öne çıkarır. İki katkı birlikte yaklaşma, hedef ve değerlendirme ilişkisini kurar; bu imge gerçek bir yolculuk ya da belirli bir zarar ve ön davranışlar listesi ileri sürmez.

İki yargının ses örgüsü yerel bir kapanış kurar: {ar:فَٰحِشَةًۭ, tr:fāḥishatan, gloss:ağır çirkinlik} ile sondaki {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol}, belirsiz-mansup bitişleriyle birbirine karşılık verir. {ar:سَآءَ, tr:sāʾa, gloss:ne kötü!} içindeki uzun ā ve hemze değerlendirmeyi bir an askıda duyurur; hemen ardından gelen sabīlan hem kötü bulunan yönü belirtir hem yargıyı çözer. Böylece son kelime buyrukla iki gerekçeyi aynı ses inişinde toplar. Bu ses katkısı ayetin yerel örgüsüne aittir; daha geniş bir ses düzeni ya da dışarıdaki yol imgeleri bu okumayı kurmaz.

Aynı kök ailesindeki ayrı bir isim örtülmesi beklenen mahrem bedensel bölgeyi adlandırır; 17:32’de ise bu isim değil, {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol}ı yargılayan çekimli {ar:سَآءَ, tr:sāʾa, gloss:kötü diye yermek} fiili kullanılır. Bu ayrım, beden anlamını fiilin sözlük anlamına taşımaz. Bununla birlikte {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşmak}ın temas eşiği ve {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki}nın cinsel hedefi, saklı mahremiyet anlamını {ar:فَٰحِشَةًۭ, tr:fāḥishatan, gloss:ağır çirkinlik}nin görünür ve ağır ihlal niteliğinin yanına getirir. Bu keşifsel kök çağrışımı mahremiyet ile ihlali karşı karşıya koyar; gerçek bir açığa çıkma ya da kamusal ifşa anlatmaz.

Aynı surede yetim malı için de “yaklaşmayın” buyruğu kullanılır (17:34): {ar:وَلَا تَقْرَبُوا مَالَ الْيَتِيمِ, tr:wa-lā taqrabū māla l-yatīmi, gloss:yetimin malına yaklaşmayın} denir ve {ar:إِلَّا بِالَّتِي هِيَ أَحْسَنُ, tr:illā bi-llatī hiya aḥsanu, gloss:ancak en güzel biçimde} koşulu yalnız o malı gözeten hükme eklenir. Aynı yaklaşma fiili, cinsel eylemle mal erişimini eşitlemeden, korunan hakka müdahale başlamadan önce işleyen bir sınırı görünür kılar; bu istisna 17:32’ye taşınmaz. Yakın dizide haksız yere cana kıymama ve kısasın sınırı (17:33), tartıda adalet (17:35), bilgin olunmayanın ardına düşmeme (17:36), kibirle yürümeme (17:37) ve toplu bir değer yargısı (17:38) da kendi koruma ve ölçü alanlarını açar.

Ebeveyne yönelen merhametli yakınlık, odaktaki yaklaşma yasağının yanında olumlu bir karşılık sunar: alçak gönüllülük kanadını indirme imgesi (17:24), {ar:وَاخْفِضْ لَهُمَا جَنَاحَ الذُّلِّ مِنَ الرَّحْمَةِ, tr:wa-khfiḍ lahumā janāḥa dh-dhulli mina r-raḥmah, gloss:merhametle ikisine alçak gönüllülük kanadını indir} sözleriyle kurulur. Akrabaya hakkını verme buyruğundaki {ar:الْقُرْبَىٰ, tr:al-qurbā, gloss:yakın akrabalık} (17:26) ise soy bağına dayanan hakkı adlandırır. Al-qurbā ile odaktaki {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşmak} aynı yakınlık kök ailesindendir, ancak farklı biçim ve görevlerdedir; bu kök yankısı akrabalık hakkını yaklaşma fiilinin eşanlamlısı yapmaz. Ebeveyne merhamet, akrabaya hak ve yetimin malını gözetme (17:34), yakınlığın ilişkiye ve korunan menfaate göre ayarlanabileceği okumasını destekler. Yetim kırılganlığı bu bağlamdan çıkarılan bir atıftır; ayrı hak hükümleri okuması da geçerliliğini korur.

Başka ayetlerde yaklaşma farklı hedef ve şartlarla olumlu ya da sınırlı bir yöneliş olarak belirir: cinsel ilişkiye yaklaşma adet döneminde kısıtlanıp sonrasında izin görür (2:222), yetim malına ancak en iyi biçimde yaklaşılır (6:152), secdeden sonra yaklaşma olumlu biçimde buyurulur (96:19). Bu çeşitlilik, yaklaşmanın değerini nesne ve koşulun belirlediğini gösterir. Karşılaştırma bu bağlamlarla sınırlıdır: oradaki şartlar 17:32’ye istisna oluşturmaz, secde yakınlığı cinsel değildir ve morfolojik çözümleme verilmediğinden buradan ortak kök özdeşliği çıkarılmaz.

Yaklaşma eşiği, farklı bağlamlardaki öncesi ve sınır imgelerini yan yana okumayı sağlar. Çirkinliğe götüren adımlar eyleme giden hareketi görünür kılar (24:21); açık ve gizli çirkinliklere yaklaşmama bir sınır çizer (6:151); bakışı indirme ve iffeti koruma bedensel dikkati düzenler (24:30, 24:31); arzuyu kışkırtabilecek söyleyişten sakınma ise sözü gözetir (33:32). Vahiy yerine başka söz konması baskısı altındaki eşik, tavize yaklaşmayı düşündürür (17:73, 17:74); kibirle yürüme yasağına da ayrı bir bedensel hareket aittir (17:37). Bu imgeler 17:32’deki yaklaşma eşiğine farklı katkılar sunar, ancak her ayetin kendi fiili ve gerekçesi korunur: bunlar zinanın başka adları ya da buyruklar arasında ileri sürülmüş ortak kök bağlantıları değildir.

Ebeveyne iyilik (17:23), akrabanın hakkı (17:26), çocukları koruma (17:31), yetim malını gözetme ve ahde vefa (17:34) yol imgesine tek karşılaşmayı aşan bakım sürekliliği boyutu ekler. Bu haklar ebeveynden akrabalığa, çocuklara ve yetime uzanır; sabīlan bu bağlamda gözetim zincirinde olası bir kopuşu düşündürebilir. Bu, ayetlerin komşuluğundan doğan ve nedensellik ileri sürmeyen bir okumadır: çocukların anılması her olayda çocuk doğduğu, yetimlik ya da ahit kopuşu yaşandığı anlamına gelmez. Hakları ayrı ayrı sıralayan katalog okuması da korunur.

Fāḥishanın sözlü kullanım alanı da aileye dönük sınırlarla ayrı bir yankı kurar. Ebeveyne “uff” demek ve onları azarlamak yasaklanır (17:23): {ar:فَلَا تَقُلْ لَهُمَا أُفٍّ وَلَا تَنْهَرْهُمَا, tr:fa-lā taqul lahumā uffin wa-lā tanharhumā, gloss:ikisine uff deme ve onları azarlama}. Sövmek, incitici söz ve utanmazca konuşma yönü, cinsel sınırın yanına sözlü incitme temasını getirerek iki ayrı korunan alanı aynı ahlaki çevrede duyurur. Bu sözlü yankı 17:23’teki hitabı fāḥisha diye sınıflandırmaz ya da onu zinayla özdeşleştirmez; bağlantının kapsamı ortak ahlaki alandır.

Saçıp savurma dili bakım imgesine ayrı, maddi bir yankı ekler: harcayıp dağıtma yasağı ve savurganlar adı (17:26, 17:27) {ar:وَلَا تُبَذِّرْ تَبْذِيرًا, tr:wa-lā tubadhdhir tabdhīran, gloss:saçıp savurma} ve {ar:الْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:savurgunlar} biçimlerinde geçer. Bu kullanımlardan doğan tohum saçılması imgesi, odaktaki cinsel eylem ve sonuç taşıyabilen sabīlanı, yakın bağlamdaki çocukların korunmasıyla (17:31), {ar:أَوْلَادَكُمْ, tr:awlāda-kum, gloss:çocuklarınız} sözüyle buluşturur; böylece üretkenliğin bakım yapılarından uzağa dağılması keşifsel bir benzetme olarak belirir. Bu bağ, etimoloji ya da nedensellik iddiası değildir: zinayı savurganlıkla özdeşleştirmez ve her olayda çocuk, kaynak israfı ya da bakım aksaması bulunduğunu ileri sürmez.

Sabīlanın güzergâh imgesi aynı surede üç ayrı katkıyla genişler (17:35, 17:36, 17:37): sonuç ifadesi olası bir varış noktası verir (17:35), bilgin olunmayanın ardına düşmeme buyruğundaki {ar:وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِ عِلْمٌ, tr:wa-lā taqfu mā laysa laka bihi ʿilm, gloss:hakkında bilgin olmayan şeyin ardına düşme} iz sürme imgesi ilk işaretle sonraki hareket arasında bir bağ düşündürür (17:36), kibirle yürüme yasağıysa bedenin güzergâhtaki devamını görünür kılar (17:37). 17:35’teki bir sözcük için önerilen alternatif eşleme sonucu ardışık bir basamak gibi duyurabilir; 17:36’daki sözcüğün alternatif eşlemesi de iz ile hareket arasındaki bağı yalnızca yorum düzeyinde destekler. Bu eşlemeler olasılıktır; varış, iz ve yürüyüş imgeleri güzergâhı ayrıntılandırsa da buyrukları tek bir kronolojik sürecin aşamaları hâline getirmez. Böyle bir okuma, bedensel devam başlamadan önce gidişin kesilebilmesini de açık tutar.

İşitme, görme ve kalp güzergâh imgesine olası bir dikkat ve duygu başlangıcı ekler. Hesabı verilecek yetiler olarak anılan {ar:السَّمْعَ, tr:as-samʿa, gloss:işitme}, {ar:الْبَصَرَ, tr:al-baṣara, gloss:görme} ve {ar:الْفُؤَادَ, tr:al-fuʾāda, gloss:kalp} (17:36), keşifsel okumada bedensel yaklaşımdan önceki dikkat kanalları gibi düşünülebilir; kalbe atfedilen iç ısınma da duygusal bir evre katar. Bu yorum arzuyu ayette açıkça sıralanmış bir aşama yapmaz; yetilerin hesabının verilmesi bağımsız bir buyruk olarak da anlamını korur.

Toplu değerlendirme, odaktaki iki hükme ortak bir değer yankısı verir: davranışların kötü yanı ve hoş görülmeyen niteliği anılır (17:38), {ar:سَيِّئُهُ, tr:sayyiʾuhu, gloss:kötü olanı} ve {ar:مَكْرُوهًا, tr:makrūhan, gloss:hoş görülmeyeni}. Makrūhan, odaktaki kötü yol ve ağır çirkinlik yargılarının istenmeyen değerini pekiştirir; ölçü aşımı dalını ayrıca adlandırmaz. Hikmet çerçevesi (17:39), {ar:مِنَ الْحِكْمَةِ, tr:mina l-ḥikmah, gloss:bilgelikten} yasağı erken müdahale eden, önleyici ya da düzeltici bir koruma kuralı olarak okumaya imkân verir. Bu, bağlamdan çıkarılan bir işlev yorumudur, hikmet sözcüğünün sözlük anlamı ya da ayetler arasında aynı mekanizmanın işlediği iddiası değil. Kāna’nın 17:38’de yinelenmesi niteliği yeniden işittirir, ancak zaman yorumunu tek başına belirlemez.

Fāḥisha kategorisi toplumsal düzeyde meşrulaştırma ve yayılma arzusuyla da yankılanır: miras alınmış bir uygulamanın Allah’ın buyruğu olduğu iddiası reddedilir (7:28), müminler arasında bu tür çirkinliğin yayılması arzulanır (24:19). Bu iki sahne kategorinin toplumsal dolaşımına katkı sunar; 7:28’de davranış belirtilmez, 24:19’daki çirkinlik de odak ayetin {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki} diye adlandırdığı eylem olarak tanımlanmaz. Dolayısıyla bu yankı bir konuşma yasağı değil, kategori düzeyinde bir bağlantıdır.

İhlalden sonra dönüş imkânı, önleme buyruğunun ciddiyetiyle birlikte görünür kalır: fāḥisha işleyen ya da kendine haksızlık eden kişiler Allah’ı anar, bağışlanma diler ve yaptıklarında ısrar etmez (3:135). Bu sahne ahlaki yola geri dönüşü ekler; fāḥisha burada genel addır, özellikle odaktaki {ar:ٱلزِّنَىٰٓ, tr:az-zinā, gloss:evlilik bağı dışındaki cinsel ilişki} diye tanımlanmaz ve ayetler arasında bir hukukî sıra kurmaz.

Yol kesme imgesi, sabīlanın toplumsal ölçekteki olası yankısını açar: başka bir cinsel davranış, yol kesme ve kamusal kötülük yan yana anılır (29:29). Yol kesme kötü güzergâh yargısına bireysel gidişin ötesinde toplumsal bir boyut katabilir; kamusal kötülük sahnenin kamusal niteliğini, cinsel davranış ise ayrı bir eylemi belirtir. Bu bağlantı ihtimallidir, çünkü yol kesmenin anlamı ve hedef biçimlerin morfolojisi burada belirlenmemiştir; üç eylem ayrı durur ve cinsel davranış odaktaki zinā değildir.

Dosdoğru yola yönelme duası, kötü güzergâh yargısına olumlu bir karşılık verir (1:6): {ar:اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ, tr:ihdinā ṣ-ṣirāṭa l-mustaqīm, gloss:bizi dosdoğru yola ilet} etkin bir hidayet dileğidir. İki ifade arasındaki karşıtlık yol imgesinde kurulur; bu bağlantı ortak kök ya da doğrudan gönderme iddiası taşımaz. Karşıtlık 1:6’daki sözle sınırlıdır: zina orada anılmaz ve buradan Fâtiha’nın tamamına tema genellenmez.

</source_prose>
