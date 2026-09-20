# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:4**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.middle.claims.json`

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
- Refer to source paragraphs as `17:4 ¶N`.

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

`(17:4 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:4",
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
        "citation": "(17:4 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_4/17_4.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_4/17_4.middle.claims.json \
  --ayah-ref 17:4
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_4/17_4.prose.editorial.tr.md`

<source_prose>
Âyet, İsrailoğullarına Kitap'ta şu hükmü bildirir: yeryüzünde iki kez bozgunculuk yapacak ve büyük bir yükselişle yükseleceklerdir. Başındaki {ar:وَ, tr:wa, gloss:ve}, tamamlanmış {ar:قَضَيْنَآ, tr:qaḍaynā, gloss:hükme bağladık} fiiline eklenip önceki söz akışını sürdürürken yeni hükmü de açar; 17:3'teki soy anışı bu yakın bağlamı verir, 17:4'ün yerel bildirimi ise kendi başına anlaşılır. Fiil bir belirleme ve yargılama eylemini tamamlanmış olarak sunar. {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} ile kurduğu özel yönelme kalıbı, hükmü adı verilen alıcıya kesin bir bildirim, ahit ya da talimat olarak ulaştırır. Bu kalıpta yön, hükmün fiziksel varış yerini değil, alıcısını belirler: {ar:بَنِىٓ إِسْرَٰٓءِيلَ, tr:banī isrāʾīla, gloss:İsrailoğulları}. Alıcının {ar:فِى ٱلْكِتَٰبِ, tr:fī al-kitābi, gloss:Kitap'ta} çerçevesinden önce gelmesi, söylemde önce kime seslenildiğini, sonra hükmün nerede kayıtlı olduğunu öne alır; bu sıra topluluğun önem derecesini belirlemez. {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} tarafından yönetilen tamlamadaki çoğul-genitif {ar:بَنِىٓ, tr:banī, gloss:soyundan gelenler}, gerçek çocukluk ve soy bağını taşır; ardından gelen yabancı özel ad İsrail bu soyun kime ait olduğunu belirler. Özel adın bu işlevi, adın kökeninden ayrıca bir sözlük anlamı çıkarmayı gerektirmez.

## Soy Çizgisinde Rehberlik

Soy adı, bu topluluğun daha önce aldığı yönlendirmeyi de duyurur. 17:2'de Musa'ya verilen {ar:ٱلْكِتَٰبَ, tr:al-kitāba, gloss:Kitap}, aynı topluluk için {ar:هُدًى لِّبَنِىٓ إِسْرَٰٓءِيلَ, tr:hudan li-banī isrāʾīla, gloss:İsrailoğullarına yol gösterici} diye nitelenir ve {ar:أَلَّا تَتَّخِذُوا۟ مِن دُونِى وَكِيلًا, tr:allā tattakhidhū min dūnī wakīlan, gloss:benden başka bir koruyucu edinmeyin} buyruğuyla bir sınır çizer (17:2). 17:3'te aynı topluluk {ar:ذُرِّيَّةَ مَنْ حَمَلْنَا مَعَ نُوحٍ, tr:dhurriyyata man ḥamalnā maʿa nūḥin, gloss:Nuh'la birlikte taşıdıklarımızın soyu} diye anılır (17:3). Rehberlik, koruyucuya ilişkin buyruk ve taşınmış soy çizgisi aynı muhatapta buluşunca, 17:4'teki bozgunculuk öngörüsü alınmış yönlendirme içindeki bir ihlâl olarak ağırlaşır; komşu ayetlerin bu basıncı, {ar:قَضَيْنَآ, tr:qaḍaynā, gloss:hükme bağladık} bildirimine sorumluluk yükleyen bağlayıcı bir buyruk yönü de kazandırır. Nuh'la birlikte taşınmış olmayı anmak nimeti hatırlatır; sorumluluğu atadan toruna aktararak soya kalıtsal suç yüklemez.

## Yazılı Çerçeve ve Yeryüzü

17:4'teki {ar:فِى ٱلْكِتَٰبِ, tr:fī al-kitābi, gloss:Kitap'ta} öbeğinde {ar:فِى, tr:fī, gloss:içinde} doğrudan Kitap sözcüğünü yönetir. Öngörü cümlelerinden önce durması, yazılı çerçevenin Kitap'la sınırlı mı kaldığını, yoksa ardından gelen iki yükleme de mi uzandığını açık bırakır. Vasl okuyuşunda {ar:فِى, tr:fī, gloss:içinde} ile {ar:ٱلْكِتَٰبِ, tr:al-kitābi, gloss:Kitap} tek bir ses akışı gibi bağlanır; Kitap hükmü taşıyan bitişik bir öbek olarak işitilir. Belirlilik takısı yazılı metni tanınır bir kayıt hâline getirir; bu kayıt belirli bir tarihî nüshayla sınırlandırılmaz. Temel okuyuşta ad tekildir; bildirilen {ar:ٱلْكُتُبِ, tr:al-kutubi, gloss:Kitaplar} çoğul biçimi yazılı tanıklığın kapsamını genişletirken iki öngörünün içeriğini korur. Böylece tekil ve çoğul kapsam birlikte açık kalır.

Kitap burada yazılmış metin ve kayıt anlamını korur; aynı sözcük ailesinin ayrı bir kullanımı ise yazıyla geçerli kılınan bağlayıcı hükmü, yükümlülüğü ya da önceden belirlenmiş sonucu anlatır. Bu anlam, yazılı kararın bir hükmü bağlayıcı kıldığı durumda işler; yazdırma ve yazmayı öğretme başka yapılara bağlıdır. Tamamlanmış {ar:قَضَيْنَآ, tr:qaḍaynā, gloss:hükme bağladık} fiiliyle ardından gelen iki vurgulu gelecek bildirimi, kaydın hükmü saptayıp yürürlüğe koyan yönünü de duyurur. Böylece bağlayıcılık yazılı kaydın üzerine eklenir: Kitap kayıt olarak kalır, hüküm fiilinin yerini almaz ve ikinci bir kutsal metin kurmaz.

Tekrarlanan {ar:فِى, tr:fī, gloss:içinde} önce hükmü Kitap'a, sonra eylemi {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍi, gloss:yeryüzünde} yazar. İki öbek kayıtla yaşanan yeri ayrı alanlarda tutarken birbirine de cevap verir. {ar:ٱلْأَرْضِ, tr:al-arḍi, gloss:yeryüzü}ndeki belirlilik yaşanan geniş zemini tanınır kılar; yerel bir ülke çağrışımı bu geniş anlam içinde kalır ve belirli bir coğrafya adı vermez. Aynı sözcük ailesindeki bir şeyin alt bölümünü ya da ayağın yere değen kısmını anlatan kullanımlar belirli tamlamalara bağlıdır; burada yalın yeryüzü anlamı taşınır. Cümle önce eylemi, sonra alanını, ardından {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} sayısını verir. Yeryüzü böylece yükselişin yukarı yönüne karşı yaşanan zemin ve aşağı alan katkısını sunar; bu mekânsal karşıtlık, tek başına baskıcı bir hedef belirlemez.

Bu alanda {ar:لَتُفْسِدُنَّ, tr:la-tufsidunna, gloss:mutlaka bozarsınız} ikinci çoğul muhatabı IV. bâbın ettirgen fiiliyle bozulmanın faili yapar: düzgün ve elverişli durumdaki bir şeyi bozup o durumdan çıkarırlar. {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍi, gloss:yeryüzünde} bu eylemi soyut bir ahlak etiketinden yaşanan düzene taşır; fiil burada yeryüzündeki düzenin elverişliliğini yitirmesini anlatır. İkinci çoğul eki az önce adlandırılan topluluğu özne olarak geri çağırır. Kitap çerçevesinin hemen ardından gelen {ar:لَ, tr:la-, gloss:vurgulama lâmı} ilk suçlamanın fiiline vurgu taşır; lâm ile sonundaki ağır nûn bozmayı ihtimal değil, kesin ve güçlü bir gelecek öngörüsü yapar. “Yemin gibi” nitelemesi bu gramatik kuvveti belirtir, ayrı bir yemin formülü kurmaz. Aktarılan edilgen ya da bozulmayı öznenin kendi durumuna çeken biçimler eyleyenliği başka türlü kurar; temel ettirgen biçimin dışa dönük sorumluluğu korunur ve okuyuşlar arasında üstünlük sırası kurulmaz.

Yeryüzünün bu geniş alanı, 17:5'te yerleşim içindeki bir güzergâha yaklaşır. Oradaki ayrı sevk eylemi {ar:بَعَثْنَا, tr:baʿathnā, gloss:gönderdik} ile açılır; gönderilen kuvvetin {ar:فَجَاسُوا۟ خِلَٰلَ ٱلدِّيَارِ, tr:fa-jāsū khilāla al-diyār, gloss:meskenlerin arasından dolaştılar} geçişi hareketi evlerin ve aralıkların içinden geçirir (17:5). {ar:خِلَٰلَ, tr:khilāla, gloss:aralarından} boşluk ve geçitlerden ilerleyişi, {ar:ٱلدِّيَارِ, tr:al-diyār, gloss:meskenler} evleri ve sakinlerin ortak toplumsal alanını verir. Bu mekânsal geçirgenlik, odaktaki bozgunculuğu hane ve kent dokusuna yayılan bir düzen kaybı olarak duyurabilir. 17:5'teki sevk ve geçiş daha sonraki bir girişin faili olabilir; bu özel temas odaktaki bozulmanın kesin nedenini belirlemez. Yerleşim içindeki güzergâh yeryüzünün genişliğinden dardır; istilayı olası bir bağlam olarak açar, her bozgunculuğu istilayla özdeşleştirmez ya da belirli bir tarihî olayı saptamaz.

Yeryüzü zeminiyle görünen yükselişin karşılaşması, malzemeye ilişkin iki ayrı benzetme dalını açar. Yeryüzünü anlatan sözcük ailesinin dar bir kullanımında odunla beslenen küçük bir canlı, buna bağlı başka bir kullanımda da onun yemesiyle aşınmış odun anılır. Ettirgen bozulmayla yukarıda görünen yükseliş bu dalı etkinleştirince zemin, sağlamlığını içeriden yitiren bir malzeme gibi duyulur; bu canlı ve odun, yeryüzü sözcüğünün buradaki temel anlamı değil, onun ayrı kullanım yankılarıdır. Yara ile kurulan tamlamaya bağlı başka bir kullanım, irin biriktirip kabararak bozulan yarayı anlatır. Bu dal, aynı bozulmayı içeriden yayılan ve irinlenir gibi kabaran bir hasar olarak somutlaştırır; katkısı odun imgesinden ayrıdır ve tıbbi bir olgu bildirmez. Her iki imgenin yanında {ar:ٱلْأَرْضِ, tr:al-arḍi, gloss:yeryüzü} yaşanan, göğe karşı aşağıdaki zemini; {ar:وَلَتَعْلُنَّ, tr:wa-la-taʿlunna, gloss:ve mutlaka yükseleceksiniz} ile {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yükseliş} olağan yukarı çıkışı taşır. “Alt bölüm” anlamı yine belirli tamlamalara bağlıdır; bu karşıtlık hasarlı zeminle görünen yükseklik arasındadır, gerçek bir bina ya da fiziksel çöküş tasviri değildir.

## İki Sayım, İki Vuruş

İlk suçlamadaki {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez}, bozulma eyleminin iki tam gerçekleşmesini sayan ikil biçimdir; neyin sayıldığını {ar:لَتُفْسِدُنَّ, tr:la-tufsidunna, gloss:mutlaka bozarsınız} yüklemi verir. İkil, olayların tarihini, süresini ya da rotasını değil, tekrar adedini belirler. İçindeki ikizleşmiş r sesi iki sayısını kulağa da duyuran bir yankı kurar. Aynı sözcük ailesindeki ayrı duyusal kullanım yalnız yiyecek ve içecek gibi tadılabilen şeylerde acı tadı ya da acılaşmayı anlatır. Bozucu eylemin yıkıcı niteliği bu dar dalı benzetmeli olarak etkinleştirir: iki gerçekleşme acı bir ton kazanır; tat, sayı sözcüğünün temel anlamına dönüşmez.

İkil, çevredeki dönüş anlatısıyla birlikte hem tam iki gerçekleşmeyi sayar hem yinelenmenin mümkün olduğu bir ritme açılır. 17:5'te {ar:فَإِذَا جَآءَ وَعْدُ أُولَىٰهُمَا, tr:fa-idhā jāʾa waʿdu ūlāhumā, gloss:ikisinin ilkinin vaadi geldiğinde} ilk eşik kurulur (17:5). 17:6'da {ar:ثُمَّ رَدَدْنَا لَكُمُ ٱلْكَرَّةَ عَلَيْهِمْ, tr:thumma radadnā lakumu al-karrata ʿalayhim, gloss:sonra üstünlüğü size onlara karşı geri verdik} sözü önceki konumu geri getirir; {ar:ٱلْكَرَّةَ, tr:al-karrata, gloss:geri dönüş} dönüşü iki gerçekleşme arasındaki ritme taşır (17:6). Aynı ayette {ar:وَأَمْدَدْنَٰكُم بِأَمْوَٰلٍۢ وَبَنِينَ, tr:wa-amdadnākum bi-amwālin wa-banīna, gloss:mallar ve oğullarla destekledik} yenilenen konuma kaynak ve kuvvet ekler; {ar:وَجَعَلْنَٰكُمْ أَكْثَرَ نَفِيرًا, tr:wa-jaʿalnākum akthara nafīran, gloss:sizi daha kalabalık kıldık} topluluğun sayısal gücünü belirtir (17:6). 17:8'deki {ar:إِنْ عُدْتُمْ عُدْنَا, tr:in ʿudtum ʿudnā, gloss:siz dönerseniz biz de döneriz} koşulu da eylemle karşılığı karşılıklı dönüş içinde buluşturur (17:8). Bu dizilim tam iki sayımını korurken yinelenme olasılığını açar; sabit iki olayı dışlamaz, fakat bunlara tarih ya da fail vermez ve yenilenen kaynakları sonraki bozgunculuğun nedeni yapmaz.

Sayıyla yazılı hükmün buluşması, iki eylemi önceden belirlenmiş kaydın içeriği gibi duyurur. {ar:قَضَيْنَآ إِلَىٰ, tr:qaḍaynā ilā, gloss:alıcısına hüküm bildirdik} kalıbının ulaştırdığı karar {ar:فِى ٱلْكِتَٰبِ, tr:fī al-kitābi, gloss:Kitap'ta} yer alır; tamamlanmış hüküm, iki vurgulu gelecek bildirimi ve kesin {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} sayısı kaydı gelecekte bildirilenle birleştirir. Ettirgen fiil iki tam eylemi bu sayıya bağlar. Bu yankı Kitap'ı hüküm fiiliyle özdeşleştirmez; kayıt sabitliğini duyururken olayların tarihini ya da kimliğini belirtmez.

İki öngörü yan yana iki ayrı yüklem kurar. {ar:لَتُفْسِدُنَّ فِى ٱلْأَرْضِ, tr:la-tufsidunna fī al-arḍi, gloss:yeryüzünde mutlaka bozgunculuk yapacaksınız} eylemi, alanı ve iki sayısını verir; eşgüdümle gelen {ar:وَلَتَعْلُنَّ عُلُوًّا كَبِيرًا, tr:wa-la-taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle mutlaka yükseleceksiniz} yükselişin kendisine ve büyüklüğüne ayrı bir içerik ekler. Her iki fiildeki vurgulama lâmı ve ağır nûn öngörüleri aynı kesinlikte kurar; ikinci suçlama ilkinin eşanlamlı tekrarı değildir. {ar:وَلَ, tr:wa-la, gloss:ve vurgulama lâmı} başlangıcı, bağlaçtan hemen sonra lâmı yeniden duyurarak ikinci bir işitsel vuruş açar; ikinci fiilin ağır sonluğu ilkinin kapanışına denk bir mühür koyar. Bu ses düzeni iki öngörünün eşit vurgusunu ayette tamamlar; sonraki bir anlatının sonucunu yüklemlere taşımaz.

İkinci yüklemin hareketi önce olağan yukarı çıkmadır. {ar:وَلَتَعْلُنَّ, tr:wa-la-taʿlunna, gloss:ve mutlaka yükseleceksiniz} yalın I. bâb fiilidir: adı verilen topluluk kendisi yükselir. Fiil hedefini dışarıda adlandırmaz; bu sözdizim toplumsal etki olasılığına açık kalır. Ardındaki {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yükseliş}, fiille aynı kökten gelen belirsiz mansup mastardır ve yükselme eylemini süreç olarak adlandırır. Mastarın nesne benzeri görevi süreci belirginleştirir; fiili ettirgen yapmaz, bir kurban da tayin etmez. Temel biçim yükselme anlamını korur, bildirilen biçim farkları da bu alanı sürdürür.

{ar:كَبِيرًا, tr:kabīran, gloss:büyük}, {ar:عُلُوًّا, tr:ʿuluwwan, gloss:yükseliş}ı doğrudan niteler; ölçü ve derece bakımından genel büyüklüğü yükselişin kendisine yükler. İki belirsiz mansup sözcüğün ortak -an kadansı onları tek bir son öbekte birleştirip hareketin ağırlığını duyurur. Sıfat yükselişin ölçeğini belirler; yaş bildirmez, karşılaştırmalı bir rakip ya da sınırsız bir ölçü kurmaz.

## Yükselişin İnsanî Yüzü

İnsan muhataplara yönelen olağan yükselme dili, aynı sözcük ailesindeki kınanan kendini üstün görme ve taşkınlık kullanımını da etkinleştirir. {ar:وَلَتَعْلُنَّ عُلُوًّا كَبِيرًا, tr:wa-la-taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle yükseleceksiniz} ifadesindeki {ar:كَبِيرًا, tr:kabīran, gloss:büyük} öz-yüceltmenin ölçeğini yoğunlaştırır. Kınama yükselme sözcüğüne değil, insanın kendini üstün görmesine yönelir. {ar:لَتُفْسِدُنَّ فِى ٱلْأَرْضِ, tr:la-tufsidunna fī al-arḍi, gloss:yeryüzünde mutlaka bozgunculuk yapacaksınız} suçlamasının zararıyla yükselme suçlaması birbirini ahlaken aydınlatır; iki yüklem ayrı kalır ve aralarında neden-sonuç kurulmaz. Ayet bu bağlantıda rakip, kurban ya da fetih hedefi belirlemez; okuma muhatapların öz-yüceltmesiyle yeryüzündeki zararı yan yana tutar.

Yeryüzündeki bozulma bu insanî üstünlük yorumunu toplumsal baskı yönünde koyulaştırır. {ar:لَتُفْسِدُنَّ, tr:la-tufsidunna, gloss:bozgunculuk yapacaksınız}ın zararı ve {ar:فِى ٱلْأَرْضِ, tr:fī al-arḍi, gloss:yeryüzünde}nin açık alanı, yükseliş ailesindeki yeryüzü üzerinde üstünlük taslama ve başkalarını bastırma kullanımını bağımsız olarak tetikler; {ar:وَلَتَعْلُنَّ عُلُوًّا كَبِيرًا, tr:wa-la-taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle yükseleceksiniz} büyüklüğü bu tonu yoğunlaştırır. Bu okuma kolektif zararı baskıcı güç tavrıyla yan yana getirir; belirli bir yönetici, karşı taraf ya da hedef atamaz.

17:43'te önce {ar:سُبْحَٰنَهُۥ, tr:subḥānahu, gloss:O münezzehtir}, ardından {ar:وَتَعَٰلَىٰ, tr:wa-taʿālā, gloss:ve yücedir} gelir; aynı {ar:عُلُوًّا كَبِيرًا, tr:ʿuluwwan kabīran, gloss:büyük bir yücelikle} öbeği burada başka bir göndergeyi anlatır (17:43). Bu yankı, 17:4'teki {ar:تَعْلُنَّ عُلُوًّا كَبِيرًا, tr:taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle yükseleceksiniz} kınamasını kökün kendisinden insanın kendini üstün görmesine taşır: 17:43 aynı söz öbeğini farklı ilişkide kınama olmadan kullanır. Karşılaştırma öbek düzeyindedir; iki ayetin dilbilgisel kuruluşunu birleştirmez ve ayrı bir inanç önermesi ileri sürmez.

Bağımsız bağlamlar bu ahlaki okumaya kamusal bir zemin sağlar. 28:4'te Firavun'un {ar:عَلَا فِي الْأَرْضِ, tr:ʿalā fī al-arḍi, gloss:yeryüzünde yükseldi} diye anılması, bir topluluğu ezip güçsüz bırakması ve {ar:مِنَ الْمُفْسِدِينَ, tr:minal-mufsidīn, gloss:bozgunculardan biri} sayılmasıyla yan yana gelir (28:4). 28:83'te ise {ar:لَا يُرِيدُونَ عُلُوًّا فِي الْأَرْضِ وَلَا فَسَادًا, tr:lā yurīdūna ʿuluwwan fī al-arḍi wa-lā fasādan, gloss:yeryüzünde üstünlük kurmayı ve bozgunculuğu istemezler} iki eğilimi birlikte reddeder (28:83). Bu iki anlam paraleli 17:4'teki ettirgen bozulmayı kolektif zarara, büyük yükselişi de bir düzen içinde başkalarını bastıran üstünlüğe bağlamaya zemin verir (28:4, 28:83). Bağ, anlam düzeyinde kalır: 28:4'ün ayrı fiil biçimi 17:4'ün dilbilgisini çözümlemez; Firavun odaktaki muhatapların yerine geçmez ve bu siyasal baskı örneği her bozgunculuğun tanımı olmaz.

Kamusal güç çağrışımı kutsal mekânın ayrı çerçevesiyle de temas eder. 17:1'deki yolculuk {ar:مِّنَ ٱلْمَسْجِدِ ٱلْحَرَامِ إِلَى ٱلْمَسْجِدِ ٱلْأَقْصَى, tr:mina al-masjidi al-ḥarāmi ilā al-masjidi al-aqṣā, gloss:Mescid-i Haram'dan Mescid-i Aksa'ya} uzanarak kutsal mekân eksenini kurar; 17:7'de {ar:لِيَدْخُلُوا۟ ٱلْمَسْجِدَ, tr:li-yadkhulū al-masjida, gloss:mescide girmeleri için} denmesi bu eksene mescide girişi ekler (17:1, 17:7). {ar:كَمَا دَخَلُوهُ أَوَّلَ مَرَّةٍ, tr:kamā dakhalūhu awwala marratin, gloss:ona ilk kez girdikleri gibi} ifadesindeki ilk giriş, 17:4'teki {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} sayımıyla temas edip giriş dizisini iki gerçekleşmeden birine bağlar; bu temas olayları tek tek teşhis etmez (17:7). Aynı ayetteki {ar:مَا عَلَوْا۟, tr:mā ʿalaw, gloss:üzerine üstün geldikleri şey} kökü bir nesneyle ilişkilendirir, {ar:تَتْبِيرًا, tr:tatbīran, gloss:bütünüyle yıkım} ise o şeyin dağıtılmasını belirginleştirir (17:7). Bu iki ayrıntı yükselişe görülebilir, maddi ve kurumsal bir iz kazandırır; mescit kutsal mekân çerçevesini sağlar, ama üstün gelinen şeyin kimliği açık kalır ve yalnız mescide indirgenmez.

## Dünyevî Konum ve Derece

Odaktaki {ar:وَلَتَعْلُنَّ عُلُوًّا كَبِيرًا, tr:wa-la-taʿlunna ʿuluwwan kabīran, gloss:büyük bir yükselişle yükseleceksiniz} çevresindeki konum ve dağılım anlatılarıyla başka bir ölçek kazanır. 17:6'da {ar:ثُمَّ رَدَدْنَا لَكُمُ ٱلْكَرَّةَ عَلَيْهِمْ, tr:thumma radadnā lakumu al-karrata ʿalayhim, gloss:üstünlüğü size geri verdik} denmesinin ardından mal ve oğullarla desteklenme ve daha kalabalık kılınma gelir (17:6). Geri verilen konum, maddi destek ve artan sayı yükselişi kaynaklarla güçlenen bir kapasite gibi duyurur; bu bağ, sonraki bozgunculuğu kaynakların sonucu ya da nedeni olarak kurmaz.

17:20'de {ar:نُّمِدُّ هَٰٓؤُلَآءِ وَهَٰٓؤُلَآءِ, tr:numiddu hāʾulāʾi wa-hāʾulāʾi, gloss:iki gruba da veririz} denmesi ve {ar:مِنْ عَطَآءِ رَبِّكَ وَمَا كَانَ عَطَآءُ رَبِّكَ مَحْظُورًا, tr:min ʿaṭāʾi rabbika wa-mā kāna ʿaṭāʾu rabbika maḥẓūrā, gloss:Rabbinin bağışından ve engellenmemiş bağışından} sözü desteğin Rabbinin bağışından geldiğini ve iki gruba da uzandığını gösterir (17:20). Bu geniş dağılım konumun yalnız muhatapların kendi ürettiği bir statü olmadığını duyurur; iki gruba da verilmesi eşit sonuç ya da odaktaki muhataplarla birebir özdeşlik anlamına gelmez. 17:21'de kimilerinin kimilerinin üstünde kılınması ve {ar:أَكْبَرُ دَرَجَٰتٍ وَأَكْبَرُ تَفْضِيلًا, tr:akbaru darajātin wa-akbaru tafḍīlan, gloss:derece ve üstünlük bakımından daha büyük} denmesi karşılaştırmalı bir mertebe ölçeği kurar (17:21). Bu ölçek büyük yükselişi saygınlık ya da kamusal önderlik gibi konumlara da açabilir; odaktaki kınama ise sürer. Böylece dünyevî güç daha geniş bağış ve dereceler içindeki geçici bir mevki olarak duyulur, hak edilmiş bir rütbe ya da 17:21'deki ahiret derecelerinin önceden bildirimi olarak değil; iki öngörüyle dereceler arasında bire bir eşleşme kurulmaz.

## Toplu Hitap, Kişisel Hesap

Kitap'ta topluluğa yöneltilen tarihî uyarı, kişinin kendi hesabıyla birlikte işler. 17:7'de iyilik veya kötülüğün sonucu kişiye döner; 17:13'te her insanın amel kaydı kendisine bağlanıp açılmış olarak karşısına çıkar; 17:14'te kişi kendi kitabını okur; 17:15'te hiçbir yük taşıyan başkasının yükünü üstlenmez (17:7, 17:13, 17:14, 17:15). Bu kişisel sonuç, kayıt, okuma ve devredilemez yük, kolektif hitapla aynı sorumluluk çerçevesinde buluşur. Soyla anılan topluluğun tarihî sorumluluğu ferdin kişisel hesabını yutmaz; soy bağı suçu başka kişiye veya sonraki kuşağa taşımaz.

Bu kişisel kayıtlar, 17:4'teki {ar:فِى ٱلْكِتَٰبِ, tr:fī al-kitābi, gloss:Kitap'ta} öbeğine ayrı bir yakınlıkla döner. 17:12'de yılların sayısı ve hesap anılır, ardından her şeyin ayrıntısıyla açıklandığı söylenir; 17:13'te kişinin kitabı kendisine bağlanıp açılır, 17:14'te okunur (17:12, 17:13, 17:14). Bu sayım, ayrıntı, açılma ve okuma sırası kaydı denetlenebilir kılar. 17:12'deki yıl sayımı, odaktaki {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} ile sayısal yankı kurar; bu yakınlık iki bozulmanın tarihini vermez. Odaktaki Kitap ile kişisel kitaplar yazılı kayıt düzeyinde buluşur, fakat aynı metin ya da nesne sayılmaz.

Bu kayıt yakınlığında {ar:بَنِىٓ, tr:banī, gloss:soyundan gelenler} gerçek soy anlamını korur. Banī ailesinin ayrı kurma kullanımı parçaları birleştirerek bir bütünü, sonuç kullanımıysa ev, duvar, saray ya da gök gibi kurulmuş yapıları anlatır; bu dallar soy adının kendi sözlük anlamı değil, gerçek kurma eylemi ve ürünüdür. Soy topluluğu, yazılı Kitap ve bozulma tehdidi bir araya gelince, nesiller boyunca taşınan ve yazıyla bir arada tutulan bir düzen imgesi kurar; ahitle ilişkisi sınırlı bir benzetme olarak kalır, ayette açık bir ahit formülü kurulmaz. Ettirgen bozulma bu düzenin elverişliliğini tehdit eder. Böylece yapısal imge kolektifin taşıdığı sürekliliği görünür kılar; Banī'nin soy anlamı yerinde kalır.

Aynı unsurlar daha sıkı, fakat ayrı bir bağ imgesi de kurar. Banī ailesinin parçaları bir araya getirerek bütün kurma kullanımı yapıyı sağlar; Kitap ailesinin yazılı kayıttan ayrı olan dikme, bağlama ya da atlarla askerleri düzenli bir birlik hâline getirme kullanımları bu bütünü bir arada tutar. {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} iki gerçekleşmeyi sayarken, aynı sözcük ailesindeki kordon kullanımı ipin kollarını burarak sağlam ip oluşturmayı verir. Böylece yapı kurma bütünü, bağlama onu tutan işlemi, burma ise iki kolu birbirine geçiren hareketi sağlar. Soy, kayıt, sayım ve {ar:وَلَتَعْلُنَّ عُلُوًّا, tr:wa-la-taʿlunna ʿuluwwan, gloss:yükselişle yükseleceksiniz} bir araya geldiğinde iki eylem yalıtılmış noktalar değil, yükseltilmiş bir bütünü taşıyan ve birbirini güçlendiren iki burulmuş tel gibi görünür. Bu benzetme boyunca {ar:بَنِىٓ, tr:banī, gloss:soyundan gelenler} soy topluluğunu, Kitap yazılı kaydı, {ar:مَرَّتَيْنِ, tr:marratayni, gloss:iki kez} iki gerçekleşmeyi, yükseliş de yukarı hareketi taşır. Ailenin üste konmuş parça ya da ek yük anlamı başka bir şeyin üstündeki parçaya bağlıdır; odaktaki fiil {ar:عَلَىٰ, tr:ʿalā, gloss:üzerine} tümleci almadığı için yükseliş gerçek bir yük ya da ip değildir, benzetmenin taşıyıcı biçimidir.

## Hüküm ve Geri Dönüş

Yazılı hükmün bağlayıcılığı ile bozgunculuk öngörüsü, 17:16'daki ayrı kasaba anlatısının uygulama sırasıyla temas eder. Orada {ar:أَمَرْنَا مُتْرَفِيهَا, tr:amarnā mutrafīhā, gloss:varlıklı ve bolluk içindeki sakinlerine buyurduk} sözünü {ar:فَفَسَقُوا۟ فِيهَا, tr:fa-fasaqū fīhā, gloss:orada sınırı aştılar} izler; buyruk karşısındaki taşkınlık norm çizgisinin aşılmasını gösterir (17:16). Ardından {ar:فَحَقَّ عَلَيْهَا ٱلْقَوْلُ, tr:fa-ḥaqqa ʿalayhā al-qawl, gloss:üzerine hüküm kesinleşti} gelir ve {ar:فَدَمَّرْنَٰهَا تَدْمِيرًا, tr:fa-dammarnāhā tadmīran, gloss:onu bütünüyle yıktık} yoğun yıkımla diziyi tamamlar (17:16). Varlıklı sakinlerin konumu dizide yer alır, ancak servet taşkınlığın nedeni yapılmaz. Buyruk, ihlâl, kesinleşen söz ve yıkım sırası odaktaki {ar:قَضَيْنَآ, tr:qaḍaynā, gloss:hükme bağladık} fiilinin bağlayıcı yönünü ve bozgunculuk öngörüsünün sonuçla temasını aydınlatır. Bu paralellik iki anlatıyı aynı tarihî olaya ya da her bozulmanın kaçınılmaz sonucuna eşitlemez.

17:5'te ilk eşik, 17:6'da geri verilen konum ve destek, 17:7'de ise üstün gelinen şeyin yıkımı görünür olur. Özellikle 17:7'deki {ar:مَا عَلَوْا۟, tr:mā ʿalaw, gloss:üzerine üstün geldikleri şey} ile {ar:تَتْبِيرًا, tr:tatbīran, gloss:bütünüyle yıkım} aynı kök çevresinde yükseliş ile onun nesnesinin dağıtılmasını buluşturur (17:7). Bu sıra ve kök yankısı yükselişi kalıcı mertebeden çok izi görülebilen, tersine çevrilebilecek toplumsal güç olarak duyurur; yıkım da bu hareketin olası karşılığına katılır. Bağlantı mümkün bir karşılık düzeyindedir: ayetler tarihî olayları birebir eşleştirmez, neden-sonuç mekanizması ya da yıkılan yerin kimliğini belirlemez. Böylece büyük yükseliş, kınaması korunarak, yeryüzünde görünür ve geri çevrilebilir bir kudret olarak duyulur.

</source_prose>
