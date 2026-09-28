# 29:38 — Sol synthesis, Astra prose

The user chose 29:38 for direct comparison with the completed Astra run, and specified Sol for the first stage and
Astra for the second. This is an authorized, controlled development experiment on a known ayah, not a blind
generalization test. The generation briefs remain general: no target answer, named image, desired omissions,
previous target commentary, review or North Star example enters either model's instructions.

Arm: `out-sol-astra-composition-29-38`. Comparison baseline:
`out-astra-blind-29-38/s029/29_38/29_38.reading.tr.md`, SHA-256
`f24993fb6f6cd3801182436cd1dcafa96358cd0a3ff770a11fed3fde894d51a0`.

The underlying evidence is copied byte-for-byte from that baseline arm's frozen sources: focus text and word
notes, window text, dictionary, cited branches, concordance, variants, discovery/QeQ records, inventory and Quran
snapshot. There is no new discovery or QeQ call, manual source curation, new window network or previous-reader
prose. The earlier standalone scope therefore remains. The preservation of broad research is unchanged; the
experiment changes how it becomes a reader's explanation.

Two serial model generations, each once at max effort, each with no inherited conversation:

1. `gpt-6-sol` reads the research and sources, uses logged lookups as needed, and returns connected interpretive
   reasoning plus selections of its supporting evidence. It must perform the integration, not provide a list of
   paragraphs for someone else to connect. It need not account for each unused item or promise future treatment.
2. If the synthesis passes structural/source-key checks, a fresh `gpt-6-astra` reads that completed reasoning,
   the same small core, selected exact sources and material qualifications. It writes prose only. It can retrieve
   any remaining frozen source through the same logged helper. It cannot inspect the baseline or evaluation.

`composition.py` implements a separate experimental path. Existing prompts, source arms, prose, accounts and
acceptance rules are unchanged. The new generic briefs are `prompts/compose.md` and `prompts/write_composition.md`.
The synthesis sees every research record; each annotation is placed beside its finding rather than presented as
an independent prose obligation. The writer initially sees the composed explanation and its selected lexical,
Quranic and concordance evidence. Selected-finding shifts and all recorded contradictions remain visible as
additional qualifications independently of the composer's selection. Full research remains accessible on demand.

Code records all selected and unselected source items in `research.disposition.json`. These are selections and
retained records, not claims of delivery, completeness, deferral to an implemented product, or interpretive quality.
The writer produces no inventory JSON. Semantic omissions are assessed independently after prose exists.
Removing a bookkeeping failure by removing that task is not evidence that the commentary itself improved.

The whole process is the treatment: an extra synthesis call, Sol at that stage, different handover, source
selection and a prose-only writer. Astra remains the final writer. Available evidence is controlled, while actual
retrieval and supplied writer evidence may differ. The comparison cannot isolate a model effect, one prompt line,
or the benefit of extra compute. Provider token usage/billing will be reported only if actually available.

Evaluation is frozen here before either new call and remains outside generation. The primary agent will read the
complete synthesis, new commentary and original commentary; no comparison agent is used. The following checks
are judgments of explanatory contribution, not item quotas or a prescribed outline:

- **Orientation:** the plain sense remains clear, with relevant local context. The reader can follow why each
  development follows the last; headings and paragraph length alone do not establish this.
- **Supported surprise:** preserve the substantive explanatory gain of the earlier shelter/seam/eye-film relation
  to the nearby spider-house, rather than retaining its names or replacing it with a conventional moral. Check
  the wording, activation, actual interaction and consequence for the primary reading. This target-specific
  comparison criterion is evaluation-only and is not supplied to either model.
- **Convergence and emphasis:** meaningful relationships govern the whole reading and receive appropriate space.
  Assess whether secondary developments deepen that understanding or create parallel essays. Record where the
  consequential turns become intelligible; do not mechanically mandate one central image or its paragraph number.
- **Earned scope:** examine what could be removed without losing distinct understanding, alongside what valuable
  understanding was lost. A shorter piece is not automatically better, and a source-record omission is not
  automatically a regression. No 800–1,000 word target or universal word cap is imposed.
- **Grounding:** quotations and declared sources pass the existing exact checks; counts have the right scope;
  morphology, gloss and transliteration support the actual explanation. A dictionary grouping does not itself
  prove etymology or the contribution of another form. Containment does not substitute for contribution.
- **QeQ and Turkish losses:** preserve those that change the explanation or the reader's hearing of its words.
  Evidence should serve the developing readings; it should not become a second survey. Look for lost consequential
  distinctions, not preservation of every previous citation or root paragraph.
- **Corrections and limitations:** the original's correction of universal destruction and careless punishment
  assignments must not become false claims in the new text. Omitting an unnecessary excursion need not restate
  every correction to it. Missing previous prose/network remains an honest scope limit.
- **Stage attribution:** identify valuable material lost in Sol's synthesis, material present there but lost in
  Astra's prose, and new problems added by the writer. Review unselected research as evidence, without turning
  archive membership into a requirement to publish it.

If the result is another catalogue, or is shorter by losing the supported surprises, this treatment has failed.
Do not tune its prompts against the result and rerun it automatically. No manual prose repair, account repair,
retry or continuation generation is authorized within this arm. A malformed or failed synthesis blocks writing.
Pre-run validation: 30 offline tests passed, including seven new checks for evidence identity, evaluation exclusion,
selection/retention, compulsory counter-evidence, phase ordering, immutable claims and logged source access.
