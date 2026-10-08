Focus: 89:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_3/D.r13/context.md =====
# 89:3 — focus

وَٱلشَّفْعِ وَٱلْوَتْرِ

Anchor translation (canonical reading, reference only):

Çifte ve teke andolsun!

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلشَّفْعِ | شَّفْع | ش ف ع | CONJ;DET;N |
| 2 | وَٱلْوَتْرِ | وَتْر | و ت ر | CONJ;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 89 — full text (context; no pericope)

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 ◀ focus وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ف ع (root_000802) — identity root of وَٱلشَّفْعِ (w1)

- **B001** benzerini ekleyerek çiftleştirme — çift olan veya bir benzeri eklenerek çift yapılmış şey · tek olana bir benzerini ekleyip çift yapmak · kuşluk namazının iki bölümü
  الشفع خلاف الوتر (maqayis;sihah)؛ الشفع ما كان من العدد أزواجا (ayn)؛ الشفع الزيادة (tahdhib)؛ ضم الشيء إلى مثله (mufradat)؛ شفعة الضحى ركعتا الضحى (tahdhib)
- **B002** başkası adına aracılık edip destek olma — başkası adına aracılık etme ve ona destek olma · başkası adına istekte bulunan aracı · birinin işi için aracılık eden destekçi · birini aracı kılıp yardımını istemek · birinin işi için başkasına aracılık etmek · aracılığını kabul edip isteğini yerine getirmek · iyi ya da kötü bir işte birine katılıp onu güçlendirmek · düşmanlıkta birine karşı yardım etmek veya ona karşı koymak
  شفع فلان لفلان إذا جاء ثانية ملتمسا مطلبه ومعينا له (maqayis)؛ الشافع الطالب لغيره (ayn;tahdhib)؛ الشفاعة كلام الشفيع للملك في حاجة يسألها لغيره (tahdhib)؛ الانضمام إلى آخر ناصرا له وسائلا عنه (mufradat)؛ يشفع لي بالعداوة أي يعين علي (maqayis)؛ يشفع لي بعداوة أي يضادني (tahdhib)
- **B003** taşınmaz satışında öncelikli alım hakkı — ev veya arazi satışında öncelikli alım hakkı · öncelikli alım hakkını isteyen kişi · satılanı öncelikle alma yetkisini ona vermek
  الشفعة في الدار (maqayis)؛ الشفعة في الدار والأرض (sihah)؛ الشفعة الزيادة حتى تضمه إلى ما عندك (tahdhib)؛ فشفعه وجعله أولى ممن بعد سببه (tahdhib)
- **B004** yavrulu koyun veya iki yavru durumundaki dişi deve — yavrusu yanında bulunan koyun · karnında yavru taşıyan veya ardından başka yavrusu gelen dişi deve
  الشاة الشافع التي معها ولدها (maqayis)؛ ناقة شافع في بطنها ولد ويتبعها آخر (sihah)؛ الشافع التي معها ولدها (tahdhib)؛ ناقة شافع إذا كان في بطنها ولد يتلوها آخر (tahdhib)
- **B005** tek sağımda iki kap dolduran dişi deve — tek sağımda iki kap dolduracak süt veren dişi deve
  ناقة شفوع وهي التي تجمع بين محلبين في حلبة واحدة (maqayis;sihah)؛ ناقة شفوع تجمع بين محلبين في حلبة (tahdhib)
- **B006** tek nesneyi çift görme — tek nesneyi çift gören göz · bir kişiyi iki kişi gibi gösteren görme bozukluğu
  عين شافعة تنظر نظرين (tahdhib)؛ أرى الشخص الواحد شخصين لضعف بصري (tahdhib)

## و ت ر (root_001621) — identity root of وَٱلْوَتْرِ (w2)

- **B001** tek sayı ve tekleştirme — tek sayı; çiftin karşıtı · tek kılmak veya tek sayıya çevirmek · gece ibadetini tek sayıda bitirmek · temizlenirken tek sayıda taş kullanmak
  الوتر والوتر الفرد (maqayis)؛ الوتر الفرد ضد الشفع (jamhara)؛ الوتر بالكسر الفرد (sihah)؛ الوتر في العدد ولغتا وتر ووتر وأوتر صلاته (tahdhib)؛ الوتر في العدد خلاف الشفع وأوتر في الصلاة (mufradat)
- **B002** öç gerektiren karşılıksız ağır zarar — öç alınmasını gerektiren ağır zarar · öç gerektiren suç veya zarar · birini ağır zarara uğratıp öç ister duruma getirmek · öcünü henüz alamamış mağdur · alınması beklenen öçler ve karşılıksız kalmış zararlar
  الوتر الذحل (maqayis)؛ الوتر الترة... قتلت له ولدا أو قريبا (jamhara)؛ الوتر بالفتح الذحل والموتور الذي قتل له قتيل (sihah)؛ الأوتار والذحول... قتل له قتيلا أو أخذت له مالا (tahdhib)؛ الوتر والترة الذحل وقد وترته إذا أصبته بمكروه (mufradat)
- **B003** hakkını veya karşılığını eksiltmek [kalıp] — hakkını eksiltmek veya elinden almak · işlerinizi veya karşılığını eksiltmeyecek
  وتره حقه أي نقصه وقوله ولن يتركم أعمالكم أي لن يتنقصكم (sihah)؛ وتر أهله وماله أي نقص أهله وماله... لن ينقصكم من ثوابكم شيئا (tahdhib)
- **B004** aralıklı tek tek ardışıklık — aralarında süre bulunan tek tek ardışıklık · birer birer peş peşe gelme · aralıklı olarak birbiri ardından · çökerken uzuvlarını bekleyerek sırayla yere koyan dişi deve · haberleri veya yazıları kısa aralarla peş peşe göndermek · bir veya iki gün tutup aynı süre ara vererek oruç tutmak
  لا تكون مواترة إلا إذا وقعت بينهما فترة (maqayis)؛ المواترة المتابعة... وقعت بينهم فترة... تترى من الوتر أي واحدا بعد واحد (sihah)؛ واترت الخبر أتبعت بعضه بعضا وبين الخبرين هنيهة... تترى متقطعة متفاوتة الأوقات (tahdhib)؛ التواتر تتابع الشيء وترا وفرادى وجاءوا تترى (mufradat)
- **B005** değişmeyen düzen ve süreklilik — değişmeyen yol, süreklilik ve yerleşik huy · aynı yöntem ve doğrultuda değişmeden
  الوتيرة المداومة على الشيء (maqayis)؛ على وتيرة من أمره أي على طريقة واحدة واستقامة (jamhara)؛ الوتيرة الطريقة... على وتيرة واحدة (sihah)؛ على وتيرة واحدة... المداومة على الشيء (tahdhib)؛ الوتيرة السجية من التواتر (mufradat)
- **B006** işte veya gidişte duraksama — işten veya gidişten geri kalma, duraksama · hiç gevşeme veya duraksama yok
  الوتيرة أيضا الفترة... سير ليست فيه وتيرة أي فتور (sihah)؛ الوتيرة في غير هذا الفترة عن الشيء والعمل (tahdhib)
- **B007** yay kirişi ve yayı kirişleme [kalıp] — yay kirişi · yaya kiriş takıp germek
  وتر القوس معروف... وترتها وأوترتها (maqayis)؛ الوتر وتر القوس معروف (jamhara)؛ الوتر بالتحريك واحد أوتار القوس... أوتر قوسه ووترها (sihah)؛ أوتار القسي... قلدوا الخيل ولا تقلدوها الأوتار (tahdhib)
- **B008** halka hedef ve benzeri yuvarlak iz — saplama veya atış çalışması için halka biçimli hedef · halkaya benzetilen yuvarlak alın lekesi, yara veya çiçek
  الوتيرة غرة الفرس مستديرة وشيء يتعلم عليه الطعن (maqayis)؛ الوتيرة حلقة يتعلم عليها الطعن... قرحة الفرس... الوردة البيضاء (jamhara)؛ الوتيرة حلقة من عقب يتعلم فيها الطعن (sihah)؛ غرة الفرس إذا كانت مستديرة... الحلقة التي يتعلم عليها الطعن... الوردة البيضاء والوردة الصغيرة (tahdhib)؛ الحلقة التي يتعلم عليها الرمي الوتيرة (mufradat)
- **B009** burun bölmesi ve benzeri ince ayırıcı — burun delikleri arasındaki bölme veya burun ucu · iki yeri ayıran ince deri, kıkırdak veya kenar
  الوترة طرف الأنف (maqayis)؛ الوترة الحائلة بين المنخرين في الأنف (jamhara)؛ وترة الأنف حجاب ما بين المنخرين... وترة كل شيء حتاره (sihah)؛ الوترة جليدة بين الإبهام والسبابة... الحاجز بين المنخرين... غريضيف في جوف الأذن... حتار كل شيء وتره (tahdhib)؛ الوتيرة الحاجز بين المنخرين (mufradat)
- **B010** uzun arazi şeridi ve doğrusal sıra — uzunlamasına uzanan toprak parçası veya yol · aynı çizgi üzerinde uzanan sıra
  الوتيرة قطعة تغلظ وتستحق من الأرض وتستطيل... على وتيرة أي على سطر (jamhara)؛ الوتيرة من الأرض الطريقة (sihah)؛ الوتيرة من الأرض ولم يحدها (tahdhib)؛ الأرض المنقادة (mufradat)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:3, and ## Buluşmalar) =====
## Çift, tek ve eşi olmayan

Üçüncü ayet sayıyla yemin eder: {ar:وَٱلشَّفْعِ وَٱلْوَتْرِ, tr:ve'ş-şef'i ve'l-vetr, gloss:çifte ve teke, source:89:3}. Çift, bir şeye benzerinin eklenmesiyle oluşur: {ar:ضم الشيء إلى مثله, tr:dammu'ş-şey'i ilâ mislih, gloss:bir şeyi benzerine katmak, source:"ش ف ع,B001"}. Tek ise yanına benzeri katılmamış olandır: {ar:الوتر الفرد ضد الشفع, tr:el-vetru'l-ferdu diddu'ş-şef', gloss:vetr, çiftin zıddı olan tektir, source:"و ت ر,B001"}. Bu katma işinin insanlar arasındaki biçimi de aynı kökle söylenir: {ar:الانضمام إلى آخر ناصرا له وسائلا عنه, tr:el-indimâmu ilâ âharin nâsıran lehû ve sâilen anh, gloss:birinin yanına geçip ona arka çıkmak ve onun için istemek, source:"ش ف ع,B002"}. Çift, bir şeyin yalnız bırakılmamasıdır.

Çiftin tanımındaki "benzer" kelimesi sekizinci ayette karşımıza çıkar: {ar:لَمْ يُخْلَقْ مِثْلُهَا, tr:lem yuhlak misluhâ, gloss:benzeri yaratılmadı, source:89:8}. Misl, karşılıktır: {ar:المثل النظير, tr:el-mislu'n-nazîr, gloss:misl, dengidir, source:"م ث ل,B001"}. İrem ülkeler içinde tek kalmış bir yapıdır, yanına benzeri katılmamıştır. Bu teklik bir övünç olarak anılır, ama Kur'an gerçek tekliği yalnız Allah'a verir: {ar:لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ, tr:leyse ke-mislihî şey', gloss:O'nun benzeri gibi hiçbir şey yoktur, source:42:11}, {ar:قُلْ هُوَ ٱللَّهُ أَحَدٌ, tr:kul huva'llâhu ehad, gloss:de ki: O Allah birdir, source:112:1}, {ar:وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ, tr:ve lem yekun lehû kufuven ehad, gloss:hiçbir şey O'na denk değildir, source:112:4}. Yaratılmışların düzeni ise çifttir: {ar:وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ, tr:ve min kulli şey'in halaknâ zevceyni leallekum tezekkerûn, gloss:her şeyden iki eş yarattık; belki düşünüp hatırlarsınız, source:51:49}.

On yedinci ayetteki yetim, insanlar arasında tek kalmış olandır: {ar:بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:bel lâ tukrimûne'l-yetîm, gloss:bilakis yetime ikram etmiyorsunuz, source:89:17}. Yetim kelimesi tekliği de anlatır: {ar:كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة, tr:kullu şey'in mufredin yeizzu nazîruhû fe-huve yetîm, ve durretun yetîme, gloss:dengi zor bulunan her tek şey yetimdir; eşsiz inciye de "yetim inci" denir, source:"ي ت م,B002"}. Ayette anlam babasız çocuktur. Yanında yanına kimse katılmamış teklik duyulur. Yetime ikram etmek, onun yanına geçip arka çıkmaktır, yani şef'in ikinci anlamıdır. Muhatapların yapmadığı şey tam olarak budur. Kur'an kıyamet gününde bu katılmanın kalmayacağını gösterir. Herkes tek gelir: {ar:وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا, tr:ve kulluhum âtîhi yevme'l-kıyâmeti ferdâ, gloss:hepsi kıyamet günü O'na tek başına gelir, source:19:95}. İnkârcılara şöyle denir: {ar:وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۢ, tr:ve lekad ci'tumûnâ furâdâ kemâ halaknâkum evvele merra, gloss:sizi ilk defa yarattığımız gibi bize teker teker geldiniz, source:6:94}. Aynı ayette yanlarına geçeceğini sandıkları kimse de görünmez: {ar:وَمَا نَرَىٰ مَعَكُمْ شُفَعَآءَكُمُ, tr:ve mâ nerâ meakum şufeâekum, gloss:yanınızda şefaatçilerinizi görmüyoruz, source:6:94}. Bir başka ayet de şöyle der: {ar:فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ, tr:fe-mâ tenfeuhum şefâatu'ş-şâfiîn, gloss:şefaatçilerin şefaati onlara fayda vermez, source:74:48}. Yetimin yanına geçmeyen, kendisi tek kalır.

Yirmi beşinci ve yirmi altıncı ayetler aynı sayımı azaba uygular: {ar:لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:lâ yuazzibu azâbehû ehad, gloss:hiç kimse O'nun azabı gibi azap edemez, source:89:25}, {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:hiç kimse O'nun bağlaması gibi bağlayamaz, source:89:26}. Olumsuz cümledeki ehad bir türün bütününü kapsar: {ar:أحد في النفي لاستغراق جنس الناطقين, tr:ehadun fi'n-nefyi li-istiğrâki cinsi'n-nâtıkîn, gloss:olumsuz cümlede ehad, konuşan varlıkların tamamını kapsar, source:"ء ح د,B002"}. Ne bir kişi ne iki kişi: bu azabın dengi yoktur. İrem'in benzersizliği yapılmış bir şeyin benzersizliğiydi. Buradaki benzersizlik yapanın kendisine aittir.

Bu tekliklerin karşısında sure kelimelerini çiftler: {ar:دَكًّۭا دَكًّۭا, tr:dekken dekkâ, gloss:dövüldükçe dövülerek, source:89:21}, {ar:صَفًّۭا صَفًّۭا, tr:saffen saffâ, gloss:saf saf, source:89:22}. Her birimin ardından benzeri gelir. Yirmi sekizinci ayette rıza da çifttir: {ar:رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak, source:89:28}. Bu sözün yanında iki taraf arasındaki karşılıklı hoşnutluk duyulur: {ar:المراضاة من اثنين, tr:el-murâdât mine'sneyn, gloss:karşılıklı razı olmak iki taraf arasında olur, source:"ر ض و,B003"}. Kur'an bu karşılıklılığı açıkça söyler: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhu anhum ve radû anh, gloss:Allah onlardan razı oldu, onlar da O'ndan razı oldular, source:98:8}. Allah'ın doğruların doğruluğunun fayda verdiği gün olarak tanıttığı günde de aynı söz geçer {source:5:119}. Sonra tek başına seslenilen can bir topluluğa katılır: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Bu katılma şöyle açıklanır: {ar:فادخلي في عبادي أي في حزبي, tr:fedhulî fî ibâdî ey fî hizbî, gloss:kullarımın arasına, yani benim topluluğuma gir, source:"ع ب د,B002"}. Surenin başında soyut bir sayı olan tek ile çift, sonunda yanına kimse katılmayan yetim ile topluluğa katılan can arasındaki farka dönüşür.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B001; 89:3 ٱلشَّفْعِ ش ف ع B002; 89:3 ٱلْوَتْرِ و ت ر B001; 89:8 مِثْلُهَا م ث ل B001; 89:17 ٱلْيَتِيمَ ي ت م B002; 89:25 أَحَدٌۭ ء ح د B002; 89:26 أَحَدٌۭ ء ح د B002; 89:28 رَاضِيَةًۭ مَّرْضِيَّةًۭ ر ض و B003; 89:29 عِبَٰدِى ع ب د B002

## Gözetleme yeri ve bakan göz

Altıncı ayet dinleyenin gözünü olup bitene çevirir: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:e-lem tera keyfe feale rabbuke bi-Âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Görmek, gözle ya da kalple bakmaktır: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakıp görmek, source:"ر ء ي,B001"}. Aynı kalıp Fil sahiplerinin akıbetini anlatırken de kullanılır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ, tr:e-lem tera keyfe feale rabbuke bi-ashâbi'l-fîl, gloss:Rabbinin fil sahiplerine ne yaptığını görmedin mi, source:105:1}. Dinleyen, bir olayın gözlemcisi yapılır.

Gözlenen şey yolda olan insanlardır. Dördüncü ayetin fiili gece yürüyenleri de adlandırır: {ar:السارية للقوم الذين يسرون بالليل, tr:es-sâriye li'l-kavmi'llezîne yesrûne bi'l-leyl, gloss:sâriye, gece yol alan topluluktur, source:"س ر ي,B001"}. Dokuzuncu ayetteki fiilin yanında ülkeleri boydan boya geçmek duyulur: {ar:جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها, tr:cubtu'l-bilâde ecûbuhâ ve ecîbuhâ ve'ctebtuhâ izâ kata'tuhâ, gloss:ülkeleri boydan boya geçtim, source:"ج و ب,B002"}. On birinci ayette bu yolcular ülkelerde sınırı aşar: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı geçmek, source:"ط غ ي,B001"}. Ayetlerin anlamı kazmak ve azmaktır. Yanında yol alan, ülke aşan ve sınırı geçen yolcular duyulur.

On dördüncü ayet yolun üzerindeki yeri adlandırır: {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin elbette gözetleme yerindedir, source:89:14}. Mirsâd hem yolun kendisidir, {ar:المرصاد الطريق, tr:el-mirsâd et-tarîk, gloss:mirsâd yoldur, source:"ر ص د,B003"}, hem de gözcünün beklediği yer: {ar:المرصاد المكان الذي يرصد به الراصد, tr:el-mirsâdu'l-mekânu'llezî yersudu bihi'r-râsıd, gloss:mirsâd, gözcünün gözetlediği yerdir, source:"ر ص د,B003"}. Gözcü bir şeyi kollayan kişidir: {ar:الراصد للشئ المراقب له, tr:er-râsıdu li'ş-şey'i el-murâkıbu leh, gloss:râsıd, bir şeyi gözetleyendir, source:"ر ص د,B001"}. Aynı kök yolda pusu kuran yılana da ad verir: {ar:يقال للحية التي ترصد المارة على الطريق رصيد, tr:yukâlu li'l-hayyeti'lletî tersudu'l-mârrate ale't-tarîki rasîd, gloss:yolda geçenleri kollayan yılana rasîd denir, source:"ر ص د,B001"}. Bu düzenin işleyişi şöyledir: gözcü kimseyi kovalamaz, yolun geçtiği yerde bekler. Her yolcu oradan geçmek zorundadır. Bir önceki ayetteki dökme fiili bu yılanın hareketini de anlatır: {ar:صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق, tr:sabbeti'l-hayyetu aleyhi izertefeat fensabbet aleyhi min fevk, gloss:yılan kalkıp yukarıdan üstüne çullandı, source:"ص ب ب,B008"}. Surenin sıralaması da bu düzene uyar. Önce darbe iner, gözetleme yeri ancak sonra adlandırılır. Yolcular gözcünün varlığını vuruldukları anda öğrenir.

Kur'an aynı yeri başka sahnelerde de kurar. Kıyamet anlatılırken cehennem için {ar:إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا, tr:inne cehenneme kânet mirsâdâ, gloss:cehennem bir gözetleme yeridir, source:78:21} denir. Antlaşmayı bozanlara karşı verilen emir şöyledir: {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehum kulle marsad, gloss:onlar için her gözetleme yerinde oturun, source:9:5}. İblis de Allah'a şöyle der: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ek'udenne lehum sırâtake'l-mustekîm, gloss:onlar için senin dosdoğru yolunun üstünde oturacağım, source:7:16}. Şuayb kavmine yollarda pusu kurmamalarını söyler: {ar:وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ, tr:ve lâ tak'udû bi-kulli sırâtin tûidûn, gloss:tehdit ederek her yolun başında oturmayın, source:7:86}. Cinler gökte kendilerini bekleyen bir alev bulur: {ar:يَجِدْ لَهُۥ شِهَابًۭا رَّصَدًۭا, tr:yecid lehû şihâben rasadâ, gloss:kendisini gözetleyen bir alev bulur, source:72:9}. Allah elçisinin önüne ve arkasına gözcüler koyar {source:72:27}. İnsanın söylediği her sözün yanında da hazır bir gözcü vardır: {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözcü vardır, source:50:18}.

Bakmanın bir de insanın içindeki yüzü vardır. On beşinci ve yirmi üçüncü ayetlerdeki "insan" kelimesi göz bebeğindeki küçük sureti de adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, gözbebeğinin karasında görünen küçük surettir, source:"ء ن س,B005"}. Bu tanımda misal ve görmek kelimeleri birlikte geçer. Sekizinci ayetin kökü sureti, {ar:التمثال الصورة, tr:et-timsâl es-sûra, gloss:timsal, surettir, source:"م ث ل,B008"}, ve görülerek alınan dersi de adlandırır: {ar:يكون المثل بمعنى العبرة, tr:yekûnu'l-meselu bi-ma'ne'l-ibra, gloss:mesel, ibret anlamına da gelir, source:"م ث ل,B011"}. Beşinci ayetin hicr kökü gözün çevresine de ad verir: {ar:ومحجر العين ما يدور بها, tr:ve mahcaru'l-ayni mâ yedûru bihâ, gloss:gözün mahceri, onu çevreleyen yerdir, source:"ح ج ر,B006"}. Üçüncü ayetteki çift kelimesi de bir tek şeyi iki gören gözü adlandırır: {ar:عين شافعة تنظر نظرين, tr:aynun şâfiatun tenzuru nazarayn, gloss:şâfia göz, iki bakışla bakan gözdür, source:"ش ف ع,B006"}. Sure insana Âd'ı, Semûd'u ve Firavun'u göstermiştir. İnsan ise hemen ardından kendi hâline bakar ve tek bir sınavı iki ayrı hüküm olarak okur: bolluğa ikram, darlığa aşağılanma der. Kur'an bu bakışın kendini nasıl gördüğünü söyler {source:96:7}. Âd'a da kulaklar, gözler ve gönüller verilmişti, ama onlara bir yararı olmadı: {ar:فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ, tr:fe-mâ ağnâ anhum sem'uhum ve lâ ebsâruhum, gloss:ne kulakları ne gözleri onlara bir yarar sağladı, source:46:26}. Kıyamet günü örtü kalkar: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık, bugün gözün keskindir, source:50:22}.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B006; 89:4 يَسْرِ س ر ي B001; 89:5 حِجْرٍ ح ج ر B006; 89:6 تَرَ ر ء ي B001; 89:8 مِثْلُهَا م ث ل B008; 89:8 مِثْلُهَا م ث ل B011; 89:9 جَابُوا۟ ج و ب B002; 89:11 طَغَوْا۟ ط غ ي B001; 89:13 فَصَبَّ ص ب ب B008; 89:14 لَبِٱلْمِرْصَادِ ر ص د B001; 89:14 لَبِٱلْمِرْصَادِ ر ص د B003; 89:15 ٱلْإِنسَٰنُ ء ن س B005

## Kan, yemin ve karşılık

Surenin birkaç kelimesi bir kan davasının araçlarını taşır. Bu bir aile imgesidir. Surenin kendisi bir cinayet anlatmaz. Beşinci ayetteki kasem kelimesinin kökü öldürülmüş birinin yakınları arasında paylaştırılan yeminlere dayanır: {ar:اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول, tr:el-yemîn fe'l-kasem, ve aslu zâlike mine'l-kasâme, ve hiye'l-eymânu tuksemu alâ evliyâi'l-maktûl, gloss:yemine kasem denir; aslı kasâmedir, yani maktulün velileri arasında paylaştırılan yeminler, source:"ق س م,B004"}. Sahnede bir kişi öldürülmüştür ve yakınları hakkı aramak için yemini aralarında bölüşür. Üçüncü ayetteki vetr kelimesinin yanında ödenmemiş kan duyulur: {ar:الوتر الذحل, tr:el-vetru'z-zahl, gloss:vetr, alınmamış kan öcüdür, source:"و ت ر,B002"}, {ar:الموتور الذي قتل له قتيل, tr:el-mevtûru'llezî kutile lehû katîl, gloss:mevtûr, yakını öldürülmüş kişidir, source:"و ت ر,B002"}. Aynı kök hakkı eksiltmeyi de anlatır: {ar:وتره حقه أي نقصه, tr:veterahû hakkahû ey nekasah, gloss:hakkını eksiltti, source:"و ت ر,B003"}. Kur'an bu fiili Allah'ın kullara davranışı için kullanır: {ar:وَلَن يَتِرَكُمْ أَعْمَٰلَكُمْ, tr:ve len yetirakum a'mâlekum, gloss:amellerinizden hiçbir şeyi eksiltmeyecektir, source:47:35}. Dokuzuncu ayetteki vadi kelimesinin kökü diyeti de adlandırır: {ar:وديت القتيل أديه دية إذا أعطيت ديته, tr:vedeytu'l-katîle edîhi diyeten izâ a'taytu diyeteh, gloss:maktulün diyetini verdim, source:"و د ي,B002"}. Kur'an diyeti yanlışlıkla öldürme hükmünde anar: {ar:وَدِيَةٌۭ مُّسَلَّمَةٌ إِلَىٰٓ أَهْلِهِۦٓ, tr:ve diyetun musellemetun ilâ ehlih, gloss:ailesine teslim edilecek bir diyet, source:4:92}.

Sekizinci ayetteki misl kelimesinin kökü ibret olsun diye verilen cezayı da adlandırır: {ar:نقمة تنزل بالإنسان فيجعل مثالا يرتدع به غيره, tr:nikmetun tenzilu bi'l-insâni fe-yuc'alu misâlen yerteduu bihî ğayruh, gloss:insanın başına inen ve başkalarının ondan çekinmesi için örnek yapılan ceza, source:"م ث ل,B002"}. Kur'an inkârcıların iyilikten önce kötülüğü acele istediklerini söyler ve onlardan önce bu örnek cezaların geçtiğini hatırlatır: {ar:وَقَدْ خَلَتْ مِن قَبْلِهِمُ ٱلْمَثُلَٰتُ, tr:ve kad halet min kablihimu'l-mesulât, gloss:onlardan önce ibret olacak cezalar gelip geçti, source:13:6}. Âd, Semûd ve Firavun bu örneklerdir. On dördüncü ayetteki mirsâd kelimesi de karşılığın hazırda tutulmasını anlatır: {ar:أنا لك مرصد بإحسانك حتى أكافئك به, tr:ene leke mursıdun bi-ihsânike hattâ ukâfieke bih, gloss:iyiliğini sana karşılık verene kadar hazırda tutarım, source:"ر ص د,B002"}, {ar:وإرصاد الانسان في المكافأة والخير, tr:ve irsâdu'l-insâni fi'l-mukâfeeti ve'l-hayr, gloss:irsâd, karşılık ve iyilik için de kullanılır, source:"ر ص د,B002"}. Gözcünün beklediği şey bir hesaptır. Karşılık kaybolmaz, yerinde durur.

Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında da kısasın verdiği hayat duyulur: {ar:ولكم في القصاص حياة أي يرتدع بالقصاص, tr:ve lekum fi'l-kısâsı hayâtun ey yurtedeu bi'l-kısâs, gloss:kısasta sizin için hayat vardır, yani insanlar kısas sayesinde kötülükten geri durur, source:"ح ي ي,B013"}. Kur'an'daki hüküm şöyledir: {ar:كُتِبَ عَلَيْكُمُ ٱلْقِصَاصُ فِى ٱلْقَتْلَى, tr:kutibe aleykumu'l-kısâsu fi'l-katlâ, gloss:öldürülenler hakkında size kısas yazıldı, source:2:178}, {ar:وَلَكُمْ فِى ٱلْقِصَاصِ حَيَوٰةٌۭ يَٰٓأُو۟لِى ٱلْأَلْبَٰبِ, tr:ve lekum fi'l-kısâsı hayâtun yâ uli'l-elbâb, gloss:ey akıl sahipleri, kısasta sizin için hayat vardır, source:2:179}. Haksız yere öldürülenin velisine yetki verilir, ama öldürmede aşırı gitmesi yasaklanır {source:17:33}. Bu hükümler akıl sahiplerine söylenir, sure de yeminini akıl sahibine yöneltmişti. Surenin dizisinde bu imge şöyle ilerler: önce yemin, sonra ibret olan kavimler, sonra karşılığı hazırda tutan Rab. Son olarak yirmi beşinci ayet hiçbir insan velinin yerine getiremeyeceği bir karşılığı haber verir.

Kaynaklar: 89:3 ٱلْوَتْرِ و ت ر B002; 89:3 ٱلْوَتْرِ و ت ر B003; 89:5 قَسَمٌۭ ق س م B004; 89:8 مِثْلُهَا م ث ل B002; 89:9 بِٱلْوَادِ و د ي B002; 89:14 لَبِٱلْمِرْصَادِ ر ص د B002; 89:24 لِحَيَاتِى ح ي ي B013

## Saf saf gelenler

Yer dövülüp düzlendikten sonra bir topluluk gelir: {ar:وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا, tr:ve câe rabbuke ve'l-meleku saffen saffâ, gloss:Rabbin ve melekler saf saf geldiğinde, source:89:22}. Gelmek (mecî') genel bir fiildir: {ar:المجيء كالإتيان لكن المجيء أعم, tr:el-mecîu ke'l-ityân, lâkinne'l-mecîe a'amm, gloss:mecî' gelmek gibidir, ama ondan daha geniştir, source:"ج ي ء,B001"}. Melek kelimesi burada tekildir, ama bütün sınıfı kapsar: {ar:الملك من الملائكة واحد وجمع, tr:el-melek mine'l-melâike vâhidun ve cem', gloss:melek kelimesi hem tekil hem çoğul için kullanılır, source:"م ل ك,B009"}. Kur'an aynı tekili yerin ve dağların ezildiği sahnede de kullanır: {ar:وَٱلْمَلَكُ عَلَىٰٓ أَرْجَآئِهَا, tr:ve'l-meleku alâ ercâihâ, gloss:melekler de göğün kenarlarındadır, source:69:17}. Saf, bir şeyi düz bir çizgi üzerine dizmektir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın mustevin, gloss:saf, bir şeyi düz bir çizgi üzerine dizmektir, source:"ص ف ف,B001"}. Durulan yer de bu kökten adlandırılır: {ar:المصف الموقف, tr:el-masaff el-mevkıf, gloss:masaff, durulan yerdir, source:"ص ف ف,B001"}. Kelimenin tekrarı bir dağıtım kalıbıdır. Arapça gelme fiilini tekrarlanan bir sayıyla aynı biçimde kurar: {ar:جاء القوم عشار عشار ومعشر معشر أي عشرة عشرة, tr:câe'l-kavmu uşâra uşâr, ve ma'şera ma'şer, ey aşeraten aşera, gloss:topluluk onar onar geldi, source:"ع ش ر,B005"}. Ayetteki tekrar da aynı şeyi söyler: saf ardından saf gelir. İkinci ayetteki "on" kelimesinin kökü bu kalıbı önceden taşır.

Gelişin ritmi surenin önceki kelimelerinde de vardır. Üçüncü ayetteki tek kelimesinin kökünden birbiri ardınca gelmek anlamı türer: {ar:تترى من الوتر أي واحدا بعد واحد, tr:tetrâ mine'l-vetr, ey vâhiden ba'de vâhid, gloss:tetrâ vetr kökündendir, yani birbiri ardınca, source:"و ت ر,B004"}. Kur'an bu kelimeyi elçilerin ve onları yalanlayan ümmetlerin dizisi için kullanır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:summe erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}. Aynı ayette yalanlayan ümmetler de birbirinin ardınca yok edilip söz konusu edilen hikâyelere dönüştürülür. Surenin altıncı ve onuncu ayetleri arasında anılan kavimler de böyle bir dizi oluşturur. İlk kelimenin kökü de bir topluluğun ansızın üstüne gelişini anlatır: {ar:انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infeceret aleyhimu'd-devâhî izâ câehumu'l-kesîru minhâ bağteten, gloss:felaketler birdenbire ve çok sayıda gelince "üstlerine boşandı" denir, source:"ف ج ر,B003"}. Dövme fiili de kalabalığın bir şeye yüklenmesini anlatır: {ar:تداك عليه القوم إذا ازدحموا عليه, tr:tedâkke aleyhi'l-kavmu izezdehamû aleyh, gloss:insanlar onun üstüne üşüştü, source:"د ك ك,B008"}.

Yirmi üçüncü ayette cehennem getirilir: {ar:وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ, tr:ve cîe yevmeizin bi-cehennem, gloss:o gün cehennem getirildiğinde, source:89:23}. Bir şeyi getirmek onu hazır etmektir: {ar:وجاء بكذا: استحضره, tr:ve câe bi-kezâ: istahdarah, gloss:onu getirdi, yani hazır etti, source:"ج ي ء,B004"}. Uzakta sanılan şey göz önüne konur. Kur'an aynı edilgen fiili Sûr'dan sonraki sahnede kullanır: {ar:وَجِا۟ىٓءَ بِٱلنَّبِيِّۦنَ وَٱلشُّهَدَآءِ, tr:ve cîe bi'n-nebiyyîne ve'ş-şuhedâ', gloss:peygamberler ve şahitler getirildi, source:39:69}. Cehennemin ortaya çıkarılmasını da şöyle anlatır: {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِمَن يَرَىٰ, tr:ve burrizeti'l-cahîmu li-men yerâ, gloss:cehennem gören herkes için ortaya çıkarılır, source:79:36}, {ar:وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ, tr:ve burrizeti'l-cahîmu li'l-ğâvîn, gloss:cehennem azgınlara gösterilir, source:26:91}. Her can da yanında bir sürücü ve bir şahitle gelir: {ar:وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ, tr:ve câet kullu nefsin meahâ sâikun ve şehîd, gloss:her can yanında bir sürücü ve bir şahitle gelir, source:50:21}. Safın kendisi de başka sahnelerde vardır: {ar:يَوْمَ يَقُومُ ٱلرُّوحُ وَٱلْمَلَٰٓئِكَةُ صَفًّۭا, tr:yevme yekûmu'r-rûhu ve'l-melâiketu saffâ, gloss:Ruh ve meleklerin saf hâlinde durduğu gün, source:78:38}, {ar:وَٱلصَّٰٓفَّٰتِ صَفًّۭا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1}. İnsanlar da Rabbe saf hâlinde sunulur: {ar:وَعُرِضُوا۟ عَلَىٰ رَبِّكَ صَفًّۭا, tr:ve urıdû alâ rabbike saffâ, gloss:Rabbine saf hâlinde sunuldular, source:18:48}. Bu geliş inkârcıların beklediği şeyin gerçekleşmesidir: {ar:هَلْ يَنظُرُونَ إِلَّآ أَن يَأْتِيَهُمُ ٱللَّهُ فِى ظُلَلٍۢ مِّنَ ٱلْغَمَامِ وَٱلْمَلَٰٓئِكَةُ, tr:hel yenzurûne illâ en ye'tiyehumu'llâhu fî zulelin mine'l-ğamâmi ve'l-melâike, gloss:onlar Allah'ın ve meleklerin bulut gölgeleri içinde gelmesinden başka bir şey mi bekliyorlar, source:2:210}. Aynı bekleyiş başka bir ayette de dile getirilir {source:6:158}. Göğün bulutla yarıldığı ve meleklerin indirildiği gün de anlatılır {source:25:25}.

Kaynaklar: 89:1 ٱلْفَجْرِ ف ج ر B003; 89:2 عَشْرٍۢ ع ش ر B005; 89:3 ٱلْوَتْرِ و ت ر B004; 89:21 دَكًّۭا د ك ك B008; 89:22 وَجَآءَ ج ي ء B001; 89:22 وَٱلْمَلَكُ م ل ك B009; 89:22 صَفًّۭا ص ف ف B001; 89:23 وَجِا۟ىٓءَ ج ي ء B004

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

