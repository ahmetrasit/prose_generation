# Layer 3 Surah Reading

This is the active runbook for producing a surah-wide reading from completed
ayah-level commentary and reviewed latent semantic material.

The final text is not a summary, an ayah-by-ayah retelling, or a catalogue of
semantic fields. It reveals cross-ayah activations that an ordinary translation
cannot supply and shows how they materially change the reader's understanding
while leaving the primary reading intact.

Files directly under `_channel/` belong to retired workflows. They are not
instructions or inputs for this workflow.

## Cold-Agent Contract

A cold orchestration agent can run this workflow using this document and the
files under `_channel/layer3/`.

- The Python scripts perform mechanical source projection and prompt assembly.
- Fresh semantic agents perform discovery, review, and composition.
- Each semantic agent reads only its generated prompt.
- Do not use `codex exec` for semantic passes. Spawn a fresh agent for each pass.
- Do not let an agent inspect source repositories or other workflow files after
  its prompt has been generated.
- Save each agent response only at the output path named by its prompt.
- Do not use output from an earlier run as fallback when a pass fails.

The scripts do not discover, merge, rank, or write channels. Cross-ayah
reasoning begins only after the mechanical input has been generated.

## Active Files

```text
_channel/layer3/
  ORCHESTRATION.md
  prompts/
    01-discover.md
    02-review.md
    03-compose.md
  schemas/
    source-packet-v2.schema.json
    discovery-hypotheses-v1.schema.json
    channel-briefs-v1.schema.json
  scripts/
    common.py
    build_packet.py
    instantiate.py
  packets/sNNN/
    N.source-packet.json
  inputs/sNNN/
    N.discover.prompt.md
    N.review.prompt.md
    N.compose.prompt.md
  outputs/sNNN/
    N.discovery-hypotheses.json
    N.channel-briefs.json
    N.surah-reading.md
```

`packets/` and `inputs/` are mechanically generated. Files under `outputs/`
are semantic-agent results.

## Source Contract

Required inputs:

- Quran text from `../quran-data/data/text/quran-uthmani.tsv`;
- accepted Layer 2 prose for every numbered ayah;
- the corresponding Layer 2 evidence files, projected to explicit rejection,
  counterpressure, and boundary sections.

Optional inputs:

- the reviewed Network V3 file at
  `../quran-data/data/analysis/channels/network-v3/sNNN/review/reader_a_pilot.md`;
- V11 `09-final-report.md`, searched in `../quran-data` first and then
  `../latent_activation/v11/run/sNNN/`.

Network V3 contributes mechanically extracted activation cards. Raw candidates
and machine-family files are excluded.

V11 contributes only its surprising-discovery and open-boundary sections. Its
prior integrated mechanism, rankings, inventories, and prewritten synthesis are
excluded so they cannot anchor the downstream answer.

Missing Network V3 or V11 material emits a warning in the terminal and in the
packet. The packet is still produced. Quran text and complete Layer 2 outputs
are required.

## Hermetic Views

`build_packet.py` creates the canonical source packet. `instantiate.py` then
projects a different hermetic view for each semantic pass.

### Discover

The discovery prompt contains:

- Quran surface rows;
- mechanically projected Network V3 activation cards;
- relevant coverage state and warnings.

It intentionally excludes Layer 2 prose, local rejection material, V11 prose,
and prior synthesis. The discovery agent opens the field without selecting,
auditing, or composing.

Output: `N.discovery-hypotheses.json`.

### Review

The review prompt contains:

- the discovery hypotheses;
- the same reviewed activation cards;
- the primary ground from completed Layer 2 prose;
- local rejection and counterpressure boundaries;
- projected V11 secondary material;
- coverage state and warnings.

The full reviewed Network V3 prose is not repeated because its activation cards
already carry the mechanically retained signals.

The review agent builds latent-dependent channel briefs. A channel qualifies
only when removing its secondary semantic contribution preserves the ordinary
reading but removes the changed understanding. Mere non-derivability is not
enough: the channel must also make a specific feature, tension, transition, or
ending of the surah newly intelligible.

Output: `N.channel-briefs.json`.

### Compose

The composition prompt contains:

- the primary ground;
- the reviewed channel briefs.

It does not contain the discovery hypotheses, Network V3 prose, V11 prose, or
the local-boundary catalogue. The briefs carry the exact usable hinge and the
specific claims that must not be made.

The composition agent writes one developing reader experience. Brief boundaries
are not prose boundaries, and the prose does not enumerate evidence. The exact
secondary hinge must be visible in ordinary reader language and must materially
alter what the reader sees.

Output: `N.surah-reading.md`.

## Run A Surah

Replace `{N}`, `{LAYER2_DIR}`, and `{LAYER2_LABEL}` with the selected surah and
accepted Layer 2 output set.

Build the source packet:

```sh
python3 _channel/layer3/scripts/build_packet.py \
  --surah {N} \
  --layer2-dir {LAYER2_DIR} \
  --layer2-label {LAYER2_LABEL}
```

If every ayah has a unique matching Layer 2 prose and evidence file,
`--layer2-label` may be omitted. If Network V3 or V11 is unavailable, confirm
that the expected warning was emitted and continue.

Generate and run discovery:

```sh
python3 _channel/layer3/scripts/instantiate.py discover --surah {N}
```

Spawn a fresh agent with this task:

```text
Read only `_channel/layer3/inputs/sNNN/N.discover.prompt.md`.
Follow that prompt and write only
`_channel/layer3/outputs/sNNN/N.discovery-hypotheses.json`.
Do not inspect other files or use outside sources.
```

Generate and run review:

```sh
python3 _channel/layer3/scripts/instantiate.py review --surah {N}
```

Spawn a fresh agent with this task:

```text
Read only `_channel/layer3/inputs/sNNN/N.review.prompt.md`.
Follow that prompt and write only
`_channel/layer3/outputs/sNNN/N.channel-briefs.json`.
Do not inspect other files or use outside sources.
```

Generate and run composition:

```sh
python3 _channel/layer3/scripts/instantiate.py compose --surah {N}
```

Spawn a fresh agent with this task:

```text
Read only `_channel/layer3/inputs/sNNN/N.compose.prompt.md`.
Follow that prompt and write only
`_channel/layer3/outputs/sNNN/N.surah-reading.md`.
Do not inspect other files or use outside sources.
```

The generated prompt tells the semantic agent the concrete value represented by
`N` and the exact output filename.

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
- The primary reading remains recoverable.
- The final prose is coherent and engaging rather than a channel catalogue.
