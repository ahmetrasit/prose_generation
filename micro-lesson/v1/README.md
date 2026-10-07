# Micro-lessons v1

One or two Turkish sentences teaching one coherent observation while a reader
reads an ayah or surah commentary. Discover all worthwhile opportunities; ranking
controls display, not discovery. A single observation may teach several related
concepts from the same or different categories.

The prose can open a family of distinct lessons about a word or construction:
meaning, ordinary uses, grammatical behavior, boundaries and distinctive Quranic
applications. Relevant sourced examples may come from outside the prose's cited
ayat. Commentary stays frozen; the teaching develops the feature it introduces.

This is a linguistic authoring workflow: prepare the passage and evidence, write
through three perspectives, edit and assemble, then review the finished teaching
claims for linguistic correctness. Review returns a compact result per lesson;
corrections stay local. No runner, hashes, automated scoring, mechanical validation
stages or lesson quotas are part of production.

The default is **Sol Max** (`gpt-6-sol`, reasoning effort `max`) for all model-assisted
authoring stages. The user selected it after the 1:1 comparison; see the
[runbook's model default](RUNBOOK.md#default-model).

- [RUNBOOK.md](RUNBOOK.md): the complete authoring and display procedure.
- [ONTOLOGY.md](ONTOLOGY.md): scope, hierarchy, multiple annotations, attachment
  rules, and coverage against the source inventories.
- [catalog/INDEX.md](catalog/INDEX.md): compact navigation to every concept.
- [catalog/ontology.json](catalog/ontology.json): concepts, definitions, boundaries,
  multiple topic memberships, broader concepts, learning relations, introductions,
  and examples. The original C001–C036 identities are preserved.
- [catalog/curriculum.json](catalog/curriculum.json): seven routes in 33 teaching modules covering the
  catalog, with overlap where a skill belongs to more than one route.
- [catalog/messages.tr.json](catalog/messages.tr.json): two shared reminder
  templates; no repeated per-concept messages.
- [prompts/](prompts/): common, grammar, semantics, mapping, and assembly instructions.
- [prompts/review.md](prompts/review.md): correctness of the finished lesson's
  forms, grammar and meaning; compact `ok` / `flag` / `uncertain` results.
- [schemas/](schemas/): a shared lesson contract and engine/page/learner contracts.
- [examples/README.md](examples/README.md): a worked passage, all three engine
  outputs, assembled lessons, and editorial decisions, plus an evidence-gap case.

## Identities and learning

`ML:C017` identifies the root/pattern concept. `ML:R017:requires` is its dismissible
reminder. `<page>:<paragraph>:<engine>:<key>` identifies a particular lesson.
Keywords are readable search handles for concepts; emit their stable concept IDs.
Dictionary root/branch/lexical-unit IDs identify the particular lexical material.
These identities serve different purposes and are never interchangeable.

A lesson's `concepts` contains any relevant direct annotations with roles
`teaches`, `reinforces`, or `contrasts`. Several `teaches` annotations are allowed;
there is no single primary objective and no requirement to stay inside one category.
Do not add every ancestor or every concept merely mentioned in the lesson.

Seeing a lesson does not establish mastery of any annotation. Learning a parent,
child, or sibling does not establish mastery of the others. Learned concepts silence
their reminders; they do not hide unseen lexical examples. Lesson exposure and
message dismissal remain separate.

## Scope and readiness

The workflow has completed a full 1:1 pilot. The preparation, shared authoring,
grammar and assembly instructions now incorporate its concrete findings: retain
meaning-bearing particles, distinguish stems/suffixes and lexical identities,
explain unfamiliar terms, attach concepts to the actual teaching, resolve prose-only
verse references, and present dictionary evidence compactly. Local error repair is
part of the assembly/resolution steps in the runbook. The subsequent linguistic
correctness review is now specified; its prompt has not yet been run.

An [edited Sol Max example](tests/1-1-sol-high-vs-max/sol-max-edited/README.md)
corrects eight identified lesson issues while preserving the original pilot.
This is ready for continued linguistic calibration; the revised instructions have
not yet been tested on varied passages, so readiness for generation at scale is
not established. See the [pilot findings](tests/1-1-sol-high-vs-max/sol-comparison.md)
and [measured usage/file sizes](tests/1-1-sol-high-vs-max/usage-and-size.md).

The catalog is authored across the full defined reading scope from day one; it is
not a seed that ordinary production must expand. Scope includes Quranic Arabic
reading distinctions, morphology, syntax, discourse, lexical semantics, and
Arabic–Turkish gloss interpretation. The dictionary supplies the lexical instances.
Rare evidence disputes can still be deferred. New concepts are exceptional editorial
changes, not the normal way to finish a lesson. See ONTOLOGY.md for the boundaries
of this completeness claim and the linguistic coverage map.

The current authoring contract is 1.1. It replaces the seed's single `objective`
with multiple `concepts`, drops compulsory `depth` and rank explanations, and
resolves reminders from templates. Existing seed examples have been rewritten.
When importing earlier artifacts, translate their objective/reinforces/contrasts
into typed annotations and review their wording; do not silently treat them as 1.1.
