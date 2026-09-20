# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:28**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.middle.claims.json`

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
- Refer to source paragraphs as `17:28 ¶N`.

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

`(17:28 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:28",
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
        "citation": "(17:28 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_28/17_28.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_28/17_28.middle.claims.json \
  --ayah-ref 17:28
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_28/17_28.prose.editorial.tr.md`

<source_prose>
## Koşuldan cevaba

17:27'deki buyrukların ardından gelen 17:28, {ar:وَ, tr:wa, gloss:ve} ile önceki akışa bağlanır ve {ar:إِمَّا, tr:immā, gloss:eğer, her ne zaman} ile yeni bir şart açar (17:27). Tekil muhatap, onlardan yüz çevirme hareketini Rabbinden bir rahmeti arama ve onu umma koşuluna bağlar; ardından aynı kişilere kolay bir söz söylemesi istenir. Böylece cümle yüz çevirmekten arayışa, arayıştan umuda, umuttan hemen verilecek karşılığa ilerler. İmmā'nın vurgulu muzari fiilden önce gelişi şartı öne çıkarır; fiil de söz diziminin odağında kalır. Koşul, soyut bir ihtimalden çok yeniden karşılaşılabilecek gerçek bir durumu açar. İmmā'daki burunlu m sesi {ar:عَنْهُمُ, tr:ʿanhumu, gloss:onlardan} ve {ar:مِّن, tr:min, gloss:-den} çevresinde yeniden işitilir; ses, şarttan muhataba ve rahmetin kaynağına uzanan cümleyi birbirine bağlar.

Şartın merkezindeki {ar:تُعْرِضَنَّ, tr:tuʿriḍanna, gloss:yüz çevirirsen} ikinci tekil eril muhataba yönelen, vurgulu bir muzari fiildir. IV. kalıptaki bu çekim burada yönelişi geri çekip yüz çevirmek demektir; aynı söz ailesindeki sergileme ve genişletme kullanımları bu anlama taşınmaz. Ardından gelen {ar:عَنْهُمُ, tr:ʿanhumu, gloss:onlardan}, ʿan edatını çoğul zamirle birleştirerek uzaklaşılan kişileri gösterir. Yanını dönme imgesi geri çekilişi bedensel olarak görünür kılar; ayet duruşu, küçümsemeyi ya da dolaylı konuşmayı ayrıca belirlemez.

Bu hareketin amacı {ar:ٱبْتِغَآءَ, tr:ibtighāʾa, gloss:arama} mastarıyla belirtilir: VIII. kalıptan gelen bu mansup biçim arama, peşine düşme eylemini adlandırır ve yüz çevirme fiilinden sonra amaç olarak gelir. Aynı söz ailesinde taşkınlık anlamı bulunsa da burada aranan nesne {ar:رَحْمَةٍ مِّن رَّبِّكَ, tr:raḥmatin min rabbika, gloss:Rabbinden bir rahmet}, kaynağı da Rabbindir. Nesneyle kaynak, arayışın yönünü bir iyiliğe sabitler. Amaç ifadesinin geri çekiliş ile cevap buyruğu arasında yer alması, hareketi rahmeti arayan ve söylenecek söze varan gerekçeli bir ara hâl olarak kurar; bu bağlantı yüz çevirmeyi tek başına kalıcı terk edişe dönüştürmez.

Aranan iyilik {ar:رَحْمَةٍ, tr:raḥmatin, gloss:bir rahmet} diye adlandırılır. Belirsiz ve müennes isim, ibtighāʾa ile kurduğu tamlamada aranan nesnedir; sonraki {ar:تَرْجُوهَا, tr:tarjūhā, gloss:onu umarsın} fiilindeki dişil hā da aynı rahmeti yeniden cümleye alır. Tanvin yardımın türünü açık bırakır. Merhamet ve esirgemeden doğan rahmet, ilahi kullanımda yaratılmışlara ulaşan koruma ve iyilik etme yönü taşır; arayış, kaynak ve umut birlikte bu etkin bakım boyutunu öne çıkarır. Cümle yardımın biçimini ve geliş vaktini belirlemez.

Rahmetin kaynağı {ar:مِّن, tr:min, gloss:-den, kaynağından} edatıyla Rabbe bağlanır. Min hem “Rabden” geliş yönünü hem “Rabden bir pay” düşüncesini açık tutar; her iki işitilişte de kaynak, konuşanın o andaki elindeki imkândan ayrıdır. {ar:رَّبِّكَ, tr:rabbika, gloss:Rabbin} unvanındaki iyelik eki bu kaynağı tekil muhatabın Rabbi olarak belirler. Sahiplik, yetki ve yönetme çağrışımları min'in kaynak ilişkisiyle buluşunca gözeten, geçimi sürdüren bir kaynak duyulur; min rabbika söylenişinde min'in sonundaki n'nin r'ye katılması da bu bağı ses içinde taşır. Rabb unvanıyla ilişkili yetiştirme ve tamamlama kolu bu kaynak imgesine ayrı bir gelişme yankısı ekler; burada temel anlam yine Rab unvanıdır.

Ardından gelen {ar:تَرْجُوهَا, tr:tarjūhā, gloss:onu umarsın} ikinci tekil muhatabı özne yapar; fiilin sonundaki dişil hā, umulan nesne olarak rahmeti gösterir. Muzari çekimin olumlu anlamı, iyi bir sonucun gerçekleşmesini umutla beklemektir: rahmet umut ufkunda kalır, henüz elde edilmiş sayılmaz. Fiil vakti ve sonucu açık bırakır. Şarttan sonra gelen emir ise bekleyiş sürerken verilebilecek karşılığı şimdiye taşır.

## Aynı muhataba yönelen söz

Umut cümlesinin ardından {ar:فَ, tr:fa, gloss:öyleyse, bunun üzerine} şartın cevabını başlatır ve hemen {ar:قُلْ, tr:qul, gloss:söyle} buyruğuna geçer. Fa ile qul hem söz diziminde hem seste tek bir sonuç vuruşu gibi gelir: açıklanan durumun karşılığı gecikmeden söze dökülür. Buyruğun ardından gelen {ar:قَوْلًا مَّيْسُورًا, tr:qawlan maysūran, gloss:kolay bir söz}, söyleme eyleminin nasıl bir ürüne dönüşeceğini bildirir. Bu akış, görünen emir, alıcı ve söz nesnesi arasındaki ilişkiyi belirginleştirir.

Sözün alıcısı {ar:لَّهُمْ, tr:lahum, gloss:onlara} ile hemen gösterilir. Lām edatıyla çoğul hum zamiri, qul buyruğunu aynı kişilere yöneltir. Az önce {ar:عَنْهُمُ, tr:ʿanhumu, gloss:onlardan} içindeki hum uzaklaşma yönünü tutarken, lām şimdi yönü onlara çevirir: hareket onlardan uzaklaşmaktan onlara seslenmeye döner. Alıcının önce belirtilmesi cevabın odağına aynı kişileri yerleştirir; sözün kendilerine erişip yarar sağlaması beklenen karşılıktır. Bu yöneliş alıcıyı belirler, maddi aktarımın miktarını ya da vaadini değil.

{ar:قَوْلًا, tr:qawlan, gloss:bir söz} belirsiz mansup mastar olarak qul emrinin söz ürününü adlandırır. Aynı söz ailesindeki emirden isimle belirtilen ürüne geçiş, konuşma eylemini duyulur bir ifadeye dönüştürür; belirsiz biçim de ezberlenecek hazır bir kalıp dayatmaz. Sözü niteleyen {ar:مَّيْسُورًا, tr:maysūran, gloss:kolay} edilgen ortaç, güçlüğün karşıtı olan kolaylığı doğrudan qawlan'a bağlar. Buradaki kolaylık, muhataba erişebilir söyleyiştir; bolluk anlamı maysūran'ın ayrı söz kolunda yer alır. Qawlan'ın tanvinli inişini maysūran'ın m başlangıcı ve uzun ū'su izler; bu kadans, anlamı da söyleyişi de kolaylaştırılmış söz üzerinde kapanır.

Bu yüz çevirme ile sözün yeniden alıcıya yönelmesi, yakın ebeveyn hitabının ayrı görgü sahnesiyle karşılaştırılabilir. 17:23'te ebeveynlere {ar:وَقُل لَّهُمَا قَوْلًا كَرِيمًا, tr:wa-qul lahumā qawlan karīman, gloss:onlara onurlu bir söz söyle} denir ve {ar:وَلَا تَنْهَرْهُمَا, tr:wa-lā tanharhumā, gloss:onları azarlayıp itme} buyruğuyla sertçe azarlama engellenir (17:23). 17:24'te ise {ar:جَنَاحَ ٱلذُّلِّ, tr:janāḥa al-dhull, gloss:alçakgönüllülük kanadı} imgesi bedeni alçaltıp sığınak açan bir yöneliş kurar; {ar:مِنَ ٱلرَّحْمَةِ, tr:min ar-raḥmati, gloss:merhametten} doğan dua bu hareketi merhamete bağlar (17:24). Bu eğilen bedenin karşısında 17:28'deki {ar:تُعْرِضَنَّ عَنْهُمُ, tr:tuʿriḍanna ʿanhumu, gloss:onlardan yüz çevirme} ve rahmet arayışıyla sınırlanan geri çekiliş, aynı kişilere yönelen {ar:قَوْلًا مَّيْسُورًا, tr:qawlan maysūran, gloss:kolay bir söz} ile ilişkisel bir karşı jest kazanır: beden uzaklaşsa da söz muhatabı ilişkinin içinde tutabilir. Bu karşılaştırmada 17:23'teki karīman onurlu söyleyişi, 17:28'deki maysūran erişilebilir söyleyişi belirler; beden imgeleri de ayrı ayetlerin kendi yönelişlerinde kalır.

17:25'te Rabbin insanların içindekini bildiği, iyilik üzere olanlar ve sık sık yönelenler için bağışlayıcı olduğu söylenir; {ar:رَّبُّكُمْ أَعْلَمُ بِمَا فِى نُفُوسِكُمْ, tr:rabbukum aʿlamu bimā fī nufūsikum, gloss:Rabbiniz içinizde olanı daha iyi bilir}, {ar:صَٰلِحِينَ, tr:ṣāliḥīn, gloss:iyilik üzere olanlar} ve {ar:لِلْأَوَّٰبِينَ غَفُورًا, tr:lil-awwābīna ghafūrā, gloss:sık sık yönelenlere karşı bağışlayıcı} ifadeleri bu iç yönelişi adlandırır (17:25). Sık sık yönelme motifi odaktaki rahmet arayışına yön bakımından eşlik eder; bedenin yüz çevirdiği koşulda iç yönelişi de duyurur, muhataplara bedenen geri dönmeyi değil. İyilik üzere olma, ilişkiyi onarma ve soğukluğu giderme ihtimaline alan açar; ifade yine iyilik üzere olma niteliğidir. Bu olasılık yüz çevirenin niyetini belirlemez: 17:25 ebeveynlere yönelik olabilir ve 17:28'deki isteği ya da alıcıların kusurunu sınıflandırmaz. 17:28'in kendi dizilişi ise rahmet arayışı, umut ve aynı kişilere söylenecek sözle geçici yetersizliğin kalıcı terk edişe dönüşmeyebileceğini düşündürür.

Bu tekil muhataba yönelmiş emirle ayrı bir dua düzlemi arasında sınırlı bir yakınlık da vardır. Fâtiha 1:5'in çoğul {ar:وَإِيَّاكَ نَسْتَعِينُ, tr:wa-iyyāka nastaʿīn, gloss:Yalnız Senden yardım dileriz} sözü, odaktaki Rabbinden rahmet arama ve onu umma ifadelerinin yanına Allah'a dayanma çerçevesi getirir (1:5). Çoğul dua ile tekil emir ayrı söz edimleridir; bu yakınlık bekleyişe Allah'a dayanma dili ekler, 17:28'in sözünü dua alıntısına ya da rahmeti maddi ödeme ve gelecek yardım güvencesine dönüştürmez.

Umut fiilinin söz ailesinde bir işi sonraya bırakma anlamı taşıyan ayrı bir kullanım bulunur; buradaki {ar:تَرْجُوهَا, tr:tarjūhā, gloss:onu umarsın} ise iyi bir sonucu umutla bekler. Bu iki anlamın ayrılığı, 2:235'te iddet tamamlanmadan nikâh akdi bağlanmamasına rağmen uygun sözün söylenebilmesiyle ve 17:30'da rızkın genişleyip daralmasıyla yan yana düşünüldüğünde, sonuç beklenirken konuşmanın ilişkiyi taşıdığı bir yankı açar (2:235, 17:30). Bu karşılaştırma, erteleme ve bekleme sürecinde sözün mümkün kalmasını odaktaki ilişkiyle buluşturur; 2:235'in hukuki takvimi kendi bağlamındadır, 17:28'deki fiil umut bildirir ve yardımın geleceğini belirlemez.

Sözün muhataba uygun kolaylığı, 3:159'daki yumuşaklığın insanların çevreden dağılmasını önlemesiyle ilişkisel bir etki kazanır (3:159). Bu ayet yumuşaklığın insanları bir arada tutan sonucunu, maysūran'ın ayrı kullanımları ise canlılarda yumuşak başlılık ve yönlendirilmeye çabuk uyumu, daha özelde binek hayvanının hafif ve düzgün adımını ekler. Birlikte bu iki katkı, kolay sözü muhataba uyum sağlayan, ilişkiyi sürdürebilen bir karşılık gibi duyurur; odak ayetteki doğrudan anlam yine qawlan'ı niteleyen kolaylıktır.

Bu söz eylemi, maddi karşılığın kısıtlanabildiği başka sahnelerde de anlamını korur. 4:5'te mal idaresine sınır konurken geçim, giysi ve güzel sözün sürmesi, maddi kısıtlamanın bakım ilişkisini tümüyle kesmediğini gösterir; 4:63'te geri çekilmenin ardından aynı kişilere öğüt ve etkili söz yöneltilmesi, konuşmayı mesafeden sonra gelen etkin bir karşılık yapar (4:5, 4:63). Bu iki sahnenin katkıları farklıdır: biri sözlü ve maddi bakımın yan yana sürmesini, diğeri uzaklaşma ardından muhataba yeniden sözle yönelmeyi gösterir. Bu örnekler kendi bağlamlarında kalırken 17:28'deki kolay sözün imkân sınırlıyken ilişkiyi taşıyan gerçek bir edim oluşunu aydınlatır.

17:53'te en güzel sözü söyleme buyruğu, insanlar arasında ayrılık çıkaran şeytan uyarısıyla yan yana gelir (17:53). Bu söz etiği, 17:28'de aynı kişilere yöneltilen {ar:قُلْ, tr:qul, gloss:söyle} emrinin ilişkiyi koruyabilecek yönünü belirginleştirir. Bağlantı, sözün ilişkileri koruma işlevini büyütür; 17:28'in muhataplarını bir çatışmanın tarafı olarak tanımlamaz ve kendi başına yardım vaadi kurmaz.

## İmkân ve bekleyiş

Yakın bağlam hakkı gözetme ile harcama ölçüsünü birlikte kurar: 17:26'da yakınların ve yoksulun hakkı verilir, 17:27'de savurganlık yasaklanır; 17:29'da elin boyna bağlanmasıyla bütünüyle açılması iki sınır imgesi kurar; 17:30'da rızkın genişleyip daralması imkânın değişkenliğini ekler (17:26, 17:27, 17:29, 17:30). Bu sırada 17:28'in {ar:قَوْلًا مَّيْسُورًا, tr:qawlan maysūran, gloss:kolay bir söz} buyruğu, alıcının hakkı sürerken o andaki aktarımın ölçülebileceği aralıkta sözlü karşılığı öne çıkarır. Aranan Rab rahmeti 17:26'daki {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:onun hakkı}nı isteğe bağlı hayra dönüştürmez; arayışın nesnesi Rabbin rahmetidir, alıcı adına ödeme çabası değil. Bağlam ölçülü kısıtlamaya yer açar, fakat bunun nedenini ya da konuşanın imkânının yetip yetmediğini belirtmez.

17:30'da rızkın genişletilmesi, rahmetin aranıp umut edilmesiyle yan yana geldiğinde ileride kapasitenin artmasını bir ihtimal olarak açar (17:30). Aynı ayetteki {ar:وَيَقْدِرُ, tr:wa-yaqdiru, gloss:daraltır, ölçülü verir}, rızkın daraltılıp paylaştırılmasını anlatır; böylece ayet hem genişleme ihtimalini hem mevcut payın ölçülülüğünü gösterir, alıcının yeri ya da konuşanın elindeki miktar hakkında hüküm vermez. 17:29'daki {ar:يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:yadaka maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlanmış tutmak} imgesi, elde tutmanın kalıcı kapanmaya dönüşme tehlikesini görünür kılar; 17:30'daki değişken rızık ise bu duraklamanın değişmez alıkoyma olmadığını düşündürür (17:29, 17:30). Maysūran'ın ayrı varlık ve bolluk anlamı rızık bağlamında kaynaklara dair yankı açarken, odaktaki dilbilgisi sözcüğü qawlan'a bağlar: burada nitelenen söz kolay ve erişilebilirdir. Bu kaynak yankısı zenginlik ya da ilerideki ödeme hakkında güvence vermez. Elin kapalı ve açık imgeleri yönü gösterir ama miktar kotası koymaz; ölçülülük ihtiyacı gözetirken eldekinin tamamını tüketmeyi şart koşmaz.

17:31'de yoksulluk korkusuyla çocukların öldürülmesine ilişkin ağır uyarı, eli boş kalma düşüncesini paylaştırılmış rızıkla birlikte ele alır (17:31). Bu sahne, 17:28'deki yüz çevirme ve zorunlu sözün toplumsal ağırlığını daha büyük bir şiddet ölçeğinde görünür kılar: maddi darlık muhtaç kişiyi muhataplıktan çıkarma riskini taşırken odaktaki söz onu dinlenen ve ilişki içinde kalan biri olarak tutar. Bağlantı ölçekler arası bir benzetmedir; para vermemeyi çocuk öldürmeyle eşitlemez, sahnelerin kişilerini ve saiklerini birleştirmez. 17:28 konuşanın eli boş olduğunu söylemediği için ihtiyatlı tasarruf olasılığı açıktır; fiilî imkânsızlık ise belirtilmez.

Bu koşul ve cevap dizilişi, maddi eylem beklerken ilişkiyi açık tutan bir aralık gibi duyulur. İbtighāʾa'daki süren arayış rahmeti hedefte, tarjūhā'daki umut ise onu henüz gelecekte tutar; geri çekiliş böylece devam eden çabanın içinde yer alır. Rahmetin koruma ve iyilik etme yönü bekleyişe özen katar; hemen ardından gelen qul buyruğu ve qawlan maysūran bu aralıkta şimdi yapılabilen, sese dökülmüş karşılığı verir. Kolaylaştırılmış söyleyiş muhataba geçişi hafifletip sonucu beklerken ilişkiyi taşır. Bu okuma aralığın niteliğini açıklar; yardımın geleceği, kapasitenin artacağı ve kullanılacak tam ifade ise belirlenmiş değildir.

Bekleyişe geleceğe dönük bir güvence eklenecekse, 17:34, 17:35 ve 17:36'daki sorumluluk ve bilgi ölçüleri o sözü biçimlendirir. 17:34 ahde bağlı kalmayı ister (17:34), 17:35 tam ölçüyü ve dosdoğru tartıyı buyurur (17:35); bu ilkeler teselliyi konuşanın yerine getirebileceği ve adilce ölçebileceği söz olarak kurar. 17:36 bilinmeyenin peşine düşmemeyi buyurur (17:36), dolayısıyla gelecek hakkında söylenen de bilgi sınırında kalır. Kolay sözün şefkati iyimserliği büyütmekten değil, doğruluğu ve ölçüyü korumaktan gelir; nezaket vaat içermeden de mümkündür. Bu özel koşullu cevap yardım sözü vermez.

## Umudun açtığı imgeler

Rahmetin bekleyişle ilişkisi, Fâtiha 1:3'teki {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:al-Raḥmān al-Raḥīm, gloss:Rahmân ve Rahîm} adlarıyla ve 18:82'deki {ar:رَحْمَةً مِّن رَّبِّكَ, tr:raḥmatan min rabbika, gloss:Rabbinden bir rahmet} ifadesiyle geniş bir yankı kazanır (1:3, 18:82). Fâtiha'daki adlar merhametin niteliğini adlandırır; 18:82'de duvarın iki yetim çocuk erginleşene dek hazineyi koruması, bu niteliğe sonucu zaman içinde gözetilen somut bir yarar ekler (18:82). Birlikte, beklenen iyiliğin gecikmesinin de merhametle bağdaşabileceğini düşündürürler. Rabb unvanıyla ilişkili yetiştirme ve tamamlama kolu bu koruma imgesine gelişme yankısı katar; duvar, hazine ve yetimler ise bu ayrı ayetin somut sahnesi olarak kalır.

Bu yankı, odağın kaynak ve zaman ilişkisini bir gelişme imgesiyle düşünmeye imkân tanır. Rahmet Rabbinden aranır ve henüz umulur; kaynak ilişkisi beklenen iyiliği konuşanın elindeki hazır imkândan ayırır. Rabb unvanıyla ilişkili ayrı yetiştirme ve eksikten tamamlanana doğru geliştirme kolu, bekleyişe zaman içinde beslenen kapasite boyutu ekler. Maysūran'ın ayrı varlık ve bolluk anlamı bu imgeye maddi imkân ölçeği getirirken, odaktaki dilbilgisi sözcüğü kolay söz olarak tutar. Bu kollar birlikte beklenen iyiliğin oluşup erişilebilir hâle gelmesini tasavvur ettirir; bu özel benzetme yoksunluğu saptamaz, zenginlik ya da zaman çizelgesi vaat etmez.

Gelişme imgesinden ayrı bir benzetme, iyiliğin içte taşınıp belirmeye yaklaşmasını düşündürür. Tarjūhā'nın doğrudan anlamı olumlu bir sonucu umutla beklemektir; aynı söz ailesindeki doğuma yaklaşma kullanımı bu bekleyişe belirme eşiği imgesi katar. Rahma merhamet anlamını korurken aynı söz ailesindeki rahim kullanımı oluşumun içte taşınmasını çağrıştırır. {ar:مِّن رَّبِّكَ, tr:min rabbika, gloss:Rabbinden} beklenen iyiliğin kaynağını belirler; Rabb'le ilişkili yetiştirme imgesi ise bu oluşuma gözetim ve gelişme boyutu verir. {ar:مَّيْسُورًا, tr:maysūran, gloss:kolay} kolaylaşan bir açılma noktası ekleyince bu katkılar henüz tamamlanmamış iyiliğin belirmesini tasavvur ettirir. {ar:إِمَّا, tr:immā, gloss:eğer, her ne zaman} koşulu ve umut, bu okumada yüz çevirmenin geçici bir aralık gibi duyulmasını sağlar; geçicilik fiilin biçiminde değil, koşul ile umut arasındaki ilişkidedir. Bu özel imge biyolojik bir olay ya da dışarıdan yardımın reddi iddiası değildir ve belirli bir vade koymaz.

Sonucun vakti ve biçimi açık kaldığında, aynı kolay söz ölçülü ve dolaylı bir söyleyiş ihtimalini taşır. {ar:تُعْرِضَنَّ, tr:tuʿriḍanna, gloss:yüz çevirirsen}deki yana dönme geri çekilişi, {ar:قَوْلًا, tr:qawlan, gloss:bir söz} buyruğu ise söze yönelen karşılığı sağlar; {ar:مَّيْسُورًا, tr:maysūran, gloss:kolay} bu karşılığın muhataba zorluk çıkarmayan, anlayışlı bir biçim almasına alan açar. {ar:تَرْجُوهَا, tr:tarjūhā, gloss:onu umarsın} olumlu bir sonucu beklemeyi sürdürdüğünden rahmetin zamanı ve biçimi açık kalır; böylece ölçülü söyleyiş belirsizliği soğuk bir geri çevirmeye dönüştürmeden taşıyabilir. Bu, olası bir üslup yönüdür, belirli bir cümle reçetesi değil; gelecek hakkında vaat etmeyi ne gerektirir ne de yasaklar.

Sözün ilişki yükünü taşıması ise ayrı, daha küçük bir imgedir. {ar:قُلْ, tr:qul, gloss:söyle} emri eylemi, {ar:قَوْلًا, tr:qawlan, gloss:bir söz} ismi onun ürününü gösterir; {ar:لَهُمْ, tr:lahum, gloss:onlara} alıcıları belirgin tutar ve maysūran sözün onlara erişmesini kolaylaştırır. Söyleme ailesindeki yükü kaldırıp taşıma anlamı bu eylem-alıcı ilişkisine eklenince, düşük maliyetli küçük bir sözün bakım ve gündelik bağın ağırlığını taşıyabileceği duyulur. Yük burada ilişkisel imgedir; maysūran'ın doğrudan anlamı kolaylıktır, kısalık değil. Böylece söz maddi iyiliğin yerini almadan bekleyiş sırasında ilişkiyi ayakta tutan bir karşılık olabilir.

</source_prose>
