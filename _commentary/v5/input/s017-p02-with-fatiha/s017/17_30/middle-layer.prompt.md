# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:30**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.middle.claims.json`

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
- Refer to source paragraphs as `17:30 ¶N`.

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

`(17:30 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:30",
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
        "citation": "(17:30 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_30/17_30.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_30/17_30.middle.claims.json \
  --ayah-ref 17:30
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_30/17_30.prose.editorial.tr.md`

<source_prose>
17:30, Rabbinin rızkı kime açıp kime ölçüyle daralttığını ve bu payların iliştiği kullar hakkındaki bilgisini art arda bildirir. Başlangıçtaki {ar:إِنَّ, tr:inna, gloss:şüphesiz} dağıtım hükmünü kesin bir bildirim olarak kurar. {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} öznesi önce {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} ve {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} eylemlerini, ardından {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} nesnesini taşır; {ar:لِمَنْ يَشَآءُ, tr:li-man yashāʾu, gloss:dilediği kimse için} kimin yarar gördüğünü belirtirken miktarı açık bırakır. İkinci {ar:إِنَّهُۥ, tr:innahu, gloss:şüphesiz O} aynı Rabbe dönen zamirle yeni cümleyi başlatır: ilk cümlenin dağıtım hükmü tamamlanmıştır, şimdi bu dağıtımı yapanın kulları bilmesi ve görmesi öne çıkar.

## Payın Açılması ve Ölçüsü

{ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} unvanının iki fiilden önce gelişi, dağıtımı adı konmuş bir Rabbin eylemi olarak duyurur; ikinci şahıs eki de hitabı doğrudan muhataba yöneltir. Bu unvan yönetme ve sahip çıkma ilişkisini kurarken, aynı sözcük ailesinin gözetileni yetiştirme ve bakım altında büyütme yönü de bakım çağrışımı katar. Odakta {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} ad biçiminde durur; rızık üzerindeki genişletme ve kısma fiilleri bu çağrışımı somut bir idare alanında duyurur. Değişen pay böylece tek seferlik bolluktan çok süren gözetim içinde belirir.

Genişletmenin fiili olan {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir}, belirli {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} nesnesi üzerinde sürmekte olan bir hareketi anlatır. Yayma ve uzatma yönü, karşısındaki {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} fiilinin ölçü ve daralma yönüyle buluşunca, rızık alanı açılıp sınırlandırılan bir kaynak gibi duyulur: ilk fiil genişlemeyi, ikincisi karşı hareketi, nesne ise yararlanılan payı sağlar. Ayet kaynağın somut maddesini belirlemediğinden imge, rızık ile bu iki hareket arasındaki dağıtım ilişkisi içinde kalır. Rızık yiyecek ve para gibi somut faydanın yanı sıra alıcının yararlandığı payı da kapsar.

{ar:وَ, tr:wa, gloss:ve} ile bağlanan daraltma, aynı dağıtım hükmünün ikinci hareketidir. İlk fiilin nesnesi yinelenmese de önceki {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} ikinci fiilde anlaşılabilir; fail de tekrarlanmayan {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin}den alınır. Bu kuruluş, genişletme ve daraltmayı ortak failin iki yönlü tahsisi olarak okutur. Nesnenin düşürülmesi aynı rızkın daraltıldığı okumasını taşırken, fiilin nesnesiz ve daha genel bir daralma bildirmesi de dilbilgisel olarak açık kalır.

Rızık adından sonra gelen {ar:لِمَنْ, tr:li-man, gloss:kimin için}, yararlanıcıyı açık ve genel bir biçimde belirtir; belirli bir toplumsal sınıf seçmez. Öbeğin iki fiile uzanması, aynı alıcının hem genişleme hem daralma ilişkisine girmesine izin verir; alıcı belirtilirken payın miktarı açık kalır. Bu ilgi öbeğindeki {ar:يَشَآءُ, tr:yashāʾu, gloss:diler} süren iradeyi bildirir. Öznenin ayrıca yinelenmemesi, en yakın {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin}i güçlü yerel karşılık yapar; cümlenin biçimi başka bir örtük özne ihtimalini de açık tutar. Dileme böylece rızık ile tahsis hareketini birbirine bağlarken alıcının kimliği ve liyakati konusunda hüküm vermez.

{ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} burada payı kısma yönündedir; aynı sözcük alanının bir ölçü koyma ve düşünerek tasarlama yönü de amaçlı fail ve irade ilişkisi içinde duyulabilir. Bu ek çağrışım daraltmayı silmeden, fiilin tam bir kader öğretisi kurduğu sonucuna varmadan işler. Miktar ve erişilen sınır anlamları, açık rızık nesnesi ve genişletme karşıtlığıyla birleşince pay rastgele yoksunluktan çok ölçüsü belirlenen bir tahsis gibi duyulur. Nesnenin ikinci fiilde düşürülmesi ve alıcının belirtilmesi, kimi söz öbeklerine özgü “birinin geçim payını daraltma” kullanımını da çağırabilir; bu özel kullanım her ölçme fiiline yayılmaz. Genel daraltma okuması da geçerlidir; ayet miktarı ya da yoksulluğu belirtmez.

## Kulların Bilgi Alanı

İkinci cümledeki {ar:إِنَّهُۥ, tr:innahu, gloss:şüphesiz O}, yeni bir fail getirmek yerine önceki cümlenin öznesi olan {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin}e döner. {ar:كَانَ, tr:kāna, gloss:olagelmiştir} geçmiş biçimli olsa da burada bir zamanlar tamamlanmış bilme olayından çok, ardından gelen iki niteliğin yerleşik durumunu taşır. Dağıtımı yapan fail böylece aynı cümle içinde kulları hakkındaki bilgisi ve görmesiyle belirir.

Bu niteliklerin alanını önce {ar:بِعِبَادِهِۦ, tr:bi-ʿibādihī, gloss:kulları hakkında} öbeği kurar. Edatın yönettiği çoğul ve iyelik eki, tekil ve açık bırakılmış yararlanıcıdan Rabbe bağlı daha geniş bir topluluğa geçiş sağlar. Burada adlandırma kulları Tanrı’ya ait ve O’na bağlı bir insan topluluğu olarak çerçeveler; bu ilişki topluluğun kapsamını verir, hukuki statüyü ya da ibadet eylemini değil. Topluluğun bu şekilde anılması da tek başına eşit pay sonucu doğurmaz.

İlk yüklem {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen}, nitelik bildiren bir sıfattır. Bilgiyi edinme ve aktarma yönü, kullar alanıyla ve ardından gelen görme sıfatıyla buluşunca tahsisin görünmeyen koşullarını da bilen bir fail tasavvuru açar. Aynı sözlük çevresinin deneyimle edinilen bilgiyi ve dış görünüşün ardındaki niteliği tanımayı kapsayan yönü daha dar bir çağrışım olarak eklenir; bu çağrışım, tek tek kulların hangi ihtiyacı taşıdığını belirlemez.

İkinci sıfat {ar:بَصِيرًا, tr:baṣīran, gloss:gören}, olağan gözle görme anlamını korur. Sözcük ailesindeki kalp ve zihnin nüfuz ederek kavrama yönü, hemen önceki {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} ve aynı kullar alanıyla temas ettiğinde iç hâlleri ayırt etme çağrışımı da kazanır. İki sözcük aynı söz dizimsel ağırlıkta yüklemlerdir; eril tekil ve belirsiz mansup biçimleri, benzer kalıpları ve yinelenen “-an” sesleri bir ritim kurar. Görmenin son sıraya gelmesi tahsis cümlesini algıyla kapatır: içi bilinen kullar, dış koşullarıyla da görüş alanındadır.

Bu kapanış, değişen payı hem irade hem bilgi çerçevesinde duyurur. {ar:يَشَآءُ, tr:yashāʾu, gloss:diler} olağan irade anlamını taşırken, {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} bazı söz öbeklerinde başka bir ölçüye uygun düşmeyi de anlatabilir; {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören} payın iliştiği kulların iç ve dış koşullarını çerçeveler. Bu unsurlar, payın kişiye uygun düşebileceği bir okuma ihtimalini birlikte açar. Bu sonuç sözlükteki sabit bir karşılıktan ya da hesaplanabilir dağıtım yönteminden değil, 17:30’daki irade, ölçü ve bilgi ilişkisinden doğar; eşit sonuçları öne sürmez ve belirli bir gizli ihtiyacı saptamaz.

17:24’teki anne baba duası, {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} unvanının bakım yönüne zaman içinde büyüyen bir insan ilişkisi verir. Konuşan, ebeveynlerinin kendisini küçükken yetiştirmesini {ar:كَمَا رَبَّيَانِى صَغِيرًا, tr:kamā rabbayānī ṣaghīrā, gloss:beni küçükken yetiştirdikleri gibi} diye anar; {ar:مِنَ ٱلرَّحْمَةِ, tr:mina r-raḥmati, gloss:merhametten} ve {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:onlara merhamet et} sözleriyle onlar için merhamet diler (17:24). Bu aile sahnesi, değişen rızık payını bakım ilişkisi içinde duyurur. Yetiştirme biçiminin kökü Rabb unvanının kökünden ayrıdır; temas kök ortaklığına değil, ebeveynin çocuğu büyüttüğü sahneye dayanır. Bu nedenle benzerlik bakım yönünü aydınlatır, bireysel payın sebebini açıklamaz.

17:25 aile anısından iç hâllere geçer: {ar:رَّبُّكُمْ أَعْلَمُ بِمَا فِى نُفُوسِكُمْ, tr:rabbukum aʿlamu bimā fī nufūsikum, gloss:İçinizdekini en iyi Rabbiniz bilir}. Bu söz, odaktaki {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} sıfatını insanın içinden geçeni bilme yönüyle somutlaştırır; değişen pay böylece yalnız görünen şartlar değil, iç hâller de bilinen bir ilahi hüküm altında duyulur. Bu temas, kişiye özgü payın nedenini belirlemez.

Fâtiha’nın unvanları hitabın ölçeğini genişletir. Odaktaki {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin}, sahiplik ve yönetim yönüyle {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabbil-ʿālamīn, gloss:âlemlerin Rabbi} (1:2) ve {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmid-dīn, gloss:hesap gününün mâliki} (1:4) unvanlarının yanına gelir. Muhataba dönük kişisel hitap ve değişken pay, böylece âlemleri ve zamanı aşan Rablik çerçevesinde duyulur; yakınlık payın miktarını değil, ilişkinin ölçeğini değiştirir.

Fâtiha 1:5’teki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa iyyāka nastaʿīn, gloss:Yalnız sana kulluk eder ve yalnız senden yardım dileriz} sözü, ilk çoğul kişiyi kulluk eden ve yardım isteyen bir topluluk olarak konuşturur (1:5). Bu “biz”, odaktaki {ar:بِعِبَادِهِۦ, tr:bi-ʿibādihī, gloss:kulları hakkında} adıyla buluşunca, rızık alanların da Rabbe bağımlılıklarını kendilerinin dile getirdiği bir ilişki açılır; pay, Rabbe yönelen topluluğun yaşadığı bağ içinde duyulur. Fâtiha’daki topluluk dua eder; odaktaki “kulları” ise dağıtım cümlesinde yararlanıcılar olarak adlandırılır.

## Payın İnsanî Yüzü

17:30’da yararlanıcı genel bırakılır; 17:26 ve 17:31 bu dağıtımın temas ettiği insan ilişkilerini belirginleştirir. 17:26’daki {ar:ءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ, tr:āti dhā l-qurbā ḥaqqahu, gloss:yakına hakkını ver} buyruğu kaynakları yakının hakkına bağlar. 17:31’de çocuklar özellikle anılır ve {ar:نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:naḥnu narzuquhum wa iyyākum, gloss:onlara da size de biz rızık veririz} sözü onları anne babalarıyla birlikte rızık alıcısı olarak gösterir (17:26, 17:31). Odaktaki {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören} böylece yakının hakkı ve çocukların alıcılığıyla somutlaşan insan alanında yankılanır. Buradaki bağ, ilahi payı yakınlar arasındaki hakla özdeşleştirmez; dağıtımın insanlar arasında doğurduğu yükümlülükleri görünür kılar.

17:31’deki {ar:خَشْيَةَ إِمْلَاقٍ, tr:khashyata imlāqin, gloss:yoksulluk korkusuyla} sözü, beklenen yoksulluğun ve korkunun baskısını adlandırır. Odaktaki {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} ile bu darlık arasındaki temas, gelecekte çocuğa hiç pay kalmayacağı yolundaki sıfır toplamlı hesabı görünür kılar. 17:31 çocukları öldürmeyi {ar:وَلَا تَقْتُلُوا۟ أَوْلَادَكُمْ, tr:wa-lā taqtulū awlādakum, gloss:çocuklarınızı öldürmeyin} diye yasaklar, ardından çocuklara ve anne babaya rızık verildiğini söyler ve öldürmeyi {ar:إِنَّ قَتْلَهُمْ كَانَ خِطْـًٔا كَبِيرًا, tr:inna qatlahum kāna khiṭʾan kabīran, gloss:onları öldürmek büyük bir yanlıştır} diye niteler. Bu karşılık, korkunun çocuğu gelecekteki rızık ilişkisinden çıkarmasını reddeder; maddi yoksulluk korkusu gerçek kalır, ayetin açık yasağı ise çocuk öldürmeye yönelir (17:31). Bu bağlantı yoksulluk korkusunu ve yasağın kapsamını açıklar; her geçim sınırını yok sayan genel bir kural kurmaz.

34:15’teki {ar:كُلُوا مِن رِّزْقِ رَبِّكُمْ, tr:kulū min rizqi rabbikum, gloss:Rabbinizin rızkından yiyin} çağrısı, rızkın yarar payı anlamına bedensel beslenme yüzü verir: rızıktan yenir (34:15). 17:31’de çocukların da alıcı oluşu bu beslenme imgesini bağımlıların hayatına taşır (17:31). İki bağlam, değişen payı yaşama katılan maddi destek olarak somutlaştırır; 34:15 yiyeceğe ilişkin bu kullanımı gösterirken 17:30’daki rızkın kapsamı daha geniş kalır.

89:15’te bolluk gören kişi bunu {ar:رَبِّىٓ أَكْرَمَنِ, tr:rabbī akramanī, gloss:Rabbim beni onurlandırdı}, 89:16’da darlık gören ise {ar:رَبِّىٓ أَهَانَنِ, tr:rabbī ahānanī, gloss:Rabbim beni aşağıladı} diye yorumlar. Bu ayetler, maddi farkın insan dilinde onur ve aşağılanma yargısına çevrilişini gösterir (89:15, 89:16). Odaktaki {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} bolluk, {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} darlık tarafıyla bu yargıların dayandığı farkı açığa çıkarır; böylece 17:30’un pay dili, insanın bu farkı nasıl anlamlandırdığını görünür kılar. Onur-aşağılanma hükümleri bu bağlamdaki insan yorumlarıdır, 17:30’un dağıtım ölçütü değil; daralma ile ölçüye uygun düşme ihtimali ise odak ilişkide birlikte kalır.

17:70’te insanların karada ve denizde taşınması, ardından güzel şeylerden rızıklandırılmaları anlatılır: {ar:وَحَمَلْنَٰهُمْ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:wa-ḥamalnāhum fī l-barri wa-l-baḥri, gloss:karada ve denizde onları taşıdık} ve {ar:وَرَزَقْنَٰهُم مِّنَ ٱلطَّيِّبَٰتِ, tr:wa-razaqnāhum mina ṭ-ṭayyibāti, gloss:onlara güzel şeylerden rızık verdik} (17:70). Taşıma, hareket hâlindeki insanlığı; sonraki ifade, onlara ulaşan nimetleri öne çıkarır. Odaktaki {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} ile birlikte okunduğunda bu sıra değişen payı insanların hareketi içinde alınan maddi destek olarak duyurabilir. Bu çağrışım 17:70’in kendi sırasına dayanır: taşıma bireysel payı belirlemez ve 17:66, 17:67, 17:68, 17:69’daki kurtarılma sahneleri bu pay okumasına taşınmaz.

## İnsanî Ölçü

İlahi rızık dağıtımının insanın verme gücüyle teması, 17:29’daki iki el ucunda belirginleşir. {ar:مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:maghlūlatan ilā ʿunuqika, gloss:boynuna bağlanmış} el, vermeyi kısıtlamayı; {ar:وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ, tr:wa-lā tabsuṭhā kulla l-basṭi, gloss:elini bütünüyle uzatma} buyruğu ise savurganlığa ve {ar:مَلُومًا مَّحْسُورًا, tr:malūman maḥsūran, gloss:kınanmış ve tükenmiş} kalmaya varan sınırsız vermeyi gösterir (17:29). 17:26’daki yakının hakkı ve savurganlık uyarısı bu uçları yükümlülük içinde tartar: ilkinde hak askıda kalır, ikincisinde kaynak tükenir (17:26, 17:29). Odaktaki {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} eli değil rızkı nesne alır; böylece iki ayet ilahi tahsis ile insanın verme kapasitesini farklı eylemler olarak yan yana getirir (17:29, 17:30). 17:31’de çocuklarla anne babanın alıcı oluşu, insanî vermenin kime ulaşabileceğini somutlaştırır (17:31). Bu ilişki cömertliği hak borcu ve mevcut kapasiteyle sınırlar; ne hakkı vermemeye ne de tükenene kadar harcamaya indirger.

İnsanın elini nasıl kullanacağı, {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} fiilinin ölçme yönünü yeni bir ilişkide duyurur. Sözcük alanının ölçüp karşılaştırarak bir işi tasarlaması, iki el ucu ve 17:26’daki hak-savurganlık karşıtlığıyla birleşince verme kapasitesini tartma imgesi kurar; kimi söz öbeklerindeki “başka bir ölçüye uygun düşme” anlamı da bu imgeye orantı fikrini katar (17:26, 17:29). Buradaki orantı belirli bir sayısal orta nokta değildir. Bağ, insanın harcama gücünü tartma düzeyinde kalır; ilahi tahsis hazır bir kişisel bütçe kuralına dönüşmez.

17:100, insanın elini kapalı tutmasının ardındaki başka bir güdüyü gösterir: Rablerinin rahmet hazinelerini ellerinde bulundurdukları varsayımında insanlar {ar:لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ, tr:la-amsaktum khashyata l-infāq, gloss:harcama korkusuyla elinizde tutardınız} (17:100). Buradaki tutma harcama korkusundan doğar; odaktaki {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} ve {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} ise payın genişlemesi ve ölçülmesini anlatır. 42:27’deki {ar:يُنَزِّلُ بِقَدَرٍ مَّا يَشَاءُ, tr:yunazzilu biqadarin mā yashāʾu, gloss:dilediğini ölçüyle indirir} bu ilahi ölçülü gönderimi ayrıca görünür kılar (42:27). Yan yana geldiklerinde 17:100, kaynağı tüketme korkusuyla alıkoymayı; 42:27, ölçüyle göndermeyi sağlar. Bu karşıtlık, odaktaki daralma olasılığını insanî cimrilikten ayırır; herhangi bir dağıtım politikasını ya da kişinin özel pay nedenini belirlemez.

## Emanet, Bilgi ve Sınır

17:34’teki yetim malını koruma ve ahdi yerine getirme, başkasına ait olanı gözetip teslim etme yükümlülüğünü kurar: {ar:وَلَا تَقْرَبُوا۟ مَالَ ٱلْيَتِيمِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ, tr:wa-lā taqrabū māla l-yatīmi illā bi-llatī hiya aḥsan, gloss:Yetim malına en iyi biçimde yaklaşın} buyruğu malı yetim erginleşinceye dek korumayı, {ar:وَأَوْفُوا۟ بِٱلْعَهْدِ, tr:wa-awfū bi-l-ʿahdi, gloss:ahdi yerine getirin} ise bağlayıcı ahdi tamamlamayı ister (17:34). 17:35 bu emanet ilişkisini alışverişteki ölçüye taşır: {ar:وَأَوْفُوا۟ ٱلْكَيْلَ إِذَا كِلْتُمْ, tr:wa-awfū l-kayla idhā kiltum, gloss:ölçtüğünüzde ölçüyü tam verin} yiyeceğe uygulanan miktarı, {ar:وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:wa-zinū bi-l-qisṭāsi l-mustaqīm, gloss:doğru teraziyle tartın} doğru tartıyı öne çıkarır (17:35). Böylece korunan mal ve yerine getirilen ahit, başkasına eksiksiz aktarılacak ölçüyle buluşur; insanî ölçü emanetin hakkını teslim eder. Bu temas miktar ve hakkaniyet düzeyindedir: odaktaki fiil insanın pazar terazisini adlandırmaz.

42:27 rızkın sınırsız genişlemesini yeryüzündeki taşkınlık ihtimaliyle ilişkilendirir; {ar:يُنَزِّلُ بِقَدَرٍ مَّا يَشَاءُ, tr:yunazzilu biqadarin mā yashāʾu, gloss:dilediğini ölçüyle indirir} sözü bu sahnede ölçülü gönderimi, {ar:خَبِيرٌ بَصِيرٌ, tr:khabīrun baṣīrun, gloss:derinlemesine bilen ve gören} kapanışı ise dağıtımı bilen ve gören faili vurgular (42:27). 29:62 başka bir katkı yapar: kullara yönelik rızık dağıtımında {ar:يَبْسُطُ ٱلرِّزْقَ, tr:yabsuṭu ar-rizqa, gloss:rızkı genişletir} ile {ar:وَيَقْدِرُ لَهُۥ, tr:wa-yaqdiru lahu, gloss:ona ölçü koyar ya da kısar} aynı rızık ilişkisini açıkça kurar, ardından her şeyi bilme niteliği gelir (29:62). İlk ayette ölçü genişletmenin taşkınlıkla ilişkisini sınırlar; ikincide aynı çift alıcıya yöneltilmiş rızık tahsisini belirginleştirir. Birlikte bu bağlamlar, odaktaki genişlemeyi geçim imkânı, daraltmayı payın ölçüsü olarak duyurur; 42:27’deki gönderim ayrıca söz öbeğine bağlı “ölçüye uygun düşme” çağrışımını destekler. Orantı ile azaltma aynı ilişkide buluşabilir, ancak bu okuma 17:30’da belirli bir kişi için hesap vermez.

17:36, odaktaki {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören} sıfatlarını insan bilgisinin sınırıyla karşı karşıya getirir. {ar:وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِۦ عِلْمٌ, tr:wa-lā taqfu mā laysa laka bihi ʿilmun, gloss:Hakkında bilgin olmayan şeyin ardına düşme} buyruğunun yanında {ar:ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ, tr:as-samʿa wa-l-baṣara wa-l-fuʾāda, gloss:kulağı, gözü ve gönlü} sayılır ve hepsinin sorumlu olduğu bildirilir (17:36). Bu ayet, insanın bildiği ve duyduğu kadarıyla hüküm verme sınırını kurar: görünen rızık, insanın alıcının iç değeri hakkında hüküm vermesine yetmez; algı yetileri de kendi sorumluluklarıyla sınırlıdır. Gönlün anılması {ar:بَصِيرًا, tr:baṣīran, gloss:gören} için iç kavrayış yankısı açarken olağan görme anlamı da sürer. 17:36’daki sınır her bilgi iddiasına ilişkindir; burada rızıkla kesişmesi, servetin insanın saklı değerini ölçemeyeceğini özellikle görünür kılar.

17:17’de kulların günahlarının anılması, {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} ve {ar:بَصِيرًا, tr:baṣīran, gloss:gören} çiftine günahları bilme bağlamı verir; 17:96’da {ar:شَهِيدًا بَيْنِى وَبَيْنَكُمْ, tr:shahīdan baynī wa-baynikum, gloss:benimle sizin aranızda tanık} sözünü aynı çift izler ve iki taraf arasındaki tanıklığı öne çıkarır (17:17, 17:96). Bu ayrı bağlamlar, 17:30’daki kapanışta kulların iç yüzünü bilme ile onları görüş alanında tutmanın kapsamını aydınlatır. Görünen pay insanın bütün koşullarını göstermez; günah ve tanıklık kendi ayetlerinin bağlamında kalır. Bu yankı 17:30’u tehdit tonuna çekmez ve darlığı suçluluk işareti yapmaz.

17:36’daki bilgi sınırından 17:37’de insanın kendine biçtiği boya geçilir. {ar:مَرَحًا, tr:maraḥan, gloss:gururla ve taşkın sevinçle} yürümek dağların ve boyca yüksekliğin sınırıyla karşılaştırılır (17:37). Bu dikey ölçek, odaktaki geniş rızık imgesine farklı bir boyut ekler: {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} maddi imkânın yatay kapsamını, {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} erişilen miktarın sınırını düşündürürken, gururlu yürüyüş kişisel yücelik iddiasını dağ yüksekliğiyle ölçer. Böylece yatay imkân ile dikey öz-yüceltme arasındaki fark görünür olur. Bu bağlantı rızkı fiziksel boya dönüştürmez; 17:37’nin kendi uyarısı genel kibir üzerinedir.

## Bakımın Doğal İmgesi

Sözlük çevresindeki bakım ve yüzey çağrışımları, dağıtımı büyüyen bir zemin imgesiyle duyurur. {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} yönetme unvanı olarak kalırken, aynı kelime ailesinin gözetileni ya da ürünü besleyip büyütme yönü zeminin bakımını düşündürür. {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} ayette fiildir; ailede yere serilip yüzeyi kaplayan yaygı ve serilmiş düz, geniş arazi anlamları da vardır. Bu yayılma, {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} nesnesi ile {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} fiilinin miktar-sınır yönüyle buluşunca, bakım altında açılan ve sınırları belirlenen verimli bir zemin imgesi kurar. Unvan ve fiilin odaktaki biçimleri kendi anlamlarını korur; zemin görüntüsü aynı kelime ailelerinin çağrışımından ve dağıtım fiillerinin ilişkisinden doğar.

Bu zemin imgesine hayat veren girdi, {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} adının ayrı bir sözlük kullanımı olan yağmur ya da yağmur suyudur; bu kullanım büyümeyi besleyen kaynağı sağlar. {ar:يَقْدِرُ, tr:yaqdiru, gloss:ölçer ya da daraltır} ise girdinin miktar ve sınırını duyurur. Bakım, serilmiş yüzey, yağmur ve ölçü böylece ayrı işler üstlenerek ekili zeminin büyümesini kurar. Aynı sözlük çevresindeki gevşek, alçak ve su tutan arazi ya da birikinti çağrışımı bu toprağa dönük resmi destekler; ancak odaktaki {ar:خَبِيرًا, tr:khabīran, gloss:derinlemesine bilen} bilgi bildiren sıfattır. Bu nedenle su tutan arazi, sözcük ailesinden gelen uzak bir çağrışım olarak kalır; odaktaki sıfatın bilgi niteliğini değiştirmez.

22:63’te gökten indirilen {ar:مَاءً, tr:māʾan, gloss:su} ile {ar:ٱلْأَرْضُ مُخْضَرَّةً, tr:al-arḍu mukhḍarratan, gloss:yeşeren yeryüzü} aynı yağmur ve yeşerme sahnesinde buluşur (22:63). Bu ayet doğal imgeye görünür bir sahne verir; odaktaki {ar:ٱلرِّزْقَ, tr:ar-rizqa, gloss:rızkı} adının yağmur kullanımıyla kaynak yönünü, {ar:رَبَّكَ, tr:rabbaka, gloss:Rabbin} unvanının yetiştirme çağrışımıyla bakım yönünü güçlendirir. Ayrı olarak, 42:27’deki {ar:بِقَدَرٍ, tr:biqadarin, gloss:bir ölçüyle} gönderim miktarın ölçülü oluşuna dayanak verir (42:27). Böylece 22:63 suyun büyümeyi besleyişini, 42:27 ise ölçülü gönderimi katkı olarak sunar; bu iki destek 17:30’daki payı büyümeyi taşıyan bir kaynak gibi duyurur. Bağlantı odaktaki dağıtım imgesini açar: 17:30 yağmuru açıkça adlandırmaz, mevsimleri açıklamaz ve kişinin payını yağışla eşitlemez.

</source_prose>
