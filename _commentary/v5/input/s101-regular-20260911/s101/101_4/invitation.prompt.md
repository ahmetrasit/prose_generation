# V5 reading invitation — 101:4

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

`_commentary/v5/editorial/s101-regular-20260911/s101/101_4/101_4.invitation.tr.md`

Do not add a heading, wrapper label, index, ledger, evidence file, or any other
artifact. Do not modify the editorial prose.

After writing the invitation, run:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s101-regular-20260911/s101/101_4/101_4.invitation.tr.md
```

If validation fails, repair only the reported mechanical file-contract issues
and rerun it, for at most two repair cycles. Report the final validator result
in your response.

<editorial_prose>
İnsanların etrafa saçılmış pervaneler gibi olacağı gün gösterilir. {ar:يَوْمَ, tr:yevme, gloss:gün} sahneyi zamana yerleştirir; {ar:يَكُونُ, tr:yekûnu, gloss:olacağı} insanların gireceği hâli açar; {ar:ٱلنَّاسُ, tr:en-nâsu, gloss:insanlar} bütün insanlığı bu hâlin taşıyıcısı yapar; {ar:كَٱلْفَرَاشِ, tr:kel-ferâşi, gloss:pervaneler gibi} karşılaştırmayı kurar ve {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} görüntüyü dağılmışlıkta tamamlar. İlk elde görülen şey budur: çetin bir günde insan topluluğu, saçılmış pervaneler gibi bir görünüm kazanacaktır.

{ar:يَوْمَ, tr:yevme, gloss:gün} burada günün kendisini tanımlayan bir ad gibi değil, olayın ne zaman görüneceğini bildiren bağlı bir zaman çerçevesi gibi çalışır. Bu biçim, başka bir çekimin günü doğrudan adlandırmaya doğru itebileceği yerde zamanı kurar. Önceki sorudan bu sahneye açık bir bağlaç olmadan geçilmesi, cevabı soyut bir açıklama halinde değil, birdenbire önümüzde beliriveren zaman manzarası halinde verir (101:3). Gün, karşılaşmanın ve dönüşümün sınırları çizilmiş vakti olur; böylece insanların bu hâle ne zaman gireceği ve o anda ne görüleceği birlikte belirir.

Günün ağırlığı yalnızca takvimde duran bir noktadan gelmez. Büyük olayın yaşandığı kritik vakit, insanların toplandığı ve ayrıştığı hüküm anı gibi duyulabilir (44:40, 70:8); bu temas, cümledeki zaman görevini koruyarak günün basıncını artırır. 101:6'daki zaman aralığı ve uzun gece, 101:6'daki gün terazisinin orta noktası ve 101:9'daki uzak zaman teması bu çerçeveye değdiğinde gün hem belirli bir olay vakti hem de ölçülebilen, uzayabilen bir süre olarak duyulur (101:6, 101:9). Zaman aralığı böylece boş bir arka plan olarak kalmaz; insanların ve çevrelerindeki varlıkların değişmesinin içine alınır.

Bu zaman çerçevesini dolu bir sahneye çeviren kelime {ar:يَكُونُ, tr:yekûnu, gloss:olacağı} olur. İnsanlar cümlenin öznesidir; fiil onların içine girdikleri hâli bildirir ve bu hâlin nasıl meydana geldiğini açıklamadan değişimin taşıyıcısını görünür kılar. Uzayan ünlüsü zaman ifadesinden görüntüye geçerken kısa bir bekleyiş bırakır. Oluş ve meydana gelme ağırlığı, insanlığın yeni bir biçimde ortaya çıkmasını hissettirir; aynı kelime ailesinin oldurma ve yaratma çağrışımı burada doğrudan bir yaratma buyruğu kurmadan yeni hâlin varlık ağırlığını artırır.

{ar:يَكُونُ, tr:yekûnu, gloss:olacağı} fiilinin yüklemi, hemen ardından gelen {ar:كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:kel-ferâşi el-mebsûsi, gloss:saçılmış pervaneler gibi} öbeğidir. Pervane görüntüsü fiilin yanına iliştirilmiş bir süs değil, insanların ne hâle geleceğini tamamlayan ilişkidir. Oluş kalıbının gelecek yönü sonucu bitmiş bir rapor gibi kapatmaz; göz önünde açılan bir geçiş duygusu verir. Aynı oluş kelimesinin hemen ardından dağların başka bir dönüşümünü taşıması, insanlardaki çözülmeyi kozmik ölçekte gevşeyen dağlara bağlayan bir geçiş kapısı açar (101:5); iki sahne aynı oluş kalıbıyla birbirine yaklaşır ve bu ayetin payı, dağ benzetmesine ışık tutan insan-pervane sahnesi olarak belirginleşir.

{ar:ٱلنَّاسُ, tr:en-nâsu, gloss:insanlar} dilbilgisel olarak cümlenin merkezindeki özne olsa da, anlamca kendi seçtikleri bir değişimin sahibi değil, kendilerine gelen hâle giren taraftır. Belirli oluşu ve güneş harfiyle birleşen sesi, saçılmadan hemen önce bütün insanlığı tek bir işitsel topluluk halinde toplar. Bu belirli topluluk, yalnızca bir yerde toplanmış korkmuş kalabalığı değil, tür olarak insanlığı sahneye getirir; yayılmanın canlıları alana serme yönü burada insanlığın kendisine döner. Çok tanıdık bir insan sözcüğü, yanındaki olağanüstü yüklem sayesinde tanıdıklığını korurken aşırı bir hâli görünür kılar.

İnsan kelimesinin yakınlık ve topluluk tarafının mı, yoksa unutma tarafının mı öne çıkacağı bu cümlede tek bir açıklamaya zorlanmaz. Benzetme, hangi basınç duyulursa duyulsun insan adını korur; fakat birbirini tanıyan ve bir arada duran topluluğun ilişkice çözülmüş, aynı alanda bulunup ortak yön taşımayan bedenler halinde algılanmasına izin verir. Önceki soruda muhatap alınan bilme konumundan üçüncü şahısla adlandırılan insan kitlesine geçiş de burada belirginleşir: okur artık yalnızca kendisine sorulanı bilmeye değil, insanlığın sahneye nasıl konduğunu görmeye çağrılır (101:3).

## Benzetmenin Hareketi

{ar:كَ, tr:ke-, gloss:gibi} bağlı biçimde geldiği için karşılaştırmayı ayrı bir durak gibi değil, sonraki kelimeye yapışan bir hareket olarak duyurur. Bu edat insanları pervane görüntüsünün içine yerleştirir ve o görüntünün özelliklerini onlara taşır; karşılaştırma, insanları gerçek böceklere dönüştürmeden çalışır. Üstelik yönettiği öbek, {ar:يَكُونُ, tr:yekûnu, gloss:olacağı} fiilinin yüklemi olduğundan yalnızca "gibi" demekle kalmaz, insanların hangi hâle geleceğini söyler. Önceki sorunun cevabı bu yüzden soyut bir hüküm değil, göz önüne getirilen somut bir yayılma görüntüsüdür (101:3).

{ar:ٱلْفَرَاشِ, tr:el-ferâşi, gloss:pervaneler} belirli tekil biçimiyle tek bir böceği değil, tanınabilir bir görüntü sınıfını topluca önümüze getirir. Kelime, çırpınan küçük canlıyı ve ince, savrulmuş parçayı aynı anda duyurabilecek bir açıklık taşır; yerel cümle pervane görüntüsünü öne çıkarırken kırılgan ve yayılmış madde basıncını da açık bırakır. Aynı kelime ailesinde açıp yayarak hazırlanmış bir yüzeyin, serilmiş bir örtünün veya yere bırakılmış bir döşeğin düzeni de duyulabilir. Bu ilk yerel sahnede bu ek anlamın katkısı, saçılmış ve açıkta kalan insan görüntüsünün içinde düzen ile çözülme arasındaki gerilimi duyurmaktır; serili yüzey imgesi bağlamsal bir yankı olarak kalır.

Pervane kelimesinin ses dokusu da {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} sözcüğünün gelmesinden önce çırpınma ve yayılma hareketini hazırlar. Önceki kelimedeki ş sesinden son kelimedeki dişler arasından çıkan tekrarlı seslere geçiş, anlamdaki dağılmayı işitsel olarak dışarı doğru uzatır. Böylece iki kelimelik benzetme yalnızca "dağınık" niteliğini vermez; hareketli, hafif, kırılgan ve çok parçalı bir görüntü kurar. Serilmiş yüzeyin düzeni bu görüntüyü silmez, onun içinde düzen ile çözülme arasındaki gerilimi canlı tutar.

{ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} bir bütünü ayırıp farklı yönlere dağıtılmış hale getiren pasif biçimi taşır. Etkin dağıtma yönü bu bağlamda maruz kalınan sonuca çevrilir; insanlığın düzeni üzerindeki dış etki görünürleşir ve cümle bu etkiyi yapan failin kimliğini açık bırakır. Son kelime isim-sıfat kuyruğunu kapattığı için saçılmışlık benzetmenin kenarında duran bir etiket değil, insanların içine girdiği son durum gibi belirir. İçeride tutulanın dışarı çıkması ve dökülen bir keder yönünde de basınç bırakabilir; görünen fiziksel dağılma, artık hiçbir şeyin içeride tutulamadığı bir açıklıkla derinleşir. Kelimenin dehşet karşısında korunmuş ve düzenlenmiş rahatlığı çağrıştıran karşıt yüzü de burada yerleşmiş rahatlık yerine çözülmüşlüğü keskinleştirir.

Bu yüzden kelimelerin sırası da önemlidir: gün sahneyi açar, oluş fiili bir hâle geçişi kurar, insanlar o hâlin taşıyıcısı olur, bağlı "gibi" karşılaştırmayı açar, pervane kaynağı hareketi verir ve son sıfat onu saçılmışlıkta kapatır. İnsanların pervaneler gibi oluşu böylece hareketi, hafifliği ve ortak yönün kaybını aynı görüntüde taşır. Saçılma kelimesinin ses ve biçimle kurduğu kapanış, hemen sonraki dağ benzetmesinde daha yoğun bir bütünün gevşeyip çok parçalı hale gelmesine geçit verir (101:5); bu geçiş, insan görüntüsünün açık anlamını genişleten bir devam olarak işler.

## Dağılan Topluluğun Yeni Yönleri

Pervane görüntüsü, kelimenin kendi somut kapasitesinden hareketle ışığa veya ateşe yönelip çevresinde çırpınan küçük uçan böcek ayrıntısını da açabilir. İlerideki ateş ve insanları ateşle birlikte anan uyarı sahnesi bu ayrıntıya değdiğinde (101:11, 66:6), burada görülen dağınık hareket yalnızca biçimsel bir uçuş değil, tehlikeli bir çekim ufkuna açık bir yönelim olarak yeniden duyulur. Bu temas, pervane görüntüsüne tehlikeli bir yönelim katkısı yapar; ateşin bütün topluluğu mu, bir kesimi mi, yoksa yalnızca sonraki bir menzili mi belirlediği açık bırakılır.

Aynı görüntü insan kelimesinin topluluk alanıyla temas ettiğinde sosyal bir çözülme de gösterir. Pervaneler aynı yerde bulunabilir, fakat ortak bir yöne veya birbirini tutan bir ilişkiye sahip olmayabilir; böylece sayıca yakın insan topluluğu ilişkice ayrılmış bedenler gibi görünür. Gece boyunca yayılan tek sıra hayvanlar, küçük veya yük taşımayan evcil hayvanlar ve çobansız dolaşan bir sürüye ilişkin sahneler bu basınca eklendiğinde (101:5, 101:8, 101:9, 21:78), insan-pervane benzetmesine gözetimsiz ve rehbersiz hareket ayrıntısı gelir. Hayvan sahnesinin katkısı, insan topluluğunun yön verici düzenini kaybetmesini sosyal bir sürü görüntüsüyle hissettirmektir; özne ve benzetmenin taşıyıcısı yine insan topluluğudur.

Dağılmışlığın bir başka yerel açılımı görünürlükte belirir. {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} içte tutulanı dışarı vurup bildirme yönüyle, bilme ve farkındalık taşıyan sahnelere değdiğinde dış dağılım kişisel farkların açığa çıktığı bir eşiğe dönüşür. İnsanların gruplar halinde amellerini görmek üzere ayrılması ve herkesin o gün görünür hale gelmesi, saçılmış topluluğun daha sonra ayrı ayrı okunabilecek kişilerden oluştuğunu hissettirir (99:6, 40:16). Fiziksel saçılma burada korunur; pasif biçim bilgiyi dış görünürlüğe taşıyan bir geçiş kurar ve bu geçişi doğrudan bir bilme fiiline dönüştürmeden açık bırakır (101:3, 101:10).

Bu dışa açılma sözün kamusal alana çıkması yönünde de ilerleyebilir. Saklı içeriğin dışarı vurulması, düşünülmeden atılan söz ve dili serbest bırakıp dilediği gibi konuşma görüntüleriyle buluştuğunda (101:5), bedenlerin yayılması gizlilikten söze uzanan sınırlı bir iletişim hareketi kazanır. Kaynaktan bolca dışarı akan içerik ve bilme-farkındalık çizgisiyle birlikte düşünüldüğünde insan gerçekliği gizlilikten boşalan bir akış gibi de görünebilir (101:3). Bu bağlantının katkısı, saçılma ile açığa çıkma arasında bağlamsal bir iletişim hareketi kurmaktır; odaktaki fiziksel dağılma kendi anlamını korur.

Uçuşan görüntü yere doğru serilmiş bir alana da açılır. {ar:ٱلْفَرَاشِ, tr:el-ferâşi, gloss:pervaneler} kelimesinin yayarak düzleme hazırlama yönü, serili halıların ve yatağın kurduğu yüzeyle birleştiğinde hareket eden insanların açık bir zeminde okunabilir hale geldiği sonucu verir (88:16, 56:6). {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} ise sarsıntıdan sonra saçılmış toz görüntüsüyle temas ederek bu yüzeyin üzerine ayrılmış maddeyi yerleştirir (56:6). Önceki çarpan olayın açık ve yüksek yol veya avlu yüzeyi de buna değdiğinde (101:1), insan kalabalığı görünür bir olay düzlemine yayılmış gibi görünür. Halı, toz ve yol burada hareketin ardından beliriveren yüzeyi ve güzergâhı tarif eder; karşılaştırmanın taşıyıcısı yine insan-pervane sahnesidir.

Bu açık alanda yön kaybının nasıl oluştuğuna dair nitelikli bir hareket okuması belirir. Bir şeye çarpma, elle uzanıp fırlatma, düşüş ve bir bütünü farklı yönlere dağıtma görüntüleri birbirine değdiğinde, toplanmış biçimi yerinden eden bir darbe ve aşağı doğru bir vektör duyulur (101:1, 101:9). Günün çetin olayı insanları kararlı ekseninden çıkarır; {ar:يَكُونُ, tr:yekûnu, gloss:olacağı} yeni hâle gelişi, {ar:كَٱلْفَرَاشِ, tr:kel-ferâşi, gloss:pervaneler gibi} titreşen ve ışığa açık hareketi, {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} ise sonunda alana yayılan tozu tamamlar. Sarsıntı, şaşkınlık ve bağların kopması; yayılan sürü ve saçılmış toz, bu dört aşamalı hareketi ayrı ayrı besler (22:1, 22:2, 54:7, 56:6). Sıra imgelerden çıkarılan bir bağlantıdır, cümlenin ilan ettiği zorunlu kronoloji veya tek bir hareket nedeni değildir; tekrarlanan darbe, gerçek bir artçı kadar retorik bir büyütme olarak da kalabilir (101:3).

Bu nedenle gün hem çarpışmanın kritik vakti hem de ölçülen bir aralık gibi duyulur. Güneşin doğuşundan batışına uzanan sayılabilir gün, daha genel bir zaman süresi, uzun gece ve gün terazisinin orta noktası gibi ayrıntılarla karşılaştığında olay tek bir anla sınırlanmayıp uzayan bir eşik kazanır (101:6, 101:9). Bir kişinin geceyi kötü bir halde geçirmesi, insanlar arasındaki düşmanlığın alevlenmesi ve günün büyük olayın kritik vakti oluşu da aynı çevrede bir felaket koşulu kurar (101:5, 101:11). Bu genişleme, {ar:يَوْمَ, tr:yevme, gloss:gün} kelimesinin zaman görevini koruyarak felaketi günün içinde oluşan ve insanları o hâle getiren koşul olarak duyurur.

## Maddenin Çözülmesi ve Yeniden Açılması

Saçılma yalnızca çözülmüş bir kütlenin görüntüsü olmayabilir; yere doğru yayılan ekin, en az üç yapraklı gelişim evresi, ağaç çiçeği ve iç hurma dallarıyla birlikte düşünüldüğünde bir merkezden dışarı yayılan olgunlaşma ve çiçeklenme de görünür (101:5, 101:11). Bu bağlamda dağılma, canlılığın büyüyerek açılması yönünü kazanır. Bu bitki görüntüsünün katkısı, pervane gibi saçılmış insan sahnesine açılma ve gelişme hareketini eklemektir; insan topluluğu odaktaki özne olarak kalır.

İnsan topluluğu ile dağların ardından gelen yün görüntüsü arasında başka bir maddi dönüşüm belirir. Sıkı dokunmuş kumaş ve boyanmış yumuşak yün önce kompakt bir bütünün bağını ve rengini taşır; didilmiş, kabartılmış yün ve pamuk ise aynı malzemenin tel tel gevşemiş halini gösterir (101:5). {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} kelimesindeki ayırıp dağıtma, {ar:ٱلْفَرَاشِ, tr:el-ferâşi, gloss:pervaneler} kelimesindeki açıp yayma hareketiyle buluşunca, toplu biçim bağını kaybederek liflere ayrılmış gibi görünür. İnsan sürüsü ile yün kütlesi bu bağ çözülmesi bakımından birbirini aydınlatabilir; biri topluluğun, diğeri malzemenin çözülüşünü taşıyan iki ayrı resim olarak yerini korur.

İnce ve dağınık yüzey bu kez dokunulabilir bir beden yapısına yaklaşır. Kalın ve kaba beden, bacak kası veya kabarık et, toynak yanları ile kemik ya da demirden ince levha aynı alanda birleştiğinde tabaka, destek ve yere değen kenardan oluşan katmanlı bir gövde hissi doğar (101:5, 101:11). Bu anatomi görüntüsünün katkısı, saçılma alanındaki yüzeyi katmanlı ve dokunulabilir kılmaktır; pervane benzetmesi bu görüntüyü taşıyan çerçeve olarak kalır.

Levhanın altındaki boşluk bir darbenin koruyucu yüzeyi aşmasıyla da açılabilir. Başın özü ve ona ulaşan yara, ince tabaka, kafatasını çatlatan veya kemiğe ulaşan darbe, açılmış yara ve oyulmuş beden görüntüleriyle buluştuğunda yüzeyden desteğe, darbeden açık iç boşluğa giden bir sıra oluşur (101:1, 101:9). Böylece saçılmış topluluk, yıkımın dış yüzeyden içeri ilerleyişini düşünmeye izin verir; yara sahnesi, insan-pervane görüntüsüne yüzeyden içeri ilerleyen bir yıkım ayrıntısı ekler.

Açılmış yüzeyin altında kararmış ve artık bırakmış bir madde de görülebilir. Kuru ağaç veya odun, siyah ve kötü çamur, kararan gece ya da bulut; kapta veya yeryüzünde kalan çok az ince su tabakasıyla birleştiğinde saçılmış görüntünün altına karanlık, kalıntı ve değişmiş bir zemin eklenir (101:1, 101:11). Aynı büyüme çizgisinde kabak, yere doğru yayılan ekin ve yapraklanma canlılığın çekilmesiyle yan yana durur; biçim büyürken ortam kuruyabilir (101:5, 101:11). Bu malzeme ve bitki analojilerinin katkısı, uçuşan insan görüntüsünün altında bir yüzey değişimini duyurmaktır; odaktaki özne ve benzetme insan-pervane olarak kalır.

Serilmiş yüzeyin bir başka sonucu, boş bir zemin yerine hayatı taşıyan ve koruyan hazırlanmış bir yer olmasıdır. Hazır ve erişilebilir geçim imkânı, koruma ve engelleme, bedenin yere veya örtüye serilmesiyle temas ettiğinde saçılma alanı bedenleri barındıran, kaynakları hazır tutan bir habitata yaklaşır (101:5, 101:7, 101:9, 101:11). Taşıyan ve besleyen anne, merkez ve yuva; yatmak, oturmak veya evi donatmak için serilen eşya da bu görüntüyü besler. Böylece açıkta kalan insan-pervane sahnesinin içinde bakım gören bir yuva ve yaşamı sürdüren bir düzen seçilebilir; ev imgesi bu bağlantıda kalabalığın bağlamsal habitatını tarif eder.

## Yön, Varış ve Ateş

İlk bakışta yönsüz görünen yayılma, amaç ve hedef temaslarıyla bir varış güzergâhı da kazanabilir. Bir şeye yönelme, niyet etme, üzerine gitme ve koruma-engelleme; zemine veya örtüye yayılma ve bulunan ya da durulan nokta ile buluştuğunda saçılmış bedenler savunulan bir yere yaklaşan bir hareket halinde görünür (101:3, 101:5, 101:9, 101:11). Kura çekip payları ayırma ve seçilmiş bir noktaya yönelme de bu alanı düzenlenmiş bir varış gibi gösterebilir (101:1, 101:3, 101:9). Açık ve yüksek yol veya avlu, işaret feneri, belirgin bir giriş ve arkasındaki oyuk görüntüleri dağılmış bedenleri dış eşiğin ötesindeki iç boşluğa uzanan bir güzergâha yerleştirir (101:1, 101:9, 101:11). Bu temas saçılmanın içine yön, hedef ve korunma ihtimalini ekler; askeri anlam bu bağlantının kapsamına girmez.

Yere serilen yüzey, bir merkezden çıkan şeyin sonradan bırakıldığı bir kap gibi de düşünülebilir. Anne-kaynak, toplanma noktası ve dönüş referansı; kap veya toplama torbası; açıp yayarak düzleme ve ayırıp dağıtma hareketleriyle buluştuğunda saçılmış pervaneler, bir zamanlar bir yerde tutulan içeriğin dışarı bırakılması gibi görünür (101:1, 101:9). Bu maddi sıra, saçılmanın hem dışarı açılan bir sonuç hem de daha önce bir merkezle ilişkili olabilecek bir hareket olduğunu duyurur; burada kap ve toplama torbası, bu bırakılma ilişkisini görünür kılan maddi ayrıntılardır.

Pervanenin ışık veya ateş çevresindeki çırpınışı ilerideki yanan ateş ve aydınlatma görüntüsüyle yeniden karşılaşınca (101:11), ateş hareketleri düzenleyen sıcak bir çekim noktası gibi görünür. Dağılan bedenler tek bir uç noktaya yaklaşabilir; dağınıklık ile birleşme burada iki farklı ölçekte yan yana durur. Aynı ateş, koruma, uzaklaştırma ve dışarı çıkışı engelleme anlamlarıyla çevreleyen yasaklayıcı bir sınır olarak da kurulabilir (101:11). Çekim merkezi ile içeride çeviren sıcak çevre, ateşin iki ayrı uzamsal işleyişini açık tutar; ateşin herkesin, bir alt grubun veya yalnızca sonraki bir menzilin varış yeri olduğu seçilmez.

Bu yönelim, saçılmanın her zaman son durak olmadığı başka bir hareketi de açar. {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} dışarı yayılmış sonucu verirken, 101:9'daki ana-kaynak ve toplama-merkezi imgesi dağılmış kişilerin yeniden bir referansa bağlanabileceğini düşündürür. Derinliğe düşme, hızla yuvarlanma, bir yere dönme ve yönelme görüntüleri saçılmış yörüngelere korkunç bir çekim merkezi ile geri dönüş yönü verir (101:9, 42:29). Bu hareketin sınırı, yeniden merkezlenmeyi odak sözcüğün zorunlu anlamı veya hemen gerçekleşecek tek sonuç yapmamasıdır; saçılmanın kapanmayan yönünü açık tutan bir karşı hareket olarak kalır.

## Hafiflik, Ağırlık ve İlişki

Pervanenin hafifliği, yalnızca uçuşun fiziksel niteliği olarak kalmayabilir. Önemsiz veya küçük şey, küçümseme, ayrılmadan gevşekçe bükülme ve geceyi kötü durumda geçirme görüntüleriyle buluştuğunda insanlar hem kolay savrulan hem de toplumsal ağırlığı azalmış bedenler gibi görünür (101:5, 101:8, 101:9). Hafiflik, düşüncesizlik ve çalkantı bu hareketi daha huzursuz kılar; kişinin tutunma ve saygınlık payı da azalır. Bu bağın katkısı, görsel benzetmeye yoksunluk ve tutunma kaybı basıncı eklemektir; {ar:يَوْمَ, tr:yevme, gloss:gün} kelimesinin zaman anlamı kendi yerinde kalır.

Hayvan görüntüsü hareketin ötesinde taşıma ve oluşma zincirine de açılabilir. Ağırlaşan gebelik, korunan damızlık deve, dişi devenin rahim damarları, küçük ve yük taşımayan evcil hayvanlar ve aygırın örtme vuruşu; pervane-hayvan temasıyla birleştiğinde bir beden içinde korunan üreme sürecini düşündürür (101:1, 101:5, 101:6, 101:11). Ağırlık burada yükten çok yeni hayatı taşıyan bir koşul haline gelir. Bu biyolojik sahnenin katkısı, saçılma görüntüsünün altında korunmuş oluş ihtimalini açmaktır; kapsamı odak cümlesinin insan-pervane benzetmesine eklenen bağlamsal bir süreçle sınırlıdır.

Açılma ve yayılma düzensizliğe olduğu kadar korumaya da hizmet edebilir. Kuşun kanatlarını açıp yere veya hedefe yaklaşması, tüyleri kabartıp gevşek bir yayılım oluşturması ve bir şeyi ayırıp dağıtma hareketi aynı bedensel alanda buluştuğunda saçılma biçimi yavruyu örten, ısıtan ve koruyan bir kanat hareketi gibi de görünür (101:5). Bu dalın katkısı, dağılmanın içinde koruyucu bir örtme işlemini de görünür kılmaktır; kanat görüntüsü bu koruma hareketini taşır.

Hafiflik ve yönün dışarıdan gelmesi, itaat ve bağımlılık ilişkisini de görünür kılabilir. Hafif karşılık ve boyun eğme, direnç göstermeme, kadın köle veya cariye görüntüsüyle ve düşüşün derinliğiyle temas ettiğinde saçılmış insan sahnesinde bir defalık teslimiyetten uzun süren bağlılığa uzanan bir ilişki belirir (101:8, 101:9). Aynı itaat, seven, güvence veren ve başkası adına sorumluluk üstlenen bir davranış olarak da duyulabilir; böylece davranış yalnızca uyum değil, bir başkasına karşı cevap verebilir olma niteliği kazanır (101:7, 101:8). Bu temasın katkısı, insan sahnesinde bağlılık ve başkasına karşı cevap verebilirlik ilişkisini duyurmaktır; hukukî terim veya literal hizmetkârlık anlamı bu özel bağlantının kapsamı değildir.

İlişki alanı bir düzeltme ve geri dönüş sahnesine de açılır. Hafif karşılık, hoşnut kılma ve vuran bir uyarıyla dizginleme; açılıp yüzeyi düzleyen hareketle birleştiğinde itirazın kesildiği, karşı tarafın yatıştığı ve geçilebilir bir alanın açıldığı ihtimalini verir (101:1, 101:7, 101:8). Sonraki kabul, hayatın sürmesi, yakınlık ve sevinç görüntüleriyle karşılaşınca eski yabancılık ve ürkeklik kalkıp yeniden kurulmuş bir ilişkiye dönüşebilir (101:7). Bu, sosyal çözülmeden sonra kabul gören yeni bir yaşama biçimine geçiş ihtimalidir. Sınırı, sonraki hoşnutluğun bütünüyle başka bir durumu da anlatabilmesidir; bu yüzden dönüş ihtimal olarak açık kalır.

## Görünürlük ve Ölçü

Saçılma kalabalığı ortadan kaldırıyor gibi görünürken kişileri ayrı ayrı seçilebilir hale getirebilir. İnsan türü, insan topluluğu ve tek insan arasındaki geçiş; bir bütünü ayırıp farklı yönlere dağıtma; ağır ve hafif tartılar, ölçü ve ağırlıkla birleştiğinde toplu biçimin kaybı her kişinin ayrı ayrı değerlendirilebildiği bir açıklık üretir (101:3, 101:6, 101:8). Böylece sonraki tartılma, ilk görüntünün sonradan derinleşen bir dönüşü gibi duyulabilir: topluluk önce dağınık bir şekil olarak görünür, sonra kişisel farklar okunur. Bunun yanında ağırlık, bu çözülmeyi açıklamayan sıradan devam okumasını da açık tutar.

Ağırlık bir sayıdan fazlasını da taşıyabilir. Değerli ve yüksek kıymetli ağırlık, malı iyi yönetme, seçilmiş ve güvenilen kişi, başkası için sorumluluk üstlenip güvence olma ve ağırbaşlı sağlam hüküm anlamlarına değdiğinde insanın ölçülmesi bir mülkiyet yönetimi değil, emanet edilmiş bir sorumluluğun hesabı gibi görünür (101:1, 101:5, 101:6). Saçılmış bedenler bu bağlamda ayrı ayrı değerlendirilecek ve taşıdıkları sorumlulukla okunacak kişiler olur; emanetçi görüntüsü normal terazinin anlamına sorumluluk boyutu ekler.

Gün ve oluş fiili geçmişin sesle taşındığı bir hafıza sahnesine de izin verir. Doğal ve yazısız durumdaki kişi, bilme ve farkındalık, yaşlı birinin geçmiş gençliğini anlatmasından doğan ad ve bilinen gündüz sınırlarına bağlı olmayan zaman süresiyle birleştiğinde gün yalnızca tarih değil, aktarılmış bir tanıklık gibi duyulur (101:3, 101:5, 101:9). Buradaki oluş fiili böylece yazıya dayanmayan bir hatırlamanın ve sesle taşınan bilginin sahnesine değebilir; bu katkı, kelimenin doğrudan sözlük tanımı olarak değil, zaman ve farkındalıkla kurulan bağlamsal bir okuma olarak kalır.

Dışarı yayılan biçim, içinin ne taşıdığı sorusunu da açık bırakır. Saklı içeriği açıklama, düşünülmeden dışarı atılan söz, kabak ve yanlış ya da boş konuşma görüntüsüyle buluştuğunda dışarıya taşan form ile içerideki yokluk yan yana gelir (101:1, 101:5, 101:9). Görünür yüzey ile iç doluluk burada ayrı sorular olarak kalır; biçim ile içerik arasındaki ayrım, insan-pervane görüntüsüne dışarı taşan form ile içerideki yokluğu birlikte düşündüren sınırlı bir karşılaştırma ekler.

İlerideki tartılma ve ateş sahneleri odaktaki iki bileşene farklı yönlerden geri döner (101:6, 101:7, 101:8, 101:9, 101:11, 42:29). {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} toplu görüntünün ayrı ayrı değerlendirilecek kişilere açılan yönünü, {ar:كَٱلْفَرَاشِ, tr:kel-ferâşi, gloss:pervaneler gibi} ise ateşe veya ışığa açık tehlikeli hareketi taşır. Okur ilk görüntüyü sonradan derinleşmiş olarak yeniden bulur; bu geri dönüş ateşin kapsamını ve saçılmanın sonucunu açık bırakır.

Gözlem alanı da bu hareketi ölçekte değiştirebilir. Göz bebeğinin kara bölümündeki küçük insan biçimli yansıma, ışık veya ateş çevresinde titreşen böcek ve aydınlatılmış alana dağılan bedenlerle birleştiğinde insanlık görüş alanına serpilmiş küçük noktalar gibi görünür (101:11). Bu, algısal bir ölçek analogisidir: insan adı ve insanların pervaneler gibi saçılmış olduğu olağan sahne, gözlemcinin bakışında küçülerek yeniden çerçevelenir.

Sonunda saçılma kapalı bir yok oluş görüntüsü olarak kalmaz. Dışarıya yayılmış topluluk ile ana-kaynak, toplanma merkezi ve başvuru noktası yan yana geldiğinde dağılmanın ardından ilişki veya referans bulmaya açık bir karşı hareket belirir (101:9, 42:29). {ar:ٱلْمَبْثُوثِ, tr:el-mebsûsi, gloss:etrafa saçılmış} dağılmayı ve saklı farkların açılmasını taşımaya devam eder; ana-kaynak imgesi ise dağılanın yeniden bir merkeze bağlanabilme ihtimalini duyurur. Bu yeniden toplanma, saçılmış pervaneler görüntüsünün dışarı açıldıktan sonra bir yön ve başvuru noktası aramaya devam eden açık hareketini gösterir; hemen gerçekleşen tek sonuç olarak sunulmaz.

</editorial_prose>
