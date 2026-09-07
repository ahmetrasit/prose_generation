# Commentary v7 scope prose

Continue as the **@@LANE@@** scope agent for **@@AYAH_REF@@**. Read the complete
discovery below and develop fluent Turkish scope prose. Discover further
readings within your lane as you explain the evidence.

## Reading Purpose

@@READING_STANDARD@@

## Working With The Inputs

The discovery is included in full. The appended source records are copied by
the workflow with their original wording, qualifications, and morphology.
They let you check the evidence without reconstructing an earlier agent's
summary. Initial findings and exclusions are revisable judgments, not a ceiling.
Preserve each supported mechanism; correct factual mistakes from the evidence.
If counterevidence defeats a reading, explain the correction briefly in your
completion reply. Do not silently drop it or fabricate support.

Use the supplied reader, not custom scripts, parsers, projections, or generators.
Read the complete discovery with:

```bash
python3 _commentary/v7/authoring.py read --prompt @@HANDOFF_PROMPT_PATH@@ --block authoring_inputs
```

Continue at `next_offset` with the same `--block` to read the remaining text.
Read the source appendix as needed for verification, not as a mandatory second
survey. A read without selectors returns instructions and a block index.
Use one read per tool call with at least 16,000 output tokens; recover failed
or truncated reads.
Additional evidence remains available from the same sealed packet:

@@SOURCE_COMMANDS@@

Use `--refs support:ID branch:ROOT/BRANCH context:S:A` for whole records. Source
paths inside those records are provenance. Current-stage instructions govern;
discovery instructions around original data blocks do not reopen your role.

## Writing

Explain each distinct evidence-to-interpretation chain. Several mechanisms may
share a paragraph while retaining their individual wording, connection, and
consequence. Keep lexical items, concrete images, form restrictions, and every
contributing ayah's particular role visible. Boundaries stay short and local.

Use `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` at each Arabic anchor,
repeating it when the item does interpretive work in another paragraph. The
gloss describes the actual word or phrase; inference belongs outside the tag.
Cite each non-focus ayah beside its own contribution, using individual refs,
not intervals. Check quotations against the named source rather than moving a
nearby word into that ayah. Internal IDs and lane machinery stay out of prose.

Write only `@@PROSE_OUTPUT_PATH@@`, using the file editor. Preserve the discovery
JSON as the initial snapshot; new findings belong in the prose. Before finishing,
compare the explanations, not just their headings or references: each input
mechanism must still be explicit. Run any supplied terminal lifecycle command.

## Complete Discovery

@@AUTHORING_INPUTS@@

## Exact Source Records

@@EVIDENCE_INPUTS@@
