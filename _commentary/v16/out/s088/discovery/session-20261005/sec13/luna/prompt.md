Read /Volumes/aro/projects/prose_generation/_commentary/v16/out/s088/discovery/session-20261005/sec13/luna/package.md. It holds one image section of a Turkish commentary on
surah 88 ("Hatırlatıcı, gözetmen değil"): the section's prose, the ayat of the
surah it rests on with their Arabic, the roots and words it names, and the
whole surah in Arabic.

Find, from the whole Quran, every ayah outside surah 88 that this image
activates: an ayah a reader of this section should have before them. Judge each
ayah on what it says there, in its own context, not on retrieval similarity.
Weigh at least:

- scene: the same scene, object or act is staged, with or without a shared
  word (the cloud and the pasture, the flood and its foam, the herd and its
  herdsman, the arrows of the lot, the womb, the cracked field, the brand on
  the hide, a fire seen from afar, what is neither dead nor alive, height and
  the lowly life, and whatever this section's image is);
- root: the roots and words the section names, used in the same sense; and in
  a different sense, when the difference matters for this image;
- theme: what the image makes perceptible (what passes and what remains, what
  is provided and what is hidden, what is made fit and what is measured, …)
  stated in other words;
- speaker: the same speaker, addressee or stance (a command to glorify, a
  promise of ease, a reminder for the one who fears, a people preferring the
  nearer life);
- contrast: the same scene or object carrying the opposite, or a boundary;
- neighbour: the ayat next to a passage you name, when the scene continues
  there.

Before grading candidates, work through every distinct scene, object, action,
relation, and secondary dictionary sense actually developed in the section.
For each, recall direct formulations, repeated occurrences elsewhere,
nonlexical parallels, and relevant reversals. Do not let the title, the first
scene, or the ayat already quoted stand in for the whole section. The same
ayah may qualify for more than one image, for different stated reasons. For
a Buluşmalar section, also consider the particular meetings between images
that its prose develops. Do this review internally; output only the TSV rows.

Search exhaustively for connections specific to this image. Scene, root,
theme, speaker, contrast, and neighbour are ways to discover candidates;
each candidate still needs a concrete connection.

For every included ayah, identify the particular detail or claim in this
section, the corresponding detail in the ayah's own context, and what their
relationship adds to the reader's understanding. Put this connection in
short_explanation, in English, with the Arabic word where a word carries
the link. Keep Arabic quotations short and quote only words you remember as
belonging to the cited ayah. If exact wording is uncertain, explain the
connection in English instead of reconstructing a quotation. Explicitly label
a root, dictionary form, or wording from the source section as such. Never
combine words from different ayat into one quotation; mark omitted words.
Check the speaker, action, negation, and ayah boundary in your remembered
context. If a neighbour is needed to complete the claim, name that ayah and
describe the cited row's own contribution separately.

Shared vocabulary, a broad religious theme, or the same speaker alone is
insufficient. Do not introduce imagery into your explanation that neither
passage supports. Preserve indirect, parallel, secondary, and contrary
readings when you can state their specific connection; do not pick one
preferred meaning. A shared word is not required. The whole surah supplies
context; the selected image defines the scope.

Include every candidate meeting this standard. There is no target list
length. For a neighbour, name the linked ayah and explain what the neighbour
completes; proximity alone does not qualify it or make it strong.

Examples of the inclusion boundary for an image about a guide, the middle
of the way, and losing the way (these are examples, not automatic candidates
for other images):
- Include 2:108: ضَلَّ سَوَاءَ السَّبِيلِ directly connects losing the way
  to the section's middle-of-the-way detail.
- Do not include 103:1 on the explanation that time measures "the repeated
  ground on which the path is walked": that explanation invents a path
  connection around the oath by time.

Write one TSV row per ayah with exactly four tab-separated fields:

strength	ayah_ref	basis	short_explanation

Use only these strength labels:
- strong: a direct, specific correspondence to an identifiable feature of this
  image, including a secondary feature actually developed in the prose;
- medium: a specific correspondence whose interpretive bridge you can state
  explicitly;
- weak: a plausible, specific correspondence whose uncertainty you identify
  explicitly; uncertainty does not excuse a generic connection;
- contrast: a specific reversal or boundary that illuminates the image.

Contrast describes the kind of relationship, not a lower confidence level.
Use it when the principal link is a reversal or boundary; explain any
uncertainty in the note. Whenever an otherwise graded row also makes a
contrast, include contrast among its bases. Neither model agreement nor a
follow-up origin makes a candidate stronger.

Even a weak candidate must meet the inclusion standard. Use only these
bases, joined by + when several hold: scene, root, theme, speaker, contrast,
neighbour. Write the ayah reference as canonical surah:ayah, one ayah per row,
no ranges: consecutive ayat get their own rows. Strongest first.

Do not write a header row, rank numbers, Markdown, sections, commentary or
prose outside TSV rows. Do not list ayat of surah 88 itself.

Save the rows to /Volumes/aro/projects/prose_generation/_commentary/v16/out/s088/discovery/session-20261005/sec13/luna/list.tsv. The saved file, not the chat response, is
the deliverable.
