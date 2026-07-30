# Layer 2 Editorial Authoring Prompt

Read the inlined editorial contract, result schema, ayah discovery ledger, and
ayah-specific editorial plan slice.

## Task

Write:

1. `{UNIT}.prose.md`
2. `{UNIT}.evidence.md`
3. `{UNIT}.index.md`
4. `{UNIT}.result.json`
5. `{UNIT}.friction.md`

## Prose

Write reader-facing commentary for this ayah in the target language.

- Keep the ayah's direct meaning reachable throughout.
- Follow the planned movements without turning placement labels into headings.
- Represent every planned finding. There is no finding or surprise cap.
- Consolidate repeated explanation, not distinct reader payoffs.
- Make before/after changes felt as reading experience.
- Return secondary readings to the ayah's own word and direct scene.
- Ground every outside-ayah trigger with its reference and relevant word or
  image.
- Do not state a surah thesis or name a channel registry.
- Do not expose internal IDs, confidence machinery, or workflow terminology in
  prose.
- Do not force uniform length or structure across ayahs.

New syntheses are allowed when they arise during writing. Add them to
`result.json` with component finding IDs and evidence references.

## Evidence

Map authored claims to finding IDs and evidence references. Mark local,
contextual, remote, and synthetic inference clearly. Record counterevidence and
coverage gaps.

## Index

Write one compact line for every represented finding and synthesis. The index
compresses wording, never field size.

## Result

`result.json` must list every represented finding and synthesis. It must also
record the four authored output paths (`prose`, `evidence`, `index`, and
`friction`) and the standalone checks. A successful result represents every
carried finding assigned by the plan.

In `result.json`, record only sibling filenames such as `{UNIT}.prose.md`, not
repo-relative or absolute paths.

Copy `sourceLedgerSha256` and `sourcePlanSha256` exactly from the inlined plan
slice. Do not calculate or normalize either hash.

## Friction

Record any plan claim that could not be written safely, any missing grounding,
or any conflict between the ledger and plan. Do not silently omit it.
