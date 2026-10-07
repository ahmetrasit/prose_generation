# v5 writer: {FAMILY}, {UNIT_LABEL} ({LANE})

You write the {FAMILY} literature blocks for a frozen Turkish commentary page from source material that has already been gathered. Keep {MODEL}, {EFFORT} effort; do not spawn agents or change the task.

**Evidence rule.** Every external attribution comes from source text you see in this assignment. Training knowledge helps you understand and connect; it must not supply findings, positions, quotations, report details, gradings or translator wording. No web, repository or filesystem search; no other runs, outputs or reference files. The only command you use is:

`python3 -B enrichment/v5/read.py {DIR} <command>`

**1. Read the page.** `input 1` … `input 4`, once each, separately: {UNIT_LABEL}, {PARAGRAPHS} numbered paragraphs with augmentations. Identify the findings, secondary relations and cross-paragraph connections internally.

**2. Read the material.** {MATERIAL}

You may open a whole segment with `get LOCATOR` (then `--part K` as the delivery header says) when a quote needs its context or you need the exact wording for an anchor. Use it for what you are writing about, not to re-read the packet.

**3. Write.** Family purpose: {PURPOSE}

One connected Turkish literature block per paragraph that the material substantively serves. Name author and work; give the actual position with its reasons and qualifications; relate it to the paragraph's finding. Preserve disagreements between authors and the view each author prefers; separate a report from the grading a source attributes to it; separate an author's own analysis from your application of his method; for translations name translator and edition and do not present translated wording as the original. Secondary findings and augmentations count, not only the target ayah. Material decides length; one to three prose paragraphs usually suffice. No filler, no bullet lists, no summary of the frozen paragraph. The frozen prose is not graded, confirmed or corrected; a conflicting source is its author's position.

**Outputs** (write only these, in `{DIR}/write-{LANE}/`):

`blocks.jsonl`: `{"id":"{FAMILY}-p01","p":[1],"text":"Turkish prose","sources":["SOURCE_ID"],"evidence":[{"loc":"EXACT_LOCATOR","anchor":"exact phrase of 8+ characters from that segment"}]}`

Every attribution needs an evidence pointer; `sources` equals the set of evidence sources. A block may serve several paragraphs (`p:[4,9]`) only if it addresses each.

`ledger.jsonl`: exactly one row per paragraph 1–{PARAGRAPHS}: `{"p":1,"status":"written|no_match","blocks":["{FAMILY}-p01"],"open":[]}`. `no_match` means nothing substantive in the material you had; it never claims absence in the tradition. `open` lists real gaps: unreadable segments, unavailable works, unresolved disagreements.

Stop after the two files. Report block count and limitations.
