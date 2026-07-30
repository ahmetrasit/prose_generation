# Surah Registry Reconciliation Prompt

Read the editorial contract, channel registry schema, and reconciliation schema.
The attached registries were produced independently for editorial pericopes in
the same surah.

## Task

Produce:

1. `whole-surah.channel-registry.json`
2. `whole-surah.registry-coverage.json`
3. `whole-surah.registry-friction.md`

This pass reconciles candidate identity. It does not write Layer 3 prose and it
does not adjudicate channel truth.

## Rules

- Preserve every source channel candidate.
- Merge candidates only when they express the same invariant and their members
  form one defensible chain.
- Keep similarly worded but mechanically different channels separate.
- Preserve every member finding ID and evidence reference.
- A source candidate may map to one or more resulting candidates when it
  contains separable systems.
- Do not reject a candidate here. Layer 3 performs channel adjudication.
- Record likely continuations and unresolved joins in friction.
- Copy the union of `sourceLedgers` from the input descriptor exactly into the
  reconciled registry.
- Copy `sourceRegistries` from the input descriptor exactly into the coverage
  output.

The coverage output must contain one row for every source candidate, marked
`represented` or `merged`, with at least one resulting candidate ID.
