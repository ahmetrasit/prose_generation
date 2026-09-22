# V5 source snapshot

The executable V5 workflow was copied at repository commit
`5da704350beafa97217f6ff2191812d97ca2ea23` before V8 Batch changes were made.
The copy includes source modules, pinned guidance, prompt templates, validators,
tests, operations tooling, the benchmark, and inter-ayah test instructions.

Generated `input/`, `raw/`, `editorial/`, `middle/`, `concise/`, and `output/`
trees were not copied. Neither were `.cache/`, `__pycache__/`, Firebase build
cache, operations runtime state, `.DS_Store`, or historical pricing/comparison
reports. Those are artifacts or runtime state, not executable workflow source.

V5 schema-version strings intentionally remain unchanged where V8 preserves an
artifact contract. Repository paths and package imports point to
`_commentary/v8_batch`; Batch transport additions are documented in
`ORCHESTRATION.md`.
