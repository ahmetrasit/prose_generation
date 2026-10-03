# -*- coding: utf-8 -*-
# Annotation block data, part B: sections 1 (late additions), 3-10.
B = []

def add(anchor, **kw):
    B.append((anchor, kw))

CHK = "Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)"

# ------------------------------------------------------------ SECTION 1 late: yura'un meal review
add(5, id="S107-MEAL-010", type="semantic_history", tradition="historical", ayah="107:6", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="extended", audience="general",
    term="yurâûn", scope="meal-review:yurâûn", scholar="Diyanet|Ateş|Hayrat|Bilmen|Çantay|Elmalılı|Esed|İslamoğlu|Öztürk",
    prose="Meal incelemesi: “yurâûn”. Çoğu meal fiili “gösteriş yaparlar” diye verir (Diyanet, Okuyan, Süleymaniye Vakfı, Bulaç). Üç fark görülür. (1) Parantezli kapsam: güncel Diyanet “Onlar (namazlarıyla) gösteriş yaparlar”, Ateş “gösteriş (için ibadet) yaparlar”, Hayrat “riyâkârlık (gösteriş için ibâdet) ederler” der. Namazla sınırlama Ali’den gelen “yurâûne bi-salâtihim” rivayetiyle (Süyûtî) ve Taberî’nin bağlam okumasıyla desteklenir; öte yandan Bikâî “namazlarıyla ve başka işleriyle” der, Kurtubî riyanın dört biçimini sayar; parantez kapsamı daraltır ama okura bunu gösterir. Gölpınarlı’nın “bütün işlerini gösteriş için yaparlar” ifadesi tersine kapsamı bütün işlere genişletir ve Bikâî’nin okumasına yakındır. (2) İsim kalıbı: Bilmen “riyâkardırlar”, Çantay “riyakârların ta kendileridir”, Elmalılı özgün metin “mürailik ederler”, Hayrat “riyâkârlık ederler”. Fiil yerine sıfat/isim kullanmak Zemahşerî’nin müfâale vurgusundaki (gösteren işi gösterir, seyirci övgüyü gösterir) çift yönlülüğü silikleştirir; hata sayılmaz. (3) Niyete kayış: Esed “niyetleri yalnızca görülüp takdir edilmektir”, İslamoğlu “(ibadeti) gösteriye dönüştürürler”, Öztürk “Riyaya sapandır onlar”. Râzî’nin münafık ile müraî ayrımıyla (müraî kalbinde olmayan huşuu gösterir) uyumludur. Hiçbiri yanlış değildir; farklar kapsam ve vurgu farkıdır.",
    source="MEAL-DIY-107|MEAL-ATE-107|MEAL-HAY-107|MEAL-GOL-107|MEAL-BIL-107|MEAL-CAN-107|MEAL-ELM-107|MEAL-ESED-107|MEAL-ISL-107|MEAL-YNO-107|KASH-107|RAZI-107|SUY-107|BIQ-107|QURT-107|TAB-107")

# ------------------------------------------------------------ SECTION 3
add(33, id="S107-NOV-004", type="novelty", tradition="project", ayah="107:2", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="none_found_in_checked_sources",
    checked_sources="Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)|Maqayis(yatm,sahw)",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “yetim = gaflet ve gecikme” okuması için denetim. Kontrol edilen ayet sayfalarında yetim kelimesinin gaflet ya da gecikme kökenli açıklaması bulunmadı; klasik şerhler yetimi hak, mal ve ikram bağlamında ele alır (S107-SEM-003). Maqâyîs’in yetim maddesinde “her tek kalan şey yetimdir” tanımı vardır; “yetimin aslı gaflettir” ve “gecikmedir” tanımları baz metinde başka sözlük girişlerinden alınmıştır ve bu çalışmada yeniden doğrulanmamıştır. Sehv’in (5. ayet) ayrı bir kök olduğu tespiti doğrudur: Maqâyîs sehvi gaflet olarak verir. İki kökün gaflette buluşturulması proje sentezidir ve kontrol edilen kaynaklarda paralel görülmedi.",
    source="BASE-LEX|MAQ-SAHW")

add(35, id="S107-NOV-005", type="novelty", tradition="project", ayah="107:5|107:6", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="building_blocks_only",
    checked_sources="Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)|Maqayis(sahw)",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “Suhâ yıldızı” ve “gözden kaçıran gözden kaçmak ister” okuması için denetim. Yapıtaşları ayrı ayrı mevcuttur: Maqâyîs sehv maddesinde “Suhâ’ya gelince, birinci bâbdan olması muhtemeldir, çünkü çok gizlidir, görülmesinden gaflet edilir” der (varsayım kipiyle, kesin hükümsüz); sehvin gaflet olduğu klasik tefsirlerde açıktır; riyanın görülmek istemek olduğu da (Zemahşerî, Râzî). Suhâ yıldızını beşinci ayetin tefsiri olarak kullanan ya da yetim, sehv ve riya arasında bir bakış-tersine çevirme ağı kuran bir tefsir kontrol edilen sayfalarda bulunmadı. Bağ proje sentezidir ve ayetin bağlamsal anlamı yerine geçmez.",
    source="MAQ-SAHW|BASE-LEX|KASH-107|RAZI-107")

add(39, id="S107-XQ-003", type="cross_quran", tradition="rivayet", ayah="107:5", role="corroboration",
    relation="lexical", status="explicit", connection="strong", confidence="medium", priority="extended", audience="advanced",
    scholar="Tabari",
    prose="Zâriyât 51:11’deki “ellezîne hum fî ġamratin sâhûn” kalıbı baz metinde 107:5 ile paralel okunur. Taberî bu ayeti “sapıklığın dalgası içinde, Hak’tan sâhûn; ondan lehv ile yüz çevirmiş” diye açıklar ve İbn Abbas’tan “gafletle lâhûn”, İbn Zeyd’den “kendilerine gelene ve indirilene ve emredilene sâhûn” aktarır. Böylece “sâhûn”un Kur’an kullanımında da gaflet/ihmal anlamı taşıdığı Taberî’de açıkça vardır. Taberî bu ayeti 107:5 ile açıkça ilişkilendirmez; ilişki yapıtaşıdır.",
    source="TAB-51-11")

# ------------------------------------------------------------ SECTION 4
add(45, id="S107-HIS-002", type="historical_context", tradition="historical", ayah="107:2", role="historical_context",
    relation="historical", status="inferred", confidence="low", priority="extended", audience="advanced",
    scholar="al-Qurtubi",
    prose="Kurtubî 107:2’de yetime yapılan itme olgusunu, Nisâ sûresinde anlatılan bir uygulamayla ilişkilendirir: mızrakla vurup kılıçla savaşan mala sahip olur diyerek kadınlara ve küçüklere miras vermeyen çevre. Ayrıca “Müslümanlardan bir yetimi geçimine yetene kadar yanına katanın cenneti vacip olur” sözünü Peygamber’e nispetle aktarır (isnâd ve derece bu çalışmada incelenmedi). Bu bağ, “yedu‘‘u’l-yetîm”in yalnız kaba muamele değil, hak ve mal bağlamı da taşıdığına dair en erken okumayı (İbn Abbas: “yetimin hakkını iter”) tarihsel olarak anlaşılır kılar. Çıkarım niteliğindedir; Kurtubî bu bağı dolaylı kurar, Nisâ’daki açıklamaya gönderme yapar ve olayın ayrıntısını burada vermez.",
    source="QURT-107|TAB-107")

add(45, id="S107-SEM-003", type="semantic_history", tradition="rivayet", ayah="107:2", role="semantic_range",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    term="yedu‘‘u", scholar="Tabari|Ibn Abbas|Mujahid|Qatada|Dahhak|Zamakhshari|Razi|Qurtubi|Ibn Kathir",
    prose="“Yedu‘‘u’l-yetîm” için erken ve geç kaynaklar dört dal verir ve “itmek” bunların yalnızca birine denk gelir. (1) Hakkından ve malından itmek: İbn Abbas “yetimin hakkını iter” (Taberî), Taberî’nin kendi şerhi “yetimi hakkından iter ve ona zulmeder” ve “da‘a’tü fülânen an hakkıhî” örneği; İbn Abbas’ın Nâfi‘ b. Ezrak’a cevabı “hakkından iter” ve Ebû Tâlib beyti (Süyûtî, Tustî yoluyla). (2) Yedirmemek: Mücâhid “yetimi iter ve ona yedirmez” (Taberî). (3) Ezmek ve zulmetmek: Katâde ve Dahhâk “yakhar(uh) ve yazlimuh”, İbn Kesîr de “yetimi ezer, hakkını yer, ona yedirmez, iyilik yapmaz” der. (4) Sert ve kaba itiş: Zemahşerî “şiddetli, cefâ ve eziyetle itmek, azarla ve kabalıkla geri çevirmek”; Maqâyîs dec’i “ed-def‘” diye tanımlar ve 52:13’ü gösterir. Râzî bunları üç katmanda toplar: hakkından ve malından zulümle itmek; ikram etmeyi bırakmak (vacip olmasa bile); azarlamak, vurmak, küçümsemek. Kurtubî “mânâ birbirine yakındır” der. Dolayısıyla “itip kakmak” deyimi fiziksel-davranışsal dalı verirken “hak ve mal” dalı ayrı bir erken yorum olarak durur.",
    source="TAB-107|SUY-107|KASH-107|RAZI-107|QURT-107|KATH-107|MAQ-DAA")

add(45, id="S107-TAF-007", type="tafsir", tradition="dirayet", ayah="107:2", role="interpretive_consequence",
    relation="grammatical", status="explicit", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Razi", term="yedu‘‘u (teşdîd)",
    prose="Râzî fiildeki teşdîdin (“yedu‘‘u”) alışkanlığı gösterdiğini belirtir: tek seferlik bir itiş değil, âdet hâline gelmiş bir tutum. Bu yüzden pişman olan kişi tehdidin kapsamına girmez; kıyasla “ellâ’l-lemem” (53:32) verilir, bir mümin günah işleyince hemen pişman olur, ısrar edense yalanlayandır. Bu, Türkçeye anlık bir eylemi anlatan biçimde (“itiverir”) aktarmanın, ayetin sürekliliğini kaybettireceği anlamına gelir.",
    source="RAZI-107")

add(45, id="S107-QIR-003", type="qiraat", tradition="rivayet", ayah="107:2", role="semantic_range",
    relation="grammatical", status="reported", priority="research", audience="research",
    note="Attribution of reader not given in the sources read; canonical status not assessed",
    prose="İkinci ayette “yedu‘‘u” yerine “yeda‘u” (terk eder, uzak tutar) okuyuşu kaydedilmiştir (Zemahşerî, Beyzâvî, Râzî: “yani yetimi bırakır, cefa eder”). Râzî ayrıca “yed‘û” (yetimi çağırır) okuyuşunu da anar: gösteriş için yemeğe çağırıp sonra yedirmeyen, ancak hizmet, zorlama ya da üstünlük taslamak için çağıran. Bu okuyuşların okuyucu nispeti okunan sayfalarda verilmemiştir; kanonik durumu değerlendirilmemiştir. Anlam olarak “itmek” değil, “bırakmak/ilgilenmemek” koluna ya da onun tersine yol açar.",
    source="KASH-107|BAYD-107|RAZI-107")

add(45, id="S107-MEAL-005", type="semantic_history", tradition="historical", ayah="107:2", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="yedu‘‘u’l-yetîm", scope="meal-review:yedu‘‘u", scholar="Diyanet|Okuyan|Öztürk|Hayrat|Ateş|Elmalılı|Bilmen|Gölpınarlı|Süleymaniye Vakfı|Yüksel (dolaylı)",
    prose="Meal incelemesi: “yedu‘‘u’l-yetîm”. Taranan meallerin hemen hepsi “itip kakar/itip kakandır” der (Diyanet, Okuyan, Öztürk, Hayrat, Süleymaniye Vakfı, Bulaç); Ateş “iter, kakar”, Elmalılı özgün “iter yetîmi”. “İtip kakmak” Türkçede kabaca ve küçümseyerek davranmak demektir; Zemahşerî’nin “itmek ve kabalıkla geri çevirmek” ve Katâde’nin “ezmek” yorumlarıyla örtüşür. Dolayısıyla ortak seçim savunulabilirdir. Ancak İbn Abbas’ın, Taberî’nin kendi şerhinin ve Râzî’nin ilk sırada gösterdiği “yetimi hakkından ve malından iter” dalı hiçbir taranan mealde görünmez. Eski Diyanet metni “öksüzü kakıştıran” ile aynı alanda kalıyordu. Gölpınarlı “horlar” der ve Katâde’nin “ezer/aşağılar” koluna kayar. Bilmen “itiverir” der; bu anlık ve tek sefer bir eylem anlamı verir ve Râzî’nin teşdîd/alışkanlık vurgusunu kaybeder (S107-TAF-007). Yüksel’in “öksüze kötü davranan” biçimi (yalnızca dolaylı kaynakla, düşük güven) genelleştirir ve “itme” hareketini siler. Hiçbiri hata değildir; hak ve mal koluna bir dipnot düşülmesi yararlı olurdu.",
    source="MEAL-DIY-107|MEAL-DIYOLD-107|MEAL-OKU-107|MEAL-YNO-107|MEAL-HAY-107|MEAL-ATE-107|MEAL-ELM-107|MEAL-BIL-107|MEAL-GOL-107|MEAL-SUL-107|MEAL-YUK-107|TAB-107|SUY-107|KASH-107|RAZI-107")

add(45, id="S107-MET-004", type="method_note", tradition="project", ayah="107:2", role="constraint",
    relation="lexical", status="explicit", confidence="high", priority="research", audience="advanced",
    prose="Kaynak notu: Baz metin “da‘ da‘” (sürçene “kalk”) ve koyun sürme sesini kök ailesi çağrışımı olarak anar. Maqâyîs aynı maddede bu sesleri asıl saymaz: “seslerin ve onların hikâyelerinin kıyas edilmesi pek mümkün değildir, bunlar asıllar değildir” der ve kökün kıyasî çekirdeğini hareket, itme ve çalkalanma olarak verir (ed-dec ‘itmek’, 52:13; ed-de‘de‘a ‘ölçeği sarsmak’). Bu yüzden “kaldıran çağrı” yalnızca ses çağrışımıdır; baz metin onu ayetin anlamının “yanında duyulur” diye zaten sınırlar, ama okur bunun kökün asli anlamı olmadığını bilmelidir. Baz metin değiştirilmemiştir.",
    source="MAQ-DAA|BASE-LEX")

add(45, id="S107-REJ-003", type="method_note", tradition="project", ayah="107:2", role="rejected_candidate",
    relation="lexical", status="interpretive", connection="rejected", priority="research", audience="research",
    reason="Maqâyîs sesli çağrıları asıl saymaz; klasik şerhlerin hepsi dec’i ‘itmek’ diye açıklar.",
    prose="Aday: “yedu‘‘u’l-yetîm”i, kökün “da‘ da‘” (kalk) çağrısı üzerinden “yetimi kaldırır/çağırır” diye okumak. İncelendi ve reddedildi: erken ve geç hiçbir şerh bu anlamı vermez, Maqâyîs bu sesleri asıl saymaz (S107-MET-004). Râzî’nin aktardığı “yed‘û” okuyuşu (yetimi çağırır) ters bir anlamdır ve “kaldırmak” değil, gösteriş ya da hizmet için çağırıp yedirmemektir.",
    source="MAQ-DAA|RAZI-107")

add(47, id="S107-SEM-004", type="semantic_history", tradition="dirayet", ayah="107:3", role="semantic_range",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    term="lâ yehuddu alâ ta‘âmi’l-miskîn", scholar="Tabari|Zamakhshari|Baydawi|Razi|Biqai|Qurtubi|Ibn Kathir",
    prose="“Lâ yehuddu” için klasik aralık şunu kapsar: kimi şerh başkasını, kimi kendisini de içerir. Taberî “başkasını muhtaca yemek yedirmeye teşvik etmez”, Zemahşerî “ehlini harekete geçirmez”, Beyzâvî “ehlini ve başkalarını” der. Râzî iki vecih verir: kendisini teşvik etmez (yemeği “miskinin yemeği” diye ona izâfe etmek, o yemeğin miskinin hakkı olduğunu gösterir; yani hakkı olan şeyi esirgemiştir) ya da başkasını teşvik etmez, çünkü onda sevap görmez. Bikâî “kendisini, ehlini ve başkalarını büyük bir teşvikle harekete geçirmez, hatta miskinden nefret eder” der. Kurtubî hükmün genel olmadığını, gücü yetmediği için yapamayanı kapsamadığını, ayetin cimrilik edip mazeret bulanlar (“Allah dileseydi doyururdu” diyenler) hakkında olduğunu söyler. İbn Kesîr miskini “hiçbir şeyi olmayan fakir” diye açıklar. Dolayısıyla klasik okuma “başkasını teşvik” ve “kendisi de yapmama” kollarını birlikte taşır; teşvik edilen şey yemek yedirmedir ve ayet gücü olmayanı hedeflemez.",
    source="TAB-107|KASH-107|BAYD-107|RAZI-107|BIQ-107|QURT-107|KATH-107")

add(47, id="S107-TAF-008", type="tafsir", tradition="nazm", ayah="107:3", role="clarification",
    relation="grammatical", status="explicit", confidence="medium", priority="research", audience="research",
    scholar="al-Biqai|al-Razi", term="ta‘âm",
    prose="Bikâî üçüncü ayette bir ihtibâk (karşılıklı hazif) görür: ilk ayetteki “dec” (itmek), ikincide “maktı” (nefret etmek) anlamını; ikincideki “hadd” (teşvik), birincide benzerini gösterir. Üçüncü ayetteki “ta‘âm” (yemek) sözcüğünün “it‘âm” yerine seçilmesini ve “miskin”e izâfe edilmesini zenginin malında miskinin Allah’ın taktir ettiği ölçüde ortaklığına işaret saymasını da kaydeder; Râzî de izâfenin yemeğin miskinin hakkı olduğunu gösterdiğini söyler.",
    source="BIQ-107|RAZI-107")

add(47, id="S107-MET-005", type="method_note", tradition="project", ayah="107:3", role="constraint",
    relation="lexical", status="explicit", confidence="high", priority="research", audience="advanced",
    prose="Kaynak notu: Baz metin “hadd”i (teşvik) ve “hadîd”i (dağ eteğinde yerin en dip noktası) aynı kök diye bir araya getirir. Maqâyîs bu maddeyi “iki asıl” olarak verir: birincisi bir şeye sevk ve teşvik (el-ba‘s alâ’ş-şey’), ikincisi alçak zemin (el-hadîd). Yani lugat bunları aynı harflerle yazılan iki ayrı asıl sayar; “teşvik, en dipte yatana doğru yapılan bir itiştir” çağrışımı bu yüzden harf birliğinden doğan bir rezonanstır, anlam birliği değildir. Maqâyîs’in aktardığı Halîl ayrımı da şunu söyler: “hass” (حث) yürüyüşte, sürmede ve her şeyde kullanılabilir, “hadd” (حض) ise yürüyüşte ve sürmede kullanılmaz. Bu, baz metindeki “sürmek” glossunun Türkçe bir çağrışım olduğunu, kökün teşvike özgü olduğunu gösterir. Baz metin değiştirilmemiştir.",
    source="MAQ-HDD|BASE-LEX")

add(47, id="S107-MEAL-006", type="semantic_history", tradition="historical", ayah="107:3", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="lâ yehuddu alâ ta‘âmi’l-miskîn", scope="meal-review:yehuddu", scholar="Diyanet|Okuyan|Öztürk|Hayrat|Bilmen|Ateş|Gölpınarlı|Elmalılı|Süleymaniye Vakfı|İslamoğlu|Esed",
    prose="Meal incelemesi: “lâ yehuddu”. (1) “Özendirmez/teşvik etmez”: güncel Diyanet (“yoksula yedirmeyi özendirmeyen kimsedir”), Okuyan, Hayrat, Öztürk, Bulaç, Bilmen (“teşvikte bulunmaz”). Bu seçim başkasını teşviki verir; Taberî ve Zemahşerî’nin ilk okumasıyla desteklenir, savunulabilir bir daraltmadır, ama Râzî ve Bikâî’nin “kendisi de” kolu görünmez. (2) “Önayak olmaz”: Ateş ve Elmalılı’nın sadeleştirilmiş metni (kuranmeali.com etiketiyle). “Önayak olmak” hem kişinin kendi girişimini hem başkasını harekete geçirmeyi taşıyabilen bir Türkçe deyimdir; Râzî’nin iki veciheyle ve Bikâî’nin “kendisini, ehlini, başkasını” okumasıyla en iyi örtüşen karşılık budur. (3) Gölpınarlı “doyurmaz da, önayak olmaz da doyurmaya yoksulu” der: iki kolu ayrı ayrı yazar; Râzî’nin birinci vechini ve Bikâî’yi açıkça yansıtır. (4) “Gayret etmeyen/arzusu duymayan”: İslamoğlu ve Esed nefse dönük kolu seçer ve başkasını teşvik dalını silikleştirir. (5) Elmalılı’nın özgün metni “kayırmaz doyurmak üzere miskini” der; “kayırmak” hadd’in “teşvik” anlamını gözetme/sahip çıkma tonuna kaydırır; bu kol kontrol edilen klasik şerhlerde görülmedi, ama hata değil yorum rengidir (düşük güven). (6) Süleymaniye Vakfı’nın “çaresizlerin yiyeceği için teşvikte bile bulunmayan” ifadesi Râzî’nin ve Bikâî’nin vurguladığı “miskinin yemeği” izâfesini korur. “Yoksul” karşılığı da İbn Kesîr’in “miskin = hiçbir şeyi olmayan fakir” tanımıyla çelişmez. Hiçbir meal Kurtubî’nin “gücü yetmeyeni kapsamaz” sınırını göstermez.",
    source="MEAL-DIY-107|MEAL-OKU-107|MEAL-HAY-107|MEAL-YNO-107|MEAL-BUL-107|MEAL-BIL-107|MEAL-ATE-107|MEAL-GOL-107|MEAL-ELM-107|MEAL-SUL-107|MEAL-ISL-107|MEAL-ESED-107|TAB-107|KASH-107|RAZI-107|BIQ-107|KATH-107|QURT-107")

add(53, id="S107-XQ-004", type="cross_quran", tradition="dirayet", ayah="107:2|107:3|107:7", role="corroboration",
    relation="thematic", status="explicit", connection="strong", confidence="high", priority="extended", audience="advanced",
    scholar="al-Razi", attested_in="Qurtubi",
    prose="Baz metnin Kur’an içi bağlarından birkaçı Râzî’de aynı yerde vardır. 107:2’de “yedu‘‘u”yu “yevme yuda‘‘ûne ilâ nâri cehenneme da‘‘â” (52:13) ile açıklar. 107:3’te yetimin ve yoksulun hakkı için karşıtı olarak müminlerin “tevâsav bi’l-merhame” (90:17) ve “tevâsav bi’l-hakk, tevâsav bi’s-sabr” (103:3) sıfatını anar. 107:7’de cimrilik ve teşvik tersine çevirmesi için “ellezîne yebhalûne ve ye’mürûne’n-nâse bi’l-buhl” (4:37) ve “mennâ‘in li’l-hayr mu‘tedin esîm” (68:12) ayetlerini getirir. Taranan sayfalarda 89:17-18, 93:9-10, 68:17-24 ve 90:11-16 bağları bulunmadı.",
    source="RAZI-107|QURT-107")

# ------------------------------------------------------------ SECTION 5
add(61, id="S107-SEM-005", type="semantic_history", tradition="rivayet", ayah="107:7", role="semantic_range",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    term="mâ‘ûn", scholar="Tabari|Ali|Ibn Umar|Ibn Mas'ud|Ibn Abbas|Ikrima|Muhammad b. Ka'b|Said b. al-Musayyab|Zuhri|Qurtubi|Razi|Ibn Kathir",
    attested_in="Qurtubi|Razi|Ibn Kathir|Suyuti",
    prose="“Mâ‘ûn” için aralık çok dallıdır ve erken kaynaklar bunu açıkça kaydeder. Taberî’de en çok zincir şunlar için verilir: zekât (Ali; Mücâhid ve Ebû Sâlih yoluyla; İbn Ömer; Hasan; Katâde; Saîd b. Cübeyr; İbnü’l-Hanefiyye; Dahhâk; İbn Zeyd) ve ödünç ev eşyası (İbn Mes‘ûd: balta, kazan, kova; Ebu’l-Ubeydeyn, İbrâhim et-Teymî, Ebû Vâil yoluyla; İbn Abbas: âriyet ve metâü’l-beyt; Saîd b. Cübeyr; Ebû Mâlik). Ek olarak: Muhammed b. Ka‘b “el-ma‘rûf”; Saîd b. el-Müseyyeb ve Zührî “Kureyş lisanıyla mal”; İbn Abbas’ın (Ali b. Ebî Talha yoluyla) “insanlar ihtilaf etti: kimi zekât, kimi itaat, kimi âriyet dedi”; Leys yoluyla İbn Abbas’tan “ehli henüz gelmedi”. Ali’den bir başka rivayet “zekât ile balta, kova, kazan”ı birlikte sayar. İbn Ömer, kendisine İbn Mes‘ûd’un görüşü hatırlatılınca “benim dediğim budur” diyerek “hakkı verilmeyen mal”ı kast eder (Taberî, Süyûtî). İkrime: “mâ‘ûnun başı mal zekâtı, en aşağısı elek, kova ve iğnedir” (İbn Ebî Hâtim, İbn Kesîr). Kurtubî on iki görüş, Râzî dört görüş sayar (zekât; ödünç eşya; su; itaat). Râzî ödünç eşya görüşünü “çoğu müfessirin” görüşü sayar; Taberî’de ise zincir sayısı zekât lehine daha çoktur (bu bir sayımdır, ağırlıklandırma değil). Tekrarlayan nakiller (İbn Kesîr, Kurtubî, Süyûtî) yeni ek bilgi taşımadıkları için ayrıca açılmamıştır.",
    source="TAB-107|QURT-107|RAZI-107|KATH-107|SUY-107")

add(61, id="S107-TAF-009", type="tafsir", tradition="dirayet", ayah="107:7", role="clarification",
    relation="lexical", status="explicit", confidence="high", priority="extended", audience="advanced",
    scholar="Qutrub|Jawhari|Ibn al-Arabi|Razi|Alusi", term="mâ‘ûn (türetme)",
    prose="“Mâ‘ûn”un türetmesi için klasik kaynaklar birden çok yol verir. (1) Fâûl vezninde ma‘n’dan: az ve kolay şey; Kutrub “ma‘n = az, ma‘rûf”, “mâ lehu sa‘ne ve lâ ma‘ne” (ne çok ne az şeyi yok); Râzî zekâtın da “maldan kırkta bir”, yani çoktan azın alınması dolayısıyla mâûn diye adlandırıldığını söyler. (2) Ma‘ûne’den (yardım): elif hâ yerine geçer (Cevherî’den, Kurtubî’de). (3) İbn Arabî’den: a‘âne’den mef‘ûl, yani yardım ve imdat araçları (Kurtubî). (4) Âlûsî ayrıca a‘âne’den ism-i mef‘ûl olan “me‘vûn”un harf yer değiştirmesiyle (kalb) ve vâvın elife dönüşmesiyle “mâ‘ûn”a vardığı vecihi verir. Bu çeşitlilik Türkçe karşılıklara da yansır: “yardım” sözcüğü (ma‘ûne/a‘âne) türetmesine, “ufacık/küçük” (ma‘n) türetmesine uyar; iki türetme de klasik kaynaklarda canlıdır.",
    source="QURT-107|RAZI-107|ALUSI-107")

add(61, id="S107-TAF-010", type="tafsir", tradition="rivayet", ayah="107:7", role="anchor",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    scholar="Tabari|Ibn Kathir|Razi|Biqai", attested_in="Baydawi",
    prose="Çok dallı aralığı birleştiren iki erken sentez vardır. Taberî kendi hükmünde, Allah’ın bu kişilerin insanlara karşı mâûnu esirgediklerini genel olarak bildirdiğini, bir şeyi tahsis etmediğini söyler; bu yüzden onların hem insanların birbirine ödünç verdikleri şeyleri hem de ihtiyaç sahibine mallarında Allah’ın farz kıldığı hakları esirgedikleri anlaşılmalıdır, çünkü bunların hepsi insanların birbirinden yararlandığı menfaatlerdir. İbn Kesîr İkrime’nin “mâ‘ûnun başı zekât, en aşağısı elek, kova ve iğne” sözünü “güzel” bulur: bütün görüşleri kapsar ve hepsi tek şeye, mal ya da fayda ile yardımlaşmayı terk etmeye döner. Râzî de en uygun olanın yapılması kolay her itaat olduğunu söyler. Bikâî sonuç olarak esirgenen şeyin “verilmesi gereken şey” (fazla otlak, su, zekât gibi) olarak anlaşılması gerektiğini söyler ki veyli gerektirebilsin. Beyzâvî “zekât ya da âdetçe ödünç verilen şey” der.",
    source="TAB-107|KATH-107|RAZI-107|BIQ-107|BAYD-107")

add(61, id="S107-HIS-001", type="historical_context", tradition="historical", ayah="107:7", role="historical_context",
    relation="historical", status="explicit", confidence="medium", priority="core", audience="general",
    scholar="Tabari|Ibn Kathir|Razi|Zamakhshari|Qurtubi",
    prose="Ödünç verilen eşya erken kaynaklarda somut olarak sayılır ve gündelik bir komşuluk uygulamasını gösterir. İbn Mes‘ûd: “Biz Peygamber’in zamanında mâûnu kova ve kazan ödünç vermek sayardık” (İbn Kesîr’e göre Ebû Dâvûd ve Nesâî rivayeti; Süyûtî Ebû Dâvûd, Nesâî, Bezzâr, Beyhakî gibi başka derleyicileri de sayar); aynı İbn Mes‘ûd’dan balta, kazan, kova ve terazi (mîzân). Başka bir rivayette İbn Mes‘ûd “mâûndan balta, kazan ve kova esirgemek; bu üçünden iki huy” der ve Şu‘be “baltada şüphe yoktur” ekler (Taberî). Zemahşerî ve Râzî kıvılcım çakmağı (mikdaha), kalbur ve keser (kadûm) gibi aletleri ekler; Râzî komşunun ekmeğini sizin tandırınızda pişirmek istemesini ya da eşyasını bir gün bırakmasını örnek verir. İbn Kesîr âriyetin “şeyin kendisinin kalıp sonra sahibine dönmesi” olduğunu belirtir (aynı eşya döner). Zemahşerî ve Kurtubî bunun hükmünü şöyle ayırır: zorunluluk (iztırar) hâlinde esirgemek yasak, zorunluluk dışında mürüvvette çirkin olabilir.",
    source="TAB-107|KATH-107|SUY-107|RAZI-107|KASH-107|QURT-107")

add(61, id="S107-HAD-007", type="hadith", tradition="hadith", ayah="107:7", role="source_criticism",
    relation="thematic", status="reported", hadith_grade="not_assessed", connection="speculative", priority="research", audience="research",
    transmitter="Ubayy b. Ka'b (as cited by Razi)", origin="Zamakhshari/Baydawi closing; Razi under 107:7",
    prose="Zemahşerî ve Beyzâvî sûre sonunda “kim Erâeyte sûresini okursa, zekât veren biriyse Allah onu bağışlar” sözünü Peygamber’e bağlayarak anar; Râzî bunu Übey hadisi diye anar ve “mâ‘ûn zekâttır” anlayışına işaret ettiğini söyler. Senedi okunan sayfalarda verilmemiştir ve bu çalışmada incelenmemiştir; bu nedenle hadis olarak derece verilmedi ve “mâ‘ûn = zekât” için kanıt olarak kullanılmadı. Sûre faziletleriyle ilgili bu söz ancak tefsir geleneğinin zekât okumasına nasıl yaslandığını gösteren bir veri olarak kaydedilir.",
    source="KASH-107|BAYD-107|RAZI-107")

add(61, id="S107-MEAL-007", type="semantic_history", tradition="historical", ayah="107:7", role="disagreement",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="mâ‘ûn", scope="meal-review:mâ‘ûn", scholar="Diyanet|Hayrat|Çantay|Gölpınarlı|Okuyan|Ateş|İslamoğlu|Süleymaniye Vakfı|Öztürk|Bulaç|Elmalılı|İzmirli|Bilmen|Diyanet Vakfı|İbni Kesir (etiket)",
    prose="Meal incelemesi: “mâ‘ûn”. Klasik aralık zekâtı, ödünç ev eşyasını, ma‘rûfu, malı, suyu ve itaati kapsar (S107-SEM-005); Taberî ve İbn Kesîr bunları tek bir yapıda toplar (S107-TAF-010). Meallerin dağılımı: (1) Yalnız zekât: Hayrat (“mâûn’u (zekâtı) men‘ ederler”), Çantay (“Zekâtı da men‘ederler”), Gölpınarlı (“zekât vermeyi menederler”) ve acikkuran.com’da “İbni Kesir” etiketi taşıyan metin. Bu dal Ali, İbn Ömer, Hasan, Katâde ve pek çok erken zincirle güçlü desteklenir; fakat Taberî, İbn Kesîr ve Râzî aralığı tek dala indirmez; bu nedenle desteklenmiş ama daraltıcı bir seçimdir, hata değildir. “İbni Kesir” etiketli metnin zekâta indirgemesi, İbn Kesîr’in kendi tercihi olan İkrime’nin kapsayıcı sözüyle uyuşmaz; etiketin hangi çeviriye ait olduğu doğrulanmadı. (2) Küçük yardım/küçük şey: güncel Diyanet (“Ufacık bir yardıma bile engel olurlar”), Ateş (“En ufak bir yardımı esirgerler”), Okuyan (“(En ufak) yardıma (bile) engel olurlar”), İslamoğlu, Süleymaniye Vakfı. Bu, ma‘n (az ve kolay şey; Kutrub, Râzî) türetmesine ve İkrime’nin “en aşağısı” ucuna dayanır; zekât ve ödünç eşya gibi somut kolları gizler. “Yardım” sözcüğü ma‘ûne/a‘âne türetmesine de uyar (S107-TAF-009). Eski Diyanet metni “basit şeyleri dahi vermezler” demişti. (3) Aralığı açık tutanlar: Öztürk (“kamu hakkına/yardıma/zekâta/iyiliğe”), Bulaç (“ufacık bir yardımı (veya zekâtı)”), Elmalılı özgün (“yardımlığı sakınır (zekâtı vermezler)”), İzmirli (“Zekât ve âriyet”). Klasik aralığa en yakın olanlar bunlardır; Öztürk’ün “kamu hakkı”nı İbn Ömer’in “hakkı esirgemek” sözünün modern karşılığı olarak okumak mümkündür (çıkarım). (4) Bilmen “men edilmesi mutad olmayan bir şeyi bile” der: Râzî’nin “âdette esirgenmeyen şey” tanımını taşıyan tek meal. (5) Diyanet Vakfı “hayra da mâni olurlar” der; Muhammed b. Ka‘b’ın “ma‘rûf” görüşüne uyan en genel seçimdir ama somut içeriği (alet, zekât, su) siler. (6) Hiçbir meal suyu, ateşi ya da tuzu öne çıkarmaz (Âişe, Kurtubî; S107-HAD-005). Fiil için “engel olurlar” (Diyanet, Okuyan, Öztürk) “araya girmek” imgesini, “esirgerler” (Ateş, İslamoğlu) vermenin karşıtını korur; ikisi de savunulabilir.",
    source="MEAL-DIY-107|MEAL-DIYOLD-107|MEAL-HAY-107|MEAL-CAN-107|MEAL-GOL-107|MEAL-IKT-107|MEAL-OKU-107|MEAL-ATE-107|MEAL-ISL-107|MEAL-SUL-107|MEAL-YNO-107|MEAL-BUL-107|MEAL-ELM-107|MEAL-IZM-107|MEAL-BIL-107|MEAL-DVK-107|TAB-107|KATH-107|RAZI-107|QURT-107")

add(65, id="S107-NOV-006", type="novelty", tradition="project", ayah="107:2|107:3|107:5|107:7", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="building_blocks_only",
    checked_sources=CHK + "|Maqayis(yatm,sahw,dae,hadd,man)",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “evin içi” ağı için denetim. Eski ve açık olan kısım: mâûnun ev eşyası (kova, kazan, balta, terazi, elek, iğne) olması ve komşuluk ödüncü (Taberî, İbn Kesîr, Zemahşerî, Râzî, Kurtubî). Bulunmayan kısım: dec’in küçük çocuklar (di‘â‘) ve sarsılarak doldurulan ölçekle (de‘de‘a) aynı kökte bulunması, miskin kökünün ev ve ev halkı (seken) ile, sehv kökünün evin önündeki raf (sehve) ile ayrı ayrı anılması ve bunların tek bir ev sahnesinde birleştirilmesi. Bu birleştirme proje sentezidir; yapıtaşlarının bir kısmı lugatta ayrı ayrı vardır, tefsirlerde yoktur.",
    source="TAB-107|KATH-107|KASH-107|RAZI-107|QURT-107|BASE-LEX")

add(67, id="S107-XQ-005", type="cross_quran", tradition="dirayet", ayah="107:3", role="corroboration",
    relation="thematic", status="explicit", connection="strong", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Qurtubi",
    prose="Baz metindeki Yâsîn 36:47 bağı (“Allah dileseydi doyuracağı kimseyi biz mi doyuracağız”) Kurtubî’de üçüncü ayetin tefsirinde açıkça geçer: ona göre ayet gücü yetmeyeni değil, cimrilik edip bu sözle mazeret bulanları hedefler. Baz metindeki öbür bağlar (76:8, 18:77-82, 12:63, 83:1-3, 4:8) taranan sayfalarda bulunmadı.",
    source="QURT-107")

# ------------------------------------------------------------ SECTION 6
add(73, id="S107-SEM-006", type="semantic_history", tradition="rivayet", ayah="107:7", role="semantic_range",
    relation="lexical", status="explicit", confidence="high", priority="core", audience="general",
    term="mâ‘ûn = su", scholar="Tabari|Fara|Razi|Qurtubi|Zamakhshari",
    prose="“Mâûn = su” kolu klasik kaynaklarda açıkça vardır. Taberî “mâûnun aslı her şeyin menfaatidir; bulutlardan inen suya mâûn denir” der ve Ea‘şâ’dan (“bi-ecvedi minhu bi-mâ‘ûnihî izâ mâ semâühüm lem teġim”) ile başka bir beyitten (“yemucc u sabîruhu’l-mâ‘ûne sabbâ”) delil getirir. Râzî ve Kurtubî bunu Ferrâ’nın bir Araptan duyduğu “el-mâ‘ûn: el-mâ” sözüne bağlar; Kurtubî suyu “su ve otlak” (yedinci görüş) ve “yalnız su” (sekizinci görüş) olarak ayrı sayar. Râzî bu seçimin gerekçesini şöyle verir: su “bulunmayanların en kıymetlisi, bulunanların en ucuzu”dur; cehennem ehlinin ilk istediği ve cennet ehlinin ilk tattığı şeydir. Zemahşerî ve Kurtubî Âişe’den “su, ateş, tuz” rivayetini verir (S107-HAD-005). Bu, baz metindeki “suya da mâûn denir” cümlesinin doğrudan klasik dayanağıdır.",
    source="TAB-107|RAZI-107|QURT-107|KASH-107")

add(73, id="S107-HAD-004", type="hadith", tradition="hadith", ayah="107:7", role="corroboration",
    relation="direct_hadith_tafsir", status="weak", hadith_grade="daif", connection="strong", confidence="medium",
    priority="extended", audience="advanced", transmitter="Qurra b. Dimus al-Numayri; Ali via Ibn Qani'; al-Harith b. Shurayh",
    origin="Ibn Abi Hatim and Ibn Mardawayh via Ibn Kathir and Suyuti",
    note="Grade reflects Ibn Kathir's criticism of the Qurra report; the variants in Suyuti were not graded here except Umm Atiyya (Suyuti: weak chain)",
    prose="Kurre b. Dı‘mûs en-Numeyrî’den: bir heyetin “bize ne tavsiye edersin” sorusuna Peygamber’in “mâûnu esirgemeyin” dediği, “mâûn nedir” sorusuna “taşta, demirde, suda” diye cevap verdiği, demirin kazan ve baltanın demiri, taşın taş kazan olduğunun açıklandığı rivayet edilir (İbn Ebî Hâtim, İbn Merdeveyh). İbn Kesîr bunu “çok garîb, merfû‘ olması münker, isnâdında tanınmayan var” diye değerlendirir. Süyûtî buna yakın rivayetleri de verir: Ali’den (İbn Kâni‘ yoluyla) ve el-Hâris b. Şüreyh’ten (Bâverdî) “taş, demir, su”; Ümmü Atıyye’den Taberânî’nin “zayıf bir senetle” aktardığı “mâûn insanların birbirine verdiğidir” sözü. Bunlar mâûnun suyu da kapsadığını doğrudan Peygamber tefsiri olarak gösterir ama zayıftır; su kolunun asıl dayanağı lugat (Taberî, Ferrâ) ve Âişe rivayetidir.",
    source="KATH-107|SUY-107")

add(73, id="S107-HAD-005", type="hadith", tradition="hadith", ayah="107:7", role="corroboration",
    relation="thematic", status="reported", hadith_grade="not_assessed", connection="strong", confidence="medium",
    priority="extended", audience="general", transmitter="A'isha", origin="Tha'labi tafsir; Ibn Majah per Qurtubi; Zamakhshari attributes the same triad to A'isha",
    note="Qurtubi: isnad has softness (layyin); no independent grading here",
    prose="Zemahşerî mâûnu Âişe’den “su, ateş ve tuz” diye aktarır. Kurtubî hadisi daha açık verir: Âişe “menedilmesi helâl olmayan şey nedir?” diye sorar; Peygamber “su, ateş ve tuz” der; ateş ve tuz için, kim ateş verirse onunla pişirilen her şeyi tasadduk etmiş, kim tuz verirse onunla lezzetlenen her şeyi tasadduk etmiş gibi olur, kim su bulunan yerde bir yudum su verirse köle azat etmiş gibi, su bulunmayan yerde verirse bir cana hayat vermiş gibi olur (Kurtubî bunu Sa‘lebî’nin tefsirine ve İbn Mâce’nin Sünen’ine bağlar ve “isnâdında lîn var” der). Hadis ayeti doğrudan tefsir etmez, mâûn konusuna tematik bir paraleldir; Kurtubî onu on ikinci görüş olarak mâûn tefsirine yerleştirir. İsnâd bu çalışmada incelenmemiştir.",
    source="KASH-107|QURT-107")

add(73, id="S107-NOV-007", type="novelty", tradition="project", ayah="107:7", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="partial",
    checked_sources=CHK + "|QurtubiSura67",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “akan su” ağı için denetim. Açıkça eski olan kısım: mâûnun su anlamı (Taberî, Ferrâ, Râzî, Kurtubî, Zemahşerî; S107-SEM-006) ve su, ateş, tuzun esirgenmemesi gerektiği. Bulunmayan kısım: ma‘în, mu‘nân ve mem‘ûn sözcüklerinin vadi yatağı ve ot sahnesiyle kurulan bütün imgesi; yedinci ayetin son kelimesiyle Mülk 67:30’un “mâin ma‘în”i arasındaki bağ ve miskin kökündeki “mer‘an müskin” çağrışımı. Kurtubî Mülk 67:30’u ayrı bir yerde “ma‘în = akan” diye açıklar (S107-XQ-006), ancak 107:7 ile ilişkilendirmez. Dolayısıyla su anlamı klasiktir; imge ağı ve Mülk bağı proje sentezidir.",
    source="TAB-107|RAZI-107|QURT-107|QURT-67-30|BASE-LEX")

add(77, id="S107-XQ-006", type="cross_quran", tradition="dirayet", ayah="107:7", role="clarification",
    relation="lexical", status="explicit", connection="strong", confidence="medium", priority="research", audience="advanced",
    scholar="al-Qurtubi",
    prose="Mülk 67:30’daki “mâin ma‘în” için Kurtubî şunları kaydeder: “ma‘în”, Katâde ve Dahhâk’a göre “câr” (akan); İbn Abbas’a göre gözlerin gördüğü açık su; bir başka açıklamada “ma‘ne’l-mâ’ = suyun çoğalması” (fe‘îl vezninde); İbn Abbas’tan “tatlı su”. Baz metindeki “ma‘în = akan su” eşitlemesi bu nedenle bir klasik açıklama (Katâde, Dahhâk) olarak mevcuttur. Kurtubî’nin 67:30 şerhinde 107:7’ye gönderme yoktur; iki ayetin ilişkisi klasik kaynakta bulunmadı.",
    source="QURT-67-30")

# ------------------------------------------------------------ SECTION 7
add(85, id="S107-SEM-007", type="semantic_history", tradition="dirayet", ayah="107:4", role="semantic_range",
    relation="lexical", status="explicit", confidence="high", priority="core", audience="general",
    term="veyl", scholar="Tabari|Razi|Qurtubi|Biqai|Zamakhshari|Baydawi",
    prose="“Veyl” klasik kaynaklarda şöyle açıklanır. Taberî “Cehennem ehlinin irininden akan vadi, namaz kılıp da Allah’ı kast etmeyen münafıklar için” der. Kurtubî “azap” der. Râzî bu sözcüğün ancak ağır suç için kullanıldığını söyler ve “veylün li’l-mutaffifîn” (83:1), “fe-veylün lehüm mimmâ ketebet eydîhim” ve “veylün li-külli humezetin lumeze” örneklerini verir; ayrıca herkesin ateşte suçuna göre ağıt yakacağı rivayetini aktarır (kimi “şeref sevgisinden veylim”, kimi “cahiliye hamiyetinden”, kimi “namazımdan veylim” der). Bikâî veylin hakaretin en büyüğünü gösteren söz olduğunu söyler. Zemahşerî ve Beyzâvî fâyı “cezâiyye/sebebiyye” sayar ve “el-musallîn”in zamirin yerine konulduğunu belirtir. Dolayısıyla “veyl” bir kınama değil, azap/yıkım anlamlı bir tehdit sözüdür.",
    source="TAB-107|QURT-107|RAZI-107|BIQ-107|KASH-107|BAYD-107")

add(85, id="S107-TAF-011", type="tafsir", tradition="rivayet", ayah="107:4", role="disagreement",
    relation="direct_tafsir", status="explicit", confidence="medium", priority="core", audience="advanced",
    scholar="Tabari|Ibn Abbas|Ibn Kathir|Razi|Zamakhshari|Alusi|Biqai",
    prose="“El-musallîn” kimdir? Taberî ve İbn Abbas’ın aktardığı erken görüş: münafıklar (İbn Abbas, Mücâhid, Dahhâk; Mâlik de Âlûsî’de). İbn Kesîr “namaz ehli olup ona bağlandıklarını söyleyen, sonra sehv edenler” der. Râzî’nin güvendiği cevap münafıklardır ve ayetten kâfirin ibadet farzlarından da sorumlu tutulduğuna delil çıkarır (Şâfiî görüşü); aynı kaynağın öbür cevapları ise mümini dışlamaz. Zemahşerî “el-musallîn”in birden fazla anlamda cins olduğunu ve zamirin yerine konulduğunu, tanım sıfatının cümleyi genelleştirdiğini söyler; “ya da fâsıklar” ihtimalini de bırakır. Âlûsî’de Ebû Hayyân “namazla yükümlü olan herkes, kâfir de olsa” okumasını ekler. Bikâî sıfat kullanımının hükmü genelleştirdiğini ve namazla aldanmaya karşı uyarı olduğunu söyler. Dolayısıyla kimlik tek değildir: münafık (en erken ve en güçlü), namaz ehli tüm mükellefler (Ebû Hayyân, Bikâî) ve fâsık Müslümanlar (Zemahşerî).",
    source="TAB-107|KATH-107|RAZI-107|KASH-107|ALUSI-107|BIQ-107")

add(85, id="S107-NAZ-002", type="nazm", tradition="nazm", ayah="107:3|107:4", role="nazm",
    relation="structural", status="explicit", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Razi|al-Zamakhshari|al-Baydawi|al-Alusi|al-Biqai",
    prose="Dördüncü ayetin üçüncü ayetle bağlantısı için klasik şerhler birden çok açıklama sunar. Râzî’nin üç vechi: (1) yetimi incitmek ve yoksulu teşvik etmemek nifakın göstergesiyse, namazdaki huşusuzluk daha da güçlü bir göstergedir, çünkü ilki mahlûkla, ikincisi Hâlık’la muameledir; (2) “namaz fuhşiyattan ve münkerden alıkoymaz mı?” (29:45) itirazına, riya ve sehivden yapılmış namazın alıkoyamayacağı cevabı; (3) birinde yaratıklara şefkat, ötekinde Allah’a tazim eksikliği vardır ve ikisi birleşince şekavet tamamlanır. Zemahşerî ve Beyzâvî “fe”yi cezâiyye sayar: yetime aldırmamak imanın zayıflığındansa, dinin direği namazdan sehv, şirkin bir kolu riya ve İslâm’ın köprüsü zekâtı esirgemek bundan daha lâyıktır. Bikâî “halkla ilişkiden sonra Hâlık’la ilişkiye geçildi” der. Âlûsî’de bu geçişin “terakkî” (yükselen aşama) ya da “istitrâd” olduğu tartışılır. Baz metnin “namaza gelir” sıralaması bu klasik geçiş çizgisiyle uyumludur.",
    source="RAZI-107|KASH-107|BAYD-107|ALUSI-107|BIQ-107")

add(85, id="S107-MEAL-008", type="semantic_history", tradition="historical", ayah="107:4", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="fe-veylün li’l-musallîn", scope="meal-review:veyl-musallîn", scholar="Diyanet|Okuyan|Esed|Diyanet Vakfı|Öztürk|Ateş|Bulaç|Bilmen|Gölpınarlı|Hayrat|Elmalılı|İslamoğlu|Süleymaniye Vakfı",
    prose="Meal incelemesi: veyl, fâ ve musallîn. (1) Veyl: “Vay haline” (Öztürk’ün bir varyantı, Ateş, Bulaç, Bilmen, Gölpınarlı, Hayrat) ve “veyl” (Elmalılı özgün) eskatolojik tehdidi taşır; “Yazıklar olsun” (güncel Diyanet, Okuyan, Esed, Diyanet Vakfı) ise ahlâkî kınama tonuna kayar ve Taberî’nin “Cehennem vadisi” ile Râzî’nin “ağır suç sözcüğü” çizgisindeki yıkım/tehdit anlamını yumuşatır; Türkçede “yazıklar olsun” kınama ve bedduayı birlikte taşıdığı için bu savunulabilir bir daraltmadır. Öztürk’ün kuranmeali.com’da görünen varyantı “Lanet olsun o namaz kılanlara/dua edenlere ki” veyli lanet (la‘n) olarak verir; klasik şerhlerde veyl azap ve yıkım diye açıklanır, lanet diye değil; bu varyant gerçekten o basımdaysa yanıltıcıdır (düşük–orta güven, çünkü varyantın hangi basıma ait olduğu belirlenemedi; acikkuran.com ve ayetbul.net “Vay haline” der). İslamoğlu “olmaz olsun” ve Süleymaniye Vakfı’nın bir metni “Sürekli didinip duran bazı kişilerin çekecekleri var” der (acikkuran.com bunu “Eski” diye etiketler, kuranmeali.com etiketsiz verir; güncel mi eski mi olduğu belirlenemedi); ikincisi “musallîn”i “didinip duranlar” diye çevirerek salât/namaz anlamını ortadan kaldırır ve Arapçaya aykırı olduğu için hata sayılmalıdır. (2) Fâ: Elmalılı özgün “Fakat veyl” der; “fakat” fâyı karşıtlık gibi okutur, oysa Beyzâvî ve Zemahşerî’ye göre fâ cezâiyye/sebebiyyedir (“bu durumda”, “öyleyse”). Bilmen ve Hayrat “Artık vay haline”, İslamoğlu “İşbu yüzden” ile sonuç bağını korur. (3) Musallîn: hemen tüm meal “namaz kılanlar” der. Okuyan “salât (ibadet) edenler”, İslamoğlu “ibadet edenler”, Süleymaniye Vakfı “kulluk görevlerini de yapan”; salâtı genel ibadete açmak lugat bakımından geniştir (Maqâyîs salâtı hem şer‘î namaz hem dua olarak verir), ama Taberî ve İbn Kesîr bu ayette “musallîn”i namaz kılanlar olarak açıklar. Öztürk’ün varyantındaki “namaz kılanlar/dua edenler” “dua” kolunu da ekler; bu kol kontrol edilen tefsirlerde bu ayet için görülmedi: lugatça geçerli ama tefsir geleneğince desteklenmeyen bir aralık genişlemesidir. Süleymaniye Vakfı’nın “(Müslüman görünmek için)” parantezi münafık okumasını (Taberî; İbn Abbas, Mücâhid) metne katar; erken dayanağı güçlüdür ama Zemahşerî’nin “fâsıklar” ve Ebû Hayyân’ın “mükellefler” ihtimalini dışlar; parantez içinde olduğu için daraltma okura görünür.",
    source="MEAL-DIY-107|MEAL-OKU-107|MEAL-ESED-107|MEAL-DVK-107|MEAL-YNO-107|MEAL-ATE-107|MEAL-BUL-107|MEAL-BIL-107|MEAL-GOL-107|MEAL-HAY-107|MEAL-ELM-107|MEAL-ISL-107|MEAL-SUL-107|TAB-107|RAZI-107|BAYD-107|KASH-107|KATH-107|MAQ-SAHW|ALUSI-107")

add(85, id="S107-REJ-004", type="method_note", tradition="project", ayah="107:4", role="rejected_candidate",
    relation="lexical", status="interpretive", connection="rejected", priority="research", audience="research",
    reason="Taranan tefsirlerde musallîn ateşle ilişkili bir kökten açıklanmaz; hepsi namaz kılan anlamını verir.",
    prose="Aday: “el-musallîn” sözcüğünü ateş kökünden (salâ) türeyen bir ad olarak, yani “ateşe yaslananlar” diye çevirmek ya da okumak. İncelendi ve reddedildi. Taberî ve İbn Kesîr “musallîn”i namaz kılanlar diye açıklar; Kur’an’da aynı harflerden fiil (69:31 “sallûhu”) ateş anlamındadır, ama bu, 107:4’ün anlamının yerine geçmez. Kök ailesindeki ateş çağrışımı yalnızca baz metnin işaret ettiği biçimde, anlamın “yanında duyulan” bir rezonans olarak kalır.",
    source="TAB-107|KATH-107|BASE-LEX")

add(85, id="S107-NOV-008", type="novelty", tradition="project", ayah="107:4|107:5", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="building_blocks_only",
    checked_sources=CHK,
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “ocak ve ateş” ağı için denetim. Yapıtaşları: veylin Cehennem’de bir vadi/azap olarak açıklanması (Taberî, Kurtubî) klasik olarak vardır ve ayetle ateş arasında doğrudan bir klasik bağ kurar. Ancak “musallîn”in kökünün ateş taşıdığı, yoksulun kökündeki “seken = ocak” ile birleşip “ocağın değil ateşin karşısında durmak” sahnesini kurduğu bir okuma kontrol edilen tefsirlerde bulunmadı. Bu birleşim proje sentezidir.",
    source="TAB-107|QURT-107|BASE-LEX")

add(87, id="S107-XQ-007", type="cross_quran", tradition="dirayet", ayah="107:3|107:4", role="corroboration",
    relation="thematic", status="explicit", connection="direct", confidence="high", priority="extended", audience="advanced",
    scholar="al-Qurtubi|al-Razi",
    prose="Hâkka 69:34 (“ve lâ yehuddu alâ ta‘âmi’l-miskîn”) üçüncü ayetle kelimesi kelimesine aynıdır ve Kurtubî 107:3’te bunu açıkça gösterir (“bu, Hâkka sûresindeki ayetin benzeridir”). Veyl kullanımı için Râzî Mutaffifîn 83:1’i ve iki benzer ayeti (2:79’un “fe-veylün lehüm” ibaresi ve 104:1) anar. Baz metindeki 69:25-33, 83:10-17, 92:14-16, 4:10, 50:24-25 bağları taranan 107. sûre sayfalarında bulunmadı.",
    source="QURT-107|RAZI-107")

# ------------------------------------------------------------ SECTION 8
add(93, id="S107-SEM-008", type="semantic_history", tradition="dirayet", ayah="107:1", role="semantic_range",
    relation="lexical", status="explicit", confidence="medium", priority="extended", audience="advanced",
    term="ed-dîn", scholar="al-Razi|al-Alusi",
    prose="“Din”in karşılık/borç ve boyun eğiş yönleri klasik kaynaklarda ayrı ayrı bulunur. Râzî bu bağlamda dînin “Allah’a boyun eğiş (hudû‘)” olduğunu söyler; mutlak dînin İslâm ıstılahında ve Kur’an’da İslâm demek olduğunu (3:19) ve öbür görüşlerin ancak kayıtla “din” diye anıldığını da kaydeder. Âlûsî “ed-dîn = ceza” anlamını “kemâ tedînü tüdân” (nasıl borç verirsen borç ödenirsin / nasıl karşılık verirsen karşılık görürsün) sözüyle destekler. Râzî ayrıca “yedu‘‘u”yu Tûr 52:13’e bağlar. Baz metindeki “din = itaat/boyun eğiş” (Maqâyîs) ve “din = karşılık/ödeme” okumaları bu nedenle klasik aralıkta ayrı ayrı yer alır; “borç/defter” sahnesi ise bir proje imgesidir (S107-NOV-010).",
    source="RAZI-107|ALUSI-107")

add(95, id="S107-TAF-013", type="tafsir", tradition="dirayet", ayah="107:7", role="early_attestation",
    relation="lexical", status="explicit", confidence="high", priority="extended", audience="advanced",
    scholar="Abu Ubayd|Zajjaj|Mubarrad|Abu Ubayda|Tabari|Razi|Akhfash", attested_in="Zamakhshari|Alusi|Biqai",
    prose="Baz metnin “mâûn cahiliyede her türlü yarar ve bağış, İslâm’da itaat ve zekâttır” cümlesi klasik tefsirde de açıkça vardır. Kurtubî bunu Zeccâc’a, Ebû Ubeyd’e ve Müberred’e bağlar ve er-Râî’nin “kavmün alâ’l-İslâmi lemmâ yemne‘û mâ‘ûnehüm” beytiyle destekler; Taberî aynı beyti “mâûn: itaat ve zekât” diye açıklar; Zemahşerî ve Âlûsî de beyti anar; Bikâî aynı bilgiyi Ebû Ubeyde’ye bağlar. Râzî ayrıca “mâûn = hüsnü’l-inkıyâd” görüşünü “devene bineği öğret ki sana mâûnu versin” (yani itaat etsin) örneğiyle verir; Kurtubî aynı görüşü Ahfeş’in bir bedeviden duyduğu söz ve bir recez parçasıyla belgeler. Bu nedenle “mâûn = itaat” kolu mevcuttur ama en az taşınan koldur; baz metin onu zekâtla birlikte kullanır.",
    source="QURT-107|TAB-107|KASH-107|ALUSI-107|BIQ-107|RAZI-107")

add(95, id="S107-NOV-009", type="novelty", tradition="project", ayah="107:1|107:7", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="partial",
    checked_sources=CHK,
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “ilk nesne (ed-dîn) ile son nesne (mâûn) itaatte buluşur” tezi için denetim. Klasik kaynaklarda iki bileşen de açıkça vardır: Râzî dînin Allah’a boyun eğiş olduğunu (107:1) ve mâûnun hüsnü’l-inkıyâd, itaat olduğunu (107:7) söyler; Taberî ve Kurtubî mâûnu itaat ve zekât diye verir; Bikâî ise sûrenin sonunun başa döndüğünü, “bu son, birincinin aynıdır, çünkü onu buraya taşıyan tekzîptir” (107:7) diye açıkça söyler. Ancak ilk ve son nesnenin “itaat” kavramında buluştuğunu tek yargıda söyleyen bir kaynak bulunmadı; bu bağ bileşenleri klasik, birleşimi proje sentezidir.",
    source="RAZI-107|TAB-107|QURT-107|BIQ-107")

add(97, id="S107-NOV-010", type="novelty", tradition="project", ayah="107:1|107:7", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="building_blocks_only",
    checked_sources=CHK,
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “borç, hesap ve defter” çerçevesi (dâyentü, dintü, “kezebe aleykumu’l-hacc” deyimi ve “ödenmeyen küçük borç”) için denetim. Yapıtaşı: Âlûsî’de “ed-dîn = ceza, kemâ tedînü tüdân”. “Dâyentü/dintü” borç deyimleri, “kezebe aleyke” = “üzerine vacip oldu” deyimi ve yedinci ayetteki küçük esirgemenin bir borcun ödenmemesi olarak okunması kontrol edilen tefsirlerde bulunmadı. Birleşik defter imgesi proje sentezidir ve bağlamsal anlamın yerine geçmez.",
    source="ALUSI-107|BASE-LEX")

# ------------------------------------------------------------ SECTION 9
add(105, id="S107-TAF-014", type="tafsir", tradition="rivayet", ayah="107:4|107:5|107:7", role="intertext",
    relation="lexical", status="explicit", connection="strong", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Tabari",
    prose="Tevbe 9:103 için Taberî “ve salli aleyhim”i “onlar için dua et, bağışlanma dile” diye, “inne salâteke seken lehüm”ü “duan ve bağışlanma dilemen onlar için huzurdur (tatmin)” diye açıklar; İbn Abbas’tan “rahmet”, Katâde’den “vakar” da aktarılır. “Sadaka”yı Taberî’nin kendi şerhi “temizler, yükseltir” diye anlatır ve zekâtı bir rivayette (İbn Abbas’a dayandığı anlaşılan bir zincirde) “Allah’a itaat ve ihlâs” diye verir. Taberî ayrıca okuyuş farkını kaydeder: Medine okuyucuları “salavâtike”, Irak okuyucuları ve bazı Mekkeliler “salâteke” okur ve Taberî tekil okuyuşu (çokluk ve çeşitliliği daha iyi taşıdığı için) tercih eder. Baz metnin “salât = dua; sekîne = huzur” bağı bu nedenle Taberî’de bu ayet için açıkça vardır; ancak 107. sûreyle ilişkisi klasik kaynakta kurulmaz.",
    source="TAB-9-103")

add(105, id="S107-NOV-011", type="novelty", tradition="project", ayah="107:4|107:5|107:7", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="partial",
    checked_sources=CHK + "|TabariSura9:103",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “mal, dua ve huzur halkası; sûrenin adamları bu halkayı ortasından koparır” okuması için denetim. Eski olan: namaz ile zekâtın ikiz olması (Zemahşerî, Beyzâvî: “zekât namazın kardeşi ve İslâm’ın köprüsü”), Râzî’de “namaz Allah için, mâûn halk içindir; Allah’a ait olanı halka sunarlar, halkın hakkı olanı onlardan saklarlar” biçiminde ters çevirme (S107-SEM-005 ile birlikte), Taberî’de 9:103’te salât-dua ve seken-huzur. Bulunmayan: 9:103 halkasının 107. sûrenin sahnesine uygulanması ve “dışa dönük namaz” tezi. Yapıtaşları klasiktir; uygulama proje sentezidir.",
    source="KASH-107|BAYD-107|RAZI-107|TAB-9-103")

add(109, id="S107-XQ-009", type="cross_quran", tradition="dirayet", ayah="107:5|107:6|107:7", role="corroboration",
    relation="thematic", status="explicit", connection="strong", confidence="medium", priority="extended", audience="advanced",
    attested_in="Qurtubi|Razi|Ibn Kathir",
    prose="Baz metnin bu bölümündeki bağlardan bazıları klasik şerhlerde 107 ile birlikte anılır. Kurtubî 107:5’te Meryem 19:59’u (“namazı yitirdiler”) anar ve 107:7’de münafıkların üçlüsünü (namaza üşenerek gelmek, gösteriş yapmak, ancak isteksizce harcamak) Nisâ 4:142 ve Tevbe 9:54’le birlikte verir. Râzî dördüncü ayette “namaz fuhşiyattan ve münkerden alıkoyar” (29:45) ayetini soru olarak getirir (S107-NAZ-002). İbn Kesîr beşinci ayette Nisâ 4:142’yi anar. Baz metindeki öteki bağlar (11:87, 19:31, 2:83) taranan sayfalarda bulunmadı.",
    source="QURT-107|RAZI-107|KATH-107")

# ------------------------------------------------------------ SECTION 10
add(115, id="S107-NAZ-003", type="nazm", tradition="nazm", ayah="107:1|107:7", role="nazm",
    relation="structural", status="explicit", confidence="high", priority="core", audience="general",
    scholar="al-Biqai",
    prose="Baz metnin “sûre başladığı yerde biter” fikri Bikâî’de açıkça vardır. Bikâî 107:7’de, “bu son, birincinin aynıdır; çünkü onu buraya taşıyan tekzîptir” der ve bu önemsiz şeyleri esirgeyenin mahşerde Kevser’e varmaktan men edilmeye lâyık olduğunu ekler. Sûrenin kapanışında “nasıl sonu başına kavuştuysa, sûre bütün olarak da (Kur’an’ın başından sayılan) benzeri Enfâl’e kavuştu” der ve Enfâl’den namaz-infak (8:4), duanın alay hâli (8:32), Beytullah’ta namazın ıslık ve el çırpma olması (8:35), cehenneme sürülme (8:36), humus ve yetimler ile yoksullar (8:41) ve gösteriş (8:47) ayetlerini sayar. Dolayısıyla “son = ilk” nazm gözlemi klasik kaynakta vardır; Bikâî’nin bunu başa dönüşün içeriği olarak tekzîbe bağlaması baz metnin itaat tezinden farklıdır.",
    source="BIQ-107")

add(119, id="S107-NOV-012", type="novelty", tradition="project", ayah="107:1|107:3|107:4", role="novelty_assessment",
    relation="thematic", status="interpretive", connection="strong", classical_attestation="none_found_in_checked_sources",
    checked_sources=CHK,
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin Müddessir 74:42-46’yı “bütün imgeleri tek ağızdan söyleyen sahne” diye okuması için denetim. Kontrol edilen 107. sûre sayfalarında Müddessir’deki namaz, doyurma, dalma ve din gününü yalanlama dizisiyle 107’nin ilişkilendirildiği bir açıklama bulunmadı; Müddessir’in kendi tefsir sayfaları bu çalışmada okunmadığı için sonuç yalnızca taranan sayfalarla sınırlıdır. Bağ, iki sûrenin ortak unsurlarının (namaz, yoksulu doyurma, yalanlama) metin düzeyinde doğrudan karşılaştırmasına dayanır ve proje okuması olarak değerlendirilmelidir.",
    source="BASE-LEX")

add(125, id="S107-NAZ-004", type="nazm", tradition="nazm", ayah="107:7", role="nazm",
    relation="structural", status="explicit", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Biqai|al-Razi",
    prose="Komşu sûre ilişkisi için Bikâî 108:1’de şunu söyler: Dîn sûresi “cimrilerin en cimrisi ve yaratıkların en aşağısı: men‘” ile bitti; Kevser sûresi tersine “cömertliğin en cömerti: ata” ile başlar ve en şerefli yaratığa verilir; yani Peygamber, Mâûn’un yasakladığı şeylerin hiçbirine bulaşmış değildir. Râzî sûrenin sonunda şöyle dua eder: bu sûre münafıkları, sonraki sûre Muhammed’in sıfatını anlatır. Baz metnin kapanış paragrafı bu komşu sûre ilişkisini kurmaz; ilişki klasik kaynaklarda kayıtlıdır.",
    source="BIQ-106-108|RAZI-107")

add(125, id="S107-SRC-003", type="source_note", tradition="project", ayah="107:7", role="source_criticism",
    relation="methodological", status="interpretive", confidence="high", priority="research", audience="research",
    prose="Bikâî sûrenin kapanışında sûrenin kelime sayısı (25) ile Hicret’in 12. ve 16. yıllarındaki ridde savaşları ve fetihler arasında bir hesap uyumu kurar ve sûrenin münafık ve murtedlerin “gösteriş için namaz kılıp zekâtı esirgemesini” tarihsel ridde olaylarıyla da bağlar. Bu, Bikâî’nin kendi sayısal nazm yorumudur; bu dosya onu baz metne bağlamaz ve tarihsel bir olgu olarak kullanmaz; yalnızca Bikâî’nin sûreyi böyle okuduğunu kaydeder.",
    source="BIQ-107")

add(125, id="S107-MEAL-009", type="semantic_history", tradition="historical", ayah="107:1-7", role="interpretive_consequence",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    scope="meal-review:summary",
    prose="Meal incelemesinin özeti (hata, yanıltıcı ve savunulabilir daraltma ayrımı). Ortak çekirdekte (yalanlamak, yetimi itip kakmak, yoksulu doyurmaya teşvik etmemek, namaz kılanlara veyl, gösteriş) mealler birbirine ve klasik kaynaklara yakındır; farklar anahtar kelimelerde toplanır. Kesin hata ya da yanıltıcı sayılanlar: (a) ‘an yerine “namazlarında” çevirisi (Bulaç, Onan, Bilmen’in kuranmeali.com metni, Elmalılı’nın sadeleştirilmiş metni): klasik şerhlerin açıkça ayırdığı fî anlamını verir ve veylin kime yöneldiğini değiştirir (S107-MEAL-003). (b) Fiili “yalan söylemek”e kaydıran Süleymaniye Vakfı varyantları (S107-MEAL-002). (c) Veyli “lanet” diye veren Öztürk varyantı (varyantın basımı belirsiz; S107-MEAL-008). (d) Musallîn’i “sürekli didinip duranlar” yapan Süleymaniye Vakfı metni (S107-MEAL-008). Aralığı daraltan ama erken bir otoriteye dayanan seçimler: güncel Diyanet’in “hesap ve ceza günü” (Taberî, İbn Cüreyc, İbn Kesîr, Râzî’nin çoğunluk görüşü), “özendirmeyen” (başkasını teşvik; Taberî, Zemahşerî), “namazlarını ciddiye almazlar” (umursamama kolu; Zemahşerî, Katâde, Taberî’nin lâhûn’u) ve “ufacık bir yardım” (ma‘n; Kutrub, Râzî, İkrime’nin “en aşağısı”); Hayrat, Çantay ve Gölpınarlı’nın “zekât”ı (Ali, İbn Ömer, Hasan, Katâde); Yazıklar olsun (veyl tonunu yumuşatma). Aralığı korumaya en yakın seçimler: Okuyan ve Hayrat’ın “Dini (hesap gününü)”, Öztürk ve Bulaç’ın mâûn için sıraladığı seçenekler, Ateş ve Gölpınarlı’nın “önayak olmaz”/“doyurmaz da önayak olmaz da”, Bilmen’in “men edilmesi mutad olmayan bir şeyi bile”, Esed’in “kalpleri namazlarına yabancıdır”. Hiçbir taranan meal vakit geciktirme kolunu (Sa‘d, Mesrûk, İbn Abbas), yetimin hakkından itilmesi kolunu (İbn Abbas, Taberî) ya da suyu, ateşi ve tuzu (Âişe) göstermez; bu, en iyi belgelenmiş bazı dalların meallerde temsil edilmediği anlamına gelir. Bu bloklar çevirmenleri hükme bağlamak için değil, kullanıcının hangi seçimin neyi seçtiğini görebilmesi içindir.",
    source="MEAL-DIY-107|MEAL-OKU-107|MEAL-YNO-107|MEAL-BUL-107|MEAL-ONAN-107|MEAL-BIL-107|MEAL-ELM-107|MEAL-SUL-107|MEAL-HAY-107|MEAL-CAN-107|MEAL-GOL-107|MEAL-ATE-107|MEAL-ESED-107|TAB-107|KASH-107|RAZI-107|KATH-107|BIQ-107")
