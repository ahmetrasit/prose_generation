# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:2**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.middle.claims.json`

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
- Refer to source paragraphs as `31:2 ¶N`.

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

`(31:2 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:2",
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
        "citation": "(31:2 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_2/31_2.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_2/31_2.middle.claims.json \
  --ayah-ref 31:2
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_2/31_2.prose.editorial.tr.md`

<source_prose>
## İşaret edilen söz

Âyetin açık sözü “İşte bunlar hikmetli kitabın ayetleridir” der. Başlangıçtaki {ar:تِلْكَ, tr:tilka, gloss:şu}, belirli, dişil tekil ve uzaktan gösteren bir zamirdir. Bu uzaklık fiziksel mesafe ya da rütbe değil, söz içindeki gösterenle gösterilen arasındaki ayrılığı kurar. Gönderge hemen ardından gelen {ar:ءَايَٰتُ ٱلْكِتَٰبِ ٱلْحَكِيمِ, tr:āyātu al-kitābi al-ḥakīmi, gloss:hikmetli kitabın ayetleri} öbeğinde açılır; okur “şu”nun neyi gösterdiğini bulmak için önceki âyete dönmek zorunda kalmaz. Cümle bir olayı fiille anlatmak yerine {ar:تِلْكَ, tr:tilka, gloss:şu} öznesini öne alarak tanımlar. Arapçada insan dışı çoğulların dişil tekil biçimle uyum kurabilmesi, {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} adını çoğul bırakırken bu ayetleri tek bir gösterilen bütün olarak toplamaya imkân verir.

Bu tanımın ad yüklemi olan {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} nominatif (merfûʿ, yalın) durumda gösterileni adlandırır. Ardından gelen {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} tamlayan durumuyla ayetleri kitaba bağlar; yeni bir yargı kurmaz. Belirli artikel kitabı bilinen bir metin bütünü olarak sunarken tamlayan biçimi ilişkinin yönünü açık tutar: ayetler kitaba ait olabilir, kitabın görünür içeriğini de oluşturabilir. {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} ise belirlilik, eril tekil biçim ve cer hâliyle kitaba uyan sıfattır; doğrudan nitelenen her ayet ayrı ayrı değil, kitaptır. Böylece kısa diziliş, işaret ile hikmet arasında yerel bir menteşe kurar; başka başlangıçlarda tekrarlanan bir formül ya da sonraki âyetlere yayılan bir hat önermez. “Hikmetli kitap” ifadesinin ikinci bir yargı gibi duyulması ise bu tanıma eşlik eden yan bir izlenim olarak kalır.

Bu bağlar ses örgüsünde de duyulur. {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} kelimesinin belirgin başlangıcı ve uzun ā’sı kulağı {ar:تِلْكَ, tr:tilka, gloss:şu} işaretinden yüklemin adına, oradan tamlamaya taşır. Ayet adıyla {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} arasındaki ses bağı tamlamayı duyurur; belirli artikelin yinelenişi ve tamlayan kadansı, kitabı niteleyen {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} sözüne geçişi işittirirken isimle sıfatın görevlerini ayrı tutar. Son niteliğin uzun ī’si ve m ile kapanışı onu kulağa yerleştirir, öğeleri üstünlük sırasına dizmez. Buradaki kitap yazma eylemi değil, nitelenen yazılı metin bütünüdür; yazıyla bağı kitap oluşunda sürer. Hikmetli olma da tek bir yargılama veya yazma işi değil, kitaba süreklilik kazandıran niteliktir.

“Âyet” sözü yazılı metindeki bölümleri adlandırırken görünür belirti anlamını da taşır: {ar:آية, tr:āya, gloss:görünür belirti} fark edilir kılar ve bir şeye işaret eder. Bu bağlamda çoğul {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} yazılı ayetler olarak kalır; kitabın metin çerçevesi işaret anlamını tek tek incelenebilen delillere doğru genişletir. Bu bağlantı yazılı bölüm ile onun delil gücüne odaklanır; kişi veya topluluk, harf parçası ya da güneş ışığı için kullanılan öteki âyet anlamlarını devreye sokmaz. Daha ihtilaflı dönüş-yönelme çağrışımını ise {ar:تِلْكَ, tr:tilka, gloss:şu} zamirinin gösterme gücü harekete geçirir: okur ayetleri yön bulmak için dönebileceği başvuru noktaları gibi de düşünebilir. Buradaki dönüş fiziksel bir yolculuk değil, yazılı ayetlere yeniden başvurup yön bulma imgesidir; bu yerel çağrışım metinsel anlamın yerini almaz.

Yazılı bütün fikrini {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} sözü de genişletir. Sözcük kitap anlamındadır; aynı sözlük ailesindeki başka bir kullanım, deri parçalarını dikmek gibi bir şeyi diğerine katıp birleştirmeyi anlatır. Bu maddi birleşme imgesi çoğul {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} ile temas edince ayrı ayetlerin tutarlı bir yazılı bütün içinde toplanmasını düşündürür; odaktaki söz, gerçek bir dikiş ya da yazma eylemi anlatmaz. Kitap başka bağlamlarda farz, hüküm veya yazgı anlamlarını da taşıyabilir. Bu normatif ağırlığı ayet çoğulu değil, onları niteleyen {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliği devreye sokar: kitabın yazılı kimliği korunurken ona bağlayıcı bir güç eklenir. Bu bağlantı kitabı belirli bir ödev, yasa, sicil, kişi adına kayıt ya da ödeme ve serbest bırakma şartları belirlenmiş sözleşme olarak tanımlamaz; yalnızca yazılı kitap okumasına normatif ağırlık ekler.

{ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin temel anlamı, bilgi ve akılla doğruyu bulma hikmetidir. {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} delil taşırken {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} metinsel bir düzen kurar; bu iki temas hikmetli olmayı soyut övgüden iş gören yargı gücüne doğru genişletir. Aynı sözlük ailesindeki {ar:حَكَمَ, tr:ḥakama, gloss:alıkoymak veya geri çevirmek} kişiyi haksızlık ya da bozulmadan uzak tutmayı; {ar:حَكَمَ بَيْنَهُمْ, tr:ḥakama baynahum, gloss:aralarında hükme varmak} ise ihtilafı bağlayıcı kararla bitirmeyi anlatır. Kanıt taşıyan ayetler ile yetkili kitap bu kullanımlara ayrı ayrı temas eder: metin zararlı yönelişi durduran bir düzeltme, anlaşmazlıkta karar vermeye elverişli bir bütün gibi okunabilir. Bir başka kullanım, {ar:الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا, tr:al-ḥukmu bi-shayʾ an taqḍiya annahu kadhā aw laysa bi-kadhā, gloss:bir şeyin ne olduğuna karar vermek}, önermenin doğru olup olmadığına hükmetmektir; ayetlerin delili ve kitabın düzeni bu belirleme gücünü de düşündürür. Bu okuma belirli bir zarar, taraf ya da fiilen verilmiş karar anlatmaz; hikmet anlamını koruyarak odağa düzeltici ve yargısal bir kapasite ekler.

Yargı yönünün yanında aynı niteliğin sağlamlaştırma çağrışımı, odaktaki öbeğin kuruluşuna başka bir katkı verir. {ar:أَحْكَمَ الشَّيْءَ, tr:aḥkama al-shayʾ, gloss:bir şeyi sağlamlaştırmak} bir yapıyı dayanıklı kılmayı anlatır; odaktaki sıfat bu eylemin adı değildir. Metne özgü {ar:آيَاتُهُ أُحْكِمَتْ وَفُصِّلَتْ, tr:āyātuhu uḥkimat wa-fuṣṣilat, gloss:ayetleri sağlamlaştırılıp açıklanmıştır} kullanımı (11:1), ayetlerin kuşku ve karışıklığa yer bırakmayacak biçimde düzenlenmesini anlatır. Burada çoğul ayetler {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} içinde birleşirken, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliği bu bütünü güvenilir ve bozulmaya dirençli duyurur. Ayrı ayrı incelenebilen işaretlerin bir metinde toplanması, dışarıya yön ve hüküm verebilen bir bütünü içeriden de sağlamlaştırılmış düzen olarak duyurur. Bu yerel birleşim belirli bir kuralı, zararı veya kararı adlandırmaz ve metnin her özelliğinin mutlak kusursuzluğunu ileri sürmez; odağın düzeltici ve bağlayıcı kapasitesini gösterir.

Bu yargı ve sağlamlık yönleri, kitabın başka bağlamlardaki kullanımlarıyla da belirginleşir. Kitap insanların ayrılığa düştüğü konularda hükme bağlama işlevi taşır (2:213); hüküm ve ölçü olarak öne çıkar (4:105, 5:48), başka bir yerde de hakem diye anılır (6:114). Bu örnekler {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} için bağlayıcı belirleme, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} içinse yargısal ve sağlamlaştırıcı yönler sunar. Bu karşılaştırma kitabın tümünü hukuk koduna dönüştürmez, her uyuşmazlığın sonuçlandığını da söylemez; burada tuttuğu sınır, odak kitabın başka bağlamlardaki işlevleriyle kurduğu benzerliktir. Bu temaslarla odaktaki yazılı bütün, iddiaları ayıran güvenilir bir ölçü gibi duyulur.

## Rehberlikten davranışa

Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} yazılı bütün önceki bölümde güvenilir bir ölçü gibi duyulmuştu; şimdi onun yön gösterme gücünün yaşama nasıl geçtiği açılır. 31:3’te iyilik yapanlara verilen {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} hakikat yönelişini, 31:5’te Rablerinden gelen hidayet bu yöneliş üzerinde olmayı anlatır; Allah’ın yolundan söz eden {ar:سَبِيلِ ٱللَّهِ, tr:sabīli llāhi, gloss:Allah’ın yolu} 31:6’da ayrı bir güzergâh sunar (31:3, 31:5, 31:6). Hidayetle ilgili başka bir imge, önden giden kılavuz ya da bir şeyin ön kısmıdır. Bu imge yazılı kitaptan gelen yönü yolu açan bir rehber gibi duyurabilir. {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin zararı durdurup yönelişi düzeltme çağrışımı hidayetle buluşurken, sağlamlaştırma yönü odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} bütününün güvenilirliğini korur. Bu pasajda kılavuz, gerçek yolculuk değil, odağın yazılı bütününe yön verme gücünü açıklayan yerel imgedir; başka hidayet anlamlarını geçersiz saymaz.

Bu yöneliş, davranış ve şefkatle karşılaştığında daha somut bir sonuç kazanır. Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} için bağlayıcı güç, 31:3’te {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} ile birlikte verilen {ar:رَحْمَةًۭ, tr:raḥmatan, gloss:merhamet} ile şefkatli amaca açılır; 31:4’te {ar:يُقِيمُونَ ٱلصَّلَوٰةَ, tr:yuqīmūna ṣ-ṣalāta, gloss:namazı ayakta tutarlar} namazın sürdürülmesini, zekât da somut karşılığı gösterir (31:3, 31:4). {ar:بِٱلْءَاخِرَةِ هُمْ يُوقِنُونَ, tr:bi-l-ākhirati hum yūqinūn, gloss:ahirete kesin inanırlar} sözü kesinliği bildirir. Namazı sürdürmek yönelişi davranışta yerleştirirken, ahirete kesin inanmak kuşkunun gerilediği bir kavrayış gösterir; bu kesinlik {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin bilgiyle doğruyu bulma yönüne temas eder. Bu sıra hem odaktaki kitabın işleyişini hem de onu alanların karşılığını açık tutar.

31:3’teki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} sözü olağan yön gösterme anlamını korurken, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğiyle düşük kesinlikli ve biçim-ses bakımından uzak bir çağrışım da kurabilir. Bu yan imge iki ayrı yönde gelişir: dirençli bir örüntü kırılıp direnci kesilebilir ya da çocuk ritimle yatıştırılarak daha alıcı hâle gelebilir. İlk resimde düzeltme engeli koparır; ikincisinde yumuşatıp dikkati açar. Kırma ve yatıştırma, 31:3’teki hidayetin kökü ya da olağan sözlük anlamı değil, bu belirli ses-biçim çağrışımının iki düşük kesinlikli imgesidir. Böylece hidayetin yön gösterme anlamı yerinde kalırken düzeltici etkinin karşılanışına iki ayrı görünüm eklenir.

Yolun yönü kadar dikkatin hangi söz tarafından tutulduğu da önem kazanır. 31:6’da Allah’ın yolundan bilgisizce saptıran, satın alınmış {ar:لَهْوَ, tr:lahw, gloss:oyalanma} ilgiyi başka şeye bağlar; yanındaki {ar:ٱلْحَدِيثِ, tr:al-ḥadīth, gloss:yenilenen söz} tekrar tekrar tazelenen konuşma gibi duyulur. 31:7’de ise odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} {ar:ءَايَٰتُنَا, tr:āyātunā, gloss:ayetlerimiz} diye yeniden anılır ve {ar:تُتْلَىٰ, tr:tuṭlā, gloss:peş peşe okunur} sözüyle birer birer aktarılır (31:6, 31:7). {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} yazılı anlamını korurken, bu okuma onu zamana yayılan ve dinleyenin dikkatini isteyen bir iletime taşır. İki söz aynı dikkat alanında yarışır: satın alınmış oyalama ilgiyi başka yöne çeker, art arda okunan ayetler işitilebilir biçimde sunulur. Böylece metnin aktarılışıyla alımlanışı, odak kitabın ayetlerinde birleşir.

Okuma dinleyene ulaşsa da karşılık kendiliğinden gelmez. 31:7’de alıcının {ar:وَلَّىٰ, tr:wallā, gloss:yüz çevirdi} sözüyle yüzünü dönmesi, işitme yolunu keser; {ar:لَمْ يَسْمَعْهَا, tr:lam yasmaʿhā, gloss:onları duymamış gibi} ifadesi duyumu olduğu kadar anlama ve cevap vermeyi de düşündürür. Kulaktaki {ar:وَقْرًۭا, tr:waqran, gloss:ağırlık} engeli bedensel ağırlık gibi canlandırır; yüz çevirmeyle birleşince kişinin kurduğu kapanma belirginleşir. Bu ağırlık, gerçek bir sağırlık tanısı değil, 31:7’deki alımlanmama hâlini bedensel olarak canlandıran imgedir. Odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler ve işaretler} görünür ya da işitilir işaret anlamını korurken, başka örnekler alıcı tepkisinin değişebildiğini gösterir: ayetlerin okunup öğretilmesi (2:151), hakikat üzere okunan ayetler (45:6) ve belirtinin görülmesine rağmen inanmama (26:103). Açıklık tek başına inanç doğurmaz ve her belirti ayet değildir; {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin açık, sağlam metin yönü bu yüzden alıcının kabulünden ayrı kalır.

31:7’deki işitme ve kabul meselesinden ayrı olarak, vaat edilen sonucun güvencesi 31:9’da öne çıkar. Vaadin yanında yinelenen {ar:ٱلْعَزِيزُ ٱلْحَكِيمُ, tr:al-ʿazīzu l-ḥakīmu, gloss:güçlü ve hikmetli} niteliği, odaktaki {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} sözüne yerel bir yankı verir. {ar:وَعْدَ ٱللَّهِ حَقًّۭا, tr:waʿda llāhi ḥaqqan, gloss:Allah’ın vaadi gerçektir} vaadi gerçek diye mühürler; tekrarlanan hikmet niteliği güvenceye otorite katar. Bu yankı, kitabı vaatle özdeşleştirmeden odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} ile vaat arasındaki güven bağını güçlendirir.

Vaadin güvenceye alınmasından sonra 31:10, sözü yaratılışın göz önündeki düzenine taşır (31:10). {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} ayrı parçaları birleştiren yazılı bütün anlamını taşırken, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} için açılan sağlamlaştırma yönü, yeryüzünün sallanmaması için dağların yerleştirilmesiyle temas eder. {ar:خَلَقَ ٱلسَّمَٰوَٰتِ, tr:khalaqa s-samāwāti, gloss:gökleri yarattı} yaratmayı bildirir; ölçü ve oranla kurma okuması, devamındaki yerleştirme ve denge ayrıntılarından doğar. {ar:بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:bi-ghayri ʿamadin tarawnahā, gloss:gördüğünüz direkler olmadan} görünür direklerin bulunmadığını söyleyerek göklerin dayanağı sorusunu açar. Tasvir görünmeyen direkleri öne sürmez; bunun ardından yeryüzüne konan {ar:وَأَلْقَىٰ فِى ٱلْأَرْضِ رَوَٰسِىَ, tr:wa-alqā fī l-arḍi rawāsiya, gloss:yere sabit dağlar yerleştirdi} dağlar, göklerin dayanağına değil, {ar:أَن تَمِيدَ بِكُمْ, tr:an tamīda bikum, gloss:sizinle sallanmasın diye} yeryüzünün sallantısını önlemeye bağlanır. Böylece direkler sorusu ile sabitleme imgesi ayrı görevlerde kalır.

Aynı yaratılış tasviri yeryüzündeki canlılığı ve üretkenliği de izletir. 31:10’da canlıların yeryüzüne yayılması anılır; ardından {ar:وَأَنزَلْنَا مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَنۢبَتْنَا فِيهَا مِن كُلِّ زَوْجٍۢ كَرِيمٍ, tr:wa-anzalnā mina s-samāʾi māʾan fa-anbatnā fīhā min kulli zawjin karīmin, gloss:gökten su indirip bitirdik} gökten inen suyla bitkilerin çıkışını gösterir (31:10). Böylece dağlar sallantıyı önleme, canlılar yayılma, suyla bitkiler de üretkenlik ayrıntısını taşır. 31:10 sahneyi ayet diye adlandırmaz; bu bağ, görünür yaratılış ayrıntıları ile odak ayetlerin delil anlamı arasındaki yorumlu temastır.

Yaratılışın geniş ölçeğinden sonra 31:12’de Lukmân’a verilen hikmet, ardından 31:13, 31:14 ve 31:17’deki öğütler davranışa değen yakın çevreye geçer. Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} yazılı bir bütün olarak öğüdün eyleme ulaşabildiği bir araç gibi okunabilir. 31:12’deki {ar:ٱلْحِكْمَةَ, tr:al-ḥikmata, gloss:hikmet} odaktaki {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğini bilgi ve akılla doğruyu bulma yetkinliği olarak yankılar; hikmetin verilmesi onun aktarılabildiğini, Lukmân’ın şükrü ise görünür karşılık bulduğunu gösterir. Oğluna yakın hitapla gelen sakındırma (31:13), anne babaya ilişkin sorumlulukla kuşaklararası öğüde genişler (31:14). İyiliği emretmek ve namazı kılmak olumlu yönü, başa gelene sabretmek bu yönelişi sürdürmeyi, kötülükten sakındırmak sınırı kurar (31:17). Böylece hikmet hem bağlayıcı yön verir hem zararlı eylemi durdurur; odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler} gösterge olmaktan yaşama yön veren kaynağa, yazılı bütün de öğüdün eyleme ulaşabildiği araca doğru genişler. Bu, öğüdün odağa nasıl temas ettiğine dair bir bağlantıdır: kitap Lukmân’a hikmet veren kaynak diye sunulmaz ve ayetler tekil davranış kurallarına indirgenmez; yazılı bütünün katkısı öğüdün yaşama ulaşabildiği aracı olmaktır.

Davranışı doğrultma imgesi, hareketi sınırlayıp yönlendiren gem parçasıyla daha bedensel hâle gelir. {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} bir sıfatken, aynı sözlük ailesindeki {ar:حِكْمَةُ اللِّجَامِ, tr:ḥikmat al-lijām, gloss:gemin çeneyi saran bölümü} hayvanın çenesini kuşatıp ileri atılımını sınırlayan gem parçasının adıdır; bu somut isim odaktaki sıfatın doğrudan karşılığı değildir. 31:18’de yanağı ve boynu böbürle çevirmemek, 31:19’da adımı ölçülü tutup sesi alçaltmak hareket ve söz üzerindeki özdenetimi ayrı ayrı görünür kılar (31:18, 31:19). Gem imgesi bu öğütlerin yön ve ifade gücünü sınırlama işini bedensel olarak kavratır; gem terimi ve hayvan öğütlerin kendi sahnesinde değil, bu benzetme bağlantısındadır. Bu yerel benzetme, hikmetli niteliğin davranışı doğrultma gücünü somutlaştırır.

## Görünen, gizli ve bağlayıcı olan

Gem imgesi hareketi ve sözü ölçülü tutmuştu; 31:20 bakışı dışta görünenle içte saklı olana çevirir. Nimetlerin birlikte anılması odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler ve işaretler} sözünün görünür belirti anlamını derinleştirir: açık nimetler görünen tarafı, ayrıca anılan iç nimetlerse hemen seçilemeyen derinliği düşündürür. Bu işaret, saklı olanın eksiksiz haritası değil; görünenden görünmeyen ilişkilere açılan bir temas noktasıdır (31:20). Aynı âyette bilgi olmadan Allah hakkında çekişme, bilgi ve yönelişten kopmuş tartışmanın nasıl düğümlenebildiğini gösterir; bu okuma bilgi dışı her ayrılığı kötü niyete bağlamaz. Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} ile yan yana duran {ar:كِتَٰبٍۢ مُّنِيرٍۢ, tr:kitābin munīrin, gloss:aydınlatıcı kitap}, görünürle saklı olanı birbirine karıştırmadan derinliği aydınlatan kaynak imgesini sunar. Oradaki {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} bu işarete gizliye doğru yön veren olası bir imge katar; bu bağlantı kesinleşmiş sözlük anlamı değildir. Böylece bilgi, hidayet ve aydınlatıcı kitap, aynı derinliğe açılan ayrı girişler olarak kalır.

Görünenle saklının işarete kattığı derinliğin ardından 31:22 bağlılığın sürdürülme biçimini kişinin eylemine taşır (31:22). Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} için açılan bağlayıcı yükümlülük ve {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin sağlamlık yönü bu eylemlerle temas eder. Kişi önce {ar:أَسْلَمَ وَجْهَهُۥ لِلَّهِ, tr:aslama wajhahu li-llāhi, gloss:yüzünü Allah’a teslim etti} diye yönünü teslim eder, sonra {ar:ٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:al-ʿurwati l-wuthqā, gloss:sağlam kulp} gibi sıkıca tutunur; bu tutuş güvenceye ve ardından gelen sonuca bağlanır. Sağlam kulp 31:22’nin kendi maddi imgesidir; odak kitabın karşılığı değil, odak ile kişinin tutunma eylemi arasında benzetme köprüsüdür. Bu köprü, odakta bağlayıcı görünen ilişkinin eylemde sürdürülen katılım olarak kavranmasını sağlar.

Kişinin etkin tutuşu 31:27’de yerini yazının maddi araçlarına bırakır; soru bu kez yazılı ortamın neyi taşıyıp neyi tüketemediğidir (31:20, 31:27). Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} yazılı metin olmayı sürdürür; 31:20’deki {ar:كِتَٰبٍۢ مُّنِيرٍۢ, tr:kitābin munīrin, gloss:aydınlatıcı kitap} imgesi de bu ilişkiye katılır. 31:27’de ağaçları kalem, denizi mürekkep yapmak yazı kapasitesini kurar; yeni denizler ekleyip mürekkebi beslemek bu kapasiteyi daha da büyütür. Yine de {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri} bu maddi imkânlarla kuşatılamaz: araçlar sınıra dayanırken söz sürer. Âyetin sonundaki {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} düzenin sağlamlığını çağrıştırır ve bu nitelik araçların sınırlı oluşuyla çatışmaz. 31:27’nin tükenmezlik vurgusu ilahî sözler hakkındadır; odaktaki kitabın sonluluğu hakkında yeni bir iddia kurmaz. {ar:هُدًۭى, tr:hudan, gloss:yol gösterme}, kitap ve ışık da bu bağlantıda ardışık aşamalar değil, yan yana duran kaynaklardır.

Yazılı bütünün birliği, 31:28’de çokluk ile tek işleyiş arasındaki ayrı bir yapısal benzerliğe açılır. Odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler ve işaretler} farklı göstergeleri adlandırır; {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} için verilen birleştirme kullanımı bunları tek düzende toplamayı düşündürür. 31:28’de birçok varlığın yaratılması ve diriltilmesi tek bir benliğin yaratılıp diriltilmesi kadar kolay gösterilir; çokluk tek bir kudret ve işlem içinde kapsanabilir (31:28). Buradaki temas çokluğun tek düzende kapsanmasıdır: odaktaki kitap yaratılış ya da dirilişle özdeşleşmez, ayetler de tek bir işleme indirgenmez. Böylece yazılı bir bütünde toplanan çeşitli işaretlerle çok sayıda varlığın tek kudrette kapsanması arasında yapısal bir benzerlik kurulur.

31:28 çokluğu tek işleyişte düşünür; 31:31 ve 31:32 ise bundan ayrı olarak hareket ve kriz içindeki bir sahneye geçer (31:28, 31:31, 31:32). Odaktaki {ar:ءَايَٰتُ, tr:āyātu, gloss:ayetler ve işaretler} bu kez yolculukta görünür delil anlamını taşır. 31:31’de gemi su üstünde ilerler, 31:32’de dalgalar onu sarar; hareket önce akışı, sonra krizin baskısını görünür kılar. Tehlike geçip kurtuluş geldiğinde sahne tamamlanır, fakat kurtarılanların işaretleri bilerek inkâr etmesi yaşanan kanıtın kabulü zorunlu kılmadığını gösterir. Böylece kriz delili olayın içinden seçilir kılar, kurtuluş da alıcının karşılığını kendiliğinden belirlemez. Gemi bu iki âyetin özel sahnesinde istikrarsızlığı görünürleştiren taşıyıcıdır; bu bağlantı bütün ayetleri seyir işaretine dönüştürmez.

Gemi sahnesi olay içindeki işaretleri ve alıcının kriz sonrasındaki dönüşünü izler; başka bir benzetme hesabı kişi adına tutulan kayda yaklaştırır. Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} için ad yazma ve sicile geçirme kullanımı bir kayıt taşıyıcısı, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} için sunulan bağlayıcı karar yönü de bu kaydın güvenilir sonucunu düşündürür. Gerçek ve geleceğe dönük vaat hesap ufkunu açar (31:9); hardal tanesi kadar küçük, gizli kalabilecek bir eylemin de hesaba girmesi en küçük ölçüyü bu ufka dahil eder (31:16). Hiç kimsenin başka birinin yerine yarar sağlayamayacağı uyarısı hesabı kişiye özgü ve devredilemez kılar (31:33). Bu kayıt bağlantısı bir benzetme olarak kalır; 31:16 ve 31:33 odak kitabı adlandırmaz, özellikle 31:33’teki uyarı onun doğrudan açıklaması değildir. Bu sınırlar içinde kayıt imgesi, kitabın bağlayıcı karar yönünü kişiye özgü hesap fikriyle buluşturur.

Kişiye özgü hesap sorumluluğu belirginleştirir; 31:34 ise sorumluluğun geleceğin tüm bilgisini insana vermediğini gösterir (31:34). Odaktaki {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:kitap} doğru eyleme yön verirken, {ar:ٱلْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} niteliğinin bilgiyle doğruyu bulma anlamı insanın sınırları karşısında ölçü kazanır. Saati, yağmuru ve rahimlerde olanı Allah bilir; hiç kimse yarın ne kazanacağını ya da nerede öleceğini bilemez. Âyetin sonundaki haberdarlık içte saklı olanı da kapsar. 31:34 öncelikle Allah’ın bilgisini yüceltir; bu yüzden odağa bağlanan bilgi sınırı doğrudan sözlük anlamı değil, bağlamdan doğan bir çıkarımdır: hikmet burada insanın bilmediği şeyler karşısında eylemini ölçülü tutan yöneliş gibi duyulur.

</source_prose>
