# Layer 3 Surah Reading

This is the active runbook for producing a surah-wide reading from the typed
primary floor, completed Layer-2 v2 ayah commentary artifacts, and available
channel/network evidence.

The final text is not a summary, an ayah-by-ayah retelling, or a catalogue of
semantic fields. It reveals channels and resonances that an ordinary
translation cannot supply, in language a regular reader can follow, while the
primary reading remains intact.

Files directly under `_channel/` belong to retired workflows. They are not
instructions or inputs for this workflow.

## Cold-Agent Contract

A cold orchestration agent can run this workflow using this document and the
files under `_channel/layer3/`.

- The Python scripts perform mechanical source projection, validation, prompt
  assembly, and final publication.
- Fresh semantic agents perform discovery, review, and composition.
- Each semantic agent reads only its generated prompt.
- Do not use `codex exec` for semantic passes. Spawn a fresh agent for each
  pass.
- Do not let an agent inspect source repositories or other workflow files after
  its prompt has been generated.
- Save each agent response only at the output path named by its prompt.
- Do not use output from an earlier run as fallback when a pass fails.

The scripts do not discover, merge, rank, or write channels. Cross-ayah
reasoning begins only after the mechanical source packet has been generated.

## Active Files

```text
_channel/layer3/
  ORCHESTRATION.md
  prompts/
    01-discover.md
    02-review.md
    03-compose.md
  schemas/
    layer2-handoff-v1.schema.json
    source-packet-v3.schema.json
    discovery-hypotheses-v2.schema.json
    channel-briefs-v2.schema.json
    surah-composition-v1.schema.json
    surah-reading-evidence-v1.schema.json
  scripts/
    common.py
    build_packet.py
    instantiate.py
    validate.py
    finalize.py
  runs/v3/sNNN/{language}/{runId}/
    N.source-packet.{language}.json
    inputs/
      N.discover.attempt-01.{language}.prompt.md
      N.review.attempt-01.{language}.prompt.md
      N.compose.attempt-01.{language}.prompt.md
    outputs/
      N.discovery-hypotheses.{language}.json
      N.channel-briefs.{language}.json
      N.surah-composition.{language}.json
    published/
      N.surah-reading.{language}.md
      N.surah-reading.evidence.{language}.json
      N.surah-reading.friction.{language}.md
```

Older `packets/`, `inputs/`, and `outputs/` directories are historical
artifacts. Older schema files that are not listed above are archival only. Do
not overwrite historical artifacts or use archival schemas during v3 runs.

## Source Contract

Required inputs:

- Quran text from `../quran-data/data/text/quran-uthmani.tsv`;
- a typed Layer-1 primary floor such as `_translation/v1/output/tr/s087.json`;
- for every numbered ayah, one complete Layer-2 v2 artifact set:
  `prose`, `evidence`, `index`, and `friction`;
- `_ayah_commentary/v2/PROMPT.md`, recorded as the handoff contract.

Optional inputs:

- the reviewed Network V3 file at
  `../quran-data/data/analysis/channels/network-v3/sNNN/review/reader_a_pilot.md`;
- V11 `09-final-report.md`, searched in `../quran-data` first and then
  `../latent_activation/v11/run/sNNN/`.

Layer 2 contributes a typed handoff from its non-prose artifacts:

- the complete findings index is parsed into `findings`;
- `surprise:<id>` rows become `localResonances` with `supports-primary` or
  `shifts-primary`;
- explicit rejection/counterpressure sections from evidence become
  `boundaries`;
- prose and friction are hashed for lineage, but their content is withheld
  from semantic passes.

Missing Quran text, primary floor, or any Layer-2 artifact aborts. Missing
Network V3 or V11 material emits a warning and the run continues.

## Hermetic Views

`build_packet.py` creates the canonical v3 source packet. `instantiate.py`
projects a different hermetic view for each semantic pass.

### Discover

The discovery prompt contains:

- Quran surface anchors and typed primary-floor lines;
- mechanically projected Network V3 activation cards;
- relevant coverage state and warnings.

It intentionally excludes Layer-2 prose, Layer-2 findings, Layer-2 boundaries,
V11 prose, and prior synthesis. The discovery agent opens possible cross-ayah
recognitions without selecting, auditing, or composing.

Output: `N.discovery-hypotheses.{language}.json`.

### Review

The review prompt contains:

- the discovery hypotheses;
- typed primary ground;
- the complete Layer-2 findings handoff, local resonances, and boundaries;
- Network V3 activation cards and bounded V11 secondary material;
- source lineage, coverage state, and warnings.

The review agent builds latent-dependent channel briefs. Every discovery
hypothesis and every local resonance must either support at least one channel or
receive one non-channel disposition. Inputs can be many-to-many: one resonance
may support several channels, and several resonances may support one channel.
No channel is ranked above another, and incompatible channels may coexist.

Output: `N.channel-briefs.{language}.json`.

### Compose

The composition prompt contains:

- typed primary ground;
- the reviewed channel briefs.

The composition agent writes one JSON envelope. Its `prose` field is the
publishable reading; its evidence map proves that every admitted channel and
every admitted hinge landed in ordinary reader language. There is no paragraph,
word, channel, or length quota.

Output: `N.surah-composition.{language}.json`.

### Finalize

`finalize.py` validates the composition envelope against the packet, hypotheses,
and briefs, then emits the three publication artifacts:

- `N.surah-reading.{language}.md`;
- `N.surah-reading.evidence.{language}.json`;
- `N.surah-reading.friction.{language}.md`.

## Run A Surah

Replace `{N}`, `{LANG}`, `{LAYER2_DIR}`, and `{LAYER2_LABEL}` with the selected
surah, language, and accepted Layer-2 output set.

Build the source packet:

```sh
python3 _channel/layer3/scripts/build_packet.py \
  --surah {N} \
  --language {LANG} \
  --layer2-dir {LAYER2_DIR} \
  --layer2-label {LAYER2_LABEL}
```

If every ayah has a unique complete Layer-2 artifact set, `--layer2-label` may
be omitted. The script writes under `_channel/layer3/runs/v3/.../{runId}/`.

Generate and run discovery:

```sh
python3 _channel/layer3/scripts/instantiate.py discover --surah {N} --language {LANG}
```

Spawn a fresh agent with this task:

```text
Read only the generated discover prompt under _channel/layer3/runs/v3/.
Follow that prompt and write only the exact output file it names.
Do not inspect other files or use outside sources.
```

Generate and run review:

```sh
python3 _channel/layer3/scripts/instantiate.py review --surah {N} --language {LANG}
```

Spawn a fresh agent with the same boundary: read only the generated review
prompt and write only the exact output file it names.

Generate and run composition:

```sh
python3 _channel/layer3/scripts/instantiate.py compose --surah {N} --language {LANG}
```

Spawn a fresh agent with the same boundary: read only the generated compose
prompt and write only the exact composition JSON file it names.

Finalize after composition:

```sh
python3 _channel/layer3/scripts/finalize.py \
  --packet {RUN_DIR}/{N}.source-packet.{LANG}.json \
  --hypotheses {RUN_DIR}/outputs/{N}.discovery-hypotheses.{LANG}.json \
  --briefs {RUN_DIR}/outputs/{N}.channel-briefs.{LANG}.json \
  --composition {RUN_DIR}/outputs/{N}.surah-composition.{LANG}.json
```

## Acceptance

A completed reading must satisfy all of these conditions:

- It changes the reader's model rather than explaining the primary reading in
  greater detail.
- Its changed understanding is unavailable when the secondary semantic
  contribution is removed.
- The same contribution makes something specific in this surah newly
  intelligible rather than supplying a portable metaphor or general moral.
- Weak, remote, and counterpressured material remains usable without becoming
  an alternate translation.
- Rejected local predications do not return as claims, while their surviving
  semantic residue may participate in a bounded cross-ayah operation.
- Every admitted channel and hinge is visible in ordinary prose.
- The primary reading remains recoverable.
- The final prose is coherent and engaging rather than a channel catalogue.
