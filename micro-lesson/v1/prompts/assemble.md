# Edit and assemble the three engines

Read common.md. Inputs: original paragraphs and their relevant evidence packet,
full ontology access, all three engine results, and existing page lessons/keys when
revising. Return `schemas/page-output.schema.json`.

This is the editorial step. Check each candidate against its expression, dictionary
branch or other source, and what the beginner will understand. Smooth Turkish and
combine supported wording; do not invent new linguistic claims to resolve gaps.
Own paragraph attachment, beginner wording, annotations, prerequisites, repetition
and the reading for missed opportunities here. The later correctness review assesses
linguistic truth; it does not finish these editorial decisions.

As you edit, reread the actual teaching sentence beside its source: does the quoted
span include the particle carrying its meaning, does each stem/suffix contribute
what is claimed, and does the selected branch/gloss apply here? Then read it as a
beginner who has not seen another lesson: what can they now recognize or understand,
and what in the sentence lets them do it? A particle lesson must explain its local
meaning contribution; “bi- ilişki kurar” and a translation of the whole phrase leave
that work to the reader. A form or ending lesson must explain the useful relation
between what is visible and how the expression is understood. Revise factual labels
and paraphrases into explanations using the available evidence. Explain unfamiliar
terms through the local example, or remove terms that add no teaching value.
“Nasb uyumu” alone gives a
beginner no usable observation; showing the shared endings can. A correct anchor,
a gloss fit label, or an engine's confidence does not settle these questions.

Preserve every distinct worthwhile point. Merge only genuinely equivalent teaching
observations, keeping one or two short sentences. Shared concepts, roots or words
are not duplication. A single lesson can teach multiple concepts from any categories.
Keep distinct lessons in a family when they teach the feature's use, construction,
boundary or a Quranic contrast. Sharing bi- and the same attachment paragraph is
not a reason to collapse them into a single general statement. Supporting verses
may come from outside the prose when their teaching connection is clear.
For each retained annotation, identify the wording that teaches, reinforces or
contrasts that concept and read its catalog boundary. Remove annotations whose
teaching disappeared or was merely mentioned. Comparing different words from one
root does not itself teach polysemy of one word; naming a root does not itself teach
documented relationship versus resemblance. Never force a single primary objective
or inherit every ancestor. Make these judgments while editing; emit no annotation
justification list. Omit unused optional fields.

Read the original paragraph alongside the candidates for distinct useful opportunities
they missed, especially comparisons or prose-only verse references. When one is
apparent, ask the appropriate discovery engine for that local addition with the
relevant evidence; if the packet omitted it, correct that omission first. Resume
assembly for the affected paragraph and its neighboring repetitions. Do not invent
an observation to fill an empty list or infer exhaustive discovery from three
engines having returned the paragraph.

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
merely to make a lesson appear easy. A reminder cannot make an unexplained term
understandable within a standalone lesson. After simplifying, set level from the
remaining demands; several annotations do not by themselves make a lesson advanced.

Move candidates with unresolved central claims into `deferred`, retaining their
anchor and exact open question; they must not also remain displayable. Notes alone
do not clear a disputed lesson. A faithfully qualified, supported alternative is
different from a missing analysis. Preserve useful drafts for exceptional catalog
gaps. If the evidence rejects an idea, keep a short rejection note instead of
pretending that more waiting will resolve it.

Correct a source-settled wording or annotation error directly, keeping the lesson
ID. For a substantive correction, leave a brief paragraph note with the affected
ID, what changed and the decisive source; ordinary style edits need no log. If a
recurring misunderstanding appears, inspect other candidates using that same
construction or lexical distinction and correct only those affected. Do not rerun
unrelated engines. After assembly, the runbook's linguistic correctness review
assesses the finished lessons using review.md.

Preserve deferred records, proposals and input notes with engine attribution. For
every missing engine/paragraph pair record what is missing. `completed_engines`
includes an engine only when it returned every assigned paragraph, including empty
ones. Partial input can produce useful output but never a claimed complete pass.

The app may adapt rank through actual learner knowledge and lesson exposure. No
annotation, ancestor, display event or dismissed reminder automatically grants
mastery. Learned general concepts do not hide unseen lexical applications.
