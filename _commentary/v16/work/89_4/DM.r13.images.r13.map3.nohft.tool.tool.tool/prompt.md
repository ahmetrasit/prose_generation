Focus: 89:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_4/D.r13/context.md =====
# 89:4 — focus

وَٱلَّيْلِ إِذَا يَسْرِ

Anchor translation (canonical reading, reference only):

Geçip gittiğinde geceye andolsun!

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلَّيْلِ | لَيْل | ل ي ل | CONJ;DET;N |
| 2 | إِذَا | إِذَا |  | T |
| 3 | يَسْرِ | يَسْرِ | س ر ي | V |


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
- 89:4 ◀ focus وَٱلَّيْلِ إِذَا يَسْرِ
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
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ل ي ل (root_001392) — identity root of وَٱلَّيْلِ (w1)

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## س ر ي (root_000702) — identity root of يَسْرِ (w3)

- **B001** geceleyin yol alma ve gece götürme — gece yolculuğu · geceleyin yol aldı · geceleyin yol aldı · onu gece götürdü · onu gece götürdü · gece gelen veya ilerleyen bulut · gece yol alan topluluk · küçük asker birliği
  السرى سير الليل (maqayis;ayn;sihah;mufradat)؛ سرى وأسرى لغتان (ayn;mufradat)؛ سريت سرى ومسرى وأسريت بمعنى (sihah)؛ السارية للقوم الذين يسرون بالليل وللسحابة التي تسري (mufradat)؛ السارية من السحاب التي تجيء ليلا (ayn;sihah)؛ السرية قطعة من الجيش (sihah)
- **B002** küçük akarsu ve toprağa yayılan kök — küçük dere · akan küçük dere · ağacın kökü toprağın içinde ilerledi
  السرى أيضا نهر صغير كالجدول (sihah)؛ سريا أي نهرا يسري (mufradat)؛ سرى عرق الشجرة يسري في الأرض سريا دب دبيبا فيها (ayn)
- **B003** üstlük, seçkinlik ve en iyiyi seçme — bir şeyin üstü veya arkası · günün yükselmiş veya orta vakti · seçkin ve saygın kişi · yüce nitelikli adam · erdemli cömertlik ve yücelik · seçkin duruma geldi · seçkin duruma gelme · seçkin görünmeye çalıştı · en seçkinlerini seçti · ölüm o topluluğun önde gelenlerini aldı · sürüsünün ve malının en iyi bölümü · yücelik veya seçkinliğe işaret eden kullanım
  سراة الشيء ظهره وسراة النهار ارتفاعه (maqayis;mufradat)؛ سراة كل شيء أعلاه وسراة النهار وسطه (sihah)؛ السرو سخاء في مروءة (maqayis;sihah)؛ رجل سرو (mufradat)؛ استريت الإبل والغنم والناس أي اخترتهم (sihah)
- **B004** üzerindekini kaldırma ve sıkıntının dağılması — bir şeyi üzerindekini kaldırarak açığa çıkarma · giysiyi üzerinden çıkarma · zırhını üzerinden atma · öfkesi veya baygınlığı geçti · kaygım dağıldı · kaygım dağıldı
  السرو كشف الشيء عن الشيء (maqayis)؛ سروت عني الثوب أي كشفته (maqayis)؛ سرى عن فلان أي تجلى عنه الغضب أو غشية (ayn)؛ انسرى عني الهم انكشف وسري عني الهم مثله (sihah)؛ سروت الثوب عني أي نزعته (mufradat)
- **B005** taş veya tuğla dikme — taş veya tuğla dikme
  السارية الأسطوانة (maqayis;sihah)؛ السارية أسطوانة من حجارة أو آجر (ayn)؛ السارية يقال للأسطوانة (mufradat)
- **B006** özel adlandırma kümesi — bir ağaç türü · belirli bir topluluğa ait yerleşim · başka bir yer türüne benzer yer · yay yapılan bir ağaç · küçük bir hayvan veya çekirgenin kurtçuk evresi · bu küçük hayvanın çok bulunduğu arazi · küçük ok
  السرو شجر (sihah)؛ السرو محلة حمير (maqayis;sihah)؛ السرو مثل الخيف (sihah)؛ السراء شجر (maqayis;sihah)؛ السروة دويبة (maqayis)؛ السروة سهم صغير (sihah)

## ECHO س ر ر (root_000697) — for يَسْرِ (w3): withheld observed target; not identity

- **B001** saklama ve gizli paylaşım — gizlenen bilgi veya durum · kişinin gizli iç durumu veya gizlice yaptığı iş · bir şeyi gizleyip saklamak · birine bir sözü gizlice açmak · kulağına gizlice söylemek · kendi aralarında gizlice konuşmak · gizlice konuşmaya yarayan tomar benzeri araç
  السر خلاف الإعلان (maqayis)؛ السر ما أسررت والسريرة عمل السر (ayn)؛ السر الذي يكتم والسريرة مثله (sihah)؛ الإسرار خلاف الإعلان والسر هو الحديث المكتم في النفس (mufradat)؛ ساره في أذنه وتساروا (sihah)
- **B002** açığa vurma, tartışmalı kullanım — 
  أسررته أعلنته (maqayis)؛ أسررت الشيء أظهرته وكتمته أيضا (jamhara)؛ أسررت الشيء كتمته وأعلنته أيضا (sihah)؛ قال الفراء أخطأ أبو عبيدة (maqayis)؛ لم أسمع ذلك لغيره (tahdhib)
- **B003** gizli tutulan evlilik veya cinsel ilişki — 
  السر وهو النكاح (maqayis)؛ السر الجماع والسر الذكر (sihah)؛ السر النكاح والزنى وخطبة المعتدة (tahdhib)؛ كني عن النكاح بالسر من حيث إنه يخفى (mufradat)
- **B004** ayın görünmediği ay sonu — ayın sonunda hilalin görünmediği bir veya iki günlük dönem · ayın son gecesi
  السرار ليلة يستسر الهلال (maqayis)؛ السرار يوم يستسر فيه الهلال آخر يوم من الشهر (ayn)؛ سرر الشهر آخر ليلة منه وكذلك سراره (sihah)؛ السرار اليوم الذي يستتر فيه القمر آخر الشهر (mufradat)
- **B005** bir şeyin arı özü veya en seçkin bölümü [kalıp] — bir şeyin katkısız özü · topluluğunun merkezindeki en seçkin kesim · soyun katkısız ve en seçkin kolu · vadinin toprağı en iyi veya en elverişli yeri · bir şeyin özü ve üstün niteliğinin çekirdeği
  السر خالص الشيء وسر النسب (maqayis)؛ سر كل شيء خالصه وسر الوادي وسراره أطيبه ترابا (jamhara)؛ في سر قومه أي في أوسطهم وسر الوادي أفضل موضع (sihah)؛ استعير للخالص ومنه سر الوادي وسرارته (mufradat)
- **B006** göbek ve kesilen göbek bağı parçası — göbek · bebekten kesilen göbek bağı parçası · bebeğin göbek bağı parçasını kesmek
  السرة سرة الإنسان (maqayis)؛ السرة في البطن موضع السرر الذي يقطع من الصبي (jamhara)؛ السر ما تقطعه القابلة من سرة الصبي (sihah)؛ سرة البطن ما يبقى بعد القطع والسر والسرر لما يقطع منها (mufradat)
- **B007** devede gövde içi ağrı hastalığı — devede göbek, göğüs veya göğüs altı ağrısı · bu gövde ağrısına tutulmuş deve
  السرر داء يأخذ البعير في سرته (maqayis)؛ السرر داء يصيب الإبل في صدورها (jamhara)؛ بعير أسر وناقة سراء (sihah)؛ وجع يأخذ في الكركرة (tahdhib)
- **B008** içi oyuk olma ve oyuğa çubuk yerleştirme — ateş çubuğunun oyuğuna tutuşturma çubuğu yerleştirmek · içi oyuk boru biçimli çubuk · içi oyuk kişi
  سررت الزند وذلك أن يبقى أسر أي أجوف (maqayis)؛ قناة سراء أي جوفاء (maqayis)؛ سر زندك فإنه أسر أي أجوف (sihah)؛ رجل أسر إذا كان أجوف (tahdhib)
- **B009** avuç ve alın çizgileri — avuç içi çizgileri · alın veya yüz çizgileri ve kırışıklıkları
  الأسرار خطوط باطن الراحة (maqayis)؛ السر والسرار والجميع الأسرار خطوط راحة الكف (ayn)؛ السرر واحد أسرار الكف والجبهة (sihah)؛ أسرة الراحة وأسارير الجبهة (mufradat)
- **B010** sevinç ve gönence — üzüntüden uzak iç sevinci · beni sevindirdi · rahatlık, bolluk ve gönence · iyilik eden ve sevindiren kişi
  السرور أمر خال من الحزن (maqayis)؛ السر ضد الضر وقال قوم السر والسرور واحد (jamhara)؛ السراء الرخاء نقيض الضراء (sihah)؛ السرور ما ينكتم من الفرح (mufradat)
- **B011** oturma, yaslanma veya dinlenme yeri — oturulan, yaslanılan veya yatılan yer · başın dayandığı yer · yaşamın yerleşik rahatlığı ve dinginliği
  السرير وجمعه سرر وأسرة (maqayis)؛ سرير الرأس مستقره (maqayis)؛ السرير معروف والعدد أسرة والجميع السرر (tahdhib)؛ السرير الذي يجلس عليه من السرور (mufradat)
- **B012** bitkinin nemli üst bölümleri [kalıp] — bitkilerin nemli uçları veya gövdelerinin üst yarıları
  أطراف الريحان تسمى سرورا لأنها أرطب شيء فيه (maqayis)؛ السرور من النبات أنصاف سوقها العلى (tahdhib)
- **B013** yer mantarı üzerindeki kabuk ve toprak [kalıp] — yer mantarı üzerindeki kabuk, çamur ve toprak
  السرر ما على الكمأة من القشور والطين (sihah)؛ السرار ما على الكمأة من القشور والتراب (tahdhib)
- **B014** işlerin inceliğini bilen becerikli kişi — işlerin inceliğini bilen kavrayışlı kişi · sevdiğim ve çok yakın bulduğum kişi
  السرسور العالم الفطن (maqayis)؛ السرسور العالم الفطن الدخال في الأمور (sihah)؛ سرسور هذا الأمر إذا كان عالما به (tahdhib)؛ سرسوري وسرسورتي أي حبيبي وخاصتي (tahdhib)
- **B015** tepecik üzerindeki kum tabakası — küçük bir tepenin üzerindeki kum
  السري ما على الأكمة من الرمل (maqayis)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:4, and ## Buluşmalar) =====
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

## Gözetleme yeri ve bakan göz

Altıncı ayet dinleyenin gözünü olup bitene çevirir: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:e-lem tera keyfe feale rabbuke bi-Âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Görmek, gözle ya da kalple bakmaktır: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakıp görmek, source:"ر ء ي,B001"}. Aynı kalıp Fil sahiplerinin akıbetini anlatırken de kullanılır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ, tr:e-lem tera keyfe feale rabbuke bi-ashâbi'l-fîl, gloss:Rabbinin fil sahiplerine ne yaptığını görmedin mi, source:105:1}. Dinleyen, bir olayın gözlemcisi yapılır.

Gözlenen şey yolda olan insanlardır. Dördüncü ayetin fiili gece yürüyenleri de adlandırır: {ar:السارية للقوم الذين يسرون بالليل, tr:es-sâriye li'l-kavmi'llezîne yesrûne bi'l-leyl, gloss:sâriye, gece yol alan topluluktur, source:"س ر ي,B001"}. Dokuzuncu ayetteki fiilin yanında ülkeleri boydan boya geçmek duyulur: {ar:جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها, tr:cubtu'l-bilâde ecûbuhâ ve ecîbuhâ ve'ctebtuhâ izâ kata'tuhâ, gloss:ülkeleri boydan boya geçtim, source:"ج و ب,B002"}. On birinci ayette bu yolcular ülkelerde sınırı aşar: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı geçmek, source:"ط غ ي,B001"}. Ayetlerin anlamı kazmak ve azmaktır. Yanında yol alan, ülke aşan ve sınırı geçen yolcular duyulur.

On dördüncü ayet yolun üzerindeki yeri adlandırır: {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin elbette gözetleme yerindedir, source:89:14}. Mirsâd hem yolun kendisidir, {ar:المرصاد الطريق, tr:el-mirsâd et-tarîk, gloss:mirsâd yoldur, source:"ر ص د,B003"}, hem de gözcünün beklediği yer: {ar:المرصاد المكان الذي يرصد به الراصد, tr:el-mirsâdu'l-mekânu'llezî yersudu bihi'r-râsıd, gloss:mirsâd, gözcünün gözetlediği yerdir, source:"ر ص د,B003"}. Gözcü bir şeyi kollayan kişidir: {ar:الراصد للشئ المراقب له, tr:er-râsıdu li'ş-şey'i el-murâkıbu leh, gloss:râsıd, bir şeyi gözetleyendir, source:"ر ص د,B001"}. Aynı kök yolda pusu kuran yılana da ad verir: {ar:يقال للحية التي ترصد المارة على الطريق رصيد, tr:yukâlu li'l-hayyeti'lletî tersudu'l-mârrate ale't-tarîki rasîd, gloss:yolda geçenleri kollayan yılana rasîd denir, source:"ر ص د,B001"}. Bu düzenin işleyişi şöyledir: gözcü kimseyi kovalamaz, yolun geçtiği yerde bekler. Her yolcu oradan geçmek zorundadır. Bir önceki ayetteki dökme fiili bu yılanın hareketini de anlatır: {ar:صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق, tr:sabbeti'l-hayyetu aleyhi izertefeat fensabbet aleyhi min fevk, gloss:yılan kalkıp yukarıdan üstüne çullandı, source:"ص ب ب,B008"}. Surenin sıralaması da bu düzene uyar. Önce darbe iner, gözetleme yeri ancak sonra adlandırılır. Yolcular gözcünün varlığını vuruldukları anda öğrenir.

Kur'an aynı yeri başka sahnelerde de kurar. Kıyamet anlatılırken cehennem için {ar:إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا, tr:inne cehenneme kânet mirsâdâ, gloss:cehennem bir gözetleme yeridir, source:78:21} denir. Antlaşmayı bozanlara karşı verilen emir şöyledir: {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehum kulle marsad, gloss:onlar için her gözetleme yerinde oturun, source:9:5}. İblis de Allah'a şöyle der: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ek'udenne lehum sırâtake'l-mustekîm, gloss:onlar için senin dosdoğru yolunun üstünde oturacağım, source:7:16}. Şuayb kavmine yollarda pusu kurmamalarını söyler: {ar:وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ, tr:ve lâ tak'udû bi-kulli sırâtin tûidûn, gloss:tehdit ederek her yolun başında oturmayın, source:7:86}. Cinler gökte kendilerini bekleyen bir alev bulur: {ar:يَجِدْ لَهُۥ شِهَابًۭا رَّصَدًۭا, tr:yecid lehû şihâben rasadâ, gloss:kendisini gözetleyen bir alev bulur, source:72:9}. Allah elçisinin önüne ve arkasına gözcüler koyar {source:72:27}. İnsanın söylediği her sözün yanında da hazır bir gözcü vardır: {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözcü vardır, source:50:18}.

Bakmanın bir de insanın içindeki yüzü vardır. On beşinci ve yirmi üçüncü ayetlerdeki "insan" kelimesi göz bebeğindeki küçük sureti de adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, gözbebeğinin karasında görünen küçük surettir, source:"ء ن س,B005"}. Bu tanımda misal ve görmek kelimeleri birlikte geçer. Sekizinci ayetin kökü sureti, {ar:التمثال الصورة, tr:et-timsâl es-sûra, gloss:timsal, surettir, source:"م ث ل,B008"}, ve görülerek alınan dersi de adlandırır: {ar:يكون المثل بمعنى العبرة, tr:yekûnu'l-meselu bi-ma'ne'l-ibra, gloss:mesel, ibret anlamına da gelir, source:"م ث ل,B011"}. Beşinci ayetin hicr kökü gözün çevresine de ad verir: {ar:ومحجر العين ما يدور بها, tr:ve mahcaru'l-ayni mâ yedûru bihâ, gloss:gözün mahceri, onu çevreleyen yerdir, source:"ح ج ر,B006"}. Üçüncü ayetteki çift kelimesi de bir tek şeyi iki gören gözü adlandırır: {ar:عين شافعة تنظر نظرين, tr:aynun şâfiatun tenzuru nazarayn, gloss:şâfia göz, iki bakışla bakan gözdür, source:"ش ف ع,B006"}. Sure insana Âd'ı, Semûd'u ve Firavun'u göstermiştir. İnsan ise hemen ardından kendi hâline bakar ve tek bir sınavı iki ayrı hüküm olarak okur: bolluğa ikram, darlığa aşağılanma der. Kur'an bu bakışın kendini nasıl gördüğünü söyler {source:96:7}. Âd'a da kulaklar, gözler ve gönüller verilmişti, ama onlara bir yararı olmadı: {ar:فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ, tr:fe-mâ ağnâ anhum sem'uhum ve lâ ebsâruhum, gloss:ne kulakları ne gözleri onlara bir yarar sağladı, source:46:26}. Kıyamet günü örtü kalkar: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık, bugün gözün keskindir, source:50:22}.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B006; 89:4 يَسْرِ س ر ي B001; 89:5 حِجْرٍ ح ج ر B006; 89:6 تَرَ ر ء ي B001; 89:8 مِثْلُهَا م ث ل B008; 89:8 مِثْلُهَا م ث ل B011; 89:9 جَابُوا۟ ج و ب B002; 89:11 طَغَوْا۟ ط غ ي B001; 89:13 فَصَبَّ ص ب ب B008; 89:14 لَبِٱلْمِرْصَادِ ر ص د B001; 89:14 لَبِٱلْمِرْصَادِ ر ص د B003; 89:15 ٱلْإِنسَٰنُ ء ن س B005

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

