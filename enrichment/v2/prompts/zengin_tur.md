# zengin (tur): turn economy for this page — overrides the two briefs above where they differ

Everything in common.md and zengin.md holds, except the rules below, which override them where they differ (in
particular common.md's "Reading economy": "one file per call" no longer applies).

Why: every tool result and every thought stays in your context and is read again on every later turn, so the cost
of the page is the number of turns times the size of the context. Aim for about 25 turns in all.

1. Parallel calls. Put calls that do not depend on each other in ONE message.
   - Step 1 is one message of parallel Reads: the numbered base, words.md, dictionary.md, meals.md, turkish.md,
     sources.md, errata_candidates.json and SCHEMA_CARD.md (usage.md and roots/ files in the same message if you
     will need them, or in one later message).
   - Step 3 and Step 4 go in rounds of 5–10 parallel corpus calls per message, grouped by category, never one call
     per message. Several locators go into one `get`.
2. Reading budget: about 120k tokens of corpus text in all (about 170,000 Arabic characters). corpus.py prints at
   most 20,000 characters per call and says how to get the rest (`corpus.py get LOC --from N`). Never raise its
   --limit, never redirect its output to a file, never slice files with scripts of your own, and never open a file
   the harness saved a tool result to.
3. What you do not read is recorded, never skipped silently: gaps.json gets "unread_sources", the sources of
   PACK sources.md you did not open, each with a short reason (budget, secondary, repeats X). The finish step also
   lists them from your tool calls and compares.
4. Do not read the pipeline's code (validate.py, render.py, enrich.py, tools/), other call directories or out/:
   the schema card is the format.
5. Write the records directly as JSON lines, never through a program you write: annotations.1.jsonl,
   annotations.2.jsonl … in page order, each with one Write and at most about 25 records (one long write in a
   single turn can outlive the cache's five minutes). Do not write annotations.jsonl itself: the finish step joins
   the parts.
6. Check once, after the last part, with the Check command of the job header. Fix only what it names — FAIL (the
   record would be dropped), QUOTE (an Arabic stretch of your metin that none of the record's cited segments holds),
   MAP (placement; paragraphs with no block) — by rewriting the part that holds it, then check once more. Do not
   run the validator or the renderer and do not read a preview: the check's map replaces Step 7's read-through.
7. gaps.json as zengin.md says, plus "unread_sources".
