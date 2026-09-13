# Surah Commentary

The active whole-surah workflow is [v2/ORCHESTRATION.md](v2/ORCHESTRATION.md).
Its prompts, scripts, schemas, historical runs, and published outputs live
under `v2/`.

`PROMPT.md` is the retired, unversioned first experiment. It is preserved for
historical reproducibility and is not the active entry point.

V2 was moved from `_channel/layer3/`. Its active workflow now uses only the
completed final ayah editorials, as specified in the runbook. The earlier
channel-first contract is retained in `v2/LEGACY_ORCHESTRATION.md`; existing
legacy schema versions, `runs/v3/` paths, and run IDs remain unchanged.
The old `_channel/layer3` path is a compatibility symlink to `v2/`, so frozen
prompts and artifact references remain usable without rewriting their contents.
New commands and generated artifacts use the canonical `v2/` location.

New runs use `v2/scripts/workflow.py` and `runs/editorial-v1/`. They require no
upstream evidence sidecars or separate translation/network inputs.
