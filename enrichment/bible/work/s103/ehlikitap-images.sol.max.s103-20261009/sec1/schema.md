# Schema 3.3 card for the Bible pass (generated from schema.json; full reference: SCHEMA.md)

Record = one JSON object per line in annotations.jsonl. Required: id, gelenek, tur, ayet, islev, iliski, durum, kat, metin, kaynak, paragraf, capa, bag, tarihleme, nusha.
- IDs: S<sss>-TEV-<KOD>-<NNN> for tevrat; S<sss>-INC-<KOD>-<NNN> for incil. ayet "107:3" or "107:1-3" (several with |); kaynak = corpus locators, pipe-separated, or hafiza; metin one paragraph, at most 80 words (temel, ek) or 120 (arastirma).
- paragraf = the [¶n] number of the page's prose paragraph; capa = at least three exact words of it (or of its v16 additions, the unnumbered `<!-- v16:augment … para=n -->` blocks under it in an ayah base).

## tur (KOD; traditions; extra required fields)
- modern (MDR; islami,tevrat,incil): modern Islamic and Western scholarship, kept apart from classical attestation
- paralel (PRL; tevrat,incil): the same figure, scene or story told in the other scripture (Abraham's sacrifice, Joseph, the sleepers)
- motif (MTF; tevrat,incil): a shared image, formula or ethical motif without a shared story (praying to be seen: Mt 6:5 and 107:6)
- karsi_anlati (KRA; tevrat,incil): the Qur'an tells it differently, corrects or answers it (Mary, the crucifixion, the calf); the difference is the point
- soydas (SYD; tevrat,incil): a Hebrew, Aramaic or Syriac cognate of the Qur'anic word and how the other scripture uses it; loan claims only with named scholarship
- yorum_gelenegi (YGL; tevrat,incil): Jewish or Christian interpretation of the parallel text (Targum, midrash, Talmud; Church Fathers, Syriac homilies such as Ephrem and Jacob of Serugh)
- elenen (ELN; islami,tevrat,incil) + guc: a connection considered and rejected, kept for audit
- kaynak_notu (KNT; islami,tevrat,incil): source criticism: provenance, attribution, edition, isnād caveats
- yontem (YNT; islami,tevrat,incil): a methodological limit or distinction the reader needs here
- duzeltme (DZT; islami,tevrat,incil) + hata, taban: an error in the frozen base: wrong label, quotation, ayah number, fact or rendering; also logged to errata.jsonl

## Values
- gelenek: islami = the Islamic-literature pass: tafsir, hadith, lexica, meals and the rest of the main corpus; tevrat = the Hebrew Bible in any witness (Masoretic, Septuagint, Peshitta, Targum), the Psalms (Zebur) included; Jewish pseudepigrapha; Mishnah, Talmud, midrash; incil = the New Testament in any witness (Greek, Peshitta, Diatessaron); Christian apocrypha (Protevangelium of James, Infancy Gospels); Church Fathers; Syriac homilies. A Hebrew Bible text read through Christian exegesis is two blocks: the text (tevrat), its Christian reading (incil)
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
- bag: benzerlik = the texts resemble each other; nothing is claimed about a relation (the default); ortak_havza = both draw on a tradition current in Late Antiquity; no direction claimed; muhatap = named scholarship argues the Qur'an addresses, answers or corrects this tradition; requires alim; etki_iddiasi = named scholarship argues dependence; reported as that scholar's claim, never as fact; requires alim; impossible for a text dated after the Qur'an
- tarihleme: kuran_oncesi = written down before the early 7th century; cagdas = roughly contemporary with the Qur'an; kuran_sonrasi = redacted after the Qur'an (e.g. Pirqe de-Rabbi Eliezer); may preserve older material, which the block must argue; belirsiz = dating disputed or unknown
- nusha: masoretik = the Hebrew Bible (Westminster Leningrad Codex); septuaginta = the Greek Old Testament; pesitta = the Syriac Bible, Old and New Testament; targum = Aramaic renderings of the Hebrew Bible; yunanca_ahit = the Greek New Testament; diatessaron = Tatian's gospel harmony, through its witnesses; apokrif = Jewish pseudepigrapha or Christian apocrypha; rabbani = Mishnah, Talmud, midrash; patristik = Greek and Latin patristic writing; suryani = Syriac homilies and hymns (Ephrem, Jacob of Serugh, Narsai); tercume = a translated witness, identified explicitly; KJV is a finding aid when Hebrew or Greek is available; uygulanmaz = background scholarship or a method/source note that cites no scriptural witness

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
- paralel_bagimlilik_degil: a parallel is not a dependence: bag defaults to benzerlik; muhatap and etki_iddiasi require alim and a source that argues it; etki_iddiasi is impossible with tarihleme:kuran_sonrasi
- yenilik_tek: a separate yenilik block only when no antecedent was found, kat:arastirma, at most one per paragraph; an attested finding carries klasik_tanik/taranan/tarama on its oncul block
- okuma_akisi: blocks are read right after their paragraph: no 'taban' in metin (say şerh or state the point), no closing disclaimers, each point once on the page, at most five blocks after one paragraph
- Background-only intertexts may support modern/kaynak_notu/yontem, never a scripture parallel.
- WLC text is the written (ketiv) stream; variant_notes preserves qere separately. Name the reading used.
- A source locator names its own edition and numbering; do not copy KJV verse numbers into WLC blindly.
