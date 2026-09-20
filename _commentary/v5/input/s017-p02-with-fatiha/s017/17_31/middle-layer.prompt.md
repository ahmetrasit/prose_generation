# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:31**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.middle.claims.json`

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
- Refer to source paragraphs as `17:31 ¶N`.

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

`(17:31 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:31",
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
        "citation": "(17:31 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_31/17_31.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_31/17_31.middle.claims.json \
  --ayah-ref 17:31
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_31/17_31.prose.editorial.tr.md`

<source_prose>
## Buyruğun Sınırı

17:31 çocukları yoksulluk korkusuyla öldürmeyi yasaklar. {ar:أَوْلَٰدَكُمْ, tr:evlâdekum, gloss:çocuklarınız} yasağın doğrudan nesnesidir; {ar:خَشْيَةَ إِمْلَٰقٍۢ, tr:haşyete imlâkin, gloss:yoksulluk korkusu} ise bu eylemi güdüleyebilecek endişeyi adlandırır. Ardından çocuklar ve muhataplar, {ar:نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:nahnu narzuquhum ve iyyâkum, gloss:onlara da size de rızık veririz} sözünde aynı sağlama ilişkisinin alıcıları olur. Son hüküm, {ar:إِنَّ قَتْلَهُمْ كَانَ خِطْـًۭٔا كَبِيرًۭا, tr:inne qatlahum kâne khiṭ'en kebîran, gloss:onların öldürülmesi büyük bir günahtır} diyerek öldürmeyi ağır bir yanlış olarak niteler.

Buyruğun başındaki {ar:وَ, tr:ve, gloss:ve} söyleyişi önceki akışa bağlar, ancak hangi özel hükmün sürdüğünü tek başına belirlemez. Hemen ardından gelen {ar:لَا, tr:lâ, gloss:yapmayın} olumsuzluğu fiilden önce kısa ve keskin duyulur; ikinci çoğula yönelmiş cezmli {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} ise muhataplara yapılmaması istenen bir eylem yükler. Böylece söz yalnızca ölümün yokluğunu bildirmez, öldürme eylemi karşısında insanın sorumluluğunu açıkça kurar.

Bu eylemin nesnesi, hemen ardından gelen {ar:أَوْلَٰدَكُمْ, tr:evlâdekum, gloss:çocuklarınız} ile belirginleşir. Kırık çoğul çocukları topluca korunan bir sınıf olarak gösterir; sondaki -kum onları doğrudan muhataplara bağlar. Yakın gönderim soy çizgisinden önce gerçek çocukları gösterir. {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} yalın biçimiyle çocukların canını alıp yaşamını sona erdiren eylemdir; yoğunlaştırma ya da yineleme anlamı başka bir fiil kalıbına aittir.

## Korku ve Sağlama

Canı alınan bu çocukların öldürülme gerekçesi {ar:خَشْيَةَ, tr:haşyete, gloss:korku} ile açılır: sözcük, sakınılan bir şey karşısındaki korku ve ürpermeyi taşır; {ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} ise korkulan koşulu belirtir. Kanonik biçimde korku adının nasbı onu öldürme yasağının sebebine bağlar. Darlık endişesi eylemi güdüleyebilir, ama ona izin vermez. Aktarılan merfû okuyuş bu dilbilgisel ilişkiyi başka türlü kurar; burada açıklanan sebep bağı kanonik nasb biçimine aittir. Korkudaki nefesli başlangıçtan imlâkın sert qāf kapanışına uzanan ses de endişeyi duyurur.

{ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} az malın yanı sıra eldekinin tükenip ihtiyaç içinde kalmasını da anlatır. Fiilden süreç adı yapan IV kalıbındaki bu biçim, ayette yoksullaşmayı yaşanan durum olarak değil, korkulan gelecek olarak kurar. Terimin Kur'an'daki seyrek başka kullanımı 6:151'de yer alır; bu nadirlik 17:31'deki korku sözünün belirginliğini artırır (6:151). Qāfın sert kapanışından sonra {ar:نَّحْنُ, tr:nahnu, gloss:biz} ve {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} yeni bir ses vuruşuyla karşılık cümlesini açar.

Karşılıkta bağımsız {ar:نَّحْنُ, tr:nahnu, gloss:biz} öznesi sağlayanı ayrıca öne çıkarır. Fiilin kişi eki de özneyi gösterdiği hâlde açık “biz”, yasağın yöneldiği insan eyleyicilerinden ilahî sağlayana geçişi işittirir. Yararlanılacak bir pay verme anlamındaki {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz}, korkulan tükenişin karşısına doğrudan sağlama sözünü koyar.

Şimdiki-geniş zamanlı {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} adı konmamış nimetleri süren bir verme olarak sunar; belirli bir malı ya da değişmez bir miktarı söylemez. Fiile eklenen -hum çocukları ilk alıcılar olarak gösterir. Ardından gelen {ar:وَإِيَّاكُمْ, tr:ve iyyâkum, gloss:ve size de} ebeveynleri aynı fiilin ikinci alıcı grubu olarak ekler. Waw iki grubu ortak yükleme bağlar, sıralarını ise değiştirmez; ayrık iyyâkum ebeveynleri ayrıca vurgular ama çocukların önüne almaz. -hum ile -kum'daki mîm, waw'ın ayırdığı kısa aralıkta yeniden duyularak bu sırayı ses düzeyinde de tutar.

Bu alıcı sırası ilk buyruğa geri bağlanır: yasakta öldürme nesnesi olan çocuklar, sağlama cümlesinde -hum ekiyle rızık alanlara dönüşür. {ar:أَوْلَٰدَكُمْ, tr:evlâdekum, gloss:çocuklarınız} ile {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} arasındaki yakın gönderim, çocukların korunmasını ebeveynlerin de yer aldığı ortak pay ilişkisinin içinde tutar. Bu ilişki sağlanan nimetin biçimini ve miktarını açık bırakır.

## Hükmün Ağırlığı

Sağlama sözünün ardından gelen {ar:إِنَّ, tr:inne, gloss:şüphesiz}, bütün öldürme hükmünü vurgular. Buyruktaki {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} kapanışta {ar:قَتْلَهُمْ, tr:qatlahum, gloss:onların öldürülmesi} adıyla yinelenir; yasaklanan eylem böylece yargılanan konuya dönüşür. -hum öldürülen çocuklara döner, öldürenlere değil. Öldürme kökünün uzak bir kullanımında canlıdaki yaşam gücü de bulunur; bu yankı, sözcüğün fiziksel ölüm anlamını korurken yaşayan çocuğun hayat kuvvetinin söndürülmesini de duyurur.

Söz diziminde {ar:قَتْلَهُمْ, tr:qatlahum, gloss:onların öldürülmesi}, inne yapısının ismidir; ardından gelen {ar:كَانَ, tr:kâne, gloss:olma hâli bildiren fiil}in gizli öznesi yine bu öldürme eylemidir. {ar:خِطْـًۭٔا, tr:khiṭ'en, gloss:yanlış} onun haberini, {ar:كَبِيرًۭا, tr:kebîran, gloss:büyük} ise haberi niteleyen sıfatı kurar. Kâne bu eylemi geçip gitmiş tekil bir olaydan ziyade yerleşik bir hüküm olarak bildirir.

{ar:خِطْـًۭٔا, tr:khiṭ'en, gloss:yanlış}ın olağan alanı hata ve yanlışlıktır. Yasaklanmış {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} eylemiyle buluştuğunda sözcük bilerek yasak olana yönelme ve günah işleme anlamını da taşır; bu kol sorumluluğu eyleyene bağlar. Sözcüğün amaçlanan sonuca ulaşamama yönü de ayrı bir katkı sunar: yoksulluktan korunma hedefi ile çocuğun hayatını sona erdiren eylem karşılaşınca kaçırılan hedef öldürme niyeti değil, yoksulluk tahminidir. Böylece hedefi şaşırma sonucu, kasıtlı öldürme sorumluluğuyla birlikte okunur. Aktarılan okuyuşlar hata ile sınır aşımı arasındaki vurguyu açık tutar; ortak hüküm öldürmenin ağırlığıdır.

{ar:كَبِيرًۭا, tr:kebîran, gloss:büyük} sıfatı {ar:خِطْـًۭٔا, tr:khiṭ'en, gloss:yanlış} ile belirsiz, nasb sonlu biçimlerde uyuşur; bu uyum onu serbest bir zarftan çok hükmün niteliği yapar. Buradaki büyüklük bedensel ölçü değil, ahlaki ağırlıktır: öldürmeyi sıradan bir kusurdan ayıran ağır günah hükmünü vurgular, günahları kendi arasında sıralamaz. Kapanışın sesi de bu inişi taşır. {ar:قَتْلَهُمْ, tr:qatlahum, gloss:onların öldürülmesi} adından sonraki hemze kısa bir gırtlak kesintisi yaratır; {ar:خِطْـًۭٔا, tr:khiṭ'en, gloss:yanlış} ile {ar:كَبِيرًۭا, tr:kebîran, gloss:büyük} arasındaki uyumlu sonlar ve son sözcüğün kapanıştaki yeri, buyruğun sorumlu tutan yargıya dönüşmesini seslendirir.

Bu yargı, ekonomik korku ile bugünde gerçekleşen ölüm arasındaki zaman farkını keskinleştirir. {ar:خَشْيَةَ إِمْلَٰقٍۢ, tr:haşyete imlâkin, gloss:yoksulluk korkusu} geleceğe dönük beklentiyi, {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} geri döndürülemez fiziksel eylemi adlandırır. Çocukların da ebeveynlerin de aynı rızık fiilinin alıcısı olması, beklenen yoksulluğu çocuğun yaşayıp yaşamayacağına karar veren bir hesaba çevirmeye karşı başka bir okuma açar: korkulan gelecek bugünden ölüme dönüştürülür. Bu okuma zaman karşıtlığını belirginleştirirken fiilen yoksulluk yaşanıp yaşanmadığını açık bırakır; öldürme eylemi fiziksel anlamında kalır.

Tükeniş korkusuyla verilen karar kendi içinde yıkıcı bir karşılık üretebilir. {ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} eldekinin tükenmesini anlatırken {ar:أَوْلَٰدَكُمْ, tr:evlâdekum, gloss:çocuklarınız} ana babanın içinden doğan çocukları adlandırır; hane korktuğu kaybı önlemeye çalışırken kendi geleceğini feda edilen şeye çevirebilir. Bu olası sorumluluk okuması, öldürme anının yanı sıra çocuğu ölüme açık bırakan yıkıcı tercihi kapsar; yoksulluğun her durumda kişinin kendisinden kaynaklandığını ileri sürmez. {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} ise denetlenemeyen gelecekle yıkıcı olmayan bir ilişki açar; güvence bu ilişkinin yönündedir, belirli bir sonucun garantisinde değil.

## Kuru Zemin, Yağmur

{ar:خَشْيَةَ, tr:haşyete, gloss:korku} kökünün kuru et gibi kuruyup sertleşmiş maddeyi de adlandıran uzak kolu, korku anlamına kuruma ve sertlik duyusu ekler. Bu dokunsal yankı, korkulan {ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} ile temasında belirir; odaktaki sözcüğün olağan anlamı yine korku ve ürpermedir.

İmlâk kökünün taş ya da toprak için kullanılan uzak kolu, sıyrılıp düzleşmiş, iz tutmayan yüzeyi belirtir. Bu kol imgeye çıplaklık ve izsizlik katar; {ar:خَشْيَةَ, tr:haşyete, gloss:korku} kökünün kuru madde yankısı ise kuruluk ve sertlik verir. İki ayrı sözlük kolu birlikte korkulan tükenişi dokunsal bir zeminde duyurur. Odakta kalan anlam yoksulluk korkusudur; yüzey çağrışımı bu korkunun imgesel dokusunu açar.

Bu zemine, {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} fiilinin olağan anlamı olan yararlı pay sağlama katılır. Rızık kökünün uzak yağmur ya da yağmur suyu kullanımı bu paya hayat taşıyan akış yönü ekler; böylece çıplak zemin karşısında besleyici bir katkı belirir, ayetin odağında ise rızık verme kalır. Ardından {ar:خِطْـًۭٔا, tr:khiṭ'en, gloss:yanlış} kökünün özel arazi bağlamındaki kolu gelir: yağmur başka yere düşer ve belirli bir parçayı atlar. Bu dal imgeye mekânsal bir eksiklik katar. Yağmur benzeri sağlama ile o arazinin es geçilmesi yan yana gelince aile, hayat veren akışın uğramadığı yer gibi görünür; bu birleşim imgeseldir ve odaktaki öldürme çocukların gerçek ölümüdür.

## Bakımın ve Kaynağın Zamanı

Rızık payı, çocuğu hanedeki bir gider olmanın ötesinde, bedeni büyüyen bir alıcı olarak görünür kılar. 17:24'te konuşan kişi, kendisi küçükken yetiştirildiğini {ar:رَبَّيَانِى صَغِيرًا, tr:rabbayânî sağîran, gloss:beni küçükken yetiştirdiler} sözüyle anımsar. Bu anı ile 17:31'deki {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} yan yana geldiğinde rızık, çocuğun bedensel olarak beslenip büyütülmesine yaklaşır; iki ayet de yiyeceğin türünü belirtmez (17:24). “Çocuk” anlamındaki {ar:وَلَد, tr:walad, gloss:çocuk} sözcüğünün dar sözlük kolu erkek yeni doğanı ya da ergenlik öncesi oğlanı da kapsayabilir; 17:24'teki yetiştirilme anısıyla birlikte bu yaşça küçük anlam bağımlılığı belirginleştirir (17:24). 17:31'deki çoğul ise çocukların cinsiyetini ya da yaşını ayrıca tayin etmez.

17:24'teki geçmiş bakım, bakışı 17:23'teki yetişkin çocuğa ve yaşlanan ebeveyne doğru genişletir: yetişkin çocukların {ar:بِٱلْوَٰلِدَيْنِ, tr:bi-l-vâlideyn, gloss:anne babaya} iyiliği anne ve babayı birlikte gözetir; {ar:ٱلْكِبَرِ, tr:el-kiber, gloss:yaşlılık} ömrün ileri ucunu adlandırır (17:23). Küçükken yetiştirilme ise hem bedeni besleyip büyütmeyi hem de zaman içinde süren koruyucu bakımı düşündürür (17:24). Bu iki yön, 17:31'deki çocuk sözünü kuşaklar boyunca süren bir bakım ilişkisine yerleştirir. Bu yankı ekonomik karşılık vaadi ya da öldürme yasağının gerekçesi değildir; bakımın zamana yayılan niteliğini gösterirken gerçek darlık ihtimalini açık bırakır (17:23, 17:24).

Bakımın zaman içindeki ilişkisi, kaynakların hangi hak sahiplerine ulaştığı sorusuna açılır. 17:26 yakına, yoksula ve yolda kalmışa haklarının verilmesini, savurganlıktan kaçınmayı söyler; {ar:حَقَّهُۥ, tr:haqqahu, gloss:hakkını} bir kimseye ait alacağı belirtir (17:26). 17:31'de çocukların da rızık alıcısı olması, haklı payın yalnız ev halkının özel fazlası sayılamayacağını düşündürür. 17:26'daki {ar:تُبَذِّرْ تَبْذِيرًا, tr:tubadhdhir tabdhîran, gloss:saçıp savurmak} fiil ve aynı kökten gelen ad sıradan savurganlığı vurgular; odakla birlikte okunduğunda bu vurgu yıkıcı harcamayla haklı dolaşım arasındaki farkı aydınlatır. Bağlantı hak sahipliğini belirginleştirir, belirli bir bölüşüm miktarı koymaz (17:26).

Kaynakları dolaşıma sokmanın iki ucu 17:29'da el imgesiyle belirir: {ar:يَدَكَ, tr:yadaka, gloss:elin} evin ekonomik hareket alanını düşündürürken gerçek el anlamını da korur (17:29). {ar:مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:mağlûleten ilâ unuqik, gloss:boynuna bağlanmış} el kıpırdayamayacak kadar tutmayı, {ar:تَبْسُطْهَا كُلَّ ٱلْبَسْطِ, tr:tabsuṭhâ kulla l-basṭ, gloss:elini büsbütün açmayı} ise sınırsız harcamayı gösterir (17:29). Sonuçtaki {ar:مَّحْسُورًا, tr:maḥsûran, gloss:tükenmiş} kaynakların bitip kişinin tükenmesine varan noktayı açar (17:29). Bu iki uçla birlikte 17:31 okunduğunda, hane hesabının bir alıcıyı ortadan kaldırarak kaynakları dengelemesi mümkün bir çözüm gibi görünmez.

17:30, 17:29'un iki el hareketine başka bir ölçü ekler: rızık bazen genişletilir, bazen daraltılır (17:30). {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} artış ve bolluğu da kapsar; {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçüsüne koyar ve kısar} ölçü belirlemeyi ve payın kısılmasını birlikte taşır (17:30). Bu değişkenlik, 17:31'deki daralma korkusunu gerçek bir ihtimal olarak tutar; öldürmeye izin vermez (17:30, 17:31). 17:30'daki ölçme anlamı, 17:29'un iki el ucu arasında uygun oran fikrini çağrıştırabilir; bu, sayısal bir orta nokta değil, ölçülü sorumluluk okumasıdır (17:29, 17:30). Rızkın değişkenliği eşit pay ya da belirli miktar belirlemez ve bolluğu garanti etmez (17:30).

17:30'un sonundaki {ar:خَبِيرًا, tr:khabîran, gloss:iç durumları bilen} haberden ve sınanmış iç bilgiden haberdar oluşu, {ar:بَصِيرًا, tr:basîran, gloss:gören} ise görmeyi belirtir (17:30). Sağlayanın bilmesi ve görmesi, 17:31'de çocuklarla ebeveynlerin ayrı ayrı adlandırılmasıyla birleşince rızkı adsız bir stoktan ziyade bu alıcıları gözeten bir pay olarak düşündürür (17:30, 17:31). 17:24'ün bakım anısı, 17:26'nın hak sınırı, 17:29'un harcama uçları ve 17:30'un değişkenliği bu okumanın farklı dayanaklarıdır (17:24, 17:26, 17:29, 17:30). Birlikte alıcıya dönük dikkati desteklerler; kesin dağıtım biçimi ise açık kalır.

Çocukların payına düşen hayat da sınırsız hane yetkisi içinde düşünülemez. 17:33, {ar:ٱلنَّفْسَ ٱلَّتِى حَرَّمَ ٱللَّهُ, tr:en-nefse’lletî harramallâh, gloss:Allah'ın dokunulmaz kıldığı can}ı ancak {ar:بِٱلْحَقِّ, tr:bi-l-haqq, gloss:haklı bir neden} bulunduğunda istisna eder; öldürülen kişinin {ar:وَلِيِّهِۦ, tr:veliyyihi, gloss:velisi} için {ar:سُلْطَٰنًا, tr:sulṭânen, gloss:yetki} tanır ve {ar:فَلَا يُسْرِفْ فِى ٱلْقَتْلِ, tr:fe-lâ yusrif fi-l-qatl, gloss:öldürmede aşırı gitmeme} sınırını koyar (17:33). Bu paralellik, korunan hayatı ve sınırlı yetkiyi belirginleştirir; ebeveynin aile içindeki konumu da can üzerinde sınırsız özel tasarruf sağlamaz. Karşılaştırma yetki sınırında kalır: 17:33'ün veliye tanıdığı yetki ve karşılık hukuku, 17:31'deki öldürmeme yasağından ayrı bir hukuki konudur.

Hukuki yetki sınırı, çocuğun geleceğine bakınca bakım yükümlülüğü olarak da belirir. 17:34'te {ar:ٱلْيَتِيمِ, tr:el-yetîm, gloss:yetim} koruyucusuz çocuğu özel korumaya alır; odakla temas noktası kırılganlıktır, odaktaki çocukları yetim diye tanımlamak değil (17:34). Aynı ayette koruma, çocuk {ar:حَتَّىٰ يَبْلُغَ أَشُدَّهُۥ, tr:ḥattâ yebluğa eşuddehû, gloss:güç çağına erişinceye dek} sürer; {ar:أَوْفُوا۟, tr:evfû, gloss:eksiksiz yerine getirin} buyruğu hakkı eksiltmeden teslim etmeyi, iki kez gelen {ar:ٱلْعَهْدَ, tr:el-ahd, gloss:yükümlülüğü} ise zaman boyunca tutulan sözü vurgular (17:34). 17:35'teki {ar:وَزِنُوا۟, tr:ve zinû, gloss:tartın} ve {ar:بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:bi-l-qisṭâsi’l-mustaqîm, gloss:doğru teraziyle} kaynak baskısı altındaki adil ölçümü somutlaştırır (17:35). Bu hükümler, bağımlı çocuğun gelecekteki payını koruma okumasını besler; yetim gözetimi ve tartı adaleti kendi konularını korurken 17:31'deki çocuklara yüklenmez (17:31, 17:34, 17:35).

## Beklentiyi Sınamak

Gelecek tahmini kanıtlanmış bilgi gibi kullanıldığında, korku ile bilme arasındaki sınır önem kazanır. {ar:خَشْيَةَ, tr:haşyete, gloss:korku} kökünün aktarmalı bir kullanımı bilmeye yaklaşır; bu anlam, ancak önerme ya da beklenen sonuç gerçekten bilinen bağlamda işler. 17:31'de sözcüğün olağan anlamı öldürme yasağının gerekçesi olan korkudur. {ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} beklentisi, öldürme kökünün bir şeyi bütünüyle kavrayıp kesin olarak bilme yönüyle yan yana geldiğinde, kaygının kesinlik gibi işletilmesini düşündürür. Bu iki uzak anlam, geleceğin erkenden kapanmış sayılması okumasına katkı verir; odakta korku ve fiziksel öldürme kalır, yoksulluk tahmini kanıtlanmış bilgiye dönüşmez.

17:25'te Rabbin insanların içindekini bildiğinin söylenmesi, 17:36'daki bilgisizce peşine düşmeme uyarısıyla birlikte tahmine bir kanıt sınırı getirir (17:25, 17:36). 17:36'daki {ar:تَقْفُ, tr:taqfû, gloss:izini sürmek} iz sürme imgesini {ar:عِلْمٌ, tr:ilm, gloss:bilgi} koşuluna bağlar; aynı ayette hesabı sorulacak {ar:ٱلْفُؤَادَ, tr:el-fuâd, gloss:yürek} içsel yönelişi de sorumluluk alanına alır (17:36). Bu bağlamda uyarı, 17:31'deki korkuyla yapılacak eylemin önüne bilgi sınaması getirir; odak ayetin kendi açıklamasından değil, komşu uyarının uygulanışından doğan bir okumadır (17:31, 17:36). Gerçek yoksulluk ihtimali sürer, fakat korku tek başına onu kanıtlamaz.

Bilginin sınırına insanın erişemediği yerler de eşlik eder. 17:37'de insanın yeri dele geçememesi ve dağlara boyca erişememesi, hane hesabının hayat ve gelecek üzerindeki denetim sınırını iki somut ölçekte gösterir: {ar:تَخْرِقَ ٱلْأَرْضَ, tr:takhriqa’l-arḍ, gloss:yeri delip geçmek} ve {ar:تَبْلُغَ ٱلْجِبَالَ طُولًا, tr:tablugh al-jibâla ṭûlan, gloss:dağlara boyca erişmek} (17:37). Aynı ayetteki {ar:مَرَحًا, tr:maraḥan, gloss:böbürlenerek} kibir uyarısı, {ar:كَبِيرًۭا, tr:kebîran, gloss:büyük} kökünün uzak ululuk ve üstünlük tınısıyla yan yana duyulabilir. Bu yakınlık ağır günah hükmüne aşırı denetim kurma ihtimalini ekler; çağrışım olası bir taşkınlık tonuyla sınırlıdır, ebeveynlerin saikini tanımlamaz (17:31, 17:37).

17:39'daki başka bir ilah edinmeme sınırı, insan ölçüsünün teolojik ufkunu belirler (17:39). Odaktaki ilahî rızık ile insanın öldürme eylemi, hayat ve pay üzerinde son sözün kimde olduğu sorusunu açar; 17:39 ise Allah'la birlikte başka bir ilah tanımama hükmüdür (17:31, 17:39). Bu paralellik ebeveynlere inanç isnadı değil, ilahî sağlayış ile insan eyleyiciliği arasındaki yetki sınırına ilişkin yapısal bir karşılaştırmadır; 17:39'un ibadet hükmü ile 17:31'in öldürme yasağı kendi konularında kalır.

## Korkunun Muhatapları

Yoksulluk korkusunun yanında yardım arayışı da düşünülebilir. Fâtiha'daki {ar:إِيَّاكَ نَسْتَعِينُ, tr:iyyâke nestaîn, gloss:yalnız senden yardım isteriz} sözü açık bir yardım talebidir (1:5). Bu yöneliş, 17:31'deki {ar:خَشْيَةَ, tr:haşyete, gloss:korku} taşıyıcısına Allah'a dönme boyutunu, {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz} sözüne de aile ihtiyacını yardım ilişkisi içinde duyma imkânını ekler (1:5, 17:31). Fâtiha'daki talep genel yardımdır; maddi rızkı adlandırmaz ve 17:31'in doğrudan cevabı değildir (1:5). Odak ayet sağlayanı söyler, sağlanan miktarı açık bırakır.

2:268'de şeytan yoksullukla korkuturken Allah bağışlanma ve lütuf vaat eder; bu karşıtlık korkunun ahlaki eylem üzerindeki baskısını görünür kılar (2:268). 17:31'deki {ar:إِمْلَٰقٍۢ, tr:imlâkin, gloss:yoksulluk} tükeniş korkusuyla kurulan temas, yoksulluk tahmini ile ona verilen eylemsel karşılığı birbirinden ayırır: bu yankı korkunun karar üzerindeki baskısına ilişkindir, iki ayet aynı çocuk öldürme olayını anlatmaz (2:268, 17:31).

6:140, Allah'ın verdiği rızkı yasaklamayı çocuk öldürme ve bilgisizlik içindeki savruklukla yan yana getirir (6:140). Bu sahne, 17:31'deki {ar:نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:nahnu narzuquhum ve iyyâkum, gloss:onlara da size de rızık veririz} güvencesiyle birlikte, koruma niyetinin geleceği yanlış ölçerek kayba dönüşebileceği ihtimalini açar (6:140, 17:31). Buradaki hedef şaşması yoksulluk tahmininin yanılabilirliğini gösterir; öldürme ise kasıtlı yasak ve büyük günah olarak kalır. Bu karşılaştırma 6:140'ı 17:31'deki aynı aile olayına dönüştürmez (6:140, 17:31).

Sure içindeki başka bir korku, tekil aile kaygısını daha geniş bir elde tutma örüntüsüne bağlar. 17:100'de rahmet hazinelerine sahip olunduğu varsayımında bile harcama korkusu ve elde tutma görülür (17:100). Odaktaki {ar:خَشْيَةَ إِمْلَٰقٍۢ, tr:haşyete imlâkin, gloss:yoksulluk korkusu} ile oradaki {ar:خَشْيَةَ الْإِنفَاقِ, tr:haşyete’l-infâq, gloss:harcama korkusu} aynı korku sözcüğünü farklı nesnelere bağlar: 17:31'de korku çocukların hayatını sona erdiren eylemin gerekçesi, 17:100'de harcamayı tutma eğilimidir (17:31, 17:100). Bu karşılaştırma, kıtlık korkusu ile elde tutma arasında sure içi bir yankı kurar ve korkunun hayal edilen bollukta da sürebildiğini gösterir (17:100). 17:100 varsayımsal bir sahne ve farklı bir faildir; 17:31'de fiilî yoksulluk yaşandığını ya da iki ayetin aynı maddi koşulları anlattığını göstermez (17:31, 17:100). Bu yüzden katkısı, odaktaki yoksulluk korkusunu yaşanmış yokluk değil, geleceği şimdiden kapatan tahmin olarak duyurmaktır; çocukları öldürmeme buyruğu ve rızık güvencesi bu tahmine karşı durur (17:31).

6:151 aynı yoksulluk sözcüğünü çocukları öldürmeme buyruğunda {ar:مِنْ إِمْلَٰقٍ, tr:min imlâqin, gloss:yoksulluk bağlamında} yüzeyiyle kullanır (6:151). Bu biçim, 17:31'de korkulan yoksulluk ile 6:151'de yoksulluk içindeki durumu karşılaştırmaya açar; kapsam, görünen biçimler arasındaki temasla sınırlıdır, ayrıntılı gramer sonucu çıkaracak hedef çözümleme yoktur (6:151, 17:31). Her iki ayette de çocukları koruma buyruğuna rızık güvencesi eşlik eder: odakta {ar:نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:narzuquhum ve iyyâkum, gloss:onlara da size de rızık veririz}, 6:151'de {ar:نَحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ, tr:nahnu narzuqukum ve iyyâhum, gloss:biz size ve onlara rızık veririz} denir (6:151, 17:31). Alıcıların sırasının tersine dönmesi karşılaştırmanın ikinci dayanağıdır; benzerlik aynı aile olayı ya da aynı maddi koşullar anlamına gelmez.

4:9, geride zayıf soy kalması ihtimalini Allah'a karşı sorumluluk ve doğru sözle birlikte anarak gelecek bağımlılığına başka bir açıdan bakar (4:9). 17:31'de korku yoksulluk gerekçesine ve doğrudan koruma buyruğuna bağlanırken, 4:9'daki zayıf torun imgesi bakımın geleceğe uzanan sonucunu öne çıkarır (4:9, 17:31). Çocukları adlandıran biçimlerin morfolojisi ortak kök bağı kurmaya yetmez; ayrıca iki ayetin çocukları ayrı gönderimlerdir. Bu nedenle temas sözcük akrabalığında değil, korku, kırılgan soy ve sorumlu davranış arasındaki ilişkidedir. 4:9'un katkısı bu gelecek bağımlılığını sorumlulukla birlikte göstermektir; yoksulluk ve çocuk öldürme ise 17:31'in odağında kalır (4:9, 17:31).

Son olarak, çocukların hayatını sona erdiren {ar:تَقْتُلُوٓا۟, tr:taqtulû, gloss:öldürmek} eylemi kurbanın açısından da işitilir. 81:8'de diri gömülen kızın ortaya getirilişi ve 81:9'da hangi suçtan öldürüldüğünün sorulması, odağa hayatı alınan çocuğun kendi ölümünün hesabının görüldüğü bakışı ekler (81:8, 81:9). Bu kurban-yönlü katkı, 17:31'deki çocukların cinsiyetini ya da iki ayetin tarihsel olaylarının özdeşliğini belirlemez; değişen, öldürülenin konumudur (17:31, 81:8, 81:9).

</source_prose>
