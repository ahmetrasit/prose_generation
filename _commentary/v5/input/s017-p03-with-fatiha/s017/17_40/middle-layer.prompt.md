# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:40**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.middle.claims.json`

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
- Refer to source paragraphs as `17:40 ¶N`.

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

`(17:40 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:40",
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
        "citation": "(17:40 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_40/17_40.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_40/17_40.middle.claims.json \
  --ayah-ref 17:40
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_40/17_40.prose.editorial.tr.md`

<source_prose>
## Soru ve Dağılım

Âyet isnadı önce soru içine yerleştirir: {ar:أَفَ, tr:a-fa, gloss:soru ve bağlama} ile soruyu açan hemze, hemen ardından gelen {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} fiilinin hemzesiyle sesçe karşılaşır. A-fa-asfa dizisinin kısa dur-kalkı kulağa işitilir bir kesinti verir; yeni bir sözlük anlamı kurmadan soruyu tarafsız bilgi istemekten inkâr bekleyen bir meydan okumaya çeker. Ses hareketi isnadın somut içeriğini de açık tutar: muhataplara oğulların ayrılması ve meleklerden dişilerin edinilmesi.

İkinci isnadı ekleyen {ar:وَ, tr:wa, gloss:ve} aynı sorunun kapsamına alır; ayrı bir beyan gibi görünse de sorgunun dışında kalmaz. Ardından {ar:إِنَّكُمْ, tr:innakum, gloss:şüphesiz siz} yeni bir cümle açıp konuşanlara döner: önce seçme ve edinme iddiaları sorulur, sonra bu iddiaları dile getirenlerin sözü değerlendirilir. Bu sıra ayetin kendi sözdiziminde tamamlanır; önceki bir ayet ya da sûre tarafından kurulmuş bir çerçeve gerektirmez.

Sorudaki ilk paylaştırmada {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} içindeki -kum, tercih fiilinin alıcılarını, yani hitap edilenleri gösterir; {ar:بِ, tr:bi, gloss:bi edatı} ile bağlanan {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar} ise seçilen içeriği bildirir, doğrudan nesne olmaz. Böylece fiilin kime yöneldiğiyle neyin seçildiği ayrılır ve cümlenin kurduğu paylaşım görünür olur; bu biçimsel ayrım tek başına daha geniş bir toplumsal tahsis kuralı kurmaz. Oğulların belirli, eril çoğul biçimi tanınan bir sınıfı öne çıkarırken {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} belirsiz ve mansub bir kategori olarak karşı kutupta durur. Oğullar edatla seçme fiiline bağlanır; dişiler ise meleklere yüklenen sonuç kategorisidir. Bu yerel biçim asimetrisi polemik paraleli olmadan da seçilir; toplumsal üstünlük kuralı ise bu biçimlerden tek başına çıkarılamaz.

Seçme fiilinin olağan anlam alanında seçenekler arasından en iyi görüneni ayırmak, bir sınıfa ayrıcalıklı pay tanımak da bulunur. {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} oğulları muhataplara yöneltirken karşılarındaki {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} kategorisi seçmeyi kayırılmış bir pay gibi duyurur. Bu ayrıcalık yankısı temel seçme anlamına eşlik eder: fiil burada oğulları seçer; arıtma anlamı taşımaz ve payın fiilen tahsis edildiğini tek başına bildirmez. {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar} yalnızca bir cinsiyet sınıfını değil, ebeveynlerle gerçek çocukluk ve soy bağını da adlandırır. Oğulları muhataplara yöneltmek böylece genel bir ödülden çok soy çizgisinin sürmesine ayrılmış bir pay izlenimi verir. Bu aile okuması çocukların insani nesep anlamını kullanır; Rabbe gerçek ebeveynlik isnadı kurmaz.

Ardından gelen {ar:رَبُّكُم, tr:rabbukum, gloss:Rabbiniz} hitabındaki iyelik, sorgulanan faili muhatapların kendi Rabbiyle ilişkilendirir. Fiilden sonra gelen ad, ilk seçme fiilinin gecikmiş öznesidir; {ar:وَ, tr:wa, gloss:ve} ile başlayan {ar:ٱتَّخَذَ, tr:ittakhadha, gloss:edindi} fiilinde de aynı özne sürer. Sözdizimi iki isnadı aynı iddia edilen faile bağlar; konuşanların ileri sürdüğü ilişkiyi kurar, eylemlerin gerçekten gerçekleştiğini bildirmez. Rab adı burada konuşanların kendi Rabbi diye andığı varlığı öne çıkarır; bu özne zinciri ayetin içinde tamamlanır, önceki sûreyle ilişki kurmaz.

İkinci isnatta {ar:ٱتَّخَذَ, tr:ittakhadha, gloss:edindi} fiilinin VIII. kalıbı ilişkiyi rastlantısal bir tasvirden ziyade edinme ya da bir kategori olarak benimseme biçiminde kurar. {ar:مِنَ, tr:mina, gloss:-den} melekleri kaynakta tutar; {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} ise yüklenen sonuç kategorisidir. Belirli çoğul {ar:ٱلْمَلَٰٓئِكَةِ, tr:al-malaikati, gloss:melekler} bilinen bir kaynak sınıfı olarak kalır, dişi etiketi onlardan ayrı durur; melekler doğrudan nesneye çevrilmez. Bu kaynak-sonuç dizilimi sorudaki isnadın nasıl kurulduğunu gösterir: söz edinmeyi soru içindeki bir atıf olarak aktarır, doğrulanmış fiziksel bir olay bildirmez.

{ar:ٱلْمَلَٰٓئِكَةِ, tr:al-malaikati, gloss:melekler} adı ilahî haber ya da buyruk taşıyan haberci varlıkları da düşündürebilir. Ayrı bir {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} etiketi bu haberci sınıfını sorgulanan isnat içinde cinsiyetli bir hane konumuna iter. Dişileri adlandıran sözcüğün kökündeki yumuşaklık ve etkide zayıflık yankısı, beklenen sertlik ve güçle kurulan karşıtlığı keskinleştirir; erkek oğullar ve meleklerin ayrı kaynak sınıfı bu etkiyi cinsiyetli sınıflandırmaya bağlar. Bu kök yankısı söz konusu isnadın içindeki yerleşime katkı verir; dişi varlıkların geneli ya da meleklerin gerçek mahiyeti hakkında nitelik bildirmez.

Bu cinsiyetli paylaştırmanın iki karşılaştırması ayrı katkılar sunar. En'âm 6:139, hayvanların karınlarındakini erkeklere ayırıp eşlere yasaklayanların ölü doğum halinde hepsini ortak saymasını aktarır; böylece cinsiyete göre değişen somut bir pay düzeni gösterir. Zuhruf 43:19 ise melekleri dişi diye niteleyenlerin yaratılışa tanık olup olmadığını sorar ve bu sözün kaydedilip sorgulanacağını bildirir. Odaktaki {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} etiketi ilk sahneyle dağıtım, ikincisiyle tanıklık ve sorumluluk sorusuna açılır (6:139, 43:19). Bu temaslar konunun pay ve isnat yönlerini aydınlatır; aynı konuşanları ya da aynı uygulamayı belirlemez.

Zuhruf 43:16'da Allah'a kızlar, kendilerine oğullar yakıştırılması cinsiyetli pay iddiasını toplumsal tepkiyle buluşturur; 43:17'de haber karşısında yüz kararır ve öfke bastırılır; 43:18'de süs içinde yetişme ve tartışmada kendini açıkça ortaya koyamama bu polemik tasvirine eklenir (43:16, 43:17, 43:18). Ayrıntılar sınıflandırmanın taşıdığı gerilimi ve tartışma biçimini somutlaştırır. Bu, ayetin polemik içindeki tasviridir, kadınlara ilişkin olgusal bir genelleme değildir; odaktaki konuşanları ya da aynı uygulamayı da teşhis etmez.

Seçimin ayrıcalık yankısı, {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} ile kurulan payın insanın kendi değer sırasını ilahî düzene taşıması gibi duyulmasına imkân verir. Nahl 16:62'de konuşanlar hoşlanmadıkları payı Allah'a yakıştırıp iyiyi kendilerine mal eder; Şûrâ 42:49'da kız ve erkek çocukları vermek, 42:50'de ikisini birlikte vermek ya da kimseyi çocuk sahibi kılmamak Allah'ın dilemesine bağlanır (16:62, 42:49, 42:50). Bu karşılaştırma odaktaki {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar} ve {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} paylarını, kişinin kendine uygun gördüğü düzeni Rabbin iradesine yüklemesi olarak da duyurur. Kibir bu bağlamın açtığı bir yankıdır; {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} sözcüğünün kendisi kibir anlamına gelmez. Bu okuma etkisi konuşanların özel niyetini ya da başka ayetlerdeki kişilerin aynı topluluk olduğunu belirlemez.

## Soy, Pay ve Egemenlik

İki isnat birlikte asimetrik bir hane düzeni kurar. {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} oğulları muhataplara yönelterek seçimin ayrıcalığını gösterir; {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar}ın gerçek evlat ve soy anlamı bu payı çizginin sürmesine bağlar. Aynı {ar:رَبُّكُم, tr:rabbukum, gloss:Rabbiniz} failin meleklerden {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} edinme isnadı ise karşı kategoriyi ona yöneltir; Rab adının sahiplik, buyruk ve yönetim alanları bu faili dağıtım otoritesi gibi duyurur. Böylece ayrıcalıklı soy payı ve karşı kutup, konuşanların kendilerine tanıdığı üstünlüğü gösteren tek bir aile tasarımında birleşir. Bu tasarım isnadın nasıl kurulduğunu açıklar, doğrulanmış ilahî eylem ya da meleklerde biyolojik cinsiyet bildirmez.

{ar:ٱتَّخَذَ, tr:ittakhadha, gloss:edindi} ailesindeki “kendisi için edinme” kullanımı belirli türemiş biçim ve kalıplarla sınırlıdır; fiilin her kullanımı kendiliğinden bu anlamı taşımaz. Zümer 39:4'te çocuk edinme yalnız varsayımsal koşulda anılır; ardından Allah'ın yaratılmışlardan dilediğini seçmesi, biricik ve galip oluşu öne çıkar (39:4). Bu sıra odaktaki isnatla karşılaştırıldığında, insanın Allah adına soy belirleme iddiasını koşullu çocuk edinme ve ilahî seçme karşısında görünür kılar. Bağlantı bu söylem yapısı düzeyinde kalır: odak bir çocuk edinme olayı bildirmez, tarihsel konuşanları ya da töreni belirlemez ve kadınlarla erkekler hakkında evrensel kural kurmaz.

Rab adının yönetim yönü, Furkân 25:2'de göklerin ve yerin mülkünün Allah'a verilmesi, O'na çocuk ya da mülkte ortak tanınmamasıyla belirginleşir (25:2). Bu ayet Zümer 39:4'teki koşullu çocuk edinme anlatısıyla yan yana geldiğinde, odaktaki {ar:رَبُّكُم, tr:rabbukum, gloss:Rabbiniz}, {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar} ve {ar:ٱتَّخَذَ, tr:ittakhadha, gloss:edindi} dizisi soy isnadını egemenliğe ortaklık iması gibi duyurabilir (39:4, 25:2). Bu bağlantı soy isnadının siyasal tınısını açıklar; sahneyi gerçek bir ortak-iktidar olayı olarak sunmaz.

Pay imgesine geçişte seçme fiilinden ayrı bir biçim ve kullanım devreye girer. Aynı kökün bir isim kalıbı, bölüşüm başlamadan önce elde edilen mallardan hükümdara ayrılan özel payı anlatır; odaktaki {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} fiili o payın adı değil, seçme fiilidir. Bu ayrı isim kalıbı dağıtım başlamadan önce ayrılmış bir hisse örneği sağlar. Odaktaki iki isnat da kendi yönleriyle bir pay defteri benzetmesine açılır: {ar:ٱلْبَنِينَ, tr:al-banina, gloss:oğullar} muhataplara seçilir, {ar:ٱتَّخَذَ, tr:ittakhadha, gloss:edindi} ile karşı kategori aynı {ar:رَبُّكُم, tr:rabbukum, gloss:Rabbiniz} adına yöneltilir. Rab adının sahiplik, buyruk ve yönetim alanları böylece dağıtıcı konumunu kuvvetlendirir. Pay defteri dağılımı açıklayan bir benzetmedir, Rabliğin mülk ya da ganimet tanımı değildir; fiilin metninde “kendisi için” denmez, kendine ayırma ilişkisi payların yönünden çıkarılır.

En'âm 6:136'daki ekin ve hayvan payları bu benzetmeye ayrı, daha zayıf bir akış örneği ekler. Allah'a ve ortaklara ayrılan paylardan ortaklara düşen Allah'a ulaşmazken Allah'a ayrılan pay ortaklara aktarılabilir; yön tek taraflıdır (6:136). Bu karşılaştırma pay imgesine asimetrik aktarım ayrıntısını katar, ancak odaktaki {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} fiilinin anlamı ya da tarihsel karşılığı değildir.

Pay defterindeki dağıtım sorusu 17:42'de başka bir ölçeğe, siyasal egemenliğe geçer. Ayetin koşulunda çoğul taraflar {ar:لَٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:arayışa girerlerdi} fiiliyle tahta doğru bir yol ararlardı; {ar:ذِى ٱلْعَرْشِ, tr:dhi l-arshi, gloss:Arş'ın sahibi} ise yönelinen egemenlik merkezini verir (17:42). Bu arayış hareketi, odakta kaynak olarak anılan {ar:ٱلْمَلَٰٓئِكَةِ, tr:al-malaikati, gloss:melekler} sınıfının da tahta erişmeye çalışan taraflar arasında düşünülebilmesini sağlar. 17:43'te Allah'ın onların söylediklerinden yüce tutulması, arayıştaki taraflarla O'nun arasındaki dikey ayrımı kurar ve bu egemenlik bağlantısına sınır çizer (17:43). Bu, melekleri arayıcı taraflar arasında düşünebilen olası okumadır; 17:42 çoğul tanrı iddiasını reddeden koşullu bir ifade olarak da okunabilir. Taht burada imgesel egemenlik merkezidir; pasaj tarihsel bir sarayı ya da aynı tarihsel grubu belirlemez.

Taht ve tenzih çizgisinin yanındaki 17:54, {ar:رَبُّكُم, tr:rabbukum, gloss:Rabbiniz} adını bilgi ve rahmetle birlikte anarak Rab oluşunun niteliğini açar; 17:55 ise Allah'ın bilgisi içindeki gerçek peygamberî farklılığı, {ar:فَضَّلْنَا بَعْضَ ٱلنَّبِيِّينَ عَلَىٰ بَعْضٍ, tr:faddalna ba'da n-nabiyyina ala ba'd, gloss:peygamberlerin kimini kimine üstün kıldık} sözüyle bildirir (17:54, 17:55). Bu gerçek ilahî tercih, odaktaki {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} çevresindeki seçme yankısını insanın kendi lehine kurduğu paylaştırmadan ayırır. 17:42'deki taht ve arayış egemenlik ve yönetim alanını, 17:43'teki tenzih ise Allah ile arayıştaki taraflar arasındaki mutlak ayrımı belirginleştirir (17:42, 17:43). Bu bağlamsal alanlar melek adının sözlük anlamı değil, odak isnadın temas ettiği egemenlik çerçevesidir.

Çağrılanların tutumu bu egemenlik karşılaştırmasına bağımlılık yönünü ekler. 17:56'da çağrılan varlıklar zararı kaldıramaz ya da değiştiremez; 17:57'de kendileri Rablerine yakınlık arar, rahmet umar ve azaptan korkarlar (17:56, 17:57). Bu davranışlar, odaktaki {ar:ٱلْمَلَٰٓئِكَةِ, tr:al-malaikati, gloss:melekler} ile ilişkilendirildikleri ölçüde onları bağımsız egemenler değil Rablerine yönelen muhtaç varlıklar olarak düşündürür. Bağlantı bir özdeşlik değil, olası bir paraleldir: 17:55 başka bir soruya, 17:56 ve 17:57 başka çağrılanlara değiniyor olabilir; bu ayetler aynı tarihsel topluluğu ya da tek bir sorunun yanıtını belirlemez.

İlahî seçimin çocuk kategorilerinden ayrı bir yönü Hac 22:75'te görünür: Allah meleklerden ve insanlardan elçiler seçer, böylece melek adı soyun yanı sıra haber ve görev alanına da açılır (22:75). Nahl 16:74 Allah'ın bilgisini insan bilgisinden ayırır ve O'na benzetmeler kurmama uyarısını getirir (16:74). Bu iki bağlam seçimi insanın kendi paylaştırmasından ilahî irade ve bilgiye taşır. Elçi görevi evlat isnadından ayrı bir ilişkidir; karşılaştırma melekleri çocuk saymaz. Odaktaki isnat böylece gerçek peygamberî farklılık ve aracıların sınırlı gücü kabul edilirken kendi retorik yerini korur.

## Sözün Ağırlığı

İki isnat tamamlandıktan sonra {ar:إِنَّكُمْ, tr:innakum, gloss:şüphesiz siz} konuşanlara döner; inna vurgusu ve ekli ikinci çoğul hitap hükmü az önceki iddiayı dile getirenlere yöneltir. Yüklemdeki {ar:لَ, tr:la, gloss:pekiştirme lamı} doğrudan {ar:تَقُولُونَ, tr:taquluna, gloss:söylüyorsunuz} fiilini pekiştirir. İkinci çoğul şimdiki zaman biçimi söyleyişi süren, kamusal bir eylem olarak çerçeveler; belirli bir tekrarlı alıntı ya da konuşanların iç inancı hakkında tek başına kanıt sunmaz. Fiille aynı kökten gelen mansub {ar:قَوْلًا, tr:qawlan, gloss:söz}, söyleme eylemini değerlendirilebilir bir ad haline getirir. Belirsiz biçimi belirli bir alıntı yerine söz türü açar; içeriğini önceki seçme ve edinme isnatları sağlar.

Bu sözün dayanağı {ar:قَوْلًا, tr:qawlan, gloss:söz}, niteleyeni ise {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} sıfatıdır; sıfat doğrudan söylenen sözü niteler. Büyüklük ve güç alanı isnadın içeriğiyle karşılaşınca ahlaki ciddiyete yönelir: burada ölçülen fiziksel boyut ya da ses şiddeti değil, sözün ağırlığıdır. Yaratılmış çocuklarla melekleri Rabbe nispet eden içerik, bu ağırlığı ilahî fail ile yaratılmışlar arasındaki ilişkinin erişimine taşır; vurgulu söyleyiş de sözü kısa bir öğreti gibi duyurabilir, ancak hükmün konusu yine bu isnattır. {ar:إِنَٰثًا, tr:inathan, gloss:dişiler} biçiminden {ar:قَوْلًا, tr:qawlan, gloss:söz} ve {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} biçimlerine uzanan mansub -an akışı, cinsiyetli sınıflandırmadan sözün değerlendirilmesine geçişte yerel bir ses-sözdizimi bağı kurar; bu bağlantı daha geniş bir örüntü iddiası değildir. Âyetin son sözcüğü olan sıfat, kapanışı ağır sözün yargısında tutar.

Söyleme fiilinin olağan kamusal anlamı sürerken, 17:42'de başkalarının sözünün aktarılması ve 17:43'te Allah'ın bu isnattan yüce tutulması {ar:قَوْلًا, tr:qawlan, gloss:söz} için yanlış isnat yönünü belirginleştirir (17:42, 17:43). Bu bağlam, odaktaki söylenmiş sözün temelsiz atıf olarak da duyulmasını sağlar; olağan konuşma anlamının yerini almaz. En'âm 6:100'de çocuk ve ortakların bilgisizce Allah'a yakıştırılması bu yanlış isnada bilgisizlik ve uydurma boyutunu ekler (6:100). Kehf 18:4'te çocuk isnadında bulunanlar uyarılır; 18:5'te ne onların ne atalarının bu konuda bilgisi olduğu ve ağızlarından çıkanın büyük bir yalan olduğu bildirilir (18:4, 18:5). Bu ayetler isnadın bilgi temeli ve ağırlığını aydınlatır; odaktaki konuşanların tarihsel kimliğini ya da özel zihinsel durumunu belirlemez.

Fiille aynı kökten gelen {ar:قَوْلًا, tr:qawlan, gloss:söz} olağan söyleyiş anlamını taşır; ayrı bir isim kalıbındaki kullanım ise benimsenen görüş ya da inancı anlatabilir. Zuhruf 43:21'de melekleri dişi sayan iddia için önceki bir kitapta dayanak aranır; 43:22'de ataların izinden gitmek gerekçe gösterilir (43:21, 43:22). Bu sıra önce kanıt sorununu, ardından geleneğin iddiaya temel yapılmasını gösterir; böylece ayrı isim kalıbı miras alınmış görüş yankısı ekler. Bu katman daha önceki pay defterini bir dünya görüşüne bağlar, odaktaki olağan konuşma anlamını dönüştürmez. Karşılaştırma içsel kanaati ya da resmî bir inancı kanıtlamaz.

17:44'te her şey Allah'ı hamdiyle anar, dinleyenler ise yaratılmışların tesbihini kavrayamaz (17:44). Bu anlaşılmayan övgünün yanına konan {ar:تَقُولُونَ قَوْلًا, tr:taquluna qawlan, gloss:söz söylüyorsunuz} isnadı, odağı yanlış önermenin doğruluğundan insan sözünün kavranamayan övgü ve işaretler yanındaki yerine doğru genişletir. Yan yanalık, iddia ile övgü arasında bir alımlama boşluğu sezdirir; bu boşluğun özellikle aile isnadına neden olduğunu göstermez.

17:41'de hatırlatma için çeşitlendirilen Kur'an anlatımı kaçışı artırır; 17:46'da kalpler örtülür, kulaklara ağırlık verilir ve Rab tek başına anıldığında dinleyenler arkalarını döner (17:41, 17:46). İlk sahne hatırlatmaya karşı artan kaçışı, ikincisi içsel ve işitsel engellerle belirginleşen yüz çevirmeyi ekler. Birlikte odaktaki söyleyişi işaretleri almada güçlük yaşanan bir bağlama yerleştirir; bu aile isnadının o güçlüğe neden olduğu gösterilmez, yan yanalık yorumu açık kalır.

Kamusal sözün ilişkilerdeki işlevi 17:53'te belirginleşir. Odaktaki {ar:تَقُولُونَ قَوْلًا, tr:taquluna qawlan, gloss:söz söylüyorsunuz} iddiasının yanına en güzel olanı söyleme buyruğu gelir; hemen ardından şeytanın insanlar arasına fitne soktuğu belirtilir (17:53). Buyruk sözün niteliğini, ardından gelen uyarı ise insanlar arasındaki ayrılığı biçimlendirme gücünü öne çıkarır. Bu temas, 17:40'taki soy dağılımının sözle yeniden kurulabilecek bir toplumsal sıralama olduğunu düşündürür. Bağlantı olası bir etkidir: 17:53 genel konuşma ilkesi olarak kalabilir, odak cümleyi doğrudan hedeflediği ya da ayrışmayı kesin olarak doğurduğu gösterilmez.

## Direnç ve Karşılık

Odaktaki {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} sıfatı, yeniden yaratılış tartışmasındaki {ar:عِظَامًا, tr:izaman, gloss:kemikler} ile aynı kökün sesini paylaşır (17:49). {ar:عِظَامًا, tr:izaman, gloss:kemikler} iskeletin ve eklemlerin sert, dayanıklı parçalarını adlandırır; bu somut yapı ağır söz çevresinde iskelet yankısı kurar. Odaktaki {ar:قَوْلًا, tr:qawlan, gloss:söz} değerlendirilen söyleyişi adlandırırken, 17:49'daki kemiklere ilişkin yeniden diriliş itirazı bu ayrı malzeme imgesini sözlü tartışmanın içine yerleştirir (17:49). Bağlantı ses ve imge düzeyindedir: kemik sözcüğü sıfatın çevirisi değil, onun çevresindeki yapısal çağrışımdır.

Bu maddi imge 17:50 ve 17:51'de ayrı katkılarla genişler: taş ve demir dirençli dış malzemeyi, göğüslerde büyüyen şey ise içeride gelişen unsuru sağlar (17:50, 17:51). Kemikler bedensel iskeleti kurar; taş ve demir dayanıklılık sunar; göğüste büyüyen şey bu çizgiyi içe taşır. Bunlar tek bir maddeye dönüşmez, odak iddiaya ayrı ayrı bağlanır. {ar:قَوْلًا, tr:qawlan, gloss:söz} olağan anlamıyla söylenmiş sözü taşırken, ayrı kalıptaki benimsenmiş görüş yankısı iddia içeriğinin bu direnç imgeleriyle duyulmasını sağlar (43:21, 43:22). Birlikte, sözün yanında sertleşmiş kanaat katmanı açılır; bu benzetme özel bir iç inancı kanıtlamaz.

Ayrı bir taşıma kolunda bir şeyi kaldıracak gücü bulmak, taşımak ya da yük olarak üstlenmek anlatılır. Bu kol söylenmiş sözün olağan anlamından farklı olarak yük taşıma işlemini getirir; {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} ağırlığı, kemikler iskeleti, taş ve demir direnci, göğüste büyüyen şey ise imgenin içsel yerini sağlar (17:49, 17:50, 17:51). Bu işlemler birleşince, sözün iddia içeriğini insanların taşıdığı, direncin iskeletini kuran bir inanç benzetmesi doğar: kolayca dağılan bir söz yerine yüklenilen ve direnç gösteren bir düşünce gövdesi belirir. Taşıma kolu kök bakımından uzak ve keşifseldir; sözlük çevirisi olarak kullanılmaz, yakın seslerden doğan kelime oyunu da mümkün kalır. Bu sınırlama yalnızca yük taşıma kolunun bağlantısına ilişkindir; kemik, taş-demir ve göğüs imgelerinin kurduğu diğer yankıları geçersiz kılmaz.

Bu direnç imgesi 17:59 ve 17:60'taki uyarı ve karşılık akışıyla temas eder. 17:59'da inkâr edilen işaretler ile korkutmak amacıyla gönderilen uyarı yan yana gelir; 17:60'ta sınama ve uyarının ardından {ar:يَزِيدُهُمْ, tr:yaziduhum, gloss:onları artırır} fiili açık bir artış bildirir ve {ar:طُغْيَانًا كَبِيرًا, tr:tughyanan kabiran, gloss:büyük bir taşkınlık} sonuç olarak gelir (17:59, 17:60). Sınama baskı altındaki tutumu açığa çıkarabilir; ardından gelen artış uyarıya karşı direncin yoğunlaşabileceği bir süreci görünür kılar, fakat her dinleyicinin aynı tepkiyi verdiği söylenmez. Bu akış, {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} sözün düzeltmeye direnç büyüyebilecek bir eşikte duyulmasına imkân verir. Bağlantı süreç benzerliğidir: odak söz 17:59'daki işaret değildir, sonraki taşkınlık da aynı söz değildir; ayetler tek ve zorunlu bir nedensel döngü kurmaz.

Meryem'de aynı tür çocuk isnadı daha büyük bir sonuç ölçeğine taşınır: 19:88'de isnat dile getirilir, 19:89'da muazzam bir söz diye nitelenir; 19:90'da göklerin neredeyse yarılması, yerin çatlaması ve dağların düşmesi bu sözün kozmik karşılığını sahneye getirir (19:88, 19:89, 19:90). Böylece gök, yer ve dağ imgeleri 17:40'taki {ar:عَظِيمًا, tr:aziman, gloss:büyük ve ağır} için olağan büyüklük ve ağırlık anlamından analojik bir sonuç ölçüsü çıkarır. Bu karşılaştırma ağırlık yankısını genişletir; kozmik imgeler odak ayette gerçekleşen bir olay ya da sıfatın sözlük karşılığı değildir.

## Yönelinen Yol

Fâtiha'daki dış dua odaktaki aile isnadının karşısına farklı bir söz eylemi koyar. 17:40'taki {ar:تَقُولُونَ قَوْلًا, tr:taquluna qawlan, gloss:söz söylüyorsunuz} başkaları hakkında seslendirilen kamusal bir iddiadır; Fâtiha 1:5'teki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyaka na'budu wa-iyyaka nasta'in, gloss:yalnız Sana kulluk, yalnız Senden yardım} ise birinci çoğul ağızdan doğrudan Allah'a yönelen kulluk ve yardım talebidir (1:5). Bu karşılaştırma isnat ile dua arasındaki yöneliş farkını görünür kılar; Fâtiha burada tarihsel bir cevap ya da alıntı olarak kullanılmaz.

Odaktaki {ar:أَصْفَىٰكُمْ, tr:asfakum, gloss:size ayırdı} seçme fiili bir payın kime ayrıldığını kurarken, Fâtiha 1:6'daki {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdina as-sirata al-mustaqim, gloss:bizi dosdoğru yola ilet} dosdoğru yola kılavuzluk ister; 1:7'deki {ar:صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ, tr:sirata alladhina an'amta alayhim, gloss:nimet verdiklerinin yolu} bu yolu nimete erdirilmiş kişilere bağlar (1:6, 1:7). Böylece ayrıcalıklı seçim yankısının yanında, izlenmesi istenen bir lütuf yolu belirir. 1:5'in kulluk ve yardım talebiyle 1:6'nın hidayet isteği ayrı yönelişlerdir; 1:7 ise yolun kimlere bağlandığını bildirir.

Odak bağlamındaki gerçek peygamberî farklılık (17:55), çağrılanların zararı bağımsız biçimde gideremeyişi (17:56) ve Rablerine muhtaç yönelişi (17:57), dua ile sınırlı aracı gücü arasındaki ilişkiyi açık tutar: dua peygamberî farklılığı silmez, aracılara bağımsız egemenlik vermez. Odaktaki seçme isnadı yerinde kalırken, Fâtiha bu pay karşılaştırmasının yanına lütufla verilecek doğru yolu isteyen bir yakarış koyar.

</source_prose>
