# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:3**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.middle.claims.json`

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
- Refer to source paragraphs as `31:3 ¶N`.

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

`(31:3 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:3",
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
        "citation": "(31:3 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_3/31_3.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_3/31_3.middle.claims.json \
  --ayah-ref 31:3
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_3/31_3.prose.editorial.tr.md`

<source_prose>
## Yazılı çerçeve ve iki işlev

31:2'deki çoğul {ar:ءَايَٰتُ, tr:āyāt, gloss:ayetler} işaretleri, yazılı {ar:ٱلْكِتَٰبِ, tr:el-kitāb, gloss:Kitap} ve hikmetli {ar:ٱلْحَكِيمِ, tr:el-ḥakīm, gloss:bilge} niteliğiyle çerçeveler. Hemen ardından 31:3'te yeni bir açılış bağlacı gelmeden belirsiz mansup {ar:هُدًى, tr:hudā, gloss:yol gösterme} belirir; bu yakın geçiş, hudā'yı Kitapla ilgili sözü sürdüren bir rehberlik niteliği gibi duyurur. Ayrı bir yüklem çözümlemesi de açık kalır; Kitap çerçevesi güçlü bir okuma olsa da tek sözdizimi çözümü değildir.

Belirsiz mastar biçimi, {ar:هُدًى, tr:hudā, gloss:yol gösterme}yı belirli bir kişiye, sınırlı bir nesneye ya da tarihlenmiş olaya ilişkin emir yerine Kitapta süreklilik taşıyan bir kılavuzluk niteliği olarak sunar. Yerel anlam doğru yolu göstermedir; hudā burada Kitabın rehberlik niteliğini adlandırır, bağımsız bir fail oluşturmaz. Bu yakın ayet komşuluğu armağan ya da mabede adak anlamını etkinleştirmez; armağan yüzü daha sonra ayrı bağlamsal dayanaklarla belirginleşir.

31:2'de ayetler zaten işaretlerdir; onları göze çarpan alametler olarak duyuran ek vurgu, 31:3'teki {ar:هُدًى, tr:hudā, gloss:yol gösterme} ile birleşince işaretlerin okurun dikkatini yönlendirmesini düşündürür. {ar:ٱلْكِتَٰبِ, tr:el-kitāb, gloss:Kitap} olağan anlamıyla yazılı metindir; harfleri bir araya getirip yazı ve kitap kurma imgesi de çoğul işaretleri tek bir metinsel bütünde toplar. Peşinden gelen hidayet bu bütüne yön verme işlevi kazandırır; bu bağlamsal imge, Kitap'ın yazılı metin anlamını koruyarak işaretleri bir bütün halinde okumaya açar.

Kitabı niteleyen {ar:ٱلْحَكِيمِ, tr:el-ḥakīm, gloss:bilge} sıfatı öncelikle hikmet ve bilgelik bildirir. Bu kelimeyle ilişkilendirilen yanlış yönü alıkoyup geri çevirerek düzeltme imgesi, yazılı çerçeve ve {ar:هُدًى, tr:hudā, gloss:yol gösterme} ile buluştuğunda rehberliğin düzen kuran yanını belirginleştirir; sağlamlık, tamamlanmışlık ve kesinlik çağrışımları da yönü tutarlı ve güvenilir bir taşıyıcı gibi duyurur. İşaretlerin düzeni, hidayet ile {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in aynı yazılı çerçeveden alıcıya ulaştığı düşüncesini besler. Bu yakınlık, iki niteliğin aynı taşıyıcıda buluştuğu bir okuma imkânı sunar; Kitabın sonuçları mekanik biçimde ürettiği iddiasını değil.

Bu çerçevenin içinde {ar:هُدًى, tr:hudā, gloss:yol gösterme} ile {ar:وَرَحْمَةً, tr:wa-raḥmatan, gloss:ve rahmet} aynı belirsiz mansup mastar biçiminde ve bağlayıcı vavla gelir. Tenvinli sonlar ile vavın kurduğu ses ve dilbilgisi uyumu iki niteliği tek bir akışta duyurur; eşitlikleri her birinin ayrı yararını korur. İçerideki vav rahmeti yeni bir cümle gibi başlatmaz, hidayetin yanına ekler; ayet başında yeni bir açılış bağlacının bulunmamasıyla bu açık iç bağ yan yana duyulur.

Rahmetin de belirsiz mastar oluşu, onu tarihlenmiş bir olay ya da ilahî bir sıfat değil, hidayetle birlikte Kitabın sunduğu ikinci soyut işlev olarak kurar. Ana yüzeydeki mansup {ar:وَرَحْمَةً, tr:wa-raḥmatan, gloss:ve rahmet}, {ar:هُدًى, tr:hudā, gloss:yol gösterme} ile aynı Kitap çerçevesinde eşit düzeyde çalışır. Bildirilen merfu {ar:وَرَحْمَةٌ, tr:wa-raḥmatun, gloss:ve rahmet} biçimi rahmeti ayrı bir yüklem konumuna taşıyabilir; bu, ana okuyuşu düzeltmeden açık tutulan bir karşı imkândır. Şâz diye aktarılan başka bir okumada bu yere rahmet değil müjde gelir; aktarım ana yüzeye karıştırılmaz ve iki ihtimal arasında üstünlük sıralaması yapılmaz.

## Yararın yöneldiği sınıf

İki işlevden sonra gelen {ar:لِّلْمُحْسِنِينَ, tr:li-l-muḥsinīna, gloss:iyilik yapanlar için}, yararın kime ulaştığını belirtir. Önce hidayet ve rahmet tamamlanır, sonra li alıcı sınıfı getirir; bu iki vuruşlu sıra insanları iki yararın somut muhatapları olarak öne çıkarır. Li öbeği en yakındaki rahmete, daha uzaktaki hidayete ya da ikisine birden bağlanabilir; ortak alıcı kapsamı belirgindir, yerel bağlanma noktası açık kalır. Bu özel bağlanma sorusu 31:2'deki Kitap çerçevesini tek başına karara bağlamaz.

{ar:لِّلْمُحْسِنِينَ, tr:li-l-muḥsinīna, gloss:iyilik yapanlar için} edatındaki li, öncelikle {ar:هُدًى, tr:hudā, gloss:yol gösterme} ile {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}i bu sınıfa yarar olarak yöneltir. Bağın alıcı, uygunluk ya da sınıfı kuran ilişki şeklinde açıklanması açık kalır; sahiplik ve amaç da ikincil renkler olarak mümkündür. Yazı ve okuyuşta li, belirli artikel al- ve isim tek biçimde kaynaşsa da edatın, artikelin ve ismin ayrı dilbilgisel görevleri sürer. Birleşik ses akışı iki niteliğin ortak yönelişini duyurur; bu ses akışı tek bir sözdizimi çözümlemesini zorunlu kılmaz.

Li'den sonra gelen {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} genitif çoğuldur; dördüncü bâbın etken ortaç kalıbı, iyi işi yapan ve iyiliği gerçekleştirenleri eylem içinde adlandırır. Belirli artikel, üyeleri kapalı bir liste halinde saymadan tanınabilir bir ahlaki sınıf kurar. Bu anlam edilgin bir övgüye, yalnız estetik beğeniye ya da karşılıklı iyilik anlatısına indirgenmez; cümledeki li öbeği bu etkin sınıfı yararın alıcısı olarak konumlandırır. Ortaç eylem anlamını korur, okura ise bu sınıfa dönüş diye yeni bir buyruk vermez.

Ayetin iki soyut işlevden sonra {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} sınıfına varması, rehberlik ve rahmeti insan muhataplarına bağlar; etken adlandırma onların kendi eylemini korurken cümlede bu niteliklerin üreticisi değil yararın alıcısı olduklarını gösterir. Eril genitif çoğulun uzayan -īna sesi, kısa yarar çiftinden sonra insanlara doğru belirgin bir kapanış ağırlığı verir; bu ses sınıfı nimetlerin üstüne yerleştirmez. 31:2'deki hikmetli Kitapla yan yana geliş, iyi ve güzel eylemi bu sınıfın kendi pratiği olarak duyurur. Muhsinin sözcüğünün bir başka dar yönü de kişinin kendi işini iyi, doğru ve ustalıkla yapmasıdır; bu becerikli çalışma rengi sınıfın tek ve tüketici tanımı değildir.

## Yönün eylemde görünmesi

31:4'te {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} sınıfının {ar:يُقِيمُونَ ٱلصَّلَوٰةَ, tr:yuqīmūna ṣ-ṣalāh, gloss:namazı sürdürürler} ve {ar:وَيُؤْتُونَ ٱلزَّكَوٰةَ, tr:wa-yuʾtūna z-zakāh, gloss:zekâtı verirler} diye anlatılan pratikleri, 31:3'teki alıcı sınıfını soyut bir övgüden görünür eyleme taşır; ahirete kesin inanmaları da bu profile dahildir. 31:5'te aynı kişiler {ar:عَلَىٰ هُدًۭى, tr:ʿalā hudā, gloss:hidayet üzerinde} bulunur ve {ar:ٱلْمُفْلِحُونَ, tr:al-mufliḥūn, gloss:felaha erenler} diye anılır. Bu sıra eylem, yön ve başarıyı katılımlı bir ilerleyiş olarak okumaya imkân verir; namaz ve zekât bu yoruma göre hidayetin mekanik nedeni ya da felahın garantisi değildir, dışarıdan verilen ödül okuması da açık kalır.

Namazı sürdürmeyi bildiren 31:4'teki {ar:يُقِيمُونَ, tr:yuqīmūna, gloss:sürdürürler} fiili, ayakta tutma imgesiyle namazı ve 31:3'ün {ar:هُدًى, tr:hudā, gloss:yol gösterme} yönünü buluşturunca ibadeti sürdürülen bir hizalanma gibi duyurur; açık “sürdürme” anlamı bu bağlamsal okumada da temelde kalır. Aynı ayetteki {ar:وَيُؤْتُونَ ٱلزَّكَوٰةَ, tr:wa-yuʾtūna z-zakāh, gloss:zekâtı verirler} ifadesi olağan verme eylemini taşır. Kökün büyüme ve meyve verme imgesi, paylaşma pratiği ve rehberlikle temas ederek katkıyı gelişip ürün verebilen bir uygulama gibi genişletir; bu da kesin sözlük karşılığı değil, ihtiyatlı bir bağlam önerisidir.

31:5'te {ar:عَلَىٰ هُدًۭى, tr:ʿalā hudā, gloss:hidayet üzerinde} bulunma, yol ve izlenen tutum anlamını önceki eylemlerle birleştirir. {ar:هُدًى, tr:hudā, gloss:yol gösterme} sözcüğünün bir bütünün ilk ya da önde duran bölümü anlamında da kullanılması, yönün izleyenlerden önce yer alan bir kılavuz gibi görünmesini sağlar; kılavuz değnek ya da önden giden rehber imgesi bu öncülüğü ekler. Böylece 31:2'deki yazılı ve hikmetli çerçeveden 31:3'teki yön ve rahmete, 31:4'te yinelenen ibadet ve paylaşıma, 31:5'te hidayet üzerinde oluş ve felaha uzanan metin içi hat görünür olur. Bu okuma öndeki rehberi mecazi tutar; davranış dizisinin felahı mekanik biçimde garanti ettiği sonucuna da varmaz.

## Alımlamanın kesintiye uğraması

31:3'te iyilik yapanlara sunulan {ar:هُدًى, tr:hudā, gloss:yol gösterme} ve {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}ten sonra, 31:6'da {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahw al-ḥadīth, gloss:oyalayıcı söz} satın alıp Allah'ın yolundan saptırma anlatılır. {ar:لِيُضِلَّ, tr:li-yuḍilla, gloss:saptırmak için} ifadesinin {ar:سَبِيلِ ٱللَّهِ, tr:sabīli llāh, gloss:Allah'ın yolu} ile yan yana gelişi, hidayetin karşısında etkin bir uzaklaştırma ve terk edilebilir bir güzergâh açar; bu sözcükler arasındaki ayrıntılı bağ ihtiyatlıdır. Yolun somut rota gibi sunulması, saptırma eyleminin neye yöneldiğini belirginleştirir.

31:7'de {ar:وَلَّىٰ مُسْتَكْبِرًا, tr:wallā mustakbiran, gloss:kibirlenerek yüz çevirdi} diye nitelenen davranışın ardından, {ar:كَأَن لَّمْ يَسْمَعْهَا, tr:ka-an lam yasmaʿhā, gloss:sanki onları duymamış gibi} sözü işitmeyi ses almaktan mesajı karşılayıp alımlamaya taşır. {ar:فِىٓ أُذُنَيْهِ وَقْرًۭا, tr:fī udhunayhi waqran, gloss:kulaklarında ağırlık} tasviri de erişimin bedensel olarak kapanmasını duyulur kılar. Böylece 31:3'te sunulan {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın kasıtlı oyalanma ve yüz çevirmeyle alımlanmasının kesilebildiği görünür olur; bu sahne her alıcının reddini değil, bu belirli kapanma biçimini anlatır. {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in koruyucu yönü bu ayet komşuluğunda zorlamadan sunulan bakım gibi işitilir. Bu sınırlı bağlam okuması zorlama hakkında genel bir kuram kurmaz ve 31:6 ile 31:7'deki ceza vurgusunu silmez; iki okuma arasında seçim yapmadan alımlamanın etik boyutunu öne çıkarır.

## Yön ile bakım

Odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} olağan anlamıyla, başkasının hali karşısında yumuşayan kalbin duyduğu acıma ve yakınlıktır. Aynı kelime ailesinin etkin yüzü ise acınanı esirgemeye, korumaya ve ona iyilik etmeye yönelir. Bu iki yüz, {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın doğru yönü ve {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın eylemli alıcılığıyla buluştuğunda iki yarar arasında işleyen bir ilişki kurar: hidayet yolu açar, rahmet o yolda iyiliğin gerçekleşmesine koruyucu destek verir. Cümle bu desteğin muhatabı olarak insan sınıfını gösterir; dua, mülk ya da karşılık alışverişi gibi ayrı bir senaryo kurmaz ve alıcıları nimetin kaynağı yapmaz.

Odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ailesindeki {ar:رَحِم, tr:raḥim, gloss:rahim} sözcüğünün ayrı bir anlamı, yavrunun oluşup geliştiği ve taşındığı dişi beden içi organdır. Odaktaki {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın yönü ve {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın etkin pratiği bu imgeyi iyi eylemin gelişebileceği korunaklı koşullar olarak duyurur. Böylece rahmetin sığınak gibi hissedilen koruyucu yönü belirginleşir; odaktaki sözcüğün olağan okuması merhamet olarak kalır ve gerçek bir organ ya da gebelik anlatısı ileri sürülmez.

{ar:هُدًى, tr:hudā, gloss:yol gösterme} gösterilen yönün yanı sıra yol, gidiş, yöntem ve görünür tutum anlamlarıyla da duyulabilir. Bu yön, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in korunaklı çevresi ve {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın pratiğiyle buluşunca doğru doğrultu bakım içinde yaşanabilen ilerleyiş olur; yürüyüş imgesi burada genel bir yaşam tarzı hükmüne dönüşmez. Muhsin kişi kendi işini üstlendiğinde iyi, doğru ve ustalıkla yapma rengi kazanabilir; eylem başkasına yöneldiğinde ise yarar sağlama ve iyi davranma belirginleşir. Ustalık sınıfın tek tanımı değildir ve ayet belirli bir iyilik eylemi göstermez.

## Armağan ve karşılık

Odaktaki {ar:هُدًى, tr:hudā, gloss:yol gösterme} ailesindeki {ar:هَدِيَّة, tr:hadiyya, gloss:armağan} sözcüğü, sevilen ya da yakınlık duyulan kişiye incelik göstergesi olarak verilen şeyi adlandırır; ailedeki başka bir fiil ise hediyenin kendisini değil, onu o kişiye ulaştırma eylemini anlatır. Sûrenin girişindeki Besmele'de yer alan {ar:الرَّحْمَٰنِ, tr:ar-Raḥmān, gloss:rahmeti geniş olan} ve {ar:الرَّحِيمِ, tr:ar-Raḥīm, gloss:merhamet eden} adları (S:0), 31:3'teki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ile {ar:لِّلْمُحْسِنِينَ, tr:li-l-muḥsinīna, gloss:iyilik yapanlar için} alıcı ilişkisine temas edince, doğru yönün merhamet içinde sunulan bir armağan gibi duyulmasına imkân verir. 31:4'teki verme, 31:5'te hidayetin Rablerinden geldiğinin belirtilmesi ve 49:17'de imana yöneltilmenin açıkça ilahî lütuf diye anılması bu okumayı güçlendirir. Bu ikinci katman, hidayetin olağan doğru yön anlamını koruyarak onu şefkatle ulaşan bir iyilik gibi de işitir; armağan imgesi burada somut bir verme olayı ya da kazanılmış karşılık iddiası taşımaz.

{ar:هُدًى, tr:hudā, gloss:yol gösterme} ailesindeki armağan anlamı, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ailesindeki {ar:رَحِم, tr:raḥim, gloss:akrabalık} sözcüğünün kişiler arasında kalıcı bağ kuran ayrı kullanımıyla ihtiyatlı bir sosyal benzetmeye açılır. Sevilen kişiye incelik sunma, yakınlık ve iyiliğin başkasına yönelmesi birlikte düşünüldüğünde, iyilik önce alınır, sonra başkasına taşınabilir. Bu bağ dolaşım benzetmesidir; gerçek akrabalık ya da fiilî alışveriş ileri sürmez. {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} bu dolaşımda aldığı iyiliği sonraki eyleme taşıyabilecek alıcı sınıf olarak kalır; cümlenin sonlu fiil öznesine dönüşmez.

Alınan iyiliğe eylemle karşılık verme, armağanı satın almakla aynı şey değildir. 29:69'da Allah yolunda çaba gösterenlere yollarının gösterilmesi, ardından Allah'ın iyilik yapanlarla beraber olduğunun bildirilmesi; 31:4'te ibadet ve verme, 31:8'de iman ve düzgün işler, 49:17'de ise {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın ilahî lütuf sayılmasıyla birlikte düşünüldüğünde, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in eşlik ettiği armağanı alan {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} sınıf edilgin kalmaz. Bu eylemler hidayetin bedeli değil, alınan yönün yaşanır hale gelişidir: iyilik verilen nimet karşısında görünür olur, fakat hak edilmiş ücret diye kurulmaz.

## Ölçülü gidişten güvenli tutuşa

{ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} adı, dış görünüşteki güzelliğin yanı sıra kötü davranışın karşıtı olan iyi eylemi ve başkasına yarar sağlamayı taşır. 31:19'da {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-qṣid fī mashyik, gloss:yürüyüşünde ölçülü ol} ve {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtik, gloss:sesini alçalt} öğütleri bu niteliği ölçülü yürüyüş ve alçak sesle görünür kılar. {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın yön ve izlenen tutum anlamı bu sahnede dingin bir gidiş olarak belirir; yürüyüş rehberliğin somut bir görünümüdür, kapsamı değildir. 31:19 ile 31:22 arasındaki bağ belirgindir; 31:18'e uzanan okuma daha ihtiyatlı kalır.

31:22'de bu ölçülü gidiş, yönelmiş yüz ve sağlam tutuşla başka bir görünüm kazanır: {ar:وَمَن يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ وَهُوَ مُحْسِنٌۭ, tr:wa-man yuslim wajhahu ilā llāhi wa-huwa muḥsin, gloss:yüzünü Allah'a teslim edip iyilik yapan kimse} için {ar:فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:faqadi-stamsaka bi-l-ʿurwati l-wuthqā, gloss:sağlam kulpa sımsıkı tutunmuştur} denir. Yüzün Allah'a yönelmesi, teslimiyet, tutunma ve sağlamlaştırma birbirini izler; yararı alan kişi böylece önceden belirlenmiş edilgin bir alıcı olmaktan çıkar, yönelen ve tutunan bir özne olarak görünür. Güvenli tutuş, hidayet, rahmet ve iyiliğin olağan anlamlarını koruyarak bu üç niteliği etkin bağlılık imgesinde buluşturur; rahmetin iç yakınlık ve koruyucu bakım yüzü bu ilişkide güven verir. 31:19'daki ölçülü yürüyüşten 31:22'deki teslimiyete uzanan bağ, bu özel genişlemenin dayanağıdır.

## Onarıma açılan merhamet

Rahmetin etkin koruma yönü, 2:178'de bağışlama, uygun biçimde izleme ve güzel ödemenin Rab'den gelen kolaylık ve rahmetle yan yana gelişinde karşılık bulur: {ar:بِإِحْسَٰنٍۢ, tr:bi-iḥsān, gloss:güzel ve hakkaniyetli biçimde} ödeme ile {ar:تَخْفِيفٌۭ مِّن رَّبِّكُمْ وَرَحْمَةٌۭ, tr:takhfīfun min rabbikum wa-raḥmah, gloss:Rabbinizden bir kolaylık ve rahmet} birlikte anılır. 3:134'te infak, öfkeyi tutma ve insanları bağışlama da etkin iyilik yapanların profilini somutlaştırır. Bu iki bağlam, odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ile {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın zararı sınırlayıp onarıma alan açan yönünü belirginleştirir: bağışlama sorumluluğu silmeden ilişkiyi onarabilir, sınırı aşan saldırı da mahkûm kalır. 2:178 ve 3:134'ün sözdizimsel çözümlemesi bu karşılaştırma için verilmediğinden, burada sundukları şey 31:3 için hukuk hükmü değil, nitelikli bir metinler arası yankıdır.

## Taşıma, gelişme ve görünmeyen

31:10'da {ar:رَوَاسِىَ, tr:rawāsiya, gloss:sağlam dağlar} yeryüzünü {ar:أَن تَمِيدَ بِكُمْ, tr:an tamīda bikum, gloss:sizinle sallanmasın diye} sallanmaktan koruyarak istikrarlı bir zemin sağlar; suyun ardından {ar:فَأَنۢبَتْنَا فِيهَا, tr:fa-anbatnā fīhā, gloss:orada bitirdik} her türden bitkinin yetişmesi bu zeminde gelişme imgesini açar. Sabitleme ile bitki büyümesi aynı ayette yan yana durur; {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın yönü ve {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in korumasıyla kurulan bakım okumasına iki ayrı katkı sunar, bütün benzetmeler arasında tek bir süreç ileri sürmez.

Odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ailesindeki {ar:رَحِم, tr:raḥim, gloss:rahim} anlamı, bakım çevresine annenin taşıdığı yavruyu da ekler (31:14). {ar:حَمَلَتْهُ أُمُّهُۥ, tr:ḥamalat-hu ummuhu, gloss:annesi onu taşıdı} ifadesini {ar:وَهْنًا عَلَىٰ وَهْنٍ, tr:wahnān ʿalā wahn, gloss:güçlük üzerine güçlükle} izler; ardından {ar:وَفِصَالُهُۥ فِى عَامَيْنِ, tr:wa-fiṣāluhu fī ʿāmayn, gloss:iki yılda sütten kesilmesi} ayrılmaya geçişi gösterir. Böylece taşıma, bedensel zorlanma boyunca sürdürülen korumayı; sütten kesilme ise bakımın zamanla ayrılığa yer açmasını görünür kılar.

Dikkat daha sonra görünmeyen oluşuma yönelir. 31:16'da {ar:مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍۢ, tr:mithqāla ḥabbatin min khardal, gloss:hardal tanesi ağırlığınca} küçüklükteki bir şeyin kayada, göklerde ya da yerde saklı kalması ve Allah'ın {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīr, gloss:ince işlerden haberdar} diye anılması, gözetimin gözden kaçana eriştiğini düşündürür. 31:34'te {ar:ٱلْأَرْحَامِ, tr:al-arḥām, gloss:rahimler} içinde olanın bilinmesi oluşumun gizli yanına ayrı bir örnek ekler. Hardal tanesinin gizlenmesi küçük ve saklı olana dikkati, rahimlerde olanı bilme ise görünmeyen oluşuma erişimi öne çıkarır; bu temas {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}le açılan bakım imgesini genişletir, iki sahneyi aynı nesne ya da mekanizma saymaz.

31:10'da dağların yeri sallantıdan koruması bakım için istikrarı sağlar; 31:14'te annenin güçlük boyunca taşıması, ardından sütten kesmeyle ayrılığa yer açması bakımın hem maliyetini hem bırakma anını gösterir. 31:16'daki kayada, gökte ya da yerde saklı hardal tanesi ve 31:34'te rahimlerde olanı bilme ise dikkati küçük ve gizli kalana taşır. Bu ayrı görüntüler {ar:هُدًى, tr:hudā, gloss:yol gösterme}, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ve {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}la birlikte okunduğunda, yön veren koşul, taşıyıp koruyan çevre ve başkasına yarar sağlayarak gelişmeyi sürdüren eylem birbirini tamamlar. Bunların ilişkisi analojiktir: sahneler kendi bağlamlarını korur, tek bir sözlük anlamına ya da kanıtlanmış mekanizmaya indirgenmez.

Bakım imgesinin daha aykırı bir uzantısında, odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}le bağlantılı {ar:رَحِم, tr:raḥim, gloss:rahim ağrısı} sözcüğünün nadir sözlük dalı, rahim ağrısı ve bazı kullanımlarda doğum sonrası bozuklukları anlatır. 31:14'teki taşıma, güçlük üzerine güçlük ve sütten kesilme bu bedensel maliyet imgesine temas eder. {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} biçiminin etken ortaç oluşu, yinelenen zayıflık boyunca sürdürülen yarar sağlayıcı eylemi görünür kılar. Rahmetin şefkat anlamı korunurken bu uzak sözlük dalı, maliyet boyunca devam eden iyiliği de düşündürür; bu bağlantı keşif niteliğinde bir benzetmedir. 31:14 rahim ağrısı, hastalık ya da doğum sonrası bozukluk bildirmez; bu sınır, tıbbi bir tanının metne yüklenmesini önler.

## Yatıştırmadan kavrayışa

Hidayet ailesindeki ayrı bir fiil kalıbı, annenin ya da kadının çocuğu uyutmak için hafifçe sallamasını anlatır. Bu uzak imge, odaktaki {ar:هُدًى, tr:hudā, gloss:yol gösterme} isim biçimini yeniden tanımlamaz; ancak 31:14'te annenin taşıması, 31:16'da saklı kalan hardal tanesi ve ince gözetim, 31:22'deki sağlam tutuşla birlikte kırılgan öznenin yatıştırılmasını ve kavrayışa hazırlanmasını düşündürür. Odaktaki {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ailesinin ayrı {ar:رَحِم, tr:raḥim, gloss:rahim} anlamı güvenli taşıma çevresini, {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın etkin iyiliği bakım veren rolünü ekler; talimatı baştan anlayan bir akıldan önce gelen destek, bu imgelerin özgül katkısıdır. Sözlük gösterimlerindeki uyuşmazlık nedeniyle bu bağlantı uzak ve ihtiyatlı bir benzetme olarak kalır.

## Yakınlığın ve sorumluluğun sınırı

31:15'te ebeveyn baskısına verilen yanıt, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet} ailesindeki yakınlık anlamını itaate indirgemeden sürdürür. Önce {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:ikisine itaat etme}, ardından {ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī d-dunyā maʿrūfan, gloss:dünyada ikisine iyi biçimde eşlik et} ve {ar:وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ, tr:wa-ttabiʿ sabīla man anāba, gloss:Allah'a yönelenin yolunu izle} buyrukları gelir. Rahmet ailesindeki {ar:رَحِم, tr:raḥim, gloss:akrabalık} kullanımı ortak soydan gelen yakınlığı ve kalıcı bağı adlandırır; bu ebeveyn sahnesi o anlamı tetikler. {ar:هُدًى, tr:hudā, gloss:yol gösterme}, yanlış buyruğu reddedip Allah'a yönelenin yolunu izlemeyi gösterirken {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın eylemli niteliği ve maʿrūf eşlik ilişkiyi sürdürür. Böylece itaatsizlik bağı koparmadan mümkündür; iyi biçimde eşlik etmenin asgari görev mi, daha ileri bir iyilik mi olduğu açık kalır.

31:33 bu yakınlığı sorumluluk sınırına taşır: {ar:لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ, tr:lā yajzī wālidun ʿan waladih, gloss:hiçbir ebeveyn çocuğu adına karşılık veremez} ve çocuk da ebeveyninin yerini alamaz. Doğum bağı gerçek yakınlığını korur, fakat bir başkasının hesabını üstlenmez; {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}ın eylemli niteliği de yakına devredilemez. 31:33'te dünyanın aldatıcı parıltısına karşı uyarı, aile yakınlığını devredilebilir bir güvence saymayı engeller. Sınırlama yardımlaşmaya değil, başkasının hesabını ve kişisel iyilik eylemini devretme varsayımına yönelir.

{ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar} adı eylemli iyiliği taşırken, bağlantılı {ar:حُسْن, tr:ḥusn, gloss:güzellik ve iyilik} kökünün yalnızca iki kalıplaşmış ifadede görülen başka bir kullanımı çabanın eriştiği son sınırı anlatır. 31:15'teki ağır zorlanma ile 31:17'deki sabır ve kararlılık bu uzak anlam için birbirinden bağımsız dayanaklar sağlar. Birlikte düşünüldüklerinde bu sahneler, iyiliğin güçlük altında yönünü koruyup koruyamayacağını sorgulatan bir baskı imgesi kurar. “Çabanın son sınırı” muhsinīnin olağan anlamı değil, bu bağlamların tetiklediği bir benzetmedir; sınırlı sözlük kullanımı her tür gayrete genellenmez.

## Çalkantıdan sonra

31:31'de geminin {ar:تَجْرِى فِى ٱلْبَحْرِ بِنِعْمَتِ ٱللَّهِ, tr:tajrī fī l-baḥri bi-niʿmati llāh, gloss:Allah'ın nimetiyle denizde akması} geçişi mümkün kılar: gemi aracı, akıp giden hareket güzergâhı, ilahî nimet de geçişin imkânını verir. 31:32'de {ar:مَّوْجٌۭ كَٱلظُّلَلِ, tr:mawjun ka-ẓulal, gloss:gölgelikler gibi dalgalar} ufku örter ve yolcuları sarar; {ar:فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:fa-lammā najjāhum ilā l-barr, gloss:onları karaya çıkarıp kurtarınca} sözü kurtuluşun onları tehlikeden ayırdığı anı gösterir. Bu geçişte {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın yol ve gidiş anlamı, {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in esirgeyici iyiliğiyle birlikte belirir; {ar:الْمُحْسِنِينَ, tr:al-muḥsinīna, gloss:iyilik yapanlar}dan beklenen eylem ise kurtuluştan sonra başlar.

31:32'de kurtulanların tutumu ayrışır: {ar:فَمِنْهُم مُّقْتَصِدٌۭ, tr:fa-minhum muqtaṣid, gloss:kimileri ölçülü davranır} ölçüyü koruyanları, {ar:خَتَّارٍ كَفُورٍ, tr:khattār kafūr, gloss:çok vefasız ve nankör} ise vefasızlık ve nankörlüğü görünür kılar. Kurtuluş, tehlikenin gerçekliğini geriye dönük silmez ve şükrü kendiliğinden doğurmaz; dalgalı geçitten sonra bazıları ölçülü karşılık verirken başkaları nankörlüğe döner. Böylece {ar:هُدًى, tr:hudā, gloss:yol gösterme}nın açtığı yön ile {ar:رَحْمَةً, tr:raḥmatan, gloss:rahmet}in sağladığı koruma bir imkân sunar; kurtulanların eylemleri bu imkânın nasıl karşılandığını gösterir.

</source_prose>
