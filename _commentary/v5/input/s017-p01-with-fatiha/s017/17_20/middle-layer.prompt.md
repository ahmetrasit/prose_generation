# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:20**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.middle.claims.json`

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
- Refer to source paragraphs as `17:20 ¶N`.

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

`(17:20 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:20",
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
        "citation": "(17:20 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p01-with-fatiha/s017/17_20/17_20.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p01-with-fatiha/s017/17_20/17_20.middle.claims.json \
  --ayah-ref 17:20
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p01-with-fatiha/s017/17_20/17_20.prose.editorial.tr.md`

<source_prose>
## İki Alıcı, Ortak Fiil

17:20'nin düz okumasında Rab, herkese; şu gruba da bu gruba da kendi armağanından destek verir. Öne alınan {ar:كُلًّا, tr:kullā, gloss:hepsine} nesneyle tek {ar:نُّمِدُّ, tr:numiddu, gloss:destek verip sürdürürüz} fiili, hem alıcıların kapsamını hem de ardından gelen kaynak tamlamasını yönetir. İki {ar:هَٰٓؤُلَآءِ, tr:hāʾulāʾi, gloss:şunlar} en yakın bağlamda, peşin olanı isteyenlere (17:18) ve ahireti isteyenlere (17:19) döner; bu yakın gönderim bağlamsal bir okumadır, işaretler daha geniş grupları da kapsayabilir. Ortak fiil iki yönelişe ulaşır; alıcıların son hükmünü veya tek sonucu belirlemez.

Tekil biçimli {ar:كُلًّا, tr:kullā, gloss:hepsine}, gösterilen kümedeki her bireyi kapsama alır; buradaki bütünlük olgunlaşma değil, alıcıların eksiksiz kapsamıdır. Nesnenin fiilden önce gelmesi, eylemi duymadan önce kimin kapsandığını duyurur. Böylece iki işaret kapsamın çevresini belirlerken amaçları, payları ve varışları ayrı kalır.

İşaret zamirlerinin ikisi de insan çoğuluna yönelen aynı {ar:هَٰٓؤُلَآءِ, tr:hāʾulāʾi, gloss:şunlar} biçimindedir. Söylemde hazır olan grubu gösterirler; yakınlık burada fiziksel mesafeyi değil, konuşmadaki erişilebilirliği anlatır. İkinci {ar:وَ, tr:wa, gloss:ve}, ayrı bir grubu ilkine ekler ve ikisine aynı dilbilgisel yeri verir. Uzun işaret biçimlerinin her biri kendi işitsel ağırlığını taşırken kısa bağlaç aralarında hafif bir menteşe kurar. Bu yerel sesleniş iki alıcıyı aynı fiilde eşit görünür kılar; tek bir tilavet temposu dayatmaz.

{ar:نُّمِدُّ, tr:numiddu, gloss:destek verip sürdürürüz} alıcıya dışarıdan yardım, kaynak ya da miktar ekleyerek onu desteklemeyi anlatır. Birinci çoğul şahıs muzari biçimi sunuşu sürmekte olan etkinlik gibi açar; kökün boyuna uzatma ve dışa doğru erişme alanı da tek kaynaktan iki ayrı alıcıya uzanan desteği duyurur. Fiildeki ikiz ünsüz kısa ve sıkı bir ses etkisi katar; bu yerel işitsel izlenim genel bir ses-sembol yasası değildir. Süreklilik kökten tek başına değil, fiil biçimiyle cümledeki kaynak ve alıcıların birlikte kurulmasından doğar; bu ilişki süresiz dünyevî devamı da bildirmez.

## Kaynak ve Hüküm

Kaynağa geçişi {ar:مِنْ, tr:min, gloss:-den} başlatır: edat ardından gelen genitif {ar:عَطَآءِ, tr:ʿaṭāʾi, gloss:armağanından} adına bağlanır ve {ar:مِنْ عَطَآءِ رَبِّكَ, tr:min ʿaṭāʾi rabbika, gloss:Rabbinin armağanından} tamlamasının bütünü {ar:نُّمِدُّ, tr:numiddu, gloss:destek verip sürdürürüz} fiilinin kaynağı olur. Böylece dikkat alıcılardan verişin kökenine döner. Kaynak bildiren {ar:مِنْ, tr:min, gloss:-den}, her grubun armağandan bir pay alabileceği parça gölgesini taşır; bu ipucu toplam kaynağı, pay miktarını veya aktarım takvimini belirlemez. Kısa edatla genitif adın bitişikliği kaynak bağını işitsel olarak da sıkılaştırır; katkısı bu dilbilgisel yakınlıktır.

İki armağan adı aynı verme mastarını taşır, fakat cümlede farklı iş görür: kaynak tamlamasındaki {ar:عَطَآءِ, tr:ʿaṭāʾi, gloss:armağanından} genitif, kapanıştaki {ar:عَطَآءُ, tr:ʿaṭāʾu, gloss:armağanı} ise nominatif özne biçimindedir. Hamza ikisi arasındaki sözlüksel tanışıklığı korurken değişen bitişler, kaynağı adlandıran sözcüğün yeni cümlede hükmün öznesi olmasını duyurur; nominatif -u bu bağı işitmeye yardım eder, çözümlemeyi tek başına kurmaz. Aktarılan {ar:عَطَآءً, tr:ʿaṭāʾan, gloss:armağanı} mansup varyantı farklı görevler kurmaya imkân verir; mevcut nominatif yüzey ile varyantın biçimsel olanağı birlikte açık kalır. {ar:عَطَآءُ, tr:ʿaṭāʾu, gloss:armağanı} verme eylemini de verilen şeyi de adlandırabilen bir mastardır. Nebe 78:36'da aynı ad karşılık ve ölçü diliyle yan yana gelir; bu ayrı kullanım, armağan sözünün ölçülü bir karşılığı da taşıyabildiğini gösterirken odaktaki özne görevini korur (78:36). Aynı sözlük alanındaki bir başka kol bir başkasının işini görmeyi veya bakımını üstlenmeyi anlatır; sürmekte olan destekle karşılaşınca verişi ani bir kazançtan ibaret olmayan pratik yardım gibi duyurur. Ayet bu çağrışımı bir insan çalışanı veya ev içi hizmet olarak adlandırmaz.

Her iki tamlamadaki ikinci şahıs eki {ar:رَبِّكَ, tr:rabbika, gloss:Rabbin} hitabı aynı kaynağa yöneltir; dilbilgisi muhatabın kimliğini belirlemez. İlk {ar:رَبِّكَ, tr:rabbika, gloss:Rabbinin} kaynak armağan adının tamlayanı, ikinci {ar:رَبِّكَ, tr:rabbika, gloss:Rabbinin} ise hükmün öznesi olan armağan adının tamlayanıdır; tekrar iki ayrı görevi aynı hitapta buluşturur. Rab unvanının alışılmış anlamı sahiplik, buyruk yetkisi ve yönetip düzenleme alanını taşır. Bu tamlama armağanı belirli bir Rab kaynağına bağlar; genelleme her türlü verme hakkında değildir. Mülk 67:21'de rızık tutulursa kimin vereceği sorusu bu kaynağın yetkisini somutlaştırır: alıcılar çoğalsa da veriş başka bir bağımsız sağlayıcıya dağılmaz (67:21).

Tek kaynağa bağlı bu veriş, yakın bağlamdaki iki uyarıyla da yankılanır. Musa'ya Kitabın verildiği bölüm, başka bir vekil edinmemeyi söyler; burada bu uyarı Kitap veya hidayet hakkında yeni bir iddiaya taşınmaz (17:2). Daha ileride başka bir ilah ve yardımsız kalma uyarısı rakip dayanağı karşıya koyar; ibadet bağlamı nedeniyle bu temas maddi kaynakların tekliği konusunda bir olasılık olarak kalır (17:22). Tekrarlanan {ar:رَبِّكَ, tr:rabbika, gloss:Rabbin} ile çok alıcıya yönelen tek fiil ortak verişi tek kaynağa bağlar; bu ilişki alıcılar için bağımsız hak, eşit pay veya eşit son derece belirlemez (17:2, 17:22).

Rab unvanının olağan anlamına eşlik eden yetiştirme kolu, gözetileni eksiklikten olgunlaşmaya doğru adım adım taşır. Bu bakım çağrışımı {ar:نُّمِدُّ, tr:numiddu, gloss:destek veririz} fiilinin kaynak ekleyerek sürdürmesiyle birleşince ortak sunuşu gözetilen bir destek süreci gibi işittirir. Buradaki temas bakım anlamını etkinleştirir; gerçek bir yetiştirme olayını veya tamamlanmayı vaat etmez, unvanın olağan anlamının yerini de almaz.

İlk cümlenin etkin sunuşundan sonra gelen {ar:وَ, tr:wa, gloss:ve}, önceki cümleyi sürdürürken yeni hükmü de açar; kapanış başka bir alıcı eklemek yerine armağanın durumuna döner. Alıcı listesinden sonra gelen bu yeni özne-yüklem cümlesi, engellenmeme hükmünü adı geçen armağan hakkında genel bir ilke olarak sunar; kapsamı bütün rızık hakkında bir teoriye dönüşmez. {ar:مَا, tr:mā, gloss:değil} olumsuzluğu {ar:كَانَ, tr:kāna, gloss:bir durumda bulunur} kopulasını kapsar; nominatif {ar:عَطَآءُ رَبِّكَ, tr:ʿaṭāʾu rabbika, gloss:Rabbinin armağanı} özne, edilgen {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} ise yüklemdir. Böylece olumsuzlanan, Rabbinin verme eylemi değil armağana yüklenen kısıtlılık hâlidir. Edilgen yapı kısıtlayıcı bir failin adını vermez; dikkati armağanın durumunda tutar.

Buradaki {ar:كَانَ, tr:kāna, gloss:bir durumda bulunur} olağan kopula olarak bir hâli bağlar. Olumsuzluk, armağanın engellenmemiş oluşunu genel durum olarak öne çıkarır; yargı tek bir geçmiş olaya kapanmaz, gelecekteki her olayı da tek tek saymaz. Varlık ve ortaya çıkma çağrışımı burada armağanın hâlini duyurur; yaratılış ya da varoluş hakkında ayrı bir önerme kurmaz. Edilgen yüklemin tekil eril biçimi tekil armağan öznesiyle uyuşur ve engellenmeme hâlini iki gruba değil armağanın kendisine bağlar. Hüküm bu armağanın durumunu bildirir; bütün maddi iyiliklerin miktarını belirlemez.

İşitmede, etkin sunuşun ardından gelen kısa {ar:وَمَا, tr:wa-mā, gloss:ve değil} açılışı dikkati eylemden armağanın hâline kaydırır. Cümle sonundaki {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} sözcüğün boğumlu ünsüzleri reddedilen engeli kulağa belirgin getirir. Bu yerel kapanış izlenimi 17:19'la tempo kıyası veya ölçülmüş bir akustik özellik değildir (17:19). Başlangıçtaki {ar:كُلًّا, tr:kullā, gloss:hepsine} ile sondaki {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} tenvinleri sesçe bir çerçeve kurar; dilbilgisel görevleri ayrı tutar ve halka düzenini kanıtlamaz.

{ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} bir kişiyle şey arasına set konmasını veya bir eylemin önlenmesini anlatır; izin bağlamında yasaklama anlamı da taşır. Güncel ambargo benzetmesi, mevcut armağanın önünün kesilmesini göz önüne getirir; ayet bu bağlantıda sınırlamanın hangi kurum ya da kuraldan geldiğini belirtmez. Aynı sözlük alanındaki {ar:حَظِيرَة, tr:ḥaẓīra, gloss:çitle çevrili yer} canlıları ya da eşyayı içeride tutan çiti ve çevrili alanı gösterir. Olumsuzlanan kısıtla buluşan bu çit imgesi armağanı insan denetimindeki bir çevrenin dışında konumlandırır; gerçek bir ağıl değil, engellenmeme hâlini görünür kılan benzetmedir.

İnsanî tutma bu görüntüye ayrı bir karşılık verir: İsrâ 17:100'de rahmet hazinelerini elinde tutan insan sahneye gelir (17:100). Aynı ayetin insanı {ar:وَكَانَ ٱلْإِنسَٰنُ قَتُورًا, tr:wa-kāna al-insānu qatūran, gloss:insan eli sıkıdır} diye nitelemesi, malını tutup vermediği için ondan hayrın az görüldüğü ayrı sözlük kullanımıyla bağlamsal bir karşıtlık kurar (17:100). Buradaki bağ kök ortaklığına değil tutma ile verme karşıtlığına dayanır; edilgen {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} hâlâ armağanı niteler, vereni değil. İnsanî tutmanın karşısına Mülk 67:21'deki “rızkını tutarsa size kim rızık verebilir?” sorusu geldiğinde, armağanın açıklığı verene bağlı bir ilişki olarak duyulur (67:21).

İnsan eliyle esirgeme imgesi, 17:100'deki {ar:لَأَمْسَكْتُمْ, tr:la-amsaktum, gloss:kesinlikle tutardınız} sözü çevresinde anılan başka bir sözlük kolunu da çağırır: yumuşaklık, boyun eğme ve direnmeden uyma; özellikle yönlendireni izleyen devenin itaatkâr hareketi (17:100). Bu temas, tutmaya karşı duran {ar:عَطَآءُ, tr:ʿaṭāʾu, gloss:armağan} verişine dirençsizce ilerleyen bir aktarım niteliği katar. Odaktaki mastar verme eylemini veya verilen şeyi adlandırır; deve imgesi bu aktarımın tınısını değiştirir, ayete deve davranışı ya da ilahî psikoloji eklemez.

Engellenmemiş verişteki devam yankısı, başka bir armağanın niteliğiyle de duyulabilir. Hûd 11:108'de cennetliklere ait armağan {ar:عَطَآءً غَيْرَ مَجْذُوذٍۢ, tr:ʿaṭāʾan ghayra majdhūdh, gloss:kesintiye uğramayan armağan} diye anılır (11:108). Aynı mastarın mansup biçimi ve ayrı cümle göreviyle gelen bu armağan, kesilmeme niteliğini farklı alıcılara bağlar; bu nitelik {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} sözcüğünün kendisi değildir. Bu karşılaşma 17:20'deki verişe devam edebilme yankısı ekler; odaktaki engelin hukuki, maddi veya geleceğe dönük anlamlarından birini kesinleştirmez (11:108).

## Akışın Başlangıcı ve Havza

Kaynağı ve alıcıları belli olan {ar:نُّمِدُّ, tr:numiddu, gloss:destek veririz} fiilinin su kolu, akan, dolan ve başka suyla beslenerek yükselen nehir, kuyu ya da denizi anlatır: {ar:ماء يجري ويمتلئ ويمده ماء آخر, tr:māʾun yajri wa-yamtaliʾu wa-yamidduhu māʾun ākhar, gloss:akan ve başka suyla beslenen kaynak}. Bu özel kullanım genel bir dökme değil, başka kaynaktan yenilenen akıştır. Lokmân 31:27'de ardından yedi denizle beslenen deniz imgesi bu yenilenmeyi somutlaştırır; ayetin devamındaki tükenmeyen ilahî sözler yankıyı süreklilik yönünde genişletir (31:27). Oradaki fiilin çekimi odaktakinden ayrıdır; bu bağlantı odaktaki desteğe kaynaktan alıcıya beslenme imgesi ekler (31:27).

Bu su koluyla buluşan 17:1'deki {ar:أَسْرَىٰ, tr:asrā, gloss:gece yolculuğuna çıkardı}, olağan anlamıyla gece yolculuğunu anlatırken aynı sözlük ailesindeki küçük dere ve toprağa yayılan kök kullanımları rotaya ilk akış yönünü verir (17:1). Böylece odaktaki {ar:نُّمِدُّ, tr:numiddu, gloss:destek verip sürdürürüz} için açılan su yolu bir güzergâha kavuşur. Ardından 17:2'de Musa'ya Kitap verilişini anlatan {ar:آتَيْنَا, tr:ātaynā, gloss:verdik}, aynı ailenin su kanalını açıp akışı yönlendirme kolunu çağırır; kanal, yolculuğun açtığı yöne akışın yönlendirilmesini ekler (17:1, 17:2). Kitap verilişi bu görüntüye maddi olmayan, uzak bir armağan örneği sağlar; su yolu onun olayını veya düz anlamını değiştirmez (17:2).

Rotanın çevresindeki 17:1'in {ar:بَارَكْنَا, tr:bāraknā, gloss:bereket verdik} fiili olağan anlamıyla bereketi bildirir; aynı ailenin havuz, sarnıç veya çukurda durgunlaşan su kullanımı, bereketli çevreyi akışın toplanacağı bir varış alanı gibi kurar (17:1). {ar:حَوْلَهُۥ, tr:ḥawlahu, gloss:çevresinde} sözü o çevreyi belirtirken, ailenin su çeken çark kullanımı oraya dolaşım işlevi ekler (17:1). Odaktaki akışın yanına 17:6'daki dönüş hareketi geldiğinde, bu çark alıcı çevreden suyu çekip dolaştıran düzenek gibi belirir (17:1, 17:6). Böylece bereketli çevre havza, çark ise dönüşle birikeni yeniden dolaşıma veren işlev kazanır; iki imge akışa varış ve dolaşım katar.

Bu alıcı çevresine 17:5 ve 17:7'deki {ar:جَاءَ وَعْدُ, tr:jāʾa waʿdu, gloss:vaat geldi} ifadesi varış hareketi ekler. Ayetlerde vaatlerin gelişi anlatılır; aynı ailenin alçak yerde veya sur çevresinde su toplanan oyuk anlamı, gelişi akışın ulaşacağı bir hazneyle buluşturur (17:5, 17:7). Böylece tarihsel vaat kendi düz anlamını korurken su imgesi bir varış noktası kazanır (17:5, 17:7). 17:7'nin iyilik ve kötülüğün kişiye dönüşünü anması da bu karşılaşmanın sınırını çizer: ortak sunuş, sonraki sonucu tek başına belirlemez (17:7).

17:6'daki {ar:الْكَرَّةَ, tr:al-karrata, gloss:geri dönüş} önceki dönüşü anlatırken, aynı ailenin kuyuya veya vadiye toplanmış sığ su anlamı dönüşü havzada yeniden toplanma hareketine bağlar (17:6). Aynı ayette servet, oğullar ve artan destekçilerden söz edilmesi ise farklı bir destek kolu açar (17:6). {ar:أَمْدَدْنَٰكُم, tr:amdadnākum, gloss:size destek verdik} odaktaki fiille aynı kök ailesindendir; asker, yardımcı, yiyecek veya mal ekleme anlamları alıcıların eylem kapasitesini genişleten takviyeyi somutlaştırır (17:6). Bu maddi artış kapasiteyi genişletir; tek başına başarı ya da ayrıcalık hükmü vermez (17:6).

17:12'deki {ar:ٱلنَّهَارِ, tr:an-nahāri, gloss:gündüz} geceyle birlikte zaman göstergesi olarak sunulur; aynı ailenin toprağı yararak akan nehir anlamı, odaktaki su akışına bir yatak ve yön katar (17:12). Gündüz ayette zaman anlamını korurken bu ayrı nehir imgesiyle hareketli akışa bağlanır (17:12). Aynı ayetin {ar:فَضْلًا مِن رَبِّكُمْ, tr:faḍlan min rabbikum, gloss:Rabbinizden lütuf} arayışını ve hesabı bilmeyi gece-gündüz düzenine koyması, lütuf ile hesabı ortak gündelik çerçevede buluşturur; bu bağ akış için bir saat veya takvim belirlemez (17:12).

İlk olarak, 17:1'deki gece yolculuğu akışa bir güzergâh, 17:2'deki Kitap verilişinin kanal anlamı ise bu güzergâha yön kazandırır (17:1, 17:2). 17:1'in bereketli çevresi havza imgesini kurar; çevre anlamındaki sözcüğün çark kolu, 17:6'daki dönüşle buluştuğunda birikeni alıp yeniden dolaşıma sokar (17:1, 17:6). Böylece yol ve alıcı yer, akışın yönü ile dönüşünü birbirine bağlar; Kitap verilişi bu bağlantıda maddi olmayan örnek olarak kalır (17:2).

17:5 ve 17:7'de vaadin gelişi akışı alçak bir hazneye vardırırken, 17:6'daki geri dönüş ayrı bir hareketle sığ suyu bu havzada yeniden toplar (17:5, 17:6, 17:7). Çarkın dolaşım hareketi toplananı yeniden yola çıkarırken, 17:12'deki nehir imgesi yatağı uzatır ve gündüz-gece bağlamı lütufla hesabı aynı gündelik düzende tutar (17:1, 17:6, 17:12). 31:27'deki başka denizlerle beslenme, bu güzergâha dışarıdan yenilenme katkısı verir (31:27). Servet, oğullar ve destekçilerle genişleyen eylem kapasitesi ise akışın fiziksel devamı değil, aynı alıcılara yönelen desteğin ayrı bir sonucudur (17:6). Bu bağlantıların kurduğu imge, iki alıcıya ulaşan ve yeniden beslenen bir akıştır; ayetlerdeki tarihsel sahneler tek bir gerçek coğrafya oluşturmaz (17:1, 17:2, 17:5, 17:6, 17:7, 17:12).

Kaynağın üstünde, {ar:رَبِّكَ, tr:rabbika, gloss:Rabbin} unvanının olağan anlamına eşlik eden ayrı bir sözlük kolu katmanlı veya aşağıda asılı bulutu adlandırır. {ar:نُّمِدُّ, tr:numiddu, gloss:destek veririz} fiilinin yenilenen suyu ile bu bulut sözüne eşlik eden bitkiyi besleyici yağmur açıklaması, üstteki kaynağı aşağıdaki alıcılara ulaşan besleyici bir akışla ilişkilendirir. Bulut kullanımı unvanın olağan anlamına eşlik eder; yağmur açıklaması bu imgeye besleyicilik katar, 17:20'deki bir hava olayını bildirmez. Ardından {ar:حَظِيرَة, tr:ḥaẓīra, gloss:çitle çevrili yer} kolundaki çit, {ar:مَا, tr:mā, gloss:değil} ile reddedilen engel hâlinin karşısına çıkar: akış, çevrili bir alanda tutulmayan kaynak gibi duyulur. Bu üstten beslenme okuması 17:20'nin kaynağını besleyici bir imgeyle genişletir; gerçek bir su düzeneği ileri sürmez veya dünyevî rızkın sınırsız ya da eşit olduğunu söylemez.

## Ayrı Yönelişler ve Dereceler

17:20'nin tek {ar:نُّمِدُّ, tr:numiddu, gloss:destek veririz} fiili iki alıcı yönelişine de ulaşır. En yakın okumada ilk gösterim 17:18'de peşin olanı isteyenlere döner; orada dünya payı dilediği kimseler için seçilerek hızlandırılır (17:18). İkinci gösterim 17:19'da ahireti isteyenlere döner; onların gayreti ve çabalarının takdir edilmesi ayrı bir yol açar (17:19). Böylece ortak veriş farklı istek ve değerlendirmelerden geçer; ilk grubun payı ile ikincinin çabası aynı kullanım veya varışa dönüşmez. Bu yakın gönderim bağlamsal bir okumadır; işaretler daha geniş sınıfları da kapsayabilir.

Aynı destek kökü farklı bir yola da uzanabilir: A'râf 7:202'de başka bir çekim sapma içindeki desteği ve bunun sürmesini anlatır (7:202). Bu temas, desteğin erişim bildirdiğini, tek başına ahlaki onay vermediğini gösterir (7:202). Ra'd 13:26'da rızkın genişleyip daralması, miktarın değişebildiği başka bir anlam paraleli sunar; biçimi odaktaki fiilden ayrı kalır (13:26).

17:21'de bazılarının bazısına göre üstün kılınması, ortak kapsam içindeki farkı açıkça sahneye getirir; {ar:بَعْضَهُمْ عَلَىٰ بَعْضٍ, tr:baʿḍahum ʿalā baʿḍ, gloss:bazılarını bazısına göre} ifadesindeki “bazı” sözü bölme ve parça-bütün ilişkisini de çağırır (17:21). {ar:كُلًّا, tr:kullā, gloss:hepsine} ile açılan kapsam herkesin erişimini tutarken payların ayrı kalmasına izin verir. {ar:دَرَجَٰتٍ, tr:darajāt, gloss:dereceler} mertebeleri adlandırır; aşama aşama ilerleme kolu farklı sonuçları bir sıra içinde duyurur, dereceyi ise veriş fiili üretmez. 17:21 ahirette daha büyük derecelerden de söz eder; ilk karşılaştırmanın dünya dağılımını mı sonraki değerlendirmeyi mi anlattığı açık kalır (17:21). 17:18'in seçici payı ile 17:21'in dereceleri, bu bağlantıda açıklığın eşit bölüşüm veya her davranışa izin olmadığını gösterir (17:18, 17:21).

Armağan ve lütuf dili bu farklılaşmayı silmeden yan yana gelir. {ar:عَطَآءُ, tr:ʿaṭāʾu, gloss:armağan} verme eylemini ve verilen şeyi taşırken, 17:12'deki {ar:فَضْلًا, tr:faḍlan, gloss:lütuf} Rabbin lütfunu arama bağlamına yerleştirir; iki sözcüğün yakınlığı kök özdeşliğinden değil, bağış ve lütuf bağlamından doğar (17:12). 17:21'deki {ar:فَضَّلْنَا, tr:faḍḍalnā, gloss:üstün kıldık} üstünlük ve derece farkını dile getirir; böylece lütuf diliyle derece dili yan yana gelirken odaktaki armağan adı ayrı kalır (17:21). Aynı ayetteki {ar:انظُرْ, tr:unẓur, gloss:bak} çağrısını izleyen karşılaştırma, sözlük ailesindeki {ar:نَظِير, tr:naẓīr, gloss:denk ya da karşılık} anlamını hatırlatır: iki grup karşılaştırılabilir taraflardır, sonuçları eşit ilan edilmez (17:21).

Bu ayrım başka geçim ve derece anlatımlarında da belirginleşir. Zuhruf 43:32 dünya geçimliklerinin paylaştırılmasını ve bazılarının derece derece yükseltilmesini yan yana getirir; Ra'd 13:26 rızkın genişleyip daralmasını, En'âm 6:132 amellere göre dereceleri anar (43:32, 13:26, 6:132). Bu anlam paralelleri ortak desteği değişen miktar ve değerlendirmelerle birlikte okumaya yardım eder; kendi ayetlerinin biçimleri odaktaki fiilden ayrıdır ve 17:21'deki ilk derecelerin zamanını ya da alıcı başına miktarı belirlemez (17:21, 43:32, 13:26, 6:132).

Odaktaki bütünlük kişisel ayrıntıları da içinde taşır. 17:12'de her şey ayrıntılandırılır, 17:13'te her insan kendi kaydına bağlanır (17:12, 17:13). Böylece toplam kapsam ayrıntıdan bireysel hesap verebilirliğe ilerler; ortak veriş kişileri tek kitleye eritmez (17:12, 17:13). Kayıt sorumluluğu kişiselleştirir; ayetler onu armağan miktarını belirleyen bir cetvele bağlamaz (17:13).

Erişim, arzu ve kullanım ayrı düzlemlerde kalır. 17:11 insanın kötülüğü de iyiliği ister gibi istemesini acelecilikle yan yana getirir; böylece isteğin konusu onun ahlaki niteliğini belirlemez (17:11). 17:16'da varlıklı ileri gelenlerin ardından taşkınlıklarının gelmesi, erişim ile sonraki kullanımı ayırır (17:16). Bu sıralama verişi taşkınlığın nedeni veya her davranış için izin saymaz (17:11, 17:16).

Bu son sahnede su akışından ayrı bir sınır imgesi belirir. {ar:مَحْظُورًا, tr:maḥẓūran, gloss:engellenmiş} ile aynı sözlük ailesindeki {ar:حَظِيرَة, tr:ḥaẓīra, gloss:çitle çevrili yer} içeride tutan çiti düşündürür; 17:16'da varlıklı ileri gelenlerin ardından gelen {ar:فَفَسَقُوا, tr:fa-fasaqū, gloss:taşkınlık ettiler} sözü bu sınıra başka bir yönden temas eder (17:16). Aynı fiil ailesindeki olgun meyvenin kabuğundan çıkma kullanımı, çit imgesine dışarı taşma hareketini katar; taşkınlık böylece kişinin kendi sınırını aşması gibi görünür (17:16). Bu, fiilin etimolojisi değil, çit ve kabuk imgelerinin bu ayetle kurduğu sınırlı bağlantıdır; su-kaynağı okumasından bağımsız olarak bolluk içindeki kişinin sınırı aşan hareketini belirginleştirir (17:16).

</source_prose>
