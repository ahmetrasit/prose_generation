Read /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/sec4/luna/package.md. It holds one image section of a Turkish commentary on
surah 1 ("Rahim ve terbiye: çocuğun evi ve onu kemale erdiren"): the section's prose, the ayat of the
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

Be exhaustive: every ayah that stages the scene, anywhere in the Quran, and
every ayah that carries the theme in other words. Preserve parallel, secondary
and contrary readings; do not pick one preferred meaning. The explanation
names, in English, what the ayah adds to this image, with the Arabic word
that carries the link where a word is the link.

Write one TSV row per ayah with exactly four tab-separated fields:

strength	ayah_ref	basis	short_explanation

Use only these strength labels: strong, medium, weak, contrast. Use only these
bases, joined by + when several hold: scene, root, theme, speaker, contrast,
neighbour. Write the ayah reference as canonical surah:ayah, one ayah per row,
no ranges: consecutive ayat get their own rows. Strongest first.

Do not write a header row, rank numbers, Markdown, sections, commentary or
prose outside TSV rows. Do not list ayat of surah 1 itself.

Save the rows to /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/sec4/luna/list.tsv. The saved file, not the chat response, is
the deliverable.
