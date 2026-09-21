# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **103:2**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.middle.claims.json`

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
- Refer to source paragraphs as `103:2 ¶N`.

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

After the first complete prose draft, compute the ledger metrics and return to
this clustering stage for a mandatory diagnostic pass when the source has at
least ten prose paragraphs and any of these warning signals appears:

- `retained_word_ratio` is greater than `0.80`;
- `output_to_source_paragraph_ratio` is greater than `0.75`;
- fewer than `0.40` of the output prose paragraphs are multi-source paragraphs.

These are review triggers, not compression targets, quality scores, or
validator limits. Do not shorten until a number crosses a boundary. A
semantically irreducible commentary may remain beyond one or all of these
signals after the required pass.

For that pass, challenge every repeated setup, recap, defensive qualification,
and run of single-source paragraphs that develops the same carrier, question,
image, mechanism, or consequence. Privately draft the best continuous merged
formulation, then compare it unit by unit with the current version. Adopt the
merge only when every distinct unit still has an explicit substantive landing,
every modality and boundary remains visible, citations remain locally
meaningful, and the Turkish becomes easier rather than merely shorter. If the
merge fails any test, keep the material separate and give the relevant
standalone clusters concrete semantic non-merging reasons. Never delete,
generalize, or bury a unit merely to improve a diagnostic metric.

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

`(103:2 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "103:2",
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
        "citation": "(103:2 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s103-regular-20260911/s103/103_2/103_2.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s103-regular-20260911/s103/103_2/103_2.middle.claims.json \
  --ayah-ref 103:2
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s103-regular-20260911/s103/103_2/103_2.prose.editorial.tr.md`

<source_prose>
Âyet, 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:zamanın akışı} yemininin cevabını verir: {ar:إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ, tr:inne'l-insânu le-fî husr, gloss:İnsan gerçekten kayıp içindedir}. Buradaki {ar:إِنَّ, tr:inne, gloss:gerçekten} yalnızca cümleye eklenmiş bir giriş vurgusu değildir; insanı ve onun bulunduğu durumu bildiren bütün önermeyi yönetir. Hüküm iki ayrı sıkılaştırmayla kurulur: inne başta doğrulamayı başlatır, yüklemin başındaki lâm da bu doğrulamayı doğrudan kayıp hükmüne ulaştırır. Şedde ve art arda duyulan iki n sesi, insan adı gelmeden sözü tutup yoğunlaştırır; hüküm öznesi ve yüklemi açılmadan önce bile bastırılmış bir ses kazanır.

{ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} tekil ve belirli görünür; burada tek bir kişiyi işaret etmekten çok insan türünü bir sınıf olarak toplar ve o sınıfın her üyesini içine alır. Bu isim, kaybetme işini yapan bir faili değil, kendisine bir durum yüklenen insanlığı öne çıkarır. 103:1'de zaman gösterildikten sonra tanıklığın altında insanın durumu ilan edilir. Okunuşta başlangıçtaki burun sesi el-insân'da sürer, {ar:خُسْرٍ, tr:husr, gloss:kayıp} kelimesinin sızıcı kapanışıyla özne ve yüklem tek bir hüküm gibi birbirine bağlanır. Bu insan-kayıp eşleşmesi 22:11, 46:18 ve 41:25'teki hüküm bağlamlarında da belirginleşir. İnsan sözünün sosyal yakınlık alanı ile klasik türetimlerde anılan unutma baskısı burada sınırlı bir gerilim açar: 103:3'te iman, iyi iş ve karşılıklı öğüt, sosyal olarak kurulmuş ve unutmaya açık insanın karşısına çıkar. Bu gerilim yerel insan anlamını değiştirmez; hükmün açtığı ihtiyacı görünür kılar.

Hükmün insanı nasıl bir durumda gösterdiğini {ar:لَفِى, tr:le-fî, gloss:içindedir} kuruluşu belirler. İçinde anlamındaki {ar:فِى, tr:fî, gloss:içinde}, kaybı insanın yanında duran gevşek bir nesne gibi değil, insanın içine yerleştiği bir durum alanı gibi kurar. Lâm ile fî aynı kısa yüzeyde buluştuğu için doğrulama ile kuşatma, kayıp kelimesi söylenmeden önce birlikte duyulur. Lâm'ın yüklemin başına yerleşmesi de vurguyu cümlenin kenarında bırakmaz; doğrulama, insanın hangi durumda bulunduğunu bildiren yükleme ulaşır. Böylece 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:zamanın akışı} uzakta duran bir tanıklık olarak kalmaz; yeminin cevabını taşıyan lâm ve insanı kaybın içine yerleştiren fî, zaman baskısını içinde bulunulan bir durumun mekânına dönüştürür.

Son kelime {ar:خُسْرٍ, tr:husr, gloss:kayıp}, tek bir kaybetme olayını değil, fî'nin yönettiği soyut bir durumun adını verir. İsim-fiil yoğunluğu geniş kayıp alanını bir noktada toplar. Bu alan eksilme, anapara yitimi, ölçüde azalma ve yıkım yönlerini duyurur; cümlenin kuruluşu kaybı belirli bir ticaret veya ölçü sahnesine kapatmadığı için hüküm açık uçlu kalır. Belirsiz oluşu da belirli bir nesneye, miktara ya da tek bir kayba kapanmayan bu açıklığı korur. Standart kısa söyleyiş âyeti keskin biçimde kapatırken, aktarılan daha uzun söyleyişler aynı kayıp inişine daha ağır bir ses verir; bu karşılaştırma kısa yüzeyin kapanışını açıklar. 103:1'deki asr, 103:2'deki husr ve 103:3'teki sabr sözlerinin r ile kapanışı da bu kısa pasajın ses zincirini birbirine bağlar. 103:3'teki iman, iyi iş, gerçeğe bağlılık ve karşılıklı öğüt, burada tamamlanan geniş insan hükmüne cevap verecek açılımın zeminini hazırlar.

Bu yapı insanı yalnız zaman zaman kayba uğrayan biri değil, kuşatıcı bir eksilme koşulunun içinde bulunan bir varlık olarak duyurur. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} insan sınıfını, {ar:خُسْرٍ, tr:husr, gloss:kayıp} bu sınıfı kuşatan genel eksilmeyi, {ar:لَفِى, tr:le-fî, gloss:içindedir} ise insanın bu alanın içinde bulunuşunu taşır. İki vurgu bu ilişkiyi sıkılaştırır; böylece eksilme dışarıdan gelip geçen bir olaydan çok insanın yaşadığı koşul gibi görünür. Bu temas, insan türünün yalnızca böyle açıklanması gerektiğini söylemez; açık hükmün kuşatıcılığını genişletir.

## Sürenin Hesabı

Zaman burada kaybı üretmekten önce onun birikerek görünürleşmesini sağlar. 104:3'te servetin kalıcı olduğu sanısı keskinleştiğinde {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} görünür insan varlığını, {ar:خُسْرٍ, tr:husr, gloss:kayıp} ise miktar, bütünlük veya değerin bir bölümünü yitirmeyi taşır. İnsan böylece 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:zamanın akışı} ile zaman boyunca aşınan ve süre geçtikçe fark edilen bir değer kaybı içinde görünür. Bu bağlantı zamanın kaybın tek sebebi olduğunu kurmaz; sürenin, eksilmeyi nasıl biriktirip açığa çıkardığını gösterir.

102:1'deki biriktirme yarışı bu zamanla aşınan görüntüyü ticari bir yüzle karşılaştırır. {ar:خُسْرٍ, tr:husr, gloss:kayıp}, alım satım sonunda başlangıç anaparasının bir bölümünün yitirilmesini düşündürebilir; anapara yerinde kalsa bile beklenen kazanç doğmadığında işlem yine kayıp sayılır. 104:2'deki malı yığıp sayma hareketi birikimi gözle görülür bir hesap düzenine bağlar: {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} hesaba giren görünen özne, {ar:لَفِى, tr:le-fî, gloss:içindedir} ise hayatı o negatif bakiyenin içine yerleştiren harekettir. Böylece 102:1'in yarış hâli 104:2'nin yığma ve sayma işlemiyle somutlaşır. Bu ticari çerçeve, 102:1 ve 104:2'nin açtığı bağlantıyı gerçek bir muhasebe iddiasına dönüştürmeden genel insan kaybının bir görünüşü olarak belirginleştirir; kaybı para ve piyasa ile sınırlı bırakmaz.

## Karşılık Veren İş

103:3, kayıp hükmünün karşısına konan yönelişin nasıl kurulduğunu gösterir. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar} içte güvenip tasdik etmeye bir dayanak verir; {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} bu kabulün yönünü gerçeği ayakta tutacak şekilde belirler. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} yönelişi dışarıda gerçekleşen niyetli eyleme taşır; {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyi işler} bu eylemin bozulmayı artırmayan, yerli yerinde ve sağlam sonuçlara yönelmesini sağlar. Böylece 103:2'deki genel kayıp, içteki tasdik ile dışta gerçekleşen uygun işin birlikte karşılık verdiği bir süreç olarak duyulur. Bu bağ kaybı imanla özdeşleştirmez; ilk cümlenin hükmünü koruyarak onun karşısındaki tutarlı hayat yönünü gösterir.

Bu yöneliş emeğin dönüşünü de görünür kılar. 103:3'teki {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} işi yapan kişinin çabasını öne çıkarır; 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:zamanın akışı} bu çabadan çıkan ve alınabilen getiriyi düşündürür. 103:3'teki {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} ise bu getirinin bir kimseye düşen ve savunulabilir pay olarak görülmesini sağlar. {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} doğrudan ücret demek değildir; fakat iş karşılığı ödenen payı ve emeğin yürüttüğü çalışma topluluklarını düşündüren kullanımlar, emek ile hak edilen dönüş arasındaki bağı somutlaştırır. Ortaya konan iş karşılığa veya çekilip alınabilir bir ürüne dönüşmediğinde arada bir açık kalır. İnsan taşıdığı yeteneği amaçlı eyleme çevirmediğinde bu yetenek sermaye gibi eksilebilir; amaçlı iş ve emeğin karşılığı ise bu eksilmeye karşı imkân açar. Bu çerçeve emeğin dönüşünü gösterirken onu yalnız ücret hesabına kapatmaz.

## Miktar ve Karşılık

Bu açık ölçülebilir bir miktara dönüştüğünde {ar:خُسْرٍ, tr:husr, gloss:kayıp}, olması gereken miktarın aşağı çekilmesini ve teslim edilen payın kısa tutulmasını duyurur. 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:sıkarak verim çıkarma} önce baskının hareketini verir: bir şeyden sıvı çıkana kadar bastırılır ve gizli açık dışarı çıkar. 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} için açılan sofra yaygısı ve üzerine yığılmış yiyecek, birikmiş miktarı sayılabilir ve dağıtılabilir hâle getirir. Yine 103:3'teki {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} bir şeyi işe koşma ve kullanma yönüyle, bu baskı altında kalan kapasitenin işletilip işletilmediği sorusunu açar. Asrın akışı durdurup yararı alıkoyan yönü devreye girdiğinde malın veya faydanın dolaşıma girmemesi de ölçülebilir bir açığa dönüşür. Böylece sıkma açığı görünür kılar, yığın onu sayılabilir hâle getirir, kısa teslim ise açığın başkasına ulaşan biçimini gösterir; her biri 103:2'deki kayıp hükmüne kendi katkısıyla döner.

Ölçüdeki açık, daha sert bir alışveriş hesabı gibi de hissedilebilir. 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:çıkan verim} bir şeyden çekilip alınan getiriyi, 103:3'teki {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} belirli bir kimsenin sahip olduğu ve geri alınması gereken hakkı, {ar:عَمِلُوا۟, tr:amilû, gloss:iş yaptılar} ise kişiler arasındaki iş görme ve işlemleşmeyi düşündürür. 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} içindeki sert taşlı zemin, verimin kolayca alınmadığı direnci gösterir; aynı sözdeki acı aloe benzeri öz, geri dönüşün tatsız ve yakıcı bir yoğunlaşmaya dönüşen yüzünü verir. Bu maddi görüntü, 103:2'deki genel insan kaybını hakkın ve emeğin gerçek bir dönüş beklediği sert bir hesap alanına yaklaştırır. Bağlantı böylece ticari bir görünüş kazanır; âyetin bütününü zorunlu olarak tek bir alışveriş işlemine indirgemez.

Bu hesapta mesele yalnız malın geri dönmesi değildir; 103:3'teki insan ve hak ilişkisi kaybı insanlar arasındaki ortak ölçüye taşır. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} insan türünü, türün tek üyelerini ve aralarındaki topluluğu birlikte adlandırır. Aynı âyetteki {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} haklılık üzerinde çekişmeyi ve gerçeği ayakta tutmayı, {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyi işler} barıştırma ve uzlaştırmayı düşündürür. {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine öğüt verdiler} tek taraflı bir ilan değil, insanların birbirine yönelttiği karşılıklı sözdür. Bu söz, ortak ölçü bozulduğunda gerçeğin, hak edilen payın ve onarıcı ilişkinin yeniden kurulmasına doğru hareket eder. Aynı bağlamdaki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır}, kayba uğrayan hakkın karşısına orantılı karşılık veya hukuki ödetme sahnesini de getirebilir; hak edilen payın geri verilmesi ve karşılığın sınırlı tutulması bu bağlamsal cevabın yönünü açıklar. Bu yön, 103:3'te özel bir dava hükmü kurmaz.

İstisnanın gücü, 103:3'teki erdemlerin yan yana durmasından değil, her birinin aynı karşılıklı ağda ayrı bir iş görmesinden doğar. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan}, yabancılık ve ürküntünün kalkıp yakınlık ve rahatlığa dönüşebilen kapasitesini verir. {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar} bu kapasiteye yerleşmiş güveni ve tasdiki, {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} zor zamanda paniğe kapılmadan kendini tutmayı ekler. Tekrarlanan {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine öğüt verdiler} sözü ise yakınlığı eyleme çevirir: doğru söz ve sabrı bir kişiden diğerine taşır. {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} ile sabır böylece bir kişinin içinde saklı kalmayan ortak bir ölçü kurar. Paylaşım anlık rahatlık değil, sürdürülen bir sorumluluktur; bu ağın işlemediği yerde insanın kaybı tek başına taşınır ve ortak ölçü bozulur. Buradaki dayanıklılık, 103:2'nin hükmünü değiştirmeyen yerel bir karşılıklılık olarak kalır.

Yakınlık bozulduğunda kayıp miktarın azalmasının yanında insan ile yaptığı iş veya ilişki arasındaki uyumsuzluk olarak da görünür. 103:3'teki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} sözünün taşıdığı tanışıklık ve yakınlık yönü, bir kişiyle bir şeyin birbirine uygun hâle gelmesini düşündürür. Aynı âyetteki {ar:ٱلصَّٰلِحَٰتِ, tr:sâlihât, gloss:iyi işler} ile uzlaşma yönü, insanların yeniden elverişli bir ilişki içinde durmasını sağlar. Bu temas altında {ar:خُسْرٍ, tr:husr, gloss:kayıp}, insanın ilişki içinde yerini bulamamasına, yaptığı eylemin amacına uymamasına ve uyumsuzluğun yakınlığı aşındırmasına bağlanabilir. Uygunluk burada kelimenin zorunlu tek karşılığı değildir; 103:3'teki barışma yönü, kaybın toplumsal olmayan bir eksilme olarak da kalabileceği sınırıyla birlikte ihtiyatlı bir imkân açar.

103:3'teki sabır, gönüllü dayanmanın yanında dışarıdan uygulanan bir tutmanın görüntüsünü de açar. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} sakin biçimde kendini tutan özne kadar, başkasının elinde alıkonulan kişiyi de sahneye getirir. {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} içindeki zorunlu tutma, infaz veya yemin için kişinin iradesini sıkıştıran bir gözetim gibi okunabilir. 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:alıkoyup geri alma} imgesi bu tutmaya eklendiğinde insanın hareket alanı ve hakkı geri verilmeyerek baskı altında tutulur. Bu bağlantı, 103:2'deki genel kaybı dışarıdan dayatılan tutmanın öznenin eyleme gücünü daraltması olarak somutlaştırır; belirli bir olayın veya hukuki kimliğin kendisini tanımlamaz.

Tanıdık yakınlık ile yerleşmiş güven arasındaki fark, kaybın görünmeyen açığını belirginleştirir. 103:3'teki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} ve rahatlık hissi insanı sosyal olarak gevşemiş gösterirken, aynı âyetteki {ar:ءَامَنُوا۟, tr:âmenû, gloss:inandılar} alışkanlıktan ayrılan güveni ve doğrulayan iç kabulü kurar. Bu ikinci zemin oluşmadığında {ar:خُسْرٍ, tr:husr, gloss:kayıp}, dışarıdan güvenli görünen yakınlığın altında kalan teminatsız açıklığı görünür kılabilir. Bağlantı yakınlık ile imanı özdeşleştirmez; yalnızca tanıdık rahatlığın her zaman güvence taşımadığını gösterir.

103:3'teki hak ve ölçü teması insanı başka birinin görüşünde küçülen bir suret olarak da görünür kılabilir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan}, göz bebeğinin karanlık bölümündeki küçük insan biçimli yansımayı çağrıştırdığında, bir insanın başka birinin görüş alanında olduğundan küçük veya eksik temsil edilmesi düşünülebilir. {ar:خُسْرٍ, tr:husr, gloss:kayıp} bu küçülmeyi niceliksel bir eksilme olarak, {ar:ٱلْحَقِّ, tr:el-hakk, gloss:gerçek ve hak} gerçeğe uygun sözün çarpılmış temsili düzeltme gücü olarak tamamlar. Böylece ortak ölçü ve doğru sözle yeniden görünür hâle getirilebilecek bir insanlık payı belirir. Bu bağlantı insan sözünü doğrudan gözdeki suretle tanımlamaz; 103:3'teki hak, ölçü ve karşılıklı sözün açtığı temsil alanıyla sınırlıdır.

## Baskının İçinden Görünen Açık

İnsan hayatı sıkıştırıldığında içindeki eksik yüzeye çıkabilir. 103:2'deki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} ile {ar:خُسْرٍ, tr:husr, gloss:kayıp} yan yana geldiğinde sıkıştırılan hayatın gizli açığı yetersiz veya boşa giden bir ürün olarak görünür. 103:1'deki {ar:وَٱلْعَصْرِ, tr:vel-asr, gloss:sıkarak verim çıkarma} baskıyı bir şeyden öz çıkarana kadar yoğunlaştırır ve süre içinde birikmiş açığı görünür hâle getirir. Asr ile eksilen getiri birlikte okunduğunda insan emeğinin ve yaşantısının değerli bir dönüşe çevrilip çevrilmediği sorusu belirir. 103:3'teki {ar:ٱلصَّبْرِ, tr:es-sabr, gloss:sabır} için açılan acı aloe benzeri öz, baskıdan geriye kalan tortunun tatsızlığını; sabır sözünün dayanma yönü ise bu acının altında ayakta kalma çabasını taşır. Sıkma ve acı öz, 103:1 ve 103:3'teki temaslara bağlı duyusal bir benzetme olarak 103:2'deki kayıp hükmünün basıncını hissettirir; bu görüntü zamanı borç defteri, sabrı da acı bir madde olarak tanımlamaz.

Bu basınç altında beliren açık, 83:3'teki ölçü bağlantısıyla başkasına ulaşan miktar üzerinden sınanabilir. {ar:خُسْرٍ, tr:husr, gloss:kayıp}, olması gerekenden az yapan eylemi ve teslim edilen miktardaki açığı taşır; 83:3 bu açığı başkasının hakkını kısa vermek olarak görünür kılar. Ölçünün hangi mala, kime veya hangi ölçeğe ait olduğu açık bırakılır, fakat teslim edilenle borçlu olunan arasındaki fark belirginleşir. 26:181'deki tam ölçü buyruğu bu farkı bir doğruluk standardıyla aydınlatır: {ar:خُسْرٍ, tr:husr, gloss:kayıp}, karşısına konmuş standarda göre verilmesi gerekenden azını verme hâlini taşıyabilir. Böylece 26:181'in açtığı bağ genel kaybı düzeltilebilir bir kısa teslim olarak gösterir; bu bağlantı 103:2'nin içinde hazır bir tartı sahnesi kurmaz.

103:3'ün daha sonra açtığı karşılıklı alan, 83:3'teki kısa teslimi geriye dönük olarak ölçülebilir kılar. 83:3'teki eksik ölçü ile 90:17'deki sabra karşılıklı öğüt, verilen miktarı ve onu düzeltme sorumluluğunu birlikte düşündürür. {ar:خُسْرٍ, tr:husr, gloss:kayıp}, teslim edilen miktardaki açığı bildirirken, 90:17'deki {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine öğüt verdiler} bu açığın birlikte gözetilmesini sağlar. Böylece daha önce genel kalan kayıp, kısa teslim ve topluca hesap verilebilir bir açık olarak görünür; ilk hüküm yerinde kalır. Aynı iki bağ kaybı iki kişi arasındaki dengesizliğe ve onu onarmaya çalışan ortak bir pratiğe açar. Ortak düzeltmenin yönü belirir, fakat 83:3 ve 90:17 birlikte özel bir borçlu ya da ölçü tayin etmez.

Kayıp dışarıya verilen miktarla sınanabildiği gibi içeriden fark edilebilir de. 79:35'teki hatırlatma ve uyarı ihtiyacı, {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} sözünün görüp fark eden yüzüyle karşılaştığında insanın içinde bulunduğu kaybı başka birinin doğru sözüyle görünür kılar. Böylece 79:35'in katkısı kaybı üretmek değil, onu algılanabilir bir teşhise dönüştürmektir. 75:14'teki insanın kendi kendine tanıklığı aynı taşıyıcıyı içten bir fark edişe bağlar. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} bir durumu görüp seçebilen kapasiteyi, {ar:خُسْرٍ, tr:husr, gloss:kayıp} genel eksilmeyi taşır; insan yaşadığı kaybı kendi sorumluluk alanında görebilir. 75:14'ün açtığı fark ediş, kaybı görünür kılar ve tek başına iyileşme sözüne dönüşmez.

90:17'deki karşılıklı sabır öğüdü ile 79:35'teki uyarı birlikte düşünüldüğünde, 79:35'in görünür kıldığı açık başka bir insanın sözüyle daha seçilebilir hâle gelir. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan}, kaybı fark edebilen taşıyıcıdır; 90:17'deki karşılıklı hitap bu fark edişi tek kişinin içine kapatmadan paylaşılabilir kılar. Bu temas, insanın kaybı kendi başına göremeyeceğini ileri sürmez; doğru sözün mevcut fark edişi keskinleştirebileceğini gösterir.

İnsan sözünün yabancılık ve ürküntünün kalkıp yakınlık ve rahatlığa dönüşen yönü, 59:16'da görülen yabancılaştırıcı telkinle karşılaştığında kaybın sosyal yüzünü açar. {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} burada yalnız tür adı değil, yakınlık taşıyabilen bir varlıktır; 59:16'daki yabancılaştırma bu kapasitenin karşısındaki basıncı sağlar. Bu temasın katkısı, kaybı başkalarıyla kurulan tanıdık yakınlığın aşınması ve birlikte olma yetisinin zayıflaması olarak duyurmaktır. 90:17'deki karşılıklı sabır öğüdü aynı kapasiteyi yeniden işler hâle getirebilecek ortak bir alan açar: {ar:تَوَاصَوْا۟, tr:tevâsav, gloss:birbirlerine öğüt verdiler}, insanların birbirine destek vererek doğru sözü ve sabrı taşımasını gösterir. Böylece sosyal hareket 103:2'deki kayıp hükmünün yanına bir onarım yolu koyar; bu bağlantı insan kelimesini yalnız arkadaşlık anlamına indirgemez.

{ar:لَفِى, tr:le-fî, gloss:içindedir} sözünün içeri yerleştiren hareketi, 90:4'te insan hayatının zorluğuna verilen temasla birleşince {ar:خُسْرٍ, tr:husr, gloss:kayıp} kelimesini baskı altında kuşatan bir ortam gibi duyurur. 90:4'teki güçlük kayıp alanına basınç verir; 90:17'deki karşılıklı sabır ise o alanın içinde, eksilmenin yalnız bir tartıda görülen miktara bağlı kalmayan bir tutunma biçimini açar. Böylece biri baskının çevrelediği durumu, diğeri o basınç içinde karşılıklı dayanmayı gösterir. Bu iki temasın birbirine nasıl bağlandığı açık kalırken, zamanın kaybı doğurduğu, yalnızca onu açığa çıkardığı veya onu çerçevelediği kesinleştirilmez; 90:4 ve 90:17'nin her biri kendi katkısıyla 103:2'deki kayıp alanına döner.

## Temasların Birbirini Açtığı Yer

102:1'deki birikim yarışı önce {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} taşıyıcısına dönerek insanı zaman içinde eksilen görünür bir varlık hâline getirir. 104:2'deki yığıp sayma hareketi bu görünür eksilmeyi {ar:خُسْرٍ, tr:husr, gloss:kayıp} kelimesinin ticari yüzünde geri dönmeyen sermaye olarak belirginleştirir; {ar:لَفِى, tr:le-fî, gloss:içindedir} sözü hayatı o açık alanına yerleştirir. Aynı açık 79:35'te uyarıyla söz içinde görünür olur, 90:4'teki güçlükte ise kaybı kuşatan bir basınç kazanır. Bir görüntü insanın zaman içinde aşınmasını kurar, ikincisi bu aşınmayı yığılmış ve sayılmış bir hesapta somutlaştırır, üçüncüsü fark edişi mümkün kılar, dördüncüsü o fark edişi güçlükle çevrili bir alana yerleştirir. Böylece görünür insan, sözle fark edilen insan, baskı altındaki eksilme ve işlem biçimindeki kayıp birbirini silmeden aynı hükmü farklı yönlerden açıklar. Bu bileşim kaybı güvenlik, belirli bir mülkiyet hakkı veya kaçışı olmayan ağır sıkıntı olarak ayrıca tanımlamaz; her görüntü kendi bağının sınırında kalır.

İçte görülen kayıp ile dışarıya verilen pay 75:14 ve 83:3'te yeniden karşılaşır. 75:14'teki iç tanıklık, {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan} sözünü insanın kendi içindeki fark edişe bağlar; 83:3'teki hak ve ölçü teması {ar:خُسْرٍ, tr:husr, gloss:kayıp} kelimesini verilmesi gerekenin altında kalan dış sonuca bağlar. İlki kaybın kişinin kendi sorumluluk alanında görülmesini, ikincisi başkasına ulaşan payda sınanmasını sağlar; birlikte kaybı bilinebilir ve sınanabilir kılar. Bu iki temas, 103:2'deki genel hükmün iki görünürlük yoludur ve hiçbirini kaybın bütünü hâline getirmez.

28:67'de tövbe, iman ve salih amel ile başarı arasındaki karşıtlık, {ar:خُسْرٍ, tr:husr, gloss:kayıp} kelimesini şiddetli ama teşhis edilebilir bir açık olarak görmeye imkân verir. İnsan hüküm altında oluşunu adı konulabilir bir noksanlık olarak fark ederken, 28:67'deki tövbe, iman ve yerinde eylem bu kayıp hâlinin karşısında onu onarabilecek kapasiteler olarak belirir. Bu bağlantı 28:67'nin iyileşme düzenini 103:2'nin sözlük anlamına dönüştürmez; genel kaybın yanında bir toparlanma karşılığı görünür kılar.

</source_prose>
