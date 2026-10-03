# Enrichment resource review (conceptual, not a data audit)

Reviewer brief: does the planned resource set give an advanced Turkish reader everything needed to write their own tafsir of a surah, and does it let the project's latent-image analysis (v16) be integrated with the literature? Judged against NORTH_STAR.md, PRINCIPLES.md, the S107 v16 base, the S107 astra-max enrichment, and §13 of the old protocol. Scope assumed for the first production range: surahs 86–114.

Availability notes: "OpenITI: URI" means the URI appeared in the OpenITI books-by-length listing I checked today; "shamela" means found on shamela.ws by search; "unverified" means I could not confirm machine-readable text in a quick check.

---

## (A) Verdict

1. The plan is deep where the literature is already redundant (sixteen post-Ṭabarī tafsirs that reduce to about six voices) and thin exactly where the project's method lives: the early and maʿānī/gharīb layers, wujūh wa-naẕāʾir, al-Furūq, ḥujja/shādhdh qirāʾāt, ʿulūm al-Qurʾān lists, the bayānī school (Khūlī, Bint al-Shāṭiʾ, Quṭb), and Turkish tafsir (Elmalılı is absent).
2. The single most damaging omission for this reader is Elmalılı's Hak Dini Kur'an Dili: it is the Turkish antecedent of the project's lexical method and the ancestor of most meal word-choices, so both `oncul` and `meal` are crippled without it.
3. The antecedent/counter-evidence hunt for latent lexical images will fail if it runs only over tafsir: the real antecedent corpora are Abū ʿUbayda/Farrāʾ/Ibn Qutayba, the wujūh books, Māwardī/Ibn al-Jawzī enumerations, Zamakhsharī's Asās, Qushayrī, and Bint al-Shāṭiʾ; the real counter-evidence instruments are Furūq, Ibn ʿĀshūr/Abū Ḥayyān grammar, Maqāyīs's uṣūl statements, and loanword/comparative-Semitic data (Jeffery, Zammit, Sinai) against root-branch over-collapse.
4. The block-type list is sound; add `vucuh` and `isari`, narrow `itiraz` to argued exclusion (a classical preference is not counter-evidence), and expect `fikih` and `kelam` to be nearly empty in 86–114.
5. Several planned items are mislabelled or misdescribed: al-Rāghib's tafsir does not cover the late surahs; Nursi's İşârâtü'l-İ'câz covers only S1 and S2:1–33; Esed (TR) is a translation of Asad's English; modern Arabic dictionaries are drift detectors, not attestation; 81 rows of Jamhara is not a poetry corpus.

---

## (B) Assessment of current and planned resources

Legend: C = crucial, U = useful, M = marginal, X = unnecessary (for this reader and purpose).

### B1. Tafsir now local (86:17–114)

| Resource | Verdict | Why; role notes |
|---|---|---|
| al-Ṭabarī | C | The early layer's index; aqwāl with isnād; lexical glosses with poetry. Primary for `tefsir_rivayet`, `esbab`, `kiraat` (companion readings), `lugat` antecedents. |
| al-Māwardī, al-Nukat wa'l-ʿuyūn | C (under-rated) | Numbered wujūh per phrase without choosing: the classical form closest to the project's no-disambiguation rule. Best single `oncul` source among the local set. |
| al-Zamakhsharī | C | Majāz-aware, images, rhetoric, grammar; pair with Asās al-balāgha (he marks which senses were felt as figurative). `belagat`, `nahiv`, `oncul`/`itiraz`. |
| al-Rāzī | C | Enumerated wujūh, munāsaba (the pre-Biqāʿī naẕm), kalām, and he preserves Abū Muslim al-Iṣfahānī and other lost Muʿtazilī views. `nazm`, `kelam`, `oncul`. |
| al-Qurṭubī | C | Lugha + fiqh + aqwāl; the fiqh voice for the few legal items in 86–114. |
| Abū Ḥayyān, al-Baḥr | C | The grammar and qirāʾāt compendium; the main `itiraz` source on syntax. Mislabel risk: do not use him for rivāya. |
| al-Biqāʿī, Naẕm al-durar | C | The naẕm backbone; note he transmits al-Ḥarāllī and Ibn al-Zubayr al-Gharnāṭī; cite those where he does. |
| Ibn ʿĀshūr | C | Modern bayānī: maqāṣid, iʿjāz, careful grammar; the most frequent `itiraz` in the S107 sample (ruʾya baṣariyya). |
| Ibn ʿAṭiyya | U | Independent Andalusian judgement, concise; useful where Qurṭubī/Abū Ḥayyān lean on him. |
| al-Suyūṭī, al-Durr al-manthūr | U | A compilation, not the early layer; use as an index pointing to Ibn Abī Ḥātim, ʿAbd b. Ḥumayd, Saʿīd b. Manṣūr, then quote them. Mislabel risk: "rivayet" by proxy. |
| al-Ālūsī | U/M | Compiles Rāzī, Abū Ḥayyān, Bursevî, plus ishārī tail; valuable mainly as a bridge to the ishārī reading if Bursevî is not loaded. |
| Ibn Kathīr | M | Redundant with Ṭabarī + Durr; keep only for his hadith grading remarks. |
| al-Bayḍāwī, al-Nasafī | M | Abridgements of Zamakhsharī; the reader gains nothing new. Load on demand. |
| al-Baghawī | M | Abridgement of Thaʿlabī; load Thaʿlabī instead (lexical and ishārī content Baghawī dropped). |
| al-Wāḥidī (Wasīṭ/Wajīz) | M as loaded | His Asbāb (planned) and al-Basīṭ (planned, full) are the valuable works; Wasīṭ/Wajīz add nothing. |

Net: the core eight (Ṭabarī, Māwardī, Zamakhsharī, Rāzī, Qurṭubī, Abū Ḥayyān, Biqāʿī, Ibn ʿĀshūr) carry the information; the other eight add reading cost and, per NORTH_STAR's own finding that bulk input dilutes synthesis, should be on-demand rather than default.

### B2. Hadith now local

| Resource | Verdict | Why |
|---|---|---|
| Bukhārī, Muslim | C | The sahih-only policy's base. |
| Abū Dāwūd, Tirmidhī, Nasāʾī, Ibn Māja | U | Needed for "sahih per named grader"; make sure grader verdicts (Albānī/Arnāʾūṭ on sunnah.com) are in the index, otherwise the policy is unenforceable. |
| Mālik | M | Rarely touches 86–114. |
| Missing: Musnad Aḥmad (with Arnāʾūṭ grading), Ibn Ḥibbān, Ḥākim | should | Many tafsir-relevant reports (asbāb, faḍāʾil of short surahs, the Prophet's recitation of 87/88 in ʿĪd and Jumuʿa prayers, 112 = a third of the Qur'an) live here with graded isnāds. Without them the `hadis` block for short surahs will be thin and the `esbab` block will quote ungraded reports from tafsir instead. |

### B3. Lexica now local

| Resource | Verdict | Why; role notes |
|---|---|---|
| Project dictionary (6 lexica, every branch) | C | The guard and supplier. For enrichment, add one thing it must expose: whether a branch's lexicon entry itself cites a Qur'anic ayah (Lisān and Mufradāt do this constantly). That is the cheapest `oncul` check. |
| al-ʿAyn, Jamhara, Tahdhīb, Ṣiḥāḥ, Maqāyīs, Mufradāt full texts | C | Maqāyīs's aṣl statements are both antecedent and counter-evidence for the "branches are facets of one concept" move (Ibn Fāris often posits two or three uṣūl). |
| Lisān al-ʿArab | C | The shawāhid and the Qur'anic citations under each sense. |
| Asās al-balāgha | C | Zamakhsharī's literal/figurative partition; direct evidence of which secondary senses were heard as images by a 12th-c. ear. |
| Lane | U | For English rendering later; his Tāj-derived material is useful. |
| al-Qāmūs | M | Covered by Lisān; Tāj al-ʿArūs (missing) would add more than al-Qāmūs does. |
| al-Wasīṭ, Muḥīṭ al-Muḥīṭ, Hans Wehr | M, mislabel risk | Modern Arabic. Use only as drift detectors (a sense present here and absent from the six classical lexica is modern), never as attestation. Say so in the source registry. |
| Sībawayh | M | Grammar antecedents reach the reader through Abū Ḥayyān/Samīn; raw Sībawayh will not be read. |
| Jamharat ashʿār al-ʿArab (81 rows) | X as is | Not a corpus. Replace with a real pre-Islamic/early poetry set (see C). |
| Majāz al-Qurʾān vol. 1 | C, incomplete | Vol. 2 (planned) is the one that covers 86–114; must. |
| QAC morphology, lemma usage | C | The "Quran-loaded word" claims rest on this. |
| Qirāʾāt table (small) | insufficient | See C: Ibn Mujāhid, ḥujja works, Muḥtasab. |

### B4. Planned

| Resource | Verdict | Why |
|---|---|---|
| Wāḥidī Asbāb; Suyūṭī Lubāb | C | The right asbāb sources (OpenITI: 0468IbnAhmadWahidiNaysaburi.AsbabNuzul; 0911Suyuti.LubabNuqul). Note the `historicity` field must survive: most asbāb for 86–114 are mursal or disputed. |
| Majāz vol. 2; Farrāʾ Maʿānī | C | The oldest concrete-image glosses; primary `oncul` corpus for latent readings. (OpenITI: 0207IbnZiyadFarra.MacaniQuran.) |
| Zajjāj Maʿānī; Ibn Qutayba Gharīb | C (upgrade from "maybe") | Zajjāj is the grammatical mediator between Farrāʾ and Wāḥidī; Ibn Qutayba's Gharīb and Taʾwīl mushkil al-Qurʾān are the first systematic treatment of majāz and of wujūh in the Qur'an. (OpenITI: 0311IbnSariZajjaj.MacaniQuran; 0276IbnQutaybaDinawari.GharibQuran; .TawilMushkilQuran.) |
| Full-Qur'an texts of core tafsirs | C | Without them `yenilik` cannot be declared against a corpus and cross-Qur'an `oncul` search is impossible. Add Māwardī, Abū Ḥayyān, Samīn al-Ḥalabī al-Durr al-maṣūn, Ibn ʿAṭiyya to the list. Remove al-Rāghib's tafsir (survives only for the opening surahs; it does not reach 86–114; his Mufradāt is already in). |
| Wāḥidī al-Basīṭ | C | The lexical and grammatical mine (quotes Farrāʾ, Zajjāj, Abū ʿAlī al-Fārisī, Ibn al-Anbārī, Thaʿlab); far more valuable than the Wasīṭ now loaded. shamela (Imam Univ. edition); OpenITI unverified. |
| Kur'an Yolu (Diyanet) | U | The Turkish reader's default modern reference; moderate and synthesising; weak on lexicon. Its notes often record what the meal team decided and why: feed `meal`. Digital: kuran.diyanet.gov.tr; Diyanet open API (acikkaynakkuran-dev.diyanet.gov.tr) exposes meal; tafsir text via API unverified. |
| Meal panel (16) | C, adjust | Good core. Adjust: (a) Diyanet İşleri current, Diyanet Vakfı and Kur'an Yolu meal are one lineage; keep all three but mark lineage so agreement among them is not counted as independent consensus. (b) Esed (TR) is a translation of Asad's English: label it as the English-mediated witness. (c) Add Mustafa Öztürk, Anlam ve Yorum Merkezli Çeviri (must: the most explicitly meaning-centred paraphrase; it shows collapse most clearly). (d) Add Hüseyin Atay's later solo meal (should: co-author of the 1961 Diyanet; his own later choices expose what the 1961 compromise cost). (e) Add one literal English control (Arberry) so "what all meals lose" can be separated from "what any translation loses". (f) Elmalılı sadeleştirilmiş variants are what readers actually hold; keep original as the witness but note the drift in the simplified editions as `anlam_tarihi` material. Aggregator: kuranmeali.com has most panel members side by side (Elmalılı orijinal, Bilmen, Çantay, Ateş, Bulaç, Esed, Öztürk, İslamoğlu, Okuyan, Gölpınarlı, Süleymaniye, Hayrat, Diyanet eski/yeni); the 1961 Atay–Kutluay edition was not visibly listed there (unverified). |

---

## (C) Missing resources by priority

### C1. MUST

| Resource | What it adds for this reader | Feeds | Availability |
|---|---|---|---|
| Elmalılı, Hak Dini Kur'an Dili (original text) | The Turkish lexical-exegetical antecedent: he does root-and-usage digressions in Turkish, and his meal is the ancestor of most panel choices. Both `oncul` and the meal review need him. | tefsir_dirayet, lugat, meal, anlam_tarihi, yenilik(oncul) | Scans on archive.org (Cündioğlu edition; 10-vol. original); YEK e-kitap (ekitap.yek.gov.tr). Per-ayah sadeleştirilmiş text exists on several meal sites; machine-readable original text unverified (likely needs OCR). |
| Early exegetical layer: Mujāhid; Muqātil b. Sulaymān, Tafsīr; ʿAbd al-Razzāq; Ibn Abī Ḥātim; Yaḥyā b. Sallām | Earliest attested senses (2nd c. AH) before the lexica were compiled; a sense attested here is an antecedent that outranks any later lexicon; a sense absent here is a flag. Yaḥyā b. Sallām is the oldest full lexical tafsir. | tefsir_rivayet, anlam_tarihi, yenilik | OpenITI: 0150MuqatilIbnSulayman.TafsirMuqatil; 0255CabdRazzakSancani.Tafsir; 0327IbnAbiHatimRazi.Tafsir; 0200YahyaIbnSalam.Tafsir; Mujāhid: shamela. |
| Wujūh wa-naẕāʾir: Muqātil al-Wujūh; al-Dāmghānī Iṣlāḥ al-wujūh; Ibn al-Jawzī Nuzhat al-aʿyun | The classical form of "a word through all its Qur'anic uses": the sense inventory per lemma with ayah lists. This is the project's method in its 8th–12th c. form; every `yenilik` claim about a Qur'an-loaded word must be checked here first. | vucuh (new), ayet_ayet, anlam_tarihi, yenilik | Dāmghānī and Ibn al-Jawzī: shamela (unverified OpenITI URIs); Muqātil Wujūh: printed (ed. Shiḥāta), digital unverified. |
| Abū Hilāl al-ʿAskarī, al-Furūq al-lughawiyya | Near-synonym distinctions (qalb/ṣadr/fuʾād; faqīr/miskīn; khawf/khashya). The ṣudūr→"kalp" judgement needs exactly this to be a judgement and not a taste. | lugat, meal, itiraz | OpenITI: 0395AbuHilalCaskari.FuruqLughawiyya. |
| ʿUlūm al-Qurʾān: al-Suyūṭī al-Itqān; al-Zarkashī al-Burhān | The actual lists (nuzūl order, makkī/madanī with disputed cases, wujūh chapter, munāsabāt, fawāṣil) so `nuzul` does not rest on memory. | nuzul, nazm, kiraat, yontem | OpenITI: 0911Suyuti.Itqan; 0794BadrDinZarkashi.BurhanFiCulumQuran. |
| Qirāʾāt: Ibn Mujāhid al-Sabʿa; one ḥujja work (Ibn Khālawayh or Abū ʿAlī al-Fārisī); Ibn Jinnī al-Muḥtasab (shādhdh) | Meaning-bearing variants with their linguistic justification; shādhdh readings are where companions disambiguated toward a secondary sense, which is either an antecedent or counter-evidence for a latent image. | kiraat, oncul/itiraz | OpenITI: 0324IbnMusaBaghdadi.SabcaFiQiraat (Ibn Mujāhid); 0370IbnAhmadIbnKhalawayh.HujjaFiQiraatSabca; 0377IbnAhmadFarisi.HujjaLiQurraSabca; 0392IbnJinniMawsili (Muḥtasab listed under a variant title). |
| Bint al-Shāṭiʾ, al-Tafsīr al-bayānī (2 vols) | Method-identical antecedent; she covers 14 short surahs, almost all inside 86–114 (93, 94, 99, 100, 102, 103, 104, 107, 89, 90, 92, 96, 68, 73). The `yenilik` audit of this range is incomplete without her. Plus Khūlī, Manāhij tajdīd for the `yontem` block. | tefsir_dirayet, lugat, belagat, yenilik | shamela likely; OpenITI unverified. |
| al-Ṭabrisī, Majmaʿ al-bayān | Per pericope: lugha / iʿrāb / qirāʾa / nuzūl / maʿnā, in exactly the block structure planned; preserves Muʿtazilī views (Jubbāʾī, Abū Muslim). The cleanest non-Sunni voice, and more useful to this reader than al-Mīzān. | lugat, nahiv, kiraat, tefsir_dirayet | OpenITI: 0548IbnHasanTabarsi.TafsirMajmacBayan. |
| Muḥammad ʿAbduh, Tafsīr juzʾ ʿAmma | Covers exactly 78–114; the reformist reading for this range (al-Manār stops at 12:107 and is irrelevant here). | modern, tefsir_dirayet | shamela (unverified). |
| TDV İslâm Ansiklopedisi (islamansiklopedisi.org.tr) | Per-surah articles (names, nuzul, disputes, faḍāʾil hadith with grading), per-term articles for the Turkish theological vocabulary (KALP, NAMAZ, İBADET, DİN…), per-author articles for every source in the registry. Free, HTML, Turkish, reliable. | nuzul, tarihi_baglam, hadis, kaynak_notu, anlam_tarihi | Free web; HTML per article. |
| Turkish loanword history: Nişanyan Sözlük; Kubbealtı Lugati; TDK Tarama Sözlüğü | Without these, "Turkish loanword drift" claims (ibadet, âlem, salât, kalp) are memory. Nişanyan gives first Turkish attestation and sense; Tarama shows Old Anatolian Turkish senses. | anlam_tarihi, meal | Nişanyan: free web; Kubbealtı: free web (lugatim.com); Tarama: TDK web. |

### C2. SHOULD

| Resource | What it adds | Feeds | Availability |
|---|---|---|---|
| al-Akhfash, Maʿānī; al-Naḥḥās, Iʿrāb al-Qurʾān; al-Samīn al-Ḥalabī, al-Durr al-maṣūn and ʿUmdat al-ḥuffāẕ | Completes the maʿānī/iʿrāb chain; Samīn's ʿUmda is a Qur'anic lexicon on the Rāghib model with more branches. | nahiv, lugat | OpenITI: 0215AkhfashAwsat.MacaniQuran; 0338AbuJacfarNuhhas.IcrabQuran; Samīn: shamela. |
| Ibn al-Jawzī, Zād al-masīr; al-Thaʿlabī, al-Kashf wa'l-bayān | Zād: numbered aqwāl per word (Māwardī's form, later and fuller). Thaʿlabī: lexical, ishārī and poetic material that Baghawī removed. | tefsir, lugat, oncul | shamela; quran-tafsir.net lists ~50 works (Thaʿlabī likely present; verify). |
| Naẕm: Ibn al-Zubayr al-Gharnāṭī, al-Burhān fī tanāsub suwar al-Qurʾān; al-Suyūṭī, Tanāsuq al-durar; Farāhī, Niẕām al-Qurʾān (Arabic fragments; his Tafsīr of short surahs); Iṣlāḥī, Tadabbur-i Qurʾān (English tr. online for many surahs) | Surah-junction naẕm independent of Biqāʿī; Farāhī/Iṣlāḥī's surah pairs and ʿamūd are the modern naẕm system the reader will meet in English literature. | nazm | Gharnāṭī, Tanāsuq: shamela (unverified OpenITI). Iṣlāḥī EN: tadabbur-i-quran.org (web). Farāhī: Arabic edition exists; digital unverified. |
| Cuypers, articles on the structure of sūras 81–114 (Annales Islamologiques / MIDEO) and The Composition of the Qur'an; Farrin, Structure and Qur'anic Interpretation; Neuwirth, Der Koran Bd. 1 (Frühmekkanische Suren) | Formal structure (ring, symmetry, verse-form, rhyme groups) for exactly this range; Neuwirth's volume is a full commentary on early Meccan surahs with verse-structure analysis. | nazm (structural sub-role), belagat | Cuypers' articles: IFAO/Persée (open access likely; unverified per article); books licensed. Farrin PDF circulates; Neuwirth licensed (German). |
| Sayyid Quṭb, al-Taṣwīr al-fannī and Fī ẕilāl (late surahs) | The "image" vocabulary (taṣwīr, takhyīl) in modern Arabic criticism; Fī ẕilāl's late-surah sections are strongly scenic. | belagat, tefsir_dirayet, oncul | Fī ẕilāl is already on quran-tafsir.net; Taṣwīr: shamela/archive (unverified). |
| ʿAbd al-Qāhir al-Jurjānī, Dalāʾil al-iʿjāz and Asrār al-balāgha | The theory behind the project's "image": takhyīl, majāz, and naẕm as word-order meaning. Gives `belagat` blocks a vocabulary and gives `itiraz` a test (is this a majāz the language licenses, or a pun?). | belagat, yontem | shamela; OpenITI listing did not show it (unverified). |
| Ishārī: al-Qushayrī, Laṭāʾif al-ishārāt; Ismāʿīl Ḥakkı Bursevî, Rūḥ al-bayān | Qushayrī's hermeneutic is literally the North Star's "the thirsty hear water, the lost hear guidance"; the ishārī tradition is the historical home of state-dependent reading and will yield both `oncul` and `itiraz`. Bursevî is Ottoman, compiles Taʾwīlāt Najmiyya and Persian material, and is the Turkish reader's own tradition. | isari (new), oncul | Qushayrī: OpenITI 0465IbnHawazinQushayri.LataifIsharat; also on quran-tafsir.net. Bursevî Arabic: shamela (unverified); Turkish translation (Hilmi, 10 vols) in print; scans partial. |
| al-Sulamī, Ḥaqāʾiq; al-Tustarī | Earliest ishārī readings; short entries; occasionally the only early witness to a secondary sense. | isari | OpenITI: 0412Sulami.Tafsir; 0283SahlTustari.Tafsir. |
| al-Ṭabāṭabāʾī, al-Mīzān | The strongest systematic Qur'an-by-Qur'an (tafsīr al-Qurʾān bi'l-Qurʾān) practice; feeds `ayet_ayet` with argued, not merely associative, parallels. | ayet_ayet, kelam | Arabic full text online (almizan.org-type sites; altafsir.com); machine-readable unverified. |
| Süleyman Ateş, Yüce Kur'an'ın Çağdaş Tefsiri; Ö. N. Bilmen, Kur'anı Kerim'in Türkçe Meali Âlisi ve Tefsiri | Ateş's tafsir explains his meal and is lexically alert; Bilmen's short tafsir explains his meal's choices. Both make the meal review evidence-based rather than taste-based. | meal, tefsir_dirayet | Ateş: archive.org (11 vols, scans); ayet.online has Ateş per ayah (web). Bilmen: scans; per-ayah web text exists on meal sites (unverified). |
| Musnad Aḥmad (Arnāʾūṭ grading); Ibn Ḥibbān | See B2. | hadis, esbab | sunnah.com has Musnad with grading (web/JSON dumps exist); OpenITI: 0241IbnHanbal.Musnad (ungraded). |
| Sīra: Ibn Hishām; Hishām b. al-Kalbī, Kitāb al-Aṣnām; al-Azraqī, Akhbār Makka | Meccan setting of 86–114: the named opponents (Abū Lahab, Walīd b. Mughīra, al-ʿĀṣ b. Wāʾil, Umayya b. Khalaf), Quraysh's trade (S106), the Kaʿba, the horses and raids (S100). Cross-checks asbāb names. | tarihi_baglam, esbab | OpenITI: Ibn Hishām (0218); Aṣnām and Azraqī: shamela. |
| Arthur Jeffery, Foreign Vocabulary of the Qur'an; Zammit, Comparative Lexical Study of Qur'anic Arabic; Sinai, Key Terms of the Qur'an | Counter-evidence against root-branch over-collapse: when a Qur'anic word is a loan or a distinct Semitic lexeme (ṣalāt, zakāt, dīn, miskīn), "every attested branch of the root" mixes two words. Also the pre-Qur'anic sense that Turkish then drifted from a second time. | anlam_tarihi, itiraz, modern | Jeffery (1938): public domain, archive.org. Zammit, Sinai: licensed (Sinai is on JSTOR). |
| Badawi & Abdel Haleem, Dictionary of Qur'anic Usage | Per-occurrence sense grouping of every Qur'anic lemma: a modern wujūh book in English; direct check for "Quran-loaded word" claims. | lugat, meal, ayet_ayet | Licensed (Brill). |
| Nöldeke–Schwally chronology (GdQ; EN tr. 2013); Corpus Coranicum chronology (Neuwirth's early/middle/late Meccan) | The two Western chronologies as a table per surah, set beside the Islamic nuzūl lists (Itqān; Ibn ʿĀshūr's numbering) so the `nuzul` block reports disagreement, not a date. | nuzul | Corpus Coranicum: web, per surah (corpuscoranicum.de; API unverified). GdQ EN: licensed; German original public domain (archive.org). |
| A real poetry set: Muʿallaqāt, Mufaḍḍaliyyāt, Aṣmaʿiyyāt, Ḥamāsa (replacing the 81-row Jamhara) | Attestation of a sense in pre-Islamic usage; the shawāhid behind the lexica's branches. | lugat, anlam_tarihi | OpenITI holds many dīwāns and anthologies (URIs unverified); aldiwan.net web. |
| Tāj al-ʿArūs | Aggregates Lisān + Qāmūs with additions and corrections. | lugat | shamela; OpenITI (unverified). |

### C3. COULD

| Resource | What it adds | Feeds | Availability |
|---|---|---|---|
| Ibn Khālawayh, Mukhtaṣar fī shawādhdh al-Qurʾān; Ibn al-Jazarī, al-Nashr | Complete shādhdh list; ten-reader transmission detail. | kiraat | shamela. |
| al-Khaṭṭābī, Bayān iʿjāz; al-Bāqillānī, Iʿjāz al-Qurʾān; al-Rummānī, al-Nukat | Early iʿjāz theory; mostly for the `yontem` block. | belagat, yontem | shamela (not in OpenITI listing). |
| Qāshānī (attrib. Ibn ʿArabī), Taʾwīlāt; al-Ḥākim al-Jishumī al-Tahdhīb (Zaydī-Muʿtazilī); Hūd b. Muḥakkam (Ibāḍī, abridges Yaḥyā b. Sallām); Qāḍī ʿAbd al-Jabbār, Tanzīh al-Qurʾān | Non-mainstream voices for rare cases; Jishumī's edition is recent. | isari, kelam | Varies; Jishumī recent print; Hūd: printed; digital unverified. |
| Ahkām al-Qurʾān (Jaṣṣāṣ, Ibn al-ʿArabī al-Mālikī, Kiyā al-Harrāsī) | Legal readings; nearly nothing in 86–114 that Qurṭubī does not cover. | fikih | shamela. |
| Darwīsh, Iʿrāb al-Qurʾān wa-bayānuh; Ṣāfī, al-Jadwal | Full per-word parse as a convenience; not evidence. | nahiv | shamela. |
| Abū al-Suʿūd, Irshād; Konyalı Mehmed Vehbi, Hulâsatü'l-Beyan; Nursi (Sözler passages on 103, 112, 113) | Ottoman and republican Turkish readings for colour; Nursi's İşârâtü'l-İ'câz itself is irrelevant to 86–114. | tefsir_dirayet, modern | Abū al-Suʿūd: shamela; Nursi: erisale.com, GitHub (alitekdemir/Risale-i-Nur-Diyanet). |
| Encyclopaedia of the Qur'an; The Study Quran; Ambros, Concise Dictionary | Reference; EQ entries per concept are good `modern` summaries. | modern | Licensed. |
| Epigraphy (OCIANA, DASI); Biblical/Syriac parallels (Corpus Coranicum intertexts); rasm (al-Dānī al-Muqniʿ; Corpus Coranicum manuscripts) | Rarely decisive in 86–114 (S95 Sinai, S105, S112); Sinai's Key Terms already distils the epigraphy. | anlam_tarihi, tarihi_baglam, kiraat | Web; Corpus Coranicum intertexts per ayah (web). |

---

## (D) Non-mainstream traditions worth including, and what each uniquely shows

- **Ishārī (Qushayrī, Sulamī, Tustarī, Bursevî).** The only classical tradition that institutionalised state-dependent hearing of a word, which is the North Star's own model of how a latent image is "audible to a reader in a condition." It shows (a) that the layered-meaning claim has a thousand-year history, and (b) where that history went wrong (allegory detached from the lexicon). Both are needed: the first as `oncul`, the second as the boundary the project's dictionary-guard draws. Bursevî specifically shows the Ottoman reader's inheritance, which is the Turkish reader's inheritance.
- **Muʿtazilī voices (Zamakhsharī; Abū Muslim al-Iṣfahānī and Jubbāʾī via Rāzī and Ṭabrisī; Jishumī).** They refuse the asbāb-driven narrowing of general statements and read the Qur'an as rational argument; for 86–114 they are the voices that keep "the one who denies the dīn" general rather than a named Meccan. Useful `itiraz` against over-historicising and `oncul` for the project's refusal to pin a verse to one person.
- **Imāmī (Ṭabrisī; Ṭabāṭabāʾī).** Ṭabrisī: structure and preservation of lost views. Ṭabāṭabāʾī: disciplined Qur'an-by-Qur'an, the strongest external check on `ayet_ayet` parallels that are merely associative.
- **Bayānī school (Khūlī, Bint al-Shāṭiʾ, Quṭb's Taṣwīr).** Literally the project's declared ancestry; Bint al-Shāṭiʾ's corpus overlaps this range. She also provides the method's own self-criticism: she insists on one Qur'anic sense per word in context, which is a principled `itiraz` to no-disambiguation. The reader should see that argument stated by its best proponent.
- **Naẕm school (Biqāʿī, Gharnāṭī, Farāhī, Iṣlāḥī; Cuypers, Farrin, Neuwirth on form).** Shows the surah as a composed unit; the modern formal work (ring, symmetry, rhyme groups) is the only tradition that makes a claim about the surah's shape that can be checked against the text without any lexical commitment, so it is the ideal independent corroboration (or not) of the project's image chains.
- **Ibāḍī (Hūd b. Muḥakkam) and Zaydī (Jishumī).** Marginal; include only as transmitters of early material (Hūd preserves Yaḥyā b. Sallām).
- **Ottoman/Turkish (Elmalılı, Bursevî, Abū al-Suʿūd, Bilmen, Ateş).** For this reader not "non-mainstream" but home ground; Elmalılı is the only one that is methodologically an antecedent rather than a reference.

---

## (E) Antecedents, counter-evidence, and the meal review

### E1. Finding `oncul` for latent lexical images (ranked by yield)

1. Maʿānī/gharīb layer: Abū ʿUbayda, Farrāʾ, Ibn Qutayba, Zajjāj, Wāḥidī al-Basīṭ. They gloss with the concrete image and the poetic line; an "aha" that exists in the literature exists here first.
2. Wujūh wa-naẕāʾir (Muqātil, Dāmghānī, Ibn al-Jawzī): the inventory of senses per lemma across the Qur'an.
3. Enumerators: Māwardī, Ibn al-Jawzī Zād, Rāzī's wujūh lists, Ṭabrisī.
4. Lexica that cite ayahs under a branch: Lisān, Mufradāt, Samīn's ʿUmda, Asās (the project dictionary should expose this flag).
5. Zamakhsharī and Jurjānī for images recognised as majāz.
6. Qushayrī, Sulamī, Bursevî for state-dependent hearing.
7. Bint al-Shāṭiʾ, Quṭb, Ibn ʿĀshūr, Elmalılı for modern literary and Turkish antecedents.
8. Early layer (Mujāhid, Muqātil, ʿAbd al-Razzāq, Ibn Abī Ḥātim) for a sense's first attestation, and Ṭabarī as index.

### E2. Finding `itiraz` (argued exclusion, not mere preference)

- Grammar and context: Ibn ʿĀshūr, Abū Ḥayyān, Samīn al-Ḥalabī, Zamakhsharī (e.g., the verb pattern, the particle, transitivity that blocks an activation).
- Near-synonymy: Abū Hilāl's Furūq (if the Qur'an chose ṣadr over qalb for a reason, the image proposed must respect that reason).
- Root integrity: Maqāyīs's uṣūl (two uṣūl means two concepts); Jeffery/Zammit/Sinai for loans and homonymous roots (ṣ-l-w "prayer" is not the ṣ-l-w of the racer's second place in the same lexeme sense; the dictionary's branch list will contain both).
- Qirāʾāt and ḥujja: a canonical reading or its justification that forecloses the secondary sense.
- QAC usage counts: the "recurring role" claim can be falsified by the usage table.
- Bint al-Shāṭiʾ's one-sense-in-context principle as the strongest methodological `itiraz`.

Rule to write into the schema: a classical "al-ṣaḥīḥ huwa X" is `tercih` (preference), not `itiraz`; `itiraz` requires an argument that the secondary sense cannot be activated here.

### E3. The meal review

- Which meal conveys the meaning best: needs Mufradāt, Furūq, Badawi–Abdel Haleem for the Arabic side; Elmalılı's tafsir, Bilmen's tafsir, Ateş's tafsir, Kur'an Yolu notes for the Turkish side (translators explaining their own choices).
- What all meals lose in common: dropped particles (fa-, inna, la-), collapsed ranges (yadʿʿu → "iter"), unmarked additions, loanword drift. Grammatical references: Farrāʾ/Zamakhsharī/Ibn ʿĀshūr on the particle or construction are sufficient; a modern iʿrāb (Darwīsh) is only a convenience. No separate grammar textbook is needed.
- Loanword drift (ṣudūr→"kalp", ibadet, âlem): needs Nişanyan, Kubbealtı, Tarama Sözlüğü, TDV İA term articles, and Jeffery for the Arabic word's own earlier loan history. This is `anlam_tarihi`, not `meal`; the `meal` block should only state the consequence for the translation.
- A literal English control (Arberry) distinguishes Turkish-specific loss from universal loss.

---

## (F) Block-type changes

Add:
- `vucuh` (wujūh wa-naẕāʾir): the sense inventory of a lemma across the Qur'an with the classical lists; distinct from `ayet_ayet` (thematic parallel) and from `lugat` (lexicon branch). It is the primary antecedent instrument and will be dense.
- `isari`: ishārī reading, separately labelled so it is neither mislabelled `tefsir_dirayet` nor dropped. It is the tradition closest to the project's own stance and the reader should see it as such.
- Role `tercih` (classical preference) distinct from `itiraz` (argued exclusion). Role `tasnif` for a source that lists senses without choosing (Māwardī, Ibn al-Jawzī): it supports the no-disambiguation principle itself.
- Keep the old `classical_attestation` gradation (explicit / partial / building_blocks_only) inside `yenilik`; it was the most honest part of the old schema.

Merge or narrow:
- `anlam_tarihi` vs `lugat`: reserve `anlam_tarihi` for diachronic claims (pre-Qur'anic → Qur'anic → post-Qur'anic Arabic → Turkish loan); everything synchronic goes to `lugat`. Loanword drift lives here, not in `meal`.
- `esbab` vs `tarihi_baglam` vs `nuzul`: keep all three but define: `nuzul` = chronology and makkī/madanī lists (Itqān, Ibn ʿĀshūr, Nöldeke, Corpus Coranicum, reported together); `esbab` = isnād-bearing occasion reports with `historicity`; `tarihi_baglam` = setting from sīra, akhbār Makka, epigraphy.
- `nazm`: add a structural sub-role (ring/symmetry/rhyme groups from Cuypers, Farrin, Neuwirth) so formal and semantic coherence are not conflated.
- `hadis`: add role `fazilet` for surah-virtue reports (most hadith for short surahs are of this type) and make the sahih-only rule apply to `hadis` while `esbab` carries graded weaker reports under `historicity`.

Expect to be nearly empty in 86–114: `fikih` (S107 māʿūn/zakat, S108 naḥr, S96 and S87 sajda at most) and `kelam` (S112, S97, S91, S87). Keep them optional rather than required per surah.

---

## (G) Things in the plan I think are mistakes

1. Sixteen tafsirs for 86–114 when the North Star's own evidence says bulk input dilutes synthesis. Baghawī, Nasafī, Bayḍāwī, Ibn Kathīr, Ālūsī and the Wāḥidī Wasīṭ add almost no information beyond Ṭabarī, Māwardī, Zamakhsharī, Rāzī, Qurṭubī, Abū Ḥayyān, Biqāʿī and Ibn ʿĀshūr. Make them on-demand.
2. al-Rāghib's tafsir in the full-Qur'an list: it does not cover the late surahs. His Mufradāt (already present) is the relevant work.
3. Nursi's İşârâtü'l-İ'câz as a Turkish tafsir source: it covers only S1 and S2:1–33.
4. Jamharat ashʿār al-ʿArab at 81 rows presented as a poetry corpus.
5. No Elmalılı. For a Turkish reader and a meal review this is the largest single gap.
6. Modern Arabic dictionaries (Wehr, al-Wasīṭ, Muḥīṭ al-Muḥīṭ) listed as lexica without a role: they must be marked "drift detectors only", or they will be cited as attestation.
7. The antecedent search planned as full-Qur'an tafsir only. The antecedents of latent lexical images are in maʿānī/gharīb, wujūh, Furūq and the lexica's own ayah citations; tafsir is the third place to look.
8. The qirāʾāt layer is a small table. For latent readings, shādhdh and ḥujja material is where the evidence is.
9. (Revised.) The local hadith dataset does carry named sunan graders (al-Albānī, Zubair Ali Zai, Abū Ghudda, Aḥmad Shākir and others), so "every named grader calls it sahih" is enforceable locally for the seven collections; strike my earlier claim that it is not. Two problems remain: Musnad Aḥmad (with Arnāʾūṭ's grading) and Ibn Ḥibbān are where many asbāb and faḍāʾil reports for short surahs sit, so the enforceable rule is applied to a corpus that misses them; and the `esbab` block will still quote ungraded reports from tafsir while the `hadis` block refuses them. Resolve by letting `esbab` carry graded-weaker reports under `historicity` and keeping sahih-only for `hadis`.
10. Meal panel lineage: three Diyanet-lineage meals counted as three witnesses; Esed (TR) unmarked as English-mediated; Mustafa Öztürk missing.
11. In-memory information "allowed if marked": acceptable for interpretation, not for hadith grading, nuzūl order, or loanword history. Require a source for those three.
12. The `yenilik` block declares novelty against "a declared classical corpus". Until the full-Qur'an texts, the wujūh books and Bint al-Shāṭiʾ are loaded, the honest value for most findings in 86–114 is "not found in the local 86–114 slice", which is not a novelty claim; the schema should force that wording.

---

## (H) Asad and relay translations

### H1. Asad's notes as a modern tafsir source

Verdict: should, as a distinct witness, not as a generic `modern` entry.

What he adds for this reader. Asad (The Message of the Qur'an, 1980; ~5,000 notes) is the one modern commentator in English who works the way the project works at the lexical level: he reaches for Zamakhsharī and Rāghib first, prefers the figurative or psychological sense over the historical anecdote, refuses most asbāb narrowing, and reads miraculous narrative as allegory where the language allows. His lineage is exactly the rationalist line the user names (Zamakhsharī → ʿAbduh/Riḍā → Asad), and for 86–114 he leans on Zamakhsharī and Rāzī almost verse by verse, often with Rāghib on the key word. That makes his notes a frequent `oncul` for the project's secondary images (he routinely says "the primary meaning is X; the term also connotes Y, which is why I render it Z") and a frequent `tercih`/`itiraz` where he explicitly rejects a classical sense as "unwarranted". He also records his own interpolations in square brackets, so his translation is self-documenting about additions: this is the reason he is the right anchor for the relay comparison below.

Limits. His notes are a reader's digest of Zamakhsharī/Rāzī/Rāghib with a Muʿtazilī-rationalist filter; nothing in them is primary. Where he departs from the classics (jinn as unseen forces, miracles as parables, the "ʿAmr-and-Zayd" style rationalisation of asbāb) the departure should be labelled `modern` with his reasoning, never promoted to attestation. His English is also a strong 20th-century idiom that creates its own secondary images (the project will find images in Asad that are Asad's, not the Arabic's); the `yenilik` audit must keep "found in Asad" separate from "found in the classics he cites".

Block placement. Feed `modern` for his interpretive positions, `oncul`/`itiraz`/`tercih` for his lexical statements (always with the classical source he names), and `meal` as the English pole of the relay chain. No new block type is needed for him; the relay needs one (H2).

### H2. Relay drift as its own loss type (`aktarma`)

Yes, give it its own handling. The sixteen-meal review assumes each meal is a reading of the Arabic. For Esed (TR) that assumption is false twice over: Koytak–Ertürk translate Asad's English, and Turkish critics (e.g., the Marife 2010 critique, the zenodo tenkid, the İslâmî Araştırmalar article) document that the Turkish is a free, three-author text ("Esed, Koytak ve Ertürk tarafından yapılmış üç yazarlı bir meâl"), with the translators apparently working without Arabic. Counting it as a sixteenth independent witness to the Arabic corrupts the "what all meals lose in common" judgement; treating it as a relay turns it into a diagnostic instrument instead, because a two-step chain exposes which losses are translation-general, which are Turkish-specific, and which are the relay's own.

Proposed field: `aktarma` (relay drift) inside `meal`, with three mandatory sub-values and the two-pole quotation:
- `kaynak_zinciri`: Arabic → Asad EN → Esed TR (or Arabic → Mawdudi Urdu → TR, etc.).
- `kayip`: what the Turkish loses against Asad's English (and, separately, what Asad's English already lost against the Arabic; do not merge the two steps).
- `kazanc`: what the Turkish restores or adds against Asad that happens to be closer to the Arabic (a relay can gain by accident or by the translators' own tafsir knowledge).
- `isaretleme`: changes in the apparatus (brackets, italics, footnote presence) that alter the status of a word from "translator's addition" to "text".

Judging the example, 107:7. Arabic: wa-yamnaʿūna al-māʿūn. Asad: "and, withal, deny all assistance [to their fellow-men]"; he glosses māʿūn in a note as "all assistance" (a Rāzī/Zamakhsharī line: al-maʿrūf kulluhu). Turkish: "ve üstelik onlar, (insanlara) en ufak bir yardımı bile reddederler."
- Step 1 (Arabic → Asad): māʿūn's concrete range (the borrowed pot, axe, bucket; the small household goods; zakat; "all good") is collapsed to the abstract "assistance"; "all" is Asad's generalising choice. "withal" renders the wāw with a mild adversative colour. Square brackets correctly mark "to their fellow-men" as interpolation. Loss: concreteness and range; gain: none against the Arabic.
- Step 2 (Asad → Turkish): "all assistance" becomes "en ufak bir yardımı bile" ("even the smallest help"): this reverses Asad's quantifier from totality to minimum, and in doing so accidentally moves closer to the classical "small, easily lent things" sense (the project's own "raftaki kaplar" image) while departing from Asad. Record as `kazanc` against the Arabic and `kayip` against Asad at once; this double entry is the point of the field. "deny" → "reddederler" ("refuse") is a near match. Square brackets → round brackets: in Turkish meal convention round brackets are routine explanatory padding that readers skim, so the interpolation loses its visible status as the translator's addition; record under `isaretleme`. "withal" → "üstelik" is adequate.
- Verdict line the reader should see: the Turkish Esed is not Asad on 107:7; it is closer to the classics than Asad on the quantifier and further from him on the marking of additions. That sentence is impossible to write without the relay field.

Judging rule. A relay entry needs both poles quoted (EN and TR) and a one-line statement of the Arabic range from the dictionary; without the English pole the reader cannot tell relay drift from ordinary meal drift. Where the Turkish translators insert their own tafsir (critics show they do), label it `ceviren_eki` rather than attributing it to Asad.

### H3. Other relay translations worth the same treatment

- Tefhîmü'l-Kur'ân (Mawdudi): the Turkish (İnsan Yayınları team) was made from the Urdu, with the English (Zafar Ishaq Ansari / Towards Understanding the Qur'an) sometimes consulted; it is among the most-read tafsirs in Turkey, and its meal is widely quoted. Same `aktarma` handling; chain Urdu → TR (EN consultation noted). Should; especially valuable because Mawdudi's lexical notes are extensive for the short surahs.
- Fî Zılâli'l-Kur'ân (Quṭb, Turkish by Salih Uçan et al. and others): the Turkish is from Arabic, so it is not a relay in the strict sense, but the meal embedded in the Turkish Fî Zılâl is a translation of Quṭb's paraphrase, not of the Qur'an; treat its meal lines as relay (Arabic → Quṭb's Arabic paraphrase → TR) and its commentary as `modern`. Could.
- Elmalılı sadeleştirilmiş editions: an intralingual relay (Elmalılı's 1930s Turkish → modern Turkish by various editors), with documented drift; the same field applies and will matter to readers who hold the simplified editions. Should.
- Cemil Said (1924), the first printed Turkish translation, made from Kazimirski's French: historically the first relay meal; marginal for the reader, but a one-line `anlam_tarihi` note is worth having where a modern meal's wording descends from it. Could.
- Suat Yıldırım, Hayrat and Süleymaniye are direct from Arabic; no relay handling.
- Rule of thumb: any meal whose preface names a non-Arabic source text gets `kaynak_zinciri`; the chain is stated once in the source registry and the per-ayah entry carries only the drift.

### H4. Availability (quick check; nothing downloaded)

- Asad EN translation without notes: fawazahmed0 quran-api (eng-muhammadasad), as the coordinator states.
- Asad notes: an HTML edition "with footnotes" (proofread 2016) circulates on ebooks.rahnuma.org and similar mirrors; quran-archive.org has an explorer for Asad; several PDFs of the full book with notes circulate (epaperpdf and others); an app (MWM.ai) presents notes per verse. No structured dataset (JSON/API) of the notes was found in the quick check. Rights: the text is under copyright (The Book Foundation / Fons Vitae); the mirrors are not licensed. Status: notes available as scrapable HTML/PDF text (unverified for completeness and alignment); no verified machine-readable notes dataset.
- Esed TR (Koytak–Ertürk): meal text per ayah is on kuranmeali.com and other aggregators; the Turkish notes are in the İşaret Yayınları book; machine-readable Turkish notes unverified.
- Tefhîm TR: meal text on several aggregators; Turkish notes unverified. Mawdudi EN (Ansari) with notes exists on tafheem-type sites and on quran-tafsir aggregators (unverified alignment).
