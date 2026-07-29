# Pericope Editorial Compiler Prompt

Read the inlined editorial contract and both output schemas. The attached
discovery ledgers cover one editorial pericope.

## Task

Produce:

1. `{PERICOPE}.editorial-plan.json`
2. `{PERICOPE}.channel-registry.json`
3. `{PERICOPE}.friction.md`

This is planning, not final prose.

## Editorial plan

Construct one ayah plan for every ayah in the pericope.

- Give each ayah a reachable primary floor and a governing movement.
- Arrange placements in reading order.
- Attach every carried finding ID to at least one placement.
- Merge repeated explanation only by placing all affected finding IDs together.
- Preserve contradictory or parallel pressures when the ledgers preserve them.
- Create editorial syntheses when several findings form a grounded new reading.
- Give every synthesis a local owner ayah, component finding IDs, evidence
  references, support level, and primary relation.
- Keep every ayah independently intelligible. A later ayah may activate a
  finding, but the plan must provide the triggering word or image rather than
  assume the reader knows it.

There is no target number of placements, findings, or syntheses. Density follows
the evidence.

## Channel registry

Nominate cross-ayah systems separately from the ayah plans.

- A channel candidate needs members from at least two ayahs.
- Each member points to a carried finding and states its contribution.
- State the invariant that makes the members one system.
- State the reasoning chain rather than merely listing motifs.
- Preserve counterevidence and uncertain joins.
- Do not remove a finding from Layer 2 because it also belongs to Layer 3.
- Do not force every finding into a channel.

## Coverage

The plan's `findingCoverage` must account for every discovery finding:

- `represented` for every `carry` finding, with an ayah and placement;
- `upstream-blocked` for every discovery finding already marked `blocked`.

The compiler may not create a new blocked disposition.

Copy the `sourceLedgers` array exactly from the compiler input descriptor into
both JSON outputs. Do not calculate, reorder, or normalize the hashes.

## Friction

Record unresolved duplicate identities, contradictory ledgers, uncertain
pericope boundaries, and channel candidates that may continue outside the
current pericope.
