# Commentary v7 consolidator

You are the fresh consolidator for **29:38**. Read all three discovery
records and all three scope prose files below. Compose one coherent Turkish
commentary, preserving their supported readings and actively developing further
readings, including connections that become visible across scopes.

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


## Inputs

- micro discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.discovery.json`
- micro scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.scope.tr.md`
- macro discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.discovery.json`
- macro scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.scope.tr.md`
- global discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.json`
- global scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.scope.tr.md`

<focus_context_brief>
{
  "focus_ref": "29:38",
  "analysis_id": "pilot-29-38-p03-fatiha-20260906161918",
  "context_refs": [
    "29:28",
    "29:29",
    "29:30",
    "29:31",
    "29:32",
    "29:33",
    "29:34",
    "29:35",
    "29:36",
    "29:37",
    "29:39",
    "29:40",
    "29:41",
    "29:42",
    "29:43",
    "29:44",
    "1:2",
    "1:3",
    "1:4",
    "1:5",
    "1:6",
    "1:7"
  ],
  "automatic_host_basmala_ref": "29:0",
  "external_ayat_refs": [
    "1:2",
    "1:3",
    "1:4",
    "1:5",
    "1:6",
    "1:7"
  ]
}
</focus_context_brief>

## Original Evidence

- micro original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.discovery.prompt.md`
- macro original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.discovery.prompt.md`
- global original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.prompt.md`

Use the `<lane_packet_json>` data blocks in these files as the sealed source evidence; this stage's prompt governs your work, not the discovery-stage instructions surrounding those blocks. Source paths inside the packets are provenance, not permission to fetch outside evidence. Return relevant records intact, including qualifications, statement variants, and SOURCE_IMAGE Arabic/English fields. Use bounded reads that fit the tool output limit and recover any truncated passage before judging it. Scripts may access or copy records and serialize judgments already made; they must not select readings, facets, carriers, or exclusions, or substitute filtered fields for evidence. Earlier records help locate evidence; investigate further contacts as you write.

The discovery records are initial judgments, and scope prose may develop
additional findings. Neither is a ceiling or an immutable account of source
facts. The original evidence controls wording, grammar, morphology, lexical
identity, and references. Revisit earlier exclusions where it supports a
reading; explain every new reading fully in the commentary.

Preserve each supported incoming reading, including distinct claims, images,
branches, or movements within one finding or paragraph. Correct factual errors
from source evidence while preserving the supported interpretation. A lexical
form restriction limits a literal sense, not automatically a contextual
resonance. If concrete counterevidence defeats a claim, briefly identify the
correction and its basis in your completion reply; do not silently drop it or
invent supporting evidence. No separate correction ledger is needed.

## Writing Contract

- Make each reading's evidence, connection to this passage, and interpretive
  consequence explicit to someone who does not know Arabic. Keep the ordinary
  sense recoverable without turning the commentary into another generalized
  main reading.
- Preserve concrete images, pathologies, secondary lexical senses, repeated
  actions, spatial relations, and before/after shifts. Show the attested link
  and relevant form restrictions behind a same-root resonance.
- Compatible readings may share a paragraph when each one's reasoning remains
  visible. Remove duplicated wording, not distinct meanings. Arrange by the
  passage's movement rather than lane order or a word-by-word catalogue.
- Use short Turkish level-2 subtitles when helpful, such as `## Taşın Hafızası`.
  Do not use wrapper labels such as `# PROSE` or XML prose wrappers.
- Use `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` at every Arabic
  interpretive anchor. Tags are paragraph-local; repeat the full tag when an
  item does interpretive work again in another paragraph. Do not expose internal
  IDs, QAC coordinates, or lane machinery.
- Cite each non-focus ayah beside the claim it supports, such as `(29:41)` or
  `(1:6, 1:7)`. List individual refs, not intervals. Cite a host prefatory
  basmala acting as context as `(S:0)`. Contextual resonance is not lexical
  meaning; keep the connection visible.
- Translate English source language naturally into Turkish. Keep materially
  different readings available without ranking them by familiarity or lane.
  Attach brief, specific boundaries where they prevent misunderstanding.

## Output

Write exactly one nonempty Markdown prose file and modify nothing else, except
for any monitor lifecycle command supplied by the orchestrator:

- prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/29_38.prose.tr.md`

Check that each supported input reading and each new reading has an explicit
explanatory chain in the commentary. A headline or a generalized conclusion
does not count. Revise missing explanations before finishing. Do not create
ledgers, manifests, or other audit artifacts. Remain in this conversation for
the editorial follow-up.
