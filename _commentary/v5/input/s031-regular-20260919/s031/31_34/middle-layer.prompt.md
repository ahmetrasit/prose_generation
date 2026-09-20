# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:34**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.middle.claims.json`

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
- Refer to source paragraphs as `31:34 ¶N`.

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

`(31:34 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:34",
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
        "citation": "(31:34 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_34/31_34.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_34/31_34.middle.claims.json \
  --ayah-ref 31:34
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_34/31_34.prose.editorial.tr.md`

<source_prose>
## Bilginin Çerçevesi

31:34’ün açılışındaki {ar:إِنَّ, tr:inna, gloss:kuşkusuz} bildirimi, üç ilahî yüklemin ve insanın bilmediğini söyleyen iki cümlenin ardından ikinci kez {ar:إِنَّ, tr:inna, gloss:kuşkusuz} ile döner. İlkinde Allah’ın adı {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} olarak öne çıkar; kapanışta da {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} aynı ilahî ad yeniden anılır. Böylece iki ayrı insan sınırı—yarının kazancı ve ölümün yeri—araya girse de cümlenin öznesi dağılmaz: başlangıçtaki bildirim, son bildirimde tamamlanır.

İlk ilahî söz, bilginin yerini öne çıkaran {ar:عِندَهُۥ, tr:ʿindahu, gloss:O’nun katında} ifadesidir. Kişiye bağlı iyelik eki bu aidiyeti kurar; ifade, ayrı bir tamlama olan {ar:عِلْمُ ٱلسَّاعَةِ, tr:ʿilmu as-sāʿati, gloss:Son Saat bilgisi} gelmeden önce yer aldığı için bilgi alanını daha adı konmadan belirginleştirir. İlk söz Saat’in kendisini değil, ona ilişkin bilgiyi konuya taşır. Bu öne alış, söz konusu bilginin Allah katındaki yerini vurgular; ayet bu yerel bilgi sınırını kurarken insanların başka konularda bilgi edinebilmesini açık tutar.

{ar:ٱلسَّاعَةِ, tr:as-sāʿati, gloss:Saat} zamanın sürmesini ya da belli bir zaman kesitini de adlandırabilir; belirli artikel ve bilgi tamlaması içindeki yeri, ilk sözü belirsiz bir vakitten Son Saat’e daraltır. Ölüm ufku ve kapanıştaki ilahî bildirim bu eskatolojik anlamı belirginleştirir: burada dünyanın sona erip insanların diriltileceği hesap vakti söz konusudur. Aynı bilgi ailesinin ayette isim olarak başlaması, sonra etkin bilme fiilinde ve kapanış niteliğinde belirmesi de bu ilk sözün ötesine uzanacak bir çizgi açar.

Bu yerel çizgide {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} bilinen alanı adlandırır, {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} rahimlerde olana yönelen etkin fiil olarak döner, {ar:عَلِيمٌ, tr:ʿalīmun, gloss:her şeyi bilen} ise kapanışta niteliğe dönüşür. Aynı kökün isimden fiile, fiilden niteliğe geçmesi, Saat bilgisi ile rahimdekini bilme arasında biçimsel bir hat kurar; çizginin hareketi bilmenin kapsamından çok cümledeki kuruluş biçimindedir.

## Yağış ve İçte Taşınan

Bilgi tamlamasının ardından gelen {ar:وَ, tr:wa, gloss:ve} yeni bir yüklem başlatır. {ar:يُنَزِّلُ ٱلْغَيْثَ, tr:yunazzilu l-ghaytha, gloss:yağmuru indirir} yağışı yukarıdan aşağı gönderilen somut bir şey yapar; II. kalıp ve şimdiki-geniş zaman, bu inişi aşamalı ya da yinelenen bir gönderiş olarak duyurabilir. Ayet gönderişin ritmini ve zamanını belirlemez. Doğrudan nesne olan {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:rahatlatıcı yağmur}, sıkıntıyı gideren yağmur anlamını taşır; yağmurun Allah tarafından indirilmesi de bu değeri eyleme bağlar. Böylece ayet belirli bir kuraklık olayını anlatmadan yağışın rahatlatıcı niteliğini öne çıkarır.

Yağmur adının iki sözlük kullanımı aşağı iniş görüntüsünün çevresinde ayrı katkılar sunar. Tek bir sözlük tanıklığında {ar:غَيْث, tr:ghayth, gloss:yağmur} bulut için de kullanılır; indirme fiilinin yukarıdan yere yönü, bu tanıklıkla birlikte bulutu taşıyıcı olarak sezdirir. Ayette bulut adı geçmediği için bu, taşıyıcıyı ayrıca sahneye koyan bir iddia değil, tek tanıklığa dayalı sınırlı bir çağrışımdır. Başka bir kullanımda aynı ad yağmurun kendisinden ziyade yağmurla yetişen otu ya da bitkiyi adlandırır. Bu bitki kullanımı, suyun ardından görülen büyümeyi yağmur adının sözlük çevresine bağlar; 31:10’daki çok sayıda bitki örneği bu büyümeyi tek türe kapatmadan belirginleştirir (31:10).

İndirme eylemi, Allah’ın özne olduğu bazı sözlük yapılarında iyilik, ceza ya da bildirinin insanlara ulaşmasını da anlatır. 31:31 ve 31:32’de geminin dalga yüzünden tehlikeye düşmesi, ardından yolcuların kurtarılıp karaya ulaştırılması bu ulaştırma yüzüne somut bir sahne verir. Gemi taşıyıcıdır; dalga yolu keser; kurtarılma tehlikeden sonraki varışı, kara da ulaşılan yüzeyi kurar. Buradaki temas, indirme fiilinin yardımın insanlara ulaşması kullanımı ile kurtarılma sırası arasındadır: yolcular yağmur alan kişiler değil, dalgadan kurtarılanlardır ve bu kurtuluş yağışın sebebi olarak anlatılmaz. {ar:ٱلْغِيَاث, tr:al-ghiyāth, gloss:sıkıntıyı gideren yardım} biçimi de darlığı gideren yardımı adlandırır. Bunun {ar:غَيْث, tr:ghayth, gloss:yağmur} ile kök bağı kesin olmadığından iki biçim arasındaki temas, yağışla denizden kurtuluşu özdeşleştiren bir bağ değil, ihtiyatlı bir sözlük yankısıdır.

Yağışın darlığı gideren yardımı, umutsuzluğun ardından yağmurun indirildiği ve Allah’ın merhametinin yayıldığı anlatıda açık karşılık bulur (42:28). Burada {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} rahatlamayı, {ar:يُنَزِّلُ, tr:yunazzilu, gloss:indirir} ise iyiliğin ihtiyaç sahibine ulaşmasını duyurur. Bu yağış-yardım teması özellikle 42:28’deki umutsuzluk-sonrası yağmura dayanır; 31:31-32’deki deniz yolculuğu ise kurtarılmanın ayrı sahnesidir. Yeryüzünün su alıp yeniden canlanması da yağmurun hayatı sürdürme gücünü başka bir maddi görüntüyle açar (30:24). Böylece yağış, meteorolojik anlamını koruyarak hem darlığın giderilmesiyle hem suyu alan toprağın dirilmesiyle birlikte duyulur.

Gökten yere ulaşan suyun ardından cümle içeriye yönelir: {ar:وَيَعْلَمُ مَا فِى ٱلْأَرْحَامِ, tr:wa-yaʿlamu mā fī l-arḥāmi, gloss:ve rahimlerde olanı bilir} yeni bir bilme yüklemidir. Yan yana duran iki yüklem iki bağımsız ilahî eylem kurar: yağmur indirilir, rahimlerde olan bilinir. Açık uçlu {ar:مَا, tr:mā, gloss:ne varsa}, bilinen içeriği tek bir özellik ya da insanın inceleyebileceği sabit listeyle sınırlamaz. {ar:فِى, tr:fī, gloss:içinde} bu açık içeriği iç mekâna yerleştirir; belirli çoğul {ar:ٱلْأَرْحَامِ, tr:al-arḥāmi, gloss:rahimler} de yavrunun oluştuğu, geliştiği ve taşındığı gerçek üreme organlarını adlandırır. Odak soyut üreme kavramı değil, rahimlerin içinde bulunan içeriğe yönelen bilme fiilidir.

Rahim sözcüğünün bedensel organ anlamı sabit kalırken kök ailesi, içinde taşınan hayatı ve yakın soy bağını da duyurur. Sûrenin başındaki besmele içindeki {ar:ٱلرَّحْمَٰنِ, tr:ar-Raḥmān, gloss:çok merhametli} ve {ar:ٱلرَّحِيمِ, tr:ar-Raḥīm, gloss:esirgeyen} adlar aynı kök ailesinde merhameti, acınanı korumaya ve iyilik etmeye yönelen bir yürek hareketi olarak anlatır (S:0); odaktaki {ar:ٱلْأَرْحَامِ, tr:al-arḥāmi, gloss:rahimler} ise doğum bağını taşıyan gerçek organları adlandırır. Umutsuzluk ardından yağmurla birlikte anılan {ar:رَحْمَتَهُۥ, tr:raḥmatahu, gloss:O’nun merhameti} bu aileye ayrı bir bağlamda yeniden temas eder (42:28). Rahim sözü ortak doğum kaynağı üzerinden akrabalığa açılır: ebeveynle çocuğun birbirinin yerine geçememesi bu bağı gösterir (31:33), rahimdeki oluşumun vadeye bağlanması ise onu zamana yerleştirir (22:5).

Zaman, rahim imgesini sabit bir kap görünümünden süre içinde değişen gelişime doğru genişletir. Rahimde taşınanın azalması ve artması içeriğin değişimini, oluşumun aşamaları ve belirlenmiş süresi de bu gelişimin ölçüsünü gösterir (13:8, 22:5). Odaktaki {ar:مَا فِى ٱلْأَرْحَامِ, tr:mā fī l-arḥāmi, gloss:rahimlerde olan} o andaki gizli içeriği adlandırırken, bu iki bağlam onu oluşup değişen bir süreç olarak düşünmeye açar. Anne, taşıma ve zayıflık üstüne zayıflıkla bedensel maliyeti yaşar; sütten kesilme ayrılığı getirir, iki yıllık ölçüyü de daha sonraki yöneliş izler (31:14). Bu ayrı anne-çocuk çizgisi rahimdekini zaman içinde biçimlenen bir hayat olarak duyurur; taşıma, ayrılma ve ölçülü süre ayrıntıları da 31:14’ün kendi gelişme çizgisini korur.

{ar:عِندَهُۥ, tr:ʿindahu, gloss:O’nun katında} ifadesi yer ve aidiyet anlamını koruyarak gelişimi ölçü çerçevesine alır: her şeyin O’nun katında bir ölçüyle oluşu ile rahimde taşınanın değişimi birlikte anılır (13:8). Gizliyle açığın ve insanların kazancının bilindiği başka bir ifade, aynı bilgi alanını iç süreçten görünen eyleme taşır (6:3). Böylece bilgi sabit içerik kadar oluşum ve eylem boyunca da işler. İnsan bu çerçevede plan yapar, çalışır ve bazı şeyleri öğrenir; 13:8’deki ölçü, odaktaki “O’nun katında” ifadesini bu eylemler üzerinde nedensel denetim olarak tanımlamaz.

Bu iç süreç, 31:10’daki başka bir gelişme sahnesiyle görünmeyen koşulların görünür etkilerine açılır. Göklerin gözle görülen direkler olmadan durması, ardından görme, su ve bitki büyümesinin gelmesi, gözlenen düzenin dayanakların tamamını tüketmediğini düşündürür. Odaktaki {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} ve {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} olağan bilme anlamlarını korurken, bilgi ailesindeki ayırt edip yol gösteren belirti kullanımı bu görünür düzene temas eder. Görünür direklerin bulunmayışı, düzenin bütün dayanaklarının gizli olduğunu kanıtlamaz; bu sahnenin katkısı, görülen etkinin dayanakların tamamını açmamasıdır. Aynı sahnede sudan sonra birçok türün büyümesi, {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} adının yağmurla yetişen ot ya da bitki anlamındaki ayrı kullanımını harekete geçirir. Odakta {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} gerçek yağışı adlandırır; sözlükteki bitki kolu ise suyun ardından gelen görünür büyümeyi bu ada bağlar.

İniş ile gelişmenin maddi yakınlığı, kökün biçimce ayrı bir sözlük kullanımını da çağrıştırır: ayrı bir ad erkek üreme sıvısının boşalma sırasında dışarı çıkışını anlatır. Odaktaki {ar:يُنَزِّلُ, tr:yunazzilu, gloss:aşağı indirir} fiili bu addan farklı biçimdedir ve ayette yağmurun inişini anlatır. 31:10’da {ar:مَاءً, tr:māʾan, gloss:su} bitki büyümesinden önce gelir; suyun inişi ve ardından büyüme, odaktaki {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} ile {ar:ٱلْأَرْحَامِ, tr:al-arḥāmi, gloss:rahimler} yan yanalığına maddi temas kurar. Bu sıra—dışa iniş, içte karşılanış, görünür gelişme—yağmur okumasını genişleten uzak ve üretken bir imgedir. 31:10’daki bitkiler bitki olarak kalır, ayrı sözlüksel ad da odaktaki fiilin anlamına geçmez; bu bağlantı bedensel ya da embriyolojik bir açıklama değil, maddi süreçler arasındaki benzetmedir.

## Yarın İçin Yönelen Can

Üç ilahî yüklemin ardından gelen {ar:وَمَا تَدْرِى نَفْسٌ, tr:wa-mā tadrī nafsun, gloss:ve hiçbir can bilmez} sözü cümlenin yönünü insanın kendi geleceğine çevirir. İlk {ar:مَا, tr:mā, gloss:bilmez} olumsuzluğu, {ar:تَدْرِى نَفْسٌ مَاذَا تَكْسِبُ غَدًا, tr:tadrī nafsun mādhā taksibu ghadan, gloss:bir canın yarın ne kazanacağını bilmesi} içindeki sorunun tamamını kapsar: kazanma eylemi vardır, açık kalan onun yarınki içeriğidir. Buradaki {ar:مَاذَا, tr:mādhā, gloss:ne}, doğrudan muhataba yöneltilen bir soru değil, kazancın ne olduğunu açan gömülü sorudur.

Bu soru, eyleyen kişiyi edilgin bir bekleyene dönüştürmez. {ar:تَكْسِبُ, tr:taksibu, gloss:kazanır, edinir} kendisi için yarar sağlayacak bir şeyi arayıp elde etmeyi anlatır; açık kalan “ne” ve yakın zaman bildiren {ar:غَدًا, tr:ghadan, gloss:yarın} eylemi görünür kılarken sonucunu belirsiz bırakır. “Yarın” uzak bir yazgıdan çok planlama ve çalışma ufkudur. Ayet kazancın iyi ya da kötü değerini ve kasıtlı bir zarar niyetini belirtmez; fiilin katkısı kişinin yarara yönelen eylemini, sorunun katkısı ise elde edeceği şeyin bilinmezliğini öne çıkarmaktır.

{ar:تَدْرِى, tr:tadrī, gloss:önceden bilir ve kavrar} fiilinin algı ve deneyimle kavrama yönü bu sınırı kişiselleştirir: insan soyut bir bilgi maddesinin yanında kendi yakın geleceğini de önceden kavrayamaz. Belirsiz tekil {ar:نَفْسٌ, tr:nafsun, gloss:her bir can} bu sınırı her kişiye ayrı ayrı yükler. Kelime ailesindeki soluk alıp verme kullanımı yaşayan benlik etrafında ince bir yankı oluşturabilir; odaktaki “can” yaşayan kişiyi adlandırır, nefes alıp verme eyleminin kendisini değil.

Bilmemek anlamı sürerken {ar:تَدْرِى, tr:tadrī, gloss:bilir} ailesindeki ayrı bir sözlük kullanımı, avcının hedefi henüz açıkça görmeden aramasını, gizlenerek aldatmasını ve yaklaşma fırsatını kollamasını anlatır. Bu avcılık kolu hedefi izleme, gizlenme ve yaklaşma fırsatıyla sınırlıdır; avı vurma ya da tuzak kurma eylemlerini içermez. Yarınki kazanç sorusu ile dünya hayatının aldatmasına karşı uyarı bu görünmeyen hedef imgesini aynı yerde etkinleştirir (31:33): biri henüz bilinmeyen getiriyi, diğeri aldatıcı dünya hayatını gündeme getirir; iki kolun temas noktası görünmeyen bir hedefe yönelen arayıştır. Böylece kişi, {ar:تَكْسِبُ, tr:taksibu, gloss:kendisi için yarar arayıp edinir} fiilinin verdiği etkin kazanç arayışıyla, göz önünde olmayan bir sonuca yönelen takipçi gibi görünür. 31:33’teki uyarının katkısı çalışmayı değil, aranan getiriyi güvence saymayı sınırlar.

Rahimlerde taşınanla gelecek kazanç arasında ikinci, biçimi ayrı bir yankı vardır. Odaktaki {ar:غَدًا, tr:ghadan, gloss:yarın} ertesi gündür; biçimce farklı {ar:ٱلْغَدَوِيّ, tr:al-ghadawī, gloss:doğmamış yavruya ilişkin} kullanımı gebe hayvandaki doğmamış yavruyu ve o yıl beklenen yavru üzerine yapılan belirsiz bir satışı adlandırır. Yavru imgesi rahimdeki gizli içeriğe, satış kolu ise yarar arayışına temas eder; 31:33’teki dünya hayatının aldatıcılığı bu iki beklenen getiriyi aynı risk çerçevesinde buluşturur. Bu sözlüksel yankının katkısı, beklenen kazancın güvence olmadığını duyurmaktır. Satış kullanımı bir alışveriş hükmü kurmaz; odaktaki ghadan “yarın”dır, yavru değildir ve sözlük bağı herhangi bir gebelik aşaması belirlemez.

Geleceğe yönelmek gerçek bir niyet ve çalışma alanı bırakır. Bir işi yarın yapacağını kesin söyleme uyarısı ile her benliğin yarın için ne hazırladığına bakma çağrısı, bilme sınırı içinde eylemin sürdüğünü gösterir (18:23, 59:18). {ar:غَدًا, tr:ghadan, gloss:yarın} doğrudan ertesi gündür; aynı söz ailesindeki günün ilk vakti ve o vakitte yola çıkma kullanımı, kişinin yarın için niyetiyle ve {ar:تَكْسِبُ, tr:taksibu, gloss:kazanır} eylemiyle başlangıç-yol imgesi kurar. Bu temas benzetme düzeyindedir: günün ilk vakti yola çıkışı görünür kılar, varışın bilgisi ise insan için açık kalır. Böylece yarın boş bir takvim etiketi değil, kişinin yarar arayarak yöneldiği ufuk olur.

Bu eylem kişiye aittir. Her benliğin yarın için hazırlığı ve kendi kazancıyla anılması işi yapanla yararı göreni aynı kişide buluşturur (59:18, 6:164); şükredenin kendi benliği için şükretmesi de bu yönü pekiştirir (31:12). {ar:كَسَبَ, tr:kasaba, gloss:kendi kazancını edinir} kendi yaşayan benliğinin eylemini anlatır. Hiç kimsenin başkasının yükünü taşımaması ve ebeveynle çocuğun birbirinin yerine geçememesi kişisel sorumluluğu en yakın bağda görünür kılar (6:164, 31:33). Bu hükümler hesapta yükü ya da kişinin yerini başkasına devretmeyi sınırlar; bakım, akrabalık ve gündelik ortak sorumluluğu olduğu gibi bırakır. Rahimlerdeki bağımlı başlangıç gerçek kalırken, her kişinin kendi kazancı ve sonu başka birinin güvencesine dönüşmez.

## Ölümün Yeri

İkinci insan cümlesi ilk sınırı sürdürürken soruyu “ne kazanacağı”ndan “hangi yerde öleceği”ne çevirir. {ar:وَمَا تَدْرِى نَفْسٌ, tr:wa-mā tadrī nafsun, gloss:ve hiçbir can bilmez} özneyi yeniden kurar; ikinci belirsiz tekil {ar:نَفْسٌ, tr:nafsun, gloss:her bir can} yine her kişiyi tek tek düşündürür. Yeni {ar:مَا, tr:mā, gloss:bilmez} bu defa yer sorusunu yönetir. Tekrarlanan {ar:تَدْرِى, tr:tadrī, gloss:bilir ve kavrar} algı sınırını zamansal sonuçtan mekânsal son noktaya taşır. {ar:تَمُوتُ, tr:tamūtu, gloss:ölür} ölümü gerçekleşecek bir olay olarak bildirir; açık kalan, onun nerede gerçekleşeceğidir.

{ar:بِأَيِّ أَرْضٍ, tr:bi-ʾayyi arḍin, gloss:hangi yerde} içindeki {ar:بِ, tr:bi, gloss:-de} soruyu yer ilişkisine bağlar; mekân, ölüm bilgisinin bilinmeyen parçasıdır. Seçici {ar:أَيِّ, tr:ʾayyi, gloss:hangi}, bilinen yer kategorisinden hangi üyenin söz konusu olduğunu sorar; belirsiz {ar:أَرْضٍ, tr:arḍin, gloss:bir yer, bir toprak} genel yeryüzünü değil, adı verilmeyen belirli yeri düşündürür. Olumlu gelecek fiili {ar:تَمُوتُ, tr:tamūtu, gloss:ölür} ölümün gerçekleşeceğini bildirirken yeri açık bırakır. Böylece cümle ölümün kesinliğiyle yer bilgisinin bilinmezliğini birlikte taşır. Bir yabancı yerde bulunan kişiyi anlatan sabit kalıp ayette yer almaz; yine de {ar:أَيِّ, tr:ʾayyi, gloss:hangi} sözcüğünün seçmeli sorusu, canın adı verilmeyen son toprakla ilişkisi üzerinden yersizlik ya da yabancılık yankısı uyandırabilir. {ar:أَرْضٍ, tr:arḍin, gloss:yer} kendi başına “yabancı” demek değildir; cümle bu yeri mezar ya da ölümü yutan toprak diye de tanımlamaz.

Bu bilinmeyen konum, yaşanan yeryüzünün maddi çağrışımlarını da taşır. Yağmurun su verdiği toprak ve suyla yeniden canlanan ölü arazi, yeryüzünü yaşam zemini ve yenilenmeyi kabul eden yüzey olarak düşündürür (22:5, 30:24). Yumuşayıp verimli hâle gelen yüzeyde bitkinin tutunup gelişmesi, {ar:أَرْضٍ, tr:arḍin, gloss:yer} sözüne hayatı kabul eden bir zemin imgesi ekler; böylece toprakta yaşamla ölümün adı yan yana duyulur. Bu maddi çağrışım, ölüm yerini yaşamı kabul eden zeminle yan yana getirir; ayet ölüm yerini verimli diye nitelemez. 30:24’teki ölü arazi imgesi de insan ölümünü anlatmaz; suyla yenilenen yeryüzünün ayrı görüntüsüdür.

Bilme ailesindeki ayrı hedef seçme kullanımı mekânsal soruya yeni bir gerilim katar. “Hangi toprak?” sorusu, kaçılan ölümün insana ulaşmasıyla yan yana geldiğinde kişinin belirleyemediği bir hedef imgesini uyandırır; ölüm vakti ve ölümün kaçanı bulması bu karşılaşmayı somutlaştırır (3:145, 62:8). Odaktaki {ar:تَدْرِى, tr:tadrī, gloss:bilir} olağan bilme fiilidir; hedef seçme imgesi bu sözlük kolundan gelir ve fiilin ayetteki anlamını değiştirmez. {ar:تَمُوتُ, tr:tamūtu, gloss:ölür} yaşamın sona erişini bildirirken ölüm yerini açık bırakır. Hedef imgesi böylece sonun kişiyi buluşunu duyurur; hangi toprağın bu sonu karşılayacağı bilinmez kalır.

Denizden kurtarılıp karaya varma sahnesi aynı bilinmez yere başka bir güzergâh imgesi ekler. Gemi yolun taşıyıcısıdır; seyir doğrultuyu kurar, deniz geniş ve güvensiz bir ara alan oluşturur, yolcuları örten dalga rotayı değiştirir, kurtarılma tehlikeden sonraki varışı ve kara ulaşılan yüzeyi getirir (31:31, 31:32). Bilme ailesindeki yol doğrultusuna ilişkin ayrı kullanım bu sırayla temas eder; odaktaki {ar:تَدْرِى, tr:tadrī, gloss:bilir} bilmek demektir. Bu deniz güzergâhı, ölüm yerini yalnızca koordinat değil, yolcunun önceden çizemediği bir varış yüzeyi olarak duyurur. Gemiyle kurtuluş bağlamı odaktaki ölümü anlatmaz; ayette ölüm yeri adı verilmeyen karasal bir konumdur. İnsanın haritasını çıkaramadığı bu yer, 31:29’da hareket ve belirlenmiş sona erişten sonra yinelenen {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} niteliğiyle ilahî bilgi içine alınır.

Tek tek kişilerin bilinmeyen sonu, çokluğun diriltilmesinin tek bir canınkiyle karşılaştırıldığı sözün yanında yer alır (31:28). Odaktaki her {ar:نَفْسٌ, tr:nafsun, gloss:can} kendi yarınını ve ölüm yerini bilmez; 31:28’de ise çok sayıda kişinin yaratılması ve yeniden diriltilmesi bir kişinin yaratılmasıyla ölçülür. Tek canla yapılan kıyas, çokluğun ilahî kudret için yaratılış ve dirilişteki kolaylığını gösterir; odaktaki insan sınırı ise her bireyin kendi sonuna ilişkin bilgisizliğidir. Böylece diriltilmenin kudreti ile ölüm yerinin bilinmezliği iki ayrı iddia olarak yan yana durur.

Bu kişisel son ufku, adı başta anılan {ar:ٱلسَّاعَةِ, tr:as-sāʿati, gloss:Son Saat}in kesinliğiyle birlikte geniş bir zaman ölçeğine taşınır. Saat’in gelişinin kesinliği kabirdekilerin diriltilmesiyle yan yana gelir (22:7). Geceyi gündüze, gündüzü geceye geçiren dönüşümler yinelenen geçişleri; görevlendirilen Güneş ile Ay’ın belirlenmiş bir sona doğru akışı da süreli bir varış ufkunu duyurur (31:29). Bu göksel döngüler Saat’i tarihlemez; Güneş ve Ay’ın belirlenmiş süresi de Saat’in kendisi değildir. Böylece kişinin ölüm yerini bilmemesiyle toplumun Saat’in tarihini bilememesi farklı ölçekte, sonu kesin ama takvimi insana açık olmayan iki ufuk oluşturur.

31:34’ün sıralaması bağımsız bilinmezleri bir hayat-geçim güzergâhında birbirine yaklaştırır. Başta O’nun katında anılan {ar:عِلْمُ ٱلسَّاعَةِ, tr:ʿilmu as-sāʿati, gloss:Son Saat bilgisi} zaman ufkunu açar; ardından {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} dışarıdan gelen akışı, {ar:ٱلْأَرْحَامِ, tr:al-arḥāmi, gloss:rahimler} içte taşınan gelişimi, {ar:تَكْسِبُ, tr:taksibu, gloss:kazanır} kişinin yönelişini, {ar:بِأَيِّ أَرْضٍ تَمُوتُ, tr:bi-ʾayyi arḍin tamūtu, gloss:hangi yerde öleceğini} de yaşamın son konumunu duyurur. Bu diziliş yağıştan rahimdeki hayata, oradan kişinin edinimine ve ölüm yerine uzanan okuma hareketi kurar; yağmur kişisel kazancın nedeni, bitki kolu belirli bir hasadın vaadi değildir ve ölüm yeri verimli diye nitelenmez.

## Kayıt, Büyüme ve İç Yüz

İnsana açık kalan zaman ve yer ufukları, 31:27’de sonlu kayıt araçlarıyla yan yana gelen yazı görüntüsünde başka bir ölçü kazanır. Bilgi önce {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} adıyla, sonra {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} fiiliyle görünür; kapanıştaki {ar:عَلِيمٌ, tr:ʿalīmun, gloss:her şeyi bilen} bu bilme çerçevesini niteler. Ağaçların {ar:أَقْلَٰمٌ, tr:aqlām, gloss:kalemler} olması yazının maddi aracını, {ar:ٱلْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:al-baḥru yamudduhu min baʿdihi sabʿatu abḥur, gloss:deniz ve ardına eklenen yedi deniz} ise kaydedilecek şeyin bolluğunu büyütür (31:27). {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāh, gloss:Allah’ın kelimeleri}nin tükenmeyeceği bildirimi, insanın kalem ve denizle kurduğu sonlu kayıt imkânını aşan, iletilebilir bir ifade bolluğu açar (31:27). Denizin kalemlere sürekli mürekkep verdiği hokka resmi bu sahneden çıkarılabilecek ihtiyatlı bir yorumdur; ayette hokka ayrıca adlandırılmaz. Görünmeyenler hakkındaki bu kayıt imgesi insanın yarın ve ölüm yeri konusunda kaydedebileceği bilginin sınırını gösterir; ilahî bilginin ölçüsünü sunmaz.

Yazı görüntüsünden ayrı olarak aynı malzemeler suyun depolanması, akışı ve kabulü biçiminde buluşur. Bilgi kelimesinin kök çevresinde yer alan, biçimce ayrı {ar:عَيْلَم, tr:ʿaylam, gloss:deniz veya suyu bol kuyu} adı deniz ya da suyu bol kuyu için kullanılır; 31:27’deki {ar:ٱلْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:al-baḥru yamudduhu min baʿdihi sabʿatu abḥur, gloss:deniz ve ardından eklenen yedi deniz} bu seçeneklerden denizi seçerek bilgi için bir rezervuar imgesi açar. Odaktaki gerçek {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} depodan dışarı ulaşan su akışına karşılık gelir. Kapanıştaki {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} Allah’ın niteliğidir; biçimce ayrı {ar:ٱلْخَبْرَاءُ, tr:al-khabrāʾ, gloss:yumuşak, alçak ve su tutan arazi} kullanımıysa suyu alıp tutabilen yüzeyi sunar. Böylece imge depoda saklanan suyu, dışarıya akan suyu ve onu kabul eden zemini kendi işlevleriyle birbirine bağlar. Ardından denize eklenen yedi deniz depo imgesinin kapasitesini sonlu ölçünün ötesine taşır; {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāh, gloss:Allah’ın kelimeleri} de bu maddi bolluğa ifade boyutu ekler (31:27). Bu benzetmede deniz yağmurun kaynağı yapılmaz, bilgi suyla özdeşleşmez ve alıcıların sınırlılığı eşit paylara ilişkin bir iddia kurmaz; imge ilahî bilginin tükenmezliğini ve hayata ulaşan akış gibi düşünülebilmesini taşır.

Bu ifade bolluğu, görünür olay ile gizli içeriğin farkını keskinleştirir. Görünen {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} ile rahimde taşınan içerik, her canın geleceği ve ölüm yeri yan yana geldiğinde, {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} ve {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} ailesindeki ayırt edip tanıtan belirti kullanımı yağmuru bir alamet gibi duyurabilir; ayet yağmuru adıyla “işaret” diye nitelemez. Yağmur görünür olay olarak kalır; rahim içeriği, yarınki kazanç ve ölüm yeri ise örtüktür. Kapanıştaki {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} ve {ar:عَلِيمٌ, tr:ʿalīmun, gloss:her şeyi bilen} bu alanı geniş bilme ve iç yüzü kavrama yönleriyle karşılar. Rahmin yavrunun oluşup taşındığı gerçek iç oda oluşu ve {ar:فِى, tr:fī, gloss:içinde} ilişkisinin kapalı bir iç alan kurması, görünür yağıştan gizli içeriğe geçişi somutlaştırır. Bu temas görünür yağmuru gizli içerik için insanın çıkarım aracına dönüştürmez; yağış ile örtük kalanlar arasında bir karşıtlık kurar.

31:10’daki sahne göğün gözle görülen direkler olmadan duruşunu, ardından görme, su ve bitki büyümesini yan yana getirerek dikkati görünür etkinin ardındaki koşullara yöneltir. Odaktaki {ar:مَا فِى ٱلْأَرْحَامِ, tr:mā fī l-arḥāmi, gloss:rahimlerde olan} içeriğin azalması ve artması da değişen bir süreç gösterir (13:8). Bu iki temas, görünen sonuçların ardında görünmeyen dayanakların bulunabileceği düşüncesini açar; direklerin görünmemesi bütün destekleri gizli saymayı değil, gözlenen düzenin dayanakların tamamını açmadığını gösterir. Aynı 31:10 sahnesinde sudan sonra birçok bitki türünün büyümesi, {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} adının yağmurla yetişen bitki anlamındaki ayrı kullanımını harekete geçirir. Odaktaki {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} yağışı adlandırır; su, bitki türleri ve rahim içeriği bu imge ilişkisinde ayrı taşıyıcılar olarak kalır. {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} ve {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} ailesindeki belirti kullanımı görünen büyümeyi gizli süreçler için bir ipucu hâline getirir. Bu ipucu her gizli nedenin görünür etkisi bulunduğunu ileri sürmez; görülen büyümenin kendi koşullarının tümünü tüketmediğini gösterir.

Gizli bir sonucun ortaya çıkışı, ağırlığı belirlenen hardal tanesinin kayanın, göklerin ya da yerin içinde olsa da konumunun bilindiği ve sonra getirildiği sahnede somutlaşır (31:16). Bu görüntü, {ar:تَكْسِبُ, tr:taksibu, gloss:kazanır} ile odaktaki yarınlık kazanca temas eder: insan için sonucu bilinmeyen kazanç yoklukta değildir; küçücük ve saklı olsa da bilinir ve ortaya getirilebilir. Belirlenen ağırlık taneyi ölçülebilir kılar; kayanın, göklerin ya da yerin içindeki konumu gizliliğin kapsamını, getirilmesi de gizliden görünür sonuca geçişi kurar. Hardal tanesinin büyüme ihtimali bu ölçme ve getirme çizgisinin yanına ayrı bir gelişme dalı ekler. 31:16’nın kapanışındaki {ar:خَبِيرٌ, tr:khabīrun, gloss:iç yüzünden haberdar} içi tanıyan niteliği geri çağırır; sahne hesaplaşma olarak da okunabilir. Hardal tanesi burada kazanılmış şeyin ölçüsü değil, küçücük gizli sonucun bile bilinip ortaya çıkmasının maddi imgesidir.

İç yüzü bilme, görünür nimetlerle gizli kalanların, yapılan işlerle göğüslerde saklı olanın ve dönüşün yan yana getirildiği yerde eyleme uzanır (31:20, 31:23). Gönüldeki yönelim ile dışarıdaki iş ayrı düzlemlerdir; bu iki alan yine de gizli içten işe ve bildirilecek sonuca uzanan bir ilişki kurar. Kapanıştaki {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} durağan gizli içerikle birlikte iç yönelim ve dış eylemin temas ettiği alanı da kavrar. Yaratan’ın yarattığını bilip bilmediğini soran ve O’nu {ar:ٱلْخَبِيرُ, tr:al-khabīru, gloss:iç yüzünden haberdar} diye anan ifade bu iç derinliği yeniden hatırlatır (67:14). Bu ayrı kuruluş, odaktaki {ar:عَلِيمٌ, tr:ʿalīmun, gloss:her şeyi bilen} kapsamı ile {ar:خَبِيرٌ, tr:khabīrun, gloss:iç yüzünü bilen} niteliğinin iç bilgiye erişimini yan yana getirir. Ayetlerin dilbilgisi farklıdır; bu sıfat da tek bir teknik anlama kapanmaz. Bağlantı iç yönelimle görünen eylemi ilahî bilgi içinde birlikte düşünmeye açar, her iş için tek bir gizli neden varsaymaz.

Başta öne alınan {ar:عِلْمُ, tr:ʿilmu, gloss:bilgi} adı ile ortadaki {ar:يَعْلَمُ, tr:yaʿlamu, gloss:bilir} fiilinden sonra, insanın iki olumsuz cümlesine yeni bir ilahî bildirim karşılık verir: ikinci {ar:إِنَّ, tr:inna, gloss:kuşkusuz} ile {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} adı geri döner. Kapanıştaki {ar:عَلِيمٌ خَبِيرٌ, tr:ʿalīmun khabīrun, gloss:her şeyi bilen ve haberdar} niteliği bu sözdizimsel dönüşü tamamlar. Daha önceki üç ilahî yüklem ile insanın iki bilinmezi {ar:عَلِيمٌ, tr:ʿalīmun, gloss:her şeyi bilen} altında tek bir geniş bilme alanında buluşur; kapanış bu geniş alanı toplar, her gizli ayrıntıyı tek tek sıralamaz. Ardındaki {ar:خَبِيرٌ, tr:khabīrun, gloss:haberdar} bu genişliğe olayların iç yüzüne nüfuz eden bilgiyi ekler. Haberdarlığın edinilip aktarılabilen bilgi yönü de duyulur; Allah için bu, sonradan öğrenme değil, iç yüzü bilme niteliğidir. Rahim içeriği, yarınki edinim ve ölüm yeri insan için örtük kalırken, geniş bilme ile içeri nüfuz eden haberdarlık aynı kapanışta durur.

</source_prose>
