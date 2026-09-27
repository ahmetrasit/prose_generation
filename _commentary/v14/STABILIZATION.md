# Source and accounting revision

The user agreed to the next v14 stabilization pass and asked whether the problem was the prompt or the model.
The observed spelling failures were caused by input/verifier disagreement; the accounting bloat was permitted by
the output contract. Neither establishes a model limitation. The remaining serial-tour tendency is not causally
isolated: the first v14 comparison changed both model and handover.

New writer arms use contract 2. Existing arms retain their frozen prompts, inputs and response contracts.

## Exact sources

`sources.py` reads the same Quran corpus and normalization functions as the verifier. New concordance clauses and
the local window are mapped to that exact text, preserving counts, word IDs and clause scope. An unresolvable or
ambiguous clause is an error, not an invented replacement. The corpus hash is bound to the prepared experiment.

Two access modes share the same source:

- `--source-mode inline` supplies deduplicated complete ayat for QeQ leads, concordance uses and the local window.
  This works with the existing tool-free Opus runner but adds 50,114 bytes for the current 1:6 packet (175 ayat).
- `--source-mode lookup` freezes the corpus on disk and supplies a lookup command to an external writer with tools.
  The writer retrieves the passages it develops and 0–3 adjacent ayat per side. Each query returns at most 16
  requested references plus neighbours. Requested/returned references and response bytes are logged. The corpus
  itself is not part of the writer input. Tool response bytes are additional input, not free or ignored costs.

Full corpus availability does not prove context was consulted or interpreted correctly. Read the output and lookup
log. Source correctness remains separate from semantic quality. This revision never repairs historical prose.

## Smaller accounting

Schema 2 keeps item dispositions and exact evidence while replacing paragraph copies with one to three short
anchors (20–240 characters each). Each anchor must identify one paragraph unambiguously; a script retrieves the
full paragraph for review. Payoffs are limited to 240 characters. These limits apply only to metadata, not prose,
findings or the number of bundles. Writer self-assessments remain claims pending independent review.

## Controlled repeat

Prepared arm: `out-sol-stable`, 1:6, using the same v2 upstream and full v2 1:5 prose as `out-sol-max`. Initial input:
203,821 bytes, versus 201,665 previously. The repeat uses gpt-6-sol at max, without prior conversation or access to
target baselines/evaluation. The new source access and accounting contract are the experimental changes. This can
test the revised handover with the model held fixed; it does not isolate source retrieval from prompt changes or
prove anything about the comparative ceiling of different models.

The ten frozen passage criteria remain unchanged. Review the full candidate against both original/v2 protected
passages and the first Sol result. Report source errors, semantic losses, bookkeeping bytes and retrieved input;
never trade a lost explanation for lower cost. The previous-context ablation must follow this repeat with the same
new contract and model, so it is not confounded with the source/accounting change. No automatic extra run is used.

Twenty offline tests cover old-account compatibility, exact source mapping, changed corpus detection, bounded
lookup, frozen lookup data kept out of bulk input, short-anchor resolution and ambiguous/oversized anchor rejection,
along with the original immutability, sequential context and regression gates. The repeat is complete; see
STABILIZATION_COMPARISON.md. All 23 tags pass exactly and accounting fell 55%, but the broader review found an
omitted earlier explanation inside a record still claimed connected. The narrow ten-case gate passes; acceptance
is withheld. No response repair or additional generation was made.

Concurrent work advanced live v13 in commits f1465ac9b and 91ce372cc. The baseline audit consequently reports six
changed live source files (DESIGN, HANDOFF, net/qeq/write briefs and run.py), while all copied historical v14 data
still matches the original snapshot. Do not restore the concurrent v13 changes or include its new run outputs in
the v14 commit. This experiment's sources and comparison passages are the frozen v14 copies.
