# -*- coding: utf-8 -*-
# Annotation block data, part A: top matter, sections 1-3 (base lines 1-41).
# Each entry: (anchor_line, block_dict). anchor_line = 1-based line number of the base
# paragraph AFTER which the block is inserted; 0 = before the first base heading.

CHK_ALL = "Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi|IbnAtiyya|Wahidi"

A = []

def add(anchor, **kw):
    A.append((anchor, kw))

# ------------------------------------------------------------------ TOP
add(0, id="S107-RDR-001", type="reader_note", tradition="project", ayah="107:1-7", role="reader_orientation",
    relation="methodological", status="interpretive", priority="core", audience="general",
    prose="Bu dosyada ana yorum metni olduğu gibi korunmuştur. Satır başında “{id:...}” ile başlayan bloklar sonradan eklenmiş kanıt katmanlarıdır ve okuyucu tarafından gizlenip gösterilebilir. type alanı bilginin türünü verir (tefsir, hadis, kıraat, esbâb, anlam tarihi, nazm, Kur’an içi paralel, yöntem notu, yenilik denetimi, kaynak notu), tradition alanı kaynağın geleneğini, role alanı bloğun neden o noktada durduğunu, relation alanı ise kanıtın ayetle ilişkisini söyler: doğrudan tefsir mi, tematik bir paralel mi, lafızla mı ilgili. Klasik kaynaklardan gelen bilgi (rivâyet ve dirâyet blokları), tarih ve bağlam blokları, çağdaş meallerin incelenmesi ve projenin kendi sentezi bilerek ayrı tutulmuştur. Kök ailesinden gelen bir imge ayetin bağlamsal anlamının yerine geçmez; bu sınır ilgili yerlerde ayrıca belirtilmiştir.",
    source="BASE-LEX")

add(0, id="S107-RDR-002", type="reader_note", tradition="project", ayah="107:1-7", role="reader_orientation",
    relation="methodological", status="interpretive", priority="core", audience="general",
    scope="meal-review:overview",
    prose="Bu dosyada Mâûn Sûresi’nin yaygın Türkçe mealleri de ayrıca incelenmiştir. Bu bloklar klasik kaynaklardan gelen bir tanıklık değildir; belirli bir anahtar kelimede (yukezzibu bi’d-dîn, yedu‘‘u’l-yetîm, lâ yehuddu alâ ta‘âmi’l-miskîn, sâhûn ve “an” edatı, yurâûn, mâûn, ed-dîn, veyl) hangi meâlin hangi sözü seçtiğini, bu seçimin hangi erken otoriteyle desteklendiğini ve çok dallı bir anlam aralığını tek dala indirgeyip indirgemediğini gösterir. Süzmek için: kimliği S107-MEAL- ile başlayan blokları ya da scope alanı meal-review: ile başlayanları seçin. Hepsi tradition:historical, relation:comparative veya lexical, status:interpretive veya inferred olarak işaretlidir. Ayrım şöyle yapılır: Arapçaya ve klasik kanıta aykırı bir anlam kayması “hata” ya da “yanıltıcı” diye adlandırılır; erken kaynaklardan birine dayanan ama aralığı daraltan seçim “savunulabilir daraltma” diye adlandırılır. Meal metinlerinin nereden alındığı ve hangileri bulunamadı bilgisi S107-SRC-002 bloğundadır.",
    source="BASE-LEX")

add(0, id="S107-SRC-002", type="source_note", tradition="project", ayah="107:1-7", role="source_criticism",
    relation="methodological", status="explicit", confidence="medium", priority="extended", audience="advanced",
    scope="meal-review:sources",
    prose="Meal metinleri için kaynak durumu. Depoda (quran-data, quran-roots, _commentary, _translation) yaygın meallerin metni bulunmadı; yalnızca projenin kendi Türkçe metinleri ve sözlük açıklamaları var. Metinler 2 Ekim 2026’da web’den, WebFetch aracıyla alındı. Bu araç sayfanın kendisini değil, bir modelin ürettiği sayfa özetini döndürdüğü için bir söz ancak iki ayrı sayfada tutarlıysa ya da resmî sitede doğrulandıysa temel alındı. Bulunan ve kullanılan metinler: Diyanet İşleri Başkanlığı (güncel meal; resmî site ve üç başka sayfa), Diyanet (eski, aggregator etiketiyle), Mehmet Okuyan, Yaşar Nuri Öztürk (iki ayrı varyant, aşağıya bakın), Elmalılı Hamdi Yazır (özgün ve sadeleştirilmiş metin; iki aggregator bu iki metni farklı etiketlerle sunuyor), Ömer Nasuhi Bilmen, Süleyman Ateş, Hayrat Neşriyat, Abdülbaki Gölpınarlı, Ali Bulaç, Diyanet Vakfı; ayrıca ek olarak Süleymaniye Vakfı, Mustafa İslamoğlu, Muhammed Esed’in Türkçe çevirisi, Hasan Basri Çantay, Gültekin Onan, İsmail Hakkı İzmirli. Bulunamayan: Celal Yıldırım (hiçbir sayfa metni alınamadı; ona söz atfedilmedi). Dolaylı alınan: Edip Yüksel (yalnızca bir arama sonucu özeti; sayfalar 403 ve 500 verdi; sadece düşük güvenli teyit olarak kullanıldı). Bilinen metin ayrışmaları: Öztürk meali web’de iki biçimde görünüyor (acikkuran.com ve ayetbul.net: “Vay haline o namaz kılanların ki”; kuranmeali.com: “Lanet olsun o namaz kılanlara/dua edenlere ki”); hangisinin hangi basıma ait olduğu belirlenemedi. Süleymaniye Vakfı’nın 107:1 metni de iki farklı biçimde görünüyor. Diyanet Vakfı’nın 107:4-5 satırı güncel Diyanet metniyle özdeş görünüyor. Tüm Türkçe meal alıntıları kısa anahtar ifadelerle sınırlandı.",
    source="AGG-ACIK-107|AGG-KMEALI-107|WEB-DIYANET-107|WEB-AYETBUL-YNO")

add(0, id="S107-SRC-001", type="source_note", tradition="project", ayah="107:1-7", role="source_criticism",
    relation="methodological", status="explicit", confidence="high", priority="research", audience="research",
    prose="Klasik kaynak durumu. Tabersî, İbn Kesîr, Kurtubî, Süyûtî (ed-Durru’l-mensûr), Zemahşerî, Râzî, Beyzâvî ve Bikâî için 107. sûrenin ayet sayfalarının metinleri bu çalışmanın kaynak önbelleğinden (work/107_sonnet_5_5/sources) okundu ve doğrudan alıntılanan yerler kaynak metinle karşılaştırıldı; bu metinler yeniden indirilmedi. Âlûsî yalnızca 107:1 ve 107:7 sayfalarından, İbn Atıyye yalnızca 107:1 sayfasından, Vâhidî ise yalnızca 107:1-2 için (kaynak sayfada 3-7 için “bu kitapta tefsir yok” yazıyor) okunabildi; bu üç kaynağın okunmayan bölümleri hakkında hüküm verilmedi. Hadis birincil derlemelerinin sayfalarına (sunnah.com ve benzerleri) erişilemedi (403); hadis bilgisi İbn Kesîr, Süyûtî ve Kurtubî’nin nakilleri üzerinden alınmış, yalnızca Sahîh-i Müslim’deki “tilke salâtü’l-münâfık” hadisinin koleksiyon etiketi ikincil bir sayfadan görülmüştür. Derece (hadith_grade) yalnızca bu kaynaklardaki eleştirmen ifadesi varsa verilmiş, yoksa not_assessed bırakılmıştır. Küçük bir ad farkı: Taberî ve İbn Kesîr “‘an salâtihim dedi, fî salâtihim demedi; buna hamd olsun” sözünü Atâ b. Dînâr’a bağlar; Süyûtî’nin metni aynı sözü Atâ b. Yesâr’a bağlar; hangisinin doğru olduğu bu çalışmada çözülmedi.",
    source="TAB-107|KATH-107|SUY-107|QURT-107|ALUSI-107|IATIYYA-107|WAH-107")

add(0, id="S107-REV-001", type="revelation_history", tradition="historical", ayah="107:1-7", role="chronology",
    relation="historical", status="disputed", historicity="contested", confidence="medium", priority="core", audience="general",
    prose="Mâûn Sûresi’nin Mekkî mi Medenî mi olduğu klasik kaynaklarda tartışmalıdır. Kurtubî sûrenin Atâ, Câbir ve İbn Abbas’ın bir görüşüne göre Mekkî, Katâde ve İbn Abbas’ın öteki görüşüne göre Medenî olduğunu kaydeder. Süyûtî, İbn Merdeveyh’in İbn Abbas’tan ve Abdullah b. Zübeyr’den “Mekke’de indi” rivayetini nakleder. Âlûsî cumhurun Mekkî dediğini, Bahr’da (Ebû Hayyân) İbn Abbas, Katâde ve Dahhâk’tan Medenî görüşün geldiğini, Hibetullah ed-Darîr’in ise sûrenin yarısının Mekke’de el-Âs b. Vâil hakkında, yarısının Medine’de münafık Abdullah b. Übey hakkında indiğini söylediğini aktarır; ayrıca ayet sayısının Irak sayımında yedi, öbür sayımlarda altı olduğunu belirtir. İbn Atıyye “bildiğim kadarıyla ihtilaf yok” diyerek Mekkî der ama Sa‘lebî’nin Medenî dediğini de ekler; aynı kaynaklar arasında bu çelişki çözülmemiştir. Zemahşerî “Mekkîdir, Medenî de denmiştir”, Beyzâvî “ihtilaflıdır” der. Bu tablo yalnızca Mekkî-Medenî tartışmasıdır; sebeb-i nüzûl rivayetleri ayrıdır (S107-ASB-001).",
    source="QURT-107|SUY-107|ALUSI-107|IATIYYA-107|KASH-107|BAYD-107")

add(0, id="S107-ASB-001", type="asbab", tradition="rivayet", ayah="107:1-2", role="asbab_context",
    relation="asbab", status="reported", historicity="contested", confidence="low", priority="extended", audience="advanced",
    attested_in="Baydawi|Qurtubi|Alusi",
    prose="Birinci ve ikinci ayetin kimin hakkında indiği konusunda birbirini dışlayan şahıslar anılır. Vâhidî’de Mukâtil ve Kelbî el-Âs b. Vâil es-Sehmî’yi söyler; İbn Cüreyc ise Ebû Süfyân b. Harb’ı anar: haftada iki deve keser, yanına gelen yetim bir şey isteyince onu asasıyla kovarmış. Râzî buna Süddî’den el-Velîd b. el-Muğîre’yi, Mâverdî’den Ebû Cehil’i (yetimin vasisiydi, çıplak gelip kendi malından isteyen yetimi geri çevirdi; Kureşli büyükler alay için onu Peygamber’e göndermiş, Peygamber’le gidince Ebû Cehil malı vermiş) ve İbn Abbas’tan cimriliği ve riyayı birleştiren bir münafığı ekler. Kurtubî Dahhâk’tan Amr b. Âiz’i, Ebû Sâlih yoluyla İbn Abbas’tan el-Âs b. Vâil’i verir. Râzî ayrıca ayetin tek bir kişiye değil, ahireti yalanlayan herkese ait genel bir hüküm olduğu görüşünü de kaydeder. Bu rivayetlerden hiçbiri bu dosyada tarihsel olgu olarak alınmamıştır ve en canlı anlatı öne çıkarılmamıştır; sebeplerin çokluğu, ayetin bir kişiye bağlanamadığı görüşünü güçlendiren bir veridir.",
    source="WAH-107|RAZI-107|QURT-107|BAYD-107|ALUSI-107")

add(0, id="S107-ASB-002", type="asbab", tradition="rivayet", ayah="107:7", role="asbab_context",
    relation="asbab", status="reported", historicity="uncertain", confidence="low", priority="research", audience="research",
    origin="Ibn Mardawayh via Suyuti",
    prose="Süyûtî, İbn Merdeveyh’in İbn Mes‘ûd’dan şu rivayetini verir: Müslümanlar münafıklardan kova, kazan, balta gibi şeyleri ödünç isterlermiş, onlar da vermezlermiş; bunun üzerine “ve yemne‘ûne’l-mâ‘ûn” inmiş. Rivayetin isnadı bu çalışmada görülmemiştir; kontrol edilen öbür kaynaklarda (Taberî, İbn Kesîr, Kurtubî, Râzî) aynı sebep-i nüzûl anlatısı bulunmadı. Bu nedenle tek koleksiyoncuya bağlı, doğrulanmamış bir rivayet olarak kaydedilir ve “münafıklar–ödünç eşya” bağını güvence altına almaz.",
    source="SUY-107")

add(0, id="S107-MET-001", type="method_note", tradition="project", ayah="107:4|107:5|107:6", role="constraint",
    relation="historical", status="inferred", confidence="low", priority="research", audience="research",
    prose="Bir gerilim notu. Taberî, İbn Abbas, Mücâhid ve Dahhâk’a dayanarak sâhûn ve yurâûn olanları “Peygamber zamanında küfrü içlerinde saklayıp İslâm’ı gösteren münafıklar” diye açıklar; aynı zamanda sûrenin çoğunlukla Mekkî sayıldığı bilinir (S107-REV-001). Bu iki bilgi kaynaklarda açıkça uzlaştırılmamıştır. Çıkarım olarak iki yol görünür: “münafık” kelimesi burada gizli inkârcı tipini genel olarak anlatıyor olabilir (Râzî ayeti genel okur ve hüküm “dini yalanlayan herkes” için geçerlidir), ya da Hibetullah’ın sûreyi ikiye bölen görüşü benimsenir. Bu dosya münafık kimliğini zorunlu hüküm olarak değil, güçlü bir erken yorum olarak kaydeder ve baz metindeki “bu adamlar” ifadesini bu sınır içinde okur.",
    source="TAB-107|RAZI-107|ALUSI-107")

# ------------------------------------------------------------------ SECTION 1  (base lines 3..13)
add(3, id="S107-TAF-001", type="tafsir", tradition="dirayet", ayah="107:1", role="clarification",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    scholar="Zamakhshari|Razi|Baydawi|Alusi|Biqai", term="arâeyte",
    prose="“Erâeyte” klasik şerhlerde bir görme sorusu olarak değil, dikkat çekme ve şaşırtma olarak açıklanır. Zemahşerî ve Râzî anlamı “bana haber ver”/“kim olduğunu biliyor musun?” diye verir ve ardına şunu ekler: onu tanımıyorsan, işte o yetimi itip kakan kişidir; yani ikinci ayet bu sorunun cevabıdır (baz metindeki “bir eli gösteren parmak” okumasının klasik karşılığı). Beyzâvî soruyu “şaşkınlık bildiren istifham” sayar; Âlûsî “dinleyiciyi merakla tanımaya çağırma ve şaşırtma” der, hitabın Peygamber’e ya da bu hitaba elverişli herkese olabileceğini söyler ve görme fiilinin “ahbirnî” anlamıyla iki mef‘ûllu olabileceğini, ikinci mef‘ûlun “kimdir?” ya da “azabı hak etmiyor mu?” diye takdir edilebileceğini belirtir. Bikâî hitabı “ümmetin başı”na yöneltilmiş sayar ve ikinci mef‘ûl olarak “ondan intikam alınmaya layık değil mi?” takdirini verir. Râzî’de hitap akıl sahibi herkese de uzatılır: ebedî cezayı kısa süreli bir kazanç için satın alan kimse aklı başında biri olabilir mi?",
    source="KASH-107|RAZI-107|BAYD-107|ALUSI-107|BIQ-107")

add(3, id="S107-QIR-001", type="qiraat", tradition="rivayet", ayah="107:1", role="clarification",
    relation="grammatical", status="reported", priority="research", audience="research",
    note="Companion and non-canonical attributions are given as reported; canonical classification not assessed here.",
    prose="Birinci ayette okuyuş farkları kaydedilmiştir. (1) “Erâeyte” yerine hemzesiz “erayte”: Zemahşerî ve Râzî, Zeccâc’a dayanarak bunu tercih edilen biçim saymaz, çünkü hemze atma geçmiş zamanda değil muzâri‘de olur; baştaki istifham hemzesi işi kolaylaştırmıştır. Âlûsî bu okuyuşu Kisâî’ye nispet eder; İbn Atıyye Ebû Amr’ın hemzeyi “ihtilaflı” okuduğunu, Nâfi‘in okumadığını söyler. (2) İbn Mes‘ûd’a nispetle “erâeytek” (hitap kâfı eklenmiş): Zemahşerî, Râzî, Beyzâvî, Âlûsî. (3) Taberî’ye göre “Abdullah”ın okuyuşunda “yükezzibü’d-dîne” (bâ yok); Taberî bâ’yı sıla sayar, girmesiyle çıkması aynıdır. Bu nispetlerin kanonik ya da şâz sınıflandırması burada değerlendirilmemiştir. Anlam bakımından hiçbiri baz metindeki okumayı değiştirmez.",
    source="KASH-107|RAZI-107|BAYD-107|ALUSI-107|IATIYYA-107|TAB-107")

add(3, id="S107-NAZ-001", type="nazm", tradition="nazm", ayah="107:1", role="nazm",
    relation="structural", status="explicit", confidence="medium", priority="extended", audience="advanced",
    scholar="al-Biqai",
    prose="Bikâî sûrenin başlangıcını öncesine bağlar: Kureyş sûresi sonunda nimeti verene yalnız ona kulluk etmeyi emretmiştir; bu sûre başında, o kulluğun ancak hesaba ve karşılığa inanmakla gerçekleşebileceğini bildirir ve bunu yalanlayanı en çirkin biçimde tasvir eder. İbn ez-Zübeyr’den (Bikâî’nin nakliyle) şu açıklama gelir: önceki sûreler insanın doğasındaki cehalet ve zulümden doğan huyları (nankörlük, hüsran, malın kendini ölümsüz kılacağını sanma, çokluk yarışı, ayıplama, Fil olayındaki gurur) tehdit etmişti; bu sûre ise İslâm’a mensup olanlarda da bulunabilen davranışları (yetimi itme, yoksulu doyurmaya teşvik etmeme, namazı bırakma, riya, küçük yardımı esirgeme) sayar ve bunların hesabı yalanlayanın sıfatları olduğunu bildirir.",
    source="BIQ-107")

add(5, id="S107-TAF-002", type="tafsir", tradition="dirayet", ayah="107:6", role="anchor",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    scholar="Zamakhshari|Razi|Qurtubi|Tabari", term="yurâûn",
    attested_in="Baydawi",
    prose="Altıncı ayetteki fiilin karşılıklılık yapısı klasik açıklamada da vardır. Zemahşerî ve Râzî “el-müraât”ı “irâe”den gelen bir müfâale sayar: gösteriş yapan kişi insanlara işini gösterir, insanlar da ona övgüyü ve beğeniyi gösterir. Her ikisi de farz bir ibadeti açıkça yapmanın riya olmadığını söyler (“Allah’ın farzlarında örtme yoktur” sözüyle), gizliliğin nâfilelerde esas olduğunu belirtir; riya, gösterme niyetinin insanların göreceği, övgü getireceği şekilde yönelmesidir. Râzî münafık ile müraiyi ayırır: münafık imanı gösterip küfrü saklar, müraî ise kalbinde olmayan bir huşuu gösterir. Kurtubî riyanın hakikatini “ibadetle dünya talebi” diye verir ve İbn Arabî’den dört biçimini sayar (güzel görünüş/duruş, kısa ve kaba giyim, sözle gösteriş, namaz ve sadakayı göstererek ya da güzelleştirerek). Taberî ise münafıkların insanlar görsün diye namaz kıldığını, çünkü öyle yaparak kanlarının dökülmesinden ve çocuklarının esir edilmesinden korunduklarını söyler.",
    source="KASH-107|RAZI-107|QURT-107|TAB-107|BAYD-107")

add(5, id="S107-HAD-006", type="hadith", tradition="hadith", ayah="107:6", role="constraint",
    relation="thematic", status="reported", hadith_grade="not_assessed", connection="strong", priority="extended", audience="general",
    transmitter="Abu Hurayra; Abdullah b. Amr", origin="Ibn Kathir under 107:6",
    prose="İbn Kesîr altıncı ayetin yanında riya ile ilgili iki hadis türü anar; ikisi de ayeti doğrudan tefsir etmez, tematik paralelidir. Birincisi Ahmed’den (Abdullah b. Amr): kim insanlara yaptığı işi duyurursa Allah da onu yaratıklarının işiteceği biçimde duyurur ve onu hakir ve küçük kılar. İkincisi, bir işi gizlice yapıp insanlar öğrenince hoşlanan kişi için “ona iki ecir vardır: gizlinin ve açığın” diyen Ebû Hureyre rivayetidir; İbn Kesîr bunu Ebû Ya‘lâ’dan ve Tirmizî ile İbn Mâce’den verir, Tirmizî’nin “garîb” dediğini ve bir kısım ravilerin mürsel rivayet ettiğini aktarır. Bu ikinci hadis, ayetteki “yurâûn”un bir işin görülmesini ya da bundan hoşnut olmayı değil, ibadeti insanlar görsün diye yapmayı kastettiğini sınırlar. Derece bu çalışmada bağımsız olarak incelenmemiştir.",
    source="KATH-107")

add(5, id="S107-NOV-001", type="novelty", tradition="project", ayah="107:6", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="partial",
    checked_sources="Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)",
    confidence="medium", priority="research", audience="research",
    prose="Baz metnin “ayna” ağı için denetim. Eski olan kısım: gösteren ile gösterilenin karşılıklı görme ilişkisi (müfâale; gösteren işi gösterir, seyirci övgüyü gösterir) kontrol edilen kaynaklarda açıkça bulunur (Zemahşerî, Râzî; S107-TAF-002). Ayna (mir’ât), derinliksiz yüzey ve “er-riyyü/ruvâ’ güzel görünüştür” tanımı ise bu klasik açıklamalarda bir tefsir imgesi olarak bulunmadı; lugat malzemesi (Maqâyîs ve öbür sözlükler) ayrı ayrı vardır. Birleştirilmiş yüzey–derinlik–seyirci imgesi proje sentezidir ve ayetin bağlamsal anlamını değil, anlamın işleyişini görünür kılar.",
    source="KASH-107|RAZI-107|BASE-LEX")

add(13, id="S107-XQ-001", type="cross_quran", tradition="dirayet", ayah="107:5|107:6", role="corroboration",
    relation="thematic", status="explicit", connection="strong", confidence="high", priority="extended", audience="advanced",
    attested_in="Razi|Qurtubi",
    prose="Baz metindeki Nisâ 4:142 bağı (“namaza kalktıklarında üşenerek kalkarlar, insanlara gösteriş yaparlar”) klasik açıklamada aynı yerde vardır: İbn Kesîr bu ayeti beşinci ayetin yanında okur ve münafığın namazını anlatan hadisle birlikte verir; Râzî ve Kurtubî de aynı ayeti sehv ve riya bağlamında anar. Baz metnin öbür bağlarından 4:38 (malı gösteriş için harcamak), 96:9-14, 26:218-219, 76:9 ve 92:19-20, kontrol edilen 107. sûre sayfalarında bulunmadı.",
    source="KATH-107|RAZI-107|QURT-107")

# ------------------------------------------------------------------ SECTION 2  (base lines 19..27)
add(19, id="S107-SEM-001", type="semantic_history", tradition="rivayet", ayah="107:1", role="semantic_range",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    term="ed-dîn", scholar="Tabari|Ibn Abbas|Ibn Jurayj|Kathir|Razi|Baydawi|Alusi|Ibn Atiyya",
    prose="Birinci ayetteki “ed-dîn” erken ve geç kaynaklarda şu dallarla geçer. Taberî kendi cümlesinde “Allah’ın sevabını ve azabını yalanlayan” der; İbn Abbas’tan “Allah’ın hükmünü”, İbn Cüreyc’ten “hesabı” aktarır; Hasan’dan gelen rivayette (Süyûtî) “kâfir”dir. İbn Kesîr “mead ve karşılık”, Kurtubî “ahiretteki ceza ve hesap”, İbn Atıyye “ceza, sevap ve azap olarak; hesap buna yakındır” der. Beyzâvî “ceza ya da İslâm” der. Âlûsî “din” kelimesinin bir anlamının ceza olduğunu (“kemâ tedînü tüdân”), Mücâhid’den hesap ve İslâm’ı verir ve “Kur’an” ile “Allah’ın hükmü” diyenleri de İslâm’ı kastetmiş sayarak uzlaştırır. Râzî, “herkesin bir dini vardır” itirazına üç vecihle cevap verir: mutlak “din” İslâm ıstılahında İslâm’ın kendisidir; öbür inançlar din sayılmaz, çünkü din Allah’a boyun eğiştir, onlar ise şehvete ya da şüpheye boyun eğiştir; ve çoğu müfessirin görüşü olarak kastedilen hesap ve cezadır. Çoğunluğun gerekçesi şudur: İslâm’ı inkâr eden biri ahirete inanıyorsa iyiliği yapıp kötülükten sakınabilir; her çirkinliğe aldırmadan girişen ise ancak ba‘sı ve kıyameti inkâr edendir. Yani klasik aralık tek değildir: ağırlık hesap-ceza dalındadır, ama İslâm/din ve Allah’ın hükmü dalları da canlıdır.",
    source="TAB-107|SUY-107|KATH-107|QURT-107|IATIYYA-107|BAYD-107|ALUSI-107|RAZI-107")

add(21, id="S107-NOV-002", type="novelty", tradition="project", ayah="107:1", role="novelty_assessment",
    relation="lexical", status="interpretive", connection="resonant", classical_attestation="partial",
    checked_sources="Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)",
    confidence="medium", priority="research", audience="research",
    prose="Boyalı kumaş (kezzâbe) ve “yarıda kalan hareket” deyimleri (hücum, süt, yabani hayvanın koşusu) üzerinden kurulan “yüzey–iç” imgesi için denetim. Kontrol edilen kaynaklarda bu deyimler ve kumaş imgesi bulunmadı. Buna karşılık imgenin taşıdığı düşünce, yani yalanlamanın yalnızca bir cümleyle değil davranışla anlaşıldığı, klasik tefsirde açıktır: Zemahşerî “hesabı yalanlamanın alâmetini, iyiliği esirgemek ve zayıfı incitmeye girişmek yaptı; şayet hesaba inansa ve tehdide yakîn etse bunu yapmazdı” der; Râzî de aynı gerekçeyi verir (S107-TAF-005). Bu nedenle düşünce kısmen klasiktir; kumaş ve hayvan deyimleriyle kurulan imge proje sentezidir ve bağlamsal anlam yerine geçmez.",
    source="KASH-107|RAZI-107|BASE-LEX")

add(23, id="S107-MEAL-001", type="semantic_history", tradition="historical", ayah="107:1", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="ed-dîn", scope="meal-review:ed-dîn", scholar="Diyanet (güncel ve eski)|Okuyan|Hayrat|Ateş|Öztürk|Bulaç|Bilmen|Elmalılı|Esed|İslamoğlu",
    prose="Meal incelemesi: “bi’d-dîn”. Klasik aralık hesap-ceza, İslâm/din ve Allah’ın hükmü dallarını taşır (S107-SEM-001). Güncel Diyanet meali “hesap ve ceza gününü yalanlayanı” diyerek nesneyi tek dala bağlar; aynı kurumun eski metni “dini yalan sayanı” demiş ve aralığı korumuştu. Bu daraltma Taberî’nin (sevap ve azap), İbn Cüreyc’in (hesap), İbn Kesîr’in ve Râzî’nin “çoğu müfessir” dediği görüşün desteğine sahiptir; yani hata değil, savunulabilir bir daraltmadır, ancak İslâm/din dalı ve İbn Abbas’ın “Allah’ın hükmü” dalı okurdan gizlenir. Okuyan (“Dini (hesap gününü)”) ve Hayrat (“Dîni (hesab gününü)”) hem sözcüğü hem tefsiri parantezle birlikte verir; Ateş (“Din(ahiret cezasın)ı”) da parantezle daraltır; parantez okura seçimin tefsir olduğunu gösterdiği için daraltma görünür kalır. Öztürk’ün bir varyantı (“dini yalan sayanı”), Bulaç, Diyanet Vakfı, Bilmen (“dini tekzîp eder”) ve Elmalılı’nın özgün metni (“dîni tekzib edeni”) “din” sözcüğünü olduğu gibi bırakır; klasik aralığa en yakın seçim budur. Esed (“bütün bir ahlaki değerler sistemini”) ve İslamoğlu’nun bir varyantı (“Allah’a karşı borçluluk sorumluluğunu tümden inkâr eden”) dîni modern kavramlarla yeniden kurar; Râzî’nin “din Allah’a boyun eğiştir” tanımıyla akrabadır ama bu biçimde kontrol edilen klasik şerhlerde geçmez: hata değil, aralığın dışına taşan bir yorum çevirisidir.",
    source="MEAL-DIY-107|MEAL-DIYOLD-107|MEAL-OKU-107|MEAL-HAY-107|MEAL-ATE-107|MEAL-YNO-107|MEAL-BUL-107|MEAL-DVK-107|MEAL-BIL-107|MEAL-ELM-107|MEAL-ESED-107|MEAL-ISL-107|TAB-107|SUY-107|KATH-107|RAZI-107")

add(23, id="S107-MEAL-002", type="semantic_history", tradition="historical", ayah="107:1", role="constraint",
    relation="lexical", status="inferred", confidence="medium", priority="extended", audience="advanced",
    term="yukezzibu", scope="meal-review:yukezzibu", scholar="Süleymaniye Vakfı|Öztürk",
    prose="Meal incelemesi: fiilin cinsi. “Yukezzibu bi’d-dîn”, bâ ile geçişli bir taf‘îl fiilidir: bir şeyi yalan saymak. Taberî bunu “Allah’ın sevabını ve azabını yalanlamak” diye açıklar; yalanın kişinin kendi sözüne ait olduğu bir okuma kontrol edilen klasik şerhlerde görülmedi. Süleymaniye Vakfı’nın iki varyantı (“Bu din hakkında yalan söyleyip duranı”, “Bu dine karşı yalana sarılanı”) fiili “yalan söylemek/yalana sarılmak” anlamına kaydırır; yalan yalanlanan şeyden kişinin kendi davranışına taşınır. Bu yanıltıcıdır, çünkü ayetin nesnesi yalanlanan şey (din) olarak kalır; öte yandan baz metindeki Maqâyîs tanımı (kezib söz ve fiil için söylenir) kişinin davranışıyla yalan söylemesine bir lugat zemini verir, ancak bu zemin ayetin tefsiri değil, kök ailesi okumasıdır. Öztürk’ün bir varyantındaki “dini inkâr edeni” ise yalan sayma yerine inkâr der; fark küçüktür ve aralığı bozmaz.",
    source="MEAL-SUL-107|MEAL-YNO-107|TAB-107|BASE-LEX")

add(25, id="S107-TAF-005", type="tafsir", tradition="dirayet", ayah="107:2", role="clarification",
    relation="grammatical", status="explicit", confidence="high", priority="extended", audience="advanced",
    scholar="Razi|Baydawi|Zamakhshari|Alusi", term="fe",
    prose="İkinci ayetin başındaki “fe”nin işlevi klasik açıklamada açıktır ve baz metindeki okumayı destekler. Râzî fâyı “sebebiyyet” sayar: küfür yetimi itmenin sebebidir; yetimi itmek ve teşvik etmemek aynı zamanda iki kısmın birer örneğidir (fiil ve terk), her biriyle öbür kötülüklere işaret edilir, çünkü yalanlayanın yalnız bunları yaptığı düşünülemez. Beyzâvî cümleyi “yükezzibü”ye fâ ile bağlamayı hesabı inkârın bir sonucu olarak görür. Zemahşerî ikinci bir yol da gösterir: “fe-zâlike” “elleżî yükezzibü”ye atıf olabilir, o zaman “erâeyte”nin cevabı hazfedilmiştir (“bana haber ver, hesabı yalanlayan ve yetimi inciten hakkında ne dersin?”); Âlûsî Ebû Hayyân’ın bu yola itirazını da aktarır. Kısaca: yetimi itmek yalanlamanın sebebi değil, görünür sonucu ve delilidir (Zemahşerî: “hesabı yalanlamanın alâmeti”).",
    source="RAZI-107|BAYD-107|KASH-107|ALUSI-107")

add(25, id="S107-TAF-006", type="tafsir", tradition="dirayet", ayah="107:5", role="clarification",
    relation="grammatical", status="explicit", confidence="high", priority="core", audience="general",
    scholar="Zamakhshari|Razi|Qurtubi|Tabari|Ibn Kathir|Biqai", term="an salâtihim",
    prose="“Namazlarından” (‘an) ile “namazlarında” (fî) arasındaki fark klasik şerhlerin açıkça işlediği bir noktadır ve baz metnin “an edatı içeride değil, uzakta olmayı bildirir” cümlesinin doğrudan klasik karşılığıdır. Zemahşerî: “‘an’ onların namazdan sehv ettiklerini, onu terk edercesine ve az yönelerek ettiklerini bildirir; bu münafıkların ya da fâsıkların işidir. ‘Fî’ olsaydı şeytan vesvesesi ya da nefis konuşması yüzünden namaz içinde sehv olurdu, ki hiçbir Müslüman bundan neredeyse kurtulmaz; Peygamber’in bile namazda sehvi olmuştur, fakihler bu yüzden sehiv secdesi bâbını yazar.” Enes: “‘fî salâtihim’ dememiş olmasına hamdolsun.” Taberî ve İbn Kesîr aynı sözü Atâ’dan nakleder; Râzî ve Kurtubî İbn Abbas’tan, “fî deseydi bu tehdit müminler hakkında olurdu” sözünü verir. Râzî’ye göre “namazda sehv mümin işi, namazdan sehv kâfir işidir”; ancak o, sehvi “terk” diye açıklayan görüşü, ayet onlara “musallî” dediği için zayıf bulur. Bikâî de ‘an’ın seçilmesini namazın ihmal edilip ziyan edilmesine (tadyî‘) işaret sayar. Maqâyîs sehvi “sehavtü fi’s-salât” (namazda yanıldım) örneğiyle de verir; yani namaz içinde sehv dilde gayet meşrudur, ayet bunu değil ‘an’lı kullanımı seçmiştir.",
    source="KASH-107|RAZI-107|QURT-107|TAB-107|KATH-107|BIQ-107|MAQ-SAHW")

add(25, id="S107-SEM-002", type="semantic_history", tradition="rivayet", ayah="107:5", role="semantic_range",
    relation="direct_tafsir", status="explicit", confidence="high", priority="core", audience="general",
    term="sâhûn", scholar="Tabari|Sa'd b. Abi Waqqas|Masruq|Ibn Abbas|Mujahid|Qatada|Ibn Zayd|Abu l-Aliya|Qutrub|Ibn Kathir",
    prose="“Sâhûn” için erken kaynaklar üç ana dal ve birkaç alt dal verir. (1) Namazı vaktinden geciktirmek: Sa‘d b. Ebî Vakkâs (oğlu Mus‘ab’ın “bu kişinin namazda kendi kendine konuşması mı?” sorusuna “hayır, vaktinden geciktirmesi”), Mesrûk (“vaktini zayi etmek”), Ebu’d-Duhâ, İbn Ebzâ ve İbn Abbas’ın bir rivayeti (Taberî). (2) Terk etmek: İbn Abbas’ın bir başka rivayeti ve Mücâhid (Taberî); İbn Abbas’ın yine bir rivayetinde “ödül ummadan kılar, terk edince azap korkmaz” (Kurtubî). (3) Dalgın ve hafife alan olmak: Mücâhid “lâhûn”, Katâde “gâfil; kıldı mı kılmadı mı umursamaz”, İbn Zeyd “namaz kılarlar ama namaz onların işi değildir” (Taberî). Taberî sehvin “lâhûn: ihmal edip başka şeyle uğraşan” olduğunu, bunun bazen namazı zayi etmeyi, bazen vaktini zayi etmeyi kapsadığını söyleyerek hepsini birleştirir (S107-HAD-001, S107-HAD-002 ile birlikte); aynı kökün Zâriyât 51:11’deki “sâhûn”u da Taberî’de “lâhûn, gaflet” diye geçer. Ebu’l-Âliye “rükû ve secdesini tamamlamayan; çift mi tek mi kıldığını bilmeyen”, Kurtubî’de Kutrub “okumayan, Allah’ı anmayan”, Zemahşerî “gagalar gibi kılan, sakalıyla ve elbisesiyle oynayan, kaç rekât kıldığını bilmeyen”. İbn Kesîr ifadenin hepsini kapsadığını söyler: terk, vaktinden çıkarma, ilk vaktinden geciktirme, rükünlerini ve şartlarını yerine getirmeme, huşu ve tedebbürden uzak olma; bunlardan birini taşıyan herkes ayetten bir pay alır, hepsini taşıyan nifâk-ı ameliyi tamamlar. İbn Mes‘ûd’un “lâhûn” okuyuşu ayrıca kaydedilmiştir (S107-QIR-002).",
    source="TAB-107|TAB-51-11|QURT-107|KASH-107|KATH-107|SUY-107")

add(25, id="S107-HAD-001", type="hadith", tradition="hadith", ayah="107:5", role="early_attestation",
    relation="direct_hadith_tafsir", status="disputed", hadith_grade="not_assessed", connection="direct", confidence="medium",
    priority="core", audience="advanced", transmitter="Sa'd b. Abi Waqqas via Mus'ab b. Sa'd",
    origin="Tabari; compare Ibn Kathir and Suyuti on raf vs waqf",
    prose="Sa‘d b. Ebî Vakkâs’ın “sâhûn” hakkındaki soruya cevabı iki biçimde nakledilir. Mevkûf biçimde Taberî, Mus‘ab’ın babasına “bu kişinin namazda kendi kendine konuşması mıdır?” diye sorduğunu ve Sa‘d’ın “hayır, sehv onu vaktinden geciktirmektir” dediğini verir. Merfû‘ biçimde ise aynı Mus‘ab yoluyla Sa‘d’ın bunu Peygamber’e sorduğu ve “namazı vaktinden geciktirenlerdir” cevabını aldığı rivayet edilir. İbn Kesîr merfû‘ rivayeti Beyhakî’nin zayıf saydığını, mevkûfun senet bakımından daha sahih olduğunu ve Hâkim ile Beyhakî’nin de mevkûfu sahih saydığını söyler; Süyûtî aynı kaydı Hâkim ve Beyhakî’ye bağlar. Dolayısıyla “vaktinden geciktirme” dalının en sağlam erken dayanağı Sa‘d’ın kendi sözüdür; Peygamber tefsiri olarak merfû‘ biçimi tartışmalıdır. Dereceyi bu çalışma bağımsız olarak vermedi; yalnızca eleştirmenlerin ifadeleri kaydedildi.",
    source="TAB-107|KATH-107|SUY-107")

add(25, id="S107-HAD-002", type="hadith", tradition="hadith", ayah="107:5", role="corroboration",
    relation="direct_hadith_tafsir", status="weak", hadith_grade="daif", connection="strong", confidence="medium",
    priority="extended", audience="advanced", transmitter="Abu Barza al-Aslami", origin="Tabari",
    prose="Ebû Berze el-Eslemî’den, ayet inince Peygamber’in “Allahü ekber; bu ayet size, her birinize dünyanın tamamı verilmesinden hayırlıdır” dediği ve ardından sehv edeni “namaz kılarsa hayrını ummayan, bırakırsa Rabbinden korkmayan kişi” diye tarif ettiği rivayet edilir. Taberî’de geçer; İbn Kesîr senedinde zayıf olduğu bilinen Câbir el-Cu‘fî ve adı verilmeyen bir ravi bulunduğunu, Süyûtî ise “zayıf bir senetle” geldiğini söyler. Bu nedenle rivayet “umursamama” dalına geç ve zayıf bir destektir; tek başına dayanak yapılmamıştır.",
    source="TAB-107|KATH-107|SUY-107")

add(25, id="S107-HAD-003", type="hadith", tradition="hadith", ayah="107:5", role="corroboration",
    relation="thematic", status="explicit", hadith_grade="sahih", connection="strong", confidence="medium",
    priority="extended", audience="general", transmitter="Anas b. Malik", origin="Muslim; cited by Ibn Kathir under 107:5",
    note="Grade rests on inclusion in Sahih Muslim; no separate grading performed; numbering 622/623 varies by edition; primary page not opened",
    prose="İbn Kesîr beşinci ayetin yanında münafığın namazını anlatan hadisi verir: “İşte münafığın namazı; güneşi gözler, güneş şeytanın iki boynuzu arasına girince kalkar ve dört (rekât) gagalar, Allah’ı ancak az anar.” Bu hadis ayetin tefsiri değil, tematik bir paraleldir; vaktinden geciktirme, huşusuz kılma ve Allah’ı az anma dallarını birlikte gösterir ve İbn Kesîr bunu “nifâk-ı ameli” için delil yapar. Hadis Sahîh-i Müslim’de Enes’ten, Alâ b. Abdurrahman yoluyla yer alır (kitâbü’l-mesâcid; numara baskıya göre 622 ya da 623 görünür). Derece, Müslim derlemesine girmiş olmasına dayanır; bu çalışmada ayrıca derecelendirme yapılmamıştır.",
    source="MUS-ANAS|KATH-107")

add(25, id="S107-QIR-002", type="qiraat", tradition="rivayet", ayah="107:5", role="clarification",
    relation="lexical", status="reported", priority="research", audience="research", canonical="false",
    note="Companion reading report attributed to Ibn Mas'ud; presented as non-canonical per the attribution in the sources",
    prose="İbn Mes‘ûd’un beşinci ayeti “ellezîne hum an salâtihim lâhûn” diye okuduğu rivayeti Süyûtî’de (İbnü’l-Enbârî, Beyhakî ve Hatîb’e atıfla), Zemahşerî’de, Kurtubî’de ve Bikâî’de geçer. Bu bir mushaf okuyuşu değil, açıklayıcı bir Sahâbe okuyuşu olarak anılır; sehvi “lehv”e, yani oyalanıp ihmal etmeye bağlar ve Taberî’nin “lâhûn” tercihiyle uyumludur. Kanonik sayılan bir okuyuş değildir.",
    source="SUY-107|KASH-107|QURT-107|BIQ-107")

add(25, id="S107-MEAL-003", type="semantic_history", tradition="historical", ayah="107:5", role="constraint",
    relation="grammatical", status="inferred", confidence="medium", priority="core", audience="general",
    term="‘an vs fî", scope="meal-review:an-fi", scholar="Bulaç|Onan|Bilmen|Elmalılı (sadeleştirilmiş)|Ateş|Öztürk|Hayrat|Çantay|Okuyan|Elmalılı (özgün)",
    prose="Meal incelemesi: ‘an edatı. Ayet “namazlarından” (‘an) der; klasik şerhler ‘an ile fî’yi bilerek ayırmıştır (S107-TAF-006). Mealler iki gruba ayrılır. ‘An’ı koruyanlar: Ateş (“namazlarından gaflet ederler”), Hayrat (“namazlarından gaflet edenlerdir”), Çantay (“namazlarından gaafildirler”), Öztürk’ün bir varyantı (“Namazlarından gaflet içindedir”), Okuyan (“salâtlarından habersizdir”) ve Elmalılı’nın özgün metni (“Namazlarından yanılmaktadırlar”). Fî’ye çevirenler: Bulaç ve Onan (“namazlarında yanılgıdadırlar”), Bilmen (“namazlarında yanılanlardır”, kuranmeali.com metni) ve Elmalılı’nın sadeleştirilmiş metni (“namazlarında yanılmaktadırlar”, acikkuran.com metni). Elmalılı’nın özgün metninde ‘an’ korunurken sadeleştirilmiş metinde fî’ye dönmesi, edata ilişkin kaymanın bir yayın/sadeleştirme sonucu olabileceğini gösterir. Değerlendirme: ‘namazlarında yanılmak’ ifadesi sehvi namazın içine yerleştirir; Zemahşerî’ye, Enes’e, Atâ’ya ve İbn Abbas’a göre bu, ayetin seçmediği ve sıradan müminlerin yanılgısını anlatan öbür anlamdır (“fî deseydi tehdit müminlere olurdu”, Râzî ve Kurtubî). Bu yüzden fî’li çeviriler edat bakımından yanıltıcıdır; çevirmenin niyeti Türkçedeki “yanılmak”la gündelik sehivleri kastetmek olabilir, ancak ayetteki veyl tehdidi o anlamla uyuşmaz. “Namazlarını ciddiye almazlar” (güncel Diyanet) ve “namazlarını unuturlar” (Gölpınarlı) gibi nesne yapıları edatı hiç göstermez ama uzaklık/ihmal anlamını korur.",
    source="MEAL-BUL-107|MEAL-ONAN-107|MEAL-BIL-107|MEAL-ELM-107|MEAL-ATE-107|MEAL-HAY-107|MEAL-CAN-107|MEAL-YNO-107|MEAL-OKU-107|MEAL-DIY-107|MEAL-GOL-107|KASH-107|RAZI-107|QURT-107|TAB-107")

add(25, id="S107-MEAL-004", type="semantic_history", tradition="historical", ayah="107:5", role="semantic_range",
    relation="comparative", status="interpretive", confidence="medium", priority="core", audience="general",
    term="sâhûn", scope="meal-review:sâhûn", scholar="Diyanet (güncel ve eski)|Okuyan|Esed|İslamoğlu|Süleymaniye Vakfı|Ateş|Hayrat",
    prose="Meal incelemesi: “sâhûn”un karşılığı. Güncel Diyanet meali “namazlarını ciddiye almazlar” der; eski Diyanet metni “kıldıkları namazdan gafildirler” demişti. Yeni ifade klasik aralığın “umursamama/hafife alma” koluna oturur (Zemahşerî ve Beyzâvî: “kıllet-i mübâlât/gayr-i mübâlîn”, Katâde: “kıldı mı kılmadı mı umursamaz”, Taberî’nin “lâhûn”u); dolayısıyla savunulabilir bir daraltmadır. Kaybolan şeyler sehv/gaflet sözcüğünün kendisi ve klasik rivayetlerde en sağlam dayanağı olan vakit geciktirme kolu (Sa‘d, Mesrûk, İbn Abbas’ın Ebû Cemre rivayeti). Okuyan “habersizdir” ile gaflet kolunu korur, ancak “(yaptıklarını sandığı)” parantezi, onların yaptığının gerçekte salât olmadığı çıkarımını ekler; bu çıkarım İbn Zeyd’in “namaz kılarlar ama namaz onların işi değildir” sözüyle kısmen örtüşür (Taberî), başka erken dayanağı kontrol edilen kaynaklarda bulunmadı. Esed’in “kalpleri namazlarına yabancıdır” ifadesi Maqâyîs’in “sehv: kalbin ondan gitmesi” tanımına ve Taberî’nin lehv anlayışına en yakın karşılıktır. İslamoğlu “ibadetin hakiki amacından gafil görünmektedirler” der: “hakiki amaç” İbn Kesîr’in huşû ve tedebbür koluna uyar, “görünmek” ise Arapçada olmayan bir görünüş kaydıdır. Süleymaniye Vakfı’nın metni “önemsemeyenlerdir” (acikkuran.com) ve “akılları başka yerde olanlardır” (kuranmeali.com) diye iki biçimde görünür. Kontrol edilen yaklaşık elli meal satırında vakit geciktirme kolunu gösteren bir ifade görülmedi; bu, en erken ve en iyi belgelenmiş dalın meallerde hiç temsil edilmemesi demektir.",
    source="MEAL-DIY-107|MEAL-DIYOLD-107|MEAL-OKU-107|MEAL-ESED-107|MEAL-ISL-107|MEAL-SUL-107|KASH-107|BAYD-107|TAB-107|KATH-107|MAQ-SAHW")

add(25, id="S107-REJ-001", type="method_note", tradition="project", ayah="107:5", role="rejected_candidate",
    relation="grammatical", status="interpretive", connection="rejected", priority="research", audience="research",
    reason="Klasik şerhler ‘an ile fî’yi ayırır; ‘fî’ okuması öbür (sıradan sehiv) anlamdır.",
    prose="Aday: “‘an salâtihim” ifadesini “namazlarında” diye, yani namaz içindeki gündelik yanılgı olarak çevirmek. İncelendi ve reddedildi. Dayanak: Zemahşerî, Enes, Atâ, İbn Abbas (Râzî ve Kurtubî’de) ve Bikâî’nin ‘an’ vurgusu; fî ile sehv sıradan müminin başına gelen ve sehiv secdesiyle giderilen şeydir (S107-TAF-006). Dil bakımından fî’li kullanım mümkündür (Maqâyîs: “sehavtü fi’s-salât”) ama ayet bu kullanımı seçmemiştir.",
    source="KASH-107|RAZI-107|QURT-107|BIQ-107|MAQ-SAHW")

add(25, id="S107-MET-002", type="method_note", tradition="project", ayah="107:5", role="constraint",
    relation="grammatical", status="interpretive", confidence="medium", priority="extended", audience="advanced",
    prose="Baz metindeki “Bu surenin adamları namazı kılarken namazın dışındadır” cümlesi ‘an’ okumasının tek bir dalını görselleştirir: ihmal ve gaflet (lâhûn) kolu. Klasik aralıkta aynı ifade vaktinden geciktirme (Sa‘d, Mesrûk), terk, hafife alma ve huşusuzluk (İbn Kesîr) dallarını da kapsar (S107-SEM-002). Baz metnin bu ifadesi aralığı dışlamaz; ancak okur onu ayetin tek klasik anlamı sanmamalıdır. Bu not baz metni değiştirmez.",
    source="TAB-107|KATH-107|KASH-107")

add(27, id="S107-NOV-013", type="novelty", tradition="project", ayah="107:2|107:5|107:7", role="novelty_assessment",
    relation="thematic", status="interpretive", connection="resonant", classical_attestation="none_found_in_checked_sources",
    checked_sources="Tabari|IbnKathir|Suyuti|Zamakhshari|Razi|Baydawi|Biqai|Qurtubi|Alusi(107:1,107:7)",
    confidence="medium", priority="research", audience="research",
    prose="Bu bölümün “yüzey ile alt” sahneleri (Bakara 2:264 kayası, Münâfikûn 63:4 kütükleri, Bakara 2:177 birr ayeti, Necm 53:33-34, Meâric 70:23 ve 70:34, Beyyine 98:5) kontrol edilen 107. sûre tefsir sayfalarında bu sûreyle ilişkilendirilmiş olarak bulunmadı. Taranan kaynaklarda açık bir paralel görülmedi; bu, başka klasik eserlerde bulunamayacağı anlamına gelmez. Bu paraleller proje sentezi olarak okunmalıdır.",
    source="BASE-LEX")
