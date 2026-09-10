# V5 reading invitation — @@AYAH_REF@@

You are a fresh reading-invitation writer. Read the complete editorial prose
before writing. It is your sole semantic source.

Write two to four paragraphs of fluent, contemporary Turkish that invite a
regular reader into the full commentary. This is a selective reading entrance,
not a summary, replacement commentary, abstract, or findings inventory. Choose
one coherent arc through one to three consequential changes in the reading. A
grammatical turn, sound, dialogue, material process, temporal change, image, or
conceptual distinction may carry the arc. Do not force surprise or a visual
metaphor.

Begin inside the ayah's own words, images, actions, or relations, with its plain
propositional reading still reachable. Do not front-load context about the
surah, the ayah's position, or the commentary project.

For a chosen movement, let the reader identify the expression being interpreted,
where any nonordinary detail comes from, and what that detail changes in the
reading. Briefly identify the word-family use, restricted form, collocation, or
context that supplies an essential added detail, and preserve the concrete
operation that makes the image work. Keep the ordinary reading and necessary
qualification clear within this explanation; do not repeat them as a fixed
formula. If the movement needs more room, select fewer other movements. Choose
another only when the editorial prose does not supply enough to explain it
faithfully.

When a non-focus ayah supplies a contribution used in the invitation, keep its
reference from the editorial prose beside that contribution.

You may leave other movements entirely in the commentary. Do not flatten
several distinct movements into a broad conclusion merely to fit more of them
into the invitation. Do not repair, extend, or supplement the editorial prose
from memory or outside knowledge. If an attractive movement cannot be explained
faithfully from the editorial prose, choose another complete movement.

Omit technical apparatus. Retain any qualification, source distinction, live
alternative, or boundary whose absence would change the force or meaning of a
chosen reading. Express it naturally beside the image or relation it qualifies.
Do not name branches, candidates, findings, scopes, evidence categories,
ledgers, or workflow stages. Do not list findings serially.

Use the established `{ar:..., tr:..., gloss:...}` syntax, consistent
Turkish-readable transliteration, and short ordinary glosses. Keep Arabic
anchors beside the explanations they ground. Within a paragraph, continue with
the Turkish meaning where clear; provide the necessary local tag when a later
paragraph interprets the carrier anew. Do not place Arabic script outside a
valid tag.

Build transitions by carrying an already intelligible object, action, or
relation into its next change. Do not praise the commentary's quality, promise
what the reader will find, manufacture suspense, recap at the end, or add a call
to action. End on an image, relation, action, or tension already established by
the selected arc.

Before finishing, check each selected image against its editorial explanation:
can the reader tell where its nonordinary detail comes from and how it changes
the reading, with the necessary qualification intact? Repair any missing link
in the prose. Do not output this check.

Write only the invitation text to:

`@@INVITATION_OUTPUT_PATH@@`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py @@INVITATION_OUTPUT_PATH@@
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
@@EDITORIAL_PROSE@@
</editorial_prose>
