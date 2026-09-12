# V5 reading invitation — 100:11

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

`_commentary/v5/editorial/s100-regular-20260911/s100/100_11/100_11.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s100-regular-20260911/s100/100_11/100_11.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
100:11, (100:9, 100:10)'da mezarların altüst edilmesi ve göğüslerde saklı olanların ortaya çıkarılmasıyla açılan sahnenin ardından, bu sahneyi açıklayan sabit hükmü verir: `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` `{ar:يَوْمَئِذٍۢ, tr:yawmaʾidhin, gloss:işte o gün}` `{ar:لَّ, tr:la, gloss:vurgulu yüklem öneki}` `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}`; onların Rabbi o gün onlardan elbette haberdardır.

Bu cümlede `{ar:إِنَّ, tr:inna, gloss:elbette}` önceki açılma ve hesaplanma vaktine cevap verir gibi işitilebilir; ancak cümleyi önceki sözlere bağlı bir aktarıma dönüştürmeden kendi isim cümlesini başlatır. Böylece (100:9, 100:10)'daki sahneyle bağ korunur, hükmün bağımsız kesinliği de ayakta kalır. İnna'nın başındaki çift ünsüzlü tutulma, özne daha duyulmadan iddiayı sıkılaştırır; ilerideki `{ar:لَّ, tr:la, gloss:vurgulu yüklem öneki}` ile son `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` birlikte hükmü iki uçtan kavrayan bir vurgu çerçevesi kurar.

`{ar:إِنَّ, tr:inna, gloss:elbette}` yönettiği özne hemen `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ile yerleşir. Araya `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` ve `{ar:يَوْمَئِذٍۢ, tr:yawmaʾidhin, gloss:işte o gün}` girdiği halde okur bu özneyi son yükleme kadar taşır. Önceki ayetlerde olay olarak görünür hale gelen şeyin ardından yeni bir olay değil, o içerikle ilişkili Rab adlandırılır. Rabbahum'un sahip olma, yönetme, düzenleme ve gözetme ilişkisi, sonradan gelen bilginin dışarıdan tutulmuş bir kayda değil, bu insanlar üzerindeki ilişkiye dayandığını duyurur; aynı ses gövdesi `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ile buluşunca içte yoğunlaşmış bir öz veya tortu rengine de açılır.

`{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` bi edatıyla hum zamirini tek bir kısa birimde birleştirir. Bu bağlı zamir, insanları `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgisinin alanına sokar; belirsiz bir “bir şey hakkında” ilişkisi değil, bu insanlar hakkındaki bilgidir. Aynı hum, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinde Rabbe ait olanları, bihim'de ise hakkında hüküm verilenleri gösterir. Grup sabit kalırken zamirin dilbilgisel rolü sahip olunan ilişkiden bilgiye konu olan alana döner; (100:9, 100:10)'da mezar ve göğüsten açığa çıkan içerik böylece yeniden belirli bir insan topluluğuna bağlanır.

`{ar:يَوْمَئِذٍۢ, tr:yawmaʾidhin, gloss:işte o gün}` işaretini (100:9, 100:10)'daki diriliş ve açığa çıkma sahnesine geri çevirir. Bu, herhangi bir gün ya da belirsiz bir dönem değil, mezarların çevrilmesi ve göğüslerdekilerin görünür olmasıyla tamamlanan vakittir. Yawmaʾidhin yeni bir özne veya nesne eklemez; bilginin hangi anda hükme bağlandığını gösteren zaman zarfı olarak cümleye yerleşir. İç kesintisi ve tenvinli sonu, `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` ifadesindeki insan alanından belirlenmiş güne, oradan da son bilgi sıfatına geçişte kısa bir işitsel eşik oluşturur.

Zaman zarfından sonra gelen `{ar:لَّ, tr:la, gloss:vurgulu yüklem öneki}` doğrudan `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` yüklemine bağlanır. Kesinlik Rabb'e, `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` ifadesine veya zamana değil, son bilgi niteliğine yönelir. La-khabīrun, (100:6, 100:7, 100:8)'deki vurgulu insan hükümlerinin ardından gelen son halka gibi çalışır; la ve son tenvin, yüklemi çift vurgulu bir kapanışa taşır. Khabīrun nominatif cümle yükleminde çözülür: `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` özneyi, bihim insan alanını, `{ar:يَوْمَئِذٍۢ, tr:yawmaʾidhin, gloss:işte o gün}` zamanı taşır ve cümlenin haberi, haber verdiği bilme niteliğinde sonlanır.

Bu dilbilgisel kapanış, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ilişkisinin yetkisini `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgisinin içe ulaşan yönüyle birleştirir. (1:2)'deki geniş Rablik çerçevesi, bu bilen öznenin insan grubunu zaten kuşatan Rab olduğunu duyurur; (17:96)'daki tanıklık ve uzman farkındalığı ise bilginin kişilere dönük niteliğini belirginleştirir. Bu birleşme, insanî bir soruşturma yöntemi kurmadan, kendi ilişkisi içindeki insanların gerçek durumunu bilen yetkili bir tanımayı öne çıkarır; (100:6)'da Rabbe karşı tavır olarak görünen bağ, (100:11)'de insanlar hakkındaki kesin bilgiye döner.

`{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin bakım ve yönetim yüzü zamana yayıldığında, bilginin bir anda edinilmiş bir sonuçtan çok oluşumun içindeki tanışıklık olarak duyulması mümkün olur. (14:25)'te Rabbin izniyle süren meyve, yetişmenin devamlılığını; (17:30)'da ölçülü rızık ve bilen özne, verilenle karşılık veren insanlara uzanan uzun ilişkiyi açar. (100:9, 100:10)'daki “o gün” bu geçmişi tek bir varışta toplar. Bakım ile uzmanlığın bu yan yana gelişi, süreçle yakın tanışıklık kuran bir bakım temelli uzmanlık olarak duyulur; bu yakınlık uzaktan gözetim imkânını kapatmaz. Bu, bilginin sonradan kazanıldığı bir nedensellik iddiası değil; bakımın, karşılığın ve tamamlanmış sonucun aynı hüküm içinde görünür hale gelmesidir.

Buradan `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ile `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` arasındaki temas bir yetiştirme ve ürün imgesine de açılır. (14:25)'teki süren meyve ve (22:63)'te yağmurdan sonra görülen yeşil büyüme, bakılmış bir sürecin ne verdiğini düşünmeye izin verir. Khabīrun'un gevşek, alçak ve su tutan zemin; üründen yarı, üçte bir veya belirli bir pay alan çiftçi ya da ortakçı çağrışımı bu sonucu somutlaştırır. Daha dar biçimiyle bu tarım bağlantısı, bakım gören sürecin ne verdiğini bilen bakıcıyı öne çıkarır; tohum, çorak arazi ve hasat kökü ise bu bağlantıya eklenen benzetmeli renkler olarak kalır.

## Bağın ve toplanmanın biçimleri

`{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin ilişki yüzeyi, bir iş için bir araya gelen tarafların **bağlayıcı sözleşme ve ittifak** içinde tutulduğu bir görüntü kurar. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` başkasına destek olmak üzere katılmayı, `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` kurulmuş bağı sıkılaştırmayı duyurur. (100:5, 100:6, 100:8)'deki merkez, Rabbe karşı tavır ve iyilikle bağlanma bu sırayı besler: önce taraflar belirir, sonra yükümlülük ve son olarak süreklilik veren sıkılık gelir. (100:1)'deki açılış yemini bu ilişkiye yalnızca zayıf bir komşuluk verir; okuma, Rabbahum'un olağan Rablik anlamını koruyan bağlayıcı bir ilişki görüntüsü olarak kalır.

Aynı toplanma hareketi bu kez **sığır ve sürü topluluğu** olarak görünür. `{ar:أَثَرْ, tr:athar, gloss:iz}` boğayı ve erkek sığırı, `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` dağınık parçaların karışık topluluğa dönüşmesini, `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` küçük veya kısa bedenliyi, `{ar:صُبْحًا, tr:ṣubḥan, gloss:sabah}` ise sabah yerinde kalan deveyi çağrıştırır. (100:3, 100:4, 100:5, 100:6, 100:8)'deki sabah, iz-toz, merkez, Rabbe karşı tavır ve sevgi-iyilik sahneleri bu farklı beden ve hareketleri aynı sınırlı sürüde buluşturur. Böylece `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin bilgisi, farklılıkları silmeden topluluğu kuşatan bir tutma olarak duyulur.

Toplanmanın daha sıkı maddi biçimi **düğüm, bağ ve kelepçe**dir. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` elleri boyna doğru bir kısıt gibi toplar; `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` bu bağı sertleştirir. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` yüzeyinin gereksinim, düğüm ve iyilik gibi ayrı duyuluşları aynı sözlüğe kapatılmadan yan yana durur. (100:5, 100:6, 100:8)'deki toplanma, Rabbe karşı tavır ve iyilik, ittifaktaki ilişkiyle uzuvları sınırlayan kelepçeyi aynı maddi hareket çevresinde buluşturur.

Bu toplanma insanlara yöneldiğinde **çokluk, buluşma yeri ve çağrı** olur. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` dağınık parçaları tek bütünde tutar; buluşma yeri ortak alanı, buluşma günü zamanı, çağrı ise hareketin başlangıcını kurar. `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` hazır bulunmayı tanıklıkla birleştirir. (100:5, 100:6, 100:7)'deki merkez, Rabbe karşı tavır ve tanıklık, “onlar hakkında bilme”yi yalnız dağınık bireylere değil, tanıklık için bir araya gelmiş topluluğa açar.

## Zemin, kap ve hareket

İnsan topluluğunun böylece bir araya gelmesinden sonra dikkat, içeriğin nerede tutulduğuna döner. `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` gevşek, yumuşak ve alçak zeminin suyu alıp bir havzada tutmasını; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bolca toplanmış suyu; `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` ise durulmuş suyu veya içine ıslanan şeyi düşündürür. `{ar:يَعْلَمُ, tr:yaʿlamu, gloss:biliyor}` ile taşınan büyük birikim imgesi, zeminin alması ve suyun toplanmasıyla dağınık hareketin altında korunan bir bütüne dönüşür. (100:4, 100:6, 100:9)'daki iz, Rab ilişkisi ve mezarların açılması bu tutulumun yerel dayanaklarıdır.

Bu zemin, hareketin dağıttığı şeyi taşıyan **alıcı çevre** olarak da duyulur. (22:63)'te suyun yeşil büyümeyi görünür kılması ve (17:30)'da rızkın ölçülü sunulması, çevreyi hareketin dağıttığı şeyi taşıyan yardımcı bir alan haline getirir. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bakım ve tedarik ilişkisini, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise bu alanın neye dönüştüğünü bilen tanışıklığı taşır. Bu yardımcı çevre resmi, Rab ve haberdarlık hükmünün maddi bir tutulumla nasıl duyulabildiğini açıklar; arazi, su ve bulut bağlantısı bu özel çağrışımın sınırında kalır.

Alıcı yüzeyin karşısında **yumuşak havza, düz ova ve sert zemin** ayrımı belirir. `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` sert veya düzensiz yeri, `{ar:قُبُورِ, tr:qubūr, gloss:mezarlar}` gizlenmeyi ve içe gömülmeyi, `{ar:كَنُودٌ, tr:kanūdun, gloss:nankör}` kısır ve ürün vermeyen araziyi, `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` düz kil düzlüklerini düşündürürken `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` suyu kabul eden yüzeyle karşılaştırmayı taşır. (100:1, 100:4, 100:9)'daki koşu, iz-toz ve açığa çıkarma, suyun tutulduğu ya da sertlik ve gömülme içinde dışarıda kaldığı iki sonucu görünür kılar; koşu yemini bu karşıtlığın yalnızca uzak bir komşuluğudur.

Tutulan hacim bir **saklama ve sunma kabı** biçimi de alır. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` doluluğu, `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` büyük küpü veya desteği, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` geniş su tulumunu, `{ar:قَدْحًا, tr:qadḥan, gloss:çakıp tutuşturma}` içecek kabını, `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` ise durgun ve tutulmuş içeriği taşır. Hacim önce korunur ve taşınır, sonra içilebilir bir pay olarak sunulur. (100:2, 100:4, 100:5, 100:8)'deki ateş, iz-toz, merkez ve iyilik bu kap hareketine farklı uzaklıklardan eşlik eder; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ve khabīrun böylece saklananı muhafaza edip erişilebilir kılan iki uç olarak duyulur.

Kabın tuttuğu yoğun öz, **kesik süt, şurup, bal ve ikramlık yiyecek** görüntüsüne geçer. `{ar:أَثَرْ, tr:athar, gloss:iz}` kurutulmuş kesik süt topağını, koyu meyve özünü veya yağ dibindeki tortuyu; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bu yoğun maddenin ilişki içindeki yerini; `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` peteğin içindeki balı; `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` hazırlanmış yiyeceği, kesilmiş eti veya soğutulmuş sütü çağrıştırır. Yoğunlaşan madde depolamadan ikrama geçer: içecek ya da yiyecek olarak karşılanabilir hale gelir. (100:6, 100:7, 100:8)'deki Rabbe karşı tavır, tanıklık ve iyilik, saklanan özün ikrama çevrilmesiyle bilgi hükmüne karşılık hareketi ekler.

Yüzeydeki birikim **bulut, tabaka, kabarcık ve dalga** olarak da yükselir. `{ar:أَثَرْ, tr:athar, gloss:iz}` dışa yayılan tortuyu, `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` kabarcıklanmayı, kabarmayı ve dalgalanmayı, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` üst üste binen veya aşağıda asılı duran katmanlı bulutu düşündürür. Nem ve hareket görünür birikimler kurarken `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` dağınık izlerin biçim kazanmasını bilen nitelik olarak duyulur. (100:4, 100:6, 100:8)'deki toz, Rab ilişkisi ve iyilik bu yüzey görüntüsünü taşır; bu bulut, bu işlemlerin oluşturduğu yardımcı yüzey biçimidir ve zorunlu bir meteorolojik gönderme olarak kurulmaz.

Bu yüzey hareketinin altında **hidrolik tutulum** belirir. `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` üstte yükselen tozu ve durulmuş suyu aynı sahnede yan yana getirir; alçak zemin suyu alttan tutar, katmanlı bulut yukarıda asılı kalır ve türbülansın altında saklanan bir birikim duyulur. (100:4, 100:9)'daki iz-toz ve mezarların açılması, hareketin dağıttığı şeyin sonra yeniden görünür olmasına bağlanır. Bu bağlantı, naqʿan için su ve Rabbahum için bulut anlamı çıkarmaktan çok, maddi imgelerin `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgisini görünür hareket altında korunan içeriğe uzatmasını somutlaştırır.

Sınırlı bir kümenin elde tutulması, **elde kura okları ve kap** görüntüsünü kurar. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` elin çukur yüzeyini ve bir araya getirilmiş nesneleri, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` deri veya bezden okları ve çubukları tutan kabı, `{ar:قَدْحًا, tr:qadḥan, gloss:çakıp tutuşturma}` kaptan ya da kuyudan çekme hareketini ve ok sapını düşündürür. Çokluk önce kapta tutulur, sonra el seçer ve tek bir sonuç çıkar. (100:2, 100:5, 100:6)'daki ateş, merkez ve Rabbe karşı tavır bu seçimin çevresini kurar; sonuç, kaybolmamış imkânların bir karara bağlanması rengini alır.

Aynı sınırlı kap bu kez **yörüngelerin ok torbası** olarak uzaklaşır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ile `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}`, dışarı fırlatılmış çoklu güzergâhların tek bir günde toplanmasını; `{ar:قَدْحًا, tr:qadḥan, gloss:çakıp tutuşturma}` ok sapını; `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` dağınık yolların tek bütünde tutulmasını taşır. (100:2, 100:5)'teki ateş ve merkez, bu yerel toplama fikrine temas eder. Ok torbası, sınırlı bir benzetme içinde seyrin bilgisinin kaybolmamasını düşündürür; bu bağlantı kader ve zorunlu belirlenim meselesine taşınmadan burada tamamlanır.

## Büyüme ve karşılık

Kapta tutulan içeriğin zamanla gelişmesi, **tohum, hurma ve yeşil filiz** zincirini açar. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` tohumdan yetişen, türü belirlenmemiş hurma ağaçlarını; `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` taşınan çekirdeği; `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` hurma üzerindeki ilk meyveyi; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` yeşil bitkiyi; `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` yaz otunu; `{ar:قَدْحًا, tr:qadḥan, gloss:çakıp tutuşturma}` narin bitki uçlarını çağrıştırır. Çekirdek, ilk meyveye, yeşil ota ve filize doğru bir yetişme zinciri kazanır. (100:1, 100:2, 100:5, 100:6, 100:8, 100:10)'daki koşu, ateş, merkez, Rabbe karşılık, iyilik ve içlerin açığa çıkması bu zincire farklı temaslar verir; ilk ayetin yemini burada yalnızca sınırlı bir karşı-kanıttır.

Bu gelişim **gebelik, doğum işaretleri ve olgunluk** olarak da duyulur. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` gebeliğin tutulmasını, bekâretin korunmasını ve dağılmadan bütünlüğü; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` başlangıçtaki yenilik ve tazeliği; `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` tam olgunluk ve gücü; `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` doğum ve ergenlikteki boşalma eşiğini taşır. (100:5, 100:6, 100:7, 100:8)'deki merkez, Rabbe karşı tavır, tanıklık ve sevgi-iyilik, başlangıçtan doğuma ve olgun güce ilerleyen görüntüyü besler. Bedensel ayrıntı burada, Rabbahum ve `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ifadesinin olağan anlamını taşıyan bağlamsal bir benzetme olarak kalır; yeni bir gramer iddiası kurmaz.

Toplanma ve gelişme **birleşme, soy ve bakım bağı**na dönüşür. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` cinsel birleşmeyi ve gebeliğin tutulmasını, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` gözetileni eksikten tamamlanmışa yetiştiren bakımı, `{ar:مُورِيَٰتِ, tr:mūriyāti, gloss:ateş çıkaranlar}` ise çocuktan sonra gelen torunu ve bakım yoluyla kurulmuş aile bağını düşündürür. İlişki birleşmeden nesle, nesilden bakıma doğru sürer. (100:2, 100:5, 100:6)'daki ateş, merkez-toplanma ve insanın Rabbe karşı tavrı bu sürekliliğe temas eder; aile ve cinsel birleşme burada bakım ve nesil hareketinin daha uzak çağrışımını taşır, hedef cümlenin gramerini genişletmez.

Koşunun karşı kutbunda **ikamet ve hareketsiz hayvan** görüntüsü belirir. `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` yorgunluktan yerinde sabitlenmiş deveyi, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bir yere bağlanıp kalmayı, `{ar:صُبْحًا, tr:ṣubḥan, gloss:sabah}` sabah yerinde kalan hayvanı, `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` ise sert veya düzensiz zemini getirir. (100:1, 100:3, 100:6, 100:8)'deki koşu, sabah, Rabbe karşı tavır ve iyilik, hareketin durup ikamete dönüşmesini kurar; Rabbahum'un ilişki yüzü de ayrılmama ve sürme olarak belirginleşir.

Gelişen zeminle hareket arasındaki bağ, **ekim, sulama ve yetiştirme** işlemlerinde somutlaşır. `{ar:أَثَرْ, tr:athar, gloss:iz}` toprağı kaldırıp karıştırmayı, `{ar:مُغِيرَٰتِ, tr:mughīrāti, gloss:akın edenler}` sağlama, sulama ve onarımla yarar üretmeyi, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bakım ilişkisini, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise ürünün ne verdiğini bilen çiftçi veya pay alan ortakçıyı taşır. (100:3, 100:4, 100:6)'daki sabah, iz-toz ve insanın Rabbe karşı tavrı, hareketin toprağa ve yetiştirmeye çevrilmesini destekler. Böylece önceki ürün imgesi, sulama ve onarım işlemleriyle nasıl ayakta tutulduğunu kazanır.

Koşu ve soluk aynı zamanda **bedensel tanı benzetmesi**ne izin verir. `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` hızlı hareketi, `{ar:ضَبْحًا, tr:ḍabḥan, gloss:soluklanma sesi}` işitilebilir soluklanmayı, `{ar:مُورِيَٰتِ, tr:mūriyāti, gloss:ateş çıkaranlar}` içi tüketen veya akciğeri etkileyen hastalığı düşündürür. Dışarıdan duyulan çaba belirtilerinden içerideki kaynağı okuyan `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` uzmanlığı belirir. (100:1, 100:2)'deki koşu ve ateş bu benzetmenin temas noktalarıdır; hastalık bağlantısı bu bedensel görüntüyle sınırlı kalır ve Rabbe yüklenmez; bu dal uzak ve keşifseldir.

Verilen iyiliğin karşılığı **ihsan ve bozulmuş karşılık** görüntüsünü kurar. `{ar:خَيْرِ, tr:khayr, gloss:hayır ve servet}` iyilik ve bağışı, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` sahip olma ve yönetme yetkisini, `{ar:مُغِيرَٰتِ, tr:mughīrāti, gloss:akın edenler}` sağlama, sulama ve düzeltmeyle yarar üretmeyi, `{ar:كَنُودٌ, tr:kanūdun, gloss:nankör}` ise bu iyiliği kesen nankör ve verimsiz karşılığı taşır. (100:3, 100:6, 100:8)'deki sabah, Rabbe karşı tavır ve sevgi-iyilik, verilenin nasıl karşılıksız bırakıldığını gösterir. Bilgi böylece yalnız failin kimliğini değil, iyiliğin ilişki içinde uğradığı dönüşümü de kapsar.

Bu dönüşüm **yetiştirme karşısında kopuş** olarak keskinleşir. `{ar:إِنسَٰنَ, tr:insāna, gloss:insan}` aşinalık ve insan alanını, `{ar:رَبِّ, tr:rabbi, gloss:Rab}` eksikten tamamlanmışa yetiştirmeyi, `{ar:كَنُودٌ, tr:kanūdun, gloss:nankör}` kesme, ayrılma ve kısır kalmayı duyurur. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ile `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bu bakım bağının başarısız karşılıklılık boyunca da bilinir kalmasını taşır. (100:6)'daki insanın aynı Rabbe karşı tavrı, bakımın cevapsız bırakılmasına rağmen ilişkinin sürmesini görünür kılar; kısırlık ve kesilme bu ilişkiyi açıklayan atfedilmiş renklerdir.

İçte kalan karşılık, **içteki bağ düğümü** olarak duyulur. `{ar:كَنُودٌ, tr:kanūdun, gloss:nankör}` iyilik ve sevgiye karşı nankörlüğü, `{ar:حُبِّ, tr:ḥubb, gloss:sevgi}` kalbe yapışan sevgiyi ve karanlık iç çekirdeği, `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` bağın sıkılığını ve cimriliğin yoğunluğunu, `{ar:خَيْرِ, tr:khayr, gloss:hayır ve servet}` iyiliği taşır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ile `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bu düğümlenmiş tutmanın içten bilinmesini bir arada tutar. (100:6, 100:8)'deki Rabbe karşı tavır ve sevgi-iyilik, serbestçe karşılık vermesi beklenen iyiliğin içte sahiplenici bir sıkışmaya dönüşmesini açıklar; Bu bağlantı, kalbin anatomisini açıklamak için değil, bağlanma ve içte sıkışmayı görünür kılmak için çalışır.

Bu ilişki dış bağlamda **ilişkisel sorumluluk** kazanır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` bağlayıcı iyilik ilişkisini, (14:7)'deki şükür ve inkâr karşıtlığı ile (102:8)'de nimetin sorgulanmasını aynı sorumluluk alanında buluşturur. Alınan iyilik ve verilen karşılık, son bilgiyi uzak bir davranış kaydından ilişkinin uğradığı yarayı bilen tanımaya çevirir. Bu temasın kapsamı, resmî bir ahit ilanından ziyade iyilikle beslenen bağın içindeki nankörlüğü görünür kılan sınırlı bir sorumluluk ilişkisidir.

## Açığa çıkan bilgi

İçte düğümlenen karşılığın bilgisi, **tanıklık, bildirim ve söz** hareketiyle dışarı çıkar. `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgi edinme ve iç yüzünü tanıma yönünü, `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` bilgiden gelen tanıklığı ve tanıklık eden dili, `{ar:يَعْلَمُ, tr:yaʿlamu, gloss:biliyor}` ise şeyin açığa çıktıkça bilinmesini taşır. (100:7, 100:9)'daki tanıklık ve mezarların açılması, saklı olayın bilen tanığın sözü ve görünür hale gelen sahneyle bildirilmesini kurar. Bilgi bu hareket içinde bildirime dönüşürken, ayetin kendi Rab ve haberdarlık hükmü yerinde kalır.

Bilgiye ulaşmanın başka bir yolu **algı, bilgi ve uzmanlık**tır. `{ar:إِنسَٰنَ, tr:insāna, gloss:insan}` görme, duyma veya hissetmeyle fark etmeyi; `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bir şey hakkında bilgi edinmeyi, bildirmeyi ve deneyerek iç yüzünü tanımayı; `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` Tanrı bilgisiyle ve dinî konularda sağlam bilgiyle yetişmiş bilgin imgesini; `{ar:يَعْلَمُ, tr:yaʿlamu, gloss:biliyor}` ise açıklığa çıktıkça bilmeyi taşır. (100:6, 100:9)'daki insan ve açığa çıkarma, duyudan fark etmeye ve oradan iç bilgiye ilerleyen kavrayışı destekler. Bu uzmanlık rengi, ilahî özneyi insanî bir araştırmacıya dönüştürmeden bilgiyi derinleştirir.

Bu bilme yolları **epistemik kipler** olarak yan yana durur. `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` insan alanını, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise içten sınanmış tanışıklığı taşır. (17:96)'daki hazır bulunma ve uzman farkındalığı, (11:5)'te gizlenen göğüslerin bilinmesiyle aynı kapanışta buluşur. Hazır bulunma, olayın açığa çıkması ve iç yüzü tanıma birbirine indirgenmeden korunur; kaynak metin bunlar arasında zorunlu bir üstünlük sırası kurmaz.

İzlerin bilgiye dönüşmesi, **adli etki zinciri** gibi okunabilecek bir hareket kurar. `{ar:مُورِيَٰتِ, tr:mūriyāti, gloss:ateş çıkaranlar}` gizli ateşi, `{ar:قَدْحًا, tr:qadḥan, gloss:çakıp tutuşturma}` vurarak çıkan kıvılcımı, `{ar:صُبْحًا, tr:ṣubḥan, gloss:sabah}` şafak eşiğini, `{ar:أَثَرْ, tr:athar, gloss:iz}` geride kalan izi, `{ar:نَقْعًا, tr:naqʿan, gloss:toz bulutu}` yükselen tozu, `{ar:وَسَطْ, tr:wasat, gloss:orta}` merkezde yerleşmeyi ve `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` dağınık etkilerin toplanmasını duyurur. (100:2, 100:3, 100:4, 100:5)'teki ateş, sabah, iz-toz ve merkez sırası, gizli nedenin belirti üretip iz bırakmasını ve izin merkezde toplanmasını düşündürür; `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` hem nedeni hem iz bırakan kişiyi bilen nitelik olarak bu zinciri tamamlar. Bu görüntü, atfedilmiş ve nitelikli bir okuma olarak zinciri derinleştirir; tozun izi silebilmesi ve zamirlerin başka göndermelere açık kalması onun kapsamını belirler.

Bu iz zinciri **adli açığa çıkma** görüntüsünü daha geniş bir alana taşır. (86:9)'da sırların sınanması, (99:4)'te yerin haber vermesi ve (99:6)'da amellerin insanlara gösterilmesi, dağınık izlerin okunabilir bir hesaba toplanmasını ve gizli iç durumun görünür alana girmesini sağlar. `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgisi böylece işaretlerin arkasındaki gerçeklikle buluşur. Bu bağlantı, kapanıştaki iç yüzü bilme niteliğini derinleştirir; (100:11) burada bir soruşturma usulü değil, işaretlerden iç gerçeğe uzanan bilme hükmü olarak kalır.

Sonucun içte toplanması, **içte toplama ve son açıklık** hareketini görünür kılar. `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` sonucu açıklığa çıkana kadar toplama ve ayıklamayı, `{ar:صُّدُورِ, tr:ṣudūr, gloss:göğüsler ve içler}` eylemlerin çıktığı kaynağı, `{ar:يَعْلَمُ, tr:yaʿlamu, gloss:biliyor}` açıklığa çıktıkça bilmeyi taşır. (100:9, 100:10)'daki mezarların ve göğüslerin açılması, dışarıdan içeriye doğru bu toplama hareketini kurar; bilgi, göğüste duran kaynak belirlenene kadar dağılmaz ve son toplama saklı olanı görünür kılar.

Dış belirtiyle iç nedenin ayrılması, **bilme asimetrisi** yaratır. `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` hazır bulunma ve bilgiye dayalı tanıklığı, `{ar:يَعْلَمُ, tr:yaʿlamu, gloss:biliyor}` açıklığa çıktıkça bilmeyi, `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` ise sonuç belirene kadar toplamayı taşır. (100:7, 100:9, 100:10)'daki tanıklık, mezarların açılması ve göğüslerin ortaya konması, görünen işaret ile bilinen iç neden arasında bir mesafe bırakır. Bu mesafe tanıklığı, açıklanmayı ve sonucu tek bir zorunlu yoruma kapatmadan, dış işaretten iç bilgiye doğru hareketi görünür kılar.

Dış örtünün açılması ile iç kaynağın çıkarılması **dış kabuk ve iç kazının çifte hareketi**dir. `{ar:بُعْثِرَ, tr:buʿthira, gloss:ortaya çıkarıldı}` toprağı çevirip gömülüyü açmayı veya bir havuzu tersine çevirmeyi, `{ar:قُبُورِ, tr:qubūr, gloss:mezarlar}` ölünün ve gizlinin içe gömülmesini, `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` örtüden çekirdeği çıkarmayı, `{ar:صُّدُورِ, tr:ṣudūr, gloss:göğüsler ve içler}` ise eylemlerin iç kaynağını düşündürür. (100:9, 100:10)'da dış mezar ve iç göğüs birlikte açılır: kabuk çevrilir, çekirdek görünür olur ve kişi bütünü yeniden belirir. Bu paralel, dirilme hükmünü açıklayan atfedilmiş bir çift kazı benzetmesi olarak çalışır; hükmün kendisinin yerine geçmez.

Bu dış-iç hareket, **mezar ve göğüs** paralelinde insanın bütünlüğüne döner. `{ar:بِهِمْ, tr:bihim, gloss:onlar hakkında}` çoğul insan alanını, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ilişki içindeki kişileri, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise dış kişiyi ve iç kaynağı birlikte kavrayan bilgiyi taşır. (11:5)'te gizlenen göğüsler ve (99:4)'te toprağın haber vermesi, dışarı çıkarılan kişiyle göğüste saklı iç durumu tek bir bilme alanında buluşturur. Zamirin olağan göndermesi korunur; bu paralel, bihim'e yeni bir dilbilgisel gönderme eklemeden bağlamsal bir genişleme sağlar.

Zaman ve bilgi yeniden hareket alanına döndüğünde **koşunun sayılmış dönüşü** duyulur. `{ar:يَوْمَئِذٍۢ, tr:yawmaʾidhin, gloss:işte o gün}` belirli vakti, `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` koşuyu, hızlı dış hareketi, sayılabilir izi ve ayrılıştan sonra geri dönüşü, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise bu seyrin iç tarihini bilen niteliği taşır. (100:1)'deki koşu yemini ile (100:11)'deki o gün ve bilgi kapanışı, dışarı açılan hareketin sayılabilir bir geçmiş olarak geri dönmesini düşündürür. Bu dalda ʿādiyāti, koşu ve dönüşü açan biçimsel ve bağlamsal bir yankı olarak kalır; bağımsız bir sözlük karşılığı ileri sürülmez.

Bakım ilişkisinin sonucu **yetiştirme ve hasat sonucu** olarak görünür. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` besleyip büyütmeyi, `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ürünün iç yüzünü bilmeyi, `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` ise kaldırma ve ayırmadan sonra değerli özü bulmayı taşır. (100:6, 100:8, 100:10)'daki Rabbe karşı tavır, sevgi-iyilik ve göğüslerin açılması, tohumdan gelişmeye, kısır zeminden ürüne ve sonunda ayrılmış öz ya da sonuca uzanan çizgiyi kurar. Bu çizgi, bilmenin bakımdan bağımsız bir son denetim değil, yetişmenin görünür sonucuna ulaşan tanıma olarak duyulmasını sağlar; tohum, kısırlık ve hasat burada birlikte kurulan keşifsel imgelerdir.

## Yetke ve karşılığın sınırı

Bilginin açığa çıkması **iddia, tanıklık ve telafi** zincirine de yerleşir. `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bilgi ve iç yüzü tanımayı, `{ar:شَهِيدٌ, tr:shahīd, gloss:tanık}` tanıklığı, `{ar:صُّدُورِ, tr:ṣudūr, gloss:göğüsler ve içler}` parasal yükümlülüğün yerine getirilmesini, `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` hakkı geri isteme başvurusunu, `{ar:مُغِيرَٰتِ, tr:mughīrāti, gloss:akın edenler}` misilleme yerine hukuki telafiyi düşündürür. (100:1, 100:3, 100:7, 100:10)'daki koşu, sabah, tanıklık ve göğüslerin açılması, iddiadan tanıklığa ve oradan karşılığın sonuçlandırılmasına uzanan işlemi görünür kılar. Telafi bu bağlantıda, hukuki hüküm koymak için değil, bilgi ile karşılık hareketini görünür kılan bağlamsal bir biçim olarak çalışır.

Bu işlem görüntüsü **sözleşme ve fazlalık hesabı**nda daralır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ve `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` bağlayıcı ilişkiyi; `{ar:خَيْرِ, tr:khayr, gloss:hayır ve servet}` iyilik ve bağışı; `{ar:كَنُودٌ, tr:kanūdun, gloss:nankör}` nankör karşılığı; `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` cimriliğin sıkılığını; `{ar:حُصِّلَ, tr:ḥuṣṣila, gloss:toplandı ve ortaya çıkarıldı}` ise sonuçların toplanıp görünür olmasını taşır. (100:6, 100:8, 100:10)'daki Rabbe karşı tavır, iyilik ve iç açıklık, verilen iyiliği anapara üstü fazlalık gibi tutulan uzak bir alışveriş çağrışımına çevirir. Bu uzak alışveriş benzetmesi, Rabbahum'un anlamını rabâ yorumuna veya hukukî sonuca taşımadan işlemsel hesabı görünür kılar.

`{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin yetkisi **öncelik ve pekiştirilmiş yetke** olarak duyulur. `{ar:صُّدُورِ, tr:ṣudūr, gloss:göğüsler ve içler}` ilk veya öncelikli parçayı ve eylemlerin çıktığı merkezi, `{ar:شَدِيدٌ, tr:shadīd, gloss:şiddetli}` sıkılaştırmayı, `{ar:وَسَطْ, tr:wasat, gloss:orta}` iki taraf arasındaki merkezi taşır. (100:5, 100:6, 100:8, 100:10)'daki merkez, Rabbe karşı tavır, iyilik ve göğüslerin açılması, göğüste toplanan eylem kaynağını pekiştirilmiş bir yetke çevresinde okutur; görüntü, olağan Rab ve bilgi hükmünün kapsamını korur.

Bu yetke **denizcilik buyruğu ve bölümleme** görüntüsünde bütünü paylara ayırır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` gemiciler topluluğu üzerinde başlık ve yönetim yetkisini, `{ar:صُّدُورِ, tr:ṣudūr, gloss:göğüsler ve içler}` ayrılmış payı, `{ar:وَسَطْ, tr:wasat, gloss:orta}` ise bütünü ikiye kesme hareketini düşündürür. (100:5, 100:6, 100:10)'daki merkez, insanın Rabbe karşı tavrı ve içlerin ortaya konması, yönetilen topluluğun bölümlere ayrılmasını görünür kılar. Bu denizcilik bağlantısı yalnız yönetim ve paylaşma hareketini taşır; hedef cümleye gemi ya da deniz için ayrı bir adlandırma eklemez.

Merkezdeki yetke **taraflar arasında aracılık** olur. `{ar:جَمْعًا, tr:jamʿan, gloss:toplanma}` bir işe destek olmak üzere katılmayı, `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` karşılıklı söz ve güvenceyle bağı, `{ar:عَٰدِيَٰتِ, tr:ʿādiyāti, gloss:koşanlar}` düşmanlık içeren karşı tarafı, `{ar:وَسَطْ, tr:wasat, gloss:orta}` ise insanlar arasında merkezde durup aracılık etmeyi taşır. (100:1, 100:5, 100:6)'daki koşu yemini, merkez ve Rabbe karşı tavır, çekişen iki tarafın ortada yeniden düzenlenen bir ilişkide buluşmasını düşündürür; ilk ayetin katkısı burada da zayıf komşuluk olarak kalır.

`{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ve `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ilişkisinin dış alanı, Fâtiha'daki `{ar:عَٰلَمِينَ, tr:al-ʿālamīn, gloss:âlemler}` ile sınırlı bir **dış alanı besleyen Rab ilişkisi**ne kadar genişler. (1:2)'deki Rab ve âlemler alanı, çok miktarda toplanmış suyu bütün alana yayılan rızık ve tedarik ilişkisi gibi duyurur. Böylece Rab unvanı yalnız bir grubun bilgisi değil, alan boyunca ulaşan bir besleme ilişkisi olarak da görünür. Bu dış alan bağlantısında al-ʿālamīn, su anlamına değil tedarik ilişkisini genişleten âlemler alanına işaret eder; hedef cümleye yeni bir dilbilgisi eklenmez.

Bu bağın daha dar bir sınırı **sözleşmeyle yaralanmış ilişki** olarak belirir. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin iyilik ve bağlılık taşıyan yüzeyi, (14:7)'de şükür ile inkârın karşıtlığı ve (102:8)'de nimetin sorgulanmasıyla birlikte düşünüldüğünde, verilen iyiliğin karşılıksız bırakılmasını ilişkinin içinde oluşan bir yara olarak gösterir. Böylece bakım bağı, doğrudan resmî bir ahit ilan etmeden, ihlal ve karşılık meselesini taşıyan sınırlı bir sözleşme ilişkisi rengine açılır; hedef cümlenin bilgisi bu yarayı bilen tanıma olarak derinleşir.

İlişkinin devamı da aynı yerde korunur. (14:7)'de şükür ve inkâr, ilişkinin öznesini değiştirmeden ahlaki rengini dönüştürür; (14:25)'te Rabbin izniyle süren ürün, bu bağ içinde gelişmiş bir geçmişi taşır. `{ar:رَبَّهُم, tr:rabbahum, gloss:onların Rabbi}` ifadesinin kuşattığı insanlar değişen karşılıklarıyla yine aynı ilişkinin içindedir; (100:11)'deki `{ar:خَبِيرٌۢ, tr:khabīrun, gloss:iç yüzü bilen}` ise bu süreklilik içinde görünen davranışı ve iç durumu bilen son nitelik olarak kapanır.

</editorial_prose>
