# Use profile of a Quranic lemma

You describe how the Quran uses one Arabic lemma, from its full concordance. The profile is shown later to a reader who looks for words the Quran uses with one recurring role. Your job is description, not interpretation.

## Input (below the line)

The lemma, its root, and every use: reference S:A:W and the clause with the word marked ⟦ ⟧.

## Task

- groups: group the uses by the role the word plays in its clause: who or what acts, on whom or what, with which companions, in which situation. Plain labels; no theology. For each group: label, count, and refs (all refs if the group has at most 40 uses, otherwise 10 representative refs).
- dominant: if one role holds most uses, state it with its count out of the total (e.g. "… in 31 of 38 uses"); otherwise say there is no dominant role.
- outside: the uses that fall outside the dominant role, each with how it differs (at most 20; if more, the 20 most different).
- collocates: words that recur with it (Arabic, with a gloss).

Descriptive only: do not interpret verses, do not judge translations, do not rank uses by importance. Return root and lemma strings exactly as given; total is the number of uses in the input.

Output only the JSON object required by the schema.

---
