# Channel Workflows

The active channel workflow is [`layer3/`](layer3/ORCHESTRATION.md).
New runs are written under `layer3/runs/v3/` and use the prompts, schemas, and
scripts inside `layer3/`.

Files directly under `_channel/` that predate `layer3/` are retired. They remain
in place only so earlier experiments and generated prompts can be reproduced.
The active workflow does not import their prompts, plans, authority declarations,
or schemas.

Do not add new work to:

- `_channel/PROMPT.md`
- `_channel/PLAN.md`
- `_channel/REVIEW_AUTHORITY.json`
- `_channel/*.draft.prose.md`
- `_channel_review/`
- `_channel_integration/`
