# Commentary v7 editorial handoff

Continue as the same live consolidator for **@@AYAH_REF@@**. Read the first-pass
prose, improve its clarity and Turkish fluency, and actively develop further
readings wherever close attention to the evidence reveals them.

## Reading Purpose

@@READING_STANDARD@@

## Inputs

- first-pass prose: `@@PROSE_INPUT_PATH@@`

@@AUTHORING_INPUTS@@

## Original Evidence

@@EVIDENCE_INPUTS@@

Earlier findings and exclusions are revisable judgments. Check source facts
against the original evidence, not just an earlier agent's wording. Preserve
every supported reading from the first pass and its inputs, including findings
first developed in scope prose or consolidation. Correct factual mistakes while
preserving supported interpretations. If concrete counterevidence defeats a
claim, briefly explain the correction and its basis in your completion reply;
do not silently remove it or fabricate support. A form restriction may limit
literal meaning without defeating contextual resonance.

## Editorial Contract

- Make each reading's particular evidence, connection to the passage, and
  interpretive change explicit. Recover any supporting link compressed out of
  the first pass. Develop new readings just as fully.
- Improve wording, cadence, order, proportion, and repetition. No sentence is
  verbatim-immutable. Coherence must preserve the reasoning behind every
  reading, not absorb several readings into a general statement.
- Preserve concrete images, pathologies, secondary senses, repeated actions,
  spatial relations, and before/after shifts. Keep the ordinary sense
  recoverable and explain the bridge to each additional reading. Boundaries
  should be brief, specific, and attached where needed.
- Use helpful Turkish level-2 subtitles, for example `## Taşın Hafızası`.
  Do not add generic `# PROSE`, `=== PROSE ===`, or XML wrappers.
- Preserve `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` at every Arabic
  interpretive anchor. Tags are paragraph-local: repeat the full tag when the
  item does interpretive work again in a new paragraph. Do not substitute plain
  Arabic/transliteration, add QAC IDs, or invent another tag shape.
- Write Turkish prose; translate English analytic terminology. Internal IDs,
  lane names, and QAC coordinates stay out of reader prose.
- Put every non-focus ayah reference beside the interpretation it supports,
  usually in parentheses such as `(29:41)`. List every contributing ayah, such
  as `(29:17, 29:25)` or `(1:6, 1:7)`, rather than intervals or vague phrases
  like "sûrenin ilerleyen yerinde". Cite a host prefatory basmala used as
  context as `(S:0)`; use `(1:1)` when Al-Fatiha 1:1 itself is the source.

Compare the result with the first-pass prose and its inputs. Each supported
reading must retain its explicit evidence, connection, and consequence. Check
new readings to the same standard, Arabic anchors for paragraph-local tags,
and contextual claims for references that actually support their wording.

## Output and Mechanical Validation

Write exactly one nonempty Markdown prose file:

- prose: `@@PROSE_OUTPUT_PATH@@`

Modify no other files and create no audit artifacts. After writing, run:

```bash
python3 _commentary/v7/validate_prose.py @@PROSE_OUTPUT_PATH@@
```

For nonzero results, repair the reported mechanical format issues in this file
and rerun, at most twice. These repairs concern tags, braces, placeholders,
wrappers, and Arabic outside tags; they are not a reason to alter findings.
After two cycles, leave the prose in place and report remaining issues. Run any
terminal monitor lifecycle command supplied by the orchestrator; report
`attention` if mechanical issues remain, `completed` only if validation passes.
Do not launch another agent or write a validation report.

<editorial_instructions>
@@EDITORIAL_INSTRUCTIONS@@
</editorial_instructions>
