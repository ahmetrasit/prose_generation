# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:36**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.middle.claims.json`

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
- Refer to source paragraphs as `17:36 ¶N`.

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

`(17:36 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:36",
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
        "citation": "(17:36 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_36/17_36.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_36/17_36.middle.claims.json \
  --ayah-ref 17:36
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_36/17_36.prose.editorial.tr.md`

<source_prose>
## İz Sürmenin Bilgi Eşiği

17:36, önceki buyruk dizisinin ardından {ar:وَلَا, tr:wa-lā, gloss:ve yapma} ile bir sınır daha ekler (17:35). Yasaklayıcı {ar:لَا, tr:lā, gloss:yapma}, ikinci tekil muhataba yönelen {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek} fiilini yönetir. Cezmde fiilin sonundaki illet harfi düşerek biçimi kısalır; verilen okuyuş farklılıkları bu kısalmayı duyurur, yasağın yönünü değiştirmez. Fiilin olağan anlamı birinin ya da bir izin ardından gitmektir. Ayak izini takip etme imgesi burada, bilgisi olmayan bir iddia veya meseleye yönelmeye taşınır. Bu kullanım araştırmaya bir bilgi koşulu getirir: yasak, hakkında bilgi bulunmayan şeyi izlemeyi kapsar.

Takip edilen şey, artikelsiz ve iyelik almamış {ar:مَا, tr:mā, gloss:şey} ile açık bırakılır; onu izleyen ilgi cümlesi kapsamı “bilgin olmayan şey” diye belirler ve mā fiilin doğrudan nesnesi olur. {ar:لَيْسَ لَكَ بِهِۦ عِلْمٌ, tr:laysa laka bihi ʿilmun, gloss:ona dair bilgin yok} içindeki {ar:لَيْسَ, tr:laysa, gloss:bulunmamak}, konuya ilişkin bilgi bağının yokluğunu bildirir: ölçü kanaatin gücü veya uzmanlık derecesi değil, o konuda bilgi bulunup bulunmamasıdır. {ar:لَكَ, tr:laka, gloss:senin için} ölçüyü doğrudan muhataba bağlar: bilginin başka birinde bulunması, senin o konudaki bilgi eşiğini karşılamaz; uzaktan duymak tek başına bu eşiği geçirmez. {ar:بِهِۦ, tr:bihi, gloss:ona dair} bilginin konusunu gösterir ve zamiri māya döner. Bāʾ harfinin olumsuzluğu pekiştirdiği yönündeki dilbilgisel açıklama da bu konu ile bilgi arasındaki ilişkiyi korur. Olumsuzluk altındaki belirsiz {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi}, eşiği uzmanlıkla daraltmaz; herhangi bir bilgi bağının bulunup bulunmadığını sorar.

Bu konu ilk cümlede {ar:بِهِۦ, tr:bihi, gloss:ona dair} ile izlenen şey olarak belirir, son cümledeki {ar:عَنْهُ, tr:ʿanhu, gloss:onun hakkında} ile hesap sorulacak meseleye taşınır. {ar:لَيْسَ, tr:laysa, gloss:bulunmamak} ile ʿilm arasındaki ses akışı daralıp yokluğu belirginleştirirken, ayetin sonundaki {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır} sözü bu bilgi konusunu cevap verebilirliğe bağlar. Araya giren {ar:إِنَّ, tr:inna, gloss:şüphesiz} ikinci cümleyi vurgulu bir gerekçe olarak açar: sınırın gerekçesi işitme, görme ve gönlün de hesap konusu olmasıdır. {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme}, {ar:ٱلْبَصَرَ, tr:al-baṣara, gloss:görme} ve {ar:ٱلْفُؤَادَ, tr:al-fuʾāda, gloss:gönül}, inna'nın yönettiği cümlede {ar:وَ, tr:wa, gloss:ve} ile eşdeğer yetiler olarak sıralanır; muhataba yöneltilen takip yasağı böylece duyumdan iç değerlendirmeye uzanan bir hesapla gerekçelenir.

İlk sıradaki {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme}, kulağın organından çok işitme yetisini ve ses alma sürecini adlandıran belirli bir mastardır. Ses dokusu duyulanın içe ilerleyip hesaba ulaşmasını hafifçe sezdirir; olağan işitme anlamı ise anlatının dayanağı olarak kalır. İşitme bir sesi alabilir, bir haberin taşındığı kanal olabilir; sesin alınmış olması haberi kendiliğinden doğru kılmaz.

İşitmenin edilgin ses alımından dikkatle dinlemeye geçişi ayrı bir bağlamda görünür: sığınan kişiye, Allah'ın sözünü işitinceye kadar korunma verilir; dinlemesinin ardından güvenli yerine ulaştırılır (9:6). Buradaki sıra, kulağa ses gelmesinden sese yönelmiş dikkate geçişi belirginleştirir. İşitmenin başka bir kullanımı, duyulan sözün anlamını kavramaktır; 17:36'daki iz sürme ve bilgi eşiği, algılananın anlaşılmasını da hesaba katar. Bu anlamayı sözün kabul edilip ona göre davranmasına dek genişletmek mümkündür: takip, benimsenen içeriğe uzanabilir. Odak ayet ise belirli bir talimatı ya da gerçekleşmiş itaati adlandırmaz; burada açılan, alımdan anlamaya ve olası karşılığa uzanan dinleme çizgisidir.

Listenin ortasındaki {ar:ٱلْبَصَرَ, tr:al-baṣara, gloss:görme}, işitmeye tabi olmayan ikinci bir yetidir; inna tarafından aynı düzeyde yönetilir. Sıralamada ses alan işitme ile iç işlemi adlandıran fuʾād arasında durması, geleni sınayan ara duyuyu görünür kılar. Sözcük tek tek göz ya da bakış yerine görme yetisinin bütününü adlandırır. Olağan anlamı fiziksel görme ve gözlemdir: görülen işaret, kesin hükme dönüşmeden önce izleme ve bilgi ölçüsünde sınanır.

Basar için ayrıca iç kavrayış, bir şeyi bilme, doğrulanmış idrak, delil ve kanıt, ibret, açıklayıcı bildirim ve kişinin kendini tanıması anlamları kullanılır. Odaktaki {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} ve {ar:ٱلْفُؤَادَ, tr:al-fuʾāda, gloss:gönül} bu içe dönük kullanımı çağırırken, kuruntuyu hakikatin karşısına koyan ifade bu ayrımı keskinleştirir (53:28). Orada {ar:يَتَّبِعُونَ إِلَّا ٱلظَّنَّ, tr:yattabiʿūna illā aẓ-ẓanna, gloss:ancak kuruntunun peşinden giderler} denir; 17:36 ise zannı adlandırmaz. İki pasajın teması, duyusal belirtinin henüz bilgi olmadığını gösterir: belirsiz kalan yeri tahmin doldurduğunda, tahmin gerçeğe uygun idrak yerine geçmez. Bu içgörü kullanımı fiziksel görmeyi silmez ve görülen her şeyi kanıt saymaz; görülenin iddia için nasıl sınandığını açığa çıkarır.

İşitme adının dişil birleşik sözlük kullanımlarından biri, bilgi edinmek için dinleyip bakan, belirli bir nesneye ya da kesin delile ulaşamayınca tahminde bulunan kadını anlatır. Odak ayetteki {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme} ise işitme yetisinin adıdır; bu birleşik örnekle kurulan temas biçim özdeşliğine değil, taqfu ile iz sürmenin, basar ile görmenin ve ʿilm eşiğinin yan yana gelişine dayanır. Bu ilişki, hangi haber veya iddianın söz konusu olduğunu belirlemeden, algının kesin kanıt bulunmadığında varsayıma kayabileceği eşiği duyurur.

Ayrı sözlük dalındaki kan parçası veya leke, yara ya da darbe izi görünür izin maddi yüzeyini verir. Fiziksel görme, {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek}in iz sürmesi ve sondaki {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır} bir araya geldiğinde, görünür izin takip edilip hesabının sorulduğu keşifsel imge belirir. Bu bağlantı odak ayette fiziksel bir olay anlatmaz; görünür iz ile iz sürme ve cevap verebilirlik arasındaki ilişkiyi somutlaştırır.

Üçüncü sıradaki {ar:ٱلْفُؤَادَ, tr:al-fuʾāda, gloss:gönül}, dış duyulardan içe doğru ilerleyen listeyi tamamlar. Sözcüğün olağan çekirdeği göğüsteki yürektir; sıralamada ise duyumların iç işlem ve yargı yerinde buluşmasını adlandırır. İşitme ve görmeden gelenler hükme ve inanca bu iç uçta taşınabilir; bu, fizyoloji veya psikoloji kuramı değil, yetilerin işleyişini anlatan bir sıra imgesidir. Hemzeli biçimin üçüncü sıradaki gelişi listeye belirgin bir ses kapanışı verir; verilen okuyuş farklılıklarında hemzenin hafifletilmesi gönderimi korurken duyulan vurgu noktasını değiştirir.

Fuʾādın sözlük çevresindeki için için ısınan iç çekirdek imgesi, gönül yetisine duygusal bir doku ekler. Bu imge yoksulluk korkusunun iç hükme baskısını düşündürür: çocukları öldürme saiki olarak anılan korku 17:31'de, öldürmede haklı nedeni ve maktulün velisine tanınan yetki ise 17:33'te yer alır; aynı bağlamdaki aşırılığı önleme buyruğu yetkinin sınırını çizer. Korku iç hükmü etkileyen bir saik olsa da bilgi ölçüsünün yerini tutmaz; velisine tanınan yetki de bu iki ayetteki öldürme durumlarında aşırılığı sınırlar.

Bu üç yeti gerçek bir armağandır; armağan oluşları doğru bilginin, şükrün veya uygun karşılığın kendiliğinden oluşmasını garanti etmez. İnsanların hiçbir şey bilmezken işitme, görme ve gönülle donatılıp şükre yöneltilmesi başlangıçtan bilgiye doğru bir imkânı gösterir (16:78); az şükürden söz edilmesi karşılığın ayrı bir yöneliş olduğunu hatırlatır (67:23). Ayetleri yalanlayan belirli topluluğa verilen işitme, gözlem ve yürek de fayda sağlamamıştır (46:26). 16:78'deki bilgisizlik otomatik bilgi değil, bilgiye doğru hareketin başlangıç koşuludur. Bu örnekler kendi topluluk ve durumlarında kalır; yanılgının kasıtlılığını ya da yetilerin her kullanımdaki başarısını genellemek yerine armağan ile karşılığın ayrımını gösterir.

## Her Yetinin Cevabı

Üç yeti {ar:كُلُّ, tr:kullu, gloss:her biri} ile kurulan tamlamada hem tek tek hem birlikte kapsanır; biçimce tekil olan tümelleyici hükmü listedeki her birine dağıtır. {ar:أُو۟لَٰٓئِكَ, tr:ulāʾika, gloss:işte bunlar} önceki listeye yeniden işaret eder. Akıllı varlıklar için kullanılan çoğul gösterim yetileri dilbilgisel düzeyde cevap verebilir muhataplar gibi kişileştirir; böylece her biri hesapta ayrı ayrı görünür, gerçek insan failler olarak sunulmaz. Tekil {ar:كَانَ, tr:kāna, gloss:idi}, kullu ile uyum sağlar ve özneyi {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır} yüklemine bağlar. Kāna'nın tamamlanmış görünüşü yalnızca ileride yaşanacak tek bir olayı değil, kurulmuş ve geçerli bir hesap durumunu da anlatabilir.

İlk cümledeki {ar:بِهِۦ, tr:bihi, gloss:ona dair}, {ar:مَا, tr:mā, gloss:şey} ile açılan konuyu bilginin nesnesi yapar; ikinci cümledeki {ar:عَنْهُ, tr:ʿanhu, gloss:onun hakkında} aynı konuyu hesap sorusuna taşır. Anhu'nun tekil zamiri meseleye dönebilir, her bir yetiye dağıtılabilir veya bir kişiyi gösterebilir; dilbilgisi tek bir gönderimi zorunlu kılmaz. Yine de zamir, {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır}ın ilişki tümleci olarak cevap beklenecek konuyu cümlede tutar.

Masʾūlan edilgen ortaçtır: işitme, görme ve gönül sorunun yöneltildiği ve hesabın sorulduğu taraftır. Belirsiz biçim cevap verebilirliği belirli bir soruşturma sahnesine kapatmaz; kullu'nun dağıtımı bu yükümlülüğü listedeki her yetiye uygular. Hemzenin ses akışında yarattığı küçük eşik cümleyi cevap verebilirlik durumuna bağlayarak kapatır; yasakla açılan takip yeni bir olayla değil, yerleşik bir hesap ilişkisiyle sonlanır.

Masʾūlanın etkin kullanım alanı soru sormayı, bilgi edinmeyi veya bir şeyi istemeyi de kapsar. Odaktaki edilgenlik yetileri hesap soran değil, hesap verilen taraf yapar; etkin kullanımın yankısı ise dikkati yalnızca izlenen iddiaya değil, bilgiye hangi yoldan varıldığına da çevirir. Aynı kökün başka bir kullanımı, bağlı ya da kapalı bir yerden bir şeyi nazikçe ve fark ettirmeden çekip çıkarmayı anlatır. Taqfu ile üç yetinin yan yana gelişi bu ayrı imgeye temas edince, her yetiden örtülü izin fark ettirmeden çıkarılıp seçilen izlekle birleştirildiği bir inceleme belirir; bu imge gizli malzemenin görünürleşmesine katkı verirken odaktaki masʾūlan edilgen hesap anlamını taşır.

Birbirine bağlı dizi anlamı, adımların nasıl bağlandığını öne çıkarır: {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek} ile başlayan takip {ar:كُلُّ, tr:kullu, gloss:her biri} ile her yetiye dağılır, {ar:أُو۟لَٰٓئِكَ, tr:ulāʾika, gloss:işte bunlar} ile listeye yeniden bağlanır ve {ar:عَنْهُ, tr:ʿanhu, gloss:onun hakkında} ile ortak bir hesap konusuna yönelir. Çekip çıkarma imgesi örtülü malzemeyi görünür kılar; dizi anlamı ise takibi, her yetiyi ve ortak hesap konusunu birbirine tutturur. Böylece iki ayrı sözlük katkısı takipten cevaba uzanan hattın hem içeriğini hem bağlantılarını aydınlatır.

Bu hatta önce {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek} bir izin peşinde ilerler; {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme} duyulanı, {ar:ٱلْبَصَرَ, tr:al-baṣara, gloss:görme} görüleni alır. {ar:ٱلْفُؤَادَ, tr:al-fuʾāda, gloss:gönül} bu izlenimleri içte işlerken {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} benimsenen iddianın bilgi eşiğini korur; {ar:كُلُّ, tr:kullu, gloss:her biri} ile {ar:أُو۟لَٰٓئِكَ, tr:ulāʾika, gloss:işte bunlar} her yetiyi hesaba dağıtır ve {ar:عَنْهُ, tr:ʿanhu, gloss:onun hakkında} konuyu açık tutar. Bu sıra duyumdan iddiaya ve eyleme geçiş için ayrı bir değerlendirme eşiği kurar: algı, yorum ve hüküm adımlarının her biri cevaplanabilir bir aşamadır.

ʿIlm'in bilme ve gerçeği kavrama anlamına ek olarak, bir şeyi ayırt ettiren nişan veya yol gösteren işaret kullanımı da vardır. İz sürme ve yetilerin hesabıyla temas eden bu kullanım, belirgin bir dağ, yol levhası ya da kumaş bordürü gibi sınırları tanımaya yarayan işaretleri akla getirir. İşaret takip edilen şeyin ne olduğunun sınanmasına dayanak olur; bu imge belirli bir soruşturma, haber veya suçlama seçmeden, algıdan hükme uzanan ve her adımı açıklanabilir bir kanıt hattını öne çıkarır.

## Duyulan Söz, Soru ve İsnat

İşitme sözlüğündeki başka bir dal, adın veya şöhretin duyulup yayılmasını; bazı ettirgen biçimler ise haberin yayılmasını anlatır. Odaktaki {ar:ٱلسَّمْعَ, tr:as-samʿa, gloss:işitme} işitme yetisinin adıdır; duyulan sözün dolaşıma girmesi, iz sürme, görme, gönülde değerlendirme ve hesap ilişkisiyle kurulan olası bir yankıdır, ayetin anlattığı gerçekleşmiş olay değil. Bu ihtimalin çevresindeki iki bağlam kendi konularını korur: ana babaya yöneltilen güzel sözü düzenleyen buyruk kamusal söylentiyi konu edinmez (17:23), savurganlık uyarısı kaynakların saçılmasını anlatır (17:26). Bunları haberin yinelenen aktarımıyla yan yana getirmek, duyulanı almakla başkalarına yaymayı ayrı sorumluluk aşamaları olarak görmeye yarayan keşifsel bir benzetme kurar. Bu bağlantı kişinin kendi inanç ve bilgi denetimine de uygulanabilir; haberin toplumsal dolaşımını kesinleştirmez.

Bilgi eşiği duyulanı aktarmanın yanında, bilgi bulunmayan şeyi sormayı da ölçer. Nuh'a verilen cevapta aynı koşul soru biçiminde kurulur: Allah, “bilgin olmayan şeyi bana sorma” der (11:46). Bu belirli karşılık, 17:36'daki takip nesnesine soru yoluyla arayışı ekleyerek aynı bilgi eşiğini görünür kılar; Nuh'a özgü bu cevap bütün sorular için genel bir şablon oluşturmaz.

Taqfu biçiminin olağan anlamı iz sürmektir; q-f-w kökünün başka sözlük kullanımları ise bir kişiye çirkin eylem isnat etmeyi, asılsız suçlama veya yalancı tanıklıkla itibarını zedelemeyi ve gizlice kusur aramayı içerir. Odak biçim nehiy altında ikinci tekil muhataba yöneltilmiş takip fiilidir; isnat ve suçlama anlamları aynı kökün ayrı sözlük dalında kalır. Bu dal, kanıtlanmamış izin kişiye yöneltilmesiyle doğan itibar zararını görünür kılar. Haberin zarar vermeden önce araştırılması istenir (49:6); bilinmeyen bir şeyin dillerle aktarılıp ağızla söylenmesi anlatılır (24:15); duyulmuş söz için büyük iftira nitelemesi yapılır (24:16). Bu örneklerle odaktaki duyma, görme ve iç yönelim birlikte düşünüldüğünde, itibar zedeleyici iddiayı kabul etmemek, onaylamamak ve dolaşıma katmamak yönünde pratik bir uyarı belirir. Odak fiil iz sürme anlamını korur; suçlama riski ayrı sözlük dalı ve bu ayetlerdeki sınırlı bağlamların katkısıdır, her haber için evrensel bir hukuk hükmü değil.

Duyulan ve görülen izler başkalarının iç saiki hakkında hükme dönüştüğünde başka bir sınır belirir. İnsanların içlerinde olanı Allah'ın bildiği söylenir (17:25); ilahî bilgi, görme ve rızkın genişletilip daraltılması da komşu bağlamda anılır (17:30). Oradaki {ar:خَبِيرًا بَصِيرًا, tr:khabīran baṣīran, gloss:haberdar ve gören} sıfatındaki baṣīre yüklenen içgörü ve doğrulanmış idrak anlamı o bağlama aittir; odak ayetteki {ar:ٱلْبَصَرَ, tr:al-baṣara, gloss:görme} ise fiziksel görme yetisini adlandırır. Bu ayetler ilahî bilgiyi, görmeyi ve rızık üzerindeki tasarrufu hatırlatır; insanın her saiki okuyamayacağına dair genel bir hüküm kurmaz. Odaktaki bilgi eşiği, gözlenebilir izden çıkarılan sonuçla görülmemiş niyeti kesin bilgi diye sunmayı ayırır.

Kuruntunun çoğundan sakınma, tecessüs ve gıybetten kaçınma uyarıları bu ayrımı davranış alanına taşır (49:12); gaybı Allah'ın bildiği ve insanların yaptıklarını gördüğü de belirtilir (49:18). Bu karşılık, başkasının saiki hakkındaki kanıtsız kuşkuyu bilgi yerine koymayı sınırlar. Davranış yorumları kanıta dayanabilir; uyarının sınırı, erişilemeyen niyeti kesin bilgi diye sunmaktır.

## Emanet, Ölçü ve Yön

Yetilerin nasıl kullanıldığı sorusu, yetim malını koruma buyruğunun ardından gelen ahdi yerine getirme ve ahdin de hesaba konu oluşuyla emanet çerçevesine girer (17:34). Allah'ın ahdinin cevaplanabilirliğini bildiren benzer ifade bu hesap dilini başka bir bağlamda yineler (33:15). Bu ortaklık, işitme, görme ve gönlü alınan bilginin nasıl karşılandığı, saklandığı ve aktarıldığı bakımından emanet edilmiş tanıklar gibi okumaya açar. Bu benzetme yetileri ahitle özdeşleştirmez; dayanağı iki bağlamdaki ortak hesap dilidir.

Bilgi eşiği ölçü fikriyle de temas eder. Hemen önceki buyruk ölçüyü tam vermeyi, ölçerken yeniden tam ölçmeyi, doğru teraziyle tartmayı ve bunun iyi sonuç doğuracağını söyler (17:35). {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} için ayırt ettiren işaret kullanımı ile {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek}in iz sürmesi yan yana geldiğinde, iddianın dayanağını yeniden karşılaştırma, ağırlığını değerlendirme, düz ve tarafsız bir ölçü arama, hükmün neticesini düşünme çizgisi belirir. Terazi benzetmesi iddianın dayanağını ve sonucunu tartma fikrini taşır; raporlar fiziksel terazide tartılmaz, 17:35 ile 17:36 da ayrı buyruklar olarak kalır. Böylece tam ölçü ve iyi sonuç dili, izlenen kanıtı eylemden önce yeniden sınamanın özenini somutlaştırır.

İnsan kudretine konan sınır bu ölçüyü beden ölçeğine taşır: kişi yeri delemez, dağların yüksekliğine erişemez (17:37). Bu somut erişim sınırı, taqfu'nun iz sürme anlamıyla yan yana geldiğinde takibin hem kanıta hem insan kudretine göre ölçülmesini düşündürür. Yeri delme imgesi taqfu'nun sözlük anlamı değil, bedensel erişimden bilgiye erişime uzanan bağlamsal köprüdür. Q-f-w kökünün ayrı suçlama ve yalancı tanıklık dalı da başka bir aşırı erişim imgesi sunar: sahte tanıklık kanıtın taşıdığından ileri uzanan bir iddiadır. Bu iki katkı, biri bedensel kudreti, diğeri tanıklığın dayanağını ölçerek sınır fikrini belirginleştirir; bağlantı keşifseldir. 17:37'nin kibirli yürüyüşe karşı öğüt olarak okunması da kendi bağlamını korur. Komşu buyruklarda sözün yönü, ilahî bilgi ve görme, saik ve eylem sınırları, doğru tartı ve bedensel erişim ayrı ayrı ölçülür (17:23, 17:30, 17:31, 17:33, 17:35, 17:37); 17:36 bu dizide iddiayı izlemenin bilgi dayanağını belirler. Bu ölçü araştırma için dayanağı, iddiadan hükme ve eyleme geçiş için de gözetilecek sınırı verir.

Bedensel sınırı izleyen değerlendirme, önceki davranışları topluca ele alır (17:38). Oradaki {ar:كُلُّ ذَٰلِكَ كَانَ سَيِّئُهُۥ عِندَ رَبِّكَ مَكْرُوهًۭا, tr:kullu dhālika kāna sayyiʾuhu ʿinda rabbika makrūhā, gloss:bunların kötüsü Rabbin katında hoş karşılanmaz} ifadesinde kullu önceki eylemleri bir araya getirir; dilbilgisel gönderimi eylemlerdir. Odak ayetteki {ar:كُلُّ, tr:kullu, gloss:her biri}nin yetileri dağıtması ve {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:sorgulanır}ın hesap dilini kurması, buna karşılık yetileri davranışın algılanıp karara bağlandığı bir denetim katmanı olarak düşünmeye elverir. Bu paralellik, yetilerdeki hesap dilini çevredeki eylemlerle birlikte okumayı mümkün kılar; denetim katmanı yorumu bağlamsal kalırken 17:38'in açıkça değerlendirdiği şey önceki davranışlardır.

Bir sonraki ayette buyruk dizisi vahyedilmiş hikmet olarak nitelenir (17:39). Hikmet, doğru yargıyı yönlendirerek bilgi dayanağının doğrudan görmeye indirgenmediğini gösterir. İşitmenin duyulanı anlama, kabul etme ve ona göre davranma yönü bu bağlamda vahyi alma ve karşılık verme sürecini de düşündürür. Gizli yoldan bilgi ulaştırma veya ilahî bildirim açıklaması, bu pasajla kurulan bağlamsal okumadır; sözlük anlamı diye genellenmez. Hikmetin muhatabı özellikle elçi olabilir. Böylece vahyedilmiş hikmet duyusal erişimi aşan bir bilgi dayanağı sunar; bu örnek doğrulanmamış her haber için genel bir kabul ölçütü değildir.

İz sürme imgesi Fâtiha'daki yol duasıyla birlikte okunduğunda yön bakımından yeni bir karşılık kazanır (1:6, 1:7). {ar:تَقْفُ, tr:taqfu, gloss:ardına düşmek} ile taşınan takip, dosdoğru yola yönelme isteğiyle yan yana gelir; 1:7 bu yolu nimete erenlerin yolu olarak belirler ve öfkeye uğrayanlarla sapmışları ondan ayırır. Bu alıntı ya da özdeşlik değil, bilgi eşiğini kendi anlamında tutan keşifsel bir yön ilişkisidir: bilmeden iz sürmenin karşısında, kendi başına güzergâh seçmek yerine rehberliği istenen yolu arama imkânı belirir.

</source_prose>
