# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:15**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.middle.claims.json`

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
- Refer to source paragraphs as `31:15 ¶N`.

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

`(31:15 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:15",
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
        "citation": "(31:15 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_15/31_15.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_15/31_15.middle.claims.json \
  --ayah-ref 31:15
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_15/31_15.prose.editorial.tr.md`

<source_prose>
## Baskı, sınır ve bakım

31:15, {ar:وَإِن, tr:wa-in, gloss:ve eğer} ile iki ebeveynin tekil muhataba yönelttiği baskıyı koşullu bir ihtimal olarak açar. {ar:جَٰهَدَاكَ, tr:jāhadāka, gloss:ikisinin seni zorlaması} gücün ve dayanma sınırının sonuna dek zorlamayı da duyurur; {ar:عَلَىٰ, tr:ʿalā, gloss:-e doğru} bu çabayı belirli bir hedefe yöneltir ve {ar:أَن تُشْرِكَ, tr:an tushrika, gloss:ortak koşman} istenen eylemi talebin içeriği yapar. Fiilin IV. bâbdaki muzari mansup biçimi {ar:أَن, tr:an, gloss:-masını} tarafından yönetilir; ortak koşma tamamlanmış bir olay değil, yanıt bekleyen baskı hedefidir. Bu yoğunluk baskının ağırlığını gösterir; yöntemi, süresi, fiziksel şiddeti ya da tekrarlanan istismarı belirlemez. Koşul, her aile anlaşmazlığına değil, açıkça bu şirk talebine bağlanır.

İstenen ortaklığın yönü, {ar:بِى, tr:bī, gloss:Benimle} ile ilahî konuşmacıya bağlanır; sonraki {ar:إِلَىَّ, tr:ilayya, gloss:Bana} aynı birinci tekil yönelişi sürdürür. Buradaki ortaklık sıradan bir ortaklık değil, Allah’a ait sayılan yetkiyi başka bir varlığa da tanımaktır. {ar:مَا, tr:mā, gloss:şey/her ne} olası ortağı adsız bırakır: tek biri belirtilmez, olası ortakların tümü de özdeş kılınmaz. {ar:لَيْسَ لَكَ بِهِۦ عِلْمٌۭ, tr:laysa laka bihi ʿilm, gloss:ona dair bilgin yok} bu belirli ortaklık iddiası için bilme, tanıma ve gerçeği kavrama dayanağının bulunmadığını söyler; “ona dair” nesnesi adsız ortağa döner. “Sana ait” bilgi bağı, ebeveyn otoritesinin muhatabın bu özel öneriye ilişkin eksik dayanağını tamamlayamayacağını gösterir; ret ebeveyne duyulan hoşnutsuzluktan değil, tam bu iddianın dayanağından doğar. Olumsuzluk da bu iddiayla sınırlıdır, bütün bilgiler ya da her iddia hakkında genel bir kuşku kuralı kurmaz. 29:8’de ebeveyne iyilik, şirk baskısı, bilgi yokluğu, dönüş ve hesabın benzer bir düzende yan yana gelişi, baskı ile gerekçe arasındaki bağı genişletir; sözcük çözümlemesini birebir yinelemez.

Bu koşula verilen doğrudan yanıt {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:öyleyse ikisine itaat etme} buyruğudur: iki ebeveyn bu talimatın tarafıdır ve belirtilen isteğe uyulmaz. Yasak biçimi baskı doğduğunda yapılacak eylemi söyler; olmuş bitmiş bir davranışı betimlemez. İtaat sözcüğünün sağlanan başka bir kullanımındaki isteyerek ya da direnç göstermeden bir yöne uyma çağrışımı, kuvvetli baskıyla karşılaşınca reddi iradeyi koruyan bir duraklama gibi duyurur; buyruğun kapsamı yine yalnızca bu şirk talebidir. Aynı ikili zamir, biraz sonra eşlik emrinde yeniden görünür. 31:13 şirk koşmayı ağır bir yanlış sayarken, 31:14 annenin çocuğu taşımasını, zayıflığın üst üste gelişini, sütten kesmenin iki yılda tamamlanmasını ve Allah’a, ardından anne babaya şükretmeyi anlatır. Böylece reddedilen talep ile bakım geçmişi aynı ebeveyn bağı içinde ayrışır. Sütten kesilme, itaatin kesilip beraberliğin sürmesine sınırlı bir benzetme sunar; 31:14 aynı süreyi biyografik bilgi olarak da verir. Bakım geçmişi her talebi bağlayıcı kılmaz, ret de ihmal anlamına gelmez; aile bağı ise iyi muameleyle sürer.

Yasak emrinin ardından gelen {ar:وَصَاحِبْهُمَا, tr:wa-ṣāḥibhumā, gloss:ve ikisine eşlik et} içindeki bağlaç, aynı iki ebeveynle ilişkiyi sürdüren yeni ve olumlu bir yükümlülük ekler. Eşlik fiilinin yakın ve süreğen beraberliğin yanı sıra gözetim ve destek sunan kullanımı, emri yalnızca yakında bulunmaktan daha etkin kılar. {ar:مَعْرُوفًا, tr:maʿrūfan, gloss:iyi ve uygun biçimde} eşliğin nasıl yaşanacağını belirleyen mansup tarz sözcüğüdür: iyi sayılanı fiilen yapmak gerekir, fakat eylemlerin tümü tek tek sıralanmaz. 31:14’ün bakım ve şükür dili bu iyiliği ev içinde somutlaştırır; 31:17’de {ar:ٱلْمَعْرُوفِ, tr:al-maʿrūf, gloss:iyilik ve doğru sayılan} buyurulur, {ar:ٱلْمُنْكَرِ, tr:al-munkar, gloss:yanlış ve yadırganan} karşısında durulur ve {ar:وَٱصْبِرْ, tr:wa-iṣbir, gloss:sabret} denir (31:17). Sabır buyruğu, reddin ve ilişkinin baskı altında birlikte sürdürülebileceğini gösterir. Bu yankı, anne babayla güzel geçinmenin olağan nezaket anlamını koruyarak onu etkin bir iyilik hâline getirir. Eşliğin destek yönü her ihtiyacı karşılama borcu çıkarmaz ve reddedilen ortaklığa uyma yükümlülüğü doğurmaz; sınır içinde ailede iyi davranışı etkin kılar.

{ar:فِى ٱلدُّنْيَا, tr:fī al-dunyā, gloss:dünya hayatında} eşliğin alanını belirler. Dünya sözcüğünün yakınlık ve yaklaşma kullanımı, sonraki hayata göre içinde bulunulan ilk hayat anlamıyla birlikte duyulur; bu ikinci zaman ufkunu, bakım emrinden sonra gelen {ar:ثُمَّ إِلَىَّ مَرْجِعُكُمْ, tr:thumma ilayya marjiʿukum, gloss:sonra dönüşünüz Bana’dır} açar. Burada etkin olan, bu yakın/ilk hayat ufkudur; başka kalıplaşmış yakınlık anlamları bu ifadeye taşınmaz. Dünyadaki aile bağı gerçek ve sürmesi gereken bir yakınlıktır, ancak daha sonraki varış tek zaman ufku değildir. Bu yerel ifade bakımın değerini ya da anne babanın haklarını azaltmaz; bütün hukukî ve ahiret meselelerini tek başına çözmediği gibi ayrıntılı bir kronoloji de vermez. Eşlik böylece mevcut hayatta somut bakım olarak kalırken, sonraki varışı da görünür kılar.

Yakınlığın sürmesi, bir aile üyesinin ötekinin hesabını üstlenmesi demek değildir. 31:33’te {ar:لَا يَجْزِى وَالِدٌ عَن وَلَدِهِ, tr:lā yajzī wālidun ʿan waladihī, gloss:baba çocuğu adına karşılık veremez} ile {ar:وَلَا مَوْلُودٌ هُوَ جَازٍ عَن وَالِدِهِ شَيْئًا, tr:wa-lā mawlūdun huwa jāzin ʿan wālidihī shayʾan, gloss:çocuk da babası adına bir şeyi karşılayamaz} iki yönlü sınırı kurar; 39:7’de de kimsenin başkasının yükünü taşımaması, Allah’a dönüş ve yapılanların bildirimiyle birlikte anılır (31:33, 39:7). 31:33’te {ar:ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:al-ḥayāta d-dunyā, gloss:yakın dünya hayatı} yanıltıcı parıltıyı çağrıştıran {ar:ٱلْغَرُورُ, tr:al-gharūr, gloss:aldatıcı görünüş} ile yan yana gelir: sınanan, aile yakınlığının başkasının sorumluluğunu ikame edebileceği sanısıdır; ilişkinin kendisi aldatıcı sayılmaz. {ar:مَعْرُوفًا, tr:maʿrūfan, gloss:iyi ve uygun biçimde} için sağlanan “tanınan, ayırt edilen” kullanım da iyiliğin ilişki içinde görülebilir bir iz kazanmasını düşündürür. Böylece eşlik etkin bakımı korurken herkesin kendi hesabını kendisine bırakır. 31:14’teki Allah’a varış sözü ile 31:15’te dönüşün ardından yapılanların bildirilmesi, bu bakımın da aile tartışmasını aşan hesap ufkuna girdiğini gösterir (31:14, 31:15); bu ufuk şimdiki bakımı iptal etmez.

İlişki içindeki baskı, ebeveyn bağı ve dünya hayatının alanı, {ar:تُشْرِكَ, tr:tushrika, gloss:ortak koşman} biçiminin uzak bir sözlük kolundaki avı yakalayıp bağlayan kapan imgesine ayrı ayrı temas eder. {ar:جَٰهَدَاكَ, tr:jāhadāka, gloss:ikisinin seni zorlaması} talebin zorlayıcı yönünü, 31:14’teki bakım geçmişi ebeveyn bağını, {ar:فِى ٱلدُّنْيَا, tr:fī al-dunyā, gloss:dünya hayatında} da bu ilişkinin alanını kapan yorumuna taşır. Olağan şirk anlamı korunur; bu katkıların birleşmesi talebi dünyasal ilişkinin içinde yakalanma riski gibi duyurur. {ar:فَلَا تُطِعْهُمَا, tr:fa-lā tuṭiʿhumā, gloss:öyleyse ikisine itaat etme} reddi yakalanma hareketini keser; {ar:وَصَاحِبْهُمَا, tr:wa-ṣāḥibhumā, gloss:ve ikisine eşlik et} ise aynı iki kişiyle beraberliği sürdürür. Eşlik fiilinin beraber tutma çağrışımı, kopuş olmadan uyumsuzluğun sürebileceğini de duyurur. Kapan imgesi bu bağlantıların açtığı riskle sınırlıdır: ebeveynler gerçek avcı olarak çizilmez, baskı kasıtlı psikolojik yönlendirme ya da direnci aşama aşama tüketme diye belirlenmez; dünya hayatı da bütünüyle kötü sayılmaz.

## Yol ve rehber

Aileyle eşlik emrini ekleyen bağlaçtan sonra {ar:وَٱتَّبِعْ, tr:wa-ttabiʿ, gloss:ve izle} yeni bir yön verir: {ar:سَبِيلَ, tr:sabīla, gloss:yol} olanı izlemek. İzleme fiilinin nesnesi yoldur; söz, yürünüp ilerlenen bir güzergâhı ve doğru yöne götüren yolu birlikte duyurur, ayrıntılı bir harita çizmez. {ar:مَنْ أَنَابَ إِلَىَّ, tr:man anāba ilayya, gloss:Bana yönelen kimse} bu yolun ölçütünü soy ya da rütbe yerine Allah’a dönüş eylemiyle belirler; belirli bir tarihsel kişiyi seçmez. Sağlanan dönüş kullanımı yanlıştan vazgeçip Allah’a içtenlikle yönelmeyi de kapsar. Önceki şirk talebi ve ona verilen ret, bu dönüşün belirli bir yanlıştan Allah’a dönme olasılığını açar (31:13); izlenen herkesin geçmişte aynı yanlışı yaptığı sonucu çıkmaz. İlk {ar:إِلَىَّ, tr:ilayya, gloss:Bana doğru} seçilmiş rehberin yöneldiği yeri belirtir; bundan ayrı olarak ayet herkesin dönüşünü de bildirecektir.

Yolun kaynağını sınamak için 31:21, aynı izleme fiilini iki dayanağa uygular: {ar:مَآ أَنزَلَ ٱللَّهُ, tr:mā anzala llāh, gloss:Allah’ın indirdiği} ve konuşan grubun {ar:وَجَدْنَا عَلَيْهِ ءَابَآءَنَا, tr:wajadnā ʿalayhi ābāʾanā, gloss:atalarımızı üzerinde bulduğumuz} diye anlattığı yol (31:21). {ar:ٱتَّبِعُوا۟, tr:ittabiʿū, gloss:izleyin} ile {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izleriz} aynı ardından gitme eylemini hem vahye hem ataların sürdürdüğüne bağladığından, izlemek tek başına taraf seçmez; rehberliğin kaynağı sınanır. Bu, 31:21’de konuşan grubun yanıtıdır; bütün ataların yolu bilgisiz ya da yanlış sayılmaz, başka görüşteki anne babaya gösterilecek özen de ortadan kalkmaz. 31:13’teki şirk uyarısı ile buradaki vahiy-miras karşıtlığı rehberi, belirli bir yanlıştan Allah’a yönelen biri olarak duyurma olasılığını ayrı bağlamlardan açar; bu, bütün ebeveynlere ya da bütün atalara yöneltilmiş bir hüküm değildir (31:13, 31:21). Aileyle beraberlik ve yol için ölçüt böylece ayrı tutulabilir.

Yol imgesinin bedensel karşılığı, 31:19’daki açık buyruklarda belirir: {ar:وَٱقْصِدْ فِي مَشْيِكَ, tr:wa-qṣid fī mashyika, gloss:yürüyüşünde ölçülü ol} ve {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtika, gloss:sesini alçalt} (31:19). Orada yürüyüş ölçülür, ses kısılır; ahlaki yön bedenin adımında da duyulabilir. Bu gerçek yürüyüş sahnesi anne babayla beraberlik ya da dönüş hakkında yeni bir olay anlatmaz. 31:14’teki bakım dili, 31:21’deki rehberlik tercihi ve 31:19’daki yürüyüş ölçüsü, iki bağlılığı ayrı katkılarla görünür kılar: ebeveynle iyi ilişki sürerken Allah’a yönelen yol izlenir.

Bu güzergâhın ölçüsünü {ar:سَبِيلَ, tr:sabīla, gloss:yol} ile {ar:عِلْمٌۭ, tr:ʿilm, gloss:bilgi} arasındaki temas açar. Bilginin olağan anlamı bilme ve gerçeği kavramadır; başka bir kullanımda aynı söz bayrak, belirgin dağ, yol işareti ya da kenar deseni gibi tanıtan bir alameti de adlandırır. Bu alamet çağrışımı, bilgisizliği yön tayin ettirecek işaretten yoksun kalmak gibi duyurur; odaktaki ayet gerçek bir bayrak ya da dağ göstermez. 31:6’da {ar:سَبِيلِ ٱللَّهِ, tr:sabīli llāh, gloss:Allah’ın yolu} saptırmanın hedefidir; bu ayrı yol görüntüsü, başka bir akışın odaktaki güzergâhı kesebileceğini düşündürür (31:6). 31:20’de {ar:بِغَيْرِ عِلْمٍ, tr:bi-ghayri ʿilm, gloss:bilgi olmadan} dayanağı olmayan tartışmanın yanında {ar:هُدًى, tr:hudan, gloss:yol gösterme} ve {ar:كِتَابٍ مُّنِيرٍ, tr:kitābin munīr, gloss:aydınlatan kitap} yer alır (31:20). Kitap iki ayrı katkı sunar: sıralı harfleri incelenebilen yazılı bir kaynak olarak güzergâhın dayanağıdır; “aydınlatan” oluşuyla da tartışmanın bıraktığı yönü gösteren bir fener gibi okunabilir. Yazılı kaynak ve ışık, kitabı yol sözcüğünün eşanlamlısı yapmadan rehberliğin dayanağını ve yönünü görünür kılar. 6:153’te dosdoğru yol ayrılan yollardan ayrılır, 17:36’da bilinmeyenin izlenmemesi söylenir (6:153, 17:36). Bu bağlamlar, 31:21’deki miras karşıtlığını bütün mirasa hükme çevirmeden, odaktaki yolun bilgi ve rehberlik dayanağıyla nasıl sınandığını belirginleştirir.

31:21’deki “atalarımızı üzerinde bulduk” sözü, miras alınan güzergâhı üç ayrı ama birikimli imgeyle düşünmeye açar. {ar:تُشْرِكَ, tr:tushrika, gloss:ortak koşman} biçiminin uzak bir sözlük kolundaki sandal kayışı, sandalı ayağa bağlama imgesi üzerinden miras alınan güzergâha bağlılığı düşündürür; {ar:سَبِيلَ, tr:sabīla, gloss:yol} için verilen başka bir kullanım yol oluklarını ve belirgin izleri adlandırır; yol oluğu, önceden yürünmüş yolun bıraktığı aşınmış izi taşır. {ar:ٱتَّبِعْ, tr:ittabiʿ, gloss:izle} için sağlanan iz-sürme kullanımı da aranan yönün ardışık işaretlerini adım adım incelemeyi ekler. “Bulduk” sözü bu son kola ayrı bir temas verir. Birlikte, güzergâha bağlanmayı, önceki geçişin bıraktığı izi ve o izleri izleyerek yön bulmayı aynı miras-yol sorusunda buluştururlar; kayış oluğa, oluk iz-sürmeye dönüşmez. 31:21 gerçek kayışları ya da olukları, yahut gerçek bir soruşturmayı anlatmaz. “Atalarımızı üzerinde bulduk” sözü güzergâha aile bağını katar ama kendisi gizli bir kelime anlamı taşımaz; bu uzak benzetmeler de her aile geleneğini yanlış saymaz. Böylece 31:15’te yol, miras etiketiyle değil Allah’a yönelen kişinin rehber ölçütüyle seçilir.

İzlenen yönelişin sınavı kriz sona erdikten sonra da görünür. 31:32’de dalgalar gölgelikler gibi üzerlerine kapanıp birbirine karışarak kabarır; çevre seçenekleri örter ve kararsız bir baskı kurar. Bu örtülme içinde insanlar {ar:دَعَوُا ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu d-dīn, gloss:Allah’a yalnız O’na bağlılıkla dua ettiler} diyerek içtenlikle seslenir; {ar:ٱلدِّينَ, tr:d-dīn, gloss:bağlılık} burada boyun eğme ve yöneliş katmanlarını da taşır (31:32). Dalgalar yatışıp {ar:فَلَمَّا نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:fa-lammā najjāhum ilā l-barr, gloss:onları kurtarıp karaya çıkarınca} denildiğinde kurtuluş baskıdan ayrılır; çağrı sıkıntı içindeki gerçek dönüş olarak kalır. Kurtulanlar arasındaki {ar:فَمِنْهُم مُّقْتَصِدٌ, tr:fa-minhum muqtaṣid, gloss:aralarında orta yolu tutan var} farklı bir ölçü ya da dereceyi gösterir; bu kişinin hâli tek başına mahkûmiyet hükmü vermez ve samimiyetini yitirdiği sonucuna götürmez. 39:8’de sıkıntıda Allah’a dönüşün yanına nimet sonrasında unutma ya da saptırılma olasılığı da gelir (39:8); bu ihtimal herkes hakkında bir hüküm kurmaz. Böylece kriz dönüşü gerçek kalırken, 31:15’teki izleme buyruğu kurtuluş baskısı kalktıktan sonra da sürdürülen yönelişi sorar.

Reddin ardından seçilen yön, 31:22’deki mekânsal imgelerle belirginleşir. {ar:وَمَن يُسْلِمْ وَجْهَهُۥ لِلَّهِ, tr:wa-man yuslim wajhahu li-llāh, gloss:yüzünü Allah’a teslim eden} kişi yüzünü Allah’a çevirir; teslim burada bir şeyi elden bırakıp O’na yöneltmeyi de duyurur, yüz ise yön ve istikameti taşır (31:22). Ardından {ar:ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:istamsaka bi-l-ʿurwati l-wuthqā, gloss:sağlam bağa tutunur} tutuşu güvenilir ve dayanıklı bir dayanağa bağlar; {ar:عَاقِبَةُ ٱلْأُمُورِ, tr:ʿāqibatu l-umūr, gloss:işlerin sonu} da sonuç ufkunu açar (31:22). Yüzün Allah’a dönmesi reddin istikametini, sağlam bağa tutunma bu yönelişin dayanağını, işlerin sonu ise bağlılığın sonuç ufkunu gösterir; ebeveyn talebine uymama böylece sınırsız özerklik boşluğu değil, Allah’a yönelme ve sağlam bağlılık içinde okunur. 31:20’deki aydınlatan kitap rehberliğin kaynağını, 31:22’deki yüz ise yönelme hareketini öne çıkarır; bu ayrı mekânsal katkılar odaktaki ret ile izlenecek yol ilişkisini aydınlatır (31:20, 31:22).

İtaat emrinin yön verişi, 31:20’deki {ar:كِتَابٍ مُّنِيرٍ, tr:kitābin munīr, gloss:aydınlatan kitap} ile 31:22’deki {ar:وَجْهَهُۥ, tr:wajhahu, gloss:yüzü ve yönü} gibi birbirinden ayrı mekânsal görüntülerle tetiklenen uzak bir biçim benzerliği de taşır: {ar:تُطِعْهُمَا, tr:tuṭiʿhumā, gloss:ikisine itaat et} olağan anlamıyla ebeveynlere uymayı bildirirken, direk imgesi evi ayakta tutan dikey desteği ve yukarı doğru uzanmayı çağrıştırır; talebi eylem alanını düzenleyen bir dayanak gibi tasarlar. Kitap ışıklı bir kaynak, Allah’a dönük yüz belirli bir yöneliş sunar; direğin taşıdığı yapı bu ayrı katkıları eylemi düzenleyen dayanak imgesinde buluşturur. Böylece ret, keyfî yönsüzlük değil başka bir istikamete dönüş gibi duyulur. Bu biçim benzerliği uzak bir çağrışım olarak kalır: direk ve yükselme itaat fiilinin sözlük anlamı değildir; benzetme itaatin bütün koşullarını belirlemez.

## Dönüş ve bildirim

Seçilmiş rehberin Allah’a yönelişi ile bütün muhatapların dönüşü, aynı cümlede iki ayrı ölçekte yer alır. {ar:ثُمَّ, tr:thumma, gloss:sonra} dünya hayatındaki beraberlik ve yol buyruğundan dönüşe geçişi kurar; şimdiki davranışla sonraki varış arasına mesafe koyar, fakat ayrıntılı bir takvim vermez. İlk {ar:أَنَابَ إِلَىَّ, tr:anāba ilayya, gloss:Bana yönelip döndü} izlenmesi seçilen kişinin yönelişini anlatırken, ardından gelen {ar:إِلَىَّ مَرْجِعُكُمْ, tr:ilayya marjiʿukum, gloss:dönüşünüz Bana’dır} tüm muhatapların ortak varışını bildirir. Bu sıralama, izlenen güzergâhın yeniden Allah’a yönelmekle düzeltilebileceği bir devamlılığı da düşündürür; izleme emri kesintisiz bir adım dizisi dayatmaz ve her dönüşenin hâlini tek başına hükme bağlamaz. Tekrarlanan “Bana” yönü seçilmiş dönüş ile herkesin dönüşünü aynı istikamette buluşturur ve süren bir yöneliş düşündürebilir; kaç kez dönüldüğünü saymaz. 31:14’teki {ar:إِلَيَّ ٱلْمَصِيرُ, tr:ilayya al-maṣīr, gloss:son varış Bana aittir} bu varış ufkunu yaklaştırır (31:14). Dönüşün ardından eylemlerin bildirileceği vaadi, ölüm sonrası hesaplaşma ufkunu mümkün kılar; verilen bağlam ölümün ya da dirilişin nasıl ve ne zaman gerçekleştiğini anlatmaz, dönüş dili de yaşamların döngü halinde tekrarlandığını söylemez.

{ar:مَرْجِعُكُمْ, tr:marjiʿukum, gloss:dönüşünüz} önceki bir yere ya da duruma dönüşü anlatır. Hemen ardından gelen {ar:فَأُنَبِّئُكُم, tr:fa-unabbiʾukum, gloss:öyleyse size bildireceğim} ve 24:64’teki benzer dönüş-bildirim sırası, varışın bir iletiyi gönderene ulaştırıp cevapla karşılanması gibi duyulmasına izin verir (24:64). Bu çağrışımda eylemler kişiye geri dönen yanıtı andırır; bildirme anlamını dönüş fiili değil, onu izleyen söz taşır ve yazılı bir yanıt varsayılmaz. Bildirim fiilinin başındaki bağlaç dönüşü doğrudan izler, araya yeni bir koşul sokmaz; geçen süreyi de belirtmez. Tekil konuşmacının çoğul muhataplara seslenmesi sahneyi ebeveynlerle tek çocuk arasındaki gerilimden bütün dinleyenlere açar.

Bu bildirimin erişimi, 31:16’daki ayrı bir görüntüyle genişler. {ar:مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ, tr:mithqāla ḥabbatin min khardal, gloss:hardal tanesi ağırlığınca} bir şeyin {ar:فِي صَخْرَةٍ, tr:fī ṣakhratin, gloss:bir kayanın içinde} bulunması, küçüklük ile sertçe örtülmeyi bir araya getirir; {ar:لَطِيفٌ خَبِيرٌ, tr:laṭīfun khabīr, gloss:incelikle haberdar} inceliği, gizliyi ve iç gerçeği bilmeyi duyurur (31:16). 31:23’teki {ar:إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوا, tr:ilaynā marjiʿuhum fa-nunabbiʾuhum bimā ʿamilū, gloss:bize dönüşleri; yaptıklarını onlara bildireceğiz} dizisi de dönüşün ardından eylemlerin haber verilmesini sağlar; {ar:عَمِلُوا, tr:ʿamilū, gloss:eylemde bulundular} bilinçli yapılan işe, {ar:بِذَاتِ ٱلصُّدُورِ, tr:bi-dhāti ṣ-ṣudūr, gloss:göğüslerin özünde olanlar} ise eylemlerin iç kaynağına işaret eder (31:23). Böylece hesap görünür davranışla sınırlı kalmayabilecek bir ufuk kazanır. 31:34’te Allah’ın sürekli bilmesi, insanların gelecekte ne kazanacağını ve nerede öleceğini bilememesiyle karşılaştırılır; bu bağlam insan bilgisinin sınırını da hatırlatır (31:34). 31:16’daki küçük nesnenin mutlaka bir amel olduğu söylenmez: bu ayrı sahneler 31:15’te vaat edilen bildirimin ne kadar küçük ya da gizli olana erişebileceğini aydınlatır.

Son sözlerin içeriğini {ar:بِمَا, tr:bi-mā, gloss:her ne hakkında} ile açılan {ar:مَا, tr:mā, gloss:her ne/şey} ilgi cümlesi geniş tutar; onu izleyen eylem fiili bildirimin sınırını belirler ve tek bir davranış türü seçmez. {ar:كُنتُمْ, tr:kuntum, gloss:olageldiniz} geçmişte olma çerçevesini, {ar:تَعْمَلُونَ, tr:taʿmalūn, gloss:yaptıklarınız} muzari eylemi getirerek bildirilecek olana tek bir anın ötesinde zaman derinliği verir: hem davranış örüntüleri hem tekil işler bu ufka girer. Eylem, yapanın bilerek ortaya koyduğu iştir; sıklığı ya da süresi ölçülmez ve her birine ayrı bir iyi-kötü hükmü verilmez. Böylece odak, muhatapların zaman içinde yaptıklarının kendilerine bildirilmesine kapanır.

</source_prose>
