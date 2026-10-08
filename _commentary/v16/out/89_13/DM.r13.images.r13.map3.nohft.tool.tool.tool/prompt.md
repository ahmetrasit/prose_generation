Focus: 89:13. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_13/D.r13/context.md =====
# 89:13 — focus

فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ

Anchor translation (canonical reading, reference only):

Bunun üzerine Rabbin üzerlerine bir azap kamçısı yağdırdı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَصَبَّ | صَبَّ | ص ب ب | CONJ;V |
| 2 | عَلَيْهِمْ | عَلَىٰ |  | P;PRON |
| 3 | رَبُّكَ | رَبّ | ر ب ب | N;PRON |
| 4 | سَوْطَ | سَوْط | س و ط | N |
| 5 | عَذَابٍ | عَذَاب | ع ذ ب | N |


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
- 89:13 ◀ focus فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
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


===== _commentary/v16/work/89_13/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ب ب (root_000838) — identity root of فَصَبَّ (w1)

- **B001** yukarıdan dökmek ve dökülüp akmak — suyu veya benzeri bir sıvıyı yukarıdan dökmek · dökülmek veya akmak · sıcağın bastırması, iyice şiddetlenmesi · üzerlerine ağır bir ceza indirmek
  صببت الماء أصبه صبا (maqayis); صبيت الماء صبا (ayn); صب الماء وغيره صبا (jamhara); صببت الماء صبا فانصب أي سكبته فانسكب (sihah); صبك الماء ونحوه (tahdhib); صب الماء إراقته من أعلى (mufradat)
- **B002** inişli yer veya aşağı eğimli akış yolu — inişli yer; aşağı eğimli yol veya ırmak kesimi · inişli, aşağı eğimli yerler
  لما انحدر من الأرض صبب وجمعه أصباب (maqayis); الصبب تصوب نهر أو طريق يكون في حدور (ayn;tahdhib); صب في الوادي إذا انحدر فيه (jamhara); الصبب ما انحدر من الأرض وجمعه أصباب (sihah)
- **B003** kapta kalan az miktar ve onu içme — kabın dibinde kalan az miktarda su veya içecek · kabın dibindeki az içeceği içmek; bir şeyden az miktar edinmek · dökülebilecek kadar kalan az su veya içecek
  الصبابة البقية من الماء في الإناء (maqayis); الصبابة ما فضل في أصل إناء من شراب (ayn); الصبابة من الشيء باقيه (jamhara); الصبابة بالضم البقية من الماء في الإناء وتصاببت الماء إذا شربت صبابته (sihah); البقية اليسيرة تبقى في الإناء من الشراب فإذا شربها الرجل قال تصاببتها (tahdhib); الصبابة والصبة البقية التي من شأنها أن تصب (mufradat)
- **B004** sevgiyle yönelten ince ve yakıcı özlem — sevgiyle yönelten ince ve yakıcı özlem · sevgi ve özlemle bağlanmış erkek veya kadın · birine ya da bir şeye sevgiyle yönelmek
  الصبابة من صب إليه ورجل صب إذا غلبه الهوى (maqayis); الصبابة مصدر الرجل الصب وهو يصب إليها عشقا وهو الوجد والمحبة (ayn); رجل صب بين الصبابة والصبابة رقة الشوق (jamhara); الصبابة رقة الشوق وحرارته ورجل صب عاشق مشتاق (sihah); صب الرجل إذا عشق يصب صبابة والصبابة رقة الهوى (tahdhib); صبا إلى كذا صبابة مالت نفسه نحوه محبة له (mufradat)
- **B005** bir araya yığılmış madde veya canlı kümesi — bir araya yığılmış yiyecek veya toplanmış hayvan ya da insan kümesi
  الصبة القطعة من الخيل والقطعة من الغنم (maqayis); الصبة كل ما صببته من طعام أو غيره مجتمعا والصبة القطعة من الخيل ومن الغنم (jamhara); الصبة الكثبة من الطعام وغيره والصبة القطعة من الغنم (jamhara); الصبة القطعة من الخيل والصرمة من الإبل ومن المعز ما بين العشرة إلى الأربعين (sihah); الصبة الجماعة من الناس والقطعة من الإبل والشاه (tahdhib); الصبة كالصرمة (mufradat)
- **B006** çıkarılmış veya dökülmüş sıvı ve madde adı — susam yaprağı suyu, kına özü, kan, kırmızı boya, ter, buz veya dökülen yağmur
  الصبيب ماء ورق السمسم أو عصارة الحناء (maqayis;sihah;tahdhib); الصبيب الدم والعصفر المخلص (maqayis;ayn;sihah;tahdhib); الصبيب صبغ أحمر (jamhara); العرق صبيب والجليد صبيب (tahdhib); الصبيب المصبوب من المطر ومن عصارة الشيء ومن الدم (mufradat)
- **B007** tükenip çok az kalmak veya dağılıp bütünlüğünü yitirmek — tükenip yok olmak veya yalnızca çok azı kalmak · topluluk dağılmak; orduyu veya malı dağıtmak
  تصبب الشيء ذهب ومحق (maqayis); تصبصب الشيء امحق وذهب (sihah); المتصبصب الذاهب الممحق وتصَبصب القوم إذا تفرقوا وصبصب إذا فرق جيشا أو مالا (tahdhib); تصبصب ذهبت صبابته (mufradat)
- **B008** yılanın yükselip hedefinin üzerine atılması — yılanın yükselip ısıracağı kişinin üzerine yukarıdan atılması
  الحيات الأساود الصب إذا أرادت النكز انصبت على الملدوغ (maqayis); الحية السوداء إذا أرادت أن تنهش ارتفعت ثم صبت (sihah); صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق (tahdhib)
- **B009** bir kişiyi bağ içine koyup hareketini kısıtlamak — bir erkeği bağ içine koyup hareketini kısıtlamak
  صب رجل فلان في القيد إذا قيد (tahdhib)
- **B010** ara vermeden ve gevşemeden yol alma — ara vermeden ve gevşemeden sürdürülen yol alış
  خمس صبصاب مثل بصباص (sihah); خمس صبصاب وبصباص وحصحاص كل هذا السير الذي ليست فيه وتيرة ولا فتور (tahdhib)
- **B011** başkasının koyun sürüsüne girip zarar vermek — başkasının koyun sürüsüne girip zarar vermek
  صب فلان غنم فلان إذا عاث فيها (tahdhib)

## ر ب ب (root_000532) — identity root of رَبُّكَ (w3)

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

## س و ط (root_000759) — identity root of سَوْطَ (w4)

- **B001** bir şeyi karıştırıp iç içe geçirme — bir şeyi kendi içinde karıştırmak · bir şeyi iyice karıştırmak · işlerini birbirine katıp yönetimini bozmak · malları aralarında birbirine karışmış olmak · karıştırma aracı · karıştırma bağlamında geçen, anlamı ayrıca belirlenmemiş söz
  أصل يدل على مخالطة الشيء الشيء (maqayis)؛ سطت الشيء خلطت بعضه ببعض (maqayis)؛ خلطك الشيء بالشيء (ayn)؛ سوط أمره تسويطا أي خلط فيه (ayn;tahdhib)؛ أموالهم سويطة بينهم أي مختلطة (sihah;tahdhib)؛ أصل السوط خلط الشيء بعضه ببعض (mufradat)
- **B002** kırbaç ve kırbaçla vurma — örgülü deri kırbaç · hayvanı kırbaçlamak
  السوط لأنه يخالط الجلدة (maqayis)؛ سطته بالسوط ضربته (maqayis)؛ السوط معروف (ayn)؛ السوط الذي يضرب به (sihah)؛ وسطته إذا ضربته بالسوط (sihah)؛ ساط دابته إذا ضربه بالسوط (tahdhib)؛ السوط الجلد المضفور الذي يضرب به (mufradat)
- **B003** cezadan bir pay veya çok şiddetli ceza [kalıp] — cezadan bir pay · çok şiddetli bir ceza türü · kırbaç cezasına benzetilen veya türlü cezaların birleşimini anlatan ceza
  فصب عليهم ربك سوط عذاب أي نصيبا من العذاب (maqayis)؛ سوط عذاب أي نصيب عذاب ويقال شدته (sihah)؛ لكل نوع من العذاب تدخل فيه السوط (tahdhib)؛ جرى لكل عذاب إذا كان فيه عندهم غاية العذاب (tahdhib)؛ تشبيها بما يكون في الدنيا من العذاب بالسوط (mufradat)؛ إشارة إلى ما خلط لهم من أنواع العذاب (mufradat)
- **B004** suyu ve hurması bol sulu yemek — suyu ve hurması bol sulu yemek
  السويطاء مرقة كثيرة التمر والماء (ayn)؛ السويطاء مرقة كثير ماؤها وتمرها (tahdhib)

## ع ذ ب (root_000994) — identity root of عَذَابٍ (w5)

- **B001** tatlı ve kolay tüketilen yiyecek ya da içecek — tatlı, hoş ve kolay tüketilir · tatlılık ve içim hoşluğu · suları tatlılaştı veya tatlı suya kavuştular · tatlı içme suyu aradılar veya sağladılar · onu tatlı saydı · onun için şu kuyudan su çekilir · birlikte anılan tükürük ve şarap
  عذب الماء عذوبة فهو عذب طيب (maqayis;ayn;tahdhib)؛ العذب ضد الملح وكل مستسيغ من طعام أو شراب (jamhara)؛ ماء عذب طيب بارد (mufradat)؛ استعذب القوم ماءهم إذا استقوه عذبا (sihah)
- **B002** yemeden içmeden durma — susuzluktan yemedi · yiyip içmeden duran · yiyip içmeden duran · yemekten kaçınır · geceyi yemeden içmeden geçirdi
  عذب الحمار يعذب عذبا وعذوبا فهو عاذب وعذوب لا يأكل من شدة العطش (maqayis;ayn)؛ العذوب من الدواب وغيرها القائم الذي لا يأكل ولا يشرب (sihah)؛ بات عذوبا إذا لم يأكل شيئا ولم يشرب (tahdhib)
- **B003** vazgeçme veya alıkoyma — o şeyden vazgeçti · kadınlardan söz etmekten kaçının · onu o işten alıkoydu · onu o işten kesti · senden vazgeçtim
  أعذب عن الشيء إذا لها عنه وتركه (maqayis)؛ أعذب عن الشيء إذا امتنع عنه (jamhara;tahdhib)؛ أعذبته عن الأمر إذا منعته عنه (sihah)؛ عذبته تعذيبا كقولك فطمته عن هذا الأمر (ayn;tahdhib)
- **B004** gökyüzüne karşı örtüsüz — gökyüzüne karşı örtüsüz olan · gökyüzüne karşı örtüsüz olan · geceyi gökyüzüne açık geçirdi
  العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب (maqayis;tahdhib)؛ فبات عذوبا للسماء كأنه سهيل (maqayis;tahdhib)
- **B005** ağır acı çektirme ve cezalandırma — ağır acı ve ceza · ona ağır acı çektirdi veya ceza verdi · yok edici ceza
  العذاب يقال منه عذب تعذيبا وناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة (maqayis)؛ عذبت الرجل وغيره تعذيبا والاسم العذاب (jamhara)؛ العذاب العقوبة وقد عذبته تعذيبا (sihah)؛ العذاب هو الإيجاع الشديد (mufradat)
- **B006** ince uç veya sarkan bağlı parça — kamçının ucu veya askısı · mızrak başına bağlanan bez · dilin ince ucu · teraziyi kaldıran ip · ağaç dalı · deve kamışının öndeki sivri ucu · ayakkabı bağının serbest ucu · kayışların uçları · eyerin arkasından sarkan deri parçası · ağıtçı kadının bezi · kamçıya askı yaptı
  عذبة السوط طرفه (maqayis;tahdhib)؛ عذبة الرمح الخرقة التي تشد على رأسه (jamhara)؛ عذبة اللسان طرفه (jamhara;sihah;tahdhib)؛ عذبة الميزان الخيط الذي يرفع به (sihah;tahdhib)؛ عذبة الشجر غصنه (sihah;tahdhib)؛ عذبة شراك النعل المرسلة من الشراك (tahdhib)
- **B007** yalıtık adlandırmalar — sudaki çer çöp veya yüzey tabakası · çer çöpü bol su · havuzundaki çer çöpü çıkar · havuzun yüzey tabakasını kır · çevresinde otlak bulunmayan su başı
  العذبة القذاة وماء ذو عذب أي كثير القذى (sihah)؛ أعذب حوضك أي انزع ما فيه من القذى (sihah)؛ اضرب عذبة الحوض حتى يظهر الماء أي اضرب عرمضه (tahdhib)؛ ماء ما به عذبة أي لا رعي فيه ولا كلأ (tahdhib)
- **B008** iyi ve cömert huylu — iyi ve cömert huylu
  العذبي الكريم الأخلاق (sihah)
- **B009** biçime bağlı adlandırmalar — doğumdan sonra döl yatağından çıkan madde · kadının döl yatağı
  العذب ما يخرج على أثر الولد من الرحم (tahdhib)؛ العذابة رحم المرأة (tahdhib)

## ECHO ر ب و (root_000537) — for رَبُّكَ (w3): withheld observed target; not identity

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

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:13, and ## Buluşmalar) =====
## Su: fışkıran, taşan, yukarıdan dökülen

İlk kelimenin kökü, karanlıktan önce suyun yarılmasını anlatır: {ar:انفجر الماء انفجارا تفتح, tr:infecera'l-mâu'nficâran tefettah, gloss:su fışkırdı, önü açıldı, source:"ف ج ر,B001"}. Fışkırma şöyle tarif edilir: {ar:إذا انبعث سائلا, tr:ize'nbe'ase sâilen, gloss:akarak fırladığında, source:"ف ج ر,B001"}. Kaya ya da toprak bir noktada çatlar, içerideki su bastırarak dışarı fırlar ve akmaya başlar. Kur'an bu sahneyi taşın içinden kurar. İsrailoğullarına kalplerinin taştan da katı olduğu söylenirken bazı taşlardan ırmakların fışkırdığı hatırlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi var ki içinden ırmaklar fışkırır, source:2:74}. Nuh'un tufanında aynı fiil yeryüzünü kaynaklara çevirir ve su ölçüsü önceden belirlenmiş bir iş üzerinde buluşur: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ, tr:ve feccernâ'l-arda uyûnen fe'lteka'l-mâu alâ emrin kad kudir, gloss:yeri kaynaklar hâlinde fışkırttık, su takdir edilmiş bir iş üzerinde buluştu, source:54:12}. Kıyamette denizler fışkırtılır: {ar:وَإِذَا ٱلْبِحَارُ فُجِّرَتْ, tr:ve ize'l-bihâru fuccirat, gloss:denizler fışkırtıldığında, source:82:3}. Mekke'de inkârcılar Peygamber'den, arasından ırmaklar fışkırttığı bir bahçe isterler {source:17:91}. Kur'an bu işi cennette Allah'ın kullarına verir: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdu'llâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği, dilediklerince fışkırttıkları bir kaynak, source:76:6}.

Aynı kök günahı da adlandırır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-me'âsî fucûrâ, gloss:günahlara atılmak ve açılmak, fücur, source:"ف ج ر,B004"}. Suyun önünü yarıp fırlaması ile insanın günaha açılıp atılması aynı kelimeyle söylenir. Bu yüzden surenin geçmiş kavimleri anlatan bölümü bir sel gibi duyulur.

Dokuzuncu ayette Semûd kayayı vadide oymuştur: {ar:بِٱلْوَادِ, tr:bi'l-vâd, gloss:vadide, source:89:9}. Vadi selin yoludur: {ar:كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل, tr:kullu mufracin beyne cibâlin ve âkâmin ve tilâlin yekûnu meslekan li's-seyl, gloss:dağlar, tepeler ve tümsekler arasında selin geçtiği her açıklık, source:"و د ي,B005"}. Kök akmayı adlandırır: {ar:ودى أي سال, tr:vedâ ey sâl, gloss:aktı, source:"و د ي,B001"}. Kaya evler suyun indiği yatağa kurulmuştur. Kur'an'ın sel benzetmesinde vadiler kendi ölçüleri kadar akar ve sel kabarık bir köpük taşır: {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا, tr:fe-sâlet evdiyetun bi-kaderihâ fahtemele's-seylu zebeden râbiyâ, gloss:vadiler ölçülerince aktı, sel kabarık bir köpük taşıdı, source:13:17}. Köpük gider, insanlara yarayan yerde kalır. Âd da vadilerine doğru gelen bulutu yağmur sanmıştır. Hûd'un Ahkâf'ta kavmini uyarmasıyla başlayan sahnede {source:46:21} bulutu görünce şöyle derler: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا ۚ بَلْ هُوَ مَا ٱسْتَعْجَلْتُم بِهِۦ ۖ رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:kâlû hâzâ âridun mumtırunâ, bel huve me'sta'celtum bih, rîhun fîhâ azâbun elîm, gloss:"Bu bize yağmur getiren bir bulut" dediler. Hayır, o acele istediğiniz şeydir: içinde acı bir azap olan bir rüzgâr, source:46:24}.

On birinci ayetin fiili suyun taşmasıdır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:o ülkelerde azanlar, source:89:11}. Arapçada sel için {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel bol suyla gelince "taştı" denir, source:"ط غ ي,B002"}, su için de {ar:طغى الماء خروجه عن المقدار, tr:tuğyânu'l-mâi hurûcuhû ani'l-mikdâr, gloss:suyun taşması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} denir. Ayette anlam azgınlıktır. Yanında ölçüsünden çıkan, yatağını aşan su duyulur. Kur'an kelimeyi tufan için doğrudan kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayet taşkının sonucunu verir: {ar:فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ, tr:fe-ekserû fîhe'l-fesâd, gloss:oralarda bozgunu çoğalttılar, source:89:12}. Çoğalmak {ar:الكثرة نماء العدد, tr:el-kesretu nemâu'l-aded, gloss:çokluk, sayının büyümesidir, source:"ك ث ر,B001"} demektir, bozulmak da {ar:الفساد خروج الشيء عن الاعتدال, tr:el-fesâdu hurûcu'ş-şey'i ani'l-i'tidâl, gloss:fesat, bir şeyin dengeden çıkmasıdır, source:"ف س د,B001"}. Hacim büyür ve şeyler dengelerinden çıkar. Bozgunun tarifindeki "çıkış" suyun ölçüden çıkışıyla aynı kelimedir. Kur'an'da bozgun karaya ve denize yayılır: {ar:ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:zahera'l-fesâdu fi'l-berri ve'l-bahr, gloss:karada ve denizde bozgun ortaya çıktı, source:30:41}. Salih de Semûd'a, Âd'dan sonra yerleştirildikleri yeryüzünde ovalardan saraylar edinip dağları ev diye oyduklarını hatırlatır ve sonra şöyle der: {ar:وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ, tr:ve lâ ta'sev fi'l-ardı mufsidîn, gloss:yeryüzünde bozguncular olarak dolaşmayın, source:7:74}.

On üçüncü ayet taşkına yukarıdan karşılık verir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üzerlerine azap kamçısı yağdırdı, source:89:13}. Sabb, suyun fiilidir: {ar:صب الماء إراقته من أعلى, tr:sabbu'l-mâi irâkatuhû min a'lâ, gloss:suyu dökmek, onu yukarıdan akıtmaktır, source:"ص ب ب,B001"}. Vadiye inmek de bu fiille söylenir: {ar:صب في الوادي إذا انحدر فيه, tr:sabbe fi'l-vâdî izenhadera fîh, gloss:vadiye indi, oraya doğru aktı, source:"ص ب ب,B002"}. Aşağıda yatağını taşan suya yukarıdan dökülen bir şey karşılık verir. Dökülenin adı azaptır ve bu kelimenin harfleri tatlı suyu da adlandırır: {ar:العذب ضد الملح وكل مستسيغ من طعام أو شراب, tr:el-azbu diddu'l-milhi ve kullu mustesâğin min taâmin ev şarâb, gloss:azb, tuzlunun zıddıdır; boğazdan rahat geçen her yiyecek ve içecek, source:"ع ذ ب,B001"}. Âd'ın yağmur sandığı rüzgâr bu iki yüzü tek sahnede gösterir: beklenen tatlı su, gelen ise azaptır {source:46:24}.

Aynı su sahnesi surenin ikinci yarısında rahmet olarak döner. Kur'an insana yemeğine bakmasını söyler: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şekakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Fiil aynıdır, ama bu kez arkasından yarılan toprak ve biten yemek gelir. Surenin sınav sahnesindeki kelimeler bu yağmuru da taşır. İkram için {ar:كرم السحاب أتى بالغيث, tr:keruma's-sehâbu etâ bi'l-ğays, gloss:bulut cömert davrandı, yağmur getirdi, source:"ك ر م,B002"} denir. Rızık için {ar:وقد يسمى المطر رزقا, tr:ve kad yusemma'l-mataru rızkâ, gloss:yağmura da rızık denir, source:"ر ز ق,B003"} denir. Kur'an da şöyle der: {ar:وَفِى ٱلسَّمَآءِ رِزْقُكُمْ, tr:ve fi's-semâi rızkukum, gloss:rızkınız göktedir, source:51:22}. Ölçü için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-mataru bi-mikdâr, gloss:yağmur ölçüyle iner, source:"ق د ر,B001"} denir. On altıncı ayette rızkın daraltılması, yağmurun ölçüyle inmesinin insanın gözünden görünen yüzüdür. Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında yağmur duyulur: {ar:الحيا المطر لأنه يحيي الأرض بعد موتها, tr:el-hayâ el-mataru li-ennehû yuhyi'l-arda ba'de mevtihâ, gloss:hayâ yağmurdur, çünkü yeri ölümünden sonra diriltir, source:"ح ي ي,B002"}. Yirmi sekizinci ayetteki "dön" kelimesinin yanında da dökülüp yeniden gelen yağmur duyulur: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-rec'u el-ğaysu ve huve'l-mataru li-ennehâ tuğîsu ve tasubbu summe terci'u fe-tuğîs, gloss:rec' yağmurdur, çünkü yağar, dökülür, sonra döner ve yine yağar, source:"ر ج ع,B006"}. Kur'an da göğe dönüşüyle yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâi zâti'r-rec', gloss:dönüp dönüp yağan göğe, source:86:11}. Ölü toprağa yağmur gönderilmesi, ölülerin çıkarılmasının örneğidir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhricu'l-mevtâ leallekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Son kelime bu suyun ürününe varır: bahçeye ve bitkinin gürleşip çiçek açmasına: {ar:جن النبت جنونا إذا اشتد وخرج زهره, tr:cenne'n-nebtu cunûnen izeştedde ve harace zehruh, gloss:bitki gürleşip çiçeğini çıkarınca "cenne" denir, source:"ج ن ن,B011"}.

Surede suyun işleyişi bir ölçüye bağlanır. Ölçüsünde kalan su hayat verir, ölçüsünü aşan su süpürür. Âd, Semûd ve Firavun ölçüyü aşan taşkındır ve onlara yukarıdan azap dökülür. İnsana ölçülü rızık iner ve o, ölçünün kendisini aşağılanma sanır.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B001; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:9 بِٱلْوَادِ و د ي B001; 89:9 بِٱلْوَادِ و د ي B005; 89:11 طَغَوْا۟ ط غ ي B002; 89:12 فَأَكْثَرُوا۟ ك ث ر B001; 89:12 ٱلْفَسَادَ ف س د B001; 89:13 فَصَبَّ ص ب ب B001; 89:13 فَصَبَّ ص ب ب B002; 89:13 عَذَابٍ ع ذ ب B001; 89:15 فَأَكْرَمَهُۥ ك ر م B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B003; 89:24 لِحَيَاتِى ح ي ي B002; 89:28 ٱرْجِعِىٓ ر ج ع B006; 89:30 جَنَّتِى ج ن ن B011

## Gözetleme yeri ve bakan göz

Altıncı ayet dinleyenin gözünü olup bitene çevirir: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:e-lem tera keyfe feale rabbuke bi-Âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Görmek, gözle ya da kalple bakmaktır: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakıp görmek, source:"ر ء ي,B001"}. Aynı kalıp Fil sahiplerinin akıbetini anlatırken de kullanılır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ, tr:e-lem tera keyfe feale rabbuke bi-ashâbi'l-fîl, gloss:Rabbinin fil sahiplerine ne yaptığını görmedin mi, source:105:1}. Dinleyen, bir olayın gözlemcisi yapılır.

Gözlenen şey yolda olan insanlardır. Dördüncü ayetin fiili gece yürüyenleri de adlandırır: {ar:السارية للقوم الذين يسرون بالليل, tr:es-sâriye li'l-kavmi'llezîne yesrûne bi'l-leyl, gloss:sâriye, gece yol alan topluluktur, source:"س ر ي,B001"}. Dokuzuncu ayetteki fiilin yanında ülkeleri boydan boya geçmek duyulur: {ar:جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها, tr:cubtu'l-bilâde ecûbuhâ ve ecîbuhâ ve'ctebtuhâ izâ kata'tuhâ, gloss:ülkeleri boydan boya geçtim, source:"ج و ب,B002"}. On birinci ayette bu yolcular ülkelerde sınırı aşar: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı geçmek, source:"ط غ ي,B001"}. Ayetlerin anlamı kazmak ve azmaktır. Yanında yol alan, ülke aşan ve sınırı geçen yolcular duyulur.

On dördüncü ayet yolun üzerindeki yeri adlandırır: {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin elbette gözetleme yerindedir, source:89:14}. Mirsâd hem yolun kendisidir, {ar:المرصاد الطريق, tr:el-mirsâd et-tarîk, gloss:mirsâd yoldur, source:"ر ص د,B003"}, hem de gözcünün beklediği yer: {ar:المرصاد المكان الذي يرصد به الراصد, tr:el-mirsâdu'l-mekânu'llezî yersudu bihi'r-râsıd, gloss:mirsâd, gözcünün gözetlediği yerdir, source:"ر ص د,B003"}. Gözcü bir şeyi kollayan kişidir: {ar:الراصد للشئ المراقب له, tr:er-râsıdu li'ş-şey'i el-murâkıbu leh, gloss:râsıd, bir şeyi gözetleyendir, source:"ر ص د,B001"}. Aynı kök yolda pusu kuran yılana da ad verir: {ar:يقال للحية التي ترصد المارة على الطريق رصيد, tr:yukâlu li'l-hayyeti'lletî tersudu'l-mârrate ale't-tarîki rasîd, gloss:yolda geçenleri kollayan yılana rasîd denir, source:"ر ص د,B001"}. Bu düzenin işleyişi şöyledir: gözcü kimseyi kovalamaz, yolun geçtiği yerde bekler. Her yolcu oradan geçmek zorundadır. Bir önceki ayetteki dökme fiili bu yılanın hareketini de anlatır: {ar:صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق, tr:sabbeti'l-hayyetu aleyhi izertefeat fensabbet aleyhi min fevk, gloss:yılan kalkıp yukarıdan üstüne çullandı, source:"ص ب ب,B008"}. Surenin sıralaması da bu düzene uyar. Önce darbe iner, gözetleme yeri ancak sonra adlandırılır. Yolcular gözcünün varlığını vuruldukları anda öğrenir.

Kur'an aynı yeri başka sahnelerde de kurar. Kıyamet anlatılırken cehennem için {ar:إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا, tr:inne cehenneme kânet mirsâdâ, gloss:cehennem bir gözetleme yeridir, source:78:21} denir. Antlaşmayı bozanlara karşı verilen emir şöyledir: {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehum kulle marsad, gloss:onlar için her gözetleme yerinde oturun, source:9:5}. İblis de Allah'a şöyle der: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ek'udenne lehum sırâtake'l-mustekîm, gloss:onlar için senin dosdoğru yolunun üstünde oturacağım, source:7:16}. Şuayb kavmine yollarda pusu kurmamalarını söyler: {ar:وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ, tr:ve lâ tak'udû bi-kulli sırâtin tûidûn, gloss:tehdit ederek her yolun başında oturmayın, source:7:86}. Cinler gökte kendilerini bekleyen bir alev bulur: {ar:يَجِدْ لَهُۥ شِهَابًۭا رَّصَدًۭا, tr:yecid lehû şihâben rasadâ, gloss:kendisini gözetleyen bir alev bulur, source:72:9}. Allah elçisinin önüne ve arkasına gözcüler koyar {source:72:27}. İnsanın söylediği her sözün yanında da hazır bir gözcü vardır: {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözcü vardır, source:50:18}.

Bakmanın bir de insanın içindeki yüzü vardır. On beşinci ve yirmi üçüncü ayetlerdeki "insan" kelimesi göz bebeğindeki küçük sureti de adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, gözbebeğinin karasında görünen küçük surettir, source:"ء ن س,B005"}. Bu tanımda misal ve görmek kelimeleri birlikte geçer. Sekizinci ayetin kökü sureti, {ar:التمثال الصورة, tr:et-timsâl es-sûra, gloss:timsal, surettir, source:"م ث ل,B008"}, ve görülerek alınan dersi de adlandırır: {ar:يكون المثل بمعنى العبرة, tr:yekûnu'l-meselu bi-ma'ne'l-ibra, gloss:mesel, ibret anlamına da gelir, source:"م ث ل,B011"}. Beşinci ayetin hicr kökü gözün çevresine de ad verir: {ar:ومحجر العين ما يدور بها, tr:ve mahcaru'l-ayni mâ yedûru bihâ, gloss:gözün mahceri, onu çevreleyen yerdir, source:"ح ج ر,B006"}. Üçüncü ayetteki çift kelimesi de bir tek şeyi iki gören gözü adlandırır: {ar:عين شافعة تنظر نظرين, tr:aynun şâfiatun tenzuru nazarayn, gloss:şâfia göz, iki bakışla bakan gözdür, source:"ش ف ع,B006"}. Sure insana Âd'ı, Semûd'u ve Firavun'u göstermiştir. İnsan ise hemen ardından kendi hâline bakar ve tek bir sınavı iki ayrı hüküm olarak okur: bolluğa ikram, darlığa aşağılanma der. Kur'an bu bakışın kendini nasıl gördüğünü söyler {source:96:7}. Âd'a da kulaklar, gözler ve gönüller verilmişti, ama onlara bir yararı olmadı: {ar:فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ, tr:fe-mâ ağnâ anhum sem'uhum ve lâ ebsâruhum, gloss:ne kulakları ne gözleri onlara bir yarar sağladı, source:46:26}. Kıyamet günü örtü kalkar: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık, bugün gözün keskindir, source:50:22}.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B006; 89:4 يَسْرِ س ر ي B001; 89:5 حِجْرٍ ح ج ر B006; 89:6 تَرَ ر ء ي B001; 89:8 مِثْلُهَا م ث ل B008; 89:8 مِثْلُهَا م ث ل B011; 89:9 جَابُوا۟ ج و ب B002; 89:11 طَغَوْا۟ ط غ ي B001; 89:13 فَصَبَّ ص ب ب B008; 89:14 لَبِٱلْمِرْصَادِ ر ص د B001; 89:14 لَبِٱلْمِرْصَادِ ر ص د B003; 89:15 ٱلْإِنسَٰنُ ء ن س B005

## Kırbaç, kazık ve bağ

On üçüncü ayetteki ceza bir aletle sahnelenir: {ar:سَوْطَ عَذَابٍ, tr:savte azâb, gloss:azap kamçısı, source:89:13}. Kamçı örülmüş deriden yapılır: {ar:السوط الجلد المضفور الذي يضرب به, tr:es-savtu'l-cildu'l-madfûru'llezî yudrabu bih, gloss:savt, vurmak için örülmüş deridir, source:"س و ط,B002"}. Adı da derinin içine işlemesinden gelir: {ar:السوط لأنه يخالط الجلدة, tr:es-savtu li-ennehû yuhâlitu'l-cilde, gloss:kamçıya savt denir, çünkü deriye karışır, source:"س و ط,B001"}. Ayetteki ifade de bu karışmayla açıklanır: {ar:إشارة إلى ما خلط لهم من أنواع العذاب, tr:işâratun ilâ mâ hulita lehum min envâi'l-azâb, gloss:onlar için birbirine katılmış türlü azaplara işaret, source:"س و ط,B003"}. Tamlamanın ikinci kelimesi de kamçıya döner: {ar:عذبة السوط طرفه, tr:azebetu's-savti tarafuh, gloss:kamçının azebesi ucudur, source:"ع ذ ب,B006"}. Azabın aslı vurmaktır: {ar:أصل العذاب الضرب ثم استعير ذلك في كل شدة, tr:aslu'l-azâbi'd-darbu summe'stuîra zâlike fî kulli şidde, gloss:azabın aslı vurmaktır, sonra her şiddet için kullanılmıştır, source:"ع ذ ب,B005"}. "Azap kamçısı" tamlamasında iki kelime aynı şeyi iki uçtan söyler: biri örgülü deri, öteki onun vuran ucu. Fiil ise bu tabloya bir şey katar. Kamçı vurulur, dökülmez. Dökülen sudur. Fiil kamçıya bir sağanağın hacmini verir. Ortaya tek bir darbe değil, üstten inen bir kütle çıkar. Aynı fiil ayağı prangaya geçirmeyi de söyler: {ar:صب رجل فلان في القيد إذا قيد, tr:subbe riclu fulânin fi'l-kaydi izâ kuyyid, gloss:ayağı prangaya döküldü, yani bağlandı, source:"ص ب ب,B009"}.

Onuncu ayetteki kazıkların işi bir şeyi yere tutturmaktır: {ar:تد وتدك بالميتدة, tr:tid vetideke bi'l-mîtede, gloss:kazığını tokmakla çak, source:"و ت د,B001"}. Ayak için de {ar:وتد فلان رجله في الأرض إذا ثبتها, tr:vetede fulânun riclehû fi'l-ardı izâ sebbetehâ, gloss:ayağını yere çaktı, sabitledi, source:"و ت د,B003"} denir. Firavun kazık sahibidir, yani bir şeyi yere çakan, bağlayan ve tutan güç onda toplanmıştır. Kur'an onun azap iddiasını kendi ağzından aktarır. Musa'ya iman eden sihirbazlara şöyle der: {ar:وَلَأُصَلِّبَنَّكُمْ فِى جُذُوعِ ٱلنَّخْلِ وَلَتَعْلَمُنَّ أَيُّنَآ أَشَدُّ عَذَابًۭا وَأَبْقَىٰ, tr:ve le-usallibennekum fî cuzûi'n-nahli ve le-ta'lemunne eyyunâ eşeddu azâben ve ebkâ, gloss:sizi hurma kütüklerine asacağım ve hangimizin azabının daha çetin ve daha kalıcı olduğunu bileceksiniz, source:20:71}.

Yirmi beşinci ve yirmi altıncı ayetler bu iddiaya cevap verir: {ar:فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ, tr:fe-yevmeizin lâ yuazzibu azâbehû ehad, gloss:o gün hiç kimse O'nun azabı gibi azap edemez, source:89:25}, {ar:وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ, tr:ve lâ yûsiku vesâkahû ehad, gloss:hiç kimse O'nun bağlaması gibi bağlayamaz, source:89:26}. Azap şiddetli acıdır: {ar:العذاب هو الإيجاع الشديد, tr:el-azâbu huve'l-îcâu'ş-şedîd, gloss:azap, şiddetli acı vermektir, source:"ع ذ ب,B005"}. Vesâk ise bağlamaya yarayan her şeydir: {ar:الوثاق: كل ما أوثقت به شيئا, tr:el-vesâk kullu mâ evsakte bihî şey'â, gloss:vesâk, bir şeyi bağladığın her şeydir, source:"و ث ق,B003"}. Bağlama da sağlamlaştırmaktır: {ar:وثقت الشيء: أحكمته, tr:vesiktu'ş-şey'e ahkemtuh, gloss:şeyi sağlamlaştırdım, source:"و ث ق,B002"}. Kur'an bu ipi savaş sahnesinde kullanır: {ar:فَشُدُّوا۟ ٱلْوَثَاقَ, tr:fe-şuddu'l-vesâk, gloss:bağı sıkı bağlayın, source:47:4}. Kıyamette ise ip zincire dönüşür. Kitabı sol eline verilen kişi için {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:tutun onu, bağlayın, source:69:30} denir, sonra {ar:ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ, tr:summe fî silsiletin zer'uhâ seb'ûne zirâan feslukûh, gloss:sonra onu boyu yetmiş arşın olan bir zincire geçirin, source:69:32}. Sebebi de açıkça söylenir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmezdi, source:69:34}. Bu, surenin on sekizinci ayetinde kınanan şeyin ta kendisidir. Kur'an başka yerlerde de prangalar {ar:إِنَّ لَدَيْنَآ أَنكَالًۭا وَجَحِيمًۭا, tr:inne ledeynâ enkâlen ve cahîmâ, gloss:bizim katımızda prangalar ve yakıcı bir ateş var, source:73:12}, birbirine zincirlenmiş suçlular {ar:مُّقَرَّنِينَ فِى ٱلْأَصْفَادِ, tr:mukarranîne fi'l-asfâd, gloss:zincirlere vurulmuş hâlde, source:14:49} ve boyunlardaki demir halkalar {source:40:71}, {source:76:4} anlatır. Surede kazık sahibinin yere çaktığı ayak, sonunda hiçbir insanın bağlayamayacağı bir bağla karşılanır.

Kaynaklar: 89:10 ٱلْأَوْتَادِ و ت د B001; 89:10 ٱلْأَوْتَادِ و ت د B003; 89:13 فَصَبَّ ص ب ب B009; 89:13 سَوْطَ س و ط B001; 89:13 سَوْطَ س و ط B002; 89:13 سَوْطَ س و ط B003; 89:13 عَذَابٍ ع ذ ب B005; 89:13 عَذَابٍ ع ذ ب B006; 89:25 يُعَذِّبُ عَذَابَهُۥٓ ع ذ ب B005; 89:26 يُوثِقُ وَثَاقَهُۥٓ و ث ق B002; 89:26 وَثَاقَهُۥٓ و ث ق B003

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

