# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:29**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.middle.claims.json`

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
- Refer to source paragraphs as `17:29 ¶N`.

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

`(17:29 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:29",
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
        "citation": "(17:29 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_29/17_29.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_29/17_29.middle.claims.json \
  --ayah-ref 17:29
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_29/17_29.prose.editorial.tr.md`

<source_prose>
## İki Hareket, Aynı El

Önce muhatabın kendi {ar:يَدَكَ, tr:yadaka, gloss:elini} eli görünür: onu {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} bir hâle getirip {ar:إِلَىٰ عُنُقِكَ, tr:ilā ʿunuqika, gloss:boynuna doğru} yöneltmemesi istenir; ardından aynı eli {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} bütünüyle açıp yaymaması gelir. Ayrı yasaklar iki uç hareketi karşı karşıya getirir; arada tutulacak miktar ya da yöntem söylenmez. Sonuç cümlesinin hemen ardından gelmesi, özellikle tam uzatmayla olan bağı belirginleştirir. İlk hareket de ortak sonuç ufkunda kalır, ancak iki yasağın bu sonuca eşit ölçüde bağlandığı belirtilmez.

Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} önceki söyleyişe eklenir, fakat onun içeriğini burada yeniden kurmaz; böylece iki hareket süren bir talimat akışı içinde duyulur. Her iki yasakta da {ar:لَا, tr:lā, gloss:sakın} parçacığı fiilden ayrıdır ve yasağı fiile yöneltir. İlkinde ikinci tekil eril {ar:تَجْعَلْ, tr:tajʿal, gloss:hâle getirmek} biçimi muhataba doğrudan seslenir; ayrı bir seslenme sözü ya da başka bir katılımcı eklenmez. Fiil {ar:يَدَكَ, tr:yadaka, gloss:elini} ilk nesne olarak alırken {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} elin içine sokulduğu hâli bildirir. Bu kuruluş, yalnızca bağlı duran bir el değil, muhatabın kendi eli üzerinde kurduğu bir hâl verir. Fiil belirli bir tarihsel kişiyi ya da gerçekleşmiş fiziksel değişikliği saptamak yerine, muhatabın elini bir duruma sokmasını kurar. Özneye yüklenen eylem sorumluluğu kendi başına hukukî ya da psikolojik bir kural koymaz.

Bağlanmış elin yönü de görüntünün kuruluşuna dahildir. {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} edatı {ar:عُنُقِكَ, tr:ʿunuqika, gloss:boynuna} sözcüğünü yönetir; boyun bağlama aracı değil, elin yöneldiği uç noktadır. Sözdizimi önce eli, sonra bağlanmış hâlini, ardından boyna doğru yönelişi verir; sahne bu son unsurla tamamlanır. İyelik eki boynu aynı muhataba bağlar; kısıt böylece kişinin kendi boynuna kapanan somut beden düzeninde belirir. Bu kuruluşun taşıdığı anlam elin kendi bedenine doğru kısıtlanmasıdır; yaralanma, yük ya da hastalık bu görüntüye eklenmez. {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} biçiminin edilgen ve dişil oluşu, taşıyıcının eril boyun değil dişil {ar:يَدَكَ, tr:yadaka, gloss:elini} olduğunu gösterir; biçim elin durumunu öne çıkarır, bağlayan faili ya da aracı belirtmez. Sözcüğün somut alanındaki demirden ya da ham deriden halka uzvu kuşatıp hareketini sınırlar. Boyunlara geçirilen halkaların çenelere kadar yükselerek kişileri başları kalkık tuttuğu sahne de bu bedensel kısıtı keskinleştirir (36:8). Bu temasın katkısı halka ve hareket sınırıdır; sahneler aynı olay ya da cezaya dönüşmez.

İlk yasaktaki el, ikinci harekette de aynı muhatabın elidir. {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} fiiline ekli dişil zamir yeniden {ar:يَدَكَ, tr:yadaka, gloss:elini} sözcüğüne döner; aynı el iki karşıt hareketin nesnesidir. Bu tekrar, organın bedensel işlevini koruyup elin iş görme ve başkasına erişme kapasitesini de açar. İyelik eki eli muhataba bağlar; malı ayrıca adlandırmaz. Böylece sorumluluk ve verme yankısı somut elde kalır, el de sabit bir “kişinin işleri” deyimine dönüşmez.

İkinci yasak ilkini dilbilgisel olarak karşılar: {ar:وَ, tr:wa, gloss:ve} ile gelen ayrı {ar:لَا, tr:lā, gloss:sakın}, bu kez {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} fiilini yönetir. Paralellik iki ayrı yasağı bir çift hâlinde duyurur; her fiil kendi el düzenini taşır, aralarında bir orta ölçü ya da göreli ağırlık sırası kurulmaz. Kabul edilmiş kıraat varyantının ses vurgusu uzatmayı daha belirgin duyurabilir; bu katkı sözdizimini, zamanı ya da aynı el olan nesneyi değiştirmez.

Uzatmanın ilk görüntüsü bedenseldir: {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} eli hareket alanına çıkarır; {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatmayı} ise toplamanın karşısındaki yayma eylemini adlandırır. Fiil hareketi başlatır, onunla aynı yayma köküne dönen eylem adı bu hareketi ölçülebilir bir süreç hâline getirir. Aradaki {ar:كُلَّ, tr:kulla, gloss:bütününü} tekil biçimde olsa da kapsam bakımından bütün uzatma eylemini ölçer: yasak yalnızca harekete başlamaya değil, onu tam ölçüsüne kadar sürdürmeye uzanır. Kapsam, tek eylemin bütünlüğüdür; alıcı ya da aktarım başına ayrı bir kural, ömür boyu aktarımların toplamı veya sayısal bir eşik kurmaz.

## Sonuçta Kalan

Tam uzatma ölçüsünün ardından gelen {ar:فَ, tr:fa, gloss:böylece}, doğrudan {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturmak} fiiline bağlanır. Böylece iki ayrı el hareketi tek sonuç cümlesine varır; arada üçüncü bir yasak eylemi yoktur ve iki hareket birbirinin yerine geçmez. Oturmanın öznesi önceki fiillerdeki aynı örtük muhataptır. Biçim, gerçekleşmiş ve tamamlanmış bir çöküşü bildirmekten çok içine düşülebilecek bir sonucu açar. Buradaki {ar:تَقْعُدَ, tr:taqʿuda, gloss:oturmak} ayakta durmanın karşıtı olan bedensel oturuşu ve orada kalışı anlatır. 17:26'daki verme buyruğunun tetiklediği ayrı kullanım, beklenen aktarımı artık yapamama ve eylemden geri kalma gölgesini ekler (17:26); bu bağlantı bedensel oturuşu silmez ya da her oturuşu ret saymaz.

Ardından gelen {ar:مَلُومًا, tr:malūman, gloss:ayıplanmış} ve {ar:مَحْسُورًا, tr:maḥsūran, gloss:tükenmiş}, oturuşta taşınan iki ayrı hâli belirtir. İlki kınanmayı, ikincisi tükenmeyi getirir; birlikte oturuşa toplumsal ve maddi bir daralma boyutu katarlar, biri ötekini açıklayıp ortadan kaldırmaz. Sonucun tam uzatmanın hemen ardından gelmesi ikinci hareketle bağı öne çıkarır; ilk yasağın aynı kuvvette bir sonuç bağı kurduğunu göstermez. İki hâlin açtığı eylem daralması, hastalık, kalıcı yetersizlik ya da bir daha eylemde bulunamama tanısı değildir.

Eril edilgen {ar:مَلُومًا, tr:malūman, gloss:ayıplanmış} biçimi kınanmayı aynı muhatabın üzerine yerleştirir; böylece toplumsal kenar görünür olurken kınayan kişi ya da merci açık kalır ve resmî bir yargı kurulmaz. Sözcüğün alanı ayıplanan davranışın kişiye yüklenmesini taşır. İçten öz-kınama mümkün bir karşı-okuma olarak kalır, ancak yerel yapı onu seçmez; biçim kınanmanın hak edilmişliğini de belirlemez.

Ayrı bir yasaktan sonra oturup kınanma ve yardımsız kalma sonucunun belirmesi, odaktaki sonucu bir sorumluluk yankısına yaklaştırır (17:22). Bu paralellik sonuç kalıbındadır; yasakların gerekçeleri ayrı kalır ve somut el eylemde kullanılan araç olarak sorumlulukla ilişkilendirilir (17:22). “Ellerin yaptığı ya da kazandığı” anlamındaki özel deyim ise ayrı bir yapıdır; odaktaki el bu deyime dönüşmeden sorumluluk yankısını taşır.

Aynı kınanmışlık çerçevesi başka bir yasaktan sonra da kullanılır: Allah ile birlikte başka bir ilah edinmeme buyruğunun ardından {ar:مَلُومًا مَّدْحُورًا, tr:malūman madhūran, gloss:kınanmış ve kovulmuş} sonucu gelir (17:39). Odaktaki {ar:تَجْعَلْ, tr:tajʿal, gloss:hâle getirmek} eli bir duruma sokarken, bu fiilin ayrı kullanımı bir şeyi adlandırma ya da ona statü verme boyutu da taşır. 17:39'daki ifade hâle getirme olarak da yorumlanabildiği için, bu yankı odaktaki duruma sokma kuruluşunu koruyarak statü okumasını ekler (17:39). Ortak {ar:مَلُومًا, tr:malūman, gloss:ayıplanmış} kınanma bağını kurar; {ar:مَدْحُورًا, tr:madhūran, gloss:kovulmuş} ise kovulma sonucunu 17:39'a özgü olarak genişletir (17:39). Bu bağlantı, muhatabın eyleme gücünü gerçek bırakırken onu nihai ve sınırsız kudret saymayı sınırlar; iki yasağın gerekçeleri ayrı kalır.

Son sıradaki edilgen {ar:مَحْسُورًا, tr:maḥsūran, gloss:tükenmiş} eylemden sonra geriye kalan kapasiteyi öne çıkarır; sıralama sonucun sıklığını belirtmez. Sözcük, uzun çaba sonunda insanın ya da hayvanın gücünün azalmasını, iş görme yetisinin körelmesini ve tükenmesini anlatabilir. Tam uzatmanın ardından bu anlam, kınanmış oturuşta kalan kişiyi ve sürdürecek güç ya da imkânın azalmasını duyurur. Aynı tükenme eldeki mal veya başka bir imkânın bitmesine de açılır; odak ayet belirli bir mal hesabı, kayıp miktarı ya da kesin bir iç duygu belirlemez.

Koruyucu donanımdan yoksun kalma, {ar:مَحْسُورًا, tr:maḥsūran, gloss:tükenmiş} sözcüğünün başka bir dalıdır; tükenmeyi korunaksızlık olarak da duyurur. 17:27'deki {ar:ٱلْمُبَذِّرِينَ, tr:al-mubadhdhirīna, gloss:saçıp savuranlar} uyarısı bu kullanımı tetikleyince, ölçüsüz çıkış verenin koruyucu payını da azaltabilir (17:27). Bu korumasızlık yankısı pranganın el-boyun görüntüsüne eklenir; giysi ya da zırh odak sahnenin kendisi değildir. Sözlük alanındaki örtüyü kaldırıp altta kalanı görünür kılma dalı da kınanmış ve durağan sonuçtaki kapasiteyi açıkta kalmış gibi duyurur. Bu dalın katkısı savunmasızlığın görünmesidir; gerçek bir soyunma sahnesi kurmaz.

Tükenen kaynağa duyulan acı, savurma uyarısının yanında bir pişmanlık yankısı da açar (17:27). Allah'ın yolunu engellemek için yapılan harcamanın ardından gelen pişmanlık ve yenilgi, geri gelmeyen imkânın kaybını görünür kılar (8:36). Bu tepkiyi adlandıran {ar:حَسْرَةً, tr:ḥasratan, gloss:kayıp ardından derin pişmanlık}, odaktaki edilgen {ar:مَحْسُورًا, tr:maḥsūran, gloss:tükenmiş} biçiminden ayrıdır. Böylece kayıp ardından duyulan acı, bitkinliğe mümkün bir yan anlam olarak katılır; pişmanlık 17:29'da açıkça bildirilmez ve kaçınılmaz da kılınmaz (17:27, 8:36).

{ar:كُلَّ, tr:kulla, gloss:bütününü} ile {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatmayı} birlikteliği tek uzatma eyleminin tamamını ölçer; bu bütünlük, sonrasında kalan kapasiteyi düşünmeye zemin verir. Aynı kök alanındaki ayrı bir fiil, {ar:كَلَّ السَّيْفُ, tr:kalla al-sayfu, gloss:kılıç keskinliğini yitirdi}, kılıcın körelmesini ve insanın ya da hayvanın iş görme gücünün azalmasını anlatır. Bu kapasite kaybı yankısı {ar:مَحْسُورًا, tr:maḥsūran, gloss:tükenmiş} ile buluşur; kılıcın körelmesi ve güç azalması, bütünlük belirtecinden ayrı bir fiil biçimine aittir. 17:36'da işitme, görme ve gönül ile bunların tümü sorgulanır; 17:38'de de bütün bunlar hesap ve değerlendirme çerçevesine girer (17:36, 17:38). Bu yetilerin sorumluluk alanıyla yan yana gelişi, tam bir seferlik açılmanın daha sonra gereken kapasiteyi azaltabileceği okumasını mümkün kılar. Yorgunluk bu bağlamda bir sonuç yankısıdır, bütünlük belirtecinin dilbilgisel anlamı değil.

Bedensel uzatma, erişimin sonlu ölçülerini de görünür kılar. Dağlara boyca ulaşma ve yeri yarıp geçme insanın aşamayacağı iki sınırdır; aynı bağlam kibirli yürüyüşü konu eder (17:37). {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatmanın} sağlanan dar kullanımlarından biri bir geçitte katedilen mesafeyi, diğeri ayakta duran kişinin elini yukarı uzatınca eriştiği yüksekliği anlatır. Bu kullanımlar {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} hareketini bedensel erişim olarak keskinleştirir: el tümüyle açılsa bile erişim bedenin sınırları içindedir. Bu karşılaştırma uzatmanın fiziksel imgesine insan erişiminin sonluluğunu ekler; 17:37'deki yürüyüş sınırı ise harcamanın ölçüsü değildir (17:37).

## Elin Yönü ve Hakkın Akışı

Karşıt bağlamlar elin uzanışına farklı yönler verir. Bir sahnede kişi öldürmek için elini uzatırken öteki aynı amaçla elini uzatmayı reddeder (5:28); başka bir bağlamda açık ve harcayan eller belirir (5:64). Bu kullanımlar {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} ve {ar:يَدَكَ, tr:yadaka, gloss:elini} ile kurulan bedensel uzatmayı kaynak aktarımı ile zarar verme yönleri arasında açar (5:28, 5:64). Böylece odaktaki uçlar miktarın yanında elin erişimini ve yönünü de düşündürür; saldırı yönü 5:28'e aittir, 17:29'a taşınmaz.

{ar:يَد, tr:yad, gloss:el} için ayrı bir kullanım başkasına ulaştırılan iyiliği ya da karşılık beklemeyen yararı adlandırabilir. Harcama bağlamı bu yararı odaktaki {ar:يَدَكَ, tr:yadaka, gloss:elini} ile buluşturur: uzanan el, faydayı başkasına eriştirebilecek bir imkân gibi duyulur (5:64). Bağ, sözcük tekrarından değil, harcamanın yararı başka birine ulaştırmasından doğar. Bu özel yarar borç, satış ya da karşılıklı ödeme biçiminde değildir; odak ayette belirli bir alıcı ve tamamlanmış aktarım gösterilmez.

Elin yönü, önce hak sahibine ulaştırma buyruğuyla somutlaşır: yakına, yoksula ve yolda kalmışa {ar:ءَاتِ, tr:āti, gloss:ver} sözüyle {ar:حَقَّهُۥ, tr:ḥaqqahu, gloss:hakkını} verme çağrısını {ar:لَا تُبَذِّرْ تَبْذِيرًا, tr:lā tubadhdhir tabdhīran, gloss:saçıp savurma} yasağı izler (17:26, 17:27). Bu sıra, 17:29'daki eli sahibinin tuttuğu kaynağın yanı sıra hak sahibine erişebilecek bir kanal olarak da duyurur. {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} el bir erişim boğumuna, {ar:يَدَكَ, tr:yadaka, gloss:elini} ise malın elden ele ulaşmasını sağlayan bedensel araca dönüşebilir. Verme ve hak bağlamının tetiklediği bu doğrudan aktarım yankısı satış ya da nakit ödeme kurmaz; bu özel bağlantı da her maddi kısıtın mutlaka bir hakkı kestiğini söylemez.

Hakkın önce gelmesi, bazı çıkışların isteğe bağlı cömertlik değil yerine getirilecek yükümlülük olduğunu gösterir; ardından gelen savurma yasağı elde kalan imkânın israfa dönmesini sınırlar (17:26, 17:27). Bu sıra bu iki ayetin yerel düzenidir, evrensel muhasebe formülü değil (17:26, 17:27). İki uç dolaşımdaki kapasiteyi farklı biçimde etkiler: el bütünüyle kapanırsa hak sahibine erişemeyebilir, bütünüyle açılırsa verenin sürdürme gücü tükenebilir. Sonucun tam açmadan hemen sonra gelmesi ikinci bağı daha doğrudan duyurur. Gelecekteki ihtiyaca yetecek kapasitenin azalması makul bir yankıdır; ihtiyaç ise bağlama eklenen bir çerçevedir ve ayet hedef miktarı, alıcıyı ya da iki yasağın eşit sonuç derecesini belirlemez.

Harcamanın ulaşabileceği kişiler başka bir bağlamda anne baba, yakınlar, yetimler, yoksullar ve yolda kalmışlar olarak sayılır (2:215). {ar:يَد, tr:yad, gloss:el} için başkasına ulaştırılan iyilik ve yarar anlamı bu listeyle toplumsal bir yön kazanır; {ar:يَدَكَ, tr:yadaka, gloss:elini} ile taşınan verme kapasitesi bu ihtiyaç sahiplerine fayda ulaştırabilir (2:215). Liste yararlanıcıları somutlaştırır, ancak sabit bir öncelik sırası, kişi başına miktar ya da hakları ödeyip ardından yedek ayırma kuralı belirlemez (2:215). İyilik yönü görünür olurken odaktaki el somut uzuv, verenin imkânı da değişebilen bir sınır olarak kalır.

## Maddi Sınır, Açık İlişki

Maddi aktarımın yanında anne babaya {ar:إِحْسَٰنًا, tr:iḥsānan, gloss:iyilikle davranma} buyruğu bakımın tek seferlik bir miktara indirgenmediğini gösterir (17:23). {ar:جَنَاحَ ٱلذُّلِّ, tr:janāḥa al-dhulli, gloss:alçakgönüllülük kanadı} koruyup saran ve buyurmayan bir alçalış sunar; merhamet ve merhamet etme çağrısı da bakımın duygusal yönünü açar (17:24). Bu imgeler, {ar:ٱلرَّحْمَةِ, tr:ar-raḥmati, gloss:merhamet} ve {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} sözleriyle birlikte, {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} elin maddi hareketi sınırlıyken de ilişkinin bakım yoluyla sürebileceğini gösterir (17:24). Bu ilişki katkısı maddi hakkın kendiliğinden karşılandığı anlamına gelmez; bakım ile kaynak aktarımı yan yana durur (17:23, 17:24).

Yardımın mümkün olmadığı anda ilişkiyi nasıl açık tutacağına ayrı bir yanıt verilir (17:28). Merhamet umarak talep sahibinden geçici biçimde geri durma ihtimalini {ar:تُعْرِضَنَّ, tr:tuʿriḍanna, gloss:yüz çevirirsen} açar; ardından ona kolay bir söz söyleme buyruğu gelir: {ar:فَقُل لَّهُمْ قَوْلًا مَّيْسُورًا, tr:fa-qul lahum qawlan maysūran, gloss:onlara kolay bir söz söyle} (17:28). Bu sıra, maddi imkânın sınırlılığını ilişkiden çekilmekten ayırır. {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} ve {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatma} için sağlanan başka bir kullanım rahat ve açık toplumsal davranışı, kimi kalıplarda yüzde görünen açıklığı anlatabilir; kolay söz bu sosyal açıklığı bağımsızca tetikler (17:28). Bu yankı ilişkiyi açık tutar, fiile “güzel konuşmak” anlamını vermez. 17:28'in bu durumu geçici geri duruşla ilgilidir; her geri çevirme geçici sayılmaz ve söz maddi hakkı karşılamaz (17:28).

Eldeki imkânın değişmesi, geçimliği {ar:يَبْسُطُ, tr:yabsuṭu, gloss:genişletir} ve {ar:وَيَقْدِرُ, tr:wa-yaqdiru, gloss:daraltır} bağlamıyla görünür (17:30). Buradaki genişlik miktar ve kapasiteyle ilgilidir; 17:29'daki {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} fiziksel hareketi ve {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatmanın} eylem adından ayrılır. Rızkın genişleyip daralması, eldeki imkân zarfının sabit olmadığını ve ölçünün duruma göre değiştiğini düşündürür (17:30). Bu karşılaştırmanın katkısı değişen kapasitedir; odak fiilini geçimlik miktarıyla özdeşleştirmez ve herkese ortak bir oran belirlemez.

Yoksulluk korkusuyla çocukları öldürmeme buyruğu ve çocuklara da size de rızık verileceği sözü yan yana gelir (17:31). {ar:خَشْيَةَ إِمْلَٰقٍ, tr:khashyata imlāqin, gloss:yoksulluk korkusuyla} boş el imgesini etkinleştirir; bu imge {ar:يَدَكَ, tr:yadaka, gloss:elini} karşısına elde hiçbir şey kalmama endişesini koyar (17:31). Yoksulluk imgesi, {ar:مَغْلُولَةً, tr:maghlūlatan, gloss:bağlanmış} elin başka bir sözlük anlamı değil, bu korku bağlamının katkısıdır. Böylece boyna kapanan el kıtlık beklentisine karşı savunmacı bir kapanış gibi duyulabilir; çocukların yaşam imkânına yönelen baskı da görünür olur (17:31). Çocukları öldürme yasağıyla bağlı el özdeş eylemler değildir. {ar:وَلَا تَقْتُلُوا أَوْلَٰدَكُمْ, tr:wa-lā taqtulū awlādakum, gloss:çocuklarınızı öldürmeyin} buyruğunu, çocuklara ve size rızık verileceği sözü izler: {ar:نَّحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:naḥnu narzuquhum wa-iyyākum, gloss:onlara da size de rızık veririz} (17:31). Bu güvence, insan elinin gelecekteki her payın tek kaynağı olduğu varsayımını gevşetir; bağlamsal okuma her yedek birikimini panik saymaz (17:31).

Kaynak korkusu, rahmet hazinelerinin insanların elinde olduğu varsayılan bollukta da harcama endişesi olarak belirir (17:100). Bu karşı-imge gösterir ki, korku yalnızca kaynak yokluğundan doğmaz. Odaktaki {ar:مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlanmış} eli bu bağlamda kaynak çıkışını kapatan iç baskı ve cimri tutum olarak da duyulabilir: kaybı önleme isteği kişinin kendi elini kısıtlar (17:100). Bu özel yankı bedenî bağı korur; gizli el koyma ya da iç kin isnat etmez ve sınırsız vermeyi öğütlemez.

Savurganlıkla eli sıkı tutma arasında ölçülü kalma çağrısı iki ucu ve aralarındaki orta yolu görünür kılar (25:67). Bu bağlam, kapasite ve miktar genişliği bildiren ayrı {ar:ٱلْبَسْطِ, tr:al-basṭi, gloss:uzatmanın} kullanımını etkinleştirir; böylece fiziksel yayma eylemine nicelik boyutu eklenir, fiil sabit bir miktara dönüşmez (25:67). Harcananın yerine konması aynı tutarın bire bir geri geleceğini vaat etmez (34:39). İmkânı geniş olanın genişliğine, rızkı dar olanın kendisine verilene göre harcaması ise ölçüyü mevcut koşula bağlar (65:7). Birlikte bu bağlamlar herkese ortak bir orta miktar yerine değişen imkâna cevap veren sınır sunar; kesin bir geri ödeme oranı ya da sayısal eşik belirlemez (25:67, 34:39, 65:7).

## Yetki ve Emanet

El, bazı özel kullanımlarda beden gücünün yanında buyruk ve yön verme yetkisini de taşıyabilir (17:33); bu bağlam odaktaki {ar:يَدَكَ, tr:yadaka, gloss:elini} imgesinin bedensel zeminini değiştirmez. Haklı eylem, verilmiş yetki ve aşmama sınırı ayrı ayrı kurulur: {ar:بِٱلْحَقِّ, tr:bil-ḥaqqi, gloss:hakkıyla}, {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} ve {ar:يُسْرِف, tr:yusrif, gloss:aşırıya gitmek} (17:33). Bu yan yana geliş, kapasitenin felce uğratılmadan sınırlandırılabileceğini ve meşru eylemin sürdüğünü düşündürür. {ar:تَبْسُطْهَا, tr:tabsuṭhā, gloss:elini uzatmak} için sağlanan özel kalıp, eli ya da kolu istemek, almak, vurmak veya vermek üzere uzatmayı anlatabilir; hareketin yönünü bağlam belirler, uzatma tek başına cömertlik ya da zarar anlamını seçmez (17:33). Öldürmeye ilişkin bu hüküm 17:33'ün kendi sınırında kalır, harcamaya yönelik hukuk kuralı oluşturmaz.

Elde tutulan imkân, yetim malı, ahit ve ölçüyle dışsal bir hesaba bağlanır: {ar:مَالَ ٱلْيَتِيمِ, tr:māla al-yatīmi, gloss:yetimin malı} ile ahdi yerine getirme çağrısını {ar:ٱلْكَيْلَ إِذَا كِلْتُمْ, tr:al-kayla idhā kiltum, gloss:ölçüyü ölçtüğünüzde tam verin} ve {ar:وَزِنُوا بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ, tr:wa-zinū bil-qisṭāsi al-mustaqīmi, gloss:doğru teraziyle tartın} buyrukları izler (17:34, 17:35). Bir şeyin birinin “elinde” bulunmasını anlatan sahiplik ve denetim kullanımı bu yetim malı ve tartı bağlamıyla etkinleşir; odaktaki yalın iyelikli {ar:يَدَكَ, tr:yadaka, gloss:elini} kendi başına bu deyim değildir (17:34, 17:35). Kaynağı elinde tutan kişi onu yönetebilir, fakat nihai yararlanıcı her zaman kendisi değildir; yetim de korunacak kişi ve aktarımın muhatabıdır (17:34, 17:35). {ar:وَأَوْفُوا بِٱلْعَهْدِ, tr:wa-awfū bil-ʿahdi, gloss:ahdi yerine getirin} yükümlülüğün bitip bitmediğine sahibin tek başına karar vermesini sınırlar (17:34). Ölçü ve terazi, iki uç arasında sezilen orta miktarı denetlenebilir karşılığa bağlar (17:35). Bu temas dışsal hesap verebilirlik ekler; odaktaki el tartı anlamına gelmez ve bu bağlam bütün kaynakları yetim malı, her mal sahibini de hukukî vekil saymaz (17:34, 17:35).

Ahit çağrısı, {ar:يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:yadaka maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlanmış} görüntüsüne elin güvence olarak verilmesini anlatan ayrı bir kullanımı ekler: böyle bir söz borç ya da yükümlülük üstlenmeyi anlatabilir (17:34). Bu taahhüt yankısı elin kapasitesini mülkiyetin yanı sıra sözle de sınırlar; boyun eğme anlamından ve düz el adından ayrıdır. Bağlantı 17:34'ün ahit bağlamına aittir; 17:29'un kendi görüntüsü akit ya da hukukî rehin kurmaz.

İnsan elinin kaynakların yönünü etkilemesi, son dağıtım yetkisinin nerede bulunduğu sorusunu açar (57:29). Nimet ve iyiliği dağıtma yetkisi Allah'a aittir (57:29). Açık ve harcayan ellerle birlikte düşünüldüğünde, {ar:يَدَكَ, tr:yadaka, gloss:elini} kaynağın yönünü etkileyebilen, ama son dağıtım kararını taşımayan sınırlı insan gücü olarak duyulur (5:64, 57:29). İnsanlara bırakılan malı harcamaları da emanetçilik olarak çerçevelenir (57:7). {ar:يَد, tr:yad, gloss:el} için sağlanan iş görme ve elde tutup yöneltme yeterliği bu emanet fikrine temas eder; bu temas emanet kavramını elin sözlük anlamına dönüştürmez ve mutlak sahiplik iddiasını desteklemez (57:7). Bu bağlamlar belirli bir alıcıyı adlandırmaz.

## Yardımla Taşınan Kapasite

Elin iş görme gücünün kaynağı sorusu yardım dileme sözüyle açılır: {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım dileriz} (1:5). {ar:يَد, tr:yad, gloss:el} için sağlanan ayrı kullanım beden organından değil, işi yapmaya yarayan güç ve yeterlikten söz eder; bu anlam düz {ar:يَدَكَ, tr:yadaka, gloss:elini} adına taşınmaz. Güçlendirme ya da gücün yetmemesi bildiren özel sözler de kendi kalıplarında kalır. Yardım dileme bu yeterlik kullanımını tetiklediğinde, odaktaki elin kapasitesi etkin ama kaynağı kendisi olmayan bir güç gibi duyulur (1:5). Bu okuma Fātiḥa'daki tek bir ifadeye bağlıdır; miktar, alıcı ya da bütçe kuralı eklemez ve sûrenin tamamı adına konuşmaz. El iş görür, fakat gücü kendinden kaynaklanan, kendi kendine yeten bir imkân olarak kapanmaz.

</source_prose>
