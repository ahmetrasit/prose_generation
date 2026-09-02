# Commentary v4

V4 keeps the v3 linguistic agents and removes the v3 run-management system.
It is a fixed four-agent workflow backed by Git, with exactly three artifact
roots:

```text
_commentary/v4/
  input/sNNN/S_A/       source snapshots, packets, prompts, one manifest
  raw/sNNN/S_A/         three analyst ledgers and four first-pass files
  editorial/sNNN/S_A/   four editorial files
```

V4 simplifies the authoring workflow, not upstream evidence construction. Its
starting contract is the existing validated v3 source bundle and adjudication
docket, and it reuses v3's packet projection code. `prepare` snapshots both into
the unit input; downstream agents never operate in the v3 authoring trees.

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

The one intentionally new prompt is `prompts/canonical.md`. It lets one fresh
writer perform reconciliation, prose preparation, and canonical composition in
one reasoning pass. That adaptation is required to remove the reconciler,
three scope-prose turns, and all repair loops. It does not impose a length
limit or a scripted semantic verdict. Explicit analyst decisions remain
authoritative; the adapter preserves their complete finding/evidence unions and
handles only lossless accounting recovery from the supplied packets.

## Commands

Prepare or advance one numbered ayah:

```bash
python3 _commentary/v4/workflow.py advance --ayah 29:38
```

The first call creates the unit input and returns three parallel scope
handoffs. Each analyst writes the JSON object it returns to the declared
`expected_response`. Run the same command again after all three files exist;
it creates one canonical prompt and returns the canonical writer handoff.

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

After the writer has produced both phases:

```bash
python3 _commentary/v4/workflow.py verify --ayah 29:38
```

`verify` checks generated-input identity, fixed-path and regular-file
boundaries, the first-pass hashes supplied to the editorial turn, and nonempty
outputs. It does not judge findings, request repairs, constrain prose, or
rewrite agent work. Git remains the history and review boundary for the final
editorial file bytes; v4 creates no completion receipt.

Use `prepare` directly when source paths need to be supplied explicitly:

```bash
python3 _commentary/v4/workflow.py prepare \
  --ayah 29:38 \
  --source-bundle path/to/29_38.bundle.json \
  --docket path/to/29_38.docket.json
```

Generated inputs are idempotent. If their semantic source changes, preparation
stops instead of mixing old raw output with new evidence. `--force-input`
updates generated input only; it never changes raw or editorial work.
Explicit `--source-bundle` and `--docket` overrides are single-ayah options.

## Evidence boundary

Each scope prompt is self-contained. The canonical stage is prompt-bounded: it
may read only the three packet files in the unit input, while the three raw
ledgers and governing documents are embedded in its prompt. The packets can be
large, so duplicating all three inside one canonical prompt would waste context
and reduce writing quality. Provenance pointers inside a packet are not
permission to read external files.

This is not an executor-enforced read sandbox. The handoff grants the worker the
repository workspace so it can write the declared outputs; compliance with the
evidence boundary remains an agent instruction. Exact-path checks prevent the
workflow or a returned handoff from following symlinked unit directories or
output filenames outside the three artifact roots.

V4 currently accepts numbered ayahs only. A prefatory basmala needs the planned
versioned `unit_kind`, `surface_ref`, and `linguistic_source_ref` protocol before
it enters authoring.

## Deliberate omissions

Reader maps and invitation summaries are presentation derivatives and are not
part of the authoring core. They can be run downstream against committed
editorial files. Workspace policing is also outside v4: the handoff declares
exact output paths, and ordinary Git review shows every changed file.
