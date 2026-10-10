You will add Bible verses to a frozen Turkish commentary on Qur'an {{REF}}. The commentary is below, with its
paragraphs numbered [¶n]. Do not change, summarise or rewrite it.

The goal: each added verse must help the reader understand the paragraph it stands beside, from the Bible's side.
Similarity alone is not the test, and a verse may help without sharing any word. A verse helps when, after reading
it, the reader understands that paragraph's point better than before: it says the same point in its own words, or
says it the other way round so the difference shows what is distinctive here, or shows the world of an image or
practice the paragraph relies on, or shows how the Hebrew or Aramaic relative of a word the paragraph discusses is
used.

Below the commentary is a list of Hebrew Bible and New Testament verses that other readers recalled from memory,
with the paragraph they thought each would help. Each comes with its KJV text and, when available, the Hebrew (WLC)
or Greek (SBLGNT) text at the same reference. The Hebrew numbering sometimes differs from the KJV's; trust the KJV
text for what the verse says. The readers' notes and paragraph numbers are hints, not evidence: read each verse and
each paragraph yourself.

For every listed verse decide one of:

- place: it helps the reader understand a particular paragraph. Give that paragraph (or paragraphs).
- end: it clearly helps the reader understand the ayah as a whole, but no single paragraph. Use this sparingly.
- drop: it does not help. Give the reason in one sentence (only a shared word or theme; a wrong reference whose text
  does not fit; a weaker repeat of a verse you keep; it explains a side detail without making the paragraph's point
  clearer).

The test before you place a verse: say in one sentence what the reader understands about the paragraph's point
after reading it that they did not before. If you cannot, drop it.

Rules:

- Every listed verse appears in exactly one row. Consecutive or closely joined verses that make one point may share
  one row (list them all in `refs`).
- The note is written in Turkish for an advanced reader. Its first sentence is the test sentence: what the verse
  makes clearer about the paragraph's point. Then what the verse says, in its own context, quoted briefly in
  Turkish translation, and where it meets or parts from the paragraph. No source talk, no hedging about dependence.
- `way` is how it helps: same, opposite, background or word.
- You may add a verse that is not listed only if you are sure of it; mark it `"added": true`.
- Do not read files, run commands or search. Everything you need is here.

Reply with JSON Lines only (one object per line, no Markdown):

{"refs": ["Book.C.V", ...], "decision": "place", "paragraphs": [n], "way": "same|opposite|background|word", "note_tr": "..."}
{"refs": ["Book.C.V"], "decision": "end", "way": "...", "note_tr": "..."}
{"refs": ["Book.C.V"], "decision": "drop", "reason": "..."}

=== COMMENTARY ===

{{PROSE}}

=== VERSES ===

{{VERSES}}
