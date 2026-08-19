# Layer 3 Surah Reading

This is the active runbook for producing a surah-wide reading from the typed
primary floor, completed reader-facing Layer-2 editorial artifacts, and
available channel/network evidence.

Layer 3 builds one whole-surah semantic model and renders it at two reader
moments:

- a **prelude** prepares the reader to notice admitted secondary images in the
  ayah readings without resolving them;
- a **postlude** reinforces those local encounters and completes their
  cross-ayah, whole-surah payoff.

Neither surface is a summary, an ayah-by-ayah retelling, or a catalogue of
semantic fields. The primary reading remains intact, while coherent secondary
images and systems unavailable from an ordinary translation become visible.

Files directly under `_channel/` belong to retired workflows. They are not
instructions or inputs for this workflow.

## Agent Contract

A cold orchestration agent can run this workflow using this document and the
files under `_channel/layer3/`.

- Python scripts perform mechanical source projection, validation, prompt
  assembly, and final publication.
- A fresh semantic agent performs discovery.
- A second fresh semantic agent performs review.
- A third fresh semantic agent performs composition and remains open for the
  editorial follow-up. Do not spawn a separate editor.
- "Spawn" means the orchestration environment's native facility for creating
  an isolated semantic-agent conversation and, for composition, sending a
  second turn to that same conversation. Confirm that this facility is
  available before building the packet. If it is unavailable, stop and report
  the missing capability; do not substitute `codex exec`, the orchestration
  agent itself, or a single shared conversation for all passes.
- Each semantic agent reads only its generated prompt. The composition agent
  may read both its generated compose prompt and, in the same conversation, its
  generated edit prompt.
- Do not use `codex exec` for semantic passes.
- Do not let an agent inspect source repositories or workflow files after its
  prompt has been generated.
- Save each response only at the output path named by its prompt.
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
    04-edit.md
  schemas/
    layer2-handoff-v1.schema.json
    source-packet-v3.schema.json
    discovery-hypotheses-v3.schema.json
    channel-briefs-v3.schema.json
    surah-composition-v2.schema.json
    surah-reading-evidence-v2.schema.json
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
      N.edit.attempt-01.{language}.prompt.md
    outputs/
      N.discovery-hypotheses.{language}.json
      N.channel-briefs.{language}.json
      N.surah-composition.draft.{language}.json
      N.surah-composition.{language}.json
    failed/
      attempt-specific invalid semantic outputs, preserved only after a
      validator rejects them
    published/
      N.surah-reading.prelude.{language}.md
      N.surah-reading.postlude.{language}.md
      N.surah-reading.evidence.{language}.json
      N.surah-reading.friction.{language}.md
  outputs/sNNN/
    N.surah-reading.prelude.{language}.md
    N.surah-reading.postlude.{language}.md
    N.surah-reading.evidence.{language}.json
    N.surah-reading.friction.{language}.md
```

`runs/v3/.../published/` is the immutable run-local publication copy tied to
one packet, prompt set, and run ID. `_channel/layer3/outputs/sNNN/` is the
stable reader-facing publication directory for the latest accepted Layer-3
reading of that surah. Do not use stable outputs as semantic inputs for a new
v3 run; they are publication targets only.

Older `packets/` and `inputs/` directories are historical artifacts. Older
schema files not listed above are archival. Do not overwrite historical
artifacts or use archival schemas during active v3 runs.

## Source Contract

Required inputs:

- Quran text from `../quran-data/data/text/quran-uthmani.tsv`;
- a typed Layer-1 primary floor such as `_translation/v1/output/tr/s087.json`;
- for every numbered ayah, one complete **editorial** Layer-2 v2 artifact set:
  `prose`, `evidence`, `index`, and `friction`;
- `_ayah_commentary/v2/PROMPT.md`, recorded as the handoff contract.

Optional inputs:

- the reviewed Network V3 file at
  `../quran-data/data/analysis/channels/network-v3/sNNN/review/reader_a_pilot.md`;
- V11 `09-final-report.md`, searched in `../quran-data` first and then
  `../latent_activation/v11/run/sNNN/`.

The packet builder rejects a non-editorial Layer-2 label. It parses the complete
editorial findings index into `findings`, projects typed `surprise:<id>` rows as
`localResonances`, and retains explicit evidence boundaries. Layer-2 prose is
hashed in the packet but withheld from discovery and review. After review has
admitted channels, `instantiate.py` verifies the hashes again and projects
reader-facing prose only for ayahs named by admitted channel members into the
compose and edit prompts. Friction content remains withheld.

A local resonance always carries exactly one primary-relation tag. Its
`inference` value follows the Layer-2 row: `[inference]` marks a writer
synthesis, while its absence is a valid grounded resonance and must not cause
Layer 3 ingestion to fail. Relation tags on non-`surprise:*` findings are
preserved as finding metadata but do not promote those rows to local
resonances.

Missing Quran text, primary floor, any Layer-2 artifact, or the editorial label
aborts. Missing Network V3 or V11 material emits a warning and the run continues.

## Semantic Passes

### Discover

The discovery prompt contains Quran surface anchors, typed primary-floor lines,
Network V3 activation cards, and relevant coverage warnings. It excludes all
Layer-2 material, V11 prose, and prior synthesis.

The agent opens concrete image-system hypotheses. Every hypothesis names its
system boundary and the distinct contribution of at least two ayahs. Every
activation card is accounted once in `activationCardCoverage`, including cards
that opened no coherent hypothesis. Discovery does not rank, merge, admit, or
reject.

Output: `N.discovery-hypotheses.{language}.json`.

### Review

The review prompt contains discovery hypotheses, typed primary ground, the
complete Layer-2 findings/local-resonance/boundary handoff, activation cards,
bounded V11 material, and lineage state. It still excludes Layer-2 prose.

The agent first builds concrete channels at their natural granularity, then
accounts for unused hypotheses and local resonances. Admission tests the
secondary image and its operation, not whether a broad moral conclusion is
surface-derivable. Every admitted channel records:

- its concrete image system and system boundary;
- distinct member landings in at least two ayahs;
- cross-member hinges that preserve each member's contribution;
- its whole-surah operation and indispensable secondary gain;
- a prelude promise and a postlude payoff.

When a member or hinge uses a discovery hypothesis, it carries the relevant
`activation:*` refs from that hypothesis into its evidence refs. When it uses a
local resonance, it carries both the resonance and its exact paired finding ref.

Compatible and incompatible admitted channels coexist without ranking or
disambiguation. Inputs merge only when both concrete mechanism and reader payoff
are the same.

Output: `N.channel-briefs.{language}.json`.

### Compose Draft

The compose prompt contains typed primary ground, reviewed channel briefs, and
verified reader-facing Layer-2 prose for admitted member ayahs. The selected
prose supports recognition and continuity; it cannot introduce an unreviewed
channel.

The agent writes both reader surfaces in one draft envelope:

- the prelude has one compact primary footing and one unresolved promise per
  channel;
- the postlude lands every channel, concrete member, and hinge, and returns to
  the primary surah with changed understanding.

Reader surfaces must not ask the reader to trust unattached images. Every
non-obvious image or working system needs a light first-use attachment to at
least one representative ayah number and surface word or phrase. These anchors
are reader orientation, not evidence apparatus: use forms like `1:6'daki yol
isteği` or, when the Arabic word itself matters,
`1:6'daki yol, {ar:ٱلصِّرَٰطَ, tr:es-sırât, gloss:yol}`.

The evidence map records one primary grounding per surface, every prelude
promise, and every postlude channel/member/hinge landing. It does not require a
primary claim per ayah.

Output: `N.surah-composition.draft.{language}.json`.

### Editorial Revision

Send the generated edit prompt to the **same composition agent**. It revises
both surfaces for contemporary reader language, movement, transitions, and
deduplication without reducing any admitted image, member, hinge, or payoff.
The prelude must remain anticipatory; the postlude must remain complete. The
agent updates every evidence span after revision.

Output: `N.surah-composition.{language}.json`.

### Finalize

`finalize.py` accepts only an editorial composition whose `revisionOf` points to
the expected draft ID. It emits the two reader surfaces, shared evidence map,
and friction report.

## Run A Surah

Run every command from the repository root. Resolve these values before the
first command:

- `{N}`: the unpadded surah number, for example `1`;
- `{LANG}`: the normalized language tag, for example `tr`;
- `{PRIMARY_FLOOR}`: the exact typed Layer-1 file selected for this run, for
  example `_translation/v1/output/tr/s001.v3-gloss-test.json`;
- `{LAYER2_DIR}`: the directory containing the complete Layer-2 artifacts;
- `{LAYER2_LABEL}`: the exact editorial artifact label, for example
  `editorial.tr` or `luna-max.editorial.tr`.
- `{STABLE_OUT_DIR}`: the stable publication directory for the accepted reader
  surfaces, `_channel/layer3/outputs/sNNN/` where `NNN` is the zero-padded surah
  number.

The scripts emit additional paths. Copy each emitted path exactly rather than
reconstructing it:

- `{PACKET}`: the path printed by `build_packet.py`;
- `{RUN_DIR}`: the parent directory of `{PACKET}`;
- `{DISCOVER_PROMPT}`, `{REVIEW_PROMPT}`, `{COMPOSE_PROMPT}`, and
  `{EDIT_PROMPT}`: paths printed by the corresponding `instantiate.py` command;
- `{HYPOTHESES}`, `{BRIEFS}`, `{DRAFT}`, and `{COMPOSITION}`: exact output paths
  named inside those generated prompts.

Do not choose a file by searching `runs/v3/`; multiple runs and attempts may be
present.

### Build And Validate The Packet

```sh
python3 _channel/layer3/scripts/build_packet.py \
  --surah {N} \
  --language {LANG} \
  --primary-floor {PRIMARY_FLOOR} \
  --layer2-dir {LAYER2_DIR} \
  --layer2-label {LAYER2_LABEL}
```

Record the emitted packet path as `{PACKET}` and its parent as `{RUN_DIR}`. Then
run the explicit source gate:

```sh
python3 _channel/layer3/scripts/validate.py packet \
  {PACKET} --verify-sources
```

Do not begin a semantic pass unless this prints `ok`.

### Discover

```sh
python3 _channel/layer3/scripts/instantiate.py discover \
  --surah {N} --language {LANG} \
  --packet {PACKET} \
  --attempt 1
```

Record the emitted path as `{DISCOVER_PROMPT}`. Open the first fresh isolated
semantic-agent conversation and send exactly this task, with the placeholder
replaced by that exact path:

```text
Read only this generated prompt: {DISCOVER_PROMPT}
Follow it exactly and write only the output file it names.
Do not inspect any other file or use outside sources.
```

Record the output path named by the prompt as `{HYPOTHESES}`. After the agent
writes it, run:

```sh
python3 _channel/layer3/scripts/validate.py hypotheses \
  {HYPOTHESES} --packet {PACKET}
```

Close the discovery agent only after this prints `ok`.

### Review

```sh
python3 _channel/layer3/scripts/instantiate.py review \
  --surah {N} --language {LANG} \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES} \
  --attempt 1
```

Record the emitted path as `{REVIEW_PROMPT}`. Open the second fresh isolated
semantic-agent conversation and send the same three-line task above with
`{REVIEW_PROMPT}` as the exact path. Record the output named by that prompt as
`{BRIEFS}`, then run:

```sh
python3 _channel/layer3/scripts/validate.py briefs \
  {BRIEFS} \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES}
```

Close the review agent only after this prints `ok`.

### Compose Draft

```sh
python3 _channel/layer3/scripts/instantiate.py compose \
  --surah {N} --language {LANG} \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES} \
  --briefs {BRIEFS} \
  --attempt 1
```

Record the emitted path as `{COMPOSE_PROMPT}`. Open the third fresh isolated
semantic-agent conversation and send the same three-line task with
`{COMPOSE_PROMPT}` as the exact path. Record the named output as `{DRAFT}` and
keep this agent conversation open. Then run:

```sh
python3 _channel/layer3/scripts/validate.py composition \
  {DRAFT} \
  --packet {PACKET} \
  --briefs {BRIEFS} \
  --hypotheses {HYPOTHESES} \
  --phase draft
```

Do not generate the edit prompt unless this prints `ok`.

### Edit In The Same Conversation

```sh
python3 _channel/layer3/scripts/instantiate.py edit \
  --surah {N} --language {LANG} \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES} \
  --briefs {BRIEFS} \
  --draft {DRAFT} \
  --attempt 1
```

Record the emitted path as `{EDIT_PROMPT}`. In the still-open composition-agent
conversation, send only the three-line task above with `{EDIT_PROMPT}` as the
exact path. Do not add critique, validator output, or another request. Record
the named output as `{COMPOSITION}`, then run:

```sh
python3 _channel/layer3/scripts/validate.py composition \
  {COMPOSITION} \
  --packet {PACKET} \
  --briefs {BRIEFS} \
  --hypotheses {HYPOTHESES} \
  --phase editorial
```

Close the composition agent only after this prints `ok`.

### Editorial Integration Follow-Up

If the validated editorial surfaces preserve coverage but still read as a
channel catalogue, send the message below verbatim to the same composition
agent. Do not re-send the packet, briefs, draft, generated prompts, validator
output, or orchestrator critique. This follow-up is a prose-integration pass
inside the already accepted semantic model; it must not reduce channel
visibility or evidentiary coverage.

After the agent completes, rerun the editorial composition validator above. If
it prints `ok`, regenerate both the run-local `published/` artifacts and the
stable `_channel/layer3/outputs/sNNN/` artifacts from the revised composition
before closing the composition agent.

```text
Please revise your current Layer 3 editorial composition again, using the existing draft/editorial composition, channel briefs, evidence map, and paths already present in this same conversation and workspace. Do not read repository workflow files, do not request a new bundle, and do not create a fresh semantic model.

This is an editorial-integration pass, not a compression pass.

Revise without reducing interpretive yield or changing admission/evidentiary judgments. Preserve the primary footing and every admitted channel, concrete member, hinge, claim boundary, and distinct reader payoff. Keep every channel/member/hinge visibly recoverable in the postlude, and keep every prelude promise visibly recoverable in the prelude. Do not rank, disambiguate, merge away, or drop any admitted image or payoff. Merge prose only when it performs the same image work and gives the reader the same payoff.

Do not shorten merely for length. There is no word, paragraph, section, heading, or channel quota. Give every significant image enough room. The goal is not less coverage; the goal is reader-facing continuity while preserving full coverage.

Rewrite the prelude as fluent, contemporary Turkish for a regular reader. It must remain anticipatory: one compact surface foothold, one concrete unresolved promise per admitted channel, no proofs, no exhaustive member sequences, and no completed postlude payoff. Let the promises form one anticipatory movement rather than a catalogue. Do not let images float unattached: when an image or system first appears, attach it lightly to at least one representative ayah number and surface word or phrase, such as `1:6'daki yol isteği`; when the Arabic word itself matters, use a compact span such as `{ar:ٱلصِّرَٰطَ, tr:es-sırât, gloss:yol}` after the ordinary Turkish sense.

Rewrite the postlude as fluent, contemporary Turkish for a regular reader. It must remain complete: every admitted channel, member image, and hinge must land visibly. Remove analyst shorthand, workflow language, stiff technical calques, defensive repetition, and evidence-catalogue rhythm. Avoid restarting every paragraph as an independent finding or repeatedly announcing another image. Create cinematic continuity without adding drama or interpretation: each section should inherit a concrete image, question, tension, relation, or motion from the preceding section and carry it somewhere new. Keep every non-obvious image anchored on first use to a representative ayah number and surface word or phrase, so the reader can tell where the image enters the surah without consulting the hidden evidence map.

Keep distinct findings recoverable even when they belong to one larger movement. Preserve the separateness of materially distinct systems such as water, passage, sight, repair, gift, belonging, account, protection, conflict, naming, and bodily uprightness; do not collapse them into a generic thesis. But let them operate inside a developing whole-surah reading rather than as separate exhibits.

Use reader-facing subtitles only where the reading genuinely changes movement. Subtitles should create an expectation about what becomes visible next; they must not name evidence categories, channels, findings, workflow stages, schema parts, or source types.

Let the ending return naturally to the surah's primary force and show what has become newly visible, rather than listing all findings again. Restore a governing reader movement where it is earned by the existing material: naming/praise, dependence/help, guidance, path, received favor, and differentiated end states.

Update every evidence span after revision. Every evidence span must occur exactly once in its designated surface. The evidence map must continue to cover exactly the required primary groundings, prelude promises, postlude channels, postlude members, and postlude hinges.

Overwrite only the current canonical editorial composition JSON path you previously wrote for this run. Write no other files.
```

### Failed Attempts

Never advance with an invalid output and never overwrite it in place. If a
semantic validator fails:

1. Preserve the rejected artifact under `{RUN_DIR}/failed/` with the form
   `{N}.{STAGE}.attempt-{AA}.invalid.{LANG}.json`, where `{STAGE}` is
   `discover`, `review`, `compose`, or `edit` and `{AA}` is the two-digit
   attempt number.
2. Re-run the same `instantiate.py` command with the next `--attempt` number and
   record the newly emitted prompt path exactly.
3. Discovery and review retries use new fresh semantic agents. A compose-draft
   retry uses a new fresh composition agent, which must remain open for edit.
   An edit retry stays in the same composition-agent conversation.
4. Run the same validator again. Continue only after it prints `ok`.

The mechanical archive operation is:

```sh
mkdir -p {RUN_DIR}/failed
mv {FAILED_OUTPUT} \
  {RUN_DIR}/failed/{N}.{STAGE}.attempt-{AA}.invalid.{LANG}.json
```

If the composition-agent conversation is lost before editorial validation,
stop and report the failure. Do not use a different agent to edit its draft. If
a structurally valid output fails the Acceptance review below, treat it as a
failed attempt at the earliest stage where the semantic loss entered; do not
ask a later stage to invent missing channels.

### Semantic Gate And Finalize

Inspect the validated editorial surfaces and briefs against every Acceptance
condition below. Mechanical validation is not permission to publish. For a
production run, obtain the required human semantic approval before finalizing.

Finalize first to the run-local `published/` directory for immutable provenance:

```sh
python3 _channel/layer3/scripts/finalize.py \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES} \
  --briefs {BRIEFS} \
  --composition {COMPOSITION}
```

Then publish the same validated composition to the stable reader-facing
directory:

```sh
python3 _channel/layer3/scripts/finalize.py \
  --packet {PACKET} \
  --hypotheses {HYPOTHESES} \
  --briefs {BRIEFS} \
  --composition {COMPOSITION} \
  --out-dir {STABLE_OUT_DIR}
```

The stable files are the normal paths to show readers and downstream consumers:

```text
_channel/layer3/outputs/sNNN/N.surah-reading.prelude.{language}.md
_channel/layer3/outputs/sNNN/N.surah-reading.postlude.{language}.md
_channel/layer3/outputs/sNNN/N.surah-reading.evidence.{language}.json
_channel/layer3/outputs/sNNN/N.surah-reading.friction.{language}.md
```

If stable files already exist for the same surah/language, replace only those
four publication artifacts after the new editorial composition has validated
and received semantic approval. Keep the superseded run-local `runs/v3/...`
artifacts intact.

## Acceptance

A completed reading must satisfy all of these conditions:

- It changes the reader's model rather than explaining the primary reading in
  greater detail.
- Every channel is a concrete secondary image or working system, not an
  abstract topic with latent references attached.
- Every activation card was searched and accounted during discovery.
- Each admitted channel has distinct members in at least two ayahs and produces
  a whole-surah gain no ayah-by-ayah reading can supply.
- Inputs with different mechanisms or reader payoffs have not been hidden under
  one broad hinge.
- Weak, remote, and counterpressured material remains bounded without becoming
  an alternate translation.
- The prelude promises every admitted channel without resolving all members or
  hinges.
- The postlude visibly lands every channel, member, and hinge while remaining
  coherent prose rather than a catalogue.
- Every non-obvious image or working system has a light reader-facing attachment
  to at least one representative ayah number and surface word or phrase on first
  use. The prose does not require the reader to remember Layer-2 commentary or
  trust unattached imagery.
- Neither surface retells the surah one ayah at a time.
- The primary reading remains recoverable in both surfaces.
- The editorial output contains no duplicate paragraphs or stray draft tails.

Mechanical validation proves lineage, coverage, evidence pairing, required
landings, and publication hashes. It does not prove literary or interpretive
quality. A production run still requires human semantic review before release.
