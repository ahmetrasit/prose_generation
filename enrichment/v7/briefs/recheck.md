<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: recheck of digested segments for missed verses, chunk {N} ({SEGMENTS} segments)

## ROLE
Earlier readers took notes on each segment below, for a later writer who builds commentary prose from the notes without rereading the source. Each segment either contains words of the verses listed after `CHECK` in its header, or (marked `number only`) carries that verse's number as a marker such as `(2)` or `[البلد: 2]`; none of its notes is filed under those verses. Your job is to find what the earlier notes missed about those verses, and only that. You do not write commentary. Do not spawn agents. Do not change the task.

## SOURCES IN THIS CHUNK
{SOURCES}

The verses to check, with their text:
{AYAT}

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens).

| Command | What it does |
|---|---|
| `cat enrichment/v7/recheck/{RUN}/chunks/c{NN}.pK.txt` (K = 0 … {LAST}) | prints part K of your chunk (at most 10,000 characters) |
| `python3 -B enrichment/v7/recheck.py check {RUN} --model {TAG} --chunk {N}` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE: follow in order, each step once
**Step 1.** Read parts 0 to {LAST} in order, each exactly once. Each segment starts with `=== SEGMENT <LOCATOR> | source <ID> | indexed … | CHECK <verses> | heading ===`, then its text, then `--- notes already taken on this segment ---` with the earlier notes, and ends with `=== END SEGMENT <LOCATOR> ===`. A segment may continue into the next part. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line at its end), run that same part once more.

A `CORPUS METADATA` line may precede the body. Use its source-quality warnings,
alignment notes and attribution/grade flags as provenance; it is not source wording
and cannot supply an anchor. Each earlier note is one line: the verses it is about,
the verses it mentions, speaker, stance, claim and its exact words in «». They are
comparison material, not a second source.

**Step 2.** For every segment and every verse after its `CHECK`, decide: does the segment say something about this verse that none of the earlier notes carries? See WHAT COUNTS.

**Step 3.** Write the whole output file `enrichment/v7/recheck/{RUN}/out/{TAG}/c{NN}.jsonl` in one write with your file-writing tool, after you have read every part.

**Step 4.** Run the check command. If it lists problems, fix only the lines it names and run it again, until it prints `OK`. Do not stop while it still lists problems, except one: if a problem says a segment's source changed since the build or is no longer in the corpus index, stop and report it (that chunk must be rebuilt; you cannot fix it).

**Step 5.** Stop. Reply with the number of segments and the number of new notes.

## WHAT COUNTS
A segment says something about a verse when it explains, interprets, parses, reads, reports on, or draws a lesson from that verse or its words, as that verse. Then:
- **The point is already in an earlier note** (filed under another verse, or worded differently): write nothing for it.
- **The point is in no earlier note**: write a new note, one per distinct point, in the format below, with the checked verse in `verses`.
- **The verse's words only occur in the segment** (quoted as evidence for a point about another verse, part of a longer quotation, a coincidence of wording, a bare translation or the verse text alone), or **only its number does** (a marker with nothing said about that verse, or a number that is not that verse at all): write nothing.

Most checked verses need nothing. Never repeat a point an earlier note carries, and never record points about other verses.

## OUTPUT: one JSON object per line, one line for EVERY segment, in chunk order
```
{"loc":"EXACT_LOCATOR","rows":[{"verses":["S:A"],"words":["a word of the verse"],"type":"interpretation","speaker":"author","stance":"holds","claim":"one-line paraphrase in English","anchor":"exact words copied from the segment","mentions":[]}]}
{"loc":"EXACT_LOCATOR","rows":[],"none":"short reason, e.g. 90:3 quoted only as evidence for 90:4"}
```
| Field | Rule |
|---|---|
| `loc` | the locator exactly as in the segment header |
| `verses` | the verse(s) the point is about, as `S:A`; at least one must be a verse after this segment's `CHECK` |
| `words` | the word or words of the verse this point is about, copied from the verse text above (a phrase is fine); `["*"]` when the point concerns the whole verse |
| `type` | exactly one of the types below |
| `speaker` | who holds the view, as named in the source and in its own script; `author` for the author's own view |
| `stance` | the author's attitude to the point: `holds`, `prefers`, `reports`, `rejects` |
| `claim` | the point in one English line, at most 40 words |
| `anchor` | 5 to 25 words copied exactly from the segment (same letters, same order; vowel marks may be left out) that carry the point |
| `mentions` | other verses this point quotes or names, as `S:A`; `[]` when none |

Types:
{TYPES}

## CHECKLIST BEFORE STOPPING
- [ ] every segment has exactly one line (`rows` empty with a `none` reason when nothing was missed)
- [ ] every new note is about a verse after its segment's `CHECK`, and no earlier note carries it
- [ ] the check command prints `OK`
