# Commentary v5

V5 is a simple prompt-preparation workflow for ayah commentary. The code does
one bounded job: validate the available inputs, assemble the hermetic evidence
needed for the focus, and write three scope prompts.

```text
prepare
  -> micro, macro, global scope agents in parallel
  -> same three agents write scope prose after nomination
  -> one consolidator merges the three prose drafts without dropping findings
  -> same consolidator writes the editorial version without reducing coverage
```

There is no V5 state machine after `prepare`: no `advance`, no `verify`, no
manifest audit, no repair loop, and no hidden session registry. After the three
prompts exist, orchestration is normal agent management and Git-visible files.

## Basic Command

Native focus:

```bash
python3 _commentary/v5/workflow.py prepare --ayah 29:38
```

Batch focus selectors are accepted:

```bash
python3 _commentary/v5/workflow.py prepare --ayah 100:1-11
python3 _commentary/v5/workflow.py prepare --ayah 1:1-7 2:1-5
```

The command writes one prompt per lane:

```text
_commentary/v5/input/<analysis-id>/sNNN/S_A/micro.discovery.prompt.md
_commentary/v5/input/<analysis-id>/sNNN/S_A/macro.discovery.prompt.md
_commentary/v5/input/<analysis-id>/sNNN/S_A/global.discovery.prompt.md
```

The first scope-agent turn writes the matching discovery files under `raw/`:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/micro.discovery.json
_commentary/v5/raw/<analysis-id>/sNNN/S_A/macro.discovery.json
_commentary/v5/raw/<analysis-id>/sNNN/S_A/global.discovery.json
```

It also creates the matching raw and editorial output directories for agent
work:

```text
_commentary/v5/raw/<analysis-id>/sNNN/S_A/
_commentary/v5/editorial/<analysis-id>/sNNN/S_A/
```

The JSON printed by `prepare` contains the generated prompt paths, the
focus/context brief, and short orchestration notes. It is advisory; it is not a
completion manifest.

Consolidation is prose work, not evidence selection. Every retained scope
finding must keep its carrier, independent trigger, contact, changed reading,
concrete semantic detail, and boundary visible in the reader-facing result.
When one scope paragraph contains multiple claims, images, branches, or
movements, each distinct one is a separate mandatory landing.
Editorial rewriting may improve Turkish and cadence, but it must not reduce
that coverage.

## Context And External Ayat

An ordered analysis uses named segments. Same-surah context in the focus
segment is macro; ordinary cross-segment or cross-surah context is global.

Explicit external ayat use `--add-ayat`. They are first-class, context-only
members of `--member-surah`, enter macro once, retain their original Quran
identity, and receive root cues conditioned by the host-surah focus. They never
become focus ayat implicitly. The option accepts comma-separated individual
refs and rejects ranges. To add all of S1, list all seven ayat:

```bash
python3 _commentary/v5/workflow.py prepare \
  --analysis-id s100-with-fatiha \
  --segment host=100:1-11 \
  --member-surah 100 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --ayah 100:1-11
```

## Basmala Policy

For every numbered focus in S2-S8 and S10-S114, the host `S:0` prefatory
basmala is mandatory. It enters macro exactly once as the same lean, ordinary
non-focus context projection used for any other context ayah. It does not carry
its standalone-focus payload into another ayah's prompt.

S1 already contains its basmala as `1:1`; S9 has no prefatory basmala. `1:0`
and `9:0` are invalid.

A prefatory basmala can itself be the focus:

```bash
python3 _commentary/v5/workflow.py prepare --ayah 29:0
```

That derives analysis `s029-basmala-full` with `29:0,29:1-69` in one host
segment. All numbered host ayat become ordinary lean macro context. The focus
surface remains `29:0`; its canonical linguistic source `1:1` is an alias, not
external context.

## Pericope Packages

Use the dedicated wrapper instead of adding pericope behavior to
`scripts/build_bundle.py`:

```bash
python3 scripts/build_pericope_bundles.py --surah 29 --pericope 3
```

For a pericope plus external Fatiha context:

```bash
python3 _commentary/v5/workflow.py prepare \
  --analysis-id s029-p03-with-fatiha \
  --context-bundles-dir bundles/s029-pericopes/p03_028-044 \
  --member-bundles-dir bundles \
  --member-surah 29 \
  --add-ayat 1:1,1:2,1:3,1:4,1:5,1:6,1:7 \
  --segment p03=29:28-44 \
  --ayah 29:38
```

Focus and ordinary pericope members come from the package root. Automatic
basmala and explicit external members may come from the member root. If an
external member exists in both roots, the canonical bundle content must agree.

See [ORCHESTRATION.md](ORCHESTRATION.md) for the cold-agent runbook.
