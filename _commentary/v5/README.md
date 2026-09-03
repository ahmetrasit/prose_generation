# Commentary v5

V5 keeps V4's hermetic evidence, composition, basmala, external-ayah, and
provenance behavior. It changes authoring into two planned lane turns so that
evidence discovery is completed before prose pressure begins:

```text
prepare
  -> micro, macro, global discovery agents (fresh, parallel)
  -> composition follow-up to those same three agents (parallel)
  -> canonical writer (fresh)
  -> editorial follow-up to the same canonical writer
  -> verify
```

There is no reconciler, repair stage, semantic retry loop, or persisted agent
session. Invalid artifacts stop the unit. Git-visible files and their hashes are
the workflow state.

## Why V5

V4 asked each lane agent to discover candidates, audit hundreds of unrelated
branch facets, and write polished prose in one response. It then made every
scope sentence verbatim-immutable. That combination could suppress uncandidate
discoveries, preserve generic wording instead of exact mechanisms, and carry
English source phrases into editorial prose.

V5 instead makes the structured discovery ledger authoritative and keeps prose
editable:

- candidates are reviewed, but do not limit independent discovery;
- only candidate-attached branches, explicitly nominated facets, context refs,
  and semantic obligations require negative accounting;
- candidate-specific word/channel evidence and HFT activation traces,
  before/after readings, and containment become named obligations;
- retained context must occur in an activation carrier or trigger;
- a specialization cannot survive without its branch's core facet;
- word-analysis candidates receive source-derived root IDs without automatic
  branch nomination, plus a compact non-nominating branch index for discovery;
- lane, canonical, and editorial reader prose reject obvious English leakage;
- canonical and editorial landing maps preserve exact declared traceability
  while wording may be rewritten or fluently grouped.

The full packet is embedded only in the discovery prompt. The planned
composition prompt carries the validated finding set and compact semantic
requirements; the canonical prompt carries the same prose-relevant requirements
with provenance-only metadata removed. Agent responses do not echo source
hashes or source payloads. Evidence contains one compact provenance ledger per
finding, while the index contains only its hash.
Hard byte budgets stop accidental packet or ledger dumps in prompts and output
files. The current ceilings are 4.8 MB per lane packet, 5 MB per discovery
prompt, 4 MB per composition or canonical prompt, and 512 KB per editorial
handoff. Discovery and composition responses are capped at 2 MB and 1 MB,
respectively; each semantic record is capped at 32 KB. Preparation keeps at
most 80 optional candidates and never truncates an over-budget inventory.

## Artifact Layout

```text
_commentary/v5/
  input/<analysis-id>/sNNN/S_A/
    source.bundle.json
    docket.json
    manifest.json
    <lane>.packet.json
    <lane>.discovery.prompt.md
    <lane>.composition.prompt.md       # after valid discovery
    canonical.prompt.md                # after all lane compositions
    editorial.prompt.md                # after first pass
  raw/<analysis-id>/sNNN/S_A/
    <lane>.discovery.json
    <lane>.contribution.json
    S_A.{prose,evidence,index,friction}.tr.md
  editorial/<analysis-id>/sNNN/S_A/
    S_A.{prose,evidence,index,friction}.editorial.tr.md
```

Active schemas are `commentary-v5-unit-manifest-v1`,
`commentary-v5-lane-evidence-packet-v1`,
`commentary-v5-scope-discovery-v1`, and
`commentary-v5-scope-composition-v1`.

## Basic Commands

Start or advance one native ayah:

```bash
python3 _commentary/v5/workflow.py advance --ayah 29:38
```

The command is idempotent and returns only the next valid handoff. Run the same
command after each complete agent wave. Verify a completed unit with:

```bash
python3 _commentary/v5/workflow.py verify --ayah 29:38
```

Ranges and repeated selectors are supported for batch orchestration:

```bash
python3 _commentary/v5/workflow.py advance --ayah 100:1-11
python3 _commentary/v5/workflow.py advance --ayah 1:1-7 2:1-5
```

See [ORCHESTRATION.md](ORCHESTRATION.md) for the exact cold-agent procedure.

## Context And External Ayat

An ordered analysis uses named segments. Same-surah context in the focus
segment is macro; ordinary cross-segment or cross-surah context is global.

Explicit external ayat use `--add-ayat`. They are first-class, context-only
members of `--member-surah`, enter macro once, retain their original Quran
identity, and receive root cues conditioned by the host-surah focus. They never
become focus ayat implicitly. The option accepts repeatable comma-separated
individual refs and rejects ranges. To add all of S1, list all seven ayat:

```bash
python3 _commentary/v5/workflow.py advance \
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
its standalone-focus payload into another ayah's packet.

S1 already contains its basmala as `1:1`; S9 has no prefatory basmala. `1:0`
and `9:0` are invalid.

A prefatory basmala can itself be the focus:

```bash
python3 _commentary/v5/workflow.py advance --ayah 29:0
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
python3 _commentary/v5/workflow.py advance \
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
external member exists in both roots, canonical hashes must agree. Flat package
roots require a valid `pericope.bundle-manifest.json`, which is revalidated on
every manifest load.

## Verification Boundary

`verify` rechecks paths, byte counts, raw and canonical hashes, source identity,
package manifests and builder hashes, context projections, implementation and
prompt hashes, discovery/composition identities, editorial input hashes, fixed
output names, declared landing-map coverage, compact provenance placement,
artifact size budgets, internal-ID leakage in prose, and obvious English in all
human-authored Turkish output text.

The check is intentionally mechanical. It verifies identity, ordering, hashes,
and exact quote placement for the agent-declared semantic map. It cannot prove
that a Turkish passage entails its mapped source semantics, or decide whether
an interpretation is substantively persuasive; those remain authoring quality
responsibilities.
