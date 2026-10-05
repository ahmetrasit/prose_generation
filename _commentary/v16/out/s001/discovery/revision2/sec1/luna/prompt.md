Read /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision2/sec1/luna/package.md. It holds one image section of a Turkish commentary on
surah 1 ("Çiğnenmiş yol: önden giden kılavuz, yolun ortası, nişanlar ve yolu bulamayan"): the section's prose, the ayat of the
surah it rests on with their Arabic, the roots and words it names, and the
whole surah in Arabic.

Find, from the whole Quran, every ayah outside surah 1 that this image
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

Search exhaustively for connections specific to this image. Scene, root,
theme, speaker, contrast, and neighbour are ways to discover candidates;
each candidate still needs a concrete connection.

For every included ayah, identify the particular detail or claim in this
section, the corresponding detail in the ayah's own context, and what their
relationship adds to the reader's understanding. Put this connection in
short_explanation, in English, with the Arabic word where a word carries
the link. Quote only wording belonging to the cited ayah; distinguish a
root or dictionary form from an ayah quotation.

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
- strong: a direct, specific correspondence central to the image;
- medium: a specific correspondence requiring an explicit interpretive bridge;
- weak: a plausible, specific correspondence with an identified uncertainty;
- contrast: a specific reversal or boundary that illuminates the image.

Even a weak candidate must meet the inclusion standard. Use only these
bases, joined by + when several hold: scene, root, theme, speaker, contrast,
neighbour. Write the ayah reference as canonical surah:ayah, one ayah per row,
no ranges: consecutive ayat get their own rows. Strongest first.

Do not write a header row, rank numbers, Markdown, sections, commentary or
prose outside TSV rows. Do not list ayat of surah 1 itself.

Save the rows to /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision2/sec1/luna/list.tsv. The saved file, not the chat response, is
the deliverable.
