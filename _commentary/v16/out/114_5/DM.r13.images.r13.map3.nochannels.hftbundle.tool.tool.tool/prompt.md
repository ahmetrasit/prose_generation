Focus: 114:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
  a speaker.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/114_5/D.r13/context.md =====
# 114:5 — focus

ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ

Anchor translation (canonical reading, reference only):

O, insanların göğüslerinde vesvese verir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 2 | يُوَسْوِسُ | وَسْوَسَ | و س و س | V |
| 3 | فِى | فِى |  | P |
| 4 | صُدُورِ | صَدْر | ص د ر | N |
| 5 | ٱلنَّاسِ | نَّاس | ن و س | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 114 — full text (context; no pericope)

- 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- 114:2 مَلِكِ ٱلنَّاسِ
- 114:3 إِلَٰهِ ٱلنَّاسِ
- 114:4 مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- 114:5 ◀ focus ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- 114:6 مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ


===== _commentary/v16/work/114_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و س و س (root_001651) — identity root of يُوَسْوِسُ (w2)

- **B001** sessiz iç konuşma veya kötülüğe yönelten iç telkin — sessiz iç konuşma; kötülüğe yönelten iç telkin · birinin içine kötü bir düşünce düşürmek veya ona içten telkinde bulunmak · insanın göğsünde sessiz bir iç konuşma belirmek · iç telkinlerin etkisine kapılmış, sürekli kuruntu duyan · sessiz iç konuşma veya iç fısıltı
  الوسوسة حديث النفس؛ وسوس إلي ووسوس في صدري (ayn)؛ الوسوسة ما يلقيه الشيطان في القلب (jamhara)؛ الوسوسة حديث النفس؛ وسوست إليه نفسه؛ فوسوس لهما الشيطان (sihah)؛ الوسوسة الخطرة الرديئة؛ فوسوس إليه الشيطان (mufradat)
- **B002** belli belirsiz ses veya hafif hareket sesi — gizli, hafif ses veya duyulabilen belli belirsiz hareket sesi · bir nesnenin duyulan hafif hareket sesi
  الوسواس الصوت الخفي من ريح تهز قصبا ونحوه؛ صوت الحلي؛ همس الصائد وكلامه (ayn)؛ وسوسة الشيء إذا سمعت حركته (jamhara)؛ همس الصائد والكلاب وأصوات الحلى وسواس (sihah)؛ صوت الحلي والهمس الخفي؛ همس الصائد وسواس (mufradat)
- **B003** kötülüğe sürükleyen görünmez varlığın sözlükleşmiş adı — kötülüğe sürükleyen görünmez varlığın adı
  الوسواس اسم الشيطان (ayn;sihah)

## ص د ر (root_000849) — identity root of صُدُورِ (w4)

- **B001** göğüs bölgesi — göğüs · göğüsler · göğsün üstte çıkıntılı kesimi · göğsü örten kısa giysi · devenin göğsündeki damga · yükü sabitleyen göğüs bağı · göğsünden rahatsız olan kimse · birinin göğsüne bir şeyle vurmak · göğsü ağrımak · güçlü göğüslü aslan
  الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)
- **B002** ön, üst ya da başlangıç bölümü — ön, üst ya da başlangıç bölümü · mızrağın üst bölümü · işin başlangıcı · toplantının ön kısmı; kitabın veya sözün başlangıcı · okun ortasından ucuna uzanan ön bölümü · ön gövdesi kalın ok · göğsüyle öne çıkıp yarışı geçmek · kitaba giriş bölümü koymak · toplantının başköşesine oturmak
  الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)
- **B003** geldiği yerden ayrılıp dönme — bir yerden ya da durumdan ayrılış · su başından, geldikten sonra ayrılmak · geri döndürmek · su başından dönüşü sağlayan yol
  صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)
- **B004** eylem türetme temeli; çıkış yeri veya zamanı — eylemlerin türediği temel sözcük biçimi · çıkış yeri ya da zamanı
  المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)
- **B005** para ödeme ve güvence yükümlülüğü koyma — birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak · kendisine para ödeme ve güvence yükümlülüğü konmak
  صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)
- **B006** bir şeyin bölümü ya da kümesi — bir şeyin bölümü ya da kümesi
  الصدر الطائفة من الشيء (sihah)

## ء ن س (root_000059) — identity root of ٱلنَّاسِ (w5)

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

===== _commentary/v16/out/s114/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 114:5, and ## Buluşmalar) =====
## Görünen ve örtülü

Surenin son ayeti iki kelimeyi yan yana koyar: {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} ve {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:6}. Bu iki kelimenin kökleri birbirine karşı tanımlanır. İnsan, görünür olduğu için bu adı alır: {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-ins hilâfu'l-cinn ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için bu adı almışlardır, source:"ء ن س,B001"}. Cin ise gözden örtülü olduğu için: {ar:الجن سموا بذلك لأنهم متسترون عن أعين الخلق, tr:el-cinn summû bi-zâlike li-ennehum mütesettirûne an a'yuni'l-halk, gloss:cinler yaratılmışların gözlerinden örtülü oldukları için böyle adlandırıldı, source:"ج ن ن,B005"}. Kökün işleyişi tek bir harekettir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenn setru'ş-şey'i ani'l-hâsse, gloss:cenn kökünün aslı bir şeyi duyudan örtmektir, source:"ج ن ن,B001"}. Bu kök imgeleri her yerde kelimenin ayetteki anlamının yanında duyulur, onun yerine geçmez: ayette "insanlar" ve "cinler" kastedilir, imge bu anlamın arkasından gelen yankıdır.

Bu karşıtlık geriye doğru okunur. "Rab", "Melik", "İlah" diye üç kez anılan ve beşinci ayette göğüsleri hedef alınan "insanlar", altıncı ayete gelince görünenler olarak belirir. Aynı kök görmeyi ve işitmeyi de adlandırır: {ar:آنسته أبصرته وآنست الصوت سمعته, tr:âneston-hu ebsartu-hû ve âneste's-savte semi'tu-hû, gloss:onu fark ettim, gördüm; sesi fark ettim, işittim, source:"ء ن س,B002"}. Görünenler aynı zamanda algılayanlardır. Onlara işleyen ise algının hemen altında durur. Dördüncü ayetin {ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} kelimesi gizli bir sestir: {ar:الوسواس الصوت الخفي من ريح تهز قصبا ونحوه, tr:el-vesvâsu's-savtu'l-hafiyyu min rîhin tehuzzu kasaben, gloss:vesvas, kamışı sallayan rüzgârın gizli sesidir, source:"و س و س,B002"}; yalnızca bir kıpırtı olarak duyulur. Yanındaki {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} saklanmayı ve örtünmeyi söyler {source:"خ ن س,B001"}. Kötülüğün kendi kelimesi {ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} ise ters yönü taşır: {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşertu'ş-şey'e izâ ebraztuhû ve azhartuhû, gloss:bir şeyi ortaya çıkarıp görünür kıldığımda "eşrartu" derim, source:"ش ر ر,B008"} ve {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastuke'ş-şey'e fi'ş-şems, gloss:şerr, bir şeyi güneşe sermendir, source:"ش ر ر,B002"}. Kötülük bir açığa çıkarma kökünden adlandırılır, ama saklanan birine aittir.

Kuran bu sahneyi bahçede kurar. Şeytan Âdem'le eşine fısıldar ve fısıltının amacı açıkça söylenir: {ar:فَوَسْوَسَ لَهُمَا ٱلشَّيْطَٰنُ لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا مِن سَوْءَٰتِهِمَا, tr:fe-vesvese lehume'ş-şeytânu li-yubdiye lehumâ mâ vûriye anhumâ min sev'âtihimâ, gloss:şeytan onlara örtülü kalan çıplaklıklarını açmak için fısıldadı, source:7:20}. İki ayet sonra iş tamamlanır: {ar:بَدَتْ لَهُمَا سَوْءَٰتُهُمَا, tr:bedet lehumâ sev'âtuhumâ, gloss:çıplaklıkları kendilerine göründü, source:7:22}. Saklananın işi açığa çıkarmakla biter. Hemen ardından Allah Âdemoğullarına seslenir ve gözün dengesizliğini adlandırır: {ar:إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ, tr:innehû yerâkum huve ve kabîluhû min haysu lâ terevnehum, gloss:o ve onun takımı, sizin onları göremediğiniz yerden sizi görür, source:7:27}. Surenin görünen insanları, görülmeden gören birine karşı korunmaktadır. Kuran'da cinlerin kendi anlatımı ise sığınmanın yanlış yöne döndüğü bir durumu bildirir: {ar:رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ فَزَادُوهُمْ رَهَقًۭا, tr:ricâlun mine'l-insi yeûzûne bi-ricâlin mine'l-cinni fe-zâdûhum rehakâ, gloss:insten bazı adamlar cinden bazı adamlara sığınırdı, bu da onların azgınlığını artırdı, source:72:6}. Surenin "insanların Rabbine sığınırım" sözü bu sapmanın düzeltilmiş halidir: sığınma görünmeyen tarafa değil, iki tarafın da Rabbine yönelir.

Altıncı ayet fısıldayanın iki sınıftan çıkabileceğini söyler. Kuran aynı ikiliyi peygambere düşmanlık bağlamında verir: {ar:شَيَٰطِينَ ٱلْإِنسِ وَٱلْجِنِّ يُوحِى بَعْضُهُمْ إِلَىٰ بَعْضٍۢ زُخْرُفَ ٱلْقَوْلِ غُرُورًۭا, tr:şeyâtîne'l-insi ve'l-cinni yûhî ba'duhum ilâ ba'din zuhrufe'l-kavli gurûrâ, gloss:ins ve cin şeytanları aldatmak için birbirlerine yaldızlı söz fısıldar, source:6:112}. Yani görünenler de örtülü bir iş yapabilir. Surenin son ifadesi, Kuran'da başka yerde de aynı sözcüklerle durur: {ar:لَأَمْلَأَنَّ جَهَنَّمَ مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ أَجْمَعِينَ, tr:le-emleenne cehenneme mine'l-cinneti ve'n-nâsi ecmaîn, gloss:cehennemi cinlerden ve insanlardan dolduracağım, source:11:119}, {source:32:13}. Yaratılışları da yan yana konur: insan kuru balçıktan {source:55:14}, cann ateşten {source:55:15}. Sonunda yoldan çıkmış olanlar, görmedikleri saptırıcıları görmek ister: {ar:رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ, tr:rabbenâ erine'llezeyni edallânâ mine'l-cinni ve'l-ins, gloss:Rabbimiz, bizi saptıran cin ve insi bize göster, source:41:29}. Görünmezlik orada biter.

Kaynaklar: 114:1–3, 5, 6 ٱلنَّاسِ ء ن س B001; 114:5, 6 ٱلنَّاسِ ء ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B005; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B001; 114:4 شَرِّ ش ر ر B008; 114:4 شَرِّ ش ر ر B002

## Göğüs ve içinde saklanan

Beşinci ayet fısıltının yerini adlandırır: {ar:فِى صُدُورِ ٱلنَّاسِ, tr:fî sudûri'n-nâs, gloss:insanların göğüslerinde, source:114:5}. Göğüs bedenin bir odasıdır, önü yükselen bir kafestir: {ar:الصدرة من الإنسان ما أشرف من أعلى صدره, tr:es-sudretu mine'l-insâni mâ eşrafe min a'lâ sadrih, gloss:insanın sudresi göğsünün üstünde yükselen kısmıdır, source:"ص د ر,B001"}. Altıncı ayetin {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} kelimesinin kökü bu odanın parçalarını da adlandırır: {ar:الجناجن عظام الصدر, tr:el-cenâcin izâmu's-sadr, gloss:cenâcin göğüs kemikleridir, source:"ج ن ن,B016"}. Odanın içindeki kalp de aynı kökten, gizli olduğu için adını alır: {ar:الجنان القلب لكونه مستورا عن الحاسة, tr:el-cenânu'l-kalbu li-kevnihî mestûran ani'l-hâsse, gloss:cenân kalptir, duyudan örtülü olduğu için, source:"ج ن ن,B010"}. Ve kök bir şeyi göğüste saklamayı söyler: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî ekenentuh, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Böylece saldıranın adı ile saldırının yapıldığı odanın kemikleri ve içindeki kalp aynı köke bağlanır: örtülü olan, örtülü bir odaya girer.

Fısıltı tam bu odaya yerleştirilir: {ar:وسوس إلي ووسوس في صدري, tr:vesvese ileyye ve vesvese fî sadrî, gloss:bana fısıldadı, göğsümde fısıldadı, source:"و س و س,B001"}. Ve fısıltı, kişinin kendi kendine konuşmasına benzer: {ar:الوسوسة حديث النفس, tr:el-vesvesetu hadîsu'n-nefs, gloss:vesvese nefsin kendi kendine konuşmasıdır, source:"و س و س,B001"}. İnsan kökü de kendine döner: {ar:كيف ابن إنسك يعني نفسه, tr:keyfe'bnu insik, gloss:"insinin oğlu nasıl" yani kendisi nasıl, source:"ء ن س,B006"}. Bu yüzden fısıltı dışarıdan gelen bir ses gibi değil, kişinin kendi sesi gibi duyulur; tehlikeyi görünmez kılan budur. İkinci ayetin {ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü kalbi bedenin dayanağı sayar: {ar:القلب ملاك الجسد, tr:el-kalbu milâku'l-ced, gloss:kalp bedenin ayakta tutanıdır, source:"م ل ك,B005"}. Fısıltı bedeni ayakta tutan noktaya gider. İlk ayetin {ar:قُلْ, tr:kul, gloss:de, source:114:1} kelimesinin kökü de içte tutulan sözü bilir: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde açığa vurmadığım bir söz var, source:"ق و ل,B012"}. Göğüs iki sözün de yeridir: emredilen sığınma sözü oradan çıkar, fısıltı oraya girer.

İnsan kökü bir eve girmeden önce izin istemeyi de adlandırır {source:"ء ن س,B007"}. Kuran bunu emreder: {ar:لَا تَدْخُلُوا۟ بُيُوتًا غَيْرَ بُيُوتِكُمْ حَتَّىٰ تَسْتَأْنِسُوا۟ وَتُسَلِّمُوا۟ عَلَىٰٓ أَهْلِهَا, tr:lâ tedhulû buyûten gayra buyûtikum hattâ teste'nisû ve tusellimû alâ ehlihâ, gloss:kendi evlerinizden başka evlere, izin alıp halkına selam vermeden girmeyin, source:24:27}. Fısıldayan bu kuralın tersini yapar: göğüs odasına izin almadan girer.

Kuran göğsün içini bilen yakınlığı aynı fiille gösterir: {ar:وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Fısıltının girdiği yerden daha derinde bir yakınlık vardır; sığınılan Rab bu yakınlıktadır. Göğsünü saklamak için bükenler de anlatılır: {ar:يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ, tr:yesnûne sudûrahum li-yestahfû minh, gloss:ondan gizlenmek için göğüslerini bükerler, source:11:5}; elbiselerine bürünseler de {ar:إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ, tr:innehû alîmun bi-zâti's-sudûr, gloss:o göğüslerin özünü bilir, source:11:5}. Sözlükteki "göğüste gizlemek" fiilinin kardeşi Kuran'da da göğüslere söylenir: {ar:وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ, tr:ve rabbuke ya'lemu mâ tukinnu sudûruhum, gloss:Rabbin göğüslerinin gizlediğini bilir, source:28:69}. Kalp göğsün içindedir: {ar:ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ, tr:el-kulûbu'lletî fi's-sudûr, gloss:göğüslerdeki kalpler, source:22:46}. Göğüste oturan bir şeye karşı ilaç da sığınmadır: {ar:إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ مَّا هُم بِبَٰلِغِيهِ ۚ فَٱسْتَعِذْ بِٱللَّهِ, tr:in fî sudûrihim illâ kibrun mâ hum bi-bâliğîh, festeiz billâh, gloss:göğüslerinde yalnızca ulaşamayacakları bir büyüklenme var; Allah'a sığın, source:40:56}. Sonunda göğüslerdekinin hepsi dışarı çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussile mâ fi's-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Göğüs, Kuran'ın açıp genişlettiği bir oda olarak da görünür: {ar:رَبِّ ٱشْرَحْ لِى صَدْرِى, tr:rabbi'şrah lî sadrî, gloss:Rabbim, göğsümü aç, source:20:25}.

Kaynaklar: 114:5 صُدُورِ ص د ر B001; 114:6 ٱلْجِنَّةِ ج ن ن B016; 114:6 ٱلْجِنَّةِ ج ن ن B010; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:5 يُوَسْوِسُ و س و س B001; 114:2 مَلِكِ م ل ك B005; 114:5 ٱلنَّاسِ ء ن س B006; 114:1 قُلْ ق و ل B012; 114:5 ٱلنَّاسِ ء ن س B007

## Sığınma: okunan muska ve bedenin örtüleri

{ar:أَعُوذُ, tr:eûzu, gloss:sığınırım, source:114:1} birine sığınıp ona tutunmaktır, ve fiil kendi Rabbiyle tek ifadede durur: {ar:عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به, tr:âze fulânun bi-rabbihî yeûzu avzen izâ lecee ileyhi va'tesame bih, gloss:Rabbine sığındı, ona kaçıp tutundu, source:"ع و ذ,B001"}. Sığınılan bir kaçış yeridir: {ar:وهو عياذي أي ملجئي, tr:ve huve iyâzî ey melceî, gloss:o benim sığınağım, kaçtığım yerdir, source:"ع و ذ,B001"}. Kök kişinin sığındığı nesneyi de adlandırır: okunan söz ve takılan muska, {ar:العوذة ما يعاذ به من الشيء ومنه قيل للتميمة والرقية عوذة, tr:el-ûzetu mâ yuâzu bihî ve minhu kîle li't-temîmeti ve'r-rukyeti ûze, gloss:ûze sığınılan şeydir; muskaya ve okunan duaya da bu yüzden ûze denir, source:"ع و ذ,B002"}; yazılıp bedene asılan {source:"ع و ذ,B002"}; ve özellikle {ar:العوذة والمعاذة التي يعوذ بها الإنسان من فزع أو جنون, tr:el-ûzetu ve'l-meâzetu'lletî yeûzu bihe'l-insânu min fezain ev cunûn, gloss:insanın korkuya ya da deliliğe karşı sığındığı şey, source:"ع و ذ,B002"}. Atın boynunda gerdanlığın asıldığı yer de bu köktendir {source:"ع و ذ,B005"}. Böylece "de: sığınırım" emri, dilde taşınan bir korunak olur; muskayı taşıyan organ dildir {source:"ق و ل,B002"}. Sığınılan Rab sahip olan, itaat edilen ve düzelten olarak tanımlanır {source:"ر ب ب,B001"}.

Surenin öbür kelimeleri bedenin başka örtülerini getirir. Altıncı ayetin kelimesinin kökü kalkanı ve zırhı adlandırır: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-tursu ve'l-cunnetu'd-dir'u ve kullu mâ vakâke fe-huve cunnetuk, gloss:micenn kalkandır, cunne zırhtır; seni koruyan her şey senin cunnendir, source:"ج ن ن,B008"}; insanı örten elbiseyi, {ar:ما علي جنان إلا ما ترى أي ثوب يواريني, tr:mâ aleyye cenânun illâ mâ terâ, gloss:üstümde gördüğünden başka beni örten bir giysi yok, source:"ج ن ن,B001"}; ve saklanılacak yeri {source:"ج ن ن,B017"}. Beşinci ayetin kelimesinin kökü göğsü örten bir giysiyi bilir: {ar:الصدار ثوب يغطي الصدر, tr:es-sidâru sevbun yugattî's-sadr, gloss:sidâr göğsü örten giysidir, source:"ص د ر,B001"}. Bütün bu örtüler dıştadır; fısıltı ise göğsün içinde, her örtünün altında işler. Zırh ve kalkan dışardan gelen saldırıya yarar; içerden fısıldayana karşı tek örtü, söylenen sığınmadır. Ayrıca aynı kelime iki tarafı adlandırır: örtülü saldıran (cinne) ve kalkan (cunne).

Kuran sığınmayı hep söylenen bir söz olarak verir. İmran'ın karısı doğumdan sonra şöyle der: {ar:وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:ve innî uîzuhâ bike ve zurriyyetehâ mine'ş-şeytâni'r-racîm, gloss:onu ve soyunu kovulmuş şeytandan sana sığındırırım, source:3:36}. Yusuf kapıları kapalı evde: {ar:مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ, tr:meâza'llâh, innehû rabbî ahsene mesvây, gloss:Allah'a sığınırım; o benim efendimdir, bana güzel bir yer verdi, source:12:23}. Meryem ruha karşı: {ar:إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ, tr:innî eûzu bi'r-rahmâni mink, gloss:senden Rahman'a sığınırım, source:19:18}. Musa kavmine: {ar:إِنِّى عُذْتُ بِرَبِّى وَرَبِّكُم, tr:innî uztu bi-rabbî ve rabbikum, gloss:ben benim de sizin de Rabbinize sığındım, source:40:27}, {source:44:20}. Peygambere öğretilen dua da Rabbe bağlanır: {ar:وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ, tr:ve eûzu bike rabbi en yahdurûn, gloss:Rabbim, onların yanıma gelmesinden de sana sığınırım, source:23:98}. İkiz sure de aynı sözle açılır: {ar:قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ, tr:kul eûzu bi-rabbi'l-felak, gloss:de ki: sabahın Rabbine sığınırım, source:113:1}. Kalkan anlamı Kuran'da yanlış kullanılır: münafıklar {ar:ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ, tr:ittehazû eymânehum cunneten fe-saddû an sebîli'llâh, gloss:yeminlerini kalkan edinip Allah'ın yolundan alıkoydular, source:58:16}, {source:63:2}. Giysi ve soyulması da yan yana durur: {ar:لِبَاسًۭا يُوَٰرِى سَوْءَٰتِكُمْ, tr:libâsen yuvârî sev'âtikum, gloss:çıplaklıklarınızı örten bir giysi, source:7:26}, {ar:وَلِبَاسُ ٱلتَّقْوَىٰ ذَٰلِكَ خَيْرٌۭ, tr:ve libâsu't-takvâ zâlike hayr, gloss:takva giysisi ise daha hayırlıdır, source:7:26}; sonra şeytan giysiyi çekip alır {source:7:27}. Dış giysi soyulabilir; takva giysisi içtedir.

Kaynaklar: 114:1 أَعُوذُ ع و ذ B001; 114:1 أَعُوذُ ع و ذ B002; 114:1 أَعُوذُ ع و ذ B005; 114:1 أَعُوذُ ع و ذ B007; 114:1 قُلْ ق و ل B002; 114:1 بِرَبِّ ر ب ب B001; 114:6 ٱلْجِنَّةِ ج ن ن B008; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:6 ٱلْجِنَّةِ ج ن ن B017; 114:5 صُدُورِ ص د ر B001

## Av: mırıltı, sığınak, tetikteki hayvan, korunan bitki

{ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} avcının ve köpeklerinin hafif sesidir: {ar:همس الصائد والكلاب وأصوات الحلى وسواس, tr:hemsu's-sâidi ve'l-kilâbi ve asvâtu'l-hulî vesvâs, gloss:avcının ve köpeklerin fısıltısı, takıların sesleri vesvastır, source:"و س و س,B002"}; ve avın yattığı sazlıktaki hışırtıdır {source:"و س و س,B002"}. {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü ceylanların sığınağını ve ceylanların kendisini adlandırır: {ar:الخنس مأوى الظباء؛ الخنس الظباء أنفسها, tr:el-hunnes me'vâ'z-zıbâ; el-hunnesu'z-zıbâu enfusuhâ, gloss:hunnes ceylanların sığınağıdır; hunnes ceylanların kendisidir, source:"خ ن س,B004"}; bütün sığırlar da basık burunludur {source:"خ ن س,B003"}. Rab kökü yaban sığırı sürüsünü {source:"ر ب ب,B014"}, sığınma kökü yeni doğurmuş ceylanları {source:"ع و ذ,B003"} ve dikenlerin dibinde otlayanların erişemediği bitkiyi bilir {source:"ع و ذ,B004"}. İnsan kökü korkutan bir şeyi sezip etrafına bakan hayvanı adlandırır: {ar:والاستئناس النظر وأحس بما رابه, tr:ve'l-isti'nâsu'n-nazar ve ehasse bimâ râbeh, gloss:isti'nâs bakmak ve kuşkulandıran şeyi sezmektir, source:"ء ن س,B002"}; ve evcili yabaninin karşısına koyar, ısırmayan köpeği ısıranın karşısına {source:"ء ن س,B003"}. Altıncı ayetin kökü saklanma yeridir {source:"ج ن ن,B017"}.

Sahne şudur: bir avcı alçak bir mırıltıyla sokulur; av sığınağında durur; tetikteki hayvan sezer ve etrafına bakar; bir bitki dikenler arasında erişilmez büyür. Fısıldayan mırıldanan avcıdır, ama adıyla sığınağında duran av gibi de saklanır. İnsanlar sezmesi gerekenlerdir. Sığınma, erişilemeyen yerdir.

Kuran avcıyı İblis'in ağzından verir: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ak'udenne lehum sırâtake'l-mustakîm, gloss:senin dosdoğru yolunun üstünde onları bekleyeceğim, source:7:16}, sonra {ar:ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:summe le-âtiyennehum min beyni eydîhim ve min halfihim ve an eymânihim ve an şemâilihim, gloss:sonra onlara önlerinden, arkalarından, sağlarından ve sollarından geleceğim, source:7:17}. Pusuya yatmak, sonra her yandan kuşatmak. Allah İblis'e seslenir: {ar:وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:vestefziz meni'stata'te minhum bi-savtike ve eclib aleyhim bi-hayli-ke ve racilik, gloss:onlardan gücünün yettiğini sesinle ürküt, atlıların ve yayalarınla üstlerine sür, source:17:64}. Ses ile ürkütmek ve sürmek, avcının işidir. Kaçan av da Kuran'da görülür: {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:keennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri, source:74:50}, {ar:فَرَّتْ مِن قَسْوَرَةٍۭ, tr:ferrat min kasvera, gloss:arslandan kaçan, source:74:51}.

Kaynaklar: 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B004; 114:4 ٱلْخَنَّاسِ خ ن س B003; 114:1 بِرَبِّ ر ب ب B014; 114:1 أَعُوذُ ع و ذ B003; 114:1 أَعُوذُ ع و ذ B004; 114:5 ٱلنَّاسِ ء ن س B002; 114:5 ٱلنَّاسِ ء ن س B003; 114:6 ٱلْجِنَّةِ ج ن ن B017

## At ve binici

Surenin beş kelimesi atın bir parçasını ya da koşusunu adlandırır. Binici hayvana insî yandan biner ve sağar: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbe li'l-cânibi'llezî yeli'r-râkib, gloss:hayvanın insîsi biniciye bakan yanıdır, source:"ء ن س,B004"}. Atın bacakları ve boynu onu yönetendir, onun "milk"idir: {ar:ملك الدابة قوائمها وهاديها, tr:milku'd-dâbbe kavâimuhâ ve hâdîhâ, gloss:hayvanın milki ayakları ve boynudur, source:"م ل ك,B008"}. Boynunda gerdanlığın asıldığı girdap sığınma kökündendir: {ar:معوذ الفرس موضع القلادة ودائرة المعوذ تستحب, tr:muavvizu'l-feresi mevdiu'l-kılâde, gloss:atın muavvizi gerdanlığın yeridir; o yerdeki girdap beğenilir, source:"ع و ذ,B005"}. Yeni doğurmuş kısraklar da ûz arasındadır {source:"ع و ذ,B003"}. Hannâs kökünden bir at da vardır: {ar:فرس خنوس وهو الذي يعدل وهو مستقيم في حضره ذات اليمين وذات الشمال, tr:ferasun hanûs, ve huvellezî ya'dilu ve huve mustakîmun fî hudrihî zâte'l-yemîni ve zâte'ş-şimâl, gloss:hanûs at, dörtnala düz koşarken sağa sola sapandır, source:"خ ن س,B005"}. Ve at yarışı göğüsle kazanır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-feresu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle önde gelince "sadera" denir, source:"ص د ر,B002"}.

Fısıldayan, düz bir koşunun içindeki sapmadır: at yolundan çıkmaz ama sağa sola kayar. Sığınma, gerdanlığın asıldığı yerde takılır. Göğüs, yarışı kazanan uçtur; fısıltı tam oraya yerleşir.

Kuran'da İblis'in yaklaşımı aynı iki yönü adlandırır: {ar:وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:ve an eymânihim ve an şemâilihim, gloss:sağlarından ve sollarından, source:7:17}. Şeytana atlılar verilir {source:17:64}. Allah koşan atlara yemin eder: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًۭا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara, source:100:1}, {ar:فَٱلْمُورِيَٰتِ قَدْحًۭا, tr:fe'l-mûriyâti kadhâ, gloss:nallarıyla kıvılcım çıkaranlara, source:100:2}; ve aynı sure göğüslerdekinin ortaya dökülmesiyle biter {source:100:10}.

Kaynaklar: 114:1–6 ٱلنَّاسِ ء ن س B004; 114:2 مَلِكِ م ل ك B008; 114:1 أَعُوذُ ع و ذ B005; 114:4 ٱلْخَنَّاسِ خ ن س B005; 114:5 صُدُورِ ص د ر B002; 114:1 أَعُوذُ ع و ذ B003

## Suya giden yol ve dönüş

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kökü yolun ortasını, {ar:الزم ملك الطريق أي وسطه, tr:ilzem milke't-tarîk ey vesatah, gloss:yolun milkine, yani ortasına sarıl, source:"م ل ك,B006"}; sürünün takip ettiği öndeki hayvanı {source:"م ل ك,B008"}; ve yolcunun yanında taşıdığı, onu ayakta tutan suyu adlandırır: {ar:والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره, tr:ve'l-melku'l-mâu yekûnu mea'l-musâfir, gloss:melk yolcunun yanındaki sudur, çünkü yanında olunca işini elinde tutar, source:"م ل ك,B007"}. {ar:صُدُورِ, tr:sudûr, gloss:göğüsler, source:114:5} kökü sudan dönmeyi, {ar:الصدر الانصراف عن الورد وعن كل أمر, tr:es-sadaru'l-insirâfu ani'l-virdi ve an kulli emr, gloss:sader sudan ve her işten geri dönmektir, source:"ص د ر,B003"}; halkını sudan geri getiren yolu, {ar:طريق صادر يصدر بأهله عن الماء, tr:tarîkun sâdirun yasduru bi-ehlihî ani'l-mâ, gloss:halkını sudan geri getiren dönüş yolu, source:"ص د ر,B003"}; ve dönüşün yerini ve zamanını adlandırır {source:"ص د ر,B004"}. Rab kökü develerin durduğu yeri bilir {source:"ر ب ب,B007"}. Hannâs kökü topluluktan gizlice sıyrılanı bilir {source:"خ ن س,B001"}.

Sahne şudur: bir sürü önderinin ardından yolun ortasından suya gider, içer ve dönüş yolundan geri gelir; biri topluluktan gizlice ayrılır. Beşinci ayetteki çoğul aynı zamanda "dönüşler" diye de duyulur: göğüsler, insanın her işten döndüğü yerdir. Fısıldayan yolun ortasından ayırmaya çalışır.

Kuran bu sahneyi Musa'nın Medyen yolunda kurar: {ar:عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ, tr:asâ rabbî en yehdiyenî sevâe's-sebîl, gloss:umarım Rabbim bana yolun ortasını gösterir, source:28:22}; suya varınca {ar:وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ, tr:vecede aleyhi ummeten mine'n-nâsi yeskûn, gloss:başında su içiren bir insan topluluğu buldu, source:28:23}, ve kadınlar {ar:لَا نَسْقِى حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ, tr:lâneskî hattâ yusdira'r-riâ, gloss:çobanlar sürülerini sudan geri çevirmedikçe biz su veremeyiz, source:28:23} der. Sonunda: {ar:رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ, tr:rabbi innî limâ enzelte ileyye min hayrin fakîr, gloss:Rabbim, bana indireceğin her hayra muhtacım, source:28:24}. Yol, su, insanlar, sudan dönüş ve Rab bir pasajdadır. Surenin iki kelimesi tek cümlede de durur: {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amelleri kendilerine gösterilmek üzere dağınık halde dönerler, source:99:6}. Yolun ortasında pusuya yatan İblis'tir {source:7:16}; yoldaş şeytanlar yoldan alıkoyar: {ar:وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ, tr:ve innehum le-yesuddûnehum ani's-sebîli ve yahsebûne ennehum muhtedûn, gloss:onları yoldan alıkoyarlar, onlar da doğru yolda olduklarını sanırlar, source:43:37}. Topluluğundan koparılan da anlatılır: {ar:كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا, tr:kellezi'steh'vethu'ş-şeyâtînu fi'l-ardı hayrâne lehû ashâbun yed'ûnehû ile'l-hude'tinâ, gloss:şeytanların yerde ayartıp şaşkın bıraktığı, arkadaşlarının "bize gel" diye doğru yola çağırdığı kişi gibi, source:6:71}. Yolun kendisi adlandırılır: {ar:هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:hâzâ sırâtun mustakîm, gloss:bu dosdoğru bir yoldur, source:36:61}.

Kaynaklar: 114:2 مَلِكِ م ل ك B006; 114:2 مَلِكِ م ل ك B008; 114:2 مَلِكِ م ل ك B007; 114:5 صُدُورِ ص د ر B003; 114:5 صُدُورِ ص د ر B004; 114:1 بِرَبِّ ر ب ب B007; 114:4 ٱلْخَنَّاسِ خ ن س B001

## Buluşmalar

İlk buluşma göğüstedir. Örten kök göğsün içinde çalışır: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Görünen ve örtülü imgesi ile göğüs imgesi burada tek sahne olur: görünen insanların içinde, kemik kafesin altında, gizli kalp vardır; örtülü olan, örtülü odaya girer. Kuran'ın göğüslerini bükerek saklananları {source:11:5} da bu sahneye aittir: ne kadar örtünseler de göğüslerin özü bilinir. Sığınma imgesindeki bütün dış örtüler (göğüs giysisi, zırh, kalkan) bu odanın dışında kalır; içerdeki fısıltıya karşı yalnız söylenen söz işler.

İkinci buluşma sözdedir. Sözlük, söylenen sözü "telaffuzla dışarı çıkarılan" diye tanımlarken kullandığı fiili {source:"ق و ل,B001"} kötülük kökünün "ortaya çıkarmak" anlamında da kullanır {source:"ش ر ر,B008"}. Sure böylece iki çıkarma arasında kurulur: sığınma sözü içten dışa çıkar, fısıltının amacı ise örtülüyü açığa çıkarmaktır {source:7:20}. Söz ile çekilme de buluşur: {ar:الشيطان يوسوس فإذا ذكر الله خنس, tr:eş-şeytânu yuvesvisu fe-izâ zukira'llâhu hanes, gloss:şeytan fısıldar, Allah anılınca çekilir, source:"خ ن س,B001"}. "De" emri bu anmayı dile getirir; "sinip çekilen" sıfatı onun sonucunu adlandırır. Söz ile sığınma okunan muskada birleşir {source:"ع و ذ,B002"}: emredilen cümle, dilde taşınan korunaktır.

Üçüncü buluşma gece ile çekilmededir. Hannâs kökü hem geri çekilmeyi hem gündüz gizlenip yörüngesinde dönen yıldızları adlandırır; Kuran onlara yemin eden pasajda deliliği ve şeytan sözünü reddeder {source:81:15}. İbrahim'in gecesinde batanlara karşı {source:6:76} Rab kökünün "yerinden ayrılmayan" anlamı {source:"ر ب ب,B007"} durur. Fısıldayan gidip gelir; Rab batmaz.

Dördüncü buluşma unvanlar ile sığınmadadır: {ar:عاذ فلان بربه, tr:âze fulânun bi-rabbih, gloss:Rabbine sığındı, source:"ع و ذ,B001"}. Fiil ile unvan tek ifadede durur. Ana ve yavru imgesi bu bağa sıcaklık verir: aynı iki kök yeni doğurmuş anneyi adlandırır, ve Kuran'da bir anne yeni doğan kızını Rabbine sığındırır, Rab da onu bir bitki gibi büyütür {source:3:37}. Bağlama imgesi aynı sığınmayı topluluğa genişletir: sığınmanın açıklaması olan tutunmak {source:3:103} bütün insanları tek ipte toplar; kötülük kökü ise parçalar.

Surenin hareketi bu buluşmalarla taşınır. İlk üç ayet aynı insanları üç unvan altında, bir arada ve görünür olarak toplar; dördüncü ayet görünmeyen ve gidip gelen bir fısıltıyı adlandırır; beşinci ayet onu en içteki odaya, göğse yerleştirir; altıncı ayet kaynağını hem örtülülere hem görünenlere açar. Sığınma sözü bu yolun tersinden ilerler: içten dışa, dilde söylenir, ve yerinden ayrılmayan bir Rabbe tutunur.

