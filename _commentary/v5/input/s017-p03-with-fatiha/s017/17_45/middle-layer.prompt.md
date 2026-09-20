# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:45**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.middle.claims.json`

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
- Refer to source paragraphs as `17:45 ¶N`.

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

`(17:45 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:45",
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
        "citation": "(17:45 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_45/17_45.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_45/17_45.middle.claims.json \
  --ayah-ref 17:45
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_45/17_45.prose.editorial.tr.md`

<source_prose>
## Tilavetin şartı ve aralığın kurulması

Ayet, sen {ar:الْقُرْآنَ, tr:al-Qur'āna, gloss:Kur'an'ı} okuduğunda Allah’ın okuyanla âhirete inanmayanlar arasına gizli bir perde koyduğunu bildirir. Başındaki {ar:وَ, tr:wa, gloss:ve} söylem çizgisini sürdürürken hemen ardından gelen {ar:إِذَا, tr:idhā, gloss:olduğunda} bu cümlede kendi şart-zaman alanını açar. İkisi sesçe tek bir girişe yaklaşarak açılışı akıtır; wa'nın bağlayıcı etkisi idhā'nın sınırını silmez, ikinci bir koşul da eklemez. Bu cümlenin koşul-cevap bağı, 17:44'teki yaratılmışların tesbihi sahnesinden türetilmez. İdhā, {ar:قَرَأْتَ, tr:qara'ta, gloss:tilavet ettiğinde} eylemini yinelenebilir bir koşul olarak alır ve onu {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik} cevabına bağlar; bu koşul her tilavete yayılan genel bir hüküm kurmaz.

Koşuldaki ikinci tekil {ar:قَرَأْتَ, tr:qara'ta, gloss:tilavet ettiğinde} hitap edilen muhatabı okuma eyleminin faili yapar; bu biçim hitabı başka bir zamana ya da daha geniş bir kitleye taşımaz. Belirli mansub {ar:الْقُرْآنَ, tr:al-Qur'āna, gloss:Kur'an'ı}, fiilin doğrudan nesnesi olarak bilinen Kur'an'ı gösterir; böylece eylem genel bir metin anması değil, belirli bir tilavettir. Qara'ta, I. bâbın mâzî biçimiyle olağan olarak okumak ve tilavet etmek demektir. Aynı kökün fiil ile nesnede yinelenmesi, okuma eylemini ses içinde bir araya geliş ya da toplanma yankısıyla buluşturabilir. Bu yankı Kur'an adının tartışmalı türetimini çözmez ve tilaveti ayrı bir toplama işlemine dönüştürmez. İki biçimdeki hemze akışta küçük bir kesinti verir; bu ses teması tilavetin nesnesini değiştirmez ve kıraat varyantı ileri sürmez.

Koşul bölümündeki ikinci tekil {ar:قَرَأْتَ, tr:qara'ta, gloss:tilavet ettiğinde} muhatabı eylemin faili yapar; karşılıktaki birinci çoğul {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik} geldiğinde dilbilgisel fail değişir ve karşılığı kuran ayrı bir ilahî eylem belirir. Böylece ja'alna bağımsız bir tasvir değil, koşul gerçekleştiğinde yapılan iştir. İki {ar:بَيْنَكَ وَبَيْنَ, tr:baynaka wa-bayna, gloss:seninle ... arasında} yapısının açtığı konuma {ar:حِجَابًا, tr:ḥijāban, gloss:perde} yerleştirilmesi, fiilin burada bir şeyi belirli konuma ya da duruma getirme anlamını öne çıkarır; bu yerleştirme okuması yoktan yaratma iddiası gerektirmez. Özne değişimi bu koşul-cevap cümlesinin içindedir, daha geniş bir söylem geçişi değildir.

Kurulan yer, iki kez yinelenen {ar:بَيْنَكَ وَبَيْنَ, tr:baynaka wa-bayna, gloss:seninle ... arasında} yapısıyla açılır. İlk kutuptaki -ka muhatabı aralığın bir tarafı olarak gösterir ama kendi başına fiziksel bir konum belirtmez; ikinci {ar:بَيْنَ, tr:bayna, gloss:arasında} başıysa öteki tarafı henüz açık bırakır. {ar:جَعَلْنَا, tr:ja'alna, gloss:araya yerleştirdik} fiilinin araya koyduğu {ar:حِجَابًا, tr:ḥijāban, gloss:perde}, iki kutup arasındaki yeri doldurup ayırıcı etki verir. Bayn “arada olma”yı hem mekânsal yer hem de iki tarafı aynı ilişki içinde tutan çerçeve olarak kurar; ayırma işini bayn değil, perde yapar. Böylece taraflar ayrılır ama ilişkisiz kalmaz; aralık ölçülebilir uzaklık vermez ve yakınlık ya da uzlaşma vaat etmez. İki bayn başı arasındaki kısa {ar:وَ, tr:wa, gloss:ve} ritmi sesleri bağlayıp kutupları ayrı tutar; ikinci grubu ilk kutbun niteliğine çevirmeden iki parçayı eşgüdümler. Bu kısa ses eşgüdümü wa'ya ayrı bir sözlük anlamı yüklemez ve yeni bir katılımcı eklemez.

{ar:الَّذِينَ, tr:alladhīna, gloss:kimseler ki} bağıl ifadesi ve ardından gelen cümle, ikinci {ar:بَيْنَ, tr:bayna, gloss:arasında} başının açtığı yeri birlikte tamamlar; öteki kutup böylece tutum bildiren bir tümceyle kurulur. {ar:لَا يُؤْمِنُونَ, tr:lā yuʾminūna, gloss:inanmayanlar} topluluğu nesep ya da miras alınmış kabile etiketiyle değil, inanç tutumuyla niteler. Bağıl tümce bu kutup için inanç tutumunu seçer; grubun başka kimlikleri ve üyelerinin başka amaçlardaki tanımları açık kalır.

Bağıl cümlede ayrı {ar:لَا, tr:lā, gloss:olumsuzluk}, geniş zaman {ar:يُؤْمِنُونَ, tr:yuʾminūna, gloss:inanırlar} fiilinden önce gelir ve olumsuzluğu açıkça kurar; geniş zaman da bunu tek bir ret anı değil, süregelen bir tutum olarak duyurur. Sözcük sırası kendi başına bir saik vermez; bu biçim grubun bütün geçmişini ya da her kişinin iç dünyasını açıklamaz. Fiil {ar:بِالْآخِرَةِ, tr:bi-l-ākhirati, gloss:âhirete} öbeğiyle tamamlanır: bi edatı inanmamanın yöneldiği nesneyi, âhireti, açıkça belirler; bu yerel hedef bütün olası inanç nesnelerinin reddine yayılmaz.

{ar:يُؤْمِنُونَ, tr:yuʾminūna, gloss:inanırlar} burada Arapçanın IV. bâbındaki muzari biçimiyle inanmak anlamını taşır. Aynı kökün güvenilirlik ve korkudan emin olma alanı, araya konan {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ile yan yana geldiğinde olağan inanma anlamının yanında âhirete yönelik güvenin de geri çekilmesi yankısını duyurabilir. Fiilin olağan inanma anlamı cümlenin odağında kalır; bu bağlamdaki güven yankısı nüans olarak işler, fiziksel korunma ya da kurtuluştan dışlanma hükmü kurmaz.

Bu inanç hedefinin adı {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:âhiret}: belirli dişil isim dünyadan sonraki varoluş düzenini, belirsiz bir sonraki olayı değil, gösterir. “Sonra gelen, öteki” yankısı bu hedefe son ufkun ağırlığını ekler; sözcük erteleme eylemine dönüşmez. {ar:بِالْآخِرَةِ, tr:bi-l-ākhirati, gloss:âhirete} ile tamamlanan kimlik tümcesinin son isim öğesi, hemen arkasındaki {ar:حِجَابًا, tr:ḥijāban, gloss:perde} önünde durur. Bu bitişiklik, reddedilen ufkun bugünkü {ar:بَيْنَكَ وَبَيْنَ, tr:baynaka wa-bayna, gloss:iki taraf arasındaki aralık} içinde duyulmasına izin veren bir menteşe kurar; sözdizimsel yan yanalık perdenin nedenini açıklamaz, aralık da ölçülebilir uzaklık belirtmez.

İki kutup kurulduktan sonra gelen belirtisiz mansub {ar:حِجَابًا, tr:ḥijāban, gloss:perde}, önce aradaki boşluğu hissettirir, ardından bu aralığa perde adını verir. Belirtisizlik engelin türünü açık bırakır; maddesi ya da belirli bir fiziksel biçimi verilmez. Sonundaki {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli}, {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ile biçim uyumu kuran belirtisiz edilgen sıfat-fiildir. Bu sonuç durumu gizliliği başka bir kişiye değil perdenin kendisine yükler; sonda yer alması da gizli hâli adın ardından cümle kapanışına taşır. Bu niteleme gizliliğin sıklığını ya da perdeyi kimin ve hangi saikle örttüğünü belirtmez.

{ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} sözcüğündeki örtme ve gizleme alanını hemen önceki {ar:حِجَابًا, tr:ḥijāban, gloss:perde} imgesi açar. Tilavet koşulu gerçekleştiğinde {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik} cevabı sınırı eylem olarak devreye sokar; {ar:قَرَأْتَ, tr:qara'ta, gloss:tilavet ettiğinde} tilaveti ve {ar:بَيْنَكَ وَبَيْنَ, tr:baynaka wa-bayna, gloss:iki taraf arasındaki aralık} ilişkisiyle birlikte düşünüldüğünde perdenin olağan bölme anlamı, okunan hitabın karşı tarafa erişimini etkileyen görünmez sınıra genişler. Böylece perde hem görünmeyen hem erişimi örten olarak duyulur. Bu bağlantı şartlı tilavette erişimi etkileyen sınırla ilgilidir: her tilavette herkesin bütünüyle engellendiği ya da fiziksel, toplumsal veya kurtuluşa ilişkin dışlanma hükmü çıkarıldığı anlamına gelmez; mekanizma, maddi biçim, ölçülebilir uzaklık ve perdenin ötesi açık bırakılır.

Bu iki öğenin yakın sesleri, {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ile {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} nitelemesini kulakta tek bir kapanışta bağlar. Ahenk bu ayırıcıyı ve onun örtülülüğünü birlikte duyurur; katkısı bu sözcüklerin yerel ses ilişkisidir.

## İşitme ve alımlama

Görünmeyen sınır, tilavetin nasıl karşılandığı sorusunu da açar. Önceki ayette (17:41) {ar:ٱلْقُرْءَانِ, tr:al-Qur'āni, gloss:Kur'an} farklı biçimlerde sunulur ve bu sunuş hatırlamaya yönelir: {ar:صَرَّفْنَا, tr:ṣarrafnā, gloss:çeşitli biçimlerde sunduk}, {ar:لِيَذَّكَّرُوا, tr:li-yadhdhakkarū, gloss:hatırlasınlar diye}. Ardından aynı sunuşun uzaklaşmayı artırdığı bildirilir: {ar:وَمَا يَزِيدُهُمْ إِلَّا نُفُورًا, tr:wa-mā yazīduhum illā nufūran, gloss:onların uzaklaşmasını artırır}. Bu hatırlatma amacı ile 17:45'teki {ar:قَرَأْتَ, tr:qara'ta, gloss:okuduğunda} tilaveti ve {ar:حِجَابًا, tr:ḥijāban, gloss:perde} yan yana gelince uzaklaşma ile perde aynı okuma alanında belirir; hatırlatma amacı taşıyan sunuşun dirençle karşılaşabildiği bir alımlama döngüsü duyulur. Bu bağlantı uzaklaşmayı perdenin nedeni ya da kalktığının işareti yapmaz ve bu karşılığı bütün dinleyicilere yaymaz.

Hemen sonraki ayette (17:46) {ar:جَعَلْنَا, tr:ja'alna, gloss:yerleştirdik} fiili yinelenir; kalpler üzerine {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler}, kulaklara {ar:وَقْرًا, tr:waqran, gloss:ağırlık} konur. Kavrayamama ve Kur'an'da Rabbin adı anıldığında yüz çevirme de bu sahneye katılır. 17:45'te iki kutup arasındaki dış aralıkta duran {ar:حِجَابًا, tr:ḥijāban, gloss:perde}, kalbin kavrayışı ve kulağın işitmesine uzanan bir erişim sorusu doğurur. Kalp örtüsü kavrayışı, kulak ağırlığı işitmeyi, aradaki perdeyse dış aralığı duyurur; bu ayrı imgeler arasındaki yankı erişim sınırını iç alımlamaya doğru genişletir, ama imgeleri tek bir bedensel duvar ya da mutlak sağırlıkta birleştirmez.

Kavrayış ile işitmenin ayrılığı, 17:44, 17:46 ve 17:47 arasındaki akışta belirginleşir. 17:44'te yaratılmışların tesbihi için {ar:لَا تَفْقَهُونَ, tr:lā tafqahūna, gloss:kavrayamıyorsunuz} denmesi kozmik bir kavrayış sınırıdır; bu ayrı sahne odaktaki topluluğun olayı değildir. 17:46'daki örtü ve ağırlığın ardından 17:47'de {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} fiilinin yinelenmesi dinlemenin sürdüğünü gösterir. Bu akışta 17:45'in {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} perdesi, sesin ulaşması ile anlamın kavranmasının farklı aşamalar olabileceği bir sınır gibi okunabilir: 17:47 dinlemenin sürdüğünü gösterir ama kavrayışı kanıtlamaz.

17:45'teki {ar:قَرَأْتَ, tr:qara'ta, gloss:okuduğunda} tilavetinin ardından 17:47'de {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} diye anılanlar elçiyi {ar:مَسْحُورًا, tr:masḥūran, gloss:büyülenmiş} diye adlandırır; 17:48'de ona {ar:ضَرَبُوا۟ لَكَ ٱلْأَمْثَالَ, tr:ḍarabū laka al-amthāla, gloss:sana benzetmeler kurdular} diye benzetmeler yöneltirler. Bu düşmanca etiket ve karşılaştırmalar mesajı onu taşıyan kişi üzerinden yeniden çerçeveler. Ardından 17:48'de yollarını şaşırıp yol bulamama anılır: {ar:فَضَلُوا۟ فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-ḍallū fa-lā yastaṭīʿūna sabīlan, gloss:yollarını şaşırıp bir yol bulamazlar}. Bu işaretler aynı direnç çevresinde yan yana gelir, ancak etiketler yol kaybının nedeni değildir ve bu bağlantı bütün dinleyenlere yayılmaz. Böylece ses ulaştıktan sonra taşıyıcı üzerinden işleyen yeniden çerçeveleme, {ar:حِجَابًا, tr:ḥijāban, gloss:perde} imgesine ikinci bir süzgeç ekler.

17:48'deki {ar:سَبِيلًا, tr:sabīlan, gloss:yol} bulamama, Fatiha'nın dosdoğru yola yönelme isteğiyle (1:6) karşılaştırıldığında iki ayrı kök ve yönü yan yana getirir: sabīl yol bulamamayı, {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} ise doğru yola iletilme talebini taşır. Bu karşılaştırma iki ayeti aynı topluluk ya da olay saymaz; 17:45'teki Kur'an'ı da açıkça hidayet aracı diye adlandırmaz. Bu sınırlar içinde sabīl'in bulamama yönü ile ṣirāt'a yönelme isteği birbirini aydınlatan ayrı hareketler olarak kalır.

Bu yol karşıtlığının yanında Kur'an tilavetine verilen karşılıkların çeşitliliği görünür. 7:204'te {ar:فَاسْتَمِعُوا لَهُ وَأَنْصِتُوا, tr:fastamiʿū lahu wa-anṣitū, gloss:onu dinleyin ve sessiz olun} buyruğu merhamet umuduna bağlanır. 46:29'da Kur'an'ı işiten bir topluluk birbirine sessizce dinlemeyi hatırlatır, ardından kendi halkını uyarmak üzere döner. Bu iki sahne 17:45'teki {ar:قَرَأْتَ, tr:qara'ta, gloss:okuduğunda} koşuluna temas ederek Kur'an'ı farklı karşılıklara açık ortak bir hitap olarak duyurur; odak ayet ise dikkatini âhireti reddettiği belirtilen gruba yöneltir. Karşılaştırma bu sahnelerdeki dinleyicileri 17:45'in muhataplarıyla özdeşleştirmez ya da perdenin aşıldığını göstermez; farklı dinleme karşılıkları, odak perdenin belirli hedefi korunarak birlikte görünür olur.

Okumayı izleyen ayrı bir yanıt, korunma tınısını açar. 16:98'de {ar:فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ, tr:fa-idhā qara'ta al-Qur'āna, gloss:Kur'an'ı okuduğunda} koşulundan sonra Allah'a şeytandan sığınma buyruğu gelir. 17:45'te aynı tilavet koşulunun cevabı {ar:جَعَلْنَا حِجَابًا, tr:ja'alna ḥijāban, gloss:bir perde yerleştirdik}, 16:98'deyse sığınmadır. Bu benzerlik, 16:98'deki açık sığınma buyruğunu 17:45'in perdesine eşdeğer ya da onun açıklaması yapmaz; odak ayet de perdenin niçin konduğunu söylemez. Bu ayrım içinde koşul-cevapların yan yanalığı, tilavete ayrılığın yanında ikincil bir korunma tınısı ekler.

İşitmeden görünen işarete geçildiğinde, kabulün başka bir sınırı belirir. 17:59'da önceki kuşakların gönderilen ayetleri yalanladığı söylenir: {ar:بِٱلْءَايَٰتِ, tr:bi-l-āyāti, gloss:ayetlerle ya da işaretlerle}, {ar:كَذَّبَ بِهَا ٱلْأَوَّلُونَ, tr:kadhdhaba bihā al-awwalūna, gloss:öncekiler onları yalanladı}. Ardından Semûd'a verilen, gözle görülen dişi deve {ar:ٱلنَّاقَةَ مُبْصِرَةً, tr:al-nāqata mubṣiratan, gloss:gözle görülen dişi deve} ve ona karşı işlenen haksızlık {ar:فَظَلَمُوا۟ بِهَا, tr:fa-ẓalamū bihā, gloss:ona haksızlık ettiler} gelir. 17:60'ta görülen rüya {ar:ٱلرُّءْيَا, tr:al-ruʾyā, gloss:görülen rüya} bir {ar:فِتْنَةً, tr:fitnatan, gloss:sınama} sayılır; uyarı da {ar:فَمَا يَزِيدُهُمْ إِلَّا طُغْيَانًا, tr:fa-mā yazīduhum illā ṭughyānan, gloss:azgınlıklarını artırır} diye artan azgınlıkla karşılanır. Semûd sahnesi görünür bir işaret karşısındaki haksızlığı, 17:60'taki rüya ve uyarı ise sınama ile artan azgınlığı gösterir. Bu ayrı sahneler odak grubun olayı sayılmaz ve tepkileri ona genellenmez; 17:45'in {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ve {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} imgeleriyle yan yana gelişleri, alımlama sınırını işitmeden görmeye doğru genişletir.

## Aralık ve temas

Görünür işaretlerin ayrı sahnelerinden ilişkiyi sözün biçimlendirdiği 17:53'e geçince, iki kutup arasındaki “arasında” bağı başka bir yön kazanır. 17:45'te {ar:قَرَأْتَ, tr:qara'ta, gloss:okuduğunda} sırasında konan {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ve {ar:بَيْنَكَ, tr:baynaka, gloss:seninle ... arasında} ayırıcı aralığı kurar; 17:53'te kullardan {ar:يَقُولُوا۟ ٱلَّتِى هِىَ أَحْسَنُ, tr:yaqūlū allatī hiya aḥsanu, gloss:en güzel olanı söylesinler} diye istenir, çünkü şeytan {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaghu baynahum, gloss:aralarına fitne sokar}. 17:53'teki bu bağımsız konuşma etiği, odak ayetteki ayırıcı aralığın yanında kırılgan ilişkiyi koruyabilecek olası bir eşik sunar. Bu iki sahne arasındaki olası yankı perdenin amacını açıklamaz ya da konuşanların aynı olduğunu göstermez. Ayetin sonundaki {ar:عَدُوًّا مُّبِينًا, tr:ʿaduwwan mubīnan, gloss:açık bir düşman} yalnızca düşmanı niteler, ikinci bir aralık kurmaz. Böylece “aralarında” sözü ayırıcı aralığın yanında korunmaya muhtaç bağı da ihtimal olarak duyurur.

Perde bu kez karşı taraftan, konuşanların kendi sözleriyle belirir. 41:5'te “{ar:بَيْنَنَا وَبَيْنَكَ حِجَابٌ, tr:baynanā wa-baynaka ḥijābun, gloss:aramızda ve seninle aramızda bir perde var}” derler. 17:45'te Allah'ın araya koyduğu {ar:حِجَابًا, tr:ḥijāban, gloss:perde} sözcüğünü burada konuşanlar kendi taraflarından adlandırır; iki kutuplu perde imgesi böylece karşı yönden duyulur, fakat sahnelerin toplulukları özdeş değildir. 41:5'te konuşanlar ayrıca kalplerinin örtülü, kulaklarının ağır olduğunu söyler; 6:25'te Kur'an'ı dinleyenlerin kalplerindeki örtüler anlamayı engeller, kulak ağırlığı da dinleme sahnesine eşlik eder. 17:45'teki {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} ile bu içsel örtünme ve ağırlık imgeleri aynı biçim değil, imge düzeyinde temas kurar. Bu temas, odak perdenin sınırını kalp ve kulak imgelerine bağlayarak dış aralıktan alımlama ilişkisine uzatır.

41:26'da Kur'an'ı dinlememek ve dinleme sırasında gürültü çıkarmak öğütlenir; alımı bozan eylem burada kasıtlıdır. 8:23 ise işitme sağlansa bile yüz çevrilebileceğini bildirir; sesin ulaşması yönelişi tek başına belirlemez. 41:5 ve 6:25'teki kalp örtüsü kavrayışa, kulak ağırlığı işitmeye dönük sınırı gösterirken, 41:26'daki gürültü dinlemeyi kasıtla bozar ve 8:23 işitmeye rağmen yüz çevirmeyi ekler. Bu sahneler aynı dinleyicileri göstermez; ilahî yerleştirme ile dinleyici eğilimi ya da kasıtlı engelleme arasındaki neden açık kalır. Bu ayrımlar 17:45'in {ar:حِجَابًا, tr:ḥijāban, gloss:perde} imgesini dış aralıktan işitme ve kavrayışa uzanan bir alım sınırı olarak genişletir.

Perde imgesi, (7:46), (19:17), (33:53) ve (42:51) ayetlerinde farklı temas biçimleri içinde görünür. 7:46'da {ar:حِجَابٌ, tr:ḥijābun, gloss:perde} iki bölge arasında dururken yüksek yerlerdeki kişiler Cennet halkını işaretlerinden tanır ve onlara seslenir; perde ayrılık içinde hitabı çerçeveler. 19:17'de Maryam ötekilerden ayrı bir {ar:حِجَابًا, tr:ḥijāban, gloss:perde} edinir, ardından bir ruh ona insan görünümünde belirir; sınırın ardından görünüş gerçekleşir. 33:53'te {ar:حِجَابٍ, tr:ḥijābin, gloss:perde} ardından konuşma istemek kalpler için daha temiz bir düzen sayılır; 42:51'de perde ardından konuşma ilahî hitap yollarından biridir. İlk iki sahnede perde çevresinde hitap ya da görünüş sürer; son ikisinde perde istek ve ilahî hitabın kuruluşunu düzenler. Bu karşılaştırma aynı kişileri ya da odak tarafların perdeyi aştığını ileri sürmez; odak ayetin {ar:حِجَابًا, tr:ḥijāban, gloss:perde} ile kurduğu ayrılığı korurken, başka sahnelerde perdenin iletişimi de çerçeveleyebildiğini gösterir.

## Âhiret ufku

17:45'in muhatapları {ar:ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:alladhīna lā yuʾminūna bi-l-ākhirati, gloss:âhirete inanmayanlar} diye adlandırılır; bu şimdiki ret, yakın ayetlerde bir zaman ufku kazanır. 17:49'da kemik ve ufalanmış kalıntı olduktan sonra yeniden diriltilip diriltilmeyecekleri sorulur: {ar:أَءِنَّا لَمَبْعُوثُونَ, tr:a-innā la-mabʿūthūna, gloss:gerçekten yeniden mi diriltileceğiz?}. 17:51'de “bizi kim geri döndürecek?” sorusuna {ar:يُعِيدُنَا, tr:yuʿīdunā, gloss:bizi geri döndürecek} ve ilk kez yaratanı anan {ar:فَطَرَكُمْ أَوَّلَ مَرَّةٍ, tr:faṭarakum awwala marratin, gloss:sizi ilk kez yaratmış olan} cevabı gelir. 17:52'de çağrı ve karşılığı {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır}, {ar:فَتَسْتَجِيبُونَ, tr:fatastajībūna, gloss:karşılık verirsiniz} diye sıralanır. Bu dizi tövbe ya da yeni iman, perdenin kalkması veya sürenin uzunluğu hakkında hüküm vermez; 17:45'teki şimdiki reddi gelecekteki diriliş, geri dönüş, çağrı ve cevap ufkuna yerleştirir.

Âhirete inanmayanlar adı iki ayrı tepki sahnesinde yinelenir (39:45, 27:4): {ar:ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ, tr:alladhīna lā yuʾminūna bi-l-ākhirati, gloss:âhirete inanmayanlar}. 39:45'te Allah tek başına anıldığında bu nitelemeyle anılanların kalpleri tiksintiyle daralır; 27:4'te amelleri kendilerine süslü gösterilir ve şaşkınlık içinde kalırlar. Tekrarlanan {ar:ٱلْءَاخِرَةِ, tr:al-ākhirati, gloss:âhiret} göndergesi anlamını korur: 17:45'te inanç tanımı olarak kurulan grup adı, 39:45'te ilahî anışa tepki ve 27:4'te amellerin süslü gösterilmesiyle şaşkınlıkta kalma sahnelerinde ayrı ayrı yankılanır. Bu paralellik aynı kişileri belirlemez ve tepkileri 17:45'teki tilavete bağlamaz; iki ayrı karşılık sahnesi odak ayetin tanımını daha geniş bir yönelim içinde yankılandırır.

83:15'te bir topluluk o gün Rablerinden perdelenmiş olarak anılır: {ar:لَمَحْجُوبُونَ, tr:la-maḥjūbūna, gloss:perdelenmiş olanlar}. Bu, 17:45'teki {ar:حِجَابًا, tr:ḥijāban, gloss:perde} adından farklı, aynı kök ailesine bağlı edilgen çoğul sıfattır; böylece kişiler arasındaki aralığın yanına Rab'den perdelenmeye dönük uhrevî ayrılık gelir. İki ayet aynı topluluğu göstermez ve biri diğerinin nedeni olarak sunulmaz; kök yankısı biçim farkını koruyarak kişilerarası uzaklığı son uhrevî ufka taşır.

Bu örtülülük, tilavetteki ses üzerinden 17:58'deki yazılılık sözüne yaklaşır. 17:45'in {ar:مَّسْتُورًا, tr:mastūran, gloss:örtülü ya da gizli} nitelemesi, Kitap içinde satırlara geçirilmiş olmayı bildiren {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:Kitap} ve {ar:مَسْطُورًا, tr:masṭūran, gloss:satırlara yazılmış} ile işitsel bir yankı kurar (17:58). İlki örtülülüğü, ikincisi yazılı oluşu bildirir; kökleri s-t-r ile s-ṭ-r olarak ayrılır ve ayırt edici ses t ile kalın ṭ arasındadır. Bu ses yakınlığı iki biçim arasında çağrışım kurar; kök ayrımı eşanlamlılık ya da perdenin Kitap'ta yazılı olduğu iddiası vermez. Böylece tilavetteki örtülülük, satıra geçirilmişlik sözüne dokunur ve iki ayrı imge kulakta belirginleşir.

</source_prose>
