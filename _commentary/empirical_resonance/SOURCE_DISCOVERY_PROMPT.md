# Empirical Resonance Source Discovery Prompt

Use this prompt only when the run is allowed to search for external sources.
This stage prepares `research_sources` and candidate hooks for the hermetic
render prompt. It does not write reader prose.

## Task

Given one ayah, an ayah window, or a pericope, plus optional Layer 2 output,
identify concrete empirical hooks and collect sources that can responsibly
support or reject a resonance finding.

The output is a source packet fragment, not commentary.

## Source Standard

Prefer sources in this order:

1. systematic reviews, meta-analyses, consensus statements, textbooks, official
   statistics, or institutional reports;
2. multiple independent primary studies with compatible results;
3. single primary studies;
4. expert historical, legal, or institutional context;
5. popular summaries only as search leads, not as evidence.

For each source, capture enough metadata for the render output:

- source ID;
- source type;
- authors or responsible institution;
- year;
- title;
- venue or publisher;
- DOI or stable URL;
- relevant claim or claims;
- population, time period, and domain limits;
- reason the source was retained.

## Search Discipline

Search for the narrow empirical question, not for "Qur'an science" claims.

Good searches:

- prefrontal cortex executive function inhibitory control review
- eyewitness testimony memory stress intimidation systematic review
- debt contract witness social pressure literacy historical context

Bad searches:

- scientific miracles in the Qur'an
- proof that the Qur'an predicted neuroscience
- why two women equal one man scientifically

## Hook Rules

Keep only hooks grounded in explicit ayah material:

- a body part, bodily act, perception, cognitive act, emotion, memory, illness,
  sleep, aging, or death;
- a social or legal procedure, including testimony, debt, contract, inheritance,
  marriage, household relation, coercion, authority, reputation, or group action;
- a physical, ecological, agricultural, astronomical, navigational, or material
  process.

Reject hooks that require turning a general moral term into a modern scientific
claim. Record tempting rejected hooks under `exclusions`.

## Strength Pre-Assessment

For each retained source claim, suggest the likely strength label:

- `established`
- `well_supported`
- `plausible`
- `contested`
- `speculative`
- `unsupported`

Use the weakest honest label. For social-science and gender-related claims, be
especially cautious: task-specific, historical, access-based, and institutional
explanations are usually safer than claims about innate capacity.

## Required Output

````markdown
## Candidate Hooks

| hook_id | ayah_ref | text_anchor | domain | why_candidate | keep |
| --- | --- | --- | --- | --- | --- |

## Research Sources

```json
[
  {
    "source_id": "src01",
    "type": "review",
    "title": "...",
    "authors": ["..."],
    "year": 2021,
    "venue": "...",
    "doi": "...",
    "url": "...",
    "abstract_or_note": "...",
    "relevant_claims": [
      {
        "claim_id": "src01_c01",
        "claim": "...",
        "population_or_scope": "...",
        "limitations": "...",
        "suggested_strength": "well_supported"
      }
    ],
    "retention_reason": "..."
  }
]
```

## Exclusions

- <Rejected hook or source, with reason.>

## Discovery Notes

- <Any uncertainty, unresolved source conflict, or follow-up search need.>
````

## Hard Limits

- Do not write reader prose.
- Do not cite unsourced memory.
- Do not use apologetic websites or popular essays as evidence.
- Do not retain a source unless it bears directly on a grounded ayah hook.
- Do not generalize social-science findings beyond the population and context
  of the source.
