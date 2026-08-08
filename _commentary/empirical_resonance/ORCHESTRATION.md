# Empirical Resonance Orchestration

Status: draft.

This workflow creates a separate empirical resonance note for one ayah, an ayah
window, or a pericope. It can use completed Layer 2 commentary as an anchor, but
it does not modify Layer 2 and does not create tafsir claims.

## Stage 0: Select Scope

Choose a small scope:

- `ayah`: one ayah;
- `window`: one ayah plus immediate local context;
- `pericope`: a short contiguous unit when the empirical hook depends on the
  scene rather than one sentence.

The packet records `primary_refs` and `context_refs`. The output must not drift
outside that scope.

## Stage 1: Build Ayah Packet

Collect:

- Arabic ayah text and Turkish translation;
- token notes or branch refs if available;
- optional Layer 2 prose, evidence, and findings;
- any existing exclusions or cautions from commentary work.

Layer 2 is used for anchoring and wording only. It is not empirical evidence.

## Stage 2: Hook Scan

Identify candidate hooks from explicit ayah material:

- body, cognition, perception, illness, aging, sleep, emotion, memory;
- testimony, debt, contract, family, coercion, authority, reputation;
- agriculture, animals, ecology, weather, water, astronomy, navigation;
- material culture, travel, built environment, legal procedure.

Reject hooks that require a vague moral term to become a modern claim. Record
the rejection in packet `exclusions` when the rejected hook is tempting or
likely to recur.

## Stage 3: Source Discovery

This stage is optional only when a packet already contains enough
`research_sources`.

If external search is allowed, run
[`SOURCE_DISCOVERY_PROMPT.md`](SOURCE_DISCOVERY_PROMPT.md) before prose is
written. Prefer:

1. systematic reviews, meta-analyses, consensus statements, textbooks, and
   official statistics;
2. multiple independent primary studies;
3. single primary studies;
4. expert historical or institutional context;
5. popular summaries only as pointers to better sources, not as evidence.

For every retained source, record citation metadata and one or more
`relevant_claims` in the packet. Do not keep a source merely because it sounds
useful; it must bear directly on a hook.

The result of this stage is a frozen hermetic packet. The render prompt must not
add uncited empirical claims from memory.

## Stage 4: Hermetic Render

Run [`PROMPT.md`](PROMPT.md) against the frozen packet. The prompt emits:

- `Empirical Resonance`: continuous reader-facing prose;
- `Findings`: one row per claim, each with strength, sources, and limits;
- `Source Gaps`: relevant claims that could not be responsibly stated;
- `References`: full source list for every cited source ID.

Prose should be compact. It is acceptable for a run to produce no resonance
finding when the source packet is weak or the ayah has no concrete hook.

## Stage 5: Validation

Before accepting an output, check:

- every empirical claim has a source ID;
- every source ID resolves to a reference;
- every finding has one strength label from `SCHEMA.md`;
- no prose says or implies scientific proof, prediction, or replacement of
  tafsir;
- no social-science claim is universalized beyond its studied population or
  context;
- no Layer 2 claim is treated as empirical evidence.

## Future Script Targets

Provisional paths:

```text
_commentary/empirical_resonance/inputs/sNNN/S_A.empirical.packet.json
_commentary/empirical_resonance/outputs/sNNN/S_A.empirical.md
```

Pericope/window names can append a stable scope suffix:

```text
S_A-S_B.empirical.packet.json
S_A-S_B.empirical.md
```
