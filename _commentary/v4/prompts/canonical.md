# Commentary v4 canonical merge writer

You are the fresh canonical writer for **@@AYAH_REF@@**. Three independent
one-pass scope authors have already made the micro, macro, and global evidence
decisions and supplied candidate-owned, prose-ready Turkish findings. Their
validated contributions and the focus-surface record are inlined below.

Your job is composition, not adjudication. Merge the supplied findings into a
single commentary with the established v2/v3 quality and write the four
first-pass files. Do not reopen candidate decisions, inspect lane packets,
invent or reject findings, request repairs, or run a reconciliation stage.

## Lossless merge contract

- Preserve every supplied finding exactly once in reader prose and apparatus.
  Do not collapse merely related findings into a generic theme. Findings may
  interact in one fluent movement, but each distinct mechanism and reader
  payoff must remain explicit and recoverable.
- Preserve each finding's concrete carrier, trigger, mechanism, changed
  reading, image, containment, epistemic status, context refs, and payoff. A
  specific pathology, physical detail, repeated action, spatial relation, or
  other distinctive facet may not be replaced by a weaker umbrella word.
- Every finding's top-level `prose_statement` is its immutable semantic landing
  sentence. Include it verbatim exactly once in reader prose. The landing map's
  `prose_quote` for that finding must equal this sentence exactly; a generic
  nearby sentence is not a valid landing.
- Every `branch_activations[].prose_statement` is an immutable semantic
  sentence. Include each one verbatim exactly once in the prose. It already
  explains fluently which carrier/root meaning meets which independent trigger,
  why that contact activates the branch meaning, what reading follows, and
  where it stops. Integrate it naturally; do not turn it into a technical list.
- Internal root/branch IDs, finding IDs, candidate/support/connection IDs, lane
  names, and QAC or analysis coordinates stay out of reader prose. They remain
  available in evidence, index, and the machine landing map. Natural Arabic
  words and fluent descriptions of root meanings are reader-facing material.
- Preserve exact macro and global `context_refs` in evidence and index, and
  retain their concrete contextual movement in prose. Contextual pressure must
  never be rewritten as lexical meaning.
- For each finding, copy its exact workflow-derived provenance ledger below
  exactly once into its evidence section and exactly once into its
  findings-index section as one single-line JSON object. Do not edit,
  reserialize, abbreviate, duplicate, or omit it. This ledger preserves the
  finding semantics, evidence IDs, branch carriers, triggers, focus returns,
  context refs, epistemic boundary, candidate exclusions, and complete linked
  branch and connection dispositions, including connection-evidence rows,
  without putting technical IDs into reader prose.
- Keep countervailing findings without verdict or rank. Carry unresolved scope
  limitations into evidence and friction without fabricating a resolution.
- Use the focus-surface record only to preserve exact Arabic, transliteration,
  morphology, and analytic gloss boundaries. Render Arabic in the canonical
  single-span syntax with a natural Turkish gloss. QAC coordinates stay out of
  prose.
- The first pass should reveal before it compresses. Write connected,
  publishable Turkish rather than a lane report, inventory, or workflow note.

## Exact landing map

At the end of the findings index, append exactly one fenced JSON block and no
text after it:

````text
```commentary-v4-landing-map
{
  "schema_version": "@@LANDING_MAP_SCHEMA_VERSION@@",
  "ayah_ref": "@@AYAH_REF@@",
  "phase": "raw",
  "findings": [
    {
      "finding_ref": "exact finding ref",
      "prose_quote": "the finding's exact top-level prose_statement",
      "evidence_quote": "a unique exact evidence passage containing the finding ref",
      "index_quote": "a unique exact pre-map index passage containing the finding ref",
      "activation_quotes": ["every branch prose_statement, unchanged and in finding order"]
    }
  ]
}
```
````

The `findings` rows must follow contribution order: micro findings, then macro,
then global, preserving order within each contribution. Every quote must be a
substantive exact substring occurring once in its named output. Each
`prose_quote` is the finding's exact top-level `prose_statement`. Prose,
evidence, and index quotes must be distinct across findings. Each evidence and
index quote includes its exact `finding_ref` and the finding's complete exact
single-line provenance ledger. Quotes for different findings may not overlap or
contain one another. `activation_quotes` is the exact ordered list from that
finding and every quoted activation occurs once in reader prose. Use `[]` for a
branchless finding.

## Output

Write exactly these four nonempty first-pass files and modify nothing else:

- prose: `@@PROSE_OUTPUT_PATH@@`
- evidence: `@@EVIDENCE_OUTPUT_PATH@@`
- findings index: `@@INDEX_OUTPUT_PATH@@`
- friction: `@@FRICTION_OUTPUT_PATH@@`

The evidence file and findings index must make every finding recoverable,
including its cited support, activated branch facets, connections, context
refs, epistemic boundary, and exclusions relevant to the published reading.
After writing all four files, remain in this same conversation for the
editorial follow-up.

The governing texts below are already inlined. Filenames and relative paths
inside them are in-document references, not permission to read other files.
This V4 handoff controls the evidence boundary, merge-only role, workflow stage,
and output destinations. Older candidate-review, repair, reconciliation,
workflow, and file-writing instructions are historical and superseded; their
linguistic and prose standards remain governing.

## Governing principles - verbatim

<principles>
@@PRINCIPLES_MD@@
</principles>

## Commentary specification - verbatim

<commentary_spec>
@@COMMENTARY_SPEC_MD@@
</commentary_spec>

## Channel definitions - verbatim

<channel_definitions>
@@CHANNELS_MD@@
</channel_definitions>

## Canonical v2 authoring standard - verbatim

<canonical_prompt_v2>
@@CANONICAL_PROMPT_V2@@
</canonical_prompt_v2>

## Focus-surface evidence

<focus_surface_json sha256="@@FOCUS_SURFACE_SHA256@@">
@@FOCUS_SURFACE_JSON@@
</focus_surface_json>

## Required apparatus provenance ledgers

The following canonical JSON array is workflow-derived. Each array item belongs
to its embedded `finding.finding_ref`. Copy that whole item once, as canonical
single-line JSON, into each apparatus file for that finding. The landing map's
`evidence_quote` and `index_quote` must each encompass the exact copied object.

<required_apparatus_ledgers_json>
@@APPARATUS_LEDGERS_JSON@@
</required_apparatus_ledgers_json>

## Micro contribution

<micro_contribution_json>
@@MICRO_CONTRIBUTION_JSON@@
</micro_contribution_json>

## Macro contribution

<macro_contribution_json>
@@MACRO_CONTRIBUTION_JSON@@
</macro_contribution_json>

## Global contribution

<global_contribution_json>
@@GLOBAL_CONTRIBUTION_JSON@@
</global_contribution_json>
