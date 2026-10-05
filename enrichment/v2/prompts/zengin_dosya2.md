# zengin (dosya2): the page in about five turns, on a corpus extract — overrides the two briefs above where they differ

Everything in common.md and zengin.md holds, except the rules below, which override them where they differ.

Why: every tool result and every thought stays in your context and is read again on every later turn, so the cost
of the page is the number of turns times the size of the context. This page is written in about five turns.

The job header lists your corpus EXTRACT (extract.N.md), built by script: every corpus segment tied to this ayah
(ranges included), sources ranked in zengin.md Step 3's order (short editions before -FULL), each source shown up to
5,000 characters. A segment cut there says how to get the rest (`corpus.py get LOC --from N`); segments past the
extract's budget are listed at its end by locator and size. Meals, translations and the Qur'an text are in the pack.

## The turns
T1. One message of parallel Reads: the numbered base, words.md, dictionary.md, meals.md, turkish.md,
    errata_candidates.json, SCHEMA_CARD.md and every extract file. Not sources.md (the extract replaces it).
T2. Work out Steps 2–5 (claims, research, antecedents and counter-evidence, meal review) from what you read. Then
    send, in ONE message, every lookup you need as parallel calls (at most 30): `get` for the rest of a cut segment
    (`--from`) or a listed one; `search` for antecedents across the Qur'an (Step 4), sahih hadith (`--sahih`), the
    wujūh and maʿānī works; `get MEAL-X:S:A` for a translator's renderings at other occurrences; Reads of usage.md
    or roots/ files if the meal review or the lexicon needs them. corpus.py prints at most 20,000 characters per
    call: put several locators in one `get`. One further round only if a result makes it necessary.
T3, T4. Write the records directly as JSON lines in two parts, annotations.1.jsonl and annotations.2.jsonl (one
    Write each, about half the page each, in page order). Never through a program you write. Do not write
    annotations.jsonl itself: the finish step joins the parts.
T5. Run the Check command of the job header once. Fix only what it names — FAIL (the record would be dropped),
    QUOTE (an Arabic stretch of your metin that none of the record's cited segments holds), MAP (placement) — by
    rewriting the part that holds it. Write gaps.json as zengin.md says, plus "unread_sources": the extract's
    listed or cut sources you did not use, each with a short reason.

## Caps are never silent
A file the job header gives with line ranges is read in those ranges. A Read that shows a "PARTIAL view" banner, or a corpus.py cut ("[cut: …]", "NOTE: … not shown"), is either continued or named in gaps.json with the reason; the finish step audits your transcript for every cap and records what you did not see.

## Not allowed
The pipeline's code (validate.py, render.py, enrich.py, tools/), other call directories, out/, files the harness
saved a tool result to, redirecting corpus output to files, raising corpus.py's --limit, the validator and the
renderer (the check replaces them).
