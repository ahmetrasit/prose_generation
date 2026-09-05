**V5 fix review — 2026-09-04**

Reviewed `45332231` against `7f1ac73c`. The fixes are partly complete. There is
a reproducible reference-extraction bug in the new code, a weakened semantic
instruction, and several incomplete evidence repairs. No implementation,
bundle, prompt, or generated commentary was edited during this review.

The findings below come from tracing the changed code, generating fresh packets
from real inputs, inspecting their evidence, and constructing additional edge
cases. Existing test results are not the basis for the conclusions. Current
preparation was exercised for native 29:38; split, external-overlay, Fatiha, and
comma-list compositions; 29:0; 1:1; 87:1; 100:1; 24:31; 24:61; 48:29; 73:20;
and 14:22. Output destinations were redirected to temporary review directories.
Historical preparation code and prompts were also loaded separately for a
before/after size comparison. No new semantic agents were launched.

1. **High priority — the new reference extractor loses real source references.**

   [`_extract_quran_refs`](../../_commentary/v5/workflow.py), starting at line
   315, handles a simple same-surah range but does not carry the surah over a
   comma-separated list. This is a source format already present in the 29:38
   channel supports, not merely a hypothetical input.

   For `A:Mark, Landmark, and Inward Sight`, the actual occurrence support says:

   ```text
   ء ي ي 29:35,44; ع ل م 29:28,32,41-43;
   ب ي ن 29:35,38-39; ب ص ر 29:38; ت ر ك 29:35.
   ```

   The resulting candidate lists only `29:28` and `29:35` as required context.
   It omits `29:32`, `29:39`, and `29:41–44`. A fresh preparation with
   `--analysis-id review-comma --segment host=29:28,29:35,29:38 --ayah 29:38`
   puts this candidate in **macro**, although the omitted references require
   **global** under the composition contract. The packet nevertheless declares
   `candidate_context_refs_are_exact: true`, and the policy tells the agent that
   this list is authoritative.

   `A:Fitted Dwelling Structure` also loses `29:34–36` from expressions such as
   `29:31,34` and `29:28-30,35-36`. A separate parser probe gives
   `29:41-29:43 -> [29:41, 29:43]`, silently omitting the interior ayah.

   Parse the reference grammar used by the source formats, including inherited
   surah numbers and repeated-surah range endpoints. Do not certify an incomplete
   extraction as exact. This is a defect in the newly restored normalization.

2. **High priority — the two bundle repairs fix schema compatibility but leave
   almost all word-to-morpheme links stale.**

   The commit adds `morpheme_skip_count: 0` to the existing non-null spans in
   [14:22](../../bundles/s014/14_22.ayah.json) and
   [73:20](../../bundles/s073/73_20.ayah.json). Both now prepare successfully.
   However, their saved crosswalks still resolve only:

   | Focus | Saved resolved analysis words | Current resolver, same local sources |
   | --- | ---: | ---: |
   | 14:22 | 4 / 56 | 56 / 56 |
   | 73:20 | 7 / 95 | 95 / 95 |

   I called `load_morphemes_tsv` and `resolve_word_morpheme_spans` from the
   [current builder](../../scripts/build_bundle.py) using each saved bundle's
   word analysis. All previously resolved rows remained identical; all remaining
   rows acquired spans. The regenerated spans also passed the preparation
   module's QAC lineage validation in memory, with zero unresolved words.

   This affects actual agent inputs: 14:22's `قُضِيَ` analysis row, for example,
   still has `qac_refs: []` in every freshly prepared lane, although the current
   resolver supplies `14:22:4:1`. The bundle coverage still reports 52 and 88
   unresolved words respectively. Regenerate the crosswalks and associated
   coverage from the current builder rather than only adding the required field.
   This is an incomplete repair of existing stale data.

3. **High priority — routing a candidate does not assemble all evidence that
   the new required-context list names.**

   The new routing pass moves candidates and their existing supports but does
   not load newly discovered context evidence. In fresh native 29:38 global
   evidence, `29:38:23:inverse-rare-echo` now correctly requires `7:201`, but
   that ayah has no exact Arabic context record or typed occurrence projection.
   The agent receives an English assertion about the inverse encounter with
   shaytan and insight. It cannot independently check that target from the
   supplied packet, and the discovery prompt prohibits consulting other files.

   Other required references without an exact Arabic context record in this
   packet are `15:84`, `27:46–50`, `27:53`, `29:48`, and `29:62`. The first
   groups arise from the Thamud word-topic ranges; the latter two arise from
   `delta_nonbinding_knowledge`. Existing target records generally remain
   Arabic-only even where a local bundle could supply typed morphology.

   After normalization, assemble available context evidence for the required
   refs and explicitly distinguish unavailable evidence from a rejected reading.
   The routing improvement is real, but this part of the previous evidence
   preparation finding remains open.

4. **Medium priority — semantic obligations cover only part of the actual
   candidate schemas.**

   The new obligation builder is useful for ordinary word topics and the HFT
   format used in most 29:38 records. Its field allowlists at workflow lines
   527–535 and 587–605 do not cover all supplied semantic payloads.

   In a fresh 100:1 macro packet, HFT candidate
   `reader_hft_a:O01_REDRESS_RUN` has four activation-trace obligations and one
   changed-reading obligation. Its `rendering_caution`, `why_still_valid`, and
   `why_surprising` fields have no obligations. The caution specifically says
   that the packet does not resolve the raiding form or the focus participle to
   a beneficent referent. That is consequential containment for this surprise
   reading, not expendable metadata. Other real 100:1 records also use
   `abductive_moves`, `ablation`, and `minimal_triggers`, which this builder
   does not enumerate.

   Likewise, the 29:38 `cross_run_publication` candidate `finding-1` has
   `semantic_obligations: []`: its serialized support stores the claim under
   `text`, which the decoded-object allowlist omits. This focus-local candidate
   also remains global with no required context, because the empty-reference
   routing correction only recognizes the two reader-walk source types.

   The original source fields remain visible; this is not physical deletion of
   their text. The failure is that explicit retention/exclusion accounting does
   not cover them despite the prompt's completeness claim. Use source-specific
   semantic field mappings, including substantive cautions and inference steps,
   while excluding ordinary provenance metadata.

5. **Medium priority — shortening the policy removed the explicit containment
   guarantee.**

   The old embedded [principles](../../_commentary/work/layer_3_channel_commentary/PRINCIPLES.md)
   require each latent reading to contain the ordinary reading intact, with the
   ordinary reading recoverable throughout the prose. The new authoritative
   [discovery policy](../../_commentary/v5/prompts/discovery-policy.md) says to
   make the ordinary sense clear first, then explain the developments. The
   discovery schema describes `containment` as limits and uncertainty. Neither
   is the same non-replacement requirement, and the fresh consolidator no longer
   receives the principles or the compact discovery policy.

   This is an instruction regression, not a demonstrated error in a newly
   generated commentary. Restore one concise rule in the operative discovery
   and writing contracts: every resonance must preserve the ordinary reading
   intact and keep it recoverable where the resonance is explained. The longer
   historical documents need not return.

6. **Medium priority — instruction bloat decreased, but total prompt payload
   did not.**

   Removing four governing documents and putting top-level list records on
   separate lines are useful improvements. However, a controlled comparison
   using 29:38, host segment 29:38–41, and external Fatiha 1:2–7 gives these
   approximate UTF-8 sizes; minor path-length differences are immaterial:

   | Lane | Before | After |
   | --- | ---: | ---: |
   | Micro | 848 KB | 864 KB |
   | Macro | 901 KB | 811 KB |
   | Global | 1,368 KB | 1,554 KB |
   | Total | 3,117 KB | 3,229 KB |

   The new obligation and routing records offset the removed instructions, and
   routing imports additional branch records into global. The full repeated
   atlas and internal duplication remain. Fresh 73:20 global preparation reaches
   approximately **4.84 MB**. Record-line serialization makes partial reads more
   manageable but does not establish that the agent inspected every required
   record. No model-token or complete-reading check has been demonstrated.

   Compact repeated evidence while retaining every distinct lexical restriction,
   unusual facet, and counterexample. The appropriate next reduction is in
   duplicated evidence and instructions, not a cap that silently drops branches.

7. **Lower priority — rerouting leaves contradictory HFT and scope metadata.**

   For the 29:38–41 plus Fatiha composition, fresh macro has two assigned HFT
   records but `scope.hft.assigned_record_count` still says three. Global has
   eighteen but its scope count says seventeen. The HFT record
   `delta_false_stability_architecture` moves to global while its `owning_lane`
   remains macro. `lane_counts` remains the old distribution, and moved
   connections retain native `relation_scope` labels.

   The new routing fields are explicitly authoritative, which limits the
   damage, but the packet still gives agents conflicting current-scope signals.
   Recompute derived counts and ownership or clearly label the retained values
   as upstream provenance. The relevant partial update is at workflow lines
   1689–1697.

Several changes do work on the independently inspected real data. The 29:39
auxiliary-participle echo reaches macro in native 29:38. The two focus-local
reader activations reach micro; the 29:41–43 retrospective reaches macro; and
the 29:61 retrospective stays global. The split-segment 29:41 connection moves
to global, while external 44:32 moves into macro. Across the four principal
29:38 compositions, all 92 candidates and 269 connections remain present in
aggregate. Word-analysis root options are populated. Real 87:1 ambiguous branch
expansions are explicitly marked as alternatives rather than cumulatively
established identities.

The new policy also explicitly requires preservation of the lexical explanation
behind an unusual image and distinguishes accusative case from objecthood.
Consolidation now receives discovery records and permits supported factual
corrections. The monitor's former artifact-only validation inference is removed:
an editorial file without a completion event no longer certifies validation.
The bounded stop and nonblocking pause changes are coherent on inspection;
live Firebase shutdown was not exercised in this review.

These prompt changes have not established a corrected 29:38 output. The saved
[editorial](../../_commentary/v5/editorial/s029-38-41-with-fatiha/s029/29_38/29_38.prose.editorial.tr.md)
still contains the previously identified transitive/object description of
`mustabṣirīna` at line 49. No commentary output was changed by the fix commit,
so restoration of the eye-film's lexical explanation also remains unverified
in a fresh semantic run. Code/preparation fixes and demonstrated prose quality
should be tracked separately.

**Implementation follow-up — 2026-09-04, working tree after this review**

The preparation and instruction repairs are now implemented. The earlier
findings above describe commit `45332231`, not the repaired working tree.
Agent outputs remain unchanged: attempted hand edits were reverted, and
`git diff -- _commentary/v5/raw _commentary/v5/editorial` is empty. No fresh
semantic agents were run. Corrected commentary must be produced by agents
working from the repaired inputs and instructions.

- Reference extraction now preserves comma continuations, repeated-surah range
  endpoints, and explicit cross-surah ranges. The real 29:38 channel candidate
  requires `29:28, 29:32, 29:35, 29:39, 29:41, 29:42, 29:43, 29:44`; the
  restricted comma-list composition correctly routes it to global.
- The deterministic word-to-morpheme mappings in the 14:22 and 73:20 source
  bundles were rebuilt with the existing resolver: coverage is **56/56** and
  **95/95**, respectively. Independent comparison with HEAD confirms that all
  previously resolved mappings and every field outside the mappings and their
  coverage record are unchanged. All repaired mappings pass QAC lineage checks.
- Every required context reference receives its available exact Arabic and
  typed morphology from the local QAC corpus, even without a target bundle.
  Real 7:201 now supplies `مُّبْصِرُونَ`, root `ب ص ر`, and its Form IV active
  participle features to 29:38. Missing or corrupt morphology is explicitly
  reported without deleting Arabic or rejecting a semantic possibility.
  Prefatory aliases reuse morphology only after Arabic equivalence is checked.
- Semantic obligations now cover published finding text, HFT rendering
  cautions, validity/surprise explanations, abductive moves, ablation,
  limitations, trigger lists, and list-valued claims. Focus-local published
  findings route to micro. Current HFT ownership/counts and connection scope
  follow routing; original labels are marked as upstream provenance.
- Discovery and writing prompts again require the ordinary reading to remain
  intact and recoverable. Same-root resonances must preserve the attested
  lexical connection and form restrictions. Direct source facts can cite the
  focus, branch, or context registry without inventing a support ID. The
  existing case-versus-syntax rule and agent correction instructions remain in
  force; saved grammatical errors have not been manually corrected.
- Exact repeated packet values now use an inline reference table, with a
  reversible decoder and explicit agent reading instructions. Every distinct
  branch, restriction, candidate, and connection remains available. Reserved
  transport-field collisions fail explicitly rather than overwriting evidence.

Independent preparation checks covered the same **14 real configurations**
listed above, producing **42 lane prompts**. All required context references
in these cases had both Arabic and morphology. Each of the five 29:38
configurations retained all **92 candidates and 269 connections** across its
three lanes; routing, HFT ownership, and counts were checked separately.
All 42 packets survived encoding, JSON serialization, and decoding with exact
structural equality. As secondary checks, the V5 suite passes **79 tests** and
the inherited V3 preparation suite passes **73 tests**. Final loader regressions
also cover corrupt gzip data and focus/self-reference morphology coverage.

The transport reduces serialized packet bytes by **13.6%** across those 42
packets compared with the same fully expanded evidence. This does not mean
total prompts are smaller than the reviewed commit: supplying previously
missing morphology raises the 29:38-plus-Fatiha total from approximately
3.229 MB to **3.415 MB** despite deduplication. The largest tested prompt,
73:20 global, is approximately **6.017 MB**. Bounded reading and deduplication
improve access, but complete agent inspection, model-token fit, preservation
of the eye-film explanation, and the quality of surprise readings remain
unverified until a fresh semantic run is reviewed. These are the remaining
evaluation limits, not evidence that the saved prose has been repaired.
