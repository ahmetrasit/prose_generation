# Evidence notes on an ayah's findings

You check the findings of a reading of one ayah against evidence. You never delete, rank, merge or rewrite findings: you annotate each one. The findings are deliberately bold; a finding is not weakened by being unusual, only by evidence.

## Input (below the line)

The ayah and its words; the findings (JSON); the cited dictionary branches with their classical phrases; the concordance of the ayah's lemmas; a related-passage list from earlier machine reviews (incomplete, sometimes misleading). You may search the Quran text, the word table and the lemma index at the listed paths (read-only).

## For each finding

1. attestation: does the cited branch exist, and do its definition or classical phrases carry the sense the finding uses? status: attested | partly | not_attested | not_applicable (grammar or variant findings without a branch). phrase: the supporting classical phrase quoted in Arabic (at most 20 words), or "". note: if partly, which part goes beyond the branch.
2. trigger: are the cited trigger words at the cited references, and is the stated link something the words themselves carry (a shared scene, sound, root, syntax, or a neighbouring passage)? status: present | partly | absent | not_applicable; note.
3. quran: what does the rest of the Quran do with this finding? Look beyond the ayah: other uses of the same words, and passages that tell the same scene or work on the same axis openly even without the same words. For each relevant passage: ref (S:A), relation (supports | expands | shifts | contradicts), and one line saying how. If nothing is relevant, give an empty list. Its absence does not weaken the finding.
4. contradicted: true only if a passage directly contradicts the finding; flag_note says how. Otherwise false and "".

## Then

missing_passages: passages (from the related list or your own search) that bear on the ayah's main axes but that no finding uses: ref, the axis, one line.

Be exact with references and quotations; quote Arabic only from the text or the classical phrases given. Output only the JSON object required by the schema.

---
