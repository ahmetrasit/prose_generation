Focus: 89:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_7/D.r13/context.md =====
# 89:7 — focus

إِرَمَ ذَاتِ ٱلْعِمَادِ

Anchor translation (canonical reading, reference only):

Sütunlar sahibi İrem'e,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِرَمَ | إِرَم |  | PN |
| 2 | ذَاتِ | ذُو |  | N |
| 3 | ٱلْعِمَادِ | عِمَاد | ع م د | DET;N |


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
- 89:7 ◀ focus إِرَمَ ذَاتِ ٱلْعِمَادِ
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


===== _commentary/v16/work/89_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع م د (root_001043) — identity root of ٱلْعِمَادِ (w3)

- **B001** isteyerek yönelme ve bilerek yapma — bir şeye isteyerek yönelmek · yanlışlıkla değil, bilerek yapılan eylem · bile isteye, ciddiyetle ve kesinlikle
  عمدت فلانا إذا قصدت إليه (maqayis); عمدت فلانا أي قصدته وتعمدته (ayn); عمدت للشئ قصدت له وهو نقيض الخطاء (sihah); عمدت للشيء إذا قصدت له (tahdhib); العمد والتعمد خلاف السهو (mufradat)
- **B002** dayanak koyarak destekleme — nesneyi dayayıp desteklemek · nesnenin altına dayanak koymak
  تعمد الشيء بعماد يمسكه ويعتمد عليه (maqayis;ayn); عمدت الشيء أسندته (maqayis;mufradat); أقمته بعماد يعتمد عليه وأعمدته جعلت تحته عمدا (sihah); عمدت الحائط إذا دعمته (tahdhib)
- **B003** taşıyıcı dik direk veya sütun — dayanak veya taşıyıcı direk · ahşap, demir ya da taş sütun · uzatılmış ateş sütunları içinde
  الشيء الذي يسند إليه عماد وجمع العماد عمد والعمود من خشب أو حديد (maqayis); عمود الخباء من خشب قائم في الوسط (ayn); العمود عمود البيت وجمعه أعمدة وعمد (sihah); العمد أساطين الرخام وفي عمد من النار (tahdhib); العمود خشب تعتمد عليه الخيمة وجمعه عمد (mufradat)
- **B004** yalnız çadırlarda yaşayan topluluk — başka yerde konaklamayan çadır halkı
  أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها (maqayis;ayn); كانوا أهل عمد ينتقلون إلى الكلأ (tahdhib); أصحاب الأخبية الذين لا ينزلون غيرها (tahdhib)
- **B005** kalıba bağlı uzunluk ve yücelik [kalıp] — uzun boylu veya evi uzaktan görünen · dayanak sayılan yüce kişi
  رجل معمد أي طويل والعماد الطول (maqayis); العماد الأبنية الرفيعة وفلان طويل العماد (sihah); ذات العماد أي ذات الطول وقيل ذات البناء الرفيع (tahdhib)
- **B006** güvenilip dayanılan önder veya temel unsur — topluluğun güvendiği önder · güvenilip dayanılan kişi, mal veya temel unsur
  عميد القوم سيدهم ومعتمدهم (maqayis); عميد القوم سيدهم الذي يعتمدون عليه (ayn); عميد القوم وعمودهم سيدهم والعمدة ما يعتمد عليه (sihah); فلان عمدة قومه إذا كانوا يعتمدونه (tahdhib); العميد السيد الذي يعمده الناس (mufradat)
- **B007** kalıba göre ana, orta veya uzunlamasına parça [kalıp] — işin belkemiği ve ana dayanağı · kulağın ana ve büyük bölümü · mızrak ucunun iki ağzı arasındaki orta bölüm · karında uzanan damar veya gövdeyi taşıyan sırt · karaciğeri besleyen damar ve ana atardamar · tan ışığının ilk yayılışı · kılıç sırtının ortasındaki uzun çizgi · erkek devekuşunun direğe benzeyen iki bacağı
  عمود الأمر قوامه (maqayis;ayn); عمود الأذن معظمها وقوامها (maqayis;ayn;tahdhib); عمود السنان ما توسط شفرتيه (maqayis;ayn;tahdhib); عمود البطن شبه عرق ممدود (maqayis;ayn;tahdhib); عمود الكبد عرق يسقيها وعمود السحر الوتين (maqayis;ayn;tahdhib); عمود الصبح ابتداء ضوئه (sihah;mufradat); عمود السيف الشطيبة في وسط متنه (tahdhib)
- **B008** acıyla ezilip güçten düşme — oturamayacak kadar güçten düşmüş hasta · sevgi veya üzüntü acısıyla yıkılmış yürek · hastalık onu tüketip acıttı
  العميد الرجل المعمود لا يستطيع الجلوس من مرضه (maqayis;ayn;tahdhib); القلب العميد المعمود المشعوف الذي هده العشق (maqayis;ayn); عمد المرض فدحه (sihah); المعمود الحزين الشديد الحزن وما يعمدك أي ما يوجعك (tahdhib); القلب الذي يعمده الحزن والسقيم الذي يعمده السقم (mufradat)
- **B009** baskıyla içten zedelenme [kalıp] — binme yükünden hörgücü içten çökmüş deve · erken sıkıldığı için şişen yara
  السنام إذا كان ضخما فحمل عليه فكسر وبعير عمد وناقة عمدة (maqayis); عمد البعير إذا انفضح داخل سنامه من الركوب (sihah); العمد في السنام أن ينشدخ انشداخا والجرح العمد الذي يعصر فيرم (tahdhib); عمد البعير توجع من عقر ظهره (mufradat)
- **B010** yağmurla derinden ıslanıp topaklanan toprak — yağmurla ıslanıp avuçta topaklanan toprak · yağmur toprağın derinine işledi
  ثرى عمد إذا بلته الأمطار (maqayis); عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك (maqayis;tahdhib); عمد الثرى إذا بلله المطر وتعقد واجتمع من ندوته (sihah); عمد الثرى إذا كان تراكب بعضه على بعض وندي (tahdhib)
- **B011** gençliğinin dolgun çağında, gelişkin bedenli — gençliğinin dolgun çağında, gelişkin bedenli kişi
  العمد الشاب الممتلئ شبابا وهو العمداني وامرأة عمدانية ذات جسم وعبالة (maqayis); العمد الشاب الشديد الممتلئ شبابا والمرأة عمدانية (ayn); العمد الشاب الممتلىء شبابا وامرأة عمدانية (tahdhib)
- **B012** bundan daha fazlası veya şaşırtıcısı var mı — bundan daha fazlası mı, yoksa daha şaşırtıcısı mı
  أعمد من سيد قتله قومه (maqayis;sihah;tahdhib); هل زاد على سيد قتله قومه (maqayis;tahdhib); أعجب من سيد قتله قومه (maqayis;tahdhib); أنا أعمد من كذا أي أعجب منه (sihah)
- **B013** selin önünü kapatıp suyu biriktirme — selin önünü kapatıp suyu bir yerde toplamak
  عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة (tahdhib)
- **B014** yanından ayrılmadan bağlı kalma — ona bağlı kalıp yanından ayrılmamak
  حلس به وعرس به وعمد به ولزب به إذا لزمه (tahdhib)
- **B015** öfke ve onunla bağlantılı acılı sıkıntı — öfke veya öfkenin verdiği acılı sıkıntı
  العمد والضمد الغضب (tahdhib); عمد توجع من حزن أو غضب أو سقم (mufradat)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:7, and ## Buluşmalar) =====
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

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

