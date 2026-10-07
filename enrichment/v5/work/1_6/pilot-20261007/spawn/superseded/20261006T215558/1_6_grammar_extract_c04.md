<!-- agent /root/v5p_1_6_grammar_extract_c04 | model gpt-6-luna | effort max | service default | fast off -->

# v5 extractor: grammar, 1:6, chunk 4 of 8

You read one chunk of a source packet in full and quote, verbatim, everything in it that a later writer needs. You do not write commentary. Keep gpt-6-luna, max effort; do not spawn agents or change the task.

**Evidence rule.** The packet is the only evidence. Training knowledge helps you understand the language; it must not add positions, quotations, report details or translator wording. No web, repository or filesystem search; no other runs, outputs or reference files. The only command you use is:

`python3 -B enrichment/v5/read.py enrichment/v5/work/1_6/pilot-20261007/grammar <command>`

**1. Read the page.** `input 1` … `input 4`, once each, in separate calls. This is the frozen Turkish commentary on 1:6: 22 numbered paragraphs, including augmentations. Note each paragraph's findings, secondary relations and cross-references internally; no inventory essay.

**2. Read your chunk completely.** `chunk 4 --part 0`, then every `--part` the delivery header names, until `next: None`. Each segment opens with a header: locator, source, heading, the verses it was gathered for and the paragraphs those verses come from. A segment may run across deliveries.

**3. Extract.** For each segment, decide what bears on any paragraph's findings (not only the paragraphs in the header). Family purpose: Nahw, maani and gharib: syntax, objects and prepositions, morphology, word order and author-specific glosses that affect the findings. External authors' lexical views may be reported; do not reopen the frozen dictionary analysis.

Quote the source's own words, copied exactly, long enough to carry the point: the author's position and reasons, competing views and who holds them, which view the author prefers, transmitters and chains when they matter, grading statements the source attributes, edition or translator identity, wording differences (meal), lexical witnesses with the commentator's gloss (poetry). Several quotes from one segment are normal. Never summarise in place of quoting; never repair OCR; keep footnote markers. If a relevant passage is long, quote all of it rather than trimming it to a phrase. If unsure whether something matters, extract it — the writer can discard; it cannot recover what you skip.

Translations: a source flagged as a translation is quoted as the translation; its wording is not the author's original.

**Outputs** (write only these two files, in `enrichment/v5/work/1_6/pilot-20261007/grammar/extract/c04/`):

`extracts.jsonl`, one object per quote:
`{"loc":"EXACT_LOCATOR","p":[3,7],"kind":"position|disagreement|preference|report|grading|translation|witness|context","quote":"verbatim text from the segment","note":"one line: what this shows and for which finding"}`

`coverage.jsonl`, exactly one row for every segment in the chunk, in order:
`{"loc":"EXACT_LOCATOR","status":"extracted|not_relevant|unreadable","note":"short reason when not extracted"}`

`p` lists the paragraphs the quote serves. `unreadable` is for OCR or encoding that prevents reading; say what is wrong. `not_relevant` means you read it and nothing in it bears on the page. The parent checks that every quote occurs in its segment and that every segment has a coverage row.

Stop after the two files. Report counts and any unreadable or doubtful segments.
