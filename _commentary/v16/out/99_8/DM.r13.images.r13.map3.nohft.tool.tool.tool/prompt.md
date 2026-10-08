Focus: 99:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_8/D.r13/context.md =====
# 99:8 — focus

وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ

Anchor translation (canonical reading, reference only):

Kim de zerre ağırlığınca kötülük yaparsa onu görür.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَن | مَن |  | CONJ;COND |
| 2 | يَعْمَلْ | عَمِلَ | ع م ل | V |
| 3 | مِثْقَالَ | مِثْقَال | ث ق ل | N |
| 4 | ذَرَّةٍ | ذَرَّة | ذ ر ر | N |
| 5 | شَرًّا | شَرّ | ش ر ر | N |
| 6 | يَرَهُۥ | رَءَا | ر ء ي | V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 99 — full text (context; no pericope)

- 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 ◀ focus وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع م ل (root_001046) — identity root of يَعْمَلْ (w2)

- **B001** bilerek yapılan iş veya eylem — bilerek yapılan iş veya eylem · iş yapan kimse · kendisi için çalışmak veya işe koyulmak · iş veya uğraş · işte kullanılan sığırlar · iyi ve kötü davranışlar
  أصل واحد صحيح وهو عام في كل فعل يفعل (maqayis); عمل عملا فهو عامل (ayn;sihah;tahdhib); كل فعل يكون من الحيوان بقصد (mufradat); الأعمال الصالحة والسيئة (mufradat)
- **B002** işe koşmak veya kullanmak — onu çalıştırdı · onu kullandı veya çalıştırdı · ondan çalışmasını istedi · görüşünü, sözünü veya mızrağını kullandı · kerpici yapıda kullandı · zihnini işletip düşündü
  يستعمل غيره ويعمل رأيه أو كلامه أو رمحه؛ والبناء يستعمل اللبن (maqayis); أعمله غيره واستعمله بمعنى؛ واستعمله أيضا أي طلب إليه العمل (sihah); أعمل فلان ذهنه في كذا وكذا إذا دبره بفهمه (tahdhib)
- **B003** işe görevli kılma veya görev üstlenme — bağışları toplayan görevliler · bağış işi görevlisi · resmi bir işi üstlendi · birine iş görevi verme · bir kimseyi bir şehirde görevli kılmak
  العاملين عليها هم السعاة الذين يأخذون الصدقات (tahdhib); استعمل فلان إذا ولي عملا من أعمال السلطان (tahdhib); التعميل تولية العمل (sihah); العاملين عليها هم المتولون على الصدقة (mufradat)
- **B004** iş ücreti — iş karşılığı ücret veya pay · iş ücreti
  العمالة أجر ما عمل (maqayis); العمالة بالضم رزق العامل (sihah); العمالة رزق العامل (tahdhib); العملة والعمالة أجر العمل (tahdhib); العمالة أجرته (mufradat)
- **B005** karşılıklı işlem — karşılıklı işlem veya alışveriş ilişkisi · bir kimseyle alışveriş veya benzeri işlem yaptı
  المعاملة مصدر من قولك عاملته وأنا أعامله معاملة (maqayis); عاملت الرجل أعامله معاملة في المبايعة وغيرها (tahdhib)
- **B006** el işçileri — elleriyle çalışan işçi topluluğu
  العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه (maqayis); العملة القوم الذين يعملون بأيديهم ضروبا من العمل في طين أو حفر أو غيره (tahdhib)
- **B007** zahmete girmek [kalıp] — kendini yorma · ihtiyacın için zahmete gireceğim · zahmet etme
  لا تتعمل في أمرك ذا كقولك لا تتعن (tahdhib); سوف أتعمل في حاجتك أي أتعنى (tahdhib); لا تعمل أي لا تتعن (tahdhib)
- **B008** işe yatkın ve dayanıklı — işe yatkın üstün dişi deve · işe nispet edilen dişi deve · işe yatkın adam · işe yatkın çalışkan adam · işe yatkın, güçlü ve üstün dişi deve
  اليعملة من الإبل اسم لها اشتق من العمل (maqayis); رجل عمل بكسر الميم أي مطبوع على العمل؛ ورجل عمول؛ اليعملة الناقة النجيبة المطبوعة على العمل (sihah); ناقة عملة بينة العمالة مثل اليعملة إذا كانت فارهة (tahdhib); اليعملة مشتقة من العمل (mufradat)
- **B009** mızrak ucunun alt bölümü — mızrağın sivri ucuna yakın ön gövde bölümü · mızrağın ucuna yakın gövde bölümü
  عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره (maqayis); عامل الرمح ما يلي السنان وهو دون الثعلب (sihah); عامل الرمح صدره دون السنان ويجمع عوامل (tahdhib); عامل الرمح ما يلي السنان (mufradat)
- **B010** iş gören beden parçası [kalıp] — hayvanın ayakları · uzağı gören göz
  عوامل الدابة قوائمه واحدها عاملة (tahdhib); وترقبه بعاملة قذوف أي ترقبه بعين بعيدة النظر (tahdhib)
- **B011** işlek yol [kalıp] — işlek ve belirgin yol
  طريق معمل أي لحب مسلوك (sihah)
- **B012** yaya yolcular [kalıp] — yaya giden yolcular
  المسافرون إذا مشوا على أرجلهم يسمون بني العمل (tahdhib)

## ث ق ل (root_000202) — identity root of مِثْقَالَ (w3)

- **B001** ağırlık — bir şeyin ağır gelmesi, hafif olmaması · ağırlık, maddi ya da soyut ağır gelme niteliği · ağır, ağırlık taşıyan
  ضد الخفة (maqayis;sihah)؛ ثقل ثقلا فهو ثقيل والثقل رجحان الثقيل (ayn;tahdhib)؛ الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني (mufradat)
- **B002** ağır yükler — yolcunun eşyası ve beraberindeki taşınır yük · yükler, eşyalar veya yerin çıkardığı ağır şeyler · yüklerinizi taşır
  أثقال الأرض كنوزها وأجساد بني آدم (maqayis;sihah;mufradat)؛ متاع المسافر وحشمه وجمعه أثقال (ayn;sihah;tahdhib)؛ تحمل أثقالكم أي أحمالكم الثقيلة (mufradat)
- **B003** günah yükü — kişiyi ağırlaştıran günahlar ve sorumluluklar · günah yüküyle ağırlaşmış kimse
  الأثقال الآثام (ayn)؛ حاملة أوزار وخطايا (ayn)؛ أوزارهم وأوزار من أضلوا وهي الآثام (tahdhib)؛ أثقالهم آثامهم التي تثقلهم وتثبطهم (mufradat)
- **B004** ölçü ağırlığı — bilinen ağırlık ölçüsü veya tartı ağırlığı · bir şeyin ağırlığı kadar ölçü · ona ağırlığını ver · hayvanı tartıp ağırlığını yokladı · ağırlığı eksik olmayan dinar
  المثقال وزن معلوم قدره ومثقال الشيء ميزانه من مثله (ayn;tahdhib)؛ أعطه ثقله أي وزنه وثقلت الشاة (sihah;tahdhib)؛ المثقال ما يوزن به وهو اسم لكل سنج (mufradat)
- **B005** değer ağırlığı — kıymetli, korunmuş veya itibarlı şey · büyük önemleri sebebiyle birlikte anılan iki varlık ya da değerli iki emanet · büyük değeri ve etkisi olan söz
  سمي الجن والإنس الثقلين (maqayis;sihah;tahdhib)؛ كل شيء نفيس مصون ثقل ويقال للسيد العزيز ثقل (tahdhib)؛ قولا ثقيلا يعني عظم قدره وجلالة خطره وقول له وزن (tahdhib)؛ الثقيل في الإنسان يستعمل في المدح (mufradat)
- **B006** ağırlık ve halsizlik — içte, bedende veya yemekten sonra duyulan ağırlık ve gevşeklik · bastıran uyku hali · hastalık onu ağırlaştırdı · uyku ona ağır bastı · ağırlaşmış, yavaş veya gücünü aşan yük altında kalmış · ağırdan alma, yavaşlama ve ayak sürüme · sözün kulağa hoş gelmemesi veya kabulünün ağır gelmesi
  أجد في نفسي ثقلة (maqayis)؛ الثقلة نعسة غالبة وأثقله المرض واستثقله النوم والمثقل البطيء والتثاقل من التباطؤ (ayn)؛ وجدت ثقلة في جسدي أي ثقلا وفتورا (sihah)؛ الثقلة ما وجد الإنسان من ثقل الطعام وأصبح ثاقلاء أثقله المرض (tahdhib)؛ اثاقلتم إلى الأرض (mufradat)
- **B007** gebelikte ağırlaşma — kadının gebelik yüküyle ağırlaşması · gebeliği ağırlaşmış kadın
  اثقلت المرأة فيه مثقل (ayn)؛ أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها (sihah)؛ المثقل من النساء التي قد ثقلت من حملها (tahdhib)
- **B008** dolgun kalçalı ağırbaşlı kadın [kalıp] — dolgun kalçalı veya mecliste ağırbaşlı kadın
  امرأة ثقال أي ذات مآكم وكفل (ayn;sihah;tahdhib)؛ هذه امرأة ثقال وهذه امرأة رزان أي رزينة في مجلسها (tahdhib)
- **B009** işitme ağırlığı [kalıp] — kulağında ağırlık var, işitmesi zayıf
  في أذنه ثقل إذا لم يجد سمعه كأنه يثقل عن قبول ما يلقى إليه (mufradat)

## ذ ر ر (root_000511) — identity root of ذَرَّةٍ (w4)

- **B001** küçük karıncalar ve bunlardan biri — küçük karıncalar; tekil biçimin çoğulu · küçük karıncalardan biri, en küçük karınca · küçük karınca adından türetilmiş erkek adı · küçük karınca adından türetilmiş erkek lakabı
  الذر صغار النمل الواحدة ذرة (maqayis)؛ الذر جمع ذرة وهي أصغر النمل (sihah)
- **B002** taneli ya da toz maddeyi serperek dağıtmak — tahıl, ilaç veya tuzu serperek dağıtmak · serpip dağıtma
  ذررت الملح والدواء (maqayis)؛ ذررت الحب والدواء والملح أذره ذرا فرقته (sihah)
- **B003** bilinen ince toz veya hoş kokulu madde — bilinen ince bir toz veya hoş kokulu madde · aynı maddenin dilsel varyantı olan ad · bu varyant adın çoğul biçimi
  الذريرة معروفة (maqayis)؛ الذرور بالفتح لغة في الذريرة (sihah)
- **B004** güneşin ince ışıkla doğması ya da bitkinin yerden çıkması — güneşin doğup ince, yayılmış ışığını göstermesi · güneşin doğuşu · gün doğduğu sürece · güneşin kenarı göründüğü sürece · bitkinin topraktan çıkması
  ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر (maqayis)؛ ما ذر شارق وما ذر قرن الشمس (maqayis)؛ ذر البقل إذا طلع من الأرض (maqayis;sihah)؛ ذرت الشمس تذر ذرورا طلعت (sihah)
- **B005** huysuzlaşmak veya öfkeyle yüz çevirmek — 
  ذارت الناقة وهي مذار إذا ساء خلقها (maqayis)؛ ذارت الناقة تذار مذارة وذرارا أي ساء خلقها وهي مذار (sihah)؛ في فلان ذرار أي إعراض غضبا كذرار الناقة (maqayis;sihah)

## ش ر ر (root_000787) — identity root of شَرًّا (w5)

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## ر ء ي (root_000531) — identity root of يَرَهُۥ (w6)

- **B001** gözle ya da içsel kavrayışla görme — gözle ya da içsel kavrayışla görmek · görme, gözle algılama · kendi gözüyle görme · yeni ayı görebilmek için dikkatle bakmaya çalıştık
  نظر وإبصار بعين أو بصيرة (maqayis)؛ رأيت بعيني رؤية ورأيته رأي العين (ayn;tahdhib)؛ الرؤية بالعين (sihah)؛ الرؤية إدراك المرئي بالحاسة (mufradat)
- **B002** düşünüp bir görüşe varma — bilmek, sanmak veya öyle olduğuna inanmak · görüş, kanı veya değerlendirme · düşünüp taşınmak ve bir görüşe varmak · ağır ağır ve dikkatle düşünme · bir görüşe varmak için düşünme · adamın görüşünü sordu · onunla görüş alışverişinde bulundu · gözle gördüğünün gereğince öyle sandı
  الرأي ما يراه الإنسان في الأمر (maqayis)؛ الرأي رأي القلب (ayn;tahdhib)؛ بمعنى العلم تتعدى إلى مفعولين ورأى في الفقه رأيا (sihah)؛ الرأي اعتقاد النفس والروية والتروية التفكر (mufradat)؛ استرأيت الرجل في الرأي أي استشرته (tahdhib)
- **B003** uykuda görülen düş — uykuda görülen düş · uykuda görülen düşler
  الرؤيا معروفة والجمع رؤى (maqayis)؛ رأيت رؤيا حسنة (ayn)؛ رأى في منامه رؤيا وجمع الرؤيا رؤى (sihah)؛ لا تجمع الرؤيا وتجمع الرؤيا رؤى (tahdhib)؛ الرؤيا ما يرى في المنام (mufradat)
- **B004** karşı karşıya gelip görünür olma — topluluk birbirini gördü · görünmek üzere karşıma çıktı · birbirine bakar ve karşılıklı konumda
  تراءى القوم إذا رأى بعضهم بعضا (maqayis)؛ تراءى القوم رأى بعضهم بعضا وتراءى لي فلان (ayn)؛ قوم رئاء وبيوتهم رئاء وتراءى الجمعان (sihah)؛ تراءينا أي تلاقينا فرأيته ورآني وداري ترى دار فلان (tahdhib)؛ تراءا الجمعان أي تقاربا وتقابلا ومنازلهم رئاء (mufradat)
- **B005** başkaları görsün diye yapma — başkaları görsün diye yapma · işini başkalarına gösteriş için yaptı · gösteriş yapmaya zorlandı veya özendi
  وراءى فلان يرائي وفعل ذلك رئاء الناس وهو أن يفعل شيئا ليراه الناس (maqayis)؛ فلان مراء والاسم الرياء وفعل ذلك رياء وسمعة (sihah)؛ يرآءون الناس إذا أبصرهم الناس صلوا وإذا لم يروهم تركوا الصلاة (tahdhib)؛ فعل ذلك رئاء الناس أي مراءاة (mufradat)
- **B006** görünüş, belirti ve yansıtıcı yüzey — ayna · aynada yüzüne baktı · güzel ve parlak dış görünüş · göze güzel görünen durum veya donanım · yüzde beliren budalalık belirtisi
  الرئي ما رأت العين من حال حسنة والرواء حسن المنظر والمرآة معروفة (maqayis)؛ المرآة التي ينظر فيها والري ما أريت القوم من حسن الشارة والهيئة والرواء حسن المنظر (ayn)؛ المرآة التي ينظر فيها والمرآة المنظر الحسن والرواء حسن المنظر ورأوة الحمق (sihah)؛ الرئي المنظر والرواء حسن المنظر والمرآة التي ينظر فيها ورأوة أي نظرة ودمامة (tahdhib)؛ المرآة ما يرى فيه صورة الأشياء (mufradat)
- **B007** aybaşı sonu izi ve denetleme bezi — aybaşı sonrası hafif sarı, beyaz veya bulanık iz · aybaşı belirtisi olarak görülen iz
  الترئية والترية ما تراه الحائض من صفرة بعد دم حيض أو أمارات الحيض (maqayis)؛ الترية الخرقة التي تعرف بها المرأة حيضها من طهرها والماء الأصفر عند انقطاع الدم (jamhara)؛ الترية الشيء الخفي اليسير من الصفرة والكدرة (sihah)؛ الترية ما تراه المرأة من بقية حيضها من صفرة أو بياض (tahdhib)
- **B008** kişiye görünen görünmez yoldaş — kişiye alışıp onunla ilişki kuran görünmez varlık · görünmez yoldaşı ona göründü
  الرئي جني يتعرض للرجل يريه كهانة وطبا (ayn)؛ به رئي من الجن أي مس (sihah)؛ رئي من الجن وهو الذي يعتاد الإنسان من الجن وأرأى إذا صار له رئي من الجن (tahdhib)؛ مع فلان رئي من الجن (mufradat)
- **B009** akciğer ve ona gelen zarar — akciğer · akciğerine vurdu veya sapladı · akciğerinden yakındı
  الرئة موضع الريح والنفس وجمعها الرئات والرئين (ayn)؛ الرئة مهموزة وتجمع على رئين ورأيته أي أصبت رئته (sihah)؛ أرأى إذا اشتكى رئته (tahdhib)؛ الرئة العضو المنتشر عن القلب ورئته إذا ضربت رئته (mufradat)
- **B010** meme gelişmesiyle gebeliğin belli olması — dişi devenin gebeliği memesi gelişince belli oldu · dişi koyunun gebeliği memesi büyüyünce belli oldu
  أرأت الناقة إذا أرأى ضرعها أنها أقربت وأنزلت (ayn)؛ أرأت الشاة إذا عظم ضرعها قبل ولادها (sihah)؛ إذا استبان حمل الشاة وعظم ضرعها قيل أرأت (tahdhib)؛ أرأت الناقة إذا أظهرت الحمل حتى يرى صدق حملها (mufradat)
- **B011** görünür yere dikilen bayrak — dikili bayrak veya görünür işaret · bayrağı dikti
  الراية من رايات الأعلام (ayn)؛ الراية العلم لا تهمزها العرب وأصلها الهمز (tahdhib)؛ الراية العلامة المنصوبة للرؤية (mufradat)
- **B012** gösterip görmesini sağlama — bakması için aynayı ona tuttu · ona gösterip görmesini sağladı · ver, uzat · Tanrı onu düşmanını sevindirecek bir duruma düşürdü
  أرني يا فلان ثوبك لأراه وأرنا للمعاطاة (ayn)؛ أريته الشيء فرآه (sihah)؛ رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها وأرى الله الناس بفلان (tahdhib)؛ أرنا وبما أراك الله أي بما علمك (mufradat)
- **B013** söyler misin, bir düşün — söyler misin, bir düşün · söyleyin bakalım, bir düşünün
  أرأيتك وأنت تقول أخبرني (tahdhib)؛ يجري أرأيت مجرى أخبرني وكل ذلك فيه معنى التنبيه (mufradat)

## ECHO  () — for ذَرَّةٍ (w4): non-dominant observed target (1 occ.); not identity

- () no Turkish dictionary entry

## ECHO ش ر ي (root_000792) — for شَرًّا (w5): withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

## ECHO ر و ي (root_000615) — for يَرَهُۥ (w6): withheld observed target; not identity

- **B001** suya kanma ve susuzluğun giderilmesi — susuzluğu sona erinceye kadar su içmek · suya kanmak · suya kanmışlık; susuzluğun sona ermesi · suya kanmış, susuzluğu kalmamış · tatlı ve içeni iyice kandıran bol su · bol sulu pınar
  خلاف العطش (maqayis)؛ رويت من الماء ريا وارتويت وترويت (sihah)؛ روي فلان من الماء يروى ريا فهو ريان (tahdhib)؛ ماء رواء وروى (sihah;tahdhib;mufradat)؛ عين رية (sihah)
- **B002** başkaları için su çekip getirme — ailesine su getirip taşımak · topluluk için su çekmek · su çekmede kullanılan yük hayvanı veya su çeken kişi · su taşımaya yarayan büyük tulum · su taşıma işini meslek edinen kimse · hacıların sonraki günler için su tedarik ettiği gün
  رويت على أهلي أروي ريا (maqayis;sihah;tahdhib)؛ رويت القوم أرويهم إذا استقيت لهم (sihah;tahdhib)؛ الراوية البعير أو البغل أو الحمار الذي يستقى عليه (sihah)؛ الراوية هو البعير الذي يستقى عليه الماء والرجل المستقي أيضا راوية (tahdhib)؛ يوم التروية سمي به لأنهم يرتوون فيه من الماء (sihah;tahdhib)
- **B003** anlatı veya şiir aktarma — anlatıyı veya şiiri aktarmak · anlatı veya şiir aktaran kimse · çok sayıda şiir ya da anlatı aktaran kimse · birine şiiri tekrar ederek ezberletmek
  رويت الحديث والشعر رواية فأنا راو (sihah)؛ روى فلان حديثا وشعرا يرويه رواية فهو راو (tahdhib)؛ روى فلان فلانا شعرا إذا رواه له حتى حفظه للرواية عنه (tahdhib)؛ الذي يأتي القوم بعلم أو خبر فيرويه كأنه أتاهم بريهم من ذلك (maqayis)
- **B004** enine boyuna düşünüp değerlendirme — enine boyuna düşünme; değerlendirme · bir mesele üzerinde düşünüp değerlendirmek
  الرَّوِيَّة التفكر في الأمر (sihah)؛ رويت في الأمر إذا نظرت فيه وفكرت (sihah)؛ روأت في الأمر وريأت فكرت (tahdhib)
- **B005** birinden beklenen ihtiyaç veya talep [kalıp] — birinden beklenen ihtiyaç veya talep
  لنا قبلك روية أي حاجة (sihah)؛ لنا عند فلان روية وأشكلة وهما الحاجة (tahdhib)
- **B006** geriye kalan bölüm veya miktar — borçtan ya da başka bir şeyden kalan miktar
  الرَّوِيَّة البقية من الدين ونحوه (sihah)؛ بقيت منه روية أي بقية مثل التلية (tahdhib)
- **B007** yük bağlama ipi — yükü veya su tulumlarını yük hayvanına bağlayan ip · yükü veya su tulumlarını özel iple hayvana bağlamak · su tulumlarını yük hayvanına bağlayan ip
  الرِّوَاء حبل يشد به المتاع على البعير (sihah)؛ رويته على الرجل إذا شددته على ظهر البعير (sihah)؛ الرِّوَاء الحبل الذي يروى به على الراوية إذا عكمت المزادتان (tahdhib)؛ يقال له المروى وجمعه مراوى (tahdhib)
- **B008** yapıya göre dolgunlaşma veya suya kavuşma [kalıp] — ipin lifleri kalınlaşıp bükümü sıkılaşmak · eklemler dengeli ve dolgun hale gelmek · sırtı semirip dolgunlaşmış at · kurak yere dikildikten sonra kökten sulanmak
  ارتوى الحبل غلظت قواه (sihah)؛ ارتوت مفاصل الرجل اعتدلت وغلظت (sihah)؛ ارتوت مفاصل الدابة إذا اعتدلت وغلظت (tahdhib)؛ فرس ريان الظهر إذا سمن متناه (tahdhib)؛ ارتوت النخلة إذا غرست في قفر ثم سقيت في أصلها (tahdhib)
- **B009** hoş ve güzel dış görünüş — hoş dış görünüş; görünen güzellik · kökeni tartışmalı bir görünüş güzelliği biçimi
  رجل له رُوَاء أي منظر (sihah)؛ من لم يهمز رئيا جعله من روي كأنه ريان من الحسن (mufradat)
- **B010** hoş koku — hoş koku; bir şeyin güzel kokusu
  طيبة الرِّيَا إذا كانت عطرة الجرم (tahdhib)؛ ريا كل شيء طيب رائحته (tahdhib)
- **B011** dişi dağ keçisi — dağ keçisi; özellikle dişisi, bazı kullanımlarda erkeği de · çok sayıda dağ keçisi; dağ keçileri topluluğu · kadın adı
  الإِرْوِيَّة الأنثى من الوعول (sihah)؛ أروى أيضا اسم امرأة (sihah)؛ الأُرْوِيَّة الأنثى من الوعول (tahdhib)؛ يقال للأنثى أروية وللذكر أروية (tahdhib)؛ لا تجمع بين الأروى والنعام (tahdhib)
- **B012** bayrak — bayrak; sancak
  الرَّايَة العلم (sihah)
- **B013** temel uyak harfi — şiir boyunca değişmeyen temel uyak harfi
  الرَّوِيّ حرف القافية (sihah)؛ قصيدتان على روي واحد (sihah)
- **B014** iri damlalı güçlü yağmur bulutu — iri damlalı, sert yağan yağmur bulutu
  الرَّوِيّ سحابة عظيمة القطر شديدة الوقع (sihah)
- **B015** topluluğun ağır yükümlülüklerini üstlenen ileri gelenler — topluluk adına kan bedeli ve ağır yükümlülükleri üstlenen ileri gelenler
  يقال لسادة القوم الروايا (tahdhib)؛ شبه السيد الذي تحمل الديات عن الحي بالبعير الراوية (tahdhib)؛ روايا الثقل حوامل ثقل الديات (tahdhib)

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:8, and ## Buluşmalar) =====
## İçerinin çıkarılıp gösterilmesi

Sure boyunca içerdeki şeyler görünüre doğru hareket eder. Yerin ağırlıkları yer altındadır, hazineler göz önünden gömülüdür {source:"ث ق ل,B002"}. Çıkarmak, gizli olanı çekip almak, gömülü suyu yukarı çekmek gibidir {ar:الاستخراج كالاستنباط, tr:el-istihrâc kel-istinbât, gloss:çıkarıp almak, gizli suyu çekip çıkarmak gibidir, source:"خ ر ج,B002"}. Yerin haberleri işlerin içidir; anlatmak ise açığa çıkarmaktır {ar:الحدث الإبداء, tr:el-hadsu el-ibdâ’, gloss:açığa vurmak, source:"ح د ث,B006"}, hatta bir kılıcı cilalayıp donuk tabakasını gidermektir {ar:أحدث الرجل سيفه وحادثه إذا جلاه, tr:ahdeser-raculu seyfehû ve hâdesehû izâ celâh, gloss:kılıcını cilaladığında "ahdese" denir, source:"ح د ث,B007"}. Yer anlattıkça yüzeyi parlar ve altındaki görünür.

Altıncı ayette yön insana döner: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Fiil edilgendir: insanlar görmeye getirilir. Görme kökünün ettirgen kullanımı birine bir şeyi gösterip gördürmektir, birine ayna tutup bakmasını sağlamaktır {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra’eytur-racule ter’iyeten izâ emsektu lehul-mir’âte li-yenzura fîhâ, gloss:adama bakması için ayna tuttuğumda "ra’eytuhu" derim, source:"ر ء ي,B012"}. Amel sahibinin önüne ayna gibi tutulur. Aynı kök, insanların görmesi için iş yapmayı da adlandırır {ar:أن يفعل شيئا ليراه الناس, tr:en yef‘ale şey’en li-yerâhun-nâs, gloss:bir şeyi insanlar görsün diye yapmak, source:"ر ء ي,B005"}; Kur’an münafıkları {ar:يُرَآءُونَ ٱلنَّاسَ, tr:yurâûnen-nâs, gloss:insanlara gösteriş yaparlar, source:4:142} diye anlatır. Surede yön tersine döner: herkes başkasına değil, kendi amelini görmeye getirilir. Yedinci ve sekizinci ayetin {ar:يَرَهُۥ, tr:yerahû, gloss:onu görür, source:99:8} fiili gözle ya da iç görüyle görmektir {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakış ve görüş, source:"ر ء ي,B001"}.

Sekizinci ayetin kötülük kelimesi de bu harekete katılır: aynı kök bir şeyi ortaya çıkarıp sergilemek anlamını taşır {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşrartuş-şey’e izâ ebreztuhû ve azhartuh, gloss:bir şeyi ortaya çıkarıp gösterdiğimde "eşrartu" derim, source:"ش ر ر,B008"}, bir şeyi kurusun diye güneşe yaymak anlamını da {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastukeş-şey’e fiş-şems, gloss:şerr, bir şeyi güneşe yaymandır, source:"ش ر ر,B002"}. Zerrenin kökü de güneşin doğuşunda yayılan ince ışığı adlandırır {ar:ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر, tr:zerratiş-şemsu zurûran izâ tala‘at ve huve dav’un latîfun munteşir, gloss:güneş doğup ince ışığını yaydı, source:"ذ ر ر,B004"}. Bu anlamlar kelimelerin ayetteki anlamını, iyilik ve kötülüğü, değiştirmez; yanlarında, en küçük kötülüğün bile güneşe serilmiş gibi açıkta olduğunu duyururlar. Gören de bu sahnededir: insan görünür olduğu için böyle adlandırılmıştır {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-insu hilâful-cinni ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için böyle adlandırıldılar, source:"ء ن س,B001"}; göz bebeğinde görünen küçük suret {ar:إنسان العين المثال الذي يرى في السواد, tr:insânul-ayn el-misâlullezî yurâ fis-sevâd, gloss:göz bebeği, karalıkta görünen suret, source:"ء ن س,B005"} de aynı adı taşır; görmek ve duymak da bu köktendir {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestuş-şey’e izâ ra’eytuhû ve ânestuhû izâ semi‘tuh, gloss:bir şeyi gördüğümde ve duyduğumda "ânestu" derim, source:"ء ن س,B002"}. Üçüncü ayetin insanı sarsıntıyı görür, haberi duyar ve sonunda amelini görür.

Kur’an bu açığa çıkarışı birçok yerde sahneler. Kabirlerdekiyle göğüslerdeki birlikte çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fis-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Altıncı ayetin fiili göğüs kelimesiyle aynı köktendir {source:"ص د ر,B001"}; bu bir kök ortaklığıdır, aynı anlam değildir, ama bu ayetin yanında duyulur. Gizliler o gün sınanır {source:86:9}; {ar:يَوْمَئِذٍ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌ, tr:yevmeizin tu‘radûne lâ tahfâ minkum hâfiyeh, gloss:o gün arz olunursunuz, sizden hiçbir gizli kalmaz, source:69:18}. Çıkarma fiili kayıt için de kullanılır: {ar:وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:ve nuhricu lehû yevmel-kıyâmeti kitâben yelkâhu menşûrâ, gloss:kıyamet günü onun için açılmış bulacağı bir kitap çıkarırız, source:17:13}; hemen ardından {ar:ٱقْرَأْ كِتَٰبَكَ, tr:ikra’ kitâbek, gloss:kitabını oku, source:17:14} denir. Sayfalar açılır {source:81:10}. Allah’ın uyarısında her nefis yaptığı iyiliği hazır bulur {ar:يَوْمَ تَجِدُ كُلُّ نَفْسٍ مَّا عَمِلَتْ مِنْ خَيْرٍ مُّحْضَرًا, tr:yevme tecidu kullu nefsin mâ amilet min hayrin muhdarâ, gloss:her nefsin yaptığı iyiliği hazır bulduğu gün, source:3:30}. Musa ve İbrahim’in sayfalarındaki söz surenin edilgen fiilini kullanır: {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa‘yehû sevfe yurâ, gloss:ve onun çabası görülecektir, source:53:40}. İnsana dirilişte {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌ, tr:fekeşefnâ anke gitâeke fe-basarukel-yevme hadîd, gloss:örtünü üzerinden kaldırdık, bugün gözün keskindir, source:50:22} denir; herkes ellerinin öne sürdüğüne bakar {source:78:40}. Ve o gün yer, Rabbinin nuruyla aydınlanır, kitap konur {ar:وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ, tr:ve eşrakatil-arzu bi-nûri rabbihâ ve vudi‘al-kitâb, gloss:yer Rabbinin nuruyla parladı ve kitap kondu, source:39:69}.

Kaynaklar: 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 وَأَخْرَجَتِ خ ر ج B002; 99:4 أَخْبَارَهَا خ ب ر B001; 99:4 تُحَدِّثُ ح د ث B006; 99:4 تُحَدِّثُ ح د ث B007; 99:6 لِّيُرَوْا۟ ر ء ي B012; 99:6 لِّيُرَوْا۟ ر ء ي B005; 99:7 يَرَهُۥ ر ء ي B001; 99:8 شَرًّا ش ر ر B008; 99:8 شَرًّا ش ر ر B002; 99:7 ذَرَّةٍ ذ ر ر B004; 99:3 ٱلْإِنسَٰنُ ء ن س B001; 99:3 ٱلْإِنسَٰنُ ء ن س B005; 99:3 ٱلْإِنسَٰنُ ء ن س B002; 99:6 يَصْدُرُ ص د ر B001

## Serpilen zerre ve sıçrayan kıvılcım

Zerre kökünün işlemi serpmektir: tahılı, tuzu ya da ilacı dağıtarak saçmak {ar:ذررت الحب والدواء والملح أذره ذرا فرقته, tr:zerartul-habbe ved-devâe vel-milha ezurruhû zerran ferraktuh, gloss:taneyi, ilacı, tuzu serptim, yani dağıttım, source:"ذ ر ر,B002"}. Zerre de karıncaların en küçüğüdür, dağınık bir sürünün tek bir bireyi {ar:الذر صغار النمل الواحدة ذرة, tr:ez-zerru sıgârun-nemli, el-vâhidetu zerra, gloss:zerr küçük karıncalardır, tekili zerredir, source:"ذ ر ر,B001"}; aynı kökten ince bir tozun adı gelir {source:"ذ ر ر,B003"}. Altıncı ayetin bölükleri de bir topluluğun parçalara ayrılmasıdır {ar:شت يشت شتاتا وهو التفرق, tr:şette yeşittu şetâten ve huvet-teferruk, gloss:dağıldı, dağılmak, source:"ش ت ت,B001"}. Bu üç kelime tek bir imge kurar: bir kütle birimlere serpilir ve birim küçülür, insan bölüklerinden yedinci ve sekizinci ayette tartılan {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:7} ölçüsüne kadar.

Sekizinci ayette bu birime bir kıvılcım eklenir. Kötülük kelimesinin kökü ateşten sıçrayan kıvılcımı adlandırır {ar:الشرر ما تطاير من النار الواحدة شررة, tr:eş-şerer mâ tetâyera minen-nâr, el-vâhidetu şerera, gloss:şerer ateşten uçuşandır, tekili şereredir, source:"ش ر ر,B003"}. Bu bir kök ortaklığıdır; ayetteki kelime kötülük demektir. Ama {ar:مِثْقَالَ ذَرَّةٍ شَرًّا, tr:miskâle zerratin şerran, gloss:zerre ağırlığınca kötülük, source:99:8} sözünde kıvılcım da duyulur: en küçük kötülük, ateşten kopup uçan en küçük parça gibidir. Kur’an ateşin kıvılcımını ters ölçekte gösterir; inkâr edenlere anlatılan ateş {ar:إِنَّهَا تَرْمِى بِشَرَرٍ كَٱلْقَصْرِ, tr:innehâ termî bi-şererin kel-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32}. Zerre büyüklüğündeki kötülükle saray büyüklüğündeki kıvılcım aynı kökte buluşur.

Kur’an insanları da dağınık bir sürü gibi gösterir: yayılmış çekirgeler {source:54:7} ve {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnun-nâsu kel-ferâşil-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Sarsılan yerin ardından dağlar da toza döner: {ar:فَكَانَتْ هَبَآءً مُّنۢبَثًّا, tr:fekânet hebâen munbessâ, gloss:saçılmış toz oldu, source:56:6}. En küçük canlıların sürüsü bir sahnede konuşur da: Süleyman’ın ordusu yaklaşırken bir karınca {ar:يَٰٓأَيُّهَا ٱلنَّمْلُ ٱدْخُلُوا۟ مَسَٰكِنَكُمْ, tr:yâ eyyuhen-neml udhulû mesâkinekum, gloss:ey karıncalar, yuvalarınıza girin, source:27:18} der.

Kaynaklar: 99:7 ذَرَّةٍ ذ ر ر B002; 99:7 ذَرَّةٍ ذ ر ر B001; 99:7 ذَرَّةٍ ذ ر ر B003; 99:6 أَشْتَاتًا ش ت ت B001; 99:8 شَرًّا ش ر ر B003; 99:8 ذَرَّةٍ ذ ر ر B001

## Ağırlık: yerin yüklerinden zerrenin miskaline

Ağırlık kökü surede iki biçimde durur: ikinci ayetin {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2} sözü yerin dev yükleridir, son iki ayetin {ar:مِثْقَالَ, tr:miskâle, gloss:ağırlığınca, miskal, source:99:7} sözü ise bilinen bir tartı birimidir {ar:المثقال ما يوزن به وهو اسم لكل سنج, tr:el-miskâlu mâ yûzenu bihî ve huvesmun li-kulli senc, gloss:miskal kendisiyle tartılan şeydir, her tartı ağırlığının adıdır, source:"ث ق ل,B004"}. Hareket en büyük ağırlıktan en küçüğüne gider. Ağırlık hafifliğin karşıtıdır ve aslında bedenlere aittir, sonra anlamlara geçer {ar:الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني, tr:es-sikalu vel-hıffetu mutekâbilâni ve asluhû fil-ecsâmi summe fil-meânî, gloss:ağırlık ve hafiflik karşıttır, aslı bedenlerde, sonra anlamlardadır, source:"ث ق ل,B001"}; surenin kendisi bu geçişi yapar, yerin içindeki bedenlerden amellerin ağırlığına. Yükler günahlar da demektir {ar:الأثقال الآثام, tr:el-eskâl el-âsâm, gloss:ağırlıklar günahlardır, source:"ث ق ل,B003"}; kötülük kökünün ikilenmiş bir biçimi de ağırlıkları adlandırır {ar:الشراشر الأثقال الواحدة شرشرة, tr:eş-şerâşir el-eskâl, el-vâhidetu şerşera, gloss:şerâşir ağırlıklardır, tekili şerşeredir, source:"ش ر ر,B006"}.

Terazinin kefelerine konanlar karşıt adlarla tanımlanır: iyilik herkesin istediği şeydir {ar:الخير ما يرغب فيه الكل, tr:el-hayru mâ yergabu fîhil-kull, gloss:hayır herkesin rağbet ettiğidir, source:"خ ي ر,B001"}, kötülük herkesin yüz çevirdiği {ar:الشر الذي يرغب عنه الكل, tr:eş-şerrullezî yergabu anhul-kull, gloss:şer herkesin yüz çevirdiğidir, source:"ش ر ر,B001"}. Tartılan da kasıtla yapılan iştir {ar:كل فعل يكون من الحيوان بقصد, tr:kullu fi‘lin yekûnu minel-hayevâni bi-kasd, gloss:canlıdan kasıtla çıkan her iş, source:"ع م ل,B001"}. Kefeye konan en küçük şey de en küçük karıncadır {source:"ذ ر ر,B001"}.

Aynı tartı bir pazar ve hazine sahnesinde de kurulur. Miskal sikkenin ağırlığıdır; birine tam ağırlığını vermek {ar:أعطه ثقله أي وزنه, tr:a‘tıhî sikalehû ey veznehû, gloss:ona ağırlığını, yani tartısını ver, source:"ث ق ل,B004"} diye söylenir. Çıkma kökü de verenin çıkarıp ödediği malı, yıllık vergiyi ve geliri adlandırır {ar:الخراج والخرج الإتاوة لأنه مال يخرجه المعطي, tr:el-harâcu vel-harcu el-itâve, li-ennehû mâlun yuhricuhul-mu‘tî, gloss:harac ve harc vergidir, çünkü veren onu çıkarır, source:"خ ر ج,B003"}; ortakların paylarını ayırmasını da {source:"خ ر ج,B012"}. Amel kökü işin ücretini {ar:العمالة أجر ما عمل, tr:el-umâle ecru mâ amil, gloss:umâle yapılan işin ücretidir, source:"ع م ل,B004"} ve alışverişte karşılıklı muameleyi {source:"ع م ل,B005"} adlandırır; iyilik kelimesi de güzel yoldan toplanmış mal anlamına gelir {source:"خ ي ر,B004"}. Bu sahnede yer borcunu çıkarıp öder, her amel sikke gibi tartılır, sahibi de işinin ücretini alır; eksik tartılmış hiçbir şey kalmaz.

Kur’an surenin sözünü aynen Allah’ın adaleti için kullanır: {ar:إِنَّ ٱللَّهَ لَا يَظْلِمُ مِثْقَالَ ذَرَّةٍ, tr:innallâhe lâ yazlimu miskâle zerra, gloss:Allah zerre ağırlığınca haksızlık etmez, source:4:40}. Peygambere hitapta amel, Rab, zerre ve yer tek ayette toplanır: {ar:وَمَا يَعْزُبُ عَن رَّبِّكَ مِن مِّثْقَالِ ذَرَّةٍ فِى ٱلْأَرْضِ, tr:ve mâ ya‘zubu an rabbike min miskâli zerratin fil-arz, gloss:yerde zerre ağırlığınca bir şey Rabbinden gizli kalmaz, source:10:61}; Saati inkâr edenlere verilen cevapta da aynı söz geçer {source:34:3}. Lokman oğluna gizli bir küçük ağırlığın yerden çıkarılacağını söyler: {ar:إِن تَكُ مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ فَتَكُن فِى صَخْرَةٍ أَوْ فِى ٱلسَّمَٰوَٰتِ أَوْ فِى ٱلْأَرْضِ يَأْتِ بِهَا ٱللَّهُ, tr:in teku miskâle habbetin min hardelin fetekun fî sahratin ev fis-semâvâti ev fil-ardı ye’ti bihallâh, gloss:hardal tanesi ağırlığınca olsa da bir kayada, göklerde ya da yerde bulunsa Allah onu getirir, source:31:16}. Kıyamet günü teraziler kurulur ve hardal tanesi ağırlığınca olan da getirilir {source:21:47}; o gün {ar:فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:femen sekulet mevâzînuh, gloss:kimin tartıları ağır gelirse, source:7:8} ve {ar:وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve men haffet mevâzînuh, gloss:kimin tartıları hafif gelirse, source:7:9}. Hemen ardından gelen sure de aynı iki kefeyi gösterir {source:101:6}, {source:101:8}. Kayıt da en küçüğü bırakmaz: {ar:وَكُلُّ صَغِيرٍ وَكَبِيرٍ مُّسْتَطَرٌ, tr:ve kullu sagîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Yük olarak günah, başkalarının yükünü taşımayı teklif eden inkâr önderleri için söylenir: {ar:وَلَيَحْمِلُنَّ أَثْقَالَهُمْ وَأَثْقَالًا مَّعَ أَثْقَالِهِمْ, tr:ve le-yahmilunne eskâlehum ve eskâlen mea eskâlihim, gloss:kendi yüklerini ve yüklerinin yanında başka yükleri de taşıyacaklar, source:29:13}; yüklü bir nefis yükünü taşıtmak için çağırsa da kimse taşımaz {source:35:18}. Hesap sahnesinde ise ücret tam ödenir: {ar:وَإِنَّمَا تُوَفَّوْنَ أُجُورَكُمْ يَوْمَ ٱلْقِيَٰمَةِ, tr:ve innemâ tuveffevne ucûrakum yevmel-kıyâmeh, gloss:ücretleriniz ancak kıyamet günü tam olarak ödenir, source:3:185}; {ar:وَلِيُوَفِّيَهُمْ أَعْمَٰلَهُمْ وَهُمْ لَا يُظْلَمُونَ, tr:ve li-yuveffiyehum a‘mâlehum ve hum lâ yuzlemûn, gloss:onlara amellerini tam ödesin diye, haksızlığa uğramazlar, source:46:19}; kitabın konduğu günün sonunda {ar:وَوُفِّيَتْ كُلُّ نَفْسٍ مَّا عَمِلَتْ, tr:ve vuffiyet kullu nefsin mâ amilet, gloss:her nefse yaptığı tam ödendi, source:39:70}. Harac ile Rab ve hayır da tek bir ayette, Peygambere söylenen sözde buluşur: {ar:أَمْ تَسْـَٔلُهُمْ خَرْجًا فَخَرَاجُ رَبِّكَ خَيْرٌ, tr:em tes’eluhum harcen fe-harâcu rabbike hayr, gloss:yoksa onlardan bir ücret mi istiyorsun, Rabbinin vergisi daha hayırlıdır, source:23:72}; öne gönderilen hayır da Allah katında bulunur {source:2:110}.

Kaynaklar: 99:2 أَثْقَالَهَا ث ق ل B001; 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 أَثْقَالَهَا ث ق ل B003; 99:7 مِثْقَالَ ث ق ل B004; 99:7 ذَرَّةٍ ذ ر ر B001; 99:7 خَيْرًا خ ي ر B001; 99:7 خَيْرًا خ ي ر B004; 99:8 شَرًّا ش ر ر B001; 99:8 شَرًّا ش ر ر B006; 99:7 يَعْمَلْ ع م ل B001; 99:7 يَعْمَلْ ع م ل B004; 99:7 يَعْمَلْ ع م ل B005; 99:2 وَأَخْرَجَتِ خ ر ج B003; 99:2 وَأَخْرَجَتِ خ ر ج B012

## Ak ile kara kadar uzak iki pay

Bölük bölük kelimesi yalnızca dağılmak değildir. Aynı kökten iki şey arasındaki büyük mesafe söylenir {ar:شتان ما بينهما, tr:şettâne mâ beynehumâ, gloss:ikisinin arası ne kadar uzak, source:"ش ت ت,B003"}, ikisi arasındaki bağın kalkması {ar:ارتفاع الالتئام بينهما, tr:irtifâul-iltiâmi beynehumâ, gloss:aralarındaki kaynaşmanın kalkması, source:"ش ت ت,B003"}. İyilik ve kötülük de birbirinin karşıtıdır {ar:الشر نقيض الخير, tr:eş-şerru nakîdul-hayr, gloss:şer hayrın zıddıdır, source:"ش ر ر,B001"}. Çıkma kökü ise iki renkli bir yüzeyi adlandırır {ar:الخرج لونان بين سواد وبياض, tr:el-harac levnâni beyne sevâdin ve beyâd, gloss:harac karayla ak arasında iki renktir, source:"خ ر ج,B007"}. Altıncı ayetin kalabalığı surenin son iki ayetine ayrılır: biri {ar:خَيْرًا يَرَهُۥ, tr:hayran yerahû, gloss:iyilik, onu görür, source:99:7}, öbürü {ar:شَرًّا يَرَهُۥ, tr:şerran yerahû, gloss:kötülük, onu görür, source:99:8}. İki ayet aynı kelimelerle kurulur, yalnızca son kelimeden önceki ad değişir; bu eşitlik iki payın arasındaki uzaklığı daha keskin gösterir.

Kur’an bu ayrılışı renkle gösterir: {ar:يَوْمَ تَبْيَضُّ وُجُوهٌ وَتَسْوَدُّ وُجُوهٌ, tr:yevme tebyaddu vucûhun ve tesveddu vucûh, gloss:kimi yüzlerin ağarıp kimi yüzlerin karardığı gün, source:3:106}; {ar:وُجُوهٌ يَوْمَئِذٍ مُّسْفِرَةٌ, tr:vucûhun yevmeizin musfira, gloss:o gün parlayan yüzler var, source:80:38} ve {ar:وَوُجُوهٌ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌ, tr:ve vucûhun yevmeizin aleyhâ gabera, gloss:ve o gün üzerinde toz olan yüzler var, source:80:40}. Saatin günü insanlar ayrılır {source:30:14}, ardından {ar:فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ, tr:fe-emmallezîne âmenû ve amilus-sâlihât, gloss:iman edip salih amel işleyenlere gelince, source:30:15} ve {ar:وَأَمَّا ٱلَّذِينَ كَفَرُوا۟, tr:ve emmallezîne keferû, gloss:inkâr edenlere gelince, source:30:16} gelir: kalabalık amellere göre ikiye ayrılır. Toplanma günü {ar:فَرِيقٌ فِى ٱلْجَنَّةِ وَفَرِيقٌ فِى ٱلسَّعِيرِ, tr:ferîkun fil-cenneti ve ferîkun fis-saîr, gloss:bir bölük cennette, bir bölük alevli ateşte, source:42:7}. Aynı kök çabaların ayrılığı için de kullanılır: {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa‘yekum le-şettâ, gloss:çabalarınız elbette çeşit çeşittir, source:92:4}. Kitap da iki payı ayırır: sağından verilen {source:69:19} ve solundan verilen {source:69:25}.

Kaynaklar: 99:6 أَشْتَاتًا ش ت ت B003; 99:6 أَشْتَاتًا ش ت ت B001; 99:7 خَيْرًا خ ي ر B001; 99:8 شَرًّا ش ر ر B001; 99:2 وَأَخْرَجَتِ خ ر ج B007

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

