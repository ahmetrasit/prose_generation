Focus: 89:20. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_20/D.r13/context.md =====
# 89:20 — focus

وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا

Anchor translation (canonical reading, reference only):

Malı da çok büyük bir sevgiyle seviyorsunuz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَتُحِبُّونَ | أَحْبَبْ | ح ب ب | CONJ;V;PRON |
| 2 | ٱلْمَالَ | مَال | م و ل | DET;N |
| 3 | حُبًّا | حُبّ | ح ب ب | N |
| 4 | جَمًّا | جَمّ | ج م م | ADJ |


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
- 89:20 ◀ focus وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
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


===== _commentary/v16/work/89_20/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ح ب ب (root_000286) — identity root of وَتُحِبُّونَ (w1)

- **B001** tane, tohum ve taneye benzeyen tek parça — tahıl tanesi ve yenebilir bitki tohumu · tek tane, tohum veya taneye benzeyen parça · dolu tanesi
  الحبة واحد الحب (jamhara;sihah)؛ الحب والحبة في الحنطة والشعير وبزور الرياحين (maqayis;tahdhib;mufradat)؛ الحبة من الشيء القطعة منه وحب الغمام وحب المزن وحب قر والحب القرط من حبة واحدة (sihah;tahdhib)
- **B002** sevgi ve yeğleme — sevgi; nefretin karşıtı · iyi görülen şeye yönelen güçlü sevgi · sevmek veya sevdirmek · yeğlemek veya sevmeye yönelmek · birbirini sevmek
  الحب والمحبة اشتقاقه من أحبه إذا لزمه (maqayis)؛ أحببته نقيض أبغضته (ayn)؛ المحبة إرادة ما تراه أو تظنه خيرا (mufradat)؛ استحبوا أي آثروه عليه (mufradat)
- **B003** övgü, güçlü istek ve kabul bildiren kalıplar — ne güzel; ne iyi · en büyük isteğin bunu yapmaktır · peki, memnuniyetle ve baş üstüne
  حبذا حرفان حب وذا تقول حبذا زيد (ayn;sihah;tahdhib)؛ حبابك أن تفعل ذاك معناه غاية محبتك (ayn;sihah;tahdhib;mufradat)؛ الحبة بالضم الحب يقال نعم وحبة وكرامة (sihah)
- **B004** kalbin içindeki kara öz [kalıp] — kalbin kara iç noktası veya özü
  حبة القلب سويداؤه ويقال ثمرته (maqayis;sihah)؛ حبة القلب هي العلقة السوداء التي تكون داخل القلب (tahdhib)؛ حبة القلب تشبيها بالحبة في الهيئة (mufradat)
- **B005** devenin güçsüzlükten yerinden ayrılamaması — devenin güçsüzlükten durup yerinden ayrılamaması · devenin hastalık veya güçsüzlükten çökmesi
  المحب البعير الذي يحسر فيلزم مكانه (maqayis)؛ بعير محب وقد أحب إحبابا وهو أن يصيبه مرض أو كسر فلا يبرح من مكانه (sihah;tahdhib)؛ أحب البعير إذا حرن ولزم مكانه (mufradat)
- **B006** suyla dolmak veya doldurup dolulaştırmak — su içip dolmak veya suya kanmak · doldurup dolu hale getirmek
  تحبب الحمار إذا امتلأ من الماء وشربت الإبل حتى حببت (sihah)؛ أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره (tahdhib)
- **B007** iri küp ve iki kulplu küpün dört parçalı desteği — iri küp veya büyük saklama kabı · iki kulplu küpün dört parçalı ayağı
  الحب الجرة الضخمة ويجمع على حببة وحباب (ayn;tahdhib)؛ الحب الخابية فارسي معرب والجمع حباب وحببة (sihah)؛ الحب الخشبات الأربع التي توضع عليها الجرة ذات العروتين (ayn;tahdhib)
- **B008** su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy — su kabarcıkları, suyun ana kütlesi, dalgası veya yüzey çizgileri · ağaç üzerindeki çiy
  حباب الماء فقاقيعه الطافية (ayn;tahdhib)؛ حباب الماء معظمه (maqayis;ayn;sihah;tahdhib)؛ حباب الماء موجه والطرائق التي في الماء (tahdhib)؛ الحباب من الماء النفاخات تشبيها به (mufradat)؛ الحباب الطل على الشجر (tahdhib)
- **B009** düzenli diş dizisi ve beyaz tükürük parıltısı — düzenli diş dizisi veya dişlerdeki beyaz tükürük parıltısı
  الحبب تنضد الأسنان (maqayis;ayn;sihah;tahdhib)؛ الحبب تنضد الأسنان تشبيها بالحب (mufradat)؛ حبب الفم ما يتحبب من بياض الريق على الأسنان (tahdhib)
- **B010** kısa veya küçük yapılı; develerde cılız — kısa boylu veya küçük bedenli kimse · cılız develer
  الحبحاب الرجل القصير (maqayis)؛ الحباحب الصغار (maqayis;sihah)؛ الحبحاب الصغير الجسم (tahdhib)؛ إبل حبحبة مهازيل (tahdhib)
- **B011** yararsız zayıf kıvılcım veya gece ışıldayan böcek — yararsız zayıf kıvılcım veya gece ışıldayan böcek · zayıf kıvılcımın tutuşması
  نار الحباحب ما اقتدحت من شرار النار في الهواء من تصادم الحجارة (ayn;tahdhib)؛ نار الحباحب ما أورت الخيل لا ينتفع به (maqayis;sihah;tahdhib)؛ ذباب يطير بالليل له شعاع كالسراج (ayn;sihah;tahdhib)
- **B012** yılan; yılanla ilişkilendirilen kötücül ruh adı — yılan veya yılanla ilişkilendirilen kötücül ruh adı
  ومما شذ عن الباب الحباب وهو الحية (maqayis)؛ الحباب أيضا الحية (sihah)؛ الحباب الحية وإنما قيل الحباب اسم شيطان لأن الحية يقال لها شيطان (tahdhib)

## م و ل (root_001457) — identity root of ٱلْمَالَ (w2)

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ج م م (root_000261) — identity root of جَمًّا (w4)

- **B001** çoğalıp birikerek doluluğa ulaşma — çoğalıp birikmek · çok, bol · kuyuda biriken bol su · kuyuda suyun toplandığı yer veya orada biriken su · suyu bol kuyu veya kuyudaki su bolluğu · ölçeğin ağzına dek dolması veya dolmaya yaklaşması · içindeki ölçü ağzına kadar ulaşmış kap
  كثرة الشيء واجتماعه (maqayis)؛ جم الشيء واستجم أي كثر (ayn;tahdhib)؛ جم المال وغيره إذا كثر والجم الكثير (sihah)؛ أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ (jamhara)؛ جمة الماء معظمه ومجتمعه (mufradat)
- **B002** dinlenip gücünü yeniden toplama — dinlenme ve yorgunluğun geçmesi · atın yorgunluğu geçmek veya güç toplaması için onu dinlendirmek · kendini bir süre dinlendir · koşu gücünü her düşüşten sonra yeniden toplayan at
  الجمام الراحة (maqayis;ayn;sihah)؛ جم الفرس إذا ذهب إعياؤه (sihah;tahdhib)؛ جم الفرس وأجم إذا ترك أن يركب (maqayis)؛ أجمم نفسك يوما أو يومين (sihah;tahdhib)؛ أصل الكلمة من الجمام أي الراحة للإقامة وترك تحمل التعب (mufradat)
- **B003** bir araya gelmiş kalabalık insan bütünü — öldürme karşılığı ödenecek bedeli istemek için toplanan grup · geride kimse kalmadan gelen bütün kalabalık · alt boyları birleştiren büyük boylar veya onların önderleri
  الجمة القوم يسألون في الدية (maqayis;jamhara)؛ الجماء الغفير الجماعة من الناس (maqayis;ayn;sihah;mufradat)؛ جاءوا جما غفيرا وجماء أي بجماعتهم (tahdhib)؛ جماجم العرب القبائل التي تجمع البطون (maqayis;sihah)؛ جماجم العرب رؤساؤهم (tahdhib)
- **B004** başta toplanmış saç ya da beyni saran kafatası — başta toplanmış saç kütlesi · baş saçı uzun adam · kafatası ve ona bağlı baş kemikleri
  الجمة مجتمع شعر ناصيته (maqayis)؛ الجمة الشعر (ayn;jamhara;tahdhib)؛ الجمة بالضم مجتمع شعر الرأس (sihah)؛ ما اجتمع من شعر الناصية (mufradat)؛ الجمجمة عظم الرأس المشتمل على الدماغ (sihah)؛ الجمجمة القحف وما تعلق به من العظام (ayn;tahdhib)
- **B005** toprağı örten, henüz olgunlaşmamış genç bitki örtüsü — toprağı örten, henüz tam gelişmemiş genç bitki veya ot · toprağın genç bitki örtüsü tamamlanmak veya bitki toplu bir baş oluşturmak
  الجميم مجتمع من البهمى (maqayis)؛ الجميم النبات إذا تخطى الأرض (ayn)؛ الجميم ما تجمم من البقل إذا أراد أن يثمر (jamhara)؛ الجميم النبت الذي طال بعض الطول ولم يتم (sihah)؛ جميم حسن لنبت قد غطى الأرض ولم يتم بعد (tahdhib)
- **B006** beklenen araçtan veya çıkıntıdan yoksun olma — savaşta yanında mızrağı olmayan kişi · boynuzsuz koyun · duvarlarının üstünde mazgal bulunmayan yapı · dirsekleri dışarı doğru çıkıntı yapmayan kadın
  الأجم الذي لا رمح معه في الحرب (maqayis;ayn;sihah;tahdhib)؛ الشاة الجماء التي لا قرن لها (maqayis;ayn;sihah;tahdhib;mufradat)؛ بنيان أجم لا شرف له (sihah)؛ المساجد جما أي لا يكون لجدرانها شرف (maqayis;tahdhib)؛ امرأة جماء المرافق (sihah)
- **B007** yaklaşıp vakti gelmek — iş yaklaşmak, hazır olmak veya vakti gelmek · birinin gelişi yaklaşmak ve vakti gelmek
  أجم الشيء دنا (maqayis)؛ أجمت الحاجة أي دنت وحاجت (ayn)؛ أجم الأمر إذا دنا وحضر وأجم الفراق إذا حان (sihah)؛ أجمت الحاجة إذا دنت وحانت وأجم الفراق إذا دنا (tahdhib)
- **B008** sözü açık ve anlaşılır biçimde söylememe — sözünü açık söylememek veya anlaşılmaz konuşmak
  الجمجمة ألا تبين كلامك من غير عي (ayn)؛ جمجم الرجل وتجمجم إذا لم يبين كلامه (sihah)؛ الجمجمة ألا تبين كلامك من عي (tahdhib)
- **B009** göğsü geniş ve kolu açık olma [kalıp] — göğsü geniş, eli kolu rahat · göğsü dar
  رجل رحب المجم أي رحب الصدر (jamhara)؛ فلان واسع المجم إذا كان واسع الصدر رحب الذراع (tahdhib)؛ ضيق المجم (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:20, and ## Buluşmalar) =====
## Pay, sofra ve ağzına kadar dolan kap

Rızık bir paydır: {ar:الرزق يقال للعطاء الجاري وللنصيب, tr:er-rızku yukâlu li'l-atâi'l-câri ve li'n-nasîb, gloss:rızık, akıp gelen bağış için de pay için de söylenir, source:"ر ز ق,B001"}. Her şeyin bir ölçüsü vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir ölçüsü ve bir süresi vardır, source:"ق د ر,B001"}. Kur'an da geçimi kendisinin bölüştürdüğünü söyler: {ar:نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ, tr:nahnu kasemnâ beynehum maîşetehum, gloss:aralarında geçimlerini biz bölüştürdük, source:43:32}, {ar:ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ, tr:Allâhu yebsutu'r-rızka li-men yeşâu ve yakdir, gloss:Allah rızkı dilediğine genişletir ve daraltır, source:13:26}. Beşinci ayetteki kasem kelimesinin kökü bu bölüştürmeyi adlandırır, mirasın sahiplerine ayrılmasını da içine alarak: {ar:إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما, tr:ifrâzu'n-nasîbi ve kısmetu'l-mîrâsi ve'l-ğanîmeti tefrîkuhumâ alâ erbâbihimâ, gloss:payı ayırmak; miras ve ganimeti bölmek, onları sahiplerine dağıtmaktır, source:"ق س م,B003"}. Kur'an'ın miras hükmü surenin sofrasını tek bir ayette kurar: {ar:وَإِذَا حَضَرَ ٱلْقِسْمَةَ أُو۟لُوا۟ ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينُ فَٱرْزُقُوهُم مِّنْهُ, tr:ve izâ hadara'l-kısmete ulu'l-kurbâ ve'l-yetâmâ ve'l-mesâkînu ferzukûhum minh, gloss:paylaştırmada akrabalar, yetimler ve yoksullar hazır bulunursa onlara da ondan rızık verin, source:4:8}. Paylaştırma, yetim, yoksul ve rızık: on altıncı ayetle on dokuzuncu ayet arasındaki bütün öğeler buradadır. Payın kendisi de konmuştur: {ar:نَصِيبًۭا مَّفْرُوضًۭا, tr:nasîben mefrûdâ, gloss:belirlenmiş bir pay, source:4:7}.

On sekizinci ayet bu sofraya kimin çağrılmadığını söyler: {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}. Fiilin kalıbı karşılıklıdır: {ar:والمحاضة أن يحث كل واحد منهما صاحبه, tr:ve'l-muhâdda en yehusse kullu vâhidin minhumâ sâhibeh, gloss:muhâdda, ikisinden her birinin ötekini teşvik etmesidir, source:"ح ض ض,B001"}. Kınanan şey yalnız tek tek kişilerin cimriliği değildir. Topluluğun birbirini yoksula yöneltmeyi bırakmasıdır. Yemek, birinin istediği şeydir: {ar:استطعمه سأله أن يطعمه, tr:istat'amehû seelehû en yut'imeh, gloss:ondan yemek istedi, source:"ط ع م,B002"}. Yoksul da zayıf düşmüş kişidir: {ar:المسكين الفقير وقد يكون بمعنى الذلة والضعف, tr:el-miskînu'l-fakîr, ve kad yekûnu bi-ma'ne'z-zilleti ve'd-da'f, gloss:miskin fakirdir; düşkünlük ve zayıflık anlamına da gelir, source:"س ك ن,B006"}. Aynı kök azığı, insanın yerinde kalabilmesini sağlayan şey olarak adlandırır: {ar:قيل للقوت سكن لأن المكان به يسكن, tr:kîle li'l-kûti sekenun li-enne'l-mekâne bihî yusken, gloss:azığa seken denir, çünkü bir yerde onunla oturulur, source:"س ك ن,B010"}. Yoksulun payını vermek, onun yerinde durabilmesini sağlamaktır. Kur'an aynı cümleyi başka iki sahnede tekrarlar. Biri dini yalanlayanın tarifidir: {ar:فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ, tr:fe-zâlike'llezî yeduu'l-yetîm, gloss:işte o, yetimi itip kakandır, source:107:2}, {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmez, source:107:3}. Öteki kitabı sol eline verilen kişinin zincirlenme sebebidir {source:69:34}. Sarp yokuş da açlık gününde yakın bir yetimi ya da toprağa düşmüş bir yoksulu doyurmaktır: {ar:أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ, tr:ev it'âmun fî yevmin zî mesğabeh, gloss:ya da açlık gününde doyurmak, source:90:14}, {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabeh, gloss:yakını olan bir yetimi, source:90:15}, {ar:أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ, tr:ev miskînen zâ metrabeh, gloss:ya da toprağa düşmüş bir yoksulu, source:90:16}.

On dokuzuncu ayet sofranın öbür ucunu gösterir: {ar:وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا, tr:ve te'kulûne't-turâse eklen lemmâ, gloss:mirası silip süpürerek yiyorsunuz, source:89:19}. Miras, bir topluluğa ait olanın başkalarına geçmesidir: {ar:أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب, tr:en yekûne'ş-şey'u li-kavmin summe yasîra ilâ âharîne bi-nesebin ev sebeb, gloss:bir şeyin bir topluluğa ait olup sonra soy ya da başka bir sebeple başkalarına geçmesi, source:"و ر ث,B001"}. Miras geçerken paylara ayrılmalıdır. Lemm ise ayırmadan hepsini toplamaktır: {ar:لممته أجمع حتى أتيت على آخره, tr:lememtuhû ecmaa hattâ eteytu alâ âhirih, gloss:sonuna kadar hepsini toplayıp aldım, source:"ل م م,B001"}. Yemek fiili zayıfların malını yemeyi de anlatır: {ar:فلان يستأكل الضعفاء أي يأخذ أموالهم, tr:fulânun yeste'kilu'd-duafâe ey ye'huzu emvâlehum, gloss:falanca zayıfları yiyor, yani mallarını alıyor, source:"ء ك ل,B004"}. Kur'an yetimlerin malı için şöyle uyarır: {ar:وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ, tr:ve lâ te'kulû emvâlehum ilâ emvâlikum, gloss:onların mallarını kendi mallarınıza katarak yemeyin, source:4:2}. O malın aslında ne olduğunu da gösterir: {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:innemâ ye'kulûne fî butûnihim nârâ, gloss:onlar karınlarına ancak ateş yerler, source:4:10}. Aynı fiil ateşin işidir: {ar:أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi, source:"ء ك ل,B005"}. Yiyen, yirmi üçüncü ayette getirilen ateşle karşılaşır. Miras da sonunda asıl sahibine döner: {ar:يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه, tr:yebkâ ve yefnâ men sivâhu fe-yerciu mâ kâne milke'l-ibâdi ileyh, gloss:O kalır, O'ndan başkası yok olur ve kulların mülkü O'na döner, source:"و ر ث,B004"}. Kur'an bunu şöyle söyler: {ar:إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا وَإِلَيْنَا يُرْجَعُونَ, tr:innâ nahnu neriçu'l-arda ve men aleyhâ ve ileynâ yurceûn, gloss:yere ve üzerindekilere biz varis oluruz ve onlar bize döndürülür, source:19:40}. Bir başka ayet de göklerin ve yerin mirasının Allah'a ait olduğunu hatırlatarak harcamaya çağırır {source:57:10}.

Yirminci ayet yığılan malı bir kaba koyar: {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا, tr:ve tuhibbûne'l-mâle hubben cemmâ, gloss:malı aşırı bir sevgiyle seviyorsunuz, source:89:20}. Cemm bir ölçeğin ağzına kadar dolmasıdır: {ar:أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ, tr:a'taytuhû cumâme'l-mekkûki ve cimâmehû izâ kâraba en yemtelî', gloss:ölçeği ağzına kadar, neredeyse taşacak kadar doldurup verdim, source:"ج م م,B001"}. Suyun yığılmış kütlesi de böyle adlandırılır: {ar:جمة الماء معظمه ومجتمعه, tr:cemmetu'l-mâi mu'zamuhû ve muctemeuh, gloss:suyun cemmesi, en büyük ve toplanmış kısmıdır, source:"ج م م,B001"}. Sevgi kelimesinin kökü de dolmayı ve kabı adlandırır: {ar:وحببته فتحبب إذا ملأته للسقاء وغيره, tr:ve habebtuhû fe-tehabbebe izâ mele'tuhû li's-sikâi ve ğayrih, gloss:su tulumunu ve benzerini doldurdum, doldu, source:"ح ب ب,B006"}, {ar:الحب الجرة الضخمة, tr:el-hubb el-cerratu'd-dahme, gloss:hubb, iri küptür, source:"ح ب ب,B007"}. Aynı harfler tahılı da adlandırır: {ar:الحب والحبة في الحنطة والشعير, tr:el-habbu ve'l-habbe fi'l-hıntati ve'ş-şaîr, gloss:habb, buğday ve arpa tanesidir, source:"ح ب ب,B001"}. Ayette anlam aşırı sevgidir. Yanında ağzına kadar dolmuş bir küp duyulur, hem de yoksulun istediği tahılla dolu bir küp. On ikinci ayetteki çoğaltma fiili de bu yarışı taşır: {ar:المكاثرة والتكاثر التباري في كثرة المال والعز, tr:el-mukâsera ve't-tekâsur et-tebârî fî kesreti'l-mâli ve'l-izz, gloss:mal ve itibar çokluğunda yarışmak, source:"ك ث ر,B002"}. Kur'an bu dolduranı birkaç sahnede gösterir: {ar:أَلْهَىٰكُمُ ٱلتَّكَاثُرُ, tr:elhâkumu't-tekâsur, gloss:çoğaltma yarışı sizi oyaladı, source:102:1}. Bir diğeri malı toplayıp sayandır: {ar:ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ, tr:ellezî cemea mâlen ve addedeh, gloss:mal toplayıp onu sayan, source:104:2}, {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kılacağını sanır, source:104:3}. Ateş de toplayıp istifleyeni çağırır: {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve cemea fe-ev'â, gloss:toplayıp kaba istifleyen, source:70:18}. Sevginin sofraya dönen biçimi de Kur'an'dadır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut'imûne't-taâme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, ona olan sevgilerine rağmen yoksula, yetime ve esire yedirirler, source:76:8}. Malın da: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ, tr:ve âte'l-mâle alâ hubbihî zevi'l-kurbâ ve'l-yetâmâ ve'l-mesâkîn, gloss:malı, ona olan sevgisine rağmen akrabalara, yetimlere ve yoksullara veren, source:2:177}. Sevgi aynıdır, ama burada kap dolmaz, boşaltılır. Ağzına kadar dolmuş küpün sonu da Kur'an'da gösterilir. Kitabı sol eline verilen şöyle der: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ ۜ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}. Cehennem ise hiç dolmayan bir kaptır: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu?" deriz, o da "daha yok mu?" der, source:50:30}.

Kaynaklar: 89:5 قَسَمٌۭ ق س م B003; 89:12 فَأَكْثَرُوا۟ ك ث ر B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B001; 89:18 تَحَٰٓضُّونَ ح ض ض B001; 89:18 طَعَامِ ط ع م B002; 89:18 ٱلْمِسْكِينِ س ك ن B006; 89:18 ٱلْمِسْكِينِ س ك ن B010; 89:19 وَتَأْكُلُونَ ء ك ل B004; 89:19 وَتَأْكُلُونَ ء ك ل B005; 89:19 ٱلتُّرَاثَ و ر ث B001; 89:19 ٱلتُّرَاثَ و ر ث B004; 89:19 لَّمًّۭا ل م م B001; 89:20 حُبًّۭا ح ب ب B001; 89:20 وَتُحِبُّونَ ح ب ب B006; 89:20 حُبًّۭا ح ب ب B007; 89:20 جَمًّۭا ج م م B001

## Yol, binek ve dönüş

Surenin kelimeleri bir yolculuğun aşamalarını sırayla taşır. Dördüncü ayette gece yürüyüşü başlar: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:gece yürüyüşü, source:"س ر ي,B001"}. Kur'an bu kökü kul ve gece kelimeleriyle aynı cümlede kullanır: {ar:سُبْحَٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًۭا, tr:subhâna'llezî esrâ bi-abdihî leylen, gloss:kulunu geceleyin yürüten Allah'ı tesbih ederim, source:17:1}. Dokuzuncu ayetteki fiilin yanında ülke ülke dolaşan yolcu duyulur: {ar:رجل جواب إذا كان قطاعا للبلاد, tr:raculun cevvâbun izâ kâne kattâan li'l-bilâd, gloss:cevvâb, ülkeleri durmadan aşan adamdır, source:"ج و ب,B002"}. On beşinci ve on altıncı ayetlerdeki sınav fiilinin yanında da yolun bineği yıpratması duyulur: {ar:ناقة بلو سفر أبلاها السفر, tr:nâkatun ilvu seferin eblâhe's-sefer, gloss:yolculuğun yıprattığı dişi deve, source:"ب ل و,B001"}. Elbisenin eskimesi de aynı köktendir: {ar:بلي الثوب يبلى بلى وبلاء, tr:beliye's-sevbu yeblâ bilen ve belâ', gloss:elbise eskidi, yıprandı, source:"ب ل و,B001"}. Ayette anlam sınamaktır. Yanında kullanıldıkça yıpranan, yürüdükçe tükenen bir binek duyulur. Sınavın, insanın kendisine ait sandığı şeyi aşındırdığı da duyulur.

Yolculuğun karşısında yere yapışmak vardır. Yirminci ayetteki sevgi kelimesi bir şeye yapışıp kalmakla açıklanır: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbe iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi bir şeye yapışıp ondan ayrılmamaktan türer, source:"ح ب ب,B002"}. Aynı fiil inatla yerinden kalkmayan deveyi de anlatır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-baîru izâ harana ve lezime mekâneh, gloss:deve inat edip yerinden kalkmayınca "ehabbe" denir, source:"ح ب ب,B005"}. Malı yapışarak seven insan çöküp kalmış bir bineğe benzer. Sekizinci ve on birinci ayetlerdeki "ülkeler" kelimesi de yerleşip kalmayı taşır: {ar:بلد بالمكان أقام به فهو بالد, tr:belede bi'l-mekâni ekâme bih, gloss:bir yerde kalıp yerleşti, source:"ب ل د,B009"}, {ar:بلد الرجل بالأرض إذا لزق بها, tr:belede'r-raculu bi'l-ardı izâ leziga bihâ, gloss:adam yere yapıştı, source:"ب ل د,B010"}. Devenin göğsünü yere koyup çökmesi de aynı köktendir: {ar:وضعت الناقة بلدتها بالأرض إذا بركت, tr:vedaati'n-nâkatu beldetehâ bi'l-ardı izâ berakat, gloss:deve göğsünü yere koyup çöktü, source:"ب ل د,B002"}. Yirmi birinci ayetteki yer kelimesinin kökü yere ağırlaşmayı da söyler: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerrudu eydan et-tesâkulu ile'l-ard, gloss:teerrud, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}. Onuncu ayetteki kazık ayağı yere çakar, yirmi altıncı ayetteki bağ ise bağlar. Kur'an bu ağırlığı bir çağrı sahnesinde adlandırır. Allah yolunda harekete geçmeye çağrılan müminlere şöyle seslenir: {ar:ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ, tr:issâkaltum ile'l-ard, e-radîtum bi'l-hayâti'd-dunyâ mine'l-âhira, gloss:yere çakılıp kaldınız; dünya hayatına ahiretten daha mı razı oldunuz, source:9:38}. Yer, razı olmak ve hayat: surenin sonundaki kelimeler burada ters yönde dizilmiştir. Ayetlerine rağmen yere saplanıp kalan adam da şöyle anlatılır: {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ, tr:ve lâkinnehû ahlede ile'l-ardı ve'ttebea hevâh, gloss:ama o yere saplanıp kaldı ve hevesine uydu, source:7:176}.

Yolun sonu dönüştür. Altıncı ayette adı geçen Âd, Arapçada dönüş anlamındaki kökün altında sayılır: {ar:عاد قبيلة وهم قوم هود, tr:Âd kabîle, ve hum kavmu Hûd, gloss:Âd bir kabiledir, Hûd'un kavmidir, source:"ع و د,B012"}. Aynı kök varılacak yeri de adlandırır: {ar:المعاد المصير والمرجع, tr:el-meâd el-masîru ve'l-merci', gloss:meâd, varılacak ve dönülecek yerdir, source:"ع و د,B002"}. Âd bir özel addır ve bu anlamı taşımaz, yalnız harfleri dönüşü çağrıştırır. Kur'an Peygamber'e dönüş yerini vaat eder: {ar:لَرَآدُّكَ إِلَىٰ مَعَادٍۢ, tr:le-râdduke ilâ meâd, gloss:seni elbette dönüş yerine döndürecektir, source:28:85}. Yirmi yedinci ayet yolcuyu durulmuş olarak karşılar: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetuhe'n-nefsu'l-mutmainne, gloss:ey huzura kavuşmuş can, source:89:27}. Huzur, sarsıntıdan sonra gelen dinginliktir: {ar:الطمأنينة والاطمئنان السكون بعد الانزعاج, tr:et-tume'nîne ve'l-itmi'nân es-sukûnu ba'de'l-inzi'âc, gloss:itminan, sarsıntıdan sonraki dinginliktir, source:"ط م ء ن,B001"}. Kur'an bu dinginliğin kaynağını da söyler: {ar:أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ, tr:elâ bi-zikri'llâhi tatmainnu'l-kulûb, gloss:bilin ki kalpler ancak Allah'ı anmakla huzura kavuşur, source:13:28}. Yirmi sekizinci ayetteki çağrı şöyledir: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ, tr:irciî ilâ rabbiki, gloss:Rabbine dön, source:89:28}. Dönmek, başlanılan yere geri gitmektir: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûu'l-avdu ilâ mâ kâne minhu'l-bed', gloss:rücû, başlangıç noktasına dönmektir, source:"ر ج ع,B001"}. Aynı kök, bir yolculuktan ötekine geri gönderilen yorgun hayvanı da adlandırır: {ar:الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال, tr:er-recî' mine'd-devâbbi mâ raca'tehû min seferin ilâ sefer, ve huve'l-kâll, gloss:recî', bir yolculuktan ötekine döndürülen yorgun hayvandır, source:"ر ج ع,B014"}. Çağrılan can ise yeni bir yola gönderilmez. Yolun bittiği yere döndürülür. Kur'an insanın bütün çabasını bu yöne bağlar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe-mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Varılacak yer de bir yerleşmedir: {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ, tr:ilâ rabbike yevmeizini'l-mustekarr, gloss:o gün varılıp karar kılınacak yer Rabbinin huzurudur, source:75:12}. Azan insana da aynı söz söylenir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş Rabbinedir, source:96:8}. Sınanıp musibete uğrayanların sözü de dönüşle biter: {ar:إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ, tr:innâ li'llâhi ve innâ ileyhi râciûn, gloss:biz Allah'a aitiz ve O'na döneceğiz, source:2:156}. Yorgun binek imgesi ile dönüş çağrısı burada aynı insanda birleşir. Dönüşün tersi de Kur'an'dadır. Ölüm gelince inkârcı geri gönderilmeyi ister: {ar:رَبِّ ٱرْجِعُونِ, tr:rabbi'rciûn, gloss:Rabbim, beni geri gönderin, source:23:99}. Cevap ise surenin iki kez kullandığı kelimedir: {ar:كَلَّآ ۚ إِنَّهَا كَلِمَةٌ هُوَ قَآئِلُهَا, tr:kellâ, innehâ kelimetun huve kâiluhâ, gloss:hayır, bu yalnızca onun söylediği bir sözdür, source:23:100}. Yolun en son aşaması giriştir: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Kur'an bu girişi kapılar açılırken bölük bölük sürülen bir kafile olarak da gösterir: {ar:وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا, tr:ve sîka'llezîne'ttekav rabbehum ile'l-cenneti zumerâ, gloss:Rablerinden sakınanlar bölük bölük cennete sürülür, source:39:73}.

Kaynaklar: 89:4 يَسْرِ س ر ي B001; 89:6 بِعَادٍ ع و د B002; 89:6 بِعَادٍ ع و د B012; 89:8 ٱلْبِلَٰدِ ب ل د B002; 89:8 ٱلْبِلَٰدِ ب ل د B009; 89:11 ٱلْبِلَٰدِ ب ل د B010; 89:9 جَابُوا۟ ج و ب B002; 89:15 ٱبْتَلَىٰهُ ب ل و B001; 89:20 وَتُحِبُّونَ ح ب ب B002; 89:20 وَتُحِبُّونَ ح ب ب B005; 89:21 ٱلْأَرْضُ ء ر ض B006; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B001; 89:28 ٱرْجِعِىٓ ر ج ع B001; 89:28 ٱرْجِعِىٓ ر ج ع B014; 89:29 فَٱدْخُلِى د خ ل B001

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

