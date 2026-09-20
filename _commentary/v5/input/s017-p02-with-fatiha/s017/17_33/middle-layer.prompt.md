# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:33**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.middle.claims.json`

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
- Refer to source paragraphs as `17:33 ¶N`.

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

`(17:33 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:33",
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
        "citation": "(17:33 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_33/17_33.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_33/17_33.middle.claims.json \
  --ayah-ref 17:33
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_33/17_33.prose.editorial.tr.md`

<source_prose>
## Canın Dokunulmazlığı

Ayetin açılışındaki {ar:لَا تَقْتُلُوا۟, tr:lā taqtulū, gloss:öldürmeyin} topluluğun tümüne yöneltilmiş ortak bir öldürme yasağıdır. Cezmli ikinci çoğul muzari biçimi sorumluluğu bütün muhataplara taşır. {ar:تَقْتُلُوا۟, tr:taqtulū, gloss:öldürmek} yalın I. kalıpta can almayı anlatır; kökün daha geniş yıkım çağrışımı ve daha yoğun anlam verebilen II. kalıp, yerel yasağı can almanın kendisinden başka bir eyleme daraltmaz. Açık nesne olan {ar:ٱلنَّفْسَ, tr:an-nafsa, gloss:yaşam taşıyan kişi}, korunacak şeyi soyut bir dava değil, hayat taşıyan kişiyi kılar.

{ar:ٱلنَّفْسَ, tr:an-nafsa, gloss:yaşam taşıyan kişi} sözü hem bedene yaşam veren canı hem bu canı taşıyan ayrı bireyi düşündürebilir; belirli tekil biçim bir kişiye olduğu kadar korunan hayat sınıfına da açılır. Soluk alıp verme çağrışımı, öldürmenin sona erdirdiği canlılığı somutlaştırarak yaşayan kişiyi korumanın odağına getirir. Bu, sözcüğün anlam alanındaki bir yankıdır; tüketici bir tanım ya da metafizik bir ruh açıklaması değildir. Böylece doğrudan öldürme fiiline bağlanan nesne, korumanın yaşayan kişiye yöneldiğini baştan duyurur.

Bu yaşayan kişi, dişil ilgi zamiri {ar:ٱلَّتِى, tr:allatī, gloss:-dığı} ile gelen cümlecikte nitelenir: zamir yeniden {ar:ٱلنَّفْسَ, tr:an-nafsa, gloss:yaşam taşıyan kişi}ya döner; tamamlanmış II. kalıp {ar:حَرَّمَ, tr:ḥarrama, gloss:dokunulmaz kıldı} fiilinin öznesi {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah}, nesnesi candır. Böylece dokunulmazlık, muhataplara yöneltilen yasaktan önce kurulmuş ilahî bir eylem olarak görünür. H-r-m sözcük ailesindeki yasaklama, kutsallık ve çiğnenmemesi gereken saygınlık ya da korunmuş hak çağrışımları burada yaşayan kişiye dönük korumayı duyurur: tamamlanmış fiil kişiyi ihlal edilemez bir sınır yapar. Bu bağlantı bu kişi merkezli kullanıma aittir; hükmü kutsal bir mekâna ya da belirli bir sözleşmeye taşımaz. Aynı ilahî kaynak biraz sonra veliye yetki verir; bu atama, önceden kurulan hayat korumasının içinde okunur.

Bu korumanın ardından gelen {ar:إِلَّا بِٱلْحَقِّ, tr:illā bi-l-ḥaqqi, gloss:ancak hak gereği} öldürme yasağının istisnasını dar bir hak ölçüsüne bağlar. Belirli {ar:ٱلْحَقِّ, tr:al-ḥaqqi, gloss:hak ve gerçeklik} hem gerçekte doğru olanı hem yükümlülüğü, hak edilmiş payı ve bir sahibin ileri sürebileceği istemi duyurur; {ar:بِ, tr:bi, gloss:hakka dayanarak} bağı da “hak üzerinden”, “hakla birlikte” ya da “hakkın gereği olarak” okunabilir. Bu yolların her birinde ölçü kişisel saik değil, bağlayıcı olması gereken haktır; bir iddiaya hak denmesi onu kendiliğinden hakka dönüştürmez. Ayet bu koşulun kapsadığı bütün vakaları veya her vakada uygulanacak usulü saymaz. Ardından gelen {ar:وَ, tr:wa, gloss:ve} yeni bir şart cümlesi açar: giderim istisna öbeğine eklenmiş bir izin değil, haksız öldürülme gerçekleştiğinde devreye giren ayrı bir hükümdür; fiziksel giderim olasılığı bu dilde açık kalır.

## Mağdurun Hakkı ve Yetki

Bu yeni şartta {ar:مَنْ, tr:man, gloss:her kim} soy, ad, cinsiyet ya da toplumsal sınıfla daraltılmayan özneyi kurar; {ar:قُتِلَ, tr:qutila, gloss:öldürüldü} ise açılıştaki etkin öldürme yasağını mağdurun başına gelmiş tamamlanmış olaya çevirir. Edilgen fiil öldüreni adlandırmaz; dikkati önce failin kimliğine değil, öldürülen kişinin durumuna verir. O durumu {ar:مَظْلُومًا, tr:maẓlūman, gloss:haksızlığa uğramış halde} belirler: mansup edilgen ortaç, kişinin olay sırasındaki hâlini niteler ve şartı her öldürmeye yaymaz. Bu seyrek niteleme mağduriyeti cümlede belirginleştirir; seyrekliği tek başına bir sıklık hesabı değildir. Z-l-m alanındaki yerinden, payından ya da uygun ölçüsünden çıkarma anlamı, önceki {ar:ٱلْحَقِّ, tr:al-ḥaqqi, gloss:hak ve gerçeklik} ve verilecek {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} ile birleşince haksızlığı genel bir sıkıntıdan çok hak edilmiş ölçünün bozulması olarak duyurur. Yakınma ve hakkını geri isteme çağrışımı, mağduriyeti temsil yoluyla ileri sürülebilir bir talebe yaklaştırır. Bu bağlantı niteleyicinin anlam alanında kalır: ortaç doğrudan “şikâyetçi” demez ve öldürüleni etkin bir öz-yardım buyruğunun faili yapmaz.

Şartın cevabındaki {ar:فَقَدْ, tr:fa-qad, gloss:öyleyse kesinlikle} geçişi ve pekiştirici {ar:قَدْ, tr:qad, gloss:kesinlik bildirici}, tamamlanmış {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir konuma atadık} fiilini koşul gerçekleştiğinde kurulmuş bir atamaya bağlar. Birinci çoğul şahıs ilahî kaynağı duyurur; fiil burada alıcıyı ve verilen şeyi belirleyerek temsilciye bir konum verir. Bu atama kişiyi yoktan var etmek ya da ham, sınırsız güç yaratmak değildir. Öne alınan {ar:لِ, tr:li, gloss:yararına} önce {ar:وَلِيِّهِۦ, tr:waliyyihī, gloss:öldürülenin velisi}, sonra verilen {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} ile bağ kurar. Bu sıralama, yetkinin kimin yararına ve kime verildiğini aynı hareket içinde belirler.

İyelik eki {ar:وَلِيِّهِۦ, tr:waliyyihī, gloss:öldürülenin velisi} sözünü öldürülen kişiye bağlar. Wali yakınlık ve gözetimin yanı sıra bir başkasının işini üstlenip yürütmeyi, onun adına sorumluluk almayı ve daha uygun ya da hak sahibi olmayı da taşıyabilir. Atama ve sultanla yan yana geldiğinde bu yakınlık, mağdurun talebini izleyen sorumlu temsile dönüşür: işi veli yürütür, hakkın kaynağı yine mağdurdur. Bu yüzden veli yalnız duygusal bir yakın ya da belirsiz bir öç alıcılar topluluğu değildir. Bağ akrabalık, komşuluk veya azat ilişkisi olabilir; sözcük tek başına belirli bir akrabalık derecesi, miras kuralı ya da modern bir makam seçmez. Temsilci iddiayı taşır, hakkın sahibini değiştirmez.

Verilen {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} belirsiz tekil ve mansup bir addır; {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir konuma atadık} fiilinin nesnesi olarak başkaları üzerinde etkili olabilecek güç ve tanınmış bir hakkı kullanma kapasitesi taşır. Aynı söz üstün gelen kanıtı ya da iddiayı taşıyan hukuki dayanağı da düşündürebilir; bu olasılık, {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} koşuluyla mağdurun ileri sürülebilir hakkı arasında bağ kurar, fakat etkili kapasite anlamını ortadan kaldırmaz. Başka bir sahnede cezalandırma veya öldürme tehdidi açık bir dayanak getirme koşuluna bağlanır (27:21); bu sahne zorlayıcı etkiyle kanıt talebini birlikte duyurur. Buradaki bağlantı farklı aktörlerin sahnesinden kurulan bir analojidir, 17:33 için hukuk kuralı koymaz. Allah’ın indirmediği bir dayanakla ortak koşmanın ve Allah hakkında bilgisizce konuşmanın reddi de kanıt ve bağlayıcı gerekçe yönünü aydınlatır (7:33). Bu okumalar velinin hangi delili sunacağını, hangi usulün uygulanacağını belirlemez; yetkinin fiziksel giderim kapasitesi de açık kalır.

Bu kapasitenin hemen ardından {ar:فَلَا, tr:fa-lā, gloss:böylece yapmasın} gelir: {ar:فَ, tr:fa, gloss:böylece} açıklama ya da sonuç ilişkisi kurabilir, ama her iki okumada da atama ile sınır arasında boşluk bırakmaz. Yasaklayıcı {ar:لَا, tr:lā, gloss:yasak} ve IV. kalıbın cezmli üçüncü tekil eril fiili {ar:يُسْرِف, tr:yusrif, gloss:ölçüyü aşmak}, ilk öldürmeme buyruğunu yankılayan bağlayıcı bir sınır koyar. Karşılaştırmada görülen {ar:يُسْرِفُ, tr:yusrifu, gloss:ölçüyü aşar} bildirme biçimiyle {ar:تُسْرِفْ, tr:tusrif, gloss:ölçüyü aş} doğrudan hitabı, odaktaki üçüncü şahıs yasağının kuvvetini değiştirmez. Fiilin temel ölçüsü uygun sınırı aşmaktır. Daha uzaktaki yanılma ya da hedefi şaşırma çağrışımı, yanlış kişiye yönelen giderime karşı ek bir ihtiyat kurar; bu bağlantı olağan aşırılık anlamının yerine geçmez ve hakkı ortadan kaldırmaz.

Sınırın uygulandığı alanı {ar:فِى, tr:fī, gloss:içinde} edatıyla gelen belirli {ar:ٱلْقَتْلِ, tr:al-qatli, gloss:öldürme} mastarı adlandırır; mastar doğrudan nesne değil, düzenlenen eylem alanıdır. Birlikte, aşmanın öldürmenin içinde, bu mesele hakkında ya da öldürme nedeniyle gerçekleşmesi seçeneklerini açık tutarlar; her durumda sınır öldürme ve giderim alanına bağlıdır. Belirli ad hem az önceki öldürme olayına dönebilir hem de öldürme türünü genelleyebilir. Kökün sırası önce topluluğa yöneltilen etkin {ar:لَا تَقْتُلُوا۟, tr:lā taqtulū, gloss:öldürmeyin} yasağında, sonra mağdurun edilgen {ar:قُتِلَ, tr:qutila, gloss:öldürüldü} olayında, en sonunda düzenlenen isimleşmiş {ar:ٱلْقَتْلِ, tr:al-qatli, gloss:öldürme} alanında belirir. Böylece başta korunan hayat, veliye tanınan giderimin de ölçüsü olarak kalır.

## Komşu Buyruklarda Ölçü

Bu ölçü, yakınlara ilişkin buyruklarda bakım ve özdenetim yönü kazanır. Ebeveyne iyilik ve saygın söz söyleme buyruğu, velilikle kurulabilecek bir akrabalık çerçevesi sunar (17:23); bu bağlantı her velinin kan bağı taşıdığı anlamına gelmez. Güçlü olanın merhametten “tevazu kanadını indirmesi” bedensel imgesi, üstünlüğü azaltıp gücü yumuşak ve esnek kullanmayı anlatır (17:24). Buradaki {ar:ٱلذُّلِّ, tr:adh-dhull, gloss:tevazu} sözü merhametle biçimlenen özdenetimi adlandırır; aşağılanmayı değil. Aynı merhamet kanat imgesinde ve {ar:رَبِّ ٱرْحَمْهُمَا, tr:rabbi irḥamhumā, gloss:Rabbim ikisine merhamet et} duasında yinelenir (17:24). Yaşlı ebeveyne saygı, veliye verilen gücü kırılgan yakına dönük hesap verebilir gözetim olarak duymayı sağlar; ebeveyne ilişkin görev öldürme vakasındaki hukuki yükümlülüğün yerine geçmez, fakat aşmama ölçüsünü bakım sorumluluğuyla doldurur.

Bu gözetimin hak sahibiyle ilişkisi, yakına ait payın doğrudan ona verilmesinde belirginleşir: yakın akrabaya hakkını verme buyruğu (17:26), {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} ile duyulan isteme bir hamil kazandırır. Böylece veliye verilen {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki}, belirli bir talep sahibine bağlı görev olarak görünür; bu örnek velinin bütün kurumsal yetkilerini ya da miras derecelerini tarif etmez. Temsilci iddiayı taşıyabilir, fakat payın sahibi ve giderimin dayandığı hayat öldürülen kişiye bağlı kalır.

Yakına ait hakkın ardından kaynakları kullanma ölçüsü gelir. Savurganlığı bırakma buyruğu (17:26), serveti boşa saçmamayı ister; elin boyna bağlı tutulmasıyla bütünüyle açılması arasındaki karşıtlık (17:29) ise kısmakla tümüyle salmak arasına görünür bir sınır çizer. Rızkın genişletilip ölçülmesi (17:30), miktarın da bir ölçüye bağlı olduğunu ekler. Bu kaynak görüntüleri sultanı gerçek bir yönetim kapasitesi olarak bırakırken, onu amaç ve ölçüyle sınırlı bir hak gibi düşündürür. {ar:يُسْرِف, tr:yusrif, gloss:ölçüyü aşmak} fiilinin para, yiyecek ya da suyu yarar ve miktar dışında harcama yönündeki ayrı kullanımı bu ekonomik sahnelerde benzetme olarak etkinleşir; öldürme fiilinin çevirisine dönüşmez ve buradan belirli bir kısas miktarı ya da hukuki eşitlik çıkmaz.

Ayrı bir kullanımda öldürme kökü, içkiye su katıp karıştırarak sertliğini azaltmayı anlatır. Bu ayrıntının yanında bütünüyle açılmış el (17:29) kapasitenin serbest bırakılışını, rızkın genişletilip ölçülmesi (17:30) ise miktarın ayarlanışını düşündürür. Bu üç imgenin burada yan yana gelişi, karşılık gücünü geri döndürülemez bir öldürme itkisine dönüşmeden önce yumuşatma benzetmesi açabilir: el salıverişi, rızık anlatımı miktarın ayarını, içkiye su katma da sertliğin azaltılmasını taşır. Bu yalnızca kökün ayrı kullanımından kurulan bir benzetmedir; odaktaki {ar:تَقْتُلُوا۟, tr:taqtulū, gloss:öldürmek} ve {ar:قُتِلَ, tr:qutila, gloss:öldürüldü} biçimleri ile {ar:ٱلْقَتْلِ, tr:al-qatli, gloss:öldürme} mastarı olağan can alma anlamını korur, iki komşu ayette içki ya da su geçmez. Bu bağlantının katkısı eylem sonrası hesap değil, şiddetin yoğunluğunu eylemden önce azaltmanın koruyucu değeridir.

Yakın bağlamdaki başka bir öldürme örneği, gerekçe ile ihtiyacı karşı karşıya getirir. Çocukları yoksulluk korkusuyla öldürmeme buyruğu (17:31), öldürme yasağını yineler; {ar:خَشْيَةَ, tr:khashyata, gloss:korku} beklenen sıkıntıyı, {ar:إِمْلَٰقٍ, tr:imlāq, gloss:yoksulluk ve kaynak darlığı} gelecekteki kıtlığı adlandırır. Buna karşılık “onları da sizi de biz rızıklandırırız” güvencesi anne babaları ve çocukları birlikte kapsar; ardından bu öldürme “büyük suç” diye nitelenir (17:31). Bu örnekte korku ya da hesaplanan yarar, {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} koşulunu tek başına karşılayamaz. Örnek çocukların yoksulluk korkusuyla öldürülmesiyle sınırlıdır; bütün hak durumlarının ölçütünü vermez.

Bu koruma, son öldürme anının çevresindeki yaklaşma sınırlarıyla yan yana gelir. Zinaya yaklaşmama buyruğu (17:32) ve yetim malına yalnız en iyi yolla yaklaşma koşulu (17:34), aynı “yaklaşma” fiilini cinsel alan ve korunmasız kişinin malı gibi ayrı menfaatlere yöneltir. Yetimin anılması velisi bulunmayan kırılgan kişiyi de koruma görüntüsüne katar; bu koruma yalnız yetimlere özgü değildir. Yetim malına en iyi yolla erişme koşulu, {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} ile korunan bir alana erişimin sınırlanması bakımından buluşur, ancak iki koşul aynı hukuki test değildir. Odaktaki {ar:حَرَّمَ, tr:ḥarrama, gloss:dokunulmaz kıldı} kişinin dokunulmazlığını kurarken, aynı sözcük ailesinin kutsal şehir ya da çevresini korunan mekân olarak anlatan ayrı kullanımı bu yaklaşmama sınırlarına mekânsal bir benzetme katar. Bu mekânsal benzetme canı son zarardan önce de korunan alanlar örüntüsü içinde görünür kılar; burada kurulan bağlantı, komşu buyrukların kendi hükümlerini cinayeti önleme kuralı diye tanımlamaz.

Erişim sınırından sonra alışveriş sahnesi ölçüyü gözle görülür kılar. Ölçüyü tam verme ve dosdoğru teraziyle tartma emirleri (17:35), ticari işlemi eksiksiz ölçmeye bağlar; {ar:ٱلْقِسْطَاسِ, tr:al-qisṭās, gloss:terazi} kişisel tahmin yerine herkesçe incelenebilir bir alet sunar. {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīm, gloss:dosdoğru} niteliğinin düzlük imgesi de {ar:يُسْرِف, tr:yusrif, gloss:ölçüyü aşmak} yasağını ve {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} koşulunu eğrilmeyen ölçüyle buluşturur; bu ihtiyatlı bir benzetmedir, bağımsız bir teknik hukuk terimi değildir. Sahnenin kendisi ticari ölçüyle ilgilidir; bu bağlantı terazi imgesini cinayet mahkemesi, öldürmeye özgü sayısal eşik, kan hesabı ya da başka canları birbirinin yerine sayma kuralı yapmaz. Uygun sınırı aşma anlamı, sorumlu faili aşıp başka birine yönelen giderimi de olası bir sınır ihlali olarak düşündürebilir; bu, {ar:يُسْرِف, tr:yusrif, gloss:ölçüyü aşmak} için bağlamsal bir özelleştirmedir, belirli bir olayın hükmü değildir.

Görünür ölçünün yanına, bilginin hesabını veren buyruk eklenir. Bilmediğinin peşine düşmeme uyarısı ve işitme, görme, gönlün sorgulanacağı bildirimi (17:36), bilgi toplayan kanalı, ayrı bir yeti olan görmeyi ve iç muhakemeyi birlikte sorumluluğa bağlar. Böylece veliye tanınan {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} kuvvet kullanılmadan önce bilinebilen olgulara cevap vermesi gereken bir kapasite olarak da duyulur; üstün gelen kanıt anlamı açık ve güçlü delilin karşı görüşü aşabilmesini düşündürebilir. Bu bağlantı 17:36’yı kazanan tarafı ya da eksiksiz bir delil kanununu ilan eden hükme dönüştürmez. Gönlün anılması iç muhakemeyi de hesaba katar, ancak her karar vericinin saiki hakkında hukuk hükmü kurmaz. Böylece sahne öldürmeye özgü bir mahkeme değil, yetkinin dayandığı bilginin hesabını soran genel bir ahlak çerçevesi sunar.

Görmenin ayrıca anılması, yetki sözcüğünün ait olduğu kelime ailesindeki yakılarak ışık veren bitkisel yağ kullanımına bir görüntü kapısı açar. Bilgi ve gerçek görme olguları görünür kıldıkça lamba yağı ayrıntısı, davanın kuvvet kullanılmadan önce aydınlanması benzetmesini zenginleştirir (17:36). Kanıt ve dayanak anlamı ışığı iddianın doğruluğunu inceleme zemininde tutar; bu bağlantıda sultan sözcüğü yağ değil yetki anlamındadır ve imge tek başına her delilin kesin sonucunu güvenceye almaz. Aynı öldürme kökünün bir şeyi bütünüyle kavrayıp kesin bilme yönündeki ayrı kullanımı da bilmeden iz sürmeme uyarısıyla temas eder (17:36): bu yankı geri döndürülemez eylem öncesi titizliği güçlendirir, odaktaki öldürme biçimlerinin anlamını değiştirmez.

Görünür olgulara cevap vermesi gereken yetki, şimdi tevazu ve kaynağı bakımından sınanır. Yeryüzünde böbürlenerek yürümeme uyarısı (17:37), makam sahibini büyütmeye izin vermez; yeri yaramama görüntüsü yatay erişimin, dağlara boyca erişememe ise dikey erişimin sınırını ayrı ayrı gösterir (17:37). Bu imgeler iradeli zorlama ile gerçekten erişilebilir kudret arasındaki farkı hissettirir; buradaki bağlantı velinin yargı alanını fiziksel bir sınamayla ölçmez. Önceki buyrukların hikmet içinde toplanması ve Allah’ın yanına başka ilah koyma yasağı (17:39), yetkinin daha yüksek kaynağını görünür kılar. Odaktaki {ar:جَعَلْنَا, tr:jaʿalnā, gloss:bir konuma atadık} ile {ar:تَجْعَلْ مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ, tr:tajʿal maʿa Allāhi ilāhan ākhar, gloss:Allah’ın yanına başka ilah koyma} aynı kılma ve yerleştirme ailesindendir, ama biri veliye konum verirken öteki Allah’ın yanına ilah atfeder. Odakta {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah}, {ar:حَرَّمَ, tr:ḥarrama, gloss:dokunulmaz kıldı} fiilinin öznesidir; bu özel adın işlevi ibadet, yemin ya da hitap değil, koruma eyleminin ilahî kaynağını belirtmektir. Bu kapanış, devredilmiş yetkinin kendini yetkilendiremeyeceğini düşündürür. 17:37 ve 17:39 ayrıca genel tevazu ve tevhid de bildiriyor olabilir; burada kurulan bağ belirli bir hukuk teorisi kurmaz.

## Ölçülü Karşılık

Yakın bağlamdaki bu ölçülülük, daha geniş koruma ve giderim örüntüsünde de sürer. Canı koruyan yasak başka ayetlerde yinelenir (6:151, 25:68); dokunulmazlığın denk karşılıkla yan yana gelişi (2:194), giderim konuşulurken de korunan hayatın ölçü olmaya devam ettiğini gösterir. Bir canı öldürmenin bütün insanları öldürmeye, bir canı kurtarmanın hepsini yaşatmaya benzetilmesi (5:32) bu hayatın değerini tekil olayın ötesine taşır. İstisnadaki {ar:بِٱلْحَقِّ, tr:bi-l-ḥaqqi, gloss:hakka dayanarak} böylece belirli bir talep sahibine de bağlanır: öldürülenin kardeşine kısasın yanında bağışlama ve ödeme yolu açılır (2:178), tazminat aileye yönelir (4:92), cana karşı can ölçüsünün yanına bağışlama konur (5:45). Bu yollar hakkı taşıyan kişiyi ve karşılığın çeşitliliğini görünür kılar; tek bir yararlanıcı derecesi ya da ortak bir usul belirlemez.

Karşılığın ölçüsü, bağışlamaya da yer bırakır. Alınan zarara denk cevap ve sabrın daha iyi oluşu (2:194, 16:126), eşdeğer karşılığın yanına af ve barışmayı koyan anlatımla genişler (42:40); haksızlığa uğradıktan sonra hakkını arayanın kınanmamasıyla, haksız yere sınırı aşanın kınanması arasındaki fark da çizilir (42:41, 42:42). Bu temaslar {ar:يُسْرِف, tr:yusrif, gloss:ölçüyü aşmak} yasağını belirsiz bir ihtiyattan ölçülü karşılık sınırına taşırken bağışlamayı da açık tutar. Sorumlu kişide durmayıp başkasına yönelme ihtimali (2:194, 5:45) bu yüzden aşımın bir biçimi olarak düşünülebilir; bu, karşılık ve bağışlama örüntüsünden çıkan bağlamsal bir özelleştirmedir, adı konmuş bir olayın hükmü değildir.

## Desteğin Yönü

Öldürmede aşmama sınırından sonra ayet, {ar:إِنَّهُۥ, tr:innahū, gloss:şüphesiz o} vurgusuyla güvenceye döner; ona bitişen hu zamiri güvenceyi başlatır ama göndergeyi tek başına belirlemez. Ardından gelen {ar:كَانَ, tr:kāna, gloss:oldu} eksik fiili yerleşik ya da süren bir durumu da taşıyabilir; haberi olan {ar:مَنصُورًا, tr:manṣūran, gloss:desteklenmiş} belirsiz ve mansup edilgen ortaç, yeni bir eylemden çok destek görenin hâlini öne çıkarır. Edilgen yüklem yardımı kişinin kendi gücü değil, kendisine yönelen destek olarak duyurur. Zamir veliye, öldürülen kişiye ya da yürütülen hak işine dönebilir; ayetin sonu misilleme buyruğu değil, alınan desteğin güvencesidir.

Bu destek sözü hem birine yardım edip onu güçlü kılmayı hem zulmedene karşı koyarak hakkı geri almayı çağrıştırabilir. Haksızlıktan sonra hakkını arayanın kınanmaması (42:41) etkin hak arama dalını duyurur; 17:33’teki edilgen {ar:مَنصُورًا, tr:manṣūran, gloss:desteklenmiş} biçim ise öldürüleni etkin karşı koyan kişiye çevirmez. {ar:وَلِيِّهِۦ, tr:waliyyihī, gloss:öldürülenin velisi} hakkı izleyen taraf olabilir, öldürülen de bu çabanın yarar göreni olarak kalabilir. Veliye verilen {ar:سُلْطَٰنًا, tr:sulṭānan, gloss:yetki} ile birlikte düşünüldüğünde destek, iddianın etkili biçimde ileri sürülmesini veya hukuken tanınmasını; somut yardımı ve fiziksel giderimi de taşıyabilir. Bu olasılıklar aynı sonuca indirgenmez, misillemede zaferi de tek sonuç yapmaz.

Bu ayrım, yardım gücü verilen mağdurların ve veliyle yardımcı için yakaran ezilenlerin sahnelerinde farklı yönleriyle belirir: ilkini haksızlığa uğrayanlara yardım gücü veren ayet (22:39), ikincisini ezilenlerin yakarışı gösterir (4:75). Diri diri gömülen kız çocuğuna hangi günahı yüzünden öldürüldüğünün sorulması (81:8, 81:9) ise {ar:قُتِلَ, tr:qutila, gloss:öldürüldü} ve {ar:مَظْلُومًا, tr:maẓlūman, gloss:haksızlığa uğramış halde} ile odakta öne çıkan kişiyi yalnız velisinin yetkisine konu değil, hesabı sorulan mağdur olarak da görünür kılar. Bu yardım ve sorgu sahneleri, olağan destek anlamını koruyarak öldürülenin hakkının görülmesi ihtimalini de açar; metin belirli bir kurum, ölüm sonrası hâl veya yargılama usulü adlandırmaz.

Fâtiha’daki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:Yalnız Sana kulluk eder ve yalnız Senden yardım isteriz} duası yardım talebini yalnız Allah’a yöneltir (1:5). Bu çağrı, 17:33’te yardım eden faili belirtilmeyen edilgen güvenceye nihai kaynak bakımından ilahî bir yön ekleyebilir; öldürülenin velisine verilmiş insanî yetkiyle aynı görev değildir. Bu bağlantı yardımın nihai kaynağına yöneliktir: Fâtiha mağduru adlandırmaz; 17:33’ün zamiri ve edilgen ortaç da desteğin alıcısını ya da yardım eden faili kesinleştirmez. Böylece atanmış veli hakkı izleyen insanî kapasiteyi taşırken, güvence içindeki yardımın son kaynağı açık kalır.

</source_prose>
