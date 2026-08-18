# Layer 3 v3 Implementation Status

Status as of 2026-08-18: **v3 code path implemented and locally tested;
production semantic passes have not been run.**

## Completed

- Layer 2 uses `_ayah_commentary/v2/PROMPT.md` through `scripts/instantiate.py`.
- Layer 2 v2 prompt/runbook references are aligned around explicit local
  resonances, no disambiguation, selective word analysis, four artifacts, and
  no prose quota.
- Layer 3 v3 now has active schemas:
  - `_channel/layer3/schemas/layer2-handoff-v1.schema.json`;
  - `_channel/layer3/schemas/source-packet-v3.schema.json`;
  - `_channel/layer3/schemas/discovery-hypotheses-v2.schema.json`;
  - `_channel/layer3/schemas/channel-briefs-v2.schema.json`;
  - `_channel/layer3/schemas/surah-composition-v1.schema.json`;
  - `_channel/layer3/schemas/surah-reading-evidence-v1.schema.json`.
- `_channel/layer3/scripts/build_packet.py` builds `layer3-source-packet-v3`:
  - requires Quran text, a typed Layer-1 primary floor, and complete Layer-2
    `prose/evidence/index/friction` artifacts for every numbered ayah;
  - parses every Layer-2 findings-index row;
  - projects `surprise:<id>` rows as local resonances;
  - carries Layer-2 evidence boundaries;
  - hashes Layer-2 prose and friction for lineage while withholding their
    content from semantic passes;
  - projects Network V3 activation cards and bounded V11 material when present;
  - writes language-aware packet filenames under immutable v3 run directories.
- `_channel/layer3/scripts/instantiate.py` is rewritten for v3:
  - validates packet/hypotheses/brief contracts before prompt generation;
  - writes immutable per-attempt prompts under
    `_channel/layer3/runs/v3/sNNN/{language}/{runId}/inputs/`;
  - defaults stage outputs under the same run directory;
  - discovery is blind to Layer 2;
  - review receives typed primary ground plus complete Layer-2 handoff;
  - compose expects a JSON composition envelope.
- `_channel/layer3/scripts/finalize.py` publishes validated composition output:
  - `N.surah-reading.{language}.md`;
  - `N.surah-reading.evidence.{language}.json`;
  - `N.surah-reading.friction.{language}.md`.
- `_channel/layer3/scripts/validate.py` validates packets, discovery
  hypotheses, channel briefs, composition envelopes, and publication evidence.
- Active Layer 3 prompts now require:
  - explicit reader-friendly channels and resonances;
  - no disambiguation among admitted channels;
  - incompatible channels to coexist when admitted;
  - complete accounting for every discovery hypothesis and local resonance;
  - no word, paragraph, channel, or length quota;
  - visible prose landings for every admitted channel and hinge.
- Runbooks/spec references updated:
  - `_channel/layer3/ORCHESTRATION.md`;
  - `COMMENTARY_SPEC.md`;
  - `docs/CHANNELS.md`;
  - `README.md`;
  - `_channel/README.md`;
  - `scripts/README.md`.
- `tests/test_layer3_channel_workflow.py` was replaced with stdlib `unittest`
  coverage for strict handoff selection, malformed indexes, discovery
  blindness, many-to-many review accounting, complete local-resonance
  dispositions, composition landings, and finalizer evidence hashes.

## Validation Completed

- `python3 -B -m unittest tests/test_layer3_channel_workflow.py` passes.
- AST parsing passes for:
  - `_channel/layer3/scripts/common.py`;
  - `_channel/layer3/scripts/build_packet.py`;
  - `_channel/layer3/scripts/instantiate.py`;
  - `_channel/layer3/scripts/validate.py`;
  - `_channel/layer3/scripts/finalize.py`.
- JSON parsing passes for all `_channel/layer3/schemas/*.schema.json`.
- Scoped `git diff --check` passes for the Layer 3 migration files.
- Real S87 packet build previously succeeded against `_commentary/outputs/s087`
  and wrote `/private/tmp/l3-s087-source-packet.tr.json` with 81 sources and one
  V11 fallback warning.
- Current v3 instantiation successfully generated
  `/private/tmp/l3-s087-discover-current.prompt.md` from that S87 packet.

## Not Completed

- No semantic Layer 3 discovery/review/compose agent pass has been run.
- No real S87 review or compose smoke has been run because that requires
  semantic outputs.
- A fresh real S87 packet rebuild could not be repeated after
  `_commentary/outputs/s087` disappeared from the current worktree. Do not
  restore or rewrite generated commentary outputs unless the user explicitly
  requests it.
- No commit has been made for the current v3 completion work in this turn.

## Current Worktree Warning

There are many unrelated dirty files outside this Layer 3 migration, including
deleted/generated `_commentary` outputs and bundle artifacts. They are not part
of the v3 implementation change set. Preserve them unless the user explicitly
asks to restore or remove them.

The intended Layer 3/doc/test change set is limited to:

- `README.md`;
- `COMMENTARY_SPEC.md`;
- `docs/CHANNELS.md`;
- `scripts/README.md`;
- `_channel/README.md`;
- `_channel/layer3/ORCHESTRATION.md`;
- `_channel/layer3/prompts/`;
- `_channel/layer3/schemas/`;
- `_channel/layer3/scripts/`;
- `tests/test_layer3_channel_workflow.py`.

## Remaining Work

1. Run actual semantic Layer 3 passes on a chosen surah:
   - discovery agent;
   - review agent;
   - compose agent;
   - finalizer.
2. Re-run a full real S87 packet build after the Layer-2 S87 output directory is
   available again.
3. Review the first real channel briefs manually for prose usefulness:
   - all admitted channels visible;
   - no ranking/disambiguation;
   - all local resonances accounted for;
   - claim policies strong enough to protect counterpressured material.
4. Commit and push the current v3 implementation once unrelated worktree
   changes are handled or carefully excluded from staging.
