# Commentary orchestration

How to produce commentary for any ayah or any surah, in any target language,
from a cold start. One file covers all layers because they are dependent: layer
3 consumes layer 2's outputs, and layer 2 is obliged to carry layer 3's
rejections.

Rules are in [`../PRINCIPLES.md`](../PRINCIPLES.md). What commentary is for is in
[`../COMMENTARY_SPEC.md`](../COMMENTARY_SPEC.md). This file is the run contract:
what to do, in what order, and what must exist before each step.

---

## Directory contract

```
_commentary/
  ORCHESTRATION.md          this file
  inputs/s{NNN}/            instantiated prompts — generated, never edited
    {S}_{A}.ayah.prompt.md
    {S}_{A}.ayah.{profile}.prompt.md
    {S}_{A}.ayah.manifest.json
    {S}_{A}.ayah.{profile}.manifest.json
    {NNN}.surah.prompt.md
    {NNN}.surah.manifest.json
  inputs/archive/s{NNN}/    archived non-default profile prompts
  outputs/s{NNN}/           agent-written
    {S}_{A}.prose.md
    {S}_{A}.evidence.md
    {S}_{A}.friction.md
    {S}_{A}.prose.{agent-type}.md       comparative runs
    {S}_{A}.evidence.{agent-type}.md
    {S}_{A}.friction.{agent-type}.md
    {NNN}.surah.prose.md    (and .evidence.md, .friction.md)

bundles/s{NNN}/             builder output — generated, never edited
  {S}_{A}.ayah.json
  {NNN}.surah.json
```

Everything under `inputs/` and `bundles/` is reproducible from
`../quran-data/` by re-running stages 1 and 2. Only `outputs/` is authored, and
only by an agent.

The unit id `{S}_{A}` uses unpadded surah and ayah (`100_1`, not `100_001`).
The surah id `{NNN}` is zero-padded to three (`s100/100.surah.json`). This
asymmetry is inherited from the builder; do not glob across it — the zero-padding
glob mismatch is a shipped bug in this repo's history.

## Task variables

| variable | example | notes |
| --- | --- | --- |
| `SURAH` | `100` | unpadded |
| `AYAH` | `1` | omit to process every ayah of the surah |
| `LAYER` | `ayah` | `ayah` \| `surah`; `pericope` is not yet implemented |
| `LANGUAGE` | `tr` | target prose language |
| `DATE` | `2026-07-27` | stamped into the prompt header |

`DATE` is the **only** non-deterministic input. Pass it explicitly to reproduce
an earlier prompt file byte-for-byte.

---

## Stage 1 — Build the bundle

```
python3 scripts/build_bundle.py --surah 100
python3 scripts/build_bundle.py --surah 100 --ayah 1     # one ayah
```

Reads `../quran-data/data/` and nothing else (D-a). Writes
`bundles/s{NNN}/`.

The builder runs a **preflight** that enumerates every expected source for the
surah and aborts with the complete gap list. It does not abort on the first
failure, and it does not proceed past a missing required source.

Three states are distinguished and must never be collapsed:

| state | meaning | builder behaviour |
| --- | --- | --- |
| absent | no file at the expected path | recorded in `coverage`, build continues if optional |
| parsed | file found, content extracted | normal |
| **present but empty** | file found, parser matched nothing | **hard failure** |

The third state is the defining bug class of this repo. Two shipped instances —
`branch_inventories: {}` for 110 surahs at exit 0, and a zero-padding glob that
dropped 15 of 30 files — plus two found by review in 2026-07-27 (a whole-surah
reading parser that handled one of three real line formats, and an ayah-walk
parser that required an em dash). A file that is found but yields nothing is
never reported as absent.

Required sources raise loudly. Optional sources record their absence in
`coverage`, which the writing agent then reports in its coverage note.

**Check before continuing:** read the `coverage` block of one ayah bundle. If a
source you expect to be present is marked absent, resolve that before
instantiating. Absence propagates silently into prose otherwise.

Current ayah bundles distinguish three V12 reader-derived families:

| bundle field | source | use |
| --- | --- | --- |
| `v12_reader_responses` | retired per-ayah focus runs | explicit absent/retired coverage field in the default lane |
| `v12_reader_walks` | regular full-context ayah walks | retrospective/full-context reader evidence |
| `v12_reader_walks_wide` | plus/minus-5 / 11-ayah-context walks | wider-window retrospective reader evidence |
| `v12_cross_run_publication` | compact final cross-run findings | coverage/priority check derived from regular plus wide readers |

The cross-run field is not prose to copy. It is a compact audit surface for what
the upstream publication run retained, graded, and anchored.

Per-ayah focus runs are no longer part of the default workflow. Normal bundles
use the surah `full_context_packet.json` branch inventory scoped to this ayah's
roots and anchored citations, plus regular/wide reader walks and cross-run
publication findings when present. A later audit can re-enable focus packets
explicitly, but that is no longer the production lane.

S1 basmalah lookup is explicit. Canonical commentary units keep `ayahRef: 1:1`;
some V12 reader/publication artifacts store that same basmalah as `1:0`.
Reader-walk lookup accepts both `1:1` and `1:0` for the S1 basmalah and records
the matched source ref per reader. Cross-run publication lookup records
`lookup_ref: 1:0` and `canonical_ayah_ref: 1:1`. This is source lookup
provenance, not hidden ayah renumbering.

## Stage 2 — Instantiate the prompt

```
python3 scripts/instantiate.py --surah 100 --layer ayah              # all ayahs
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah
python3 scripts/instantiate.py --surah 100 --layer surah
python3 scripts/instantiate.py --surah 100 --layer ayah --language tr --date 2026-07-27
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.6-sol-high
```

Writes `_commentary/inputs/s{NNN}/`. One prompt file plus one manifest per unit.
With `--profile`, the profile label is appended before `.prompt.md`, for example
`100_1.ayah.v2.5.6-sol-high.prompt.md`.

The prompt is **hermetic**: the task document, every governing document, every
cross-reference between them, and the bundle are inlined in full. The agent is
told explicitly that it has no filesystem and that a filename in the text is an
in-document pointer, not an instruction to go find a file.

This is not tidiness. It is what makes a cold agent runnable, what makes two
different models comparable on verifiably identical input, and what closed
friction #4 from the S1 baseline — that run reached outside its bundle because
nothing stopped it.

The manifest records every source path with its byte count. **Before running,
compare those byte counts against the working tree.** A mismatch means the
prompt was instantiated against a document you have since edited, and the run
will not reproduce.

Inlined per layer:

| layer | task document | governing | bundle |
| --- | --- | --- | --- |
| ayah | `_ayah_commentary/PROMPT.md` | `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, `docs/CHANNELS.md` | `{S}_{A}.ayah.json` |
| surah | `_surah_commentary/PROMPT.md` | same three | `{NNN}.surah.json` + every ayah bundle |

`docs/SOURCES.md` is deliberately not inlined. It documents how the bundle was
built, not how to write from it, and its content is already resolved into the
bundle. The dangling filename reference is left for the friction report to
surface if it disorients a writer.

## Stage 3 — Run layer 2, one agent per ayah

Feed one prompt file to one cold agent as its **entire** prompt. No system
prompt, no repo access, no other context, no conversation history.
Do not set a service-tier override when spawning these agents; use the model and
reasoning effort only.

**One agent per ayah is a correctness requirement, not a preference.** An agent
holding the whole surah writes ayah readings that are slices of a thesis it has
already formed (`COMMENTARY_SPEC.md` §4), and it cannot write 100:1 as if it had
not read 100:11. The isolation is what layer 3 later depends on: it reads
commentary written without knowledge of the argument, and therefore cannot be
retro-fitted to one.

Agents at this stage do not communicate. Run them in parallel.

The defining constraint the agent operates under is that **layer 2 does not
select** (`PRINCIPLES.md` §6). It carries the full field, including readings
that pull against each other. If it selects, the no-disambiguation guarantee is
gone and nothing downstream restores it.

### State A / State B

What the agent may do with channel material depends on what exists:

| | condition | permitted |
| --- | --- | --- |
| **State A** | an adjudicated ledger exists at `_surah_commentary/channels/s{NNN}.ledger.json` | carry a channel increment bounded by maturity |
| **State B** | only `channel_subchannels_anchored_here` from a first-pass review | let the material inform how this ayah's own words connect; **never name the channel** |

**State B is today's state for every surah.** No ledger exists anywhere. The
review is single-reader, no accept/reject, no maturity. Naming a channel from it
is exactly the unearned authority `PRINCIPLES.md` §2 forbids, and the reader
cannot tell the difference.

Both states are described in the inlined prompt; the agent reads its bundle and
determines which applies. The orchestrator does not need to tell it.

## Stage 4 — Layer 2.5, pericope — **not implemented**

No prompt, no registry entry in `instantiate.py`. Skip this stage; it is
specified here so the dependency is visible.

When it exists, a pericope agent consumes **layer 2 outputs plus surah scope**,
never raw ayah bundles. That is the compression step that makes layer 3
possible:

```
layer 2    per ayah      ayah bundle (~300 KB)           → prose + evidence (~1.5k words)
layer 2.5  per pericope  layer-2 OUTPUTS + surah scope   → pericope reading
layer 3    per surah     pericope outputs + surah bundle → argument + channel candidates
```

Spans come from
`../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl`
— 351 rows across 79 surahs, mean 4.4 per surah, mean span 16.8 ayahs.

**A surah with no rows there is one pericope**, so the same prompt serves both
and the stage is degenerate rather than blocking. The 35 uncovered surahs are all
short; the minimum segmented span is 10 ayahs. S100 has zero rows and is
therefore a single pericope.

A pericope **may select**, like layer 3, and hands its exclusions down to layer
2. `PRINCIPLES.md` §6's handoff table does not yet carry that row.

## Stage 5 — Run layer 3, one agent per surah

Blocked in the general case, and the block is measured, not projected.
Self-contained layer-3 prompt sizes for S100:

| unit | tokens |
| --- | ---: |
| `100_1.ayah` | 58k |
| `100_2` … `100_11.ayah` | 85k–100k each |
| **`100.surah`** | **907k** |

`{NNN}.surah.json` *references* its ayah bundles rather than duplicating them, so
hermetic instantiation must inline all of them. An 11-ayah surah already exceeds
any context window. **Layer 3 is unrunnable from raw bundles on anything but the
shortest surahs.**

The route through stage 4 is what fixes this: 11 ayah readings at ~1.5k words is
roughly 25k tokens. Until stage 4 exists, layer 3 can only be run by hand-feeding
layer-2 outputs, which is not reproducible and should not be treated as a pilot
result.

Layer 3 **selects** — it builds a thesis, and a thesis excludes. Its rejections
are handed to layer 2 (`PRINCIPLES.md` §6). It emits **channel candidates** and
does not compute maturity; adjudication is a separate step (`PLAN.md` action 8).

## Output contract — agent-owned

Every unit produces three files. The agent writes them; the orchestrator does not
edit them.

| file | content |
| --- | --- |
| `{unit}.prose.md` | continuous prose, target language, single voice, no provenance markers, no wrapper label such as `=== THE PROSE ===` |
| `{unit}.evidence.md` | phrase → bundle ref, with inference marked distinctly from bundle-traceable claims, plus a coverage note listing what was missing |
| `{unit}.friction.md` | every point where the instructions were ambiguous, contradictory, unsatisfiable, or silent |

For comparative runs, append a stable agent label before `.md`, for example
`100_1.prose.5.6-sol-high.md`. The label records the model/run class; it does
not change the content contract.

Arabic lexical items in prose may be authored as structured spans:

```
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

Renderers can then produce a reader edition with transliteration first, a
listener/TTS edition with the Arabic surface form, or a Turkish-only edition with
the gloss. Raw root skeletons, branch IDs, and letter-by-letter root
transliterations stay in evidence. Prose should attach root discussion to the
surface word, for example `el-âdiyât'ın bağlı olduğu kök alanı...`.

Prose and apparatus never mix (`PRINCIPLES.md` §12). Absence goes in the
coverage note, never in the prose — the reader does not learn a source was
missing; the reviewer does.

**The friction report is not optional and is not a courtesy.** It is the primary
instrument for improving the prompts. The 16-item report from the S1 baseline
falsified a quality verdict that had been reached by reading the prompts alone,
and every prompt fix since has come from it. An agent that returns prose without
friction has completed half the task.

## Batch orchestration

For a surah, in order:

1. `build_bundle.py --surah N` — one process
2. `instantiate.py --surah N --layer ayah` — one process, writes every unit
3. verify manifest byte counts against the working tree
4. spawn one agent per ayah, in parallel, each with one prompt file
5. collect three files per agent into `_commentary/outputs/s{NNN}/`
6. read the friction reports **before** reading the prose

Step 6 is deliberate. Prose reads as authoritative whether or not it is; the
friction report is where the instructions' failures are visible.

Stages 1 and 2 are idempotent. Re-running with the same `--date` overwrites with
identical bytes.

## Cross-model runs

The hermetic prompt is what makes this possible. To compare Claude against
another model, hand both the same `.prompt.md` file, unmodified, with no system
prompt. Any difference in output is attributable to the model.

Current S100 ayah pilot default:

```
model: gpt-5.6-sol
reasoning_effort: high
prompt_profile: v2.5.6-sol-high
output_label: v2.5.6-sol-high
per_ayah_focus_runs: retired
```

`gpt-5.6-sol` at `max` remains useful as a lexical/evidence comparator, but the
default reader-facing prose lane is the high-effort v2 profile until a later
pilot changes this record. Keep only the current default profile prompt in the
active `_commentary/inputs/s{NNN}/` path. Move comparator profile prompts to
`_commentary/inputs/archive/s{NNN}/` after use; they are reproducible with
`scripts/instantiate.py --profile`.

**Never evaluate on S1.** The governing documents inlined into every prompt
contain worked answers for 1:6 — `docs/CHANNELS.md:48` and `:216` state the
`sırât` finding and its branch id, `:132` gives the same finding in ready-made
Turkish, and `_ayah_commentary/PROMPT.md:33` asserts the doubled-article point.
Those are legitimate few-shot teaching of register and should stay. They make S1
useless as an eval surah.

S100 leaks five lines, and they say the horses are unattached and a channel
attaches them — where to look, not what to find. Near-inert for layer 2, since
State B bars naming channels. A real thumb on the scale for layer 3.

## Ablation runs

Ablations must change both the bundle and the prompt profile when a source is
removed from under a live instruction. Do not compare an ablated prompt against
an older control prompt built from a different bundle.

Two S100:1 ablation arms remain useful for experiments:

| arm | bundle mutation | prompt profile | purpose |
| --- | --- | --- | --- |
| `no-focus` | legacy label for the current default: scoped surah branch inventory and no `v12_reader_responses` | `v2.5.6-sol-high-no-focus` | reproduce the pilot that promoted the current default |
| `no-reader` | remove `v12_reader_walks`, `v12_reader_walks_wide`, `v12_cross_run_publication`, `butuncul_okuma_line`, and `channel_subchannels_anchored_here` | `v2.5.6-sol-high-no-reader` | test lexical/grammar commentary without reader-derived material |

Build and instantiate with:

```sh
python3 scripts/build_ablation_bundles.py --surah 100 --ayah 1 --mode no-focus --out /tmp/prose_generation_ablation_no_focus
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir /tmp/prose_generation_ablation_no_focus --profile v2.5.6-sol-high-no-focus --out _commentary/inputs/s100-ablation-no-focus

python3 scripts/build_ablation_bundles.py --surah 100 --ayah 1 --mode no-reader --out /tmp/prose_generation_ablation_no_reader
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir /tmp/prose_generation_ablation_no_reader --profile v2.5.6-sol-high-no-reader --out _commentary/inputs/s100-ablation-no-reader
```

## Decisions and rationale

| | decision | why |
| --- | --- | --- |
| D-a | `quran-data` is the only source root | three roots made silent divergence unnoticeable |
| D-b | no checksums or release pinning yet | git provides versioning; revisit once a workflow runs end to end |
| D-c | a pericope layer exists | forced by arithmetic, confirmed by the 907k measurement |
| D-d | one orchestration file for all layers | the layers are dependent; two files would diverge |
| D-e | input/output split, prompts hermetic | cold-agent runnable, cross-model comparable |
| D-f | S100 is the test surah, not S1 | contamination, above |
| D-g | do not generate the remaining 84 whole-surah readings | all long, none a candidate until layers 2/3 are validated |

## Completion-state limitation

This spec describes a workflow that has never been run end to end. What is known
to work, and what is not:

| stage | state |
| --- | --- |
| 1 build | runs; rewritten 2026-07-27 for `quran-data`-only, preflight, pericopes, gloss join |
| 2 instantiate | runs; verified deterministic by double-run diff |
| 3 layer 2 | exercised **once**, on 1:6, contaminated. Prose quality high; size and shape unresolved |
| 4 pericope | not implemented |
| 5 layer 3 | never run; blocked on stage 4 |

Two instructions in the inlined prompts are currently **unsatisfiable**, and
agents should be expected to report them:

- Layer 2 is told to pick up layer 3's excluded readings. No layer 3 output
  exists, so there is nothing to pick up.
- Layer 2 is told to pick up layer 1's `consideredNotPrimary` rejections. That
  field is not yet recorded in the anchor seeds, so those rejections are being
  destroyed rather than handed forward.

Both are real gaps in the pipeline, not errors in the prompt. They are named here
so a friction report that reports them is confirming a known state rather than
discovering a new one.

Three further items from the S1 baseline remain open: what counts as an
activated reading is now answered by `commentary_obligation` in the bundle, but
`PRINCIPLES.md` §9's never-filter rule is still not satisfiable against 143
inter-ayah rows, and no model prose exists for a State B move — the only worked
examples in `docs/CHANNELS.md` §3 are State A.
