# 1:6 family memory baseline

You are one of nineteen independent family researchers. Your assignment gives your family, research purpose, and output directory. Keep the selected GPT-6 Astra model and max effort. Do not enable Fast, spawn agents, run model scripts, or change your task.

Use learned knowledge only. No web, repository search, corpus retrieval, source checking, dictionary checking, other agents' work, or earlier enrichment outputs. You may read only this brief, your supplied source roster, and the four supplied input files; tools may also write your own output files. Do not inspect helper implementations or survey directories.

The input is the complete frozen Turkish commentary for 1:6, v16 r13 with existing augment9, in 22 numbered paragraphs. Read all four input files before authoring: input-1.txt (1–5), input-2.txt (6–10), input-3.txt (11–16), input-4.txt (17–22). Read each once, in separate calls with 12,000 output tokens; print command output directly. If truncated, retrieve only missing text. Keep connections across the whole page in view. The delivery groups are not independent research scopes.

First identify the substantive findings, including augmentations, secondary relationships within paragraphs, and connections between paragraphs. Maintain this compact map in your working context; no separate inventory essay. Then consider every named work in your family roster against those findings. Corpus IDs are mnemonic source prompts, not evidence that a work was read. Multiple editions or excerpts of one work do not constitute different scholarly positions. If a work is unfamiliar or no relevant position is remembered, record that limitation briefly; never invent its view. You may include another clearly relevant remembered work within your family's remit.

Write a prose block for each paragraph with substantive remembered literature from your family. Each block is a concise, connected Turkish literature review of the actual findings: name the author and work, explain the relevant position and useful reasons or qualifications, and make its relationship to the finding clear. Preserve differences between authors and schools. Capture support, disagreement, expansion, or a changed perspective where remembered, without forcing categories. Distinguish discussion of components from discussion of their complete synthesis. Include secondary findings and additions; do not merely discuss the ayah generally. One to three prose paragraphs often suffice, but material determines length. No filler, intermediate source essays, bullet lists inside blocks, or repeated summaries of the frozen paragraph.

The frozen commentary and its lexical foundation are not being graded, confirmed, corrected, or rewritten. An external author's conflicting view is an attributed position, not your verdict. Translation choices and errors are explicitly within the meal research remit. Do not independently authenticate reports; distinguish remembered reception from remembered grading judgments attributed to their sources.

All attributions in this baseline are memory-based and unverified. Name an exact verse, report number, volume/page, wording, or quotation only if actually remembered; otherwise give a broader work/section pointer or mark the precise recollection uncertain. Do not fabricate precision. No-recall never establishes absence, exhaustive coverage, consensus, or historical novelty. Uncertain useful leads remain clearly labelled. No routine tails about what each source does not prove.

Write final blocks directly to FAMILY_DIRECTORY/blocks.jsonl, one JSON object per block:

{"id":"FAMILY-p01","p":[1],"text":"Connected Turkish prose naming authors, works and relevant positions.","sources":["SOURCE_ID"]}

Use your assigned family prefix for unique IDs. A genuinely shared discussion may use p:[4,9]; its prose must clearly address both paragraphs, and the parent will place it at the first paragraph with a link from the other. Separate blocks are preferred when findings differ. References and uncertain recollections belong naturally in the prose. Do not write empty blocks.

Write a small FAMILY_DIRECTORY/ledger.jsonl containing exactly one row for each of paragraphs 1–22:

{"p":1,"status":"written","blocks":["FAMILY-p01"],"open":[]}

Use status "no_recall" and blocks [] when no substantive relevant position was recalled. Use open only for useful unresolved leads, uncertain source details, or material omissions; do not repeat universal memory caveats. This ledger records the work, not proof that all training data was searched. No matrices, hashes, provenance manifests, extra tracking files, or rendering. Leave the frozen input untouched.

Finish after this assignment. Return your block count, output paths, and material limitations, including unfamiliar roster sources where relevant. Do not claim verified attributions or whole-workflow completion.

Isolation: read only the exact supplied input, brief and your own roster paths. Never read or write any other benchmark lane or another family directory. Your supplied inputs are independent copies; other model outputs are forbidden.
