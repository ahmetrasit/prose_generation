# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:26**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.middle.claims.json`

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
- Refer to source paragraphs as `17:26 ¶N`.

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

`(17:26 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:26",
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
        "citation": "(17:26 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_26/17_26.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_26/17_26.middle.claims.json \
  --ayah-ref 17:26
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_26/17_26.prose.editorial.tr.md`

<source_prose>
## Alıcının Hakkı

17:26'nın alışılmış okuyuşu, yakın akrabaya hakkını vermeyi, yoksulu ve yolcuyu aynı buyruğa katmayı, ardından da malı savurganca saçıp ziyan etmeyi yasaklamayı söyler. Başındaki {ar:وَءَاتِ, tr:wa-āti, gloss:ve ver} biçiminde vav, emri sürmekte olan söyleme bağlar; önceki sözün içeriğini tek başına açıklamaz. Bitişik yazımda bağlama ile eylemin başlaması iç içedir: vav sözü sürdürürken {ar:ءَاتِ, tr:āti, gloss:ver} fiili hemen emir kipine geçer, bu yüzden ayet bağımsız ve yeni bir yönerge gibi açılmaz. Form IV'ün ikinci tekil kişiye yönelen gizli “sen” öznesi fiilde duyulur, ancak muhatabın kimliği ya da toplumsal rolü belirlenmez. Vavdan sonraki hemze kısa bir gırtlak kapanışıyla işitilir; bu ses eşiği ayrıca bir anlam ayrımı kurmaz.

Emir iki nesneli bir aktarım kurar: {ar:ذَا ٱلْقُرْبَىٰ, tr:dhā al-qurbā, gloss:yakın akrabalık sahibi} ilk nesne, yani alıcı; {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:ona ait hak/pay} ikinci nesne, yani ulaştırılacak şeydir. {ar:ذَا, tr:dhā, gloss:yakınlık sahibi} beş isim çekimindeki mansup biçimiyle alıcı konumundadır; belirli ve mecrur {ar:ٱلْقُرْبَىٰ, tr:al-qurbā, gloss:yakınlık/akrabalık} onu ilişki içinde tanımlar. İkinci nesnenin sonundaki “-hu” eki payı aynı kişiye bağlar. Böylece sözdizimi sahibine yönelmiş hak teslimini duyurur ve miktarı açık bırakır. {ar:ءَاتِ, tr:āti, gloss:ver/ulaştır} olağan verme ve ulaştırma buyruğu olarak kalır; belirli bir vergi ya da tahsilat mekanizması tarif etmez.

Bu tamlamada {ar:ذَا, tr:dhā, gloss:ilişki taşıyan kişi}, yakın olma ve akrabalık alanlarını tek bir muhatapta toplar; yakınlık soy ve aile bağıyla kurulur, derecesi açık kalır. {ar:ٱلْقُرْبَىٰ, tr:al-qurbā, gloss:yakınlık} sözcüğünün yaklaşma alanı, başka bir kullanımda Tanrı'ya yakınlık arayan işi ya da sunuyu hafifçe hatırlatabilir. Bu yankı, buradaki ayrı verme eylemine bir yaklaşma imgesi ekler; ilişki yalnızca bu benzetme düzeyindedir ve alıcı yakın akraba olarak kalır.

Bu aile bağı, hemen önceki sözlerin bakım ve merhamet çizgisi içinde duyulur. (17:23, 17:24) önce Rabbin buyruğunu, ardından anne babaya iyiliği ve onları yetiştirdikleri gibi esirgeyip büyüten Rabbe yönelen duayı getirir: {ar:وَقَضَىٰ رَبُّكَ, tr:wa-qaḍā rabbuka, gloss:Rabbin hükmetti}, {ar:وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًا, tr:wa-bi-l-wālidayni iḥsānan, gloss:anne babaya iyilik} ve {ar:رَبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا, tr:rabbi irḥamhumā kamā rabbayānī ṣaghīran, gloss:Rabbim, beni küçükken yetiştirdikleri gibi onlara merhamet et}. (17:24) içindeki {ar:مِنَ ٱلرَّحْمَةِ, tr:mina al-raḥma, gloss:merhametle} sözü, ailevi merhameti rahim yakınlığıyla buluşturan bir bağlam yankısı kurar. Çocuğu büyüten ebeveynin daha sonra destek bekleyen muhatap oluşu, bugünkü hakkı geçmiş bakımla birlikte düşündürebilir; bu olası karşılık, işlemsel bir borç olarak kurulmaz. Benzer biçimde (4:36) ebeveyne iyiliği akraba, yoksul ve yolcuyla yan yana getirir, (2:215) ebeveynleri ve yakınları harcamaya katar, (59:7) ise servetin varlıklılar arasında birikmesine karşı dağıtım kurar. Bu örnekler akraba hakkını geniş aile desteği ve paylaşım düzenine taşır; ebeveynle çocuk arasındaki bakım yönünün değişmesi bağlamsal bir yankı olarak kalır.

İlk alıcının ardından gelen {ar:وَٱلْمِسْكِينَ, tr:wa-l-miskīna, gloss:ve yoksulu} yeni bir cümle ya da emir açmadan aynı diziye eklenir. Belirli tekil biçim tek bir kişiyi değil, tanınabilir bir ihtiyaç sahipleri sınıfını gösterir. Yeni bir {ar:ءَاتِ, tr:āti, gloss:verme buyruğu} söylenmez; fiil ile daha önce belirtilen {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hakkı} bu alıcı için de geri kazanılır. Ardından {ar:وَٱبْنَ ٱلسَّبِيلِ, tr:wa-ibna al-sabīl, gloss:ve yolcuyu} aynı yönetim alanına katılır. Hak her üç alıcıya taşınırken sıra, yakın ilişkiden geçim ihtiyacına ve yolculuğa doğru sorumluluk alanını genişletir; kimseyi ötekinden üstün tutmaz. Yoksul, ihtiyaçtan hareket halindeki yolcuya geçişin orta halkasıdır, bir hak derecesi değil.

{ar:ٱلْمِسْكِينَ, tr:al-miskīna, gloss:yoksul/muhtaç} burada geçim araçlarından yoksun kişidir. Kelime ailesindeki durma ve yerinde kalma yönü, ardından gelen yolcunun hareketiyle karşıtlık kurarak ihtiyaç ile hareket kısıtını duyurur; bu imge kişinin fiziksel olarak durduğunu söylemez. Ailenin ayrı bir kolu yaşamı sürdüren yiyecek ya da geçimliği, hatta sürüyü göçe çıkarmayacak bol otlağı anlatabilir. (2:215) yoksul ve yolcuya harcamayı, (59:7) dağıtımı öne çıkararak bu kolun geçimlik etkisini insan ihtiyacına taşır. Bu katkı odak sözcüğe “otlak” anlamı vermez ve yoksulun yerleşik olduğunu varsaymaz.

Son alıcı, bitişik vavla aynı emre eklenen tek bir mansup tamlamadır: {ar:ٱبْنَ, tr:ibna, gloss:çocuk/oğul} tamlamanın başı, belirli mecrur {ar:ٱلسَّبِيلِ, tr:al-sabīl, gloss:yol} ise onu tanımlayan tamamlayıcıdır. Yerleşik ifade gerçek bir yol kullanıcısını, üzerinde ilerlenebilen geçilebilir güzergâhtaki yolcuyu adlandırır; belirli tekil biçim tanınabilir bir yol kategorisi sunar. Buradaki yol somut rotadır; yolcu ifadesi doğrudan dinî güzergâh ya da soyut yöntem anlamına gelmez. “Çocuk/oğul” başı soy ilişkisini taşırken genitif “yol” kaynağı aile soyundan yolculuk aidiyetine kaydırabilir; başka kullanımlardaki “yolun çocuğu” imgesi bu aidiyeti derinleştirir. Bu yol aidiyeti mecazidir: soy ya da hukukî nesep, yolun bakım veren bir ebeveyn olduğu anlamına gelmez. Bir başka kullanım evinden uzakta ya da yolda çaresiz kalmış kişiyi düşündürebilir; bu ayette özel bir mahrumiyet veya gerçekten mahsur kalma belirtilmez. Yolcu listenin son alıcısıdır; bitişik bağlaçtan hemen sonra yasak başlar.

## Hedefli Veriş ve Savurma

Son alıcıyı izleyen {ar:وَلَا, tr:wa-lā, gloss:ve ...ma} yeni bir cümle molası vermeden nehyi başlatır. Aynı, kimliği belirtilmemiş ikinci tekil kişiye bu kez {ar:تُبَذِّرْ تَبْذِيرًا, tr:tubadhdhir tabdhīran, gloss:savurup ziyan etme} denir. Olumlu emir adı belli alıcıyı ve {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hakkı} gösterirken nehiy harcanan şeyi ya da varacağı yeri değil, savurganlık tarzını hedefler. İki fiil, hak sahibine teslim ile kaynakları savurma arasındaki karşıtlığı kurar; bu nehiy listedekiler dışındaki her harcamayı kapsamaz.

{ar:تُبَذِّرْ, tr:tubadhdhir, gloss:yersizce savur} Form II biçiminde savurganca harcamayı adlandırır ve açık bir nesne almaz. Nehiy edatı {ar:لَا, tr:lā, gloss:nehiy edatı} fiili cezmli kılar; ardından gelen aynı kökün belirsiz {ar:تَبْذِيرًا, tr:tabdhīran, gloss:savurma} mastarı mef'ûl-i mutlak olarak eylemi yineleyip pekiştirir. Bu yapı yasaklanan savurma örüntüsünü tek bir olaya kapatmaz; kapsamı savurgan harcamadır, bütün harcamalar değil. Kökün tohum saçma imgesi de ayrı bir kullanım olarak duyulur ve dağılma niteliğini ekler; tohum burada harcanan nesne değildir. Aynı kökün son sözcükte yinelenmesi 17:26 içinde işitsel ve konumsal bir kapanış kurar.

Sahibine bağlı {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hak/pay}, bu karşıtlıkta isteğe bağlı bir lütuftan çok önceden tanınmış, hesabı verilebilir bir pay gibi duyulur; bu yorum miktarı veya kapsamlı hukukî sonucunu belirlemez. Savurganca harcama ise kaynağı boşa çıkarıp işlevsiz bırakabilir. İhtiyatla atfedilen okumada yakın akrabalık aile bağını, “-hu” eki payın sahibini, yoksul maddi ihtiyacı, yolcu güzergâha bağlı muhataplığı sağlar; birlikte, kaynağın belirli hak sahiplerine yönelmesini açıklar. Savurma bu yönü saptırabilir. Yoksul için güçsüzlük ve ezilmişlik tonu mümkün bir çağrışım olarak kalır, ayrı bir sözlük anlamı değildir. Bu okuma alıcıları sıralamaz, sabit bir yüzde ya da biçimsel borç belgesi kurmaz ve tek bir hukukî dağıtım şeması dayatmaz.

## Akış ve Ekin

Alıcıya yönelen hak imgesi, sözcük ailelerinin ayrı kullanımlarıyla keşifsel bir dolaşım benzetmesine açılır. {ar:ءَاتِ, tr:āti, gloss:ver/ulaştır} burada olağan teslim fiilidir; aynı ailede başka bir kullanım, suyu kanalla araziye taşıyarak akışa yön verir. {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hak/pay} sahibine verilecek nesnedir; ayrı bir kullanımda kapı ayağının dönerek oturduğu yuva anlamı, alıcıya uyan payın karşılanma yerini düşündürür. Akış ve karşılanma yeri benzetmeye ayrı katkılar sunar; bu yan anlamlar odaktaki veriş ve hak anlamlarının yerini almaz.

Bu benzetmede {ar:ٱلْمِسْكِينَ, tr:al-miskīna, gloss:yoksul/muhtaç} kökün durma ve yerinde kalma yönüyle akışın durduğu noktayı, {ar:ٱبْنَ ٱلسَّبِيلِ, tr:ibna al-sabīl, gloss:yolcu} ise gerçek güzergâhta ilerleyen kişiyi temsil eder. {ar:ءَاتِ, tr:āti, gloss:ver/ulaştır} kaynakları taşıyan yönlü akışı; {ar:تُبَذِّرْ تَبْذِيرًا, tr:tubadhdhir tabdhīran, gloss:israfla saçıp savurma} içindeki tohum imgesi ise bu akıştan ayrılan yayılmayı getirir. Bir araya geldiklerinde, alıcıya ulaşan dolaşım ile güvenli varış noktası olmayan saçılma karşıtlaşır: ilki hakkın yönünü belirginleştirir, ikincisi bu yönü kaybettirebilir. Bu atfedilmiş benzetme, yoksulu gerçek bir kişi ve yolcuyu gerçek rota üzerindeki muhatap olarak bırakır; durma imgesi fiziksel hareketsizlik iddiası değildir.

Bahçe ve hasat, yönelmiş akışın üretken sonucunu ve savurmanın yıkıcı ucunu görünür kılar. (2:265) yağmurla beslenen bahçeyi, (6:141) ürünü ve hasat hakkına konan aşırılık sınırını, (3:117) ise ekini mahveden kırağılı rüzgârı sunar. Bu sahneler {ar:وَءَاتِ, tr:wa-āti, gloss:ver/ulaştır} için suyu yöneltme ve ürün verme dallarını, {ar:تَبْذِيرًا, tr:tabdhīran, gloss:tohum saçma} içinse saçılma imgesini etkinleştirir: amaçlı saçılan tohum ürün verebilir; hasat hakkı ve ölçüsü bu verimi gözetirken kırağılı rüzgâr ürünü yok eder. Böylece aynı tarımsal alan, yönlendirilmiş verim ile yıkıcı dağılmanın farklı sonuçlarını kurar. Bunlar ayrı kullanımlardan gelen benzetmelerdir; odaktaki fiiller olağan verme ve savurganca harcama anlamlarını korur, tarımsal mecazın kasıtlı olduğu ise kesinleşmez.

## Bağ, Uzaklık ve Gösteriş

(17:27) savurganları adlandıran {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīn, gloss:savurganlar} sözünü {ar:إِخْوَٰنَ ٱلشَّيَٰطِينِ, tr:ikhwāna al-shayāṭīn, gloss:şeytanların kardeşleri} nitelemesiyle birleştirerek eylemin yanına toplumsal aidiyeti ekler. Kardeşlik imgesi bağla birbirine tutturmayı taşır; böylece yakın akrabaya hakkı ulaştırmak toplumsal bağı sürdüren bir hareket, savurganlık ise bu bağı rakip bir aidiyete yöneltebilecek karşı hareket gibi duyulur. Aynı bağlamdaki {ar:ٱلشَّيْطَٰنُ, tr:al-shayṭān, gloss:şeytan} sosyal uzaklığı bu yakınlığın karşısına koyabilir. Bu, bağlamsal bir karşıtlıktır; sözün sözlük anlamını ya da her savurganın kimliğini tanımlamaz.

(17:27) sonundaki {ar:كَفُورًا, tr:kafūran, gloss:nankör}, olağan okuyuşta nankörlüğü, bu imgesel hatta ise nimeti örtmeyi getirir. Örtme, tohum saçılmasının ardından yararlı sonucu gizleyen ve bakım halkasını kesen bir evre gibi düşünülebilir; böylece verimli döngünün nasıl kırılabileceğini gösterir. Bu tarımsal katkı analojiktir; kafūr'un nankörlük anlamı yerinde kalır. Tohum ve örtme dağılımın sonucunu, kardeşlik ve uzaklık ise aktarımın toplumsal bağ üzerindeki etkisini açıklar.

(17:37) yer ve dağ imgeleri savurma okumasına bedensel bir ölçü ve kendini büyütme sahnesi ekler. {ar:مَرَحًا, tr:maraḥan, gloss:kibirli taşkınlık}, {ar:تَخْرِقَ ٱلْأَرْضَ, tr:takhriqa al-arḍ, gloss:yeri yarıp geçmek} ve {ar:تَبْلُغَ ٱلْجِبَالَ طُولًا, tr:tablugh al-jibāla ṭūlan, gloss:dağlara boyca erişmek} insanın yeri yarıp dağlara erişemeyeceği bir taşkınlık sahnesi kurar. Savurma yasağıyla kurulan bu bağlantı, aşırı harcamanın gösterişe ve başkalarını aşarak kendini büyütmeye dönüşebileceği ihtimalini açar. Bu olası saik 17:26'da belirtilmez; bağlantı savurma fiilinin sözlük tanımını değiştirmez.

## İlişkiyi Sürdürmek

(17:28) yüz çevirme koşulunu umulan Rab rahmetini arayışa bağlar: {ar:وَإِمَّا تُعْرِضَنَّ عَنْهُمُ, tr:wa-immā tuʿriḍanna ʿanhum, gloss:şayet onlardan yüz çevirirsen} ve {ar:ٱبْتِغَآءَ رَحْمَةٍ مِّن رَّبِّكَ تَرْجُوهَا, tr:ibtighāʾa raḥmatin min rabbika tarjūhā, gloss:umduğun Rabbin rahmetini ararken}. Ardından gelen {ar:فَقُل لَّهُمْ قَوْلًا مَّيْسُورًا, tr:fa-qul lahum qawlan maysūrā, gloss:onlara kolay ve gönül alıcı bir söz söyle} muhatapla bağı sürdüren bir edim sunar. İkincil okumada, eğer maddi aktarım o sırada mümkün değilse, bu kolay söz ilişkiyi taşır ve alıcının hakkı maddi görev olarak yerinde kalır. Ayet yüz çevirmenin nedenini ya da sonraki ödemeyi açıklamaz; maddi yetersizlik mümkün bir okuma, nezaket bildiren okuma da mümkündür.

(24:22) bu toplumsal bağı kırgınlık içinden sürdürür: imkân sahibi kişilere incinmiş olsalar bile yakınlarına ve yoksula yardımı kesmemeleri söylenir. Burada kaynak vardır, gerilim ilişkinin içindedir; (17:28) için olası görülen maddi yetersizlik ya da aktarımın aksamasından farklıdır. Yan yana okuma, sahibine bağlı {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hak/pay}ı hem imkânsızlık hem kırgınlık koşulunda duyurur, ama bu koşulları birleştirmez ya da biçimsel ertelenmiş borç kurmaz.

## Kapasite ve Rızık

(17:29) aktarım aracını, {ar:مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:maghlūlatan ilā ʿunuqika, gloss:boyna bağlanmış} el ile {ar:وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ, tr:wa-lā tabsuṭhā kulla al-basṭ, gloss:onu bütünüyle uzatma} arasında gerer. Verme aracı bir uçta donmuş gibi tutulur, ötekinde bütünüyle salınır; tam uzatmanın sonucu {ar:فَتَقْعُدَ مَلُومًا مَّحْسُورًا, tr:fa-taqʿuda malūman maḥsūrā, gloss:kınanmış ve tükenmiş kalman} diye, kınanma ve tükenme olarak verilir. Bu el imgesi harcamanın gelecekteki verme gücünü de etkileyebileceğini düşündürür. (17:30) rızkın genişleyip daralmasını anlatarak iki uç arasına değişken kapasiteyi ekler: ikincil okumada alıcıya veriş, sürdürme gücünü gözetir. Bu bağlamsal ölçü sayısal bir harcama kuralı değildir ve insanın dağıtımı ilahî rızık taksimiyle özdeşleştirmez.

Başka bağlamlar bu el geriliminin iki yanını ve amacını ayırt eder. (17:100) harcama korkusuyla elde tutuşu gösterir, fakat 17:26'daki alıcı listesini yinelemez; (30:39) kazanç için artış arayışını Allah'ın rızası için vermeden ayırır. (6:141) hasat hakkını aşırılık sınırıyla birlikte sunarak verimli akışa ölçü ekler. (5:64) Allah'ın iki elinin açık oluşu ve dilediğince harcamasıyla insanın kapasitesini aşan bir rızık düzenini görünür kılar. Bu imgeler hedefli teslimi korkuyla tutuş ve savurgan çıkış arasında konumlandırır; ilahî açıklık insana ölçüsüz verme buyruğu oluşturmaz.

(30:38) aynı üç alıcıya hak verme formülünü yineler ve bu maddi aktarımın amacına Allah'ın rızasını arama ile kurtuluşu ekler. (30:39) kazanç ile rıza için vermeyi ayırır, (5:64) ise insanın katıldığı daha geniş rızık düzenini gösterir; bu bağlantı insanı mutlak sahip değil sorumlu katılımcı olarak düşündürür. (17:29, 17:30) hakkındaki el ve kapasite okuması da insanın verme sorumluluğunu koruyarak bu katılımı ölçülü sürdürmeye açar; bu bağlamlar tek bir ekonomi öğretisi kurmaz ve rıza amacı her harcamayı ibadete dönüştürmez. (17:27) kardeşlik imgesi ise başka bir katkı sunar: harcamanın toplumsal aidiyetle ilişkisini gösterir.

## Hayat ve Emanet

Bu yoksulluk ve rızık bağlamları, muhtacın hakkını savunmasız yaşamı sürdürme ufkuna genişletir. (17:31) yoksulluk korkusuyla çocukları öldürmeme buyruğunu {ar:خَشْيَةَ إِمْلَاقٍ, tr:khashyata imlāq, gloss:yoksulluk korkusuyla} ve {ar:نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:narzuquhum wa-iyyākum, gloss:onlara da size de rızık veririz} güvencesiyle yan yana getirir; ardından {ar:وَلَا تَقْتُلُوا أَوْلَادَكُمْ, tr:wa-lā taqtulū awlādakum, gloss:çocuklarınızı öldürmeyin} ve {ar:إِنَّ قَتْلَهُمْ كَانَ خِطْـًٔا كَبِيرًا, tr:inna qatlahum kāna khiṭʾan kabīrā, gloss:onların öldürülmesi büyük bir suçtur} gelir. (6:151) de yoksullukta rızık vermeyi ebeveyne iyilik ve çocukların öldürülmesine karşı hayatı korumayla bir araya getirir. Bu bağlantı bağlamsal ufuktur; tek bir 17:26 aktarımının öldürmeyi önlediğini ileri sürmez.

(17:33) içindeki {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqq, gloss:hakka dayanarak} ve {ar:فَلَا يُسْرِفْ فِي ٱلْقَتْلِ, tr:fa-lā yusrif fī al-qatl, gloss:öldürmede haddi aşmasın} hakka dayanmayı aşmama sınırıyla birleştirir. Bu ölçü, kıtlık paniği ile aşırı karşılığı birlikte sınırlayan yaşamı koruyucu okumaya katkı sunar; odaktaki hak ve savurma yasağıyla kurulan bu bağ bağlamsal bir çıkarımdır. Böylece 17:26'nın kendi başına öldürme hükmü koymadığı ve sonraki hukukî buyruğun ayrı alanını koruduğu açık kalır.

(17:34) başka birinin malını koruma, ahdi yerine getirme ve ahitten hesap sorulacağını hatırlatma yoluyla mülkiyet ile süreklilik taşıyan yükümlülüğü somutlaştırır: {ar:مَالَ ٱلْيَتِيمِ, tr:māla al-yatīm, gloss:yetimin malı}, {ar:وَأَوْفُوا بِٱلْعَهْدِ, tr:wa-awfū bi-l-ʿahd, gloss:ahdi yerine getirin} ve {ar:إِنَّ ٱلْعَهْدَ كَانَ مَسْـُٔولًا, tr:inna al-ʿahda kāna masʾūlā, gloss:ahitten sorulacaktır}. Bu özel emanet, odaktaki sahibine bağlı {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:onun hakkı} ile buluşunca payın gerçek bir sahibi bulunduğunu belirginleştirir; alıcıların bütünü yetimle özdeşleşmez. (17:35) ölçüyü tam verme ve doğru tartma buyruklarıyla teslimin doğruluğuna ölçü standardı ekler: {ar:أَوْفُوا ٱلْكَيْلَ, tr:awfū al-kayl, gloss:ölçüyü tam verin} ve {ar:وَزِنُوا بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:wa-zinū bi-l-qisṭāsi al-mustaqīm, gloss:doğru teraziyle tartın}. (70:24) mal içindeki bilinen payı, (6:141) ise hasattaki hakkı ve aşırılık sınırını göstererek maddi hak fikrine iki ayrı ölçü alanı ekler. Bu örnekler 17:26'daki payı sahibine eksiksiz ulaştırılması gereken sorumluluk olarak aydınlatır; odak ayet miktar belirlemez, bu uygulamalar da onun doğrudan tanımı değildir.

## Yakınlık ve Yol

(17:32) yakınlık fikrini ilişki ile eylem sınırı arasında ayırır. Odaktaki {ar:ٱلْقُرْبَىٰ, tr:al-qurbā, gloss:yakın akrabalık} hak alıcısını soy bağıyla tanımlarken, {ar:وَلَا تَقْرَبُوا ٱلزِّنَىٰ, tr:wa-lā taqrabū al-zinā, gloss:zinaya yaklaşmayın} yasaklanan eyleme yaklaşmayı durdurur; ardından {ar:وَسَاءَ سَبِيلًا, tr:wa-sāʾa sabīlan, gloss:ne kötü bir yol} o eylemin yolunu kötü diye niteler. Böylece yakınlık birinde hak doğuran ilişkiyi, ötekinde sakınılacak eyleme doğru hareketi taşır; aynı yaklaşma alanı iki metinde farklı ahlaki yönler alır.

Bu karşılaştırma {ar:ٱبْنَ ٱلسَّبِيلِ, tr:ibna al-sabīl, gloss:yolcu}yi gerçek yol kullanıcısı olarak korur: (17:32) içindeki {ar:سَبِيلًا, tr:sabīlan, gloss:yol} kötü diye nitelenen güzergâhtır; yolcunun hakkı ise maddi desteğe ilişkindir. Fatiha'da topluluk (1:6) dosdoğru yola iletilmeyi, (1:7) nimet verilenlerin yolunu anar: {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} ve {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:ṣirāṭ al-ladhīna anʿamta ʿalayhim, gloss:nimet verdiklerinin yolu}. Odaktaki {ar:ٱلسَّبِيلِ, tr:al-sabīl, gloss:yol} ile Fatiha'daki {ar:ٱلصِّرَٰطَ, tr:al-ṣirāṭ, gloss:yol} ayrı sözcük ve köklerdir; ortak yol imgesi iki okuma arasında çağrışım kurar. Topluluğun yön bulma duası ile yol üzerindeki gerçek kişinin maddi ihtiyacı birlikte duyulur: dua edilen yön korunurken yolcu da desteğe hakkı olan somut muhatap olarak kalır.

</source_prose>
