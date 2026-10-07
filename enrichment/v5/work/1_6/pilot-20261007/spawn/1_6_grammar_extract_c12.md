<!-- agent /root/v5p_1_6_grammar_extract_c12 | model gpt-6-luna | effort max | service default | fast off -->

# TASK: verbatim extraction — grammar, 1:6, chunk 12 of 31

## ROLE
You copy source passages. You do not write commentary. Model gpt-6-luna, effort max. Do not spawn agents. Do not change the task.

## THE ONLY COMMAND YOU MAY RUN
`python3 -B enrichment/v5/read.py enrichment/v5/work/1_6/pilot-20261007/grammar <subcommand>`

| Subcommand | What it does |
|---|---|
| `input N` (N = 1, 2, 3, 4) | prints part N of the commentary page |
| `chunk 12 --part K` (K = 0, 1, 2, …) | prints delivery K of your source chunk |
| `selfcheck 12` | checks your two output files and lists every problem |

No other commands. No `--help`. No web, no repository search, no other files, no other runs.

**Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens) and print the output directly. A delivery is at most 10,000 characters, so it arrives whole. If any output still looks cut (a delivery header without its full text, or text ending mid-segment with no `<<continues` line), run that same delivery once more with the 12,000-token setting; never mark text `unreadable` because the display was clipped.

## PROCEDURE — follow in order, each step once

**Step 1.** Run `input 1`, `input 2`, `input 3`, `input 4`, one call each. The page has 22 numbered paragraphs. Note each paragraph's findings in your head. Do not write anything yet.

**Step 2.** Run `chunk 12 --part 0`. Read the header line: it says the last delivery number and `next: K`. Run `--part K` for every K until the header says `next: None`. **Read each delivery exactly once. Never re-run a delivery.**
Each source segment starts with a line `=== SEGMENT <LOCATOR> | source … | verses … | paragraphs … ===`. A segment may continue into the next delivery.

**Step 3.** For every segment, decide: does anything in it bear on any paragraph's findings? (Any paragraph, not only the ones in its header.)
Family purpose: Nahw, maani and gharib: syntax, objects and prepositions, morphology, word order and author-specific glosses that affect the findings. External authors' lexical views may be reported; do not reopen the frozen dictionary analysis.

**Step 4.** Write the two output files (format below) in `enrichment/v5/work/1_6/pilot-20261007/grammar/extract/c12/`, using your file-writing tool.

**Step 5.** Run `selfcheck 12`. If it lists problems, fix the files and run `selfcheck 12` again. Repeat until it prints `OK`.

**Step 6.** Stop. Reply with: number of segments, extracted, not_relevant, unreadable, number of quotes.

## WHAT TO QUOTE
- MUST copy the source's own words exactly: same letters, same order. Do not correct, translate, shorten inside, or add vowels.
- MUST quote enough to carry the point: the position and its reasons; competing views and who holds them; which view the author prefers; transmitters when they matter; grading words the source states; translator or edition names; differing wordings (translations); a poetry line plus the commentator's gloss.
- A long relevant passage: quote all of it. Several quotes from one segment are normal.
- When unsure whether something matters: quote it. The writer can drop it; nobody can recover what you skip.
- A source marked as a translation stays a translation; never present it as the original author's words.

## OUTPUT FILE 1: `extracts.jsonl` — one JSON object per line, one per quote
```
{"loc":"EXACT_LOCATOR","p":[3,7],"kind":"position","quote":"exact source words","note":"one line: what it shows, for which finding"}
```
| Field | Rule |
|---|---|
| `loc` | the locator exactly as in the segment header |
| `p` | list of paragraph numbers (1–22) the quote serves |
| `kind` | one of: `position`, `disagreement`, `preference`, `report`, `grading`, `translation`, `witness`, `context` |
| `quote` | exact words from that segment |
| `note` | one short line in English or Turkish |

## OUTPUT FILE 2: `coverage.jsonl` — exactly one line for EVERY segment in your chunk
```
{"loc":"EXACT_LOCATOR","status":"extracted","note":""}
```
| `status` | Use when |
|---|---|
| `extracted` | you wrote at least one quote from it |
| `not_relevant` | you read it and nothing bears on the page; give a short reason in `note` |
| `unreadable` | the source text itself is broken (OCR or encoding); say what is wrong in `note`. Never use it for text you did not get to see. |

## CHECKLIST BEFORE STOPPING
- [ ] every segment of the chunk has exactly one coverage line
- [ ] every `extracted` segment has at least one quote, and every quoted segment is `extracted`
- [ ] `selfcheck 12` prints `OK`
