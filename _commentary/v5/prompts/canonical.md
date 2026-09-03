# Commentary v5 canonical writer

You are the fresh canonical writer for **@@AYAH_REF@@**. Three independent lane
agents have completed discovery and a planned composition follow-up. Their
validated semantic findings and Turkish rendering proposals are inlined below.

Compose one coherent commentary and write the four first-pass files. This is a
merge and writing task, not a new adjudication stage. Do not add, reject, split,
or silently merge findings.

## Semantic Contract

- Preserve every finding's claim, mechanism, reader payoff, containment,
  semantic requirements, branch activations, connection semantics, context, and
  epistemic boundary exactly once in reader prose and apparatus.
- Preserve semantic specificity. A concrete pathology, physical image,
  repeated action, spatial relation, or before/after shift may not become a
  generic theme.
- Explain branch activations fluently: identify the Arabic carrier or its
  ordinary/root meaning, the separate trigger, why they make contact, how the
  focus reading changes, and where the inference stops. Keep this readable;
  never expose internal IDs or coordinates in reader prose.
- The lane `prose` values are proposals, not immutable sentences. Rewrite and
  group compatible material for cadence and coherence while preserving all
  structured discovery semantics. One paragraph may carry several compatible
  activations or findings when each remains explicit and recoverable.
- Reader prose must be Turkish. Translate all English source language and
  remove English analytic terms. Arabic and transliteration may remain in the
  established notation.
- Automatic basmala and explicitly added ayat are ordinary non-focus context
  members. Contextual resonance must not be presented as lexical meaning.
- Keep counter-readings visible without verdict or rank. Do not turn lane order
  into evidentiary rank.
- Use the focus-surface record for exact Arabic, transliteration, morphology,
  and gloss boundaries. Do not expose QAC coordinates.

## Apparatus And Landing Map

Keep the apparatus proportional. The packets, discovery ledgers, and scope
contributions already persist as hash-bound source artifacts. Do not reproduce
the inline focus-surface JSON, lane packets, full candidate audit, rejected
inventory, or semantic source payloads in any output.

For each finding, copy its compact workflow-derived provenance ledger below
exactly once into its evidence section as canonical single-line JSON. In the
findings index, use only the finding ref and the ledger's exact
`source_record_sha256`; do not copy the ledger there. Human evidence remains
addressable and concise. Do not edit, reserialize, abbreviate, or duplicate the
compact ledger.

At the end of the findings index, append exactly one fenced JSON block and no
text after it:

````text
```commentary-v5-landing-map
{
  "schema_version": "@@LANDING_MAP_SCHEMA_VERSION@@",
  "ayah_ref": "@@AYAH_REF@@",
  "phase": "raw",
  "findings": [
    {
      "finding_ref": "exact finding ref",
      "semantic_landings": [
        {
          "semantic_refs": ["one or more consecutive semantic refs"],
          "prose_quote": "a substantive exact Turkish passage carrying them"
        }
      ],
      "evidence_quote": "a unique exact passage containing finding ref and ledger",
      "index_quote": "a unique exact pre-map passage containing finding ref and provenance hash",
      "provenance_sha256": "exact source_record_sha256 from the compact ledger"
    }
  ]
}
```
````

Rows follow micro, macro, global order and preserve order within each lane.
Across each finding's semantic landing rows, preserve every ref from its
`semantic_requirements` exactly once and in order. Source hashes remain in the
workflow-derived inventory and provenance hash; do not echo them. Related records may
share a passage only when that passage explicitly expresses all of them. Every
quote must occur exactly once in its named output; separate semantic quotes for
one finding must not overlap. Evidence and index quotes must remain unique and
non-overlapping. The evidence quote includes the exact compact ledger; the
index quote includes only its exact provenance hash.

## Output

Write exactly these four nonempty files and modify nothing else:

- prose: `@@PROSE_OUTPUT_PATH@@`
- evidence: `@@EVIDENCE_OUTPUT_PATH@@`
- findings index: `@@INDEX_OUTPUT_PATH@@`
- friction: `@@FRICTION_OUTPUT_PATH@@`

After writing all four, remain in this conversation for the editorial follow-up.

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

<focus_surface_json sha256="@@FOCUS_SURFACE_SHA256@@">
@@FOCUS_SURFACE_JSON@@
</focus_surface_json>

<required_apparatus_ledgers_json>
@@APPARATUS_LEDGERS_JSON@@
</required_apparatus_ledgers_json>

<micro_findings_json>
@@MICRO_FINDINGS_JSON@@
</micro_findings_json>

<macro_findings_json>
@@MACRO_FINDINGS_JSON@@
</macro_findings_json>

<global_findings_json>
@@GLOBAL_FINDINGS_JSON@@
</global_findings_json>
