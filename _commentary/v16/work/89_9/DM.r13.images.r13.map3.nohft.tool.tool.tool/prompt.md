Focus: 89:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_9/D.r13/context.md =====
# 89:9 — focus

وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ

Anchor translation (canonical reading, reference only):

Vadide kayaları oyan Semûd'a da,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَثَمُودَ | ثَمُود |  | CONJ;PN |
| 2 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 3 | جَابُوا۟ | جَابُ | ج و ب | V;PRON |
| 4 | ٱلصَّخْرَ | صَّخْر | ص خ ر | DET;N |
| 5 | بِٱلْوَادِ | وَاد | و د ي | P;DET;N |


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
- 89:9 ◀ focus وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
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


===== _commentary/v16/work/89_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج و ب (root_000273) — identity root of جَابُوا۟ (w3)

- **B001** delip geçerek kesme — bir şeyi delip geçecek biçimde kesmek · kayayı oyarak kesmek · gömleğin yaka açıklığı · gömleğin yakasını kesip açmak · gömleğe yaka açıklığı açmak · kesme veya yama yapma aleti · bir yeri kazıp oymak · ceylan boynuzunun deriyi delerek çıkması
  خرق الشيء (maqayis)؛ قطعك الشيء كما يجاب الجيب (ayn)؛ جبت الشيء أجوبه إذا قطعته جوبا (jamhara)؛ جاب يجوب جوبا إذا خرق وقطع (sihah)؛ اجتاب احتفر (tahdhib)؛ جاب قرنها الجلد فطلع (tahdhib)؛ وثمود الذين جابوا الصخر بالواد (mufradat)
- **B002** bir yeri baştan başa geçme — yeri ve ülkeleri baştan başa geçmek · bir yeri baştan başa geçmek · ülkeleri sürekli dolaşan kimse · bütün gece yol alan kimse · karanlığı yarıp ilerlemek · ülkeden ülkeye taşınan haber · uzak yerlerden gelen şaşırtıcı haberler
  جبت الأرض جوبا فأنا جائب وجواب؛ خبر يجوب البلاد (maqayis)؛ جبت المفازة أي قطعتها؛ الجوائب الغرائب من الأخبار (ayn)؛ جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها؛ جائبة خبر يجوب الأرض من بلد إلى بلد (sihah)؛ جبت البلد أجوبه جوبا إذا قطعته؛ رجل جواب إذا كان قطاعا للبلاد (tahdhib)؛ يستعمل في قطع كل أرض؛ جائبة خبر (mufradat)
- **B003** söze ya da çağrıya karşılık verme — söze ya da soruya verilen karşılık · karşılık vermek · karşılık verme ve çağrıya uyma · isteyenin dileğini karşılamak · karşılıklı konuşmak · karşılık · yanlış işitip yanlış karşılık vermek
  مراجعة الكلام؛ أجابه جوابا؛ تجاوبا مجاوبة (maqayis)؛ الجواب رديد الكلام (ayn)؛ الجواب معروف؛ الإجابة والاستجابة بمعنى؛ المجاوبة والتجاوب التحاور (sihah)؛ أجوبه من الإجابة أي أسرعه إجابة (tahdhib)؛ جواب الكلام؛ أجيبوا داعي الله؛ أجيب دعوة الداع؛ فليستجيبوا لي (mufradat)
- **B004** açılmış ya da ortası boş geniş aralık — geniş açıklık ya da çukur alan · ortası boş veya oyuk · bulutun açılıp dağılması
  الجوبة كالغائط وهو من الباب لأنه كالخرق في الأرض (maqayis)؛ كل مجوف وسطه فهو مجوب (ayn)؛ الجوبة الفرجة في السحاب وفي الجبال؛ انجابت السحابة انكشفت (sihah)؛ الجوبة من الأرض الدارة؛ كل منفتق يتسع فهو جوبة (tahdhib)؛ الجوب قطع الجوبة وهي كالغائط من الأرض (mufradat)
- **B005** giysi, zırh veya kalkan; giysiyi üstüne geçirme — kadının giydiği zırh ya da giysi · kalkan · kesilmiş bir tür giysi · giysiyi üstüne geçirmek
  الجوب درع تلبسه المرأة وهو مجوب (maqayis)؛ الجوب درع تلبسه المرأة (ayn)؛ الجوب الترس (jamhara)؛ الجوب الترس؛ الجوب كالبقيرة؛ اجتبت القميص إذا لبسته (sihah)؛ الجوب الترس؛ اجتاب فلان ثوبا إذا لبسه (tahdhib)
- **B006** ışık, açığa çıkarma ve belirginleştirme — 
  جوب نور وكشف وجلى (tahdhib)

## ص خ ر (root_000847) — identity root of ٱلصَّخْرَ (w4)

- **B001** iri ve sert kaya — iri ve sert kayalar · büyük kaya parçası · kayalar · kayalar · kaya · kayalık yer · kayalık yer
  الصخرة الحجرة العظيمة (maqayis)؛ الصخر عظام الحجارة وصلابها (ayn;tahdhib)؛ ما عظم من الحجارة (jamhara)؛ الحجارة العظام وهي الصخور (sihah)؛ الحجر الصلب (mufradat)
- **B002** pişmiş toprak kap — pişmiş toprak kap · pişmiş toprak kap
  الصاخر إناء من خزف (ayn;tahdhib)؛ الصاخرة إناء من خزف (sihah)
- **B003** bir bitki — bir bitki
  الصخير نبات (ayn)
- **B004** demirlerin çarpışma sesi — demirlerin çarpışma sesi
  الصاخر صوت الحديد بعضه على بعض (tahdhib)

## و د ي (root_001637) — identity root of بِٱلْوَادِ (w5)

- **B001** idrar sonrası ince akıntı ve erkek hayvanda organın dışarı çıkıp dikleşerek sıvı damlatması — idrar sonrası gelen ince akıntı · idrar sonrası gelen ince akıntı · akmak veya ince akıntı çıkarmak · atın çiftleşmek ya da işemek için cinsel organını dışarı çıkarması · eşeğin cinsel organının dikleşmesi ve sıvı damlatması
  ودى الفرس ليضرب أو يبول إذا أدلى (maqayis); الودى ماء يخرج من الإنسان كالمذي (maqayis); ودى الدابة والرجل يدي وديا وهو الماء الرقيق الذي يخرج مع البول (jamhara); الودي بالتسكين ما يخرج بعد البول (sihah); ودى الفرس إذا أخرج جردانه (tahdhib); ودى أي سال ومنه الودي لخروجه وسيلانه (tahdhib); ودى الحمار فهو واد إذا أنعظ (tahdhib); ودى بمعنى قطر منه الماء عند الإنعاظ (tahdhib)
- **B002** öldürülen kişi için mali karşılık ve bu karşılığı ödeme ya da alma — öldürülen kişi için hak sahibine ödenmesi gereken mali karşılık · öldürülen kişinin mali karşılığını hak sahibine ödemek · öldürülen kişi için ödenen mali karşılığı almak
  وديت الرجل أديه دية (maqayis); ووديت القتيل أديه دية إذا أعطيت ديته (jamhara); الدية واحدة الديات وديت القتيل أديه دية إذا أعطيت ديته (sihah); واتديت أي أخذت ديته (sihah); ودى فلانا إذا أدى ديته إلى وليه (tahdhib)
- **B003** küçük hurma fidanı ve bu fidanların topluluğu — küçük hurma fidanları · bir küçük hurma fidanı · küçük hurma fidanları
  الودى صغار الفسلان (maqayis); والودي الفسيل والواحد ودية (jamhara); الودى على فعيل صغار الفسيل الواحدة ودية (sihah); هو الودي لصغار النخل واحدتها ودية (tahdhib); تجمع الودية ودايا (tahdhib)
- **B004** ölmek veya yok olmak; zaman ya da ölüm tarafından yok edilmek — ölmek veya yok olmak · zamanın ya da ölümün birini yok etmesi · ölme veya yok olma · ölmüş veya yok olmuş · yok oluş için az kullanılan ad
  وأودى الشيء يودي إيداء إذا تلف وأودى به الدهر (jamhara); أودى فلان أي هلك فهو مود (sihah); أودى الرجل إذا هلك (tahdhib); أودى به المنون أي أهلكه (tahdhib); اسم الهلاك من ذلك الودى وقلما يستعمل والمصدر الحقيقي الإيداء (tahdhib)
- **B005** yükseltiler arasında sel sularına yol veren vadi — yükseltiler arasında sel sularına yol veren vadi · vadi sözünün son sesi düşmüş biçimi · vadiler
  والوادي معروف وأحسبه راجعا إلى هذا لسيلان الماء فيه (jamhara); والوادي معروف والجمع الأودية (sihah); ومنه الوادي (tahdhib); والوادي كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل أو منفذا (tahdhib)
- **B006** yavrunun emmesini önlemek için devenin meme uçlarına bağlanan tahta parçaları — yavrunun emmesini önlemek için devenin meme uçlarına bağlanan tahta parçaları · emme önleyici takımın tek bir tahta parçası · devenin meme uçlarını iki tahta parçayla bağlamak
  التوادي الخشبات التى تشد على خلف الناقة إذا صرت الواحدة تودية (sihah); والتوادي الخشبات التي تصر بها أطباء الناقة لئلا يرضعها الفصيل وقد وديت الناقة بتوديتين (tahdhib)

## ECHO ج ي ب (root_000283) — for جَابُوا۟ (w3): withheld observed target; not identity

- **B001** gömlek açıklığı ve onu oyup oluşturma — gömlek açıklığı veya açıklığın yeri · gömleğin açıklığını oyarak açmak · gömleğe açıklık yapmak
  الجيب جيب القميص (maqayis;sihah)؛ جيب القميص معروف (jamhara)؛ جبيت القميص تجبيبا جعلت له جيبا (ayn)؛ جبت القميص قورت جيبه وجيبته جعلت له جيبا (maqayis)؛ جيبت القميص تجييبا إذا جعلت له جيبا (sihah)؛ جمع جيب (mufradat)

## ECHO ج ب ي (root_000220) — for جَابُوا۟ (w3): withheld observed target; not identity

- **B001** bir şeyi toplayıp elde etmek — bir şeyi kendisi için ya da bir yerde toplayıp elde etmek · vergiyi toplayıp almak · suyu su teknesinde toplamak
  جبيت الخراج جباية أي جمعته وحصلته (ayn)؛ جبيت الخراج جباية وجبوته جباوة (sihah)؛ جبيت الشيء إذا حصلته لنفسك؛ جباية الخراج جمعه وتحصيله (tahdhib)؛ جبيت الماء في الحوض جمعته؛ جبيت الخراج جباية؛ يجبى إليه ثمرات كل شيء (mufradat)؛ أصل واحد يدل على جمع الشيء والتجمع؛ جبيت المال أجبيه جباية (maqayis_v4+maqayis_v5)
- **B002** birikmiş su veya büyük su teknesi — su teknesinde ya da başka bir yerde birikmiş su · su teknesinde birikmiş su · hayvanların su içtiği geniş ve büyük su teknesi · büyük su tekneleri · su teknesinde biriken bir miktar su
  الجبى ما جمع في الحوض من الماء؛ الجابية حوض ضخم واسع (ayn)؛ الجبى الماء المجموع في الحوض؛ الجابية الحوض الذي يجبى فيه الماء؛ الجمع الجوابي (sihah)؛ الجبى ما جمع في الحوض من الماء؛ الجبى جمع جبية (tahdhib)؛ الحوض الجامع له جابية وجمعها جواب (mufradat)؛ الحوض نفسه جابية؛ الجبا بكسر الجيم ما جمع من الماء في الحوض أو غيره (maqayis_v4+maqayis_v5)
- **B003** kuyu çukuru veya çevresindeki kazı toprağı — kuyu çukuru, kuyu çevresindeki kazı toprağı veya su teknesinin çevresi
  الجبى محفر البئر؛ نثيلة البئر وهي ترابها الذي حولها (ayn)؛ الجبا بالفتح مقصور نثيلة البئر وهي ترابها الذي حولها (sihah)؛ الجبا مقصور ما حول البئر؛ الجبى ما حول الحوض يكتب بالياء (tahdhib)؛ الجبا مقصور ما حول البئر (maqayis_v4+maqayis_v5)
- **B004** seçip kendine yaklaştırmak — seçmek, özel bir yere ayırmak ve yakına getirmek · Yaratıcının bir kulunu seçip özel iyiliklere ayırması
  اجتبى الرجل الرجل إذا قربه (ayn)؛ اجتباه أي اصطفاه (sihah)؛ اختار لك الشيء واجتباه؛ يجتبيك ربك معناه يختارك ويصطفيك (tahdhib)؛ الاجتباء الجمع على طريق الاصطفاء؛ اجتباء الله العبد تخصيصه إياه (mufradat)
- **B005** onu kendin derleyip uydursaydın ya — Onu kendin derleyip uydursaydın ya!
  لولا اجتبيتها معناه هلا اختلقتها وافتعلتها من قبل نفسك (tahdhib)؛ هلا جمعتها تعريضا منهم بأنك تخترع هذه الآيات وليست من الله (mufradat)
- **B006** öne eğilmek veya diz çöküp yere kapanmak — öne eğilmiş duruş veya diz çöküp yüzüstü kapanma · bedenini toplayarak yere kapanmak
  التجبية ركوع كركوع المصلي؛ التجبية أن يجبي الرجل على وجهه باركا (ayn)؛ التجبية أن يقوم الإنسان قيام الراكع؛ أن يضع يديه على ركبتيه وهو قائم؛ أن ينكب على وجهه باركا (sihah)؛ جبى يجبي إذا سجد وهو تجمع (maqayis_v4+maqayis_v5)
- **B007** ürünü olgunlaşmadan alıp satmak — ekini veya tarla ürününü olgunluğu belli olmadan alıp satma · Ürünü olgunlaşmadan satan, yasak kazanca girmiş olur.
  الإجباء بيع الزرع قبل أن يبدو صلاحه؛ من أجبى فقد أربى؛ أصله الهمز (sihah)؛ الإجباء بيع الحرث قبل صلاحه؛ من أجبى فقد أربى (tahdhib)؛ أجبأت إذا اشتريت زرعا قبل بدو صلاحه؛ بعضهم يقوله بلا همز؛ من أجبى فقد أربى (maqayis_v4)

## ECHO ج ب ب (root_000214) — for جَابُوا۟ (w3): withheld observed target; not identity

- **B001** kokunden kesip ayirma — kokunden kesme ve koparma · onu kesip kokunden ayirdi · horgucu kokunden kesmek · horgucu kesilmis deve · erkeklik organlari kesilerek alinmis kisi
  الجب القطع (maqayis;sihah;mufradat)؛ استئصال السنام من أصله وبعير أجب (ayn;tahdhib)؛ كل شيء قطعته فقد جببته وخصي مجبوب (jamhara)
- **B002** ustun gelip geride birakma — toplulugu yenip asmak · kadinin diger kadinlari guzelligiyle gecmesi
  جبه إذا غلبه بحسنه أو غيره كأنه قطعه عن مساماته (maqayis)؛ والجب الغلبة (ayn)؛ جبت المرأة النساء إذا غلبتهن من حسنها (jamhara;tahdhib;mufradat)؛ فلان جب القوم إذا غلبهم (sihah)
- **B003** bedeni saran giysi — bedeni saran giysi · giyilen giysiler veya zırhlar · zırh adi olarak kullanilan giysi
  الجبة معروفة لأنها تشمل الجسم وتجمعه فيها (maqayis)؛ الجباب جمع الجبة التي تلبس (ayn)؛ الجباب التي تلبس (sihah)؛ الجبة التي تلبس والجبة من أسماء الدروع (tahdhib)؛ الجبة التي هي اللباس منه (mufradat)
- **B004** icine girilen yuva — mızrak ucunun sap giren yuvasi · goz cukuru ve cevresi · evin ortasi ve ici · tomurcugun ic kismi · boynuzdaki ilik yeri
  الجبة ما دخل فيه ثعلب الرمح من السنان (maqayis)؛ جبة السنان أي مدخله (ayn)؛ الجبة ما دخل فيه الرمح من السنان (sihah)؛ جبة العين حجاجها وجبة الدار وسطها وجب طلعة داخلها وجب القرن الذي فيه المشاشة (tahdhib)؛ به شبه ما دخل فيه الرمح من السنان (mufradat)
- **B005** deri veya iskembe kabi — toprak tasiyan deri sepet · et veya yag konan iskembe kabi · bu kaba et parcalari koymak veya ona gore hazirlanmak · bu tur kaplarin ticaretini yapmak
  الجبجبة زبيل من جلود يجمع فيه التراب والجبجبة الكرش يجعل فيه اللحم (maqayis)؛ الجبجبة الكرش يجعل فيها الخلع أو تذاب الإهالة فتحقن فيها والجبجبة أيضا زبيل من جلود ينقل فيه التراب (sihah)؛ الجبجبة زبيل من جلود ينقل فيه التراب والجبجبة الكرش يجعل فيها اللحم ويسمى الخلع (tahdhib)
- **B006** hurma asılama isi ve zamani [kalıp] — insanlarin hurmalari asılamasi · hurma asilama veya hurma isleri zamani
  وجب الناس النخل إذا ألقحوه وذا زمن الجباب (maqayis)؛ الجباب أيضا تلقيح النخل وقد جب الناس النخل (sihah)؛ إذا لقح الناس النخيل قيل قد جبوا وقد أتانا زمن الجباب (tahdhib)؛ كجب النخل وقيل زمن الجباب نحو زمن الصرام (mufradat)
- **B007** sert kalin toprak yuzeyi — sert veya kalin yer yuzeyi · yerden koparilan iri sert toprak kesegi
  الجبوب الأرض الغليظة (maqayis)؛ الجبوب وجه الأرض الصلبة (ayn)؛ الجبوب الأرض الغليظة ويقال وجه الأرض (sihah)؛ الجبوب وجه الأرض والأرض الغليظة والأرض الصلبة والمدر المفتت (tahdhib)؛ جبوب أي أرض غليظة (mufradat)
- **B008** ana yol hatti — ana yol ve yolun toplanma hatti
  المجبة جادة الطريق ومجتمعه (maqayis)؛ المجبة جادة الطريق (sihah)؛ ركب فلان المجبة وهي الجادة (tahdhib)
- **B009** kaplanmamis derin kuyu — kaplanmamis veya derin kuyu · genis icli kuyu veya kuyu ici · belirli bir su yeri adi
  الجب البئر (maqayis)؛ الجب البئر العميقة التي لا طي لها الكثيرة الماء البعيدة القعر (jamhara)؛ الجب البئر التي لم تطو وجمعها جباب وجببة (sihah)؛ الجب البئر التي لم تطو وبئر مجببة الجوف والقليب الواسعة الشحوة وركية تجاب في الصفا (tahdhib)؛ الجب أي بئر لم تطو (mufradat)
- **B010** kacis icin toparlanip savusma — kacip savusmak, kacis icin toparlanmak
  جببت تجبيبا إذا فر وذلك أنه يجمع نفسه للفرار ويتشمر (maqayis)؛ التجبيب أيضا النفار يقال جبب فلان فذهب (sihah)؛ جبب الرجل تجبيبا فهو مجبب إذا فر وعرد (tahdhib)
- **B011** deve sutu kopugu benzeri birikinti — deve sutu ustunde toplanan kopuk benzeri madde
  الجباب شيء يجتمع من ألبان الإبل كالزبد وليس للإبل زبد (maqayis)؛ الجباب كهيئة الزبد من ألبان الإبل (ayn)؛ الجباب بالضم شيء يعلو ألبان الإبل كالزبد ولا زبد لألبانها (sihah)؛ الجباب شبه الزبد يعلو ألبان الإبل ويجتمع عند فم السقاء (tahdhib)؛ الجباب شيء يعلو ألبان الإبل (mufradat)
- **B012** hayvan ayaginda beyaz nişan ve yuva — hayvan ayaginda yukariya uzanan beyazlik · beyazligi dizlerine kadar ulasan at · ayak-bacak birlesimi veya tirnak yuvasi
  الجبة بياض تطأ فيه الدابة بحافرها حتى تبلغ الأشاعر والنعت مجبب (ayn)؛ الجبة موصل الوظيف في الذراع ومغرز الوظيف في الحافر والتجبيب أن يبلغ التحجيل ركبة اليد وعرقوب الرجل (sihah)؛ المجبب الفرس الذي يبلغ تحجيله إلى ركبتيه وجبة الفرس ملتقى الوظيف في أعلى الحوشب والجبب جمع جبة وهو وعاء الحافر (tahdhib)
- **B013** dikilmis su tulumu — parcalari birbirine dikilmis su tulumu
  نهى النبي عن الجب قيل هو المزادة يخيط بعضها إلى بعض (tahdhib)
- **B014** siddetli kuraklik — siddetli kuraklik
  الجباب القحط الشديد (tahdhib)
- **B015** iri yanli ve dolgun bedenli olma — iri yanli veya iri bedenli · zayifliktan sonra bedeni buyumek veya semirmek
  رجل جباجب ومجبجب إذا كان ضخم الجنبين ونوق جباجب وجمل جباجب وبجابج ضخم وقد جبج إذا عظم جسمه بعد ضعف وجبجب إذا سمن (tahdhib)
- **B016** sığ sudaki su kayasi — sığ sudaki su kayasi
  الجبجبة أتان الضحل وهو صخرة الماء (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:9, and ## Buluşmalar) =====
## Su: fışkıran, taşan, yukarıdan dökülen

İlk kelimenin kökü, karanlıktan önce suyun yarılmasını anlatır: {ar:انفجر الماء انفجارا تفتح, tr:infecera'l-mâu'nficâran tefettah, gloss:su fışkırdı, önü açıldı, source:"ف ج ر,B001"}. Fışkırma şöyle tarif edilir: {ar:إذا انبعث سائلا, tr:ize'nbe'ase sâilen, gloss:akarak fırladığında, source:"ف ج ر,B001"}. Kaya ya da toprak bir noktada çatlar, içerideki su bastırarak dışarı fırlar ve akmaya başlar. Kur'an bu sahneyi taşın içinden kurar. İsrailoğullarına kalplerinin taştan da katı olduğu söylenirken bazı taşlardan ırmakların fışkırdığı hatırlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi var ki içinden ırmaklar fışkırır, source:2:74}. Nuh'un tufanında aynı fiil yeryüzünü kaynaklara çevirir ve su ölçüsü önceden belirlenmiş bir iş üzerinde buluşur: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ, tr:ve feccernâ'l-arda uyûnen fe'lteka'l-mâu alâ emrin kad kudir, gloss:yeri kaynaklar hâlinde fışkırttık, su takdir edilmiş bir iş üzerinde buluştu, source:54:12}. Kıyamette denizler fışkırtılır: {ar:وَإِذَا ٱلْبِحَارُ فُجِّرَتْ, tr:ve ize'l-bihâru fuccirat, gloss:denizler fışkırtıldığında, source:82:3}. Mekke'de inkârcılar Peygamber'den, arasından ırmaklar fışkırttığı bir bahçe isterler {source:17:91}. Kur'an bu işi cennette Allah'ın kullarına verir: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdu'llâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği, dilediklerince fışkırttıkları bir kaynak, source:76:6}.

Aynı kök günahı da adlandırır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-me'âsî fucûrâ, gloss:günahlara atılmak ve açılmak, fücur, source:"ف ج ر,B004"}. Suyun önünü yarıp fırlaması ile insanın günaha açılıp atılması aynı kelimeyle söylenir. Bu yüzden surenin geçmiş kavimleri anlatan bölümü bir sel gibi duyulur.

Dokuzuncu ayette Semûd kayayı vadide oymuştur: {ar:بِٱلْوَادِ, tr:bi'l-vâd, gloss:vadide, source:89:9}. Vadi selin yoludur: {ar:كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل, tr:kullu mufracin beyne cibâlin ve âkâmin ve tilâlin yekûnu meslekan li's-seyl, gloss:dağlar, tepeler ve tümsekler arasında selin geçtiği her açıklık, source:"و د ي,B005"}. Kök akmayı adlandırır: {ar:ودى أي سال, tr:vedâ ey sâl, gloss:aktı, source:"و د ي,B001"}. Kaya evler suyun indiği yatağa kurulmuştur. Kur'an'ın sel benzetmesinde vadiler kendi ölçüleri kadar akar ve sel kabarık bir köpük taşır: {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا, tr:fe-sâlet evdiyetun bi-kaderihâ fahtemele's-seylu zebeden râbiyâ, gloss:vadiler ölçülerince aktı, sel kabarık bir köpük taşıdı, source:13:17}. Köpük gider, insanlara yarayan yerde kalır. Âd da vadilerine doğru gelen bulutu yağmur sanmıştır. Hûd'un Ahkâf'ta kavmini uyarmasıyla başlayan sahnede {source:46:21} bulutu görünce şöyle derler: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا ۚ بَلْ هُوَ مَا ٱسْتَعْجَلْتُم بِهِۦ ۖ رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:kâlû hâzâ âridun mumtırunâ, bel huve me'sta'celtum bih, rîhun fîhâ azâbun elîm, gloss:"Bu bize yağmur getiren bir bulut" dediler. Hayır, o acele istediğiniz şeydir: içinde acı bir azap olan bir rüzgâr, source:46:24}.

On birinci ayetin fiili suyun taşmasıdır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:o ülkelerde azanlar, source:89:11}. Arapçada sel için {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel bol suyla gelince "taştı" denir, source:"ط غ ي,B002"}, su için de {ar:طغى الماء خروجه عن المقدار, tr:tuğyânu'l-mâi hurûcuhû ani'l-mikdâr, gloss:suyun taşması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} denir. Ayette anlam azgınlıktır. Yanında ölçüsünden çıkan, yatağını aşan su duyulur. Kur'an kelimeyi tufan için doğrudan kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayet taşkının sonucunu verir: {ar:فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ, tr:fe-ekserû fîhe'l-fesâd, gloss:oralarda bozgunu çoğalttılar, source:89:12}. Çoğalmak {ar:الكثرة نماء العدد, tr:el-kesretu nemâu'l-aded, gloss:çokluk, sayının büyümesidir, source:"ك ث ر,B001"} demektir, bozulmak da {ar:الفساد خروج الشيء عن الاعتدال, tr:el-fesâdu hurûcu'ş-şey'i ani'l-i'tidâl, gloss:fesat, bir şeyin dengeden çıkmasıdır, source:"ف س د,B001"}. Hacim büyür ve şeyler dengelerinden çıkar. Bozgunun tarifindeki "çıkış" suyun ölçüden çıkışıyla aynı kelimedir. Kur'an'da bozgun karaya ve denize yayılır: {ar:ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:zahera'l-fesâdu fi'l-berri ve'l-bahr, gloss:karada ve denizde bozgun ortaya çıktı, source:30:41}. Salih de Semûd'a, Âd'dan sonra yerleştirildikleri yeryüzünde ovalardan saraylar edinip dağları ev diye oyduklarını hatırlatır ve sonra şöyle der: {ar:وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ, tr:ve lâ ta'sev fi'l-ardı mufsidîn, gloss:yeryüzünde bozguncular olarak dolaşmayın, source:7:74}.

On üçüncü ayet taşkına yukarıdan karşılık verir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üzerlerine azap kamçısı yağdırdı, source:89:13}. Sabb, suyun fiilidir: {ar:صب الماء إراقته من أعلى, tr:sabbu'l-mâi irâkatuhû min a'lâ, gloss:suyu dökmek, onu yukarıdan akıtmaktır, source:"ص ب ب,B001"}. Vadiye inmek de bu fiille söylenir: {ar:صب في الوادي إذا انحدر فيه, tr:sabbe fi'l-vâdî izenhadera fîh, gloss:vadiye indi, oraya doğru aktı, source:"ص ب ب,B002"}. Aşağıda yatağını taşan suya yukarıdan dökülen bir şey karşılık verir. Dökülenin adı azaptır ve bu kelimenin harfleri tatlı suyu da adlandırır: {ar:العذب ضد الملح وكل مستسيغ من طعام أو شراب, tr:el-azbu diddu'l-milhi ve kullu mustesâğin min taâmin ev şarâb, gloss:azb, tuzlunun zıddıdır; boğazdan rahat geçen her yiyecek ve içecek, source:"ع ذ ب,B001"}. Âd'ın yağmur sandığı rüzgâr bu iki yüzü tek sahnede gösterir: beklenen tatlı su, gelen ise azaptır {source:46:24}.

Aynı su sahnesi surenin ikinci yarısında rahmet olarak döner. Kur'an insana yemeğine bakmasını söyler: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şekakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Fiil aynıdır, ama bu kez arkasından yarılan toprak ve biten yemek gelir. Surenin sınav sahnesindeki kelimeler bu yağmuru da taşır. İkram için {ar:كرم السحاب أتى بالغيث, tr:keruma's-sehâbu etâ bi'l-ğays, gloss:bulut cömert davrandı, yağmur getirdi, source:"ك ر م,B002"} denir. Rızık için {ar:وقد يسمى المطر رزقا, tr:ve kad yusemma'l-mataru rızkâ, gloss:yağmura da rızık denir, source:"ر ز ق,B003"} denir. Kur'an da şöyle der: {ar:وَفِى ٱلسَّمَآءِ رِزْقُكُمْ, tr:ve fi's-semâi rızkukum, gloss:rızkınız göktedir, source:51:22}. Ölçü için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-mataru bi-mikdâr, gloss:yağmur ölçüyle iner, source:"ق د ر,B001"} denir. On altıncı ayette rızkın daraltılması, yağmurun ölçüyle inmesinin insanın gözünden görünen yüzüdür. Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında yağmur duyulur: {ar:الحيا المطر لأنه يحيي الأرض بعد موتها, tr:el-hayâ el-mataru li-ennehû yuhyi'l-arda ba'de mevtihâ, gloss:hayâ yağmurdur, çünkü yeri ölümünden sonra diriltir, source:"ح ي ي,B002"}. Yirmi sekizinci ayetteki "dön" kelimesinin yanında da dökülüp yeniden gelen yağmur duyulur: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-rec'u el-ğaysu ve huve'l-mataru li-ennehâ tuğîsu ve tasubbu summe terci'u fe-tuğîs, gloss:rec' yağmurdur, çünkü yağar, dökülür, sonra döner ve yine yağar, source:"ر ج ع,B006"}. Kur'an da göğe dönüşüyle yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâi zâti'r-rec', gloss:dönüp dönüp yağan göğe, source:86:11}. Ölü toprağa yağmur gönderilmesi, ölülerin çıkarılmasının örneğidir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhricu'l-mevtâ leallekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Son kelime bu suyun ürününe varır: bahçeye ve bitkinin gürleşip çiçek açmasına: {ar:جن النبت جنونا إذا اشتد وخرج زهره, tr:cenne'n-nebtu cunûnen izeştedde ve harace zehruh, gloss:bitki gürleşip çiçeğini çıkarınca "cenne" denir, source:"ج ن ن,B011"}.

Surede suyun işleyişi bir ölçüye bağlanır. Ölçüsünde kalan su hayat verir, ölçüsünü aşan su süpürür. Âd, Semûd ve Firavun ölçüyü aşan taşkındır ve onlara yukarıdan azap dökülür. İnsana ölçülü rızık iner ve o, ölçünün kendisini aşağılanma sanır.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B001; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:9 بِٱلْوَادِ و د ي B001; 89:9 بِٱلْوَادِ و د ي B005; 89:11 طَغَوْا۟ ط غ ي B002; 89:12 فَأَكْثَرُوا۟ ك ث ر B001; 89:12 ٱلْفَسَادَ ف س د B001; 89:13 فَصَبَّ ص ب ب B001; 89:13 فَصَبَّ ص ب ب B002; 89:13 عَذَابٍ ع ذ ب B001; 89:15 فَأَكْرَمَهُۥ ك ر م B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B003; 89:24 لِحَيَاتِى ح ي ي B002; 89:28 ٱرْجِعِىٓ ر ج ع B006; 89:30 جَنَّتِى ج ن ن B011

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

