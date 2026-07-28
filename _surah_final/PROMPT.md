# Final Surah Reconciliation Prompt

Read the inlined `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, and
`docs/CHANNELS.md` first. This file is the task.

## Task

Reconcile the Layer-3 draft prose with the reviewed channel plan and the
Layer-2.5 ayah overlays. Produce the publishable whole-surah prose only after
channel admission and disclosure have both been checked.

You receive:

- the original Layer-3 prose and thesis;
- the Layer-3 evidence surface;
- the reviewed channel plan;
- the validated Layer-2.5 overlay JSON and its reading preview.

Produce:

- `{S}.surah.final.prose.md`;
- `{S}.surah.final.validation.md`;
- `{S}.surah.final.friction.md`.

## Reconcile

Preserve the primary-grounded argument unless review evidence makes it
unsustainable. Use only channels with `reviewDecision: "accepted"`. Remove a
rejected channel completely; do not retain it as suggestive language. A `revise`
channel is not publishable.

For every accepted channel:

1. confirm that each member used in the final prose exists in the reviewed plan;
2. confirm that every local effect named in the final prose was seeded or
   explicitly omitted in the Layer-2.5 coverage;
3. make the complete channel feel like recognition of the ayah sequence, not a
   late catalogue of roots and branches;
4. state how it supports or shifts the whole-surah primary reading;
5. keep it distinct from the surah's primary-grounded argument.

Do not repeat the Layer-2.5 additions. The final prose gathers them into their
completed shape and shows what that shape does to the whole surah.

## Validation report

The markdown validation report is an audit surface. List every accepted channel,
its final-prose paragraph, its overlay coverage, and any reviewed member not used.
Record rejected and `revise` channels as excluded from prose. If the thesis
changed, state exactly why and map the change to evidence.

The final prose contains no provenance labels, IDs, review language, or apparatus.
