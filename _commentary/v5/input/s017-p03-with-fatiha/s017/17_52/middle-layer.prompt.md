# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:52**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.middle.claims.json`

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
- Refer to source paragraphs as `17:52 ¶N`.

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

`(17:52 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:52",
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
        "citation": "(17:52 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_52/17_52.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_52/17_52.middle.claims.json \
  --ayah-ref 17:52
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_52/17_52.prose.editorial.tr.md`

<source_prose>
## Günün İçinde Çağrı

Ayet, daha bir fail ya da eylem anılmadan önce mansub zaman adı {ar:يَوْمَ, tr:yawma, gloss:gün} ile sahneyi açar. Bu, sıradan ve sınırları belli bir gündür; hemen ardından gelen {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} çağrısı ise onu dirilişin belirleyici vakti, hatta olayın kendisi olarak da duyurabilir. Günün yakın olabileceği haberi (17:51) ve kitapta yazılı kaydı (17:58) bu eşik niteliğini güçlendirir. Fâtiha'daki {ar:مَالِكِ يَوْمِ الدِّينِ, tr:māliki yawmi d-dīn, gloss:karşılık ve hesap gününün sahibi} adı karşılık ve hesap ufku ekler (1:4); böylece sıradan gün, kritik vakit ve hesap ufku birlikte duyulur, biri ötekini tek yoruma indirgemez. Ayetin sıralaması çağrıyı, cevabı, hamdi ve daha sonra kalışın geriye dönük tartılmasını aynı günün içine alır. Bu ortak çerçeve, olayın ya da hatırlanan kalışın ölçülebilir dış kronolojisini değil, çağrıdan geriye bakan zamanı belirginleştirir.

Bu günün içindeki eylem olağan bir sesli hitapla başlar: {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} fiilinin muzari biçimindeki -kum eki çağrılan çoğulu nesne yapar ve sesle sözü muhatabı konuşana yönelten bir çağrı kurar. Ardından gelen {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:böylece karşılık verirsiniz} içindeki {ar:تَسْتَجِيبُونَ, tr:tastajībūna, gloss:karşılık verirsiniz}, ikinci çoğul Form X cevap biçimidir. Bitişik fa, ayrı kalan iki faili tek yerel alışverişte buluşturur: çağrı cevabın bağımsız tetikleyicisi, cevap da o hitabın alımlanışıdır. Bu yakın bağ anlatımı araya durak koymadan ilerletir; yakınlık anlatım sırasındadır, ölçülebilir bir süreyi ya da bedensel yaklaşmayı belirlemez. Cevap fiilinde çağrıya uyma ve onu eylemle üstlenme nüansı da duyulabilir; muhataplar katılımcıya dönüşürken hangi eylemin istendiği ve sözlerin tam içeriği açık kalır. Çağrı yalın sesli hitaptır; özel bir yemek daveti ya da belirli bir yere yönelten kullanım bu ilişkiye eklenmez. Bu karşılığı verecek muhatapların kimliği, önceki diriliş itirazına dönmeyi gerektirir.

## Dağılmış Bedenden Görünür Mevcudiyete

Çağrının muhatabı olan bedenler, hemen önceki itirazda kemikler ve ufalanmış kalıntılara dönüşmüştür (17:49); taş, demir, hatta onlardan daha dirençli bir şeye dönüşme ihtimali dirilişi başka bir maddi sınamaya taşır (17:50). “Bizi kim geri getirecek?” sorusuna ilk kez yaratanın cevabı verilir (17:51): {ar:عِظَامًا وَرُفَاتًا, tr:ʿiẓāman wa-rufātan, gloss:kemikler ve ufalanmış kalıntılar}, {ar:مَن يُعِيدُنَا, tr:man yuʿīdunā, gloss:bizi kim geri getirecek} sorusunu ve {ar:فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:faṭarakum awwala marratin, gloss:sizi ilk kez yaratan} karşılığını bu tartışmaya bağlar. Odaktaki {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} ve {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:böylece karşılık verirsiniz} kalıntı olabilen bedenleri çağrıya cevap veren özneler olarak kurar. Cevap kökünün dağılmış şeyleri bir araya getirip elde etmeye ilişkin uzak sözlük kolu, kalıntıların ardından yanıt veren topluluğu yeniden birleşmiş gibi duyurur. Bu maddi benzetme odaktaki ikinci çoğul Form X'in olağan cevap anlamına eklenir; çağrı fiziksel bir toplama mekanizması olarak sunulmaz ve bedenlerin çağrıdan önceki bütünlüğü belirlenmez.

Yanıt verebilen bu özneler, önceki ayetlerin erişim güçlüğüyle yan yana gelince daha belirginleşir. Erişimi örten perde, kalbi kuşatan örtü ve kulaklardaki ağırlık ayrı ayrı anılır (17:45, 17:46). Hatırlatmaların çeşitlenmesi kaçışı artırır (17:41); Rab tek başına anıldığında muhataplar sırt çevirir (17:46), uyarının ardından haddi aşmaları büyür (17:60). Bu kapanma geçmişteki alımlanmayı, odaktaki {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:böylece karşılık verirsiniz} yanıtı ise değişen karşılığı gösterir; yanıt, engeller arasında açılan bir geçit gibi duyulur. Bu karşıtlık yanıtın etkisini belirginleştirir, fakat engellerin ne zaman ya da nasıl çözüldüğünü saptamaz. Olağan ve seçilmiş bir cevap mümkündür; engellerin önceden kalkmış olması, ikna, zorlama ya da diriliş sırasında önceden dönüşüm arasında tercih yaptıran bir ayrıntı verilmez. Bu aralık, cevap fiilinin uzak bir sözlük kolunun nasıl işitilebileceğini de belirler.

Çağrı ile cevap arasındaki boşluk ve önceki perde, örtü ve ağırlık, yanıtı aynı kökün biçimi ve geçişliliği ayrı olan {ar:الخَرْق والقطع النافذ, tr:al-kharq wa-l-qaṭʿ al-nāfidh, gloss:yarma ve geçerek kesme} kullanımıyla buluşturur; bu sözlük kolu bir nesneyi yarıp delerek açıklık açmayı anlatır ve {ar:جبت الشيء, tr:jabtu al-shayʾa, gloss:bir şeyi delip geçerek kestim} örneğiyle somutlaşır. Bu temas, {ar:تَسْتَجِيبُونَ, tr:tastajībūna, gloss:karşılık verirsiniz} cevabına sessizliği ya da mesafeyi aşma imgesi ekler: cevap, kapalı aralığı yararak içinden geçen bir karşılık gibi duyulur. Katkı imgeseldir; odak fiilin X. bâbdaki olağan anlamı yanıt vermek olarak kalır, bu bağlantı fiziksel kesik ya da yara bildirmez. Açıklığın mekânsal niteliğini şimdi başka sahnelerin ayrı katkıları belirginleştirir.

Yerin yarılması insanların hızla çıkışını ve toplanmanın kolaylaşmasını sahneye taşır (50:44); yeryüzüne dağıtılmış olanların O'na toplanması dağılmış topluluğu yeniden bir araya getirir (67:24). Kökün ayrı adı {ar:الجوبة, tr:al-jawbah, gloss:açılmış aralık ya da oyuk} ortası boş ya da açılmış alanı, aynı kökün bir yeri baştan başa aşmaya ilişkin başka bir kullanımı ise çağrıdan cevaba yönelen alışverişte ve {ar:يَوْمَ, tr:yawma, gloss:gün} çerçevesinde sınır geçişini öne çıkarır. Her bir imge ayrı bir iş görür: yarılma açıklığı, oyuk onun boşluğunu, dağılma ve toplanma ayrılığın aşılmasını duyurur. Bir araya geldiklerinde cevap, kapalı aralıktan görünür mevcudiyete geçen bir eşik gibi okunabilir. Bu bağın katkısı geçiş imgesidir; belirli bir güzergâhı, mesafeyi, varış yerini ya da dirilişin fiziksel işleyişini tarif etmez.

İşitenlerin cevap vermesinin hemen ardından ölülerin Allah tarafından diriltilip O'na döndürülmesi anılır (6:36). Bu yan yanalık, odaktaki cevabı işitilmiş çağrı, diriliş ve dönüş arasında okunur kılar; katkısı yakınlıktır, neden-sonuç ya da iki sahnenin aynı olay olduğu iddiası değil. Allah'a ve Elçi'ye cevap verme buyruğunun ardından insanın hayat verene çağrılması ve O'na toplanması gelir (8:24). Bu sıra, odaktaki {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} ile {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:böylece karşılık verirsiniz} arasındaki çağrı-cevap ufkuna hayat ve toplanmayı ekler. Bu paralel, iki çağrıyı özdeşleştirmeden ve 17:52'yi bugüne yönelik bir öğüde çevirmeden diriliş ufkunu genişletir.

Çağrının yönü, insanların daha önceki yakarışlarıyla karşılaştırıldığında tersine döner. Kendilerine yardım etmesini umdukları güçlere seslenen insanlar, onlardan zararı gidermelerini ya da kendi durumlarını değiştirmelerini sağlayamaz; çağrılanlar da Rablerine yakınlık arar (17:56, 17:57). Şimdi eski çağıranlar Allah'ın {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} hitabının muhatabıdır; {ar:تَسْتَجِيبُونَ, tr:tastajībūna, gloss:karşılık verirsiniz} cevabındaki {ar:بِحَمْدِهِۦ, tr:bi-ḥamdihī, gloss:O'na hamd ederek} çağıranla çağrılanın tersine dönen yönünü görünür kılar. Gerçek çağrının Allah'a ait oluşu ve O'ndan başkasına yakaranların ağızlarına ulaşmayan suya uzanmış eller gibi kalması aynı karşıtlığı başka bir imgeyle açar (13:14); insanların başkalarına seslendiği sahne de odakta Allah'ın insanları çağırmasıyla yüz yüze gelir (35:14). Fâtiha'nın {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīnu, gloss:yalnız sana kulluk eder ve yalnız senden yardım dileriz} doğrudan hitabı, insanın Allah'a yöneldiği bağımsız ve ters yöndeki karşılığı ekler (1:5). Bu karşılaştırmanın katkısı çağıranla çağrılanın rollerini ters çevirmesidir; aynı kişilerin konuştuğu ya da odaktaki sözlerin alıntılandığı buradan çıkmaz. Diriliş sahnesindeki olağan itaat okuması korunur; polemik yankısı duyulabilir ve başka bir sahneye geçiş olasılığı açık kalır.

Yüz çevirenlerin yine çağrılanlar arasında yer alması (70:17) ve herkesin Gün'ün Çağrıcısını izlemesi (20:108), odaktaki {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} hitabının önceden uzak duranlara da ulaşabileceğini düşündürür. Bu karşılaştırma aynı kişileri belirlemez ve cevabın zorlandığını göstermez. Ortak sayılanlara yöneltilen çağrının cevapsız kalması (18:52), insanların seslendiği varlıkların çağrıyı işitmemesi veya işitseler bile karşılık vermemesi (35:14), {ar:تَسْتَجِيبُونَ, tr:tastajībūna, gloss:karşılık verirsiniz} ile verilen yanıtın bu sahnelerden nasıl ayrıldığını gösterir. Sınır, anılan çağrı durumları arasındaki karşıtlıktır; buradan her yakarışın yanıtsız olduğu ya da odaktaki cevabın zorlandığı genellenmez.

## Hamdin Açtığı Yön

Yanıtı izleyen {ar:بِحَمْدِهِۦ, tr:bi-ḥamdihī, gloss:O'na hamd ederek} ifadesindeki bi, hamdi cevapla bağlar; bağlı zamir -hi övgüyü O'na yöneltir. Bi eşlik, sebep ya da araç ilişkilerinden birini kurabilir; ayet bunlar arasında seçim yaptırmaz. {ar:حَمْدِهِۦ, tr:ḥamdihī, gloss:O'na hamd} yermenin karşıtı olan övgüyü, iyilik karşısındaki teşekkürü de içine alacak biçimde taşır; hamd yalnız teşekkürden geniştir. Çokça övme ise ayrı bir türemiş biçime, {ar:تَحْمِيد, tr:taḥmīd, gloss:çokça övme} sözüne bağlıdır. Cevabın parçası olarak hamd, çağıranın övgüye değerliğini tanıyan sözlü bir karşılık gibi duyulabilir; hangi niteliğin övüldüğü ya da sözlerin tam biçimi belirtilmez. Uzun cevap vuruşundan sonra kısa hamd ifadesi sesli bir kapanış izlenimi yaratır: gırtlaksı sürtünme olan ḥ sesinden genizden gelen m'ye, oradan d'nin kapanışına uzanan akış, cevabın hamdde sıkışıp sona erdiği izlenimini verebilir. Bu, sesin işitsel katkısıdır; sözlük anlamını tek başına belirlemez.

Gökler, yer ve içindekilerin Allah'ı tesbih etmesi, insan cevabının katılabileceği daha geniş bir övgü alanı kurar; insanların bu tesbihi kavrayamadığı da belirtilir (17:44). Odaktaki {ar:بِحَمْدِهِۦ, tr:bi-ḥamdihī, gloss:O'na hamd ederek} kişisel hamd anlamını koruyarak insanın sesini süren övgüye katılma ihtimaline açar. Gök gürültüsünün O'nu hamdiyle tesbih etmesi ve meleklerin O'ndan haşyet içinde anılması bu yankıya iki belirgin yaratılmış örneği ekler (13:13); aynı ifade ölümsüz Diri'yi tesbih etme buyruğunda da iş görür (25:58). Bu ayetlerin katkısı insan cevabını yaratılmışların övgüsü içinde duyurmaktır; açıkça anılanlar gök gürültüsü ve meleklerdir, bu bağlantı bütün yaratılışın odaktaki çağrıya cevap verdiğini ya da odaktaki hamdin anlam değiştirdiğini söylemez. Fâtiha'nın {ar:الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ, tr:al-ḥamdu li-llāhi rabbi l-ʿālamīn, gloss:âlemlerin Rabbi Allah'a hamdolsun} formülü bu geniş övgü alanına insanın açıkça dile getirdiği bir ikrar ekler (1:2); çağrılanların aynı sözleri söylediğini değil, insanî hamdin sözlü biçimini gösterir.

## Kalışın Ölçüsü

Hamdin ardından gelen {ar:وَتَظُنُّونَ, tr:wa-taẓunnūna, gloss:ve sanırsınız}, sesli cevaptan kalışın iç değerlendirmesine geçer. Başındaki wa fa gibi zorunlu ardışıklık kurmaz: düşünme cevapla eşgüdümlü ikinci eylem ya da ona eşlik eden hâl olabilir. Fiile bitişikliği düşünceyi aynı sahnede tutar; iki eylemin eşzamanlı mı ardışık mı olduğu açık kalır. Bu çoğul fiil, arkasındaki kalış cümlesinin tümünü düşünce içeriği yapar; kısa süre anlatıcının dışarıdan verdiği ölçü değil, grubun değerlendirmesidir. Çağrıdaki -kum, cevap ve düşünmedeki -ūna, kalıştaki -tum aynı muhatap grubunu taşır: çağrılanlar cevap verir, kalır ve kalışlarını tartar. Şeddeli nûn düşünme vuruşunu işitsel olarak belirginleştirir, kanaatin kesinlik derecesini değil.

Bu düşüncenin içeriğini, {ar:إِنْ, tr:in, gloss:olumsuzluk edatı} ile başlayan ve {ar:لَبِثْتُمْ, tr:labithtum, gloss:kaldınız} fiiline bağlanan kısıtlama oluşturur. Edat koşul değil olumsuzluk kurar; nûn sesi fiilin başındaki lâmda birleşerek kısıtlamayı duyurur, kalma anlamını değiştirmez. Ardından gelen {ar:إِلَّا, tr:illā, gloss:ancak / müstesna} olumsuzluğu tamamlar; cümlenin sonunda duran {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} kalış süresini niteler. Sözcüklerin sırası daralmayı adım adım kurar: olumsuzluk açar, istisna sınırlar, mansub ve belirsiz son ölçü süreyi nitelikçe az gösterir. Böylece kalış zamanı kısıtlanır, fakat sayı ya da karşılaştırma verilmez.

Tamamlanmış biçimdeki {ar:لَبِثْتُمْ, tr:labithtum, gloss:kaldınız}, diriliş sahnesinin geleceğinden bakıldığında geçmişte sürmüş bir kalışı geriye yerleştirir. Fiilin olağan anlamı bir yerde bulunmayı sürdürmektir; duraksamak ya da yavaş davranmak değildir. {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} bu kalışın zaman boyutunu ölçerek onu içinden geçilmiş ve sonradan tartılabilir bir aralık gibi duyurur. Bu okuma sürenin yerini, nesnel uzunluğunu ya da yaşanma biçimini belirlemez; fiil kalışın istekle mi edilgen biçimde mi sürdüğünü de seçmez. Acı, isteksiz gecikme veya amaçlı ikamet eklenmez. Azlık sözü süre bakımından gerçek bir kısalığı bildirirken {ar:وَتَظُنُّونَ, tr:wa-taẓunnūna, gloss:ve sanırsınız} grubun gözünde az sayılan zamanı da duyurabilir. Bu bakış kalışı değersizleştirmez; nesnel kısalıkla sonradan az görünmesi arasındaki ağırlık açık kalır.

Bu açık kalan ağırlık, {ar:وَتَظُنُّونَ, tr:wa-taẓunnūna, gloss:ve sanırsınız} fiilinin özel bir kalıp şartına bağlı olmayan anlam alanında da görünür: bir belirtiyle güçlenip bilgi düzeyine varan inanıştan kesinleşmemiş tahmine kadar uzanır. Aynı gündeki {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} çağrısı, {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:böylece karşılık verirsiniz} cevabı ve {ar:بِحَمْدِهِۦ, tr:bi-ḥamdihī, gloss:O'na hamd ederek} hamdi bu azlık yargısına belirti gibi ağırlık vererek güçlü kanaat okumasını mümkün kılabilir; ayet bu karşılaşmayı açıkça belirti diye adlandırmaz ve kalış süresini doğrulanmış bilgi yapmaz. Kalış süresi sorulur (23:112), bir gün ya da günün bir parçası diye yanıtlanır (23:113), sonra ancak az kalındığı “bilseydiniz” kaydıyla söylenir (23:114). Bu değişen kısa tahminler, aynı fiilin kesinleşmemiş sanı anlamını da korur; güçlü kanaat ve belirsiz tahmin aynı yargıda birlikte bulunur, biri ötekine üstün tutulmaz. Olay görüldüğünde kalışın bir akşam ya da sabah kadar görünmesi de geriye dönük kısalmayı belirginleştirir (79:46); bu imge takvim miktarını hesaplamaz.

Farklı çağrı ve toplanma sahneleri odaktaki cevaba ayrı katkılar sunar: herkesin Gün'ün Çağrıcısını izlemesi yönelişi belirginleştirir (20:108), yeryüzüne dağıtılanların O'na toplanması grubun yeniden birleşmesini gösterir (67:24), yarılan yerden insanların hızla çıkması ve toplanmanın kolaylaşması görünür çıkış sahnesi açar (50:44). Bu paralellikler çağrı-cevap okumasını genişletir; doğrudan alıntı ya da metinler arası bağımlılık ileri sürmez ve izlemeyi çağırma fiilinin sözlük anlamı yapmaz. Kalışa ilişkin soru (23:112), bir gün ya da günün parçası diye verilen tahmin (23:113), ancak az kalındığına ve “bilseydiniz” kaydına varan ölçü (23:114), ardından akşam ya da sabah kadar görünen süre (79:46), önceki aralığın geriye bakışta daralmasını kurar. Bu zaman hareketiyle çağrı çevresinde yönelme, yeniden birleşme ve görünür çıkış imgeleri yan yana geldiğinde odak, bedenlerin diriltilmesi anlamını koruyarak cevap veren ve geçmiş kalışını kısa gören topluluğa doğru genişler. İlk kez yaratanı hatırlatan geri getirilme cevabı, böylece yaklaşan Gün'de çağrı, yanıt ve hamd ile görünür olan bir ilişki kazanır. Bu birleştirme çağrıyı dirilişin nedeni yapmaz; olayların sırası, kalışın yeri ve nesnel süresi, yanıtın gönüllülüğü de bu karşılaştırmayla belirlenmez. Bu sınırlar yalnızca burada kurulan bağlantının kapsamını gösterir; ayetin bedensel diriliş anlamını ya da başka kalış süreleriyle ilgili okumaları geçersiz kılmaz. Ayetin sonundaki {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} kulağı baştaki {ar:يَوْمَ, tr:yawma, gloss:gün} sözüne döndürür: hatırlanan kalışın kısalığı çağrının geldiği günün çerçevesinde son iz olur, dış kronoloji yine ölçülemez. Bu çerçevede son ölçü sözcüğünün uzak sözlük yankıları, kalış ile kalkış arasındaki imge gerilimini açar.

Azlık sözcüğünün bağlı olduğu {ar:ق ل ل, tr:q-l-l, gloss:azlık kökü} için uzak bir sözlük kolu, bir nesneyi kaldırmaya güç yetirmeyi, onu taşıyıp yük olarak üstlenmeyi anlatır; genişleyen imgesi aşağıdan yukarı yükselmeye, harekete geçmeye ve hatta uçuşa başlamaya uzanır. Diriliş ve ayağa kalkış kalışın karşısında durduğunda bu kol, kısa aralığın yük gibi taşınıp yükselişe varması yankısını doğurabilir. Kökün bağımsız başka bir kolu, bulunduğu yerde sabit kalmayıp sallanan ya da düzensiz hareket eden şeyi anlatır; {ar:لَبِثْتُمْ, tr:labithtum, gloss:kaldınız} ile kurulan sürüp kalış, diriliş ve kalkış karşısında yerinden çözülme imgesiyle temas eder. İlk kol aralığı taşıyıp yükselişe yöneltirken ikincisi kalışın kararlılığını gevşetir; bunlar ayrı ve keşif niteliğinde sözlük yankılarıdır, maddi yükü, sarsıntıyı ya da fiilî hareketi bildirmez. Odaktaki {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} yine ölçü bakımından az bir kalıştır.

</source_prose>
