# Schema 3.2 card for the Islamic-literature pass (generated from schema.json; the full reference, with the Bible pass, is SCHEMA.md)

Record = one JSON object per line in annotations.jsonl. Required in every record: id, tur, ayet, islev, iliski, durum, kat, metin, kaynak, paragraf, capa (gelenek is added by the script).
- id S<sss>-<KOD>-<NNN>; ayet "107:3" or "107:1-3" (several with |); kaynak = corpus locators, pipe-separated, or hafiza; metin one paragraph, at most 80 words (temel, ek) or 120 (arastirma).
- paragraf = the [¶n] number of the page's prose paragraph; capa = at least three exact words of it (or of its v16 additions, the unnumbered `<!-- v16:augment … para=n -->` blocks under it in an ayah base).

## tur (KOD; traditions; extra required fields)
- tefsir_rivayet (TRV; islami): explanations of Companions/Successors as transmitted (Mujāhid, Muqātil, Ṭabarī's aqwāl, al-Durr al-manthūr)
- tefsir_dirayet (TDR; islami): an exegete's own analysis: language, reasoning, theology (Zamakhsharī, Rāzī, Ibn ʿĀshūr, Elmalılı, Kur'an Yolu)
- isari (ISR; islami): ishārī readings (Qushayrī, Sulamī, Tustarī, Bursevî); labelled as such, never as dirayet
- nazm (NZM; islami): sequence, adjacency, surah unity, surah-to-surah relation; structural form (ring, symmetry, rhyme groups) with islev:yapi
- nuzul (NZL; islami) + tarihsellik: Makkī/Madanī, revelation order and chronology lists (Itqān, Ibn ʿĀshūr; Nöldeke, Neuwirth reported beside them)
- esbab (ESB; islami) + derece, tarihsellik: isnād-bearing occasion reports of any grade, each with derece and tarihsellik shown
- hadis (HDS; islami) + derece: Prophetic hadith; sahih only (Bukhārī, Muslim, or sunan reports every named grader calls sahih)
- kiraat (KRT; islami) + kiraat_turu: canonical and non-canonical readings and their linguistic justification (ḥujja)
- lugat (LGT; islami) + sozluk: synchronic lexical evidence: senses, branches, the lexica's own wording and shawāhid
- vucuh (VCH; islami) + guc, terim: the senses a word takes across the Qur'an, from the wujūh wa-naẓāʾir books (Muqātil, Dāmghānī, Ibn al-Jawzī) and the usage table
- nahiv (NHV; islami): syntax, iʿrāb, morphology that bears on meaning
- belagat (BLG; islami): rhetoric, majāz, imagery, iʿjāz theory (Zamakhsharī, Jurjānī, Asās)
- ayet_ayet (AYT; islami) + guc: a Qur'anic passage that explains, extends or contrasts this one
- anlam_tarihi (ANT; islami) + terim: diachronic change only: pre-Qur'anic → Qur'anic → later Arabic → Turkish loanword drift
- tarihi_baglam (TBG; islami): sourced setting: sīra, Mecca, material culture, institutions
- fikih (FKH; islami): legal readings; optional
- kelam (KLM; islami): theological debate; optional
- meal (MEL; islami) + kayip, mutercim, terim: how Turkish (and relay) translations render a term: what they keep, lose or add
- modern (MDR; islami,tevrat,incil): modern Islamic and Western scholarship, kept apart from classical attestation
- yenilik (YNL; islami) + guc, klasik_tanik, tarama, taranan: how far a finding of the base is attested, written only when no antecedent was found (klasik_tanik bulunamadi or yapitaslari); an attested finding carries klasik_tanik on its oncul block. At most one per paragraph; always kat:arastirma
- elenen (ELN; islami,tevrat,incil) + guc: a connection considered and rejected, kept for audit
- kaynak_notu (KNT; islami,tevrat,incil): source criticism: provenance, attribution, edition, isnād caveats
- yontem (YNT; islami,tevrat,incil): a methodological limit or distinction the reader needs here
- duzeltme (DZT; islami,tevrat,incil) + hata, taban: an error in the frozen base: wrong label, quotation, ayah number, fact or rendering; also logged to errata.jsonl

## Values
- islev: dayanak = the received contextual meaning; erken_tanik = an early attestation of an interpretation or sense; aciklama = clarifies wording, grammar, referent or a distinction; destek = independently supports a reading already on the page; oncul = a source that already states (part of) a finding of the base; itiraz = an argument that a reading of the base cannot hold here (grammar, near-synonymy, root identity, reading); not a mere preference; tercih = a source's stated preference among readings ("the correct view is X"); reported, not adjudicated; tasnif = a source lists several senses without choosing (Māwardī, Ibn al-Jawzī); ihtilaf = a genuine disagreement among sources; anlam_alani = several live senses of a word or expression; gelisim = how an interpretation or sense changed over time; sinir = what the ayah or a reading does not say; prevents an overreading; karsit = an opposite or counter-scene that sharpens the reading; sonuc = why a distinction matters for understanding; fazilet = reports on the merit of a surah or ayah; yapi = formal structure: ring, symmetry, rhyme groups, parallelism
- iliski: dogrudan = the source explicitly treats this ayah or phrase (Bible pass: a text the scholarship reads as directly addressed by this ayah); tematik = same theme, not an explanation of this ayah; lafzi = linked through the same word, root or expression; yapisal = linked through position, sequence or form; karsilastirmali = a comparison across sources, readings or translations
- durum: acik = stated in the cited source; aktarilan = the source transmits it; its truth is not established; tartismali = competing reports or positions; cikarim = inferred from evidence, not stated; yorum = an interpretive synthesis (the base's or the block's); degerlendirilmedi = not checked against a source; required for model memory
- kat: temel = shown by default: what an advanced reader should see first at that point; ek = shown by default: supporting detail; arastirma = hidden by default (the reader opens it): audit trail, novelty detail, rejected candidates, technical source criticism
- guc: dogrudan = direct support for the reading in context; guclu = a strongly illuminating link that is not the primary meaning; ikincil = a legitimate secondary resonance that keeps the primary meaning intact; zayif = possible but thinly constrained; reddedildi = considered and rejected
- klasik_tanik: acik = the same connection is stated in a checked source; kismi = an important part is stated; the base adds the rest; yapitaslari = the ingredients are attested separately; the combination is not; bulunamadi = no parallel in the listed sources; never an absolute claim
- tarama: dilim = only the per-ayah texts of this surah were searched; a negative result is weak; tam = whole-book texts were searched across the Qur'an
- derece: sahih = sahih by the named authority; hasan = esbab only; zayif = esbab only; mevzu = esbab only; ihtilafli = esbab only; name the graders; degerlendirilmedi = esbab only; no grade found
- tarihsellik: sabit = independently established; muhtemel = probable; belirsiz = uncertain; tartismali = competing reports
- kiraat_turu: mutevatir = one of the canonical readings; sazz = a non-canonical reading; sahabe = a reading reported from a Companion's codex, often explanatory; belirsiz = standing not established
- kayip: kelime = a different concept (ṣudūr rendered as kalp); eleman = a preposition, pronoun, number, emphasis, conjunction or voice the Turkish could have kept; aralik = several live senses narrowed to one; ekleme = the translator's own words presented as the text; kayma = a loanword whose Turkish sense has shifted (namaz, din, ibadet); isaretleme = brackets, italics or notes changed so an addition no longer looks like one; aktarma = a difference that comes from translating an intermediate text (Asad's English, Mawdudi's Urdu), not the Arabic
- yon: kayip = the translation loses against the pole; kazanc = the translation recovers something against the pole
- kiyas: arapca = judged against the Arabic; ara_metin = judged against the text it was translated from
- hata: kaynak_etiketi = a wrong source or lexicon label; alinti = a misquoted text; ayet_no = a wrong reference; olgu = a factual error; ceviri = a wrong rendering of the Arabic

## Also required
- islev:oncul: guc

## Optional fields
- derece_veren: who grades it: Buhârî | Müslim for the Sahihayn, named graders for other books (as the corpus records them); empty only with derece:degerlendirilmedi
- yon: loss or gain; a relay step can be both against different poles
- kiyas: the pole a meal is judged against: the Arabic, or the intermediate text it was translated from
- alim: named authority the block reports
- ravi: transmitter of a report
- koken: earliest traceable source of a report
- tekrar: later works repeating the same report unchanged, pipe-separated IDs
- gerekce: reason for a rejection or a grade
- not: short technical note

## Rules
- hadis_sahih: tur:hadis requires derece:sahih and derece_veren naming Buhârî, Müslim or the graders recorded in the corpus; merit (fazilet) reports are hadith and follow the same rule; a weak Prophetic attribution of a sound Companion statement is reported as the Companion's (tefsir_rivayet)
- hafiza: kaynak:hafiza (or a corpus source with access hafiza) requires durum:degerlendirilmedi; forbidden for tur hadis and nuzul, for derece, and for Turkish loanword history in anlam_tarihi
- itiraz_vs_tercih: a source preferring another reading is islev:tercih; islev:itiraz needs an argument that the base's reading cannot hold here
- yenilik_scope: klasik_tanik:bulunamadi with tarama:dilim must say in metin that only the per-ayah slice was searched
- modern_dictionaries: modern Arabic dictionaries (VASIT, MUHIT, HANSWEHR) may be cited only in anlam_tarihi, as evidence of later drift
- paragraf_zorunlu: every block names its prose paragraph (paragraf) and quotes at least three words of it (capa); it is rendered right after that paragraph; a block whose number and words do not match is dropped
- gelenek_ayrimi: each block belongs to one gelenek and its tur must allow it. islami blocks cite no Bible, Jewish or Christian source (kind intertext); tevrat and incil blocks cite only sources of their own gelenek, plus the Qur'an text and modern scholarship. The passes run separately and never read each other's records
- yenilik_tek: a separate yenilik block only when no antecedent was found, kat:arastirma, at most one per paragraph; an attested finding carries klasik_tanik/taranan/tarama on its oncul block
- okuma_akisi: blocks are read right after their paragraph: no 'taban' in metin (say şerh or state the point), no closing disclaimers, each point once on the page, at most five blocks after one paragraph
