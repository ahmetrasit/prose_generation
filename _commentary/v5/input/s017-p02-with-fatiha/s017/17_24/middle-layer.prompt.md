# Commentary v5 lossless middle-layer consolidator

You are the middle-layer consolidator for **17:24**. Transform the
supplied editorial ayah commentary into prose that is materially shorter and
easier to follow while preserving every distinct semantic finding, mechanism,
detail, qualification, and live alternative.

This is a semantic consolidation task, not summarization and not a new
evidence-selection stage. The supplied editorial prose is the complete evidence
boundary. Do not inspect upstream evidence, add interpretations, strengthen a
claim, resolve an uncertainty, or silently remove a difficult or peripheral
finding.

Produce two synchronized outputs:

- reader prose: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.prose.middle.tr.md`
- atomic claim ledger: `_commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.middle.claims.json`

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
- Refer to source paragraphs as `17:24 ¶N`.

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

`(17:24 ¶12, ¶15, ¶16, ¶17)`

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
`_commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.middle.claims.json` with this structure:

```json
{
  "schema_version": "commentary-v5-middle-claim-ledger-v2",
  "ayah_ref": "17:24",
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
        "citation": "(17:24 ¶1)"
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
python3 _commentary/v5/validate_prose.py _commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.prose.middle.tr.md
python3 -B _commentary/v5/validate_middle_layer.py \
  --source _commentary/v5/editorial/s017-p02-with-fatiha/s017/17_24/17_24.prose.editorial.tr.md \
  --prose _commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.prose.middle.tr.md \
  --ledger _commentary/v5/middle/s017-p02-with-fatiha/s017/17_24/17_24.middle.claims.json \
  --ayah-ref 17:24
```

Repair every reported prose, ledger, mapping, anchor, metric, or density
finding without changing the semantic inventory, then rerun both commands
until they report `ok`. The middle-layer validator also confirms that the
ledger is valid JSON and that reader prose contains no Quran interval
shorthand. Mechanical validation does not establish semantic completeness or
Turkish fluency; all four audit passes remain required.

## Input

Source prose path: `_commentary/v5/editorial/s017-p02-with-fatiha/s017/17_24/17_24.prose.editorial.tr.md`

<source_prose>
## Duruştan duaya

17:24, anne babaya merhametle alçalmayı ve ardından ikisi için Rabb'den merhamet dilemeyi buyurur: {ar:وَٱخْفِضْ لَهُمَا جَنَاحَ ٱلذُّلِّ مِنَ ٱلرَّحْمَةِ, tr:wa-ikhfiḍ lahumā janāḥa adh-dhull mina ar-raḥmah, gloss:merhametten ötürü ikisine tevazu kanadını indir} ve {ar:وَقُلْ رَبِّ ٱرْحَمْهُمَا, tr:wa-qul rabbi irḥamhumā, gloss:de ki Rabbim ikisine merhamet et}. Son cümledeki {ar:كَمَا رَبَّيَانِي صَغِيرًا, tr:kamā rabbayānī ṣaghīran, gloss:beni küçükken yetiştirdikleri gibi} bu dileğin dayanağı olarak hatırlanan ebeveyn bakımını gösterir. Buyruğun ilk kolu bedene, ikincisi söze yönelir; ikisi aynı ilişkiye dönse de ayrı eylemlerdir.

İki emrin başındaki {ar:وَ, tr:wa, gloss:ve} süren bir diziyi devam ettirir; kendi başına önceki adımın ne olduğunu açıklamaz. {ar:وَٱخْفِضْ, tr:wa-ikhfiḍ, gloss:ve alçalt} ile {ar:وَقُلْ, tr:wa-qul, gloss:ve söyle} aynı bağlaçla eş düzeyde açılır: ayetin yerel sırası önce bedensel duruşu, sonra duayı verir, fakat birini ötekinden üstün kılmaz. İlk eylemde {ar:لَهُمَا, tr:lahumā, gloss:ikisi için} kanat imgesi tamamlanmadan iki ebeveyni yararlanıcı olarak görünür kılar; sözcüğün kısa, birleşik sesi de çifti kulakta taşır. Edatlı ikil biçim eylemin iki ebeveynin yararına olduğunu gösterir; bu ilişkiye ayrıca bir ödül vaadi yüklemez. Alçaltma fiili ebeveynleri değil, tamlamadaki {ar:جَنَاحَ ٱلذُّلِّ, tr:janāḥa adh-dhull, gloss:alçalışın kanadı} imgesini doğrudan nesne alır. Duada {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} içindeki ikil nesne aynı iki kişiyi bu kez dileğin alıcısı yapar; iki işlev değişirken ebeveyn çifti ayet boyunca açık kalır. Okuma başka bir zamirin gönderimini çözmeye dayanmaz.

Bedensel alçalmanın ardından {ar:قُلْ, tr:qul, gloss:söyle} buyruğu, yakarışı yalnız aktarılacak bir içerik olmaktan çıkarıp ağızdan söylenecek bir söz eylemi kurar. İlk emir bedeni ebeveynlere yöneltmişken {ar:وَقُلْ, tr:wa-qul, gloss:ve söyle} sözü {ar:رَبِّ, tr:rabbi, gloss:Rabbim} hitabına ve ikisi için dileğe geçirir; bakımın yönü ve aracı değişir. Kısa {ar:قُلْ, tr:qul, gloss:söyle} sesinin hemen {ar:رَبِّ, tr:rabbi, gloss:Rabbim} hitabına açılması yerel bir işitme hareketidir. Dua böylece konuşanın ağzından kurulur; karşılığı ise gerçekleşmiş bir sonuç değil, Allah'tan istenen merhamettir.

{ar:ٱخْفِضْ, tr:ikhfiḍ, gloss:alçalt} olağan anlamıyla aşağı indirmeyi taşır; nesnesi olan {ar:جَنَاحَ, tr:janāḥa, gloss:kanat} önce kuşun uçma organını düşündürür ve emrin yönünü görünür kılar. Kanadın bir yana eğilen, koruyucu tarafı da ayrı bir çağrışım açar. Aşağı indirme, iki ebeveynin yararlanıcı oluşu ve merhamet ibaresiyle birleşince bu kanat onlara doğru eğilen bir siper, yaklaştırılan gölge gibi duyulur. Yönelişi kanat sözcüğü tek başına değil, aşağı indirme emriyle açık alıcının birlikteliği kurar; kanat burada gerçek bir uzuv değil, ebeveynlere sunulan koruyucu davranışın imgesidir. Fiilin güç ve sertliği azaltma, yumuşatma yönü de bu özel kanatlı-merhametli kuruluşta işler: aşağı hareket korunurken tutum ebeveynlere karşı incelir. Bu nüans bu kuruluşla sınırlıdır; fiilin her kullanımına genellenmez. Kısa emrin sıkışık sesiyle ardından açılan kanat ve merhamet sözlerinin genişliği arasındaki karşıtlık da anlamı tek başına belirlemeyen, bu ifadeye özgü keşif niteliğinde bir işitme izlenimidir; alçalmanın yönünü kulakta tutar.

Tamlamada {ar:ٱلذُّلِّ, tr:adh-dhull, gloss:alçalış ve yumuşaklık} kanadın niteliğini kurar; tevazu imgenin içindedir, ayrı bir emir değildir ve iki sözcüğün anlam alanları birbirine karışmaz. Sözcük hem düşük, değeri zedelenmiş konumun basıncını hem de kişinin değerini yitirmeden isteyerek yumuşamasını taşıyabilir. Kanat imgesi ile iki alıcının açıklığı bu alçalmayı ilişkiye bağlar; tamlamadan sonra gelen ayrı {ar:مِنَ ٱلرَّحْمَةِ, tr:mina ar-raḥmah, gloss:merhametten} öbeği merhameti onun çerçevesi yapar. Buradaki {ar:مِنَ, tr:mina, gloss:-den / -dan} yeni bir öbek açar; belirli {ar:ٱلرَّحْمَةِ, tr:ar-raḥmah, gloss:merhamet} duruşun adı konmuş kaynağı ya da niteliği olarak duyulabilir. Bu iki yakın dilbilgisel vurgu açık kalır. Merhamet çerçevesi aşağı yön ve sözcüğün sert basıncını silmeden, isteyerek yumuşama okumasını zorla ezilmeden ayırır. Çift ünsüzün kanatla merhamet arasında kısa bir ağırlık tuttuğu izlenimi ölçülmüş akustik etki değil, keşif niteliğinde yerel bir sestir; alçalış ile merhamet çerçevesinin birlikteliğini işittirir.

Merhamet ibaresi aşağı duruşun saikini adlandırır; aynı sözcük ailesinin {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} biçimi ardından istenen eyleme döner. İçten şefkat ve yakınlık, iki ebeveyne yöneltilmiş etkin esirgeme ve iyilik dileğine geçer; ikil nesne kime yöneldiğini gösterir, merhametin nasıl gerçekleşeceğini değil. {ar:مِنَ ٱلرَّحْمَةِ, tr:mina ar-raḥmah, gloss:merhametten} ifadesinin sonundaki n sesinin sonraki r'ye bağlanması, kaynak öbeğini okunuşta kesintisiz duyurabilir; bu da yerel bir tilavet izlenimidir. İnsan tutumu duanın saiki, ilahî merhamet ise henüz gerçekleştiği bildirilmeyen istektir; bu ayrım korunurken duanın yönelişi şefkatli duruştan Allah'tan dilenen etkin esirgemeye geçer.

{ar:رَبِّ, tr:rabbi, gloss:Rabbim} hitabı ilk kişiyi seslenişin içine alır; dua uzaktan yapılan bir tasvir değil, ilişki içinden yöneltilen kişisel yakarış olur. Çekim notu bu seslenişi öne çıkarırken nominatif çözümleme olasılığını da açık bırakır; ayrı bir biçim verilmediği için bu olasılıklar arasında kesin hüküm kurulmaz. Rab ve hükümranlık hitabındaki gözetme, buyurma ve yönetme alanı, merhamet dileğini kabul edebilecek muhatabı belirginleştirir; duanın içeriğini ise ardından gelen merhamet isteği taşır. {ar:رَبِّ, tr:rabbi, gloss:Rabbim} ile ilerideki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} yakın sesleri ve gözetip yetiştirme yönündeki çağrışımları birbirine yaklaştırır. Bu yankı, ayrı kök ve failleri koruyarak kişisel yakarışın yanına ebeveyn yetiştirmesi hatırasını getirir.

{ar:كَ, tr:ka, gloss:gibi} karşılaştırması tek bir sözcüğü değil, ardından gelen {ar:مَا, tr:mā, gloss:ki / yetiştirme} ile açılan ebeveynlik eyleminin tümünü ölçüye alır. Yüzeyde bitişik {ar:كَما, tr:kamā, gloss:nasıl ki} kısa bir eşik gibi karşılaştırma işaretini içerik açıcıya bağlayıp okuyucuyu son cümleye geçirir; bu bağlılık {ar:مَا, tr:mā, gloss:ki / yetiştirme} için iki çözümlemeden hangisinin seçileceğini belirlemez. Bir okumada dua “beni nasıl yetiştirdilerse” biçiminde bakımın tarzına bağlanır; diğerinde yetiştirmenin kendisi, eylem adı gibi düşünülen bakım olayı karşılaştırmanın içeriği olur. Her iki durumda da ölçü tek sözcük değil, tamamlanmış yetiştirme cümlesidir. Böylece merhamet dileği hatırlanan bakıma dayanır; karşılaştırma insanî yetiştirme ile ilahî merhamet eylemini aynı miktara indirmez, hatırlanan bakımı duanın zemini yapar. Kısa eşiğin yumuşak kadansı sabit bir ses kuralı değil, karşılaştırmadan bakım cümlesine geçişe eşlik eden yerel bir izlenimdir.

{ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} tamamlanmış bir eylemi anlatır: iki ebeveyn, birinci tekil kişi olan konuşanın bakımını üstlenmiştir. Dua hatırlanan yetiştirmeye dayanır; geçmiş zaman ebeveynlerin bugünkü ihtiyacı hakkında hüküm vermez. İkil özne iki ebeveyni aynı eylemde gösterirken, her anı aynı biçimde yaşadıklarını belirlemez. İki ebeveyn ile tek konuşanın bu biçimde birleşmesi genel büyüme alanını kişisel anıya çevirir; biçimin ayırt edici kuruluşu kendi başına ek anlam yüklemez. Sondaki uzayan ses birinci kişi nesne bağını işitilir kılar ve bakım görme hatırasını yakınlaştırır. Yetiştirme ve büyüme yönü, ardından gelen {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} ile temas ederek bağımlılıktan yeterliğe uzanan bir süreç düşündürür; bu özel temas başka artma ya da yükselme anlamlarını fiile taşımaz, çocukluk hatırasını gelişme süreci içinde açar.

{ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} yetiştirme sırasında konuşanın hâlini bildirir; kalıcı kimliğini ya da ebeveynlerin niteliğini değil. Belirsiz biçimi kesin bir yaşı seçmeden çocukluk içindeki bağımlılık ve kırılganlık süresini açık tutar. Sözcüğün temel karşıtı büyüklüktür; yetiştirme fiili bu küçüklüğü soyut ölçüden bakım gören çocuğun hâline taşır. Bu bağlamda küçüklük değersizleştirme değil, çocukluk bağımlılığıdır; yaşın kesinliği açık bırakılır. Ayetin sonundaki konum, hatırlanan çocukluğu dileğin yakın gerekçesi olarak yoğunlaştırırken ebeveyn bakımının tek boyutu yapmaz. Son sözcüğün yumuşak kadansı ölçülmüş bir ses kuralı değil, bu çocukluk hatırasını dileğin kapanışında duyuran yerel bir okuma izlenimidir.

Bu yapı, atfedilmiş ve ihtiyatlı bir karşılıklılık okumasına da açılır: bir zamanlar küçük çocuğu yetiştiren ebeveynlere, şimdi konuşanın bedeni koruyucu bir alçalışla döner. {ar:ٱخْفِضْ, tr:ikhfiḍ, gloss:alçalt} aşağı hareketi, {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} ve {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} hatırasıyla yan yana gelince, geçmişte bakım alan küçüklüğün karşısında bugünkü davranış görünür olur; {ar:جَنَاحَ, tr:janāḥa, gloss:kanat} ve {ar:لَهُمَا, tr:lahumā, gloss:ikisi için} bu yönelişi ebeveynlere dönük siper olarak tutar. Bu yorum emir fiilinin olağan aşağı yönünü korur ve konuşanın yaşını bildirmez; çocuklukta alınan bakım ile bugünkü merhametli tutum arasında ihtiyatlı bir hayat evresi bağlantısı kurar, bire bir geri ödeme ya da katı rol değişimi ileri sürmez.

Bedensel alçalma evladın gösterebildiği özeni, dua ise yapabildiğinin ötesindeki merhameti Rabb'e emanet etme yönelişini görünür kılar. Bu, bedenle gösterilen bakımın yetersiz sayılması değil, eylemden yakarışa geçiştir: kişi yapabildiği özeni gösterir, ebeveynleri için dilediği daha kapsamlı korumayı {ar:رَبِّ, tr:rabbi, gloss:Rabbim} hitabıyla Rabb'ine yöneltir. Rabb'in hükmetme ve gözetme yetkisi, isteği gerçekleştirebilecek muhataba seslenişi belirginleştirir; {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} dileğinin içeriği yine iki ebeveyndir. Daha uzak ve biçimce dolaylı bir çağrışımda {ar:قُلْ, tr:qul, gloss:söyle} olağan konuşma anlamını korurken yük kaldırma ya da üstlenme yönünde duyulabilir. {ar:ٱخْفِضْ, tr:ikhfiḍ, gloss:alçalt} aşağı yönü, {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} geçmiş ebeveyn bakımını, {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} ise konuşanın o zamanki çocukluk hâlini hatırlatır; bu ayrıntılarla söz, ebeveynlerin ihtiyacını yukarı taşıyan dua gibi düşünülebilir. Bu yukarı taşıma, {ar:قُلْ, tr:qul, gloss:söyle} için çeviri ya da gerçek bir yükseliş değil, bedensel alçalışla kurulan ihtiyatlı bir karşı-hareket imgesidir.

## Yakın bağlamda ebeveyn

Çocukluk hatırasının hemen öncesinde 17:23 anne babanın yaşlılığa erişmesinden söz eder: {ar:الْكِبَرَ, tr:al-kibara, gloss:yaşlılık} ve {ar:وَبِالْوَالِدَيْنِ إِحْسَانًا, tr:wa-bi-l-wālidayni iḥsānan, gloss:anne babaya iyilik}. 17:23'teki yaşlılık ile 17:24'teki {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} yan yana gelince, bir zamanlar bağımlı olan kişinin şimdi kapasitesi değişebilen ebeveynlerine yönelmesiyle aynı bakım ilişkisinin iki evresi duyulabilir. Bu, yan yana gelişe bağlı ihtiyatlı bir hayat döngüsü okumasıdır: yakın emirler aile edebini de öne çıkarabilir ve katı bir rol değişimini kanıtlamaz.

17:23'teki {ar:وَلَا تَنْهَرْهُمَا, tr:wa-lā tanharhumā, gloss:ikisine çıkışma} yasağı ile {ar:وَقُلْ لَهُمَا قَوْلًا كَرِيمًا, tr:wa-qul lahumā qawlan karīman, gloss:ikisine güzel söz söyle} buyruğu bedensel alçalışın yanına söz adabını koyar. Çıkışmamak ve değerli söz söylemek, 17:24'teki {ar:ٱلذُّلِّ, tr:adh-dhull, gloss:alçalış ve yumuşaklık} içinde duyulan gönüllü inceliği somutlaştırır; odaktaki {ar:وَقُلْ, tr:wa-qul, gloss:ve söyle} bu konuşma yönünü iki ebeveyn için edilen duaya taşır. Güzel söz buyruğu ile dua ayrı söz eylemleri olarak kalır, fakat ikisi de aynı aile ilişkisine dönük merhametli davranışın yüzleridir.

17:23 ibadeti Allah'a ayırır: {ar:أَلَّا تَعْبُدُوا إِلَّا إِيَّاهُ, tr:allā taʿbudū illā iyyāhu, gloss:yalnız O'na kulluk etmek} buyruğu kulluğu yalnız O'na yöneltirken, 17:24 bedeni anne babaya ve {ar:رَبِّ, tr:rabbi, gloss:Rabbim} hitabındaki duayı Allah'a yöneltir. Böylece ebeveyne dönük derin hürmetin ibadet olmadığı, bedenin yöneldiği muhatap ile duanın yöneldiği muhatabın ayrı kaldığı görülür. 17:39'daki {ar:وَلَا تَجْعَلْ مَعَ اللَّهِ إِلَٰهًا آخَرَ, tr:wa-lā tajʿal maʿa llāhi ilāhan ākhar, gloss:Allah ile başka bir ilah edinme} yasağı bu yönelişi başka ilahlardan da ayırır; aynı ayetin {ar:مِمَّا أَوْحَىٰ إِلَيْكَ رَبُّكَ مِنَ الْحِكْمَةِ, tr:mimmā awḥā ilayka rabbuka mina l-ḥikmah, gloss:Rabbinin sana vahyettiği hikmetten} ifadesi aile buyruğunu vahyedilmiş hikmet içine yerleştirir. 17:23 ve 17:39'un aile buyruğunu kuşatan kitap ayracı okuması, yalnız 17:24'ün kanat imgesine değil, bütün yakın emir dizisine uzanıyor olabilir. Bu sınır ebeveyne gösterilen şefkati küçültmeden ibadetin muhatabını ayırt eder.

Kanadın alçaltılması cömertçe yönelmeyi ve kendini bütünüyle vermeyi düşündürür; yakın ayetler bu yönelişi hak, dil ve imkân bakımından açar. 17:26 yakının hakkını adlandırır: {ar:ذَا الْقُرْبَىٰ حَقَّهُ, tr:dhā al-qurbā ḥaqqahu, gloss:yakına hakkını ver}. Maddi yardım verilemediğinde 17:28 merhametle ve {ar:قَوْلًا مَيْسُورًا, tr:qawlan maysūran, gloss:kolay ve yumuşak söz} ile yönelmeyi öne çıkar; imkân daralsa da söz sürer. 17:29'daki {ar:يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:yadaka maghlūlatan ilā ʿunuqika, gloss:elini boynuna bağlanmış tut} ve {ar:وَلَا تَبْسُطْهَا كُلَّ الْبَسْطِ, tr:wa-lā tabsuṭhā kulla l-basṭi, gloss:elini bütünüyle açma} vermenin kıstırılmışlık ile sınırsızca açılma uçlarını; 17:30'daki {ar:يَبْسُطُ الرِّزْقَ وَيَقْدِرُ, tr:yabsuṭu r-rizqa wa-yaqdiru, gloss:rızkı genişletir ve daraltır} ise maddi kapasitenin değişmesini gösterir. Yakın bağlamın bu bağlantısı hakları 17:24'ten türetmez, ebeveynlerin maddi durumunu da bildirmez; cömert bakımın hakkı gözetme, imkân daralınca yumuşak sözle sürme ve değişen rızka göre ölçülü kalma biçimlerini belirginleştirir.

Hatırlanan yetiştirmeye karşılık verme düşüncesi, 17:35'in ölçüyü tam tutma ve doğru teraziyle tartma buyruklarıyla başka bir eylem alanına taşınabilir: alınan iyiliğe aynı işi yineleyerek değil, farklı bir doğru davranışla karşılık verme fikri belirir. Odaktaki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} ile bu buyruklar arasındaki bağ, {ar:كَمَا, tr:kamā, gloss:gibi} karşılaştırmasına farklı eylemler arasında sadakat çağrışımı ekleyen ihtiyatlı bir okumadır. 17:35 malı ölçüp tartar; bu temas ebeveyn emeğini sayılabilir ve eşit karşılığı ödenebilir bir borç yapmaz. Böylece sadakat, aynı eylemin tekrarı değil, başka bir doğru davranış olarak duyulur.

Küçükken alınan bakım hatırası, korunmaya muhtaç çocuk ve yetime dönük özenle de ihtiyatlı bir temas kurar. 17:31'de {ar:خَشْيَةَ إِمْلَاقٍ, tr:khashyata imlāq, gloss:yoksulluk korkusuyla} çocukları öldürme yasağını, çocukların ve ebeveynlerin rızıklandırılacağı güvencesi {ar:نَحْنُ نَرْزُقُهُمْ وَإِيَّاكُمْ, tr:naḥnu narzuquhum wa-iyyākum, gloss:onları da sizi de biz rızıklandırırız} izler; bu yan yana geliş 17:24'teki merhamet isteğini darlık altında yaşatma ve bakım sorumluluğuyla buluşturur. 17:34'te {ar:مَالَ الْيَتِيمِ, tr:māla l-yatīmi, gloss:yetimin malı} üzerindeki koruma erginliğe dek sürer; {ar:وَأَوْفُوا بِالْعَهْدِ, tr:wa-awfū bi-l-ʿahd, gloss:ahde bağlı kalın} buyruğu bu sürekliliği sadakate bağlar. Böylece kişisel yetiştirilme hatırası, yoksulluk korkusu altındaki çocuğun yaşatılması ile yetim malının erginliğe dek korunmasını ayrı bakım sorumlulukları olarak görünür kılar. Bu bağlantı 17:24'ü sonraki hükümlerin hukukî kaynağı yapmaz ve konuşanın çocukluğunu yetimin durumuyla özdeşleştirmez.

## Alçalma ve yükselmenin başka sahneleri

Anne babaya dönük gündelik tevazu, 17:37'nin yer ve dağlarla çizdiği dikey sınır yanında da okunabilir. {ar:لَن تَخْرِقَ الْأَرْضَ, tr:lan takhriqa l-arḍa, gloss:yeri asla yarıp geçemezsin} yeri yarıp geçememeyi, {ar:وَلَن تَبْلُغَ الْجِبَالَ طُولًا, tr:wa-lan tablugha l-jibāla ṭūlan, gloss:boyca dağlara erişemezsin} dağlara boyca erişememeyi söyler; aynı ayetin {ar:وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا, tr:wa-lā tamshi fī l-arḍi maraḥan, gloss:yeryüzünde böbürlenerek yürüme} buyruğu böbürlü beden tavrını adlandırır. 17:24'teki kanat ve alçaltma ise bedeni anne babaya yöneltir. Yetiştirme ailesinin artma, yükselme ve başkasından yukarıda bulunma yönündeki uzak sözlük kullanımları, 17:37'deki boy ölçüsüyle ihtiyatlı bir yankı kurabilir: yetişkinin kapasitesi kendinden doğmuş üstünlükten çok, geçmişte aldığı bakımın devamı gibi duyulur. Bu, yalnız sözlük yankısıyla kurulan bir bağlantıdır; 17:37 genel kibre de yöneliyor olabilir ve 17:24'teki yetiştirme fiili dağa fiziksel erişmeyi anlatmaz. Bu sınırlı yankı, bakımın verdiği kapasiteyi kendinden kaynaklanan üstünlük yerine alınmış desteğin izi olarak duyurur.

Başka dikey sahneler, odaktaki bakım içindeki küçüklüğü farklı ilişkilerle karşılaştırır. 26:4'te bir işaret karşısında boyunların eğilmesi bu karşılaşmaya verilen bedensel karşılığı, 56:3'te alçaltma ile yükseltmenin yan yana gelişi iki yönlü dikey değişimi duyurur. 27:37'de küçüklük zorla aşağılanmayla birlikte görünür; bu, 17:24'ün {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} diye andığı çocuklukla aynı ilişki değildir. Bu ayetler burada tek bir olay dizisinin aşamaları olarak değil, dikey hareketin ayrı bağlamları olarak karşılaştırılır. 26:18'de yetiştirilme hatırası hak iddiasına çevrilirken 17:24'te aynı hatıra merhamet duasının dayanağıdır; bu karşılaştırma, odaktaki geçmiş bakımı sahiplik ya da borç talebi değil, dua zemini olarak belirginleştirir.

Kanadın koruyucu çağrışımına, bir şeyi erişilir kılma imgesi de eklenir. 76:14'te {ar:وَذُلِّلَتْ قُطُوفُهَا, tr:wa-dhullilat quṭūfuhā, gloss:meyve salkımları erişilebilir kılınmıştır} meyve salkımlarını yakına ve ele erişir hâle getirir; aynı fiil alanının başka kullanımları engeli ya da direnci azaltarak su yolunu açma veya bineği kolaylaştırma gibi ayrı maddi sonuçlara uzanır. 17:24'teki {ar:ٱلذُّلِّ, tr:adh-dhull, gloss:alçalış ve yumuşaklık} isim biçiminde kanadın niteliğini kurar; 76:14'teki ayrı edilgen fiil biçimi ise erişilebilir kılmayı anlatır. Bu sözlüksel yakınlık biçim özdeşliği değildir. 76:14'teki yaklaşan gölge ve ele erişen meyve, odaktaki kanadın bakım ve sığınağı ebeveynlere yaklaştıran davranış gibi duyulmasına somutluk katar.

15:88'de ve 26:215'te kanadın indirilmesi aile dışındaki özen ilişkilerine, sırasıyla müminlere ve izleyici müminlere doğru yönelir; bu kullanımlar koruyucu imgenin topluluk bağlamındaki kapsamını gösterirken 17:24'ün alıcılarını değiştirmez. 8:61'de barışa karşılıklı yönelme, alçalmanın yalnız aşağıda duruşu değil, birine doğru yönelişi de düşündürebileceği ayrı bir temas sunar. Bu bağlantı yalnız yöneliş benzerliğidir: 17:24'te barış müzakeresi veya ebeveynlerin başlattığı bir girişim yoktur ve {ar:لَهُمَا, tr:lahumā, gloss:ikisi için} alıcıları iki ebeveyn olarak sabitler.

Ebeveyn bakımının daha uzun zaman çizgisi 31:14 ve 46:15'te başka kişilerin anlatılarıyla açılır. 31:14 annenin çocuğu güçlük üstüne güçlükle taşımasını, iki yıl süren sütten kesmeyi ve anne babaya şükrü anar. 46:15 taşıma ve doğum güçlüğünü, gebelik ile sütten kesmenin toplam otuz ayını, tam güce erişmeyi ve şükrü birlikte verir. Bu ayrı evreler 17:24'teki {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} hatırasını tek bir iyilik anı değil, bağımlı dönem boyunca süren destek olarak duyurabilir; {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} bu bağlantıda yaş ve bağımlılık alanını belirginleştirir. Bu anlatılar başka kişiler ve şartlara aittir: 17:24 gebelik, doğum, sütten kesme ya da kesin bir yaş sıralaması vermez. Karşılaştırma, odaktaki konuşanın geçmişini bu evrelerle doldurmadan, hatırlanan bakımın daha uzun zaman çizgisini açar.

## Merhametin uzak yankıları

Karşılaştırma, 17:24'te anne babayla merhamet dileğinin özgül biçimde eşleşmesini belirginleştirir. 23:118'deki {ar:وَقُل رَّبِّ ٱغْفِرْ وَٱرْحَمْ, tr:wa-qul rabbi ighfir wa-rḥam, gloss:de Rabbim bağışla ve merhamet et} çağrısı bağışlanma ve merhamet ister, anne babayı anmaz; 14:41 ve 71:28'de anne babaya bağışlanma dilenir, merhamet değil. 17:24 ise Allah'tan merhamet görmeleri istenen iki kişiyi açıkça anne baba olarak belirler.

17:26'daki yakının hakkı, merhamet dileğinin akrabalık yönünü bağımsız biçimde tetikler: {ar:ذَا الْقُرْبَىٰ حَقَّهُ, tr:dhā al-qurbā ḥaqqahu, gloss:yakına hakkını ver}. Odaktaki {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} etkin merhamet isteği olarak kalırken aynı sözcük ailesindeki {ar:رَحِم, tr:raḥim, gloss:akrabalık bağı / rahim} yakın ve kalıcı soy bağını da adlandırabilir. Bu yankı, duruşun yararlanıcısı {ar:لَهُمَا, tr:lahumā, gloss:ikisi için} ve duanın ikil nesnesi {ar:هُمَا, tr:humā, gloss:ikisini} aracılığıyla aynı iki ebeveyne bağlanır. Böylece dua daha geniş bir bakım ağı içindeki yakınların hakkıyla da duyulabilir; akrabalık çağrışımı etkin merhamet isteğini soy bağıyla sınırlamaz.

Sure başındaki açılış basmalası (17:0), odaktaki merhamet dileğini surenin başında Allah'ın merhamet adlarıyla anıldığı bir çerçeveye yerleştirir: {ar:بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ, tr:bismi llāhi r-raḥmāni r-raḥīm, gloss:Rahmân ve Rahîm Allah'ın adıyla}. Açılıştaki {ar:الرَّحْمَٰنِ الرَّحِيمِ, tr:ar-Raḥmān ar-Raḥīm, gloss:Rahmân ve Rahîm} ile odaktaki {ar:ٱرْحَمْهُمَا, tr:irḥamhumā, gloss:ikisine merhamet et} aynı sözcük ailesinden gelir; etkin esirgeme dileği böylece başta anılan ilahî merhamet kaynağına yönelir. Bu sözcük bağı isteği gerçekleşmiş bir sonuç gibi sunmaz ve insanın şefkatini Allah'tan dilenen eylemle özdeşleştirmez.

39:6'da annelerin rahimlerinde yaratılışın bir hâlden diğerine geçmesi, aynı kök ailesindeki ayrı {ar:رَحِم, tr:raḥim, gloss:akrabalık bağı / rahim} sözcüğün döl yatağı anlamını açar. 17:24'teki {ar:ٱلرَّحْمَةِ, tr:ar-raḥmah, gloss:merhamet} ise ebeveynlere dönük şefkati anlatmayı sürdürür. Kanat imgesi {ar:جَنَاحَ, tr:janāḥa, gloss:kanat}, {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} hatırası ve {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} çocukluk hâli birlikte düşünüldüğünde koruyup taşıma ufkunu çocukluk öncesine doğru uzatabilir. Bu uzak benzetme 17:24'te gebelik ya da doğum anlatıldığı anlamına gelmez; merhamet “rahim” anlamına dönüşmez ve ikil biçimler iki ebeveyni korur.

Aynı kök ailesinin daha uzak bir sözlük kullanımı, döl yatağının ağrımasını ya da hastalanmasını, bazı kullanımlarda doğum sonrasında görülen bir bozukluğu adlandırır. {ar:رَبَّيَانِي, tr:rabbayānī, gloss:beni yetiştirdiler} ile {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} bakım geçmişine bağımsız biçimde dönerek yalnızca keşif niteliğinde bir beden maliyeti yankısı kurar. Bu bedensel anlam merhamet dileğine yüklenmez; 17:24 ağrı, doğum ya da doğum sonrası bozukluk anlatmaz. Yetiştirme fiili olağan ebeveyn bakımını bildirir ve besleyip geliştirme yönü beden maliyeti imgesinden süreğen bakıma dönüşü sağlar; bu sözlük yankısı iki ilişkiyi anlamca özdeşleştirmez.

En uzak çağrışımlardan biri, 17:24'teki {ar:صَغِيرًا, tr:ṣaghīran, gloss:küçükken} çocukluk küçüklüğünü, küçük ile büyüğün kayda geçtiği daha geniş ölçekle yan yana getirir. 10:61 ve 34:3'te zerre ağırlığındaki şeyin, ondan küçüğün ya da büyüğün gizli kalmaması açık kayda bağlanır; 54:53'te {ar:وَكُلُّ صَغِيرٍ وَكَبِيرٍ مُّسْتَطَرٌ, tr:wa-kullu ṣaghīrin wa-kabīrin mustaṭar, gloss:her küçük ve büyük şey yazılıdır} denir. Bu bağımsız ifadeler çocukluk küçüklüğünü küçük-büyük ve kaydedilme ufkuna taşır; çocukluk daha geniş ölçekte kaybolmayan bir parça gibi duyulur. Bu yalnızca yankıdır: 17:24'teki küçüklük atom ya da nicelik değil, yaş ve bakım içindeki bağımlılıktır.

</source_prose>
