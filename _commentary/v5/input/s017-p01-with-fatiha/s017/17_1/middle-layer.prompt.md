# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:1**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.middle.claims.json`

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
- Refer to source paragraphs as `17:1 ¶N`.

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

`(17:1 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:1",
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
        "citation": "(17:1 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_1/17_1.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_1/17_1.middle.claims.json \
  --ayah-ref 17:1
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_1/17_1.prose.editorial.tr.md`

<source_prose>
## Gece Yolunun Çizgisi

{ar:سُبْحَٰنَ, tr:subḥāna, gloss:tenzih ve yüceltme} Allah’ı eksiklikten uzak tutan övgüyle ayeti açar; hemen ardından gelen {ar:ٱلَّذِىٓ, tr:alladhī, gloss:o ki} bu övgünün öznesini {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} eylemiyle tanıtır. Dördüncü bâbın ettirgen mazi biçimi, gece taşımasını tamamlanmış bir ilahî eylem olarak verir: Allah kulunu geceleyin götürmüştür. Tenzih, bu olağan sınırları aşan tasarrufu Allah’a bedensel bir yer değiştirme yüklemeden anlatır. {ar:بِعَبْدِهِۦ, tr:bi-ʿabdihi, gloss:O’nun kuluyla} içindeki bi, kulu hem eyleme eşlik eden kişi hem de taşınan katılımcı olarak fiile bağlayabilir; edatın ada bitişmesi bu yakın dilbilgisel teması gösterir, yeni bir bi anlamı kurmaz. {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} bi ile mecrur olsa da kimin taşındığını fiilin anlamı belirler. Sahiplik eki yolcuyu Allah’la bağı içinde tanımlar: yaratılmışlık ve kulluk ilişkisi bu aidiyete katılır, hukuki mülkiyet değil.

İlk {ar:مِّنَ, tr:min, gloss:-den} gece hareketinin bilinen çıkış yerini, ardından gelen belirli tekil mecrur {ar:ٱلْمَسْجِدِ, tr:al-masjid, gloss:mescid} ise secde ve ibadet için ayrılmış mekânı verir. Bu biçim ilk minin yönettiği bilinen bir kaynak terkibi kurar; belirli mecrur {ar:ٱلْحَرَامِ, tr:al-ḥarām, gloss:kutsal ve korunan} sıfatı da mescid adıyla belirlilik ve çekim uyumu gösterir, tek başına yeni bir yer teşhisi getirmez. Mescid aynı zamanda toplu ibadet için ayrılmış bir alanı ya da bu amaçla kurulmuş yapıyı anlatabildiğinden, burada ibadet yeri ile yapı ihtimali birlikte duyulur; belirli bir mimari biçim çizilmez. Bu ilk menzil sınırları ve yakın çevresiyle korunan kutsal bir mekândır. İkinci {ar:ٱلْمَسْجِدِ, tr:al-masjid, gloss:mescid} ise {ar:إِلَى, tr:ilā, gloss:-e doğru} tarafından hedef yapılır. Aynı ibadet yeri adının iki uçta yinelenmesi, yolculuğu aynı yapı içinde değil, secde ve toplu ibadetle tanımlanan iki ayrı durak arasında kurar.

Hedefin {ar:ٱلْأَقْصَىٰ, tr:al-aqṣā, gloss:en uzak} diye nitelenmesi, onu yalnız uzak bir yer değil, bu güzergâhın en uzak ucu olarak sunar. Sözcüğün uzak yan ya da son sınır anlamındaki ayrı kullanımı, mesafeyi erişilen bir eşik gibi duyurur; bu ölçü çıkış ile hedef arasındaki güzergâh içinde kalır, mutlak mesafe ya da harita belirlemez. Böylece korunan başlangıçla uzak uç aynı çizginin iki farklı niteliğini taşır; uzaklık aralarında değer sırası kurmaz. {ar:ٱلْمَسْجِدِ ٱلْحَرَامِ, tr:al-masjidi al-ḥarāmi, gloss:kutsal mescid} ortak alanına erişimin engellenebilmesi de bu çıkışı korunan bir eşikten geçiş olarak okumayı destekler (22:25). Bu benzerlik erişim engeliyle sınırlıdır; 22:25’teki engel odak yolculuğunda yaşanmış bir anlaşmazlık olarak aktarılmaz.

Odaktaki iki ibadet yeri arasındaki gece hareketi, geri verme ve yeniden dönüş sözleriyle tarih içinde yinelenen bir çizgiye bağlanır (17:1, 17:6): {ar:رَدَدْنَا, tr:radadnā, gloss:geri çevirdik} ile {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:yeniden dönüş} bu sırayı başlatır. Ardından aynı {ar:ٱلْمَسْجِدِ, tr:al-masjid, gloss:mescid} adının ve giriş fiilinin yinelenmesi gelir (17:7): {ar:وَلِيَدْخُلُوا الْمَسْجِدَ كَمَا دَخَلُوهُ أَوَّلَ مَرَّةٍ, tr:wa-li-yadkhulū al-masjida kamā dakhalūhu awwala marratin, gloss:mescide ilk girdikleri gibi yeniden girsinler} ilk girişin tekrarını, hemen ardından gelen {ar:وَلِيُتَبِّرُوا۟ مَا عَلَوْا تَتْبِيرًا, tr:wa-li-yutabbirū mā ʿalaw tatbīrā, gloss:üstün geldiklerini bütünüyle yıksınlar} ise yıkımı bildirir. Yıkımın odaktaki {ar:بَٰرَكْنَا حَوْلَهُۥ, tr:bāraknā ḥawlahu, gloss:çevresini bereketli kıldık} ile yan yana gelişi, bereketli hedefi insan davranışı ve tarihsel sorumlulukla birlikte düşündürür (17:1, 17:7). Bu yan yanalık, odak menzillerden birinin yıkıldığını ileri sürmez. Koşullu {ar:عُدْتُمْ عُدْنَا, tr:ʿudtum ʿudnā, gloss:siz dönerseniz Biz de döneriz} karşılığı bu tarihsel diziyi sürdürür (17:8); korunan menzilin anlamı böylece tarih dışı bir güvenceye kapanmaz. Bu yankıda sonraki mescid odaktaki Haram ya da Aksa diye belirlenmez ve iki ayetin aynı olayı anlattığı söylenmez (17:1, 17:7).

Uzak hedefin tarifi, amaç bildiren lām’dan önce tamamlanır: ikinci {ar:ٱلَّذِى, tr:alladhī, gloss:ki} ile açılan cümle {ar:بَٰرَكْنَا, tr:bāraknā, gloss:bereket verdik} eylemini ve {ar:حَوْلَهُۥ, tr:ḥawlahu, gloss:çevresinde} sözünü hedefe bağlar. Birinci çoğul özne ekli mazi, çevredeki bereketi tamamlanmış ilahî bir eylem olarak sunar; bereketin yerleşmiş hayır ve artış anlamı hedef çevresine derinlik katar, miktarını ise belirlemez. {ar:حَوْلَهُۥ, tr:ḥawlahu, gloss:çevresinde} tek noktadan çevreye açılan, sınırı belirtilmemiş bir alan kurar. Durum ya da yer değişimini anlatan ayrı kullanım da gece hareketi ve bereket eylemiyle yan yana gelince varış çevresini değişmiş bir yer gibi duyurur; bu ek çağrışım yakınlık anlamını gölgelemez ve her şeyin fiziksel olarak değiştiğini ileri sürmez.

Ardından gelen amaç lām’ı, yolculuğu {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} gösterme eylemine yöneltir. Dördüncü bâbın ettirgen biçimindeki “biz” gösteren faili, ekli zamir ise görecek kişiyi, kulu belirtir. İkinci {ar:مِنْ, tr:min, gloss:bir kısmından} mekân bildiren ilk minden farklı olarak {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:işaretlerimiz} kümesinden seçilmiş bir bölümü gösterir. Çoğul iyelik eki işaretleri ilahî konuşana bağlar; görünür belirtiler başka şeylere delalet eden kanıtlar olarak da okunabilir. Böylece kul bütün işaretlerin dökümünü değil, içeriği tek tek açıklanmamış seçilmiş bir payı görür; yolculuk da yalnızca yol kenarındaki manzaraya indirgenmez. Musa’ya büyük işaretleri gösterme amacı da görme ile işaret arasındaki bu bağı belirginleştirir (20:23), fakat o sahne bu gece yolculuğuyla aynı değildir.

Aktarılan iki varyant, {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} biçimindeki gösterme ilişkisinin failini başka türlü kurar: birinde Allah kulu gören özneye yaklaştırılır, ötekinde ettirgen gösterme korunurken özne değişir. Bu varyantlar, kimin gösterdiğini ve kimin gördüğünü ayırt ettirir; kanonik biçimin yerine geçmez. Korunan ibadet durağından en uzak ibadet yerine yönü belli gece hareketi, bereketle nitelenmiş varışın ardından yolcuyu seçilmiş işaretlere yönelten amaçta bir açıklanma geçidine dönüşür. Bu metinsel bağlantıda kutsal geçiş okumasını taşıyan tek bir yer adı değil, fiilin faili, iki menzilin yönü, bereketli çevre ve gösterme amacının kurduğu sıradır.

Uzun eylem cümlesinin sonunda {ar:إِنَّهُۥ, tr:inna-hu, gloss:şüphesiz O} güçlü tasdikle özneyi yeniden açılışa bağlar. Ardındaki {ar:هُوَ, tr:huwa, gloss:O} iki belirli sıfattan önce durur; hem yüklemi ayıran açıklayıcı zamir hem de sınırlayıcı vurgu olarak okunabilmesi dilbilgisel bir açıklık bırakır. {ar:ٱلسَّمِيعُ, tr:al-samīʿ, gloss:her şeyi işiten} ile {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:her şeyi gören} Allah’ın işitmesini ve görmesini bildirir. İşitme, anlamlı sözün içeriğini kavramaya; görme, seçilmiş işaretlerden içgörüye ve doğrulanmış anlayışa açılabilir. Bu iki algı alanı kulun aldığı görmeyi ilahî görüş içinde anlamlı kılar; kabul ya da uygun karşılık ihtimali açık kalır. Ayet belirli bir söz, cevap veya işaretlerin açıklamasını vermez.

## Gecenin İçinden Görünene

Gösterme amacı gece vakti içinde kurulduğundan, {ar:لَيْلًا, tr:laylan, gloss:gece vakti} zarfının sınırları önem kazanır. Belirsiz mansub biçim yolculuğun ne zaman yapıldığını bildirir, tarih ya da ölçülmüş süre vermez; gece sözü gündüzün karşıtı olan vakit bölümünü taşır ve tek bir geceye ya da gecelere işaret edebilmesi burada süre ölçüsü oluşturmaz. {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} bir kişinin gece yol almasını ve birini yanında gece götürmeyi anlatır; geceye girmek ya da gece vaktine erişmek, ayrıca gece yolcusunu adlandırmak anlamları zaman ile yolcuyu aynı eylemin çevresinde toplar. Gece kelimesinin kökeni üzerine farklı açıklamalar aktarılır; bu tartışma zarfın işlevini değiştirmez. Parçalı-gece biçimindeki varyant da kanonik {ar:لَيْلًا, tr:laylan, gloss:gece vakti} zarfının yerini almaz.

Bu zaman adı surede daha geniş bir gece-gündüz düzenine katılır. Gece ile gündüz iki işaret diye anılır; gece işareti silinir, gündüz işareti görünür kılınır: {ar:مَحَوْنَآ ءَايَةَ ٱلَّيْلِ, tr:maḥawnā āyata al-layli, gloss:gecenin işaretini sildik} karşısında {ar:ءَايَةَ ٱلنَّهَارِ مُبْصِرَةً, tr:āyata al-nahāri mubṣiratan, gloss:gündüzün işaretini görünür kıldık} yer alır (17:12). Gündüzün iki kez adlandırılması, gece ve gündüzü aynı işaret düzeninin ayrı evreleri olarak belirginleştirir (17:12). Rızık arama, yılları sayma ve işlerin ayrıntılı biçimde belirlenmesi de bu düzene bağlanır (17:12); odaktaki gece yolculuğu böylece daha geniş bir zaman dünyasında duyulur. Gecenin karanlığı görünür işaretlerle karşıtlık kurar, ancak bu karşıtlık yolculuğa saklanma amacı yüklemez. Gündüz için kullanılan {ar:مُبْصِرَةً, tr:mubṣiratan, gloss:görünür ya da görmeye elverişli} nitelemesi (17:12), odaktaki {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} ve kapanıştaki {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:her şeyi gören} ile ortak bir algı alanı açar: gündüz görünürlüğü, görmenin sağlanması ve ilahî görme birbirine yaklaşır. Sözcüklerin biçimleri özdeşleşmez ve iki ayetteki işaretler aynı içerik sayılmaz.

Gece ile görünür gündüz arasındaki ayrım, insanların bu ritim içindeki yerini de duyurur. Gece dinlenme, gündüz görünürlük için anılır; ikisi işaretlerle ve işiten insanlarla ilişkilendirilir (10:67). Bu karşıtlık, odaktaki {ar:لَيْلًا, tr:laylan, gloss:gece vakti} sözünü daha geniş zamansal-algısal bir düzene yerleştirirken odağın gecesine dinlenme işlevi yüklemez (10:67). Gece-gündüz düzenini işaret sayanlar insandır; kapanıştaki {ar:ٱلسَّمِيعُ, tr:al-samīʿ, gloss:her şeyi işiten} ise Allah’a aittir. Gözle görünür gündüz de Allah’ın {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:her şeyi gören} oluşuyla özdeşleşmez. Böylece insanların işittiği ritim ile Allah’ın işitmesi ve görmesi yan yana gelir; iki özne birbirine karışmaz (10:67).

Geceden şafağa uzanan başka bir vakit çizgisi, tanıklanan fecr okuyuşunu anarak algı çerçevesini genişletir: {ar:وَقُرْءَانَ ٱلْفَجْرِ ۖ إِنَّ قُرْءَانَ ٱلْفَجْرِ كَانَ مَشْهُودًۭا, tr:wa-qurʾāna al-fajri inna qurʾāna al-fajri kāna mashhūdan, gloss:fecr okuyuşu tanıklanır} ifadesi bu sınır vaktini belirginleştirir (17:78). Odaktaki gece taşınması ve kulun görmesi, bu fecr çerçevesiyle birlikte daha geniş bir gece-fecr ritmi içinde okunabilir (17:78). Bu yakınlık zamansal ve algısaldır: ortak ritüel ya da aynı olay ileri sürülmez; 17:79’daki yükseltilmiş makam da bu okumaya eklenmez, çünkü ilişki 17:78’in gece-fecr çerçevesiyle sınırlıdır (17:78, 17:79).

Bu görünür zaman çizgisinin yanında, gece örtülme ve açığa çıkma çağrışımına da kapı aralar. {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} için bir sözü, bilgiyi, işi ya da iç durumu başkalarının bilgisinden saklı tutma anlamındaki ayrı kullanım vardır; başka bir kullanımda üstteki şey kaldırılır ve altındaki görünür olur. Gecenin örtücülüğünü söyleyen ifade (92:1), bu iki sözlük kolunu odaktaki {ar:لَيْلًا, tr:laylan, gloss:gece vakti} ile {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} gösterme amacı ve seçilmiş {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:işaretlerimiz} arasında buluşturur. Saklılıktan seçilmiş işaretlerin açılmasına uzanan bu algı hareketi, işaretlerin kavranma eşiğini derinleştirir. Sözlük bağlantısı karanlığın sürüp sürmediğini, gösterenin niyetini ya da tanık bulunup bulunmadığını belirlemez.

## Yolcunun Alıcılığı

Gece taşınan ve görmesi sağlanan kişinin {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} diye adlandırılması, yakın sure bağlamında alıcılık ile rehberliği alma ve taşıma ilişkisini buluşturur. Musa’ya {ar:ءَاتَيْنَا, tr:ātaynā, gloss:verdik} ile {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} verilmesi ve onun İsrailoğulları için {ar:هُدًى, tr:hudan, gloss:hidayet} kılınması ayrı bir ilahî armağan sahnesidir (17:2). Odaktaki {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} gösterme eylemi bu topluluğa yöneltilen rehberliğin eşiğinde okunabilir (17:2); gösterilen işaretler Kitap’ın kendisi değildir ve gece yolcusu Musa ya da Kitap’ı aktarmakla görevlendirilmiş kişi olarak tanımlanmaz (17:1, 17:2). Ardından Nuh’la birlikte taşınanların soyuna değinen ifade, taşıma imgesini tek yolcudan kuşaklara genişletir (17:3): {ar:ذُرِّيَّةَ مَنْ حَمَلْنَا مَعَ نُوحٍ, tr:dhurriyyata man ḥamalnā maʿa Nūḥ, gloss:Nuh’la birlikte taşıdıklarımızın soyu}. Aynı ayetteki {ar:عَبْدًا, tr:ʿabdan, gloss:bir kul} ile {ar:شَكُورًا, tr:shakūran, gloss:çok şükreden} kulluk ve nimete şükürle karşılık verme temasını taşır (17:3). Musa, Nuh’la birlikte taşınanların soyundan gelenler ve odak yolcusu ayrı göndergelerdir (17:1, 17:2, 17:3). Bu armağan ve taşıma sahneleri alıcılık çizgisini genişletir; birbirlerinin ya da odakta gösterilen işaretlerin yerine geçmez.

Tekil {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} adı, cemaatin çoğul ibadet ve yardım diliyle başka bir ölçekte yankılanır. Fâtiha’da topluluk {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:yalnız sana kulluk eder, yalnız senden yardım dileriz} diye konuşur (1:5); “kul” adıyla “kulluk ederiz” fiili aynı sözlük ailesinde buluşur. Sayının değişmesi, tekil yolcunun yanına ibadet ile yardım dileğini birleştiren ortak bağımlılık sesini ekler (17:1, 1:5). Suredeki başka bir bağlam, Allah’la birlikte başka bir ilah edinmeme buyruğuyla kulluğu ayrıca belirler: {ar:لَا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhara, gloss:Allah’la birlikte başka ilah edinme} (17:22). Bu yankı bireysel ve toplu kulluk dilini ilişkilendirir, fakat yolcuyu Fâtiha cemaatine eşitlemez; yolculuk onların duasının cevabı ya da herkes için verilmiş bir örnek değildir (17:1, 1:5).

{ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} sözü taşınan kişiyi adlandırmanın yanında boyun eğerek hizmet etme ve kişinin kendini kulluğa verme anlamlarına açılır. Gece eylemini alan ve işaretleri görmeye çağrılan yolcu için bunlar, ayrı bir ibadet sahnesi kurmadan, alınan ilahî eyleme hizmet ve yönelişle karşılık verme biçimini duyurur. Sözcüğün saygı gören, yüce tutulan kişi anlamı da özel yolculuk ve seçilmiş gösterimle birleşerek onurlandırılma tonu ekler; toplumsal bir rütbe tayin etmez. Bu sözlük alanı yolcuyu ilahî eylemi alan, hizmet ve yönelişle karşılık verebilecek bir özne olarak kurar: alıcıdır, fakat ne edilgin bir yüke ne de hareketi kendi gücüyle gerçekleştiren kahramandır.

Bu konum, surede rızkın iki gruba ulaşması ve destekten yoksun kalma görüntüsüyle belirginleşir. {ar:نُّمِدُّ, tr:numiddu, gloss:sağlarız} biçimi Rabbin iki gruba rızık ulaştırdığını, bağışının da engellenmediğini bildirir (17:20). Bu iki gruba uzatılan imkân, odaktaki {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} ile ilahî iradeyle gerçekleşen taşınmanın kendi kendine üretilmeyen dayanağını düşündürür (17:1, 17:20). Buna karşılık, {ar:لَا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhara, gloss:Allah’la birlikte başka ilah edinme} buyruğunun yanında {ar:قَاعِدًا, tr:qāʿidan, gloss:oturur halde} ve {ar:مَخْذُولًا, tr:makhdhūlan, gloss:terk edilmiş} kalma görüntüsü belirir (17:22). Taşınan {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} yolcunun hareketi, oturma ve desteksizliğe karşı ilahî ihsanın mümkün kıldığı hareketi duyurur; bağımlılık burada destek ve itibar da taşır (17:1, 17:22). Bu iki bağlam tematik karşıtlık kurar, gece yolculuğunun nedeni-sonucunu değil; 17:20’deki iki grup da ibadet durumlarına göre ayrılmaz (17:20, 17:22).

Geceleyin birilerini yola çıkarma eylemi bu taşıma temasını başka bir sure sahnesinde çoğul kullara taşır: {ar:فَأَسْرِ بِعِبَادِى لَيْلًا, tr:fa-asri bi-ʿibādī laylan, gloss:kullarımı geceleyin yola çıkar} buyruğu geceyi bir yolcu grubunun sevkiyle birleştirir (44:23). Oradaki kullar odaktaki tekil kuldan ayrıdır; iki sahnenin ortaklığı geceleyin birini ya da bir grubu yola çıkaran eylemdir (17:1, 44:23). {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} sözcüğünün fiziksel güç ve sağlamlık anlatan ayrı kullanımı da yolcunun ilahî taşınış içindeki sebatını mecazen duyurur (17:1, 44:23). Bu çağrışım taşınma ilişkisindeki sebatı öne çıkarır, beden gücünü ya da kişinin kendi çabasını değil; kulluk ve tapınmaya yönelme anlamı da yolculuğun nedeni olarak verilmez (17:1, 44:23).

Taşınan kulun eyleyiciliğini koruyucu bir sınır da belirginleştirir: 17:65’te şeytanın Allah’ın kulları üzerinde yetkisi olmadığı bildirilir: {ar:إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌۭ, tr:inna ʿibādī laysa laka ʿalayhim sulṭān, gloss:kullarım üzerinde senin bir yetkin yok}. Bu beyan, gece sevkini anlatan {ar:فَأَسْرِ بِعِبَادِى لَيْلًا, tr:fa-asri bi-ʿibādī laylan, gloss:kullarımı geceleyin yola çıkar} sahnesi (44:23) ve açılıştaki {ar:سُبْحَٰنَ, tr:subḥāna, gloss:tenzih ve yüceltme} ile birlikte, yolcuyu ilahî eylem içindeki korunmuş bir kul olarak duyurur (17:1, 17:65). Bu yankı kulluğu korumanın sebebi yapmaz ve iki sahnenin kullarını özdeşleştirmez; Âdem ile şeytanın karşıtlığına ayrılan bağlam da buraya taşınmaz (17:61, 17:62, 17:63, 17:64).

Korunma dilinden sonraki yerel yankı, kuldan mekânın çevresine geçer. Başka bir olayda ateştekilerin ve çevrelerindekilerin kutsanmasıyla Allah’ın tesbihi yan yana gelir (27:8): {ar:أَنۢ بُورِكَ مَن فِى ٱلنَّارِ وَمَنْ حَوْلَهَا وَسُبْحَٰنَ ٱللَّهِ, tr:an būrika man fī n-nāri wa-man ḥawlahā wa-subḥāna llāhi, gloss:ateştekiler ve çevrelerindekiler kutsandı; Allah eksiklikten uzaktır}. 27:8’in katkısı, başka bir sahnede kutsanmış çevre ile tesbihin birlikteliğidir; oradaki kişiler 44:23’teki kullardan ayrıdır (27:8, 44:23). Bu birliktelik 17:1’in başındaki {ar:سُبْحَٰنَ, tr:subḥāna, gloss:tenzih ve yüceltme} ile hedef çevresini bildiren {ar:بَٰرَكْنَا حَوْلَهُۥ, tr:bāraknā ḥawlahu, gloss:çevresini bereketli kıldık} arasında övgü ve mekân ilişkisi kurar (17:1, 27:8); bu dilsel yankı iki olayı ya da yeri aynı mescide indirgemez.

Uzaklık ile bereket başka bir yönelişte buluşur: 21:71’de bereket verilen ülkeye doğru hareket anılır. Bu güzergâh, {ar:ٱلْأَقْصَىٰ, tr:al-aqṣā, gloss:en uzak} adının uzak uç değerini odaktaki {ar:بَٰرَكْنَا, tr:bāraknā, gloss:bereket verdik} eylemiyle aynı düşünce alanına getirir (21:71); bu yankı mesafe ölçmez ve ülkeyi Mescid-i Aksâ diye adlandırmaz. Ayrı bir seyahat sahnesi, bereketli yerleşimler arasında gece ve gündüz güvenle yol almaya yer verir (34:18); bu güzergâh çevreye yayılan bereket fikrini beslerken yerleşimleri odak hedefle özdeşleştirmez.

## Bereketin Akışı ve Tanıklık

Bu güzergâh imgesi, sözcüklerin ayrı anlam kollarıyla akışa doğru genişler. {ar:سُبْحَٰنَ, tr:subḥāna, gloss:tenzih ve yüceltme} hareket fiili değil, Allah’ı tenzih ederek yücelten isimdir; aynı sözcük ailesinin su ya da hava içinde yüzme ve akıcı ilerleme anlamı övgüye hareket dokusu ekler. {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} için küçük, akıp giden dere anlamındaki ayrı kullanım, ilk {ar:مِّنَ, tr:min, gloss:-den} ile {ar:إِلَى, tr:ilā, gloss:-e doğru} arasındaki kaynak-hedef çizgisine akış imgesini katar. Taşıma ve aktarma dizisi (17:2, 17:3, 17:4, 17:5, 17:6) ile bereketli yerleşimler arasında güvenli gece-gündüz yolculuğu (34:18), bu dereyi iletim güzergâhı gibi düşündürür. Odaktaki gece yolculuğu ile 34:18’deki seyahat ayrı eylemlerdir; su akışı bu iki pasajda anlatılan bir olay değil, sözlük çağrışımının mecazıdır (17:1, 34:18). Böylece akış benzetmesi iki hareketi birbirine çevirmeden rota boyunca taşıma hissi kazandırır.

Akış güzergâhına, bereketin su tutan küçük havuz anlamındaki ayrı kullanımı hedefte toplama işlemini ekler. Olağan okumada {ar:بَٰرَكْنَا, tr:bāraknā, gloss:bereket verdik} hedefin çevresine ilahî bereket yerleştirir; havuz çağrışımı bu çevreyi akışın tutulduğu bir durak gibi duyurur. {ar:حَوْلَهُۥ, tr:ḥawlahu, gloss:çevresinde} için kuyudan suyu yukarı çeken döner düzenek anlamındaki ayrı kullanım ise tutmayı değil, çekip yükseltmeyi karşılar. Böylece çevredeki bereketle buluşan iki ayrı sözlük imgesi akışı toplama ve suyu yukarı alma işlemlerini ayırt eder; aynı araç ya da fiziksel sıra kurmaz. Ayet bu sözcükleri gerçek bir düzenek olarak tarif etmez; çevrenin sınırını ve bereketin miktarını da belirlemez.

Akış, toplama ve yükseltme imgelerinin ardından alıcı uçta {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} belirir: odaktaki olağan anlamıyla kulun seçilmiş işaretleri görmesi sağlanır. Aynı sözcük biçiminin su içerek susuzluğu giderme, suya kanma anlamındaki ayrı kullanımı alıcıya yenilenme çağrışımı katar. Odaktaki {ar:مِنْ, tr:min, gloss:bir kısmından} {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:işaretlerimiz} içinden seçilen payın yolcuya gösterilmesi, susuzluğu giderme çağrışımıyla alıcıda tazelenme gibi de duyulur. Birleşik mecaz güzergâhta iletmeyi, hedef çevresinde suyu tutup yukarı çekmeyi, alıcıda yenilenmeyi yan yana getirir; bunlar ayrı sözlük çağrışımlarının kurduğu işlemlerdir, tek bir fiziksel dizi değildir. Odaktaki gösterme ve görünür işaretler olağan anlamlarını korur; 34:18 de su ya da susuzluktan söz etmez (17:1, 34:18).

Bu akış imgesine yakın ama ondan ayrı bir sözlük bağlantısı, uzatıp sağlama fiilinde görülür. İsrailoğullarına mal ve çocuk verilmesini anlatan biçim (17:6) ile iki gruba rızkın ulaştırılmasını anlatan biçim (17:20), bu bağlamlarda sağlanan imkânı bildirir: {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:size sağladık} ve {ar:نُّمِدُّ, tr:numiddu, gloss:sağlarız}. Ayrı bir akış anlamında aynı fiil ailesi suyun akmasını, kabarmasını ve yeni suyla beslenmesini anlatır. Bu akış kolu hedef çevresine bereket yerleştiren {ar:بَٰرَكْنَا حَوْلَهُۥ, tr:bāraknā ḥawlahu, gloss:çevresini bereketli kıldık} ile buluşunca, devam eden ihsanı bereketli alanı besleyen bir akış gibi duyurabilir (17:6, 17:20). Bu bağlantı iki ayetin ayrı bağlamları arasında kurulan mecazdır ve özellikle 17:20’ye uzanan yankı gevşek kalır; rızıkların mescid çevresinden çıktığını ya da gerçek suyun aktığını ileri sürmez (17:6, 17:20).

Gösterilen işaretler, görmeyi kanıt ve kişinin kendi hesabını okumasıyla buluşturan başka bir sure çizgisini açar. 17:13’te işin insana bağlanıp kaydının yazılması ve açılması, 17:14’te kişinin kendi kitabını okuyarak kendi hesabı için kendisinin yeterli hesapçı olması, 17:15’te başkasının yükünü kimsenin taşımaması ve elçi gelmeden azap edilmemesi art arda verilir (17:13, 17:14, 17:15). Odaktaki {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} ile {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:her şeyi gören}, seçilmiş {ar:ءَايَٰتِنَآ, tr:āyātinā, gloss:işaretlerimiz} kümesinin görülmesinden açılmış kaydın kişinin kendisine okunmasına uzanan bir görme hattı kurar (17:13, 17:14). Kayıt odaktaki işaretlerden ayrı bir delildir; Musa’ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāb, gloss:Kitap} ise ayrı bir armağandır (17:1, 17:2). Gece yolcusu sonraki kaydın okuru diye tanımlanmaz (17:13, 17:14, 17:15). Kendi hesabını okuma sahnesi görmenin iç kavrayış anlamını belirginleştirirken işaretlerin içeriğini önceden tayin etmez.

Kendi hesabını görmeye dönen çizgide bakışın yönü yeniden dışarıdan kula çevrilir (17:17). Nuh’tan sonraki kuşakların yıkımıyla birlikte kulların günahlarının bilindiği ve görüldüğü söylenir (17:17); {ar:عِبَادِهِ, tr:ʿibādihī, gloss:kulları} odaktaki tekil {ar:عَبْدِهِۦ, tr:ʿabdihi, gloss:O’nun kulu} adını yineleyerek ilahî gözetim temasını genişletir, ancak aynı kişileri göstermez (17:1, 17:17). {ar:خَبِيرًا بَصِيرًا, tr:khabīran baṣīran, gloss:her şeyden haberdar ve gören} nitelemesi de işaretleri gören yolcuyu ilahî bilgi ve görüş alanında duyurur (17:17). Günahların anılması görme ayrıcalığının yanına hesap verebilirliği ekler; ayet Allah’ın genel bilgisinden söz ediyor da olabilir (17:17). Bu yankı alınan işaretleri ilahî gözetim içindeki bir karşılaşma olarak derinleştirir, fakat yolculuğu sonraki kuşakların yargılanmasının nedeni yapmaz (17:17).

Bir gösterimin muhatabı tek kişiyle sınırlı kalmadığında, başka bir ayet insanlara dönük sonucu öne çıkarır. Odaktaki {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} kulu işaretleri görmeye yöneltirken, 17:60’ta gösterilen görüngü insanlar için sınama kılınır: {ar:وَمَا جَعَلْنَا ٱلرُّءْيَا ٱلَّتِىٓ أَرَيْنَٰكَ إِلَّا فِتْنَةًۭ لِّلنَّاسِ, tr:wa-mā jaʿalnā r-ruʾyā allatī araynāka illā fitnatan li-n-nās, gloss:sana gösterdiğimiz görüngüyü insanlar için bir sınama kıldık} (17:60). Bu yankı gösterimi alıcının algısından izleyenlerin karşılığına doğru genişletir; o görüngü odak yolculukla aynı sahne değildir ve tek tek insanların nasıl karşılık verdiği belirlenmez (17:60).

Tekil alıcı, gece vakti ve uzak {ar:ٱلْأَقْصَىٰ, tr:al-aqṣā, gloss:en uzak} hedefin bir araya gelişi, gösterimi kamusal sergiden çok düşük görünürlüklü bir karşılaşma gibi duyurur. {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} için saklı bilgiye ilişkin ayrı kullanım bu okumaya katkı verir; {ar:لَيْلًا, tr:laylan, gloss:gece vakti} ile {ar:لِنُرِيَهُۥ, tr:li-nuriyahu, gloss:ona görmesini sağlamak için} ise başkaları görsün ve beğensin diye sergileme anlamındaki ayrı kullanımla karşılaştırılabilir. Ekli zamir tek kulu muhatap yapar. Bu karşıtlık alıcı ve sunum biçimiyle ilgilidir; dışarıdaki herkesin görüp görmediğini ya da gösterenin niyetini belirlemez.

Son iki sıfat, tanıklığın dayanağını kamusal ünden Allah’ın işitme ve görmesine taşır. {ar:ٱلسَّمِيعُ, tr:al-samīʿ, gloss:her şeyi işiten} için sözün geniş çevrede yayılıp tanınmışlık kazanması anlamı da vardır; bu sözlük kolu, burada doğrulamayı halk arasındaki üne bağlamayan karşıtlığı belirginleştirir. {ar:أَسْرَىٰ, tr:asrā, gloss:geceleyin götürdü} ve {ar:لَيْلًا, tr:laylan, gloss:gece vakti} ile kurulan yolculuk ve {ar:ٱلْأَقْصَىٰ, tr:al-aqṣā, gloss:en uzak} hedefin yanında, çevresinde kimsenin görüp duymadığı boş arazi anlamı yalnızca ıssızlık imgesi ekler; varış yerinin gerçekten boş olduğunu söylemez. {ar:ٱلْبَصِيرُ, tr:al-baṣīr, gloss:her şeyi gören} sözcüğünün iç kavrayış anlamı da seçilmiş işaretler ve işitme sıfatıyla birleşerek ilahî tanıklığı derinleştirir. Bu karşılaştırmanın sınırı, doğrulamayı halk arasındaki üne dayandırmamaktır; olayın sonradan anlatılmasını ya da insan tanıkların bulunmasını dışlamaz. Dayanak yolcuyu ve işaretleri kuşatan Allah’ın işitmesi ve görmesidir.

</source_prose>
