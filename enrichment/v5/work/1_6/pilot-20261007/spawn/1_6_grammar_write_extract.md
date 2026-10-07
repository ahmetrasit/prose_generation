<!-- agent /root/v5p_1_6_grammar_write_extract | model gpt-6-sol | effort high | service default | fast off -->

# v5 writer: grammar, 1:6 (extract)

You write the grammar literature blocks for a frozen Turkish commentary page from source material that has already been gathered. Keep gpt-6-sol, high effort; do not spawn agents or change the task.

**Evidence rule.** Every external attribution comes from source text you see in this assignment. Training knowledge helps you understand and connect; it must not supply findings, positions, quotations, report details, gradings or translator wording. No web, repository or filesystem search; no other runs, outputs or reference files. The only command you use is:

`python3 -B enrichment/v5/read.py enrichment/v5/work/1_6/pilot-20261007/grammar <command>`

**1. Read the page.** `input 1` … `input 4`, once each, separately: 1:6, 22 numbered paragraphs with augmentations. Identify the findings, secondary relations and cross-paragraph connections internally.

**2. Read the material.** Run `extracts --part 0` and every following part until `next: None`. These are verbatim quotes, grouped by paragraph, taken by fresh readers from every segment of your packet (1057 segments, about 361,328 tokens); each quote names its locator, kind and what it shows.

You may open a whole segment with `get LOCATOR` (then `--part K` as the delivery header says) when a quote needs its context or you need the exact wording for an anchor. Use it for what you are writing about, not to re-read the packet.

**3. Write.** Family purpose: Nahw, maani and gharib: syntax, objects and prepositions, morphology, word order and author-specific glosses that affect the findings. External authors' lexical views may be reported; do not reopen the frozen dictionary analysis.

One connected Turkish literature block per paragraph that the material substantively serves. Name author and work; give the actual position with its reasons and qualifications; relate it to the paragraph's finding. Preserve disagreements between authors and the view each author prefers; separate a report from the grading a source attributes to it; separate an author's own analysis from your application of his method; for translations name translator and edition and do not present translated wording as the original. Secondary findings and augmentations count, not only the target ayah. Material decides length; one to three prose paragraphs usually suffice. No filler, no bullet lists, no summary of the frozen paragraph. The frozen prose is not graded, confirmed or corrected; a conflicting source is its author's position.

**Outputs** (write only these, in `enrichment/v5/work/1_6/pilot-20261007/grammar/write-extract/`):

`blocks.jsonl`: `{"id":"grammar-p01","p":[1],"text":"Turkish prose","sources":["SOURCE_ID"],"evidence":[{"loc":"EXACT_LOCATOR","anchor":"exact phrase of 8+ characters from that segment"}]}`

Every attribution needs an evidence pointer; `sources` equals the set of evidence sources. A block may serve several paragraphs (`p:[4,9]`) only if it addresses each.

`ledger.jsonl`: exactly one row per paragraph 1–22: `{"p":1,"status":"written|no_match","blocks":["grammar-p01"],"open":[]}`. `no_match` means nothing substantive in the material you had; it never claims absence in the tradition. `open` lists real gaps: unreadable segments, unavailable works, unresolved disagreements.

Stop after the two files. Report block count and limitations.
