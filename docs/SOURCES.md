# Sources

Paths, formats, and verified gotchas for every upstream source read by this
repository. Shared contract for `_translation/v1/tools/build_bundle.py` (layer
1), `scripts/build_bundle.py` (full commentary base bundles), and
`scripts/tier_branch_payloads.py` (the required pre-Layer-2 projection).

All paths are relative to the sibling-repo root `/Volumes/OZTURK/_projects`.

Verified against S103 and S1 on 2026-07-27. For *how much* of each source exists,
see [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md).

---

## 1. Canonical data (`quran-data`)

| source | path | format notes |
| --- | --- | --- |
| Quran text | `quran-data/data/text/quran-uthmani.tsv` | **pipe-delimited, not tab.** `S:A\|text`. Includes `S:0` prefatory basmalah rows. |
| word analysis | `quran-data/data/analysis/word-analysis/s{NNN}.jsonl.zst` | zstd JSONL, one record per ayah, `schema_version: word-analysis-output-v2`. Each record has `words[]` with `aligned_qac_word_ref`, `root_display`, `gloss_range`, `prose`, `topics[]`. Topic `status` is `used` or `narrowed`; `narrowed` is the non-disambiguating marker. |
| QAC morphology | `quran-data/data/morphology/qac.sqlite.gz` | gzip'd sqlite. Table `qac_morphemes`; cols include `qac_ref`, `qac_word_ref`, `surah`, `ayah`, `word_index`, `morpheme_index`, `root_join_key`, `root_ar`, `pos`, `morph_features`. Empty `root_join_key` means no root. |
| Furuq / V4 lexicon | `quran-data/data/lexicon/furuq.sqlite.zst`, `v4.sqlite.gz` | Both are `lexicon-build` sqlite with identical tables (`roots`, `branch_images`, `dictionary_entries`, `lexical_unit_senses`). **Furuq is the successor and superset**: v4 (2026-06-30, 1,700 roots) was imported into furuq (2026-07-07, 3,470 roots). Use furuq. |
| QAC↔V4 form bridge | `quran-data/data/bridges/qac-v4.sqlite.gz` | Form-level table `qac_v4_form_bridge`: morpheme ref → V4 form handle, with `match_status` (unique/ambiguous/unmatched/no_v4_forms), `confidence`, `downstream_usable`. Do not use this for root identity. |
| QAC↔Furuq root bridge | `quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz` | Root-level bridge used by `scripts/build_bundle.py` and `../latent_activation/focus_trace`. Views include `qac_to_furuq`; split QAC roots map to multiple Furuq `root_id` values, all of which must be preserved. |
| grammar attachments | `quran-data/data/grammar/attachments/attachments.tsv` | **ayah-keyed and joinable**: `sura`, `ayah`, `relation`, `status`, `confidence`. 11 rows for S103. Records syntactic dependencies — e.g. `وَ` as oath particle governing `العصر` at `status=syntactically_forced`. |
| grammar contextual | `quran-data/data/grammar/contextual/*_v2.tsv` | **root/form-keyed aggregate statistics** (narration ratio, imperative ratio, …), *not* ayah-scoped. **Do not join by ayah.** |

## 2. Activation Artifacts

Stable v12 activation artifacts are read from frozen `quran-data` copies. New
Hermetic Focus Trace outputs are generated in the sibling `latent_activation`
checkout and are consumed by default by this repo.

| source | path | format notes |
| --- | --- | --- |
| v12 surah packet | `quran-data/data/analysis/ayah-activation/v12-tr/s{NNN}/full_context_packet.json` | **Exists for all 114 surahs.** Carries `branch_inventories` plus `missing_branch_inventories`. Scope is the whole surah's roots, unstaged. This is the required branch source for the current default lane. |
| retired v12 input packets | `quran-data/data/analysis/ayah-activation/v12-tr/s{NNN}/focus_{S}_{A}/stage_{NN}_*.json` | Same `branch_inventories` structure, but scoped to the focus ayah's own roots at stage 0 and staged by reveal order. **Exists for 6 ayahs corpus-wide** — see §5. |
| retired v12 reader responses | `quran-data/data/analysis/ayah-activation/v12-tr/s{NNN}/focus_{S}_{A}/responses/reader_{x}/stage_{NN}.json` | **Retired from the default lane and usually absent.** Each has `models[]` with `model_id`, `status`, `confidence`, `mechanism`, `activation_trace[]`, `structural_cues[]`, `abductive_moves[]`, `changed_reading{before,after}`, `minimal_triggers[]`, `ablation`. |
| Hermetic Focus Trace | `latent_activation/focus_trace/runs/s{NNN}/packets/{S}_{A}.packet.json` or `runs/s{N}/packets/{S}_{A}.packet.json`; matching `readers/{reader_id}/{S}_{A}.focus_trace.json` | New one-call reconstructed focus workflow. Packets are generated upstream in `latent_activation`, not `quran-data`. The builder accepts either padded (`s012`) or unpadded (`s12`) run directories and fails if both contain active data for the same target. Responses enter bundles under `v12_focus_trace_hermetic` with `baseline_models`, `context_deltas`, and `surprising_valid_outliers`. Packets use `qac-furuq-v4-root-map.sqlite.gz`; split roots preserve `mapped_root_id` with `branch_id`. |
| v12 reader walks | `quran-data/data/analysis/ayah-activation/v12-tr/s{NNN}/full_context_control/reader_s{NNN}_{a,b}_ayah_walk.md` | Markdown. Per ayah: numbered *Activated readings* with lexical evidence and `Reading change:`, then *Retrospective surprises*. **Highest-value whole-surah reader source; do not skip.** |
| v12 plus/minus-5 reader walks | `quran-data/data/analysis/ayah-activation/v12-tr-11ayah/s{NNN}/full_context_control/reader_s{NNN}_{a,b}_ayah_walk.md` | Markdown in the same ayah-walk shape, generated with wider local context. Bundled separately as `v12_reader_walks_wide`. |
| v12 cross-run publication | `quran-data/data/analysis/ayah-activation/v12-cross-run/tr/{S}_ayah_findings_publication.json` | Compact reconciled findings derived from regular and plus/minus-5 reader walks. Use as coverage/priority check, not prose to copy. |
| whole-surah reading | `quran-data/data/analysis/ayah-activation/v12-tr/s{NNN}/full_context_control/{NNN}-0-{N}-butuncul-okuma.md` | Turkish. Per-ayah primary reading plus context expansion, with branch citations. |

## 3. Channels (`latent_activation/network/v3`)

| source | path | format notes |
| --- | --- | --- |
| channel candidates | `latent_activation/network/v3/experiments/corpus_neo_adaptive/s{NNN}/` | Deterministic discovery from the surah-local SLM graph. Complete for 111 eligible surahs (2026-07-23): 89,199 dense candidates, 11,572 families, 4,157,715 sparse paths, 457,281 path families. Stage summaries: `summary.json`, `families/consolidation_summary.json`, `paths/path_summary.json`, `paths/path_families/path_family_summary.json`. |
| channel review | `latent_activation/network/v3/reviews/s{NNN}/reader_a_pilot.md` | Markdown. Parent channels → subchannels, each with `Semantic invariant`, `Surface relation`, `Surprising reach`, `Reading type`, `Scene or process`, `Active motifs`, `Ayah anchors`, `Synthesis`. **110 surahs; missing for S108, S110, S113, S114.** |

Motifs are cited as `root:branch/mNN` — e.g. `ع ب د:B005/m01`, "paved or trodden
road". Note the `mNN` suffix: this is a **morpheme-sense** level finer than
`branchId`, and it is not one of the identities in `PRINCIPLES.md` §11. Nothing
downstream can join on it yet.

`Reading type` ∈ {`surface-primary`, `mixed`, `latent/lexical`} is effectively
the depth model under another name. Build-time only; it must never surface.

**This is first-pass, single-reader review, not an adjudicated ledger.**
`REVIEW_ORCHESTRATION.md` describes itself as a prototype and specifies a
staged order (pilot S001 → calibrate on S100/S112/S113/S114 → medium batch);
what exists is the first pass everywhere. There is no accept/reject, no second
reader, and no per-ayah maturity. Working ledgers are explicitly kept internal,
so the markdown report is the only durable artifact. Consequences for what may
be rendered: `CHANNELS.md` §5.

Governing docs: `network/v3/README.md`, `ORCHESTRATION.md`,
`REVIEW_ORCHESTRATION.md`, prompt at `network/v3/prompts/blind_candidate_review.md`.

## 4. Relations (`quran-slm`)

| source | path | format notes |
| --- | --- | --- |
| inter-ayah | `quran-slm/inter-ayah/outputs/focus_{S}_{A}_cutoff_100.tsv` | **Headerless**, 3 tab-separated columns: `label`, `ayahRef`, `note`. Label ∈ {`strong`, `medium`, `weak`, `no value`}. Governed by `quran-slm/inter-ayah/ORCHESTRATION_SPEC.md`. |

The label axis measures marginal contribution, not reality. **Order with it;
never filter with it** — see `PRINCIPLES.md` §9.

## 5. Target-language lexical evidence (`dictionary`)

| source | path | format notes |
| --- | --- | --- |
| gloss results | `dictionary/v2/gloss_generation/results/{language}/` | Branch-concept, contextual, and lexical glosses, plus facet coverage, semantic error classification, losses, additions, collisions, and review provenance. See `dictionary/v2/gloss_generation/README.md`. |

These are controlled lexical projections, not fluent translations. Their review
status does not override the draft status of their source entries.

This is the source of the **error profiles** that join to the layer-1 spine by
`(rootId, branchId, language)`. They are deliberately not embedded in the spine
— see `_translation/v1/README.md`.

---

## 6. Verified gotchas

**Focus directory naming.** `focus_{S}_{A}` is surah-then-ayah. `focus_103_1` is
103:1; `focus_1_103` is 1:103. Both exist in the same directory.

**Reveal-order variants.** A v12 focus dir may contain `left_first/` and
`right_first/` subdirectories. Both are valid; keep both, keyed separately. A
flat focus dir is keyed `default`.

**Quarantine.** `pilot_invalid_prompt_leak/` directories are excluded from
bundles unconditionally, wherever they appear.

**Focus runs are a pilot, not a corpus.** Six focus dirs exist in the whole
corpus, and the reader IDs show successive protocol revisions rather than a
production sweep (`a/b/c` quarantined, then `d/e/f`, `j`, `k`, `l`):

| run | stages | responses | readers |
| --- | ---: | ---: | --- |
| `s103/focus_103_1` | 3 | 9 | d, e, f |
| `s100/focus_100_1` | 11 | 6 | l |
| `s112/focus_112_1` | 4 | 4 | j |
| `s113/focus_113_1` | 5 | 5 | k |
| `s103/focus_103_2`, `_3` | in variant subdirs | 0 | — |

So the staged before/after trajectory — `stage_00` in isolation through
`changed_reading{before,after}` as neighbours reveal — exists for **five ayahs**.
Absence is the rule; treat its presence as a bonus, not a section every ayah
commentary is expected to have.

**Branch inventories are scoped from surah packets.** Retired focus runs are no
longer the production branch lane. `scripts/build_bundle.py` reads the frozen
`full_context_packet.json`, scopes it to this ayah's roots and anchored channel
citations, and records `coverage.branch_inventories.scope = "surah_fallback"`.
There is no staged reveal order in that inventory.

**Hermetic Focus Trace is required generated evidence by default.** A
focus-trace packet can exist before any model response. In that state the bundle
records `coverage.v12_focus_trace_hermetic.packet_present: true` and
`present: false`; because HFT is required unless `--exclude-focus-trace` is
passed, preflight aborts until reader JSON exists and validates.

It is required by default at the base-build layer and by the production
`tier_branch_payloads.py` contract. A no-HFT base bundle is allowed only when
`build_bundle.py --exclude-focus-trace` is passed for coverage review or a
controlled ablation; it is not accepted as a new canonical Layer-2 tiered
bundle.

For focused production refreshes, keep the strict sequence:
`build_bundle.py`,
`tier_branch_payloads.py --compact-output`, and
`instantiate.py --require-focus-trace`. This gives three failure points for the
same class of regression: source build, Layer-2 projection, and prompt
instantiation. Missing or unusable HFT must fail rather than degrade quietly
unless `--exclude-focus-trace` records the intentional omission in coverage.

**Focus Trace run directories may be padded or unpadded.** Production tooling
checks both `latent_activation/focus_trace/runs/s{NNN}` and `runs/s{N}` for the
requested surah. Keep only one active source directory for a target; if both
forms contain usable HFT for the same ayah, the builder fails so prompt
provenance stays explicit.

**Whole-surah reading filenames are inconsistently zero-padded.** S103 is
`103-0-3-butuncul-okuma.md` but S1 is `1-0-7-...` and S87–S99 are unpadded too.
Of the 30 files that exist, 15 are unpadded. Glob both forms — matching only
`{surah:03d}` silently drops half of them, including S1 and S96.

**Reader B has no synthesis section.** Reader A's ayah-walk file has a
`# Turkish Prose Synthesis` section; reader B's does not.
`turkish_prose_synthesis_md: null` for reader B is correct, not an error.

**Bare finding refs in inter-ayah notes.** Notes sometimes reference v12 findings
as bare `f01`/`f02` strings inside prose — 13 of 468 S103 rows. Extract by regex
and mark unreliable; this join should eventually be promoted to a column.

**Branch IDs are per-root.** `ع ص ر` runs B001–B015 accepted. `B002` is
meaningless without its root.

**Packets carry accepted branches only.** A v12 packet's `branch_inventories` is
exactly furuq's `branch_images` filtered to `status='accepted'`. `ع ص ر` has 16
branch rows; B001–B015 are accepted and appear, B016 is `status='review'` and
does not. Sourcing branches from packets is therefore equivalent to sourcing from
the lexicon of record — **for accepted branches only.** Review-status branches
are invisible to every current consumer.

---

## 7. Bundles must report coverage

Every bundle carries a coverage block naming what is present and what is missing,
per source, per ayah. A missing v12 response set is a first-class fact the writer
must be able to state (`PRINCIPLES.md` §7).

**Fail loud on required sources.** Quran text, the word-analysis record, QAC
morphemes, and branch inventories are structurally expected for every canonical
numbered ayah; their absence aborts the base build. The pre-Layer-2 tierer also
requires a consistent coverage block, HFT reader payload, and well-formed branch
identities/citations; it aborts rather than treating a missing field as empty.

**Degrade gracefully on optional sources.** Retired v12 reader responses,
reader-walk entries, the whole-surah reading line, cross-run publication rows,
channel review/output manifests, pericopes, and inter-ayah TSVs are recorded as
`present: false` with a note; the run continues. Hermetic Focus Trace does this
only during explicit `--exclude-focus-trace` ablations; otherwise missing or
unusable HFT aborts preflight.

---

## 8. Furuq projection in Layer 2

The full Furuq/V4 sqlite and QAC↔V4 form bridge are not copied wholesale. The
base ayah bundle uses the root bridge to inline Turkish dictionary/gloss entries
for every mapped dominant and non-dominant Furuq target. It keeps every branch
in those entries and records the complete target mapping in coverage.

`scripts/tier_branch_payloads.py` then projects only the dictionary/gloss branch
records for Layer 2. Explicitly cited branches remain full except for
`what_is_not_ar` and `identity_judgment.boundary_note`; uncited B001/B002 branches
receive the rich-lite safety payload; all others receive the compact payload.
No root or dictionary branch identity is filtered. Branch inventories and all
non-branch evidence are copied unchanged. The exact tier counts, interest-source
coverage, resolution gaps, and trim contract are recorded under
`coverage.root_lexicon.branch_policy`.

Malformed citations and unresolved citations whose Arabic root exists in the
bundle's root lexicon or branch inventory are hard errors. A valid Arabic
citation to a contextual root absent from both resolution surfaces cannot be
promoted; it remains explicit under
`resolution.unresolved_out_of_scope_arabic_citations` rather than disappearing
silently.

Grammar attachments remain folded into word-analysis `prose`/`topics[]` through
`evidence_checked` tags and are unaffected by branch tiering.
