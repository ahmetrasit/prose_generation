# Commentary v3 synthesis

Write the final Turkish commentary for **@@AYAH_REF@@** from the complete
selected-evidence packet below. The adjudicator has already decided admission.
Use every selection and only the registered evidence supplied here; add no
outside knowledge or new reading. Return one JSON object only. The workflow
renders prose, evidence, index, and friction files deterministically.

## Binding identity

- `source_canonical_sha256`: `@@SOURCE_SHA256@@`
- `docket_payload_sha256`: `@@DOCKET_SHA256@@`
- `adjudication_payload_sha256`: `@@ADJUDICATION_SHA256@@`
- `synthesis_packet_sha256`: `@@PACKET_SHA256@@`
- `prompt_sha256`: copy the exact `identity.prompt_sha256` value from the
  adjacent `.prompt.json` manifest supplied with this prompt

Echo all identity values exactly.

## Lossless prose contract

- Write continuous, reader-facing Turkish in a single voice. Do not use headings,
  bullets, evidence labels, confidence labels, or candidate/support/branch IDs.
- Begin from the ayah's local wording and grammar. Let macro and global evidence
  sharpen the local reading without turning a neighboring image into an
  unrestricted surah-wide thesis.
- Preserve every selected contribution. Expository grouping is allowed only when
  each candidate still has its own non-overlapping `landing_quote`; no candidate,
  mechanism, reader payoff, or bounded surprise may be merged away for density.
- For each selection, copy its exact `claim` into that candidate's
  `landing_quote`. Express its `reader_payoff`, mechanism, and any needed
  `containment` in natural Turkish around that claim; do not paste those fields
  mechanically. The normalized quote must occur exactly once in the complete
  published prose and within its assigned paragraph. Landing quotes may not
  overlap one another.
- The structured evidence output retains each selection's complete `mechanism`,
  `selection_basis.deletion_loss`, `support_quote`, support set, and branch set.
  Make the prose explain the supplied mechanism naturally, but never copy
  apparatus identifiers from a mechanism into reader prose.
- State each surprise turn in reader language: establish the ordinary reading,
  identify the supplied mechanism that changes its pressure, and state what the
  exact reader payoff now makes visible.
- Develop the selected morphology, syntax, lexical range, sound, and neighboring
  contacts as exposition, not as a checklist. Do not compress a small grammatical
  or lexical contribution merely because it supports a larger finding.
- Keep `inference` and especially `exploratory` contributions naturally bounded.
  A resonance never replaces a word's local lexical sense. State a needed boundary
  once in a short reader-facing clause; never paste a dictionary's rejected-sense
  inventory into prose.
- Do not expose internal word or morpheme coordinates, analysis-record language,
  lane names, or workflow vocabulary such as `Coda`, `perfect`, `mikro-inferans`,
  `ankraj`, `scope limit`, or `bounded inference`. Ayah references are allowed.
- Remove semantic repetition before returning the response. Closely related
  findings may share a paragraph, but each distinct contribution must be explained
  once and retain its own exact, non-overlapping landing quote.
- When an ayah word is first discussed, prefer the established structured span
  `{ar:..., tr:..., gloss:...}` where the packet supplies enough form/gloss
  evidence. Do not fabricate transliteration or morphology.
- Produce between **@@MIN_PROSE_CHARS@@** and **@@MAX_PROSE_CHARS@@** prose
  characters. The lower bound includes the deterministic minimum required to
  land every selected contribution. The fail-loud paragraph safety ceiling is
  **@@PARAGRAPH_SAFETY_CEILING@@**; it is not a density target.

## Exact findings map

- Emit exactly **@@REQUIRED_FINDING_COUNT@@** findings: one for every packet
  selection, in exact packet order. Use keys `f001`, `f002`, and so on. Each
  finding carries the singular `candidate_id` of the selection at that position.
- Copy that selection's complete `support_ids` and complete `branch_refs` arrays
  exactly. Do not choose a representative subset.
- `landing_quote` must be the unique, non-overlapping prose substring described
  above and must contain that selection's exact claim. The exact reader payoff,
  containment, mechanism, deletion loss, and lineage remain in the deterministic
  evidence apparatus even when prose renders them more naturally.
- `bundle_traceable` is reserved for direct docket `word_analysis` readings.
  Channel, cross-context, legacy, and newly recovered relations are `inference`
  or `exploratory`.
- Use `baseline`, `supports_primary`, or `shifts_primary` to describe what the
  finding does to the ordinary reading. An exploratory finding cannot be baseline.
- Paragraph keys are sequential `p001`, `p002`, and so on. Across paragraphs,
  `finding_keys` must flatten to `f001` through the final finding without any
  omission, duplication, or reordering.

## Friction notes

Emit every still-material live alternative, scope limit, evidence gap, or
production issue. The fail-loud note safety ceiling is
**@@FRICTION_SAFETY_CEILING@@**; it is not a quota. Set `friction_complete=true`
only after all such notes have been emitted. The workflow appends the complete
adjudication and branch ledgers automatically, so do not repeat them.

## Response contract

Use exactly this shape, without Markdown fences or extra keys:

```json
{
  "schema_version": "commentary-v3-synthesis-response-v2",
  "identity": {
    "ayah_ref": "@@AYAH_REF@@",
    "source_canonical_sha256": "@@SOURCE_SHA256@@",
    "docket_payload_sha256": "@@DOCKET_SHA256@@",
    "adjudication_payload_sha256": "@@ADJUDICATION_SHA256@@",
    "synthesis_packet_sha256": "@@PACKET_SHA256@@",
    "prompt_sha256": "copy the 64-hex value from the adjacent prompt manifest"
  },
  "paragraphs": [
    {
      "paragraph_key": "p001",
      "text": "Turkish prose paragraph",
      "finding_keys": ["f001"]
    }
  ],
  "findings": [
    {
      "finding_key": "f001",
      "title": "Short Turkish title",
      "summary": "Concise Turkish reading",
      "effect": "baseline",
      "epistemic_status": "bundle_traceable",
      "candidate_id": "cand_...",
      "support_ids": ["sup_..."],
      "branch_refs": [],
      "paragraph_key": "p001",
      "landing_quote": "unique exact prose substring containing the exact claim"
    }
  ],
  "friction_complete": true,
  "friction_notes": [
    {
      "kind": "scope_limit",
      "summary": "Concise Turkish note",
      "candidate_ids": ["cand_..."],
      "support_ids": ["sup_..."]
    }
  ]
}
```

JSON string content may be Turkish; keys and enums must match the contract.

<selected_evidence_packet_json>
@@PACKET_JSON@@
</selected_evidence_packet_json>
