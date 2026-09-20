# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:44**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.middle.claims.json`

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
- Refer to source paragraphs as `17:44 ¶N`.

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

`(17:44 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:44",
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
        "citation": "(17:44 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_44/17_44.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_44/17_44.middle.claims.json \
  --ayah-ref 17:44
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_44/17_44.prose.editorial.tr.md`

<source_prose>
17:44, taşıyıcılarını anmadan önce {ar:تُسَبِّحُ, tr:tusabbiḥu, gloss:yüceltir} fiilini duyurur. II. bâbın muzari biçimi yüceltmeyi sürmekte ve pekişmiş bir eylem olarak kurar; şeddeli orta ünsüz söyleyişe işitsel bir yoğunluk da verir. Gökler ve yer daha sonra özne olarak geldiğinde bu fiili yine onlar yönetir: önce eylem, ardından onu taşıyanlar belirir. Fiilin önüne alınan {ar:لَهُ, tr:lahu, gloss:O'na} öznelerden önce alıcıyı, Allah'ı, belirginleştirir. Böylece öne alınan tamamlayıcı övgünün adresini gösterir; Allah'a fayda ya da sahiplik ilişkisi yüklemez.

## Göklerden Her Şeye

İlk özne belirli çoğul biçimdeki {ar:السَّمَاوَاتُ, tr:as-samāwātu, gloss:gökler}dir; hemen yanındaki {ar:السَّبْعُ, tr:as-sabʿu, gloss:yedi}, yeni bir fail değil göklerin niteliğidir. Yedili belirleme bu ilk kozmik alanı düzenli ve tamamlanmış bir bütün gibi duyurur, niceliği simgesel hesaba çevirmeden. Gök sözcüğünün olağan gök anlamına eklenen yukarıda yükselen ya da örten alan çağrışımı, ardından gelen {ar:وَالْأَرْضُ, tr:wa-l-arḍu, gloss:ve yeryüzü} ile üst-alt eksen kurar: yeryüzü yaşanan yer ve yer küresi anlamını korurken aşağı kutbu tutar, göklerse üst kutbu belirginleştirir. Bağlaç yeryüzünü de aynı fiilin eş öznesi yapar; ikisi, aradaki bütün katmanlar tek tek adlandırılmadan, ortak bir övgü alanı açar. Bu bağlamda göğün çağrışımı bulut, yağmur, bitki ya da hava olayına; yeryüzününkü verimlilik, alt yüz ya da hayvan ayağına kaymaz. Yeryüzü ortak özne olarak yaratılmış övgüye katılır; bu dilbilgisel eşlik onu insanlaştırıp insan diliyle konuşturmaz.

Allah'ı tenzih edip yüceliğini bildiren söz 17:43'te ayrı bir kökle kurulur; ardından 17:44'ün gökleri, yeri ve içindekileri övgüye katması, yaratılmışların yönelişini aşkınlık ifadesinin yanına getirir (17:43). Bu geçiş, göğün yaratılmış yükseklik imgesini övgü alanına alırken ilahî yücelikten ayrı tutar: gök Allah'ın bulunduğu yer, yüceliğinin ölçüsü ya da rakibi değildir. İki sözcük ailesi ayrıdır; bu temas göğün yükselme veya örtme çağrışımına dayanır, gerçek bir çatı ya da hava olayı tasvirine değil.

Alanların ardından {ar:وَمَنْ فِيهِنَّ, tr:wa-man fīhinna, gloss:ve onların içinde bulunanlar} aynı övgü fiilinin özne alanına katılır. Buradaki {ar:مَنْ, tr:man, gloss:her kim}, ortak özne listesindeki mevsul grubu kurar; {ar:فِيهِنَّ, tr:fīhinna, gloss:onların içinde} içindeki dişil çoğul ek de yer tamlayıcısını önceki gökler ve yeryüzüne bağlar. Böylece odak alanlardan sakinlerine iner: içindekiler yeni bir gök ya da yer alanı değil, adlandırılmış bu yerlerde yaşayanlardır. Man'ın olağan insan ya da akıl sahibi varlık çağrışımı insan katılımcıları görünür kılar; ardından gelen her-şey hükmü kapsamı insanlarla sınırlamadan genişletir, insan dışı türleri ise tek tek tasnif etmez. Bu, bütün sûreye yayılan bir şema değil, göklerden yere, sakinlere ve sonunda her şeye uzanan ayet içi kapsam sırasıdır.

## Kapsam ve Hamd

Sakinlerin ardından {ar:وَإِنْ, tr:wa-in, gloss:ve hiçbir ... değil} önceki özne listesini koruyarak kapsamı her varlığa taşıyan ayrı bir hüküm açar. Bu yerel kuruluşta {ar:إِنْ, tr:in, gloss:değil} şart değil olumsuzluktur. Vurgulu {ar:مِنْ, tr:min, gloss:hiçbir} ile tekil ve belirsiz {ar:شَيْءٍ, tr:shayʾin, gloss:herhangi bir şey} olumsuzluğu her üyeye ulaştırır; min burada başlangıç ya da kaynak göstermez. Tekil şey adı evrenselliği tek tek varlıklar üzerinden kurar, yalnızca sayılabilir nesnelerle sınırlamaz. Ardından gelen {ar:إِلَّا, tr:illā, gloss:ancak}, yükleme bağlanan bir menteşe gibi, dışarıda bırakma izlenimini hiçbir varlığı dışarıda bırakmayan sonuca çevirir. Bu kapsam parçacığın tek başına anlamı değil, olumsuz-istisna yapısı ile yüklemin birlikte kurduğu etkidir.

Menteşeyi izleyen {ar:يُسَبِّحُ, tr:yusabbiḥu, gloss:yüceltir}, eril tekil {ar:شَيْءٍ, tr:shayʾin, gloss:herhangi bir şey} ile uyum kurarak her tekil varlığa aynı eylemi bağlar. Açılıştaki {ar:تُسَبِّحُ, tr:tusabbiḥu, gloss:yüceltir} gökler öznesiyle dişil tekildir; sonraki yüklem bu biçimin yalın tekrarı değildir. II. bâbın muzari fiili övgü eylemini her üyeye dağıtır ve ilk fiili hatırlatarak özne alanını genişletir. Gökler, yer ve sakinler ortak övgü alanında kalırken, hüküm bütün varlıkları kapsar.

Ayet içindeki kök akışı, {ar:تُسَبِّحُ, tr:tusabbiḥu, gloss:yüceltir} ve {ar:يُسَبِّحُ, tr:yusabbiḥu, gloss:yüceltir} fiillerinden eylemi adlandıran {ar:تَسْبِيحَهُمْ, tr:tasbīḥahum, gloss:onların tesbihi} ismine ilerler. Bu üç biçimin sırası, yaratılmışların yaptığı yüceltmeyi insanların kavrayıp kavrayamadığı adlandırılmış bir olguya çevirir; eylem adı yeni ve bağımsız bir eylem başlatmaz. Sonundaki çoğul iyelik eki tesbihi onu yapan varlıklara bağlar; böylece eylem onlarınki olarak kalır, fakat Allah'tan bağımsız bir kaynak kurulmaz.

Bu eyleme {ar:بِحَمْدِهِ, tr:bi-ḥamdihi, gloss:O'na hamdiyle} bağlanır. Bi, hamdi tesbih fiiline eşlik ya da araç ilişkisiyle taşıyabilir; bu iki imkân açık kalırken sondaki zamir hamdi Allah'a yöneltir. {ar:حَمْد, tr:ḥamd, gloss:övgü ve takdir} yermenin karşıtı olan olumlu övgüdür; iyilik için teşekkür içerebilir, ama ona indirgenmez. Bu bağ, yaratılmışların yüceltmesine olumlu takdir boyutu ekler; hamd tesbihten kopuk ikinci bir eylem olarak kurulmaz.

## Övgünün Yankıları

Yüceltmenin olağan anlamı sürerken, aynı kökün ayrı bir sözlük kolu suda yüzmeyi ya da su ve havada hızlı, akıcı biçimde ilerlemeyi anlatır. Güneş ve ayın yörüngede akışını bildiren ifade bu devinimi somutlaştırır (21:33): {ar:كُلٌّۭ فِى فَلَكٍۢ يَسْبَحُونَ, tr:kullun fī falakin yasbaḥūna, gloss:Her biri bir yörüngede akıp gider}. 17:44'teki II. bâb fiili Allah'ı yüceltme anlamında kalır; temas kök ailesindedir, iki ayetteki biçimlerin özdeşliğinde değil. Yörünge sahnesi övgüye düzenli kozmik seyir imgesi ekler. Gök-yeryüzü çifti bu olası devinime üst-alt bir doğrultu verir; böylece evrensel övgü alanı, yaratılış içinde akıp giden bir icra ihtimaliyle duyulabilir. Bu yankı 21:33'te güneş ve aya bağlıdır; 17:44 için her varlığa ya da yeryüzüne fiziksel yörünge atfetmez, yıldızları ve tek bir övgü biçimini de belirlemez.

Hamdle birleşen tesbih başka bir yönden iki kutuplu bir tanıklık gibi duyulabilir. Olağan yüceltme anlamını taşıyan eylem, Allah'ı kusur ve eksiklikten uzak sayıp yüceltme çağrışımıyla temas eder; hamdin olumlu övgüsü de tanıklığın onaylayan kutbunu kurar. Böylece yaratılmışların hem kusuru reddedip hem Allah'ı olumlu biçimde övdüğü düşünülebilir; bu tanıklık okuması tek bir söylenmiş cümle değildir. Olumsuz-istisna yapısındaki {ar:شَيْءٍ, tr:shayʾin, gloss:herhangi bir şey} bu ihtimalli tanıklığı her varlığa yayar. Hamdın teşekkür ihtimali yerinde kalırken olumlu övgü anlamı sürer; bu özel birliktelik tüm varlıklar için insan dilinde ya da işitilebilir bir söyleyiş dayatmaz.

Yaratılmış katılımın iki ayrı örneği farklı kipleri görünür kılar. Kuşlarla göklerde ve yerdekiler saf tutup dua ve tesbih eder; Allah her birinin duasını ve tesbihini bilir (24:41). Melekler hamdle tesbih ettiklerini ve {ar:نُقَدِّسُ لَكَ, tr:nuqaddisu laka, gloss:Seni her eksiklikten uzak sayarız} dediklerini bildirir (2:30). Bu ayrı fiil, Allah'ı eksiklikten uzak tutma anlamını açar; hamdin olumlu övgüsüyle yan yana geldiğinde iki yönlü tanıklık daha belirginleşirken odaktaki olağan yüceltme anlamı sürer. Örnekler yaratılmış övgünün farklı katılımcı biçimlerini sunar; her varlığa aynı sözlü ya da duyulur kip yüklenmediği gibi meleklerin biçimi de tüm yaratılışa genellenmez.

Gök gürültüsü de ayrı bir doğal katılımcı olarak anılır: {ar:وَيُسَبِّحُ الرَّعْدُ بِحَمْدِهِ, tr:wa-yusabbiḥu al-raʿdu bi-ḥamdihi, gloss:gök gürültüsü O'nu hamdiyle yüceltir} (13:13). Örnek, hamd ile tesbihin bağını somutlaştırır; aynı ayette insanların Allah hakkında tartışmasıyla yan yana durunca doğal övgü ile insan çekişmesi ortak bir sahnede belirir (13:13). Bu birliktelik tesbihin doğal katılımını ve tartışmanın eşzamanlılığını gösterir; gök gürültüsünün nasıl algılandığına ya da insanların onu işitip işitmediğine dair bu bağlantıdan bir sonuç çıkarmaz.

Bu yaratılmış tanıklığı, çevresindeki insan isnatlarıyla karşılaştırınca başka bir anlam kazanır. 17:40'ta insanlara oğullar verilip meleklerden dişilerin Allah'a isnat edilmesi soruyla reddedilir; 17:43'te Allah, kendisine söylediklerinden tenzih edilip büyük yücelikle anılır (17:40, 17:43). 17:44'teki yüceltmenin kusurdan uzak tutma çağrışımı ile övgünün her yaratılmışa yayılması, bu iddiaların karşısına Allah'a yönelen yaratılış tanıklığını koyabilir. Bu bağlantı yakın bağlamdaki reddi genişletir; tanıklığı insan cümlelerine dönüştürmez ve ayetin tek amacını polemikle sınırlamaz.

## Kavrayış ve Alımlama

Her varlığa yayılan hükmün ardından gelen {ar:وَلَٰكِنْ, tr:wa-lākin, gloss:ama} hitabı insan muhataplara çevirir. İkinci çoğul biçimle kurulan hitap dinleyicileri bir toplulukta toplar, bilgilerini eşitlemez. {ar:لَا تَفْقَهُونَ, tr:lā tafqahūna, gloss:derinlemesine kavrayamazsınız} içindeki olumsuzluk insanların kavrayışına yönelir; açık nesne {ar:تَسْبِيحَهُمْ, tr:tasbīḥahum, gloss:onların tesbihi} bu sınırı yaratılışın bütünü yerine varlıkların adlandırılmış eylemine bağlar. Böylece ayet insanın erişimini evrensel övgünün yanına getirir: tesbih sürer, insan onu bütünüyle kavrayamaz. Kavrayış kökünün algılayıp anlayarak bilgiye ulaşma anlamı burada belirli bir eylemi derinlemesine anlama sınırına dönüşür.

Önceki {ar:شَيْءٍ, tr:shayʾin, gloss:herhangi bir şey} geniş varlık anlamını taşımayı sürdürürken, olası “bilinebilir varlık” çağrışımı evrensel kapsama yeni bir bağ kurar: hükme dahil olmak, insanların o varlığın tesbihini bilmesiyle aynı değildir. Bu yankı bir ihtimal olarak kalır, şey adının temel anlamını değiştirmez. Kavrayış sınırı insan dışı ya da sözsüz icraya da yer açar; bir kip seçmeden başka ifade biçimlerini ve duyusal erişim sorusunu açık bırakır.

Aynı kavrayış kökü bir konuşanın sözünü anlama bağlamında da kullanılır: 20:28'deki {ar:يَفْقَهُوا۟ قَوْلِى, tr:yafqahū qawlī, gloss:sözümü kavrasınlar} ifadesinde açık nesne sözdür (20:28). Bu kullanım, 17:44'teki sınırı alıcının anlama eylemi üzerinden düşünmek için bir benzetme sağlar; odağın nesnesi ise yaratılmışların tesbihi olarak kalır. Böylece sözün anlaşılmasına dair örnek, kavrayış fiilini aydınlatır ama 17:44'ün tesbihini sözlü bir ifadeyle özdeşleştirmez.

Anlamadığını söylemek, başka bir bağlamda toplumsal gerilim içinde de ortaya çıkar. 11:91'de bir topluluk elçinin söylediklerinin çoğunu anlamadığını belirtir; ardından gelen tehdit bu iddiayı zorlayıcı bir ilişkiye yerleştirir (11:91). Bu örnek, odaktaki kavrayış sınırını insan alımlamasındaki gerilim yanında düşünmeye açar. Tehdit ve konuşanların saikleri 11:91'in sahnesine aittir; bu okuma onları 17:44'ün muhataplarına yüklemez.

İnsan cevabının başka bir yüzünde sunulan şey ile alıcının tepkisi ayrılır. Kur'an'ın çeşitli biçimlerde anlatılması dinleyenlerde uzaklaşmayı artırır (17:41): {ar:صَرَّفْنَا فِي هَٰذَا الْقُرْآنِ, tr:ṣarrafnā fī hādhā al-qurʾāni, gloss:bu Kur'an'da çeşitli biçimlerde anlattık} ve {ar:وَمَا يَزِيدُهُمْ إِلَّا نُفُورًا, tr:wa-mā yazīdūhum illā nufūrā, gloss:onlarda yalnızca uzaklaşmayı artırır}. Çeşitlenen sunuş ile artan uzaklaşma birlikteyken, açıklamanın sunulması ve alıcının cevabı ayrı kalır. Bu örnek 17:44'teki kavrayış sınırını alımlama yönünden aydınlatır; kendi konusu kozmik tesbih değil Kur'an tilaveti ve dinleyici tepkisidir.

Semûd'a verilen dişi deve açık bir işarettir; aynı bağlamda önceki toplulukların işaretleri yalanladığı da anılır (17:59): {ar:النَّاقَةَ مُبْصِرَةً, tr:an-nāqata mubṣiratan, gloss:açık bir işaret olan dişi deve} ve {ar:كَذَّبَ بِهَا الْأَوَّلُونَ, tr:kadhdhaba bihā al-awwalūn, gloss:öncekiler onu yalanladı}. Görünürlük ile kabulün bu ayrılığı, insanın kavrayış sınırını hiçbir şey sunulmamış olmasıyla karıştırmamayı sağlar. Bu karşılaştırma yalnızca sunulan işaret ile alıcının cevabını ayırır; 17:44'teki tesbihin görünür bir işaret ya da herkesin duyularıyla eriştiği bir nesne olduğunu ileri sürmez.

17:60 başka bir alımlama çizgisi kurar: Peygamber'e gösterilen görüntü insanlar için sınamadır, uyarı ise bazılarında büyük azgınlığı artırır (17:60). Görüntü, sınanma, uyarı ve aşırı tepki sırası, açıklanan şey ile alıcının karşılığını birbirinden ayırır. Bu örnek, 17:44'teki tesbihin görünür bir sınama nesnesi olduğu ya da kavrayış sınırının tek bir saikle açıklanacağı anlamına gelmez; katkısı insan cevabının başka bir biçimini göstermesidir.

Alıcının cevabından erişimin önündeki engellere geçince, 17:45'te Kur'an tilaveti ile dinleyici arasına {ar:حِجَابًا مَسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde} konur (17:45). 17:46 kalpteki {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} ile kulaktaki {ar:وَقْرًا, tr:waqran, gloss:ağırlık} imgesini ekler; aynı kavrayış kökü tilaveti anlamayı anlatan {ar:يَفْقَهُوهُ, tr:yafqahūhu, gloss:onu kavrasınlar} biçiminde yeniden belirir (17:46). Dış perde, içteki kalp örtüleri ve kulak ağırlığı ayrı erişim katmanlarıdır; bir işaretin hiç sunulmaması ile sunulanı kavrayamama arasındaki farkı görünür kılar.

Bu dizide dinleyiciler tilaveti gerçekten işitir: 17:47'de {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinlerken} denir (17:47). Böylece işitme ile kavrama ayrılır; sesin alınması, anlamanın tamamlandığını garanti etmez. Belirli dinleyicilere ve Kur'an tilavetine ait bu zincir, 17:44'teki insan sınırını erişim benzetmesiyle aydınlatır; odaktaki tesbihin duyusal kipini ya da bu sınırın nedenini belirlemez.

## Düzen ve Maddi Değişim

İnsan kavrayışından kozmik düzene dönünce, 23:71 başka bir koşul kurar: hak insanların arzularına uysaydı gökler, yer ve içindekiler bozulurdu; ardından insanlar hatırlatmadan yüz çevirir (23:71). Bu karşıtlık, evrensel övgü alanını insan arzusundan bağımsız kozmik düzenle ilişkilendirip ahlaki ölçeği genişletir. Bu bağlantıda 23:71 bir karşıtlık sunar: oradaki konu bozulma ve hatırlatmadan yüz çeviriştir, tesbih değil; odak ayetin yerel bir suçlamaya yanıt verdiğini de kanıtlamaz.

Aynı gökler ve yer, başka bir sahnede ilahî buyruğa istekle karşılık verir: {ar:أَتَيْنَا طَآئِعِينَ, tr:ataynā ṭāʾiʿīna, gloss:isteyerek geldik} (41:11). Bu yanıt, 17:44'te övgüyü taşıyan alanın eyleyiciliğine ayrı bir görünüm ekler. Buradaki katkı gökler ile yerin gönüllü karşılığıdır; bu, tesbihin başka adı ya da tüm varlıklar için bir konuşma iddiası değildir.

Evrensel {ar:شَيْءٍ, tr:shayʾin, gloss:herhangi bir şey} hükmü maddi dağılma sorusuyla sınanır. İnsanlar kemik ve kırıntı olduklarında yeniden yaratılıp yaratılmayacaklarını sorar (17:49): {ar:أَئِذَا كُنَّا عِظَامًا وَرُفَاتًا, tr:a-idhā kunnā ʿiẓāman wa-rufātan, gloss:kemik ve kırıntı olduğumuzda mı} ve {ar:لَمَبْعُوثُونَ خَلْقًا جَدِيدًا, tr:la-mabʿūthūna khalqan jadīdan, gloss:yeni bir yaratılış olarak diriltilecek miyiz}. Evrensel şey kapsamı, dağılmış kalıntıları da varlık alanında tutar; parçalanma görünen maddi hâli değiştirir, ama kapsamı kendi başına kesmez. Bu karşılaşma övgüyü şimdiki maddenin görünüşüne indirgemeden düşünmeye açar; diriliş sonrası eylemin biçimi bu bağlantının konusu değildir.

Soru bu kez direncin uçlarına gider: 17:50'de muhataplardan taş ya da demir olmaları istenir (17:50): {ar:كُونُوا حِجَارَةً أَوْ حَدِيدًا, tr:kūnū ḥijāratan aw ḥadīdan, gloss:taş ya da demir olun}. Bu sert maddeler evrensel övgünün kapsamına karşı bir sınama oluşturur; katılık kapsam dışı kalmanın ölçüsü olmaz. Ardından “Kim bizi geri döndürecek?” sorusu ilk yaratılışa döner (17:51): {ar:مَن يُعِيدُنَا, tr:man yuʿīdunā, gloss:kim bizi geri döndürecek}. Böylece maddi dirençten geri dönüşe geçilir; ilk yaratılış, değişimin ötesinde yeniden yaratılma sorusuna dayanak olur.

Bu geri dönüş, insanın gelecekteki cevabına ulaşır. Çağrı karşısında insanlar hamd ederek karşılık verir (17:52): {ar:يَدْعُوكُمْ, tr:yadʿūkum, gloss:sizi çağırdığında} ve {ar:فَتَسْتَجِيبُونَ بِحَمْدِهِ, tr:fa-tastajībūna bi-ḥamdihi, gloss:O'na hamd ederek karşılık verirsiniz}. Buradaki hamd, 17:44'teki {ar:بِحَمْدِهِ, tr:bi-ḥamdihi, gloss:O'na hamdiyle} ile yankılanır; evrensel övgüye farklı bir özne ve gelecek zamanla somut bir insan cevabı ekler. Bu örnek, taş ve demir imgesine söz yüklemez; insanın yanıtı da her tesbihin tek bir sözlü kalıpta gerçekleştiğini belirlemez.

## Tek Adres, Farklı Sesler

Gelecekteki bu cevabın yanında Fâtiha 1:5 şimdiki zamanda birinci çoğul insan sesi kurar: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:Yalnız Sana kulluk eder ve yalnız Senden yardım isteriz} (1:5). 17:44'teki {ar:لَهُ, tr:lahu, gloss:O'na} yönelişiyle aynı ilahî adreste buluşması, insanın kendi kulluk ve yardım isteğini daha geniş yaratılmış övgüsü içindeki bir ses olarak işitmesine imkân verir. Bu benzerlik insanın ritüel kulluğunu öteki varlıkların tesbih kipiyle özdeşleştirmez ya da onların nasıl övdüğünü bildiğini varsaymaz.

Tek alıcıya yönelen bu çoğulluk, komşu bağlamlardaki arayışla birlikte okunabilir. 17:42'de varsayılan rakip ilahların Arş'ın sahibine bir yol arayacakları söylenir: {ar:لَابْتَغَوْا إِلَىٰ ذِي الْعَرْشِ سَبِيلًا, tr:la-btaghaw ilā dhī al-ʿarshi sabīlā, gloss:Arş'ın sahibine bir yol ararlardı} (17:42). Bu koşullu sahnede varsayılan rakipler de yönelinen merkez değil, ona yol arayanlar olarak belirir; böylece 17:44'teki {ar:لَهُ, tr:lahu, gloss:O'na} tek alıcı vurgusuyla bir yankı kurar.

Bağımlı arayış başka bir yönden 17:56 ve 17:57'de açılır. 17:56'da Allah dışında çağrılanlar zararı giderme gücüne sahip değildir; onları çağırma buyruğu bu sınırı görünür kılar: {ar:لَا يَمْلِكُونَ كَشْفَ الضُّرِّ عَنكُمْ, tr:lā yamlikūna kashfa al-ḍurri ʿankum, gloss:zararı sizden giderme gücüne sahip değiller} ve {ar:ادْعُوا, tr:udʿū, gloss:çağırın} (17:56). 17:57'de aynı çağrılan varlıkların kendileri Rablerine yakınlık arar, rahmetini umar ve azabından korkar (17:57): {ar:أُولَٰئِكَ الَّذِينَ يَدْعُونَ يَبْتَغُونَ إِلَىٰ رَبِّهِمُ الْوَسِيلَةَ, tr:ulāʾika alladhīna yadʿūna yabtaghūna ilā rabbihimu al-wasīlata, gloss:çağırdıkları varlıklar Rablerine yaklaşma yolu ararlar} ve {ar:يَرْجُونَ رَحْمَتَهُ وَيَخَافُونَ عَذَابَهُ, tr:yarjūna raḥmatahu wa-yakhāfūna ʿadhābahu, gloss:rahmetini umar ve azabından korkarlar}. Üç sahne birlikte, çağrılanların da kendilerinden daha yüce bir merkeze bağlı arayanlar oluşunu öne çıkarır. Bu, komşu ayetlerden doğan olası bir paralelliktir: polemik övgüyle yan yana ilerleyebilir, ancak göklerin içindekiler ne varsayılan rakiplerle ne de çağrılanlarla özdeşleştirilir.

Göklerde ve yerdekilerin tesbihinden sonra mülkün ve hamdin Allah'a ait olduğunu söyleyen 64:1, aynı ilahî muhatabı övgü ve egemenliğin merkezi yapar (64:1). Böylece odaktaki yöneliş, bu ayrı bağlamda mülkün de aynı merkeze ait oluşuyla genişler; bu yankı aracılar ya da rakip ilahlar hakkında başlı başına bir hüküm kurmaz.

Alıcıdan ayrı bir eksen de süredir. Gece gündüz tesbih edip gevşememeyi anlatan ifade övgüye kesintisiz zaman boyutu ekler (21:20): {ar:يُسَبِّحُونَ ٱلَّيْلَ وَالنَّهَارَ لَا يَفْتُرُونَ, tr:yusabbiḥūna al-layla wa-n-nahāra lā yafturūna, gloss:gece gündüz tesbih eder ve yorulmazlar}. Bu zaman yankısı 21:20'deki katılımcılarına bağlı kalır; burada özne ve biçim belirtilmediğinden aynı gece-gündüz düzeni 17:44'teki her varlığa taşınmaz.

## Kapanışın Nitelikleri

İnsan kavrayışının ardından gelen {ar:إِنَّهُ, tr:innahu, gloss:şüphesiz O/bu}, açıklamayı güçlü bir ilahî yükleme bağlar. Zamir doğrudan Allah'a da az önce kurulan hükmün kendisine de dönebilir; kapanış bu iki gönderimden birini zorunlu kılmaz. {ar:كَانَ, tr:kāna, gloss:idi/olagelmiştir} ile {ar:حَلِيمًا غَفُورًا, tr:ḥalīman ghafūran, gloss:halîm ve çok bağışlayıcı} aynı yüklem yapısında birleşir. Kāna'nın geçmiş biçimi burada tamamlanmış bir olayı değil yerleşik bir niteliği bildirir; bu okuma daha geniş bir zamansızlık öğretisi kurmaz.

Yüklem önce {ar:حَلِيمًا, tr:ḥalīman, gloss:halîm}, ardından ayrı bir niteleme olan {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} sıfatını getirir. Bu sıra önce kendini tutma niteliğini, sonra bağışlayıcılığı duyurarak kapanışın akışını kurar; nitelikler özdeş ya da önem bakımından dereceli değildir. Yoğun ghafūr kalıbı bağışlamanın bol oluşunu vurgular; son sözcük olarak bağışlanma ayetin kapanış sesini taşır.

Halîm'in taşkınlığa kapılmadan kendini tutma anlamı, insanların tesbihi kavrayamamasından sonra gelince, karşılık verebilecek olanın aceleci karşılığını tutması gibi duyulabilir. Ghafūr'un ardından gelişi bu yerel sıralamayı ihtimalli bir karşılık ilişkisine açar: kavrayamamak suç sayılmaz, belirli bir ceza ya da esirgenen ceza da adlandırılmaz. Halîm böylece insani öfke veya psikoloji değil, aceleci karşılığa kapılmayan ilahî sükûneti anlatır.

Ghafūr'un olağan anlamı bağışlamadır; bu bağışlamanın kişiyi cezadan koruyup sığınak olabilmesi de ikincil bir imkân sunar. Kökün örtüp koruma çağrışımıyla, sonraki iki ayetteki engelleyici imgeler işlevsel bir karşıtlık kurar (17:45, 17:46): dış perde {ar:حِجَابًا مَسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir perde}, kalp örtüleri {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler} iletilenin alımlanmasını sınırlar. Bağışlamanın koruyucu örtüsü ile tilaveti perdeleyen bu engellerin kelime aileleri ayrıdır; benzetme ghafūr'a sığınak rengi eklerken anlamını bağışlama olarak tutar ve belirli bir kusur, ceza ya da gizleme eylemi atfetmez.

Aynı {ar:حَلِيمًا غَفُورًا, tr:ḥalīman ghafūran, gloss:halîm ve çok bağışlayıcı} nitelikleri, 35:41'de Allah'ın gökleri ve yeri yerinden oynamaktan alıkoyup tuttuğu anlatımın sonunda da gelir (35:41). Bu kez kozmik koruma görüntüsünü, tutuş tamamlandıktan sonra gelen hilim ve bağışlama adları izler; böylece kapanış insanın tesbihi kavrayışından düzenin sürmesine doğru genişler. Bu bağlamda sıfatlar tutuşun nedeni ya da tesbihin kendisi değil, kozmik korunmayla yan yana anılan niteliklerdir.

</source_prose>
