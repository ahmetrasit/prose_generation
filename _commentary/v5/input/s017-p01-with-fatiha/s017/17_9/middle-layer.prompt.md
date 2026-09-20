# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:9**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.middle.claims.json`

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
- Refer to source paragraphs as `17:9 ¶N`.

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

`(17:9 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:9",
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
        "citation": "(17:9 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_9/17_9.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_9/17_9.middle.claims.json \
  --ayah-ref 17:9
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_9/17_9.prose.editorial.tr.md`

<source_prose>
## Bir bildirim, iki iş

17:9'un olağan bildirimi açıktır: Kuşkusuz bu Kur'an en düzgün olana yol gösterir ve iyi işler yapan inananlara büyük bir karşılık müjdeler. {ar:إِنَّ, tr:inna, gloss:kuşkusuz} özne adlandırılmadan önce bildirime güvence verir. {ar:هَٰذَا, tr:hādhā, gloss:bu} okurun dikkatini toplar; buradaki yakınlık fiziksel mesafe değil, dilin gösterme hareketidir. Ardından gelen belirli {ar:ٱلْقُرْءَانَ, tr:al-Qurʾāna, gloss:Kur'an} gösterileni adlandırır. Bu ad, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} ile {ar:وَيُبَشِّرُ, tr:wa-yubashshiru, gloss:müjde verir} yüklemlerinin ortak öznesidir: biri belirtilen hedefe yöneltir, öteki alıcısına haber ulaştırır. Aynı özne bu iki işi bağlar; yol gösterme hedefe, müjde alıcıya yönelen ayrı işlevler olarak kalır.

{ar:هَٰذَا, tr:hādhā, gloss:bu} işaretinden {ar:ٱلْقُرْءَانَ, tr:al-Qurʾāna, gloss:Kur'an} adına geçiş, bağlı tilavette de tek bir ses akışı kurar. Belirli adın başındaki vasl hemzesi ayrı bir başlangıç sesi olarak söylenmez ve ayet bu noktada zorunlu bir durak koymaz; sözcüğün içindeki hemze ayrı bir ses odağı olarak duyulur. Bu işitsel vurgu, gösterme ile adlandırma bağını belirginleştirirken yerleşik adı daha duyulur kılar.

Buradaki {ar:ٱلْقُرْءَانَ, tr:al-Qurʾāna, gloss:Kur'an} öncelikle bilinen Kitabın ve söylemin adıdır. Adın sözlük ailesindeki “toplayıp bir araya getirme” çağrışımı ihtiyatla duyulduğunda, aynı özneye bağlanan iki işlev Kur'anı ayrı işleri bir arada taşıyan derlenmiş malzeme gibi gösterir. Ad seslendirilen tilavet olarak da işitilebilir: bu çağrışım Kur'anı hidayet içeren bir metin olarak korurken, bir araya gelip okunarak iş gören bir hitap niteliğini de öne çıkarır. Her iki çağrışım da yerleşik adı ve gönderimini korur; Kur'anın yol gösterme ve müjde verme işleriyle temas ettikleri ölçüde cümleye katılır.

## Yolun hedefi

Kur'anın ilk işi, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} fiiliyle anlatılır. Form I'in üçüncü tekil eril muzari biçimi, başka bir kılavuzu görevlendirmek yerine Kur'anın kendisini yol gösteren özne yapar ve bu işi sürmekte olan bir işlev gibi sunar; biçim, bunun her an kesintisiz gerçekleştiğini ileri sürmez. Fiil kimin yöneltildiğini söylemez; ardından gelen hedef “kime?”den çok “nereye?” sorusunu karşılar. Bu nedenle müjde alıcıları yol göstermenin tek muhatabı diye geriye taşınmaz. Buradaki yöneliş, armağan ya da adak sunmak değil, açıkça belirtilen hedefe doğru kılavuzluktur.

Bu hedefi kuran {ar:لِلَّتِى, tr:li-llatī, gloss:şu olana} tek bir yazılı birim gibi görünse de iki görev taşır: başındaki lâm yönelişi bildirir, dişil ilgi zamiri ise ardından gelen tanımı açar. Böylece hedef, fiilin doğrudan nesnesi değil, yol göstermenin yöneldiği yerdir. Dişil zamir adı söylenmemiş bir hedefi düşündürür; yol, inanç, hâl ya da nitelik gibi olasılıklar açık kalır, fakat ayet bunlardan birini seçip adlandırmaz.

Bu söylenmemiş hedefe dönen bağımsız {ar:هِىَ, tr:hiya, gloss:o} iç cümlenin öznesi, {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} ise yüklemidir; en düzgün olma niteliği böylece Kur'an adına değil hedefe yüklenir. Zamirin niteliği söylemeden önce duyulması yükleme ayrı bir işitsel ağırlık verir, ancak tilavette zorunlu bir durak oluşturmaz. {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} yalın “doğru”dan daha güçlü bir üstünlük derecesi taşır: karşılaştırma kümesi söylenmediğinden başka seçenekleri kendiliğinden elemiş sayılmaz.

Hedefin bu niteliği, {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün}’ün düz çizgide kalma, denge ve sapmama çağrışımlarına düzeni ayakta tutma ve sürdürme yönünü ekler. {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} fiilinin hedefe yönelişi ile {ar:لِلَّتِى, tr:li-llatī, gloss:şu olana} öbeğinin hedefi kurması buluşunca, dayanak imgesi yolun istikrarı olarak belirir. Bu özel temas fiziksel bir destek nesnesi ya da diriliş sahnesi kurmaz; dayanak çağrışımının katkısı düzeni sürdürebilen bir doğrultudur. {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} olağan olarak doğru yönü gösterir; fiilin daha ihtiyatlı kök çağrışımı yol ya da hakikate ince bir işaret edişi de duyurabilir ve bu nüansın dayanağı yine açık hedeftir. {ar:ٱلْقُرْءَانَ, tr:al-Qurʾāna, gloss:Kur'an} adı derlenmiş ve seslendirilen malzeme olarak duyulduğunda, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} ile {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} tilaveti tekrar izlenebilir bir yol ve davranış örüntüsü hâlinde kurar. Bu örüntünün kapsamını 17:9'da adı verilmeyen, cümlede işaret edilen hedef belirler; bu bağlantı tek başına genel bir hayat tarzı ya da tek bir hukuk düzeni seçmez.

İzlenebilir güzergâh imgesi, önceki anlatıda kısmi görünürlük içindeki gece yolculuğuyla kurulur. İki menzil arasındaki hareket boyunca gösterilen işaretler yön bulmaya yardım eder ({ar:أَسْرَىٰ بِعَبْدِهِۦ لَيْلًا, tr:asrā biʿabdihi laylan, gloss:kulunu gece yürütmesi}; {ar:لِنُرِيَهُۥ مِنْ ءَايَٰتِنَآ, tr:linuriyahu min āyātinā, gloss:ona işaretlerimizden gösterelim diye}; {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:işaretlerimiz}; (17:1)). Bu sahne {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} ile buluşunca, hedefe yöneltilen yol gösterme işaretler belirdikçe izlenen bir güzergâh olarak da duyulur; bu, ilk bağlamın yerel katkısıdır (17:1). 17:2 ayrı bir boyut ekler: önceki Kitap açıkça rehberlik diye nitelenir ve başka bir vekile dayanmama uyarısı verilir ({ar:ٱلْكِتَٰبَ, tr:al-kitāba, gloss:Kitap}; {ar:هُدًى, tr:hudan, gloss:rehberlik}; (17:2)). Bu kez yazılı Kitap, yol üzerindeki görünür işaretlerden farklı olarak, rehberliğin topluluklar ve zaman boyunca taşınabilmesini düşündürür. İki bağlam birlikte 17:9'daki hedefi genişletir; güzergâh her hidayetin yöntemi değil, önceki anlatı da vahyin çevresini kuruyor olabilir (17:1, 17:2).

## Yolu istemek ve almak

Bu hedef, Fātiha'daki toplu dua ile yan yana okunduğunda okurun konumunu değiştirir. 17:9'da Kur'an insanı yöneltirken, dua eden topluluk {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭa al-mustaqīma, gloss:bizi dosdoğru yola ilet} diye kendisi için yol ister; okur hem yöneltilen hem de yön talep eden kişidir (1:6, 1:7). İstenen yol, nimet verilenlerin yolu diye açılır ve gazaba uğrayanlar ile sapmışların yolundan ayrılır ({ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:ṣirāṭa alladhīna anʿamta ʿalayhim, gloss:nimet verdiklerinin yolu}; {ar:غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ, tr:ghayri al-maghḍūbi ʿalayhim wa-lā al-ḍāllīn, gloss:gazaba uğrayanların ve sapmışların yolu olmayan}). {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} ile duadaki dosdoğru sıfatı aynı sözcük değildir; ortak çizgide kalma ve sapmama yönü, bildirilen hedefi istenen ve izlenen yola yaklaştırır. Bu yan yana geliş, kronolojik bir cevap ilişkisi değil, okurun hem yöneltilen hem kendisi için yön isteyen kişi olduğu bir karşılaşmadır; nimet verilenler ile 17:9'daki inananlar ayrı topluluklar olarak kalır (1:6, 1:7).

Yolu istemek, hitabın nasıl karşılandığı sorusunu açar. Kur'an üzerinde düşünmeye çağıran 4:82, başka bir kaynaktan gelmiş olsaydı onda birçok tutarsızlık bulunacağına ilişkin bir karşılaştırma ölçüsü koyar; 47:24 aynı düşünme sorusunun yanında kalpler üzerindeki kilitleri gündeme getirir ({ar:أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ, tr:a-fa-lā yatadabbarūna al-Qurʾāna, gloss:Kur'an üzerinde düşünmezler mi}; {ar:أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَآ, tr:am ʿalā qulūbin aqfāluhā, gloss:yoksa kalpler üzerinde kilitler mi var}; (4:82, 47:24)). Böylece {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} yalın bilgi aktarımından fazlası, düşünerek karşılanabilecek bir hitap gibi duyulur; tefekkür 17:9'un açıklamadığı bir önkoşula dönüşmeden, kalplerin kapalı kalma ihtimali de görünür olur (4:82, 47:24).

Yol gösteren hitaba verilen karşılık her bağlamda aynı değildir. Bir sınama oluşturan görülen rüya ve lanetlenmiş ağaçtan sonra uyarının büyük bir taşkınlığı artırdığı bildirilir ({ar:ٱلرُّءْيَا, tr:al-ruʾyā, gloss:görülen rüya}; {ar:ٱلشَّجَرَةَ ٱلْمَلْعُونَةَ, tr:al-shajarata al-malʿūnata, gloss:lanetlenmiş ağaç}; {ar:طُغْيَٰنًا كَبِيرًا, tr:ṭughyānan kabīran, gloss:büyük bir taşkınlık}; (17:60)). Elçi başka bir yerde halkının Kur'anı terk edilmiş saydığını bildirir ({ar:هَٰذَا ٱلْقُرْءَانَ مَهْجُورًا, tr:hādhā al-Qurʾāna mahjūran, gloss:bu Kur'anı terk edilmiş saydı}; (25:30)). İki ayrı hüküm de belirli topluluklara aittir: taşkınlık edenlere yol gösterilmediği bildirilir (63:6); iman edip açık delilleri gördükten sonra inkâr eden zalimler de anılır (3:86). Bu örnekler 17:9'a yeni bir alıcı koşulu eklemez; her biri kendi muhataplarına aittir. Böylece Kur'anın yol göstermesiyle alımlanma biçimlerindeki farklılık birlikte görünür olur (17:60, 25:30, 63:6, 3:86).

Karşılığın bir başka görünümü, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} hitabının bedende bıraktığı değişimdir. 39:23'te korkanların derileri önce ürperir, ardından derileri kalpleriyle birlikte Allah'ı anmaya yumuşar; bu iki aşamalı beden ve kalp tepkisi Allah'ın hidayeti diye adlandırılır ({ar:تَقْشَعِرُّ مِنْهُ جُلُودُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُمْ, tr:taqshaʿirru minhu julūdu alladhīna yakhshawna rabbahum, gloss:Rablerinden korkanların derileri ondan ürperir}; {ar:ثُمَّ تَلِينُ جُلُودُهُمْ وَقُلُوبُهُمْ إِلَىٰ ذِكْرِ ٱللَّهِ, tr:thumma talīnu julūduhum wa-qulūbuhum ilā dhikri llāh, gloss:sonra derileri ve kalpleri Allah'ı anmaya yumuşar}; {ar:ذَٰلِكَ هُدَى ٱللَّهِ يَهْدِى بِهِۦ مَن يَشَآءُ, tr:dhālika hudā llāhi yahdī bihi man yashāʾ, gloss:bu Allah'ın hidayetidir ve dilediğini onunla doğruya yöneltir}; (39:23)). 17:82 farklı bir ayrıntı ekler: Kur'an inananlar için şifa ve rahmet, zalimler için kaybın artmasıdır ({ar:شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ, tr:shifāʾun wa-raḥmatun li-l-muʾminīn, gloss:inananlara şifa ve rahmet}; {ar:وَلَا يَزِيدُ ٱلظَّٰلِمِينَ إِلَّا خَسَارًا, tr:wa-lā yazīdu al-ẓālimīna illā khasāran, gloss:zalimlerin ancak kaybını artırır}; (17:82)). İlk imge alımlanmanın bedensel sürecini, ikincisi muhataplara göre farklı sonucunu görünür kılar; birlikte onarıcı bir görünüş açarlar, herkese aynı sonucu yüklemezler (39:23, 17:82). Derinin bu ürperme ve yumuşama sahnesi, {ar:يُبَشِّرُ, tr:yubashshiru, gloss:müjde verir} için duyulan yüz ve deri yankısıyla temas etse de iki ayrı bağlamın katkıları birbirine karışmaz.

Alımlanma zaman içinde de görünür olur. 17:11 insanı aceleci diye niteler ve kötüyü de iyiyi ister gibi isteyebildiğini bildirir ({ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci}; (17:11)). 17:12 geceyle gündüzü iki işaret yapar: gece işaretinin silinmesi ve gündüzün aydınlatması zaman farkını belirginleştirir; yılların sayısı ile hesap ve ayrıntılandırma bu farkları izlemeyi sağlar ({ar:ٱلَّيْلَ وَٱلنَّهَارَ ءَايَتَيْنِ, tr:al-layla wa-l-nahāra āyatayn, gloss:geceyi ve gündüzü iki işaret}; {ar:عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:ʿadada al-sinīna wa-l-ḥisāba, gloss:yılların sayısını ve hesabı}; {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:onu ayrıntısıyla bölümledik}; (17:12)). Bu iki katkı {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} ile {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} hedefini zamana bakarak ayrım yapan, acele hükmü tartan bir yöneliş olarak genişletir; bu ölçü çağrışımı her hızlı davranışa ilişkin hüküm değildir (17:11, 17:12). 17:12'nin pratik zaman hesabı yerinde kalır. Okuma ve tilavetin ritmi ihtiyatlı bir zamansal yankı sunarken, {ar:ٱلْقُرْءَانَ, tr:al-Qurʾāna, gloss:Kur'an} adı vahyedilmiş Kitabı gösterir; ne zamanın kendisine ne özel bir para ölçüsüne dönüşür, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} de gerçek anlamda yürüme değildir.

Bu hesap bağlamından ayrı iki ayet, tilavet ve söze farklı katkılar yapar. Kur'anın ölçülü okunması okuyuşun biçimini, daha düzgün söz ise ifadenin niteliğini öne çıkarır ({ar:وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا, tr:wa-rattili al-Qurʾāna tartīlan, gloss:Kur'anı ölçülü okuyuşla oku}; {ar:وَأَقْوَمُ قِيلًا, tr:wa-aqwamu qīlan, gloss:sözü daha düzgün}; (73:4, 73:6)). Böylece 73:4 ölçülü tilavet boyutunu, 73:6 ise {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} niteliğinin konuşmadaki yankısını ekler. İlk buyruk {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} fiilinin anlamını ya da hidayetin sebebini tanımlamaz; 73:6'daki gece sözü de kendi bağlamına aittir. Bu sınırlar içinde iki ayrı ifade, 17:9'daki yönelişin işitilme ve dile geliş biçimlerini belirginleştirir (73:4, 73:6).

Tilavetin ölçüsü, vahyin zamana yayılan alımlanmasına dair başka bir tasvirle tamamlanır. 25:32 Kur'anın tek parça hâlinde indirilmemesini kalbin sağlamlaştırılması ve ölçülü okuyuşla birlikte anar ({ar:جُمْلَةً وَاحِدَةً, tr:jumlatan wāḥidatan, gloss:tek parça halinde}; {ar:لِنُثَبِّتَ بِهِۦ فُؤَادَكَ, tr:li-nuthabbita bihi fuʾādaka, gloss:kalbini onunla sağlamlaştıralım diye}; {ar:وَرَتَّلْنَٰهُ تَرْتِيلًا, tr:wa-rattalnāhu tartīlan, gloss:onu ölçülü okuyuşla}; (25:32)); 54:22 hatırlamak için kolaylaştırılmasını ekler ({ar:يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ, tr:yassarnā al-Qurʾāna li-l-dhikr, gloss:Kur'anı hatırlama için kolaylaştırdık}; (54:22)). İlki kalbin güçlenmesi ve ölçülü okuma yolunu, ikincisi hatırlamaya erişilebilirliği öne çıkarır. Birlikte, {ar:يَهْدِى, tr:yahdī, gloss:yol gösterir} ile verilen hedefi zaman içinde alınabilen bir hitap olarak genişletirler; bu olası alımlanma biçimi her hidayet için tek süreç dayatmaz (25:32, 54:22).

## Müjdenin muhatabı

Yönelişe eklenen ikinci iş, {ar:وَيُبَشِّرُ, tr:wa-yubashshiru, gloss:müjde verir} ile aynı özneye bağlanır. Başındaki bağlı “ve”, onu yeni bir cümle değil Kur'anın ikinci yüklemi yapar; muzari Form II biçimi bu işi sürmekte olan bir eylem gibi sunar. Yön gösterme ile müjde arasındaki ses bağı iki işi aynı özne altında tutar, anlamlarını birleştirmez. Yakın yalın ve ettirgen biçimler karşılaştırma noktalarıdır; ayetin Form II'si ek yoğunluk taşımadan sürmekte olan müjde verme işini kurar.

Olağan kullanımında {ar:يُبَشِّرُ, tr:yubashshiru, gloss:müjde verir} alıcısına sevinç verecek haber getirir; inananların alıcı, büyük ödülün de haberin içeriği olması bu olumlu yönü tamamlar. Aynı sözcük ailesinin yüz ve deri başta olmak üzere insanın görünen dış yüzüne ilişkin kullanımı, haberi alan kişide sevinç ve beklentinin bedensel olarak hissedilmesini düşündürür. Yüz ve deri dalı, alıcının sevincini benzetmeli bir beden imgesiyle duyurur; fiil haber verme anlamında kalır, kişiyi ya da deriye dokunuşu adlandırmaz.

Olumlu haber, hemen ardından açılan ayrı bir gelecekle yan yana gelir. Ahirete inanmayanlar başka bir alıcı grubu olarak anılır ve onlar için acı verici bir azabın hazırlandığı bildirilir ({ar:وَأَنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:wa-anna alladhīna lā yuʾminūna bi-l-ākhirati, gloss:ahirete inanmayanlar}; {ar:أَعْتَدْنَا لَهُمْ عَذَابًا أَلِيمًا, tr:aʿtadnā lahum ʿadhāban alīman, gloss:onlara acı verici bir azap hazırladık}; (17:10)). Böylece 17:9'daki ödül vaadi ile 17:10'daki acı sonuç, farklı alıcı ve akıbetlere yönelen daha geniş bir duyuruda buluşur (17:9, 17:10). 17:10'un önceki cümleye hangi sözdizimsel düzeyde bağlandığı açık bırakılır; bu bağlantı 17:9'daki {ar:يُبَشِّرُ, tr:yubashshiru, gloss:müjde verir} fiilinin olağan iyi haber anlamını değiştirmez (17:10). Kötü haber yönü, açık olumsuz içerik ya da alaycı tersleme bulunduğunda düşünülebilir; burada açık acı sonucu bu daha geniş okumaya zemin verir (17:10).

Olumlu vaadin alıcıları belirli eril çoğul etkin ortaç olan {ar:ٱلْمُؤْمِنِينَ, tr:al-muʾminīn, gloss:inananlar}dır; tanınabilir bir topluluktur, belirsiz bir “herhangi biri” değildir. Sözcüğün güven ve korkudan emin olma alanı, büyük ödül haberini doğru kabul eden ve onunla kalbi yatışan bir tutum gibi renklendirir; yerel anlam yine inananlardır. İman edip imanlarını zulümle karıştırmayanlara güvenlik ve hidayet bağlayan başka bir ifade bu güven tonunu somutlaştırır ({ar:ٱلَّذِينَ ءَامَنُوا۟ وَلَمْ يَلْبِسُوا۟ إِيمَٰنَهُم بِظُلْمٍ, tr:alladhīna āmanū wa-lam yalbisū īmānahum bi-ẓulmin, gloss:imanlarını zulümle karıştırmayanlar}; {ar:ٱلْأَمْنُ, tr:al-amn, gloss:güvenlik}; {ar:هُدًى, tr:hudan, gloss:rehberlik}; (6:82)). Bu ayetin güvenlik sözü korkuya karşı emniyet, iç huzur ve tehlikeden emin olmayı somutlaştırır; şartı kendi bağlamında kalır, topluluklar da özdeşleşmez (6:82). Karşı grubu tanımlayan {ar:لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:lā yuʾminūna bi-l-ākhirati, gloss:ahirete inanmayanlar}, 17:10'da iman karşıtlığını ahirete dair bildirimi doğru kabul etme ekseninde kurar (17:10). Böylece 17:9'daki inananlar güvenle alınan haberin alıcıları olarak renklenirken, iki bağlamın koşulları ayrı kalır.

Alıcı grubunun niteliğini {ar:ٱلَّذِينَ, tr:alladhīna, gloss:olanlar} açar: ilgi zamiri inananlara bağlanır ve ardından gelen çoğul eylem cümlesini onların özelliği yapar. Bu sıra, önce alıcıları ve yaptıklarını, ardından anna cümlesinde vaadin içeriğini gösterir; eylem cümlesi ödülün ikinci bir içeriği değil, müjde alan topluluğun niteliğidir. Böylece ayetin yerel etik dizisinde inanç, süren iş ve salih ameller yan yana durur, birbirinin yerine geçmez.

Bu ortak eylem {ar:يَعْمَلُونَ, tr:yaʿmalūna, gloss:yapıp ederler} ile verilir: çoğul muzari biçim, inananların amaçlı ve sürmekte olan işini öne çıkarır. Tek seferde tamamlanmış bir işten çok devam eden eylemi niteler; geçmişteki tekil bir işi de kapsam dışında bırakmaz. Fiilin nesnesi açıkça {ar:ٱلصَّٰلِحَٰتِ, tr:al-ṣāliḥāti, gloss:iyi işler}dir; eylem genel faaliyetten iyi ve yararlı işlerin açık uçlu sınıfına yönelir. İnananlar işi yapan, salih işler ise yapılanın nesnesidir; bu, etkisi olan bilinçli bir iş görmedir. Buradaki iş ücretli ya da resmî görev ve alışveriş değil, güvenle kabul edilen haberi amaçlı davranışta görünür kılan eylemdir. Bu yerel bağ belirli bir dünyevi sonuç ya da bütün sureye taşınacak bir kural seçmeden inançla işi birbirine bağlar.

{ar:ٱلصَّٰلِحَٰتِ, tr:al-ṣāliḥāti, gloss:iyi işler} belirli dişil çoğul bir ad olarak kapalı bir davranış listesi değil, iyi, düzgün ve yararlı işlerden oluşan açık bir sınıftır. Aynı sözlük ailesi iyi durumda olmayı ve bozuk olanı düzelterek bu duruma getirmeyi kapsar; eylemin nesnesi ameller olduğunda ikinci yön de duyulur. Bu onarım çağrışımı kategoriye tek bir kusur, teknik tamir nesnesi ya da kişiler arası uzlaşma senaryosu bağlamaz.

## İşin onarıcı yönü

Düzeltme çağrışımı, tövbe, işleri düzeltme, Allah'a tutunma ve dini içtenlikle O'na adama eylemlerinin bir araya geldiği bağlamda somutlaşır. Bu kişiler inananların arasına döner ve ödülle anılır; {ar:وَأَصْلَحُوا۟, tr:wa-aṣlaḥū, gloss:işleri düzelttiler} aynı sözlük ailesindeki iyi durumda olma adını etkin düzeltme işine taşır (4:146). Bu örnek salih işlerin onarıcı yönünü görünür kılar; kapsamı burada anlatılan tövbe ve dönüş dizisidir, her salih amelin tövbe olduğu ya da önceden kişiler arası çatışma bulunduğu sonucu değildir (4:146).

Bu onarıcı yön tarihsel bir düzen kaybıyla somutlaşır. İsrailoğullarının yeryüzünde iki kez bozgunculuk çıkaracağı bildirilir ({ar:لَتُفْسِدُنَّ فِى ٱلْأَرْضِ مَرَّتَيْنِ, tr:latufsidunna fī al-arḍi marratayni, gloss:yeryüzünde iki kez bozgunculuk çıkaracaksınız}; (17:4)). Bu bozulma, salih işlerin yanıt verebileceği belirli bir düzen kaybını kurar. İyilik edenin iyiliğinin, kötülük edenin kötülüğünün kendisine döndüğü tekrarlandığında, eylemin etkisi failine bağlanır ({ar:إِنْ أَحْسَنتُمْ أَحْسَنتُمْ لِأَنفُسِكُمْ, tr:in aḥsantum aḥsantum li-anfusikum, gloss:iyilik ederseniz kendiniz için iyilik etmiş olursunuz}; {ar:وَإِنْ أَسَأْتُمْ فَلَهَا, tr:wa-in asaʾtum falahā, gloss:kötülük ederseniz o da kendinizedir}; (17:7)). Böylece {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} hedefi düzeni sürdürebilen bir yapı, {ar:ٱلصَّٰلِحَٰتِ, tr:al-ṣāliḥāti, gloss:iyi işler} ise bu bozulmaya cevap veren işler olarak duyulur (17:4, 17:7). Bu tarihsel temasın katkısı fail ile eylem arasındaki geri dönüşü göstermektir; genel ya da anlık sonuç yasası kurmadan eylemin etkisini kendi yapanına bağlar (17:4, 17:7).

Bu tarihsel dizilimin son hareketinde merhamet ihtimali koşullu dönüşle birlikte durur: “Belki Rabbiniz size merhamet eder” ve “dönerseniz biz de döneriz” ifadeleri tekrarı yeni bir yönelme olanağıyla yan yana getirir ({ar:عَسَىٰ رَبُّكُمْ أَن يَرْحَمَكُمْ, tr:ʿasā rabbukum an yarḥamakum, gloss:belki Rabbiniz size merhamet eder}; {ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:eğer dönerseniz biz de döneriz}; (17:8)). Böylece düzeltme yalnız kapalı bir ceza döngüsü olarak görünmez; dönüş olanağı bu anlatılan tarih içinde kalır ve genel bir sonuç yasasına dönüşmez (17:8).

## Ödülün cümlesi

İşlerin ardından müjdenin içeriğini {ar:أَنَّ, tr:anna, gloss:ki} açar. Ayetin başındaki {ar:إِنَّ, tr:inna, gloss:kuşkusuz} ana bildirimi kurar; açık hemzeli anna ise bu bildirimin içinde müjdenin ne söylediğini tamamlayan gömülü vaat cümlesidir. {ar:وَيُبَشِّرُ, tr:wa-yubashshiru, gloss:müjde verir} hem haberi alanları hem içeriği ister: {ar:ٱلْمُؤْمِنِينَ, tr:al-muʾminīn, gloss:inananlar} alıcıdır, önceki ilgi cümlesi onların salih işler yaptığını açıklar ve anna cümlesi ödülü bildirir. Böylece eylem alıcıların niteliği olarak vaatten önce gelir.

Ödül adı gelmeden önce görünen {ar:لَهُمْ, tr:lahum, gloss:onlar için} aynı inanan ve salih iş yapan topluluğu cümlede taşır. Lâm ödülün onlara ayrıldığını ve onlara yarar sağladığını bildirir; okur önce kime yöneldiğini, sonra neyin verileceğini duyar. Öbek böylece müjde fiilinin alıcılarına ulaşan yarar ile ödül cümlesindeki tahsisi birlikte taşır; burada cümle ödülün fiziksel biçimini değil, kime ayrıldığını ve kime yarar sağladığını belirginleştirir.

Belirsiz ve belirtme durumundaki {ar:أَجْرًا, tr:ajran, gloss:karşılık}, anna cümlesinin içinde vaadin içeriğidir. Sözcüğün olağan alanı yapılan işten işi yapana dönen yararlı karşılıktır; burada bu dönüş olumlu bir yarar olarak kurulur. Maddi ücret, kira ve hizmet karşılığı yalnızca anlam alanını aydınlatan benzetmelerdir; 17:9 bunları sözleşme ya da dünyalık ödeme olarak sunmaz. Vaadin yönü iyi iş için beklenen manevi ödüldür, verileceği zaman ise belirtilmez. Tanvin miktarı burada ölçülmeden bırakır; bu belirsizlik ödülün yokluğu ya da bilinemeyeceği değil, ölçüsünün bu cümlede açıklanmadığı anlamına gelir.

Ardından gelen {ar:كَبِيرًا, tr:kabīran, gloss:büyük}, ödül adıyla eril tekil, belirtme ve belirsizlik özelliklerinde uyuşur; büyüklük inananlara ya da işlerine değil, karşılığın kendisine aittir. Olumlu vaat geniş bir ölçü ve derece kazanır; ihtiyatlı bir okumada sıradan ücretten daha büyük ölçekte duyulur. Bu sıfat alıcının yaşı, rütbesi, kibri ya da günahını değil, ödülün olumlu genişliğini niteler; belirli bir en büyük payı da seçmez. İki tanvinli son, ödül ile büyüklüğünü tek bir ses kapanışında buluştururken miktarı açık bırakır; burada sayı ya da sonsuzluk hesabı verilmez. Böylece ayetin son vurgusu iki Kur'an işlevinden belirtilmiş işe ve karşılığın genişliğine ilerler.

Karşılığın olağan yararlı dönüş anlamından uzakta, aynı sözcük ailesi kırık bir kemiğin ya da elin yeniden birleştirilmesini anlatabilir. Bu maddi okumanın ayrı tetikleyicileri vardır: salih işlerin sağlamlığı, 17:4'teki tarihsel bozulma, 17:6'da üstünlüğün geri verilmesi ve 17:16'daki yıkım ({ar:أَجْرًا, tr:ajran, gloss:karşılık}; {ar:ثُمَّ رَدَدْنَا لَكُمُ ٱلْكَرَّةَ عَلَيْهِمْ, tr:thumma radadnā lakumu al-karrata ʿalayhim, gloss:sonra üstünlüğü onlara karşı size geri verdik}; {ar:فَدَمَّرْنَٰهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık}; (17:4, 17:6, 17:16)). Birleşen kemik çoğu kez eğri, çıkıntılı ya da düzgün olmayan biçimde kaynayabilir; bu süreç onarımı ve geride kalabilen hasar izini aynı maddi imge içinde kurar (17:4, 17:6, 17:16). Bu uzak, keşifsel temas ajr'in olağan anlamını değiştirmez ve gerçek kemik iyileşmesi ya da toplumsal düzelme vaadi değildir; 17:6'daki üstünlüğün geri gelişi kendi tarihsel bağlamında kalır (17:4, 17:6, 17:16). İmgenin katkısı, onarımın hasar izini taşıyabileceğini düşündürmesidir.

## Emeğin ileriye uzanan ufku

Bugünkü işin kime döneceği, sonraki kişisel kayıt sahnesinde beden ve okuma üzerinden görünür olur. Kişinin eylemi boynuna bağlanır, önüne açılmış bir kayıt çıkar ve ona kitabını okuması söylenir ({ar:أَلْزَمْنَٰهُ طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:alzam-nāhu ṭāʾirahu fī ʿunuqihi, gloss:kendi payını boynuna bağladık}; {ar:كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:kitāban yalqāhu manshūran, gloss:açılmış olarak karşısına çıkan kitap}; {ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku}; (17:13, 17:14)). Kendi nefsinin o gün hesap görücü olarak yeterli oluşu okumayı salt kayıttan hesaba çevirir ({ar:كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā bi-nafsika al-yawma ʿalayka ḥasīban, gloss:bugün kendi nefsin sana hesap görücü olarak yeter}; (17:14)). Ardından hidayetin kişinin yararına, sapmanınsa yine kendi aleyhine olduğu söylenir ({ar:ٱهْتَدَىٰ لِنَفْسِهِۦ, tr:ihtadā li-nafsihi, gloss:kendi yararına doğru yolu buldu}; {ar:ضَلَّ فَإِنَّمَا يَضِلُّ عَلَيْهَا, tr:ḍalla fa-innamā yaḍillu ʿalayhā, gloss:saparsa zararı yine kendisine olur}; (17:15)). Böylece 17:9'daki süren iş, kişinin daha sonra kendi eylemini okuyacağı bir ufka uzanır. Yazılı Kur'an ile kişisel amel kaydı ayrı kitap işlevleri taşır; aynı okuma dizisindeki yankı şimdiki yönelişi ileride okunacak eylemle buluştururken yargı gününe ilişkin olağan anlamı korur (17:13, 17:14, 17:15).

Bu ufuk, yakın ve uzak amaçların ayrıldığı pasajda zaman içinde daha da belirginleşir. Hemen geleni isteyenin payı hızla verilir; ahireti isteyen kişi ise ona yaraşır biçimde çaba gösterir ve mümin olarak kalır ({ar:ٱلْعَاجِلَةَ, tr:al-ʿājilata, gloss:hemen geleni}; {ar:ٱلْءَاخِرَةَ, tr:al-ākhirata, gloss:ahireti}; {ar:سَعَىٰ لَهَا سَعْيَهَا, tr:saʿā lahā saʿyahā, gloss:ona yaraşır biçimde çaba gösterdi}; {ar:وَهُوَ مُؤْمِنٌ, tr:wa-huwa muʾminun, gloss:inanmış olarak}; (17:18, 17:19)). Şimdiki rızkın iki gruba da ulaşması ve derecelerin karşılaştırılması, bu ayrı yönelişleri aynı zamana sıkıştırmaz; çaba takdir edilmiş olarak da anılır ({ar:سَعْيُهُم مَّشْكُورًا, tr:saʿyuhum mashkūran, gloss:çabaları takdir edilmiş}; {ar:أَكْبَرُ دَرَجَٰتٍ وَأَكْبَرُ تَفْضِيلًا, tr:akbaru darajātin wa-akbaru tafḍīlan, gloss:dereceler ve üstünlük bakımından daha büyük}; (17:20, 17:21)). Bu yan yana geliş, {ar:يَعْمَلُونَ ٱلصَّٰلِحَٰتِ, tr:yaʿmalūna al-ṣāliḥāti, gloss:iyi işler yaparlar} işini seçilen ufka dönük gayretle ilişkilendirir; iyi işin alanı ahiret arayışından geniş kalır (17:9, 17:18, 17:19). 17:21'in derece karşılaştırması büyük vaadin ufkunu açar; 17:9'daki sıfat da bu karşılaştırmadan tek bir rütbe, alıcı ya da maddi miktar çıkarmadan açık kalır (17:21).

İşten sonra bulunan karşılık düşüncesi, iyi olanı önden gönderip onu Allah katında bulma ve daha büyük ecirle birlikte anılma üzerinden başka bir zaman bağı kazanır ({ar:وَمَا تُقَدِّمُوا لِأَنفُسِكُم مِّنْ خَيْرٍ تَجِدُوهُ عِندَ ٱللَّهِ, tr:wa-mā tuqaddimū li-anfusikum min khayrin tajidūhu ʿinda Allāh, gloss:önden gönderdiğiniz hayrı Allah katında bulursunuz}; {ar:وَأَعْظَمَ أَجْرًا, tr:wa-aʿẓama ajran, gloss:daha büyük ecir}; (73:20)). Bugünkü iyilikle daha sonra bulunan ödül arasındaki aralık, {ar:أَجْرًا, tr:ajran, gloss:karşılık} sözcüğündeki yararlı dönüş yönünü genişletir; ilişki piyasa ücretinden ayrılarak şimdi gönderilen iyiliğin sonra bulunan karşılığı olarak duyulur (73:20).

## Dosdoğru yönün yaşanan biçimleri

Hedefin düzgün çizgide kalma ve denge yönü, gündelik ölçüde somut bir uygulama bulur. Ölçüyü tam vermek ve dosdoğru teraziyle tartmak, adil alışverişte doğruluğu yaşatır ({ar:بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:bi-l-qisṭāsi al-mustaqīm, gloss:dosdoğru teraziyle}; (17:35)). Bu sahne {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} niteliğinin denge ve doğruluk yönünü yaşanan bir pratiğe taşır; terazi kendi sözcüğü olarak kalır, iki ifade arasında biçimsel türetme kurulmaz (17:35).

Ölçüden kişiler arası tutuma geçildiğinde, antlaşmalı taraflar birbirlerine dosdoğru kaldıkları sürece aynı doğrulukla karşılık vermeye çağrılır ({ar:فَمَا ٱسْتَقَٰمُوا۟ لَكُمْ فَٱسْتَقِيمُوا۟ لَهُمْ, tr:fa-mā istaqāmū lakum fa-staqīmū lahum, gloss:onlar size dosdoğru kaldıkça siz de onlara dosdoğru kalın}; (9:7)). Düz çizgiyi koruma ve dengede kalma yönü böylece toplumsal bir davranışta görünür olur; antlaşma bağlamın özel uygulaması olarak kalırken 17:9'daki hedef genel yöneliş niteliğini korur (9:7).

Yolda dosdoğru kalmanın şartlı olarak bol suya bağlandığı ifade, düzgün yönelişle hayatı sürdüren maddi dayanağı yan yana getirir ({ar:ٱسْتَقَٰمُوا۟ عَلَى ٱلطَّرِيقَةِ, tr:istaqāmū ʿalā al-ṭarīqati, gloss:yolda dosdoğru kaldıklarında}; {ar:لَأَسْقَيْنَٰهُم مَّآءً غَدَقًا, tr:la-asqaynāhum māʾan ghadaqan, gloss:onlara bol su verirdik}; (72:16)). Aynı sözcük ailesinin düzeni ayakta tutan dayanak ya da yeterli geçim anlamındaki uzak kolu, suyu yaşamı taşıyan destek olarak duyurur. Bu, 72:16 ile 17:9 arasındaki sınırlı bir benzetmedir: su, odak ayetin vaadi ya da {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} sözcüğünün anlamı değil, destek çağrışımını somutlaştıran unsurdur (72:16).

Dosdoğru hedefin bedensel yankısı, başka ilah edinmeme uyarısının ardından kişinin kınanmış ve desteksiz bırakılarak oturmasıyla belirir ({ar:لَا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhar, gloss:Allah ile birlikte başka ilah edinme}; {ar:فَتَقْعُدَ مَذْمُومًا, tr:fa-taqʿuda madhmūman, gloss:kınanmış olarak oturup kalırsın}; {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız ve terk edilmiş}; (17:22)). Bu sahne {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} hedefinin bedensel dik durma yankısına karşı oturuş ve desteksizliği getirir; karşıtlık bu bağlantıda imgeseldir, dilbilgisel değildir. {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün} hedefin niteliğini bildiren yüklem olarak kalır; {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız ve terk edilmiş} ise olağan anlamında terk edilmişlik ve desteksizlik taşır. Bacak desteğini yitirip dik duramama imgesi bu iki görünüşün yan yana gelişinden doğar, makhdhūlan'ın bağımsız sözlük anlamı değildir. Bu özel karşılaşmada dik durma çağrışımı hedefi eylemi ayakta tutabilen bir yön olarak duyurur (17:22).

Hareket hâlindeki beden, yönelişi iki ayrı yürüyüşün karşıtlığında görünür kılar: yüzüstü kapanarak yürüyen kişiyle dengeli biçimde dosdoğru yolda yürüyenin hangisinin daha iyi yönlendirildiği sorulur ({ar:يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ, tr:yamshī mukibban ʿalā wajhihi, gloss:yüzüstü kapanarak yürümek}; {ar:يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:yamshī sawiyyan ʿalā ṣirāṭin mustaqīm, gloss:düz bir yolda dosdoğru yürümek}; (67:22)). Bu kişilerin sahnesi 67:22'ye aittir; 17:9'la kurulan temas, aynı kişileri ya da gerçek bir yürüyüşü odak ayete taşımaz. Onun yerine {ar:أَقْوَمُ, tr:aqwamu, gloss:en düzgün}’ün çizgiyi koruma, denge ve sapmama yönü, yol üzerindeki bedenin hareketinde kavranabilir hâle gelir (67:22).

</source_prose>
