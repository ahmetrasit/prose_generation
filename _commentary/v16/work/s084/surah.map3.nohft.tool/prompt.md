Surah: 84. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S84 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), an earlier reader's channel review (channels.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not delegate, browse or inspect files; run only the command the header describes.

The channel review is an earlier reader's proposal. Ignore its judgements: grades,
strength or confidence labels, reading types, words such as "surprising", "exploratory" or "latent", and every
statement of what a reading may or may not do. Make your own judgement from the surah's words, the dictionary
phrases and the Quran. Do not rediscover what it already assembled: start from its chains, test each one
against the dictionary phrases and the text, and join, extend, split or correct them. Where its wording
abstracts a member, go back to the dictionary phrase and name what it actually says.

A chain belongs on the map when its members are senses the dictionary attests for words that stand in the surah,
and together they make one image or process that the surah's wording or sequence lets a listener hear. A member
need not be the sense that translates its word in its own ayah; a chain is heard across the surah, not in one
word. A chain may join a sense and its reversal as well as the parts of one scene. Mark a member attested only
inside a fixed expression [fixed expression]; add no other label to a member or a chain, and where a source
records a phrase and rejects it, say so of that phrase alone. When the dictionary itself joins two of the
surah's words in one phrase, quote that phrase: it is the strongest evidence a chain can have. Keep a scene at
the level of its objects, their parts and their operation. When proposals share members, do not fold one into
another's more abstract function unless nothing concrete is lost. Carry every chain that meets this test,
however unusual; leave out proposals that do not.

Write the map in English, with Arabic quoted exactly (surah wording from the text, dictionary phrases from the
dictionary). It is working material for the writer, not commentary prose.

1. `## Chains`. For each chain, a `###` heading naming the image. One paragraph on what the image is and how it
   moves through the surah. Then its members, one line each: the ayah ref, the word as it stands in the text,
   the root and branch id, the dictionary's own phrase quoted exactly, and what this member contributes to the
   image. Add Quran passages outside the surah, with exact refs, where they stage or confirm the chain; for
   each, name the speaker and the situation in a few words, and include the ayah that opens its scene when the
   passage continues one.
2. `## Interactions`. Where chains meet: a shared member, a dictionary phrase that joins members of two chains,
   a Quran passage that stages two chains together, or one chain's scene needing another's. One line each: the
   chains, where they meet, the evidence.
3. `## Ayat`. For each ayah in order: the chains its words take part in, what its words add to each, and in one
   line the whole scene each chain makes across the surah, so that a writer who sees only this ayah sees the
   scene, not a fragment.
4. `## Not carried`. Each channel subchannel you did not carry into a chain: one short line
   each, its name and why, no prose.

No ranking and no labels of strength or confidence. No list of what a writer must include. There is no length
target and no required number of chains or members.

===== _commentary/v16/work/s084/surah.r2/text.md =====
# Surah 84

- 84:1 إِذَا ٱلسَّمَآءُ ٱنشَقَّتْ
- 84:2 وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ
- 84:3 وَإِذَا ٱلْأَرْضُ مُدَّتْ
- 84:4 وَأَلْقَتْ مَا فِيهَا وَتَخَلَّتْ
- 84:5 وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ
- 84:6 يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ
- 84:7 فَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ بِيَمِينِهِۦ
- 84:8 فَسَوْفَ يُحَاسَبُ حِسَابًۭا يَسِيرًۭا
- 84:9 وَيَنقَلِبُ إِلَىٰٓ أَهْلِهِۦ مَسْرُورًۭا
- 84:10 وَأَمَّا مَنْ أُوتِىَ كِتَٰبَهُۥ وَرَآءَ ظَهْرِهِۦ
- 84:11 فَسَوْفَ يَدْعُوا۟ ثُبُورًۭا
- 84:12 وَيَصْلَىٰ سَعِيرًا
- 84:13 إِنَّهُۥ كَانَ فِىٓ أَهْلِهِۦ مَسْرُورًا
- 84:14 إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ
- 84:15 بَلَىٰٓ إِنَّ رَبَّهُۥ كَانَ بِهِۦ بَصِيرًۭا
- 84:16 فَلَآ أُقْسِمُ بِٱلشَّفَقِ
- 84:17 وَٱلَّيْلِ وَمَا وَسَقَ
- 84:18 وَٱلْقَمَرِ إِذَا ٱتَّسَقَ
- 84:19 لَتَرْكَبُنَّ طَبَقًا عَن طَبَقٍۢ
- 84:20 فَمَا لَهُمْ لَا يُؤْمِنُونَ
- 84:21 وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ ۩
- 84:22 بَلِ ٱلَّذِينَ كَفَرُوا۟ يُكَذِّبُونَ
- 84:23 وَٱللَّهُ أَعْلَمُ بِمَا يُوعُونَ
- 84:24 فَبَشِّرْهُم بِعَذَابٍ أَلِيمٍ
- 84:25 إِلَّا ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ أَجْرٌ غَيْرُ مَمْنُونٍۭ


===== _commentary/v16/work/s084/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م و (root_000745): 84:1 ٱلسَّمَآءُ

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ECHO و س م (root_001650): for 84:1 ٱلسَّمَآءُ: withheld observed target; not identity

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

## ش ق ق (root_000807): 84:1 ٱنشَقَّتْ

- **B001** yarma, yarılma ve açılma — bir şeyi yarıp açmak veya ikiye ayırmak · çatlak, yarık veya delik · dağda, yerde veya başka bir şeydeki çatlaklar · derinin çatlaması veya hayvanın bileklerindeki çatlak hastalığı · dişin çıkması veya tanın sökmesi
  شققت الشيء أشقه شقا إذا صدعته (maqayis); الشق مصدر قولك شققت والشقاق تشقق الجلد والصدوع في الجبال والأرضين (tahdhib); الشق الخرم الواقع في الشيء وشققته بنصفين (mufradat); شققت الشيء فانشق وشققت الحطب وغيره فتشقق وشق ناب البعير وشق الفجران (sihah;tahdhib)
- **B002** yarım veya yan — bir şeyin yarısı veya yanı · öz kardeş, denk veya insanın öteki yarısı · başın ve yüzün bir yarısını tutan ağrı, migren
  يقال لنصف الشيء الشق والشق أيضا الناحية من الجبل والشق الشقيق وشق نفسي (maqayis); الشق بالكسر نصف الشيء والشق أيضا الناحية من الجبل والشق أيضا الشقيق والشقيقة وجع يأخذ نصف الرأس والوجه (sihah); الشق الجانب والشق الشقيق وخذ هذا الشق لشقة الشاة والشقيقة صداع يأخذ في نصف الرأس والوجه (tahdhib); شققته بنصفين (mufradat)
- **B003** ağır güçlük ve çaba — ağır iş, güçlük ve yoğun çaba · bütün gücünü zorlayarak, çok güçlükle · bir işin kişiye ağır gelmesi
  أصاب فلانا شق ومشقة وذلك الأمر الشديد (maqayis); الشق المشقة ومنه بالغيه إلا بشق الأنفس (sihah); الشق المشقة في السير والعمل ومعناه إلا بجهد الأنفس وشق علي ذاك الأمر مشقة أي ثقل علي (tahdhib)
- **B004** anlaşmazlıkla bölünüp ayrılma — anlaşmazlık, düşmanlık ve topluluktan ayrılma · birliği bozup topluluktan ayrılmak
  الشقاق وهو الخلاف وذلك إذا انصدعت الجماعة وتفرقت وشقوا عصا المسلمين (maqayis); شق فلان العصا أي فارق الجماعة والمشاقة والشقاق الخلاف والعداوة (sihah); الشقاق العداوة بين فريقين والخلاف بين اثنين وشق الخوارج عصا المسلمين (tahdhib)
- **B005** uzak yol ve uzun yolculuk — uzun yolculuk veya uzak yol mesafesi · uzak ve aşılması güç yol
  الشقة مسير بعيد إلى أرض نطية وهذه شقة شاقة ولكن بعدت عليهم الشقة (maqayis); الشقة أيضا السفر البعيد وشقة شاقة (sihah); الشقة بعد مسير إلى الأرض البعيدة يقال شقة شاقة (tahdhib)
- **B006** yarılıp ayrılmış parça — tahtadan kopan kıymık veya bir kumaş parçası · çok öfkelenip çılgına dönmek
  الشقة شظية تشظى من لوح أو خشبة وفطارت منه شقة والشقة من الثياب (maqayis); الشقة شظية تشظى من لوح أو خشبة والشقة بالضم من الثياب (sihah); الشقة شظية تشق من لوح أو خشبة وشقة في الأرض وشقة في السماء والشقة معروفة في الثياب (tahdhib)
- **B007** kum sırtları arasındaki otlu açıklık — kum sırtları arasında ot bitiren açıklık veya sert toprak · kırmızı anemon çiçeği · bol yağmur taşıyan bulutlar
  الشقيقة فرجة بين الرمال تنبت والشقيقة أرض غليظة بين حبلين من الرمل (maqayis); الشقيقة الفرجة بين الحبلين من حبال الرمل تنبت العشب وشقائق النعمان معروف (sihah); الشقيقة الفرجة بين الرمال تنبت العشب ونور أحمر يسمى شقائق النعمان والشقائق أيضا سحائب (tahdhib)
- **B008** devenin böğürme kesesi — devenin böğürürken ağzından çıkardığı boğaz dokusu · gür sesli ve sözünde usta hatip · erkek devenin böğürmesi veya kuşun özel ötüşü
  الشقشقة لهاة البعير ويقال للخطيب هو شقشقة (maqayis); شقشق الفحل شقشقة هدر والعصفور يشقشق والشقشقة شيء كالرئة يخرجها البعير وإذا قالوا للخطيب ذو شقشقة (sihah); الشقشقة لهاة الجمل وجمعها الشقاشق والخطيب الجهير الصوت هرت الشقاشق (tahdhib)
- **B009** amaç çizgisinden yana sapma — konuşmada veya tartışmada ana amaçtan sağa sola sapmak · koşarken bir yanına eğilen at
  اشتق في الكلام في الخصومات يمينا وشمالا مع ترك القصد وفرس أشق إذا مال في أحد شقيه عند عدوه (maqayis); الاشتقاق الأخذ في الكلام وفي الخصومة يمينا وشمالا وفرس أشق (sihah); الاشتقاق الأخذ في الخصومات يمينا وشمالا وفرس أشق وقد اشتق في عدوه (tahdhib)
- **B010** uzun veya bacak arası geniş at — uzun veya bacak arası geniş at; ayrıca zayıflayıp incelmek
  فرس أشق أي طويل والأنثى شقاء (sihah); فرس أشق له معنيان الأشق الطويل والأشق من الخيل الواسع ما بين الرجلين وتشقق الفرس تشققا إذا ضمر (tahdhib)

## ECHO ش ق و (root_000808): for 84:1 ٱنشَقَّتْ: withheld observed target; not identity

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ن ش ق (root_001506): for 84:1 ٱنشَقَّتْ: withheld observed target; not identity

- **B001** bir bağa takılıp tutulma — tuzağa veya ipe takılıp kalmak · yavruların boynuna geçirilen bağ veya boyun bağı halkası · içinden kolayca çıkamayacağı bir işe düşmüş kişi · boyun bağının halkaları · onu ipe takıp tutmak · avının boynuna tuzak bağı geçen avcı · av paylaşımında boyun halkasına yakalanan pay
  أصل صحيح يدل على نشوب شيء (maqayis)؛ نشق الظبي في الحبالة علق فيها والنشقة حبل يجعل في أعناق البهم (maqayis)؛ رجل نشق إذا وقع في أمر لا يكاد يخلص منه (maqayis)؛ نشب الصيد في حبله ونشق وعلق وارتبق (tahdhib)؛ لحلق الربق نشق واحدها نشقة (tahdhib)
- **B002** burundan ilaç uygulama — ilacı veya burun ilacını buruna dökmek · burun deliklerine konup burundan alınan ilaç · burun ilacını buruna dökme · yakılmış pamuğu burna yaklaştırıp kokusunu içeri aldırmak · ilacı burundan almak · ilacı burundan içeri çekmek
  أنشقت الصبي الدواء صببته في أنفه (maqayis)؛ النشوق اسم لكل دواء ينشق (maqayis;tahdhib)؛ النشق صب سعوط في الأنف وأنشقته الدواء (ayn;tahdhib)؛ أنشقته قطنة محرقة أي أدنيتها من أنفه ليدخل ريحها في أنفه وخياشيمه (ayn;tahdhib)؛ النشوق سعوط يجعل في المنخرين (tahdhib)
- **B003** kokuyu burundan algılama [kalıp] — esintiyi veya kokuyu koklamak · koklaması hoş olmayan koku · birinden hoş bir koku almak
  استنشقت الريح تشممتها (maqayis;tahdhib)؛ ريح مكروهة النشق أي الشم (maqayis;ayn;tahdhib)؛ استنشقته أي تشممته (ayn)؛ نشقت من الرجل ريحا طيبة (tahdhib)
- **B004** suyu burnuna çekme [kalıp] — suyu burnuna çekip iç burun kanallarına ulaştırmak
  المتوضىء يستنشق الماء عند استنثاره (maqayis)؛ استنشقت الماء مددته بريح الأنف (ayn)؛ المتوضىء يستنشق إذا أبلغ الماء خياشيمه (tahdhib)
- **B005** umduğunu bulamayacağını söyleyerek geri çevirme — umduğunu bulamayacaksın diyerek isteğini geri çevirmek
  استنشق الريح فإنك لا تجد ما ترجو إذا أراد شيئا فخيبته (ayn)

## ء ذ ن (root_000022): 84:2 وَأَذِنَتْ, 84:5 وَأَذِنَتْ

- **B001** kulak ve kulak biçimli tutamak — kulak; işitme organı · kulaklar · kulaklı · kulaklı ya da uzun kulaklı dişi hayvan · büyük kulaklı · kupanın ya da kabın kulak biçimli tutamağı · ayakkabıya kulak biçimli bağ ya da işaret yapmak · kulağına vurmak ya da kulağını ovmak
  الأذن معروفة مؤنثة؛ أذن كل ذي أذن (maqayis)؛ هو أذن؛ الأذن العروة أي عروة الكوز (ayn)؛ الأذن تخفف وتثقل وهي مؤنثة؛ رجل أذاني؛ أذنت النعل إذا جعلت لها أذنا (sihah)؛ آذان الكيزان عراها؛ أذنت فلانا إذا ضربت أذنه (tahdhib)؛ الأذن الجارحة وشبه به أذن القدر وغيرها (mufradat)
- **B002** kulak verip benimseme — her söyleneni dinleyip kabul eden kişi · her şeyi dinleyen kişi · kulak vermek, dikkatle dinlemek · buyruğu dinleyip uymak
  الأذن الاستماع؛ رجل سامع من كل أحد أذن (maqayis)؛ أذن له استمع؛ رجل أذنة يستمع لكل شيء (ayn)؛ أذن له أذنا استمع؛ رجل أذن إذا كان يسمع مقال كل أحد ويقبله (sihah)؛ أذنت للشيء إذا استمعت له؛ هو أذن أي يستمع فيقبل؛ وأذنت لربها أي سمعت سمع طاعة وقبول (tahdhib)؛ أذن استمع؛ ويستعار لمن كثر استماعه (mufradat)
- **B003** bilme ve başkasına bildirme — bu konuyu bilmek · ona bunu bildirmek · duyuru; özellikle namazı ve vaktini bildiren çağrı · bildirme ve duyurma · duyuru ya da sesli çağrı · çağrının her yandan ulaştığı yer · duyurucu ya da çağrıcı · namaz vakitlerini çağrıyla bildiren kişi · namaz çağrısının yapıldığı kule ya da yüksek yer
  الأصل الآخر العلم والإعلام؛ آذنني فلان أعلمني؛ الأذان اسم التأذين؛ الأذين المكان يأتيه الأذان؛ الأذين المؤذن (maqayis)؛ أذنت بهذا الشيء أي علمت؛ آذنني أعلمني؛ الأذان اسم للتأذين؛ هل سمعت الأذان من المئذنة (ayn)؛ أذن بمعنى علم؛ الأذان الإعلام؛ أذان الصلاة معروف؛ المئذنة المنارة؛ آذنتك بالشيء أعلمتكه (sihah)؛ آذنته إذا أعلمته؛ الأذان للصلاة إعلام بها وبوقتها؛ المؤذن المعلم بأوقات الصلاة؛ ثم أذن مؤذن أي نادى مناد (tahdhib)؛ يستعمل ذلك في العلم؛ المؤذن كل من يعلم بشيء نداء (mufradat)
- **B004** onay verme ve yetkilendirme — bir işi yapmasına onay vermek · onay veya yetkilendirme; ayrıca bilgisi ya da buyruğuyla yapılan iş · birinden onay istemek · içeri girişe onay veren kapı görevlisi
  فعله بإذني أي بعلمي ويجوز بأمري؛ أذن لي في كذا (maqayis)؛ فعله بإذني أي بعلمي وهو في معنى بأمري؛ الذي يأذن بالدخول (ayn)؛ أذن له في الشيء؛ ائذن لي على الأمير؛ الآذن الحاجب (sihah)؛ أذنت لفلان في أمر كذا؛ استأذنت فلانا؛ بإذن الله أي بعلمه؛ ويكون بإذنه أي بأمره (tahdhib)؛ ائذن لي؛ الأذن والأذان لما يسمع ويعبر بذلك عن العلم (mufradat)
- **B005** kendini bağlayan kesin bildirim — 
  تأذن ربكم؛ التأذن من قولك لأفعلن كذا تريد به إيجاب الفعل؛ وأوضح منه أعلم ربكم (maqayis)؛ التأذن من قولك تأذنت لأفعلن كذا يراد به إيجاب الفعل (ayn)؛ تأذنت لأفعلن كذا وكذا يراد به إيجاب الفعل (tahdhib)

## ر ب ب (root_000532): 84:2 لِرَبِّهَا, 84:5 لِرَبِّهَا, 84:6 رَبِّكَ, 84:15 رَبَّهُۥ

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

## ECHO ر ب و (root_000537): for 84:2 لِرَبِّهَا, 84:5 لِرَبِّهَا, 84:6 رَبِّكَ, 84:15 رَبَّهُۥ: withheld observed target; not identity

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

## ح ق ق (root_000347): 84:2 وَحُقَّتْ, 84:5 وَحُقَّتْ

- **B001** gerçekliğe uygun, kesin doğruluk — gerçekte var olana uygun, doğru ve sağlam olan · işin açığa çıkmış gerçek yüzü · kesinlikle yapmayacağım diye yemin etme sözü · konuyu doğrulayıp kesinliğinden emin oldum · haber doğru çıktı ve kesinleşti · gerçekte var olan şey veya sözün ilk anlamı
  الحق نقيض الباطل (maqayis;sihah;tahdhib)؛ أصل الحق المطابقة والموافقة (mufradat)؛ حققت الأمر وأحققته إذا تحققته وصرت منه على يقين (sihah)؛ الحقيقة خلاف المجاز (sihah)
- **B002** bağlayıcı gereklilik ve hak ediş — gerekli ve bağlayıcı oldu · bildirilen hüküm onun için kesinleşip bağlayıcı oldu · buna layık veya bunu yapmakla yükümlü · bunu yapman sana düşer veya senin yükümlülüğündür · gerekli kıldı veya bir sonucu hak etti · korktuğu şeyi yapıp başına getirdi · doğru bir istem ileri sürdü ve isteği kesinleşti
  حق الشيء وجب (maqayis;sihah;tahdhib)؛ حقيق بكذا ومحقوق به (maqayis;sihah;tahdhib)؛ أحققت الشيء أي أوجبته واستحققته أي استوجبته (sihah)؛ يستعمل استعمال الواجب واللازم والجائز (mufradat)
- **B003** sahibine bağlı pay ve istem yetkisi — sahibine ait ve onun isteyebileceği özel pay · kişinin kendine ait belirli payı · malı, elinde tutana karşı kendisinin saydırıp geri aldı
  إنك لتعرف الحقة عليك (maqayis)؛ الحق واحد الحقوق والحقة أخص منه، هذه حقتي أي حقي (sihah;tahdhib)؛ استحقها على المشتري أي ملكها عليه (tahdhib)؛ وبعولتهن أحق بردهن (mufradat)
- **B004** doğru taraf olma savıyla çekişme — doğrunun kendisinde olduğunu ileri sürerek onunla çekişti · karşılıklı çekişip her biri kendini doğru saydı · küçük konularda bile durmadan çekişen · çekişmede savını kabul ettirip üstün geldi
  حاق فلان فلانا إذا ادعى كل واحد منهما (maqayis)؛ حاقه أي خاصمه، والتحاق التخاصم والاحتقاق الاختصام (sihah)؛ تحاق القوم واحتقوا إذا تخاصموا (tahdhib)؛ حاققته فحققته أي خاصمته في الحق فغلبته (mufradat)
- **B005** doğruluğunu belirleme ve gösterme — konuyu doğrulayıp kesinliğinden emin oldum · sözünün veya sanısının doğru çıktığını gösterdi · savını geçerli kılıp karşısındakine üstün geldi · doğruyu söyledi veya doğru istemi kabul edildi
  حققت الأمر وأحققته أي كنت على يقين منه (maqayis)؛ حققت قوله وظنه تحقيقا أي صدقت (sihah)؛ حقق الرجل إذا قال هذا الشيء هو الحق (tahdhib)؛ أحققت كذا أي أثبته حقا أو حكمت بكونه حقا، ليحق الحق (mufradat)
- **B006** karşılığın kesinleştiği Son Gün — bütün karşılıkların kesinleştiği Son Yargı Günü
  الحاقة القيامة لأنها تحق بكل شيء (maqayis)؛ الحاقة القيامة سميت بذلك لأن فيها حواق الأمور (sihah)؛ سميت حاقة لأنها تحق كل إنسان بعمله (tahdhib)؛ الحاقة إشارة إلى القيامة لأنه يحق فيه الجزاء (mufradat)
- **B007** korunması ve savunulması gereken şey — koruması gereken şeyi savunan kişi · korunacak bayrak, dokunulmaz değer veya çevre
  حامي الحقيقة إذا حمى ما يحق عليه أن يحميه ويقال الحقيقة الراية (maqayis)؛ الحقيقة ما يحق على الرجل أن يحميه (sihah)؛ الحقيقة الراية والحرمة والفناء وما يلزمه الدفاع عنه (tahdhib)؛ فلان يحمي حقيقته أي ما يحق عليه أن يحمى (mufradat)
- **B008** dördüncü yaşındaki yük taşımaya elverişli deve — üç yaşını tamamlamış, yük veya binme için elverişli dişi deve · üç yaşını tamamlamış, yük veya binme için elverişli erkek deve · dişi devenin çiftleştirildiği belirli zaman
  الحقة من أولاد الإبل ما استحق أن يحمل عليه (maqayis)؛ الحق من الإبل ابن ثلاث سنين وقد دخل في الرابعة والأنثى حقة (sihah;tahdhib)؛ الحق من الإبل ما استحق أن يحمل عليه والأنثى حقة (mufradat)؛ أتت الناقة على حقها أي الوقت الذي ضربت فيه (sihah;tahdhib;mufradat)
- **B009** iç boşluğa ulaşan düz saplanış — düz ilerleyip bedenin iç boşluğuna ulaşan saplanış · avın bir bölümünü öldürücü veya delici biçimde vurdu
  طعنة محتقة إذا وصلت إلى الجوف (maqayis)؛ طعنة محتقة أي لا زيغ فيها وقد نفذت (sihah)؛ المحتق من الطعن النافذ إلى الجوف (tahdhib)
- **B010** sıkı dokunmuş veya sağlam kurulmuş [kalıp] — sıkı ve düzgün dokunmuş kumaş · sağlam, tutarlı ve iyi kurulmuş söz
  ثوب محقق إذا كان محكم النسج (maqayis;sihah)؛ كلام محقق أي رصين (sihah)؛ أحققت الأمر إحقاقا إذا أحكمته وصححته (tahdhib)
- **B011** özel adlandırma kümesi — iki kemiğin birleştiği eklem yeri · başın tam ortası veya kışın ortası · ağaçtan veya fildişinden yapılmış küçük kap · kapı ayağının oturup döndüğü yuva · örümcek ağı
  الحق ملتقى كل عظمين والحق من الخشب (maqayis)؛ سقط على حاق رأسه وجئته في حاق الشتاء (sihah)؛ الحقة من خشب وحق العاج وحق الورك وحق الوابلة وحق الكهول بيت العنكبوت (tahdhib)؛ مطابقة رجل الباب في حقه (mufradat)
- **B012** bineği gücünü aşacak biçimde sert sürme — bineğin sırtını yoran, gücünü aşan sert sürüş
  الحقحقة أرفع السير وأتعبه للظهر (maqayis;sihah)؛ الحقحقة عند العرب أن يسار البعير ويحمل على ما يتعبه ولا يطيقه (tahdhib)؛ الحقحقة السير الشديد (tahdhib)
- **B013** devenin veya sürünün iyice semirmesi — dişi deve semirdi veya çiftleşip gebe kaldı · topluluğun sürüsü semirdi veya en semiz durumuna ulaştı
  أحقت الناقة من الربيع أي سمنت (maqayis)؛ استحقت الناقة سمنا وأحقت وحقت إذا سمنت (tahdhib)؛ أحق القوم إحقاقا إذا سمن مالهم واحتق المال إذا سمن وانتهى سمنه (tahdhib)
- **B014** terlemeyen veya art ayağını ön ayak izine basan at — terlemeyen veya art ayağını ön ayağının bastığı yere koyan at · at zayıfladı ve bedeni inceldi
  الأحق من الخيل الذي لا يعرق (maqayis;sihah;tahdhib)؛ الأحق أن يطبق هذا ذاك (maqayis)؛ الأحق الذي يضع رجله في موضع يده (tahdhib)؛ احتق الفرس أي ضمر (sihah)

## ء ر ض (root_000025): 84:3 ٱلْأَرْضُ

- **B001** yer ve yere bakan alt bölüm — yer, yeryüzü · yerler, ülkeler · bir şeyin yere bakan altı · hayvanın tırnağı veya ayaklarının altı
  كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)
- **B002** yumuşak ve verimli toprak — yumuşak, verimli ve bol bitkili toprak · yumuşak tabanlı geniş çayırlık · toprak verimlileşti · bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi · toprakta kök salmış fidan · oğlak yer bitkisini yedi veya onunla semirdi
  أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)
- **B003** iyiliğe yatkın ve layık [kalıp] — iyiliğe yatkın, layık ve alçak gönüllü kişi · bunu yapmaya en uygunları
  رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)
- **B004** yabancı kimse — yabancı kimse
  فلان ابن أرض أي غريب (maqayis)
- **B005** kalın yün veya kıl yaygı — kalın yün veya kıl yaygı
  الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)
- **B006** yere çökercesine ağırlaşıp oyalanmak — yere bağlı kalmak, ağırlaşıp oyalanmak
  تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)
- **B007** karşısına çıkıp kendini ortaya koymak — birinin karşısına çıkıp kendini ortaya koymak
  جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)
- **B008** titreme veya ürperme — insanı tutan titreme veya ürperme · titreme ve sarsılma
  الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)
- **B009** soğuk algınlığı — soğuk algınlığı · soğuk algınlığına yakalanmış · soğuk algınlığına uğratmak
  الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)
- **B010** odun yiyen küçük canlı — odun yiyen küçük canlı · odunu bu canlı yedi ve zarar verdi
  الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)
- **B011** yaranın irinlenip bozulması [kalıp] — yara irinlenip kabardı ve bozuldu
  أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)
- **B012** doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu — görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi
  المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)

## م د د (root_001407): 84:3 مُدَّتْ

- **B001** uzatma ve boyuna yayılma — bir şeyi boyuna çekip uzatmak · uzamak veya yayılmak · gölgeyi uzatıp yaymak · bakışı uzağa yöneltmek; görüş mesafesi · günün yükselip ilerlemesi · uzun boylu · gerinip uzanmak · iplerle gerilip uzatılmış · birini oyalayıp çekiştirmek
  جر شيء في طول واتصال شيء بشيء في استطالة (maqayis)؛ مددت الشيء ومددت الحبل فامتد (maqayis;jamhara;sihah;tahdhib)؛ أصل المد الجر ومد الظل ومددت عيني (mufradat)؛ مد النهار ارتفاعه ومد البصر ورجل مديد القامة وتمدد الرجل (maqayis;sihah;tahdhib)
- **B002** destekleyici ek sağlama — orduya destek kuvvet göndermek · yardım veya takviye kuvvet · bir topluluğa destek olmak · yiyecek veya benzeri kaynak sağlamak · bağlı ek; başka bir şeyi besleyen kaynak · toprağa toprak veya gübre eklemek · sözlerinin sayısı ve çokluğu
  أمددت الجيش بمدد (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الاستمداد طلب المدد ومددنا القوم صرنا مددا لهم وأمددناهم بغيرنا (sihah;tahdhib)؛ أمددناهم بفاكهة وأمددت الإنسان بطعام (sihah;mufradat)؛ المدد ما أمددت به قومك من طعام أو أعوان والمادة كل شيء يكون مدادا لغيره (tahdhib)؛ مددت الأرض إذا زدت فيها ترابا أو سمادا ومداد كلماته أي عددها وكثرتها (tahdhib)
- **B003** suyun akıp çoğalması ve başka sudan beslenmesi — nehrin akması veya dolup suyunun artması · başka bir akarsuyun suyunu artırıp onu beslemesi · taşkın; suyun arttığı dönemlerdeki bolluk · çalının gövdesinde su yürümek
  مد النهر ومده نهر آخر (maqayis;jamhara;sihah;tahdhib;mufradat)؛ المد السيل وكثرة الماء أيام المدود (sihah;tahdhib)؛ امتد النهر ومد إذا امتلأ وقل ماء ركيتنا فمدتها ركية أخرى (tahdhib)؛ أمد العرفج إذا جرى الماء في عوده (sihah;tahdhib)؛ البحر يمده من بعده سبعة أبحر (mufradat)
- **B004** uzamış süre ve süreyi uzatma — süre, zaman aralığı veya vade · vadeyi ertelemek veya uzatmak · ömrünü uzatmak · yanlışında ona süre tanımak · yolculuğun uzaması · birini oyalayıp çekiştirmek
  أطال مدته (maqayis)؛ أمددت لك في الأجل أنسأتك فيه والمدة الأجل (jamhara)؛ مد الله في عمره ومده في غيه أمهله وطول له ومدة من الزمان برهة منه (sihah)؛ المدة الغاية وأمد الله في عمرك وامتد بهم السير (tahdhib)؛ المدة للوقت الممتد ومددته في غيه (mufradat)
- **B005** yazı sıvısı ve hokkadan kaleme aktarılması — mürekkep · hokkaya su veya mürekkep eklemek · kalemi hokkaya batırıp bir dolumluk mürekkep almak
  المداد ما يكتب به لأنه يمد بالماء ومددت الدواة وأمددتها (maqayis)؛ أمددت الدواة إذا زدت في مائها ونقسها والمدة استمدادك من الدواة (jamhara)؛ المداد النقس ومددت الدواة وأمددتها وأمددت الرجل مدة بقلم (sihah)؛ مدني يا غلام أي أعطني مدة من الدواة (tahdhib)؛ من قولهم مددت الدواة (mufradat)
- **B006** dörtte birlik geleneksel hacim ölçüsü — daha büyük bir ölçünün dörtte biri olan geleneksel hacim ölçüsü
  المد من المكاييل لأنه يمد المكيل بالمكيل مثله (maqayis)؛ المد مكيال معروف والجمع مداد (jamhara)؛ المد بالضم مكيال والصاع أربعة أمداد (sihah)؛ المد مكيال معلوم وهو ربع الصاع ومد وثلاثة أمداد ومدد ومداد كثيرة (tahdhib)؛ المد من المكاييل معروف (mufradat)
- **B007** yarada biriken veya yaradan çıkan irin — yara irinlenmek · yarada biriken veya yaradan çıkan irin
  أمد الجرح صارت فيه مدة وهي ما يخرج (maqayis)؛ أمد الجرح (jamhara;tahdhib)؛ المدة بالكسر ما يجتمع في الجرح من القيح وأمد الجرح صارت فيه مدة (sihah)؛ مدة الجرح (mufradat)
- **B008** deveye içirilen tahıllı su — develere unlu veya tohumlu su içirmek · develere içirilen suyla karıştırılmış ezme tahıl
  مددت الإبل مدا أسقيتها الماء بالدقيق أو بشيء تمده به والاسم المديد (maqayis)؛ مددت الإبل وأمددتها أن تنثر لها على الماء شيئا من الدقيق ونحوه فتسقيها (sihah)؛ مددت الإبل وهو أن يسقيها الماء بالبزر أو الدقيق أو السمسم والمديد شعير يجش (tahdhib)؛ مددت الإبل سقيتها المديد وهو بزر ودقيق يخلطان بماء (mufradat)
- **B009** tuzlalardaki çok tuzlu su [kalıp] — tuzla suyu veya çok yoğun tuzlu su
  مما شذ عن الباب ماء إمدان شديد الملوحة (maqayis)؛ ماء إمدان شديد الملوحة (sihah)؛ الإمدان مياه السباخ والأمدان الماء الملح الشديد الملوحة (tahdhib)

## ل ق ي (root_001372): 84:4 وَأَلْقَتْ, 84:6 فَمُلَٰقِيهِ

- **B001** yüzü veya ağız köşesini eğrilten hastalık — yüzü ya da ağız köşesini eğrilten yüz hastalığı · bu yüz hastalığına tutulmuş kişi
  اللقوة داء يأخذ في الوجه يعوج منه (maqayis)؛ اللقوة داء في الوجه يقال منه لقي الرجل فهو ملقو (sihah)؛ اللقوة داء يأخذ في الوجه يعوج منه الشدق (tahdhib)
- **B002** biçime bağlı adlandırmalar — kuyuya salınınca başka bir kovayı yukarı çeken kova · gagası eğri veya ağız açıklığı geniş dişi kartal
  اللقوة الدلو التي إذا أرسلتها في البئر وارتفعت أخرى شالت معها (maqayis)؛ اللقوة العقاب سميت لاعوجاجها في منقارها (maqayis)؛ اللقوة العقاب الأنثى سميت لقوة لسعة أشداقها (sihah;tahdhib)
- **B003** çabuk gebe kalma — çabuk gebe kalan dişi deve, kadın veya dişi hayvan · çabuk gebe kalan ile çabuk dölleyenin denk gelmesi; birbirine uygun iki kişi
  اللقوة الناقة السريعة اللقاح (maqayis)؛ اللقوة الناقة السريعة اللقاح وفي المثل لقوة صادفت قبيسا (sihah)؛ السريعات اللقح من جميع الحيوان واللقوة من النساء السريعة اللقح (tahdhib)
- **B004** karşılaşma, karşılama veya karşısında bulunma — karşılaşmak, rastlamak veya yüz yüze gelmek · karşılaşmak ve buluşmak · birini karşılamak · onun tam karşısında oturmak · birini belirli bir şeyle karşılamak · kıyamette Tanrı'nın huzuruna çıkma ve O'na dönüş · öncekilerle sonrakilerin toplanıp herkesin yaptıklarıyla yüzleştiği kıyamet günü
  اللقاء الملاقاة وتوافي الاثنين متقابلين (maqayis)؛ اللقيان كل شيئين يلقى أحدهما صاحبه (ayn;tahdhib)؛ التقوا وتلاقوا بمعنى وتلقاه أي استقبله وجلس تلقاءه أي حذاءه (sihah)؛ اللقاء مقابلة الشيء ومصادفته معا (mufradat)
- **B005** bir şeyi atma, bırakma veya birine yöneltme — atmak, fırlatmak veya bırakmak · birine sevgi yöneltmek veya göstermek · çözmesi için birine bilmece niteliğinde söz yöneltmek
  ألقيته نبذته إلقاء (maqayis)؛ ألقيته أي طرحته وألقيت إليه المودة وألقيت عليه ألقية (sihah)؛ ألقيت عليه ألقية كلمة معاياة يلقيها عليه (tahdhib)؛ الإلقاء طرح الشيء حيث تلقاه ثم صار اسما لكل طرح (mufradat)
- **B006** atılmış veya terk edilmiş şey — atılmış, terk edilmiş veya değersiz görülüp bırakılmış şey · eski dönemde kutsal yapının çevresinde dönerken çıkarılıp bırakılan giysi
  الشيء الطريح لقى والملقى لقى (maqayis)؛ اللقى ما ألقى الناس من خرقة ونحوه (ayn)؛ اللقى بالفتح الشيء الملقى لهوانه وجمعه ألقاء (sihah)؛ اللقى ثوب المحرم يلقيه وكل شيء متروك مطروح كاللقطة (tahdhib)
- **B007** iyilik ya da kötülükle karşılaşma — başına sürekli kötülük gelen bahtsız kişi · kişinin karşılaştığı güçlükler ve kötülükler · iyilik ya da kötülükle karşılaşmak
  رجل لقي شقي لا يزال يلقى شرا والألاقي من عسر وشر (ayn)؛ شقي لقي إتباع له (sihah)؛ رجل شقي لقي لا يزال يلقى شرا (tahdhib)؛ يقال لقي فلان خيرا وشرا (mufradat)
- **B008** kervanı pazar öncesinde karşılayıp malını satın alma [kalıp] — pazara gelmeden önce kervanları karşılayıp mallarını satın alma
  نهي عن التلقي أي يتلقى الحضري البدوي فيبتاع منه متاعه بالرخيص (ayn)؛ نهى النبي عن تلقي الركبان والأجلاب والتلقي هو الاستقبال (tahdhib)
- **B009** sırtüstü uzanma — sırtüstü uzanma
  الاستلقاء على القفا وكل شيء فيه كالانبطاح فيه استلقاء (ayn)؛ استلقى على قفاه (sihah)؛ الاستلقاء على القفا وكل شيء كان فيه كالانبطاح ففيه استلقاء (tahdhib)
- **B010** iki tarafı birbirine kavuşturma — iki kişiyi buluşturup bir araya getirmek · bir çubuğun iki ucunu eğip birbirine kavuşturmak
  لاقيت بين فلان وفلان وبين طرفي القضيب ونحوه حتى تلاقيا واجتمعا (ayn)؛ لاقيت بين فلان وفلان ولاقيت بين طرفي قضيب حنيته حتى تلاقيا والتقيا (tahdhib)
- **B011** sözü aktarıp öğretme veya birinden alıp öğrenme — sözü veya okumayı öğretip tekrarlatmak · sözü birinden alıp öğrenmek · sözleri veya vahiy metnini birinden alıp öğrenmek
  الرجل يلقي الكلام والقراءة أي يلقنه وتلقيت الكلام منه أخذته عنه (ayn)؛ إذ تلقونه بألسنتكم أي يأخذه بعض عن بعض (sihah)؛ فتلقى آدم من ربه كلمات أي أخذها عنه وتعلمها (tahdhib)؛ إنك لتلقى القرآن (mufradat)
- **B012** biçime bağlı adlandırmalar — dağ kenarlarındaki çıkıntılar veya iki dağ arasındaki birleşim yeri · rahim ağzındaki dallar veya üreme organındaki dar geçitler
  الملقى إشراف نواحي الجبل والملقاة والجميع الملاقي شعب رأس الرحم (ayn)؛ الملقاة وجمعها الملاقي شعب رأس الرحم وشعب دون ذلك أيضا (tahdhib)؛ الذي رواه الليث إن صح فهو ملتقى ما بين الجبلين والملقات واحدتها ملقة والميم أصلية (tahdhib)

## خ ل و (root_000436): 84:4 وَتَخَلَّتْ

- **B001** içinde ya da üzerinde bir şey bulunmaması — bir şeyin başka bir şeyden yoksun veya sıyrılmış olması · evde ya da yerde kimsenin veya hiçbir şeyin kalmaması · boş yer; ayrıca ayakyolu veya açık arazi · bir yeri boş bulmak
  تعري الشيء من الشيء (maqayis)؛ خلا الشيء يخلو خلوا فهو خال (ayn;sihah;tahdhib)؛ خلت الدار وأخلت (maqayis;tahdhib)
- **B002** başkalarını dışarıda bırakarak baş başa kalmak veya tek şeyle yetinmek — biriyle baş başa buluşmak · biriyle baş başa bir araya gelmek · özel görüşme ya da boş bir oturum yeri istemek · yalnız sütle veya etle yetinmek
  خلوت به خلوة وخلاء (sihah;tahdhib)؛ خلوت إليه إذا اجتمعت معه في خلوة (sihah)؛ استخليت الملك فأخلاني (ayn;tahdhib)؛ خلا فلان على اللبن أو على اللحم (tahdhib)
- **B003** zaman içinde geçip gitmiş olmak — geçmiş çağlar veya geçmiş topluluklar · geçip gitmek · ölmek
  القرون الخالية المواضي (maqayis;sihah)؛ خلا قرن أي مضى (ayn;tahdhib)؛ خلا فيها نذير أي مضى وأرسل (sihah)؛ خلا فلان أي مات (tahdhib)
- **B004** genel hükmün dışında tutmak [kalıp] — birini genel hükmün dışında tutmak · belirli çekimi gerektiren dışlama kalıbı · yalnızca sana öğüt vermiş olmam dışında
  ما في الدار أحد خلا زيد وزيدا (maqayis;ayn;sihah;tahdhib)؛ ما خلا زيدا نصبت لا غير (sihah;tahdhib)؛ خلا أني وعظتك أي إلا أني وعظتك (ayn;tahdhib)
- **B005** artık kınanacak bir yanın yok [kalıp] — artık kınanacak bir yanın yok
  افعل ذاك وخلاك ذم أي عداك (maqayis)؛ وخلاك ذم أي أعذرت وسقط عنك الذم (sihah;tahdhib)
- **B006** bir kişiyle, işle veya suçla bağ ve sorumluluk taşımamak [kalıp] — senden ve sorumluluğundan uzağım · bu işten uzak ve sorumsuz
  أنت خلو منه (ayn)؛ أنا منك خلاء أي براء (sihah)؛ أنا خلي من هذا وخلاء (tahdhib)؛ خلا إذا تبرأ من ذنب (tahdhib)
- **B007** kaygı ve keder taşımamak — kaygısız, tasasız
  الخلي الخالي من الغم (maqayis)؛ الخلي الذي لا هم له (ayn;tahdhib)؛ الخلى الخالى من الهم خلاف الشجي (sihah)
- **B008** engeli kaldırıp serbest bırakmak veya iki tarafı baş başa bırakmak [kalıp] — serbest bırakmak; yolunu açmak · ikisini baş başa bırakmak veya aralarındaki engeli kaldırmak
  خليت عنه أي أرسلته (ayn)؛ خليت عنه خليت سبيله فهو مخلى (sihah)؛ أخليت فلانا وصاحبه وخليت بينهما (ayn)؛ خاليته أي تاركته (tahdhib)
- **B009** eşi ya da çocuğu olmama ve boşanmış sayılma [kalıp] — boşanmış ya da eşi ve çocuğu olmayan kadın · boşama niyetiyle söylenen ayrılık sözü · eşi olmayan erkek
  امرأة خلية كناية عن الطلاق (maqayis;sihah)؛ أنت خلية برية فتطلق بها المرأة (tahdhib)؛ امرأة خلية لا أزواج لهن ولا أولاد (tahdhib)؛ رجل خلي لا نساء لهم (tahdhib)
- **B010** yavrusundan ayrılıp başka yavruya alıştırılan dişi deve — yavrusu ayrılmış ve başka yavruya alıştırılmış dişi deve
  الخلية الناقة تعطف على غير ولدها (maqayis)؛ الخلية الناقة خلت من ولدها ورعت ولد غيرها (ayn)؛ الخلية الناقة تعطف مع أخرى على ولد واحد (sihah)؛ الخلية الناقة تنتج فينحر ولدها (tahdhib)
- **B011** gemi; özellikle büyük veya çekilmeden ilerleyen gemi — gemi, özellikle büyük gemi
  الخلية السفينة (maqayis)؛ الخلية السفينة تسير من ذاتها من غير جذب (ayn)؛ الخلية السفينة العظيمة (sihah)؛ الخلية العظيمة من السفن (tahdhib)
- **B012** arıların barındığı ve bal yaptığı yuva — arıların bal yaptığı yuva veya kovan
  الخلية بيت النحل (maqayis;sihah)؛ الخلى والخلية الموضع الذي يعسل فيه النحل (ayn)؛ الخلية ما يعسل النحل فيه من راقود أو طين أو خشب (tahdhib)
- **B013** ot ve onu biçip kökünden alma — ot veya kökünden sökülmüş bitki · otu biçmek ya da kökünden koparmak · biçilmiş otun konduğu torba · kılıcın kesip biçmesi
  الخلى مقصور هو الحشيش (maqayis;ayn;sihah;tahdhib)؛ الخلاة كل بقلة قلعتها (tahdhib)؛ اختليته وبه سميت المخلاة (ayn;sihah;tahdhib)؛ السيف يختلى أي يقطع (maqayis;sihah)
- **B014** karşı karşıya gelmek veya aradaki barışı sona erdirmek — biriyle güreşmek veya karşı karşıya ayrışmak · düşmanla aradaki ateşkesi ve anlaşmayı sona erdirmek · birine karşı çıkmak
  خاليت فلانا إذا صارعته (ayn;tahdhib)؛ خلاني فلان مخالاة أي خالفني (tahdhib)؛ خاليت العدو أي تركت ما بيني وبينه من الموادعة (tahdhib)؛ عدو مخال أي ليس له عهد (tahdhib)
- **B015** alay etmek veya kandırmak [kalıp] — biriyle alay etmek · birini kandırmak
  خلا به إذا سخر به (maqayis)؛ خلوت به أي سخرت به (sihah)؛ فلان خلا لفلان أي خادعه (ayn)؛ يخلو بفلان إذا خادعه (tahdhib)
- **B016** koruyucusuz olduğu için kolay hedef olan kimse veya şey — koruyucusu olmadığı için kolay hedef olan kimse veya şey
  الخلاة ممن يطمع فيه ولا حافظ له (maqayis)

## ء ن س (root_000059): 84:6 ٱلْإِنسَٰنُ

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

## ك د ح (root_001287): 84:6 كَادِحٌ, 84:6 كَدْحًا

- **B001** zahmetle çalışıp çabalamak — zahmetli çalışma, sürekli çabalama ve kazanma · çalışıp kazanmak; kendi geçimi için çabalamak · zahmetle çalışan veya kazanan kimse · bir işte didinip yorulmak · bu dünya veya ölüm sonrası yaşam için çalışıp çabalamak · ailesinin geçimini sağlamak için çalışıp kazanmak · başkaları ya da ailesi için kazanç sağlamak · yaratıcısına doğru iyi ya da kötü işler yaparak zahmetle çalışıp çabalamak
  كدح إذا كسب فهو كادح (maqayis)؛ اكتسب وكدح لدنياه وكدح لآخرته (jamhara)؛ العمل والسعي والخدش والكسب (sihah)؛ عمل الإنسان من الخير والشر بمعنى يسعى ونصب إلى ربك نصبا والسعي والدؤوب في العمل (tahdhib)؛ السعي والعناء (mufradat)
- **B002** çizmek ve çizik ya da ısırık izi bırakmak — çizme; çizik ya da hafif ısırık izi · çizmek veya iz bırakmak · yüzünü çizmek · çizik veya ısırık izleri · derisi çizilmek · çizme, çizik oluşturma · başka eşeklerin ısırık izlerini taşıyan eşek
  أصل صحيح يدل على تأثير في شيء وكدحه إذا خدشه وحمار مكدح قد عضضته الحمر (maqayis)؛ تكدح جلده إذا تخدش وكدوح وخدوش وحمار مكدح آثار من عض الفحول (jamhara)؛ كدح وجهه وبه كدح وكدوح أي خدوش والكدح أكثر من الخدش والتكديح التخديش وتكدح الجلد (sihah)؛ الكدح دون الكدم بالأسنان والكدح بالحجر والحافر والكدوح أثر الخدوش وكل أثر من خدش أو عض (tahdhib)؛ يستعمل استعمال الكدم في الأسنان والكدح دون الكدم (mufradat)
- **B003** kişinin yüzünü lekelemek veya işin gidişini bozmak [kalıp] — birinin yüzünü çirkinleştirmek veya lekelemek · bir işin görünümünü ya da gidişini bozmak
  كدح فلان وجه فلان إذا ما عمل به ما يشينه وكدح وجه أمره إذا أفسده (tahdhib)

## ء ت ي (root_000009): 84:7 أُوتِىَ, 84:10 أُوتِىَ

- **B001** gelmek, ulaşmak — gelmek veya ulaşmak · ona gitmek veya yanına varmak · geciktiğini düşünüp gelmesini istemek
  أتى يأتي أتيا (jamhara)؛ الإتيان المجئ (sihah)؛ أتاني فلان إتيانا وأتيا وأتية وأتوة (tahdhib;maqayis)؛ الإتيان مجيء بسهولة (mufradat)
- **B002** vermek; getirip sunmak — vermek; bir şeyi getirip sunmak
  آتى يؤتي إيتاء في معنى أعطى (jamhara)؛ آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به (sihah)؛ الإتياء الإعطاء (tahdhib)؛ الإيتاء الإعطاء (mufradat;maqayis)
- **B003** uygun yoldan ele almak ve elverişli hale gelmek — işin uygun yönü ve tutulacak yolu · uyma ve razı olma · bir şeyin ona elverişli hale gelmesi · ihtiyacını uygun yoldan ve incelikle yürütmek
  أتيت الأمر من مأتاته (sihah;maqayis)؛ آتيته على ذلك الأمر مواتاة إذا وافقته وطاوعته (sihah)؛ آتيت فلانا على أمره مؤاتاة وهو حسن المطاوعة (maqayis)؛ تأتى له الشيء أي تهيأ (sihah)؛ تأتى فلان لحاجته إذا ترفق لها (tahdhib)
- **B004** su kanalı açmak ve akışı yönlendirmek — su kanalı; suyu tutan odun ve yaprak birikintisi · bu suya yol açıp akışını yönlendirmek
  أت لمائك أي سهل له سبيلا وذلك السبيل الأتي (jamhara)؛ الأتي الجدول يؤتيه الرجل إلى أرضه (sihah)؛ كل جدول ماء أتي (tahdhib)؛ أت لهذا الماء أي سهل جريه (maqayis)؛ الأتي ما وقع في النهر من خشب أو ورق مما يحبس الماء (maqayis)
- **B005** başka bölgeden gelen sel [kalıp] — yağmur alan başka bir bölgeden gelen sel
  الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك (jamhara)؛ سيل أتي وأتاوي إذا جاءك ولم يصبك مطره (sihah)؛ المسيل الذي يأتي من بلد قد مطر فيه إلى بلد لم يمطر فيه أتي (tahdhib)؛ السيل المار على وجهه أتي وأتاوي (mufradat)؛ الأتي أيضا السيل الذي يأتي من بلد غير بلدك (maqayis)
- **B006** topluluğa yabancı kimse [kalıp] — içinde bulunduğu topluluğa mensup olmayan yabancı adam
  رجل أتي وأتاوي وهو الغريب (jamhara)؛ الاتي أيضا والاتاوى الغريب (sihah)؛ إنما هو أتي فينا (tahdhib)؛ به شبه الغريب فقيل أتاوي (mufradat)؛ رجل أتي أي غريب في قوم ليس منهم وأتاوي كذلك (maqayis)
- **B007** gelişip bol ürün vermek — ekin ve hurmanın gelişmesi, ürünü ve bol verimi · çalkalanan tulumun yağının ortaya çıkması
  أتاء هذا النخل أي ثمره وكذلك الزرع (jamhara)؛ الاتاء البركة والنماء وحمل النخل (sihah)؛ جاء أتوه (sihah;mufradat)؛ إتاء النخلة ريعها وزكاؤها وكثرة ثمارها (tahdhib)؛ الإتاء نماء الزرع والنخل وأتى الماء إتاء أي كثر (maqayis)
- **B008** ödenen vergi; rüşvet — vergi veya baş vergisi; rüşvet · ona rüşvet vermek
  الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك (jamhara)؛ الاتاوة الخراج والجمع الاتاوي (sihah)؛ الإتاوة الخراج وجمعها الأتاوى والإتاوات (tahdhib)؛ أتوته أتوة إذا رشوته إتاوة وهي الرشوة (tahdhib)
- **B009** devenin ön ayaklarını geri getirişi [kalıp] — devenin yürürken ön ayaklarını geri getirişi
  ما أحسن أتو قوائم الناقة وأتيها في السير (jamhara)؛ ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير (sihah)؛ ما أحسن أتو يديها وأتي يديها يعني رجع يديها (tahdhib)
- **B010** işlek ana yol, son sınır ve karşı hizası — yarışın son sınırı; işlek ana yol veya yol kavşağı · yarışın son sınırı veya yolun ana kesimi · bir evin karşısında veya aynı hizasında
  الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل (sihah)؛ الميتاء الطريق العامر ومجتمع الطريق (sihah)؛ داري بميتاء دار فلان وميداء دار فلان أي تلقاء داره ومحاذية لها (sihah)؛ طريق ميتاء مسلوك وميتاء الطريق وميداؤه محجته (tahdhib)
- **B011** felakete uğramak, kaybetmek veya düşmanca ele geçirilmek [kalıp] — ölüm, ağır hastalık, bela veya kırığa uğramak · malı yok olmak · uğruna öldürülmek, götürülmek veya yenilmek · düşman yaklaşmış olmak
  أتى على فلان أتو أي موت أو بلاء أصابه (tahdhib)؛ الأتو المرض الشديد أو كسر يد أو رجل أو موت (tahdhib)؛ أتي على يد فلان إذا هلك له مال (tahdhib)؛ يؤتى دونه أي يذهب به ويغلب عليه (tahdhib)؛ أتي فلان إذا أطل عليه العدو (tahdhib)؛ الإتيان يقال في الخير وفي الشر (mufradat)
- **B012** dişi devenin çiftleşmek istemesi [kalıp] — dişi devenin çiftleşmek için erkek deve istemesi
  استأتت الناقة استئتاء مهموز أي ضبعت وأرادت الفحل (sihah)
- **B013** etkili ve işini yürüten adam [kalıp] — etkili ve işini yürütebilen adam
  رجل أتي إذا كان نافذا (maqayis)

## ك ت ب (root_001283): 84:7 كِتَٰبَهُۥ, 84:10 كِتَٰبَهُۥ

- **B001** bir şeyi başka bir şeye katıp birleştirme — bir şeyi başka bir şeye katıp birleştirme · su tulumunu dikerek birleştirmek · katırın üreme organının dudaklarını halka veya kayışla birleştirmek · dişi devenin burun deliklerini iplikle dikmek veya bağlamak · dişi devenin memelerini bağlamak · su tulumunun ağzını bağıyla sıkıca kapatmak · kayışın iki yüzünü birleştiren boncuk · bir arada duran atlı veya askerî birlik · atların toplanması · askerleri birlik birlik düzenlemek
  أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)
- **B002** yazma ve yazılı metin — kitabı yazmak veya kopyalamak · yazılı metin veya üzerinde yazı bulunan sayfa · yazma işi ve yazıcılık · kitabı yazmak veya kopyalamak · ona şiiri söyleyerek yazdırmak · birinden kendisi için bir şey yazmasını istemek · çocuğa yazmayı öğretmek · yazı öğretmeni veya yazı öğretilen yer · öğretim yerindeki çocuklar veya onların topluluğu
  الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)
- **B003** bağlayıcı olarak hükme bağlama ve belirleme — yükümlülük, hüküm veya yazgı · size zorunlu kılındı · Tanrı belirledi, karara bağladı veya zorunlu kıldı
  الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)
- **B004** adını sicile yazma veya bir gruba dâhil etme — pay veya geçim tahsisatı için kaydolma · adını pay kaydına veya yönetim siciline yazdırmak · bizi tanıklar topluluğuna kat
  الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)
- **B005** özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi — kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi · özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi · köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak · kölenin özgürlüğünü satın almak için yaptığı sözleşme
  المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)

## ي م ن (root_001698): 84:7 بِيَمِينِهِۦ

- **B001** uğur ve iyilik getirme, bunları umma — uğur, iyilik artışı ve mutluluk · uğurlu ve iyilik getiren · topluluğuna uğur ve iyilik getirdi · uğur ve iyilik getiren kimse · onu uğurlu sayıp iyilik umdu · onun görüşünü uğurlu sayıp iyilik umuyor · mutluluk ve iyi yazgı sahipleri · mutluluğa ve Tanrı'ya yakınlığa ulaştıran araç sayılan Kara Taş
  واليمن البركة وهو ميمون (maqayis)؛ يمن الرجل فهو ميمون والميمن الذي أتى باليمن والبركة (ayn)؛ اليمن البركة وتيمنت به تبركت (sihah)؛ اليمن نظير البركة ويمن الرجل فهو ميمون (tahdhib)؛ أصحاب اليمين أصحاب السعادات والميامن واستعير اليمين للتيمن والسعادة (mufradat)
- **B002** sağ el ve sağ yön — sağ el veya sağ yön · yanındakileri sağa götür · sağ taraf veya sağ yön · solun karşıtı olan sağ taraf · sağa doğru ilerledi · iki sağ eliyle verdiği azık · sağ eller
  فاليمين يمين اليد (maqayis)؛ واليمين اليد اليمنى والأيمان جمعه (ayn)؛ اليمنة خلاف اليسرة والأيمن والميمنة خلاف الأيسر والميسرة (sihah)؛ يقال لليد اليمنى يمين وأخذ فلان يمينا وأخذ يسارا ويامن بأصحابك (tahdhib)؛ اليمين أصله الجارحة والميمنة ناحية اليمين (mufradat)
- **B003** kutsal tanıklı ant ve söz güvencesi — ant veya kutsal tanıklı söz güvencesi · antlar ve bağlayıcı sözler · Tanrı adına ant olsun · senin adına ant olsun · Tanrı adına edilen ant · Tanrı adına ant olsun diyen kısaltılmış söz
  واليمين الحلف (maqayis)؛ واليمين من القسم والأيمان جماعته وأيمن حرف وضع للقسم (ayn)؛ اليمين القسم الجمع أيمن وأيمان وأيمن الله اسم وضع للقسم (sihah)؛ الأصل يمين الله وأيمن الله وليمنك (tahdhib)؛ اليمين في الحلف مستعار من اليد (mufradat)
- **B004** güç, savunma ve güçlü doğruluk dayanağı — güç, yetki veya doğruluğun güçlü tarafı · dinî gerekçe veya doğruluk yönünden · güçle veya doğruluğa dayanarak · güç kullanarak engelledi ve savdı
  اليمين القوة (maqayis)؛ واليمين القوة وعن اليمين من قبل الدين (sihah)؛ باليمين أي بالقوة وقيل بالقوة والحق وتخدعوننا بأقوى الأسباب من قبل الدين (tahdhib)؛ لأخذنا منه باليمين أي منعناه ودفعناه (mufradat)
- **B005** Yemen ülkesi, halkı ve ona aidiyet — Yemen ülkesi veya Yemen yönü · Yemenli veya Yemen'e ait · Yemenli veya Yemen'e ait · Yemenli kadın veya Yemen'e ait dişil varlık · Yemenli kadın veya Yemen yönünden olan · Yemen dokumasından yapılmış örtü · Yemen'e mensup oldu · Yemen yönüne gitti veya Yemen'e vardı
  وكذلك اليمن وهو بلد ورجل يماز وسيف يمان (maqayis)؛ واليمن أرض وجيل من الناس واليمن ما كان على يمين القبلة (ayn)؛ اليمن بلاد للعرب والنسبة إليها يمنى ويمان وتيمن تنسب إلى اليمن واليمنة البردة من برود اليمن (sihah)؛ تيامن القوم وأيمنوا إذا أتوا اليمن وقولهم رجل يمان منسوب إلى اليمن واليمنة ضرب من برود اليمين (tahdhib)
- **B006** antlaşma bağı veya kesin sahiplik bildiren sağ el sözleri — aranda antlaşma bulunan bağlı kişi · kesin sahip olduğum ve tasarrufumda bulunan şey
  ومولى اليمين هو من بينك وبينه معاهدة وملك يميني أنفذ وأبلغ من قولهم في يدي (mufradat)
- **B007** ölmek; mezarda sağ yana yatırılmayla ilişkilendirilen kullanım — öldü; mezarda sağ yanına yatırılmasıyla ilişkilendirilen kullanım
  والتيمن الموت يقال تيمن فلان تيمنا إذا مات والأصل فيه أنه يوسد يمينه إذا مات في قبره (tahdhib)

## ح س ب (root_000318): 84:8 يُحَاسَبُ, 84:8 حِسَابًا

- **B001** sayarak nicelik belirleme — nesneyi saymak ve niceliğini çıkarmak · sayma ve nicelik belirleme işlemi · sayma işlemi · sayı yoluyla belirleme · belirli sayı düzeni ve zaman ölçüsü · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · sayıp değerlendiren ve gözeten
  الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان
- **B002** öyle olduğunu sanmak — öyle sanmak ve zihnen öyle olduğuna hükmetmek · sanı ve kesin olmayan yargı
  الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين
- **B003** gereksinimi karşılayacak kadar yetmek — bu sana yeter; bununla yetin · Tanrı bize yeter · bu bana yetti · ona yetecek veya onu hoşnut edecek kadar vermek · yeterli ya da bol armağan · ölçmeden, denetlemeden veya kısmadan; beklenenden fazla · soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü
  الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا
- **B004** atalardan gelen saygınlık ve iyi işler birikimi — atalardan gelen saygınlık ve övünülecek işler · soylu, saygın veya eli açık kişi · soyluluk ya da yeterlik diye yorumlanan şiir sözü
  الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه
- **B005** Tanrı katında karşılığını beklemek — bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek · Tanrı katında karşılık umularak yapılan iş
  احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى
- **B006** işi gözetme, kötü davranışı sorgulama ve kamusal denetim — kötü davranışından dolayı kınamak ve yaptığını sorgulamak · işi iyi çekip çevirmek ve gözetmek · kentte kamu düzenini ve davranışları gözeten görevli
  حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر
- **B007** kısa ok veya yukarıdan gelen yıkıcı gönderim — kısa oklar veya atılan küçük nesneler · gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey
  الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا
- **B008** yalıtık adlandırmalar — küçük yastık · deriden yapılmış veya baş altına konan yastık · birini yastığa oturtmak veya başına yastık koymak · yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış
  الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة
- **B009** deri veya tüyde karışık ak, kızıl ve koyu görünüm — derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve · koyu zemin üstünde bozluk ya da kızıla çalan karalık
  الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة
- **B010** yalıtık adlandırmalar — haberi sorup izini sürmek · birinin elinde ne olduğunu sınayıp öğrenmek
  بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها

## ي س ر (root_001694): 84:8 يَسِيرًا

- **B001** kolaylık; kolay ve hazır duruma gelme ya da getirme — kolaylık, güçlüğün karşıtı · kolay olan, güç olmayan · kolaylaşıp hazır duruma gelmek · kolaylaştırıp hazırlamak · birine anlayış gösterip kolaylık sağlamak · kolay olan · kolay, güç olmayan
  اليسر: ضد العسر (maqayis;mufradat)؛ الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ (sihah)؛ تيسر واستيسر أي تسهل وتهيأ، وأيسرت المرأة وتيسرت في كذا أي سهلته وهيأته (mufradat)؛ ياسره أي ساهله (sihah)
- **B002** az miktar veya kısa süre — az miktar veya kısa süre
  اليسير: القليل، وشيء يسير أي هين (sihah)؛ واليسير يقال في الشيء القليل (mufradat)
- **B003** maddi bolluk ve varlıklı olma — maddi bolluk ve varlıklılık · varlıklılık ve maddi güç · varlıklılık · varlıklı duruma gelmek
  الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى (sihah)؛ الميسرة واليسار عبارة عن الغنى (mufradat)
- **B004** sol el veya sol yön — sol el veya sol yön · soldaki, sağın karşıtı · sol taraf · sola yönelip ilerlemek · iki elini de kullanabilen kişi
  اليسار لليد، تياسروا إذ أخذوا ذات اليسار، وياسروا (maqayis)؛ الأيسر: نقيض الأيمن، والميسرة خلاف الميمنة، واليسار خلاف اليمين، والياسر نقيض اليامن، ورجل أعسر يسر للذي يعمل بكلتا يديه (sihah)
- **B005** yumuşak başlı ve harekette uyumlu olma — yumuşak başlı ve çabuk uyum gösteren · hafif bacaklar · hayvanın bacaklarını iyi aktarması
  اليسرات: القوائم الخفاف؛ فرس حسن التيسور أي حسن نقل القوائم؛ رجل يسر ويسر أي حسن الانقياد (maqayis)؛ ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس (ayn)؛ اليسرات: القوائم الخفاف، ودابة حسن التيسور أي حسن نقل القوائم (sihah)
- **B006** koyunların süt ve yavru bakımından çoğalması [kalıp] — koyunların sütü ve yavrusu çoğalmak
  يسرت الغنم إذا كثر لبنها ونسلها (maqayis;sihah)
- **B007** fal oklarıyla oynanan paylaştırmalı talih oyunu — fal oklarıyla oynanan geleneksel talih oyunu · fal okları oyununa katılmak için toplananlar · fal oklarıyla oynayan kişi · fal oklarıyla oynayan kişi · topluluğun deveyi kesip parçalarını paylaştırması · deveyi kesip oyun düzenine göre paylaştırmak
  الأيسار: القوم يجتمعون على الميسر، واحدهم يسر؛ والميسر: القمار (maqayis)؛ الميسر: قمار العرب بالأزلام؛ الياسر: اللاعب بالقداح؛ اليسر والياسر بمعنى والجمع أيسار؛ يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها (sihah)
- **B008** ayrı avuç çizgileri veya uyluk damgası — avuç içindeki birbirine bitişmeyen çizgiler · uyluklardaki damga
  اليسرة: أسرار الكف إذا كانت غير ملزقة (maqayis;sihah)؛ اليسرة أيضا: سمة في الفخذين (sihah)
- **B009** aşağı doğru burma veya yüz hizasına saplama — sağ eli gövdeye çekerek aşağı doğru burma · yüz hizasına yöneltilen saplama
  اليسر: الفتل إلى أسفل، وهو أن تمد يمينك نحو جسدك؛ والطعن اليسر: حذاء وجهك (sihah)
- **B010** yer ve kişi adı kullanımları — bir yerin adı · çöl bölgesindeki bir geçidin adı · anlatıda geçen bir kişinin adı
  يسر: مكان (maqayis)؛ اليسر أيضا: دخل لنبى يربوع بالدهناء (sihah)؛ يسار الكواعب هو اسم عبد (sihah)
- **B011** genç erkek — genç erkek, delikanlı
  اليسار: الفتى (maqayis)

## ق ل ب (root_001248): 84:9 وَيَنقَلِبُ

- **B001** yürek ve iç merkez — yürek; akıl, kavrayış, ruh, bilgi, cesaret ve duygusal incelik merkezi
  القلب قلب الإنسان وغيره (maqayis;jamhara)؛ القلب مضغة من الفؤاد معلقة بالنياط (ayn;tahdhib)؛ القلب الفؤاد وقد يعبر به عن العقل (sihah)؛ يعبر بالقلب عن الروح والعلم والشجاعة (mufradat)
- **B002** öz ve katışıksız seçkin kısım — bir şeyin özü, en seçkin ve katışıksız kısmı · saf ve katışıksız Arap; soyu karışmamış kişi · Kur'an'ın merkezi sayılan bölüm; kaynakta Yasin ile açıklanan adlandırma
  خالص كل شيء وأشرفه قلبه (maqayis)؛ جئتك بهذا الأمر قلبا أي محضا لا يشوبه شيء (ayn;tahdhib)؛ عربي قلب أي خالص (jamhara;sihah;tahdhib)؛ قلب القرآن ياسين (ayn;tahdhib)
- **B003** hurma ağacının yumuşak iç sürgünü — hurma ağacının beyaz ve yumuşak iç sürgünü · ağaçların veya taze bitkilerin yumuşak iç kısımları
  قلب النخلة شحمتها (ayn)؛ قلوب الشجر ما رخص من عروقه وأجوافه (ayn;tahdhib)؛ قلب النخلة جمارها (tahdhib)؛ قلبت النخلة نزعت قلبها (maqayis;jamhara;sihah)
- **B004** çevirmek ve yönünü değiştirmek — bir şeyi çevirdi, ters yüz etti veya yönünü değiştirdi · birini yöneldiği taraftan çevirdi veya saptırdı · işleri yönetmek için düşünüp evirip çevirmek · gönülleri ve bakışları bir görüşten başka görüşe çevirmek · tehdit veya öfke anında gözünü ya da göz bebeğini çevirmek · ekmeğin diğer yüzünün çevrilme zamanı geldi · toprağı çevirmeye yarayan demir tarım aleti · anasının veya aslının renginden farklı renkte olan · satın almadan önce kusurlarını görmek için kişiyi inceleyip çevirmek
  قلبت الثوب قلبا (maqayis)؛ قلبت الشيء كببته وقلبته بيدي تقليبا (maqayis;jamhara;sihah)؛ القلب تحويلك الشيء عن وجهه (ayn;tahdhib)؛ قلب الشيء تصريفه وصرفه عن وجه إلى وجه (mufradat)؛ تقليب الأمور تدبيرها والنظر فيها (mufradat)
- **B005** dönüş ve akıbet — dönüp ayrılma veya geri dönüş · varış yeri, dönüş yeri, sonuç veya akıbet · öğretmen çocukları evlerine geri gönderdi
  المنقلب مصيرك إلى الآخرة (ayn;tahdhib)؛ المنقلب يكون مكانا ويكون مصدرا (sihah)؛ الانقلاب الانصراف (mufradat)
- **B006** pişmanlıkla avuç çevirmek [kalıp] — pişmanlıkla avuçlarını çevirdi veya ellerini çırpıp durdu
  تقليب اليد عبارة عن الندم؛ فأصبح يقلب كفيه
- **B007** kaplanmamış kuyu — içi henüz örülmemiş kuyu; bazı aktarımda genel kuyu adı
  القليب البئر قبل أن تطوى (maqayis;ayn;sihah;tahdhib;mufradat)؛ القليب الركي مذكر (jamhara)؛ القليب اسم من أسماء الركي مطوية أو غير مطوية (tahdhib)
- **B008** tek parça bilezik veya halka süs — bilezik ya da tek parça halka biçimli süs eşyası
  القلب من الأسورة ما كان قلبا واحدا (maqayis;sihah)؛ القلب من الأسورة ما كان قلدا واحدا (ayn;tahdhib)؛ القلب السوار (jamhara)؛ القلب المقلوب من الأسورة (mufradat)
- **B009** takıya benzetilen beyaz yılan — halka biçimli süse benzetilerek adlandırılan beyaz yılan
  شبه الحية بالقلب من الحلى فسمى قلبا (maqayis)؛ القلب الحية البيضاء شبهت بالقلب (ayn)؛ القلب أيضا حية تشبه به (sihah)
- **B010** Akrep'in Yüreği yıldızı [kalıp] — Akrep'in Yüreği diye bilinen parlak yıldız veya ay konağı
  القلب نجم يقولون إنه قلب العقرب (maqayis)؛ القلب نجم من منازل القمر (jamhara)؛ قلب العقرب منزل من منازل القمر وهو كوكب نير (sihah)
- **B011** yürekle ilişkili hastalık ve hastalık yokluğu kalıbı — deveyi veya yüreği tutan hastalık · onda hastalık, kusur ya da gizli zarar yok
  القلاب داء يصيب البعير فيشتكى قلبه (maqayis)؛ ما به قلبة أي لا داء ولا غائلة (ayn;tahdhib)؛ القلاب داء يأخذ البعير (sihah)؛ ما به قلبة علة يقلب لأجلها (mufradat)
- **B012** dudak dönüklüğü — dudakta dönüklük; dudağı dönük kişi veya dönük dudak
  القلب انقلاب الشفة وهي قلباء وصاحبها أقلب (maqayis)؛ الأقلب من في شفتيه انقلاب وشفة قلباء (ayn)؛ القلب بالتحريك انقلاب الشفة (sihah)؛ القلب انقلاب في الشفة (tahdhib)
- **B013** Yemen kullanımında kurt adı — Yemen'e nispet edilen dilde kurt adı
  القليب والقلوب فيقال إنه الذئب (maqayis)؛ القلوب الذئب يمانية (ayn)؛ القليب الذئب لغة يمانية (jamhara)؛ القليب وكذلك القلوب (sihah)؛ القليب والقلوب الذئب بلغة أهل اليمن (tahdhib)
- **B014** biçim verme kabı — içine dökülerek veya yerleştirilerek bir şeye biçim verilen kap ya da araç
  القالب دخيل (ayn;tahdhib)؛ القالب الذي يصب فيه الشيء من صفر أو غيره (jamhara)؛ القالب قالب الخف وغيره (sihah)
- **B015** kızarmış ham hurma — kızarmış ham hurma · ham hurma kırmızı renge döndü
  القالب بالكسر البسر الأحمر (sihah)؛ القالب البسر الأحمر يقال منه قلبت البسرة إذا احمرت (tahdhib)
- **B016** yüreğinden vurmak — birini yüreğinden vurdu veya yüreğine isabet ettirdi
  قلبته أي أصبت قلبه (sihah)؛ قلبت فلانا إذا أصبت قلبه فهو مقلوب (tahdhib)

## ء ه ل (root_000064): 84:9 أَهْلِهِۦ, 84:13 أَهْلِهِۦ

- **B001** yakın çevre ve bağlı topluluk — yakınlık, ev, din veya başka bir bağla birleşen insan çevresi · bir erkeğin eşi ve en yakın insanları · evin sakinleri ve eve bağlı sayılan kişiler · Islam'a bağlı olan kişiler · yakın çevre veya ev halkı için çoğul biçimler
  أهل الرجل زوجه وأخص الناس به؛ أهل البيت سكانه؛ أهل الإسلام من يدين به (maqayis;ayn;tahdhib)؛ أهل الرجل من يجمعه وإياهم نسب أو دين أو صناعة وبيت وبلد (mufradat)؛ أهل الرجال وأهل الدار (sihah)
- **B002** evlenip yakın çevre edinmek — evlenmek ve eş edinmek · bir kadını eş olarak almak · Allah sana cennette eş ve yakın çevre versin
  التأهل التزوج (maqayis;ayn)؛ أهل فلان يأهل أهولا أي تزوج وكذلك تأهل (sihah)؛ أهل الرجل يأهل أهولا إذا تزوج للأنس الذي بين الزوجين (tahdhib)؛ تأهل إذا تزوج ومنه آهلك الله في الجنة أي زوجك فيها وجعل لك فيها أهلا (mufradat)
- **B003** uygun ve layık olmak — bir şey için uygun ve yaraşır olmak · saygı gösterilmeye ve bağışlamaya layık olan · onu bu iş için uygun ve hazır hale getirdi · bu işi hak etmiş sayılan kimse; kullanımı tartışmalı
  أهلته لهذا الأمر تأهيلا (maqayis;ayn;tahdhib)؛ فلان أهل كذا أو كذا (ayn;tahdhib)؛ هو أهل التقوى وأهل المغفرة أي أهل لأن يتقى وأهل لمغفرة من اتقاه (ayn;tahdhib)؛ فلان أهل لكذا أي خليق به (mufradat)؛ فلان أهل لكذا ولا تقل مستأهل (sihah)
- **B004** sakinli ve alışılmış yerleşiklik — sakinleri bulunan yer · içinde yaşayanları olan yer · eskiden içinde yaşanmış konaklama yerleri · insanlara ve yerleşim yerlerine alışmış, evcil · onunla yakınlık duydum ve yabancılık çekmedim · insanları ve sakinleri bulunan hale geldi
  مكان آهل مأهول (maqayis)؛ مكان مأهول فيه أهل ومكان آهل له أهل (ayn;tahdhib)؛ منزل آهل أي به أهله (sihah)؛ كل شيء من الدواب وغيرها إذا ألف مكانا فهو آهل وأهلي (maqayis;tahdhib)؛ كل دابة ألف مكانا يقال أهل وأهلي (mufradat)؛ أهلت به إذا استأنست به (sihah;tahdhib)
- **B005** rahatlatan karşılama sözü — geniş yer ve yakın insanlar buldun; rahat ol, yabancılık çekme
  مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش (sihah)؛ مرحبا وأهلا ومعناه نزلت رحبا أي سعة وأتيت أهلا لا غرباء (tahdhib)؛ مرحبا وأهلا في التحية للنازل بالإنسان أي وجدت سعة مكان عندنا (mufradat)
- **B006** eritilmiş yemeklik yağ — kuyruk yağı, iç yağı, don yağı, sıvı yağ veya katık yapılan yağlı madde · bu yağlı maddeden alan veya onu yiyen kimse · bu yağlı maddeyi yemeğe katık yaptı
  الأصل الآخر الإهالة وهي الألية ونحوها يؤخذ فيقطع ويذاب (maqayis)؛ الإهالة الودك والمستأهل الذي يأخذ الإهالة أو يأكلها (sihah)؛ الإهالة هي الشحم والزيت قط؛ كل ما اؤتدم به من زبد وودك شحم ودهن سمسم وغيره فهو إهالة؛ استأهل الرجل إذا ائتدم بالإهالة (tahdhib)

## س ر ر (root_000697): 84:9 مَسْرُورًا, 84:13 مَسْرُورًا

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

## و ر ي (root_001642): 84:10 وَرَآءَ

- **B001** iç organları bozan ya da akciğeri tutan hastalık — iç organları ya da akciğeri tutan hastalık · içi hastalıktan bozuldu; irin içini yedi · içi bu hastalıkla bozulmuş kimse · akciğeri tutan hastalık · akciğerinden yaraladı · yara, onu yoklayana bu hastalığı geçirdi
  الورى داء يداخل الجسم (maqayis)؛ وري جوف فلان فهو موري إذا فسد من داء يصيبه (jamhara)؛ ورى القيح جوفه يريه وريا: أكله (sihah)؛ الورى داء يصيب الرجل والبعير في أجوافهما (tahdhib)؛ الوارية داء يأخذ في الرئة (ayn;tahdhib)
- **B002** çakmaktan ateş çıkarma ve sönük ateşi harlama — çakmaktan ateş çıktı · sönük ateşi harlayıp yükseltti · ateş yakmaya yarayan araç
  ورى الزند خرجت ناره (maqayis;jamhara;sihah;mufradat)؛ إذا أخرج الزند النار قيل وري الزند يري (tahdhib)؛ أوريت النار إذا كانت خامدة فأججتها (ayn)؛ أريت النار تأرية إذا رفعتها (tahdhib)
- **B003** çakmak benzetmesiyle başarma, yardım görme ya da savunma [kalıp] — giriştiği işte başarıya ulaşan · sende yardım, içten öğüt ve cömertlik buldum · onu destekledi ve savundu
  ورت بك زنادي إذا أنجده وأعانه (jamhara)؛ وريت بك زنادي أي رأيت منك ما أحب من النصح والنجابة والسماحة (ayn)؛ لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب (tahdhib;mufradat)؛ لوريت عن مولاك أي نصرته ودفعت عنه (tahdhib)
- **B004** yağlı ve semiz olma; iliğin dolgunlaşması — yağlı ve semiz · semiz dişi deve · kemik iliği dolup yoğunlaştı
  اللحم الواري: السمين (maqayis;mufradat)؛ الواري الشحم السمين والوري مثله (ayn)؛ ناقة وارية بغير همز: سمينة (jamhara)؛ وري المخ إذا اكتنز وناقة وارية أي سمينة ولحم وري أي سمين (sihah)
- **B005** gizleme, gizlenme ve başka anlam gösterme — şeyi gizleyip gözden sakladı · gizlendi, gözden kayboldu · haberi gizleyip başka bir anlamı öne çıkarma · niyetini gizlemek için başka bir şey söyledi
  التورية إخفاء الخبر وعدم إظهار السر تقول وريته تورية (ayn)؛ واريت الشيء أي أخفيته وتوارى هو أي استتر (sihah)؛ التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره (tahdhib)؛ واريت كذا إذا سترته وتوارى استتر (mufradat)
- **B006** konuma göre arka, ön, öte ya da öbür yan — arka, ön, öte ya da öbür yan · geri çekil; yana açıl
  وراءك يكون من خلف ويكون من قدام (maqayis)؛ وراء ممدود خلاف قدام (ayn)؛ وراء بمعنى خلف وقد يكون بمعنى قدام وهي من الأضداد (sihah)؛ الوراء الخلف ويكون الأمام وبما وراءه أي بما سواه (tahdhib)؛ وراء زيد كذا لمن خلفه ويقال لما كان قدامه أو في أي جانب من الجدار (mufradat)
- **B007** torun — torun, özellikle oğlun oğlu
  الوراء ولد الولد (maqayis;sihah;mufradat)؛ الوراء ممدود ولد الولد (ayn)؛ الوراء ابن الابن (tahdhib)
- **B008** yeryüzündeki bütün yaratılmışlar — yeryüzündeki yaratılmışlar
  الورى: الخلق (maqayis;sihah;tahdhib)؛ الورى مقصور الأنام الذي على ظهر الأرض (ayn)؛ الورى الأنام الذين على وجه الأرض في الوقت (mufradat)
- **B009** sapıklık çakmağından kıvılcım çıkarmaya çalışma [kalıp] — sapıklık çakmağından kıvılcım çıkarmaya çalışıyor
  فلان يستوري زناد الضلالة

## ظ ه ر (root_000970): 84:10 ظَهْرِهِۦ

- **B001** açığa çıkıp belirginleşmek — açığa çıkmak, belirip anlaşılır olmak · görünür ve dışta olan
  ظهر الشيء إذا انكشف وبرز (maqayis)؛ الظهور بدو الشيء الخفي (ayn;tahdhib)؛ ظهر الشيء ظهورا تبين (sihah)؛ أن يحصل شيء على ظهر الأرض فلا يخفى (mufradat)
- **B002** sırt ve arka yüz — sırt; karın ya da ön tarafın karşıtı olan arka yüz · sırtı güçlü kimse · sırtı ağrıyan veya incinmiş kimse · birinin sırtına vurmak veya zarar vermek · kolları arkada bağlayan veya yere düşüren tutuş
  ظهر الإنسان خلاف بطنه (maqayis)؛ الظهر خلاف البطن من كل شيء (ayn;sihah;tahdhib)؛ الظهر الجارحة وجمعه ظهور (mufradat)؛ رجل مظهر شديد الظهر ورجل ظهر يشتكي ظهره (maqayis;sihah;tahdhib;mufradat)
- **B003** yüksek ya da dışta kalan yüz — yerin yüksek veya açıkta kalan yüzü · dış ya da üst yüz; astarın karşıtı
  الظهر من الأرض ما غلط وارتفع (ayn;tahdhib)؛ الظاهرة كل أرض غليظة مشرفة (ayn)؛ الظواهر أشراف الأرض (sihah;tahdhib)؛ ظهر الأرض وبطنها (mufradat)؛ الظهارة خلاف البطانة (ayn;sihah;tahdhib)
- **B004** öğle vakti ve ona bağlı eylemler — öğle vakti ve o vakitte kılınan namaz · gün ortası veya öğle sıcağı · öğle vaktine girmek veya o sırada yol almak · hayvanların her gün öğleyin suya gelmesi
  وقت الظهر والظهيرة أظهر أوقات النهار (maqayis)؛ الظهر ساعة الزوال وصلاة الظهر والظهيرة حد انتصاف النهار (ayn;tahdhib)؛ الظهر بعد الزوال والظهيرة الهاجرة (sihah)؛ صلاة الظهر والظهيرة وقت الظهر وأظهر فلان حصل في ذلك الوقت (mufradat)؛ الظاهرة أن ترد كل يوم ظهرا (sihah;tahdhib)
- **B005** yük bineği ve yedek deve — yük taşıyan binek veya deve topluluğu · gerektiğinde kullanılmak üzere hazır tutulan deve
  الركاب الظهر لأن الذي يحمل منها الشيء ظهورها (maqayis)؛ الظهر الركاب تحمل الأثقال في السفر (ayn;tahdhib)؛ الظهر الركاب وبنو فلان مظهرون (sihah)؛ يعبر عن المركوب بالظهر وظهري معد للركوب (mufradat)؛ البعير الظهري العدة للحاجة (sihah;tahdhib)
- **B006** yardım edip güçlendirmek — yardımcı, destekçi · yardımlaşma ve destek olma · ondan yardım alıp güçlenmek
  الظهير المعين كأنه أسند ظهره إلى ظهرك (maqayis)؛ الظهير العون والمظاهر المعاون وهما يتظاهران أي يتعاونان (ayn)؛ الظهير المعين والمظاهرة المعاونة والتظاهر التعاون واستظهر به استعان به (sihah)؛ ظهير في معنى ظهراء أي أعوان وظاهروا أي عاونوا (tahdhib)؛ ظاهرته عاونته وما له منهم من ظهير أي معين (mufradat)
- **B007** üzerine çıkmak veya üstün gelmek [kalıp] — üstün gelmek veya üzerinde güç kurmak · damın veya yüzeyin üstüne çıkmak
  الظهور الغلبة (maqayis)؛ الظهور الظفر بالشيء (ayn;tahdhib)؛ ظهرت على الرجل غلبته وظهرت البيت علوته (sihah)؛ ظهر على الحائط وعلى السطح وظهر على الشيء إذا غلبه وعلاه (tahdhib)؛ ظهر عليه غلبه وليظهره على الدين كله (mufradat)
- **B008** bilgiye ulaşıp öğrenmek [kalıp] — bir şeyi öğrenmek veya bulup ortaya çıkarmak
  ظهرت على كذا إذا اطلعت عليه (maqayis)؛ والله أظهرنا عليه أي أطلعنا (ayn)؛ أظهرني الله على ما سرق مني أي أعثرني عليه وظهرت على الأمر (tahdhib)؛ فلا يظهر على غيبه أحدا أي لا يطلع عليه (mufradat)
- **B009** çıkık göz — çökük gözün karşıtı olan çıkık göz
  الظاهرة العين الجاحظة (maqayis)؛ الظاهرة العين الجاحظة وهي خلاف الغائرة (ayn)؛ الظاهرة من العيون الجاحظة (sihah)؛ العين الظاهرة التي ملأت نقرة العين وهي خلاف الغائرة (tahdhib)
- **B010** eşe yönelik benzetmeli yasaklama sözü — kocanın eşini kendisine yasak saydığını bildiren geleneksel söz · eşini annesinin sırtına benzeterek kendisine yasak sayma sözü
  الظهار قول الرجل لامرأته أنت علي كظهر أمي (maqayis;sihah;mufradat)؛ مظاهرة الرجل امرأته إذا قال هي علي كظهر أمي أو كظهر ذات رحم محرم (ayn)؛ وأوجبت الكفارة على من ظاهر من امرأته (tahdhib)
- **B011** kanadın dış tüyleri — kanadın dıştan görünen tüyleri veya tüy sapının sırt yönündeki parçası
  الظهار من الريش ما يظهر منه في الجناح (maqayis)؛ الظهار من الريش الذي يظهر من ريش الطائر وهو في الجناح (ayn;tahdhib)؛ الظهار ما جعل من ظهر عسيب الريشة والظهران الجانب القصير من الريش (sihah;tahdhib)
- **B012** geriye atıp önemsememek — arkaya atılıp unutulan şey · bir isteği önemsemeyip geriye atmak
  الظهري كل شيء تجعله بظهر أي تنساه (maqayis)؛ الظهري الشيء تنساه وتغفل عنه (ayn;tahdhib)؛ لا تجعل حاجتي بظهر أي لا تنسها (sihah)؛ ظهرت بكذا أي خلفته ولم ألتفت إليه (mufradat)
- **B013** ayıbı kişiden uzak olmak [kalıp] — ayıbı sana yapışmayan, senden uzak söz veya durum
  أمر ظاهر عنك عاره أي زائل (maqayis;sihah)؛ ظهر عني هذا العيب أي نبا عني ولم يعلق بي (tahdhib)؛ تلك شكاة ظاهر عنك عارها (maqayis;sihah;tahdhib)
- **B014** ev eşyası ve yedek mallar — ev eşyası ve gerektiğinde yararlanılan mallar
  الظهرة متاع البيت وأحسب هذه مستعارة من الظهر أيضا لأن الإنسان يستظهر بها (maqayis)؛ الظهرة بالتحريك متاع البيت (sihah)؛ الظهرة ما في البيت من المتاع والثياب (tahdhib)
- **B015** kara yolu ve dıştaki yüksek kesim — deniz yolunun karşıtı olan kara yolu · Mekke'nin dış veya yüksek kesimlerinde yaşayan Kureyşliler
  طريق الظهر (ayn;sihah;tahdhib)؛ سلكنا الظهر يريدون طريق البر (maqayis)؛ قريش الظواهر سموا بذلك لأنهم ينزلون ظاهر مكة (maqayis;sihah;tahdhib)؛ ظاهرة الجبل أعلاه وظاهرة كل شيء أعلاه (tahdhib)
- **B016** güç alınan destekçi topluluğu — kişinin güç aldığı yardımcıları ve yakın topluluğu
  جاء فلان في ظهرته وناهضته أي قومه (maqayis;sihah)؛ الظهرة ظهر الرجل وأنصاره (tahdhib)؛ الظهراء أعوان النبي (tahdhib)
- **B017** topluluk veya zaman sınırları arasında [kalıp] — aralarında, topluluğun ortasında · iki gün veya iki zaman sınırı arasında
  أنا بين ظهرانيهم وظهريهم (ayn)؛ نازل بين ظهريهم وظهرانيهم (sihah)؛ نزل فلان بين ظهرينا وظهرانينا وأظهرنا (tahdhib)؛ بين الظهرانين معناه في اليومين أو في الأيام (sihah;tahdhib)
- **B018** bir konuyu her yönüyle incelemek [kalıp] — bir konuyu evirip çevirerek her yönüyle incelemek
  قلبت الأمر ظهرا لبطن (ayn;tahdhib)
- **B019** ezberleyip bellekten söylemek — kitaba bakmadan, ezberden · ezberlemek ve kitaba bakmadan okumak
  تكلمت بذلك عن ظهر غيب (ayn;tahdhib)؛ ظهر القلب حفظ من غير كتاب (ayn;tahdhib)؛ استظهر الشيء أي حفظه وقرأه ظاهرا (sihah)؛ حمل القرآن على ظهر لسانه (tahdhib)
- **B020** iki katmanı üst üste getirmek [kalıp] — iki giysiyi veya iki zırhı üst üste getirmek
  ظاهر بين ثوبين أي طارق بينهما وطابق (sihah)؛ ظاهر فلان بين ثوبين وبين درعين إذا طابق بينهما (tahdhib)
- **B021** yedek hazırlayıp güvence sağlamak — gerektiğinde kullanılmak üzere hazır tutulan deve · yedek hazırlayarak önlem almak ve güvence sağlamak
  البعير الظهري العدة للحاجة (sihah;tahdhib)؛ الاستظهار في كلامهم الاحتياط والاستيثاق (tahdhib)؛ استظهر ببعيرين ظهريين محتاطا بهما (tahdhib)
- **B022** birbirine sırt çevirip uzaklaşmak — birbirine sırt çevirip uzaklaşmak
  تظاهر القوم إذا تدابروا (maqayis;sihah)؛ كل واحد منهما أدبر عن صاحبه وجعل ظهره إليه (maqayis)
- **B023** karşılıksız veya artandan vermek [kalıp] — karşılık beklemeden, kendiliğinden vermek · geçim gereklerinden artan bolluktan vermek
  عن ظهر يد معناه ابتداء من غير مكافأة (tahdhib)؛ ما كان عن ظهر غنى عن فضل عيال (tahdhib)
- **B024** bir şeyle övünmek [kalıp] — bir şeyle övünmek ve onu övünç dayanağı yapmak
  ظهرت به أي افتخرت به (tahdhib)؛ واظهر ببزته أي افخر به على غيره (tahdhib)

## د ع و (root_000478): 84:11 يَدْعُوا۟

- **B001** seslenerek kendine yöneltme — seslenmek; çağırmak · yemeğe çağırma · belirtilen yeri amaçlayıp oraya gitmek
  أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك؛ دعوت أدعو دعاء؛ الدعوة إلى الطعام بالفتح؛ دعا فلانا مكان كذا إذا قصد ذلك المكان كأن المكان دعاه
- **B002** hak veya aidiyet ileri sürme — soy bağı ileri sürme · kendisi veya başkası adına hak iddia etme · savaşta soyunu söyleyerek kendini tanıtma · öz babasından başkasına bağlanan kişi
  الادعاء أن تدعي حقا لك أو لغيرك (maqayis)؛ الادعاء في الحرب الاعتزاء (maqayis)؛ الدعوة ادعاء الولد الدعي غير أبيه ويدعيه غير أبيه (ayn)؛ الدعوة في النسب بالكسر (maqayis)
- **B003** sütün devamını çekmek için memede bırakılan pay [kalıp] — sonraki sütü çekmek için memede bırakılan süt payı
  داعية اللبن ما يترك في الضرع ليدعو ما بعده
- **B004** Tanrı'nın birine istemediği bir sıkıntıyı vermesi [kalıp] — Tanrı'nın birinin başına hoşlanmadığı bir sıkıntıyı getirmesi
  دعا الله فلانا بما يكره أي أنزل به ذلك
- **B005** birbiri ardından çökme veya yıkma — duvarların birbiri ardından çökmesi · yapıları üzerlerine birbiri ardından yıkmak
  تداعت الحيطان وذلك إذا سقط واحد وآخر بعده؛ داعيناها عليهم إذا هدمناها واحدا بعد آخر
- **B006** dönemin olaylara yön veren değişimleri [kalıp] — dönemin değişimleri ve getirdiği olaylar
  دواعي الدهر صروفه كأنها تميل الحوادث
- **B007** gizli cevabı buldurmaya yönelik bilmeceleşme — gizli cevabı buldurmak için karşılıklı sorulan bilmeceler · sana bir bilmece sorayım
  لبنى فلان أدعية يتداعون بها وهي مثل الأغلوطة كأنه يدعو المسؤول إلى إخراج ما يعميه عليه
- **B008** evde hiç kimsenin bulunmaması — evde hiç kimse yok
  ما بالدار دَعْوِيّ أي ما بها أحد كأنه ليس بها صائح يدعو بصياحه

## ECHO د ع ع (root_000477): for 84:11 يَدْعُوا۟: withheld observed target; not identity

- **B001** itme — sert ve kaba itme · sertçe itmek · yetimi itip azarlamak · ateşe doğru zorla sürmek
  الدَّعّ الدفع (maqayis;tahdhib)؛ دَعَعته أدَعُّه دَعًّا أي دفعته (sihah)؛ دفع في جفوة (ayn)؛ الدفع الشديد (mufradat)
- **B002** sallayarak doldurma — kabı sallayarak doldurma · bir şeyi doldurmak veya hareket ettirerek sıkıştırmak · ağzına kadar dolu büyük çanak · selin vadiyi doldurması
  الدعدعة تحريك المكيال ليستوعب الشيء (maqayis)؛ دعدعت الشيء ملأته وجفنة مدعدعة (sihah)؛ دعدع مكيالا أو جوالقا حتى يكتنز (tahdhib)
- **B003** hayvanı seslenerek yönlendirme — küçükbaş hayvanı seslenerek çağırma veya azarlama · keçilere seslenip onları yönlendirmek · çobanın keçileri yönlendirmek için çıkardığı geleneksel çağrı
  الدعدعة زجر الغنم (maqayis)؛ للمعز خاصة دعدعت بها إذا دعوتها (sihah)؛ يقول الراعي للمعزى داع داع وهو زجر لها (tahdhib)
- **B004** tökezleyeni ayağa kalkmaya çağırma — tökezleyene söylenen 'kalk, toparlan' sözü
  قولك للعاثر دع دع (maqayis)؛ أن تقول للعاثر دع دع أي قم فانتعش (sihah;tahdhib)؛ أصله أن يقال للعاثر دع دع (mufradat)
- **B005** kıvrılarak yavaş koşma — kıvrıla kıvrıla yavaş koşma
  الدعدعة عدو في التواء (maqayis)؛ عدا عدوا فيه بطء والتواء (sihah)؛ عدو في التواء وبطء (tahdhib)
- **B006** kısa boylu adam — 
  دعداع فإن صح فهو من الإبدال من دحداح (maqayis)؛ الدعداع والدحداح الرجل القصير (tahdhib)
- **B007** iki hurma arasındaki açıklık veya seyrek hurmalar — 
  الدعاع ما بين النخلتين؛ الدعاع النخل المتفرق؛ رواه بعضهم في ذعاع النخل بالذال
- **B008** yazın su barındıran, sığırların yediği bitki — yazın su tutan ve sığırların yediği bir bitki
  الدعدع نبت يكون فيه ماء في الصيف يأكله البقر
- **B009** küçük çocuklar ve bakmakla yükümlü olunan küçükler — bir erkeğin küçük çocukları ve bakımına bağlı küçükler · bakımına bağlı küçüklerin sayısı çoğalmak
  الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه
- **B010** yabani bitki tohumu — yabani bir bitkinin tohumu · kuraklıkta yenen siyah tohum; ona benzeyen siyah karınca · bu tohumu ve başka bir yabani tohumu yemek için toplayan adam
  الدعاع حب شجرة برية؛ الدعاعة حبة سوداء؛ نملة سوداء تشاكل هذه الحبة؛ رجل دعاع فثاث

## ث ب ر (root_000193): 84:11 ثُبُورًا

- **B001** düz arazi, beyazımsı toprak, çukur veya coğrafi ad — düz arazi; kirece benzer beyazımsı toprak; çukur veya kuyu · bilinen bir yer adı · bilinen bir dağ adı · aynı adla anılan dağlar veya yerler
  الثبرة الأرض السهلة (maqayis;sihah)؛ الثبرة تراب شبيه بالنورة (maqayis;jamhara)؛ الثبرة حفرة أو نقرة أو ركية (sihah;tahdhib)؛ ثبير جبل معروف (maqayis;jamhara;sihah;mufradat)
- **B002** yok oluş, yıkım, kayıp, bozulma veya akıl eksikliği — 
  الثبور الهلاك (maqayis;tahdhib)؛ الثبور الويل والهلاك (jamhara;tahdhib)؛ الثبور الهلاك والخسران (sihah)؛ الثبور الهلاك والفساد (mufradat)؛ رجل مثبور هالك أو مهلك (maqayis;jamhara;tahdhib)؛ مثبورا ناقص العقل (mufradat)
- **B003** alıkoyma, engelleme, geri çevirme veya iyilikten yoksun bırakma — 
  ثبره عن كذا حبسه وما ثبرك عن حاجتك (sihah)؛ ما ثبرك أي ما منعك وما صرفك عنه (tahdhib)؛ ثبرت فلانا عن الشيء رددته عنه (tahdhib)؛ مثبورا مغلوبا ممنوعا من الخير (tahdhib)
- **B004** bir işi kararlılıkla sürdürme; savaşta art arda saldırma [kalıp] — bir işi düzenli ve kararlı biçimde sürdürmek · savaşta birbirinin üzerine atılıp art arda saldırmak
  ثابرت على الشيء أي واظبت (maqayis)؛ المثابر على الشيء المواظب عليه (jamhara)؛ المثابرة على الشيء المواظبة عليه (sihah)؛ ثابر فلان على الأمر مثابرة إذا واظب عليه (tahdhib)؛ المثابر على الإتيان أي المواظب (mufradat)؛ تثابرت الرجال في الحرب إذا تواثبت (maqayis;jamhara)
- **B005** doğum yeri; dişi devenin kesildiği yer; erkeğin oturduğu yer — dişi devenin yavrusunu ve doğumla çıkanları bıraktığı yer · kadının doğurduğu veya dişi devenin yavruladığı yer · dişi devenin kesilip parçalandığı yer · erkeğin oturduğu yer; seyrek kullanım
  مثبر الناقة الموضع الذي تطرح فيه ولدها (maqayis)؛ مثبر الناقة الموضع الذي تطرح فيه ولدها وما يخرج معه (jamhara)؛ المثبر الموضع الذي تلد فيه المرأة وكذلك حيث تضع الناقة وربما قيل لمجلس الرجل مثبر (sihah)؛ المثبر الموضع الذي تلد فيه المرأة وكذلك حيث تضع فيه الناقة وحيث تعضى وتنحر (tahdhib)
- **B006** denizin geri çekilmesi veya yaranın açılması [kalıp] — deniz suyunun kıyıdan geri çekilmesi · yaranın açılması
  ثبر البحر جزر (maqayis;jamhara)؛ ثبرت القرحة أي انفتحت (tahdhib)

## ص ل ي (root_000880): 84:12 وَيَصْلَىٰ

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ECHO ص ل و (root_000879): for 84:12 وَيَصْلَىٰ: withheld observed target; not identity

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## س ع ر (root_000708): 84:12 سَعِيرًا

- **B001** ateşin tutuşması, yakılıp harlanması; ateş, yakıt, sıcaklık ve harlama aracı — ateşin yanışı, yakıtı ve yanmasını sağlayan şey · ateşi yakmak ve harlamak · ateş tutuşup alevlenmek · alevli ateş · ateş karıştırma ve harlama aracı · ateşin yakıcı sıcaklığı
  أصل واحد يدل على اشتعال الشيء واتقاده (maqayis); السعير نار (maqayis); السعر وقود النار (ayn); سعرت النار هيجتها وألهبتها (sihah); سعرت النار إذا أوقدتها وهي مسعورة (tahdhib); السعر التهاب النار (mufradat); المسعر الخشب الذي يسعر به (maqayis;sihah;mufradat)
- **B002** savaşı ve kötülüğü alevlendirmek; yakıcı saldırı ya da taşkın yayılma yaratmak [kalıp] — savaşı körükleyip kızıştırmak · savaşı sürekli körükleyen kişi ya da etken · üzerlerine kötülük salmak · onları oklarla yakıp acıtmak · hırsızlar taşkınca harekete geçip yayılmak
  السعر وقود النار والحرب (ayn); سعرت النار والحرب هيجتهما وألهبتهما (sihah); سعرناهم بالنبل أي أحرقناهم وأمضضناهم (sihah); رجل مسعر حرب (sihah;tahdhib); سعرت نار الحرب واستعرت النار (tahdhib); استعر الحرب واللصوص نحو اشتعل (mufradat); سعرهم شرا (maqayis;sihah)
- **B003** piyasa fiyatı ve fiyat belirleme — malın ya da yiyeceğin piyasa fiyatı · piyasa esnafı bir fiyatta anlaşmak veya fiyat belirlemek
  السعر سعر السوق الذي تقوم عليه بالثمن (ayn); أسعر أهل السوق إسعارا وسعروا تسعيرا (ayn); السعر واحد أسعار الطعام والتسعير تقدير السعر (sihah); السعر من الأسعار وهو الذي يقوم عليه الثمن (tahdhib); السعر في السوق تشبيها باستعار النار (mufradat); سعر الطعام من هذا لأنه يرتفع ويعلو (maqayis)
- **B004** yakıcı bedensel şiddet, çılgın taşkınlık ve ağır acı; ayrıca ateşin harareti — delilik; çekilen ağır acı ve ceza · keskin ve çılgınca davranan deve · sıcak rüzgârdan, şiddetli açlıktan ya da susuzluktan kavrulmak · açlığın ve susuzluğun yakıcı şiddeti · sapma içinde delilik ya da ağır acı
  السعار حر النار (maqayis;tahdhib;mufradat); سعر الرجل إذا ضربته السموم (maqayis;sihah); السعار شدة الجوع أيضا (sihah); السعر أيضا الجنون (maqayis;sihah); ناقة مسعورة أي مجنونة (maqayis;sihah); العناء والعذاب خاصة (sihah;tahdhib); سعار العطش التهابه وسعار الجوع لهيبه (tahdhib); سعر الرجل فهو مسعور إذا اشتد جوعه أو عطشه (tahdhib); ناقة مسعورة نحو موقدة ومهيجة (mufradat)
- **B005** devede uyuzun başladığı ya da şiddetlendiği koltuk altı, kasık ve benzeri bölgeler — devenin uyuzun başladığı koltuk altı, kasık ve benzeri kıvrım bölgeleri · uyuz devenin kıvrım bölgelerinde başlamak veya şiddetlenmek
  مساعر البعير آباطة وأرفاغه واصل ذنبه حيث رف وبره (maqayis); الجرب يستعر فيها أولا ويستعر فيها أشد (maqayis); مساعر الإبل آباطها وأرفاغها (sihah); استعر الجرب في البعير إذا ابتدأ بمساعره (sihah); مساعر البعير حيث يستعر فيه الجرب من الآباط والأرفاغ وأم القراد والمشافر (tahdhib)
- **B006** güneş ışığı demetinde görülen uçuşan ince toz — güneş ışığında görülen uçuşan ince toz
  السعرارة هي التي تراها في الشمس كالهباء (maqayis); السعرارة الهباء في الشمس (sihah); السعرارة ما تردد في الضوء الساقط في البيت من الشمس وهو الهباء المنبث (tahdhib)
- **B007** iş için dolaşıp yayılmak; hızla koşmak veya ayakları dağınık biçimde ilerlemek — bugün işimin peşinde dolaştım · deve hızla yürümek · ayaklarını dağınık savurarak ilerleyen at · koşunun şiddeti ve hızı
  سعرت اليوم في حاجتي أي طفت (sihah;tahdhib); سعرت الناقة إذا أسرعت في سيرها فهي سعور (tahdhib); فرس مسعر ومساعر وهو الذي تطيح قوائمه متفرقة ولا ضبر له (tahdhib); السعران شدة العدو (tahdhib); استعر الناس في كل وجه (tahdhib)
- **B008** esmerden biraz koyu, siyaha çalan ten rengi — esmerden biraz koyu, siyaha çalan renk
  السعرة لون إلى السواد (sihah); السعرة في الإنسان لون يضرب إلى سواد فويق الأدمة (tahdhib)
- **B009** toprağa kazılmış ekmek fırını — toprağa kazılmış ekmek fırını
  الساعورة كهيئة التنور يحفر في الأرض يختبز فيه (tahdhib)
- **B010** keskin öksürük; bir işin ilk ve en sert evresi — keskin ve şiddetli öksürük · işin ilk ve sert evresi
  السعيرة تصغير السعرة وهي السعال الحاد (tahdhib); هذا سعرة الأمر أي أوله وحدته (tahdhib)
- **B011** uzun; güçlü, sert veya şiddetli — uzun veya güçlü ve sert
  المسعر أيضا الطويل (sihah); المسعر الشديد (tahdhib); المسعر الطويل (tahdhib)

## ك و ن (root_001332): 84:13 كَانَ, 84:15 كَانَ

- **B001** gerçekleşme, bulunma ve olma bildirimi — gerçekleşip ortaya çıkmak veya hazır bulunmak · geçmişte bir durumu bildirmek · oluş; gerçekleşme · olma, oluş · sonradan gerçekleşen iş · yüklemi pekiştiren ek söz · birini geliş kapsamı dışında tutan bağlı söz · var edip gerçekleşmesini sağlamak
  الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)
- **B002** bulunma yeri ve konum değeri — bulunulan yer · yerler · konum, düzey veya bulunulan yer · birinin yanında güçlü konumu olan · yerleşmek veya güç kazanmak · birinin yanında şu yer veya düzeyde bulunmak
  المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)
- **B003** birini güvenceyle üstlenme — başkası için güvence üstlenme · birini üstlenmek · birine güvence olmak
  الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)
- **B004** boyun eğme — boyun eğme
  الاستكانة الخضوع (sihah)
- **B005** gençliğini anan yaşlı kişi — gençken şöyleydim diye anlatan yaşlı kişi
  يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)
- **B006** kötü durumda gece geçirme [kalıp] — geceyi kötü durumda geçirmek
  الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

## ظ ن ن (root_000969): 84:14 ظَنَّ

- **B001** belirtiye dayanıp kesin bilgiye varan güçlü inanış — kesin olarak bilmek; emin olmak · bir belirtiden doğup güçlendikçe bilgiye, zayıfladıkça kuruntuya yaklaşan inanış
  ظننت ظنا أي أيقنت (maqayis)؛ قد يوضع موضع العلم؛ أي استيقنوا (sihah)؛ الظن يقين وشك؛ أي علمت (tahdhib)؛ متى قويت أدت إلى العلم (mufradat)
- **B002** bir şeyin bulunduğu düşünülen yer veya onu gösteren belirti — bir şeyin bulunduğu düşünülen yer, alışılmış alan veya onu gösteren belirti
  مظنة الشيء وهو معلمه ومكانه (maqayis)؛ مظنة الشيء موضعه ومألفه الذي يظن كونه فيه (sihah)؛ فلان مظنة من كذا ومئنة أي معلم (tahdhib)
- **B003** zayıf belirtiye dayalı kesinleşmemiş inanış — bir belirtiden doğup güçlendikçe bilgiye, zayıfladıkça kuruntuya yaklaşan inanış · kesin bilmeden öyle sanmak; kuşku duymak · sanıya dayanarak düşünme
  الشك؛ ظننت الشيء إذا لم تتيقنه (maqayis)؛ باليقين لا بالشك (sihah)؛ الظن يقين وشك (tahdhib)؛ متى ضعفت جدا لم يتجاوز حد التوهم (mufradat)
- **B004** birini suçlu sayma, suçlama ve suçlanan kişi — suçlama · hakkında suç kuşkusu bulunan kişi · onu suçladı · onu suçladı · o kişiyi suçladım
  الظنة التهمة؛ الظنين المتهم (maqayis)؛ الظنة التهمة؛ فلان ظنين أي متهم (jamhara)؛ الظنين الرجل المتهم؛ اطنه واظنه إذا اتهمه (sihah)؛ الظنين المتهم؛ ظننت بزيد أي اتهمت (tahdhib)؛ بظنين أي بمتهم (mufradat)
- **B005** başkaları hakkında kötü düşünme ve kötülük bekleme — herkese kuşkuyla bakan kimse · onun hakkında kötü düşündüm · kötülük yakıştıran düşünce
  الظنون السيئ الظن؛ سؤت به ظنا (maqayis)؛ الظنون الرجل السيئ الظن (sihah)؛ الظنون الرجل السيىء الظن بكل أحد (tahdhib)
- **B006** varlığı, doğruluğu veya sonucu belirsiz olduğu için güven vermeyen şey — su veya başka bir konuda güven vermeyen şey · suyu olup olmadığı bilinmeyen kuyu · ödenip ödenmeyeceği bilinmeyen alacak · sonucu bilinmeyen iş · o konudaki bilgisi güvenilir değil · iyiliği az kimse
  الظنون البئر لا يدرى أفيها ماء أم لا؛ الدين الظنون الذي لا يدرى أيقضى أم لا (maqayis)؛ الدين الظنون؛ الظنون البئر لا يدرى أفيها ماء أم لا (sihah)؛ الظنون كل ما لا يوثق به من ماء وغيره؛ علمه بالشيء ظنون إذا لم يوثق به؛ كل أمر تطالبه ولا تدري على أي شيء أنت منه فهو ظنون (tahdhib)
- **B007** düşmanlık eden kişi — düşmanlık eden kişi
  الظنين المعادي (tahdhib)
- **B008** bağlama göre güçsüz ya da yükleneni kaldırabilen kişi — bağlama göre güçsüz ya da yükleneni kaldırabilir · güçsüz veya çaresi az kimse
  ما هو بضعيف؛ هو محتمل له؛ الرجل الضعيف أو القليل الحيلة؛ ربما دلك على الرأي الظنون (tahdhib)
- **B009** evlenince kendisinden çocuk beklenen saygın kadın — evlenince kendisinden çocuk beklenen saygın kadın
  الظنون من النساء التي لها شرف تتزوج؛ سميت ظنونا لأن الولد يرتجى منها (tahdhib)

## ح و ر (root_000369): 84:14 يَحُورَ

- **B001** göz akıyla göz karasının güçlü karşıtlığı — göz akıyla karasının güçlü karşıtlığı · göz akı ile karası belirgin kadınlar ya da gözler · gözünün akı ve karası belirgin erkek ya da kadın
  الحور شدة بياض العين في شدة سوادها (maqayis;sihah)؛ الحور شدة بياض العين وشدة سوادها (ayn)؛ الحور نقاء بياض العين وصفاء سوادها (jamhara)؛ جمع أحور وحوراء (mufradat)
- **B002** aklaştırma ve aklaştırılarak arıtılmış yiyecek — giysileri yıkayıp aklaştırmak · ak ve arıtılmış ince un ya da yiyecek · hörgüç yağıyla aklaştırılmış büyük yemek kabı · ak tenli ya da kentli kadınlar
  حورت الثياب أي بيضتها (maqayis)؛ الحوارى أجود الدقيق وحورته تحويرا أي بيضته (ayn)؛ الدقيق الحوارى لبياضه ونقائه (jamhara)؛ تحوير الثياب تبيضها والاحوارى ما حور من الطعام (sihah)؛ حورت الشيء بيضته ومنه الخبز الحوارى (mufradat)
- **B003** içtenlikle destekleyen kimse — bir peygamberin yanında yer alan yakın destekçiler · içtenlikle destekleyen kimse
  قيل لأصحاب عيسى الحواريون لأنهم كانوا يحورون الثياب (maqayis)؛ سمي كل ناصر حواريا (maqayis)؛ الحواريون الذين كانوا مع عيسى ينصرونه (ayn)؛ الحواريون أنصار عيسى (mufradat)
- **B004** özel yöntemle işlenmiş, kızıl ya da şerit kesilmiş deri — özel biçimde sepilenmiş, kızıl boyanmış ya da şerit kesilmiş deri · içi bu tür deriyle kaplanmış ayakkabı
  الحور ما دبغ من الجلود بغير القرظ (maqayis)؛ الحور الأديم المصبوغ بحمرة (ayn)؛ الحور جلود تشق (jamhara)؛ الحور جلود حمر يغشى بها السلال (sihah)
- **B005** geri dönme, gerileme ve kararsız kalma — geri dönmek ya da iki durum arasında gidip gelmek · geri dönüş ve artıştan sonra azalma · yükselişten sonra gerileme · giderek azalma ya da şaşırıp yön bulamama · bir işte ne yapacağını bilemeyip kararsız kalmak
  حار إذا رجع (maqayis)؛ كل نقص ورجوع حور (maqayis)؛ الحور الرجوع إلى الشيء وعنه (ayn)؛ الحور الرجوع من صلاح إلى فساد أو من زيادة إلى نقصان (jamhara)؛ حار يحور حورا رجع (sihah)؛ الحور التردد (mufradat)
- **B006** karşılıklı söz alışverişi ve sözlü karşılık — karşılıklı konuşma ve söz alışverişi · biriyle karşılıklı konuşup sözlerine karşılık vermek · sözlü karşılık vermek
  كلمته فما رجع إلي حوارا (maqayis)؛ المحاورة مراجعة الكلام (ayn)؛ حاورت فلانا محاورة وحوارا وحويرا (jamhara)؛ المحاورة المجاوبة والتحاور التجاوب (sihah)؛ المحاورة والحوار المرادة في الكلام (mufradat)
- **B007** dönme mili ve döndürerek biçim verme — makara veya benzeri parçanın üzerinde döndüğü mil · ekmeklik hamuru çevirip yuvarlayarak pişirmeye hazırlamak
  المحور الخشبة التي تدور فيها المحالة (maqayis)؛ المحور الحديدة التي تدور عليها البكرة (ayn)؛ حورت الخبزة إذا دورتها (jamhara)؛ المحور العود الذي تدور عليه البكرة (sihah)؛ المحور للعود الذي تجري عليه البكرة لتردده (mufradat)
- **B008** sütten kesilmemiş deve yavrusu — doğumdan sütten kesilmeye kadarki deve yavrusu
  حوار الناقة وهو ولدها (maqayis)؛ الحوار الفصيل أول ما ينتج والجميع الحيران (ayn)؛ حوار الناقة ولدها وجمع الحوار حيران وأحورة (jamhara)؛ الحوار ولد الناقة ولا يزال حوارا حتى يفصل (sihah)
- **B009** yok olma, işlerin durması ya da durum değiştirme — yok olup gitme; kimi bağlamda şaşkınlık veya işlerin durması · tükenmiş, işleri durmuş ya da şaşkın kişi
  كل شيء تغير من حال إلى حال فقد حار (ayn)؛ الحور أيضا الهلكة (sihah)؛ فلان حائر بائر هذا قد يكون من الهلاك ومن الكساد (sihah)

## ب ص ر (root_000121): 84:15 بَصِيرًا

- **B001** gözle görme — görme duyusu; bakan göz · bir şeyi gözle görmek · gören, kör olmayan kişi · dikkatle dikilerek bakış; belirgin ve sert durum · göz ucuyla süzerek incelemek · yavrunun gözünün açılması
  أبصرته إذا رأيته (maqayis)؛ البصر العين (ayn;tahdhib)؛ البصر حاسة الرؤية وأبصرت الشيء رأيته والبصير خلاف الضرير (sihah)؛ والبصر معروف أبصر يبصر إبصارا فهو مبصر وبصير (jamhara)؛ الجارحة الناظرة والباصرة (mufradat)؛ رأيته لمحا باصرا أي نظرا بتحديق شديد (maqayis;sihah;tahdhib;mufradat)؛ بصر الجرو تبصيرا فتح عينه (ayn;tahdhib;mufradat)
- **B002** iç kavrayış — bir şeyi bilip kavramak · bilgi; kalbin kavrayışı · bilgili, kavrayış sahibi kişi · düşünüp tanımak · işinde veya dininde kavrayış sahibi olmak · kalp bilgisi, delil ve ibret · deliller, ibretler ve açıklamalar
  أحدهما العلم بالشيء وبصرت بالشيء إذا صرت به بصيرا عالما والبصيرة البرهان (maqayis)؛ البصر نفاذ في القلب والبصيرة اسم لما اعتقد في القلب من الدين وحقيق الأمر واستبصر في أمره ودينه (ayn;tahdhib)؛ حسن البصيرة إذا كان مستبصرا في دينه (jamhara)؛ البصر العلم وبصرت بالشيء علمته والتبصر التأمل والتعرف والبصيرة الحجة والاستبصار في الشيء (sihah)؛ لقوة القلب المدركة بصيرة وبصر وعلى معرفة وتحقق (mufradat)
- **B003** aydınlatıcı açıklık — aydınlık, açık kılan ve görmeyi sağlayan · açıklama ve belirgin kılma
  المبصرة المضيئة تبصرهم أي تجعلهم بصراء والمبصرة بالفتح الحجة (sihah)؛ مبصرة مضيئة وتبين لهم ومبصرا بها (tahdhib)؛ آياتنا مبصرة أي مضيئة للأبصار وقيل صار أهله بصراء وتبصرة أي تبصيرا وتبيانا (mufradat)
- **B004** kan izi — yerde veya bedende kan lekesi, kan izi · kanlar; kan bedelleri veya öçler
  البصيرة القطعة من الدم إذا وقعت بالأرض استدارت (maqayis;jamhara)؛ بصائر الدماء طرائقها على الجسد (ayn)؛ البصيرة من الدم ما كان على الأرض وشيء من الدم يستدل به على الرمية (sihah)؛ بصيرة من دم والجدية منها على الأرض والبصيرة الدية ومقدار الدرهم من الدم (tahdhib)؛ البصيرة قطعة من الدم تلمع (mufradat)
- **B005** koruyucu savaş gereci — kalkan, zırh veya giyilen savaş koruması
  البصيرة الترس فيما يقال (maqayis)؛ البصيرة الدرع وما لبس من السلاح فهو بصائر السلاح (ayn;tahdhib)؛ البصيرة في هذا البيت الترس أو الدرع (sihah)؛ الترس اللامع (mufradat)
- **B006** kalın kenar ve ek yeri — bir şeyin yanı, kenarı veya kalın dış yüzü · iki deri parçasını birleştirip dikme · çadır, elbise veya kapta iki parça arası · iki parça arasında yamanmış ek
  بصر الشيء غلظه والبصر هو أن يضم أديم إلى أديم يخاطان والبصيرة ما بين شقتي البيت (maqayis)؛ البصر غلظ الشيء نحو بصر الجبل والسماء والحائط (ayn)؛ بصر كل شيء جلده الظاهر وثوب ذو بصر إذا كان غليظا وثيجا (jamhara)؛ البصر أن يضم أديم إلى أديم والبصر بالضم الجانب والحرف من كل شيء وغلظها (sihah)؛ الباصر الملفق بين شقتين والبصيرة الشقة التي تكون على الخباء والبصر أن يضم أديم إلى أديم (tahdhib)؛ البصر الناحية والبصيرة ما بين شقتي الثوب والمزادة وبصرت الثوب والأديم إذا خطت ذلك الموضع (mufradat)
- **B007** yumuşak parlak taş — yumuşak veya parlak taş; böyle taşlı yer · sonundaki ek düşmüş biçimiyle yumuşak taş · adı bu taşlı yer olan yere gitmek
  البصرة الحجارة الرخوة وبصر بكسر الباء من الأصل الثاني (maqayis)؛ البصرة أرض حجارتها جص والبصرة الحجارة التي فيها بعض اللين (ayn)؛ البصرة حجارة رخوة وبه سميت البصرة (jamhara)؛ البصرة حجارة رخوة إلى البياض وبصر بالكسر (sihah)؛ البصر والبصرة الحجارة البراقة وأرض كأنها جبل من جص وبصر الأرض غلظها وبصر فلان تبصيرا إذا أتى البصرة (tahdhib)؛ البصرة حجارة رخوة تلمع ويقال له بصر (mufradat)

## ق س م (root_001226): 84:16 أُقْسِمُ

- **B001** yüz güzelliği — güzellik, güzel görünüş · eksiksiz güzellik · yüz, özellikle yüzün güzel bölümü · yakışıklı ya da güzel yaradılışlı erkek · güzel yüzlü · yüzü güzel ve uyumlu · güzel yüz · güzel yüzlü kadın · güzel
  القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)
- **B002** şiddetli öğle sıcağı veya vakti — şiddetli öğle sıcağı veya öğle sıcağı vakti
  والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)
- **B003** paylara ayırma ve ayrılmış pay — bir şeyi parçalara veya paylara ayırmak · paylara ayırma · pay, kişiye düşen bölüm · bölüştürme, paylaşma · arazi veya evleri paylaştıran kimse · birlikte paylaşan ortak · öteki araziden ayrılmış arazi · az suyu eşit paylaştırmaya yarayan taş · kişilere ayrılmış paylar · ayırma ve dağıtma · zaman onları ayırıp dağıttı
  تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)
- **B004** yemin etme ve öldürme davasında paylaştırılan yeminler — yemin · yemin etti · ona yemin etti veya onunla antlaştı · Tanrı adına karşılıklı yemin ettiler · öldürme davasında yakınlara paylaştırılan yeminler
  اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)
- **B005** işaretli ok çekerek karar arama [kalıp] — işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme
  الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)
- **B006** işi ölçüp biçme; kaygıyla zihnin dağılması — işini ölçüp biçiyor ve nasıl yapacağını düşünüyor · kaygının dağıttığı zihin · kaygılar yüzünden düşüncesi dağılmış
  أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)
- **B007** yalıtık adlandırmalar — giysiyi ilk kez katlayıp kat izlerini oluşturan kimse · iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at
  القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)
- **B008** düşman ile Müslümanlar arasındaki ateşkes — düşman ile Müslümanlar arasındaki ateşkes
  القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)

## ش ف ق (root_000803): 84:16 بِٱلشَّفَقِ

- **B001** incelik, düşük nitelik ya da azlık — ince, düşük nitelikli veya az şey · ince ya da düşük nitelikli giysi veya örtü · dokumayı düşük nitelikli yapmak veya verilecek miktarı azaltmak · azaltılmış veya az miktardaki bağış
  أصل واحد يدل على رقة في الشيء (maqayis)؛ الشفق الرديء من الأشياء (maqayis;ayn;sihah;tahdhib)؛ شفق الثوب أي جعله في النسج شفقا (tahdhib)؛ عطاء مشفق أي مقلل (sihah)
- **B002** gün batımı kızıllığı — gün batımından sonra kalan kızıllık veya gündüz aydınlığı · bazı hukukçulara göre akşam kızıllığından sonra kalan beyazlık
  الشفق الحمرة التي بين غروب الشمس إلى وقت صلاة العشاء الآخرة (maqayis;ayn;sihah)؛ الشفق الحمرة التي في المغرب من الشمس (tahdhib)؛ اختلاط ضوء النهار بسواد الليل عند غروب الشمس (mufradat)
- **B003** kaygılı ilgi ve sakınma — kaygıyla gözetme ve sakınma · bir şeyden çekinip sakınmak · biri için kaygılanıp onu gözetmek · iyiliğini kaygıyla gözeten dikkatli öğütçü · bir şeyden çekinmek; seyrek ve tartışmalı kullanım
  أشفقت من الأمر إذا رققت وحاذرت (maqayis)؛ الشفق الخوف وهو مشفق أي خائف (ayn;tahdhib)؛ أشفقت عليه فأنا مشفق وشفيق وأشفقت منه تعني حذرته (sihah)؛ الإشفاق عناية مختلطة بخوف (mufradat)
- **B004** erzakı esirgemek veya bağışı kısmak [kalıp] — erzakı veya geçimliği cimrice esirgemek · azaltılmış veya az miktardaki bağış
  كما شفقت على الزاد العيال فمعناه بخلت به (maqayis)؛ عطاء مشفق أي مقلل (sihah)؛ إذا شفقت على الرزق العيال (tahdhib)
- **B005** bir işin çeşitli yönleri içinde olmak [kalıp] — bu işin çeşitli yönleri veya tarafları içindeyim
  أنا في أشفاق من هذا الأمر أي نواح منه (tahdhib)؛ ومثله أنا في عروض منه وفي أعراض منه أي في نواح (tahdhib)

## ل ي ل (root_001392): 84:17 وَٱلَّيْلِ

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## و س ق (root_001648): 84:17 وَسَقَ, 84:18 ٱتَّسَقَ

- **B001** üzerinde veya içinde taşımak — bir şeyi taşıyıp yükünü kaldırmak · gözün suyu içinde tutması · deveye yük yüklemek · dişi hayvanın karnında yavru taşıması · palmiye ağacının meyve vermesi · palmiye ağacının bol meyve vermesi
  كلمة تدل على حمل الشيء؛ وسقت العين الماء حملته؛ أوسقت البعير حملته حمله (maqayis)؛ الوسق حمل؛ أوسقت البعير أوقرته (ayn)؛ وسقت الشيء جمعته وحملته؛ ما وسقت عيني الماء؛ وسقت الناقة وغيرها حملت؛ أوسقت النخلة كثر حملها (sihah)؛ وسقت الشيء إذا حملته؛ كل شيء حملته فقد وسقته؛ وسقت الأتان إذا حملت ولدا؛ وسقت النخلة إذا حملت (tahdhib)
- **B002** toplamak veya bir araya gelmek — bir şeyi toplayıp parçalarını birleştirmek · gecenin örttüğü şeyleri bir araya toplaması · develerin bir araya gelip toplanması · develeri toplamak · işi zihninde toparlayamamak · işin mümkün hale gelip yoluna girmesi
  والليل وما وسق أي جمع وحمل (maqayis)؛ الوسق ضمك الشيء إلى الشيء؛ استوسقت الإبل اجتمعت وانضمت؛ يسقها أي يجمعها؛ وما وسق أي جمع (ayn)؛ وسقت الشيء جمعته وحملته؛ فإذا جلل الليل الجبال والأشجار والبحار والأرض فاجتمعت له فقد وسقها؛ استوسقت الإبل اجتمعت (sihah)؛ وما وسق أي ما جمع وضم؛ وما جمع من الجبال والبحار والأشجار؛ لا يسق لي باله أي لا يجتمع لي أمره (tahdhib)؛ الوسق جمع المتفرق؛ وسقت الشيء إذا جمعته (mufradat)
- **B003** altmış birimlik sabit hacim ölçüsü — altmış küçük hacim birimine eşit ölçü · buğdayı ölçülük bölümlere ayırmak
  الوسق وهو ستون صاعا (maqayis)؛ الوسق حمل يعني ستين صاعا (ayn)؛ الوسق ستون صاعا؛ وسقت الحنطة توسيقا أي جعلتها وسقا وسقا (sihah)؛ خمسة أوسق من التمر؛ الوسق مكيلة معلومة وهي ستون صاعا؛ كل وسق بالملجم ثلاثة أقفزة (tahdhib)
- **B004** düzenli biçimde bütünleşip tamamlanmak — uyumlu biçimde birleşip düzenli hale gelme · ayın dolup düzgün bir bütün haline gelmesi
  الاتساق الانضمام والاستواء كاتساق القمر إذا تم وامتلأ فاستوى (ayn)؛ الاتساق الانتظام (sihah)؛ اتساقه امتلاؤه واجتماعه واستواؤه ليلة ثلاث عشرة وأربع عشرة؛ امتلاؤه واتساقه (tahdhib)
- **B005** hayvanları topluca sürmek; sürülen hayvan grubu — hayvanları bir arada sürmek ve önüne katmak · birlikte sürülen deve grubu · eşek sürüsü
  الوسيقة من الإبل كالرفقة من الناس؛ وسيقة الحمار عانته (ayn)؛ الوسق الطرد؛ الوسيقة وهي من الإبل كالرفقة من الناس فإذا سرقت طردت معا (sihah)؛ الطريدة من الإبل وسيقة لأن طاردها إذا طردها وسقها أي جمعها وقبضها؛ الوسيقة القطعة من الإبل يطردها السلال؛ وسيقة الحمار عانته (tahdhib)
- **B006** denk biçimde karşı çıkıp boy ölçüşmek — birine karşı çıkıp onunla boy ölçüşmek ve geri kalmamak · denkler arasında karşılıklı çekişme
  واسقت فلانا مواسقة إذا عارضته فكنت مثله ولم تكن دونه؛ الوساق والمواسقة المناهدة (tahdhib)
- **B007** uçarken kanatlarını çırpan kuş — uçarken kanatlarını çırpan kuş
  مما شذ عنه طائر ميساق وهو ما يصفق بجناحيه إذا طار وقد يهمز (maqayis)؛ الميساق الطائر الذي يصفق بجناحيه إذا طار (sihah)؛ المئساق وجمعه مآسيق؛ هكذا روي لنا بالهمز (tahdhib)

## ق م ر (root_001255): 84:18 وَٱلْقَمَرِ

- **B001** Ay, ay ışığı ve ayla aydınlanan gece — gökteki Ay · küçük Ay; Ay adının küçültme biçimi · ay ışığı · ay ışığıyla aydınlanan gece · Ay üzerimize doğdu
  القمر قمر السماء سمى قمرا لبياضه (maqayis)؛ القمراء ضوء القمر وليلة مقمرة (ayn;tahdhib)؛ القمر بعد ثلاث ليال إلى آخر الشهر (sihah)؛ القمر قمر السماء يقال عند الامتلاء (mufradat)
- **B002** ay ışığını andıran beyaz ya da yeşile çalan açık renk — beyaz ya da yeşile çalan açık renkli · yeşile çalan beyazımsı renk
  حمار أقمر أي أبيض (maqayis)؛ القمرة لون الحمار الأقمر وهو لون يضرب إلى الخضرة (ayn;tahdhib)؛ سحاب أقمر وأتان قمراء بيضاء وهجان أقمر (sihah;tahdhib)؛ حمار أقمر على لون القمراء (mufradat)
- **B003** ay ışığında yaklaşma, avı gafil yakalama ve avlama — ona ay ışığında gitti · aslan ay ışığında ava çıktı · kuşların gece görüşünü şaşırtıp onları avladılar · ona ay ışığında gitti; gafletinden yararlanıp aldattı; başka bir açıklamada onunla evlenip onu götürdü
  تقمرته أتيته في القمراء (maqayis;sihah;mufradat)؛ تقمر الأسد إذا خرج في القمراء يطلب الصيد (maqayis;sihah)؛ قمر القوم الطير إذا عشوها ليلا فصادوها (maqayis)؛ تقمرها أتاها في القمراء وطلب غرتها وخدعها (tahdhib)؛ تقمر الصياد الظباء والطير بالليل فتقمر أبصارها فتصاد (tahdhib)
- **B004** olgunlaşmadan soğuğa uğrayıp tatsızlaşma — palmiye meyvesi olgunlaşmadan soğuğa uğrayıp tadını ve tatlılığını yitirdi
  قمر التمر وأقمر إذا ضربه البرد فذهبت حلاوته قبل أن ينضج (maqayis)؛ أقمر التمر أي لم ينضج حتى أصابه البرد فذهبت حلاوته وطعمه (ayn;tahdhib)؛ أقمر التمر ضربه البرد فذهبت حلاوته قبل أن ينضج (sihah)
- **B005** kar beyazlığından gözü kamaşıp görememe — kar beyazlığında gözü kamaşıp göremez oldu
  قمر الرجل إذا لم يبصر في الثلج (maqayis;sihah)؛ قمر الرجل إذا حار بصره في الثلج فلم يبصر (tahdhib)
- **B006** su tulumunun ay aydınlığı ya da katman arası suyla bozulması — su tulumu ay aydınlığından yanmış gibi ya da su deri katmanları arasına girdiği için bozuldu
  قمرت القربة وهو شيء يصيبها كالاحتراق من القمر (maqayis)؛ قمرت القربة... يصيبها من القمر كالاحتراق فيدخل الماء بين الأدمة والبشرة (sihah)؛ قمرت القربة... دخل الماء بين الأدمة والبشرة فأصابها قضاء وفساد (tahdhib)؛ قمرت القربة فسدت بالقمراء (mufradat)
- **B007** değer ortaya koyulan talih oyununda karşılaşma, yenme ve aldatma — para ya da mal ortaya konan talih oyunu ve bu oyunda karşılıklı yarışma · onunla talih oyununda yarışıp onu yendi · oynayacak rakip aradı ya da rakibini yendi · onu hileyle aldattı
  القمار من المقامرة... تقمر الرجل إذا طلب من يقامره (maqayis)؛ قامرته فقمرته من القمار (ayn)؛ تقمر فلان أي غلب من يقامره وتقامروا لعبوا القمار وقمرت الرجل إذا لاعبته فغلبته (sihah)؛ القمار مأخوذ من الخداع يقال قامره بالخداع فقمره (tahdhib)؛ قمرت فلانا خدعته عنه (mufradat)
- **B008** su ve otlağın bol olması — su ve otlak bol oldu
  قمر الماء والكلأ إذا كثر (tahdhib)
- **B009** ay ışığında uykusu kaçıp uyuyamama — ay ışığında uykusu kaçtı ve uyuyamadı
  قمر الرجل أرق في القمر فلم ينم (tahdhib)
- **B010** develerin akşam yeminin gecikmesi — develerin akşam yemi gecikti
  قمرت الإبل إذا تأخر عشاؤها (tahdhib)
- **B011** hayvan sürüsünü gece çobansız ve gözetimsiz bırakma [kalıp] — hayvan sürüsünü gece çobansız ve gözetimsiz bıraktım
  استرعيت مالي القمر إذا تركته هملا ليلا بلا راع يحفظه (tahdhib)؛ لم أسترعها الشمس والقمر أي لم أهملها (tahdhib)
- **B012** üveyik ya da güvercin benzeri kuş — üveyik ya da güvercin benzeri kuş ve bu kuşların çoğulu
  القمري طائر كالفاختة مسكنه الحجاز (ayn)؛ القمرى منسوب إلى طير قمر والجمع قماري (sihah)؛ القمري طائر يشبه الحمام (tahdhib)

## ر ك ب (root_000589): 84:19 لَتَرْكَبُنَّ

- **B001** bineğe ya da tekneye binme ve üzerinde veya içinde bulunma — hayvana ya da tekneye binmek · binen kimse; özellikle deve yolcusu · binekli yolcu topluluğu · yolcu taşıyan develer · gemi yolcuları · binilen hayvan ya da taşıt · binek hayvanı veya kara ya da deniz taşıtı; binme yeri veya binme eylemi · eyer üzengisi · develerle taşınan yağ · binmeye elverişli dişi deve · binilecek çağa gelmek · başkasının atıyla savaşa katılan kimse
  يقال ركب ركوبا يركب والركاب المطي (maqayis); الركوب في الأصل كون الإنسان على ظهر حيوان وقد يستعمل في السفينة (mufradat); الركبان والأركوب والركب فراكبو الدابة وركاب السفينة الذين يركبونها (ayn;tahdhib); الركاب الإبل التي يسار عليها والركوب والركوبة ما يركب (sihah;tahdhib); ركاب السرج معروف (jamhara;sihah;tahdhib); المركب الذي يغزو على فرس غيره (maqayis;ayn;jamhara;tahdhib)
- **B002** üstüne çıkma veya üst üste yığılma — bir şeyin başka bir şeyin üstüne çıkması · hörgücün önündeki üst üste yağ katmanları · üst üste binmiş, yığılmış · bulutları taşıyan ya da üstlerine çıkan rüzgarlar
  أصل واحد مطرد منقاس وهو علو شيء شيئا (maqayis); كل شيء علا شيئا فقد ركبه (ayn;tahdhib); رواكب الشحم طرائق بعضها فوق بعض (maqayis;ayn;tahdhib); تراكب السحاب وتراكم صار بعضه فوق بعض (tahdhib); المتراكب ما ركب بعضه بعضا (mufradat); الرياح ركاب السحاب (ayn;tahdhib)
- **B003** işe girişme, yükleme veya yük altında kalma — birine iş yüklemek; işi ya da suçu işlemek · borç altında kalmak · vergi toplayan görevlilere haksız yük çıkaran kişi
  ركب فلان فلانا بأمر وارتكبه وكل شيء علا شيئا فقد ركبه وركبه الدين ونحوه (ayn;tahdhib); ارتكاب الذنوب إتيانها (sihah); ركيب السعاة بمعنى الراكب يركب السعاة فيظلمهم (tahdhib)
- **B004** parçayı yerine geçirip sabitleme — bir parçayı bir şeyin içine yerleştirip sabitlemek · yerine takılmış parça · parçaların düzenli biçimde birleştirilmesi
  كل شيء أثبته في شيء فقد ركبته نحو السنان في الرمح وغيره (jamhara); تركيب الفص في الخاتم والنصل في السهم ركبته فتركب فهو مركب وركيب (sihah); المركب المثبت في الشيء كتركيب الفصوص (ayn); شيء حسن التركيب والركيب اسما للمركب في الشيء مثل الفص ونحوه (tahdhib)
- **B005** diz eklemi ve dizle kurulan vurma ilişkisi — diz eklemi · dizi iri ya da kusurlu olan · dizine vurmak ya da kendi diziyle vurmak
  ركبة الإنسان وهي عالية على ما هي فوقه (maqayis); ركبة البعير في يده (ayn;tahdhib); الركبة معروفة (jamhara;sihah;mufradat); الأركب العظيم الركبة (maqayis;sihah;tahdhib); ركبته أصبت ركبته وأصبته بركبتي (mufradat); ركبت الرجل إذا ضربته بركبتك أو ضربته بركبته (maqayis;jamhara;sihah)
- **B006** kasık ve üreme organı çevresindeki beden bölgesi — kasık kıllarının çıktığı bölge veya üreme organı çevresindeki etli kısım
  الركب ركب المرأة ولا يقال للرجل (maqayis;tahdhib); الأركاب للنساء خاصة (ayn); الركبان أصلا الفخذين اللذان عليهما لحم الفرج من الرجل والمرأة (jamhara); الركب منبت العانة للمرأة خاصة وقال الفراء للرجل والمرأة (sihah); الركب كناية عن فرج المرأة (mufradat)
- **B007** gövdeye bağlı köksüz sürgün ve bağlı bitki parçaları — gövdeye bağlı, toprağa kök salmamış hurma sürgünü · başakta ilk çıkan öncü parçalar · kesilmiş yabani otun dip kısmı
  الركابة شبه فسيلة من أعلى النخلة عند قمتها (maqayis;ayn;tahdhib); الراكب ما ينبت في جذوع النخل ليس له في الأرض عروق (ayn;sihah;tahdhib); الراكبة فسيلة تتعلق بالنخلة لا تبلغ الأرض (jamhara); ركبان السنبل سوابق السنبل التي تخرج في أوله (tahdhib); الركبة أصل الصليانة إذا قطعت (tahdhib)
- **B008** saygın soy ve toplumsal köken [kalıp] — soyu, kökeni ve toplumsal dayanağı saygın olan
  المركب الأصل والمنبت يقال هو كريم المركب (maqayis); رجل كريم المركب أي كريم أصل منصبه في قومه (ayn;sihah); هذا الرجل كريم المركب أي كريم الأصل (tahdhib)
- **B009** kanallar arası toprak sırtı ve tarımsal uzantıları — bağ kanalları arasındaki yüksek sırt; sıraya dikilmiş hurmalık ya da ekili tarla
  الركيب ما بين نهري الكرم وهو الظهر الذي بين النهرين ويكون عاليا على دونه (maqayis;ayn); الركيب ما بين نهري الكرم (tahdhib); ركيب من نخل وهو ما غرس سطرا على جدول أو غير جدول (tahdhib); يقال للقراح الذي يزرع فيه ركيب (tahdhib)
- **B010** koyunlarda sırtı etkileyen hastalık — koyunların sırtını etkileyen hastalık
  الراكب داء يأخذ الغنم في ظهورها (maqayis)

## ط ب ق (root_000927): 84:19 طَبَقًا, 84:19 طَبَقٍ

- **B001** üstüne örtüp kapatmak — bir şeyi ötekinin üstüne koyup örtmek · kapak; üstüne örtülen parça · yeryüzünün tamamını kaplayan şey
  وضع شيء مبسوط على مثله حتى يغطيه (maqayis)؛ الطبق كل غطاء لازم (ayn)؛ أطبقت الشيء أي غطيته وجعلته مطبقا (sihah)؛ رحمة الله طباق الأرض أي تغشى الأرض كلها (tahdhib)؛ أطبقت عليه الباب (mufradat)
- **B002** üst üste katmanlar — omurga katmanı veya ince ayırıcı kemik · katman; üst üste duran bölüm · birbirinin üstünde kat kat gökler
  الطبق عظم رقيق يفصل بين الفقارتين (maqayis)؛ السماوات طباق بعضها فوق بعض (ayn)؛ منزلة فوق منزلة والسماوات الطباق بعضهن فوق بعض (jamhara)؛ طبقات الناس في مراتبهم والسموات طباق (sihah)؛ كل فقارة طبقة والطبقة من الأرض (tahdhib)؛ سبع سماوات طباقا أي بعضها فوق بعض (mufradat)
- **B003** uygun düşmek ve uyuşmak — uygunluk; birbirine uygun hale getirme · bir konuda birleşip fikir birliğine varmak · birbirine tam uyan iki kişi veya şey için söylenen söz
  أطبق الناس على كذا كأن أقوالهم تساوت (maqayis)؛ أطبق القوم على هذا الأمر أي اجتمعوا وصارت كلمتهم واحدة (ayn)؛ طابق فلان فلانا على الأمر إذا مالأه عليه (jamhara)؛ المطابقة الموافقة والتطابق الاتفاق (sihah)؛ طابق فلان فلانا إذا وافقه وعاونه (tahdhib)؛ طابقته على كذا وتطابقوا وأطبقوا عليه ومنه جواب يطابق السؤال (mufradat)
- **B004** durumdan duruma geçmek — durumdan duruma, aşamadan aşamaya · durum; geçilen aşama
  الطبق الحال (maqayis)؛ الطبقة الحال وطبقات شتى من الدنيا أي حالات (ayn)؛ طبقا عن طبق كأنها منزلة فوق منزلة (jamhara)؛ الطبق الحال أي حالا عن حال (sihah)؛ يترقى منزلا عن منزل وأحوال شتى (mufradat)
- **B005** benzerlerden oluşan sınıf — insan topluluğu veya benzer insanlardan oluşan sınıf · çekirge topluluğu · benzer kişilerden oluşan sınıf; toplumsal tabaka
  الطبق الجماعة من الجراد (maqayis)؛ الطبق جماعة من الناس (ayn)؛ الطبقة القوم المتشابهون والناس طبقات (jamhara)؛ أتانا طبق من الناس وطبق من الجراد أي جماعة (sihah)؛ لكل جماعة متطابقة هم في أم طبق وقيل الناس طبقات (mufradat)
- **B006** doğru noktaya tam isabet etmek [kalıp] — hakka isabet etmek; doğruyu bulmak · ekleme veya doğru delile tam isabet etmek · kılıçla eklem yerine vurup uzvu ayırmak
  طبق الحق إذا أصابه وطبق إذا أصاب المفصل (maqayis)؛ رجل يطبق المفصل إذا أصاب الحجة (jamhara)؛ طبق السيف إذا أصاب المفصل فأبان العضو (sihah)؛ طبقت أراد أصبت وجه الفتيا وأصله إصابة المفصل (tahdhib)؛ طبقته بالسيف (mufradat)
- **B007** adımları yakınlaştırmak veya izleri çakıştırmak — bağlı kişinin yakın adımlı yürüyüşü · arka ayağını ön ayağının bastığı yere koymak
  المطابقة فمشي المقيد ورجلاه تقعان متقاربتين (maqayis)؛ المطابقة في المشي كمشي المقيد (ayn)؛ وضع خفي رجليه في موضع خفي يديه (jamhara)؛ مطابقة الفرس وضع رجليه مواضع يديه (sihah)؛ المطابقة المشي في القيد وأن يضع الفرس رجله في موضع يده (tahdhib)؛ المطابقة في المشي كمشي المقيد (mufradat)
- **B008** yapışıp açılamama — yana yapışık veya açılmayan el · konuşamayan kişi; çiftleşemeyen erkek hayvan
  يد طبقة إذا التزقت بالجنب (maqayis)؛ طبقت يد البعير أو الإنسان إذا لصقت بجنبه (jamhara)؛ طبقت يده إذا كانت لا تنبسط والطباقاء من الرجال العيي (sihah)؛ يد فلان طبقة واحدة إذا لم تكن منبسطة (tahdhib)؛ رجل عياياء طباقاء لمن انغلق عليه الكلام وفحل طباقاء (mufradat)
- **B009** kalıplaşmış bir felaket adı — büyük felaket; bazı anlatımlarda kaplumbağa veya yılan adı
  إحدى بنات طبق هي الداهية (maqayis)؛ بنت الطبق الداهية (jamhara)؛ بنت طبق سلحفاة ومنه قولهم للداهية إحدى بنات طبق (sihah)؛ بنات طبق وهي الداهية وقيل للحية أم طبق وبنت طبق (tahdhib)؛ عبر عن الداهية ببنت الطبق (mufradat)
- **B010** gece veya gündüzün bir bölümü [kalıp] — gecenin bir bölümü veya büyük kısmı · gündüzün bir saati, bölümü veya büyük kısmı
  طبقا عن طبق أي حالا عن حال يوم القيامة (ayn)؛ مر طبق من الليل ومن النهار أي معظم منه (jamhara)؛ مضى طبق من الليل وطبق من النهار أي معظم منه (sihah)؛ مضى طبق من النهار أي ساعة (tahdhib)؛ طبق الليل والنهار ساعاته المطابقة (mufradat)
- **B011** çeneleri kapatmak veya elleri belirli biçimde yerleştirmek — ibadette elleri belirli biçimde birleştirme
  إطباق الحنكين (ayn)؛ التطبيق في الصلاة جعل اليدين بين الفخذين في الركوع (sihah)؛ التطبيق في حديث ابن مسعود أن يضع كفه اليمنى على اليسرى والتطبيق في الركوع (tahdhib)

## ء م ن (root_000054): 84:20 يُؤْمِنُونَ, 84:25 ءَامَنُوا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ق ر ء (root_001210): 84:21 قُرِئَ, 84:21 ٱلْقُرْءَانُ

- **B001** toplamak ve bir araya getirmek — bir şeyi toplayıp parçalarını birleştirmek · insanların toplandığı yerleşim · konukların çevresinde toplandığı veya yiyeceğin toplandığı büyük kap · develerin su içmeye geldiği uzun yalak · sıkma düzeneğine benzeyen araç · kemiklerin birleştiği sırt · içindekileri toplayan kursak
  أصل صحيح يدل على جمع واجتماع (maqayis-v4;maqayis-v5)؛ قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض (sihah)؛ معنى قرآن معنى الجمع (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض (mufradat)؛ الجرية أصلها قرية لأنها تقري الشيء أي تجمعه (maqayis-ibdal)
- **B002** okumak, okutmak ve birlikte okumak — kutsal metni, kitabı, şiiri veya anlatıyı okumak · düzenli ve güzel okuma · Kur'an; ayrıca okuma eylemi · okuyan kişi · ona Kur'an okumayı öğretmek veya okutmak · onunla karşılıklı okuyup çalışmak
  قرأت القرآن عن ظهر قلب أو نظرت فيه (ayn)؛ وقرأ فلان قراءة حسنة فالقرآن مقروء وأنا قارئ (ayn)؛ قرأت الكتاب قراءة وقرآنا ومنه سمي القرآن (sihah)؛ قرأت القرآن لفظت به مجموعا (tahdhib)؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا (tahdhib)؛ أقرأت غيري أقرئه إقراء (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل (mufradat)؛ قارأته دارسته (tahdhib;mufradat)
- **B003** aybaşı ya da arınma dönemi — aybaşı, arınma veya bunların dönemi · bekleme süresini belirleyen aybaşı ya da arınma dönemleri · kadının aybaşı olması, arınması veya döngü dönemine girmesi · kadının kanama görmesi veya aybaşı olması
  قرأت المرأة قرءا إذا رأت دما وأقرأت إذا حاضت (ayn)؛ القرء الحيض والقرء أيضا الطهر وهو من الأضداد (sihah)؛ القرء انقضاء الحيض وما بين الحيضتين (sihah)؛ الأقراء الحيض والأقراء الأطهار (tahdhib)؛ القرء اسم للوقت يصلح للحيض ويصلح للطهر (tahdhib)؛ اسم للدخول في الحيض عن طهر (mufradat)؛ القرء وقت يكون للطهر مرة وللحيض مرة (maqayis-v4;maqayis-v5)
- **B004** rahminde taşıyıp gebe olmak — dişi devenin rahminde yavru veya doğum artığı taşımak · dişi devenin gebe olması · gebe dişi deve
  فأما الناقة فإذا حملت قيل قرؤت قروءة (ayn)؛ القارئ الحامل (ayn)؛ ما قرأت هذه الناقة سلى قط وما قرأت جنينا (sihah)؛ لم تضم رحمها على ولد (sihah)؛ ما قرأت الناقة سلى قط وما قرأت ملقوحا قط (tahdhib)؛ لم تحمل علقة أي دما ولا جنينا (tahdhib)؛ ما قرأت هذه الناقة سلى كأنه يراد أنها ما حملت قط (maqayis-v4;maqayis-v5)
- **B005** vakit, yaklaşma veya gecikme — vakit · rüzgarların esme vakti · rüzgarın vaktine girmesi veya yıldızlara bağlanan yağmurun gecikmesi · ihtiyacın ya da işin yaklaşması veya gecikmesi · yolculuktan dönmek veya aileye yaklaşmak
  القارئ الوقت (sihah)؛ أقرأت الريح إذا دخلت في وقتها (sihah)؛ أقرأت النجوم إذا تأخر مطرها (sihah)؛ أقرأت حاجتك دنت (sihah)؛ هذا قارئ الرياح لوقت هبوبها (tahdhib)؛ أقرأت من سفري أي انصرفت وأقرأت من أهلي أي دنوت (tahdhib)؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر (tahdhib)؛ هبت الرياح لقارئها لوقتها (maqayis-v4;maqayis-v5)
- **B006** dindar okur; öğrenmeye yönelen kişi — dindar ve ibadete bağlı okur · ibadete bağlı okurlar veya çok dindar okur · kendini ibadete vermek, öğrenmek veya anlamak
  رجل قارئ عابد ناسك وفعله التقري والقراءة (ayn)؛ القراء الرجل المتنسك وقد تقرأ أي تنسك (sihah)؛ قرأت أي صرت قارئا ناسكا وتقرأت بهذا المعنى (tahdhib)؛ قال بعضهم تقرأت تفقهت (tahdhib)؛ تقرأت تفهمت (mufradat)
- **B007** esenlik dileğini iletmek [kalıp] — sana selamını iletti · sana selamını iletti; biçimin doğruluğu tartışmalıdır · selamımı alıp ilet
  فلان قرأ عليك السلام وأقراك السلام بمعنى (sihah)؛ اقرأ عليه السلام ولا يقال أقرئه السلام لأنه خطأ (tahdhib)؛ اقترئ مني السلام (tahdhib)
- **B008** yeni gelinen yöreye bağlı salgın etkisi [kalıp] — yeni gelinen yörenin zamanla geçen salgın etkisi
  القرأة بالكسر الوباء (sihah)؛ إذا قدمت بلادا فمكثت بها خمس عشرة فقد ذهبت عنك قرأة البلاد (sihah)؛ قرأة البلاد وأهل الحجاز يقولون قرة البلاد بغير همز (tahdhib)؛ إن مرضت بعد ذلك فليس من وباء البلاد (tahdhib)
- **B009** dişi devenin çiftleşme dönemi [kalıp] — erkek devenin, gebe kalıp kalmadığını anlamak için dişiyi bırakması · dişi devenin çiftleşme isteği veya dönemi
  استقرأ الجمل الناقة إذا تاركها لينظر ألقحت أم لا (sihah)؛ ضرب الفحل الناقة على غير قرء وقرء الناقة ضبعتها (tahdhib)؛ ما دامت الوديق في وداقها فهي في قرئها وإقرائها (tahdhib)
- **B010** biçime bağlı adlandırmalar — kadın köleyi aybaşı görene kadar gözetim altında tutmak · kadın kölenin gebe olmadığını aybaşı bekleyerek anlamak · onu hapsetmek
  دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (sihah)؛ دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (tahdhib)؛ قرأت الجارية استبرأتها بالقرء (mufradat)؛ أعتم فلان قراه وأقرأه أي حبسه (tahdhib)
- **B011** bir yolu veya örneği izlemek — tek bir yol, amaç veya izlenen yön · şiirin başka bir şiirin yöntem ve örneğine göre olması
  القرو كل شيء على طريقة واحدة (maqayis-v4;maqayis-v5)؛ رأيت القوم على قرو واحد (maqayis-v4;maqayis-v5)؛ القرو القصد تقول قروت وقريت إذا سلكت (maqayis-v4;maqayis-v5)؛ أقرأت في الشعر (tahdhib)؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله (tahdhib)
- **B012** bilgiyi toplayıp tanıklık eden kişi — tanık · yeryüzündeki tanıklar; bilgiyi toplayıp tanıklık edenler
  القارئة وهو الشاهد (maqayis-v4;maqayis-v5)؛ الناس قواري الله تعالى في الأرض هم الشهود (maqayis-v4;maqayis-v5)؛ ممكن أن يحمل هذا على ذلك القياس أي إنهم يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها (maqayis-v4;maqayis-v5)
- **B013** hayvan varlığı veya bakmakla yükümlü olunanlar — deve ve küçükbaş hayvan varlığı veya bakmakla yükümlü olunan aile
  القرة المال من الإبل والغنم (maqayis-v4;maqayis-v5)؛ والقرة العيال (maqayis-v4;maqayis-v5)

## ق ر ء (root_001211): 84:21 قُرِئَ, 84:21 ٱلْقُرْءَانُ

- **B001** biçime bağlı adlandırmalar — Kur'an; adı toplama anlamıyla ilişkilendirilmiş, fakat bu köken reddedilmiştir · Kur'an'ı sözlerini birleştirerek okumak · okuma ve sözleri söyleme · başkasına okutmak veya okumayı öğretmek · okuyan kişi · başkasına okutan veya okumayı öğreten kişi · dindar bir okur durumuna gelmek · dindar bir okur olmak veya öğrenmek · onunla karşılıklı okuyup çalışmak · birinden okumasını istemek; aktarımda açıklama verilmemiştir
  ومعنى قرآن معنى الجمع؛ قرأت القرآن لفظت به مجموعا؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا؛ أقرأت غيري إقراء؛ قارأت فلانا مقارأة أي دارسته؛ تقرأت تفقهت
- **B002** özel adlandırma kümesi — aybaşı veya arınmanın gerçekleştiği dönem · aybaşı ve arınma dönemleri · kadının aybaşı veya arınma dönemine girmesi · rüzgarların esme vakti · dişi devenin çiftleşme isteği · yeni gelinen yörenin ilk günlerdeki salgın etkisi
  الأقراء الحيض والأطهار؛ القرء اسم للوقت؛ قارئ الرياح لوقت هبوبها؛ قرء الناقة ضبعتها؛ قرأة البلاد
- **B003** rahimde toplanıp taşınmak — kanın rahimde toplanması · dişi devenin doğum artığı taşımaması veya dışarı atmaması · yavruyu rahminde toplamamak, taşımamak veya dışarı atmamak · rahminde bir aybaşılık kan toplamamış olmak
  لم تجمع جنينا؛ لم تضطم رحمها على الجنين؛ لم تلقه؛ ما قرأت الناقة سلى قط أي ما طرحت وتأويله ما حملت؛ القرء اجتماع الدم في الرحم؛ ما ضمت رحمها على حيضة
- **B004** biçime bağlı adlandırmalar — 
  أقرأت من سفري أي انصرفت؛ أقرأت من أهلي أي دنوت؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر؛ أعتم فلان قراه وأقرأه أي حبسه
- **B005** şiiri başka bir şiirin örneğine göre kurmak — bu şiirin öteki şiirin yöntem ve örneğine göre olması · şiir bağlamında kullanmak; bağımsız anlamı açıklanmamıştır
  أقرأت في الشعر؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله؛ على قري هذا الشعر وغراره
- **B006** belirli kalıpla selam iletmek — ona selam ilet · selamımı alıp ilet · selam iletmek için yanlış sayılan biçim
  اقرأ عليه السلام ولا يقال أقرئه السلام؛ اقترىء مني السلام

## س ج د (root_000675): 84:21 يَسْجُدُونَ

- **B001** alçalıp boyun eğme ve alnı yere koyma — boyun eğmek veya alnını yere koymak · alçalıp boyun eğme; isteyerek ya da zorunlu düzene bağlılık · bir kez alnını yere koyarak eğilme veya bu eğilişin biçimi
  أصل واحد مطرد يدل على تطامن وذل (maqayis)؛ سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض (sihah)؛ سجد إذا وضع جبهته بالأرض (tahdhib)؛ السجود أصله التطامن والتذلل (mufradat)
- **B002** alnı yere koyma yeri, buna ayrılmış yapı veya küçük yaygı — toplu tapınma yeri veya bu amaçla kurulmuş yapı · zeminde alnın konduğu yer · iki belirli kutsal kentteki iki tanınmış tapınma yapısı · üzerinde alnı yere koyarak eğilinen küçük dokuma yaygı · tapınma yerleri veya alnı yere koymaya elverişli yerler
  المسجد اسم جامع يجمع المسجد وحيث لا يسجد بعد أن يكون اتخذ لذلك (ayn)؛ المسجد معروف (jamhara)؛ المسجد والمسجد واحد المساجد والمسجدان مسجد مكة ومسجد المدينة (sihah)؛ المسجد موضع الصلاة (mufradat)؛ السجادة الخمرة (sihah)
- **B003** yere dayanan beden bölümleri ve alındaki temas izi — alnı yere koyarken yere dayanan beden bölümleri · alnın yere değen ve temas izi oluşan bölümü · alında tekrarlanan yere temasın bıraktığı iz
  المسجد الإرب الذي يسجد عليه مثل الكفين والركبتين والقدمين والجبهة (jamhara)؛ الآراب السبعة مساجد والمسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود (sihah)؛ المساجد مواضع السجود من الإنسان الجبهة والأنف واليدان والركبتان والرجلان (tahdhib;mufradat)
- **B004** başı ve gövdeyi aşağı eğme veya yük altında yana yatma — başını alçaltıp gövdesini öne eğmek · belden öne eğilmiş durumda olmak · meyve yüküyle eğilip yana yatmış hurma ağacı
  أسجد الرجل إذا طأطأ رأسه وانحنى (maqayis;sihah;tahdhib)؛ أسجد للبعير أي طأطأ لها لتركبه (sihah;tahdhib)؛ سجدا أي ركعا (tahdhib)؛ نخلة ساجدة إذا أمالها حملها (tahdhib)
- **B005** bakışı aşağıda ve devinimsiz tutma, göz kapaklarında gevşeklik — bakışı aşağı yönelmiş durumda uzun süre ve devinimsiz tutma · durgun ve gevşek bakışlı göz · gözleri durgun ve gevşek görünen kadınlar
  الإسجاد إذا أدام النظر في خفض (maqayis)؛ الإسجاد إدامة النظر مع سكون (ayn;tahdhib)؛ أصل السجود إدامة النظر في إطراق إلى الأرض (jamhara)؛ الإسجاد إدامة النظر وإمراض الأجفان (sihah)؛ نساء سجد فاترات الأعين وامرأة ساجدة ساجية (ayn)؛ الإسجاد أيضا فتور الطرف (tahdhib)
- **B006** önünde eğilinilen hükümdar betimli sikkeler [kalıp] — üzerlerindeki betimler veya betimlenen hükümdar önünde eğilinilen sikkeler
  دراهم الإسجاد دراهم كانت عليها صور فيها صور ملوكهم وكانوا إذا رأوها سجدوا لها (maqayis)؛ دراهم كانت عليها صور يسجدون لها (sihah)؛ دراهم عليها صورة ملك سجدوا له (mufradat)
- **B007** Yahudiler için ad, baş vergisi ve bu verginin parası — Yahudiler · baş vergisi · baş vergisi olarak verilen para
  الإسجاد بكسر الهمزة اليهود (tahdhib)؛ أعطونا إسجادا أي الجزية (tahdhib)؛ دراهم الأسجاد عنى دراهم الجزية (tahdhib)

## ك ف ر (root_001307): 84:22 كَفَرُوا۟

- **B001** örtmek, kapatmak — bir şeyi örtmek ve kapatmak · zırhının üstüne bir giysi geçirmek · silahlarıyla örtünmek veya silah kuşanmak · rüzgârın savurduğu toprakla örtülmüş kül · güneşin yıldızları görünmez kılması
  الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)
- **B002** örten karanlık veya enginlik — karanlık gece, deniz, büyük ırmak, gün batımı veya bulut
  الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)
- **B003** dinî gerçeği reddetme — dinî gerçeği veya inancı reddetme · kalben bildiği gerçeği diliyle kabul etmeme · gerçeği bildiği hâlde inatla kabul etmemek · kalben reddederken diliyle inanmış görünmek · gerçeği hem kalple hem dille inkâr etmek
  الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)
- **B004** nimeti yadsıma — nimeti yadsımak ve şükrünü yerine getirmemek · nimeti yadsıma ve şükretmeme · nimetleri aşırı biçimde yadsıyan kimse · iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam
  كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)
- **B005** bağını reddedip uzaklaşmak — bir şeyle bağını reddedip ondan uzaklaşmak
  يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)
- **B006** inançsız saymak — birini inançsız saymak veya öyle adlandırmak
  أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)
- **B007** itaatsizliğe zorlamak — itaat eden birini itaatsizliğe zorlamak
  إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)
- **B008** tohumu örten çiftçi — tohumu toprakla örten çiftçi · tohumları toprakla örten çiftçiler
  يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)
- **B009** günah yükünü giderme — günahı veya bozulan yeminin yükünü gideren karşılık · bozulan yeminin gerektirdiği yükümlülüğü yerine getirme · günahları örtüp etkisini silme
  الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)
- **B010** çiçek veya meyve kılıfı — üzüm salkımının veya hurma çiçeğinin kılıfı · hurma çiçeğinin ya da meyvenin kılıfı · hurma ağacından çıkan kapalı çiçek kılıfları
  الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)
- **B011** koku maddesi, su kaynağı veya bitki — güzel kokulu karışımlarda kullanılan madde · cennetteki bir su kaynağı · çiçeği papatyaya benzeyen bir bitki
  الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)
- **B012** uzak arazi; köy, uzak yer halkı veya mezar — insanlardan uzak, pek uğranmayan arazi · köy veya mezar · köyler veya uzak yerlerin halkı
  الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)
- **B013** dağ geçidi; iri dağ veya alçak duvar — dağ geçitleri · dağ geçidi veya iri dağ · alçak duvar
  الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)
- **B014** eğilerek boyun eğme gösterisi — başını eğmek veya elini göğsüne koyup eğilmek
  التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)
- **B015** hükümdara taç giydirme veya taç — hükümdara taç giydirme veya tacın kendisi
  التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)

## ك ذ ب (root_001290): 84:22 يُكَذِّبُونَ

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## ء ل ه (root_000047): 84:23 وَٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 84:23 وَٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ع ل م (root_001040): 84:23 أَعْلَمُ

- **B001** bilme ve gerçeğini kavrama — bilgi; bir şeyi gerçeğiyle kavrama · bir şeyi bilmek ve tanımak · haberinden haberdar olmak · bildirmek, haberdar etmek · öğretmek, öğrenmesini sağlamak · öğrenmek, kavramaya yönelmek · bilmek; buyrukta bil ki · bilgi yarışında yenmek · bilen ve bildiğine göre davranan kişi · bilgili, bilgi sahibi · çok bilgili, çok bilen · son derece bilgili kişi
  العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)
- **B002** ayırt edici ve yol gösterici işaret — ayırt edici işaret · bayrak, sancak · yol gösteren belirgin dağ · kumaşın kenar işareti veya deseni · yol gösteren iz veya belirti · savaşta kendine ayırt edici işaret takmak · kumaşı işaretlemek · işaret olarak kullanılan kına · sarığı tanıtıcı bir biçimde sarmak · tanınmış ve öne çıkan kişi · son saatin yaklaştığını gösteren belirti
  أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)
- **B003** evren ve bütün yaratılmışlar — evren veya yaratılmışlar bütünü · bütün yaratıklar veya varlık sınıfları · evrenler, varlık dünyaları
  العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)
- **B004** üst dudak yarığı — üst dudaktaki yarık · üst dudağı yarık kişi veya deve · üst dudağını yarmak
  العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)
- **B005** deniz ya da suyu bol kuyu — deniz · suyu bol kuyu
  العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)
- **B006** doğan veya atmaca türü yırtıcı kuş — doğan veya atmaca · çevik ve zeki adam
  العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)
- **B007** erkek sırtlan — erkek sırtlan
  العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)

## و ع ي (root_001664): 84:23 يُوعُونَ

- **B001** akılda tutmak ve içinde saklamak — sözü ya da bilgiyi akılda tutmak · akılda tutma; içte saklama · duyduğunu aklında tutan kulak · içlerinde yalanlama düşüncesini saklıyorlar · aklında tut
  وعى حديثا ونحوه أي حفظ (ayn)؛ وعى العلم يعيه وعيا (jamhara;maqayis)؛ وعاه أي حفظه ووعيت الحديث (sihah)؛ الوعي حفظ القلب للشيء (tahdhib)؛ الوعي حفظ الحديث ونحوه وتعيها أذن واعية (mufradat)؛ والله أعلم بما يوعون أي يضمرون في قلوبهم (sihah)
- **B002** bir kaba alma ve kap — eşyayı ya da azığı bir kaba koyup toplamak · eşyayı kaba koyup saklama · kap · kaplar · kap sözcüğünün bir söyleyiş biçimi · kaba konmuş ve içinde saklanan
  أوعيت شيئا في الوعاء وفي الإعاء (ayn)؛ أوعى المتاع إذا جمعه في وعاء (jamhara)؛ الوعاء واحد الأوعية وأوعيت الزاد والمتاع (sihah)؛ أوعى الشيء في الوعاء (tahdhib)؛ الإيعاء حفظ الأمتعة في الوعاء (mufradat)؛ أوعيت المتاع في الوعاء (maqayis)
- **B003** kırık kemiğin kaynayıp güçlenmesi [kalıp] — kırık kemiğin kaynayıp güçlenmesi · kemiğin eğri kaynaması
  وعى العظم إذا انجبر بعد كسر (ayn;sihah)؛ جبر العظم على وعي إذا لم يستو جبره (jamhara)؛ جبر العظم بعد الكسر على عثم وهو الاعوجاج (tahdhib)؛ وعى العظم اشتد وجمع القوة (mufradat)
- **B004** yarada irin birikmesi ya da akması — irinin yarada birikmesi · yaranın irin toplaması ya da irinin yaradan akması · irin
  وعت المدة في الجرح ووعت جايئته (ayn)؛ الوعي القيح والمدة وعت المدة في الجرح إذا اجتمعت (sihah)؛ إذا سال القيح من الجرح قيل وعى الجرح (tahdhib)؛ وعي الجرح جمع المدة (mufradat)
- **B005** feryat ve gürültü — ölünün ardından feryat eden kimse; ölüm feryadı · gürültü ve sesler · topluluğun sesleri · topluluğun feryadı · kovalama sırasında köpeklerin çıkardığı gürültü
  الواعية الصراخ على الميت والوعلأ جلبة وأصوات للكلاب (ayn)؛ واعية القوم أصواتهم وكذلك وعاهم (jamhara)؛ الوعى الجلبة والأصوات والواعية الصارخة (sihah;maqayis)؛ الواعية والوعي والوعى كلها الصوت (tahdhib)؛ الواعية الصارخة ووعي القوم صراخهم (mufradat)
- **B006** geri duramamak ve başka çare bulamamak [kalıp] — ondan geri duramamak, kendini ondan alamamak · ondan başka çare bulunmaması
  لا وعي لي عن كذا أي لا ارتداد لي عنه (jamhara)؛ لا وعي عن ذلك الأمر أي لا تماسك دونه ومالي عنه وعي أي بد (sihah)؛ مالي عنه وعي أي بد ولا وعي عن كذا أي لا تماسك دونه (tahdhib)؛ لا وعي عن كذا أي لا تماسك للنفس دونه ومالي عنه وعي أي بد (mufradat)؛ لا وعي عن كذا (maqayis)
- **B007** öksüzün bakımını üstlenen kimse [kalıp] — öksüzün bakımını üstlenen kimse
  بئس واعي اليتيم ووالي اليتيم وهو الذي يقوم عليه (tahdhib)
- **B008** çok sayıda erkeğin arasında [kalıp] — çok sayıda erkeğin arasında
  إنه لفي وعي رجال أي في رجال كثير (tahdhib)

## ب ش ر (root_000120): 84:24 فَبَشِّرْهُم

- **B001** derinin dış yüzü ve toprağın beliren bitkisi — derinin görünen dış yüzü · toprağın üzerinde beliren bitki örtüsü · toprak bitkisini çıkardı
  البشرة ظاهر جلد الإنسان (maqayis;sihah;mufradat)؛ البشرة أعلى جلد الوجه والجسد (ayn;tahdhib)؛ بشرة الأرض ما ظهر من نباتها وأبشرت الأرض إذا أخرجت نباتها (maqayis;sihah;tahdhib;mufradat)
- **B002** insan ya da insanlık — insan ya da insanlık
  وسمى البشر بشرا لظهورهم (maqayis)؛ البشر الإنسان الواحد رجلا كان أو امرأة (ayn)؛ البشر اسم يقع على الناس (jamhara)؛ البشر الخلق (sihah;tahdhib)؛ عبر عن الإنسان بالبشر اعتبارا بظهور جلده (mufradat)
- **B003** doğrudan temas etme veya işi bizzat yürütme [kalıp] — bir erkeğin bir kadınla ten tene yakınlaşması · kadına doğrudan tenle temas etme · işin başında bizzat bulunup onu yürütme
  باشر الرجل المرأة إفضاؤه ببشرته إلى بشرتها (maqayis)؛ مباشرة الرجل المرأة لتضام أبشارهما (ayn;tahdhib)؛ مباشرة المرأة ملامستها (sihah)؛ باشر الرجل المرأة إذا ألصق بشرته ببشرتها (jamhara)؛ المباشرة الإفضاء بالبشرتين (mufradat)؛ مباشرة الأمر أن تحضره بنفسك (ayn;sihah;tahdhib)
- **B004** dış katmanı soyma, soyulan parça ve yüzeydekini tüketme — işlenmiş derinin dış yüzünü soydu · derinin dış katmanını soyma · işlenmiş deriden soyulup düşen parça · çekirgeler yerin üstündekileri yedi
  بشرت الأديم إذا قشرت وجهه (maqayis)؛ البشر قشرك البشرة عن الجلد (ayn)؛ بشرت الأديم إذا قشرت بشرته وبشارة الأديم ما سقط منه (jamhara)؛ بشرت الأديم إذا أخذت بشرته (sihah;tahdhib)؛ بشرت الأديم أصبت بشرته وبشر الجراد الأرض إذا أكلته (mufradat)؛ بشر الجراد الأرض إذا أكل ما عليها (sihah;tahdhib)
- **B005** sevindirici haber verme; kötü haberde açık nitelemeli alaycı bildirim — adama sevindirici haber verdi · ona sevindirici bir haber verdi · sevindirici haber · sevindirici haber · iyi ya da kötü haberi getiren kişi · onlara acı verici cezayı alaycı biçimde haber verdi · sevindirici haberi alınca sevindi · topluluk üyeleri birbirlerine sevindirici haber verdiler
  بشرت فلانا تبشيرا وذلك يكون بالخير وربما حمل عليه غيره من الشر (maqayis)؛ البشارة ما بشرت به والبشير المبشر بخير أو شر والبشرى الاسم (ayn;tahdhib)؛ بشرت الرجل وبشرته بما يسر به والبشرى والبشارة اسم لما بشرت به (jamhara)؛ البشارة المطلقة لا تكون إلا بالخير وإنما تكون بالشر إذا كانت مقيدة به (sihah)؛ أخبرته بسار بسط بشرة وجهه ويقال للخبر السار البشارة والبشرى (mufradat)
- **B006** güler yüzlülük ve güzel görünüş — güler yüzlülük · güzellik ve hoş görünüş · güzel yüzlü kişi · güzel yüzlü kadın · yaradılışı ve ten rengi güzel genç kadın · güzel ya da orta yapılı, ne zayıf ne semiz deve
  البشير الحسن الوجه والبشارة الجمال (maqayis)؛ البشارة الجمال وامرأة بشيرة (ayn)؛ البشر طلاقة الوجه وفلان حسن البشر والبشارة الجمال وحسن الهيئة (jamhara)؛ حسن البشر أي طلق الوجه والبشير الجميل وناقة بشيرة أي حسنة (sihah)؛ فلان يلقاني ببشر أي بوجه منبسط عند السرور ورجل بشير الوجه وامرأة بشيرة الوجه (tahdhib)؛ تباشير الوجه وبشره ما يبدو من سروره (mufradat)
- **B007** bir şeyin ilk belirtileri ve başlangıç görünümleri — sabahın ilk ışıkları · hurmanın ilk olgunlaşma belirtileri · yağmurun yaklaştığını bildiren rüzgârlar · bir şey tamamlanmadan önce beliren ilk izler
  تباشير الصبح أوائله وكذلك أوائل كل شيء (maqayis;ayn;sihah)؛ تباشير النخل أول ما يرطب ورأى الناس التباشير في النخل إذا رأوا الحمرة والصفرة (jamhara)؛ التباشير طرائق ضوء الصبح في الليل وآثار الرياح وآثار جنب الدابة (tahdhib)؛ المبشرات الرياح التي تبشر بالغيث (maqayis;ayn;sihah;tahdhib;mufradat)؛ تباشير الوجه وبشره ما يبدو من سروره وتباشير الصبح ما يبدو من أوائله وتباشير النخيل ما يبدو من رطبه (mufradat)
- **B008** yumuşaklıkla sağlamlığı ve dışla iç erdemleri birleştiren tam yetkinlik — yumuşaklıkla sağlamlığı ve iç-dış erdemleri birleştiren yetkin kişi · her yönden yetkin, iç ve dış erdemleri birleştiren kadın
  فلان مؤدم مبشر إذا كان كاملا من الرجال كأنه جمع لين الأدمة وخشونة البشرة (maqayis;sihah)؛ رجل مؤدم مبشر وهو الذي قد جمع لينا وشدة مع المعرفة بالأمور (tahdhib)؛ فلان مؤدم مبشر عبر بذلك عن الكامل الذي يجمع بين الفضيلتين الظاهرة والباطنة (mufradat)؛ فلانة مؤدمة مبشرة إذا كانت تامة في كل وجه (tahdhib)

## ع ذ ب (root_000994): 84:24 بِعَذَابٍ

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

## ء ل م (root_000046): 84:24 أَلِيمٍ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ع م ل (root_001046): 84:25 وَعَمِلُوا۟

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

## ص ل ح (root_000876): 84:25 ٱلصَّٰلِحَٰتِ

- **B001** iyi ve düzgün olma; düzeltme — iyilik, düzgünlük ve bozulmamışlık · iyi ve düzgün duruma gelmek · kendisi iyi ve düzgün olan kişi; iyi ve yararlı iş · işlerini düzelten veya başkasını iyi duruma getiren kimse · bozukluğu giderip iyi ve düzgün duruma getirme · hayvana iyi davranmak · iyilik ya da yarar sağlayan şey · iyi ve yararlı duruma getirmeye çalışma
  أصل واحد يدل على خلاف الفساد (maqayis)؛ الصلاح نقيض الطلاح ورجل صالح ومصلح وأصلحت إلى الدابة أحسنت إليها (ayn)؛ الصلاح ضد الطلاح وصلح الرجل صلاحا وصلوحا (jamhara)؛ الصلاح ضد الفساد والاصلاح نقيض الإفساد والمصلحة والاستصلاح (sihah)؛ الصلاح ضد الفساد مختصان في أكثر الاستعمال بالأفعال وإصلاح الله تعالى الإنسان (mufradat)
- **B002** barışma ve uzlaşma — barışma, uzlaşma ve aradaki soğukluğun giderilmesi · birbiriyle barışıp uzlaşmak
  والصلح تصالح القوم بينهم (ayn)؛ الصلاح بكسر الصاد المصالحة والاسم الصلح وقد اصطلحا وتصالحا واصالحا (sihah)؛ الصلح يختص بإزالة النفار بين الناس، يقال اصطلحوا وتصالحوا (mufradat)
- **B003** sana uygun olma [kalıp] — bu sana uygundur; bu sana uyar
  وهذا الشئ يصلح لك، أي هو من بابتك (sihah)
- **B004** kişi adı olan kök türevleri — bu kökten türemiş kişi adları; bunlardan biri bir peygamber adıdır
  وقد سمت العرب صالحا وصليحا ومصلحا (jamhara)؛ وصالح اسم للنبي عليه السلام (mufradat)
- **B005** bir kent ve bir nehir için özel adlar — belirli bir kentin özel adı · belirli bir nehrin özel adı
  إن مكة تسمى صلاحا (maqayis)؛ والصلح نهر بميسان (ayn)؛ وصلاح في وزن حذام وقطام وهو اسم مكة (jamhara)؛ وصلاح مثل قطام اسم مكة (sihah)

## ء ج ر (root_000015): 84:25 أَجْرٌ

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## غ ي ر (root_001119): 84:25 غَيْرُ

- **B001** yarar sağlayıp durumunu iyileştirme — aileyi geçindiren azık ve ihtiyaç payı · aileye geçimlik ve yarar sağlama · ailesine geçimlik sağladı ve yarar dokundurdu · ona yarar sağladı ve ihtiyacını giderdi · Tanrı onlara yağmur verip durumlarını iyileştirdi · yağmur toprağı suladı · sulanmış toprak · sulanmış toprak · yük takımlarını düzeltiyorlar · devesinin yükünü indirip durumunu düzeltti · hayvanı rahatlatmak için yük takımını düzenleyen kişi
  الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)
- **B002** cana karşılık ceza yerine kabul edilen kan bedeli — bana kan bedelini ödedi · kan bedeli · cana karşılık ceza yerine kabul edilen kan bedeli
  غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)
- **B003** biçimini değiştirme veya yerine başkasını koyma — şeyi değiştirdi ve öncekinden farklı hale getirdi · biçimini değiştirme veya yerine başkasını koyma · durumundan ayrılıp farklı hale geldi · yanlış olanı doğru olanla değiştirip giderdi · onunla alışverişte karşılıklı değiş tokuş yaptı · yerine konan karşılık
  الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)
- **B004** eşini veya ailesini kıskanarak koruma duygusu — eşini veya ailesini kıskanarak koruma duygusu · eşini veya ailesini kıskanıp sakındı · eşine veya ailesine karşı kıskanç ve korumacı · eşine veya ailesine karşı kıskanç erkek · eşine veya ailesine karşı kıskanç kadın · eşine veya ailesine karşı çok kıskanç kişi · eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi
  الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)
- **B005** başka olma, dışta bırakma veya olumsuzlama — başka, aynı olmayan veya aykırı · dışında, dışta bırakarak · değil, olmayan · doğru olmayan, yanlış · biri öteki olmayan iki şey · şeyler birbirinden farklılaştı
  هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)

## م ن ن (root_001449): 84:25 مَمْنُونٍۭ

- **B001** kesip eksilterek sürekliliği sona erdirme — ipi kesmek · kesme veya eksiltme · kesintisiz ve eksiltilmemiş · ömürleri kesip sayıyı azaltan ölüm veya zaman · yürümeyi kestiren aşırı yorgunluk
  المن: القطع؛ مننت الحبل: قطعته؛ المنون: المنية لأنها تنقص العدد وتقطع المدد؛ المن: الإعياء... المعيي ينقطع عن السير (maqayis)؛ المن: القطع ويقال النقص؛ لهم أجر غير ممنون؛ المنون: الدهر؛ المنون: المنية... تقطع المدد وتنقص العدد (sihah)؛ غير مقطوع ولا منقوص؛ المنون للمنية لأنها تنقص العدد وتقطع المدد (mufradat)
- **B002** ayakta tutan güç ve bu gücün zayıflığı — insanı ayakta tutan güç · dayanma gücü zayıf · güçsüz veya dayanıksız
  المنة، وهي القوة التي بها قوام الإنسان (maqayis)؛ المنة بالضم: القوة؛ هو ضعيف المنة؛ رجل منين؛ المنين: الحبل الضعيف؛ المنين: الغبار الضعيف (sihah)
- **B003** iyilik yapma ve bunu yük ya da başa kakma haline getirme — birine iyilik etmek veya yaptığı iyilikle onu yük altında bırakmak · karşıdakini yük altında bırakan iyilik · yaptığı iyiliği sözle başa kakma · bol bol bağışlayıp iyilik eden · yaptığı iyiliği çokça başa kakan · ver veya harca · verdiğini başa kakma ya da daha çoğunu bekleyerek verme
  من يمن منا، إذا صنع صنعا جميلا (maqayis)؛ من عليه منا: أنعم؛ المنان؛ من عليه منة، أي امتن عليه؛ المنة تهدم الصنيعة؛ كثير الامتنان (sihah)؛ المنة: النعمة الثقيلة؛ من فلان على فلان: إذا أثقله بالنعمة؛ المنة منهم بالقول، ومنة الله عليهم بالفعل (mufradat)
- **B004** tutsağı karşılıksız serbest bırakma [kalıp] — sonrasında tutsağı karşılıksız serbest bırakma
  فإما منا بعد وإما فداء؛ فالمن إشارة إلى الإطلاق بلا عوض (mufradat)
- **B005** eski ağırlık ölçüsü ve ölçülüp tartılmış olma — ağırlık ölçüsü veya tartılmış miktar · iki alt ağırlık birimine eşit ölçü · miktarı belirlenmiş veya tartılmış
  المن: المنا، وهو رطلان، والجمع أمنان، وجمع المنا أمناء (sihah)؛ المن: ما يوزن به؛ من، ومنان، وأمنان؛ ويقال لما يقدر: ممنون كما يقال: موزون (mufradat)
- **B006** ağaçlara çiy gibi düşen tatlı madde ve bağışlanan azık — ağaçlara çiy gibi düşen tatlı doğal madde · tatlı yiyecekle bıldırcından oluşan bağışlanmış azık
  المن: شيء حلو كالطرنجبين؛ الكمأة من المن (sihah)؛ المن شيء كالطل فيه حلاوة يسقط على الشجر؛ المن والسلوى... ما أنعم الله به عليهم (mufradat)



===== _commentary/v16/work/s084/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s084/reader_a_pilot.md)

# S084 Semantic Channel Discovery

## Parent Channels

### 1. Sky, Night, and Cyclical Time
- Semantic invariant: The world is ordered through enclosure, layering, gathering, illumination, and recurring intervals.
- Surface relation: direct; the sky splits (84:1), twilight recedes (84:16), night gathers (84:17), the moon fills (84:18), and one layer succeeds another (84:19).
- Surprising reach: Cloud masses, a hidden moon, a stellar marker, insomnia, late supper, and unattended animals all extend the same temporal enclosure.

#### Subchannel A. Sky Canopy and Exposed Overhead
- Reading type: mixed
- Scene or process: An upper expanse arches over an outspread lower surface, while exposed things remain uncovered beneath it.
- Active motifs: sky `س م و:B004/m01`; earth `ء ر ض:B001/m01`; exposure to the open sky `ع ذ ب:B004/m01`; outer surface `ظ ه ر:B003/m01`
- Ayah anchors: `س م و` (84:1); `ء ر ض` (84:3); `ع ذ ب` (84:24); `ظ ه ر` (84:10)
- Synthesis: The opening sky and stretched earth form a vertical enclosure whose latent counterpart is the condition of standing openly beneath an uncovered surface.

#### Subchannel B. Cloud Gathering and Atmospheric Layers
- Reading type: latent/lexical
- Scene or process: Clouds accumulate, ride over one another, and become a covering made of stacked strata.
- Active motifs: cloud mass `ر ب ب:B008/m01`; stacking `ر ك ب:B002/m01`; superposed layers `ط ب ق:B002/m01`; covering `ك ف ر:B001/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ر ك ب` (84:19); `ط ب ق` (84:19); `ك ف ر` (84:22)
- Synthesis: Atmospheric accumulation concretizes the surah's movement through successive layers as a gathered, covering mass.

#### Subchannel C. Twilight and Enclosing Night
- Reading type: surface-primary
- Scene or process: Fading light gives way to darkness that covers and gathers what moves within it.
- Active motifs: twilight `ش ف ق:B002/m01`; night `ل ي ل:B001/m01`; dark covering `ك ف ر:B002/m01`; gathered load `و س ق:B002/m01`
- Ayah anchors: `ش ف ق` (84:16); `ل ي ل` (84:17); `ك ف ر` (84:22); `و س ق` (84:17, 84:18)
- Synthesis: Twilight marks the threshold, while night performs the enclosing and gathering action stated on the surface.

#### Subchannel D. Moon, Hidden Crescent, and Stellar Marker
- Reading type: mixed
- Scene or process: A celestial body passes from concealment to fullness while nearby stellar signs mark the nocturnal field.
- Active motifs: moon `ق م ر:B001/m01`; hidden moon `س ر ر:B004/m01`; star `ق ل ب:B010/m01`; fullness and alignment `و س ق:B004/m01`
- Ayah anchors: `ق م ر` (84:18); `س ر ر` (84:9, 84:13); `ق ل ب` (84:9); `و س ق` (84:17, 84:18)
- Synthesis: The full moon is one phase in a larger visibility cycle that includes concealment, stellar orientation, and completed alignment.

#### Subchannel E. Calendar, Cycle, and Measured Interval
- Reading type: latent/lexical
- Scene or process: Recurring celestial and bodily periods define bounded portions of time and transitions between them.
- Active motifs: recurring period `ق ر ء:B002/m01`; portion of an hour `ط ب ق:B010/m01`; evening interval `ل ي ل:B003/m01`; extended duration `م د د:B004/m01`; elapsed time `خ ل و:B003/m01`
- Ayah anchors: `ق ر ء` (84:21); `ط ب ق` (84:19); `ل ي ل` (84:17); `م د د` (84:3); `خ ل و` (84:4)
- Synthesis: The visible succession of night and moon opens onto a lexical network of cycles, elapsed spans, and measured time portions.

#### Subchannel F. Night Practice, Wakefulness, and Delayed Rest
- Reading type: latent/lexical
- Scene or process: Night becomes a behavioral interval for sustained activity, wakefulness, delayed eating, or neglected supervision.
- Active motifs: nocturnal practice `ل ي ل:B002/m01`; insomnia `ق م ر:B009/m01`; late supper `ق م ر:B010/m01`; unattended herd at night `ق م ر:B011/m01`
- Ayah anchors: `ل ي ل` (84:17); `ق م ر` (84:18)
- Synthesis: The temporal field is not merely astronomical; it governs human routines and the risks of wakefulness or unattended livestock.

### 2. Terrain, Water, and Cultivation
- Semantic invariant: Land receives, channels, stores, and yields material life through soil, water, plants, and changing terrain.
- Surface relation: direct; the earth is spread and empties what it contains (84:3-4), while latent branches specify fertile soil, irrigation, floodwater, crops, and landforms.
- Surprising reach: Canal banks, wells, truffles, frost-damaged dates, camphor, aloes, sand clefts, and bee habitat emerge from the terrestrial field.

#### Subchannel A. Fertile Ground and Plant Establishment
- Reading type: latent/lexical
- Scene or process: Prepared soil becomes fit for growth, receives seed, and supports rooted vegetation.
- Active motifs: fertile land `ء ر ض:B002/m01`; fitness for good growth `ء ر ض:B003/m01`; cultivated plant `ر ب ب:B012/m01`; seed-covering farmer `ك ف ر:B008/m01`; plant species `ص ل ي:B010/m01`
- Ayah anchors: `ء ر ض` (84:3); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ك ف ر` (84:22); `ص ل ي` (84:12)
- Synthesis: The stretched earth becomes an agrarian receiving surface whose value lies in fitness, covering seed, and sustaining growth.

#### Subchannel B. Depressions, Wells, and Unstable Ground
- Reading type: latent/lexical
- Scene or process: Ground opens into pits or wells and can shift through tremor or subsidence.
- Active motifs: pit or soft depression `ث ب ر:B001/m01`; well `ق ل ب:B007/m01`; ground tremor `ء ر ض:B008/m01`; opening and ebb `ث ب ر:B006/m01`
- Ayah anchors: `ث ب ر` (84:11); `ق ل ب` (84:9); `ء ر ض` (84:3)
- Synthesis: Emptying and spreading land has a complementary recessed form in pits, wells, openings, and unstable earth.

#### Subchannel C. Irrigation Channels and Raised Field Edges
- Reading type: latent/lexical
- Scene or process: Water is directed through canals bordered by raised ridges into productive ground.
- Active motifs: canal `ء ت ي:B004/m01`; canal bank or raised field `ر ك ب:B009/m01`; flowing water extension `م د د:B003/m01`; abundant water source `ع ل م:B005/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ر ك ب` (84:19); `م د د` (84:3); `ع ل م` (84:23)
- Synthesis: The land's extension is operationalized as an irrigation system whose channels, banks, and water supply regulate yield.

#### Subchannel D. Flood, Stored Water, and Sweet Supply
- Reading type: latent/lexical
- Scene or process: Water arrives in force, gathers in quantity, and becomes a drinkable or sustaining reserve.
- Active motifs: imported floodwater `ء ت ي:B005/m01`; water supply `ر ب ب:B013/m01`; sweet water `ع ذ ب:B001/m01`; abundance `ق م ر:B008/m01`; extended water `م د د:B003/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ع ذ ب` (84:24); `ق م ر` (84:18); `م د د` (84:3)
- Synthesis: Arrival, extension, and abundance converge on water as both overwhelming influx and sustaining provision.

#### Subchannel E. Palm Growth, Fruit Core, and Crop Yield
- Reading type: latent/lexical
- Scene or process: A palm produces offshoots and fruit whose core, husk, first signs, and final yield form a cultivation sequence.
- Active motifs: agricultural yield `ء ت ي:B007/m01`; palm core `ق ل ب:B003/m01`; palm offshoot `ر ك ب:B007/m01`; husk `ك ف ر:B010/m01`; first fruit signs `ب ش ر:B007/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ق ل ب` (84:9); `ر ك ب` (84:19); `ك ف ر` (84:22); `ب ش ر` (84:24)
- Synthesis: The same root network that presents arrival and covering also describes the staged emergence, protection, and harvest of palm produce.

#### Subchannel F. Frost Damage and Spoiled Dates
- Reading type: latent/lexical
- Scene or process: Exposure to cold or moonlit conditions damages dates and their containers, interrupting ripening and storage.
- Active motifs: frost-spoiled dates `ق م ر:B004/m01`; moon-damaged waterskin `ق م ر:B006/m01`; reddening fruit `ق ل ب:B015/m01`; direct exposure `ب ش ر:B003/m01`
- Ayah anchors: `ق م ر` (84:18); `ق ل ب` (84:9); `ب ش ر` (84:24)
- Synthesis: Lunar visibility has an agrarian underside in vulnerable fruit and storage materials altered by nocturnal exposure.

#### Subchannel G. Sand Clefts, Mounds, and Sediment
- Reading type: latent/lexical
- Scene or process: Loose terrain divides into sandy clefts, accumulates in mounds, and records deposited traces.
- Active motifs: sandy cleft `ش ق ق:B007/m01`; sand mound `س ر ر:B015/m01`; deposited blood-like trace `ب ص ر:B004/m01`; receding opening `ث ب ر:B006/m01`
- Ayah anchors: `ش ق ق` (84:1); `س ر ر` (84:9, 84:13); `ب ص ر` (84:15); `ث ب ر` (84:11)
- Synthesis: Splitting, concealment, and trace-bearing surfaces describe a terrain shaped by separation and deposition.

#### Subchannel H. Wild Growth, Truffle, and Aromatic Plants
- Reading type: latent/lexical
- Scene or process: Uncultivated or specialty growth yields edible crusts and aromatic woods or plants.
- Active motifs: truffle crust `س ر ر:B013/m01`; camphor `ك ف ر:B011/m01`; aloes plant `ء ل ي:B005/m01`; cultivated plant `ر ب ب:B012/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ك ف ر` (84:22); `ء ل ي` (84:6, 84:9); `ر ب ب` (84:2, 84:5, 84:6, 84:15)
- Synthesis: The terrestrial inventory extends beyond staple crops to concealed edible growth and valued aromatic vegetation.

#### Subchannel I. Hive, Colony, and Productive Habitat
- Reading type: latent/lexical
- Scene or process: A hollow dwelling supports an organized colony whose members work within a bounded habitat.
- Active motifs: hive `خ ل و:B012/m01`; plant support `ر ب ب:B012/m01`; work crew `ع م ل:B006/m01`; inhabited place `ك و ن:B002/m01`
- Ayah anchors: `خ ل و` (84:4); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ع م ل` (84:25); `ك و ن` (84:13, 84:15)
- Synthesis: Emptiness becomes productive enclosure when a hollow is inhabited by a coordinated working colony.

#### Subchannel J. Mown Grass and Herd Fodder
- Reading type: latent/lexical
- Scene or process: Grass is cut, gathered, and reserved to feed managed livestock.
- Active motifs: cut grass `خ ل و:B013/m01`; cutting fragment `ش ق ق:B006/m01`; herd `ر ب ب:B014/m01`; gathered livestock `و س ق:B005/m01`
- Ayah anchors: `خ ل و` (84:4); `ش ق ق` (84:1); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و س ق` (84:17, 84:18)
- Synthesis: Cultivated terrain supports husbandry through the intermediate process of cutting and storing fodder.

### 3. Perception, Knowledge, and Disclosure
- Semantic invariant: Sensory reception becomes inward retention, analysis, certainty, doubt, concealment, or discovery.
- Surface relation: direct; the surah names perception, knowledge, inward retention, supposition, and divine seeing at 84:6, 84:14-15, and 84:23.
- Surprising reach: Eye anatomy, lowered gaze, memorization, expert diagnosis, accusation, and deliberate reversal inhabit one epistemic field.

#### Subchannel A. Sight and Insight
- Reading type: mixed
- Scene or process: The eye receives a visible scene and converts it into discerning awareness.
- Active motifs: eyesight `ب ص ر:B001/m01`; insight `ب ص ر:B002/m01`; knowledge `ع ل م:B001/m01`; visible manifestation `ظ ه ر:B001/m01`
- Ayah anchors: `ب ص ر` (84:15); `ع ل م` (84:23); `ظ ه ر` (84:10)
- Synthesis: Surface seeing is linked to the epistemic movement from outward appearance to inward comprehension.

#### Subchannel B. Pupil, Sclera, and Directed Gaze
- Reading type: latent/lexical
- Scene or process: Contrasting eye structures focus vision while posture can lower or impair the gaze.
- Active motifs: pupil `ء ن س:B005/m01`; contrasting eye white and dark `ح و ر:B001/m01`; lowered gaze `س ج د:B005/m01`; snow blindness `ق م ر:B005/m01`
- Ayah anchors: `ء ن س` (84:6); `ح و ر` (84:14); `س ج د` (84:21); `ق م ر` (84:18)
- Synthesis: Visual perception is grounded in a precise bodily apparatus vulnerable to both disciplined lowering and environmental impairment.

#### Subchannel C. Hearing, Acceptance, and Receptive Attention
- Reading type: latent/lexical
- Scene or process: A message enters through hearing, is noticed, and is either accepted or met with withdrawal.
- Active motifs: hearing and acceptance `ء ذ ن:B002/m01`; perception and noticing `ء ن س:B002/m01`; unprotected exposure `خ ل و:B016/m01`; lowered attention `س ج د:B005/m01`
- Ayah anchors: `ء ذ ن` (84:2, 84:5); `ء ن س` (84:6); `خ ل و` (84:4); `س ج د` (84:21)
- Synthesis: The sky and earth's obedience to hearing contrasts with human vulnerability and the possibility of withholding receptive attention.

#### Subchannel D. Heart, Memory, and Internal Storage
- Reading type: mixed
- Scene or process: Experience is gathered into an inward container where words and events are retained.
- Active motifs: heart `ق ل ب:B001/m01`; internal memory `و ع ي:B001/m01`; memorization `ظ ه ر:B019/m01`; studied recitation `ق ر ء:B001/m02`
- Ayah anchors: `ق ل ب` (84:9); `و ع ي` (84:23); `ظ ه ر` (84:10); `ق ر ء` (84:21)
- Synthesis: The surah's language of inward awareness expands into a model of the heart as a vessel for memorized recitation and experience.

#### Subchannel E. Deliberation, Turning, and Analysis
- Reading type: latent/lexical
- Scene or process: A matter is turned over, divided, and examined before a deliberate course is chosen.
- Active motifs: turning and analysis `ق ل ب:B004/m01`; deliberate action `ظ ه ر:B018/m01`; deliberative division `ق س م:B006/m01`; critical alteration `ك د ح:B003/m01`
- Ayah anchors: `ق ل ب` (84:9); `ظ ه ر` (84:10); `ق س م` (84:16); `ك د ح` (84:6)
- Synthesis: Physical turning and division become a cognitive procedure for testing alternatives and exposing defects.

#### Subchannel F. Certainty, Truth, and Verification
- Reading type: mixed
- Scene or process: A proposition is established as real through knowledge, verification, and settled conviction.
- Active motifs: truth and reality `ح ق ق:B001/m01`; establishing truth `ح ق ق:B005/m01`; certainty `ظ ن ن:B001/m01`; knowledge `ع ل م:B001/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ظ ن ن` (84:14); `ع ل م` (84:23)
- Synthesis: The surah's fulfilled obedience and divine knowledge support a latent chain from supposition to verified reality.

#### Subchannel G. Probability, Doubt, and Uncertain Outcome
- Reading type: mixed
- Scene or process: A person estimates an outcome without full security, moving among likelihood, doubt, and unreliable expectation.
- Active motifs: probability `ح س ب:B002/m01`; doubt `ظ ن ن:B003/m01`; unreliable outcome `ظ ن ن:B006/m01`; safety and reliability `ء م ن:B001/m01`
- Ayah anchors: `ح س ب` (84:8); `ظ ن ن` (84:14); `ء م ن` (84:20, 84:25)
- Synthesis: Reckoning can remain speculative until tested against the security of a reliable conclusion.

#### Subchannel H. Accusation, Mistrust, and Disproof
- Reading type: latent/lexical
- Scene or process: Suspicion hardens into accusation, while counterevidence challenges a disputed claim.
- Active motifs: accusation `ظ ن ن:B004/m01`; mistrust `ظ ن ن:B005/m01`; attribution of falsehood `ك ذ ب:B002/m01`; disputed truth `ح ق ق:B004/m01`
- Ayah anchors: `ظ ن ن` (84:14); `ك ذ ب` (84:22); `ح ق ق` (84:2, 84:5)
- Synthesis: Epistemic uncertainty becomes socially consequential when it produces mistrust, accusation, and adversarial verification.

#### Subchannel I. Concealment, Discovery, and Manifestation
- Reading type: mixed
- Scene or process: A hidden matter is retained out of view, then uncovered and made visible.
- Active motifs: secret `س ر ر:B001/m01`; concealment `و ر ي:B005/m01`; discovery `ظ ه ر:B008/m01`; visible manifestation `ظ ه ر:B001/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `و ر ي` (84:10); `ظ ه ر` (84:10)
- Synthesis: What is inwardly concealed remains part of a disclosure process culminating in visible appearance or discovery.

#### Subchannel J. Expertise and Penetrating Discernment
- Reading type: latent/lexical
- Scene or process: An expert reads beneath the surface and reaches the operative core of a difficult matter.
- Active motifs: expert knower `س ر ر:B014/m01`; scholar `ر ب ب:B003/m01`; effective penetration `ء ت ي:B013/m01`; insight `ب ص ر:B002/m01`; inner essence `ق ل ب:B002/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ء ت ي` (84:7, 84:10); `ب ص ر` (84:15); `ق ل ب` (84:9)
- Synthesis: Deep understanding is figured as movement through an outer layer into an essence accessible to trained discernment.

### 4. Speech, Signs, and Textual Transmission
- Semantic invariant: Meaning is announced, exchanged, inscribed, named, patterned, and carried through audible or visible signs.
- Surface relation: direct; calling, recitation, denial, knowledge, and retained content appear at 84:11 and 84:21-23.
- Surprising reach: Formulaic greetings, banners, ink, grammar particles, poetic models, clamorous noise, and bird calls occupy the same transmission field.

#### Subchannel A. Call, Announcement, and Proclamation
- Reading type: mixed
- Scene or process: A speaker projects a summons or public announcement toward an audience.
- Active motifs: call `د ع و:B001/m01`; proclamation `ء ذ ن:B003/m01`; sign or banner `ع ل م:B002/m01`; naming aloud `س م و:B005/m01`
- Ayah anchors: `د ع و` (84:11); `ء ذ ن` (84:2, 84:5); `ع ل م` (84:23); `س م و` (84:1)
- Synthesis: The desperate call on the surface belongs to a broader communicative spectrum from private invocation to formal proclamation.

#### Subchannel B. Dialogue, Reply, and Precise Discourse
- Reading type: latent/lexical
- Scene or process: Interlocutors exchange turns and refine a claim through exact verbal formulation.
- Active motifs: dialogue `ح و ر:B006/m01`; learned words `ل ق ي:B011/m01`; precise discourse `ح ق ق:B010/m02`; articulated speech `ب ل ل:B006/m01`
- Ayah anchors: `ح و ر` (84:14); `ل ق ي` (84:4, 84:6); `ح ق ق` (84:2, 84:5); `ب ل ل` (84:22)
- Synthesis: Returning speech becomes a disciplined exchange in which wording, articulation, and truth conditions are jointly negotiated.

#### Subchannel C. Greeting, Tidings, and Responsive Formula
- Reading type: latent/lexical
- Scene or process: A conventional utterance opens contact and delivers news that changes the recipient's state.
- Active motifs: formulaic greeting `ق ر ء:B006/m01`; glad tidings `ب ش ر:B005/m01`; joy `س ر ر:B010/m01`; affirmative response `ب ل ي:B010/m01`
- Ayah anchors: `ق ر ء` (84:21); `ب ش ر` (84:24); `س ر ر` (84:9, 84:13); `ب ل ي` (84:15)
- Synthesis: Greeting, announcement, emotional reception, and reply form a complete interpersonal transmission scene.

#### Subchannel D. Recitation, Study, and Learned Wording
- Reading type: surface-primary
- Scene or process: A text is gathered into ordered wording, read aloud, studied, and transmitted to a learner.
- Active motifs: reading `ق ر ء:B001/m01`; gathered wording and study `ق ر ء:B001/m02`; learned words `ل ق ي:B011/m01`; knowledge `ع ل م:B001/m01`
- Ayah anchors: `ق ر ء` (84:21); `ل ق ي` (84:4, 84:6); `ع ل م` (84:23)
- Synthesis: Recitation is simultaneously vocal performance, textual gathering, study, and the reception of learned language.

#### Subchannel E. Writing, Joining, and Ink
- Reading type: latent/lexical
- Scene or process: Separate marks or materials are joined into durable writing through inscription and ink.
- Active motifs: writing `ك ت ب:B002/m01`; joined construction `ك ت ب:B001/m01`; ink `م د د:B005/m01`; retained content `و ع ي:B001/m01`
- Ayah anchors: `ك ت ب` (84:7, 84:10); `م د د` (84:3); `و ع ي` (84:23)
- Synthesis: The written record arises from joining marks with ink and preserving the resulting content for later retrieval.

#### Subchannel F. Naming, Appellation, and Reputation
- Reading type: latent/lexical
- Scene or process: A name identifies a person or place and can expand into a publicly circulating reputation.
- Active motifs: naming `س م و:B005/m01`; reputation `س م و:B008/m01`; good name `ص ل ح:B004/m01`; proper name or place-name `ي س ر:B010/m01`
- Ayah anchors: `س م و` (84:1); `ص ل ح` (84:25); `ي س ر` (84:8)
- Synthesis: Naming begins as reference but becomes a social sign whose value is measured through reputation.

#### Subchannel G. Banner, Mark, and Trace
- Reading type: latent/lexical
- Scene or process: A visible mark identifies allegiance, location, condition, or a past contact event.
- Active motifs: banner or sign `ع ل م:B002/m01`; trace `ب ص ر:B004/m01`; scratch or defacement `ك د ح:B002/m01`; distinguishing facet `ش ف ق:B005/m01`
- Ayah anchors: `ع ل م` (84:23); `ب ص ر` (84:15); `ك د ح` (84:6); `ش ف ق` (84:16)
- Synthesis: Meaning can be carried without speech through banners, surface traces, deliberate marks, and differentiating visual facets.

#### Subchannel H. Contrast, Exception, and Affirmation
- Reading type: latent/lexical
- Scene or process: Small grammatical operators redirect an utterance by contrast, exclusion, endpoint, or emphatic confirmation.
- Active motifs: contrast particle `ب ل ل:B008/m01`; affirmative reply `ب ل ي:B010/m01`; endpoint preposition `ء ل ي:B001/m01`; exception `غ ي ر:B005/m01`; exception from a set `خ ل و:B004/m01`
- Ayah anchors: `ب ل ل` (84:22); `ب ل ي` (84:15); `ء ل ي` (84:6, 84:9); `غ ي ر` (84:25); `خ ل و` (84:4)
- Synthesis: Lexical particles organize reasoning by setting boundaries, reversing expectations, and affirming what a prior statement leaves open.

#### Subchannel I. Number, Pronoun, and Collective Expression
- Reading type: latent/lexical
- Scene or process: Grammatical form shifts reference between singular, plural, accompaniment, and collected wording.
- Active motifs: plural or pronominal form `ء ل ي:B004/m01`; scattering into plurality `ب ل ي:B008/m01`; gathered wording `ق ر ء:B001/m02`; accompaniment `ء ل ي:B003/m01`
- Ayah anchors: `ء ل ي` (84:6, 84:9); `ب ل ي` (84:15); `ق ر ء` (84:21)
- Synthesis: The same lexical field that marks direction also regulates how participants and words are grouped in discourse.

#### Subchannel J. Method, Path, and Poetic Model
- Reading type: latent/lexical
- Scene or process: A speaker or worker follows an established formal pattern, method, or compositional route.
- Active motifs: poetic model `ق ر ء:B005/m01`; method or path `ق ر ء:B011/m01`; work method `ع م ل:B011/m01`; route or junction `ء ت ي:B010/m01`
- Ayah anchors: `ق ر ء` (84:21); `ع م ل` (84:25); `ء ت ي` (84:7, 84:10)
- Synthesis: Textual composition and practical action share the idea of moving through a recognized patterned course.

#### Subchannel K. Alarm, Clamor, and Bird Call
- Reading type: latent/lexical
- Scene or process: Non-discursive sound attracts attention through noise, alarm, or repeated animal vocalization.
- Active motifs: noise `و ع ي:B005/m01`; clamor `ب ل ل:B009/m01`; bird call `ب ل ل:B010/m01`; dove `ق م ر:B012/m01`; orator's projected voice `ش ق ق:B008/m02`
- Ayah anchors: `و ع ي` (84:23); `ب ل ل` (84:22); `ق م ر` (84:18); `ش ق ق` (84:1)
- Synthesis: Communication extends below propositional speech to attention-getting sound, resonant voice, and recognizable animal calls.

### 5. Worship, Faith, and Ritual Submission
- Semantic invariant: A worshipper recognizes sovereignty, adopts belief, performs embodied submission, invokes aid, and negotiates rejection or release.
- Surface relation: direct; lordship, prostration, belief, disbelief, recitation, and recompense structure 84:6, 84:15, and 84:20-25.
- Surprising reach: Sanctuary space, intercession, liturgical affirmation, expiation, and manumission-like release elaborate the ritual field.

#### Subchannel A. Deity, Lordship, and Devotion
- Reading type: surface-primary
- Scene or process: A human subject recognizes divine dominion and directs devotion toward the sovereign source.
- Active motifs: deity and worship `ء ل ه:B001/m01`; lordship and dominion `ر ب ب:B001/m01`; devoted reciter `ق ر ء:B001/m02`; faith `ء م ن:B002/m01`
- Ayah anchors: `ء ل ه` (84:23); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ق ر ء` (84:21); `ء م ن` (84:20, 84:25)
- Synthesis: Divine lordship supplies the relational center from which recitation, belief, and worship take their direction.

#### Subchannel B. Sanctuary and Consecrated Place
- Reading type: latent/lexical
- Scene or process: A bounded place is set apart for worship, prostration, and communal approach.
- Active motifs: sanctuary `س ج د:B002/m01`; place of prayer `ص ل ي:B008/m01`; sanctuary or sacred toponym `ص ل ح:B005/m01`; inhabited sacred place `ء ه ل:B004/m01`
- Ayah anchors: `س ج د` (84:21); `ص ل ي` (84:12); `ص ل ح` (84:25); `ء ه ل` (84:9, 84:13)
- Synthesis: Ritual action generates a spatial counterpart in the sanctuary as an inhabited and morally ordered place.

#### Subchannel C. Prostration, Bowing, and Bodily Submission
- Reading type: surface-primary
- Scene or process: The body lowers itself in a visible act of worship and compliant posture.
- Active motifs: prostration `س ج د:B001/m01`; bowing `س ج د:B004/m01`; prayer `ص ل ي:B001/m01`; submission `ك و ن:B004/m01`
- Ayah anchors: `س ج د` (84:21); `ص ل ي` (84:12); `ك و ن` (84:13, 84:15)
- Synthesis: The refused prostration on the surface is clarified by a cluster of lowering, prayer, and willing submission.

#### Subchannel D. Supplication, Blessing, and Intercession
- Reading type: mixed
- Scene or process: A worshipper calls toward a higher authority and seeks blessing, mediation, or a favorable response.
- Active motifs: invocation `د ع و:B001/m01`; blessing and intercession `ص ل ي:B002/m01`; liturgical affirmation `ء م ن:B003/m01`; divine invocation `ء ل ه:B002/m01`
- Ayah anchors: `د ع و` (84:11); `ص ل ي` (84:12); `ء م ن` (84:20, 84:25); `ء ل ه` (84:23)
- Synthesis: The act of calling can move from a cry of ruin to prayerful invocation, blessing, and communal affirmation.

#### Subchannel E. Faith, Conviction, and Testimony
- Reading type: surface-primary
- Scene or process: Inward conviction is publicly or verbally ratified as reliable testimony.
- Active motifs: faith `ء م ن:B002/m01`; testimony and affirmation `ء م ن:B003/m01`; established truth `ح ق ق:B005/m01`; insight `ب ص ر:B002/m01`
- Ayah anchors: `ء م ن` (84:20, 84:25); `ح ق ق` (84:2, 84:5); `ب ص ر` (84:15)
- Synthesis: Belief is presented as both inward recognition and an assent grounded in perceived and established truth.

#### Subchannel F. Disbelief, Denial, and Rejection
- Reading type: surface-primary
- Scene or process: A hearer covers over or rejects a received truth and attributes falsehood to it.
- Active motifs: disbelief `ك ف ر:B003/m01`; false denial `ك ذ ب:B001/m01`; attribution of falsehood `ك ذ ب:B002/m01`; turning away `ظ ه ر:B022/m01`
- Ayah anchors: `ك ف ر` (84:22); `ك ذ ب` (84:22); `ظ ه ر` (84:10)
- Synthesis: Denial combines cognitive rejection, false attribution, and bodily or social withdrawal from the message.

#### Subchannel G. Expiation, Disavowal, and Release
- Reading type: latent/lexical
- Scene or process: A burdened subject is cleared through expiation, formal disavowal, or release from restraint.
- Active motifs: expiation `ك ف ر:B009/m01`; disavowal `ك ف ر:B005/m01`; absolution `خ ل و:B006/m01`; release `م ن ن:B004/m01`
- Ayah anchors: `ك ف ر` (84:22); `خ ل و` (84:4); `م ن ن` (84:25)
- Synthesis: Covering can function not only as denial but as a compensatory act that removes liability and restores freedom.

### 6. Law, Authority, and Institutional Status
- Semantic invariant: Social order assigns duties, verifies claims, authorizes action, records status, distributes liability, and binds parties under sovereign power.
- Surface relation: direct; records, reckoning, fulfilled obligation, and divine authority appear directly at 84:2, 84:5, 84:7-10, and 84:15, while the legal and administrative procedures are lexical extensions.
- Surprising reach: Taxation, manumission contracts, blood money, coronation, truce, surety, and protected charges form a detailed institutional network.

#### Subchannel A. Duty, Decree, and Binding Obligation
- Reading type: mixed
- Scene or process: An authoritative determination imposes a duty that becomes due and must be fulfilled.
- Active motifs: binding duty `ح ق ق:B002/m01`; decree `ك ت ب:B003/m01`; obligatory exhortation `ك ذ ب:B003/m01`; formal reckoning `ح س ب:B001/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ك ت ب` (84:7, 84:10); `ك ذ ب` (84:22); `ح س ب` (84:8)
- Synthesis: The surah's language of due fulfillment and written records expands into a complete scene of authoritative obligation and accounting.

#### Subchannel B. Right, Claim, and Adversarial Dispute
- Reading type: latent/lexical
- Scene or process: A claimant asserts entitlement, another party contests it, and the dispute requires adjudication.
- Active motifs: legal right `ح ق ق:B003/m01`; dispute `ح ق ق:B004/m01`; claim and asserted lineage `د ع و:B002/m01`; argumentative dialogue `ح و ر:B006/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `د ع و` (84:11); `ح و ر` (84:14)
- Synthesis: Truth becomes institutional when it is framed as an enforceable right advanced and contested through claims.

#### Subchannel C. Permission, Access, and Licensed Action
- Reading type: mixed
- Scene or process: An authority hears a request, grants entry or action, and opens an otherwise restricted avenue.
- Active motifs: permission `ء ذ ن:B004/m01`; hearing and acceptance `ء ذ ن:B002/m01`; release into access `خ ل و:B008/m01`; available avenue `ء ت ي:B003/m01`
- Ayah anchors: `ء ذ ن` (84:2, 84:5); `خ ل و` (84:4); `ء ت ي` (84:7, 84:10)
- Synthesis: The direct obedience of sky and earth to authorization supports a latent procedural scene of accepted request and opened access.

#### Subchannel D. Surety, Adequacy, and Guaranteed Performance
- Reading type: latent/lexical
- Scene or process: A guarantor or sufficient reserve secures performance when an outcome cannot rest on trust alone.
- Active motifs: adequacy and surety `ح س ب:B003/m01`; guarantor `ك و ن:B003/m01`; attribution of reliability or unreliability `ك ف ر:B006/m01`; protected charge `ح ق ق:B007/m01`
- Ayah anchors: `ح س ب` (84:8); `ك و ن` (84:13, 84:15); `ك ف ر` (84:22); `ح ق ق` (84:2, 84:5)
- Synthesis: Reckoning includes the institutional question of whether a person, reserve, or guarantee is sufficient to cover an obligation.

#### Subchannel E. Liability, Absolution, and Formal Discharge
- Reading type: latent/lexical
- Scene or process: Responsibility is assigned, denied, or removed through a recognized act of discharge.
- Active motifs: disavowal `ك ف ر:B005/m01`; freedom from blame `خ ل و:B005/m01`; absolution `خ ل و:B006/m01`; removal of shame or liability `ظ ه ر:B013/m01`; release `م ن ن:B004/m01`
- Ayah anchors: `ك ف ر` (84:22); `خ ل و` (84:4); `ظ ه ر` (84:10); `م ن ن` (84:25)
- Synthesis: Institutional status changes when liability is explicitly severed and the subject emerges cleared of blame.

#### Subchannel F. Administration, Audit, and Official Office
- Reading type: mixed
- Scene or process: An office gathers records, examines conduct, and renders an account under delegated authority.
- Active motifs: administration `ح س ب:B006/m01`; inquiry and testing `ح س ب:B010/m01`; official office `ع م ل:B003/m01`; discovery through inspection `ظ ه ر:B008/m01`
- Ayah anchors: `ح س ب` (84:8); `ع م ل` (84:25); `ظ ه ر` (84:10)
- Synthesis: The easy or difficult reckoning on the surface unfolds into an administrative process of record collection, inspection, and judgment.

#### Subchannel G. Enrollment, Registration, and Named Status
- Reading type: latent/lexical
- Scene or process: A person is entered into an official register under a stable name and attested status.
- Active motifs: enrollment `ك ت ب:B004/m01`; naming `س م و:B005/m01`; testimony `ء م ن:B003/m01`; written record `ك ت ب:B002/m01`
- Ayah anchors: `ك ت ب` (84:7, 84:10); `س م و` (84:1); `ء م ن` (84:20, 84:25)
- Synthesis: The received book has an institutional analogue in registration, where writing, naming, and attestation establish public standing.

#### Subchannel H. Contracted Manumission and Release
- Reading type: latent/lexical
- Scene or process: A dependent person enters a written arrangement whose installments culminate in freedom.
- Active motifs: manumission contract `ك ت ب:B005/m01`; wage or payment `ع م ل:B004/m01`; release `م ن ن:B004/m01`; licensed departure `خ ل و:B008/m01`
- Ayah anchors: `ك ت ب` (84:7, 84:10); `ع م ل` (84:25); `م ن ن` (84:25); `خ ل و` (84:4)
- Synthesis: Writing, payment, and release align as sequential roles in a formal transition from dependency to liberty.

#### Subchannel I. Tax, Levy, and Assessed Share
- Reading type: latent/lexical
- Scene or process: Authority assesses a compulsory contribution and divides the burden among liable parties.
- Active motifs: tax or levy `ء ت ي:B008/m01`; allotment `ق س م:B003/m01`; administrative calculation `ح س ب:B006/m01`; dominion `ر ب ب:B001/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ق س م` (84:16); `ح س ب` (84:8); `ر ب ب` (84:2, 84:5, 84:6, 84:15)
- Synthesis: The root of coming or rendering develops an institutional sense in which assessed value is brought to a ruling authority.

#### Subchannel J. Covenant, Truce, and Restitution
- Reading type: latent/lexical
- Scene or process: Opposed parties bind themselves by covenant, suspend conflict, and compensate prior injury.
- Active motifs: covenant `ر ب ب:B011/m01`; truce `ق س م:B008/m01`; peace and reconciliation `ص ل ح:B002/m01`; blood money or restitution `غ ي ر:B002/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ق س م` (84:16); `ص ل ح` (84:25); `غ ي ر` (84:25)
- Synthesis: Binding agreement, cessation of hostility, restored relations, and compensatory payment form one legal peace process.

#### Subchannel K. Oath, Vow, and Sworn Commitment
- Reading type: mixed
- Scene or process: A speaker binds future conduct or testimony through a solemn verbal act.
- Active motifs: oath `ق س م:B004/m01`; sworn vow `ء ل ي:B007/m01`; oath formula `ب ل ي:B005/m01`; right-hand oath `ي م ن:B003/m01`
- Ayah anchors: `ق س م` (84:16); `ء ل ي` (84:6, 84:9); `ب ل ي` (84:15); `ي م ن` (84:7)
- Synthesis: The surface oath expands into a juridical act linking utterance, bodily side, commitment, and accountability.

#### Subchannel L. Dominion, Crown, and Investiture
- Reading type: latent/lexical
- Scene or process: Sovereign power is made visible through rule, divine invocation, and ceremonial investiture.
- Active motifs: dominion `ر ب ب:B001/m01`; divine name and sovereignty `ء ل ه:B002/m01`; crown `ك ف ر:B015/m01`; public elevation `س م و:B002/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ء ل ه` (84:23); `ك ف ر` (84:22); `س م و` (84:1)
- Synthesis: Abstract lordship takes an embodied political form in elevation and the placing of a crown.

#### Subchannel M. Protected Charge and Security Precaution
- Reading type: latent/lexical
- Scene or process: A vulnerable person or entrusted matter is bound into protective custody before danger arrives.
- Active motifs: protected charge `ح ق ق:B007/m01`; precaution `ظ ه ر:B021/m01`; securing knot `ر ب ب:B016/m02`; prior detention `ء ل ي:B013/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ظ ه ر` (84:10); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ء ل ي` (84:6, 84:9)
- Synthesis: Legal care and physical preparation converge on securing a charge in advance of foreseeable risk.

### 7. Work, Exchange, and Provision
- Semantic invariant: Effort transforms material or institutional conditions and is answered by wages, prices, gifts, provisions, measures, or burdens.
- Surface relation: direct; striving, reckoning, deeds, reward, and an unending recompense appear at 84:6, 84:8, and 84:25.
- Surprising reach: Work crews, officeholding, animal labor, storage vessels, market price, parsimony, cargo, and capacity all enter the exchange system.

#### Subchannel A. Toil, Exertion, and Arduous Labor
- Reading type: surface-primary
- Scene or process: A worker expends sustained effort through hardship toward an eventual encounter or result.
- Active motifs: toil `ك د ح:B001/m01`; exertion `ع م ل:B007/m01`; hardship `ش ق ق:B003/m01`; arduous travel `ح ق ق:B012/m01`; maximal effort `ء ل ي:B010/m01`
- Ayah anchors: `ك د ح` (84:6); `ع م ل` (84:25); `ش ق ق` (84:1); `ح ق ق` (84:2, 84:5); `ء ل ي` (84:6, 84:9)
- Synthesis: The direct image of strenuous striving is reinforced by lexical scenes of hard travel and effort carried to capacity.

#### Subchannel B. Productive Action and Operational Work
- Reading type: mixed
- Scene or process: Intent is converted into an effective deed, operation, or repair.
- Active motifs: deed `ع م ل:B001/m01`; operation `ع م ل:B002/m01`; nurture and repair `ر ب ب:B002/m01`; effective penetration `ء ت ي:B013/m01`
- Ayah anchors: `ع م ل` (84:25); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ء ت ي` (84:7, 84:10)
- Synthesis: Work is not only effort but effective transformation, measured by whether an intended operation reaches its object.

#### Subchannel C. Wage, Reward, and Earned Return
- Reading type: mixed
- Scene or process: Completed labor generates an owed payment or recompense.
- Active motifs: wage `ء ج ر:B001/m01`; earned payment `ع م ل:B004/m01`; price `س ع ر:B003/m01`; due right `ح ق ق:B003/m01`
- Ayah anchors: `ء ج ر` (84:25); `ع م ل` (84:25); `س ع ر` (84:12); `ح ق ق` (84:2, 84:5)
- Synthesis: The promised reward at the close is economically modeled as a wage whose amount and payment follow from performed work.

#### Subchannel D. Office, Crew, and Organized Employment
- Reading type: latent/lexical
- Scene or process: An institution assigns roles to an officeholder and a coordinated body of workers.
- Active motifs: office `ع م ل:B003/m01`; work crew `ع م ل:B006/m01`; enrollment `ك ت ب:B004/m01`; administrative oversight `ح س ب:B006/m01`
- Ayah anchors: `ع م ل` (84:25); `ك ت ب` (84:7, 84:10); `ح س ب` (84:8)
- Synthesis: Individual deeds scale into organized employment through registration, delegated office, and collective labor.

#### Subchannel E. Price, Dealing, and Negotiated Value
- Reading type: latent/lexical
- Scene or process: Parties assess an object's value and transact under a stated or contested price.
- Active motifs: market price `س ع ر:B003/m01`; dealing `ع م ل:B005/m01`; calculation `ح س ب:B001/m01`; dialogue `ح و ر:B006/m01`
- Ayah anchors: `س ع ر` (84:12); `ع م ل` (84:25); `ح س ب` (84:8); `ح و ر` (84:14)
- Synthesis: Reckoning becomes commercial when calculation and dialogue determine the terms of exchange.

#### Subchannel F. Gift, Favor, and Unearned Bestowal
- Reading type: latent/lexical
- Scene or process: Value passes from giver to recipient as a gift or favor rather than as earned payment.
- Active motifs: bestowal `ء ت ي:B002/m01`; gift `ء ل ي:B012/m01`; favor `ر ب ب:B016/m03`; benefaction `م ن ن:B003/m01`; tested benefaction `ب ل ي:B003/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ء ل ي` (84:6, 84:9); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `م ن ن` (84:25); `ب ل ي` (84:15)
- Synthesis: The network sharply distinguishes earned recompense from value conferred through generosity, favor, or providential benefaction.

#### Subchannel G. Provision, Storage, and Parsimony
- Reading type: latent/lexical
- Scene or process: Goods are gathered into a reserve, guarded for dependents, and rationed or withheld.
- Active motifs: provision `ب ل ل:B002/m01`; need `ر ب ب:B016/m01`; parsimony `ش ف ق:B004/m01`; dependent wealth `ق ر ء:B013/m01`; storage vessel `و ع ي:B002/m01`; surplus wealth `ظ ه ر:B023/m01`
- Ayah anchors: `ب ل ل` (84:22); `ش ف ق` (84:16); `ق ر ء` (84:21); `و ع ي` (84:23); `ظ ه ر` (84:10)
- Synthesis: Gathering can secure a household reserve, but the same control over stored goods can become protective thrift or withholding.

#### Subchannel H. Measure, Weight, and Volume
- Reading type: latent/lexical
- Scene or process: Material value is standardized through counting, capacity, volume, and weight.
- Active motifs: standard measure `و س ق:B003/m01`; weight `م ن ن:B005/m01`; volume `م د د:B006/m01`; counting `ح س ب:B001/m01`
- Ayah anchors: `و س ق` (84:17, 84:18); `م ن ن` (84:25); `م د د` (84:3); `ح س ب` (84:8)
- Synthesis: Reckoning is materially grounded in the instruments and dimensions by which goods are quantified.

#### Subchannel I. Cargo, Debt, and Carried Burden
- Reading type: latent/lexical
- Scene or process: A load is placed on a carrier and persists as physical cargo or financial debt until discharged.
- Active motifs: burden or debt `ر ك ب:B003/m01`; carried load `و س ق:B001/m01`; mounted load `ظ ه ر:B005/m01`; throwing off a burden `ل ق ي:B005/m01`
- Ayah anchors: `ر ك ب` (84:19); `و س ق` (84:17, 84:18); `ظ ه ر` (84:10); `ل ق ي` (84:4, 84:6)
- Synthesis: What night gathers and earth casts out is mirrored economically in loads taken up, transported, and eventually discharged.

#### Subchannel J. Capacity, Readiness, and Sufficient Means
- Reading type: latent/lexical
- Scene or process: Action becomes possible when resources, skill, and access reach a sufficient threshold.
- Active motifs: capacity `ء ل ي:B011/m01`; readiness and ease `ي س ر:B001/m01`; adequacy `ح س ب:B003/m01`; fullness and alignment `و س ق:B004/m01`; available avenue `ء ت ي:B003/m01`
- Ayah anchors: `ء ل ي` (84:6, 84:9); `ي س ر` (84:8); `ح س ب` (84:8); `و س ق` (84:17, 84:18); `ء ت ي` (84:7, 84:10)
- Synthesis: Ease is not passivity but a state in which means, alignment, and access are sufficient for the required task.

### 8. Household, Lineage, and Care
- Semantic invariant: Domestic continuity is organized through marriage, descent, fertility, caregiving, guardianship, and protected family status.
- Surface relation: direct; return to one's people appears at 84:9 and 84:13, while the detailed kinship and care roles are latent lexical developments.
- Surprising reach: Stepchildren, childlessness, expected pregnancy, grandparental descent, jealousy, guardianship, and marital repudiation appear within the household frame.

#### Subchannel A. Marriage, Spousal Bond, and Repudiation
- Reading type: latent/lexical
- Scene or process: Two people enter a recognized household bond that can be strained by jealousy or a formal distancing formula.
- Active motifs: marriage `ء ه ل:B002/m01`; marital repudiation `ظ ه ر:B010/m01`; jealous protection `غ ي ر:B004/m01`; family belonging `ء ه ل:B001/m01`
- Ayah anchors: `ء ه ل` (84:9, 84:13); `ظ ه ر` (84:10); `غ ي ر` (84:25)
- Synthesis: The household is constituted by belonging and marriage but can be destabilized by possessiveness or juridical separation.

#### Subchannel B. Childlessness, Solitude, and Household Lack
- Reading type: latent/lexical
- Scene or process: A household is marked by the absence of spouse or offspring and the social solitude that follows.
- Active motifs: spouseless or childless state `خ ل و:B009/m01`; expected child `ظ ن ن:B009/m01`; family membership `ء ه ل:B001/m01`; empty state `خ ل و:B001/m01`
- Ayah anchors: `خ ل و` (84:4); `ظ ن ن` (84:14); `ء ه ل` (84:9, 84:13)
- Synthesis: Emptiness acquires a domestic meaning when the expected kin relation is absent from the household.

#### Subchannel C. Lineage, Descent, and Family Stock
- Reading type: latent/lexical
- Scene or process: Persons are located within a remembered line of descent that carries status and inherited affiliation.
- Active motifs: lineage and honor `ح س ب:B004/m01`; descent or stock `ر ك ب:B008/m01`; claimed lineage `د ع و:B002/m01`; noble stock `ع ذ ب:B008/m01`
- Ayah anchors: `ح س ب` (84:8); `ر ك ب` (84:19); `د ع و` (84:11); `ع ذ ب` (84:24)
- Synthesis: Family identity is both genealogical and evaluative, joining descent claims to inherited social standing.

#### Subchannel D. Caregiver, Stepchild, and Dependent Ward
- Reading type: latent/lexical
- Scene or process: A dependent child or ward is attached to an adult who nurtures, supervises, and protects.
- Active motifs: caregiver and stepchild `ر ب ب:B005/m01`; guardian `و ع ي:B007/m01`; protected charge `ح ق ق:B007/m01`; detained ward `ء ل ي:B013/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و ع ي` (84:23); `ح ق ق` (84:2, 84:5); `ء ل ي` (84:6, 84:9)
- Synthesis: Nurture becomes a structured relation of custody in which a vulnerable dependent is held and protected.

#### Subchannel E. Expected Child and Approaching Birth
- Reading type: latent/lexical
- Scene or process: A family interprets signs of pregnancy and anticipates an approaching child whose outcome is not yet visible.
- Active motifs: expected child `ظ ن ن:B009/m01`; conception `ل ق ي:B003/m01`; approaching event `ق ر ء:B004/m01`; human offspring `ب ش ر:B002/m01`
- Ayah anchors: `ظ ن ن` (84:14); `ل ق ي` (84:4, 84:6); `ق ر ء` (84:21); `ب ش ر` (84:24)
- Synthesis: Supposition acquires a domestic role as the uncertain but embodied expectation of new family life.

#### Subchannel F. Grandchild and Extended Descent
- Reading type: latent/lexical
- Scene or process: Family continuity passes beyond children into later descendants and younger generations.
- Active motifs: grandchild `و ر ي:B007/m01`; youth `ي س ر:B011/m01`; caregiver relation `ر ب ب:B005/m01`; lineage `ر ك ب:B008/m01`
- Ayah anchors: `و ر ي` (84:10); `ي س ر` (84:8); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ر ك ب` (84:19)
- Synthesis: Return to one's people is deepened by a multigenerational lineage extending through care, youth, and descent.

#### Subchannel G. Household Honor and Protective Jealousy
- Reading type: latent/lexical
- Scene or process: Family status is defended through honor codes that protect vulnerable members but can become possessive.
- Active motifs: protected charge `ح ق ق:B007/m01`; jealous protection `غ ي ر:B004/m01`; lineage honor `ح س ب:B004/m01`; removal of shame `ظ ه ر:B013/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `غ ي ر` (84:25); `ح س ب` (84:8); `ظ ه ر` (84:10)
- Synthesis: Domestic protection, lineage honor, jealousy, and shame management form a single social-status mechanism.

### 9. Community, Belonging, and Hospitality
- Semantic invariant: People become insiders, outsiders, residents, crowds, allies, guests, or named collectivities through patterns of settlement and recognition.
- Surface relation: direct; the surah twice depicts a person among their people at 84:9 and 84:13.
- Surprising reach: Foreigners, welcoming formulas, disciples, remote settlements, ethnonyms, toponyms, and deceptive familiarity all arise from belonging.

#### Subchannel A. Humanity and Human Collectivity
- Reading type: mixed
- Scene or process: Individual persons are recognized as members of the broader human kind and of gathered social bodies.
- Active motifs: human being `ء ن س:B001/m01`; humankind `ب ش ر:B002/m01`; people `و ر ي:B008/m01`; gathered crowd `و ع ي:B008/m01`
- Ayah anchors: `ء ن س` (84:6); `ب ش ر` (84:24); `و ر ي` (84:10); `و ع ي` (84:23)
- Synthesis: The addressed human is situated within progressively larger circles of species, people, and assembled community.

#### Subchannel B. Family Belonging, Class, and Social Body
- Reading type: mixed
- Scene or process: A person belongs to a household and also occupies a class within a larger social body.
- Active motifs: family and belonging `ء ه ل:B001/m01`; social class `ط ب ق:B005/m01`; crowd `ر ب ب:B004/m01`; collected group `و ع ي:B008/m01`
- Ayah anchors: `ء ه ل` (84:9, 84:13); `ط ب ق` (84:19); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و ع ي` (84:23)
- Synthesis: The surface household is nested within classes and crowds that define wider communal membership.

#### Subchannel C. Settlement, Residence, and Inhabited Place
- Reading type: latent/lexical
- Scene or process: People settle a site, make it habitable, and acquire a stable relation to its land.
- Active motifs: inhabited place `ء ه ل:B004/m01`; settlement `ء ر ض:B006/m01`; settled residence `ر ب ب:B007/m01`; remote settlement `ك ف ر:B012/m01`
- Ayah anchors: `ء ه ل` (84:9, 84:13); `ء ر ض` (84:3); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ك ف ر` (84:22)
- Synthesis: Belonging is spatialized through residence, from central inhabited land to a remote outlying settlement.

#### Subchannel D. Stranger, Foreigner, and Outsider
- Reading type: latent/lexical
- Scene or process: A newcomer arrives without established ties and is recognized as outside the resident group.
- Active motifs: stranger `ء ت ي:B006/m01`; foreigner `ء ر ض:B004/m01`; otherness `غ ي ر:B005/m01`; unfamiliar elder or outsider `ك و ن:B005/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ء ر ض` (84:3); `غ ي ر` (84:25); `ك و ن` (84:13, 84:15)
- Synthesis: Arrival has a social consequence when the comer lacks local belonging and is classified as other.

#### Subchannel E. Welcome, Familiarity, and Intimate Company
- Reading type: latent/lexical
- Scene or process: An outsider is received into familiar company through welcome, recognition, and close association.
- Active motifs: familiarity `ء ن س:B003/m01`; intimate companion `ء ن س:B006/m01`; welcome `ء ه ل:B005/m01`; private company `خ ل و:B002/m01`
- Ayah anchors: `ء ن س` (84:6); `ء ه ل` (84:9, 84:13); `خ ل و` (84:4)
- Synthesis: Hospitality converts social distance into familiarity and, at its closest, shared private space.

#### Subchannel F. Supporters, Disciples, and Allied Community
- Reading type: latent/lexical
- Scene or process: A central figure is surrounded by people who extend support, reinforce standing, and share allegiance.
- Active motifs: supporter or disciple `ح و ر:B003/m01`; supporters `ظ ه ر:B016/m01`; reinforcement `م د د:B002/m01`; reliable allegiance `ء م ن:B001/m01`
- Ayah anchors: `ح و ر` (84:14); `ظ ه ر` (84:10); `م د د` (84:3); `ء م ن` (84:20, 84:25)
- Synthesis: Community becomes operational when affiliation is converted into reinforcement and dependable support.

#### Subchannel G. Tribe, Ethnonym, and Place-Name
- Reading type: latent/lexical
- Scene or process: A collective identity is fixed through a tribal name, regional designation, or remembered place-name.
- Active motifs: tribal name `ب ل ي:B007/m01`; ethnonym or place-name `ل ي ل:B004/m01`; Yemen `ي م ن:B005/m01`; proper place-name `ي س ر:B010/m01`; sacred toponym `ص ل ح:B005/m01`
- Ayah anchors: `ب ل ي` (84:15); `ل ي ل` (84:17); `ي م ن` (84:7); `ي س ر` (84:8); `ص ل ح` (84:25)
- Synthesis: Belonging is preserved linguistically by names that bind communities to lineage, region, and place.

#### Subchannel H. Hospitality, Deceptive Familiarity, and Boasting
- Reading type: latent/lexical
- Scene or process: Social warmth can be genuine welcome or a performance masking deception and status display.
- Active motifs: welcoming familiarity `ء ن س:B003/m01`; welcome `ء ه ل:B005/m01`; deceptive private approach `خ ل و:B015/m01`; boasting `ظ ه ر:B024/m01`
- Ayah anchors: `ء ن س` (84:6); `ء ه ل` (84:9, 84:13); `خ ل و` (84:4); `ظ ه ر` (84:10)
- Synthesis: The convivial household scene has a shadow form in manipulative intimacy and public self-display.

### 10. Embodied Form and Bodily Marking
- Semantic invariant: The body is mapped through surfaces, openings, joints, sides, colors, traces, and tissues that display identity or condition.
- Surface relation: indirect; body-oriented surface roots occur throughout S084, especially face, back, sight, and right-hand imagery at 84:7, 84:10, and 84:15.
- Surprising reach: The navel, pubis, uvula, lip, sclera, palm lines, marrow, fat, armor-like skin, and facial palsy form a highly articulated anatomy.

#### Subchannel A. Face, Beauty, and Facial Condition
- Reading type: latent/lexical
- Scene or process: The face presents identity and beauty but can also register muscular impairment.
- Active motifs: face `ب ش ر:B006/m01`; facial beauty `ق س م:B001/m01`; facial palsy `ل ق ي:B001/m01`; visible surface `ظ ه ر:B001/m01`
- Ayah anchors: `ب ش ر` (84:24); `ق س م` (84:16); `ل ق ي` (84:4, 84:6); `ظ ه ر` (84:10)
- Synthesis: The face is both a valued public surface and a diagnostic site where bodily disorder becomes visible.

#### Subchannel B. Ear, Appendage, and Handle
- Reading type: mixed
- Scene or process: A projecting form receives sound in the body and provides a grasping point on an object.
- Active motifs: ear `ء ذ ن:B001/m01`; handle or ear-like appendage `ء ذ ن:B001/m02`; hearing `ء ذ ن:B002/m01`; direct grasp `ب ل ل:B004/m01`
- Ayah anchors: `ء ذ ن` (84:2, 84:5); `ب ل ل` (84:22)
- Synthesis: The ear's receptive and projecting shape motivates a bridge from sensory anatomy to object design and graspability.

#### Subchannel C. Lip, Uvula, Tongue Tip, and Voice
- Reading type: latent/lexical
- Scene or process: The mouth's edges and suspended structures shape articulation and projected speech.
- Active motifs: cleft upper lip `ع ل م:B004/m01`; inverted lip `ق ل ب:B012/m01`; uvula `ش ق ق:B008/m01`; tongue tip `ع ذ ب:B006/m02`; projected voice `ش ق ق:B008/m02`
- Ayah anchors: `ع ل م` (84:23); `ق ل ب` (84:9); `ش ق ق` (84:1); `ع ذ ب` (84:24)
- Synthesis: Speech is anatomically grounded in small visible and suspended structures whose shape can alter articulation.

#### Subchannel D. Navel, Umbilical Center, and Severance
- Reading type: latent/lexical
- Scene or process: A central bodily mark records former nourishment and the cutting of an original attachment.
- Active motifs: navel `س ر ر:B006/m01`; bodily trace `ب ص ر:B004/m01`; cutting or termination `م ن ن:B001/m01`; inner essence `س ر ر:B005/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ب ص ر` (84:15); `م ن ن` (84:25)
- Synthesis: The navel is a residual surface sign of a once-internal bond that has been severed.

#### Subchannel E. Pubis, Groin, and Protected Intimacy
- Reading type: latent/lexical
- Scene or process: The lower central body is marked as an intimate and socially protected zone.
- Active motifs: pubis `ر ك ب:B006/m01`; protected charge `ح ق ق:B007/m01`; bodily mark `ي س ر:B008/m01`; privacy `خ ل و:B002/m01`
- Ayah anchors: `ر ك ب` (84:19); `ح ق ق` (84:2, 84:5); `ي س ر` (84:8); `خ ل و` (84:4)
- Synthesis: Anatomy and social regulation meet in a body region defined by centrality, privacy, and protection.

#### Subchannel F. Back, Spine, and Posterior Surface
- Reading type: mixed
- Scene or process: The body's rear surface supports loads, displays turning away, and borders the birth passage.
- Active motifs: back `ظ ه ر:B002/m01`; back disease `ر ك ب:B010/m01`; rear or birth passage `ص ل ي:B006/m01`; mounted load `ظ ه ر:B005/m01`
- Ayah anchors: `ظ ه ر` (84:10); `ر ك ب` (84:19); `ص ل ي` (84:12)
- Synthesis: The back is simultaneously anatomy, carrying surface, directional orientation, and a site of bodily vulnerability.

#### Subchannel G. Joint, Knee, and Forehead
- Reading type: latent/lexical
- Scene or process: Articulated contact points permit movement or ritual lowering and can be struck, marked, or fitted.
- Active motifs: joint or socket `ح ق ق:B011/m01`; struck joint `ط ب ق:B006/m01`; knee `ر ك ب:B005/m01`; forehead and prostration mark `س ج د:B003/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ط ب ق` (84:19); `ر ك ب` (84:19); `س ج د` (84:21)
- Synthesis: Joints organize movement, while the knee and forehead become contact surfaces in lowered posture.

#### Subchannel H. Skin, Hide, and Outer Surface
- Reading type: latent/lexical
- Scene or process: An outer membrane covers the body, can be peeled or tanned, and can be joined as material.
- Active motifs: bodily surface `ب ش ر:B001/m01`; peeled skin `ب ش ر:B004/m01`; hide `ح و ر:B004/m01`; thick hide edge `ب ص ر:B006/m01`
- Ayah anchors: `ب ش ر` (84:24); `ح و ر` (84:14); `ب ص ر` (84:15)
- Synthesis: The visible body surface bridges directly into worked hide as a removable, joinable protective layer.

#### Subchannel I. Complexion, Whiteness, and Dark Color
- Reading type: latent/lexical
- Scene or process: Color differences mark bodily appearance and can signal condition or categorical contrast.
- Active motifs: complexion `ح س ب:B009/m01`; whiteness `ح و ر:B002/m01`; dark coloration `س ع ر:B008/m01`; pale or green color `ق م ر:B002/m01`
- Ayah anchors: `ح س ب` (84:8); `ح و ر` (84:14); `س ع ر` (84:12); `ق م ر` (84:18)
- Synthesis: Visual contrast extends from the eye to the whole surface of the body through graded light and dark coloration.

#### Subchannel J. Lines, Wrinkles, and Identifying Marks
- Reading type: latent/lexical
- Scene or process: Fine linear traces on forehead, palm, or skin preserve identity, age, or prior contact.
- Active motifs: forehead and palm lines `س ر ر:B009/m01`; identifying marks `ي س ر:B008/m01`; mountain-pass-like crease `ك ف ر:B013/m01`; scratch `ك د ح:B002/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ي س ر` (84:8); `ك ف ر` (84:22); `ك د ح` (84:6)
- Synthesis: Bodily surfaces are readable records whose lines and scratches function as persistent signs.

#### Subchannel K. Flesh, Fat, Oil, and Marrow
- Reading type: latent/lexical
- Scene or process: Soft tissues and stored fats occupy protected interior or posterior regions and supply bodily richness.
- Active motifs: rump flesh `ء ل ي:B015/m01`; fat `و ر ي:B004/m01`; fat or oil `ء ه ل:B006/m01`; mature fat animal `ح ق ق:B013/m01`; inner essence `ق ل ب:B002/m01`
- Ayah anchors: `ء ل ي` (84:6, 84:9); `و ر ي` (84:10); `ء ه ل` (84:9, 84:13); `ح ق ق` (84:2, 84:5); `ق ل ب` (84:9)
- Synthesis: The body's less visible substance is represented as nutritive richness concealed beneath an identifying surface.

#### Subchannel L. Limb, Organ, and Integrated Form
- Reading type: latent/lexical
- Scene or process: Distinct limbs and organs cooperate as components of a single shaped body.
- Active motifs: limb or organ `ع م ل:B010/m01`; bodily shape `ل ق ي:B002/m01`; matched joint `ط ب ق:B003/m01`; human surface `ب ش ر:B001/m01`
- Ayah anchors: `ع م ل` (84:25); `ل ق ي` (84:4, 84:6); `ط ب ق` (84:19); `ب ش ر` (84:24)
- Synthesis: Embodied action depends on fitted parts whose collective organization produces a recognizable human form.

### 11. Disease, Injury, and Recovery
- Semantic invariant: Bodily integrity is disrupted by wound, infection, fracture, pain, deprivation, or mental disturbance and may be restored through repair.
- Surface relation: direct; painful punishment is direct at 84:12 and 84:24, while the medical conditions and treatments arise through lexical extensions of surface roots.
- Surprising reach: Pus, epidemic, scabies, facial palsy, snow blindness, fracture setting, convalescence, contagion, and derangement form a detailed pathological system.

#### Subchannel A. Wound, Pus, and Discharge
- Reading type: latent/lexical
- Scene or process: Damaged tissue festers, accumulates fluid, and releases a painful discharge.
- Active motifs: festering wound `ء ر ض:B011/m01`; pus `م د د:B007/m01`; purulent accumulation `و ع ي:B004/m01`; bodily pain `ء ل م:B001/m01`
- Ayah anchors: `ء ر ض` (84:3); `م د د` (84:3); `و ع ي` (84:23); `ء ل م` (84:24)
- Synthesis: The earth's emptying has a bodily analogue in a wound that gathers and expels corrupt material.

#### Subchannel B. Internal Disease and Neuromuscular Impairment
- Reading type: latent/lexical
- Scene or process: Hidden disease affects an internal organ or the nerves controlling visible movement.
- Active motifs: internal disease `و ر ي:B001/m01`; heart disease `ق ل ب:B011/m01`; facial palsy `ل ق ي:B001/m01`; diseased back `ر ك ب:B010/m01`
- Ayah anchors: `و ر ي` (84:10); `ق ل ب` (84:9); `ل ق ي` (84:4, 84:6); `ر ك ب` (84:19)
- Synthesis: Concealed pathology becomes legible through impaired facial, cardiac, or spinal function.

#### Subchannel C. Fracture, Setting, and Bone Union
- Reading type: latent/lexical
- Scene or process: A broken bone is aligned, bound, and gradually knitted back into integrity.
- Active motifs: fracture setting `ء ج ر:B002/m01`; knitting bone `و ع ي:B003/m01`; repair `ص ل ح:B001/m01`; matched fit `ط ب ق:B003/m01`
- Ayah anchors: `ء ج ر` (84:25); `و ع ي` (84:23); `ص ل ح` (84:25); `ط ب ق` (84:19)
- Synthesis: Medical repair follows the same structural logic as fitting and joining separated parts.

#### Subchannel D. Epidemic, Contagion, and Afflicted Locality
- Reading type: latent/lexical
- Scene or process: Illness attaches to a place, spreads among residents, and defines the locality as dangerous.
- Active motifs: local epidemic `ق ر ء:B008/m01`; cold or contagion `ء ر ض:B009/m01`; remote settlement `ك ف ر:B012/m01`; inhabited place `ء ه ل:B004/m01`
- Ayah anchors: `ق ر ء` (84:21); `ء ر ض` (84:3); `ك ف ر` (84:22); `ء ه ل` (84:9, 84:13)
- Synthesis: Disease can be mapped geographically when a settlement and its inhabitants become associated with a transmissible affliction.

#### Subchannel E. Mange, Scabies, and Animal Skin Disease
- Reading type: latent/lexical
- Scene or process: Irritating lesions spread across characteristic skin or back sites in livestock.
- Active motifs: scabies sites `س ع ر:B005/m01`; sheep back disease `ر ك ب:B010/m01`; hide `ح و ر:B004/m01`; scratch `ك د ح:B002/m01`
- Ayah anchors: `س ع ر` (84:12); `ر ك ب` (84:19); `ح و ر` (84:14); `ك د ح` (84:6)
- Synthesis: Surface irritation unites animal pathology, hide, and scratching into a coherent veterinary scene.

#### Subchannel F. Convalescence and Restored Fitness
- Reading type: latent/lexical
- Scene or process: A weakened subject recovers moisture, strength, and functional soundness after illness or wear.
- Active motifs: recovery `ب ل ل:B003/m01`; wear and decay `ب ل ي:B001/m01`; repair `ص ل ح:B001/m01`; restored fitness `ص ل ح:B003/m01`
- Ayah anchors: `ب ل ل` (84:22); `ب ل ي` (84:15); `ص ل ح` (84:25)
- Synthesis: Recovery reverses depletion by restoring the subject's integrity and capacity for proper function.

#### Subchannel G. Pain, Infliction, and Torment
- Reading type: mixed
- Scene or process: Suffering is experienced as sensation and deliberately intensified as punitive infliction.
- Active motifs: bodily pain `ء ل م:B001/m01`; painful infliction `ء ل م:B002/m01`; punishment `ع ذ ب:B005/m01`; frenzied torment `س ع ر:B004/m01`
- Ayah anchors: `ء ل م` (84:24); `ع ذ ب` (84:24); `س ع ر` (84:12)
- Synthesis: The surface painful punishment is lexically decomposed into felt pain, an inflicting agent, and escalating torment.

#### Subchannel H. Hunger, Thirst, and Forced Abstinence
- Reading type: latent/lexical
- Scene or process: Food or drink is withheld, producing deprivation and a heightened need for supply.
- Active motifs: abstention from food or drink `ع ذ ب:B002/m01`; water need `ر ب ب:B013/m01`; prevention `ع ذ ب:B003/m01`; absence of delay or relief `ك ذ ب:B005/m01`
- Ayah anchors: `ع ذ ب` (84:24); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ك ذ ب` (84:22)
- Synthesis: Punitive deprivation is modeled as blocked access to the provisions needed to restore the body.

#### Subchannel I. Derangement, Possession, and Disordered Condition
- Reading type: latent/lexical
- Scene or process: Mental or behavioral coherence collapses into an afflicted, unstable state.
- Active motifs: deranged or possessed person `ء ر ض:B012/m01`; bad condition `ك و ن:B006/m01`; internal disorder `ق ل ب:B011/m01`; frenzy `س ع ر:B004/m01`
- Ayah anchors: `ء ر ض` (84:3); `ك و ن` (84:13, 84:15); `ق ل ب` (84:9); `س ع ر` (84:12)
- Synthesis: Pathology reaches beyond tissue into a condition where cognition, behavior, and inner state lose stable order.

#### Subchannel J. Cold Injury and Snow Blindness
- Reading type: latent/lexical
- Scene or process: Severe cold or reflected brightness impairs exposed tissue and vision.
- Active motifs: cold affliction `ء ر ض:B009/m01`; snow blindness `ق م ر:B005/m01`; eyesight `ب ص ر:B001/m01`; direct exposure `ب ش ر:B003/m01`
- Ayah anchors: `ء ر ض` (84:3); `ق م ر` (84:18); `ب ص ر` (84:15); `ب ش ر` (84:24)
- Synthesis: Environmental exposure links lunar brightness, cold terrain, and temporary failure of sight.

### 12. Gestation, Birth, and Animal Husbandry
- Semantic invariant: Reproductive life moves from cyclic readiness through conception, gestation, birth, nursing, herd care, and animal labor.
- Surface relation: indirect; the parent is latent but is built entirely from roots occurring in S084, especially gathering, meeting, returning, coming, and livestock-related branch senses.
- Surprising reach: Womb contents, afterbirth, camel gestation, ewe lactation, estrus, working animals, and herd dependency create a complete husbandry cycle.

#### Subchannel A. Womb, Conception, and Fetal Gathering
- Reading type: latent/lexical
- Scene or process: The womb receives reproductive material, gathers a fetus, and holds developing life.
- Active motifs: fetal gathering in the womb `ق ر ء:B003/m01`; conception `ل ق ي:B003/m01`; womb or afterbirth `ع ذ ب:B009/m01`; calf or young `ح و ر:B008/m01`
- Ayah anchors: `ق ر ء` (84:21); `ل ق ي` (84:4, 84:6); `ع ذ ب` (84:24); `ح و ر` (84:14)
- Synthesis: Gathering and meeting acquire a biological role in the reception and containment of developing offspring.

#### Subchannel B. Delivery, Birth Passage, and Afterbirth
- Reading type: latent/lexical
- Scene or process: Gestation culminates at a delivery place through a birth passage followed by expelled afterbirth.
- Active motifs: delivery place or seat `ث ب ر:B005/m01`; birth passage `ص ل ي:B006/m01`; afterbirth or blood `ق ر ء:B003/m02`; emptying `خ ل و:B001/m01`
- Ayah anchors: `ث ب ر` (84:11); `ص ل ي` (84:12); `ق ر ء` (84:21); `خ ل و` (84:4)
- Synthesis: The surah's broader emptying pattern appears biologically as the ordered release of offspring and afterbirth.

#### Subchannel C. Reproductive Cycle and Readiness
- Reading type: latent/lexical
- Scene or process: Periodic bodily changes establish reproductive readiness and delimit phases of fertility.
- Active motifs: reproductive period `ق ر ء:B002/m02`; camel estrus `ق ر ء:B009/m01`; estrus `ء ت ي:B012/m01`; recurring interval `ط ب ق:B010/m01`
- Ayah anchors: `ق ر ء` (84:21); `ء ت ي` (84:7, 84:10); `ط ب ق` (84:19)
- Synthesis: Cyclical time becomes reproductive timing through recurring periods of readiness and approach.

#### Subchannel D. Camel Gestation, Motherhood, and Bereavement
- Reading type: latent/lexical
- Scene or process: A mature female camel carries young, gives birth, and may become defined by the loss of offspring.
- Active motifs: mature camel `ح ق ق:B008/m01`; grave or pregnant camel `ب ل ي:B006/m01`; bereft she-camel `خ ل و:B010/m01`; calf `ح و ر:B008/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ب ل ي` (84:15); `خ ل و` (84:4); `ح و ر` (84:14)
- Synthesis: Maturity, pregnancy, offspring, and loss describe the full reproductive status cycle of a domesticated camel.

#### Subchannel E. Mating, Estrus, and Animal Approach
- Reading type: latent/lexical
- Scene or process: A male approaches a receptive animal during a seasonally or physiologically marked period.
- Active motifs: bull mating `س م و:B003/m01`; estrus `ء ت ي:B012/m01`; camel estrus `ق ر ء:B009/m01`; expected offspring `ظ ن ن:B009/m01`
- Ayah anchors: `س م و` (84:1); `ء ت ي` (84:7, 84:10); `ق ر ء` (84:21); `ظ ن ن` (84:14)
- Synthesis: Ascent, coming, and cyclical readiness converge on the directed approach that initiates animal reproduction.

#### Subchannel F. Ewe, Udder, Milk, and Nursing Yield
- Reading type: latent/lexical
- Scene or process: A ewe bears young and supplies milk whose abundance or cessation measures reproductive health.
- Active motifs: newborn ewe `ر ب ب:B009/m01`; reserved milk `د ع و:B003/m01`; milk cessation `ك ذ ب:B006/m01`; milk fertility `ي س ر:B006/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `د ع و` (84:11); `ك ذ ب` (84:22); `ي س ر` (84:8)
- Synthesis: Nursing links maternal condition, stored milk, fertility, and the failure or ease of yield.

#### Subchannel G. Herd, Livestock Wealth, and Dependents
- Reading type: latent/lexical
- Scene or process: Animals are gathered as a managed herd that constitutes wealth and supports dependents.
- Active motifs: herd `ر ب ب:B014/m01`; livestock wealth and dependents `ق ر ء:B013/m01`; driven herd `و س ق:B005/m01`; gathered load `و س ق:B002/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ق ر ء` (84:21); `و س ق` (84:17, 84:18)
- Synthesis: Night's gathering action has a pastoral analogue in assembling livestock that embody both material wealth and household support.

#### Subchannel H. Work Animal, Stamina, and Load Capacity
- Reading type: latent/lexical
- Scene or process: A domesticated animal is selected and trained for sustained work under load.
- Active motifs: work animal and stamina `ع م ل:B008/m01`; mature animal `ح ق ق:B008/m01`; driven livestock `و س ق:B005/m01`; mounted load `ظ ه ر:B005/m01`
- Ayah anchors: `ع م ل` (84:25); `ح ق ق` (84:2, 84:5); `و س ق` (84:17, 84:18); `ظ ه ر` (84:10)
- Synthesis: Animal maturity becomes economically valuable when converted into endurance, transport, and productive labor.

#### Subchannel I. Veterinary Disease and Herd Care
- Reading type: latent/lexical
- Scene or process: A keeper detects skin or back disease and intervenes to preserve the herd's function.
- Active motifs: sheep back disease `ر ك ب:B010/m01`; scabies sites `س ع ر:B005/m01`; nurture and repair `ر ب ب:B002/m01`; guardian `و ع ي:B007/m01`
- Ayah anchors: `ر ك ب` (84:19); `س ع ر` (84:12); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و ع ي` (84:23)
- Synthesis: Husbandry includes not only breeding and yield but diagnostic care for conditions that reduce animal fitness.

### 13. Hunting, Wildlife, and Animal Motion
- Semantic invariant: Animals are located, pursued, trapped, classified, and read through characteristic calls or patterns of movement.
- Surface relation: indirect; the scenes are lexical extensions of surface roots for elevation, moon, prayer, knowledge, heart, layering, and ease.
- Surprising reach: Nocturnal hunting, hawks, hyenas, wolves, snakes, doves, racing rank, and diagnostic gait form a coherent field ecology.

#### Subchannel A. Hunting, Night Hunt, and Trap
- Reading type: latent/lexical
- Scene or process: A hunter uses darkness and celestial timing to locate and capture quarry.
- Active motifs: hunting `س م و:B006/m01`; night hunting `ق م ر:B003/m01`; trap `ص ل ي:B005/m01`; concealed approach `و ر ي:B005/m01`
- Ayah anchors: `س م و` (84:1); `ق م ر` (84:18); `ص ل ي` (84:12); `و ر ي` (84:10)
- Synthesis: Moon, concealment, and directed capture combine into a specialized nocturnal hunting scene.

#### Subchannel B. Hawk, Dove, and Recognizable Bird
- Reading type: latent/lexical
- Scene or process: Birds are identified by predatory role, shape, or repeated call.
- Active motifs: hawk `ع ل م:B006/m01`; dove `ق م ر:B012/m01`; bird call `ب ل ل:B010/m01`; elevated flight `س م و:B001/m01`
- Ayah anchors: `ع ل م` (84:23); `ق م ر` (84:18); `ب ل ل` (84:22); `س م و` (84:1)
- Synthesis: Wildlife recognition coordinates visible elevation, species knowledge, and characteristic sound.

#### Subchannel C. Hyena, Wolf, and Serpent
- Reading type: latent/lexical
- Scene or process: Dangerous wild animals are recognized through species-specific form and proverbial threat.
- Active motifs: hyena `ع ل م:B007/m01`; wolf `ق ل ب:B013/m01`; serpent `ط ب ق:B009/m02`; white snake `ق ل ب:B009/m01`
- Ayah anchors: `ع ل م` (84:23); `ق ل ب` (84:9); `ط ب ق` (84:19)
- Synthesis: Knowledge of wild danger ranges from named predators to serpentine shapes encoded in figurative warning.

#### Subchannel D. Gait, Foreleg, and Rapid Movement
- Reading type: latent/lexical
- Scene or process: An animal's foreleg placement and stride reveal speed, soundness, and condition.
- Active motifs: foreleg or gait `ء ت ي:B009/m01`; fast movement `س ع ر:B007/m01`; gait `ط ب ق:B007/m01`; characteristic gait `ي س ر:B005/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `س ع ر` (84:12); `ط ب ق` (84:19); `ي س ر` (84:8)
- Synthesis: Coming and movement are anatomically specified through the repeated placement and tempo of the animal's limbs.

#### Subchannel E. Equestrian Training and Race Position
- Reading type: latent/lexical
- Scene or process: A horse is trained into a controlled gait and evaluated by its place relative to competitors.
- Active motifs: horse gait `ح ق ق:B014/m01`; controlled gait or stiffness `ط ب ق:B008/m01`; second in a race `ص ل ي:B007/m01`; rivalry `س م و:B007/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ط ب ق` (84:19); `ص ل ي` (84:12); `س م و` (84:1)
- Synthesis: Animal movement becomes competitive performance when disciplined gait determines rank.

#### Subchannel F. Herd Running, Stopping, and Driving
- Reading type: latent/lexical
- Scene or process: A moving group of animals alternates between charge, halt, and directed gathering.
- Active motifs: animal run and stop `ك ذ ب:B007/m01`; herd `ر ب ب:B014/m01`; driven herd `و س ق:B005/m01`; forceful movement `س ع ر:B007/m01`
- Ayah anchors: `ك ذ ب` (84:22); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و س ق` (84:17, 84:18); `س ع ر` (84:12)
- Synthesis: The herd's motion is a coordinated alternation between collective momentum and imposed restraint.

### 14. Travel, Orientation, and Transport
- Semantic invariant: Agents move along routes, cross distances, orient by side or elevation, meet destinations, and carry themselves or goods by animal or vessel.
- Surface relation: direct; striving toward encounter, returning, and riding layer after layer appear at 84:6, 84:9, 84:14, and 84:19.
- Surprising reach: Road junctions, pedestrians, ships, captains, left-right orientation, reclining, and throwing off loads emerge from the travel system.

#### Subchannel A. Road, Junction, and Established Route
- Reading type: latent/lexical
- Scene or process: A traveler selects and follows a known route through a branching junction.
- Active motifs: road or junction `ء ت ي:B010/m01`; practical method or road `ع م ل:B011/m01`; path `ق ر ء:B011/m01`; directional endpoint `ء ل ي:B001/m01`
- Ayah anchors: `ء ت ي` (84:7, 84:10); `ع م ل` (84:25); `ق ر ء` (84:21); `ء ل ي` (84:6, 84:9)
- Synthesis: Movement toward an endpoint depends on a patterned route that can also metaphorically structure action or study.

#### Subchannel B. Distance, Migration, and Pedestrian Travel
- Reading type: mixed
- Scene or process: A traveler leaves a settled place and covers a difficult distance on foot.
- Active motifs: distance `ش ق ق:B005/m01`; pedestrian `ع م ل:B012/m01`; remote settlement `ك ف ر:B012/m01`; arduous travel `ح ق ق:B012/m01`
- Ayah anchors: `ش ق ق` (84:1); `ع م ل` (84:25); `ك ف ر` (84:22); `ح ق ق` (84:2, 84:5)
- Synthesis: The surah's strenuous progress is spatialized as migration across a long route between settlements.

#### Subchannel C. Mounting, Riding, and Carried Load
- Reading type: mixed
- Scene or process: A rider mounts an animal or vehicle that bears both person and cargo.
- Active motifs: mount or riding `ر ك ب:B001/m01`; mounted load `ظ ه ر:B005/m01`; carried burden `و س ق:B001/m01`; work animal `ع م ل:B008/m01`
- Ayah anchors: `ر ك ب` (84:19); `ظ ه ر` (84:10); `و س ق` (84:17, 84:18); `ع م ل` (84:25)
- Synthesis: Riding from layer to layer extends naturally into the practical arrangement of rider, carrier, and load.

#### Subchannel D. Ship, Captain, and Water Passage
- Reading type: latent/lexical
- Scene or process: A vessel carries travelers over water under the direction of a responsible captain.
- Active motifs: ship `خ ل و:B011/m01`; captain `ر ب ب:B017/m01`; carried load `و س ق:B001/m01`; water `م د د:B003/m01`
- Ayah anchors: `خ ل و` (84:4); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و س ق` (84:17, 84:18); `م د د` (84:3)
- Synthesis: The transport scene transfers carrying and governance from land travel to a vessel moving across water.

#### Subchannel E. Right, Left, Side, and Inward Orientation
- Reading type: mixed
- Scene or process: The body and its path are oriented by right and left sides, inward face, and lateral deviation.
- Active motifs: right side `ي م ن:B002/m01`; left side `ي س ر:B004/m01`; inward-facing side `ء ن س:B004/m01`; swerving aside `ش ق ق:B009/m01`
- Ayah anchors: `ي م ن` (84:7); `ي س ر` (84:8); `ء ن س` (84:6); `ش ق ق` (84:1)
- Synthesis: The right-hand book is embedded in a broader directional grid that distinguishes sides, inward orientation, and deviation.

#### Subchannel F. Ascent, Descent, and Vertical Passage
- Reading type: mixed
- Scene or process: An agent rises, dominates a height, descends, or reclines after movement.
- Active motifs: ascent `س م و:B001/m01`; rising or domination `ظ ه ر:B007/m01`; downward thrust `ي س ر:B009/m01`; reclining `ل ق ي:B009/m01`
- Ayah anchors: `س م و` (84:1); `ظ ه ر` (84:10); `ي س ر` (84:8); `ل ق ي` (84:4, 84:6)
- Synthesis: Vertical movement supplies a spatial model for elevation, dominance, forced descent, and eventual rest.

#### Subchannel G. Encounter, Reception, and Casting Off
- Reading type: surface-primary
- Scene or process: A traveler reaches another party or destination, receives what arrives, and discards what was carried.
- Active motifs: encounter `ل ق ي:B004/m01`; throwing or casting off `ل ق ي:B005/m01`; arrival `ء ت ي:B001/m01`; return and outcome `ق ل ب:B005/m01`
- Ayah anchors: `ل ق ي` (84:4, 84:6); `ء ت ي` (84:7, 84:10); `ق ل ب` (84:9)
- Synthesis: The human journey toward meeting the Lord is mirrored by the earth's casting out, the book's arrival, and the traveler's final outcome.

### 15. Conflict, Competition, and Security
- Semantic invariant: Opposed agents attack, defend, compete, restrain, prepare, or suspend hostility through tactical and material means.
- Surface relation: indirect; the parent develops from S084 roots for splitting, fire, right, denial, layering, support, and protection rather than from an explicit battle scene.
- Surprising reach: Spear shafts, quivers, armor, forceful cavalry, gambling, schism, preventive detention, and preparedness produce a coherent conflict system.

#### Subchannel A. Charge, Thrust, and Forceful Attack
- Reading type: latent/lexical
- Scene or process: An attacker commits to a forward charge intended to penetrate an opposing line.
- Active motifs: thrust `ح ق ق:B009/m01`; failed or cowardly charge `ك ذ ب:B004/m01`; resolute charge `ك ذ ب:B004/m02`; downward thrust `ي س ر:B009/m01`; war ignition `س ع ر:B002/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ك ذ ب` (84:22); `ي س ر` (84:8); `س ع ر` (84:12)
- Synthesis: Truth-like firmness and false retreat are recast tactically as the contrast between a committed and failed attack.

#### Subchannel B. Weapon Shaft, Strap, Quiver, and Fragment
- Reading type: latent/lexical
- Scene or process: A weapon system is assembled from a shaft, securing strap, projectile container, and detachable pieces.
- Active motifs: spear shaft `ع م ل:B009/m01`; strap or thong `ع ذ ب:B006/m01`; arrow case `ر ب ب:B010/m01`; fragment `ش ق ق:B006/m01`; fitted insertion `ر ك ب:B004/m01`
- Ayah anchors: `ع م ل` (84:25); `ع ذ ب` (84:24); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ش ق ق` (84:1); `ر ك ب` (84:19)
- Synthesis: Joining, binding, and containing organize the material construction and readiness of weapons.

#### Subchannel C. Armor, Layering, and Bodily Defense
- Reading type: latent/lexical
- Scene or process: Protective material is fitted in overlapping layers over the body to absorb attack.
- Active motifs: armor `ب ص ر:B005/m01`; layered armor `ظ ه ر:B020/m01`; superposed cover `ط ب ق:B002/m01`; fitted shape `ل ق ي:B002/m01`
- Ayah anchors: `ب ص ر` (84:15); `ظ ه ر` (84:10); `ط ب ق` (84:19); `ل ق ي` (84:4, 84:6)
- Synthesis: The surah's layering vocabulary acquires a defensive material form in fitted, overlapping armor.

#### Subchannel D. Enemy, Opposition, and Schism
- Reading type: latent/lexical
- Scene or process: Distrust divides a community into opposed sides and identifies the other as an enemy.
- Active motifs: enemy `ظ ن ن:B007/m01`; direct confrontation `ء ر ض:B007/m01`; confrontation after seclusion `خ ل و:B014/m01`; schism `ش ق ق:B004/m01`; fierce opposition `ب ل ل:B005/m01`
- Ayah anchors: `ظ ن ن` (84:14); `ء ر ض` (84:3); `خ ل و` (84:4); `ش ق ق` (84:1); `ب ل ل` (84:22)
- Synthesis: Cognitive suspicion and structural splitting become a social process of factional opposition.

#### Subchannel E. Rivalry, Gambling, and Allotted Chance
- Reading type: latent/lexical
- Scene or process: Competitors seek superiority or stake value on a divided, chance-governed outcome.
- Active motifs: rivalry `س م و:B007/m01`; gambling `ق م ر:B007/m01`; lots `ي س ر:B007/m01`; division and allotment `ق س م:B003/m01`; gambling arrows `ر ب ب:B010/m01`
- Ayah anchors: `س م و` (84:1); `ق م ر` (84:18); `ي س ر` (84:8); `ق س م` (84:16); `ر ب ب` (84:2, 84:5, 84:6, 84:15)
- Synthesis: Competitive elevation and material risk converge in games where divided shares are assigned by chance.

#### Subchannel F. Restraint, Prevention, and Confinement
- Reading type: latent/lexical
- Scene or process: An authority or defender blocks movement, access, or harmful action.
- Active motifs: restraint `ث ب ر:B003/m01`; prevention `ع ذ ب:B003/m01`; withholding `ء ل ي:B009/m01`; necessary confinement `و ع ي:B006/m01`; verification detention `ق ر ء:B010/m01`
- Ayah anchors: `ث ب ر` (84:11); `ع ذ ب` (84:24); `ء ل ي` (84:6, 84:9); `و ع ي` (84:23); `ق ر ء` (84:21)
- Synthesis: Security is produced by limiting movement until danger, uncertainty, or liability is resolved.

#### Subchannel G. Precaution, Readiness, and Reinforcement
- Reading type: latent/lexical
- Scene or process: A threatened party anticipates attack, secures vulnerable points, and gathers support.
- Active motifs: precaution `ظ ه ر:B021/m01`; protected charge `ح ق ق:B007/m01`; prior detention or preparation `ء ل ي:B013/m01`; covenant security `ر ب ب:B011/m01`; reinforcement `م د د:B002/m01`
- Ayah anchors: `ظ ه ر` (84:10); `ح ق ق` (84:2, 84:5); `ء ل ي` (84:6, 84:9); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `م د د` (84:3)
- Synthesis: Defensive success depends on anticipatory custody, binding commitments, and reinforced capacity before conflict begins.

#### Subchannel H. Bow, Feather, and Projectile Flight
- Reading type: latent/lexical
- Scene or process: A bow launches a feathered projectile along an elevated path toward a target.
- Active motifs: bow `ك ف ر:B014/m01`; feather `ظ ه ر:B011/m01`; arrow case `ر ب ب:B010/m01`; elevated flight `س م و:B001/m01`
- Ayah anchors: `ك ف ر` (84:22); `ظ ه ر` (84:10); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `س م و` (84:1)
- Synthesis: Weapon, stabilizing feather, stored projectile, and flight form a compact projectile system.

### 16. Assembly, Division, and Structural Fit
- Semantic invariant: Material or conceptual wholes are made by joining parts, dividing surfaces, layering covers, matching forms, and articulating around pivots.
- Surface relation: direct; splitting, spreading, emptying, gathering, and passing through layers appear at 84:1, 84:3-4, 84:17, and 84:19.
- Surprising reach: Stitching, sockets, pleats, parity, inserted parts, stiff closures, and animal gait all instantiate the same structural operations.

#### Subchannel A. Joining, Stitching, and Gathering
- Reading type: mixed
- Scene or process: Separate elements are brought together and fastened into a continuous whole.
- Active motifs: joining or stitching `ك ت ب:B001/m01`; gathering `ق ر ء:B001/m02`; collecting `و س ق:B002/m01`; joining ends `ل ق ي:B010/m01`
- Ayah anchors: `ك ت ب` (84:7, 84:10); `ق ر ء` (84:21); `و س ق` (84:17, 84:18); `ل ق ي` (84:4, 84:6)
- Synthesis: The surah's gathering motion has a material counterpart in aligning and fastening separate edges or elements.

#### Subchannel B. Splitting, Half, and Fragment
- Reading type: mixed
- Scene or process: A whole opens along a line, separates into sides, and may leave detachable fragments.
- Active motifs: splitting `ش ق ق:B001/m01`; half or side `ش ق ق:B002/m01`; fragment `ش ق ق:B006/m01`; cleft form `ع ل م:B004/m01`
- Ayah anchors: `ش ق ق` (84:1); `ع ل م` (84:23)
- Synthesis: The sky's splitting projects into a general morphology of halves, sides, clefts, and broken pieces.

#### Subchannel C. Cover, Layer, and Superposition
- Reading type: surface-primary
- Scene or process: One surface covers another and repeated placement builds a multi-layered structure.
- Active motifs: cover `ط ب ق:B001/m01`; layers `ط ب ق:B002/m01`; stacking `ر ك ب:B002/m01`; covering `ك ف ر:B001/m01`
- Ayah anchors: `ط ب ق` (84:19); `ر ك ب` (84:19); `ك ف ر` (84:22)
- Synthesis: Riding layer upon layer is grounded in the physical operations of covering, stacking, and superposition.

#### Subchannel D. Matching, Parity, and Functional Fitness
- Reading type: latent/lexical
- Scene or process: Components correspond in shape or value closely enough to operate as a pair.
- Active motifs: match `ط ب ق:B003/m01`; parity `و س ق:B006/m01`; fitness `ص ل ح:B003/m01`; adequacy `ح س ب:B003/m01`
- Ayah anchors: `ط ب ق` (84:19); `و س ق` (84:17, 84:18); `ص ل ح` (84:25); `ح س ب` (84:8)
- Synthesis: Structural correspondence becomes functional when paired elements are equal, sufficient, and fit for their role.

#### Subchannel E. Axis, Pivot, Joint, and Socket
- Reading type: latent/lexical
- Scene or process: A moving part turns around a central axis seated within a fitted joint.
- Active motifs: axis `ح و ر:B007/m01`; joint or socket `ح ق ق:B011/m01`; struck joint `ط ب ق:B006/m01`; fitted insertion `ر ك ب:B004/m01`
- Ayah anchors: `ح و ر` (84:14); `ح ق ق` (84:2, 84:5); `ط ب ق` (84:19); `ر ك ب` (84:19)
- Synthesis: Return and turning are mechanically realized through a pivot held in a fitted articulation.

#### Subchannel F. Folding, Pleating, and Shaped Edge
- Reading type: latent/lexical
- Scene or process: A flexible surface is dampened, folded, or gathered into stable pleats and edges.
- Active motifs: folding while damp `ب ل ل:B007/m01`; garment fold `ق س م:B007/m01`; pleated gait-like fold `ح ق ق:B014/m01`; thick edge `ب ص ر:B006/m01`
- Ayah anchors: `ب ل ل` (84:22); `ق س م` (84:16); `ح ق ق` (84:2, 84:5); `ب ص ر` (84:15)
- Synthesis: Repeated bends create a structured surface whose folds resemble ordered movement and reinforced borders.

#### Subchannel G. Shape, Form, and Inversion
- Reading type: latent/lexical
- Scene or process: A recognizable form is produced, reversed, or compared to another shape.
- Active motifs: shape `ل ق ي:B002/m01`; inversion `ق ل ب:B004/m01`; inverted lip `ق ل ب:B012/m01`; serpentine form `ط ب ق:B009/m02`
- Ayah anchors: `ل ق ي` (84:4, 84:6); `ق ل ب` (84:9); `ط ب ق` (84:19)
- Synthesis: Turning and matching generate a morphology in which identity can survive transformation or inversion.

#### Subchannel H. Closure, Stiffness, and Blocked Articulation
- Reading type: latent/lexical
- Scene or process: A fitted structure closes so tightly that movement becomes restricted or rigid.
- Active motifs: closure or stiffness `ط ب ق:B008/m01`; restraint `ث ب ر:B003/m01`; securing knot `ر ب ب:B016/m02`; tight fit `ح ق ق:B010/m01`
- Ayah anchors: `ط ب ق` (84:19); `ث ب ر` (84:11); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ح ق ق` (84:2, 84:5)
- Synthesis: The same operations that produce secure assembly can pass into rigidity when closure eliminates needed movement.

### 17. Craft, Materials, and Furnishing
- Semantic invariant: Raw hide, fiber, wood, stone, pigment, and aromatic matter are shaped into textiles, tools, structures, furniture, and adornment.
- Surface relation: indirect; craft scenes arise from S084 roots for writing, joining, covering, spreading, back, heart, prayer, and splitting.
- Surprising reach: Tight weave, deceptive dye, termite damage, aloeswood, grinding slabs, parapetless roofs, couches, pillows, bracelets, and incense are all represented.

#### Subchannel A. Tight Weave and Hide Sewing
- Reading type: latent/lexical
- Scene or process: Fibers or hide edges are drawn together into a dense, durable surface.
- Active motifs: tight weave `ح ق ق:B010/m01`; sewing thick hide `ب ص ر:B006/m01`; stitching `ك ت ب:B001/m01`; hide `ح و ر:B004/m01`
- Ayah anchors: `ح ق ق` (84:2, 84:5); `ب ص ر` (84:15); `ك ت ب` (84:7, 84:10); `ح و ر` (84:14)
- Synthesis: Truth-like exactness becomes a craft value in tightly aligned fibers and securely joined hide.

#### Subchannel B. Cloth, Castoff, Fold, and Deceptive Dye
- Reading type: latent/lexical
- Scene or process: Textile is cut, folded, discarded, or colored so that appearance may conceal its actual condition.
- Active motifs: cloth fragment `ش ق ق:B006/m01`; castoff material `ل ق ي:B006/m01`; garment fold `ق س م:B007/m01`; deceptive dyed cloth `ك ذ ب:B009/m01`
- Ayah anchors: `ش ق ق` (84:1); `ل ق ي` (84:4, 84:6); `ق س م` (84:16); `ك ذ ب` (84:22)
- Synthesis: Textile handling moves from structural division and folding to an ethical problem when surface color misrepresents quality.

#### Subchannel C. Wood, Splinter, and Termite Damage
- Reading type: latent/lexical
- Scene or process: Wood is cut into pieces and remains vulnerable to hidden consumption by insects.
- Active motifs: termite `ء ر ض:B010/m01`; wooden fragment `ش ق ق:B006/m01`; aloeswood `ء ل ي:B014/m01`; concealed interior `س ر ر:B008/m01`
- Ayah anchors: `ء ر ض` (84:3); `ش ق ق` (84:1); `ء ل ي` (84:6, 84:9); `س ر ر` (84:9, 84:13)
- Synthesis: Split wood can become valued material, but its concealed interior may also host destructive infestation.

#### Subchannel D. Aloeswood, Firestick, and Incense
- Reading type: latent/lexical
- Scene or process: Aromatic wood is prepared, drilled or rubbed, and heated to release fire or fragrance.
- Active motifs: aloeswood `ء ل ي:B014/m01`; firestick cavity `س ر ر:B008/m01`; spark `و ر ي:B002/m01`; aloes plant `ء ل ي:B005/m01`
- Ayah anchors: `ء ل ي` (84:6, 84:9); `س ر ر` (84:9, 84:13); `و ر ي` (84:10)
- Synthesis: A valued plant becomes a worked aromatic material whose hidden cavity can generate ignition and scent.

#### Subchannel E. Cord, Strap, Tassel, and Shaft
- Reading type: latent/lexical
- Scene or process: Long flexible or rigid components are cut, bound, and attached to tools or ornaments.
- Active motifs: strap or thong `ع ذ ب:B006/m01`; spear shaft `ع م ل:B009/m01`; inserted attachment `ر ك ب:B004/m01`; cut fragment `ش ق ق:B006/m01`
- Ayah anchors: `ع ذ ب` (84:24); `ع م ل` (84:25); `ر ك ب` (84:19); `ش ق ق` (84:1)
- Synthesis: Craft organizes linear materials by cutting, binding, and fitting them into a functional composite.

#### Subchannel F. Grinding Slab, Flour, and Paste
- Reading type: latent/lexical
- Scene or process: Grain or another dry material is ground on stone and mixed into a workable paste.
- Active motifs: grinding slab `ص ل ي:B009/m01`; mixed condiment or paste `م د د:B008/m01`; syrup or reduced mixture `ر ب ب:B006/m01`; dampening `ب ل ل:B001/m01`
- Ayah anchors: `ص ل ي` (84:12); `م د د` (84:3); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `ب ل ل` (84:22)
- Synthesis: Friction, moisture, and mixture transform raw food material into a uniform processed substance.

#### Subchannel G. Rug, Roof, and Architectural Surface
- Reading type: latent/lexical
- Scene or process: Broad horizontal surfaces are spread underfoot or raised overhead as parts of habitation.
- Active motifs: thick rug `ء ر ض:B005/m01`; roof without parapet `ء ج ر:B003/m01`; outer surface `ظ ه ر:B003/m01`; covering layer `ط ب ق:B001/m01`
- Ayah anchors: `ء ر ض` (84:3); `ء ج ر` (84:25); `ظ ه ر` (84:10); `ط ب ق` (84:19)
- Synthesis: The spread earth and overhead sky are miniaturized architecturally as floor covering and roof.

#### Subchannel H. Couch, Pillow, and Furnished Rest
- Reading type: latent/lexical
- Scene or process: A raised couch and supporting cushion furnish a place for reclining and rest.
- Active motifs: couch or throne `س ر ر:B011/m01`; pillow `ح س ب:B008/m01`; reclining `ل ق ي:B009/m01`; inhabited place `ء ه ل:B004/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ح س ب` (84:8); `ل ق ي` (84:4, 84:6); `ء ه ل` (84:9, 84:13)
- Synthesis: Domestic habitation is materially completed by objects that support the resting body.

#### Subchannel I. Covering, Blanket, and Protective Wrap
- Reading type: latent/lexical
- Scene or process: Flexible material is placed over a body or object to conceal, warm, or protect it.
- Active motifs: cover `ط ب ق:B001/m01`; covering `ك ف ر:B001/m01`; cast covering `ل ق ي:B005/m01`; layered surface `ر ك ب:B002/m01`
- Ayah anchors: `ط ب ق` (84:19); `ك ف ر` (84:22); `ل ق ي` (84:4, 84:6); `ر ك ب` (84:19)
- Synthesis: Covering is a basic craft operation whose function ranges from concealment to insulation and layered protection.

#### Subchannel J. Bracelet, Aromatic Adornment, and Display
- Reading type: latent/lexical
- Scene or process: Worked material is worn or scented to enhance the body's visible and olfactory presentation.
- Active motifs: bracelet `ق ل ب:B008/m01`; aloeswood perfume `ء ل ي:B014/m01`; camphor `ك ف ر:B011/m01`; public surface `ب ش ر:B001/m01`
- Ayah anchors: `ق ل ب` (84:9); `ء ل ي` (84:6, 84:9); `ك ف ر` (84:22); `ب ش ر` (84:24)
- Synthesis: Concealed aromatic matter and shaped ornament are brought to the body as controlled social display.

#### Subchannel K. Household Goods and Portable Furnishings
- Reading type: latent/lexical
- Scene or process: Domestic objects are assembled as a movable stock that can be carried between residences.
- Active motifs: household goods `ظ ه ر:B014/m01`; couch `س ر ر:B011/m01`; pillow `ح س ب:B008/m01`; carried load `و س ق:B001/m01`
- Ayah anchors: `ظ ه ر` (84:10); `س ر ر` (84:9, 84:13); `ح س ب` (84:8); `و س ق` (84:17, 84:18)
- Synthesis: Furnishings become household property when resting objects are gathered into a transportable domestic inventory.

### 18. Fire, Heat, and Combustive Transformation
- Semantic invariant: Friction or ignition produces heat that cooks, straightens, illuminates, wages war, or inflicts torment.
- Surface relation: direct; entering a blaze and receiving painful punishment appear at 84:12 and 84:24.
- Surprising reach: Firestick cavities, ovens, material straightening, midday heat, sun motes, cough onset, and war ignition broaden the combustion scene.

#### Subchannel A. Spark, Firestick, and Ignition
- Reading type: latent/lexical
- Scene or process: Prepared wood is rubbed or struck until a concealed spark emerges and catches.
- Active motifs: spark `و ر ي:B002/m01`; firestick cavity `س ر ر:B008/m01`; ignition `س ع ر:B001/m01`; direct contact `ب ش ر:B003/m01`
- Ayah anchors: `و ر ي` (84:10); `س ر ر` (84:9, 84:13); `س ع ر` (84:12); `ب ش ر` (84:24)
- Synthesis: Fire begins as hidden potential released through contact between fitted materials.

#### Subchannel B. Oven, Heating, and Straightening
- Reading type: latent/lexical
- Scene or process: Sustained heat in a bounded chamber cooks matter or makes a warped object pliable enough to straighten.
- Active motifs: oven `س ع ر:B009/m01`; heating and straightening `ص ل ي:B004/m01`; exposure to fire `ص ل ي:B003/m01`; closure `ط ب ق:B008/m01`
- Ayah anchors: `س ع ر` (84:12); `ص ل ي` (84:12); `ط ب ق` (84:19)
- Synthesis: Contained heat is technically productive when it transforms food or restores material form.

#### Subchannel C. Blaze, War, and Punitive Torment
- Reading type: surface-primary
- Scene or process: Fire expands from physical flame into the consuming violence of battle and punishment.
- Active motifs: blaze `س ع ر:B001/m01`; war ignition `س ع ر:B002/m01`; frenzied torment `س ع ر:B004/m01`; fire exposure `ص ل ي:B003/m01`; punishment `ع ذ ب:B005/m01`
- Ayah anchors: `س ع ر` (84:12); `ص ل ي` (84:12); `ع ذ ب` (84:24)
- Synthesis: The surface blaze concentrates a lexical continuum from ignition to collective violence and inflicted suffering.

#### Subchannel D. Midday Heat, Sun Motes, and Rising Intensity
- Reading type: latent/lexical
- Scene or process: Solar heat reaches a daily peak, filling the air with visible motes and increasing intensity.
- Active motifs: midday heat `ق س م:B002/m01`; sun motes `س ع ر:B006/m01`; length or intensity `س ع ر:B011/m01`; midday exposure `ظ ه ر:B004/m01`
- Ayah anchors: `ق س م` (84:16); `س ع ر` (84:12); `ظ ه ر` (84:10)
- Synthesis: Heat is temporally staged, becoming most visible and forceful at the exposed middle of the day.

#### Subchannel E. Irritation, Cough, and Heat-Like Onset
- Reading type: latent/lexical
- Scene or process: A bodily irritation begins abruptly and intensifies like a kindled fire.
- Active motifs: onset or cough `س ع ر:B010/m01`; bodily pain `ء ل م:B001/m01`; internal disease `و ر ي:B001/m01`; rising intensity `س ع ر:B011/m01`
- Ayah anchors: `س ع ر` (84:12); `ء ل م` (84:24); `و ر ي` (84:10)
- Synthesis: Combustive vocabulary models the sudden onset and escalation of an internal irritation.

### 19. Food, Drink, and Material Richness
- Semantic invariant: Raw moisture, grain, sweetness, fat, and concentrated mixtures are transformed into nourishment or valued reserves.
- Surface relation: indirect; these scenes are lexical developments of S084 roots for lordship, extension, dampness, sweetness, fitness, and bodily surface.
- Surprising reach: Syrup, condiment, paste, flour, sweet water, mixed drink, tallow, oil, and animal fat create a compact culinary system.

#### Subchannel A. Syrup, Condiment, and Reduced Mixture
- Reading type: latent/lexical
- Scene or process: Liquid or crushed material is concentrated and blended into a thick flavoring or paste.
- Active motifs: syrup `ر ب ب:B006/m01`; mixed condiment or paste `م د د:B008/m01`; dampening `ب ل ل:B001/m01`; proper consistency `ص ل ح:B003/m01`
- Ayah anchors: `ر ب ب` (84:2, 84:5, 84:6, 84:15); `م د د` (84:3); `ب ل ل` (84:22); `ص ل ح` (84:25)
- Synthesis: Extension and reduction work together in culinary preparation until ingredients reach a fit consistency.

#### Subchannel B. Flour, Grinding, and Dough Formation
- Reading type: latent/lexical
- Scene or process: Grain is pulverized and combined with moisture into a cohesive food material.
- Active motifs: grinding slab `ص ل ي:B009/m01`; dampness `ب ل ل:B001/m01`; joined mass `ك ت ب:B001/m01`; measured volume `م د د:B006/m01`
- Ayah anchors: `ص ل ي` (84:12); `ب ل ل` (84:22); `ك ت ب` (84:7, 84:10); `م د د` (84:3)
- Synthesis: Grinding divides grain while measured moisture rejoins the particles as dough.

#### Subchannel C. Sweet Water and Mixed Drink
- Reading type: latent/lexical
- Scene or process: Water is evaluated for sweetness and combined with other material into a prepared drink.
- Active motifs: sweet water `ع ذ ب:B001/m01`; mixed drink `م د د:B008/m01`; water supply `ر ب ب:B013/m01`; fullness `و س ق:B004/m01`
- Ayah anchors: `ع ذ ب` (84:24); `م د د` (84:3); `ر ب ب` (84:2, 84:5, 84:6, 84:15); `و س ق` (84:17, 84:18)
- Synthesis: Nourishing drink depends on both the quality of its water and the measured completeness of its mixture.

#### Subchannel D. Fat, Oil, and Tallow
- Reading type: latent/lexical
- Scene or process: Animal or plant tissues yield rich fats used as food, fuel, or household material.
- Active motifs: fat `و ر ي:B004/m01`; fat or oil `ء ه ل:B006/m01`; mature fat animal `ح ق ق:B013/m01`; bodily flesh `ء ل ي:B015/m01`
- Ayah anchors: `و ر ي` (84:10); `ء ه ل` (84:9, 84:13); `ح ق ق` (84:2, 84:5); `ء ل ي` (84:6, 84:9)
- Synthesis: Stored bodily richness crosses into household use as edible fat, oil, or combustible tallow.

#### Subchannel E. Moisture, Freshness, and Preserved Provision
- Reading type: latent/lexical
- Scene or process: Controlled moisture keeps food usable, while excessive exposure or withholding threatens its quality.
- Active motifs: dampness `ب ل ل:B001/m01`; provision `ب ل ل:B002/m01`; recovery of freshness `ب ل ل:B003/m01`; storage vessel `و ع ي:B002/m01`; parsimony `ش ف ق:B004/m01`
- Ayah anchors: `ب ل ل` (84:22); `و ع ي` (84:23); `ش ف ق` (84:16)
- Synthesis: Food preservation balances moisture, storage, and distribution so that a reserve remains fit for use.

### 20. Change, Trial, and Outcome
- Semantic invariant: Subjects pass through testing, reversal, delay, deterioration, repair, ruin, persistence, and final termination.
- Surface relation: direct; the surah repeatedly stages irreversible transition, return, encounter, reckoning, and contrasting outcomes.
- Surprising reach: Vicissitudes, calamity, structural repair, delayed approach, burial, forgetting, weathering, and stubborn persistence elaborate the passage from state to state.

#### Subchannel A. Trial, Inquiry, and Lived Experience
- Reading type: mixed
- Scene or process: A subject enters a testing situation whose result reveals quality, reliability, or character.
- Active motifs: trial `ب ل ي:B002/m01`; inquiry and testing `ح س ب:B010/m01`; lived experience or fortune `ل ق ي:B007/m01`; calamity as experience `ء ت ي:B011/m01`
- Ayah anchors: `ب ل ي` (84:15); `ح س ب` (84:8); `ل ق ي` (84:4, 84:6); `ء ت ي` (84:7, 84:10)
- Synthesis: Reckoning is prepared by lived tests that expose what a subject becomes under changing conditions.

#### Subchannel B. Vicissitude, Fortune, and Uncertain Event
- Reading type: latent/lexical
- Scene or process: Events arrive unpredictably and alter a person's fortune beyond prior calculation.
- Active motifs: vicissitudes `د ع و:B006/m01`; fortune or experience `ل ق ي:B007/m01`; arriving calamity `ء ت ي:B011/m01`; unreliable outcome `ظ ن ن:B006/m01`
- Ayah anchors: `د ع و` (84:11); `ل ق ي` (84:4, 84:6); `ء ت ي` (84:7, 84:10); `ظ ن ن` (84:14)
- Synthesis: Coming events frustrate confident expectation and convert abstract uncertainty into experienced reversal.

#### Subchannel C. Ruin, Collapse, and Overwhelming Calamity
- Reading type: latent/lexical
- Scene or process: A structure or life-course fails catastrophically and falls beyond ordinary repair.
- Active motifs: ruin `ث ب ر:B002/m01`; cascading collapse `د ع و:B005/m01`; ruin or devastation `ح و ر:B009/m01`; enclosing calamity `ط ب ق:B009/m01`
- Ayah anchors: `ث ب ر` (84:11); `د ع و` (84:11); `ح و ر` (84:14); `ط ب ق` (84:19)
- Synthesis: The cry for destruction belongs to a larger scene of collapse that closes around the affected subject.

#### Subchannel D. Return, Decline, and Reversed Course
- Reading type: mixed
- Scene or process: A movement reaches a turning point and proceeds back toward an earlier place or diminished condition.
- Active motifs: return or decline `ح و ر:B005/m01`; return and outcome `ق ل ب:B005/m01`; elapsed condition `خ ل و:B003/m01`; reversing turn `ق ل ب:B004/m01`
- Ayah anchors: `ح و ر` (84:14); `ق ل ب` (84:9); `خ ل و` (84:4)
- Synthesis: The denied return in 84:14 is lexically linked to reversal, outcome, and decline after a completed interval.

#### Subchannel E. Repair, Substitution, and Restored Condition
- Reading type: latent/lexical
- Scene or process: A damaged or unsuitable element is repaired or replaced so the whole can function again.
- Active motifs: repair `ص ل ح:B001/m01`; provision and repair `غ ي ر:B001/m01`; substitution `غ ي ر:B003/m01`; nurture and repair `ر ب ب:B002/m01`
- Ayah anchors: `ص ل ح` (84:25); `غ ي ر` (84:25); `ر ب ب` (84:2, 84:5, 84:6, 84:15)
- Synthesis: Change becomes restorative when alteration replaces a failed part or returns it to a sound condition.

#### Subchannel F. Delay, Detention, and Deferred Approach
- Reading type: latent/lexical
- Scene or process: An expected arrival is postponed while a person or process remains confined.
- Active motifs: delay or confinement `ق ر ء:B004/m02`; detention `ء ل ي:B013/m01`; absence of delay `ك ذ ب:B005/m01`; extended duration `م د د:B004/m01`
- Ayah anchors: `ق ر ء` (84:21); `ء ل ي` (84:6, 84:9); `ك ذ ب` (84:22); `م د د` (84:3)
- Synthesis: Temporal extension becomes institutionally or bodily consequential when approach is deferred and movement is held back.

#### Subchannel G. Termination, Death, and Burial
- Reading type: latent/lexical
- Scene or process: A life or process is cut off and the body is placed in a final bounded location.
- Active motifs: cutting or termination `م ن ن:B001/m01`; death and right-side burial `ي م ن:B007/m01`; grave `ك ف ر:B012/m02`; endpoint `ء ل ي:B001/m01`
- Ayah anchors: `م ن ن` (84:25); `ي م ن` (84:7); `ك ف ر` (84:22); `ء ل ي` (84:6, 84:9)
- Synthesis: The journey's endpoint has a bodily counterpart in death, ritual orientation, and burial.

#### Subchannel H. Forgetting, Discarding, and Leaving Behind
- Reading type: latent/lexical
- Scene or process: A once-held object, memory, or concern is cast behind and ceases to guide present action.
- Active motifs: forgetting or discarding `ظ ه ر:B012/m01`; beyond or behind `و ر ي:B006/m01`; indifference `ب ل ي:B009/m01`; casting off `ل ق ي:B005/m01`
- Ayah anchors: `ظ ه ر` (84:10); `و ر ي` (84:10); `ب ل ي` (84:15); `ل ق ي` (84:4, 84:6)
- Synthesis: Physical placement behind the body becomes a model for abandonment, forgetting, and indifference.

#### Subchannel I. Wear, Decay, and Material Deterioration
- Reading type: latent/lexical
- Scene or process: Time and exposure reduce a material's strength, surface, or usable form.
- Active motifs: wear and decay `ب ل ي:B001/m01`; decline `ح و ر:B005/m01`; husk or exhausted covering `ك ف ر:B010/m01`; defacement `ك د ح:B003/m01`
- Ayah anchors: `ب ل ي` (84:15); `ح و ر` (84:14); `ك ف ر` (84:22); `ك د ح` (84:6)
- Synthesis: Passage through successive states includes a material trajectory from intact form to worn and emptied residue.

#### Subchannel J. Persistence, Strength, and Survival
- Reading type: latent/lexical
- Scene or process: A subject continues through adversity by maintaining force and resisting collapse.
- Active motifs: persistence `ث ب ر:B004/m01`; strength `م ن ن:B002/m01`; functional soundness `ص ل ح:B003/m01`; power `ي م ن:B004/m01`
- Ayah anchors: `ث ب ر` (84:11); `م ن ن` (84:25); `ص ل ح` (84:25); `ي م ن` (84:7)
- Synthesis: Against ruin and decay stands a counterprocess of sustained force, fitness, and survival.

### 21. Emotion, Value, and Social Standing
- Semantic invariant: Persons and things are evaluated through joy, concern, honor, shame, purity, gratitude, wealth, weakness, and public reputation.
- Surface relation: direct; joy among one's people, concern-laden twilight, disbelief, good deeds, and reward establish an evaluative field across 84:9, 84:13, 84:16, and 84:22-25.
- Surprising reach: Nobility, boasting, excuse, carefree indifference, deceptive display, scantness, benefaction, and reproach form a nuanced social-affective system.

#### Subchannel A. Joy, Good News, and Successful Outcome
- Reading type: mixed
- Scene or process: Favorable news or achievement produces visible gladness and a sense of welfare.
- Active motifs: joy `س ر ر:B010/m01`; glad tidings `ب ش ر:B005/m01`; blessing `ي م ن:B001/m01`; ease and relief `ي س ر:B001/m01`; success and support `و ر ي:B003/m01`
- Ayah anchors: `س ر ر` (84:9, 84:13); `ب ش ر` (84:24); `ي م ن` (84:7); `ي س ر` (84:8); `و ر ي` (84:10)
- Synthesis: The surface joy of family life extends to the emotional result of welcome news, achieved ease, and successful support.

#### Subchannel B. Honor, Nobility, Purity, and Inner Worth
- Reading type: latent/lexical
- Scene or process: A person or substance is valued for inherited standing, refined quality, or an uncorrupted inner core.
- Active motifs: honor `ح س ب:B004/m01`; nobility `ع ذ ب:B008/m01`; inner essence `س ر ر:B005/m01`; core essence `ق ل ب:B002/m01`; worthiness `ء ه ل:B003/m01`
- Ayah anchors: `ح س ب` (84:8); `ع ذ ب` (84:24); `س ر ر` (84:9, 84:13); `ق ل ب` (84:9); `ء ه ل` (84:9, 84:13)
- Synthesis: Social honor and material purity share a valuation pattern centered on the quality of what lies within.

#### Subchannel C. Shame, Blame, and Restored Standing
- Reading type: latent/lexical
- Scene or process: Public discredit attaches to a person and can later be removed through vindication or release.
- Active motifs: freedom from blame `خ ل و:B005/m01`; removal of shame `ظ ه ر:B013/m01`; release `م ن ن:B004/m01`; established truth `ح ق ق:B005/m01`
- Ayah anchors: `خ ل و` (84:4); `ظ ه ر` (84:10); `م ن ن` (84:25); `ح ق ق` (84:2, 84:5)
- Synthesis: Social restoration occurs when truth becomes visible and the burden of blame is formally severed.

#### Subchannel D. Praise, Reputation, and Boasting
- Reading type: latent/lexical
- Scene or process: A good name circulates publicly and may be cultivated into exaggerated self-display.
- Active motifs: reputation `س م و:B008/m01`; good reputation `ص ل ح:B004/m01`; boasting `ظ ه ر:B024/m01`; elevated standing `س م و:B002/m01`
- Ayah anchors: `س م و` (84:1); `ص ل ح` (84:25); `ظ ه ر` (84:10)
- Synthesis: Public elevation ranges from deserved good repute to performative boasting.

#### Subchannel E. Concern, Caution, and Protective Care
- Reading type: mixed
- Scene or process: Awareness of possible harm produces solicitude, vigilance, and protective preparation.
- Active motifs: concern `ش ف ق:B003/m01`; safety `ء م ن:B001/m01`; precaution `ظ ه ر:B021/m01`; protected charge `ح ق ق:B007/m01`
- Ayah anchors: `ش ف ق` (84:16); `ء م ن` (84:20, 84:25); `ظ ه ر` (84:10); `ح ق ق` (84:2, 84:5)
- Synthesis: The emotional coloring of twilight opens into a practical ethic of concern for vulnerable persons and outcomes.

#### Subchannel F. Indifference, Slackness, and Carefree Release
- Reading type: latent/lexical
- Scene or process: A person relaxes effort or concern, ranging from legitimate freedom from burden to negligent indifference.
- Active motifs: indifference `ب ل ي:B009/m01`; slackness `ء ل ي:B008/m01`; carefree state `خ ل و:B007/m01`; forgetting `ظ ه ر:B012/m01`
- Ayah anchors: `ب ل ي` (84:15); `ء ل ي` (84:6, 84:9); `خ ل و` (84:4); `ظ ه ر` (84:10)
- Synthesis: Release from constraint can become morally ambiguous when ease passes into disregard and forgetting.

#### Subchannel G. Weakness, Strength, and Social Power
- Reading type: latent/lexical
- Scene or process: A subject's capacity is evaluated on a scale from frailty to effective power.
- Active motifs: weakness `ظ ن ن:B008/m01`; strength `م ن ن:B002/m01`; power `ي م ن:B004/m01`; elevation `س م و:B002/m01`
- Ayah anchors: `ظ ن ن` (84:14); `م ن ن` (84:25); `ي م ن` (84:7); `س م و` (84:1)
- Synthesis: Physical capacity and social standing reinforce one another through the evaluative contrast of weakness and power.

#### Subchannel H. Deception, Ridicule, and False Display
- Reading type: latent/lexical
- Scene or process: A person manipulates appearances, mocks another, or presents an unreliable surface.
- Active motifs: deceptive self-presentation `ك ذ ب:B008/m01`; deceptive familiarity `خ ل و:B015/m01`; mocking attribution `ك ف ر:B006/m01`; gambling deception `ق م ر:B007/m01`
- Ayah anchors: `ك ذ ب` (84:22); `خ ل و` (84:4); `ك ف ر` (84:22); `ق م ر` (84:18)
- Synthesis: Falsehood can be embodied socially as a misleading persona, manipulative intimacy, or contemptuous public labeling.

#### Subchannel I. Gratitude, Ingratitude, Favor, and Reproach
- Reading type: latent/lexical
- Scene or process: A received benefit elicits gratitude or denial, while the giver may convert generosity into reproach.
- Active motifs: ingratitude `ك ف ر:B004/m01`; benefaction `م ن ن:B003/m01`; reproach for favor `م ن ن:B003/m02`; favors `ء ل ي:B006/m01`; benefaction under trial `ب ل ي:B003/m01`
- Ayah anchors: `ك ف ر` (84:22); `م ن ن` (84:25); `ء ل ي` (84:6, 84:9); `ب ل ي` (84:15)
- Synthesis: Value exchange becomes moral evaluation through the recipient's gratitude and the giver's restraint from humiliating reminder.

#### Subchannel J. Wealth, Scarcity, and Generous Capacity
- Reading type: latent/lexical
- Scene or process: Material means range from scant reserve to surplus capable of supporting others.
- Active motifs: wealth `ي س ر:B003/m01`; little or scarcity `ي س ر:B002/m01`; surplus `ظ ه ر:B023/m01`; gift `ء ل ي:B012/m01`; scantness `ش ف ق:B001/m01`
- Ayah anchors: `ي س ر` (84:8); `ظ ه ر` (84:10); `ء ل ي` (84:6, 84:9); `ش ف ق` (84:16)
- Synthesis: Ease and generosity depend on a material threshold separating insufficiency from distributable surplus.

#### Subchannel K. Fitness, Worthiness, and Moral Eligibility
- Reading type: latent/lexical
- Scene or process: A person, place, or action is judged suitable for a valued role.
- Active motifs: worthiness `ء ه ل:B003/m01`; fitness `ص ل ح:B003/m01`; fitness for good `ء ر ض:B003/m01`; verified rightness `ح ق ق:B005/m01`
- Ayah anchors: `ء ه ل` (84:9, 84:13); `ص ل ح` (84:25); `ء ر ض` (84:3); `ح ق ق` (84:2, 84:5)
- Synthesis: Evaluation reaches beyond beauty or status to the practical and moral question of eligibility.

#### Subchannel L. Excuse, Reproach, and Accountable Blame
- Reading type: latent/lexical
- Scene or process: A subject offers an excuse against blame while another party assesses whether reproach remains justified.
- Active motifs: excuse `ب ل ي:B004/m01`; freedom from blame `خ ل و:B005/m01`; reproach `م ن ن:B003/m02`; reckoning `ح س ب:B001/m01`
- Ayah anchors: `ب ل ي` (84:15); `خ ل و` (84:4); `م ن ن` (84:25); `ح س ب` (84:8)
- Synthesis: Accountability is socially negotiated through explanation, judgment, and the possible removal or confirmation of blame.

### 22. Existence, Place, and Logical Relation
- Semantic invariant: Events and entities are located by occurrence, state, proximity, absence, boundary, duration, necessity, contrast, and affirmation.
- Surface relation: direct; coming, being, return, endpoint, exception, affirmation, and state succession are grammatically and lexically active throughout S084.
- Surprising reach: No-caller absence, middle versus outskirts, behindness, outer-inner completeness, inevitable confinement, and truth-affirming contrast form an abstract relational system.

#### Subchannel A. Occurrence, Coming, and Event
- Reading type: mixed
- Scene or process: A previously unrealized event comes into being and enters the experienced world.
- Active motifs: existence or occurrence `ك و ن:B001/m01`; coming event `ء ت ي:B001/m01`; vicissitude `د ع و:B006/m01`; encounter `ل ق ي:B004/m01`
- Ayah anchors: `ك و ن` (84:13, 84:15); `ء ت ي` (84:7, 84:10); `د ع و` (84:11); `ل ق ي` (84:4, 84:6)
- Synthesis: Being is dynamically presented as what comes, happens, and is finally encountered.

#### Subchannel B. Place, Status, and Proximity
- Reading type: latent/lexical
- Scene or process: An entity occupies a location or rank defined relative to a nearby point.
- Active motifs: place or status `ك و ن:B002/m01`; proximity `ء ل ي:B002/m01`; likely place `ظ ن ن:B002/m01`; destination or outcome-place `ق ل ب:B005/m01`
- Ayah anchors: `ك و ن` (84:13, 84:15); `ء ل ي` (84:6, 84:9); `ظ ن ن` (84:14); `ق ل ب` (84:9)
- Synthesis: Existential state is inseparable from relational position, whether spatially near or socially ranked.

#### Subchannel C. Emptiness, Absence, and No Caller
- Reading type: mixed
- Scene or process: A container, place, or social field is emptied until no occupant or responding voice remains.
- Active motifs: emptiness `خ ل و:B001/m01`; no caller `د ع و:B008/m01`; uninhabited place `ء ه ل:B004/m01`; emptied contents `ل ق ي:B005/m01`
- Ayah anchors: `خ ل و` (84:4); `د ع و` (84:11); `ء ه ل` (84:9, 84:13); `ل ق ي` (84:4, 84:6)
- Synthesis: The earth's emptying extends from material contents to the existential absence of inhabitant, responder, or social presence.

#### Subchannel D. Otherness, Exception, and Set Boundary
- Reading type: mixed
- Scene or process: A member is distinguished from a set by being other than, outside, or exempted from its general rule.
- Active motifs: otherness or exception `غ ي ر:B005/m01`; exception `خ ل و:B004/m01`; contrast particle `ب ل ل:B008/m01`; divided class `ط ب ق:B005/m01`
- Ayah anchors: `غ ي ر` (84:25); `خ ل و` (84:4); `ب ل ل` (84:22); `ط ب ق` (84:19)
- Synthesis: The closing exception for the faithful belongs to a broader logic of set membership and boundary marking.

#### Subchannel E. Phase, Condition, and Successive State
- Reading type: surface-primary
- Scene or process: An entity occupies one condition, crosses a threshold, and enters another.
- Active motifs: state or phase `ط ب ق:B004/m01`; condition `ك و ن:B006/m01`; extended interval `م د د:B004/m01`; return or change `ح و ر:B005/m01`
- Ayah anchors: `ط ب ق` (84:19); `ك و ن` (84:13, 84:15); `م د د` (84:3); `ح و ر` (84:14)
- Synthesis: Layer after layer is simultaneously spatial succession and passage through changing existential conditions.

#### Subchannel F. Necessity, Inevitability, and Constrained Outcome
- Reading type: latent/lexical
- Scene or process: Circumstances close around an agent until only one required outcome remains.
- Active motifs: necessity `و ع ي:B006/m01`; obligatory exhortation `ك ذ ب:B003/m01`; binding duty `ح ق ق:B002/m01`; constraining enclosure `ط ب ق:B009/m01`
- Ayah anchors: `و ع ي` (84:23); `ك ذ ب` (84:22); `ح ق ق` (84:2, 84:5); `ط ب ق` (84:19)
- Synthesis: Fulfillment is framed not merely as prediction but as a constrained state in which obligation and outcome coincide.

#### Subchannel G. Limit, Endpoint, and Duration
- Reading type: mixed
- Scene or process: A process extends for a bounded span and terminates at a defined endpoint.
- Active motifs: endpoint `ء ل ي:B001/m01`; duration `م د د:B004/m01`; termination `م ن ن:B001/m01`; time portion `ط ب ق:B010/m01`
- Ayah anchors: `ء ل ي` (84:6, 84:9); `م د د` (84:3); `م ن ن` (84:25); `ط ب ق` (84:19)
- Synthesis: Striving toward the Lord combines direction and duration within a process whose end is fixed.

#### Subchannel H. Affirmation, Contrast, and Established Reality
- Reading type: mixed
- Scene or process: A prior denial is reversed or corrected through emphatic affirmation of what is real.
- Active motifs: affirmative response `ب ل ي:B010/m01`; contrast correction `ب ل ل:B008/m01`; truth and reality `ح ق ق:B001/m01`; certainty `ظ ن ن:B001/m01`
- Ayah anchors: `ب ل ي` (84:15); `ب ل ل` (84:22); `ح ق ق` (84:2, 84:5); `ظ ن ن` (84:14)
- Synthesis: The surah's corrective particles and truth vocabulary jointly move discourse from denial or supposition to established reality.

#### Subchannel I. Interior, Middle, Surface, and Complete Boundary
- Reading type: latent/lexical
- Scene or process: An entity is mapped from inner core through middle region to outer surface as a bounded whole.
- Active motifs: outer-inner completeness `ب ش ر:B008/m01`; midst `ظ ه ر:B017/m01`; surface `ب ش ر:B001/m01`; inner essence `ق ل ب:B002/m01`
- Ayah anchors: `ب ش ر` (84:24); `ظ ه ر` (84:10); `ق ل ب` (84:9)
- Synthesis: Spatial relation becomes mereological, defining a whole through coordinated interior, middle, and exterior zones.

#### Subchannel J. Behind, Outskirts, and Outer Route
- Reading type: latent/lexical
- Scene or process: A point is located beyond the central field, behind the observer, or along an exterior road.
- Active motifs: beyond or behind `و ر ي:B006/m01`; outskirts or outer road `ظ ه ر:B015/m01`; back `ظ ه ر:B002/m01`; remote place `ك ف ر:B012/m01`
- Ayah anchors: `و ر ي` (84:10); `ظ ه ر` (84:10); `ك ف ر` (84:22)
- Synthesis: Marginality is spatially represented by what lies behind the body or outside the inhabited center.

## Standalone Subchannels

### S1. Image-Bearing Coinage
- Reading type: latent/lexical
- Scene or process: A coin carries a representational image that makes the object recognizable as marked currency.
- Active motifs: image-bearing coin `س ج د:B006/m01`
- Ayah anchors: `س ج د` (84:21)
- Synthesis: The prostration root preserves a compact numismatic scene in which an impressed image identifies an exchange object.

### S2. Riddle and Puzzle
- Reading type: latent/lexical
- Scene or process: A speaker encodes a referent in an indirect verbal challenge that another person must solve.
- Active motifs: riddle `د ع و:B007/m01`; inference under uncertainty `ظ ن ن:B003/m01`; learned method `ق ر ء:B011/m01`
- Ayah anchors: `د ع و` (84:11); `ظ ن ن` (84:14); `ق ر ء` (84:21)
- Synthesis: Calling becomes an oblique invitation to infer a concealed answer rather than a direct summons.

### S3. Curse and Imprecation
- Reading type: latent/lexical
- Scene or process: A speaker calls for pain, ruin, or punishment to befall a target.
- Active motifs: curse `د ع و:B004/m01`; painful infliction `ء ل م:B002/m01`; punishment `ع ذ ب:B005/m01`; ruin `ث ب ر:B002/m01`
- Ayah anchors: `د ع و` (84:11); `ء ل م` (84:24); `ع ذ ب` (84:24); `ث ب ر` (84:11)
- Synthesis: The destructive call is a self-contained speech act whose requested outcome is suffering or ruin.

### S4. Pale Stone Marker
- Reading type: latent/lexical
- Scene or process: A distinctively pale stone serves as a visible natural landmark or identifying marker.
- Active motifs: pale stone `ب ص ر:B007/m01`; sign or landmark `ع ل م:B002/m01`; distinguishing facet `ش ف ق:B005/m01`; earth surface `ء ر ض:B001/m01`
- Ayah anchors: `ب ص ر` (84:15); `ع ل م` (84:23); `ش ف ق` (84:16); `ء ر ض` (84:3)
- Synthesis: Color, facet, and terrain converge in a compact landmark scene not reducible to the larger anatomical or architectural channels.


