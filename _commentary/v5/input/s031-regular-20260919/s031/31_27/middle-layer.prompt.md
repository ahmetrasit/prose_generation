# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:27**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.middle.claims.json`

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
- Refer to source paragraphs as `31:27 ¶N`.

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

`(31:27 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:27",
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
        "citation": "(31:27 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_27/31_27.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_27/31_27.middle.claims.json \
  --ayah-ref 31:27
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_27/31_27.prose.editorial.tr.md`

<source_prose>
## Ağaçtan kaleme, denizden söze

Ayetin ilk sesi olan {ar:وَلَوْ, tr:wa-law, gloss:ve eğer}, önceki akışa “ve” ile tutunurken aynı anda yeni bir koşulu “eğer” ile açar. Yeryüzündeki bütün ağaçlar ({ar:شَجَرَةٍ, tr:shajaratin, gloss:ağaç}) kalemler ({ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler}) olsa, deniz ({ar:الْبَحْرُ, tr:al-baḥru, gloss:deniz}) de ardından gelen yedi denizle ({ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz}) beslenip uzasa ({ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:onu uzatır ve besler}), Allah’ın sözleri ({ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri}) yine tükenmez ({ar:مَا نَفِدَتْ, tr:mā nafidat, gloss:tükenmedi}); son niteleme O’nu güçlü ({ar:عَزِيزٌ, tr:ʿazīzun, gloss:güçlü}) ve hikmet sahibi ({ar:حَكِيمٌ, tr:ḥakīmun, gloss:hikmet sahibi}) diye bildirir. Başlangıçtaki kısa ses, önceki sözlerin içeriğini belirlemeden sürekliliği taşır; uzun karşıolgusal kaynak dizisi cevap gelmeden önce kurulur. Âyet böylece tükenme sınırını düşüncede sonuna kadar zorlayan bir varsayım açar; koşul, olmuş bir olayı bildirmez.

Bu varsayımın alanı önce {ar:أَنَّمَا, tr:annamā, gloss:yeryüzünde ne varsa} ile bütünüyle açılır; {ar:فِي الْأَرْضِ, tr:fī l-arḍi, gloss:yeryüzünde} o bütünün yerini, {ar:مِن شَجَرَةٍ, tr:min shajaratin, gloss:ağaç cinsinden} ise içinden alınacak malzeme türünü kurar. Sözcük sırası okuru önce yeryüzünün tamamına, sonra ağaç cinsine götürür. Buradaki belirli {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü}, bilinen yer alanını tek bir belirsiz arsadan ayırarak bildirir; “içinde” bağlantısı toplam kapsamla ağaç sınıfını birbirine bağlar. “-den”in burun sesiyle ağaç sözcüğünün sonundaki benzer bitiş tür bağını kulağa yaklaştırır; toplam kapsamı ise sözdizimi belirler. Yeryüzü olağan yer anlamını korurken, ağaçların ondan çıkması maddi kaynakların dayandığı zemini de duyurur.

Bu zemindeki {ar:شَجَرَةٍ, tr:shajaratin, gloss:ağaç}, gövdeli ve canlı bitki anlamındadır; tekil-belirsiz biçim tek bir gövdeyi seçmek yerine varsayıma giren ağaç cinsini temsil eder. Ağaç dallanır ve iç içe geçer; sert ucundan kesilip yontularak yazıya hazırlanan {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} bu yapılı canlı malzemeyi araca çevirir. Kalem ailesindeki kesme ve düzeltme kullanımı ağaçla bu karşılaşmada etkinleşir: koşul, kesme işlemini gerçekleşmiş diye anlatmadan olası kalem stokunu düşünceye taşır. Belirsiz çoğul kalemler sayılabilir, envanteri açık bir stok kurar; varsayımın genişliği fiziksel sonsuzluk ya da bütün bir koruluğun gerçekten işlenmesi iddiasına uzanmaz. Ağaçların kalem oluşu ayrıca bir “olmak” fiiliyle değil, koşul içindeki adlandırmayla kurulur.

Ağaçların {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} kalemlere dönüşmesiyle katı araç stoğu kurulunca, {ar:وَالْبَحْرُ, tr:wa-l-baḥru, gloss:ve deniz} sıvı kaynağı olarak yanına eklenir. Standart biçimde merfû gelen deniz, yeni cümlenin öznesi ve ayrı bir malzeme olarak toplamı genişletir; kalemler katı araç stoğu olarak yerinde kalır. Bağlantıdaki “ve” hem eklemeyi hem de ardından gelen deniz-ikmal durumunu koşula bağlayan bir okuma imkânı taşır. Aktarılan kabul edilmiş biçim farklılıkları bu ilişkiyi başka türlü kurabilir; standart yüzeyde deniz ayrı cümlenin öznesi olarak kalır.

Olağan anlamıyla {ar:بَحْرُ, tr:baḥru, gloss:deniz} büyük bir su kütlesidir. Aynı kelime ailesindeki bol ve geniş su, büyük deniz ya da ırmak kullanımları, {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} ile açılan yazı ortamı ve {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} ile karşılaşınca ilk denizi genişleyen bir sıvı rezerv gibi duyurur. Böylece yazı sıvısı yankısı denizin olağan su kütlesi anlamına katman olarak eklenir; deniz kendi başına mürekkep anlamı taşımaz. Tekil denizin kırık çoğulla yeniden görünmesi aynı kaynak türünü çoğaltır. “Yedi” tam ve sayılabilir bir miktardır; belirsiz bolluk ya da sembolik başka bir sayı değil, dünyadaki denizlerin toplamını da bildirmeyen belirli bir sayıdır. Sayının ritmi envantere ağırlık verirken tanvinli {ar:أَبْحُرٍ, tr:abḥurin, gloss:denizler} biçimi daha sonra kapanışta duyulacak ses benzerliğine de zemin hazırlar.

Bu envanterin akışını {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:onu uzatır ve besler} fiili taşır: uzatmak ve destek sağlamak anlamındaki geniş zaman, tek seferlik bir yığın değil varsayım boyunca süren ikmali duyurur. “Onu” zamiri ilk denize döner; {ar:بَحْرُ, tr:baḥru, gloss:deniz} alıcı, {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} ise sonradan gelen kaynaklardır. Fiil ailesi bir alıcıya yiyecek, mal veya başka destek ulaştırmayı; bir su kütlesinin nehir, kuyu ya da başka denizden beslenmesini de karşılar. Bu kullanımlar denizle yedi deniz arasındaki ikmali anlaşılır kılar, fakat ölçülmüş gerçek bir hidrolojik olayı rapor etmez. Fiildeki çift d sesi ve doğrudan alıcıya bağlanan zamir, yenilenme izlenimini kuvvetlendirir; ses, sürenin miktarını tek başına belirlemez.

İkmalin yönünü, fiile bağlanan {ar:مِنۢ بَعْدِهِۦ, tr:min baʿdihi, gloss:ondan sonra ve ötesinden} sözü açar. “Sonra/öte”nin zamiri ilk denize, yani {ar:بَحْرُ, tr:baḥru, gloss:deniz} alıcısına döner; “-den” edatı da bu mesafeyi kaynak ilişkisine katar. Böylece {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} ilk denize göre sıralanır: kaynaklar bağımsız bir yığın değil, ondan sonra gelenlerdir. {ar:بَعْدِهِۦ, tr:baʿdihi, gloss:ondan sonra ve ötesinde} hem tedarik sırasındaki sonralığı hem de öte tarafta bulunma basıncını taşır; uzaktaki yedek kaynak hissi doğar, ama denizler dünyanın dışına yerleştirilmez. “Min”in burun sesi edatıyla mesafe ilişkisini işitsel olarak da bağlar. Fiilin aktarılan okuyuş farklılıkları uzatma, takviye ve yedi denizle uyum olasılıklarını açık tutar; bunlar standart yüzeyin yerine geçmez.

Odaktaki {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} ile ilk deniz {ar:بَحْرُ, tr:baḥru, gloss:deniz} alıcı olunca, {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:uzatıp tedarik eder} fiilinin başka bir kolu da etkinleşir: hokkaya su, boya ya da mürekkep ekleyip sıvıyı yenilemek, kalemi batırmak ve bir yazımlık sıvıyı kaleme aktarmak. Bu işlemler kalemlerin varlığı ve denizin alıcı oluşuyla ayrı ayrı tetiklenir. 96:4’te kalemle öğretme ({ar:عَلَّمَ بِالْقَلَمِ, tr:ʿallama bi-l-qalami, gloss:kalemle öğretti}), 18:109’da ise denizin Rabb’in sözlerine mürekkep oluşu ({ar:مِدَادًا لِكَلِمَاتِ رَبِّي, tr:midādan li-kalimāti rabbī, gloss:Rabbimin sözlerine mürekkep}) açıkça dile gelir (96:4, 18:109). Aynı 18:109 denizin Rabb’in sözleri tükenmeden önce tükeneceğini de söyler ({ar:لَنَفِدَ الْبَحْرُ قَبْلَ أَن تَنفَدَ كَلِمَاتُ رَبِّي, tr:la-nafida l-baḥru qabla an tanfada kalimātu rabbī, gloss:deniz Rabbimin sözlerinden önce tükenirdi}; 18:109). Bu karşılaştırma sınırlı yazı sıvısıyla sözler arasındaki ölçü farkını açar. Hokka ve mürekkep işlemleri böylece görünür olur; odaktaki deniz yine su kaynağı, fiil ise uzatma ve tedarik eylemidir. Sınırlı kalem ile yenilenen sıvı, sözleri taşıyan bir yazı düzeni kurar; bu düzen anlamın maddi izlerle iletilebildiğini gösterir, bütün sözlerin fiilen yazıya geçirildiği bir üretim sahnesi kurmaz.

Malzeme dizisi tamamlandıktan sonra {ar:مَا, tr:mā, gloss:hayır} kısa bir eşik kurar: geçmiş biçimdeki {ar:نَفِدَتْ, tr:nafidat, gloss:tükendi} tamamlanmış tükenmeyi olumsuzlar. Fiil önce geldiğinden yanıt gecikir; ardından özne olan {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} belirir ve tükenmeme hükmünün kalemlere ya da denizlere değil sözlere ilişkin olduğunu gösterir. Cansız çoğul “sözler” ile fiilin dişil tekil biçimi arasındaki Arapça uyum da bu yapıyı taşır. Burada bir fail sözleri tüketen geçişli eylem yapmaz; olumsuzlanan şey tamamlanmış tükeniştir. Kısa {ar:مَا نَفِدَتْ, tr:mā nafidat, gloss:tükenmedi} yanıtının ardından {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri} tamlaması uzayıp kapanışı genişletir.

Bu {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} çoğulu tek tek anlam taşıyan birimleri ve söylenen sözleri kapsar; Arapça çoğul en az üçü duyurur, fakat kesin toplam vermez. {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} kalemlerin yüzeyde bıraktığı izler bu birimleri görünür kılar. Aynı kelime ailesinde yara ve ayırt edici iz bırakma, hatta bir hayvanı yaralayarak ona iz kazandırmaya özgü kullanım da vardır; kalemin çizgisi bu bağımsız izi tetikleyince söz yazıda etkili bir işaret gibi duyulur. Bu, sözleri bedensel yaraya dönüştürmez: olağan anlamları yine söylenen ve anlam taşıyan sözlerdir. Ayrıca uzunluk ve bağlantı yönündeki {ar:يَمُدُّ, tr:yamuddu, gloss:uzatır} anlamları birimler arasındaki uzayan diziyi düşündürür. Maddi yazı sayılabilir izler bırakabilir; bu uzama bütün sözlerin fiziksel olarak yazıldığı ya da yazının sonsuza dek sürdüğü iddiasını gerektirmez.

“Allah’ın sözleri” tamlamasında {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri} Allah adı sözlerin kaynağını belirler. Burada genel bir unvan değil özel addır; olası türeyiş açıklamaları bu yerel görevini değiştirmez. Aynı ad önce genitif biçimiyle sözlere bağlanır, sonra {ar:إِنَّ ٱللَّهَ, tr:inna llāha, gloss:şüphesiz Allah} içinde belirtme biçimindeki cümle öznesi olarak yeniden gelir. {ar:إِنَّ, tr:inna, gloss:şüphesiz} uzun koşuldan kısa, sıkı bir bildirime geçişi işaretler: kaynak adı şimdi nitelenen özne konumundadır.

Bu özneyi niteleyen {ar:عَزِيزٌ, tr:ʿazīzun, gloss:güçlü ve yenilmez} olağan kudret ve üstünlük anlamını taşır. Sınırlı {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} ve {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} karşısında {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} sözlerinin erişilemez oluşu, aynı ailedeki “az bulunan, zor elde edilen” yönü de çağırır; bu yankı ilahî gücü kıt veya erişilmez bir nesneye dönüştürmez. {ar:حَكِيمٌ, tr:ḥakīmun, gloss:bilge ve hikmet sahibi} bilgelikle birlikte yargılama, sınır koyma ve düzenleme yönlerini açar: yenilenebilir kaynakların başarısız hesabı ölçüsüz birikimle değil, düzenli bir hükümle kapanır. Düzenli söz ya da metin çağrışımı bu kapanışı renklendirir, ancak ayet özel bir hukuk kuralı veya el yazması anlatmaz. İki sıfat eşgüdümlüdür; biri ötekine üstün tutulmaz. Yedi deniz biçimindeki tanvin sesi, son {ar:عَزِيزٌ حَكِيمٌ, tr:ʿazīzun ḥakīmun, gloss:güçlü ve hikmet sahibi} çiftinin bitişiyle envanterden niteliğe işitsel bir köprü kurar. Kapanış, yeni kaynak eklemek yerine bu düzen ölçüsüne varır.

## Yaratılmış alanın sınırları

Bu maddi alanın kime ait olduğu, hemen önceki 31:26’da göklerde ve yerde olanların Allah’a ait olduğunun söylenmesiyle genişler ({ar:لِلَّهِ مَا فِي السَّمَاوَاتِ وَالْأَرْضِ, tr:li-llāhi mā fī s-samāwāti wa-l-arḍi, gloss:göklerde ve yerde olanlar Allah’ındır}; 31:26). Aynı ayet Allah’ı {ar:الْغَنِيُّ, tr:al-ghaniyy, gloss:hiçbir şeye muhtaç olmayan} diye niteler. Odaktaki {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} ve {ar:الْبَحْرُ, tr:al-baḥru, gloss:deniz} bu sahip olunan yaratılmış alanın parçalarıdır; 31:26 bu toplamı okumaya zemin verir, fakat odak cümlesinin sözlük anlamını veya gramerini açıklayan bir sebep değildir. {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:onu destekler} ile dış kaynaklardan beslenen deniz düşüncesi, muhtaç olmayan Allah’la yaratılmış sıvı kaynağı yan yana getirir; odaktaki {ar:مَا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mā nafidat kalimātu llāhi, gloss:Allah’ın sözleri tükenmedi} hükmü de bu ayrımı sözlerin tükenmezliği yönünde kapatır. İki ayetin kendi bildirimleri ayrışırken maddi ikmalin sınırı daha belirginleşir.

Ardından 31:28, yaratma ve diriltmeyi çok kişi ölçeğinden tek bir benlik ölçeğine indirir: {ar:خَلْقُكُمْ, tr:khalqukum, gloss:sizin yaratılmanız} ile {ar:بَعْثُكُمْ, tr:baʿthukum, gloss:sizin diriltilmeniz} karşılaştırılır, {ar:كَنفْسٍ وَاحِدَةٍ, tr:ka-nafsin wāḥidatin, gloss:tek bir benlik gibi} tekliği ölçü yapar (31:28). Odaktaki {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} yaratılmış çoğulluğun büyük bir örneği olarak kalır; bu karşılaştırma Allah’a fiziksel emek veya iş yükü isnat etmez. Sayının büyüklüğü, ilahî kudretin zahmetini ölçmek yerine insan ölçeğinin sınırlılığını gösterir.

31:29’da geceyle gündüzün birbirine geçirilmesi ve güneşle ayın {ar:يَجْرِي, tr:yajrī, gloss:seyreder} biçiminde {ar:لِأَجَلٍ مُّسَمًّى, tr:li-ajalin musamman, gloss:belirlenmiş bir vadeye kadar} sürmesi, odaktaki {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:uzatır ve destekler} için bir zaman karşılığı açar (31:29). Aynı kelime ailesinin süreyi uzatma ve belirli vadeye dek devam ettirme yönü, denizlerin sırayla ikmaline zaman boyutu ekler; {ar:بَعْدِهِۦ, tr:baʿdihi, gloss:ardından} ise kaynak sırasındaki “sonra” anlamını taşır. Gök döngüleri belirlenmiş bir sona giderken, odaktaki {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} için böyle bir vade biçilmez. Geceyle gündüzün birbirine geçirilmesini anlatan {ar:يُولِجُ, tr:yūliju, gloss:birini ötekine sokar} biçimi, {ar:بَحْرُ, tr:baḥru, gloss:deniz} yönünde uzak bir derinlik yankısı uyandırabilir; bu ihtiyatlı çağrışım denizi göksel döngülerin sebebi yapmaz. Güneş ve ayın ölçülü seyri de kapanıştaki {ar:عَزِيزٌ حَكِيمٌ, tr:ʿazīzun ḥakīmun, gloss:güçlü ve hikmet sahibi} düzeniyle yan yana durur; zaman benzetmesi yediyi deyimsel bolluğa veya kehanete dönüştürmez.

Bu belirlenmiş döngülerin ardından 31:30, gerçeğin sabit kalmasını ve batılın boşa çıkmasını söyler ({ar:الْحَقُّ, tr:al-ḥaqqu, gloss:gerçek ve hakikat}; {ar:الْبَاطِلُ, tr:al-bāṭilu, gloss:batıl ve boşa çıkan}; 31:30). Bu karşıtlık, odaktaki {ar:مَا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mā nafidat kalimātu llāhi, gloss:Allah’ın sözleri tükenmedi} hükmüne nicelikten kalıcılığa uzanan bir yankı verir. {ar:حَكِيمٌ, tr:ḥakīmun, gloss:hikmet sahibi} için sağlam, bozulmaya dirençli düzen anlamı da bu kalıcılığı duyurur. Gerçek-batıl ayrımı kendi ayetinin beyanı olarak kalır; insan sözlerinin tümünü yanlış ilan etmez.

Odaktaki denizin ({ar:بَحْرُ, tr:baḥru, gloss:deniz}) {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} kalemlerle kurulan yazı sıvısı imgesinin yanına, 31:31 ve 31:32’de insanların içinden geçtiği başka bir görünüm eklenir. 31:31’de {ar:ٱلْفُلْكُ, tr:al-fulku, gloss:gemi} {ar:تَجْرِي, tr:tajrī, gloss:seyreder} ve {ar:ٱلْبَحْرِ, tr:al-baḥri, gloss:deniz} boyunca ilerlerken Allah’ın {ar:آيَاتِهِ, tr:āyātihi, gloss:O’nun işaretleri} görünür (31:31). 31:32’de {ar:مَوْجٌ كَالظُّلَلِ, tr:mawjun kaẓ-ẓulali, gloss:gölgelikler gibi dalgalar} insanları sarar; onlar Allah’a içtenlikle yakarır ({ar:دَعَوُا ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿawullāha mukhliṣīna lahu d-dīna, gloss:Allah’a içtenlikle yakardılar}) ve O onları karaya çıkarıp kurtarır ({ar:نَجَّىٰهُمْ إِلَى ٱلْبَرِّ, tr:najjāhum ilā l-barri, gloss:karaya çıkararak kurtardı}; 31:32). Bazıları ölçülü kalırken yalnızca hain ve nankör tutumundakiler ({ar:خَتَّارٍ كَفُورٍ, tr:khattārin kafūrin, gloss:hain ve nankör}) işaretleri inkâr eder ({ar:يَجْحَدُ بِآيَاتِنَا, tr:yajḥadu bi-āyātinā, gloss:işaretlerimizi inkâr eder}; 31:32). Böylece deniz, bu bağlamda gemilerin geçtiği ve tehlike taşıyabilen bir ortama genişler; buradaki işaretler {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} ile aynı şey değildir, deniz sahnesi de 31:27’yi gerçek bir kriz anlatısına çevirmeden yeni bir görünüm ekler.

31:33’te ise ebeveyn ve çocuk birbirinin yerine karşılık veremez ({ar:لَا يَجْزِي وَالِدٌ عَنْ وَلَدِهِ, tr:lā yajzī wālidun ʿan waladihi, gloss:hiçbir ebeveyn çocuğunun yerine karşılık vermez}; {ar:وَلَا مَوْلُودٌ هُوَ جَازٍ عَنْ وَالِدِهِ شَيْئًا, tr:wa-lā mawlūdun huwa jāzin ʿan wālidi-hi shayʾan, gloss:çocuk da ebeveyni yerine hiçbir şeyi üstlenmez}; 31:33). Odaktaki {ar:سَبْعَةُ أَبْحُرٍ, tr:sabʿatu abḥurin, gloss:yedi deniz} yedi deniz, ilk denizi —{ar:بَحْرُ, tr:baḥru, gloss:deniz} diye anılan alıcıyı— {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:destekleyip uzatır} fiili ve {ar:مِنۢ بَعْدِهِۦ, tr:min baʿdihi, gloss:ardından} bağıyla sırayla besler; bu en yakın insan bağınınsa yerini dolduracak bir karşılık yoktur. “Karşılık vermek” ailesinin kesme-bölme yönü de {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} kalemlerin ayırdığı çizgileri uzaktan çağrıştırır; bu ikincil ses odaktaki {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} sözlerini bedensel kesik yapmaz. Aile yankısı maddi iz fikrini derinleştirir; ebeveyn-çocuk sahnesi ise denizlerin doğrudan göndergesi veya odak için bir hukuk kuralı değildir.

31:34’te yağmur, denizden farklı bir su kaynağıdır ({ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur}; 31:34). {ar:ٱلْبَحْرُ, tr:al-baḥru, gloss:deniz} ailesindeki tuzlu su ve içmekle dinmeyen şiddetli susama kullanımları, odaktaki yinelenen {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:onu destekler} ile bu yağmur bağlamında bir araya gelir. Bu temas, miktarı artırmanın niteliği güvenceye almayabileceğini düşündürür; yağmurun hayat veren inişi bu farkı belirginleştirir. 31:34’teki {ar:ٱلْغَيْثَ, tr:al-ghaytha, gloss:yağmur} da bu kelime alanına uzak ve belirsiz bir ses yankısı verir, yeni bir anlam kurmaz. Odaktaki deniz bu yüzden tuzlu ya da susatıcı olarak tanımlanmaz: âyet deniz-suyu tamlaması değil, denizi alıcı yapan bir destek fiili kullanır. Kaynağın yeterliliği sınanırken hedef yine {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} olur; {ar:مَا نَفِدَتْ, tr:mā nafidat, gloss:tükenmedi} nicelik hükmü yürürlükte kalır.

Aynı 31:34 insanın bilmediği alanları da sayar: saatin bilgisi, rahimlerde olan, yarının kazancı ve kişinin nerede öleceği; yağmurun indirilmesi de ilahî bilgiye dahildir (31:34). Bu geniş bilinmezlik, odaktaki {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri} ifadesini kapanmış bir kayıt olmaktan çok açılan bir dünya gibi duyurabilir; 31:34’teki her bilginin odak sözlerinde tek tek sayıldığı anlamına gelmez. “Hiçbir benlik bilmez” ifadesindeki {ar:مَا تَدْرِي نَفْسٌ, tr:mā tadrī nafsun, gloss:hiçbir benlik bilmez} ve {ar:تَدْرِي, tr:tadrī, gloss:bilmek} olağan bilme anlamını korur; bol akışa uzanan kök yankısı uzak ve ihtiyatlıdır, bu anlamı değiştirmez. {ar:غَدًا, tr:ghadan, gloss:yarın} yakın geleceği açarken, odaktaki geniş {ar:فِي الْأَرْضِ, tr:fī l-arḍi, gloss:yeryüzünde} alan 31:34’teki kişinin hangi yerde öleceği sorusunda ({ar:بِأَيِّ أَرْضٍ تَمُوتُ, tr:bi-ayyi arḍin tamūtu, gloss:hangi yerde öleceği}) tekil varış yerine daralır. Aynı “yer” sözcüğünün genel yeryüzü kapsamından tekil ölüm yerine dönüşü, iki ayetin ortak sözcüğünü yinelerken ölçek farkını korur.

## Yazı, kayıt ve konuşulan söz

Bu maddi imgenin sûrede daha önceki bir yankısı, 31:10’da su verilmesiyle çeşitli güzel bitkilerin yetişmesidir ({ar:مَاءً فَأَنبَتْنَا فِيهَا مِن كُلِّ زَوْجٍ كَرِيمٍ, tr:māʾan fa-anbatnā fīhā min kulli zawjin karīm, gloss:su verip orada her güzel türden bitki bitirdik}; 31:10). Bu sahne odaktaki {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} için verimli, yumuşak toprak kullanımını; {ar:شَجَرَةٍ, tr:shajaratin, gloss:ağaç} için canlı gövdeli bitkiyi öne çıkarır. Su ile bitki büyümesi, ağaçları olası yenilenen {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} stoğu gibi ve değişik bitki türlerini farklı malzeme biçimleri gibi düşündürebilir. Dışarıdan girdi ekleyen {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:besler ve uzatır} bu okumada suyun bitkiyi beslemesiyle temas eder. Bu yenilenebilir malzeme zinciri bağlamsal bir çıkarımdır; odak yalnızca ayakta duran ağaçları sayıyor olabilir.

Yazı aracının işlevi 96:4’te kalemle öğretme ({ar:عَلَّمَ بِالْقَلَمِ, tr:ʿallama bi-l-qalami, gloss:kalemle öğretti}) ile, yazı sıvısıysa 18:109’da denizin Rabb’in sözlerine mürekkep olmasıyla açıkça görünür ({ar:مِدَادًا لِكَلِمَاتِ رَبِّي, tr:midādan li-kalimāti rabbī, gloss:Rabbimin sözlerine mürekkep}; 96:4, 18:109). Bu iki yer odaktaki {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} ve {ar:بَحْرُ, tr:baḥru, gloss:deniz} arasındaki yazı ilişkisini aydınlatır: sınırlı izler anlamı taşıyabilir, ama anlamın kendisi olmaz; denizden sözlere uzanan mürekkep bağı başka ayette açıkça kurulur, odak ise bu sıvıyı adlandırmadan {ar:يَمُدُّهُۥ, tr:yamudduhu, gloss:uzatıp besler} fiiliyle ikmali anlatır. Bu nedenle yazı düzeni okunabilir bir benzetmedir, her sözün yazıya geçirilmiş olduğu iddiası değil.

Sûrenin 31:2’deki açılışı {ar:تِلْكَ آيَاتُ الْكِتَابِ الْحَكِيمِ, tr:tilka āyātu l-kitābi l-ḥakīmi, gloss:işte hikmetli kitabın ayetleri} diye görünür kitabı ve onun ayetlerini öne çıkarır (31:2). Bu kitap, odaktaki kalemleri ve anlamlı sözleri ({ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler}; {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler}) birbirine yaklaştırır. Sonlu ve görülebilir bir kitap, tükenmez sözlerin tümünü içine alan envanter değil, onların belirli bir sunumu olarak düşünülebilir. {ar:الْحَكِيمِ, tr:al-ḥakīmi, gloss:hikmetli} bilgelik anlamını korurken, aynı kelime ailesinin sağlam ve kusursuz kılma yönü bu belirli biçimi renklendirir. 31:9’da {ar:الْعَزِيزُ الْحَكِيمُ, tr:al-ʿazīzu l-ḥakīm, gloss:güçlü ve hikmet sahibi} çifti kalıcı bir vaat sonrasında yinelenir (31:9); tekrar odaktaki sonucu hikmetli düzen içinde duyurur, fakat vaadi ilahî kelamla aynı konuya dönüştürmez.

İnsan kalemiyle tutulan kayıt, 6:59’daki kapsayıcı kayıttan başka bir iş görür: düşen yaprak, yerin karanlığındaki tohum, yaş ve kuru olan her şey açık kitapta bilinir ({ar:وَمَا تَسْقُطُ مِن وَرَقَةٍ إِلَّا يَعْلَمُهَا, tr:wa-mā tasquṭu min waraqatin illā yaʿlamuhā, gloss:düşen bir yaprak yoktur ki O bilmesin}; {ar:وَلَا حَبَّةٍ فِي ظُلُمَاتِ الْأَرْضِ, tr:wa-lā ḥabbatin fī ẓulumāti l-arḍ, gloss:yeryüzünün karanlıklarındaki bir tohum bile}; {ar:وَلَا رَطْبٍ وَلَا يَابِسٍ إِلَّا فِي كِتَابٍ مُّبِينٍ, tr:wa-lā raṭbin wa-lā yābisin illā fī kitābin mubīn, gloss:yaş ve kuru her şey açık bir kitaptadır}; 6:59). Bu ayrıntı düzeyinde odaktaki {ar:شَجَرَةٍ, tr:shajaratin, gloss:ağaç} kalem malzemesi, yaprak ve tohum ise kaydedilen şeylerdir; {ar:بَحْرُ, tr:baḥru, gloss:deniz} de bilinen {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} alanının içindeki varlıktır. İnsan kalemi bir yazı aracıdır, kapsayıcı kitap ise her ayrıntının kaydıdır; iki düzen farklı işler görür. Odaktaki {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} ayrıntıların yanında anlamlı birimler olarak durur, kaydın kendisiyle özdeşleşmez.

Bu ayrışmış ayrıntı ölçeğini 31:16, hardal tanesinin ağırlığı kadar küçük bir ölçüyle açar ({ar:مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ, tr:mithqāla ḥabbatin min khardal, gloss:bir hardal tanesinin ağırlığı}; 31:16). Tohum kayanın içinde, göklerde veya yerde gizli olsa Allah onu getirir ({ar:فِي صَخْرَةٍ أَوْ فِي السَّمَاوَاتِ أَوْ فِي الْأَرْضِ, tr:fī ṣakhratin aw fī l-samāwāti aw fī l-arḍ, gloss:bir kayanın ya da göklerin veya yerin içinde}; {ar:يَأْتِ بِهَا اللَّهُ, tr:yaʾti bihā llāhu, gloss:Allah onu getirir}; 31:16); kapanış O’nun ince ayrıntıları bilmesini ve her şeyden haberdar oluşunu söyler ({ar:إِنَّ اللَّهَ لَطِيفٌ خَبِيرٌ, tr:inna llāha laṭīfun khabīr, gloss:Allah incelikleri bilir ve her şeyden haberdardır}; 31:16). Ölçülebilir küçüklük, tükenmeyen {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} sözlerinin biçimsiz bir yığın değil, ayrışmış anlam birimleri olarak düşünülmesine yardım eder. Gizli ayrıntının ortaya çıkarılması bu okumayı güçlendirir; 31:16’nın yalnızca hesap verme bağlamı olarak okunması da mümkündür.

16:96, insanların elindekinin tükenmesini Allah katında olanın kalmasına karşı koyar (16:96). Bu mülkiyet ve kalıcılık karşıtlığı odaktaki {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler}, {ar:بَحْرُ, tr:baḥru, gloss:deniz} ve {ar:نَفِدَتْ, tr:nafidat, gloss:tükenme} biçimlerine daha geniş bir fânilik ölçüsü ekler; iki yerde aynı nesnelerden veya aynı yazı aracından söz edilmez. 18:5’te ağızlarından çıkan tek bir söz hemen yalan diye nitelenir (18:5); bu örnek, insanın tekil sözüyle odaktaki çoğul ve Allah’a nispet edilen {ar:كَلِمَٰتُ ٱللَّهِ, tr:kalimātu llāhi, gloss:Allah’ın sözleri} arasında kaynak ve kapsam farkı kurar. Bu tekil örnek her insan sözünü yanlış saymaz, biçimler arasında da morfolojik özdeşlik ileri sürmez.

Sûrede sözler yalnızca yazı izleri değil, insanlar arasında iş gören konuşmalardır: 31:13’te Lokman’ın oğluna sözü öğüttür; 31:14’te ebeveyne ilişkin yükümlülük aktarılır; 31:17’de iyilik emriyle kötülük yasağı davranışı yönlendirir; 31:19’da sesi alçaltma buyruğu hem eylemi hem söyleyişin sesini ölçer (31:13, 31:14, 31:17, 31:19). Bu nedenle odaktaki {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} anlamlı birimler olarak öğüt, yükümlülük, emir, yasak ve ses ölçüsü içinde de duyulur. 31:17’nin yakındaki bağımsız bir hikmet birimi olması ihtimali açıktır; bu durumda onu önceki öğüdün devamı saymak gerekmez.

Son olarak, 31:20’de Allah hakkında bilgisizce tartışanların sahnesi aynı kelimeleri başka bir dizilişte duyurur (31:20). {ar:شَجَرَةٍ, tr:shajaratin, gloss:ağaç} olağan ağaç anlamını korurken, sözlüksel ailesindeki çekişme ve iç içe geçme yönü tartışmayla etkinleşir. {ar:أَقْلَٰمٌ, tr:aqlāmun, gloss:kalemler} yazı aracının yanında kura için işaretlenmiş çubuk veya ok kullanımlarını çağırabilir; bu keşifsel dal gerçek bir kura çekildiğini söylemez. Tartışma bağlamında {ar:نَفِدَتْ, tr:nafidat, gloss:tükendi} kanıtların tüketilmesine, {ar:كَلِمَٰتُ, tr:kalimātu, gloss:sözler} ise yazı izinin yanına gelen yaralayıcı söze açılır; tükenme tartışmanın özel kullanımı, yara ve ayırt edici iz de söz ailesinin ayrı bir yüzüdür. {ar:عَزِيزٌ, tr:ʿazīzun, gloss:güçlü ve üstün} rakibi alt etme yönünü, {ar:حَكِيمٌ, tr:ḥakīmun, gloss:bilge ve hüküm veren} anlaşmazlığı bağlayıcı kararla çözme ihtimalini verir. Böylece insan söz düellosu sonlu kanıt ve karşılaşmayla bir hükme kapanır gibi okunabilir; bu ikincil okuma gerçek mahkeme ya da yara anlatmaz, odaktaki ağaç-kalem-deniz yazı düzenini de yerinde bırakır.

</source_prose>
