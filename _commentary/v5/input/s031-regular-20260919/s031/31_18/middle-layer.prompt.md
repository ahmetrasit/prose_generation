# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:18**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.middle.claims.json`

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
- Refer to source paragraphs as `31:18 ¶N`.

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

`(31:18 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:18",
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
        "citation": "(31:18 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_18/31_18.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_18/31_18.middle.claims.json \
  --ayah-ref 31:18
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_18/31_18.prose.editorial.tr.md`

<source_prose>
## Yanağın yönü

31:18, insanlara yönelen yüz hareketini ve ortak yerdeki yürüyüşü iki ayrı yasak olarak kurar: {ar:تُصَعِّرْ خَدَّكَ لِلنَّاسِ, tr:tuṣaʿʿir khaddaka li-n-nās, gloss:insanlara yanağını çevirme} ve {ar:وَلَا تَمْشِ فِى ٱلْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī al-arḍ maraḥan, gloss:yeryüzünde taşkınlıkla yürüme}. Ardından bu davranışları {ar:إِنَّ ٱللَّهَ لَا يُحِبُّ كُلَّ مُخْتَالٍ فَخُورٍ, tr:inna Allāha lā yuḥibbu kulla mukhtālin fakhūrin, gloss:Allah kendini üstün görüp övünen herkesi sevmez} hükmüyle bir karakter tipine bağlar. Böylece bakış önce başkalarıyla karşılaşan bedene, sonra o bedenin bastığı ortak zemine, en sonunda da hareketlerde beliren üstünlük iddiasına yönelir.

İlk yasağın hedefi, yüzün yana çevrilmesidir. {ar:لَا, tr:lā, gloss:yapma} parçacığı {ar:تُصَعِّرْ, tr:tuṣaʿʿir, gloss:yanağını yana çevir} fiilini cezm ederek bu hareketi durdurur; kibir yorumu ayrı bir sıfattan değil, yüzün insanlara yönelen bu hareketinden doğar. Fiilin orta ünsüzündeki şedde, Form II muzari biçimini belirginleştirirken yana eğilen beden hareketini sıkıştırılmış biçimde duyurur. Yakın biçimlerden ayrılan bu yüzey, ayetteki yanak dönüşünü belirginleştirir; fiilin seyrek kullanımı da yanak nesnesi ve insanlara yönelen tamamlayıcıyla daha özgül bir toplumsal jesti öne çıkarırken kelime ailesinin diğer kullanımlarına yer bırakır. Şedde dönüşü hem anlamda hem seste sıkıştırır. Yüzün, yanağın ya da boynun düz konumdan yana eğilmesini anlatan kullanım bedende görünür; eğriliği patolojiye benzeten dal da bu jesti resmeder, klinik bir tanı koymaz.

Jestin yerini {ar:خَدَّكَ, tr:khaddaka, gloss:yanağını} gösterir: yanak, göz çukuru ile çene arasındaki yüz yanıdır ve fiilin doğrudan nesnesidir; iyelik eki muhatabın kendi görünen yüzeyini öne çıkarır. {ar:لِلنَّاسِ, tr:li-n-nās, gloss:insanlara} hareketin toplumsal yönünü insanlarla kurulan ilişkiye sabitler; saik ile tekil mağdur açık bırakılır. Belirli çoğul biçimdeki {ar:النَّاسِ, tr:al-nās, gloss:insanlar}, topluluğu ve gerektiğinde üyelerini kapsar; böylece uyarı tek bir özel hakaret sahnesinden daha geniş, kamusal karşılaşma alanına yönelir. Yanak bedensel parça olarak kalırken, insanlara çevrilen yüz karşılaşmanın kamusal yüzünü taşır.

Yüzün bu küçük yüzeyi, yürüyüşle birlikte ortak zemindeki daha geniş bir çizgiye açılır. {ar:خَدَّكَ, tr:khaddaka, gloss:yanağını} taşıyan kelime ailesinde toprakta açılan uzun oluk anlamı da vardır; ayrı bir tetikleyici olan {ar:تَمْشِ فِى ٱلْأَرْضِ, tr:tamshi fī al-arḍ, gloss:yeryüzünde yürümen} bu ince beden çizgisini üzerinde yürünülen geniş geçişe yankılatır. Yanak bedensel anlamını korurken yüz çizgisi ortak rota üzerinde bir iz düşüncesi kazanır. Aynı ailenin yalın bir kullanımı yolu, başka belirli bir biçimi ise yol yüzeyindeki izi ve oluğu adlandırır. Gerçek yürüme güzergâhı bu iki dalı harekete geçirince, yüz çevirme karşılaşmadan uzaklaşan bir sosyal çizgi gibi duyulabilir; beden yüzeyi ortak rotada iz bırakır. Bu bağlantı, yanağı “yol”a çevirmek yerine yanak ile güzergâh arasında bir yüzey yankısı kurar.

Yanağın dönüşü ile yürüyüş rotası, aynı kelime ailesindeki başka hareketleri de ayrı ayrı görünür kılar. {ar:تُصَعِّرْ, tr:tuṣaʿʿir, gloss:yanağını yana çevir} sözcüğünün bir kullanımı ilerleyen devenin yana yön vermesini anlatır. Yeryüzünde yürüme güzergâhı bu imgeye temas edince üst bedenin açısı yolu yana yönlendiriyor gibi görünür; bu dal bedensel jestin yön verici etkisini belirginleştirir, ayetin sahnesinde bir deve bulunmaz. Ailenin develerin ayrılıp dağılmasını anlatan başka bir kullanımı, insan topluluğu ve ortak yürüyüş alanı içinde geri çekilen yüzü sürüden kopuşa benzetir; bu karşılaştırma toplumsal ayrılığı düşündürür, deve sürüsünü ayete taşımaz. Kesme ve bütünlüğü bozma kullanımıysa geri çekilen ilişkinin ortak çizgide bıraktığı kopmayı duyurur; bedensel eylem yanağı çevirmek olarak kalır.

Bu çizgi, toplumsal konum imgesini de açar. {ar:خَدَّكَ, tr:khaddaka, gloss:yanağını} taşıyan ailenin bir başka kullanımı insan topluluğunu ya da katmanları adlandırır. {ar:النَّاسِ, tr:al-nās, gloss:insanlar} topluluğu ile {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} kişinin statü iddiası bu dalı harekete geçirince, jest sınıflar arasındaki konumu işaretler gibi okunabilir; bu bağlantı belirli bir sınıf düzeni tayin etmez. İnsanları adlandıran sözün sınırlı bir kullanımındaki “yakın yan” anlamı yüzün yönünü bir ilişki eksenine yerleştirir. Göz bebeğinde görünen küçük insan yansımasını anlatan ayrı bir dal ise başkasının bakışını yansıtıcı yüzey kılar: yanağın dönüşü ile üstünlük iddiasını taşıyan suret karşılaşınca yüzünü kaçırmak karşılıklı bakıştan uzaklaşma gibi duyulur. Bu aynasal çağrışım kelime ile jestin keşifsel birleşimidir; göz ve göz bebeği ayette ayrıca anlatılmaz.

## Yürüyüşün ölçüsü

İlk yüz hareketinin ardından gelen kısa {ar:وَ, tr:wa, gloss:ve} yanına yürüyüşü ikinci bir davranış alanı olarak ekler: {ar:وَلَا تَمْشِ فِى ٱلْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī al-arḍ maraḥan, gloss:yeryüzünde taşkınlıkla yürüme}. İlk iki {ar:لَا, tr:lā, gloss:yapma} eylemleri cezm ederek durdurur; yüzü çevirme ile yürüme ayrı buyruklardır ve ardından gelen karakter hükmü onları aynı profile bağlar. Bu iki hareket ortak sahnede buluşur: {ar:خَدَّكَ, tr:khaddaka, gloss:yanağını} ve {ar:تُصَعِّرْ, tr:tuṣaʿʿir, gloss:yanağını yana eğme} üst bedenin açısını, {ar:تَمْشِ فِى ٱلْأَرْضِ, tr:tamshi fī al-arḍ, gloss:yeryüzünde yürüme} gerçek güzergâhı sağlar. {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} ile {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} ise adımın ölçüsünü büker; beden açısı ile güzergâh böylece ortak zeminde tek bir mekânsal bozulma imgesine katkıda bulunur, iki buyruk yine ayrı kalır.

Bu ikinci eylemin olağan anlamı {ar:تَمْشِ, tr:tamshi, gloss:yürümen} ile duyulur: Form I’deki fiil geçişsiz ve sıradan bir yürüme hareketidir; yasak parçacığı onu cezmli yapar. Ardından gelen {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍ, gloss:yeryüzünde} yürüyüşün yerini, belirli tekil {ar:ٱلْأَرْضِ, tr:al-arḍ, gloss:yeryüzü} ise bilinen, birlikte yaşanan fiziksel zemini gösterir. “Alan” yankısı bu ortak zemin içinde duyulur; söz belirli bir parseli değil üzerinde birlikte yaşanan yeryüzünü öne çıkarır. Cümle önce nerede, sonra nasıl yüründüğünü bildirir.

Nasıl sorusunun cevabı {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} sözünde belirir. Kelime sıradan neşeden daha güçlü, ölçüyü aşan ve kişiyi yerinde duramayacak kadar harekete çağıran bir canlılık taşır. Mansup hâl sözü yürüyüşün tarzını niteler; yasak yürüyüşü ve sevinci genelleştirmek yerine taşkınlığın yürüyüşte sergilenme biçimini sınırlar. Hâl kuruluşu hafif bir saik gölgesi de taşır, ancak cümlede önde olan yürüyüşün tarzıdır ve belirli bir niyeti açık bırakır. Yeryüzü ise göğün karşısında aşağıda bulunan, üzerinde yaşanan fiziksel yerdir; bu ikinci buyruğun sahnesini ortak zemin olarak belirler.

Yürüyüşün biçimi hemen sonraki buyrukta yeniden ele alınır: {ar:وَٱقْصِدْ فِى مَشْيِكَ, tr:wa-qṣid fī mashyika, gloss:yürüyüşünü ölçülü kıl} (31:19). Bu kez hareket sürer, ölçüsü değişir. Buyrukla ilişkilendirilen doğrultu ve iki uç arasındaki orta yol imgeleri, taşkın sevincin ve ağır gösterişli adımın karşısına yön ile oran koyar; bu bağlamsal imgeler sözcüğü tek bir zorunlu sözlük karşılığına kapatmadan yürüyüşe ölçü boyutu ekler. Ardından {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:wa-ghḍuḍ min ṣawtika, gloss:sesini alçalt} (31:19) ölçüyü yürüyüşten işitilen sese taşır. Adım sürerken dışavurumun şiddeti de ayarlanır; yüz, gösterişli yürüyüş ve övünmeyle kurulan kamusal tavır böylece ortak bir dışavurum düzleminde buluşur.

Bu ölçü, önceki buyrukların bulunduğu bağlamla da konuşur. Namazı kılma, iyiliği emretme ve kötülükten sakındırma görevlerinin ardından (31:17) {ar:وَٱصْبِرْ, tr:wa-ṣbir, gloss:sebat et} çağrısı ve {ar:عَزْمِ ٱلْأُمُورِ, tr:ʿazmi l-umūr, gloss:kararlılık isteyen işler} ifadesi gelir. Sabır ve kararlılık, ardından gelen ölçülü adım ve alçak sesle birlikte okunduğunda enerjiyi söndürmeden yönünü ve gösterişini düzenleyen bir çizgi kurabilir (31:17, 31:19). Bu okumada tevazu, kamusal görevi ve hareketi sürdürürken ölçüyü korur; edilgenlik değildir. Buyrukların ayrı öğütler olarak okunması da yerini korur. Ortak düzenleme çizgisi bu bağlamlar arasındaki yorumlayıcı bağlantıdır ve 31:18’in kibirli gösterişe koyduğu yerel sınırı aşmadan ona ek bir yön verir.

{ar:تَمْشِ, tr:tamshi, gloss:yürüme} eylemi, yeryüzünün yürüyene koyduğu bedensel sınırla da duyulur. Yeryüzünü yarıp geçememeyi ve dağların boyuna erişememeyi hatırlatan uyarı (17:37), aynı yürümeyi böbürlenerek yapmayı da yasaklar. İnsan bedeni bastığı yeri delemez, dağların yüksekliğine erişemez; ortak zemin böylece yürüyenin fiziksel ölçeğini belirler. {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan taşkınlık} bu ölçüye karşı duyulan canlılığı taşır; yürüyüşteki taşkınlık bedensel erişimi büyüten bir kudret olarak değil, sınır içindeki bir tavır olarak kalır.

## Üstünlük iddiasının görünüşü

İki eylem yasağından sonra {ar:إِنَّ, tr:inna, gloss:şüphesiz} vurgulu bir bildirim açar; {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adı bu edatın yönettiği mansup biçimdedir ve {ar:لَا يُحِبُّ, tr:lā yuḥibbu, gloss:sevmez} yüklemi hükmü tamamlar. Bakış, ilk hareketin toplumsal hedefi olan {ar:النَّاسِ, tr:al-nās, gloss:insanlar} topluluğundan ikinci eylemin ortak yerini belirten {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍ, gloss:yeryüzünde} sözüne, oradan da {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adına uzanır. İnsan adabı böylece çevrenin beğenisinin ötesinde Allah adına kurulan bir değerlendirmeye bağlanır. Burada Allah adı, köken türetiminden çok hükmün öznesi olarak işlev görür. Son {ar:لَا, tr:lā, gloss:olumsuzluk parçacığı}, ilk iki yerdeki yasaklayıcı parçacığın aynısı olsa da bu kez bildirim biçimindeki merfu fiili ve nesne öbeğini olumsuzlar; karakter tipi hakkında hüküm verir, üçüncü bir davranış buyruğu kurmaz.

Olumlu bağlılık ve sevgi bildiren {ar:يُحِبُّ, tr:yuḥibbu, gloss:sever} fiilinin olumsuzlanması, bu tipe yönelen süreğen tutumu anlatır; hüküm bir anlık tepkinin ölçüsünü değil ilişki yönünü belirler ve ayrı bir nefret eylemi kurmaz. Buradaki sevgi fiili Form IV’tür; son {ar:لَا, tr:lā, gloss:olumsuzluk parçacığı} olumlu bağlılığı geri çeker. Fiilin tek nesnesi {ar:كُلَّ مُخْتَالٍ فَخُورٍ, tr:kulla mukhtālin fakhūrin, gloss:her kendini üstün görüp övünen kişi} öbeğidir. {ar:كُلَّ, tr:kulla, gloss:her} hükmü bu nitelikleri taşıyan herkes için kurar; kapsamı bütün insanlara yaymaz. Aynı kendini üstün gören ve övüngen tipin başka bir yerde anılması bu karakter alanını pekiştirir (57:23). Yeryüzünde haksız taşkın sevinci anan bağlam da {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} sözünün ölçüsünü belirginleştirerek sıradan mutluluktan ayırır (40:75).

Öbeğin iki niteliği aynı karakter profilinin ayrı boyutlarını kurar: {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} içteki üstünlük duygusunu, {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} ona eklenen dışa vurulan övünmeyi bildirir. Faʿūl kalıbındaki ikinci nitelik yoğun ve yerleşik bir karakter özelliğidir; tek bir övünme anından çok alışkanlık hâlindeki tutumu anlatır, belirli bir rakibi ise açık bırakır. Verilmiş nimetle övünmeme uyarısı bu karakter alanını açarken (57:23), mal ve çocuklar üzerine karşılıklı övünme toplumsal karşılaştırma yüzünü belirginleştirir (57:20). Hâl sözü olan {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} ile iki karakter niteliğinin tenvinli sonlanışları davranıştan kişilik tasvirine ses bağı kurar; son {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} biçimindeki uzun ses bu yankıyı tamamlar, anlamları birleştirmez.

Kişiyi üstün gören {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} söz ailesinde görünür ya da zihinde kurulmuş benzerlik ve suret anlamı da vardır. Yürüme ve övünme gibi ayrı, görünür davranışlar bu kullanımı tetikleyince üstünlük iddiası kamusal bir benlik sunumu olarak sahnelenir: gerçek yüz ve adımlar, sergilenmek istenen imgeyi taşır. Benzerlik alanı gölgeye, yansımaya, düşe ya da zihinde canlanan bir biçime kadar uzanabilir. İnsanlara yönelen yüz ve övünme bu sureti başkasının bakışıyla karşı karşıya getirir; bakış, gösterilen benlik için yansıtıcı yüzey olur. Bu aynasal okuma gerçek bir ayna sahnesi kurmaz ve kişinin üstünlük iddiasının yanlışlığını kanıtlamaz. Aynı ailenin kesin bilgiden yoksun tasarım ya da sanı kullanımı da insan hedefi ve açık övünmeyle birleşince, üstünlüğün kurulmuş bir iddia olarak sunulmasını düşündürür; bu dal iddianın doğruluğunu hükme bağlamaz.

Bu görünür benlik adımda da belirir. {ar:تَمْشِ, tr:tamshi, gloss:yürümen} ve taşkın hâli belirten {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} ile yan yana gelen {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} ailesinin ağır ve gösterişli yürüme kullanımı, içteki üstünlük duygusunu bedende sergilenen statüye taşır; bu çağrışım sıfatın kendisini yürüme fiiline dönüştürmez. İnsanlara dönük yürüyüş izleyici ihtimalini açar; metin izleyici tepkisini ya da rakibin yenilgisini anlatmaz. {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} kişinin geçmiş başarılarını veya sahip olduklarını sıralayarak böbürlenmesini de düşündürür; ayet bu övünmenin içeriğini belirtmez. Ailenin ayrı bir kullanımı üstünlük iddiasına karşılaştırmalı bir boyut ekler. İnsanlara yöneliş ve kendini üstün görme bu kıyasa zemin sağlar; belirli rakip ve yarış bağlamın dışında kalır.

Dışa dönük bu benlik sunumu, başka kamusal sahnelerle yan yana geldiğinde statü gösterisi olarak daha belirginleşir. İnsanların gösteriş için evlerinden çıkması (8:47), yapmadıkları işle övülüp övgü bekleyenlerle gerçekte yaptıkları arasındaki açıklık (3:188) ve süs, karşılıklı övünme, mal ve çocuklar üzerine ölçüşme (57:20), kamusal karşılaştırmanın ayrı yüzlerini gösterir. Bu bağlamda yanağı çevirme {ar:تُصَعِّرْ خَدَّكَ, tr:tuṣaʿʿir khaddaka, gloss:yanağını çevirme}, yürüme {ar:تَمْشِ, tr:tamshi, gloss:yürüme} ve suret yankısı taşıyan {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} ile {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} nitelikleri başkalarının önünde rütbe sergileme ihtimalini birlikte kurar; bu okuma gösteriyi görünür kılar, sonucunu ya da bir kazananı belirlemez. {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} ailesindeki ayrı bir kullanım başarı karşısındaki şaşma ve beğeniyi birleştiren ünlemi ekler. İnsanlara dönük hareket ve övünmeyle temas edince davranış hayranlık bekleyen bir gösteri gibi duyulabilir; ayette sözel bir övgü karşılığı anlatılmaz.

Kişinin kendine biçtiği yüksek yer, yücelik ve büyüklüğün Allah’a nispet edildiği bağlamla karşılaşır (31:30); dünya hayatının aldatıcılığına ilişkin uyarı da üstünlük iddiasının dayanağını sorgulatır (31:33). {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} üzerinden taşınan böbürlenme, {ar:ٱلْعَلِيُّ ٱلْكَبِيرُ, tr:al-ʿAliyy al-Kabīr, gloss:en yüce ve en büyük} niteliği karşısında insanın kendi kurduğu suretle yücelik kazanamayacağını düşündürür. Bu bağlamlar yanağın ve yürüyüşün bedensel yüzeyini korurken, üstünlük iddiasının temelini ve görünüşün güvenilirliğini sorgular. Karşılıklı övünme ve biriktirme sahnesi de iddianın toplumsal statü yarışına katılabileceğini düşündürür (57:20); bu, kelimenin sözlük karşılığı değil, bağlamın açtığı genişlemedir.

{ar:مَرَحًا, tr:maraḥan, gloss:taşkın yürüyüş hâli} için aktarılan sınırlı kullanım, yeni bir tulumun suyla doldurulup dikişlerinin ıslatılarak hazırlanmasını anlatır; bu dal kaba biçim verme ve dolum işlemlerini birleştirir. Sevgi fiilinin bağlı olduğu ailedeki başka biçimler bir kabın dolmasını ve içip ilk kez doygunluğa ulaşan hayvanı, ayrı bir kullanım ise büyük saklama küpünü anlatır. Bu dalların her biri iç hacmin dolması veya doyuma ulaşma ilişkisine katkı verir; birlikte taşkınlığı içeride biriken basınç gibi duyururlar. Ardından {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} ailesindeki pişmiş toprak kap, {ar:ٱلْأَرْضِ, tr:al-arḍ, gloss:yeryüzü} ile malzeme bağını kurup bu iç basınca sert bir dış kabuk ekler. Böylece dolan iç hacim ile pişmiş kabın dış yüzeyi, iç basınç ve dış gösteriş benzetmesinde ayrı katkılar sunar. Bu söz bağlantısı gerçek su, susuzluk ya da kaplardan oluşan bir olay anlatmaz; kapların kırılganlığı hakkında da sonuç vermez. Sevgi, taşkın hâl ve övüngen kişi olağan anlamlarında kalır.

## Yüzün ilişki içindeki yeri

İnsanlara çevrilen yanağın toplumsal anlamı, yanlış buyruğa uymadan da iyi ilişkiyi sürdürmenin mümkün olduğunu gösteren bağlamla genişler. Ebeveynlerin yanlış çağrısına uymama buyruğunun ardından onlarla dünyada iyi biçimde yoldaşlık etme ve Allah’a yönelen kişinin yolunu izleme emri gelir (31:15): {ar:وَصَاحِبْهُمَا فِى ٱلدُّنْيَا مَعْرُوفًا, tr:wa-ṣāḥibhumā fī al-dunyā maʿrūfan, gloss:dünyada onlarla iyi biçimde yoldaşlık et} ve {ar:وَٱتَّبِعْ سَبِيلَ مَنْ أَنَابَ إِلَىَّ, tr:wa-ttabiʿ sabīla man anāba ilayya, gloss:Bana yönelen kişinin yolunu izle}. Yanlış buyruğa hayır demek beraberliği bitirmez; yönü ilkeli bir seçim belirler, iyi davranış ise sürer (31:15). {ar:خَدَّكَ, tr:khaddaka, gloss:yanağını} fiziksel yanak anlamını korurken bu komşu buyrukla okunduğunda anlaşmazlık karşısında geri çekilmeyen bir mevcudiyeti de düşündürür. Allah’a yönelen kişinin yolu {ar:تَمْشِ, tr:tamshi, gloss:yürüme} imgesiyle buluşunca kişi edilgen uyum yerine seçtiği ahlaki yönde ilerler. İnsanları adlandıran {ar:النَّاسِ, tr:al-nās, gloss:insanlar} söz ailesindeki bir kullanım yabancılığın kalkıp aşinalık ve rahatlığın doğmasını, bir başkası ise yanında bulunup yabancılığı gideren yoldaşı anlatır. Bu yakınlık 31:15’te ebeveynlerle etkin beraberlik olarak görünür; bütün insan ilişkilerine yayılması benzetmeli bir genişletmedir. Böylece yorum genişlese de 31:18’in yanağı küçümseyerek çevirme sınırı yerinde kalır.

İlişkide yüz çevirmek ile sevgi hükmü arasındaki bağ, başka ayetlerin toplumsal çevresiyle de belirginleşir. Aynı kendini üstün gören ve övüngen tipin sevilmediği söylenirken anne-babaya ve komşuya iyilikten söz edilmesi (4:36), yanağın çevrilişini toplumsal davranış alanına yerleştirir. Barışçı insanlara adaletle davrananların Allah’ın sevgisiyle anılması da olumlu bağlılığın adaletle ilişkisini gösterir (60:8). Böylece {ar:لَا يُحِبُّ, tr:lā yuḥibbu, gloss:sevgi göstermez} ile {ar:تُصَعِّرْ خَدَّكَ, tr:tuṣaʿʿir khaddaka, gloss:yanağını çevirme} yan yana okunduğunda yüz hareketi seçilmiş bir toplumsal mesafe gibi duyulur. Bu bağlamlar jestin ilişki boyutunu aydınlatır; ilişkinin tüm sahnesini tek başına belirlemez.

Yön değişimi bu kez bütün yüz üzerinden görünür olur. Allah’a yüzünü yöneltmekten söz eden {ar:وَجْهَهُۥٓ إِلَى ٱللَّهِ, tr:wajhahu ilā Allāh, gloss:yüzünü Allah’a yöneltmesi}, 31:18’de insanlardan çevrilen {ar:خَدَّكَ, tr:khaddaka, gloss:yanağın} karşısına başka bir ilişkiye yönelmiş yüzü koyar (31:22). Aynı bağlamdaki {ar:بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:bi-l-ʿurwati l-wuthqā, gloss:en sağlam bağa} imgesi istikrarı gösterişli üstünlükten sağlam bir ilişkiye taşır (31:22). Yüzünü Allah’a yöneltmek, denetimi bırakıp bir yön seçmek ve iyilikle birlikte teslim olmak anlamı taşır; insanlara açık yanağın onay ya da rütbe aramak yerine Allah’a yöneliş içinde okunmasını da mümkün kılar. Yatay toplumsal yüz ile Allah’a yönelmiş bütün yüz arasındaki ilişki, iki ayet arasında dilbilgisel bağ değil yorumlayıcı bir genişletmedir; 31:22’nin genel iman ve iyilik çerçevesi de kendi başına yerini korur. Bu karşı-imge, somut yanak yasağını korurken ona başka bir ilişki yönü ekler.

Yüzün yönelmesi, algı ve kabulün kapanmasıyla da yankılanır. Başka bir yerde kişi böbürlenerek arkasını döner, sanki sözü işitmemiş gibi davranır; kulaklarında ağırlık varmış gibi gösterilir (31:7): {ar:وَلَّىٰ مُسْتَكْبِرًا كَأَن لَّمْ يَسْمَعْهَا, tr:wallā mustakbiran ka-an lam yasmaʿhā, gloss:böbürlenerek dönüp sanki onu işitmemiş gibi}. Bu dizide işitmek söyleneni duymayı, dinlemek ise alıcı ve kabul edici duruşu da taşır; görme, duyma ve fark etme kanallarının kapanması bedensel bir engel gibi kurulur (31:7). 31:18’de insanlara çevrilen yanak, bu sahneyle birlikte seçilmiş bir tanımama tavrı olarak okunabilir; bu kesişim yüz jestine algısal kapanma boyutu ekler, “işitmek” anlamını yüklemez. 31:7’nin açık çerçevesi vahyin reddidir; insanlara dönük tanımama ise yüz hareketi ve toplumsal hedef üzerinden kurulan ihtiyatlı bir genişletmedir.

## Alınmış zemin ve bilinmeyen yol

Övünmenin karşısına alınmış iyilik fikrini koyan bağlamlar, yeryüzünü de kişinin kendi başarısından ayırır. Şükretme buyruğu nimeti vereni tanımayı, şükredenin yararının ise kendisine döndüğünü söyler (31:12): {ar:أَنِ ٱشْكُرْ لِلَّهِ, tr:ani ushkuri lillāhi, gloss:Allah’a şükret}. Bu tanıma, {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen} kişinin başarı ya da sahipliğini kendi üstünlüğüne yazan yönüyle karşı karşıya gelir. Görünür ve gizli nimetlerin birlikte anılması, sergilenen sahipliği rütbe kanıtı yapan hesabı görünmeyen iyilikle sınırlar (31:20). Göklerde ve yerde bulunanların insanlara sunulan yararlarla anılması da (31:20), {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍ, gloss:yeryüzünde} yürümeyi kişinin kendi başarısı değil, üzerinde yaşadığı alınmış zemin olarak düşündürür. Bu bağlantı, nimetleri kendine mal eden bir övünme biçimini aydınlatır; her övüngenin bunu bilerek yaptığı ya da gizli iyiliği reddettiği iddiasında bulunmaz.

Bu ölçekte küçücük ve gizli olan da görünürlükten kaçmaz. Hardal tanesi kadar bir şey kaya içinde, göklerde ya da yerde bulunsa Allah’ın onu ortaya çıkaracağı söylenir (31:16); küçük ve saklı olan da bilgi ve karşılığın dışına düşmez. Böylece insanların önündeki büyük gösteri tek ölçü olmaktan çıkar: {ar:تَمْشِ, tr:tamshi, gloss:yürüme} içindeki küçük bir hareket bile ahlaki ölçekte sıfır değildir. Hardal tanesi, görünmeyenin de kuşatıcı bilgi içinde bulunduğunu pekiştirir (31:16); nimeti kişisel başarıya dönüştürme biçimini tek başına açıklamaz. Sevgi bildiren {ar:يُحِبُّ, tr:yuḥibbu, gloss:sever} fiilinin bağlı olduğu söz ailesinde tane, yenebilir tohum ya da ekilebilir çekirdek anlamları da bulunur. Ayrı bir tetikleyici olan {ar:ٱلْأَرْضِ, tr:al-arḍ, gloss:yeryüzü} ile karşılaşınca sevgi çevresinde hafif bir ekim imgesi belirir; yeryüzünün yumuşak, verimli toprak anlamındaki sınırlı kullanımı da bu tane çağrışımına dokunur. Ortak fiziksel zemin ile sevgi anlamı önde kalır; ekim ve büyüme ayette anlatılan süreçler değil, bu bağlantının eklediği hafif yankıdır. Hardal tanesinin küçük ama bilinen ölçüsü tohum çağrışımını destekler (31:16); iki dal ayrı sözlük anlamları olarak kalır.

Yeryüzünün ortak zemini, taşkın yürüyüşü alınmış gelişmeyle karşılaştıran bir tarımsal yankı da açar. {ar:مَرَحًا, tr:maraḥan, gloss:taşkın yürüyüş hâli} için sınırlı kullanımlardan biri yağmurdan sonra hızla yeşeren toprağı, bir diğeri ilk başağını çıkaran ekini anlatır. Yere sağlamlık verilmesi, onun insanlarla sarsılmasının önlenmesi ve orada bitkinin büyütülmesi bu görüntülere zemin sağlar (31:10). Sabit zemin büyümeyi taşır, filiz ise gelişmenin zeminden geldiğini görünür kılar; bunun karşısında {ar:تَمْشِ, tr:tamshi, gloss:yürüyüş} içindeki böbürlenme, alınmış gelişmenin kendiliğinden üretilmiş taklidi gibi okunabilir. Bu bağlantı, {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinçle} sözünü tarım anlamına çevirmez; taşkın yürüyüş ile büyüme imgesini karşılaştırır. Hardal tanesi küçük ve saklı olanın da ölçüde bulunduğunu ekler (31:16), böylece görünür gösterinin karşısında küçük eylemlerin önemini açar. 31:10 ve 31:16’nın yaratılış gücü ile Allah’ın bilgisi hakkındaki daha genel okuması da yerini korur; kendiliğinden büyüme taklidi, bu bağlamlarla kurulan keşifsel bir genişletmedir.

Yürümenin zemine bağımlılığı, daha geniş bir yolculuk imgesiyle de ölçülür. Gök cisimlerinin, güneş ve ay dâhil, akışlarını sürdürürken her birinin belirlenmiş bir vakte doğru gittiği anlatılır (31:29). Bu bütün ve süreli hareket alanı odağın {ar:كُلَّ, tr:kulla, gloss:her} sözüne temas edince karakter tipinin her taşıyıcısını sınırlı bir seyir içinde düşündürür (31:29). Böylece göksel akışın kapsayıcılığı “her”in kapsamını bütün insanlara yaymak yerine, bu sıfatları taşıyan herkesi zamanla çevrili bir hareket alanına yerleştirir. Göksel akış sürer ve belirlenmiş vadesine yönelir; üstünlük iddiası da bu karşılaştırmada zamanı aşan bir mevki değil, sınırları olan bir seyir olarak görünür.

Yeryüzünde ilerleyen gemi, yürümenin zemine bağımlılığını başka bir hareketle somutlaştırır. Deniz yolculuğu Allah’ın nimetiyle gerçekleşir (31:31); gölge gibi üzerlerine gelen dalgalar geçişin denetim dışına çıkışını, kurtarılıp karaya çıkarılmaları ise hareketin yeniden yeryüzüne bağlanışını gösterir (31:32). Gemi, dalga ve karaya dönüş yürüyüşe destek ve sınır içinde ilerleyen ayrı bir yolculuk örneği sunar (31:31, 31:32). Karaya çıkanlar arasında anılan {ar:مُّقْتَصِدٌ, tr:muqtaṣid, gloss:ölçülü davranan kişi}, aşırılıkla eksiklik arasındaki ölçüyü taşıyan kişiyi niteler. Bu bağlantı, yürüyüşü sözlük anlamı bakımından deniz yolculuğuyla bir tutmadan, onu desteği ve sınırı olan küçük bir yolculuk gibi görmeye imkân verir.

Benlik imgesi, geleceği güvenceye alan bir vekil gibi sunulamaz; bu karşılaştırma onun sınırını görünür kılar. Dünya hayatının aldatıcılığı ve yarının bilinmezliği içinde {ar:مُخْتَالٍ, tr:mukhtāl, gloss:kendini üstün gören} için açılan görünür benzerlik ve zihinde kurulan suret, kişinin yerine geçecek sağlam bir dayanak değil, sınanabilir bir tasarı olarak kalır (31:33, 31:34). Ebeveyn-çocuk ilişkisinde ebeveyn çocuğu adına karşılık veremez (31:33); bir kişinin yerine başkasının sonuç üstlenememesi, çekici ama oynak görünüşün kimlik yerine geçemeyeceği düşüncesini besler. Dünya hayatını adlandıran ifade yanağın adıyla ses düzeyinde uzak bir yankı kurabilir; bu bağlantı yanakla insanlara gösterilen sureti ses bakımından yakınlaştırır, iki sözü eşanlamlı kılmaz. Aynı ailenin kesin bilgi olmadan kurulan tasarım anlamı da yarın hakkında bir güvence sunmayan benlik anlatısını düşündürür (31:33, 31:34); ayetlerin hesap ve aldanışa ilişkin daha genel çerçevesi bu özel çağrışımla birlikte yerini korur.

Geçmiş başarı ve sahiplikleri kişisel liyakat hesabına çeviren {ar:فَخُورٍ, tr:fakhūr, gloss:övüngen}, alınmış nimet için övünmeme uyarısı ve yapılmamış işler için övgü bekleme sahnesiyle karşılaştırılır (57:23, 3:188). Yarın ne kazanılacağının ve nerede ölüneceğinin bilinmemesi bu hesabın geleceğe uzanmasını sınırlar (31:34). Ölüm yerine ilişkin uzak yol-yönü yankısı, {ar:تَمْشِ فِى ٱلْأَرْضِ, tr:tamshi fī al-arḍ, gloss:yeryüzünde yürüme} ile buluşunca sonu önceden bilinmeyen bir güzergâh imgesi verir. Aynı suret ailesinin sınırlı bir başka kullanımı kişi, dişi deve ya da toprağı iyi bir sonucun işareti sayabilir; benlik imgesiyle kurulan bu bağlantı olumlu işaretin yarın için güvence olamayacağını düşündürür. 31:33 ve 31:34’ün ahiret aldanışı ve hesap hakkındaki genel okuması da yerini korur; suret ile gelecek bağı, bu çerçeveye 31:18’deki böbürlenme açısından eklenen ihtiyatlı bir çağrışımdır.

</source_prose>
