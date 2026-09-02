# Commentary v4 orchestration

This is the complete runbook for a cold orchestrator. Do not invoke v3's
authoring state machine. V4 reads focus and context units from the single
`bundles/` root by default, derives the V3 docket in memory, and writes only
under `input/<analysis-id>/`, `raw/<analysis-id>/`, and
`editorial/<analysis-id>/`. Ordered compositions never fall back between roots.
If you intentionally run a controlled package source, pass an explicit
`--context-bundles-dir`; pass `--member-bundles-dir` separately for ayat added
to that package membership.

## Cold-start preflight

Run every command from the repository root. Bundle generation requires the
sibling `../quran-data/data/` source tree. The default Hermetic Focus Trace
policy also requires `../latent_activation/focus_trace/`; use
`--exclude-focus-trace` only for an intentional, provenance-recorded no-HFT
build.

Choose one source mode before starting agents:

1. For a native focus `S:A`, require
   `bundles/sNNN/S_A.ayah.json`. Build a missing numbered focus with:

   ```bash
   python3 scripts/build_bundle.py --surah S --ayah A --out bundles/sNNN
   ```

2. For every numbered focus in S2-S8 or S10-S114, also require the host
   prefatory bundle `bundles/sNNN/S_0.ayah.json`. Build it with:

   ```bash
   python3 scripts/build_bundle.py --surah S --ayah 0 --out bundles/sNNN
   ```

   S1 already has the basmala as numbered ayah `1:1`; S9 has no prefatory
   basmala. Never create `1:0` or `9:0`.

3. For a pericope focus, inspect the canonical index first:

   ```bash
   rg '"surah":\s*29' \
     ../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl
   python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
   ```

   If no index row exists, declare the span and label explicitly:

   ```bash
   python3 scripts/build_pericope_bundles.py \
     --surah 29 --pericope 3 --ayah-from 28 --ayah-to 44 \
     --pericope-label "Declared operator span"
   ```

   Use the emitted `bundles/sNNN-pericopes/pPP_AAA-BBB/` directory as
   `--context-bundles-dir`. The wrapper fails on stale extras or mismatched
   identities; do not copy unrelated bundle files into that package.

4. For a pericope run, load the host `S:0`, external ayat, and any deliberately
   selected out-of-pericope ayat from `--member-bundles-dir`. Build any missing
   member as an ordinary single-ayah bundle before preparation:

   ```bash
   python3 scripts/build_bundle.py --surah E --ayah A --out bundles/sEEE
   ```

   Every external ayah must be enumerated through `--add-ayat`; adding all of S1
   therefore means listing `1:1,1:2,1:3,1:4,1:5,1:6,1:7`.

Run `advance` without `--force-input` first. A pre-existing unit manifest is
revalidated against every recorded source, package manifest, packet, template,
and snapshot hash. If that validation reports stale input, inspect the source
change and `git diff` before using `--force-input`. That option replaces only
generated input; it never adopts, deletes, or rewrites raw or editorial work.

## One unit

1. Run:

   ```bash
   python3 _commentary/v4/workflow.py advance --ayah S:A
   ```

2. At `stage: scope_review`, start the returned micro, macro, and global
   handoffs as three fresh independent agents in parallel through the
   multi-agent spawn tool. Spawn each with model override `gpt-5.6-luna` and
   reasoning effort `max`; omit any priority/service-tier option. Give each
   agent its absolute prompt path and expected response path. The agent writes
   its exact returned JSON object to that path. Do not edit, normalize, or
   repair it.

3. Run `advance` again. It performs only JSON parsing and identity checks, then
   returns `stage: canonical_write`. It does not score semantic completeness or
   request repairs.

4. Start one fresh canonical writer through the multi-agent spawn tool with
   model override `gpt-5.6-luna` and reasoning effort `max`; omit any
   priority/service-tier option. Give it the returned canonical prompt and four
   raw output paths. Keep that live agent available. After it writes all four
   first-pass files, run `advance` again. This hashes those exact inputs and
   returns `stage: canonical_editorial`.

5. Send the returned editorial prompt and four declared editorial output paths
   to that same live writer. The handoff embeds the exact v3 editorial
   instructions and adds only the bound input hashes and destination map.

6. Run:

   ```bash
   python3 _commentary/v4/workflow.py verify --ayah S:A
   ```

7. Inspect `git diff` and commit the unit's `input/`, `raw/`, and `editorial/`
   artifacts together when accepted.

## Custom context

On the first wave, define the ordered composition and all desired focus units:

```bash
# Add one external ayah to every Fatiha focus.
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-with-17-50 \
  --segment fatiha=1:1-7 \
  --member-surah 1 \
  --add-ayat 17:50 \
  --ayah 1:1-7

# Fatiha followed by S100; every S100 ayah is a parallel focus.
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-lens-s100 \
  --segment fatiha=1:1-7 \
  --segment s100=100:1-11 \
  --ayah 100:1-11
```

For every later wave, retain the analysis ID in the command; the composition is
loaded from each unit's fixed input snapshot:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-lens-s100 --ayah 100:1-11
python3 _commentary/v4/workflow.py verify \
  --analysis-id fatiha-lens-s100 --ayah 100:1-11
```

An `--analysis FILE` JSON is equivalent to repeated `--segment`; it is the
preferred interface for a composition reused across separate invocations.
For each current focus, every other selected unit is context. This does not
rewrite the focus bundle's canonical pericope; it adds explicitly provenance-
bound context to the analysis packets. A same-surah unit in the focus's segment
goes to macro even when it lies outside the native pericope. A separate-segment
or cross-surah unit goes to global. Selected units can be discontinuous and
cross-surah, and their order and segment IDs are preserved. Do not put the same
unit in two segments. Direct `S:0` focus/context analysis uses this same
mechanism; name it explicitly because ranges cannot start at zero. Numbered
ayah packets for S2-S8 and S10-S114 automatically include the target surah's
`S:0` prefatory basmala as hash-bound surah-preface context in every lane.
Explicit `--add-ayat` refs are a separate context-only set: list each `S:A`
reference explicitly, comma-separated, and do not use ranges. They are
available to micro, macro, and global but are never eligible as focuses. Use an
ordinary segment only when its macro/global routing and focus eligibility are
intended; use `--add-ayat` for first-class external activation context.

## Pericope package roots

For larger surahs, build pericope package roots with the dedicated wrapper
instead of altering the whole-surah builder:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

This writes non-tiered direct ayah files under
`bundles/sNNN-pericopes/pPP_AAA-BBB/` plus
`pericope.bundle-manifest.json`. Use that directory as
`--context-bundles-dir`; V4 requires and revalidates the manifest for a flat
package root. Supply the mandatory host basmala and external/out-of-pericope
ayat through `--member-bundles-dir`. Only non-basmala external ayat need
explicit membership through `--member-surah` and `--add-ayat`:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

Inside the pericope, focus and selected same-package context are non-tiered.
Out-of-pericope members are read from the member root, so use the full, basic,
or tiered member root appropriate to the size budget and record that choice in
the command. Added ayat retain their original Quran identities and provenance;
the automatic basmala is always the host surah's `S:0`, never the source
surah's basmala for an external ayah.

For a dedicated basmala analysis, make `S:0` the host focus rather than an
added ayah and put its activating numbered ayat in the ordinary composition:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id s029-p03-basmala \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --segment host=29:0,29:28-44 \
  --ayah 29:0
```

## Rules

- Do not create or record session IDs. The workflow issues no agent-close
  operation and stores no lifecycle state.
- Do not run a post-scope repair checker. The canonical writer owns semantic
  reconciliation and can inspect every immutable lane packet.
- Each scope analyst receives one substantive turn. `coverage_complete: false`
  and other semantic limitations go forward to the canonical writer; they never
  create a scope repair turn.
- Do not modify analyst ledgers. Missing files receive their initial fixed
  handoff. Invalid, malformed, stale, or wrong-unit JSON stops that unit with an
  error; v4 does not turn it into an automated replacement or repair cycle. An
  operator may explicitly remove or replace the failed artifact and rerun the
  unit. A symlink or escaped output target is likewise a path-safety error that
  must be resolved explicitly.
- Never drive `advance` in an automatic retry loop. A unit error is terminal for
  that orchestration wave; report it while unrelated batch units continue.
- Do not use an existing commentary as evidence or as a gap checklist.
- If the live canonical conversation is lost before editorial completion,
  restart from `canonical.prompt.md`, regenerate all four first-pass files, run
  `advance` to rebind them, and apply the newly generated
  `editorial.prompt.md`. There is no session-recovery layer.
- A partial or failed run is ordinary Git-visible working state. Preserve it by
  commit or branch when it matters; v4 does not manufacture a second history.

## Parallel ayahs

Request a whole same-surah range or any explicit set in one command:

```bash
python3 _commentary/v4/workflow.py advance --ayah 100:1-11
python3 _commentary/v4/workflow.py advance --ayah 1:1-7 2:1-5
```

The command prepares units deterministically and returns a flat
`parallel_handoffs` array. Launch all returned handoffs concurrently. Each item
contains its `ayah_ref` and `stage`; never infer either from list order.

Do not call `advance` for an ayah while one of its workers is still writing.
Either wait for every handoff in the current batch wave and then rerun the full
batch, or rerun only the explicit ayah refs whose workers have returned. Output
presence is a file boundary, not an agent-liveness signal; v4 intentionally has
no persisted session registry from which to infer liveness.

For a canonical wave, retain an in-memory map from `ayah_ref` to that live
canonical writer. After the selected writer or full wave finishes first-pass
work, run `advance` for those completed refs, then send each
`canonical_editorial` handoff to the matching live writer. This map is temporary
executor state, not a persisted workflow session. If a writer is no longer
available, use that handoff's `restart_if_agent_unavailable` path and regenerate
the unit's complete first-pass set.

Different ayahs have disjoint fixed paths, so their scope, canonical, and
editorial work may run concurrently without a repository-wide guard. Do not run
two orchestrators for the same analysis ID and ayah at the same time. Native and
custom analyses of the same ayah have disjoint paths and may run concurrently.
A batch can contain mixed stages and unit errors; continue every returned
handoff and address only the reported failed units. `partial_error` deliberately
exits nonzero so automation cannot miss the failed unit, but its JSON and
`parallel_handoffs` remain valid.

Prefatory basmala units are valid for S2-S8 and S10-S114. Their target surface
and target-surah reader evidence remain `S:0`; word/QAC identities remain
canonical `1:1:*`; HFT, inter-ayah, and native pericope states are explicitly
not applicable. For numbered ayahs in those surahs, preparation snapshots
`prefatory_basmala.bundle.json` beside the focus source and embeds that full
bundle into each micro, macro, and global lane packet. Never synthesize `1:0`,
`9:0`, or `S:0:*` linguistic refs.
