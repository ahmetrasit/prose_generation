Focus: 101:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_3/D.r13/context.md =====
# 101:3 — focus

وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ

Anchor translation (canonical reading, reference only):

Ve çarpan felaketin ne olduğunu sana ne bildirdi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَمَآ | مَا |  | CONJ;INTG |
| 2 | أَدْرَىٰكَ | أَدْرَىٰ | د ر ي | V;PRON |
| 3 | مَا | مَا |  | INTG |
| 4 | ٱلْقَارِعَةُ | قَارِعَة | ق ر ع | DET;N |


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
- 101:3 ◀ focus وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## د ر ي (root_000473) — identity root of أَدْرَىٰكَ (w2)

- **B001** bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme — bir şeyi bilmek veya ondan haberdar olmak · birine bildirmek, onun bilmesini sağlamak · bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi · bilmiyorum
  دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)
- **B002** saldırı amacıyla bir yer ya da kişiyi seçmek [kalıp] — bir yeri baskın veya saldırı için seçmek
  أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)
- **B003** avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak — avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan · avı gizlenip aldatarak atış menziline getirmek · hileyle kandırmak
  الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)
- **B004** sivri uç ve bundan ad alan saç düzeltme aracı — sivri boynuz; saçı düzeltmeye yarayan sivri araç · saçı ayırıp düzeltmeye yarayan şiş biçimli araç · saçını tarayıp düzeltmek
  الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)
- **B005** saplama ve atış alıştırma hedefi — üzerinde saplama alıştırması yapılan hedef
  الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)
- **B006** insanlarla yumuşak ve incelikli geçinmek [kalıp] — insanlara karşı yumuşak ve uzlaştırıcı davranmak
  مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)

## ق ر ع (root_001219) — identity root of ٱلْقَارِعَةُ (w4)

- **B001** bir şeye vurmak veya çarpmak — vurmak, çarpmak veya vurarak uyarmak · kaptakini sonuna kadar içince kabın alnına değmesi · hayvana vurmak için kullanılan değnek · taş kırmaya yarayan balta benzeri araç · ateş yakmak için kullanılan çakma aracı
  القاف والراء والعين معظم الباب ضرب الشيء (maqayis)؛ كل شيء ضربته فقد قرعته (ayn)؛ قرعت الباب أقرعه قرعا (sihah)؛ قرع راحلته أي ضربها بسوطه (tahdhib)؛ القرع ضرب شيء على شيء (mufradat)
- **B002** kılıçlarla karşılıklı çarpışmak — savaşta kılıçlarla karşılıklı dövüşme · dövüşte karşı karşıya gelen rakip
  مقارعة الأبطال قرع بعضهم بعضا (maqayis)؛ المقارعة والقراع المضاربة بالسيف في الحرب (ayn)؛ قريعك الذي يقارعك (sihah)؛ القراع والمقارعة المضاربة بالسيوف (tahdhib)
- **B003** damızlık erkeğin dişiyle çiftleşmesi ve dişinin erkeği istemesi — erkek hayvanın dişiye çiftleşmek için çıkması · çiftleşme için ayrılmış damızlık erkek · dişi deve veya sığırın çiftleşmek istemesi
  القريع الفحل لأنه يقرع الناقة (maqayis)؛ القريع من الإبل الفحل (ayn)؛ قرع الفحل الناقة يقرعها قرعا وقراعا (sihah)؛ استقرعت الناقة إذا اشتهت الضراب (tahdhib)
- **B004** kura çekmek ve kurayla paylaştırmak — kura veya kurada çıkan pay · aralarında kura çektirmek · kura çekerek seçmek veya paylaştırmak
  الإقراع والمقارعة هي المساهمة (maqayis)؛ أقرع القوم وتقارعوا بينهم والاسم القرعة (ayn)؛ أقرعت بينهم من القرعة واقترعوا وتقارعوا بمعنى (sihah)؛ أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه (tahdhib)
- **B005** sarsıcı büyük felaket veya dünyanın sonundaki hesap günü — büyük felaket veya dünyanın sonundaki hesap günü · Kuran'dan korkuya karşı okunan koruyucu bölümler
  القارعة الشديدة من شدائد الدهر والقارعة القيامة (maqayis)؛ القارعة القيامة والقارعة الشدة (ayn)؛ القارعة الشديدة من شدائد الدهر وهي الداهية (sihah)؛ النازلة الشديدة تنزل عليهم بأمر عظيم (tahdhib)؛ القارعة ما القارعة (mufradat)
- **B006** öğütle yola gelmek; durdurmak veya azarlamak — öğüt dinleyip vazgeçmek · doğru olana geri dönüp boyun eğmek · alıkoymak ve caydırmak · sertçe azarlama ve kınama · pişmanlıktan dişine vurmak
  رجل قرع إذا كان يقبل مشورة المشير (maqayis)؛ أقرعت إلى الحق إقراعا رجعت (maqayis)؛ فلان لا يقرع إقراعا إذا كان لا يقبل المشورة والنصيحة (sihah)؛ التقريع التعنيف (sihah)؛ فلان لا يقرع أي لا يرتدع (tahdhib)؛ أقرعته إذا كففته (tahdhib)
- **B007** seçilmiş önder veya bir şeyin en iyi bölümü; en iyisini vermek — güvenilen önder veya başkan · seçilmiş kişi veya önder · malın en iyi ve seçkin bölümü · evin sıcak veya soğukta en iyi yeri · ona malının en iyi bölümünü vermek
  القريع وهو السيد سمى بذلك لأنه يعول عليه في الأمور (maqayis)؛ أقرع فلان فلانا أعطاه خير ماله وخيار المال قرعته (maqayis)؛ القريعة وهو خير بيت في الربع (maqayis)؛ المقروع المختار للفحلة والمقروع السيد (sihah)؛ قريعة البيت خير موضع فيه (tahdhib)؛ القريعة والقرعة خيار المال (tahdhib)
- **B008** saç ya da örtü kaybı; bir yerin boş veya bitkisiz kalması — bir hastalık yüzünden saçların dökülmesi · saçı hastalık nedeniyle dökülmüş; kel · deri veya tüy hastalığına tutulmuş yavru deve · avlu veya hayvan barınağının boş kalması · bitki yetiştirmeyen veya otlatılıp çıplak kalmış arazi · açıkta kalan cinsel bölge · başında tüy bulunmayan iri yılan
  مما شذ عن هذا الأصل القرع وفصيل مقرع والقرع أيضا ذهاب الشعر من الرأس (maqayis)؛ القرع ذهاب شعر الرأس من داء (ayn)؛ الأقرع الذي ذهب شعر رأسه من آفة (sihah)؛ قرع الفناء إذا خلا من الغاشية (sihah)؛ أرض قرعة لا تنبت شيئا (tahdhib)؛ أصبحت الرياض قرعا قد جردتها المواشي (tahdhib)
- **B009** kabak meyvesi — kabak meyvesi
  القرع حمل اليقطين الواحدة قرعة (ayn)؛ القرع حمل اليقطين الواحدة قرعة (sihah)؛ القرع حمل اليقطين (tahdhib)
- **B010** yolun açık üst kesimi veya evin önü — yolun açık veya üst kesimi; evin önündeki açık alan
  قارعة الدار ساحتها وقارعة الطريق أعلاه (sihah)؛ قرعاء الدار ساحتها (tahdhib)؛ قارعة الطريق ساحتها وقارعة الطريق أعلاه (tahdhib)
- **B011** sert ve dayanıklı; kazınıp pürüzsüzleştirilmiş — sert ve dayanıklı · çakılla ovulmuş kap veya kabuğu soyulmuş dal · sertleşmiş toynak veya işkembe
  القراع الصلب الشديد (sihah)؛ ترس أقرع إذا كان صلبا وهو القراع أيضا (tahdhib)؛ قدح أقرع وهو الذي حك بالحصى (tahdhib)؛ مكان أقرع شديد صلب (tahdhib)
- **B012** yiyecek veya hurma konan torba ya da kap — yiyecek koymaya yarayan küçük veya geniş torba · hurma toplamak için kullanılan kap
  القرعة الجراب الواسع يلقى فيه الطعام (tahdhib)؛ القرعة الجراب الصغير وجمعها قرع (tahdhib)؛ المقرع وعاء يجبى فيه التمر (tahdhib)؛ قرع فلان في مقرعه كله السقاء والزق (tahdhib)

## ECHO د ر ر (root_000469) — for أَدْرَىٰكَ (w2): withheld observed target; not identity

- **B001** bir kaynaktan bolca çıkma veya bol ürün verme — sütün memeden çıkıp akması · süt · bol sütlü dişi deve · bulutun yağmur boşaltması · bol yağmur getiren · gözünden yaş akması · damarların kanla dolması · Ne güzel iş ve iyilik! · İyiliği artmasın! · vergi gelirinin artması · pazarın canlanması · dişi keçilerin teke istemesi · sütün bolluğu veya akışı
  الدر در اللبن (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در السحاب بالمطر ودرت السماء وسحابة مدرار (maqayis;jamhara;sihah;tahdhib;mufradat)؛ لله دره ولا در دره أي خيره أو عمله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در الخراج وحلوبة المسلمين وللسوق درة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ استدرت المعزى إذا أرادت الفحل (maqayis;sihah;tahdhib;mufradat)
- **B002** hızlı, güçlü ve akıcı koşma — çok hızlı koşan binek hayvanı · atın hızlı ve rahat koşması · bacakta güçlü koşma yetisi · atın tırıs sırasında ön ayağını kaldırıp indirdiği yürüyüş biçimi
  الدرير من الدواب الشديد العدو السريعة (maqayis)؛ در الفرس دريرا إذا عدا عدوا شديدا سهلا (jamhara)؛ فرس درير أي سريع (sihah)؛ در الفرس درة فهو درير إذا أسرع في عدوه والإدرار في الخيل (tahdhib)
- **B003** gevşekçe sallanma veya tekrar tekrar gidip gelme — diş yuvaları; kimi kullanımda dil ucu · çocuğun bir şeyi ağzında çevirip çiğnemesi · sallanıp oynamak · dişleri dökülüp diş yuvaları görünmek · gereksiz yere gidip gelen kimse
  الدردر منابت أسنان الصبي ومن تدردرت اللحمة إذا اضطربت ودردر الصبي الشيء إذا لاكه (maqayis)؛ الدردر مغارز أسنان الصبي ودردر الصبي البسرة لاكها (sihah)؛ تدردر أي تمرمر وترجرج والدردر مغرز السن وطرف اللسان والدردرى الذي يذهب ويجيء في غير حاجة (tahdhib)
- **B004** doğrultu, yön veya karşı karşıya hizalanma — yolun doğrultusu veya güzergâhı · rüzgârın esiş yönü · tam karşında veya hizanda
  درر الريح مهبها ودرر الطريق قصده (maqayis)؛ هما على درر واحد ونحن على درر الطريق ودرر الريح مهبها (sihah)؛ فلان دررك أي قبالتك وعلى درر الطريق أي مدرجته وداري بدرر دارك أي بحذائها (tahdhib)
- **B005** iri inci; inci gibi beyaz ve parlak yıldız — iri inciler veya inci topluluğu · iri inci; tek bir inci · inci gibi beyaz ve parlak yıldız
  الدر كبار اللؤلؤ والكوكب الدري الثاقب المضيء (maqayis)؛ الدرة ما عظم من اللؤلؤ (jamhara)؛ الدرة اللؤلؤة والكوكب الدري الثاقب المضيء نسب إلى الدر لبياضه (sihah)؛ الدر العظام من اللؤلؤ والكوكب الدري الثاقب المضيء (tahdhib)
- **B006** özellikle yöneticinin kullandığı vurma değneği — özellikle yöneticinin kullandığı vurma değneği
  الدرة التي يضرب بها عربية معروفة (jamhara)؛ الدرة التي يضرب بها (sihah)؛ الدرة درة السلطان التي يضرب بها (tahdhib)
- **B007** ipliği sıkı bükmek için iği döndürme — ipliği sıkı bükmek için iği veya dönen parçasını çevirmek
  أدرت المرأة المغزل إذا فتلته فتلا شديدا فهي مدر والمغزل مدر (jamhara)؛ أدرت الغزالة درارتها إذا أدارتها لتستحكم قوة ما تغزله (tahdhib)
- **B008** gemiyi tehlikeye atan çalkantılı deniz girdabı — girdap; gemiyi tehlikeye atan çalkantılı deniz yeri
  الدردور الماء الذي يدور ويخاف فيه الغرق (sihah)؛ الدردور موضع من البحر يجيش ماؤه وقلما تسلم السفينة منه (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:3, and ## Buluşmalar) =====
## Kapı çalınır, içeriden soru gelir

Aynı fiil kapının çalınmasını da anlatır: {ar:قرعت الباب أقرعه قرعا, tr:kara'tu'l-bâbe, gloss:kapıyı çaldım, source:"ق ر ع,B001"}. Kelime, evin önündeki açık alanın, yani vuruşun indiği yerin adıdır da: {ar:قارعة الدار ساحتها, tr:kâriatu'd-dâr sâhatuhâ, gloss:evin kâriası, onun avlusudur, source:"ق ر ع,B010"}. Bu imgeyle surenin ilk üç ayeti bir kapı sahnesi gibi işler. Önce vuruş gelir: tek kelime. Sonra içeriden bir ses sorar: {ar:مَا ٱلْقَارِعَةُ, tr:me'l-kâria, gloss:nedir o çarpan, source:101:2}. Ardından soru katlanır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ, tr:ve mâ edrâke me'l-kâria, gloss:o çarpanın ne olduğunu sana ne bildirdi, source:101:3}. Kapıyı çalanın kim olduğu söylenmez; cevap bir isim olarak değil, dördüncü ve beşinci ayetlerdeki sahne olarak gelir.

"Bildirmek" fiilinin kökü, kişinin kendi çabasıyla vardığı bir bilgiyi anlatır: {ar:الدراية المعرفة المدركة بضرب من الحيل, tr:ed-dirâye el-ma'rifetu'l-mudreke, gloss:dirâye, bir tür çabayla ulaşılan bilgidir, source:"د ر ي,B001"}; aynı kökte bilmek ile bildirilmek yan yanadır: {ar:دريته ودريت به أي علمت به وأدريته أي أعلمته, tr:dereytuhû... ve edreytuhû, gloss:onu bildim; ona bildirdim, source:"د ر ي,B001"}. Üçüncü ayetteki soru, bu bilginin çabayla ulaşılamayacağını, ancak dışarıdan verilebileceğini hissettirir. Dördüncü ayetin mebsûs kelimesi bu imgeye bir anlam daha katar: aynı kök, haberin yayılmasını ve gizlinin açığa vurulmasını da adlandırır: {ar:أبثثتك سري؛ أظهرته لك, tr:ebsestuke sirrî, gloss:sırrımı sana açtım, source:"ب ث ث,B002"}. Sorunun cevabı, her şeyin açığa saçıldığı bir sahne olarak gelir.

Kelimenin bir anlamı daha, kapıyı çalmanın amacını gösterir: uyarı, onu dinleyeni geri döndürür; dinlemeyen için ise azardır. {ar:أقرعت إلى الحق إقراعا رجعت, tr:akra'tu ile'l-hakk, gloss:hakka döndüm, source:"ق ر ع,B006"}; {ar:فلان لا يقرع أي لا يرتدع, tr:fulânun lâ yukra', gloss:filan kişi uyarıdan geri durmaz, source:"ق ر ع,B006"}. Sure bir vuruşla açılır, çünkü vuruş içerideki kişiyi uyandırmak içindir.

Onuncu ayette aynı soru kalıbı geri döner, bu kez çukur için: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}. Bu sefer cevap bekletilmez; on birinci ayet tek bir ifadeyle karşılık verir: {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Surenin başındaki soru bir sahneyle, sonundaki soru bir ateşle cevaplanır.

Kur'an bu soru kalıbını birçok yerde kullanır. Hâkka suresi aynı üç adımla açılır: {ar:ٱلْحَآقَّةُ, tr:el-hâkka, gloss:gerçekleşecek olan, source:69:1}, {ar:مَا ٱلْحَآقَّةُ, tr:me'l-hâkka, gloss:nedir o gerçekleşecek olan, source:69:2}, {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحَآقَّةُ, tr:ve mâ edrâke me'l-hâkka, gloss:onun ne olduğunu sana ne bildirdi, source:69:3}; hemen ardından Semûd ile Âd'ın kâriayı yalanladığı anlatılır {source:69:4}. Hümeze suresinde Allah, kusur arayanın {ar:لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ, tr:le-yunbezenne fi'l-hutame, gloss:o mutlaka ezip kırana atılacak, source:104:4} olduğunu söyler, sonra sorar: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:ezip kıranın ne olduğunu sana ne bildirdi, source:104:5} ve cevap yine bir ateştir: {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nâru'llâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Müddessir suresinde {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sekar, gloss:sekarın ne olduğunu sana ne bildirdi, source:74:27} sorusuna {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ tezer, gloss:ne bırakır ne geri koyar, source:74:28} diye cevap verilir. İnfitâr suresinde soru iki kez sorulur, {ar:ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:summe mâ edrâke mâ yevmu'd-dîn, gloss:sonra, ceza gününün ne olduğunu sana ne bildirdi, source:82:18}, ve cevap {ar:يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا, tr:yevme lâ temliku nefsun li-nefsin şey'â, gloss:hiçbir canın bir başka can için hiçbir şeye güç yetiremediği gün, source:82:19} olur. Târık suresinde gece gelen yolcu da aynı soruyla anılır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلطَّارِقُ, tr:ve mâ edrâke me't-târık, gloss:gece gelenin ne olduğunu sana ne bildirdi, source:86:2}, cevap {ar:ٱلنَّجْمُ ٱلثَّاقِبُ, tr:en-necmu's-sâkıb, gloss:delip geçen yıldız, source:86:3}. Arapçada târık, gece kapıyı çalarak gelen kişidir {source:"memory"}; kökü kâriadan farklıdır, ama sahne aynı türden bir kapı vuruşudur.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B010; 101:1 ٱلْقَارِعَةُ ق ر ع B006; 101:3 أَدْرَىٰكَ د ر ي B001; 101:10 أَدْرَىٰكَ د ر ي B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B002

## Savaş günü

Araplar savaşlarına "gün" adını verirdi. Aynı kökte gün, olup biten olayın kendisidir: {ar:الأيام في معنى الوقائع, tr:el-eyyâm fî ma'ne'l-vekâi', gloss:günler, vakalar, çarpışmalar anlamında, source:"ي و م,B003"}. Bu tanım dördüncü ayetin fiilini de içine alır: {ar:اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت, tr:el-yevm: el-kevn, el-kâine, gloss:gün, olan şey, inip meydana gelen olaydır, source:"ي و م,B003"}. Fiilin kendi kökünde ise {ar:الكون الحدث يكون بين الناس, tr:el-kevnu el-hadesu yekûnu beyne'n-nâs, gloss:kevn, insanlar arasında olan olaydır, source:"ك و ن,B001"} denir. Dördüncü ayetin {ar:يَوْمَ يَكُونُ ٱلنَّاسُ, tr:yevme yekûnu'n-nâs, gloss:insanların ... olacağı gün, source:101:4} ifadesi, bu tanımın kelimelerini taşır.

Kâria kelimesinin bir kolu da kılıç çarpışmasıdır: {ar:المقارعة والقراع المضاربة بالسيف في الحرب, tr:el-mukâra'a ve'l-kırâ', gloss:savaşta kılıçla karşılıklı vuruşmak, source:"ق ر ع,B002"}. Surenin öbür kelimeleri, aynı meydanın birer parçasını adlandırır. Mebsûs atların akına dağıtılmasıdır: {ar:بثوا الخيل, tr:besse'l-hayl, gloss:atları yaydılar, source:"ب ث ث,B001"}. "Bildirmek" fiilinin bir kalıp kullanımı, bir yerin baskın hedefi olarak seçilmesini anlatır: {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fulân mekâne kezâ, gloss:filan oğulları falan yeri baskın için hedef aldı, source:"د ر ي,B002"}. Sekizinci ayetin "hafif geldi" fiili, obanın aceleyle göçmesini de anlatır: {ar:خف القوم إذا ارتحلوا مسرعين, tr:haffe'l-kavm, gloss:topluluk aceleyle göçtü, source:"خ ف ف,B002"}. On birinci ayetin ateşi, kabile içinde parlayan düşmanlığın da adıdır: {ar:النائرة الكائنة تقع بين القوم, tr:en-nâira el-kâine, gloss:nâira, topluluk arasında patlak veren olaydır, source:"ن و ر,B007"}; burada yine kâine kelimesi, yani gün ve olmak kelimelerinin kökü geçer. Hâmiye ise savaşta ailesini koruyanı {ar:حمى أهله في القتال حماية, tr:hamâ ehlehû fi'l-kıtâl, gloss:savaşta ailesini korudu, source:"ح م ي,B002"} ve öfkesi kızışan savaşçıyı {ar:حميت عليه غضبت, tr:hamîtu aleyh, gloss:ona öfkelendim, source:"ح م ي,B003"} anlatır.

Bu imge, düz bir anlatımın veremeyeceği bir şeyi duyurur: kıyamet uzak bir tarih değil, bir topluluğun başına gelen bir gündür, tıpkı tarihte anılan savaş günleri gibi. Kelimenin bir kalıp kullanımı da bunu Kur'an'a bağlar: {ar:وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, yani Âd'a, Semûd'a ve başkalarına inen azabı, source:"ي و م,B004"}. İbrâhîm suresinde Allah, Mûsâ'yı kavmine gönderirken ona {ar:وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, source:14:5} diye emreder; birkaç ayet sonra Mûsâ, kavmine Nûh, Âd ve Semûd kavimlerinin haberini hatırlatır {source:14:9}. Hâkka suresinde ise kâriayı yalanlayanlar tam da bu iki kavimdir {source:69:4}: {ar:فَأَمَّا ثَمُودُ فَأُهْلِكُوا۟ بِٱلطَّاغِيَةِ, tr:fe-emmâ Semûdu fe-uhlikû bi't-tâğiye, gloss:Semûd, haddi aşan bir sarsıntıyla yok edildi, source:69:5}, {ar:وَأَمَّا عَادٌۭ فَأُهْلِكُوا۟ بِرِيحٍۢ صَرْصَرٍ عَاتِيَةٍۢ, tr:ve emmâ Âdun fe-uhlikû bi-rîhin sarsarin âtiye, gloss:Âd ise azgın, uğuldayan bir rüzgârla yok edildi, source:69:6}. Bu iki ayetin "fe-emmâ ... ve emmâ" kalıbı, Kâria suresinin altıncı ve sekizinci ayetlerinde tekrarlanır.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B002; 101:4 يَوْمَ ي و م B003; 101:4 يَوْمَ ي و م B004; 101:4 يَكُونُ ك و ن B001; 101:5 وَتَكُونُ ك و ن B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:3 أَدْرَىٰكَ د ر ي B002; 101:10 أَدْرَىٰكَ د ر ي B002; 101:8 خَفَّتْ خ ف ف B002; 101:11 نَارٌ ن و ر B007; 101:11 حَامِيَةٌ ح م ي B002; 101:11 حَامِيَةٌ ح م ي B003

## Işığa düşen pervaneler

Dördüncü ayetin benzetmesi {ar:كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:ke'l-ferâşi'l-mebsûs, gloss:saçılmış pervaneler gibi, source:101:4} ifadesidir. Ferâş, ışığı arayarak uçan, sonunda kandile ya da ateşe düşen küçük kanatlı böcektir: {ar:الفراش التي تطير طالبة للضوء, tr:el-ferâş elletî tatîru tâlibeten li'd-dav', gloss:ferâş, ışığı arayarak uçan böceklerdir, source:"ف ر ش,B005"}; {ar:الفراشة التي تطير وتهافت في السراج, tr:el-ferâşe elletî tatîru ve tehâfetu fi's-sirâc, gloss:uçup kandile üşüşerek düşen pervane, source:"ف ر ش,B005"}; {ar:الفراش ما تراه كصغار البق يتهافت في النار, tr:yetehâfetu fi'n-nâr, gloss:küçük sinekler gibi ateşe üşüşüp düşenler, source:"ف ر ش,B005"}. Aynı kök, yere yakın kanat çırpışı da anlatır: {ar:تفرش الطائر إذا قرب من الأرض ورفرف بجناحه, tr:teferreşe't-tâir, gloss:kuş yere yaklaşıp kanat çırptı, source:"ف ر ش,B006"}. Mebsûs, sürünün dağılmasıdır; aynı fiil çekirgelerin yayılması için de kullanılır: {ar:انبث الجراد, tr:inbesse'l-cerâd, gloss:çekirgeler yayıldı, source:"ب ث ث,B001"}.

Benzetmenin açık anlamı, insanların dağınık, şaşkın ve sayısız oluşudur. Bu yüzeyin yanında, kelimenin içinden bir sahne duyulur: bir ateş vardır, sürü ona doğru uçar ve içine düşer. Surenin son kelimesi de nârdır, ateş. Ateşin kökü ışıkla birdir ve bu kök, aynı anda parlaklığı ve titrek, kararsız hareketi anlatır: {ar:النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة, tr:en-nûr ve'n-nâr, gloss:nur ve nar bu adı ışık saçtıkları ve titrek, hızlı hareketli oldukları için aldılar, source:"ن و ر,B002"}. Pervanenin çırpınışı ile alevin titreyişi aynı harekettir. Aynı kökte uzaktan görülen ateşe yönelmek de vardır: {ar:تنورت نارا قصدت إليها, tr:tenevvertu nâran, gloss:bir ateşe yöneldim, source:"ن و ر,B003"}.

Surenin kelimeleri bu yolculuğun adımlarını sırayla verir. Dördüncü ayetin {ar:ٱلنَّاسُ, tr:en-nâs, gloss:insanlar, source:101:4} kelimesi, uzaktan bir ateşi fark etmek anlamındaki fiille birlikte anılan kökle ilişkilendirilir: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan bir ateş gördü, source:"ء ن س,B002"}. Dokuzuncu ayetin {ar:فَأُمُّهُۥ, tr:fe-ummuhû, gloss:onun anası, source:101:9} kelimesinin kökü, bir hedefe doğru yönelmeyi de anlatır: {ar:الأم القصد المستقيم وهو التوجه نحو مقصود, tr:el-emm el-kasdu'l-mustakîm, gloss:emm, bir hedefe doğru dosdoğru yönelmektir, source:"ء م م,B012"}. Hâviye kelimesinin kökü, bir topluluğun birbiri ardınca çukura düşüşünü anlatır: {ar:تهاوى القوم في المهواة سقط بعضهم في إثر بعض, tr:tehâve'l-kavmu fi'l-mehvât, gloss:topluluk çukura birbiri ardınca düştü, source:"ه و ي,B002"}; pervanelerin birer birer kandile düşüşü gibi. On birinci ayetin hâmiyesi ise sürünün vardığı yerin sıcaklığıdır: {ar:حمي الشيء يحمى حميا إذا سخن, tr:hamiye'ş-şey', gloss:şey ısındı, source:"ح م ي,B001"}. Işık, sürü, yöneliş, düşüş ve sıcaklık tek bir sahnede birleşir. Ateşin kökü bunun tersini de adlandırır, ürküp kaçmayı: {ar:النوار النفار, tr:en-nevâr en-nifâr, gloss:nevâr, ürküp kaçmaktır, source:"ن و ر,B006"}. Bir canlının ateş karşısında yapması gereken budur; pervanenin yaptığı ise tam tersidir.

Aynı türden bir cezbetme sahnesi avcılıkta da vardır. "Bildirmek" fiilinin kökü, avcının avı alıştırmak için diktiği deveyi adlandırır: {ar:الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد, tr:ed-diriyye, gloss:dirye, avın alışması için avcının diktiği dişi devedir, source:"د ر ي,B003"}; avcı onun arkasına saklanır ve görünmeden yaklaşır: {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytu's-sayd... ve dereytuhû hateltuh, gloss:avın nerede olduğuna baktım, henüz görmeden; ve onu pusuyla avladım, source:"د ر ي,B003"}. Aynı kökte mızrak talimi için dikilen halka da hedef olarak anılır {source:"د ر ي,B005"}. İnsanların kökü burada iki karşıt hali verir: ürkmeyen, alışmış hal, {ar:الأنس أنس الإنسان بالشيء إذا لم يستوحش منه, tr:el-uns, gloss:üns, insanın bir şeye ürkmeden alışmasıdır, source:"ء ن س,B003"}, ve bir şeyden kuşkulanınca etrafa bakınmak, {ar:الاستئناس النظر وأحس بما رابه, tr:el-isti'nâs, gloss:bakınmak ve kuşkulandığı şeyi sezmek, source:"ء ن س,B002"}. Mebsûs, avcının köpeklerini salmasıdır, {ar:بث الصياد كلابه, tr:bessa's-sayyâdu kilâbeh, gloss:avcı köpeklerini saldı, source:"ب ث ث,B001"}, hâviye ise kartalın avına pike yapması: {ar:هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء, tr:hevet el-ukâb, gloss:kartal pike yaptı; avını kollayınca ona daldı denir, source:"ه و ي,B003"}. Işık pervaneyi nasıl çekiyorsa, tuzak da avı öyle alıştırır. Üçüncü ve onuncu ayetteki "sana ne bildirdi" sorusu, bu aile imgesinde görünmeden yaklaşanın kökünde durur.

Kur'an'da ateşe yönelen insan sahnesi, bu imgenin tersini gösterir. Tâhâ suresinde Mûsâ, ailesiyle yolculuk ederken bir ateş görür: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran le'allî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Kasas suresi aynı sahneyi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-Tûri nârâ, gloss:Tûr tarafından bir ateş gördü, source:28:29} diye anlatır; Neml suresinde Mûsâ ateşten bir haber ya da ısınmak için bir kor getirmeyi umar {source:27:7}. Mûsâ'nın vardığı ateş yol gösterir; pervanenin vardığı ateş yakar. Bakara suresinde Allah, münafıkları ateş yakan birine benzetir: {ar:كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ, tr:ke-meseli'llezi'stevkade nâran fe-lemmâ edâet mâ havlehû zeheba'llâhu bi-nûrihim, gloss:ateş yakan biri gibi; ateş çevresini aydınlatınca Allah onların ışığını götürdü, source:2:17}; ışık ile ateşin aynı kökten oluşu orada da sahnenin kendisidir. Kamer suresinde Allah, insanların kabirlerden çıkışını {ar:كَأَنَّهُمْ جَرَادٌۭ مُّنتَشِرٌۭ, tr:ke-ennehum cerâdun munteşir, gloss:yayılmış çekirgeler gibi, source:54:7} diye anlatır; Meâric suresinde ise {ar:كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ, tr:ke-ennehum ilâ nusubin yûfidûn, gloss:sanki dikili bir hedefe koşuşuyorlarmış gibi, source:70:43}. Hedefe koşan, birbiri ardınca düşen sürü, dördüncü ve dokuzuncu ayetlerin aile imgesinde de duyulur.

Kaynaklar: 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:4 كَٱلْفَرَاشِ ف ر ش B006; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:4 ٱلنَّاسُ ء ن س B002; 101:4 ٱلنَّاسُ ء ن س B003; 101:9 فَأُمُّهُۥ ء م م B012; 101:9 هَاوِيَةٌ ه و ي B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:11 نَارٌ ن و ر B002; 101:11 نَارٌ ن و ر B003; 101:11 نَارٌ ن و ر B006; 101:11 حَامِيَةٌ ح م ي B001; 101:3 أَدْرَىٰكَ د ر ي B003; 101:3 أَدْرَىٰكَ د ر ي B005; 101:10 أَدْرَىٰكَ د ر ي B003

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

