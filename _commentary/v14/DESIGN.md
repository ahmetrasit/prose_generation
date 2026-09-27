# v14 design — 2026-09-27

v14 began as a byte-for-byte copy of all 308 v13 files. `baseline.manifest.json` records their hashes and source
commit. The copied out*/ and work/ data remain unchanged. The active changes are confined to writing experiments
and their evaluation. The v13 discovery/network/QeQ prompts and packet builder are retained unchanged; this is
not a claim that every inherited input or upstream instruction is optimal.

## Preserve the funnel; change its writing handover

`experiment.py prepare` freezes completed activation, network and QeQ records from a copied source arm. It also
freezes the writer brief, core evidence and immediate predecessor. New calls cannot regenerate those inputs.
Each candidate arm carries a manifest and hashes. Copied historical arms reject mutation through the v14 CLI.

`synthesis.py` retains every F record, QeQ annotation (E_F), Q record, independent axis (A), relevant image and
local meeting. It handles wrapped network entries and adjacent tags. Its image index shows this ayah's concrete
members and the suggested disclosure depth. Develop/assemble entries retain full members; meet/touch entries
carry local members plus movement, purpose and disclosure. Full source records remain in synthesis.json.

The writer composes connected explanations and decides how much space each earns. No fixed item cap or mandatory
passage list is used. Tags describe evidence; a same-word definition may matter more than a redundant staging.
A separate JSON account maps used items to an exact prose excerpt and an explanatory payoff. Mentioned, explained
and connected remain distinct claims. Unreported and deferred items, and unused passage candidates, are preserved
in handforward. An explicit remaining deferral keeps metadata compact. No model call is spent on bookkeeping.

## Context and inputs

The writer receives exact surrounding Quranic text, the concordance its instructions require, and only the variant
section of the old digest (not its conflicting usage table). Every input has an explicit job in the brief.
Only the immediately preceding commentary is supplied, with a warning against assuming unsupplied earlier delivery.
Within a prepared sequence, the second writer waits for the first candidate; it never silently falls back to old
prose. One-ayah context is an honest limit, not complete progressive disclosure across a long surah.

The 1:6 pilot input is 201,665 bytes versus v13's recorded 151,835. The previous 1:5 prose is 49,245 bytes. Thus
v14 does not yet demonstrate cheaper input or better prose. This context is a deliberate testable cost, and its
usefulness must be judged in the output. Removing it is a later ablation, not an assumed saving.

## Acceptance

`eval/regressions.json` contains ten passage-based criteria fixed before the candidate: eight preservation criteria
and two improvements (water-system integration and readable development). Existing weaknesses are improvement
targets, not retroactively declared regressions. Inherited mistakes are not protected merely because they appeared
in a baseline. Evaluation files and target baseline prose never enter a writer packet.

`review.py init` creates an independent review sheet and runs source/tag checks without editing the prose or calling
a model. Every criterion needs a verdict, exact candidate excerpt and explanation. `check` rejects a lost criterion,
uncertainty, incomplete accounting, source failures or changed evidence. There is no aggregate score. `accept` writes
an immutable pointer inside the candidate arm only if all checks pass; it never overwrites baseline text.

Mechanical checks establish exact quotation and accounting, not interpretive correctness. The independent reviewer
must read the explanations. A truthful regression verdict leaves the candidate experimental.

## Runs and limits

Opus generation remains high effort with a below-$5 historical estimate gate. The CLI requires --execute to make
that call. External writers use export → exclusive claim → one agent → ingest; their model and effort are recorded,
and their dollar cost stays unknown when the agent facility supplies no billing data. No automatic Opus repair is
triggered by an external Sol result. Source failures block acceptance; a separately authorized repair can be planned
within the standing one-repair limit. Generation is never retried and a started claim is permanent.

The user requested one Sol max trial on a selected ayah. Use 1:6, with v2 upstream and v2 1:5 as preceding prose.
This tests the v14 writing path and a different writer simultaneously. It cannot isolate the handover's effect from
the model change; an Opus control would be a separate authorized experiment. No other paid runs are authorized here.

Surah writing, the reciprocal final check, long-surah context, API caching/batching and revised output-cost estimates
remain outstanding. See INPUT_AUDIT.md for the inherited input gaps. v14 is a controlled writing experiment, not a
completed production pipeline.
