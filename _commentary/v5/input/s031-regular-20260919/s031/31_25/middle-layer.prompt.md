# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:25**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.middle.claims.json`

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
- Refer to source paragraphs as `31:25 ¶N`.

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

`(31:25 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:25",
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
        "citation": "(31:25 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_25/31_25.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_25/31_25.middle.claims.json \
  --ayah-ref 31:25
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_25/31_25.prose.editorial.tr.md`

<source_prose>
## Soru, cevap ve sözün yönü

Âyet, gökleri ve yeri kimin yarattığını sorar; onlara böyle sorulsa mutlaka “Allah” diyeceklerini bildirir, ardından peygambere “De ki: Hamd Allah’a aittir” buyruğunu yöneltir ve çoğunun bilmediğini ekler: {ar:مَنْ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:man khalaqa as-samāwāti wa-l-arḍa, gloss:gökleri ve yeri kim yarattı}, {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler}, {ar:قُلِ ٱلْحَمْدُ لِلَّهِ, tr:quli al-ḥamdu li-llāh, gloss:de ki hamd Allah’a aittir}, {ar:بَلْ أَكْثَرُهُمْ لَا يَعْلَمُونَ, tr:bal aktharuhum lā yaʿlamūna, gloss:aksine çoğu bilmez}.

Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} önceki söz akışına bağlanır; ardından gelen {ar:لَئِنْ, tr:la-in, gloss:eğer} koşulu soruyu tek seferlik bir anlatı değil, yeniden kurulabilir bir yoklama olarak açar. Şart lâmı ile “eğer” edatının birlikteliği soruya yemin tınısı verir; yanıttaki karşılık lâmı ve ağır nûn ise grubun ne diyeceğini kesinleştirir. Bu kesinlik yalnız söylenecek Allah adına aittir: içtenliği ya da kavrayışı ölçmez. Koşulun tamamlanmış soru eylemini {ar:سَأَلْتَهُمْ, tr:saʾaltahum, gloss:onlara sorsan} yanıtın muzâri biçimi {ar:لَيَقُولُنَّ, tr:la-yaqūlunna, gloss:mutlaka diyecekler} izler; her yeniden kurulan yoklamanın gerçekten yaşandığı ileri sürülmez ve belirtilmeyen bir yemin konusu da eklenmez.

Soruyu yönelten tekil muhatap, yanıt beklenen çoğul gruba seslenir: {ar:مَنْ, tr:man, gloss:kim}, {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} fiilinin özne yerini sorar. Böylece istenen bilgi yaratma yöntemine, nesnesine ya da yardıma değil, yaratanın kimliğine ilişkindir; bu tek yönlü bir yoklamadır, karşılıklı araştırma değildir. Koşuldaki aynı grup yanıt fiilinin öznesi olur ve yalnız {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} adını söyler. Nominatif biçim açık bırakılan fail yerini doldurur: yaratıcıyı adlandırır, yaratma sürecini tarif etmez.

Bu cevapta anılan gökler ve yer, aynı {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} fiilinin iki nesnesidir; tamamlanmış etkin fiil onları tek bir yaratma kapsamına alır ve tek Allah adı her ikisinin de yaratıcısını gösterir. Belirli çoğul {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler}, belirli tekil {ar:ٱلْأَرْضَ, tr:al-arḍa, gloss:yeryüzü} ile birleşerek üst alanı ve üzerinde yaşanan yeri karşı karşıya getirir. Sayı ayrımı gök katmanlarının adedini ya da fiziksel ölçüyü vermez; yer de burada başka ülkeler veya alt bölümler değil, yaşanan kozmik alandır. Böylece cümle, göklerin çoğulluğu ile yerin tekilliğini aynı yaratma kapsamındaki üst ve yaşanan alt alan olarak bir arada tutar.

Olağan anlamıyla {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} var etmektir; aynı sözcük ailesindeki başka bir kullanım, işi yapmadan önce ölçü ve sınır belirlemeyi anlatır. Gerçek göklerle yerin bu fiile bağlanması, yaratılışı ölçüsü olan bir düzen olarak da duyurur; bu yankı fiilin var etme anlamını değiştirmez, fiziksel boyutları ya da yöntemi belirlemez. {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} sözcüğünün uzak bir kolundaki “üstte bulunma, örtme” imgesi, yaşanan {ar:ٱلْأَرْضَ, tr:al-arḍa, gloss:yeryüzü} ile karşılaşınca üst alanla zemin arasındaki görünüşü elle tutulur kılar. Bu üst-örtü/zemin imgesi yalnızca göklerin üstte, yerin yaşanan aşağı alan oluşuna dayanır; yağmur, bulut ya da modern gök katmanları bu bağlantının parçası değildir. Üst ile zeminin bu çifti, bir sonraki buyrukta yaratıcıya yönelen hamdin dayandığı yaratılmış bütünü de göz önüne getirir.

## Övgü buyruğuna geçiş

Yaratıcı cevabının ardından gelen {ar:قُلِ, tr:quli, gloss:söyle} buyruğu söz sırasını değiştirir: önce üçüncü çoğul biçimde grubun ne diyeceği bildirilir, sonra tekil muhataba—peygambere—{ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} sözünü söyleme görevi verilir. Soru, grubun yanıtı ve emir ayet içinde üç ayrı söz dönüşüdür. {ar:لَيَقُولُنَّ, tr:la-yaqūlunna, gloss:kesinlikle diyecekler} ile {ar:قُلِ, tr:quli, gloss:söyle} aynı olağan “söylemek” eylemini taşır; biri cevabı bildirir, diğeri hamdi dile getirir. Bu değişim konuşanın görevini belirler; ayet grubu cevabın zorla söyletildiği ya da samimiyetsiz olduğu hükmüne bağlamaz.

Buyruğun konusu {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü}dur: belirli, nominatif bir mastar olarak tek bir teşekkür eylemini değil, adlandırılmış övgü kategorisini konu eder. Hamd yermenin karşıtı olan övgüdür; iyilik için teşekkürü içine alır, ama teşekküre indirgenmez. Ardından gelen {ar:لِ, tr:li, gloss:-e/-a} edatı övgüyü Allah adına yöneltir. Cevaptaki nominatif {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah}, burada lâmın yönetimiyle genitif {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah’a} olur: aynı ad önce yaratıcı failin, sonra övgünün yöneldiği varlığın adıdır. Lâm, hamdi Allah’a bağlarken sahiplik ve övgüye layıklık inceliklerini birlikte açık bırakır.

Bu iki konum aynı adı bir araya getirir: yaratıcı diye verilen {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} cevabı, övgünün yöneldiği Allah adında sürer. Allah adının bağlı olduğu sözcük ailesindeki tapınma yönelişi, lâmın {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} sözünü ona çevirmesiyle nitelikli bir yankı kazanır; özel ad yine ad olarak kalır, tapınma fiiline dönüşmez. Böylece ayetin kendi sıralanışı yaratıcıyı adlandırmaktan onu övgüye layık kaynak olarak tanımaya ilerler. Hamd bu cevabı silmez, ona bir değerlendirme ekler.

Odaktaki {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} buyruğunu hemen izleyen 31:26’da göklerde ve yerde ne varsa Allah’a ait olduğu, O’nun kendine yeter ve övgüye layık olduğu söylenir: {ar:لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:li-llāhi mā fī as-samāwāti wa-l-arḍ, gloss:göklerde ve yerde ne varsa Allah’ındır}, {ar:إِنَّ ٱللَّهَ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:inna Allāha huwa al-ghaniyyu al-ḥamīd, gloss:Allah kendine yeter ve övgüye layıktır} (31:26). 31:12’de şükredenin yararının kendisine döndüğü de belirtilir (31:12). Bu yakın bağlamlarda hamd, Allah’a yeni bir değer ekleyen ödeme değil, nimeti tanıyan konuşanın iyiliğin kaynağına yönelişidir; değişen Allah değil, konuşanın konumudur. Kendine yeterlilik ve övgüye layıklık, reddin Allah’a zarar vermeyeceği güvencesini de düşündürür; bu güvence yöneliş okumasının yanında kalır.

## Söylenen ile bilinen

{ar:بَلْ, tr:bal, gloss:aksine} vurguyu {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} sözünden bilgi hükmüne taşır; böylece yaratıcı cevabı ve hamd yerinde kalırken çoğunluğun kavrayışı ayrıca değerlendirilir. Hükmün öznesi {ar:أَكْثَرُهُمْ, tr:aktharuhum, gloss:onların çoğu}dur: kapsam bütün gruba yayılmaz ve azınlığın ne bildiği belirtilmez. {ar:لَا, tr:lā, gloss:değil} yalnızca {ar:يَعْلَمُونَ, tr:yaʿlamūna, gloss:bilirler} yüklemini olumsuzlar; çoğul muzâri, çoğunluğun hüküm anında süren bilme eksikliğini anlatır, başlangıcını ya da bitişini bildirmez. Buradaki bilme, söylenenin gerçeğini tanıyıp kavramaktır; hangi ayrıntının bilinmediği açık bırakılır. Odak, yanlış bir adlandırmadan çok, doğru adın çoğunluk için kavrayışa dönüşmeyişidir.

Bilme fiilinin ailesindeki evreni ve yaratılmışların bütününü adlandıran uzak kullanım da bu mesafeye yankı verir. Burada {ar:يَعْلَمُونَ, tr:yaʿlamūna, gloss:bilirler} doğrudan “bilmek” anlamında kalır; hemen yanındaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} ile {ar:ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ, tr:as-samāwāti wa-l-arḍa, gloss:gökler ve yer} bütünü bu kavrayışın yaratılmış gerçeklikle ilişkisini düşündürür. Fiilin olağan bilme anlamı ile yaratılmışlar bütününe yönelik bu uzak yankı yan yana gelince, doğru adı söylemekle yaratılmış alanı gerçekten kavramak arasındaki fark belirginleşir.

31:22’de Allah’a yüzünü teslim eden kişinin sağlam kulpa tutunduğu anlatılır: {ar:يُسْلِمْ وَجْهَهُۥٓ إِلَى ٱللَّهِ, tr:yuslim wajhahu ilā Allāhi, gloss:yüzünü Allah’a teslim eder}, {ar:ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:istamsaka bi-l-ʿurwati al-wuthqā, gloss:sağlam kulpa tutunur} (31:22). Yüze yönelme ve güvenilir tutuş, odaktaki {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler} kısa cevabı ile {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūna, gloss:bilmezler} hükmünün yanına geldiğinde tanımayı benliği yönlendiren, sürdürülen bir yöneliş olarak da duyurur. Bu temas bilgiyi itaate indirgemez; 31:22’yi daha genel bir sadakat anlatısı olarak okumak da mümkündür.

31:27’de yazı araçları adım adım çoğalır: ağaçlar kalem olur, deniz yazıyı besleyen mürekkebe dönüşür ve ona yedi deniz daha katılır: {ar:أَقْلَٰمٌۭ وَٱلْبَحْرُ يَمُدُّهُۥ مِنۢ بَعْدِهِۦ سَبْعَةُ أَبْحُرٍۢ, tr:aqlāmun wa-l-baḥru yamudduhu min baʿdihi sabʿatu abḥur, gloss:kalemler ve ardından yedi denizin desteklediği deniz} (31:27). Bu büyüyen yazı aracına rağmen Allah’ın sözleri tükenmez: {ar:مَّا نَفِدَتْ كَلِمَٰتُ ٱللَّهِ, tr:mā nafidat kalimātu Allāh, gloss:Allah’ın sözleri tükenmez} (31:27). Kalem, mürekkep ve ek denizlerin çoğalması yazı kapasitesini büyütürken sözlerin tükenmemesi başka bir ölçek kurar. Bu karşılaştırma, {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler} cevabını ve {ar:قُلِ, tr:quli, gloss:söyle} buyruğunu doğru ama ilahî hitabı kuşatmayan bir söyleyiş olarak duyurur: tek ad Allah’ın sözlerini tüketmez. Bu ölçek cevabı doğru ve yerinde bırakır; 31:27 ilahî kudreti yüceltiyor olabilir, insan bilgisinin darlığını ayrıca ölçmeyebilir.

29:63’te yağmurla yeryüzünün diriltilmesi gibi gözlenebilir bir işaretin ardından yine göklerle yeri kimin yarattığı sorulur, Allah cevabı ve {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} buyruğu gelir; orada çoğunluğun akletmediği de belirtilir (29:63). Bu tekrar, odaktaki {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler} cevabı ile {ar:أَكْثَرُهُمْ, tr:aktharuhum, gloss:onların çoğu} hakkındaki hükmü birlikte duyurur: aynı adı çok kişinin söylemesi kavrayışı ya da yönelişi ölçmez. 29:63’teki son fiil akletmeyi adlandırır; odaktaki bilme hükmüyle farklıdır. Tekrar, Allah cevabı ve hamd buyruğunu korurken çoğunluğun kavrayışını sayıdan ayrı değerlendirir. Bu hüküm yalnız çoğunluğu kapsar; azınlığın bilgisi hakkında çıkarım yapılmaz. Böylece tekrar, doğru yanıtın ardından bilginin nasıl görünür olacağı sorusunu açık bırakır.

31:20 görünür ve gizli nimetleri, ardından bilgiye, hidayete ya da aydınlatıcı kitaba dayanmadan Allah hakkında tartışmayı anar (31:20). Bu bağlam, odaktaki {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūna, gloss:bilmezler} hükmünü kanıt yokluğundan çok, mevcut göstergeleri doğru yargı ve yönelişe bağlayamama olarak düşündürür: nimetleri görmek, onları anlamakla aynı şey değildir. Tartışma kanıt varken anlamı çarpıtabilecek bir yol açar; hidayet ve aydınlatıcı kitap da aynı bağlamda yön gösteren bir ışık imgesi sunar (31:20). Bu, cevap verenlerin Allah adını doğru söyledikleri gerçeğini koruyan ihtiyatlı bir okumadır; nimetlerin sorumluluğu ağırlaştırması, ama bilmenin yapısını açıklamaması da canlı bir alternatiftir. 31:20’deki gruplar odaktaki cevap verenlerle özdeşleştirilmez; bağlam yine de görünür nimeti tanımayla onun önünde tartışma arasındaki mesafeyi düşündürür.

31:21’de vahiy yerine ataların izini sürme tercihi, söylenen söz ile yaşayışta benimsenen yönelişi ayırmaya başka bir kapı açar (31:21). Odaktaki {ar:لَيَقُولُنَّ, tr:la-yaqūlunna, gloss:kesinlikle diyecekler} biçimi sesli söylemeyi anlatır; aynı sözcük ailesindeki bir kullanım ise görüş ya da inanç benimsemeyle ilgilidir. 31:21 bu ayrımı etkinleştirir, ama odaktaki fiili doğrudan “inanmak” anlamına çevirmez; ataların izini sürmek sadık bir devamlılık da olabilir. Buradaki kişilerle odak ayette cevap verenlerin aynı olduğu söylenmez. Temasın açtığı fark şudur: doğru adı söylemek, onu yargı ve davranışa katmayı kendiliğinden garanti etmez. Söylenen adın işaret ettiği yaratıcı, şimdi soruda anılan gökler ve yerin görünür düzeni içinde yeniden okunur.

## Görünen yaratılış ve işaretler

31:10, sorudaki {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} ve {ar:ٱلْأَرْضَ, tr:al-arḍa, gloss:yeryüzü} adlarını işleyen bir dünya içinde görünür kılar: gök görünür direkler olmadan yükseltilir, dağlar da yeryüzünün insanlar altında salınmasını önleyecek biçimde yerleştirilir (31:10). Odak ayet dağların bunu hangi fiziksel yolla yaptığını açıklamaz. Yağmur iner ve ardından bitki çıkar; yukarıdan gelen su ile yerden beliren bitki, yaratılmış alanın yaşam üreten niteliğini somutlaştırır (31:10). Böylece odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} yaratma cevabı yalnız uzaktaki ilk nedeni değil, ayakta duran ve süren düzenin kaynağını da tanımaya açılır.

31:11’de “ötekilerin ne yarattığını gösterin” çağrısı, bu işleyen alanı rakip yaratıcı iddialarla karşılaştırılabilecek bir zemine çevirir; ardından zulmedenlerin açık bir sapma içinde olduğu belirtilir (31:11). 31:10’daki düzen ayrıntılarıyla 31:11’deki gösterme talebi, odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} fiilinin görünür yaratılışla temas etmesini sağlayan paralel dayanaklardır. Bu iki bağlam tek bir zorunlu neden-sonuç zinciri kurmaz; 31:11’deki sapma hükmü de 31:25’te cevap verenlere yöneltilmez ve nedenini açıklamaz. Böylece görünür düzen yaratıcıyı tanıma imkânı sunarken, doğru cevabın doğru değerlendirmeye dönüşüp dönüşmediği açık kalır.

31:28 yaratma ile yeniden diriltmeyi tek bir canı yaratmak kadar kolay gösterir: {ar:خَلْقُكُمْ وَلَا بَعْثُكُمْ, tr:khalqukum wa-lā baʿthukum, gloss:sizin yaratılışınız ve diriltilmeniz} (31:28). 31:29 geceyi gündüzün içine, gündüzü gecenin içine geçirir; güneş ve ay da belirlenmiş bir süreye doğru akar: {ar:يُولِجُ ٱلَّيْلَ فِى ٱلنَّهَارِ وَيُولِجُ ٱلنَّهَارَ فِى ٱلَّيْلِ, tr:yūliju al-layla fī al-nahāri wa-yūliju al-nahāra fī al-layli, gloss:geceyi gündüzün içine, gündüzü gecenin içine geçirir}, {ar:كُلٌّۭ يَجْرِىٓ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:kullun yajrī ilā ajalin musammā, gloss:her biri belirlenmiş bir süreye doğru akar} (31:29). 31:30 Allah’ı gerçek, O’ndan başkasına yönelinenleri bâtıl diye niteler: {ar:ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلْحَقُّ وَأَنَّ مَا يَدْعُونَ مِن دُونِهِ ٱلْبَٰطِلُ, tr:dhālika bi-anna Allāha huwa al-ḥaqqu wa-anna mā yadʿūna min dūnihi al-bāṭil, gloss:Allah gerçektir, O’ndan başkasına yöneldikleri ise bâtıldır} (31:30). Dönüş, devam eden düzen ve belirlenmiş süre çizgisi ile hakikat ayrımı ayrı bağlamlar olarak odaktaki yaratıcı atfını genişletir. Bu genişleme, yaratma fiilinin bütün ayrıntıları sözlük anlamında taşıdığı demek değildir; her bağlam cevaba kendi katkısını yapar. Zaman ve hakikat çizgisinden, aynı yaratılış cevabının gözle görünen alanına dönünce yeni bir ilişki açılır.

Görünür üst alanı adlandıran {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} ile yaşanan yeri bildiren {ar:وَٱلْأَرْضَ, tr:wa-l-arḍa, gloss:ve yeryüzü}, 31:11’in “gösterin” çağrısına karşılaştırma zemini sunar (31:11). Gök sözcüğünün başka bir kullanımı, gözlenen belirtiden bir durum ya da nitelik hakkında çıkarım yapmaktır; bu kullanım daha çok insanlar üzerindeki işaretlerle ilgilidir. Bu insan-işareti kullanımıyla görünür gök-yer çiftinin teması, gökleri görünmeyen yaratıcı kaynağa yönelten bir belirti gibi okumaya imkân verir. Aktarım analojik ve keşifseldir: göğün düz anlamı “işaret” olmaz, tek tek özelliklerine gizli mesaj yüklenmez. Okunan ilişki, görünür yaratılış ile “bunu kim yaptı?” sorusu arasındadır.

Aynı sözcük ailesinin göklerden biçimce uzak kolu, yakma, kulağı kesme ya da çentik açmayla hayvan veya nesne üzerinde başkalarından ayıran görünür bir iz bırakmayı anlatır. 31:31’de denizde nimetiyle giden gemi Allah’ın işaretlerinden sayılır; sabreden ve şükredenler için de açık işaretler bulunduğu belirtilir: {ar:ءَايَٰتِهِۦٓ, tr:āyātihi, gloss:O’nun işaretleri}, {ar:لَءَايَٰتٍۢ لِّكُلِّ صَبَّارٍۢ شَكُورٍۢ, tr:la-āyātin li-kulli ṣabbārin shakūr, gloss:çok sabreden ve şükredenler için işaretler vardır} (31:31). Ayrıca odaktaki bilme fiilinin ailesinde ayırt edici işareti tanıma kullanımı da vardır; bu biçim yine olağan “bilmek” anlamını taşır. Bu öğeler buluşunca {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} yaratılmış gökleri, {ar:يَعْلَمُونَ, tr:yaʿlamūna, gloss:bilirler} ise işareti tanımayı çağrıştırır: yaratıcıyı doğru adlandırmakla yaratılmış işaretleri okumak arasındaki fark belirginleşir. Bu aktarım keşifseldir; gök sözcüğü düz anlamıyla gök olarak kalır, göklere fiziksel iz veya 31:31’in kurmadığı bir şifre düzeni yüklenmez.

Söz söyleme fiili de görünür yaratılışla başka bir yoldan karşılaşır. Odaktaki {ar:لَيَقُولُنَّ, tr:la-yaqūlunna, gloss:kesinlikle diyecekler} insanların sesli cevabıdır; aynı sözcük ailesinde sözsüz bir durumun bir şeyi belli etmesi kullanımı da vardır. 31:11’in “ötekilerin ne yarattığını gösterin” çağrısı ile {ar:ٱلسَّمَٰوَٰتِ, tr:as-samāwāti, gloss:gökler} ve {ar:ٱلْأَرْضَ, tr:al-arḍa, gloss:yeryüzü} çiftinin görünürlüğü bu iki kolu temas ettirir: insanın “Allah” sözü, yaratılıştan gelen sessiz bir belirtinin yanında sesli yankı gibi duyulabilir (31:11). İnsanlar sözün gerçek konuşanlarıdır; kozmosa ses ya da bilinç atfedilmez. Böylece sözlü cevapla görünür yaratılışın sessiz belirtisi iki ayrı gösterme yolu olarak yan yana gelir.

Görünen düzen, hamdin değerlendirme yönünü de açar. {ar:ٱلْحَمْدُ, tr:al-ḥamdu, gloss:övgü} olağan anlamıyla övgüdür; sözcük ailesindeki başka bir kullanım ise bir şeyi deneyip övülesi ya da uygun bulmayı anlatır. Odaktaki {ar:خَلَقَ, tr:khalaqa, gloss:yarattı} fiilinin ölçü belirleme kolu, 31:10’daki dağlar, yağmur ve bitkinin işleyen düzeniyle; var etme anlamı 31:11’in başkalarının ne ortaya koyabildiğini gösterme çağrısıyla karşılaşır (31:10, 31:11). Bu ayrı dayanaklar bir araya gelince hamd, görünen düzeni inceleyip kaynağını övülesi bulma yargısı olarak da duyulur. Hamdın olağan anlamı yine övgüdür; sözcük doğrudan “sınamak” anlamına gelmez ve 31:10 ile 31:11 tek bir zorunlu neden-sonuç zinciri kurmaz.

## Sorunun açtığı ihtimal ve bilgi sınırları

Odaktaki {ar:سَأَلْتَهُمْ, tr:saʾaltahum, gloss:onlara sorsan} olağan anlamıyla muhataptan bilgi istemektir. Sözcük ailesinin biçimce uzak bir kullanımı ise bağlı ya da kapalı bulunduğu yerden bir şeyi nazikçe, fark ettirmeden çekip çıkarmayı anlatır. 31:24’teki {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları zorunlu bırakırız} zorlama, odaktaki koşullu soru ve vurgulu {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler} cevabıyla; 29:63’te yinelenen soru ve hazır yanıtla temas eder (31:24, 29:63). Bu işlemler, çekip çıkarma imgesini bilinen cevabı yüzeye alan tanısal bir yoklamaya dönüştürür. Odaktaki fiil gerçek bir soru sormadır; bu yankı sorunun kendisini zorlayıcı yapmaz ve cevabın içten benimsenmiş inanç olduğunu kanıtlamaz.

31:32’de dalgalar gölgelikler gibi insanları örter ve kriz ağırlaşır: {ar:غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-l-ẓulal, gloss:gölgelikler gibi onları dalgalar kapladığında} (31:32). Bu örtülme içinde insanlar dini yalnız Allah’a has kılarak O’na yakarır: {ar:دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:daʿaw Allāha mukhliṣīna lahu al-dīn, gloss:dini yalnız O’na has kılarak Allah’a yakardılar} (31:32). Kurtulup karaya çıkınca bazıları ölçülü kalır, bazıları ise Allah’ın ayetlerini bildiği hâlde inkâr eden hain ve nankör olarak belirir: {ar:يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا كُلُّ خَتَّارٍۢ كَفُورٍۢ, tr:yajḥadu bi-āyātinā illā kullu khattārin kafūr, gloss:ayetlerimizi ancak hain nankör inkâr eder} (31:32).

31:24’teki {ar:نَضْطَرُّهُمْ, tr:naḍṭarruhum, gloss:onları zorunlu bırakırız} zorlama ile 31:32’deki {ar:غَشِيَهُم مَّوْجٌۭ كَٱلظُّلَلِ, tr:ghashiyahum mawjun ka-l-ẓulal, gloss:gölgelikler gibi onları dalgalar kapladığında} örtüsü yan yana gelince, koşullu soruda verilen {ar:لَيَقُولُنَّ ٱللَّهُ, tr:la-yaqūlunna Allāhu, gloss:kesinlikle Allah diyecekler} cevabının baskı altında dile gelip kurtuluş sonrasında davranışı yönetmeyebileceği ihtimali açılır; bilinen şey eylem içinde gömülebilir (31:24, 31:32). Bu ihtimal, odaktaki süren {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūna, gloss:bilmezler} hükmünün de yanına gelir. Bu iki bağlamdaki insanlar özdeşleştirilmez ve her bilgisizlik isteyerek sayılmaz; odaktaki sıradan soru ve doğru cevap okuması yerini korur.

Bu davranış ihtimalinin yanında, 17:85 insana bilgiden ancak az bir pay verildiğini bildirir: {ar:وَمَآ أُوتِيتُم مِّنَ ٱلْعِلْمِ إِلَّا قَلِيلًۭا, tr:wa-mā ūtītum mina l-ʿilmi illā qalīlan, gloss:bilgiden size ancak azı verilmiştir} (17:85). Bu genel insanî sınır, odaktaki {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūna, gloss:bilmezler} hükmünün bir yanını gerçek yaratılmışlık sınırı olarak düşündürür; belirli çoğunluğun bilgisizliğini tek başına açıklamaz ve doğru cevabı davranışa katmama ihtimalini ortadan kaldırmaz.

31:34’te saatin bilgisi, yağmurun indirilmesi ve rahimlerde olanı bilmek Allah’a nispet edilir; hiçbir can da yarın ne kazanacağını veya hangi yerde öleceğini bilmez: {ar:إِنَّ ٱللَّهَ عِندَهُۥ عِلْمُ ٱلسَّاعَةِ وَيُنَزِّلُ ٱلْغَيْثَ وَيَعْلَمُ مَا فِى ٱلْأَرْحَامِ, tr:inna Allāha ʿindahu ʿilmu al-sāʿati wa-yunazzilu al-ghaytha wa-yaʿlamu mā fī al-arḥām, gloss:saatin bilgisi Allah katındadır, yağmuru indirir ve rahimlerde olanı bilir}, {ar:وَمَا تَدْرِى نَفْسٌۭ مَّاذَا تَكْسِبُ غَدًا وَلَا تَدْرِى نَفْسٌۢ بِأَىِّ أَرْضٍۢ تَمُوتُ, tr:wa-mā tadrī nafsun mādhā taksibu ghadā wa-lā tadrī nafsun bi-ayyi arḍin tamūtu, gloss:hiçbir can yarın ne kazanacağını ya da hangi yerde öleceğini bilemez} (31:34). Bu, yaratılmışın geleceğin ayrıntılarına erişemediği gerçek bir sınırdır (31:34). Odaktaki {ar:لَا يَعْلَمُونَ, tr:lā yaʿlamūna, gloss:bilmezler} hükmüyle açılan kavrayış eksiğini ya da doğru cevabı yaşayışa katmama ihtimalini tek başına açıklamaz; bunlar ayrı bilgi durumlarıdır.

</source_prose>
