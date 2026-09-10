# V5 reading invitation — 1:4

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

`_commentary/v5/editorial/s001-ce-invitation-v2-20260910/s001/1_4/1_4.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s001-ce-invitation-v2-20260910/s001/1_4/1_4.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
## Bir Zincirin Tuttuğu Gün

Âyetin açık sözü kısadır: Allah hesap gününün sahibidir. Bu anlamı taşıyan {ar:مَٰلِكِ, tr:mâliki, gloss:sahibi ve hükmeden}, {ar:يَوْمِ, tr:yevmi, gloss:Gün} ve {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık düzeni} Türkçede tek bir tamlama gibi duyulsa da Arapçada birbirine geçen iki aidiyet bağıyla kurulur. Başta duran mâliki bütün yapıyı elinde tutar; yevmi bir yandan onun neye sahip olduğunu söylerken öte yandan ed-dîni kendisine bağlar. Böylece söz, sahibinden belirli bir zamana, o zamandan da onu hesap ve karşılık günü yapan içeriğe doğru iner. Ortadaki Gün pasif bir ara halka değildir: sahipliği alır, hesabı yönetir ve ikisini aynı menteşede birleştirir.

Bu zincirde belirginlik sondan başa doğru yürür. {ar:يَوْمِ, tr:yevmi, gloss:Gün} kendi üzerinde bir belirli artikel taşımadığı hâlde, sonundaki {ar:ٱلدِّينِ, tr:ed-dîni, gloss:belirli hesap düzeni} onu herhangi bir gün olmaktan çıkarır; ed-dîni’nin belirginliği yevmi’ye, oradan bütün tamlamaya yayılır. Son kelime gramer bakımından bağlı unsur olduğu hâlde anlam bakımından önceki zamanı tanımlar: söz, başka bir gün türünü seçmeden tanınan “hesap günü” formülünü kurar ve baştan beri söylenen sahipliğin neye ait olduğunu geriye dönerek açıklar. Buradaki genitif biçim Gün’ü sahip olunan unsur olarak zincirin içinde tutar. Aktarılan hâl karşıtlığında mansup bir biçim zamanı “o gün” diye zarflaşmış bir sahneye çevirebilirdi; mevcut okuyuş ise o ihtimali cümleye taşımaz, Gün’ü doğrudan sahiplik bağının içinde bırakır.

{ar:مَٰلِكِ, tr:mâliki, gloss:sahibi ve hükmeden} bir fiil gibi “o Gün sahip olacak” demez. Etkin ortaç biçimi, sahipliği Gün başlayınca ortaya çıkacak bir olay olarak değil, zaten duran ilahî bir nitelik olarak verir; sonlu fiili olmayan ad zinciri bu sürekliliği pekiştirir. Kur’an’da seyrek görülen bu etkin sahiplik biçiminin ilahî göndergeyle buluşması da sözü sıradan bir mülk kaydından ayırır. Buradaki sahiplik, ince bir hukukî unvandan fazlasıdır: elde bulundurma ile o şey üzerinde tasarruf ve hüküm yürütme yetkisini birlikte taşır. Aktarılan başka okuyuş, sahiplik tonuna hükümdarlığı da ekler; biri ötekini hükümsüz bırakmaz, mevcut mâliki söyleyişi ikisini aynı otorite aralığında tutar.

Bu yerel biçim, kelimenin ilişebildiği her uzak kullanımı kendiliğinden çağırmaz. {ar:مَٰلِكِ, tr:mâliki, gloss:sahiplik ve tasarruf} burada evlilik, haber taşıma ya da yolun merkezi gibi başka alanlarla değil, belirli Gün üzerindeki yetkiyle seçilmiştir; yolun ana kesimiyle ilgili kullanım ancak bağımsız yol talebi ona dokunduğunda ayrıca açılacaktır (1:6, 1:7). Ses ve yazı akışı da önce bu seçilmiş başı duyurur: mâliki’deki uzun ünlü sözü genişletir, ardından art arda gelen genitifler alanı daraltır. {ar:يَوْمِ, tr:yevmi, gloss:Gün} ile {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap düzeni} arasındaki yumuşak geçiş, artikelin d sesine katılıp başlangıcı çiftlemesi ve sonlardaki nazal tını, iki adı tek bir işitilebilir bütün hâline getirir. Açılan sesin ed-dîni’de kapanması, tamlamanın hem gramer hem anlam bakımından tamamlandığını duyurur; bu işitsel hareket yeni bir sözlük anlamı eklemez.

## Günün İçini Dolduran Hesap

{ar:يَوْمِ, tr:yevmi, gloss:Gün} burada bir eylemi ya da o eylemi yapanı bildirmez; kararlı bir zaman adıdır. Tekil ve sınırlı bir zaman birimini korur; yine de {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık} ile kurduğu yerleşik formül onu nötr bir takvim yaprağından belirleyici olayın ufkuna taşır. Gün, hem hesabın gerçekleştiği sınır hem o hesabı görünür kılan büyük olay olur. Bu esneklik zamanı belirsiz ya da sınırsız bir devreye yaymaz. Aynı zamanda tamlamanın ortasında durarak soldaki kalıcı sahipliği sağdaki hüküm ve karşılık içeriğine geçirir.

{ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık düzeni} bu zamanın içinde ne olduğunu söyler. Âyet “yargılıyor” diye hareketli bir fiille kapanmaz; belirli, tekil ve soyut bir adla Gün’e içeriğini veren tanımlı bir sistemi adlandırır. Yerel seçim hüküm, hesap ve karşılığı öne çıkarır. Bunun çevresinde borca konu olanın verilmesi, geri dönmesi ve yükümlülüğün karşılanması baskısı; ayrıca bağlayıcı ahlâkî düzen, itaat ve boyun eğme yönleri duyulabilir. Böylece hesap, havada kalan tek bir karar değil, yapılanın karşılığının görüldüğü ve ilişkiyi bağlayan bir düzen olarak belirir. Bu daha geniş düzen duygusu hesabı silmez; ed-dîni’yi yalnız mali borca, yalnız itaate ya da genel bir “yaşam yolu”na da kapatmaz.

Üç kelimenin ilk ortak açılımı, kamusal bir olay sahnesidir. {ar:مَٰلِكِ, tr:mâliki, gloss:egemen sahiplik} kalıcı ve ilahî egemenliği, {ar:يَوْمِ, tr:yevmi, gloss:kritik olay zamanı} büyük olayın zamanını, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hüküm ve karşılık} ise o olayda icra edilen hesabı getirir. Birbirlerine değdiklerinde Gün, takvimde işaretli bir tarihten çıkıp otoritenin açıkça işlediği, sonuçların belirdiği bir ufuk olur. Bu görüntü hesap gününün olağan anlamını içerir; ayrıntılı bir mahkeme düzeni ya da yeni bir hüküm öğretisi kurmaz.

Bu olay ufku, hesabı vadesi gelen bir yükümlülük gibi de somutlaştırır. {ar:مَٰلِكِ, tr:mâliki, gloss:sahiplik ve tasarruf} borcu ve onun zamanını elinde tutan yetkiyi, {ar:يَوْمِ, tr:yevmi, gloss:vade süresi} gündüzün uzunluğuna bağlı olmayan olgunlaşma aralığını, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:borç yükümlülüğü} ise alınıp verilenden doğan cevap sorumluluğunu taşır. Hesap böylece ertelenmiş yükümlülüğün vadesine erişip kapanması gibi duyulur. Bu maddi model karşılığın zamanını ve ciddiyetini görünür kılar; dîni mali sözleşmeyle özdeşleştirmez, Gün’ü de belirsiz bir süreye dönüştürmez.

Vadenin sürmesi, aynı sözleri bir bağlılık ilişkisi içinde duymaya izin verir. {ar:مَٰلِكِ, tr:mâliki, gloss:kamusal yönetim yetkisi} buyruk koyan otoriteyi, {ar:يَوْمِ, tr:yevmi, gloss:süren zaman alanı} bağlılığın yaşandığı süreyi, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:boyun eğerek uyma} ise üstün iradeye tekrar tekrar uymayı getirir. Bu temas, sahipliği yalnız olayın sonunda beliren yetki olmaktan çıkarıp zaman içinde işleyen bir itaat düzeninin yönetimi olarak da duyurur. Yine de belirli hesap günü yerinde kalır; bu görüntü her tarihsel yönetim biçimine yayılmaz ve sonul karşılık sahnesini ortadan kaldırmaz.

Daha ihtiyatlı, aktarılan bir açılımda sahiplik düzeni ayakta tutan iç dayanak olarak belirir. {ar:مَٰلِكِ, tr:mâliki, gloss:taşıyan dayanak} güçlü ve iç tutarlı biçimde bir arada tutan temeli, {ar:يَوْمِ, tr:yevmi, gloss:süreklilik alanı} bu taşımanın sürdüğü zamanı, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:yerleşmiş düzen} ise tekrarlandıkça alışkanlık ve kuruma dönüşen işi taşır. Böylece egemenlik, yapının zaman içinde dağılmadan işlemesini mümkün kılan dayanak gibi duyulabilir. Dîni’nin düzenlenmiş toplu yerleşim, hatta kent çağrışımı bu soyut düzeni kurumsal bir biçimde göz önüne getirir. Fakat kelime gerçek bir şehir adına dönüşmez, mâliki fiziksel bir temel demek olmaz, yevmi sonsuz devirler hakkında bir iddia kurmaz. Bu atfedilmiş görüntü, “hesap gününün sahibi” sözünün taşıyıcı egemenliğine eklenir.

## Övgüden Muhataba

{ar:مَٰلِكِ, tr:mâliki, gloss:sahibi ve hükmeden} önceki ilahî nitelemelerden kopuk yeni bir unvan gibi gelmez; genitif biçimiyle süren övgü ve niteleme zincirine bağlanırken kendi sağında yeni tamlamayı açar (1:2, 1:3). Böylece önceki rahmet sözlerinden hesabın belirli zamanına geçilir; Gün’ün ileriye dönük ufku hemen sonraki ibadet ve yardım hitabını, ardından yol talebini hazırlar (1:5, 1:6), fakat onların ayrıntılarını bu üç kelimenin içine taşımaz. Başlangıçtaki {ar:ٱللَّهِ, tr:Allâhi, gloss:Allah adı} kimin adlandırıldığını gösterir (1:1); biraz sonra gelen {ar:نَعْبُدُ, tr:na‘budu, gloss:kulluk ediyoruz} ise aynı muhataba fiilen yönelir (1:5). Bu iki bağımsız temas sayesinde hesap sahibinin egemenliği soyut ve adsız bir yetki olarak kalmaz: adı anılmış, ibadet edilen ve buyruğuna uyulan Allah’ın yetkisi olur. Ad burada sahibin kimliğini gösteren işaret, ibadet de bu asimetrik ilişkinin yaşanan cevabıdır; ikisi hesap ve karşılık anlamını değiştirmeden onun kime ait olduğunu somutlaştırır.

Bu yetki, {ar:ٱلرَّحْمَٰنِ, tr:er-Rahmâni, gloss:merhameti kuşatan} ve {ar:ٱلرَّحِيمِ, tr:er-Rahîmi, gloss:merhameti sürdüren} sözlerinin hemen ardından duyulur (1:1, 1:3). Bu yüzden {ar:مَٰلِكِ, tr:mâliki, gloss:sahibi ve hükmeden} içindeki tasarruf, merhametin çevrelediği sahiplik olarak karşılanır; {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık} hüküm işini sürdürürken, o hükmün muhatabıyla kurduğu ilişki yakınlık kazanır. Rahmet hesabı gevşetmez ve karşılığı kaldırmaz; hesabın sahibinin duygu dışı bir mülk sahibi ya da kopuk bir cezalandırıcı olarak tasavvur edilmesini engelleyen çerçeveyi kurar.

Önceki {ar:ٱلْحَمْدُ, tr:el-hamdu, gloss:övgü ve değer takdiri} de {ar:يَوْمِ, tr:yevmi, gloss:belirleyici Gün} ile {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık} üzerinde başka bir ışık açar (1:2). Hamd doğrudan Allah’a yönelen övgü olarak bütünüyle yerinde durur; aynı zamanda övülecek olanla yergiye düşenin ayrımını ve ulaşılması övülen sonu duyurabilir. Bu temasla hesap günü, yalnız cezanın dağıtıldığı bir mahkeme değil, neyin övgüye ya da yergiye layık olduğunun açığa çıktığı son değerlendirme olur. Değerin görünmesi hüküm ve karşılığın yerine geçmez; onların neyi değerlendirdiğini anlaşılır kılar ve hamdin yalnız bu ikincil çağrışıma kapatılmasına izin vermez.

{ar:رَبِّ, tr:rabbi, gloss:besleyip geliştiren sahip} sözünün onarma, besleme ve tamamına erdirme hareketi (1:2), {ar:مَٰلِكِ, tr:mâliki, gloss:işi ayakta tutan sahip} içindeki dayanakla buluşunca vadenin içi boş bekleyiş olmaktan çıkar. {ar:يَوْمِ, tr:yevmi, gloss:olgunlaşma aralığı} yükümlülüğün biçimlendiği süreyi, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve yükümlülük} ise sonunda yerine getirilecek sorumluluğu taşır; sahip, bu hesabın geliştiği aralığı taşıyan zemin gibi görünür. {ar:ٱلرَّحْمَٰنِ, tr:er-Rahmâni, gloss:kuşatan merhamet} ile {ar:ٱلرَّحِيمِ, tr:er-Rahîmi, gloss:süren merhamet} içindeki rahim ve taşıyıcılık çağrışımı da aynı oluşumu koruyucu bir kap içinde düşünmeye izin verir (1:1, 1:3). Bu, yevmi’nin gebelik ya da biyolojik gelişim anlamına geldiği bir okuma değildir: rabblik yetişmeyi, rahmet taşınmayı, mâliki dayanağı, Gün süreyi ve dîni vadesi gelecek yükümlülüğü ayrı ayrı verir; birlikte hesabın zaman içinde olgunlaşmasını görünür kılarlar.

Adlandırma ile yetiştirme, hesabın neyi kapsadığı konusunda da bir açıklık üretir. {ar:مَٰلِكِ, tr:mâliki, gloss:elinde bulunduran sahip} envanterinde hiçbir şeyin eksik kalmadığı bir tasarrufu taşırken, {ar:يَوْمِ, tr:yevmi, gloss:açığa çıkış günü} görünür eşiği, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:kanıtların hesabı} ise o eşikte yapılacak değerlendirmeyi kurar. Başlangıçtaki {ar:ٱللَّهِ, tr:Allâhi, gloss:Allah adı} adlandırmanın seçici işaretini (1:1), {ar:ٱلْعَٰلَمِينَ, tr:el-âlemîn, gloss:bilinen varlıklar ve dünyalar} ise bilinir olma ve ayırt edici alamet çağrışımını getirir (1:2). Böylece hesap, yalnız görünür olanı kaydetmekten öte, kimliklerin ve hâllerin tanınır hâle geldiği bir açıklık gibi de duyulur. Âlemîn tek başına bütün saklı şeylerin listesini vermez; işaret ve bilinirlik, hesabın nesnelerini tanınabilir kılan bağlamsal tetikleyicidir.

## Bugünkü Bağlılık, Gelecekteki Karşılık

{ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve bağlılık} gelecekteki karşılığı adlandırırken hemen sonraki {ar:نَعْبُدُ, tr:na‘budu, gloss:kulluk ediyoruz} bu ilişkiyi şimdiki zamanda yaşanan bir bağlılığa çevirir (1:5). Mâliki’nin kurduğu asimetrik sahiplik, konuşanların isteyerek kulluk ettiği muhataba yönelir; na‘budu’daki yüceltme ve onurlandırma, itaati salt zor altında eğilme görüntüsünden korur. Hükmün Allah’a ait oluşuyla dînin buluşması (12:40) ve teslimiyetin dinle birlikte anılması (3:19), kelimenin boyun eğme çekirdeğini bu yerel ibadetle temas ettirir. Hesap günü kullanımı ise hüküm ve karşılık yönünü gelecekte açık tutar (82:15). Böylece bugünkü kulluk, sonradan açığa çıkacak hesabın ufkunda yeniden okunur; itaat ile karşılık tek sözlük anlamına eritilmez ve aralarında her sonucu zorunlu kılan tek bir nedensellik yasası kurulmaz.

Bu bağlılık içinde borç görüntüsü yeni bir ilişki kazanır. {ar:مَٰلِكِ, tr:mâliki, gloss:alacağın ve imkânın sahibi} tasarruf sahibini, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:borç ve ödeme yükümlülüğü} cevap verilmesi gereken hesabı kurarken, {ar:نَسْتَعِينُ, tr:nesta‘înu, gloss:yardım istiyoruz} cevap verme gücünün yine aynı muhataptan istendiğini söyler (1:5). Bu nedenle alacak sahibi yalnız talep eden değil, yükümlülüğün karşılanabilmesi için kapasiteyi sağlayan yardımcı gibi de görünür. Nesta‘înu’nun hazır imkân ve önden verilmiş destek çağrışımı, gücün ödeme anından önce sunulduğu bir avans görüntüsünü keskinleştirir. Yardım kendi olağan anlamını korur; krediye dönüşmez. Finansal benzetmenin gösterdiği şey, hesapla onu karşılayacak imkânın aynı sahipte buluşmasıdır.

Alınan iyilik bu devreyi daha somut kılar. {ar:ٱلدِّينِ, tr:ed-dîni, gloss:borç ve vadeli karşılık} içindeki şimdi alınıp sonra cevap bekleyen yükümlülük, şükür (1:2), yardım (1:5) ve {ar:أَنْعَمْتَ, tr:en‘amte, gloss:nimet verdin} sözüyle temas eder (1:7); nimetlerin sorulması (102:8), güvenlik ile rızkın verilmesi de aynı ilişkiyi dışarıdan görünür kılar (106:4). Nimet böylece kişinin tek başına ürettiği ve sahiplendiği bir şey değil, bağımlılığı açığa çıkaran ve cevap doğuran bir iyilik gibi duyulur. Bu, her nimeti mekanik bir borç kalemine ya da otomatik kefalete çevirmez; şükür, yardım ve nimet dîni’nin sözlük taşıyıcıları değil, borç modelini harekete geçiren bağımsız bağlamlardır. Vade imgesi, alınmış iyiliğin ileride karşılığının görüldüğü bir ufuk açar; yardım ise bu cevabın kişinin kendi gücüyle kapanmadığını gösterir.

## Kritik Olay ve Son Karşılaşma

Başka ayetlerde açılan temaslar, Gün’ün olay niteliğini keskinleştirir. Mülk ve egemenliğin Allah’ın tasarrufunda oluşu (3:26) {ar:مَٰلِكِ, tr:mâliki, gloss:egemen sahip} sözündeki ilahî hükümdarlığı; ayırma günü (77:13) ile ağır gün (76:10) {ar:يَوْمِ, tr:yevmi, gloss:çetin ve belirleyici Gün} içindeki kritik olayı; hesap günü de {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hüküm ve karşılık hesabı} içindeki hesabı belirginleştirir (82:15). Bu üç katkı birleşince Gün, farklı gidişlerin sonuçlarının egemen biçimde ayrıldığı yetkili bir olay olur. Nimet, öfke ve kayıp ayrımları bu sonuç ufkunu destekler (1:7); öfke ve sapma ise yevmi’nin kendi sözlük anlamı hâline getirilmez. Görüntü ayrıntılı bir kıyamet ya da mahkeme sahnesi kurmaz, bütün yolları tek biçimli bir sınıflamaya da zorlamaz.

Bu olayda sahipliğin sonucu tutan yönü öne çıkar. {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hüküm ve karşılık hesabı} karşılığın eksiksiz ödenmesiyle temas eder (24:25); mülkün Allah’a ait oluşu ve O’nun bağışlama ya da cezalandırma tasarrufu da {ar:مَٰلِكِ, tr:mâliki, gloss:sonuçları tutan sahip} sözünü, hesabın sonuçlarını belirleyen yetkili olarak duyurur (5:40). İnsanların diri ve her şeyi ayakta tutan Rab önünde alçalması (20:111), âlemlerin Rabbi için ayağa kalkması ise {ar:يَوْمِ ٱلدِّينِ, tr:yevmi’d-dîni, gloss:hesap günü} ifadesine yüz yüze bir karşılaşma verir (83:6). Yön talebiyle birlikte okunduğunda bugünkü yürüyüş, sonunda sahibin önünde nasıl durulacağına hazırlanan bir yön kazanır (1:6). Bu temas her davranışı ayrıntılı bir cetvele çevirmez; bağışlama, ceza, nimet ve öfkenin bütün dağılımını da tek ifadeden çıkarmaz.

Son ayetteki farklılıklar hesabın ayırıcı işini içeriden gösterir (1:7). {ar:مَٰلِكِ, tr:mâliki, gloss:sonuçları tayin eden sahip} egemen taksimi, {ar:يَوْمِ, tr:yevmi, gloss:sonuç günü} ayrımın görünür olduğu olayı, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:gidişe verilen karşılık} ise önceki gidişle ortaya çıkan durum arasındaki bağı kurar. {ar:أَنْعَمْتَ, tr:en‘amte, gloss:nimet verdin} iyi durum ve bağışlanma kutbunu; {ar:غَيْرِ, tr:ğayri, gloss:başka ve dışında} farkı, istisnayı ve sınırı; {ar:ٱلْمَغْضُوبِ, tr:el-mağdûbi, gloss:öfkeye uğrayan} yoğun karşılık öfkesini; {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:yolunu kaybedenler} ise bundan ayrı bir kayıp durumunu taşır. Hesap bu sonuçları tek tip cezaya eritmeden ayırır. Onların yalnız gelecekteki Gün’deki sonuçları mı, yoksa şimdiden yürünmekte olan yolları da mı anlattığı sorusu açık kalır.

Bu ayrım, alışılmış düzenin değişmesi ihtimalini de açar. {ar:ٱلدِّينِ, tr:ed-dîni, gloss:yerleşmiş düzen ve hesap} öteden beri süren hâl yönüyle duyulduğunda, {ar:غَيْرِ, tr:ğayri, gloss:başkalaştıran ayrım} içindeki bir şeyi başka biçime koyma çağrışımı ona dokunur (1:7). {ar:مَٰلِكِ, tr:mâliki, gloss:değiştirmeye yetkili sahip} dönüşümü taşıyan egemenliği, {ar:يَوْمِ, tr:yevmi, gloss:kırılma günü} büyük olayın anını verir; hesap günü böylece yerleşmiş işleyişin başka bir düzene çevrildiği egemen kırılma gibi de duyulur. Bu keşifsel görüntü dîni’yi yalnız âdet anlamına getirmez ve tek bir tarih çizelgesini zorunlu kılmaz. Ghayri de dönüşümü tetikleyen bağlam olarak kalır; odak kelimenin yerine geçmez.

Ayırma, kaybolmuş görünenin hesaptan düşmesi demek değildir. {ar:مَٰلِكِ, tr:mâliki, gloss:hiçbir şeyi eksik bırakmayan sahip} sahiplik envanterini, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:açığa çıkaran hesap} değerlendirilecek olanın geri getirilmesini gerektiren hesabı taşır. {ar:ٱلْعَٰلَمِينَ, tr:el-âlemîn, gloss:bilinenler ve ayırt edici işaretler} bilinirlik ve alameti (1:2), {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:kaybolmuş ve yolunu yitirmiş olanlar} ise saklı kalma, kaybolma ve koruyamama yüzlerini sağlar (1:7). Temas, hesabı yok olmuş görüneni yok saymak yerine yeniden ayırt edilir kılan bir toplama gibi açar. Dâllîn tek başına her kaybın fiziksel olarak geri getirileceğinin ya da zorunlu bir nihai açıklamanın kanıtı değildir; görüntünün değiştirdiği şey, sahibin hesabında kayıp görünenin de eksik bırakılmamasıdır.

## Yolun Sahibi, Ölçüsü ve Eşiği

Kaybolma ihtimali, yolun hangi hattında yüründüğü sorusuna geri götürür. {ar:مَٰلِكِ, tr:mâliki, gloss:yolun ana hattını tutan sahip} kelimesinin yolun ya da vadinin orta ve ana kesimi yönü, yol isteği (1:6, 1:7) ve yönelme ile sapma karşıtlığıyla buluşunca hareketi yan kollardan ayıran bir eksen olarak duyulur (53:30). Dosdoğru dinle kurulan yön ilişkisi bu ana hattın yönetilen merkezini belirginleştirir (30:43). Aynı kelimenin bir düzeni ayakta tutan dayanak yönü de yolun dağılmadan işlemesini sağlar: sahip yalnız hattın ortasını tutmaz, onun yürünebilir kalmasının temeli gibi görünür. Yön, sapma ve dosdoğruluk burada bağımsız tetikleyicilerdir; kendi sözlük alanlarını mâliki’ye aktarmazlar. Bu bağlam resmi, mâliki’nin yerel “sahip” anlamını fiziksel bir yol nesnesiyle değiştirmez ve her soyut dayanağı kelimeye yüklemez.

Bu ana hat, sahibin yalnız sonda beklemediğini de düşündürür. {ar:مَٰلِكِ, tr:mâliki, gloss:önden giderek yön veren sahip} içindeki önden giden ve gruba yön veren unsur, {ar:ٱهْدِنَا, tr:ihdinâ, gloss:bizi yönelt} sözünün nazik rehberliği ve {ar:ٱلصِّرَٰطَ, tr:es-sırâta, gloss:ana yol} ile buluşur (1:6); {ar:يَوْمِ, tr:yevmi, gloss:varış olayı} güzergâhın vardığı ağır sonucu, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:varıştaki hesap} ise orada işleyen karşılığı verir. Hesap sahibinin yetkisi böylece sona götüren yaklaşma yolunu da yöneten bir önderlik olarak duyulabilir. Mâliki sözlükçe zorunlu olarak “rehber” demek olmaz; önderlik, yol talebinin sahiplik üzerinde açtığı ilişkidir.

Yolun varışı, geçişin nasıl işlediğini de görünür kılar. {ar:ٱلصِّرَٰطَ, tr:es-sırâta, gloss:ana yol} için verilen yutucu geçiş ve kılıç gibi kesme çağrışımları (1:6), bu varışı bir eşik hâline getirir. {ar:مَٰلِكِ, tr:mâliki, gloss:geçişi elinde tutan sahip} güzergâhı, {ar:يَوْمِ, tr:yevmi, gloss:ağır eşik olayı} geçiş zamanını, {ar:ٱلدِّينِ, tr:ed-dîni, gloss:ayrılan karşılıklar} ise eşikte birbirinden ayrılacak sonuçları taşır. Yol eski durumu içine alıp yeni sonuca geçirir; keskinlik de gidişlerin farklı sonuçlara bölünmesini görünür kılar. Ana yol, kritik olay ve hesap anlamları yerinde kalır; sırâtın bu uzak çağrışımları hesabı açıklayan bir eşik benzetmesidir.

Yolun ana merkezi ile alınmış iyiliğin hesabı aynı odakta bulunsa da tek bir resme eritilmez. {ar:مَٰلِكِ, tr:mâliki, gloss:yolun ana hattını tutan sahip} yürüyüşün eksenini tutarken (1:6, 1:7, 53:30), {ar:ٱلدِّينِ, tr:ed-dîni, gloss:borç ve cevap hesabı} o yolda alınanın cevap doğurmasını açık tutar: nimet verilmiştir ve nimetler sorulacaktır (1:7, 102:8). Biri nereye ve hangi ana hattan gidildiğini, öteki yolcunun kendi kendine yeterli olmadığını ve aldığı iyilikle nasıl bir ilişki kurduğunu gösterir. Bu iki hareket birbirini açıklar ama aynı sözlük anlamı olmaz; {ar:نَعْبُدُ, tr:na‘budu, gloss:kulluk ediyoruz} içindeki fiilî bağlılık da hesabı bugünden koparmadan yol ve borç imgelerinin her ikisini yerinde bırakır (1:5).

Bu eksenin niteliğini {ar:ٱلْمُسْتَقِيمَ, tr:el-mustaqîme, gloss:dosdoğru ve dengeli} doğruluk, denge ve eşitlikle belirler (1:6). Bu nedenle {ar:ٱلدِّينِ, tr:ed-dîni, gloss:hesap ve karşılık} bir ölçüye göre yapılan değerlendirme gibi görünür. {ar:مَٰلِكِ, tr:mâliki, gloss:ölçüyü ayakta tutan sahip} içindeki dayanak bu ölçünün sabit zeminini sağlar; mustaqîme’nin değer biçme ve fiyatlandırma çevresine uzanan çağrışımı da karşılığın gerçek ölçüsünü tayin eden değerlendirmeyi görünür kılar. Eşit ağırlık ve orantı resmi, hükmü ölçüsüz tepkiden ölçüye geri getiren bir düzeltme olarak duyurur. Bu benzetme hesabı mekanik bir makineye indirgemez; egemenlik ile merhametin daha önce kurduğu ufku da kapatmaz.

Aynı {ar:ٱلْمُسْتَقِيمَ, tr:el-mustaqîme, gloss:dosdoğru ve dengeli} sözünün kalkma ve ayağa doğrulma çevresi (1:6), {ar:يَوْمِ, tr:yevmi, gloss:büyük olay günü} ile {ar:ٱلدِّينِ, tr:ed-dîni, gloss:olayın hüküm ve karşılığı} yan yana durduğunda soyut hesabı bedenlenmiş bir kalkış olarak sezdirir. Gün yükselişin zaman ufkunu, hesap o yükselişin neden belirleyici olduğunu verir; huzurda alçalma (20:111) ve ayağa kalkma sahnesi de bu bedensel karşılaşmayı destekler (83:6). “Yükseliş” mustaqîme’nin bu bağlamdan bağımsız sözlük karşılığı değildir ve hesap gününün olağan anlamını değiştirmez; yolun sonunda insanın sahibinin önünde duracağı fikrine somut bir beden kazandırır.

Bu duruşta ayrımların korunması son bir maddi ayrıntıyla görünür olur. {ar:مَٰلِكِ, tr:mâliki, gloss:güçlü biçimde bir arada tutan sahip} içindeki sağlamlık, sonuçları taşıyan yapıyı; {ar:ٱلدِّينِ, tr:ed-dîni, gloss:ayıran hesap} o yapıda karşılıkları birbirinden seçen işlemi kurar. {ar:غَيْرِ, tr:ğayri, gloss:başka ve dışında} sınıflar arasındaki sınırı çizerken, {ar:ٱلْمَغْضُوبِ, tr:el-mağdûbi, gloss:öfkeye uğrayan} içindeki yoğunluk ve sertlik o sınırı kolayca biçim değiştirmeyen bir yüzey gibi duyurur; {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:yolunu kaybedenler} ise öfkeden ayrı kalan kayıp sonucunu taşır (1:7). Öfke taşa, egemenlik duvar örmeye dönüşmez. Maddi görüntünün açtığı şey, hesap sahibinin ayırdığı nimet, öfke ve kayıp sonuçlarının birbirine karışmadan kendi sınırlarında kalmasıdır.

</editorial_prose>
