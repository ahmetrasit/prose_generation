# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:8**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.middle.claims.json`

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
- Refer to source paragraphs as `17:8 ¶N`.

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

`(17:8 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:8",
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
        "citation": "(17:8 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_8/17_8.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_8/17_8.middle.claims.json \
  --ayah-ref 17:8
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_8/17_8.prose.editorial.tr.md`

<source_prose>
17:8, {ar:عَسَىٰ رَبُّكُمْ أَنْ يَرْحَمَكُمْ, tr:ʿasā rabbukum an yarḥamakum, gloss:umulur ki Rabbiniz size merhamet eder} sözüyle merhameti gerçekleşmiş bir sonuç olarak değil, açık bir umut olarak sunar. Hemen ardından {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:eğer dönerseniz biz de döneriz} şartı gelir; son bağ ise {ar:وَجَعَلْنَا جَهَنَّمَ لِلْكَٰفِرِينَ حَصِيرًا, tr:wa-jaʿalnā Jahannam li-l-kāfirīna ḥaṣīran, gloss:Cehennem'i inkâr edenler için hapseden bir yer kıldık} diye tamamlanır. Böylece umut, mümkün bir insan dönüşü ve ona verilen ilahî yanıtın ardından, kime yöneldiği ayrıca belirtilen tamamlanmış bir atama duyulur.

Başlangıçtaki {ar:عَسَىٰ, tr:ʿasā, gloss:umulur ki} umut ve beklenti fiilidir; ardından gelen {ar:أَنْ, tr:an, gloss:-mesi} maṣdariyye parçacığı bu umudun içeriğini {ar:يَرْحَمَكُمْ, tr:yarḥamakum, gloss:size merhamet etmesi} eylemiyle tamamlar ve muzari fiili mansub kılar. Bu yapı merhameti amaç ya da sonuç olarak değil, umudun içerik tamamlayıcısı olan eylem olarak sunar. İlâhî hitabın bu umuda verdiği kesinlik değeri ayrıca belirlenmez; merhamet açık ihtimal olarak kalır. I. bâbdaki yarḥamakum doğrudan merhamet eylemini muhataplara yöneltir; merhamet ailesinin yakınlık, esirgeme ve koruyucu iyilik tonları bu yönelişte duyulur.

Umudun açık öznesi {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} unvanıdır. Rabbukum içindeki -kum aynı toplulukla ilişkiyi kurarken, yarḥamakum sonundaki -kum onları eylemin nesnesi, yani merhametin alıcısı yapar; biraz sonra {ar:عُدتُّمْ, tr:ʿudtum, gloss:dönerseniz} içindeki -tum ise aynı topluluğu şartlı dönüşün faili kılar. Böylece dilbilgisel ilişki, Rab ile muhataplar arasında bakım ve yönelişten onların eyleyiciliğine doğru değişir. Rabb bir isimdir; kelime ailesindeki eksik olanı gözetip düzeltme, aşama aşama tamamlanmaya götürme kullanımı, umut ile merhametin yanında bu unvana bakım ve onarım tonu verir. Bu bakım tonu unvanın isim niteliği içinde kalır; merhametin gerçekleşme derecesi ise açık bırakılır.

Merhametten dönüş şartına geçen tek harflik {ar:وَ, tr:wa, gloss:ve} bağlayıcısı, açık {ar:إِنْ, tr:in, gloss:eğer} koşuluyla önceki umudu aynı söyleyiş içinde tutar. In, “ne zaman” diyerek zaman belirlemek yerine mümkün bir durumu açar; tek koşul hem muhatapların dönüşünü hem de karşılık olan ilahî dönüşü yönetir. Uzun ā taşıyan {ar:عَسَىٰ, tr:ʿasā, gloss:umut fiili}, kısa ve birbirine sesçe yaklaşan {ar:عُدتُّمْ, tr:ʿudtum, gloss:dönerseniz} ile {ar:عُدْنَا, tr:ʿudnā, gloss:biz de döneriz} biçimlerinden önce işitsel bir alan açar. Bu süre farkı ayetin kendi ritmine katkı verir; önceki ayetlerde bağımsız bir tekrar örüntüsü iddiası taşımaz.

{ar:عُدتُّمْ, tr:ʿudtum, gloss:dönerseniz} biçimi mâzî görünüşlüdür; açık in koşulunda ise geçmişte tamamlanmış olay değil, mümkün bir gelecek dönüşü bildirir. İkinci çoğul eki muhatapları bu hareketin faili yapar. Nesne ve hedef verilmediğinden dönüşün konusu açık kalır; cümle bu boşluğu belirli bir günah, terk edilmiş yol, söylenmemiş söz ya da fiziksel yolculukla doldurmaz. Karşılık olan {ar:عُدْنَا, tr:ʿudnā, gloss:biz de döneriz} aynı dönme eylemini başka bir özneyle yineler; ilahî birinci çoğul fail, ayrı bir adla değil -nā ekiyle fiilin içindedir. İki biçim birlikte koşullu, karşılıklı bir yanıt kurar. Bu bağlamda çiftin taşıdığı eylem karşılıklı dönüştür; sayma ya da hazırlama ayrı sözlük anlamları bu okumayı yönetmez.

İkinci {ar:وَ, tr:wa, gloss:ve} bağlayıcısı, {ar:جَعَلْنَا, tr:jaʿalnā, gloss:kıldık, atadık} ile gelen son bildirimin dönüş yanıtına eklenmesine de kısa koşuldan sonra yeni bir cümle olarak başlamasına da izin verir. Her iki çözümlemede jaʿalnā birinci çoğul fail ekli mâzî biçimiyle tamamlanmış ilahî atamayı bildirir: mevcut bir nesneye rol verir, yani yaratılıştan çok konumlandırma ve atama ilişkisini öne çıkarır. Ayetin üç vuruşu böylece umut edilen merhamet, koşullu insan ve ilahî dönüş çifti, tamamlanmış atama olarak duyulur.

Atamanın ilk nesnesi {ar:جَهَنَّمَ, tr:Jahannam, gloss:Cehennem} özel adıdır. Yabancı kökenli ve gayr-i munsarif bu adın olağan tenvin almaması da özel ad yapısıyla uyumludur: belirsiz bir ceza türünü değil, fiilin ilk nesnesi olan Cehennem'i gösterir. {ar:حَصِيرًا, tr:ḥaṣīran, gloss:hapseden nitelik} bu adın ikinci tamamlayıcısıdır; yakın bir hâl çözümlemesi de açık kalır. Belirsiz mansub biçim ayeti yeni bir nesneyle değil, atanan yerin niteliğiyle kapatır. Jahannam adında duyulabilecek derinlik ya da uçurum çağrışımı, yanındaki ḥaṣīran'ın mekânsal katkısıyla sınırlı bir yankı kazanır; özel adın yerini alan bir çeviri olmaz. Jaʿalnā ile Jahannam başındaki “ja” sesi eylemle nesneyi işitmede birbirine bağlar; bu yakınlık ses düzeyindeki katkıdır, tek başına etimolojik ya da dilbilgisel kanıt oluşturmaz.

Son tamlamadaki {ar:لِلْكَٰفِرِينَ, tr:li-l-kāfirīn, gloss:inkâr edenler için} başındaki tahsis lâmıyla atamanın alıcı sınıfını belirtir; fiilin doğrudan nesnesi olmaz. Belirli eril çoğul etkin ortaç olan {ar:كَٰفِرِينَ, tr:kāfirīn, gloss:inkâr edenler} olağan anlamıyla inkâr edenleri adlandırır ve ikinci çoğul hitaptan belirli bir insan sınıfına geçişi sağlar. Ortaç biçiminin örtme anlamı kuşatma ve örülme imgeleriyle karşılaştığında, alıcıları ayrıca “örtücüler” olarak duyurur; böylece bu imge atanan kapalı sonuca örtme ilişkisini eklerken olağan sınıf adını korur.

## Tekrarın Açtığı Zaman

Bu dönüş çiftinin arkasındaki tarihsel örüntü, önceki ayetlerde ayrı aşamalarla kurulmuştur: iki bozulma ve büyüklenme haberi (17:4), ilk saldırı ve cezanın uygulanması (17:5), ardından güç, mal, çocuk ve sayıca artışın geri verilmesi (17:6), son olarak yapılan iyilik ya da kötülüğün yapanlara dönmesi ve mescide ikinci giriş (17:7). Bu sıra, {ar:عُدتُّمْ, tr:ʿudtum, gloss:dönüşünüz} ile {ar:عُدْنَا, tr:ʿudnā, gloss:bizim dönüşümüz} biçimlerini tek bir geri dönüşten ibaret bırakmaz: tekrarlanan davranış, sonucu, aradaki imkânların iadesi ve eylemin yapanlara dönüşü aynı tarihin farklı basamakları olur. Böylece bu tarihsel örüntü 17:8'deki Cehennem atamasını yinelenen gidişin sonuçlu ucuna bağlar; bağlantı önceki grubu son alıcı sınıfla özdeşleştirmez.

Karşılıklı dönüşün başka kullanımlardaki yankıları da ayrı sahnelerden gelir. Azabın kısa süre kaldırılmasından sonra “yeniden döneceksiniz” denmesi bu hareketi süreli bir kesintinin ardından açar (44:15); vazgeçme seçeneğinden sonra “dönerseniz biz de döneriz” yanıtı koşullu karşılıklılığı öne çıkarır (8:19). Yasaklandıkları şeye geri dönme, dönüşün nüks olasılığını belirginleştirir (6:28). Bu sahneler 17:8'deki koşullu yanıta kendi bağlamlarından yankı verir; ilişki doğrudan alıntı ya da zorunlu kaynak değil, ortak bir tekrar biçimidir. Nüks bu nedenle mümkün okumalardan biridir; dönüşün kaçınılmaz sonucu olarak sunulmaz.

Dönüş kökünün ayrı bir kullanımında eylemi yinelemek onu kolay ve yerleşik bir davranışa çevirebilir; bir başka süreç kullanımıysa tekrarla alışma, alıştırma ve yeterlik kazanmayı anlatır. Açık {ar:إِنْ, tr:in, gloss:eğer} koşulu, merhamet umudu ve ʿudtum-ʿudnā çiftiyle karşılaşınca bu uzantılar kesilip yeniden başlayabilen bir pratiği düşündürür: dönüş alışkanlığa yaklaşabilir ya da yeniden başlayan bir yeterlik sürecine açılabilir. Bu pratik imgesi sabit bir yatkınlık yüklemez ve her dönüşü nüks saymaz. Dönüş çiftinin bağımsız biçimde tetiklediği Rabb ailesindeki “bir yerde kalma, ayrılmama” kullanımı da gözetimin yinelenen insan dönemleri boyunca sürmesi yankısını verir; bu sözlük yankısı bir yerleşim iddiası değil, kesintiler boyunca gözetim sürekliliğidir.

İnsan davranışı ile {ar:عُدْنَا, tr:ʿudnā, gloss:biz de döneriz} biçimindeki ilahî yanıtın yan yana gelişi, sürmekte olan gidişe karşılık veren bir ilişki olarak okunabilir. Fiilin ilahî faili, bu karşılığı insanın kendi kendine ürettiği geri bildirimle sınırlamaz; insan davranışından bağımsız egemen bir yeniden ceza ihtimali de bu ilişkinin yanında açık kalır. Böylece bağlantı hem insan dönüşüyle ilişkili karşılığı hem ilahî eyleyiciliği taşır, fakat dönüşün hedefiyle yanıtın nasıl bağlandığını tayin etmez.

## Kuşatan Yer

{ar:حَصِيرًا, tr:ḥaṣīran, gloss:hapseden nitelik} önce dışarıdan uygulanan bir gücün kişiyi tutup serbest hareketini engellemesini, ayrıca mekânın çevreyi sararak alanı daraltmasını anlatan kullanımlara açılır. Odakta bu işlemler {ar:جَعَلْنَا, tr:jaʿalnā, gloss:atama fiili} ile adlandırılan {ar:جَهَنَّمَ, tr:Jahannam, gloss:Cehennem} ve {ar:كَٰفِرِينَ, tr:kāfirīn, gloss:inkâr edenler} arasında kurulur: atanan yer alıcıları tutar, çevrelerini sarar ve hareket alanlarını sınırlar. Cehennem'in inkâr edenleri kuşattığının söylenmesi bu mekânsal işlemin açık bir karşılığıdır (29:54). Bu bağlantıda kuşatma, yer ile alıcı sınıfın temasından doğan hareketi daraltan kapalı alan imgesidir; askerî kuşatma sahnesi olarak değil, çevreyi daraltan mekânsal işleviyle okunur.

Aynı kelimenin ayrı isim kullanımı, kamış ya da benzeri bitki parçalarının sıkıca örülmesiyle yapılan düz yaygıdır. Bu dalda ayrı parçaların birbirine geçirilmesi, tek ve sıkı bir yüzey oluşturur. Örtme çağrışımı taşıyan {ar:كَٰفِرِينَ, tr:kāfirīn, gloss:örtücüler} bu yüzeye kapalılık verir; {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir nitelik olarak atadık} ise niteliğin atama içindeki yerini kurar. Önceki dizide yinelenen eylemler, bu ayrı örülme imgesinde yüzeye katılan parçalar gibi düşünülebilir (17:4, 17:7). Cehennem'in döşek, üzerindekilerin örtüler diye anılması bu görüntüye yataklık ve örtülme yakınlığı ekler (7:41). Bu yakınlık sözcükleri ḥaṣīran ile eş anlamlı yapmaz; saz ya da hasır malzemesi de 17:8'de atanan yerin gerçek maddesi olarak ileri sürülmez.

Örülmüş yüzeyden ayrı olarak, ḥaṣīran'ın bir başka kullanımı içeridekini tutan ve çıkışına izin vermeyen kapalı yerdir. Cehennem'in bu niteliğin atandığı yer olması, alıcı sınıfla birlikte onu cezalandırıcı bir meskene dönüştürür. Ateşi görünce suçluların oraya düşeceklerini sezmesi ve ondan kaçacak yol bulamaması çıkışsızlığı somutlaştırır (18:53); Cehennem'in onların barınağı sayılması ve ateş her yatıştığında alevin artırılması, aynı kapalı yerde yinelenen cezayı duyurur (17:97). Burada ateşin yeniden alevlenmesi içeride kalmayı yinelenen bir deneyim olarak biçimlendirir; 17:8'in kendi ifadesi bu deneyimin süresini belirtmez.

Bu mesken imgesinin etkisi başka ayetlerde bedensel ve toplumsal ölçeğe de taşınır: Cehennem'in hemen elde edileni isteyen kişi için hazırlanması, ateşin yakması, kınanma ve uzaklaştırılma ile birlikte verilir (17:18). Kınanmış ve desteksiz biçimde oturmak ise ayrı bir sahnede hareketsizlik ve ilişkisizliği öne çıkarır (17:22). Bu tasvirler 17:8'deki atamaya bedensel maruz kalma ve ilişkisel dışlanma boyutları ekler; 17:8 bu ayrı görüntüleri tek bir kronolojik ceza dizisi olarak sıralamaz.

Kapalı yerde tutulan sakinler, ḥaṣīran ailesinin konuşmaya ilişkin ayrı fiil biçimine geçişi anlaşılır kılar: {ar:حَصَرَ الرَّجُلُ فِي كَلَامِهِ, tr:ḥaṣara r-rajulu fī kalāmihi, gloss:adam konuşurken dili tutuldu} kişi konuşurken, hitap ederken ya da okurken söz üretemez hâle gelmesini anlatır. Fiil, sözün kullanımı sırasında beliren bir engeli gösterir ve ayetteki ḥaṣīran isim biçiminden ayrılır; bu özel bağlantıda konuşma engeli imgesi doğuştan dilsizlikten ya da isteyerek susmaktan farklıdır. Cehennem sakinlerinin kör, dilsiz ve sağır diye nitelenmesi ile aynı yerin onların barınağı olması, konuşma engelini mekândan sakinlerine taşıyan sınırlı bir benzetme kurar (17:97). Bu aktarım çıkışsızlığa iletişimin kesilmesini ekler; isim ile fiilin sözlük anlamları yine ayrı kalır.

## Merhamet ve Yeniden Bağ

Sakinleri içeride tutan yerden bakış, ayetin başındaki merhamet eyleminin açtığı başka bir iç ve bağ ufkuna geçer. {ar:يَرْحَمَكُمْ, tr:yarḥamakum, gloss:size merhamet etmesi} muhataplara yönelen esirgeme ve iyilik eylemi olarak kalırken, aynı kelime ailesinin ayrı isim kullanımı {ar:رَحِم, tr:raḥim, gloss:akrabalık bağı} ortak soydan gelenler arasındaki kalıcı yakınlığı adlandırır. Nuh'la taşınan soy anlatısı ve Rabb unvanının gözeten ilişkisi bu akrabalık dalını harekete geçirir (17:3). Kapalı mekânın karşısında bu bağ, kesintiye uğrayan ilişkilerin yeniden kurulabileceği bir ufuk açar; yüz çevirme, yeryüzünde bozgunculuk ve akrabalık bağlarını kesmenin aynı uyarıda buluşması bu ilişkisel ufku genişletir (47:22). Bu bağlantı akrabalığı merhamet eyleminin şartı değil, onun yanında açılan ayrı bir ilişki çağrışımı olarak tutar.

Aynı {ar:رَحِم, tr:raḥim, gloss:döl yatağı} adının ayrı anlamı, yavrunun oluşup geliştiği ve doğuma dek taşındığı iç mekândır. Bu anlamı çağıran taşıyıcı, isim değil merhamet eylemini bildiren {ar:يَرْحَمَكُمْ, tr:yarḥamakum, gloss:size merhamet etmesi} fiilidir; Rabb'in gözetip yetiştirmesi ve ḥaṣīran'ın kapalı içi bu çağrışımı besler. Böylece merhamet hayatı içeride taşıyıp geliştiren bakım gibi duyulur; kapanıştaki yer ise hareketi durdurup çıkışı keser. İki iç mekânın katkıları karşıt kalır: biri oluş ve taşımayı, diğeri hapsi ve hareket kısıtını öne çıkarır.

Bu bakım ufku önceki ayetlerdeki tarihsel ayrıntılarla zaman içinde genişler. Çevresi bereketlendirilen yer, merhamet ve gözetimle birlikte süreklilik taşıyan bir iyilik ortamı düşündürür (17:1). Nuh'la taşınan soy ve şükreden niteliği bakımın kuşaklar arası ufkunu açar (17:3). Yenilgi sonrasında imkânların, malın ve çocukların geri verilmesi ve topluluğun sayıca artması somut bir ara onarımı gösterir (17:6). {ar:رَبُّكُمْ, tr:rabbukum, gloss:Rabbiniz} ailesinin eksikten gelişmeye ve artışa uzanan ayrı kullanımı 17:6'daki açık çoğalma ile tetiklenir; unvan isim olarak kalırken merhamet ve dönüş, yeniden gelişebilecek bir çizgi içinde işitilir. Bu bağlantı kalıcı onarımı mümkün bir ufuk olarak taşır. Ufkun sınırı da belirgindir: 17:1'in gece yolculuğu ve çevrelenmiş mekânları dönüş döngüsünü açıklamaz, 17:3'teki şükür kendi niteliği olarak kalır, 17:6'daki artış ise kuşaklar arası nedensellik ya da önceki alıcılarla 17:8'deki sınıf arasında özdeşlik kurmaz.

Umut bildiren {ar:عَسَىٰ, tr:ʿasā, gloss:umulur ki} biçimine ses ve yazılışça yaklaşan, fakat ayrı sözlük biçimleri olan {ar:المعسية, tr:al-maʿsiyya, gloss:sütü belirsiz dişi deve} ile {ar:المعسيات, tr:al-maʿsiyāt, gloss:sütü belirsiz dişi develer} adları başka bir yenilenme imgesi açar. Bu adlar sütü kesilmiş ya da süt durumu belirsiz dişi develeri anlatır; sözlük açıklaması, sütü durmuş develerde sütün yeniden gelebileceği umudunu da kaydeder. Ayrı deve adları ʿasā fiilinin anlamını değiştirmez; ses ve biçim yakınlığı yalnız bu bağlantının taşıyıcısıdır. ʿudtum-ʿudnā dönüş çifti ise kesintiden sonra yeniden süt gelmesini merhametin onarıcı ve besleyici ihtimaline benzetmeye imkân verir. Bereketlenen çevre yerleşik bir deveden sağlanan sütü çağrıştırabilir (17:1); Nuh soyunun taşınmasını bildiren {ar:حَمَلْنَا, tr:ḥamalnā, gloss:taşıdık} içte taşıma ve meyve verme yankısı, {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} ise uzaktan doluluk ve süt bolluğu yakınlığı ekler (17:3). Bu unsurlar keşifsel bir beslenme benzetmesi kurar: 17:1 ve 17:3 imgeye renk verir, tarihsel dönüş döngüsünü açıklamaz; 17:8 de gerçek bir deve ya da anatomi sahnesi ileri sürmez.

Merhamet ihtimali için uygulanabilir bir yön, içten tövbe çağrısının ardından aynı {ar:عَسَىٰ رَبُّكُمْ أَنْ, tr:ʿasā rabbukum an, gloss:umulur ki Rabbiniz} kuruluşuyla bağışlanma ve cennet umudunun açıldığı başka bir ayette belirir (66:8). Bu komşu kullanım 17:8'deki dönüşe onarıma yönelen pratik bir istikamet kazandırır. Bu bağlantı tövbe çağrısını 17:8'in belirtilmiş şartı hâline getirmez; merhamet de açık umut olarak kalır.

Onarım yönünün nasıl bir hareket olabileceği, hemen sonraki ayette daha açık bir yol hâline gelir: Kur'an en doğru olana yöneltir, inananlar iyi işler yapar ve büyük ödül alır (17:9). Bu güzergâh dönüşü eski davranışa nüks yanında daha doğru olana yönelen değişmiş bir hareket olarak da duyurur. Ahirete inanmayanlar için hazırlanmış acı azap bu yönelimin karşı kutbunu kurar (17:10). Bu komşu çerçeve 17:8'in merhamet ve dönüşünü onarıcı bir yol içinde okumaya yardım eder; belirli muhatapların seçimini ya da sonunu tayin etmez.

Dönüşün yönü kadar zamanı da önem kazanır. İnsan kötülüğü, iyiliği ister gibi ister ve acele eder; gece işaretinin silinip gündüzün görünür kılınması yılları sayılabilir hâle getirir ve her şeyin ayrıntılandırılmasını sağlar (17:11, 17:12). Bu zaman karşıtlığı, 17:8'deki dönüş çiftine aralıkları ve sonuçları ayırt eden ölçülü bir karşılık ufku katar. Bu, ayete bir takvim ya da süre ekleyen bir okuma değil, bağlamsal zaman benzetmesidir: 17:8 gecikmeyi belirtmez ve ʿudtum ile ʿudnā olağan dönüş anlamını korur.

Gruba yönelen tarihsel dönüş, her kişinin kendi hesabını taşıdığı bir ölçeğe de açılır. Kişinin kaydının boynuna bağlanması ve kitabının açılması, hesabı doğrudan sahibine iliştirir (17:13); kişiye kitabını okuyup kendi hesabını görmesi söylenir (17:14). Bu çerçevede yenilenen gidişin taşıyanına görünür olması ve {ar:حَصِيرًا, tr:ḥaṣīran, gloss:kuşatan kapalı hâl} imgesinin sahibini saran bir duruma yaklaşması mümkün bir kişisel okuma olur. Hiç kimsenin başkasının yükünü taşımaması ve elçi gönderilmeden azap edilmemesi de sorumluluğu bildirim ve hesap çerçevesine yerleştirir (17:15). Bu kişisel çerçeve tarihsel topluluk okumasının yerini almaz; ona devredilemeyen hesap ve kişinin kendi kaydıyla karşılaşması boyutunu ekler.

## Kapanıştaki Sınıf

Kişisel kayıt çerçevesi, ayetin ikinci çoğul muhataplarından kapanıştaki belirli alıcı sınıfına geçişi görünür kılar: {ar:لِلْكَٰفِرِينَ, tr:li-l-kāfirīn, gloss:inkâr edenler için}. Aynı kelime ailesinin fiziksel örtme kullanımı {ar:كَفَرَ الشَّيْءَ, tr:kafara al-shayʾa, gloss:bir şeyi örtmek} bu sınıf adına ayrı bir görüntü ekler. Işık içinde yürüyen kişinin karşısında karanlıklarda kalıp çıkamayan kişinin bulunması ve ayetin sonunda inkâr edenlerden söz edilmesi, örtme ile çıkışsızlığı kuşatan yer imgesinde buluşturur (6:122). Bu sahne alıcı sınıfın olağan “inkâr edenler” anlamını korur; karanlık ve örtülme çağrışımı ise kapalı sonucun nasıl duyulduğunu derinleştirir.

Örtme imgesinden ayrı bir kol, nimeti yadsıma ve şükrü yerine getirmeme anlamındaki {ar:كَفْرُ النِّعْمَةِ, tr:kufru n-niʿmah, gloss:nimeti yadsıma} kullanımıdır. Bir insana merhametin tattırılması, ardından geri alınması ve kişinin nankör diye nitelenmesi bu anlamı somutlaştırır (11:9). Bu sahne kapanıştaki sınıf adına alınan iyiliği tanımama olasılığını katar; bu yankı 11:9'daki geri çekilmeyi 17:8'de yaşanmış bir merhamet kaybı olarak kurmaz.

Bu çağrışım önceki tarih dizisindeki iade ve geri dönüşle temas eder: mal, çocuk ve sayı artışının geri verilmesi (17:6), ardından iyilik ve kötülüğün yapanlara dönmesi (17:7), alınan nimeti örtme ya da şükrünü esirgeme olasılığını görünür kılar. Bu bağlantı önceki imkânları alanlarla 17:8'in sonundaki alıcı sınıfı özdeşleştirmez; inkârın olağan anlamı nankörlük ihtimalinden daha geniş kalır.

Genel bağışın iki gruba da ulaşıp engellenmemesi, 17:8'deki belirli atamayla farklı bir kapsam taşır: Rab her iki gruba desteğini sürdürür ve armağanı yasaklanmış değildir (17:20). {ar:نُّمِدُّ, tr:numiddu, gloss:desteğimizi sürdürürüz} uzanan yardımı, {ar:عَطَآءِ, tr:ʿaṭāʾ, gloss:armağan} verilen nimeti, {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} ise olumsuz yapı içinde bu bağışın esirgenmediğini taşır. Bu karşılaştırmanın sınırı şudur: ḥaṣīran her türlü nimetin kesilmesi anlamına gelmez, genel bağış da cezayı bütünüyle insanın kendi kendine ürettiği bir sonuca indirgemez.

</source_prose>
