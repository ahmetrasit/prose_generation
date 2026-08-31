# Commentary v3 canonical merge

Write the final Turkish commentary for **@@AYAH_REF@@** from the complete set of
accepted micro, macro, and global findings below. Use every accepted finding and
only the supplied evidence. Add no outside knowledge.

The prose is the primary result. The JSON findings map is an audit surface that
must demonstrate coverage without controlling the prose's wording or order.

## Binding identity

- `source_canonical_sha256`: `@@SOURCE_SHA256@@`
- `docket_payload_sha256`: `@@DOCKET_SHA256@@`
- `adjudication_payload_sha256`: `@@ADJUDICATION_SHA256@@`
- `synthesis_packet_sha256`: `@@PACKET_SHA256@@`
- `prompt_sha256`: copy the exact `identity.prompt_sha256` value from the
  adjacent `.prompt.json` manifest supplied with this prompt

Echo all identity values exactly.

## Governing prose contract

@@CANONICAL_PROSE_CONTRACT@@

## Merging the three scopes

`micro`, `macro`, and `global` are evidence scopes, not prose sections, ranks,
or competing theses.

- **Micro** keeps the ayah's wording, morphology, syntax, sound, and local
  lexical work exact. It supplies the reader's footing.
- **Macro** records what the declared pericope or neighboring ayahs genuinely
  activate, sharpen, revise, or place under pressure.
- **Global** records grounded reader-walk, cross-run, and wider-context findings,
  including bounded surprises that remain local enough to change this ayah's
  reading.

Before drafting, silently audit all three scopes. Then compose by the ayah's own
movement. Do not write a micro section followed by macro and global appendices.
Do not let the local material crowd out later-context findings, and do not let a
vivid wider resonance displace the plain local reading. When findings from
different scopes perform the same work and give the same reader payoff, they may
share one passage. When they differ in mechanism, payoff, or direction, each
must remain recoverable even if they occupy the same broader movement.

The finding records appear in packet order only so coverage can be checked.
That order does not govern paragraph order. A `landing_quote` identifies the
passage that carries a finding; it does not need to copy the adjudicator's claim,
and compatible findings may identify the same or overlapping prose passage.

## Coverage map

- Emit exactly **@@REQUIRED_FINDING_COUNT@@** finding records, one for every
  packet selection, in packet order, using keys `f001`, `f002`, and so on.
- Each record carries the singular `candidate_id` at that packet position and
  copies its complete `support_ids` and `branch_refs` arrays. These requirements
  protect coverage and lineage; they do not prescribe prose phrasing.
- Assign each finding to the paragraph that carries it. Paragraphs may organize
  findings in any reader-serving order. A transition paragraph may have an
  empty `finding_keys` array.
- `landing_quote` must be a nonempty exact substring of the assigned paragraph.
  It may be a natural sentence or passage written by the author. It need not be
  unique and need not contain the packet claim verbatim.
- Use `bundle_traceable` for direct word-analysis readings. Use `inference` or
  `exploratory` for channel, neighboring-context, cross-run, or newly recovered
  relations. An exploratory finding cannot be `baseline`.
- Use `baseline`, `supports_primary`, or `shifts_primary` to describe the
  finding's relation to the ordinary reading. These labels remain in apparatus,
  never in prose.

The paragraph, finding, and friction counts have fail-loud infrastructure
ceilings of **@@PARAGRAPH_SAFETY_CEILING@@**, **@@REQUIRED_FINDING_COUNT@@**, and
**@@FRICTION_SAFETY_CEILING@@** respectively. They are not editorial targets or
compression instructions. There is no prose-length quota.

## Friction notes

Emit every still-material live alternative, scope limit, evidence gap, or
production problem in `friction_notes`; keep those notes out of reader prose.
Set `friction_complete=true` after the audit. The workflow joins the full
adjudication and branch ledgers deterministically, so do not paste them into the
commentary.

## Response contract

Return one JSON object only, without Markdown fences or extra keys:

```json
{
  "schema_version": "commentary-v3-synthesis-response-v3",
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
      "title": "Short Turkish apparatus title",
      "summary": "Concise Turkish reading",
      "effect": "baseline",
      "epistemic_status": "bundle_traceable",
      "candidate_id": "cand_...",
      "support_ids": ["sup_..."],
      "branch_refs": [],
      "paragraph_key": "p001",
      "landing_quote": "natural exact passage from the assigned paragraph"
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
