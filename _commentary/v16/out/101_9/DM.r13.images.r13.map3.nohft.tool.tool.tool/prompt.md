Focus: 101:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_9/D.r13/context.md =====
# 101:9 — focus

فَأُمُّهُۥ هَاوِيَةٌۭ

Anchor translation (canonical reading, reference only):

onun anası bir uçurumdur.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَأُمُّهُۥ | أُمّ | ء م م | RSLT;N;PRON |
| 2 | هَاوِيَةٌ | هَاوِيَة | ه و ي | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 101 — full text (context; no pericope)

- 101:1 ٱلْقَارِعَةُ
- 101:2 مَا ٱلْقَارِعَةُ
- 101:3 وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 ◀ focus فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء م م (root_000053) — identity root of فَأُمُّهُۥ (w1)

- **B001** anne ve annelik işlevi — anne · anneler · anneler; özellikle insan dışı canlılar için kullanılan çoğul · anne yokluğu üzerinden öven ya da yeren kalıp söz
  الأم الواحد والجمع أمهات وربما قالوا أم وأمات وفلانة تؤم فلانا أي تغذوه وتربيه (maqayis)؛ الأم معروفة (jamhara)؛ الأم الوالدة والجمع أمات وأصل الأم أمهة لذلك تجمع على أمهات وأمت المرأة صارت أما (sihah)؛ الأم بإزاء الأب وهي الوالدة القريبة والبعيدة (mufradat)
- **B002** ana kaynak ve toplayıcı odak — bir şeyin kaynağı, başlangıcı veya parçalarının döndüğü odak · Mekke; bağlama göre çevresindeki yerleşimleri toplayan ana kent · kitabın ana kaynağı; bağlama göre başlangıç bölümü veya korunmuş ana kayıt · bir şeyin kaynağını, odağını veya ana bölümünü gösteren adlandırma
  كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما (maqayis)؛ كل شيء يضم إليه سائر ما يليه فإن العرب تسمي ذلك الشيء أما (ayn)؛ كل شيء انضمت إليه أشياء فهو أم (jamhara)؛ أم الشيء أصله ومكة أم القرى (sihah)؛ كل ما كان أصلا لوجود شيء أو تربيته أو إصلاحه أو مبدئه أم (mufradat)
- **B003** beyin bölgesi ve ona ulaşan baş yarası — beyin veya baş içindeki beyin bölgesi · beyne ulaşan baş yarası · başından beyin bölgesine ulaşan darbeyle yaralanmış kişi · ağır baş yaralısı; baş ezmeye yarayan taş
  أم الرأس وهو الدماغ والشجة الآمة التي تبلغ أم الدماغ (maqayis)؛ أم الرأس وهو الدماغ ورجل مأموم والشجة الآمة التي تبلغ أم الدماغ (ayn)؛ أم رأسه بالعصا إذا أصاب أم رأسه وهي أم الدماغ (jamhara)؛ أم الدماع الجلدة التي تجمع الدماغ ويقال أيضا أم الرأس وأمه أي شجه آمة (sihah)؛ أمه شجه فحقيقته أن يصيب أم دماغه (mufradat)
- **B004** ortak bağla birleşen topluluk veya tür — ortak bir bağla birleşen topluluk veya canlı türü
  كل قوم نسبوا إلى شيء وأضيفوا إليه فهم أمة وكل جيل من الناس أمة (maqayis)؛ كل قوم في دينهم من أمتهم وكل جيل من الناس هم أمة وكل جنس من السباع أمة (ayn)؛ الأمة القرن من الناس (jamhara)؛ الأمة الجماعة وكل جنس من الحيوان أمة (sihah)؛ الأمة كل جماعة يجمعهم أمر ما (mufradat)
- **B005** benimsenen inanç ve yaşayış yolu — benimsenen inanç veya yaşayış yolu · inanç veya izlenen yol anlamındaki değişik söyleyiş
  الأمة الدين (maqayis)؛ الأمة كل قوم في دينهم من أمتهم (ayn)؛ الأمة الملة (jamhara)؛ الأمة الطريقة والدين والإمة أيضا لغة في الأمة وهي الطريقة والدين (sihah)؛ إنا وجدنا آباءنا على أمة أي على دين مجتمع (mufradat)
- **B006** boy ve beden görünüşü — insanın boyu, beden yapısı veya görünüşü
  الأمة القامة وطوال الأمم وبدنه ووجهه وما أحسن أمته أي خلقه (maqayis)؛ طوال الأمم يعني القامة والجسم (ayn)؛ الأمة قامة الإنسان والأمة الطول (jamhara)؛ الأمة القامة (sihah)
- **B007** okuma yazma bilmeyen — okuma yazma bilmeyen kişi
  الأمي في اللغة المنسوب إلى ما عليه جبلة الناس لا يكتب (maqayis)؛ الأمي هو الذي لا يكتب ولا يقرأ من كتاب وقيل منسوب إلى الأمة الذين لم يكتبوا وقيل لنسبته إلى أم القرى (mufradat)
- **B008** bir süre, zaman dilimi — bir süre veya zaman dilimi
  الأمة في قوله وادكر بعد أمة أي بعد حين (maqayis)؛ الأمة الحين (sihah)؛ وادكر بعد أمة أي حين وحقيقة ذلك بعد انقضاء أهل عصر أو أهل دين (mufradat)
- **B009** öne konulan ve izlenen kılavuz — önder veya izlenen kılavuz · birlikte kılınan namazda öne geçip önderlik etmek
  الإمام كل من اقتدي به وقدم في الأمور والخيط الذي يقوم عليه البناء إمام (maqayis)؛ كل من اقتدي به وقدم في الأمور فهو إمام والإمام الطريق (ayn)؛ إن إبراهيم كان أمة أي إماما ورئيس القوم أما لهم (jamhara)؛ أممت القوم في الصلاة إمامة والإمام الذي يقتدى به والإمام الطريق (sihah)؛ الإمام المؤتم به إنسانا أو كتابا أو غير ذلك (mufradat)
- **B010** iyilik ve iyi durum — iyilik, bolluk veya iyi durum
  الأمة النعمة (maqayis)؛ الإمة النعمة (ayn)؛ الإمة النعمة (jamhara)؛ الإمة بالكسر النعمة (sihah)
- **B011** ön taraf ve yakın konum — ön, ön taraf veya ilerisi · yakın, erişilebilir veya orta uzaklıkta olan
  الأمام القدام وامض يمامي في معنى امض أمامي والأمم الشيء القريب المتناول (maqayis)؛ الأمام بمنزلة القدام والأمم الشيء القريب (ayn)؛ سرت أمام الرجل وأمامته ويمامته (jamhara)؛ كنت أمامه أي قدامه والأمم بين القريب والبعيد وأخذت ذلك من أمم أي من قرب (sihah)
- **B012** amaçlayıp yönelmek — bir şeyi amaçlayıp ona yönelmek · bir şeyi bilerek seçmek ve hedeflemek · kutsal eve yönelenler
  الأمم القصد وآمين البيت الحرام أي يقصدونه والتيمم يجري مجرى التوخي أي تعمدوا (maqayis)؛ أم يؤم أما إذا قصد للشيء (jamhara)؛ الأم بالفتح القصد أمة وأممه وتأممه إذا قصده (sihah)؛ الأم القصد المستقيم وهو التوجه نحو مقصود (mufradat)
- **B013** az, küçük veya önemsiz şey — az, küçük ya da değersiz şey
  الأمم الشيء اليسير الحقير وأمم أي صغير وعظيم من الأضداد (maqayis)؛ الأمم الشيء اليسر الهين الحقير (ayn)؛ الامم الشئ اليسير يقال ما سألت إلا أمما (sihah)
- **B014** genç kız veya kadın köle — genç kız veya kadın köle
  الأمة الوليدة (jamhara)
- **B015** insandaki kusur — insandaki kusur veya ayıp
  الآمة العيب (ayn)؛ الأمة العيب في الإنسان (jamhara)
- **B016** seçenek veya düzeltme bildiren soru bağlacı — iki soru seçeneğini bağlayan veya düzeltmeli yeni soru açan "yoksa"
  أم مخففة حرف عطف في الاستفهام تقع معادلة لألف الاستفهام بمعنى أي وتكون منقطعة (sihah)؛ أم إذا قوبل به ألف الاستفهام فمعناه أي وإذا جرد عن ذلك يقتضي معنى ألف الاستفهام مع بل (mufradat)

## ه و ي (root_001609) — identity root of هَاوِيَةٌ (w2)

- **B001** hava ve boşluk; kalpte boşluk ve yüreksizlik — hava; boşluk veya aralık · kalpleri bomboş, kavrayışsız ve kararsızdır · yüreksiz, korkak ya da akılsız kimse
  الهَواء ممدود هو الجو (ayn)؛ قلبه هَواء (ayn)؛ هَواء الجو ممدود (jamhara)؛ الهَواء ما بين السماء والأرض وكل خال هواء (sihah)؛ الهَواء والخواء واحد (tahdhib)؛ الهَواء كل فرجة بين شيئين (tahdhib)؛ هوى صدره أي خلا (tahdhib)؛ الهوهاءة الضعيف الفؤاد الجبان (tahdhib)؛ الهَواء ما بين الأرض والسماء (mufradat)؛ أصل صحيح يدل على خلو وسقوط (maqayis)؛ أصله الهَواء بين الأرض والسماء سمي لخلوه (maqayis)
- **B002** yukarıdan düşme; yönlü gidiş, derin çukur, düşürme, ölüm ve yas bağlantıları — yukarıdan aşağı düştü veya indi · dipsiz uçurum; ateş azabının adı · derin çukur veya düşme yeri · topluluk derin çukura birbiri ardınca düştü
  هوى الطائر يهوي هويا (ayn)؛ هاوية من أسماء جهنم والهاوية كل مهواة لا يدرك قعرها (ayn)؛ هوى فلان أي مات (ayn)؛ هوى الشيء يهوي إذا خر من علو إلى سفل (jamhara)؛ هوى بالفتح يهوي هويا أي سقط إلى أسفل (sihah)؛ الهاوية اسم من أسماء النار والهاوية المهواة (sihah)؛ هوت أمه فهي هاوية أي ثاكلة (sihah)؛ هويت أهوي هويا إذا سقطت من علو إلى أسفل (tahdhib)؛ المؤتفكة أهوى أي أسقطها (tahdhib)؛ الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة (tahdhib)؛ الهوي سقوط من علو إلى سفل (mufradat)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ هوى الشيء يهوي سقط (maqayis)؛ تهاوى القوم في المهواة سقط بعضهم في إثر بعض (maqayis)
- **B003** eli ya da nesneyi hedefe yöneltmek; yukarıdan atmak — almak için elini ona uzattı · nesneyle işaret etti veya kılıçla vurdu · onu yukarıdan aşağı attı
  أهوى إليه فأخذه أي أهوى إليه يده (ayn)؛ أهوى إليه بيده ليأخذه (sihah)؛ أهويت بالشيء إذا أومأت به (sihah)؛ أهويت له بالسيف (sihah)؛ أهويت له بالسيف وغيره (tahdhib)؛ أهويته إذا ألقيته من فوق (tahdhib)؛ هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء (tahdhib)؛ أهوى إليه بيده ليأخذه كأنه رمى إليه بيده إذا أرسلها (maqayis)
- **B004** benliğin sevgi ve isteğe yönelmesi — benliğin sevgiye veya isteğe yönelmesi · sevdi, gönlü ona yöneldi · ötekinden daha çok sevilen · çeşitli kişisel eğilimlerin izleyicileri
  الهَوَى مقصور الحب (ayn)؛ هوى النفس مقصور (jamhara)؛ الهَوَى مقصور هوى النفس والجمع الأهواء (sihah)؛ هوى بالكسر يهوى هوى أي أحب (sihah)؛ هذا الشيء أهوى إلى من كذا أي أحب إلي (sihah)؛ أفئدة من الناس تهوى إليهم يقول تريدهم (tahdhib)؛ وتهوي إليهم تهواهم (tahdhib)؛ الهَوَى مقصور هوى الضمير (tahdhib)؛ أهل الأهواء واحدها هوى (tahdhib)؛ الهَوَى ميل النفس إلى الشهوة (mufradat)؛ الهوى هوى النفس فمن المعنيين جميعا (maqayis)؛ هويت أهوى هوى (maqayis)
- **B005** ayartıp şaşkınlığa ve isteklerinin peşine sürüklemek [kalıp] — ayartıcı güçler onu yoldan çıkarıp şaşkınlığa sürükledi
  استهوته الشياطين فهو حيران هائم (ayn)؛ استهواه الشيطان أي استهامه (sihah)؛ استهوته الشياطين فهو حيران هائم (tahdhib)؛ كالذي زينت له الشياطين هواه حيران (tahdhib)؛ استهوته الشياطين هوت به وأذهبته (tahdhib)؛ استهوته الشياطين أي حملته على اتباع الهوى (mufradat)
- **B006** uzun bir zaman veya gecenin bir bölümü — uzun bir zaman · gecenin bir bölümü veya dilimi
  الهوي الملي الحين الطويل من الزمان (ayn)؛ مر هوي من الليل أي قطعة منه وكذلك تهواء من الليل (jamhara)؛ مضى هوى من الليل أي هزيع منه (sihah)؛ الهوي الملي الحين الطويل من الزمان (tahdhib)
- **B007** yaranın açılması veya gövdenin boşalıp oyuklaşması [kalıp] — saplama yarası açılıp genişledi · böğür bölgesi zayıflıktan oyuklaşıp açıldı
  هوت الطعنة تهوى فتحت فاها (sihah)؛ هوى بين الكلى والكراكر (sihah)؛ هوت الطعنة إذا فتحت فاها (tahdhib)؛ خلا وانفتح من الضمر (tahdhib)؛ هوى صدره يهوي هواء إذا خلا (tahdhib)؛ هوت الطعنة فتحت فاها تهوى وهو من الهواء الخالي (maqayis)
- **B008** hızlı yönlü ilerleme, atılımlı koşu ve sert yol alma — hızlı veya güçlü ilerleme · yırtıcı kuş hızla daldı veya deve güçlü biçimde koştu · sert ve hızlı yol alma · çeşitli yol alış biçimleri
  الهوي في السير إذا مضى (sihah)؛ المهاواة شدة السير (sihah)؛ الهوي في السير إذا مضى (tahdhib)؛ الهوي السريع إلى أسفل والهوي السريع إلى فوق (tahdhib)؛ هوت العقاب إذا انقضت (tahdhib)؛ هوت الناقة تهوي إذا عدت عدوا أرفع العدو (tahdhib)؛ الهواهي ضروب من السير (tahdhib)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ الهوي ذهاب في انحدار والهوى في الارتفاع (maqayis)؛ شدة السير لما في ذلك من الترامي بالأبدان عند السير (maqayis)
- **B009** karşılıklı inatlaşma ve çekişme — karşılıklı inatlaşma ve çekişme
  المهاواة الملاجة (sihah)؛ المهاواة فذكر أبو عمرو أنها الملاجة (maqayis)؛ أما الملاجة فلأن كل واحد منهما يحب هوى صاحبه (maqayis)
- **B010** asılsız ve boş sözler — asılsız ve boş sözler
  الهواهي الباطل واللغو من القول (sihah)؛ الهواهي الأباطيل (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:9, and ## Buluşmalar) =====
## Vuruş: sıkı olanın dağılması

Surenin ilk kelimesi bir şeyi adıyla değil, yaptığı işle anar. {ar:ٱلْقَارِعَةُ, tr:el-kâria, gloss:vuran, çarpan, source:101:1} kelimesinin kökünde yatan iş, sert bir şeyin başka bir şeyin üstüne indirilmesidir: {ar:القرع ضرب شيء على شيء, tr:el-kar' darbu şey'in alâ şey', gloss:kar', bir şeyin bir şeye vurulmasıdır, source:"ق ر ع,B001"}. Binicinin hayvanını kamçıyla dürtmesi de aynı fiille söylenir: {ar:قرع راحلته أي ضربها بسوطه, tr:karaa râhilatehû, gloss:bineğini kamçısıyla vurdu, source:"ق ر ع,B001"}. Aynı kelime, insanların başına inen ağır belanın da adıdır: {ar:القارعة الشديدة من شدائد الدهر وهي الداهية, tr:el-kâria eş-şedîde min şedâidi'd-dehr, gloss:kâria, zamanın ağır sıkıntılarından biri, büyük felakettir, source:"ق ر ع,B005"}. Bir aile imgesi, kelimenin ayetteki anlamının yerine geçmez; o anlamın yanında duyulur. Burada kelimenin anlamı kıyamettir, duyulan imge ise bir darbenin inişi.

Bu darbe imgesini yalın bir açıklamadan ayıran şey, sonrasında olanlardır. Bir vuruş, sıkı ve bütün olan şeyi çözer; parçaları havaya kaldırır. Dördüncü ayet insanları {ar:ٱلْمَبْثُوثِ, tr:el-mebsûs, gloss:saçılmış, source:101:4} diye niteler. Bu kökün temel işi, rüzgârın toprağı kaldırıp dağıtması gibi bir dağıtmadır: {ar:التفريق وإثارة الشيء كبث الريح التراب, tr:et-tefrîk ve isâratu'ş-şey', gloss:ayırmak ve bir şeyi rüzgârın toprağı savurduğu gibi kaldırmak, source:"ب ث ث,B001"}; kışkırtılan toza da bu adla bakılır {source:"ب ث ث,B001"}. Beşinci ayetin dağları {ar:ٱلْمَنفُوشِ, tr:el-menfûş, gloss:didilmiş, atılmış, source:101:5} yündür. Yünün atılması da bir dövme işidir: {ar:نفش الصوف وهو أن يطرق حتى يتنفش, tr:nefşu's-sûf ve hüve en yutraka hattâ yetenaffeş, gloss:yünü atmak, kabarıp açılıncaya kadar onu dövmektir, source:"ن ف ش,B001"}. Yani dağların sonunu gösteren benzetme de darbelerle kurulmuştur. Yünü anlatan {ar:ٱلْعِهْنِ, tr:el-ıhn, gloss:boyalı yün, source:101:5} kelimesinin kökü, ayrıca kuvvetle kırılmış ama kopmamış, sarkıp kalmış bir dalı da adlandırır: {ar:أصل العاهن أن يتقصف القضيب من الشجرة ولا يبين منها فيبقى معلقا مسترخيا, tr:aslu'l-âhin en yetekassafe'l-kadîb, gloss:âhin, ağaçtan kırılıp ayrılmayan, asılı ve gevşek kalan daldır, source:"ع ه ن,B002"}. Sert bir biçim boyun eğmiş, ama yerinden kopmadan sallanıp kalmıştır.

Dokuzuncu ayetin {ar:هَاوِيَةٌ, tr:hâviye, gloss:düşülen derin çukur, source:101:9} kelimesinin kökü, darbenin öbür yarısını, vuran kolun inişini ve yukarıdan aşağı fırlatmayı da taşır: {ar:أهويت له بالسيف, tr:ehveytu lehû bi's-seyf, gloss:kılıcı ona doğru indirdim, source:"ه و ي,B003"}; {ar:أهويته إذا ألقيته من فوق, tr:ehveytuhû izâ elkaytuhû min fevk, gloss:onu yukarıdan attım, source:"ه و ي,B003"}. Böylece sure vuruştan saçılmaya, saçılmadan çukura atılışa doğru ilerler: önce iniş, sonra dağılma, en sonda hafif olanın aşağı fırlatılması.

Aynı kökler başa inen bir darbeyi de adlandırır. Kafatasının ince kemikleri {ar:فراش الرأس عظام رقاق تلي القحف, tr:ferâşu'r-re's izâmun rikâk, gloss:başın ferâşı, kafatasına bitişik ince kemiklerdir, source:"ف ر ش,B010"} diye anılır ve bir deyim, bu kemikleri uçuran vuruşu anlatır: {ar:ضربة فأطار فراش رأسه, tr:darbeten fe-etâra ferâşe re'sih, gloss:bir vuruş ki başının ince kemiklerini uçurdu, source:"ف ر ش,B011"}. Beynin zarına {ar:أم الرأس وهو الدماغ, tr:ummu'r-re's, gloss:başın anası, yani beyin, source:"ء م م,B003"} denir; ağzını açan yara için de {ar:هوت الطعنة إذا فتحت فاها, tr:hevet et-ta'ne, gloss:mızrak yarası ağzını açtı, source:"ه و ي,B007"} söylenir. Surenin kelimeleri bu dizilişte birbirini izler: birinci ayette vuruş, dördüncüde ferâş, dokuzuncuda ümm ve hâviye. Bu dizi bir aile imgesidir; ayetlerin anlamı kıyamet, insanlar, dağlar ve varılacak yerdir.

Kur'an bu darbeyi başka yerlerde de sahneler. Hâkka suresinde Allah, geçmiş kavimleri anlatırken {ar:كَذَّبَتْ ثَمُودُ وَعَادٌۢ بِٱلْقَارِعَةِ, tr:kezzebet Semûdu ve Âdun bi'l-kâria, gloss:Semûd ve Âd o çarpanı yalanladı, source:69:4} der; aynı surede yer ve dağlar kaldırılır ve {ar:فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ, tr:fe-dukketâ dekketen vâhide, gloss:bir tek çarpışla ezilip düzlendiler, source:69:14}. Ra'd suresinde Allah, inkâr edenler hakkında Peygamberine, onlara yaptıkları yüzünden {ar:قَارِعَةٌ أَوْ تَحُلُّ قَرِيبًۭا مِّن دَارِهِمْ, tr:kâriatun ev tehullu karîben min dârihim, gloss:bir çarpan, ya da yurtlarının yakınına inen bir bela, source:13:31} isabet etmeye devam edeceğini söyler; aynı ayet, Kur'an ile dağların yürütülmesini de anar. Vâkıa suresinde dağlar {ar:وَبُسَّتِ ٱلْجِبَالُ بَسًّۭا, tr:ve bussetil-cibâlu bessâ, gloss:dağlar ufalanıp un ufak edilir, source:56:5} ve {ar:فَكَانَتْ هَبَآءًۭ مُّنۢبَثًّۭا, tr:fe-kânet hebâen munbessâ, gloss:saçılmış toz olur, source:56:6}; buradaki "saçılmış", dördüncü ayetteki mebsûs ile aynı köktendir. Darbe ile dağılmanın arka arkaya gelişi, böylece Kur'an'ın kendi sahnesinde de görülür.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B005; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 ٱلْمَنفُوشِ ن ف ش B001; 101:5 كَٱلْعِهْنِ ع ه ن B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:4 كَٱلْفَرَاشِ ف ر ش B010; 101:4 كَٱلْفَرَاشِ ف ر ش B011; 101:9 فَأُمُّهُۥ ء م م B003; 101:9 هَاوِيَةٌ ه و ي B007

## Işığa düşen pervaneler

Dördüncü ayetin benzetmesi {ar:كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:ke'l-ferâşi'l-mebsûs, gloss:saçılmış pervaneler gibi, source:101:4} ifadesidir. Ferâş, ışığı arayarak uçan, sonunda kandile ya da ateşe düşen küçük kanatlı böcektir: {ar:الفراش التي تطير طالبة للضوء, tr:el-ferâş elletî tatîru tâlibeten li'd-dav', gloss:ferâş, ışığı arayarak uçan böceklerdir, source:"ف ر ش,B005"}; {ar:الفراشة التي تطير وتهافت في السراج, tr:el-ferâşe elletî tatîru ve tehâfetu fi's-sirâc, gloss:uçup kandile üşüşerek düşen pervane, source:"ف ر ش,B005"}; {ar:الفراش ما تراه كصغار البق يتهافت في النار, tr:yetehâfetu fi'n-nâr, gloss:küçük sinekler gibi ateşe üşüşüp düşenler, source:"ف ر ش,B005"}. Aynı kök, yere yakın kanat çırpışı da anlatır: {ar:تفرش الطائر إذا قرب من الأرض ورفرف بجناحه, tr:teferreşe't-tâir, gloss:kuş yere yaklaşıp kanat çırptı, source:"ف ر ش,B006"}. Mebsûs, sürünün dağılmasıdır; aynı fiil çekirgelerin yayılması için de kullanılır: {ar:انبث الجراد, tr:inbesse'l-cerâd, gloss:çekirgeler yayıldı, source:"ب ث ث,B001"}.

Benzetmenin açık anlamı, insanların dağınık, şaşkın ve sayısız oluşudur. Bu yüzeyin yanında, kelimenin içinden bir sahne duyulur: bir ateş vardır, sürü ona doğru uçar ve içine düşer. Surenin son kelimesi de nârdır, ateş. Ateşin kökü ışıkla birdir ve bu kök, aynı anda parlaklığı ve titrek, kararsız hareketi anlatır: {ar:النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة, tr:en-nûr ve'n-nâr, gloss:nur ve nar bu adı ışık saçtıkları ve titrek, hızlı hareketli oldukları için aldılar, source:"ن و ر,B002"}. Pervanenin çırpınışı ile alevin titreyişi aynı harekettir. Aynı kökte uzaktan görülen ateşe yönelmek de vardır: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}.

Surenin kelimeleri bu yolculuğun adımlarını sırayla verir. Dördüncü ayetin {ar:ٱلنَّاسُ, tr:en-nâs, gloss:insanlar, source:101:4} kelimesi, uzaktan bir ateşi fark etmek anlamındaki fiille birlikte anılan kökle ilişkilendirilir: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan bir ateş gördü, source:"ء ن س,B002"}. Dokuzuncu ayetin {ar:فَأُمُّهُۥ, tr:fe-ummuhû, gloss:onun anası, source:101:9} kelimesinin kökü, bir hedefe doğru yönelmeyi de anlatır: {ar:الأم القصد المستقيم وهو التوجه نحو مقصود, tr:el-emm el-kasdu'l-mustakîm, gloss:emm, bir hedefe doğru dosdoğru yönelmektir, source:"ء م م,B012"}. Hâviye kelimesinin kökü, bir topluluğun birbiri ardınca çukura düşüşünü anlatır: {ar:تهاوى القوم في المهواة سقط بعضهم في إثر بعض, tr:tehâve'l-kavmu fi'l-mehvât, gloss:topluluk çukura birbiri ardınca düştü, source:"ه و ي,B002"}; pervanelerin birer birer kandile düşüşü gibi. On birinci ayetin hâmiyesi ise sürünün vardığı yerin sıcaklığıdır: {ar:حمي الشيء يحمى حميا إذا سخن, tr:hamiye'ş-şey', gloss:şey ısındı, source:"ح م ي,B001"}. Işık, sürü, yöneliş, düşüş ve sıcaklık tek bir sahnede birleşir. Ateşin kökü bunun tersini de adlandırır, ürküp kaçmayı: {ar:النوار النفار, tr:en-nevâr en-nifâr, gloss:nevâr, ürküp kaçmaktır, source:"ن و ر,B006"}. Bir canlının ateş karşısında yapması gereken budur; pervanenin yaptığı ise tam tersidir.

Aynı türden bir cezbetme sahnesi avcılıkta da vardır. "Bildirmek" fiilinin kökü, avcının avı alıştırmak için diktiği deveyi adlandırır: {ar:الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد, tr:ed-diriyye, gloss:dirye, avın alışması için avcının diktiği dişi devedir, source:"د ر ي,B003"}; avcı onun arkasına saklanır ve görünmeden yaklaşır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytu's-sayd... ve dereytuhû hateltuh, gloss:avın nerede olduğuna baktım, henüz görmeden; ve onu pusuyla avladım, source:"د ر ي,B003"}. Aynı kökte mızrak talimi için dikilen halka da hedef olarak anılır {source:"د ر ي,B005"}. İnsanların kökü burada iki karşıt hali verir: ürkmeyen, alışmış hal, {ar:الأنس أنس الإنسان بالشيء إذا لم يستوحش منه, tr:el-uns, gloss:üns, insanın bir şeye ürkmeden alışmasıdır, source:"ء ن س,B003"}, ve bir şeyden kuşkulanınca etrafa bakınmak, {ar:الاستئناس النظر وأحس بما رابه, tr:el-isti'nâs, gloss:bakınmak ve kuşkulandığı şeyi sezmek, source:"ء ن س,B002"}. Mebsûs, avcının köpeklerini salmasıdır, {ar:بث الصياد كلابه, tr:bessa's-sayyâdu kilâbeh, gloss:avcı köpeklerini saldı, source:"ب ث ث,B001"}, hâviye ise kartalın avına pike yapması: {ar:هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء, tr:hevet el-ukâb, gloss:kartal pike yaptı; avını kollayınca ona daldı denir, source:"ه و ي,B003"}. Işık pervaneyi nasıl çekiyorsa, tuzak da avı öyle alıştırır. Üçüncü ve onuncu ayetteki "sana ne bildirdi" sorusu, bu aile imgesinde görünmeden yaklaşanın kökünde durur.

Kur'an'da ateşe yönelen insan sahnesi, bu imgenin tersini gösterir. Tâhâ suresinde Mûsâ, ailesiyle yolculuk ederken bir ateş görür: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran le'allî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Kasas suresi aynı sahneyi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-Tûri nârâ, gloss:Tûr tarafından bir ateş gördü, source:28:29} diye anlatır; Neml suresinde Mûsâ ateşten bir haber ya da ısınmak için bir kor getirmeyi umar {source:27:7}. Mûsâ'nın vardığı ateş yol gösterir; pervanenin vardığı ateş yakar. Bakara suresinde Allah, münafıkları ateş yakan birine benzetir: {ar:كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ, tr:ke-meseli'llezi'stevkade nâran fe-lemmâ edâet mâ havlehû zeheba'llâhu bi-nûrihim, gloss:ateş yakan biri gibi; ateş çevresini aydınlatınca Allah onların ışığını götürdü, source:2:17}; ışık ile ateşin aynı kökten oluşu orada da sahnenin kendisidir. Kamer suresinde Allah, insanların kabirlerden çıkışını {ar:كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ, tr:ke-ennehum cerâdun munteşir, gloss:yayılmış çekirgeler gibi, source:54:7} diye anlatır; Meâric suresinde ise {ar:كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ, tr:ke-ennehum ilâ nusubin yûfidûn, gloss:sanki dikili bir hedefe koşuşuyorlarmış gibi, source:70:43}. Hedefe koşan, birbiri ardınca düşen sürü, dördüncü ve dokuzuncu ayetlerin aile imgesinde de duyulur.

Kaynaklar: 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:4 كَٱلْفَرَاشِ ف ر ش B006; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:4 ٱلنَّاسُ ء ن س B002; 101:4 ٱلنَّاسُ ء ن س B003; 101:9 فَأُمُّهُۥ ء م م B012; 101:9 هَاوِيَةٌ ه و ي B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:11 نَارٌ ن و ر B002; 101:11 نَارٌ ن و ر B003; 101:11 نَارٌ ن و ر B006; 101:11 حَامِيَةٌ ح م ي B001; 101:3 أَدْرَىٰكَ د ر ي B003; 101:3 أَدْرَىٰكَ د ر ي B005; 101:10 أَدْرَىٰكَ د ر ي B003

## Çobansız sürü, seyrelen kalabalık

Menfûş kelimesinin kökü, yünün yanında bir sürü sahnesini de taşır: develerin ve koyunların geceleyin, çobansız, otlağa yayılması: {ar:نفشت الإبل والغنم أي رعت ليلا بلا راع ولا يكون النفش إلا بالليل, tr:nefeşeti'l-ibilu ve'l-ğanem, gloss:develer ve koyunlar geceleyin çobansız otladı; nefş ancak gece olur, source:"ن ف ش,B003"}; {ar:نفشت الإبل ترددت وانتشرت بلا راع, tr:nefeşeti'l-ibil, gloss:develer çobansız oraya buraya gidip yayıldı, source:"ن ف ش,B003"}. Ferâş kökü sürünün genç hayvanlarını ve yere yayılan ekini adlandırır: {ar:الفرش صغار الإبل, tr:el-ferş sığâru'l-ibil, gloss:ferş, küçük develerdir, source:"ف ر ش,B004"}; {ar:الفرش الزرع إذا فرش, tr:el-ferş ez-zer', gloss:ferş, yayıldığında ekindir, source:"ف ر ش,B008"}. Aynı açıklama, ferşi beşş ile, yani dördüncü ayetin iki kelimesini birbiriyle anlatır: {ar:يحتمل أن يكون مصدرا من فرشها الله أي بثها بثا, tr:ferşehâ'llâhu ey besse-hâ bessâ, gloss:Allah onları yaydı, yani saçıp dağıttı, source:"ف ر ش,B004"}. Kâria kökü ise otlakların sürülerce soyulup çıplak kalmasını ve ziyaretçisiz kalan avluyu anlatır: {ar:أصبحت الرياض قرعا قد جردتها المواشي, tr:asbahati'r-riyâdu kur'â, gloss:çayırlar hayvanların soyduğu çıplak yerler oldu, source:"ق ر ع,B008"}; {ar:قرع الفناء إذا خلا من الغاشية, tr:kari'a'l-finâ', gloss:avlu gelip gidenlerden boşaldı, source:"ق ر ع,B008"}. Hâviye kökü gecenin bir dilimini de adlandırır {source:"ه و ي,B006"}; sürünün başıboş kaldığı vakit.

İnsanların kendisi de bir topluluktur: {ar:الإنس جماعة الناس, tr:el-ins cemâ'atu'n-nâs, gloss:ins, insanların topluluğudur, source:"ء ن س,B001"}. Dağın kökü büyük bir insan kalabalığını da adlandırır: {ar:الجبل الجماعة العظيمة الكثيرة, tr:el-cibl el-cemâ'atu'l-azîme, gloss:cibl, büyük ve kalabalık topluluk, source:"ج ب ل,B002"}. Sekizinci ayetin fiili, bu kalabalığın seyrelmesini anlatır: {ar:خف القوم خفوفا أي قلوا وقد خفت زحمتهم, tr:haffe'l-kavmu hufûfen, gloss:topluluk azaldı, kalabalıkları hafifledi, source:"خ ف ف,B003"}; ve evlerinden hafifçe göçmelerini: {ar:خفوا عن منازلهم ارتحلوا منها في خفة, tr:haffû an menâzilihim, gloss:evlerinden hafifçe göçtüler, source:"خ ف ف,B002"}. Mebsûs bütün bunları tek kelimede toplar: {ar:كل شيء فرقته, tr:kullu şey'in ferraktehû, gloss:ayırıp dağıttığın her şey, source:"ب ث ث,B001"}. Bu aile imgesinde dördüncü ayetin insanları başıboş, gece dağılmış bir sürü gibidir; geride çıplak bir yer kalır.

Kur'an'da nefş fiili tam da bu sahnede geçer. Enbiyâ suresinde Allah, Dâvûd ile Süleymân'ın bir ekin hakkında hüküm verişini anlatır: {ar:إِذْ نَفَشَتْ فِيهِ غَنَمُ ٱلْقَوْمِ, tr:iz nefeşet fîhi ğanemu'l-kavm, gloss:o topluluğun koyunları geceleyin ona dağılıp otladığında, source:21:78}. En'âm suresinde Allah {ar:وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا, tr:ve mine'l-en'âmi hamûleten ve ferşâ, gloss:hayvanlardan yük taşıyanları ve küçükleri, source:6:142} yarattığını hatırlatır. Kalabalığın dağılışı da Kur'an'ın kıyamet sahnelerindedir: Zilzâl suresinde {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amellerini görmek için dağınık gruplar halinde çıkarlar, source:99:6}; Hac suresinde ise kıyametin sarsıntısında {ar:وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ, tr:ve tere'n-nâse sukârâ ve mâ hum bi-sukârâ, gloss:insanları sarhoş görürsün, oysa sarhoş değillerdir, source:22:2}.

Kaynaklar: 101:5 ٱلْمَنفُوشِ ن ف ش B003; 101:4 كَٱلْفَرَاشِ ف ر ش B004; 101:4 كَٱلْفَرَاشِ ف ر ش B008; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:1 ٱلْقَارِعَةُ ق ر ع B008; 101:9 هَاوِيَةٌ ه و ي B006; 101:4 ٱلنَّاسُ ء ن س B001; 101:5 ٱلْجِبَالُ ج ب ل B002; 101:4 يَكُونُ ك و ن B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B002

## Terazi: ağır kefe, hafif kefe

Altıncı ve sekizinci ayetler iki kefeyi karşı karşıya koyar: {ar:فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:fe-emmâ men sekulet mevâzînuhû, gloss:tartıları ağır gelen kimseye gelince, source:101:6} ve {ar:وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve emmâ men haffet mevâzînuhû, gloss:tartıları hafif gelen kimseye gelince, source:101:8}. Tartmanın tanımı, bir şeyin ağırlığını benzeriyle karşılaştırmaktır: {ar:الوزن ثقل شيء بشيء مثله, tr:el-vezn siklu şey'in bi-şey'in mislih, gloss:vezn, bir şeyin ağırlığını benzeri olan bir şeyle ölçmektir, source:"و ز ن,B001"}. Ağır olan kefe aşağı iner: {ar:الثقل رجحان الثقيل, tr:es-sikal rüchânu's-sakîl, gloss:ağırlık, ağır olanın basıp inmesidir, source:"ث ق ل,B001"}. Miskal, benzerine karşı konan bilinen bir ağırlıktır {source:"ث ق ل,B004"}. Mîzân ise hem alet hem adalettir: {ar:الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل, tr:el-âletu elletî yûzenu bihe'l-eşyâ', gloss:şeylerin tartıldığı alet mîzândır; mîzân adalettir, source:"و ز ن,B002"}.

Bu imgenin düz anlatımın ötesinde gösterdiği şey, ağırlığın değer olmasıdır. Değerli ve korunan her şey ağır sayılır: {ar:كل شيء نفيس مصون ثقل, tr:kullu şey'in nefîsin masûnin sekal, gloss:değerli, korunan her şey sekaldir, source:"ث ق ل,B005"}; insanlar ve cinler "iki ağırlık" diye anılır: {ar:سمي الجن والإنس الثقلين, tr:summiye'l-cinnu ve'l-insu's-sekaleyn, gloss:cinler ve insanlar iki ağırlık diye adlandırıldı, source:"ث ق ل,B005"}. Yerin ağırlıkları, onun hazineleri ve Âdemoğullarının bedenleridir {source:"ث ق ل,B002"}. Hafiflik ise tersine değersizliktir: {ar:ما لفلان عندنا وزن أي قدر لخسته, tr:mâ li-fulânin indenâ vezn, gloss:filanın yanımızda bir ağırlığı yok, yani değeri yok, source:"و ز ن,B007"}. Hafif gelmek hem ağırlıkta hem halde hafifliktir, {ar:الخفة خفة الوزن وخفة الحال, tr:el-hiffe hiffetu'l-vezn ve hiffetu'l-hâl, gloss:hafiflik, ağırlığın ve halin hafifliğidir, source:"خ ف ف,B001"}, iyi amellerin azlığıdır {source:"خ ف ف,B003"}, akıl hafifliğidir, {ar:وخفة الرجل طيشه, tr:ve hiffetu'r-raculi tayşuh, gloss:adamın hafifliği onun savrukluğudur, source:"خ ف ف,B004"}, ve hafife alınmaktır: {ar:استخف به أهانه, tr:istehaffe bihî, gloss:onu hafife aldı, aşağıladı, source:"خ ف ف,B005"}. Hafif olan kolayca yerinden oynatılır ve peşe takılır: {ar:استخفه فلان إذا استجهله فحمله على اتباعه في غيه, tr:istehaffehû fulân, gloss:onu cahil yerine koydu ve sapkınlığında kendisine uymaya sürükledi, source:"خ ف ف,B004"}.

Surenin öbür kelimeleri bu teraziyi önceden kurar. Dördüncü ayetin pervanesi hafifliğinden dolayı bu adı almıştır: {ar:الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف, tr:sumiye bi-zâlike li-hiffetih; el-ferâşe er-raculu'l-hafîf, gloss:pervane hafifliğinden ötürü böyle adlandırıldı; ferâşe hafif adamdır, source:"ف ر ش,B005"}; {ar:أطيش من فراشة, tr:etyaşu min ferâşe, gloss:pervaneden daha savruk, source:"ف ر ش,B005"}. Burada geçen savrukluk, sekizinci ayetin hafifliğini anlatan kelimenin ta kendisidir. Beşinci ayetin yünü içi boş liftir {source:"ن ف ش,B002"}; dağ ise iri, kalın gövdedir: {ar:ذو جبلة إذا كان غليظ الجسم, tr:zû cebeletin izâ kâne ğalîza'l-cism, gloss:iri gövdeli olan, source:"ج ب ل,B003"}. Yeryüzünün en ağır şeyi, en hafif şeye dönüşür. Dokuzuncu ayetin fiili hem hızlı bir düşüşü hem hızlı bir yükselişi anlatır: {ar:الهوي السريع إلى أسفل والهوي السريع إلى فوق, tr:el-huviyy es-serî' ilâ esfel ve'l-heviyy es-serî' ilâ fevk, gloss:aşağıya hızlı iniş ve yukarıya hızlı çıkış, source:"ه و ي,B002"}. Bir terazide hafif kefe yukarı kalkar; dokuzuncu ayette ise hafif kefenin sahibi aşağı düşer.

Kâria kelimesinin bir anlamı da ortaklar arasında paylaşılacak bir şey için kura çekmektir: {ar:أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه, tr:akra'tu beyne'ş-şurakâ', gloss:paylaşacakları bir şey için ortaklar arasında kura çektim, source:"ق ر ع,B004"}; {ar:الإقراع والمقارعة هي المساهمة, tr:el-ikrâ' ve'l-mukâra'a hiye'l-musâheme, gloss:kura çekmek, pay için ok atmaktır, source:"ق ر ع,B004"}. Bu adı taşıyan sureden sonra insanlar "fe-emmâ ... ve emmâ" ile iki paya ayrılır. Ama ayırma kura ile değil, iki şeyi karşı karşıya koyarak yapılır: {ar:وازنت بين الشيئين, tr:vâzentu beyne'ş-şey'eyn, gloss:iki şeyi tarttım, birbiriyle karşılaştırdım, source:"و ز ن,B003"}. Payı belirleyen tesadüf değil, ölçüdür. Kur'an'da kura çekilen iki sahne vardır: Sâffât suresinde Yûnus yüklü gemide {ar:فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ, tr:fe-sâheme fe-kâne mine'l-mudhadîn, gloss:kura çekti ve kaybedenlerden oldu, source:37:141}; Âl-i İmrân suresinde Allah, Peygambere Meryem'in kimin himayesine gireceği için {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne eklâmehum eyyuhum yekfulu Meryem, gloss:hangisinin Meryem'e bakacağı için kalemlerini atarlarken, source:3:44} orada olmadığını söyler.

Kur'an'da teraziyi açıkça kuran ayetler surenin kelimelerini aynen tekrarlar. A'râf suresinde Allah {ar:وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve'l-veznu yevmeizini'l-hakk, fe-men sekulet mevâzînuhû fe-ulâike humu'l-muflihûn, gloss:o gün tartı haktır; kimin tartıları ağır gelirse işte onlar kurtuluşa erenlerdir, source:7:8} ve {ar:وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم, tr:ve men haffet mevâzînuhû fe-ulâike'llezîne hasirû enfusehum, gloss:kimin tartıları hafif gelirse, işte onlar kendilerini kaybedenlerdir, source:7:9} der. Mü'minûn suresi aynı çifti verir {source:23:102} ve hafif gelenlerin {ar:فِى جَهَنَّمَ خَٰلِدُونَ, tr:fî cehenneme hâlidûn, gloss:cehennemde ebedî kalıcıdırlar, source:23:103} olduğunu ekler. Enbiyâ suresinde Allah {ar:وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ, tr:ve neda'u'l-mevâzîne'l-kıst li-yevmi'l-kıyâme, gloss:kıyamet günü için adalet terazilerini kurarız, source:21:47} der ve hardal tanesi ağırlığında bir şeyi bile getireceğini söyler. Kehf suresinde, ağırlıksızlığın değersizlik olduğu açıkça söylenir: {ar:فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا, tr:fe-lâ nukîmu lehum yevme'l-kıyâmeti veznâ, gloss:kıyamet günü onlar için hiçbir tartı kurmayız, source:18:105}. Zilzâl suresinde yer {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkarır, source:99:2}, ve zerre ağırlığındaki her iyilik görülür: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığında bir iyilik yaparsa onu görür, source:99:7}. Hafifliğin peşe takılmak olduğunu da Kur'an sahneler: Zuhruf suresinde Firavun {ar:فَٱسْتَخَفَّ قَوْمَهُۥ فَأَطَاعُوهُ, tr:fe'stehaffe kavmehû fe-etâûh, gloss:kavmini hafife aldı, onlar da ona uydular, source:43:54}; Rûm suresinde Allah Peygambere, kesin inanmayanların onu hafifletip yerinden oynatmamasını söyler {source:30:60}.

Kaynaklar: 101:6 ثَقُلَتْ ث ق ل B001; 101:6 ثَقُلَتْ ث ق ل B002; 101:6 ثَقُلَتْ ث ق ل B004; 101:6 ثَقُلَتْ ث ق ل B005; 101:6 مَوَٰزِينُهُۥ و ز ن B001; 101:6 مَوَٰزِينُهُۥ و ز ن B002; 101:6 مَوَٰزِينُهُۥ و ز ن B003; 101:8 مَوَٰزِينُهُۥ و ز ن B007; 101:8 خَفَّتْ خ ف ف B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B004; 101:8 خَفَّتْ خ ف ف B005; 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:5 ٱلْمَنفُوشِ ن ف ش B002; 101:5 ٱلْجِبَالُ ج ب ل B003; 101:9 هَاوِيَةٌ ه و ي B002; 101:1 ٱلْقَارِعَةُ ق ر ع B004

## Hoşnut yaşayış ve döşenmiş ev

Yedinci ayet, tartıları ağır geleni {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o, hoşnut bir yaşayış içindedir, source:101:7} diye anlatır. Îşe, yaşamaktır: {ar:العيش الحياة, tr:el-ayş el-hayât, gloss:ayş, hayattır, source:"ع ي ش,B001"}. Bu iki kelime dilde zaten birlikte anılır ve aynı sırada tersleri de sayılır: {ar:عيشة صالحة وراضية وصدق وسوء وضنك, tr:îşetun sâliha ve râdiye ve sıdk ve sû' ve dank, gloss:iyi, hoşnut, gerçek, kötü ve dar yaşayış, source:"ع ي ش,B001"}. Ayş aynı zamanda insanın onunla yaşadığı ve içinde yaşadığı şeydir: {ar:المطعم والمشرب وما يكون به الحياة, tr:el-mat'am ve'l-meşrab, gloss:yemek, içecek ve hayatın onunla sürdüğü şey, source:"ع ي ش,B002"}; {ar:كل شيء يعاش به أو فيه فهو معاش, tr:kullu şey'in yu'âşu bihî ev fîh, gloss:onunla ya da içinde yaşanan her şey maâştır, source:"ع ي ش,B002"}. Râdiye, öfkenin karşıtıdır, {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhid yedullu alâ hılâfi's-suht, gloss:hoşnutsuzluğun zıddını gösteren tek kök, source:"ر ض و,B001"}; bol hoşnutluktur {source:"ر ض و,B002"} ve iki taraflıdır: {ar:المراضاة من اثنين, tr:el-murâdât mini'sneyn, gloss:karşılıklı hoşnutluk iki kişi arasındadır, source:"ر ض و,B003"}. Ayetin tuhaf görünen yapısı, yaşayışın kendisinin hoşnut olması, bu iki taraflılığı hissettirir: yaşayış hem hoşnut eder hem hoşnut olur.

Surenin öbür kelimeleri bu yaşayışın evini döşer. Ferâş, döşenmiş yataktır ve kelimenin örnekleri cennetin döşekleridir: {ar:يقال للمفروش فرش وفراش؛ وفرش مرفوعة؛ فرش بطائنها من إستبرق, tr:ve furuşin merfû'a, gloss:serilene ferş ve firâş denir; yükseltilmiş döşekler; astarları kalın ipekten döşekler, source:"ف ر ش,B002"}. Mebsûs, evin içine serilmiş halılardır: {ar:وزرابي مبثوثة, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:"ب ث ث,B001"}. Ihn kökü, hazır yemeği ve içeceği, bir yerde yerleşik kalmayı da adlandırır: {ar:العاهن الطعام الحاضر والشراب الحاضر, tr:el-âhin et-taâmu'l-hâdır, gloss:âhin, hazır yemek ve hazır içecektir, source:"ع ه ن,B001"}; {ar:عهن بالمكان أقام به, tr:ahene bi'l-mekân, gloss:o yerde kaldı, yerleşti, source:"ع ه ن,B001"}. Ümm kökü de nimeti, iyi hali anlatır: {ar:الإمة النعمة, tr:el-imme en-ni'me, gloss:imme, nimettir, source:"ء م م,B010"}. Bu aile imgesinde, dördüncü ve beşinci ayetlerde dağılmayı anlatan kelimeler, başka bir okumada yedinci ayetin evinin eşyalarıdır.

Kur'an yedinci ayetin sözlerini aynen başka bir sahnede tekrarlar. Hâkka suresinde, kitabı sağından verilen {ar:فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ, tr:fe-emmâ men ûtiye kitâbehû bi-yemînih, gloss:kitabı sağından verilene gelince, source:69:19} sevinçle kitabını gösterir ve {ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ, tr:fe-huve fî îşetin râdiye, gloss:o hoşnut bir yaşayış içindedir, source:69:21}, {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:69:22}; meyveleri sarkmış, yakındır {source:69:23}. Aynı surede öbür taraf {ar:وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِشِمَالِهِۦ, tr:ve emmâ men ûtiye kitâbehû bi-şimâlih, gloss:kitabı solundan verilene gelince, source:69:25} diye açılır. Gâşiye suresinde yüzler {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdiye, gloss:çabalarından hoşnuttur, source:88:9}, ve onların halıları serilidir: {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:ve serilmiş halılar, source:88:16}; mebsûs kelimesi burada dördüncü ayetteki ile aynı kalıptadır. Fecr suresinde huzura ermiş can {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut olunmuş olarak dön, source:89:28} diye çağrılır; iki taraflı hoşnutluk burada iki kelimeyle söylenir. Hoşnut yaşayışın zıddı da Kur'an'dadır: Tâhâ suresinde Allah, zikrinden yüz çevirene {ar:فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:fe-inne lehû maîşeten dankâ, gloss:onun için dar bir geçim vardır, source:20:124} olduğunu söyler.

Kaynaklar: 101:7 عِيشَةٍ ع ي ش B001; 101:7 عِيشَةٍ ع ي ش B002; 101:7 رَّاضِيَةٍ ر ض و B001; 101:7 رَّاضِيَةٍ ر ض و B002; 101:7 رَّاضِيَةٍ ر ض و B003; 101:4 كَٱلْفَرَاشِ ف ر ش B002; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 كَٱلْعِهْنِ ع ه ن B001; 101:9 فَأُمُّهُۥ ء م م B010

## Anası: dipsiz çukur

Dokuzuncu ayet, tartıları hafif gelene bir ana verir: {ar:فَأُمُّهُۥ هَاوِيَةٌۭ, tr:fe-ummuhû hâviye, gloss:onun anası hâviyedir, source:101:9}. Ayetin anlamı, onun sığınağının ve varacağı yerin hâviye olduğudur. Ümm, besleyen ve büyütendir: {ar:فلانة تؤم فلانا أي تغذوه وتربيه, tr:fulânetun teummu fulânâ, gloss:filan kadın filanı besler ve büyütür, source:"ء م م,B001"}. Ümm aynı zamanda yanındakileri kendine toplayan her şeydir: {ar:كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما, tr:kullu şey'in yedummu ileyhi mâ sivâh, gloss:yanındakileri kendine katan her şeye Araplar ümm der, source:"ء م م,B002"}; {ar:كل شيء انضمت إليه أشياء فهو أم, tr:kullu şey'in indammet ileyhi eşyâ', gloss:başka şeylerin kendisine katıldığı her şey ümmdür, source:"ء م م,B002"}. Bir şeyin varlığının, büyümesinin ya da başlangıcının kaynağı olan her şey de böyle adlandırılır {source:"ء م م,B002"}.

Hâviye, dibine erişilemeyen her uçurumdur: {ar:الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة, tr:el-hâviye kullu mehvâtin lâ yudraku ka'ruhâ, gloss:hâviye, dibine erişilemeyen her çukurdur; huvve, derinleştirilmiş her çukurdur, source:"ه و ي,B002"}; düşmek, yukarıdan aşağı yuvarlanmaktır: {ar:هوى الشيء يهوي إذا خر من علو إلى سفل, tr:heve'ş-şey'u yehvî, gloss:şey yukarıdan aşağıya düştü, source:"ه و ي,B002"}. Kökün temelinde boşluk ile düşüş birdir: {ar:أصل صحيح يدل على خلو وسقوط, tr:aslun sahîh yedullu alâ hulüvvin ve sukût, gloss:boşluk ve düşüşü gösteren sağlam bir kök, source:"ه و ي,B001"}. Gökle yer arasındaki hava da, boş bir kalp de bu kökle anılır: {ar:الهَواء ما بين السماء والأرض وكل خال هواء, tr:el-hevâ' mâ beyne's-semâi ve'l-ard, gloss:hevâ, gökle yer arasındaki şeydir; her boş şey hevâdır, source:"ه و ي,B001"}; {ar:قلبه هَواء, tr:kalbuhû hevâ', gloss:kalbi bomboş, source:"ه و ي,B001"}. Düşmek ölmektir de: {ar:هوى فلان أي مات, tr:hevâ fulân, gloss:filan düştü, yani öldü, source:"ه و ي,B002"}; hâviye, cehennemin adlarından biridir {source:"ه و ي,B002"}.

Ümm ile hâviyeyi bir araya getiren bir deyim vardır: {ar:هوت أمه فهي هاوية أي ثاكلة, tr:hevet ummuhû fe-hiye hâviye, gloss:anası düştü, yani evladını yitirdi; o, hâviyedir, source:"ه و ي,B002"}. Arapçada bu söz bir beddua olarak kullanılır, "anası ağlasın" gibi {source:"memory"}. Böylece ayet iki sahneyi birden taşır. Biri: anası evladını yitirmiştir, çünkü o ölmüştür. Öbürü: çukur onun anasıdır ve bir ananın çocuğunu bağrına basması gibi onu içine alır. Çukur besleyen değil yutan bir anadır; toplayan ama bırakmayan. Karşısında yedinci ayetin adamı durur, onun bir hayatı, bir yaşayışı vardır {source:"ع ي ش,B001"}. Hayat ile evladını yitirmiş ana, ayetlerin karşıtlığını aile imgesinde de kurar.

Çukurun bir dibi yoktur. Dağın kökü, kazanların kayaya varıp durduğu anı adlandıran bir deyim taşır: {ar:أجبل القوم إذا حفروا فبلغوا المكان الصلب, tr:ecbele'l-kavm, gloss:topluluk kazdı ve sert yere vardı, source:"ج ب ل,B005"}. Dipsiz çukur bunun tersidir: duracak bir kaya yoktur, çünkü dağlar da yün olmuştur. On birinci ayetin hâmiyesi, bir kuyunun duvarını ören ağır taşları da adlandırır: {ar:الحامية الحجارة يطوى بها البئر, tr:el-hâmiye el-hıcâre yutvâ bihe'l-bi'r, gloss:hâmiye, kuyunun onlarla örüldüğü taşlardır, source:"ح م ي,B011"}; {ar:الحوامي عظام الحجارة وثقالها, tr:el-havâmî izâmu'l-hıcâre ve sikâluhâ, gloss:havâmî, taşların iri ve ağır olanlarıdır, source:"ح م ي,B011"}. Bu aile imgesinde çukurun duvarları ağır taştır, içine düşen ise hafif olandır.

Kur'an'da düşüş ve boşluk, bu kökün sahneleridir. Hac suresinde Allah, ona ortak koşanı {ar:فَكَأَنَّمَا خَرَّ مِنَ ٱلسَّمَآءِ فَتَخْطَفُهُ ٱلطَّيْرُ أَوْ تَهْوِى بِهِ ٱلرِّيحُ فِى مَكَانٍۢ سَحِيقٍۢ, tr:fe-ke-ennemâ harra mine's-semâi fe-tahtafuhu't-tayru ev tehvî bihi'r-rîhu fî mekânin sehîk, gloss:sanki gökten düşmüş, kuşlar onu kapıyor ya da rüzgâr onu uzak bir yere savuruyor, source:22:31} diye anlatır. İbrâhîm suresinde zalimler gözlerin donup kaldığı günde {source:14:42} anlatılır: {ar:وَأَفْـِٔدَتُهُمْ هَوَآءٌۭ, tr:ve ef'idetuhum hevâ', gloss:kalpleri bomboştur, source:14:43}. Tâhâ suresinde Allah İsrâiloğullarına {ar:وَمَن يَحْلِلْ عَلَيْهِ غَضَبِى فَقَدْ هَوَىٰ, tr:ve men yahlil aleyhi ğadabî fe-kad hevâ, gloss:kime gazabım inerse o düşmüştür, source:20:81} der; Necm suresinde altüst edilen kentler için {ar:وَٱلْمُؤْتَفِكَةَ أَهْوَىٰ, tr:ve'l-mu'tefikete ehvâ, gloss:altüst olanı da düşürdü, source:53:53} söylenir. Tevbe suresindeki sahne başka bir kökle kurulur ama aynı düşüşü gösterir: bina, çökecek bir yarın kenarına kurulmuştur, {ar:فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:fe'nhâra bihî fî nâri cehennem, gloss:onunla birlikte cehennem ateşine yıkılıp gitti, source:9:109}. Kâf suresinde dipsizlik bir konuşmaya dönüşür: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu" deriz, o da "daha var mı" der, source:50:30}. Nâziât suresinde Allah insanları ayırır, her birine bir sığınak verir: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:işte cehennem, sığınak odur, source:79:39} ve {ar:فَإِنَّ ٱلْجَنَّةَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cennete hiye'l-me'vâ, gloss:işte cennet, sığınak odur, source:79:41}; ikisinin arasında, cennete gidenin nefsini {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ani'l-hevâ, gloss:ve nefsini hevadan alıkoydu, source:79:40} diye anılması, hâviye ile aynı kökü taşır.

O gün insan anası da elinden bırakır. Hac suresinde kıyametin sarsıntısında {ar:تَذْهَلُ كُلُّ مُرْضِعَةٍ عَمَّآ أَرْضَعَتْ, tr:tezhelu kullu murdı'atin ammâ erda'at, gloss:her emziren, emzirdiğini unutur, source:22:2}; Abese suresinde, kulakları sağır eden ses geldiğinde {source:80:33}, {ar:يَوْمَ يَفِرُّ ٱلْمَرْءُ مِنْ أَخِيهِ, tr:yevme yefirru'l-mer'u min ahîh, gloss:kişinin kardeşinden kaçtığı gün, source:80:34}, {ar:وَأُمِّهِۦ وَأَبِيهِ, tr:ve ummihî ve ebîh, gloss:anasından ve babasından, source:80:35}. Mü'minûn suresi bunu, terazi ayetlerinin hemen öncesinde söyler: {ar:فَلَآ أَنسَابَ بَيْنَهُمْ يَوْمَئِذٍۢ وَلَا يَتَسَآءَلُونَ, tr:fe-lâ ensâbe beynehum yevmeizin ve lâ yetesâelûn, gloss:o gün aralarında soy bağı kalmaz, birbirlerini de sormazlar, source:23:101}. Gerçek ana çocuğunu bırakınca, geriye o kişiyi kucaklayan tek ana olarak çukur kalır.

Kaynaklar: 101:9 فَأُمُّهُۥ ء م م B001; 101:9 فَأُمُّهُۥ ء م م B002; 101:9 هَاوِيَةٌ ه و ي B001; 101:9 هَاوِيَةٌ ه و ي B002; 101:7 عِيشَةٍ ع ي ش B001; 101:5 ٱلْجِبَالُ ج ب ل B005; 101:11 حَامِيَةٌ ح م ي B011

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

