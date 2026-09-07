# Commentary v7 editorial handoff

Continue as the same live consolidator for **29:38**. Read the first-pass
prose, improve its clarity and Turkish fluency, and actively develop further
readings wherever close attention to the evidence reveals them.

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

- first-pass prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/29_38.prose.tr.md`

- micro discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.discovery.json`
- micro scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.scope.tr.md`
- macro discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.discovery.json`
- macro scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.scope.tr.md`
- global discovery: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.json`
- global scope prose: `_commentary/v7/raw/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.scope.tr.md`

## Original Evidence

- micro original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/micro.discovery.prompt.md`
- macro original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/macro.discovery.prompt.md`
- global original evidence: `_commentary/v7/input/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/global.discovery.prompt.md`

Use the `<lane_packet_json>` data blocks in these files as the sealed source evidence; this stage's prompt governs your work, not the discovery-stage instructions surrounding those blocks. Source paths inside the packets are provenance, not permission to fetch outside evidence. Return relevant records intact, including qualifications, statement variants, and SOURCE_IMAGE Arabic/English fields. Use bounded reads that fit the tool output limit and recover any truncated passage before judging it. Scripts may access or copy records and serialize judgments already made; they must not select readings, facets, carriers, or exclusions, or substitute filtered fields for evidence. Earlier records help locate evidence; investigate further contacts as you write.

Earlier findings and exclusions are revisable judgments. Check source facts
against the original evidence, not just an earlier agent's wording. Preserve
every supported reading from the first pass and its inputs, including findings
first developed in scope prose or consolidation. Correct factual mistakes while
preserving supported interpretations. If concrete counterevidence defeats a
claim, briefly explain the correction and its basis in your completion reply;
do not silently remove it or fabricate support. A form restriction may limit
literal meaning without defeating contextual resonance.

## Editorial Contract

- Make each reading's particular evidence, connection to the passage, and
  interpretive change explicit. Recover any supporting link compressed out of
  the first pass. Develop new readings just as fully.
- Improve wording, cadence, order, proportion, and repetition. No sentence is
  verbatim-immutable. Coherence must preserve the reasoning behind every
  reading, not absorb several readings into a general statement.
- Preserve concrete images, pathologies, secondary senses, repeated actions,
  spatial relations, and before/after shifts. Keep the ordinary sense
  recoverable and explain the bridge to each additional reading. Boundaries
  should be brief, specific, and attached where needed.
- Use helpful Turkish level-2 subtitles, for example `## Taşın Hafızası`.
  Do not add generic `# PROSE`, `=== PROSE ===`, or XML wrappers.
- Preserve `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}` at every Arabic
  interpretive anchor. Tags are paragraph-local: repeat the full tag when the
  item does interpretive work again in a new paragraph. Do not substitute plain
  Arabic/transliteration, add QAC IDs, or invent another tag shape.
- Write Turkish prose; translate English analytic terminology. Internal IDs,
  lane names, and QAC coordinates stay out of reader prose.
- Put every non-focus ayah reference beside the interpretation it supports,
  usually in parentheses such as `(29:41)`. List every contributing ayah, such
  as `(29:17, 29:25)` or `(1:6, 1:7)`, rather than intervals or vague phrases
  like "sûrenin ilerleyen yerinde". Cite a host prefatory basmala used as
  context as `(S:0)`; use `(1:1)` when Al-Fatiha 1:1 itself is the source.

Compare the result with the first-pass prose and its inputs. Each supported
reading must retain its explicit evidence, connection, and consequence. Check
new readings to the same standard, Arabic anchors for paragraph-local tags,
and contextual claims for references that actually support their wording.

## Output and Mechanical Validation

Write exactly one nonempty Markdown prose file:

- prose: `_commentary/v7/editorial/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/29_38.prose.editorial.tr.md`

Modify no other files and create no audit artifacts. After writing, run:

```bash
python3 _commentary/v7/validate_prose.py _commentary/v7/editorial/pilot-29-38-p03-fatiha-20260906161918/s029/29_38/29_38.prose.editorial.tr.md
```

For nonzero results, repair the reported mechanical format issues in this file
and rerun, at most twice. These repairs concern tags, braces, placeholders,
wrappers, and Arabic outside tags; they are not a reason to alter findings.
After two cycles, leave the prose in place and report remaining issues. Run any
terminal monitor lifecycle command supplied by the orchestrator; report
`attention` if mechanical issues remain, `completed` only if validation passes.
Do not launch another agent or write a validation report.

<editorial_instructions>
No additional unit-specific instructions.
</editorial_instructions>
