# V5 reading invitation — 12:34

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

`_commentary/v5/editorial/s012-p02-with-fatiha/s012/12_34/12_34.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s012-p02-with-fatiha/s012/12_34/12_34.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
Bu âyet, Yusuf'un duasına Rabbinin karşılık verdiğini ve kadınların onun için kurduğu düzeni ondan uzaklaştırdığını bildirir. Sonunda bu iki eylemi yapan Rabbi işiten ve bilen olarak tanınır: {ar:فَٱسْتَجَابَ لَهُۥ, tr:fe-istecâbe lehû, gloss:ona karşılık verdi} ve {ar:فَصَرَفَ عَنْهُ كَيْدَهُنَّ, tr:fe-ṣarafa ʿanhu kaydahunna, gloss:onların düzenini ondan uzaklaştırdı}. Cümlenin düz anlamı açıktır: dua cevap bulur, kadınların amaca yönelmiş düzeni Yusuf'tan çekilir ve bu koruyucu eylem işitme ile bilme nitelikleriyle açıklanır.

Başındaki {ar:فَ, tr:fa, gloss:ardından} önceki yalvarıştan gerçekleşmiş cevaba geçişi kurar. Önceki duada (12:33) dile gelen dua burada yeniden söylenmeden, {ar:ٱسْتَجَابَ, tr:istecâbe, gloss:karşılık verdi} fiilinin yöneldiği {ar:لَهُۥ, tr:lehû, gloss:ona / onun için} tamlamasında taşınır. Bu fiilin Form X kalıbı, sözü yalnızca duymayı değil, yöneltilmiş söze karşılık verip isteği kabul edilmiş bir sonuca ulaştırmayı duyurur. Geçmiş zaman ve etkin yapı da bekleyişi tamamlanmış bir ilahî eyleme çevirir; cevap, Yusuf'un içinde bulunduğu duruma dokunan bir karşılıktır.

{ar:لَهُۥ, tr:lehû, gloss:ona / onun için} belirli bir yararlanıcıyı cümlenin başında tutar; hemen ardından gelen {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi} ise önceki duada yönelinen Rabbi bu defa cevabı gerçekleştiren açık özne yapar. Yusuf'un korunması, failin adı duyulmadan önce cümlede hazırlanır; sonra aynı özne hem karşılık vermeyi hem uzaklaştırmayı taşır. `Rabb` sahip olma ve yönetme anlamıyla birlikte, gözetileni eksik hâlinden tamamlanmış hâle doğru yetiştiren bir bakım yönü de açar. Kelimedeki şedde, bağlaçların ve fiillerin hafif akışı arasında kısa bir ses ağırlığı oluşturarak bu faili işitmede sabitler.

İlk fiilin ardından gelen ikinci {ar:فَ, tr:fa, gloss:ardından} cevabı koruyucu eyleme çevirir. {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı} fiilinin Form I biçimi, yönü Rabbin müdahalesiyle değişen tamamlanmış bir eylemi öne çıkarır. Fiil, yönü çareyle ve kontrollü bir değişimle çevirir. Önceki duada istenen uzaklaştırma (12:33), burada aynı yön çerçevesini taşıyan geçmiş zaman fiiliyle gerçekleşmiş korunmaya dönüşür; bağlaçların akışından sonra fiilin belirgin başlangıcı ikinci hareketi ses bakımından da öne çıkarır.

Bu hareketin yönü ve nesnesi birbirinden ayrılmaz: {ar:عَنْهُ, tr:ʿanhu, gloss:ondan} Yusuf'u uzaklaşmanın korunan son noktası yapar, {ar:كَيْدَهُنَّ, tr:kaydahunna, gloss:onların kurduğu düzen} ise Rabbin geri çevirdiği doğrudan nesnedir. Okur önce güvenliğin yönünü, sonra o yönden çekilen tehlikenin adını alır. `ʿanhu` ile hemen sonraki `kaydahunna` arasındaki burunlu ses yankısı da kişiyi ve ondan uzaklaştırılan düzeni birbirine bağlar. `Kayd` belirsiz bir kötülük değil, amaca ulaşmak için dolaylı ve önceden kurulmuş bir plandır; dişil çoğul iyelik eki, tek bir düzeni birden fazla kadının ortak sahipliğiyle gösterir. Bu sözdiziminde Yusuf korunan uç olarak kalır; uzaklaştırılan doğrudan nesne, kadınların kurduğu düzendir.

{ar:إِنَّهُۥ, tr:innahû, gloss:şüphesiz O} ile başlayan kapanış yeni bir olay eklemez, iki eylemin dayanağını açıklar. Bağımsız {ar:هُوَ, tr:huwa, gloss:O} zamiri ilk sıfatı geciktirerek kısa bir bekleme kurar; özneyi sıfatlardan ayırıp az önce eyleyen Rabbi iki kesin nitelemeye bağlar. {ar:ٱلسَّمِيعُ, tr:es-semîʿu, gloss:işiten} belirli ve yoğun bir ilahî ad olarak, yalnız bu duanın duyulmuş olmasını değil, cevabı mümkün kılan işitici niteliği bildirir. Cevabın hemen ardından gelişi, duyulan duayı geriye dönük olarak açıklar. {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} bilme ve gerçeği kavrama anlamıyla birlikte gizli düzeni ayırt eden bir basınç taşır; uzaklaştırma cümlesinden sonra gelmesi, düzenin neden isabetle çevrildiğini açıklar. İki ad, biri duaya diğeri saklı düzene temas eden dengeli bir kapanışta buluşur.

## Cevabın İçindeki Hareket

Çevirinin tek karşılıkta topladığı kelime yönleri burada adım adım korumanın nasıl işlediğini gösterir. {ar:ٱسْتَجَابَ, tr:istecâbe, gloss:karşılık verdi}nın önceden yöneltilmiş söze cevap verme hareketi, {ar:ٱلسَّمِيعُ, tr:es-semîʿu, gloss:işiten}nun sesi alıp anlamaya varan işitmesiyle birleşir; duyma sonuç doğuran bir karşılığa dönüşür. {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi}nin gözetip tamamlayan yönü cevaba bakım ve tamamlanmışlık verir. Ardından {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı} ile {ar:عَنْهُ, tr:ʿanhu, gloss:ondan} tehdidin Yusuf'un hattından başka bir yöne aktarılmasını kurar; {ar:كَيْدَهُنَّ, tr:kaydahunna, gloss:onların kurduğu düzen}nın önceden hazırlanmış baskısı müdahalenin hedefini belirler. {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen}nun gizli yapıyı ayırt eden yönü bu akışı tamamlar. Bu katkılar bir araya geldiğinde olağan haber korunur: cevap, duyulmuş ihtiyaç ve bilinmiş baskı üzerinde işleyen koruyucu bir yönlendirme olarak belirir.

Bunun yanında baskının hattı, silinmek yerine karşılanıp başka yöne aktarılmış bir karşı-hareket olarak görünür. {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı}nın işler içinde çare kullanarak yön değiştirme yönü, {ar:كَيْدَهُنَّ, tr:kaydahunna, gloss:onların kurduğu düzen}nın yoğun çabası ve önceden hazırlanmış baskısıyla karşılaşır; {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} hangi baskının hangi yöne aktarılacağını ayırt eden bilgiyi taşır. Canlı bir baskı böylece bilgili bir müdahaleyle Yusuf'un hattından çevrilir. Plan yerinde kalır; kurucularının silinmesi veya tehdidin bütünüyle yok olması bu bağlantının kapsamına girmez. Odak, kurulmuş baskının yönünün değiştirilmesidir.

Koruma burada iki sonucu birlikte taşır: Yusuf'un hattı korunurken, içinde bulunduğu durumun yönü ve sonucu da değişir. {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi}nin eksik olanı tamamlanmışa doğru yetiştiren yönü, {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı}nın hâller arasında geçiş taşıyan eylemiyle buluşur. {ar:ٱسْتَجَابَ, tr:istecâbe, gloss:karşılık verdi} değişen hâli kişisel bir cevaba bağlar; {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} ise değişime okunabilir bir istikamet verir. Bu ilişki ayetteki kısa ve tamamlanmış uzaklaştırma eyleminin sınırını korur; cevabın baskının varlığını sürdürdüğü bir durumda onun vardığı sonucu değiştirebileceğini görünür kılar.

## Baskı İçinde Değişen Yön

Bu yerel yön değiştirme, 12:19, 12:20 ve 12:21'deki sıralama ile birlikte okunduğunda Yusuf'un durumundaki daha uzun dönüşüm çizgisine bağlanır. 12:19'da onun gizlice elden çıkarılması {ar:أَسَرُّوهُ, tr:eserrûhu, gloss:onu gizlediler} ve bir mal gibi görülmesi {ar:بِضَاعَةً, tr:bidâaten, gloss:mal veya meta} iki ayrı temasla Yusuf'u yerel planların nesnesi konumuna iter. 12:20'deki {ar:بَخْسٍ, tr:bahsin, gloss:eksik değer} bu daralmayı daha da belirginleştirir. 12:21'de {ar:مَكَّنَّا لِيُوسُفَ, tr:mekkennenâ li-Yûsuf, gloss:Yusuf'a yer ve imkân verdik} ile yer ve kapasite açılır; {ar:تَأْوِيلِ ٱلْأَحَادِيثِ, tr:teʾvîli'l-ehâdîs, gloss:sözlerin ve olayların yorumuna erişim} bir sonuca erişme imkânını, {ar:وَٱللَّهُ غَالِبٌ عَلَىٰ أَمْرِهِ, tr:vallâhu gâlibun alâ emrihî, gloss:Allah işinde üstün gelendir} ise yerel planları aşan kuvveti duyurur. Bu bağ, odaktaki {ar:فَصَرَفَ, tr:fe-ṣarafa, gloss:yönünü geri çevirdi} fiilinin {ar:عَنْهُ, tr:ʿanhu, gloss:ondan} ile koruduğu uzaklaşma yönünü sürdürürken, toplumsal baskının Yusuf'u belirleyecek güçten çıkıp çevrede kalan bir baskı hâline geldiğini düşündürür.

Bu daha geniş hareketin kapalı sahnedeki karşılığına 12:23 ve 12:24'te bakıldığında, cevap mekânsal bir geçit gibi hissedilir. {ar:فَٱسْتَجَابَ لَهُۥ, tr:fe-istecâbe lehû, gloss:ona karşılık verdi} olağan anlamıyla duaya cevap vermeyi korurken, açılmış ve ortası boş geniş aralık imgesi kapalı alan içinde geçilebilir bir yol düşündürür. {ar:فَصَرَفَ عَنْهُ, tr:fe-ṣarafa ʿanhu, gloss:onu ondan uzaklaştırdı} bu yolun yön değiştirme hareketini taşır. {ar:وَغَلَّقَتِ ٱلْأَبْوَابَ, tr:ve gallekati'l-ebvâb, gloss:kapıları sıkıca kapattı} duvar gibi bir baskı kurar; eşik geçişin sınırını belirler; {ar:مَعَاذَ ٱللَّهِ, tr:meʿâze'llâh, gloss:Allah'a sığınak} korunmanın yönünü verir. {ar:لِنَصْرِفَ عَنْهُ ٱلسُّوٓءَ, tr:li-nasrife ʿanhu's-sûʾe, gloss:kötülüğü ondan uzaklaştıralım} ifadesi de kapalı alandan çıkış hareketini tamamlar. Kapı, eşik, sığınak ve yakalanmışlıktan çıkışın bu örtüşmesi (12:23, 12:24), odaktaki geçiş duygusunu genişletir; bu ilişki `ṣarafa`yı kapı sözcüğüne dönüştürmeden mekânsal resmi canlı tutar.

Kapalı alandan çıkışın ardından 12:25, 12:26, 12:27 ve 12:28'de yön maddi bir iz üzerinden sınanır. Gömleğin yırtığıyla görünen delilin buluşması, cevabı bir suçlamayı çeviren maddi ölçü gibi düşündürür. Odaktaki {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı}nın durum dönüştüren yönü, {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen}nun ayırt edici işaret bilgisiyle birleşir. {ar:قَدَّتْ قَمِيصَهُۥ مِن دُبُرٍ, tr:kaddet kamîsahu min dubur, gloss:gömleğini arkasından yırttı} yırtığı bedenin arkasındaki kesik olarak somutlaştırır. {ar:شَهِدَ شَاهِدٌ, tr:şehide şâhid, gloss:bir tanık tanıklık etti} ile {ar:فَصَدَقَتْ, tr:fe-sadekat, gloss:o doğru söyledi} tanıklık ve doğruluk, yırtığın yönünü suçlamayı sınayan ölçüte çevirir. {ar:فَلَمَّا رَءَا قَمِيصَهُۥ, tr:fe-lemmâ raʾâ kamîsahu, gloss:gömleğini görünce} görülünce ve {ar:إِنَّهُۥ مِن كَيْدِكُنَّ, tr:innehû min keydikunne, gloss:bu sizin düzeninizdendir} denilince görme ile kurulu düzen aynı kanıt sahnesinde yeniden çerçevelenir. Bu maddi dönüş, belirli suçlama sahnesinin sınırları içinde kalır; kadınların çoğul düzeni ilk suçlamaya indirgenmeden, yırtık üzerinden kanıtın yönünü görünür kılar.

Bu kanıt sahnesi, cevabın olağan anlamını koruyan ayrı bir kalkan imgesine de açılır. {ar:فَٱسْتَجَابَ لَهُۥ, tr:fe-istecâbe lehû, gloss:ona karşılık verdi} duaya karşılık verme olarak yerinde dururken, açıklık ile bedeni saran giysi imgesi cevabı yırtılmış bir yüzeyin içinden açılan koruyucu çizgi gibi hissettirir. Gömleğin {ar:قَدَّتْ قَمِيصَهُۥ, tr:kaddet kamîsahu, gloss:gömleğini yırttı} eylemi ve {ar:مِن دُبُرٍ, tr:min dubur, gloss:arkasından} yönü yarığı belirler; {ar:شَهِدَ شَاهِدٌ, tr:şehide şâhid, gloss:bir tanık tanıklık etti} tanıklığı ile {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen}nun ayırt edici bilgi yönü bu yarığı maddi delile bağlar (12:25, 12:26). Bağın sınırı da açıktır: `istecâbe` burada gömleği adlandırmaz; yırtık, tılsımlı veya kendiliğinden işleyen bir koruma değil, maddi delil imgesini taşır.

12:29'da aynı uzaklaşma yönü iki farklı nesneye uygulanır. {ar:يُوسُفُ أَعْرِضْ عَنْ هَٰذَا, tr:Yûsufu aʿriḍ ʿan hâzâ, gloss:Yusuf bundan yüz çevir} emri dikkati bir olaydan çevirirken, {ar:فَصَرَفَ عَنْهُ كَيْدَهُنَّ, tr:fe-ṣarafa ʿanhu kaydahunna, gloss:onların düzenini ondan uzaklaştırdı} düzenin kuvvetini Yusuf'tan çevirir. Emrin devamındaki {ar:وَٱسْتَغْفِرِى لِذَنۢبِكِ, tr:vestagfirî li-zenbiki, gloss:suçun için bağışlanma dile} ve {ar:مِنَ ٱلْخَٰطِـِٔينَ, tr:mine'l-hâṭiʾîn, gloss:yanılanlardan} sözleri, dikkat çevrildikten sonra sorumluluğun da başka bir çerçeveye taşındığını gösterir. Bu karşılaştırma iki eylemin nesne ve yararlanıcılarını aydınlatır; ev halkının niyetini açık bırakır ve iki uzaklaştırmayı aynı anlama kapatmaz.

Dikkatin çevrilmesinden sonra sözün şehirde dolaşıma girmesi, 12:30 ve 12:31'de `kaydahunna`daki çoğul düzeni tekil bir niyetten toplumsal bir harekete taşır. {ar:ٱلسَّمِيعُ, tr:es-semîʿu, gloss:işiten} adı işitmeyi yalnız ses almak değil, duyulanı anlayıp ona uymaya uzanan bir eylem gibi duyurur. {ar:وَقَالَ نِسْوَةٌ فِي ٱلْمَدِينَةِ, tr:ve kâle nisvetun fi'l-medîne, gloss:şehirdeki kadınlar söyledi} sözü ve Aziz'in eşinin adını anması, söylentinin konuşanlar arasında dolaşan teşhir gücünü açar. {ar:سَمِعَتْ بِمَكْرِهِنَّ, tr:semiʿat bi-mekrihinne, gloss:onların düzenini işitti} ile olay duyulmuş bir şeye, {ar:أَرْسَلَتْ إِلَيْهِنَّ, tr:erselet ileyhinne, gloss:onlara haber gönderdi} ile de çağrılmış bir buluşmaya dönüşür (12:30, 12:31). Bu halka, bu düzenin işitilerek başkalarını harekete geçirebilen toplumsal dolaşımını gösterir; başka sosyal alışverişler hakkında genel bir hüküm kurmaz.

Bu dolaşımdaki çağrı 12:32 ve 12:33'te Yusuf'un kendi öz-tutmasıyla karşılaşır. {ar:مِمَّا يَدْعُونَنِيٓ إِلَيْهِ, tr:mimmâ yedʿûnenî ileyhi, gloss:bana çağırdıkları şey} çağrının yöneldiği şeyi açar; odaktaki {ar:فَصَرَفَ عَنْهُ, tr:fe-ṣarafa ʿanhu, gloss:onu ondan uzaklaştırdı} dıştaki düzenin başka yöne çevrilmesini taşır. {ar:فَٱسْتَعْصَمَ, tr:fe-staʿṣama, gloss:kendini tutup korudu} etkin öz-tutmayı, {ar:أَحَبُّ, tr:eḥabb, gloss:daha çok tercih edilir} hapishanenin çağrılan şeye göre tercih edilişini görünür kılar. Yusuf'un {ar:كَيْدَهُنَّ, tr:kaydahunna, gloss:onların kurduğu düzen} diye adlandırdığı baskı, {ar:أَصْبُ إِلَيْهِنَّ, tr:aṣbû ileyhinne, gloss:onlara içten yönelirim} korkusuyla içsel bir yön kazanır ve {ar:ٱلْجَٰهِلِينَ, tr:el-câhilîn, gloss:bilgisizlerden} olma ihtimaliyle sınırlandırılır. Bu iki hareket aynı koruma sahnesinde buluşur; bağlantı, insan direncini ilahî cevabın sebebi olarak ilan etmeden birlikte işleyen korunmayı görünür kılar.

Yusuf'un kendini tutmasıyla yerel buyruğun gücü de aynı sahnede ayrışır. {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi} sahip olma, buyurma ve düzenleme çekirdeğini taşırken, 12:25, 12:32 ve 12:33'te görülen {ar:سَيِّدَهَا, tr:seyyidehâ, gloss:onun efendisi} ev halkının yerel hâkimiyetini gösterir. {ar:مَآ ءَامُرُهُۥ, tr:mâ âmuruhû, gloss:ona emrettiğim şey} buyruğa uymayı, {ar:لَيُسْجَنَنَّ, tr:le-yüs-cenenne, gloss:onu mutlaka hapsedecekler} ise uymama karşılığındaki zorlayıcı yeri belirler. Böylece Yusuf'un nerede tutulacağını belirleyen yerel emir ile düzenin Yusuf üzerindeki amaçlanan etkisini Rabbin cevabının çevirmesi yan yana gelir; yerel güç kendi sahasında görünür, karşılaştırma ise daha geniş bir siyaset öğretisi kurmadan bu iki otorite ölçeğini ayırır.

Bu ayrımın sonucu 12:35'te daha somut bir biçim alır: {ar:رَأَوُا ٱلْءَايَٰتِ, tr:raʾavü'l-âyât, gloss:işaretleri gördüler} denilmesi görünür işaretlerin kaldığını, {ar:لَيَسْجُنُنَّهُۥ, tr:le-yüscunûnnehû, gloss:onu mutlaka hapsedecekler} kararı ve {ar:حَتَّىٰ حِينٍ, tr:ḥattâ ḥîn, gloss:belirli bir vakte kadar} sınırı ise gecikmenin sürdüğünü gösterir. Görülen işaret yeni bir görüş doğurur; bu görme, {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} adının ayırt edici işareti bilme yönüyle buluşur. Odaktaki uzaklaştırma böylece kadınların düzenini Yusuf'tan çeviren korumayı, görünür işaretlerin ve dünyevî gecikmenin sürmesiyle birlikte kurar.

{ar:ٱلسَّمِيعُ, tr:es-semîʿu, gloss:işiten}nun çevresinde beliren başka bir yerel imge, hareketi sınırlayan ayak bağı ve bağlanma duygusudur. Cevap olağan anlamıyla dileğe karşılık vermeyi sürdürürken 12:35'teki hapis yeri hareketi sınırlar; {ar:حَتَّىٰ حِينٍ, tr:ḥattâ ḥîn, gloss:belirli bir vakte kadar} bu bağlılığı zamanca çerçeveler. İşitilmiş cevap böylece kısıt altında da etkin kalabilen bir cevap gibi duyulur. Bu imge işitmeye bağlamak anlamı vermez; hapis ve zaman sınırı, cevabın kısıt altında da etkin kalabildiği çerçeveyi çizer ve sonucu hemen serbest bırakmayla eşitlemez.

12:32 ve 12:33'teki içe yönelme korkusuna dönüldüğünde, {ar:فَصَرَفَ عَنْهُ, tr:fe-ṣarafa ʿanhu, gloss:onu ondan uzaklaştırdı} gönül yönünü çeviren bir nesneyi düşündüren daha kültürel bir benzetmeye açılır. Bir erkeğin gönlünü istediği kişiden uzaklaştırdığına inanılan gönül çevirme boncuğu, {ar:فَٱسْتَعْصَمَ, tr:fe-staʿṣama, gloss:kendini tutup korudu} öz-tutması ve {ar:كَيْدَهُنَّ, tr:kaydahunna, gloss:onların kurduğu düzen} dış baskısıyla yan yana geldiğinde, cevabın düzeni kalbe ulaşmadan çevirdiği okunabilir. Bu kültürel benzetme, odak fiilinin yön değiştirme anlamını kalbin vektöründe hissettirir; boncuk burada ilahî cevabın tılsımlı mekanizması değil, dış baskının iç yön üzerindeki karşılığını duyuran bir nesnedir.

Daha önceki değer kaybı sahnesine, 12:19 ve 12:20'ye dönüldüğünde, ilahî dönüş bir karşı-değerleme duygusu da açar. {ar:صَرَفَ, tr:ṣarafa, gloss:uzaklaştırdı} için para değiştirme ve değer farkı imgesi, {ar:بِضَاعَةً, tr:bidâaten, gloss:mal veya meta} olarak kurulmuş nesne konumuna temas eder. {ar:بِثَمَنٍۢ بَخْسٍ, tr:bi-semenin bahsin, gloss:eksik bir bedelle} ve {ar:دَرَٰهِمَ مَعْدُودَةٍ, tr:derâhime maʿdûde, gloss:sayılı birkaç dirhem} fiyatı görünür kılar; {ar:مِنَ ٱلزَّٰهِدِينَ, tr:mine'z-zâhidîn, gloss:değer vermeyenlerden} bu değerin küçültüldüğünü açıklar. Buna karşı {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi}nin yetiştirip tamamlayan yönü, Yusuf'un değerinin ilk alışverişle sabitlenmediğini düşündürür (12:19, 12:20). Bu bağ `ṣarafa`nın ekonomik sözlük anlamını öne sürmez; ilk alışverişin Yusuf'un nihai değerini belirlemediğini düşündüren sınırlandırılmış bir yankı olarak kalır.

Fâtiha'daki {ar:رَبِّ ٱلْعَٰلَمِينَ, tr:rabbi'l-ʿâlemîn, gloss:âlemlerin Rabbi} ifadesi, odaktaki kişisel {ar:رَبُّهُۥ, tr:rabbuhû, gloss:onun Rabbi} hitabını ve kapanıştaki {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} adını yaratılmış bütünün ufkuna taşıyan dış bir yankı kurar (1:2). Yusuf'a cevap veren Rabbi tek kişilik sahnenin içinde kalırken, bu yakınlıkta bütün yaratılmışları yöneten bir kapsam içinde de duyulur; âlemler imgesi bilme niteliğinin olay örgüsünün ötesine uzanmasına izin verir. Bu yankının kapsamı (1:2)'deki Rab ve âlemler yakınlığıdır; Fâtiha'nın tamamını bu sahneye taşımadan, `rabbuhû`yu `rabbi'l-ʿâlemîn` diye tercüme etmez ve `el-ʿalîmu`yu âlemler sözcüğüne dönüştürmez.

İşiten ve bilen kapanışı, şeytanın dürtüsü karşısında Allah'a sığınma çağrısıyla birlikte 41:36'da da duyulur. Bu yankı, {ar:ٱلسَّمِيعُ, tr:es-semîʿu, gloss:işiten} ile {ar:ٱلْعَلِيمُ, tr:el-ʿalîmu, gloss:bilen} adlarını baskı altındaki koruyucu cevapla buluşturur: sesli ihtiyaç ve onun arkasındaki kırılganlık birlikte kavranır. 41:36'daki sığınma sahnesi kendi bağlamını korur; 12:34'ün bütün dil bilgisel ayrıntılarını buraya taşımadan, işitme ile bilmenin korunma bağlamında birlikte etkinleşebileceğini düşündüren sınırlı bir yankı olarak kalır.

Odaktaki uzaklaştırma ile cevabın gerçekleşmesi, sıkıntının o anda bütünüyle bitmesiyle eşitlenmez. Kadınların planının yeniden anılması, Yusuf'un hapishaneye girişi ve ardından kral tarafından çağrılıp güvenilir bir mevkiye yerleştirilmesi 12:36, 12:52 ve 12:54'te aynı yön değiştiren güzergâhın iki görünümünü açar. {ar:فَصَرَفَ, tr:fe-ṣarafa, gloss:yönünü geri çevirdi} bir yandan tehdidin Yusuf'a ulaşan yönünü geri çevirir; öte yandan yönler ve hâller arasında geçiş taşıyarak hapishaneden güven ve yetki konumuna uzanan rotayı düşündürür. Bu bağlantının katkısı, koruma ile güçlüğü aynı güzergâhta birlikte görmektir: planın başarısızlığa uğraması, mahpusluğun sürmesi ve gecikmiş yolun kamuya açık güven ve yetki konumuna varması aynı rota üzerinde görünür. Hapishane bu okumada kendi başına iyi ilan edilmez; kadınların planı gerçekdışı sayılmaz; saraydaki atama ayetin tek sonucu değil, yön değiştiren rotanın sonraki bir görünümüdür. Böylece ayetin koruması, baskının içinden geçerek yolun vardığı hâli değiştirebilen bir cevap olarak tamamlanır.

Odaktaki uzaklaştırma ile cevabın gerçekleşmesi, sıkıntının o anda bütünüyle bitmesiyle eşitlenmez. Kadınların planının yeniden anılması, Yusuf'un hapishaneye girişi ve ardından kral tarafından çağrılıp güvenilir bir mevkiye yerleştirilmesi 12:36, 12:52 ve 12:54'te aynı yön değiştiren güzergâhın iki görünümünü açar. {ar:فَصَرَفَ, tr:fe-ṣarafa, gloss:yönünü geri çevirdi} bir yandan tehdidin Yusuf'a ulaşan yönünü geri çevirir; öte yandan yönler ve hâller arasında geçiş taşıyarak hapishaneden güven ve yetki konumuna uzanan rotayı düşündürür. Planın başarısızlığa uğramasıyla mahpusluk birlikte kalabilir, gecikmiş yol başka bir kamu sonucuna açılabilir. Bu bağlantı hapishaneyi kendi başına iyi ilan etmez, kadınların planını gerçekdışı saymaz ve saraydaki atamayı ayetin tek sonucu olarak belirlemez; ayetteki korumanın baskının içinden geçerek yolun vardığı hâli değiştirebildiğini görünür kılar.

</editorial_prose>
