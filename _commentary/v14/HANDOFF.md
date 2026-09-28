# v14 handoff — 2026-09-27

Read DESIGN.md and INPUT_AUDIT.md. The v13 handoff remains at ../v13/HANDOFF.md. V14 began as an exact copy of all
308 files; baseline.manifest.json records that snapshot. Never edit copied historical out*/ or work/ files.

Production requirement clarified by the user: this pipeline must run blind for any supplied ayah. No ayah-specific
fixes, manually supplied missing connections, or generation rules derived from target evaluation answers. Known
omissions belong in evaluation only. Generic changes must be justified as mechanisms that work from normal inputs.
The 1:6 comparison selects a promising writer; it does not establish readiness for arbitrary ayat.

Latest result: read COMPOSITION_RESULT.md and the unchanged pre-run plan COMPOSITION_TRIAL.md. The user chose
29:38 again and specified Sol 6 max for synthesis, then a fresh Astra 6 max for prose. Both completed once, with
no inherited conversation, target hints, interruption, retry, repair or manual prose edit. The ten evidence files
are byte-identical to the previous arm; no new upstream call was made. Arm: out-sol-astra-composition-29-38.
This is a known-ayah development comparison of the whole redesigned process, not a blind or model-isolation test.

The result is clearer but fails the predeclared goal: 1,374 raw / 1,221 reader words, 15 paragraphs, 18 exact Quran
tags, zero dictionary quotations. The tent-seam / web-like eye-film relationship is already absent from Sol's
819-word explanation and source selection, although the full synthesis input contains it. Astra's selected
packet contains no cue to recover it; Astra makes no extra lookup and does not recover it. Archive retention
and exact-key lookup do not make unknown omissions visible. The primary agent reviewed; no comparison agent ran.
Read independent.review.json and comparison.metrics.json beside the candidate. No acceptance pointer exists.
Under the agreed stopping rule, stop this treatment: no prompt tuning, target-specific restoration or new call
starts automatically. Thirty offline tests passed before generation; code, prompts, inputs and 298 copied
historical data files remain intact. Cost/tokens are unavailable, not a rejection reason. Leave v15 work alone.

Previous result: read BLIND_29_38_RESULT.md and the unchanged pre-run plan BLIND_29_38.md. The user-requested blind
29:38 run is complete: fresh Opus-high discovery and Quran-relation analysis, then one Astra 6 max generation,
with no prompt/code changes, target hints, retry or repair. This is the existing standalone-ayah path: normal
29:21–51 window, no window network and no preceding prose. It does not test sequential or full-surah continuity.

Candidate: out-astra-blind-29-38/s029/29_38/29_38.reading.tr.md. All 140 Arabic tags pass exactly; 6,509 raw /
5,131 gloss words, 60 prose paragraphs and five section headings. The house/seam/eye-film and road/water sequences
develop functional connections, and upstream corrections survive. Serial excursions and explicit omissions remain.
The account fails on two rows sharing an anchor whose final period differs from the prose's colon. F13, Q2, F70
and E_F70 consequently become unreported despite explanations in the prose. No generated output was hand-fixed.
Read independent.review.json, sources.check.json and comparison.metrics.json beside the candidate. No acceptance
pointer exists. All 13 frozen files, unchanged generation code/prompts and 298 copied historical data files verify.
Upstream cost is $4.413; Astra billing/tokens are unavailable and are not a rejection reason. The historical V9 Sol
comparison has different inputs and is not a matched model comparison. No further call starts automatically.

The neutral input catalogue requested by the user is at ../../AVAILABLE_INPUTS.md. Concurrent work, including v15,
must not be staged or restored as part of this run. Earlier comparisons below remain historical evidence.

Previous result: read ARGUMENT_COMPARISON.md. The authorized Sol 6 max / Astra 6 max pair finished in parallel,
one generation each, no interruption/restart/repair. Same 1:6 evidence, v2 upstream, full v2 1:5, revised brief,
lookup capability and schema-3 trace; packets are identical after normalizing the routing tag. Fifteen criteria
were separately frozen and excluded from writer input. Both complete outputs were compared by the primary agent.

Astra is stronger in this pair: Book/fire/resurrection, working well frame and sustained functional development.
Sol improves exact source anchoring but drops those explanations. Both miss the explicit trodden-surface connection
to signs/centre, so neither is accepted. All 110 Sol / 140 Astra tags pass exactly. Prose: 4,055 / 6,442 raw words,
2,920 / 5,119 gloss-substituted; accounting: 15,112 / 16,180 bytes. Tokens/billing are unknown, not a rejection reason.
Read both review.json and supplemental.review.json. Links are locations, never claims of full explanation; omitted
components still hide inside some linked records. Astra also identifies missing rock-branch and variant evidence.

Next proposed evaluation: freeze the current pipeline and test a varied set of previously unused ayat through the
normal input path, with no manual evidence curation or prompt changes between results. Evaluate source correctness,
grounding, supported connections, consequential omissions, continuity and readable development independently.
Component-level omission tracking, prior-reader-state handling and source-reference completeness are hypotheses
for general mechanisms, not instructions to restore particular 1:6 examples. Do not tune again on 1:6 to claim blind
readiness. No additional model run starts automatically. A compact previous-context ablation remains separate.
Twenty-three offline tests passed before the pair; no implementation changed after that test run. All four arms'
frozen inputs and copied historical data remain intact. Concurrent v13 work must not be staged/restored.
The previous completed repeat and its shortcomings are recorded below as history.

Previous result: read STABILIZATION_COMPARISON.md and REVIEW_RESPONSE.md. The agreed out-sol-stable repeat is complete:
same Sol max, v2 upstream and full v2 1:5 context; one generation, no interruption/restart/repair. All 23 tags pass
exactly. Prose: 4,802 raw / 4,605 gloss-substituted words. Accounting: 20,173 bytes (32.1% of response), down 55%.
Initial input: 203,821 bytes; 15 selective lookups added 97,910 bytes. All 147 cited ayat were in returned text.
Tokens and dollars remain unknown; the user explicitly accepts max effort and the cost of this experiment.

Eight preservation and two improvement criteria pass, but acceptance is withheld: the broader review finds the
earlier 18:1–2 upright-Book explanation omitted while E_F1 is still claimed connected. Other source records also
remain only partly explained despite full connected labels. The ten-case gate is narrower than zero regression.
Read both review.json and supplemental.review.json; no accepted.json exists. The repeat restores 20:10 and 17:97.
Next: precise partial-use/deferral accounting and local evidence for lexical claims; keep previous-context reduction
as a separate ablation. Do not start another model run automatically. The user's quoted review is mostly sound for
the first arm but does not establish a Sol model ceiling; see REVIEW_RESPONSE.md.

Twenty offline tests pass. Both frozen Sol inputs and all copied historical data remain unchanged. Concurrent v13
commits advanced the live source and have an active out-v4 arm; do not restore or stage that work. `audit` flags six
changed live source files but no copied historical-data changes. The earlier result below is historical.

User scope: create v14 from v13, revise the synthesis handover and regression protection, audit redundant/missing
inputs, then run one Sol agent at max effort on a chosen ayah and compare with earlier runs. Selected ayah: 1:6.
No unrequested Opus runs. Comparisons are done by the primary agent. The user explicitly authorized this Sol writer.

Implemented: frozen experimental arms; lossless F/E_F/Q/A/image/meeting inventory; corrected adjacent-tag parsing;
role-aware image projection; connected-explanation brief; exact-excerpt accounting and complete handforward;
sequential immediate-predecessor context; independent passage review and immutable acceptance pointer; offline
source verification; measured input audit. Source/tag validation never starts an automatic repair call.

Prepared arm: out-sol-max, v2 activations/network/QeQ, v2 1:5 context. Exact input is
out-sol-max/s001/1_6/write.input.md. Ten regression criteria are frozen in eval/regressions.json and never enter input.
Source packets/prompts/results are checksum-bound; an external call uses a permanent exclusive write.started.json.

Commands (python3 -B avoids modifying copied runtime caches):

    python3 -B -m unittest discover -s _commentary/v14 -p test_v14.py -v
    python3 -B _commentary/v14/run.py audit
    python3 -B _commentary/v14/run.py prepare 1:6,1:7 --tag NEW --seed-from v2
    python3 -B _commentary/v14/run.py preview 1:6 --tag NEW
    python3 -B _commentary/v14/run.py write 1:6,1:7 --tag NEW --execute

The last command spends an Opus call per ayah and requires the user's authorization. For the authorized external
Sol call, export/claim once, generate once, ingest the returned prose plus SYNTHESIS JSON, then review:

    python3 -B _commentary/v14/run.py external-start 1:6 --tag sol-max --model gpt-6-sol --effort max
    python3 -B _commentary/v14/run.py ingest 1:6 --tag sol-max --response RESPONSE_PATH
    python3 -B _commentary/v14/review.py init 1:6 --tag sol-max
    python3 -B _commentary/v14/review.py check 1:6 --tag sol-max

Edit review.json only after independently reading candidate and baseline passages; never hand-fix model prose.
A mixed or regressed result stays experimental. No automatic retry and no average score can hide a lost criterion.

First-trial readiness at its original commit: thirteen offline tests passed; v13 and copied historical data were
unchanged. Input was 201.7 KB versus
151.8 KB in v13; almost all growth is the 49.2 KB preceding commentary. This is not yet a cost improvement.
Surah prose, reciprocal final check, full-surah reader state, common-root/rare-lemma concordance coverage, future
QeQ digest cleanup and API economics remain unbuilt/unresolved. Sol usage dollars are unknown unless reported
by the agent facility. The Sol comparison cannot isolate a prompt effect from a writer-model effect.

Completed: one gpt-6-sol/max generation, no repair. Candidate and raw response are in out-sol-max/s001/1_6.
Read COMPARISON.md and that directory's review.json. Eight preservation criteria survive; water-system local
integration and reader development improve over v2. The candidate is NOT accepted: four Quranic spelling/mark
differences fail source verification. All four match supplied concordance forms, so retrieval/verification must
agree on exact text. Review check exits 1 as intended; no accepted.json was created.

Output: 4,971 raw words; 4,617 after Arabic tags become their Turkish gloss (v2: 7,451 / 5,672). Twenty-seven Arabic
tags: 23 exact, four fixable; no missing/bad-source tags. The account covers all 192 items structurally, but its
180 connected claims are not endorsed as semantic coverage. It uses 51.4% of response bytes: shorten evidence
anchors and narrow claims before another arm. The citation diagnostic now handles source: tags and inclusive
same-surah ranges; only derived diagnostics were recomputed. Input and generated prose remain frozen.

The first trial led to the source and accounting revision in STABILIZATION.md and the completed repeat above.
Compact prior-reader context remains untested. These are targeted revisions, not grounds to discard the
discovery/network pipeline. Neither Sol run exposed usage dollars/tokens.
