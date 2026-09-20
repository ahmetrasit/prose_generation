# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:22**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.middle.claims.json`

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
- Refer to source paragraphs as `17:22 ¶N`.

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

`(17:22 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:22",
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
        "citation": "(17:22 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_22/17_22.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_22/17_22.middle.claims.json \
  --ayah-ref 17:22
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_22/17_22.prose.editorial.tr.md`

<source_prose>
17:22, Allah'ın yanında başka bir ilah edinmeyi yasaklar ve bu atamanın mümkün sonucunu aynı cümlede sürdürür: {ar:لَا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhara, gloss:Allah'ın yanında başka bir ilah edinme} ve {ar:فَتَقْعُدَ مَذْمُومًا مَّخْذُولًا, tr:fa-taqʿuda madhmūman makhdhūlan, gloss:kınanmış ve yardımsız kalırsın}. İlk söz bir mevki verme eylemini engeller; ikinci söz, bu yasağın önlediği sonu oturuş, kınanma ve destek yoksunluğu boyunca açar.

Başlangıçtaki {ar:لَا, tr:lā, gloss:yasaklama edatı} tilavette fiilden önce ayrı duyulur; bu küçük ses eşiği reddi işitilir kılar, fakat edata yeni bir sözlük anlamı eklemez. Ardındaki {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} cezmli fiil, olup bitmiş bir hâli bildirmek yerine muhatabın yapabileceği atamayı doğrudan yasaklar. Uyarı bu yüzden genel bir ahlâk sözüne değil, bir varlığa statü verme kararına yönelir.

Bu kararın dilbilgisel yükünü {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} taşır: fiil, mevcut bir katılımcıyı yeni bir hâle, niteliğe ya da mevkiye getirir; {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} onun nesnesidir. Böylece yasak, yoktan bir ilah yaratmaya değil, var olan bir şeyi ilah statüsüne yerleştirmeye uzanır. Sözlükte bir varlığı belirli bir adla anma kullanımı da bulunur; bu yan kol “başka ilah” nitelemesini adlandırma yönünden de duyurur, hükmün ağırlığını ise fiilin mevki verme gücü taşır.

İlah isminin tapınılan varlığı bildirmesi, bu statü atamasına bir ibadet ilişkisi ekler. {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah}, {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} ile nesne konumuna girdiğinde, tapınma ilişkisi çekimli bir ibadet fiilinden değil, ismin nesne oluşu ve Allah'la kurduğu karşıtlıktan okunur. Bu temas, rakipliği kişinin kimliğine değil aldığı ibadet mevkiine bağlar: var olan bir şey Allah'ın yanına rakip tapınma nesnesi olarak yerleştirilir. İbadet, sığınma, otorite, bağlılık ve hayret alanlarına uzanan kelime ailesi bu ilişkiye art alan verirken, cümlenin somut yönü ilah isminin nesne oluşunda kalır.

{ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} cümlede belirli özel ad olarak kalır; aynı kelime ailesinden gelen {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} ise tekil, belirsiz ve nasb hâlinde bir ortak isimdir. Bu biçim, yasağı belli bir tarihsel puta ya da kişiye daraltmadan adı konmamış herhangi bir rakibe açar. Özel ad ile ortak isim aynı kökten gelir, ancak biçimleri ve göndergeleri ayrıdır. Seslenme, ant ve kısaltılmış biçimler de bu ailenin ayrı kollarıdır; burada Allah özel adının cümle içindeki biçimi kullanılır. Kök ailesindeki sığınma ve otorite yankısı, özel adı “sığınak” diye çevirmeden ya da bütün kök alanını bu tekil nesneye yüklemeden, sonda duyulan {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} ile kurulan koruma gerilimini derinleştirir.

{ar:مَعَ, tr:maʿa, gloss:yanında} edatı, {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} ile birliktelik kurar. Fiziksel yan yanalık resmi soyut beraberliği duyurur; odaktaki ilişki ilah nesnesini Allah'ın yanına yerleştirirken tarafları eşitlemez. Tilavette edatın ardından gelen genitif biçim {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah}, bu yönetim bağını duyulur kılar; özel ad böylece beraberlik yapısının bağlı öğesi olarak işitilir.

Bu belirli merkez ile onun yanına konan belirsiz nesne arasındaki farkı {ar:ءَاخَرَ, tr:ākhara, gloss:başka} sıfatı tamamlar. İsimden sonra gelir; eril ve nasb hâlinde {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} ile uyum gösterir. Tenvin almayan gayr-i munsarif sıfat biçimi belirsizliğini korur ve ilahı niteleyen ortak isim ilişkisini sürdürür. Kök ailesi “başka”, “öteki” ve “sonraki” anlamlarını taşır; Allah'ın belirli adı ile belirsiz ilah arasındaki yerel karşıtlık zamansal “sonraki”yi geri plana iter ve “başka”yı öne çıkarır.

Bu sıfatın sert başlangıcı, söz öbeğinin sonunda kısa bir işitsel kesinti yaratır. {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} üzerindeki nasb tenviniyle duyulan “-an”, {ar:ءَاخَرَ, tr:ākhara, gloss:başka} ile kesilir ve sonlarda {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ile {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} biçimlerinde yeniden belirir. İki edilgen ortaç m sesi, nasbı ve tenvini paylaşarak kapanışı ritmik biçimde toplar; ikinci biçimin daha pürüzlü sonu vurguyu desteğin çekilmesinde bırakır. Böylece ritim, yasağın ardından gelen sonucu önce kınanma sonra destek yoksunluğu olarak duyurur.

Atama fiilinin var olan bir şeye mevki verme değeri, düzen kurma tasviriyle de yankılanır. Yeryüzünün yerleşik kılınması, nehirler ve dağların yerleştirilmesi anlatısının ardından “Allah'la birlikte başka bir ilah mı?” sorusu gelir (27:61): {ar:جَعَلَ ٱلْأَرْضَ قَرَارًا, tr:jaʿala l-arḍa qarāran, gloss:yeryüzünü yerleşik kıldı} ve {ar:أَءِلَٰهٌۭ مَّعَ ٱللَّهِ, tr:a-ilāhun maʿa Allāh, gloss:Allah'la birlikte bir ilah mı?}. Düzen tasviriyle ilah sorusunun ardışıklığı, 17:22'deki {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} için mevcut olana mevki verme okumasını güçlendirir; bu temas biçimbilgisel bir karşılaştırmaya değil, iki anlatımın yan yana gelişine dayanır. Fiilin melekleri dişi diye adlandıran özel sözlük tanıklığı da adlandırma kolunu açar; odakta ise temel anlam mevcut olana ilah mevkii vermeyi taşır.

“Başka ilah” ifadesi, koşullu bir karşı-olguda daha geniş bir düzen baskısı kazanır: Allah'tan başka ilahlar bulunsaydı gökler ve yer bozulurdu (21:22): {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:law kāna fīhimā ālihatun illā Allāhu la-fasadatā, gloss:Allah'tan başka ilahlar olsaydı gökler ve yer bozulurdu}. Bu koşul, {ar:ءَاخَرَ, tr:ākhara, gloss:başka} olanı sıradaki bir nesneden çok düzeni bozabilecek rakip bir merkez gibi duyurur. Çoğulluk varsayımda kalır; bu nedenle 21:22 odaktaki yasağa doğrudan cevap vermek yerine birden çok merkezin düzen üzerindeki bozucu etkisini belirginleştirir.

## Oturuş, kınanma ve destek

İlk cümledeki rakip mevki şimdi bir sonuç hareketine bağlanır. {ar:فَ, tr:fa, gloss:sonuca bağlayan bağlaç}, yeni bir bölüm açmadan {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} fiiline bitişir; tek bir geçiş, önceki yasağı muhtemel neticeye taşır. Mansub fiil yasağı nedensel bir sonuç ilişkisine bağlarken “bu hâle düşmeyesin” uyarısını da taşır; iki yön birlikte kalır ve sonucun mutlaka gerçekleştiğini bildirmez. Ardından gelen iki ortaç başka eylemler değil, bu tek neticenin aynı özne üzerinde topladığı iki durumdur.

Aynı ikinci tekil muhatap, önce {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} ile atama yapan etkin kişi, sonra {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ile sonucun içinde sabit kalan kişi olur. Fiiller eşanlamlı değildir: birincisi statü verir, ikincisi oturuş ve sabitlenme imgesi kurar. “Olmak, kalmak” karşılığı bu kökün yalnız belirli yardımcı-fiil veya yer bildiren kalıplarında görülür; burada sonuç fiilinin temel duyumu oturmak ya da bir hâlde kalmaktır. Sözlükte beklenen bir işten, çıkıştan veya yoldan geri durma kullanımı da bu oturuşa eklenince, bedenin duruşu eyleme gücünün tutulması olarak genişler.

Bu hâlin ilk niteliği {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ile verilir. Mansub edilgen ortaç, {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} öznesine yüklenir: kişi kınamayı yapan değil, olumsuz yargının ve itibar kaybının muhatabı olur. Sözcük övgünün karşıtını bildirir, bedensel bir acıyı değil; kınayan fail adlandırılmadığı için vurgu kınanmış konumda kalır.

Ardından {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış}, aynı özneye bağlı ikinci mansub edilgen hâl olarak desteğin kesildiğini söyler. Kimin yardımı çektiği açık bırakılır; sıra önce kınanmayı, sonra destek yoksunluğunu verir ama bu iki hâl arasında neden-sonuç kurmaz. İlk ortaç itibarı, ikincisi dayanak ilişkisini keser; ortak yapı onları aynı sonuç kişisine bağlarken ses eşleşmesi iki ayrı hâli tek kapanışta toplar. Böylece kınama yargısı ile yardımın çekilmesi ayrı kalır, ama son konumda birlikte ağırlık kazanır.

Bu destek yoksunluğunun dar bedensel yankısı ayrı bir sözlük kalıbında görülür: {ar:تَخَاذَلَتْ رِجْلَاهُ, tr:takhādhulat rijlāhu, gloss:bacakları güçten düştü} bacakların, örneğin yaşlılık ya da sarhoşluk bağlamında, güçten düşmesini anlatır. Odaktaki {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} bu kalıp değil, edilgen bir ortaçtır; {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ile yan yana gelişi, ayağın taşıyamaması kadar sınırlı bir beden benzetmesi kurar. Aynı sözlük alanındaki başka bir insan biçimi hiç kıpırdayamayan kişiyi anlatır; {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} odaktaki olağan kınanma anlamını korurken sabit duruşa ikinci bir bedensel yankı ekler. Bu iki yan kullanım, oturuşla destek kaybının eylem gücünü daraltışını beden üzerinden duyurur; ayet bacak, hastalık, sakatlık ya da felç teşhisi koymaz.

Desteksiz kalma, güvence ve korumayla ilgili ayrı bir yankı da açar. Söz veya anlaşma güvence sağlayabilir; hak ya da dokunulmazlık kişiye bağlayıcı bir sorumluluk yükleyebilir. Bu sözlük alanı, {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ile taşınan yargıyı ve {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} ile belirtilen destek kaybını, koruma vaadinin kırılması ihtimalinde bir araya getirir. Ayet bir antlaşmayı adlandırmadığından rakibe mevki vermenin bağlılık sözünü çiğnemesi kesin bir olay değil, olası bir yankıdır; bu okumada kınanma koruma bağının kırılmasına da ilişir, desteksizlik ise beklenen himaye ve beraberliğin dışında kalmayı duyurur.

Bu iki hâl ve oturuş birlikte işlediğinde sonuç, üç sıfatı yan yana sıralamanın ötesine geçer. {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} eylemi durdurur; {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} itibarı zedeler; {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} beklenen desteği keser; {ar:مَعَ, tr:maʿa, gloss:yanında} ile kurulan beraberlik de çözülür. Bu dört hareket birlikte, rakip mevkiyi Allah'ın yanına yerleştiren kişinin kendi eyleme gücünü tutan bir sonuca varmasını gösterir. Bacak imgesi bu bileşik sonuca yalnız ayağın taşıyamaması kadar sınırlı bir beden yankısı verir; kınanma, destek kaybı ve beraberliğin çözülmesi odaktaki eylemsizlik sonucunu kurar.

Bacak benzetmesinden ayrı olarak, atama ile oturuş bir temel imgesi kurar. Atama fiili {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} var olan nesneye sahte bir temel mevkii verir; ilah statüsü de tapınılan varlığı hayatın dayanağıymış gibi yerleştirir. Kelime alanındaki ayrı bir isim kolu, bir şeyin altında duran dayanağı ya da temel bölümünü anlatır. Bu isim kolunun temel anlamı fiilin doğrudan karşılığı değildir; atama ile {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} yan yana geldiğinde kişi, kendisini yükseltemeyen temelin üzerine oturur: yerleştirdiği rakip dayanak onu yukarı taşımaz.

## Güven ve hareket

Yardımın kesilmesi, güvenin kime bırakıldığı sorusunu sûrenin yakındaki bağlamına taşır. İnsan 17:1'de {ar:بِعَبْدِهِۦ, tr:bi-ʿabdihi, gloss:O'nun kulu} olarak anılır; ardından Kitap rehber kılınır ve Allah'tan başka vekil edinmeme uyarısı gelir (17:2): {ar:وَجَعَلْنَٰهُ هُدًۭى, tr:wa-jaʿalnāhu hudan, gloss:onu rehber kıldık} ve {ar:مِن دُونِى وَكِيلًا, tr:min dūnī wakīlan, gloss:Ben'den başka vekil}. Allah'ın Kitap'a rehberlik rolü vermesiyle insanın başka ilaha mevki vermesi, aynı yapma fiilinin farklı fail ve yönlerdeki kullanımlarını karşılaştırır; bu, aynı olay oldukları anlamına gelmez. 17:1'deki kul adı tek başına geniş bir kulluk öğretisi kurmaz; 17:2'deki vekil uyarısıyla birlikte 17:22'nin bölünmüş yönelişini tek dayanak sorusu olarak duyurur.

Vekil ile ilah arasındaki fark, temasın sınırını da belirler. {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} tapınılan nesneyi, {ar:وَكِيلًا, tr:wakīlan, gloss:vekil} ise işi kendisine bırakılan ve yürütüp koruması beklenen tarafı anlatır (17:2). Bu iki görev ayrı kalır; yine de rakip ilah, güven ve sorumluluğun teslim edildiği alternatif bir merci gibi düşünülebilir. Her vekil tapınılan bir varlık değildir ve odak belirli bir emanet ya da vekile bırakılmış iş adı vermez; bu yüzden böyle bir güven ilişkisi burada olasılık düzeyinde kalır. 17:2'deki {ar:مِن دُونِى, tr:min dūnī, gloss:Ben'den başka} ile odaktaki {ar:مَعَ ٱللَّهِ, tr:maʿa Allāhi, gloss:Allah'ın yanında} ve {ar:ءَاخَرَ, tr:ākhara, gloss:başka} arasındaki karşıtlık, seçilen rakibi tek referans merkezinden ayrı bir taraf olarak belirginleştirir.

Bu emanet beklentisi, kişinin amelinin kendisine bağlanması, kitabının önüne konması, kendi hesabını kendisinin görmesi ve hiçbir yük taşıyanın başkasının yükünü almamasıyla karşılaşır (17:13, 17:14, 17:15): {ar:طَٰٓئِرَهُۥ فِى عُنُقِهِۦ, tr:ṭāʾirahu fī ʿunuqihi, gloss:amelinin karşılığı boynuna bağlanmış} (17:13), {ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku} (17:14), {ar:كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā bi-nafsika l-yawma ʿalayka ḥasīban, gloss:bugün kendi nefsin hesap görücü olarak yeter} (17:14) ve {ar:وَلَا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:wa-lā taziru wāziratun wizra ukhrā, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz} (17:15). Başkasına bırakılması umulan iş, kişisel kayıt ve öz hesapta sahibine döner; hiçbir başkası onun yükünü devralamaz.

Bu sıra, 17:22'deki {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} hâlini kişinin kendi kaydıyla yüzleşmesine, {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} hâlini ise başarısız bir ikame beklentisine bağlayabilir. Vekil ve sorumluluğun devredilememesi yan yana gelince umulan dayanak yükü üstlenemez; odak, rakibin özellikle kefil seçildiğini söylemediğinden tapınma ilişkisi ile hesabı başkasına bırakma ayrı çizgiler olarak kalır. Bu karşılaşma, kınanma ve desteksizliğin kişiyi kendi kaydı ve yüküyle baş başa bırakmasını belirginleştirir.

Bu yalnız kalışın yanında, 17:15'le temas eden dar bir sözlük imgesi başka türden ayrılığı görünür kılar: yavrusunun yanında kalan dişi yaban hayvanı otlayan sürüye katılmaz; ceylan da geride kalır. Bu bağlantıda hayvan imgesi insanı hayvanla özdeşleştirmez; başkasının yükünü devralmama çizgisine, beklenen topluluktan ayrı kalmanın görüntüsünü ekler.

Yardım edecek bir topluluğun bulunmaması ve kişinin kendi kendine de yardım edememesi, desteksizliği başka bir anlatıda görünür kılar (18:43): {ar:وَلَمْ تَكُن لَّهُۥ فِئَةٌۭ يَنصُرُونَهُۥ مِن دُونِ ٱللَّهِ وَمَا كَانَ مُنتَصِرًا, tr:wa-lam takun lahu fiʾatun yanṣurūnahu min dūni Allāh wa-mā kāna muntaṣiran, gloss:Allah'tan başka ona yardım edecek bir topluluğu yoktu ve kendisi de yardım edemiyordu}. Bu, 17:22'deki kişiyle aynı olay değil, benzer desteksizliği başka bir kişide gösteren paralel sahnedir. {ar:مَعَ, tr:maʿa, gloss:yanında} ile kurulan beraberlik, 18:43'te grubun yokluğunda kopmuş destek bağı gibi duyulur; bağlı parçaların bütünden ayrılmasını anlatan ayrı sözlük kolu bu kopuşu somutlaştırır. Bu bağlantı, önceki yaban hayvanı imgesinden ayrı olarak, topluluk desteğinin kesilmesini öne çıkarır.

Vekâlet sorusu daha keskin bir biçimde 25:43'te ortaya çıkar: hevasını ilah edinen kişi üzerine Elçi vekil olabilir mi diye sorulur (25:43): {ar:مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ, tr:man ittakhadha ilāhahu hawāhu, gloss:hevasını ilah edinen kişi} ve {ar:أَفَأَنتَ تَكُونُ عَلَيْهِ وَكِيلًا, tr:a-fa-anta takūnu ʿalayhi wakīlan, gloss:onun üzerinde vekil mi olacaksın?}. Bu soru, başka ilah edinmenin güvenilir bir koruyucu ya da vekil sağlamadığı ihtimalini, odaktaki sıradan destekten yoksun kalma anlamına ekler. 25:43, vekilin güvenilir himaye sağlayıp sağlayamayacağını öne çıkarır; bu karşılaştırma kişisel kayıt ve devredilemeyen yükün ele alındığı 17:13, 17:14 ve 17:15'teki sorumluluk çizgisinden ayrılır.

Hesapta tek başına kalma, sure içindeki toplu hareketle karşıtlaşınca bedensel bir uzaklığa dönüşür. Yardım ve kuvvetle harekete geçen topluluğun yönü (17:6), 17:22'deki {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ve {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} kişinin ters kutbudur: biri destekle ilerlerken öteki oturur ve geride kalır. Bu, geçmişteki genişletici yardımın tersine dönmüş biçimi gibi duyulabilir; karşılaştırma iki ayeti aynı tarihsel olay, hapis ya da hastalık sahnesi yapmaz. Katkısı, destekle ilerleyen grupla oturup geride kalanı karşı karşıya getirerek kaybı hareket eden topluluğun dışına düşme görüntüsüne çevirmesidir.

Bu görüntüye iki ayrı hayvan kullanımı renk verir. {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} ile ilişkili özel dal, yavrusuyla kalıp otlayan sürüye katılmayan dişi yaban hayvanını ve geride kalan ceylanı anlatır; 17:6'daki ilerleyen topluluk bu görüntüdeki ayrılığı geride kalma karşıtlığı olarak belirginleştirir. Başka bir sözlük dalında {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ile ilişkili binek hayvanı yorulup gücünü kaybederek ötekilerin gerisinde kalır; aynı sözcüğün ayrı insan kullanımı da hareket edecek gücün kalmamasını anlatabilir. Bu sözlük kolları ayette gerçek bir hayvan ya da yorgunluk sahnesi kurmaz: ilki topluluktan ayrı kalışı, ikincisi hareket gücünün tükenişini resmeder. Odaktaki {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} olağan kınanma anlamını korurken bu iki imge, destekle ilerleyen grubun karşısında sabit kalmanın sosyal ve bedensel yönlerini ayırt eder.

Hareketin durması, kuşatılma imgesiyle de çevrelenir. Cehennem'in inkârcıları kuşatıcı bir yer kılınması, 17:22'deki oturuşa ilerleyişi kesilmiş bir görünüm ekler (17:8): {ar:وَجَعَلْنَا جَهَنَّمَ لِلْكَٰفِرِينَ حَصِيرًا, tr:wa-jaʿalnā jahannama lil-kāfirīna ḥaṣīran, gloss:Cehennem'i inkârcılar için kuşatıcı bir yer kıldık}. 17:8'deki kuşatılma imgesi, odaktaki oturuşu hapisle özdeşleştirmeden onun hareket alanını çıkışsızlık yönünde daraltır.

Kuşatılmış bu duruşun karşısında Kur'an'ın en dik ve en düzgün olana yöneltmesi bulunur (17:9): {ar:يَهْدِى لِلَّتِى هِىَ أَقْوَمُ, tr:yahdī lillatī hiya aqwamu, gloss:en doğru ve en düzgün olana yöneltir}. {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ayakta durmanın karşısına oturuşu koyarken, {ar:أَقْوَمُ, tr:aqwamu, gloss:en dik ve en düzgün} bedensel doğrulma yönünü sağlar; bacakların güçten düşmesi imgesi de bu rehberli yolda ilerleyememeyi belirginleştirir. Aynı sözcük doğruluk ve dengeli dosdoğruluk anlamı taşır, böylece beden karşıtlığı ahlaki istikamete uzanır; 17:22 açıkça eğrilik bildirmez. Ayrı sözlük adları hastalık ya da sakatlık yüzünden yürüyememeyi anlatır; odaktaki {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ise sonuç bildiren fiildir, hastalık adı değil. Bu bağlantı bir tanı koymaz; sabit oturuştan ilerleyememe imgesini {ar:أَقْوَمُ, tr:aqwamu, gloss:en dik ve en düzgün} ile bedensel doğrulmadan ahlaki istikamete taşır.

Sabitlenme fiilinin bağlam içindeki tekrarı, farklı davranışların ardından benzer oturuşlar kurar. Harcamada eli kısmak ya da ölçüsüzce açmak uyarısını 17:29'da “kınanmış ve bitkin kalırsın” sonucu izler: {ar:فَتَقْعُدَ مَلُومًا مَّحْسُورًا, tr:fa-taqʿuda malūman maḥsūran, gloss:kınanmış ve bitkin kalırsın}; bu davranış 17:22'deki ilah edinme yasağından ayrıdır. Buna karşılık 17:39, odaktaki yasağı aynı sözlerle yineler ve ardından cehenneme atılma, kınanma ve uzaklaştırılmayı getirir: {ar:لَا تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:lā tajʿal maʿa Allāhi ilāhan ākhara, gloss:Allah'ın yanında başka bir ilah edinme} ve {ar:فَتُلْقَىٰ فِى جَهَنَّمَ مَلُومًا مَّدْحُورًا, tr:fa-tulqā fī jahannama malūman madḥūran, gloss:cehenneme atılır kınanmış ve uzaklaştırılmış olursun}. Bu sonuçlar kronolojik bir dizi değil, metindeki iki ayrı sondur: birinde kişi oturup bitkin kalır, ötekinde zorla cehenneme atılıp uzaklaştırılır. Böylece yinelenen yasak, farklı bağlamlarda eylemsiz kalma ile dışarı atılma sonuçlarını ayırt eder.

Bu iki tekrar, {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} için beklenen işten ya da yolculuktan geri durma, katılmama veya bir engelle alıkonma yönündeki özel kullanımı öne çıkarır. 17:29'daki bitkinlik ile 17:39'daki zorla uzaklaştırılma kendi bağlamlarında ayrı sonuçlardır; odak fiilin {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} ile buluşması ise oturuşa etkili eylemden alıkonma yönünü ekler. Böylece bu sözlük yolu odaktaki yasağın davranış kapsamını değiştirmeden, ardından resmedilen sonuç hareketini aydınlatır.

## Yönelişin ufukları

Sözle bir şeyi adlandırma ihtimali, insanın neye yöneldiği sorusunu 17:11'e taşır. Orada insan kötülüğü iyilik çağırır gibi çağırır ve aceleci diye nitelenir: {ar:وَيَدْعُ ٱلْإِنسَٰنُ بِٱلشَّرِّ دُعَآءَهُۥ بِٱلْخَيْرِ, tr:wa-yadʿu l-insānu bi-sh-sharri duʿāʾahu bi-l-khayri, gloss:insan kötülüğü iyilik çağırır gibi çağırır} ve {ar:وَكَانَ ٱلْإِنسَٰنُ عَجُولًا, tr:wa-kāna l-insānu ʿajūlan, gloss:insan acelecidir}. 17:22'de {ar:تَجْعَلْ, tr:tajʿal, gloss:bir duruma getirmek} mevcut bir şeye mevki verir; adlandırma kullanımıyla 17:11'deki {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} eylemi buluşunca, sözle çağrılan zararlı bir güce pratik otorite ve nihai yer verme ihtimali belirir. {ar:إِلَٰهًا, tr:ilāhan, gloss:ilah} tapınılan nesneyi öne çıkarır; acelecilik de neyin iyi ya da nihai sayıldığını tartmadan yönelme riskini artırır. Bu bağlantı belirli bir gücü adlandırmaz ve her hızlı duayı ilah edinme saymaz; 17:11'le kurduğu sınırlı temas, zararlı diye çağrılana aceleyle pratik otorite verme tehlikesini görünür kılar.

Çağrılan şey ile işaret edilen son merci arasındaki ayrım, gece ve gündüzün işaret kılınmasıyla başka ölçekte belirir. Allah geceyi ve gündüzü iki işaret kılar, sonra her şeyi ayrıntılarıyla ayırır (17:12): {ar:وَجَعَلْنَا ٱلَّيْلَ وَٱلنَّهَارَ ءَايَتَيْنِ, tr:wa-jaʿalnā l-layla wa-n-nahāra āyatayn, gloss:geceyi ve gündüzü iki işaret kıldık} ve {ar:فَصَّلْنَٰهُ تَفْصِيلًا, tr:faṣṣalnāhu tafṣīlan, gloss:her şeyi ayrıntılarıyla açıkladık}. Aynı yapma fiili burada geceyle gündüze işaret rolü, odakta ise insana başka bir varlığa ilah statüsü verir. Bu yan yanalık, gösterge olan şeyle tapınılan son nesneyi ayırır ve yaratılmış bir varlığın işaret ettiği nihai merci yerine konması ihtimalini düşündürür; 17:22'nin belirli geceyi, gündüzü ya da işareti rakip seçtiği anlamına gelmez.

Atama fiilinin faili değiştiğinde, 17:18'de ters yönde bir karşı-atama duyulur. Hemen elde edileni isteyen kişiye Allah'ın Cehennem'i tayin etmesi aynı yapma fiilini, ardından aynı {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} hâlini getirir (17:18): {ar:ثُمَّ جَعَلْنَا لَهُۥ جَهَنَّمَ, tr:thumma jaʿalnā lahu jahannama, gloss:sonra ona Cehennem'i kıldık} ve {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:hemen elde edilen}. Böylece insanın rakibe mevki vermesi ile Allah'ın sonucu tayin etmesi fiil ve kınanma üzerinden karşılaşır; bu yankı nedenleri ya da cezaları özdeşleştirmez. Hemen olana yöneliş, rakip mevki atamasıyla kınanmış son arasında olası bir önceki tercih gibi düşünülebilir, ancak bu karşılaştırma kesin neden-sonuç kurmaz ve odak hemen olanı kendi başına adlandırmaz. 17:18'deki {ar:مَّدْحُورًا, tr:madḥūran, gloss:uzaklaştırılmış} ile 17:22'deki {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} da ayrılığın iki farklı biçimini gösterir: kovulma ve desteğin kesilmesi.

Hemen olanın karşısında 17:19'da arzu edilen ve uğruna çaba gösterilen ahiret ufku bulunur: {ar:ٱلْءَاخِرَةَ, tr:al-ākhirah, gloss:ahiret}. Odaktaki {ar:ءَاخَرَ, tr:ākhara, gloss:başka} ise ilahı niteleyen belirsiz eril sıfattır; iki biçim aynı kelime ailesinde buluşur, fakat sıfat isim yerine geçmez. 17:18'deki hemen olana yöneliş, 17:19'daki arzu ve amaçlı çaba, 17:21'de ahiretin derece ve üstünlükçe daha büyük sayılmasıyla bir değer ölçeğine dönüşür: {ar:وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ وَأَكْبَرُ تَفْضِيلًا, tr:wa-la-l-ākhiratu akbaru darajātin wa-akbaru tafḍīlan, gloss:ahiret derece ve üstünlük bakımından daha büyüktür}. Dereceler varış ufuklarının değerini sıralarken, uğruna gösterilen çaba seçilmiş hedefin ardından gelen emeği de düzenler. Odaktaki sıfatın anlamı “başka” olarak kalır; bu kelime ailesi ve bağlam yankısı, onu “ahiret” diye çevirmeden rakip ilahın arzuyu, çabayı ve nihai değer yönünü düzenleyen seçilmiş bir ufuk gibi işleyebileceği ihtimalini açar.

Bu son ufuk ilişkisi 16:22'de tek ilahın anılmasıyla ahirete inanmama sözünün aynı ayette buluşmasıyla da belirginleşir: {ar:إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ, tr:ilāhukum ilāhun wāḥidun, gloss:ilahınız tek bir ilahtır} ve {ar:لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:lā yuʾminūna bi-l-ākhirah, gloss:ahirete inanmazlar} (16:22). Bu yan yanalık, odaktaki {ar:ءَاخَرَ, tr:ākhara, gloss:başka} sıfatına alternatif bir nihai yönelim ufku ekleyebilir: rakip ilah edinmeyi tek ilah inancı ve ahiret yönelimi karşısında düşündürür. Bağlantı sıfatı “ahiret” diye çevirmeden ve bir zaman mekanizması kurmadan bu iki yöneliş ufkunu yan yana getirir.

17:21'in derece karşılaştırması önce 17:19'daki değer ufkunu sürdürür: ahiret derece ve üstünlük bakımından daha büyüktür. Bu sıralama, 17:22'deki {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturup kalmak} ve {ar:مَّخْذُولًا, tr:makhdhūlan, gloss:yardımsız bırakılmış} ile beliren sabitlik ve desteksizlik yanına bedensel bir karşı-imge de açar: zayıf ayağın yükselişi taşıyamaması derecelere katılamamayı düşündürür. Bu, derece sıralamasını fiziksel tırmanışa çevirmek değil, aynı “yükselme” imgesinin bedensel yankısını kurmaktır. 17:18'deki kınanma ve uzaklaştırılma ile 17:23'teki yalnız Allah'a kulluk vurgusu bu imgeye ahlaki ve toplumsal yön ekler: ikame edilen merci yükselişi taşıyamaz. Bu bağlantı hastalık teşhisi koymaz; oturuş ve destek kaybının sonucunu kınanmanın ötesinde eylemsizlik olarak duyurur.

Fātiḥa'daki toplu yöneliş, kulluk ile yardım istemeyi aynı muhataba yönelen iki ayrı fiilde birleştirir (1:5): {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:Yalnız Sana kulluk eder ve yalnız Senden yardım isteriz}. Öne alınan {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız Sana} her iki fiilin de nesnesidir. Böylece odaktaki tapınma nesnesi ve kesilen destek, tek muhataba yönelen kulluk ve yardım isteme pratiğinin olumlu karşı kutbunda belirir. Bu karşılaştırma 17:22'yi duaya ya da aynı konuşanın sözüne dönüştürmez; Fātiḥa'nın ilk çoğul toplu pratiğinde ayrı fiillerin aynı muhataba yönelmesini gösterir.

</source_prose>
