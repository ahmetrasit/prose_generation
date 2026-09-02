# Commentary v4

V4 keeps the v3 linguistic agents and removes the v3 run-management system.
It is a fixed four-agent workflow backed by Git, with exactly three artifact
roots:

```text
_commentary/v4/
  input/<analysis-id>/sNNN/S_A/       snapshots, packets, prompts, manifest
  raw/<analysis-id>/sNNN/S_A/         three ledgers and four first-pass files
  editorial/<analysis-id>/sNNN/S_A/   four editorial files
```

`native` is the default analysis ID. Custom ordered contexts use a stable,
human-readable ID, so several readings of the same focus have disjoint paths
without run IDs or session directories.

V4 simplifies the authoring workflow, not upstream evidence construction. Its
default input is one canonical non-tiered unit bundle under `bundles/`; the
exact origin and hash are recorded in the unit manifest.
It reuses V3's deterministic preparation and packet-projection code in memory,
then snapshots the source, derived docket, and packets into the V4 unit input.
No pre-existing V3 input, adjudication, output, or session tree is required. An
explicit legacy docket remains available only for exact historical replay.

There are no run IDs, content-addressed directories, session files, turn
receipts, repair generations, completion manifests, or hidden temporary work
trees. A SHA-256 stays inside the unit manifest and model response identity; it
does not become a directory name. Git records artifact history.

There is also no semantic repair cycle. Each scope analyst gets one substantive
turn, and the canonical writer absorbs reconciliation and incomplete coverage
without sending work back. Invalid or stale response JSON is a terminal unit
error, not an automatically generated replacement turn; recovery is an explicit
operator action. V4 has no attempt counter and must not be driven by an automatic
retry loop.

## Preserved behavior

- Micro, macro, and global remain independent fresh analysts.
- Their rendered prompts use the v3 scope templates verbatim and the same v3
  evidence packets and request identities.
- The canonical writer receives the same governing principles,
  `COMMENTARY_SPEC.md`, channel definitions, and canonical Layer-2 v2 prompt
  verbatim.
- The canonical editorial instructions are embedded byte-for-byte from
  `_commentary/v3/prompts/editorial-followup.md` in a deterministic handoff that
  adds only exact input hashes and the separate editorial destination paths.
  That handoff is sent to the same live canonical writer.
- The three evidence scopes, exact source identities, HFT qualifications,
  Arabic surface evidence, and no-selection rules remain intact.
- Ordered compositions add hash-bound context candidates to the existing packet
  shapes. Explicitly added ayat are context-only members of all three lanes;
  ordinary ordered context retains macro/global routing. Neither changes the
  scope prompts, response protocol, editorial instructions, or turn count.
- Automatic basmala, explicit external ayat, and ordinary selected context use
  one native-depth projection: lean ayah roots/occurrences plus compact mapped
  branch images. A context unit never imports its standalone-focus products.

The one intentionally new prompt is `prompts/canonical.md`. It lets one fresh
writer perform reconciliation, prose preparation, and canonical composition in
one reasoning pass. That adaptation is required to remove the reconciler,
three scope-prose turns, and all repair loops. It does not impose a length
limit or a scripted semantic verdict. Explicit analyst decisions remain
authoritative; the adapter preserves their complete finding/evidence unions and
handles only lossless accounting recovery from the supplied packets.

## Commands

Before operating a new surah or package root, follow the source and bundle
decision tree in [`ORCHESTRATION.md`](ORCHESTRATION.md#cold-start-preflight).
That file is the authoritative end-to-end runbook; this section summarizes the
command interface.

Prepare or advance one native numbered ayah:

```bash
python3 _commentary/v4/workflow.py advance --ayah 29:38
```

The first call creates the unit input and returns three parallel scope
handoffs. Spawn each scope analyst through the multi-agent spawn tool with model
override `gpt-5.6-luna`, reasoning effort `max`, and no priority/service-tier
option. Each analyst writes the JSON object it returns to the declared
`expected_response`. Run the same command again after all three files exist; it
creates one canonical prompt and returns the canonical writer handoff.

Spawn the canonical writer through the same multi-agent spawn tool settings.
After that writer creates the four first-pass files, keep it live and run the
same command once more. V4 binds those exact files by hash, creates the
editorial handoff with the unchanged v3 editorial instructions, and returns it
for the same writer.

Multiple ayahs use the same command. Pass explicit refs, comma-separated refs,
or same-surah ranges:

```bash
python3 _commentary/v4/workflow.py advance --ayah 100:1-11
python3 _commentary/v4/workflow.py advance --ayah 1:1-7 2:1-5
```

A batch response contains one result per ayah and one flat
`parallel_handoffs` array. Every handoff carries `ayah_ref` and `stage`, so an
orchestrator can launch all currently ready scope or canonical turns in
parallel. Wait for every launched handoff in the current batch wave before
advancing that full batch again. To advance agents as they finish, call
`advance` with only those completed ayah refs; never advance a unit while one of
its workers is still writing. Keep only an in-memory mapping from ayah ref to
each live canonical writer until its editorial follow-up is sent; v4 persists
no agent handle or session ID. One failed unit is reported without hiding the
handoffs ready for other units. A `partial_error` batch exits nonzero while
still returning those valid handoffs in its JSON.

### Ordered context analyses

Define one or more ordered segments and select any subset as focus units. The
other units become context for each focus:

```bash
# Add one external ayah as a first-class context member for every Fatiha focus.
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-with-17-50 \
  --segment fatiha=1:1-7 \
  --member-surah 1 \
  --add-ayat 17:50 \
  --ayah 1:1-7

# Analyze every S100 ayah through an ordered Fatiha-then-S100 lens.
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-lens-s100 \
  --segment fatiha=1:1-7 \
  --segment s100=100:1-11 \
  --ayah 100:1-11
```

The first call snapshots the same composition as `analysis.json` under every
focus input. Later waves use only the stable ID and selected focuses:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-lens-s100 --ayah 100:1-11
```

For a reusable declaration, pass `--analysis path/to/analysis.json`; omit
`--ayah` to run all of its `focus_refs`. The JSON shape is:

```json
{
  "schema_version": "commentary-v4-analysis-composition-v2",
  "analysis_id": "fatiha-lens-s100",
  "segments": [
    {"id": "fatiha", "refs": ["1:1-7"]},
    {"id": "s100", "refs": ["100:1-11"]}
  ],
  "focus_refs": ["100:1-11"]
}
```

The equivalent reusable declaration for `--member-surah 100 --add-ayat
1:1,1:2` adds `"surah_membership":{"target_surah":100,
"added_ayat_refs":["1:1","1:2"]}`. Each added ref must be enumerated.

Selectors may be discontinuous or cross-surah. A unit may occur only once in a
composition, the focus must be selected from it, and ranges may not start at
zero. Every selected unit other than the current focus becomes context without
changing the canonical pericope. Same-surah context in the focus's segment is
routed to macro, including an explicitly selected ayah outside the native
pericope; cross-segment or cross-surah context is routed to global; micro
remains focus-local. `--add-ayat` accepts repeatable comma-separated `S:A`
refs, not ranges; the refs need not be repeated in a segment. They enter every
lane as context-only members and can never become focuses. Direct `S:0`
focus/context analysis is selected in exactly the same way as any explicit
ref. Independently of explicit composition, every
numbered ayah packet for S2-S8 and S10-S114 automatically carries the target
surah's `S:0` prefatory basmala as hash-bound surah-preface context in each
lane. S1 uses numbered `1:1`; S9 has no `9:0`.

After the writer has produced both phases:

```bash
python3 _commentary/v4/workflow.py verify --ayah 29:38
```

`verify` checks generated-input identity, fixed-path and regular-file
boundaries, the first-pass hashes supplied to the editorial turn, and nonempty
outputs. It does not judge findings, request repairs, constrain prose, or
rewrite agent work. Git remains the history and review boundary for the final
editorial file bytes; v4 creates no completion receipt.

Use `prepare` directly when a source path needs to be supplied explicitly. A
docket is derived automatically with the fixed V4 preparation policy:

```bash
python3 _commentary/v4/workflow.py prepare \
  --ayah 29:38 \
  --source-bundle path/to/29_38.ayah.json
```

`--docket path/to/29_38.docket.json` is an optional compatibility override, not
a normal workflow step. `--context-bundles-dir` changes the canonical package
root used for the focus and same-package selected-context units. The default is
`bundles/`. If you intentionally run a controlled alternate package root, such
as `bundles/s029-pericopes/p02_036-069/`, V4 loads package units from that root
and does not fall back to another root. `--member-bundles-dir` is a separate
root for the mandatory target-surah prefatory basmala and explicitly added or
out-of-pericope ayat.

For larger surahs, build a non-tiered pericope root first:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
python3 _commentary/v4/workflow.py prepare \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

Inside the pericope package, the complete selected bundle is loaded from the
pericope root as the hash-bound source. Out-of-pericope or external members are
loaded from `--member-bundles-dir`. In every case the agent-facing context is a
deterministic lean projection, not the complete selected bundle. The target
`29:0` basmala is injected automatically from that member root and is not listed
in `--add-ayat`.

To analyze the target basmala itself, make `S:0` an ordinary host-surah focus
and explicitly choose the numbered ayat that should activate it:

```bash
python3 _commentary/v4/workflow.py prepare \
  --analysis-id s029-p03-basmala \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --segment host=29:0,29:28-44 \
  --ayah 29:0
```

The pericope package manifest is mandatory for a flat context root. V4 verifies
its exact file set, bundle identities, raw and canonical hashes, builder hashes,
and pericope-index hash during preparation and every later manifest load.

Generated inputs are idempotent. If their semantic source changes, preparation
stops instead of mixing old raw output with new evidence. `--force-input`
updates generated input only; it never changes raw or editorial work.
Explicit `--source-bundle` and `--docket` overrides are single-unit options.

## Evidence boundary

Each scope prompt is self-contained. For every selected context unit,
preparation embeds the same HFT-style non-focus categories: a lean ayah record
and compact `branch_image_ar` cues for each mapped root target. It does not
embed that unit's word commentary, full QAC/coverage/root records, prior HFT,
reader products, inter-ayah rows, or channel material. The complete source
bundle stays outside the model-visible support and is bound by path, byte count,
canonical hash, projection hash, and lane-packet hash. The canonical stage is
prompt-bounded: it may read only the three packet files in the unit input, while
the three raw ledgers and governing documents are embedded in its prompt.
Provenance pointers inside a packet are not permission to read external files.

This is not an executor-enforced read sandbox. The handoff grants the worker the
repository workspace so it can write the declared outputs; compliance with the
evidence boundary remains an agent instruction. Exact-path checks prevent the
workflow or a returned handoff from following symlinked unit directories or
output filenames outside the three artifact roots.

V4 accepts `prefatory_basmala` units with explicit `unit_kind`, `surface_ref`,
and `linguistic_source_ref`. S:0 surface evidence belongs to the target surah
while QAC and word identities remain `1:1:*`; native HFT, inter-ayah, and
pericope scope are explicitly not applicable. For numbered ayahs in a surah
with a prefatory basmala, preparation snapshots `prefatory_basmala.bundle.json`
beside the focus source for provenance and projects it at ordinary context depth
into every micro, macro, and global lane packet. The snapshot itself is not
model-visible. Unit-manifest validation rechecks the snapshot bytes, canonical
bundle identity, deterministic context projection, selected-context lineage,
and every lane packet before workflow advancement.

## Deliberate omissions

Reader maps and invitation summaries are presentation derivatives and are not
part of the authoring core. They can be run downstream against committed
editorial files. Workspace policing is also outside v4: the handoff declares
exact output paths, and ordinary Git review shows every changed file.
