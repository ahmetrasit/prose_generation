# Commentary Orchestration

Active ayah commentary work uses `_ayah_commentary/v2/PROMPT.md`, with inputs
and generated work products coordinated by the existing scripts under `scripts/`
and `_commentary/`.

The retired direct-instantiation path documented in `ORCHESTRATION.md` builds a
full source bundle, applies `scripts/tier_branch_payloads.py`, and passes the
tiered directory to `scripts/instantiate.py --bundles-dir`. Do not use that path
for new multi-agent Layer 2 work.

The separate multi-stage workflow formerly called v2 is archived under
`archive/_commentary/v2/`; it is unrelated to the active ayah prompt version.
Nothing under `archive/` is an active workflow or should be used for new runs
unless it is redesigned and explicitly reactivated.

For parallel prose-first authoring from validated v3 source bundles and
adjudication dockets, use the simplified v4 runbook:
[`v4/ORCHESTRATION.md`](v4/ORCHESTRATION.md). V4 preserves the established
V2/V3 linguistic and prose standard inside three one-pass scope-author prompts,
then uses a merge-only canonical writer and same-writer editorial turn. Its
fixed per-ayah paths have no persisted sessions or repair state machine.
