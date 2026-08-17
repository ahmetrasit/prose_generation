# Commentary Orchestration

Active ayah commentary work uses `_ayah_commentary/v2/PROMPT.md`, with inputs
and generated work products coordinated by the existing scripts under `scripts/`
and `_commentary/`.

New Layer 2 prompts must use the tiered bundle workflow documented in
`ORCHESTRATION.md`: build the full source bundle with `scripts/build_bundle.py`,
transform each ayah with `scripts/tier_branch_payloads.py`, then pass the tiered
directory to `scripts/instantiate.py --bundles-dir`. Do not instantiate new
Layer 2 prompts directly from the full base bundle.

The separate multi-stage workflow formerly called v2 is archived under
`archive/_commentary/v2/`; it is unrelated to the active ayah prompt version.
Nothing under `archive/` is an active workflow or should be used for new runs
unless it is redesigned and explicitly reactivated.
