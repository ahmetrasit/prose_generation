# grup, stage 2: place every line on one page

Below is one page of a frozen Turkish commentary (the "şerh"), with its prose paragraphs numbered [¶n], and every
line the source groups extracted for this page: one position each, with its pointers (k) and holders (a). The
reader will see, after each paragraph, the points the sources discuss there. Your job is placement and grouping,
not writing: you never change a line's sentence, pointers or holders.

Write yer.jsonl, one JSON line for EVERY input line, exactly once:
- `{"id":"<input id>","p":<n>}`: the paragraph the line speaks to (the one whose subject, word or claim it
  concerns; when several do, the first). A line about the ayah or surah in general goes after the paragraph that
  introduces that subject. Optional: `"kat":"temel|ek|arastirma"` (temel: what an advanced reader should see first
  here; arastirma: technical detail; default ek), `"f":"destek|oncul|itiraz|…"` when the line's function against
  THIS paragraph differs from its own f (destek: supports the paragraph's reading; oncul: a source already states
  the paragraph's own finding, then also `"guc"`; itiraz: argues the paragraph's reading cannot hold, then
  also `"gerekce"`: the argument, in a few Turkish words).
- Same position, several lines: give them one cluster `"c":"<short name>"` and mark exactly one `"rep":true`: the
  clearest sentence, kept as it is; the script adds every member's pointers and holders to it. Cluster only lines
  that state the same position for the same reason; two holders who differ in reason, scope or wording that
  matters stay separate lines.
- `{"id":"<input id>","elenen":"<reason>"}`: only for a line that belongs to no paragraph of this page (e.g. it
  concerns another ayah) or repeats another line word for word without adding a pointer. Say which.

Then bos.jsonl: for each paragraph claim of the commentary that no line touches (a lexical image, a resonance, a
synthesis of its own), `{"p":<n>,"iddia":"<the claim in a few Turkish words>"}`. These go to the antecedent search.

Run the check from the job header and fix every FAIL. Reply with one line: written.
