# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:23**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.middle.claims.json`

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
- Refer to source paragraphs as `17:23 ¶N`.

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

`(17:23 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:23",
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
        "citation": "(17:23 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_23/17_23.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_23/17_23.middle.claims.json \
  --ayah-ref 17:23
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_23/17_23.prose.editorial.tr.md`

<source_prose>
## Hükmün Yönü

Ayet, önceki akışa {ar:وَ, tr:wa, gloss:ve} ile eklenir; bu bağlaç süreklilik kurar, cümle ise önceki uyarıyı açıklayan özel bir bağ kurmaz (17:22). {ar:قَضَىٰ, tr:qaḍā, gloss:hükme bağlamak} tamamlanmış fiil biçimiyle buyrukları karara bağlanmış, yerleşik yükümlülükler olarak sunar. Dâdın kalın tınısı bu yerleşiklik hissini hafifçe pekiştirebilir; hükmün bağlayıcılığı fiil biçimi ve cümle kuruluşundan gelir. Fiile nasihat anlamı veren veya onu isim biçiminde okuyan başka okuyuşlar da aktarılır; lafızları belirtilmediği için aralarındaki ayrıntı ve tercih açık kalır.

Buyruğun kaynağı {ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin} diye muhataba dönük biçimde adlandırılır. İkinci kişi eki hükmü kişisel bir ilişkiye bağlar; Rab adı sahiplik, buyruk yetkisi ve yönetim anlamlarını taşır. Anne baba ve iyilik buyruğunun hemen gelişi, bu olağan otorite anlamına besleyip yetiştirme yönünü de ekleyebilir. Böylece aile sorumluluğu kişisel ilahî hüküm içinde duyulur; bu yakınlık anne babanın muhatabı geçmişte yetiştirdiğine dair bir anlatı kurmaz.

Hükmün ilk içeriği, {ar:أَلَّا, tr:allā, gloss:ki ... etmeyesiniz} biçiminde bağlaçla olumsuzluğu birleştiren yan cümledir; ardından gelen fiil bu hükme bağımlıdır. {ar:تَعْبُدُوا, tr:taʿbudū, gloss:kulluk etmeniz} çoğul muzari ve mansup biçimiyle tamamlanmış bir olayı değil, muhataplar için süren kulluk yükümlülüğünü kurar. Olumsuzluğun ardından gelen {ar:إِلَّا, tr:illā, gloss:ancak} ve öne çıkarılmış mansup ayrık zamir {ar:إِيَّاهُ, tr:iyyāhu, gloss:yalnız O}, bu yükümlülüğün tek olumlu odağını belirler. Böylece ibadet ayrı bir buyrukla yan yana duran yasak değil, aynı hükmün ilk içeriği olarak yalnız Allah'a yönelir.

Bu kulluk yönelişinin yanında, aynı kelime ailesinin ayrı bir kullanımında çokça geçilerek düzleşmiş, yürünebilir hâle gelmiş bir yol da bulunur. {ar:تَعْبُدُوا, tr:taʿbudū, gloss:kulluk etmeniz} ile {ar:إِلَّا إِيَّاهُ, tr:illā iyyāhu, gloss:O'ndan başkasına değil} arasındaki temas, yolu tek hedefe doğru tekrar tekrar izlenen bir yöneliş gibi duyurabilir. Bu mecazi yol çağrışımı kulluğun tek hedefe doğru sürmesini belirginleştirir; ayet gerçek bir güzergâh anlatmaz.

Bağlayıcı vav, anne babaya iyiliği de aynı {ar:قَضَىٰ, tr:qaḍā, gloss:hükme bağlamak} çatısına alır. Kulluk ile aileye iyilik tek hüküm içinde buluşur, ama ayrı görevler olarak kalır. {ar:بِالْوَالِدَيْنِ, tr:bi-l-wālidayni, gloss:anne babaya} öbeğindeki bā iyiliğin alıcısını gösterir; {ar:الْوَالِدَيْنِ, tr:al-wālidayni, gloss:anne baba} ise doğum ve köken anlamlı aileden gelen etkin ortaç biçiminin ikilidir. Emir, genel olarak yaşlılara veya bakım verenlere değil, kişinin kendi anne baba çiftine yönelir; sözcüğün biçimi onların geçmişte ne yaptığını anlatmaz. {ar:إِحْسَانًا, tr:iḥsānan, gloss:iyilik etme} açık bir eylem fiili olmadan gelen mansup mastardır ve iyilik etme yükünü adlandırır. İhsanın kimi kullanımlarındaki denk karşılığı aşan etkin yarar tonu, burada görevi incitmemenin ötesine taşır. Bu, iyiliğin miktarı ölçülmüş bir fazlalığını buyurmaz ve adaleti askıya almaz.

## Yaşlılık Eşiği

Genel buyruk {ar:إِمَّا, tr:immā, gloss:eğer} ile belirli bir koşula iner. Vurgulu {ar:يَبْلُغَنَّ, tr:yablughanna, gloss:ulaşırsa} fiili standart biçimde tekildir ve kendisinden sonra gelen {ar:أَحَدُهُمَا, tr:aḥaduhumā, gloss:ikisinden biri} öznesiyle tamamlanır: okur önce yaşlanmaya erişme olayını, sonra kaç ebeveynin söz konusu olduğunu duyar. Bu fiille ikil uyum kuran başka bir okuyuş da aktarılır; lafzı verilmediğinden biçimleri karşılaştırmak ya da birini seçmek mümkün değildir.

Fiilin nesnesi {ar:الْكِبَرَ, tr:al-kibara, gloss:ileri yaşlılık}, erişilen hayat evresidir. Kelime ailesindeki büyüklük ve derece anlamları bu eşiğe ağırlık katar; burada konu kibir, rütbe ya da ahlaki değer değil, ömrün ulaşılan evresidir. Ailenin “ağır gelme” yönündeki ayrı kullanımı da, muhataba yakınlık ve ardından gelen söz özdenetimiyle birlikte, bakımın zor yanını hafifçe duyurabilir. Bu bağlamsal tını ebeveyni yük diye tanımlamaz; cümledeki sözcük yaşlılığı adlandırır.

{ar:عِندَكَ, tr:ʿindaka, gloss:senin yanında} yer veya zaman bakımından yakınlığı muhatabın alanına taşır. İkinci kişi eki, anne babanın muhatabın yanında yaşlanmasını sorumluluğun somut tetikleyicisi yapar; ifade bu yakınlığı kurar, ev düzeni veya sahiplik ilişkisi tarif etmez. {ar:أَحَدُهُمَا, tr:aḥaduhumā, gloss:ikisinden biri} ikilinin tek üyesini aynı çifte bağlı olarak seçer. Tek başına eşsiz bir varlığı çağrıştırabilen kullanım burada çiftin üyelerinden biriyle sınırlıdır; ilahî eşsizlik anlamı bu koşulun parçası değildir. {ar:أَوْ, tr:aw, gloss:ya da} ile gelen {ar:كِلَاهُمَا, tr:kilāhumā, gloss:ikisinin ikisi de} anne babanın ikisini kapsar. Koşulun cevabını açan {ar:فَلَا تَقُلْ, tr:fa-lā taqul, gloss:öyleyse deme} her iki duruma da uygulanır: yükümlülük, ebeveynlerden biri yaşlandığında da ikisi birlikte yaşlandığında da işler.

## Hitabın Ölçüsü

Koşul gerçekleştiğinde ilk sınır {ar:لَا تَقُلْ, tr:lā taqul, gloss:deme} buyruğudur: anne babaya {ar:أُفٍّ, tr:uffin, gloss:kısa hoşnutsuzluk ünlemi} denmemelidir. {ar:لَهُمَا, tr:lahumā, gloss:onlara} ikil yönelmesi anne babayı sesin doğrudan alıcısı yapar; odak, onlar hakkındaki konuşmada değil, onlara yöneltilen hitaptadır. Uff hoşnutsuzluğun en küçük açık sözlü işaretidir; ikizleşmiş f'si ve sıkışık tınısı bu tepkiyi kısa bir dışavurumda toplar. Yasak bu söylenmiş işareti hedefler; içte kalan duyguyu, her sesi veya maddi bir rahatsızlık nesnesini değil. Okuyuşlarda ünlemin dilbilgisel sınıflandırması ve tenvini değişebilse de aktarılan anlamı korunur; belirtilmeyen biçimler arasında seçim yapılmaz. Oğulun aynı sesi anne babasına yönelttiği sahne onu yüz yüze reddin işareti olarak somutlaştırır (46:17). İki sahnenin koşulları ayrıdır; 46:17 öfkenin nedenini açıklar, odak ayet açıklamaz.

İkinci vav, kısa hoşnutsuzluk işaretinden daha sert bir söz edimine geçer: {ar:لَا تَنْهَرْهُمَا, tr:lā tanharhumā, gloss:onları azarlama}. {ar:تَنْهَرْهُمَا, tr:tanharhumā, gloss:sertçe azarlamak} anne babaya doğrudan yöneltilen sert azarlama ve engellemeyi anlatır. Bu, düzeltme veya öğüdün tümünü değil, daha dar bir yüz yüze çıkışı adlandırır. İki yasak ayrı hitapları sınırlar; sıraları aralarında önem derecesi kurmaz.

Ardından gelen {ar:وَقُلْ, tr:wa-qul, gloss:ve söyle} olumlu bir hitap ister. Yasaklanan {ar:تَقُلْ, tr:taqul, gloss:söyleme}, emredilen {ar:قُلْ, tr:qul, gloss:söyle} ve onun ardından gelen {ar:قَوْلًا, tr:qawlan, gloss:söz}, aynı Arapça kelime ailesinde söyleme edimini yasaktan emre, oradan söylenen şeyin adına taşır. Buyruğun kapanışındaki {ar:لَهُمَا, tr:lahumā, gloss:onlara}, anne babayı bu olumlu sözün de alıcısı yapar; cevap sessizlik değil, onlara gerçekten yöneltilen bir hitaptır.

{ar:قَوْلًا, tr:qawlan, gloss:söz} mansup mastarı belirli bir cümleyi seçmez; onunla biçimce uyuşan {ar:كَرِيمًا, tr:karīman, gloss:onurlu} sıfatı sözün niteliğini belirler. Değer verme ve başkasını onurlandırma tonu, hitabı tarafsız ya da yalnızca hakaret etmeyen sözden daha ileri taşır. {ar:إِحْسَانًا, tr:iḥsānan, gloss:iyilik etme} ile aynı anlamda değildir; anne babaya yöneltilen söz, daha geniş iyilik yükünün konuşmadaki uygulamasıdır. Emir onur veren niteliği belirlerken söylenecek kalıbı açık bırakır ve maddi bir armağan istemez. Ses dizisi de kısa {ar:أُفٍّ, tr:uffin, gloss:hoşnutsuzluk ünlemi}nden sert {ar:تَنْهَرْهُمَا, tr:tanharhumā, gloss:azarlama}ya, oradan daha dolu {ar:قَوْلًا كَرِيمًا, tr:qawlan karīman, gloss:onurlu ve değer veren söz}e ilerler. Bu işitsel yay hitabın niteliğini duyurur; tek başına sözlük anlamını veya konuşanın iç hâlini kanıtlamaz. İki son sözcüğün tenvini kapanışa hafif bir ritim verir; ilerideki akarsu benzetmesi ise bu ses dizisinden değil, ayrı bir kelime kullanımıyla maddi ölçü ayetlerinin buluşmasından doğar.

## Bakımın Zamanı

Yaşlılık buyruğunun ardından gelen dua, anne babanın geçmiş emeğini anımsatır: yetiştirme anlamındaki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} ve çocukluk evresini bildiren {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} geçmişteki bakımı görünür kılar (17:24). Böylece {ar:يَبْلُغَنَّ, tr:yablughanna, gloss:ulaşırsa} ile işaretlenen ileri yaş, bir zamanlar çocuğu büyüten anne babanın yanına yerleşir; bakımın yönü hayat içinde olası bir karşılık bulur. Bu okuma iki dönemin ihtiyaçlarını eşitlemez veya tam rol değişimi ileri sürmez; minnettarlık ile merhamet birlikte açıklama olarak kalır.

Bu bakımın bedensel karşılığı, anne babaya doğru alçalan koruyucu duruştur. {ar:وَاخْفِضْ لَهُمَا, tr:wa-khfiḍ lahumā, gloss:ikisi için alçalt} buyruğunda {ar:جَنَاحَ, tr:janāḥ, gloss:kanat} yan, kol ve örtü imgesini, {ar:الذُّلِّ, tr:al-dhull, gloss:yumuşak alçak gönüllülük} ise aşağılanmayı değil, gönüllü şefkati taşır (17:24). {ar:ارْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} duası bu duruşun yönünü merhamet olarak adlandırır ve onu Allah'tan ister; tek bir güdüye indirgemez. Sert hitaba karşılık bedensel yakınlık belirirken, {ar:قَوْلًا كَرِيمًا, tr:qawlan karīman, gloss:onurlu söz} aynı bakımın sözlü biçimini gösterir; dua ve beden imgesi konuşma buyruğunu tamamlar, onunla özdeşleşmez.

{ar:كِلَاهُمَا, tr:kilāhumā, gloss:ikisinin ikisi de} anne babanın ikisini kapsayan olağan anlamını korurken, biçimce uzak bir kullanım rüzgârdan korunan ve gemilerin sığındığı limanı çağrıştırır. Bu uzak mekân koluna iki ayrıntı katkı verir: koruyucu kanat gibi alçalan beden bir siper imgesi sağlar (17:24), anne babanın muhatabın yanında bulunması da {ar:عِندَكَ, tr:ʿindaka, gloss:senin yanında} ile bakım alanını belirler. Birlikte, çocuğun yakını sığınak gibi duyulabilir. Liman çağrışımı bu belirli bağlantıyı aydınlatır; ayetin anne baba çifti hakkındaki olağan anlamının yerini almaz ve gerçek bir gemi sahnesi kurmaz.

Ebeveyn önündeki alçalış, daha geniş bir beden ölçüsü içinde de okunabilir: yeryüzünde böbürlenerek yürümemek, yeri delemediğini ve boyca dağlara erişemediğini bilmek tevazuyu genel insanlık sınırı olarak resmeder (17:37). {ar:وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī l-arḍi maraḥan, gloss:yeryüzünde böbürlenerek yürüme} yürüyüşe, {ar:لَنْ تَخْرِقَ الْأَرْضَ وَلَنْ تَبْلُغَ الْجِبَالَ طُولًا, tr:lan takhriqa l-arḍa wa-lan tablugha l-jibāla ṭūlan, gloss:yeri delemez ve dağlara boyca erişemezsin} ise erişilemeyen yer ve dağ ölçeğine sınır koyar. Bu, ebeveyn ilişkisine özgü bir buyruk değil; aile içindeki alçak duruşun içinde bulunduğu daha geniş tevazu ölçüsüdür.

Ulaşma fiili ebeveyn-çocuk bağındaki ayrı hayat eşiklerini görünür kılar. Annenin hamilelik ve doğum sıkıntısından sonra çocuk olgunluğa ve kırk yaşına erişir, anne babasına şükreder ve kendi çocukları için iyilik diler (46:15). Oradaki {ar:يَبْلُغَ, tr:yablugha, gloss:ulaşması} ile odaktaki yaşlılığa erişme aynı fiil ailesindendir; {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} bakım çizgisinin çocukluk ucunu ekler. Kırk yaş anne babanın ileri yaşıyla aynı zaman noktası değil, aynı ilişkideki başka bir eştir. İki yetim oğlanın hazinesi, babalarının salihliği nedeniyle olgunluklarına dek bir duvar altında korunur (18:82); bu görüntü bakımın babadan çocuklara yönünü gösterir ve yaşlı babaya çocuğun hizmetinden ayrı kalır.

Başka bir geç yaş sahnesinde ihtiyar konuşan, kısır eşiyle birlikte bir oğul diler (19:8). Bu beden sınırı yaşlılık ile çocuk arzusunu kendi sahnesinde buluşturur; 17:23'teki bakım buyruğunu doğum mucizesine dönüştürmez veya her yaşlıyı bağımlı saymaz. Ayrı ihtiyaçlar içinden odak ayete dönen bağ, ebeveyn-çocuk ilişkisinin hayat boyunca farklı eşiklerden geçmesidir.

Yetiştirme duasındaki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} ile hükmün kaynağı {ar:رَبُّكَ, tr:rabbuka, gloss:senin Rabbin} arasındaki ses yakınlığı, yetiştirme sahnesinin bakım tonunu Rab adına taşıyabilir (17:24). Böylece adın olağan otorite anlamına yerel bir yetiştirme çağrışımı eklenir. Biçimler ayrı köklerden geldiğinden bu ses ilişkisi etimolojik değildir; ayrıca 17:23 anne babanın muhatabı nasıl yetiştirdiğine dair bir yaşam öyküsü anlatmaz.

## İyiliğin Çevresi

Yalnız Allah'a kulluk, anne babaya iyilik ve insanlara güzel söz bir antlaşmada yan yana gelir (2:83). İyilik halkası akraba, yetim, yoksul ve komşuya doğru genişler (4:36); anne babaya iyi davranma da çocukları yoksulluk korkusuyla öldürmeme buyruğunun yanında yer alır (6:151). Bu bağlamlar kulluğun yakın ilişkilerde davranışa dönüştüğünü ve bakımın aile dışına da uzandığını gösterir; odaktaki ihsan yine özellikle anne babaya yöneltilmiş yükümlülük olarak kalır.

Hükmün Allah'a ait olduğu ve yalnız O'na kulluk edildiği savı, {ar:قَضَىٰ, tr:qaḍā, gloss:hükme bağlamak} fiilinin karar verici gücünü belirginleştirir (12:40); buradaki otorite insanlar arası bir yargılama değildir. Anne babaya iyilik, onların ortak koşmaya çağıran baskısına uymama sınırıyla birlikte sürer (29:8). Bu karşılaşma, ebeveyne ihsanın ilahî kulluğa bağlılığını açar; her isteği aynı ölçüde buyruk kılmaz.

Fâtiha'daki {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyāka naʿbudu wa-iyyāka nastaʿīn, gloss:Yalnız Sana kulluk eder ve yalnız Senden yardım isteriz} kullukla yardım arayışını aynı Allah'a yöneltir (1:5). Bu eşlik, ebeveyn sorumluluğunu kendine yeterli güçten değil, Allah'a kulluk edip O'ndan yardım isteyen bir duruştan düşündürür; yardım duası özellikle ebeveyn bakımı için kurulmuş değildir. Anne baba için merhamet duası ile kulluk buyruğunun kapanıştaki vurgusu ayrı bağlamlarında kalır (17:24, 17:39).

Onurlu hitabın değeri farklı muhataplarda da belirir: insanlara güzel söz buyruğu (2:83) ve Musa ile Harun'un Firavun'la yumuşak konuşmasının istenmesi (20:44), nitelikli dilin ayrı ilişki ve güç koşullarında da yerini gösterir; söz kalıpları aynı değildir. Soy yerine takvayı saygınlığın ölçüsü yapan buyruk (49:13), {ar:كَرِيمًا, tr:karīman, gloss:onur ve değer taşıyan} niteliğini miras alınmış mevki değil ahlaki dikkat yönünde duyurur. Bu bağlamlar etik yönü aydınlatır; toplumsal saygınlık ayeti karīman'ın sözlük tanımı veya ebeveyne hitap için tek başına bir ölçüt değildir.

İstekte bulunan kişiyi azarlamama buyruğu bu dil ölçüsünü aile dışındaki doğrudan karşılaşmaya taşır (93:10). İstekte bulunan anne babayla aynı ilişki değildir; ortak nokta, yüz yüze azarın karşılaşmayı kapatabilmesidir (17:23, 93:10). Azarlamamak, maddi yardım henüz sunulmamışken de isteyen kişinin haysiyetini ve kabulünü koruyabilir. Bu söz talebin karşılanacağını vaat etmez, maddi yardımın yerini tutmaz veya yardımın gecikeceğini varsaymaz. Ebeveyn iyiliğinin yanındaki güzel söz ve geniş bakım halkası, bu saygın hitabın aile dışındaki ilişkisel değerini de gösterir (2:83, 4:36).

## Sözün İç Sınırı

Dışa yönelen hitabın yanında iç yönelişin de değerlendirme ufkunda olduğu bildirilir: Rab insanların içindekini en iyi bilir (17:25). {ar:رَبُّكُمْ أَعْلَمُ بِمَا فِي نُفُوسِكُمْ, tr:rabbukum aʿlamu bimā fī nufūsikum, gloss:Rabbiniz içinizdekini en iyi bilir} ifadesi, {ar:أُفٍّ, tr:uffin, gloss:hoşnutsuzluk ünlemi} gibi duyulur sözün yanı sıra düşünce ve iç ürpertiyi de hesaba katar; duygu böylece değerlendirme ufkuna girer, fakat söylenmiş sözle özdeşleşmez. {ar:صَالِحِينَ, tr:ṣāliḥīn, gloss:düzgün ve yapıcı olanlar} yapıcı bir doğrultuyu, {ar:الْأَوَّابِينَ, tr:al-awwābīn, gloss:tekrar tekrar dönenler} ise yeniden yönelmeyi belirtir. {ar:غَفُورًا, tr:ghafūran, gloss:çok bağışlayan} bağışlaması yanlışın ardından dönüş ve onarıma imkân verir; hangi iç durumun yeterli olduğu ayrıca belirlenmez. Bu güvence genel bir anlam taşır; anne babaya söylenen sözü onarma yönünde okumak bağlamsal bir çıkarımdır. Her iki okumada da bağışlanma sert hitaba izin vermez ve dışa dönük onurlu sözün yerini yalnız niyete bırakmaz.

Bilgiye dayanmayan yargı için ayrı bir sınır çizilir: kişinin bilmediğinin peşine düşmemesi istenir (17:36). {ar:وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِ عِلْمٌ, tr:wa-lā taqfu mā laysa laka bihi ʿilm, gloss:hakkında bilgin olmayan şeyin peşine düşme} kanıtsız iz sürmenin kesin yargıya dönüşmesini engeller. {ar:السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ, tr:as-samʿ wa-l-baṣar wa-l-fuʾād, gloss:işitme görme ve yürek} işitme, görme ve yüreği hesap verecek kavrayış alanları olarak bir araya getirir. Yüreğin iç harareti, sıkıntının azara dönüşmesini mümkün kılan bir iç süreç gibi duyulabilir; bu imge belirli bir konuşanın duygusunu teşhis etmez. {ar:مَسْؤُولًا, tr:masʾūlan, gloss:hesaba çekilir} bu algı ve kavrayışın hesabını vurgular. Ayetin genel tanıklık ve inanç anlamı sürerken, bunu aile konuşmasına uygulamak bağlamsal bir okumadır; bu yüzden her azarlama bilgisiz sayılmaz. Güçlü yargı kanıt ve uygun tonla birlikte taşınmalıdır.

## Ölçü ve Emanet

İyilik maddi cömertlikle de ilişki kurar; sonraki buyruklar bu ilişkinin sınırlarını başka muhataplar üzerinden açar. Akrabaya hakkını vermek söylenir (17:26). Maddi isteğe karşılık veremeyip geri dönmek gerektiğinde ise kolay, erişilebilir bir sözle karşılık verme imkânı tanınır (17:28): {ar:قَوْلًا مَيْسُورًا, tr:qawlan maysūran, gloss:kolay ve erişilebilir söz}. İstekte bulunanın anne baba olduğu belirtilmez. Maysuranın kolaylık niteliği, {ar:قَوْلًا كَرِيمًا, tr:qawlan karīman, gloss:onurlu söz} içindeki onur niteliğiyle aynı değildir; maddi yardım verilemediğinde de saygın bir karşılık mümkündür.

Harcamaya ilişkin sonraki ölçüler elin iki ucunu gösterir: boyna bağlanmış el verişi işlemez kılarken, bütünüyle açılan el sınır tanımayan harcamayı resmeder (17:29). El imgeleri bakım verenin bedenini değil, vermenin iki uçtaki biçimini gösterir. Allah'ın rızkı açıp daraltması imkânın ölçüsünü getirir (17:30); doğru tartı da cimrilikle insanı tüketen aşırılık arasındaki adil dengeyi kurar (17:35). Bu ölçüler cömertliği gerçek imkân içinde kalibre eder; böylece sürdürülebilir verme ebeveyne ihsanı asgari adalete indirgemez, ihsan da imkânı tüketen harcama buyruğuna dönüşmez.

Maddi ölçüler, {ar:تَنْهَرْهُمَا, tr:tanharhumā, gloss:sertçe azarlamak} için uzak bir kelime kullanımını harekete geçirir; odaktaki fiilin olağan anlamı sert sözlü azarlamadır. Ayrı kullanımda bol su taşıyan, toprağı yaran akarsu yatağı belirir. Bu imgeye harcama ayetlerinin her biri ayrı katkı verir: kapalı ve bütünüyle açılan el karşıtlığı ölçüsüz akışı, rızkın açılıp daraltılması kapasiteyi, doğru tartı ise akışın denge ihtiyacını görünür kılar (17:29, 17:30, 17:35). Böylece denetimsiz söz baskısı toprağı aşındıran bir sel gibi düşünülebilir. Fiilin başka uzak kullanımları açma, genişletme ve açılmış yerden kan akıtmayı da içerir; bunlar kelime ailesinin ayrı maddi dallarıdır. Akarsu yatağı, açılma ve kan salma anlamları bu uzak kolun keşifsel çağrışımlarıdır; odaktaki kullanımın doğrudan anlamı sert azarlamadır.

{ar:كَرِيمًا, tr:karīman, gloss:onur veren} ise ayrı bir uzak kullanım kolunda yağmur getiren bulut, verimli toprak ve gür bitki imgelerini toplar. Bulut yağmuru taşır, verimli toprak onu alır, gür bitki yetişen hayatı görünür kılar; bu dizi aşındırıcı akıştan farklı bir besleme imgesi sunar. Harcama ayetlerinin ölçüsü, bu karşıtlık içinde onurlu sözü denetimli ve besleyici yönde düşündürür (17:29, 17:30, 17:35). İki kelime kolunun katkısı bu belirli okumada ayrıdır: biri taşkın sözün aşındırmasını, diğeri onurlu hitabın besleyici niteliğini aydınlatır; konuşmanın hacmi için bir kural koymaz.

Bağımlı kuşaklara ilişkin maliyet kaygısı daha keskin bir sınama bulur. Anne baba ile çocukları adlandıran sözler aynı doğum ilişkili kelime ailesine uzanır; odakta ebeveynler anılırken çocukları öldürmeme buyruğu genç kuşağa döner (17:31). {ar:الْوَالِدَيْنِ, tr:al-wālidayni, gloss:anne baba} ve {ar:أَوْلَادَكُمْ, tr:awlādakum, gloss:çocuklarınız} kapsamı sayı, cinsiyet veya yaş bakımından daraltmaz. Yoksulluk korkusuyla öldürmeme buyruğu ve Allah'ın çocuklara rızık vereceği sözü, geçim endişesini doğrudan karşılar: {ar:خَشْيَةَ إِمْلَاقٍ, tr:khashyata imlāq, gloss:yoksulluk korkusuyla} ve {ar:نَرْزُقُهُمْ, tr:narzuquhum, gloss:onlara rızık veririz}. Bu korku yaşlı ebeveynin bakımını da maliyet gibi duyurabilir; ancak {ar:الْكِبَرَ, tr:al-kibara, gloss:ileri yaşlılık} yaş evresini adlandırır, yükü değil, ayrıca 17:23 ebeveynlere benzer bir maddi tahsis vaadi vermez. İki hüküm özdeşleşmeden, maliyet yüzünden bağımlı bir kuşağı gözden çıkarmama yönünde ihtiyatlı bir ortak okuma açar.

Olgunluğa erişme eşiği yetim malını koruma buyruğunda yeniden belirir: odaktaki {ar:يَبْلُغَنَّ, tr:yablughanna, gloss:ulaşırsa} ile aynı fiil, yetimin olgun gücüne erişmesine dek gözetimi sürdürür (17:34). {ar:الْيَتِيمِ, tr:al-yatīmi, gloss:yetim} kırılgan ve malı başkasının gözetiminde olan kişidir; {ar:وَلَا تَقْرَبُوا مَالَ الْيَتِيمِ إِلَّا بِالَّتِي هِيَ أَحْسَنُ, tr:wa-lā taqrabū māla l-yatīmi illā bi-llatī hiya aḥsan, gloss:yetim malına en iyi yol dışında yaklaşmayın} malı olgunluk eşiğine dek en iyi yolla idare etmeyi ister. Ardından ahdi yerine getirme ve hesabının sorulacağını bilme çağrısı gelir: {ar:وَأَوْفُوا بِالْعَهْدِ إِنَّ الْعَهْدَ كَانَ مَسْؤُولًا, tr:wa-awfū bi-l-ʿahdi inna l-ʿahda kāna masʾūlā, gloss:ahdi yerine getirin ve hesabının sorulacağını bilin}. Ahid sözcüğünün yinelenmesi gözetimin hesabını öne çıkarır: yetim malını olgunluğa dek idare etmek mülkiyet değil, geçici ve teslimle tamamlanan emanettir. Yaşlı ebeveyne bakım ile yetim malının korunması ayrı ilişki ve hukukî eşiklerdir; ortak olan, kırılganlık karşısındaki geçici gücün hesap verebilir kullanılmasıdır.

Ev içindeki yakınlığın otorite sınırı, muhatabın yanını bildiren {ar:عِندَكَ, tr:ʿindaka, gloss:senin yanında} ile Rab katını bildiren {ar:عِندَ رَبِّكَ, tr:ʿinda rabbika, gloss:Rabbin katında} arasındaki benzerlikte belirir (17:38). İlki çocuğun bakım alanını, ikincisi davranışın ilahî değerlendirmesini gösterir. Aynı ayetteki kötü ve hoş görülmeyen davranış, {ar:قَوْلًا كَرِيمًا, tr:qawlan karīman, gloss:onurlu söz} ile daha geniş bir karşıtlık kurabilir; bu bağlantı 17:38'in ebeveyne hitabı adıyla kötü davranış diye nitelemesi değildir. 17:38 ile 17:39'un buyruk dizisini birlikte çerçevelediği okumasında, 17:39 bu hükümleri hikmet olarak anar ve Allah'la birlikte başka bir ilah edinmeme yasağıyla tevhid temasına döner (17:38, 17:39). Ebeveyne bakım bu hikmet dizisindeki hükümlerden biridir; aile içindeki pratik güç daha yüksek bir otorite altında hesap verebilir kalır.

</source_prose>
