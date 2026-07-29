# Layer 3 Channel Authoring Prompt

Read the inlined editorial contract, result schema, and channel registry.

## Task

Write:

1. `{PERICOPE}.channels.prose.md`
2. `{PERICOPE}.channels.evidence.md`
3. `{PERICOPE}.channels.result.json`
4. `{PERICOPE}.channels.friction.md`

## Channel prose

Build the complete recurring images and meaning systems visible in this
pericope.

- State the invariant that makes the members one channel.
- Show how each member changes or extends the accumulated image.
- Distinguish the channel from the primary argument.
- Keep every member anchored to its ayah and local word.
- Make the whole feel like recognition of previously grounded local findings.
- Preserve counterevidence and weak joins at their real strength.
- Do not admit a channel merely because several findings share vocabulary.
- Do not impose a maximum or preferred number of channels.

Layer 3 may select for coherence. Rejected candidates remain accounted for in
the result and evidence; their Layer 2 findings remain valid local material.

## Result

Account for every registry candidate as:

- `accepted`;
- `merged`;
- `revised`;
- `rejected`.

Every accepted or revised channel must list its source candidates, member
finding IDs, ayah sequence, relation to the primary floor, and prose section.
Every merged or rejected candidate must state why.

Copy `sourceRegistrySha256` exactly from the inlined Layer 3 input descriptor.
Do not calculate or normalize the hash.

## Evidence and friction

Evidence maps channel claims to registry members and original evidence
references. Friction records unresolved joins, likely cross-pericope
continuations, and missing grounding.
