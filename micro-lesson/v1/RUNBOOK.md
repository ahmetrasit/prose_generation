# Authoring workflow

## Default model

Use **Sol Max**: model `gpt-6-sol`, reasoning effort `max`, for grammar,
semantics, mapping, assembly and linguistic correctness review, and for
model-assisted evidence preparation.
This is the user's selected workflow default following the
[1:1 pilot](tests/1-1-sol-high-vs-max/sol-comparison.md).
A different model or effort requires an explicit user instruction for that run.

## 1. Prepare the passage and its evidence

Give the page a stable ID and its prose paragraphs stable IDs. Include headings and
neighboring paragraphs as context. Numbered v16 augment additions belong to their
parent paragraph; make that grouping explicit. Keep the original commentary unchanged.
Choose an actual reading text, not an execution log or an error saved as Markdown.

For each paragraph supply the focus ayah and the ayat it quotes, cites, or clearly
discusses, with exact Arabic and available word/morpheme analysis. Resolve implicit
references by reading the prose, not just its numeric citations: “the last word
of the seventh ayah” in a Fatiha discussion points to 1:7. Record the resolved
reference with that paragraph; if ambiguous, name the question rather than guess.
Do not pull in every ayah in a surah or automatic neighbors.
Include dictionary quotations actually discussed, clearly distinguished from ayat.

Use a small Markdown packet, as in [examples/input.md](examples/input.md). It needs
the paragraph, its local expressions, relevant analysis and compact source locators;
there is no input schema or mechanical preparation gate. All engines share the same
passage and resolved word identities. They can read different relevant evidence
sections without copying unrelated dictionary material into every context.

Sources, relative to this repository root:

- Commentary: `_commentary/v16/out/` ayah readings and surah `images.md`, or an
  explicitly selected existing numbered enrichment input.
- Arabic/morphology: `../quran-data/data/text/quran-uthmani.tsv`, the QAC database
  under `../quran-data/data/morphology/`, or existing exported word packets.
- Root identity: reviewed bindings and alternatives under `../quran-data/data/bridges/`.
  Follow `../dictionary/AGENTS.md` for dictionary root lookup, including supplemental
  headwords when appropriate. Similar Latin spelling is not identity.
- Dictionary: finalized `../dictionary/entries/tr/<root-envelope>.json`; reviewed
  concept/contextual/lexical gloss profiles in
  `../dictionary/v2/gloss_generation/results/tr/<root-envelope>.json`.
  If the finalized entry is absent, the gloss result's `source_entry.path` can locate
  its upstream entry under `../dictionary/`. Preserve any unresolved editorial
  qualification from that entry/review; an available file is not proof that its
  disputed claim is settled. A missing final export is not absence of a dictionary.
- Existing `../quran-data/data/dictionary/tr/*_entry.json` exports may be used when
  they retain the required fields for this occurrence. The abbreviated v16
  `dictionary.md` projection alone is insufficient for mapping.

Carry the selected branch's complete **semantic content**: Arabic definition and
boundaries, identity qualifications, lexicalization conditions, relevant root
profile, lexical-unit bindings, gloss applicability, excluded glosses, useful
neighbor distinctions, and per-gloss error profiles. Consult other branches when
the teaching comparison needs them. Do not copy build metadata, hashes, rendering
apparatus, or unrelated occurrence lists.

Present this semantic content once per relevant branch, with source locators;
do not repeat substantially identical upstream, finalized and reviewed projections.
Keep any meaningful differences and their provenance explicit. Leave full source
files accessible for consultation, rather than pasting them into every engine's
context. Select additional branches for actual paragraph uses or comparisons,
not simply because they belong to a root already mentioned.

The encyclopedia `error_profile` supplies `fit`, `preserves`, `loses`, `adds`, and
`collision`. Compact reviewed glosses use `error` with `fit`, `loses_facet_ids`,
`adds`, `collision`, and `reason`; interpret facet IDs with their source definitions
and roles. These are two source shapes for linguistic evidence, not two authoring
passes. A recorded loss can concern a specialization or source variant that is not
required in this occurrence. Never copy a fit label directly into a verdict on the ayah.

Name the exact gloss being discussed. Also include the commentary's Turkish phrase
when relevant. Dictionary concept glosses explain the branch; contextual glosses
serve a particular use. Neither is automatically the wording of the commentary.

Record missing evidence as a specific question. Its affected opportunity can be
deferred while the paragraph's other lessons proceed.

## 2. Discover through three linguistic perspectives

Each engine reads `prompts/common.md`, its own prompt, ONTOLOGY.md, and the same
passage packet. Start with `catalog/INDEX.md` for the complete concept inventory;
read the full definitions, boundaries and relations in `catalog/ontology.json`
for candidate attachments. Consult introductory examples when setting prerequisites.
No engine is restricted to concepts from its namesake category.

The engines are grammar, semantics, and mapping. They may be run sequentially or
concurrently by an authorized operator using the model default above; this workflow
does not launch agents. Several paragraphs can share a call. Each engine returns
`schemas/engine-output.schema.json`, including each assigned paragraph even when
it found no lesson. Empty output needs a brief reason, not a made-up observation.

Discover without a page quota. Each lesson must have independent learning value,
one coherent point, and one or two short Turkish sentences. Several ontology
annotations can describe that point. Do not split one explanatory contrast simply
to make one lesson per keyword. Conversely, an unrelated second point is a new lesson.

When revising an existing page, supply its prior lessons and keys. Retain keys for
wording edits, and give a changed teaching point a new key. Do not derive identity
from rank. Retain paragraph IDs on resegmentation or record an explicit old/new map.

## 3. Edit, merge and rank with the passage visible

Give `prompts/assemble.md` the original packet, ontology access, all three outputs,
and previous page output if present. Assembly is the editorial step, not another
discovery engine. It returns `schemas/page-output.schema.json`.

Read each proposed lesson against its expression and supporting source. Retain
distinct observations, including several applications of the same concept. Merge
only if the resulting lesson loses no teaching value and remains coherent and short.
Keep all justified annotations from the retained wording, regardless of category
or engine; never blindly union tags from removed prose. Record absorbed IDs only
when a merge occurred. Preserve an existing published survivor's ID when possible.

During that reading, check the learner sentence's quoted span and word parts,
the local applicability of its branch/gloss, and whether a beginner can understand
its terms. Then judge the annotations against the final wording. Complete Arabic
in an anchor cannot compensate for a dropped negative particle in the lesson.

Read across neighboring paragraphs for repetition. When the same observation on
the same occurrence is repeated, attach the survivor to the paragraph where it
helps most. Keep a second occurrence when it supplies a meaningful application or
contrast. Ontology overlap alone is never grounds for merging.

Rank by accessibility, local relevance, useful foundations, and reuse. Use the
lesson's level 0–4 alongside its actual assumed knowledge; ontology position is
not a difficulty score. The array order is display order, with consecutive ranks
inside each paragraph. A rank explanation is optional for a non-obvious decision.

An unresolved conflict affecting a lesson's claim moves that lesson out of the
displayable list into `deferred`. A note alone does not clear it for display.
Qualified scholarly alternatives may be taught when the qualification fits the
lesson and the evidence supports it; missing evidence is not an alternative analysis.
Preserve engine notes and identify any missing engine/paragraph combination.
`completed_engines` lists only engines covering every assigned paragraph, even
where their lesson lists are empty. Never label a partial example a complete pass.

## 4. Review the finished lessons for linguistic correctness

Use [prompts/review.md](prompts/review.md) in a fresh context after assembly.
One review run reads every displayable lesson in the ayah-based file. Supply the
finished output and access to the relevant Arabic, morphology and lexical evidence;
consult commentary only when needed for context. Earlier engine drafts and author
reasoning are unnecessary.

The review assesses the truth of the lesson's linguistic claims: forms, readings,
grammatical assignments, meanings, derivations and generalizations. It does not
audit generation procedure or reassess ontology placement, style or coverage.
Return a compact line per lesson ID: `ok`, `flag` with correction and linguistic
basis, or `uncertain` with the precise open question. Save it beside the page as
`linguistic-review.md`; the reviewer leaves the lesson file unchanged.

Repair flagged lessons through step 5 and recheck only the changed lessons with
the same prompt. Resolve uncertain claims before display, or move the affected
lesson to `deferred`. A newly completed deferred lesson also receives this review.
Keep the current result for each lesson in the same review file. An `ok` means no
error was found against the available evidence, not a guarantee of correctness.

The review prompt has been authored; it has not yet been run on the pilot outputs.

## 5. Resolve only what remains open

Every deferred record retains its anchor, opportunity, blocker, and a concrete
question to resolve. For a catalog gap, also preserve any supported draft and a
short proposed concept definition with plausible parents. Do not invent an ID.

- Missing evidence: obtain the missing source or binding, then rewrite only the
  affected candidate with that evidence.
- Conflicting evidence: settle or faithfully qualify the exact disagreement;
  keep unresolved claims out of the displayed lesson.
- Exceptional catalog gap: edit the catalog definition, hierarchy and introductory
  example, then attach and finish the saved draft.

Reassemble only affected paragraphs, checking any repetition with their neighbors.
An idea that evidence disproves is rejected in an editorial note, not kept forever
as a pending claim. Keep repair local; no status database or rerun of all engines
is needed. The correctness review in step 4 checks the repaired teaching claims.

The same local repair applies to errors found after assembly. For a source-settled
error, correct the lesson directly, preserving its ID, and leave a brief paragraph
note naming the lesson, correction and source. If its central claim is unresolved,
defer it; if disproved, reject it. Inspect other lessons using the same construction
or lexical distinction when the error suggests a repeated misunderstanding. Update
the relevant prompt only for a reusable lesson from the error. Regenerate any
reader-facing rendering of the affected page from the corrected output. Keep
benchmark originals intact and make their editorial corrections separately.

## Learning and reminders in the application

`concepts` is the lesson's many-to-many annotation list. The app may group by any
topic/ancestor and prefer lessons with familiar prerequisites. It never treats
all annotated concepts as mastered because the lesson was seen.

Use `requires` only for knowledge the actual explanation assumes; `helped_by` is
optional useful context. Catalog relations are suggestions to inspect, not lists
to copy. Rewrite needlessly technical wording before adding prerequisites. Remove
catalog prerequisites made unnecessary by the explanation or transliteration.
An introduced concept must not also be required by that lesson. A reinforced
concept can be prerequisite only when knowledge beyond the brief repetition is
actually assumed. Contrasted concepts are not automatically prerequisites.

Outputs use reminder IDs only: C017 resolves to R017 with either `requires` or
`helped_by`. Show at most the nearest useful unlearned introduction at a time,
including its example; allow the reader to follow its own prerequisites. Never
dump every ancestor or turn a reminder into a hard access gate. If both relations
were proposed for a concept, keep only the stronger justified relation.

The shared message templates interpolate the concept's Turkish label. Muting
`ML:R017:requires` mutes that message only. Marking C017 learned suppresses both
its reminder variants; neither action changes the other concept states. Missing
concept state means unseen. `seen`, `learning`, and `learned` remain distinct.
The reader can explicitly change a concept state and undo it; exposure alone
never establishes mastery.

Skip individual seen or hidden lessons when requested. Never hide an unseen
lesson merely because some or all of its broad concepts are learned: a new root,
branch, construction or contrast can still teach something. Keep all lessons
available in review. No quiz, scoring system, or spaced-repetition engine is
required by this authoring workflow.

## Linguistic calibration

During the first pages, compare a few finished paragraphs with an editor's own
reading: what useful observations were missed, which repeat each other, and what
a beginner still cannot follow. Read for faithful Arabic, meaningful annotations,
natural Turkish and actual prerequisite need. Apply those judgments inside the
existing authoring/assembly steps. There is no automated completeness claim,
validation pipeline, numeric pass score, or obligation to find a fixed count.
