"""Source registry for the meal / translation corpus (fetch_meal.py).
primary = the witness whose text becomes segments.jsonl; cross = other hosts' texts of the same work,
compared over S1, S22, S87-114 (agreement written into source.json.notes)."""

LIC = {
    'tanzil': 'tanzil.net translation terms: non-commercial use, verbatim, cite tanzil.net; rights remain with translator/publisher; local research copy only.',
    'fawaz': 'fawazahmed0/quran-api (repo released as Unlicense, but the texts are collected from third-party sites and stay under their owners\' rights); local research copy only.',
    'alqc': 'api.alquran.cloud (Islamic Network) public API; text rights remain with the translator/publisher; local research copy only.',
    'quranenc': 'QuranEnc.com terms: free non-commercial use with attribution, no modification; local research copy only.',
    'kd': '(c) T.C. Diyanet İşleri Başkanlığı (kuran.diyanet.gov.tr); no open licence stated; local research copy only.',
    'km': 'kuranmeali.com aggregator; no licence stated; rights remain with translator/publisher; local research copy only.',
    'ak': 'acikkuran.com: CC BY-NC-SA 4.0, name the translator (robots Content-Signal: ai-train=no); local research copy only.',
    'mo': 'mealler.org aggregator; no licence stated; rights remain with translator/publisher; local research copy only.',
    'svm': 'suleymaniyevakfimeali.com (publisher\'s own site): "Tüm hakları saklıdır"; local research copy only.',
}

# kuranmeali.com div key -> (host label, about-page id)
KM = {
    'golpinarli': ('Abdulbaki Gölpınarlı Meali', 3), 'aakgul': ('Abdullah-Ahmet Akgül Meali', 36),
    'aparliyan': ('Abdullah Parlıyan Meali', 5), 'ahmettekin': ('Ahmet Tekin Meali', 7),
    'ahmetvarol': ('Ahmet Varol Meali', 6), 'abulac': ('Ali Bulaç Meali', 4),
    'alifikriyavuz': ('Ali Fikri Yavuz Meali', 8), 'bahaeddinsaglam': ('Bahaeddin Sağlam Meali', 30),
    'bayraktar': ('Bayraktar Bayraklı Meali', 9), 'besimatalay': ('Besim Atalay Meali (1965)', 34),
    'cemalkulunkoglu': ('Cemal Külünkoğlu Meali', 10), 'cemilsaid': ('Cemil Said (1924)', 42),
    'diyanetislerieski': ('Diyanet İşleri Meali (Eski)', 11), 'diyanetisleriyeni': ('Diyanet İşleri Meali (Yeni)', 13),
    'kuranyolu': ("Kur'an Yolu (Diyanet İşleri)", 110), 'diyanetvakfi': ('Diyanet Vakfı Meali', 14),
    'elmalilisade': ('Elmalılı Hamdi Yazır Meali', 16), 'elmaliliorj': ('Elmalılı Meali (Orijinal)', 17),
    'demiryent': ('Emrah Demiryent Meali', 92), 'erhanaktas': ('Erhan Aktaş Meali', 37),
    'hbasricantay': ('Hasan Basri Çantay Meali', 18), 'haydarozturkserkanyilmaz': ('Haydar Öztürk-Serkan Yılmaz Meali', 119),
    'hayrat': ('Hayrat Neşriyat Meali', 19), 'ihsanaktas': ('İhsan Aktaş Meali', 118),
    'ilyasyorulmaz': ('İlyas Yorulmaz Meali', 35), 'baltacioglu': ('İsmayıl Hakkı Baltacıoğlu', 55),
    'ismailhakkiizmirli': ('İsmail Hakkı İzmirli', 40), 'ismailyakit': ('İsmail Yakıt', 105),
    'kadricelik': ('Kadri Çelik Meali', 20), 'mahmutkisa': ('Mahmut Kısa Meali', 33),
    'mahmutozdemir': ('Mahmut Özdemir Meali', 46), 'mehmetcakir': ('Mehmet Çakır Meali', 44),
    'mehmetcoban': ('Mehmet Çoban Meali', 72), 'mehmetokuyan': ('Mehmet Okuyan Meali', 45),
    'mehmetturk': ('Mehmet Türk Meali', 12), 'muhammedesed': ('Muhammed Esed Meali', 100),
    'mustafacavdar': ('Mustafa Çavdar Meali', 38), 'islamoglu': ('Mustafa İslamoğlu Meali', 31),
    'orhankuntman': ('Orhan Kuntman Meali', 104), 'osmanfirat': ('Osman Fırat Meali', 111),
    'omererdogdu': ('Ömer Erdoğdu Meali', 121), 'omernasuhi': ('Ömer Nasuhi Bilmen Meali', 21),
    'syildirim': ('Suat Yıldırım Meali', 23), 'sates': ('Süleyman Ateş Meali', 24),
    'suleymantevfik': ('Süleyman Tevfik (1927)', 63), 'abayindir': ('Süleymaniye Vakfı Meali', 32),
    'spiris': ('Şaban Piriş Meali', 25), 'simsek': ('Ümit Şimşek Meali', 26), 'ynuri': ('Yaşar Nuri Öztürk Meali', 27),
    'eskianadoluturkcesi': ('Eski Anadolu Türkçesi', 41), 'satiralti': ('Satıraltı Meal (1534)', 43),
}

AK_IDS = {'Mustafa İslamoğlu': 38, 'Mehmet Okuyan': 107, 'Bayraktar Bayraklı': 8, 'Süleymaniye Vakfı': 52,
          'Süleymaniye Vakfı (Eski Baskı)': 117, 'Erhan Aktaş': 105, 'Ahmed Hulusi': 3, 'Gültekin Onan': 18,
          'Ali Rıza Safa': 51, 'Muhammed Esed': 22, 'Hasan Basri Çantay': 19, 'Elmalılı Hamdi Yazır': 14,
          'Elmalılı (sadeleştirilmiş)': 15}


def S(id, title, author, primary, cross=(), panel=False, lineage=None, relay=None, kind='meal', language='tr',
      tradition='', edition='', notes='', death_ah=None, translator=None, notes_from=None):
    return dict(id=id, title=title, author=author, primary=primary, cross=list(cross), panel=panel, lineage=lineage,
                relay=relay, kind=kind, language=language, tradition=tradition, edition=edition, notes=notes,
                death_ah=death_ah, translator=translator or author, notes_from=notes_from)


SOURCES = [
    # ------------------------------------------------------------ THE PANEL (16)
    S('MEAL-DIB', "Kur'an-ı Kerim Meali (Diyanet İşleri Başkanlığı, current)",
      'Halil Altuntaş & Muzaffer Şahin (Diyanet İşleri Başkanlığı, Din İşleri Yüksek Kurulu)',
      'kd:1', ['km:diyanetisleriyeni', 'ak:Diyanet İşleri'], panel=True, lineage='diyanet', tradition='official-sunni',
      edition='kuran.diyanet.gov.tr Mushaf, meal ML=1 (current DİB meal, with verse groups as on the site)',
      notes_from='km:diyanetisleriyeni',
      notes='Identity: kuranmeali.com about-page (id 13) names the official current DİB meal as prepared by Halil Altuntaş and Muzaffer Şahin; '
            'kd ML=1 = kuranmeali "Diyanet İşleri Meali (Yeni)" = acikkuran "Diyanet İşleri" (see cross-check). The DİB footnotes are not in the '
            'kuran.diyanet page data; they are attached from kuranmeali.com (notes_host) where present. kuranmeali\'s square-bracketed numbers in '
            'this meal are footnote markers, not translator additions.'),
    S('MEAL-DIB1961', "Kur'an-ı Kerim ve Türkçe Anlamı (Diyanet İşleri, 1961; Hüseyin Atay - Yaşar Kutluay)",
      'Hüseyin Atay & Yaşar Kutluay (Diyanet İşleri Başkanlığı)', 'tanzil:tr.diyanet',
      ['fawaz:tur-diyanetisleri', 'km:diyanetislerieski', 'mo:Diyanet İşleri (eski)', 'mo:Bekir Sadak'],
      panel=True, lineage='diyanet-1961', tradition='official-sunni',
      edition='tanzil tr.diyanet (last update 2011-12-27); identified by kuranmeali.com as the old 1961 Diyanet meal (Atay-Kutluay)',
      notes='Identity: kuranmeali.com about-page (id 11): e-text of the DİB meal, first edition 1961, prepared by Dr. Hüseyin Atay and Dr. Yaşar '
            'Kutluay under Hasan Hüsnü Erdem and Yusuf Ziyaeddin Ersal, revised by a committee chaired by Mahir İz; used by DİB until c. 1990. '
            'tanzil tr.diyanet = fawaz tur-diyanetisleri = kuranmeali "Diyanet İşleri Meali (Eski)" = mealler.org "Diyanet İşleri (eski)". '
            'mealler.org "Bekir Sadak" is also this text (~88% identical, ASCII-ised variants), i.e. a mislabelled copy. '
            'tanzil represents a merged verse group by repeating the group text on each ayah; consecutive identical ayat are stored once as a..a_end '
            '(except Arabic near-twins such as 94:5-6, 102:3-4).'),
    S('MEAL-TDV', "Kur'an-ı Kerim Meali (Türkiye Diyanet Vakfı)",
      'Ali Özek, Hayreddin Karaman, Ali Turgut, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadreddin Gümüş',
      'kd:4', ['km:diyanetvakfi', 'mo:Diyanet Vakfi', 'quranenc:turkish_shahin', 'tanzil:tr.vakfi'],
      panel=True, lineage='diyanet', tradition='official-sunni',
      edition='kuran.diyanet.gov.tr Mushaf, meal ML=4 (official grouped TDV meal)', notes_from='km:diyanetvakfi',
      notes='TDV "açıklamalı meal" explanatory notes are not in the kuran.diyanet page data; attached from kuranmeali.com "Diyanet Vakfı Meali" '
            '(notes_host). Page-range division of labour (kuranmeali about-page id 14, from the TDV preface): Özek pp. 1-48, 581-604; Karaman 76-126; '
            'Çağrıcı 49-62, 281-358; Dönmez 63-75, 358-420, 561-580; Gümüş 127-280; Turgut 421-560. kuran.diyanet ML=4 lacks Turkish letters in '
            'some passages (e.g. 108:1-3 "Kuskusuz", "Simdi", "süphesiz") - a host data defect, kept as published.'),
    S('MEAL-KURANYOLU', "Kur'an Yolu Türkçe Meal (Diyanet İşleri Başkanlığı)",
      'Hayreddin Karaman, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadrettin Gümüş', 'kd:5', ['km:kuranyolu'],
      panel=True, lineage='diyanet', tradition='official-sunni', edition='kuran.diyanet.gov.tr Mushaf, meal ML=5'),
    S('MEAL-ELMALILI', "Hak Dini Kur'an Dili - meal (original wording)", 'Elmalılı Muhammed Hamdi Yazır', 'kd:6',
      ['ak:Elmalılı Hamdi Yazır', 'km:elmaliliorj', 'mo:Elmalılı Hamdi Yazır'], panel=True, tradition='ottoman-late-hanafi',
      death_ah=1361, edition='kuran.diyanet.gov.tr Mushaf, meal ML=6 (Elmalılı original)',
      notes='ORTHOGRAPHY CAVEAT: the kuran.diyanet text is the original wording in lightly modernised spelling (şüphesiz, hakikaten, Rabbin, '
            '"Allah Tealâ\'nın adıyla (Okumaya başlarım)" at 1:1) and it re-divides some sentences across ayat (22:42-43, 89:19-20, 91:14-15). '
            'kuranmeali.com "Elmalılı Meali (Orijinal)" keeps the 1935 spelling (şübhesiz, hakıkaten, rabbının, va\'dinde) and is the better witness '
            'for the original orthography; acikkuran (author 14) = mealler.org (~99%), same e-text as kuranmeali but circumflex-stripped on acikkuran. '
            'Agreement with each is only ~70-75% per ayah for these reasons, not because of different translations.'),
    S('MEAL-BILMEN', "Kur'ân-ı Kerîm'in Türkçe Meâl-i Âlîsi ve Tefsiri", 'Ömer Nasuhi Bilmen', 'km:omernasuhi',
      ['mo:Ömer Nasuhi Bilmen'], panel=True, tradition='ottoman-late-hanafi', death_ah=1391,
      notes='kuranmeali.com gives one rendering per ayah; mealler.org repeats Bilmen\'s connected renderings across short ayat (e.g. 89:2-4, 100:1-2), '
            'which explains most per-ayah disagreement (~70% identical).'),
    S('MEAL-CANTAY', "Kur'ân-ı Hakîm ve Meâl-i Kerîm", 'Hasan Basri Çantay', 'km:hbasricantay',
      ['ak:Hasan Basri Çantay', 'fawaz:tur-hasanbasricanta', 'mo:Hasan Basri Çantay'], panel=True, death_ah=1384),
    S('MEAL-ATES', "Kur'ân-ı Kerîm ve Yüce Meâli", 'Süleyman Ateş', 'mo:Süleyman Ateş',
      ['tanzil:tr.ates', 'fawaz:tur-suleymanates', 'km:sates', 'ak:Süleyman Ateş'], panel=True, tradition='academic',
      notes='Primary is mealler.org because it is the only host that keeps the circumflexes (Allâh, Âlemlerin, sâhibi); tanzil/kuranmeali/acikkuran '
            'carry the same wording with circumflexes stripped.'),
    S('MEAL-BULAC', "Kur'an-ı Kerim ve Türkçe Anlamı", 'Ali Bulaç', 'tanzil:tr.bulac',
      ['fawaz:tur-alibulac', 'km:abulac', 'ak:Ali Bulaç', 'mo:Ali Bulaç'], panel=True),
    S('MEAL-ESED', "Kur'an Mesajı (Turkish of Asad, The Message of the Qur'an)",
      'Muhammad Asad (Turkish: Cahit Koytak & Ahmet Ertürk)', 'km:muhammedesed',
      ['fawaz:tur-muhammedesed', 'ak:Muhammed Esed', 'mo:Muhammed Esed'], panel=True, relay='ASAD-EN',
      tradition='reformist', translator='Cahit Koytak & Ahmet Ertürk', death_ah=1412,
      edition="İşaret Yayınları (1999); text as on kuranmeali.com"),
    S('MEAL-YNOZTURK', "Kur'an-ı Kerim Meali", 'Yaşar Nuri Öztürk', 'tanzil:tr.ozturk',
      ['km:ynuri', 'ak:Yaşar Nuri Öztürk', 'fawaz:tur-yasarnuriozturk', 'fawaz:tur-ynozturk', 'mo:Yaşar Nuri Öztürk'],
      panel=True, tradition='reformist', notes='fawaz "tur-ynozturk" (from qurandatabase.org) is a variant edition (~79%).'),
    S('MEAL-ISLAMOGLU', "Hayat Kitabı Kur'an (current revised edition)", 'Mustafa İslamoğlu', 'km:islamoglu',
      ['ak:Mustafa İslamoğlu', 'mo:Mustafa İslamoğlu'], panel=True,
      notes='kuranmeali.com carries a later revised edition with the numbered footnotes (e.g. 107:1 "BAK ŞU Hesap Günü\'nü yalanlayan kişiye!"); '
            'acikkuran.com and mealler.org carry an earlier edition (107:1 "Allah\'a karşı borçluluk sorumluluğunu tümden inkar eden birini tasavvur '
            'edebilir misin!"), kept separately as MEAL-ISLAMOGLU-ESKI. Square brackets with superscript numbers in the text are footnote markers.'),
    S('MEAL-OKUYAN', "Kur'an Meal-Tefsir", 'Mehmet Okuyan', 'ak:Mehmet Okuyan', ['km:mehmetokuyan', 'mo:Mehmet Okuyan'],
      panel=True, tradition='academic',
      notes='BRACKET CAVEAT: hosts disagree on markup. kuranmeali.com puts retained Arabic terms in square brackets ("[Rahmân], [Rahîm] [*]", '
            '"[salât]larından", "[Beyyine] [*](apaçık bir elçi)"); acikkuran.com (primary) has plain terms with numbered footnotes; mealler.org has '
            'neither. Check the printed edition before judging Okuyan\'s marking of additions.'),
    S('MEAL-GOLPINARLI', "Kur'ân-ı Kerîm ve Meâli", 'Abdülbâki Gölpınarlı', 'mo:Abdulbaki Gölpınarlı',
      ['tanzil:tr.golpinarli', 'fawaz:tur-abdulbakigolpin', 'km:golpinarli'], panel=True, death_ah=1402,
      notes='Primary is mealler.org: it keeps the circumflexes (rahîmdir, kıyâmetin) and has fewer typos (1:7 "gazaba"; tanzil/fawaz "gazebe"). '
            'tanzil/fawaz/kuranmeali share one circumflex-stripped e-text.'),
    S('MEAL-SULEYMANIYE', 'Süleymaniye Vakfı Meali (current edition)', 'Süleymaniye Vakfı (Abdulaziz Bayındır et al.)',
      'svm:site', ['ak:Süleymaniye Vakfı', 'mo:Süleymaniye Vakfı'], panel=True,
      edition="publisher's site suleymaniyevakfimeali.com (whole surah per page, with footnotes)",
      notes='The meal is revised continuously (kuranmeali about-page id 32). Versions found: publisher site (primary) ~80% = acikkuran author 52; '
            'mealler.org "Süleymaniye Vakfı" a further, different version (~4% identical to the current text); the old edition is MEAL-SULEYMANIYE-ESKI '
            '(acikkuran 117 = kuranmeali "abayindir"). [*] / [1*] in the text are the site\'s footnote markers.'),
    S('MEAL-HAYRAT', "Muhtasar Kur'ân meâli (Hayrat Neşriyat)", 'Hayrat Neşriyat (ten-member committee, İlmî Araştırma Merkezi)', 'km:hayrat',
      ['mo:Hayrat Neşriyat'], panel=True, tradition='nurcu'),

    # ------------------------------------------------------------ English
    S('ASAD-EN', "The Message of the Qur'an (translation only, no notes)", 'Muhammad Asad', 'alqc:en.asad', ['fawaz:eng-muhammadasad', 'ak:Muhammad Asad'],
      kind='translation', language='en', tradition='reformist', death_ah=1412),
    S('ARBERRY', 'The Koran Interpreted', 'Arthur J. Arberry', 'tanzil:en.arberry', ['fawaz:eng-ajarberry', 'ak:Arthur John Arberry'],
      kind='translation', language='en', tradition='academic',
      notes='Literal English control for the meal review (what any translation loses vs what Turkish meals lose).'),

    # ------------------------------------------------------------ reference set
    S('MEAL-ISLAMOGLU-ESKI', "Hayat Kitabı Kur'an (earlier edition)", 'Mustafa İslamoğlu', 'ak:Mustafa İslamoğlu',
      ['mo:Mustafa İslamoğlu'], notes='Earlier edition; the current revised text is MEAL-ISLAMOGLU (kuranmeali.com).'),
    S('MEAL-SULEYMANIYE-ESKI', 'Süleymaniye Vakfı Meali (earlier edition)', 'Süleymaniye Vakfı (Abdulaziz Bayındır et al.)',
      'ak:Süleymaniye Vakfı (Eski Baskı)', ['km:abayindir']),
    S('MEAL-ELMALILI-SADE', "Elmalılı meali, sadeleştirilmiş (A)", 'Elmalılı Muhammed Hamdi Yazır (simplified by unnamed editors)',
      'tanzil:tr.yazir', ['km:elmalilisade', 'fawaz:tur-elmalilihamdiya', 'fawaz:tur-diyanetisleri1', 'fawaz:tur-elmallsadelesti1'],
      notes='Simplified (sadeleştirilmiş) Elmalılı, not the original wording (original = MEAL-ELMALILI). tanzil labels it "Elmalılı Hamdi Yazır" '
            '(tr.yazir) without saying it is simplified. fawaz "tur-diyanetisleri1" (label "Diyanet Isleri") is this same text (~98%): a misattribution. '
            'fawaz "tur-elmallsadelesti1" is a variant of it (~79%).'),
    S('MEAL-ELMALILI-SADE-B', 'Elmalılı meali, sadeleştirilmiş (B)', 'Elmalılı Muhammed Hamdi Yazır (simplified by unnamed editors)',
      'fawaz:tur-elmallsadelesti', ['ak:Elmalılı (sadeleştirilmiş)'],
      notes='A second simplified Elmalılı text, distinct from MEAL-ELMALILI-SADE (~10% identical); = acikkuran "Elmalılı (sadeleştirilmiş)" (author 15), ~81%.'),
    S('MEAL-TDV-DUZ', 'Diyanet Vakfı meali, earlier ungrouped e-text (circulates online also as "Adem Uğur")',
      'Ali Özek, Hayreddin Karaman, Ali Turgut, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadreddin Gümüş (TDV committee)',
      'tanzil:tr.vakfi', ['mo:Adem Uğur', 'fawaz:tur-diyanetvakfi', 'fawaz:tur-ademugur'],
      lineage='diyanet', edition='tanzil tr.vakfi ("Diyanet Vakfı"); per-ayah text without the official verse groups',
      notes='Identity: wording equals the official grouped TDV meal (kd ML=4) wherever that meal does not group (1:5, 1:7, 93:7) and shows an '
            'earlier revision elsewhere (22:46 "(Sana karşı çıkanlar)" vs kd "(Seni yalanlayanlar)"). The same e-text is labelled "Adem Uğur" on '
            'mealler.org and fawazahmed0 (tur-ademugur); no evidence was found that it is a separate Adem Uğur translation, so the label is treated '
            'as a misattribution of the TDV text (host label kept here for the record).'),
    S('MEAL-TDV-QE', 'Diyanet Vakfı text as revised for QuranEnc ("Dr. Ali Ozek and others")',
      'Ali Özek et al. (revised under Rowad Translation Center)', 'quranenc:turkish_shahin', ['fawaz:tur-muslimshahin'],
      lineage='diyanet', edition='QuranEnc turkish_shahin v1.0.0',
      notes='QuranEnc key "turkish_shahin" / fawaz "Muslim Shahin" is the TDV (Özek et al.) text revised for QuranEnc: ~60% identical to the TDV '
            'e-text (1:5 "Ancak sana ibadet (kulluk) eder ve ancak senden yardım isteriz"). The "Shahin" label does not name the translator.'),
    S('MEAL-SYILDIRIM', "Kur'an-ı Hakîm ve Açıklamalı Meali", 'Suat Yıldırım', 'km:syildirim',
      ['tanzil:tr.yildirim', 'fawaz:tur-suatyildirim', 'mo:Suat Yıldırım'],
      notes='kuranmeali text = tanzil tr.yildirim, plus footnotes. fawaz tur-suatyildirim and mealler.org carry a different edition (~80%).'),
    S('MEAL-YUKSEL', "Mesaj: Kur'an Çevirisi", 'Edip Yüksel', 'tanzil:tr.yuksel', ['fawaz:tur-edipyuksel'],
      tradition='quranist',
      notes='EXCLUDED FROM THE PANEL. mealler.org removed this text under ANKARA 4. SULH CEZA HAKİMLİĞİ decision of 24.06.2026, '
            'no. 2026/6172 D. İş (the page now shows that notice); acikkuran.com no longer lists it either. Text here is tanzil tr.yuksel only.'),
    S('MEAL-AFYAVUZ', "Kur'ân-ı Kerîm ve Meâl-i Âlîsi", 'Ali Fikri Yavuz', 'km:alifikriyavuz', ['fawaz:tur-alifikriyavuz', 'mo:Ali Fikri Yavuz']),
    S('MEAL-CYILDIRIM', "Kur'an-ı Kerim meali", 'Celal Yıldırım', 'mo:Celal Yıldırım', ['fawaz:tur-celalyldrm'],
      notes='fawaz label "Celal Y Ld R M" (broken diacritics). fawaz and mealler.org group verses differently (e.g. 113), hence ~68% per-ayah equality.'),
    S('MEAL-IBNKESIR-ANON', "Meal printed in a Turkish edition of İbn Kesîr's tafsir (translator not named)", 'anonymous',
      'ak:İbni Kesir', ['mo:İbni Kesir', 'fawaz:tur-ibnikesir'],
      notes='Host label "Ibni Kesir" names the tafsir, not the translator; the meal is anonymous. Not Ibn Kathīr\'s own text.'),
    S('MEAL-FIZILAL', "Fî Zılâli'l-Kur'ân - Turkish meal lines", 'Sayyid Quṭb (Turkish translators: Salih Uçan et al.)',
      'mo:Seyyid Kutub', ['fawaz:tur-fizilalilkuran'], relay='Quṭb\'s Arabic paraphrase (Fī ẓilāl al-Qurʾān)',
      notes='Relay witness: the Turkish renders Quṭb\'s paraphrase, not the Qur\'an directly.'),
    S('MEAL-TEFHIM', "Tefhîmu'l-Kur'ân - Turkish meal", 'Abul Aʿla Mawdudi (Turkish: İnsan Yayınları team)',
      'mo:Tefhim-ul Kuran', ['fawaz:tur-tefhimulkuran'], relay="Mawdudi's Urdu Tafhīm al-Qurʾān (English consulted)",
      notes='Relay witness (Urdu -> Turkish). The Turkish Tefhîm team (İnsan Yayınları) included Ali Bulaç: its meal lines are ~73% identical to '
            'MEAL-BULAC over S1, S22, S87-114, so the two are not independent witnesses.'),
    S('MEAL-PIRIS', "Kur'an-ı Kerim Türkçe Anlamı", 'Şaban Piriş', 'km:spiris', ['fawaz:tur-sabanpiris', 'ak:Şaban Piriş', 'mo:Şaban Piriş']),
    S('MEAL-PIRIS-REV', 'Şaban Piriş meali, revised (QuranEnc "Shaaban British")', 'Şaban Piriş (revised under Rowad Translation Center)',
      'quranenc:turkish_shaban', ['fawaz:tur-shabanbritch'],
      notes='QuranEnc label "Shaaban British"/fawaz "Shaban Britch" = Şaban Piriş, revised.'),
    S('MEAL-RWWAD', 'Turkish translation, Rowwad Translation Center', 'Rowwad Translation Center (team)', 'quranenc:turkish_rwwad',
      ['fawaz:tur-wwwislamhouseco'], notes='fawaz "www.islamhouse.com" = this text (~99%). ~26% identical to MEAL-DIB: draws on the DİB meal.'),
    S('MEAL-BAYRAKLI', "Yeni Bir Anlayışın Işığında Kur'an Meali", 'Bayraktar Bayraklı', 'km:bayraktar', ['ak:Bayraktar Bayraklı', 'mo:Bayraktar Bayraklı']),
    S('MEAL-EAKTAS', "Kerim Kur'an", 'Erhan Aktaş', 'ak:Erhan Aktaş', ['km:erhanaktas', 'mo:Erhan Aktaş', 'ak:Erhan Aktaş (Eski Baskı)', 'ak:Erhan Aktaş (10. Baskı)'],
      notes='At least four revisions circulate: acikkuran current / 10th printing / old printing, kuranmeali (sent by the author, updated 2026-09-02) '
            'and mealler.org; they agree on only ~50-94% of ayat.'),
    S('MEAL-HULUSI', "Türkçe Kur'an Çözümü", 'Ahmed Hulusi', 'ak:Ahmed Hulusi', ['mo:Ahmed Hulusi'], tradition='sufi-modern'),
    S('MEAL-ONAN', "Kur'an-ı Kerim meali", 'Gültekin Onan', 'ak:Gültekin Onan', ['fawaz:tur-gultekinonan', 'mo:Gültekin Onan'],
      notes='~69% identical to MEAL-BULAC over S1, S22, S87-114: not an independent witness to Bulaç.'),
    S('MEAL-SAFA', "Kur'an-ı Kerim Gerçek", 'Ali Rıza Safa', 'ak:Ali Rıza Safa'),
    S('MEAL-UNAL', "Kur'an-ı Kerim ve Açıklamalı Meali", 'Ali Ünal', 'mo:Ali Ünal'),
    S('MEAL-ALIMIHR', 'Kur\'an-ı Kerim meali', 'İskender Ali Mihr', 'fawaz:tur-iskenderalimihr'),
    S('MEAL-HYILMAZ', 'İşte Kur\'an', 'Hakkı Yılmaz', 'mo:Hakkı Yılmaz'),
    S('MEAL-HARUNYILDIRIM', 'Kur\'an meali', 'Harun Yıldırım', 'mo:Harun Yıldırım'),
    S('MEAL-EROGLU', 'Kur\'an meali (verse)', 'Mehmet Ali Eroğlu', 'mo:Mehmet Ali Eroğlu'),
    S('MEAL-SEMS', 'Kur\'an meali', 'Muhammed Celal Şems', 'mo:Muhammed Celal Şems'),
    S('MEAL-CEVIK', 'Kur\'an meali', 'Mustafa Çevik', 'mo:Mustafa Çevik'),
    S('MEAL-ONGUT', 'Kur\'an meali', 'Ömer Öngüt', 'mo:Ömer Öngüt'),
    S('MEAL-TURKMEN', 'Kur\'an meali', 'Sadık Türkmen', 'mo:Sadık Türkmen'),
    S('MEAL-SIMSEK', 'Kur\'an meali', 'Ümit Şimşek', 'km:simsek', ['mo:Ümit Şimşek']),
    S('MEAL-KCELIK', 'Kur\'an meali', 'Kadri Çelik', 'km:kadricelik', ['mo:Kadri Çelik']),
    S('MEAL-KULUNKOGLU', "Kur'an-ı Kerim Gerekçeli ve Açıklamalı Meali", 'Cemal Külünkoğlu', 'km:cemalkulunkoglu', ['mo:Cemal Külünkoğlu'],
      notes='kuranmeali.com and mealler.org carry two different Külünkoğlu texts (~16% identical over S1, S22, S87-114; e.g. 89:7 grouped vs '
            'single-ayah, 22:3 different wording): different editions or revisions. kuranmeali (with notes) is primary; neither is dated on its host.'),
    S('MEAL-PARLIYAN', 'Kur\'an meali', 'Abdullah Parlıyan', 'km:aparliyan', ['mo:Abdullah Parlıyan']),
    S('MEAL-VAROL', 'Kur\'an meali', 'Ahmet Varol', 'km:ahmetvarol', ['mo:Ahmet Varol']),
    S('MEAL-TEKIN', 'Kur\'an meali', 'Ahmet Tekin', 'km:ahmettekin', ['mo:Ahmet Tekin']),
    S('MEAL-AKGUL', 'Kur\'an meali', 'Abdullah & Ahmet Akgül', 'km:aakgul'),
    S('MEAL-SAGLAM', 'Kur\'an meali', 'Bahaeddin Sağlam', 'km:bahaeddinsaglam'),
    S('MEAL-ATALAY', 'Kur\'an meali (1965)', 'Besim Atalay', 'km:besimatalay'),
    S('MEAL-CEMILSAID', 'Kur\'ân-ı Kerîm Tercümesi (1924)', 'Cemil Said', 'km:cemilsaid', relay="Kazimirski's French",
      notes='First printed Turkish translation; made from Kazimirski\'s French (relay).'),
    S('MEAL-DEMIRYENT', 'Kur\'an meali', 'Emrah Demiryent', 'km:demiryent'),
    S('MEAL-HOZTURK-SYILMAZ', 'Kur\'an meali', 'Haydar Öztürk & Serkan Yılmaz', 'km:haydarozturkserkanyilmaz'),
    S('MEAL-IAKTAS', 'Kur\'an meali', 'İhsan Aktaş', 'km:ihsanaktas'),
    S('MEAL-YORULMAZ', 'Kur\'an meali', 'İlyas Yorulmaz', 'km:ilyasyorulmaz'),
    S('MEAL-BALTACIOGLU', 'Kur\'an meali', 'İsmayıl Hakkı Baltacıoğlu', 'km:baltacioglu'),
    S('MEAL-IZMIRLI', 'Kur\'an meali', 'İsmail Hakkı İzmirli', 'km:ismailhakkiizmirli'),
    S('MEAL-YAKIT', 'Kur\'an meali', 'İsmail Yakıt', 'km:ismailyakit'),
    S('MEAL-KISA', 'Kur\'an meali', 'Mahmut Kısa', 'km:mahmutkisa'),
    S('MEAL-MOZDEMIR', 'Kur\'an meali', 'Mahmut Özdemir', 'km:mahmutozdemir'),
    S('MEAL-CAKIR', 'Kur\'an meali', 'Mehmet Çakır', 'km:mehmetcakir'),
    S('MEAL-COBAN', 'Kur\'an meali', 'Mehmet Çoban', 'km:mehmetcoban'),
    S('MEAL-MTURK', 'Kur\'an meali', 'Mehmet Türk', 'km:mehmetturk'),
    S('MEAL-CAVDAR', 'Kur\'an meali', 'Mustafa Çavdar', 'km:mustafacavdar'),
    S('MEAL-KUNTMAN', 'Kur\'an meali', 'Orhan Kuntman', 'km:orhankuntman'),
    S('MEAL-OFIRAT', 'Kur\'an meali', 'Osman Fırat', 'km:osmanfirat'),
    S('MEAL-ERDOGDU', 'Kur\'an meali', 'Ömer Erdoğdu', 'km:omererdogdu'),
    S('MEAL-STEVFIK', 'Kur\'an meali (1927)', 'Süleyman Tevfik', 'km:suleymantevfik'),
    S('MEAL-ESKIANADOLU', 'Old Anatolian Turkish interlinear meal', 'anonymous', 'km:eskianadoluturkcesi',
      notes='Historical text as presented by kuranmeali.com; edition and manuscript not stated on the host.'),
    S('MEAL-SATIRALTI', 'Satıraltı meal (1534)', 'anonymous', 'km:satiralti',
      notes='Historical interlinear text as presented by kuranmeali.com; edition not stated on the host.'),
]

TEFSIR = S('KURANYOLU-TEFSIR', "Kur'an Yolu: Türkçe Meal ve Tefsir (tefsir text)",
           'Hayreddin Karaman, Mustafa Çağrıcı, İbrahim Kâfi Dönmez, Sadrettin Gümüş', 'kdtefsir:1', kind='tafsir_tr',
           lineage='diyanet', tradition='official-sunni',
           edition="kuran.diyanet.gov.tr Mushaf, tefsir route (TefsirList); each unit carries its print reference (Kur'an Yolu Tefsiri cilt/sayfa) in 'ref'")

POINTERS = [
    dict(id='MEAL-MOZTURK', title="Kur'an-ı Kerim Meali: Anlam ve Yorum Merkezli Çeviri", author='Mustafa Öztürk',
         kind='meal', language='tr', tradition='academic',
         edition='Ankara Okulu Yayınları (several editions since 2011)', panel=False,
         notes='Pointer only (access hafiza): no licensed online text. PDFs circulate only on unlicensed mirrors; deliberately NOT downloaded. '
               'Anything cited from it is model memory and must be marked so.'),
    dict(id='ASAD-NOTES', title="The Message of the Qur'an - commentary notes", author='Muhammad Asad', death_ah=1412,
         kind='modern', language='en', tradition='reformist', edition='Dar al-Andalus, Gibraltar 1980 (notes); Turkish notes in İşaret 1999',
         panel=False,
         notes='Pointer only (access hafiza). Full-text copies with notes exist online only on unlicensed mirrors (e.g. PDF re-uploads and '
               'islamicity-style HTML copies); deliberately NOT downloaded. The Turkish notes (Koytak-Ertürk) appear in truncated form in '
               'MEAL-ESED notes from kuranmeali.com (notes_truncated: true).'),
    dict(id='MEAL-HAMIDULLAH', title="Aziz Kur'an: Kur'ân-ı Kerîm'in Türkçe Meâli (from Hamidullah's French)",
         author='Muhammed Hamidullah (Turkish: Abdülaziz Hatip & Mahmut Kanık)', kind='meal', language='tr',
         relay="Hamidullah's French Le Saint Coran", edition='Beyan Yayınları', panel=False,
         notes='Pointer only (access hafiza): no licensed online text found.'),
    dict(id='MEAL-ATAY', title="Kur'an-ı Kerim Türkçe Çeviri (solo meal)", author='Hüseyin Atay', kind='meal', language='tr',
         edition='Atay\'s later single-author meal (various editions)', panel=False,
         notes='Pointer only (access hafiza). Co-author of the 1961 Diyanet meal (MEAL-DIB1961); his own later choices show what the 1961 '
               'compromise cost. No licensed online text found.'),
]


def all_sources():
    return SOURCES + [TEFSIR]


def witness_homes():
    """single-file witness -> source dir that keeps its raw file."""
    homes = {}
    for src in SOURCES:                     # a witness lives with the source that uses it as primary ...
        w = src['primary']
        if w.split(':', 1)[0] in ('tanzil', 'fawaz', 'quranenc', 'alqc'):
            homes.setdefault(w, src['id'])
    for src in SOURCES:                     # ... else with the first source that cross-checks against it
        for w in src['cross']:
            host = w.split(':', 1)[0]
            if host in ('tanzil', 'fawaz', 'quranenc', 'alqc'):
                homes.setdefault(w, src['id'])
    return homes
