# V5 reading invitation — 18:85

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

`_commentary/v5/editorial/s018-regular-20260912/s018/18_85/18_85.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s018-regular-20260912/s018/18_85/18_85.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
18:85'te dikkat önce cümlenin hareketine yönelir: {ar:فَأَتْبَعَ سَبَبًا, tr:fa-atbaʿa sababan, gloss:derken bir yol veya araç izledi}. Bu yalın ifade, önceki anlatıda imkân verilen öznenin bir yolu ya da aracı izlemeye koyulduğunu bildirir. Cümle başındaki {ar:فَ, tr:fa, gloss:hemen ardından bağlayan parçacık}, bu eylemi önceki verilmiş imkâna bağlar (18:84); böylece sağlanmış imkânın kullanım içinde harekete geçişi öne çıkar. {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} da hareketi soyut bir "sebep" olarak bırakmayıp adı konmamış bir güzergâh veya vasıta üzerinde toplar. Yolun nereye vardığı ve sonucun ne olacağı bu kısa cümlede açık bırakılır.

Bu geçişin gerisinde 18:84'teki {ar:مَكَّنَّا, tr:makkannā, gloss:imkân verdik} ve {ar:ءَاتَيْنَاهُ, tr:ātaynāhu, gloss:ona verdik} ifadeleri vardır. Daha önce güç ve araç verilen kişi, adı yeniden anılmadan şimdi o imkânı kullanan fail olur. Etkin üçüncü tekil biçim yeni bir kişi eklemeden bu değişimi kurar; imkân pasif bir ayrıcalık olarak kalmaz, eylemde işlerlik kazanır. {ar:فَ, tr:fa, gloss:hemen ardından bağlayan parçacık}, önceki sağlanmayla sonraki fiil arasındaki doğrudan kullanım sırasını duyurur. Böylece imkân ile insan fiilinin eklemi belirginleşir; araç, failin eylemi ve sonraki yönelişle birlikte anlam kazanır.

{ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilinin tamamlanmış etkin IV biçimi, öznenin bir şeyi bilinçle eyleme sokarak peşine düşmesini ve takibi kararlı bir hareket olarak kurar. Fiilin bağımsız nesnesi olan {ar:سَبَبًا, tr:sababan, gloss:ulaştıran bağ veya araç}, bu hareketin neye yöneldiğini gösterir. Sonlu fiil ile tek açık nesne hareketi başlatmaya yeter; biçim kararlılığı taşırken yön ve varış için sonraki sahneye açık alan bırakır. Okur, ulaşmadan önce başlayan bir takip görür; bu aracın nereye vardığı sonraki sahnede açılır (18:86).

{ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesinin tekil, belirsiz ve mansup oluşu, önceki geniş imkân içinden adı verilmeyen tek bir aracın seçilmesini öne çıkarır (18:84). Bu biçim, tek bir yol-aracı temasını kurar; çoğul bir ağ, tamlamalı göksel erişim veya ayrı bir "sebep kılma" eylemi bu bağlantının parçası değildir. Kelimenin doğrudan nesne olması da yolu çevrede duran bir manzara olmaktan çıkarıp eylemin yöneldiği şey yapar. Böylece {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilindeki ardından gitme basıncı, kişi ya da öğretiyi takip etmekten çok bir aracı izlemeye daralır. Kabul edilmiş bir biçim varyantı aynı yol-aracı nesnesini korurken eylemi kişisel olarak o yola uyma yönünde farklı hissettirebilir; standart yüzeyin kararlı takip anlamı yine yerindedir.

Bu iki kelime kısa bir ses ve görüntü örgüsü içinde de birbirine bağlanır. {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} içindeki kısa ses baskısı takipte çaba ve yönelmişlik duygusu uyandırabilir; fiil ile {ar:سَبَبًا, tr:sababan, gloss:ulaştıran bağ veya araç} arasındaki tekrarlanan **b** sesi de nesneyi eyleme işitsel olarak yaklaştırır. Ses, yeni bir sözlük dalı açmaktan çok bu yakınlığı güçlendirir. Sebebin sıradan bağ ve iplik basıncı, doğrudan nesne oluşuyla işlevsel bir seyahat bağlantısına dönüşür: aynı şey hem izlenen güzergâh hem de verilen imkânı ileri taşıyan araç gibi duyulur. İp imgesi burada bu bağlantının somutluğunu anlatır; 18:85'in kendi nesnesi ise yol ve araç anlamında kalır. Bağ ve erişim duyumu da bu yerel doğrudan nesne ilişkisiyle sınırlıdır.

İlk hareketin sıkılığı, aynı fiil-nesne dizisinin sonraki iki açılışta yeniden belirmesiyle görünür olur (18:89, 18:92). 18:85'teki {ar:فَأَتْبَعَ سَبَبًا, tr:fa-atbaʿa sababan, gloss:derken bir yol veya araç izledi} geçişi önceki imkâna sıkıca bağlanırken, sonraki bağlayıcılarla kurulan tekrarlar yeni aşamalar açar. Aynı kalıp her sahnede yeni bir hareket başlatır; tekrar, üç aşamayı tek bir olayda eritmeden ortak bir ritim kurar. Böylece {ar:سَبَبًا, tr:sababan, gloss:yol veya araç}, sağlanan imkândan izlenen araca ve oradan yeniden açılan aşamalara uzanan bir anlam ipi kurar (18:84, 18:89, 18:92). {ar:فَ, tr:fa, gloss:hemen ardından bağlayan parçacık} ile fiil ve nesnenin geçiş işlevi, cümleyi bağlı sonraki birimin başlangıcı gibi duyurur; bu ritim sonraki aşamaları birbirine bağlarken bütün yolculuğun tek cümleden çıkarıldığı bir sonuç vermez.

Bu yerel takip-aracı ilişkisi, ihtiyatlı bir genişlemede erişim için bilinçle izlenen bağlantılı bir yol görüntüsü açar. {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilinin ardından gitme anlamı, bağımsız olarak önüne gelen {ar:سَبَبًا, tr:sababan, gloss:ulaştıran bağ veya araç} kelimesinin ulaştıran yol ve araç anlamıyla temas eder; hareket yalnızca ilerlemek değil, mevcut konumun ötesine geçmeyi mümkün kılan bir şeyi takip etmek gibi görünür. İzler boyunca bilinçli geri dönüşün anlatıldığı yerde bu fiziksel takip yüzü somutlaşır (18:64). Böylece sıradan "bir yol izledi" zemini işlevsel bir erişim hattı olarak derinleşir; bu hattın katkısı bağlantı kurmaktır, fiziksel ip veya hedef ayrıntısı 18:85'te ayrıca kurulmaz.

Bir başka ihtiyatlı çizgide takip, yolu yalnızca seçmekten ziyade izleri adım adım okuyarak ilerlemek gibi duyulur. Bu araştırma ve iz sürme basıncı {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilinin zaman aralıklarında parçalı ilerleme taşıyan kullanımından gelir; bağımsız tetikleyici, izlerin üzerinde ilerlenebileceği yol ve araç anlamındaki {ar:سَبَبًا, tr:sababan, gloss:ulaştıran bağ veya araç} nesnesidir. Araç bu adımları erişilebilir bir hatta toplar; bu okuma izlerin yöntemli biçimde takip edilmesini görünür kılarken araştırma prosedürünün ve hedefin ayrıntısını açık bırakır. Hedefe doğru sürdürme kararlılığı ve izleri geriye doğru takip, art arda gelen varışlarla birlikte düşünüldüğünde fiil tek hamlelik bir yönelişten çok zaman içinde parça parça ilerleyen bir yöntemi de taşıyabilir (18:60, 18:64, 18:86, 18:89, 18:90, 18:92). Her yeni varış ve geri izleme, önceki işaretin ardından incelenen bir belirti gibi bağlanır; sıradan yol seçimi bu yöntemli takip içinde yerini korur.

Yolun işlerlik kazanması, yönün ve gayretin eşlik ettiği başka temaslarda da belirginleşir. Allah'a yaklaşmak için vesile arama gayretle, dosdoğru yolun izlenmesiyle birlikte anılır (5:35, 6:153); bu temaslar {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilinin bir iz, yön veya buyruk doğrultusunda davranma yüzünü açar. Verilmiş imkânın, yeryüzünde yürüyüp rızık arama, verilenden yararlanarak arama ve gayret edenlere yolların açılmasıyla birlikte düşünülmesi, {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesini yürüyüş ve çabayla etkinleşen bir dayanak olarak duyurur (18:84, 67:15, 28:77, 29:69). Araç bu bağlamlarda failin çabasıyla işlerlik kazanan bir dayanak olarak kalır; sağlanmış kapasite ile onu kullanan hareket aynı düzlemde buluşur.

Göğe doğru uzatılıp sonra kesilen somut ip, {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesindeki tutunarak erişme çekirdeğini ayrı bir görüntü olarak görünür kılar (22:15). İp, kişi ile varış arasında elle tutulur bir bağlantı çizgisi kurar; bu kaynak böylece 18:85'teki aracın hareketi taşıyan bir geçiş unsuru olarak duyulmasını sağlar. İp görüntüsü dış temasın somut katkısıdır; odak cümlesindeki nesne ise yol ve araç anlamında kalır.

## Menzile Ulaşan Takip

18:85'in hedefi açık bırakması, sonraki sahnelerde yolun menzile varmasıyla anlam kazanır. Batı ve doğu sınırlarına {ar:بَلَغَ, tr:balagha, gloss:ulaştı} ile varılır (18:86, 18:90); iki engelin arasına erişim ise {ar:بَيْنَ, tr:bayna, gloss:arasında} ile belirlenir (18:93). Bu temaslar {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesini yalnızca "sebep" olmaktan çıkarıp kişiyi sınıra ve iki engel arasındaki alana taşıyan güzergâh olarak duyurur. 18:85'te açık bırakılan varış, sonraki anlatının açtığı menzillere doğru ilerleyen tamamlanmamış hareket olarak kalır.

Anlatının kendi kuruluşu da bu hareketi ileri taşır. Olayların art arda açılacağını bildiren {ar:أَتْلُوا۟, tr:atlū, gloss:anlatacağım} ve {ar:ذِكْرًا, tr:zikran, gloss:bir anış veya anlatı} ifadeleri bir sunuş başlatır (18:83); aynı yol cümlesinin yeniden kurulması, {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilinin fiziksel takipten anlatıdaki geçişleri düzenleyen bir harekete doğru genişlemesini düşündürür (18:89, 18:92). Tekrarların ardından varış, sınır ve karşılaşma gelir: menziller (18:86, 18:90, 18:93), kuşatıcı ara bilgi (18:91) ve {ar:وَجَدَ, tr:wajada, gloss:buldu} ile bildirilen karşılaşmalar bu alanı genişletir. Böylece "yolu izle, sınıra ulaş, orada bir durumla karşılaş" ritmi, her sahnenin kendi menzilini koruyarak 18:85'teki takip eylemini anlatısal bir geçiş olarak görünür kılar.

Bu menzil duygusuna daha silik bir çevre tonu eşlik eder. Geniş, açık ve sınırları ancak hareketle kavranan arazi, {ar:الْأَرْضِ, tr:al-arḍ, gloss:yeryüzü} ile başlayan ve batı sınırıyla güneşin batışını anan sahnede belirir (18:84, 18:86). Görüntü, izlenen yolun önündeki açıklığı artırır ve batı sahnesinin tonunu besler. Böylece {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesinin sözlük çekirdeği değişmeden, menzile doğru ilerleyen olağan yol okumasına ihtiyatlı bir görsel alt ton eklenir.

Yolun sonundaki karşılaşma erişimi bir karar alanına bağlar. Karşılaşılan toplulukla nasıl muamele edileceği {ar:تَتَّخِذَ, tr:tattakhidha, gloss:edinmek veya seçmek} ve {ar:حُسْنًا, tr:ḥusnan, gloss:güzel davranış} ile; yanlış eylem ile sonuç ve iyi karşılık ise {ar:ظَلَمَ, tr:ẓalama, gloss:zulmetti} ve {ar:جَزَاءً, tr:jazāʾan, gloss:karşılığı} ile ayrılır (18:86, 18:87, 18:88). Takip edilen yol böylece fiziksel erişimi, erişimin ardından gelen muamele ve karşılık sorusuna bağlar. Bu hesap verebilirlik katmanı {ar:سَبَبًا, tr:sababan, gloss:izlenen araç} kelimesinin doğrudan sözlük anlamı değil, batı menzilindeki karar ve sonuç sahnesinin takip eylemine kattığı nitelikli genişlemedir; 18:85'in açık bıraktığı eylem burada belirli bir hüküm seçmeden bu karar alanına ulaşır.

İlk varışın bu sorumluluk ufku, izleyenlerin ve sebeplerin sonuç alanını birlikte gösteren sahneyle başka bir açıdan da temas eder (18:86, 2:166). {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} burada sahip olunacak sabit bir sonuçtan çok, kişiyi karşılaşmaya taşıyan bir eşik gibi duyulur; {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} bu eşiğe doğru etkin hareketi kurar. İzleyenlerin ayrışması ve {ar:وَتَقَطَّعَتْ بِهِمُ ٱلْأَسْبَابُ, tr:wa-taqaṭṭaʿat bihimu al-asbāb, gloss:sebepler onlarla birlikte koptu} ifadesinin aynı sonuç alanını açması, takip edilen olaydan kişinin üzerinde kalan ve yerine getirilmesi beklenen hak, istem veya yükümlülük duygusunu çağırır (2:166). Yolun açtığı karşılaşma, hoş olmayan bir sonuç, yük veya haksızlığın sorumluluğunu üstlenme ihtimalini de taşır. Bu temas, 18:85'teki eylemi hukukî ya da eskatolojik bir hükme sabitlemeden karşılaşma ufkunu genişletir.

Aynı sahne, aracın işlerliğinin sürekliliğe bağlı bir bağ olduğunu somutlaştırır (2:166). Sebeplerin kesilmesi, bir şeyi kesilmiş duruma getirme ayrıntısını odaktaki ulaştırıcı araçla buluşturur: çalıştığı sürece yol kişiyi sonuca bağlar, bağ koptuğunda erişim durur. İzleyenlerin birbirinden ayrılması da bu bağlantının iki taraf arasında karşılıklı kopabileceğini duyurur. Böylece imkân, bir kez edinilmiş sabit bir nesne değil, işlerliği korunması gereken bir ilişki gibi görünür. Bu bağlantının somut katkısı erişimin süreklilik şartıdır; fiziksel kesme ve akrabalık bağına ilişkin anlamlar ise (2:166)'daki ayrı sahnenin bu odakla kurduğu temasın kapsamı dışındadır.

## Araçtan Yapıya

Yol ve araç fikri, ortak bir yapım sürecinde başka bir biçim alır. Topluluğun {ar:فَأَعِينُونِي بِقُوَّةٍ, tr:fa-aʿīnūnī bi-quwwatin, gloss:bana güçle yardım edin} çağrısı işi birlikte kurmayı ister (18:94). Ardından {ar:زُبَرَ الْحَدِيدِ, tr:zubar al-ḥadīd, gloss:demir kütleleri} yerleştirilir ve {ar:سَاوَىٰ, tr:sāwā, gloss:denkledi} ile ölçülü hâle getirilir (18:95); {ar:ٱنفُخُوا۟, tr:unfukhū, gloss:üfleyin} ile ısıtılır, {ar:أُفْرِغْ عَلَيْهِ قِطْرًا, tr:ufriġ ʿalayhi qiṭran, gloss:üzerine erimiş bakır dökeyim} denilerek kaplanır ve sonuçta {ar:نَقْبًا, tr:naqban, gloss:delik veya geçit} bulunamaz (18:96, 18:97). Bu işlemler sırayla ortak emeği, ölçülü yerleştirmeyi, ısıtmayı, kaplamayı ve geçişin kapanmasını kurar. Böylece {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiilindeki takip basıncı bir yöntemi aşama aşama izleme görüntüsüne, {ar:سَبَبًا, tr:sababan, gloss:işleyen araç veya yöntem} kelimesi ise ortak emekle kurulabilen işleyen bir düzeneğe yaklaşır. Bu bağlamsal yapım dizisi, 18:85'in temel çevirisini değiştirmeden yolun birlikte kurulabilen bir araç olarak nasıl somutlaştığını gösterir.

Bu yapımın yönü erişimden koruyucu kapanmaya çevrilebilir. İki setin arasına ulaşılır, bu aralık için yardım istenir, ardından doldurulmuş bir set oluşturulur ve sonunda delik veya geçit bulunamaz (18:93, 18:94, 18:95, 18:97). {ar:السَّدَّيْنِ, tr:as-saddayn, gloss:iki set veya engel} iki engel arasındaki erişim alanını, {ar:رَدْمًا, tr:radman, gloss:doldurulmuş bir set} açıklığın doldurulmasını, {ar:نَقْبًا, tr:naqban, gloss:delik veya geçit} ise geçişin kapanmış sonucunu görünür kılar. Bu işlemler birlikte düşünüldüğünde, açık geçit sağlayan araç sonuç değiştiğinde koruyucu kapamaya hizmet eder. Araç anlamı korunur; değişen, erişim düzeninin yönüdür.

İmkânın sınırı da bu dönüşümün içinde kalır. Verilen güç ve araç, {ar:رَحْمَةٌ, tr:raḥma, gloss:merhamet ve lütuf} olarak anılan nimetin, {ar:وَعْدُ, tr:waʿd, gloss:vaat} ile geleceğe dönük ilahî sözün ve yapının bir gün {ar:دَكَّاء, tr:dakkāʾ, gloss:dümdüz edilmiş} hâle geleceğini bildiren {ar:حَقًّا, tr:ḥaqqan, gloss:gerçek} ifadenin çerçevesine girer (18:84, 18:98). Bu çerçeve, etkili aracı verilmiş, işlerliği koşullu ve vakti geldiğinde aşılacak bir imkân olarak sınırlar.

Bu yol ve yöneliş, başka bir ayetteki {ar:ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ, tr:ihdinā aṣ-ṣirāṭ al-mustaqīm, gloss:bizi dosdoğru yola ilet} çağrısıyla sınırlı bir karşılaştırmaya açılır (1:6). Dosdoğru yol isteği, 18:85'te sağlanan aracın belirli menzillere götüren bir yön taşıyabilmesiyle biçimsel olarak buluşur. Bu temas, 18:85'teki yol ve yön katkısını başka bir ayetteki yöneliş çağrısıyla yan yana getirir; iki cümlenin doğrudan anlamı ve anlatı yapısı ayrı kalır.

Son erişim ufkunda {ar:سَبَبًا, tr:sababan, gloss:yol veya araç} kelimesi, farklı sahnelerdeki göksel erişim tasarımlarıyla temas eder (22:15, 40:36, 40:37, 38:10). Tekil-belirsiz mansup isim, fiilin doğrudan nesnesi olarak sıradan bir imkânı taşımaya devam eder; bu ayrı sahnelerde ise ip, yol, araç ve göğe giriş yönleri belirginleşir. Göğe uzatılıp kesilen ip, erişmek için tutunulan uzun bağlantıyı; göklere ulaşma ve yükselme sebepleri, hedefe götüren yolu; sebeplerle üstünlük arama ise göğe çıkış imkânını kendi gücüyle üretme arzusunu görünür kılar (22:15, 40:36, 40:37, 38:10). İlk görüntü bağlantının fiziksel tutunma biçimini, ikinci görüntü erişimin yön ve katlarını, üçüncü görüntü ise verilmiş kapasiteyle erişimi kendiliğinden üretme arzusu arasındaki gerilimi katkı olarak taşır. Bu temaslar 18:85'teki yol ve araç okumasını genişletir; hedef gökler olarak belirlenmez, {ar:أَتْبَعَ, tr:atbaʿa, gloss:ardından gitti ve izledi} fiili de yükselişi değil önüne verilen yolu izleyen hareketi bildirir.

</editorial_prose>
