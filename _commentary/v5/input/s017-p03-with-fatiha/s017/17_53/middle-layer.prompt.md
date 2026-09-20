# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:53**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.middle.claims.json`

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
- Refer to source paragraphs as `17:53 ¶N`.

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

`(17:53 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:53",
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
        "citation": "(17:53 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_53/17_53.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_53/17_53.middle.claims.json \
  --ayah-ref 17:53
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_53/17_53.prose.editorial.tr.md`

<source_prose>
## Buyruğun İç Yapısı

Başındaki {ar:وَ, tr:wa, gloss:ve} önceki hitabı sürdürür; ardından gelen {ar:قُل, tr:qul, gloss:söyle} Peygamber'e yönelmiş dış buyruğu kurar. Bu buyruğun içinde {ar:لِعِبَادِي, tr:liʿibādī, gloss:kullarıma} yönelen topluluğa {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} denir. Böylece Elçi'ye söyletilen söz, kulların nasıl konuşacağını bildiren ikinci bir talimatı taşır. Sözcüğe bitişik {ar:لِ, tr:li, gloss:-e yönelten edat}, hedef toplulukla ona aktarılan emri sıkı biçimde bağlar. Buradaki {ar:قُل, tr:qul, gloss:söyle} ile {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} sesle söz söyleme fiilleridir; söz ailesinin organ, unvan ya da söylenti anlamındaki ayrı kullanımları bu buyrukların anlam alanına taşınmaz.

Bu hitaptaki {ar:عِبَادِي, tr:ʿibādī, gloss:kullarım}, hizmet ve kullukla birlikte Allah'a yönelmiş boyun eğişi duyurur. Birinci tekil iyelik eki, topluluğu emir kendilerine ulaşmadan önce konuşanın aidiyetinde sunar; ilahî bağlamda güzel söz buyruğu, kulluğun gündelik davranışta görünmesi gibi işitilebilir. Buradaki kulluk ve hizmet alanı konuşma eyleminin çerçevesidir; kendi başına hukuki kölelik ya da ayrıca kurulmuş bir ibadet sahnesi anlatmaz.

Emrin içindeki {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} bir bildirim değil, dıştaki söyleme buyruğuna bağlanan dolaylı talimattır. Biçim, sözü tek bir alıntıyla sınırlamadan yinelenebilir bir pratik olarak sunar; belirli bir konuşma anı ya da sınırsız sıklık tayin etmez. Ardından gelen {ar:ٱلَّتِي, tr:allatī, gloss:ki o / olanı}, söylenecek şeyi veya söyleme tarzını açık bırakır: önünde tek bir açık isim karşılığı yoktur; emir ve konuşma fiili konuşma alanını kurar ama tam olarak hangi sözün ya da tarzın kastedildiğini belirlemez. Aradaki {ar:هِيَ, tr:hiya, gloss:odur} ise gizli bir isme eklenmiş sıfattan çok, “o en güzel olandır” biçiminde açık bir yargı kurar ve yeni bir gönderge getirmez.

Yargının ölçüsü {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} sözüdür. Ölçü zarar vermemeyi de kapsar; ayrıca iyi iş gören, beğenilir ve duruma yakışan bir söz ister. Güzellik, görsel nitelikten konuşmanın iyiliği ve yerindeliğine genişler. Türkçedeki “daha güzel” ve “en güzel” karşılıkları açık kalır; ikisinden biri zorunlu olmadığından ölçü, tek bir hazır kalıptan çok söylenecek şeye uygulanır. Hemen ardından gelen uyarı, bu standardın neden önem taşıdığını ilişki düzeyinde somutlaştırır.

İlk {ar:إِنَّ, tr:inna, gloss:şüphesiz}, standardın yanına vurgulu bir gerekçe getirir: {ar:ٱلشَّيْطَٰنَ, tr:ash-shayṭāna, gloss:Şeytan} insanlar arasında kışkırtma çıkarır. Böylece en güzel sözü söyleme buyruğu, ayette adı konan ilişki tehlikesine verilmiş yerel bir cevap olur. Vurgu, bu yakın bağlantıyı öne çıkarır; gerekçenin kapsamı ayetin kurduğu ilişkiyle sınırlıdır.

İlk uyarıda Şeytan, {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} fiilinin etken failidir; kullar ise {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} ifadesinin taraflarıdır. Böylece fail, ortak ilişkilerinin arasına giren Şeytan; taraflar, kullardır. Fiilin şimdiki/geniş görünüşü iş başındaki ya da yinelenebilen müdahaleyi duyurabilir; eylemin süresi açık bırakılır. Çoğul zamir önce kulları kapsar; ikinci cümlede hedef insanın geneline açılacaktır.

Şeytan adının uzaklıkla ilişkilendirilen köken açıklaması, bu ilk cümlede yerel bir yankı bulur. {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} eylemi ve {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} ilişkisi, insanlar arasındaki bozucu işe uzaklaştırıcı bir gölge eklerken özel adın olağan anlamını korur. Bu bağlantı, ayet içindeki bir yankı olarak kalır; etimoloji kanıtı oluşturmaz.

Söyleme buyruğu, kışkırtmanın ilişkiye nasıl zarar verebileceğini düşündürür. {ar:قُل, tr:qul, gloss:söyle} ve {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} sözü sesle dışa vurur; sözün ağızdan çıkmadan önce seçilmesi burada keşifsel bir eşik açar. {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} ölçütü ve {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} fiilindeki dürtme imgesi, tek tanıklıktaki birini sözle iğneleme kullanımıyla buluşunca, kışkırtmanın dile saplanan olası bir yolunu görünür kılar. Odaktaki fiil bu dar kullanıma indirgenmez; bu bağlantıda iyi sözü seçmek, ilişkiye saplanabilecek söz açık düşmanlığa dönüşmeden onu gözeten bir tutum olarak okunabilir. Ayet belirli bir hakaret ya da konuşan-hedef çifti belirtmez; odağın tamamlayıcısı insanlar arasındaki ilişki olarak kalır.

Bu ilişkinin taşıyıcısı {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında}, iki ya da daha çok taraf arasındaki ortak aralığı gösterir. Sözcük ailesindeki ayrılma ve kopuş kullanımları, kışkırtma ile ardından anılan düşmanlık yan yana geldiğinde, bu ortak alanı parçalanmaya açık bir bağ gibi duyurur. Bu bağlantıda kopuş, edatın temel karşılığı değil; yakın bağlamın açtığı olasılıktır. Ortak aralığın çizgisi, şimdi daha maddi bir bağ imgesine dönüşür.

Uzun, sıkıca bükülmüş ve kuyudan su çekmeye yarayan ip, ilişki çizgisini elle tutulur kılar; aynı ip bağlamak için de kullanılır. {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} taraflar arasındaki çizgiyi taşırken ip, yük ve gerilimi duyurur: çekildikçe bağ gerilebilir, gevşediğinde üzerindeki yük kopuş olmadan azalabilir. {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} bu çizgiye saplanan sözlü iğne imgesine yaklaşır; iyi söz de gerilimi yumuşatıp iğnenin kopuşa dönüşmesini önleyebilecek bir karşılık sunar. Böylece uzaklık yankısına bağın maddi gerilimi eklenir. Bu, adın kökenine ilişkin yeni bir iddia değil, ilişki çizgisi çevresinde kurulan keşifsel bir imgedir.

Kullara seslenişteki {ar:عِبَادِي, tr:ʿibādī, gloss:kullarım} sözcük ailesi, ipten ayrı olarak sık geçişle düzleşip geçilebilir hâle gelen yol imgesini açar. Katranlanmış deve ve kaplanmış gemi örnekleri, aynı ailenin yol düzleme ve yüzeyi kaplama kullanımlarını somutlaştırır. {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} buyruğu ile {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} ölçütü buluştuğunda, iyi söz insanlar arasındaki geçişi açık ve kullanılabilir kılabilir. Yolun tekrarlanan geçişle açılması, ipin ise yükü ve gerilimi taşıması iki ayrı katkıdır; bu yol imgesi kullar adını hukuki sahiplik anlamına genişletmez.

İkinci cümlede {ar:إِنَّ, tr:inna, gloss:şüphesiz} yeniden gelir ve {ar:ٱلشَّيْطَٰنَ, tr:ash-shayṭāna, gloss:Şeytan} adı zamirle geçilmeden tekrarlanır. Fail aynı kalırken soru “aralarında ne yapıyor?”dan “insana karşı nasıl bir konumda?”ya kayar. {ar:كَانَ, tr:kāna, gloss:olagelmiştir} ile {ar:عَدُوًّا, tr:ʿaduwwan, gloss:düşman} düşmanlığı tekil eylemden çok yerleşik bir nitelik olarak kurar; bu yüklem niteliğin süresini, başlangıcını ya da nedenini belirlemez. İki uyarıdaki ad tekrarı, özellikle vurgulu ṭ ve uzun â sesleriyle işitsel bir ısrar oluşturabilir. Bu etki okuma izlenimi düzeyindedir; fonolojik yasa ya da etimolojik kanıt sayılmaz. Uzaklık yankısı şimdi insana yönelmiş düşmanlığa ayırıcı bir gölge katar.

Bu yapıda Şeytan özne, {ar:عَدُوًّا, tr:ʿaduwwan, gloss:düşman} onun niteliğini bildiren yüklemdir; {ar:لِلْإِنسَٰنِ, tr:li-l-insāni, gloss:insana karşı} düşmanlığın yöneldiği tarafı, son {ar:مُّبِينًا, tr:mubīnan, gloss:apaçık} ise düşmanın niteliğini açıklar. İnsan bu ilişkide hedef, fail değildir. Yönelme, {ar:لِ, tr:li, gloss:-e yöneliş} edatının tek başına değil, özneyle düşman yükleminin kurduğu ilişkinin sonucudur. Tekil-genel {ar:ٱلْإِنسَٰنِ, tr:al-insāni, gloss:insan}, uyarıyı kullar arasındaki yakın alandan insan türünün geneline taşır; burada kurulan hüküm bu düşmanlığın yönüdür.

İnsan adının yakınlık ve aşinalıkla, yabancılık ya da ürkekliğin kalkmasıyla gelen rahatlık ve sevinçle ilişkilendirilen kullanımları bu genişlemeye bir gölge düşürür. {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} kışkırtması ve {ar:عَدُوًّا, tr:ʿaduwwan, gloss:düşman} niteliği karşısında bu yankı, insanı yakınlık kurabilen ve bağı incinebilir toplumsal bir varlık olarak duyurur. Buradaki çağrışım duyusal algı ya da unutkanlıktan değil, yabancılığın kalkmasıyla oluşan aşinalık ve yakınlıktan beslenir; odaktaki “insan” anlamı korunur.

Düşmanlığın ortak alana girmesi, kişiler arasındaki sınırı aşan bir saldırganlık imgesi doğurabilir; bu imge ilişkisel alandadır, hukuki ihlal ya da fiziksel saldırı değildir. {ar:كَانَ, tr:kāna, gloss:olagelmiştir} ile kurulan yerleşik hâl ve karakter bildiren düşman niteliği, tutumun yinelenerek alışkanlığa dönüşmesini de düşündürebilir. Bu bağlantı tekrar izlenimidir; düşman sözcüğünün sözlük anlamını ya da biçimin tek başına süreklilik kanıtladığını ileri sürmez.

Son niteleme {ar:مُّبِينًا, tr:mubīnan, gloss:apaçık}, düşmanın belirgin oluşunu ve düşmanlığı açığa çıkaran niteliğini iki yakın biçimde duyurabilir; etkin ortaç yapısı ve hemen önceki düşman yüklemine bağlanışı bu iki okumaya da izin verir. Niteleme insanı değil düşmanı açıklar. {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} taraflar arasındaki alanı, {ar:مُّبِينًا, tr:mubīnan, gloss:apaçık} açıklık ve görünürlüğü taşıyan aynı sözcük ailesindendir; yan yanalıkları, ortak bağın zedelenişiyle düşmanlığın görünür hâle gelişini ilişkilendiren yerel bir yankı oluşturabilir. Bu bağlantı kasıtlı cinas iddiası taşımaz; burada {ar:مُّبِينًا, tr:mubīnan, gloss:apaçık} “konuşma” anlamına gelmez.

## Sözün İçeriği ve Alınışı

Düşmanlığın insana yöneldiği bu uyarı, “en güzel” sözün içeriğini ve karşılıklı konuşma koşullarını yakın bağlamda sınar. 17:40'ta muhataplara oğullar, Allah'a ise meleklerden dişiler isnat eden söylem ağır söz diye nitelenir (17:40). {ar:تَقُولُونَ قَوْلًا, tr:taqūlūna qawlan, gloss:söz söylüyorsunuz} biçimi sıradan bir söz söyleme eylemidir; yanlışlığın kaynağı odaktaki {ar:قُل, tr:qul, gloss:söyle} ya da {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} fiillerinin sözlük anlamı değil, bu bağlamda söylenen iddianın içeriğidir. Aynı söz ailesinin yanlış iddia bağlamında kullanılması, gerçek konuşma eylemini yalana indirgemeden doğruluğu da {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} ölçüsüne katar.

17:40'taki söz {ar:عَظِيمًا, tr:ʿaẓīman, gloss:ağır ve büyük} diye nitelenir (17:40); bu niteleme kanıtını aşan, ölçüsüzce büyümüş bir iddia imgesine izin verir, konuşanların kendilerini yüceltme saiki hakkında hüküm vermez. 17:43'te Allah'ın onların sözlerinden yüce oluşu {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yücelik} ile dikey bir ölçek kurar; {ar:كَبِيرًا, tr:kabīran, gloss:büyük} bu yüceliğin büyüklüğünü ayrıca vurgular (17:43). Yüceltilen Allah'tır. Bu iki sahne {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} ölçüsüne doğruluk ve ölçülülük boyutunu, söz konusu isnat bağlamında ekler; başka anlaşmazlıkları ya da konuşanların niyetlerini sınıflamaz.

Bu standart tartışmayı terk etmeyi gerektirmez. Muhatapların Elçi'ye benzetmeler sunması {ar:ضَرَبُوا لَكَ الْأَمْثَالَ, tr:ḍarabū laka al-amthāla, gloss:sana benzetmeler sundular} ve ardından {ar:فَضَلُّوا, tr:fa-ḍallū, gloss:yoldan saptılar} denmesiyle anlatılır (17:48). Bu sıra, benzetmelerin tartışmayı çarpıtan bir çerçeve kurmuş olabileceği izlenimini verir; bu, fiilin zorunlu anlamı ya da konuşanların kesin saiki hakkında hüküm değildir. Ardından 17:49'da kemik olup ufalanmış kalıntılara dönüşme itirazı gelir (17:49); 17:50'de muhataplar taş ya da demir olsalar bile geri getirilecekleri bildirilir (17:50); 17:51'de ilk yaratılış hatırlatılır ve bunun ne zaman olacağını sorarlar (17:51). Bu aynı meseledeki gerçek soru-cevap, söz ailesinin müzakere için kullanılan başka bir kalıbını çağrıştırır; odaktaki {ar:قُل, tr:qul, gloss:söyle} ve {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} ise yalın söyleme eylemleridir. Sahne, cevabın konuya bağlı kalabileceğini gösterir; bu özel örnek sessizlik buyruğu ya da ikna ve zafer garantisi getirmez.

Sözün nasıl karşılandığı da buyruğun anlamını değiştirir. 17:41'de hatırlatmaların uzaklaşmayı artırması, mesajın reddedilebildiği bir alım koşulu kurar (17:41). 17:45'te Kur'an okunurken anılan {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde}, mesajın alıcıya erişmeden gizli kalabilmesi görüntüsünü verir (17:45). 17:46'daki {ar:وَقْرًا, tr:waqran, gloss:kulaklarda ağırlık} işitmeye ağırlık bindirir; anlamama ve {ar:نُفُورًا, tr:nufūran, gloss:yüz çevirme} alımdaki güçlüğü yüz çevirmeye taşır (17:46). 17:47'de {ar:نَجْوَى, tr:najwā, gloss:gizli konuşma} özel istişare alanı açar ve mesaj bu kez “büyülenmiş bir adamı izliyorsunuz” diye düşmanca yeniden anlatılır (17:47). Perde erişimin kapanmasını, kulak ağırlığı işitme güçlüğünü, yüz çevirme geri çekilmeyi, gizli konuşmadaki yeniden anlatım ise mesajın çarpıtılmasını gösterir. Birlikte, iyi söz sorumluluğunun alımı denetlemekten değil, belirsiz alım koşulunda sadık ve incitmeyen hitabı sürdürmekten doğduğunu açıklar. Bu çıkarım söz konusu sahnenin koşullarına aittir.

17:47'deki düşmanca yeniden anlatım, sözlü iğne imgesine ayrı bir temas sağlar (17:47). Odaktaki {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} kişiler arasında işleyen kışkırtmadır; tek bir kişiyi belirli bir ifadeyle hedef alan iğneleme, bunun olası sözlü yollarından birini düşündürür. Bu bağlantı, fiilin geniş ilişki anlamını korur: 17:53 hakaret sözcüğü kullanmaz, Şeytan'ın yöntemini ya da belirli bir konuşan-hedef eşleşmesini açıklamaz.

“En güzel”in eylem boyutu, düşmanlık taşıyan ilişkiye verilen cevabın ne yapabildiğini gösterir. {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} odakta sözün niteliğini belirleyen addır; aynı sözcük ailesinin fiilleri bir şeyi güzelleştirmeyi, işi iyi ve özenle yapmayı, başkasına iyilik etmeyi anlatır. 41:34'te {ar:بِٱلَّتِي هِيَ أَحْسَنُ, tr:bi-llatī hiya aḥsanu, gloss:daha iyi olanla} karşılık verme, arada düşmanlık bulunan birinin candan dosta dönüşmesiyle yan yana gelir (41:34). Bu sahne, odak biçimin isim niteliğini koruyarak söz standardını başkasına yönelen iyiliğin ilişkisel etkisine doğru genişletir. Buradaki sevgi 41:34'ün sahnesindeki sonuçtur; odak sözcüğün doğrudan karşılığı ya da her ilişki için vaat değildir.

Bu dostluğa dönüş, {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} için aralık yanında ilişki ve bağlantı yönünü de açar. Sözcük ailesinin ayrı bir kullanımı bağı ve birleşmeyi anlatır; 41:34'te düşmanlığın yakın dosta dönüşmesi bu kullanıma bağımsız bir bağlam sağlar (41:34). Böylece odaktaki “aralarında” alanı boşluktan ibaret kalmaz: iyilikle desteklenebilir, kışkırtmayla zarar görebilir. Burada dostluğa dönüş, 41:34 ile kurulan ilişki paralelidir; 17:53'ün sonucu olarak vaat edilmez.

Yusuf'un sözü, bu bağın kopuşa uğrayıp yeniden kurulabildiğini aile içinde gösterir. 12:100'de Şeytan'ın Yusuf'la kardeşlerinin arasını bozduğu söylenir; ardından Yusuf, Allah'ın kendisini zindandan çıkarıp ailesini bir araya getirmesini iyilik olarak anar (12:100). Böylece kışkırtma aile ilişkisine girer ve aynı sahnede yeniden birleşme belirir. Örnek, odaktaki {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaghu baynahum, gloss:aralarında kışkırtır} ile ilişki düzeyinde paraleldir; 17:53'teki kulların kimliğini belirlemez.

Tek tanıklıktaki {ar:نَزَغَهُ بِكَلِمَةٍ, tr:nazaghahu bi-kalimatin, gloss:bir sözle onu iğneledi} kullanımı, belirli bir ifadeyle birini hedef alıp yermeyi anlatır; böylece sözlü iğne kolu kışkırtmanın bir ilişkiye nasıl batabileceğini somutlaştırır. Odaktaki {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} daha geniş bir anlam taşır; bu tek tanık onu tanımlamaz. 6:108'de başka varlıklara sövmemeleri, yoksa onların da Allah'a sövecekleri bildirilir: {ar:وَلَا تَسُبُّوا الَّذِينَ يَدْعُونَ مِنْ دُونِ اللَّهِ فَيَسُبُّوا اللَّهَ, tr:wa-lā tasubbū alladhīna yadʿūna min dūni llāhi fa-yasubbū llāha, gloss:başka varlıklara sövmeyin yoksa onlar da Allah'a söver} (6:108). Bu ayet, bir sözün karşılık bulup gerilimi yükselttiği alışverişi görünür kılar; en güzel söz ölçüsü de ilişkiye eklenen bu sonucu hesaba katmaya çağırır.

Karşılıklı alışverişin yanında, sözün topluluk içinde dolaşması ayrı bir yüzdür. Söz ailesindeki {ar:القول الفاشي في الناس, tr:al-qawlu al-fāshī fī al-nās, gloss:insanlar arasında dolaşan söz} ifadesi, iyi ya da kötü sözün insanlar arasında yayılmasını adlandırır. Odaktaki {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} ise söyleme eylemini bildirir; toplumsal dolaşım bu fiilin kendiliğinden taşıdığı anlam değildir. İnsanların ortak alanı ve 6:108'deki karşılıklı sövgü, sözün grup içinde alınıp geri verilebildiğini gösterir (6:108). Bu bağlantı her sözün yayıldığını ya da ilgili kullanımı dedikodu olarak tanımlamaz; yalnızca iyi sözün de dolaşıma katılabileceğini açar.

Bu toplumsal dolaşımın yanında hastalık benzetmesi, düşmanlığın yakın ilişkiler ağı boyunca kişiden kişiye geçebilmesini görünür kılar. {ar:عَدُوًّا, tr:ʿaduwwan, gloss:düşman} niteliğini {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} ve {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} ile ortak ağa yerleştiren cümle, {ar:قُل, tr:qul, gloss:söyle} ve {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} buyruğundaki konuşmayla birleşince, sözün aktarım koşullarını değiştirebileceğini düşündürür. Bu toplumsal bulaşma benzetmesinde insan yakınlığı yayılma zeminini, düşmanlık taşınan şeyi, sözlü iğneleme ise imgenin konuşma boyutunu verir; iyi söz zinciri kesebilir. Benzetme biyolojik hastalık ya da hastadan uzak durma öğüdü değildir; {ar:ٱلْإِنسَٰنِ, tr:al-insāni, gloss:insan} anlamı korunurken kırılganlaşan, insanlar arasındaki ortak bağdır.

Yakın dostluğun düşmanlığa dönüşmesi, bu bağın çözülme ihtimalini başka bir ölçekte gösterir. 43:67'de yakın dostların o gün birbirine düşman kesileceği, Allah'a karşı sorumluluk bilinci taşıyanların ise bu dönüşümden ayrı tutulacağı söylenir (43:67). Birlik ve ayrılmayı anlatan ayrı “bayn” kullanımı, bu sahnede ilişkinin çözülme yönünü öne çıkarır. Böylece odaktaki “aralarında” alanı, bağ kurulmasının yanı sıra kopuşun da yaşanabildiği ortak yerdir; 43:67 bu olasılığı gösterir, odak sözcüğün temel anlamını değiştirmez.

“Apaçık düşman” niteliğinin ayrı bir bağlamı, ilişki riskini aile içindeki bir planla birlikte gösterir. 12:5'te {ar:إِنَّ الشَّيْطَانَ لِلْإِنسَانِ عَدُوٌّ مُّبِينٌ, tr:inna ash-shayṭānu li-l-insāni ʿaduwwun mubīn, gloss:Şeytan insanın apaçık düşmanıdır} denirken Yakup Yusuf'a rüyasını kardeşlerine anlatmamasını, onların kendisine tuzak kurabileceğini söyler: {ar:عَلَىٰ إِخْوَتِكَ فَيَكِيدُوا لَكَ كَيْدًا, tr:ʿalā ikhwatika fa-yakīdū laka kaydan, gloss:kardeşlerin sana tuzak kurabilir} (12:5). Böylece apaçık düşmanlık, insan ilişkilerinin içine düşebilecek yıkıcı bir planla yan yana gelir. Bu bağlantı ilişki düzeyindedir; biçimsel bir dilbilgisi eşleşmesi ileri sürmez. Sahne düşmanlığın yöntemini odağa eklemez ve en iyi söz ölçüsünü her bağı onarma vaadine dönüştürmez.

## Sözün Ses ve Miktar Boyutu

Söylemenin sesle dışa vurulması, {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} buyruğunun sunuluş biçimini de düşündürür. 17:110'daki namaz okuyuşuna ilişkin tekil, geriye dönük bir okuma ölçülü seslendirmeyi olası bir çağrışım olarak verir (17:110). Burada Arapça lafız ve biçim karşılaştırılamadığı için bu temas keşifsel kalır: sözün nasıl seslendirilebileceğini düşündürür, 17:53 için ses yüksekliği kuralı koymaz.

17:52 başka bir ölçü boyutu açar. Orada {ar:قَلِيلًا, tr:qalīlan, gloss:az bir süre} diriliş çağrısından sonra kalınan zamanı ölçer; bu zaman kullanımı konuşma sayısını doğrudan ölçmez (17:52). Söz ailesindeki azlık kullanımı, odaktaki gerçek konuşma eylemine yalnızca analojiyle hacim boyutu ekler: niteliğin yanı sıra ne kadar söz söylendiği de düşünülebilir. Bu bağlantı {ar:قُل, tr:qul, gloss:söyle} ya da {ar:يَقُولُوا, tr:yaqūlū, gloss:söylesinler} biçimlerine “az konuş” anlamı vermez. {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} için çaba ve erişilebilir üst sınır okumaları iki sabit ifadeye aittir; odaktaki biçim bu kalıpların dışındadır.

Aynı 17:52'de {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırır} çağrıyı başlatır, ardından {ar:فَتَسْتَجِيبُونَ, tr:fa-tastajībūna, gloss:ardından karşılık verirsiniz} cevap hareketini getirir (17:52). Bu diriliş sahnesi, odaktaki {ar:بَيْنَهُمْ, tr:baynahum, gloss:aralarında} ilişkisinin yanıt verebilir oluşuna sınırlı bir benzetme sunar: {ar:يَنزَغُ, tr:yanzaghu, gloss:kışkırtır} bağı kesintiye uğratırken iyi söz onu cevaplanabilir tutabilir. Çağrı ile karşılık iki ayrı harekettir; bu özel temas odağı diriliş anlatısına taşımaz. Aynı sözcük ailesindeki {ar:مُّبِينًا, tr:mubīnan, gloss:apaçık} ise bu bağlamda açıklık ve belirginlik taşır; “bağlantı” yankısı burada bayn ile sınırlı kalır.

## Sözün Erişimi ve Sınırı

İyi sözün muhataba öğüt ve düzeltme yoluyla yararı olabilir; 17:54 ise nihai sonucu Allah'a bırakır. Allah'ın dilerse merhamet edeceği, dilerse azap edeceği ve Peygamber'in muhataplar üzerinde {ar:وَكِيلًا, tr:wakīlan, gloss:gözetici ve vekil} olmadığı bildirilir (17:54). Bu sınır içinde {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} hitap, başka birine iyilik etmeye açık bir eylem yönü kazanır; konuşan akıbeti üstlenmez ya da denetlemez. Bu sınır düzeltme ve ahlaki değerlendirmeyi sürdürür; daha genel sorumluluk sınırının hidayet sonucuyla ilgili olması da mümkündür. Vekil/gözetim alanındaki başkası üzerinde hüküm ya da denetim üstlenme kullanımı burada ayrı bir benzetme koludur; bu özel temas odaktaki söyleme fiilinden değil, Peygamber'in vekil olmadığının bildirilmesinden doğar.

Topluluğa yönelen iyi söz, tek kişiye yöneltilmiş korunma çağrısının yanında ayrı bir imkân olarak belirir. 7:200'de Şeytan'dan bir kışkırtma erişirse Allah'a sığınma buyruğu {ar:وَإِمَّا يَنزَغَنَّكَ مِنَ الشَّيْطَانِ نَزْغٌ فَاسْتَعِذْ بِاللَّهِ, tr:wa-immā yanzaghannaka mina ash-shayṭāni nazghun fa-staʿidh bi-llāh, gloss:Şeytanın kışkırtması erişirse Allah'a sığın} biçiminde kurulur (7:200). Bu, odaktaki {ar:يَنزَغُ بَيْنَهُمْ, tr:yanzaghu baynahum, gloss:aralarında kışkırtır} ile aynı sözcük ailesinden kışkırtmayı bireysel sığınma çağrısına bağlar; karşılaştırma burada kök ve anlam düzeyindedir. Kişisel sığınma ve topluluğa yöneltilen iyi söz, korunmanın iki ayrı yolunu gösterir; bu bağlantı onları hiyerarşik kılmaz ve tek bir sözün başkasını ikna edeceğini garanti etmez.

17:59-60'taki uyarı dizisi, sözün tarzıyla birlikte ardından doğan tepkiyi de hesaba katmayı düşündürür. 17:59'un sonundaki {ar:تَخْوِيفًا, tr:takhwīfan, gloss:korkutarak uyarma} işaretlerin korkutma/uyarma işlevini belirtir (17:59). 17:60'ta {ar:نُخَوِّفُهُمْ, tr:nukhawwifuhum, gloss:onları korkuyla uyarıyoruz} tekrarlanır; ardından {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:onları artırır} artışı ve {ar:طُغْيَانًا, tr:ṭughyānan, gloss:sınırı aşma ve azgınlık} sınır aşımı gelir (17:60). Bu sahnede tekrar edilen ilahî uyarı, direnen muhatapların tepkisindeki artışla zincir kurar. Odaktaki {ar:يَنزَغُ, tr:yanzaghu, gloss:ilişkileri bozan kışkırtma} ve {ar:أَحْسَنُ, tr:aḥsanu, gloss:en güzel} ile bağlantı, insan sözünün ilişkiye katkısını ve tepkisini tartmayı sağlar; bu özel analoji her uyarıyı sakıncalı saymaz ya da uyarıdan kaçınma kuralı koymaz.

Bu dizideki {ar:طُغْيَانًا, tr:ṭughyānan, gloss:sınırı aşma ve azgınlık} öncelikle ahlaki haddi aşmayı adlandırır. Aynı yüzey, bundan ayrı ve ihtiyatlı bir taşarak yayılma imgesine de izin verir; bu olası yankının bağımsız su anlamı doğrulanmış değildir ve ahlaki sınır okumasından ayrı kalır. 17:60'taki {ar:الشَّجَرَةَ الْمَلْعُونَةَ, tr:al-shajarata al-malʿūnata, gloss:lanetlenmiş ağaç} ise bağlamda gerçek ağaçtır (17:60); dallanma ve dolanma biçimi, ilişkisel karmaşıklığı düşünmek için ayrı, keşifsel bir imge sağlar. Taşma yankısı {ar:طُغْيَانًا, tr:ṭughyānan, gloss:sınırı aşma ve azgınlık} yüzeyine, dallanma imgesi ağacın biçimine bağlıdır; ikisi birbirini doğuran tek bir mecaz değildir. Ağaç imgesi bu bağlantıda sözel bir mekanizma da tarif etmez. İlahî uyarı-tepki dizisi kendi bağlamını korurken, bu imgelerin konuşma buyruğuna taşınması olasılık düzeyinde kalır.

Bu hitabın kulluk çerçevesi, Fâtiha'daki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:yalnız sana kulluk ederiz yalnız senden yardım dileriz} sözüyle de duyulabilir (1:5). {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} Allah'a yönelmiş boyun eğişi ve kendini O'na vermeyi, {ar:نَسْتَعِينُ, tr:nastaʿīn, gloss:yardım dileriz} ise O'na bağımlılığı belirginleştirir. Bu “biz” ile 17:53'teki {ar:لِعِبَادِي, tr:liʿibādī, gloss:kullarıma} ayrı göndergelerdir; ortak kulluk sözcük ailesi, söz ahlakını ibadet ve Allah'a muhtaçlık ufkunda duyurur. Bu bağlantı en güzel konuşmayı kulluk ufkuna yerleştirir, onu ibadet fiiliyle özdeşleştirmez.

</source_prose>
