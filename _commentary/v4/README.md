# Commentary v4

V4 is a Git-native rewrite of the commentary workflow. It preserves the v2/v3
linguistic and prose standard while reducing orchestration to:

```text
prepare
  -> micro, macro, global one-pass scope authors (fresh, parallel)
  -> canonical merge writer (fresh)
  -> editorial follow-up (same canonical writer)
  -> mechanical verify
```

There is no reconciler, scope repair, reconciliation repair, semantic retry,
session registry, or run-ID directory. An invalid artifact stops that unit. The
operator must inspect and explicitly replace or relocate it before continuing.

## Artifact layout

```text
_commentary/v4/
  input/<analysis-id>/sNNN/S_A/       snapshots, packets, prompts, manifest
  raw/<analysis-id>/sNNN/S_A/         3 contributions + 4 first-pass files
  editorial/<analysis-id>/sNNN/S_A/   4 editorial files
```

`native` is the default analysis ID. A custom ordered context uses a stable,
human-readable analysis ID so that different readings of the same focus have
disjoint paths.

Preparation derives the v3 docket in memory from a canonical non-tiered bundle,
projects the three evidence lanes, and snapshots every model input. It does not
depend on a v3 run, session, adjudication, or output tree. The manifest binds
source files, package manifests, context members, prompt sources, generated
packets, generated prompts, projection implementations, Quran text, and
inter-ayah inputs by path and SHA-256.

## Authoring contract

Each fresh scope author receives one self-contained lane prompt. In that single
turn it must:

1. decide every packet candidate exactly once;
2. preserve exact support, branch, connection, and context references;
3. state bounded findings and their reader payoffs; and
4. supply fluent, prose-ready Turkish movements.

The response is one `commentary-v4-scope-contribution-v1` JSON object written to
`raw/.../<lane>.contribution.json`. V4 checks identity, complete candidate
accounting, evidence-reference existence, and exactly one movement landing per
finding. These are structural checks. V4 does not alter an agent's substantive
accept, narrow, represent, or reject judgment.

The canonical writer receives only the three validated contributions, the
focus-surface record, and the governing v2/v3 texts. It does not receive or
reopen lane packets. Its job is to merge all supplied findings into the four
first-pass files without genericizing concrete context movements. The same live
writer then receives the unchanged v3 editorial instructions, bound to those
four first-pass hashes, and writes four separate editorial files.

See [ORCHESTRATION.md](ORCHESTRATION.md) for the cold-agent runbook.

## Basic commands

Start or advance one native numbered ayah:

```bash
python3 _commentary/v4/workflow.py advance --ayah 29:38
```

The first call prepares inputs and returns three `scope_authoring` handoffs.
After all three contribution files exist, run the same command to receive the
`canonical_write` handoff. After its four files exist, run it again to receive
the `canonical_editorial` handoff for the same live writer. Run `advance` once
more after editorial completion, then verify explicitly:

```bash
python3 _commentary/v4/workflow.py verify --ayah 29:38
```

The active manifest schema is `commentary-v4-unit-manifest-v5`. Existing
schema-v4 inputs and `.review.json` files are historical artifacts, not valid
one-pass state. Preserve their Git history, relocate legacy raw/editorial files,
then regenerate input explicitly with `advance --force-input`; raw and editorial
output is never deleted or adopted automatically.

Batch selectors accept explicit refs, comma lists, and same-surah ranges:

```bash
python3 _commentary/v4/workflow.py advance --ayah 100:1-11
python3 _commentary/v4/workflow.py advance --ayah 1:1-7 2:1-5
```

The batch result contains one unit result and a flat `parallel_handoffs` array.
Wait until a unit's current workers have finished writing before advancing that
unit again.

## Context membership

Native context follows the established lane boundary:

- `micro` is focus-local.
- Same-surah context in the focus segment is `macro`.
- Cross-segment or cross-surah selected context is `global`.

Explicit `--add-ayat` members are different from ordinary ordered segments.
They are inserted as first-class, non-focus members of the declared host surah
or pericope and therefore enter `macro` once. They use the same lean context
projection as every other non-focus ayah. They are never copied into all three
lanes and never become focuses implicitly.

List every external ayah explicitly. The option accepts repeatable,
comma-separated `S:A` refs and rejects ranges. Adding all of S1 means listing
all seven refs:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id s100-with-fatiha \
  --segment host=100:1-11 \
  --member-surah 100 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --ayah 100:1-11
```

An ordinary cross-surah segment remains available when global routing and focus
eligibility are intended:

```bash
python3 _commentary/v4/workflow.py advance \
  --analysis-id fatiha-lens-s100 \
  --segment fatiha=1:1-7 \
  --segment s100=100:1-11 \
  --ayah 100:1-11
```

The first invocation snapshots `analysis.json` beneath every focus input. Later
waves need only the stable analysis ID and selected refs. A reusable
`--analysis FILE` can replace repeated `--segment` declarations.

## Basmala policy

For every numbered focus in S2-S8 and S10-S114, the host surah's `S:0` bundle
is mandatory. Preparation snapshots it for provenance and inserts one lean,
ordinary non-focus context projection into `macro`. It has the same information
categories and depth as another context ayah. It is not a larger standalone
basmala package and is not duplicated across lanes. If the host `S:0` is also
declared in an ordinary segment, V4 normalizes it to the same macro route.

S1 already has its basmala as numbered ayah `1:1`. S9 has no prefatory
basmala. `1:0` and `9:0` are invalid.

To analyze a prefatory basmala itself, make `S:0` the focus:

```bash
python3 _commentary/v4/workflow.py advance --ayah 29:0
```

The CLI derives analysis ID `s029-basmala-full` and the ordered host segment
`29:0,29:1-69`. All numbered host ayat are ordinary lean macro context for the
basmala focus. An explicit composition with an `S:0` focus must contain the
same complete, canonical host-surah sequence; a basmala-only or pericope-only
focus fails closed.

`S:0` keeps target-surah surface identity while its word and QAC linguistic
identity remains `1:1`. Native HFT, inter-ayah, and native pericope evidence are
not applicable to the synthetic prefatory unit.

## Pericope packages

Build large-surah package roots with the wrapper, not by changing
`scripts/build_bundle.py`:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

It writes direct non-tiered ayah bundles and
`pericope.bundle-manifest.json` under
`bundles/sNNN-pericopes/pPP_AAA-BBB/`. Use that directory as the package root;
use `bundles/` as the member root for the mandatory host basmala and external
ayat:

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

Focus and ordinary package members must come from the package root. Explicit
external members may come from the package or member root; if both exist, their
canonical hashes must agree. Flat package roots require a valid pericope
manifest. V4 revalidates its exact file set, identities, hashes, builder hashes,
and pericope-index provenance on every manifest load.

## Evidence depth and verification

Every context member, including automatic basmala and `--add-ayat`, is reduced
to `commentary-v4-native-context-member-v1`: one lean ayah record plus compact
mapped branch images relevant to the current focus roots. Standalone-focus HFT,
reader products, full dictionaries, word analysis, inter-ayah material, and
channel payloads are excluded. The complete source remains hash-bound outside
the model-visible projection.

`verify` rechecks all persisted input records, source identities, canonical
hashes, Quran and inter-ayah sources, projection implementation hashes, context
projections, lane routing, prompt sources, contribution identity and structure,
first-pass hashes bound into the editorial handoff, and all eight nonempty
outputs. It also rejects unexpected non-hidden files in a unit's raw or
editorial directory. It does not score prose quality or rewrite agent work. Git
is the final history and review boundary.

Generated inputs are idempotent. If evidence or a prompt changes, preparation
stops instead of adopting existing prose under new inputs. `--force-input`
replaces generated input only; it never edits raw or editorial artifacts.
