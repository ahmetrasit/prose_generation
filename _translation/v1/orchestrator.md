# Cold translation orchestrator

You are the sole controller for one translation-layer job. This runbook is
complete: do not rely on prior conversation or undocumented project knowledge.
Perform deterministic preparation and checking yourself. Delegate the
linguistic writing to exactly one fresh worker.

## Required assignment

Resolve these values from the task that sent you here:

- `surah`: integer, for example `1`;
- `language`: BCP-47 target-language tag, for example `en`;
- `output`: optional output path. If omitted, use
  `_translation/v1/output/{language}/s{surah3}.json`.

Run from the `prose_generation` repository root. Read and write only this
repository. Sibling repositories are input-only.

## Ownership

The controller:

- prepares the compact input bundle;
- launches and retains one cold writer;
- runs the mechanical output check; and
- reports the resulting path or exact failure.

The writer alone authors occurrence glosses, card glosses, and fluent
translation wording. The controller must not silently rewrite linguistic
content.

Use a fresh agent with no inherited conversation context. Request GPT-5.5 with
high reasoning effort. Prefer the runtime's native spawn operation when it can
select those settings; otherwise use its ephemeral agent runner. Tell the
writer not to delegate.

## 1. Prepare

Format the surah as three digits (`1` becomes `001`) and run:

```sh
python3 _translation/v1/tools/build_bundle.py \
  --surah <surah> \
  --language <language>
```

This must produce:

```text
_translation/v1/input/<language>/s<surah3>.json
```

If preparation fails because the primary-anchor seed or dictionary branch
evidence does not exist, stop and report that exact missing prerequisite. Do
not invent branches or lexical evidence.

If the intended output already exists, run the check in step 3. A passing
existing output is complete. Do not replace it unless the assignment
explicitly authorizes replacement.

## 2. Launch one cold writer

Read `_translation/v1/prompt.md` and replace its three placeholders with
concrete absolute paths:

- `<input-bundle>`;
- `<output-schema>`; and
- `<output-path>`.

Spawn one fresh worker with no inherited conversation context and send only
that rendered prompt. Do not prepend instructions, summarize the task, or
provide conversational context. The prompt itself is the complete linguistic
handoff.

The writer must see only the rendered bundle and schema, not earlier
translations. If the runtime cannot restrict repository reads, stage those two
files in an otherwise empty temporary working directory and copy the completed
artifact to `output` afterward.

Wait for that worker to finish. Do not launch competing writers for the same
surah-language pair.

## 3. Check the returned file

Run:

```sh
python3 _translation/v1/tools/check_output.py \
  --surah <surah> \
  --language <language> \
  --output <output>
```

This check is mechanical only. It verifies the final shape, locked identities,
valid QAC references, and exact translation-text reconstruction. It does not
judge or rewrite the translation.

If it fails, stop and report the exact checker output. Do not patch the
writer's JSON or send supplementary linguistic instructions.

## 4. Finish

On success, report:

- the output path;
- that the cold writer completed the whole surah; and
- that the mechanical check passed.

Do not claim canonical publication or linguistic approval. Those are later
editorial decisions.
