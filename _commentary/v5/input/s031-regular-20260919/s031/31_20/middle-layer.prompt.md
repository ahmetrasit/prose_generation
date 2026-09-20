# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **31:20**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.middle.claims.json`

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
- Refer to source paragraphs as `31:20 ¶N`.

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

`(31:20 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "31:20",
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
        "citation": "(31:20 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s031-regular-20260919/s031/31_20/31_20.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s031-regular-20260919/s031/31_20/31_20.middle.claims.json \
  --ayah-ref 31:20
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s031-regular-20260919/s031/31_20/31_20.prose.editorial.tr.md`

<source_prose>
## Görmeye çağrılan önerme

Âyet, {ar:أَلَمْ, tr:ʾa-lam, gloss:görmediniz mi} ve {ar:تَرَوْا۟, tr:taraw, gloss:görürsünüz} biçimleriyle muhatapların önünde görülebilir bir delil bulunduğunu varsayar ve onları bunu tanımaya, ikrar etmeye çağırır; böylece soru sıradan bir bilgi sorusu olmaktan çıkar. Cezm kipindeki ikinci çoğul görme fiili bakma yükünü tek kişiye değil topluluğa verir. Bu ortak sesleniş, sûrenin kozmik kanıtı birlikte görmeye yönelten yinelenen söyleyişiyle uyumludur. Görme fiili {ar:أَنَّ, tr:ʾanna, gloss:şu gerçeği} ile bir önermenin içeriğine bağlandığında da çıplak bakıştan tanımaya ve hükme varmaya doğru genişler.

Görülecek önerme, Allah’ın evreni insanların yararına hizmete yöneltip nimetlerini ulaştırdığı bütünlüklü bir eylemdir; dağınık olgular toplamı değildir. {ar:أَنَّ, tr:ʾanna, gloss:şu gerçeği} yapısındaki {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} açıkça mansup özne olarak yer alır; nimeti kimin verdiğini okurun çıkarsamasına bırakmaz. Aynı ad, ileride tartışmanın konusu olarak yeniden duyulacağı için iki uç arasında bir gerilim kurar. Allah adının {ar:سَخَّرَ, tr:sakhkhara, gloss:hizmete yöneltti} ve {ar:أَسْبَغَ, tr:ʾasbagha, gloss:bolca ulaştırdı} fiillerine yüklediği kulluk ve sığınma ihtiyacı, etimoloji iddiası olmaksızın önermenin sesini belirler.

## Kozmik hizmetin kapsamı

Bu önermedeki {ar:سَخَّرَ, tr:sakhkhara, gloss:hizmete yöneltti}, geçmişte tamamlanmış biçimiyle gerçekleşmiş bir ilahî eylemi sunan II. kalıp fiilidir: yaratılmış olanı yalnız yönetmekten daha güçlü biçimde belirli bir işe sevk eder. Gökleri ve yeri insan yararına bağlayan söz, tek başına güç gösterisinden çok yinelenen kozmik nimet söyleyişine katılır. Ayrı bir yarar kaydı olan {ar:لَكُمْ, tr:lakum, gloss:sizin için} insanları bu eylemin faili değil yararlanıcısı yapar; kozmosu düzene koyan özne nimet veren Allah’tır. Hizmet ve yarar ilişkisi evreni edilgin bir kaynaktan insan yararına yönelmiş bir çevreye dönüştürür; bu dönüşüm mülkiyeti insana vermez. Fiildeki güç asimetrisi ve kimi kullanımlarında hissedilen zorlama kuvveti, başkasını karşılıksız hizmete zorlama ile sunulan hizmet arasındaki ayrımı düşündüren ihtiyatlı bir sorumluluk gölgesi taşır; fiilin yerel anlamı yine alay değildir. Bu çağrışım, imkânı alanın onu nasıl kullanacağı sorusunu açar; âyet insan emeği sahnesi kurmaz.

Hizmete yöneltilen kapsam, göklerin ve yerin adlarıyla sınırlı kalmaz. İlk {ar:مَا, tr:mā, gloss:ne varsa} göklerin kendisini değil, göklerin içindeki her şeyi; yinelenen ikinci {ar:مَا, tr:mā, gloss:ne varsa} de yeryüzünün içindekileri kapsar. İki kez gelen {ar:فِى, tr:fī, gloss:içinde}, bu içeriklerin bulunduğu alanları paralel kaplar gibi kurar; ikinci öbeğin başındaki {ar:وَ, tr:wa, gloss:ve}, yerdekileri ilk nesneye eklenmiş bir dipnot değil, aynı fiilin eş kapsamlı ikinci nesnesi yapar. Belirli ve çoğul {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} üstteki katmanlı, yüksek alanı; belirli fakat tekil {ar:ٱلْأَرْضِ, tr:al-ʾarḍi, gloss:yeryüzü} aşağıdaki somut ve yaşanan zemini karşılar. Böylece iki kutuplu bütünlük asimetrik çizilir: yukarıda katmanlar, aşağıda tek bir yaşama alanı.

Bu {ar:سَخَّرَ, tr:sakhkhara, gloss:hizmete yöneltti} yararı, mülkiyetin insanlara devredildiği anlamına gelmez. Yeryüzü ve geminin kullanıma açılıp göğün tutulmuş gösterilmesi yararlanmanın sınırını duyurur (22:65); deniz, gemilerin yol alışı, rızık arayışı ve şükürle birlikte anılır (45:12); bineğe binen kişiye de nimeti anıp kendi başına yönetemediğini söylemesi öğretilir (43:13). Bu ayrı sahneler kullanım imkânını verene bağlılık içinde düşündürür (22:65, 45:12, 43:13). Yerde böbürlenmenin sınırlanması (31:18), yaratma ve mülkiyetin Allah’a döndürülmesiyle de yan yana durur (31:25, 31:26); yararlanma böylece egemenlikten çok sorumlu kullanıma açılır.

## Nimeti yaymak ve iki yüzü

Yararlanıcıların değişmediği bu düzenin ardından gelen {ar:وَ, tr:wa, gloss:ve}, {ar:أَسْبَغَ, tr:ʾasbagha, gloss:bolca ulaştırdı} fiilini aynı Allah öznesine bağlar: kozmik düzenleme ile nimet ulaştırma tek failin iki eylemidir. IV. kalıp fiili tam ölçüyle eriştirme ve tamamlayıp verme yönü taşır; {ar:نِعَمَهُۥ, tr:niʿamahu, gloss:onun nimetleri} nesnesiyle birleşince nimetin alıcısına dolu ölçüyle sunuluşu belirginleşir. Ayrı alıcı kaydı {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} ise bu doluluğu muhatapların üstüne ve çevresine, son sınırına dek yayılan bir alan gibi duyurur. Bu yerel tamamlanma, nimetin alıcı çevresinde tam ölçüyle yayılması imgesini güçlendirir; zırh giydirme sahnesi kurmaz ve bütün olası nimetlerin tek tek sayıldığını ileri sürmez. Kabul edilmiş bir ses varyantında ıslıklı tınıdan daha kalın tınıya geçiş yoğunluğu artırabilir; anlamın ağırlığını yine temel biçim taşır.

İki yarar kaydı aynı topluluğu sürdürür: {ar:لَكُمْ, tr:lakum, gloss:sizin için} nimetin kime yarar sağladığını söylerken {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} bolluğun o topluluğun üstüne ve çevresine yayıldığını duyurur. İki zamirdeki çoğul kişi eki ikinci eylemde yeni bir alıcı grubuna geçilmediğini gösterir. {ar:نِعَمَهُۥ, tr:niʿamahu, gloss:onun nimetleri} içindeki iyelik de nimetleri Allah’a ait tutar; insanlara ulaştırılmaları mülkiyet devri değildir. Ana yüzeydeki çoğul okuyuş birçok nimeti, kabul edilmiş tekil okuyuş ise kuşatıcı bir nimet bütününü duyurabilir; her iki okuma da kapsamı açık bırakır.

Bu kapsam yalnızca sayılabilir hediyelerle sınırlı kalmaz. Olağan “nimetler” anlamındaki {ar:نِعَمَهُۥ, tr:niʿamahu, gloss:nimetleri}, tamamlayıp yayan {ar:أَسْبَغَ, tr:ʾasbagha, gloss:bolca ulaştırdı} ve “üzerinize” alıcısı {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:üzerinize} ile buluştuğunda rahatlık, bolluk ve incelik içindeki yaşam koşullarını da düşündürür. Nimet böylece hayatı sürdürmeyi kolaylaştıran bir iyi oluş alanına genişler ve yaşanan iyilik şükre zemin olur; bu genişleme kelimenin olağan anlamını taşımaya devam eder, her alıcının hayatını aynı biçimde varsaymaz.

İki dişil tekil mansup ortaç, hâl işleviyle, ulaştırılan nimetleri eş düzeyli iki görünüşte sunar. {ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:görünür halde} yeni bir nesne değil, nimetin görünür bir hâlde oluşudur; onu {ar:وَ, tr:wa, gloss:ve} ile bağlanan {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli halde} aynı görevde karşılar. Görünürlük ve gizlilik ayrı olaylar değil, aynı nimet alanının iki niteliğidir. Görünür yüzün karşısındaki iç, karın ya da ast yüz imgesi bu içliği somutlaştırır; nimet sözcüğünü beden anatomisine indirmez. Gizli olan böylece anılan bir nimet yönüdür; bütün gizli nedenlerin insan için bütünüyle açıldığı sonucu çıkmaz.

{ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:görünür} ve {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} yüzleri, baştaki {ar:تَرَوْا۟, tr:taraw, gloss:görürsünüz} çağrısını görünen etkiden içteki koşullara, oradan yeniden görünen bütüne yönelen bir inceleme olarak somutlaştırır. Görme fiili böylece düşünüp hükme varma çağrışımını da taşır. İki yüzü birlikte çevirerek inceleme imgesi bu ilişkiye eşlik eder; biçimsel bir yan çağrışım olarak kalır, ortaçların sözlük anlamı değildir. Bu bakış, her nimetin zarar sakladığını değil, görünen etkinin hangi gizli desteklere dayanabileceğini araştırmayı önerir.

Görünür {ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:görünür} etki ile {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} kaynak arasındaki temas, gök adı ve nimet fiilinden bir geçiş imgesi de doğurur: {ar:ٱلسَّمَٰوَٰتِ, tr:al-samāwāti, gloss:gökler} geçirgen ara yüzü, {ar:أَسْبَغَ, tr:ʾasbagha, gloss:bolca ulaştırdı} ise nimetin görünür yaşama erişmesini düşündürür. Bu ilişki dar bir geçit ya da suyun bir yüzeye değmesi gibi malzeme benzetmeleriyle hayal edilebilir; bunlar erişme biçimini anlatır, gök sözcüğünü delik ya da açıklık yapmaz ve gökte fiziksel bir yapı ileri sürmez. Gök terimi ayrıca görünür belirtiyi okuyup görünmeyen niteliği sezme imgesine katılır; bu bağlantı fiziksel bir işaret ileri sürmez.

31:10–11’deki ayrı yaratılış sahnesi, görünen düzenin ardındaki destekleri göklerin kurulması, dağların yeryüzünün yalpalamasını önleyecek biçimde yerleştirilmesi, canlıların yayılması, yağmur ve bitki örtüsüyle gösterir (31:10, 31:11). Dağların sabitleyici rolü, göz önündeki düzeni görünmeyen işleyişle birlikte düşünmeye zemin verir (31:10). Sütunlara ilişkin söz, belirli görünmez sütunların varlığını bildirmekten çok sütunların görülmediğini anlatıyor da olabilir; bu nedenle buradan belirli bir gizli kolon sonucu çıkarılmaz (31:10). Rakip yaratılışın gösterilmesini isteyen {ar:أَرُونِي, tr:arūnī, gloss:bana gösterin} sözüyle odaktaki yalın {ar:تَرَوْا۟, tr:taraw, gloss:görürsünüz} arasındaki temas görme ve delil düzeyindedir: biri gösterme buyruğu, öteki görme çağrısıdır (31:11). Bu sahneler düzenin kanıtını açar; insanın bütün dayanaklara eriştiğini söylemez (31:10, 31:11).

Görünür ve gizli yüzlerin çevresindeki sözcük alanı başka bağlamlarda da ayrı yankılar bulur: açık ve gizli günahlardan sakındırma (6:120), görünür ve gizli adlarının yan yana gelişi (57:3), engelin iç ve dış yanı ile aranan ışık (57:13). Odaktaki {ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:görünür} ve {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} taşıyıcıların iç yüzü ve gizli yönü kadar tamamlanma, son sınıra dek uzanma, açığa çıkma ve arazide yüksekçe belirginleşen yüz olma ayrıntıları da bu yankılarda işitilir (6:120, 57:3, 57:13). Birlikte okunduklarında bu bağımsız temaslar nimet çiftini, tüm destekleyici işleyişi göz önünde olmayan ama görünür etkilerinden iz sürülebilen tamamlanmış bir kanıt alanı gibi duyurur (6:120, 57:3, 57:13). Bu sözlüksel temas nimetleri ilahî adlarla özdeşleştirmez; görünenden çıkarım yapılabilmesi de gizlinin tamamını bilinir kılmaz.

İç yönün dışarıda okunabilmesi ihtimali bu kez beden davranışlarında belirir. {ar:تُصَعِّرْ خَدَّكَ, tr:tuṣaʿʿir khaddaka, gloss:yanağını insanlardan çevirip bükme} buyruğu ve böbürlenerek yürüme (31:18), gizli üstünlük taslamasının yüzde ve adımda alabileceği biçimler olarak okunabilir: {ar:مُخْتَالٍۢ, tr:mukhtālin, gloss:böbürlenen} yürüyüşteki gösterişi, {ar:مَرَحًا, tr:maraḥan, gloss:taşkın sevinç} ölçüyü aşan hareketi öne çıkarır (31:18). {ar:وَٱغْضُضْ مِن صَوْتِكَ, tr:waghḍuḍ min ṣawtika, gloss:sesini alçalt} buyruğu ile seslerin en çirkini diye anılan eşek sesi de sesi kamusal bir yüzey yapar (31:19). Odaktaki {ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:açığa çıkan} saklı olanın görünürleşmesini, {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:içte saklı olan} ise iç yönü taşır; yüz, yürüyüş ve ses bu belirme fikrinin ayrı somut yüzeyleridir (31:18, 31:19). Bu sure içi okuma, 31:18–19’daki ölçülü yürüyüş ve alçak ses buyruklarını kendi görgü çağrıları olarak korur; ilişki her davranışın iç dünyayı açığa vurduğu evrensel bir kural değil, sûrenin açtığı bir gelişim okumasıdır (31:18, 31:19).

Başka bir bağlam aynı iç-dış ilişkisini bu kez bedensel emek üzerinden kurar. Çocuğun aldığı hayatın ardında {ar:حَمَلَتْهُ أُمُّهُۥ, tr:ḥamalathu ummuhu, gloss:annesi onu taşıdı} sözüyle anlatılan taşıma; {ar:وَهْنًا عَلَىٰ وَهْنٍۢ, tr:wahnān ʿalā wahnin, gloss:güçten düşme üstüne güçten düşme} diye yinelenen yorgunluk ve iki yıl içindeki {ar:وَفِصَالُهُۥ فِى عَامَيْنِ, tr:wa-fiṣāluhu fī ʿāmayn, gloss:sütten ayrılması iki yıl içindedir} süreci vardır (31:14). Görünür sonucun önünde uzun bir bakım ve bağımlılık uzanır (31:14). {ar:أَنِ ٱشْكُرْ لِى وَلِوَٰلِدَيْكَ, tr:ani-shkur lī wa-liwālidayka, gloss:bana ve anne babana şükret} buyruğu alınan iyiliğin arkasındaki emeği de şükrün konusu yapar (31:14). Bu aile sahnesi, gizli nimet yönünün başkasının emeğini ve maliyetini içerebileceğini somutlaştırır; anne emeği bütün gizli nimetlerin açıklaması değildir ve Allah nimet veren fail olarak kalır (31:14).

Gündelik bakımın ardındaki süreç, saklı izin daha küçük ölçekteki erişilebilirliğine açılır. Bir şey hardal tanesi ağırlığında olup kayanın içinde, göklerde ya da yerde gizlense de Allah onu ortaya çıkarır (31:16). {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli halde} iç tarafı, odaktaki {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} ise tartışanın yoksun olduğu bilgiyi taşırken {ar:يَأْتِ بِهَا ٱللَّهُ, tr:yaʾti bihā Allāhu, gloss:Allah onu ortaya çıkarır} sözü saklı izlerin ilahî erişime kapalı olmadığını gösterir (31:16). {ar:لَطِيفٌ, tr:laṭīf, gloss:en ince ayrıntılara erişen} ve {ar:خَبِيرٌ, tr:khabīr, gloss:her şeyden haberdar olan} nitelemeleri en küçüğe erişmeyi iç yüzü bilmekle yan yana getirir (31:16). Hardal tanesi ölçüsü en küçük izin hesaba konu olabileceğini düşündürebilir; bu bir çıkarımdır. Sahne nimetlerden çok Allah’ın her şeyin içini bilmesini anlatıyor da olabilir (31:16). Göğüslerde olanı Allah’ın bilmesi de insanın gözlem sınırıyla bu bilgiyi birlikte düşündürür (31:23); ilahî erişim, insanın her gizli şeyi bildiği anlamına gelmez.

## Delilden tartışmaya

İnsanın gizli olana erişiminin sınırı çizildikten sonra, {ar:وَ, tr:wa, gloss:ve} yeni bir bildirme yargısı başlatır. Artık topluluğa ikinci çoğul kişiyle seslenilmez: öne alınan {ar:مِنَ, tr:mina, gloss:arasından} insanlardan bir kesimi ayırır, {ar:ٱلنَّاسِ, tr:al-nāsi, gloss:insanlar} tartışanı insan topluluğunun içinde tutar, tekil {ar:مَنْ, tr:man, gloss:kim} ise bu kesimi bir tartışmacı tipinde toplar. Böylece ortak muhataplardan insanlığın içindeki birine dönülür; suçlama bütün insanlara yayılmaz. İnsan topluluğunun ortak delil alanı unutkanlık ihtimalini de keskinleştirir: bu kişinin görünür delili tanımamasıyla, {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli halde} diye nitelenen nimetlerin varlığını kabul etmekten onlar hakkında dayanaksız iddia kurmaya geçiş karşı karşıya gelir; gizlilik cehalete mazeret olmaz. Başlangıçtaki {ar:تَرَوْا۟, tr:taraw, gloss:görürsünüz} çağrısının ardından gelen bu ani dönüş, görmeye çağrı ile dayanağı olmadan tartışmayı karşı karşıya getirerek söyleyişe kınayıcı bir kuvvet verir.

Bu dönüş, aynı Allah adını da başka bir ilişkiye taşır. Önce göklerin ve yerin içindekileri konumlandıran {ar:فِى, tr:fī, gloss:içinde}, şimdi {ar:فِي, tr:fī, gloss:hakkında} biçiminde tartışmanın konusunu gösterir; kapsama alanı kozmik mekândan düşünsel alana kayar. Önermenin içindeki {ar:ٱللَّهَ, tr:Allāha, gloss:Allah}, {ar:أَنَّ, tr:ʾanna, gloss:şu gerçeği} sonrasında mansup özne olarak nimeti veren faildir; bu edat sonrasındaki {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} ise mecrur konu olur. Aynı sağlayan, önce delilin faili, sonra çekişmenin konusu hâline gelir; i‘rab ve edat değişimi âyetin bolluk anlatımından tartışmacıya dönüşünü taşır.

Bu Allah hakkında tartışmanın yakınında, {ar:لَا تُشْرِكْ بِٱللَّهِ, tr:lā tushrik billāh, gloss:Allah’a ortak koşma} buyruğu ve {ar:إِنَّ ٱلشِّرْكَ لَظُلْمٌ عَظِيمٌۭ, tr:inna ash-shirka laẓulmun ʿaẓīm, gloss:şirkin büyük bir zulüm oluşu} tevhid bakımından somut bir sınır çizer (31:13). Odaktaki {ar:فِي, tr:fī, gloss:hakkında} {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah} öbeği bu çerçevede duyulur; bu yakınlık tartışmacıya şirk hükmü vermez ve onu 31:13’teki uyarının muhatabıyla özdeşleştirmez (31:13). Başka bir sure içi sahnede {ar:مِنَ ٱلنَّاسِ, tr:mina al-nāsi, gloss:insanlardan bazıları} kalıbıyla biri Allah’ın yolundan saptıran oyalayıcı sözü satın alır; bu edinme hareketi {ar:ٱشْتَرَىٰ, tr:ishtarā, gloss:satın aldı} fiiliyle, sözün kendisi de {ar:لَهْوَ ٱلْحَدِيثِ, tr:lahw al-ḥadīth, gloss:oyalayıcı söz} ifadesiyle kurulur ve işaretleri alaya alma bu sahneye eşlik eder (31:6). Bu ayrı sahne, satın alınmış dikkatten odaktaki {ar:يُجَٰدِلُ, tr:yujādilu, gloss:tartışır} çekişmesine uzanabilecek bir toplumsal yol düşündürür; tekrar aynı kişiyi ya da zorunlu bir sırayı kanıtlamaz (31:6). İki bağlam birlikte, çekişme için tevhid sınırını ve olası bir toplumsal genişlemeyi görünür kılar (31:6, 31:13).

Tartışmanın nasıl bir eylem olduğunu {ar:يُجَٰدِلُ, tr:yujādilu, gloss:tartışır} belirginleştirir. III. kalıptaki biçim, iki tarafın söz ileri sürüp karşılık verdiği karşılıklı çekişmeyi anlatır; şimdiki-geniş kullanımı da tek seferlik bir itirazdan çok süren veya alışkanlık hâlini almış tartışmayı bu kişiyi tanıtan bir özellik gibi sunar. Aynı kökün başka bir biçim ve kullanımında ip, çözülmesi zor olacak kadar sıkı bükülür; kökün güreşme alanına değen imgesiyle birlikte bu ayrı yankı, sözlü çekişmeye gerilip düğümlenen bir mücadele tınısı katabilir. Fiziksel ip fiilin bu kalıptaki doğrudan çevirisi, güreş de âyetin anlattığı gerçek bir sahne değildir. Allah hakkında bilgisizce çekişme ve asi şeytana uyma yan yanalığı (22:3, 22:8), sözün sıkı örülmesinin doğruluğa tek başına güvence olmadığını düşündürür; bu niteleme burada anlatılan tartışmacıyla sınırlı kalır.

## Bilgi, yön ve yazılı ölçü

Tartışmanın dayanak eksiği önce {ar:بِغَيْرِ عِلْمٍۢ, tr:bi-ghayri ʿilmin, gloss:bilgisizce} ile anlatılır. Bu öbek fiile hâl ya da eşlik koşulu olarak bağlanır; bilgi eksikliği tartışmacının uzağında duran kusur değil, tartışmanın yürütülme biçimidir. İçindeki {ar:غَيْرِ, tr:ghayri, gloss:yoksun} bağımsız bir olumsuzluk parçacığı değildir; {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} adını yöneten tamlama ismidir. “Dışında kalma” basıncı iddiayı bilgiden uzak duyurabilir, ama yerel anlam yine “bilgisizce”dir; burada anlatılan eksiklik belirli bir uzmanlığın yokluğu değil, bilginin kendisinden yoksunluktur.

Aynı kökten gelen farklı biçimdeki {ar:عَلَم, tr:ʿalam, gloss:ayırt edici işaret}, bir şeyi ötekinden ayıran belirgin işareti anlatabilir; odaktaki {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} doğrudan “işaret” demek değildir. Ardından gelen yön ve ışık sözleri, bu ayrı biçimin yol seçtiren işaret çağrışımını da düşünmeye açar. Başlangıçtaki görme çağrısı ile bilgiden yoksun tartışmacının karşılaşması, delilce zengin çevreyle dayanakça boş iddia arasındaki yerel karşıtlığı kurar; bu, her soruyu kusur saymaz, burada anlatılan iddianın dayanağını sorgular.

Odaktaki {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} ile doğru cevabı dile getirmek arasındaki ayrım, yaratılışa ilişkin başka bir soruda görünür olur: gökleri ve yeri kimin yarattığı sorusuna “Allah” cevabı verilir, ardından insanların çoğunun bilmediği söylenir (31:25). Bu yan yana geliş, bir doğru önermeyi söylemekle onu tanıyıp kavramanın, şükür ve bağlılığı da düzenleyecek biçimde anlamanın aynı olmadığını düşündürür (31:25). Bununla birlikte “çoğu bilmez” sözü, yaratıcı cevabının kendisinden ziyade daha ileri gerçekler ya da sonuçlar hakkındaki bilgisizliği anlatıyor olabilir; iki yerdeki insanlar özdeş değildir (31:25).

İkinci dayanak, {ar:وَ, tr:wa, gloss:ve} ile ayrı bir unsur olarak eklenen {ar:لَا, tr:lā, gloss:yok} ve belirsiz {ar:هُدًۭى, tr:hudan, gloss:yol gösterme} biçimiyle devreden çıkar. Olumsuzluk belirli bir rehberi değil herhangi bir yönlendirmeyi kapsar. Hidayet yalnızca bilgi miktarını değil, gidilecek yönü ve güzergâhı da taşır; böylece tartışmacı bir yargıyı doğru yöne sevk edecek yoldan da yoksundur. Bu ikinci eksiklik bilgiyi başka sözlerle yinelemez, ayrı bir dayanağı devreden çıkarır.

Bu yokluk, sûrenin başında zaten sunulmuş imkânları tersine çevirir: {ar:كِتَٰبٍ حَكِيمٍۢ, tr:kitābin ḥakīmin, gloss:hikmetli kitap} ile {ar:هُدًۭى وَرَحْمَةًۭ, tr:hudan wa-raḥmatan, gloss:rehberlik ve rahmet} anılması (31:2, 31:3), 31:20’de {ar:هُدًۭى, tr:hudan, gloss:hidayet} ve {ar:كِتَٰبٍۢ مُنِيرٍۢ, tr:kitābin munīrin, gloss:aydınlatıcı kitap} yokluğunu daha keskin duyurur (31:2, 31:3). Bu eksiklik, veri açığının yanında sûrenin görünür kıldığı rehberlik düzeninden kopukluk olarak da okunabilir (31:2, 31:3); açılıştaki karşıtlık bu okumayı destekler, ancak her tartışmacının rehberliği bilerek reddettiğini kanıtlamaz (31:2, 31:3).

Yönün yokluğuna karşılık, aynı sûrede toplumsal olarak aktarılmış bir yol belirir. Allah’ın indirdiğini izleme çağrısına bazıları atalarının üzerinde buldukları şeyi izleyeceklerini söyleyerek karşılık verir; {ar:ٱتَّبِعُوا۟, tr:ittabiʿū, gloss:izleyin} ve {ar:نَتَّبِعُ, tr:nattabiʿu, gloss:izliyoruz} yinelemesi iz sürmeyi öne çıkarırken, {ar:مَا وَجَدْنَا عَلَيْهِ, tr:mā wajadnā ʿalayhi, gloss:üzerinde bulduğumuz şey} önceden var olan pratiği, {ar:ءَابَآءَنَآ, tr:ābāʾanā, gloss:atalarımızı} da bu yolun toplumsal kaynağını gösterir (31:21). Böylece odaktaki {ar:هُدًۭى, tr:hudan, gloss:doğru yönü gösterme} eksikliğinin yerini miras alınmış bir izlek alabilir; izlenen yolun varlığı onu doğru kılmaz, fakat bu bağ her miras uygulamasını yanlış saymaz ve iki ayetin kişilerini birleştirmez (31:21).

Bu aynı sure içi sahnede {ar:ٱلشَّيْطَٰنُ يَدْعُوهُمْ إِلَىٰ عَذَابِ ٱلسَّعِيرِ, tr:ash-shayṭānu yadʿūhum ilā ʿadhābi as-saʿīr, gloss:şeytan onları alevli azaba çağırır} sözü de yer alır (31:21). Yıkıcı çağrı, birinin seslenmesinin tek başına doğru yola götürmediğini gösteren ayrı bir karşılıktır; odaktaki {ar:هُدًۭى, tr:hudan, gloss:hidayet} anlamı şeytanın çağrısına indirgenmez (31:21). Miras alınmış yol dışarıdan devralınan çerçeveyi, göğüslerde olanı Allah’ın bilmesi içte saklı yönü (31:23), doğru yaratıcı cevabından sonra çoğunluğun bilmez sayılması da odaktaki {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} yokluğunun neyi kapsadığı sorusunu gündeme getirir (31:25). Bu sure içi karşılaştırmalar tartışmanın çevresine toplumsal kaynak, iç dünya ve bilme sorularını yerleştirir; kişileri özdeşleştirmez (31:21, 31:23, 31:25).

Bu yön sorununa başka bir sahne bedeni, eylemi ve tutunmayı ekler. Kişi yüzünü Allah’a teslim eder, iyi davranır ve sağlam kulpa tutunur (31:22): {ar:أَسْلَمَ وَجْهَهُۥ, tr:aslama wajhahu, gloss:yüzünü teslim etti} ve {ar:ٱلْعُرْوَةِ ٱلْوُثْقَىٰ, tr:al-ʿurwati al-wuthqā, gloss:sağlam kulp} yönelimin güvenilir desteğe nasıl bağlandığını somutlaştırır (31:22). Böylece {ar:هُدًۭى, tr:hudan, gloss:hidayet} yalnız doğru içeriği almak değil, teslimiyet ve iyi eylemle sürdürülen, etkin biçimde tutunulan bir yöneliş olarak da duyulur; beden imgesi bilgi, yön ve yazı kavramlarını tek tek fiziksel harekete eşitlemez (31:22).

Üçüncü eksiklik, ikinci bir {ar:وَ, tr:wa, gloss:ve} ile eklenen bağımsız {ar:لَا, tr:lā, gloss:yok} altında {ar:كِتَٰبٍۢ, tr:kitābin, gloss:yazılı kitap}tır; yazılı ölçü hidayetin alt başlığına indirgenmez. Belirsiz biçim herhangi bir kitap ya da yazılı dayanağın yokluğunu söyler, belirli bir kutsal metnin adını vermez. Odaktaki isim metin, sayfa ya da kitap anlamındadır. Kök ailesindeki başka kullanımlar bir şeyi diğerine bağlayıp bütün kurmayı ve harfleri düzenleyerek metin yazmayı ya da kopyalamayı düşündürebilir; bağlayıcı yükümlülük bildiren ayrı bir biçim de vahiy ile gelenek karşıtlığında kitabı sınanabilir yazılı ölçü gibi duyurur. Bu çağrışımlar odaktaki sözcüğü doğrudan “hüküm” diye çevirmeyi gerektirmez.

Kitabı niteleyen {ar:مُّنِيرٍۢ, tr:munīrin, gloss:aydınlatan}, IV. kalıptaki etkin ortaçtır: metnin yalnız ışık taşımasını değil, okura açıklık sağlayıp yolu görünür kılmasını anlatır. Buradaki aydınlık bilişsel açıklıktır; ateş anlamı sıfatın yerel karşılığı değildir. Belirsiz bilgi, hidayet ve kitap adlarının art arda gelişi yokluk dizisini son aydınlatıcı sıfata taşır ve cümlenin işitsel doruğunu kurar.

Bu üç eksikliğin birlikte nasıl çalıştığı, her birinin ayrı işlevi korunduğunda görülür. {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} iddianın tanınacağı dayanağı, {ar:هُدًۭى, tr:hudan, gloss:hidayet} izlenecek doğru yönü verir; yazılı {ar:كِتَٰبٍۢ, tr:kitābin, gloss:kitap} bu iddiayı sabitleyip sınamaya açarken {ar:مُّنِيرٍۢ, tr:munīrin, gloss:aydınlatan} yazılı ölçüyü okunur kılar. Böylece bilgi bir iddiayı tanımaya, hidayet güzergâhı seçmeye, kitap ölçüyü kayda bağlamaya yarar; aydınlık da bu yolun ve ölçünün görülebilmesini sağlar. Harita, yol ve işaret bu işlemlerden kurulan bir bileşik imgedir, gerçek eşyalar değildir. {ar:يُجَٰدِلُ, tr:yujādilu, gloss:tartışır} fiilinin sıkıca bükülen ip yankısı burada yeni bir ilişki kazanır: söz kendi içinde ne kadar örgülü görünse de bilgi, yön ve yazılı sınama dışarıda kaldığında örgünün tutarlılığı iddiayı doğrulamaya yetmez (22:3, 22:8). Bu, tek tartışmacının dayanağına ilişkin bir nitelemedir; bütün tartışmaları kusurlu saymaz.

Daha uzak ve keşifsel bir toplumsal benzetmede, {ar:يُجَٰدِلُ, tr:yujādilu, gloss:tartışır} fiilindeki karşılıklı çekişme ile {ar:كِتَٰبٍۢ مُنِيرٍۢ, tr:kitābin munīrin, gloss:aydınlatan yazılı ölçü} ortak bir zeminde buluşur. Kamusal ve aydınlık bir yazılı alan, farklı iddiaları toplumsal ilişkiler içinde sınanabilir ve birlikte tutulabilir kılabilir; bu imge topluluklar arası düşmanlığa karşı ortak denetim düşüncesini açar. Uzak bir benzetme olarak kalır: her tartışma şiddet değildir, yazılı dayanak çekişmeyi kendiliğinden bitirmez ve kitap otoritesinin yerini almaz. “Aydınlatan” sözcüğünün anlamı da bu toplumsal ateş karşıtlığıyla ateşe dönüşmez.

Yazılı ölçünün sınırı, başka bir sure içi görüntüde belirginleşir (31:27). Yazı kamışları ve kalemler denizi ve ona katılan denizleri mürekkep gibi tüketse de sözler tükenmez (31:27). Odaktaki {ar:كِتَٰبٍۢ, tr:kitābin, gloss:kitap} yazıyla kurulmuş metni, {ar:مُّنِيرٍۢ, tr:munīrin, gloss:aydınlatan} ise görmeyi sağlayan açıklığı taşır; bu ikisi birlikte yazılı ölçüyü okura yol açan bir pencere gibi düşündürür (31:27). Pencere imgesi yazının rehberliğini korurken ilahî sözlerin sonunu getirmez; 31:27’nin bolluk görüntüsü de odaktaki kitabın içeriğiyle özdeş değildir (31:27).

## Zaman, yolculuk ve bilginin sınırı

Hizmete yöneltilmiş düzen bu kez sabit bir nesne listesi değil, zaman içinde işleyen bir devinim olarak görünür. Gece gündüze, gündüz geceye girer; güneşle ay belirlenmiş bir süreye dek akar (31:29). {ar:سَخَّرَ, tr:sakhkhara, gloss:hizmete yöneltti} belirli işe yöneltilmiş düzeni, {ar:ظَٰهِرَةًۭ, tr:ẓāhiratan, gloss:görünür} açığa çıkan yüzü, {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} içte kalanı taşırken, bu ayrı zaman sahnesi görünürlük ve örtülmenin sürekli değiştiği bir dolaşım düşündürür (31:29). Gece ve gündüz nimet çiftinin kendisi değildir; sahne yararlanıcının yönetmediği ritmi ve sonlu zamanı ekler (31:29).

Bu zaman ölçeğinden ayrı bir anlatı anı deniz yolculuğudur. Allah’ın nimetiyle ilerleyen gemi, odaktaki {ar:سَخَّرَ, tr:sakhkhara, gloss:hizmete yöneltti} düzeninin ve elverişli yaşamı taşıyan {ar:نِعَمَهُۥ, tr:niʿamahu, gloss:nimetleri} nimetinin elle tutulur örneği olur; sabredenlerle şükredenler için bir işaret sayılır (31:31). Ardından gölge gibi örten, birbirine karışıp yükselen dalgalar yolcuların görünür güvenliğini kapatır (31:32). Yolcular sıkışınca dini yalnız Allah’a has kılarak yakarırlar; kurtuluşun ardından bazıları ölçülü kalırken bazıları bildikleri işaretlere rağmen inkâr eder, nimete karşılık vermez ve ona ihanet eder (31:32). Böylece bu nimet görünür yarar sağlarken, {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} iç yönü de tehlike ve kurtuluşta kişinin iddiasıyla uyuşup uyuşmadığı bakımından sınanabilir (31:31, 31:32). Tepkiler sabit bir gizli kişiliğin kanıtı olmak zorunda değildir; duruma bağlı kalabilir (31:32). 31:29’daki dolaşım ile (31:31, 31:32) deniz krizi ayrı sahnelerdir; birlikte biri yaşama imkânı veren ritmi, öteki iç karşılığı görünür kılabilen sınanma koşulunu açar (31:29, 31:31, 31:32).

Baştaki “Görmüyor musunuz?” çağrısına dönüş, bu incelemenin sınırını da gösterir. {ar:تَرَوْا۟, tr:taraw, gloss:görmek ve düşünmek} görünür nimetlerin iç yüzünü {ar:بَاطِنَةًۭ, tr:bāṭinatan, gloss:gizli} ve bilginin ölçüsünü {ar:عِلْمٍۢ, tr:ʿilmin, gloss:bilgi} düşünmeye çağırırken, saatin ne zaman geleceği, gökten hayat veren yağmurun inişi, rahimlerde olan, insanın yarın ne kazanacağı ve nerede öleceği Allah katındaki bilgi alanları olarak anılır (31:34). Bu beş başlık insanın denetim sınırını belirginleştirir: görünür etkilerden gizli desteği tanımak mümkündür, fakat bu dikkat gelecek hakkındaki her ayrıntıyı açma yetkisi vermez (31:34). Listenin yalnız belirli gelecek bilgilerini sınırladığı, gizli nimetler üzerine bütün çıkarımları yasaklamadığı yorumu da açık kalır (31:34).

</source_prose>
