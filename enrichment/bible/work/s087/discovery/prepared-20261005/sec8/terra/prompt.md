Read /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/discovery/prepared-20261005/sec8/terra/package.md. It holds image section 8 (Uzaktan görülen ateş) of the frozen surah commentary of surah 87: the Arabic text of the ayat concerned, the Turkish
commentary written on them, the words/roots/branch labels recorded in the frozen surah commentary, and the
whole surah in Arabic. The selected commentary defines your scope; the other inputs supply context.

Find, from the Hebrew Bible, the New Testament, and the Jewish and Christian literature around them (Targum,
Mishnah, Talmud, midrash, pseudepigrapha, Christian apocrypha, Church Fathers, Syriac homilies), every text an
advanced reader of this commentary should have beside it. Judge each text on what it says in its own place, not
on resemblance of a word. Weigh at least:

- paralel: the same figure, scene or story told in the other scripture;
- motif: a shared image, formula, liturgical act or ethical motif without a shared story;
- karsi_anlati: the Qur'an tells it differently, corrects or answers it; the difference is the point;
- soydas: a Hebrew, Aramaic or Syriac cognate of a key word of these ayat and how the other scripture uses it;
- yorum_gelenegi: Jewish or Christian interpretation of a parallel text that changes what the parallel means.

Before grading, work through every distinct scene, object, action, relation, formula and secondary sense
actually developed in the commentary, including its augment9 additions. Recall direct formulations, repeated
occurrences, nonlexical parallels, relevant reversals and interpretive traditions. Do not let the title, first
scene or already quoted passages stand in for the whole page. For a Buluşmalar section, consider the particular
meetings between images its prose develops. Root/branch labels are not dictionary definitions, evidence of
cognacy or permission to import an undeveloped sense. Do this review internally; output only candidate rows.

Every explanation must identify a particular detail or claim in the commentary, the corresponding detail in
the candidate's own context, and what the relationship adds. Shared vocabulary, a broad religious theme or
the same speaker alone is insufficient. Do not invent imagery that neither text supports. A shared word is
not required. Preserve indirect, secondary and contrary readings with a concrete connection; do not choose
one preferred reading. A parallel is not a dependence: say what the texts share, not who borrowed.

Check the speaker, addressee, action, negation and verse boundary in remembered context. Name a neighbouring
verse separately when its own contribution is necessary; proximity alone does not qualify it. Keep Hebrew,
Aramaic, Syriac and Greek quotations short and specific to the cited passage and witness. If exact wording or
numbering is uncertain, explain the connection and uncertainty in English instead of reconstructing a quote.
Label roots, dictionary forms and wording from the source commentary explicitly. Never combine verses into
one quotation. Distinguish WLC's written/ketiv stream from qere and other readings; name another witness when
you rely on it. Discovery is memory-only: the later verifier will open the actual texts and check your claims.

Include every candidate meeting this standard. There is no target list length. Strong means a direct,
specific correspondence, including a secondary feature developed in the prose. Medium means a specific
correspondence with an explicit interpretive bridge. Weak means a plausible, specific connection whose
uncertainty you identify; it still cannot be generic. Counter-narrative is a relationship kind, not weaker
confidence. Model agreement and a follow-up origin never make a claim verified.

Write one TSV row per distinct connection with exactly six tab-separated fields:

strength	tradition	kind	ref	basis	short_explanation

strength: strong, medium, weak. tradition: tevrat (Hebrew Bible and Jewish literature) or incil (New Testament and
Christian literature). kind: paralel, motif, karsi_anlati, soydas, yorum_gelenegi. ref: for the Hebrew Bible and
the New Testament an edition-qualified OSIS reference, one verse per row, no ranges
(WLC:Gen.22.2, WLC:Ps.1.3, SBLGNT:Matt.6.5; consecutive verses on their own rows).
Use Hebrew WLC numbering for Hebrew Bible candidates and SBLGNT numbering for New Testament candidates;
do not silently transfer English/KJV verse numbers. For other works give the work and its place as a reader
cites it (Targum Jonathan on Genesis 22:2;
Genesis Rabbah 56:1; Berakhot 60b; Ephrem, Hymns on Paradise 5:6; Protevangelium of James 8). basis: the words,
scene or motif that carries the link, in a few words. Strongest first. Keep distinct reasons or link kinds for
one passage in separate rows; exact repeated connections are unnecessary. Do not regrade an existing row.
The handoff groups references but preserves each distinct connection for an individual verdict.

Do not write a header row, rank numbers, Markdown, sections or prose outside TSV rows. Save the rows to
/Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/discovery/prepared-20261005/sec8/terra/list.tsv. End nonempty files with a newline. Zero qualifying candidates means an explicitly created
empty file. The saved file, not the chat response, is the deliverable.
