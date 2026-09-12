# V5 reading invitation — 110:2

You are a fresh reading-invitation writer. Read the complete editorial prose
before writing. It is your sole semantic source.

Write two to four paragraphs of fluent, contemporary Turkish that reveal a
surprising reading by following one or two main channels of resonance in the
ayah. A channel is a connected background of meanings, images, actions, or
relations through which the ayah can be heard and understood differently.
Several editorial findings may together develop one channel. Summarize that
connected movement and its consequence for the ayah's main meaning, rather
than compressing findings individually. Give the reading's substance now;
the invitation comes from understanding it, not from a promise of hidden depth.

Before drafting, read the entire editorial prose and silently select the one
or two channels with the strongest interpretive consequence and enough
grounding to explain clearly. Favor channels that expand or shift what the
ayah says, the relation it establishes, or what is at stake in its action or
image. One fully developed channel is sufficient; add a second only when it
offers a distinct consequential reading that can be explained within the
invitation. No finding, channel, or major shift has an individual coverage
claim. Unselected material may remain entirely in the full commentary.

A channel may develop through grammar, sound, dialogue, a material process,
time, imagery, or a conceptual relation. Resonance is not limited to acoustic
effects, and an unusual image alone does not establish a channel. Use only
connections the editorial prose actually develops. If it supplies no such
channel, explain its strongest grounded reading without inventing connections
or surprise.

Begin inside the ayah's own words, images, actions, or relations and reveal a
selected distinctive reading in the first paragraph. Keep the plain meaning
reachable with only the orientation needed to understand the change. Do not
spend an opening paragraph on routine explanation or front-load context about
the surah, the ayah's position, or the commentary project.

For each selected channel, begin with the expression that opens it, unfold the
connected background, and show how the ayah reads or sounds against that
background. Let a detail lead into the next through an intelligible relation
or process, so the reader experiences the emerging reading. This is a movement
of thought, not a mandatory sentence pattern or one paragraph per finding.
Let the reader identify the expression being interpreted,
where any nonordinary detail comes from, and what that detail changes in the
reading. Briefly identify the word-family use, restricted form, collocation, or
context that supplies an essential added detail, and preserve the concrete
operation that makes the image work. Keep the ordinary reading and necessary
qualification clear within this explanation; do not repeat them as a fixed
formula. Preserve the particular object, process, or relation that makes this
reading distinctive, and state its interpretive consequence for the ayah as a
whole. Make intelligible what the familiar reading leaves less visible and
what the expanded or shifted reading now lets the reader understand. Preserve
the editorial's force: an exploratory possibility remains possible, while a
developed shift must not be softened into a decorative association or a
reassurance that everything means the same thing. A concrete
account of how something is carried, transformed, lost, or restored must not
shrink to a general statement about care, guidance, dependence, or goodness.
Keep the details needed to make the selected channel work; omit side findings
and shorten routine setup. If a channel cannot be explained faithfully from
the editorial prose, choose another grounded channel or reading.

When a non-focus ayah supplies a contribution used in the invitation, keep its
reference from the editorial prose beside that contribution.

Do not turn the invitation into a miniature inventory of the commentary's
conclusions, or flatten distinct channels into a broad theme to include more
material. Do not repair, extend, or supplement the editorial prose from memory
or outside knowledge.

Omit technical apparatus. Retain any qualification, source distinction, live
alternative, or boundary whose absence would change the force or meaning of a
chosen reading. Express it naturally beside the image or relation it qualifies.
Favor positive explanations of the relation between layers: what remains in
the foreground and what the resonance makes audible in the background. State
how that background reinforces, expands, or shifts the understanding of the
main meaning, with the source and degree of certainty clear. Reserve explicit
exclusions for concrete ambiguities or live counter-evidence that need them.
Repeated "this is not X" endings make a reading sound withdrawn; express the
substantive qualification through what the reading does contribute wherever
possible. Use varied, natural language rather than a repeated "second layer"
formula, and preserve the force of expansions and shifts.
Do not name branches, candidates, findings, scopes, evidence categories,
ledgers, or workflow stages, or label the prose as numbered channels. Do not
list findings serially.

Use the established `{ar:..., tr:..., gloss:...}` syntax, consistent
Turkish-readable transliteration, and short ordinary glosses. Keep Arabic
anchors beside the explanations they ground. Within a paragraph, continue with
the Turkish meaning where clear; provide the necessary local tag when a later
paragraph interprets the carrier anew. Do not place Arabic script outside a
valid tag.

Build transitions within a channel through its shared object, action, or
relation. If two channels are selected, they may occupy separate paragraphs;
do not invent a link between them. Do not praise the commentary's quality,
promise what the reader will find, manufacture suspense, recap at the end, or
add a call to action. End on an image, relation, action, or tension already
established by the selected reading.

Before finishing, compare the invitation with the entire editorial prose:
does the chosen channel reveal a consequential reading, or could the text have
been written from the ordinary translation and a modest explanation alone?
When the editorial supports a surprising channel, the latter fails this task.
Can the reader follow the opening expression into a connected background and
understand how that background expands or shifts the ayah's main meaning?
Check the selected connections against their editorial explanation: can the
reader tell where the nonordinary details come from, with the necessary
qualifications intact? Repair generic explanation, isolated curiosities, or a
compressed findings list by developing the selected channel. Do not add
omitted channels merely for coverage. Do not output this check.

Write only the invitation text to:

`_commentary/v5/editorial/s110-regular-20260911/s110/110_2/110_2.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s110-regular-20260911/s110/110_2/110_2.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
Bu âyet, 110:1'de duyurulan yardım ve açılıştan sonra görülen sonucu sahneye getirir: muhatap, insanların Allah'ın dinine grup grup girdiğini görür. Başlangıçtaki `{ar:وَ, tr:wa, gloss:ve}` bu tanıklığı önceki olaydan koparmadan taşır; önceki olayı izleyen sıralama ile o açılışın içinde gerçekleşen görme hâli aynı akışta buluşur. Bağlacın bitiştiği `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` cümleyi 110:1'de açılan şartın içine yerleştirir. Bu nedenle görülen giriş, 110:3'te gelecek hamd ve bağışlanma buyruğuna doğru ilerleyen şartın vesilesidir; cevap henüz bu cümlenin içinde kapanmaz. Buna karşılık âyetin kendi tanıklığı tamamdır: `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` görülen topluluğu, `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` süren geçişi, `{ar:فِى دِينِ ٱللَّهِ, tr:fī dīni llāhi, gloss:Allah'ın dinine}` hedefi, `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}` ise geçişin tarzını kurar. `{ar:وَرَأَيْتَ, tr:wa-ra'ayta, gloss:ve gördüğünde}` sesinde bağlaçla görme fiili tek bir açılış vuruşunda birleşir; gözün önündeki bağlı sahne kulağa da bağlı bir akış olarak ulaşır.

Bu akışın bakış noktası `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` kelimesidir. İkinci tekil kişiye yönelen etkin ve tamamlanmış görme biçimi, muhatabı başkalarını sergileyen kişi değil, 107:1'deki karşıt bakışın ve 110:1'deki ilân edilmiş yardımın ardından sonucu gören tanık olarak sabitler. Görme doğrudan bir göz tanıklığıdır; aynı zamanda göz önüne gelen hareketi kavrama yönü taşır ve nedensel bir “gösterme”ye dönüşmez. Kelimenin içindeki hemze, 107:1'deki bakıştan 110:1'deki duyuruya geçerken ilk içerik kelimesinin önünde küçük bir işitsel eşik kurar; bu ses tanıklığı yoğunlaştırır, sözdiziminin yerine geçmez. `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` önce `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` nesnesini alır, ardından `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` ile o insanların hangi hâlde görüldüğünü açar. Böylece geri kalan ifade ikinci bir rapor değil, tek görme fiilinin içeriğidir. Tamamlanmış görme ile sürmekte olan giriş yan yana gelir: tanıklık belirlenmiş bir görme anını taşırken, insanların hareketi o bakışın içinde devam eder. Tek bir muhatabın bakışı, geniş kamusal sahneyi daraltmadan çoğul hareketin ölçeğini görünür kılar.

Görülen topluluğun niteliği `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` kelimesinde yoğunlaşır. Belirli artikel taşıyan bu ad, 110:1'de aktörsüz duyulan yardımın ardından tanınabilir bir insan topluluğunu kamusal sahneye çıkarır; her bireyin kimliğini tek tek belirlemeden, küçük ve belirsiz bir kalabalık yerine toplumsal bir gövde kurar. Aynı kelime `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` fiilinin nesnesi, `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` fiilinin ise anlamca öznesidir: görülen insanlar, aynı zamanda hareket eden insanlardır. Cümle böylece yardımın sonucunu yaşayan insanları görünür kılar ve gizli bir üçüncü fail eklemez. İnsan adının çoğul giriş ve sonundaki `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}` ile birlikte ilerlemesi, tek bir topluluk görüntüsünü ardışık kollara ayırır. İçindeki ve giriş fiilindeki burunlu sesler bu hareketi son kelimenin sesine kadar örer; duyulan süreklilik toplu akışı destekler. Bu birleşim, insanları sayılan bir nesne olmaktan çıkarıp giriş sırasında yabancılığın azalabildiği ve yakınlığın kurulabildiği ilişki kuran bir gövde olarak gösterir; yakınlık ihtimali her birey için aynı iç sonucu zorunlu kılmaz.

Görülen insanların yaptığı geçiş `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` fiilinde belirginleşir. Etkin çoğul biçimin katkısı, insanların 110:1'de açılan imkânın içinden geçtiklerini ve geçişin hâlâ sürdüğünü göstermesidir. Birinci bâbın etkin yapısı onları eşiği geçenler olarak öne çıkarır; böylece insan hareketine yer açar, 110:1'deki ilahî yardımı da silmez. Sağlanan edilgen kıraat varyantı aynı sahneye kabul edilme yönünü ekler; etkin hareket ile edilgen kabul birlikte duyulur ve varyant yüzeydeki etkin okuyuşu değiştirmez. Fiil burada doğrudan nesne almaz; hareketin yönü biraz sonra gelen `{ar:فِى, tr:fī, gloss:içine}` edatıyla tamamlanır. Bu fiilin bu âyette açtığı eşik, görünür ve süren geçişi taşır; gizli kusur, saldırı veya mahremiyet gibi yönlerin devreye girmesi için ayrı bir taşıyıcı ve temas gerekir. Sıkı ünsüz dokusu ise eşiği geçme basıncını ses bakımından yoğunlaştırır. Böylece fiilin süren hareketi, 110:1'deki açılıştan 110:3'teki cevaba doğru ilerleyen canlı olayı taşır.

## Açılan Eşik

Bu canlı hareket, 110:1'deki `{ar:جَآءَ, tr:jā'a, gloss:geldi}` ile `{ar:ٱلْفَتْحُ, tr:al-fatḥ, gloss:açılış}` kelimelerinin hazırladığı imkânı görünür kılar. Gelen yardım ve kapananın açılması, burada insanların kullandığı geçilebilir bir eşiğe dönüşür; grupların içeri girmesi böylece rastgele ortaya çıkan bir kalabalık akışı olmaktan çıkar. `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` fiilinin 48:27'deki erişim yankısıyla temas etmesi, duyurulmuş imkânı yaşanmış bir geçiş gibi hissettirir. Yakınların birlikte içeri alındığı sahne (13:23) ve kullar arasına girme çağrısı (89:29), bu geçişin birden çok kişiyi taşıyan sosyal yönünü açar. Eşiğin bu bağlantıdaki katkısı, insanların geçişiyle işe yaradığı görülen sosyal ve soyut bir imkânı görünür kılmaktır; tek bir fiziksel kapı veya yalnız bir zafer açıklaması bu kapsamı tüketmez.

Bu eşiğin yönü `{ar:فِى, tr:fī, gloss:içine}` edatıyla belirlenir. Edatın katkısı, hareketi yalnızca bir şeye yaklaşma olmaktan çıkarıp o alanın içinde yerleşmeye dönüştürmesidir. Kulak önce geçişi, sonra geçişin alanını alır. `{ar:فِى, tr:fī, gloss:içine}` ile `{ar:دِينِ, tr:dīni, gloss:dinine}` tamlaması, giriş fiilinin açıkta kalabilecek hedefini kapatır; dîn sonradan iliştirilmiş bir açıklama değil, hareketin yöneldiği alandır. Aynı ilişki içeri girişi ve içeride bulunmayı birlikte taşır. Edatın uzun ön ünlüsü `{ar:فِى دِينِ, tr:fī dīni, gloss:dinin içine}` akışında yön ile alanı tek bir ses hareketinde birbirine bağlar. Ortak hedefin kurulması, 110:3'teki kişisel Rab ilişkisine geçiş için de zemin hazırlar; toplulukta görülen hareket, sonraki âyette kişisel sorumluluğa açılabilecek bir iç alan kazanır.

Bu alanın niteliğini `{ar:دِينِ, tr:dīni, gloss:dinine}` kelimesi açar. İnsanların girdiği yer, sırf bir kimlik etiketi değil, boyun eğme, bağlılık ve uyulacak kuralların kurduğu bir düzendir. Dîn'in başka bağlamlarla temasları bu düzene farklı katkılar getirir: göklerin ve yerin Allah'a boyun eğmesi (3:83) itaatin kapsamını, hesap ve karşılıkla birlikteliği (95:7) yükümlülüğü, din içinde şahitlik eden düzenli topluluk (22:78) ise ortak hayatı görünür kılar. 110:3'teki hamd ve bağışlanma buyruğu, bu katılımın toplumsal görünüşten hesap ve bakıma doğru açıldığını hatırlatır. Bu katkılar birlikte dîni inanç yolu ve kurallar bütünü, hesap karşısında yükümlülük ve insanların birlikte düzen kurduğu geniş bir alan olarak duyurur. Ortak hayatı anlatan yerleşim benzetmesi bu alanı somutlaştırabilir; yerel hedef ilişkisi dîni tek bir gerçek şehre, yalnızca son hesap gününe, ayrıntılı bir hukuk kurumuna, somut bir borca veya tek bir egemenlik dalına sınırlandırmadan bu yüzleri bir arada tutar. Tekil dîn, çoğul insanlar ve grupları tek bir hedefte toplar: çokluk girişenlere, birlik girilen alana aittir.

Girilen alanın kime ait olduğu `{ar:ٱللَّهِ, tr:allāhi, gloss:Allah'ın}` adıyla belirlenir. Cümle önce dîn hedefini verir, sonra Allah'ın adını getirerek tamlamayı tamamlar. Bu ad giriş fiilinin doğrudan nesnesi değil, `{ar:دِينِ ٱللَّهِ, tr:dīni llāhi, gloss:Allah'ın dini}` tamlamasının ikinci unsurudur; böylece insanların neye girdiği ile düzenin kime ait olduğu birbirine karışmaz. Önceki âyetteki `{ar:نَصْرُ ٱللَّهِ, tr:naṣru llāhi, gloss:Allah'ın yardımı}` ile burada yeniden duyulan Allah adı, yardımın kaynağı ile girilen alanın belirleyicisini aynı ilişkide tutar (110:1). Bu temasın katkısı, insan girişini gerçek bir hareket olarak korurken onu gözlemcinin kendi mülkü olan bir başarı olmaktan çıkarıp yardımı görünür kılan bir sonuç olarak çerçevelemektir; ilahî yardım insan iradesini silen tek neden hâline getirilmez. Allah adı bu kullanımda girilen düzenin belirleyicisi ve yönelinen sığınağın adı olarak iş görür; yemin veya doğrudan yakarış anlamı bu genitif ilişkinin içine taşınmaz. Kamusal girişteki bu adın 110:3'te `{ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin}` hitabına açılması, ortak hedef ile kişisel bakım arasındaki geçişi görünür kılar.

## Grupların Akışı

Girişin tarzını son kelime belirler: `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}`. Belirsiz kırık çoğul, kapalı bir liste vermeden birbirinden seçilebilen insan topluluklarını gösterir. Mansup hâli, ikinci bir özne kurmak yerine girişin hâlini ve tarzını açıklar; insanlar girer, gruplar hâlinde girerler. Sonundaki tenvin ve açık `-an` sesi çoğulluğu belirli bir sayıya kapatmadan âyeti açık bir hareketle bitirir. Bu kelimenin çevresindeki yankılar farklı katkılar getirir: 38:59'daki sert giriş grup hareketinin karşıtını, 78:18'deki toplu dalga görüntüsü kalabalık hareketinin yankısını, 22:27'de çağrıya karşılık gruplar hâlinde geliş ise ilerleme ritmini görünür kılar. Bu âyette 38:59'un düşmanca zorlaması ve 78:18'in tamamlanmış toplu görüntüsü kendi bağlamlarında kalır; burada onların katkısı grup grup girişin biçimini belirginleştirmektir. Buradaki etkin ve sürmekte olan giriş, grupların uyumlu bir varış içinde ilerlediğini duyurur; girenlerin niyeti hakkında hüküm vermez. Son kelime 110:3'teki kapanışa doğru çoğulluğu taşırken, ses i'rabın ve olağan gruplar anlamının yerini almaz.

Grupların bu ilerleyişinde geniş bir geçiş alanı imgesi belirir. İki yükselti arasındaki açıklık gruplara genişlik, `{ar:فِى, tr:fī, gloss:içine}` edatı dışarıdan içeriye yön, `{ar:دِينِ, tr:dīni, gloss:dinine}` kelimesi düzenli bir iç alan, `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}` ise bu açıklıktan geçen ardışık kolları verir. Bu dört katkı birleşince 110:1'deki açılış, sonuç listesine eklenmiş bir başlık olmaktan çıkar; içinden geçildiği görülen bir eşik olarak işler. Geçişin ölçüsü elde tutulan bir nesne veya tarif edilmiş bir arazi değildir; açılan yerin işe yaradığını, içinden geçen toplulukların hareketi gösterir. Arazi ve şehir burada kelimelerin düz çevirisi değil, insan gruplarının geniş bir yaklaşımdan düzenli bir içeriye alınış biçimini görünür kılan sınırlı bir benzetmedir.

Aynı hareket, mekân imgesinden ayrı bir temasla suyun bırakılıp kanallara dağılışına da yaklaştırılabilir. 110:1'deki yardım yağmur ve ferahlık gibi, açılış da bir çıkıştan suyun fışkırması gibi duyulur. `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` fiilinin suyu başkaları için çekip ulaştıran yönü, `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` fiilinin gerçek giriş hareketiyle ve `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}` kelimesinin yayılan kollarıyla temas eder (110:1). Gruplar böylece yeni açılmış kanallara dağılan, yön bulmuş bir su akışı gibi art arda görünür; statik bir sayı yerine salınmış ve yayılımlı bir hareket belirir. Bu benzetme insanları suya, dîni suya veya girişi fiziksel bir su başına dönüştürmez; yalnızca toplu girişin serbest bırakılmış, yönlendirilmiş ve genişleyen biçimini açıklar.

## İçerideki Hayat

Geçişin yönü ve akışı, dîn alanında başlayan hayatın nasıl sürdüğünü de düşündürür. `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` sonradan bir topluluğa katılan yeni gelenlerin hareketini, `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` ise mevcut insan gövdesini taşır. Yeni gruplar bu gövdeye yaklaştıkça yabancılık azalabilir ve aidiyet kurulabilir; bu ihtimal her kişide aynı duyguyu zorunlu kılmaz. `{ar:دِينِ, tr:dīni, gloss:dinine}` kelimesinin tekrarlarla yerleşen alışılmış davranış ve sürekli yöneliş tarafı açıldığında, giriş bir anlık beyanın değil yaşanan bir pratiğin alanı olur. İnsanlar ve gruplar girdikçe ortak düzenin toplumsal bileşimi de değişir; böylece bireysel dönüşümün yanında parçaları birbirine geçen daha geniş bir katılım görünür. Dîn'in düzenli yaşanan bir yerleşim gibi hissedilmesi ortak hayatı somutlaştırır, fakat gerçek bir kent kurmaz. 110:3'teki `{ar:رَبِّكَ, tr:rabbika, gloss:senin Rabbin}` sözü bu oluşun onarım, yetiştirme ve tamamlanma yönünü açar. Aynı âyetteki `{ar:كَانَ, tr:kāna, gloss:olagelmiştir}` zaman içinde süren oluşu, `{ar:تَوَّابًا, tr:tawwāban, gloss:dönüşü kabul eden ve döndüren}` ise yeniden yönelmeyi, doğrultmayı ve hazır hâle getirmeyi düşündürür. Böylece varış, girişten sonra yönelişin yeniden kurulabildiği bir erişim ve devam ritmi kazanır; bu, tarihsel olayın tekrarlandığı hükmü değil, içerideki yönün yenilenebileceği ihtimalidir.

## Görünür Sonucun Sınırı

Görülen girişin kamusal gerçekliği, içerideki durumu bütünüyle tüketmez. `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` dışarıdan görülen yüzü ve eldeki belirtiyi, `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` göz önündeki insan topluluğunu, `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` ise içeri yerleşmenin gözle tamamlanmayan tarafını duyurabilir. Girişin içte kalan boyutunda saklı bir durum ve içten bozan bir kusur ihtimali bulunabilir; bu ihtimal belirli insanlara teşhis veya aldatma hükmü olarak yüklenmez. Dış görüntünün iç bütünlüğü kendiliğinden kanıtlamadığını gösteren bağlar 4:142 ve 67:27'de görünür; bu bağlar gözün eriştiği dış yüzün sınırını belirler. Ardından gelen `{ar:ٱسْتَغْفِرْهُ, tr:istaghfirhu, gloss:ondan bağışlanma dile}` buyruğu bu sınırda örtme, koruma, sonuçlardan esirgeme ve onarma yönünü devreye sokar (110:3). Bağışlanma ile rahmete alınmanın birlikte istendiği yakarış (7:151), topluluk dîne girerken beraberinde taşıyabileceği görünmeyen kırılganlıklar için kabulün ardından da koruyucu bakım bulunduğunu düşündürür. Böylece dışarıdan görülen hareket gerçek kalır; içeride korunacak ve yetiştirilecek bir hayat için alan açık tutulur.

Bu sınır, tanıklığın kendisini de bir sorumluluk anına çevirir. `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` ile `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` birlikte görülen kalabalığı zihinde bir görüşe ve değerlendirmeye taşıyabilir; görünür bir başarı başkaları görsün ve beğensin diye sergilenen bir manzaraya kayabilir. Gösterilmek için yapılan davranış (107:6) ve insanların önünde riya görüntüsü (4:142) bu ihtimalin somut sınırlarını gösterir. Bu temas muhatabın riya yaptığına dair suçlama kurmaz; yalnızca gözlenen olayın övgüyü kendine mal etme riskini açar. Hemen ardından gelen `{ar:سَبِّحْ, tr:sabbiḥ, gloss:tenzih et}` emri sahneyi tanığın kendisine yazmaktan arındırır, `{ar:بِحَمْدِ, tr:bi-ḥamdi, gloss:hamdiyle}` ise övgünün yönünü doğru kaynağa çevirir (110:3). Sonraki emir kendi ibadet buyruğu olarak da yerinde kalır; görme böylece bilgi edinmenin yanında gördüğü başarı karşısında bakışını düzenleme anı olur.

Bakışın bu dönüşü, kalabalığı tanığın önünde duran sabit bir nesne olmaktan çıkarıp tanıklığın içinde oluşan bir görüntüye taşır. `{ar:رَأَيْتَ, tr:ra'ayta, gloss:gördüğünde}` görünür ve yansıtıcı yüzey çağrışımını, `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` ise görüş alanında, hatta göz bebeğinde beliren küçük insan görüntüsünü düşündürür. Bu iki katkı birleşince kalabalık, gözleyen kişinin sahip olduğu bir nesne olmaktan çok onun bakışında oluşan bir görüntü gibi belirir. Ardından gelen `{ar:سَبِّحْ, tr:sabbiḥ, gloss:tenzih et}` bu görüntünün tanığın payıymış gibi yazılmasını engelleyen etik dönüşü sağlar (110:3). Bu figürasyon, kelimelerin sözlükte doğrudan ayna veya göz bebeği demesi değildir; görme ile görülen insan kitlesinin buluşmasından doğan, tanığın bakışını değiştiren sınırlı bir benzetmedir. Görünen başarı ile içerideki hükmün açık kalması, bu benzetmenin de taşıdığı sınırdır.

Bu görüntüden sonra dikkat, grupların bütününe ve onların içte kalan yanına döner. `{ar:ٱلنَّاسَ, tr:an-nāsa, gloss:insanları}` insan türünü ve ortak gövdeyi, `{ar:أَفْوَاجًا, tr:afwājan, gloss:gruplar hâlinde}` sayılabilir ve ayırt edilebilir toplulukları taşır; `{ar:يَدْخُلُونَ, tr:yadkhulūna, gloss:girerler}` ise her grubun kendi iç yüzünü bu görüntü içinde tutar. Ardışıklık yerinde kalırken, `{ar:ٱسْتَغْفِرْهُ, tr:istaghfirhu, gloss:ondan bağışlanma dile}` emrinin örtme ve koruma yönü grupları ayrı ayrı görünen sayılar olarak bırakmaz, onları bütünüyle gözetilen bir kalabalık içinde toplar (110:3). Örtü burada kalabalıkla eşitlenmiş bir sözlük anlamı değildir; görünür hareketin biçimini koruyarak bakımın görünmeyen içlere de ulaşmasını sağlayan bağlantıdır. Böylece her grubun dışarıdan görülen gelişi kendi düzenini korur, fakat o geliş bağışlanma ve rahmet ufkunda korunacak bir iç hayata açılır.

</editorial_prose>
