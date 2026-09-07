# Commentary v7 editorial handoff

Continue as the same live consolidator for **@@AYAH_REF@@**. Improve the
commentary's Turkish and the explicitness of its readings. Develop further
readings whenever attention to the evidence reveals them.

## Reading Purpose

@@READING_STANDARD@@

## Editorial Work

Edit the existing explanations in place as your default. Improve wording,
cadence, order, and repetition while retaining their factual anchors. Reorganize
where it clarifies relationships. Merge explanations only if their evidence,
connection, and interpretive consequence are equivalent; a similar conclusion
does not make different mechanisms redundant. There is no shortening target.

The complete first pass and original authoring inputs are below, followed by
exact source records. Use them to restore explanations lost in consolidation
and verify factual changes. Source facts control earlier wording. A lexical
form restriction may qualify a literal meaning while leaving the resonance
available. If counterevidence defeats a reading, briefly explain that correction
in your completion reply; do not silently remove it or fabricate support.

Preserve the specific attested lexical item, its relation to the passage,
independent contact, and interpretive change. A generic source-image description
does not preserve a lexical connection. Keep ordinary meaning separate from
inference, with short boundaries where needed. New readings need the same
explanation as incoming ones.

Use the supplied reader, not custom scripts, parsers, projections, or generators:

```bash
python3 _commentary/v7/authoring.py read --prompt @@HANDOFF_PROMPT_PATH@@ --block authoring_inputs
```

Continue at `next_offset` with the same `--block` to read the first pass and
scope inputs. Consult source records as needed for verification; no second
exhaustive source survey is required. A read without selectors returns
instructions and a block index. Use one read per tool call with at least 16,000
output tokens; recover failed or truncated reads. Additional original evidence
is in the same sealed packets:

@@SOURCE_COMMANDS@@

Use `--refs support:ID branch:ROOT/BRANCH context:S:A` for whole records. Source
paths within records remain provenance; this editorial prompt governs the task.

Use helpful Turkish level-2 subtitles and paragraph-local
`{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` tags. A gloss states the
actual word's meaning; inferred scenes belong outside it. Cite individual
non-focus ayat beside their own contributions. Verify quotations against the
stated source rather than transferring a neighboring ayah's wording. Internal
IDs and workflow machinery stay out of reader prose.

Compare the edited explanations with the first pass and scope inputs. Restore
any missing source fact, linguistic connection, or interpretive consequence.
References, headings, and general themes alone do not establish preservation.

## Output And Format Check

Write only `@@PROSE_OUTPUT_PATH@@`, using the file editor. Create no ledger or
audit artifact. After writing, run:

```bash
python3 _commentary/v7/validate_prose.py @@PROSE_OUTPUT_PATH@@
```

Repair reported format issues and rerun at most twice. This check covers tags,
braces, placeholders, wrappers, and Arabic outside tags; it does not check
semantic preservation or quotation accuracy. Do not change findings to satisfy
it. Run any supplied terminal lifecycle command; report `attention` if format
issues remain, `completed` if they are resolved.

## Complete Authoring Inputs

@@AUTHORING_INPUTS@@

## Exact Source Records

@@EVIDENCE_INPUTS@@
