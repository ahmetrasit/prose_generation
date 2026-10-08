Focus: 104:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/104_7/D.r13/context.md =====
# 104:7 — focus

ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ

Anchor translation (canonical reading, reference only):

Yüreklere ulaşan.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱلَّتِى | ٱلَّذِى |  | REL |
| 2 | تَطَّلِعُ | طَّلَعَ | ط ل ع | V |
| 3 | عَلَى | عَلَىٰ |  | P |
| 4 | ٱلْأَفْـِٔدَةِ | فُؤَاد | ف ء د | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 104 — full text (context; no pericope)

- 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- 104:5 وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- 104:6 نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- 104:7 ◀ focus ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- 104:8 إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ


===== _commentary/v16/work/104_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ط ل ع (root_000945) — identity root of تَطَّلِعُ (w2)

- **B001** güneşin, ayın, yıldızın veya tanın doğması; doğuş olayı ve yeri [kalıp] — güneşin, tanın, yıldızın ya da ayın doğması · güneşin doğduğu yer veya yön · tanın sökmesi; tan vakti ya da tanın belirdiği yer
  المطلع الموضع الذي تطلع عليه الشمس؛ والمطلع مصدر من طلع (ayn)؛ طلعت الشمس والكوكب طلوعا ومطلعا؛ والمطلع موضع طلوعها (sihah)؛ طلعت الشمس؛ وكذلك طلع الفجر والنجم والقمر؛ المطلع بالفتح هو الطلوع والمطلع بالكسر هو الموضع (tahdhib)؛ طلع الشمس طلوعا ومطلعا؛ والمطلع موضع الطلوع (mufradat)؛ أصل واحد صحيح يدل على ظهور وبروز؛ طلعت الشمس طلوعا ومطلعا؛ والمطلع موضع طلوعها (maqayis)
- **B002** bir topluluğun karşısına çıkmak; ayrı kuruluşta onlardan gözden kaybolmak [kalıp] — topluluğun karşısına çıkmak, yanına gelmek ya da baskın verircesine belirmek; sınırlı bir aktarımda gözden kaybolmak · onların yanından ayrılıp gözden kaybolmak
  طلع علينا فلان يطلع طلوعا إذا هجم (ayn)؛ طلعت على القوم إذا أتيتهم؛ طلعت عنهم إذا غبت عنهم (sihah)؛ يقال طلع فلان علينا من بعيد؛ طلعت على صاحبي إذا أقبلت عليه؛ طلعت على القوم إذا غبت عنهم حتى لا يروك (tahdhib)؛ وعنه استعير طلع علينا فلان واطلع؛ وطلعت عنه غبت (mufradat)؛ طلع علينا فلان إذا هجم (maqayis)
- **B003** bir şeyi öğrenmek ya da başkasına gösterip bildirmek; görüşünü yoklamak [kalıp] — bir şeye yukarıdan bakmak veya iç yüzünü bütünüyle öğrenmek · başkasına bir işi ya da saklı sözü gösterip bildirmek · başını dışarı çıkarıp görünür kılmak · birinin görüşünü öğrenmek için ne düşündüğünü araştırmak · bir şeyi inceleyip içinde ne bulunduğunu öğrenmek
  أطلع فلان رأسه أظهره؛ اطلع أشرف على الشيء؛ أطلع غيره إطلاعا؛ أطلعني طلع هذا الأمر حتى علمته كله؛ استطلعت رأيه (ayn)؛ اطلعت على باطن أمره؛ طالعت الشيء أي اطلعت عليه؛ أطلعتك على سري؛ استطلعت رأي فلان (sihah)؛ اطلع فلان إذا أشرف على شيء؛ أطلع غيره؛ استطلعت رأي فلان إذا نظرت ما رأيه؛ أطلعني فلان (tahdhib)؛ اطلع؛ أطلع الغيب؛ أطلعتك على كذا؛ واستطلعت رأيه (mufradat)؛ أطلعتك على الأمر إطلاعا؛ أطلعتك طلعه؛ استطلعت رأي فلان إذا نظرت ما الذي يبرز إليك منه (maqayis)
- **B004** düşmanı gözlemek için önden gönderilen gözcü veya gözcü birliği — düşmanı gözlemek için önden gönderilen gözcü kişi veya birlik · önden gönderilen gözcü toplulukları
  الطليعة قوم يبعثون ليطلعوا طلع العدو؛ الطلائع الجماعات في السرية (ayn)؛ طليعة الجيش من يبعث ليطلع طلع العدو (sihah)؛ طليعة القوم الذين يبعثون ليطلعوا طلع العدو (tahdhib)؛ وطليعة الجيش أول من يطلع (mufradat)؛ وطليعة الجيش من يطلع طلع العدو (maqayis)
- **B005** palmiye ağacının kapalı çiçek salkımı; salkımın veya ekinin belirmesi — palmiye ağacının henüz açılmamış çiçek salkımı · kılıf içindeki tek bir palmiye çiçek salkımı · palmiye ağacının çiçek salkımını çıkarması · ekinin belirip görünmesi
  الطلع طلع النخلة الواحدة طلعة؛ وأطلعت النخلة؛ وطلع الزرع بدا (ayn)؛ والطلع طلع النخلة؛ واطلع النخل إذا خرج طلعه (sihah)؛ طلع الزرع إذا بدا؛ وأطلعت النخلة إذا أخرجت طلعها؛ الطلع كفراها قبل أن تنشق (tahdhib)؛ تشبيها بالطلوع قيل طلع النخل؛ لها طلع نضيد؛ وقد أطلعت النخل (mufradat)؛ والطلع طلع النخلة؛ وقد أطلعت النخلة (maqayis)
- **B006** dağa çıkma ve çıkış yolu; bir işin yaklaşım yönü veya ürkütücü eşiği [kalıp] — dağa tırmanıp çıkmak · dağa çıkılan yol veya dağa erişilen yön · bir işin ele alınacağı yön veya giriş yolu · yüksekten bakınca önünde açılan ağır durumun ürkütücülüğü
  طلعت الجبل أي علوته؛ المطلع المأتى؛ موضع الإطلاع من إشراف إلى انحدار (sihah)؛ طلعت الجبل إذا علوته؛ المطلع موضع الاطلاع من إشراف إلى الانحدار؛ وقد يكون المطلع المصعد؛ مطلع هذا الجبل مصعده ومأتاه؛ ما لهذا الأمر مطلع أي وجه ولا مأتى (tahdhib)؛ والمطلع المأتى؛ أين مطلع هذا الأمر أي مأتاه؛ هول المطلع (maqayis)
- **B007** bir alanı sınırına kadar doldurma; ayrı aktarımda güneşin gördüğü yeryüzü [kalıp] — yeryüzünü dolduracak çokluk; başka bir aktarımda güneşin gördüğü yeryüzü · avucu dolduran şey; özellikle gövdesi avucu dolduran yay · ağzına kadar dolu kap veya su gözü · ölçü kabını taşacak kadar doldurmak
  الطلاع ما طلعت عليه الشمس؛ وطلاع الأرض ملء الأرض؛ وقوس طلاع إذا كان عجسها يملأ الكف (ayn)؛ طلاع الشيء ملؤه؛ طلاع الأرض ملؤها؛ قوس طلاع الكف (sihah)؛ طلاع الأرض ملؤها حتى يطالع أعلى الأرض؛ طلاع الأرض ما طلعت عليه الشمس؛ قدح طلاع ممتلىء؛ عين طلاعة ممتلئة (tahdhib)؛ الطلاع ما طلعت عليه الشمس والإنسان؛ وقوس طلاع الكف ملء الكف (mufradat)؛ الطلاع ما طلعت عليه الشمس من الأرض؛ قوس طلاع الكف إذا كان عجسها يملأ الكف (maqayis)
- **B008** bir şeye istekle yönelme; bir görünüp bakıp bir gizlenme [kalıp] — bir şeye sürekli ve güçlü biçimde yönelen iç istek · bir görünüp bakıp bir geri çekilerek gizlenen kadın
  إن نفسك لطلعة إلى هذا الأمر؛ أي تتطلع إليه؛ وامرأة طلعة قبعة تنظر ساعة وتتنحى أخرى (ayn)؛ وتطلعت إلى ورود كتابك؛ ونفس طلعة؛ وامرأة طلعة (sihah)؛ نفسك لطلعة إلى هذا الأمر؛ وإنها لتطلع إليه أي لتنازع إليه؛ وامرأة طلعة قبعة تنظر ساعة ثم تختبىء ساعة (tahdhib)؛ امرأة طلعة قبعة تظهر رأسها مرة وتستر أخرى (mufradat)؛ ونفس طلعة تتطلع للشيء؛ وامرأة طلعة إذا كانت تكثر الإطلاع (maqayis)
- **B009** bir insanın görülüşü ve göz önündeki görünüşü — bir insanın yüzü, genel görünüşü veya görülüşü
  والطلعة الرؤية؛ ما أحسن طلعته أي رؤيته؛ حيا الله طلعتك (ayn)؛ والطلعة الرؤية (sihah)؛ طلعته رؤيته؛ يقال حيا الله طلعتك (tahdhib)؛ وطلعة الإنسان رؤيته لأنها تطلع (maqayis)
- **B010** okun nişan alınan yerin üstünden geçip arkasına düşmesi [kalıp] — yükselip nişan alınan yerin üstünden geçerek arkasına düşen ok · attığı ok nişan alınan yerin üstünden geçmek
  وأطلع الرامي أي جاز سهمه من فوق الغرض (sihah)؛ والطالع من السهام الذي يقع وراء الهدف؛ يسجد للطالع؛ شخص سهمه فارتفع عن الرمية (tahdhib)؛ ورمى فلان فأطلع وأشخص إذا مر سهمه برأس الغرض (maqayis)
- **B011** kusmak ve kusmuk — kusmak · kusmuk
  وأطلع أي قاء؛ والطلعاء القيء (sihah)؛ أطلع الرجل إطلاعا إذا قاء؛ الطولع الطلعاء وهو القيء (tahdhib)؛ ومن الباب الطلعاء القيء؛ يقال أطلع إذا قاء (maqayis)
- **B012** çevresindeki palmiye ağaçlarını boyca aşma; uzun boylu erkek — yanındaki palmiye ağaçlarından daha uzun olan palmiye · uzun boylu adam
  نخلة مطلعة إذا طالت النخيل (sihah)؛ نخلة مطلعة إذا طالت النخلة التي بحذائها فكانت أطول منها (tahdhib)؛ الهطلع الرجل الطويل زيدت فيه الهاء من طلع (maqayis)

## ف ء د (root_001122) — identity root of ٱلْأَفْـِٔدَةِ (w4)

- **B001** yüksek ateş ısısı; ateşte pişirme, ateş yakma ve bunların ürün, araç ve yerleri — eti ateşte kızartmak veya pişirmek · ateşte kızartılmış ya da pişirilmiş · kızartma veya közde pişirme aracı; şiş ya da fırını karıştırma çubuğu · kızartma ya da ateş yakma yeri · ekmeği sıcak kül ve köz içinde pişirmek · ekmek için kül ve ateş içinde pişirme yuvası açmak · ekmeğin yerleştirildiği sıcak kül ve ateş yuvası · fırını karıştırma veya kızartma araçları · kızartma şişi · onu ateşte kızarttı · kızartma şişi veya ateşte pişirme aracı · ateş · topluluk ateş yaktı
  أصل صحيح يدل على حمى وشدة حرارة (maqayis)؛ فأدت اللحم شويته ولحم فئيد أي مشوي (maqayis;sihah;mufradat)؛ فأدت الخبزة مللتها أو خبزتها في الملة (maqayis;sihah;tahdhib)؛ افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها (tahdhib)؛ المفأد السفود أو ما يخبز ويشوى به والمفتأد موضع الوقود (maqayis;sihah;tahdhib)
- **B002** iç ısısı gözetilen yürek — yürek; iç ısısı veya yanışı gözetilerek adlandırılan organ · yürekler
  الفؤاد القلب والجمع الأفئدة (sihah)؛ الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد (mufradat)؛ الفؤاد سمي بذلك لحرارته أو لتفؤده (maqayis;tahdhib)
- **B003** yüreği vurup yaralama veya yürekte hastalık oluşması — yüreğe vurup yaralama eylemi · yüreğine vurmak veya yüreğinde hastalık oluşturmak · yüreğinden vurulmuş veya yüreği hastalanmış kimse · adamın yüreği hastalandı
  الفأد مصدر فأدته إذا أصبت فؤاده (maqayis)؛ فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده (sihah)؛ فأدت الصيد إذا أصبت فؤاده وفئد الرجل أصابه داء في فؤاده (tahdhib)
- **B004** yüreksiz ve korkak kişi — yüreği zayıf, yüreksiz ve korkak kimse · yüreksiz veya yüreği zayıf kimse
  رجل مفؤود وفئيد لا فؤاد له (sihah)؛ المفؤود الضعيف الفؤاد الجبان مثل المنخوب (tahdhib)

===== _commentary/v16/out/s104/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 104:7, and ## Buluşmalar) =====
## Toplanan su, çiçeklenen ekin, kuru saplar

Surenin kelimeleri neredeyse eksiksiz bir doğa sürecini de taşır. Toplama fiilinin kökünde her yerden akıp birikmiş sel vardır {ar:استجمع السيل اجتمع من كل موضع, tr:istecme'a's-seyl ictema'a min külli mevdı', gloss:sel her yerden toplandı, source:"ج م ع,B010"}. Sayma fiilinin kökünde ise suyun toplandığı yer ve kesilmeyen kaynak {ar:العد مجتمع الماء, tr:el-idd mücteme'u'l-mâ', gloss:"idd" suyun toplandığı yerdir, source:"ع د د,B004"}, {ar:الماء العد الدائم الذي لا انقطاع له, tr:el-mâü'l-idd ed-dâim ellezî lâ inkıtâ'a leh, gloss:"idd" su, kesintisi olmayan sürekli sudur, source:"ع د د,B004"}. Bu tanımlarda "toplanmak", "sürekli" ve "kesilmeyen besleme" birlikte geçer; adamın mala yüklediği süreklilik, suyun dilinde zaten vardır. Son ayetin iki kelimesi de bu sahneye girer: bir nehrin başka bir nehirle beslenip kabarması {ar:مد النهر ومده نهر آخر, tr:medde'n-nehrü ve meddehû nehrün âhar, gloss:nehir kabardı, başka bir nehir onu besledi, source:"م د د,B003"}, selin önünü taş ve toprakla kesip suyu bir yerde toplamak {ar:عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة, tr:ammedtü's-seyle ta'mîden izâ sedette vechü cerayetihî hattâ yectemi'a fî mevdı', gloss:selin akışını toprak ya da taşla kesip bir yerde toplanmasını sağladım, source:"ع م د,B013"}, ve yağmurla ıslanıp avuçta topaklanan toprak {ar:عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك, tr:amidet'il-ardu izâ rasaha fîhe'l-matar, gloss:yağmur toprağa işleyip avucunda topaklandı, source:"ع م د,B010"}. Bent bir direk gibi suyu tutar ve toplar.

Su ekini getirir. Yedinci ayetin fiilinin kökü ekinin baş göstermesini ve hurmanın tomurcuk vermesini anlatır {ar:طلع الزرع إذا بدا; وأطلعت النخلة إذا أخرجت طلعها, tr:tala'a'z-zer'u izâ bedâ ve atla'ati'n-nahletü, gloss:ekin baş gösterdi, hurma tomurcuğunu çıkardı, source:"ط ل ع,B005"}. Ateşin kökü ağacın çiçek açması için de kullanılır {ar:تنوير الشجرة: إزهارها, tr:tenvîru'ş-şecera izhâruhâ, gloss:ağacın "tenvir"i çiçek açmasıdır, source:"ن و ر,B004"}. Sonra sıcak gelir: tutuşma kökü yazın en sıcak günlerini adlandırır {ar:وقدة الصيف أشده حرا, tr:vakdetü's-sayf eşeddühû harran, gloss:yazın "vakde"si en sıcak zamanıdır, source:"و ق د,B004"}. Kırıcının kökü kıtlık yılını {ar:الحطمة السنة الشديدة لأنها تحطم كل شيء, tr:el-hutame es-senetü'ş-şedîde, gloss:hutame her şeyi kırdığı için şiddetli kıtlık yılıdır, source:"ح ط م,B003"}, sanma fiilinin kökü de gökten inip bahçeyi yakan ateşi, doluyu ya da çekirgeyi bilir {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ' ey nâran tuhrikuhâ, gloss:gökten bir "husban", yani onu yakan bir ateş, source:"ح س ب,B007"}. Geriye kalan kırılmış kuru saplardır {ar:الحطام ما تكسر من اليبس, tr:el-hutâm mâ tekessera mine'l-yebs, gloss:hutam kurumuş şeyden kırılandır, source:"ح ط م,B001"}; aynı kelime dünyanın süsü ve malı için de söylenir {ar:حطام الدنيا عرضها وأثرها وزينتها, tr:hutâmü'd-dünyâ arazuhâ ve eseruhâ ve zînetühâ, gloss:dünya kırıntısı onun geçici malı ve süsüdür, source:"ح ط م,B009"}.

Sure kendi anlamında yalnızca toplama, sayma, sanma, atılma ve ateşi söyler. Bu süreç, kelimelerin ailesinde duyulur ve yığılan malı bir mevsim gibi gösterir: kesilmeyecek sanılan bir kaynak, kabaran bir nehir, çiçek, sonra sıcak, kıtlık, gökten ateş ve kuru sap. Kuran bu süreci malın çoğaltılmasının benzetmesi olarak açıkça kurar. Hadid suresinde Allah {ar:وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ve tekâsürun fi'l-emvâli ve'l-evlâd, ke-meseli ğaysin a'cebe'l-küffâra nebâtühû sümme yehîcü fe-terâhü musfarran sümme yekûnü hutâmâ, gloss:mallarda ve evlatlarda çoğalma yarışı; bitkisi ekincileri hayran bırakan bir yağmur gibi, sonra kurur, sararmış görürsün, sonra kırık saplara döner, source:57:20} der. "Hutam", surenin ateşinin adıyla aynı köktendir. Zümer suresinde Allah gökten indirdiği suyu {ar:فَسَلَكَهُۥ يَنَٰبِيعَ فِى ٱلْأَرْضِ, tr:fe-selekehû yenâbî'a fi'l-ard, gloss:onu yerde kaynaklara yürüttü, source:39:21} der, ekin çıkarır, sararır ve {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا, tr:sümme yec'alühû hutâmâ, gloss:sonra onu kırıntıya çevirir, source:39:21}. Vakıa suresinde Allah ekenlere sorar ve {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا فَظَلْتُمْ تَفَكَّهُونَ, tr:lev neşâü le-ce'alnâhü hutâmen fe-zaltüm tefekkehûn, gloss:dileseydik onu kırıntı yapardık da şaşakalırdınız, source:56:65} der. Kehf suresinde dünya hayatı suyla karışan bitkiye benzetilir ve {ar:فَأَصْبَحَ هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:fe-asbaha heşîmen tezrûhü'r-riyâh, gloss:rüzgârların savurduğu çer çöpe döndü, source:18:45}. Aynı surede iki bahçe sahibinin hikâyesi bu sürecin bütününü bir mal sahibinin başından geçirir: bahçenin arasından bir nehir akıtılmıştır, sahibi onun yok olmayacağını sanır ve arkadaşı ona Rabbinin {ar:وَيُرْسِلَ عَلَيْهَا حُسْبَانًۭا مِّنَ ٱلسَّمَآءِ فَتُصْبِحَ صَعِيدًۭا زَلَقًا, tr:ve yursile aleyhâ husbânen mine's-semâi fe-tusbiha sa'îden zelekâ, gloss:üzerine gökten bir "husban" gönderip onu kaygan bir toprağa çevirebileceğini, source:18:40} söyler. Bu "husban", surenin sanma fiiliyle aynı köktendir. Sonunda ürün kuşatılır ve adam {ar:فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:fe-asbaha yukallibü keffeyhi alâ mâ enfeka fîhâ, gloss:harcadıklarına yanıp avuçlarını ovuşturur hale geldi, source:18:42}. Avuç orada boş kalır. Taha suresinde de dünyanın süsü bir çiçektir: Allah Peygambere {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temüddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhüm zehrete'l-hayâti'd-dünyâ, gloss:onlardan bazı kesimlere dünya hayatının çiçeği olarak verdiğimiz şeylere gözlerini dikme, source:20:131} der. Kehf suresi de aynı dersi çıkarır: {ar:ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:el-mâlü ve'l-benûne zînetü'l-hayâti'd-dünyâ, gloss:mal ve oğullar dünya hayatının süsüdür, source:18:46}.

Kaynaklar: 104:2 جَمَعَ ج م ع B010; 104:2 وَعَدَّدَهُۥ ع د د B004; 104:9 مُّمَدَّدَةٍۭ م د د B003; 104:9 عَمَدٍ ع م د B013; 104:9 عَمَدٍ ع م د B010; 104:7 تَطَّلِعُ ط ل ع B005; 104:6 نَارُ ن و ر B004; 104:6 ٱلْمُوقَدَةُ و ق د B004; 104:4 ٱلْحُطَمَةِ ح ط م B003; 104:3 يَحْسَبُ ح س ب B007; 104:4 ٱلْحُطَمَةِ ح ط م B001; 104:4 ٱلْحُطَمَةِ ح ط م B009

## Ocak ve yutan ateş

Dördüncü ve yedinci ayet arasındaki ateş bir ocak gibi kurulur. {ar:ٱلْمُوقَدَةُ, tr:el-mûkade, gloss:tutuşturulmuş, source:104:6} kökü ateşin tutuşmasını {ar:كلمة تدل على اشتعال نار, tr:kelimetün tedüllü alâ iştiâli nâr, gloss:ateşin alevlenmesini gösteren bir kelime, source:"و ق د,B001"}, yakıtı {ar:الوقود الحطب, tr:el-vekûd el-hatab, gloss:vekûd odundur, source:"و ق د,B002"} ve ocağın yerini {ar:الموقد والمستوقد موضع النار, tr:el-mevkıd ve'l-müstevkad mevdı'u'n-nâr, gloss:ateşin yeri, source:"و ق د,B003"} adlandırır. "Mûkade" edilgendir: biri onu yakmıştır, ateş kendiliğinden değil tutuşturulmuş olarak durur. Dördüncü ayetin atılışı bu sahnede ocağa yakıt atmaya benzer; Arapçada atma fiili hurmayı ya da kuru üzümü bir kaba atıp üstüne su dökmek için de kullanılır {ar:يأخذ تمرا أو زبيبا فينبذه أي يلقيه في وعاء أو سقاء ويصب عليه الماء, tr:ye'huzü temran ev zebîben fe-yenbizühû, gloss:hurma ya da üzüm alıp bir kaba atar ve üstüne su döker, source:"ن ب ذ,B006"}. Büyük kazana da toplama kökünden ad verilir {ar:قدر جامعة وهي العظيمة, tr:kidrun câmi'atün ve hiye'l-azîme, gloss:büyük kazana "câmia" denir, source:"ج م ع,B012"}. Kalıcılık kökü ise ocak taşlarını, uzun süre yerinde kaldıkları için, "kalıcılar" diye anar {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid li'l-esâfî ve'l-hicâra li-tûli mekshihâ, gloss:ocak taşlarına uzun süre kaldıkları için "havâlid" denir, source:"خ ل د,B001"}. Kendisini kalıcı sanan adamın kelimesinde kalıcı olanlar ateşin altındaki taşlardır.

Yedinci ayetin {ar:ٱلْأَفْـِٔدَةِ, tr:el-ef'ide, gloss:yürekler, source:104:7} kelimesinin kökü sıcaklık ve kızgınlık bildirir {ar:أصل صحيح يدل على حمى وشدة حرارة, tr:aslün sahîhun yedüllü alâ hummâ ve şiddeti harâra, gloss:ateşli sıcaklık ve şiddetli harareti gösterir, source:"ف ء د,B001"}; eti kızartmak ve ekmeği sıcak külde pişirmek bu köktendir {ar:فأدت اللحم شويته ولحم فئيد أي مشوي, tr:fe'edtü'l-lahme şeveytüh, gloss:eti kızarttım; "feîd" kızarmış ettir, source:"ف ء د,B001"}, {ar:فأدت الخبزة مللتها أو خبزتها في الملة, tr:fe'edtü'l-hubzete melletühâ, gloss:ekmeği sıcak külde pişirdim, source:"ف ء د,B001"}. Arapça bu kökü doğrudan altıncı ayetin fiiliyle açıklar {ar:افتأد القوم إذا أوقدوا نارا والفئيد النار نفسها, tr:ifte'ede'l-kavmü izâ evkadû nâran, gloss:topluluk ateş yaktığında "ifte'ede" denir; feîd ateşin kendisidir, source:"ف ء د,B001"}.

Ateşin adı onu bir yiyici yapar. {ar:ٱلْحُطَمَةِ, tr:el-hutame, gloss:ezip kıran, source:104:4} ateşe karşılaştığı her şeyi kırdığı için verilmiştir {ar:سميت النار الحُطَمَة لحطمها ما تلقى, tr:summiyeti'n-nâru'l-hutame li-hatmihâ mâ telkâ, gloss:ateşe, karşılaştığını kırdığı için hutame denmiştir, source:"ح ط م,B002"}. Aynı ad çok yiyen kişiye de verilir ve Arapça bu adı açıkça cehenneme benzetmeye bağlar {ar:قيل للأكول حُطَمَة تشبيها بالجحيم, tr:kîle li'l-ekûli hutame teşbîhen bi'l-cahîm, gloss:obur kişiye cehenneme benzetilerek hutame denmiştir, source:"ح ط م,B008"}; öğütüp sindiren organlara da bu kökten ad verilir {ar:يقال للجوارس حاطوم وهاضوم, tr:yükâlü li'l-cevâris hâtûm ve hâdûm, gloss:öğüten organlara hâtûm ve hâdûm denir, source:"ح ط م,B008"}. Ateş, aldığını parçalayan bir midedir. Yedinci ayetin fiilinin bir dalı ise yemenin tersini, kusmayı adlandırır {ar:أطلع الرجل إطلاعا إذا قاء, tr:atla'a'r-racülü izâ kâe, gloss:adam kustu, source:"ط ل ع,B011"}. Bu dal ayetin anlamına girmez; aile imgesi olarak, yutulanın yukarı doğru çıkışını, ateşin içten yukarı yükselişinin yanında duyurur.

Kuran mal sahiplerini yakıt olarak anar. Al-i İmran suresinde Allah {ar:إِنَّ ٱلَّذِينَ كَفَرُوا۟ لَن تُغْنِىَ عَنْهُمْ أَمْوَٰلُهُمْ وَلَآ أَوْلَٰدُهُم مِّنَ ٱللَّهِ شَيْـًۭٔا ۖ وَأُو۟لَٰٓئِكَ هُمْ وَقُودُ ٱلنَّارِ, tr:inne'llezîne keferû len tuğniye anhüm emvâlühüm ve lâ evlâdühüm minallâhi şey'â, ve ülâike hüm vekûdü'n-nâr, gloss:inkâr edenlere malları da evlatları da Allah'a karşı bir yarar sağlamaz; ateşin yakıtı onlardır, source:3:10} der. Bakara suresinde Kuran'dan şüphe edenlere ve Tahrim suresinde müminlere aynı ateş anılır: {ar:وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:vekûdühe'n-nâsü ve'l-hicâra, gloss:yakıtı insanlar ve taşlardır, source:66:6}. Enbiya suresinde Allah putperestlere {ar:إِنَّكُمْ وَمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ حَصَبُ جَهَنَّمَ, tr:inneküm ve mâ ta'büdûne min dûnillâhi hasabü cehennem, gloss:siz ve Allah'tan başka taptıklarınız cehennemin çırasısınız, source:21:98} der. Mümin suresinde zincirlerle sürüklenenler {ar:فِى ٱلْحَمِيمِ ثُمَّ فِى ٱلنَّارِ يُسْجَرُونَ, tr:fi'l-hamîmi sümme fi'n-nâri yuscerûn, gloss:kaynar suda, sonra ateşte yakılırlar, source:40:72}. Buruc suresinde ateşin kendisi yakıtla tanımlanır: {ar:ٱلنَّارِ ذَاتِ ٱلْوَقُودِ, tr:en-nâri zâti'l-vekûd, gloss:yakıtı bol ateş, source:85:5}. Nisa suresinde pişme açıkça söylenir: {ar:كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:küllemâ nadıcet cülûdühüm beddelnâhüm cülûden ğayrahâ, gloss:derileri pişip bittikçe onları başka derilerle değiştiririz, source:4:56}. Aynı surede yenen mal ateşe dönüşür: {ar:إِنَّ ٱلَّذِينَ يَأْكُلُونَ أَمْوَٰلَ ٱلْيَتَٰمَىٰ ظُلْمًا إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:inne'llezîne ye'külûne emvâle'l-yetâmâ zulmen innemâ ye'külûne fî butûnihim nârâ, gloss:yetimlerin mallarını haksızca yiyenler karınlarına ancak ateş yerler, source:4:10}. Kaf suresinde Allah cehenneme sorar ve o doymaz: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlü li-cehenneme heli'mtele'ti ve tekûlü hel min mezîd, gloss:o gün cehenneme "doldun mu" deriz, o da "daha var mı" der, source:50:30}. Ra'd suresinde ise insanlar süs ya da eşya elde etmek için madenin üstüne ateş yakar: {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ ٱبْتِغَآءَ حِلْيَةٍ أَوْ مَتَٰعٍۢ زَبَدٌۭ مِّثْلُهُۥ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâri'btiğâe hilyetin ev metâ'in zebedün mislüh, gloss:süs ya da eşya elde etmek için ateşte üzerine yaktıkları şeyden de onun gibi bir köpük çıkar, source:13:17}; köpük gider, insanlara yarayan yerde kalır. Mal için yakılan ateşte bile kalıcı olan, yarar olandır.

Kaynaklar: 104:6 ٱلْمُوقَدَةُ و ق د B001; 104:6 ٱلْمُوقَدَةُ و ق د B002; 104:6 ٱلْمُوقَدَةُ و ق د B003; 104:3 أَخْلَدَهُۥ خ ل د B001; 104:2 جَمَعَ ج م ع B012; 104:4 لَيُنۢبَذَنَّ ن ب ذ B006; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B001; 104:4 ٱلْحُطَمَةِ ح ط م B002; 104:4 ٱلْحُطَمَةِ ح ط م B008; 104:7 تَطَّلِعُ ط ل ع B011

## Tutuşan yürek

{ar:ٱلْأَفْـِٔدَةِ, tr:el-ef'ide, gloss:yürekler, source:104:7} kelimesi kalbin bir adıdır, ama sıcaklık yönüyle anılan adıdır: kalbe, tutuşma anlamı göz önünde tutulduğunda "fuâd" denir {ar:الفؤاد كالقلب لكن يقال له فؤاد إذا اعتبر فيه معنى التفؤد أي التوقد, tr:el-fuâdü ke'l-kalb lâkin yükâlü lehû fuâdun izâ'tübira fîhi ma'ne't-tefe'üd ey et-tevakkud, gloss:fuad kalp gibidir, ama içinde tutuşma anlamı gözetildiğinde fuad denir, source:"ف ء د,B002"}. Tanımdaki "tevakkud", altıncı ayetin {ar:ٱلْمُوقَدَةُ, tr:el-mûkade, gloss:tutuşturulmuş, source:104:6} kelimesinin köküdür {ar:وقدت النار واتقدت وتوقدت وأوقدتها, tr:vekadeti'n-nâru vetteka det ve tevakkadet ve evkadtühâ, gloss:ateş tutuştu, alevlendi, ben onu yaktım, source:"و ق د,B001"}. Tutuşturulmuş ateş, tutuşmayla adlanan organa çıkar. Ayetin sırası bunu yapar: önce ateşin sıfatı, hemen ardından onun ulaştığı yer.

Kalp aynı zamanda üçüncü ayetteki sanının oturduğu yerdir. {ar:أَخْلَدَهُۥ, tr:ahledeh, gloss:onu kalıcı kıldı, source:104:3} kelimesinin kökünden "hald", kalpte yerleşik olduğu için akıl ve gönül demektir {ar:الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت, tr:el-haled el-bâl ve summiye bi-zâlike li-ennehû müstekırrun fi'l-kalbi sâbit, gloss:"haled" gönüldür; kalpte sabit durduğu için böyle denmiştir, source:"خ ل د,B004"}, {ar:وقع ذلك في خلدي أي في قلبي, tr:veka'a zâlike fî haledî ey fî kalbî, gloss:bu benim içime, yani kalbime düştü, source:"خ ل د,B004"}. Sanı kalpte doğdu; ateş kalbe çıkar. Kalbin kökü bir de avı kalbinden vurmayı ve kalp hastalığını {ar:فأدته فهو مفؤود أصبت فؤاده وكذلك إذا أصابه داء فؤاده, tr:fe'edtühû fe-hüve mef'ûd, gloss:onu kalbinden vurdum; kalp hastalığına tutulan da "mef'ûd"dur, source:"ف ء د,B003"}, korkudan zayıflamış yüreği {ar:المفؤود الضعيف الفؤاد الجبان مثل المنخوب, tr:el-mef'ûd ed-da'îfü'l-fuâd el-cebân, gloss:yüreği zayıf, korkak kişi, source:"ف ء د,B004"} adlandırır. Son ayetin kökü de kalbi hüzün ve hastalıkla çökertilmiş olarak anar {ar:القلب الذي يعمده الحزن والسقيم الذي يعمده السقم, tr:el-kalbü'llezî ya'midühü'l-huzn, gloss:hüznün çökerttiği kalp ve hastalığın çökerttiği hasta, source:"ع م د,B008"}. Yürek tutuşan, vurulan, zayıflayan ve çöken bir organ olarak dört kelimenin ailesinde görünür. Surenin ilk kelimesinin kökünde göğüs, kalbin barındığı yer olarak geçer {ar:الكلكل الصدر, tr:el-kelkel es-sadr, gloss:kelkel göğüstür, source:"ك ل ل,B007"}; ilk ayetin kökündeki şeytan dürtüsü de kalbe çöker.

Dışarıda toplanan mala, en içteki organa ulaşan ateş karşılık verir. Kuran malı ve kalbi aynı ölçüye koyar. Şuara suresinde İbrahim duasında hesap gününü anar: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfe'u mâlün ve lâ benûn, gloss:malın da oğulların da yarar vermediği gün, source:26:88}, {ar:إِلَّا مَنْ أَتَى ٱللَّهَ بِقَلْبٍۢ سَلِيمٍۢ, tr:illâ men etallâhe bi-kalbin selîm, gloss:ancak Allah'a temiz bir kalple gelen müstesna, source:26:89}. Değer, toplanan şeyde değil kalptedir. İsra suresinde Allah {ar:إِنَّ ٱلسَّمْعَ وَٱلْبَصَرَ وَٱلْفُؤَادَ كُلُّ أُو۟لَٰٓئِكَ كَانَ عَنْهُ مَسْـُٔولًۭا, tr:inne's-sem'a ve'l-basara ve'l-fuâde küllü ülâike kâne anhü mes'ûlâ, gloss:kulak, göz ve yürek, bunların her biri ondan sorumludur, source:17:36} der; bilmediği şeyin ardına düşmeyi yasaklayan ayettir ve "fuad" sorguya açıktır. Mutaffifin suresinde Allah kazancın kalplerin üstünü kapladığını söyler: {ar:كَلَّا ۖ بَلْ ۜ رَانَ عَلَىٰ قُلُوبِهِم مَّا كَانُوا۟ يَكْسِبُونَ, tr:kellâ bel râne alâ kulûbihim mâ kânû yeksibûn, gloss:hayır, kazandıkları kalplerinin üstünü pas gibi kaplamıştır, source:83:14}. Adiyat suresinde insan {ar:وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ, tr:ve innehû li-hubbi'l-hayri le-şedîd, gloss:o mal sevgisinde çok şiddetlidir, source:100:8} diye anlatılır ve kabirler deşildiğinde {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fi's-sudûr, gloss:göğüslerdekiler ortaya dökülür, source:100:10}. Hac suresinde içi eriten sıcaklık söylenir: {ar:يُصْهَرُ بِهِۦ مَا فِى بُطُونِهِمْ وَٱلْجُلُودُ, tr:yusharu bihî mâ fî butûnihim ve'l-cülûd, gloss:onunla karınlarındakiler ve derileri eritilir, source:22:20}. İbrahim suresinde o günün yürekleri boştur: {ar:وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ, tr:ve ef'idetühüm hevâ', gloss:yürekleri bomboştur, source:14:43}.

Kaynaklar: 104:7 ٱلْأَفْـِٔدَةِ ف ء د B002; 104:6 ٱلْمُوقَدَةُ و ق د B001; 104:3 أَخْلَدَهُۥ خ ل د B004; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B004; 104:9 عَمَدٍ ع م د B008; 104:1 هُمَزَةٍ ه م ز B005; 104:1 لِّكُلِّ ك ل ل B007

## Aşağı atılan, yukarı çıkan ve hedefini bulan ateş

Surenin dikey bir sahnesi vardır ve bir avcının nişanı ile aynı hareketi paylaşır. Adam aşağı atılır; atma kökünün özü fırlatıp bırakmaktır {ar:أصل صحيح يدل على طرح وإلقاء, tr:aslün sahîhun yedüllü alâ tarhin ve ilkâ', gloss:atıp bırakmayı gösterir, source:"ن ب ذ,B001"}. Ateş ise yukarı çıkar. {ar:تَطَّلِعُ, tr:tattali'u, gloss:çıkıp vurur, üstüne tırmanır, source:104:7} fiilinin kökü güneşin ve yıldızın doğuşudur {ar:طلعت الشمس والكوكب طلوعا ومطلعا, tr:tala'ati'ş-şemsü ve'l-kevkeb, gloss:güneş ve yıldız doğdu, source:"ط ل ع,B001"}; görünmek ve belirmek {ar:أصل واحد صحيح يدل على ظهور وبروز, tr:aslün vâhidün sahîhun yedüllü alâ zuhûrin ve burûz, gloss:görünüp ortaya çıkmayı gösterir, source:"ط ل ع,B001"}. Bir dağın tepesine tırmanmak ve tepeden aşağıya bakılan yerin dehşeti de bu köktendir {ar:طلعت الجبل أي علوته, tr:tala'tü'l-cebele ey alevtüh, gloss:dağa çıktım, yani üstüne yükseldim, source:"ط ل ع,B006"}, {ar:هول المطلع, tr:hevlü'l-muttala', gloss:tepeden bakılan yerin dehşeti, source:"ط ل ع,B006"}. Bir kabı ağzına kadar doldurmak da {ar:قدح طلاع ممتلىء, tr:kadahun tılâ'un mümteli', gloss:ağzına kadar dolu kap, source:"ط ل ع,B007"}. Ayetteki yapı da önemlidir: fiil "alâ" edatıyla gelir ve Arapçada aynı yapı bir topluluğun üstüne baskın yapmak için kullanılır {ar:طلع علينا فلان يطلع طلوعا إذا هجم, tr:tala'a aleynâ fülânün izâ hecem, gloss:falan üstümüze çıkageldi, yani baskın yaptı, source:"ط ل ع,B002"}. Ateş doğan bir güneş gibi belirir, bir tırmanıcı gibi yükselir, bir baskıncı gibi üstlerine gelir ve kabı doldurur gibi yükselir. Ateşin kökünde de kararsızca kıpırdayan ışık vardır {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslün sahîhun yedüllü alâ idâetin ve ıdtırâbin ve kılleti sebât, gloss:aydınlanma, çalkalanma ve sabit durmamayı gösterir, source:"ن و ر,B001"}.

Bu yükseliş bir hedefe yöneliktir. Beşinci ayetin {ar:أَدْرَىٰكَ, tr:edrâke, gloss:sana bildirdi, source:104:5} fiilinin kökü avcının ustalığını da taşır: avın yerini daha görmeden kollamak ve onu bir siper hayvanının ardından gizlice yaklaşarak aldatmak {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytü's-sayde izâ nazartü eyne hüve ve lem erahü ba'd, gloss:avı henüz görmeden nerede olduğunu kolladım ve ona sinsice yaklaştım, source:"د ر ي,B003"}, {ar:الدرية الدابة التي يستتر بها الذي يرمي الصيد, tr:ed-dariyye ed-dâbbetü'lletî yesteteru bihe'llezî yermi's-sayd, gloss:avcının ardına saklandığı hayvan, source:"د ر ي,B003"}, nişan alıştırması yapılan halka {ar:الدريئة الحلقة التي يتعلم عليها الطعن, tr:ed-darî'e el-halkatü'lletî yute'allemu aleyhe't-ta'n, gloss:mızrak atmanın öğrenildiği halka, source:"د ر ي,B005"} ve bir yeri seçip baskın için ona yönelmek {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fülânin mekâne kezâ ey i'temedûhü bi-ğazvin ev ğâra, gloss:falan oğulları bir yeri seçip baskınla ona yöneldiler, source:"د ر ي,B002"}. Bu açıklamadaki "i'temedûhü", son ayetteki direklerin köküdür; o kökte kasten yönelmek de vardır {ar:العمد والتعمد خلاف السهو, tr:el-amd ve't-ta'ammüd hilâfü's-sehv, gloss:kasıt, yanılmanın zıddıdır, source:"ع م د,B001"}. İlk ayetin kökü güçlü atan yayı adlandırır {ar:قوس همزي شديدة الدفع للسهم, tr:kavsün hemezâ şedîdetü'd-def'i li's-sehm, gloss:oku güçlü iten yay, source:"ه م ز,B003"}; yedinci ayetin kökü düşmanı gözetlemek için önden gönderilen öncüleri {ar:الطليعة قوم يبعثون ليطلعوا طلع العدو, tr:et-talî'a kavmün yüb'asûne li-yattali'û tal'a'l-adüvv, gloss:düşmanın durumunu gözetlemek için gönderilen topluluk, source:"ط ل ع,B004"}; yüreklerin kökü avı kalbinden vurmayı {ar:فأدت الصيد إذا أصبت فؤاده, tr:fe'edtü's-sayde izâ esabtü fuâdeh, gloss:avı kalbinden vurdum, source:"ف ء د,B003"}. Aynı kökün bir dalı tersini de söyler: atıcının oku hedefin üstünden aşıp gider {ar:وأطلع الرامي أي جاز سهمه من فوق الغرض, tr:ve atla'a'r-râmî ey câze sehmühû min fevki'l-ğaraz, gloss:atıcı "atla'a" etti, yani oku hedefin üstünden geçti, source:"ط ل ع,B010"}. Surenin yükselişi aşmaz: {ar:عَلَى ٱلْأَفْـِٔدَةِ, tr:ale'l-ef'ide, gloss:yüreklerin üzerine, source:104:7} durur. Bunlar fiilin ayetteki anlamının yanında duyulan aile imgeleridir; ayetin kendisi ateşin yüreklere ulaştığını söyler.

Yükseliş, sekizinci ayette yukarıdan kapanan örtüyle biter: {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mü'sade, gloss:o, üzerlerine kapatılmıştır, source:104:8}; "aleyhim" yedinci ayetteki "alâ"yı tekrar eder. Kökün anlamı kapıyı kapatıp sıkıca örtmektir {ar:أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة, tr:evsadtü'l-bâbe ve âsadtühû ey atbaktühû ve ahkemtüh, gloss:kapıyı kapadım, sıkıca örttüm; mü'sade üstü kapatılmış demektir, source:"و ص د,B001"}.

Kuran ateşe atılmayı ve ateşin onlara yönelişini başka yerlerde canlandırır. Furkan suresinde Allah {ar:إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا, tr:izâ raethüm min mekânin ba'îdin semi'û lehâ teğayyuzan ve zefîrâ, gloss:onları uzaktan görünce, onun öfkeyle köpürüşünü ve uğultusunu duyarlar, source:25:12} der; ateş görür ve hedefine yönelir, ardından {ar:وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا, tr:ve izâ ülkû minhâ mekânen dayyikan mukarranîne de'av hünâlike sübûrâ, gloss:bağlanmış olarak onun dar bir yerine atıldıklarında orada yok olmayı dilerler, source:25:13}. Mülk suresinde {ar:إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:izâ ülkû fîhâ semi'û lehâ şehîkan ve hiye tefûr, gloss:oraya atıldıklarında onun hırıltısını duyarlar, o kaynar, source:67:7}, {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdü temeyyezü mine'l-ğayz, gloss:öfkeden neredeyse çatlayacaktır, source:67:8}. Yukarı yol kapalıdır: Hac suresinde {ar:كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا, tr:küllemâ erâdû en yahrucû minhâ min ğammin u'îdû fîhâ, gloss:kederden oradan çıkmak istedikçe oraya geri döndürülürler, source:22:22}, Secde suresinde de aynı söz {source:32:20}. Atılmanın kendisi Kasas suresinde Firavun ve ordusu için anlatılır: {ar:فَأَخَذْنَٰهُ وَجُنُودَهُۥ فَنَبَذْنَٰهُمْ فِى ٱلْيَمِّ, tr:fe-ehaznâhü ve cünûdehû fe-nebeznâhüm fi'l-yemm, gloss:onu ve ordularını yakalayıp denize attık, source:28:40}. Aynı surede Firavun yükselmeyi ve tutuşturmayı tek cümlede ister: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا لَّعَلِّىٓ أَطَّلِعُ إِلَىٰٓ إِلَٰهِ مُوسَىٰ, tr:fe-evkıd lî yâ Hâmânü ale't-tîni fec'al lî sarhan le'allî ettali'u ilâ ilâhi Mûsâ, gloss:Haman, benim için çamurun üstünde ateş yak, bana bir kule yap; belki Musa'nın ilahına çıkıp bakarım, source:28:38}. İnsanın yaktığı ateşle kurulan kule yukarı çıkmak içindir; bu surede ise tutuşturulmuş ateşin kendisi yükselir. Saffat suresinde cennetteki bir kişi dünyadaki arkadaşını arar: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettala'a fe-raâhü fî sevâi'l-cahîm, gloss:yukarıdan baktı ve onu cehennemin ortasında gördü, source:37:55}. Aynı fiil orada tepeden aşağı bakmaktır.

Kaynaklar: 104:4 لَيُنۢبَذَنَّ ن ب ذ B001; 104:7 تَطَّلِعُ ط ل ع B001; 104:7 تَطَّلِعُ ط ل ع B002; 104:7 تَطَّلِعُ ط ل ع B006; 104:7 تَطَّلِعُ ط ل ع B007; 104:7 تَطَّلِعُ ط ل ع B010; 104:7 تَطَّلِعُ ط ل ع B004; 104:6 نَارُ ن و ر B001; 104:5 أَدْرَىٰكَ د ر ي B003; 104:5 أَدْرَىٰكَ د ر ي B005; 104:5 أَدْرَىٰكَ د ر ي B002; 104:9 عَمَدٍ ع م د B001; 104:1 هُمَزَةٍ ه م ز B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:8 مُّؤْصَدَةٌۢ و ص د B001

## Sanmak, bilmemek, bilinmek

Sure bilginin üç konumundan geçer. Önce adam sanır: {ar:يَحْسَبُ, tr:yahsebü, gloss:sanıyor, source:104:3}, iki zıttan birine hüküm vermektir {ar:حسبت كذا في معنى ظننت, tr:hasibtü kezâ fî ma'nâ zanentü, gloss:"hasibtü" "zannettim" anlamındadır, source:"ح س ب,B002"}. Kökün bir dalı ise birinin içinde ne olduğunu yoklamaktır {ar:احتسبت فلانا اختبرت ما عنده, tr:ihtesebtü fülânen ihtebertü mâ indeh, gloss:falancanın içinde ne olduğunu sınadım, source:"ح س ب,B010"}. Adamın yapmadığı yoklama, sonunda ona yapılır.

Sonra dinleyiciye bilmediği söylenir: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:hutamenin ne olduğunu sana ne bildirdi, source:104:5}. Bu fiil bilmek ve bildirilmektir {ar:دريته ودريت به أي علمت به وأدريته أي أعلمته, tr:dereytühû ve dereytü bihî ey alimtü bih, ve edreytühû ey a'lemtüh, gloss:onu bildim; ona bildirdim, source:"د ر ي,B001"}, ve kökün örnek cümlesi bildireni Allah olarak anar {ar:دريت الشيء والله أدرانيه, tr:dereytü'ş-şey'e vallâhü edrânîh, gloss:şeyi bildim, onu bana Allah bildirdi, source:"د ر ي,B001"}. Altıncı ayet de cevabı Allah'a bağlar: {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nârullâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Soru, insanın kendi bilgisiyle ulaşamayacağı bir şeyi gösterir ve cevabı yalnızca bildirilen bir bilgi olarak verir.

Son olarak ateş bilir. {ar:تَطَّلِعُ عَلَى, tr:tattali'u alâ, gloss:üzerine çıkar, source:104:7} yapısı Arapçada bir işin içyüzüne vakıf olmak için de kullanılır {ar:اطلعت على باطن أمره, tr:ittala'tü alâ bâtını emrih, gloss:işinin içyüzüne vakıf oldum, source:"ط ل ع,B003"}, {ar:أطلعني طلع هذا الأمر حتى علمته كله, tr:atla'anî tal'a hâze'l-emri hattâ alimtühû küllehû, gloss:bu işin içini bana gösterdi, hepsini öğrendim, source:"ط ل ع,B003"}. Ayetin anlamı ateşin yüreklere ulaşmasıdır; yanında, içi bilinen bir yüreğin sesi duyulur. Hesabını yapan adam kendi hesabını bilmiyordu; ateş, yürekte olanı bilir.

Kuran aynı sırayı başka surelerde de kurar. Müddessir suresinde Allah tek başına yarattığı ve {ar:وَجَعَلْتُ لَهُۥ مَالًۭا مَّمْدُودًۭا, tr:ve ce'altü lehû mâlen memdûdâ, gloss:ona uzayıp giden bir mal verdim, source:74:12} dediği adamı anlatır; sonra {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu Sekar'a sokacağım, source:74:26}, {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sekar, gloss:Sekar'ın ne olduğunu sana ne bildirdi, source:74:27}, {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ tezer, gloss:ne bırakır ne geri koyar, source:74:28}. Mal, "ne bildirdi" sorusu, ateş ve ardından bir sayı: bu surenin sırası oradadır. Karia suresinde aynı kalıp ateşe açılır: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}, {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Hakka suresinde kitabı sol eline verilen kişi iki fiili, bilmeyi ve hesabı, tek feryatta söyler: {ar:يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ, tr:yâ leytenî lem ûte kitâbiyeh, gloss:keşke kitabım bana verilmeseydi, source:69:25}, {ar:وَلَمْ أَدْرِ مَا حِسَابِيَهْ, tr:ve lem edri mâ hisâbiyeh, gloss:ve hesabımın ne olduğunu bilmeseydim, source:69:26}. Aynı surede sağdan verilen ise {ar:إِنِّى ظَنَنتُ أَنِّى مُلَٰقٍ حِسَابِيَهْ, tr:innî zanentü ennî mülâkın hisâbiyeh, gloss:ben hesabıma kavuşacağımı zaten sanıyordum, source:69:20} der; doğru sanı, hesaba kavuşacağını bilen sanıdır. Beled suresinde de aynı sanı vardır: {ar:أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ, tr:e-yahsebü en len yakdira aleyhi ehad, gloss:kimsenin ona gücünün yetmeyeceğini mi sanıyor, source:90:5}, {ar:يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا, tr:yekûlü ehlektü mâlen lübedâ, gloss:yığın yığın mal harcadım diyor, source:90:6}, {ar:أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ, tr:e-yahsebü en lem yerahû ehad, gloss:onu kimsenin görmediğini mi sanıyor, source:90:7}. Görülmediğini sanan adam, içini bilen bir ateşle karşılaşır. Meryem suresinde mal ve evlat iddia eden kişiye sorulur: {ar:أَطَّلَعَ ٱلْغَيْبَ أَمِ ٱتَّخَذَ عِندَ ٱلرَّحْمَٰنِ عَهْدًۭا, tr:ettala'a'l-ğaybe emi'ttehaze inde'r-rahmâni ahdâ, gloss:gaybı mı gördü, yoksa Rahman katında bir söz mü aldı, source:19:78}. Gaybın içine bakamayan insanın karşısında, bu surede içini bilen bir ateş durur. Karun'un iddiası da bir bilgidir {source:28:78}; Tarık suresi ise gizlilerin sınanacağı günü anar: {ar:يَوْمَ تُبْلَى ٱلسَّرَآئِرُ, tr:yevme tüble's-serâir, gloss:gizlilerin sınandığı gün, source:86:9}.

Kaynaklar: 104:3 يَحْسَبُ ح س ب B002; 104:3 يَحْسَبُ ح س ب B010; 104:5 أَدْرَىٰكَ د ر ي B001; 104:7 تَطَّلِعُ ط ل ع B003

## Buluşmalar

İlk ayetteki iki kelime iki imgeyi aynı anda taşır: el ve dil. İtme ifadesi ile gıyap ve huzur ifadesi aynı iki kelimeyi birleştirir. Mümtehine suresindeki ayet, ellerin ve dillerin birlikte kötülükle uzatılmasını {source:60:2} söyleyerek bu ikisini tek sahnede toplar. Sıkan, iten, kusur arayan ve arkadan dürten kişi, ikinci ayette malın üstüne kapanan yumruğa dönüşür. Kökte o yumruğun sonu bukağıdır, ellerin boyna toplanması {source:"ج م ع,B008"}. Hakka suresinde malının işe yaramadığını söyleyen adam bukağılanır {source:69:30}. Toplayan el ile bağlanan el, aynı kökün iki ucudur.

Sayma ile yaslanma üçüncü ayetin bir tek fiilinde buluşur: "yahsebü" hem saymanın hem yeterliğin köküdür, kalıcılık fiili de sanarak yaslanmak diye açıklanır. Tevbe suresindeki {ar:خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ, tr:hâlidîne fîhâ, hiye hasbühüm, gloss:orada kalıcı olarak; o onlara yeter, source:9:68} sözü, adamın mala yüklediği iki şeyi, kalıcılığı ve yeterliği, ateşe verir. Aynı iki imge su sahnesiyle de buluşur: sayma kökündeki kesilmeyen su, adamın sandığı süreklilik; kırıcının kökündeki tükenen mal, bu sürekliliğin sonu. Kehf suresindeki bahçe sahibi bu yolu baştan sona yürür: bahçesinin arasından nehir akar, bahçenin yok olmayacağını sanır, sanma fiiliyle aynı kökten bir "husban" bahçeyi vurur ve avuçları boş kalır {source:18:40}. Hadid suresi aynı yolu mal çoğaltma yarışının benzetmesi yapar ve "hutam" ile bitirir {source:57:20}.

Kalıcılık ile ocak arasında bir buluşma daha vardır: kalıcılık kökünde "kalıcılar" diye anılan tek şey ocak taşlarıdır. Kendini kalıcı sanan adam, ateşin altında yıllarca kalan taşların adını taşıyan bir fiille konuşur. Kalıcılık kökünün bir dalı da kalbe gider: sanı, kalpte yerleşik olan gönüle düşer. Ocak ile yürek de iki kez birleşir: yürek tutuşmayla adlandırılır ve yüreklerin kökü ateş yakmanın fiiliyle açıklanır. Altıncı ve yedinci ayetler bu yüzden bir sıfat ile onun yerini ardı ardına söyler: tutuşturulmuş ateş, tutuşmayla adlanan yüreğe çıkar. Sanının oturduğu yer, ateşin vardığı yerdir.

Sürü ile kapalı yapı sekizinci ayetin kelimesinde buluşur: aynı kök mal için dağda yapılan taş ağılı ve üstü kapatılmış ateşi adlandırır. Sürüyü ağıla kapatan adam, kapatılmış bir ateşin içindedir. Sürü ile ateş damgada buluşur: devenin ateşi damgasıdır, Tevbe suresinde biriktirilen hazine kızdırılıp alınlara basılır {source:9:35}, Kalem suresinde mal ve oğullar sahibi hemmâz burnundan damgalanır {source:68:16}. Bu son ayet ilk imge ile sürüyü birbirine bağlar: iğneleyen dil, mal ve damga aynı adamdadır.

Yükselen ateş ile avcı, aynı kökün iki dalında buluşur: ateşin yükselişini anlatan fiil, okun hedefin üstünden aşmasını da adlandırır ve bu ateş aşmaz, yüreklerin üstünde durur. Avcının kolladığı yer yürektir; yüreklerin kökü avı kalbinden vurmaktır. Bilmek ile avcılık da beşinci ayetin fiilinde aynı köktür: görmeden kollamak ve bilmek. Sanan adam ile içini bilen ateş arasındaki mesafeyi, "ne bildirdi" sorusu kapatır ve cevabı Allah'ın ateşi olarak verir.

Surenin hareketi bu buluşmalarla taşınır. İlk iki ayette her şey adamın elindedir: sıkan, iten, toplayan, sayan bir el ve onu yaralayan bir dil. Üçüncü ayette bu el bir sanıya dayanır ve kalbe yerleşir. Dördüncü ayetten sonra yön tersine döner: el açılır ve atılan adamın kendisidir; topladığı malın adı kırıntı olur, saydığı sayı onu saymaz, dayandığı direkler onu tutar, sürüsünü kapattığı ağıl üzerine kapanır. Ateş aşağıdan yükselir ve sanının oturduğu yüreğe ulaşır. İlk ayetteki kuşatma kelimesinden son ayetteki direklere kadar sure, dışarıya uzanan bir elden içeriye kapanan bir yapıya doğru ilerler.

