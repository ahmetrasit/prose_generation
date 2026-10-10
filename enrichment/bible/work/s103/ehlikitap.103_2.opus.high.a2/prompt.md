# Job

- Surah: 103 (ayat 1–3); ids use S103
- Target: 103:2 — the ayah page of 103:2 (base PACK/numbered/103_2.md; Arabic text in PACK/quran.json); every record's ayet must include 103:2
- Workspace root: /Volumes/aro/projects/prose_generation
- PACK: /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/pack
- Your call directory (write only here): /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2
- Schema card: /Volumes/aro/projects/prose_generation/enrichment/bible/SCHEMA_BIBLE_CARD.md (read it once; the full reference is /Volumes/aro/projects/prose_generation/enrichment/bible/SCHEMA.md)
- Corpus tool: python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py
- Validator: python3 /Volumes/aro/projects/prose_generation/enrichment/bible/validate.py --surah 103 --target 103:2 --annotations /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2/annotations.jsonl --pass ehlikitap
- Renderer (preview): python3 /Volumes/aro/projects/prose_generation/enrichment/bible/render.py --surah 103 --target 103:2 --annotations /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2/annotations.jsonl --out /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2/preview
- Verdict draft check: python3 /Volumes/aro/projects/prose_generation/enrichment/bible/verdicts.py --surah 103 --target 103:2 --annotations /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2/annotations.jsonl --draft --report /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_2.opus.high.a2/verdicts.draft.json
- Hebrew root and cognate tool: python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py root ROOT | cognates 'ARABIC ROOT' | word WLC:Book.C.V
- Deliverables: annotations.jsonl, verdicts.jsonl, gaps.json and root_verdicts.jsonl in your call directory.
- Pass: ehlikitap (the Tevrat and İncil layers; brief ehlikitap.md); corpus tool: python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext (the flag before the subcommand)
- Prefetch: read prefetch.json beside the selected discovery list; record its gaps in your gaps.json.
- Review: read the .merged.json beside the discovery TSV. It preserves wording findings, repeats, repairs and provenance.
- Discovery list: /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/103_2.merged.tsv


# Bible enrichment: working rules

You add evidence from Jewish and Christian texts around a frozen Turkish commentary. Read the numbered base
named in the job header (the frozen r13 commentary, or an augment9 base in packs built before
2026-10-09). Preserve every word of it, including any v16 augment additions it holds. Every annotation names
one paragraph and an exact anchor within it. The script inserts annotations and builds the source registry.

## Inputs and tools
- All working inputs belong to `enrichment/bible/`. PACK in the job header contains `base/`, `numbered/`,
  `base.json`, `quran.json` and `pack.json`. There are no dictionary or word-binding files in this pack.
- Read `enrichment/bible/SCHEMA_BIBLE_CARD.md` completely. Consult its full `SCHEMA.md` only if necessary.
- Read the selected discovery list, its `.merged.json` review sidecar, and adjacent `prefetch.json`. Reader
  grades, reasons and wording flags are unverified. Prefetch gaps are gaps in available evidence. Distinct
  connections under one reference need distinct verdicts; a high grade or reader agreement is not proof.
- Use `python3 enrichment/bible/corpus.py sources`, `get LOC [LOC …]`, `ayah S:A`, or
  `search 'words' --src WLC` / `--src SBLGNT`. Search matches word prefixes after removing Hebrew pointing and
  Greek accents; it is not a morphological or root index. Try inflected forms and inspect the results.
- For roots and lemmas use `python3 enrichment/bible/hebrew.py root ROOT` (every WLC occurrence of a Hebrew or
  Aramaic root, with lexicon entries and BDB notes), `cognates 'ع ص ر'` (the corresponding Hebrew/Aramaic roots of
  an Arabic root) and `word WLC:Book.C.V` (each word of a verse with its lemma, root and gloss). BDB heads keep
  cognate glosses, but this edition shows Arabic or Syriac script only as a placeholder ([Arabic]).
- Use the absolute tool paths in the header. Bible tool commands run one at a time, without shell loops,
  variables, redirection, command substitution or command separators. Read-only shell (`cat`, `head`, `tail`,
  `ls`, `grep`, `wc`, `sed -n`, `python3 -I -c` that only reads JSON or TSV) may be used on your inputs and call
  directory, joined by pipes or `;` but with no redirection. Use the file tools to write your records.
- A helper script (for example one that summarises the discovery list or assembles verdicts.jsonl from your own
  judgement table) goes INSIDE your call directory, written with the file tools, run as `python3 -I SCRIPT`, and
  may name only your inputs and call directory; standard modules such as json, csv, re and collections only.
  Never write anywhere else (no session scratchpad). Your judgements stay yours: a script only formats them.
- Read each input once and retain notes in your call directory. Start searches with `--n 10 --chars 300` and
  lookups with `--chars 1500`; request more context when needed. Every cited passage must actually be opened.
- Save `annotations.jsonl`, `verdicts.jsonl`, `gaps.json` and `root_verdicts.jsonl` in your call directory. The verdict draft command
  checks structure during work; final acceptance also checks the native transcript's actual corpus get results.
- Write only in your call directory. Do not read accepted enrichment pages, other calls, or the Islamic
  enrichment workspace. Do not fetch sources, rebuild packs or indexes, or call models. Report missing texts.

## Evidence and prose
Every `kaynak` uses a locator returned by this corpus. Hebrew WLC and Greek SBLGNT are the primary biblical
texts. English KJV is a finding aid. Identify editions and resolve each edition's own verse numbering.

Memory must be explicit: `kaynak:"hafiza"` (or a source whose access is hafiza) and
`durum:degerlendirilmedi`. It cannot establish a quotation or verify a candidate. Report absent witnesses in
`gaps.json`; do not imply they were searched.

Keep the Qur'anic context, the other text's evidence and the commentary's synthesis distinct. Present parallels
as parallels. Attribute stronger historical claims to named scholarship, observe dating, and retain alternatives.
Report evidence for and against the commentary without choosing among its readings.

Write concise Turkish in the commentary's register: one paragraph, at most 80 words for temel/ek or 120 for
arastirma. Name the text or scholar and explain what the evidence adds at this location. Refer to the commentary
as “şerh” when necessary. No first person, process narration or repeated points. Use the schema's relationship
and status fields; explain a limitation in the prose only when it changes the reading.

## Semitic evidence (Hebrew, Biblical Aramaic and the Arabic roots of the page)
Arabic, Hebrew and Aramaic are sister languages, and their shared roots are evidence in their own right. Use them
both to explain the ayah and to show where the Bible's version differs from what the ayah says:
- The page's Semitic root table lists every Arabic root the frozen text cites, with the Hebrew and Biblical Aramaic
  roots that correspond to it by regular sound correspondences and exist in the lexicon. Work through each one.
- For a corresponding root, look at its semantic range across its Hebrew Bible occurrences (`hebrew.py root`),
  not only one verse: which senses it shares with the Arabic branch the page develops, which it lacks, and
  where the Bible uses it in a scene, formula or image comparable to the ayah's.
- Look for wordplay and paronomasia carried by a root (a Hebrew text that plays on the same consonants the ayah
  or its commentary turns on), for a Biblical Aramaic usage, and for a Hebrew passage whose wording makes the
  Qur'anic difference visible (karsi_anlati).
- Name the basis of every cognate claim: "BDB cites an Arabic cognate" (the lexicon's own note) or "sound
  correspondence only" (unverified by a lexicon), and quote the WLC wording verbatim from the corpus. A shared
  root is evidence of related vocabulary, not of borrowing or dependence; a loan claim needs named scholarship.
- A root may correspond in form and differ in meaning (a false friend): say so rather than force a link. A root
  the table does not list may still be proposed from knowledge, marked as such, and checked in the corpus.

Record one decision per Arabic root of the table in `root_verdicts.jsonl`, one JSON object per line:
{"root":"<the Arabic root as written in the table>","decision":"used","hebrew":["<Hebrew or Aramaic root>"],"reason":"…","paragraphs":[n],"annotations":["<kept annotation id>"]}
`decision` is `used` (it carries at least one kept annotation), `no_qualifying_parallel` (a corresponding root
exists but adds nothing specific here), `false_friend` (same consonants, unrelated sense) or `no_hebrew_cognate`
(nothing corresponds). Every root needs a specific reason; no root may be left without a line.


# ehlikitap: one page's Bible-pass records (Tevrat and İncil layers), in one call

You produce every Bible-pass block for ONE page, the target in the job header: the surah page or one ayah page.
This pass runs apart from the Islamic pass and never reads its records; a script merges the layers afterwards
(after each base paragraph: the Islamic blocks, then tevrat, then incil). You write records, not Markdown: a
script checks each record, drops any that fails a rule (it is not sent back to you), inserts the rest into the
frozen base after the paragraph each names, and builds the source registry.

The Bible working rules (common.md) apply:
- Cite ONLY the Jewish and Christian sources of the intertext index (and the Qur'an
  text, and modern scholarship), never a tafsir, hadith, lexicon or meal. An Islamic source that itself quotes the
  Bible (al-Biqāʿī) belongs to the Islamic pass, not here.
- The corpus tool is `python3 enrichment/bible/corpus.py --intertext …` (the `--intertext` flag before the
  subcommand): sources WLC (Hebrew Bible, Masoretic, locators WLC:Gen.22.2), SBLGNT (Greek New Testament,
  SBLGNT:Matt.6.5), KJV (the English aid, KJV:Gen.22.2; never the text quoted as scripture when the Hebrew or Greek
  is in the corpus), SEFARIA (Targum, Talmud, midrash and classical Jewish commentary fetched for this page,
  SEFARIA:Targum_Jonathan_on_Genesis.22.2), CORPUSCORANICUM-INTERTEXT (Corpus Coranicum's intertext entries for the
  surah's ayat, with the editors' notes and dating). `corpus.py --intertext ayah S:A` lists the Corpus Coranicum
  entries attached to an ayah; `search` works on Hebrew (consonantal and pointed), Greek and English.
- Every block carries `gelenek`: tevrat (Hebrew Bible in any witness, the Psalms included; Jewish pseudepigrapha;
  Mishnah, Talmud, midrash, Targum, classical Jewish commentary) or incil (New Testament in any witness;
  Christian apocrypha; Church Fathers; Syriac homilies). A Hebrew Bible text read through Christian exegesis is two
  blocks: the text (tevrat) and its Christian reading (incil). Each block cites only sources of its own tradition
  (SHARED: the Qur'an text and modern scholarship).
- Every block carries `bag` (what is claimed about the link: benzerlik by default; ortak_havza when both texts draw
  on a Late Antique tradition; muhatap or etki_iddiasi only with a named scholar in `alim`; never a dependence
  claim for a text dated after the Qur'an), `tarihleme` (the other text's dating relative to the Qur'an) and
  `nusha` (the witness or witnesses the block rests on). A parallel is not a dependence: use the weakest fitting
  value.

## Scope by target
- Ayah page (target S:A): every Jewish and Christian text an advanced reader should have beside that ayah: the same
  figure, scene or story told in the other scripture (paralel); a shared image, formula or ethical motif without a
  shared story (motif); where the Qur'an tells it differently, corrects or answers (karsi_anlati: the difference is
  the point); a Hebrew, Aramaic or Syriac cognate of the ayah's word and how the other scripture uses it (soydas:
  loan claims only with named scholarship); Jewish or Christian interpretation of the parallel text (yorum_gelenegi:
  Targum, midrash, Talmud; Church Fathers, Syriac homilies). Every record's `ayet` includes the target ayah. Anchor
  to the paragraphs of PACK/numbered/S_A.md (the frozen paragraphs the page's other layers use); a block about a
  v16 addition, in an older augment9 pack, anchors to its ¶n.
- Surah page (target surah): what belongs to the surah as a whole: a parallel that runs through the surah, a
  liturgical or structural kinship (the Lord's Prayer and the Fātiḥa), a motif the surah commentary's images turn
  on; per-ayah detail only where a paragraph of the surah commentary is about it. Anchor to PACK/numbered/surah.md.
- Every block sits right after the base paragraph it speaks to; there is no section at the end of the page.

## Step 1. Read
Read the target's numbered base page completely, once, and keep your own notes (paragraph numbers and claims) in
your call directory; do not read it again. Then the discovery list named in the job header, when there is one: the
candidate passages two readers proposed for this page, with the tradition, the kind of link and the reason. It is
a seed, not a verdict: every candidate is checked against the text itself, and what it misses is yours to find.
Read the adjacent .merged.json review sidecar too: inspect all wording findings, repeat provenance and accepted
repairs. A normalized Hebrew/Greek match establishes neither relevance nor historical influence. A mismatch
may be a root, inflection, orthographic difference, ketiv/qere distinction, different witness or verse boundary.

## Step 2. Claims of the base
List for yourself every claim or image of the target page that the other scriptures speak to: a figure, a scene,
a formula, a word, an ethical motif, a liturgical act; each with its paragraph number [¶n].

## Step 3. Research
1. Corpus Coranicum: `corpus.py --intertext ayah S:A` for every ayah of the page; read the entries' notes and
   dating; they are the editors' judgement, not yours.
2. The discovery candidates, one by one: open the text (`get WLC:… SBLGNT:… SEFARIA:…`), read it in its own
   context (the neighbouring verses with `get`), and decide the kind of link and the `bag`. Judge EACH distinct
   `connection_id` in the TSV evidence against every paragraph of this page. Two models may share a connection
   ID: judge it once. Different reasons or kinds for the same reference remain separate decisions. Being
   already cited does not rule out a different, concrete contribution to another paragraph.
3. Your own search: the scene, figure or formula elsewhere in the Hebrew Bible and the New Testament (`search`
   with Hebrew or Greek words, the KJV as a finder in English); the cognates of the ayah's key words (Hebrew root
   consonants, Syriac via the Peshitta only from memory, marked); the Jewish reading of each parallel (SEFARIA
   Targum, midrash, Talmud, Rashi, Ibn Ezra, Ramban as fetched); the Christian reading from memory, marked, until
   patristic texts are in the corpus.
3b. The Semitic root table at the end of this prompt (common.md, Semitic evidence): every Arabic root, its
   corresponding Hebrew/Aramaic roots, their range across the Hebrew Bible (`hebrew.py root`), wordplay, and the
   passages where the Bible's wording shows a difference from the ayah. One root_verdicts.jsonl line per root;
   each Hebrew passage you open for it needs its research verdict like any other lookup.
4. Modern scholarship on the parallel (Neuwirth, Sinai, Reynolds, Witztum, Zellentin and others): memory pointers
   (access hafiza) with `durum:degerlendirilmedi`; a dependence or address claim is theirs, named in `alim`.
Deduplicate as you go: one block per point.
Review every paragraph for additional connections, including secondary details and contrary readings. Every
passage opened with `get`, including context-only neighbours and unsuccessful lookups, needs a verdict. Search
result snippets alone do not verify evidence. Open every evidence locator with `get`; request omitted portions
when the tool reports a cut. Explicitly mark unavailable witnesses and uncertainty instead of reconstructing them.

**Relevance (user, 2026-10-09).** Accept a connection only when it is substantive: the other text shares the commentary's scene, claim, image, argument or formula, or reverses one of them, and you can name that shared element in one sentence. A shared word, root, name or broad theme alone is not enough: reject such a candidate with the reason `keyword-only: <the shared word or theme>` (a cognate goes as `soydas` only when the other scripture's use of the word illuminates the commentary's point). Prefer fewer, stronger blocks; a `motif` block must say concretely what image or formula the two texts share.

## Research verdict ledger (verdicts.jsonl)
Write one JSON object per distinct discovery connection, including rejected and unavailable connections:

{"connection_id":"BC-<copy the exact ID from evidence>","ref":"WLC:Gen.22.2","status":"accepted","reason":"The precise connection and what the Hebrew/context establishes.","paragraphs":[2],"evidence":["WLC:Gen.22.2"],"annotations":["S001-TEV-PRL-001"]}

Use `accepted`, `rejected`, `unresolved`, or `unavailable`. Every row needs a specific reason, the exact ref,
and arrays for paragraphs, evidence and annotations (empty arrays are allowed for nonaccepted rows). An accepted
connection needs at least one valid paragraph, actual opened corpus evidence and a kept annotation ID. Cite the
exact WLC/SBLGNT verse in evidence before accepting OR rejecting its connection. Distinguish rejection on textual
grounds from unavailable evidence. Do not mark a remembered or unverified connection accepted.

For a passage from your own research or a context-only lookup, use `"connection_id":null,"origin":"research"`
with the same other fields. Give one research verdict per ref; a context-only passage may be rejected with the
reason that it supplies context but no independent addition. Each opened ref needs its own verdict even when
it also supplies evidence for another connection. Unresolved refs belong in gaps.json.unresolved; unavailable
refs belong in gaps.json.missing_sources or not_found. Include the exact ref in those entries. Every kept
annotation must be linked by a verdict; a memory-only source note can be linked to an unresolved verdict.
Evidence must include every local source cited by the linked annotation. More than one connection may use the
same annotation if it expresses their shared point. An annotation dropped by validation cannot implement an
accepted verdict. This complete internal ledger is separate from the selected research notes shown to readers.

## Step 4. Compose the records
What a good Bible page has:
- the parallels and motifs that an advanced reader of this ayah or surah would expect, each with the text quoted
  in its own language in the base's reader-tag form ({ar:…} is for Arabic; for Hebrew and Greek use
  {he:…, tr:…, gloss:…, source:…} and {el:…, tr:…, gloss:…, source:…}: the exact text copied from the corpus, a
  readable transliteration, a Turkish gloss, the corpus locator), and what it adds here;
- the counter-narratives where the Qur'an's telling differs, stated as the difference, without adjudicating;
- the cognates that illuminate a word, with the other scripture's usage;
- the interpretive tradition where it changes what the parallel means;
- elenen blocks for candidates you weighed and rejected (kat:arastirma), kaynak_notu for provenance and dating
  problems, yontem where a reader needs the limit (a resemblance is not a borrowing), duzeltme for an error in
  the base about the Bible (with `taban` and `hata`);
- at most five blocks after any one paragraph; each block one distinct unit of value; nothing the base already
  says.
Block text in Turkish, in the base's register, at most 80 words (temel/ek) or 120 (arastirma); name the text and
its place in words ("Tekvin 22'de", "Matta 6:5'te"); no first person, no talk about the process.

Record format (annotations.jsonl, one JSON object per line): the required and applicable optional schema fields (SCHEMA_BIBLE_CARD.md; enum
values exactly as listed; `gelenek` written by you here: tevrat or incil), `bag`, `tarihleme`, `nusha`, plus the
placement, both required: `paragraf` and `capa` (at least three consecutive words copied exactly from that
paragraph). ids: S<sss>-<TEV|INC>-<KOD>-<NNN> with the KOD of the block's tur, numbered in page order per
tradition and KOD: S001-TEV-PRL-001, S001-INC-MTF-001.

Search the original-language text first: Hebrew WLC for the Hebrew Bible, Greek SBLGNT for the New Testament.
Use English KJV only as a finding aid. WLC's main text preserves the written (ketiv) stream; qere and other
readings are in variant_notes, never additional words of the verse. Identify the reading when it matters.
Discovery references specify a source edition (WLC:Ps.1.3, SBLGNT:Matt.6.5, SEFARIA:...). Resolve the cited
edition's numbering; never assume an English verse number is the Hebrew one. Background-only intertexts may
support modern, kaynak_notu or yontem, but do not turn them into Jewish or Christian scripture.

## Step 5. Check and finish
1. Re-open every locator you cite (`corpus.py --intertext get`) and confirm the text says what the block says.
2. Write gaps.json: {"missing_sources":[what the intertext corpus lacks: Peshitta, patristic texts, …],
   "not_found":[…], "unresolved":[…]}.
   If no block qualifies, also write a nonempty `no_findings_reason`; an empty result without an explanation,
   or a result whose records all fail validation, cannot be accepted.
   Preserve the prefetch report's missing refs in these arrays. Write all three files even when they are empty;
   empty annotation output does not waive verdicts for the discovered or researched passages.
3. Run the validator from the job header and fix every error and warning; a record that still fails is dropped.
4. Write root_verdicts.jsonl (one line per Arabic root of the table) and run the verdict draft check in the header. The final check also audits actual get results and completeness
   against the native transcript. No candidate may disappear from this ledger.
5. Render the preview (job header) and read the page once as the reader would.
Final message: blocks by gelenek and tur, the candidates accepted and rejected, and anything you could not do.


# Semitic root table of this page

The Arabic roots this page cites, with the Hebrew and Biblical Aramaic roots that correspond to them by regular sound correspondences and exist in the lexicon (hebrew.py). Each root needs one line in root_verdicts.jsonl (Step 3b).

== Arabic root ء ن س: 4 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew אנש (ء→א ن→נ س→ש): BDB cites an Arabic cognate; 1275 WLC occurrences; `hebrew.py root אנש` lists them
  - אֱנוֹשׁ (ʾĕnôš) N 'man' [H582; Hebrew; 42 WLC occurrences] Strong: properly, a mortal (and thus differing from the more dignified 120); hence, a man in general (singly or collectively)
  - אָנַשׁ (ʾānaš) V 'be weak' [H605; Hebrew; 9 WLC occurrences] Strong: to be frail, feeble, or (figuratively) melancholy
  - אֵשׁ (ʾēš) N 'fire' [H784; Hebrew; 376 WLC occurrences] Strong: fire (literally or figuratively)
  - אֶשְׁדָּת (ʾešdāt) N 'fire' [H799; Hebrew; 1 WLC occurrence] Strong: a fire-law
  - אִשֶּׁה (ʾiššeh) N 'an offering made by fire' [H801; Hebrew; 65 WLC occurrences] Strong: properly, a burnt-offering; but occasionally of any sacrifice
  - אִשָּׁה (ʾiššâ) N 'woman' [H802; Hebrew; 781 WLC occurrences] Strong: a woman
  - אֶשָּׁה (ʾeššâ) N 'from their fire' [H800; Hebrew; 1 WLC occurrence] Strong: fire
* Aramaic אנש (ء→א ن→נ س→ש): sound correspondence only (unverified); 26 WLC occurrences; `hebrew.py root אנש` lists them
  - אֱנָשׁ (ʾĕnāš) N 'man' [H606; Aramaic; 25 WLC occurrences] Strong: a man
  - נְשִׁין (nĕšîn) N 'wives' [H5389; Aramaic; 1 WLC occurrence]
* Hebrew אנס (ء→א ن→נ س→ס): sound correspondence only (unverified); 1 WLC occurrences; `hebrew.py root אנס` lists them
  - אָנַס (ʾānas) V 'compel' [H597; Hebrew; 1 WLC occurrence] Strong: to insist
* Aramaic אנס (ء→א ن→נ س→ס): sound correspondence only (unverified); 1 WLC occurrences; `hebrew.py root אנס` lists them
  - אֲנַס (ʾănas) V 'oppress' [H598; Aramaic; 1 WLC occurrence] Strong: figuratively, to distress

== Arabic root ح ق ق: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew חקק (ح→ח ق→ק ق→ק): sound correspondence only (unverified); 254 WLC occurrences; `hebrew.py root חקק` lists them
  - חֹק (ḥōq) N 'something prescribed' [H2706; Hebrew; 127 WLC occurrences] Strong: an enactment; hence, an appointment (of time, space, quantity, labor or usage)
  - חֻקָּה (ḥuqqâ) N 'something prescribed' [H2708; Hebrew; 105 WLC occurrences]
  - חֵקֶק (ḥēqeq) N 'something prescribed' [H2711; Hebrew; 2 WLC occurrences] Strong: an enactment, a resolution
  - חָקַק (ḥāqaq) V 'cut in' [H2710; Hebrew; 19 WLC occurrences] Strong: properly, to hack, i.e. engrave (Judges 5:14, to be a scribe simply); by implication, to enact (laws being cut in stone or metal tablets in primitive times) or (gen.) prescribe
  - חֻקֹֿק (ḥuqōq) Np 'Hukkok' [H2712a; Hebrew; 1 WLC occurrence] Strong: Chukkok or Chukok, a place in Palestine

== Arabic root خ س ر: 3 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew חשר (خ→ח س→ש ر→ר): BDB cites an Arabic cognate; 2 WLC occurrences; `hebrew.py root חשר` lists them
  - חִשֻּׁר (ḥiššur) N 'nave' [H2840; Hebrew; 1 WLC occurrence] Strong: combined, i.e. the nave or hub of a wheel (as holding the spokes together)
  - חַשְׁרָה (ḥašrâ) N 'collection' [H2841; Hebrew; 1 WLC occurrence] Strong: properly, a combination or gathering, i.e. of watery clouds
* Hebrew חסר (خ→ח س→ס ر→ר): sound correspondence only (unverified); 59 WLC occurrences; `hebrew.py root חסר` lists them
  - חֶ֫סֶר (ḥeser) N 'want' [H2639; Hebrew; 2 WLC occurrences] Strong: lack; hence, destitution
  - חָסֵר (ḥāsēr) A 'needy' [H2638; Hebrew; 19 WLC occurrences] Strong: lacking; hence, without
  - חָסֵר (ḥāsēr) V 'lack' [H2637; Hebrew; 21 WLC occurrences] Strong: to lack; by implication, to fail, want, lessen
  - חֹ֫סֶר (ḥōser) N 'want' [H2640; Hebrew; 3 WLC occurrences] Strong: poverty
  - חֶסְרוֹן (ḥesrôn) N 'thing lacking' [H2642; Hebrew; 1 WLC occurrence] Strong: deficiency
  - מַחְסוֹר (maḥsôr) N 'need' [H4270; Hebrew; 13 WLC occurrences] Strong: deficiency; hence, impoverishment
* Aramaic חסר (خ→ח س→ס ر→ר): sound correspondence only (unverified); 1 WLC occurrences; `hebrew.py root חסר` lists them
  - חַסִּר (ḥassir) A 'lacking' [H2627; Aramaic; 1 WLC occurrence] Strong: deficient

== Arabic root ص ب ر: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew צבר (ص→צ ب→ב ر→ר): sound correspondence only (unverified); 8 WLC occurrences; `hebrew.py root צבר` lists them
  - צִבּוּר (ṣibbûr) N 'heap' [H6652; Hebrew; 1 WLC occurrence] Strong: a pile
  - צָבַר (ṣābar) V 'heap up' [H6651; Hebrew; 7 WLC occurrences] Strong: to aggregate

== Arabic root ع ص ر: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew עצר (ع→ע ص→צ ر→ר): sound correspondence only (unverified); 63 WLC occurrences; `hebrew.py root עצר` lists them
  - מַעְצוֹר (maʿṣôr) N 'restraint' [H4622; Hebrew; 1 WLC occurrence] Strong: objectively, a hindrance
  - מַעְצָר (maʿṣār) N 'restraint' [H4623; Hebrew; 1 WLC occurrence] Strong: subjectively, control
  - עֶ֫צֶר (ʿeṣer) N 'restraint' [H6114; Hebrew; 1 WLC occurrence] Strong: restraint
  - עָצַר (ʿāṣar) V 'restrain' [H6113; Hebrew; 46 WLC occurrences] Strong: to inclose; by analogy, to hold back; also to maintain, rule, assemble
  - עֹ֫צֶר (ʿōṣer) N 'restraint' [H6115; Hebrew; 3 WLC occurrences] Strong: closure; also constraint
  - עֲצָרָה (ʿăṣārâ) N 'assembly' [H6116; Hebrew; 11 WLC occurrences] Strong: an assembly, especially on a festival or holiday

== Arabic root ع م ل: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew עמל (ع→ע م→מ ل→ל): sound correspondence only (unverified); 76 WLC occurrences; `hebrew.py root עמל` lists them
  - עָמֵל (ʿāmēl) A 'toiling' [H6001b; Hebrew; 5 WLC occurrences] Strong: toiling; concretely, a laborer; figuratively, sorrowful
  - עָמֵל (ʿāmēl) N 'laborer' [H6001a; Hebrew; 4 WLC occurrences] Strong: toiling; concretely, a laborer; figuratively, sorrowful
  - עָמַל (ʿāmal) V 'labour' [H5998; Hebrew; 11 WLC occurrences] Strong: to toil, i.e. work severely and with irksomeness
  - עָמָל (ʿāmāl) N 'trouble' [H5999; Hebrew; 55 WLC occurrences] Strong: toil, i.e. wearing effort; hence, worry, whether of body or mind
  - עָמָל (ʿāmāl) Np 'Amal' [H6000; Hebrew; 1 WLC occurrence] Strong: Amal, an Israelite

== Arabic root و ص ي: 0 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
  no Hebrew or Aramaic root with these corresponding consonants is in the lexicon
