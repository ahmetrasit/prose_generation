# Edit and assemble the three engines

Read common.md. Inputs: original paragraphs and their relevant evidence packet,
full ontology access, all three engine results, and existing page lessons/keys when
revising. Return `schemas/page-output.schema.json`.

This is the editorial step. Check each candidate against its expression, dictionary
branch or other source, and what the beginner will understand. Smooth Turkish and
combine supported wording; do not invent new linguistic claims to resolve gaps.

Preserve every distinct worthwhile point. Merge only genuinely equivalent teaching
observations, keeping one or two short sentences. Shared concepts, roots or words
are not duplication. A single lesson can teach multiple concepts from any categories.
Retain the concept annotations supported by the final wording; remove annotations
whose teaching disappeared. Never force a single primary objective or inherit
every ancestor. Omit unused optional fields.

Read adjacent paragraphs for repetitions of the same point on the same occurrence.
Keep the best local attachment; retain another example when it contributes an actual
contrast or application. For merges, choose an existing survivor where possible,
retain its key/ID, and record the other full IDs in `merged_from`. A new lesson's ID
is `<page_id>:<paragraph_id>:<engine>:<key>`, with the best fitting engine as owner.
Engine ownership does not constrain annotations. Do not change identity for a new rank.

Rank within each paragraph for a beginner: accessible and locally useful first,
needed foundations before demanding explanations, reusable points before obscure
ones when otherwise comparable. Use actual prerequisite demands and level, never
engine order or graph depth. Array order follows consecutive ranks starting at 1.
`rank_reason` is optional for an editorial choice worth explaining.

Resolve prerequisites against the final wording. Remove unnecessary catalog
prerequisites, including material now explained within the lesson. An introduced
concept must not be required. Keep only justified reminder IDs; requires takes
precedence over helped_by for the same concept. Do not remove genuine assumptions
merely to make a lesson appear easy.

Move candidates with unresolved central claims into `deferred`, retaining their
anchor and exact open question; they must not also remain displayable. Notes alone
do not clear a disputed lesson. A faithfully qualified, supported alternative is
different from a missing analysis. Preserve useful drafts for exceptional catalog
gaps. If the evidence rejects an idea, keep a short rejection note instead of
pretending that more waiting will resolve it.

Preserve deferred records, proposals and input notes with engine attribution. For
every missing engine/paragraph pair record what is missing. `completed_engines`
includes an engine only when it returned every assigned paragraph, including empty
ones. Partial input can produce useful output but never a claimed complete pass.

The app may adapt rank through actual learner knowledge and lesson exposure. No
annotation, ancestor, display event or dismissed reminder automatically grants
mastery. Learned general concepts do not hide unseen lexical applications.
