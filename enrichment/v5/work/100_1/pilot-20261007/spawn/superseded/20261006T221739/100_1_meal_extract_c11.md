<!-- agent /root/v5p_100_1_meal_extract_c11 | model gpt-6-luna | effort max | service default | fast off -->

# TASK: verbatim extraction — meal, 100:1, chunk 11 of 11

## ROLE
You copy source passages. You do not write commentary. Model gpt-6-luna, effort max. Do not spawn agents. Do not change the task.

## THE ONLY COMMAND YOU MAY RUN
`python3 -B enrichment/v5/read.py enrichment/v5/work/100_1/pilot-20261007/meal <subcommand>`

| Subcommand | What it does |
|---|---|
| `input N` (N = 1, 2, 3, 4) | prints part N of the commentary page |
| `chunk 11 --part K` (K = 0, 1, 2, …) | prints delivery K of your source chunk |
| `selfcheck 11` | checks your two output files and lists every problem |

No other commands. No `--help`. No web, no repository search, no other files, no other runs.

## PROCEDURE — follow in order, each step once

**Step 1.** Run `input 1`, `input 2`, `input 3`, `input 4`, one call each. The page has 22 numbered paragraphs. Note each paragraph's findings in your head. Do not write anything yet.

**Step 2.** Run `chunk 11 --part 0`. Read the header line: it says the last delivery number and `next: K`. Run `--part K` for every K until the header says `next: None`. **Read each delivery exactly once. Never re-run a delivery.**
Each source segment starts with a line `=== SEGMENT <LOCATOR> | source … | verses … | paragraphs … ===`. A segment may continue into the next delivery.

**Step 3.** For every segment, decide: does anything in it bear on any paragraph's findings? (Any paragraph, not only the ones in its header.)
Family purpose: Turkish translations: wording that narrows or shifts meaning, interpretive additions, omitted distinctions and consistent translation errors supported by repeated examples. Preserve alternatives and edition identities; a defensible tafsir choice is not automatically a translation error. Compare secondary verses where relevant; English originals and Turkish versions are both in scope when supplied.

**Step 4.** Write the two output files (format below) in `enrichment/v5/work/100_1/pilot-20261007/meal/extract/c11/`, using your file-writing tool.

**Step 5.** Run `selfcheck 11`. If it lists problems, fix the files and run `selfcheck 11` again. Repeat until it prints `OK`.

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
| `unreadable` | OCR or encoding prevents reading; say what is wrong in `note` |

## CHECKLIST BEFORE STOPPING
- [ ] every segment of the chunk has exactly one coverage line
- [ ] every `extracted` segment has at least one quote, and every quoted segment is `extracted`
- [ ] `selfcheck 11` prints `OK`
