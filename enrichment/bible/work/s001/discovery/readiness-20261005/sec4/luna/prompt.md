Read /Volumes/aro/projects/prose_generation/enrichment/bible/work/s001/discovery/readiness-20261005/sec4/luna/package.md. It holds image section 4 (Rahim ve terbiye: çocuğun evi ve onu kemale erdiren) of the frozen surah commentary of surah 1: the Arabic text of the ayat concerned, the Turkish
commentary written on them, and the whole surah in Arabic.

Find, from the Hebrew Bible, the New Testament, and the Jewish and Christian literature around them (Targum,
Mishnah, Talmud, midrash, pseudepigrapha, Christian apocrypha, Church Fathers, Syriac homilies), every text an
advanced reader of this commentary should have beside it. Judge each text on what it says in its own place, not
on resemblance of a word. Weigh at least:

- paralel: the same figure, scene or story told in the other scripture;
- motif: a shared image, formula, liturgical act or ethical motif without a shared story;
- karsi_anlati: the Qur'an tells it differently, corrects or answers it; the difference is the point;
- soydas: a Hebrew, Aramaic or Syriac cognate of a key word of these ayat and how the other scripture uses it;
- yorum_gelenegi: Jewish or Christian interpretation of a parallel text that changes what the parallel means.

Be exhaustive: every passage that stages the scene or carries the motif, anywhere in those literatures. Preserve
parallel, secondary and contrary readings. A parallel is not a dependence: say what the texts share, not who
borrowed. The explanation names, in English, what the text adds to this commentary.

Write one TSV row per text with exactly six tab-separated fields:

strength	tradition	kind	ref	basis	short_explanation

strength: strong, medium, weak. tradition: tevrat (Hebrew Bible and Jewish literature) or incil (New Testament and
Christian literature). kind: paralel, motif, karsi_anlati, soydas, yorum_gelenegi. ref: for the Hebrew Bible and
the New Testament an edition-qualified OSIS reference, one verse per row, no ranges
(WLC:Gen.22.2, WLC:Ps.1.3, SBLGNT:Matt.6.5; consecutive verses on their own rows).
Use Hebrew WLC numbering for Hebrew Bible candidates and SBLGNT numbering for New Testament candidates;
do not silently transfer English/KJV verse numbers. For other works give the work and its place as a reader
cites it (Targum Jonathan on Genesis 22:2;
Genesis Rabbah 56:1; Berakhot 60b; Ephrem, Hymns on Paradise 5:6; Protevangelium of James 8). basis: the words,
scene or motif that carries the link, in a few words. Strongest first.

Do not write a header row, rank numbers, Markdown, sections or prose outside TSV rows. Save the rows to
/Volumes/aro/projects/prose_generation/enrichment/bible/work/s001/discovery/readiness-20261005/sec4/luna/list.tsv. The saved file, not the chat response, is the deliverable.
