# Commentary v7 scope discovery

You are the fresh **@@LANE@@** discoverer for **@@AYAH_REF@@**. Discover and
explain readings from the supplied evidence. Write the discovery JSON to
`@@DISCOVERY_OUTPUT_PATH@@`, then remain available for your composition turn.
Modify only that output and run any supplied monitor lifecycle commands.

## Reading Purpose

@@READING_STANDARD@@

## Evidence

The inline packet is the complete evidence boundary. Paths inside source records
are provenance, not permission to fetch other files. Candidate and prior-reader
judgments are nominations, not established facts or discovery limits.

Use the supplied reader for access; do not write scripts, parsers, projections,
or semantic generators. Write your JSON directly with the normal file editor.
The reader returns complete records, including all statement variants and
qualifications. Do not filter its responses. A failed or truncated read must be
recovered before relying on that material. Use one read per tool call and allow
at least 16,000 output tokens for complete record batches.

```bash
python3 _commentary/v7/authoring.py read --prompt @@DISCOVERY_PROMPT_PATH@@ --section candidate_inventory
python3 _commentary/v7/authoring.py read --prompt @@DISCOVERY_PROMPT_PATH@@ --section branch_registry --start 0
python3 _commentary/v7/authoring.py read --prompt @@DISCOVERY_PROMPT_PATH@@ --refs support:EXACT_ID branch:EXACT_ROOT/BRANCH context:S:A
```

Other sections include `focus`, `focus_surface_evidence`,
`focus_word_alignment`, `support_registry`, `connection_registry`,
`context_evidence`, and `context_evidence_coverage`. `next_start` locates the
remaining records; `--count` adjusts a batch. For a long single record use the
reader's exact text windows as directed. Reading has no checkpoint file or
completion gate.

Inspect all actual candidates, available branches, and connections; use complete
support and context records to investigate the contacts they suggest and others
you discover. Focus morphology and alignment remain source evidence. A candidate
with `kind: focus_root_occurrence` is provenance only: inspect it but give it
neither a candidate decision nor a finding merely for existing.

Analysis IDs and QAC IDs are distinct. Use `word_alignment` and
`focus_word_alignment` for joins. Shared morphemes do not make readings duplicates.
An unresolved alignment leaves its source reading available but does not license
an invented carrier. Context morphemes follow `context_morpheme_columns`.

Candidate-specific supports control routing; cross-references in shared word
evidence do not move sibling readings to another lane. Assess a
`focus_only_reader_activation` in micro from its supplied local mechanism.

## Discovery Record

The unit of discovery is a complete explanation, not a headline or a filled
semantic form. Write the actual wording, grammatical relation, attested lexical
item, or context fact; explain its particular contact with this passage; then
develop what changes in the reading. Include uncertainty and a brief boundary
where needed. A citation such as "the context supports this" supplies no fact.

Keep distinct mechanisms explicit even when they support the same conclusion.
Related mechanisms may share one finding if each is fully explained. A lexical
resonance must identify the other attested form or sense and its relationship to
the passage's ordinary wording. An inferred scene belongs in the explanation,
not inside the ordinary gloss of a word. A root match alone proves no reading.

Do not separately reproduce the explanation as claim, mechanism, payoff,
activation, and result. The workflow copies your cited source records in full
for downstream use; you supply the reasoning, not generic source placeholders.
Each `evidence_refs` entry selects a whole record:

- `support:SUPPORT_ID`
- `branch:ROOT_ID/BRANCH_ID`
- `context:S:A`
- `connection:CONNECTION_EVIDENCE_REF` (a `connection_ref` returns all its rows)

Focus wording, morphology, and alignment are attached automatically. Cite every
other record doing substantive work. For an unresolved branch, cite its actual
nomination support and explain the uncertainty rather than inventing a branch.
Source attachment establishes availability; it does not approve a reading.

Use this schema:

```json
{
  "schema_version": "@@SCOPE_DISCOVERY_SCHEMA_VERSION@@",
  "ayah_ref": "@@AYAH_REF@@",
  "lane": "@@LANE@@",
  "candidate_decisions": [
    {
      "candidate_id": "exact packet ID",
      "decision": "accept | narrow | represented | reject",
      "finding_refs": ["@@LANE@@:stable-key"],
      "reason": "specific reason; for narrowing or rejection, explain the omitted readings and failed connections"
    }
  ],
  "findings": [
    {
      "finding_ref": "@@LANE@@:stable-key",
      "title": "short descriptive title",
      "reading": "A self-contained explanation with concrete evidence, connection, interpretive change, and any necessary boundary. Several paragraphs are welcome when the reasoning needs them.",
      "evidence_refs": ["support:EXACT_ID", "branch:EXACT_ROOT/BRANCH", "context:S:A"]
    }
  ],
  "friction_notes": []
}
```

Decide each actual candidate exactly once. `accept` carries its complete reading;
`narrow` explicitly explains every omitted branch, nominated facet, context
contribution, and semantic obligation in its reason. `represented` is only for
the same evidence, connection, and consequence already fully explained in a
named finding. `reject` identifies the failed connections and has no finding
refs. New findings need no candidate. Do not create a negative inventory of
uncandidate possibilities. Use exact IDs and no placeholders.

## Lane Procedure

@@LANE_SPECIFIC_PROCEDURE@@

<discovery_policy>
@@DISCOVERY_POLICY_MD@@
</discovery_policy>

<lane_packet_json>
@@LANE_PACKET_JSON@@
</lane_packet_json>
