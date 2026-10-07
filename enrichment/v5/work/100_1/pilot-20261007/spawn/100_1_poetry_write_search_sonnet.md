<!-- agent /root/v5p_100_1_poetry_write_search_sonnet | model claude-sonnet-5-5 | effort high | service default | fast off -->

Working directory: run every command from /Volumes/aro/projects/prose_generation (prefix it with `cd /Volumes/aro/projects/prose_generation && `). Write output files with the Write tool at absolute paths under /Volumes/aro/projects/prose_generation. Use no other files, tools or commands than those the brief names.

# v5 search writer: poetry, 100:1 (search-sonnet)

This family's sources are not reliably tied to verses, so you find the material yourself and then write the poetry literature blocks. Keep claude-sonnet-5-5, high effort; do not spawn agents or change the task.

**Evidence rule.** Every external attribution comes from a corpus passage you read in this assignment. Training knowledge helps you understand, choose search words and connect; it must not supply findings, positions, quotations, report details or gradings. No web, repository or filesystem search; no other runs, outputs or reference files. The only command you use is:

`python3 -B enrichment/v5/read.py enrichment/v5/work/100_1/pilot-20261007/poetry <command>`

**1. Read the page.** `input 1` … `input 4`, once each, separately: 100:1, 22 paragraphs with augmentations.

**2. Read the leads.** Run `candidates --part 0` and every following part. Each lead is a remembered, unverified item with the corpus passages its search terms hit. Leads are pointers only: confirm by reading the passage; a lead without hits may still be worth one search of your own.

**3. Search and read.** `search "WORDS"` (optionally `--source ID`, `--offset N`) lists candidate locators in your roster; `get LOCATOR` reads one (follow `--part` continuations). Search words come from the page, from passages you have read, or from the leads. Work through every substantial finding, not just the target ayah; follow up leads with corpus hits; for each paragraph look for direct witnesses (the actual word or wording), not only thematic parallels. A search hit is not evidence: read the passage. Batch your reading: decide what to open from a result list before opening it, and do not re-open passages you have read.

**4. Write.** Family purpose: Poetry witnesses: direct lexical attestations for the supplied words and concrete images, with poem or collection attribution and commentator gloss where available. Distinguish direct word evidence from thematic parallels; do not substitute a famous general horse poem for an actual lexical witness. Address all substantial paragraph findings.

Same block rules as every v5 writer: connected Turkish prose per paragraph the material serves; author and work named; actual position, reasons and qualifications; disagreements and preferences preserved; report separate from attributed grading; direct lexical witness separate from thematic parallel; your application of a method separate from the author's analysis. No filler or bullet lists; the frozen prose is not graded.

**Outputs** (only these, in `enrichment/v5/work/100_1/pilot-20261007/poetry/write-search-sonnet/`):

`blocks.jsonl`: `{"id":"poetry-p01","p":[1],"text":"Turkish prose","sources":["SOURCE_ID"],"evidence":[{"loc":"EXACT_LOCATOR","anchor":"exact phrase of 8+ characters from that passage"}]}`

`ledger.jsonl`: one row per paragraph 1–22: `{"p":1,"status":"written|no_match","blocks":[…],"open":[]}`. `open` names unresolved leads and gaps.

Stop after the two files. Report block count, leads confirmed, leads not found, and limitations.
