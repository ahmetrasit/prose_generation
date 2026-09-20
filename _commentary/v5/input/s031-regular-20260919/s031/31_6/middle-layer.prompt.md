# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:6**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.middle.claims.json`

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
- Refer to source paragraphs as `31:6 ¶N`.

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

`(31:6 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:6",
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
        "citation": "(31:6 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_6/31_6.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_6/31_6.middle.claims.json \
  --ayah-ref 31:6
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_6/31_6.prose.editorial.tr.md`

<source_prose>
## Söylemin Alımı

Âyet, insanlar arasından davranışıyla tanınan bir tipi gösterir: kişi oyalayıcı bir söylem satın alır; bilgisizce başkalarını Allah’ın yolundan saptırmaya ve gönderimi açık bırakılan bir şeyi alay konusu edinmeye yönelir. Son hüküm bu topluluğa aşağılayıcı bir azap bulunduğunu bildirir. Başlangıçtaki {ar:وَ, tr:wa, gloss:ve} önceki söz akışını sürdürür; hemen ardından gelen {ar:مِنَ, tr:mina, gloss:-den}, belirli çoğul {ar:ٱلنَّاسِ, tr:al-nāsi, gloss:insanlar} içinden bir kesit seçer. Böylece uyarı bütün insanları aynı davranışla tanımlamaz: önce insan topluluğu anılır, açık tekil {ar:مَن, tr:man, gloss:kim} ise bu alan içinden davranışıyla tanınacak kişiyi gösterir; aynı açık zamir bu davranışı sürdüren herkese de yayılabilir. Kısa bağlaç ve edatın ardışık sesi de toplumsal çerçeveye kesintisiz bir giriş duyurur; eylemler sıralanmadan önce hangi tür insan davranışının anlatılacağı belirir. {ar:ٱلنَّاسِ, tr:al-nāsi, gloss:insanlar} sözcüğünün temel karşılığı “insanlar”dır; sözlük ailesindeki “görerek fark etme” kullanımı satın alma ve dikkati yöneltme sahnesine ihtiyatlı bir algı çağrışımı ekler. Türetim çözümlemesi tartışmalı olduğu için bu temas temel anlamın yerini almaz.

{ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} fiilinin sekizinci kalıptaki geniş zamanlı biçimi alışverişi yinelenebilir bir edinim, faili de bu eylemin içine giren biri olarak sunar. Satın alınanın ne olduğu açıkça söylenir: fiilin nesnesi olan {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}. Âyet geniş oyun ve eğlence alanının tamamını değil, konuşmayı da içeren belirli bir oyalamayı öne çıkar. Fiil, ödenecek bedeli ya da elden çıkarılan değeri adlandırmaz; yine de satın alma çerçevesi bir karşılık verildiğini düşündürür. Bu okumada karşılığın miktarı belirlenmez. Aynı {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}, hem satın alınan nesne hem de tamlamanın ilk parçasıdır; belirli biçimdeki {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} bu oyalamanın içeriği olarak bağlanır, bağımsız herhangi bir konuşma diye bırakılmaz. {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} için olağan anlatı ve aktarılan söz anlamlarının yanında “yeni, taze, başlangıcına yakın” bir kullanım da vardır. Oyalama sözcüğünün yönettiği bu bağlamda yenilik, dikkat dağıtan içeriğe dönüşebilir; fiilin tekrarlanabilir alışverişiyle birleşince art arda edinilen taze söz birimleri de akla gelir. Bu yan çağrışım, söylemin taze içeriğini öne çıkarırken olağan “söylem” anlamını korur; nitelik bütün konuşmalara yayılmaz. İşitilişte açık heceli {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}dan daha ağır ritimli {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}e geçiş bir ağırlık artışı duyurur; bu ritim söylemi oyalama başlığı altında işittirir, anlam bağını ise tamlama düzeni taşır.

Alışverişin bu çağrışımı iki ayrı sahnede yankılanır: sapmanın bedelle edinilmesi (4:44) ve Allah’ın ayetlerinin az bir karşılıkla değiştirilmesi (9:9). Bu paraleller {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} fiilinin edinme kadar elden çıkarma yönünü de açar; böylece bedelli alışveriş yankısı olağan satın alma anlamını genişletir. Bu yakın okuma (31:6)’daki alıcıyı dış sahnelerin aktörleriyle özdeşleştirmez ve ne verdiğini ya da hangi bedeli ödediğini belirlemez; somut fiyat veya gerçek pazar kurulmaz. {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}nun bir başka yüzü, ilgiyi başka yere çekip kişiyi belirli bir şeyden alıkoymasıdır; satın alınan söylemin Allah’ın yolundan uzaklaştırma amacı bu dikkat işlevini harekete geçirir. Bu, dikkatin yönü üzerine bir temastır; belirli bir modern araç ya da mecra iddiası değildir. Böylece satın alma yalnızca eğlence edinmek değil, dikkati ve bağlılığı yönlendiren bir rekabete katılmak olarak da duyulur.

Satın alınan söz, bu kez dikkatin başka uğraşlarla yarıştığı alana girer. (21:2)’de yenilenen bir hatırlatma {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}nin tazelik anlamına bağımsız bir temas açar; aynı sahnede oyunla meşgul olanlar {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}nun eğlenme ve zevk veren uğraş anlamını tetikler. (63:9)’da mal ve çocukların anmadan alıkoyması, aynı {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} kelimesinin dikkati başka yöne verip kişiyi bir şeyden uzaklaştıran işlevini ayrı bir bağlamda gösterir. Bu katkılar birlikte satın alınmış söylemi hatırlamadan uzaklaştırabilecek uğraşlar arasına yerleştirir. Taze birimler taşıyabilen {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}, bilinçli edinmeyi taşıyan {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır}, meşguliyeti taşıyan {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}, başkasını yönünden ayıran {ar:يُضِلَّ, tr:yudilla, gloss:saptırır} ve yürünebilir rota olan {ar:سَبِيلِ, tr:sebîl, gloss:yol} birlikte düşünüldüğünde söylem, Allah’ın yolundan başkalarını saptırmak üzere tekrar tekrar edinilen bir araca dönüşebilir. Bu, olağan söz ve oyalama anlamlarını koruyan ihtiyatlı bir sözcüksel bütünleştirmedir; (21:2) ile (63:9)’daki kişiler (31:6)’daki alıcıyla özdeşleştirilmez, satın alınan söz de vahiy diye yeniden adlandırılmaz. Kök temasları kesin biçim çözümlemesi iddiası taşımaz.

Sözün çekiciliğinin bir başka yönünü, insan ile konuşma arasındaki ilişki açar: {ar:ٱلنَّاسِ, tr:al-nāsi, gloss:insanlar} yakınlık, arkadaşlık ve yabancılığı gideren eşliği; {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} işitilen ve aktarılan sözü; {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} edinmeyi; {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} dikkati başka yöne çekmeyi hatırlatır. Böylece söz, önermesi tartılmadan önce tanıdık bir beraberlik ya da aidiyet sunarak da çekebilir. Bu bağ, yakınlık ve aidiyetin söze ekleyebileceği çekimi gösterir; özel sözlük temasından doğduğu için temel anlamı veya biçim çözümlemesini değiştirmez.

Söylemin yakınlık ve aidiyet yoluyla çekebilmesi, alışverişin yöneldiği amacı gölgelemez: amaç bildiren lâm {ar:لِ, tr:li, gloss:için}, doğrudan {ar:يُضِلَّ, tr:yudilla, gloss:saptırır} fiiline eklenir ve satın almayı saptırmanın amacı ya da sonucu olarak kurar. Bu bağ, sorumluluğu hem tasarlanmış yanıltmaya hem de öngörülebilir saptırıcı sonuca uzatır. Dördüncü kalıbın ettirgen biçimi, bir failin başkasını yoldan ayırmasını öne çıkarır; etkilenen kişiler belirtilmediğinden kimlerin saptırıldığı açık kalır. Aktarılan {ar:يَضِلَّ, tr:yaḍilla, gloss:sapsın} okuyuşu ise failin kendisinin sapması olasılığını da canlı tutar; iki okuma birbirini silmez. Fiilin ikizleşen ünsüzü işitsel bir basınç yaratır, fakat anlamı tek başına ses değil, ettirgen biçimle yol ilişkisidir. Ayrıca bu fiilin sözlük ailesindeki kaybolma, gizlenme ve gözden yitme kullanımı, bağımsız {ar:عَن, tr:ʿan, gloss:-dan uzak} edatıyla ve adı konan yolla buluşunca güzergâhın görünmezleşmesi imgesini açar. Kaybolma ve gözden yitme dalı, burada ettirgen “saptırma”ya yerel bir imge ekler; fiilin olağan anlamı sürer, fiziksel gizlenme ya da belirli bir etkilenen kişi tanımlanmaz.

{ar:عَن, tr:ʿan, gloss:-dan uzak} ile onu izleyen {ar:سَبِيلِ, tr:sebîl, gloss:yol}, uzaklaşılan noktayı insanların üzerinde yürüyebildiği uzanmış bir güzergâha dönüştürür; kayıp belirsiz bir nesneye göre değil, Allah’ın adıyla belirtilen yola göre ölçülür. Tekil ve belirli tamlama herhangi bir hedefi değil, belli bir yolu gösterir; {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} tamlayan olarak bu yolu O’na nispet eder. Bu tamlama hem yürünüp ilerlenen belirli bir güzergâhı hem doğruluk, iyilik ya da kurtuluşa yönelten dinî yolu açık tutar. Saptırmanın ölçüsü böylece belirsiz bir kayıp değil, Allah’a nispet edilen yoldan uzaklaşmadır. Güzergâhın sıradan, yürünebilir anlamı sürerken rehberlik de rota gibi kavranır; bu mekânsal temas söz konusu sözdizimsel kesitle sınırlıdır. (31:5)’te hidayet ve başarıyla gösterilen yol, bu güzergâhın rehberlik yüzünü açar; tilavet karşısında yüz çeviren dinleyici (31:7)’de satın alınan söylemin bu rehberlikle işitme düzeyinde nasıl yarışabildiğini gösterir. Bu bağlantıda {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} ile alınan söz, {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}nun dikkati çekmesi ve {ar:يُضِلَّ, tr:yudilla, gloss:saptırır}nin başkasını yönünden ayırması üzerinden {ar:سَبِيلِ ٱللَّهِ, tr:sebîlullāh, gloss:Allah’ın yolu}ndan başka yöne çeken bir araca dönüşebilir. Alay da terk edilen güzergâhı değersiz gösterme etkisi kazanır. Bu komşuluk (31:7)’de ayrı bir alay eylemi ya da zorunlu neden-sonuç çizgisi kurmaz, her satın alınmış eğlenceye de genellenmez; bu sınırlar içinde alay, yolun değersiz görülmesiyle yerel bir yankı kurar.

Bu yol değişiminin işitmeyle ilişkisi, (31:7)’nin kendi sahnesinde belirginleşir. Âyetteki {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}, okunan ayetlerle aynı işitme alanına girebilen bir söylemdir; {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} ise dikkati tilavet işitilmeden önce başka yöne çekebilir. Böylece söz, ikna edici düşünce tartılmadan önce alımlamayla yarışan bir uğraş olarak düşünülebilir. (31:7)’de ayetler peş peşe okunur, dinleyen etkin biçimde yüz çevirir ve onları işitmemiş gibi olur; kulaklardaki ağırlık, anlamaya ve uymaya açılan alımlayamamanın bedensel bir modeli olarak belirir. (31:7)’de dinleyenin kibirli yüz çevirmesi satın alınmış sözden bağımsız bir ret nedeni olarak kalır; kulaklardaki ağırlık ise anlamaya ve uymaya açılan alımlayamamanın bedensel modelidir. Konuşma ve anlatma tilavetle aynı söylem türü değildir; bu bağlantı söylemlerin özdeşliğini değil, değerlendirmeden önceki işitme rekabetini gösterir.

İşitmenin nasıl yöneldiği sorusunun ardından, (31:2)’de hikmetli Kitabın ayetlerinin önce anılması satın alınan söyleme başka bir ölçü getirir. Bu sırayla bakıldığında kuşku yalnızca sözün yeni ya da eğlenceli olmasından değil, yön veren ve düzeltici söyleme karşı kullanılmasından doğabilir. Kitabın ayetleri görünür ve incelenebilir işaretler, Kitabın bütünlüğü parçaları birbirine bağlayan bir yapı, hikmet de düzeltici bir yön sunar; âyetteki {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} ilgiyi bu yönelimden başka yere çeker. Bu sıralama, (31:2)’deki ayet, bütünlük ve hikmetin oyalayıcı söylem karşısında ölçü sunmasını sağlar. (31:2) ile (31:6) arasındaki bu yakınlık başka konuşmaları kusurlu saydırmaz ya da odak âyetin anlamını tek başına belirlemez.

## Yol, İşitme ve Bilgi

(31:10)’da göklerin görünür direkler olmadan yaratılması, yere sağlam dağların yerleştirilmesi ve yeryüzünün sallanmasının önlenmesi anlatılır. Bu maddi sahnede dayanak ayakta tutar, dağlar yerinden oynamaya direnir, salınımın önlenmesi istikrar sağlar. {ar:سَبِيلِ ٱللَّهِ, tr:sebîlullāh, gloss:Allah’ın yolu} ile birlikte düşünüldüğünde saptırma, yanlış hedefe yönelmenin yanında güzergâhta yönünü koruma istikrarını sarsma olarak da okunabilir. Bu benzetme (31:10)’daki yaratılış sahnesini söylemin kozmik dayanakları ortadan kaldırdığı iddiasına dönüştürmez; burada yalnızca yol imgesine dayanak ve sarsılmaya direnç boyutu ekler.

Söylemin işitilmesi bu kez oyalama sözcüğünün maddi biçimde alınıp verilmesine açılan iki bağımsız kullanımı görünür kılar: {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}. Bunlardan biri öğütülecek tahıl payıdır: öğütmelik, değirmenin ağzına ya da üst deliğine elle bırakılır. {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} işitene ulaşan söz içeriği anlamıyla ve (31:7)’nin kulağa gelen tilavetiyle buluştuğunda alınan oyalama, işlenen ve duyulur biçimde sunulan bir içerik gibi canlanır. Başka bir kullanım ağız tavanının gerisinde boğaza doğru sarkan küçük dil dokusunu adlandırır; konuşma ve anlatma eylemiyle, ardından gelen tilavetin bağımsız ses akışıyla birleşince odağı soyut içerikten ağızdan kurulup işitilen söze taşır. Tahılın değirmene verilmesi, içeri alınan ve işlenen girdi boyutunu; küçük dilin söz üretimindeki yeri ise ağızdan çıkıp işitilen ses boyutunu sağlar. Bunlar ayrı işlemlerdir, ama birlikte alınan, işlenen ve duyulan içerik akışını kurarlar. Bu iki özel sözlük kullanımı âyetin sahne unsuru ya da her oyalama sözcüğüne yayılan bir anlam değildir.

Bu girdi imgesi, (31:27)’deki kalemler ve yenilenen mürekkeple başka bir yöne açılır: denizler mürekkep olsa bile Allah’ın sözleri tükenmez. Âyetteki {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} ile alınan {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}, yazı araçları, yeniden dolan mürekkep ve anlamlı sözlerin tükenmezliği yan yana gelince maddi olarak sağlanan bir söylem türüyle kıtlığın ötesinde kalan bir söz kaynağı karşılaşır. Okuyucu yalnızca söylemin ne dediğini değil, nasıl sağlandığını da görür: biri alınan ve yenilenen bir ürün, diğeri tüketilemeyen bir kaynak gibi belirir. Bu karşılaştırma (31:27)’nin asıl odağı olan ilahî büyüklüğü korur: (31:6)’daki alıcıya Allah’ın sözlerini değiştirme amacı yüklemez, kalem ve mürekkep sahnesini de günümüz iletişim endüstrisiyle özdeşleştirmez. 

{ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} için verilen tahıl kullanımı, öğütülecek payın değirmen ağzına elle bırakılmasını anlatır; bu somut giriş, alınan içeriğin beslenmesi imgesine malzeme olur. {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem}nin yeni ya da taze anlamı art arda ortaya çıkan birimleri, {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır}nin bilinçli edinimi, (31:27)’de yenilenen mürekkep ise süren tedariki ekler. Bu katkılar birlikte oyalamayı tek mesajdan çok yeni içeriklerle beslenen bir dikkat süreci olarak düşündürür. Bağlantı özel ve uzaktır: mürekkep dışarıdan gelen girdi olarak kalır; bu okuma {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}nın olağan karşılığını değiştirmez ve gerçek bir iletişim mecrası ya da fiyat belirlemez.

Sözün nasıl beslendiği anlatıldıktan sonra, “bilgisizce” koşulu yol ile bilgiyi yeniden aynı soruda buluşturur. {ar:بِ, tr:bi, gloss:ile} davranışa sıkıca bağlanan bu koşulu açar; {ar:غَيْرِ, tr:ghayri, gloss:olmadan} başı {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} adını yöneterek yokluğu bağımsız bir olumsuzluk sözcüğünden çok isim tamlaması içinde kurar. Belirsiz {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} belirli bir öğretiyi değil, bilgi dayanağının yokluğunu anlatır; “bilgi olmaksızın” kaydı saptırma ile alay konusu edinme eylemlerinin ikisine de yayılır. Bilgi adının sonundaki tenvin bu kısa öbeği {ar:وَ, tr:wa, gloss:ve} ile gelen ikinci eylemden önce işitsel olarak kapatır. Sözlük ailesinde olağan bilme ve gerçeği kavrama anlamının yanı sıra bir şeyi ayırt ettiren, tanıtan ve yol gösteren belirgin iz anlamı da vardır. {ar:سَبِيلِ, tr:sebîl, gloss:yol} sözcüğü ve {ar:بِغَيْرِ عِلْمٍ, tr:bi-ghayri ʿilmin, gloss:bilgi olmaksızın} yapısı bu sınırlı işaret kullanımını yön bulma alanına taşır: bayrak, belirgin bir dağ, yol belirtisi ya da kumaş kenarındaki desen gibi bir iz, güzergâhı tanımaya yardım eder. Böylece yön gösteren iz anlamı, olağan bilme ve gerçeği kavrama anlamının yerine geçmeden eksik bilgiyle yol bulma arasında ihtiyatlı bir çağrışım kurar.

Bu işaret imgesi, kaybolmayla ve başka bir şeyin yerini almayla iki ayrı şekilde ilerler. Bir okumada {ar:سَبِيلِ, tr:sebîl, gloss:yol} gerçek güzergâhı ve {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} sözcüğünün tanıtan işaret anlamını, (31:34)’ün bilinmeyen ufkuyla birlikte düşünür; orada yarın ne kazanılacağı ve insanın hangi yerde öleceği bilinmez. Âyetteki {ar:يُضِلَّ, tr:yudilla, gloss:saptırır}nin gizlenme ve algılanamaz biçimde gözden yitme anlamı, yol ve işaretin yokluğuyla temas edince güzergâhı pratikte görünmez kılar. Burada “işaretleri silmek” yeni bir fiil anlamı değildir; bu işaret kullanımının bayrak, belirgin dağ, yol belirtisi veya kumaş kenarındaki desen gibi ayırt edici izleri yön bulma ihtiyacını somutlaştırır. Yol ve işaretin görünmezleşmesi okumasına (31:34)’ün bilinmeyen ufku eklenir; bu, işaretlerin yön bulmadaki katkısını belirginleştirir. Bağlantı iki sahnenin aktörlerini özdeşleştirmez ve geleceği bilmeden yol izleyememe koşulu kurmaz.

İşaret imgesi iki ayrı mekanizmayla genişler: bol söylem güzergâhı tanıtan izleri örtebilir; {ar:غَيْرِ, tr:ghayri, gloss:olmadan}nin başka bir şeyin yerine koyma kullanımı ise yeni işaretlerin yerleştirilmesini düşündürebilir. Örtülme görünürlüğün kaybıdır; yer değiştirme dalı yalnızca araştırıcı bir olasılıktır, gerçekten sahte işaretler kurulduğu ileri sürülmez. Olağan “bilgisizce” anlamı korunurken bu özel kelime temasları yön bulma okumasını genişletir; gizlenme ve değiştirme sözcüklerin çevirisi olmaz.

Bilgi yokluğu bu kez (31:20)’de Allah hakkında bilgisizce konuşan tartışmacıyla karşılaştırılır; onun sahnesinde yol gösterici ve aydınlatıcı bir Kitap da yoktur. Âyetteki {ar:بِغَيْرِ عِلْمٍ, tr:bi-ghayri ʿilmin, gloss:bilgi olmaksızın} ve {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} ile dış sahnedeki tartışma; “insanlardan biri” ve “bilgisizce” çerçevelerinin tekrarıyla yaklaşır. Hidayetin ve incelenebilir bir kitabın ayrıca eksikliği, yön ve metin ışığı için iki denetim ölçütü ekler. Böylece söz yalnızca zeminsiz bilgi parçası değil, yönsüz ve aydınlatıcı kitaptan yoksun, yine de ikna gücü taşıyabilen bir tartışma düzeni olarak görülebilir. Bu karşılaştırma bilgisiz sözde yön ve doğrulanabilir metin ışığının birlikte eksik oluşunu gösterir; (31:20)’deki tartışmacı, bu yorumda (31:6)’daki alıcıya dönüştürülmez.

Bilgi yokluğu kanıtsız yönlendirmeyi kanıtsız bir talebi reddetmekle karıştırmamayı da sağlar. (31:15)’te bilgiden yoksun, zorlayıcı bir buyruğa karşı çıkılır; buna rağmen aileye iyilikle davranma sorumluluğu sürer. Buradaki {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} ile {ar:سَبِيلِ, tr:sebîl, gloss:yol}, baskı, ret, iyi arkadaşlık ve seçerek izleme dizisiyle temas eder: kişi şirk çağrısına uymaz, ailesine iyi davranır ve Allah’a dönenlerin yolunu izler. Böylece başkasını bilgisizce yönlendirmekle bilgisiz bir buyruğu reddetmek ayrılır; bir talepten uzaklaşmak tek başına yoldan sapma değildir. Bu bağlamda sahne, başkasını bilgisizce yönlendirmekle bilgisiz buyruğu reddetmeyi ayırır; bu karşılaştırma (31:6)’daki kişi ya da aile düzenini tanımlamaz.

Bu ayrımın bir başka sınırını (31:34)’te yarınki kazanç ve ölüm yerinin bilinemez oluşu çizer. Burada da {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} ve {ar:سَبِيلِ, tr:sebîl, gloss:yol} düşüncesi, kanıta dayanarak yön tutmanın geleceğin her durağını sahiplenmek anlamına gelmediğini gösterir.

Yönlendirme ve bilgiden doğan sorumluluk, bu ayrımın ardından (17:36)’da daha açık bir hesap verme ufkuna kavuşur. Bilgisi olmayan şeyin peşinden gitmeme uyarısına işitme, görme ve gönlün sorumluluğu eklenir. Âyetteki {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} bilme ve gerçeğe uygun kavramayı, {ar:سَبِيلِ, tr:sebîl, gloss:yol} izlenen güzergâhı taşır; bunlar (17:36)’daki takip eylemiyle yan yana gelince sorun yalnızca eksik bilgi değil, kanıtsız bir yönlendirmeyi işitme, görme, kavrama ve ardından izleme sorumluluğudur. Bu paralellik (17:36), (31:6)’daki yön ve bilgi ilişkisini daha geniş bir hesap verebilirlik alanına taşır. Bağlantı, iki ayetin aktörlerini birleştirmez ya da her bilgisizlik biçimini aynı ölçüde suç saymaz.

Hesap verme ufku, sözün kendisinin her zaman oyalayıcı olmadığını da belirginleştirir: (31:13)’te Luqmân’ın oğluna verdiği öğüt dinleyeni doğru yöne çevirmeyi amaçlayan ayrı bir konuşma örneğidir. Âyetteki {ar:ٱلْحَدِيثِ, tr:el-hadîs, gloss:söylem} konuşmayı, {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} dikkati başka yöne çeken işlevi taşır; bu yüzden belirleyici olan sözün varlığı değil, dinleyenin dikkatini nereden alıp nereye götürdüğüdür. Bu karşılaştırma kişileri değil sözün işlevini karşı karşıya getirir; tür ya da konuşmacının otoritesi de iki sahne arasındaki farkı açıklayabilir.

Dikkatin hangi yöne çevrildiği sorusu, yolun toplumsal olarak başka bağlılıklarla değiştirildiği iki ayrı sahneye uzanır: (31:21) ve (31:32). (31:21)’de vahye uyma çağrısı karşısında ataların izlediği yol seçilir; (31:32)’de kurtuluştan sonra işaretler bilerek inkâr edilir. Âyetteki {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} dikkati başka bir kaygıya çeken uğraştır; satın alma ve saptırma amacıyla birlikte, yürünebilir {ar:سَبِيلِ, tr:sebîl, gloss:yol}nin yerini alabilecek bir bağlılık gibi okunabilir. Ettirgen {ar:يُضِلَّ, tr:yudilla, gloss:saptırır} bu sahnelerle buluşunca yön kaybının toplumsal ve bilerek sürdürülen biçimleri de görünür olur. Bu iki bağlam okurun ilk yön değişimini sonradan gelen bilinçli inkârdan ayırmasını sağlar; bu karşılaştırma onları tek kişinin yaşam öyküsüne ya da (31:6)’daki alıcının davranışlarına dönüştürmez.

Bu toplumsal yöneliş örneklerinden (31:32)’ye yeniden, bu kez dikkatin kriz sırasında nasıl değiştiğini izlemek için bakabiliriz. Büyük tehlike ve kabaran dalgalar geldiğinde sıkıntı içindekiler yalnız Allah’a yönelir; kurtuluşun ardından ise işaretleri bilerek inkâr ederler. {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş}nun tuttuğu yer, bu öncesi ve sonrası içinde sınanır: tehlikede dikkat dağınıklığı geçici olarak düşebilir, güvenlikte yeniden kurulabilir. Bu zaman dizisinde tehlike, oyalamanın örtebildiği bağlılığı yeniden görünür kılar; korku da dikkatin daralmasını açıklayabilir. Bu, dikkatin kriz karşısındaki değişimine dair bir imgedir; gerçek bir medya katmanı varsaymaz ve iki ayetin kişilerini özdeşleştirmez.

Kriz sahnesinden ayrı bir bağlılık ölçüsü (31:22)’de belirir; âyetteki {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır} ve {ar:يَتَّخِذَهَا, tr:yattakhidhahā, gloss:onu edinir} fiilleri Allah’a teslimiyet, sağlam bir kulpa tutunmak ve güvenilir olana güvenmekle betimlenir. Sağlam kulp, neye bağlanılacağı ve seçilen bağlılığın ne kadar taşıyıcı olduğu konusunda bağımsız bir güven ölçüsü getirir; soru hangi söylemin seçildiğinden, hangi bağlılığın gerçekten ağırlık taşıdığına kayar. Bu retorik karşıtlık nedensel açıklama kurmaz; dişil zamirin gönderimi bu bağlantıda açık kalır.

Bağlılığın neye dayandığı sorusunun yanında, geleceğe ilişkin bilginin sınırı da belirir: (31:34)’te hiçbir canın yarın ne kazanacağını ya da hangi yerde öleceğini bilmediği söylenir. Âyetteki {ar:يَشْتَرِى, tr:yaşterî, gloss:satın alır}, {ar:سَبِيلِ, tr:sebîl, gloss:yol} ve {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} birlikte düşünüldüğünde, edinme iddiası izlenecek yönle ve bilginin sınırıyla karşılaşır: insan gelecekteki dönüşünü ve son noktasını güvence altına alamaz. Bu yüzden mesele yalnızca bir bilgi eksiği değil, kimsenin sahiplenemeyeceği bir gelecek yönünü kesinmiş gibi satma ya da satın alma iddiası olabilir. (31:34) burada genel bir bilgi sınırı sunar; odaktaki alıcıyı tanımlamaz. Satın alımı geleceğin sahibi olma diye yorumlamak, yalnızca bu iki bağlamı buluşturan bir çıkarımdır. Aynı ayetteki {ar:تَدْرِى, tr:tadrī, gloss:bilir} olağan olarak bilme fiilidir; yaygın olmayan bir eşleştirme bu fiilin çevresinde yolun gidişi ve hizalanması çağrışımı kurar. Bu yol-kursu benzetmesi ihtiyatlı bir yan okumadır; {ar:عِلْمٍ, tr:ʿilm, gloss:bilgi} sözcüğünün çevirisi ya da dilbilgisi değildir ve fiilin olağan “bilme” anlamını korur. Yarınki kazanç ve ölüm yeri hakkındaki bilinmezlik âyetteki gerçek yol ve onu tanıtan işaretler için bağımsız bir ufuk sunar; rota imgesi yalnızca bu sınırlı benzerlik içinde geçerlidir.

## Alay ve Sonuç

{ar:وَ, tr:wa, gloss:ve} burada önceki amaç zincirine ikinci bir eylem ekler; yoldan uzaklaştırmaya küçümsemeyi katar ve davranışı ağırlaştırır. Yolun ya da söylemin alay konusu yapılması, edinmenin geçici bir sahiplikten daha fazlasına dönüşmesiyle belirir. {ar:يَتَّخِذَهَا, tr:yattakhidhahā, gloss:onu edinir} sekizinci kalıpta “kendisi için edinme”yi, dişil nesne zamiriyle birlikte taşır; iki nesne alan yapı, gönderimi açık bir unsuru {ar:هُزُوًا, tr:huzuwan, gloss:alay konusu} konumuna sokar. Mastarın nesne görevindeki biçimi burada gülme olayını değil, nesneye yüklenen statüyü adlandırır. Böylece alay, bir anlık gülme olayından çok bir şeye verilmiş statü, benimsenmiş bir küçümseme tutumu olur. İkiz ünsüzlü fiil edinme eylemini işitsel olarak ağırlaştırır, hemzeli alay sözü keskin bir kontur çizer; bu ses özellikleri ifadeleri belirginleştirir, zamirin gönderimi ise açık kalır. (45:9)’da alay kalıbının Allah’ın ayetlerinden sonra gelmesi ve (5:57)’de dinin alay ile oyun konusu yapılması, ayet ya da dinin gösteri ve küçümseme nesnesine çevrilebildiğini gösterir. Bu dış paralellik alayın yön ve vahiy çevresindeki hedeflerini aydınlatır; dişil zamirin göndergesi bu bağlantıda yine açık kalır. Bir başka ihtiyatlı temas, yol ya da söylemin gelip geçici bir şaka değil, süreğen bir alay aracı olarak benimsenmesidir. Kancalı aracın sapı tutma, denetleme ve doğrultmaya yarar; bu işlev bir yön nesnesini alay için edinme fikrine benzetme yoluyla yaklaşır. Bu sözlük çağrışımı seçilen yön nesnesinin nasıl kavrandığını düşündürür; âyette gerçek bir araç sahnesi kurulmaz.

Ardından uzak çoğul {ar:أُو۟لَٰٓئِكَ, tr:ulāʾika, gloss:işte onlar} tekil davranış tipini yargılanan bir topluluk olarak yeniden gösterir; {ar:هُمْ, tr:hum, gloss:onlar} zamiri de “kim”den bu gruba uzanan gönderim zincirini tamamlar. Eylemin betimlenişinden hükme böylece geçilir. Satın alma imgesinin sonucu {ar:لَهُمْ, tr:lahum, gloss:onlara} ile alıcılara döner: cümlenin başına alınan lâm, “onlara” ile “onların payı” yankılarını birlikte taşır. Bu sözcüksel karşılık hükmü alışverişle ilişkilendirir, gerçek bir ödeme anlatmaz. Ceza dilbilgisel olarak gruba bağlanır; grup alıcı olarak gösterildikten sonra belirsiz biçimdeki ve cümlede özne görevini alan {ar:عَذَابٌ, tr:ʿadhābun, gloss:azap} gecikmiş özne olarak gelir ve cezanın türünü belirtmeden varlığını bildirir.

Olağan acı ve ağır cezalandırma anlamındaki {ar:عَذَابٌ, tr:ʿadhābun, gloss:azap}, etkin ortaç biçimindeki {ar:مُّهِينٌ, tr:muhīnun, gloss:aşağılayıcı} ile birlikte hem acı veren hem küçük düşüren bir yaptırımı düşündürür. Dördüncü kalıptaki sıfat cezayı yalnızca aşağılanmış durumda değil, aşağılayıcı etkiyi gerçekleştiren nitelikte sunar. İkili tenvinin işitilişi hükmü sıkı bir kapanışa toplar, fakat yeni bir ceza türü eklemez; ceza ile aşağılayıcılığı aynı kısa son seste birleştirir. Başta satın alınan oyalama, hükümde onur düşüren bir sonuçla karşılanır. Ceza olağan acı ve ağır yaptırım anlamında kalır; ayrı sözlük kullanımları burada özel bir ceza biçimi belirlemez, tam biçim açık bırakılır. Allah’ın yolundan söz edildikten sonra gönderimi açık bir unsurun alay konusu yapılması, {ar:مُّهِينٌ, tr:muhīnun, gloss:aşağılayıcı} sıfatındaki onur kaybı ve değersizleştirme anlamıyla bir ayna okuması kurabilir: başkasını küçümseyen tutum, failin kendi itibarının düşmesiyle karşılık bulur. (45:9)’da alay ile aşağılayıcı cezanın yeniden yan yana gelişi bu okumayı destekler; kapsamı her cezanın suçu aynen yansıttığı bir kurala dönüşmez. Burada metindeki etkin, aşağılayıcı sıfat öne çıkar; başka bir kök çözümlemesindeki sakinlik anlamının âyette bağımsız bir taşıyıcısı yoktur. Bu alay-aşağılama yankısı söz konusu çözümleme farkı nedeniyle ihtiyatlı kalır, başka okumaları geçersiz kılmaz.

Bir başka ihtiyatlı aynalama, {ar:عَذَابٌ, tr:ʿadhābun, gloss:azap} ve {ar:مُّهِينٌ, tr:muhīnun, gloss:aşağılayıcı} ile alınan değeri ya da gücü kullanıma koşup yıpratma alanını küçümsemeden doğan onur kaybıyla buluşturur: yönlendirmeyi araçsallaştıran kişinin kendi konumu aşağı çekilebilir. Özel sözlük eşleştirmelerinden doğan bu tersine dönüş benzetmesi, olağan ceza anlamı ile aşağılayıcı niteliği birlikte duyurur; gerçek anlamda bir yıpratma eylemi değil, aşağı çekilen fail konumunu belirginleştiren ikincil bir imgedir.

Alaydan önce seçilen uğraş, ceza sözcüğünün başka bir yanını açar. {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} oyun oynayarak ya da zevkli bir işle meşgul olarak eğlenmeyi anlatabilir; (31:24)’te kısa bir yararın ardından zorla cezaya sürüklenme gelir. {ar:عَذَابٌ, tr:ʿadhābun, gloss:azap} için verilen “kişiyi bir işten uzak tutma, o işi ona bıraktırma” kullanımı bu geçişle temas eder: kişi seçtiği uğraştan koparılır gibi düşünülebilir. Aynı dalın “sütten keser gibi ayırma” özelleşmesi, bu kopuşu yerine koyduğu hazdan mecazen kesilme imgesiyle somutlaştırır.

{ar:مُّهِينٌ, tr:muhīnun, gloss:aşağılayıcı} sıfatındaki küçük düşürülme, onur kaybı ve güçsüzlük bu ayrılığa aşağılayıcı bir nitelik katar. Bu uzak ve ikincil çağrışım seçilmiş hazdan mecazi kopuşu somutlaştırır; (31:24)’teki kişiler odaktaki grupla özdeşleşmez ve ceza olağan acı-yaptırım anlamında kalır. Bu bağlantı gerçek bir sütten kesme ya da özel bir ceza biçimi bildirmez; sözlük çözümlemeleri arasındaki ayrım korunur.

Âyetteki {ar:لَهْوَ, tr:lehve, gloss:oyalayıcı uğraş} ile {ar:عَذَابٌ, tr:ʿadhābun, gloss:azap} arasındaki geçiş (31:24)’te kısa yararın ardından zorla cezaya sürüklenme ve (31:33)’te dünya hayatı ile aldatıcının aldatmasına karşı uyarı üzerinden zamana yayılır. Bu iki sahne ayrı bağlamlar olarak kalır; (31:6)’daki alıcıyı tanımlamaz ve onun gelecekteki bedeli bilerek gizlediğini ileri sürmez. Yan yana okuma ise satın alınan zevkin görünen yararıyla sonradan karşılaşılan maliyeti aynı karar ufkunda buluşturur; böylece âyetin sıkıştırdığı süre açılır.

</source_prose>
