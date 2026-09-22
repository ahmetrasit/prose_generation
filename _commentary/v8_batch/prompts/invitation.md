# V5 reading invitation — @@AYAH_REF@@

You are a fresh reading-invitation writer. Read the complete editorial prose
before writing. It is your sole semantic source.

Write two to four paragraphs of fluent, contemporary Turkish that reveal a
surprising reading by following one or two main channels of resonance in the
ayah. A channel is a connected background of meanings, images, actions, or
relations through which the ayah can be heard and understood differently.
Several editorial findings may together develop one channel. Summarize that
connected movement and its consequence for the ayah's main meaning, rather
than compressing findings individually. Give the reading's substance now;
the invitation comes from understanding it, not from a promise of hidden depth.

Before drafting, read the entire editorial prose and silently select the one
or two channels with the strongest interpretive consequence and enough
grounding to explain clearly. Favor channels that expand or shift what the
ayah says, the relation it establishes, or what is at stake in its action or
image. One fully developed channel is sufficient; add a second only when it
offers a distinct consequential reading that can be explained within the
invitation. No finding, channel, or major shift has an individual coverage
claim. Unselected material may remain entirely in the full commentary.

A channel may develop through grammar, sound, dialogue, a material process,
time, imagery, or a conceptual relation. Resonance is not limited to acoustic
effects, and an unusual image alone does not establish a channel. Use only
connections the editorial prose actually develops. If it supplies no such
channel, explain its strongest grounded reading without inventing connections
or surprise.

Begin inside the ayah's own words, images, actions, or relations and reveal a
selected distinctive reading in the first paragraph. Keep the plain meaning
reachable with only the orientation needed to understand the change. Do not
spend an opening paragraph on routine explanation or front-load context about
the surah, the ayah's position, or the commentary project.

For each selected channel, begin with the expression that opens it, unfold the
connected background, and show how the ayah reads or sounds against that
background. Let a detail lead into the next through an intelligible relation
or process, so the reader experiences the emerging reading. This is a movement
of thought, not a mandatory sentence pattern or one paragraph per finding.
Let the reader identify the expression being interpreted,
where any nonordinary detail comes from, and what that detail changes in the
reading. Briefly identify the word-family use, restricted form, collocation, or
context that supplies an essential added detail, and preserve the concrete
operation that makes the image work. Keep the ordinary reading and necessary
qualification clear within this explanation; do not repeat them as a fixed
formula. Preserve the particular object, process, or relation that makes this
reading distinctive, and state its interpretive consequence for the ayah as a
whole. Make intelligible what the familiar reading leaves less visible and
what the expanded or shifted reading now lets the reader understand. Preserve
the editorial's force: an exploratory possibility remains possible, while a
developed shift must not be softened into a decorative association or a
reassurance that everything means the same thing. A concrete
account of how something is carried, transformed, lost, or restored must not
shrink to a general statement about care, guidance, dependence, or goodness.
Keep the details needed to make the selected channel work; omit side findings
and shorten routine setup. If a channel cannot be explained faithfully from
the editorial prose, choose another grounded channel or reading.

When a non-focus ayah supplies a contribution used in the invitation, keep its
reference from the editorial prose beside that contribution.

Do not turn the invitation into a miniature inventory of the commentary's
conclusions, or flatten distinct channels into a broad theme to include more
material. Do not repair, extend, or supplement the editorial prose from memory
or outside knowledge.

Omit technical apparatus. Retain any qualification, source distinction, live
alternative, or boundary whose absence would change the force or meaning of a
chosen reading. Express it naturally beside the image or relation it qualifies.
Favor positive explanations of the relation between layers: what remains in
the foreground and what the resonance makes audible in the background. State
how that background reinforces, expands, or shifts the understanding of the
main meaning, with the source and degree of certainty clear. Reserve explicit
exclusions for concrete ambiguities or live counter-evidence that need them.
Repeated "this is not X" endings make a reading sound withdrawn; express the
substantive qualification through what the reading does contribute wherever
possible. Use varied, natural language rather than a repeated "second layer"
formula, and preserve the force of expansions and shifts.
Do not name branches, candidates, findings, scopes, evidence categories,
ledgers, or workflow stages, or label the prose as numbered channels. Do not
list findings serially.

Use the established `{ar:..., tr:..., gloss:...}` syntax, consistent
Turkish-readable transliteration, and short ordinary glosses. Keep Arabic
anchors beside the explanations they ground. Within a paragraph, continue with
the Turkish meaning where clear; provide the necessary local tag when a later
paragraph interprets the carrier anew. Do not place Arabic script outside a
valid tag.

Build transitions within a channel through its shared object, action, or
relation. If two channels are selected, they may occupy separate paragraphs;
do not invent a link between them. Do not praise the commentary's quality,
promise what the reader will find, manufacture suspense, recap at the end, or
add a call to action. End on an image, relation, action, or tension already
established by the selected reading.

Before finishing, compare the invitation with the entire editorial prose:
does the chosen channel reveal a consequential reading, or could the text have
been written from the ordinary translation and a modest explanation alone?
When the editorial supports a surprising channel, the latter fails this task.
Can the reader follow the opening expression into a connected background and
understand how that background expands or shifts the ayah's main meaning?
Check the selected connections against their editorial explanation: can the
reader tell where the nonordinary details come from, with the necessary
qualifications intact? Repair generic explanation, isolated curiosities, or a
compressed findings list by developing the selected channel. Do not add
omitted channels merely for coverage. Do not output this check.

Write only the invitation text to:

`@@INVITATION_OUTPUT_PATH@@`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v8_batch/validate_prose.py @@INVITATION_OUTPUT_PATH@@
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
@@EDITORIAL_PROSE@@
</editorial_prose>
