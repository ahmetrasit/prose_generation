# Turkish loanword cards

You write short cards on Turkish loanwords of Quranic Arabic words, for a Turkish reader who hears the Quran through these loanwords. The cards are reused wherever the lemma occurs; they describe Turkish usage and must not interpret any verse.

## Input (below the line)

Arabic lemmas, each with its root and the root's dictionary branches (branch | Arabic image | Arabic definition | Turkish gloss).

## Task

For each lemma, decide whether present-day Turkish has one or more common words borrowed from this lemma or its root (words a Turkish reader meets in religious or everyday language, including those used in Turkish Quran translations). If none, give an empty list and a one-line none_reason.

For each loanword:
- word: the Turkish word as written today;
- modern_senses: its senses in present-day Turkish, everyday and religious, most common first;
- drift: how it narrowed, widened, shifted or specialised against the Arabic word;
- reader_hears: what a Turkish reader most likely hears when a translation uses it;
- arabic_keeps: what the Arabic word keeps that the Turkish word does not, each tied to a branch id of the input (branch, note); only from the given branches;
- false_friend: a warning if the Turkish word can mislead, else null.

Rules: descriptive; no verse interpretation; no invented etymologies; if you are unsure of a Turkish usage, leave it out. Return every lemma of the input exactly as given (root and lemma strings unchanged).

Output only the JSON object required by the schema.

---
