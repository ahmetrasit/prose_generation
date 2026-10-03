"""Registry of whole-book sources fetched by fetch_openiti.py.

Each entry pins one OpenITI version URI (chosen from the OpenITI RELEASE metadata, OpenITI_metadata_2025-1-9.tsv;
the version marked `pri` unless `why` says otherwise), or names another host, or is a pointer (access hafiza).

fields
  uri      OpenITI version URI (author.book.version-lang) — host openiti
  host     openiti (default) | qtnet (quran-tafsir.net per-ayah pages) | pointer (no local text)
  qorder   True when the book follows the muṣḥaf order: surah/ayah are detected and filled
  mode     auto (headings, else ~1500-char chunks) | hadith (one segment per numbered ḥadīth)
  why      reason when the chosen version is not the RELEASE primary
  notes    identity caveats (kept in source.json.notes)
"""

W = []


def w(id, title, author, death, kind, tradition, uri=None, qorder=False, mode="auto", why="", notes="", **kw):
    W.append(dict(id=id, title=title, author=author, death_ah=death, kind=kind, tradition=tradition, uri=uri,
                  qorder=qorder, mode=mode, why=why, notes=notes, host=kw.pop("host", "openiti" if uri else "pointer"),
                  **kw))


# ---------------------------------------------------------------- MUST: asbāb
w("WAHIDI-ASBAB", "Asbāb nuzūl al-Qurʾān", "al-Wāḥidī", 468, "ulum", "asbab al-nuzul, sunni-rivaya",
  "0468IbnAhmadWahidiNaysaburi.AsbabNuzul.Shamela0011314-ara1", qorder=True,
  notes="ed. ʿIṣām al-Ḥumaydān (Dār al-Iṣlāḥ, Dammam).")
w("SUYUTI-LUBAB", "Lubāb al-nuqūl fī asbāb al-nuzūl", "al-Suyūṭī", 911, "ulum", "asbab al-nuzul, sunni-rivaya",
  "0911Suyuti.LubabNuqul.JK000436-ara1", qorder=True)
# ---------------------------------------------------------------- MUST: maʿānī / gharīb
w("MAJAZ", "Majāz al-Qurʾān", "Abū ʿUbayda Maʿmar b. al-Muthannā", 209, "maani", "basran philology",
  "0209AbuCubayda.MajazQuran.Shamela0023630-ara1", qorder=True,
  why="the RELEASE primary (JK010146) holds vol. 1 only (pages V01 1-132); Shamela0023630 is Sezgin's edition "
      "(al-Khānjī) with both volumes (V01, V02 to p. 453) and surah headings 1-114.")
w("FARRA", "Maʿānī al-Qurʾān", "al-Farrāʾ", 207, "maani", "kufan philology",
  "0207IbnZiyadFarra.MacaniQuran.Shamela0023634-ara1", qorder=True,
  notes="ed. al-Najātī / al-Najjār / al-Shalabī.")
w("ZAJJAJ", "Maʿānī al-Qurʾān wa-iʿrābuh", "al-Zajjāj", 311, "maani", "basran philology",
  "0311IbnSariZajjaj.MacaniQuran.Shamela0000922-ara1", qorder=True, notes="ed. ʿAbd al-Jalīl Shalabī.")
w("IBNQUTAYBA-GHARIB", "Gharīb al-Qurʾān (Tafsīr gharīb al-Qurʾān)", "Ibn Qutayba", 276, "maani", "philology",
  "0276IbnQutaybaDinawari.GharibQuran.Shamela0003259-ara1", qorder=True, notes="ed. Aḥmad Ṣaqr.")
w("IBNQUTAYBA-MUSHKIL", "Taʾwīl mushkil al-Qurʾān", "Ibn Qutayba", 276, "maani", "philology",
  "0276IbnQutaybaDinawari.TawilMushkilQuran.Shamela0023596-ara1",
  notes="Thematic, not in muṣḥaf order: s/a not assigned.")
# ---------------------------------------------------------------- MUST: wujūh
w("MUQATIL-WUJUH", "al-Ashbāh wa-l-naẓāʾir fī al-Qurʾān al-karīm (al-Wujūh wa-l-naẓāʾir)", "Muqātil b. Sulaymān",
  150, "wujuh", "early tafsir", host="pointer",
  notes="Not in OpenITI (RELEASE 2025-1-9: no Muqātil work besides the Tafsīr). Printed: ed. ʿAbd Allāh Maḥmūd "
        "Shiḥāta (Cairo 1975); ed. Ḥātim al-Ḍāmin (2006). Yaḥyā b. Sallām's al-Taṣārīf (a wujūh work built on "
        "Muqātil's) is in OpenITI: 0200YahyaIbnSallam.Tasarif.Shamela0011783-ara1 (not fetched). archive.org search "
        "(2026-10-03) found no dedicated item, only bulk Shamela dumps. shamela.ws search answered HTTP 403 to a scripted request (2026-10-03), so Shamela availability is not verified.")
w("DAMGHANI", "Iṣlāḥ al-wujūh wa-l-naẓāʾir fī al-Qurʾān al-karīm (Qāmūs al-Qurʾān)", "al-Dāmghānī", 478, "wujuh",
  "wujuh wa-nazair", "0478IbnMuhammadDamghani.QamusQuran.ShamAY0034085-ara1",
  notes="ed. ʿAbd al-ʿAzīz Sayyid al-Ahl (Beirut 1980, as 'Qāmūs al-Qurʾān'). Arranged by word, not by ayah.")
w("IBNJAWZI-NUZHA", "Nuzhat al-aʿyun al-nawāẓir fī ʿilm al-wujūh wa-l-naẓāʾir", "Ibn al-Jawzī", 597, "wujuh",
  "wujuh wa-nazair", "0597IbnJawzi.NuzhatAcyun.JK007134-ara1", notes="ed. M. ʿA. K. al-Rāḍī. Arranged by word.")
w("FURUQ", "al-Furūq al-lughawiyya", "Abū Hilāl al-ʿAskarī", 395, "lexicon", "mutazili philology",
  "0395AbuHilalCaskari.FuruqLughawiyya.JK006960-ara1",
  notes="Plain al-ʿAskarī text. NOT Shamela0001736 (Muʿjam al-furūq al-lughawiyya, which merges al-Jazāʾirī's "
        "Furūq into it).")
# ---------------------------------------------------------------- MUST: ʿulūm
w("ITQAN", "al-Itqān fī ʿulūm al-Qurʾān", "al-Suyūṭī", 911, "ulum", "ulum al-quran",
  "0911Suyuti.Itqan.JK001295-ara1", notes="ed. Saʿīd al-Mandūb (Dār al-Fikr 1996).")
w("BURHAN", "al-Burhān fī ʿulūm al-Qurʾān", "al-Zarkashī", 794, "ulum", "ulum al-quran",
  "0794BadrDinZarkashi.BurhanFiCulumQuran.JK000162-ara1", notes="ed. M. Abū l-Faḍl Ibrāhīm (Dār al-Maʿrifa).")
# ---------------------------------------------------------------- MUST: qirāʾāt
w("IBNMUJAHID", "Kitāb al-Sabʿa fī al-qirāʾāt", "Ibn Mujāhid", 324, "qiraat", "qiraat",
  "0324IbnMujahid.SabcaFiQiraat.JK000912-ara1", qorder=True, notes="ed. Shawqī Ḍayf (Dār al-Maʿārif).")
w("IBNKHALAWAYH-HUJJA", "al-Ḥujja fī al-qirāʾāt al-sabʿ", "Ibn Khālawayh (attr.)", 370, "qiraat", "qiraat",
  "0370IbnAhmadIbnKhalawayh.HujjaFiQiraatSabca.JK000461-ara1", qorder=True, running_heads=True,
  notes="ed. ʿAbd al-ʿĀl Sālim Mukarram. The attribution to Ibn Khālawayh is disputed in the literature.")
w("FARISI-HUJJA", "al-Ḥujja li-l-qurrāʾ al-sabʿa", "Abū ʿAlī al-Fārisī", 377, "qiraat", "qiraat, basran grammar",
  "0377IbnAhmadFarisi.HujjaLiQurraSabca.Shamela0035101-ara1", qorder=True,
  notes="ed. Badr al-Dīn Qahwajī / Bashīr Juwayjābī (Dār al-Maʾmūn).")
w("IBNJINNI-MUHTASAB", "al-Muḥtasab fī tabyīn wujūh shawādhdh al-qirāʾāt", "Ibn Jinnī", 392, "qiraat",
  "qiraat (shawadhdh), grammar", "0392IbnJinniMawsili.MuhtasabFiTabyin.Shamela0008660-ara1", qorder=True)
# ---------------------------------------------------------------- MUST: early tafsir
w("MUQATIL", "Tafsīr Muqātil b. Sulaymān", "Muqātil b. Sulaymān", 150, "tafsir", "early tafsir",
  "0150MuqatilIbnSulayman.TafsirMuqatil.Tafsir02067-ara1", qorder=True,
  notes="altafsir.com text (commentary only, no introduction, no pagination); every passage is headed with its "
        "surah.ayah range.")
w("ABDURRAZZAQ", "Tafsīr ʿAbd al-Razzāq", "ʿAbd al-Razzāq al-Ṣanʿānī", 211, "tafsir", "early tafsir, rivaya",
  "0211CabdRazzaqSancani.Tafsir.JK000435-ara1", qorder=True, notes="ed. Muṣṭafā Muslim Muḥammad (al-Rushd 1410).")
w("IBNABIHATIM", "Tafsīr al-Qurʾān al-ʿaẓīm (Tafsīr Ibn Abī Ḥātim)", "Ibn Abī Ḥātim al-Rāzī", 327, "tafsir",
  "sunni-rivaya", "0327IbnAbiHatimRazi.Tafsir.JK006474-ara1", qorder=True,
  notes="ed. Asʿad M. al-Ṭayyib. The extant text is incomplete (large lacunae in the later surahs).")
w("YAHYA-SALLAM", "Tafsīr Yaḥyā b. Sallām", "Yaḥyā b. Sallām", 200, "tafsir", "early tafsir",
  "0200YahyaIbnSallam.Tafsir.Shamela0012851-ara1", qorder=True,
  notes="ed. Hind Shalabī (DKI): the surviving portions only, not the whole Qurʾān.")
w("MUJAHID", "Tafsīr Mujāhid", "Mujāhid b. Jabr", 104, "tafsir", "early tafsir",
  "0104MujahidIbnJabr.Tafsir.JK000459-ara1", qorder=True,
  notes="ed. al-Sūratī; the transmitted recension (Ādam b. Abī Iyās), not Mujāhid's own book.")
# ---------------------------------------------------------------- MUST: full texts of the 16 tafsirs
w("TAB-FULL", "Jāmiʿ al-bayān ʿan taʾwīl āy al-Qurʾān", "al-Ṭabarī", 310, "tafsir", "sunni-rivaya",
  "0310Tabari.JamicBayan.Shamela0007798-ara1", qorder=True, notes="ed. al-Turkī (Dār Hajr).")
w("IBNKATHIR-FULL", "Tafsīr al-Qurʾān al-ʿaẓīm", "Ibn Kathīr", 774, "tafsir", "sunni-rivaya",
  "0774IbnKathir.TafsirQuran.Shamela0008473-ara1", qorder=True, notes="ed. Sāmī Salāma (Dār Ṭayba).")
w("DURR-FULL", "al-Durr al-manthūr fī al-tafsīr bi-l-maʾthūr", "al-Suyūṭī", 911, "tafsir", "sunni-rivaya",
  "0911Suyuti.DurrManthur.Shamela0012884-ara1", qorder=True, notes="Dār al-Fikr ed.")
w("KASHSHAF-FULL", "al-Kashshāf ʿan ḥaqāʾiq ghawāmiḍ al-tanzīl", "al-Zamakhsharī", 538, "tafsir",
  "mutazili-dirayet", "0538JarAllahZamakhshari.Kashshaf.JK001496-ara1", qorder=True,
  notes="ed. ʿAbd al-Razzāq al-Mahdī (Dār Iḥyāʾ al-Turāth).")
w("RAZI-FULL", "Mafātīḥ al-ghayb (al-Tafsīr al-kabīr)", "Fakhr al-Dīn al-Rāzī", 606, "tafsir", "sunni-dirayet",
  "0606FakhrDinRazi.MafatihGhayb.JK006478-ara1", qorder=True, notes="DKI ed. 2000.")
w("BAYDAWI-FULL", "Anwār al-tanzīl wa-asrār al-taʾwīl", "al-Bayḍāwī", 685, "tafsir", "sunni-dirayet",
  "0685NasirDinBaydawi.AnwarTanzil.Tafsir01006-ara1", qorder=True,
  notes="altafsir.com text (commentary only, no pagination), passages headed surah.ayah.")
w("BIQAI-FULL", "Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar", "al-Biqāʿī", 885, "tafsir", "nazm",
  "0885BurhanDinBiqaci.NazmDurar.JK009270-ara1", qorder=True, notes="ed. ʿAbd al-Razzāq Ghālib al-Mahdī (DKI).")
w("QURTUBI-FULL", "al-Jāmiʿ li-aḥkām al-Qurʾān", "al-Qurṭubī", 671, "tafsir", "sunni-dirayet",
  "0671AbuCabdAllahQurtubi.JamicLiAhkamQuran.Tafsir01005-ara1", qorder=True,
  notes="altafsir.com text (commentary only, no pagination), passages headed surah.ayah.")
w("IBNATIYYA-FULL", "al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz", "Ibn ʿAṭiyya", 542, "tafsir",
  "sunni-dirayet", "0541IbnCatiyyaAndalusi.MuharrarWajiz.Shamela0023632-ara1", qorder=True,
  notes="ed. ʿAbd al-Salām ʿAbd al-Shāfī (DKI). OpenITI dates the author 541.")
w("ABUHAYYAN-FULL", "al-Baḥr al-muḥīṭ fī al-tafsīr", "Abū Ḥayyān al-Gharnāṭī", 745, "tafsir", "sunni-dirayet",
  "0745AbuHayyanGharnati.TafsirBahrMuhit.Shamela0023591-ara1", qorder=True, notes="ed. Ṣidqī M. Jamīl (Dār al-Fikr).")
w("ALUSI-FULL", "Rūḥ al-maʿānī fī tafsīr al-Qurʾān al-ʿaẓīm wa-l-sabʿ al-mathānī", "al-Ālūsī", 1270, "tafsir",
  "sunni-dirayet", "1270ShihabDinAlusi.RuhMacani.JK000906-ara1", qorder=True, notes="Dār Iḥyāʾ al-Turāth ed.")
w("BAGHAWI-FULL", "Maʿālim al-tanzīl", "al-Baghawī", 516, "tafsir", "sunni-rivaya",
  "0510IbnMascudBaghawi.Tafsir.Shamela0000041-ara1", qorder=True,
  notes="ed. al-Nimr et al. (Dār Ṭayba). OpenITI dates the author 510; he died 516.")
w("MAWARDI-FULL", "al-Nukat wa-l-ʿuyūn", "al-Māwardī", 450, "tafsir", "sunni-dirayet",
  "0450AbuHasanMawardi.NukatWaCuyun.JK009396-ara1", qorder=True, notes="ed. al-Sayyid b. ʿAbd al-Maqṣūd (DKI).")
w("WAHIDI-BASIT", "al-Tafsīr al-basīṭ", "al-Wāḥidī", 468, "tafsir", "sunni-dirayet, philology",
  "0468IbnAhmadWahidiNaysaburi.TafsirBasit.Sham19Y0013231-ara1", qorder=True,
  notes="Imām University ed. (15 doctoral theses).")
w("WAHIDI-WAJIZ", "al-Wajīz fī tafsīr al-kitāb al-ʿazīz", "al-Wāḥidī", 468, "tafsir", "sunni-dirayet",
  "0468IbnAhmadWahidiNaysaburi.WajizFiTafsir.Tafsir08060-ara1", qorder=True,
  notes="This is the work quran-tafsir.net serves as 'wahidy' (its book list, checked 2026-10-03: "
        "'الوجيز في تفسير الكتاب العزيز للواحدي'), i.e. the local per-ayah WAHIDI-QT slice is al-Wajīz — not al-Wasīṭ, "
        "al-Basīṭ or the Asbāb. altafsir.com text, passages headed surah.ayah.")
w("IBNASHUR-FULL", "al-Taḥrīr wa-l-tanwīr", "Ibn ʿĀshūr", 1393, "tafsir", "modern-bayani",
  "1393MuhammadTahirIbnCashurTunisi.TahrirWaTanwir.JK009362-ara1", qorder=True, notes="Dār Saḥnūn ed. 1997.")
w("NASAFI-FULL", "Madārik al-tanzīl wa-ḥaqāʾiq al-taʾwīl", "al-Nasafī", 710, "tafsir", "sunni-dirayet",
  "0710IbnAhmadHafizDinNasafi.Tafsir.JK000876-ara1", qorder=True)
# ---------------------------------------------------------------- MUST: others
w("TABRISI", "Majmaʿ al-bayān fī tafsīr al-Qurʾān", "al-Ṭabrisī", 548, "tafsir", "imami",
  "0548IbnHasanTabarsi.TafsirMajmacBayan.Tafsir04003-ara1", qorder=True,
  notes="altafsir.com text (commentary only, no pagination), passages headed surah.ayah.")
w("ABDUH-AMMA", "Tafsīr al-Qurʾān al-karīm: Juzʾ ʿAmma", "Muḥammad ʿAbduh", 1323, "tafsir", "reformist",
  host="pointer",
  notes="Not in OpenITI (RELEASE 2025-1-9 has only Risālat al-tawḥīd and the Nahj al-balāgha commentary by "
        "ʿAbduh), and not on quran-tafsir.net's book list. First printed Cairo 1322/1904 (al-Manār); the author "
        "died 1905, so the text is out of copyright, but no free digital text was located in this pass (archive.org "
        "search 2026-10-03: no matching item). shamela.ws search answered HTTP 403 to a scripted request (2026-10-03), so Shamela availability is not verified.")
w("BINTSHATI", "al-Tafsīr al-bayānī li-l-Qurʾān al-karīm (2 vols)", "ʿĀʾisha ʿAbd al-Raḥmān (Bint al-Shāṭiʾ)",
  1419, "tafsir", "bayani", host="pointer",
  notes="In copyright (author d. 1998 CE); not in OpenITI, not on quran-tafsir.net. Dār al-Maʿārif, Cairo "
        "(1962, 1969). Pointer only. archive.org has user-uploaded scans of unclear licence (items 052Pdf., "
        "elshandawily0546, elshandawily0547; listing seen 2026-10-03, not downloaded).",
  urls=["https://archive.org/details/elshandawily0546", "https://archive.org/details/elshandawily0547"])
w("KHULI", "Manāhij tajdīd fī al-naḥw wa-l-balāgha wa-l-tafsīr wa-l-adab", "Amīn al-Khūlī", 1385, "modern",
  "bayani", host="pointer",
  notes="In copyright (author d. 1966 CE); not in OpenITI (which has three other al-Khūlī books from Hindawi: "
        "Fī al-adab al-Miṣrī, Hādhā al-naḥw, Raʾy fī Abī l-ʿAlāʾ). Dār al-Maʿrifa, Cairo 1961. Pointer only. "
        "archive.org has user-uploaded scans of unclear licence (items AAlexandrina-087373, "
        "moharram1965_gmail_20171113_0102, elshandawily3374; listing seen 2026-10-03, not downloaded).",
  urls=["https://archive.org/details/AAlexandrina-087373"])
# ---------------------------------------------------------------- SHOULD
w("AKHFASH", "Maʿānī al-Qurʾān", "al-Akhfash al-Awsaṭ", 215, "maani", "basran philology, mutazili",
  "0215AkhfashAwsat.MacaniQuran.Shamela0022371-ara1", qorder=True, notes="ed. Hudā Maḥmūd Qarāʿa (al-Khānjī).")
w("NAHHAS", "Iʿrāb al-Qurʾān", "Abū Jaʿfar al-Naḥḥās", 338, "maani", "irab", "0338AbuJacfarNahhas.IcrabQuran.JK001417-ara1",
  qorder=True, bare_numbers=True, notes="ed. Zuhayr Ghāzī Zāhid (ʿĀlam al-Kutub).")
w("SAMIN-DURR", "al-Durr al-maṣūn fī ʿulūm al-kitāb al-maknūn", "al-Samīn al-Ḥalabī", 756, "maani", "irab",
  "0756IbnYusufSaminHalabi.DurrMasun.Tafsir02079-ara1", qorder=True,
  notes="altafsir.com text (no pagination), passages headed surah.ayah.")
w("SAMIN-UMDA", "ʿUmdat al-ḥuffāẓ fī tafsīr ashraf al-alfāẓ", "al-Samīn al-Ḥalabī", 756, "lexicon",
  "quranic lexicon", "0756IbnYusufSaminHalabi.CumdatHuffaz.Sham19Y0017829-ara1",
  notes="ed. M. Bāsil ʿUyūn al-Sūd (DKI). Arranged by root.")
w("IBNJAWZI-ZAD", "Zād al-masīr fī ʿilm al-tafsīr", "Ibn al-Jawzī", 597, "tafsir", "sunni-dirayet",
  "0597IbnJawzi.ZadMasir.JK000791-ara1", qorder=True)
w("THALABI", "al-Kashf wa-l-bayān ʿan tafsīr al-Qurʾān", "al-Thaʿlabī", 427, "tafsir", "sunni",
  "0427AbuIshaqThaclabi.KashfWaBayan.Shamela0023578-ara1", qorder=True, notes="ed. Ibn ʿĀshūr (Dār Iḥyāʾ al-Turāth).")
w("GHARNATI", "al-Burhān fī tanāsub suwar al-Qurʾān", "Abū Jaʿfar Ibn al-Zubayr al-Gharnāṭī", 708, "nazm", "nazm",
  "0708IbnIbrahimAbuJacfarGharnati.Burhan.Shamela0001388-ara1", qorder=True, surah_only=True, notes="ed. Muḥammad Shaʿbānī.")
w("SUYUTI-TANASUQ", "Tanāsuq al-durar fī tanāsub al-suwar (publ. as Asrār tartīb al-Qurʾān)", "al-Suyūṭī", 911,
  "nazm", "nazm", "0911Suyuti.AsrarTartibQuran.JK000440-ara1", qorder=True, surah_only=True,
  notes="OpenITI title 'Asrār tartīb al-Qurʾān' (ed. ʿAbd al-Qādir Aḥmad ʿAṭā, Dār al-Iʿtiṣām) — the edition under "
        "which Tanāsuq al-durar is usually printed; check the introduction before citing it under the other title.")
w("QUSHAYRI", "Laṭāʾif al-ishārāt", "al-Qushayrī", 465, "isari", "ishari",
  "0465IbnHawazinQushayri.LataifIsharat.JK009257-ara1", qorder=True)
w("SULAMI", "Ḥaqāʾiq al-tafsīr", "al-Sulamī", 412, "isari", "ishari", "0412Sulami.Tafsir.JK007094-ara1", qorder=True,
  notes="ed. Sayyid ʿImrān (DKI).")
w("TUSTARI", "Tafsīr al-Qurʾān al-ʿaẓīm", "Sahl al-Tustarī", 283, "isari", "ishari",
  "0283SahlTustari.Tafsir.Tafsir03029-ara1", qorder=True, notes="altafsir.com text, passages headed surah.ayah.")
w("BURSEVI", "Rūḥ al-bayān", "İsmāʿīl Ḥaqqī Bursevī", 1127, "isari", "ishari, ottoman",
  "1127IsmacilHaqqiBurusawi.RuhBayan.ShamAY0034059-ara1", qorder=True, notes="Dār Iḥyāʾ al-Turāth ed.")
w("TABATABAI", "al-Mīzān fī tafsīr al-Qurʾān", "Muḥammad Ḥusayn al-Ṭabāṭabāʾī", 1402, "tafsir", "imami",
  "1402SayyidTabatabai.TafsirMizan.Tafsir04056-ara1", qorder=True,
  notes="altafsir.com text, passages headed surah.ayah. Modern work (author d. 1981 CE) distributed by OpenITI; "
        "local research copy.")
w("QUTB-ZILAL", "Fī ẓilāl al-Qurʾān", "Sayyid Quṭb", 1386, "tafsir", "modern-haraki", host="qtnet", slug="qotb",
  notes="Copyrighted modern work. quran-tafsir.net serves it openly per ayah (slug 'qotb'); only S1 and 86-114 "
        "were fetched. OpenITI also has 1386SayyidQutb.FiZilalQuran.Tafsir07053-ara1 (446,925 chars, i.e. a "
        "small part of the book) — not fetched.")
w("JURJANI-DALAIL", "Dalāʾil al-iʿjāz", "ʿAbd al-Qāhir al-Jurjānī", 471, "ulum", "balagha, ijaz",
  "0471CabdQahirJurjani.DalailIcjaz.JK001019-ara1",
  notes="ed. al-Tanjī (Dār al-Kitāb al-ʿArabī 1995). Shākir's edition is in OpenITI as Shamela0012055 (not used).")
w("JURJANI-ASRAR", "Asrār al-balāgha", "ʿAbd al-Qāhir al-Jurjānī", 471, "ulum", "balagha",
  "0471CabdQahirJurjani.AsrarBalagha.JK006906-ara1")
w("MUSNAD-AHMAD", "al-Musnad", "Aḥmad b. Ḥanbal", 241, "hadith", "sunni-hadith",
  "0241IbnHanbal.Musnad.Shamela0025794-ara1", mode="hadith",
  notes="ed. al-Arnaʾūṭ / Murshid (al-Risāla); the editors' gradings were in footnotes, which OpenITI removed: "
        "UNGRADED here. Use only with the grade shown from elsewhere.")
w("IBNHIBBAN", "Ṣaḥīḥ Ibn Ḥibbān (al-Iḥsān fī taqrīb Ṣaḥīḥ Ibn Ḥibbān, arr. Ibn Balbān)", "Ibn Ḥibbān", 354,
  "hadith", "sunni-hadith", "0739CalaDinIbnBalban.Ihsan.Sham19Y0001729-ara1", mode="hadith",
  notes="Ibn Balbān's (d. 739) arrangement, ed. al-Arnaʾūṭ (al-Risāla 1988); gradings not carried.")
w("IBNHISHAM", "al-Sīra al-nabawiyya", "Ibn Hishām", 213, "sira", "sira",
  "0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1", notes="ed. al-Saqqā / al-Abyārī / Shalabī (al-Ḥalabī).")
w("KALBI-ASNAM", "Kitāb al-Aṣnām", "Hishām b. al-Kalbī", 204, "sira", "akhbar", "0204IbnKalbi.Asnam.JK007059-ara1",
  notes="ed. Aḥmad Zakī Bāshā.")
w("AZRAQI", "Akhbār Makka", "al-Azraqī", 249, "sira", "akhbar", "0249Azraqi.AkhbarMakka.JK003504-ara1",
  notes="ed. Rushdī al-Ṣāliḥ Malḥas.")
w("MUALLAQAT", "Sharḥ al-Muʿallaqāt al-sabʿ", "al-Zawzanī", 486, "poetry", "jahili poetry with commentary",
  "0486IbnAhmadZuzani.SharhMucallaqat.Shamela0011253-ara1", notes="The seven odes with al-Zawzanī's sharḥ.")
w("MUFADDALIYYAT", "al-Mufaḍḍaliyyāt", "al-Mufaḍḍal al-Ḍabbī", 168, "poetry", "jahili/early islamic poetry",
  "0168MufaddalDabbi.Mufaddaliyyat.Shamela0006904-ara1", notes="ed. Shākir / Hārūn.")
w("ASMAIYYAT", "al-Aṣmaʿiyyāt", "al-Aṣmaʿī", 216, "poetry", "jahili/early islamic poetry",
  "0216IbnQuraybAsmaci.Asmaciyyat.Shamela0006905-ara1", notes="ed. Shākir / Hārūn.")
w("HAMASA", "Sharḥ Dīwān al-Ḥamāsa (Abū Tammām's Ḥamāsa with al-Marzūqī's commentary)", "al-Marzūqī", 421,
  "poetry", "anthology with commentary", "0421IbnMuhammadMarzuqi.SharhDiwanHamasa.Shamela0026536-ara1",
  notes="Abū Tammām's own text is not in OpenITI as a separate book; this is al-Marzūqī's sharḥ (ed. Gharīd "
        "al-Shaykh). al-Tabrīzī's sharḥ is 0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1 (not fetched).")
w("TAJ", "Tāj al-ʿarūs min jawāhir al-Qāmūs", "Murtaḍā al-Zabīdī", 1205, "lexicon", "classical-lexicography",
  "1205MurtadaZabidi.TajCarus.Shamela0007030-ara1", mode="lexicon",
  why="the RELEASE primary (JK007140) has no root headings (4 in 41 MB); Shamela0007030 is the same Kuwait "
      "edition (Dār al-Hidāya) with one heading per root, which gives entry locators TAJ:<root>.",
  notes="Kuwait ed. (Dār al-Hidāya), several editors. Locator TAJ:<root> (continuations #2, #3 …); page in `page`.")
# ---------------------------------------------------------------- COULD
w("NASHR", "al-Nashr fī al-qirāʾāt al-ʿashr", "Ibn al-Jazarī", 833, "qiraat", "qiraat",
  "0833IbnJazari.Nashr.Shamela0022642-ara1", notes="ed. al-Ḍabbāʿ. Vol. 1 is theory; vol. 2 (farsh) follows the muṣḥaf.")
w("KHATTABI", "Bayān iʿjāz al-Qurʾān", "al-Khaṭṭābī", 388, "ulum", "ijaz",
  "0388AbuSulaymanKhattabi.BayanIcjazQuran.Sham19Y0013900-ara1", notes="In Thalāth rasāʾil fī iʿjāz al-Qurʾān.")
w("BAQILLANI", "Iʿjāz al-Qurʾān", "al-Bāqillānī", 403, "ulum", "ijaz, ashari", "0403AbuBakrBaqillani.IcjazQuran.JK001020-ara1",
  notes="ed. Aḥmad Ṣaqr.")
w("RUMMANI", "al-Nukat fī iʿjāz al-Qurʾān", "al-Rummānī", 384, "ulum", "ijaz, mutazili",
  "0384AbuHasanRummani.NukatFiIcjazQuran.Sham19Y0013981-ara1", notes="In Thalāth rasāʾil fī iʿjāz al-Qurʾān.")
w("QASHANI", "Taʾwīlāt al-Qurʾān (printed as Tafsīr Ibn ʿArabī)", "ʿAbd al-Razzāq al-Qāshānī", 736, "isari",
  "ishari, akbari", "0638IbnCarabi.Tafsir.Tafsir03033-ara1", qorder=True,
  notes="OpenITI files it under Ibn ʿArabī (0638), following the printed title; the work is al-Qāshānī's "
        "Taʾwīlāt. altafsir.com text, passages headed surah.ayah.")
w("JISHUMI", "al-Tahdhīb fī al-tafsīr", "al-Ḥākim al-Jishumī", 494, "tafsir", "mutazili, zaydi",
  "0494HakimJushami.TahdhibFiTafsir.Meshkat0014420-ara1", qorder=True)
w("IBNKHALAWAYH-MUKHTASAR", "Mukhtaṣar fī shawādhdh al-Qurʾān min Kitāb al-Badīʿ", "Ibn Khālawayh", 370, "qiraat",
  "qiraat (shawadhdh)", host="pointer",
  notes="Not in OpenITI (RELEASE 2025-1-9 lists three Ibn Khālawayh books, not this one). Printed: ed. G. "
        "Bergsträsser (Bibliotheca Islamica 7, Cairo 1934). archive.org has PDF scans of that edition uploaded by "
        "users (items 20210405_20210405_1626, 5023pdf, 0886Pdf; listing seen 2026-10-03, not downloaded, no text "
        "layer checked). shamela.ws search answered HTTP 403 to a scripted request (2026-10-03), so Shamela availability is not verified.",
  urls=["https://archive.org/details/20210405_20210405_1626"])

BY_ID = {x["id"]: x for x in W}

# Eyeball spot-checks of the s/a assignment (10 segments per Qur-an-ordered source), filled after review.
QA: dict[str, str] = {
    # 10 random segments with an ayah, read against the Qur'an text (2026-10-03). "plausible" = the segment's
    # discussion belongs to the assigned ayah (range); "off" = the segment mainly treats a neighbouring ayah.
    "WAHIDI-ASBAB": "10/10 correct. Quality: good.",
    "SUYUTI-LUBAB": "9/10 correct; 1 segment opens with material on 76:8 but is filed at 76:20. Quality: good.",
    "MAJAZ": "10/10 correct (lemma «…» (n) structure). Front matter and the indexes carry no s/a. Quality: good.",
    "FARRA": "9/10 correct, 1 off by one (5:95 filed as 5:96). Quality: good.",
    "ZAJJAJ": "9/10 correct, 1 off by two (segment starts on 6:3, filed 6:5). Quality: good.",
    "IBNQUTAYBA-GHARIB": "10/10 correct. Quality: good.",
    "IBNMUJAHID": "8/10 correct, 2 off (2:97-98 filed 2:102; 28:34 filed 28:37); the uṣūl chapters inside S1-2 carry the "
                  "surah only or the nearest farsh entry. Quality: partial.",
    "IBNKHALAWAYH-HUJJA": "9/10 correct, 1 off (19:25 filed 19:31). Surah boundaries come partly from running page "
                          "titles. Quality: good.",
    "FARISI-HUJJA": "10/10 plausible (long grammatical excursuses are filed under the lemma that opened them); 70% of "
                    "segments carry an ayah. Quality: partial.",
    "IBNJINNI-MUHTASAB": "10/10 plausible but only ~53% of segments carry an ayah (the lemmas are shādhdh readings that "
                         "often do not match the canonical text). Quality: partial.",
    "MUQATIL": "10/10 correct (altafsir surah.ayah headings). Quality: good.",
    "ABDURRAZZAQ": "10/10 correct (JK 'sura : ( n )' headings). Quality: good.",
    "IBNABIHATIM": "10/10 correct. Quality: good.",
    "YAHYA-SALLAM": "10/10 correct ([sura: n] citations after every lemma). Only the extant portions exist. Quality: good.",
    "MUJAHID": "10/10 correct. Quality: good.",
    "TAB-FULL": "10/10 correct (Shamela [sura: n] headings). Quality: good.",
    "IBNKATHIR-FULL": "10/10 correct; long ḥadīth runs are filed under the section's ayah. Quality: good.",
    "DURR-FULL": "10/10 correct; ~25% of segments (long runs of reports with no Qur'an quotation) carry the surah only. "
                 "Quality: good where assigned.",
    "KASHSHAF-FULL": "9/10 correct, 1 off by one (3:19 filed 3:18). Quality: good.",
    "RAZI-FULL": "10/10 correct. Quality: good.",
    "BAYDAWI-FULL": "altafsir surah.ayah headings (structural). Quality: good.",
    "BIQAI-FULL": "10/10 plausible. Quality: good.",
    "QURTUBI-FULL": "altafsir surah.ayah headings (structural); 87% of segments quote their ayah. Quality: good.",
    "IBNATIYYA-FULL": "8/10 correct, 2 off by 1-2 (e.g. 2:282 filed 2:280-281). Shamela section headings give ranges. "
                      "Quality: good.",
    "ABUHAYYAN-FULL": "10/10 inside the right range, but Abū Ḥayyān's sections are long (e.g. 'الآيات 1 الى 54'): ~46% "
                      "of segments carry the whole section range (a..a_end > 10 ayahs) because the commentary cites "
                      "lemmas without brackets. Quality: partial (range-level).",
    "ALUSI-FULL": "10/10 correct. Quality: good.",
    "BAGHAWI-FULL": "10/10 correct. Quality: good.",
    "MAWARDI-FULL": "10/10 correct. Quality: good.",
    "WAHIDI-BASIT": "10/10 correct. Quality: good.",
    "WAHIDI-WAJIZ": "altafsir surah.ayah headings (structural). Quality: good.",
    "IBNASHUR-FULL": "10/10 correct; ~20% of segments (introduction, long excursuses) carry no ayah. Quality: good.",
    "NASAFI-FULL": "10/10 correct. Quality: good.",
    "TABRISI": "altafsir surah.ayah headings (structural). Quality: good.",
    "AKHFASH": "9/10 correct, 1 general grammatical note filed under 2:41. Quality: good.",
    "NAHHAS": "10/10 correct (the book's own bare ayah numbers). Quality: good.",
    "SAMIN-DURR": "altafsir surah.ayah headings (structural); 81% of segments quote their ayah. Quality: good.",
    "IBNJAWZI-ZAD": "10/10 correct. Quality: good.",
    "THALABI": "10/10 plausible; ~10% carry a whole Shamela section range. Quality: good.",
    "GHARNATI": "surah only (the book treats the link between whole surahs; ayah numbers are deliberately not set). "
                "10/10 surahs correct. Quality: good (surah level).",
    "SUYUTI-TANASUQ": "surah only (munāsabāt between whole surahs); 10/10 surahs correct. Quality: good (surah level).",
    "QUSHAYRI": "9/10 correct, 1 off by two (50:25 filed 50:27). Quality: good.",
    "SULAMI": "10/10 correct ([الآية: n] markers). Quality: good.",
    "TUSTARI": "altafsir surah.ayah headings (structural). Quality: good.",
    "BURSEVI": "10/10 correct; ~27% (Persian/Turkish verse, excursuses) carry the surah only. Quality: good.",
    "TABATABAI": "altafsir surah.ayah headings (structural); the long baḥth sections carry the passage range. "
                 "Quality: good.",
    "QASHANI": "altafsir surah.ayah headings (structural). Quality: good.",
    "JISHUMI": "9/10 correct where assigned, but only ~42% of segments carry an ayah (auto-tagged headings, sections "
               "al-lugha/al-iʿrāb/al-maʿnā without quotations). Quality: partial.",
}
