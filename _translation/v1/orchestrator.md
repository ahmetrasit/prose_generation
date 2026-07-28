# Cold translation orchestrator — layer 1

You are the sole controller for one layer-1 job. This runbook is complete: do not
rely on prior conversation or undocumented project knowledge.

Perform every deterministic step yourself. Delegate exactly two things, each to
one fresh cold agent: the Turkish-assisted shared branch selection, and the
target-language writing.

## Required assignment

- `surah`: integer, for example `103`;
- `language`: BCP-47 target-language tag, for example `tr`;
- `date`: ISO date stamped into the prompt header. It is the only
  non-deterministic input; pass it explicitly to reproduce a prompt byte-for-byte.

Run from the `prose_generation` repository root. Read and write only this
repository; sibling repositories are input-only.

## Ownership

The controller prepares inputs, renders prompts, runs mechanical checks, and
reports. The agents alone author linguistic content. **The controller never
rewrites what an agent authored** — a failing check is reported, not patched.

## The two units of work, and why they are separate

| stage | unit | shared across languages |
| --- | --- | --- |
| 0 — anchors | one surah or explicit ayah chunk | **yes** — Turkish-assisted selection is shared |
| 1–5 — translation | one surah, one language | no |

Stage 0 runs **once per surah, ever**, or once per explicit pilot chunk before
the chunks are concatenated into a surah seed. It uses the independently
authored ordinary Turkish baseline as non-authoritative assistance, but Arabic
morphology and context control the shared result.

---

## Stage 0 — Seed the primary anchors

Skip to stage 1 if `_translation/v1/source/s{surah3}.primary-anchors.json`
already exists and a `primary-anchor-seed-v4` passes the stage-0 check below.
Older seeds remain readable by `build_bundle.py` only as migration
compatibility; new anchor work must use v4.

```sh
python3 _translation/v1/tools/build_anchor_input.py --surah <surah>
python3 _translation/v1/tools/instantiate.py --surah <surah> --stage anchors --date <date>
```

The first command enumerates every rooted QAC stem, every candidate Furuq root,
and every Arabic branch definition. It also attaches the independently authored
ordinary Turkish baseline and QAC-word alignment. The second command renders
one self-contained prompt at
`_translation/v1/prompts/s{surah3}.anchors.prompt.md`.

If the rendered prompt is beyond a comfortable context window — `instantiate.py`
warns above 900 KB — seed in chunks. The candidate space is per root, not per
occurrence, so chunks concatenate cleanly:

```sh
python3 _translation/v1/tools/build_anchor_input.py --surah 2 --ayahs 1-20
```

Send the rendered prompt, and nothing else, to one fresh cold agent with no
inherited conversation context. The agent returns the complete JSON artifact plus
its friction section. The controller saves the JSON bytes exactly at the path
named in the prompt, then runs the check. Do not prepend instructions or
summarise the task; the prompt is the complete handoff.

Check what comes back:

```sh
python3 _translation/v1/tools/check_anchors.py --surah <surah>
```

This verifies coverage, ordering, and that every primary and resonant branch
exists on a candidate root in the frozen exhaustive input. It does not judge
whether either semantic role is right.

## Stage 1 — Build the language bundle

```sh
python3 _translation/v1/tools/build_bundle.py --surah <surah> --language <language>
```

Produces `_translation/v1/input/<language>/s<surah3>.json`.

The builder derives Turkish branch-core and contextual evidence, with complete
available error profiles, under the selected branches. It omits lexical senses
and hoists each evidence package once per distinct root and selected branch set;
rooted cards carry an `evidenceRef`. Target-language evidence omits
`evidenceLanguage`; explicit bridge-language exceptions are preserved. The
builder also omits derivable `qacWordRef` and `glossId`, unselected branch
evidence, split-root candidate packets, and repeated `rootResolution`. It reads
only v4 `primary`; `resonances` stay in the seed for downstream analysis and are
deliberately omitted from Stage 1. If evidence is missing, stop and report the
prerequisite.

## Stage 2 — Render the writer's prompt

```sh
python3 _translation/v1/tools/instantiate.py --surah <surah> --stage translation \
  --language <language> --date <date>
```

Produces `_translation/v1/prompts/s{surah3}.translation.{language}.prompt.md`
with the task, the output schema, and the bundle inlined in full.

The manifest beside it records every source path with its byte count. **Compare
those counts against the working tree before running.** A mismatch means the
prompt was rendered against a document you have since edited, and the run will
not reproduce.

## Stage 3 — Launch one cold writer

One agent authors the whole surah, or one explicit pilot chunk: occurrence
glosses first, then card glosses and fluent translation. Ayah-level splitting
within that unit would save little and would make repeated wording less
consistent.

Send only the rendered prompt to one fresh agent with no inherited context. Tell
it not to delegate. It returns the complete `translation-authored-v1` JSON
artifact plus its friction section. The controller saves the JSON bytes exactly
at `_translation/v1/authored/<language>/s<surah3>.authored.json` or the explicit
chunk path named in the prompt.

The writer sees its bundle and its output schema. It does not see an existing
translation, and it does not see the commentary principles — layer 1 holds the
primary reading still and does not reason about latent readings. If the runtime
cannot restrict repository reads, stage the prompt in an otherwise empty
temporary directory and copy the artifact back afterwards.

Do not launch competing writers for the same surah-language pair.

## Stage 4 — Assemble

```sh
python3 _translation/v1/tools/assemble.py --surah <surah> --language <language> \
  --model <model-id>
```

The writer authors only language. Every identity — QAC refs, root ids, branch
ids, gloss ids — is joined here from the bundle and the anchor seed, which makes
transcription error structurally impossible rather than merely detectable, and
which is what makes a long surah viable at all.

`assemble.py` validates the authored file as it joins and refuses to emit on any
error. It writes `_translation/v1/output/<language>/s<surah3>.json` including a
`provenance` block recording the release, the anchor/bundle/authored/prompt
hashes, the assembler version, and the model id.

## Stage 5 — Check the artifact

```sh
python3 _translation/v1/tools/check_output.py --surah <surah> --language <language>
```

Mechanical only: final shape, identities against the bundle, valid QAC
references, provenance completeness, and exact translation-text reconstruction.
It judges nothing linguistic.

If it fails, stop and report the exact output. Do not patch the JSON and do not
send the writer supplementary linguistic instructions — a second instruction
outside the prompt makes the run unreproducible.

## Finish

Report the output path, that the cold agents completed their stages, that both
mechanical checks passed, and both friction sections verbatim.

Do not claim canonical publication or linguistic approval. Those are later
editorial decisions.

## What is deliberately not automated

Whether a selected branch is the right floor, and whether the target prose is
good. Both are review acts. Every mechanical check in this runbook exists to make
those two judgements the only ones a human has to make.
