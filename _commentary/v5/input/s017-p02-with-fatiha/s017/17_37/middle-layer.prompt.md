# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:37**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.middle.claims.json`

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
- Refer to source paragraphs as `17:37 ¶N`.

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

`(17:37 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:37",
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
        "citation": "(17:37 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_37/17_37.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_37/17_37.middle.claims.json \
  --ayah-ref 17:37
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_37/17_37.prose.editorial.tr.md`

<source_prose>
## Adımın Tarzı

17:37, {ar:وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī al-arḍi maraḥan, gloss:yeryüzünde taşkın sevinçle yürüme} diyerek bedensel bir hareketi ve o hareketin tarzını yasaklar. Başındaki {ar:وَلَا, tr:wa-lā, gloss:ve yapma} bu buyruğu önceki söyleme ekler; önceki sözün içeriği burada belirtilmez. Birleşik yapıdaki {ar:لَا, tr:lā, gloss:yapma} yasaklayıcıdır; ardından gelen ikinci tekil şahıs, cezmli yalın fiil {ar:تَمْشِ, tr:tamshi, gloss:yürümek} muhatabın kendi adımını atmasını anlatır. Böylece buyruk bütün yürüme eylemini değil, {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} ile nitelenen yürüyüş tarzını sınırlar.

Bu niteleme önce adımın tarzına bağlanır: {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç}, belirsiz ve mansup bir isim-fiildir. Onu hâl, amaç ya da pekiştirme sayan dilbilgisel çözümlemeler aynı yürüyüş bağını farklı yollardan kurar; girdikleri çözümleme değişse de tek bir yorum zorunlu değildir. Aktarılan bir okuyuşta nitelik doğrudan yürüyene yüklenir, dolayısıyla dilbilgisel taşıyıcı değişse de sahnede taşkın bir edayla yürüyen kişi kalır. Sözcüğün çekirdeği olağan ölçüyü aşan sevinç ve yerinde duramayan canlılıktır. Bu canlılığın davranışta nasıl görünür olduğunu başka ayetler belirginleştirir: 40:75’te yeryüzündeki haksız sevinci anlatan {ar:تَفْرَحُونَ فِي الْأَرْضِ بِغَيْرِ الْحَقِّ, tr:tafrahūna fī al-arḍi bi-ghayri al-ḥaqq, gloss:yeryüzünde haksız yere sevinirsiniz} ifadesini aynı sözcük ailesinin başka bir biçimi olan {ar:تَمْرَحُونَ, tr:tamraḥūna, gloss:taşkınca coşarsınız} izler; 31:18’de yürüyüş yasağının yanına böbürlenen ve övüngen kişi konur; 31:19’da adımda ölçü ve seste alçalma çağrılır; 25:63’te ise yeryüzünde yumuşakça yürüyenler gösterilir (40:75, 31:18, 31:19, 25:63). Bu örnekler adımı toplumsal olarak okunabilen bir tavra dönüştürür: ölçüsüz canlılık bedende kendini büyüten bir eda halinde görünür. Böylece {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} kibirli tavırla bağ kurar; sözcüğün çekirdeği ölçüyü aşan sevinçtir ve bu hüküm her sevince yayılmaz.

## Yeryüzü ve İki Yön

Adımın sahası {ar:فِي الْأَرْضِ, tr:fī al-arḍi, gloss:yeryüzünde} ile açılır: {ar:فِي, tr:fī, gloss:içinde} konumu, belirli {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} ise yürüyenin üzerinde bulunduğu ortak zemini bildirir. Belirlilik küçük ve özel bir arazi yerine daha geniş, ortak yaşanır yeri düşündürür; bu genişlik bütün kozmosu adlandırmaz. Dağlar üst karşılaştırıcı olunca yeryüzü, göğe göre aşağıda kalan yaşanılır zemin olarak dikey kıyasın alt dayanağına dönüşür; bu ilişki göğü ayet sahnesine katmaz. Aynı belirli yer, ikinci sınamada {ar:تَخْرِقَ الْأَرْضَ, tr:takhriqa al-arḍa, gloss:yeryüzünü yarıp geçmek} fiilinin nesnesi olarak döner. Önce bedeni barındıran zemin, ardından reddedilen eylemin hedefi olur: dilbilgisel rol değişir, söz konusu yer değişmez. Sözcüğün hemzeyle açılıp vurgulu ḍādla sürmesi zemine sert bir ses kenarı verir; bu ses dokusu yarma imgesini işitsel olarak keskinleştirir, toprağın maddi sertliğine kanıt oluşturmaz.

Yürüyüş yasağını izleyen {ar:إِنَّكَ, tr:inna-ka, gloss:kuşkusuz sen} vurgusu yasağı aynı muhatabın iki ayrı kapasite sınırıyla ilişkilendirir. İlk fiilden önceki {ar:لَنْ, tr:lan, gloss:geleceğe dönük olumsuzluk} o eylemi olumsuzlar. İkinci sınamayı bağlayan {ar:وَ, tr:wa, gloss:ve}, ardından gelen {ar:وَلَنْ, tr:wa-lan, gloss:ve asla} içinde bağlantıyı sürdürürken yeni bir lan olumsuzluğu da başlatır. Lan’ın iki fiil önünde yinelenmesi her sınamayı kendi tam olumsuzluğuyla kurar: ilki yeryüzüne doğru delme girişimi, ikincisi dağlara doğru erişmedir. İkinci fiilde lan’ın tekrarı olumsuzluğu da yeniler; sınama ilkinden eksik bir olumsuzluk devralmaz. Başlangıçtaki yasaklayıcı lâ yürüyüş tarzını, lan’lar ise delme ve erişme kapasitelerini geleceğe dönük olarak sınırlar. {ar:إِنَّكَ, tr:inna-ka, gloss:kuşkusuz sen}deki tekil muhatap ile {ar:تَمْشِ, tr:tamshi, gloss:yürümek}, {ar:تَخْرِقَ, tr:takhriqa, gloss:delmek} ve {ar:تَبْلُغَ, tr:tablugha, gloss:erişmek} fiillerindeki ikinci şahıs aynı kişiyi buyruktan iki sınıra kadar izler; tekil hitap muhatabı belirler, buyruğun geçerliliğini tek kişiye daraltmaz.

İlk sınama, {ar:تَخْرِقَ, tr:takhriqa, gloss:delmek} fiilinin Form I’deki yalın fiziksel yarma ve delme anlamıyla kurulur; daha yoğun türemiş bir biçim değil, en yalın delme eylemi bile imkânsızlık sınırına girer. Lan’ın yönettiği mansup fiilin açık nesnesi belirli yeryüzüdür; hedef dilbilgisel olarak seçiktir ve eylemin gerçekleşmeyeceği bildirilir. Sözcük ailesindeki incelik gözetmeden hoyrat davranma kullanımı, taşkın {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} ile toprağın nesne oluşuna temas ederek sınır aşımı yankısı verir; bu çağrışım odağın fiziksel yarma fiilini genişletmez. Biçimin seyrekliği de yalnızca biçimsel bir gözlemdir, yeni anlamın kanıtı değil. İlk sınır böylece yarılamayan yeryüzüyle somutlaşır.

Karşı yöndeki sınama {ar:تَبْلُغَ الْجِبَالَ طُولًا, tr:tablugha al-jibāla ṭūlan, gloss:dağlara boyca erişmek} ifadesidir. {ar:تَبْلُغَ, tr:tablugha, gloss:erişmek} yine Form I’de öznenin kendisinin hedefe varmasını anlatır. Belirli çoğul {ar:الْجِبَالَ, tr:al-jibāla, gloss:dağlar} tek bir zirveyi ya da insan topluluğunu değil, çevresindeki araziden yükselen doğal kütleler sınıfını karşılaştırıcı yapar. Sondaki mansup {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} dağları niteleyen sıfat değil, erişmenin ölçüsünü bildiren unsurudur. Yeryüzü ile dağlar böylece bedeni alt ve üst yönden sınırlayan fiziksel ölçekleri verir; her fiil kendi hedefi ve kendi lan’ıyla ayrı bir imkânsızlık kurar.

Başlangıçtaki {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} ile sondaki {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} belirsiz mansup biçimleri ve benzer ses sonlarıyla birbirine cevap verir: ilki adımın tarzını, ikincisi erişme sınırının ölçüsünü belirler. Bu ikinci sözcüğün ilişkili kullanımları fiziksel boy kıyasının çevresinde üç ayrı kapasite açar. Açıkça bildirilen erişememe, bir işi yapmaya yetecek güç ya da maddi imkân anlamını harekete geçirir; temas kapasite sınırındadır ve kendi başına mal varlığı bildirmez. Taşkın yürüyüş ile gerçek dağ yüksekliği yan yana geldiğinde kendini üstün görme kullanımı da erişilemeyen bedensel büyüklük iddiasını düşündürür; bu, {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} sözcüğünün doğrudan anlamı değil, marah ile dağ kıyasının açtığı ilişkidir. Belirli söz kuruluşlarındaki uzun süre kullanımıysa büyüme benzetmesinde kısa hamleye devamlılık ölçüsü katar; odakta zaman göstergesi bulunmadığından bu katkı analojik kalır, genel bir zaman anlamı kurmaz.

Bu parçalar bir araya geldiğinde taşkın adımın ne iddia ettiği belirginleşir. {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} yürüyüşe kendini büyük gösteren bir eda verir; 31:18’deki böbürlenen ve övüngen kişi bu edaya toplumsal karşılık sağlar (31:18). Aşağıdaki zemini yarma ile yukarıdaki dağlara erişme girişimleri de bu bedenin kudret ve boy iddiasını iki ayrı fiziksel ölçekle sınar. 40:75’te haksız sevinci izleyen taşkın coşku, sevinç ile gösterişli eda arasındaki bağı destekler (40:75). 31:19’un ölçülü adım ve alçak ses çağrısı aynı beden için başka bir davranış ölçüsü sunar; ölçüyü gözetme, delme imgesine hoyratlık yankısı katabilir, ancak başarısızlık beceriksizlikle açıklanmaz (31:19). 40:56’da dayanak olmaksızın Allah’ın ayetleri hakkında tartışanların erişemeyecekleri bir büyüklenme içinde olması da erişme temasını dağ boyu kıyasına yaklaştırır; bu ilişki anlam üzerinden kurulur, alıntı ya da aynı sözcük biçimi üzerinden değil (40:56). Böylece fiziksel yer ve dağ kıyası, yürüyüşteki gösterişi ölçüsünü aşan bir kudret iddiası olarak duyurur.

Yürüyüş ve delme sınırları yatay bir hareket tasarısını kurar. {ar:تَمْشِ, tr:tamshi, gloss:yürümek} bir yerden ötekine iradeyle ilerlemeyi taşır; fiil ailesindeki ayrı bir kullanım açık araziyi bir uçtan ötekine katetmeyi anlatarak serbest geçiş imgesini açar. Bu kullanım, fiziksel delme anlamını değiştirmeden {ar:تَخْرِقَ الْأَرْضَ, tr:takhriqa al-arḍa, gloss:yeryüzünü yarıp geçmek} ile buluşur. Yeryüzü ailesindeki zemine bağlı kalma, ağırlaşma ve oyalanma yönü ise bu geçişi yere sabitler; burada {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} “ağırlık” demek değil, zeminde kalma çağrışımını taşıyan addır. Dağın kazıcının daha ileri gidemediği sert katman olarak aktarılan kullanımı, bu yatay ilerlemeye son bir eşik ve durma noktası ekler; bu katman karşılaştırmanın parçasıdır, ayette anlatılan bir kazı olayı değil. {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü}nün karşılaştırmalı kullanımı da bir varlığın ötekini boyca aşmasını sağlayan üst kıyas noktasını verir. Serbest geçişi açan yürüyüş, zemini yaran eylem, sert katmandaki durak ve dağ boyu böylece aynı imgeye ayrı katkılar sunar: yatayda ve yukarıda sınırları aşma tasarısı belirir. Bu bileşik okuma analojiktir; ayetin fiziksel delme ve erişememe anlamları sürer.

Ayrı ve daha uzak bir keşif çizgisi aynı yürüme sahnesini kısa süreli büyüme hamlesi olarak okur. {ar:تَمْشِ, tr:tamshi, gloss:yürümek} ailesindeki artma ve çoğalma kullanımı genişlemeyi; {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç} için kaydedilen, yağmurdan sonra hızla yeşeren toprak ya da ilk başağını veren ekinle sınırlı kullanım ise ani ve taşkın canlılığı sağlar. {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} ailesindeki yumuşak, bitki yetiştiren verimli zemin bu yeşermenin tutunduğu maddeyi; büyük doğal kütleler olarak {ar:الْجِبَالَ, tr:al-jibāla, gloss:dağlar} kalıcı ölçeği verir. Son olarak {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ailesinin belirli söz kuruluşlarındaki süre kullanımı kısa büyüme hamlesini uzun devamlılıkla karşılaştırır. Yağmur sonrası yeşerme ve ilk başak sözcük kullanımlarının açtığı imgelerdir, ayette anlatılan olaylar değil; verimli zemin ve dağın jeolojik süresi de bu benzetmenin ölçeğidir. Böylece taşkın adımın kısa kabarışı, sağlam ve uzun ömürlü dağ kütlesinin yanında belirir; süre katkısı analojiktir ve ṭūl ailesine genel bir zaman anlamı vermez.

## Yakın Buyruklarda Ölçü

Dağa erişme fiilinin olağan “bir yere varma” anlamı, yakın buyruklarda yaşlılığa erişen ebeveyn sahnesine bağlanır: anne ya da babadan biri veya ikisi kişinin yanında yaşlılığa erişebilir (17:23). Bunun ardından merhametten ebeveyne kanat indirme emri gelir (17:24). {ar:يَبْلُغَنَّ عِندَكَ الْكِبَرَ, tr:yablughanna ʿindaka al-kibara, gloss:yanında yaşlılığa erişmeleri} odaktaki fiilin olağan varış anlamını görünür kılarken, ebeveyne yönelen bakım kendini yukarı taşıyan duruşun karşısına ilişkisel bir alçalış koyar; dağ yüksekliği fiziksel kıyas olarak kalır. {ar:وَاخْفِضْ لَهُمَا جَنَاحَ الذُّلِّ مِنَ الرَّحْمَةِ, tr:wa-khfiḍ lahumā janāḥa al-dhulli mina al-raḥma, gloss:merhametten onlara alçakgönüllülük kanadını indir} içindeki {ar:ذُلّ, tr:dhull, gloss:alçakgönüllülük} aşağılanmayı değil, şefkatle seçilen yumuşak duruşu anlatır. Bu bağlam kanatla birlikte sesin de alçaltılmasını düşündürebilir; sesin alçalması burada ayrı bir sözlük tanımı değil, bağlamsal bir uzantıdır. Kendini üstün görme çağrışımlı {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ile taşkın sevinç anlamındaki {ar:مَرَحًا, tr:maraḥan, gloss:ölçüyü aşan sevinç}, bakımın gerektirdiği alçak edayı karşıt ışıkta gösterir. Böylece yakın bağlam iki ayrı buyruğu karşıt duruşlar olarak yan yana getirir; bu ilişki benzetmeseldir, ebeveyne bakım yürüyüş yasağının nedeni değildir (17:23, 17:24).

Kanat imgesi başka bir hitapta kendisine uyan müminlere yönelir; onlara karşı alçalma buyruğu, ebeveyn sahnesindeki bakıma yeni bir muhatap ve ilişki ekler (26:215). Burada alçak eda takip eden müminlere dönüktür. İki ayrı hitap, fiziksel yükseklik kıyasının yanında başkalarına karşı seçilebilen ilişkisel alçaklığı gösterir; 17:37’deki {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ise bedensel ölçü olarak kalır ve odak buyruğun konusu yürüyüş tarzıdır.

Elin bağlanması, bütünüyle uzatılması ve sonunda tükenmesi, yakın bağlamda kişinin imkânı kullanma ölçüsünü görünür kılar (17:29). Rızkın genişletilmesi ya da ölçüyle daraltılması bu maddi sınırı toplumsal imkâna taşır (17:30). El burada eyleme uzanan araçtır; bu komşuluk odaktaki {ar:تَبْلُغَ, tr:tablugha, gloss:erişmek} fiilinin sözlük anlamını değiştirmez. Aynı erişme ailesinin bir ihtiyacı karşılamaya yetecek düzeye varma kullanımı, sonuna kadar uzanan el ile pay edilmiş rızkı buluşturur; tükenen el yeterliğin sınırını somutlaştırır. {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ailesinin maddi genişlik ve yeterli varlık kullanımı da rızkın açılıp kısılması yanında duyulur, bedenin dağa erişememesi ise fiziksel kıyas olarak sürer. Rızkın dışarıdan ölçüyle daraltılması, kişinin kendi kapasitesini sınırsızca belirleyebileceği iddiasını desteklemez. Bu imkân okuması komşu bağlamdan çıkarılan bir benzetmedir; 17:29 ve 17:30’daki ölçülü harcama buyruğu olarak doğrudan okunuş da kendi yerini korur (17:29, 17:30).

67:15’te kullanıma elverişli yeryüzü üzerinde yürüme ve rızıktan yeme izni, insan kapasitesinin olağan ve meşru işleyişini gösterir; bu sahne 17:37’de sınanan taşkın adıma karşı ölçülü bir kullanım örneği sunar (67:15). 7:74’te düzlüklere saray kurma, dağları evler için yontma ve yeryüzünde bozgunculuktan sakındırılma, aynı yeryüzü-yürüme-dağ ilişkisini gerçek emek ve yapılarla genişletir (7:74). Bu iki sahne, {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ailesindeki bir işi yapmaya yetecek güç ve maddi imkân anlamını yürüme, beslenme ve inşa gibi somut kapasitelerle buluşturur; bozgunculuk uyarısı ise bu imkânın ölçüsüz kullanılabileceğini gösterir. Bağlantı insan kapasitesi düzeyindedir: burada ṭūl doğrudan zenginlik ya da belirli bir ekonomik hüküm bildirmez; 17:37’nin yasağı yemek ve yapı yapmaya uzanmaz.

İmkân sahnelerinin yanındaki 17:32, 17:33 ve 17:34, yaklaşma, güç kullanma ve koruma için ayrı sınırlar kurar. Zinaya yaklaşmama buyruğu ilk sınırı koyar (17:32); Allah’ın dokunulmaz kıldığı can ve öldürmede haddi aşmama, yetki tanınmış olsa bile gücün sınırını belirler (17:33). Yetim malına yaklaşmama ve malı yetim olgunluğa erişinceye kadar koruma ise hak sahipliği ile zamanı birleştirir (17:34). {ar:حَتَّىٰ يَبْلُغَ أَشُدَّهُ, tr:ḥattā yablugha ashuddahu, gloss:güçlü çağına erişinceye kadar} odaktaki {ar:تَبْلُغَ الْجِبَالَ طُولًا, tr:tablugha al-jibāla ṭūlan, gloss:dağlara boyca erişmek} ile olağan erişme anlamını paylaşır; buradaysa erişim bir yaş eşiği ve zamana bağlanır, 17:37’de böyle bir yaş ölçüsü yoktur. Allah’ın koruduğu can, {ar:تَخْرِقَ الْأَرْضَ, tr:takhriqa al-arḍa, gloss:yeryüzünü yarıp geçmek} imgesindeki kuvvetli geçiş tasarısına dokunulmaz hak sınırını ekler. Öldürmede haddi aşmama güç kullanımını, 17:32 ve 17:34’te yinelenen “yaklaşmayın” ise eyleme yaklaşma mesafesini belirginleştirir. Bu yan yanalık üç ayrı hükmü tek bir hareket yasasına dönüştürmez; odaktaki bedenin gösterişli yürüyüşü ve fiziksel ölçülerle ilişkisi ön planda kalır.

Yakın dizide 17:35 ölçüyü hareketten alışverişe taşır: ölçüyü tam verme, doğru terazide tartma, doğruluk ve daha iyi sonuç ticari miktarı ve adil tartıyı açıkça düzenler (17:35). Bu ölçme dili, dağa erişemeyen beden için sabit bir kıyas noktası sağlar; tam ölçü ve doğru tartı, kendine biçilen boyu da doğru kalibre etme benzetmesini açar. {ar:وَأَحْسَنُ تَأْوِيلًا, tr:wa-aḥsanu taʾwīlan, gloss:sonuç bakımından daha iyi} ifadesindeki sonuç ufku bu kıyası anlık yetersizlikten daha uzun bir hesaba taşımayı düşündürür. Ticari tartı doğrudan okunuş olarak yerinde kalır; öz-değerlendirme ve bedenin terazide tartılması komşuluktan doğan, kesinleşmeyen benzetmelerdir, sözcüğe yeni bir sözlük anlamı eklemez.

17:36 ölçüyü bu kez bilginin dayanağına taşır: bilmediği şeyin peşine düşmeme emriyle birlikte işitme, görme ve gönlün sorumluluğu anılır (17:36). Böylece 17:37’deki {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} ayağın bastığı zemin olmayı sürdürürken, kanıtın dayanacağı zemin için de bir benzetme sağlar. Dağlara erişememe bilginin neyi temellendirebileceğine dair olası bir sınır açar; {ar:تَمْشِ, tr:tamshi, gloss:yürümek} ise yönelme imgesi kazanır ve fiziksel adım olarak kalır. 17:36’daki {ar:السَّمْعَ, tr:al-samʿa, gloss:işitme} duyulanı anlayarak dinlemeyi, {ar:الْبَصَرَ, tr:al-baṣara, gloss:görme} olağan görmenin yanında ihtiyatlı bir içgörü rolünü düşündürür. {ar:عِلْمٌ, tr:ʿilmun, gloss:bilgi} iddianın dayanağını, iz sürme fiili {ar:تَقْفُ, tr:taqfu, gloss:iz sürmek} o dayanağın peşine düşmeyi belirginleştirir; {ar:الْفُؤَادَ, tr:al-fuʾāda, gloss:gönül} için önerilen iç alan da kanıtın hükme dönüştüğü yerdir, burada ayrıca bir sözlük tanımı kurulmaz. Aynı bilgi bağlamı, {ar:تَخْرِقَ, tr:takhriqa, gloss:delmek} ailesindeki gereken ölçüyü kuramama ya da işi bilmeden iyi yapamama kullanımını çağırır; fiziksel delme anlamı odakta sürer. Bu, yakın iki yasağın kurduğu bağlamsal bir okumadır: 17:37’nin kendi konusu biliş değildir.

Bilgi sınırı toplumsal dolaşıma taşındığında keşifsel bir söz imgesi açılır. {ar:تَخْرِقَ الْأَرْضَ, tr:takhriqa al-arḍa, gloss:yeryüzünü yarıp geçmek} odağın fiziksel delme eylemini korurken, aynı fiil ailesinin gerçek dışı söz ya da haber uydurma kullanımı konuşmaya ve belirli bir kuruluş biçimine özgüdür; bu kullanım toplumsal imgeye malzeme verir, odaktaki yalın fiilin anlamını değiştirmez. Bilinmeyen şeyin peşine düşmeme buyruğu, dolaşan iddianın dayanağını ve ona takılma hareketini birlikte düşündürür (17:36). Yürüyüş ailesinin belirli bir yapıda insanlar arasında kötüleyici söz taşıma kullanımı da hareketi sözün taşıyıcısına dönüştürür; yalın {ar:تَمْشِ, tr:tamshi, gloss:yürümek} gıybet anlamına gelmez. 68:11’deki iftiracı ve söz taşıyan kişiyi anlatan kalıp bu özel kullanıma somut bir taşıyıcı sağlar (68:11). İki kullanım birleşince doğrulanmamış söz, insanlar arasında kendine geçit açar gibi dolaşır; bu, fiziksel yürüyüşün keşifsel ve sınırlı toplumsal yankısıdır. Bağlamsal dayanak 17:36’daki bilgi ve işitme sorumluluğudur; bu ilişki 17:37’ye ayrı bir gıybet yasağı eklemez.

## Yön, Yol ve Beden

Odaktaki {ar:تَمْشِ, tr:tamshi, gloss:yürümek} iradeyle atılan adımı taşırken, Fâtiha 1:6 doğru yola başkasının hidayetiyle yönelmeyi isteyen bir dua sunar: {ar:اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet}. Böbürlenen adım kendi yönünü tayin eder gibi görünür; dua ise yönü başkasından istemeyi öne çıkarır. Bu analoji Fâtiha 1:6 ile sınırlıdır: odak ayette yol sözcüğü ve ortak kök yoktur, bağlantıyı Fâtiha’nın diğer ayetlerine yayacak ayrı bir dayanak bulunmaz (1:6). Hidayet isteği, 17:37’deki fiziksel yürüyüş yasağının yerini almaz.

Yolun gösterilmesi sorusu 67:22’de bedenlerin yönüne çevrilir: yüzü üzerine kapanmış halde yürüyen kişiyle düzgünce dosdoğru bir yol üzerinde yürüyen kişi karşılaştırılır ve hangisinin daha iyi hidayet üzerinde olduğu sorulur (67:22). Duruş ile izlenen yol birlikte anlam taşır; bu karşılaştırma 17:37’deki fiziksel adımı beden-yön-yol ilişkisi içinde yeniden duyurur. Bağlantı bu beden ve yön ilişkisini aydınlatır; 67:22’deki hesap verme ve algı sorumluluğu kendi bağlamında kalır.

17:95 iki beden duruşundan ayrı bir yeryüzü sahnesinde, huzur içinde yürüyen melekler bulunsaydı diye koşullu bir durum kurar (17:95). Bu sakin yürüyüş kipi, odaktaki gösterişli ve taşkın adıma karşıt bir hareket örneği sunar; koşul varsayımsaldır, bildirilmiş bir olay ya da insanlara verilmiş doğrudan buyruk değildir.

17:97’de bakış varsayımsal meleklerden kıyamet günü yüzleri üzerine toplanan insanlara geçer (17:97). 17:37’de yürüyen kendi adımına yön verirken, burada bedenin yönelişi dışarıdan belirlenir; bu ayrı hidayet ve haşir sahnesi seçilmiş hareket ile zorunlu beden yönünü karşılaştırır. Ayrı bağlamı korununca 17:97, 17:37’nin öngörüsü ya da yakın buyruk dizisinin kapanışı olmaz; katkısı beden yönünün artık kişinin iradesine bırakılmadığı karşıtlığıdır.

## Dizinin Son Hareketi

Bu karşılaştırmalı beden sahnelerinden sonra yakın surenin akışına dönüldüğünde, 17:38’de önceki davranış dizisinin tümü istenmeyen diye nitelenir; hükmün kapsamı yalnız 17:37 ile sınırlı değildir (17:38). 17:39’daki hikmet, taşkınca kendi yönünü tayin eden hareketi gemleyen bir imge olarak okunabilir; gem burada yorumlayıcı imgedir, sözcüğün sözlük anlamı değil (17:39). Ardından edilgen biçimde yere atılma, kınanma ve uzaklaştırılma gelir: {ar:فَتُلْقَىٰ, tr:fa-tulqā, gloss:sonunda yere atılmak}, {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ve {ar:مَدْحُورًا, tr:madḥūran, gloss:uzaklaştırılmış}. Kendi seçtiği yukarı yön böylece dışarıdan dayatılan aşağı harekete, mevki ve yön tayin etme iradesi kaybına döner. {ar:الْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} “yere bağlılık” anlamında kullanılmaz; yere tutunup yükselememe imgesi kişi merkezli duruşu, dağ yüksekliğini ve zorla aşağı atılmayı ağırlık üzerinden buluşturur. {ar:طُولًا, tr:ṭūlan, gloss:boy ölçüsü} ailesinin üstünlük kullanımı bu yükselme arzusunu tersine çevirirken fiziksel boy kıyası sürer. 17:38’deki yargı tüm buyruk dizisine uzanabilir; bu yüzden 17:39’daki düşüş 17:37’deki yürüyüşün kesin sonucu diye sunulmaz, dizinin kendi yönünü dayatan bedeni başkasının yönlendirdiği harekete çeviren imgesidir.

</source_prose>
