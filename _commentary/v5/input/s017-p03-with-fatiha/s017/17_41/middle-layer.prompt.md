# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:41**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.middle.claims.json`

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
- Refer to source paragraphs as `17:41 ¶N`.

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

`(17:41 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:41",
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
        "citation": "(17:41 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_41/17_41.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_41/17_41.middle.claims.json \
  --ayah-ref 17:41
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_41/17_41.prose.editorial.tr.md`

<source_prose>
## Çeşitlendirilmiş Sunuş

Başlangıçtaki {ar:وَ, tr:wa, gloss:bağlayıcı} söylemi önceki akışa ekler, ancak tek bir önceki iddiayı seçmez. Açılıştaki {ar:لَ, tr:la, gloss:pekiştirme lâmı} ile {ar:قَدْ, tr:qad, gloss:gerçekleşmişlik}, birinci çoğul çekimli tamamlanmış {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} eylemini öne alır. Düz akışta, “Bu Kur’an’da çeşitlendirdik ki muhataplar öğüt alıp hatırlasınlar” denir; arkasından onlarda ürküntüyle uzaklaşmanın arttığı bildirilir. Birinci çoğul çekim eylemi tamamlanmış ilahî bir fiil olarak kurar, özneyi ise bu dilbilgisel biçimin ötesinde tanımlamaz.

{ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} Form II biçimiyle bir şeyi farklı yön ve biçimler arasında tekrar tekrar çevirerek sunuşu çeşitlendirmeyi anlatır. Burada söz konusu olan harcama ya da değiş-tokuş değil, anlatımın çeşitli biçimlerde sunulmasıdır. Fiilin doğrudan nesnesi ayrıca söylenmediği için hangi unsurların çeşitlendirildiği açık kalır. Ardından gelen {ar:فِي, tr:fī, gloss:içinde} öbeği öncelikle bu eylemin alanını gösterir; Kur’an’ın ortam ya da konu gibi duyulması da ikincil ve nitelikli bir olasılık olarak kalır, söylenmeyen nesnenin yerini almaz.

Bu alanı {ar:هَٰذَا, tr:hādhā, gloss:bu} ile hemen arkasındaki belirli {ar:ٱلْقُرْءَانِ, tr:al-qurʾān, gloss:Kur’an} adı sabitler: tekil-eril uyum ve açıklayıcı ad ilişkisi, gösterileni bu söylemde şimdi anılan metne bağlar. Belirlilik eki ve tamlayan biçimi, çeşitlendirmenin içinde gerçekleştiği bilinen tek bir okunmuş bütünü gösterir; çeşitlendirilen bütün unsurları saymaz ve daha geniş bir öz-atıf dizisi kurmaz. Böylece fī öbeği, amaç lâmına geçmeden ilk eylemin alanını tamamlar.

{ar:ٱلْقُرْءَانِ, tr:al-qurʾān, gloss:Kur’an} olağan anlamıyla adı konan metindir. Aynı kullanım çevresindeki {ar:قراءة وتلاوة وإقراء, tr:qirāʾah wa-tilāwah wa-iqrāʾ, gloss:okuma, tilavet ve okutma} ise metni okumayı, tilavet etmeyi, başkasına okumayı ya da okutmayı ve birlikte çalışmayı kapsayan ayrı bir kıraat imgesi açar. Bu temas, {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} fiili metnin sunuşunu biçimler arasında dolaştırdığında belirir: adı konan metin aynı kalırken okunan ve işitilen sunuş değişir. Kıraat çağrışımı, adı konan metnin çevresine okunan ve aktarılan sunuş katmanını ekler; olağan gönderge metin olarak kalır.

## Hatırlama ve Uzaklaşma

Açılıştaki pekiştirme lâmından sonra gelen {ar:لِ, tr:li, gloss:amaç lâmı} başka bir işi üstlenir: {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlamaları için} fiilini tamamlanmış eyleme bağlar. Lâmın yönettiği Form V fiilin mansup biçimi, onu bağımsız bir bildirim değil çeşitlendirmenin amacını taşıyan bağlı tümce yapar. Bu amaç lâmı eylemin hedefini gösterir; gerçekleşen karşılığı ise sonuç bölümü ayrıca bildirir.

Bu hatırlamanın açık bir nesnesi verilmez: Kur’an adlandırılmış alanı, çeşitlendirme sunuşun biçimini sağlar, fakat hangi tek bilginin hatırlanacağı belirtilmez. Form V {ar:يَذَّكَّرُوا۟, tr:yadhdhakarū, gloss:öğüt alıp hatırlasınlar} muhatabın kendisine öğüt alıp hatırlatmasına yönelen içe dönük dikkati taşır. Unutulmuş ya da zihinden uzaklaşmış bilginin yeniden bilince gelmesi, değişik biçimlerde sunulan Kur’an’la karşılaşınca yanıtı yalnızca sözleri yinelemekten ayırır. Burada Form V, muhatabın kendine dönük hatırlama eylemini taşır; hatırlatıcı araç bağlantısı ise bu fiile değil, Kur’an adıyla belirlenen metin alanına aittir.

Hatırlamanın içe yönelen bu hareketinin karşısına sonuçtaki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} dışa çekilmeyi koyar. Sözcüğün olağan anlamı kaçınma ve ürküntüdür; somut imgesinde ürken ya da tedirgin olan yüzünü çevirip hitapla arasına mesafe koyar. Böylece amaçtaki yeniden bilince çağırma ile bildirilen bedensel geri çekilme aynı yerel harekette karşı karşıya gelir. Odak sözcük bu cümlede ürküp yüz çevirerek mesafe koymayı anlatır; toplu kalkış kullanımı başka bağlamın imgesi olarak kalır.

Amaçtan sonuca geçişteki ikinci {ar:وَ, tr:wa, gloss:bağlayıcı}, başlangıçtakinden farklı olarak {ar:مَا, tr:mā, gloss:olumsuzluk} ile başlayan sonuç bölümüne eklenir. Düz bağlamanın yanı sıra karşıtlık ya da durum bildiren bir nüans da duyulabilir; bu olasılık, amaç lâmının işlevini değiştirmez. {ar:مَا, tr:mā, gloss:olumsuzluk} artış bildirimini olumsuzlarken {ar:إِلَّا, tr:illā, gloss:ancak; yalnızca}, son {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} adını istisna olarak öne çıkarır. İstisnanın addan önce gelişi dikkati daralan sonuca çevirir: bu tümcede bildirilen tek artış ürküntüyle uzaklaşmadır. Böylece istisna, yalnız bu tümcenin bildirdiği sonucu daraltır; daha geniş bir dinleyici tepkileri toplamı kurmaz.

Artışı taşıyan {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} şimdiki zaman biçimiyle süren ya da yinelenen bir çoğalmayı anlatır; fiilin kendisi olumsuz değil, başka bir öğenin eklenip büyümesini bildirir. Sonuçtaki {ar:هُمْ, tr:hum, gloss:onları} ekiyle öğüt alması beklenen üçüncü çoğul özne, artıştan etkilenen gruba dönüşür; çoğul biçim grubu artıştan etkilenen bir alıcı olarak gösterir, kimliğini açık bırakır. Artış fiilinin öznesi açıkça kurulmadığından, yakındaki Kur’an ile önceki çeşitlendirme eylemi iki olası etken olarak kalır; yerel dilbilgisi aralarında seçim yapmaz.

Belirsiz ve mansup {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} hem neyin arttığını verir hem de yakın sözdiziminde artışın içeriği ya da ikinci nesnesi olarak okunabilir; iki çözümleme de aynı geri çekilme sonucunu korur. Belirsiz mastar, uzaklaşmayı miktarı, derecesi ve yoğunluğu açık bir durum ya da süreç olarak sunar; tekrar sayısını ya da tek bir tamamlanmış olayın sınırını belirlemez. Son sıraya gelişi, tamamlanmış eylemden amaca ve kısıtlanmış sonuca uzanan cümle hareketini ürküntüde kapatırken hatırlama hedefini de yerinde tutar.

Bu dilbilgisel hareket, daha yorumlayıcı bir öğretici dönüş imgesine de açılır. Sabit metnin sunuşu biçimler arasında çevrilir, Form V hatırlama amacı muhatabı kendisine öğüt almaya yöneltir; buna karşılık {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} ile {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} hedeflenen içe dönüş karşısında artan bir mesafe kurar. Böyle işitildiğinde bildirilen sonuç öğretici düzenlemenin yönünü tersine çevirir. Bu imge ayetteki amaç-sonuç dizilişini yorumlar; ölçülmüş bir yöntem ya da her sunuş için geçerli bir nedensel kural ileri sürmez.

Bu uzamsal imge metinle sunuş arasındaki ilişkiden doğar: {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} aynı metnin farklı yüzlerini sunar; {ar:يَذَّكَّرُوا۟, tr:yadhdhakarū, gloss:öğüt alıp hatırlasınlar} unutulmuş bilgiyi yeniden bilince getirerek bu bütüne yönelen iç hareketi taşır, {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} ise yüz çevirip dışa mesafe koymayı gösterir. {ar:قراءة وتلاوة وإقراء, tr:qirāʾah wa-tilāwah wa-iqrāʾ, gloss:okuma, tilavet ve okutma} kullanım çevresi, {ar:ٱلْقُرْءَانِ, tr:al-qurʾān, gloss:Kur’an} adını hem okunmuş bütüne hem onu seslendiren değişken sunuşa bağlar. Bu öğeler birlikte düşünüldüğünde sabit metin farklı yüzleriyle bir arada duran merkez gibi duyulur. İçe ve dışa yöneliş de aynı mekânsal imge içinde karşı karşıya gelir. Toplanmış merkez, Kur’an sözcüğünün kanıtlanmış sözlük anlamı değil, bu yerel ilişkilerin kurduğu uzamsal çağrışımdır.

Bu içe yönelen amaç, sunuşun dinleyiciyi kendine çekmesiyle ilgili ayrı bir hitabet çağrışımını da taşır. {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} için söz ve konuşma bağlamına özgü {ar:صرف الحديث والكلام بتزيين وزيادة, tr:ṣarfu al-ḥadīthi wa-l-kalāmi bi-tazyīnin wa-ziyādah, gloss:söze süs ve ekleme katma} kullanımı, dinleyicinin ilgisini yöneltmeyi anlatır. Kur’an’ın iletişim alanı ve hatırlatma amacı beklenen çekimi kurarken {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} onun yerine geri çekilmeyi getirir. Ayetin kendisi ayrıca bir konuşma adı vermediği için bu hitabet katkısı Kur’ani iletişim alanındaki yerel çağrışım olarak kalır; odaktaki fiilin olağan çeşitlendirme anlamı temel okuma, konuşmaya özgü anlam ise bu bağlamın ek katkısıdır.

Bu amaç ve karşılık düzeni başka bir ayette doğrudan yinelenir: Kur’an’da örneklerin çeşitli biçimlerde sunuluşu hatırlama amacıyla bağlanır, ardından çoğu insanın reddedişi gelir (25:50): {ar:صَرَّفْنَاهُ بَيْنَهُمْ, tr:ṣarrafnāhu baynahum, gloss:onu aralarında türlü biçimlerde sunduk}, {ar:لِيَذَّكَّرُوا, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlasınlar}, {ar:فَأَبَىٰ أَكْثَرُ النَّاسِ إِلَّا كُفُورًا, tr:fa-abā aktharu n-nāsi illā kufūran, gloss:çoğu insan yine de reddetti}. Bu Arapça tekrar, sunuşu önce hatırlama amacına, ardından çoğunluğun reddedişine bağlayarak odaktaki çeşitlendirme-karşılık ilişkisini yineler. Hatırlama amacı sunuşun yönünü gösterir; çoğunluğun reddedişi gerçekleşen karşılığı ayrıca bildirir. Amaç yapısı ayrıca hedefe giderken elverişli çarelere başvurma benzetmesini çağırır; bu planlama çağrışımı amaçlı düzenlemeye aittir, temel fiil yine sunuşu çeşitlendirmeyi anlatır ve 25:50 bu ardışıklığın neden-sonuç bağı olduğunu değil, amaç ile reddedişin yan yana gelişini gösterir.

Başka bir çağrı bu ilişkiye farklı bir karşılık ekler: Rahmân’a secde etme buyruğuna itirazdan sonra ürküntünün arttığı söylenir (25:60): {ar:ٱسْجُدُوا۟ لِلرَّحْمَٰنِ, tr:usjudū li-r-raḥmān, gloss:Rahmân’a secde edin}, {ar:وَزَادَهُمْ نُفُورًا, tr:wa-zādahum nufūran, gloss:ürküntülerini artırdı}. Buradaki artış, odaktaki {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} fiilinin nötr çoğalma anlamıyla; artanın ne olduğunu ise ayrı {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} tamamlayıcısıyla gösterir. Hatırlama hedefinden sonraki reddediş ile secde çağrısından sonraki ürküntü, çağrı ve karşılığın farklı biçimlerde buluştuğunu gösterir; bu karşılaştırma her dinleyici için tek bir alımlanma öngörmez ve iki sahne arasında doğrudan nedensellik kurmaz.

Farklı alımlanmalar, artış fiilinin yönünü tek başına belirlemediğini başka örneklerde de görünür kılar. Kur’an’da örnekler çeşitli biçimlerde sunulduktan sonra çoğunluğun reddedişi anılır (17:89): {ar:صَرَّفْنَا لِلنَّاسِ فِى هَٰذَا ٱلْقُرْءَانِ مِن كُلِّ مَثَلٍ, tr:ṣarrafnā li-n-nāsi fī hādhā l-qurʾān min kulli mathal, gloss:Kur’an’da insanlara her tür örneği sunduk}, {ar:فَأَبَىٰ أَكْثَرُ النَّاسِ إِلَّا كُفُورًا, tr:fa-abā aktharu n-nāsi illā kufūran, gloss:çoğu insan yine de reddetti}. Buna karşılık Kur’an inananlara şifa ve rahmet olurken zalimlerin kaybı artar (17:82): {ar:شِفَاءٌ وَرَحْمَةٌ لِلْمُؤْمِنِينَ, tr:shifāʾun wa-raḥmatun li-l-muʾminīn, gloss:inananlara şifa ve rahmet}, {ar:وَلَا يَزِيدُ الظَّالِمِينَ إِلَّا خَسَارًا, tr:wa-lā yazīdu ẓ-ẓālimīna illā khasāran, gloss:zalimlerin kaybını artırmaktan başka sonuç vermez}. İndirilen sûre inananların imanını artırır (9:124): {ar:فَزَادَتْهُمْ إِيمَانًا, tr:fa-zādathum īmānan, gloss:imanlarını artırır}; ateş görevlilerinin sayısı ise sınama olarak verilirken inananların imanı artar, kalbinde hastalık olanlarla inkârcılar örneğin ne murat ettiğini sorar (74:31): {ar:وَيَزْدَادَ الَّذِينَ آمَنُوا إِيمَانًا, tr:wa-yazdāda alladhīna āmanū īmānan, gloss:inananların imanı artsın}, {ar:مَاذَا أَرَادَ اللَّهُ بِهَٰذَا مَثَلًا, tr:mādhā arāda llāhu bi-hādhā mathalan, gloss:Allah bu örnekle neyi murat etti?}. Bu ayrı karşılıklar, odaktaki {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} fiilinin kendi başına bir yön seçmediğini gösterir: burada eşlik eden {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} ürküntüye, başka ayetlerde eşlik eden unsurlar ise başka sonuçlara yön verir. Böylece 17:41’deki ürküntü bu ayetin anlattığı muhataplara ait kalır; örnekler artışın tepkiye yol açıp açmadığını ya da önceden yönelmiş tutumu görünür kıldığını ayırt etmez.

## Okunan Sözün Çevresi

Bu farklı karşılıkların yakınında, iddia, sınama ve tenzih başka tanıma yolları açar. Oğullar ve meleklerden kızlar isnadı ağır bir söz diye nitelenir (17:40): {ar:قَوْلًا عَظِيمًا, tr:qawlan ʿaẓīman, gloss:ağır bir söz}. Çoğul ilahlar varsayımı karşı-olgusal bir sınamaya dönüşür (17:42): varsayılan ilahların Arş sahibine bir {ar:سَبِيلًا, tr:sabīlan, gloss:yol} arayacakları, {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} koşullu fiiliyle kurulur. Cevap, aşkınlık bildiren {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:O her türlü eksiklikten münezzehtir} sözüyle kapanır (17:43). Bu yakınlık, odaktaki çeşitlendirme ve hatırlama amacı çevresinde birkaç tanıma girişi açar: isnat itiraz edilen iddiayı, karşı-olgusal sınama yol düşüncesini, tenzih ise aşkınlığı öne çıkarır. Bunları öğretici bir sıranın parçaları olarak okumak mümkündür; her ayetin kendi reddiye işlevi de yerinde kalır, dolayısıyla yakınlık tek bir tasarlanmış dizi olduğunu kanıtlamaz.

Ardından ölçek bütün yaratılışa açılır: gökler, yer ve içlerindekiler Allah’ı överek yüceltir, fakat insanlar bu yüceltmeyi kavrayamaz (17:44): {ar:يُسَبِّحُ بِحَمْدِهِۦ, tr:yusabbiḥu bi-ḥamdihi, gloss:O’nu överek yüceltir}, {ar:لَا تَفْقَهُونَ تَسْبِيحَهُمْ, tr:lā tafqahūna tasbīḥahum, gloss:onların yüceltmesini kavrayamazsınız}. Bu sürekli övgü, hatırlama amacını Tanrı’ya yönelen kulluk, bilinçli anma ve şükür yüzüne genişletir; yaratılışta süren övgüyü fark etmek, {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlamaları için} hedefinin yanına gelir. Bu yan yanalık yaratılışın yüceltmesini hatırlamanın olası içeriğine yaklaştırır; 17:44 övgüyü odakta belirlenecek tek nesne yapmadığından bu okuma iki ayetin açtığı anlam alanıyla sınırlı kalır.

Hatırlamanın nasıl alımlandığı, okuma ve dinleme sahnelerinde daha dokunsal bir çevre kazanır (17:45, 17:46, 17:47). Kur’an okunduğunda okuyuşla inkârcılar arasına bir perde konur (17:45): {ar:قَرَأْتَ ٱلْقُرْءَانَ, tr:qaraʾta al-qurʾān, gloss:Kur’an’ı okuduğunda}, {ar:حِجَابًا, tr:ḥijāban, gloss:bir perde}. Kalplerin üzerindeki örtüler ve kulaklardaki ağırlık hatırlatmayı kavramayı güçleştirir (17:46): {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler}, {ar:وَقْرًا, tr:waqran, gloss:ağırlık}; sırt çevirip ürküntüyle uzaklaşma da bu sahnede belirir: {ar:وَلَّوْا۟ عَلَىٰٓ أَدْبَٰرِهِمْ, tr:wallaw ʿalā adbārihim, gloss:sırtlarını dönüp uzaklaştılar}. Sonraki ayette dinleyenlerden söz edilmesi (17:47): {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinlerler}, Kur’an adını okunan, işitilen ve başkasına ulaştırılan bir tilavet olayına da bağlar. Bu sahneler, hatırlama hedefinin erişim, kavrama ve işitme boyunca karşılaştığı engelleri görünür kılar; sırt çevirme {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} için bedensel bir biçim verir. Böylece odaktaki sonuç metnin okunması ile dinleyicinin alımlaması arasındaki çevrede belirginleşir, kesin nedeni ise açık kalır.

Aynı dinleme sahnesi hatırlama kökünün ayrı bir fiil biçimine sözlü bir karşılık verir: Rabbi Kur’an’da yalnız anmaktan söz edilir (17:46): {ar:ذَكَرْتَ رَبَّكَ فِي ٱلْقُرْءَانِ وَحْدَهُۥ, tr:dhakarta rabbaka fī al-qurʾān waḥdahu, gloss:Kur’an’da yalnız Rabbini andığında}. Odaktaki Form V {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlamaları için} muhatabın zihinsel hatırlamasını ve kendine öğüt vermesini taşırken, buradaki Form I {ar:ذَكَرْتَ, tr:dhakarta, gloss:andığında} Rabbi sözle anmayı anlatır; dinleyicilerin ardından geri dönmesi anmayı işitilen bir karşılaşmaya çevirir. Bu Form I örneği, hatırlama hedefinin Kur’an içindeki sesli karşılığını genişletir; Form V’in muhatabın kendine dönük zihinsel hatırlama işlevi ayrı kalır.

Bu alımlama engelleri, algı yetileriyle ilgili sorumluluk ve direnenlerin kendi sözleriyle kurdukları benzer imgeler yanında daha belirginleşir. İşitme, görme ve gönlün her birinin hesabı olduğu belirtilir (17:36): {ar:إِنَّ السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ, tr:inna s-samʿa wa-l-baṣara wa-l-fuʾāda, gloss:işitme, görme ve gönül}. Okunan hitaba direnenler kalplerinin örtüler içinde, kulaklarının ağır ve kendileriyle elçi arasında bir perde bulunduğunu söyler (41:5): {ar:قُلُوبُنَا, tr:qulūbunā, gloss:kalplerimiz}, {ar:فِي أَكِنَّةٍ, tr:fī akinnatin, gloss:örtüler içinde}, {ar:وَفِي آذَانِنَا وَقْرٌ, tr:wa-fī ādhāninā waqrun, gloss:kulaklarımızda ağırlık}, {ar:وَمِن بَيْنِنَا وَبَيْنِكَ حِجَابٌ, tr:wa-min bayninā wa-baynaka ḥijābun, gloss:aramızda bir perde}. 17:45, 17:46 ve 41:5 arasındaki perde-örtü-ağırlık bağı aynı sözcüklerin yinelenmesine değil, imge benzerliğine dayanır. 17:36’daki algı sorumluluğu da bu karşılaştırmaya katılınca, dört ayet odaktaki {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} ile sunulan hatırlama çağrısının karşılaştığı alımlama engellerini görünür kılar (17:36, 17:45, 17:46, 41:5). Bu yorum engellerin ürküntüye neden olduğunu, klinik bir durumu ya da bütün dinleyicilere yayılan bir kuralı belirlemez.

Örtü, perde ve ağırlık, beden üzerinde yükselen bir direnç imgesine zemin hazırlar (17:45, 17:46). Odaktaki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} olağan anlamıyla ürkerek geri çekilmedir; aynı kökün hastalığa bağlı ayrı kullanımında deri, ağız ya da yara şişip çevresinden ayrılarak kabarır: {ar:انتفاخ الجلد وتجافيه بالسقم, tr:intifāk al-jild wa-tajāfīhi bi-s-saqam, gloss:hastalıkla derinin şişip çevresinden ayrılması}. Şişen parçanın çevresinden ayrılıp yüzeyin üzerine yükselme hareketi, bu tasviri dokunsal bir karşı-koyuş imgesine dönüştürür. {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} fiilinin nötr artış yönüyle okunduğunda perde (17:45), kalp örtüleri ve kulak ağırlığı (17:46), alımlamanın karşısında kabaran yüzeyin görsel dayanakları olur; artışın bir öğeyi büyütmesi bu yüzeyi odak sonucuyla buluşturur. Bu bağlantı hastalığı odak ayete taşımadan, bariyerlerin sunduğu alımlama direncini dokunsal kılar.

İşitilen sözün çevresinde biriken bu engeller, mesajın insanlar arasında nasıl işlendiği sorusunu açar. Dinleyenlerin sözünden sonra gizli danışma gelir (17:47): {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinlerler}, {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma}; ardından elçiyi “büyülenmiş bir adam” diye niteleyen iddia aktarılır: {ar:إِن تَتَّبِعُونَ إِلَّا رَجُلًا مَّسْحُورًا, tr:in tattabiʿūna illā rajulan masḥūran, gloss:siz ancak büyülenmiş bir adama uyuyorsunuz}. Etiket mesajın içeriğinden elçinin durumuna yönelir. Ardından onun için örnekler ileri sürüldüğü ve bir yol bulamadıkları söylenir (17:48): {ar:ضَرَبُوا۟ لَكَ ٱلْأَمْثَالَ, tr:ḍarabū laka al-amthāl, gloss:senin için benzetmeler ve örnekler ileri sürdüler}, {ar:فَضَلُّوا۟ فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-ḍallū fa-lā yastaṭīʿūna sabīlan, gloss:şaşırdılar ve yola güç yetiremediler}. Dinleme ile özel yorum arasındaki bu dolaşım, mesajın alıcılar arasında nasıl işlendiğini gösterir; işitilmiş olması tek başına kabul anlamına gelmez. Danışmanın içeriği ve bu sosyal işlemenin odaktaki geri çekilmeyle bağı açık kalır.

Bu sözlü dolaşım, konuşmaya özgü çekim imgesini somut bir alana yerleştirir: {ar:صرف الحديث والكلام بتزيين وزيادة, tr:ṣarfu al-ḥadīthi wa-l-kalāmi bi-tazyīnin wa-ziyādah, gloss:söze süs ve ekleme katma} kullanımı, söz ve konuşmaya güzelleştirme ile ilave katarak dinleyiciyi yöneltmeyi anlatır. Bu sınırlı hitabet yüzü, Kur’an’ın iletişim alanı ve hatırlatma amacıyla birlikte düşünüldüğünde beklenen çekimi açıklar; odaktaki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} ise karşı yönde mesafe koyar. 17:47’deki danışma ve 17:48’deki düşmanca adlandırma bu alımlama farkını toplumsal bir dolaşıma taşır. Odaktaki olağan çeşitlendirme anlamı temel okuma olarak sürer. Hitabet kullanımı ise yalnızca bu iletişim bağlamında beklenen çekimle gerçekleşen geri çekilme arasındaki karşıtlığa katkı verir.

Sonraki uyarı, kişiler arası sözün doğurabileceği gerilimi adlandırır: en güzel sözün söylenmesi istenir, şeytanın insanlar arasında kışkırtma çıkarabileceği belirtilir (17:53): {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaġu baynahum, gloss:aralarını kışkırtır}. Özel danışmadan düşmanca etikete ve kişiler arası gerilime uzanan olası dolaşım, bireysel geri çekilmenin çevresinde toplumsal bir karşılığın nasıl tasavvur edilebileceğini gösterir (17:47, 17:48, 17:53). Bağlantı olasılık düzeyinde kalır: bütün muhalifleri kışkırtılmış saymaz ve bu gerilimi ürküntünün doğrudan nedeni olarak belirlemez.

## Dönüş ve Yöneliş

Söz dolaşımından sonra yakın bağlam bedensel dağılma ve yeniden çağrılma sorusuna döner. Kemiklerin ufalanmış kalıntılara dönüşmesinin ardından yeniden kaldırılma itirazı dile getirilir (17:49): {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar}, {ar:لَمَبْعُوثُونَ, tr:lamabʿūthūna, gloss:elbette yeniden diriltileceğiz}. İtiraz taş ya da demir olmayı da kapsar (17:50): {ar:حِجَارَةً, tr:ḥijārah, gloss:taş}, {ar:حَدِيدًا, tr:ḥadīdan, gloss:demir}. “Bizi kim geri getirecek?” sorusuna, onları ilk kez yaratan cevabı verilir (17:51): {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri getirecek}, {ar:فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:faṭarakum awwala marratin, gloss:sizi ilk kez yaratan}. Ufalanmış kemikten dirençli maddelere, oradan ilk yaratılışla dönüşü aynı failde buluşturan yanıta ilerleyen bu tartışma, odaktaki çeşitlendirmeyle farklı maddi biçimler üzerinden; hatırlama amacıyla da ilk kökenin yeniden tanınması üzerinden temas eder. Bu yakınlık, hatırlama amacına ilk yaratılışla dönüşü yeniden tanıma imgesi ekler; diriliş tartışması 17:41’in çevresindeki bağlamdır ve odak ayet dirilişi doğrudan anlatmaz. Ayetlerin sıralı gelişi ilk kökenle dönüşü yan yana düşünmeye elverir, tek bir tasarlanmış kanıt dizisi olmasını şart koşmaz.

17:49’daki {ar:رُفَاتًا, tr:rufātan, gloss:ufalanmış kalıntılar} dağılmayı, 17:52’de çağrıya O’nu överek karşılık verme ise yeniden bir araya gelen cevabı öne çıkarır: {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır}, {ar:فَتَسْتَجِيبُونَ بِحَمْدِهِۦ, tr:fa-tastajībūna bi-ḥamdihi, gloss:O’nu överek karşılık verirsiniz}. Tilavetteki yakınlık bu ayrı sahneler arasında dağılma ile yanıtı buluşturur. Odaktaki {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} farklı sunuş yüzlerini, {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlamaları için} hatırlama amacını taşır; {ar:ٱلْقُرْءَانِ, tr:al-qurʾān, gloss:Kur’an} adındaki okunmuş bütün de bu iki sahne arasında toparlanma imgesine katkı verir. Kalıntı ile övgülü cevabın bu tilavette yan yana gelişi, Kur’an adının sözlük anlamından ayrı, yerel bir toplanma imgesi kurar.

17:47’deki {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ile 17:53’teki {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaġu baynahum, gloss:aralarını kışkırtır} toplumsal karşılık benzetmesini ayrı ayrı tetikler. Artış fiiliyle aynı kökten gelen bir kullanım, yolculuk ya da geçiş için gerekli azığı önceden hazırlayıp taşımayı anlatır: {ar:حمل الزاد للانتقال, tr:ḥamlu al-zādi li-l-intiqāl, gloss:yol azığı hazırlayıp taşımak}. Bu hazırlık, odaktaki {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} fiilinin anlamı değil, toplumsal tepkinin önceden düzenlenişine dair ayrı bir çağrışımdır. Uzaklaşma sözcüğüyle aynı kökün başka bir kullanımında ise önemli bir iş, yardım ya da düşmanla karşılaşma çağrısı üzerine gruplar hâlinde kalkılır: {ar:النهوض إلى الحرب أو النصرة, tr:an-nuhūḍu ilā al-ḥarbi aw an-nuṣrati, gloss:savaş ya da yardım için topluca kalkışma}. Önceden hazırlanan yol azığı ile çağrı üzerine topluca kalkışma bir araya gelince, bireysel geri çekilmenin çevresinde olası bir karşı-seferberlik imgesi belirir. Bu yerel benzetmede odaktaki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} ürküp yüz çevirerek mesafe koymayı anlatır; imge gerçek bir silahlı gücün varlığını ileri sürmez.

Bu toplu kalkış imgesinin ters yönü Nisâ’daki çağrıda belirginleşir (4:71): {ar:فَٱنفِرُوا۟ ثُبَاتٍ أَوِ ٱنفِرُوا۟ جَمِيعًا, tr:fa-nfirū thubātin awi-nfirū jamīʿan, gloss:gruplar hâlinde yahut hep birlikte yola çıkın}. Buradaki çoğul emir, önemli bir iş ya da düşmanla karşılaşma için gruplar hâlinde veya hep birlikte yola çıkmayı söyler. Odaktaki mastarın ürküp geri çekilmesine karşı 4:71’in farklı fiil biçimi insanları harekete çağırır; amaçtaki öğüde yönelme de bu karşıt yönü belirginleştirir. Karşılaştırma aynı kök alanındaki ayrı biçimlere dayanır: 4:71’in toplu çıkışı 17:41’deki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} sözcüğünün ürkek uzaklaşma anlamını değiştirmez.

Toplumsal alımlama zemininde elçinin rolü ayrıca sınırlandırılır: insanlar üzerinde {ar:وَكِيلًا, tr:wakīlan, gloss:vekîl veya gözetici} kılınmadığı bildirilir (17:54). Bu sınır, hatırlatmayı iletmekle dinleyicinin yanıtını yönetmeyi ayırır; odaktaki {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} böylece dinleyicinin alımlama karşılığı olarak kalır. 17:54 elçinin rolünü açık ederken geri çekilmenin nedenini açık bırakır.

Yakın bağlam şimdi yön değiştirmeyi, zararı giderme ve hâli dönüştürme kudretiyle karşılaştırır (17:56). İnsanların Allah’tan başka çağırdığı varlıkların sıkıntıyı gidermeye ya da durumu başka hâle çevirmeye {ar:لَا يَمْلِكُونَ, tr:lā yamlikūna, gloss:güç yetiremedikleri} söylenir; bu sınırlı alan {ar:كَشْفَ ٱلضُّرِّ, tr:kashfa aḍ-ḍurri, gloss:sıkıntıyı giderme} ve {ar:تَحْوِيلًا, tr:taḥwīlan, gloss:başka hâle çevirme} sözleriyle kurulur. Odaktaki {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitlendirdik} olağan okumasında sunuşu farklı biçimlerde verir; kökün yön ya da hâl değiştirme yüzü de bu iki ayrı hareketle yön değiştirme çağrışımı kurar. Böylece 17:56, çeşitlendirme imgesinin yanına zararı kaldırma ve hâli değiştirme kudretini koyar; benzerlik bu ayetin temasına aittir ve yaratılış alanına taşınmaz.

Çağrılan varlıkların yönü bir sonraki ayette başka türlü döner: onlar Rablerine yaklaştıracak yolu arar, hangilerinin daha yakın olduğu sorulur (17:57): {ar:يَبْتَغُونَ إِلَىٰ رَبِّهِمُ الْوَسِيلَةَ, tr:yabtaghūna ilā rabbihimu al-wasīlata, gloss:Rablerine yaklaştıracak bir yol ararlar}, {ar:أَيُّهُمْ أَقْرَبُ, tr:ayyuhum aqrabu, gloss:hangilerinin daha yakın olduğu}. Bu yan yana geliş yönelişi karşıtlık içinde aydınlatır: odaktaki muhataplar mesafe koyarken 17:57’de çağrılan varlıkların kendileri Rablerine yakınlık arar; yakındakilerin de yönelişte olduğu böylece görünür. Karşılaştırma geri çekilmenin nedenini açıklamadan, iki yönün ayrılığını gösterir.

Uyarı ve sınanma dili, artış fiilini başka bir sonuçla yeniden karşılaştırır (17:59, 17:60). İşaretlerin korkutma ve uyarı amacıyla gönderildiği, önceki toplulukların onları yalanladığı söylenir (17:59): {ar:بِٱلْءَايَٰتِ, tr:bi-l-āyāti, gloss:işaretlerle}, {ar:تَخْوِيفًا, tr:takhwīfan, gloss:korkutma ve uyarı}, {ar:كَذَّبَ, tr:kadhdhaba, gloss:yalanladı}. Ardından gösterilen rüya bir sınama diye nitelenir; korkutma ve Kur’an adı aynı sahneye girer (17:60): {ar:أَرَيْنَٰكَ, tr:araynāka, gloss:sana gösterdiğimiz}, {ar:فِتْنَةً, tr:fitnatan, gloss:bir sınama}, {ar:نُخَوِّفُهُمْ, tr:nukhawwifuhum, gloss:onları korkuturuz}, {ar:ٱلْقُرْءَانِ, tr:al-qurʾān, gloss:Kur’an}. Burada yine {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} denir, fakat artan şey büyük taşkınlıktır: {ar:يَزِيدُهُمْ إِلَّا طُغْيَٰنًا كَبِيرًا, tr:yazīduhum illā ṭughyānan kabīran, gloss:onları ancak büyük bir taşkınlıkta artırır}. Odaktaki ürküntü, 17:59’daki korkutma ve 17:60’taki sınanma-taşkınlık dili yanında yinelenen bir uyarı-alımlama örüntüsü olarak duyulur. 17:60’ın sonucu taşkınlık, 17:41’inki ise {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} sonucudur; ortak artış yapısı bu sonuçları özdeşleştirmeden karşılaştırır. Tekrarlanan tepki yerleşik bir yönelimi açığa çıkarıyor olabilir; bu yan yanalık uyarının tepkiye neden olduğunu belirlemez.

## Fâtiha’da Okur Yanıtı

Bu uyarı ve alımlanma çevresinden sonra tilavet, hatırlama amacına başka bir cevap sesi ekler. Fâtiha’da (1:5) birinci çoğul özne Allah’a kulluk ve O’ndan yardım isteme sözü verir: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:Yalnız sana kulluk eder, yalnız senden yardım dileriz}. Odaktaki {ar:لِيَذَّكَّرُوا۟, tr:li-yadhdhakkarū, gloss:öğüt alıp hatırlamaları için} zihinsel hatırlama anlamını korur; Fâtiha’daki ayrı dua, Tanrı’ya yönelen kulluk ve bilinçli anmayı okurun kişisel cevabı olarak getirir. Bu birinci çoğul dua sesi 17:41’in muhatap grubundan ayrıdır; cevap odak ayetin içinde değil, Fâtiha’nın kendi okunuşunda yer alır.

17:42’deki {ar:سَبِيلًا, tr:sabīlan, gloss:yol} sorusu, Fâtiha’da dosdoğru yolun istenmesi ve ardından nimet verilenlerin yolu ile yoldan sapmışların anılmasıyla yeniden duyulur (1:6, 1:7): {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet}, {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:ṣirāṭa alladhīna anʿamta ʿalayhim, gloss:nimet verdiklerinin yolu}, {ar:ٱلضَّآلِّينَ, tr:aḍ-ḍāllīn, gloss:yoldan sapmış olanlar}. Bu tilavet yakınlığı, dosdoğru yolu dileme ile 17:41’deki ürkek uzaklaşmayı karşıt yönelişler olarak duyurur. Fâtiha’daki “yoldan sapmışlar” ifadesi {ar:نُفُورًا, tr:nufūran, gloss:ürkerek uzaklaşma} sözcüğünün sözlük anlamını değiştirmez; dua edenlerle odak ayetin muhatapları da ayrı kalır. Okuyuşta belirginleşen, istenen yola yönelme ile geri çekilmenin yan yana gelişidir.

</source_prose>
