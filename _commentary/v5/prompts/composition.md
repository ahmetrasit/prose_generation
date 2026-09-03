# Commentary v5 scope composition

Continue as the **@@LANE@@** scope agent for **@@AYAH_REF@@**. This is the
planned second turn. The validated discovery ledger is authoritative for what
must be expressed; now render each finding as fluent, publishable Turkish.

Write exactly one JSON object to `@@CONTRIBUTION_OUTPUT_PATH@@` and modify
nothing else. This prompt includes the validated finding set and its compact
semantic requirements, so a replacement agent can perform the turn without a
second copy of the candidate-decision ledger or full lane packet.

## Composition Contract

- Preserve every finding's claim, mechanism, reader payoff, containment,
  semantic obligations, branch activations, and connections. Do not reopen,
  add, reject, merge, or split findings.
- Explain naturally why a meaning becomes active: name the Arabic carrier or
  its ordinary/root meaning, the independent word/image/relation that triggers
  it, the contact between them, the resulting changed reading, and its limit.
  Do not expose internal root, branch, finding, candidate, support, connection,
  obligation, lane, or QAC IDs in `prose`.
- Preserve concrete details. Do not replace a pathology, physical image,
  repeated action, spatial relation, before/after shift, or other distinctive
  semantic with an umbrella term.
- Turkish is mandatory in every reader-facing `prose` value. Translate English
  source formulations naturally. Do not copy English phrases such as
  "discernment" or "salience" into the Turkish prose.
- Wording is not immutable. You may combine compatible activation explanations
  into one fluent movement inside a finding, provided all structured semantics
  remain explicit and recoverable.
- The supplied semantic requirements are the compact rewrite contract. Map every
  record exactly once to a substantive exact passage in your prose. Related
  records may share one passage only when that passage explicitly carries all
  of them. Do not copy source payloads into the response.

## Response Schema

```json
{
  "schema_version": "@@SCOPE_COMPOSITION_SCHEMA_VERSION@@",
  "ayah_ref": "@@AYAH_REF@@",
  "lane": "@@LANE@@",
  "findings": [
    {
      "finding_ref": "exact discovery finding ref",
      "prose": "fluent Turkish paragraph or paragraphs",
      "semantic_landings": [
        {
          "semantic_refs": ["one or more consecutive semantic refs"],
          "prose_quote": "one substantive exact passage from this finding's prose"
        }
      ]
    }
  ],
  "friction_notes": ["composition limitation, if any"]
}
```

Return one row per discovery finding in exact order. Across its landing rows,
copy every semantic ref exactly once and in inventory order. Source hashes are
computed and bound by the workflow; do not echo them into the response.
Each prose quote must occur exactly once in that finding's prose; separate
landing quotes must not overlap. This map is compact traceability, not a place
to repeat the source semantics.

<principles>
@@PRINCIPLES_MD@@
</principles>

<commentary_spec>
@@COMMENTARY_SPEC_MD@@
</commentary_spec>

<channel_definitions>
@@CHANNELS_MD@@
</channel_definitions>

<canonical_prompt_v2>
@@CANONICAL_PROMPT_V2@@
</canonical_prompt_v2>

<validated_discovery_findings_json>
@@DISCOVERY_FINDINGS_JSON@@
</validated_discovery_findings_json>

<semantic_requirements_json>
@@SEMANTIC_REQUIREMENTS_JSON@@
</semantic_requirements_json>
