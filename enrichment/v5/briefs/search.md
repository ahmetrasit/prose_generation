# v5 search writer: {FAMILY}, {UNIT_LABEL} ({LANE})

This family's sources are not reliably tied to verses, so you find the material yourself and then write the {FAMILY} literature blocks. Keep {MODEL}, {EFFORT} effort; do not spawn agents or change the task.

**Evidence rule.** Every external attribution comes from a corpus passage you read in this assignment. Training knowledge helps you understand, choose search words and connect; it must not supply findings, positions, quotations, report details or gradings. No web, repository or filesystem search; no other runs, outputs or reference files. The only command you use is:

`python3 -B enrichment/v5/read.py {DIR} <command>`

**1. Read the page.** `input 1` … `input 4`, once each, separately: {UNIT_LABEL}, {PARAGRAPHS} paragraphs with augmentations.

**2. Read the leads.** {LEADS}

**3. Search and read.** `search "WORDS"` (optionally `--source ID`, `--offset N`) lists candidate locators in your roster; `get LOCATOR` reads one (follow `--part` continuations). Search words come from the page, from passages you have read, or from the leads. Work through every substantial finding, not just the target ayah; follow up leads with corpus hits; for each paragraph look for direct witnesses (the actual word or wording), not only thematic parallels. A search hit is not evidence: read the passage. Batch your reading: decide what to open from a result list before opening it, and do not re-open passages you have read.

**4. Write.** Family purpose: {PURPOSE}

Same block rules as every v5 writer: connected Turkish prose per paragraph the material serves; author and work named; actual position, reasons and qualifications; disagreements and preferences preserved; report separate from attributed grading; direct lexical witness separate from thematic parallel; your application of a method separate from the author's analysis. No filler or bullet lists; the frozen prose is not graded.

**Outputs** (only these, in `{DIR}/write-{LANE}/`):

`blocks.jsonl`: `{"id":"{FAMILY}-p01","p":[1],"text":"Turkish prose","sources":["SOURCE_ID"],"evidence":[{"loc":"EXACT_LOCATOR","anchor":"exact phrase of 8+ characters from that passage"}]}`

`ledger.jsonl`: one row per paragraph 1–{PARAGRAPHS}: `{"p":1,"status":"written|no_match","blocks":[…],"open":[]}`. `open` names unresolved leads and gaps.

Stop after the two files. Report block count, leads confirmed, leads not found, and limitations.
