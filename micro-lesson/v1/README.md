# Micro-lessons v1

One or two Turkish sentences teaching one coherent observation while a reader
reads an ayah or surah commentary. Discover all worthwhile opportunities; ranking
controls display, not discovery. A single observation may teach several related
concepts from the same or different categories.

This is a linguistic authoring workflow: prepare the passage and evidence, write
through three perspectives, then edit and assemble. No runner, hashes, automated
scoring, validation stages, quotas, or extra review agents are part of production.

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
