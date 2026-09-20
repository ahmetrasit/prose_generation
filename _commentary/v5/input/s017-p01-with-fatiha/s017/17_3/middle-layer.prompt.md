# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:3**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.middle.claims.json`

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
- Refer to source paragraphs as `17:3 ¶N`.

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

`(17:3 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:3",
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
        "citation": "(17:3 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_3/17_3.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_3/17_3.middle.claims.json \
  --ayah-ref 17:3
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_3/17_3.prose.editorial.tr.md`

<source_prose>
## Soydan Tanıklığa

17:3'teki {ar:ذُرِّيَّةَ مَنْ حَمَلْنَا مَعَ نُوحٍ, tr:dhurriyyata man ḥamalnā maʿa Nūḥin, gloss:Nuh'la birlikte taşıdıklarımızın soyu} sözü, Nuh'la birlikte taşınanların soyuna seslenir. Ardından {ar:إِنَّهُ كَانَ عَبْدًا شَكُورًا, tr:innahu kāna ʿabdan shakūran, gloss:şüphesiz o çok şükreden bir kuldu} gelir; zamir en doğal biçimde Nuh'a döner. Böylece ayet, önce taşınmış bir topluluğun ortak geçmişini, sonra bu ilişki içinde adı anılan kişinin kulluk ve şükür niteliğini duyurur. Yakın ad ve ardından gelen insanî nitelemeler Nuh okumasını öne çıkarırken, zamirin başka bir göndergeye bağlanma olasılığı dilbilgisi bakımından tümüyle kapanmaz.

Açılıştaki {ar:ذُرِّيَّةَ, tr:dhurriyyata, gloss:soyundan gelenler} mansup biçimiyle önceki hitaba bağlı bir devam gibi durur; tek başına tamamlanmış yeni bir cümle açmaz. Nahiv açıklamaları bu bağı farklı biçimlerde çözdüğünden, açılışta bir eşik hissedilir ama tek bir çözümleme dayatılmaz. Hafs okuyuşu mansup ve şeddeli biçimi korur; bildirilen başka kıraatler öznelik ve tamlayanlık ilişkilerini, hareke, şedde ve hemze biçimlerini değiştirerek sözün sesini ve sentaksını farklı duyurur. Bunlar Hafs biçiminin yerine geçirilmez. Sözcüğün olağan anlamı soyundan gelenlerdir; türeyiş tartışması ise taşınmış topluluğun yanında saçılmış tohum ve yaratılmış devam yankılarını hafifçe duyurabilir, temel anlamı değiştirmez.

Bu soy adını izleyen {ar:مَنْ, tr:man, gloss:kimseler}, hem soy tamlamasına bağlanır hem {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} fiilinin nesnesi olur. Sayı ya da cinsiyet bildirmeyen bu ilgi biçimi, bütün topluluğu tek bir bağ içinde tutar; Arapçadaki biçim tek bir yolcuyu değil, bağlamın verdiği kişileri kapsar. İlgi bağı ancak taşıma eylemi, {ar:مَعَ, tr:maʿa, gloss:ile} refakat edatı ve {ar:نُوحٍ, tr:Nūḥin, gloss:Nuh} adıyla tamamlanır. {ar:مَنْ, tr:man, gloss:kimseler}, {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık}, {ar:مَعَ, tr:maʿa, gloss:ile} ve {ar:نُوحٍ, tr:Nūḥin, gloss:Nuh} boyunca işitilen nazal sesler de bu yerel akışı birbirine bağlar: ilgi ilişkisinden eyleme, oradan eşliğe ve ada geçilir.

{ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık}, birinci çoğul failin yaptığı tamamlanmış, etkin Form I taşıma eylemidir; {ar:مَنْ, tr:man, gloss:kimseler} taşınanları gösterir. Sözcüğün somut alanı bir şeyi kaldırıp taşıyıcının üzerinde tutarak başka yere götürmektir. Fiil doğrudan fiziksel taşımayı bildirir; ettirgen ya da dönüşlü bir kalıba geçmez, aracını ve koşullarını açık bırakır. {ar:مَعَ, tr:maʿa, gloss:ile} Nuh'la eşliği kuran bağımsız bir edattır; bu söz öbeği korunmuş topluluğu görünür kılar, belirli bir taşıt adlandırmadığından geniş kurtuluş anlatısının ayrıntılarını açık bırakır.

Kısa {ar:مَعَ, tr:maʿa, gloss:ile}, taşıma haberinin ardından {ar:نُوحٍ, tr:Nūḥin, gloss:Nuh ile} adını yeni bir cümle açmadan getirir. Ad, edatın yönettiği mecrur biçimiyle ilk söz öbeğini tamamlar; soy, taşıma ve eşlik kurulduktan sonra gelmesi okura önce kurtuluş ilişkisini duyurur. Nuh adı ardından tanıklığın odağına yeniden yaklaşır. Çevresindeki ağıt ve dinlenme yankıları sahneye keder ve ferahlık rengi katar; bu yankılar özel adın olağan karşılığını değiştirmeden kurtuluş ilişkisinin duyuluşunu renklendirir.

Bu gecikmiş addan sonra {ar:إِنَّهُ, tr:innahu, gloss:şüphesiz o} yeni ve vurgulu bir bildirim açar. Vurgu edatı ile üçüncü kişi zamiri tek sözcükte birleşir; zamir, Nuh'un adını izleyen tanıklığı başlatır. Önceki ilgi cümlesi burada sürmez: ardından gelen {ar:كَانَ, tr:kāna, gloss:idi}, {ar:عَبْدًا, tr:ʿabdan, gloss:kul} ve {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} sözleri yeni bildirimin içeriğidir. En doğal gönderge Nuh olsa da zamir başka bir göndergeye dönme olasılığı bütünüyle kapanmış değildir.

Buradaki {ar:كَانَ, tr:kāna, gloss:idi}, olma ve bulunma çerçevesini açan, ardından gelen yüklemlerle tamamlanan eksik fiildir. Tamamlanmış geçmiş çekimi Nuh'u gelişmekte olan bir eylemle değil, hatırlanan bir karakterle tanıtır; kendi başına bu niteliğin ne kadar sürdüğünü ölçmez. Kul oluşu ve şükür bu çerçevenin içeriğini ayrı ayrı verir. Fiilden sonra gelen {ar:عَبْدًا, tr:ʿabdan, gloss:kul} ile {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} sözcüklerinin uyumlu belirsiz mansup sonları da dengeli bir ikili ritim kurar, anlamlarını birbirine eşitlemeden.

Belirsiz mansup biçimdeki {ar:عَبْدًا, tr:ʿabdan, gloss:kul}, hem bir nitelik hem de kul olma ilişkisini bildirir; yüklem yerinde bulunduğu için unvan gibi duyulabilse de yalnızca sabit bir unvanla sınırlı değildir. Kul sözü bağımlı hizmeti, boyun eğişi ve Allah'a yönelen ibadeti birlikte taşır. Aynı biçimdeki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ona sıfat gibi sıkıca bağlanır; mansup ve belirsiz uyum bunu destekler. Sözdizimi hâl ya da ikinci yüklem çözümlemesine de açık kaldığından bu seçeneklerden biri kesinleştirilmez. Buradaki ad belirli bir ritüeli veya hukuki mülkiyet ilişkisini anlatmaz.

Uzun ünlülü faʿūl kalıbındaki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden}, arızi bir teşekkürü değil yoğun bir niteliği bildirir; belirli bir eylem sayısı ya da sıklık vermez. Şükür, iyiliği ve kaynağını tanımayı; bu kabulü içten kavrayışla, sözle veya iyiliğe uygun davranışla görünür kılmayı kapsar. Böylece {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} somut korunma zeminini, {ar:عَبْدًا, tr:ʿabdan, gloss:kul} bağımlı hizmet ilişkisini, {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ise bu ilişki içindeki karşılığı sağlar. Ayet şükrü korunmanın ardından duyulan karakter cevabı olarak verir; bu cümlede belirli bir övgü sözü, kurtuluşla nedensellik ilişkisi ya da maddi çoğalma belirtilmez. Sondaki yoğun niteleme kulağı şükürde bırakırken, onu kul oluşunun ve soy haberinin içinde duyurur.

## Sûrenin Yakın Akışı

İsrâ 17:1'de {ar:أَسْرَىٰ بِعَبْدِهِۦ لَيْلًا, tr:asrā bi-ʿabdihi laylan, gloss:geceleyin kulunu yola çıkardı} sözü bir hareketi, {ar:لِنُرِيَهُ مِنْ آيَاتِنَا, tr:linuriyahu min āyātinā, gloss:ona ayetlerimizden göstermek için} ifadesi de onun amacını bildirir (17:1). Aynı kul ailesindeki {ar:عَبْدًا, tr:ʿabdan, gloss:kul}, 17:3'te Nuh'un niteliğidir; 17:1'de ise işaretleri görecek alıcı gece yolculuğunun içindedir. Bu yakınlık, 17:3'te taşınmış soyun kurtuluş hatırasını Nuh'un kulluk ve şükrüyle birleştirirken 17:1'in ilahî hareketindeki alıcılığı kendi sahnesinde tutar. Yankı, aynı yolculuk değil; kul adının ilahî hareket içindeki alıcılık ile korunmaya verilen karşılığı yan yana getirmesidir.

Bir önceki ayette Musa'ya verilen kitabın İsrailoğulları için hidayet olduğu ve Allah'tan başka vekil edinilmemesi buyurulur (17:2). Hemen önce anılan topluluk, 17:3'teki {ar:ذُرِّيَّةَ, tr:dhurriyyata, gloss:soy} hitabına yerel bağlam sağlar; 17:2'de soy terimi doğrudan geçmediğinden bu yakınlık İsrailoğullarının tümünü Nuh'la taşınanların soyuyla özdeşleştirmez. Vekil yasağı, kurtarılmış ataların hatırasını devredilmiş güven karşısında düşünmeye ve Nuh'un {ar:عَبْدًا, tr:ʿabdan, gloss:kul} oluşundaki boyun eğiş ile ibadet yönünü duymaya açar. Sûrenin ilerleyen yasağı, Allah'ın yanında başka ilah edinmemeyi söyleyerek bu kulluk yönünü tek-yönlü ibadet olarak çerçeveler (17:22). Bu iki emirle soy hitabı arasındaki bağ yakın bağlamın sunduğu bir ihtimaldir; metin emirleri Nuh'un sözü ya da soy cümlesinin nedeni olarak vermez.

Kulluk sözcüğü yakındaki tarih anlatısında başka bir topluluğun görevlendirilmesine de katılır. İsrâ 17:4, İsrailoğullarının yeryüzünde iki kez bozgunculuk edeceğini ve kendilerini büyük ölçüde yükselteceklerini bildirir; ardından 17:5'te {ar:بَعَثْنَا عَلَيْكُمْ عِبَادًا لَنَا, tr:baʿathnā ʿalaykum ʿibādan lanā, gloss:üzerinize bize ait kullar gönderdik} denir. Bu gönderilmiş kişiler {ar:أُولِي بَأْسٍ شَدِيدٍ, tr:ulī baʾsin shadīdin, gloss:çetin bir güce sahip} diye nitelenir ve evlerin arasına dalarlar (17:4, 17:5). Odaktaki tekil {ar:عَبْدًا, tr:ʿabdan, gloss:kul} ile buradaki çoğul kullar aynı hizmet ve kulluk ailesindedir; “bize ait” sözü görevlilerin aidiyetini, gönderilmeleri üstlendikleri işi belirtir. Nuh ise {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} niteliğiyle şahsen anılır. Ortak kul adı burada farklı rolleri bağlar: Nuh şükreden birey, 17:5'teki kullar gönderilmiş görevlilerdir. Bu bağlantı hizmet ve aidiyet alanını açar; ahlaki denkliği ya da metnin kurmadığı kesin bir karşıtlığı gerektirmez.

Bu bozulma ve gönderilme anlatısının ardından 17:6'da üstünlüğün geri verilmesi, mal ve oğullarla desteklenme gelir; 17:8'de “yeniden dönerseniz biz de döneriz” sözü dönüşün ardından karşılığı ekler (17:4, 17:5, 17:6, 17:7, 17:8). Bu tarihsel çevrede alınan nimetin ve ona verilen davranışsal cevabın yinelenmesi, Nuh'un {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} oluşunu iyiliği tanıyıp karşılayan bir pratik olarak duyurur. Buradaki bağ, İsrailoğullarının Nuh'u unuttuğuna ya da şükrün sonraki davranışları durdurduğuna ilişkin bir neden-sonuç iddiası değil, ayrı özneler arasındaki yerel bir karşılaştırmadır.

Yakın bağlam bu kez toplumsal tarihten insanın zamana verdiği cevaba döner. 17:11'de {ar:كَانَ, tr:kāna, gloss:idi} insanın durumunu kurar: kişi {ar:يَدْعُ الْإِنسَانُ بِالشَّرِّ دُعَاءَهُ بِالْخَيْرِ, tr:yadʿu al-insānu bi-sh-sharri duʿāʾahu bi-l-khayr, gloss:hayrı ister gibi kötülüğü çağırır}, sonra {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} diye nitelenir (17:11). Aynı olma çerçevesinde Nuh'un {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} niteliği, anlık sonucu hayır sanan acelecilik karşısında iyiliği zaman içinde tanıyan bir yöneliş açar. Bu yan yana geliş zaman yönünü karşılaştırır; iki sıfatı sözlükte karşıtlaştırmaz ve 17:11 Nuh'u ayrıca “acele karşıtı” diye nitelemez.

Topluca taşınmış ataların geçmişinden tek tek insanların hesabına geçişi, İsrâ 17:12'de her şeyin ayrıntısıyla açıklanması ve 17:13'te her kişinin kendi kaydının kendisine bağlanıp kitabının önüne çıkarılmasıyla belirginleşir (17:12, 17:13). Odaktaki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} fiziksel olarak taşınmış topluluğu anlatmayı sürdürürken, bu kayıt herkesin kendi eylemleriyle karşılaşacağı başka bir ölçek açar. Ayrıntılı açıklama 17:12'de, kişisel hesabı açan adım 17:13'te belirir.

Bu kişisel sınır, 17:15'te ahlaki yükün devredilmediği açık ilkeyle belirginleşir: {ar:وَلَا تَزِرُ وَازِرَةٌ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü yüklenmez} (17:15). Buradaki {ar:وِزْرَ أُخْرَىٰ, tr:wizra ukhrā, gloss:başkasının günah yükü} başka bir sözcük ailesindendir; 17:3'teki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} ile kök ortaklığı değil, yük imgesi paylaşılır. Taşıma ailesinin güvenilmiş sorumluluğu ya da mesajı üstlenme gibi ayrı kullanımları da bu bağlamda duyulabilir: aynı ayette ceza için {ar:حَتَّىٰ نَبْعَثَ رَسُولًا, tr:ḥattā nabʿatha rasūlan, gloss:bir elçi gönderinceye kadar} denir. Elçinin görevi ayrı bir gönderilme ve mesaj ilişkisini açar; odaktaki fiil insanları fiziksel olarak taşıma anlamını korur. Bu karşılaşma ortak kurtuluş geçmişini kişisel sorumluluğun yanında düşündürür; bağlantı yük imgesine dayanır, 17:3'e günah taşıma ya da yargı kuralı anlamı, iki ayete de zorunlu bir karşıtlık yüklemez.

Nuh'tan sonraki soyun tarihi, taşınmış olmanın kalıcı korunma güvencesi olmadığını gösterir. İsrâ 17:17, Nuh'tan sonra nice kuşağın helak edildiğini ve Rabbin kullarının günahlarını bildiğini söyler; oradaki {ar:عِبَادِهِ, tr:ʿibādihi, gloss:O'nun kulları} adı Nuh'a verilen kul adlandırmasını başka insanlara taşır (17:17). Soy geçmişi korunmuş bir başlangıç sağlar, fakat Nuh'un {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} oluşu gibi iyiliği tanıyıp karşılık verme niteliği kişisel kalır. 17:17'nin genel tarih uyarısı oluşu bu soy yankısını olası bir bağ olarak tutar; ayetin soy hitabını doğrudan yeniden tanımladığı sonucunu vermez.

## Korunmadan Süren Hayat

Bu sonraki kuşakların kırılgan tarihi, taşıma imgesine bedenden bakmak için yeni bir açı açar. Lokman 31:14'te {ar:حَمَلَتْهُ أُمُّهُ وَهْنًا عَلَىٰ وَهْنٍ وَفِصَالُهُ فِي عَامَيْنِ, tr:ḥamalat-hu ummuhu wahnan ʿalā wahnin wa-fiṣāluhu fī ʿāmayn, gloss:annesi onu güçlük üstüne güçlük içinde taşıdı; sütten ayrılması iki yıl sürdü} denir. 17:3'teki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} ile aynı fiil ailesindeki bu taşımanın faili burada annedir; güçlük üstüne güçlükle sürdüğü ve çocuğun iki yılda sütten ayrılmasına uzandığı açıkça anlatılır (31:14). Bu temas fiziksel kurtuluş okumasını genişletir: soy çizgisi, güçlük içinde bedenle taşınan ve sütten ayrılmaya uzanan bir hayat gibi duyulur. Bu bağlantıda gebelik imgesi anne bedenine aittir; 17:3'te taşınanlar Nuh'la birlikte kurtarılan insanlardır.

İbrahim'in 14:37'deki duasında soy {ar:بِوَادٍ غَيْرِ ذِى زَرْعٍ, tr:bi-wādin ghayri dhī zarʿ, gloss:ekinsiz bir vadide} yerleştirilir; ona meyvelerden rızık dilenir ve {ar:لَعَلَّهُمْ يَشْكُرُونَ, tr:laʿallahum yashkurūn, gloss:umulur ki şükretsinler} diye umut edilir (14:37). Buradaki {ar:يَشْكُرُونَ, tr:yashkurūn, gloss:şükretsinler}, odaktaki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ile aynı aileden ama farklı biçim ve işlevdedir: biri dua içindeki çoğul eylem, öteki Nuh'u niteleyen yoğun sıfattır. Ailenin ayrı bir sözlük dalı az girdiyi yeterli bulma veya sınırlı girdiden belirgin gelişme nüansı da taşır; bu doğrudan odak sıfatının anlamı değildir. Ekinsiz vadi, istenen meyve ve şükür umudu kıtlık, umulan rızık ve minnet cevabını bir araya getirir. Meyve burada gerçekleşmiş hasat değil, duada istenen nimettir; bu bağlantının katkısı, soyun ihtiyaç içindeki devamını şükür umuduyla birlikte düşündürmesidir.

Bu manzaradaki meyve isteği, taşıma ailesinin iki somut dalını hatırlatır: rahimde yavru taşıyan beden hayatı içeriden sürdürür; kendi meyvesini taşıyan ağaç ise aynı taşıma alanını üretken bir devamla buluşturur. Bu çağrışımlar, 17:3'teki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} ile {ar:ذُرِّيَّةَ, tr:dhurriyyata, gloss:soy} arasındaki fiziksel taşıma ve nesiller bağına organik bir devam imgesi ekler. Şükür ailesindeki ayrı bir sözlük yankısı gövde ya da dipten çıkan körpe sürgünü ve ince dalı çağrıştırır; taze saç, yavru kuşun ince tüyü ve küçük çocuk da bu genç oluşumlara benzetilir. Böylece gebelik ve meyve taşıma hayatın nasıl sürdüğünü, sürgün ile genç beden örnekleri ise yeni büyümenin nasıl görünür olduğunu katkılandırır; 14:37'deki istenen meyve de bu ilişkiyi ihtiyaç ve umut sahnesinde tutar.

Tohum yatağı imgesi bu katkıları bir araya getirir: bedensel taşıma hayatı kopuş içinden sürdürür, ekinsiz vadide dilenen meyve nimetin umudunu, sürgün ve yavru imgeleri yeni büyümeyi görünür kılar. Bu organik sahne 17:3'ün literal olayı değil, bu bağlantıların kurduğu yorumlayıcı benzetmedir; odaktaki sözler Nuh'la taşınan insanları ve onların soyunu anlatır. Doğuş ya da ışıkla ilgili bağımsız bir işaret bu imgeyi başlatmaz. Sûrenin girişindeki rahmet vurgusu (S:0) bu çizgiye rahmet tonu, yıkım sonrası dönüş ve toparlanma ise kopuştan sonra yeniden kurulan hayat boyutunu katar (17:4, 17:5, 17:6, 17:7, 17:8); bu ayetler benzetmeye yorumlayıcı destek verir. Birlikte, taşıma, meyve umudu ve körpe büyüme kurtarılmış topluluktan sonra da yaşamı sürdüren, nimete şükürle cevap veren bir soy çizgisini duyurur.

## Taşımanın Başka Ölçekleri

Bu soy çizgisinin daha geniş insanlık içindeki yeri, İsrâ 17:70'te aynı fiziksel taşıma ailesiyle açılır: {ar:وَحَمَلْنَٰهُمْ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:wa-ḥamalnāhum fī al-barri wa-al-baḥr, gloss:onları karada ve denizde taşıdık} denerek Âdem oğullarının karada ve denizde taşınması, ardından {ar:وَرَزَقْنَٰهُم مِّنَ ٱلطَّيِّبَٰتِ, tr:wa-razaqnāhum mina al-ṭayyibāt, gloss:onlara güzel nimetlerden rızık verdik} denerek iyi nimetlerle rızıklanması anlatılır (17:70). Odaktaki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} gibi buradaki eylem de insanları taşır; ölçek Nuh'la kurtarılan belirli topluluktan bütün insanlığa genişler ve taşıma ile rızıklandırmayı yan yana getirir. Bu yankı ortak ilahî desteği açar; 17:3'teki özel kurtuluşu herkesin ortak geçmişi saymaz.

İnsanlık ölçeğindeki bu genişlik, soyun geleceğini de açık uçlu bırakır. Şeytan, soy üzerinde ileride kurmayı tasarladığı tasallutu azı dışında herkesi kapsayacak bir niyetle dile getirir (17:62). Oradaki {ar:لَأَحْتَنِكَنَّ ذُرِّيَّتَهُ إِلَّا قَلِيلًا, tr:la-aḥtanikanna dhurriyyatahu illā qalīlan, gloss:azı dışında soyunu mutlaka ele geçireceğim} tehdidi, Nuh'la taşınmış soyun devam eden fakat tehlikeye açık bir çizgi olduğunu düşündürür. Ayetin sunduğu kapsam bir gelecek niyetidir; gerçekleşmiş sonucu veya her torun için aynı kaderi belirlemez. Böylece 17:70'in insanlığa açtığı genel destekle 17:62'nin soy üzerindeki tehdidi farklı ufuklarda kalır; Nuh'un soyu tek ayrıcalıklı hat olmaz.

Taşıma ailesi fiziksel insan taşımaktan emanet edilmiş sorumluluğa da uzanır. Ahzâb 33:72'de {ar:الْأَمَانَةَ, tr:al-amānah, gloss:emanet} göklere, yere ve dağlara sunulur; onlar yüklenmekten kaçınırken {ar:وَحَمَلَهَا الْإِنْسَانُ, tr:wa-ḥamalahā al-insān, gloss:insan onu yüklendi} denir (33:72). Bu, odaktaki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} ile aynı Form I ailesinin başka bir anlamıdır: burada taşınan insan topluluğu değil emanet ve sorumluluktur. Bu bağlantı fiziksel kurtuluşun yanına üstlenilmiş görev yankısını ekler; emanetin sorumluluğu Nuh'un soyuna aktarılmaz.

Soy bağı ile kişisel sorumluluk yan yana durur. Tûr 52:21'de imanla izleyen soyların ailelerine katılmasından söz edilir; hemen ardından {ar:كُلُّ ٱمْرِئٍ بِمَا كَسَبَ رَهِينٌۭ, tr:kullu imriʾin bimā kasaba rahīn, gloss:her kişi kendi kazandığına bağlıdır} denir (52:21). Bu birliktelik aileye katılma ile bireysel kazanç sorumluluğunu birlikte tutar: Nuh'un torunları onun örneğine kendi cevaplarını verebilir, fakat onun suçunu ya da faziletini devralmaz; ayet torunları yargılamaz. Meryem 19:58'de {ar:وَمِمَّنْ حَمَلْنَا مَعَ نُوحٍۢ, tr:wa-mimman ḥamalnā maʿa Nūḥin, gloss:Nuh'la birlikte taşıdıklarımızdan} ifadesi Âdem, İbrahim ve İsrail soylarının, peygamberlerin ve hidayete erdirilmiş seçkinlerin anıldığı diziye katılır (19:58). Böylece taşınanlardan bir hat peygamberlik tarihine yerleşir; bu dizi her yolcuyu veya her torunu peygamber olarak tanımlamaz.

## Şükrün Eylemi ve Karşılığı

Kişisel cevabın nasıl görüldüğü, İsrâ 17:19'da çabanın takdir edilmesiyle başka bir biçim alır. Ahireti dileyip ona yaraşır çaba gösterenler {ar:سَعَىٰ لَهَا سَعْيَهَا, tr:saʿā lahā saʿyahā, gloss:ona yaraşır çabayla çalışmak} diye anlatılır; ardından {ar:كَانَ سَعْيُهُم مَّشْكُورًا, tr:kāna saʿyuhum mashkūran, gloss:çabaları takdir edilmişti} denir (17:19). Odaktaki etkin ve yoğun {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ile burada çabayı niteleyen edilgen {ar:مَّشْكُورًا, tr:mashkūran, gloss:takdir edilmiş} aynı kelime ailesindendir ama dilbilgisel olarak aynı biçim değildir. Her iki yerdeki {ar:كَانَ, tr:kāna, gloss:idi} ayrı kişilerin yerleşik durumlarını yan yana getirir; böylece nimeti tanıyan cevap, gösterilen çaba ve bu çabanın görülmesi karşılıklılık kazanır. Bu yan yanalık ayrı kişilerin paylaştığı bir soy bağı kurmaz; edilgen takdirin kabul veya ödül anlamı da açık kaldığından temas olası bir yankı olarak kalır.

Bu karşılıklılık, şükredenin ödüllendirilmesiyle ve emeğin görülmesiyle başka iki ayette belirginleşir. Kamer 54:35'te {ar:نِّعْمَةًۭ مِّنْ عِندِنَا ۚ كَذَٰلِكَ نَجْزِى مَن شَكَرَ, tr:niʿmatan min ʿindinā kadhālika najzī man shakara, gloss:bizden bir nimet; şükredeni böyle ödüllendiririz} denir; buradaki {ar:شَكَرَ, tr:shakara, gloss:şükretti} bir eylemi anlatır, odaktaki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ise kişiyi niteleyen yoğun sıfattır (54:35). İnsân 76:22'de {ar:سَعْيُكُم مَّشْكُورًا, tr:saʿyukum mashkūran, gloss:çabanız takdir edilmiştir} sözü {ar:جَزَآءًۭ, tr:jazāʾan, gloss:karşılık} ile yan yana gelir (76:22). Bu ayetler nimete cevap, emeğin görülmesi ve karşılık düşüncesini genişletir; eylem, yoğun sıfat ve edilgen takdir biçimlerini ayrı tutarken kendi bağlamlarını korur, Nuh'un hayatına yeni olaylar eklemez.

Karşılık ilişkisinde verenin teşekkür beklemesi gerekmez. İnsân 76:9'da Allah rızası için insanları doyuranlar {ar:لَا نُرِيدُ مِنكُمْ جَزَاءً وَلَا شُكُورًا, tr:lā nurīdu minkum jazāʾan wa-lā shukūran, gloss:sizden ne karşılık ne de teşekkür istiyoruz} der (76:9). Buradaki {ar:شُكُورًا, tr:shukūran, gloss:teşekkür}, odaktaki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ile aynı ailedendir ama bu bağış sahnesinde istenmeyen bir karşılık adıdır. Bu ayrı örnek, Nuh'un niteliğindeki şükrü bir ücret olmaktan çıkarıp serbestçe verilen cevaba yerleştirir; iyilik, teşekkür talebine bağlı olmadan sunulur.

İsrâ 17:20'de bağış iki gruba da ulaşır: {ar:كُلًّا نُّمِدُّ هَٰؤُلَاءِ وَهَٰؤُلَاءِ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:bu iki kesimin ikisine de veririz} denir ve {ar:وَمَا كَانَ عَطَاءُ رَبِّكَ مَحْظُورًا, tr:wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışı esirgenmiş değildir} sözü bağışın esirgenmediğini ekler; 17:21 ise {ar:فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:faḍḍalnā baʿḍahum ʿalā baʿḍ, gloss:onları birbirlerine göre üstün kıldık} diyerek dereceleri ayırır (17:20, 17:21). Bu geniş destek içinde Nuh'la taşınan belirli topluluğun kurtuluşu özel bir olay olarak yer alır; taşıma herkese ortak bir olay olmaz. {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} nimet karşısındaki kişisel cevaptır; bağışa erişme koşulu veya Nuh soyuna ayrılmış ayrıcalık değildir. 17:20 gündelik dünya rızkını da anlatabilir; bu olasılık 17:21'deki derece farklarını yerinde bırakır.

Şükür, yalnızca niteliği bildiren bir söz değil, ibadet ve iş olarak da görünür. Sebe 34:13'te Dâvûd ailesine {ar:ٱعْمَلُوا۟ ءَالَ دَاوُۥدَ شُكْرًا, tr:iʿmalū āla dāwūda shukran, gloss:Ey Dâvûd ailesi, şükürle çalışın} buyurulur; buradaki {ar:شُكْرًا, tr:shukran, gloss:şükürle} isim biçimi, şükürle yapılacak işi bildirir. Ardından {ar:وَقَلِيلٌۭ مِّنْ عِبَادِيَ ٱلشَّكُورُ, tr:wa-qalīlun min ʿibādī al-shakūr, gloss:şükreden kullarım azdır} denir (34:13). Odaktaki {ar:عَبْدًا, tr:ʿabdan, gloss:kul} ile duyulan kulluğun Allah'a yönelen ibadet tarafı burada eyleme, şükürle çalışmaya döner.

Eyleme açık bu şükür, zaman içinde yinelenen bir imkânla da buluşur. Furkân 25:62'de geceyle gündüzün birbirini izlemesi, hatırlamak ya da şükretmek isteyenlere yenilenen bir fırsat verir: {ar:جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ لِّمَنْ أَرَادَ أَن يَذَّكَّرَ أَوْ أَرَادَ شُكُورًا, tr:jaʿala al-layla wa-al-nahāra khilfatan li-man arāda an yadhakkara aw arāda shukūran, gloss:geceyle gündüzü hatırlamak veya şükretmek isteyenler için birbirinin ardı sıra kıldı} (25:62). Buradaki {ar:شُكُورًا, tr:shukūran, gloss:şükretme}, odaktaki {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} sıfatından farklı biçim ve işlevde, şükretme isteğini anlatır. 34:13'ün iş buyruğu şükrü eylemde, 25:62'nin gece-gündüz dönüşü ise bu cevaba yeniden açılan fırsatta gösterir; bu fırsat Nuh'un her gün yaptığına dair biyografik bir kayıt değil, şükür imkânının sürekliliğidir.

Bu yenilenen yöneliş, Fâtiha'da bugünkü ortak dua biçimini alır. Fâtiha'nın 1:5'teki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīnu, gloss:Yalnız Sana kulluk eder ve yalnız Senden yardım dileriz} sözü, geçmişte alınmış desteğin yanına ortak kulluk ve yardım isteğini koyar (1:5). 17:3'teki {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} fiziksel taşıma, {ar:عَبْدًا, tr:ʿabdan, gloss:kul} kulluk ilişkisi, Fâtiha'daki {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} ise etkin tapınma fiilidir. Bu karşılaştırma 1:5'in dua hareketiyle sınırlıdır: Fâtiha Nuh'u veya taşınmış topluluğu adlandırmaz; {ar:حَمَلْنَا, tr:ḥamalnā, gloss:biz taşıdık} fiziksel taşımadır, yardım dileği değildir. Bu fark, geçmiş nimeti tanımayı bugünkü ortak kulluk ve Allah'tan yardım dilemenin yanına koyar; şükür ortak duada Allah'a yönelen ses olarak sürer.

</source_prose>
