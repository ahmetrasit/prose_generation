# Channel Review Prompt

Read the inlined governing documents first. This file is the task.

## Task

Independently review one draft channel plan. A Layer-3 draft may already have
channel prose and proposed maturity; a `sourceLane: channel-only` draft has
neither. In both cases your job is evidence admission, not prose repair.

You receive `{S}.surah.channels.draft.json` plus the applicable bundle and
evidence surface. A Layer-3 draft also carries its Layer-2 handoff. A
channel-only draft carries the lean channel bundle and channel-draft
adjudication surface; it deliberately does not reload Layer-2.

Produce `{S}.surah.channels.reviewed.json`, conforming to
`schemas/surah-channel-plan-v1.schema.json`, and
`{S}.surah.channels.review.md`.

## Review each channel

Apply all five membership tests in `docs/CHANNELS.md`:

1. every member has an exact lexical anchor;
2. non-primary branches contribute substantially;
3. the system recurs across more than one ayah;
4. the members explain one another as a system rather than sharing a topic;
5. the system changes both participating ayahs and the whole-surah reading.

Check the evidence refs, not just the descriptions. A valid root or branch ID
attached to the wrong morpheme is not an exact member identity. A Layer-2
inference, where present, remains an inference. A `network/v3` nomination
remains a candidate until this review.

For each draft channel set `reviewDecision` to:

- `accepted` when the system and all retained members pass;
- `rejected` when the system fails recurrence, coherence, exact identity, or
  yield;
- `revise` when the system may survive but the plan still contains unsupported
  members, missing effects, or an unusable maturity path.

Remove an unsupported member rather than weakening its description. Record the
reason in `reviewReason_tr` and preserve the rejected source in
`rejectedMotifs`.

## Author or review maturity

A channel-only draft intentionally carries `maturityStatus:
deferred-to-review` and an empty `maturityByAyah`. Do not reject that deferral.
After deciding which members survive, author the maturity path from those
members. For a Layer-3 draft, independently verify and revise the proposed path.

Maturity follows reading order and never moves backwards:

`latent` -> `emerging` -> `mature` -> `complete`

The state is determined by members the reader has encountered by that ayah, not
by what the reviewer knows about the completed surah.

- `latent`: one member; Layer 2.5 must say nothing about the channel.
- `emerging`: at least two encountered members whose relation is statable.
- `mature`: enough encountered members for the system's shape to be visible.
- `complete`: every accepted member has appeared.

Every `newMemberIds` and `recalledMemberIds` value must resolve to a retained
member. `focusAyahShift_tr` must describe the effect on that ayah, not repeat
the whole-surah yield. `disclosure_tr` may say only what has matured there.

## Output rules

Set top-level `reviewState` to `reviewed` and add `review`. Preserve stable IDs
unless an ID is invalid or duplicated. For a channel-only plan, set each
channel's `maturityStatus` to `reviewed`; grounding remains deferred to the
Layer-2.5 integration stage. Do not rewrite Layer-3 prose and do not create
Layer-2.5 additions.

The markdown report explains decisions and unresolved evidence gaps. It is an
audit surface, not reader prose.
