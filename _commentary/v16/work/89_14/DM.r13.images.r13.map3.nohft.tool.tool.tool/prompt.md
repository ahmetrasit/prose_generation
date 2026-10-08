Focus: 89:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_14/D.r13/context.md =====
# 89:14 — focus

إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ

Anchor translation (canonical reading, reference only):

Kuşkusuz Rabbin gözetlemektedir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّ | إِنّ |  | ACC |
| 2 | رَبَّكَ | رَبّ | ر ب ب | N;PRON |
| 3 | لَبِٱلْمِرْصَادِ | مِرْصَاد | ر ص د | EMPH;P;DET;N |


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
- 89:14 ◀ focus إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
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


===== _commentary/v16/work/89_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ب ب (root_000532) — identity root of رَبَّكَ (w2)

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

## ر ص د (root_000566) — identity root of لَبِٱلْمِرْصَادِ (w3)

- **B001** gözetleyip bekleme — 
  رصدته أرصده أي ترقبته؛ الراصد للشئ المراقب له؛ الرصد هم القوم الذين يرصدون كالحرس؛ الرصد يقال للراصد الواحد وللجماعة الراصدين وللمرصود؛ يقال للحية التي ترصد المارة على الطريق رصيد
- **B002** birisi veya bir amaç için hazırlayıp ayırma — 
  أرصدت له كذا أي هيأته له؛ أرصدت له أي أعددت؛ أرصدت له شيئا أرصده أعددت له؛ وإرصاد الانسان في المكافأة والخير؛ أنا لك مرصد بإحسانك حتى أكافئك به؛ أرصدته له
- **B003** gözetleme yeri veya yolu — gözetleme yeri veya yol · gözetleme yeri veya yol · yırtıcı hayvan tuzağı · yırtıcı hayvanlar için hazırlanmış tuzaklar
  المرصد موقع الرصد؛ المرصد موضع الرصد؛ المرصاد الطريق؛ المرصد والمرصاد عند العرب الطريق؛ المرصاد المكان الذي يرصد به الراصد؛ المرصاد نحوه لكنه يقال للمكان الذي اختص بالترصد؛ الرصائد الوصائد مصايد تعد للسباع
- **B004** ilk ya da az yağmur ve seyrek ot — ilk yağmur, az yağmur veya seyrek ot · bir yağmur geçişi veya ilk yağmur geçişi · yağmur almış ve yeşermesi beklenen arazi
  الرصد أول المطر؛ الرصد كلأ قليل في أرض يرجى بها حيا الربيع؛ الرصدة بالفتح الدفعة من المطر؛ الرصد بالتحريك القليل من الكلأ والمطر؛ من أسماء المطر الرصد واحدتها رصدة؛ أرض مرصدة وهي التي مطرت وهي ترجى لأن تنبت

## ECHO ر ب و (root_000537) — for رَبَّكَ (w2): withheld observed target; not identity

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

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:14, and ## Buluşmalar) =====
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

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

