# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:34**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.middle.claims.json`

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
- Refer to source paragraphs as `17:34 ¶N`.

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

`(17:34 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:34",
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
        "citation": "(17:34 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_34/17_34.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_34/17_34.middle.claims.json \
  --ayah-ref 17:34
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_34/17_34.prose.editorial.tr.md`

<source_prose>
## Malın Sınırı ve İyi Muamele

Yetimin malı önce yaklaşma yasağıyla koruma altına alınır: {ar:لَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ, tr:lā taqrabū māla al-yatīmi, gloss:yetimin malına yaklaşmayın}. Ardından gelen {ar:إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ, tr:illā bi-llatī hiya aḥsanu, gloss:ancak en iyi biçimde}, erişimin bütünüyle kapatılmadığını, yalnız en iyi muamele yoluyla açıldığını bildirir. Gözetim {ar:حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ, tr:ḥattā yablugha ashuddahu, gloss:olgun gücüne erişinceye kadar} çocuğun kendi olgun gücüne erişmesine dek sürer. Bu eşiğin ardından {ar:وَأَوْفُوا۟ بِٱلْعَهْدِ, tr:wa-awfū bi-l-ʿahdi, gloss:ahdi eksiksiz yerine getirin} buyruğu yükümlülüğün tam ifasını ister; {ar:إِنَّ ٱلْعَهْدَ كَانَ مَسْـُٔولًا, tr:inna al-ʿahda kāna masʾūlan, gloss:ahit hakkında hesap sorulacaktır} kapanışı da ahdi hesap verilecek bir sorumluluk olarak kurar. Böylece koruma, malın kime ait olduğu, gözetimin ne zamana kadar süreceği ve üstlenilen işin nasıl tamamlanacağıyla birlikte düşünülür.

Yasağı kuran {ar:لَا, tr:lā, gloss:yaklaşmayın} ile ikinci çoğul meczum {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşın}, muhatapların kendi hareketlerine sınır koyar; yalnızca uzak durma hâlini betimlemez. Fiilin birinci bâb biçimi, malı yaklaştırmayı değil, kişinin mal alanına kendisinin yönelmesini anlatır. Yaklaşma temas etmeyi ya da bir işe karışmayı da kapsadığından, {ar:مَالَ, tr:māla, gloss:mal} ile birleşen yasak tamamlanmış el koymadan önce işler: zarar doğurabilecek tasarrufa giden yönelişi de keser. Sınır, zarara açılabilecek yönelişi keserken gündelik teması bütünüyle dışlamaz; hemen arkasındaki istisna da malın hangi yolla ele alınabileceğini belirler.

{ar:مَالَ, tr:māla, gloss:mal}, fiilin doğrudan nesnesi olarak yalnızca sonradan yenecek ya da harcanacak kısmı değil, sahip olunan değerli varlığın bütününü korur. Sürü anlamı göçebe toplulukların kullanımında kalırken burada sözcük kişinin mülkünü anlatır. İyelik yapısındaki {ar:ٱلْيَتِيمِ, tr:al-yatīmi, gloss:yetim}, malın sahibini de cümlenin içine yerleştirir. İnsan için yetim, ergenliğe erişmeden babasını yitirmiş çocuktur; koruma ihtiyacı olağan babalık desteğinden yoksun kalmasıyla belirginleşir. Buradaki kullanım, hayvan yavrusu anlamından ayrılarak insan çocuğunu ve onun malını odağa alır. Vasinin yetim malını kendi malına katarak tüketmesine karşı çıkan çağrı, bu mülkiyet ayrımını somutlaştırır: gözetim vasinin elinde olsa da mal çocuğa ait kalır (4:2).

{ar:ٱلْيَتِيمِ, tr:al-yatīmi, gloss:yetim} insan çocuğu anlamının yanı sıra tek başına kalmış ya da benzeri az bulunan bir şeyi de niteleyebilir. Çocuğa ait belirli malın korunması bu seyrek çağrışımla buluştuğunda, her sahibin kıymeti eşsiz bir inciyi andırır. İnci benzetmesinin taşıdığı değer, malın maddi niteliğine değil, korunan çocuğun tekilliğine ilişkindir.

İstisna bildiren {ar:إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ, tr:illā bi-llatī hiya aḥsanu, gloss:ancak en iyi biçimde}, yaklaşmama buyruğunun içinde {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşın} fiilinin izin alanını düzenler. {ar:بِٱلَّتِى, tr:bi-llatī, gloss:hangi yolla} içindeki bā, yetim malına erişimin nasıl gerçekleşeceğini gösterir; korunan nesne baştan sona çocuğun malı olarak kalır. Başsız dişil ilgi adılı {ar:ٱلَّتِى, tr:allatī, gloss:hangi yol ki} yolu önceden tek bir yöntemle adlandırmadan açık bırakır. Dişil tekil biçimin eril mal adıyla uyuşmaması, örtük göndergenin maldan çok ona muamele etme yolu olduğunu düşündürür. Açık {ar:هِىَ, tr:hiya, gloss:o} zamiriyle üstünlük derecesindeki {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi} tam bir ölçü kurar: yeterli görülen herhangi bir yöntem değil, en iyi yol izinlidir. Duruma göre yöntem değişebilse de ölçünün titizliği değişmez.

Bu ölçüdeki {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi}, güzelliği ve iyi yapılmış işi de duyurur. Yetimin malıyla yan yana gelen üstünlük, iyiliği kötü davranıştan kaçınmanın ötesinde doğru ve özenli bir icraya taşır; eylem başkasına yöneldiğinde ona yarar sağlama anlamı da kazanır. Böylece yasak içindeki izin, yalnız haksız tüketimi önlemekle kalmaz, mal üzerinde yetime fayda getiren bir iş görme imkânı açar. İzin, zarar doğurabilecek tasarrufa karşı sınırı korurken yarar sağlayan erişime alan açar; hangi vesayet yönteminin kullanılacağını ise açık bırakır.

Yetim malının yararı, başkasına ait hakkın sahibine ulaştırılmasıyla görünür; aynı bağlamdaki savurup saçma yasağı da değerin tüketilmesine karşı sınırı çizer (17:26). Elin boyna bağlanması kullanımı felce uğratan kısıtlamayı, bütünüyle açılması ise ölçüsüz saçmayı canlandırır (17:29). Rızkın genişletilip daraltılması bunlara, paylaştırmanın ölçüye göre ayarlanabileceği boyutunu ekler (17:30). Birlikte bu sahneler, malı savurmadan ve sahibinin yararına kullanılamaz hâle getirmeden yönetme aralığını görünür kılar. Harcama ölçüsünü yetim malının gözetimine uygulamak ihtiyatlı bir bağlam okuması olarak kalır; odak ayet belirli bir idare usulü tarif etmez.

Yaklaşmanın önceden sınırlanması, başka bir nesneyle zina hakkında da görünür: aynı {ar:تَقْرَبُوا۟, tr:taqrabū, gloss:yaklaşın} fiilinin ardından eylemi çirkin, ona giden yolu kötü diye niteleyen ifade gelir (17:32). Bu örneğin katkısı, fiilin gerçekleşmiş zararın yanı sıra ona açılan güzergâha da yönelmesini göstermektir. Bağlantı bu önleyici işleve aittir: 17:32 zinayı ve ona giden yolu yasaklarken 17:34’te {ar:مَالَ ٱلْيَتِيمِ, tr:māla al-yatīmi, gloss:yetimin malı} üzerinde {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi} muamele yolu açık kalır.

Mal sahibine ait hakkın teslimi, yetim malını gözetenin kimin yararına hareket ettiğini belirler (17:26). Öldürülen kişinin velisine etkili bir yetki tanınırken, öldürmede aşırıya gitmeme uyarısı bu yetkiyi sınırlar (17:33). İki sahnenin ortak katkısı, başkasının hakkı adına kullanılan gücün sınırlı olabileceğini göstermeleridir. Bağlantı temsil ve sınır ilkesinde kalır: 17:33’teki makam, öldürülen kişinin yakınına ve öldürme yetkisine aittir; yetim malı için aynı hukuk yolunu kurmaz. Bu bağlamda gözetenin takdiri, mal sahibinin yararına bağlı kalır.

Aynı üstünlük derecesi, en iyi sözü seçme buyruğunda konuşmanın niteliğini belirler (17:53); kötülüğe daha iyi bir davranışla karşılık verme ölçüsü ise düşmanlığa verilen yanıtı düzenler (41:34). Bu iki örnek, {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi} standardının eylemde nasıl gerçekleştiğini göstererek 17:34’teki iyi muameleyi de somutlaştırır. Katkıları davranışın niteliğini aydınlatmaktır; yetim malına ilişkin ayrı bir hüküm kurmazlar.

## Süre ve Olgunluk

{ar:حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ, tr:ḥattā yablugha ashuddahu, gloss:olgun gücüne erişinceye kadar}, gözetimin sonunu yetimin ulaşacağı bir eşiğe bağlar. {ar:حَتَّىٰ, tr:ḥattā, gloss:-e kadar} süreyi sınırlar; mansub muzari biçimindeki {ar:يَبْلُغَ, tr:yablugha, gloss:ulaşmak} henüz gerçekleşmemiş bir varışı anlatır. Fiil ettirgen değildir: eşiğe ulaşan koruyucu değil, çocuğun kendisidir. {ar:أَشُدَّهُۥ, tr:ashuddahu, gloss:olgun gücü} de genel bir kategori yerine onun kendi gücünü adlandırır; bedensel kuvvet, yetişkinlik, sağduyu, deneyim ve dayanıklılık anlamlarını bir araya getirir. Kişinin kendi kapasitesine bağlı bu zaman sınırı, koruyucuya süresiz sahiplik değil, olgunluğa kadar süren bir gözetim verir.

Olgunluk için aktarılan farklı yaşlar ve {ar:أَشُدَّهُۥ, tr:ashuddahu, gloss:olgun gücü} biçiminin farklı çözümlenişleri, tek bir takvim sayısından çok yeterliğe açılan bir eşiğe işaret eder. Bu yeterlik, iş ve mal ilişkilerini taşıyabilme olarak düşünülebilir; kişinin kendi adına iş görmesi ve söz alması da hafifçe sezilir. Burada konuşma ayrıca sahnelenmediği için bu son çağrışım bir yaş, sınama yolu ya da hukukî devir işlemi belirlemez.

4:6’da yaşama eşiğine ulaşmanın ardından {ar:رُشْدًا, tr:rushdan, gloss:sağduyu olgunluğu} ayrıca tanınır ve malın teslimi bu tanımadan sonra gelir. Bu iki aşamalı dizi, 17:34’teki {ar:يَبْلُغَ, tr:yablugha, gloss:ulaşmak} ile {ar:أَشُدَّهُۥ, tr:ashuddahu, gloss:olgun gücü} ifadesine temas ettiğinde yaşın yanında sorumluluk taşıma kapasitesini de düşündürür (4:6). Bu temas, 17:34’ün bedensel ve kronolojik eşiğine kapasite boyutunu ekler; 4:6’daki ayrı rüşd tanıması kendi mal teslimi dizisinde kalır. Bu karşılaştırmadan 17:34 için sayısal yaş ya da hukukî-mali ehliyet ölçütü çıkmaz.

Bu kişisel yeterlik, yakın bağlamda başkasına bakım vermenin başka bir zaman ölçeğiyle karşılaşır. Anne-babanın kişinin yanında yaşlılığa erişmesi, odaktaki {ar:يَبْلُغَ, tr:yablugha, gloss:ulaşmak} fiiliyle aynı varış fikrini taşır; ortaklık erişme eylemindedir, yaşlılıkla çocuğun olgunluğunun aynı eşik olmasında değil (17:23). Aynı ayetteki {ar:إِحْسَٰنًا, tr:iḥsānan, gloss:iyilik ederek}, yarar sağlayan davranışı bir eylem olarak adlandırır; ebeveyne somut bakım, {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi} yolun niteliğine ayrı bir örnek sunar. Anne-babanın çocuğu küçükken yetiştirdiğini anması da büyümeyi ve alınmış bakımı öne çıkarır (17:24). Bu kuşaklar arası temas, bakımın gelişime eşlik edebileceği ihtimalini açar; ebeveyn bakımıyla yetiştirilme hatırasını odaktaki olgunlaşma eşiğine bağlayan ihtiyatlı bir bağlam okumasıdır, ayrı bir yetiştirme buyruğu ya da devir ölçütü değildir.

Varış fiilinin başka bir ölçekteki kullanımı, bu yeterlik düşüncesini insanın erişemeyeceği kudretten ayırır. Dağlara boyca erişememek dikey sınırı, yeri delemeden geçememek ise derinlik karşısındaki sınırı canlandırır (17:37). İki somut engel birlikte, insanın erişemediği bir güç tasavvuru kurar; {ar:أَشُدَّهُۥ, tr:ashuddahu, gloss:olgun gücü} ise ulaşılabilir bir insan eşiğidir. 17:37’nin kibir eleştirisi olarak da okunabilmesi, bu bağlantıyı olgunluğu imkânsız bir kudretle karşılaştıran imge düzeyinde tutar; dağlar yetim malı için hukukî bir yeterlik ölçüsü vermez.

Emanetlerin sahiplerine adaletle geri verilmesi buyruğu, gözetimin yöneldiği sonu görünür kılar: koruma hak sahibine dönüşle tamamlanır (4:58). Bu ışıkta {ar:حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ, tr:ḥattā yablugha ashuddahu, gloss:olgun gücüne erişinceye kadar}, çocuğun malını kendi yeterliği belirene dek gözetilen sınırlı bir emanet gibi duyurur. Ardından gelen {ar:وَأَوْفُوا۟ بِٱلْعَهْدِ, tr:wa-awfū bi-l-ʿahdi, gloss:ahdi eksiksiz yerine getirin}, malın olgunlukta eksiltilmeden sahibine bırakılmasını doğal bir tamamlanış olarak sezdirir. Bu, süre eşiğiyle ifa buyruğunun birlikte düşündürdüğü bir teslim okumasıdır; ayet resmî bir devir usulü tarif etmez.

## İfa ve Hesap

Süreli gözetimden ahdin ifasına geçişi açan {ar:وَ, tr:wa, gloss:ve}, burada hükümleri yan yana getirmekle kalmaz, buyruğun yönünü de değiştirir. Mal üzerinde zararlı tasarruftan sakınmanın ardından üstlenilen yükümlülüğü etkin biçimde yerine getirme emri gelir. {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi}, yetim malına yaklaşmanın niteliğini belirlerken, {ar:أَوْفُوا۟ بِٱلْعَهْدِ, tr:awfū bi-l-ʿahdi, gloss:ahdi eksiksiz yerine getirin} başka bir işi, ahdin tam ifasını ister. İki emir birbirini tamamlar: biri iyi muamelenin niteliğini, diğeri yükümlülüğün yerine getirilmesini belirler.

{ar:أَوْفُوا۟, tr:awfū, gloss:eksiksiz yerine getirin}, dördüncü bâbın ikinci çoğul emir biçimidir; muhataplardan yerine getirme işini tamamlamalarını ister. Burada öne çıkan bağlılığın bir kimlik sıfatı olması değil, yükümlülüğü eksiksiz icra eden eylemdir. {ar:ٱلْعَهْدِ, tr:al-ʿahdi, gloss:ahit} ile birlikte fiil, verilen sözü ve bağlayıcı yükümlülüğü bozulmadan yerine getirmeyi buyurur. {ar:بِٱلْعَهْدِ, tr:bi-l-ʿahdi, gloss:ahde} içindeki bā, ifanın neye bağlandığını gösterir; istisnadaki {ar:بِٱلَّتِى, tr:bi-llatī, gloss:hangi yolla} bā ise izinli yaklaşmanın tarzını belirtir. Aynı biçim iki ayrı ilişki kurar: biri ahdi ifanın konusu yapar, diğeri yaklaşmanın yolunu gösterir. 17:35’te aynı emir ölçü miktarının eksiksiz verilmesini örnekler; nesne değiştiğinde bu ölçü anlamı ahde aktarılmaz. Buradaki ahit, belirli bir sözleşme türünden önce tutulması gereken bağlayıcı söz ve yükümlülüktür.

Ölçü bağlamında aynı fiil, ölçme anında miktarı eksiksiz vermeyi ister (17:35). {ar:ٱلْكَيْلَ, tr:al-kayla, gloss:ölçülen miktar} ölçülecek ayrı miktarı, {ar:كِلْتُمْ, tr:kiltum, gloss:ölçtüğünüzde} ölçme eylemini belirtir. Ardından tartma gelir; {ar:ٱلْقِسْطَاسِ, tr:al-qisṭās, gloss:ölçü aleti} teraziyi, {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīm, gloss:doğru ve dengeli} adil standardı gösterir. Miktar, işlem, alet ve ölçüt sıralandığında tam ifa gözle görülebilir ve sınanabilir bir edim olur. Bu sahne ölçüp tartmada doğruluğu örnekler; 17:35 yetim malı için ayrıca bir kayıt usulü belirtmez. Bu örneğin 17:34’teki emanet gözetimine doğrudan uygulanıp uygulanmadığı açık kalır; 17:36’daki bilgi ve muhakeme sorumluluğu da daha geniş etik çerçevede komşu bir sorumluluk alanı olabilir (17:35, 17:36).

Ölçü buyruğunun sonunda 17:35 daha hayırlı ve sonuç bakımından daha iyi bir varış ufku açar (17:35). Bu olumlu sonuç ya da karşılık yönünü {ar:تَأْوِيلًا, tr:taʾwīlan, gloss:sonuç ve varış} taşır: odaktaki {ar:أَحْسَنُ, tr:aḥsanu, gloss:en iyi} izinli yolun niteliğini, komşu ayetteki ifade ise tam ölçü ve doğru tartının varacağı sonucu belirginleştirir. Böylece ölçünün değerlendirilmesi, o anki işlemden onun sonucuna uzanır; bu ufuk belirli bir dünyevî başarıyı garanti etmez.

Ölçülebilen miktarlar, yetim malının tek bir toplam değer olarak değil, ayrı hak sahiplerinin payları halinde de izlenebileceği ihtimalini doğurur. {ar:مَالَ, tr:māla, gloss:mal} korunan varlığı, {ar:ٱلْيَتِيمِ, tr:al-yatīmi, gloss:yetim} ise onu kimin adına tuttuğumuzu hatırlatır. Yetim sözcüğünün tek başına kalma ya da benzeri az bulunma çağrışımı, 17:35’teki ayrık miktarlarla buluşunca her çocuğun payını belirlenebilir kılma fikrini açar (17:35). Nadir ve tekil olma çağrışımı böylece ayrı miktarların izlenebilirliğiyle birleşir: ortak emanet içinde her çocuğun ne kadar ve hangi değerle korunduğu görünür tutulabilir. Bu ihtiyatlı vesayet iması, payların ayırt edilebilirliğini öne çıkarır; ortak havuzu yasaklamaz ve ayrı hesap tutmayı zorunlu kılmaz.

17:36, ölçülebilir sonucun yanına kararın bilgi temelini de getirir. Bilinmeyen bir iz ya da iddianın peşinden gitmeme uyarısı, neye dayanarak hüküm verildiğini öne çıkarır. İşitme, görme ve iç muhakeme birlikte sorumluluk alanına girer; duyulanı anlama, fark etme ve tartma da hesaba katılır. Ayetin sonunda bu üçünün her biri odaktaki {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:hakkında soru sorulacak} edilgen niteliğiyle sorulabilir kılınır (17:36). Böylece emanet gözetiminde yalnız malın son durumu değil, karara götüren algı ve muhakeme de hesap alanına girer; ayet bu sorumluluğu resmî arşiv ya da denetim usulüne dönüştürmez.

Emirde {ar:بِٱلْعَهْدِ, tr:bi-l-ʿahdi, gloss:ahde} ile ifaya bağlanan ad, kapanışta {ar:إِنَّ ٱلْعَهْدَ, tr:inna al-ʿahda, gloss:şüphesiz ahit} yapısında cümlenin konusu olur. Aynı ahit önce yerine getirilecek şey, sonra hakkında hüküm verilen yükümlülük olarak duyulur; bu tekrar ifa buyruğunun gerekçesini de görünür kılar. Vurgulu {ar:إِنَّ, tr:inna, gloss:şüphesiz} bir koşul ya da olumsuzluk değil, bildirimi kuvvetle ileri sürer. {ar:كَانَ, tr:kāna, gloss:idi ve durumunda bulunuyordu} geçmiş biçimi, sorulabilirliği yeni başlayan bir olaydan çok yerleşik bir durum gibi sunar.

Belirsiz ve tanvinli edilgen ortaç {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:hakkında soru sorulan}, ahdi hesap sorulmasının konusu yapar ve nitelemeyi tek bir vakaya kapatmadan genelleştirir. Sorma, isteme ve talep etme anlamları, ahit ile {ar:أَوْفُوا۟, tr:awfū, gloss:eksiksiz yerine getirin} buyruğunun kurduğu yükümlülüğe değince merak sorusu hesap talebine dönüşür: ahdin gereğinin nasıl yerine getirildiği gündeme gelir, soru mercii ve yöntemi ise adlandırılmadan kalır. Sondaki hemze kapanışı işitsel olarak belirginleştirir; edilgen ortaç kalıbının seyrekliği anlamı belirleyen unsur değil, ikincil bir dağılım gözlemidir.

Belirli vadeli borcun yazıyla kayda alınması ve tanıkla doğrulanması, hakkın eksiltilmesine karşı zayıf tarafı gözeten bir düzen örneği sunar (2:282). Bu yazılı iz ve tanıklık, ifanın görünür biçimde doğrulanmasına katkıda bulunur. Kişinin kendisine tam ölçü alırken başkasına eksik vermesi ise kendi lehine kurulan ölçünün ötekine uygulanmayabileceğini gösterir; tam teslim iddiası tek başına kendini doğrulamaz (83:2). Bu iki örnek, ifanın gözlenebilir ve sınanabilir oluşunu aydınlatır. 2:282’nin kayıt düzeni vadeli borca özgüdür; 17:34’le kurulan bu bağlantı her ahit için aynı yazılı usulü ya da yetim malına özgü bir yöntem öngörmez.

Emanetleri ve ahitleri gözetmenin birlikte anılması, süre boyunca yenilenen sorumluluk için bir çerçeve sunar (70:32). Ahdin isim biçimi tutulması gereken bağlayıcı sözü anlatır; aynı söz ailesinin bazı fiil biçimleri ise durumu yeniden yoklama ve sorumluluğu sürdürme anlamı taşır. Bu fiilsel çağrışım, olgunlukta sona eren gözetim çizgisiyle buluşunca korumayı zaman içinde yinelenen bir görev gibi duyurur, ancak isim biçimiyle aynı kullanım değildir. Ahdin kendisinin de sorulacak sayılması, {ar:أَوْفُوا۟ بِٱلْعَهْدِ, tr:awfū bi-l-ʿahdi, gloss:ahdi eksiksiz yerine getirin} buyruğu ile edilgen {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:hakkında soru sorulacak} yüklemini yan yana getirir (33:15). Bu temas, bağlayıcı sözün yalnızca verilmesini değil, gereğinin yapılmasını ve bunun hesabının verilebilmesini öne çıkarır; yazılı belge şartı koymaz.

Alışverişte kullanılan ayrı bir biçim olan {ar:ٱلْعُهْدَة, tr:al-ʿuhda, gloss:ayıp ya da hak iddiasına karşı güvence}, sonradan ortaya çıkabilecek ayıp ya da hak talebine karşı güvence sağlayan şartı veya belgeyi adlandırabilir. Bu ticari terimin biçimi ve kullanım alanı, odaktaki {ar:ٱلْعَهْدِ, tr:al-ʿahdi, gloss:ahit} sözcüğünden ayrıdır. 17:35’teki ölçü, tartı ve doğruluk standardı alışverişteki güvenceyi hatırlatırken, odaktaki tam ifa buyruğu ve ahdin sorulabilir oluşu olası bir sonradan karşılama ya da onarım sorumluluğu imgesini açar. Bu bağlantı yalnızca ihtiyatlı bir ticari yankıdır: odak ayet satış, talep sahibi, iade ya da belirli bir onarım yolu kurmaz.

## Hesabın Daha Geniş Ufku

Fâtiha’daki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi d-dīn, gloss:hesap ve karşılık gününün sahibi} ifadesi, 17:34’teki yerel mal ve ahit yükümlülüğüne daha geniş bir karşılık ufku ekler (1:4). Odaktaki {ar:مَسْـُٔولًا, tr:masʾūlan, gloss:hakkında soru sorulacak} ile {ar:ٱلدِّينِ, tr:al-dīn, gloss:hesap ve karşılık} arasındaki temas, soru ve hesap düşüncesindedir; sözcükler eşanlamlı değildir. Böylece sahibine teslim pratik sorumluluk olarak yerinde kalırken nihai karşılık da ufka girer. Bu bağlantı ahdin anlamını eskatolojik bir terime çevirmek yerine, yerel yükümlülüğü daha geniş hesap düşüncesinin yanında duyurur.

Herkesin kendi kitabıyla karşılaşması, hesap imgesine kişisel bir muhataplık kazandırır; en ince lifine kadar uzanan kayıt ise bu hesabın ayrıntısını duyurur (17:71). Bu iki özellik {ar:إِنَّ ٱلْعَهْدَ كَانَ مَسْـُٔولًا, tr:inna al-ʿahda kāna masʾūlan, gloss:ahit hakkında hesap sorulacaktır} ifadesine değdiğinde, yükümlülüğün eylem bittikten sonra da kişiye ait okunabilir bir iz bırakabileceği ihtimalini açar. 17:71 ile ahit arasında doğrudan kurulmuş bir bağ olmadığından, bu kişisel ve ayrıntılı kayıt imgesi sözlük anlamı ya da yerleşik yorum çizgisi değil, sorumluluğun görünürlüğüne dair ihtiyatlı bir çağrışım olarak kalır.

</source_prose>
