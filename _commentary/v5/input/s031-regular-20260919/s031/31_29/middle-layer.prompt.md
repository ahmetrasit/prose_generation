# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:29**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.middle.claims.json`

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
- Refer to source paragraphs as `31:29 ¶N`.

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

`(31:29 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:29",
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
        "citation": "(31:29 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_29/31_29.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_29/31_29.middle.claims.json \
  --ayah-ref 31:29
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_29/31_29.prose.editorial.tr.md`

<source_prose>
31:29 muhatabına “Görmez misin?” diye seslenir: Allah geceyi gündüze, gündüzü geceye geçirir; güneşle ayı yönetir ve her birini belirlenmiş bir süreye doğru akıtır. Ardından aynı hitap insanın yaptığı işi de önüne getirir. Göklerde görünen düzen ile insan eylemi, farklı içerikleri korunarak tek tanıma çağrısında buluşur.

## Görme çağrısı ve iki bildirim

{ar:أَلَمْ تَرَ, tr:a-lam tara, gloss:Görmez misin?} tekil muhataba yönelen bir sorudur. Başındaki {ar:لَمْ, tr:lam, gloss:-medi mi?} olumsuzluğu, sonu zayıf olan ikinci tekil {ar:تَرَ, tr:tara, gloss:görmek} fiilini cezm eder ve zayıf son harfi düşürür. Bu kesik biçim soyut bir gözlemden çok doğrudan bir çağrı kurar: muhataptan önündeki düzene bakması ve onu tanıması istenir. {ar:تَرَ, tr:tara, gloss:görmek} gözle algılamayı korurken görülenler üzerinde düşünüp bir yargıya varmayı da taşıyabilir; gece-gündüz çevrimiyle gök cisimlerinin hareketi bu tefekkürlü bakışın görünür malzemesidir. Buradaki görme çağrısı gözlem ve kavrayışı birlikte taşır; rüya anlamını gerektiren bir uyku bağlamı yoktur.

Bu çağrının hemen öncesindeki 31:25’te gökleri ve yeri kimin yarattığı sorulur, “Allah” cevabı verilir ve insanların çoğunun bilmediği söylenir. Bu cevapla bilmezlik arasındaki açıklık, 31:29’daki {ar:تَرَ, tr:tara, gloss:görmek} sorusunu bilinen cevabı yinelemekten çıkarıp gece-gündüzün ve gök cisimlerinin göz önündeki akışına dikkat kesilme çağrısına dönüştürür. 31:25’in bilmezliği bu döngülere özgü bir bilgisizlik olarak sınırlandırmaz ve konuşanları Yaratıcı’yı inkâr edenler diye tanımlamaz. Böylece doğrudan görme anlamı korunurken bakış, görülen düzenden sonuç çıkarmaya doğru genişler.

İlk {ar:أَنَّ, tr:anna, gloss:ki} görme çağrısının ardından kozmik eylemleri bildiren önermeyi açar; {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} bu yapıda edatın mansub ismidir ve gece-gündüzü geçiren, güneşle ayı yönelten eylemlerin açıkça adlandırılan failidir. Ardından gelen {ar:وَأَنَّ, tr:wa-anna, gloss:ve ki} aynı hitaba insan fiilleri hakkında ikinci bir bildirim ekler. Burada da {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} edatın ismidir; bu kez {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} yüklemi insan işlerini uzmanlıkla bildiğini söyler. İki önerme aynı görme çağrısı altında eşit yapısal ağırlık taşır; göksel işleyiş ile insanın yaptığı işler tek bakışta tutulurken kendi ayrı içeriklerini korur.

## Zamanın birbirine girişi ve gök cisimlerinin seyri

İlk önerme iki eşleşmiş Form IV fiille açılır: {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} önce geceyi gündüze geçirir; ilk kullanımda {ar:ٱلَّيْلَ, tr:al-layla, gloss:geceyi} nesne, {ar:فِي, tr:fī, gloss:içine} sonrasındaki {ar:ٱلنَّهَارِ, tr:al-nahāri, gloss:gündüzün} ise hedef alandır. Aynı fiilin {ar:وَيُولِجُ, tr:wa-yūliju, gloss:ve içeri sokar} diye yinelenmesi rolleri tersine çevirir: bu kez {ar:ٱلنَّهَارَ, tr:al-nahāra, gloss:gündüzü} nesne, {ar:فِي ٱلَّيْلِ, tr:fī al-layli, gloss:gecenin içine} alıcı alandır. İsimlerin nesne ve hedef görevlerini değiş tokuş etmesi, iki dönemin yalnızca sırayla yer değiştirmesinden daha belirgin bir iç-alan ilişkisi kurar. Ettirgen fiil, içeri girme ile Allah’ın bir evreyi ötekinin içine sokmasını aynı örüntüde buluşturur; tekrarlanan şimdiki-geniş zaman biçimi bu geçişi süren bir düzen olarak duyurur. İkinci cümle başındaki {ar:وَ, tr:wa, gloss:ve} ilkini açıklamaz, ters yönü ona dengeli biçimde bağlar. Bu nedenle iç-alan ilişkisi zaman evreleri düzeyinde işler: gece ve gündüz olağan zaman dilimleri olarak kalır, fiil fiziksel bir kap anlatmaz.

Bu geçişte {ar:ٱلَّيْلَ, tr:al-layla, gloss:gece} gündüzün karşıtı olan karanlık dönemi anlatır; sağlanan kullanımın örtülülük dokusu da gündüzün ışığı ve karşılıklı girişle belirginleşir. Gece adının kök çağrışımına ilişkin belirsizlik açık kalır. {ar:ٱلنَّهَارِ, tr:al-nahāri, gloss:gündüz} şafaktan gün batımına uzanan aydınlık süredir. Gündüz adının bağlı olduğu kelime ailesindeki “açma, açıklığı genişletme” kullanımı, karşılıklı roller ve Hac 22:61’deki yinelenişle etkinleşir; sınırın ötekine açıldığı imgesini eklerken gündüzün olağan zaman anlamını korur. Bu kök çağrışımı gündüzü fiziksel bir kapı ya da açıklık gibi kurmaz.

Hac 22:61’deki karşılıklı giriş ile Zümer 39:5’in geceyi ve gündüzü birbirinin üzerine sarar gibi anlatması, bu iki dönemin sürelerinin de ötekine doğru uzandığını farklı uzamsal ilişkilerle düşündürür. Her biri bir cümlede giren, ötekinde içine girilen evredir; böylece geçiş, yalnızca iki kapalı zaman aralığının sırayla değişmesi değil, karşılıklı iç içe uzamadır. Hac 22:61 ve Zümer 39:5 bu uzamanın hızını ya da ölçüsünü vermez. Zümer 39:5’te güneşle ayın {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre}ye doğru akması, bu açılıp uzanan döngüyü ayrıca belirlenmiş bir sınır içinde tutar; sınır giriş fiilinin yerini almaz ve bir takvim ya da fiziksel mekanizma kurmaz.

İki giriş fiilinden sonra {ar:وَسَخَّرَ, tr:wa-sakhkhara, gloss:ve boyun eğdirdi} anlatımın yönünü değiştirir. Şimdiki-geniş zamanlı biçimler süren geçişi anlatırken mâzî biçimindeki Form II {ar:سَخَّرَ, tr:sakhkhara, gloss:boyun eğdirip yöneltti} gök cisimleri üzerinde kurulan yönetimi bildirir. Belirtili ve mansub {ar:ٱلشَّمْسَ, tr:al-shamsa, gloss:güneşi} ile bağlaçla aynı fiile eklenen {ar:ٱلْقَمَرَ, tr:al-qamara, gloss:ayı} iki ayrı nesnedir; tek yöneltme ikisini de kapsar. Allah adı tekrar yazılmasa da eylemlerin faili olarak sürer, araya yeni bir fail girmez. Bu gök çiftinde fiilin amaçlı yöneltme ve hizmete bağlama anlamı öne çıkar; daha sert kullanım kolundaki zorla belirli işe sevk çağrışımı da bu yöneltilmiş hizmetin niteliğini duyurabilir. Alay etme anlamıysa bu nesne ve fiil yapısına uymaz.

Güneş, görünen diski, ışığı ve ısısıyla bu yönetilen düzenin parlak öğesidir. Ay ise ayrı bir gök cismi olarak kalır; güneşle karşıtlığı ay ışığını ve onun aydınlattığı geceyi de çağırabilir. Böylece ortak yönetim, güneşin ışık ve ısısını ayın ayrı ışık taşıyan varlığıyla yan yana getirir. Kumara ya da kar körlüğüne ilişkin kullanımlar bu bağlamda etkin değildir; ifade yerel gök çiftini kurar ve benzer söyleyiş kalıpları tek başına daha geniş bir dağılım göstermez.

Yaratıcıyı başkalarından ayıran {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} özel adı, güneşle ay üzerindeki yönetim eylemiyle yerel bir egemenlik çağrışımı kazanır; bu anlam adın kökeninden değil, izleyen fiille kurduğu ilişkiden doğar. Hemen ardından 31:30 göksel düzeni Allah’ın hak oluşu ve O’ndan başka çağrılanların bâtıllığıyla yan yana getirerek görünen nizamın işaret değerini genişletir. Bu bağlam, işaret okumasını Allah’a yöneltir; 31:30 güneşle ayı özellikle bâtıl çağrıların nesnesi diye adlandırmaz, dolayısıyla odaktaki gönderimleri gök cisimleri olarak sürer.

Yönetilen bu çiftin ardından gelen {ar:كُلٌّ, tr:kullun, gloss:her biri} merfû tekil ismi yeni bir isim cümlesi açar; tekil {ar:يَجْرِي, tr:yajrī, gloss:akar veya ilerler} yüklemi güneşle ayın her birine ayrı ayrı dağılır. Böylece boyun eğdirme ile hareket birlikte görünür: her cisim kendi yolunu sürdürür, ikisi tek bir varlıkta erimez. Geçişsiz fiilin anlattığı seyir, önceki yönetim altında sürer ve bağımsız iradeye değil yöneltilmiş harekete karşılık gelir. {ar:كُلٌّ, tr:kullun, gloss:her biri}nin bu cümledeki kapsamı hemen önceki güneş-ay çiftiyle sınırlıdır; her iki cismi ayrı ayrı rotaya bağlar.

Râ‘d 13:2 aynı güneş-ay çiftini, onların yönetilmesini ve her birinin {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre}ye kadar akmasını birlikte anarak buyruğa bağlı hareketin sürekliliğini gösterir. {ar:يَجْرِي, tr:yajrī, gloss:akar veya ilerler} yol boyunca sürme anlamını korur; su ve rüzgâr akabilir, at koşabilir, gök cismi ya da gemi izlediği yolda ilerleyebilir. Bu kullanımların ortak noktası belirli güzergâhta devam eden harekettir. Râ‘d 13:2’de yinelenen seyir, kök ailesindeki “alışılmış davranış yolu” çağrışımını sınırlı biçimde devreye sokar: tekrar düzenlilik hissi kazandırır. Bu düzenlilik benzetmesi insan alışkanlığı, niyeti ya da seçimini gök cisimlerine yüklemez; Râ‘d 13:2 de hareketin fiziksel işleyişini açıklamaz.

Bu seyrin yönünü {ar:إِلَىٰ, tr:ilā, gloss:…e doğru} öbeği belirler: her biri {ar:أَجَلٍ مُسَمًّى, tr:ajalin musammā, gloss:belirlenmiş bir süreye} doğru ilerler. {ar:أَجَلٍ, tr:ajalin, gloss:süre ve son sınır}, edattan sonra mecrur gelerek yönelinen bitişi adlandırır; {ar:مُّسَمًّى, tr:musammā, gloss:adlandırılmış ve belirlenmiş} edilgen ortaç bu hedefin tayin edilmiş olduğunu bildirir. Böylece her rota belirli bir sınıra sahiptir, takvimdeki kesin tarih ise söylenmez. Ortaç adlandıranı dilbilgisel olarak belirtmez; yakın cümlede Allah’ın kozmik fiillerin faili oluşu ilahî belirleyeni mümkün kılar, fakat bu fail ortaçta açıkça kurulmaz.

{ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre ve son sınır}ın farklı kullanımları bu terimin göksel, kişisel ve sözleşmesel bağlamlarda sabit bir sonu nasıl taşıdığını gösterir. Zümer 39:5 ve Rûm 30:8 süreyi kozmik ve yaratılmış düzen içinde anar; Münâfikûn 63:11 vade geldiğinde hiçbir canın ertelenmeyeceğini bildirir. Bakara 2:282’de borç vadesinin yazılıp tanıklanması, belirlenmiş bir sürenin bilinebildiği ve kayda geçirilebildiği bir örnektir. Bu çeşitlilik, her ecelin insanlarca bilinemez olduğu biçimindeki genellemeyi dışarıda bırakır; 31:29’un güneşle ay için bildirdiği belirlenmiş sona karşılık kesin gün yine açıklanmaz.

“Adı konmuş” okuması korunurken, {ar:مُّسَمًّى, tr:musammā, gloss:adlandırılmış} için sağlanan daha uzak fiziksel iz koyma kullanımı da bir işaret çağrışımı açar. {ar:أَلَمْ تَرَ, tr:a-lam tara, gloss:Görmez misin?} görme çağrısı, görünür gök düzeni ve {ar:أَجَلٍ, tr:ajalin, gloss:süre} sınırı birlikte düşünüldüğünde, belirlenmiş son okunabilir bir işaret gibi duyulur. Bu imge tayin edilmiş sınırın seçilebilirliğini güçlendirir; fiziksel bir iz ya da takvim tarihi iddiası taşımaz. Nitelemenin temel karşılığı yine adlandırılmış süredir.

31:27 ve 31:28’in genişlik tasvirleri, her gök cisminin sonlu kursunu daha büyük bir kudret ufku içinde görünür kılar. 31:27’de yeryüzündeki ağaçlar kalem, deniz mürekkep olsa ve ardından yedi deniz daha eklense bile {ar:كَلِمَاتُ اللَّهِ, tr:kalimātu llāh, gloss:Allah’ın sözleri} tükenmez; denizlerin çoğalması, yazı araçlarının sınırsızlaşması ve anlamlı içeriğin eksilmemesi aynı imgeyi kurar. 31:28’de insanları yaratmak ve diriltmek {ar:كَنَفْسٍ وَاحِدَةٍ, tr:ka-nafsin wāḥidah, gloss:tek bir can gibi}dir. Bu iki bağlam, 31:29’daki göksel kursların sınırını korurken ilahî sözleri ve yeniden yaratma kudretini ölçülemez bırakır; genişlik süre sözcüğünü sonsuzlaştırmaz.

Gök cisminin rotası, 31:31 ve 31:32’deki deniz yolculuğuyla varış fikri bakımından buluşur. 31:31’de Allah’ın lütfuyla gemi kıyıdan uzak, engin ve derin denizde ilerler; 31:32’de yükselen dalgalar yolcuları gölgelikler gibi örter, onlar Allah’a yönelir ve kurtarıldıklarında karaya ulaşırlar. Açık denizdeki yolun kuşatılma, sığınma, kurtuluş ve kıyıya varışa dönüşmesi, {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre}ye yönelen göksel seyri bir varış rotası gibi düşündürür. Câsiye 45:12’de aynı hareket kökünün başka bir çekimi, Allah’ın buyruğuyla denizde ilerleyen ve insanların O’nun nimetini aradığı gemileri anlatır; iki metni bağlayan yöneltilmiş güzergâhtır. Bu bağlantı 31:29’a deniz, dalga, kıyı ya da yolcu kırılganlığını taşımaz; gemi hareketi {ar:سَخَّرَ, tr:sakhkhara, gloss:boyun eğdirip yöneltti} ile biçimbilimsel olarak da eşleşmez.

{ar:تَرَ, tr:tara, gloss:görmek} çağrısı ile {ar:ٱلشَّمْسَ, tr:al-shamsa, gloss:güneş} ve {ar:ٱلْقَمَرَ, tr:al-qamara, gloss:ay}ın görünür seyri, En‘âm 6:76, 6:77 ve 6:78’de İbrahim’in yıldızı, ayı ve güneşi görüp batışlarına tanık olduğu sahneyle yankılanır. En‘âm 6:78’de güneş batınca İbrahim ortak koşmayı reddeder; bu sahne parlak görünmenin kalıcı egemenlik anlamına gelmediğini açar. Benzerlik, 31:29’un muhataplarını İbrahim diye tanımlamaz ve onun öyküsünü odak ayete taşımaz. Odaktaki güneş ve ay yönetilen gök cisimleri olarak kalır; karşılaştırma ay ışığı, ay evreleri ya da yeni bir astronomi bilgisi eklemez. En‘âm’daki batış da {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş son sınır} ile özdeş değildir; iki sahne yalnızca görünen hareketin sınırsız olmadığını düşündürür.

## Geçişin başka imgeleri

Deniz yolculuğundan ayrı bu su imgesi, gece-gündüz arasındaki giriş ile gök cisimlerinin yolunu bir araya getirir. Gündüz adının bağlı olduğu kelime ailesindeki taşkın suyu taşıyan, toprağı yararak belirginleşen doğal yatak ya da kanal imgeye bir taşıyıcı hat sağlar. Karşılıklı {ar:يُولِجُ وَيُولِجُ, tr:yūliju wa-yūliju, gloss:içeri sokar ve geçirir} evreleri birbirine alınan akışlar gibi gösterir; {ar:يَجْرِي, tr:yajrī, gloss:akar veya ilerler} bu hatta hareketi verir; {ar:ٱلنَّهَارِ, tr:al-nahāri, gloss:gündüz} kanal, gök cisimleri hat boyunca akanlar, {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre} de akışı toplayan havuz gibi düşünülebilir. Böylece giriş, kanal, akış ve son sınır tek bir hidrolik tasvirde birbirini tamamlar. Tasvir gündüzün aydınlık zaman anlamını ya da gök cisimlerinin gönderimini değiştirmez; zaman dilimleri zaman, cisimler gök cismi olarak kalır.

Lokmân 31:10’daki suyun gökten inişi, yeryüzüne dökülüp taşınması, bitkilerin çıkışı ve eşlenmiş ürünler, kanal imgesine ayrı bir yeryüzü karşılığı verir. Yağan ve taşınan su, karşılıklı girişle kurulan dolaşımın maddesini; yerden çıkan bitkiler ise bu aktarımın dönüşmüş sonucunu gösterir. Bu sahne gündüz adının taşkın su yatağı çağrışımını canlı tutar, fakat 31:10 ile 31:29 iki ayrı işaret dizisi olarak kalır: yağış ve büyüme güneş-ay döngüsünün sonucu diye kurulmaz. Eşlenmiş ürünler de 31:29’daki {ar:كُلٌّ, tr:kullun, gloss:her biri} kapsamına katılmaz; odakta bu kelime yalnızca güneşle ayı ayrı ayrı kapsar.

{ar:مُّسَمًّى, tr:musammā, gloss:adlandırılmış} için verilen daha uzak “dar delik, geçit ya da sığınak” kullanımı süreyi bir eşik imgesine açar. {ar:أَجَلٍ مُسَمًّى, tr:ajalin musammā, gloss:belirlenmiş süre} varışın zaman sınırını, karşılıklı {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} geçide giriş ve {ar:يَجْرِي, tr:yajrī, gloss:ilerler} güzergâh boyunca geçişi sağlar; bu işlemler birlikte her hareketin içinden geçtiği dar bir boğaz resmi kurabilir. Lokmân 31:31 ve 31:32’deki deniz sahnesinde ise yolcular kurtuluşun ardından kıyıya varır; burada imge bir varış sahilinden çok rotanın içinden geçilen dar noktaya odaklanır. Her iki benzetme de süreyi mekânsal olarak düşündürürken, odaktaki ifade belirlenmiş zaman sınırını korur.

Lokmân 31:14’te annenin çocuğu taşıması ve güçsüzlüklerin üst üste gelmesi, içeride olgunlaşan bir süreci kurar; iki yıl bu gelişime ölçü verir, sütten ayırma bir aşamadan ötekine geçişi, Allah’a dönüşe yöneliş ise sonucu belirginleştirir. 31:29’daki {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} ile içeri giriş, {ar:يَجْرِي, tr:yajrī, gloss:ilerler} ile süren hareket ve {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre} ile konan sınır, bu ölçülü dönüşüme benzetilebilir; 31:14’ün yönelişi imgeye yalnızca süre değil, varış da katar. Bu paralellik biyolojik süreci gece-gündüz çevrimine bağlamaz: iki yıl o çevrimin süresi, güneşle ay da anne ve çocuk değildir. Olgunlaşma odağa ayrı bir sözlük anlamı eklemez.

## İnsan işi ve iç yüzü bilen

İkinci önermede öne alınan {ar:بِمَا, tr:bi-mā, gloss:yaptıklarınız hakkında} öbeği, Allah’ın bilgisinin konusu olan insan işini yüklemden önce görünür kılar. Buradaki {ar:بِ, tr:bi, gloss:hakkında} uzman bilginin alanını açar; bilgiyi edinmenin aracı değildir. {ar:مَا, tr:mā, gloss:ne veya şey} yapılan işler anlamında ilgi zamiri ya da yapma faaliyeti anlamında mastar olarak okunabilir. Her iki çözümleme de aynı alanda kalır: biri yapılanları, öteki yapma eylemini öne çıkarır; ayet bu ikisinden birini seçmez.

Kozmik eylemler üçüncü kişiyle anlatıldıktan sonra {ar:تَعْمَلُونَ, tr:taʿmalūna, gloss:yapıyorsunuz} ikinci çoğul kişiye döner ve muhatapları doğrudan hitaba alır. Form I’de bu fiil yapmak ve işlemek demektir; biçim ettirme ya da karşılıklı işlem anlamı taşımaz. Kök ailesindeki amaçlı iş ve bilinçli eylem tonu, yapılanların muhataba isnat edilebilir oluşunu duyurur; ayet tek bir eylemi seçip değer biçmez. Sağlanan {ar:يَعْمَلُونَ, tr:yaʿmalūna, gloss:yapıyorlar} kıraati ise üçüncü kişiyi bildirir ve işleri muhataplar hakkında anlatır. Böylece iki şahıs biçimi aynı eylem alanını farklı muhatap ilişkileriyle taşır; biri ötekine üstün tutulmaz.

Yapma fiilinin bağlı olduğu kelime ailesindeki ağır el işi yapan kişi kullanımı, eylem ile onu yapan emekçi arasında bir karşılaştırma açar. 31:29’daki {ar:تَعْمَلُونَ, tr:taʿmalūna, gloss:yapıyorsunuz} ise çekimli bir fiildir; insanları “işçiler” diye adlandıran isim değildir. Bu form farkı benzetmenin sınırını da belirler: gök cisimlerine yöneltilmiş hizmet ile insanın yaptığı işler karşılaştırılır, insanlara belirli bir meslek ya da çalışma koşulu yüklenmez.

İkinci önermenin merfu yüklemi olan {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar}, Allah’ı insan işlerinin faili değil, o işleri bilen olarak sunar ve görme çağrısı altındaki bildirimi tamamlar. Sağlanan kullanımlar bu sıfatın bir işin dış görünüşünün ardındaki niteliği tanımaya, edinilmiş ya da aktarılan bilgiyle derinleşen haberdarlığa uzanabildiğini gösterir. {ar:بِمَا تَعْمَلُونَ, tr:bi-mā taʿmalūna, gloss:yaptıklarınız hakkında} insan işini bu uzmanlığın konusu yapınca bilgi görünen işle birlikte işin iç yüzüne de uzanır. Bu iç bilgi insan gözlemiyle aynı kapsamda değildir; gelecekteki bir raporun zamanı ya da kendisi ise bu sıfatta belirtilmez.

Lokmân 31:16’daki hardal tanesi örneği, uzman bilginin çok küçük ve saklı olana nasıl uzandığını görünür kılar. Bir şey kaya, gökler ya da yer içinde gizli bulunsa bile Allah onu ortaya çıkarır; ayet bunu Allah’ın Latîf ve {ar:خَبِيرٌ, tr:khabīrun, gloss:her şeyden haberdar} oluşuyla ilişkilendirir. Tane küçüktür, kaya büyük ve sert bir direnç oluşturur; gizlilik ile ortaya çıkarılma aynı sahnede karşılaşır. Filizlenmeye hazır tohum da henüz görünür sonuca dönüşmemiş olanı bu imgeye ekler. Bu küçük ve kapalı örnek, 31:29’daki {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} girişiyle {ar:تَعْمَلُونَ, tr:taʿmalūna, gloss:yapıyorsunuz} ve {ar:خَبِيرٌ, tr:khabīrun, gloss:iç yüzünü bilen} kapanışını, gizli eylemin de bilgi ve sorumluluk alanında kalması yönünden aydınlatır. Tohum 31:16’nın örneğinde kalır; güneşle ay onu bulup çıkaran fail olarak gösterilmez.

Lokmân 31:20’de nimetlerin zahir ve bâtın, yani dışarıdan görünen ve içte kalan yönleri anılır; aynı görme kökü orada çoğul çekimle yinelenir. 31:29’daki tekil {ar:تَرَ, tr:tara, gloss:görüp kavra} ile 31:20’deki çoğul biçim aynı hitap değildir; ortaklık, görünen düzenden daha içteki bir boyuta uzanan görme alanındadır. Bu temas görmeyi içtekinin kendiliğinden açığa çıkması gibi değil, görünenin ötesine yönelen bir eşik gibi duyurur. {ar:خَبِيرٌ, tr:khabīrun, gloss:işin iç yüzünü bilen} kapanışı bu eşiği tamamlar: dışarıdan seçilemeyen yön de ilahî bilgi içindedir. 31:20’nin belirli nimetleri odak ayete aktarılmaz; katkısı görünen döngüyü daha geniş düzenin dışa açılan yüzü gibi düşündürmesidir.

Lokmân 31:20, boyun eğdirme ilişkisini güneşle aydan göklerde ve yerde bulunanlara genişletir ve insan için nimet ile fayda çerçevesi kurar. Bu geniş bağlam, 31:29’daki {ar:سَخَّرَ, tr:sakhkhara, gloss:boyun eğdirip yöneltti} fiilini fiziksel yöneltmenin yanında yarar sağlayan bir düzen içinde duyurur. 31:20’deki nimetlerin tam ve kuşatıcı oluşu bu hizmeti bütünlüklü görmeye katkı verir; bu bütünlük sözcüğün 31:29’daki ayrı bir sözlük anlamı değildir. Gök hizmetiyle insan işi aynı hitapta buluşunca bu düzende yaşayanın eylemi de gözetim ufkuna girer.

İnsan işi ikinci önermede belirdiğinde, {ar:سَخَّرَ, tr:sakhkhara, gloss:boyun eğdirip yöneltti} fiilinin daha sert kullanım kolu da yeni bir karşılaştırma açar: amaçlı yöneltmenin yanında, kimi kullanımlarda bir şeyin zorlanarak ya da karşılık almadan hizmete koşulması bulunur. {ar:تَعْمَلُونَ, tr:taʿmalūna, gloss:yapıyorsunuz} insanın yaptığı işi adlandırırken bu kullanım kolu, hizmet alanla işi yapan arasındaki farkı düşündürür. Ağır el işi yapan kişi anlamındaki kök dalı da benzetmeye emekçi yüzü katar. Lokmân 31:20’nin nimet ve yarar çerçevesi gök hizmetini iyilik sağlayan düzen içinde tutar; böylece analoji sorgulayıcı kalırken ilahî sömürü ya da belirli bir çalışma düzeni hakkında hükme dönüşmez. Odak ayetin fiili insanları “işçiler” diye adlandırmaz; {ar:خَبِيرٌ, tr:khabīrun, gloss:işin iç yüzünü bilen} ise insan emeğini bilgi ve sorumluluk ufkunda tutar.

31:29’daki yönetilen gök cisimleri ile insan işi hakkındaki ikinci bildirim aynı görme çağrısı altında buluştuğundan, Nahl 16:12’nin geceyi, gündüzü, güneşi, ayı ve yıldızları buyruğa bağlı işaretler olarak anması kozmik düzenin anlamını genişletir. Bu bağlam, 31:29’daki {ar:سَخَّرَ, tr:sakhkhara, gloss:boyun eğdirip yöneltti} düzenini işaret değeri olan bir hizmet olarak duymaya katkı verir; yöneltmenin fiziksel aracını açıklamaz. Hadîd 57:4’te yere giren ve ondan çıkan, gökten inen ve ona yükselenlerin ardından insanların yaptıklarının görülmesi, insan eylemini bu geniş kozmik bilgi alanına katar; eylemler gök hareketine indirgenmez.

Hadîd 57:6’da geceyle gündüzün {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} fiiliyle birbirine sokulması, göğüslerde saklı olanın bilinmesi sözüne komşudur. Aynı giriş örüntüsü görünen zaman düzenini gizli insan içiyle karşılaştırır; gece-gündüz çevrimi kalbin mecazı yapılmaz. Mücâdele 58:7 gizli konuşmaları ve daha sonra bildirilecek işleri ekleyerek bu karşılaştırmayı davranışın etik boyutuna taşır. Nahl 16:12, Hadîd 57:4, Hadîd 57:6 ve Mücâdele 58:7 birlikte, kozmik hizmetin insan davranışını da kuşatan bir işaret gibi okunmasına imkân verir; gök cisimleri insan gibi işçi olmaz ve odak ayete ayrıca hesap bildiren bir fiil eklenmez.

Lokmân 31:15 ve 31:23’te insanın Allah’a dönüşü, yapılanların bildirilmesi ve işlerin içeriği iki ayrı dizide yinelenir; 31:23 göğüslerin içindekini de anar. En‘âm 6:60’ta gece, gündüz yapılan işler, belirlenmiş süre, dönüş ve amellerin bildirimi art arda gelir; Mücâdele 58:7 de gizli konuşma ile ilahî bilgiyi işlerin daha sonra bildirilmesine bağlar. Bu diziler, odaktaki bilinen işten dönüş ve açıklanmaya uzanan bir güzergâhı düşündürür: {ar:يَجْرِي, tr:yajrī, gloss:ilerler} yol imgesi, {ar:تَعْمَلُونَ, tr:taʿmalūna, gloss:yaptıklarınız} eylemi, {ar:خَبِيرٌ, tr:khabīrun, gloss:işin iç yüzünü bilen} ise içeriğin bilinmesini taşır. Bu gelecek bildirim ve dönüş, 31:29’un kendi cümlesinde kurulmaz; odakta sıfat insan eylemine uzman bilgiyi bildirir, “rapor vermek” anlamını taşımaz. Paralellik mümkün bir okuma olarak kalır.

Giriş fiilinin toplumsal yankısı, bir örüntünün ilişkilerin içine alınıp orada yer tutmasıdır. Lokmân 31:20’de güvenilen aile dışı sırdaşların kabulü özel bir iç alan açar; 31:21’de ataların izini sürme bu bağlılığı kuşaklar boyunca yinelenen bir yola çevirir; 31:32’de kurtuluştan sonra beliren vefasızlık ise içeride taşınan bağlılığın davranışta nasıl göründüğünü açığa çıkarır. Bu üç katkı, dışarıdan gelen bir örüntünün toplumsal ilişkilere yerleşmesi imgesini kurar. 31:29’daki {ar:يُولِجُ, tr:yūliju, gloss:içeri sokar} ise gerçek gece-gündüz geçişini anlatmayı sürdürür; insan ilişkileri bu fiilin göndergesi değil, benzetmenin alanıdır. {ar:خَبِيرٌ, tr:khabīrun, gloss:işin iç yüzünü bilen} gizli bağlılık ile görünür davranış arasındaki farkın da bilgi içinde olduğunu düşündürür.

Güneşle ayı ayrı ayrı bir sona bağlayan {ar:كُلٌّ, tr:kullun, gloss:her biri} ve {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre ve son sınır}, Lokmân 31:33’ün kişisel sorumluluk tasviriyle bir benzetme kurar. 31:33’te hiçbir ebeveyn çocuğunun yerine karşılık veremez, çocuk da ebeveyninin yerine geçemez; Allah’ın vaadi gerçektir. Dünya hayatı ile aldatıcı da insanı Allah hakkında yanıltmasın diye uyarılır. Bu karşılaştırma göksel kursun sonluluğuna, en yakın bağın bile başkasının sorumluluğunu üstlenemediği bir hesap ufku ekler. 31:29’un grameri güneşle ayı özne yapmayı sürdürür; insanlara eşit bir süre ya da gemi biçiminde bir yargı yolu atamaz.

Lokmân 31:34 kişisel ufkun sınırını somutlaştırır: hiçbir can yarın ne kazanacağını ya da hangi yerde öleceğini bilmez; Allah ise {ar:خَبِيرٌ, tr:khabīrun, gloss:her şeyden haberdar}dır. 31:29’un görünür döngü içindeki {ar:أَجَلٍ, tr:ajalin, gloss:belirlenmiş süre}si kozmik hareket için bir son tayin ederken, 31:34 insanın kendi geleceğinin tarihi ve yerini kapalı bırakır. Lokmân 31:23’te dönüş, yapılanların bildirimi ve göğüslerin içindekiler bu kişisel bilinmezliğe ayrı bir bağlamdan katılır. Böylece ilahî bilgi görünen işi ve iç yüzünü kuşatırken, insan kendi yarınını ve ölüm yerini öngöremez; göksel süre insanın ölüm vaktiyle özdeşleşmez.

Âyetin sonundaki {ar:خَبِيرٌ بِمَا تَعْمَلُونَ, tr:khabīrun bi-mā taʿmalūna, gloss:yaptıklarınızdan haberdar} ifadesi, görünür kozmik işaretlerden muhatabın yaptığı işin iç yüzüne uzanan bakışı tamamlar. {ar:خَبِيرٌ, tr:khabīrun, gloss:işin iç yüzünü bilen} sözcüğünün başındaki boğazdan gelen hırıltılı ses, uzun ī’si ve ayet sonundaki durak dinleyişe ağırlık verir; bu işitsel katkı sözlük anlamını değiştirmez. Son vurgu, muhatabın işinin hem görünen biçiminin hem iç niteliğinin bilinmesidir.

</source_prose>
