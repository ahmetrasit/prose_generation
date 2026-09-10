# V5 reading invitation — 1:5

You are a fresh reading-invitation writer. Read the complete editorial prose
before writing. It is your sole semantic source.

Write two to four paragraphs of fluent, contemporary Turkish that invite a
regular reader into the full commentary. This is a selective reading entrance,
not a summary, replacement commentary, abstract, or findings inventory. Choose
one coherent arc through one to three consequential changes in the reading. A
grammatical turn, sound, dialogue, material process, temporal change, image, or
conceptual distinction may carry the arc. Do not force surprise or a visual
metaphor.

Begin inside the ayah's own words, images, actions, or relations, with its plain
propositional reading still reachable. Do not front-load context about the
surah, the ayah's position, or the commentary project.

For a chosen movement, let the reader identify the expression being interpreted,
where any nonordinary detail comes from, and what that detail changes in the
reading. Briefly identify the word-family use, restricted form, collocation, or
context that supplies an essential added detail, and preserve the concrete
operation that makes the image work. Keep the ordinary reading and necessary
qualification clear within this explanation; do not repeat them as a fixed
formula. If the movement needs more room, select fewer other movements. Choose
another only when the editorial prose does not supply enough to explain it
faithfully.

When a non-focus ayah supplies a contribution used in the invitation, keep its
reference from the editorial prose beside that contribution.

You may leave other movements entirely in the commentary. Do not flatten
several distinct movements into a broad conclusion merely to fit more of them
into the invitation. Do not repair, extend, or supplement the editorial prose
from memory or outside knowledge. If an attractive movement cannot be explained
faithfully from the editorial prose, choose another complete movement.

Omit technical apparatus. Retain any qualification, source distinction, live
alternative, or boundary whose absence would change the force or meaning of a
chosen reading. Express it naturally beside the image or relation it qualifies.
Do not name branches, candidates, findings, scopes, evidence categories,
ledgers, or workflow stages. Do not list findings serially.

Use the established `{ar:..., tr:..., gloss:...}` syntax, consistent
Turkish-readable transliteration, and short ordinary glosses. Keep Arabic
anchors beside the explanations they ground. Within a paragraph, continue with
the Turkish meaning where clear; provide the necessary local tag when a later
paragraph interprets the carrier anew. Do not place Arabic script outside a
valid tag.

Build transitions by carrying an already intelligible object, action, or
relation into its next change. Do not praise the commentary's quality, promise
what the reader will find, manufacture suspense, recap at the end, or add a call
to action. End on an image, relation, action, or tension already established by
the selected arc.

Before finishing, check each selected image against its editorial explanation:
can the reader tell where its nonordinary detail comes from and how it changes
the reading, with the necessary qualification intact? Repair any missing link
in the prose. Do not output this check.

Write only the invitation text to:

`_commentary/v5/editorial/s001-ce-controlled-v3-20260910/s001/1_5/1_5.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s001-ce-controlled-v3-20260910/s001/1_5/1_5.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
## Muhatabın Öne Çıkışı

Âyetin açık sözü şudur: “Yalnız sana kulluk ederiz ve yalnız senden yardım isteriz.” Önceki âyetlerde hakkında konuşulan Allah (1:1, 1:2, 1:3, 1:4), burada doğrudan muhatap olur. {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} ikinci şahıs zamiridir; fiilden önce getirildiği için konuşma daha eylem söylenmeden yönünü bulur. Türkçedeki “yalnız” bu öne alışın kurduğu sınırı duyurur: topluluğun kulluğu baştan belirlenen bu muhataba yönelir. Böylece övgü dili hitaba, ilahî tanıma da “biz” diye verilen bir söze dönüşür.

Bu dönüşün cümledeki izi iki kez çizilir. İlk {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} ile {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} tam bir cümle kurar; {ar:وَ, tr:wa, gloss:ve} onu ikinci tam cümleye bağlarken yeni bir başlangıcın da menteşesi olur. Ardından gelen ikinci {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana}, ilk sınırlamayı ödünç almakla yetinmez: {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} fiiline kendi “yalnız Sen” çerçevesini verir ve aynı kişiyi bu kez yardımın kaynağı olarak yeniden belirler. İki fiil arasında ortak bir sözlük kökü yoktur; onları işitilir biçimde paralel kılan, kök taşımayan aynı nesne zamirinin her iki fiilin önünde yeniden kurulmasıdır. Kulluk ile yardım isteme iki ayrı eylem olarak kalır, fakat ikisi de “Sen-önce” düzeninde söylenir.

Aktarılan okuyuş ve kelime sınırı farklılıkları bu yapının ne kadar hassas işitildiğini de gösterir. İlk {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} çevresindeki ayırma ihtimalleri zamirin fiilden ayrı, öne alınmış nesne oluşunu daha duyulur kılar. {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} çevresindeki ses ve kip alternatifleri konuşanın duruşunu başka türlü kurabilecek bir karşılaştırma açsa da burada okunan biçim etkin ve birinci çoğuldur. {ar:وَإِيَّاكَ, tr:wa iyyāka, gloss:ve yalnız sana} birleşme yerinde sesler farklı kaynaşabilir; ikinci zamir yuvasının çevresindeki ayırma ihtimalleri aynı sınırı başka tonda duyurabilir. Kapanıştaki {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} için aktarılan önek ünlüsü ve uzatma farklılıkları ses rengini değiştirir. Bunların içinde yerel cümleyi taşıyan çözüm değişmez: iki ayrı ön nesne ve iki etkin birinci çoğul fiil.

## Söz Veren ve Yardım İsteyen “Biz”

İlk fiil olan {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz}, yalın birinci kalıpta hizmet ve tapınmayı bildirir. Bitmiş bir işi kayda geçiren sözden ziyade sürmekte olan, tekrar tekrar üstlenilen bir eylem duyurur; birinci çoğul kişi de bu eylemi tek kişinin özel hâli olmaktan çıkarıp topluluğun ortak pratiği yapar. Önündeki {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} bu hizmeti belirli muhataba yönelttiğinde fiil, sıradan bir işi yapmanın ötesinde boyun eğerek tapınma ve kendini dinsel yönelişe verme ağırlığı kazanır. Bu doğrudan dilbilgisel temasın seçtiği anlam kulluktur; kelime ailesindeki sahiplik, yol ve başka uzak kullanımlar ancak ayrıca bir bağ onları harekete geçirdiğinde söze katılabilir.

Ardından gelen {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz}, daha ağır türemiş onuncu kalıbıyla yardımın kendiliğinden gelmesini bekleyen edilgen kişiler çizmez; konuşanlar desteği isteme işini bizzat üstlenir. İkinci {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} yardımın kimden istendiğini fiilden önce sıkıştırarak kaynağı kesinleştirir. Buna karşılık cümle, ne için yardım istendiğini belirli bir nesneyle kapatmaz. İsteğin içeriği açık kalır ve sonraki yol talebine doğru uzanabilir (1:6). Bu yüzden ikinci yarı, kulluğun yanına eklenmiş bağımsız bir dindarlık sözü gibi değil, sözü verilen hizmeti mümkün kılacak destek talebi gibi duyulur.

Bu fiilin yerel biçimi yardım istemeyi seçer. Aynı geniş kelime çevresinde yaş ve bedensel olgunluk, yinelenmiş savaş, bir yer adı, hazır kaynak ve gözle ilgili uzak kullanımlar bulunması, bunların hepsini {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} içine kendiliğinden yerleştirmez. Yine de ilerleyen bağlar bu uzak ayrıntılardan bazılarını ayrı ayrı tetikleyebilir: güç olgunluğu yolda dengede kalmayı, yinelenmiş savaş baskı altında desteği, hazır kaynak borç karşısındaki imkânı, bakış ise koruyucu gözetimi renklendirir. Her seferinde giriş kapısı olağan “yardım isteriz” anlamıdır; yer adı ve bağlantı kurulmayan öteki göz kullanımları cümlenin dışında kalır.

Öne alınan muhatabın iki kez anılması, bu bildirim ile talebi aynı kişiye bağlanan tek bir yöneliş hâline getirir. İbadetin rakip nesnelere yönelmesi (26:71), burada başka odaklara dağılmayı önleyen sınırı belirginleştirir; rakip nesneler yalnızca karşıt çizgiyi gösterir, bu âyetin asıl taşıyıcıları kendi iki fiilidir. Çağrı ile karşılığın buluşması (2:186) yardım talebini cevap bekleyen canlı bir ilişki olarak, kulluk ile tevekkülün yan yana gelişi (11:123) ise hizmetin dayanılarak sürdürülmesini görünür kılar. Bu temaslar {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} ile {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} arasındaki bağı derinleştirir: hizmet de onu taşıyacak destek de aynı muhataba yönelir. Bunun ötesinde bütün ibadet nesneleri, bütün yardım biçimleri veya yardımın tek bir psikolojik ve tarihsel modeli hakkında genel bir hüküm kurulmaz.

Üstelik bu muhatap cümleye çıplak bir “sen” olarak girmez. {ar:بِسْمِ, tr:bismi, gloss:isimle} onu adlandırma içinde anmış, {ar:ٱللَّهِ, tr:Allāh, gloss:Allah} ibadet edilen ilâhı belirtmiş, {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:al-Raḥmān al-Raḥīm, gloss:Rahmân ve Rahîm} merhameti öne çıkarmıştır (1:1). {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabb al-ʿālamīn, gloss:âlemlerin Rabbi} terbiye eden Rabliği (1:2), {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi al-dīn, gloss:hesap gününün sahibi} ise mülkiyet, hüküm ve hesap ufkunu ekler (1:4). Bu adlandırmaların ardından {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} denmesi, tanınmış olanı doğrudan hizmet edilen ve yardımı istenen kişi yapar. Önceki övgü bağlayıcı bir uygulama sözüne geçer; zamirin öne alınmış nesne ve sınırlama işlevi de aynen sürer.

## Bağımlılık İçinde Eylemek

{ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} açıkça ibadet etmeyi söylerken, ait olduğu kelime ailesi bağımlılığın birkaç ayrı ucunu da taşır. Bir uçta başkasına ait, özgür kişinin karşıtı olan kul vardır; başka bir uçta insanı zorla boyunduruk altına alma; fiilin burada seçtiği uçta ise Tanrı’ya yönelip kendini hizmete verme bulunur. Rahmet ve bilgi verilmiş kul (18:65), ait oluşun yalnız edilgin yoksunluk demek olmadığını gösterir. Zorla boyunduruk altına alma (26:22) aynı asimetrinin sert sınırını açar. Kullukla tevekkülün (11:123), yardım istemekle sebatın buluşması da (7:128) bağımlı kişinin yine de yönelen, isteyen ve dayanan bir özne olarak kaldığını gösterir. Böylece {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz}, bağlı konumdan hareket eden failliği görünür kılar; birinci kalıptaki kulluk fiili hukuki köleliğin doğrudan adı hâline gelmez.

Bu asimetriye hürmet de eşlik eder. {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} ile bağlantılı başka bir kullanım, saygıdeğer ve yüce tutulan kişiye sunulan hizmeti düşündürür. {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabb al-ʿālamīn, gloss:âlemlerin Rabbi} (1:2) ile {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:māliki yawmi al-dīn, gloss:hesap gününün sahibi} (1:4) mülkiyet ve tasarruf farkını korurken, bu onurlu hizmet yönü muhatabın etkin biçimde yüceltilmesini sağlar. {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} ise bu hürmeti konuşanların kendi kendilerine yeterli oldukları iddiasına dönüştürmeden sürdürür. Ardından gelen {ar:أَنْعَمْتَ, tr:anʿamta, gloss:nimet verdin} içindeki yumuşaklık, kolaylık ve iyi hâl ayrıntıları (1:7), köleleştirmenin çıplak zorlama ucuna karşı basınç oluşturur. Bağımlılık kaybolmaz; zorla boyun eğdirilme ile onurlu hizmet de tek bir anlama eritilmez.

Merhamet bu bağımlılığın içinde nasıl yaşandığını değiştirir. {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:al-Raḥmān al-Raḥīm, gloss:Rahmân ve Rahîm} adlarının bağlı olduğu anlam çevresinde (1:1, 1:3) rahim, bağımlı hayatı içine alan, tutan ve biçimlendiren bir kuşatma imgesi taşır. Bu imge, {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} içindeki sahip olunan statüsü ile {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} içindeki devam eden destek talebine değdiğinde, hizmet çıplak zorlama altında değil, hayatın korunup biçimlendiği bir bakım zemini üzerinde sürer. Merhamet yardım fiilinin yeni sözlük karşılığı değildir; bağımlılığın asimetrisini koruyarak o ilişkinin çevresini değiştirir.

Bakım imgesi {ar:رَبِّ, tr:rabb, gloss:Rab} sözündeki onarma, yetiştirme ve tamamlamayla gelişir (1:2). {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} bitmemiş görünüşüyle süren pratiği taşırken, {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} çevresinde beliren bedensel güç olgunluğu, işe yarar kapasiteye erişme ayrıntısını sağlar. Rabliğin aşamalı bakımı ile aynı bağlamdaki büyüme ve beslenme, bu kapasitenin bir defada hazır bulunmadığını; hizmet edenlerin onarılıp yetiştirilerek iş görebilir hâle geldiğini düşündürür. Âyet yine kulluk ile yardım isteğini söyler: fiziksel yaş yardımın anlamına, bu ilişki de tamamlanmış bir gelişim teorisine dönüşmez.

Bakımın daha uzak bir görünümü, koruyucu dikkattir. {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} çevresindeki göz ve bakışla ilgili kullanım, ancak {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} içindeki saygı ve hizmet ilişkisiyle temas ettiğinde yerel bir karşılık bulur: istenen yardım, dışarıdan eklenen kuvvetin yanında hizmet eden topluluğu göz önünde tutan, koruyan ve gözeten bir dikkat gibi hissedilebilir. Bu keşifsel temas yardım istemenin olağan anlamını genişletir; gözle ilgili öteki uzak anlamları cümleye doldurmaz.

Bakım altında gelişen hizmet, Rabliğin farklı bir ayrıntısıyla ahit diline yaklaşır. {ar:رَبِّ, tr:rabb, gloss:Rab} ile bağlantılı bağlayıcı sözleşme ve ahit kullanımı (1:2), {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} bildirimini bağlılık taahhüdü olarak duyurur. Ardından {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz}, bu taahhüdün yerine getirilebilmesi için gereken arkalama ve imkânı ister. Bir taraf hizmet sözünü, öteki onu sürdürecek desteği taşır; yerel ahit benzetmesi cümlenin bildirim ile talep yapısını korur.

Bu söz şimdide verilirken hesabın geleceğine de açıktır. {ar:مَٰلِكِ, tr:māliki, gloss:sahip ve hükmeden}, {ar:يَوْمِ ٱلدِّينِ, tr:yawmi al-dīn, gloss:hesap günü} içinde mülkiyet ile tasarrufu, sınayıcı ve şiddetli günü, hesaplaşmayı ve karşılığı getirir (1:4). Bu ufukta {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} hesap verecek itaati şimdi sürdürür; {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} de o süreklilik için dayanma desteğini şimdi ister. Hesap günü fiillere yeni bir gelecek zaman yüklemez ve mevcut kulluğu ertelemez; bugünkü hizmeti, sorumluluğunun ileride karşılık bulacağı bir yerleşmeye doğru açar.

Sorumluluk, konuşanların kendi başarılarını büyütmesine de izin vermez. {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} gerçek ve etkin bir iş yaptıklarını söyler; {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} ise o işi yapabilme gücünün istendiğini açıklar. {ar:ٱلْحَمْدُ, tr:al-ḥamd, gloss:övgü} değeri muhataba yerleştirir (1:2); aynı anlam çevresindeki, birinin başkasına yaptığı iyilikle övünmesi ihtimali de “biz yaptık, öyleyse övgü bize aittir” sonucunu görünür kılıp keser. {ar:ٱهْدِنَا, tr:ihdinā, gloss:bizi ilet} sözünde sevgiyle gönderilen armağan ayrıntısı (1:6), {ar:أَنْعَمْتَ, tr:anʿamta, gloss:nimet verdin} sözünde ise bağış ve iyi hâl belirir (1:7). Böylece yardım, hizmet karşılığında kazanılmış ücret yerine hizmeti mümkün kılan lütuf olarak duyulur; kulluk eylemi silinmez, basit yardım dileğinin başka canlı okumaları da kapanmaz.

Ücret hesabı kesilmiş olsa da hesap dilinin açtığı ayrı bir ekonomik benzetme yaşamaya devam eder. {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} içindeki sahip olunan statüsü ile {ar:مَٰلِكِ, tr:māliki, gloss:sahip ve tasarruf eden} mülkiyet ilişkisini kurar; {ar:ٱلدِّينِ, tr:al-dīn, gloss:hesap ve karşılık} borç ve ertelenmiş ödeme çağrışımını getirir (1:4). Bunlara {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} çevresindeki, eldeki maddi para gibi hemen kullanılabilir kaynak ayrıntısı eklenince, borç altındaki bağımlı hizmetli kendisinde bulunmayan hazır imkânı sahibinden ister gibi görünür. Bu benzetme mülkiyet, borç, mevcut kaynak ve yardımın ayrı katkılarıyla kurulur; yardım fiili nakit para demek olmaz ve lütfu ücret hesabına geri çevirmez.

## Geçilebilir Yol ve Onu Taşıyan Destek

Yardımın neye açıldığı, {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā al-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} talebiyle somutlaşır (1:6). Bu yakınlık, {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} kelime ailesindeki özel bir yol kullanımını da işitilir kılar: sık sık üzerinden geçildiği için basılmış, düzleşmiş ve geçilebilir hâle gelmiş yol. İbadet ile dosdoğru yolun yan yana anılması (36:61), yönlendirmenin yine dosdoğru yol üzerinden söylenmesi de (37:118) bu teması bağımsız biçimde destekler. Bu temaslar odağa döndüğünde kulluk, içsel bağlılığın yanında tekrarlı pratikle geçiş imkânı hazırlayan yol emeği gibi duyulabilir. Bu ayrıntı mevcut fiilin sözlük kökenini yeniden yazmaz; maddi yol yapımını, bütün bir yol sistemini veya aynı kelime çevresindeki deve ve gemi kullanımlarını âyete taşımaz.

Bu yol imgesi belirginleşince yardımın katkısı daha seçik görünür. İbadet ile rota arasındaki bağ (36:61), {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} içindeki sık geçiş emeğini açar; yardım istemekle sebatın ve aitliğin yan yana gelişi (7:128) ise {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} içindeki dayanışmayı açar. Bir işlem yolu yürünebilir kılar, öteki o yol üzerindeki hareketi taşır. Yöneltme ve dosdoğruluk geçişin yönünü (1:6), yol ayrımları ise bu yönün kaybedilebileceği sınırı gösterir (1:7). Böylece hizmet ile destek, yol emeği ve destekli yürüyüş olarak birbirini açıklar; bu yerel birleşme sonraki âyetlerin bütün mimarisini 1:5’in tek başına kurduğu iddiasına dönüşmez.

{ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} bu yürüyüşte yalnız dışarıdan kurtarılmayı değil, hareketi dengede sürdürecek kuvveti de düşündürür. Yardım, sebat ve aitlik beraber göründüğünde (7:128), kelime çevresindeki güç olgunluğu ve bedensel denge ayrıntısı yolda dik durmayı sağlayan desteğe dönüşür. Dosdoğru yola yönlendirilme eklenince (37:118) kişiler, güçlerini toparlayarak belirlenmiş yönde birlikte ilerleyen bir topluluk gibi görünür. Bu iki bağ odağa döndüğünde dışarıdan gelen destek ile iç hizalanma aynı yürüyüşte buluşur. Yardım fiziksel yaş demek olmaz; yönlendirme, dik duruş ve dosdoğruluk da yardım fiilinin içinde ayrı sözlük anlamları olarak ilan edilmez.

Bu yüzden yardım yalnız yetenek çöktüğünde başvurulan bir kurtarma değildir; kulluğu ayakta tutan sürekli destek olarak da duyulur. {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:al-Raḥmān al-Raḥīm, gloss:Rahmân ve Rahîm} merhametin çevresini (1:1, 1:3), {ar:رَبِّ, tr:rabb, gloss:Rab} yetiştirici bakımı (1:2), {ar:ٱلْمُسْتَقِيمِ, tr:al-mustaqīm, gloss:dosdoğru} gözetilip korunacak dengeyi (1:6), {ar:أَنْعَمْتَ, tr:anʿamta, gloss:nimet verdin} ise bağışı sağlar (1:7). Bu ayrı temaslar {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} talebini, kulluğun sürmesini sağlayan ilişkisel bir imkân olarak renklendirir. {ar:ٱهْدِنَا, tr:ihdinā, gloss:bizi ilet} yumuşakça yöneltmeyi ekler (1:6); dosdoğru oluş da hareketin gözetilip korunmasını sağlar. Hidayet ile yardım birbirine karışmaz, merhamet ve nimet de yardım fiilinin yeni sözlük anlamı olmaz.

Yolun önünde engel bulunduğunda aynı ilişki daha sert bir görüntü kazanabilir. {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} istenen kuvveti getirir; {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} çevresindeki güç ve sağlamlık ayrıntısı bağlılığın dayanıklılığını besler. {ar:ٱهْدِنَا, tr:ihdinā, gloss:bizi ilet} geçişi açacak yöneltmeyi, {ar:ٱلصِّرَٰطَ, tr:al-ṣirāṭ, gloss:yol} ise kesip içinden geçen yol görüntüsünü verir (1:6). Destek ilerlemeyi tıkayan şeye yetişir; sağlamlık onun karşısında tutunmayı sağlar; yöneltme nereye geçileceğini belirler; kesen geçit de engelin içinden yol açar. Yardım bu etkileşim içinde engeli kaldıran kuvvet gibi hissedilir. Bu, hidayetin etimolojisi veya şiddet emri değildir; olağan yardım ve yol talebine eklenen, sınırı engelin kaldırılmasıyla çizilmiş bir imgedir.

## Yönü Kaybetmemek

Geçilebilir yolu hazırlamak yalnız dış engelle ilgili değildir; hizmet eden kişinin içinde de bir direnç bulunabilir. Gönüllü kulluğun kibirle geri durmanın karşısına konması (4:172), incinmiş gurur ve öfkeli iç gerilim ayrıntısını {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} içindeki boyun eğmiş hizmete değdirir: kulluk, kendini dayatan karşı koyuşu çözen bir iç disiplin gibi işler. Yüründükçe geçilebilir olan yol emeği (36:61) bu iç disiplinle yan yana kalır; biri ötekini seçip silmez. {ar:ٱلْمَغْضُوبِ, tr:al-maghḍūb, gloss:öfkeye uğrayanlar} ve {ar:ٱلضَّآلِّينَ, tr:al-ḍāllīn, gloss:sapanlar} da karşıtlığa dönme ile yönü kaybetme ihtimalini görünür kılar (1:7). Kulluk fiili bununla öfke, keder veya intikam diye çevrilmez; açık ibadet, gururu yumuşatan yönü de taşıyarak sürer.

Tekrarlanan {ar:إِيَّاكَ, tr:iyyāka, gloss:yalnız sana} bu iç disipline bir hedef verir. {ar:غَيْرِ, tr:ghayr, gloss:başka değil} ikame ve başkasına dönüşme ihtimalini, {ar:ٱلْمَغْضُوبِ, tr:al-maghḍūb, gloss:öfkeye uğrayanlar} karşıtlığı, {ar:ٱلضَّآلِّينَ, tr:al-ḍāllīn, gloss:sapanlar} ise hedef kaybını açar (1:7). Bunlar {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} ile {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} üzerine baskı yaptığında, ayrıcalık vurgusu yalnız muhatabı tekleştirmekle kalmaz; bağlılığın nesnesini değiştirmeme ve yönü kaydırmama disiplini olur. Yardım da yalnız hizmeti yapabilmek için değil, hizmetin kime yöneldiğini korumak için istenir. İbadet karşıtlık veya sapma anlamına dönüşmez; bu bağ, onların doğurduğu kaymayı önleyen yardımı görünür kılar.

Yönü koruma ihtiyacı “biz” sözünün içindeki kırılganlığı da açar. Birinci çoğul {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} topluluğu zaten ortak bir eylem içinde gösterir; aynı kelime çevresindeki, bir bütünü oluşturan öğelerin farklı yönlere dağılması ayrıntısı ise bu birliğin ayrışma ihtimalini duyurur. {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} karşılıklı arkalama sağlar. Yol ile toplu yöneliş (1:6), uçuş, dağılma ve sapma görüntüleri de (1:7) bu arkalamanın nedenini somutlaştırır. Aynı muhataba iki kez seslenmek, yolları ayrılabilecek kişileri yeniden tek hedef çevresinde toplar. Bu yerel dağılma imgesi konuşanların tarihsel olarak bölünmüş olduğunu ileri sürmez; düz okumadaki birlik, dağılma ihtimaline karşı etkin biçimde korunur.

Bu korunma daha sert, keşifsel bir ihtimalde mücadele desteği gibi de duyulabilir. {ar:نَسْتَعِينُ, tr:nastaʿīnu, gloss:yardım isteriz} çevresindeki tekrarlanmış ve yeniden alevlenen savaş kullanımı, yardım ile sebatın buluşması sayesinde direnç karşısında arkalama arayan hareketi açar (7:128). {ar:نَعْبُدُ, tr:naʿbudu, gloss:kulluk ederiz} boyun eğmiş bağlılığı ve baskı altında sağlamlığı taşır. {ar:ٱلصِّرَٰطَ, tr:al-ṣirāṭ, gloss:yol} kesen geçit ve kesici kenar görüntüsünü (1:6), {ar:ٱلْمَغْضُوبِ, tr:al-maghḍūb, gloss:öfkeye uğrayanlar} misillemeye yükselebilen öfkeyi ve karşıt yol gruplarını getirir (1:7). Kibirli karşı koyuş da (40:60) mücadelenin yalnız dış engel değil, ibadetten geri duran direnç olduğunu gösterir. Destek bu yinelenen dirence karşı arkalama sağlar; boyun eğmiş hizmet bağlılığı tazeler; kesen yol ilerleme baskısını, öfke ise misilleme tehlikesini belirginleştirir. Böylece topluluk, tekrarlanan mücadele içinde yönünü koruyacak desteği istiyor gibi görünür. Sahne belirli bir tarihsel savaşı veya şiddet buyruğunu kurmaz, 1:7’deki her sapma ayrıntısını yardım fiiline yüklemez ve savaşı kulluğun sözlük anlamı yapmaz; barışçıl kulluk ile genel yardım duasının içinde, baskı karşısında sebat eden ikinci bir model olarak kalır.

</editorial_prose>
