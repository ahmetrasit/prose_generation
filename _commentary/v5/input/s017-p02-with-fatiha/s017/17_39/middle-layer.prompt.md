# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:39**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.middle.claims.json`

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
- Refer to source paragraphs as `17:39 ¶N`.

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

`(17:39 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:39",
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
        "citation": "(17:39 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_39/17_39.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_39/17_39.middle.claims.json \
  --ayah-ref 17:39
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_39/17_39.prose.editorial.tr.md`

<source_prose>
## Vahyedilen sözden buyruğa

17:39, Rabbinin muhatabına vahyettiği hikmetten söz eder; ardından Allah'la birlikte başka bir ilah edinmeyi yasaklar ve bu yasağın sonucunu Cehennem'e atılmak, kınanmak ve kovulmak olarak bildirir. Ayetin akışı, önceki uyarıları bir gösterme sözüyle toplar, bildirimin kime yöneldiğini açıklar, sonra yasağı ve akıbeti birbirine bağlar.

Başlangıçtaki {ar:ذَٰلِكَ, tr:dhālika, gloss:bu}, isim cümlesinin öznesi olarak önceki sözleri özetleyen bir işaret kurar. Geri dönüşün sınırı açıktır: dhālika hangi sözlerin tamamını topladığını tayin etmez, önceki ayetin yargısını da ayrıca devralmaz. {ar:مِمَّا أَوْحَى, tr:mimmā awḥā, gloss:vahyettiği şeylerden} içindeki mā, vahyedilen içeriği bildirme eylemine bağlar. İlk mimmā'daki min, içeriği daha geniş vahyedilmiş bütünden gelen ya da o bütünden bir pay olan bir aktarım şeklinde duyurabilir. Ardından gelen {ar:مِنَ الْحِكْمَةِ, tr:min al-ḥikma, gloss:hikmetten veya hikmet kapsamında} ise buyrukları hikmet kategorisine yerleştirebilir ya da hikmetten bir bölüm sayabilir. Böylece ilk min vahyedilen içerikle daha geniş bütün arasındaki kaynak/pay ilişkisini, ikincisi içerikle hikmet arasındaki kategori/pay ilişkisini açar; iki bağ ayrı ayrı açık kalır ve biri ötekini çözmek zorunda değildir.

{ar:أَوْحَىٰ, tr:awḥā, gloss:vahyetti}, tamamlanmış bildirme eylemini kuran mâzi IV. bâb biçimidir; {ar:إِلَيْكَ, tr:ilayka, gloss:sana} ise yöneldiği muhatabı gösterir. İkinci tekil kişiyi taşıyan bu yönelme, özeti doğrudan hitaba çevirir. Cümle önce alıcıyla eylemi duyurur, ardından {ar:رَبُّكَ, tr:rabbuka, gloss:Rabbin}i kaynak olarak getirir; bu gecikme zamansal değil, söz dizimindedir. Böylece eylem, muhatap, kaynak ve hikmet nitelemesi tek bir yerel çerçevede birleşir; daha geniş bir vahiy tarihi anlatılmaz. Awḥā'nın olağan vahyetme ve bildirme anlamına, aynı kelime ailesindeki sözü ya da bilgiyi gizlilik içinde ulaştırma kullanımı da bir aktarım nüansı ekler: Rabb kaynak, ilayka alıcı olduğunda bildirim hedefli ve muhataba özel duyulur. Bu, ayette vasıta belirtilmeyen ve herkesten saklandığı ileri sürülmeyen bir gizli-iletişim yankısıdır; olağan vahiy anlamının yanında kalır.

{ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin}, ikinci kişi ekiyle unvanı {ar:إِلَيْكَ, tr:ilayka, gloss:sana} ile gösterilen muhataba kişisel olarak bağlar; bu hitap, {ar:لَا تَجْعَلْ, tr:lā tajʿal, gloss:edinme} yasağına yönetici otorite boyutu verir. Kelime ailesindeki adım adım yetiştirip geliştirme ve büyüyeni tamamlama kullanımı ise hikmet adı ve yasağın somut içeriğine bakım ve gelişim imgesi katar. Bu, davranışın oluşumuna katılan mecazi bir rehberliktir: unvanın yönetici otoritesini korur, insanî ya da maddî sahiplik ve tamamlanmış biyolojik büyüme iddiası taşımaz.

{ar:الْحِكْمَةِ, tr:al-ḥikma, gloss:hikmet}, {ar:مِنَ الْحِكْمَةِ, tr:min al-ḥikma, gloss:hikmetten veya hikmet kapsamında} ifadesinde min sonrasında belirli ve mecrur biçimde gelir; böylece buyruklar tanınabilir bir hikmet kategorisine yerleşir, kategorinin bütün içeriği değil. Olağan bilgelik anlamı başka ilah edinmeme yasağında somutlaşır. Kelime ailesindeki alıkoyma ve yöneldiği şeyden geri çevirme kullanımı da yasağa pratik bir sınır imgesi ekler. Bu çağrışım hikmet adını somut bir nesneye ya da alıkoyma eyleminin adına dönüştürmez. Aradaki {ar:وَ, tr:wa, gloss:ve}, önceki bildirimi yasağa bağlayabilir ya da yeni bir uyarı başlatabilir; her iki okumada da akış vahyedilen içerikten somut buyruğa ilerler.

{ar:لَا تَجْعَلْ, tr:lā tajʿal, gloss:edinme}, olumsuzluk edatının muzari fiili cezmli biçime sokmasıyla doğrudan yasak olur. {ar:تَجْعَلْ, tr:tajʿal, gloss:yapmak veya yerleştirmek} olağan anlamıyla yapmayı ya da yerleştirmeyi bildirir; bağlı olduğu kelime ailesindeki, var olan bir katılımcının durumunu veya konumunu değiştirme kullanımı da burada açılır. Hem {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah}ın doğrudan nesne oluşu hem {ar:مَعَ اللَّهِ, tr:maʿa Allāh, gloss:Allah ile birlikte} ilişkisi bu statü okumasını destekler. Böylece yasak, Allah yanında bir rakibe ilahlık statüsü vermeye yönelir; odağı put imalatı değil, statü atamasıdır.

{ar:مَعَ اللَّهِ, tr:maʿa Allāh, gloss:Allah ile birlikte} olağan eşlik ilişkisini taşır. Maʿa'nın önce gelişi, kulağa önce bu bağı, ardından {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah} nesnesini getirir. Allah, eşlik yapısının sabit gönderimli özel adı ve mecrur tamamlayıcısıdır; ilāhan ise tajʿal'ın doğrudan nesnesi olan belirsiz cins isimdir. Böylece özel adın sabit gönderimiyle, ilahlık statüsü verilebilecek genel sınıf karşı karşıya gelir. Belirsiz cins isim belirli bir put ya da kişiden daha geniş bir ilahlık kategorisi kurar; kapsamı yine bu statüyle sınırlıdır, her tür otoriteye açılmaz. Maʿa'nın katkısı fiziksel yan yana duruştan çok birlikte ilahlık ilişkisidir; Allah adı burada yemin ya da sesleniş değil, bu ilişkinin tamamlayıcısıdır. Tilavette maʿa'nın son sesi Allah adına bağlanırken, tajʿal'ın kısa ve sıkışık ünsüzlerinden maʿa'nın açık seslerine geçiş eylemden ilişkiye yönelen bir artikülasyon izlenimi verir. Bu ses katkısı okuma izlenimi olarak kalır; yeni bir sözlük anlamı ya da dilbilgisi kuralı kurmaz.

Allah özel adı ile ilāh genel adı aynı kelime ailesiyle bağlantılıdır; özel ad burada sabit gönderimini korurken ilāh, tapınılan varlığı ve ibadetin yöneldiği nesneyi çağrıştırır. {ar:تَجْعَلْ, tr:tajʿal, gloss:yerleştirmek} fiilinin statü ataması maʿa Allāh'ın ortak ilişki kuran yapısıyla birleşince, yasak başka bir varlığa tapınma yönelimi verme ihtimalini de kapsar. Bu okuma yasağın ilişki ve statü boyutunu aydınlatır; ayet gerçekleşmiş bir tapınma eylemini anlatmaz.

{ar:آخَرَ, tr:ākhara, gloss:başka}, mansub eril biçimiyle {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah}ı niteler; ötekilik böylece Allah adına ya da bütün cümleye değil, yasaklanan rakip üyeye bağlanır. Nesne öbeği önce {ar:مَعَ اللَّهِ, tr:maʿa Allāh, gloss:Allah ile birlikte} ilişkisini, ardından bu başka ilahı getirerek {ar:فَ, tr:fa, gloss:öyleyse / sonuç olarak} öncesinde tamamlanır. Ākhara'nın olağan “başka, öteki” anlamı bir rakip üyeyi işaretler; bu bağlamda gecikme ya da ahiret anlamı taşımaz. İlāhan'ın sonundaki -an, daha sonraki {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş} sonlarını işitsel olarak önceler; bu tilavet yankısı dilbilgisel bağ değildir. Birlikte okunduğunda hikmetin alıkoyucu yönü eylemi sınırlar, tajʿal statü atar, ilāh tapınılacak statüyü belirtir, maʿa da rakibin Allah'la ilişkisindeki yerini kurar. Bu katkılar, yasağın rakip bir tapınma mercii ve ilişkisi kurmaya yöneldiğini gösterir.

Bu yerel akış, Rabden muhataba yöneltilen bildirimi somut bir buyruğa bağlar: hikmet içeriği tanınır bir kategoriye yerleştirir, {ar:لَا تَجْعَلْ, tr:lā tajʿal, gloss:edinme} ise davranışa ve tapınma yönüne sınır koyar. Rabb unvanının yetiştirici yankısı rehberlik boyutunu ekler; bu bileşim sürecin tamamlandığını ya da kelime ailelerindeki her anlamın aynı anda etkinleştiğini ileri sürmez.

## Atılma ve iki hâl

{ar:فَتُلْقَىٰ, tr:fa-tulqā, gloss:öylece atılırsın}, yasağı yerel bir sonuç ilişkisiyle izler; zamanlamanın tamamını ya da yargının bütün açıklamasını belirlemez. Buyruktaki eylemci muhatap, IV. bâb edilgen fiilde atılmanın etkilenen kişisine dönüşür; tulqā atanı belirtmez. Olağan atılma anlamı ve {ar:فِي جَهَنَّمَ, tr:fī Jahannama, gloss:Cehennem'e / Cehennem'de} varış yapısı, kelime ailesindeki atma, bırakma ya da yöneltme nüansıyla birleşerek kişiyi adı konmuş hedefe kuvvetle savrulan biri gibi gösterir. Bu cümlede atma/atılma kolu belirleyicidir; aynı ailenin karşılaşma ya da alma kullanımları ikinci bir kabul olayı olarak işitilmez.

{ar:تُلْقَىٰ, tr:tulqā, gloss:atılırsın} fiilinin uzayan son ünlüsü, eylemi ardından gelen hedefe dek askıda tutan bir tilavet temposu kurar. {ar:فِي جَهَنَّمَ, tr:fī Jahannama, gloss:Cehennem'e / Cehennem'de} ise hem varışa doğru hareketi hem varılan yerin içinde kalma ve kuşatılma boyutunu taşır. Sonuç, {ar:جَهَنَّمَ, tr:Jahannam, gloss:Cehennem} adı verilen cezalandırma yerine yönelir. {ar:فَ, tr:fa, gloss:sonuç bağlacı} ile {ar:فِي, tr:fī, gloss:-e / -de} arasındaki kısa f sesinin tekrarı, sonuç ve varış bağlarını tilavette birbirine yaklaştırır; bu ses katkısı söz dizimini değiştirmez. Jahannam'la ilgili yabancı biçim ya da derinlik kökenleri tartışmalı arka plan açıklamalarıdır; bu bağlam belirli bir etimoloji ya da topoğrafik tasvir kurmaz.

Varış yerinin ardından {ar:مَلُومًا مَدْحُورًا, tr:malūman madḥūran, gloss:kınanmış ve kovulmuş} gelir: iki mansub hâl sözü aynı kişiyi, atılmanın etkilenenini, eşzamanlı olarak niteler. Bunlar yeni varış yerleri değil, Cehennem'e atılmaya eşlik eden durumlardır. Malūman mekânsal sona ahlaki kınanma ekler; bu, kişinin içten pişman olduğunu ya da kınamanın haklılığını tek başına bildirmez. Madḥūran ise kelime ailesindeki yakından etkin biçimde uzaklaştırma imgesini taşıyarak zorla kovulma ve dışlanma hâlini belirginleştirir. Böylece varış yeri, kınanma ve uzaklaştırılma aynı kişinin ayrı durumları olarak birleşir.

Ses dizisi de cezalandırma hareketini bir kapanışa taşır: {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah} sonundaki -an, {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş} sonlarını önceden duyurur. Malūman'ın tenvini tilavette madḥūran'ın başındaki sese benzeşip bağlanır; sondaki kafiye kınanma ile kovulmayı çift hâlinde işittirir. Bunlar tilavetin ses katkılarıdır, sözcükler arasında dilbilgisel bağ kurmaz; madḥūran'ın başındaki ikiz duyumu da kökte ikiz ünsüz bulunduğunu göstermez. Son sözün madḥūran olması kapanışın ağırlığını zorla uzaklaştırılmaya verir.

Sıra, yasağın başındaki {ar:تَجْعَلْ, tr:tajʿal, gloss:yerleştirirsin} eylemcisini sonundaki etkilenene dönüştürür: muhatap önce statü atayan kişi, sonra {ar:تُلْقَىٰ, tr:tulqā, gloss:atılırsın} ile atılan, {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ile kınanan ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş} ile uzaklaştırılan kişidir. Atılma imgesiyle değer yitimi ve dışlanma birleşince terk edilmiş, değeri düşmüş bir nesneye benzeyen ikincil bir görüntü oluşur; bu, sonuçtan doğan mecazdır ve tulqā'nın kişiyi değil atılma eylemini bildirmesini değiştirmez. Kınanma bu görüntüye eşlik eder, ancak tek başına kınamanın hak edilmişliğine hükmetmez.

## Uyarının çevresindeki buyruklar

17:23'te {ar:وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوا إِلَّا إِيَّاهُ, tr:wa-qaḍā rabbuka allā taʿbudū illā iyyāhu, gloss:Rabbin yalnız O'na kulluk etmenizi hükme bağladı} denmesi (17:23), odaktaki {ar:وَلَا تَجْعَلْ مَعَ اللَّهِ إِلَٰهًا آخَرَ, tr:wa-lā tajʿal maʿa Allāhi ilāhan ākhara, gloss:Allah'la birlikte başka bir ilah edinme} yasağına açılış karşılığı verir. İlk ayetteki kesin hükümle son ayetteki yasak, aradaki etik buyrukları tek Rabbe bağlılığın yaşanan biçimleri olarak çerçeveleyebilir. Odaktaki {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah}ın eylem karşılığı yalnız O'na yöneltilen kulluk fiilidir (17:23); bu iki uç, eylemle yöneldiği nesneyi açıp kapatır. Doğru teraziyle tartma (17:35) ve davranışların kötü, istenmeyen sayılması (17:38) da etik çerçeveye bağlanır. Bu, aradaki her görevi ritüel kulluğun eş anlamlısı yapan bir özdeşlik değil, bağlılığın davranışlarda görünmesine dair bir çerçevedir; açılış ve kapanışın tekrarı ayrıca vurgulu bir sınır da çizebilir.

Bu sınırın hemen öncesinde ebeveynlere merhametle tevazu gösterme ve insanın küçükken yetiştirilmiş olduğunu hatırlama çağrısı vardır (17:24). {ar:رَبَّيَانِي صَغِيرًا, tr:rabbayānī ṣaghīran, gloss:beni küçükken büyüttüler} sözü, odaktaki {ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin} unvanına adım adım besleyip geliştirme imgesi katar. Bağlantı kök ortaklığı değil, yetiştirme sahnesiyle kurulan benzetmedir. Aynı ayetteki {ar:وَاخْفِضْ لَهُمَا جَنَاحَ الذُّلِّ مِنَ الرَّحْمَةِ, tr:wa-khfiḍ lahumā janāḥa al-dhulli mina al-raḥmah, gloss:merhametle onlara tevazu kanadını indir} çağrısı da (17:24) bu bakım zeminini görünür kılar: indirilen tevazu kanadı, merhameti bedensel bir imgeye taşır; hikmetin alıkoyup geri çevirme yönüyle yan yana geldiğinde sınır koymayı düzeltici ve şefkatli bir davranış olarak düşündürür.

Geri dönüş çizgisi de bu yasağın yanında belirir. {ar:لِلْأَوَّابِينَ, tr:li-l-awwābīna, gloss:sık sık dönenler için} sözü dönüşü, {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayıcı} ise dönenlerin kusurunun örtülmesini adlandırır (17:25). Hikmetin alıkoyup geri çevirme yönü bu iki imgeyle buluşunca düzeltici sınır, dönüş ve onarıma yer açan bir düzen gibi duyulur. Böylece merhamet ve bağışlanma, Cehennem'e atılma uyarısının yanında gerçek bir dönüş imkânı sunar; güvence ise her yasaklı davranış için genellenmez. Bu komşu sahneler bağımsız buyruklar olarak da okunabilir; bu durumda da odaktaki yasak ve akıbet değişmez.

Son yasağın çevresindeki maddi buyruklar, verme ve tutma ölçüsünü görünür kılar. Yakınlara, yoksula ve yolda kalmışa vermek emredilirken savurganlık yasaklanır (17:26). Sonraki ayet, eli boyna bağlı kılma ile onu büsbütün açmayı iki uç olarak gösterir (17:29). {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:wa-lā tajʿal yadaka maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlı kılma} içindeki tajʿal, odaktaki {ar:تَجْعَلْ, tr:tajʿal, gloss:edinme} gibi bir durumu kurar; burada kurulan elin hâli, odakta yasaklanan ilahlık statüsünden ayrı bir nesne ve amaçtır. {ar:وَلَا تَبْسُطْهَا كُلَّ الْبَسْطِ, tr:wa-lā tabsuṭhā kulla al-basti, gloss:elini büsbütün açıp saçma} ölçüsüz genişletmeyi gösterir (17:29), Rabbin dilediğine rızkı genişletip kısması da dağıtımın ilahî sınırını ekler (17:30). Bu sahneler, başka ilaha statü vermeyi değer ve bağlılığın nihai tahsisi gibi duyurabilir; benzerlik serveti ibadetle özdeşleştirmez ve ayrı bir kader öğretisi kurmaz.

Aşırı el açmanın ardından gelen {ar:مَلُومًا مَحْسُورًا, tr:malūman maḥsūran, gloss:ayıplanmış ve gücü tükenmiş} sonucu kınanmayı tükenişle birleştirir (17:29). Odaktaki {ar:مَلُومًا, tr:malūman, gloss:kınanmış} sözcüğün tekrarı bu iki yasak-sonuç dizisi arasında yankı kurar; aynı sözcük, ayrı eylem ve akıbetleri birbirine eşitlemez (17:29). Maḥsūran'ın güçten düşme imgesinin yanına odak ayet Cehennem'e atılmayı ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş} ile yakınlıktan zorla uzaklaştırılmayı ekler. Böylece odaktaki sonuç, yer ve fail olma imkânı bakımından daha ağır bir kayıp gibi okunabilir; bu karşılaştırma iki yerde aynı yaptırımın uygulandığını ileri sürmez.

Malūman'ın olağan kınanmışlık anlamı temel kalırken, uzak ve keşif niteliğindeki bir sözlük yankısı ek bir düzen imgesi sunar. Belirli kalıplardaki kullanım dağılmış parçaları toplayıp düzensizliği giderme yönüne yaklaşır; savurganlık bu dağılmanın tersini tetikler (17:26), kınanma ve tükenme çifti ise sonuçların fail çevresinde toplanması ihtimaline bağlamsal dayanak verir (17:29). Aynı uzak eşlemenin sıkıntılı bir olayın kişinin başına gelmesi anlamı, odaktaki atılma ve kovulma sonuna kuşatılmışlık gölgesi katar. Bunlar ikinci bir türetim ya da fiziksel toplama süreci değil, bağlamla etkinleşen yankılardır; olağan kınanmışlık anlamı sürer ve bu yankı tek başına cezayı adlandırmaz.

Başka bir bağlamda, haksız yere öldürülen kişinin velisine hakkının peşinden gitmesi için {ar:سُلْطَانًا, tr:sulṭānan, gloss:yetki} verilir ve hemen ardından velinin öldürmede aşırıya kaçmaması istenir (17:33). Odaktaki {ar:تَجْعَلْ, tr:tajʿal, gloss:edinme} ile buradaki {ar:جَعَلْنَا, tr:jaʿalnā, gloss:verdik} aynı statü kurma yönünü, farklı kişiler ve amaçlar üzerinden paylaşır (17:33): birinde insan {ar:إِلَٰهًا, tr:ilāhan, gloss:bir ilah} statüsü atamaktan men edilir, ötekinde veliye hakka uygun, belirli işlevli ve sınırlı bir yetki tanınır. Bu yetki devri, ilahın tapınma statüsünden ayrıdır. Hikmet ailesindeki karar yetkisini devretme kullanımı ada bir renk katabilir; hikmet odakta isim, yetkiyi fiilen veren eylem ise bu başka bağlamdadır (17:33). Bağlantı sınırlı bir benzetmedir, genel siyaset kuralı değildir; yasağı yalnız ritüel ibadetle ilişkilendiren okuma da geçerliliğini korur.

## Ölçü ve hesap

Bir sonraki üç buyruk, alınan yönlendirmenin davranışta aldığı ayrı biçimleri gösterir: ahdi yerine getirme ve ahdin hesabını verme sorumluluğu (17:34), doğru teraziyle kurulan ölçü (17:35), bilgin olmayan şeyin ardına düşmeme eşiği (17:36). Hikmet ailesindeki sağlam ve kusursuz düzenleme imgesi, ilk iki buyruğu güvenilir uygulama olarak birleştirir; hikmetin doğruyu bilgi ve akılla ayırt etme yönü de ölçü ile bilgi eşiğini buluşturur. Vahiy bildiriminin bu sorumluluklarla yan yana gelişi, rehberliğin uygulanmasını düşündürür; bilgi şartı vahyi sıradan insan kanıtına indirgemez.

Aynı hesap, işitme, görme ve gönül yetilerinin sorgulanmasına kadar uzanır: {ar:السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ, tr:al-samʿa wa-l-baṣara wa-l-fuʾāda, gloss:işitme, görme ve gönül} de hesaba katılır (17:36). Ahdin sorumluluğu, ölçü, bilgi eşiği ve bu yetilerin hesabı böylece vahyedilmiş hikmeti uygulanabilir bir etik ölçü olarak görünür kılar. Bunlar tek bir karar sürecinin aşamaları olabileceği gibi yan yana duran ayrı buyruklar da olabilir; bilgi eşiğinin kapsamı belirli bir takip eylemidir, kapsamlı bir bilgi kuramı ya da teolojik ispat kuralı değil.

Yükselme ve erişme imgesi hesap hattını dikey bir sınırla keser. Ölçüyü aşan bir coşkuyla yürüyen kişi yeri delemez, dağların yüksekliğine de erişemez (17:37): {ar:لَن تَخْرِقَ الْأَرْضَ, tr:lan takhriqa al-arḍa, gloss:yeri asla delemezsin} ve {ar:وَلَن تَبْلُغَ الْجِبَالَ طُولًا, tr:wa-lan tablugh al-jibāla ṭūlan, gloss:dağların yüksekliğine erişemezsin}. Yer ile dağlar, aşağıya nüfuz etme ve yukarıya erişme sınırlarını birlikte çizer. Marahan yürüyüşe kendini yükseltmeye dönük taşkınlık gölgesi verir; dağ yüksekliği de üstün bir mevki arayışı çağrışımına izin verir. Bunlar bağlamsal statü okumalarıdır; belirli bir güdü ya da gerçekten yeri delmeye kalkışma sahnesi anlatılmaz.

Davranışların kötü diye toplanıp Rabbin katında istenmeyen sayılması, odaktaki hikmet özeti ve ceza uyarısını az önce değerlendirilen eylemlere bağlar (17:38). {ar:ذَٰلِكَ, tr:dhālika, gloss:bu} gösterme sözünün odakta yinelenmesi, bu değerlendirmeyi hikmet başlığına taşır (17:38); hikmetin alıkoyup geri çevirme yönü de istenmeyen davranışla buluşur. Ardından gelen Cehennem'e atılma ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş}, dağ yüksekliğine erişememenin karşısında zorla belirlenmiş bir yere yönelme ve yakınlıktan dışarı sürülme görüntüsünü kurar. Bu dikey terslik, erişemeyen yürüyüşle atılma ve dışlanmayı birbirine bağlar; ayet açık bir güzergâh çizmez. Dhālika olağan bir özetleme de olabilir ve yaptırım bağımsız durabilir; bu imge tek başına ilahî güdüyü kanıtlamaz.

Fâtiha'daki {ar:رَبِّ الْعَالَمِينَ, tr:rabb al-ʿālamīna, gloss:âlemlerin Rabbi} tamlaması, odaktaki {ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin} hitabının kişisel ilişki ufkunu “bütün âlemler”e genişletir (1:2). Fâtiha'daki {ar:مَالِكِ يَوْمِ الدِّينِ, tr:māliki yawmi al-dīn, gloss:din gününün sahibi} ise Cehennem'e atılma sonucuna hesap ve yargı zamanı ufku ekler (1:4). Bu iki temas yalnızca ilgili tamlamalarla sınırlıdır: Fâtiha'nın bütünü devreye girmez, varış yeri değişmez ve bir zaman çizelgesi kurulmaz. Aynı biçimde, odaktaki {ar:آخَرَ, tr:ākhara, gloss:başka} hâlâ ilahı niteleyen “başka” sıfatıdır; hesap ufkuyla yakınlığı ona ahiret anlamı yüklemez.

## Hikmetin başka bağlamları

Vahyin muhataba yönelmesi başka bir baskıyla karşılaşır: elçiyi kendisine vahyedilenden uzaklaştırıp başka bir uydurma anlatıya çekmeye çalışırlar (17:73). {ar:عَنِ الَّذِي أَوْحَيْنَا إِلَيْكَ, tr:ʿani lladhī awḥaynā ilayka, gloss:sana vahyettiğimiz şeyden} sözü, bu saptırma girişimiyle birlikte odaktaki {ar:أَوْحَىٰ, tr:awḥā, gloss:vahyetti} için hedefli ve muhataba özel aktarım yankısını güçlendirir; olağan ilahî bildirim anlamı temel kalır. Odakta {ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin} kaynak, {ar:إِلَيْكَ, tr:ilayka, gloss:sana} alıcı oluşu bu kişiye yönelmiş aktarımı destekler. Ayrı bir örüntüde vahyedilene uyma çağrısının ardından O'ndan başka ilah olmadığı ve müşriklerden yüz çevrilmesi gelir (6:106); bu, rehberliğe bağlılıkla ortak ilahı reddetme yönünü buluşturur. İki bağlam sırasıyla hedefli aktarım ve tektanrılı yöneliş için dayanak sağlar; bağlam biçimleri odaktaki sözcüklerle özdeş sayılmaz.

Hikmet ailesindeki sağlam ve kusursuz düzenleme imgesi, yasağın sınır koyan yönüne bağlanır; kapanıştaki {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ve {ar:مَدْحُورًا, tr:madḥūran, gloss:kovulmuş} bu yönlendirmenin ahlaki ve mekânsal sonucunu görünür kılar. Böylece hedefli bildirimden sorumluluk taşıyan davranışa uzanan bir okuma oluşur. Bu bağlantı hikmet adının düzenleme yankısına dayanır; gizlilik tek başına otorite kanıtı değildir ve isim bir inşa fiiline dönüşmez.

Aynı alıkoyma ailesinin fiziksel imgesi, hayvanın çenesini kuşatıp koşmasını ve başıboş ilerlemesini engelleyen gemdir. Vahiy yönünden başka tarafa çekilme girişimi bu imgeyi hikmet adına benzetme yoluyla bağlar (17:73): gem hareketi tutarken rehberlik de yönün kaybolmasını önleyen dayanak gibi duyulur. Namazın hayâsızlık ve kötülükten alıkoyması, aynı gem imgesine bağımsız bir ahlaki tetikleyici verir (29:45); bu örnekte vurgu yıkıcı davranıştan geri çevrilmedir. İki bağlam farklı katkılarla alıkoyma benzetmesini destekler; namaz odak ayette yer almaz ve fiziksel gem hikmetin doğrudan sözlük karşılığı değildir.

Başka bir ayette aynı rakip-ilah eyleminin ardından şiddetli azaba atma buyruğu gelir (50:26). Bu etkin atma sahnesi, odaktaki {ar:فَتُلْقَىٰ فِي جَهَنَّمَ, tr:fa-tulqā fī Jahannama, gloss:Cehennem'e atılırsın} edilgen sonucunun zorlayıcı gücünü belirginleştirir; odakta atan belirtilmez ve varış yeri Cehennem olarak kalır. Kelime ailesinin iyilik ya da kötülükle karşılaşma ve ondan pay alma kolu da Cehennem ve şiddetli azap bağlamında, atılan kişinin yaşayacağı zarara bir yankı ekler (50:26). Bu zarar çağrışımı atılma okumasına eşlik eder, onun yerini almaz.

Hemen elde edilene yönelmenin ardından Cehennem ve kınanma-kovulma sonucu gelir (17:18). {ar:مَذْمُومًا مَدْحُورًا, tr:madhmūman madḥūran, gloss:yerilmiş ve kovulmuş} ifadesi odakla kovulma hâlini paylaşır; odaktaki {ar:مَلُومًا, tr:malūman, gloss:kınanmış} ise farklı biçim ve köktedir. Böylece bağlam, aynı sözcüğü değil kınanma ve uzaklaştırılma sonucunu yankılar. Başka ilah edinmeme yasağının kınanma ve yardımsız kalmayla sonuçlanması da bu uyarı örüntüsüne bir varyant ekler (17:22): {ar:وَلَا تَجْعَلْ مَعَ اللَّهِ إِلَٰهًا آخَرَ فَتَقْعُدَ مَذْمُومًا مَخْذُولًا, tr:wa-lā tajʿal maʿa Allāhi ilāhan ākhara fa-taqʿuda madhmūman makhdhūlan, gloss:Allah'la birlikte başka ilah edinme; yoksa kınanmış ve yardımsız kalırsın}. Bu örnekler odaktaki Cehennem'e atılma ve kovulmayı sonuç ailesine yerleştirir; yer ve dışlanma boyutlarıyla onu kendi kip ve akıbeti olarak bırakır.

Odaktaki {ar:آخَرَ, tr:ākhara, gloss:başka} sıfatı, koşullu ilahlar iddiasıyla birlikte yeni bir ilişki kazanır: eğer iddia edildiği gibi O'nunla başka ilahlar olsaydı, onların Arş sahibine bir yol arayacağı söylenir (17:42), ardından O'nun söylediklerinden yüce olduğu bildirilir (17:43). Bu koşul, iddia edilen ilahların gerçekten var olduğunu doğrulamaz. Koşullu sahne, ākhara'nın olağan “başka, öteki” anlamını korurken rakipleri bağımsız eşitlerden çok Arş sahibine yönelen bağımlı talipler gibi gösterir; bağımlılık sıfatın sözlük anlamı değil, bu bağlamın katkısıdır. Kapsamı bu iki ayetin koşullu iddiasıdır: 17:44'teki kozmik övgü (17:44) ve çevredeki etik buyruklar (17:34), (17:35), (17:36), (17:37), (17:38) bu okumaya eklenmez; vahyin yazılı bir kod olduğu da ileri sürülmez. Hedef biçimlerin odaktaki sözcüklerle özdeşliği iddia edilmez.

Aynı koşullu sahne hikmetin alıkoyup geri çevirme yönüne de temas eder (17:42; 17:43): yol arayışı rakip ilahların bağımlı konumunu, aşkınlık bildirimi ise bu iddianın sınırını belirginleştirir. Böylece buyruk, rakip ilahi mertebeye ve nihai yetki iddiasına sınır çizen bir yönlendirme gibi okunabilir. Bu, hikmetin sözlük tanımını değil, söz konusu iki ayetin sağladığı bağlamsal genişlemeyi anlatır; hedef biçimlere ilişkin ek çözümleme getirmez.

Yetki teması başka bir bağlamda yargılamaya döner: çekişilen konuların bağlayıcı hükmü Allah'a bırakılır (42:10). Odaktaki {ar:تَجْعَلْ, tr:tajʿal, gloss:edinme / yapma} statü atama fiili ile {ar:الْحِكْمَةِ, tr:al-ḥikma, gloss:hikmet} adı bu hüküm yetkisiyle buluşunca rakip bir bağlayıcı merci kurma sorusunu açar. Bu bağlantı karar yetkisine dair bir düşünce alanı sağlar; odak ayet mahkemeleri ya da bütün insan yargısını şirk olarak adlandırmaz. İbadetle hüküm yetkisinin aynı alan olup olmadığı açık kalır; bağlam sözcükleri için biçimbilgisel özdeşlik ileri sürülmez.

Hikmet adının doğruyu bilgi ve akılla ayırma yönü, verilen hikmetin çok hayır sayılması ve akıl sahiplerinin anılmasıyla aydınlanır (2:269). Şükür buyruğunun yanına Allah'a ortak koşmama uyarısının gelmesi, bu ayırt edici bilgeliği davranış yönüne taşır (31:12; 31:13). Bu bağlamlar, odaktaki yasağı hikmetli ayrımın yaşanan bir örneği gibi duyurur; bağlantı tematik yankıdır, alıntı ya da biçim özdeşliği değildir ve hikmetin bütün anlamını bu yasağa indirmez.

Son olarak, ayetleri sağlamlaştırıp ardından ayrıntılandıran kitap tasviri (11:1), odaktaki {ar:ذَٰلِكَ, tr:dhālika, gloss:bu} işaretiyle toplanan {ar:الْحِكْمَةِ, tr:al-ḥikma, gloss:hikmet} buyruk bloğuna iyi kurulmuş bir vahiy düzeni imgesi katar. Sağlamlaştırma ve açıklama sırası, bu buyrukların düzenli ve açık bir bütün içindeki yerini düşündürür. Bu, kelime ailesinden gelen bağlamsal bir imgedir; odak buyruk bloğunu kusursuz metin diye nitelemez, hikmet de “kusursuz kitap” anlamına gelmez. Başka ayetteki biçimlerle özdeşlik ileri sürülmez.

</source_prose>
