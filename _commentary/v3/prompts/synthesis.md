# Commentary v3 synthesis

Write the final Turkish commentary for **@@AYAH_REF@@** from the selected-evidence
packet below. The adjudicator has already decided admissibility. Use only its
`selections` and their registered supports and branches; add no outside knowledge
or new reading in this stage. Return one JSON object only; the workflow will
render prose, evidence, index, and friction files deterministically.

## Binding identity

- `source_canonical_sha256`: `@@SOURCE_SHA256@@`
- `docket_payload_sha256`: `@@DOCKET_SHA256@@`
- `adjudication_payload_sha256`: `@@ADJUDICATION_SHA256@@`
- `synthesis_packet_sha256`: `@@PACKET_SHA256@@`
- `prompt_sha256`: copy the exact `identity.prompt_sha256` value from the
  adjacent `.prompt.json` manifest supplied with this prompt

Echo all identity values exactly.

## Prose

- Write continuous, reader-facing Turkish in a single voice. Do not use headings,
  bullets, evidence labels, confidence labels, or candidate/support/branch IDs.
- Begin from the ayah's local wording and grammar. Let macro or global activation
  sharpen that local reading; do not turn a neighboring image into a surah-wide
  thesis.
- Cover every selected candidate visibly. Findings may share a paragraph only
  when the prose still leaves each reader payoff recoverable.
- Use each selection's `selection_basis.deletion_loss` as its minimum distinct
  contribution. Consolidate overlapping exposition, but do not erase that
  stated consequence from the final reading.
- Give every selected candidate an exact prose landing: copy its packet `claim`
  verbatim into a `landing_quote` that occurs verbatim in the named paragraph.
  Several claims may share one landing quote and paragraph.
- State the surprise turn in reader language: establish the ordinary reading,
  identify the supplied mechanism that changes its pressure, then say what the
  reader can now notice.
- Keep `inference` and especially `exploratory` findings naturally bounded in the
  prose. A resonance never replaces a word's local lexical sense. Supply an exact
  `containment_quote` from that prose sentence.
- When an ayah word is first discussed, prefer the established structured span
  `{ar:..., tr:..., gloss:...}` where the packet supplies enough form/gloss
  evidence. Do not fabricate transliteration or morphology.
- Produce between **@@MIN_PROSE_CHARS@@** and **@@MAX_PROSE_CHARS@@** prose
  characters in at most **@@MAX_PARAGRAPHS@@** paragraphs.

## Findings map

- Emit at most **@@MAX_FINDINGS@@** findings. Every packet selection ID must occur
  in one or more findings; no ID absent from `selections` may occur.
- Each finding cites at least one selected support for every candidate it carries.
  Cite branch refs only when those refs are already attached to the carried
  candidates. Across all findings carrying a candidate, cite every one of that
  candidate's `branch_refs`; none may silently disappear.
- `bundle_traceable` is reserved for direct word-analysis readings. Channel,
  cross-context, legacy, and newly recovered relations are `inference` or
  `exploratory`.
- `landing_quote` must be an exact, nonempty substring of the named prose
  paragraph and must contain the exact packet `claim` of each candidate it lands.
  `containment_quote` must also be exact for every inferential or exploratory
  finding; it may be `null` only for direct bundle-traceable findings.
- Use `baseline`, `supports_primary`, or `shifts_primary` to describe what the
  finding does to the ordinary reading. An exploratory finding cannot be baseline.

## Friction notes

Add at most **@@MAX_FRICTION_NOTES@@** notes only for a live alternative, scope
limit, evidence gap, or production issue that remains material after synthesis.
Do not repeat all rejected candidates; the workflow appends the complete
adjudication ledger automatically.

## Response contract

Use exactly this shape, without Markdown fences or extra keys:

```json
{
  "schema_version": "commentary-v3-synthesis-response-v1",
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
      "paragraph_key": "p01",
      "text": "Turkish prose paragraph",
      "finding_keys": ["local_clarity"]
    }
  ],
  "findings": [
    {
      "finding_key": "local_clarity",
      "title": "Short Turkish title",
      "summary": "Concise Turkish reading",
      "effect": "baseline",
      "epistemic_status": "bundle_traceable",
      "candidate_ids": ["cand_..."],
      "support_ids": ["sup_..."],
      "branch_refs": [],
      "paragraph_key": "p01",
      "landing_quote": "exact prose substring",
      "containment_quote": null
    }
  ],
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

Paragraph keys must be sequential (`p01`, `p02`, ...). Finding keys are unique
lowercase ASCII labels. JSON string content may be Turkish; keys and enums must
match the contract.

<selected_evidence_packet_json>
@@PACKET_JSON@@
</selected_evidence_packet_json>
