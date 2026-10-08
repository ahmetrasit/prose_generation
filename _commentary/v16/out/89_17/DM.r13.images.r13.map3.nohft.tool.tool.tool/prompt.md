Focus: 89:17. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_17/D.r13/context.md =====
# 89:17 — focus

كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ

Anchor translation (canonical reading, reference only):

Hayır! Aksine siz yetime değer vermiyorsunuz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | كَلَّا | كَلَّا |  | AVR |
| 2 | بَل | بَل |  | RET |
| 3 | لَّا | لَا |  | NEG |
| 4 | تُكْرِمُونَ | أَكْرَمَ | ك ر م | V;PRON |
| 5 | ٱلْيَتِيمَ | يَتِيم | ي ت م | DET;N |


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
- 89:17 ◀ focus كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
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


===== _commentary/v16/work/89_17/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ر م (root_001294) — identity root of تُكْرِمُونَ (w4)

- **B001** övgüye değer soyluluk, eli açıklık ve onurlandırma — soyluluk, eli açıklık ve övgüye değer huy · soylu, eli açık, bağışlayıcı; kendi türünde seçkin · soylular; seçkin ve övgüye değer olanlar · onurlandırdı veya değerli kıldı · onurlandırma ve incitmeden değerli yarar sağlama · onurlandırma; saygınlık · ayıp ve utanç verici şeylerden uzak durdu · soylu ve değerli çocukları oldu · değerli bir bağ ya da varlık edindi · yumuşak ve saygılı söz · kendi alanında yararlı ve övgüye değer tür · içerdiği yol gösterme, açıklama, bilgi ve bilgelikle övgüye değer kitap · içeriği güzel, saygın ya da mühürlü yazı · en soylu ve en erdemli · güzel ve saygın giriş yeri
  شرف في الشيء في نفسه أو شرف في خلق من الأخلاق (maqayis)؛ الكريم الصفوح (maqayis;sihah)؛ الكرم شرف الرجل (ayn)؛ تكرم عن الشائنات أي تنزه (ayn;tahdhib)؛ الكرم ضد اللؤم (sihah)؛ أتى بأولاد كرام واستحدث علقا كريما (sihah)؛ الكثير الخير الجواد المنعم المفضل (tahdhib)؛ اسم جامع لكل ما يحمد (tahdhib)؛ الأخلاق والأفعال المحمودة (mufradat)؛ كل شيء شرف في بابه (mufradat)
- **B002** yağmur getirme ve toprağın verimli oluşu [kalıp] — bulut yağmur getirdi ve suyunu bolca verdi · bitkisi gür, toprağı iyi ve taşları ayıklanmış arazi · toprağı işlenip gübrelendikten sonra bitkisi gürleşti
  كرم السحاب أتى بالغيث (maqayis;sihah)؛ أرض مكرمة للنبات إذا كانت جيدة النبات (maqayis;sihah)؛ إذا جاد السحاب بغيثه قيل كرم (ayn)؛ أرض مثارة منقاة من الحجارة (ayn;tahdhib)؛ البقعة الطيبة التربة العذاة المنبت بقعة مكرمة (tahdhib)؛ كرمت أرض فلان إذا دملها فزكا نبتها (tahdhib)
- **B003** boyun kolyesi — boyna takılan kolye veya dizili süs · kolyeler
  الكَرْم وهي القلادة (maqayis)؛ الكَرْم القلادة (ayn;sihah)؛ رأيت في عنقها كَرْما حسنا من لؤلؤ (sihah)؛ الكروم القلائد واحدها كَرْم (tahdhib)
- **B004** üzüm ve asma — üzüm, asma veya asmanın meyvesi · tek asma sürgünü veya bir asma
  الكَرْم فالعنب أيضا لأنه مجتمع الشعب منظوم الحب (maqayis)؛ الكرمة طاقة من الكرم (ayn)؛ الكَرْم كرم العنب (sihah)؛ الكرمة الطاقة الواحدة من الكرم (tahdhib)؛ يسمى الكرم كرما لأنه وصف بكرم شجرته وثمرته (tahdhib)
- **B005** kap ağzına konan tabak biçimli kapak — testi veya tencere ağzına konan tabak biçimli kapak
  الكرامة طبق يوضع على رأس الحب (ayn;sihah)؛ لطبق القدر والحب الكرامة (tahdhib)
- **B006** eli açıklıkta övünme yarışı ve üstün gelme — onunla eli açıklık konusunda övünme yarışına girdi · eli açıklıkta onu geçti
  كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه (sihah)
- **B007** uyluk kemiğinin kalça yuvasındaki yuvarlak başı — uyluk kemiğinin kalça yuvasındaki yuvarlak başı
  الكرمة رأس الفخذ المستدير كأنه جوزة تدور في قلت الورك (sihah)
- **B008** karşılık bekleyerek sunma ve övgüyü ödüllendirme — karşılığında ödül almak için onu sundu · kendisine yöneltilen övgüyü ödüllendiren kişi
  أكارم بها يهود أي أهديها إليهم فيثيبوني عليها (tahdhib)؛ أخ مكارم أي يكافئني على مدحي إياه (tahdhib)
- **B009** memnuniyetle kabul ve saygı bildiren kalıp yanıt [kalıp] — evet, memnuniyetle ve seve seve · senin için seve seve; sana duyduğum saygıyla
  نعم وحبا وكرامة (sihah)؛ نعم وحبا وكرما وحبا وكرمة (sihah)؛ أفعل ذلك وكرمة لك وكرمى لك وكرامة لك وكرما لك وكرمة عين (tahdhib)
- **B010** değer verilen varlık ve topluluğun seçkin kişisi — senin için çok değerli olan kişi veya şey · topluluğun soylu, saygın ve seçkin kişisi
  كل شيء يكرم عليك فهو كريمك وكريمتك (tahdhib)؛ الكريمة الرجل الحسيب (tahdhib)؛ إذا أتاكم كريمة قوم فأكرموه أي كريم قوم (tahdhib)؛ لا تدخر عنه شيئا يكرم عليك (tahdhib)

## ي ت م (root_001692) — identity root of ٱلْيَتِيمَ (w5)

- **B001** babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma — insanda babasız, hayvanda annesiz kalma · babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu · çocuk babasını yitirip babasız kaldı · Tanrı onu babasız bıraktı · çocukları babasız bıraktı · babasını yitirmiş çocuklar · babasını yitirmiş çocuklar · çocukları babasız kalmış kadın · çocukları babasız kalmış kadın · onları babasız bıraktı · çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi · babasını yitirmiş çocuklar topluluğu
  اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)
- **B002** tek kalmış ya da benzeri zor bulunan şey — tek başına veya eşi zor bulunan · tek başına duran veya benzeri olmayan şiir dizesi · tek ve eşi zor bulunan inci · tek başına duran kumluk veya dişil varlık
  لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)
- **B003** dalgınlık ve gerekeni eksik yapma — dalgınlık ve gerekeni eksik yapma · gidişinde dalgınlık veya eksik davranış yok
  اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)
- **B004** yavaşlama veya gecikme — gidişinde yavaşlama var · yavaşlama ve gecikme
  في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)
- **B005** evlilikle sona erip ermediği tartışmalı kadın adlandırması [kalıp] — evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın · kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz
  المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:17, and ## Buluşmalar) =====
## Çift, tek ve eşi olmayan

Üçüncü ayet sayıyla yemin eder: {ar:وَٱلشَّفْعِ وَٱلْوَتْرِ, tr:ve'ş-şef'i ve'l-vetr, gloss:çifte ve teke, source:89:3}. Çift, bir şeye benzerinin eklenmesiyle oluşur: {ar:ضم الشيء إلى مثله, tr:dammu'ş-şey'i ilâ mislih, gloss:bir şeyi benzerine katmak, source:"ش ف ع,B001"}. Tek ise yanına benzeri katılmamış olandır: {ar:الوتر الفرد ضد الشفع, tr:el-vetru'l-ferdu diddu'ş-şef', gloss:vetr, çiftin zıddı olan tektir, source:"و ت ر,B001"}. Bu katma işinin insanlar arasındaki biçimi de aynı kökle söylenir: {ar:الانضمام إلى آخر ناصرا له وسائلا عنه, tr:el-indimâmu ilâ âharin nâsıran lehû ve sâilen anh, gloss:birinin yanına geçip ona arka çıkmak ve onun için istemek, source:"ش ف ع,B002"}. Çift, bir şeyin yalnız bırakılmamasıdır.

Çiftin tanımındaki "benzer" kelimesi sekizinci ayette karşımıza çıkar: {ar:لَمْ يُخْلَقْ مِثْلُهَا, tr:lem yuhlak misluhâ, gloss:benzeri yaratılmadı, source:89:8}. Misl, karşılıktır: {ar:المثل النظير, tr:el-mislu'n-nazîr, gloss:misl, dengidir, source:"م ث ل,B001"}. İrem ülkeler içinde tek kalmış bir yapıdır, yanına benzeri katılmamıştır. Bu teklik bir övünç olarak anılır, ama Kur'an gerçek tekliği yalnız Allah'a verir: {ar:لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ, tr:leyse ke-mislihî şey', gloss:O'nun benzeri gibi hiçbir şey yoktur, source:42:11}, {ar:قُلْ هُوَ ٱللَّهُ أَحَدٌ, tr:kul huva'llâhu ehad, gloss:de ki: O Allah birdir, source:112:1}, {ar:وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ, tr:ve lem yekun lehû kufuven ehad, gloss:hiçbir şey O'na denk değildir, source:112:4}. Yaratılmışların düzeni ise çifttir: {ar:وَمِن كُلِّ شَىْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ, tr:ve min kulli şey'in halaknâ zevceyni leallekum tezekkerûn, gloss:her şeyden iki eş yarattık; belki düşünüp hatırlarsınız, source:51:49}.

On yedinci ayetteki yetim, insanlar arasında tek kalmış olandır: {ar:بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:bel lâ tukrimûne'l-yetîm, gloss:bilakis yetime ikram etmiyorsunuz, source:89:17}. Yetim kelimesi tekliği de anlatır: {ar:كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة, tr:kullu şey'in mufredin yeizzu nazîruhû fe-huve yetîm, ve durretun yetîme, gloss:dengi zor bulunan her tek şey yetimdir; eşsiz inciye de "yetim inci" denir, source:"ي ت م,B002"}. Ayette anlam babasız çocuktur. Yanında yanına kimse katılmamış teklik duyulur. Yetime ikram etmek, onun yanına geçip arka çıkmaktır, yani şef'in ikinci anlamıdır. Muhatapların yapmadığı şey tam olarak budur. Kur'an kıyamet gününde bu katılmanın kalmayacağını gösterir. Herkes tek gelir: {ar:وَكُلُّهُمْ ءَاتِيهِ يَوْمَ ٱلْقِيَٰمَةِ فَرْدًا, tr:ve kulluhum âtîhi yevme'l-kıyâmeti ferdâ, gloss:hepsi kıyamet günü O'na tek başına gelir, source:19:95}. İnkârcılara şöyle denir: {ar:وَلَقَدْ جِئْتُمُونَا فُرَٰدَىٰ كَمَا خَلَقْنَٰكُمْ أَوَّلَ مَرَّةٍۢ, tr:ve lekad ci'tumûnâ furâdâ kemâ halaknâkum evvele merra, gloss:sizi ilk defa yarattığımız gibi bize teker teker geldiniz, source:6:94}. Aynı ayette yanlarına geçeceğini sandıkları kimse de görünmez: {ar:وَمَا نَرَىٰ مَعَكُمْ شُفَعَآءَكُمُ, tr:ve mâ nerâ meakum şufeâekum, gloss:yanınızda şefaatçilerinizi görmüyoruz, source:6:94}. Bir başka ayet de şöyle der: {ar:فَمَا تَنفَعُهُمْ شَفَٰعَةُ ٱلشَّٰفِعِينَ, tr:fe-mâ tenfeuhum şefâatu'ş-şâfiîn, gloss:şefaatçilerin şefaati onlara fayda vermez, source:74:48}. Yetimin yanına geçmeyen, kendisi tek kalır.

Yirmi beşinci ve yirmi altıncı ayetler aynı sayımı azaba uygular: {ar:لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:lâ yuazzibu azâbehû ehad, gloss:hiç kimse O'nun azabı gibi azap edemez, source:89:25}, {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:hiç kimse O'nun bağlaması gibi bağlayamaz, source:89:26}. Olumsuz cümledeki ehad bir türün bütününü kapsar: {ar:أحد في النفي لاستغراق جنس الناطقين, tr:ehadun fi'n-nefyi li-istiğrâki cinsi'n-nâtıkîn, gloss:olumsuz cümlede ehad, konuşan varlıkların tamamını kapsar, source:"ء ح د,B002"}. Ne bir kişi ne iki kişi: bu azabın dengi yoktur. İrem'in benzersizliği yapılmış bir şeyin benzersizliğiydi. Buradaki benzersizlik yapanın kendisine aittir.

Bu tekliklerin karşısında sure kelimelerini çiftler: {ar:دَكًّۭا دَكًّۭا, tr:dekken dekkâ, gloss:dövüldükçe dövülerek, source:89:21}, {ar:صَفًّۭا صَفًّۭا, tr:saffen saffâ, gloss:saf saf, source:89:22}. Her birimin ardından benzeri gelir. Yirmi sekizinci ayette rıza da çifttir: {ar:رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak, source:89:28}. Bu sözün yanında iki taraf arasındaki karşılıklı hoşnutluk duyulur: {ar:المراضاة من اثنين, tr:el-murâdât mine'sneyn, gloss:karşılıklı razı olmak iki taraf arasında olur, source:"ر ض و,B003"}. Kur'an bu karşılıklılığı açıkça söyler: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhu anhum ve radû anh, gloss:Allah onlardan razı oldu, onlar da O'ndan razı oldular, source:98:8}. Allah'ın doğruların doğruluğunun fayda verdiği gün olarak tanıttığı günde de aynı söz geçer {source:5:119}. Sonra tek başına seslenilen can bir topluluğa katılır: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Bu katılma şöyle açıklanır: {ar:فادخلي في عبادي أي في حزبي, tr:fedhulî fî ibâdî ey fî hizbî, gloss:kullarımın arasına, yani benim topluluğuma gir, source:"ع ب د,B002"}. Surenin başında soyut bir sayı olan tek ile çift, sonunda yanına kimse katılmayan yetim ile topluluğa katılan can arasındaki farka dönüşür.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B001; 89:3 ٱلشَّفْعِ ش ف ع B002; 89:3 ٱلْوَتْرِ و ت ر B001; 89:8 مِثْلُهَا م ث ل B001; 89:17 ٱلْيَتِيمَ ي ت م B002; 89:25 أَحَدٌۭ ء ح د B002; 89:26 أَحَدٌۭ ء ح د B002; 89:28 رَاضِيَةًۭ مَّرْضِيَّةًۭ ر ض و B003; 89:29 عِبَٰدِى ع ب د B002

## Kucak, ikram ve yetim

On beşinci ayet bir sınavla açılır: {ar:فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ, tr:fe-emme'l-insânu izâ me'btelâhu rabbuhû fe-ekramehû ve na''amehû, gloss:insan ise Rabbi onu sınayıp ikram ettiğinde ve nimet verdiğinde, source:89:15}. İbtilâ denemektir: {ar:بلوته بلوا جربته واختبرته, tr:belevtuhû belven carrabtuhû ve'htebertuh, gloss:onu denedim, sınadım, source:"ب ل و,B002"}. Allah'ın sınaması iki yolla olur: {ar:اختبار الله للعباد تارة بالمسار وتارة بالمضار, tr:ihtibâru'llâhi li'l-ibâdi târeten bi'l-mesârri ve târeten bi'l-medârr, gloss:Allah kullarını bazen sevindiren, bazen zarar veren şeylerle sınar, source:"ب ل و,B003"}. Kur'an bunu açıkça söyler: {ar:وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ, tr:ve nebluküm bi'ş-şerri ve'l-hayri fitneh, gloss:sizi deneme olarak kötülükle de iyilikle de sınarız, source:21:35}. İsrailoğulları da iyiliklerle ve kötülüklerle sınanmıştır, belki dönerler diye {ar:وَبَلَوْنَٰهُم بِٱلْحَسَنَٰتِ وَٱلسَّيِّـَٔاتِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve belevnâhum bi'l-hasenâti ve's-seyyiâti leallehum yerci'ûn, gloss:belki dönerler diye onları iyiliklerle ve kötülüklerle sınadık, source:7:168}.

Sınayan "Rabbi"dir. Rab kökü bir şeyi aşama aşama büyütmeyi anlatır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi olgunluğuna erinceye kadar hâlden hâle geçirerek yetiştirmektir, source:"ر ب ب,B002"}. Aynı kök üvey çocuğu da adlandırır: {ar:ربيب الرجل ابن امرأته, tr:rabîbu'r-racul ibnu'mraetih, gloss:adamın rebîbi, karısının oğludur, source:"ر ب ب,B005"}. Nimet vermek de bir babanın çocuklarına davranışıyla söylenir: {ar:نعم فلان أولاده ترفهم, tr:na''ame fulânun evlâdehû tarrafehum, gloss:çocuklarını bolluk içinde, nazla büyüttü, source:"ن ع م,B002"}. İkram eden de şöyle tarif edilir: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayri'l-cevâdu'l-mun'imu'l-mufdıl, gloss:hayrı bol, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Ayetin yanında bir aile sahnesi duyulur: bir çocuk kucakta büyütülür, nazla beslenir ve el üstünde tutulur. Beşinci ayetin hicr kelimesi bu kucağın kendisini de adlandırır: {ar:حجر المرأة وحجرها حضنها, tr:hicru'l-mer'eti ve hacruhâ hıdnuhâ, gloss:kadının hicri kucağıdır, source:"ح ج ر,B005"}. Kur'an rab kökünü ve kucak kelimesini bir hükümde bir araya getirir: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rebâibukumu'llâtî fî hucûrikum, gloss:kucaklarınızda büyüyen üvey kızlarınız, source:4:23}. Büyümüş çocuk anne babası için şöyle dua eder: {ar:رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:rabbi'rhamhumâ kemâ rabbeyânî sağîrâ, gloss:Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et, source:17:24}. Firavun ise Musa'ya büyütme hakkıyla gelir: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi, source:26:18}.

İnsan bu bakımı bir rütbe olarak okur: {ar:فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe-yekûlu rabbî ekramen, gloss:"Rabbim bana ikram etti" der, source:89:15}. Darlıkta ise şöyle olur: {ar:فَقَدَرَ عَلَيْهِ رِزْقَهُۥ, tr:fe-kadera aleyhi rızkahû, gloss:rızkını daralttı, source:89:16}. Bu ifade şöyle açıklanır: {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rızkuhû ey duyyika aleyh, gloss:rızkı daraltılan, yani darlığa sokulan, source:"ق د ر,B004"}. İnsan bu kez "Rabbim beni aşağıladı" der. Aşağılanmış kişi ikramdan yoksun olandır: {ar:الهين الذي لا كرامة له, tr:el-heyyinu'llezî lâ kerâmete leh, gloss:hîn, ikramı olmayandır, source:"ه و ن,B003"}. Aşağılanma bir otoritenin hor görmesiyle gelir: {ar:الهوان من جهة متسلط مستخف به, tr:el-hevânu min cihetin mutesallitin mustahiffin bih, gloss:hevân, onu hafife alan bir hükmedenden gelir, source:"ه و ن,B003"}. İnsan darlığı böyle okur, Rabbini kendisini hor gören bir efendi yerine koyar. Kur'an'da rızkın genişletilmesi ve daraltılması bir hüküm değil, Allah'ın dilemesidir. Bunu Kârûn'un yere geçirilişinden sonra, dün onun yerinde olmayı isteyenler söyler: {ar:وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ, tr:veykeenna'llâhe yebsutu'r-rızka li-men yeşâu min ibâdihî ve yakdir, gloss:demek ki Allah rızkı kullarından dilediğine genişletiyor ve daraltıyormuş, source:28:82}. Rızkı daraltılana verilen hüküm de, Allah'ın verdiğinden harcamasıdır {ar:وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ, tr:ve men kudira aleyhi rızkuhû fe'l-yunfik mimmâ âtâhu'llâh, gloss:rızkı daraltılan, Allah'ın kendisine verdiğinden harcasın, source:65:7}. Nimeti kendi bilgisine bağlayan insana Kur'an şöyle cevap verir: {ar:بَلْ هِىَ فِتْنَةٌۭ, tr:bel hiye fitneh, gloss:hayır, o bir sınavdır, source:39:49}.

On yedinci ayet bu okumayı kökünden çevirir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ, bel lâ tukrimûne'l-yetîm, gloss:hayır, asıl siz yetime ikram etmiyorsunuz, source:89:17}. Az önce insanın kendine alınan bir sıfat sandığı ikram, burada başkasına yapılan bir iş olur. Arapçada ikram cömertlikte yarışmak ve o yarışta öne geçmektir: {ar:كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه, tr:kâramtu'r-racule izâ fâhartuhû fi'l-kerem fe-keremtuhû izâ ğalebtuhû fîh, gloss:cömertlikte yarıştım ve onu cömertlikte geçtim, source:"ك ر م,B006"}. İnsan bu yarışa hiç girmez. Yetim tam bu yerde durur. O, kucağı kalmamış çocuktur: {ar:انقطاع الصبي عن أبيه قبل بلوغه, tr:inkıtâu's-sabiyyi an ebîhi kable bulûğih, gloss:çocuğun ergenliğe ermeden babasından kopması, source:"ي ت م,B001"}. Kelimenin iki yan anlamı da onun durumunu anlatır: {ar:أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره, tr:aslu'l-yutmi'l-ğafle, ve bihî yusemma'l-yetîmu li-ennehû yutegâfelu an birrih, gloss:yetimliğin aslı gaflettir; yetime bu ad verilir, çünkü ona iyilik etmek ihmal edilir, source:"ي ت م,B003"}, {ar:اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه, tr:el-yutmu'l-ibtâ', ve minhu ühıze'l-yetîmu li-enne'l-birra yubtıu anh, gloss:yutm gecikmedir; yetim adı buradan gelir, çünkü iyilik ona geç ulaşır, source:"ي ت م,B004"}. Rabbi tarafından nazla büyütülen insan, babasız çocuğa geç kalır. Kur'an Peygamber'e kendi yetimliğini hatırlatarak bu ilişkiyi kurar: {ar:أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ, tr:e-lem yecidke yetîmen fe-âvâ, gloss:seni yetim bulup barındırmadı mı, source:93:6}, {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:öyleyse yetimi ezme, source:93:9}. Barındırılmış olan barındırır. İkramın ölçüsü de verilir: {ar:إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ, tr:inne ekramekum inda'llâhi etkâkum, gloss:Allah katında en değerliniz, en takvalı olanınızdır, source:49:13}. Allah'ın aşağıladığını kimse yüceltemez: {ar:وَمَن يُهِنِ ٱللَّهُ فَمَا لَهُۥ مِن مُّكْرِمٍ, tr:ve men yuhini'llâhu fe-mâ lehû min mukrim, gloss:Allah kimi aşağılarsa onu yüceltecek kimse yoktur, source:22:18}. Cehennemdeki suçluya ise bu sıfat alay olarak söylenir: {ar:ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ, tr:zuk inneke ente'l-azîzu'l-kerîm, gloss:tat bakalım, hani sen güçlüydün, değerliydin, source:44:49}.

Kaynaklar: 89:5 حِجْرٍ ح ج ر B005; 89:15 ٱبْتَلَىٰهُ ب ل و B002; 89:15 ٱبْتَلَىٰهُ ب ل و B003; 89:15 رَبُّهُۥ ر ب ب B002; 89:15 رَبُّهُۥ ر ب ب B005; 89:15 فَأَكْرَمَهُۥ ك ر م B001; 89:15 وَنَعَّمَهُۥ ن ع م B002; 89:16 فَقَدَرَ ق د ر B004; 89:16 أَهَٰنَنِ ه و ن B003; 89:17 تُكْرِمُونَ ك ر م B006; 89:17 ٱلْيَتِيمَ ي ت م B001; 89:17 ٱلْيَتِيمَ ي ت م B003; 89:17 ٱلْيَتِيمَ ي ت م B004

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

