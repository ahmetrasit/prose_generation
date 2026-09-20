# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:11**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.middle.claims.json`

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
- Refer to source paragraphs as `17:11 ¶N`.

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

`(17:11 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:11",
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
        "citation": "(17:11 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_11/17_11.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_11/17_11.middle.claims.json \
  --ayah-ref 17:11
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_11/17_11.prose.editorial.tr.md`

<source_prose>
## Çağrının Sözdizimi

17:11'de insan hem kötülüğü hem iyiliği çağırır; ayet aynı insanı ardından aceleci diye niteler. {ar:ٱلْإِنسَٰنُ, tr:al-insānu, gloss:insan} eylemin açık öznesi, {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} etken fiilidir. {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} ile {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilik için} aynı çağrının karşıt içeriklerini verir; aralarındaki {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} mastarı da eylemi yeniden adlandırır. Son sıfat {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci}, çağıran insanı niteler. Böylece cümle, ahlaki anlamları ayrı kalan iki değerin aynı insanın isteğine girebildiğini söyler.

Başlangıçtaki {ar:وَيَدْعُ, tr:wa-yadʿu, gloss:ve çağırır} biçiminde bağlaç fiile bitişir ve cümleyi bekletmeden insanın eylemine açar. İlk waw önceki söyleme yerel bir bağ kurar; önceki kısmı kendi başına uyarı ya da ceza diye adlandırmaz. Belirli tekil {ar:ٱلْإِنسَٰنُ, tr:al-insānu, gloss:insan} genel insan türünü özne yapar: bu genellik tek bir adlandırılmış kişiye indirgenmediği gibi bireysel örnekleri de dışlamaz. Etken, yinelenebilir {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} çağırmayı insana yükler ve bir eylem örüntüsü kurar; her insanın her an aynı isteği dile getirdiğini söylemez. Yazıda fiilin son vavı görünmezken tilavette uzun ünlü korunur: sayfadaki biçim kısa görünür, sesli okuyuş uzar; fiil sesletimde kısalmış ya da eksik kalmış olmaz.

İnsanın ne çağırdığı, {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} öbeğindeki bā ile belirtilir. Kötülük doğrudan nesne değil, çağrının içeriğidir; bu nedenle karşılaştırma tamamlanmadan önce istenen zarar olarak duyulur. Aynı edat isteğe hangi yoldan karıştığı konusunda daha ihtiyatlı, nedensel ya da araçsal bir tını da bırakır; içerik okuması önde kalır. Bu bā'lı yapı ile ardından gelen aynı çağırma ailesinden mansup mastar, bağlamı dilek ve yakarışa daraltır; adlandırma, hak iddia etme, yemeğe ya da belirli bir yere çağırma gibi anlamlar başka yapılara bağlıdır.

Fiilden sonra gelen {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} mastarı çağırma eylemini ad olarak yineler, hem adlandırır hem ölçer. Kötülük ile iyilik arasına yerleştiğinden tek bir çağrının bu iki karşıt içeriği nasıl taşıdığını gösterir; mastarın katkısı eylemi yeniden adlandırıp belirginleştirmektir. Uzun ünlülerle hemze, fiilin yankısını uzatıp iki içeriğin arasındaki çağrıyı işitilir kılar. Sondaki kişi eki bu isteme tarzını aynı genel insana bağlar: burada belirginleşen, isteği kimin dile getirdiğidir; istenen sonuçları denetlemesi değil.

Çağırmanın sözlük ailesindeki bir kullanım, ses ve sözle yöneltileni konuşana doğru çekmektir. Odaktaki {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} ile {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} bu yönelişi, yalnız zihinde kalan bir arzudan çok sesle dışarı çıkan bir isteme gibi duyurur. Bağımsız bir sahnede iyilik çağrısını zararın dokunması izler: {ar:دُعَآءِ ٱلْخَيْرِ, tr:duʿāʾi l-khayri, gloss:iyilik çağrısı}nı {ar:مَسَّهُ ٱلشَّرُّ, tr:massahu sh-sharru, gloss:zarar ona dokunduğunda} görürüz (41:49). Bu karşılaşma odaktaki örüntüyü genişletir; burada zarar çağrının içeriği değil, iyilik çağrısının ardından gelen olaydır.

İki bā'lı öbek aynı belirli ve soyut biçimde, aynı sözdizimsel yerde durur. İlk gelen {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} tanınan zarar ve kötülük kategorisini adlandırır; tek tek sonuçları ya da bir derece sıralamasını değil. Mastardan sonra gelen {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilik için} karşıt olumlu değeri aynı kalıpta yineler ve karşılaştırmayı kapatır; ad soyut iyilik olarak kalır, “daha iyi” sıfatına dönüşmez. Eşleşen konumlar iki değeri biçimsel olarak karşılaştırılabilir kılar, ahlaki ayrımı korur. Kötülüğün önce duyulması başlangıca ağırlık verir; iyilikle kapanış karşıtlığı tamamlar. Kötülük öbeğindeki ikizleşmiş ş sesi de işitsel ayrımı belirginleştirir; anlamı sözcüklerin olağan karşıtlığı taşır.

Bu karşılaştırmanın kötülük kutbu olağan anlamıyla zarar ve kaçınılacak olumsuzluktur. Aynı sözcüğün ayrı bir kullanımındaki {ar:شَرَارَة, tr:sharārah, gloss:kıvılcım}, ateşten kopup havaya sıçrayan yanar parçacıktır. Bu kıvılcım dalının taşıyıcısı odaktaki kötülük öbeği; bağımsız tetikleyicileri ise içeriği dışarı veren {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} eylemiyle beklemeden davranmayı anlatan {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} niteliğidir. Kıvılcım sıçrayışın uçuculuğunu, çağrı içeriğin dışarı çıkışını, acele salıverilişin hızını katar; birlikte zararlı isteği küçük ve uçucu bir başlangıç gibi duyururlar. Bu temas benzetme düzeyindedir: odaktaki kötülük anlamını korur, fiziksel ateşleme ya da kesin nedensellik ileri sürülmez.

## Acele ve Ayırt Etme

İyilik-kötülük karşılaştırması tamamlanınca ikinci waw'la açılan {ar:وَكَانَ, tr:wa-kāna, gloss:ve idi} cümlesi yeni bir özne-yüklem teşhisine döner. İlk {ar:وَيَدْعُ, tr:wa-yadʿu, gloss:ve çağırır} insanın eylemini, ikincisi onu izleyen niteliği getirir; iki açılış böylece iki vuruşlu bir gözlem ve teşhis çerçevesi kurar. {ar:وَكَانَ, tr:wa-kāna, gloss:ve idi} önceki karşılaştırmayı kapatırken aceleciliği hem çağrıdan sonra gelen bir tanı hem de çağrının gerçekleştiği hâl gibi duyurabilir. İki ilişki ayetin yerel dizilişinde birlikte kalır; bu okuma, eylemden teşhise geçişe dayanır, daha geniş sûre yapısı iddiasına değil.

İlk cümlenin yinelenebilen {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} fiiliyle ardından gelen geçmiş biçimli {ar:كَانَ, tr:kāna, gloss:idi} aynı insan için yerleşik bir durum teşhisi kurar: çağrı tek bir geçmiş ana kapanmaz, niteliği de değişmez öz ilan edilmez. Burada {ar:كَانَ, tr:kāna, gloss:idi} bağ fiilidir; {ar:ٱلْإِنسَٰنُ, tr:al-insānu, gloss:insan} özne, {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} yüklemdir. Yapı niteliği insana yükler, onu aceleci kılan bir neden bildirmez. İnsan adının zamir yerine yinelenmesi çağıran genel insanı niteliğin taşıyıcısı olarak yeniden öne çıkarıp ayet içindeki bağı kapatır; tekrarın kapsamı daha geniş bir insan formülü değildir. Bu öne çıkarma bedensel değil dilbilgiseldir: insan, acele niteliğini taşıyan özne olarak belirir.

Yaygın durum fiili {ar:كَانَ, tr:kāna, gloss:idi} ile sonundaki seyrek ve belirgin {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} sıfatının yerel eşleşmesi teşhisi keskinleştirir; keskinlik fiilin sık kullanılmasından değil bu karşıtlıktan doğar. Hareket ve hızla ilişkili anlam ailesinden gelen sıfat, seyrek faʿūl kalıbında insan niteliğini bildirir; tek bir eylemin hızını değil alışılmış yatkınlığı adlandırır. Belirsiz ve mansup yüklem aceleciliği nötr çabukluktan daha yoğun duyurur. Cümlede açıkça yüklemdir; çağrıya eşlik eden koşul gölgesi duyulabilse de niteliği insana verir. Genel insan öznesi bu yatkınlığın her bireyde her an aynı davranış olarak görünmesini gerektirmez. Sondaki sıfat, karşıt içeriklerin aynı çağrı tarzında dile getirilebilmesine son sözü verir; uzun ünlü ile tenvinli kapanış bu tanıya işitsel ağırlık ekler.

Bu sıfatın olağan acelecilik anlamının yanında, beklemeden ve bir şeyi vaktinden önce isteyerek davranma kullanımı da vardır. Bu kullanımı burada bağımsız olarak tetikleyen, insanın kötülüğü de iyiliği de aynı çağrı kalıbına koymasıdır: acele hızlı eylemden erkenci değerlemeye kayar, çünkü istek sonuçlar ayrışmadan dile gelir. {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} fiiliyle {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} mastarı tek isteme eylemini yineler, {ar:كَانَ, tr:kāna, gloss:idi} bunu insanın durumu olarak teşhis eder, {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} beklemeyen niteliği taşır. Böylece karşıt içerikler aynı talep kanalına, değerlendirmeye ayrılan süre daralmışken girer. Bu bağlantı yalnız odaktaki insan niteliğini yorumlar; her yakarışa, başka bir yaşam çizgisine ya da sözün fiziksel sonuç doğurduğu bir nedenselliğe genellenmez.

{ar:ٱلْإِنسَٰنُ, tr:al-insānu, gloss:insan} adının olağan anlamı genel insandır. Aynı anlam ailesindeki {ar:آنَسْتُ الشَّيْءَ, tr:ānastu ash-shayʾa, gloss:şeyi görüp fark ettim} kullanımı gözle görerek fark etme ve seçmeyi anlatır; bu yorum yalnız o görsel ayırt etme kolundan yararlanır, işitme, belirti sezme ve çevreyi araştırma anlamlarını insan adına aktarmaz. Odaktaki iki değerin eşlenmiş çağrısı ve aceleci nitelik, algılama imkânı olan insanla sonuçları zamanında ayırt edememe arasında gerilim kurar. Sözlük karşılığı yine “insan”dır; bu bilişsel temas onu “algılayan” ya da “unutkan” diye çevirmek yerine acele karşısında tanıma imkânını belirginleştirir.

Bu gerilim, çevredeki gösterme ve hesap sahneleriyle somutlaşır. {ar:لِنُرِيَهُۥ مِنْ ءَايَٰتِنَآ, tr:linuriyahu min āyātinā, gloss:ayetlerimizden gösterelim} ifadesi ve açık alametler bir gösterme sahnesi kurar (17:1); odaktaki insanın onları özellikle fark ettiğini bu sahne tek başına söylemez. Gündüz ayetinin aydınlatıcı kılınması görünür dünyayı arayışa açar: {ar:لِّتَبْتَغُوا۟ فَضْلًا, tr:li-tabtaghū faḍlan, gloss:bir lütuf arayasınız diye} arayışı, {ar:عَدَدَ ٱلسِّنِينَ وَٱلْحِسَابَ, tr:ʿadada as-sinīna wa-l-ḥisāb, gloss:yılların sayısı ve hesap} zaman hesabını, {ar:وَكُلَّ شَىْءٍۢ فَصَّلْنَٰهُ تَفْصِيلًا, tr:wa-kulla shayʾin faṣṣalnāhu tafṣīlan, gloss:her şeyi ayrıntılandırdık} ise ayrımları gözetmeyi ekler (17:12). Bu iki bağlam, iyilikle zararı tartmak için görünür inceleme basamakları sağlar; insan adının olağan anlamını değiştirmeden aceleci çağrı çevresindeki ayırt etme gerilimini derinleştirir.

## İyilik, Ölçü ve Vakit

Odaktaki {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilik için} belirli ve soyut iyilik değeridir, seçenekler arasındaki “daha iyi” değildir. Aynı sözcük ailesinin seçenekler içinden daha iyi görüleni arayıp ayırma ve seçme kullanımı, karşısındaki kötülük ve aceleciliğin zaman baskısıyla burada önem kazanır: istenen iyilik ayırt etmeyi gerektiren bir amaç gibi duyulur, adı ise soyut iyilik olarak kalır. Yerel rehberlik bu amaca ölçü verir; doğru ve istikametli olan {ar:يَعْمَلُونَ ٱلصَّٰلِحَٰتِ, tr:yaʿmalūna aṣ-ṣāliḥāt, gloss:salih ve uygun işler yaparlar} eyleminde, {ar:أَجْرًا كَبِيرًا, tr:ajran kabīran, gloss:büyük bir karşılık} ise işin sonucunda görünür (17:9). Bu, rehberlik bağlamının sunduğu bir ölçüdür; odaktaki khayr'ın bütün kullanımlarını tanımlamaz ve karşılığın vaat oluşuna da açıktır.

Bu hedefin yanına toplu ve yol gösterici bir yakarış biçimi konabilir. Fātiḥa'da yardım dileği toplu sesle gelir ({ar:وَإِيَّاكَ نَسْتَعِينُ, tr:wa-iyyāka nastaʿīn, gloss:yalnız Senden yardım dileriz}; 1:5); ardından dosdoğru yola yönelme istenir ({ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet}; 1:6), sonrasında bu yol nimet verilenlerle, öfkeye uğrayanların ve sapanların yolundan ayrıştırılır ({ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ, tr:ṣirāṭ alladhīna anʿamta ʿalayhim ghayri l-maghḍūbi ʿalayhim wa-la ḍ-ḍāllīn, gloss:nimet verilenlerin yolu; öfkelenilenlerin ve sapmışların yolu değil}; 1:7). Bu örnek, tek bir nesneye yönelen {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} yanına toplu yardım ve istikamet arayışını koyar. Bağlantı doğrudan alıntı ya da gönderme değil: 17:11 muhatabı veya toplu kapsamı belirtmez, rehberlik zaten yerel bağlamda 17:9'da yer alır; Fātiḥa'nın katkısı yeni bir yol öğretisi sunmak değil ortak dua biçimini göstermektir.

Bu iki kutbun değeri, istenen şeyle gerçek yarar veya zarar her zaman örtüşmediğinde belirginleşir. Sevilen şey zararlı, sevilmeyen şey yararlı olabilir (2:216); insan iyilik için acele ederken zarar aynı hızda öne alınmaz (10:11); iyilikle kötülük birlikte sınanma olarak anılır (21:35). İyilik çağrısını zararın insana dokunması izleyen sahne de odaktaki iyi çağrısı ile zarar arasındaki bağı genişletir (41:49). Geceyle gündüzün ölçülü düzeni ve hemen arananla daha sonraki çabanın, bağışın ve derecelerin ayrılması zaman ufkunu açar (17:12, 17:18, 17:19, 17:20, 17:21). Bu bağlamlar karşıt değerleri ayırarak istekle gerçek sonuç arasındaki aralığı görünür kılar; zararı kendi başına ahlaki suç saymadan ve çağrıyı sonucun nedeni yapmadan, ortak katkıları acele değerlemesinin bu aralığı daraltmasıdır.

Zaman sorusu nesnenin yanına eklenir: insanın {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} çağrısı ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} niteliği olumsuz sonucun ne zaman gelmesini istediği sorusunu da açar. Zararın insan hızına göre öne alınmaması bu baskının bir karşıtını verir (10:11); bir payın hesap gününden önce hızlandırılmasının istenmesi başka, bağımsız bir talep örneğidir ({ar:عَجِّلْ لَنَا قِطَّنَا قَبْلَ يَوْمِ ٱلْحِسَابِ, tr:ʿajjil lanā qiṭṭanā qabla yawmi l-ḥisāb, gloss:payımıza düşeni hesap gününden önce hızlandır}; 38:16). Sayım sürerken acele etmeme çağrısı bu isteğin karşı kutbunda durur (19:84). Bu karşılaştırma geliş zamanını belirleme baskısını düşündürür; odak belirli bir ceza ya da pay adlandırmaz, sözün sonucu meydana getirdiğini ileri sürmez ve 38:16'daki talebi 17:11'deki çağrıyla özdeşleştirmez.

Yakın olanla ertelenen sonuç arasındaki fark sonraki ayetlerin zaman ufkunda açılır. Ahirete inanmayanlar için acı verici ceza bildirilir (17:10); hemen gelen dünya hayatının istenmesi ise seçici bir hızlandırma anlatımıyla yan yana durur: {ar:ٱلْعَاجِلَةَ, tr:al-ʿājilah, gloss:hemen gelen dünya hayatı} istenir, {ar:عَجَّلْنَا لَهُۥ فِيهَا مَا نَشَآءُ لِمَن نُّرِيدُ, tr:ʿajjalnā lahu fīhā mā nashāʾu liman nurīdu, gloss:dilediğimizi dilediğimiz kişiye orada hızla veririz} seçici verişi belirtir ve ardından {ar:جَهَنَّمَ, tr:Jahannam, gloss:cehennem} ihtimali görünür (17:18). Buna karşılık ahireti isteyen kişi ona özgü çabayla sürekli çalışır ({ar:وَمَنْ أَرَادَ ٱلْءَاخِرَةَ وَسَعَىٰ لَهَا سَعْيَهَا, tr:wa-man arāda al-ākhirata wa-saʿā lahā saʿyahā, gloss:ahireti isteyen ve ona özgü çabayla çalışan}) ve çabası takdir edilir ({ar:كَانَ سَعْيُهُم مَّشْكُورًا, tr:kāna saʿyuhum mashkūran, gloss:çabaları takdir edilir}; 17:19). Bu karşılaştırma varış hızının tek başına iyiliği belirlemediğini gösterir; odaktaki çağrıyı ahiret inkârıyla özdeşleştirmeden, daha dar ve aceleyle söylenmiş istek okumasını korur.

Acele ailesinin ayrı bir adı olan {ar:العَجَالَة, tr:al-ʿajālah, gloss:çabuk sunulan ya da kolay yenilen azık}, yolcunun hurma ve kavrulmuş tahılını, çobanın hızla getirdiği sütü veya hazırlık bitmeden sunulan yemeği anlatır. Bu somut azık, hemen gelen hayat ve seçici hızlandırmaya; ardından gelen sürdürülen çabaya; iki ayrı yönelişe kesintisiz uzanan bağışa ve paylar arasındaki derecelere gündelik bir yüz kazandırır (17:18, 17:19, 17:20, 17:21). Böylece acele ailesinin bu ayrı adı, zaman ufkuna erken gelenin elle tutulur imgesini ekler. Odaktaki {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} ise insan niteliğidir; yiyecek adı onun anlamını üstlenmez. İstenmeyen sıkıntının hızla ulaştırılmasına ilişkin başka kullanım ilahi seçici veriş bağlamına aittir (17:18), insanın sözlü çağrısının yapısına değil.

Bu verişte iki ayrı yönelişe kaynak sürer: {ar:كُلًّا نُّمِدُّ هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ, tr:kullan numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:iki gruba da destek veririz} ve Rabbinin bağışının engellenmediği bildirilir ({ar:عَطَاءُ رَبِّكَ وَمَا كَانَ عَطَاءُ رَبِّكَ مَحْظُورًا, tr:ʿaṭāʾu rabbika wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışı engellenmiş değildir}; 17:20). Sonraki bakış bazı kişilerin diğerlerine göre farklılaştırılmasını ve üstün kılınmasını, ahiretin ise derece bakımından daha büyük oluşunu gösterir ({ar:ٱنظُرْ كَيْفَ فَضَّلْنَا بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:unẓur kayfa faḍḍalnā baʿḍahum ʿalā baʿḍ, gloss:bir kısmını diğerlerine nasıl üstün kıldığımızı gör}, {ar:وَلَلْءَاخِرَةُ أَكْبَرُ دَرَجَٰتٍۢ, tr:wa-la-l-ākhiratu akbaru darajāt, gloss:ahiret derecece daha büyüktür}; 17:21). İstek bu çerçevede dile gelir ama alınan miktarı ya da sırayı belirlemez; çağrının yöneltme hareketi ile verenin elindeki dağıtım yan yana işler. Geniş bağış dua etkinliğini dışlamaz: etkili dua, farklı yönelişlere uzanan destekle birlikte düşünülebilir. Dereceler de aceleci evet-hayır beklentisini aşan sonuç farklılıklarını gösterir.

İyilik ailesinin ayrı bir kullanımı malı veya serveti, kimi açıklamalarda çok ya da övgüyle edinilmiş malı adlandırır; odaktaki soyut iyilik bu anlam dalından daha geniştir ({ar:خَيْر, tr:khayr, gloss:genel iyilik}). Servetin açıkça anılması (17:6), armağan ve payların dağıtılmasıyla (17:20, 17:21) birlikte, istenen iyiliğin maddi bir payı da içerebileceğini düşündürür ({ar:بِأَمْوَٰلٍۢ وَبَنِينَ, tr:bi-amwālin wa-banīna, gloss:mallar ve oğullarla}). Bu maddi olasılık tarihî topluluk ile sonraki dağıtım bağlamında kalır; odaktaki isteği özellikle para diye belirlemez, servet dalı da khayr'ın evrensel tanımı değildir.

## Ölçü ve Değiş Tokuş

İstemenin başka bir maddi imgesi sallanarak doldurulan ölçüdür: sallandıkça içindekiler yerleşir, kap kullanılabilir hacmiyle dolar. Çağırma fiili {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} ve mastarı {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} bu ayrı ölçü kullanımını taşır; {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} erkenci baskıyı, {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilik için} ise arzulanan değer ölçütünü getirir. İçerik yerleşip hacim dolmadan çağrının kapasiteyi hemen doldurmaya zorlaması böylece görünür olur. Ölçü imgesi meseleyi yanlış nesne seçimine değil, sonuç hazır olmadan kapasiteyi şimdi doldurma baskısına bağlar. Bu benzetmede iyilik ölçüt işlevindedir; kap ya da içine dolan madde değildir.

Acele ailesinde, odaktaki {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci} sıfatından biçimce farklı bir kullanım yavrusunu olağan vaktinden önce doğuran gebe dişiyi anlatır. Çağrı fiiliyle mastarın belirttiği istenen sonuç bu erkenci varış imgesine temas edince talep, hazır oluşundan önce sonuç beklemeye benzer. Bu kullanım benzetmeye vakitsiz varış boyutunu verir; gebelik gerçek bir olay olarak ileri sürülmez ve odaktaki çağrı anlamı yerinde kalır.

Bir başka benzetmede biçimsel karşılaştırılabilirlik alışveriş imgesini açar. {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} ile {ar:بِٱلْخَيْرِ, tr:bi-l-khayri, gloss:iyilik için} aynı sözdizimsel yerde durur; {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} mastarı bu kalıp içindeki isteme tarzını ölçer. Kötülük sözcüğünün ayrı bir kullanımı bedel karşılığı alıp satmayla ilgilidir; bu dal, iyilik aynı karşılaştırma çerçevesine girdiğinde zararı istenen şey uğruna ödenen bedel ya da alınan karşılık gibi gösterir. Aynı sözcüğün “eş ve denk” kullanımı da ortak sözdizimsel konumla etkinleşir ve biçimsel denkliği ekler. Bu iki kullanım odaktaki kötülük ve zarar anlamını değil, benzetmenin alışveriş işlemlerini sağlar.

İyiliğin seçenekler arasından daha iyi olanı ayırıp seçme kullanımı alışveriş imgesine karar ölçüsünü katar. Karşıt seçenek ve {ar:عَجُولًا, tr:ʿajūlan, gloss:aceleci}nin zaman baskısı uzun vadeli değeri tartmaya ayrılan süreyi kısaltır; zarar, arzulanan şeye ödenebilecek bedelmiş gibi aceleyle kabul görür. Böylece aynı konumdaki öbekler, bedel dalı ve mastarın ölçtüğü isteme tarzı birlikte yanlış fiyatlandırılmış bir alışveriş imgesi kurar: seçilebilecek daha iyi sonuç yeterince tartılmadan zarar onun denk karşılığı sayılır. Bu katkı değerleme benzetmesiyle sınırlıdır; gerçek bir piyasa işlemi kurulmaz, iki değer ahlaken eşitlenmez ve khayr soyut isim olarak kalır.

## Dönüş ve Kayıt

Alışveriş imgesinde tek bir seçimin bedeli tartılır; çağırma ailesinin ayrı, yapıya bağlı {ar:التداعي بالسقوط, tr:at-tadāʿī bi-s-suqūṭ, gloss:birbiri ardından çöküş} kullanımı ise art arda gelen hareketi sağlar. Bu kullanım duvarların ya da yapı parçalarının birbiri ardına kendiliğinden düşmesini, bir failin de onları sırayla yıkmasını anlatır. Odaktaki {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} ile {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı} dışarı yönelen sözü taşır; kıvılcım dalı küçük parçacığın sıçrayışını, acele değerlendirme aralığının kısalmasını getirir. Bu katkılar birleşince çağrı olası dizinin ilk halkası gibi duyulur: söz dışarı çıkar, kıvılcım imgesi yayılabilir bir başlangıç verir, acele ise aradaki değerlendirme durağını silikleştirir. Bu bağlantı yalnız olasılık imgesidir; fiziksel nedensellik ya da kesin sonuç ileri sürmez.

Art arda geliş imgesinin yanında, başka bir bağlam sonuçların aynı özneye geri döndüğü bir halka kurar. İki bozulma ve ardından üstünlüğün geri verilmesi döngünün önceki basamaklarını açar (17:4, 17:6). İyilik edenin yararı, kötülük edenin zararı yine kendi benliğine döner ({ar:أَحْسَنتُمْ لِأَنفُسِكُمْ, tr:aḥsantum li-anfusikum, gloss:iyilik ettiğinizde kendiniz için etmiş olursunuz}; {ar:وَإِنْ أَسَأْتُمْ فَلَهَا, tr:wa-in asaʾtum fa-lahā, gloss:kötülük ettiğinizde yine kendinize etmiş olursunuz}; 17:7). Geri dönme koşuluyla karşılığın yinelenmesi halkayı kapatır ({ar:وَإِنْ عُدتُّمْ عُدْنَا, tr:wa-in ʿudtum ʿudnā, gloss:geri dönerseniz biz de döneriz}; 17:8). Bu toplu tarih anlatısıyla odaktaki çağrı arasındaki benzerlik, sonuçların geri dönebilen düzenindedir; çağrının bu olayları başlattığı ileri sürülmez. Bu sınır yalnız iki sahne arasındaki nedensellik iddiasını belirler; tarih anlatısının kendi okumasını daraltmaz.

Kişinin kendi payına dönüşünden ayrı bir ölçekte, başka bir sahne kentin toplumsal yıkıma giden aşamalarını gösterir (17:16). Odaktaki {ar:بِٱلشَّرِّ, tr:bi-sh-sharri, gloss:kötülük için} olağan anlamıyla zarar ve kötülüktür; onun ayrı kıvılcım kullanımı ile yapısal çöküşü anlatan {ar:التداعي بالسقوط, tr:at-tadāʿī bi-s-suqūṭ, gloss:birbiri ardından çöküş} dalını, bu ayetin kendi toplumsal sırası yan yana getirir. Önce refah içindekiler rahatlık yaşar ({ar:مُتْرَفِيهَا, tr:mutrafīhā, gloss:refah içindekileri}); sonra orada taşkınlık ederler ({ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:orada taşkınlık ettiler}). Taşkınlık bildiren sözcüğe eşlik eden olgun hurmanın kabuğundan çıkış imgesi sınır aşımını canlandırır. Ardından hüküm bağlayıcı biçimde kesinleşir; söylenmiş söz geçiş eşiği olur ({ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawl, gloss:üzerine hüküm kesinleşti}) ve şehir bütünüyle yıkılır ({ar:فَدَمَّرْنَٰهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık}). Kıvılcım küçük başlangıcı, çöküş dalı ardışık yıkımı, 17:16 ise bu imgeleri birleştiren kolektif yargı sırasını sağlar. Bu özel benzetme odaktaki tekil yakarışı kentin fiziksel nedeni yapmaz.

Kolektif yıkım sahnesinden sonra dikkat tek insanın bedenine ve kaydına döner. Odaktaki {ar:يَدْعُ, tr:yadʿu, gloss:çağırır} ile {ar:دُعَآءَهُۥ, tr:duʿāʾahu, gloss:onun çağrısı}nın olağan yönelişi muhatabı ses ve sözle konuşana doğru çeker; bu dışa yöneliş, eylemin sahibinden kopması değil, izinin onunla kalması olarak da düşünülebilir. Kişinin uçuşla ilişkilendirilen payı boynuna bağlanır: {ar:طَٰٓئِرَهُۥ, tr:ṭāʾirahu, gloss:uçuşuyla ilişkilendirilen payı}, {ar:أَلْزَمْنَٰهُ, tr:alzamnāhu, gloss:ona bağladık} ile zorunlu biçimde iliştirilir; {ar:عُنُقِهِۦ, tr:ʿunuqihi, gloss:boynunda} bu bağı bedende konumlandırır (17:13). Ardından açık halde karşısına çıkan kitap izi görünür kılar ({ar:كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:kitāban yalqāhu manshūran, gloss:açık halde karşısına çıkan bir kitap}; 17:13). Kişiye kitabını okuması söylenir ({ar:ٱقْرَأْ كِتَٰبَكَ, tr:iqraʾ kitābaka, gloss:kitabını oku}); aynı benlik hesap görücü olarak yeterlidir ({ar:كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:kafā bi-nafsika al-yawma ʿalayka ḥasīban, gloss:bugün hesap görücü olarak kendi nefsin yeter}; 17:14). Çağrı dışarı yönelişi, boyna bağlanan pay sahibinden kopmayan ilişkiyi, açık kitap ise okunabilir izi sağlar; birlikte ayrılıp gidenin aynı kişinin karşısına çıkmasını düşündürür. Kitap kişinin bütün işlerini kapsar, uçuş imgesi özellikle dua diye belirtilmez; bu benzetme genel kaydı tek bir sözlü isteğin özel kaydı saymaz.

</source_prose>
