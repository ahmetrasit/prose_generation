# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:48**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.middle.claims.json`

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
- Refer to source paragraphs as `17:48 ¶N`.

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

`(17:48 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:48",
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
        "citation": "(17:48 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_48/17_48.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_48/17_48.middle.claims.json \
  --ayah-ref 17:48
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_48/17_48.prose.editorial.tr.md`

<source_prose>
17:48, muhatabına kendisi hakkında nasıl örnekler verildiğini incelemesini söyler. Tekil {ar:ٱنظُرْ, tr:unẓur, gloss:bak} emri onu önce bir gözlemci konumuna getirir; {ar:كَيْفَ, tr:kayfa, gloss:nasıl} yan cümlesi hem örnek verme eyleminin tarzını hem de peşinden gelen iki sonucu aynı dikkat çerçevesine alır: örnekleri verenler sapar ve herhangi bir yol bulmaya güç yetiremez. Soru, eylemin gerçekleşip gerçekleşmediğini değil nasıl kurulduğunu araştırmaya açar; yanıtı peşinen belirlemez. Örnek verme ile iki sonuç arasındaki yerel sırayı görünür kılar, bütün nedenleri açıklayan bir kuram sunmaz.

{ar:ٱنظُرْ, tr:unẓur, gloss:bak} buyruğunun olağan görsel dikkati, {ar:كَيْفَ, tr:kayfa, gloss:nasıl} sorusuyla eylem tarzını araştırıp sonucunu tartmaya doğru genişler; bu düşünsel incelemede görsel yönelim de sürer. Bu yöneliş, uydurulmuş bir sözün nasıl kurulduğunun araştırıldığı (4:50) ve görülen işaretten yüz çevrilip onun başka bir adla sınıflandırıldığı (54:2) pasajlarla tematik olarak yankılanır. Bu iki bağlamın 17:48'e katkısı, sözün kuruluşu ile işareti yeniden adlandırma arasındaki yakınlıktır; hedef biçimbilgileri kişiler ya da olaylar arasında özdeşlik kurmaz.

Örnekleri veren {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} etkin, tamamlanmış bir çoğul eylemdir. Özne, ardından gelen sonuçlarda da aynı çoğul grup olarak sürer. Fiil hem {ar:لَكَ, tr:laka, gloss:sana} hedefini hem {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} nesnesini belirtir. Muhatap, içerikten önce kısa {ar:لَكَ, tr:laka, gloss:sana} öbeğiyle duyurulur; edatla ikinci kişi zamirinin birleşmesi örneklerin kime yöneltildiğini öne çıkarır. Böylece {ar:ٱنظُرْ, tr:unẓur, gloss:bak} emrinin tekil muhatabı, sunulan benzetmelerin de hedefi olur. Bu sıranın katkısı yöneltilmişliği vurgulamasıdır; gizleme anlamı taşımaz. Polemik bağlamı yönelişi keskinleştirebilir, fakat düşmanlık datif biçimin kodladığı bir anlam değildir.

Buradaki olağan deyim, {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} ile bir düşüncenin karşılaştırma yoluyla görünür kılınmasıdır; {ar:ضَرَبَ الْمَثَلَ, tr:ḍaraba al-mathala, gloss:örnek vererek açıklamak} kalıbında anlam, eylemle nesnenin birleşiminden doğar. Aynı fiilin yalın sözlük kullanımında bir nesne başka bir şeye indirilerek doğrudan temas ettirilir. {ar:لَكَ, tr:laka, gloss:sana} hedefiyle {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} nesnesinin yan yana gelişi, örneklerin muhatabın önüne kuvvetle konduğu izlenimini ekler. Temas imgesi sözün yöneltilmişliğini duyurur; eylem, olağan anlamıyla örnek sunma olarak kalır.

Belirli, çoğul ve belirtme durumundaki {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri}, tanınabilir bir benzetmeler kümesini gösterir; kümenin kaç örnek içerdiği açık bırakılır. Nesne ilk eylem öbeğini kapatır, hemen ardından gelen {ar:فَ, tr:fa, gloss:sonuç bağlacı} sonuç cümlesini başlatır. Tilavette {ar:لَكَ, tr:laka, gloss:sana} ilişkisinden sonra tanımlı nesnenin ayrıca duyulması, hedefle içeriği ardışık vuruşlar hâlinde öne çıkarırken söz dizimini değiştirmez. Tekil {ar:مَثَل, tr:mathal, gloss:örnek ve benzetme}, bir şeye benzetilerek yapılmış görünür biçimi de adlandırabilir; görüntü üretme ve biçime girme çağrışımları belirli yapılara bağlıdır. Bu yapısal ayrım korunurken, örnek verme eylemiyle belirli muhatabın birleşmesi benzetmeleri tanımayı düzenleyen modeller gibi duyurabilir: burada fiziksel portreden çok örneklerin tanıma üzerindeki etkisi öne çıkar.

Örnek modelinin tanımayı düzenlemesi, onun öğretici gücünü de görünür kılar. Örneğe hak ve açıklamayla karşılık verilmesi, benzetmenin bir durumu anlaşılır kılabildiğini gösterir (25:33); örnek karşısındaki alımlanışın hidayet ya da sapma yönünde ayrılması ise aynı aracın farklı yönelişlere eşlik edebildiğini gösterir (2:26). Bu iki bağlam, odaktaki örneklerin açıklama ve ders çıkarma işlevini korurken alımlanışın değişkenliğini belirginleştirir. Yanlış bir benzetme algıyı daraltıp yol bulmayı güçleştirebilir; bu olasılık öğretici işlevi ortadan kaldırmaz.

Bu öğretici okumaya ek olarak, {ar:لَكَ, tr:laka, gloss:sana} ile belirlenen kişi ve {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} için biri hakkında nitelik bildirme ya da onu betimleme yönündeki ayrı kullanım da düşünülebilir. Bu dalda örnek, kişiye dönük bir tasvir gibi duyulur; hak ve açıklamayla verilen karşılık, böyle bir sözün sınanıp açıklanabileceğini düşündürür (25:33). Temasın sınırı bu kadardır: hedef biçimbilgileri odaktaki kişileri ya da olayları 25:33'teki kişilerle özdeşleştirmez.

{ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} için örnek verme deyiminden ayrı bir okuma, türü, sınıfı ya da üretim kalıbını öne çıkarır. Örnek kurma eylemi böyle bir kalıbı muhatabın önüne koyduğunda temsil, temsil ettiği şeyin yerini alabilir; tanıma, göndergeyi yeniden sınamak yerine sunulan modelin içinde kapanır. Hemen ardından {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} denmesi ve {ar:فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-lā yastaṭīʿūna sabīlan, gloss:bir yol bulmaya güç yetiremezler} ile yol bulma gücünün kesilmesi, modele dönüp onu sınayacak yöntemin kapanması gibi duyulabilir. Bu ihtimale iki bağlam farklı katkı verir: elçinin “büyülenmiş adam” diye sınıflanması kişiyi bir tipe yerleştiren sözü gösterir (17:47); diriliş tartışmasındaki maddi modeller ise temsilin somut düşünme aracı oluşunu aydınlatır (17:49, 17:50, 17:51). Bu özel bağlantı temsilin tanımayı nasıl daraltabileceğini gösterir; her benzetmeyi aldatıcı saymaz ve {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} fiiline kategori hatası anlamı yüklemez.

Örnek verme eyleminden sonra gelen {ar:فَ, tr:fa, gloss:sonuç bağlacı}, sapmayı sonuç sırasının ilk halkası yapar. Bağlacın {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} başına bitişmesi geçişi sıkıştırır, iki eylemi tek fiile dönüştürmez. Tamamlanmış sapmanın ardından gelen ikinci {ar:فَ, tr:fa, gloss:sonuç bağlacı}, süren güç yetirememe durumunu açar. Böylece söz dizimi örnek verme, sapma ve yetersizlik arasında yerel bir ilerleyiş kurar; bu sıra bütün nedenleri açıklama iddiası taşımaz.

{ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} nesne almayan, tamamlanmış ve etkin bir fiildir: örnekleri veren çoğul grup kendisi sapar. Bu biçim, eyleyeni örnek verenlerle aynı grupta tutar; başka birini saptırma anlamı yüklemez, güdülerini ise açıklamaz. Fiildeki çift l sesi, sonuç cümlesine geçişte yerel bir ses dönüm noktası oluşturur.

Sapma fiilinin olağan anlamına eşlik eden bir dal, gizlenip algılanamaz hâle gelmeyi taşır. Sıvıda erime ve ölüyü gömme örnekleri bu dalın başka yapılardaki somut kullanımlarıdır. Odaktaki temsil çerçevesinde {ar:ضَلُّوا۟, tr:ḍallū, gloss:saptılar} bu imgeye, göndergenin model içinde gözden yitmesiyle katkıda bulunur. Buradaki bağ, gerçek bir gizlenme olayı değil, örneğin algı üzerindeki örtücü etkisidir.

Aynı anlam alanındaki yitirme ya da yerini bulamama dalı, kanın karşılıksız kalması gibi özel kullanımları başka yapılarda barındırır. Ardından gelen {ar:سَبِيلًا, tr:sabīlan, gloss:yol}, yön şaşırmayı ve nerede olunduğunu bilememeyi mekânsal bir imgeye açar. {ar:فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-lā yastaṭīʿūna sabīlan, gloss:bir yol bulmaya güç yetiremezler} ilişkisi sabit bir yere varamama hâlini önlerindeki güzergâhı bulamamaya taşır. Bu bağlantıda {ar:سَبِيلًا, tr:sabīlan, gloss:yol}, {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} fiilinin sözlük karşılığı değil, yön kaybını güzergâh arayışına açan imgedir; cümle ayrıca yitirilmiş bir nesne varsaymaz.

Sonuç dizisinin son halkası, {ar:فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-lā yastaṭīʿūna sabīlan, gloss:bir yol bulmaya güç yetiremezler} sözünde olumsuzlanmış güç yetirmeyi yol nesnesiyle birlikte tutar. Bildirici cümledeki {ar:لَا, tr:lā, gloss:...mezler} süren yetememeyi, önündeki {ar:فَ, tr:fa, gloss:sonuç bağlacı} ise sapmanın ardından gelen durumu kurar; burada yasak değil sonuç bildirilir. Belirsiz tekil ve belirtme durumundaki {ar:سَبِيلًا, tr:sabīlan, gloss:yol}, önceden belirlenmiş tek bir güzergâh yerine kullanılabilir herhangi bir yola erişimi anlatır. Güç yetirme işi yapacak kudretle onu mümkün kılan koşulları içerir; yol nesnesi bu kapasiteyi uygulanabilir erişime bağlar. Odaktaki sonuç genel zayıflıktan çok kullanılabilir güzergâha ya da erişim aracına ulaşamamaktır; cümle belirli bir yol veya varış noktası saptamaz.

{ar:سَبِيلًا, tr:sabīlan, gloss:yol} hem üzerinde yürünüp hedefe varılan güzergâhı hem de sonuca ulaştıran yöntemi ya da olanağı anlatabilir. Olumsuzlanan güç yetirme bu iki yüzü birlikte harekete geçirir: kat edilecek yol ve işe yarayacak erişim yolu kullanılamazdır. Bu bağlantı belirli bir dinî yolu özelleştirmez. Amaçlı yeryüzü yolculuğunu anlatan {ar:ضَرَبَ فِي الْأَرْضِ, tr:ḍaraba fī al-arḍ, gloss:yeryüzünde yolculuk etmek} ayrı bir yapıdır; bu hareket anlamı yalın {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} fiiline taşınmaz. Yine de bu ayrı hareket dalı, örnek kuranların ilerleyecek güzergâh bulamayışını ironik biçimde geri çağırır; yankı yol bulamama imgesinde kalır.

Olumsuzlanan {ar:يَسْتَطِيعُونَ, tr:yastaṭīʿūna, gloss:güç yetirebilirler} biçiminin olağan anlamı bir işi yapabilmektir. İlişkili başka bir kullanım, zorlamaya direnmeden yönelmeyi, kolayca uymayı ya da boyun eğmeyi anlatır; eli, hayvanı, dizgini ve dili kolayca yöneltme örnekleri bu dalın başka yapılardaki sınırını gösterir. Bu ayrı anlam, {ar:لَا, tr:lā, gloss:...mezler} olumsuzluğu ile {ar:سَبِيلًا, tr:sabīlan, gloss:yol} birlikte duyulduğunda yola doğru uyumlu bir harekete geçememe gibi sınırlı bir yankı verir. Odaktaki bildirim güç yetirememektir; uyma çağrışımı bu kapasite anlamına eşlik eder.

Çevredeki ayetler yol bulamamanın erişim boyutunu aracılara dair ayrı yönlerden açar: ileri sürülen ilahî ortaklar Taht'ın Rabbine götürecek yolu kendileri arar (17:42); çağrılanlar zararı giderme ya da değiştirme gücünden yoksundur (17:56); Allah'a yakınlık ararken umut ve korku taşırlar (17:57). Bu üç katkının ortak noktası, aracı sayılanların da bağımlı oluşudur; ayetler tek bir mekânsal şemaya dönüşmez. Böylece odaktaki erişemeyiş keskinleşir. Sapma fiilinin yol yokluğuyla birlikte anılması (42:46) aynı kayıp temasına ayrıca yankı verir.

Hatırlatma amacıyla sunulan çeşitli şeylere artan bir yüz çevirme eşlik eder (17:41). Bu alımlanış 17:48'in örneklerini yeni bir ışığa yerleştirir: {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} açıklama ve ders çıkarma işlevini sürdürürken, dinleyicinin yönelişi tersine dönebilir. Bağlantı, örneklerin reddi doğurduğunu değil, sunumun öncesinde başlamış yüz çevirme içinde karşılandığını gösterir.

Elçiyle ahirete inanmayanların arasına konan engel erişimi keser (17:45); örtülen kalpler ve ağırlaştırılan kulaklar bu kapanışı algıya taşır, Allah anıldığında sırt dönülmesiyle yöneliş de görünür olur (17:46). Bunların yanına {ar:ٱنظُرْ, tr:unẓur, gloss:bak} buyruğu ile {ar:سَبِيلًا, tr:sabīlan, gloss:yol} geldiğinde, güzergâh bulamama algısal engellenme gibi duyulur; {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} da gözden yitme çağrışımı kazanır. Bu temas, fiziksel olarak kaybolmuş bir yol ya da önceki engellerden doğrudan kaynaklanan sapma bildirmez; 17:48'deki erişim güçlüğünü algı kapanışıyla birlikte okumayı mümkün kılar.

Elçiyi dinleme sahnesi, sözlerin işitilememesinden çok, dinlemenin özel bir danışmada nasıl yorumlandığını gösterir (17:47). Yanlış yapanlar diye tanıtılan grup, “Siz yalnızca büyülenmiş bir adamın peşinden gidiyorsunuz” der (17:47). “Adam” sözü erkek bir insanı sınıflandırır; büyülenme nitelemesi ise dikkati mesajdan elçiye çevirerek saptırma ve alıkoyma imgesi kurar. Nitelemede neyin alıkonduğu belirtilmez; bu imgenin katkısı, dikkatin yön değiştirmesidir.

Bu sözlü çerçeve, {ar:ٱنظُرْ, tr:unẓur, gloss:bak} buyruğundaki inceleme çağrısıyla yan yana geldiğinde, {ar:لَكَ, tr:laka, gloss:sana} ile hedeflenen {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} ve {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} sözünün dinleyiciler önünde bir tip kurup kimin izleneceğini etkileyebileceğini düşündürür (17:47, 17:48). Ardından gelen {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} ile {ar:سَبِيلًا, tr:sabīlan, gloss:yol}, örnek kurucuların sonucunu bildirir (17:48). Bu, iki ayet arasındaki yerel sıralamanın sunduğu bağlantıdır; ithamın doğruluğunu, bütün benzetmelerin içeriğini ya da tek nedenselliği belirlemez. Emrin girişindeki bağlantı ünlüsüne ilişkin kıraat farkı, ithamdan doğrudan hitaba işitsel bir sınır çizebilir (17:47, 17:48); tekil muhatap ve emir yapısı aynı kalır.

Bu sözlü çerçeveden sonra dirilme itirazı modeli maddi hâllerle kurar: parçalanmış kalıntılar yenilenme itirazını somutlaştırır (17:49); taş ve demir aynı itirazı başka yaratılmış maddi biçimlere taşır (17:50). İlk yaratılışın hatırlatılmasıysa, yenilenmenin imkânsız göründüğü bu hâllere karşı cevabı yaratıcının kudretine yöneltir (17:51). Bu sonraki maddi modeller 17:48'de adlandırılmaz; model imgesinin aldığı yönü gösterir ve elçinin bir tipe yerleştirildiği sözlü çerçeveden (17:47) ayrı kalır.

Bu çağrıya gelen karşılık, {ar:فَلَا يَسْتَطِيعُونَ سَبِيلًا, tr:fa-lā yastaṭīʿūna sabīlan, gloss:bir yol bulmaya güç yetiremezler} sözündeki güç yetirememe okumasına bir sınır çizer. Fiilin kolayca yönelme ve uyma yönündeki ayrı anlamı, yol nesnesiyle birlikte düşünüldüğünde yöneltilen yola uyum sağlayamama gibi duyulabilir; burada bu, kapasite bildirimine eşlik eden sınırlı bir yankıdır. Kalıntı itirazına ilk yaratıcının hatırlatılmasıyla karşılık verilir (17:49, 17:51), ardından çağrı cevap bulur (17:52). Bu geçiş, 17:48'deki yetersizliği kendi bağlamında tutarken sonraki hitabın karşılık bulduğunu gösterir; cevap gönüllü itaati kanıtlamaz ve odaktaki yetersizliği zihinsel ya da bedensel bir kusurla açıklamaz.

En iyi sözü söyleme buyruğu, kişiler arasındaki kışkırtmaya karşı uyarıyla yan yana gelir (17:53); bu birliktelik sözün dinleyicilerin tutumunu etkileyebilen bir edim olduğunu düşündürür. Aynı kelime ailesinin yerinde durmama, yinelenme ve farklı yönlere dağılma kullanımları örnek verme imgesine hareket, tekrar ve yayılma çağrışımları ekler; çatışmaya sevk etme kullanımı da ayetteki kışkırtma uyarısıyla temas eder. Bu uzak dallar keşif niteliğinde bir yankı sunar: odaktaki {ar:ضَرَبُوا۟, tr:ḍarabū, gloss:örnekler verdiler} fiilinin olağan anlamı örnek vermektir; bu örneklerin belli bir kavgaya yol açtığı söylenmez.

Deve işareti açıkça görülürken inkâr edilip haksızlıkla karşılanır (17:59). Bu sahne, {ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} ile aynı nesneyi değil, görünür sunumun alımlanışını karşılaştırmaya açar: {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} sapması bilgi eksikliğinden ibaret değildir, çünkü görünür delil kabulü zorunlu kılmaz. Ayrı bir sahnede gösterilen görü sınama diye nitelenir ve uyarının ardından aşırılık artar (17:60). Bu iki temas, sunumun alımlayanın durumunu açığa çıkarıp sapmayla birlikte bulunabileceğini düşündürür; 17:60'taki sınama sapmanın nedeni, sonraki topluluk da odaktaki grupla özdeş kılınmaz.

{ar:سَبِيلًا, tr:sabīlan, gloss:yol} için ayrı bir sözlük imgesi, gözde kırmızı damarlı ağsı bir perde oluşturarak görüşü örten rahatsızlıktır. Görsel çağrışımın üç ayrı temas noktası vardır: elçiyle inanmayanlar arasındaki engel erişimi kapatır (17:45), deve işareti görülür ama inkâr edilir (17:59), {ar:ٱنظُرْ, tr:unẓur, gloss:bak} buyruğu ise bakışı incelemeye yöneltir. Birlikte, her biri kendi yönüyle, yolun görüş alanı perdelenmişçesine erişilmez duyulmasına katkıda bulunur. Bu bağlantı görsel kapanmayı yürünebilir güzergâh imgesine ekler; rahatsızlık tıbbi teşhis ya da {ar:سَبِيلًا, tr:sabīlan, gloss:yol} sözcüğünün olağan anlamı değildir.

{ar:ٱلْأَمْثَالَ, tr:al-amthāla, gloss:benzetmeleri} ile ilişkili başka bir imge, ağır cezanın başkalarını caydıran ibretlik örnek oluşudur. Şehirlerin yıkımı (17:58) ile açık işaretin inkârı (17:59), {ar:ٱنظُرْ, tr:unẓur, gloss:bak} çağrısının yönünü elçiye sunulan benzetmelerden onları kuranların tutumuna çevirebilir; böylece ibret imgesi bakışı örneklerin içeriğinden sunanların tavrına ve olası akıbete taşır. Bu bağlantı, odak sözcüğe doğrudan ceza anlamı yüklemez ve o akıbeti konuşanlara isnat etmez.

Fâtiha'nın eklenen okuma bağlamında yol imgesi, istenen rehberlikle karşılaşır. {ar:ٱهْدِنَا, tr:ihdinā, gloss:bize yol göster} duası {ar:ٱلصِّرَاطَ, tr:al-ṣirāṭ, gloss:dosdoğru yol} boyunca yol gösterilmesini ister; bu yol nimete erenlerin yolu diye yinelenir ve {ar:ٱلضَّآلِّينَ, tr:al-ḍāllīn, gloss:sapanlar} diye bir grup anılır (1:6, 1:7). Odaktaki {ar:سَبِيلًا, tr:sabīlan, gloss:yol} bulamayış, istenen hidayetin karşı-imgelemi gibi duyulur; {ar:فَضَلُّوا۟, tr:fa-ḍallū, gloss:böylece saptılar} ile Fâtiha'nın sapma adı aynı kök alanında yankılanır (1:7). Bu bağlantı iki ayrı sözcük olan {ar:سَبِيلًا, tr:sabīlan, gloss:yol} ile {ar:ٱلصِّرَاطَ, tr:al-ṣirāṭ, gloss:dosdoğru yol} arasında eşanlamlılık kurmaz; odaktaki kişiler de Fâtiha'nın andığı grupla özdeşleştirilmez. Katkısı, eklenen okuma sırasındaki karşılaşmada yol bulamama ile istenen rehberliği birbirine karşı duyurmaktır.

</source_prose>
