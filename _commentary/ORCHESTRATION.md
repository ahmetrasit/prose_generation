# Commentary orchestration

How to produce commentary for any ayah or any surah, in any target language,
from a cold start. One file covers all passes because they are dependent: the
combined Layer 3 + 2.5 pass consumes cold Layer-2 prose and the reviewed channel
source, then writes both the whole-surah reading and its gradual ayah additions.

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
    {NNN}.channel.prompt.md
    {NNN}.channel.manifest.json
  inputs/archive/s{NNN}/    archived non-default profile prompts
  outputs/s{NNN}/           agent-written
    {S}_{A}.prose.md
    {S}_{A}.evidence.md
    {S}_{A}.index.md
    {S}_{A}.friction.md
    {S}_{A}.prose.{agent-type}.md       comparative runs
    {S}_{A}.evidence.{agent-type}.md
    {S}_{A}.index.{agent-type}.md
    {S}_{A}.friction.{agent-type}.md
    {NNN}.surah.prose.md
    {NNN}.surah.thesis.md
    {NNN}.surah.channels.reviewed.json
    {NNN}.ayah-channel-overlays.json
    {NNN}.ayah-channel-overlays.preview.md
    {NNN}.ayah-channel-overlays.friction.md
    {NNN}.surah.exclusions.md
    {NNN}.surah.evidence.md
    {NNN}.channel.friction.md

bundles/s{NNN}/             builder output — generated, never edited
  {S}_{A}.ayah.json
  {NNN}.surah.json
  {NNN}.channel.json
```

Everything under `bundles/`, and every ayah prompt under `inputs/`, is
reproducible from `../quran-data/` by re-running stages 1 and 2. Only `outputs/`
is authored, and only by an agent.

**The combined surah prompt is the exception**: it is built from `outputs/` as well, so
reproducing it needs the same layer-2 outputs, not just `quran-data`. Its
manifest names them with byte counts.

The unit id `{S}_{A}` uses unpadded surah and ayah (`100_1`, not `100_001`).
The surah id `{NNN}` is zero-padded to three (`s100/100.surah.json`). This
asymmetry is inherited from the builder; do not glob across it — the zero-padding
glob mismatch is a shipped bug in this repo's history.

## Task variables

| variable | example | notes |
| --- | --- | --- |
| `SURAH` | `100` | unpadded |
| `AYAH` | `1` | omit to process every ayah of the surah |
| `LAYER` | `ayah` | `ayah`; combined surah work uses `instantiate_channel.py` |
| `LANGUAGE` | `tr` | target prose language |
| `DATE` | `2026-07-27` | stamped into the prompt header |

`DATE` is the **only** non-deterministic input. Pass it explicitly to reproduce
an earlier prompt file byte-for-byte.

---

## Stage 1 — Build the bundle

```
python3 scripts/build_bundle.py --surah 100
python3 scripts/build_bundle.py --surah 100 --ayah 1     # one ayah
python3 scripts/build_bundle.py --surah 100 --require-focus-trace
python3 scripts/build_bundle.py --surah 100 --ayah 1 --require-focus-trace --focus-trace-variant 5.6-sol-high
```

Reads `../quran-data/data/` by default (D-a). With `--include-focus-trace` or
`--require-focus-trace`, it also reads the explicitly requested Hermetic Focus
Trace run under `../latent_activation/focus_trace/runs/s{NNN}/`. Writes
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

Current ayah bundles distinguish these V12 reader-derived families:

| bundle field | source | use |
| --- | --- | --- |
| `v12_reader_responses` | retired per-ayah focus runs | explicit absent/retired coverage field in the default lane |
| `v12_focus_trace_hermetic` | opt-in one-call reconstructed focus trace from `../latent_activation/focus_trace` | baseline/context-delta/outlier evidence for surprise and changed reading |
| `v12_reader_walks` | regular full-context ayah walks | retrospective/full-context reader evidence |
| `v12_reader_walks_wide` | plus/minus-5 / 11-ayah-context walks | wider-window retrospective reader evidence |
| `v12_cross_run_publication` | compact final cross-run findings | coverage/priority check derived from regular plus wide readers |

The cross-run field is not prose to copy. It is a compact audit surface for what
the upstream publication run retained, graded, and anchored.

Channel generated outputs are also surfaced as a lightweight manifest:
`channel_generated_outputs.files[]` names the quran-data files available for the
surah (`channel_candidates`, `channel_families`, `family_branch_inventory`,
semantic path-family summaries, and related summaries). The bundle does not
inline them because they can be large. If a run gives the agent filesystem
access, the agent may read only the listed files when channel detail is
necessary. These generated outputs are candidate/family/path evidence, not an
adjudicated ledger; State B restrictions still apply.

Retired staged per-ayah focus runs remain outside the default lane. Normal
bundles use the surah `full_context_packet.json` branch inventory scoped to this
ayah's roots and anchored citations, plus regular/wide reader walks and
cross-run publication findings when present.

Hermetic Focus Trace is the replacement ayah-level signal when a run explicitly
asks for it. Use `--include-focus-trace` to surface packet/readiness coverage
without failing on missing reader JSON. Use `--require-focus-trace` for the
actual focused commentary run after upstream readers are complete; it fails
preflight unless every target ayah has a reader response.

Use `--focus-trace-variant` when the same focus ayah has multiple HFT response
files. The unlabelled filename is variant `default`; labelled filenames such as
`100_1.5.5-high.focus_trace.json` and
`100_1.5.6-sol-high.focus_trace.json` are variants `5.5-high` and
`5.6-sol-high`. Build separate bundle/input directories for direct Layer-2
comparisons.

This should stay the same Layer-2 workflow, not a separate writer workflow:
Focus Trace is an evidence source for the ayah's before/after experience. Use a
separate bundle/output directory only when running controlled comparisons, such
as HFT versus no-HFT or no-reader ablations.

### Optional upstream focus-trace generation

If focused Layer 2 is required and reader JSONs do not exist yet, generate them
upstream in `../latent_activation/focus_trace` before the final bundle build. Do
not ask a commentary agent to create these files.

For each missing ayah response, spawn one focus-trace worker with:

```text
agent_type: worker
model: gpt-5.6-sol
reasoning_effort: max
service_tier: priority
fork_context: false
```

Each worker receives only
`focus_trace/prompts/focus_trace_hermetic.md`,
`focus_trace/schemas/focus-trace-response.schema.json`, and its assigned packet
`focus_trace/runs/sNNN/packets/{S}_{A}.packet.json`. It writes exactly one file:

```text
focus_trace/runs/sNNN/readers/<reader_id>/{S}_{A}.focus_trace.json
```

For comparison variants, keep the same reader directory and write the variant
label into the filename:

```text
focus_trace/runs/sNNN/readers/<reader_id>/{S}_{A}.{variant}.focus_trace.json
```

The unlabelled filename is `--focus-trace-variant default`; labelled filenames
are selected with the label after `{S}_{A}.`, such as `5.5-high` or
`5.6-sol-high`.

Validate each response with
`focus_trace/scripts/validate_focus_trace.py`, then rerun
`python3 scripts/build_bundle.py --surah {S} --require-focus-trace` so the
commentary bundle sees `coverage.v12_focus_trace_hermetic.present: true`. The
S100 continuation runbook is
`../latent_activation/focus_trace/runs/s100/COLD_HANDOFF.md`.

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
python3 scripts/instantiate.py --surah 100 --layer ayah --language tr --date 2026-07-27
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --profile v2.5.6-sol-high
```

Writes `_commentary/inputs/s{NNN}/`. One prompt file plus one manifest per unit.
With `--profile`, the profile label is appended before `.prompt.md`, for example
`100_1.ayah.v2.5.6-sol-high.prompt.md`.

The prompt is **hermetic by default**: the task document, every governing
document, every cross-reference between them, and the bundle are inlined in
full. A filename in the text is normally an in-document pointer, not an
instruction to go find a file.

The exception is an explicit source manifest inside the bundle. Today this is
`channel_generated_outputs.files[]`: if the run gives the agent read access, it
may inspect only those listed quran-data files when channel detail is necessary.
This keeps cold runs comparable while making large 111/114 channel output files
available without inlining them into every ayah prompt.

This is not tidiness. It is what makes a cold agent runnable, what makes two
different models comparable on verifiably identical input, and what closed
friction #4 from the S1 baseline — that run reached outside its bundle because
nothing stopped it.

The manifest records every source path with its byte count. **Before running,
compare those byte counts against the working tree.** A mismatch means the
prompt was instantiated against a document you have since edited, and the run
will not reproduce.

Inlined per layer:

| layer | task document | governing | bundle | upstream |
| --- | --- | --- | --- | --- |
| ayah | `_ayah_commentary/v1/PROMPT.md` | `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, `docs/CHANNELS.md` | `{S}_{A}.ayah.json` | — |
| combined 3 + 2.5 | `_channel/PROMPT.md` | selected excerpts + both schemas | `{NNN}.channel.json` | every Layer-2 `prose` file |

**The combined pass consumes Layer-2 prose, not raw ayah bundles.** Exact channel
identity comes from the compact reviewed-channel bundle, so Layer-2 evidence and
index files are not repeated. The contract still depends on commentary written
in isolation; re-deriving it from source would defeat stage 3.

```
python3 scripts/instantiate_channel.py --surah 100
python3 scripts/instantiate_channel.py --surah 100 --layer2-dir _commentary/outputs/s100-default
python3 scripts/instantiate_channel.py --surah 100 --layer2-label default.v2.5.6-sol-high
python3 scripts/instantiate.py --surah 103 --layer surah --inline-ayah-bundles
```

`--layer2-dir` defaults to `_commentary/outputs/s{NNN}-default`, then
`s{NNN}`. `--layer2-label` picks one comparative run when a directory holds
several; without it, an ambiguous directory is an error listing the candidates
rather than a silent choice. Missing `prose` or `evidence` for any ayah aborts
with the complete gap list; a **present but empty** output file is a hard failure,
never an absence. A missing `index` is recorded as coverage and passed to the
agent, because no layer-2 run has produced one yet.

For a present index, instantiation also records
`surprise_rows_absent_for_ayahs`. This is a handoff gap, not proof that the prose
contains no secondary resonance: it says layer 2 did not explicitly state
whether a coherent secondary line supports or shifts the primary.

Layer-2 **friction** reports are deliberately not inlined. They report on the
instructions, not on the ayahs.

`--inline-ayah-bundles` restores the raw-bundle prompt. It is viable only for the
shortest surahs — S103, at three ayahs, is 1.8 MB — and exists for reproducing
the measurement below.

`docs/SOURCES.md` is deliberately not inlined. It documents how the bundle was
built, not how to write from it, and its content is already resolved into the
bundle. The dangling filename reference is left for the friction report to
surface if it disorients a writer.

## Stage 3 — Run layer 2, one agent per ayah

Feed one prompt file to one cold agent as its **entire** prompt. No system
prompt, no other context, no conversation history. Repo/file reads are limited to
explicit external-source manifests in the bundle, currently
`channel_generated_outputs.files[]`.
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

### Local surprise boundary

The Layer-2 agent states locally grounded surprise readings, not channels. Its
prose keeps the primary floor visible, enters through this ayah's own word,
states the secondary line, and says whether that line supports or shifts the
primary. The index repeats the synthesis under `surprise:<id>` with
`[supports-primary]` or `[shifts-primary]`.

`channel_subchannels_anchored_here` and `channel_generated_outputs` may help the
agent notice local evidence. They do not license recurrence, maturity, or a
surah-wide name. Even when a reviewed plan later exists, the canonical cold
Layer-2 pass remains unchanged; channel disclosure is a Layer-2.5 overlay.

## Stage 4P — Optional pericope compression (`2P`)

This pass is not implemented and is not blocking for short surahs. It is
reserved for long surahs whose Layer-2 prose does not fit one combined prompt:
11 ayah readings are about 140 KB, while S2's 286 would be about 3.6 MB.

```
layer 2   per ayah      ayah bundle                     -> prose + evidence
layer 2P  per pericope  layer-2 outputs + surah scope   -> pericope reading
combined  per surah     reviewed channels + layer-2/2P  -> argument + channel prose + overlays
```

Pericope spans come from
`../quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl`.
A surah with no rows there is one pericope. `2P` is deliberately not called
Layer 2.5: it runs before the combined pass and compresses; Layer 2.5 is the
overlay portion of that combined pass.

## Stage 5 — Build and instantiate combined Layer 3 + 2.5

**Prerequisite: Layer 2 is complete for the surah.**

```
python3 scripts/build_channel_bundle.py --surah 87
python3 scripts/check_channel_bundle.py bundles/s087/87.channel.json --surah 87
python3 scripts/instantiate_channel.py --surah 87 \
  --layer2-label default.v2.5.6-sol-high --date 2026-07-28
```

The bundle compiler begins with the reviewed channel systems and joins each
root/branch citation to exact QAC/root anchors. The instantiator adds only the
unchanged Layer-2 prose. It refuses a partial, empty, or ambiguous prose handoff.

## Stage 6 — Run one combined agent per surah

Feed `{S}.channel.prompt.md` to one cold agent. It writes:

- the primary-grounded surah argument and thesis;
- the completed surprising channel reading;
- `{S}.surah.channels.reviewed.json` with exact members and maturity;
- `{S}.ayah-channel-overlays.json` and a merged preview;
- exclusions, evidence, and friction.

There is no second channel-admission pass. Upstream review establishes the
channel systems; this pass integrates them, derives reader-order maturity, and
designs disclosure. The cold Layer-2 prose remains canonical.

## Stage 7 — Validate plan and overlays

```
python3 scripts/check_channel_plan.py \
  _commentary/outputs/s087-default/87.surah.channels.reviewed.json \
  --state reviewed --bundle bundles/s087/87.channel.json
python3 scripts/check_channel_overlays.py \
  _commentary/outputs/s087-default/87.ayah-channel-overlays.json \
  --plan _commentary/outputs/s087-default/87.surah.channels.reviewed.json
```

The completed preview is the human gate: the whole-surah channel prose should
feel like recognition, while every original local surprise remains intact.

## Output contract — agent-owned

An ayah unit produces four files. The combined surah unit produces the artifacts
named in `_channel/PROMPT.md`. The agent writes them; the orchestrator does not
edit them.

| file | content |
| --- | --- |
| `{unit}.prose.md` | continuous prose, target language, single voice, no provenance markers, no wrapper label such as `=== THE PROSE ===` |
| `{unit}.evidence.md` | phrase → bundle ref, with inference marked distinctly from bundle-traceable claims, plus a coverage note listing what was missing |
| `{unit}.index.md` | one line per reading the prose carries — `` - `<ref>` — <clause> `` — with `[inference]` on the writer's own readings; plus one `surprise:<id>` synthesis row per earned local surprise, marked `[supports-primary]` or `[shifts-primary]`. Checked by `scripts/check_index.py` |
| `{unit}.friction.md` | every point where the instructions were ambiguous, contradictory, unsatisfiable, or silent |

For comparative runs, append a stable agent label before `.md`, for example
`100_1.prose.5.6-sol-high.md`. The label records the model/run class; it does
not change the content contract.

Arabic lexical items in prose may be authored as structured spans:

```
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

Use the full span at first mention of an ayah word, and again when the prose
returns to that word after another word or another paragraph. Renderers can then
produce a reader edition with transliteration first, a listener/TTS edition with
the Arabic surface form, or a Turkish-only edition with the gloss. Raw root
skeletons, branch IDs, and letter-by-letter root transliterations stay in
evidence. Prose should attach root discussion to the surface word, for example
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`.

Prose paragraphs may begin with the ayah's surface, a concrete image, or a
reader-facing claim. They should not begin with a bare grammar label or stacked
abstractions. "Âyet önce hamdi Allah'a verir; sabit ad cümlesi bu hamdi yerleşik
bir hüküm olarak taşır" is better than opening with "Bu âyet, tek bir isim
cümlesiyle yerleşik bir hüküm kurar."

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
5. collect each agent's files into `_commentary/outputs/s{NNN}/`
6. `check_index.py --surah N` — mechanical, before any reading (ayah units);
   add `--require-surprise` only when the run criterion requires an explicit
   local surprise in every unit
7. read the friction reports **before** reading the prose
8. `build_channel_bundle.py --surah N`; validate the compact reviewed-channel bundle
9. `instantiate_channel.py --surah N` — reads only Layer-2 prose from step 5
10. spawn one combined Layer 3 + 2.5 agent with that prompt
11. validate `{S}.surah.channels.reviewed.json`
12. validate `{S}.ayah-channel-overlays.json` against the reviewed plan
13. read the overlay preview and friction before accepting the surah prose

The ordering of steps 6 and 7 is deliberate. Prose reads as authoritative whether
or not it is, so both the mechanical check and the friction report — where the
instructions' failures are visible — come first.

Step 9 is where the layers join, and the join is a file read: whatever Layer-2
prose is in `_commentary/outputs/s{NNN}/` at that moment is what the combined
pass sees. Re-running Layer 2 afterward requires re-instantiation. The channel
manifest records every source with byte count and hash.

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
Turkish, and `_ayah_commentary/v1/PROMPT.md:33` asserts the doubled-article point.
Those are legitimate few-shot teaching of register and should stay. They make S1
useless as an eval surah.

S100 leaks five lines, and they say the horses are unattached and a channel
attaches them — where to look, not what to find. This is a real thumb on the
scale for layer 3, but it does not supply the local secondary turns layer 2 must
still derive from its own bundle.

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
python3 scripts/build_ablation_bundles.py --surah 100 --ayah 1 --mode no-focus --out _commentary/work/prose_generation_ablation_no_focus
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir _commentary/work/prose_generation_ablation_no_focus --profile v2.5.6-sol-high-no-focus --out _commentary/inputs/s100-ablation-no-focus

python3 scripts/build_ablation_bundles.py --surah 100 --ayah 1 --mode no-reader --out _commentary/work/prose_generation_ablation_no_reader
python3 scripts/instantiate.py --surah 100 --ayah 1 --layer ayah --bundles-dir _commentary/work/prose_generation_ablation_no_reader --profile v2.5.6-sol-high-no-reader --out _commentary/inputs/s100-ablation-no-reader
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
| 2 instantiate | runs for both layers; verified deterministic by double-run diff |
| 3 layer 2 | complete for S1 (7), S87 (19), S100 (11), S103 (3) in the default lane; S87 predates explicit channel rows |
| 4 pericope | not implemented; needed for long surahs, not for these four |
| 5 layer 3 | instantiates; **never run** |

Two instructions in the inlined prompts are currently **unsatisfiable**, and
agents should be expected to report them:

- Layer 2 is told to pick up layer 3's excluded readings. No layer 3 output
  exists, so there is nothing to pick up.
- Layer 2 is told to pick up layer 1's `consideredNotPrimary` rejections. Only
  `s100.1-5.primary-anchors.json` records that field; the S1 and S103 seeds have
  none and S100:6–11 have none, so those rejections are being destroyed rather
  than handed forward.
Both are real gaps in the pipeline, not errors in the prompt. They are named here
so a friction report that reports them is confirming a known state rather than
discovering a new one.

Three further items from the S1 baseline remain open: what counts as an
activated reading is now answered by `commentary_obligation` in the bundle, but
`PRINCIPLES.md` §9's never-filter rule is still not satisfiable against 143
inter-ayah rows. The S87 default run demonstrates that State B material can
produce strong local resonances, but it predates the explicit channel-turn
contract: its prose often contains the material without stating whether it
supports or shifts the primary. A fresh run is still needed to validate the new
handoff.
