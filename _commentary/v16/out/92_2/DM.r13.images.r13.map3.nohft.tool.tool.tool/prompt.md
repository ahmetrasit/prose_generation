Focus: 92:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_2/D.r13/context.md =====
# 92:2 — focus

وَٱلنَّهَارِ إِذَا تَجَلَّىٰ

Anchor translation (canonical reading, reference only):

Açığa çıktığı zaman gündüze,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلنَّهَارِ | نَهَار | ن ه ر | CONJ;DET;N |
| 2 | إِذَا | إِذَا |  | T |
| 3 | تَجَلَّىٰ | تَجَلَّىٰ | ج ل و | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 92 — full text (context; no pericope)

- 92:1 وَٱلَّيْلِ إِذَا يَغْشَىٰ
- 92:2 ◀ focus وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- 92:3 وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- 92:4 إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- 92:5 فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- 92:6 وَصَدَّقَ بِٱلْحُسْنَىٰ
- 92:7 فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- 92:8 وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- 92:9 وَكَذَّبَ بِٱلْحُسْنَىٰ
- 92:10 فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- 92:11 وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- 92:12 إِنَّ عَلَيْنَا لَلْهُدَىٰ
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ه ر (root_001559) — identity root of وَٱلنَّهَارِ (w1)

- **B001** bol su taşıyan doğal akarsu yatağı — taşkın suyun aktığı doğal akarsu yatağı · akarsu yatakları · akarsular veya akarsu yatakları · akarsu yatağı sağlam bir güzergah edindi · su aktı ve kendine bir yatak açtı · bol sulu veya geniş akarsu · suyun kazıp açtığı yatak yeri · kuyu kazısı suya ulaştı
  النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)
- **B002** şafaktan gün batımına aydınlık gündüz — şafaktan güneş batımına kadar süren aydınlık gündüz · aydınlık gündüz süreleri · gündüz vaktinde baskın yapan kimse · gündüzün aydınlığına girdik
  النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)
- **B003** bir şeyi açma veya genişletme — genişlik veya aydınlıkla birlikte genişlik · kanı açıp serbest bırakarak akıttı · yaranın veya yarığın açıklığını genişletti · genişledi · evlerin önleri arasında atık bırakılan açık alan · bağırsağı çözüldü ve akarsu gibi boşaldı · tehlikeler; birleşik bir türetme olarak açıklanan biçim
  أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)
- **B004** sert sözle azarlayıp engelleme [kalıp] — onu sert sözle azarlayıp engelledi
  نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)
- **B005** bazı kuşların yavrusu — türü aktarıma göre değişen bir kuş yavrusu
  النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)
- **B006** fırsat kollayıp gizlice kapma — fırsat kollayıp ani biçimde gizlice kapma
  النهر الدغرة وهي الخلسة (tahdhib)
- **B007** kişi, yer ve yıldızlara ait özel adlar — belirli bir topluluktan bir şairin adı · bir yer adı · sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad
  نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)
- **B008** bulut — bulut
  الناهُور السحاب (tahdhib)

## ج ل و (root_000256) — identity root of تَجَلَّىٰ (w3)

- **B001** örtülünün açığa çıkması veya çıkarılması — örtülü şeyi açığa çıkarmak · açık, belirgin; açık kanıt · haber benim için açıklığa kavuştu · hastalığı gidermek veya kaygıyı dağıtmak · ortaya çıkmak, görünür olmak · örtücü durum dağılıp açılmak · birbirimizin hali karşılıklı olarak ortaya çıktı · sarığı alından katlayarak kaldırmak
  انكشاف الشيء وبروزه (maqayis)؛ أمر جلي واضح وأجل لنا هذا الأمر أي أوضحه وجلا الله عنك المرض (ayn)؛ الجلي نقيض الخفي وجلا لي الخبر وجلوت أي أوضحت وكشفت وانجلى عنه الهم وتجالينا (sihah)؛ أصل الجلو الكشف الظاهر والتجلي قد يكون بالذات وبالأمر والفعل (mufradat)
- **B002** kılıcı parlatma ve göz boyasıyla görüşü berraklaştırma — kılıcı parlatıp temizlemek · görüşü berraklaştırdığı kabul edilen göz boyası · görüşü göz boyasıyla berraklaştırmak
  جلوت السيف جلاء (maqayis;mufradat)؛ جلا الصيقل السيف واجتلاه (ayn;tahdhib)؛ الجلا مقصور الإثمد لأنه يجلو البصر (ayn)؛ جلوت بصري بالكحل والجلا كحل (sihah;tahdhib)
- **B003** gelini törende gösterme veya gösterilmiş gelini görme [kalıp] — gelini düğünde görünür biçimde sunmak · sunulmuş gelini görmek
  جلوت العروس جلوة وجلاء (maqayis;mufradat)؛ الماشطة تجلو العروس وقد جليت على زوجها واجتلاها زوجها أي نظر إليها (ayn;tahdhib)؛ جلوت العروس جلاء وجلوة واجتليتها إذا نظرت إليها مجلوة (sihah)
- **B004** yerleşimden ayrılma veya çıkarılma — yurttan veya yerleşimden ayrılma · onları ülkeden çıkarmak · yurdundan ayrılmış topluluk; yönetim korumasında özel vergi ödeyen topluluk · çevresinde toplanılan şeyin yanından açılıp dağılmak
  جلا القوم عن منازلهم جلاء وأجليتهم (maqayis)؛ الجلاء أن يجلو قوم عن بلادهم والجالية أهل الذمة (ayn)؛ الجلاء الخروج من البلد والجالية الذين جلوا عن أوطانهم (sihah)؛ أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها (mufradat)
- **B005** ön saç çizgisinin gerilemesi — ön saçları çekilmiş kişi; ön saçların çekilmesi · geniş ve güzel alın · başın ön kısımları ve saçsız bölgeleri
  رجل أجلى إذا ذهب شعر مقدم رأسه وهو الجلا (maqayis)؛ الجبهة الجلواء والرجل أجلى (ayn)؛ انحسار مقدم الرأس (jamhara)؛ الجلاء انحسار الشعر عن مقدم الرأس والمجالي مقادم الرأس (sihah)؛ فهو أجلى مع الجلا (tahdhib)؛ رجل أجلى انكشف بعض رأسه عن الشعر (mufradat)
- **B006** adı ve konumu herkesçe bilinen kişi [kalıp] — herkesçe tanınan, durumu gizli olmayan kişi
  هو ابن جلا إذا كان لا يخفى أمره لشهرته (maqayis)؛ أنا ابن جلا أي أنا ابن الواضح الأمر المشهور (ayn)؛ الجلا الأمر الواضح المكشوف وأنا ابن جلا (jamhara)؛ كأنه يقال له جلا الأمور وكشفها (sihah)؛ هو ابن جلا للرجل إذا كان عالي الشرف لا يخفى مكانه (tahdhib)؛ فلان ابن جلا أي مشهور (mufradat)
- **B007** açık gök ve aydınlanan gündüz — bulutsuz, açık gök · bir gündüzlük aydınlık süre · gündüzün güneşi belirginleştirmesi
  السماء جلواء أي مصحية (maqayis;sihah;mufradat)؛ جلاء يوم واحد أي بياض يوم (ayn;tahdhib)؛ والنهار إذا جلاها إذا بين الشمس (tahdhib)
- **B008** başı kaldırıp bakışı hedefe yöneltme — başı ve gözleri kaldırıp bakışı ava yöneltmek · bir şeye gözeterek ve beklentiyle bakmak
  البازي يجلي إذا آنس الصيد فرفع طرفه ورأسه وتجليت الشيء نظرت إليه (ayn)؛ جلى ببصره تجلية إذا رمى به كما ينظر الصقر إلى الصيد (sihah)؛ التجلي النظر بالأشراف (tahdhib)
- **B009** gelin gösteriminde verilen armağan [kalıp] — eşinin gelin gösterimi sırasında ona bir hizmetçi armağan etmesi
  جلاها زوجها وصيفا أي أعطاها وما جلوتها بالكسر (sihah)؛ جلى فلان امرأته وصيفا حين اجتلاها أي أعطاها وصيفا عند جلوتها وما جلوتها بالكسر (tahdhib)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:2, and ## Buluşmalar) =====
## Örten gece, yarılan gündüz

Surenin ilk iki ayeti iki vakit adı verir, ama asıl taşıdıkları şey iki işlemdir. Birinci ayetteki fiil {ar:يَغْشَىٰ, tr:yağşâ, gloss:örter, source:92:1} bir şeyin üstüne başka bir şeyin serilmesini anlatır. Kökün temel anlamı {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedüllü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"} diye verilir. Bu işin aleti de aynı köktendir: {ar:الغشاء الغطاء, tr:el-ğışâu'l-ğıtâ', gloss:ğışâ örtü demektir, source:"غ ش و,B001"}. Gece kendi başına değil, karşısındakiyle tanımlanır: {ar:الليل خلاف النهار, tr:el-leylü hılâfü'n-nehâr, gloss:gece gündüzün karşıtıdır, source:"ل ي ل,B001"}. Ayette gecenin neyi örttüğü söylenmez, fiilin nesnesi yoktur. Bir önceki surede aynı iki fiil nesneleriyle gelmişti: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3} ve {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰهَا, tr:ve'l-leyli izâ yağşâhâ, gloss:onu örttüğünde geceye andolsun, source:91:4}. Orada örtülüp açılan şey güneşti. Burada nesne düşer ve örtü belli bir şeyin değil, görünen her şeyin üstüne serilir. Gündüzün fiili de değişir: {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp göründüğünde gündüze andolsun, source:92:2}. Gündüz artık başka bir şeyi göstermez, kendini gösterir.

Bu yazıda bir kelimenin kök ailesinden gelen görüntüler, kelimenin ayetteki anlamının yanında duyulur. O anlamın yerine geçmezler. Gündüzün işleyişi bu ailede üç katmanda görünür. İlk katmanda ışık yayılır: gündüz {ar:الوقت الذي ينتشر فيه الضوء, tr:el-vaktu'llezî yenteşiru fîhi'd-dav', gloss:ışığın yayıldığı vakit, source:"ن ه ر,B002"} diye tanımlanır. İkinci katmanda kökün genel resmi bir açılmadır: {ar:أصل صحيح يدل على تفتح شيء أو فتحه, tr:aslun sahîhun yedüllü alâ tefettuhi şey'in ev fethih, gloss:bir şeyin açılıvermesini ya da açılmasını gösteren sağlam kök, source:"ن ه ر,B003"}. Üçüncü katmanda nehir de adını buradan alır: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:sümmiye'n-nehru li-ennehû yenhuru'l-arda ey yeşukkuhâ, gloss:nehre bu ad verildi çünkü toprağı yarar, source:"ن ه ر,B001"}. Gündüzün fiilinin kökü ise {ar:انكشاف الشيء وبروزه, tr:inkişâfü'ş-şey'i ve burûzuh, gloss:bir şeyin üstünün açılması ve öne çıkması, source:"ج ل و,B001"} demektir. Aynı kökte {ar:الجلي نقيض الخفي, tr:el-celiyyu nakîdu'l-hafiyy, gloss:açık olan gizlinin zıddıdır, source:"ج ل و,B001"} denir ve bulutsuz gök için {ar:السماء جلواء أي مصحية, tr:es-semâu celvâu ey mushiye, gloss:gök açık yani bulutsuz, source:"ج ل و,B007"} kullanılır. Sahne böylece kurulur: Gece üstten serilen bir katmandır. Gündüz bu katmanı nehrin toprağı yarması gibi yarar, ışık yayılır ve altta kalan şey öne çıkıp seçilir hâle gelir. Düz bir anlatım "geceye ve gündüze yemin" deyip geçer. İşlem görülünce yemin, surenin geri kalanının modelini verir: İnsanların koşusu bir süre aynı örtünün altında birbirine benzer, sonra gün yarılınca {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa'yeküm leşettâ, gloss:sizin koşunuz elbette dağınık ve ayrı ayrıdır, source:92:4} hükmü görünür olur.

Kur'an iki işlemi başka yerlerde de yan yana sahneler. Allah gökleri ve yeri yaratan Rab olarak kendini anlatırken geceyi gündüzün üstüne çeker: {ar:يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًا, tr:yuğşi'l-leyle'n-nehâra yatlubuhû hasîsâ, gloss:geceyi gündüzün üstüne örter ve gece onu hızla kovalar, source:7:54}. Aynı ayet {ar:أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ, tr:elâ lehu'l-halku ve'l-emr, gloss:bilin ki yaratmak da buyurmak da O'nundur, source:7:54} diye kapanır ve üçüncü ayetin fiilini, yaratmayı, örtünün hemen yanına koyar. Başka bir ayette işlem tersten görülür, gündüz gecenin üstünden soyulan bir deridir: {ar:ٱلَّيْلُ نَسْلَخُ مِنْهُ ٱلنَّهَارَ, tr:el-leylü neslehu minhü'n-nehâr, gloss:gece; ondan gündüzü soyarız, source:36:37}. Gündüzün fiilinin en ağır kullanımı Musa'nın sahnesindedir. Musa Rabbini görmek istemiş, ona dağa bakması söylenmiştir: {ar:فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ, tr:fe-lemmâ tecellâ rabbuhû li'l-cebel, gloss:Rabbi dağa tecellî edince, source:7:143}. Ayetin devamında dağ dümdüz olur ve Musa bayılıp düşer. Açılmanın gücü, örtünün neyi koruduğunu da gösterir.

Aynı aile örtüyü göze de taşır. Gözün ya da kalbin üstündeki zar da bu köktendir: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâve mâ ğaşiye'l-kalbe min reyni't-tab', gloss:ğışâve kalbi kaplayan mühür pasıdır, source:"غ ش و,B001"}. Karşı kök gözü temizleyen sürmeyi adlandırır: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ maksûru'l-ismid li-ennehû yeclu'l-basar, gloss:celâ sürmedir çünkü gözü açar, source:"ج ل و,B002"}. Aynı kök cilacının kılıcı parlatmasını da adlandırır: {ar:جلا الصيقل السيف واجتلاه, tr:celâ's-saykalu's-seyfe ve'ctelâh, gloss:cilacı kılıcı parlattı, source:"ج ل و,B002"}. Temizlenmiş bakış ise hedefe fırlatılır: {ar:جلى ببصره تجلية إذا رمى به كما ينظر الصقر إلى الصيد, tr:cellâ bi-basarihî tecliyeten izâ remâ bihî kemâ yenzuru's-sakru ile's-sayd, gloss:doğanın avına baktığı gibi bakışını fırlattı, source:"ج ل و,B008"}. Kur'an zarı reddedenlerin gözüne yerleştirir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:ve alâ ebsârihim ğışâvetün, gloss:gözlerinin üstünde bir perde vardır, source:2:7}. Hevesini ilah edinen adamın durumu da şöyle anlatılır: {ar:وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ, tr:ve ceale alâ basarihî ğışâveten fe-men yehdîhi min ba'di'llâh, gloss:gözüne perde çekti; Allah'tan sonra onu kim yola getirir, source:45:23}. Burada perdenin hemen ardından yol gösterme sorusu gelir. Önüne ve arkasına set çekilenler için {ar:فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ, tr:fe-ağşeynâhüm fehüm lâ yubsirûn, gloss:onları örttük de görmüyorlar, source:36:9} denir. Tersi Diriliş gününde, dünyada gafil kalmış olana söylenir: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğıtâeke fe-basaruke'l-yevme hadîd, gloss:örtünü kaldırdık; bugün gözün demir gibi keskindir, source:50:22}.

Surenin devamı bu çifti adım adım işler. On ikinci ayet {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. Bu kelimenin ailesinde {ar:الهدى البيان, tr:el-hüdâ el-beyân, gloss:hidayet açıklığa kavuşturmaktır, source:"ه د ي,B001"} anlamı vardır. Böylece gündüzün işi olan açığa çıkarmayı Allah kendi üstüne alır. On dördüncü ayetin ateşi bu ailede gözü açan malzemeyi de verir: {ar:النؤور دخان الفتيلة يتخذ كحلا أو وشما, tr:en-neûr duhânu'l-fetîle yuttehazu kuhlen ev veşmâ, gloss:fitilin isi sürme ya da dövme yapılır, source:"ن و ر,B008"}. Uyarı ateşi, kendi kökünde, göze sürülen bir aydınlatmadır. Yirminci ayetteki yüzün ailesinde ise günün açılan ilk cephesi durur: {ar:وجه النهار أوله, tr:vechu'n-nehâri evvelüh, gloss:günün yüzü onun başlangıcıdır, source:"و ج ه,B007"}. Sure gecenin örtüsüyle başlar ve aranan bir yüzle biter. O yüz, kelimenin ailesinde, sabahın ilk açılan yüzünün yanında durur.

Örtünün en geniş biçimi bütün yaratılmışları saran olaydır: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâme li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:ğâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Kur'an aynı adla sorar: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:sarıp kaplayanın haberi sana geldi mi, source:88:1}. Örtü yüzlere de düşer. En güzeli yapanlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehüm katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma kaplar, source:10:26} denir. Kötülük kazananlar için ise {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhüm kıta'an mine'l-leyli muzlimâ, gloss:sanki yüzlerine gecenin karanlık parçaları örtülmüştür, source:10:27} denir. Ateş de aynı fiille yüzleri örter: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehümü'n-nâr, gloss:ateş yüzlerini örter, source:14:50}. Ama örtü kendiliğinden kötü değildir. Uhud'daki kederden sonra Allah müminlere bir güven indirmiştir: {ar:أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ, tr:emeneten nuâsen yağşâ tâifeten minküm, gloss:içinizden bir kesimi saran bir güven ve uyuklama, source:3:154}. Gece de böyledir: bir işarettir, dinlendirir. Tehlikeli olan, örtünün altında kalıp gün açıldığında da görmek istememektir.

Kaynaklar: 92:1 ٱلَّيْلِ ل ي ل B001; 92:1 يَغْشَىٰ غ ش و B001; 92:1 يَغْشَىٰ غ ش و B002; 92:2 ٱلنَّهَارِ ن ه ر B001; 92:2 ٱلنَّهَارِ ن ه ر B002; 92:2 ٱلنَّهَارِ ن ه ر B003; 92:2 تَجَلَّىٰ ج ل و B001; 92:2 تَجَلَّىٰ ج ل و B002; 92:2 تَجَلَّىٰ ج ل و B007; 92:2 تَجَلَّىٰ ج ل و B008; 92:12 لَلْهُدَىٰ ه د ي B001; 92:14 نَارًۭا ن و ر B008; 92:20 وَجْهِ و ج ه B007

## Erkek ve dişi: örtünme, gelin, doğum

Üçüncü ayet ilk iki ayetin çiftini bir başka çifte bağlar: {ar:وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ, tr:ve mâ halaka'z-zekera ve'l-ünsâ, gloss:erkeği ve dişiyi yaratana andolsun, source:92:3}. Çift tanımının içinde birbirine bağlıdır: {ar:الذكر خلاف الأنثى, tr:ez-zekeru hılâfü'l-ünsâ, gloss:erkek dişinin karşıtıdır, source:"ذ ك ر,B001"}. Gece gündüzün karşıtı olduğu gibi erkek de dişinin karşıtıdır. İlk iki ayetin fiilleri, evliliğin diliyle okunduğunda bu üçüncü ayete doğru akar. Örtme fiili kadına yaklaşmayı da adlandırır: {ar:الغشيان غشيان الرجل المرأة, tr:el-ğışyânu ğışyânü'r-racüli'l-mer'e, gloss:ğışyân erkeğin kadına girmesidir, source:"غ ش و,B004"}. Aynı fiil bir yere gelmeyi anlatırken de kullanılır: {ar:غشيت موضع كذا أتيته وكني بذلك عن الجماع, tr:ğaşîtü mevdıa kezâ eteytühû ve küniye bi-zâlike ani'l-cimâ', gloss:falan yere varmak; birleşme bununla kinaye edilir, source:"غ ش و,B004"}. Gündüzün fiili gelinin açılışıdır: {ar:الماشطة تجلو العروس وقد جليت على زوجها واجتلاها زوجها أي نظر إليها, tr:el-mâşitatü teclu'l-arûse ve kad cüliyet alâ zevcihâ ve'ctelâhâ zevcuhâ ey nazara ileyhâ, gloss:gelini süsleyen kadın onu açar; gelin kocasına gösterilir ve kocası ona bakar, source:"ج ل و,B003"}. Bu açılışın bir hediyesi vardır: {ar:جلاها زوجها وصيفا أي أعطاها, tr:celâhâ zevcuhâ vasîfen ey a'tâhâ, gloss:kocası onu açarken ona bir hizmetçi verdi, source:"ج ل و,B009"}. Bu deyim ikinci ayetin fiilini beşinci ayetin fiiliyle, {ar:أَعْطَىٰ, tr:a'tâ, gloss:verdi, source:92:5} ile aynı cümlede buluşturur. Gelin kocasına götürülür: {ar:هديت العروس إلى زوجها, tr:hüdiyeti'l-arûsu ilâ zevcihâ, gloss:gelin kocasına götürüldü, source:"ه د ي,B006"}. On ikinci ayetin hidayeti burada yol göstermenin yanında bir götürüş, bir kavuşturma olarak duyulur. Altıncı ayetin kökü ise mehri adlandırır: {ar:الصداق صداق المرأة, tr:es-sadâku sadâku'l-mer'e, gloss:sadâk kadının mehridir, source:"ص د ق,B007"}. Bu, ayetteki {ar:وَصَدَّقَ, tr:ve saddaka, gloss:ve doğruladı, source:92:6} fiilinin anlamı değildir, aynı ailenin başka bir dalıdır. Kur'an mehri vermeyi şu sözlerle buyurur: {ar:وَءَاتُوا۟ ٱلنِّسَآءَ صَدُقَٰتِهِنَّ نِحْلَةًۭ, tr:ve âtu'n-nisâe sadukâtihinne nihle, gloss:kadınlara mehirlerini gönülden bir armağan olarak verin, source:4:4}. Bu ayette on sekizinci ayetin vermesi ile altıncının kökü tek emirde durur.

Kur'an örtünmenin ardından geleni de sahneler. Allah ilk can ile eşini anlatır: {ar:فَلَمَّا تَغَشَّىٰهَا حَمَلَتْ حَمْلًا خَفِيفًۭا, tr:fe-lemmâ teğaşşâhâ hamelet hamlen hafîfâ, gloss:onu örtünce hafif bir yük yüklendi, source:7:189}. Yük ağırlaşınca ikisi Rablerine bir söz verir: {ar:لَئِنْ ءَاتَيْتَنَا صَٰلِحًۭا لَّنَكُونَنَّ مِنَ ٱلشَّٰكِرِينَ, tr:lein âteytenâ sâlihan le-nekûnenne mine'ş-şâkirîn, gloss:bize iyi bir çocuk verirsen şükredenlerden olacağız, source:7:189}. Ardından şu gelir: {ar:فَلَمَّآ ءَاتَىٰهُمَا صَٰلِحًۭا جَعَلَا لَهُۥ شُرَكَآءَ فِيمَآ ءَاتَىٰهُمَا ۚ فَتَعَٰلَى ٱللَّهُ عَمَّا يُشْرِكُونَ, tr:fe-lemmâ âtâhumâ sâlihan ceala lehû şürekâe fîmâ âtâhumâ fe-teâla'llâhu ammâ yüşrikûn, gloss:onlara iyi bir çocuk verince verdiği şeyde O'na ortaklar koştular; Allah onların ortak koştuklarından çok yücedir, source:7:190}. Bu iki ayet surenin çizgisini küçük ölçekte taşır: örtünme, doğum, verilen bir armağan, verilen sözün çiğnenmesi ve en sonda yirminci ayetteki {ar:ٱلْأَعْلَىٰ, tr:el-a'lâ, gloss:en yüce, source:92:20} kelimesinin kökünden bir fiil. Gece ile birleşme orucun gecelerinde de yan yana gelir: {ar:هُنَّ لِبَاسٌۭ لَّكُمْ وَأَنتُمْ لِبَاسٌۭ لَّهُنَّ, tr:hünne libâsün leküm ve entüm libâsün lehünn, gloss:onlar sizin için giysi, siz de onlar için giysisiniz, source:2:187}. O gece {ar:حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ, tr:hattâ yetebeyyene lekümü'l-haytu'l-ebyadu mine'l-hayti'l-esvedi mine'l-fecr, gloss:şafakta beyaz iplik siyah iplikten ayırt edilinceye dek, source:2:187} sürer. Gündüzün açılışı burada bir ipliğin ötekinden ayrılmasıdır. Çiftin yaratılışı da açıkça söylenir: {ar:وَأَنَّهُۥ خَلَقَ ٱلزَّوْجَيْنِ ٱلذَّكَرَ وَٱلْأُنثَىٰ, tr:ve ennehû halaka'z-zevceyni'z-zekera ve'l-ünsâ, gloss:çifti, erkeği ve dişiyi O yarattı, source:53:45}. Ardından gelen {ar:مِن نُّطْفَةٍ إِذَا تُمْنَىٰ, tr:min nutfetin izâ tumnâ, gloss:atıldığında bir damladan, source:53:46} ifadesi çiftten doğuma geçer.

Doğumun dili surenin üç kelimesini tek kalıba döker. Ana rahmindeki et parçası {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatün muhallakatün ey tâmmetü'l-halk, gloss:biçimlenmiş yani yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"} diye anılır. Erkek doğurmak {ar:أذكرت ولدت ذكرا والمذكار تلد الذكور, tr:ezkerat veledet zekeran ve'l-mizkâru teledü'z-zükûr, gloss:erkek doğurdu; mizkâr hep erkek doğurandır, source:"ذ ك ر,B001"} ile, kız doğurmak da {ar:آنثت المرأة إذا ولدت أنثى, tr:ânesetil-mer'etü izâ veledet ünsâ, gloss:kadın kız doğurdu, source:"ء ن ث,B001"} ile anlatılır. Zor doğum onuncu ayetin kökündendir: {ar:أعسرت المرأة إذا عسر عليها ولادها, tr:a'sarati'l-mer'etü izâ asüra aleyhâ vilâduhâ, gloss:kadının doğumu zorlaştı, source:"ع س ر,B006"}. Eski bir dua ve eski bir beddua bu kelimeleri birbirine bağlar: {ar:أيسرت وأذكرت, tr:eyserti ve ezkerti, gloss:kolay doğur ve erkek doğur, source:"ع س ر,B006"} ve {ar:أعسرت وآنثت, tr:a'serti ve ânesti, gloss:zor doğur ve kız doğur, source:"ع س ر,B006"}. Üçüncü ayetin erkeği ve dişisi, yedinci ayetin {ar:لِلْيُسْرَىٰ, tr:li'l-yüsrâ, gloss:en kolaya, source:92:7} kelimesi ve onuncu ayetin {ar:لِلْعُسْرَىٰ, tr:li'l-usrâ, gloss:en zora, source:92:10} kelimesi bu formülde aynı ağızdan çıkar. Formül kolaylığı oğula, zorluğu kıza bağlar. Sure aynı kelimeleri tutar ama bağı çözer. Erkeği de dişiyi de yaratan üzerine yemin eder ve kolaylığı ile zorluğu doğan çocuğun cinsine değil, verip vermemeye bağlar. Yaygın bir değer ölçüsü burada sessizce yerinden çıkar.

Kur'an bu ölçünün kendisini de sahneler. Kız müjdesi alan adam için {ar:وَإِذَا بُشِّرَ أَحَدُهُم بِٱلْأُنثَىٰ ظَلَّ وَجْهُهُۥ مُسْوَدًّۭا وَهُوَ كَظِيمٌۭ, tr:ve izâ büşşira ehadühüm bi'l-ünsâ zalle vechuhû müsvedden ve hüve kezîm, gloss:birine kız müjdelendiğinde yüzü kapkara kesilir ve öfkesini yutar, source:16:58} denir. Gecenin karanlığı adamın yüzüne iner. İmran'ın karısı ise karnındakini Allah'a adamıştır: {ar:إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا, tr:innî nezertü leke mâ fî batnî muharrarâ, gloss:karnımdakini sana azat edilmiş olarak adadım, source:3:35}. Doğumdan sonra şöyle der: {ar:رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ, tr:rabbi innî vada'tühâ ünsâ, gloss:Rabbim onu kız doğurdum, source:3:36}. Kur'an araya kendi sözünü koyar: {ar:وَٱللَّهُ أَعْلَمُ بِمَا وَضَعَتْ, tr:va'llâhu a'lemu bimâ vada'at, gloss:Allah onun ne doğurduğunu daha iyi bilir, source:3:36}. Bir sonraki ayette Rabbi o kızı güzel bir kabulle kabul eder {source:3:37}. Allah da şunu söyler: {ar:يَهَبُ لِمَن يَشَآءُ إِنَٰثًۭا وَيَهَبُ لِمَن يَشَآءُ ٱلذُّكُورَ, tr:yehebu li-men yeşâu inâsen ve yehebu li-men yeşâu'z-zükûr, gloss:dilediğine kızlar dilediğine erkekler bağışlar, source:42:49}. Zor doğum gerçektir ve Kur'an onu anneye borçluluğun gerekçesi olarak anar: {ar:حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا, tr:hamelethü ümmühû kürhen ve vada'athü kürhâ, gloss:annesi onu zahmetle taşıdı ve zahmetle doğurdu, source:46:15}. Surenin bağlantısını en açık kuran ayet gebe kadınların bekleme süresini anlatır: süreleri {ar:أَن يَضَعْنَ حَمْلَهُنَّ, tr:en yeda'ne hamlehünn, gloss:yüklerini bırakmalarıdır, source:65:4}. Ayet hemen ardından {ar:وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا, tr:ve men yettekı'llâhe yec'al lehû min emrihî yüsrâ, gloss:kim Allah'tan sakınırsa işinde ona bir kolaylık verir, source:65:4} der. Doğumun bağlamında takva ile kolaylık yan yana konur. Bu, beşinci ve yedinci ayetlerin bağıdır. İnsanın yaratılışı da aynı fiille anlatılır: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddarah, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19} ve {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:sümme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20}. Rahimden çıkış yolu ile hayatın yolu tek fiille kolaylaştırılır.

Kaynaklar: 92:1 يَغْشَىٰ غ ش و B004; 92:2 تَجَلَّىٰ ج ل و B003; 92:2 تَجَلَّىٰ ج ل و B009; 92:3 خَلَقَ خ ل ق B003; 92:3 ٱلذَّكَرَ ذ ك ر B001; 92:3 وَٱلْأُنثَىٰٓ ء ن ث B001; 92:6 وَصَدَّقَ ص د ق B007; 92:10 لِلْعُسْرَىٰ ع س ر B006; 92:12 لَلْهُدَىٰ ه د ي B006

## Yolu gösteren ateş, kervanın başı ve sonu

Ateş ile ışık aynı yerden adlandırılır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru sümmiyâ bi-zâlike min tarîkati'l-idâe, gloss:nur ve nar bu adı aydınlatma yönünden almıştır, source:"ن و ر,B001"}. Ateşin yol göstermede eski bir işi vardır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yünevvirûne fi'l-câhiliyyeti li-yühtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu işin bir de işareti vardır: {ar:المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها, tr:el-menâr alemü't-tarîk; darabe'l-menâra alâ tarîkıhî li-yühtedâ bihâ, gloss:menâr yolun işaretidir; yolu bulunsun diye yolunun üstüne işaret dikti, source:"ن و ر,B005"}. Yolcu bu ateşi uzaktan görür ve ona yönelir: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertü'n-nâra min baîd: tebassartühâ, gloss:ateşi uzaktan gözledim, source:"ن و ر,B003"}; {ar:تنورت نارا قصدت إليها, tr:tenevvertü nâran kasadtü ileyhâ, gloss:bir ateşe doğru yöneldim, source:"ن و ر,B003"}. Hidayet de tam bu işi adlandırır: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytühü't-tarîka ve'l-beyte hidâyeten ey arraftüh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. Başka bir tanım {ar:الهداية دلالة بلطف؛ تعريف الطرق, tr:el-hidâyetü delâletün bi-lutf; ta'rîfü't-turuk, gloss:hidayet incelikle yol göstermektir; yolları tanıtmaktır, source:"ه د ي,B001"} der. Sahne şöyle işler: Karanlıkta yüksek bir yere ateş yakılır, yolcu onu uzaktan görür, yönünü ona göre düzeltir ve ateş yolun nerede olduğunu bildirmiş olur. Gündüzün yaygın ışığında yol zaten görünür. Gece ise yolu ancak böyle bir ateş gösterir.

Surede on ikinci ayet {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. İki ayet sonra bir ateş yakılır: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertüküm nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}. Ayetteki anlam, kaçınılacak alevdir. Kelimenin ailesi ise aynı ateşin bir işaret ateşi olarak da duyulmasını sağlar: Uyarı ateşi yolun nerede bittiğini bildirerek yol gösterir. Yirminci ayetin yüzü de bu sahneye girer: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıın istakbeltehû, gloss:vicheti yöneldiğin her yerdir, source:"و ج ه,B002"}. Aynı dalda yolun ayakla açılması da anlatılır: {ar:وجهوا للناس الطريق إذا وطئوه وسلكوه, tr:vecchehû li'n-nâsi't-tarîka izâ vetıûhü ve selekûh, gloss:yolu çiğneyip yürüyerek insanlara açtılar, source:"و ج ه,B002"}. Rabbinin yüzünü arayan, o yüze dönük yürüyerek yolu belirgin kılar.

Kur'an bu sahneyi Musa ile kurar. Musa ailesiyle yolculuk ederken bir ateş görür ve onlara şöyle der: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestü nâran leallî âtîküm minhâ bi-kabesin ev ecidü ale'n-nâri hüdâ, gloss:bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Ateş, yol bulma ve getirip vermek aynı cümlede durur. Başka bir anlatımda Musa süreyi doldurmuş, ailesiyle yola çıkmıştır ve ateşi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-tûri nârâ, gloss:Tur'un yanından bir ateş gördü, source:28:29} diye görür. "Yan" kelimesi on yedinci ayetin köküdür. Üçüncü anlatımda ateşin bir başka işi söylenir: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Isınmak fiili on beşinci ayetteki {ar:يَصْلَىٰهَآ, tr:yaslâhâ, gloss:ona girip yanar, source:92:15} fiiliyle aynı köktendir. Musa'nın ateşi yanına yaklaşılan, ısıtan ve yol gösteren ateştir. Surenin ateşi ise içine girilen ateştir. Aynı kök iki mesafeyi ayırır. Gece yolculuğunda Kur'an başka işaretler de koyar: {ar:لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ, tr:li-tehtedû bihâ fî zulümâti'l-berri ve'l-bahr, gloss:karanın ve denizin karanlıklarında onlarla yol bulasınız diye, source:6:97}; {ar:وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ, tr:ve alâmâtin ve bi'n-necmi hüm yehtedûn, gloss:işaretler de koydu; onlar yıldızla yol bulurlar, source:16:16}.

Hidayetin ailesi yolu gösteren ateşin yanına bir yürüyüş düzeni de koyar. Öndeki şey hâdîdir: {ar:الهادي من كل شيء أوله, tr:el-hâdî min külli şey'in evveluh, gloss:her şeyin hâdîsi onun önüdür, source:"ه د ي,B003"}. Aynı tanım {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelü raîl, gloss:atların hâdîleri boyunları ya da ilk bölüktür, source:"ه د ي,B003"} ve {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlü yüsemmâ hâdiyen li-tekaddumih, gloss:kılavuza önde yürüdüğü için hâdî denir, source:"ه د ي,B003"} diye sürer. Sürünün önündeki deve için {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatün evvelatün ve cemelün evvelü izâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi ve erkek deveye evvel denir, source:"ء و ل,B001"} denir. Arkada kalanlar için {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun sonu, en arkada olanlardır, source:"ء خ ر,B001"} denir. Semerin de bir ön ve bir arka direği vardır: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratü'r-rahli ve kâdimetühû ve muahhiru'r-rahli ve mukaddimuh, gloss:semerin arka ve ön kaşı, source:"ء خ ر,B003"}. Gece ve gündüz yürüyüşün iki ayrı düzenidir: {ar:لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل, tr:lestü bi-leyliyyin ve lâkinnî neharun ey esîru bi'n-nehâri ve lâ utîku sura'l-leyl, gloss:gececi değilim, gündüzcüyüm; gündüz yürürüm, gece yürüyüşüne dayanamam, source:"ل ي ل,B002"}; {ar:رجل نهر صاحب نهار, tr:racülün neharun sâhibu nehâr, gloss:gündüz adamı, source:"ن ه ر,B002"}. On ikinci ve on üçüncü ayet bu düzende birlikte işitilir: {ar:وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ, tr:ve inne lenâ le'l-âhirete ve'l-ûlâ, gloss:sonuncu da ilki de elbette bizimdir, source:92:13}. Kervanın önündeki kılavuzu Allah üstlenir, baştaki deveden en arkadaki yolcuya kadar bütün dizi de O'nundur. Kur'an böyle bir gece yürüyüşünü Lut'a gönderilen elçilerin ağzından anlatır: {ar:فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ وَٱتَّبِعْ أَدْبَٰرَهُمْ وَلَا يَلْتَفِتْ مِنكُمْ أَحَدٌۭ, tr:fe-esri bi-ehlike bi-kıt'ın mine'l-leyli ve't-tebi' edbârahüm ve lâ yeltefit minküm ehad, gloss:gecenin bir bölümünde ailenle yola çık; onların arkasından yürü; hiçbiriniz arkasına dönüp bakmasın, source:15:65}. Lut dizinin en arkasında yürür ve kimse dönüp bakmaz. Surenin yalanlayanı ise bir sonraki bölümde görüleceği gibi, tam da arkasına bakan hayvanın fiilini taşır.

Kaynaklar: 92:1 ٱلَّيْلِ ل ي ل B002; 92:2 ٱلنَّهَارِ ن ه ر B002; 92:12 لَلْهُدَىٰ ه د ي B001; 92:12 لَلْهُدَىٰ ه د ي B003; 92:13 لَلْءَاخِرَةَ ء خ ر B001; 92:13 لَلْءَاخِرَةَ ء خ ر B003; 92:13 وَٱلْأُولَىٰ ء و ل B001; 92:14 نَارًۭا ن و ر B001; 92:14 نَارًۭا ن و ر B003; 92:14 نَارًۭا ن و ر B005; 92:20 وَجْهِ و ج ه B002

## Buluşmalar

Görüntülerin en sık birleştiği yer, uçurum ile elin aynı sahnede durmasıdır. Cennet ehlinden biri dünyadaki arkadaşını anlatır. Arkadaşı ona alay ederek şöyle sormuştur: {ar:يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ, tr:yekûlü einneke le-mine'l-musaddikîn, gloss:sen de mi doğrulayanlardansın derdi, source:37:52}. Sonra adam aşağı bakar ve arkadaşını ateşin ortasında görür: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:eğilip baktı ve onu cehennemin ortasında gördü, source:37:55}. Ona şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Ardından ekler: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Bu sahnede doğrulama, yuvarlanma, yüksekten bakış ve bir nimet bir aradadır. Surenin on dokuzuncu ayeti verenin yanında kimsenin bir nimeti olmadığını söyler. Cennet ehli ise kurtuluşunu tek bir nimete, Rabbinin nimetine bağlar. İnsanlar arasında karşılığı ödenecek bir el yoktur, ama Rabbin eli her şeyi taşır. Bir başka ayet aynı birleşmeyi müminlere hatırlatma olarak kurar: Allah'ın nimetiyle kardeş olmuşlardır ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Ayet {ar:لَعَلَّكُمْ تَهْتَدُونَ, tr:leallekum tehtedûn, gloss:doğru yolu bulasınız diye, source:3:103} diye kapanır. Kuyunun kenarı, nimet ve yol gösterme tek ayettedir. Kenara çekilen, uyarı ateşini işaret ateşi olarak okuyandır.

İkinci büyük buluşma bir sarayda geçer. Musa ile Harun'a Firavun'a ne diyecekleri öğretilir: {ar:وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ, tr:ve's-selâmü alâ meni't-tebea'l-hüdâ, gloss:esenlik yol göstericiye uyanadır, source:20:47}. Ardından {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48} gelir. Firavun {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbükümâ yâ mûsâ, gloss:ey Musa, sizin Rabbiniz kim dedi, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:kâle rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını verip sonra yol gösterendir dedi, source:20:50}. Bu cevapta surenin üç fiili aynı cümlededir: üçüncü ayetin yaratması, beşinci ayetin vermesi ve on ikinci ayetin yol göstermesi. Bir ayet önce de on altıncı ayetin iki fiili geçmiştir. Aynı Firavun başka bir surede yüceliği kendine mal eder: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Elin, yolun, yüz çevirmenin, yüceliğin ve mülkün görüntüleri burada tek bir karşılaşmada birleşir. Veren Rab ile tutan kral karşı karşıya gelir. Yüceliği iddia eden kral, surenin "son da ilk de bizimdir" sözüyle düşürülür.

Yüz ile elin buluşması iyiliğin tanımında görülür. İyilik yüzü doğuya ya da batıya çevirmek değildir: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tüvellû vucûheküm kıbele'l-meşriki ve'l-mağrib, gloss:iyilik yüzlerinizi doğu ve batı yönüne çevirmeniz değildir, source:2:177}. Aynı ayet iyiliği şöyle sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı sevmesine rağmen verdi, source:2:177}. Malın gittiği yerler arasında {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:boyunları çözmek için, source:2:177} de vardır. Ayet şöyle biter: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ, tr:ülâike'llezîne sadakû ve ülâike hümü'l-müttekûn, gloss:işte doğru olanlar onlardır ve sakınanlar da onlardır, source:2:177}. Yüzü çevirmek, malı vermek, boyun çözmek, hücumu sonuna kadar götüren doğruluk ve siper olan sakınma tek ayette bir araya gelir. Yüz çevirmek iyiliğin kendisi değildir, iyilik eldedir. Ama surenin yirminci ayeti eli tekrar yüze bağlar: veren el, aranan yüz için uzanır. Aynı bağ yoksulları doyuranların sözünde görülür: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Sözün sonunda {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfü min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık suratlı, çetin bir günden korkarız, source:76:10} derler. Sonra {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11} gelir. El, yüz, karşılığın reddi ve siper bu ayetlerde surenin sırasıyla dizilir. Bunun tam tersi de bir sahne olarak anlatılır. Bir adam Allah'a söz vermiştir: {ar:لَئِنْ ءَاتَىٰنَا مِن فَضْلِهِۦ لَنَصَّدَّقَنَّ, tr:lein âtânâ min fadlihî le-nessaddakanne, gloss:bize lütfundan verirse mutlaka sadaka vereceğiz, source:9:75}. Sonra şu olur: {ar:فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ, tr:fe-lemmâ âtâhüm min fadlihî bahılû bihî ve tevellev ve hüm mu'ridûn, gloss:lütfundan verince cimrilik ettiler ve yüz çevirdiler; zaten dönüp gidiyorlardı, source:9:76}. Sıkan el ile dönülen sırt aynı kişidedir. Sekizinci ve on altıncı ayetler tek bir hikâyede birleşir.

Büyüme ile yükseklik, yüksekteki bahçede buluşur. Allah'ın hoşnutluğunu arayarak harcayanların durumu {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilün fe-âtet ükulehâ dı'feyn, gloss:yüksekçe bir yerdeki bahçe gibidir; ona sağanak isabet eder ve ürününü iki kat verir, source:2:265} diye anlatılır. Bu bahçe kuyunun tam karşıtıdır. Aşağıda değil yüksektedir. Yağmur onu süpürmez, büyütür. Verme fiili de bahçenin kendi fiilidir. Aynı yükseklik ateşe dönük bir eğiklikle karşılaşır: Bir yanda takva ve hoşnutluk üzerine kurulmuş yapı, öbür yanda {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına kurulmuş, onunla birlikte cehennem ateşine yıkılmış yapı, source:9:109} vardır. Biri takva ve hoşnutluk üzerine kurulur, öteki çöküp ateşe düşer. Cimrinin malı da düştüğü yerde onun yanına yapışır: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün onlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Sakınanın yanında bir kalkan durur ve o yanından kötülükten uzak tutulur. Biriktirenin yanı ise biriktirdiğiyle dağlanır. Sırtı da yüz çevirdiği için dönmüş olan sırttır.

Musa'nın ateşi ise işaret ateşi ile yakan ateşi bir arada tutar. Musa ailesine {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Başka bir anlatımda {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7} der. Isınmak on beşinci ayetin yanmasıyla aynı köktendir. Yanına yaklaşılan ateş ısıtır ve yol gösterir. İçine girilen ateş ise yakar. Surenin hareketi bu iki mesafe arasında kurulur. İlk iki ayette gece serilir ve gün yarılır. Gece insanların koşusunu örter, gün o koşunun dağıldığını gösterir. Yol ayrılır ve her yol yürüyenine göre düzlenir. Biri verir, siper kurar ve vaadi kendi eliyle doğrular. Öteki malını tutar, ona cübbe gibi bürünür ve vaadi yalanlayıp sırtını döner. Sonra gece yolunda bir ateş yakılır ve bir ses "uyardım" der. Uyarıyı işaret olarak okuyan, dizgini tutulan bir binek gibi kenara çekilir. Yüzü kendisine bir nimet borcu olanlara değil, yüceliğe dönüktür. Uyarıyı duymayan, yuvarlandığı anda elindeki malın ona yetmediğini görür ve ateşin içine girer. Surenin son kelimesi, kayıp devesini arayan adamın onu bulduğu anın kelimesidir: hoşnutluk. Bu hoşnutluk, ilk ayetteki gecenin örtüsünden sonra gelen yüzün açılmasıdır.

