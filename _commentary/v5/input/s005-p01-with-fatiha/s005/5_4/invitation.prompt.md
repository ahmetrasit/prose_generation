# V5 reading invitation — 5:4

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

`_commentary/v5/editorial/s005-p01-with-fatiha/s005/5_4/5_4.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s005-p01-with-fatiha/s005/5_4/5_4.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
Bu âyet, kendilerine neyin helal kılındığını soran topluluğa verilen doğrudan cevaptır. Temiz ve iyi şeylerin helal kılındığı bildirilir; Allah'ın öğrettiği biçimde av için eğitilmiş hayvanların onlar için tuttuklarından yemelerine izin verilir. Ardından tutulan avın üzerinde Allah'ın adı anılır, Allah'a karşı gelmekten sakınılır ve hesabın çabuk görüleceği hatırlatılır. Hüküm böylece izin verilen şeyi, o şeyin elde edilişini, yenmesini, adlandırılmasını ve sorumluluk altında kullanılmasını aynı hareket içinde gösterir.

## Sorunun Cevabı

Âyetin başındaki {ar:يَسْـَٔلُونَكَ, tr:yas'alūnaka, gloss:sana soruyorlar} ifadesi, Peygamber'e yöneltilmiş canlı bir hukukî soruyu başlatır. {ar:مَاذَآ, tr:mādhā, gloss:ne} soruyu tek bir nesneye değil, helal kılınan şeylerin kategorisine açar. İlk {ar:أُحِلَّ, tr:uḥilla, gloss:helal kılındı} pasif biçimi soruyu hukukî bir izin alanına yerleştirir; yanındaki {ar:لَ, tr:la, gloss:için} bu iznin topluluğun kullanımı bakımından sorulduğunu belirtir. {ar:هُمْ, tr:hum, gloss:onlar} soru soranları üçüncü kişi olarak bildirirken, {ar:قُلْ, tr:qul, gloss:de} cevabı açıklama bekleyen bir anlatı olmaktan çıkarıp söylenmesi emredilen söze dönüştürür. Cevapta tekrarlanan {ar:أُحِلَّ, tr:uḥilla, gloss:helal kılındı}, sorunun aynı hukukî kelimesini alarak onu çözer; {ar:لَكُمُ, tr:lakumu, gloss:size} topluluğu doğrudan hükmün muhatabı ve yararlanıcısı yapar. {ar:ٱلطَّيِّبَٰتُ, tr:al-ṭayyibātu, gloss:temiz ve iyi şeyler} izin verilen şeyleri belirli ve çoğul bir sınıf halinde toplar: nitelikçe olumlu, temiz ve kullanılabilir olanlar.

Bu iki {ar:أُحِلَّ, tr:uḥilla, gloss:helal kılındı} biçimi izin hareketini, {ar:ٱلطَّيِّبَٰتُ, tr:al-ṭayyibātu, gloss:temiz ve iyi şeyler} ise bu hareketin ulaştığı niteliği belirler. Hukukî izin, böylece iyi ve uygun olana doğru biçimlenen seçici bir açılma olarak duyulur. Kelimelerin bu yerel teması, izin verilen alanı aydınlatır; âyetin hukukî cevabını başka bir anlama taşımaz.

## Eğitilen Gücün Hareketi

Genel izin kategorisine eklenen {ar:وَ, tr:wa, gloss:ve}, av örneğini aynı hükmün açıklayıcı uzantısı yapar. Av hayvanları adlandırılmadan önce gelen {ar:مَا, tr:mā, gloss:...olan şey} sınıfı eğitilmiş olma şartı altında açar. {ar:عَلَّمْتُمْ, tr:ʿallamtum, gloss:eğittiniz} insanın tamamlanmış eğitimini gösterir; bu rolün ağırlığı av için yetiştirilmiş hayvana verilen talimdedir. {ar:مِّنَ, tr:mina, gloss:arasından} bu eğitimi avcı canlılar arasındaki belirli bir kaynağa bağlar. {ar:ٱلْجَوَارِحِ, tr:al-jawāriḥi, gloss:avı yakalayan yırtıcılar} avı yaralama, avlama ve elde edilecek kazancı taşıma yönleriyle özel av sınıfını adlandırır. {ar:مُكَلِّبِينَ, tr:mukallibīna, gloss:av için eğitenler} odağı hayvanlardan insan eğiticilere çevirir; biçimin ayırt edici katkısı sıradan sahiplikte değil, avı yakalamaya yönelik etkin talimdedir. {ar:تُعَلِّمُونَهُنَّ, tr:tuʿallimūnahunna, gloss:onlara öğretiyorsunuz} eğitimi sürmekte olan bir ilişki olarak kurar ve dişil çoğul zamirle hayvanları öğrenen canlılar halinde tutar. {ar:مِمَّا, tr:mimmā, gloss:...den ve ...şeyden} insan eğitimini içeriği ve kaynağıyla birlikte cümlenin içine alır. {ar:عَلَّمَكُمُ, tr:ʿallamakumu, gloss:size öğretti} insandaki becerinin daha önce alınmış bir öğretime dayandığını gösterir; sonundaki {ar:ٱللَّهُ, tr:Allāhu, gloss:Allah} bu zincirin açık öğretmenidir.

Bu üç öğretme biçiminin ortak katkısı, Allah'tan insana ve insandan hayvana geçen disiplini görünür kılmasıdır. {ar:عَلَّمْتُمْ, tr:ʿallamtum, gloss:eğittiniz} tamamlanmış talimi, {ar:تُعَلِّمُونَهُنَّ, tr:tuʿallimūnahunna, gloss:onlara öğretiyorsunuz} süren eğitimi, {ar:عَلَّمَكُمُ, tr:ʿallamakumu, gloss:size öğretti} ise insanın bu beceriyi kendiliğinden değil, aldığı öğretimle taşıdığını gösterir. Biraz sonra gelen {ar:أَمْسَكْنَ, tr:amsakna, gloss:tutup alıkoydular}, bu aktarımın maddî sonucunu verir: hayvanın yırtıcı kuvveti kendi tüketiminde dağılmayıp avı insanın alacağı noktada tutar. Böylece eğitim, av hükmünü taşıyan gücü başkasına ulaşacak bir teslimata yöneltir; hayvana insan türü bilgi veya bağımsız ahlâkî sorumluluk yükleyen bir okuma kurulmaz.

Öğretenin cümlenin sonunda Allah olarak belirginleşmesi, Fâtiha'daki {ar:ٱلْعَٰلَمِينَ, tr:al-ʿālamīn, gloss:evren ve bütün yaratılmışlar} ifadesinin açtığı dünya ufkuyla da buluşur (1:2). 1:2'de bütün yaratılmışları bir bütün olarak adlandıran bu ifade, 5:4'teki {ar:عَلَّمَكُمُ ٱللَّهُ, tr:ʿallamakumu Allāh, gloss:Allah'ın size öğrettiği} öğretme zincirine döndüğünde, eğitim sahnesini yaşayan varlıklar arasındaki daha geniş bir düzen içinde gösterir. Bu ufuk 5:4'ün odağını genişletmekten çok onun içindeki öğretim ilişkisini çevreler; doğrudan konu eğitilmiş av hayvanlarıdır. 1:2 ile 5:4 arasındaki bu temas, yerel bir dünya ufku olarak kalır ve bütün Fâtiha'ya ya da bütün sûreye yayılan bir tez kurmaz.

Koşullar açıklandıktan sonra gelen {ar:فَ, tr:fa, gloss:böylece} tanımı eyleme bağlar. {ar:كُلُوا۟, tr:kulū, gloss:yiyin} yalnızca bir kategorinin hukukî durumunu bildirmez, topluluğu gerçekten yemeye yöneltir. İkinci {ar:مِمَّآ, tr:mimmā, gloss:...den ve ...şeyden} bu yemenin avlanmanın tamamına değil, hayvanların tuttuğu belirli sonuca yöneldiğini gösterir. {ar:أَمْسَكْنَ, tr:amsakna, gloss:tutup alıkoydular} dişil çoğul hayvanları avı yakalayıp serbest kalmasını önleyen özneler yapar. {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:sizin üzerinize ve sizin için} tutulan avı insanlara geri getirir: bu av onlar için fayda ve geçimdir, aynı zamanda onların üzerine düşen bir sorumluluk ilişkisine girer.

Bu yerel öğretim ve tutma dizisi, av bağlamındaki yakın sahnelerle birlikte gücün insan için korunmuş bir sonuca devredilmesini görünür kılar (5:1, 5:2, 5:3). 5:1'deki {ar:ٱلصَّيْدِ, tr:al-ṣayd, gloss:av} ve 5:2'deki {ar:فَٱصْطَادُوا۟, tr:fa-iṣṭādū, gloss:öyleyse avlanın} direnen şeyi arayıp ele geçirme hareketini taşır. Bu hareket 5:4'teki {ar:ٱلْجَوَارِحِ, tr:al-jawāriḥi, gloss:avı yakalayan yırtıcılar} adına döndüğünde, av eylemi hukukî olarak teslim edilecek yakalamanın arka planını oluşturur. Buradaki sınıfın referansı avı yakalayan yırtıcı kuşlar ve kara hayvanlarıdır; avın kendisi, tuzak ve insan uzvu bu referansın dışında kalır. {ar:مُكَلِّبِينَ, tr:mukallibīna, gloss:av için eğitenler} insan talimini bu amaca yöneltir; {ar:أَمْسَكْنَ عَلَيْكُمْ, tr:amsakna ʿalaykum, gloss:sizin için tuttukları} ise gücü avı kendi tüketimine bırakmayıp başkasının alacağı noktada durdurur. Ardından {ar:فَكُلُوا۟, tr:fa-kulū, gloss:artık yiyin} gelir ve 5:3'teki {ar:أَكَلَ ٱلسَّبُعُ, tr:akala al-subuʿ, gloss:yırtıcı hayvanın yemesi} ile karşılaşır: 5:3'te yırtıcının tüketimi öne çıkarken 5:4'te yeme, eğitilmiş yakalamanın insan tarafından alınan son halkasıdır. Bu açıklama, 5:1, 5:2 ve 5:3'ün akit, av, sınır, ölüm ve yırtıcı tüketimi sahneleriyle sınırlı bir ayet-çevresi okumasıdır.

Bu teslim görüntüsüne {ar:ٱلْجَوَارِحِ, tr:al-jawāriḥi, gloss:avı yakalayan yırtıcılar} kelimesinin bedensel yaralama yüzü de katkı verir: deri darbe, saplama veya keskin bir araçla yarılır ve yara oluşur. Bu malzeme, tekrarlanan {ar:عَلَّمْتُمْ, tr:ʿallamtum, gloss:eğittiniz}, {ar:تُعَلِّمُونَهُنَّ, tr:tuʿallimūnahunna, gloss:onlara öğretiyorsunuz} ve {ar:عَلَّمَكُمُ, tr:ʿallamakumu, gloss:size öğretti} biçimlerinin öğrendikleri görevi belirleyen iziyle ve sonucu koruyan {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} eylemiyle birleşir. Yara açabilen güç böylece öğrenilmiş görevi yapan ve sonucu serbest bırakmayan güce dönüşür. 16:79'daki eğitilmiş yaratıkların tutma ve korunan etkinlik yüzü bu kontrol biçimine ayrı bir paralel sunar; 27:36'daki bilginin Allah'tan geldiğini belirginleştiren sahne, öğretimin kaynağını Allah'a bağlayan aktarım halkasını güçlendirir (16:79, 27:36). Bu katkı, âyetin fiziksel yakalama ve yiyecek iznini taşıyan zemin üzerinde çalışır; hayvanlara insanî ahlâkî failiyet vermez.

## İzin İçindeki Sınır

İzin kelimesi burada bağlı bir yapı içinde gerçekleşen seçici açılmayı görünür kılar. 5:1'deki {ar:بِٱلْعُقُودِ, tr:bil-ʿuqūd, gloss:akitlerle bağlanmış} bağlılık, 5:2'deki korunan sınırlar ve serbestleşme sonrasındaki av izni, 5:5'teki {ar:حِلٌّ, tr:ḥill, gloss:izinli ve serbest} yiyecek düzeni ve 5:7'deki {ar:مِيثَاقَهُ, tr:mīthāqahu, gloss:onun sağlam misakı}, 5:4'teki iki {ar:أُحِلَّ, tr:uḥilla, gloss:izinli kılındı} biçiminin çevresine bağlayıcı bir çerçeve koyar (5:1, 5:2, 5:5, 5:7). Hukukî statü değişirken dokunulmazlıklar ve yükümlülükler görüş alanında kalır. Bu nedenle müsaade, yükümlülük içinde açılan belirli bir kapı olarak duyulur. İlişkinin kapsamı ayet çevresindeki izin, misak ve korunan sınır dilidir; kelimenin başka bağlamlardaki bütün kullanımlarını tek bir sözlük açıklamasında birleştirmez.

Bu seçici açılmanın 5:1 ile 5:4 arasında kurulan daha dar bir biçimi de vardır. 5:1'deki {ar:أَوْفُوا۟, tr:awfū, gloss:yerine getirin ve tamamlayın} fiili bağın bütünüyle sürdürülmesini, {ar:بِٱلْعُقُودِ, tr:bil-ʿuqūd, gloss:akitlerle bağlanmış} ise bu sürdürmenin bağlayıcılığını taşır. Bu iki hareket 5:4'teki ilk ve ikinci {ar:أُحِلَّ, tr:uḥilla, gloss:izinli kılındı} formuna döndüğünde, izin tamamlanmış bir yükümlülüğün ardından gelen yetkili açılma olarak görünür (5:1, 5:4). Bu, 5:1'in tamamlama ve bağlanma diliyle kurulan ihtiyatlı bir metin-içi ilişkidir; 5:1'deki akit emri ile 5:4'teki yiyecek izni, ortak bir maddî mekanizma olmadan art arda gelen iki ayrı konu olarak da yerini koruyabilir.

5:3'ün ölüm, tüketim ve tamamlama görüntüleri, yırtıcı gücün nesne üzerindeki geçmişini 5:4'teki tutma eyleğine bağlayan kesilebilir bir süreç kurar. 5:3'teki {ar:ٱلْمَيْتَةُ, tr:al-maytah, gloss:leş} başarısız ve tamamlanmamış ölümün sonunu, {ar:أَكَلَ ٱلسَّبُعُ, tr:akala al-subuʿ, gloss:yırtıcı hayvanın yemesi} yırtıcının tüketimini, {ar:ذَكَّيْتُمْ, tr:dhakkaytum, gloss:usulüne göre müdahale edip tamamladınız} ise tamamlayıcı müdahaleyi gösterir. 5:4'teki {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular}, süreç bitmeden korunup devredilebilen nesnenin durağını getirir (5:3, 5:4). Böylece hükümdeki ayrım, sabit bir hayvan niteliğinin yanı sıra başarısız ölümden olası tamamlanmaya ve oradan korunmuş teslime uzanan kuvvet geçmişi olarak da okunabilir. Kuralların ayrı statü işaretleri halinde kalması, bu süreç okumasının yanında canlı duran karşı okumadır.

Eğitilmiş tutma, 5:2 ve 5:11'deki iki ayrı güç sahnesiyle birleştiğinde, işe yarayan kuvvetin durabilen ve yönlendirilebilen kuvvet olduğunu gösterir. 5:2'deki {ar:تَعْتَدُوا۟, tr:taʿtadū, gloss:sınırı aşmayın} sınırın ötesine taşan hareketi, {ar:تَعَاوَنُوا۟, tr:taʿāwanū, gloss:yardımlaşın} başkasının iyiliğine yönelmiş kapasiteyi taşır. 5:11'deki {ar:يَبْسُطُوا۟ أَيْدِيَهُمْ, tr:yabsuṭū aydiyahum, gloss:ellerini uzatmaları} saldırıya ilerleyen gücü, {ar:فَكَفَّ أَيْدِيَهُمْ, tr:fa-kaffa aydiyahum, gloss:ellerini geri tuttu} ise bu güce uygulanan engeli gösterir (5:2, 5:11). Bu katkılar 5:4'teki {ar:مُكَلِّبِينَ, tr:mukallibīna, gloss:av için eğitenler} ve {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} ile buluşunca, eğitim gücü üretmenin yanında onu duracağı noktaya kadar yönlendirme işi de yapar. Buradaki temas, insanî sınırlama sahnelerinin av hükmünü açıklayan zorunlu bir kuralını değil, bu hüküm içinde beliren durma şartını görünür kılar.

{ar:ٱلطَّيِّبَٰتُ, tr:al-ṭayyibātu, gloss:iyi ve temiz olanlar}ın bir başka katkısı, 5:6'daki arınma ve kolaylaştırma sahnesinin ışığında belirir. 5:6'daki {ar:فَٱطَّهَّرُوا۟, tr:fa-iṭṭaharū, gloss:arının} ve {ar:لِيُطَهِّرَكُمْ, tr:li-yuṭahhirakum, gloss:sizi temizlemek} biçimleri kirlenmeden temiz duruma geçişi, {ar:صَعِيدًا طَيِّبًا, tr:ṣaʿīdan ṭayyiban, gloss:uygun ve temiz toprak} su bulunmadığında işe yarayan maddeyi, {ar:حَرَج, tr:ḥaraj, gloss:sıkıntı ve daraltıcı güçlük} ise geçişi bozan zorluğu gösterir (5:6). Bu ayrıntılar, iyi olanı gerekli dönüşümü amacını bozmadan taşıyabilen elverişli malzeme olarak renklendirir. 5:4'teki yiyecek kategorisi hukukî ve olumlu niteliğini korur; 5:6'nın katkısı bu kategoriyi toprağa çevirmek değil, uygunluk boyutunu açmaktır.

5:5'teki başka bir bedensel iştah, 5:4'teki yiyecek izninin yönetilmiş bedenî alımlar içindeki yerini görünür kılar (5:5). {ar:ٱلطَّيِّبَٰتُ, tr:al-ṭayyibātu, gloss:iyi ve temiz olanlar}ın yeme eylemine açılan tarafı, 5:5'teki {ar:طَعَامُ, tr:ṭaʿām, gloss:yiyecek} ile {ar:ٱلْمُحْصَنَٰتِ, tr:al-muḥṣanāti, gloss:korunmuş ve dokunulmaz kişiler} ve {ar:مُسَافِحِينَ, tr:musāfiḥīna, gloss:bağ dışına taşan ilişki yaşayanlar}ın çizdiği korunan ve bağ dışına taşan yakınlık ayrımıyla temas eder. Böylece 5:4'teki bedensel alım, hukukî biçim içinde düzenlenen daha geniş bir alanın ilk üyesi gibi okunur. Yiyecek ve yakınlık hükümlerinin her biri kendi konusu ve sınırıyla kalır; bu yerel temas kişileri av sahnesine taşımaz.

## Adın Gıdaya Eşlik Etmesi

Yemenin yanına gelen {ar:وَ, tr:wa, gloss:ve}, ad anmayı yeme emrine bağlar. {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın ve söyleyin} burada içteki hatırlamanın yanı sıra avın üzerinde sözle anma ve çağırma eylemini emreder. {ar:ٱسْمَ, tr:isma, gloss:adı} anılacak şeyi belirli kılar; {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah'ın} adın kime ait olduğunu, {ar:عَلَيْهِ, tr:ʿalayhi, gloss:onun üzerine} ise sözün tutulmuş avın kendisine veya onun yemeğe dönüşen olayına yöneldiğini gösterir. Anma böylece tutulan sonucun insanın alımına geçişini söz içinde tamamlayan açık bir işlem olur.

Bu adlandırmanın katkısı, tutulmuş avın kaynağını görünür kılan bir işaret oluşturmasıdır. {ar:أَمْسَكْنَ, tr:amsakna, gloss:tutup alıkoydular} avı elde tutulan ve kimliği korunabilen bir nesne haline getirir; {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın ve söyleyin} bu nesne üzerindeki sözlü aktarımı, {ar:ٱسْمَ, tr:isma, gloss:adı} ise yetkiyi belirleyen adı taşır. İşaret görüntüsü, adın nesne veya hayvan üzerinde fiziksel bir damga olmasını değil, adlandırmanın avın kimin yetkisiyle devredildiğini görünür tutmasını anlatır. Olağan Allah'ın adını anma emri bu görüntünün zeminidir; isim, aktarımın kaynağını belirginleştirir.

5:4'teki {ar:وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ, tr:wa-udhkurū isma Allāhi ʿalayhi, gloss:üzerinde Allah'ın adını anın} emri, sûrenin başındaki {ar:بِسْمِ ٱللَّهِ, tr:bismi Allāh, gloss:Allah'ın adıyla} açılışına yerel bir dönüş yapar (5:0). Açılışta kurulan adlandırma çerçevesi, burada tutulmuş yiyeğin üzerinde yeniden kurulduğu için emir av sahnesinin içinde süreklilik kazanır. Bu dönüş 5:0'daki basmala ile 5:4'teki adlandırma ve ilahî isim ifadesine aittir. {ar:ٱسْم, tr:ism, gloss:bir varlığı tanıtan ad} ile {ar:ٱللَّهِ, tr:Allāhi, gloss:Allah'ın özel adı} ayrı iş görür; ilişki bütün sûreye yayılan bir ritüel mimarisine dönüşmez.

Ad anma emri 5:7 ve 5:11'deki nimet hatırlamasıyla buluştuğunda, yiyecek üzerindeki sözlü kabulün katkısı genişler (5:7, 5:11). 5:4'teki {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:sözle anın ve hatırlayın} ile 5:7'deki {ar:ٱذْكُرُوا۟ نِعْمَةَ ٱللَّهِ, tr:udhkurū niʿmata Allāh, gloss:Allah'ın nimetini anın} arasındaki tekrar, adlandırmayı ilahî lütuf ve yükümlülük ilişkisini hatırlatan etkin bir söze dönüştürür. 5:11'deki nimet hatırlaması aynı pratiği taşır; bu nedenle tutulan yiyecek üzerindeki anma, yeme hükmünü korurken nimetin ve borcun farkında olma yönünü açar. İlişki 5:4, 5:7 ve 5:11'deki bu anma biçimleriyle sınırlıdır.

6:118 ve 6:119'daki adı anılarak yeme sahneleri, 5:4'teki sözlü atfın yakalama ile tüketim arasındaki geçişi nasıl düzenlediğini gösterir; 6:121'de Allah'ın adı anılmadan yenilen, bu düzenin karşıt sınırını görünür kılar (6:118, 6:119, 6:121). Bu bağlamlarda {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın} bir şeyi dile getirme, {ar:ٱسْمَ, tr:isma, gloss:ad} ise varlığı tanıtıp ondan söz etmeyi sağlayan adlandırma işini taşır. Böylece adın söylenmesi, başka bir canlının elde ettiği şeyin insanın yetkili gıdasına geçişini tamamlayan düzenleyici halka olarak görünür. Bu halka gıda pratiği içindeki işlevini korur; âyetin “yiyin ve üzerine Allah'ın adını anın” buyruğu bu okumanın içinde kalır.

Öğretme ve tutma daha önce kurulduğunda, aynı {ar:ٱسْمَ, tr:isma, gloss:ad} bu bakım ve yetkilendirme zincirini son el değiştirmede kaynağına bağlar. Başka bir canlının elde ettiği şeyi insanın yiyebileceği kaynağa sözle geri bağlayan onarıcı halka, {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın} ile işler; adın kaynağı belirginleştiren tarafı, tutulmuş avın insan gıdasına dönüşünü kapatır (6:118, 6:119). Buradaki kaynak görüntüsü, fiziksel bir yükselme tasviri değil, olağan adlandırma eylemi içinde açılan nitelikli bir çıkarımdır.

## Tutulan Sonucun Dolaşımı

İzin fiili 5:120'deki daha geniş hâkimiyet görüntüsüyle karşılaşınca, 5:4'teki yerel yiyecek izninin kapsamlı bir otorite içindeki sınırlı ve yönetilen işlem yönünü öne çıkarır (5:120). {ar:أُحِلَّ, tr:uḥilla, gloss:helal kılındı} pasif biçimi, bağlayıcı bir kısıtın kalkıp bir şeyin izinli statüye geçmesini taşıyan olağan hukukî işlemdir; 5:120 bu işlemi daha geniş bir çerçeveye yerleştiren bağımsız ve keşif niteliğinde bir tetikleyicidir. Bu temas, 5:4 için yeni bir sözlük veya gramer açıklaması değil, yerel iznin daha büyük bir düzen içindeki konumunu aydınlatan bir perdedir; bütün sûrenin tezini kurmaz.

Tutma eyleminin katkısı, yakalananı yalnızca ele geçirilmiş bir şey olarak bırakmayıp başka bir kişiye devredilecek sonucu korumasıdır. 5:3'teki kontrolsüz ölüm ile tamamlanmış müdahale karşıtlığı ve 5:5'teki karşılıklı yiyecek erişimi, {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} fiiline korunmuş bir emanet yönü verir (5:3, 5:5). Böylece elde tutulan av, muhataba ulaştırılmak üzere saklanan bir sonuç gibi görünür. Bu emanet görüntüsü fiziksel yakalama ve gıda hukuku içinde kalır; hayvan mülkiyeti veya bundan türetilmiş yeni bir hukuk alanına taşınmaz.

5:5'teki karşılıklı erişim, {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} fiilinin yönünü bireysel öğünden düzenlenmiş dolaşıma doğru genişletir (5:5). “Sizin için tuttukları” ifadesi böylece korunmuş avın toplumsal bir gıda transferine açılabilme ihtimalini de taşır; {ar:عَلَيْكُمْ, tr:ʿalaykum, gloss:sizin üzerinize ve sizin için} bu sonucu muhatapların ortak fayda ve sorumluluk alanına getirir. Bu keşif niteliğindeki genişletme, 5:5'teki karşılıklı erişime bağlıdır; her gıda kuralını zorunlu bir değiş tokuş düzenine çevirmez.

## Hesabın Hızı

Yeme ve anmadan sonra gelen son {ar:وَ, tr:wa, gloss:ve} hükmü sakınma tutumuna bağlar. {ar:ٱتَّقُوا۟, tr:ittaqū, gloss:sakının ve kendinizi koruyun} izin verilmiş iştahın çevresine etkin bir öz-koruma koyar; kişi, yanlış sonuca sürüklenmemek için kendi davranışıyla o sonuç arasına koruyucu bir tutum yerleştirir. Ardından gelen {ar:ٱللَّهَ, tr:Allāha, gloss:Allah'a} sakınmanın yönünü belirler. {ar:إِنَّ, tr:inna, gloss:şüphesiz} son cümleyi gerekçeye bağlar; yeniden gelen {ar:ٱللَّهَ, tr:Allāha, gloss:Allah} hesabın kişisel öznesini öne çıkarır. {ar:سَرِيعُ, tr:sarīʿu, gloss:çabuk} hesabı hemen ufukta duran bir sonuç olarak kurar; {ar:ٱلْحِسَابِ, tr:al-ḥisābi, gloss:hesap} izin verilmiş kullanımın her adımını sayılabilir, ölçülebilir ve değerlendirilebilir bir sonuca bağlar.

{ar:كُلُوا۟, tr:kulū, gloss:yiyin} bedensel tüketimi, {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın ve söyleyin} kaynağı dilde hazır tutmayı, {ar:ٱسْمَ, tr:isma, gloss:adı} yetkiyi belirginleştirmeyi, {ar:ٱتَّقُوا۟, tr:ittaqū, gloss:sakının ve kendinizi koruyun} faydalananın koruyucu sorumluluğunu, {ar:سَرِيعُ, tr:sarīʿu, gloss:çabuk} ve {ar:ٱلْحِسَابِ, tr:al-ḥisābi, gloss:hesap} ise bu kullanımın hızla değerlendirmeye açılmasını taşır. Bu işlemler art arda geldiğinde av, adı konmuş ve hesabı görülebilen bir aktarım içinde yenilir; her katkı kendi işini korurken dizi bütün olarak izin, yeme, anma ve sakınmayı birbirine bağlar.

İzin çevresindeki koruyucu bekçi, 5:2'deki sınırı aşmama ve doğru işbirliği, 5:7'deki nimet ile misakı hatırlama, 5:8'deki adalet ve 5:11'de uzanan ellerin geri tutulmasıyla görünür hale gelir (5:2, 5:7, 5:8, 5:11). 5:4'teki {ar:وَٱتَّقُوا۟, tr:wa-ttaqū, gloss:Allah'a karşı sakının} emri bu sahnelerle birlikte, nasıl kullanılacağı gözetilen imkânın canlı sınırını taşır. Sınırı aşan taşma, unutulan nimet ve adaletten ayrılan hareket bu koruyucu çerçevenin karşı kutupları olarak görünür; izin, kullanımın yönünü gözeten bir sorumlulukla birlikte işler. Bu temas farklı bağlamlardaki koruma ifadelerini tek bir sözlük karşılığına indirmeden 5:4'ün kapanışındaki sakınmayı aydınlatır.

## Öğretinin Sadakati

Öğretinin alınıp eyleme geçmesiyle onu kaybetmek veya başka yöne çevirmek arasındaki fark, 5:7, 5:13 ve 5:14'teki hareketlerle bu aktarım görüntüsüne eklenir. 5:7'deki sağlam ahit, işitme ve isteyerek uyma, öğrenilen şeyin kullanılabilir bir sonuca ulaşmasını sağlar. 5:13'teki yönünden saptırma, aktarılmış olanın yolundan çıkarılmasını; 5:13 ve 5:14'teki unutma ise aktarımın bir parçasının yitirilmesini gösterir (5:7, 5:13, 5:14). Bu karşıt hareketler ışığında {ar:عَلَّمْتُمْ, tr:ʿallamtum, gloss:eğittiniz}, {ar:تُعَلِّمُونَهُنَّ, tr:tuʿallimūnahunna, gloss:onlara öğretiyorsunuz} ve {ar:عَلَّمَكُمُ, tr:ʿallamakumu, gloss:size öğretti} öğretme, edinme ve ulaştırma adımlarını; {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} kaybolmasını önleyen korumayı; {ar:ٱذْكُرُوا۟, tr:udhkurū, gloss:anın} da unutmaya karşı hazır tutulan sözlü anmayı somutlaştırır. Bu karşılaştırma, av sahnesinin teknik hayvan davranışı olarak okunan düz anlamıyla birlikte yaşar; insanlar ile hayvanlar arasında ahlâkî bir özdeşlik kurmaz.

Talimatla hareket eden eğitilmiş avcılarla talimat karşısında geri dönen veya yerinde kalan insan sahneleri, bu sadakat farkını başka bir yönden görünür kılar. 5:21'deki içeri girme hareketi işitilmiş yönlendirmenin eyleme geçmesini, 5:21'deki geri dönme hareketi görevi tamamlamak yerine yönlendirilmiş hareketten çekilmeyi gösterir. 5:24'teki oturup kalma da eylemden son anda uzaklaşan karşılıktır (5:21, 5:24). Bu sahneler 5:4'teki {ar:مُكَلِّبِينَ, tr:mukallibīna, gloss:av için eğitenler} rolü ve {ar:أَمْسَكْنَ, tr:amsakna, gloss:tuttular} ile korunan sonuçla buluşunca, eğitilmiş hayvanların talimatla hareket edip sonucu muhafaza eden avcılar olarak algılanmasını sağlar. Bu karşılaştırmanın alanı, yönergeye bağlı hareket ile geri çekilme arasındaki görsel farktır; hayvanlara insanî ahlâkî failiyet vermez ve 5:24'teki oturmayı doğrudan mahkûm eden bir hüküm kurmaz. Eğitilmiş gücün yönergeyi yerine getirip sonucu koruması, emri duyduğu halde geri dönen ya da yerinde kalan insan hareketlerinin yanında belirginleşir.

</editorial_prose>
