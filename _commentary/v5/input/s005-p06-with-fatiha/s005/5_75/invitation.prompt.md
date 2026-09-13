# V5 reading invitation — 5:75

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

`_commentary/v5/editorial/s005-p06-with-fatiha/s005/5_75/5_75.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s005-p06-with-fatiha/s005/5_75/5_75.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
Bu âyet, {ar:ٱلْمَسِيحُ, tr:el-Mesîh, gloss:Mesih} {ar:ٱبْنُ, tr:ibnu, gloss:oğlu} {ar:مَرْيَمَ, tr:Meryem, gloss:Meryem} olan kişinin bir elçi olduğunu söyler. Ondan önce elçiler gelip geçmiştir; {ar:أُمُّهُۥ, tr:ummuhû, gloss:annesi} doğru ve güvenilir bir kadındır; oğlu ile annesi yemek yerler. Ardından iki kez {ar:ٱنظُرْ, tr:unzur, gloss:bak/incele} diyerek okuyucuyu, işaretlerin nasıl açıklandığına ve insanların nasıl çevrildiğine bakmaya çağırır. Kimlik iddiası böylece elçilik, soy, annelik ve bedenî ihtiyaçla birlikte ele alınır; son hareket, açıklığın alımlanma yönüyle nasıl karşılaştığını gösterir.

## Adlandırmanın Sınırı

Başlangıçtaki {ar:مَا, tr:mā, gloss:negatif açılış} sözü cümleyi hükmü daraltan bir kuruluşla açar; {ar:إِلَّا, tr:illā, gloss:ancak} bu daraltmayı olumlu bir sonuca bağlar ve Mesih'in bu ayetteki konumunu elçilik adıyla belirler. {ar:ٱلْمَسِيحُ, tr:el-Mesîh, gloss:Mesih} belirli unvanıyla hükmün kişisini sabitler. Unvanın meshetme ve temas çağrışımı, özel adın anılan yüzeyini duyurur; cümlenin belirli kullanımı bu katkıyı kişi adını aşmayan bir niteleme olarak tutar. {ar:ٱبْنُ, tr:ibnu, gloss:oğlu} ile {ar:مَرْيَمَ, tr:Meryem, gloss:Meryem} tamlaması kişiyi belirli bir anneye bağlar ve bu özel adla kapanarak ilişkiyi cümledeki görevine sabitler; ibnu kelimesinin köken ve oluşuma açılan yan basıncı insanî soy nispetini derinleştirir. Meryem adı belirli kişiyi gösterme işini üstlenir; ortak bir kök çağrışımı bu bağlantıda belirleyici değildir.

{ar:رَسُولٌۭ, tr:rasûlun, gloss:elçi} sözü özel addan gönderilmiş görev kategorisine geçirir. Tekil ve belirsiz biçim, Mesih'i gönderilme ve ulaştırılma görevi taşıyan bir kişi olarak tanımlar; görev adı onu elçiler sınıfına bağlarken bireysel kişiliğini korur. {ar:قَدْ, tr:qad, gloss:çoktan} ile {ar:خَلَتْ, tr:halet, gloss:geçip gitti} elçilerin geçip gitmişliğini tamamlanmış bir geçmiş olarak duyurur; {ar:ٱلرُّسُلُ, tr:er-rusul, gloss:elçiler} çoğulu bu geçmişi tekil bir kişiden önce uzanan elçiler zincirine açar. Dişil tekil fiil, Arapçada ardından gelen kırık çoğul özneyle uyum kurarak topluluğu tamamlanmış ve çekilip gitmiş halde gösterir. {ar:مِنْ, tr:min, gloss:-den/-dan} ile {ar:قَبْلِهِ, tr:kablihî, gloss:ondan önce} zamanı doğrudan Mesih'e göre ölçer. “Önce” böylece genel bir geçmiş değil, onun konumuna göre kurulmuş bir öncelik olur; bu ifadenin yön ve karşıya dönme basıncı da zamansal sıraya eşlik eder. Bu kalıp elçi görevini ardışık taşıyıcıların zinciri içinde süren tarihsel süreklilik olarak duyurur.

## Anne ve Beden

Elçilerden anneye geçişi {ar:وَ, tr:wa, gloss:ve} açar; bağlaç aynı açıklayıcı akışa ikinci kişiyi ekler. {ar:أُمُّهُۥ, tr:ummuhû, gloss:annesi} övgü yükleminin öznesi olarak belirir ve {ar:صِدِّيقَةٌۭ, tr:sıddîka, gloss:doğru ve güvenilir} dişil tekil biçimi bu övgüyü doğrudan Meryem'e bağlar. Sıddîka, doğru sözlülük, sağlam karakter ve güvenilirlik alanını açar. Bu sıfat annenin kendi doğruluk mertebesini kurar; elçilik kategorisiyle birleşmeden Meryem'e ait bir nitelik olarak çalışır. Anne kelimesinin belirli ve tekil oluşu ilişkiyi belirli kişide sabitler. Böylece anne çağrışımı bağı, doğum çağrışımı bedensel oluşumu, seçilmiş kadın çağrışımı da onun seçilmişlik yönünü belirginleştirir; üçü bu açık gönderme çevresinde duyulur.

Ardından {ar:كَانَا, tr:kânâ, gloss:ikisi de ... idi} ikil biçimi Mesih ile annesini aynı geçmiş durumun iki öznesi yapar. {ar:يَأْكُلَانِ, tr:ye'külâni, gloss:yiyorlardı} ikil çekimle iki kişiyi birlikte tutar; süreklilik görünüşü bedenî yaşamın alışılmış ihtiyacını gösterir. Doğrudan nesne olan {ar:ٱلطَّعَامَ, tr:et-ta'âm, gloss:yemek} yeme eylemini somut besine ve beslenme sınıfına bağlar. Elçilik ve doğruluk nitelemelerinin ardından gelen bu yemek sahnesi, yüksek unvanı gündelik bedensel alımın içine yerleştirir. Yemek fiilinin oğulluk adıyla buluşması, besinin bedenin kurulup büyümesine hizmet ettiğini görünür kılar; 5:80'deki {ar:النفس, tr:en-nefs, gloss:yaşayan öz} imgesi, yaşayan öznenin dışarıdan gelen gıdaya açıklığını bu bedensel süreçle buluşturur. Böylece yemek olağan beslenme anlamını taşıyarak bedensel bağımlılığı açar; bu sahne biyolojik ayrıntıların ya da ruhun mahiyetinin açıklamasına genişlemez.

Bu bedensel bağımlılığı dört bağlam ayrı birer görüntüyle açar. 21:8'de elçilerin yemesi fanilikle yan yana gelerek bedenî yaşamın geçiciliğini görünür kılar; 25:7'de elçinin yemek zorunda oluşu, bu ihtiyacı itirazın hedefi yapar; 26:79'da yedirip içirenin Allah olduğu, beslenmenin kaynağını belirginleştirir; 6:14'te besleyen ile beslenenin karşıtlığı, alıcı tarafın yerini açığa çıkarır. Bu dört katkı, {ar:يَأْكُلَانِ, tr:ye'külâni, gloss:yiyorlardı} ile {ar:ٱلطَّعَامَ, tr:et-ta'âm, gloss:yemek} ifadelerini alınan rızkın alıcı ucuna taşır. Odaktaki iki kişinin yemek yemesi bu insanî ve olağan anlamı sürdürür; elçilik makamı ile besine muhtaç beden aynı sahnede böylece birlikte okunur.

## Alıcı ve Kaynak

Yemeğin alıcı tarafı, yakın bağlamdaki yön ve tasarruf sorularıyla genişler. 5:72'deki {ar:اعبدوا الله ربي وربكم, tr:u'budû Allâhe rabbî ve rabbüküm, gloss:benim ve sizin Rabbimize kulluk edin} çağrısı yönelişi Allah'a çevirir ve Mesih'i bu çağrıyı ileten, ortak Rabbe bağlı kişi olarak gösterir. 5:73'teki {ar:واحد, tr:vâhid, gloss:bir} birlik sözü tekliği öne çıkarır; {ar:يشرك, tr:yuşrik, gloss:ortak koşmak} ise ortaklaştırma hareketini görünür kılar. 5:76'da {ar:يملك, tr:yemlik, gloss:sahip olup yönetir} ile {ar:ضَرًّا, tr:darran, gloss:zarar} ve {ar:نَفْعًا, tr:nef'an, gloss:fayda} kimin sonuçlar üzerinde tasarruf sahibi olduğunu sorar ve zarar-fayda sınamasını kurar. Böylece üç görüntü aynı ayrımı farklı yerlerden açar: besin alan beden dışarıdan destek alır, çağrı yönü Allah'a çevirir, zarar ile faydanın sahipliği ise başka bir düzlemde sınanır. Yemek, insanî oluşun belirtisi olmanın yanında alan ile yöneten arasındaki ayrımı görünür kılar. Yiyecek burada faydanın sahibi olarak değil, dışarıdan alınan destek olarak görünür; 5:76'nın geniş zarar-fayda sorusu yiyecek imgesine indirgenmeden kendi kapsamını korur. Mesih'in elçilik görevi bu bedensel ayrıntıyla birlikte okunur.

Aynı yemek imgesinin ahlâkî alım karşısındaki sınırı 5:62 ve 5:63'te belirginleşir. 5:62'de haksız kazancı yiyip tüketme, maddî alımın malı yozlaştıran edinme ve harcamaya dönüşen yüzünü gösterir; 5:63'te hareketin yinelenmesi bu bozulmuş tüketimin sürekliliğini duyurur. Odaktaki {ar:ٱلطَّعَامَ, tr:et-ta'âm, gloss:yemek} ise beslenme için alınan gıdanın olağan yüzünü taşır. Aynı kökün iki bağlamda buluşması olağan rızık ile ahlâken bozulmuş tüketimi karşılaştırır; bu bağlantıda odaktaki iki kişinin yemeği servet tüketme davranışı değil, beslenme görüntüsü olarak kalır.

Yemeğin akış görüntüsü, bedeni rızkın kaynağı değil kendisine ulaşan payın alıcısı olarak konumlandırır. 5:64'teki dışarı doğru harcama tedarikin hareketini; 5:66'da yukarıdan ve aşağıdan verilen pay, geçimliğin farklı yönlerden ulaşmasını görünür kılar. {ar:يَأْكُلَانِ, tr:ye'külâni, gloss:yiyorlardı} bu akışın alıcı kutbudur; {ar:ٱلطَّعَامَ, tr:et-ta'âm, gloss:yemek} alınan payın somut nesnesidir. Bu bağlantı kişiler için bağımsız bir ekonomik unvan değil, sağlayan ile beslenen arasındaki yerel görüntüyü açar; yukarı ve aşağı yönleri de bu görüntüde ilişkisel yönler olarak duyulur, fiziksel bir model olarak değil.

## Taşınan Görev

Elçi adının gönderilmiş görev oluşu, içeriğin kaynağıyla muhatabı arasındaki taşıma ilişkisini açar. {ar:رَسُولٌۭ, tr:rasûlun, gloss:elçi} 5:67'deki getirme, indirme ve bildirme görüntüleriyle mesajın gelişini, taşıyıcıya ulaşmasını ve muhataba duyurulmasını üç ayrı harekette görünür kılar; 5:78'deki dille seslendirme, bu aktarımın sözle duyurulan yüzünü açar. Bu taşıma resmi elçiyi içeriğin sahibi olmaktan çok onu doğru yere ve doğru sesle ulaştıran güvenilir makam olarak konumlandırır. 5:78'de dil, sözün kime nispet edildiğini ve duyuru biçimini belirginleştirebilir; bu bağlantıda aracılığın duyulmasına katkı verir. Bu katkı, tek başına baştan sona işleyen bir kanal şeması kurmadan elçi adının gönderilmiş görev anlamını somutlaştırır.

{ar:قَبْلِهِ, tr:kablihî, gloss:ondan önce} ile {ar:ٱلرُّسُلُ, tr:er-rusul, gloss:elçiler} arasındaki zaman bağı bu taşıma görevini ölümlü bir süreklilik içine yerleştirir. 5:70'te elçilerin peş peşe gelişi ölümlü bir elçiler zinciri kurar; mesaja karşı arzuyla direnilmesi, elçiye yanlış paye verilmesi ve cana kıyılması bu zincirin muhatap karşısındaki ayrı kırılganlıklarını gösterir. Bu görüntü odaktaki elçiliği ölümlü karşılaşmaların tarihsel alanına genişletir. Bağlantının Mesih'e uzanan payı elçilik ve insanî bağımlılık sınırında tutulur; 5:70'teki cana kıyma sahnesi onun hakkında öldürülme hükmü olarak okunmaz. Bu geçmişlik, elçilik görevinin ardışık taşıyıcılarla sürmesini görünür kılar. 5:77'deki {ar:تَتَّبِعُوا۟, tr:tettebiû, gloss:izleyip peşinden gidersiniz} fiili, {ar:أَهْوَاء, tr:ehvâ, gloss:arzular} ve üç kez yinelenen sapma sözleriyle ikinci bir süreklilik kurar: burada devam eden, elçilerin taşıdığı görev değil, din ve hakikat karşısında arzuyu izleyen yöneliştir. Elçilerin taşıdığı aktarım bir çizgi, arzuyu izleyerek yinelenen sapma ikinci çizgi olarak duyulur; bu yan yana geliş onları zorunlu bir karşıtlığa ya da özdeşliğe indirgemez. 5:77'deki topluluk odaktaki elçilerle özdeşleştirilmeden bu ikinci çizgi içinde kalır.

{ar:صِدِّيقَةٌۭ, tr:sıddîka, gloss:doğru ve güvenilir} unvanı 5:83'teki tanıma, hakikat, iman ve şahitlik sırasıyla yeniden açılır. 5:83'te {ar:عَرَفُوا۟ ٱلْحَقَّ, tr:arafû el-hakk, gloss:hakikati tanıdılar} hakikatin tanınmasını, {ar:ءَامَنَّا, tr:âmennâ, gloss:inandık} bu tanımanın imanla karşılık bulmasını, {ar:ٱلشَّٰهِدِينَ, tr:eş-şâhidîn, gloss:şahitler} ise kabulün tanıklık olarak dışa taşınmasını gösterir. Annenin doğru ve güvenilir oluşu bu sırayla buluşunca sıfat, sabit bir övgünün yanında hakikati doğru karşılayıp taşıyan insanî bir rol gibi görünür. Bu bağlantının katkısı, Meryem'i 5:83'teki kişilerle özdeşleştirmek değil, sıddîka unvanındaki güvenilirlik alanını tanıma ve tanıklık hareketiyle genişletmektir.

## Açıklığın Ardından

Âyetin son hareketi ilk cümledeki insanî sınırdan bakışın düzenine geçer. {ar:ٱنظُرْ, tr:unzur, gloss:bak/incele} tekil emir, okuyucuyu görmeye ve olup biteni zihinsel olarak incelemeye çağırır. Yanındaki {ar:كَيْفَ, tr:keyfe, gloss:nasıl} sorusu işaretlerin hangi tarzda açıklandığını sordurur. {ar:نُبَيِّنُ, tr:nubeyyin, gloss:açıklarız} birinci çoğul kişiyle açıklamayı yapan etkin özneyi sahneye çıkarır; fiilin ikinci biçimi anlamı belirginleştiren kasıtlı işi duyurur. Açıklamanın yönü, {ar:لَهُمُ, tr:lehüm, gloss:onlara} içindeki yön veren lâm ile belirlenir: işaretler belirli alıcılar için açıklanır ve bu alıcılar sonraki çevrilme fiilinde çevrilen taraf olarak yeniden görünür. Doğrudan nesne olan {ar:ٱلْءَايَٰتِ, tr:el-âyât, gloss:ayetler/işaretler} belirli çoğul biçimiyle tek bir işareti değil, bilinen işaretler kümesini kurar. Bu kelime işaret, delil, mucize ve ayet alanlarına açılır; bu cümlede açıklanan işaretler yüzü öne çıkar.

Araya giren {ar:ثُمَّ, tr:sümme, gloss:sonra} ilk bakış ile ikinci bakış arasına sıra koyar. İlk {ar:ٱنظُرْ, tr:unzur, gloss:bak/incele} açıklanan işaretlerin nasıl belirginleştirildiğine yönelir; ikinci {ar:ٱنظُرْ, tr:unzur, gloss:bak/incele} aynı dikkat çağrısını insanların bu açıklıktan sonra nasıl çevrildiğine döndürür. {ar:أَنَّىٰ, tr:ennâ, gloss:nereden/nasıl} sorusu {ar:كَيْفَ, tr:keyfe, gloss:nasıl} sorusunu genişletir ve çevrilmenin kaynağını, yönünü ve gerçekleşme biçimini yoklar. {ar:يُؤْفَكُونَ, tr:yu'fekûn, gloss:çevriliyorlar/saptırılıyorlar} edilgen geniş zaman biçimi çevrilenleri ve süren sonucu öne çıkarırken failin adını açık bırakır. Doğrultudan tersine çevrilme basıncı, sapmayı doğru yönden uzaklaştırılmış bir yöneliş olarak duyurur. Bu görüntü yön değişimini öne çıkarır; fiil tek başına fiziksel dönmeyi ya da tek bir psikolojik sebebi belirlemez.

Bu iki panel açıklık ile alımlamayı birbirine bağlayan gerilimi görünür kılar. 6:46'da açık işaretlerin görünürlüğü, 34:43'te anlamın anlaşılır oluşu, 3:78'de sözün çarpıtılması, 45:7'de ısrarlı yalanın sürmesi öne çıkar; dört katkı birlikte, anlam görünür ve anlaşılır hale gelirken söz veya yönelişin onu çarpıtabilmesini açıklar. 5:72'de inkâr ve yanlış söz, 5:73'te birlik sözü karşısındaki sapma, 5:77'de arzuların izlenmesi ve sapma sözlerinin yinelenmesi, {ar:يُؤْفَكُونَ, tr:yu'fekûn, gloss:çevriliyorlar/saptırılıyorlar} fiilinin doğruluk hattından kopma yönünü ayrı ayrı belirginleştirir. Bu temas, çevrilme fiilindeki yalan çağrışımını doğruluktan saptırılan söz ve yönelişin sonucuyla birlikte duyurur; fiilin anlamı böylece “yalan” sözcüğünden daha geniş olan doğrultu değişimini korur. İkinci bakış, açıklığın karşısında alımlamanın başarısızlaşabildiğini sorar; işaretin görünürlüğü korunurken çevrilmenin iç sebebi açık bırakılır.

Açıklanmış işaretlerle karşılaşmanın üç farklı karşılığı, bakışın alımlama sonucunu kendiliğinden belirlemediğini gösterir. 5:71'de gözlerin görmez, kulakların işitmez hale gelmesi duyusal kapanmayı, ardından tövbe ederek aynı düşüşe dönülmesi ise kapanmanın tekrarlanan dönüşünü örnekler. 5:83'te işitme, göz, taşan yaş, hakikati tanıma ve iman, işaretin içte ve dışta karşılık bulduğu yolu birlikte gösterir; 5:86'da görünür işaretlerin inkârı açıklanmış nesne karşısındaki reddi belirginleştirir. Bu üç bağlam, odaktaki iki {ar:ٱنظُرْ, tr:unzur, gloss:bak/incele} emrinde görme ile kavrayışı ayrı aşamalar olarak gösterir; bakışın sonucu tek başına belirlenmez. Bu görüntülerin odaktaki katkısı, kişilere fiziksel körlük, sağırlık veya gözyaşı hükmü vermek değil, işaretlerin açıklığından sonra yönelişin alımlanma biçimlerini görünür kılmaktır.

Fâtiha'daki üç kelime teması, açıklık ve yöneliş hareketine yerel bir yankı kazandırır. 1:2'deki {ar:العالمين, tr:el-âlemîn, gloss:âlemler} sözü, {ar:ٱلْءَايَٰتِ, tr:el-âyât, gloss:ayetler/işaretler} içindeki işaretin bir şeyi tanıtan ve görünür kılan yüzünü genişletir. 1:6'daki {ar:اهدنا, tr:ihdinâ, gloss:bizi hidayet et} yön gösterme hareketini, {ar:الصراط المستقيم, tr:es-sırât el-müstakîm, gloss:dosdoğru yol} doğru yolun biçimini belirginleştirir; 1:7'deki {ar:الضالين, tr:ed-dâllîn, gloss:sapanlar} bu yol karşısındaki sapmayı görünür kılar. Bu temas, ayetleri açıklanan içerik olarak korurken onlara yönü okunabilir kılan gösterge katkısı verir; {ar:يُؤْفَكُونَ, tr:yu'fekûn, gloss:çevriliyorlar/saptırılıyorlar} da bu göstergeyle doğru yol arasındaki temasın koparılma hareketini adlandırır. Yankı 1:2, 1:6 ve 1:7'deki kelime ilişkileriyle sınırlı bir yerel okumadır; 1:3, 1:4 ve 1:5'teki tekrarlar bu bağlantının kapsamını genişletmez, dolayısıyla açıklama Fâtiha'nın tamamına yayılmadan işaretin yönü okunur kılması ve insanların bu açıklık karşısında çevrilmesi sorusunu canlı tutar.

</editorial_prose>
