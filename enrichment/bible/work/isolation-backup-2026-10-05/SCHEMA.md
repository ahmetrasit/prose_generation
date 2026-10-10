# Annotation schema 3.3 (generated from schema.json — do not edit)

Every block is one line in the rendered page and one JSON object in annotations.jsonl:

```
{id:"S107-HDS-001", gelenek:islami, tur:hadis, ayet:"107:6", islev:destek, iliski:tematik, durum:acik, kat:ek, derece:sahih, derece_veren:"Müslim", metin:"…", kaynak:"MUSLIM:2985"}
{id:"S107-INC-MTF-001", gelenek:incil, tur:motif, ayet:"107:6", islev:karsit, iliski:tematik, durum:acik, kat:ek, nusha:yunanca_ahit, tarihleme:kuran_oncesi, bag:benzerlik, metin:"…", kaynak:"SBLGNT:Matt.6.5"}
```

- Two passes write blocks to the same frozen base and never read each other's records: the Islamic-literature pass
  (gelenek islami, stamped by the script) and the Bible pass (gelenek tevrat or incil, per block). A merged page
  shows, after each base paragraph, its islami blocks, then its tevrat blocks, then its incil blocks.

- Keys and values are ASCII-folded Turkish. The reader shows labels in Turkish, English or German from schema.json.
- Required in every block: id, gelenek, tur, ayet, islev, iliski, durum, kat, metin, kaynak. Further fields are required by type (see below).
- `id`: Islamic: S<surah, 3 digits>-<kod of tur>-<NNN>, e.g. S107-HDS-001. Bible: S<sss>-<TEV for tevrat, INC for incil>-<kod of tur>-<NNN>, e.g. S001-TEV-PRL-001 or S001-INC-MTF-001. Unique across all layers of a page. `ayet` = this page's ayah or range ("107:1-3"; several with |).
- `kaynak` = corpus locators, pipe-separated, exactly as `tools/corpus.py` prints them, or `hafiza` (model memory).
- `metin` = one paragraph in the page language; at most 80 words (temel, ek) or
  120 (arastirma).
- Placement (records only, not rendered), both required: `paragraf` = the number of a prose paragraph of the base of
  the page the record belongs to (numbered from 1 as in v16's augment; headings and "Kaynaklar:" lines unnumbered;
  the pack's numbered/ files show the numbers; v16 augment9 additions in an ayah base, `<!-- v16:augment … para=n -->`,
  are unnumbered and belong to ¶n), and `capa` = at least three exact words of that paragraph or of its additions, which
  confirm the number. The block is rendered right after that paragraph (after its additions); there are no
  end-of-page blocks, and a record whose number and words do not match is dropped. Both passes number the same base, so they merge by
  paragraph.

## Fields

| field | tr | en | required for | definition |
|---|---|---|---|---|
| `id` | Kimlik | ID | all | unique within the page |
| `gelenek` | Gelenek | Tradition | all | which literature the block belongs to; one per block. The Islamic pass stamps islami (the script adds it); in the Bible pass each block is tevrat or incil Values: `gelenek` table. |
| `tur` | Tür | Type | all | what kind of information the block carries Values: `tur` table. |
| `ayet` | Âyet | Verse | all | the ayah or range of this page the block is about: "107:3", "107:1-3"; several with \|. Other passages the block cites go in metin and kaynak, not here |
| `islev` | İşlev | Function | all | why the block stands at this point of the page Values: `islev` table. |
| `iliski` | İlişki | Relation | all | how the cited source relates to this ayah Values: `iliski` table. |
| `durum` | Durum | Status | all | epistemic status of the block's claim relative to its source Values: `durum` table. |
| `kat` | Katman | Layer | all | display layer Values: `kat` table. |
| `metin` | Metin | Text | all | the block's prose, in the page language, within the word limit of its layer |
| `kaynak` | Kaynak | Source | all | source locators, pipe-separated: <ID>:<locator> exactly as in the corpus (TAB:107:3, MUSLIM:2985, ELMALILI:107:2, LISAN:دعع), or "hafiza" for model memory; Bible locators use OSIS book abbreviations (WLC:Gen.22.2, SBLGNT:Matt.6.5) |
| `guc` | Güç | Strength | tur: yenilik\|elenen\|ayet_ayet\|vucuh, islev: oncul | strength of a connection to the project's reading Values: `guc` table. |
| `klasik_tanik` | Klasik tanıklık | Classical attestation | tur: yenilik | how far a project finding is attested in the checked sources; on a yenilik block, or on the oncul block of an attested finding Values: `klasik_tanik` table. |
| `taranan` | Taranan kaynaklar | Sources checked | tur: yenilik | corpus IDs actually searched, pipe-separated |
| `tarama` | Tarama kapsamı | Search scope | tur: yenilik | whether the check ran over the per-ayah slice only or over whole-book texts Values: `tarama` table. |
| `derece` | Derece | Grade | tur: hadis\|esbab | hadith/report grade; hadis blocks accept only sahih Values: `derece` table. |
| `derece_veren` | Derece veren | Graded by |  | who grades it: Buhârî \| Müslim for the Sahihayn, named graders for other books (as the corpus records them); empty only with derece:degerlendirilmedi |
| `tarihsellik` | Tarihsellik | Historicity | tur: esbab\|nuzul | historical standing of an event or chronology claim Values: `tarihsellik` table. |
| `kiraat_turu` | Kıraat türü | Reading type | tur: kiraat | standing of a reading Values: `kiraat_turu` table. |
| `sozluk` | Sözlük | Lexicon | tur: lugat | which lexicon(s) the observation comes from, pipe-separated corpus IDs; PROJE = the project dictionary (../dictionary via quran-data); modern Arabic dictionaries only inside anlam_tarihi |
| `mutercim` | Mütercim | Translator | tur: meal | meal source ID (MEAL-OKUYAN), several with \|, or "ortak" for a loss shared across the panel |
| `terim` | Terim | Term | tur: meal\|vucuh\|anlam_tarihi | the Arabic word or expression in question |
| `kayip` | Kayıp türü | Loss type | tur: meal | what a translation loses, pipe-separated Values: `kayip` table. |
| `yon` | Yön | Direction |  | loss or gain; a relay step can be both against different poles Values: `yon` table. |
| `kiyas` | Kıyas | Compared with |  | the pole a meal is judged against: the Arabic, or the intermediate text it was translated from Values: `kiyas` table. |
| `taban` | Taban alıntısı | Base quote | tur: duzeltme | exact short quote of the base text being corrected; must occur verbatim in the base |
| `hata` | Hata türü | Error type | tur: duzeltme | kind of error in the base Values: `hata` table. |
| `alim` | Âlim | Scholar |  | named authority the block reports |
| `ravi` | Râvi | Transmitter |  | transmitter of a report |
| `koken` | Köken | Origin |  | earliest traceable source of a report |
| `tekrar` | Tekrarlayanlar | Repeated in |  | later works repeating the same report unchanged, pipe-separated IDs |
| `gerekce` | Gerekçe | Reason |  | reason for a rejection or a grade |
| `not` | Not | Note |  | short technical note |
| `bag` | Bağ | Connection claim | gelenek: tevrat\|incil | what the block claims about the link between the Qur'an and the other text; a parallel is not a dependence, so the weakest fitting value is used Values: `bag` table. |
| `tarihleme` | Tarihleme | Dating | gelenek: tevrat\|incil | date of the cited text relative to the Qur'an (as the scholarship dates it) Values: `tarihleme` table. |
| `nusha` | Nüsha | Text witness | gelenek: tevrat\|incil | the witness or text family quoted; readings differ, and the Qur'an's closest match may be the Syriac or Greek, not the Hebrew. Pipe-separated when several are compared Values: `nusha` table. |

## `gelenek`

| value | tr | en | definition |
|---|---|---|---|
| `islami` | İslâmî literatür | Islamic literature | the Islamic-literature pass: tafsir, hadith, lexica, meals and the rest of the main corpus |
| `tevrat` | Tevrat ve Yahudi geleneği | Hebrew Bible and Jewish tradition | the Hebrew Bible in any witness (Masoretic, Septuagint, Peshitta, Targum), the Psalms (Zebur) included; Jewish pseudepigrapha; Mishnah, Talmud, midrash |
| `incil` | İncil ve Hristiyan geleneği | New Testament and Christian tradition | the New Testament in any witness (Greek, Peshitta, Diatessaron); Christian apocrypha (Protevangelium of James, Infancy Gospels); Church Fathers; Syriac homilies. A Hebrew Bible text read through Christian exegesis is two blocks: the text (tevrat), its Christian reading (incil) |

## `tur`

| value | kod | gelenek | tr | en | definition |
|---|---|---|---|---|---|
| `tefsir_rivayet` | TRV | islami | Rivâyet tefsiri | Transmitted exegesis | explanations of Companions/Successors as transmitted (Mujāhid, Muqātil, Ṭabarī's aqwāl, al-Durr al-manthūr) |
| `tefsir_dirayet` | TDR | islami | Dirâyet tefsiri | Analytical exegesis | an exegete's own analysis: language, reasoning, theology (Zamakhsharī, Rāzī, Ibn ʿĀshūr, Elmalılı, Kur'an Yolu) |
| `isari` | ISR | islami | İşârî tefsir | Allusive (Sufi) reading | ishārī readings (Qushayrī, Sulamī, Tustarī, Bursevî); labelled as such, never as dirayet |
| `nazm` | NZM | islami | Nazım | Coherence | sequence, adjacency, surah unity, surah-to-surah relation; structural form (ring, symmetry, rhyme groups) with islev:yapi |
| `nuzul` | NZL | islami | Nüzul | Revelation history | Makkī/Madanī, revelation order and chronology lists (Itqān, Ibn ʿĀshūr; Nöldeke, Neuwirth reported beside them) |
| `esbab` | ESB | islami | Esbâb-ı nüzul | Occasion of revelation | isnād-bearing occasion reports of any grade, each with derece and tarihsellik shown |
| `hadis` | HDS | islami | Hadis | Hadith | Prophetic hadith; sahih only (Bukhārī, Muslim, or sunan reports every named grader calls sahih) |
| `kiraat` | KRT | islami | Kıraat | Reading | canonical and non-canonical readings and their linguistic justification (ḥujja) |
| `lugat` | LGT | islami | Lugat | Lexicon | synchronic lexical evidence: senses, branches, the lexica's own wording and shawāhid |
| `vucuh` | VCH | islami | Vücuh ve nezâir | Sense inventory | the senses a word takes across the Qur'an, from the wujūh wa-naẓāʾir books (Muqātil, Dāmghānī, Ibn al-Jawzī) and the usage table |
| `nahiv` | NHV | islami | Nahiv | Grammar | syntax, iʿrāb, morphology that bears on meaning |
| `belagat` | BLG | islami | Belâgat | Rhetoric | rhetoric, majāz, imagery, iʿjāz theory (Zamakhsharī, Jurjānī, Asās) |
| `ayet_ayet` | AYT | islami | Âyetle tefsir | Qur'an by Qur'an | a Qur'anic passage that explains, extends or contrasts this one |
| `anlam_tarihi` | ANT | islami | Anlam tarihi | Semantic history | diachronic change only: pre-Qur'anic → Qur'anic → later Arabic → Turkish loanword drift |
| `tarihi_baglam` | TBG | islami | Tarihî bağlam | Historical setting | sourced setting: sīra, Mecca, material culture, institutions |
| `fikih` | FKH | islami | Fıkıh | Law | legal readings; optional |
| `kelam` | KLM | islami | Kelâm | Theology | theological debate; optional |
| `meal` | MEL | islami | Meal incelemesi | Translation review | how Turkish (and relay) translations render a term: what they keep, lose or add |
| `modern` | MDR | islami, tevrat, incil | Modern çalışma | Modern scholarship | modern Islamic and Western scholarship, kept apart from classical attestation |
| `yenilik` | YNL | islami | Yenilik denetimi | Novelty audit | how far a finding of the base is attested, written only when no antecedent was found (klasik_tanik bulunamadi or yapitaslari); an attested finding carries klasik_tanik on its oncul block. At most one per paragraph; always kat:arastirma |
| `paralel` | PRL | tevrat, incil | Paralel anlatı | Parallel narrative | the same figure, scene or story told in the other scripture (Abraham's sacrifice, Joseph, the sleepers) |
| `motif` | MTF | tevrat, incil | Ortak motif | Shared motif | a shared image, formula or ethical motif without a shared story (praying to be seen: Mt 6:5 and 107:6) |
| `karsi_anlati` | KRA | tevrat, incil | Karşı anlatı | Counter-version | the Qur'an tells it differently, corrects or answers it (Mary, the crucifixion, the calf); the difference is the point |
| `soydas` | SYD | tevrat, incil | Soydaş kelime | Cognate | a Hebrew, Aramaic or Syriac cognate of the Qur'anic word and how the other scripture uses it; loan claims only with named scholarship |
| `yorum_gelenegi` | YGL | tevrat, incil | Yorum geleneği | Exegetical tradition | Jewish or Christian interpretation of the parallel text (Targum, midrash, Talmud; Church Fathers, Syriac homilies such as Ephrem and Jacob of Serugh) |
| `elenen` | ELN | islami, tevrat, incil | Elenen aday | Rejected candidate | a connection considered and rejected, kept for audit |
| `kaynak_notu` | KNT | islami, tevrat, incil | Kaynak notu | Source note | source criticism: provenance, attribution, edition, isnād caveats |
| `yontem` | YNT | islami, tevrat, incil | Yöntem notu | Method note | a methodological limit or distinction the reader needs here |
| `duzeltme` | DZT | islami, tevrat, incil | Düzeltme | Erratum | an error in the frozen base: wrong label, quotation, ayah number, fact or rendering; also logged to errata.jsonl |

## `islev`

| value | tr | en | definition |
|---|---|---|---|
| `dayanak` | Dayanak | Anchor | the received contextual meaning |
| `erken_tanik` | Erken tanık | Early witness | an early attestation of an interpretation or sense |
| `aciklama` | Açıklama | Clarification | clarifies wording, grammar, referent or a distinction |
| `destek` | Destek | Corroboration | independently supports a reading already on the page |
| `oncul` | Öncül | Antecedent | a source that already states (part of) a finding of the base |
| `itiraz` | İtiraz | Counter-evidence | an argument that a reading of the base cannot hold here (grammar, near-synonymy, root identity, reading); not a mere preference |
| `tercih` | Tercih | Preference | a source's stated preference among readings ("the correct view is X"); reported, not adjudicated |
| `tasnif` | Tasnif | Enumeration | a source lists several senses without choosing (Māwardī, Ibn al-Jawzī) |
| `ihtilaf` | İhtilaf | Disagreement | a genuine disagreement among sources |
| `anlam_alani` | Anlam alanı | Semantic range | several live senses of a word or expression |
| `gelisim` | Gelişim | Development | how an interpretation or sense changed over time |
| `sinir` | Sınır | Constraint | what the ayah or a reading does not say; prevents an overreading |
| `karsit` | Karşıt | Contrast | an opposite or counter-scene that sharpens the reading |
| `sonuc` | Sonuç | Consequence | why a distinction matters for understanding |
| `fazilet` | Fazilet | Merit | reports on the merit of a surah or ayah |
| `yapi` | Yapı | Structure | formal structure: ring, symmetry, rhyme groups, parallelism |

## `iliski`

| value | tr | en | definition |
|---|---|---|---|
| `dogrudan` | Doğrudan | Direct | the source explicitly treats this ayah or phrase (Bible pass: a text the scholarship reads as directly addressed by this ayah) |
| `tematik` | Tematik | Thematic | same theme, not an explanation of this ayah |
| `lafzi` | Lafzî | Lexical | linked through the same word, root or expression |
| `yapisal` | Yapısal | Structural | linked through position, sequence or form |
| `karsilastirmali` | Karşılaştırmalı | Comparative | a comparison across sources, readings or translations |

## `durum`

| value | tr | en | definition |
|---|---|---|---|
| `acik` | Açık | Explicit | stated in the cited source |
| `aktarilan` | Aktarılan | Reported | the source transmits it; its truth is not established |
| `tartismali` | Tartışmalı | Disputed | competing reports or positions |
| `cikarim` | Çıkarım | Inferred | inferred from evidence, not stated |
| `yorum` | Yorum | Interpretive | an interpretive synthesis (the base's or the block's) |
| `degerlendirilmedi` | Değerlendirilmedi | Not assessed | not checked against a source; required for model memory |

## `kat`

| value | tr | en | definition |
|---|---|---|---|
| `temel` | Temel | Core | shown by default: what an advanced reader should see first at that point |
| `ek` | Ek | Extended | shown by default: supporting detail |
| `arastirma` | Araştırma | Research | hidden by default (the reader opens it): audit trail, novelty detail, rejected candidates, technical source criticism |

## `guc`

| value | tr | en | definition |
|---|---|---|---|
| `dogrudan` | Doğrudan | Direct | direct support for the reading in context |
| `guclu` | Güçlü | Strong | a strongly illuminating link that is not the primary meaning |
| `ikincil` | İkincil | Resonant | a legitimate secondary resonance that keeps the primary meaning intact |
| `zayif` | Zayıf | Weak | possible but thinly constrained |
| `reddedildi` | Reddedildi | Rejected | considered and rejected |

## `klasik_tanik`

| value | tr | en | definition |
|---|---|---|---|
| `acik` | Açık | Explicit | the same connection is stated in a checked source |
| `kismi` | Kısmî | Partial | an important part is stated; the base adds the rest |
| `yapitaslari` | Yapıtaşları | Building blocks only | the ingredients are attested separately; the combination is not |
| `bulunamadi` | Bulunamadı | Not found | no parallel in the listed sources; never an absolute claim |

## `tarama`

| value | tr | en | definition |
|---|---|---|---|
| `dilim` | Âyet dilimi | Verse slice | only the per-ayah texts of this surah were searched; a negative result is weak |
| `tam` | Tam metin | Whole texts | whole-book texts were searched across the Qur'an |

## `derece`

| value | tr | en | definition |
|---|---|---|---|
| `sahih` | Sahih | Sound | sahih by the named authority |
| `hasan` | Hasen | Good | esbab only |
| `zayif` | Zayıf | Weak | esbab only |
| `mevzu` | Mevzû | Fabricated | esbab only |
| `ihtilafli` | İhtilaflı | Graders disagree | esbab only; name the graders |
| `degerlendirilmedi` | Değerlendirilmedi | Not graded | esbab only; no grade found |

## `tarihsellik`

| value | tr | en | definition |
|---|---|---|---|
| `sabit` | Sabit | Established | independently established |
| `muhtemel` | Muhtemel | Probable | probable |
| `belirsiz` | Belirsiz | Uncertain | uncertain |
| `tartismali` | Tartışmalı | Contested | competing reports |

## `kiraat_turu`

| value | tr | en | definition |
|---|---|---|---|
| `mutevatir` | Mütevâtir | Canonical | one of the canonical readings |
| `sazz` | Şâz | Non-canonical | a non-canonical reading |
| `sahabe` | Sahâbe kıraati | Companion reading | a reading reported from a Companion's codex, often explanatory |
| `belirsiz` | Belirsiz | Unclassified | standing not established |

## `kayip`

| value | tr | en | definition |
|---|---|---|---|
| `kelime` | Yanlış kelime | Wrong word | a different concept (ṣudūr rendered as kalp) |
| `eleman` | Düşen öge | Dropped element | a preposition, pronoun, number, emphasis, conjunction or voice the Turkish could have kept |
| `aralik` | Daralan anlam | Collapsed range | several live senses narrowed to one |
| `ekleme` | İşaretsiz ekleme | Unmarked addition | the translator's own words presented as the text |
| `kayma` | Türkçe kayma | Turkish drift | a loanword whose Turkish sense has shifted (namaz, din, ibadet) |
| `isaretleme` | İşaret değişimi | Marking change | brackets, italics or notes changed so an addition no longer looks like one |
| `aktarma` | Aktarma kayması | Relay drift | a difference that comes from translating an intermediate text (Asad's English, Mawdudi's Urdu), not the Arabic |

## `yon`

| value | tr | en | definition |
|---|---|---|---|
| `kayip` | Kayıp | Loss | the translation loses against the pole |
| `kazanc` | Kazanç | Gain | the translation recovers something against the pole |

## `kiyas`

| value | tr | en | definition |
|---|---|---|---|
| `arapca` | Arapça | Arabic | judged against the Arabic |
| `ara_metin` | Ara metin | Intermediate text | judged against the text it was translated from |

## `hata`

| value | tr | en | definition |
|---|---|---|---|
| `kaynak_etiketi` | Kaynak etiketi | Source label | a wrong source or lexicon label |
| `alinti` | Alıntı | Quotation | a misquoted text |
| `ayet_no` | Âyet numarası | Verse number | a wrong reference |
| `olgu` | Olgu | Fact | a factual error |
| `ceviri` | Çeviri | Rendering | a wrong rendering of the Arabic |

## `bag`

| value | tr | en | definition |
|---|---|---|---|
| `benzerlik` | Benzerlik | Similarity | the texts resemble each other; nothing is claimed about a relation (the default) |
| `ortak_havza` | Ortak havza | Shared milieu | both draw on a tradition current in Late Antiquity; no direction claimed |
| `muhatap` | Muhatap | Addressed | named scholarship argues the Qur'an addresses, answers or corrects this tradition; requires alim |
| `etki_iddiasi` | Etki iddiası | Dependence claim | named scholarship argues dependence; reported as that scholar's claim, never as fact; requires alim; impossible for a text dated after the Qur'an |

## `tarihleme`

| value | tr | en | definition |
|---|---|---|---|
| `kuran_oncesi` | Kur'an öncesi | Pre-Qur'anic | written down before the early 7th century |
| `cagdas` | Çağdaş | Contemporary | roughly contemporary with the Qur'an |
| `kuran_sonrasi` | Kur'an sonrası | Post-Qur'anic | redacted after the Qur'an (e.g. Pirqe de-Rabbi Eliezer); may preserve older material, which the block must argue |
| `belirsiz` | Belirsiz | Uncertain | dating disputed or unknown |

## `nusha`

| value | tr | en | definition |
|---|---|---|---|
| `masoretik` | Masoretik metin | Masoretic text | the Hebrew Bible (Westminster Leningrad Codex) |
| `septuaginta` | Septuaginta | Septuagint | the Greek Old Testament |
| `pesitta` | Peşitta | Peshitta | the Syriac Bible, Old and New Testament |
| `targum` | Targum | Targum | Aramaic renderings of the Hebrew Bible |
| `yunanca_ahit` | Yunanca Ahd-i Cedîd | Greek New Testament | the Greek New Testament |
| `diatessaron` | Diatessaron | Diatessaron | Tatian's gospel harmony, through its witnesses |
| `apokrif` | Apokrif | Apocrypha | Jewish pseudepigrapha or Christian apocrypha |
| `rabbani` | Rabbânî literatür | Rabbinic literature | Mishnah, Talmud, midrash |
| `patristik` | Kilise babaları | Church Fathers | Greek and Latin patristic writing |
| `suryani` | Süryânî literatür | Syriac literature | Syriac homilies and hymns (Ephrem, Jacob of Serugh, Narsai) |

## Rules

- **hadis_sahih**: tur:hadis requires derece:sahih and derece_veren naming Buhârî, Müslim or the graders recorded in the corpus; merit (fazilet) reports are hadith and follow the same rule; a weak Prophetic attribution of a sound Companion statement is reported as the Companion's (tefsir_rivayet)
- **hafiza**: kaynak:hafiza (or a corpus source with access hafiza) requires durum:degerlendirilmedi; forbidden for tur hadis and nuzul, for derece, and for Turkish loanword history in anlam_tarihi
- **itiraz_vs_tercih**: a source preferring another reading is islev:tercih; islev:itiraz needs an argument that the base's reading cannot hold here
- **yenilik_scope**: klasik_tanik:bulunamadi with tarama:dilim must say in metin that only the per-ayah slice was searched
- **modern_dictionaries**: modern Arabic dictionaries (VASIT, MUHIT, HANSWEHR) may be cited only in anlam_tarihi, as evidence of later drift
- **paragraf_zorunlu**: every block names its prose paragraph (paragraf) and quotes at least three words of it (capa); it is rendered right after that paragraph; a block whose number and words do not match is dropped
- **gelenek_ayrimi**: each block belongs to one gelenek and its tur must allow it. islami blocks cite no Bible, Jewish or Christian source (kind intertext); tevrat and incil blocks cite only sources of their own gelenek, plus the Qur'an text and modern scholarship. The passes run separately and never read each other's records
- **paralel_bagimlilik_degil**: a parallel is not a dependence: bag defaults to benzerlik; muhatap and etki_iddiasi require alim and a source that argues it; etki_iddiasi is impossible with tarihleme:kuran_sonrasi
- **yenilik_tek**: a separate yenilik block only when no antecedent was found, kat:arastirma, at most one per paragraph; an attested finding carries klasik_tanik/taranan/tarama on its oncul block
- **okuma_akisi**: blocks are read right after their paragraph: no 'taban' in metin (say şerh or state the point), no closing disclaimers, each point once on the page, at most five blocks after one paragraph
