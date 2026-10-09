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
