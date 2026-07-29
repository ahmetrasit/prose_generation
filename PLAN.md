# Plan

Numbered actions in execution order. Refer to them by number.

Last updated 2026-07-28. Rules in [`PRINCIPLES.md`](PRINCIPLES.md), per-surah
state in [`STATUS.md`](STATUS.md), channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

> **Layer 3 update:** the combined channel/overlay plan below is retained as
> historical planning. Active Layer 3 work now follows
> [`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).

---

## Decisions taken (2026-07-27)

**D-a. quran-data is the single source.** The builder read three roots
(`quran-data`, `latent_activation`, `quran-slm`). All commentary inputs now live
under `quran-data/data/`. Migration verified complete — see *Source inventory*
below.

**D-b. No checksums or release pinning yet.** Git provides versioning. Revisit
once a workflow runs end to end.

**D-c. Long surahs may need a pericope compression pass (`2P`).** Forced by arithmetic: a surah agent
for S2 would need 286 × ~300 KB. Pericope spans come from
`analysis/channels/network-v3/pericopes/surah_pericopes.jsonl` — 351 rows, 79
surahs, mean 4.4 per surah, mean span 16.8 ayahs. The 35 uncovered surahs are all
short (min segmented span is 10 ayahs); **for them the surah is one pericope**, so
the same prompt serves both.

**Layer 2's output is the compression step:**

```
layer 2    per ayah      ayah bundle (~300 KB)          → prose + evidence (~1.5k words)
layer 2P   per pericope  layer-2 OUTPUTS + surah scope  → pericope reading
combined   per surah     reviewed channels + layer-2/pericope prose → argument + channels + overlays
```

A pericope agent never sees raw ayah bundles. 17 ayah readings ≈ 34k tokens. This
also preserves the guarantee: the pericope agent reads ayah commentary written in
isolation and cannot retro-fit it to a thesis.

A pericope **may select**, like layer 3, handing exclusions down to layer 2.
`PRINCIPLES.md` §6's handoff table must be updated to add the row.

**D-d. One orchestration file covering all three layers**, because they are
dependent. Modelled on `quran-slm/inter-ayah/ORCHESTRATION_SPEC.md` (directory
contract → task variables → stages → output contract → batch → decisions →
completion-state limitation).

**D-e. Input/output split, and prompts are hermetic.** The instantiated prompt is
self-contained bytes — governing docs and bundle inlined, no repo paths to
follow. This is what makes a cold agent runnable, makes Claude and gpt-5.6
comparable, and closes friction #4 (the S1 run reached outside the bundle because
it could).

```
_commentary/
  ORCHESTRATION.md            run contract, all three layers
  prompts/ayah.md  pericope.md  surah.md
  inputs/s{NNN}/              instantiated prompts, one file per unit
  outputs/s{NNN}/             prose, evidence, friction, manifest
```

**D-f. S100 is the test surah, not S1.** See *Contamination* below.

**D-g. Do not generate the remaining 84 whole-surah readings.** Coverage is S1 +
S87–S114 — all four pilot surahs included. The missing 84 are S2–S86, every one
long, and none is a candidate until layers 2/3 are validated. Revisit when a long
surah is chosen.

---

## Source inventory — verified in quran-data 2026-07-27

| source | path under `quran-data/data/` | count |
| --- | --- | ---: |
| Quran text | `text/quran-uthmani.tsv` | 6,348 |
| word analysis | `analysis/word-analysis/` | 6,236 |
| QAC morphology | `morphology/qac.sqlite.gz` | 128,219 |
| branch inventories | `analysis/ayah-activation/v12-tr/s{NNN}/full_context_packet.json` | 114 |
| reader walks | `.../v12-tr/s{NNN}/full_context_control/*ayah_walk.md` | 118 |
| whole-surah readings | `.../v12-tr/s{NNN}/full_context_control/*butuncul-okuma.md` | 30 |
| focus runs | `.../v12-tr/s{NNN}/focus_{S}_{A}/` | 6 dirs, **4 with responses** |
| channel reviews | `analysis/channels/network-v3/s{NNN}/review/reader_a_pilot.md` | 110 |
| channel candidates | `analysis/channels/network-v3/s{NNN}/` | 112 |
| pericopes | `analysis/channels/network-v3/pericopes/surah_pericopes.jsonl` | 351 rows |
| inter-ayah | `analysis/inter-ayah/focus_{S}_{A}_cutoff_100.tsv` | 5,604 |
| Turkish dictionary | `dictionary/tr/root_*.json` | 1,680 |
| Turkish glosses | `translation/glosses/locales/tr/root_*.json` | — |

`pilot_invalid_prompt_leak/` was correctly excluded from the migration.

**Not migrated, deliberately:** `latent_activation/v12/runs_11ayah/` and
`v11/run/` are different run families, not consumed by the builder.

**Known-partial, pre-existing:** whole-surah readings 30/114; channel reviews
110/114 (S108, S110, S113, S114 never generated — all 3-ayah surahs); focus runs
4 ayahs of 6,236 (100:1, 103:1, 112:1, 113:1 — 103:2 and 103:3 have packets but
zero responses).

---

## Contamination — why S1 cannot be the eval surah

The 1:6 baseline is good prose, but it cannot prove the pipeline works, because
the governing docs a writer is ordered to read contain worked answers for that
exact ayah:

| `docs/CHANNELS.md:48` | "takes its traveler into itself" — the `sırât` finding |
| `docs/CHANNELS.md:216` | "swallowing `ص ر ط:B002`" — finding *and* branch id |
| `docs/CHANNELS.md:132` | the same finding in **Turkish**, ready-made, for 1:6–1:7 |
| `_ayah_commentary/PROMPT.md:33` | asserts the doubled article "is doing work" |

Provably data-derived in that run: the ه د ي carrying-field with `hediye`/27:35,
and the ق و م loanword family (`kıyamet, makam, kıymet, mukavemet, Kayyûm`) with
its failure states. Neither appears anywhere in the docs.

S100 leaks only five lines, and they say the horses are unattached and a channel
attaches them — where to look, not what to find. They do not provide the local
secondary turn layer 2 must derive, but they are **a real thumb on the scale for
layer 3**, which matters if models are compared there.

The worked examples are arguably legitimate few-shot teaching of register. Keep
them; just never evaluate on S1.

---

## Baseline artifact

`bundles/s001/1_6.layer2-baseline.{prose,evidence,friction}.md` — the first and
only output ever produced under `COMMENTARY_SPEC.md`. 1,516 words of Turkish for
a three-word ayah, plus a 16-item friction report from the writer.

**Its verdict: the prompts are not production-ready.** The prose quality is high;
the problem is size and shape.

Open friction items, by kind:

- **Scope, unresolved (#1, #2, #3)** — "activated reading" is undefined and the
  candidate set ranges 9 to ~60; `PRINCIPLES.md` §9's never-filter rule is
  impossible against 143 inter-ayah rows; no length is specified anywhere. These
  are one problem: nothing says how much goes in.
- **Fixed already** — the maturity circularity and the channels-invisible bug
  (bug 1 and bug 2, all seven sites).
- **Needs an artifact** — loanword claims have no evidence channel (D5 join);
  `consideredNotPrimary` missing; cited ayah text absent from the bundle while §9
  requires the counter-evidence rendered.
- **Small** — evidence-surface language and format, `mNN` identity, the dead
  layer-3-exclusions bullet, header ambiguity.

**Proposed and not yet decided:** the ayah reading carries what the words do
*together*; the root field attaches to the **word**, not the ayah. In the 1:6
baseline that is a ~500 / ~900 word split. This would resolve #1–#3 at once and
follows the app's own three-layer design ("when I want to check an individual
word"). Awaiting the user's call.

---

# Actions

## 1. Rewrite `build_bundle.py` as quran-data-only — **in progress**

- collapse three source roots to `quran-data/data/`
- **preflight**: enumerate every expected source for the surah and abort with the
  *complete* gap list, not the first failure
- add pericopes: spans in the surah bundle; each ayah bundle learns its pericope
- wire `dictionary/tr` + `translation/glosses` — this is the D5 join and it gives
  friction #10 its evidence channel
- rebuild S1 and **diff against the existing `bundles/s001/`** to prove the
  repoint changed nothing

### Measured 2026-07-27 — layer 3 cannot run without pericopes

`scripts/instantiate.py` exists and is verified deterministic. Assembled
self-contained prompt sizes for S100:

| unit | tokens |
| --- | ---: |
| `100_1.ayah` | 58k |
| `100_2` … `100_11.ayah` | 85k–100k each |
| `100.surah` | **907k** |

The surah number is real, not a bug. `{surah}.surah.json` *references* its ayah
bundles rather than duplicating them, so a self-contained layer-3 prompt must
inline all of them. **11 ayahs already exceed any context window.** D-c's pericope
rationale is now empirically confirmed rather than projected: layer 3 is
unrunnable on anything but the shortest surahs until the pericope layer exists.

Layer 2 per-ayah prompts are large but workable.

### Superseded 2026-07-28 — the input contract was wrong, not the layer count

The 907k figure measured the wrong input. D-c and this repo's own stage table
both say layer 3 consumes layer 2's **outputs**; the instantiator was inlining
raw ayah bundles, and `_surah_commentary/PROMPT.md` agreed with the code rather
than with the plan. `instantiate.py --layer surah` now reads the surah-scope
bundle plus every layer-2 `prose`, `evidence`, and `index`:

| surah | ayahs | layer-3 prompt | raw-bundle prompt |
| --- | ---: | ---: | ---: |
| S103 | 3 | 189 KB | 1.8 MB |
| S1 | 7 | 379 KB | — |
| S100 | 11 | 503 KB | 5.6 MB (907k tokens) |

**Layer 3 is no longer blocked, and it was never blocked on the pericope layer.**
All three surahs with layer 2 complete are single-pericope — S100 has zero rows
in `surah_pericopes.jsonl` — so a pericope agent for any of them would cover the
whole surah and duplicate layer 3. Stage 4 is a long-surah requirement: at ~140 KB
of layer-2 output per 11 ayahs, S2's 286 would be ~3.6 MB.

Superseded again 2026-07-28: the compact reviewed-channel lane now combines
Layer 3 and Layer 2.5. Exclusions are checked against Layer 2's already-preserved
prose rather than triggering a thesis-aware rerun. Grounding and maturity are
designed with the whole-surah prose, while the cold ayah pass stays isolated.

**Accepted scope note:** `COMMENTARY_SPEC.md` references `docs/SOURCES.md`, which
is deliberately *not* inlined — it documents how the bundle was built, not how to
write from it, and its content is already resolved into the bundle. The dangling
filename reference is left for the friction report to surface if it disorients a
writer.

## 2. Write `_commentary/ORCHESTRATION.md` — **done 2026-07-27**

Per D-d and D-e. Covers all layers in one file: directory contract, task
variables, five stages, output contract, batch order, cross-model runs,
decisions, completion-state limitation. Records State B, the two unsatisfiable
exclusion instructions, and the three open friction items.

## 3. Write `scripts/instantiate.py`

Bundle + governing docs → one self-contained prompt file per unit, into
`_commentary/inputs/s{NNN}/`. Model-agnostic.

## 4. Add the optional pericope compression pass to the principles

Reserve `2P` for the pre-Layer-3 long-surah compression pass. Layer 2.5 is the
post-Layer-3 channel-integration pass and must not be used for pericope naming.

## 5. Run layer 2 on S100 — one agent per ayah, 11 agents

One agent per ayah is not a preference: an agent holding the whole surah writes
ayah readings that are slices of it (`COMMENTARY_SPEC.md` §4), and cannot write
100:1 as if it had not read 100:11.

## 6. Read the output — the gate

Does the word-function job fix the loanword problem? Is the reader ever unsure
what the ayah says? Do readings explain each other or sit next to each other?

## 7. Resolve scope from evidence

Decide #1–#3 with two real outputs in hand rather than by prediction.

## 8. Combined Layer 3 + Layer 2.5 — **implemented 2026-07-28**

The reviewed network channel source already establishes systems and branch
identities. A compact compiler joins them to exact QAC/root anchors. One
combined pass reads that bundle plus Layer-2 prose, writes the primary-grounded
surah argument and completed surprising channel reading, derives maturity in
reading order, and emits ayah overlays. The cold Layer-2 prose is never
overwritten.

Contracts and checks:

- `schemas/surah-channel-plan-v1.schema.json`
- `schemas/ayah-channel-overlays-v1.schema.json`
- `scripts/build_channel_bundle.py`
- `scripts/instantiate_channel.py`
- `scripts/check_channel_plan.py`
- `scripts/check_channel_overlays.py`

## 9. Layer 1 — D5 gloss join, then D1 assemble inversion — **D1/D2/D3/D4 done 2026-07-27**

D1 (assemble inversion), D2 (provenance), D3 (`languagePolicy`), and D4
(`consideredNotPrimary`) are implemented, plus a new stage 0 that seeds anchors
with a cold agent instead of by hand — `_translation/v1/README.md` and
`orchestrator.md`. What remains here is D5 and the re-seeding of S1 and S103,
which is what actually pulls `consideredNotPrimary` forward.

`error.fit == "narrowing" && error.loses_facet_ids != []` → "least-disorienting
gloss is materially incomplete; check the others". Derived, not authored. Pull
`consideredNotPrimary` forward: every day it is missing, layer 1 destroys the
rejections layers 2 and 3 depend on, and `عَٰلَمِينَ` B002 is the entire path
channel.

## 10. Decide the focus protocol, then scale

4 ayahs of staged before/after exist corpus-wide. Settle empirically before
committing to anything at scale.

---

## Frozen — do not touch

**Bundle sources beyond what is listed.** Adding speculatively is how the docs got
braided.
**network/v3 discovery.** Complete; re-running cannot produce a ledger.
**inter-ayah.** 5,604 outputs, 88 surahs — the most complete upstream workflow.
Every planned surah is covered. It needs nothing but protection from filtering
(`PRINCIPLES.md` §9).
