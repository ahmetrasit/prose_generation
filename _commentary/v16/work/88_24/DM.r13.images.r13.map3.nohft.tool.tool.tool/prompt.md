Focus: 88:24. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_24/D.r13/context.md =====
# 88:24 — focus

فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ

Anchor translation (canonical reading, reference only):

Allah da onu en büyük cezayla cezalandırır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَيُعَذِّبُهُ | عَذَّبَ | ع ذ ب | REM;V;PRON |
| 2 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 3 | ٱلْعَذَابَ | عَذَاب | ع ذ ب | DET;N |
| 4 | ٱلْأَكْبَرَ | أَكْبَر | ك ب ر | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 ◀ focus فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_24/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ذ ب (root_000994) — identity root of فَيُعَذِّبُهُ (w1)

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

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w2)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ك ب ر (root_001281) — identity root of ٱلْأَكْبَرَ (w4)

- **B001** küçüğün karşıtı olan büyüklük — büyük · pek büyük · daha büyük veya en büyük
  أصل صحيح يدل على خلاف الصغر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ الكبر ضد الصغر (jamhara)؛ كبر بالضم يكبر أي عظم فهو كبير وكبار (sihah)؛ الكبير والصغير من الأسماء المتضايفة (mufradat)
- **B002** bir işin ana payı ve başlıca yükü — işin büyük bölümü veya ağır yükü · onun işinin en önemli bölümü
  والكبر معظم الأمر (maqayis)؛ كبر كل شيء عظمه (ayn)؛ كبر الشيء معظمه (jamhara)؛ كبر الشيء أيضا معظمه (sihah)؛ كبر الشيء معظمه بالكسر (tahdhib)؛ والذي تولى كبره إشارة إلى من أوقع حديث الإفك (mufradat)
- **B003** gözünde büyütüp hayrete düşmek — onu gözünde büyüttü ve ona hayret etti · onu gözlerinde büyüttüler
  أكبرت الشيء استعظمته (maqayis)؛ أكبرت الشيء أكبره إكبارا إذا عظم في صدرك وعجبت منه (jamhara)؛ أكبرت الشيء استعظمته (sihah)؛ أكبرنه أعظمنه (tahdhib)؛ أكبرت الشيء رأيته كبيرا (mufradat)
- **B004** yaşlanma ve zamanla eskime — adam yaşlandı · yaşlılık veya eskilik hali
  ومن الباب الكبر وهو الهرم (maqayis)؛ الكبرة السن يقال علته كبرة (ayn)؛ بلغ فلان الكبر في السن (jamhara)؛ الكبر في السن وقد كبر الرجل أي أسن (sihah)؛ الكبر مصدر الكبير في السن من الناس والدواب (tahdhib)؛ يقال فلان كبير أي مسن (mufradat)؛ السهم والنصل العتيق الذي أفسده الوسخ قد علته كبرة (ayn)؛ للسيف والنصل العتيق الذي قدم علته كبرة (tahdhib)
- **B005** saygınlık ve önderlikte yüksek konum — kuşaktan kuşağa soylu ve saygın biçimde · onların başı veya en bilgilisi · sizin öğreticiniz veya başınız · önder veya en büyük ata
  الرفعة في الشرف (ayn)؛ ورثوا المجد كابرا عن كابر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ كبيرهم أعلمهم كأنه كان رئيسهم (tahdhib)؛ إنه لكبيركم أي رئيسكم (mufradat)؛ الكابر السيد والكابر الجد الأكبر (tahdhib)
- **B006** ululuk ve kendini üstün görme — büyüklük taslama ve kendini üstün görme · ululuk ve boyun eğmeme; Tanrı'ya özgü yücelik · büyüklendi ve kendini üstün gösterdi · gerçeği inatla reddedip büyüklük tasladı
  الكبر العظمة وكذلك الكبرياء (maqayis)؛ الكبرياء اسم للتكبر والعظمة (ayn)؛ تكبر إذا تعظم (jamhara)؛ الكبر بالكسر العظمة وكذلك الكبرياء (sihah)؛ يتكبرون أي يرون أنهم أفضل الخلق (tahdhib)؛ الكبر الحالة التي يتخصص بها الإنسان من إعجابه بنفسه (mufradat)
- **B007** ağır cezalık büyük günah — ağır cezalık büyük günah · ağır cezalık büyük günahlar
  الكبر الإثم الكبير من الكبيرة (ayn)؛ الكبيرة من الذنوب والجمع كبائر (jamhara)؛ كبيرة من الكبائر يعني الذنوب (ayn)؛ الكبيرة متعارفة في كل ذنب تعظم عقوبته (mufradat)؛ إثم كبير (mufradat)
- **B008** soy yakınlığı veya aile içi doğum sırası — soyda en yakın olan veya en büyük evlat · babasının son çocuğu; başka aktarımda en büyük çocuğu
  الولاء للكبر يراد به أقعد القوم في النسب (maqayis)؛ الكبر أكبر ولد الرجل (ayn)؛ فلان كبرة ولد أبويه إذا كان آخرهم (sihah)؛ كبرة ولد أبيه بمعنى عجزة أي آخرهم (tahdhib)؛ هو صغرة ولد أبيه وكبرتهم أي أكبرهم (tahdhib)
- **B009** Tanrı'yı en büyük diye yüceltme — Tanrı'yı en büyük diye yüceltme · Tanrı en büyüktür
  التكبير في الصلاة وغيرها تفعيل من قولهم الله أكبر (jamhara)؛ التكبير التعظيم (sihah)؛ قول المصلي الله أكبر وكذلك قول المؤذن (tahdhib)؛ التكبير يقال لتعظيم الله تعالى بقولهم الله أكبر (mufradat)
- **B010** bir işin birine ağır ve güç gelmesi [kalıp] — bize çok ağır ve güç geldi
  إذا أردت الأمر العظيم قلت كبر علينا كبارة (ayn)؛ فإذا أردت الأمر العظيم قلت كبر علينا كبارة (sihah)؛ كبر الأمر يكبر كبارة (tahdhib)؛ تستعمل الكبيرة فيما يشق ويصعب (mufradat)؛ كبر على المشركين ما تدعوهم إليه (mufradat)
- **B011** üstünlük yarışına girip yenmek [kalıp] — benimle üstünlük yarışına girdi, ben de onu yendim
  كابرني فكبرته أي غلبته (ayn)
- **B012** tek yüzlü davul — tek yüzlü davul
  الكبر طبل له وجه (ayn)؛ الكبر الطبل الذي له وجه واحد (tahdhib)؛ الكبر الطبل وجمعه كبار (tahdhib)
- **B013** günün yükseldiği vakit [kalıp] — günün yükseldiği vakit
  أكبر النهار وشباب النهار أي حين ارتفع النهار (tahdhib)

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:24, and ## Buluşmalar) =====
## Örten: Gâşiye, bahçe ve örtüsünü yitiren

Sure bir soruyla açılır: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. Gâşiye "üstüne gelip örten" demektir. Kökün temel işi, bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"}. Kelimenin elle tutulur bir karşılığı da vardır. Eyerin üstüne atılan örtüye de bu ad verilir: {ar:وغاشية السرج غطاؤه, tr:ve ğâşiyetü's-serci ğıtâuhû, gloss:eyerin gâşiyesi onun örtüsüdür, source:"غ ش و,B001"}. Böyle bir örtü yukarıdan atılır, eyeri her yanından sarar ve altında kalanı gözden saklar. Kıyamet bu adla anıldığında aynı hareket bütün yaratılmışlara uygulanmış olur: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâmetü li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:Gâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Örtü dışarıda da kalmaz. Aynı fiil, başa gelen bir şeyin aklı kapatmasını, yani bayılmayı da anlatır: {ar:غشي على فلان إذا نابه ما غشي فهمه, tr:ğuşiye alâ fülânin izâ nâbehû mâ ğaşiye fehmehû, gloss:başına gelen şey anlayışını örtünce falan bayıldı denir, source:"غ ش و,B005"}. Demek ki ilk ayetteki tek kelimede bir örtü duyulur: dışarıdan iner, her yanı kuşatır ve içeriye, akla kadar işler. Kelimeyi yalnızca "kıyamet" diye karşılamak bu hareketi kaybettirir.

Bu yazı boyunca geçerli bir kural var: Bir kelimenin akrabalarından gelen resimler, o kelimenin ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Gâşiye burada o günün adıdır. Eyer örtüsü ve baygınlık yalnızca bu adın nasıl işlediğini gösterir.

Örtünün ilk indiği yer yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2}. Yüz, bir şeyin karşıya dönük ön tarafıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. Kur'an bu sahneyi başka yerlerde açıkça kurar. Suçluların o gün zincirlere vurulduğu anlatılırken şöyle denir: {ar:سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:serâbîluhum min katırânin ve tağşâ vucûhehumu'n-nâr, gloss:gömlekleri katrandandır ve yüzlerini ateş örter, source:14:50}. Kötülük kazananlar için başka bir yerde verilen benzetme, örtüyü gecenin kendisinden yapar: {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhum kıtaan mine'l-leyli muzlimâ, gloss:sanki yüzlerine karanlık geceden parçalar örtülmüş, source:10:27}.

Surenin ilk ve son adları tek bir ayette bir araya gelir. Yusuf kıssasının sonunda Allah, Peygamber'e insanların çoğunun inanmadığını söyledikten sonra sorar: {ar:أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:e-fe-eminû en te'tiyehum ğâşiyetun min azâbillâh, gloss:Allah'ın azabından örten bir şeyin kendilerine gelmesinden emin mi oldular, source:12:107}. Bu ayette surenin ilk fiili (gelmek), ilk adı (örten) ve yirmi dördüncü ayetteki azap aynı cümlededir. Kelimenin açıklaması da bunu söyler: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbillâh ey ukûbetun mücellele teummuhum, gloss:hepsini saran ve kapsayan bir ceza, source:"غ ش و,B002"}. Duhan suresinde Allah, Peygamber'e şüphe içinde oyalananları gösterir ve göğün apaçık bir duman getireceği günü beklemesini söyler. O duman için de şöyle denir: {ar:يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ, tr:yağşe'n-nâs hâzâ azâbun elîm, gloss:insanları örter; bu acı bir azaptır, source:44:11}. Azabın çabuk gelmesini isteyenler için de örtü dört yandan tamamlanır: {ar:يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ, tr:yevme yağşâhumu'l-azâbu min fevkıhim ve min tahti ercülihim, gloss:azabın onları üstlerinden ve ayaklarının altından örteceği gün, source:29:55}. Eyer örtüsü yalnızca üstten sarardı. Burada örtü alttan da kapanır.

Onuncu ayet ikinci bir örtü getirir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10}. Bu kökün aslı da örtmektir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenni setru'ş-şey'i ani'l-hâsse, gloss:bir şeyi duyulardan gizlemek, source:"ج ن ن,B001"}. Bahçe adını ağaçlarının toprağı örtmesinden alır: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü büstânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bostan, source:"ج ن ن,B003"}. Ödül de bugün göze görünmeyen, örtülü bir şeydir: {ar:الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم, tr:el-cennetü mâ yasîru ileyhi'l-müslimûne fi'l-âhira ve huve sevâbun mestûrun anhumu'l-yevm, gloss:cennet bugün onlardan gizli olan ödüldür, source:"ج ن ن,B004"}. Aynı kökten kalkan da çıkar: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-türsü ve'l-cünnetü'd-dir'u ve küllü mâ vakâke fe-huve cünnetük, gloss:seni koruyan her şey senin kalkanındır, source:"ج ن ن,B008"}. Böylece surede iki örtü karşı karşıya durur. Biri yukarıdan iner ve ezer. Öteki aşağıdan büyür, gölgeler ve korur. Bahçe halkı bu ikinci örtüyü birincisinden kurtuluş olarak anar. Birbirlerine dönüp ailelerinin arasındayken nasıl korku içinde yaşadıklarını hatırladıktan sonra şöyle derler: {ar:فَمَنَّ ٱللَّهُ عَلَيْنَا وَوَقَىٰنَا عَذَابَ ٱلسَّمُومِ, tr:fe-mennallâhu aleynâ ve vekânâ azâbe's-semûm, gloss:Allah bize lütfetti ve bizi kavurucu azaptan korudu, source:52:27}. Burada "korumak" fiili, kalkanın tanımındaki fiilin ta kendisidir. Dördüncü ayetteki ateş sıfatı حامية'nin kökü de başka kullanımında korunan yeri anlatır: {ar:الحمى موضع فيه كلأ يحمى من الناس أن يرعى, tr:el-himâ mevziun fîhi keleun yuhmâ mine'n-nâsi en yur'â, gloss:otlu olup insanların otlatmasından korunan yer, source:"ح م ي,B002"}. Bu anlam ayetteki kızgın ateşin yanında duyulur: aynı harflerin koruyan yüzü ateşe girenler için kapanmıştır.

Yirmi üçüncü ayetteki inkâr da bir örtme fiilidir: {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in ğattâ şey'en fe-kad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"}. Kelime imanın karşıtı olarak da bu yüzden kullanılır: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfru zıddü'l-îmân summiye li-ennehû tağtiyetü'l-hak, gloss:küfür imanın zıddıdır; hakkı örttüğü için bu adı almıştır, source:"ك ف ر,B003"}. Tohumu toprakla örten çiftçiye de bu ad verilir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru'z-zâriu li-ennehû yuğattı'l-bezra bi't-turâb, gloss:kâfir tohumu toprakla örten ekincidir, source:"ك ف ر,B008"}. Çiftçinin örtüsünden bir bahçe çıkabilir; hakkı örtenin örtüsünden hiçbir şey bitmez. Kur'an inkârla göz üstündeki örtüyü aynı ayette birleştirir. Uyarılsalar da uyarılmasalar da inanmayacakları söylenenler için şöyle denir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ, tr:ve alâ ebsârihim ğışâvetun ve lehum azâbun azîm, gloss:gözlerinin üstünde bir perde vardır ve onlar için büyük bir azap vardır, source:2:7}. Buradaki perde, Gâşiye ile aynı köktendir. Hakkı örten, sonunda kendi gözünün de örtüldüğünü görür. Gece de surenin üç ayrı kökünde örtü olarak anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}; {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğü zaman geceye andolsun, source:92:1}; İbrahim'in gece karşısındaki anında ise {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ, tr:fe-lemmâ cenne aleyhi'l-leyl, gloss:gece onu örtünce, source:6:76}. Bunlar aynı kökten değildir. Üç ayrı kökün paylaştığı tek bir resimdir.

Son adım yirmi dördüncü ayettedir. Azap ceza demektir: {ar:العذاب العقوبة وقد عذبته تعذيبا, tr:el-azâbu'l-ukûbe ve kad azzebtühû ta'zîbâ, gloss:azap cezadır, source:"ع ذ ب,B005"}. Aynı kökün bir başka kolu ise örtüsüz kalmış insanı anlatır: {ar:العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب, tr:el-azûbu'llezî leyse beynehû ve beyne's-semâi sitr, gloss:kendisiyle gök arasında hiçbir örtü bulunmayan kimse, source:"ع ذ ب,B004"}. Bu anlam ayetteki cezanın yanında duyulduğunda resim tamamlanır. Azap gören hem ezici örtünün altında kalmış hem de kendisini koruyan bütün örtülerden soyulmuştur. Bahçedeki insanın üstünde ise ağaçlardan bir örtü vardır, onu ezen hiçbir şey yoktur.

Kaynaklar: 88:1 ٱلْغَٰشِيَةِ غ ش و B001; 88:1 ٱلْغَٰشِيَةِ غ ش و B002; 88:1 ٱلْغَٰشِيَةِ غ ش و B005; 88:2 وُجُوهٌ و ج ه B001; 88:4 حَامِيَةً ح م ي B002; 88:10 جَنَّةٍ ج ن ن B001; 88:10 جَنَّةٍ ج ن ن B003; 88:10 جَنَّةٍ ج ن ن B004; 88:10 جَنَّةٍ ج ن ن B008; 88:23 وَكَفَرَ ك ف ر B001; 88:23 وَكَفَرَ ك ف ر B002; 88:23 وَكَفَرَ ك ف ر B003; 88:23 وَكَفَرَ ك ف ر B008; 88:24 ٱلْعَذَابَ ع ذ ب B004; 88:24 ٱلْعَذَابَ ع ذ ب B005

## İki pınar ve kaplar

Surede iki pınar vardır ve ikisi de aynı adı taşır. Beşincisi {ar:مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:min aynin âniye, gloss:son noktasına varmış sıcak bir pınardan, source:88:5}, on ikincisi ise {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Ad aynıdır, değişen yalnızca sıfattır. Birinde su sıcaklığın sonuna varmıştır. Ötekinde hareket halindedir: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî cireten ve ceryen ve cereyânâ, gloss:su aktı, source:"ج ر ي,B001"}. Kaynayan suyun durduğu bir yer vardır, ama akan su yenilenir. Kur'an bu iki pınarı aynı surede, birkaç ayet arayla yan yana koyar. Biri günahkârların dolaştığı {ar:حَمِيمٍ ءَانٍۢ, tr:hamîmin ân, gloss:son noktasına varmış kaynar su, source:55:44} ve diğeri Rabbinin makamından korkanların iki bahçesinde akan sudur: {ar:فِيهِمَا عَيْنَانِ تَجْرِيَانِ, tr:fîhimâ aynâni tecriyân, gloss:ikisinde de akan iki pınar vardır, source:55:50}.

Beşinci ayetteki sıfatın harfleri, Arapçada kap anlamına gelen kelimenin çoğuluyla da aynıdır: {ar:الإناء معروف وجمعه آنية والأواني, tr:el-inâu ma'rûfun ve cem'uhû âniyetun ve'l-evânî, gloss:kap bilinir; çoğulu âniye ve evânîdir, source:"ء ن ي,B004"}. Ayetteki anlam sıcaklıktır. Yanında ise kapların adı duyulur. On dördüncü ayet bu kapları bahçeye koyar: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}. Kevb kulpsuz bir kadehtir: {ar:الكوب القدح لا عروة له, tr:el-kûbü'l-kadahu lâ urvete leh, gloss:kevb kulpsuz kadehtir, source:"ك و ب,B001"}. Konmuş olmak, kaldırılmışın karşıtıdır: {ar:وضعت الشيء أضعه وضعا وهو ضد رفعته, tr:vada'tü'ş-şey'e edauhû vad'an ve huve zıddü rafa'tüh, gloss:bir şeyi koydum; kaldırdım'ın zıddı, source:"و ض ع,B001"}. Kadehler el altında hazır durur, istenmeden önce oradadır. Kur'an aynı iki kelimeyi, yani kapların adını ve kadehleri, sabredenlerin karşılığını anlatırken yan yana getirir: {ar:وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠, tr:ve yutâfu aleyhim bi-âniyetin min fiddatin ve ekvâbin kânet kavârîrâ, gloss:çevrelerinde gümüş kaplar ve billur kadehler dolaştırılır, source:76:15}. Aynı ses bir yerde kaynayan pınarın sıfatıdır, başka bir yerde bahçenin gümüş kapları.

Bahçe halkı da içirilir. Fiil iki tarafta da aynıdır, değişen kaynaktır: {ar:وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا, tr:ve yuskavne fîhâ ke'sen kâne mizâcuhâ zencebîlâ, gloss:orada zencefil katkılı bir kadehten içirilirler, source:76:17}; {ar:عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا, tr:aynen fîhâ tusemmâ selsebîlâ, gloss:orada Selsebil denen bir pınardan, source:76:18}; {ar:يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ, tr:yuskavne min rahîkın mahtûm, gloss:mühürlü saf bir içkiden içirilirler, source:83:25}. Bahçenin pınarı insanın elinde akar: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdullâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği ve diledikleri yere fışkırttıkları bir pınar, source:76:6}. Kadehler de bu pınardan doldurulur: {ar:بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ, tr:bi-ekvâbin ve ebârîka ve ke'sin min maîn, gloss:kadehler ibrikler ve akan pınardan doldurulmuş kâse ile, source:56:18}. Buradaki "maîn" kelimesi gözle görünen akar suyu anlatır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Allah, Peygamber'e bu suyun kimden geldiğini sormasını söyler: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki suyunuz yere çekilse size akar suyu kim getirir, source:67:30}.

Arapçada içmek de beslenmenin bir parçası sayılır: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey'i ve't-taâmu huve'l-me'kûlu ve'l-it'âmu yekau hatta'l-mâ', gloss:tatma kökü; yemek yenendir; doyurmak suya bile uzanır, source:"ط ع م,B001"}. Böylece beşinci ve altıncı ayetler tek bir sofradır: içecek kaynar sudur, yemek de ضريع. Son ayetlerdeki azap kelimesinin kökü ise tatlı suyu da adlandırır: {ar:عذب الماء عذوبة فهو عذب طيب, tr:azube'l-mâu uzûbeten fe-huve azbun tayyib, gloss:su tatlılaştı; o tatlı ve hoş sudur, source:"ع ذ ب,B001"}. Bu anlam ayetteki cezanın yanında duyulur. Aynı harfler bir yerde tatlı su, başka bir yerde azaptır. Tatlı suyu bekleyen yüz, kaynar suyla karşılaşır.

Kaynaklar: 88:5 تُسْقَىٰ س ق ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:5 ءَانِيَةٍ ء ن ي B004; 88:6 طَعَامٌ ط ع م B001; 88:12 عَيْنٌ ع ي ن B006; 88:12 جَارِيَةٌ ج ر ي B001; 88:14 أَكْوَابٌ ك و ب B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:24 ٱلْعَذَابَ ع ذ ب B001

## Alçalan ve yükselen

İkinci ayetteki yüz başını eğmiştir: {ar:أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه, tr:aslun vâhidun yedullü ale't-tatâmün; tetâmene ve ta'ta'e ra'sehû, gloss:alçalmayı gösteren kök; başını eğip indirdi, source:"خ ش ع,B001"}. Yemeğinin kökü de alçalmayı anlatır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Onuncu ayette ise bahçe yüksektedir: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yükseliği ve yüksekte oluşu gösteren kök, source:"ع ل و,B001"}; {ar:العلاء فالرفعة, tr:el-alâu fe'r-rif'a, gloss:alâ yüksek mertebedir, source:"ع ل و,B002"}. On üçüncü ayette sedirler kaldırılmıştır. Kaldırılmak da aşağılanmanın karşıtıdır: {ar:الرفعة نقيض الذلة, tr:er-rif'atü nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. On dördüncü ayetteki "konmuş" kelimesinin kökü insanın düşük konumunu da anlatır: {ar:رجل وضيع ضد الشريف والتواضع التذلل, tr:racülün vadîun zıddü'ş-şerîf ve't-tevâdu't-tezellül, gloss:vadî şerefli olanın zıddıdır; tevazu alçalmaktır, source:"و ض ع,B005"}. Bahçede alçak konulan şey insan değildir, hizmet eden kadehlerdir. İnsan yüksek sedirde oturur.

Aynı yükseklik ve alçaklık dünyada da göze gösterilir. Gök yüksekliktir: {ar:أصل يدل على العلو؛ سموت إذا علوت, tr:aslun yedullü ale'l-uluvv; semevtü izâ alevt, gloss:yükseliği gösteren kök; yükseldiğinde semevtü dersin, source:"س م و,B001"}. Yer ise aşağıda olandır: {ar:كل شيء يسفل ويقابل السماء, tr:küllü şey'in yesfülü ve yukâbilü's-semâ', gloss:aşağıda kalıp göğün karşısında duran her şey, source:"ء ر ض,B001"}. Yirmi dördüncü ayetteki azap "en büyük" olandır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullü alâ hılâfi's-sığar, gloss:küçüklüğün karşıtını gösteren kök, source:"ك ب ر,B001"}. İki kökün öteki yüzü de duyulur. Yükseklik kökü kibirli büyüklenmeyi de anlatır: {ar:العلو فالعظمة والتجبر, tr:el-uluvvu fe'l-azametü ve't-tecebbür, gloss:ulüv büyüklenme ve zorbalıktır, source:"ع ل و,B003"}. "En büyük" kelimesinin kökü de kendini büyük görmeyi adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametü ve kezâlike'l-kibriyâ', gloss:kibir büyüklüktür; kibriya da öyledir, source:"ك ب ر,B006"}. Bu anlamlar ayetlerdeki anlamların yanında duyulur. Bahçedeki yükseklik verilmiş bir yüksekliktir. İnsanın kendi kendine verdiği yükseklik ise öteki yüzün yolunu açar ve onu "en büyük" azapla karşılaştırır.

Kur'an kıyameti bu iki hareketle adlandırır: {ar:إِذَا وَقَعَتِ ٱلْوَاقِعَةُ, tr:izâ vekaati'l-vâkıa, gloss:olacak olan olduğunda, source:56:1}; {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}. Dünyada da yükseltme Allah'ın işidir. Müminlere meclislerde yer açmaları ve kalkmaları söylendiğinde kalkmanın karşılığı şudur: {ar:يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ, tr:yerfaillâhullezîne âmenû minkum, gloss:Allah içinizden inananları yükseltir, source:58:11}. Ateşe sunulan zalimler ise {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} diye anılır. O günün gözleri için de {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş, source:70:44} denir. "En büyük azap" sözü Kur'an'da bir yerde daha geçer ve orada küçüğün karşısına konur: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuzîkannehum mine'l-azâbi'l-ednâ dûne'l-azâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce yakın azaptan tattıracağız, source:32:21}. Alt basamak bir uyarıdır, üst basamak sonun kendisidir. Önceki surede de ateş aynı ölçüyle anılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:10 عَالِيَةٍ ع ل و B001; 88:10 عَالِيَةٍ ع ل و B002; 88:10 عَالِيَةٍ ع ل و B003; 88:13 مَّرْفُوعَةٌ ر ف ع B002; 88:14 مَّوْضُوعَةٌ و ض ع B005; 88:18 ٱلسَّمَآءِ س م و B001; 88:20 ٱلْأَرْضِ ء ر ض B001; 88:24 ٱلْأَكْبَرَ ك ب ر B001; 88:24 ٱلْأَكْبَرَ ك ب ر B006

## Hatırlatıcı, gözetmen değil

Yirmi birinci ayet Peygamber'in işini tek bir kelimeye indirir: hatırlatmak. "Ancak" sözü bu işin sınırını çizer. Hatırlatma, bir şeyin akla getirilmesini sağlayan şeydir ve tekrar edilir: {ar:التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر, tr:et-tezkiretü mâ yütezekkeru bihi'ş-şey' ve'z-zikrâ kesretü'z-zikr, gloss:tezkire bir şeyin hatırlandığı araçtır; zikra çok anmaktır, source:"ذ ك ر,B009"}. Yirmi ikinci ayet de bu işin olmadığı şeyi söyler: {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üstünde bir gözetmen değilsin, source:88:22}. Musaytır, bir şeyin başına konup onu gözeten ve yaptığını yazan kişidir: {ar:المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله, tr:el-museytıru ve'l-musaytıru'l-musallatu ale'ş-şey'i li-yuşrife aleyhi ve yeteahhede ahvâlehû ve yektübe amelehû, gloss:bir şeyin başına konup onu gözeten halini kollayan ve işini yazan kişi, source:"س ط ر,B003"}; {ar:السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء, tr:es-saytaratu masdaru'l-museytır ve huve ke'r-rakîbi'l-hâfızı'l-müteahhidi li'ş-şey', gloss:bir şeyi bekleyen ve koruyan gözcü gibi olan, source:"س ط ر,B003"}. Bu yetkinin asıl sahipleri efendilerdir: {ar:المسيطرون الأرباب المسلطون, tr:el-museytırûne'l-erbâbü'l-musallatûn, gloss:başa geçirilmiş efendiler, source:"س ط ر,B003"}. Kökün aslı satırdır: {ar:أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر, tr:aslun muttaridun yedullü ale'stıfâfi'ş-şey'i ke'l-kitâbi ve'ş-şecer, gloss:yazı ve ağaç gibi şeylerin dizilişini gösteren kök, source:"س ط ر,B001"}; {ar:السطر سطر من كتب وسطر من شجر مغروس, tr:es-satru satrun min kütübin ve satrun min şecerin mağrûs, gloss:satır yazıdan bir satır ve dikilmiş ağaçtan bir sıradır, source:"س ط ر,B001"}. Gözetmen, kayıtları satır satır tutan kişidir. Bu kökün tanımında geçen diziliş kelimesi, on beşinci ayette yastıkların dizilişini anlatan kelimedir. Bu bağ kök birliğinden değil, kelimelerin açıklamasından gelir. Bahçede yastıkları dizen bir el vardır. Amelleri satıra dizen el de vardır, ama Peygamber'in eli değildir.

Kur'an bu kaydı Allah'a bağlar. Önceki kavimlerin anlatıldığı surenin sonunda şöyle denir: {ar:وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ, tr:ve küllü sağîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Buradaki "yazılmış" kelimesi musaytır ile aynı köktendir. Kur'an'da bu kelimenin geçtiği tek başka yer, inkârcılara sorulan bir sorudur: {ar:أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ, tr:em indehum hazâinu rabbike em humu'l-musaytırûn, gloss:yoksa Rabbinin hazineleri onların yanında mı, yoksa gözetmenler onlar mı, source:52:37}. Gözetmenlik ne Peygamber'indir ne de onu reddedenlerin.

Kur'an bu sınırı başka yerlerde de çizer. Kaf suresinin sonunda Allah şöyle der: {ar:وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:ve mâ ente aleyhim bi-cebbârin fe-zekkir bi'l-Kur'âni men yehâfu vaîd, gloss:sen onları zorlayan değilsin; tehdidimden korkana Kur'an ile hatırlat, source:50:45}. Başka yerlerde de {ar:فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ, tr:fe-mâ erselnâke aleyhim hafîzan in aleyke ille'l-belâğ, gloss:seni onların üstüne bekçi göndermedik; sana düşen yalnızca duyurmaktır, source:42:48} ve {ar:وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ, tr:ve mâ cealnâke aleyhim hafîzan ve mâ ente aleyhim bi-vekîl, gloss:seni onlara bekçi yapmadık; sen onların vekili de değilsin, source:6:107} denir. Cezalandırmak da Allah'ın işidir: {ar:إِن يَشَأْ يَرْحَمْكُمْ أَوْ إِن يَشَأْ يُعَذِّبْكُمْ ۚ وَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ وَكِيلًۭا, tr:in yeşe' yerhamkum ev in yeşe' yuazzibkum ve mâ erselnâke aleyhim vekîlâ, gloss:dilerse size merhamet eder, dilerse azap eder; seni onlara vekil göndermedik, source:17:54}. Zorlama da sorunun içinde reddedilir: {ar:أَفَأَنتَ تُكْرِهُ ٱلنَّاسَ حَتَّىٰ يَكُونُوا۟ مُؤْمِنِينَ, tr:e-fe-ente tukrihu'n-nâse hattâ yekûnû mu'minîn, gloss:inanan olsunlar diye insanları sen mi zorlayacaksın, source:10:99}.

Yirmi üçüncü ayetteki istisna bu sınırın içinden çıkar: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz çevirme fiilinin kökü bir göreve geçmeyi de anlatır: {ar:تولى العمل أي تقلد, tr:tevelle'l-amele ey tekalled, gloss:işi üstlendi yani göreve geçti, source:"و ل ي,B003"}. Ayetteki anlam sırt dönmektir: {ar:ولى الرجل أي أدبر, tr:vellâ'r-raculu ey edbar, gloss:adam arkasını döndü, source:"و ل ي,B007"}. Yanında ise başa geçme anlamı duyulur. Peygamber'e verilmeyen göreve karşılık, yüz çeviren kendisi için yüz çevirmeyi üstlenmiştir. Yirmi dördüncü ayet cezayı Peygamber'e değil Allah'a verir: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah da onu en büyük azapla cezalandırır, source:88:24}. Allah'ın adı kulluk edilenin adıdır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır çünkü kulluk edilendir, source:"ء ل ه,B001"}. Son iki ayette konuşan "Biz" olur ve iş bölümü tamamlanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bize'dir, source:88:25}; {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize düşer, source:88:26}. Kur'an aynı bölüşümü tek bir cümlede söyler. Allah Peygamber'e, vaat edilenin bir kısmını ona göstersin ya da canını alsın, şunu der: {ar:فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ, tr:fe-innemâ aleyke'l-belâğu ve aleyne'l-hısâb, gloss:sana düşen yalnızca duyurmaktır, hesap ise Bize düşer, source:13:40}. Önceki sure de aynı sırayı izler: önce {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefeati'z-zikrâ, gloss:hatırlatma fayda verirse hatırlat, source:87:9}, sonra {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}, sonra {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11} ve en büyük ateş gelir. Başka yerlerde de şöyle denir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve zekkir fe-inne'z-zikrâ tenfeu'l-mu'minîn, gloss:hatırlat; hatırlatma inananlara fayda verir, source:51:55}; {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ tezkira, gloss:hayır; bu bir hatırlatmadır, source:80:11}; {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:80:12}.

Kaynaklar: 88:21 فَذَكِّرْ ذ ك ر B009; 88:21 مُذَكِّرٌ ذ ك ر B003; 88:22 لَّسْتَ ل ي س B001; 88:22 بِمُصَيْطِرٍ س ط ر B001; 88:22 بِمُصَيْطِرٍ س ط ر B003; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:23 تَوَلَّىٰ و ل ي B003; 88:23 تَوَلَّىٰ و ل ي B007; 88:23 وَكَفَرَ ك ف ر B003; 88:24 ٱللَّهُ ء ل ه B001; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

