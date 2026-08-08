# Empirical Resonance Workflow

Status: draft.

This workflow produces a reader-facing support layer for ayat that mention
observable human, social, biological, physical, ecological, legal, or cognitive
phenomena. It is not tafsir, not proof rhetoric, and not an audit artifact. Its
job is to help a reader notice where disciplined contemporary knowledge may make
the ayah's wording, scene, or practical framing more legible.

The workflow stages are in [`ORCHESTRATION.md`](ORCHESTRATION.md). Source
discovery is guided by [`SOURCE_DISCOVERY_PROMPT.md`](SOURCE_DISCOVERY_PROMPT.md).
The active render prompt is [`PROMPT.md`](PROMPT.md). The source and output
contract is [`SCHEMA.md`](SCHEMA.md).

## Position in the Commentary System

Empirical resonance sits after ayah selection and can be run on one ayah, a small
ayah window, or a pericope. It may optionally consume completed Layer 2 prose and
evidence when available.

It does not change Layer 2 obligations. Layer 2 explains the ayah on its own
Arabic terms. Empirical resonance adds a separate support surface for modern
empirical checking.

## Inputs

Each run should receive:

- ayah text, reference, translation, and any local context ayat included in the
  packet;
- optional Layer 2 prose and evidence surface for the same ayah or window;
- candidate empirical hooks extracted upstream or proposed by the run packet;
- source notes with enough citation metadata to let the reader follow up.

The render agent must not use unsourced memory for factual empirical claims. If a
likely finding needs research that is not supplied, it records a source gap. A
separate source-discovery pass may use external search when the run explicitly
allows it, but its selected sources must then be frozen into the packet.

## Output

The output is disciplined prose plus a compact findings list. Every finding has:

- the ayah hook it enters through;
- the empirical domain;
- the claim;
- the attached strength;
- source references;
- limits and non-claims.

Strength labels are for reader checking, not internal audit. They tell the reader
how cautiously to carry a finding and where to look next.

## Non-Goals

- Do not claim that modern science proves the Qur'an.
- Do not force empirical material into ayat that do not give a concrete hook.
- Do not override Arabic, grammar, fiqh, asbab, or Layer 2 commentary.
- Do not turn debated psychology or sociology into biological determinism.
- Do not make apologetic claims stronger than the supplied sources support.

## Provisional File Layout

```text
_commentary/empirical_resonance/
  ORCHESTRATION.md       workflow stages
  SOURCE_DISCOVERY_PROMPT.md
  PROMPT.md              hermetic render prompt
  SCHEMA.md              packet and output contract
  inputs/sNNN/           future generated source packets
  outputs/sNNN/          future generated empirical resonance notes
```
