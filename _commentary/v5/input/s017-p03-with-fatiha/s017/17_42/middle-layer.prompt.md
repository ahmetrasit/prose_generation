# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:42**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.middle.claims.json`

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
- Refer to source paragraphs as `17:42 ¶N`.

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

`(17:42 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:42",
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
        "citation": "(17:42 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p03-with-fatiha/s017/17_42/17_42.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p03-with-fatiha/s017/17_42/17_42.middle.claims.json \
  --ayah-ref 17:42
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p03-with-fatiha/s017/17_42/17_42.prose.editorial.tr.md`

<source_prose>
17:42, {ar:قُل, tr:qul, gloss:de ki} emriyle bir cevabı dile getirir: “De ki: O’nun yanında, onların söyledikleri gibi ilahlar bulunsaydı, o takdirde Arş sahibine bir yol ararlardı.” Kurulan koşul, ilahların varlığına dair bağımsız bir hüküm değil, O’nun yanında bulunma iddiasının sonuçlarını sınayan bir varsayımdır: {ar:لَوْ, tr:law, gloss:eğer} öncülü açar, {ar:إِذًا, tr:idhan, gloss:o takdirde} sonucu getirir. Sonuçtaki {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} cevap lâmıyla güçlü biçimde vurgulanır; kesinlik koşulun içinde işler. Geçmiş çekim, varsayımın sonucunu tamamlanmış gibi kurar; burada geçmişte yaşanmış bir olayı anlatmaz. VIII. kalıp arayışı hedefe yönelmiş, maksatlı bir eylem olarak verir; sınır aşımı anlamı bu fiil biçiminden çıkmaz.

Bu çıkarımın ses düzeni koşuldan sonuca geçişe işitsel bir bağ verir. Kısa {ar:قُل, tr:qul, gloss:de ki} sözünün sonundaki lâm, hemen ardından gelen {ar:لَوْ, tr:law, gloss:eğer} sözcüğünün başındaki lâmı yakından izler. Bu yakınlık ayetin açılışında yerel bir ses bağı kurar; önceki sahneden zincir devralmaz ve kendi başına yeni bir anlam eklemez. {ar:إِذًا, tr:idhan, gloss:o takdirde} ise atıftan sonra okuru aynı koşulun sonucuna döndürür.

Koşulun içinde {ar:كَانَ, tr:kāna, gloss:olsaydı} var olma ve bulunma durumunu kurar. {ar:مَعَهُۥٓ, tr:maʿahu, gloss:O’nun yanında} ilişkisinin çoğul özneden önce gelmesi, dikkati önce beraberlik iddiasına çeker: öne çıkan, varlıkla birlikte O’nun yanında bulunma ilişkisidir; bu kuruluş ilahî özler arasında eşitlik bildirmez. {ar:ءَالِهَةٌۭ, tr:ālihatun, gloss:ilahlar} adının gecikmesi, varlık çerçevesi içinde özneyi bir an bekletir; belirsiz çoğul bu bekleyişi korurken sayıyı ve belirli bir panteonu tayin etmez. {ar:مَعَهُۥٓ, tr:maʿahu, gloss:O’nun yanında} sözünün uzayan sesi kısa bir askı yaratır; ardından {ar:ءَالِهَةٌۭ, tr:ālihatun, gloss:ilahlar} başındaki hemze yeni bir ses girişi gibi duyulur. Uzama ve hemze kısa bir ses eşiği kurar; söz dizimi ise kesintisiz sürer.

## Söylenen İddia

Koşulun kaynağını, araya giren {ar:كَمَا يَقُولُونَ, tr:kamā yaqūlūna, gloss:onların söyledikleri gibi} sözü gösterir. Kısa {ar:كَمَا, tr:kamā, gloss:gibi} atfı söyleyenleri hızla bildirir; doğruluk hükmü ise önermenin koşullu sınamasına bırakılır. Atıf yalnızca en yakındaki “ilahlar” adına değil, öne sürülen önermenin bütününe uzanabilir; böylece hem içerik hem de söyleme eylemi işitilir. Ardından gelen {ar:إِذًا, tr:idhan, gloss:o takdirde} okuru yeniden çıkarıma bağlar. {ar:يَقُولُونَ, tr:yaqūlūna, gloss:söylüyorlar} çoğul ve şimdiki zaman biçimiyle sürmekte olan bir söyleyişi verir; tekrar sıklığını ve konuşanların kimliğini belirlemez. Aktarılan sözün çevresinde kısa bir hitap gerilimi de olasılık olarak duyulabilir; lafız bunu ayrı bir söyleyişe ya da kesin kişi değişikliğine sabitlemez. {ar:قُل, tr:qul, gloss:de ki} ile {ar:يَقُولُونَ, tr:yaqūlūna, gloss:söylüyorlar} arasındaki ilişki ayet içinde bir yanıt bağı kurar; bu bağ önceki sahneden taşınan bir ses zinciri değildir.

Bu çoğulluğun neyi öne sürdüğü yakın bağlamda açılır. 17:39 başka bir ilaha yönelmeye karşı uyarır (17:39); 17:40’ta {ar:أَفَأَصْفَىٰكُم رَبُّكُم بِٱلْبَنِينَ, tr:a-fa-aṣfākum rabbukum bi-l-banīn, gloss:Rabbiniz size oğullar mı seçti} ve {ar:وَٱتَّخَذَ مِنَ ٱلْمَلَٰٓئِكَةِ إِنَٰثًا, tr:wa-ittakhadha mina al-malāʾikati ināthan, gloss:meleklerden dişiler mi edindi} sorularını {ar:إِنَّكُمْ لَتَقُولُونَ قَوْلًا عَظِيمًا, tr:innakum la-taqūlūna qawlan ʿaẓīman, gloss:gerçekten büyük bir söz söylüyorsunuz} uyarısı izler (17:40). Bu bağlamda {ar:ءَالِهَةٌۭ, tr:ālihatun, gloss:ilahlar} salt sayıyı değil, kulluğun ve yetkinin kime yöneltildiği iddiasını duyurur. Fâtiha 1:5’teki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīnu, gloss:yalnız Sana kulluk eder, yalnız Senden yardım dileriz} ibadeti ve yardımı Allah’a yönelterek bu iddianın karşısına tek bir yöneliş koyar (1:5). 21:22’de çoklu ilah varsayımı göklerde ve yerde bozulma ihtimalini, 23:91’de yaratılmışların ayrışıp birbirine üstün gelmesi ihtimalini açar (21:22; 23:91). Bu iki sonuç, yetki çokluğunun kozmik düzen ve egemenlik üzerindeki ayrı baskılarını gösterir. Koşulda aktarılan önerme yanlışsa söz de yanlıştır; bu doğruluk ilişkisi tek başına konuşanlara kasıtlı yalan ya da ortak bir niyet yüklemez.

Söyleme ailesi, bir içeriği aktarmanın yanı sıra bir görüşü benimseme anlamına da gelebilir. Bu çağrışım, “iddia doğru olsaydı ardından ne gelirdi?” sınamasını sözü kendi sonucuyla karşılaştırılan bir tutum gibi duyurur; yine de belirli konuşanların özel inancını saptamaz. 17:53 sözün toplumsal ölçeğini açar: kullara en güzel sözü söylemeleri buyurulur ve söz özenle ilişki kuran bir eylem olur (17:53). Aynı ayette şeytanın insanları birbirine düşürmesi, sözün bu ilişkiyi bozabilecek karşı yönünü gösterir (17:53). Bu bağlam, sözün toplumsal etkisini aydınlatır; 17:42’deki arayışın doğrudan nedeni olarak kurulmaz. Odağın kendi çıkarımı ise ileri sürülen ilahları arayıcı kılan eylemde belirginleşir.

## Aranan Yol

Sonucun eylemi, {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} ile amaçlı bir arayışa dönüşür. Olağan kullanımda ilah diye anılan varlıklar, arama fiiliyle tekil bir hedefe ve bir yol nesnesine yönelince ihtiyaç duyan arayıcılar olarak görünür. Ayetin sahnesi ibadet töreninden çok, tapınılan sayılan varlıkların kendilerinin de hedefe ulaşmak için yol aramasına odaklanır.

Arayışın yönünü {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} gösterir; cer hâlindeki {ar:ذِى ٱلْعَرْشِ, tr:dhī al-ʿarsh, gloss:Arş sahibi} ise yönelinen unvanı kurar. Bu hedef, cümlenin sonundaki {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} sözcüğünden önce duyulur: okur önce kimin makamına yönelindiğini, sonra hangi şeyin arandığını öğrenir. {ar:ذِى, tr:dhī, gloss:sahibi} ile belirli ve tekil {ar:ٱلْعَرْشِ, tr:al-ʿarsh, gloss:Arş} bir sahiplik unvanı oluşturur; hedef herhangi bir koltuk değil, belirli bir taht ve yönetim makamıdır. Belirli hedefin belirsiz yolla eşleşmesi, makamı tanıdık ve erişim güzergâhını adsız bırakır. Bu dilbilgisel sahiplik makamın değerini kurar; Arş’ın maddi kuruluşunu ya da mahiyetini tayin etmez. Yöneliş açıkken aranan güzergâh ve ona erişilip erişilmediği açık kalır.

{ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} önce üzerinde yürünebilecek bir güzergâhı, arayış ve hedefle temasında ise o hedefe ulaştıran yol ya da vesileyi düşündürür. Belirsiz biçimi belirli bir güzergâhı adlandırmaz: arama fiilinin doğrudan nesnesi yoldur, {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} da bu yolun yöneldiği makamı gösterir. Böylece erişim anlamı somut güzergâhtan açılır. Ayetin sonunda adsız yolun kalması, arayıcıların hedefe erişme ihtiyacını duyururken varışın gerçekleşip gerçekleşmediğini açık bırakır.

Ses akışı bu yönelişe işitsel ağırlık verir. {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} fiilindeki sıkı ses örgüsünden {ar:إِلَىٰ, tr:ilā, gloss:-e doğru} yönelimine ve sondaki {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} sözcüğüne uzanan akış, bir yön çizgisi gibi işitilir. {ar:إِذًا, tr:idhan, gloss:o takdirde}’dan aynı son sözcüğe inen ritim öncül, çıkarım ve kapanışı bağlar; işitsel çizgi, cümlede kurulan yönelişi pekiştirir.

## Tek Makam ve Dayanak

{ar:ٱلْعَرْشِ, tr:al-ʿarsh, gloss:Arş} sözcüğünün olağan zemini hükümdarın oturduğu yüksek tahttır; bu somut imgeden yönetim makamı anlamı açılır. 23:116’da Allah “gerçek Hükümdar” ve “Kerîm Arş’ın Rabbi” diye anılır; bu unvan aranan hedefi tekil egemenlik makamı olarak belirginleştirir (23:116). 17:43’te O’nun insanların söylediklerinden münezzeh ve yüce oluşu bu egemenliği iddiaların ötesinde tutar (17:43). 17:44’te yedi gök, yer ve içindekiler O’nu tesbih eder; ardından her şeyin O’na hamd ile tesbih ettiği belirtilerek yönelişin ölçeği bütün varlıklara açılır (17:44). Bu geniş tesbih düzeni karşısında çoğul arayıcı ile tek Arş sahibi arasındaki asimetri belirginleşir: arayanlar kudretin kaynağı değil, yöneldikleri makama muhtaç özneler olarak görünür.

Taht imgesine kelime ailesinin bir başka katkısı eklenir: Arş adı, işi ve düzeni taşıyan dayanağı; iktidar ve saygınlığın zeminini de düşündürür. Çoğul arayışın tek taht sahibine ve adsız bir yola yönelmesi, odağı yalnız yüksek bir makamdan o makamın dayandığı düzene taşır; güç ve saygınlık bu temele bağlı hâle gelir. Bu analoji, 23:116’daki Kerîm Arş’ın Rabbi unvanına, 17:43’teki aşkınlık bildirimine ve 17:44’teki evrensel tesbih düzenine temas ederek makam imgesini derinleştirir (23:116; 17:43; 17:44). Bu bağlantıda dayanak imgesi makamın istikrarını taşır; tahtın fiziksel yapısı hakkında hüküm vermez. Arş adının yoğun ünsüzleri de hedefe yerel bir işitsel ağırlık katar; bu ses katkısı fonetik çağrışımla sınırlıdır, ilahî mahiyet hakkında hüküm vermez.

Dayanak imgesi buradan söyleme eylemine uzanır: {ar:قُل, tr:qul, gloss:de ki} ile {ar:يَقُولُونَ, tr:yaqūlūna, gloss:söylüyorlar} olağan anlamlarıyla sözün söylenmesini bildirirken, taşıma çağrışımı öne sürülen iddiayı ayakta durması gereken bir düzen gibi düşündürür. 17:50’deki “taş ya da demir olun” sözü bu benzetmeye taşın katılığını ve demirin direncini katar (17:50). 17:53’te en güzel sözü söyleme buyruğu, aynı konuşma eyleminin ilişki kuran yönünü hatırlatır (17:53). Böylece maddi dayanıklılık ile toplumsal sorumluluk ayrı katkılar sunar: biri iddianın ayakta durması imgesini, diğeri sözün insanlar arasındaki etkisini açar. Bu özel bağlantı, odak ayetteki “söylemek” fiilinin olağan anlamını değiştirmez.

## Bağlamdaki Yönler

Yakın bağlam, görev ile egemenlik arasındaki ayrımı açar. 17:54’te elçinin insanlar üzerine vekil olarak gönderilmediği belirtilir; bu, elçilik görevinin yetki sınırını gösterir (17:54). 17:55’te bazı peygamberlerin diğerlerinden üstün kılınması ve Davud’a Zebur verilmesi, peygamberler arasındaki derece farkını görünür kılar (17:55). Bu görev ve derece farkları Rabbin kuşatıcı bilgisi ve iradesine bağlanır. Bağlam makam farklılıklarını bağımsız ilahlık iddiasından ayrı bir düzlemde tutar; bu yorumun kapsamı peygamberlik görevidir ve Arş’ın mahiyetini belirlemez.

Fâtiha 1:5’te kulluk ve yardım dileği Allah’a yönelir (1:5); 5:35’te O’na yaklaştıracak vesile, 25:57’de Rabbe giden bir yol aranır (5:35; 25:57). Bu örnekler yol arayışının ibadet edenlerin Allah’a bağımlılığı içindeki olağan yerini gösterir. Aynı amaçlı eylem 17:42’de de korunur; odaktaki dönüş, ilah diye anılan varsayımsal varlıkların kendilerinin tek bir üstün makama muhtaç arayıcılar hâline gelmesidir.

17:56 çağrılanların sınırını, sıkıntıyı gidermeye ya da değiştirmeye güç yetirememelerinde gösterir (17:56). 17:57 bakışı onların kendi yönelişine çevirir: çağrılanlar Rablerine yakınlık vesilesi arar, hangisinin daha yakın olacağını gözetir, O’nun rahmetini umup azabından korkarlar (17:57). Buradaki {ar:يَبْتَغُونَ, tr:yabtaghūna, gloss:ararlar}, odaktaki {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} ile aynı kökün VIII. kalıbıdır. Bir ayette yardım güçlerinin sınırı, ötekinde kendilerinin arayışı görünür olur; ortak fiil bu iki ayrıntıyı bağımlılık ekseninde buluşturur. Bu temas 17:42’nin varsayımsal arayıcılarını bağlamdaki çağrılanlarla özdeşleştirmez; düşmanca erişim ihtimali de açık kalır.

Arayış imgesi, kök ailesinin başka bir kullanımından olası sınır aşımı basıncı da alır. Bu aile haddi aşma, haksızlık, doğru olandan yanlışa sapma ya da kibir çağrışımlarına açılır; 7:45’te Allah’ın yolunu eğri kılmaya çalışanları anlatan {ar:وَيَبْغُونَهَا عِوَجًا, tr:wa-yabghūnahā ʿiwajan, gloss:onu eğri kılmaya çalışırlar} özellikle yolun eğriltildiği somut imgeyi verir (7:45). Bu temas kök ailesi üzerinden kurulur: 7:45’teki fiil odaktaki {ar:لَّٱبْتَغَوْا۟, tr:la-ibtaghaw, gloss:elbette ararlardı} gibi VIII. kalıp değildir. Çoğul arayıcıların tek taht sahibi çevresinde yönelmesi böylece olası erişim rekabetini ve otoritenin dayanağının sarsılması gerilimini düşündürebilir; dayanak zayıflarsa güç ve saygınlık yitimi de bu ihtimale eklenir. Bu okuma mümkün bir gerilim düzeyinde kalır: maksatlı arayış yerini korur, ayetler saldırı ya da gerçek bir çatışma bildirmez. Adsız yol, bu özel bağlantıda çoğul arayanlarla tek makam arasındaki sınırı ve rekabet ihtimalinin yönelebileceği geçidi kurar.

17:59 ve 17:60 insan tepkisine ayrı ama ilişkili ayrıntılar sunar. 17:59’da önceki toplulukların işaretleri yalanlaması ve Semud’un dişi devesine haksızlık etmesi, reddedişi somutlaştırır (17:59). 17:60’ta gösterilen rüya ile Kur’an’da lanetlenen ağaç insanlara yönelik sınama imgelerini verir; uyarıların bazılarını daha büyük bir azgınlığa artırması bu tepkinin nasıl ağırlaşabildiğini gösterir (17:60). Birlikte, reddedişten artan aşırılığa uzanan insan tepkisine dair bir ayna kurarlar. Benzerlik bu tepki örüntüsündedir; aynı topluluk ya da olay iddiası taşımaz ve 17:60’ta daha sonra anılan kişilerin kimliğini belirlemez.

İnsan tepkisinden sonra yol imgesi dikey bir ölçeğe taşınır. {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} olağan güzergâh anlamını korurken, sözcüğün ayrı bir “aşağı bırakma ya da uzatma” kullanımı yukarıdan aşağıya uzanan hattı sağlar. Yüksek Arş imgesiyle 17:44’teki {ar:ٱلسَّمَٰوَٰتُ ٱلسَّبْعُ وَٱلْأَرْضُ, tr:as-samāwātu as-sabʿu wa-l-arḍu, gloss:yedi gök ve yer} gök-yer kutupları bu hattın üst ve alt yönünü belirginleştirir (17:44). {ar:ٱلْعَرْشِ, tr:al-ʿarsh, gloss:Arş} için ayrı bir örtülü barınak ya da gölgelik kullanımı da yukarıdaki kaynak imgesine örtü ve sığınak boyutunu katar. Ayrı sözlük açılımlarının bu bileşimi, yukarıdaki kaynaktan aşağıdaki alana uzanan bağımlı bir hat sezdirir. Bu bağlantı sözcükleri eş anlamlı kılmaz; odak cümlesindeki yöneliş yine Arş sahibinedir.

Dikey güzergâh imgesinin yanında 17:45, 17:46 ve 17:48 erişimin kesildiği başka bir hareket dizisi kurar. 17:45’te Kur’an okunurken elçiyle ahirete inanmayanlar arasına {ar:حِجَابًا مَّسْتُورًا, tr:ḥijāban mastūran, gloss:örtülü bir engel} konur; bu engel erişimi örter (17:45). 17:46’da Rabbini Kur’an’da yalnız andığında onların arkalarını dönüp uzaklaşması, bu kesintiye bedensel bir yöneliş ekler (17:46). 17:48’de kurulan benzetmeler sapma ve yol bulmaya güç yetirememe ile sonuçlanır (17:48). Odaktaki {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} adı burada da geçtiğinden, iki pasaj arasında arayış ile erişememe karşıtlığı belirir: odaktaki varsayımsal varlıklar yol arar, burada benzetme kuranlar sapmış ve yol bulamamış görünür. Bu karşılaştırma yol imgesinin yönleriyle sınırlıdır; grupların ya da yolların özdeşliğini ileri sürmez.

Fâtiha 1:6’daki {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭa al-mustaqīm, gloss:bizi dosdoğru yola ilet} duası okuyucunun kendi rehberlik isteğini yol bulamama imgesinin yanına getirir (1:6). 1:7’de nimet verilenler, öfkeye uğratılanlar ve sapanlar arasındaki ayrım, istenen yönün sonuçlarını belirginleştirir (1:7). Böylece okur, Allah’tan yardım ve yol isteyen biri olarak bağımlı yönelişin anlaşılır yanını kendi duasında tanır. Bu temas rehberlik ihtiyacında kalır: {ar:سَبِيلًۭا, tr:sabīlan, gloss:yol} ile {ar:ٱلصِّرَٰطَ, tr:aṣ-ṣirāṭa, gloss:dosdoğru yol} ayrı sözcük ve imgelerdir; Fâtiha’da anılan topluluklar da odaktaki varsayımsal varlıklarla özdeşleşmez.

</source_prose>
