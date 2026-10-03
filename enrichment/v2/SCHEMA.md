# Annotation schema 3.0 (generated from schema.json — do not edit)

Every block is one line in the rendered page and one JSON object in annotations.jsonl:

```
{id:"S107-HDS-001", tur:hadis, ayet:"107:6", islev:destek, iliski:tematik, durum:acik, kat:ek, derece:sahih, derece_veren:"Müslim", metin:"…", kaynak:"MUSLIM:2985"}
```

- Keys and values are ASCII-folded Turkish. The reader shows labels in Turkish, English or German from schema.json.
- Required in every block: id, tur, ayet, islev, iliski, durum, kat, metin, kaynak. Further fields are required by type (see below).
- `id` = S<surah, 3 digits>-<kod of the type>-<NNN>. `ayet` = this page's ayah or range ("107:1-3"; several with |).
- `kaynak` = corpus locators, pipe-separated, exactly as `tools/corpus.py` prints them, or `hafiza` (model memory).
- `metin` = one paragraph in the page language; at most 80 words (temel, ek) or
  120 (arastirma).
- Placement (records only, not rendered): `capa` = an exact sentence of the base of the page the record belongs to
  (the surah page or one ayah page; one call writes one page's records); without it the block goes to the end.

## Fields

| field | tr | en | required for | definition |
|---|---|---|---|---|
| `id` | Kimlik | ID | all | unique within the page |
| `tur` | Tür | Type | all | what kind of information the block carries Values: `tur` table. |
| `ayet` | Âyet | Verse | all | the ayah or range of this page the block is about: "107:3", "107:1-3"; several with \|. Other passages the block cites go in metin and kaynak, not here |
| `islev` | İşlev | Function | all | why the block stands at this point of the page Values: `islev` table. |
| `iliski` | İlişki | Relation | all | how the cited source relates to this ayah Values: `iliski` table. |
| `durum` | Durum | Status | all | epistemic status of the block's claim relative to its source Values: `durum` table. |
| `kat` | Katman | Layer | all | display layer Values: `kat` table. |
| `metin` | Metin | Text | all | the block's prose, in the page language, within the word limit of its layer |
| `kaynak` | Kaynak | Source | all | source locators, pipe-separated: <ID>:<locator> exactly as in the corpus (TAB:107:3, MUSLIM:2985, ELMALILI:107:2, LISAN:دعع), or "hafiza" for model memory |
| `guc` | Güç | Strength | tur: yenilik\|elenen\|ayet_ayet\|vucuh, islev: oncul | strength of a connection to the project's reading Values: `guc` table. |
| `klasik_tanik` | Klasik tanıklık | Classical attestation | tur: yenilik | how far a project finding is attested in the checked sources Values: `klasik_tanik` table. |
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

## `tur`

| value | kod | tr | en | definition |
|---|---|---|---|---|
| `tefsir_rivayet` | TRV | Rivâyet tefsiri | Transmitted exegesis | explanations of Companions/Successors as transmitted (Mujāhid, Muqātil, Ṭabarī's aqwāl, al-Durr al-manthūr) |
| `tefsir_dirayet` | TDR | Dirâyet tefsiri | Analytical exegesis | an exegete's own analysis: language, reasoning, theology (Zamakhsharī, Rāzī, Ibn ʿĀshūr, Elmalılı, Kur'an Yolu) |
| `isari` | ISR | İşârî tefsir | Allusive (Sufi) reading | ishārī readings (Qushayrī, Sulamī, Tustarī, Bursevî); labelled as such, never as dirayet |
| `nazm` | NZM | Nazım | Coherence | sequence, adjacency, surah unity, surah-to-surah relation; structural form (ring, symmetry, rhyme groups) with islev:yapi |
| `nuzul` | NZL | Nüzul | Revelation history | Makkī/Madanī, revelation order and chronology lists (Itqān, Ibn ʿĀshūr; Nöldeke, Neuwirth reported beside them) |
| `esbab` | ESB | Esbâb-ı nüzul | Occasion of revelation | isnād-bearing occasion reports of any grade, each with derece and tarihsellik shown |
| `hadis` | HDS | Hadis | Hadith | Prophetic hadith; sahih only (Bukhārī, Muslim, or sunan reports every named grader calls sahih) |
| `kiraat` | KRT | Kıraat | Reading | canonical and non-canonical readings and their linguistic justification (ḥujja) |
| `lugat` | LGT | Lugat | Lexicon | synchronic lexical evidence: senses, branches, the lexica's own wording and shawāhid |
| `vucuh` | VCH | Vücuh ve nezâir | Sense inventory | the senses a word takes across the Qur'an, from the wujūh wa-naẓāʾir books (Muqātil, Dāmghānī, Ibn al-Jawzī) and the usage table |
| `nahiv` | NHV | Nahiv | Grammar | syntax, iʿrāb, morphology that bears on meaning |
| `belagat` | BLG | Belâgat | Rhetoric | rhetoric, majāz, imagery, iʿjāz theory (Zamakhsharī, Jurjānī, Asās) |
| `ayet_ayet` | AYT | Âyetle tefsir | Qur'an by Qur'an | a Qur'anic passage that explains, extends or contrasts this one |
| `anlam_tarihi` | ANT | Anlam tarihi | Semantic history | diachronic change only: pre-Qur'anic → Qur'anic → later Arabic → Turkish loanword drift |
| `tarihi_baglam` | TBG | Tarihî bağlam | Historical setting | sourced setting: sīra, Mecca, material culture, institutions |
| `fikih` | FKH | Fıkıh | Law | legal readings; optional |
| `kelam` | KLM | Kelâm | Theology | theological debate; optional |
| `meal` | MEL | Meal incelemesi | Translation review | how Turkish (and relay) translations render a term: what they keep, lose or add |
| `modern` | MDR | Modern çalışma | Modern scholarship | modern Islamic and Western scholarship, kept apart from classical attestation |
| `yenilik` | YNL | Yenilik denetimi | Novelty audit | how far a finding of the base is attested in the checked sources |
| `elenen` | ELN | Elenen aday | Rejected candidate | a connection considered and rejected, kept for audit |
| `kaynak_notu` | KNT | Kaynak notu | Source note | source criticism: provenance, attribution, edition, isnād caveats |
| `yontem` | YNT | Yöntem notu | Method note | a methodological limit or distinction the reader needs here |
| `duzeltme` | DZT | Düzeltme | Erratum | an error in the frozen base: wrong label, quotation, ayah number, fact or rendering; also logged to errata.jsonl |

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
| `dogrudan` | Doğrudan | Direct | the source explicitly treats this ayah or phrase |
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
| `temel` | Temel | Core | shown whenever its type is shown |
| `ek` | Ek | Extended | supporting detail |
| `arastirma` | Araştırma | Research | audit trail: novelty, rejected candidates, technical source criticism |

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

## Rules

- **hadis_sahih**: tur:hadis requires derece:sahih and derece_veren naming Buhârî, Müslim or the graders recorded in the corpus
- **hafiza**: kaynak:hafiza (or a corpus source with access hafiza) requires durum:degerlendirilmedi; forbidden for tur hadis and nuzul, for derece, and for Turkish loanword history in anlam_tarihi
- **itiraz_vs_tercih**: a source preferring another reading is islev:tercih; islev:itiraz needs an argument that the base's reading cannot hold here
- **yenilik_scope**: klasik_tanik:bulunamadi with tarama:dilim must say in metin that only the per-ayah slice was searched
- **modern_dictionaries**: modern Arabic dictionaries (VASIT, MUHIT, HANSWEHR) may be cited only in anlam_tarihi, as evidence of later drift
- **intertext_excluded**: Bible and other non-Islamic scripture belong to the separate intertext pass; no block in this pass cites them
