Focus: 88:10. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_10/D.r13/context.md =====
# 88:10 — focus

فِى جَنَّةٍ عَالِيَةٍۢ

Anchor translation (canonical reading, reference only):

Yüksek bir bahçededir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فِى | فِى |  | P |
| 2 | جَنَّةٍ | جَنَّة | ج ن ن | N |
| 3 | عَالِيَةٍ | عَالِيَة | ع ل و | ADJ |


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
- 88:10 ◀ focus فِى جَنَّةٍ عَالِيَةٍۢ
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
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_10/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ن ن (root_000266) — identity root of جَنَّةٍ (w2)

- **B001** örtme ve duyulardan gizleme — örtmek; gizleyecek bir örtü sağlamak; içinde saklamak · bir şeyin arkasına gizlenmek · insanı örten giysi veya örtü
  الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)
- **B002** gecenin karartıp örtmesi — gecenin kararıp üzerini örtmesi · gecenin koyu karanlığı ve nesneleri örtmesi
  جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)
- **B003** zemini ağaçlarla örtülü bahçe — zemini ağaçlarla örtülü bahçe veya koruluk
  الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)
- **B004** ölüm sonrası gizli nimetler yurdu — ölüm sonrası ödül ve gizli nimetler yurdu
  الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)
- **B005** gözle görülmeyen ruhani varlıklar topluluğu — gözle görülmeyen ruhani varlıklar · görünmeyen varlıkların atası veya bir bireyi · görünmeyen ruhani varlıkların topluluğu · görünmeyen ruhani varlıkların çok bulunduğu yer
  الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)
- **B006** aklı örten akıl yitimi — aklını yitirmek; aklını yitirmiş duruma getirmek · akıl yitimi; benlik ile akıl arasındaki engel · aklını yitirmiş gibi davranmak
  الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)
- **B007** ana rahmindeki doğmamış çocuk — ana rahmindeki doğmamış çocuk · rahminde çocuk taşımak; çocuğun rahimde saklı kalması
  الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)
- **B008** koruyucu siper veya savaş donanımı — koruyucu örtü, siper veya savaş donanımı · kalkan
  المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)
- **B009** ölüyü örtüp gömme — ölüyü örtmek ve gömmek · gömüt; ölü örtüsü; gömülmüş kişi
  الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)
- **B010** duyulardan saklı yürek ve gizli yön — yürek veya yüreğin saklı iç yönü · gizli iş veya görünmeyen yön
  الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)
- **B011** bitkinin güçlenip boylanması ve sıklaşması — bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması · uzun ağaç; bol otlu ve henüz otlanmamış arazi
  جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)
- **B012** yılan, özellikle beyaz bir tür — yılan, beyaz yılan veya belirli bir yılan türü
  الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)
- **B013** halkın büyük kitlesi — insanların çoğunluğu veya halkın büyük kitlesi
  جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)
- **B014** bir şeyin ilk ve yeni dönemi — gençliğin, çocukluğun veya bir dönemin ilk başlangıcı
  كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)
- **B015** uçuş sırasında çoğalan sinek vızıltısı — sineğin vızıltısının veya sesinin çoğalması · böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması
  جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)
- **B016** göğüs kemikleri ve kaburga uçları — göğüs kemikleri veya kaburgaların göğse yakın uçları
  الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)
- **B017** içine girilip saklanılan yer — saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı
  المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)

## ع ل و (root_001042) — identity root of عَالِيَةٍ (w3)

- **B001** yukarı yükselme ve yüksekte olma — yukarı olma; aşağı karşıtı yükseklik · bir yerde yükselmek · günün yükselmesi · yükselip uzaklaşmak
  أصل واحد يدل على السمو والارتفاع (maqayis)؛ العلو أصل البناء (ayn)؛ علا في المكان يعلو علوا (sihah)؛ العلو ضد السفل والعلو الارتفاع (mufradat)
- **B002** saygınlıkta yüksek mevki — saygınlık ve yüksek mevki · değeri yüksek kimse veya nitelik · en üstün ve en yüksek değerde olan · saygın ve yüksek mevki sahibi · toplumun seçkinleri · kazanılmış yüksek onur dereceleri
  العلاء فالرفعة (maqayis;ayn)؛ رجل عالي الكعب أي شريف (maqayis;ayn)؛ العلاء والعلاء الرفعة والشرف (sihah)؛ العلي هو الرفيع القدر (mufradat)
- **B003** kibirli üstünlük taslama — kınanan büyüklük taslama · yeryüzünde kibirlenip taşkınlık etmek · kibirli ve kendini üstün görenler
  العلو فالعظمة والتجبر (maqayis;ayn)؛ علا ملك في الأرض أي طغى وتعظم (ayn)؛ علا في الأرض تكبر (sihah)؛ علا يقال في المحمود والمذموم (mufradat)
- **B004** yapı içinde üstün gelip bastırma [kalıp] — onu yenip bastırmak · kişiyi yenmek · kılıçla vurmak · işi üstlenip tek başına yürütmek · ata binmek
  من قهر أمرا فقد اعتلاه واستعلى عليه (maqayis)؛ علوت الرجل غلبته (sihah)؛ استعلى الرجل أي علا واستعلاه أي علاه (sihah)؛ الاستعلاء قد يكون طلب العلو المذموم وقد يكون طلب العلاء (mufradat)
- **B005** üst yan ve yukarıdanlık [kalıp] — evin üst kısmı; altının karşıtı · yukarıdan · üstten veya yukarıdan · yukarıdan · rüzgarın avın üstünde kalan yönü
  أسفل الشيء وأعلاه (maqayis)؛ جئتك من أعلى ومن علا ومن عال ومن عل (maqayis)؛ علو الدار نقيض سفلها (sihah)؛ علاوة الريح وسفالتها (sihah;mufradat)؛ علاوة الشيء أعلاه (mufradat)
- **B006** gel diye çağırma — gel; buraya yönel
  تعال فهو من العلو كأنه قال اصعد إلي (maqayis)؛ لا يستعمل هذا إلا في الأمر خاصة (maqayis)؛ التعالي الارتفاع تقول منه إذا أمرت تعال (sihah)؛ تعال أصله أن يدعى الإنسان إلى مكان مرتفع (mufradat)
- **B007** yüksek yer adları — dağ başı veya yüksek yer · yüksek bölge veya yukarıdaki yerleşim · yüksek yerler veya oraların halkı · üst oda · iyi kimselere ait çok yüksek yer veya kayıt
  العلياء رأس كل جبل أو شرف (maqayis)؛ العالية من محال العرب من الحجاز (maqayis)؛ العلية غرفة (maqayis;sihah)؛ العلياء كل مكان مشرف (sihah)؛ لفي عليين (maqayis;mufradat)؛ العلية اسما للغرفة (mufradat)
- **B008** üstüne eklenen veya üst parça — tam yükten sonra üste konan ek yük · baş ve boyun · bir şeyin üst kısmı · kitabın başlığı; başta ve üstte yer alan ad
  العلاوة ما يحمل على البعير بعد تمام الوقر (maqayis)؛ رأس الرجل وعنقه علاوة (maqayis)؛ علوان الكتاب من العلو لأنه أول الكتاب وأعلاه (maqayis)؛ العلاوة ما عليت به على البعير بعد تمام الوقر (sihah)؛ علاوة الشيء أعلاه (mufradat)
- **B009** belirli araç ve parça adları — örs · kurutulmuş süt ürünü konan taş · mızrağın uç kısmına yakın bölümü · oyun oklarının yedincisi ve en değerlisi · kova ipini makaraya geri alan kişi · sağ yandan süt hayvanına yaklaşan kişi · ipi makaradaki yerine kaldırmak
  العلاة وهي السندان (maqayis)؛ العلاة حجر يجعل عليه الأقط والعلاة السندان (sihah)؛ عالية الرمح ما دخل في السنان إلى ثلثه (sihah)؛ المعلى السابع من القداح (maqayis;sihah;mufradat)؛ المعلي الذي يمد الدلو (maqayis)
- **B010** uzun ve iri yapılı — uzun iri kimse veya iri deve · sağlam yapılı dişi deve · uzun, iri ve sağlam yaratılışlı
  ناقة عليان أي طويلة جسيمة ورجل عليان طويل (maqayis)؛ يقال للناقة علاة تشبه بها في صلابتها (maqayis;sihah)؛ يقال رجل عليان وكذلك المرأة (sihah)؛ العليان البعير الضخم (mufradat)
- **B011** bedensel halden kurtulup esenleşme [kalıp] — lohusalıktan temizlenip esenliğe kavuşmak · hastalıktan kurtulmak
  للمرأة إذا طهرت من نفاسها قد تعلت (maqayis)؛ لا يقال إلا للنفساء (maqayis)؛ تعلت المرأة من نفاسها أي سلمت وتعلى الرجل من علته (sihah)
- **B012** ilgeç ve kalıplaşmış görev sözü — üzerinde, üzerine veya benzeri ilgeç görevi · şunu al · bana şunu ver · onun yanından veya üstünden
  جئت من عليك أي من عندك (maqayis)؛ على لها ثلاثة مواضع (sihah)؛ لفظة مشتركة للاسم والفعل والحرف (sihah)؛ على حرف خافض وقد يكون اسما (sihah)؛ عليك زيدا أي خذه (sihah)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:10, and ## Buluşmalar) =====
## Örten: Gâşiye, bahçe ve örtüsünü yitiren

Sure bir soruyla açılır: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. Gâşiye "üstüne gelip örten" demektir. Kökün temel işi, bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"}. Kelimenin elle tutulur bir karşılığı da vardır. Eyerin üstüne atılan örtüye de bu ad verilir: {ar:وغاشية السرج غطاؤه, tr:ve ğâşiyetü's-serci ğıtâuhû, gloss:eyerin gâşiyesi onun örtüsüdür, source:"غ ش و,B001"}. Böyle bir örtü yukarıdan atılır, eyeri her yanından sarar ve altında kalanı gözden saklar. Kıyamet bu adla anıldığında aynı hareket bütün yaratılmışlara uygulanmış olur: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâmetü li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:Gâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Örtü dışarıda da kalmaz. Aynı fiil, başa gelen bir şeyin aklı kapatmasını, yani bayılmayı da anlatır: {ar:غشي على فلان إذا نابه ما غشي فهمه, tr:ğuşiye alâ fülânin izâ nâbehû mâ ğaşiye fehmehû, gloss:başına gelen şey anlayışını örtünce falan bayıldı denir, source:"غ ش و,B005"}. Demek ki ilk ayetteki tek kelimede bir örtü duyulur: dışarıdan iner, her yanı kuşatır ve içeriye, akla kadar işler. Kelimeyi yalnızca "kıyamet" diye karşılamak bu hareketi kaybettirir.

Bu yazı boyunca geçerli bir kural var: Bir kelimenin akrabalarından gelen resimler, o kelimenin ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Gâşiye burada o günün adıdır. Eyer örtüsü ve baygınlık yalnızca bu adın nasıl işlediğini gösterir.

Örtünün ilk indiği yer yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2}. Yüz, bir şeyin karşıya dönük ön tarafıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. Kur'an bu sahneyi başka yerlerde açıkça kurar. Suçluların o gün zincirlere vurulduğu anlatılırken şöyle denir: {ar:سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:serâbîluhum min katırânin ve tağşâ vucûhehumu'n-nâr, gloss:gömlekleri katrandandır ve yüzlerini ateş örter, source:14:50}. Kötülük kazananlar için başka bir yerde verilen benzetme, örtüyü gecenin kendisinden yapar: {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhum kıtaan mine'l-leyli muzlimâ, gloss:sanki yüzlerine karanlık geceden parçalar örtülmüş, source:10:27}.

Surenin ilk ve son adları tek bir ayette bir araya gelir. Yusuf kıssasının sonunda Allah, Peygamber'e insanların çoğunun inanmadığını söyledikten sonra sorar: {ar:أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:e-fe-eminû en te'tiyehum ğâşiyetun min azâbillâh, gloss:Allah'ın azabından örten bir şeyin kendilerine gelmesinden emin mi oldular, source:12:107}. Bu ayette surenin ilk fiili (gelmek), ilk adı (örten) ve yirmi dördüncü ayetteki azap aynı cümlededir. Kelimenin açıklaması da bunu söyler: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbillâh ey ukûbetun mücellele teummuhum, gloss:hepsini saran ve kapsayan bir ceza, source:"غ ش و,B002"}. Duhan suresinde Allah, Peygamber'e şüphe içinde oyalananları gösterir ve göğün apaçık bir duman getireceği günü beklemesini söyler. O duman için de şöyle denir: {ar:يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ, tr:yağşe'n-nâs hâzâ azâbun elîm, gloss:insanları örter; bu acı bir azaptır, source:44:11}. Azabın çabuk gelmesini isteyenler için de örtü dört yandan tamamlanır: {ar:يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ, tr:yevme yağşâhumu'l-azâbu min fevkıhim ve min tahti ercülihim, gloss:azabın onları üstlerinden ve ayaklarının altından örteceği gün, source:29:55}. Eyer örtüsü yalnızca üstten sarardı. Burada örtü alttan da kapanır.

Onuncu ayet ikinci bir örtü getirir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10}. Bu kökün aslı da örtmektir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenni setru'ş-şey'i ani'l-hâsse, gloss:bir şeyi duyulardan gizlemek, source:"ج ن ن,B001"}. Bahçe adını ağaçlarının toprağı örtmesinden alır: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü büstânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bostan, source:"ج ن ن,B003"}. Ödül de bugün göze görünmeyen, örtülü bir şeydir: {ar:الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم, tr:el-cennetü mâ yasîru ileyhi'l-müslimûne fi'l-âhira ve huve sevâbun mestûrun anhumu'l-yevm, gloss:cennet bugün onlardan gizli olan ödüldür, source:"ج ن ن,B004"}. Aynı kökten kalkan da çıkar: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-türsü ve'l-cünnetü'd-dir'u ve küllü mâ vakâke fe-huve cünnetük, gloss:seni koruyan her şey senin kalkanındır, source:"ج ن ن,B008"}. Böylece surede iki örtü karşı karşıya durur. Biri yukarıdan iner ve ezer. Öteki aşağıdan büyür, gölgeler ve korur. Bahçe halkı bu ikinci örtüyü birincisinden kurtuluş olarak anar. Birbirlerine dönüp ailelerinin arasındayken nasıl korku içinde yaşadıklarını hatırladıktan sonra şöyle derler: {ar:فَمَنَّ ٱللَّهُ عَلَيْنَا وَوَقَىٰنَا عَذَابَ ٱلسَّمُومِ, tr:fe-mennallâhu aleynâ ve vekânâ azâbe's-semûm, gloss:Allah bize lütfetti ve bizi kavurucu azaptan korudu, source:52:27}. Burada "korumak" fiili, kalkanın tanımındaki fiilin ta kendisidir. Dördüncü ayetteki ateş sıfatı حامية'nin kökü de başka kullanımında korunan yeri anlatır: {ar:الحمى موضع فيه كلأ يحمى من الناس أن يرعى, tr:el-himâ mevziun fîhi keleun yuhmâ mine'n-nâsi en yur'â, gloss:otlu olup insanların otlatmasından korunan yer, source:"ح م ي,B002"}. Bu anlam ayetteki kızgın ateşin yanında duyulur: aynı harflerin koruyan yüzü ateşe girenler için kapanmıştır.

Yirmi üçüncü ayetteki inkâr da bir örtme fiilidir: {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in ğattâ şey'en fe-kad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"}. Kelime imanın karşıtı olarak da bu yüzden kullanılır: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfru zıddü'l-îmân summiye li-ennehû tağtiyetü'l-hak, gloss:küfür imanın zıddıdır; hakkı örttüğü için bu adı almıştır, source:"ك ف ر,B003"}. Tohumu toprakla örten çiftçiye de bu ad verilir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru'z-zâriu li-ennehû yuğattı'l-bezra bi't-turâb, gloss:kâfir tohumu toprakla örten ekincidir, source:"ك ف ر,B008"}. Çiftçinin örtüsünden bir bahçe çıkabilir; hakkı örtenin örtüsünden hiçbir şey bitmez. Kur'an inkârla göz üstündeki örtüyü aynı ayette birleştirir. Uyarılsalar da uyarılmasalar da inanmayacakları söylenenler için şöyle denir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ, tr:ve alâ ebsârihim ğışâvetun ve lehum azâbun azîm, gloss:gözlerinin üstünde bir perde vardır ve onlar için büyük bir azap vardır, source:2:7}. Buradaki perde, Gâşiye ile aynı köktendir. Hakkı örten, sonunda kendi gözünün de örtüldüğünü görür. Gece de surenin üç ayrı kökünde örtü olarak anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}; {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğü zaman geceye andolsun, source:92:1}; İbrahim'in gece karşısındaki anında ise {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ, tr:fe-lemmâ cenne aleyhi'l-leyl, gloss:gece onu örtünce, source:6:76}. Bunlar aynı kökten değildir. Üç ayrı kökün paylaştığı tek bir resimdir.

Son adım yirmi dördüncü ayettedir. Azap ceza demektir: {ar:العذاب العقوبة وقد عذبته تعذيبا, tr:el-azâbu'l-ukûbe ve kad azzebtühû ta'zîbâ, gloss:azap cezadır, source:"ع ذ ب,B005"}. Aynı kökün bir başka kolu ise örtüsüz kalmış insanı anlatır: {ar:العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب, tr:el-azûbu'llezî leyse beynehû ve beyne's-semâi sitr, gloss:kendisiyle gök arasında hiçbir örtü bulunmayan kimse, source:"ع ذ ب,B004"}. Bu anlam ayetteki cezanın yanında duyulduğunda resim tamamlanır. Azap gören hem ezici örtünün altında kalmış hem de kendisini koruyan bütün örtülerden soyulmuştur. Bahçedeki insanın üstünde ise ağaçlardan bir örtü vardır, onu ezen hiçbir şey yoktur.

Kaynaklar: 88:1 ٱلْغَٰشِيَةِ غ ش و B001; 88:1 ٱلْغَٰشِيَةِ غ ش و B002; 88:1 ٱلْغَٰشِيَةِ غ ش و B005; 88:2 وُجُوهٌ و ج ه B001; 88:4 حَامِيَةً ح م ي B002; 88:10 جَنَّةٍ ج ن ن B001; 88:10 جَنَّةٍ ج ن ن B003; 88:10 جَنَّةٍ ج ن ن B004; 88:10 جَنَّةٍ ج ن ن B008; 88:23 وَكَفَرَ ك ف ر B001; 88:23 وَكَفَرَ ك ف ر B002; 88:23 وَكَفَرَ ك ف ر B003; 88:23 وَكَفَرَ ك ف ر B008; 88:24 ٱلْعَذَابَ ع ذ ب B004; 88:24 ٱلْعَذَابَ ع ذ ب B005

## Alçalan ve yükselen

İkinci ayetteki yüz başını eğmiştir: {ar:أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه, tr:aslun vâhidun yedullü ale't-tatâmün; tetâmene ve ta'ta'e ra'sehû, gloss:alçalmayı gösteren kök; başını eğip indirdi, source:"خ ش ع,B001"}. Yemeğinin kökü de alçalmayı anlatır: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Onuncu ayette ise bahçe yüksektedir: {ar:أصل واحد يدل على السمو والارتفاع, tr:aslun vâhidun yedullü ale's-sumuvvi ve'l-irtifâ', gloss:yükseliği ve yüksekte oluşu gösteren kök, source:"ع ل و,B001"}; {ar:العلاء فالرفعة, tr:el-alâu fe'r-rif'a, gloss:alâ yüksek mertebedir, source:"ع ل و,B002"}. On üçüncü ayette sedirler kaldırılmıştır. Kaldırılmak da aşağılanmanın karşıtıdır: {ar:الرفعة نقيض الذلة, tr:er-rif'atü nakîdu'z-zille, gloss:yükseklik aşağılanmanın zıddıdır, source:"ر ف ع,B002"}. On dördüncü ayetteki "konmuş" kelimesinin kökü insanın düşük konumunu da anlatır: {ar:رجل وضيع ضد الشريف والتواضع التذلل, tr:racülün vadîun zıddü'ş-şerîf ve't-tevâdu't-tezellül, gloss:vadî şerefli olanın zıddıdır; tevazu alçalmaktır, source:"و ض ع,B005"}. Bahçede alçak konulan şey insan değildir, hizmet eden kadehlerdir. İnsan yüksek sedirde oturur.

Aynı yükseklik ve alçaklık dünyada da göze gösterilir. Gök yüksekliktir: {ar:أصل يدل على العلو؛ سموت إذا علوت, tr:aslun yedullü ale'l-uluvv; semevtü izâ alevt, gloss:yükseliği gösteren kök; yükseldiğinde semevtü dersin, source:"س م و,B001"}. Yer ise aşağıda olandır: {ar:كل شيء يسفل ويقابل السماء, tr:küllü şey'in yesfülü ve yukâbilü's-semâ', gloss:aşağıda kalıp göğün karşısında duran her şey, source:"ء ر ض,B001"}. Yirmi dördüncü ayetteki azap "en büyük" olandır: {ar:أصل صحيح يدل على خلاف الصغر, tr:aslun sahîhun yedullü alâ hılâfi's-sığar, gloss:küçüklüğün karşıtını gösteren kök, source:"ك ب ر,B001"}. İki kökün öteki yüzü de duyulur. Yükseklik kökü kibirli büyüklenmeyi de anlatır: {ar:العلو فالعظمة والتجبر, tr:el-uluvvu fe'l-azametü ve't-tecebbür, gloss:ulüv büyüklenme ve zorbalıktır, source:"ع ل و,B003"}. "En büyük" kelimesinin kökü de kendini büyük görmeyi adlandırır: {ar:الكبر العظمة وكذلك الكبرياء, tr:el-kibru'l-azametü ve kezâlike'l-kibriyâ', gloss:kibir büyüklüktür; kibriya da öyledir, source:"ك ب ر,B006"}. Bu anlamlar ayetlerdeki anlamların yanında duyulur. Bahçedeki yükseklik verilmiş bir yüksekliktir. İnsanın kendi kendine verdiği yükseklik ise öteki yüzün yolunu açar ve onu "en büyük" azapla karşılaştırır.

Kur'an kıyameti bu iki hareketle adlandırır: {ar:إِذَا وَقَعَتِ ٱلْوَاقِعَةُ, tr:izâ vekaati'l-vâkıa, gloss:olacak olan olduğunda, source:56:1}; {ar:خَافِضَةٌۭ رَّافِعَةٌ, tr:hâfidatun râfia, gloss:alçaltan ve yükselten, source:56:3}. Dünyada da yükseltme Allah'ın işidir. Müminlere meclislerde yer açmaları ve kalkmaları söylendiğinde kalkmanın karşılığı şudur: {ar:يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ, tr:yerfaillâhullezîne âmenû minkum, gloss:Allah içinizden inananları yükseltir, source:58:11}. Ateşe sunulan zalimler ise {ar:خَٰشِعِينَ مِنَ ٱلذُّلِّ, tr:hâşiîne mine'z-zull, gloss:aşağılanmadan eğilmiş, source:42:45} diye anılır. O günün gözleri için de {ar:خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ, tr:hâşiaten ebsâruhum terhakuhum zille, gloss:gözleri eğik ve kendilerini aşağılanma bürümüş, source:70:44} denir. "En büyük azap" sözü Kur'an'da bir yerde daha geçer ve orada küçüğün karşısına konur: {ar:وَلَنُذِيقَنَّهُم مِّنَ ٱلْعَذَابِ ٱلْأَدْنَىٰ دُونَ ٱلْعَذَابِ ٱلْأَكْبَرِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve le-nuzîkannehum mine'l-azâbi'l-ednâ dûne'l-azâbi'l-ekberi leallehum yerciûn, gloss:belki dönerler diye onlara en büyük azaptan önce yakın azaptan tattıracağız, source:32:21}. Alt basamak bir uyarıdır, üst basamak sonun kendisidir. Önceki surede de ateş aynı ölçüyle anılır: {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:10 عَالِيَةٍ ع ل و B001; 88:10 عَالِيَةٍ ع ل و B002; 88:10 عَالِيَةٍ ع ل و B003; 88:13 مَّرْفُوعَةٌ ر ف ع B002; 88:14 مَّوْضُوعَةٌ و ض ع B005; 88:18 ٱلسَّمَآءِ س م و B001; 88:20 ٱلْأَرْضِ ء ر ض B001; 88:24 ٱلْأَكْبَرَ ك ب ر B001; 88:24 ٱلْأَكْبَرَ ك ب ر B006

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

