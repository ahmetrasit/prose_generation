# 1:1 parallel pilot — Sol High, Sol Max, Luna Max — 2026-10-07

Three independent executions of the complete micro-lesson v1 workflow on the same full base commentary: **27 paragraphs**, 57 cited/discussed ayat, and branch/gloss evidence for the six discussed root families. Source selection and evidence locators are in [input/README.md](input/README.md).

- `sol-high/`: gpt-6-sol, reasoning high.
- `sol-max/`: gpt-6-sol, reasoning max.
- `luna-max/`: gpt-6-luna, reasoning max; added at the user’s request while the Sol runs were still working.

Each model performs grammar, semantics, mapping, then assembly sequentially within its own agent context. The complete runs overlap in execution; Luna started later. They share the prepared evidence and workflow, not each other's results. This is a qualitative pilot, not a controlled repeated benchmark; no lesson count target or numeric quality score is imposed.

Each completed folder contains the three engine outputs, assembled `page-output.json`, a readable `lessons.md`, and model-authored `run-notes.md`. Raw engine outputs remain available for assessing assembly decisions.

All three conditions have saved their six deliverables and recorded completion. Read the [Sol comparison](sol-comparison.md), [Sol usage and cost estimates](sol-costs.json), [Luna comparison](luna-comparison.md), and [Luna usage and cost estimates](luna-costs.json). Luna's final completion event is 17:25:11 UTC.

Subsequent editorial work is separate: [Sol Max edited copy](sol-max-edited/README.md)
contains eight targeted lesson corrections and a preparation-reference note. These
are not new model results. The workflow instructions were updated after the pilot;
the original runs therefore do not test those revisions. [Usage and file sizes](usage-and-size.md)
separates cumulative run tokens from stored artifacts.

Recovery note: a server restart interrupted Luna before it saved deliverables. Its existing agent session was resumed at about 16:55 UTC with the original task unchanged; the saved model setting remains gpt-6-luna / max. Sol had already completed. Luna elapsed time and recorded usage must be interpreted with this interruption disclosed.
