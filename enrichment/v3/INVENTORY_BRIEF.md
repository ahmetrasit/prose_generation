# 1:6 finding inventory

Use only the assigned track, this brief and the frozen v16 r13 page with existing augment9. Read all 22 paragraphs and their augmentations once in four separate deliveries, using `python3 -B enrichment/v3/pilot.py prose NUMBERS` with `1,2,3,4,5`, then `6,7,8,9,10`, then `11,12,13,14,15,16`, then `17,18,19,20,21,22`. Each group is under 15,000 characters. Call each separately with 10,000 output tokens; print only the command output, not escaped tool-result JSON. Do not combine the four outputs into one response. If a delivery is truncated, retrieve only its missing paragraphs before writing the inventory; a failed delivery does not count as a successful read. Never silently omit unread input. Do not rerun augmentation, survey the repository, read prior outputs or the other track, inspect helper code or spawn models.

Write the compact inventory directly to the assigned `claims.jsonl`. One row per substantive finding or relationship:

`{"id":"c01","p":[1],"text":"Short neutral Turkish description of the finding."}`

Consider every statement and augmentation, including secondary findings within a paragraph. Repeated findings may share an ID and paragraph list; distinct relationships remain distinct. Preserve the finding's content without expanding it into an essay or copying the prose. Do not add instructions to test its truth, validity, lexical foundation or reasoning. No dictionary checking, factual verification, criticism or confirmation of the frozen prose.

The later research collects literature that supports, conflicts with, expands on, or shifts the perspective on these findings, with source attribution and pointers. Add an optional short `lead` only for a useful remembered external interpretation, report or work; label it unverified. Do not add dictionary-verification leads or search merely to populate this field. No source reads are needed at this stage. Novelty is not decided by the inventory.

Use Standard only, never Fast; keep the selected model and effort. Instructions stay fixed throughout this assignment. If they require a material change, the parent stops and restarts affected work in a fresh context. No ledgers, hashes, manifests or separate coverage report. Return the file path and finding count, plus only a material input limitation if one occurred.
