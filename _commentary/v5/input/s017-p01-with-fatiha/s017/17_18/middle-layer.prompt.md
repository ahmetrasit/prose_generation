# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:18**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.middle.claims.json`

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
- Refer to source paragraphs as `17:18 ¶N`.

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

`(17:18 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:18",
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
        "citation": "(17:18 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_18/17_18.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_18/17_18.middle.claims.json \
  --ayah-ref 17:18
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_18/17_18.prose.editorial.tr.md`

<source_prose>
## Koşulun Ufku

17:18, {ar:مَّن, tr:man, gloss:her kim} diyerek kimliği açıklanmayan tekil bir insanın koşulunu açar. Bu kişi {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan}ı isterse, Allah onun için bu hayat içinde dilediği şeyi {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık} fiiliyle erkene alır; {ar:لِمَن, tr:liman, gloss:kime} kaydı tahsisin yöneldiği alıcıyı da ilahî dilemeye bağlar. Ardından {ar:ثُمَّ, tr:thumma, gloss:sonra} aynı kişiye döner: {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir duruma getirdik} fiilinin nesnesi özel ad olan {ar:جَهَنَّمَ, tr:Jahannam, gloss:cehennem}dır; kişi orada {ar:يَصْلَىٰهَا, tr:yaṣlāhā, gloss:orada yanar}, {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ve {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} halde bulunur. İlk yönelişten bu sonuca kadar özne aynı adsız kişidir; ayet onun tarihsel kimliğini vermez.

Koşuldaki {ar:كَانَ, tr:kāna, gloss:olmak} ile ardından gelen {ar:يُرِيدُ, tr:yurīdu, gloss:ister}, isteği tek bir anlık heves değil, sürmekte olan ya da yerleşmiş bir yöneliş olarak kurar. Belirli biçimdeki {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan}, dişil isimleşmiş etken ortacıyla hemen erişilen dünya hayatını ve yakın vakti adlandırır; burada zaman ufku öne çıkar, soyut bir hız niteliği değil. İfade istenen ufku belirler; bedensel arayış ya da yolculuk imgesi açmaz ve tek başına âhiret karşıtlığı kurmaz. Kāna yönelişin sürmesini taşır; kişinin mekânda yerleşikliği, güvencesi ya da teslimiyeti hakkında hüküm vermez.

İnsan öznesindeki {ar:يُرِيدُ, tr:yurīdu, gloss:ister} ile ilahî birinci çoğul öznenin {ar:نُرِيدُ, tr:nurīdu, gloss:dileriz} fiili aynı kök ve Form IV yapısındadır; gramatik özne tekil insandan ilahî sese geçer. Bu biçimsel dönüş insan yönelişi ile ilahî tahsisi birbirine yankılatır; failleri ve eylemleri birleştirmez. Kökün eylemi yineleyerek yapma anlamındaki ayrı kullanımı, tekrar eden sesle burada yalnız biçimsel bir yankı kurar; odaktaki fiil telaşsız tercihi de kapsayan dileme olarak kalır. Bu yankı gidip gelme, arayış ya da kararsızlık sahnesi çizmez; kestirme yol bağı ilerideki bağımsız yolculuk temasından gelir.

Yakın zamanı adlandıran isim ile cevapta gelen {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık} arasında aynı kökün isimden Form II fiile uzanan bağı vardır. {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan} yakın vakti gösterirken ʿajjalnā seçilmiş bir şeyi ya da payı bekletmeden öne alır; böylece isimdeki zaman niteliği ilahî eylemde yeniden duyulur. Bu yerel bağ hızın zaman ekseninde işlediğini gösterir; mesafeyi azaltan yol okuması ayrı bir yolculuk temasına dayanır. Koşuldan sonra gelen ilahî geçmiş zaman fiili de odağı insanın yönelişinden cevabın tahsisine çevirir.

## İçerik ve Alıcı

İlk {ar:لَهُۥ, tr:lahu, gloss:onun için} açılıştaki adsız kişiye döner ve payın alıcısını gösterir; seçim yetkisini değil. {ar:فِيهَا, tr:fīhā, gloss:onun içinde} zamiri {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan}a bağlanarak hızlandırmanın gerçekleştiği zaman alanını belirler. Ardından gelen {ar:مَا, tr:mā, gloss:ne ise} içerik yuvasını açık bırakır; birinci çoğul öznenin süreklilik taşıyan {ar:نَشَاءُ, tr:nashāʾu, gloss:dileriz} biçimi bu yuvayı ilahî iradeye bağlar, belirli bir dünyevî ödül adı vermeden.

Alıcı yuvası {ar:لِمَن, tr:liman, gloss:kime} ve onu izleyen {ar:نُرِيدُ, tr:nurīdu, gloss:dileriz} ile seçilir; böylece “ne” ile “kime” ayrı işlevler görür. Liman cümlede hızlandırma eylemine de açık bırakılan içeriğe de bağlanabilir; her iki kuruluşta da nurīdu alıcıyı ilahî dilemeye bırakır. Liman içindeki man sesi açılıştaki bağımsız koşul öznesi {ar:مَّن, tr:man, gloss:her kim} ile farklı bir dilbilgisel görev taşır. Seçilen kişinin kimliği açıklanmaz. Aktarılan tekil özne varyantı nashāʾu'nun ilahî faili sunuşunu değiştirebilir; tam yüzeyi verilmediği için buradaki açıklama görünür birinci çoğul biçime dayanır ve “ne” ile “kime” ayrımını korur.

Bu açık payın değerini, 17:11'de insanın şerri hayrı ister gibi istemesi ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} diye nitelenmesi başka bir yönden aydınlatır. Odaktaki yurīdu, al-ʿājilah ve ʿajjalnā ile birlikte okunduğunda bu uyarı hızlı tahsisin yarar kanıtı sayılamayacağını gösterir. Sınır, aceleyi yararla özdeşleştirmemektir: kısa vadeli isteklerin tümü kötü sayılmaz ve isteyen kişiye iyiyi bilerek zararla karıştırma niyeti yüklenmez. (17:11)

İsteğin karşılığının tahsisi 42:20 ve 11:15'te iki ayrı düzenle görünür. 42:20'de âhiret hasadını isteyenin hasadı artırılır; dünya hasadını isteyene ise ondan bir pay verilir ve âhirette pay bırakılmaz. 11:15'te dünya hayatını ve süsünü isteyenlere işlerinin karşılığının dünya içinde eksiksiz verilmesi anlatılır. İlki hasada göre ayrılan payı, ikincisi dünyevî karşılığın eksiksizliğini öne çıkarır; böylece iki ayrı tahsis biçimi görünür. 17:30'da rızkın dilediğine genişletilip dilediğine kısılması miktar boyutunu ekler. Bu ayetler ʿajjalnā ile birlikte, miktar, zaman ve alıcının ayrı eksenlerini belirginleştirir; yurīdu da olağan dileme anlamını korur. (42:20, 11:15, 17:30)

## Aynı Alıcıdan Sonuca

İlk {ar:لَهُۥ, tr:lahu, gloss:onun için} hızlandırılan payın alıcısını gösterirken, daha sonra gelen {ar:لَهُ, tr:lahu, gloss:onun için} aynı kişiyi Cehennem atamasına bağlar. Bu tekrar, ilk pay ile son hükmü aynı alıcı etrafında buluşturarak ironik bir benefaktif yankı kurar. 17:7'de iyilik ya da kötülüğün kişinin kendisine dönmesi bu özneye geri dönüşü destekler; odaktaki datif dağıtıcı okunduğunda da alıcı aynı kalır. Bu yankı ilk tahsisin Cehennem'e sebep olduğunu kurmaz. 42:20'deki hasat paylaşımı ayrı bir tahsis paralelidir; oradaki dünya ve âhiret hasadını isteyenler farklı özneler olduğundan, bu karşılaştırma odaktaki kişinin kimliğini belirlemez. (17:7, 42:20)

{ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık} ile {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir duruma getirdik} yakın sesleri ve birinci çoğul ilahî özneleriyle birbirine bağlanır, ama ayrı işler görür: ilki payı erkene alır, ikincisi aynı alıcıya belirlenmiş bir durum atar. {ar:ثُمَّ, tr:thumma, gloss:sonra} bu işleri sıraya koyar ve aradaki sürenin uzunluğunu açık bırakır. {ar:كَانَ, tr:kāna, gloss:olmak} ile {ar:يُرِيدُ, tr:yurīdu, gloss:ister} içinde sürmüş yöneliş, aynı kişinin aldığı sonraki durumla böylece karşı karşıya gelir. Thumma'nın açtığı birim jaʿalnā ile başlayıp Cehennem ataması, yanma, kınanma ve kovulmayı birlikte kapsar. Belirli nesne {ar:جَهَنَّمَ, tr:Jahannam, gloss:cehennem} olduğundan jaʿalnā burada atamayı bildirir; Cehennem arka plan değil, atanan sonuçtur ve fiil yaratma eylemini anlatmaz.

Hesap imgeleri kişisel hükmü elle tutulur kılar: 17:13'te herkesin payı boynuna bağlanır ve kitap önüne açılır; 17:14'te kişiye kitabını okuması söylenir; 17:14 ve 17:15'te kişinin kendi hesabını görmeye kendisinin yeteceği ve hiçbir yük taşıyanın başkasının yükünü üstlenmeyeceği bildirilir. Boyna bağlanan kayıt, okunan kitap ve devredilmeyen sorumluluk, odaktaki {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} ile {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} sonunu kişisel, dayanağı görülebilir bir hüküm gibi duyurur. Bu temas açıklayıcıdır: odaktaki adsız kişi kitap taşıyıcısı diye açıkça tanımlanmaz ve kınamanın gerekçesi bu kayıtla sınırlı tutulmaz. (17:13, 17:14, 17:15)

## Ateşte ve Yakınlığın Dışında

Atamanın ilk somut açılımı adın sesinden ve bedensel yanmadan gelir. {ar:جَهَنَّمَ, tr:Jahannam, gloss:cehennem} adındaki ikiz n sese ağırlık verir; ad için aktarılan yer kökenli derinlik çağrışımı da hemen ardından gelen ateşle birleşip kapalı mekân basıncını artırır. Bu ses ve derinlik, özel adın olağan anlamını yoğunlaştıran bir yankıdır; etimoloji kanıtı ya da başka bir sözlük anlamı değildir.

Kişinin bu yerdeki hali {ar:يَصْلَىٰهَا, tr:yaṣlāhā, gloss:orada yanar} ile bedensel olarak açılır; sondaki dişil zamir Jahannam'a dönerek yanmayı belirli yere bağlar. Fiilin ateşe girme, orada kalma ve yakıcı sıcağı çekme alanı, ikinci aktarılan ateş kullanımında da ateş içinde kalma ve sıcaklığı duyumsama yönünü öne çıkarır. Odaktaki Form I insanı yanma halinde gösterir; bildirilen Form II seçeneği ettirici bir fail okuması sunar, ancak tam yüzeyi verilmediğinden bu alternatif odak biçimin yerini almaz. Uzayan ses yanma sıfatlarından sonraki hükme geçişte işitsel bir köprü kurar; bu ses etkisi yanmanın süresini dilbilgisel bildirimin ötesine taşımaz.

Odaktaki yanmanın çevresini 17:8'de Jahannam'ı niteleyen {ar:حَصِيرًا, tr:ḥaṣīran, gloss:hapishane} sözü kapalı bir mekân olarak belirler. Yaṣlāhā çevresindeki biçimce uzak iki sözlük kullanımı bu kapanmaya ayrı katkılar sunar: ilkinde av için kurulan kapan, düzeneğin hazırlanmasını; ikincisinde hedefin içine düşüp yakalandığı tuzak, hedefin tutulmasını öne çıkarır. 17:8'in hapishane imgesi mekânsal sınırı verir; bu iki tuzak işlemi yanmaya, çevrili ve yakalanmış olma baskısını ekler. Ateş sahnenin gerçek zemini olarak kalır; kapan ve tuzak, fiilin çevirisi değil, bu belirli mekânsal bağlantının ikincil yankılarıdır. (17:8)

Yanmanın ardından gelen {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} aynı tekil insan üzerindeki ahlakî yargıyı bildirir; eril tekil özneyle uyuşan mansup edilgen ortaç, bedensel maruziyete bu yargıyı ekler. {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} yakınlıktan fiilen uzaklaştırılma boyutunu getirir. İki paralel mansup edilgen ortaç aynı kişiye bağlanıp yanma sırasında birlikte geçerli durumları kurar; yeni bir fail ya da ikinci bir olay başlatmaz. Böylece ayetin yerel kapanışı bedensel yanma, ahlakî kınama ve ilişkisel-mekânsal çıkarılmayı üst üste getirir.

Kınanma ile uzaklaştırılma, korunaklı konumun yitirilmesi ihtimalini de duyurabilir. Aynı kelime ailesinin ayrı kullanımları güvence, korunmuş hak, dokunulmazlık ve başkası için üstlenilmiş sorumluluk alanına uzanır; korunmuş söz ya da hakkın ihlali üzerine yükümlünün kınanması bu alanın bir parçasıdır. Odaktaki {ar:مَذْمُومًا, tr:madhmūman, gloss:kınanmış} olağan anlamıyla yargıyı verirken, {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir duruma getirdik} ile önceki {ar:لَهُ, tr:lahu, gloss:onun için} atama ilişkisini, {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} ise gerçek uzaklaştırılmayı taşır. Bu birleşim korunaklı bir konum kaybını olası kılar; belirli bir ahit, ihlal ya da hukukî statü ileri sürmez ve odaktaki madhmūman yine “kınanmış” demektir.

Güvence ve dayanma sorusu 17:2'de Allah'tan başka vekil edinmeme, 17:22'de Allah'la birlikte başka ilah edinmeme uyarılarıyla belirir. 17:22'nin ardından {ar:فَتَقْعُدَ مَذْمُومًا مَخْذُولًا, tr:fa-taqʿuda madhmūman makhdhūlan, gloss:kınanmış ve yardımsız kalırsın} denir: dayanağını yitiren kişi kınanmış, yardımsız halde oturup kalır, ayağa kalkamaz. Bu sahne odaktaki kınama ve uzaklaştırılmaya başarısız dayanak ile terk edilmişlik boyutunu ekler. Makhdhūlan yardımsız bırakılmayı, madḥūran ise zorla uzaklaştırılmayı bildirir; 17:22'nin yasak-sonuç kuruluşu da 17:18'deki Cehennem atamasından ayrıdır. Bu bağlantı odaktaki kişiyi müşrik diye tanımlamaz ve iki yerdeki sebebi eşitlemez. (17:2, 17:22)

## İstek, Eylem ve Emek

Güvenilecek dayanak sorusundan ayrı olarak 17:16, tek kişinin payından bir kasabanın eylem ve hüküm dizisine geçer. Önce {ar:أَرَدْنَا, tr:aradnā, gloss:diledik} ile ilahî irade bildirilir; sonra varlıklı sakinlere buyruk gelir ve onların {ar:فَفَسَقُوا فِيهَا, tr:fa-fasaqū fīhā, gloss:orada yoldan çıktılar} davranışı olağan anlamıyla fıskı, yoldan çıkmayı anlatır. Aynı kelime ailesinin olgun hurmanın kabuğundan sıyrılıp dışarı çıkmasını anlatan ayrı kullanımı, bolluk içindeki bu davranış ve hüküm öncesindeki sıralamayla buluşunca örtünün açılıp içindekinin görünmesi imgesini ekler. Böylece imge yoldan çıkma anlamını koruyarak davranışın açığa çıkışını duyurur. (17:16)

17:16'da hüküm kesinleşip kasaba bütünüyle yıkılır; 17:17 Rabbin kullarının günahlarından haberdar ve onları gören olduğunu ekler. Bu eylem-hüküm-görülme dizisi, odaktaki {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık} payını onay işaretinden ziyade davranışın ve sonucun görünür olabileceği bir bağlamda duyurur. Bağlantı bu sahneye özgüdür: hızlandırılan pay fıskın sebebi ilan edilmez, her nimet sınav sayılmaz ve kasaba sakinleri odaktaki adsız kişiyle özdeşleştirilmez. (17:16, 17:17)

Odaktaki {ar:يُرِيدُ, tr:yurīdu, gloss:ister} yakın dünya hayatına yönelirken, 17:19'da âhireti isteyen kişinin {ar:وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-saʿā lahā saʿyahā, gloss:ona yaraşır biçimde çabaladı} oluşu hedefe yönelik hareketi, işe koyulmayı ve emeği öne çıkarır. Bu kişi {ar:مُؤْمِنٌ, tr:muʾmin, gloss:inanan}dır; kelimenin olağan anlamı “inanan”dır, çabayla birlikte gelişi hedefe dönük güvene sınırlı bir nüans ekleyebilir, başarı güvencesi vermez. Emeğin {ar:مَشْكُورًا, tr:mashkūran, gloss:takdir edilen} diye karşılanması, 17:3'teki {ar:عَبْدًا شَكُورًا, tr:ʿabdan shakūran, gloss:şükreden bir kul} ile şükür alanında yankılanır; bu dilsel örüntü kişileri özdeşleştirmez. Böylece erkene alınan pay ile sonraki hedef için gösterilen emek karşılaştırılır, hızın kendisi değil yöneliş ve çaba öne çıkar. (17:19, 17:3)

17:20'de hem bu gruba hem ötekine Rabbin bağışından verilir ve bu bağış kısıtlanmaz; 17:21 kişilerin birbirinden üstün kılınmasını, âhiretin ise derece bakımından daha büyük oluşunu ekler. Böylece odaktaki ʿajjalnā ile erkene alınan pay, daha geniş dağıtımın yalnızca bir parçası olarak görünür. Bu çerçeve tam ölçeği ya da onayı tek başına belirlemez; grupların payları ve kişilerin dereceleri açıklanmadan kalır, çaba da sonucu satın almaz. (17:20, 17:21)

Başka ayetler dileme, emek ve varış arasındaki ilişkiye bağımsız bir pencere açar: 92:4 çabaların çeşitliliğini söyler; 79:40 Rabbin huzurunda durmaktan korkup isteğini dizginleyeni, 79:41 ise Cennet'i yurt edinmesini anlatır. Bu temaslar odaktaki {ar:يُرِيدُ, tr:yurīdu, gloss:ister} ve {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan} yönelişi farklı gayretler ve menziller arasındaki tercih içinde duyurur; böylece dileme ile emek ve varışın birden fazla düzeni görünür. Bu paraleller kendi aralarında üstünlük sırası kurmaz ve 17:18'e emek ya da derece koşulu taşımaz. (92:4, 79:40, 79:41)

## Yakın Yol ve Sonuç

Emek ve derece temasından ayrı olarak, yakınlık bu kez yolculuk imgeleriyle duyulur. {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:ivedi olan} ile {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık}ın aynı kelime ailesindeki yolculukla sınırlı kullanımlarından biri hızlı gidişi, diğeri varış uzaklığını azaltan yakın ya da kestirme yolu anlatır. 17:1'in gerçek gece yolculuğu {ar:أَسْرَىٰ بِعَبْدِهِۦ لَيْلًا, tr:asrā bi-ʿabdihi laylan, gloss:kulunu geceleyin yürüttü} ile {ar:الْمَسْجِدِ الْأَقْصَى, tr:al-masjidi al-aqṣā, gloss:en uzak mescit} yönüne uzanır ve {ar:لِنُرِيَهُ مِنْ آيَاتِنَا, tr:li-nuriyahu min āyātinā, gloss:ayetlerimizden göstermek için} amacını taşır. Bu bağımsız sahne gerçek yolculuğu, uzak varışı ve gösterilecek işaretleri sağlar; yolculuğun kendisi hızlı diye nitelenmez. Birlikte, iki sözlük dalı odağın hemenliğine zaman bakımından hızlı gidiş ve mekân bakımından kısalan mesafe çağrışımlarını ekler. Bu bağlantı 17:18'i gerçek seyahat anlatısına dönüştürmez; oradaki hızlandırma payın zamanına ilişkindir. (17:1)

Rota benzetmesine zaman ufkunu 87:16'da dünya hayatının tercih edilmesi, 87:17'de âhiretin daha hayırlı ve kalıcı oluşu kazandırır. Böylece seçilen hedef kadar ona varışın hangi ömür ufkuna ait olduğu da duyulur. Bu zaman karşıtlığı al-ʿājilah'a kendi başına yol anlamı yüklemez; yol imgesi yalnızca bu bağlamın bağımsız katkısıyla genişler. Hesap-kayıt dizisi (17:13, 17:14, 17:15) ile emek-derece ilişkisi (17:19, 17:21) bu rota bağlantısının kaynağı değil, ayrı yorum çizgileridir. (87:16, 87:17)

79:38 dünya hayatını tercih edeni, 79:39 yakıcı ateşi yurt edinen sonu anlatır; bu çift, rota benzetmesine seçimin varış noktasını ekler ve odaktaki {ar:يَصْلَىٰهَا, tr:yaṣlāhā, gloss:orada yanar} ateşini yönelişin muhtemel sonu olarak duyurur. 7:18'de çıkış buyruğunu kovulma ve Cehennem uyarısının izlemesi, {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} sıfatındaki fiilî uzaklaştırılmaya ayrı bir temas sağlar. Birlikte bu imgeler, hızlı ya da kısa bir varışın kabul edilmiş bir son demek olmadığını düşündürür. Bağlantı bu paralelliklerle sınırlıdır: odaktaki kişi 7:18'de anlatılanla özdeşleştirilmez ve her dünyevî istek için aynı sonuç ileri sürülmez. (79:38, 79:39, 7:18)

20:83, Musa'ya halkından ayrılışını neyin acele ettirdiğini sorarak hız ile topluluktan uzaklaşmayı aynı soruda buluşturur. Odaktaki {ar:عَجَّلْنَا, tr:ʿajjalnā, gloss:öne aldık} payı erkene alırken, sonundaki {ar:مَّدْحُورًا, tr:madḥūran, gloss:kovulmuş} yakınlıktan uzaklaştırılmayı taşır. Bu temas odaktaki zaman hareketine ilişkisel mesafe yankısı ekler; hızlı bağış ile son uzaklaştırma farklı işlerdir. Soru Musa'nın ayrı ayrılışına aittir: ortak olay ya da biçimbilgisel yapı kurmaz, onu kınamaz ve odaktaki adsız kişiyle özdeşleştirmez. (20:83)

</source_prose>
