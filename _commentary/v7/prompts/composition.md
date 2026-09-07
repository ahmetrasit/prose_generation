# Commentary v7 scope prose

Continue as the **@@LANE@@** scope agent for **@@AYAH_REF@@**. This is the
planned second turn for your lane. Read your discovery JSON at
`@@DISCOVERY_OUTPUT_PATH@@` and develop fluent Turkish scope prose. Actively
look for further readings while explaining the findings; stay within your lane.

## Reading Purpose

@@READING_STANDARD@@

## Evidence and Earlier Work

@@EVIDENCE_INPUTS@@

The discovery JSON records your initial judgments. Its exclusions and finding
list are revisable, not a ceiling. Use the original evidence to check source
facts, restore missed details, and develop further readings. Explain new
readings fully in the prose so subsequent stages can carry them forward; do not
rewrite the discovery JSON.

Preserve every supported incoming finding, including distinct claims or images
inside a single finding. Correct mistaken grammar, morphology, lexical identity,
or citations from the source evidence. A lexical form restriction limits a
literal sense; it does not by itself defeat a contextual resonance. If concrete
counterevidence defeats a claim, briefly identify that correction and its basis
in your completion reply. Do not silently discard it or invent support to keep
it. No separate correction ledger is needed.

## Writing Contract

- Explain each reading's carrier, particular trigger, connection, and changed
  interpretation in ordinary language. Keep the ordinary sense recoverable,
  while giving secondary readings their full explanation.
- Preserve concrete details: a pathology, material image, repeated action,
  spatial relation, or before/after shift must not become a general theme.
  Explain the attested lexical connection and relevant form restrictions behind
  a same-root resonance, not only the resulting image.
- Use `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` whenever an Arabic
  word or phrase does interpretive work. Tags are paragraph-local: repeat the
  full tag if the item is used interpretively in another paragraph.
- Show every non-focus ayah reference beside the interpretation it supports,
  such as `(29:41)` or `(1:6, 1:7)`. List individual refs, not intervals. A host
  prefatory basmala used as context is cited as `(S:0)`.
- Write Turkish reader prose. Translate English source language naturally; keep
  internal IDs, QAC coordinates, and lane machinery out of the prose.
- Arrange related readings coherently without making their distinct evidence
  and consequences implicit. Keep necessary boundaries brief and local.

Write exactly one nonempty Markdown file and modify nothing else, except for
any monitor lifecycle command supplied by the orchestrator:

- prose: `@@SCOPE_PROSE_OUTPUT_PATH@@`

Before finishing, check that each supported incoming and newly developed reading
has its evidence, connection, and interpretive consequence explicit in the
prose. Then run the terminal monitor command supplied by the orchestrator.
