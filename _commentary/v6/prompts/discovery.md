# Commentary v6 scope discovery

You are the **@@LANE@@** scope discoverer for **@@AYAH_REF@@**. Complete this
discovery phase across as many bounded reads and continuations as needed.
Decide what the supplied evidence supports. Do not write polished commentary.

Your working checkpoint is `@@WORK_OUTPUT_PATH@@`. Submit your literal judgments
through `checkpoint` below; the helper preserves progress and earlier records,
saves atomically, and publishes `@@DISCOVERY_OUTPUT_PATH@@` after completion
checks. Do not edit either JSON file directly. The supplied monitor lifecycle
commands are also allowed. Stay available for composition.

## Reading And Checkpoints

The sealed input consists of this instruction file, `@@READING_PLAN_PATH@@`,
and the full evidence snapshot `@@PACKET_PATH@@`. Use this helper:

```text
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ init
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ status
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ state --kind work --pointer /notes --page N
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ read --batch BATCH_ID --page N
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ lookup --pointer /branch_registry/0 --page N
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ checkpoint <<'JSON'
{"notes":[{"batch_id":"BATCH_ID","note":"your observation","source_pointers":["/..."]}]}
JSON
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ complete --batch BATCH_ID
```

- Do not write scripts, helper programs, or parsers that select facets or
  carriers, assign decisions, generate findings or exclusions, or reduce
  evidence. Use the supplied commands and literal JSON. Tool wrappers may invoke
  commands and return their output verbatim; they must not make analytical choices.
- On first use run `init`; after interruption or compaction run `status` and
  reload your checkpoint with `state`. Re-read the focus evidence and source facts needed
  to continue. Resume unfinished work without treating a conversation summary
  as the source of an exact quotation, exclusion, or morphological identity.
- Work on the `next_batch` returned by `status`: read its pages, checkpoint its
  review and useful leads, then run `complete` before starting another batch.
  The helper enforces this order. Earlier batches remain readable; use `lookup`
  for a specific comparison that needs a later source. A batch review can record
  an observation, counter-reading, unresolved contact, or a reason no further
  lead emerged. Keep it concise; no negative essay per record or finding quota.
- Return each evidence, catalog, or state page intact to your model context, one page
  per tool response. Do not filter, project, summarize, or collect pages inside
  code before you have read them. A helper delivery count does not establish
  that your tool wrapper presented the evidence. Reciprocal notes, qualifications,
  and every variant of a facet statement are part of the semantic evidence.
- Pages contain at most 24,000 UTF-8 bytes and identify `page` and `page_count`.
  Request at least 32,000 output tokens on the command tool and its outer wrapper
  (for `functions.exec`, use `// @exec: {"max_output_tokens": 32000}`). Return
  the command output verbatim and check for truncation. A truncated or failed
  response is unread; retrieve it again. Oversized source records are
  split into exact field pieces or explicitly numbered string fragments, and
  may continue across batches. Preserve the unfinished lead until all relevant
  pieces have been inspected.
- Original refs connect records across batches. Use `lookup` whenever a claim
  needs evidence from another batch. Inspect complete relevant records and all
  fragments before deciding the claim. Always consider the whole focus; batch
  boundaries neither restrict possible triggers nor create separate readings.
- Use `lookup` for every later evidence retrieval and `state` for checkpoint
  reloads; do not dump or search packet/work files with ad hoc code or shell
  commands. `state` without `--pointer` pages the complete state. Its
  `state_pointer` locates your work, not source evidence; `state_sha256` identifies
  that snapshot. Finish a multi-page reload before updating it.
- Before completing each batch, save at least one `notes` entry using
  `{"batch_id":"BATCH_ID","note":"specific review","source_pointers":["/..."]}`
  with a pointer to evidence in that batch. Preserve useful observations even
  without a candidate. Additional cross-batch notes may omit `batch_id`.
  `leads` entries use `lead_id`, `note`, `source_pointers`, `status`, `resolution`,
  and `finding_refs`. Status is `open`, `landed`, `closed`, or `unresolved`.
  Preserve earlier leads and record their disposition instead of deleting them.
  Copy an unresolved lead's resolution into the final `friction_notes`.
- `checkpoint` accepts any subset of `notes`, `leads`, `findings`,
  `candidate_decisions`, `cross_batch_review`, `coverage_complete`, and
  `friction_notes`. Notes append (identical retries are harmless); leads,
  findings, and decisions add or replace one complete record by `lead_id`,
  `finding_ref`, or `candidate_id`. Omitted records stay intact. The last three
  fields replace their previous values. To withdraw a draft finding explicitly,
  send `remove_finding_refs`; update its decision/lead links before finishing.

After all batches, read both complete catalogs with `read --catalog branches`
and `read --catalog connections`, using `--page N` for every page. Compare the
whole focus, all available facets and connections, your observations, and open
leads across batches. Seek grounded contacts that no candidate nominated. Reopen
full source records where necessary; a catalog is a navigation/review view.
Checkpoint useful observations and leads between catalog pages as needed too.
Catalog `packet_pointer` fields locate original records; `catalog_pointer`
coordinates describe only the review view and are not evidence citations.
Record what this cross-batch review established or left unresolved in
`cross_batch_review`. Submit the response records below through `checkpoint`
(findings and decisions can be saved separately), set `coverage_complete` to
true, and run:

```text
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ finish
```

Repair any reported checkpoint errors yourself and retry. These checks establish
source accounting; they do not decide whether a semantic reading is convincing.

## Evidence And Discovery

- The sealed evidence snapshot is the complete evidence boundary. All other
  paths inside source records are provenance, not permission to fetch evidence.
- Evidence records contain their full wording and qualifications. Read them in
  bounded chunks; use candidate, support, branch, and ayah IDs to join whole
  records as needed. Repeated wording is one source fact, not independent
  corroboration.
- `context_evidence` supplies the required non-focus Arabic and QAC morphemes.
  Each morpheme array follows `context_morpheme_columns` in order. Check
  `context_evidence_coverage` before assigning a target form or root; missing
  evidence is a qualification, not a verdict against a reading.
  Inspect all candidate, branch, and connection records; retrieve detailed
  context morphology as particular comparisons require it.
- Check `focus_word_alignment` for unresolved analytic units. Their source
  readings remain available, but upstream word numbering does not establish a
  QAC join. Inspect the supplied Arabic and morphology; qualify any uncertain
  carrier without treating a missing join as evidence against the reading.
- Analysis refs and QAC refs have separate identities; use each word candidate's
  `word_alignment` when supplied. Accepted overlaps can describe a whole expression and its component.
  Shared morphemes alone do not make their semantic claims duplicates.
- Candidates are a review docket, not an accepted list, discovery limit, or
  quota. Decide every candidate exactly once. Independently inspect the full
  relevant surface, supports, connections, and available branches for
  uncandidate activations and surprise readings.
- Do not emit an exhaustive negative inventory for every available branch or
  connection. Negative accounting is required only for semantics attached to a
  supplied candidate.
- Availability is not activation. A branch reading requires a real carrier, an
  independent trigger, a mechanism, a changed reading, a reader payoff, and a
  boundary. Another word, root, image, grammatical relation, or act can be the
  trigger. Macro and global context may supply a trigger within that lane.
- `root_ids` on a word-analysis candidate are provenance normalization. They
  identify source/QAC root records but do not nominate or activate a branch.
  `root_branch_options` is the compact index of focus branches under those
  roots. Inspect it specifically for a branch that fits the candidate claim
  and meets an independent word/image/relation in the focus; nominate only a
  branch that actually passes that test.
- `candidate_specific_support_ids` identify the supports that define a
  candidate and therefore control its semantic obligations and lane routing.
  Other `support_ids` remain fully available as shared word or surface evidence,
  but an incidental cross-reference in shared evidence does not turn every
  sibling candidate into a contextual claim.
- `accept` preserves the complete candidate. `narrow` preserves a bounded core
  and explicitly records every omitted candidate branch, branch facet, context
  ref, and semantic obligation. `represented` is only for an exact semantic
  duplicate carried by one named finding. `reject` names the failed edge and
  explicitly accounts for all attached obligations.
- Every item in a candidate's `semantic_obligations` is first-class. This
  includes candidate-specific word/channel evidence as well as HFT
  activation-trace roles, before/after changed readings, and containment; none
  may disappear behind a generic summary.
- A retained candidate context ref counts as landed only when it occurs in a
  branch activation's `carrier_refs` or `trigger_refs`. Merely listing it in
  `context_refs` does not count.
- When `v6_routing.basis` is `focus_only_reader_activation`, assess the supplied
  focus-local mechanism in micro. Do not infer missing wider evidence from its
  legacy source lane, and do not reject the local reading merely because that
  wider evidence was never assembled.
- Every candidate `branch_ref` must either land through an exact activated facet
  or be explicitly excluded. Separately account for any explicitly nominated
  `required_branch_facets`; do not expand this into all available facets. Judge
  each facet on its own evidence: retaining a specialization/extension does not
  imply that the branch's core facet is active.
- `represented` means exact semantic duplication: it cannot exclude any of the
  represented candidate's branches, nominated facets, context, or obligations.
  A `narrow` decision must retain at least one semantic obligation when the
  candidate has any.
- Keep uncertainty and counter-readings visible without ranking them. Source
  trust controls qualification, not automatic acceptance or rejection.

## Lane Boundary

- `micro`: local wording, syntax, morphology, sound, root pressure, and
  whole-ayah cross-root contacts.
- `macro`: what the declared pericope or host-surah context changes. Automatic
  basmala and explicitly added ayat are ordinary non-focus context members.
- `global`: a wider resonance only when a concrete wider trigger returns
  through a focus word, relation, or act and materially changes the reading.

## Lane-Specific Procedure

@@LANE_SPECIFIC_PROCEDURE@@

## Final Discovery Schema

The helper assembles these fields under checkpoint `discovery`, maintaining
`schema_version`, `ayah_ref`, and `lane` automatically:

```json
{
  "schema_version": "@@SCOPE_DISCOVERY_SCHEMA_VERSION@@",
  "ayah_ref": "@@AYAH_REF@@",
  "lane": "@@LANE@@",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["@@LANE@@:stable-key"],
      "branch_exclusions": [
        {"branch_ref": "exact ref", "reason": "specific reason"}
      ],
      "facet_exclusions": [
        {"branch_ref": "exact ref", "facet_id": "F001 or null", "reason": "specific reason"}
      ],
      "context_exclusions": [
        {"context_ref": "S:A", "reason": "specific reason"}
      ],
      "semantic_obligation_exclusions": [
        {"obligation_ref": "exact ref", "reason": "specific reason"}
      ]
    }
  ],
  "findings": [
    {
      "finding_ref": "@@LANE@@:stable-key",
      "origin_candidate_id": "accepted/narrowed candidate ID, or null",
      "represented_candidate_ids": ["exact duplicate candidate ID"],
      "title": "short descriptive title",
      "claim": "bounded interpretive claim",
      "mechanism": "how the cited evidence changes the reading",
      "reader_payoff": "what becomes newly perceptible",
      "containment": "limits, alternatives, and epistemic boundary",
      "epistemic": {
        "status": "grounded | qualified | exploratory",
        "source_trust": ["sorted exact trust labels from cited evidence"],
        "reason": "why this status fits"
      },
      "support_ids": ["exact support ID"],
      "evidence_facts": [
        {
          "support_id": "exact support ID, or null for direct focus/branch/context evidence",
          "source_pointer": "exact source field in support, focus_surface_evidence, branch_registry, or context_evidence",
          "function": "carrier | grammar | trigger | lexical_source | boundary",
          "fact": "concise source-grounded fact needed downstream"
        }
      ],
      "branch_activations": [
        {
          "branch_ref": "exact branch ref",
          "facet_id": "exact facet ID, or null only when unresolved",
          "branch_gloss": "exact packet gloss, or null",
          "facet_statement": "exact packet statement, or null",
          "application_mode": "lexical | intrinsic_cross_root | contextual_resonance | analogical | attributed",
          "carrier_refs": ["exact focus/context occurrence ref"],
          "trigger_refs": ["exact independent grounding ref"],
          "focus_return_refs": ["exact focus word/QAC ref"],
          "carrier": "ordinary/root meaning carried by the cited form",
          "independent_trigger": "the separate activating evidence",
          "activation": "why carrier and trigger make contact",
          "resulting_reading": "the materially changed reading",
          "boundary": "what is not being claimed"
        }
      ],
      "connection_refs": ["exact connection ref"],
      "context_refs": ["S:A"],
      "semantic_obligation_refs": ["exact candidate obligation ref"]
    }
  ],
  "friction_notes": ["unresolved evidence-grounded limitation"]
}
```

Use empty arrays, not placeholders. Finding refs must be unique and begin with
`@@LANE@@:`. Accepted/narrowed candidates own dedicated findings. A represented
candidate points to one exact-duplicate finding. Every cited ID/ref must exist
in the packet. Every branch activation must copy the exact gloss/facet source,
use a valid carrier occurrence, identify a distinct trigger, and return through
a focus-surface ref rather than the whole ayah. Include each non-focus ayah
used by a carrier or trigger in `context_refs`.

For every material grammatical classification, morphological claim, lexical
source, unusual sense, or interpretive boundary used by a finding, add the
smallest useful `evidence_facts` record. Copy exact source wording when it is
already concise; otherwise give a faithful compact statement and identify its
packet support and source pointer. These records let downstream composition
correct an accidental prose misstatement without reopening evidence selection.
Use the packet JSON Pointers returned by the reader for `evidence_facts`.
An obligation `source_pointer` points into its named support, including
when that support's `text` is serialized JSON; it is not permission to read an
external file.

<discovery_policy>
@@DISCOVERY_POLICY_MD@@
</discovery_policy>
