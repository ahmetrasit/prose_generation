# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:47**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.middle.claims.json`

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
- Refer to source paragraphs as `17:47 ¶N`.

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

`(17:47 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:47",
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
        "citation": "(17:47 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_47/17_47.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_47/17_47.middle.claims.json \
  --ayah-ref 17:47
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_47/17_47.prose.editorial.tr.md`

<source_prose>
## Bilginin Alanı

Âyet, karşıt grubun davranışını anlatmadan önce bilen özneyi açıkça öne çıkarır: {ar:نَّحْنُ, tr:naḥnu, gloss:biz} zamiri {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi biliriz} yüklemine bağlanır. Sözlüklerde {ar:عِلْم, tr:ʿilm, gloss:bilme} gerçeği tanıyıp kavrama anlamını taşır; bu bilme yüklemi, biraz sonra açılacak dinleme sahnesini ve cümlenin sonundaki “büyülenmiş” nitelemesini aynı bilgi çerçevesine alır. Böylece yerel anlatı, muhaliflerin eylemi görünmeden önce kendi tanıklık zeminini kurar. Bu çerçeve dinleyişi ve alıntılanan teşhisi birlikte kuşatır; gizli saiklerin her birini tek tek çözümleme iddiası taşımaz.

Hemen ardından gelen {ar:بِمَا, tr:bi-mā, gloss:neyle ya da nasıl} öbeği bu bilginin alanını dinleyişe yöneltir. {ar:مَا, tr:mā, gloss:ne} hem “dinledikleri şey” diye göreli okunabilir hem de dinleme eylemini ya da tarzını adlaştırabilir; iki çözümleme de {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi biliriz} yükleminin yönettiği aynı alanı açık tutar. {ar:بِ, tr:bi, gloss:-le ya da -den} araç, ilişki veya sebep değerlerine izin verir; edatla birleşen {ar:بِهِۦٓ, tr:bihī, gloss:onunla ya da onun üzerinden} zamiri önceki {ar:مَا, tr:mā, gloss:ne} öbeğini yeniden tutar, dinlenen içerik, vasıta ve saik seçeneklerini birlikte açık bırakır. Bilgi alanı ilk zaman sahnesinden önce kurulur; sonraki sahneler bu çerçeve içinde açılır, sıraları ise kendi başına neden-sonuç ilişkisini belirlemez.

Âyetteki iki {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} aynı VIII. bâb çekimini yineler, ama tamamlayıcıları dinleyişin iki yönünü ayırır. İlk kullanım {ar:بِهِۦٓ, tr:bihī, gloss:onunla ya da onun üzerinden} ile açık bırakılan araç, içerik veya saik ilişkisine bağlıdır; ikincisi {ar:إِلَيْكَ, tr:ilayka, gloss:sana doğru} ile bir hedef gösterir. İkinci tekil kişi eki dinleyişin Peygamber'e yöneldiğini belirlerken ilk dinleyişin arkasındaki nedeni yine açık bırakır. Tekrar, kapalı kalan ilişkiden belirgin hedefe doğru bir dönüş kurar: ses dikkatle alınır, hedefin açıklığı da yönelişi görünür kılar. Kavrayış, kabul ve itaat bu işitsel teması izleyebilecek ayrı alımlama aşamalarıdır.

## Gizli Danışmadan Alıntıya

İlk {ar:إِذْ, tr:idh, gloss:o sırada} bilgiyi belirli bir dinleme anında görünür kılar. Ardından gelen {ar:وَ, tr:wa, gloss:ve} ile yeni {ar:وَإِذْ, tr:wa-idh, gloss:ve o sırada} cümlesi ikinci zaman sahnesini açar. Burada ikinci {ar:إِذْ, tr:idh, gloss:o sırada} başka bir dinleme fiiline değil, {ar:هُمْ نَجْوَىٰٓ, tr:hum najwā, gloss:onlar gizli danışmadalar} ad cümlesine bağlanır: hareket anlatımından grubun o andaki hâline geçilir. Üçüncü {ar:إِذْ, tr:idh, gloss:o sırada} ise sözü açar. Bu merdiven gibi derinleşen sıra dikkatten danışmaya, oradan alıntıya ilerler; sahnelerin sürelerini ve kesin neden bağını belirlemeden yorum katmanlarını birbirine yaklaştırır, onlara üstünlük sırası vermez.

{ar:هُمْ, tr:hum, gloss:onlar} zamirinin açık özne oluşu, önceki fiillerdeki çoğul dinleyicileri gizli danışmanın da öznesi olarak yeniden gösterir; ayetin kendi zamir zinciri dinleyenleri danışan grup olarak tanıtır. {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ise bu kişilerin kalıcı kimliği değil, o andaki toplumsal durumu bildiren soyut addır ve cümlede yüklem görevini görür: başkalarından saklı özel konuşma ve sır paylaşımı içindedirler. Bu orta halka, duyulan söz ile biraz sonra doğrudan aktarılacak suçlamayı aynı sahne akışında birbirine yaklaştırır.

Gizli danışmanın cümledeki olağan anlamı özel konuşmadır; {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ailesindeki bedensel çıkıntı kullanımı bu yükleme taşınmaz. Ailenin zararlı ya da bağlayıcı bir durumdan sıyrılıp kurtulma kullanımı ise kısa bir sığınak imgesi doğurur. Bunu etkinleştiren yalnızca gizlilik değildir: açılıştaki {ar:أَعْلَمُ, tr:aʿlamu, gloss:en iyi biliriz} bilen öznesi ve danışmanın içeriğini açan sonraki alıntı birlikte düşünüldüğünde, saklı konuşma bilen özne karşısında korunaklı kalmaz, sözü de duyulur hâle gelir. Kurtuluş çağrışımı başarısız bir saklanma ironisi ekler; okuma danışanlara kaçma niyeti yüklemek yerine gizli sözün bu sahnede korunaksız kalışını öne çıkarır.

Üçüncü zaman işareti {ar:يَقُولُ, tr:yaqūlu, gloss:diyorlar} fiilinin önüne gelerek söyleyişi belirli bir ana yerleştirir ve gizli konuşmanın içeriğini açar. Muzari çekim sözü sahnede sürmekte olan bir söyleyiş gibi duyurur; yineleme sıklığını ayrıca belirtmez. Böylece özel konuşma özetlenmiş bir düşünce olarak kalmaz, okur konuşanların kendi sözünü işitir. Fiilin çoğul öznesi {ar:ٱلظَّٰلِمُونَ, tr:aẓ-ẓālimūna, gloss:haksızlık edenler} fiilden sonra geldiğinden söz eylemi adlandırmadan önce başlar; özne geldiğinde belirli, eril çoğul etkin ortaç olarak konuşan grubu niteler ve suçlama açılırken ahlaki çerçeveyi verir. Sıra konuşanların adını geciktirir, onları kimliksiz bir kitleye dönüştürmez.

Bu nitelemedeki haksızlık alanı, bir şeyi hak ettiği yerden, paydan ya da sınırından çıkarma basıncını taşır. Ardından gelen {ar:مَّسْحُورًا, tr:masḥūran, gloss:büyülenmiş} teşhisi algıdaki sorunu elçiye yüklediğinden, ikisi birlikte sorunun yerini değiştiren bir söz okuması kurar: dikkat duyulan iddiadan onu taşıyan kişinin sözde etkilenmiş hâline kayabilir. Bu temas haksızlık edenler nitelemesinin çevresinde, suçlamanın yön değiştirme imgesini belirginleştirir. Âyet hangi hakkın kime ait olduğunu ya da somut bir yer-zaman olayını belirtmediğinden, bu okuma alıntının içindeki yön değiştirmeyle sınırlı kalır.

Alıntının {ar:إِن, tr:in, gloss:değil} olumsuzluk parçacığı bir sınırlama çerçevesi açar; {ar:إِلَّا, tr:illā, gloss:ancak} bu çerçeveyi kapatır. İkisinin arasındaki {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} fiili, konuşanların çoğul bir “siz”e yüklediği takip eylemidir; kişi eki hitabın çoğul muhatabını gösterir, adlarını veya cevaplarını değil. Dolayısıyla sınırlama yalnız ardından gelen “adam” nitelemesini değil, muhatapların ne yaptığına dair iddiayı da kapsar. Açılıştaki {ar:بِمَا, tr:bi-mā, gloss:neyle ya da nasıl} bilgi alanı dinleyişin içeriğini veya tarzını açık bırakırken, sondaki istisna takip suçlamasını tek bir söz grubuna toplar; iki uç bu âyetin bilgi ve isnat çerçevesini kurar, ilk tamamlayıcının belirsizliğini de korur. Dilbilgisi alıntıdaki iddianın sınırını gösterir; doğruluk değerini belirlemez.

{ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} birinin yanında ya da arkasında yürümeyi, ayrıca bir örneği veya öğretiyi izleyip ona göre davranmayı kapsar. Burada insan nesnesi {ar:رَجُلًا, tr:rajulan, gloss:bir adam} olduğu için konuşanlar takip iddiasını soyut bir öğretiden çok tek bir kişiye bağlar. Belirsiz tekil “adam” sunumu kişiyi küçülten bir polemik etkisi yaratabilir; bu retorik etki dilbilgisinin zorunlu sonucu değildir. Gramer kişiyi tekil nesne olarak verir, başka öğretiler hakkında kapsam belirlemez; olumsuzlukla istisna arasındaki fiil ve insan adı ise konuşanların indirgemeci çerçevesini kurar.

Bu insan adını {ar:مَّسْحُورًا, tr:masḥūran, gloss:büyülenmiş} sıfatı tamamlar. İkisi de tekil, belirsiz ve mansub biçimdedir; edilgen ortaç isimle uyumlanıp kapanışta tek bir ad-sıfat grubu oluşturur. Ortaç adamı büyü yapan fail olarak değil, konuşanların iddiasına göre büyüden veya bir etkilenmeden pay almış kişi olarak sunar. Kökün aldatıcı algı, aklın ya da hâlin etkilenmesi anlamları bu isnat içinde duyulabilir; niteleme konuşanların teşhisi olarak kalır. Şafak ya da bedenle ilgili başka sözlük kullanımları bu biçimin yorum alanına girmez; ad ile ortaç arasındaki uyum ise etkilenmişlik isnadını adama bağlar.

Uzun mansub sonlama {ar:مَّسْحُورًا, tr:masḥūran, gloss:büyülenmiş} ile âyetin sonunda işitilir bir durak yaratır; böylece hakaret tek bir ad-sıfat birimi gibi iner ve cümle sınırı duyulur. Bu kapanışın işlevi ses ve sınırdadır. Açılıştaki bilgiyle bu son niteleme yan yana gelince alıntı, dinleyiş için konuşanların sunduğu açıklama gibi duyulur: dikkatlerini neye verdiklerini bilen anlatımın yanında onlar bağlılığı “büyülenmiş” diye adlandırdıkları adamın durumuna bağlar. Bu, konuşanların teşhisidir, anlatıcının hükmü değil; söyleyiş dikkati duyulan mesajdan elçinin sözde etkilenmişliğine kaydırır.

Gizli konuşmadan doğrudan alıntıya geçiş, sözün dolaşımını da düşünmeye açar. Sözlüklerde {ar:القَالَة, tr:al-qālah, gloss:yayılan söz} ve {ar:القِيلُ وَالقَالُ, tr:al-qīlu wa-l-qāl, gloss:dolaşımdaki söz} insanlar arasındaki söz alışverişini anlatır; odaktaki {ar:يَقُولُ, tr:yaqūlu, gloss:diyorlar} ise çoğul öznesine rağmen tekil çekimli söyleme fiili olarak sahnede kalır. Ardından gelen {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} çoğul hitabı alıntıyı dinleyici kitlesine yöneltilmiş bir etiket hâline getirir. Böylece sözlükteki dolaşım imgesi etiketin yayılma ve güven sarsma ihtimalini açar; ayet sözün sahne ötesinde gerçekten dolaşıma girdiğini bildirmez. {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ile {ar:يَقُولُ, tr:yaqūlu, gloss:diyorlar} arasındaki geçiş işitilenden söylenene uzanır; çoğul muhataba yönelen etiket de bu akışta başkalarını izleyişten caydırabilecek bir işlev kazanır.

İzleme suçlaması, dinleyicilerin yöneldiği kişi kadar suçlamayı kuranların dikkatini de metinde görünür bırakır. Aynı fiil ailesinin farklı bir türetmesi, izleri zaman içinde adım adım inceleyerek araştırmayı anlatır; buradaki {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} biçimi takip anlamında kalır. Bu ayrım, yansımayı fiilin tek başına araştırma taşımasına değil, yinelenen {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} dinleyişi ile {ar:إِلَيْكَ, tr:ilayka, gloss:sana doğru} hedefinin, başkalarının takip ettiği suçlamasının yanında durmasına bağlar. Böylece alıntı, konuşanların elçiye dönük sürekli dikkatini metin içinde karşılık olarak gösterir; bu bağ gerçek kovalamaca veya bilinçli psikolojik yansıtma iddiası değil, konuşmanın kurduğu bir aynadır.

## Perde ve Yol

Bu dinleyiş, sûrenin hemen önce kurduğu kavrayış engellerinin içinde yer alır. Göklerin, yerin ve içindekilerin tesbihinden sonra insanların onların tesbihini kavrayamadığı söylenir (17:44). Kur’an okunurken araya {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü perde} konur (17:45); kalplerde {ar:أَكِنَّةً, tr:akinnatan, gloss:örtüler}, kulaklarda {ar:وَقْرًا, tr:waqran, gloss:ağırlık} bulunur ve Rab tek başına anılınca {ar:نُفُورًا, tr:nufūran, gloss:uzaklaşma} gösterilir (17:46). Dışarıdaki perde, içteki örtüler ve kulak ağırlığı ayrı engellerdir; yan yana gelişleri sesle karşılaşmayı sözü kavrama, kabul etme ve ona uyma aşamalarından ayırır. Bu çevrede iki {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} işitsel teması anlatmayı sürdürürken açılıştaki {ar:بِمَا يَسْتَمِعُونَ بِهِۦٓ, tr:bi-mā yastamiʿūna bihī, gloss:neyle ya da nasıl dinledikleri} dinleyişin tarzına da dikkat çekebilir. Engeller bu yorumda işitmenin yokluğundan çok alımlama tarzını öne çıkarır; sûrenin ilahî olarak dayatılmış bir yetersizlik ihtimalini açık bırakması da bu bağı daha geniş bağlamında tutar.

Engellerin dıştan içe bu dizilişi, {ar:ٱلظَّٰلِمُونَ, tr:aẓ-ẓālimūna, gloss:haksızlık edenler} adında karanlıkla ilgili bir yankı da duyurabilir. Tesbihi anlayamama, araya giren perde, kalp örtüleri ve kulak ağırlığı görünür ışığın kesilmesi ya da zihnin kararması imgesine zemin hazırlar (17:44, 17:45, 17:46). Olağan haksızlık edenler nitelemesi korunur; kararma imgesi bu engel dizisinin ona eşlik ettirdiği keşfî yankıdır. Bu bağlantı sözcüğe yeni bir karşılık vermediği gibi, belirli bir hakkın veya payın esirgendiğini de ileri sürmez.

Perdenin sosyal sınır oluşu, gizli danışma için başka bir temas noktası açar. {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ailesindeki ayrılıp uzaklaşma anlamı, Kur’an okunurken araya giren örtülü yüzey ve sınır olarak {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü perde} ile yan yana gelince, özel konuşmayı kendilerine ulaşan hitaptan toplumsal olarak çekilme ve araya bir süzgeç koyma girişimi gibi duyurabilir (17:45). Bu bağlantıda perdenin katkısı araya giren sınır ve örtülü yüzeydir; bunlar ayrılma çağrışımıyla birlikte danışmayı doğrudan karşılaşmadan yalıtır. Ailedeki yüksek yer anlamı bu özel okumaya katılmaz: sahnede su veya yükselti değil, örtülü perde vardır.

Dinleme söz varlığındaki bağ anlamı olağan işitme fiilinden ayrıdır; bu maddi kullanım benzetmenin kaynağını sağlar, odaktaki fiilin çevirisini değiştirmez. İki kez yinelenen {ar:يَسْتَمِعُونَ, tr:yastamiʿūna, gloss:dinliyorlar} iki işitme noktası kurar; ardından gelen {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} bu noktaları kapalı bir toplumsal bağ içinde eşleştirir; önceki âyetteki {ar:وَقْرًا, tr:waqran, gloss:kulak ağırlığı} ise bu bağın dışına cevap vermeyi kısıtlayan ağırlığı sağlar (17:46). Böylece üç ayrı ayrıntı, dinleyişin kapalı ve hareket alanı daralmış bir durum gibi tasarlandığı tek bir maddi benzetmede buluşur.

Bu engel ve bağ imgelerinin ardından odak âyetin devamı işitmeden kurulmuş benzetmeleri incelemeye geçirir. “Bak” çağrısı, zalimlerin elçi için benzetmeler kurduğunu, sonra saptıklarını ve bir yol bulmaya güç yetiremediklerini bildirir (17:48). Gizli dinleme, {ar:نَجْوَىٰ, tr:najwā, gloss:gizli danışma} ve {ar:يَقُولُ ٱلظَّٰلِمُونَ, tr:yaqūlu aẓ-ẓālimūna, gloss:haksızlık edenler derler} ile açılan toplu söz zemini bu inceleme çağrısına taşınır. Haksızlık nitelemesinin yerinden etme çağrışımı suçlamanın yönünü, {ar:مَّسْحُورًا, tr:masḥūran, gloss:büyülenmiş} sözünün aldatıcı algı yönü ise dikkatin mesajdan onu taşıyan kişiye kayışını belirginleştirir; bu birleşim benzetmeleri sahte bir açıklama gibi duyurabilir. Ardından gelen sapma ve yol bulamama, bu açıklama çabasının somut sonucunu verir (17:48). Burada “büyülenmiş” yol kaybının köken açıklaması değil, alıntılanan isnattır; çoğul isnat başka suçlamaları kapsayabilir, sahne ise planlı bir kampanyayı anlatmaz. Böylece yol sonucu, elçinin sözde durumuna yönelen karşılaştırmanın sınırını görünür kılar.

Yol bulamama görüntüsü, “bir adamın ardından gitme” sözündeki bedensel yönü de belirginleştirir. Odaktaki {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} bir kişinin ardından yürümeyi ve bir yol ya da örneği benimsemeyi birlikte taşıyabilir; {ar:رَجُلًا, tr:rajulan, gloss:bir adam} ise erkek insanı, kadın karşıtlığı içindeki adam kategorisini adlandırır. Bu isim, kişinin kendi ayağıyla yürüyen kimse görüntüsüne de açılabilir; aynı ses ailesindeki {ar:رِجْل, tr:rijl, gloss:bacak} ise bacak uzvudur, asma veya yakalama kullanımları da kendi türemiş biçimlerine aittir. Takip fiili ile yol ve sapma, “adam”ı yaya diye çevirmeden ayakla birinin ardınca yürüme imgesine izin verir; insan gönderimi değişmez (17:48).

Bu güzergâh imgesinin yanına Fâtiha topluluğun yön arayışını koyar. {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā ṣ-ṣirāṭa l-mustaqīma, gloss:bizi dosdoğru yola ilet} duası doğru yolu ister (1:6); sonraki âyet bu yolu nimet verilenlerin yolu diye niteler, gazaba uğrayanların ve sapanların yolu olarak değil (1:7). Böylece 17:48'de yitirilen güzergâh ile 17:47'deki kişiyi izleme suçlaması, bir topluluğun yön bulma duasıyla yan yana gelir (17:47, 17:48). {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} fiilinin davranışsal “izleme” anlamı bu duada yol arayışından bir karşılık bulurken, bedensel ardından yürüme görüntüsü de korunur. Bu okuma Fâtiha'nın 1:6 ve 1:7 âyetleriyle sınırlı kalır: odaktaki elçi nimet verilen yol ile, dua eden topluluk da onun sahipleriyle özdeşleştirilmez. Böylece kişiyi izlemenin bedensel ve davranışsal yönleri, topluluğun yön istemesiyle iki ayrı ölçekte yan yana gelir.

## İtiraz ve Karşılık

17:48'deki yol imgesinin ardından soru yön değiştirip yeniden yaratılışın maddi imkânına gelir. Kemik ve ufalanmış kalıntı hâline gelmişken yeni bir yaratılışla diriltilme ihtimali sorulur (17:49). Maddi sınır taş ve demir örnekleriyle sertleştirilir (17:50); “bizi kim geri döndürecek?” sorusu da ilk kez yaratanın yeniden döndüreceği cevabını alır (17:51). Ufalanma, dirençli madde ve ilk yaratılışa dönüş itirazı aynı çizgide adım adım kurar. Bu maddeye bağlı beklenti, 17:47'deki kişisel teşhisle yan yana geldiğinde savunmacı bir okumaya imkân verir: dikkat yeniden yaratılış iddiasından onu dile getiren elçinin sözde etkilenmişliğine kayabilir. Bu bağ komşuluğa dayalı bir olasılıktır; 17:49, 17:50 ve 17:51'deki maddi meydan okuma kendi bağımsız anlamını ve basıncını korur (17:47, 17:49, 17:50, 17:51).

Sonraki çağrı sahnesi maddi itirazdan başka bir yöne döner: çağrılacakları gün karşılık verecekleri bildirilir (17:52). Odakta insanlar elçiyi dinleyip ardından gizli danışma ve isnada geçerken, sonraki sahnede çağrı cevapla tamamlanır (17:47, 17:52). Bu karşılaştırma alımlamanın ölçüsünü sesin kulağa erişmesinden anlamaya, kabule ve karşılığa doğru genişletir. Ahiret günündeki çağrı ile bugünkü dinleme ayrı bağlamlardır; burada öne çıkan, sözlük anlamını değiştirmek değil, cevap eyleminin işitmeye eklediği ölçüdür.

Dinleyişten sonra söze geçiş, insanlar arasındaki ilişkinin nasıl korunacağı sorusuna da bağlanır. Kullara en güzel sözü söylemeleri buyurulur; şeytanın aralarına girdiği ve açık bir düşman olduğu hatırlatılır (17:53). Bu genel ahlak buyruğu önceki danışmayı açıkça teşhis etmez; yine de ikisinin yan yanalığı, gizli danışma ve çoğul muhataba yöneltilen isnadı ilişkilerin arasına kama sokabilecek bir söz devresine yerleştirebilir (17:47, 17:53). En güzel söz bu olası akışta onu kesen karşılığı sunar.

Açılıştaki bilme, elçinin dinleyicilerin cevabına ilişkin sorumluluğunu da yeniden düşündürür. Rabbin insanları daha iyi bildiği söylenir ve elçinin onların üzerine gözetici olarak gönderilmediği belirtilir (17:54); bilgi göklerde ve yerde olanlara kadar genişletilir (17:55). 17:47'de belirli dinleyişin bilinmesiyle 17:54 ve 17:55'teki geniş bilgi birlikte duyulduğunda, elçinin düşmanca alımlamayı yönetmekle yükümlü olmadığına dair bir güvence de belirir (17:47, 17:54, 17:55). Bu, sözü iletmek ile muhatabın cevabını denetlemenin farklı sorumluluklar olduğunu gösteren yerel okumadır; ayetlerin açık vurgusu ilahî bilginin kuşatıcılığı olmaya devam eder.

Bu âyet çevresinde artan temasın anlayış ve kabule değil başka sonuçlara eşlik ettiği sahneler yer alır. Kur’an hatırlatmaları bir grupta uzaklaşmayı artırır (17:41). Semûd'a apaçık görünen dişi deve işareti verilir; ona haksızlık etmelerinin ardından işaretlerin uyarı için gönderildiği belirtilir (17:59). Uyarılma ise büyük bir taşkınlıkla karşılanır: {ar:يَزِيدُهُمْ, tr:yazīduhum, gloss:artırıyor} artışın yönünü, {ar:طُغْيَٰنًۭا, tr:ṭughyānan, gloss:taşkınlık} sınırı aşan karşılığı, {ar:كَبِيرًۭا, tr:kabīran, gloss:büyük} de ölçeğini verir (17:60). Bu üç ayrı sahnede hatırlatma uzaklaşmaya, görünür işaret haksız karşılığa, uyarı ise taşkınlığa eşlik eder. Birlikte, odaktaki dinleyişi daha geniş yerel örüntüye yerleştirirler; bu bağlantı değişmez bir alımlama yasası kurmaz.

## Dinlemenin Farklı Sonuçları

17:47'deki {ar:يَسْتَمِعُونَ إِلَيْكَ, tr:yastamiʿūna ilayka, gloss:sana doğru dinliyorlar} sesin kulakla algılanmasına dayanan sıradan bir dinleyiştir. Başka sahneler işitsel erişim ile kavrayış arasındaki ayrımı açar: elçiyi dinleyenlerin sağır ve akletmez diye anılması (10:42), kalplerdeki örtüler ve kulaklardaki ağırlık yüzünden işitmenin anlayışa ulaşamaması (6:25). Bu iki karşılaştırma sesle karşılaşma ile mesajı kavramanın ayrı aşamalar olduğunu gösterir; 17:47'deki grubun kavrayış düzeyini belirlemez.

Başka iki sahne aynı dinleme hareketinin daha ileri sonuçlara varabildiğini gösterir. Kur’an'ı dinleyen cinlere susmaları söylenir; ardından topluluklarına uyarıcı olarak dönerler (46:29). Bu sahne işitmeyi amaçlı dikkate ve eyleme uzatır. Sözleri dinleyip içlerinden en güzeline uyanlar ise kabulü davranışa taşır (39:18). İki paralel, dinlemenin açılabildiği ayrı sonuçları gösterir; odaktaki grupla dinleyicileri özdeşleştirmez veya onlara bu sonuçları yüklemez.

Bu olumlu izleme örneği, suçlamadaki {ar:تَتَّبِعُونَ, tr:tattabiʿūna, gloss:izinden gidiyorsunuz} fiilinin davranışsal anlamını da belirginleştirir. Fiil bir insanın ardından yürümeyi, ayrıca örnek, buyruk veya söz doğrultusunda davranmayı kapsar; 39:18'de dinlenen sözün en güzeline uyulması ikinci anlamı canlı kılar (39:18). 17:47'de konuşanlar bağlılığı, “büyülenmiş” diye niteledikleri adama yönelmiş gibi çerçeveler (17:47). Böylece fiilin bedensel ve davranışsal yönleri birlikte duyulur; olumlu örnek fiilin taşıyabileceği bir sonucu açar, 17:47 grubunun sonucunu tayin etmez.

## Danışma ve İsnadın Dış Yankıları

Odaktaki gizli danışmanın çoğul sunuluşu, bir sırdaşla değil bir grupla yürüyen özel konuşma biçimini gösterir. Haksızlık edenlerin gizlice fısıldaşıp elçi hakkında büyü sorusu yöneltmesi bu biçimi başka bir sahnede de taşır (21:3). Elçiler üzerine danışma ardından büyücülük suçlaması ve onları uzaklaştırma isteğine açılır (20:62, 20:63); başka bir yerde gizli görüşme günah, saldırganlık ve elçiye itaatsizlik diye değerlendirilir (58:8). Bu örneklerin her biri toplu konuşmanın başka bir yönünü aydınlatır, fakat bu benzerlikler odaktaki kişilerin kimliğini veya ortak bir planı belirlemez. Yakın bağlamda perde ve duyusal engeller alımlamanın önüne sınır koyar (17:45, 17:46); benzetmelerden sonra yol bulamama da yön kaybı imgesini sürdürür (17:48). Bu daha ihtiyatlı yerel bağ gizli danışmayı alımlama ve yön bulma güçlüğü çevresinde tutar. Odak âyette belirli bir hakkın kime ait olduğu söylenmez; bu yüzden “haksızlık edenler” sözü gizliliğin kendisini değil, ona eşlik edebilen sınır aşımını niteler.

Bu karşı-çerçevenin merkezindeki {ar:مَّسْحُورًا, tr:masḥūran, gloss:büyülenmiş} sözü olağan okumasında adama yöneltilmiş büyülenmişlik isnadıdır; edilgen biçimi onu büyü yapan değil, etkilenmiş kişi olarak sunar. Kökün aldatma ve saptırma alanı yanlışı doğru gibi gösterme ya da gerçekte bulunmayanı varmış gibi algılama mekanizmasını ekler. Görülen işaretin “süregelen büyü” sayılarak reddedilmesi, dikkatin işaretten elçinin sözde durumuna çevrilebildiğini gösterir (54:2). Bu algı okuması yanında, gizli güçlerden yardım alma veya onlara yaklaşmayla yapılan doğaüstü işlem anlamı da canlıdır: büyü sorusu ve elçilere yöneltilen büyücülük isnadı bu dalı taşır (21:3, 20:63). Hazine veya bahçeye sahip olmama itirazının “büyülenmiş adam” sözüyle birleşmesi, aynı nitelemenin maddi beklentiyle birlikte kullanılabildiğini gösterir (25:8). Bu bağlamlar iki okuma olasılığını ayrı ayrı besler; yakınlıkları suçlamanın doğruluğuna hükmetmez.

Aynı kök ailesindeki “büyücü” hitabı, farklı konuşma işlerinde yer alır. Bir sahnede “ey büyücü” diye sesleniş yardım isteyen bir yakarışın içindedir (43:49); başka bir sahnede Musa, kendisine yöneltilen büyü suçlamasına itiraz eder (10:77). Bu farklı kullanımlar sözcük ailesine her yerde aynı konuşma işlevini yüklemeyi engeller. Odak âyetteyse edilgen niteleme gizli danışmanın ardından bir kişiye yöneltilmiş teşhistir; anlamını hitabın sahibi ve çevresindeki söyleşi belirler.

Dokuz açık işaretin anılmasının ardından Firavun'un Musa'yı Türkçede “büyülenmiş” diye nitelemesi, kanıtlarla hesaplaşmak yerine elçinin durumunu yeniden adlandıran savunmacı bir karşı-söylem olarak okunabilir (17:101). Odaktaki aldatıcı algı ve yanlış teşhis imgesi bu paralelliği anlaşılır kılar. 17:101'deki biçim ve sözlük ayrıntıları tam sözcüksel eşleşmeyi kurmaz; bu karşılaştırma ortak konuşmacı, geçmiş veya plan da göstermez, odak âyetteki dinleyicilerin dokuz işareti gördüğünü ya da ithamın bilerek uydurulduğunu söylemez. Bu sınırlı yakınlık yine de açık işaretlerin ardından elçinin durumunu yeniden adlandıran savunmacı sözü, odaktaki algı saptırma imgesiyle birlikte düşündürür.

Son olarak {ar:رَجُلًا, tr:rajulan, gloss:bir adam} sözü erkek insanı, kadın karşıtlığı içindeki “adam” kategorisini korur. Bir başka itirazda elçi olarak {ar:بَشَرًا, tr:basharan, gloss:bir insan} gönderilmesi sorgulanır (17:94). {ar:رَجُلًا, tr:rajulan, gloss:bir adam} ile {ar:بَشَرًا, tr:basharan, gloss:bir insan} eş anlamlı değildir; bu sınırlı kategori benzerliği konuşanların aynı olduğunu veya her insan-elçi itirazının düşmanca olduğunu da göstermez. Yan yana gelişleri, “büyülenmiş adam” sözünün hem elçinin insan oluşuna hem de sözde etkilenmişliğine yönelen bir reddiye gibi duyulmasına izin verir.

</source_prose>
