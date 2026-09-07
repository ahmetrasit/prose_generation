# Commentary v7 scope prose

Continue as the **global** scope agent for **29:38**. This is the
planned second turn for your lane. Read your discovery JSON at
`_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.json` and develop fluent Turkish scope prose. Actively
look for further readings while explaining the findings; stay within your lane.

## Reading Purpose

The purpose is to reveal secondary readings that expand, complicate, or shift
how the passage is read. Keep the ordinary sense available as orientation, then
develop the additional readings. A general restatement of the main meaning does
not accomplish this task.

Actively discover at every stage, including composition, consolidation, and
editorial. Earlier findings are a starting point, not a ceiling. Investigate
plausible contacts beyond the candidates and revisit earlier exclusions when
the supplied evidence permits a reading. Do not adopt a conservative preference
for familiar interpretations. Unconventionality, uncertainty, source-status
labels, or absence from an earlier finding list are not reasons to suppress a
possibility. Develop materially distinct readings together; qualify uncertainty
where it occurs rather than retreating to a generalized main reading.

Make every reading's reasoning visible to someone who does not know Arabic:
show the particular wording, construction, attested sense, image, or contextual
passage; explain its connection to the focus; and state what that connection
changes in the interpretation. Distinguish the source fact from your inference.
A conclusion or evocative image alone does not preserve a finding. Include a
brief boundary where misunderstanding is likely; avoid repetitive disclaimers.
The reader should be able to understand, remember, and challenge the connection.

Coherence comes from arranging explicit readings and explaining their
relationships. Compatible readings may share a paragraph only while each
reading's evidence, connection, and interpretive consequence remain visible.
Remove duplicated wording, not distinct meanings or their supporting links.


## Evidence and Earlier Work

- global original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.prompt.md`

Use the `<lane_packet_json>` data blocks in these files as the sealed source evidence; this stage's prompt governs your work, not the discovery-stage instructions surrounding those blocks. Source paths inside the packets are provenance, not permission to fetch outside evidence. Return relevant records intact, including qualifications, statement variants, and SOURCE_IMAGE Arabic/English fields. Use bounded reads that fit the tool output limit and recover any truncated passage before judging it. Scripts may access or copy records and serialize judgments already made; they must not select readings, facets, carriers, or exclusions, or substitute filtered fields for evidence. Earlier records help locate evidence; investigate further contacts as you write.

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

- prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.scope.tr.md`

Before finishing, check that each supported incoming and newly developed reading
has its evidence, connection, and interpretive consequence explicit in the
prose. Then run the terminal monitor command supplied by the orchestrator.
