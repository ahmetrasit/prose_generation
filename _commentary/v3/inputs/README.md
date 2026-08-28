# Generated inputs

The v3 CLI writes typed, deterministic model inputs here:

- `source/sNNN/`: exact byte snapshots of ingested hermetic ayah bundles;
- `prepared/sNNN/`: source identity, scope audit, quarantine diagnostics, and seed ledger;
- `adjudication/sNNN/`: adjudication-safe dockets, prompts, and exact prompt manifests;
- `synthesis/sNNN/`: validated selected-evidence packets, prompts, and exact prompt manifests.

Quarantined evidence is retained only in `prepared/` and is never copied into a
model docket.
