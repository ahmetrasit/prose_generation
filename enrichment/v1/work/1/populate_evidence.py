import json
from datetime import datetime, timezone
from pathlib import Path

W = Path(__file__).resolve().parent
source_scopes = {
 'TAB1': 'Taberî 1:1, yerel metin satırları 22–26, 64–87, 91–109; 98. satır ortak rızık, bulut, yağmur, bitki.',
 'TAB2': 'Taberî 1:2, satırlar 1–11 ve 29–62; hamd, Rabb ve âlemler.',
 'TAB3': 'Taberî 1:3, metnin bütünü; besmeleyi Fatiha ayeti saymayan görüş ve tekrar tartışması; dipnot müellif değil editör.',
 'TAB4': 'Taberî 1:4, satırlar 3–17 ve 35–56; melik tercihi, dîn karşılık ve borç verme benzetmeli şiir.',
 'TAB5': 'Taberî 1:5, satırlar 1–32; kulluk, çiğnenmiş yol, uysal binek, yardım ve zamir düzeni.',
 'TAB6': 'Taberî 1:6, ana tefsir pasajının bütünü; sebat/tevfik; açık yol; İslam/Kur’an yorumları; gelin/hediye/ahiret yorumunu aktarıp birincil anlam olarak reddetmesi. Dipnotların tamamı denetlenmedi.',
 'TAB7': 'Taberî 1:7, yerel 25.625 karakterlik metnin bütünü; 4:69, ghayr dilbilgisi, gazap görüşleri, Adiyy rivayeti ve iki grubun ortak kusurları.',
 'TAB1223': 'Taberî 12:23, web ana metni özellikle 88–105. satırlar; rabbî = kadının kocası/efendi yorumu.',
 'IK1': 'İbn Kesîr 1:1, satırlar 1–22; adlar, Mekkî/Medenî/iki kez nüzul, ayet sayımı, ilk vahiy ayrımı ve fazilet rivayetleri. 23–101 denetlenmedi.',
 'IK2': 'İbn Kesîr 1:2, 38 satırlık metnin bütünü; hamd–şükür boyutları, âlemler ve sayısal rivayetlere ihtiyat.',
 'IK4': 'İbn Kesîr 1:4, 10 satırın bütünü; iki kanonik okuyuş, Mervan iddiasının eleştirisi, hesap/af.',
 'IK5': 'İbn Kesîr 1:5, 12 satırın bütünü; yol/deve, hasr, iltifat, cemaat ve yardım.',
 'IK6': 'İbn Kesîr 1:6, 23 satırın bütünü; irşat/tevfik, yol yorumları, Nevvâs temsili, devam eden hidayet.',
 'IK7': 'İbn Kesîr 1:7, satırlar 1–21; nimetliler, Adiyy, açıklayıcı farklı okuyuş, ahiret sıratı ve etkin nimet/pasif gazap. 22–31 denetlenmedi.',
 'IK676': 'İbn Kesîr 6:76, web metninin bütünü; kaybolmayan ve sürekli Rabb gerekçesi.',
 'IK679': 'İbn Kesîr 6:79, web 19–28; nazar/araştırma ile münazara yorumlarının ayrımı ve münazara tercihi.',
 'ZAM1': 'Zemahşerî 1:1, sunulan 16 satırın bütünü; sayım, fiil takdiri, ism, Allah ve rahmet/rahim.',
 'ZAM2': 'Zemahşerî 1:2, sunulan 8 satırın bütünü; hamd–şükür, Rabb ve âlem.',
 'ZAM4': 'Zemahşerî 1:4, sunulan 4 satırın bütünü; mâlik/melik ve kanonik olmayan ek biçimler.',
 'ZAM5': 'Zemahşerî 1:5, sunulan 8 satırın bütünü; koyu/dokulu kumaş örneği, hasr, iltifat, ibadet→yardım→hidayet.',
 'ZAM6': 'Zemahşerî 1:6, sunulan 3 satırın bütünü; devam/artış, yutma mecazı, s/ṣ/işmam.',
 'ZAM7': 'Zemahşerî 1:7, sunulan 12 satırın bütünü; tekrar/bedel, topluluk referentleri ve gazap yorumu.',
 'BAY1': 'Beyzâvî 1:1, sunulan 20 satırın bütünü; sayım, Mekkî gerekçesi, ism etimolojileri ve rahmet.',
 'BAY2': 'Beyzâvî 1:2, sunulan 6 satırın bütünü; hamd–şükür, tedricî terbiye, âlem.',
 'BAY4': 'Beyzâvî 1:4, sunulan 4 satırın bütünü; okuyuş, sahiplik/hükümranlık.',
 'BAY5': 'Beyzâvî 1:5, sunulan 11 satırın bütünü; yol/kumaş, iltifat/çoğul, gerekli/isteğe bağlı yardım ve binek örneği.',
 'BAY6': 'Beyzâvî 1:6, sunulan 8 satırın bütünü; sürü öncüleri, dört hidayet düzeyi, yutma kökeni.',
 'BAY7': 'Beyzâvî 1:7, sunulan 18 satırın bütünü; iman/bağışlama nimeti, kusur tipleri, gazap.',
 'DUR1': 'Süyûtî ed-Dürr 1:1, satırlar 1–17; nüzul görüşleri ve Ebû Meysere anlatısı. 18–165 denetlenmedi.',
 'DUR2': 'Süyûtî 1:2, satırlar 1–18 ve 36–44; hamd ve Müslim 223 aktarımı; aradaki 19–35 denetlenmedi.',
 'DUR3': 'Süyûtî 1:3, sunulan 3 satırın bütünü; Katâde sure açıklaması ve Ümmü Seleme sayım rivayeti. Bu rivayetler ayrıca derecelendirilmedi.',
 'DUR4': 'Süyûtî 1:4, sunulan 22 satırın bütünü; çelişen okuyuş nispetleri, hesap ve Âişe yağmur duası; Ebû Dâvûd 1173 ayrıca asıl yerinden doğrulandı.',
 'DUR5': 'Süyûtî 1:5, sunulan 5 satırın bütünü; yardım bütün işler ve farklı telaffuz/seriyye rivayetleri. Bunların dereceleri değerlendirilmedi.',
 'DUR6': 'Süyûtî 1:6, sunulan 24 satırın bütünü; yol yorumları, Nevvâs, telaffuzlar.',
 'DUR7': 'Süyûtî 1:7, satırlar 1–15; açıklayıcı okuyuşlar ve grup referentleri; 16–51 denetlenmedi.',
 'BIQ1': 'Bikâî 1:1, ana metin satırlar 1–9; maksat, besmele ve sure düzeni. Kalan notların tamamı denetlenmedi.',
 'BIQ2': 'Bikâî 1:2, sunulan 13 satırın bütünü; hamd, malikiyet ve iyilik.',
 'BIQ3': 'Bikâî 1:3, sunulan 7 satırın bütünü; tekrarda anlam gelişimi.',
 'BIQ4': 'Bikâî 1:4, sunulan 35 satırın bütünü; rahmet/hesap, ümit/korku; dijital ayet numaraları ayrıca Kur’an ile kontrol edildi.',
 'BIQ5': 'Bikâî 1:5, ana metin satırlar 1–3; iltifat, yardım ve Harâllî’den cemaat. 4–48 denetlenmedi.',
 'BIQ6': 'Bikâî 1:6, sunulan 18 satırın bütünü; yumuşak sevk ve hidayet; 93:7 numarası dijital aktarımda kaymış.',
 'BIQ7': 'Bikâî 1:7, ana metin satırlar 1–8; yolculuk, vadiler/denizler, iyi yol ve iyi arkadaş, sure bütünü. 9–117 denetlenmedi.',
 'RAZ_SCOPE': 'Râzî sayfa 1:1–6 sunulan giriş kısımları ve 1:7 sunulan 81 satırın bütünü; 1:7 de giriş/dil felsefesi. Bunlar ayetlerin tam Fatiha şerhi olarak sayılamaz; basılı tam cilt denetlenmedi.',
 'W_ASB': 'Vâhidî Esbâb, Fatiha bölümü, İslamweb ana metin 575–582, rapor 19–22 ve Mekkî/Medenî tartışması; Ebû Meysere zincirinde sahabî adı yok.',
 'NASHR': 'İbnü’l-Cezerî en-Neşr, cilt 1 basılı s.271–272 (ABL sayfaları 279–280), okuyucu/râvi/tarîk ayrımları. Basılı nüshayla görüntü kolasyonu yapılmadı.',
 'THD3_10': 'Ezherî Tehzîb, ABL cilt 3, s.10; sunulan ana metnin tamamı: iyilik/tamamlama, nimetli çocuk, güney rüzgârı, kuyu kirişleri ve qâma = makara; matbu kolasyonu yapılmadı.',
 'PKT': 'Projenin sözlük paketi: dictionary.md q-w-m satırları 341–394 tamamen okundu; diğer seçilmiş dallar base/ledger ile denetlendi. Bu kayıt, başvurulan antik kitapların tüm maddelerinin bağımsız kontrol edildiği anlamına gelmez.',
 'QUR': 'Tanzil resmî Uthmani 1.1 metni; base içindeki 169 farklı atfın tam ayetleri okundu ve 205 arapça atıf denetlendi; iki fark yalnız hamza/tatvil yazımı.',
}
for r in ['ABD','ALH','ALM','DLL','DYN','GHDB','GHYR','HDY','HMD','MLK','NAAM','QWM','RBB','RHM','SMW','SRT','WSM','YWM']:
 source_scopes['M_'+r] = f'İbn Fâris Mekâyîs, {r} kökünün Hawramani dictionary_7 asıl metin maddesi bütünü; matbu nüsha kolasyonu yapılmadı.'
hadith = {
 'H_M395': ('https://sunnah.com/muslim:395a','58–62','sahih','Sahîh Müslim koleksiyonu','direct_hadith_tafsir'),
 'H_B4474': ('https://sunnah.com/bukhari:4474','64–68','sahih','Sahîh Buhârî koleksiyonu','direct_hadith_tafsir'),
 'H_T2954': ('https://sunnah.com/tirmidhi:2954','58–64','hasan','Sayfada Darussalam','direct_hadith_tafsir'),
 'H_B5999': ('https://sunnah.com/bukhari:5999','66–69','sahih','Sahîh Buhârî koleksiyonu','thematic'),
 'H_B5988': ('https://sunnah.com/bukhari:5988','66–69','sahih','Sahîh Buhârî koleksiyonu','thematic'),
 'H_M2747': ('https://sunnah.com/muslim:2747a','58–61','sahih','Sahîh Müslim koleksiyonu','thematic'),
 'H_T2859': ('https://sunnah.com/tirmidhi:2859','58–62','hasan','Müellif Tirmizî: hasen garîb; Darussalam aynı sayfada sahih','thematic'),
 'H_M223': ('https://sunnah.com/muslim:223','58–61','sahih','Sahîh Müslim koleksiyonu','thematic'),
 'H_AD1173': ('https://sunnah.com/abudawud:1173','64–75','hasan','Sayfada Elbânî: hasen; müellif: isnâduhu ceyyid','thematic'),
 'H_B3': ('https://sunnah.com/bukhari:3','66–74','sahih','Sahîh Buhârî koleksiyonu','historical'),
}
for sid,(url,ranges,grade,authority,relation) in hadith.items():
 source_scopes[sid] = f'{url} Arapça matın, isnat, numara ve gösterilen derece alanı doğrudan okundu; web satırları {ranges}; {authority}; ilişki {relation}.'

# Each assessment attaches inspected evidence to a specific original paragraph,
# rather than treating a whole-surah bibliography as a lexical-network search.
spec = {
3:('TAB5 IK5 M_ABD','explicit','Çiğnenmiş yol ve uysal binek doğrudan 1:5 tefsirinde var; 1:6 bağlantısı sureler arası terkiptir.'),
5:('TAB6 IK6 BAY6 M_HDY','partial','Öncülük/sebat açık tefsir; hediye/gelin ayrı Mekâyîs aslı. Taberî ikincisini aktararak birincil hidayet yorumu olarak reddeder.'),
7:('TAB6 ZAM6 BAY6 NASHR M_QWM M_SRT','explicit','Düz yol ve yutma klasik; saf zāy lehçesi ile kanonik işmam aynı ses değildir.'),
9:('TAB6 TAB7 IK5 BAY5 BIQ7 QUR','explicit','Devam eden itaat ve nimetli öncüler açık; çoğulun cemaat yorumu açık.'),
11:('ZAM2 IK2 TAB4 M_ALM M_MLK M_DYN','building_blocks_only','İşaret/âlem tefsiri var; yol ortası sahiplik ve âdetin aynı sahneye taşınması proje. Mekâyîs dîn-âdet şiirinin zabtını tartışır.'),
13:('M_ABD M_QWM M_NAAM M_DLL PKT TAB6 TAB7','building_blocks_only','Dağılma ve evini bulamama sözlük malzemesi; qawm Mekâyîs’te diklikten ayrı asıl. Bütün zıtlık ağını Fatiha tercümesi sayma.'),
15:('QUR TAB6 IK6','partial','Ayetler yol ve yol ayrımını doğrudan söyler; ayrı kıssaların tek mekânsal sahne olması yorumdur.'),
17:('QUR BIQ6 TAB6 IK6','partial','37:23 cehenneme sevk, hidayetin yalın fiil olarak her bağlamda kurtuluş olmadığını gösterir; 93:7 dalâl ahlaki sapıklık diye zorlanmaz.'),
23:('TAB5 IK5 M_ABD','explicit','Yol–uysal deve–kul bağlantısı tefsirde açık. Mekâyîs yumuşaklık ile kuvveti iki asıl sayar.'),
25:('TAB1 TAB2 BAY1 BAY2 M_ALH M_MLK M_RBB','explicit','Rab efendi/sahip/ıslah eden; Mekâyîs a-l-h ibadet aslı görülmüş olmakla birlikte Allah etimolojisinde tefsirin çıkarsama ve ihtilafı korunmalı.'),
27:('TAB4 M_DYN','partial','Dîn bağlamsal hesap/karşılık; aynı aile itaat ve borç anlamı içerir, bu tek kelime özdeşliği değildir.'),
29:('TAB5 ZAM5 BAY5 IK5','explicit','İltifat, hasr ve kulluk açık klasik yorum; gramer tek başına kulun tüm hayat psikolojisini belirlemez.'),
31:('QUR TAB5 IK5 M_ABD PKT','building_blocks_only','19:93 tümünün abd olarak gelişi açık; konuk ağırlama nadir paket dalı, ayetin bağımsız anlamı değil.'),
33:('QUR TAB1223 M_RBB','partial','İnsan efendi yorumu Taberî 12:23’te açık; 3:64 ve 26:22 insanı rab/köle kılma karşısında sınır koyar.'),
39:('TAB4 IK4 M_DYN QUR','explicit','Hesap/karşılık açık; bağışlama istisnası korunur.'),
41:('TAB4 IK4 NASHR M_YWM M_MLK','partial','Mâlik/melik iki kanonik okuyuş; olay günü sözlük menzili, her olay günü ahiret değildir.'),
43:('TAB7 ZAM7 BAY7 M_QWM M_GHDB QUR','partial','Gazap=ceza belirli kelami yorum; Taberî alternatifleri de verir. Qiyâma/istikamet akraba biçimler, ayette kayyûm yok.'),
45:('TAB4 M_DYN M_QWM M_MLK PKT','partial','Taberî karşılıklı borç şiiri kullanır; dîn/dayn ayrı lafızlar. Eksiksiz dinar yalnız paket düzeyinde denetlendi.'),
47:('M_GHYR M_DLL QUR PKT','building_blocks_only','Mekâyîs ghayr iki asıl, 1:7 farklılık altındadır; diyetin hangi asla ait olduğu bile tartışmalı.'),
49:('TAB4 M_DYN M_QWM H_M223 QUR','partial','Karşılık-borç klasik öncül, değer/diklik sözlük; Fatiha tartı demiyor. Terazi Kur’an intertekstidir.'),
51:('QUR TAB4 IK4','explicit','Yevmüddîn, hüküm ve tartı için ayrı ayetler açık; tümünü bir kök anlamına katmak ayrı adım.'),
53:('QUR M_DYN M_QWM M_DLL','partial','2:282 borç sözleşmesi/tanık unutması ve aqwam tanıklık, bağlamı dini sapıklık veya fiziksel diklik değil.'),
59:('ZAM1 BAY1 M_RHM H_B5999 H_B5988','partial','Rahim bağlantısı ve ilahi merhameti insani değişimden ayırma klasik. Anatomik ev çerçevesi proje.'),
61:('TAB2 BAY2 M_RBB QUR','partial','Terbiye/tamamlama klasik; rabbayâni ayrı r-b-w ailesi, ses/anlam yakınlığı kök özdeşliği değil.'),
63:('TAB3 BIQ1 BIQ3 M_RHM M_RBB M_GHYR M_QWM M_NAAM','building_blocks_only','Besmele sayımı koşulu altında çifte rahmet nazmı; ghayr erzak/kıskançlık 1:7 farklılık aslına taşınamaz.'),
65:('QUR M_RHM M_RBB','partial','İbadet–annebaba–rahmet aynı pasajda açık; iki terbiye kökünü özdeşleştirmiyor.'),
67:('QUR M_RBB','partial','Musa’nın annesine dönüşü ve Firavun iddiası metinle doğrulandı; dramatik tek ev sahnesi projeye ait.'),
73:('M_NAAM TAB2 BAY2 TAB7 BAY7','partial','Genel lütuf ve Rabb’in tamamlama yorumu var; 1:7 nimetler dünyevi refahtan ziyade dini doğru yolla ayrılır.'),
75:('TAB2 IK2 ZAM2 BAY2 M_HMD','explicit','Hamd yalnız nimet için değildir, şükür beden/kalp/dil ile olabilir; kapsam tek boyutlu hiyerarşi olamaz.'),
77:('TAB7 BIQ2 BIQ3 BIQ7 H_M395','partial','Övgüden ihtiyaç duasına sıra klasik; nimetlerin tamamlama yolculuğu bir proje terkibi.'),
79:('QUR TAB7 BAY7','explicit','Nimet/hidayet/tamamlama intertekstleri mevcut; bağlamları iman, hac yönü, öğreti ve ahirette farklı.'),
85:('TAB7 IK7 ZAM7 BAY7 H_T2954','explicit','Etkin nimet/pasif gazap açık klasik; Yahudi/Hristiyan örneklemesi aktarılır, dondurulmuş etnik kelime tanımı değildir.'),
87:('M_GHDB M_NAAM ZAM1 BAY1','building_blocks_only','İnsani gazabın yüz/beden imgeleri; ilahi gazap sahibine aynı bedensel değişimi isnat etmez.'),
89:('QUR TAB7 IK7 M_GHDB M_NAAM','building_blocks_only','Öfkelenen öznenin kızarması gazaba uğrayanın kızarmasını gerektirmez; kıyamet yüzleri ayrı ayetlerden.'),
91:('QUR TAB7 IK7','partial','20:81 iniş/çöküş açık; 1:7 alayhim grameri literal yukarıdan aşağı hareketi zorunlu kılmaz.'),
93:('QUR TAB7 IK7 BIQ7','explicit','4:69 arkadaş/öncü ve nimet sahipleri açık; yüzleri yine ayrı eskatolojik pasajlar açıklıyor.'),
99:('ZAM1 BAY1 M_SMW M_WSM','partial','Basra sumuv/Kufe vesm rakip etimolojiler; Beyzâvî ikinciyi sarf bakımından reddeder. İkisini eşzamanlı kesin kök yapma.'),
101:('ZAM2 BAY2 IK2 M_ALM','explicit','Âlemin yaratıcı işareti oluşu açık klasik; çoğulun kapsamı konusunda türler/akıllılar alternatifleri var.'),
103:('TAB1 ZAM1 BAY1 ZAM2 M_SMW M_WSM M_ALM','building_blocks_only','Ad/işaret karşılaştırması klasik malzeme; tüm çağrışımları isimde eşzamanlı anlam diye sunma. İsm-i a‘zam rivayeti derecelendirilmedi.'),
105:('QUR ZAM1 BAY1','partial','Ad/yükseklik/çağrı ayetleri doğrudan; 12:40 adları reddeder, bu isim kelimesinin tüm dallarını onaylamaz.'),
107:('QUR TAB1 ZAM1 M_WSM','partial','Basmala iş başında ve mektupta açık; vesm örnekleri alternatif etimolojinin katı ispatı değil.'),
113:('M_YWM M_SMW M_NAAM M_ALM PKT','building_blocks_only','Gök/hilal/işaret malzemesi; q-w-m öğle ve eksiksiz sıfır gölge bağıntısı asıl kitaptan bağımsız denetlenmedi.'),
115:('PKT QUR ZAM1 BAY1 M_ALH','not_checked','Paket kaada gölge için yaklaşık söyleyiş; her öğlen/yerde gölgesizlik çıkmaz. Güneş adı Mekâyîs a-l-h tam maddesinde doğrulandı; bunun bütün Fatiha gök/terazi terkibi için kaynak taraması yapılmadı.'),
117:('QUR IK676 IK679','partial','İbrahim nazar/münazara ihtilafı var; bu kesin tarihsel çoktanrıcılık evresi diye kurulamaz.'),
123:('TAB1 M_RBB M_SMW M_WSM M_NAAM','partial','Taberî Rahman/Rahim yorumunda bulut–yağmur–bitki–ortak rızkı zaten birlikte anar.'),
125:('TAB1 M_RBB M_GHYR M_NAAM M_HMD','partial','Yağmur/bitki klasik öncül; ghayr ilk aslı ile 1:7 ikinci aslı ayrıdır. H-m-d toprak dalı paket düzeyindedir.'),
127:('M_ALM M_NAAM M_MLK M_QWM THD3_10','building_blocks_only','Mekâyîs ay̆lam için alternatif toplama etimolojisini mümkün sayar; Tehzîb kuyu kiriş/makara maddi terimlerini doğrular; Fatiha bağlamı bunları söylemez.'),
129:('TAB1 DUR4 H_AD1173 M_RBB M_MLK M_NAAM THD3_10','partial','Rahmet/rızık ve yağmur duası öncülleri var; susuz yolcu/kuyu makarasının Fatiha terkibi için tam klasik arama yapılmadı.'),
131:('QUR TAB1 H_AD1173','explicit','Yağmur, rahmet, hamd ve diriliş aynı seçilen ayetlerde açık; Fatihanın tüm sözlerini yağmura çevirmiyor.'),
133:('QUR THD3_10 M_MLK','partial','Medyen ayeti su yerini söyler, qâma/naama makara düzenini veya Musa’nın kullanmasını söylemez.'),
139:('M_RBB M_MLK M_NAAM M_WSM M_HDY BAY6','partial','Sürü öncüsü Bayzavi hidayet açıklamasında açık; geniş damga/süt/mera birleşimi ayrı sözlük malzemesi.'),
141:('M_DLL M_RBB M_NAAM H_M2747 PKT','building_blocks_only','Rabrab Mekâyîs’te istisna/belirsiz kıyas; kayıp deve temsili sahih tövbe hadisinde, doğrudan Fatiha tefsiri değil.'),
143:('BAY6 M_HDY M_DLL TAB6','partial','İhdina sürü öncülüğü kısmi klasik öncüllü; dâllin bağlamda dini sapma, ayette deve yok.'),
145:('QUR BAY6 M_HDY','partial','16:5–9 sürüden yol sözüne geçer; 7:179 sebebi anlama/görme/işitme, sahibi tanıma kıyasını açık söylemez.'),
151:('M_HDY M_ABD M_QWM PKT','building_blocks_only','Mekâyîs h-d-y iki yardımcı arasına yaslanma örneği var; h-d-ʾ/h-d-d ayrı kök. Bineğin durması ayağa kalkmayla aynı hareket değil.'),
153:('TAB5 BAY5 ZAM5 M_ABD M_QWM M_MLK M_HDY','partial','Yardımın sebep/potansiyel/binek düzeyi klasik; ʿabd kuvvet aslı itaat aslından ayrı.'),
155:('TAB5 TAB6 ZAM5 ZAM6 BAY5 BAY6 M_HDY','partial','Yardım→hidayet sırası klasik açıklanır; yorgun yolcunun omuzla doğrultulması proje terkibi.'),
157:('QUR M_QWM M_MLK','partial','Duvarı doğrultma/güçle yardım/aşağı yüzüyle yürüme ayrı kıssalar, ortak anatomik Fatiha anlamı değil.'),
163:('M_SRT M_DLL ZAM6 BAY6','partial','Yolu yutma ve yolcuda gözden kaybolma ayrı klasik açıklamalar; süt/kayıp/burial d-l-l diğer bağlamlar.'),
165:('M_SRT M_DLL TAB6 IK6','building_blocks_only','İki kayboluşun biri varışlı diye karşıt sahne yapılması proje; Fatiha dua olarak hak yola yönelmeyi ister.'),
167:('QUR M_DLL TAB6','partial','32:10 ölüm/diriliş inkârı ve 20:52 ilahi bilgiden kayıp ayrı bağlam; dâllin lafzıyla tek ahlaki anlam değildir.'),
173:('M_HDY M_NAAM M_WSM QUR','partial','Kurbanlık sevki Mekâyîs dostça gönderme aslı ve Hac ayetleri; bu bütün hidayetin sözlükte Harem’e taşıma anlamında olduğu demek değil.'),
175:('M_HDY M_MLK M_RBB TAB6 QUR','partial','Gelin/hediye Taberî’de doğrudan tartışılıp birincil Fatiha anlamı reddedilir; güvenli yere ulaştırma 9:6 ayrı lafızdır.'),
177:('TAB6 IK7 M_HDY','partial','Eve/cennete varış önerisinin klasik öncülü var ve Taberî onu reddeder. İbn Kesîr dini hidayet→ahiret sıratı bağlantısı yapar. Türkçe yöneltme varışı zorunlu olarak dışlamaz.'),
179:('QUR M_HDY TAB6','partial','Hediye reddinin açık gerekçesi ilahi nimetin üstünlüğü; rakip/dost psikolojisi ek çıkarım. Bütün kurban ve hediye yolları tek ev olamaz.'),
185:('TAB5 IK5 QUR M_ABD','explicit','Kulluk–yol açık klasik ve 36:61 doğrudan ayet; sonraki ağların tümünü onaylamıyor.'),
187:('BAY6 M_HDY M_NAAM QUR','partial','Sürü/yol/kurban birlikte proje, hidayet öncülüğü klasik. 16:9 iki Türkçe gloss eşdeğer bağlam açıklaması, kanonik okuyuş farkı değil.'),
189:('QUR M_RBB M_RHM ZAM1 BAY2','building_blocks_only','Musa’daki beş kök buluşması işaretlenebilir; alıntıların ayrı köklerini veya ayetin söylediği sınırı kaldırmaz.'),
191:('QUR TAB7 IK7 M_QWM M_GHDB','building_blocks_only','20:81 kesin helak/düşüş, tökezleme fiziksel teşbih; 67:22 figürü bunu Fatiha’ya kelime anlamı olarak eklemiyor.'),
193:('QUR M_DYN M_DLL M_QWM PKT','building_blocks_only','Borç kaydı ve ölçü–kalkış intertekst güçlü; yazma/anımsama/öğle tek mecaz bütünü proje, eksiksiz klasik audit yapılmadı.'),
195:('QUR THD3_10 M_NAAM M_MLK','building_blocks_only','Musa su yerinde su verir; kiriş/makara ve sonraki hesap sırası ayrı malzemeler, tarihsel cihaz kullanım kanıtı değil.'),
197:('QUR IK676 IK679 M_SMW M_ALM','partial','Yaratıcı/işaret ayrımı klasik; İbrahim yorum ihtilafının bir tarafı tarihsel olgu yapılamaz.'),
199:('TAB5 TAB6 TAB7 BIQ1 BIQ7 H_M395 M_HDY M_RBB M_NAAM','partial','Sure sırası/yolculuk/iyi refik klasik; ad→gök→kuyu→sürü→rahim→evin bütün dallarını eşzamanlı anlamsal akış yapma proje terkibi, tam kaynak yokluğu iddiası yok.'),
}
contradictions = {
5:['TAB6'],7:['NASHR'],11:['M_DYN'],13:['M_QWM'],23:['M_ABD'],43:['TAB7'],47:['M_GHYR'],49:['QUR'],53:['QUR'],61:['QUR'],63:['TAB3','M_GHYR'],75:['IK2','ZAM2','BAY2'],85:['TAB7','IK7'],87:['ZAM1','BAY1'],89:['QUR'],91:['QUR'],99:['BAY1'],103:['BAY1'],115:['PKT'],117:['IK679'],125:['M_GHYR'],127:['M_ALM'],133:['QUR'],141:['M_RBB'],143:['TAB6'],145:['QUR'],151:['M_ABD','M_HDY'],153:['M_ABD'],175:['TAB6'],177:['TAB6'],179:['QUR'],187:['QUR'],191:['QUR'],193:['PKT'],195:['QUR'],197:['IK679']}

claims = json.loads((W/'claim_map.json').read_text())['claims']
assert set(spec) == {r['base_line'] for r in claims}
rows = []
for r in claims:
 ids, novelty, assessment = spec[r['base_line']]
 checked = ids.split()
 support = [dict(source=s,actually_checked_passage=source_scopes[s]) for s in checked]
 rows.append(dict(claim_id=r['id'],base_line=r['base_line'],claims=r['claims'],quran_refs=r['quran_refs'],lexical_branches=r['lexical_branches'],supporting_sources=support,contradicting_sources=[dict(source=s,actually_checked_passage=source_scopes[s]) for s in contradictions.get(r['base_line'],[])],early_attestation=[s for s in checked if s.startswith(('TAB','M_'))],later_development=[s for s in checked if s.startswith(('IK','ZAM','BAY','BIQ','DUR'))],hadith_relation=[dict(source=s,relation=hadith[s][-1],grade=hadith[s][2],grade_authority=hadith[s][3]) for s in checked if s in hadith],historical_context='Lexical material is evidence of attested usage or an author’s derivational explanation; not documentary proof of a specific event. No fixed date/occasion is inferred from root meanings.',novelty_status=novelty,assessment=assessment,confidence='high for quoted lexical/contextual observations; medium or low for the project recombination',retrieval_state='inspected_positive_passages; non-exhaustive connection-level comparison',scope_limit='Named inspected passages only. Razi complete Fatiha and uninspected portions are not_checked. Rare packet-only items are not independently primary-verified; no absence claim.'))
matrix = dict(stage='evidence_populated_before_annotation_composition',annotations_composed=False,created_at=datetime.now(timezone.utc).isoformat(),all_major_base_prose_claims=len(rows),source_passage_inventory=source_scopes,hadith_checked={s:dict(url=x[0],web_lines=x[1],grade=x[2],grade_authority=x[3],relation=x[4]) for s,x in hadith.items()},revelation_history_assessment=dict(sources=['W_ASB','IK1','DUR1','BAY1','H_B3','H_B4474'],makki='preferred by several inspected authors; not a unanimous independently dated historical fact',madani='early alternative explicitly preserved',double_revelation='reported harmonization, not independently established',abu_maysara='mursal structural gap; not independently graded',first_revelation='Bukhari 3 specifies Iqra beginning; complete-first-surah question distinct'),qiraat_assessment=dict(primary='NASHR',malik_vs_maalik='both canonical; four ten-readers maalik and other six malik',sirat='sin vs sad and sad-zay ishmaam; specific narrator/path, not simply three interchangeable letters',noncanonical='gloss/companion or grammar possibilities distinguished from canonical readings',numbering='base basmala=1:1 retained; counting is contested'),corpus_limitations=['Razi seven retrieved pages are opening/introduction language material, not verified full Fatiha commentary. The copyLink insert-next-paragraph UI is not evidence of pagination.', 'Other authors were inspected in the stated ranges only; all retrieved pages do not equal complete source coverage.', 'Hawramani lexicons and ABL texts are digital primary reproductions, not image-collated editions.', 'Full rare-source lexical entries behind local packet were unavailable; packet authority is expressly separated.', 'Novelty statements make positive antecedent/ingredient distinctions and no universal nonattestation claim.'],claims=rows)
(W/'evidence_matrix.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n')
(W/'source_coverage.json').write_text(json.dumps(dict(stage=matrix['stage'],actually_inspected=source_scopes,limitations=matrix['corpus_limitations']),ensure_ascii=False,indent=2)+'\n')

# Update retrieval logs conservatively instead of leaving retrieved-only text
# indistinguishable from passages that were actually read.
code_map={'tabary':'TAB','katheer':'IK','zamakhshary':'ZAM','baidawy':'BAY','seoty':'DUR','beqaay':'BIQ'}
log=json.loads((W/'retrieval_index.json').read_text())
for item in log:
 sid=code_map.get(item['author_code'],'RAZ')+str(item['ayah'])
 if item['author_code']=='alrazy':
  item['state']='inspected_limited_introduction_not_full_verse_commentary'
  item['actually_checked']=source_scopes['RAZ_SCOPE']
 elif sid in source_scopes:
  item['state']='inspected_in_stated_ranges'
  item['actually_checked']=source_scopes[sid]
 else:
  item['state']='retrieved_not_checked'
(W/'retrieval_index.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
lex=json.loads((W/'lexicon_retrieval_index.json').read_text())
for item in lex:
 item['state']='full_extracted_primary_entry_inspected' if item['sections'] else 'no_entry_extracted_from_lookup; no_absence_inference'
 item['edition_scope']='digital transcription, not print-collated'
(W/'lexicon_retrieval_index.json').write_text(json.dumps(lex,ensure_ascii=False,indent=2)+'\n')
q=json.loads((W/'quran_quote_audit.json').read_text())
q['manual_full_verse_context_check']='All 169 selected full verse lines read in chunks 1–30,31–60,61–90,91–120,121–150,151–169.'
q['manual_exception_assessment']='The two normalizer mismatches (15:75,6:76) are hamza/tatwil orthography, not changed wording or references.'
(W/'quran_quote_audit.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(claims=len(rows),source_scopes=len(source_scopes),hadith_primary_passages=len(hadith),stage=matrix['stage']),ensure_ascii=False))
