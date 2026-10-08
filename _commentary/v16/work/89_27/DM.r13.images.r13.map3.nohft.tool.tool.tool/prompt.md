Focus: 89:27. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_27/D.r13/context.md =====
# 89:27 — focus

يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ

Anchor translation (canonical reading, reference only):

Ey huzur bulmuş ruh!

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَٰٓأَيَّتُهَا | أَيَّتُهَا |  | VOC;N |
| 2 | ٱلنَّفْسُ | نَفْس | ن ف س | DET;N |
| 3 | ٱلْمُطْمَئِنَّةُ | مُّطْمَئِنَّة | ط م ن | DET;ADJ |


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
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
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
- 89:27 ◀ focus يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_27/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ف س (root_001533) — identity root of ٱلنَّفْسُ (w2)

- **B001** soluk alıp verme — soluk alıp verme · gövdeye girip çıkan hava; soluk · tek soluk ya da soluklanma arası · soluklar
  التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)
- **B002** sıkıntıyı hafifletip ferahlatma — Tanrı onun sıkıntısını giderdi · beni sıkıntıdan kurtarıp rahatlat · Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı
  نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)
- **B003** kem gözle zarar verme — zarar verdiğine inanılan bakış · ona kem göz değdi · kem gözle zarar veren kişi
  يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)
- **B004** canlıdaki akışkan kan — kaybıyla yaşamın da yitirildiği kan · hayvandaki akışkan kan
  النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)
- **B005** doğum ve doğuma bağlı kadın-çocuk durumu — doğum yapmış ya da doğum sonrası kanaması olan kadın · doğum ve doğum sonrası kanama dönemi · yeni doğan çocuk · doğmadan önce
  الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)
- **B006** soluk aralı içim ve bir içimlik yudum — bir solukta alınan yudum ya da içim · üç soluk arasıyla içme
  كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)
- **B007** bir deri işlemeye yetecek sepi maddesi payı — deriyi bir kez işlemeye yetecek sepi maddesi · bir işlemelik sepi maddesi payı
  في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)
- **B008** yaşamı sürdüren, bol ve doyurucu su — yaşamı ayakta tutan su · bol ve susuzluğu gideren içecek · tadı kötü, bayat ve içimi güç içecek
  يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)
- **B009** kalıba bağlı yarılıp açılma ve genişleme [kalıp] — yay çatladı ya da yarıldı · sabah söktü, aydınlık yayıldı · gündüz uzayıp genişledi · ırmağın suyu artıp yayıldı
  تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)
- **B010** değerli ve uğrunda yarışılan şey — değerli, önemli ve arzulanan · bir şeyi elde etme ya da üstünlere benzeme yarışı · başkasına vermeye kıyamayıp esirgemek · sahip olduğu şey yüzünden onu kıskanmak
  شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)
- **B011** bedene yaşam veren can — bedene yaşam veren can · insan ya da canlı birey
  النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)
- **B012** şeyin kendisi ve bütün öz varlığı [kalıp] — şeyin tam kendisi ve gerçeği · başkası aracılığıyla değil, bizzat kendisi
  كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)
- **B013** iç düşünce, niyet ve ayırt etme gücü — onun içinden geçen düşünce ya da niyet · ayırt etmeyi sağlayan zihinsel güç
  نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)
- **B014** sağlam, cömert ve onurlu yaradılış — sağlam karakterli, dayanıklı ve cömert adam · büyüklük duygusu, onur, yüksek amaç ve kendine saygı
  رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)
- **B015** uzaklık, genişlik ve zaman payı — işinde rahat hareket edecek genişlikte · ek süre ya da hareket alanı · daha uzak, daha uzun ya da daha geniş
  هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)
- **B016** eski bahis oyunundaki beşinci pay oku — eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok
  النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)

## ط م ء ن (root_000948) — identity root of ٱلْمُطْمَئِنَّةُ (w3)

- **B001** tedirginlikten sonra durulup güven duygusuna kavuşma — tedirginlikten sonra durulup kendini güvende hissetmek · tedirginlikten sonra durulma · iç yatışması ve güven duygusu · bir şeye güvenip onunla içi rahat eden · inançla dinginleşip Yaradan'a içten yönelen benlik · inançla güç bulup dingin kalan yürek · ondan dolayı durulmak · ondan dolayı durulmak · dingin olanı küçültmeli veya sevecen biçimde anlatan söz · dinginliği küçültmeli veya sevecen biçimde anlatan söz · ses ve anlamca hem durulmaya hem alçalmaya yaklaşan biçim
  الطمأنينة والاطمئنان السكون بعد الانزعاج (mufradat)؛ اطمأن الرجل واطمأن قلبه واطمأنت نفسه إذا سكن واستأنس (ayn)؛ اطمأن الرجل اطمئنانا وطمأنينة أي سكن (sihah)؛ اطمأن قلبه إذا سكن والاسم الطمأنينة (tahdhib)؛ يقال اطمأن المكان يطمئن طمأنينة وطامنت منه سكنت (maqayis)
- **B002** fiziksel olarak alçakta bulunma ya da aşağı doğru eğme — arazinin çevresine göre alçak bölümü · çevresine göre alçakta kalan arazi · sırtını eğip aşağı indirdi · sırtını eğip aşağı indirdi · sırtını eğip aşağı indirdi · ses ve anlamca hem durulmaya hem alçalmaya yaklaşan biçim
  المطمئن من الأرض أرض منخفضة وهي المتطأمنة (ayn)؛ طمأن ظهره وطامنه بمعنى (sihah)؛ طامن ظهره إذا حناه ومنهم من يقول طأمن (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:27, and ## Buluşmalar) =====
## Gece örtüsü ve onu yaran şafak

Sure bir yarılmayla açılır: {ar:وَٱلْفَجْرِ, tr:ve'l-fecr, gloss:şafağa andolsun, source:89:1}. Arapçada fecr, karanlığın sabahtan ayrılıp açılmasıdır: {ar:الفجر انفجار الظلمة عن الصبح, tr:el-fecru'nficâru'z-zulmeti ani's-subh, gloss:fecr, karanlığın sabahtan yarılıp açılmasıdır, source:"ف ج ر,B002"}. Sabaha bu adın verilmesi de geceyi yarmasındandır: {ar:قيل للصبح فجر لكونه فجر الليل, tr:kîle li's-subhi fecrun li-kevnihî fecera'l-leyl, gloss:sabaha fecr denmesi geceyi yarmasındandır, source:"ف ج ر,B002"}. Sahnede gece her şeyin üstüne serilmiş bir örtüdür. Şafak bu örtüyü bir anda kaldırmaz, ufkun bir noktasından yırtar ve ışık o yarıktan sızar. Kelimenin ayetteki anlamı şafaktır. Aynı kökten gelen imgeler bu anlamın yanında duyulur, onun yerine geçmez. Aşağıdaki bütün imgeler de bu ölçüyle okunur.

Gecenin örtüsü Arapçada ayrı bir kökün işidir: {ar:جنان الليل سواده وستره الأشياء, tr:cenânu'l-leyli sevâduhû ve setruhu'l-eşyâ', gloss:gecenin cenânı, karanlığı ve şeyleri örtmesidir, source:"ج ن ن,B002"}. Kur'an bu fiili İbrahim'in sahnesinde kullanır. Gece onu örtünce bir yıldız görür ve "Bu Rabbimdir" der. Yıldız batınca batanları sevmediğini söyler: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا, tr:fe-lemmâ cenne aleyhi'l-leylu raâ kevkebâ, gloss:gece onu örtünce bir yıldız gördü, source:6:76}. Burada örtü görmeyi engellemez. Tersine, karanlığın içinde batanla batmayanı ayırmayı mümkün kılar.

İkinci ayet geceleri sayar: {ar:وَلَيَالٍ عَشْرٍۢ, tr:ve leyâlin aşr, gloss:ve on geceye, source:89:2}. Gece burada tek bir örtü değildir, birbirini izleyen karanlıklardır: {ar:ظلام الليل, tr:zalâmu'l-leyl, gloss:gecenin karanlığı, source:"ل ي ل,B001"}. Dördüncü ayet geceyi hareket hâlinde gösterir: {ar:وَٱلَّيْلِ إِذَا يَسْرِ, tr:ve'l-leyli izâ yesr, gloss:yürüyüp gittiğinde geceye, source:89:4}. Fiil gece yolculuğunu anlatır: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:surâ, gece yürüyüşüdür, source:"س ر ي,B001"}. Aynı harfler bir şeyin üstündeki örtüyü kaldırmayı da adlandırır: {ar:السرو كشف الشيء عن الشيء, tr:es-servu keşfu'ş-şey'i ani'ş-şey', gloss:bir şeyi başka bir şeyin üstünden açmak, source:"س ر ي,B004"}. Bir örnek: {ar:انسرى عني الهم انكشف, tr:insarâ anni'l-hemmu'nkeşef, gloss:tasa üzerimden kalktı, açıldı, source:"س ر ي,B004"}. Gece yürüdükçe gider, gittikçe altında kalanı açık bırakır. Örtü iki yolla kalkar: yırtılarak, ki bu fecrdir, ve kayarak, ki bu seryidir. Surenin ilk dört ayeti bu iki hareketi aynı gecenin iki ucuna yerleştirir.

Kur'an aynı ikiliyi başka yeminlerde de kurar. Tekvîr suresinde gece kararır ve sabah nefes alır: {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararıp çekildiğinde geceye, source:81:17}, {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha, source:81:18}. Müddessir suresinde gece arkasını döner ve sabah ağarır: {ar:وَٱلَّيْلِ إِذْ أَدْبَرَ, tr:ve'l-leyli iz edber, gloss:arkasını döndüğünde geceye, source:74:33}, {ar:وَٱلصُّبْحِ إِذَآ أَسْفَرَ, tr:ve's-subhi izâ esfer, gloss:ağardığında sabaha, source:74:34}. Leyl suresi ise geceye tam örttüğü anda yemin eder: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye, source:92:1}. Yarma işini Kur'an Allah'a da verir, ama başka bir kökle: {ar:فَالِقُ ٱلْإِصْبَاحِ, tr:fâliku'l-ısbâh, gloss:sabahı yarıp çıkaran, source:6:96}. Aynı kök Felak suresindeki sığınma sözünde de geçer {source:113:1}. Kökler ayrıdır ama mekanizma aynıdır: karanlık bir kabuk gibi çatlar. Oruç hükmü yarığın ne kadar ince olduğunu gösterir. Beyaz iplik siyah iplikten şafakta ayrılır: {ar:ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ, tr:el-haytu'l-ebyadu mine'l-hayti'l-esvedi mine'l-fecr, gloss:şafaktan beyaz iplik siyah iplikten, source:2:187}. Demek ki şafak bir alan değil, bir çizgidir. Kadir gecesi de bu çizgiye kadar sürer: {ar:سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ, tr:selâmun hiye hattâ matla'i'l-fecr, gloss:o, şafağın doğuşuna kadar esenliktir, source:97:5}.

Yarılmanın ters yüzü de aynı köktedir. Ahlâki yırtıklık anlamındaki fücur şöyle tarif edilir: {ar:الفجور شق ستر الديانة, tr:el-fucûru şakku sitri'd-diyâne, gloss:fücur, din örtüsünü yırtmaktır, source:"ف ج ر,B004"}. Şafak karanlığı yırtınca ışık gelir. İnsan dinin örtüsünü yırtınca açılan şey ışık değildir. Surenin ilk kelimesi bu iki yarılmayı birlikte taşır. On birinci ve on ikinci ayetlerde sınırı aşan kavimler anlatılırken ikinci yön duyulur.

Beşinci ayet yeminin kime söylendiğini sorar: {ar:هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ, tr:hel fî zâlike kasemun li-zî hicr, gloss:bunda akıl sahibi için bir yemin var mı, source:89:5}. Hicr kökü bir duvarın işini anlatır: {ar:المنع والإحاطة, tr:el-men'u ve'l-ihâta, gloss:alıkoymak ve çevrelemek, source:"ح ج ر,B001"}. Akla bu adın verilmesi de bundandır: {ar:العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي, tr:el-aklu yusemmâ hicran li-ennehû yemne'u min ityâni mâ lâ yenbeğî, gloss:akla hicr denir, çünkü yakışmayanı yapmaktan alıkoyar, source:"ح ج ر,B002"}. Örtüyü yırtan şafak, içinde bir duvar taşıyan birine seslenir. Akıl, insanı dışarı taşmaktan tutan iç duvardır. Kur'an aynı kelimeyi kıyamet gününün duvarı olarak da kullanır. Meleklerin görüldüğü gün suçlulara müjde yoktur ve o gün {ar:وَيَقُولُونَ حِجْرًۭا مَّحْجُورًۭا, tr:ve yekûlûne hicran mahcûrâ, gloss:ve "aşılmaz bir engel" derler, source:25:22}.

Sure bir örtünün içine girişle biter: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}, {ar:وَٱدْخُلِى جَنَّتِى, tr:vedhulî cennetî, gloss:ve cennetime gir, source:89:30}. Girmek, çıkmanın karşıtıdır: {ar:الدخول نقيض الخروج, tr:ed-duhûlu nakîdu'l-hurûc, gloss:girmek çıkmanın zıddıdır, source:"د خ ل,B001"}. Girilen yer gecenin örtüsüyle aynı köktendir. Bahçe {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:kullu bustânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bahçe, source:"ج ن ن,B003"} demektir, ahiretteki cennet de {ar:ثواب مستور عنهم اليوم, tr:sevâbun mestûrun anhumu'l-yevm, gloss:bugün onlardan gizli tutulan bir karşılık, source:"ج ن ن,B004"}. Kur'an bu gizliliği açıkça söyler: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ, tr:fe-lâ ta'lemu nefsun mâ uhfiye lehum min kurrati a'yun, gloss:onlar için gizlenmiş göz aydınlığını hiçbir can bilmez, source:32:17}. Aynı kök bir örtüyü daha adlandırır: {ar:الجنن القبر, tr:el-cenen el-kabr, gloss:cenen, kabirdir, source:"ج ن ن,B009"}. Yirmi birinci ayetin dövme fiili de ölünün üstüne toprak yığmayı anlatır: {ar:دككت التراب على الميت إذا هلته عليه, tr:dekektu't-turâbe ale'l-meyyiti izâ hiltuhû aleyh, gloss:toprağı ölünün üstüne yığdım, source:"د ك ك,B003"}. Yerin dövüldüğü ayette kabir toprağı da duyulur. Surenin son kelimesi ise ağaçların örtüsüdür. Ruh toprağın örtüsüne değil, bahçenin örtüsüne çağrılır.

Bir halka daha vardır. Yirmi yedinci ayette seslenilen {ar:ٱلنَّفْسُ, tr:en-nefs, gloss:can, source:89:27} kelimesinin kökü sabahın nefes almasını da adlandırır: {ar:تنفس الصبح أي تبلج, tr:teneffese's-subhu ey teballec, gloss:sabah nefes aldı, yani ağardı, source:"ن ف س,B009"}. Bu nefes alma şafağın yarılmasıyla açıklanır: {ar:إذا انشق الفجر وانفلق, tr:ize'nşakka'l-fecru ve'nfelak, gloss:şafak yarılıp açıldığında, source:"ن ف س,B009"}. Sure fecrle açılır ve son çağrısını nefse yapar. İkisini Tekvîr'in nefes alan sabahı birbirine bağlar {source:81:18}.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B002; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:2 وَلَيَالٍ ل ي ل B001; 89:4 يَسْرِ س ر ي B001; 89:4 يَسْرِ س ر ي B004; 89:5 حِجْرٍ ح ج ر B001; 89:5 حِجْرٍ ح ج ر B002; 89:21 دُكَّتِ د ك ك B003; 89:27 ٱلنَّفْسُ ن ف س B009; 89:29 فَٱدْخُلِى د خ ل B001; 89:30 جَنَّتِى ج ن ن B002; 89:30 جَنَّتِى ج ن ن B003; 89:30 جَنَّتِى ج ن ن B004; 89:30 جَنَّتِى ج ن ن B009

## Dikilen, oyulan ve yerle bir edilen

Üç kavim yaptıkları yapılarla anılır. Âd'ın şehri şöyle anılır: {ar:إِرَمَ ذَاتِ ٱلْعِمَادِ, tr:İrame zâti'l-imâd, gloss:sütunlar sahibi İrem, source:89:7}. İmâd, yükün dayandığı şeydir: {ar:الشيء الذي يسند إليه عماد, tr:eş-şey'u'llezî yusnedu ileyhi imâd, gloss:bir şeyin dayandırıldığı nesne imâddır, source:"ع م د,B003"}. Mermer sütunlar da bu adı taşır: {ar:العمد أساطين الرخام, tr:el-amed esâtînu'r-ruhâm, gloss:amed, mermer sütunlardır, source:"ع م د,B003"}. Ayetin kendisi yükseklik ya da yüksek yapı diye açıklanır: {ar:ذات العماد أي ذات الطول وقيل ذات البناء الرفيع, tr:zâtu'l-imâd ey zâtu't-tûl, ve kîle zâtu'l-binâi'r-refî', gloss:zâtu'l-imâd, yani boyu uzun; yüksek yapılı da denmiştir, source:"ع م د,B005"}. Başka bir kullanımda imâd çadır direğidir: {ar:أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها, tr:ehlu amûdin ve ehlu imâdin ashâbu'l-ahbiyeti lâ yenzilûne ğayrahâ, gloss:direk ehli, çadırdan başka yerde konaklamayanlardır, source:"ع م د,B004"}. Taş sütun da olsa çadır direği de olsa sahne aynıdır: dik duran ve üstündeki ağırlığı taşıyan bir gövde. İrem adı da dikili bir taşı çağırır, çünkü Arapçada bu kelime çölde yol işareti olarak dikilen taşlar için kullanılır: {ar:الإرم حجارة تنصب علما في المفازة, tr:el-irem hicâratun tunsabu aleman fi'l-mefâze, gloss:irem, çölde işaret olarak dikilen taşlardır, source:"memory"}. Kur'an Âd'ın bu dikme tutkusunu Hûd'un ağzından anlatır: {ar:أَتَبْنُونَ بِكُلِّ رِيعٍ ءَايَةًۭ تَعْبَثُونَ, tr:e-tebnûne bi-kulli rî'in âyeten ta'besûn, gloss:her yüksek yere oyun olsun diye bir nişan mı dikiyorsunuz, source:26:128}, {ar:وَتَتَّخِذُونَ مَصَانِعَ لَعَلَّكُمْ تَخْلُدُونَ, tr:ve tettehızûne mesânia leallekum tahludûn, gloss:sanki ölümsüz kalacakmışsınız gibi yapılar ediniyorsunuz, source:26:129}. Âd'ın kendi sözü de şuydu: {ar:مَنْ أَشَدُّ مِنَّا قُوَّةً, tr:men eşeddu minnâ kuvveh, gloss:bizden daha güçlü kim var, source:41:15}. Gökleri ise Allah sütunsuz yükseltir: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhu'llezî refe'a's-semâvâti bi-ğayri amedin teravnehâ, gloss:Allah, gökleri görebileceğiniz sütunlar olmadan yükselten, source:13:2}. İnsanın yükselttiği şey sütuna muhtaçtır. Sütun yıkılınca yükseklik de gider.

Sekizinci ayet şöyledir: {ar:ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ, tr:elletî lem yuhlak misluhâ fi'l-bilâd, gloss:ülkelerde benzeri yaratılmamış olan, source:89:8}. Halk, önceden örneği olmayan bir şeyi meydana getirmektir: {ar:الخلق ابتداع الشيء على مثال لم يسبق إليه, tr:el-halku ibtidâu'ş-şey'i alâ misâlin lem yusbak ileyh, gloss:halk, bir şeyi daha önce yapılmamış bir örneğe göre ortaya koymaktır, source:"خ ل ق,B002"}. Zanaatçının dilinde ise deriyi kesmeden önce ölçüp biçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kadertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüm, source:"خ ل ق,B001"}. Ayetteki "benzer" kelimesinin kökü iki zıt duruşu birden taşır. Biri {ar:مثل الرجل قائما انتصب, tr:mesele'r-raculu kâimen intesab, gloss:adam ayağa dikildi, source:"م ث ل,B005"}, öteki {ar:مثل أي لطأ بالأرض وهو من الأضداد, tr:mesele ey lati'e bi'l-ard, ve huve mine'l-addâd, gloss:yere yapıştı; bu, zıt anlamlı kelimelerdendir, source:"م ث ل,B006"}. Silinmiş iz de bu köktendir: {ar:الماثل الدارس, tr:el-mâsil ed-dâris, gloss:mâsil, silinip gitmiş olandır, source:"م ث ل,B006"}. Ayette anlam "benzeri"dir. Yanında, dikilip duran yapı ile yere serilmiş yıkıntı aynı harflerde duyulur. Halk kökü de yerle bir olmuş izi adlandırır: {ar:رسم مخلولق إذا استوى بالأرض, tr:resmun mahlevlik izestevâ bi'l-ard, gloss:yerle bir olmuş harabe izi, source:"خ ل ق,B008"}. Benzersiz diye anılan şehir, benzerliği anlatan kelimenin içinde hem ayakta hem yerde durur.

Dokuzuncu ayet Semûd'u bir oyma işiyle anar: {ar:وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ, tr:ve Semûde'llezîne câbu's-sahra bi'l-vâd, gloss:ve vadide kayaları oyan Semûd, source:89:9}. Cevb, oymak ve kazmaktır: {ar:اجتاب احتفر, tr:ictâbe ihtefer, gloss:oydu, kazdı, source:"ج و ب,B001"}. Ölçüsü bir gömleğin yaka deliğidir: {ar:قطعك الشيء كما يجاب الجيب, tr:kat'uke'ş-şey'e kemâ yucâbu'l-ceyb, gloss:bir şeyi, yaka deliği açar gibi kesmen, source:"ج و ب,B001"}. Kaya da sıradan bir taş değildir: {ar:الصخر عظام الحجارة وصلابها, tr:es-sahru izâmu'l-hicâreti ve sılâbuhâ, gloss:sahr, taşların iri ve sert olanlarıdır, source:"ص خ ر,B001"}. Kumaşa yaka açar gibi en sert kayaya kapı açmak: işin inceliği ile malzemenin sertliği aynı cümlede yer alır. Beşinci ayetteki hicr kelimesi burada ikinci kez duyulur: {ar:الحجر منازل ثمود, tr:el-hicru menâzilu Semûd, gloss:Hicr, Semûd'un yurdudur, source:"ح ج ر,B004"}. Aynı kelimenin bir anlamı da taşın kendisidir: {ar:الحجر الجوهر الصلب المعروف, tr:el-hacer el-cevheru's-sulbu'l-ma'rûf, gloss:hacer, bilinen sert maddedir, source:"ح ج ر,B003"}. Kur'an Hicr halkını, elçileri yalanlayan {source:15:80} ve dağlardan güven içinde ev oyan bir topluluk olarak anlatır: {ar:وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ, tr:ve kânû yenhitûne mine'l-cibâli buyûten âminîn, gloss:dağlardan güven içinde evler oyarlardı, source:15:82}. Sonları bir sabah vakti gelir: {ar:فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ, tr:fe-ehazet'humu's-sayhatu musbihîn, gloss:sabaha girerlerken onları o korkunç ses yakaladı, source:15:83}. Salih'in Semûd'a sözü de aynı işi anar {source:7:74}. Semûd'un sonu, yurtlarında yere yapışıp kalmaktır: {ar:فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ, tr:fe-asbehû fî dârihim câsimîn, gloss:yurtlarında diz üstü çökmüş olarak sabahladılar, source:7:78}.

Onuncu ayet şöyledir: {ar:وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ, tr:ve Fir'avne zi'l-evtâd, gloss:ve kazıklar sahibi Firavun, source:89:10}. Kazık, yere çakılıp bir şeyi yerinde tutan dikmedir. Kur'an Firavun'un bir başka yapısını da anlatır. Firavun Hâmân'dan çamuru ateşte pişirip kendisine bir kule yapmasını ister ki Musa'nın ilahına çıkıp baksın: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا, tr:fe-evkıd lî yâ Hâmânu ale't-tîni fec'al lî sarhâ, gloss:ey Hâmân, benim için çamurun üstünde ateş yak ve bana bir kule yap, source:28:38}. Kur'an Firavun'un kazıklarının karşısına kendi kazıklarını koyar: {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:ve dağları kazıklar, source:78:7}. Firavun "kazıklar sahibi" sıfatıyla yalanlayan kavimler arasında da sayılır {source:38:12}.

On birinci ayetin fiili, sudan sonra yüksekliği de taşır: {ar:الطغية أعلى الجبل, tr:et-tağye a'le'l-cebel, gloss:tağye, dağın en yüksek yeridir, source:"ط غ ي,B005"}, {ar:كل مكان مرتفع طغوة, tr:kullu mekânin murtefiin tağve, gloss:her yüksek yer tağvedir, source:"ط غ ي,B005"}. Azgınlık, sınırın üstüne çıkmaktır. Kur'an bunu Firavun'da gösterir: {ar:إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ, tr:inne Fir'avne alâ fi'l-ard, gloss:Firavun yeryüzünde yükseldi, source:28:4}. Firavun'un iddiası da şudur: {ar:أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:ene rabbukumu'l-a'lâ, gloss:en yüce rabbiniz benim, source:79:24}. Aynı şeyi insanda da gösterir: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6}, {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staşnâ, gloss:kendini ihtiyaçsız gördüğü için, source:96:7}.

Yirmi birinci ayet bütün bu dikili şeylere cevap verir: {ar:كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا, tr:kellâ izâ dukketi'l-ardu dekken dekkâ, gloss:hayır, yer dövüldükçe dövülüp düzlendiğinde, source:89:21}. Dekk, bir duvarı ya da dağı kırmaktır: {ar:الدك كسر الحائط والجبل, tr:ed-dekku kesru'l-hâiti ve'l-cebel, gloss:dekk, duvarı ve dağı kırmaktır, source:"د ك ك,B001"}. Kırmanın ölçüsü de yerle aynı hizaya gelmektir: {ar:ضربته وكسرته حتى سويته بالأرض, tr:darabtuhû ve kesertuhû hattâ sevveytuhû bi'l-ard, gloss:onu vurup kırdım, sonunda yerle bir ettim, source:"د ك ك,B001"}. Sonunda yer, hörgücü olmayan bir deve gibi düzleşir: {ar:أرض دكاء مسواة وناقة دكاء لا سنام لها, tr:ardun dekkâu musevvâtun ve nâkatun dekkâu lâ senâme lehâ, gloss:dekkâ yer düzlenmiş yerdir; dekkâ deve hörgücü olmayan devedir, source:"د ك ك,B002"}. Kur'an bu fiili üç sahnede kullanır. Musa Rabbini görmek ister, Rabbi dağa tecelli eder ve onu dümdüz eder: {ar:جَعَلَهُۥ دَكًّۭا وَخَرَّ مُوسَىٰ صَعِقًۭا, tr:cealehû dekkan ve harra Mûsâ sa'ikâ, gloss:dağı dümdüz etti, Musa da bayılıp yere düştü, source:7:143}. Zülkarneyn demirden seddini bitirince bunun Rabbinden bir rahmet olduğunu, Rabbinin vaadi gelince onu dümdüz edeceğini söyler: {ar:فَإِذَا جَآءَ وَعْدُ رَبِّى جَعَلَهُۥ دَكَّآءَ, tr:fe-izâ câe va'du rabbî cealehû dekkâ', gloss:Rabbimin vaadi gelince onu dümdüz eder, source:18:98}. Kıyamette de yer ve dağlar kaldırılıp tek bir darbeyle ezilir: {ar:وَحُمِلَتِ ٱلْأَرْضُ وَٱلْجِبَالُ فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ, tr:ve humileti'l-ardu ve'l-cibâlu fe-dukketâ dekketen vâhideh, gloss:yer ve dağlar kaldırılıp tek bir darbeyle ezildiğinde, source:69:14}. Dağlar sorulduğunda verilen cevap, onların dümdüz bir alana çevrileceğidir: {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:yerlerini dümdüz bir ova olarak bırakır, source:20:106}, {ar:لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا, tr:lâ terâ fîhâ ivecen ve lâ emtâ, gloss:orada ne bir çukur ne bir tümsek görürsün, source:20:107}. Sütunlar, kaya evler, kazıklar ve kuleler bu düzlükte ayrı ayrı durmaz. Hepsi dikildikleri zeminle bir olur. Kur'an Âd'ın sonunu devrilmiş hurma kütükleriyle gösterir: {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍۢ, tr:keennehum a'câzu nahlin hâviyeh, gloss:sanki içi boş hurma kütükleri gibi, source:69:7}. Sütun gibi dikilmiş gövdeler artık yerde yatmaktadır.

Yirmi ikinci ayetteki saf kelimesi bu düzlüğün adını verir: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, keennehû alâ saffin vâhid, gloss:safsaf, sanki tek bir saf üzerindeymiş gibi dümdüz olan yerdir, source:"ص ف ف,B005"}.

Alçalmanın iki yolu vardır. Yukarı çıkan zorla indirilir, ama surede kendiliğinden alçalan da vardır. On altıncı ayette insan şöyle der: {ar:رَبِّىٓ أَهَٰنَنِ, tr:rabbî ehânen, gloss:Rabbim beni aşağıladı, source:89:16}. Hevân, değersiz kılınmaktır: {ar:الهون هوان الشيء الحقير, tr:el-hûn hevânu'ş-şey'i'l-hakîr, gloss:hûn, değersiz şeyin düşüklüğüdür, source:"ه و ن,B003"}. Aynı kök yeryüzünde alçakgönüllü yürüyüşü de adlandırır: {ar:يمشي على الأرض هونا, tr:yemşî ale'l-ardı hevnâ, gloss:yeryüzünde yumuşak, alçakgönüllü yürür, source:"ه و ن,B001"}. Kur'an Rahman'ın kullarını böyle tanıtır: {ar:وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا, tr:ve ibâdu'r-rahmâni'llezîne yemşûne ale'l-ardı hevnâ, gloss:Rahman'ın kulları yeryüzünde alçakgönüllülükle yürüyenlerdir, source:25:63}. Yirmi yedinci ayetteki mutmainne kelimesi alçak yeri ve eğilmiş sırtı taşır: {ar:المطمئن من الأرض أرض منخفضة, tr:el-mutmainnu mine'l-ard ardun munhafida, gloss:yerin mutmain olanı, alçak yerdir, source:"ط م ء ن,B002"}, {ar:طامن ظهره إذا حناه, tr:tâmene zahrahû izâ henâh, gloss:sırtını eğdi, source:"ط م ء ن,B002"}. Yirmi dokuzuncu ayetteki kullar da çiğnenip düzleşmiş yolun köküyle anılır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muabbed ve huve'l-meslûku'l-muzellel, gloss:muabbed yol, çok yürünüp düzleşmiş yoldur, source:"ع ب د,B005"}. Dümdüz edilen yer ile düzleşmiş yol arasındaki fark, düzlüğün nasıl geldiğindedir: biri kırılarak düzleşir, öteki yürünerek. Çağrı ikinciye yapılır.

Kaynaklar: 89:5 حِجْرٍ ح ج ر B003; 89:5 حِجْرٍ ح ج ر B004; 89:7 إِرَمَ ا ر م (memory); 89:7 ٱلْعِمَادِ ع م د B003; 89:7 ٱلْعِمَادِ ع م د B004; 89:7 ٱلْعِمَادِ ع م د B005; 89:8 يُخْلَقْ خ ل ق B001; 89:8 يُخْلَقْ خ ل ق B002; 89:8 يُخْلَقْ خ ل ق B008; 89:8 مِثْلُهَا م ث ل B005; 89:8 مِثْلُهَا م ث ل B006; 89:9 جَابُوا۟ ج و ب B001; 89:9 ٱلصَّخْرَ ص خ ر B001; 89:11 طَغَوْا۟ ط غ ي B005; 89:16 أَهَٰنَنِ ه و ن B001; 89:16 أَهَٰنَنِ ه و ن B003; 89:21 دُكَّتِ د ك ك B001; 89:21 دَكًّۭا د ك ك B002; 89:22 صَفًّۭا ص ف ف B005; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B002; 89:29 عِبَٰدِى ع ب د B005

## Yol, binek ve dönüş

Surenin kelimeleri bir yolculuğun aşamalarını sırayla taşır. Dördüncü ayette gece yürüyüşü başlar: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:gece yürüyüşü, source:"س ر ي,B001"}. Kur'an bu kökü kul ve gece kelimeleriyle aynı cümlede kullanır: {ar:سُبْحَٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًۭا, tr:subhâna'llezî esrâ bi-abdihî leylen, gloss:kulunu geceleyin yürüten Allah'ı tesbih ederim, source:17:1}. Dokuzuncu ayetteki fiilin yanında ülke ülke dolaşan yolcu duyulur: {ar:رجل جواب إذا كان قطاعا للبلاد, tr:raculun cevvâbun izâ kâne kattâan li'l-bilâd, gloss:cevvâb, ülkeleri durmadan aşan adamdır, source:"ج و ب,B002"}. On beşinci ve on altıncı ayetlerdeki sınav fiilinin yanında da yolun bineği yıpratması duyulur: {ar:ناقة بلو سفر أبلاها السفر, tr:nâkatun ilvu seferin eblâhe's-sefer, gloss:yolculuğun yıprattığı dişi deve, source:"ب ل و,B001"}. Elbisenin eskimesi de aynı köktendir: {ar:بلي الثوب يبلى بلى وبلاء, tr:beliye's-sevbu yeblâ bilen ve belâ', gloss:elbise eskidi, yıprandı, source:"ب ل و,B001"}. Ayette anlam sınamaktır. Yanında kullanıldıkça yıpranan, yürüdükçe tükenen bir binek duyulur. Sınavın, insanın kendisine ait sandığı şeyi aşındırdığı da duyulur.

Yolculuğun karşısında yere yapışmak vardır. Yirminci ayetteki sevgi kelimesi bir şeye yapışıp kalmakla açıklanır: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbe iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi bir şeye yapışıp ondan ayrılmamaktan türer, source:"ح ب ب,B002"}. Aynı fiil inatla yerinden kalkmayan deveyi de anlatır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-baîru izâ harana ve lezime mekâneh, gloss:deve inat edip yerinden kalkmayınca "ehabbe" denir, source:"ح ب ب,B005"}. Malı yapışarak seven insan çöküp kalmış bir bineğe benzer. Sekizinci ve on birinci ayetlerdeki "ülkeler" kelimesi de yerleşip kalmayı taşır: {ar:بلد بالمكان أقام به فهو بالد, tr:belede bi'l-mekâni ekâme bih, gloss:bir yerde kalıp yerleşti, source:"ب ل د,B009"}, {ar:بلد الرجل بالأرض إذا لزق بها, tr:belede'r-raculu bi'l-ardı izâ leziga bihâ, gloss:adam yere yapıştı, source:"ب ل د,B010"}. Devenin göğsünü yere koyup çökmesi de aynı köktendir: {ar:وضعت الناقة بلدتها بالأرض إذا بركت, tr:vedaati'n-nâkatu beldetehâ bi'l-ardı izâ berakat, gloss:deve göğsünü yere koyup çöktü, source:"ب ل د,B002"}. Yirmi birinci ayetteki yer kelimesinin kökü yere ağırlaşmayı da söyler: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerrudu eydan et-tesâkulu ile'l-ard, gloss:teerrud, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}. Onuncu ayetteki kazık ayağı yere çakar, yirmi altıncı ayetteki bağ ise bağlar. Kur'an bu ağırlığı bir çağrı sahnesinde adlandırır. Allah yolunda harekete geçmeye çağrılan müminlere şöyle seslenir: {ar:ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ, tr:issâkaltum ile'l-ard, e-radîtum bi'l-hayâti'd-dunyâ mine'l-âhira, gloss:yere çakılıp kaldınız; dünya hayatına ahiretten daha mı razı oldunuz, source:9:38}. Yer, razı olmak ve hayat: surenin sonundaki kelimeler burada ters yönde dizilmiştir. Ayetlerine rağmen yere saplanıp kalan adam da şöyle anlatılır: {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ, tr:ve lâkinnehû ahlede ile'l-ardı ve'ttebea hevâh, gloss:ama o yere saplanıp kaldı ve hevesine uydu, source:7:176}.

Yolun sonu dönüştür. Altıncı ayette adı geçen Âd, Arapçada dönüş anlamındaki kökün altında sayılır: {ar:عاد قبيلة وهم قوم هود, tr:Âd kabîle, ve hum kavmu Hûd, gloss:Âd bir kabiledir, Hûd'un kavmidir, source:"ع و د,B012"}. Aynı kök varılacak yeri de adlandırır: {ar:المعاد المصير والمرجع, tr:el-meâd el-masîru ve'l-merci', gloss:meâd, varılacak ve dönülecek yerdir, source:"ع و د,B002"}. Âd bir özel addır ve bu anlamı taşımaz, yalnız harfleri dönüşü çağrıştırır. Kur'an Peygamber'e dönüş yerini vaat eder: {ar:لَرَآدُّكَ إِلَىٰ مَعَادٍۢ, tr:le-râdduke ilâ meâd, gloss:seni elbette dönüş yerine döndürecektir, source:28:85}. Yirmi yedinci ayet yolcuyu durulmuş olarak karşılar: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetuhe'n-nefsu'l-mutmainne, gloss:ey huzura kavuşmuş can, source:89:27}. Huzur, sarsıntıdan sonra gelen dinginliktir: {ar:الطمأنينة والاطمئنان السكون بعد الانزعاج, tr:et-tume'nîne ve'l-itmi'nân es-sukûnu ba'de'l-inzi'âc, gloss:itminan, sarsıntıdan sonraki dinginliktir, source:"ط م ء ن,B001"}. Kur'an bu dinginliğin kaynağını da söyler: {ar:أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ, tr:elâ bi-zikri'llâhi tatmainnu'l-kulûb, gloss:bilin ki kalpler ancak Allah'ı anmakla huzura kavuşur, source:13:28}. Yirmi sekizinci ayetteki çağrı şöyledir: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ, tr:irciî ilâ rabbiki, gloss:Rabbine dön, source:89:28}. Dönmek, başlanılan yere geri gitmektir: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûu'l-avdu ilâ mâ kâne minhu'l-bed', gloss:rücû, başlangıç noktasına dönmektir, source:"ر ج ع,B001"}. Aynı kök, bir yolculuktan ötekine geri gönderilen yorgun hayvanı da adlandırır: {ar:الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال, tr:er-recî' mine'd-devâbbi mâ raca'tehû min seferin ilâ sefer, ve huve'l-kâll, gloss:recî', bir yolculuktan ötekine döndürülen yorgun hayvandır, source:"ر ج ع,B014"}. Çağrılan can ise yeni bir yola gönderilmez. Yolun bittiği yere döndürülür. Kur'an insanın bütün çabasını bu yöne bağlar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe-mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Varılacak yer de bir yerleşmedir: {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ, tr:ilâ rabbike yevmeizini'l-mustekarr, gloss:o gün varılıp karar kılınacak yer Rabbinin huzurudur, source:75:12}. Azan insana da aynı söz söylenir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş Rabbinedir, source:96:8}. Sınanıp musibete uğrayanların sözü de dönüşle biter: {ar:إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ, tr:innâ li'llâhi ve innâ ileyhi râciûn, gloss:biz Allah'a aitiz ve O'na döneceğiz, source:2:156}. Yorgun binek imgesi ile dönüş çağrısı burada aynı insanda birleşir. Dönüşün tersi de Kur'an'dadır. Ölüm gelince inkârcı geri gönderilmeyi ister: {ar:رَبِّ ٱرْجِعُونِ, tr:rabbi'rciûn, gloss:Rabbim, beni geri gönderin, source:23:99}. Cevap ise surenin iki kez kullandığı kelimedir: {ar:كَلَّآ ۚ إِنَّهَا كَلِمَةٌ هُوَ قَآئِلُهَا, tr:kellâ, innehâ kelimetun huve kâiluhâ, gloss:hayır, bu yalnızca onun söylediği bir sözdür, source:23:100}. Yolun en son aşaması giriştir: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Kur'an bu girişi kapılar açılırken bölük bölük sürülen bir kafile olarak da gösterir: {ar:وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا, tr:ve sîka'llezîne'ttekav rabbehum ile'l-cenneti zumerâ, gloss:Rablerinden sakınanlar bölük bölük cennete sürülür, source:39:73}.

Kaynaklar: 89:4 يَسْرِ س ر ي B001; 89:6 بِعَادٍ ع و د B002; 89:6 بِعَادٍ ع و د B012; 89:8 ٱلْبِلَٰدِ ب ل د B002; 89:8 ٱلْبِلَٰدِ ب ل د B009; 89:11 ٱلْبِلَٰدِ ب ل د B010; 89:9 جَابُوا۟ ج و ب B002; 89:15 ٱبْتَلَىٰهُ ب ل و B001; 89:20 وَتُحِبُّونَ ح ب ب B002; 89:20 وَتُحِبُّونَ ح ب ب B005; 89:21 ٱلْأَرْضُ ء ر ض B006; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B001; 89:28 ٱرْجِعِىٓ ر ج ع B001; 89:28 ٱرْجِعِىٓ ر ج ع B014; 89:29 فَٱدْخُلِى د خ ل B001

## Geç gelen hatırlama, nefes ve hayat

Getirilen cehennemle birlikte insan hatırlar: {ar:يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ, tr:yevmeizin yetezekkeru'l-insânu ve ennâ lehu'z-zikrâ, gloss:o gün insan hatırlar; ama bu hatırlama ona ne fayda verir, source:89:23}. Tezekkür, geçmiş olanın peşinden gitmektir: {ar:التذكر طلب ما فات, tr:et-tezekkuru talebu mâ fât, gloss:tezekkür, kaçırılmış olanı aramaktır, source:"ذ ك ر,B003"}. Hatırlamak geriye uzanan bir el gibidir, ama uzandığı şey artık geçmiştir. Ennâ kelimesi "nereden" ve "nasıl" diye sorar: {ar:أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف, tr:ennâ ma'nâhu eyne ve min eyne ve min eyyi cihetin, ve kad tekûnu bi-ma'nâ keyfe, gloss:ennâ "nerede, nereden, hangi yönden" demektir; "nasıl" anlamına da gelebilir, source:"ء ن ي,B005"}. Aynı harflerden gelen fiil ise vaktin gelip gelmediğini söyler: {ar:ما أنى لك ولم يأن لك أي لم يحن, tr:mâ enâ leke ve lem ye'ni leke ey lem yehin, gloss:senin için vakit gelmedi, source:"ء ن ي,B003"}. Kur'an bu fiili hatırlamayla aynı cümlede, müminlere bir uyarı olarak kullanır: {ar:أَلَمْ يَأْنِ لِلَّذِينَ ءَامَنُوٓا۟ أَن تَخْشَعَ قُلُوبُهُمْ لِذِكْرِ ٱللَّهِ, tr:e-lem ye'ni li'llezîne âmenû en tahşea kulûbuhum li-zikri'llâh, gloss:iman edenlerin kalplerinin Allah'ı anarak yumuşamasının vakti gelmedi mi, source:57:16}. Bu ayetin vakti hâlâ açıktır. Surenin ayetindeki vakit ise kapanmıştır. Kur'an aynı soruyu başka yerlerde de sorar: {ar:أَنَّىٰ لَهُمُ ٱلذِّكْرَىٰ وَقَدْ جَآءَهُمْ رَسُولٌۭ مُّبِينٌۭ, tr:ennâ lehumu'z-zikrâ ve kad câehum resûlun mubîn, gloss:apaçık bir elçi gelmişken onlara hatırlama nereden, source:44:13}, {ar:فَأَنَّىٰ لَهُمْ إِذَا جَآءَتْهُمْ ذِكْرَىٰهُمْ, tr:fe-ennâ lehum izâ câethum zikrâhum, gloss:o saat gelince hatırlamaları onlara ne fayda verir, source:47:18}. Uzanmanın mesafesini de gösterir: {ar:وَأَنَّىٰ لَهُمُ ٱلتَّنَاوُشُ مِن مَّكَانٍۭ بَعِيدٍۢ, tr:ve ennâ lehumu't-tenâvuşu min mekânin baîd, gloss:o uzak yerden uzanıp ona ulaşmaları nasıl mümkün olur, source:34:52}. Aynı ifade cehennemin gösterildiği bir sahnede de geçer: {ar:يَوْمَ يَتَذَكَّرُ ٱلْإِنسَٰنُ مَا سَعَىٰ, tr:yevme yetezekkeru'l-insânu mâ seâ, gloss:o gün insan çalışıp ettiklerini hatırlar, source:79:35}. Bu sahne de büyük felaketin gelmesiyle başlar {source:79:34}.

Hatırlayan insanın tek dileği önden göndermektir: {ar:يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى, tr:yekûlu yâ leytenî kaddemtu li-hayâtî, gloss:"Keşke hayatım için önceden bir şey gönderseydim" der, source:89:24}. Önden gönderilen şey varılacak yere önceden ulaştırılan azıktır: {ar:القدم السابقة وكل ما قدمت من خير والعمل الصالح, tr:el-kadem es-sâbika ve kullu mâ kaddemte min hayrin ve'l-amelu's-sâlih, gloss:kadem, önceden yapılmış iyilik, önden gönderdiğin her hayır ve salih ameldir, source:"ق د م,B002"}. Kur'an bu bakışı müminlere bir emir olarak verir: {ar:وَلْتَنظُرْ نَفْسٌۭ مَّا قَدَّمَتْ لِغَدٍۢ, tr:ve'l-tenzur nefsun mâ kaddemet li-ğad, gloss:her can yarın için önden ne gönderdiğine baksın, source:59:18}. Kıyamette de aynı bakış bir pişmanlığa döner: {ar:يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ وَيَقُولُ ٱلْكَافِرُ يَٰلَيْتَنِى كُنتُ تُرَٰبًۢا, tr:yevme yenzuru'l-mer'u mâ kaddemet yedâhu ve yekûlu'l-kâfiru yâ leytenî kuntu turâbâ, gloss:o gün kişi elleriyle önden gönderdiğine bakar, kâfir de "keşke toprak olsaydım" der, source:78:40}. Ayrıca bkz. {source:75:13}, {source:82:5}. Keşke sözü başka sahnelerde de vardır. Zalim ellerini ısırarak şöyle der: {ar:يَٰلَيْتَنِى ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلًۭا, tr:yâ leytenî'ttehaztu mea'r-resûli sebîlâ, gloss:keşke elçiyle birlikte bir yol tutsaydım, source:25:27}. Kitabı sol eline verilen de şöyle der: {ar:يَٰلَيْتَنِى لَمْ أُوتَ كِتَٰبِيَهْ, tr:yâ leytenî lem ûte kitâbiyeh, gloss:keşke kitabım bana verilmeseydi, source:69:25}. Surede insanın üç sözü vardır: "bana ikram etti", "beni aşağıladı" ve "keşke". İlk ikisi sınavı yanlış okur, üçüncüsü bunu çok geç fark eder.

"Hayatım" kelimesi bu fark edişin içeriğidir. Hayat kelimesi büyümeden ahirete kadar geniş bir alanı kapsar: {ar:الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية, tr:el-hayâtu tusta'melu li'l-kuvveti'n-nâmiyeti ve'l-hassâseti ve'l-âkıleti ve'l-uhreviyye, gloss:hayat, büyüyen, duyan, düşünen güç için ve ahiret hayatı için kullanılır, source:"ح ي ي,B001"}. Kur'an asıl hayatın hangisi olduğunu söyler: {ar:وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ, tr:ve inne'd-dâra'l-âhirete le-hiye'l-hayevân, gloss:asıl hayat ahiret yurdudur, source:29:64}. İnsan bu kelimeyi "benim hayatım" diye ilk kez doğru yere koyar, ama o zaman da gönderilecek bir şeyi kalmamıştır. Ölüm anında geri gönderilip iyi iş yapmayı isteyen de "hayır" cevabını alır {source:23:100}.

Bu pişman sesin hemen ardından başka bir canla konuşulur. Nefs kelimesinin kökü nefesin içeriden dışarı çıkmasıdır: {ar:التنفس خروج النسيم من الجوف, tr:et-teneffusu hurûcu'n-nesîmi mine'l-cevf, gloss:teneffüs, havanın içeriden dışarı çıkmasıdır, source:"ن ف س,B001"}. Can da bedeni yaşatan şeydir: {ar:النفس الروح الذي به حياة الجسد, tr:en-nefsu'r-rûhu'llezî bihî hayâtu'l-ced, gloss:nefs, bedenin onunla yaşadığı ruhtur, source:"ن ف س,B011"}. Nefes çıkar ve geri döner. Kur'an canın alınışını ve geri bırakılışını uykuda ve ölümde gösterir: {ar:ٱللَّهُ يَتَوَفَّى ٱلْأَنفُسَ حِينَ مَوْتِهَا وَٱلَّتِى لَمْ تَمُتْ فِى مَنَامِهَا, tr:Allâhu yeteveffe'l-enfuse hîne mevtihâ ve'lletî lem temut fî menâmihâ, gloss:Allah canları ölümleri sırasında, ölmeyenleri de uykularında alır, source:39:42}. Zalimlere ölüm anında melekler ellerini uzatıp şöyle der: {ar:أَخْرِجُوٓا۟ أَنفُسَكُمُ, tr:ahricû enfusekum, gloss:canlarınızı çıkarın, source:6:93}. Aynı ayette karşılık da adlandırılır: {ar:ٱلْيَوْمَ تُجْزَوْنَ عَذَابَ ٱلْهُونِ, tr:el-yevme tuczevne azâbe'l-hûn, gloss:bugün aşağılayıcı bir azapla cezalandırılacaksınız, source:6:93}. Can köprücük kemiklerine dayandığında da yön Rabbe doğrudur {ar:كَلَّآ إِذَا بَلَغَتِ ٱلتَّرَاقِىَ, tr:kellâ izâ beleğati't-terâkıy, gloss:hayır, can köprücük kemiklerine dayandığında, source:75:26}, {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمَسَاقُ, tr:ilâ rabbike yevmeizini'l-mesâk, gloss:o gün sürülüş Rabbinedir, source:75:30}. Surenin sonundaki can ise ne zorla çıkarılır ne de sürülür. Ona seslenilir ve dönmesi söylenir. Kur'an canın başka hâllerini de anar: kötülüğü emreden can {source:12:53} ve kendini kınayan can {source:75:2}. Bu surede seslenilen ise o çalkantılardan sonra durulmuş olandır.

Kaynaklar: 89:23 يَتَذَكَّرُ ذ ك ر B003; 89:23 وَأَنَّىٰ ء ن ي B003; 89:23 وَأَنَّىٰ ء ن ي B005; 89:24 قَدَّمْتُ ق د م B002; 89:24 لِحَيَاتِى ح ي ي B001; 89:27 ٱلنَّفْسُ ن ف س B001; 89:27 ٱلنَّفْسُ ن ف س B011

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

