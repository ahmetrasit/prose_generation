Focus: 89:22. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_22/D.r13/context.md =====
# 89:22 — focus

وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا

Anchor translation (canonical reading, reference only):

Rabbin ve melek sıra sıra geldiğinde,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَجَآءَ | جَآءَ | ج ي ء | CONJ;V |
| 2 | رَبُّكَ | رَبّ | ر ب ب | N;PRON |
| 3 | وَٱلْمَلَكُ | مَلَك | م ل ك | CONJ;DET;N |
| 4 | صَفًّا | صَفّ | ص ف ف | N |
| 5 | صَفًّا | صَفّ | ص ف ف | N |


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
- 89:22 ◀ focus وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_22/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ي ء (root_000281) — identity root of وَجَآءَ (w1)

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · geliş; varış · bir kez geliş veya geliş biçimi · sık sık iyilik getiren · iyi ki geldin
  جاء يجيء مجيئا (maqayis;mufradat)؛ جاء فلان يجيء جيئة إذا جاء مرة واحدة وجيئة حسنة (jamhara)؛ المجئ: الاتيان، جاء يجئ جيئة، وجئت مجيئا حسنا (sihah)؛ المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا (mufradat)
- **B002** gelip gitmede üstün gelmek [kalıp] — benimle sık gelme yarışına girdi, ben de onu geçtim
  جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ وجاءانى على فاعلنى فجئته أجيئه، أي غالبني بكثرة المجئ فغلبته (sihah)
- **B003** suyun biriktiği çukur veya yer — suyun biriktiği yer veya büyük çukur · tuzlu ya da idrar karışmış kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره ويقال هي جيئة (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون، والموضع الذي يجتمع فيه الماء، والحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ جية من ماء أي ماء ناقع خبيث (tahdhib)
- **B004** bir şeyi getirmek veya hazır bulundurmak — sık sık iyilik getiren · bir şeyi getirmek veya hazır bulundurmak · onu getirmek
  أجأته، أي جئت به (sihah)؛ جاءه بكذا وأجاءه، وجاء بكذا: استحضره (mufradat)
- **B005** birini bir şeye zorlamak [kalıp] — onu belirli bir şeye zorlamak · seni buna gerek duyar duruma düşürmek
  أجأته إلى كذا بمعنى ألجأته واضطررته إليه (sihah)؛ أجاءها المخاض إلى جذع النخلة، قيل: ألجأها، وإنما هو معدى عن جاء (mufradat)
- **B006** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح، يقال: جاءت جائية الجراح (tahdhib)

## ج ي ء (root_000282) — identity root of وَجَآءَ (w1)

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ر ب ب (root_000532) — identity root of رَبُّكَ (w2)

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## م ل ك (root_001444) — identity root of وَٱلْمَلَكُ (w3)

- **B001** güçlü ve tutarlı biçimde bir arada durma — hamuru sıkıca yoğurup kıvamlandırmak · sürgünü kabuğuyla kurutup sertleştirmek · kendini tutmak; dayanmak · bir şeyi ayakta tutan iç sağlamlık
  أصل صحيح يدل على قوة في الشيء وصحة (maqayis)؛ أملك عجينه قوي عجنه وشده (maqayis)؛ ملكت العجين إذا شددت عجنه (sihah)؛ ملك النبعة صلبها (sihah)؛ العجين إذا كان متماسكا متينا مملوك ومملك (tahdhib)؛ حائط ليس له ملاك أي تماسك (mufradat)
- **B002** sahiplik ve tasarruf yetkisi — bir şeye sahip olup onu tasarrufunda bulundurmak · mülkiyet; sahip olunan mal veya hak · kişinin elinin altında ve sahipliğinde bulunan şey · köleleştirilmiş kişi · köleleştirilmiş kişilere iyi davranma · özgür doğmuşken tutsak edilip köleleştirilen kişi · boşanma kararını eşin tasarrufuna bırakmak
  ملك الإنسان الشيء يملكه ملكا (maqayis)؛ الملك ما ملكت اليد من مال وخول (ayn;tahdhib)؛ ملكت الشيء أملكه ملكا (sihah)؛ وملكه المال والملك فهو مملك (sihah)؛ أملكت فلانة أمرها إذا جعل أمر طلاقها بيدها (tahdhib)؛ المملوك يختص في التعارف بالرقيق من الأملاك (mufradat)
- **B003** hükümdarlık ve kamusal egemenlik — hükümdar · hükümdar; egemen yönetici · hükümranlık; kamusal egemenlik · ilahi mutlak hükümranlık · hükümdarın yönetim alanı ve ülkesi · birini başlarına hükümdar yapmak
  والاسم الملك لأن يده فيه قوية صحيحة (maqayis)؛ الملك لله المالك المليك (ayn)؛ الملكوت ملك الله وملكوت الله سلطانه (ayn)؛ الملكوت من الملك (sihah)؛ المملكة سلطان الملك في رعيته (ayn;tahdhib)؛ له ملكوت العراق وعزه وسلطانه وملكه (tahdhib)؛ الملك هو المتصرف بالأمر والنهي في الجمهور (mufradat)؛ ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا (tahdhib)
- **B004** evlilik akdi kurma — evlilik akdi; evlendirme · kadınla evlenmek
  كنا في إملاك فلان أي أملكناه امرأته (maqayis)؛ الإملاك التزويج قد أملكوه وملكوه أي زوجوه (ayn)؛ ملكت المرأة تزوجتها (sihah)؛ أملكنا فلانا فلانة إذا زوجناه إياها (sihah)؛ شهدنا إملاك فلان وملاكه وملاكه (tahdhib)؛ الملاك التزويج وأملكوه زوجوه (mufradat)
- **B005** işi ayakta tutan temel dayanak [kalıp] — işin dayandığı temel unsur · kalp bedenin temel dayanağıdır
  ملاك الأمر ما يعتمد عليه (ayn)؛ القلب ملاك الجسد (ayn;sihah;mufradat)؛ هذا ملاك الأمر وملاكه أي صلاحه (tahdhib)
- **B006** yolun veya yerin orta ya da ana kesimi — yolun ortası veya ana kesimi · vadinin sınırı veya orta kesimi · yerleşimin ortası veya büyük kesimi
  ملك الطريق أيضا وسطه (sihah)؛ خل عن ملك الطريق وملك الوادي وملكه وملكه أي حده ووسطه (tahdhib)؛ الزم ملك الطريق أي وسطه (tahdhib)؛ أراد بالمملكة وسطها وملك الطريق معظمه ووسطه (tahdhib)
- **B007** işleri ve yaşamı sürdüren su kaynağı [kalıp] — işini yürütmesini sağlayan su · hiç suyu yok · sularımız geçimimizi ayakta tutar
  والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)؛ الماء ملك أمر أي يقوم به الأمر (sihah)؛ الماء ملك أمره (tahdhib)؛ الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر (tahdhib)؛ ماله ملك ولا نقر أي ما له ماء (tahdhib)؛ مياهنا ملوكنا ومات فلان عن ملوك كثيرة (tahdhib)
- **B008** hayvanlarda önden gidip yön veren unsur [kalıp] — arı topluluğunun önderi · bineğin ön ayakları ve yönlendirici kısmı · deve ve koyun sürüsünün öncüsü
  مليك النحل يعسوبها (sihah)؛ ملك الدابة قوائمها وهاديها (sihah;tahdhib)؛ جاءنا تقوده ملكه يعني قوائمه وهاديه (tahdhib)؛ ملك الإبل والشاء ما يتقدم ويتبعه سائره (mufradat)
- **B009** ilahi haberci varlık — 
  الملك واحد الملائكة إنما هو تخفيف الملأك والأصل مألك (ayn)؛ مألك من الألوك وهو الرسالة (ayn)؛ الملك من الملائكة واحد وجمع (sihah)؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة (sihah)؛ الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك (tahdhib)

## ص ف ف (root_000871) — identity root of صَفًّا (w4)

- **B001** düz bir sıra oluşturma — düz çizgi üzerinde yan yana duran ögelerden oluşan sıra · yan yana sıraya dizmek · yan yana sıraya girmek · sıra halinde duran; kanatlarını açıp sabit tutan · savaş sırasının kurulduğu mevki · sıra halinde dizilmiş
  الصف معروف (ayn;tahdhib); الصف أن تجعل الشيء على خط مستو (mufradat); صففت القوم فاصطفوا (ayn;sihah;tahdhib); المصف الموقف والجمع المصاف (ayn;sihah;tahdhib); الصافات صفا يعني الملائكة (mufradat;tahdhib); الطير الصواف التي تصف أجنحتها فلا تحركها (ayn;tahdhib); البدن الصواف التي تصفف ثم تنحر (ayn;tahdhib)
- **B002** bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve — bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve · dişi deveyi tek sağımda iki veya üç kaba sağma
  الصفوف الناقة التي تجمع بين محلبين في حلبة (maqayis;tahdhib); الصف أن تحلب الناقة في محلبين أو ثلاثة تصف بينها (sihah); ناقة صفوف للتي تصف أقداحا من لبنها (sihah); الصفوف ناقة تصف بين محلبين فصاعدا لغزارتها (mufradat); الصفوف أيضا التي تصف يديها عند الحلب (maqayis;sihah;tahdhib)
- **B003** kurutmak ya da közlemek için sıra sıra serilmiş et — güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmiş et · eti şeritlere ayırıp sıra sıra sermek · eti genişletip inceltecek biçimde dilimleme
  الصفيف قال قوم هو القديد (maqayis); اللحم يحمل في الأسفار طبيخا أو شواء فلا ينضج (maqayis); الصفيف القديد اذا شر في الشمس (ayn;tahdhib); الصفيف ما صف من اللحم على الجمر لينشوي (sihah); صففت اللحم قددته وألقيته صفا صفا (mufradat); التصفيف نحو التشريح (tahdhib)
- **B004** yapı ya da eyer bölümü — yapıda ya da eyerde bulunan bölüm veya düzenek · hayvan için eyer düzeneği yapmak
  الصفة من البنيان والسرج ايضا (ayn); صفة الدار والسرج واحدة الصفف (sihah); صفة السرج (tahdhib); صففت للدابة صفة أي عملتها له (tahdhib); الصفة من البنيان وصفة السرج (mufradat)
- **B005** düz ve pürüzsüz arazi — düz ve pürüzsüz, kimi kullanımda bitkisiz arazi · düz ve pürüzsüz araziler
  الصفصف وهو المستوي من الأرض (maqayis); الصفصف الفلاة المستوية الملساء (ayn); الصفصف المستوى من الأرض (sihah); الصفصف الذي لا نبات فيه (tahdhib); الصفصف القرعاء (tahdhib); الصفصف المستوي الأملس (tahdhib); الصفصف المستوي من الأرض كأنه على صف واحد (mufradat)
- **B006** söğüt ağacı — söğüt ağacı
  الصفصف شجر الخلاف الواحدة بالهاء (ayn); الصفصاف شجر الخلاف (sihah;mufradat); الصفصاف الخلاف (tahdhib); هو شجر الخلاف بلغة أهل الشام (tahdhib)
- **B007** su başında toplanma [kalıp] — su başında toplanmak · su başında toplanmak
  تضافوا على الماء وتصافوا عليه بمعنى واحد إذا اجتمعوا عليه (tahdhib)

## ECHO ر ب و (root_000537) — for رَبُّكَ (w2): withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:22, and ## Buluşmalar) =====
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

