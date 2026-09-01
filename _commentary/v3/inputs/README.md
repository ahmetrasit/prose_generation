# Generated inputs

The v3 CLI writes typed, deterministic model inputs here:

- `source/sNNN/`: canonical minified snapshots of ingested hermetic ayah bundles;
- `prepared/sNNN/`: canonical minified source identity, scope audit, quarantine diagnostics, and seed ledger;
- `adjudication/sNNN/`: canonical minified adjudication-safe dockets, prompts, and exact pretty prompt manifests;
- `synthesis/sNNN/`: canonical minified selected-evidence packets, prompts, and exact pretty prompt manifests.
- `authoring/sNNN/S_A/`: content-addressed hermetic micro, macro, global,
  reconciliation, repair, prose-follow-up, genuine prose-rewrite, merge, and
  verbatim editorial prompts for one ayah, plus canonical-writer pre-turn
  workspace guards. Embedded JSON is canonical and minified; no evidence is
  sampled or semantically compressed. Native multi-agent orchestration may pass
  the paired expected response/output path beside the prompt path, but must not
  inline or summarize prompt contents.

Quarantined evidence is retained only in `prepared/` and is never copied into a
model docket.
