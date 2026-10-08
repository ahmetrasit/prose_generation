Surah: 85. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S85 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s085/surah.r2/text.md =====
# Surah 85

- 85:1 وَٱلسَّمَآءِ ذَاتِ ٱلْبُرُوجِ
- 85:2 وَٱلْيَوْمِ ٱلْمَوْعُودِ
- 85:3 وَشَاهِدٍۢ وَمَشْهُودٍۢ
- 85:4 قُتِلَ أَصْحَٰبُ ٱلْأُخْدُودِ
- 85:5 ٱلنَّارِ ذَاتِ ٱلْوَقُودِ
- 85:6 إِذْ هُمْ عَلَيْهَا قُعُودٌۭ
- 85:7 وَهُمْ عَلَىٰ مَا يَفْعَلُونَ بِٱلْمُؤْمِنِينَ شُهُودٌۭ
- 85:8 وَمَا نَقَمُوا۟ مِنْهُمْ إِلَّآ أَن يُؤْمِنُوا۟ بِٱللَّهِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- 85:9 ٱلَّذِى لَهُۥ مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ ۚ وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ شَهِيدٌ
- 85:10 إِنَّ ٱلَّذِينَ فَتَنُوا۟ ٱلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ ثُمَّ لَمْ يَتُوبُوا۟ فَلَهُمْ عَذَابُ جَهَنَّمَ وَلَهُمْ عَذَابُ ٱلْحَرِيقِ
- 85:11 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَهُمْ جَنَّٰتٌۭ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْكَبِيرُ
- 85:12 إِنَّ بَطْشَ رَبِّكَ لَشَدِيدٌ
- 85:13 إِنَّهُۥ هُوَ يُبْدِئُ وَيُعِيدُ
- 85:14 وَهُوَ ٱلْغَفُورُ ٱلْوَدُودُ
- 85:15 ذُو ٱلْعَرْشِ ٱلْمَجِيدُ
- 85:16 فَعَّالٌۭ لِّمَا يُرِيدُ
- 85:17 هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ
- 85:18 فِرْعَوْنَ وَثَمُودَ
- 85:19 بَلِ ٱلَّذِينَ كَفَرُوا۟ فِى تَكْذِيبٍۢ
- 85:20 وَٱللَّهُ مِن وَرَآئِهِم مُّحِيطٌۢ
- 85:21 بَلْ هُوَ قُرْءَانٌۭ مَّجِيدٌۭ
- 85:22 فِى لَوْحٍۢ مَّحْفُوظٍۭ


===== _commentary/v16/work/s085/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م و (root_000745): 85:1 وَٱلسَّمَآءِ, 85:9 ٱلسَّمَٰوَٰتِ

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

## ECHO و س م (root_001650): for 85:1 وَٱلسَّمَآءِ, 85:9 ٱلسَّمَٰوَٰتِ: withheld observed target; not identity

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

## ب ر ج (root_000101): 85:1 ٱلْبُرُوجِ

- **B001** sur kulesi, hisar veya saray — sur kulesi, hisar veya saray · sağlam yapılmış hisarlar veya saraylar
  أصل البروج الحصون والقصور (maqayis)؛ بروج سور المدينة والحصن بيوت تبنى على السور (ayn;tahdhib)؛ البرج من بروج الحصن أو القصر (jamhara)؛ برج الحصن ركنه وربما سمي الحصن به (sihah)؛ البروج القصور الواحد برج (mufradat)
- **B002** göğün on iki bölümlük göksel konakları — göğün bölümleri veya göksel konaklar · gök çemberinin on iki bölümü · yıldızlara veya göksel konaklara sahip gökyüzü
  البرج واحد بروج السماء (maqayis;sihah)؛ البرج واحد من بروج الفلك وهو اثنا عشر برجا (ayn;tahdhib)؛ البرج من بروج السماء (jamhara)؛ ذات البروج ذات الكواكب أو ذات القصور في السماء (tahdhib)؛ سمي بروج السماء لمنازلها المختصة بها (mufradat)
- **B003** kadının güzellik ve süsünü sergilemesi — kadının güzellik ve süsünü sergilemesi · kadın güzelliklerini gösterdi · süslerini sergileyen kadınlar
  التبرج إظهار المرأة محاسنها (maqayis;jamhara;sihah)؛ إذا أبدت المرأة محاسن جيدها ووجهها قيل تبرجت (ayn;tahdhib)؛ إظهار الزينة وما يستدعى به شهوة الرجل (tahdhib)؛ تبرجت المرأة تشبهت به في إظهار المحاسن أو ظهرت من برجها (mufradat)
- **B004** geniş, akı ve karası belirgin güzel göz — gözün geniş, güzel, akı ve karası belirgin olması · geniş ve renk karşıtlığı belirgin gözlü · gözün güzel bakışı ve genişliği
  البرج سعة العين في شدة سواد سوادها وشدة بياض بياضها (maqayis)؛ سعة بياض العين مع حسن الحدقة (ayn;tahdhib)؛ نقاء بياض العين وصفاء سوادها (jamhara)؛ بياض العين محدقا بالسواد كله (sihah;tahdhib)؛ سعة العين وحسنها (mufradat)
- **B005** kule desenli özel dokuma veya giysi [kalıp] — kule benzeri resimlerle bezeli özel giysi
  ثوب مبرج إذا كان عليه صور البروج (maqayis)؛ ثوب مبرج صور فيه تصاوير كبروج السور (ayn)؛ ثوب مبرج للمعين من الحلل (sihah)؛ ثوب مبرج قد صورت فيه تصاوير كبروج السور (tahdhib)؛ ثوب مبرج صورت عليه بروج واعتبر حسنه (mufradat)
- **B006** çarpım ve karesel kök hesabı — çarpım ve karesel kök hesabı
  حساب البرجان ما جداء كذا في كذا وما جذر كذا وكذا (ayn)؛ جداؤه مبلغه وجذره أصله الذي يضرب بعضه في بعض وجملته البرجان (tahdhib)
- **B007** büyük savaş gemisi — büyük savaş gemisi veya büyük savaş gemileri
  البارجة سفينة من سفن البحر تتخذ للقتال (ayn;tahdhib)؛ البوارج السفن الكبار واحدتها بارجة (tahdhib)
- **B008** Romalılardan bir topluluğun adı — Romalılardan bir topluluğun adı
  برجان جنس من الروم ويسمون كذلك (tahdhib)
- **B009** yeme içmede bolluğa kavuşmak — yeme içmede bolluğa kavuştu
  برج الرجل إذا اتسع أمره في الأكل والشرب (tahdhib)
- **B010** yakışıklı ve seçkin erkek — yakışıklı oğulları oldu · yakışıklı ve seçkin erkek
  أبرج الرجل إذا جاء ببنين ملاح (tahdhib)؛ البارج الملاح الفاره (tahdhib)
- **B011** yayık — yayık
  الإبريج الممخضة (sihah)
- **B012** atasözünde aşırı hırsızlığın örneği olan kişi — atasözünde anılan bir hırsızın adı · ondan bile daha hırsız
  برجان اسم لص يقال أسرق من برجان (sihah)

## ي و م (root_001700): 85:2 وَٱلْيَوْمِ

- **B001** güneşin doğuşundan batışına kadarki gün — güneşin doğuşundan batışına kadarki gün · bu anlamdaki günlerin çoğulu · gün gün veya gündelik esasa göre yapılan işlem
  اليوم: الواحد من الأيام (maqayis)؛ اليوم مقداره من طلوع الشمس إلى غروبها (ayn;tahdhib)؛ اليوم معروف والجمع أيام (sihah)؛ اليوم يعبر به عن وقت طلوع الشمس إلى غروبها (mufradat)
- **B002** herhangi bir zaman dilimi; bağlama göre devir — herhangi bir zaman dilimi; bağlama göre devir · iki devri veya bollukla sıkıntı, cömertlikle savaş gibi iki karşıt hali
  مدة من الزمان أي مدة كانت (mufradat)؛ اليوم ها هنا بمعنى الدهر (tahdhib)؛ شر أيام دهرها (tahdhib)
- **B003** büyük olayın yaşandığı çetin gün veya olay — büyük olay, olayın gerçekleştiği kritik gün veya çetin gün · çok çetin gün veya savaş günü · bilinen günlerde gerçekleşmiş olaylar · çok çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün · kötülüğü insanlar üzerinde uzun süren çetin gün
  يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)؛ اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت (ayn;tahdhib)؛ الشدة باليوم (sihah)؛ اليوم الشديد: يوم ذو أيام (ayn;tahdhib)؛ الأيام في معنى الوقائع (tahdhib)
- **B004** Tanrı'nın nimet ve ibret verici işleriyle anılan günler [kalıp] — Tanrı'nın nimet, bağışlama ve cezalandırma olaylarıyla anılan günleri
  وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب، وبالعفو عن آخرين (tahdhib)؛ جاءت الأيام بمعنى الوقائع والنعم (tahdhib)؛ أيامه: نعمه (tahdhib)؛ إضافة الأيام إلى الله تشريف لأمرها لما أفاض الله عليهم من نعمه فيها (mufradat)
- **B005** bağlamda işaret edilen o gün veya o sırada — o gün; o sırada
  يركب يوم مع إذ، فيقال: يومئذ؛ وربما يعرب ويبنى، وإذا بني فللإضافة إلى إذ (mufradat)

## و ع د (root_001662): 85:2 ٱلْمَوْعُودِ

- **B001** iyi ya da kötü bir şeyi yapacağını sözle bildirme — iyi ya da kötü bir şeyi yapacağını bildirme; verilen söz · ona iyi ya da kötü bir şeyi yapacağını bildirdi · verilen söz; söz verme · verilmiş söz · söz verme; verilen söz · ona iyilik yapacağını bildirdi
  تدل على ترجية بقول ويكون ذلك بخير وشر (maqayis)؛ الوعد والعدة يكونان مصدرا واسما (ayn;tahdhib)؛ الوعد يستعمل في الخير والشر (sihah)؛ الوعد يكون في الخير والشر (mufradat)
- **B002** kötülük yapacağını söyleyerek gözdağı verme — kötülük yapacağını bildirerek korkutma · zarar vereceğini bildirerek gözdağı verme · ona kötülük ya da dayakla gözdağı verdi · gözdağı verme
  فأما الوعيد فلا يكون إلا بشر (maqayis)؛ الوعيد من التهدد أوعدته ضربا (ayn)؛ في الشر الإيعاد والوعيد والتوعد التهدد (sihah)؛ إذا أدخلوا الباء لم يكن إلا في الشر كقولك أوعدته بالضرب (tahdhib)؛ الوعيد في الشر خاصة (mufradat)
- **B003** bir söz için belirlenmiş zaman ya da yer — söz için kararlaştırılan zaman ya da yer · sözleşilen zaman ya da yer · gerçekleşeceği önceden bildirilen belirli gün
  الموعد موضع التواعد وهو الميعاد والميعاد لا يكون إلا وقتا أو موضعا (ayn)؛ الميعاد المواعدة والوقت والموضع وكذلك الموعد (sihah)؛ يكون الموعد وقتا للعدة والميعاد لا يكون إلا وقتا أو موضعا (tahdhib)؛ فاجعل بيننا وبينك موعدا وقل لكم ميعاد يوم (mufradat)
- **B004** karşılıklı söz verme — karşılıklı söz verme; buluşmak üzere anlaşma · karşılıklı söz verme · onunla karşılıklı sözleştim · topluluk birbirine söz verdi
  والمواعدة من الميعاد (maqayis)؛ موضع التواعد (ayn)؛ تواعد القوم أي وعد بعضهم بعضا (sihah)؛ واعدت فلانا إذا وعدته ووعدني (tahdhib)؛ واعدته وتواعدنا (mufradat)
- **B005** erkek hayvanın saldırı öncesi kükremesi [kalıp] — erkek hayvanın saldırı öncesi kükremesi
  وعيد الفحل هديره إذا هم أن يصول (maqayis)؛ وعيد الفحل إذا هم أن يصول (ayn)؛ وعيد الفحل هديره إذا هم أن يصول (sihah)
- **B006** belirtileri gelecekteki bir durumu bekleten — belirtileri ilerideki durumu umduran · yağmur ve bitki bakımından umut veren toprak · başlangıcı sıcak ya da soğuk olacağını gösteren gün · iyiliği ve gelişmesi umulan hayvan ya da sürü · belirtileri cömertlik ve sağlam huy bekleten
  أرض بني فلان واعدة إذا رجي خيرها من المطر والإعشاب ويوم واعد (maqayis)؛ يوم واعد إذا وعد أوله بحر أو برد وأرض واعدة إذا رجي خيرها من النبت (sihah)؛ أرض واعدة إذا رجي خيرها ويقال للدابة والماشية واعد ويومنا يعد بردا وهذا غلام تعد مخايله كرما (tahdhib)

## ECHO ع د د (root_000989): for 85:2 ٱلْمَوْعُودِ, 85:13 وَيُعِيدُ: withheld observed target; not identity

- **B001** sayma, sayı ve sayıya göre bir topluluğa katma — bir şeyi sayıp miktarını belirlemek · sayı; sayılanın miktarı · sayıca çokluk · sayılmış veya sayıyla sınırlandırılmış · iyiler arasında sayılmak · az ya da çok sayıda topluluk · sayıları on bini aşmak
  عددت الشيء عدا أي أحصيته (maqayis;ayn;sihah;tahdhib)؛ العدد مقدار ما يعد (maqayis)؛ العديد الكثرة (maqayis;ayn;sihah;tahdhib)؛ فلان في عداد الصالحين (maqayis;ayn;sihah)؛ العدد آحاد مركبة (mufradat)
- **B002** gelecekteki bir iş için hazırlama ve hazır bulundurma — bir şeyi ilerideki iş için hazırlamak · ilerideki ihtiyaç için hazırlanmış mal, silah veya gereç · bir işe hazırlanmak ve donanmak
  أعددت الشيء إعدادا (maqayis)؛ أعددت الشيء هيأته (ayn)؛ العدة من السلاح ما اعتددته (jamhara)؛ أعده لأمر كذا هيأه له (sihah)؛ العدة ما أعد لأمر يحدث مثل الأهبة (tahdhib)؛ أعددت هذا لك أي جعلته بحيث تعده وتتناوله (mufradat)
- **B003** sayılı zaman dilimi ve bağlama bağlı bekleme ya da tamamlama süresi — kadının yeniden evlenmeden önce beklemesi gereken süre · kaçırılan günler kadar başka günlerde yerine getirmek · sayılı ve belirli günler
  عدة المرأة أيام قروئها (ayn)؛ عدة المرأة معروفة (jamhara)؛ عدة المرأة أيام أقرائها (sihah)؛ العدة عدة المرأة شهورا كانت أو أقراء أو وضع حمل (tahdhib)؛ فعدة من أيام أخر أي عليه أيام بعدد ما فاته (mufradat)؛ الأيام المعدودات أيام التشريق (sihah;tahdhib;mufradat)
- **B004** kaynağı kesilmeyen kalıcı su ve su yeri — eskiden beri var olan, tükenmeyen sürekli su · sürekli sular veya kalıcı su yerleri · köklü ve eski saygınlık
  العد مجتمع الماء وجمعه أعداد (maqayis;ayn)؛ العد من الماء القديم الذي لا ينتزح (jamhara)؛ العد بالكسر الماء الذي له مادة لا تنقطع (sihah)؛ الماء العد الدائم الذي لا انقطاع له (tahdhib)؛ ماء عد (mufradat)
- **B005** belirli zaman ve bilinen aralıklarla geri gelme — sokulma ağrısının belirli aralıklarla alevlenmesi · bana belirli zamanlarda yeniden baş göstermek · zaman, dönem veya en parlak çağ · yayın tekrarlanan titreşimi veya sesi · ayda bir gerçekleşen buluşma · dağıtım, yoklama veya geçici toplanma günü · belirli aralıklarla gelen akıl bulanıklığı
  العداد اهتياج وجع اللديغ (maqayis;ayn;sihah)؛ العداد الشيء الذي يأتيك لوقت (tahdhib)؛ عدان الشيء عهده وزمانه (mufradat)؛ كان ذلك في عدان شبابه (ayn;sihah;tahdhib)؛ عداد القوس أن تنبض بها ساعة بعد ساعة (maqayis)؛ عداد القوس صوتها (sihah;tahdhib)؛ يوم العداد يوم العطاء (maqayis;tahdhib)
- **B006** karşılıklı paydaşlık, pay ve denk sayılma — mal veya değer bakımından karşılıklı paydaş olmak · paylar, denkler veya mirastaki karşılıklı paydaşlar · onun dengi ve karşılığı
  هم يتعادون إذا اشتركوا فيما يعدد به بعضهم على بعض (ayn;tahdhib)؛ العدائد النظراء (tahdhib)؛ العدائد الحصص (tahdhib)؛ من يعاده في الميراث (sihah)؛ فلان عد فلان أي قرنه (tahdhib)

## ECHO ع و م (root_001063): for 85:2 ٱلْمَوْعُودِ: withheld observed target; not identity

- **B001** yüzme ve yüzmeye benzer akıcı ilerleme — suda yüzme · yüzüyormuş gibi akıcı ilerlemek · yüzer gibi akıcı koşan at · suda yüzen küçük canlı · güneşin gök kuşağındaki bölümler boyunca yüzüyormuş gibi ilerlemesi
  العوم السباحة (ayn;sihah;mufradat)؛ السفينة والإبل والنجوم تعوم في سيرها (ayn)؛ سير الإبل والسفينة عوم (sihah)؛ فرس عوام يعوم في جريه (ayn)؛ العوام الفرس السابح في جريه (sihah)؛ العومة دويبة صغيرة تسبح في الماء (sihah)
- **B002** bir kış ve bir yazı kapsayan yıl — yıl; bir kış ve bir yazı kapsayan yıllık çevrim; özellikle bolluk ve verimlilik dönemi için kullanılan yıl sözü · nice yıllar; pekiştirilmiş çoğul yıl ifadesi
  العام حول يأتي على شتوة وصيفة (ayn)؛ العام السنة (sihah)؛ سنون عوم (sihah)؛ العام كالسنة (mufradat)
- **B003** üzerinden bir yıl geçmiş — üzerinden bir yıl geçmiş; bir yıllık eski
  رسم عامي أو حولي أتى عليه عام (ayn)؛ نبت عامي أي يابس أتى عليه عام (sihah)
- **B004** bir yıl ürün verip bir yıl vermeme [kalıp] — hurma ağacının bir yıl ürün verip ertesi yıl vermemesi
  عاومت النخلة أي حملت سنة ولم تحمل سنة
- **B005** yıllara göre işlem yapma — yıllara göre işlem yapma · ekin veya ağaç ürününü iki ya da üç yıl için satmaya dayalı yasak işlem
  عامله معاومة كما تقول مشاهرة؛ المعاومة المنهي عنها أن تبيع زرع عامك أو ثمر نخلك أو شجرك لعامين أو ثلاثة
- **B006** dallardan yapılmış geçiş salı — dallar ve benzeri malzemelerden yapılmış geçiş salı
  العامة تتخذ من أغصان الشجر ونحوه تعبر عليها الأنهار كعبور السفن (ayn)؛ العامة أيضا الطوف الذي يركب في الماء (sihah)
- **B007** uzaktan görünen binici başı — açık arazide uzaktan görünen binici başı · açık arazide uzaktan görünen binici başı · sarığıyla görünen binici başı; sarığın baş çevresindeki kıvrımı
  العام والعومة والعامة هامة الراكب إذا بدا لك رأسه في الصحراء (ayn)؛ لا يسمى رأسه عامة حتى ترى عمامة عليه (ayn)؛ العامة كور العمامة (sihah)
- **B008** en seçkin olanı seçip ayırma — bir kimsenin malının en iyisini seçip ayırma · bir kişiyi veya malının en iyisini seçip ayırmak · ölüm canları seçip alır
  الاعتيام اصطفاء خيار مال الرجل؛ اعتمت أفضل ماله؛ الموت يعتام النفوس
- **B009** biçilmiş ürünü avuç avuç yığma — biçilmiş ürünü avuç avuç koyup biriktirme · avuç avuç biriktirilmiş hasat yığını
  التعويم وضع الحصد قبضة قبضة فإذا اجتمع فهي عامة والجمع عام
- **B010** yıllar arasındaki bir vakitte karşılaşma [kalıp] — yıllar arasındaki bir vakitte karşılaşma
  لقيته ذات العويم وذلك إذا لقيته بين الأعوام

## ش ه د (root_000822): 85:3 وَشَاهِدٍ, 85:3 وَمَشْهُودٍ, 85:7 شُهُودٌ, 85:9 شَهِيدٌ

- **B001** hazır bulunup görme — hazır bulunmak ve bizzat görmek · görerek hazır bulunma · bizzat görme ve gözle karşılaşma · insanların bulunduğu veya toplandığı yer · hac törenlerinin yapıldığı yerler · eşi yanında bulunan kadın
  أصل يدل على حضور (maqayis)؛ شهده شهودا أي حضره (sihah)؛ الشهود والشهادة الحضور مع المشاهدة (mufradat)؛ المشهد مجمع الناس (ayn;tahdhib)؛ امرأة مشهد إذا حضر زوجها (maqayis;sihah;mufradat;tahdhib)
- **B002** bilgiye dayalı tanıklık — bilgiye dayalı kesin tanıklık sözü · bildiğini tanık olarak açıklamak · tanıklık eden kişi · tanık olan veya başkası hakkında tanıklık eden kişi · birinden tanıklık etmesini istemek · birini bir konuda tanık kılmak · ilahi nitelik olarak güvenilir tanık veya bilgisine hiçbir şey uzak kalmayan
  الشهادة يجمع الحضور والعلم والإعلام (maqayis)؛ الشهادة خبر قاطع (sihah)؛ شهد فلان بحق فهو شاهد وشهيد (tahdhib)؛ الشهادة قول صادر عن علم (mufradat)؛ شهد علي فلان بكذا شهادة وهو شاهد وشهيد (ayn)
- **B003** tanıklık bildirme sözü — tanıklık sözüyle yemin etmek veya bildirmek · namazda okunan tanıklık ve selamlama bölümü
  التشهد في الصلاة من قولك أشهد (ayn)؛ قولهم أشهد بكذا أي احلف (sihah)؛ أشهد أن لا إله إلا الله وأبين (tahdhib)؛ التشهد هو أن يقول أشهد أن لا إله إلا الله (mufradat)
- **B004** Tanrı yolunda öldürülen kişi — Tanrı yolunda öldürülen veya ölüm anında bulunan kişi · bu özel ölüm statüsüyle ölmek
  الشهيد القتيل في سبيل الله (maqayis;sihah)؛ استشهد فلان فهو شهيد (ayn;sihah;tahdhib)؛ الشهيد هو المحتضر (mufradat)؛ الشهيد الحي (tahdhib)
- **B005** ifade eden dil — dil veya sahibini belli eden ifade · ne görünüşü ne de dili var
  الشاهد اللسان (maqayis;sihah;tahdhib)؛ ما لفلان رواء ولا شاهد أي ماله منظر ولا لسان (tahdhib)؛ لفلان شاهد حسن أي عبارة جميلة (tahdhib)
- **B006** doğum ve erginlik belirtisi — doğumda çocuğun başıyla ya da çocukla birlikte çıkan şey · devenin doğurduğu yerde kalan kan veya zar izi · erkek çocuğun salgıyla, kız çocuğun adetle erginleşmesi · meni öncesi salgı çıkarmak
  الشهود ما يخرج على رأس الصبي (maqayis;ayn;tahdhib)؛ الشاهد الذي يخرج مع الولد (sihah)؛ شهود الناقة آثار موضع منتجها من دم أو سلى (maqayis;sihah)؛ أشهد الغلام إذا أمذى وأدرك وأشهدت الجارية إذا حاضت وأدركت (tahdhib)
- **B007** petekli bal — petek içindeki süzülmemiş bal · petekli baldan bir parça · petekli ballar
  الشَّهْد العسل في شمعها (maqayis;sihah)؛ الشهد العسل ما لم يعصر من شمعه (ayn;tahdhib)؛ الواحدة شهدة وشهدة والجمع شهاد (ayn;sihah;tahdhib)
- **B008** durumu gösteren belirti — geceye işaret eden yıldız · akşam namazı için kullanılan ad · atın üstünlüğünü ve iyi koştuğunu gösteren koşu
  الشاهد النجم (tahdhib)؛ صلاة الشاهد صلاة المغرب (tahdhib)؛ الشاهد من جريه ما يشهد له على سبقه وجودته (tahdhib)

## ق ت ل (root_001200): 85:4 قُتِلَ

- **B001** canını alarak öldürme — öldürme, canına son verme · onu kötü ve çirkin bir biçimde öldürme · tek bir öldürme olayı · öldürülmüş kimse · insan bedenindeki ölümcül noktalar
  القتل معروف (ayn;jamhara;sihah;tahdhib)؛ قتله إذا أماته بضرب أو جرح أو حجر أو سم أو علة (ayn;tahdhib)؛ أصل القتل إزالة الروح عن الجسد (mufradat)؛ مقاتل الإنسان المواضع التي إذا أصيبت قتله ذلك (maqayis;jamhara;sihah)
- **B002** boyun eğdirme; hayvanı işe alıştırma; deneyimle pişme — uysallaştırılmış ve işe alıştırılmış · işlerce sınanmış, deneyimli adam
  أصل صحيح يدل على إذلال وإماتة (maqayis)؛ المقتل من الدواب ما ذل ومرن على العمل (ayn;tahdhib)؛ رجل مقتل أي مجرب (sihah;tahdhib)؛ قتلت فلانا وقتلته إذا ذللته (tahdhib;mufradat)
- **B003** eksiksiz ve kesin olarak bilme — bir şeyi eksiksiz ve kesin olarak bilmek
  قتلت الشيء خبرا وعلما (maqayis;sihah)؛ قتلته علما وقتلته يقينا للرأي والحديث (tahdhib)؛ قتلت كذا علما وما قتلوه يقينا أي ما علموا كونه مصلوبا علما يقينا (mufradat)
- **B004** nazlıca salınma; gereksinime yumuşakça yaklaşma; kadına yalvarma — delikanlı için süslenip nazlıca salınmak · gereksinimini ince ve yumuşak yollarla elde etmeye çalışmak · kadına boyun eğip yalvarmak
  تقتلت الجارية للرجل حتى عشقها كأنها خضعت له (maqayis)؛ تقتلت الجارية للفتى تزينت ومشت مشية حسنة تقلبت فيها وتثنت وتكسرت (ayn)؛ تقتل الرجل لحاجته إذا تأتى لها والرجل يتقتل للمرأة يتضرع إليها (jamhara)؛ تقتلت المرأة في مشيتها إذا تقلبت وتثنت وتكسرت (sihah)؛ معنى تقتلها وتدللها واختيالها (tahdhib)
- **B005** öldürülmeye açık kılma veya ölüm nedeni hazırlama — onu öldürülme tehlikesine atmak · insanın ölüm nedeni iki çenesi arasındadır, yani dilidir
  أقتلت فلانا عرضته للقتل (maqayis;ayn;sihah;tahdhib;mufradat)؛ مقتل الرجل بين فكيه أي سبب قتله بين لحييه (tahdhib)
- **B006** aşka yenik düşmüş yürek; aşk veya görünmeyen varlıklar yüzünden aklın bozulması — aşka yenik düşmüş yürek · aşk ya da görünmeyen varlıklar yüzünden aklı karışıp kendinden geçmek
  قلب مقتل إذا قتله العشق (maqayis;ayn;sihah;tahdhib)؛ إذا قتله العشق أو الجن قيل اقتتل (maqayis;sihah)؛ اقتتله العشق والجن ولا يقال ذلك في غيرهما (mufradat)؛ اقتتل الرجل إذا جن واقتتلته الجن أي خبلوه (tahdhib)
- **B007** içkiyi suyla karıştırıp sertliğini giderme [kalıp] — içkiyi suyla karıştırıp sertliğini gidermek
  قتلت الخمر بالماء إذا مزجت (maqayis;jamhara;sihah;mufradat)؛ الخمر مقتولة إذا مزجت بالماء حتى ذهبت شدتها فصار رياضة لها (tahdhib)
- **B008** düşman veya denk rakip — düşman veya rakip · onun dengi, benzeri ve rakibi
  القتل العدو وجمعه أقتال (maqayis;sihah)؛ قوم أقتال أي أهل الوتر والترة أي أعداء ذوي ترات (ayn)؛ فلان قتل فلان أي نظيره وابن عمه (jamhara)؛ الأقتال الأعداء واحدهم قتل وهم الأقران (tahdhib)؛ القتل العدو والقرن (mufradat)
- **B009** can; dişi deve için sağlam ve iri beden yapısı — can veya bedende kalan yaşam · sağlam ve iri yapılı dişi deve
  القتال النفس (maqayis;sihah)؛ القتال بقية النفس (tahdhib)؛ ناقة ذات قتال إذا كانت وثيقة أو غليظة وثيقة الخلق (maqayis;jamhara;sihah)
- **B010** Tanrı'nın lanetlemesi, yok etmesi veya düşman olması dileği [kalıp] — Tanrı onları lanetlesin veya yok etsin · kahrolsun insan
  قاتلهم الله أي لعنهم (ayn;tahdhib)؛ قتل الإنسان معناه لعن الإنسان وقاتله الله لعنه (tahdhib)؛ قتل الخراصون لفظ قتل دعاء عليهم (mufradat)؛ قاتل الله فلانا أي عاداه (tahdhib)
- **B011** öldürme amacıyla karşılıklı savaşma — birbiriyle savaşmak · karşılıklı savaşma, çatışma · savaşabilecek durumdaki kişiler · topluluk birbirleriyle savaştı
  اقتتل القوم وتقتلوا في معنى تقاتلوا (jamhara)؛ المقاتلة القتال وقد قاتلته قتالا وقيتالا (sihah)؛ قاتل فلان فلانا لا يكون إلا بين اثنين (tahdhib)؛ المقاتلة المحاربة وتحري القتل والاقتتال كالمقاتلة (mufradat)
- **B012** ölümü göze alıp kendini tehlikeye atma — ölümü göze alıp kendini tehlikeye atmak
  استقتل أي استمات (sihah)
- **B013** kışın insanları doyurup ısıtan kişi [kalıp] — kışın insanları doyurup ısıtan kişi
  هو قاتل الشتوات أي يطعم فيها ويدفىء الناس (tahdhib)

## ص ح ب (root_000844): 85:4 أَصْحَٰبُ

- **B001** süreğen eşlik ve yakın birliktelik — eşlik etmek veya birlikte bulunmak · sürekli eşlik eden kimse veya yoldaş · eşlik edenler topluluğu veya yoldaşlar · eşlik etme ve birlikte bulunma durumu · karşılıklı ve süreğen biçimde birlikte bulunma · bir şeyin sahibi veya o şeye sahip kişi · bir topluluğun ya da yöneticinin işini yürüten görevli · ey arkadaşım · iyi ve istekli biçimde arkadaşlık eden · yanında bir eşlikçisi bulunmak
  أصل واحد يدل على مقارنة شيء ومقاربته (maqayis)؛ الصاحب يجمع بالصحب والصحبان والصحبة والصحاب والأصحاب (ayn)؛ الصحب والصحاب والأصحاب والصحابة واحد (jamhara)؛ صحبه يصحبه صحبة وصحابة وجمع الصاحب صحب (sihah)؛ الصاحب الملازم إنسانا كان أو حيوانا أو مكانا أو زمانا (mufradat)؛ المصاحبة والاصطحاب أبلغ من الاجتماع (mufradat)؛ يقال للمالك للشيء هو صاحبه (mufradat)؛ وأصحب الرجل إذا كان ذا صاحب (ayn)
- **B002** eşlik eden koruma ve destek — Tanrı seni korusun · Tanrı onu korumasın · korunmak veya dinginlik ve destek görmek
  صحبك الله أي حفظك (ayn)؛ صحبه الله وأصحبه وصاحبه أي حفظه (jamhara)؛ لا يكون لهم من جهتنا ما يصحبهم من سكينة وروح وترفيق (mufradat)
- **B003** boyun eğip uyumlu duruma gelme — boyun eğmek ve güçlükten sonra uyumlu duruma gelmek · bir kimsenin ardından boyun eğerek gitmek
  أصحب فلان إذا انقاد (maqayis)؛ أصحبت الرجل إذا اتبعته منقادا (jamhara)؛ أصحب البعير والدابة إذا انقاد بعد صعوبة (sihah)؛ الإصحاب للشيء الانقياد له (mufradat)
- **B004** eşlikçi kılmak, yanında götürmek veya uygun düşmek — bir şeyi ona eşlikçi kılmak · kitabı veya başka bir şeyi yanına alıp götürmek · ona uygun düşmek ve onunla bağdaşmak
  كل شيء لاءم شيئا فقد استصحبه (maqayis;ayn;sihah)؛ أصحبته الشيء جعلته له صاحبا (sihah)؛ استصحبته الكتاب وغيره (sihah)؛ أصحب فلان فلانا جعل صاحبا له (mufradat)
- **B005** oğlunun büyüyüp babasına yoldaş olması — oğlu büyüyüp kendisine yoldaş olacak yaşa gelmek
  أصحب الرجل إذا بلغ ابنه (maqayis;sihah)؛ أصحب فلان إذا كبر ابنه فصار صاحبه (mufradat)
- **B006** kılı veya yünü üzerinde bırakılmış deri — kılı veya yünü üzerinde bırakılmış deri, post ya da tulum · hayvanı yüzerken kılı veya yünü deri üzerinde bırakmak
  الأديم إذا ترك عليه شعره مصحب (maqayis)؛ جلد مصحب إذا كان عليه شعره وصوفه (ayn)؛ صحبت المذبوح إذا سلخته وأبقيت على الجلد صوفا أو شعرا (jamhara)؛ أديم مصحب إذا دبغته وتركت عليه بعض الصوف أو الشعر (jamhara)؛ المصحب من الزقاق ما الشعر عليه (sihah)؛ أصحبته إذا تركت صوفه أو شعره عليه (sihah)؛ أديم مصحب أصحب الشعر الذي عليه ولم يجز عنه (mufradat)
- **B007** suyun yüzünü yosun kaplaması — suyun yüzü yosunla kaplanmak
  أصحب الماء إذا علاه الطحلب (maqayis;sihah)
- **B008** kızıla çalan açık toprak renginde eşek — kızıla çalan açık toprak renginde eşek
  حمار أصحب أي أصحر يضرب لونه إلى الحمرة (sihah)

## خ د د (root_000395): 85:4 ٱلْأُخْدُودِ

- **B001** yanak ve yanağa benzetilen yan yüz — yanak · yastık · taşıma kabinlerinin sağ ve sol yan levhaları
  الخَدّ خد الإنسان وبه سميت المخدة (maqayis)؛ المخدة واشتقاقها من الخد (ayn)؛ الخد في الوجه وهما خدان والمخدة (sihah)؛ الخد من الوجه من لدن المحجر إلى اللحي ومنه اشتق اسم المخدة (tahdhib)؛ أصل ذلك من خدي الإنسان وهما ما اكتنفا الأنف (mufradat)؛ الخدود في الغبط والهوادج جوانب الدفتين (tahdhib)
- **B002** uzun, derin yarık veya oluk — yarık açma veya uzun oluk kazma · toprağı yarıp oluk açan demir araç · toprakta uzunlamasına açılmış derin yarık · uzun yarıklar veya yüzeye açılmış oluk izleri · çukur · deriyi yarıp iz bırakan darbe · kamçının sırtta açtığı oluk izleri · kuyu iplerinin sürtünerek kuyu ağzında açtığı izler · selin akarken toprağı yarması
  الخد الشق والأخاديد الشقوق في الأرض (maqayis)؛ الخد جعلك أخدودا في الأرض تحفره مستطيلا وأخاديد السياط في الظهر (ayn)؛ الأخدود شق في الأرض مستطيل والخدة الحفرة وضربة أخدود (sihah)؛ خدوا في الأرض أخاديد وأخاديد السياط وأخاديد الأرشية وخد السيل في الأرض (tahdhib)؛ الخد والأخدود شق في الأرض مستطيل غائص (mufradat)
- **B003** zayıflıktan etin çekilip büzüşmesi — zayıflıktan etin çekilip çökmesi · etin zayıflıkta çekilmesi veya hayvanın cılızlaşması · eti azalmış, zayıf erkek · eti azalmış, zayıf kadın · eti çekilip büzüşmek
  التخدد تخدد اللحم من الهزال وامرأة متخددة مهزولة (maqayis)؛ التخديد تخديد اللحم عند الهزال ورجل متخدد وامرأة متخددة مهزول قليل اللحم (ayn)؛ المتخدد المهزول وقد خدد لحمه وتخدد أي تشنج (sihah)؛ التخديد من تخديد اللحم إذا ضمرت الدواب ورجل متخدد وامرأة متخددة مهزول قليل اللحم (tahdhib)؛ تخدد اللحم زواله عن وجه الجسم (mufradat)
- **B004** devenin yanağına vurulan damga — devenin yanağına vurulan damga · yanağı damgalanmış deve
  الخداد ميسم من المياسم ولعله يكون في الخد يقال منه بعير مخدود (maqayis)؛ الخداد ميسم في الخد والبعير مخدود (sihah)
- **B005** insan topluluğu, kesimi veya katmanı — insan topluluğu, kesimi veya katmanı · grup grup veya katman katman · insanların ayrı bölüklere ayrılması
  رأيت خدا من الناس أي طبقة وطائفة وقتلهم خدا فخدا أي طبقة بعد طبقة والخد الجماعة من الناس؛ تخدد القوم إذا صاروا فرقا
- **B006** yol ve yol yüzeyindeki belirgin izler — yol · yolun izlerinin veya oluklarının belirginleşmesi
  الخد الطريق؛ خدد الطريق شركه
- **B007** kesme ve kesen — onu kesip ayırdı · kesen veya kesici · devenin bir şeyi dişiyle yarıp kesmesi
  أخده فخده إذا قطعه؛ مخد أي قاطع

## ن و ر (root_001564): 85:5 ٱلنَّارِ

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## و ق د (root_001672): 85:5 ٱلْوَقُودِ

- **B001** ateşin tutuşması, yakılması ve alevli görünümü — ateş tutuştu ve yandı · tutuştu, yanmaya başladı · alevlendi, harlayarak yandı · ateşi yaktı · ateşi yakmaya girişti veya yakılmasını istedi · yanma; ortaya çıkan alev · ateşin kendisi veya görünen alevi
  كلمة تدل على اشتعال نار (maqayis)؛ وقدت النار واتقدت وتوقدت وأوقدتها (maqayis)؛ وقدت النار وقودا ووقدا (ayn;sihah;mufradat)؛ أوقدتها واستوقدتها (sihah;mufradat)؛ الوقود بالضم الاتقاد (sihah)؛ الوقد نفس النار أو ما ترى من لهبها (maqayis;ayn)؛ الوقود لما حصل من اللهب (mufradat)
- **B002** yakacak odun ve ateşlik yakıt — yakacak odun; ateş için hazırlanmış yakıt
  الوقود الحطب (maqayis)؛ وقود النار أي حطبها (ayn)؛ الوقود بالفتح الحطب (sihah)؛ الوقود للحطب المجعول للوقود (mufradat)
- **B003** ateş yakılan yer — ateş yakılan yer, ocak · ateşin bulunduğu veya yakıldığı yer
  الموقد والمستوقد موضع النار (ayn)؛ الموضع موقد مثال مجلس (sihah)
- **B004** yazın en şiddetli sıcağı ve sıcak dönemi — şiddetli sıcak; on gün ya da yarım ay süren sıcak dönem · yazın en şiddetli sıcağı
  وقدة الصيف أشده حرا (maqayis;ayn;mufradat)؛ الوقدة أشد من الحر وهي عشرة أيام أو نصف شهر (sihah)
- **B005** ateş gibi hızla parlayıp şiddetlenme [kalıp] — çabuk kıvılcım çıkaran ateş çubuğu · etkinlikte canlı ve kararlı gönül · öfkeden parladı, öfkesi şiddetlendi · savaşı başlattı veya körükledi
  زند ميقاد سريع الوري وقلب وقاد سريع التوقد في النشاط والمضاء (ayn)؛ اتقد فلان غضبا (mufradat)؛ يستعار وقد واتقد للحرب كاستعارة النار والاشتعال (mufradat)
- **B006** ateş gibi ışıldamak [kalıp] — toynağın küçük parıltısı ışıldadı · mücevher ve altın ateş gibi ışıldadı
  وقد الحافر إذا تلألأ بصيصه وفي كل شيء (ayn)؛ يستعار ذلك للتلألؤ فيقال اتقد الجوهر والذهب (mufradat)

## ق ع د (root_001244): 85:6 قُعُودٌ

- **B001** oturup yer tutma — ayakta durmayıp oturmak · tek bir oturuş · oturan kişinin oturuş biçimi · oturulan yer · dingin ve güvenli yer · savaşta yerleşilen mevziler · kuşun yere çöküp yerinde kalması
  قعد الرجل يقعد قعودا (maqayis;ayn;tahdhib)؛ قعد قعودا أي جلس (sihah)؛ القعود يقابل به القيام (mufradat)؛ القعدة المرة الواحدة (maqayis;ayn;sihah;mufradat)؛ المقاعد موضع قعود الناس (maqayis;sihah)؛ المقعد مكان القعود (mufradat)
- **B002** eylemden geri durma — sefere veya işe katılmayıp geri duran kimse · sefere kayıtlı olmayan ya da savaştan geri kalan topluluk · görüşünü taşıdığı halde ayaklanmaya katılmayan kişi · seni ne alıkoydu
  القعد القوم لا ديوان لهم (maqayis;ayn;sihah)؛ رجل قاعد عن الغزو (tahdhib)؛ يعبر عن المتكاسل في الشيء بالقاعد (mufradat)؛ ما قعدك واقتعدك أي حبسك (ayn)؛ ما تقعدني عن ذلك الأمر إلا شغل (tahdhib)؛ إنا هاهنا قاعدون يعني متوقفون (mufradat)
- **B003** doğurganlık ve evlilik çağını geçmiş kadın — ay hali, doğurma veya evlenme beklentisi kalmamış kadın
  امرأة قاعدة إن أردت القعود وقاعد عن الحيض والأزواج والجمع قواعد (maqayis)؛ امرأة قاعد وهن اللواتي قعدن عن الولد فلا يرجون نكاحا (ayn)؛ القاعد من النساء التي قعدت عن الولد والحيض (sihah)؛ امرأة قاعد إذا قعدت عن المحيض (tahdhib)؛ القاعدة لمن قعدت عن الحيض والتزوج والقواعد جمعها (mufradat)
- **B004** yanında bulunan eşlikçi — kişinin yanında bulunan eşi · yanında oturan yoldaş · bir kimseye hizmet etmek
  قعيدة الرجل امرأته (maqayis;ayn;sihah;tahdhib)؛ قعيدك جليسك (ayn)؛ القعيد المقاعد (sihah;tahdhib)؛ قعدت الرجل وأقعدته أي خدمته (tahdhib)
- **B005** bekleyip gözetleme — yanında görevli gözetleyici · pusu kurup beklemek · arkadan gelen hayvan veya kuş
  القعيد من الوحش ما يأتيك من ورائك (maqayis;sihah)؛ القعيدة ما أتاك من خلفك من ظبي أو طائر (ayn)؛ القعيد الذي يجيء من ورائك من الظباء (tahdhib)؛ عن اليمين وعن الشمال قعيد أي ملك يترصده (mufradat)؛ وقعيدا كل حي حافظاه الموكلان به (ayn)؛ عن الترصد للشيء بالقعود له (mufradat)
- **B006** Tanrı adına yalvarma yemini — Tanrı adına yemin veya yalvarma sözü
  قعيدك الله وقعدك الله في معنى القسم (maqayis)؛ قعيدك الله لا آتيك وقعدك الله لا آتيك يمين للعرب (sihah)؛ قعدك الله مثل نشدتك الله (tahdhib)؛ قعيدك الله وقعدك الله أي أسأل الله الذي يلزمك حفظك (mufradat)
- **B007** alt dayanak ve temel [kalıp] — evin temeli · taşıt kafesinin alt enine çıtaları · bulutun alt tabanı · üst üste dayanmış kum bölümü
  قواعد البيت أساسه (maqayis;ayn;sihah;mufradat)؛ قواعد الهودج خشبات أربع معترضات في أسفله (maqayis;ayn;sihah;tahdhib;mufradat)؛ قواعد السحاب أصولها المعترضة في آفاق السماء (tahdhib)؛ قواعد الرمل ما ارتكن بعضه فوق بعض (ayn)
- **B008** üzerine oturulan binek — binmek için ayrılan hayvan · üzerine binilen genç deve · eyerler ve biniş takımları
  القعدة الدابة تقتعد للركوب (maqayis;ayn;tahdhib)؛ القعود من الإبل كذلك (maqayis)؛ القعود من الإبل هو البكر حين يركب (sihah)؛ القعود والقعودة من الإبل ما اقتعده الراعي (ayn;tahdhib)؛ القعيدات السروج والرحال (sihah)؛ القعدات الرحال والسروج (tahdhib)
- **B009** hastalık yüzünden yürüyemez olma — hastalık yüzünden yürüyemeyen kimse · devenin kalçasını tutan hastalık · at bacağının doğrulamayacak kadar eğrilmesi
  الإقعاد والقعاد داء يأخذ الإبل في أوراكها (maqayis;ayn;sihah;tahdhib)؛ المقعد والمقعدة اللذان لا يطيقان المشي (ayn)؛ رجل مقعد إذا أزمنه داء (tahdhib)؛ لمن يعجز عن النهوض لزمانة به (mufradat)؛ الأقعاد في رجل الفرس أن تقوس جدا فلا تنتصب (sihah)
- **B010** henüz yükselmemiş yavru evresi — uçmadan önceki kuş yavruları · henüz tam kalkamayan kartal yavrusu · kanadı olgunlaşmamış çekirge · çömelmiş görünümlü kurbağalar · küçük hurma ağaçları · fidanın gövde oluşturması
  المقعدات فراخ القطا والنسر قبل أن تنهض للطيران (ayn)؛ المقعد فرخ النسر (maqayis;tahdhib)؛ القعيد الجراد الذي لم يستو جناحه (maqayis;sihah)؛ المقعدات الضفادع (maqayis;ayn;tahdhib)؛ وبه شبه الضفدع فقيل له مقعد (mufradat)؛ القعد النخل الصغار (ayn;tahdhib)؛ قعدت الفسيلة صار لها جذع (ayn;sihah;tahdhib)
- **B011** dolu ya da dik duran biçim — eğilmemiş, dik ve çıkıntılı meme · dolduğu için duran hububat çuvalı · uzun olmayan kum kütlesi · elde çevrilen değirmen
  الثدي المقعد الناهد (maqayis;ayn;sihah;tahdhib)؛ ثدي مقعد للكاعب ناتئ (mufradat)؛ القعيدة الغرارة لأنها تملأ وتقعد (maqayis;sihah)؛ القاعد الجوالق الممتلىء حبا (tahdhib)؛ القعيدة من الرمال التي ليست بمستطيلة (sihah;tahdhib)؛ رحى قاعدة (tahdhib)
- **B012** soydaki ata mesafesi — büyük ataya ara kuşak sayısıyla yakın sayılan soy durumu
  القعدد أقرب القوم إلى الأب الأكبر (maqayis)؛ هذا أقعد من ذاك في النسب أي أسرع انتهاء وأقرب أبا (ayn)؛ رجل قعدد إذا كان قريب الآباء إلى الجد الأكبر (sihah)؛ القعدد القريب النسب من الجد الأكبر (tahdhib)؛ القعدد البعيد النسب من الجد الأكبر وهو من الأضداد (tahdhib)
- **B013** soyluluk ve erdemden geri kalmışlık — aşağı, korkak veya erdemden geri kalmış kimse
  القعدد اللئيم وزيد في بنائه لقعوده عن المكارم (maqayis)؛ رجل قعدد وقعددة جبان لئيم قاعد عن الحرب (ayn)؛ رجل قعدد إذا كان قريب الآباء إلى الجد الأكبر ويمدح به من وجه ويذم به من وجه (sihah)؛ فلان مقعد الحسب إذا لم يكن شرف (tahdhib)؛ المقعد كناية عن اللئيم المتقاعد عن المكارم (mufradat)
- **B014** yolculuktan geri durma ayı — kutsal ziyaret öncesinde yolculuktan geri durulan ay
  ذو القعدة شهر كانت العرب تقعد فيه عن الأسفار (maqayis)؛ ذو القعدة اسم شهر كانت العرب تقعد فيه ثم تحج في ذي الحجة (ayn)؛ ذو القعدة الشهر الذي يلي شوالا (tahdhib)
- **B015** suya ulaşmadan bırakılan kuyu — suya ulaşmadan bırakılmış kuyu
  المقعدة من الآبار التي أقعدت فلم ينته بها إلى الماء وتركت (maqayis)؛ المقعدة من الآبار التي أقعدت فلم ينته بها إلى الماء فتركت (ayn)؛ المقعدة من الآبار التي احتفرت فلم ينبط ماؤها فتركت (tahdhib)
- **B016** başlamak, olmak ya da kalmak — bir şeyi yapmaya başlamak veya o duruma gelmek · bir yerde kalmak
  قعد فلان يشتمني وقام يشتمني بمعنى طفق (tahdhib)؛ يقعد الأير له لعاب كقولك يصير (tahdhib)؛ أقعد بذلك المكان كما يقال أقام (tahdhib)
- **B017** kusurlu şiir dizesi — ölçü veya uyak eksilmesi bulunan şiir dizesi
  إذا كان بيت فيه زحاف قيل له مقعد (tahdhib)؛ الإقواء نقصان الحرف من الفاصلة وكان يسمي هذا المقعد (tahdhib)

## ف ع ل (root_001167): 85:7 يَفْعَلُونَ, 85:16 فَعَّالٌ

- **B001** bir şeyi yapıp etkileme — bir şeyi yapmak, ortaya çıkarmak veya üzerinde etki bırakmak · yapma işi, eylemin ad eylem biçimi · gerçekleşmiş işin veya eylemin adı · tek bir yapma olayı veya iyi ya da kötü iş · işlerin çoğulu · eylem adı olarak kullanılan biçim · bir etkinin altında değişmek veya ona uymak
  أصل صحيح يدل على إحداث شيء من عمل وغيره (maqayis)؛ فعل يفعل فعلا وفعلا فالفِعل المصدر والفِعل الاسم (ayn)؛ الفِعل بالفتح مصدر فعل يفعل والفِعل بالكسر الاسم (sihah)؛ فعلت الشيء فانفعل كسرته فانكسر (sihah)؛ فعل يفعل فعلا وفعلا فالمصدر مفتوح والاسم مكسور (tahdhib)
- **B002** iyi iş ve kişisel tutum — eli açıklık ve güzel davranış; ayrıca tek kişinin iyi ya da kötü işi
  الفَعال بفتح الفاء الكرم وما يفعل من حسن (maqayis)؛ الفَعال اسم للفعل الحسن مثل الجود والكرم ونحوه (ayn)؛ الفَعال بالفتح الكرم (sihah)؛ الفَعال فعل الواحد خاصة في الخير والشر (tahdhib)؛ الفَعال يكون في المدح والذم (tahdhib)
- **B003** el işçileri — işçiler, özellikle çamur ve kazı işlerinde çalışanlar · marangoz
  الفَعلة العملة وهم قوم يستعملون الطين والحفر وما يشبه ذلك من العمل (ayn)؛ الفَعلة قوم يعملون عمل الطين والحفر وما أشبه ذلك من العمل (tahdhib)؛ النجار يقال له فاعل (tahdhib)
- **B004** uydurup düzme — yalanı, düzme sözü veya anlatıyı uydurmak · sahibince ortaya atılmış veya önceki örneği olmadan yapılmış şey
  افتعل كذبا وزورا أي اختلق (sihah)؛ شعر مفتعل إذا ابتدعه قائله (tahdhib)؛ افتعل فلان حديثا إذا اخترقه (tahdhib)؛ يقال لكل شيء يسوى على غير مثال تقدمه مفتعل (tahdhib)
- **B005** karşılıklı eylem — eylem iki kişi arasında gerçekleştiğinde kullanılan ad
  الفِعال بكسر الفاء إذا كان الفعل بين الاثنين (tahdhib)؛ فإذا كان من فاعلين فهو فِعال (tahdhib)
- **B006** balta ya da keser sapı — balta sapı veya balta gözüne takılan ağaç parça; keser sapı
  يقولون الفَعال خشبة الفأس (maqayis)؛ الفَعال العود الذي يجعل في خرت الفأس يعمل به (tahdhib)؛ في نصاب القدوم سماه فَعالا (tahdhib)
- **B007** dil bilgisi tümleçleri — dil bilgisinde eyleme bağlanan öge türleri · eylemin yöneldiği veya etkilediği şey; nesne · eylemin yapılma amacı veya gerekçesi · yer, zaman veya durum bildirerek eyleme bağlanan öge · eylemin üzerinde gerçekleştiği alanı bildiren öge · doğrudan eylem adı; geçişli veya geçişsiz eylemle kullanılan tür
  المفعولات على وجوه في باب النحو (tahdhib)؛ فمفعول به (tahdhib)؛ ومفعول له (tahdhib)؛ ومفعول فيه (tahdhib)؛ ومفعول عليه (tahdhib)؛ ومفعول بلا صلة وهو المصدر (tahdhib)

## ECHO ء ب و (root_000007): for 85:7 يَفْعَلُونَ, 85:16 فَعَّالٌ: withheld observed target; not identity

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ء م ن (root_000054): 85:7 بِٱلْمُؤْمِنِينَ, 85:8 يُؤْمِنُوا۟, 85:10 ٱلْمُؤْمِنِينَ, 85:10 وَٱلْمُؤْمِنَٰتِ, 85:11 ءَامَنُوا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ن ق م (root_001545): 85:8 نَقَمُوا۟

- **B001** hoşnutsuzlukla yadırgama ve ayıplama — yadırgamak, ayıplamak ve hoşnutsuzluk duymak · yadırgama ve ayıplama · ayıplayıp hoşnutsuzluğunu gösteren kimse · yadırgama ve hoşnutsuzluk
  إنكار شيء وعيبه؛ أنكرت عليه فعله (maqayis)؛ أنكر ولم يرض (ayn)؛ عتبت عليه؛ كرهته (sihah)؛ بالغت في كراهة الشيء؛ النقمة الإنكار (tahdhib)؛ أنكرته إما باللسان وإما بالعقوبة (mufradat)
- **B002** cezalandırarak karşılık verme ve öç alma — cezalandırma, acı çektirme ve öç alma · yaptığı kötülüğe ceza ile karşılık vermek · öldürülen yakınının öcünü almak · öldürülürse onun öcünü almak
  النقمة من العذاب والانتقام؛ فعاقبه (maqayis)؛ انتقمت منه كافأته عقوبة بما صنع (ayn)؛ انتقم الله منه أي عاقبه؛ النقمة (sihah)؛ نقم فلان وتره أي انتقم؛ النقمة العقوبة (tahdhib)؛ النقمة العقوبة (mufradat)

## ء ل ه (root_000047): 85:8 بِٱللَّهِ, 85:9 وَٱللَّهُ, 85:20 وَٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 85:8 بِٱللَّهِ, 85:9 وَٱللَّهُ, 85:20 وَٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ع ز ز (root_001008): 85:8 ٱلْعَزِيزِ

- **B001** güçlü, yenilmez ve saygın olma — yenilmezlik sağlayan güç ve saygınlık durumu · güçlü, üstün gelen ve yenilmeyen · güçsüzlükten çıkıp güçlü ve saygın duruma gelmek
  العين والزاء أصل صحيح واحد يدل على شدة وقوة (maqayis); العزة لله والله العزيز (ayn); عز يعز عزة وعزا إذا صار عزيزا (jamhara); العز خلاف الذل (sihah); العزيز الممتنع فلا يغلبه شيء (tahdhib); العزة حالة مانعة للإنسان من أن يغلب (mufradat)
- **B002** üstün gelip boyun eğdirme — onu yenip boyun eğdirmek · onunla üstünlük yarışına girmek · sözlü çekişmede beni yenmek · üstün gelen, yenilenin malını alır
  غلبة وقهر (maqayis); عزه على أمره إذا غلبه (maqayis); وعزني في الخطاب أي غلبني (ayn;tahdhib;mufradat); عز يعز عزا إذا قهر (jamhara); عزه يعزه عزا غلبه (sihah); عزه يعزه إذا غلبه وقهره (tahdhib)
- **B003** çok kıt ve güç bulunur olma — neredeyse bulunamayacak kadar azalmak · kıt, güç bulunan ve benzeri olmayan
  عز الشيء حتى يكاد لا يوجد (maqayis); عز الشيء جامع لكل شيء إذا قل حتى يكاد لا يوجد (ayn); عز الشئ إذا قل لا يكاد يوجد (sihah); عز كذا وكذا إذا قل حتى لا يكاد يوجد (tahdhib); يصعب مناله ووجود مثله (mufradat)
- **B004** güçlendirip pekiştirme — onu güçlü ve saygın kılmak · onu güçlendirip sağlamlaştırmak
  أعززته أنا جعلته عزيزا (maqayis); أعززته قويته وعززته أيضا (maqayis); أعزه الله (ayn); فعززنا بثالث أي قوينا وشددنا (sihah); قويناه وشددناه (tahdhib)
- **B005** kişiye ağır ve çetin gelme — bu bana zor, ağır ve çetin geldi · başına gelen bana çok büyük ve ağır geldi
  أعززت بما أصاب فلانا أي عظم علي واشتد (maqayis); أعزز علي بما أصاب فلانا أي أعظم علي (ayn); عز علي أن تفعل كذا (sihah); عز علي ذاك أي حق واشتد (sihah); عز علي كذا صعب (mufradat)
- **B006** dar kanallı ve güç sağılan olma — meme kanalı dar, sütü az veya güç sağılan dişi hayvan · malı çok olduğu halde vermeyen cimri kişi
  ناقة عزوز إذا كانت ضيقة الإحليل لا تدر إلا بجهد (maqayis); العزوز الشاة الضيقة الإحليل (ayn); العزوز من النوق الضيقة الإحليل (sihah); شاة عزوز ضيقة الإحليل لا تدر حتى تحلب بجهد (tahdhib); شاة عزوز قل درها (mufradat)
- **B007** sertleşip sıkıca pekişme — taşsız, sert ve su tutmayan zemin · kum sıkılaşıp dağılmaz hale gelmek · yağmur toprağı bastırıp pekiştirmek
  العزازة أرض صلبة ليست بذات حجارة (maqayis); العزاز أرض صلبة (ayn;sihah;tahdhib); كل شيء صلب فقد استعز (jamhara); تعزز لحم الناقة إذا صلب واشتد (maqayis;tahdhib); استعز الرمل وغيره إذا تماسك فلم ينهل (maqayis;sihah); المطر يعزز الأرض أي يلبدها (sihah;mufradat)
- **B008** çetin ve baskın doğa şiddeti — ağır ve çetin yıl · çok ve şiddetli yağmur · baskın ve güçlü sel
  العزاء السنة الشديدة (maqayis;ayn;sihah); العز من المطر الكثير الشديد (maqayis); مطر عز أي شديد (sihah); العز المطر الشديد الوابل (tahdhib); سيل عز وهو السيل الغالب (maqayis)
- **B009** hastalık veya durumun kişiye üstün gelmesi — hastalık, ölüm veya başka bir durum ona üstün gelmek · iş onun üzerinde inatla sürüp egemen olmak · hastalığı çok ağır olan kişi
  استعز على المريض إذا اشتد مرضه (maqayis); استعز به المرض (maqayis); استعز عليه الشيطان أي غلب عليه (maqayis); استعز عليه الأمر إذا لج فيه (maqayis); استعز بفلان أي غلب في كل شيء مرض أو غيره (sihah;tahdhib); استعز بفلان إذا غلب بمرض أو بموت (mufradat)
- **B010** atın iki kalça ucu arasındaki bölge — atın sağrı ile uyluk yakınındaki iki kalça ucu arası
  العزيزاء من الفرس ما بين عكوته وجاعرته (maqayis); العزيزى من الفرس وهما طرفا الوركين (sihah); العزيزاء وهما عزيزاوا الفرس ما بين جاعرتيه (tahdhib)
- **B011** biçime bağlı adlandırmalar — en güçlü veya en üstün sıfatının dişil biçimi · tapınılan bir putun veya kutsal ağacın adı · ceylan yavrusu; buradan türeyen kadın adı
  العزى تأنيث الأعز (maqayis;tahdhib); العزى صنم (mufradat); العزى سمرة كانت لغطفان يعبدونها (sihah;tahdhib); العزة بالفتح بنت الظبية وبها سميت المرأة عزة (sihah;tahdhib)
- **B012** keçiyi kovma ünlemiyle sürme — keçiyi kovmak için çıkarılan ünlem · keçiyi bu ünlemle azarlayıp sürmek
  يقال للعنز إذا زجرت عز عز (tahdhib); عزعزت بها فلم تعزعز (tahdhib)

## ح م د (root_000355): 85:8 ٱلْحَمِيدِ

- **B001** yermenin karşıtı olan, iyilik için teşekkürü de kapsayan övgü — yermenin karşıtı olan övgü; iyilik için teşekkür de içerebilir · birini, yaptığı övülesi bir işten dolayı övmek · övgü; yerginin karşıtı · Tanrı'yı güzel sözlerle çokça övme · onun için övgü ve teşekkür · övülecek bir iş yapmak ya da sonunda övgü kazanmak · her şeyi çokça, kimi zaman olduğundan fazla öven kimse · çok öven kimse · seni överek başlarım
  الحمد نقيض الذم (maqayis;ayn;jamhara;sihah;tahdhib)؛ الحمد الثناء (ayn;tahdhib;mufradat)؛ الحمد أعم من الشكر (sihah;mufradat)؛ التحميد كثرة حمد الله بحسن المحامد (ayn;tahdhib)
- **B002** deneyip övülesi ya da uygun bulma — birini deneyip övgüye değer bulmak · bir yeri yerleşmeye ya da otlatmaya elverişli bulmak · bu işi benim için uygun buluyor musun? · idrar kanalını yıkamayı sizin için uygun bulmak
  أحمدت فلانا إذا وجدته محمودا (maqayis;ayn;sihah;tahdhib)؛ أحمدت الأرض إذا رضيت سكناها أو مرعاها (jamhara;sihah)؛ هل تحمد لي هذا الأمر أي هل ترضاه لي (tahdhib)
- **B003** övülen veya birçok övülesi niteliği bulunan kimse — övülen, övgüye değer · çokça övülen, birçok övülesi niteliği bulunan · övülmeye daha çok layık olan ya da daha çok öven · övülen; bağlama göre öven
  رجل محمود ومحمد إذا كثرت خصاله المحمودة (maqayis;sihah)؛ محمد كأنه حمد مرة بعد أخرى (jamhara)؛ فلان محمود إذا حمد ومحمد إذا كثرت خصاله المحمودة (mufradat)؛ الحميد بمعنى المحمود (tahdhib;mufradat)
- **B004** övülesi işin varılabilecek en ileri sınırı — yapabileceğinin en ilerisi ve övülecek olanı · aktarılan sözde kadınlarda övülebilecek niteliklerin en ileri derecesi
  حماداك أن تفعل كذا أي غايتك وفعلك المحمود (maqayis)؛ حماداك أن تفعل كذا أي حمدك (ayn;tahdhib)؛ حماداك في معنى قصاراك (jamhara;sihah)؛ حماديات النساء معناه غاية ما يحمد منهن (tahdhib)؛ حماداك أي غايتك المحمودة (mufradat)
- **B005** iyiliğini başa kakıp kendine pay çıkarma [kalıp] — iyiliğini insanların başına kakıp bununla övgü beklemek
  فلان يتحمد علي أي يمن (sihah)؛ من أنفق ماله على نفسه فلا يتحمد به إلى الناس (sihah;tahdhib)
- **B006** muhatabı katarak övme veya iyilikleri teşekkürle anma [kalıp] — seninle birlikte Tanrı'yı övmek veya onun iyiliklerini sana teşekkürle anmak
  أحمد إليك الله أي معك (ayn;tahdhib)؛ أشكر إليك أياديه ونعمه (tahdhib)

## م ل ك (root_001444): 85:9 مُلْكُ

- **B001** güçlü ve tutarlı biçimde bir arada durma — hamuru sıkıca yoğurup kıvamlandırmak · sürgünü kabuğuyla kurutup sertleştirmek · kendini tutmak; dayanmak · bir şeyi ayakta tutan iç sağlamlık
  أصل صحيح يدل على قوة في الشيء وصحة (maqayis)؛ أملك عجينه قوي عجنه وشده (maqayis)؛ ملكت العجين إذا شددت عجنه (sihah)؛ ملك النبعة صلبها (sihah)؛ العجين إذا كان متماسكا متينا مملوك ومملك (tahdhib)؛ حائط ليس له ملاك أي تماسك (mufradat)
- **B002** sahiplik ve tasarruf yetkisi — bir şeye sahip olup onu tasarrufunda bulundurmak · mülkiyet; sahip olunan mal veya hak · kişinin elinin altında ve sahipliğinde bulunan şey · köleleştirilmiş kişi · köleleştirilmiş kişilere iyi davranma · özgür doğmuşken tutsak edilip köleleştirilen kişi · boşanma kararını eşin tasarrufuna bırakmak
  ملك الإنسان الشيء يملكه ملكا (maqayis)؛ الملك ما ملكت اليد من مال وخول (ayn;tahdhib)؛ ملكت الشيء أملكه ملكا (sihah)؛ وملكه المال والملك فهو مملك (sihah)؛ أملكت فلانة أمرها إذا جعل أمر طلاقها بيدها (tahdhib)؛ المملوك يختص في التعارف بالرقيق من الأملاك (mufradat)
- **B003** hükümdarlık ve kamusal egemenlik — hükümdar · hükümdar; egemen yönetici · hükümranlık; kamusal egemenlik · ilahi mutlak hükümranlık · hükümdarın yönetim alanı ve ülkesi · birini başlarına hükümdar yapmak
  والاسم الملك لأن يده فيه قوية صحيحة (maqayis)؛ الملك لله المالك المليك (ayn)؛ الملكوت ملك الله وملكوت الله سلطانه (ayn)؛ الملكوت من الملك (sihah)؛ المملكة سلطان الملك في رعيته (ayn;tahdhib)؛ له ملكوت العراق وعزه وسلطانه وملكه (tahdhib)؛ الملك هو المتصرف بالأمر والنهي في الجمهور (mufradat)؛ ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا (tahdhib)
- **B004** evlilik akdi kurma — evlilik akdi; evlendirme · kadınla evlenmek
  كنا في إملاك فلان أي أملكناه امرأته (maqayis)؛ الإملاك التزويج قد أملكوه وملكوه أي زوجوه (ayn)؛ ملكت المرأة تزوجتها (sihah)؛ أملكنا فلانا فلانة إذا زوجناه إياها (sihah)؛ شهدنا إملاك فلان وملاكه وملاكه (tahdhib)؛ الملاك التزويج وأملكوه زوجوه (mufradat)
- **B005** işi ayakta tutan temel dayanak [kalıp] — işin dayandığı temel unsur · kalp bedenin temel dayanağıdır
  ملاك الأمر ما يعتمد عليه (ayn)؛ القلب ملاك الجسد (ayn;sihah;mufradat)؛ هذا ملاك الأمر وملاكه أي صلاحه (tahdhib)
- **B006** yolun veya yerin orta ya da ana kesimi — yolun ortası veya ana kesimi · vadinin sınırı veya orta kesimi · yerleşimin ortası veya büyük kesimi
  ملك الطريق أيضا وسطه (sihah)؛ خل عن ملك الطريق وملك الوادي وملكه وملكه أي حده ووسطه (tahdhib)؛ الزم ملك الطريق أي وسطه (tahdhib)؛ أراد بالمملكة وسطها وملك الطريق معظمه ووسطه (tahdhib)
- **B007** işleri ve yaşamı sürdüren su kaynağı [kalıp] — işini yürütmesini sağlayan su · hiç suyu yok · sularımız geçimimizi ayakta tutar
  والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)؛ الماء ملك أمر أي يقوم به الأمر (sihah)؛ الماء ملك أمره (tahdhib)؛ الماء ملاك الأشياء يضرب للشيء الذي به كمال الأمر (tahdhib)؛ ماله ملك ولا نقر أي ما له ماء (tahdhib)؛ مياهنا ملوكنا ومات فلان عن ملوك كثيرة (tahdhib)
- **B008** hayvanlarda önden gidip yön veren unsur [kalıp] — arı topluluğunun önderi · bineğin ön ayakları ve yönlendirici kısmı · deve ve koyun sürüsünün öncüsü
  مليك النحل يعسوبها (sihah)؛ ملك الدابة قوائمها وهاديها (sihah;tahdhib)؛ جاءنا تقوده ملكه يعني قوائمه وهاديه (tahdhib)؛ ملك الإبل والشاء ما يتقدم ويتبعه سائره (mufradat)
- **B009** ilahi haberci varlık — 
  الملك واحد الملائكة إنما هو تخفيف الملأك والأصل مألك (ayn)؛ مألك من الألوك وهو الرسالة (ayn)؛ الملك من الملائكة واحد وجمع (sihah)؛ أصله مألك بتقديم الهمزة من الألوك وهي الرسالة (sihah)؛ الملك واحد الملائكة إنما هو تخفيف الملأك وهو مفعل من الألوك (tahdhib)

## ء ر ض (root_000025): 85:9 وَٱلْأَرْضِ

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

## ك ل ل (root_001315): 85:9 كُلِّ

- **B001** körelip güçten düşme — körelmek, yorulup güçten düşmek · körleşmiş, yorgun veya etkisiz · bineğini yorup güçten düşürmek
  خلاف الحدة وكل السيف واللسان والطرف (maqayis)؛ الكليل السيف الذي لا حد له ولسان كليل والكال المعيي (ayn)؛ كللت من المشي وكل السيف والريح والطرف واللسان (sihah)؛ الكليل السيف ولسان كليل والكال المعيي وثقل سمعه وكل بصره (tahdhib)؛ كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام (mufradat)
- **B002** bakımı başkasına yük olan — bakımı ve geçimi sahibine yük olan · yetim veya yakın aile desteği bulunmayan kişi · sahibinin taşıdığı, ona yük olan tapınma nesnesi · bakmakla yükümlü olduğum kişiler · yakınlarının geçim yükünü üstlenir duruma gelmek
  الكُلّ العيال واليتيم (maqayis)؛ الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل (ayn)؛ الكل العيال والثقل والكل اليتيم والكل الذي لا ولد له ولا والد (sihah)؛ الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه (tahdhib)
- **B003** bütün, tüm — bütün, tüm, tamamı
  كل اسم موضوع للإحاطة مضاف أبدا (maqayis)؛ كل لفظه واحد ومعناه جمع (sihah)؛ يقع كل على اسم منكور موحد فيؤدي معنى الجماعة وكلهم للإحاطة (tahdhib)؛ لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام (mufradat)
- **B004** üstsoy ve altsoy dışı mirasçılık — ana baba ve çocuk dışındaki yan kol mirasçılığı · yan koldan değil, doğrudan hakla miras almak · uzak kuzen · soy bakımından daha uzak olmak
  الكلالة هم الرجال الورثة وبنو العم الأباعد ومن مات وليس له ولد ولا والد (maqayis)؛ الكل النسب البعيد (ayn)؛ لم يرثه كلالة أي لم يرثه عن عرض والكلالة بنو العم الأباعد (sihah)؛ الكلالة من القرابة ما خلا الوالد والولد (tahdhib)؛ الكلالة اسم لما عدا الولد والوالد من الورثة (mufradat)
- **B005** çevresini kuşak gibi saran oluşum — taç veya süslü baş kuşağı · Ay'ın konaklarından biri, Akrep takımyıldızının başı · bir yerin çevresini dolaşan örtümsü bulut · çiçeklerle çevrili çayır · çevresi küçük bulut parçalarıyla sarılı bulut · başına taç takmak
  إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان (maqayis)؛ الإكليل شبه عصابة مزينة بالجواهر والإكليل من منازل القمر وروضة مكللة حفت بالنور (ayn)؛ الإكليل شبه عصابة ويسمى التاج إكليلا والإكليل منزل والسحاب كأن غشاء ألبسه وروضة مكللة وسحاب مكلل (sihah)؛ الغمام المكلل السحابة تكون حولها قطع والإكليل شبه عصابة والإكليل منزل (tahdhib)؛ الإكليل سمي بذلك لإطافته بالرأس (mufradat)
- **B006** ev biçimli ince koruyucu örtü — böceklerden koruyan ev biçimli ince örtü, cibinlik · mezar üzerine küçük kule veya kubbe biçimli yapı yükseltmek
  الكلة غشاء من ثوب يتوقى به من البعوض (ayn)؛ الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق (sihah)؛ الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب (tahdhib)
- **B007** göğüs — göğüs · göğüs
  الكلكل الصدر (maqayis)؛ الكلكل الصدر (ayn)؛ الكلكل والكلكال الصدر (sihah)؛ الكلكل فهو الصدر (tahdhib)؛ الكلكل الصدر (mufradat)
- **B008** kısa, kalın ve güçlü yapılı erkek [kalıp] — kısa, kalın, güçlü ve toplu yapılı erkek
  الكلكل القصير (maqayis)؛ الكلكل الرجل الضرب ليس بجد طويل والمربوع المجتمع الخلق (ayn)؛ رجل كلكل قصير غليظ مع شدة (sihah)؛ رجل كلكل وكلاكل وكوألل قصر وغلظ مع شدة (tahdhib)
- **B009** topluluklar, kümeler — topluluklar, kümeler
  الكلاكل من الجماعات كالكراكر من الخيل (ayn)؛ الكلاكل هي الجماعات كالكراكر (tahdhib)
- **B010** saldırıda ilerleme veya korkup geri durma; itaatsizlik — saldırıda durmadan ileri gitmek · savaşta korkup geri durmak · ona itaat etmemek, karşı gelmek
  كلل حمل ولعله أن يكون من المتضادات (maqayis)؛ المكلل الجاد حمل فكلل مضى قدما وقد يكون كلل بمعنى جبن (sihah)؛ المكلل الذي يحمل فلا يرجع حتى يقع بقرنه وكلل فلان فلانا لم يطعه (tahdhib)
- **B011** dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması — dişleri görünerek gülümsemek · bulutun içinden beyaz şimşek çakmak
  انكلت المرأة إذا ضحكت (maqayis)؛ انكل الرجل انكلالا تبسم وتنكل عن غر عذاب وانكلال الغيم بالبرق (sihah)؛ انكلت المرأة إذا تبسمت وانكل السحاب بالبرق إذا تبسم بالبرق (tahdhib)

## ش ي ء (root_000831): 85:9 شَىْءٍ

- **B001** varlık, olgu ya da konu — şey; varlık, olgu ya da konu · şeyler; varlıklar, olgular ya da konular · hiçbir şey yok; istenen bir şey yok
  الشيء واحد الأشياء (ayn); الشئ والجمع أشياء (sihah); أشياء جمع شيء (tahdhib); الذي يصح أن يعلم ويخبر عنه (mufradat)
- **B002** isteme ve gerçekleşmesini dileme — isteme; bir şeyin olmasını dileme · istedi, olmasını diledi · Tanrı'nın istemesiyle · Tanrı isterse
  المشيئة مصدر شاء يشاء (ayn); المشيئة الإرادة وقد شئت الشئ أشاؤه (sihah); الشيئة مصدر شاء يشاء مشيئة (tahdhib); المشيئة عند أكثر المتكلمين كالإرادة وفي الأصل إيجاد الشيء وإصابته (mufradat)
- **B003** bir işe ya da hedefe sevk etmek — adamı o işe yöneltti · onu zorlayıp getirdi · seni oraya getirir
  شيأت الرجل على الامر حملته عليه; وأشاءه لغة في أجاءه أي ألجأه; يشيئك إلى مخة عرقوب بمعنى يجيئك
- **B004** yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yaradılışı bozuk, görünüşü çirkin
  شيأ الله وجهه إذا دعا عليه بالقبح (maqayis); رجل مشيأ الخلق قبيح المنظر (jamhara); المشيأ المختلف الخلق القبيح وقد شيأ الله خلقه أي قبحه (tahdhib)
- **B005** özlem duymak; beğenip sevinmek [kalıp] — bu bende özlem uyandırdı · onu beğendim ve sevindim
  شاءني الشيء مثل شاعني إذا شاقني (jamhara); شؤت به أعجبت به وسررت (tahdhib)
- **B006** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت
- **B007** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان البعيد النظر وينعت به الفرس
- **B008** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل واحدها أشاءة
- **B009** yakınma ve şaşma ünlemi — Eyvah, ne haldeyim! · Vay, ne güzel!
  ياشيء مالي معناه الأسف والتلهف والحزن; يتعجب بشيء وهيء وفيء ويقول يا شيما أي ما أحسن هذا

## ش ي ء (root_000832): 85:9 شَىْءٍ

- **B001** isteme ve dileme — isteme; olmasını dileme · isteme, dileme · istedi, olmasını diledi
  للشيئة مصدر شاء يشاء مشيئة (tahdhib)
- **B002** yüzü veya yaradılışı bozuk ve çirkin — Tanrı yüzünü çirkinleştirsin diye beddua etti · yüzü veya yaradılışı bozuk ve çirkin
  شَيَّأ الله وجهه إذا دعا عليه بالقبح؛ وجه مشيأ (maqayis); المشيأ المختلف الخلق، القبيح، وقد شَيَّأ الله خلقه أي قبحه؛ المشيأ مثل المؤبن (tahdhib)
- **B003** uzağı görebilen at — uzağı görebilen; at için
  الشيئان بوزن الشيعان: البعيد النظر، وينعت به الفرس (tahdhib)
- **B004** beğenip sevinmek [kalıp] — onu beğendim ve sevindim
  شؤت به: أعجبت به وسررت (tahdhib)
- **B005** dikkat vererek dinlemek — kulak verip dinledim
  اشتأيت أي استمعت (tahdhib)
- **B006** genç hurma fidanları — genç hurma fidanları · tek bir genç hurma fidanı
  الإشاء الصغار من النخل، واحدها أشاءة (tahdhib)
- **B007** yakınma ve şaşma ünlemleri — Eyvah, ne haldeyim! · Eyvah, ne haldeyim! · Vay!; şaşma ünlemi · Vay, ne güzel!
  يافيء مالي، وياشيء مالي، وياهيء مالي، معناه كله الأسف والتلهف والحزن؛ يا شيء مالي ويا شي مالي يهمز ولا يهمز؛ من يتعجب بشيء وهيء وفيء؛ يا شيما أي ما أحسن هذا (tahdhib)

## ف ت ن (root_001128): 85:10 فَتَنُوا۟

- **B001** sınayarak niteliğini ortaya çıkarma — sınamak, denemek · altın veya gümüşü ateşte sınayıp ayarını belirlemek · sınama, deneme · sınanmış kimse veya şey · madeni ateşte sınayan kuyumcu
  أصل صحيح يدل على ابتلاء واختبار (maqayis); الفتنة الامتحان والاختبار، فتنت الذهب إذا أدخلته النار لتنظر ما جودته (sihah); جماع معنى الفتنة الابتلاء والامتحان، فتنت الفضة والذهب إذا أذبتهما بالنار ليتميز الرديء من الجيد (tahdhib); أصل الفتن إدخال الذهب النار لتظهر جودته من رداءته، وتارة في الاختبار (mufradat)
- **B002** ateşte yakma veya ateşle durumunu değiştirme — yakmak veya ateşe sokmak · yakma · yanmış veya ateşle değişmiş · taşları yanmış gibi kara lavlık · ekmeği ateşte yakmak · ateşin önceki durumundan değiştirdiği şey · kara teni yanmış görünüme benzetilen köle kadın
  الفتن الإحراق، وشيء فتين أي محرق، ويقال للحرة فتين (maqayis); على النار يفتنون أي يحرقون، وحرة فتين إذا كانت سوداء (jamhara); الفتن الإحراق، وورق فتبن أي فضة محرقة، ويقال للحرة فتين (sihah); يفتنون أي يحرقون بالنار، الفتن الإحراق، كل ما غيرته النار عن حاله فهو مفتون (tahdhib); استعمل في إدخال الإنسان النار، يوم هم على النار يفتنون (mufradat)
- **B003** doğru yoldan saptırma ve baştan çıkarma — insanları aldatan ve kötülüğü çekici gösteren şeytan · doğru yoldan saptıran · yönünden saptırmak · görüşünden döndürmek · bir erkeği arzusuyla baştan çıkarmak · saptırmak; kullanımı tartışmalı bir biçim · kadınlarla yasak ilişki istemek · içe doğan kuruntular · yaşam yolundan sapma
  الفتان الشيطان (maqayis); الفاتن المضل عن الحق، وفتنته المرأة إذا دلهته (sihah); أمالته عن القصد، الفتينة المميلة عن الحق، فتنت الرجل عن رأيه أي أزلته، الفتنة الإضلال، الفتان الشيطان (tahdhib); ما أنتم عليه بفاتنين أي بمضلين، يفتنوك عن بعض ما أنزل الله إليك (mufradat)
- **B004** kişiyi sınayan sıkıntı, bolluk veya ceza — sıkıntı, sınanma veya ceza · mal ve çocuklarla sınanma
  الفتنة المحنة، والفتنة المال، والفتنة الأولاد، والفتنة العذاب، وجماع الفتنة الابتلاء والامتحان (tahdhib); الفتنة كالبلاء، يستعملان فيما يدفع إليه الإنسان من شدة ورخاء، أي بليتهم وعذابهم، أموالكم وأولادكم فتنة (mufradat)
- **B005** inançta veya davranışta ağır sapma ve aşırılık — inançsızlık, günah veya karanlık yorumda aşırılık · dünya kazancı peşinde ölçüyü aşan
  الفتنة ههنا الكفر، والفتنة الإثم، والفتنة الغلو في التأويل المظلم، فلان مفتون يطلب الدنيا
- **B006** öldürme, savaş ve toplumsal ayrışma — öldürme, savaş ve insanlar arasındaki ağır ayrılık · öldürmek
  الفتنة القتل، يفتنهم أي يقتلهم، يكون القتل والحروب والاختلاف الذي يكون بين فرق المسلمين
- **B007** sarsıntı yüzünden malını veya aklını yitirme — başına gelen sarsıntıyla malını veya aklını yitirmek; iyi durumdan kötüye düşmek · aklı karışmış gönül
  افتتن الرجل وفتن إذا أصابته فتنة فذهب ماله أو عقله (sihah); الفتنة الجنون، وكذلك الفتون، المفتون الذي فتن بالجنون (tahdhib)
- **B008** eyerin deri örtüsü — eyerin deri örtüsü
  الفتان جلدة الرحل (maqayis); الفتان بكسر الفاء غشاء للرحل من أدم (sihah); الفتان غشاء يكون للرحل من أدم (tahdhib)
- **B009** hayatın tatlı ve acı iki hali [kalıp] — hayatın tatlı ve acı iki hali
  العيش فتنان أي لونان (maqayis); العيش فتنان حلو ومر، الفتن الناحية، فتنان أي حالان، فنان أي ضربان (tahdhib)

## ت و ب (root_000189): 85:10 يَتُوبُوا۟

- **B001** yanlistan Tanri'ya donus — yanlisindan donup Tanri'ya yoneldi · yanlistan donme, pismanlikla birakma · yanlistan donme eylemi · Tanri'ya tam bir donus · Tanri'ya donen kisi · Rabbine sikca donen kul · yaraticiniza donun
  كلمة واحدة تدل على الرجوع (maqayis)؛ التوب مصدر تاب يتوب توبا (jamhara)؛ التوبة الرجوع من الذنب (sihah)؛ تاب عاد إلى الله ورجع وأناب (tahdhib)؛ التوب ترك الذنب على أجمل الوجوه (mufradat)
- **B002** Tanri'nin donusu kabul etmesi — Tanri onun donusunu kabul etti ve bagisladi · kullarin donusunu cokca kabul eden Tanri · Tanri kulunun donusunu kabul edendir
  وقد تاب الله عليه وفقه لها (sihah)؛ تاب الله عليه أي عاد عليه بالمغفرة (tahdhib)؛ تاب الله عليه أي قبل توبته (mufradat)؛ التواب من صفات الله هو الذي يتوب على عباده (tahdhib)؛ يقال ذلك لله تعالى لكثرة قبوله توبة العباد (mufradat)
- **B003** donuse cagirma — ondan yanlisindan donmesini istedi veya bunu teklif etti
  استتابه سأله أن يتوب (sihah)؛ استتبت فلانا أي عرضت عليه التوبة مما اقترف (tahdhib)
- **B004** hafifletmeye dondurme — sizi hafifletmeye dondurdu veya onceki yasagi serbest kildi
  فتاب عليكم أي رجع بكم إلى التخفيف (tahdhib)؛ أي أباح لكم ما كان حظر عليكم (tahdhib)

## ECHO ت ب ب (root_000172): for 85:10 يَتُوبُوا۟: withheld observed target; not identity

- **B001** kayıp ve yok oluş — kayıp, yok oluş ve kaybın sürmesi · kayba uğradı veya yok oldu · elleri kayba uğradı; gücü boşa çıktı · ona yok oluş ve kayıp olsun · ona yok oluş diledim · kayba uğratma veya yok etme
  التباب الخسران (maqayis)؛ تبا للكافر أي هلاكا له (maqayis)؛ تبت يداه تبا وتبابا أي خسرت (jamhara)؛ التباب الخسران والهلاك (sihah)؛ تببوهم تتبيبا أي أهلكوهم (sihah)؛ التب الخسار وتبا لفلان على الدعاء (tahdhib)؛ وما زادوهم غير تتبيب أي تخسير (maqayis;tahdhib;mufradat)؛ التب والتباب الاستمرار في الخسران (mufradat)
- **B002** düzene girip süreklilik kazanma [kalıp] — iş hazır olup düzene girdi ve belli oldu · o şey onun için sürdü · açık, belirgin ve düzgün yol
  استتب الأمر إذا تهيأ (maqayis;sihah)؛ استتب أمر فلان إذا اطرد واستقام وتبين (tahdhib)؛ الطريق المستتب الواضح البين المستقيم (tahdhib)؛ استتب لفلان كذا أي استمر (mufradat)
- **B003** yaşlılık ve bedensel yıpranma — zayıf veya yaşlı adam · zayıf erkekler topluluğu · yaşlı kadın · sırtı yara olmuş eşek veya deve · yaşlandı
  رجل تاب ضعيف والجميع الإتباب؛ التابة الكبيرة ورجل تاب أي كبير؛ حمار تاب الظهر إذا دبر وجمل تاب كذلك؛ تبتب إذا شاخ
- **B004** kesmek — kesti
  تب إذا قطع

## ع ذ ب (root_000994): 85:10 عَذَابُ, 85:10 عَذَابُ

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

## ح ر ق (root_000311): 85:10 ٱلْحَرِيقِ

- **B001** sürtünmeyle ısıtıp aşındırma — bir şeyi sürterek veya eğeleyerek ısıtıp aşındırmak · dişlerini birbirine sürtüp gıcırdatmak · kumaşı döverek yıpratmak
  حك الشيء بالشيء مع حرارة والتهاب؛ حرقت الشيء إذا بردت وحككت بعضه ببعض (maqayis)؛ حريق الناب صريفه إذا حرق أحدهما بالآخر؛ حرق الثوب ما يصيبه من دق القصار (ayn)؛ حرقت الشيء حرقا بردته وحككت بعضه ببعض؛ حرق نابه أي سحقه (sihah)؛ حرق الشيء إيقاع حرارة في الشيء من غير لهيب؛ حرق الشيء إذا برده بالمبرد (mufradat)
- **B002** ateş, yakma ve yanma — ateş · yangın veya yanma · bir şeyi ateşe verip yakmak · ateş alıp yanmak
  الحرق النار (maqayis)؛ أحرقت النار الشيء فاحترق (ayn)؛ الحرق بالتحريك النار؛ أحرقه بالنار وحرقه؛ تحرق الشيء بالنار واحترق (sihah)؛ أحرق كذا فاحترق والحريق النار؛ الإحراق إيقاع نار ذات لهيب في الشيء (mufradat)
- **B003** yakıcı etki ve incitme — yakıcı derecede tuzlu su · uylukların sürtünmesinden oluşan tahriş · gözde veya kalpte yanma ve ağrı; yakıcı tat · beni ağır biçimde incitti · insanlar kınama veya yüklemeleriyle beni incittiler
  الحرقان المذح في الفخذين؛ أحرقني الناس بلومهم آذوني؛ ماء حراق ملح شديد الملوحة (maqayis)؛ أحرقني فلان إذا برح بي وآذاني؛ الحرقة ما يوجد من رمد عين أو وجع قلب أو طعم شيء محرق (ayn)؛ ماء حراق للشديد الملوحة؛ حرقها حمض بلاد فل يعني عطشها؛ الحرقان المذح (sihah)؛ ماء حراق يحرق بملوحته؛ أحرقني بلومه إذا بالغ في أذيته بلوم (mufradat)
- **B004** saçın kırılıp dökülmesi — saçı kırılmak, kopmak veya köklerinden zarar görüp dökülmek · kanadı veya kanat tüyleri kırılıp dökülmek
  ينقطع شعره وينسل حرق (maqayis)؛ الحرقة احتراق يقع في أصول الشعر فينحص (ayn)؛ حرق شعره أي تقطع ونسل فهو حرق الشعر والجناح (sihah)؛ حرق الشعر إذا انتشر (mufradat)
- **B005** koşuda atılganlık veya yoğun şimşek [kalıp] — koşuda çok atılgan at · çok şimşekli bulut
  فرس حراق إذا كان يتحرق في عدوه؛ سحاب حرق إذا كان شديد البرق (maqayis)؛ سحاب حرق أي شديد البرق؛ فرس حراق العدو إذا كان يحترق في عدوه (sihah)
- **B006** cinsel birleşme — cinsel birleşme; bir anlatımda yan yatarak birleşme · dar yapılı kadın
  المحارقة جنس من المباضعة (maqayis)؛ المحارقة المباضعة على الجنب (ayn)؛ الحارقة من النساء الضيقة؛ المحارقة المجامعة (sihah)
- **B007** kalça eklemi bağı — kalçada, uyluk kemiği başı çevresindeki bağ veya sinir · iki kalçadaki uyluk kemiği başları veya bağlar · kalça bağı kopmuş veya kalçası yerinden çıkmış kimse
  الحارقة وهي العصب الذي يكون في الورك؛ رجل محروق إذا انقطعت حارقته (maqayis)؛ الحارقة عصبة بين وابلة الفخذ التي تدور في صدفة الورك؛ حرق الرجل فهو محروق (ayn)؛ الحارقتان رؤوس الفخذين في الوركين؛ عصبتان في الورك؛ المحروق الذي انقطعت حارقته أو زال وركه (sihah)
- **B008** ateş yakma aracı ve ateş atan savaş gemisi — ateş tutuşturma aracı veya kıvılcımın düştüğü ateşlik · ateş tutuşturmaya yarayan şey · ateş tutuşturma aracının başka bir adı · ateşli atış düzenekleri taşıyan savaş gemisi
  الحروقاء هذا الذي يقال له الحراق (maqayis)؛ الحروق والحراق ما يورى به النار؛ الحراقات سفن فيها مرامي نيران (ayn)؛ الحراق والحراقة ما تقع فيه النار عند القدح؛ الحراقة سفن فيها مرامي نيران (sihah)
- **B009** çorbadan koyu yemek — çorbadan daha koyu kıvamlı yemek · çorbadan daha koyu kıvamlı yemekler
  الحريقة أغلظ من الحساء؛ ما لهم عيش إلا الحرائق (sihah)

## ع م ل (root_001046): 85:11 وَعَمِلُوا۟

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

## ص ل ح (root_000876): 85:11 ٱلصَّٰلِحَٰتِ

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

## ج ن ن (root_000266): 85:11 جَنَّٰتٌ

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

## ج ر ي (root_000240): 85:11 تَجْرِى

- **B001** bir yol boyunca akıp, koşup ya da ilerleyerek gitme — hızlı ilerleyiş ve kendi yatağında akış · aktı, koştu ya da yol aldı · suyun akışı · at koşusu · akıtmak ya da harekete geçirmek · akış, gidiş yolu ya da koşu yeri · denizde yol alan gemi · gökte yol alan güneş · suyu akan pınar · denizde yol alan gemiler · çeşitli koşu biçimleri olan at · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  أصل واحد وهو انسياح الشيء (maqayis)؛ جرى الماء يجري جرية وجريا وجريانا (maqayis;sihah;mufradat)؛ الخيل تجري والرياح تجري والشمس تجري جريا (ayn;tahdhib)؛ الجارية السفينة والجارية الشمس (maqayis;sihah)
- **B002** alışılmış yol ve davranış düzeni — kişinin alışkanlık edindiği ve sürekli izlediği yol
  للعادة الإجريا (maqayis)؛ الإجريا طريقته التي يجري عليها من عادته (ayn)؛ الإجريا الجري والعادة مما تأخذ فيه (sihah)؛ الإجرياء الوجه الذي نأخذ فيه (tahdhib)؛ الإجريا العادة التي يجري عليها الإنسان (mufradat)
- **B003** başkası adına iş gören, haber götüren ya da güvence veren kimse — başkası adına iş gören, haber götüren ya da güvence veren kimse · başkası adına iş görecek birini tutmak · kötücül ayartıcının sizi kendi işi doğrultusunda sürüklemesine ya da kendine aracı kılmasına izin vermeyin
  الجري الوكيل (maqayis;tahdhib)؛ الجري الرسول (ayn;tahdhib;mufradat)؛ الجري الضامن (tahdhib)؛ استجريت أي اتخذت وكيلا (maqayis;sihah;tahdhib)؛ لا يستجرينكم الشيطان (maqayis;sihah;tahdhib;mufradat)
- **B004** genç kız ve ona bağlı genç kızlık çağı — genç kız ya da hizmette çalıştırılan genç kadın · genç kızlık çağı · genç kızlık durumu
  الجارية من النساء لأنها تستجرى في الخدمة (maqayis)؛ الجارية مصدرها الجراء (ayn)؛ جارية بينة الجراية والجراء (sihah;tahdhib)؛ أيام جرائها أي صباها (maqayis;ayn;sihah)
- **B005** kuş kursağı — 
  الجرية وهي الحوصلة أصلها قرية (maqayis)؛ الجرية مثل القرية هي الحوصلة (sihah)؛ الجرية والقرية والنوطة لحوصلة الطائر (tahdhib)؛ يقال للحوصلة جرية لأنها مجرى الطعام (mufradat)
- **B006** sürekli verilen geçimlik ya da kalıcı yarar — düzenli görev ödeneği · onun için sürekli verildi ya da sürüp gitti · ona sürekli olarak verdim · yararı süren bağış
  الجراية الجاري من الوظائف (sihah)؛ الأرزاق جارية والأعطيات دارة (tahdhib)؛ جرى عليه ذلك الشيء ودر له بمعنى دام له (tahdhib)؛ أجريت له كذا أي أدمت له (tahdhib)؛ صدقة جارية (tahdhib)
- **B007** birlikte ilerleyip birbirine ayak uydurma — yanında koşmak ya da ona ayak uydurmak · söyleşide ona ayak uydurmak ve karşılık vermek
  جاراه مجاراة وجراء أي جرى معه (sihah)؛ جاراه في الحديث وتجاروا فيه (sihah)
- **B008** senin yüzünden ya da senin için — senin yüzünden ya da senin için
  فعلت ذلك من جراك ومن جرائك أي من أجلك (sihah)

## ت ح ت (root_000177): 85:11 تَحْتِهَا

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ن ه ر (root_001559): 85:11 ٱلْأَنْهَٰرُ

- **B001** bol su taşıyan doğal akarsu yatağı — taşkın suyun aktığı doğal akarsu yatağı · akarsu yatakları · akarsular veya akarsu yatakları · akarsu yatağı sağlam bir güzergah edindi · su aktı ve kendine bir yatak açtı · bol sulu veya geniş akarsu · suyun kazıp açtığı yatak yeri · kuyu kazısı suya ulaştı
  النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)
- **B002** şafaktan gün batımına aydınlık gündüz — şafaktan güneş batımına kadar süren aydınlık gündüz · aydınlık gündüz süreleri · gündüz vaktinde baskın yapan kimse · gündüzün aydınlığına girdik
  النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)
- **B003** bir şeyi açma veya genişletme — genişlik veya aydınlıkla birlikte genişlik · kanı açıp serbest bırakarak akıttı · yaranın veya yarığın açıklığını genişletti · genişledi · evlerin önleri arasında atık bırakılan açık alan · bağırsağı çözüldü ve akarsu gibi boşaldı · tehlikeler; birleşik bir türetme olarak açıklanan biçim
  أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)
- **B004** sert sözle azarlayıp engelleme [kalıp] — onu sert sözle azarlayıp engelledi
  نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)
- **B005** bazı kuşların yavrusu — türü aktarıma göre değişen bir kuş yavrusu
  النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)
- **B006** fırsat kollayıp gizlice kapma — fırsat kollayıp ani biçimde gizlice kapma
  النهر الدغرة وهي الخلسة (tahdhib)
- **B007** kişi, yer ve yıldızlara ait özel adlar — belirli bir topluluktan bir şairin adı · bir yer adı · sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad
  نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)
- **B008** bulut — bulut
  الناهُور السحاب (tahdhib)

## ف و ز (root_001186): 85:11 ٱلْفَوْزُ

- **B001** iyiliğe erişip kötülükten kurtulma — iyiliğe erişip kötülükten kurtulma · kurtulup iyiliğe erişmek · kurtulup iyiliğe erişen kimse · bir şeyi ele geçirip onunla uzaklaşmak · Tanrı'nın ona bir şeyi alıp götürtmesi · kumarda kura payının sahibine çıkması
  الفوز الظفر بالخير والنجاة من الشر (ayn;sihah;tahdhib;mufradat)؛ فاز بالأمر إذا ذهب به وخلص (maqayis;sihah)؛ إذا خرج قدح قوم في القمار قيل قد فاز (ayn;tahdhib)
- **B002** ölüp dünyadan ayrılma — ölmek, yaşamını yitirmek
  فوز الرجل إذا مات (maqayis;sihah;tahdhib)؛ فوز الرجل إذا هلك (mufradat)؛ صار في مفازة بين الدنيا والآخرة (ayn;tahdhib)
- **B003** kurtuluş; susuz ve tehlikeli ıssız çöl — susuz çöle girip orada yol almak · cezadan kurtuluş · susuz, ölüm tehlikesi taşıyan ıssız çöl · kurtuluş veya kurtuluş yeri
  المفازة المنجاة (maqayis;ayn;sihah;tahdhib)؛ المفازة الفلاة التي لا ماء فيها (tahdhib)؛ سميت مفازة تفاؤلا بالسلامة والفوز (maqayis;sihah;mufradat)؛ سميت من فوز إذا هلك (maqayis;sihah;mufradat)؛ فوز الرجل تفويزا ركب المفازة ومضى فيها (ayn;tahdhib)
- **B004** askerî konak yerinde kurulan yapı veya direkli gölgelik — askerî konak yerinde kurulan yapı veya direkli gölgelik
  الفازة من أبنية الحزق وغيرها تبنى في العساكر (ayn;tahdhib)؛ الفازة مظلة تمد بعمود (sihah)

## ك ب ر (root_001281): 85:11 ٱلْكَبِيرُ

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

## ب ط ش (root_000126): 85:12 بَطْشَ

- **B001** ezici güç ve zor kullanarak sertçe ele alma — ezici güçle sertçe ele alma · onu zor kullanarak sertçe ele almak · zor kullanılarak yapılan sert bir ele alış · güçle kavrayan ve zor kullanan el · zor kullanarak ele almada çok güçlü · ona karşı ezici güçle sertçe mücadele etmek · öfkeyle kırbaç ya da kılıç kullanarak vurmak veya öldürmek
  أخذ الشيء بقهر وغلبة وقوة؛ يد باطشة (maqayis)؛ البطش التناول عند الصولة؛ الأخذ الشديد في كل شيء؛ ذو البأس والأخذ لأعدائه (ayn)؛ بطش يبطش بطشا وهو الأخذ الشديد؛ رجل شديد البطش (jamhara)؛ البطشة السطوة والأخذ بالعنف؛ باطشه مباطشة (sihah)؛ البطش التناول عند الصولة؛ تقتلون عند الغضب؛ بالسوط والسيف (tahdhib)؛ البطش تناول الشيء بصولة؛ يد باطشة (mufradat)

## ر ب ب (root_000532): 85:12 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 85:12 رَبِّكَ: withheld observed target; not identity

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

## ش د د (root_000782): 85:12 لَشَدِيدٌ

- **B001** bağlayıp sağlamlaştırma — bir şeyi bağlayıp sağlamlaştırmak · gücüne güç katmak, desteklemek · Tanrı onun yönetimini güçlendirsin
  شددت العقد شدا (maqayis)؛ شد الحبل أو غيره (jamhara)؛ شده أي أوثقه (sihah)؛ شددت الشيء إذا أوثقته (tahdhib)؛ الشد العقد القوي وقويت عقده (mufradat)؛ شد عضده أي قواه (sihah)؛ شد الله ملكه وشدده أي قواه (sihah)؛ اشدد به أزرى (tahdhib)
- **B002** güç, katılık ve çetinlik — güç, katılık, dayanıklılık ve çetinlik · güçlü ve yürekli · ağır sıkıntı, çetin sınanma · büyük sarsıntılar ve ağır sıkıntılar · artırma ve ağırlaştırma · bir konuda çok sıkı davranma · hiçbir şeye gücü yetmemek · şarkı söylerken sesini yükseltmek için var gücünü kullanmak · güçlü bir bineğe sahip olmak · güçlü ve sert
  أصل واحد يدل على قوة في الشيء (maqayis)؛ الشدة الصلابة والنجدة وثبات القلب والمجاعة (ayn;tahdhib)؛ الشدة القوة في الجسم وصعوبة الزمن (jamhara)؛ الشدة القوة والجلادة والشديد الرجل القوي (tahdhib)؛ الشدة تستعمل في العقد وفي البدن وفي قوى النفس وفي العذاب (mufradat)؛ أصابتني شدى أي شدة (maqayis;sihah;tahdhib)؛ التشديد خلاف التخفيف (sihah)؛ ما أملك شدا ولا إرخاء لا أقدر على شيء (tahdhib)؛ تشددت القينة إذا جهدت نفسها (tahdhib)؛ كانت دوابهم شدادا وأشد الرجل إذا كانت معه دابة شديدة (maqayis;sihah)
- **B003** saldırıya atılma ve hızla koşma — düşmanın üzerine saldırmak · koşma, hızlı koşu · koşmak, hızla ilerlemek · tek bir saldırı hamlesi
  في الحرب أيضا يشد شدا (maqayis)؛ الشد الحمل وشد عليه في القتال (ayn;tahdhib)؛ شد على العدو إذا حمل عليه (jamhara;sihah)؛ الشد العدو والفعل اشتد (ayn;sihah)؛ الشد الحضر والفعل اشتد (tahdhib)؛ شد فلان على العدو شدة واحدة وشد شدات كثيرة (tahdhib)
- **B004** güç ve sağduyu bakımından olgunluğa erişme — güç, sağduyu ve deneyimin olgunluk düzeyi
  الأشد العشرون ويقال أربعون سنة (maqayis)؛ الأشد مبلغ الرجل الحنكة والمعرفة (ayn;tahdhib)؛ بلغ الرجل أشده والواحد شد (jamhara)؛ حتى يبلغ أشده أي قوته (sihah)؛ معناه الإدراك والبلوغ وأن يؤنس منه الرشد مع أن يكون بالغا (tahdhib)؛ يجتمع أمره وقوته ويكتهل وينتهي شبابه (tahdhib)
- **B005** günün ilerleyip yükselmesi [kalıp] — günün ilerleyip yükselmesi
  شد النهار ارتفاعه (maqayis;sihah)
- **B006** eli sıkılık — eli sıkı · eli sıkı
  الشديد والمتشدد البخيل (maqayis)؛ المتشدد البخيل (sihah)؛ لشديد أي لبخيل (tahdhib)

## ب د ء (root_000090): 85:13 يُبْدِئُ

- **B001** baslatma ve baslangic noktasi yapma — bir seyle baslamak, onu one almak · bir seyi ilk olarak yapmak veya var etmek · baslama ve bir seyi baskasindan once getirme · bir seyin kuruldugu veya meydana geldigi kaynak · bir seyi baslatan veya ilk var edis noktasini kuran
  من افتتاح الشيء يقال بدأت بالأمر وابتدأت من الابتداء (maqayis)؛ بدأت بالشئ بدءا ابتدأت به وبدأت الشئ فعلته ابتداء (sihah)؛ بدأت بكذا وأبدأت وابتدأت أي قدمت والبدء والابتداء تقديم الشيء على غيره ومبدأ الشيء هو الذي منه يتركب أو منه يكون (mufradat)
- **B002** baslatip yeniden yapmak — once baslatir, sonra yeniden yapar · donus ve baslangic halinde yapmak · geldigi yoldan geri donmek · ne baslangic sozu ne de donus sozu soylemek
  والله تعالى المبدئ والبادئ وهو يبدئ ويعيد (maqayis)؛ فعل ذلك عودا وبدءا ورجع عوده على بدئه وما يبدئ وما يعيد (sihah)؛ الله هو المبدئ المعيد ورجع عوده على بدئه وفعل ذلك عائدا وبادئا ومعيدا ومبدئا (mufradat)
- **B003** once gelen ve once baslama hakki — once anilan onde gelen bey · baskalarindan once baslama hakki sende · ilk basta, en basta
  يقال للسيد البدء لأنه يبدأ بذكره (maqayis)؛ البدء السيد الأول في السيادة والبدء والبدئ أيضا الأول ولك البدء والبدأة أي لك أن تبدأ قبل غيرك (sihah)؛ يقال للسيد الذي يبدأ به إذا عد السادات بدء (mufradat)
- **B004** sira disi yeni sey — sasirtici veya sira disi is · sira disi bir sey getirmek · daha once alisilmamis sey
  يقال للأمر العجب بدي كأنه من عجبه يبدأ به (maqayis)؛ البدئ الأمر البديع وقد أبدأ الرجل إذا جاء به (sihah)؛ شيء بديء لم يعهد من قبل كالبديع في كونه غير معمول قبل (mufradat)
- **B005** bir yerden baska yere cikmak [kalıp] — bir yerden baska bir yere cikmak
  أبدأت من أرض إلى أخرى أبدئ إبداء إذا خرجت منها إلى غيرها (maqayis)؛ أبدأت من أرض كذا أي ابتدأت منها بالخروج (mufradat)
- **B006** pay ve buyuk et parcasi — paylasimda ayrilan pay veya hayvan payi · buyuk et parcasi · hayvan payi anlamindaki cogul bicimler
  البدأة النصيب وهو من هذا أيضا لأن كل ذي نصيب فهو يبدأ بذكره (maqayis)؛ البدء والبدأة النصيب من الجزور والجمع أبداء وبدوء (sihah)؛ البدأة النصيب المبدأ به في القسمة ومنه قيل لكل قطعة من اللحم عظيمة بدء (mufradat)
- **B007** parmak eklemleri — cikintili parmak eklemleri
  البدوء مفاصل الأصابع واحدها بدء وأظنه مما همز وليس أصله الهمز وإنما سميت بدوءا لبروزها وظهورها (maqayis)
- **B008** sonradan kazilmis kuyu — sonradan kazilmis, eski olmayan kuyu
  البدء والبدئ البئر التى حفرت في الإسلام وليست بعادية وفي الحديث حريم البئر البدئ خمس وعشرون ذراعا (sihah)
- **B009** ilk ham gorus — ilk beliren, olgunlasmamis gorus
  بادئ الرأي أي ما يبدأ من الرأي وهو الرأي الفطير وقرئ بادي بغير همزة أي الذي يظهر من الرأي ولم يرو فيه (mufradat)
- **B010** dokuntulu hastaliga tutulmak — cicek hastaligi veya kizamik tutmak
  قولهم بدئ فهو مبدوء إذا جدر أو حصب (maqayis)؛ بدئ الرجل يبدأ بدءا فهو مبدوء إذا أخذه الجدري أو الحصبة (sihah)

## ب د ء (root_000091): 85:13 يُبْدِئُ

- **B001** baslatmak ve ilk var etmek — ise basladim · baslamaya girismek · bir seyi baslatan · bir seye ilk baslayan · baslatir ve yeniden yapar · yaratmayi ilk baslatmak
  من افتتاح الشيء يقال بدأت بالأمر وابتدأت من الابتداء؛ المبدئ والبادئ؛ يبدئ ويعيد؛ كيف بدأ الخلق
- **B002** sasilacak sey — saskinlik uyandiran is veya sey
  ويقال للأمر العجب بدي كأنه من عجبه يبدأ به؛ فلا بدي ولا عجيب
- **B003** adi once anilan bey — ustun oldugu icin adi once anilan bey
  ويقال للسيد البدء لأنه يبدأ بذكره؛ ترى ثنانا إذا ما جاء بدأهم
- **B004** once anilan pay — oneminden dolayi once anilan pay
  والبدأة النصيب؛ لأن كل ذي نصيب فهو يبدأ بذكره دون غيره وهو أهمها إليه
- **B005** bir yerden baska yere cikmak [kalıp] — bir yerden baska bir yere cikmak
  وتقول أبدأت من أرض إلى أخرى أبدئ إبداء إذا خرجت منها إلى غيرها
- **B006** cikintili parmak eklemleri — cikintili parmak eklemleri · parmak eklemlerinden biri
  والبدوء مفاصل الأصابع واحدها بدء؛ وأظنه مما همز وليس أصله الهمز؛ سميت بدوءا لبروزها وظهورها

## ع و د (root_001058): 85:13 وَيُعِيدُ

- **B001** geri dönme ve yeniden yapma — geri dönmek · geri dönüş; yeniden yönelme · bir şeyi yeniden yapmak veya yinelemek · bir şeyin yeniden yapılmasını istemek · önceki işe yeniden dönmek · aynı soruyu tekrar tekrar sormak · ateşi yeniden nüksetmek · önceden yenmişken yeniden sunulan yemek · sık sık dönen; geri dön buyruğu
  أصل يدل على تثنية في الأمر (maqayis)؛ بدأ ثم عاد (maqayis;ayn)؛ عاد إليه يعود عودة وعودا رجع (sihah)؛ العود الرجوع إلى الشيء بعد الانصراف عنه (mufradat)؛ استعدته الشيء فأعاده (sihah)؛ تعاود القوم في الحرب وغيرها (sihah)؛ عاودته الحمى وعاوده بالمسألة (sihah)؛ عواد بمعنى عد (sihah)؛ العوادة ما أعيد من الطعام (sihah)
- **B002** dönüş yeri ve son varış — son varış; dönüş zamanı veya yeri
  المعاد كل شيء إليه المصير (maqayis)؛ والآخرة معاد للناس (maqayis)؛ الحج معاد الحاج (ayn)؛ لرادك إلى معاد يعني مكة (ayn)؛ المعاد المصير والمرجع (sihah)؛ الآخرة معاد الخلق (sihah)؛ المعاد يقال للعود وللزمان الذي يعود فيه وقد يكون للمكان الذي يعود إليه (mufradat)
- **B003** tek söz söylememek — ne söze başlamak ne de karşılık vermek
  رأيت فلانا ما يبدئ وما يعيد أي ما يتكلم ببادية ولا عادية (ayn)؛ ما يبدئ وما يعيد أي ما يتكلم ببادئة ولا عائدة (maqayis)
- **B004** tekrarla alışkanlık ve yatkınlık kazanma — alışkanlık; tekrarla yerleşen davranış · alışmak; alışkanlık edinmek · ısrarla sürdüren; deneyimli · alıştığı için yapabilen · çiftleşmeye alışmış erkek hayvan
  العادة الدربة والتمادي في شيء حتى يصير له سجية (maqayis;ayn)؛ المواظب على الشيء المعاود (maqayis;ayn)؛ بطل معاود (maqayis;ayn)؛ العادة معروفة والجمع عاد وعادات (sihah)؛ عاده واعتاده وتعوده (sihah)؛ عود كلبه الصيد فتعوده (sihah)؛ فلان معيد لهذا الأمر أي مطيق له (sihah;ayn)؛ المعيد الفحل الذي قد ضرب في الإبل مرات (sihah)؛ العادة اسم لتكرير الفعل والانفعال حتى يصير ذلك سهلا (mufradat)
- **B005** hasta veya yas ziyareti — hasta ziyareti · hasta ziyaretçileri · insanların ziyaret ettiği felaket veya yas hâli
  العيادة أن تعود مريضا (maqayis)؛ عدت المريض أعوده عيادة (sihah)؛ من العود عيادة المريض (mufradat)؛ الرجال عواد المريض والنساء عود (ayn)؛ فلان في معادة أي مصيبة يغشاه الناس (ayn)؛ لآل فلان معادة أي أمر يغشاهم الناس له (maqayis)
- **B006** kişiye dönen yarar ve iyilik — kişiye ulaşan yarar, şefkat veya bağış · bu senin için daha yararlı veya elverişlidir · iyilik yaptıktan sonra iyiliğini artırdı
  عاد فلان بمعروفه إذا أحسن ثم زاد (ayn)؛ العائدة وهو المعروف والصلة (maqayis)؛ ما أكثر عائدة فلان علينا (maqayis)؛ العائدة العطف والمنفعة (sihah)؛ هذا الشيء أعود عليك من كذا أي أنفع (sihah)؛ هذا الأمر أعود عليك أي أرفق بك (tahdhib)؛ العائدة اسم ما عاد به عليك المفضل من صلة أو فضل (tahdhib)؛ العائدة كل نفع يرجع إلى الإنسان (mufradat)
- **B007** yeniden gelen özel gün veya hâl — bayram; tekrarlanan toplanma veya sevinç günü · kişiye yeniden gelen kaygı, sevgi veya hâl · bayrama katılmak
  العيد ما يعتاد من خيال أو هم (maqayis)؛ العيد كل يوم مجمع (maqayis)؛ لأنه يعود كل عام (maqayis)؛ عيد قد مضى ذكره في محله لأن ذلك هو الأصل (maqayis-crossref)؛ العيد ما اعتادك من هم أو غيره (sihah)؛ العيد واحد الأعياد (sihah)؛ وقد عيدوا أي شهدوا العيد (sihah)؛ العيد ما يعاود مرة بعد أخرى (mufradat)؛ يستعمل العيد في كل يوم فيه مسرة (mufradat)
- **B008** gücü kalmış yaşlı deve — gücü kalmış yaşlı deve · yaşlı dişi deve veya koyun · ileri yaşa ulaşmak · savaşta yaşlı ve deneyimli kişilerden yardım al
  الجمل المسن فهو يسمى عودا (maqayis)؛ كأنه عاود الأسفار والرحل مرة بعد مرة (maqayis)؛ العود الجمل المسن وفيه سورة أي بقية (ayn)؛ العود المسن من الإبل (sihah)؛ زاحم بعود أو دع (sihah)؛ العود الجمل المسن الذي فيه بقية قوة (tahdhib)؛ عود الرجل تعويدا إذا أسن (tahdhib)؛ لا يقال عود إلا لبعير أو لشاة (tahdhib)؛ أنثى عودة (tahdhib)؛ البعير المسن اعتبارا بمعاودته السير والعمل (mufradat)
- **B009** eski yol ve köklü geçmiş — eski ve yeniden kullanılan yol · köklü saygınlık · eski akrabalık bağı
  العود الطريق القديم (ayn)؛ رحم عودة يعني قديمة (ayn)؛ السودد العود (maqayis)؛ الطريق القديم عود (maqayis)؛ العود الطريق القديم (sihah)؛ سودد عود أي قديم (sihah)؛ طريق عود إذا كان عاديا (tahdhib)؛ العود الطريق القديم الذي يعود إليه السفر (mufradat)
- **B010** tahta parçası, tütsülük odun veya telli çalgı — tahta parçası veya ince dal · tütsü için yakılan kokulu odun · telli müzik aleti
  الأصل الآخر فالعود وهو كل خشبة دقت (maqayis)؛ كل خشبة عود (maqayis)؛ العود الذي يتبخر به معروف (maqayis)؛ العود بالضم من الخشب واحد العيدان والأعواد (sihah)؛ العود الذي يضرب به (sihah)؛ العود الذي يتبخر به (sihah)؛ العود في الأصل الخشب الذي من شأنه أن يعود إذا قطع (mufradat)؛ خص بالمزهر المعروف وبالذي يتبخر به (mufradat)
- **B011** bağlayıcı eş sözünden ilgili davranışa dönüş — eş hakkındaki bağlayıcı sözden sonra ilgili davranışa dönmek
  ثم يعودون لما قالوا (mufradat)؛ عند أهل الظاهر هو أن يقول للمرأة ذلك ثانيا (mufradat)؛ عند أبي حنيفة العود في الظهار هو أن يجامعها (mufradat)؛ عند الشافعي هو إمساكها (mufradat)؛ يحمل على فعل ما حلف له أن لا يفعل (mufradat)
- **B012** biçime bağlı adlandırmalar — eski bir kavmin adı · eski; eski bir kavme bağlanan · erkek adı · bir kavme veya erkek deveye bağlanan soylu develer
  عاد قبيلة وهم قوم هود (sihah)؛ شيء عادي أي قديم كأنه منسوب إلى عاد (sihah)؛ عادياء اسم رجل (sihah)؛ العيدية نجائب منسوبة قالوا نسبت إلى عاد (maqayis)؛ العيدية إبل منسوبة إلى فحل يقال له عيد (mufradat)

## غ ف ر (root_001096): 85:14 ٱلْغَفُورُ

- **B001** koruyucu biçimde örtme — örtme ve koruyucu biçimde kaplama · başı koruyan zincir örgülü zırh başlığı · baş yağı bulaşmasın diye başörtüsünün altına konan bez · yay kirişinin geçtiği çentiği örten yama · alttaki bulutu örten üst bulut · eşyayı bir kaba koymak · boyanın kumaşı kiri daha iyi gizler duruma getirmesi · işi gereken biçimde örtüp düzeltmek · enseden sarkan saçı örtmek
  الغفر الستر (maqayis)؛ أصل الغفر التغطية (ayn)؛ الغفر: التغطية (sihah)؛ الغفر: إلباس ما يصونه عن الدنس (mufradat)؛ المغفر وقاية للرأس (ayn)؛ المغفر: زرد ينسج من الدروع على قدر الرأس (sihah)؛ اغفروا هذا الأمر بغفرته أي استروه بما يجب أن يستر به (mufradat)
- **B002** suçu bağışlayıp cezadan koruma — suçu bağışlama ve ceza sonucundan koruma · suçu bağışlayıp cezasını kaldırma · Tanrı'nın suçu bağışlayıp kulunu cezadan koruması · suçu bağışlama · Tanrı'nın onun suçunu bağışlaması · onu bağışlamak · Tanrı'dan bağışlanma dilemek · suçu bağışlamak · çok bağışlayan · sürekli ve çok bağışlayan · içlerinde kimsenin suçunu bağışlayan yok
  الغفران والغفر بمعنى (maqayis)؛ الله الغفور الغفار يغفر الذنوب مغفرة وغفرانا وغفرا (ayn)؛ استغفر الله لذنبه ومن ذنبه فغفر له ذنبه مغفرة وغفرا وغفرانا (sihah)؛ المغفرة من الله هو أن يصون العبد من أن يمسه العذاب (mufradat)
- **B003** yüzeyi kaplayan ince tüy veya kumaş havı — kumaşın havı kalkıp yüzünü kaplamak · kumaş havı ya da bedendeki ince tüy · ince tüy · enseden aşağı sarkan saç · enseden sarkan saçı örtmek
  غفر الثوب إذا ثار زئبره وهو من الباب لأن الزئبر يغطي وجه الثوب (maqayis)؛ غفر الثوب إذا ثار زئبره غفرا (ayn)؛ الغفر أيضا شعر كالزغب يكون على ساق المرأة والجبهة ونحو ذلك؛ والغفر أيضا زئبر الثوب (sihah)
- **B004** yaranın veya hastanın yeniden kötüleşmesi [kalıp] — yara yeniden kötüleşti · hasta yeniden kötüleşti
  الغفر النكس في المرض (maqayis)؛ غفر الجرح يغفر غفرا: نكس، وكذلك المريض (sihah)
- **B005** dağ keçisi yavrusu ve annesi — dağ keçisi yavrusu · yavrunun annesi olan dişi dağ keçisi · dağ keçisi yavrusunun annesi
  الغفر ولد الأروية وأمه مغفر (maqayis)؛ الغفر ولد الأروية؛ والمغفر الأروية ويقال لها أم غفر (ayn)؛ الغفر بالضم: ولد الأروية، والجمع الأغفار، وأمه مغفرة (sihah)
- **B006** Ay'ın konaklarından olan üç küçük yıldız — Ay'ın konaklarından olan üç küçük yıldız
  الغفر من منازل القمر (ayn)؛ الغفر: ثلاثة أنجم صغار ينزلها القمر، وهي من الميزان (sihah)
- **B007** ağaçtan çıkan veya toplanan ürün — ağaçtan çıkan ürün; reçine benzeri madde veya tatlı kurt · ağaçtan çıkan ve toplanan ürünler · ağaç ürünlerini aramaya çıkmak · ağaç ürünü toplamaya çıkmak
  المغفور فشىء يشبه بالصمغ يخرج من العرفط (maqayis)؛ المغفور دود يخرج من العرفط حلو يضيح بالماء فيشرب؛ وصمغ الإجاصة مغفور (ayn)؛ ما أحسن مغافير هذا الرمث؛ خرجنا نتمغفر؛ خرجنا نتغفر، إذا خرجوا يجتنونه من شجرة (sihah)
- **B008** bütün topluluğun kalabalık ve eksiksiz gelişi [kalıp] — bütün topluluk, kalabalık ve kimse eksik olmadan · bütün toplulukla birlikte · hep birlikte ve kalabalık olarak
  جاء القوم جماء الغفير أي بلفهم ولفيفهم (ayn)؛ جاءوا جماء غفيراء؛ والجماء الغفير، وجم الغفير، وجماء الغفير، أي جاءوا بجماعتهم: الشريف والوضيع، ولم يتخلف أحد، وكانت فيهم كثرة (sihah)

## و د د (root_001634): 85:14 ٱلْوَدُودُ

- **B001** sevgi ve gönülden yakınlık besleme — bir kişiyi sevmek ve ona gönülden yönelmek · sevgi ve gönülden yakınlık · sevgi ve gönülden yakınlık · birinin sevgi bağı kurduğu kişi · çok seven kişi veya sevenlerden biri · çok seven ve sevgi gösteren · birbirini sevmek ve karşılıklı sevgi beslemek · sevgi ve yakınlık · sevgi ve yakınlık · yazılı ileti ya da sevgiyi doğuran öğüt benzeri bir araç
  كلمة تدل على محبة؛ وددته أحببته؛ الود من الوداد (maqayis;jamhara)؛ الود والود والود: المودة؛ ووددت الرجل إذا أحببته؛ الودود: المحب (sihah)؛ الود مصدر للمودة وكذلك الوداد؛ يقال في الحب الود والود والمودة والموددة؛ المودة: الكتاب (tahdhib)؛ الود: محبة الشيء؛ بأسباب المحبة من النصيحة ونحوها؛ فلان وديد فلان: مواده (mufradat)
- **B002** bir şeyin gerçekleşmesini dilemek — bir şeyin gerçekleşmesini dilemek · dileme ve istek · şöyle olmasını isterim
  ووددت أن ذاك كان إذا تمنيته؛ في التمني الودادة (maqayis)؛ وددت لو تفعل ذاك أي تمنيت (sihah)؛ الودادة مصدر وددت أود وهو من الأمنية؛ يود أحدهم لو يعمر أي يتمنى (tahdhib)؛ وتمني كونه؛ التمني هو تشهي حصول ما توده (mufradat)
- **B003** bölgesel söyleyişte kazık — kazık; bölgesel söyleyişte kaynaşmış biçim
  فأما الود فالوتد (maqayis)؛ الود لغة تميمية وهو الوتد (jamhara)؛ الود بالفتح الوتد في لغة أهل نجد كأنهم سكنوا التاء فأدغموها في الدال (sihah)؛ الود بلغة تميم الوتد (tahdhib)؛ الود: الوتد، وأصله يصح أن يكون وتد فأدغم (mufradat)
- **B004** dağ veya vadi özel adı — bilinen bir dağın özel adı · bilinen bir vadinin özel adı
  الود: جبل معروف؛ وودان: واد معروف (jamhara)؛ هو اسم جبل (sihah)
- **B005** bir putun özel adı — maddede anılan putun özel adı · bu putun adına bağlanan kişi adı
  وود: صنم هكذا فسر في التنزيل؛ وقد قالوا ود أيضا (jamhara)؛ وود: صنم كان لقوم نوح ثم صار لكلاب (sihah)؛ الود صنم كان لقوم نوح، وكان لقريش صنم يدعونه ودا؛ ومنه سمي عبد ود (tahdhib)؛ الود: صنم سمي بذلك (mufradat)

## ع ر ش (root_001000): 85:15 ٱلْعَرْشِ

- **B001** hükümdar tahtı ve yönetim makamı — hükümdarın tahtı ve yönetim makamı · insanın gerçek niteliğini bilemediği, yalnız adını bildiği Tanrı tahtı
  العرش سرير الملك (maqayis;sihah)؛ العرش في كلام العرب سرير الملك (tahdhib)؛ سمي مجلس السلطان عرشا (mufradat)؛ عرش الله ما لا يعلمه البشر إلا بالاسم (mufradat)
- **B002** üstü örtülü barınak ve gölgelik — evin tavanı · altında gölgelenilen üstü örtülü yapı · çubuklardan yapılıp üstü gölgelenen evler · hayvanları soğuktan koruyan çevrili barınak
  كل بناء يستظل به عرش وعريش (maqayis)؛ العرش سقف البيت (sihah;tahdhib)؛ العرش والعريش ما يستظل به (sihah;tahdhib)؛ العرش في الأصل شيء مسقف (mufradat)؛ عروش مكة بيوتها (sihah;tahdhib)؛ الحظيرة التي تسوى للماشية تكنها من البرد عريش (tahdhib)
- **B003** asmaya çardak kurma ve asmanın çardağa tırmanması — asmaya çardak kurup onu desteğe almak · üzüm asmasının çardağın üzerine tırmanması · çardak üzerinde yetiştirilen asmalar
  تعريش الكرم لأنه رفعه والتوثق منه (maqayis)؛ عرشت الكرم بالعروش تعريشا (sihah;tahdhib)؛ عرشت الكرم إذا جعلت له كهيئة سقف (mufradat)؛ اعترش العنب إذا علا على العراش (sihah)؛ اعترش العنب العريش إذا علاه (tahdhib)
- **B004** kuyuyu ahşapla kaplama ve ağız platformu kurma — kuyunun ahşap kaplaması ve ağız üstü çalışma yeri · altı taşla, geri kalanı ahşapla örülmüş kuyu
  عرش البئر طيها بالخشب (maqayis;sihah)؛ العرش الذي يكون على فم البئر يقوم عليه الساقي (maqayis)؛ بئر معروشة وهي التي تطوى قدر قامة من أسفلها بالحجارة ثم يطوى سائرها بالخشب (tahdhib)؛ عرشت البئر جعلت له عريشا (mufradat)
- **B005** deve üzerindeki örtülü kadın taşıma bölmesi — kadının deve üzerinde oturduğu örtülü taşıma bölmesi
  العريش شبه الهودج يتخذ للمرأة تقعد فيه على بعيرها (maqayis;sihah;tahdhib)؛ العرش شبه هودج للمرأة شبيها في الهيئة بعرش الكرم (mufradat)
- **B006** işin, iktidarın ve saygınlığın dayanağı — kişinin işini ayakta tutan dayanak · işi çöktü, iktidarı ve saygınlığı sona erdi · iktidar, yönetme gücü ve saygınlık
  قيل لأمر الرجل وقوامه عرش وإذا زال ذلك عنه قيل ثل عرشه (maqayis)؛ ثل عرشه أي وهى أمره وذهب عزه (sihah)؛ العرش الملك يقال ثل عرشه أي زال ملكه وعزه (tahdhib)؛ كني به عن العز والسلطان والمملكة قيل فلان ثل عرشه (mufradat)
- **B007** boyun yanları, ayak üstü ve bunlara bağlı beden adları — boynun iki yanındaki uzun etli bölümler · ayağın parmaklarla orta çıkıntı arasındaki üst bölümü · boyun yanlarına komşulukla aynı ad verilen iki kulak · at yelesindeki kılların son bölümü · iki yanı iri ve geniş deve
  العرش عرش العنق عرشان بينهما الفقرا وفيهما الأخدعان (maqayis)؛ العرش في القدم ما بين العير والأصابع من ظهر القدم (maqayis)؛ العرش بالضم أحد عرشي العنق (sihah)؛ للعنق عرشان بينهما القفا وفيهما الأخدعان (tahdhib)؛ ظهر القدم العرش وباطنه الأخمص (tahdhib)؛ الأذنان تسميان عرشين لمجاورتهما العرشين (tahdhib)؛ العرشان من الفرس آخر شعر العرف (tahdhib)
- **B008** Simak'ın Arşı ve Süreyya'nın Arşı diye anılan iki özel yıldız grubu — Simak'ın Arşı adıyla Avva'nın altında bulunan ve Aslan'ın arka kısmı sayılan dört küçük yıldız · Süreyya'nın Arşı adıyla Süreyya yakınındaki yıldızlar
  عرش السماك أربعة كواكب أسفل من الغواء (maqayis)؛ عرش السماك أربعة كواكب صغار أسفل من العواء (sihah)؛ عرش الثريا كواكب قريب منها (tahdhib)
- **B009** sürüsüne yöneltilen eşeğin başını kaldırıp ağzını açması [kalıp] — eşeğin sürüsüne yönelince başını kaldırıp ağzını açması
  إذا حمل الحمار على العانة رافعا رأسه شاحيا فاه قيل عرش بعانته تعريشا (maqayis)؛ عرش الحمار بعانته تعريشا إذا حمل عليها ورفع رأسه وشحا فاه (sihah)؛ عرش الحمار بعانته تعريشا وذلك إذا حمل على عانته فرفع رأسه شاخسا فاه (tahdhib)
- **B010** koyunların otlamasını engelleme — koyunların otlamasını engelleme
  الإعراش أن تمنع الغنم أن ترتع وقد أعرشتها إذا منعتها أن ترتع (tahdhib)
- **B011** bineğin üzerine çıkıp binme [kalıp] — bineğin üzerine çıkıp binmek
  اعروشت الدابة واعترشته وتعروشته إذا ركبته (tahdhib)
- **B012** bir yerde sabit kalıp yerleşme [kalıp] — bir ülkede sabit kalıp yerleşmek
  تعرشنا ببلاد كذا أي ثبتنا وتعرش فلان بها (tahdhib)

## م ج د (root_001398): 85:15 ٱلْمَجِيدُ, 85:21 مَّجِيدٌ

- **B001** cömertlik, onur ve yücelikte doruk — cömertlik, onur ve yücelikte doruk · yüce, eli açık ve yüksek değerli · onurlu ve eli açık · yüksek onur kazanmak · davranışları iyi ve cömert olmak · davranışlarıyla yücelik göstermek veya yüce görünmek
  المجد بلوغ النهاية في الكرم (maqayis)؛ المجد نيل الشرف (ayn;tahdhib)؛ المجد الكرم والمجيد الكريم (sihah)؛ المجد السعة في الكرم والجلال (mufradat)؛ قرآن مجيد والمجيد الرفيع أو الكريم (tahdhib)
- **B002** onur üstünlüğüyle böbürlenme yarışı — biriyle onur üstünlüğü konusunda yarışıp böbürlenmek · karşılıklı böbürlenip üstünlüklerini göstermek · övünme yarışında karşısındakini geçmek
  ماجد فلان فلانا فاخره (maqayis)؛ تماجد القوم إذا تفاخروا وأظهروا مجدهم (jamhara)؛ ماجدته فمجدته أي غلبته بالمجد (sihah)
- **B003** iyiliklerini ve yüceliğini anarak ululama — güzel nitelikleri anarak sözle ululama · Tanrı'nın iyiliklerini ve güzel niteliklerini anarak O'nu ululamak
  مجده خلقه تمجيدا أي تعظيما (ayn;tahdhib)؛ مجده أي ذكر آلاءه (jamhara)؛ التمجيد أن ينسب الرجل إلى المجد (sihah)؛ التمجيد من العبد لله بالقول وذكر الصفات الحسنة (mufradat)
- **B004** hayvanı doyuma yaklaştıracak kadar besleme [kalıp] — develerin otlayıp doyuma yaklaşması · hayvanı yetecek kadar yemlemek · çok yiyip içen
  مجدت الإبل مجودا نالت قريبا من شبعها (maqayis;ayn;sihah;tahdhib)؛ أصل المجد أن تأكل الماشية حتى تمتلئ بطونها (jamhara)؛ أمجدت الدابة علفتها ما كفاها (maqayis)؛ وقعت في مرعى كثير واسع (tahdhib;mufradat)؛ علفتها ملء بطنها أو نصف بطنها (sihah;tahdhib)؛ ليست بماجدة للطعام ولا الشراب أي ليست بكثيرة الطعام ولا الشراب (tahdhib)
- **B005** iki tutuşturmalık ağacın bol ateş vermesi [kalıp] — iki tutuşturmalık ağacın bol ateş verip ateş yakmaya elverişli olması
  في كل شجر نار واستمجد المرخ والعفار (maqayis;sihah;tahdhib;mufradat)؛ أي استكثرا من النار (maqayis;sihah;tahdhib)؛ فصلحا للاقتداح بهما (tahdhib)
- **B006** bağışı çoğaltma ve bolca verme — verdiği bağışı çoğaltıp bol kılmak · Tanrı'nın kuluna iyilik bağışlaması
  يكثر من العطاء طلبا للمجد (sihah)؛ أمجد فلان عطاءه ومجده إذا كثره (tahdhib)؛ ومن الله للعبد بإعطائه الفضل (mufradat)

## ر و د (root_000610): 85:16 يُرِيدُ

- **B001** dileyip yonelme — dileme, amaclama ve bir seye icten yonelme · bir seyi amaclamak, istemek ya da elde etmeye calismak · Yaraticinin bir seyi oyle diye hukme baglamasi · senden belirli bir seyi yapmani istemek ve buyurmak
  الإرادة: المشيئة (sihah)؛ الإرادة منقولة من راد يرود (mufradat)؛ نزوع النفس إلى الشيء (mufradat)؛ يذكر ويراد به القصد (mufradat)؛ فمعناه حكم فيه (mufradat)؛ قد تذكر الإرادة ويراد بها معنى الأمر (mufradat)؛ قال بعضهم الإرادة أصلها الواو (maqayis)
- **B002** birini istegine karsi razi etmeye calisma — birini belirli bir isi yapmaya razi etmeye calismak · birinin istegiyle cekisip onu gorusunden dondurmeye calismak · ters cevrilmis bicimde yeniden girisip yaklasma
  راودته على كذا مراودة وروادا، أي أردته (sihah)؛ المراودة أن تنازع غيرك في الإرادة (mufradat)؛ تصرفه عن رأيه (mufradat)؛ راودته على أن يفعل كذا إذا أردته على فعله (maqayis)؛ يرادى مقلوب ومعناه يراود (maqayis-crossref)
- **B003** dolasarak arama — bir seyi yumusakca dolasip gozden gecirerek aramak · otlak aramak icin giden ya da onde gonderilen kisi · arayisa cikan oncu adam
  راد الكلأ يروده رودا وريادا وارتاده ارتيادا أي طلبه (sihah)؛ الرائد الذي يرسل في طلب الكلإ (sihah)؛ رجل رأد بمعنى رائد (sihah)؛ الرود التردد في طلب الشيء برفق (mufradat)؛ الرائد لطالب الكلإ (mufradat)؛ بعثنا رائدا يرود الكلأ أي ينظر ويطلب (maqayis)
- **B004** gidip gelme — gidip gelmek ve ileri geri dolasmak · develerin otlakta ileri geri dolasmasi · suru veya bakicinin gidip geldigi yer · kadinin komsu evleri arasinda sik sik dolasmasi · yastiginda yerlesemeyip donup durmak
  يدل على مجيء وذهاب من انطلاق في جهة واحدة (maqayis)؛ راد الشئ يرود أي جاء وذهب (sihah)؛ رياد الإبل اختلافها في المرعى مقبلة ومدبرة (sihah)؛ المراد الموضع الذي ترود فيه الراعية (maqayis)؛ رادت المرأة ترود إذا اختلفت إلى بيوت جاراتها (maqayis)؛ راد وساده إذا لم يستقر (maqayis)
- **B005** yumusak ve yavas ilerleme — yolda yumusak davranip agir agir ilerlemek · agir ve acele etmeden yurume · yavas ol, acele etme ve biraz bekle · sert ve guclu esmeyen yumusak ruzgar
  يمشي على رود أي على مهل (sihah)؛ أرود في السير إروادا ومرودا أي رفق (sihah)؛ رويد: مهلا ورويدك: أمهل (sihah)؛ أرود يرود إذا رفق ومنه بني رويد (mufradat)؛ الإرواد في الفعل أن يكون رويدا (maqayis)؛ الرادة السهلة من الرياح لأنها ترود لا تهب بشدة (maqayis)
- **B006** cevirme kolu ve doner demir parca — el degirmenini cevirmeye yarayan tutamak kolu · ince cubuk, gemde donen demir parca veya demir makara ekseni
  الرائد يد الرحى وهو العود الذي يقبض عليه الطاحن إذا أداره (sihah)؛ الرائد العود الذي تدار به الرحى (maqayis)؛ المرود الميل وحديدة تدور في اللجام ومحور البكرة إذا كان من حديد (sihah)؛ والمرود الميل (maqayis)
- **B007** gozde dolasan bozukluk [kalıp] — gozun icinde dolasan bozukluk
  رائد العين عوارها الذي يرود فيها (sihah)؛ رائد العين عوارها الذي يرود فيها (maqayis)
- **B008** genc kiz veya genc ve guzel kadin — genc kiz · genc ve guzel kadin
  جارية رود شابة (maqayis)؛ الرؤدة والرأدة بالهمز: الشابة الحسنة (sihah)؛ وتكبير رويد رود (maqayis)

## ECHO ر د د (root_000555): for 85:16 يُرِيدُ: withheld observed target; not identity

- **B001** geri dönme veya geri döndürme — geri verme, geri gönderme veya eski durumuna döndürme · bir yere, sahibine veya kaynağına geri gönderme · kararı veya değerlendirme yetkisini bir kimseye bırakma · yolda veya durumda geri dönme · sapı içine katlanabilen ustura · görmesi geri gelmek
  أصل واحد مطرد منقاس وهو رجع الشيء (maqayis)؛ رده إلى منزله ورد إليه جوابا أي رجع (sihah)؛ الرد مصدر رددت الشيء (tahdhib)؛ الرد صرف الشيء بذاته أو بحالة من أحواله وفارتد بصيرا أي عاد إليه البصر (mufradat)
- **B002** yönünden çevirip engelleme [kalıp] — bir şeyi yolundan veya bir işten çevirme · geri dönüşü, yararı veya onu engelleyecek bir güç bulunmayan · iyiliğini engelleyebilecek kimse yok · savuşturulamayan ve önlenemeyen azap
  رده عن وجهه يرده ردا ومردا صرفه (sihah)؛ رده عن الأمر ولده أي صرفه عنه برفق (tahdhib)؛ لا راد لفضله أي لا دافع ولا مانع له وعذاب غير مردود (mufradat)
- **B003** kabul etmeyip geçersiz sayarak geri çevirme [kalıp] — sunulan şeyi kabul etmeme veya söyleyeni yanlış sayma · sahte bulunarak denetleyene geri verilen paralar
  رد عليه الشيء إذا لم يقبله وكذلك إذا خطأه (sihah)؛ ردود الدراهم واحدها رد وهو ما زيف فرد على ناقده بعد ما أخذ منه (tahdhib)
- **B004** geri isteme veya karşılıklı geri verme [kalıp] — bir şeyin geri verilmesini isteme veya onu geri alma · satışı bozarken tarafların aldıklarını karşılıklı geri vermesi
  استرده الشيء سأله أن يرده عليه وهما يترادان البيع من الرد والفسخ (sihah)؛ البيعان يترادان أي يرد كل واحد منهما ما أخذ واسترد المتاع استرجعه (mufradat)
- **B005** İslam'dan inkâra dönme — İslam'dan ayrılıp inkâra dönen kişi · Müslüman olduktan sonra inkâra dönme · dinden ayrılıp inkâra dönme · iman ettikten sonra yeniden inkâr durumuna döndürmek
  سمي المرتد لأنه رد نفسه إلى كفره (maqayis)؛ الارتداد الرجوع ومنه المرتد والردة الاسم من الارتداد (sihah)؛ ارتد الرجل عن دينه ردة إذا كفر بعد إسلامه (tahdhib)؛ الردة تختص بالكفر والارتداد يستعمل فيه وفي غيره (mufradat)
- **B006** boşanıp ailesine dönen kadın — boşanıp ailesine geri gönderilen kadın · boşanmış ve ailesine geri dönmüş kadın
  المردودة المرأة المطلقة وابنتك مردودة عليك ليس لها كاسب غيرك (maqayis)؛ المردودة المطلقة (sihah)؛ المردودة من النساء المطلقة وابنتك مردودة عليك لا كاسب لها غيرك (tahdhib)
- **B007** sütün, suyun veya bedensel sıvının birikip çoğalması — memesi sütle dolmuş koyun · memesine süt inmiş veya memesi sütle dolmuş deve · doğumdan önce memenin sütle dolması · suyu ya da dalgası bol ırmak veya deniz · uzun süre eşsiz kaldığı için cinsel isteği yoğunlaşmış erkek
  شاة مرد وناقة مردة إذا أضرعت ونهر مرد كثير الماء ورجل مرد إذا طالت عزبته (maqayis)؛ الردة امتلاء الضرع من اللبن قبل النتاج وبحر مرد كثير الموج (sihah)؛ ناقة مرد إذا أشرق ضرعها ووقع فيه اللبن ورجل مرد إذا طالت عزبته وبحر مرد أي كثير الماء (tahdhib)
- **B008** görünüş, nitelik veya konuşmadaki kusur — çenenin geriye çekikliği · yüzde güzelliğe karışan ve bakışı uzaklaştıran çirkinlik · kötü nitelikli şey · dil tutulması veya konuşma güçlüğü · çirkin kimseler
  الردة تقاعس في الذقن وقبح في الوجه مع شيء من جمال يرد الطرف (maqayis)؛ شيء رد أي رديء وفي لسانه رد أي حبسة وفي وجهه ردة أي قبح مع شيء من الجمال (sihah)؛ الردة تقاعس في الذقن وفي فلان ردة أي يرتد البصر عنه من قبحه (tahdhib)
- **B009** düşmeyi önleyen dayanak, sırt veya yük devesi — bir şeyi düşmekten koruyan dayanak; sırt veya yük taşıyan develer
  الرد عماد الشيء الذي يرده أي يرجعه عن السقوط والضعف (maqayis)؛ الرد ما صار عمادا للشيء يدفعه ويرده والرد الظهر والحمولة من الإبل (tahdhib)
- **B010** yineleme, gidip gelme, kararsızlık veya sıkı yapılı olma — bir şeyi tekrar tekrar yapma · bir eylemi defalarca yineleme · tekrar geri gelme veya iki yön arasında gidip gelme · bedeni sıkı, toplu ve parçaları birbirine geçmiş gibi olan kişi · kararsız ve ne yapacağını bilemeyen adam · develerin suya tekrar tekrar gitmesi · ellerini ağızlarına götürdüler; parmak ısırma, sus işareti yapma veya elçilerin ağızlarını kapatma biçimlerinde yorumlanan ifade
  المتردد الإنسان المجتمع الخلق كأن بعضه رد على بعض (maqayis)؛ ردده ترديدا وتردادا فتردد ورجل مردد حائر بائر (sihah)؛ فعلوا ذلك مرة بعد أخرى وردة الإبل أن تتردد إلى الماء (mufradat)

## ء ت ي (root_000009): 85:17 أَتَىٰكَ

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

## ح د ث (root_000299): 85:17 حَدِيثُ

- **B001** yokken var olma, var etme veya gerçekleşme — sonradan var olma · var etmek, ortaya çıkarmak · bir iş gerçekleşti · sonradan var edilmiş şey · eskiden beri olanlarla sonradan gerçekleşenlerin tümü · inanç ve uygulamalara sonradan eklenen yenilikler
  كون الشيء لم يكن (maqayis)؛ الحديث نقيض القديم والحدوث كون شيء لم يكن وأحدثه الله فحدث وحدث أمر أي وقع (sihah)؛ الحدوث كون الشيء بعد أن لم يكن وإحداثه إيجاده والمحدث ما أوجد بعد أن لم يكن (mufradat)
- **B002** genç, yeni ya da taze olma — yeni · genç, yaşı küçük · yaşı genç · gençler, delikanlılar · gençliğin ilk çağı · daha başlangıcındayken · taze meyve · yakın zamanda yapılmış ya da söylenmiş
  الرجل الحدث الطري السن (maqayis)؛ شاب حدث وشابة حدثة فتية في السن والحديث الجديد من الأشياء (ayn)؛ رجل حدث السن وحديث السن (jamhara)؛ رجل حدث أي شاب وهؤلاء غلمان حدثان وأوله وطراءته (sihah)؛ شاب حدث فتي السن وحدثان شبابه وحديث شبابه (tahdhib)؛ الحديث الطري من الثمار ورجل حدث وحديث السن بمعنى (mufradat)
- **B003** söz, anlatım ve karşılıklı konuşma — söz, aktarılan bilgi · anlatılar, aktarılan sözler · düşte insana söylenenler · bilgi verme, anlatma · karşılıklı konuşma · güzel ya da çok konuşan adam · çok konuşan adam · kadınlarla konuşup görüşen kimse · hükümdarların konuşma ve gece oturma arkadaşı · güzel söz söyleme niteliği · tek bir anlatı veya konuşma konusu
  الحديث لأنه كلام يحدث منه الشيء بعد الشيء ورجل حدث حسن الحديث وحدث نساء (maqayis)؛ الأحدوثة الحديث نفسه ورجل حدث كثير الحديث (ayn)؛ رجل حدث حسن الحديث وحدث نساء (jamhara)؛ الحديث الخبر والمحادثة والتحدث والتحادث والتحديث معروفات ورجل حديث كثير الحديث (sihah)؛ الحديث ما يحدث به المحدث تحديثا ورجل حدث أي كثير الحديث والأحاديث في الفقه وغيره معروفة (tahdhib)؛ كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث وحادثته وحدثته وتحادثوا (mufradat)
- **B004** insanların dilinde anlatı konusu olma — hakkında konuşulan kişi, olay veya anlatı · insanların diline düşmek · onları dilden dile aktarılan örneklere çevirdik
  صار فلان أحدوثة أي كثروا فيه الأحاديث (ayn)؛ الأحدوثة ما يتحدث به (sihah)؛ صار فلان أحدوثة أي أكثروا فيه الأحاديث (tahdhib)؛ فجعلناهم أحاديث أي أخبارا يتمثل بهم وصار أحدوثة (mufradat)
- **B005** baş gösteren ağır olay — beklenmedik ağır olay · zamanın getirdiği sıkıntılı olaylar · ortaya çıkan ağır olay
  الحدث من أحداث الدهر شبه النازلة (ayn)؛ حدثان الدهر نوائبه (jamhara)؛ الحدث والحدثى والحادثة والحدثان كلها بمعنى (sihah)؛ حدثان الدهر حوادثه والحدثان إذا ألمت بنا (tahdhib)؛ الحادثة النازلة العارضة وجمعها حوادث (mufradat)
- **B006** ortaya koyma ve görünür kılma — ortaya koyma, görünür kılma
  الحدث الإبداء (ayn)؛ الحدث الإبداء (tahdhib)
- **B007** parlatıp arındırma — kılıcı parlatıp cilalama · adam kılıcını parlattı ve cilaladı · bu yürekleri öğütlerle arındırın
  محادثة السيف جلاؤه (sihah)؛ أحدث الرجل سيفه وحادثه إذا جلاه وحادثوا هذه القلوب أي اجلوها بالمواعظ (tahdhib)
- **B008** doğru sezişli, içine esin doğan kimse — doğru sezili veya içine doğru düşünce doğan kimse
  الرجل الصادق الظن محدث بفتح الدال مشددة (sihah)؛ إن يكن في هذه الأمة محدث فهو عمر وإنما يعني من يلقى في روعه من جهة الملإ الأعلى شيء (mufradat)

## ج ن د (root_000264): 85:17 ٱلْجُنُودِ

- **B001** birlik olup destek veren topluluk — ordu; birbirini destekleyen yardımcılar topluluğu · onun yardımcıları ve destekçileri · aynı türden varlıkların oluşturduğu topluluk · ordular; topluluklar · ordular; topluluklar · canlar, uyumlarına göre birleşen ya da ayrışan kümelerdir · toplanıp düzenlenmiş topluluk · toplanmış ve düzenlenmiş
  يدل على التجمع والنصرة وأعوانه ونصاره (maqayis)؛ كل صنف من الخلق يقال لهم جند (ayn;tahdhib)؛ الجند الأعوان والأنصار (sihah)؛ الجند معروف جند وأجناد وجنود وجند مجند أي مجموع (jamhara)؛ يقال للعسكر الجند ولكل مجتمع جند (mufradat)
- **B002** beyaz taşlı sert arazi veya balçığı andıran taşlar — beyaz taşlar içeren sert arazi · balçığa benzeyen taşlar
  الجند الأرض الغليظة فيها حجارة بيض (maqayis)؛ الجند حجارة شبه الطين (ayn;tahdhib)؛ الجند الأرض الغليظة (jamhara)؛ الجند أي الأرض الغليظة التي فيها حجارة (mufradat)
- **B003** belirli yer ve idari bölge adları — Yemen'deki Jand şehri veya yeri · Şam'ın beş idari çevresi · Şam'daki Ajnadin yeri ve onunla anılan gün
  الأجناد أجناد الشام وهي خمسة (maqayis)؛ جند موضع باليمن (ayn)؛ الجند موضع باليمن وأجنادين موضع بالشام (jamhara)؛ جند بالتحريك بلد باليمن (sihah)؛ أجناد الشام خمس كور ويوم أجنادين (tahdhib)
- **B004** topluluk ve kişi adları ile aidiyet sıfatı — Yemen'den Janada topluluğu · Janad kişi adı · Janada kişi adı · Junayd kişi adı · Jand'a, o topluluğa veya yere mensup kimse
  جنادة حي من اليمن (ayn;tahdhib)؛ سمت العرب جنادا وجنادة وجنيدا (jamhara)؛ فلان الجندي (tahdhib)

## ك ف ر (root_001307): 85:19 كَفَرُوا۟

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

## ك ذ ب (root_001290): 85:19 تَكْذِيبٍ

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

## و ر ي (root_001642): 85:20 وَرَآئِهِم

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

## ح و ط (root_000372): 85:20 مُّحِيطٌۢ

- **B001** fiziksel olarak çevresini sarma — bir şeyin çevresini fiziksel olarak sardı · çevresine duvar ördü · bir yeri çevreleyen duvar · yiyecek için yapılmış çevrili saklama yeri · atlar kişinin çevresini sardı
  هو الشيء يطيف بالشيء (maqayis)؛ احتاطت الخيل بفلان وأحاطت به أي أحدقت (ayn;sihah;tahdhib)؛ الحائط لأنه يحوط ما فيه وحوطت حائطا (ayn;tahdhib)؛ الحائط الجدار الذي يحوط بالمكان (mufradat)؛ الحواطة حظيرة تتخذ للطعام (maqayis;sihah)
- **B002** koruyup gözetme — onu koruyup gözetti · koruma, gözetme ve sürekli ilgilenme · güvenli yolu seçerek önlem alma · sana karşı şefkat ve yakınlık besliyor · alıkonulmanız dışında · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  حطت الرجل أحوطه حوطا إذا حفظته (jamhara)؛ حاطه حيطة إذا تعاهده (ayn;tahdhib)؛ كلأه ورعاه (sihah)؛ الحياطة الحفظ والاحتياط استعمال ما فيه الحياطة (mufradat)؛ تستعمل في المنع (mufradat)؛ مع فلان حيطة لك أي تحنن وتعطف (sihah)
- **B003** eşeğin sürüsünü bir araya toplaması [kalıp] — eşek kendi sürüsünü toplayıp bir araya sürdü
  الحمار يحوط عانته يجمعها (maqayis;ayn;sihah;tahdhib)
- **B004** bir şeyi bütünüyle bilme veya elde etme [kalıp] — onu bütün yönleriyle eksiksiz bildi · şeyin tamamını elde edip denetim altına aldı · hakkında eksiksiz bilgi edinmediği şey
  كل من أحرز شيئا كله وبلغ علمه أقصاه فقد أحاط به (ayn;tahdhib)؛ أحاط به علما (sihah)؛ الإحاطة بالشيء علما هي أن تعلم وجوده وجنسه وقدره وكيفيته (mufradat)
- **B005** çevresinde dönme veya dolaylı yoldan razı etmeye çalışma — o işin çevresinde dönüp duruyorum · istemediği bir şeyi ondan elde etmek için dolaylı yollardan uğraştı
  أنا أحوط حول ذلك الأمر أي أدور (sihah)؛ حاوطت فلانا محاوطة إذا داورته في أمر تريده منه وهو يأباه (tahdhib)
- **B006** karşı konulmaz bir güçle kuşatılıp yıkıma sürüklenme [kalıp] — sonunu getirecek bir gücün altında kaldı · ürünü yok olup bozuldu · karşı koyamayacakları bir güçle kuşatıldılar
  أحيط بفلان إذا دنا هلاكه فهو محاط به (tahdhib)؛ أصابه ما أهلكه وأفسده (tahdhib)؛ أحيط بهم فذلك إحاطة بالقدرة (mufradat)
- **B007** yuvarlak veya hilal biçimli gümüş süs — yuvarlak gümüş süs veya boncuklu iki renkli ipteki gümüş hilal · çocuğa gümüş hilal biçimli süs taktı · akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme
  الحوط شيء مستدير تعلقه المرأة على جبينها من فضة (maqayis)؛ الحوط خيط مفتول من لونين أحمر وأسود وهلال من فضة (tahdhib)؛ أن يحلي صبيه بالحوط وهو هلال من فضة (tahdhib)
- **B008** eksik para tutarını tamamlayan ek miktar — eksik para tutarını tamamlayan ek miktar
  الدراهم إذا نقصت في الفرائض أو غيرها هلم حوطها؛ الحوط ما يتم به دراهمه

## ق ر ء (root_001210): 85:21 قُرْءَانٌ

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

## ق ر ء (root_001211): 85:21 قُرْءَانٌ

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

## ل و ح (root_001384): 85:22 لَوْحٍ

- **B001** parlayıp görünür olma — parlayıp görünür olmak · şimşeğin çakıp parıldaması · yıldızın belirmesi veya parıldaması · kılıcı veya bezi parıldatarak işaret etmek · silahın parlayan bölümleri, özellikle kılıç ve mızrak ucu · ak, beyaz veya beyazlığından ötürü böyle adlandırılan şey · bir anlık bakış veya görüş
  لاح الشيء يلوح إذا لمح ولمع (maqayis)؛ ولاح البرق وألاح إذا أومض (maqayis;sihah;mufradat)؛ كل من لمع بشيء فقد ألاح ولوح به (ayn)؛ لاح السيف والبرق وغيرهما (jamhara)؛ ألواح السلاح ما يلوح منه كالسيف والسنان (jamhara;sihah)؛ اللياح الأبيض والثور الوحشي لبياضه (maqayis;ayn;sihah)
- **B002** yakıcı veya yıpratıcı etkiden görünüşü değişme — yolculuğun rengini veya görünüşünü değiştirmesi · susuzluğun görünüşünü değiştirmesi · sıcağın, güneşin veya ateşin yakıp karartarak değiştirmesi · bir şeyi ateşte ısıtmak · insan derisini ısısıyla değiştiren veya yakan
  لوحه الحر حرقه وسوده حتى لاح (maqayis)؛ لاحه العطش ولوحه إذا غيره ولاحه البرد والسقم والحزن (ayn)؛ لاحته السموم والنار إذا غيره (jamhara)؛ لاحه السفر غيره ولوحته الشمس غيرته وسفعت وجهه (sihah)؛ لوحه الحر غيره (mufradat)
- **B003** geniş ve yassı levha — geniş ve yassı kemik, yazı tahtası veya levha · geminin gövdesini oluşturan tahta levhalar · niteliği bilinmeyen korunan levha
  اللوح الكتف والواحد من ألواح السفينة وكل عظم عريض (maqayis)؛ اللوح كل صحيفة من صفائح الخشب والكتف إذا كتب عليها (ayn)؛ اللوح كل عظم عريض ولوح الصبي لعرضه (jamhara)؛ اللوح الكتف وكل عريض والذي يكتب فيه (sihah)؛ اللوح واحد ألواح السفينة وما يكتب فيه من الخشب ونحوه (mufradat)
- **B004** gökle yer arasındaki hava — gökle yer arasındaki hava
  اللوح بالضم وهو الهواء بين السماء والأرض (maqayis;jamhara;sihah;mufradat)؛ واللوح الهواء (ayn)
- **B005** susuzluk ve çabuk susama — susuzluk · çabuk susayan veya susamış · susamış develer
  اللوح العطش ودابة ملواح سريع العطش (maqayis;mufradat)؛ الملواح العطشان (ayn)؛ رجل ملواح سريع العطش وكذلك الجمل والدابة (jamhara)؛ لاح لوحا ولواحا عطش وإبل لوحى عطشى (sihah)
- **B006** sakınma veya biri için kaygılanma [kalıp] — bir şeyden sakınmak veya endişe etmek · bir kimse için kaygılanmak veya üzülmek
  ألاح من الشيء حاذر (maqayis)؛ ألاح الرجل من الشيء إذا أشفق وحاذر (sihah)؛ ألاح الرجل على الرجل إذا جزع عليه ويليح يشفق أيضا (jamhara)
- **B007** alıp götürme veya yok etme — hakkını alıp götürmek · onu yok etmek
  ألاح بحقي إذا ذهب به (sihah)؛ يليح يذهب به (jamhara)؛ ألاحه أهلكه (sihah)
- **B008** yırtıcı kuşu çekmek için hazırlanmış baykuşlu canlı yem düzeneği — yırtıcı kuşu çekmek için hazırlanan gözleri dikilmiş baykuş ve bağlı düzenek
  الملواح أن تعمد إلى بومة فتخيط عينها وتشد في رجلها صوفة سوداء؛ فالبومة وما يليها يسمى ملواحا (ayn)

## ح ف ظ (root_000342): 85:22 مَّحْفُوظٍۭ

- **B001** koruyup gözetme — koruyup gözetme ve bakımını üstlenme · bir şeyi koruyup kolladı · bir şeyi koruyan ya da korumakla görevlendirilen kimse · insanların yaptıklarını sayıp yazan melekler · onu yalnız kendisi için sakladı · onu korumasını istedi ve güvenip kendisine teslim etti · koruma altında, kaybolmadan ve değişmeden saklanmış · gözetip başında durma
  أصل واحد يدل على مراعاة الشيء (maqayis)؛ الحفيظ الموكل بالشيء يحفظه (ayn;tahdhib)؛ حفظت الشيء حفظا (jamhara)؛ حفظت الشئ حفظا أي حرسته (sihah)؛ استحفظته كذا أي سألته أن يحفظه عليك (ayn;sihah;tahdhib)؛ تفقد وتعهد ورعاية (mufradat)
- **B002** bellekte tutma — bir şeyi unutmayacak biçimde bellekte tutma · kitabı bölüm bölüm ezberledi
  الحفظ نقيض النسيان (ayn;tahdhib)؛ حفظته أيضا بمعنى استظهرته (sihah)؛ تحفظت الكتاب أي استظهرته (sihah)؛ رزقوا حفظ ما سمعوا وقلما ينسون (tahdhib)؛ هيئة النفس التي بها يثبت ما يؤدي إليه الفهم وضبط الشيء في النفس (mufradat)
- **B003** düzenli biçimde sürdürme — bir işi düzenli biçimde sürdürme · işi bırakmadan sürdürdü · işlerin üzerinde düzenli biçimde durma
  الحفاظ المحافظة على الأمور (maqayis)؛ المحافظة المواظبة على الأمور من الصلوات والعلم ونحوه (ayn)؛ المحافظة المواظبة على الأمر (tahdhib)؛ حافظ على الأمر والعمل وثابر عليه (tahdhib)
- **B004** uyanık ve dikkatli olma — hata yapmamak için tetikte ve dikkatli olma
  التحفظ قلة الغفلة (maqayis)؛ التحفظ قلة الغفلة حذرا من السقطة في الكلام والأمور (ayn)؛ التحفظ التيقظ وقلة الغفلة (sihah)؛ التحفظ قلة الغفلة في الكلام والتيقظ من السقطة (tahdhib)
- **B005** koruyucu öfke ve onurlu tepki — dokunulmaz saydığı bir şey çiğnendiğinde duyulan koruyucu öfke · içte bekleyen koruyucu öfke · beni öfkelendirdi · yakınına ya da komşusuna zarar geldiğinde kişiyi öfkelendiren şeyler
  الغضب الحفيظة (maqayis)؛ أحفظني أي أغضبني (maqayis)؛ الحفيظة الحمية (jamhara)؛ الحفيظة الغضب والحمية وكذلك الحفظة بالكسر (sihah)؛ إنه لذو حفاظ وذو محافظة إذا كانت له أنفة (sihah)؛ الحفظة اسم من الاحتفاظ عندما يرى من حفيظة الرجل (tahdhib)
- **B006** dokunulmazlıkları, sözleri ve bağlılığı koruma — yakınları, verilen sözü ve bağlılığı koruma · kendi topluluğunu arkadan kollayıp açıklarını örtenler · haksızlığa uğrayan yakını savunmanın eski kini giderdiğini anlatan söz · yokluğunda onu ve hakkını korudu · cinsel davranışta özdenetimini koruyanlar · eşleri yokken evlilik bağını gözeten kadınlar
  الحفاظ المحافظة على المحارم ومنعها عند الحروب (ayn)؛ أهل الحفائظ المحامون من وراء إخوانهم مانعون لعوراتهم (ayn)؛ حافظت على الرجل محافظة وحفاظا إذا حفظته في مغيبه (jamhara)؛ إن الحفائظ تنقض الأحقاد (jamhara;sihah)؛ الحفاظ المحافظة على العهد والمحاماة على الحرم (tahdhib)؛ الوفاء بالعقد والتمسك بالود (tahdhib)؛ فروجهم حافظون كناية عن العفة (mufradat)؛ حافظات للغيب أي يحفظن عهد الأزواج (mufradat)
- **B007** açık, düz ve kesintisiz yol [kalıp] — açık, düz ve kesintisiz süren yol
  الطريق الحافظ هو البين المستقيم الذي لا ينقطع (tahdhib)



===== _commentary/v16/work/s085/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s085/reader_a_pilot.md)

# S085 Semantic Channel Discovery

## Parent Channels

### 1. Devotion, Belief, and Sacred Commitment
- Semantic invariant: A person or community binds itself to a sacred object through worship, assent, praise, promise, fidelity, repentance, and pardon.
- Surface relation: direct; belief and worship at 85:7-11, denial at 85:19, forgiveness and love at 85:14, and majesty at 85:15 and 85:21.
- Surprising reach: The devotional frame extends into oath formulas, the response “Amen,” treaty language, guarded honor, expiation, reputation, and named cults.

#### 1A. Worship and Divine Lordship
- Reading type: surface-primary
- Scene or process: Worshippers acknowledge a divine lord whose sovereignty, throne, and majesty ground obedience.
- Active motifs: worship and the worshipped deity `ء ل ه:B001/m01`; lordship and mastery `ر ب ب:B001/m01`; sovereign rule `م ل ك:B003/m01`; royal throne `ع ر ش:B001/m01`; majestic dignity `م ج د:B001/m01`.
- Ayah anchors: `ء ل ه` at 85:8, 85:9, 85:20; `ر ب ب` at 85:12; `م ل ك` at 85:9; `ع ر ش` at 85:15; `م ج د` at 85:15, 85:21.
- Synthesis: The motifs form a coherent hierarchy in which worship answers to lordship, lordship is expressed as sovereignty, and sovereignty is figured by the elevated throne and its majesty.

#### 1B. Invocation, Oath, and Amen
- Reading type: latent/lexical
- Scene or process: A speaker calls on the divine name, swears by it, voices a wish, and seeks ratification through “Amen.”
- Active motifs: divine name in oath and address `ء ل ه:B002/m01`; “Amen” as a request for response `ء م ن:B003/m01`; naming in direct address `س م و:B005/m01`; wished-for fulfillment `و د د:B002/m01`.
- Ayah anchors: `ء ل ه` at 85:8, 85:9, 85:20; `ء م ن` at 85:7, 85:8, 85:10, 85:11; `س م و` at 85:1, 85:9; `و د د` at 85:14.
- Synthesis: These lexical senses assemble a complete prayer act: the invoked name identifies the addressee, desire supplies the petition, and “Amen” asks that the utterance become effective.

#### 1C. Faith, Promise, and Denial
- Reading type: surface-primary
- Scene or process: A promised claim is received with settled belief or rejected through denial and counter-attribution.
- Active motifs: belief as heart-settling assent `ء م ن:B002/m01`; promise that opens expectation `و ع د:B001/m01`; denial that veils truth `ك ف ر:B003/m01`; attribution of falsehood `ك ذ ب:B002/m01`.
- Ayah anchors: `ء م ن` at 85:7, 85:8, 85:10, 85:11; `و ع د` at 85:2; `ك ف ر` and `ك ذ ب` at 85:19.
- Synthesis: Promise creates an object of assent, while disbelief and accusation reverse the same epistemic relation by refusing or discrediting what is offered as true.

#### 1D. Covenant, Fidelity, and Guarded Sanctity
- Reading type: latent/lexical
- Scene or process: Parties exchange a binding promise and preserve the relationship by defending its terms, intimacies, and honor.
- Active motifs: reciprocal pact `و ع د:B004/m01`; covenant and protected alliance `ر ب ب:B011/m01`; preservation of contract, chastity, and sacred bounds `ح ف ظ:B006/m01`; tightened bond `ش د د:B001/m01`; faithful assent `ء م ن:B002/m01`.
- Ayah anchors: `و ع د` at 85:2; `ر ب ب` at 85:12; `ح ف ظ` at 85:22; `ش د د` at 85:12; `ء م ن` at 85:7, 85:8, 85:10, 85:11.
- Synthesis: The scene joins agreement to custodianship: a promise becomes durable when its bond is tightened and its personal and communal boundaries are actively guarded.

#### 1E. Repentance, Forgiveness, and Expiation
- Reading type: mixed
- Scene or process: Wrongdoing is named, the wrongdoer is called back, and the offense is covered so that its punitive effect is removed.
- Active motifs: invitation to repent `ت و ب:B003/m01`; pardon that shields from consequence `غ ف ر:B002/m01`; expiation that effaces an offense `ك ف ر:B009/m01`; grave sin `ك ب ر:B007/m01`; retributive response `ن ق م:B002/m01`.
- Ayah anchors: `ت و ب` at 85:10; `غ ف ر` at 85:14; `ك ف ر` at 85:19; `ك ب ر` at 85:11; `ن ق م` at 85:8.
- Synthesis: Covering changes function across the process: sin first incurs punishment, repentance opens return, and forgiveness or expiation covers the offense by protecting the person from its remaining effect.

#### 1F. Praise, Gratitude, and Devotional Attachment
- Reading type: mixed
- Scene or process: Worth is publicly voiced, remembered as good fame, and intensified into affectionate or cultic devotion.
- Active motifs: praise and gratitude `ح م د:B001/m01`; verbal glorification `م ج د:B003/m01`; circulating good reputation `س م و:B008/m01`; mutual affection `و د د:B001/m01`; named object of cultic devotion `و د د:B005/m01`.
- Ayah anchors: `ح م د` at 85:8; `م ج د` at 85:15, 85:21; `س م و` at 85:1, 85:9; `و د د` at 85:14.
- Synthesis: Praise moves from an evaluative utterance to durable social memory and, at its strongest, to attachment centered on a revered name or object.

### 2. Witness, Knowledge, and Linguistic Presence
- Semantic invariant: Persons, events, and referents are made present to mind or community through attendance, testimony, memory, report, articulation, grammar, and naming.
- Surface relation: direct; witnesses at 85:3, 85:7, 85:9, the report at 85:17, the recited text at 85:21, and its preservation at 85:22.
- Surprising reach: The channel reaches ritual attendance, weddings, memorization, phonetics, interrogatives, relative and demonstrative reference, greetings, proper names, seals, and reputation.

#### 2A. Witnessed Presence and Attendance
- Reading type: mixed
- Scene or process: A person is physically present, sees what occurs, and participates as attendant, companion, celebrant, or visitor.
- Active motifs: presence with observation `ش ه د:B001/m01`; seated attendance `ق ع د:B001/m01`; accompanying presence `ص ح ب:B001/m01`; recurring festival attendance `ع و د:B007/m01`; repeated visitation `ع و د:B005/m01`.
- Ayah anchors: `ش ه د` at 85:3, 85:7, 85:9; `ق ع د` at 85:6; `ص ح ب` at 85:4; `ع و د` at 85:13.
- Synthesis: Witnessing is embodied before it is evidentiary: presence, seating, companionship, festival return, and visitation all place a participant within the event observed.

#### 2B. Testimony and Comprehensive Knowledge
- Reading type: mixed
- Scene or process: A knower reaches an encompassing understanding and turns it into decisive testimony or judgment.
- Active motifs: testimony grounded in knowledge `ش ه د:B002/m01`; complete mastery of a report `ق ت ل:B003/m01`; all-sided comprehension `ح و ط:B004/m01`; totality of parts `ك ل ل:B003/m01`; learned authority `ر ب ب:B003/m01`.
- Ayah anchors: `ش ه د` at 85:3, 85:7, 85:9; `ق ت ل` at 85:4; `ح و ط` at 85:20; `ك ل ل` at 85:9; `ر ب ب` at 85:12.
- Synthesis: The scene progresses from gathering the whole to mastering it and finally declaring it, making testimony the public form of comprehensive knowledge.

#### 2C. Memorized and Guarded Learning
- Reading type: mixed
- Scene or process: Words or concepts are received, fixed in the inner faculty, and protected against loss.
- Active motifs: memorization and retention `ح ف ظ:B002/m01`; gathered recitation and study `ق ر ء:B001/m01`; trusted inner assurance `ء م ن:B001/m01`; the hidden heart or inward thought `ج ن ن:B010/m01`.
- Ayah anchors: `ح ف ظ` at 85:22; `ق ر ء` at 85:21; `ء م ن` at 85:7, 85:8, 85:10, 85:11; `ج ن ن` at 85:11.
- Synthesis: Recitation supplies ordered verbal material, memory fixes it, and the inward heart becomes both its secure container and the seat of confidence in it.

#### 2D. Conversation, Report, and News
- Reading type: mixed
- Scene or process: An event becomes speech, circulates between speakers, and is received as report or narrated precedent.
- Active motifs: renewed speech and news `ح د ث:B003/m01`; keeping pace in conversation `ج ر ي:B007/m01`; gathered reading or recitation `ق ر ء:B001/m01`; arrival of the report `ء ت ي:B001/m01`; silence that neither begins nor answers `ع و د:B003/m01`.
- Ayah anchors: `ح د ث` and `ء ت ي` at 85:17; `ج ر ي` at 85:11; `ق ر ء` at 85:21; `ع و د` at 85:13.
- Synthesis: The channel treats discourse as motion: news arrives, speakers move together through an exchange, recitation stabilizes it, and silence marks the breakdown of reciprocal narration.

#### 2E. Tongue, Articulation, and Fluency
- Reading type: latent/lexical
- Scene or process: The tongue serves as visible witness by finding the places of the sounds and sustaining intelligible speech.
- Active motifs: tongue as expressive witness `ش ه د:B005/m01`; fluent placement of letters `ب ل ل:B006/m01`; blunt or exhausted tongue `ك ل ل:B001/m01`; speechlessness `ع و د:B003/m01`.
- Ayah anchors: `ش ه د` at 85:3, 85:7, 85:9; the `بَلْ` tokens at 85:19 and 85:21; `ك ل ل` at 85:9; `ع و د` at 85:13.
- Synthesis: Articulation makes inward content externally legible, while dullness and silence supply the contrasting failure states of the same speech mechanism.

#### 2F. Grammar, Interrogation, and Deixis
- Reading type: mixed
- Scene or process: Function words locate a referent, ask about it, connect a clause to it, or shift the discourse to a new proposition.
- Active motifs: relative connector “ذو” `ذ و و:B002/m01`; demonstrative pointer `ذ و و:B003/m01`; interrogative or relative “ماذا” `ذ و و:B004/m01`; grammatical objects and complements `ف ع ل:B007/m01`; particle of qualification “رب” `ر ب ب:B015/m01`; adversative-resumptive “بل” `ب ل ل:B008/m01`; posterior or alternative perspective `و ر ي:B006/m01`; lower spatial relation `ت ح ت:B001/m01`.
- Ayah anchors: `ذَات`, `ٱلَّذِي`, `ذَٰلِكَ`, and `ذُو` at 85:1, 85:5, 85:9, 85:11, 85:15; `ف ع ل` at 85:7, 85:16; `ر ب ب` at 85:12; `بَلْ` at 85:19, 85:21; `و ر ي` at 85:20; `ت ح ت` at 85:11.
- Synthesis: These motifs form a discourse-control system: pointing establishes the referent, interrogation opens a slot, grammar assigns its relation, and particles redirect, qualify, or spatially orient the clause.

#### 2G. Naming and Identity
- Reading type: latent/lexical
- Scene or process: A person, deity, lineage, or place is fixed and socially recognized through a name or designation.
- Active motifs: naming and name equivalence `س م و:B005/m01`; possessor or attributed identity `ذ و و:B001/m01`; personal and tribal names `ج ن د:B004/m01`; personal name “Ṣāliḥ” `ص ل ح:B004/m01`; place and poet names `ن ه ر:B007/m01`; branded identifying mark `خ د د:B004/m01`.
- Ayah anchors: `س م و` at 85:1, 85:9; the `ذَات/ذُو` tokens at 85:1, 85:5, 85:15; `ج ن د` at 85:17; `ص ل ح` at 85:11; `ن ه ر` at 85:11; `خ د د` at 85:4.
- Synthesis: Names, possessive attributions, genealogical labels, place-names, and bodily marks all make identity durable by attaching a publicly retrievable sign to its bearer.

#### 2H. Reputation, Anecdote, and Exemplar
- Reading type: latent/lexical
- Scene or process: A person’s deeds become repeated public speech and settle into praise, blame, biography, or proverb.
- Active motifs: becoming an anecdote `ح د ث:B004/m01`; circulating good fame `س م و:B008/m01`; verbal commemoration `م ج د:B003/m01`; evaluated character `ف ع ل:B002/m01`; recurring mention `ع و د:B007/m02`.
- Ayah anchors: `ح د ث` at 85:17; `س م و` at 85:1, 85:9; `م ج د` at 85:15, 85:21; `ف ع ل` at 85:7, 85:16; `ع و د` at 85:13.
- Synthesis: Conduct is converted into narrative capital: repeated telling makes the subject exemplary, and praise or blame determines the form in which the name persists.

### 3. Sovereignty, Rank, and Contest
- Semantic invariant: Power is organized as ownership, rule, elevated status, leadership, competition, administration, and submission.
- Surface relation: direct; divine might at 85:8, sovereignty at 85:9, severe power at 85:12, and throne and majesty at 85:15.
- Surprising reach: The hierarchy extends to captains, animal leaders, bureaucrats, tax collectors, social strata, competitive boasting, cowardice, and ritualized submission.

#### 3A. Ownership and Sovereign Rule
- Reading type: surface-primary
- Scene or process: An owner exercises disposal over property and a ruler governs subjects from an elevated seat.
- Active motifs: possession and disposal `م ل ك:B002/m01`; kingship and political sovereignty `م ل ك:B003/m01`; lordly ownership `ر ب ب:B001/m01`; royal throne `ع ر ش:B001/m01`; stable structure of power `ع ر ش:B006/m01`.
- Ayah anchors: `م ل ك` at 85:9; `ر ب ب` at 85:12; `ع ر ش` at 85:15.
- Synthesis: Property and rule form one graded scene, moving from control of a thing to governance of a people and finally to the throne as the structure that sustains authority.

#### 3B. Majesty, Eminence, and Dignity
- Reading type: mixed
- Scene or process: A person or institution rises above peers through strength, inherited standing, and publicly acknowledged dignity.
- Active motifs: majestic honor `م ج د:B001/m01`; elevation and high repute `س م و:B001/m01`; leadership and noble standing `ك ب ر:B005/m01`; grandeur and rightful greatness `ك ب ر:B006/m01`; strength opposed to humiliation `ع ز ز:B001/m01`.
- Ayah anchors: `م ج د` at 85:15, 85:21; `س م و` at 85:1, 85:9; `ك ب ر` at 85:11; `ع ز ز` at 85:8.
- Synthesis: Physical elevation, social precedence, strength, and praised grandeur converge on a single status transformation from lowliness to recognized dignity.

#### 3C. Primacy, Leadership, and Command
- Reading type: latent/lexical
- Scene or process: A leader goes first, is mentioned first, directs a crew or herd, and brings action to effect.
- Active motifs: chief mentioned first `ب د ء:B003/m01`; headship and teaching authority `ك ب ر:B005/m01`; captain of sailors `ر ب ب:B017/m01`; leading animal or guide `م ل ك:B008/m01`; decisive effective person `ء ت ي:B013/m01`.
- Ayah anchors: `ب د ء` at 85:13; `ك ب ر` at 85:11; `ر ب ب` at 85:12; `م ل ك` at 85:9; `ء ت ي` at 85:17.
- Synthesis: The same invariant of functional precedence links the named chief, ship captain, herd leader, and effective agent: each occupies the forward position that organizes followers.

#### 3D. Competition, Boasting, and Victory
- Reading type: latent/lexical
- Scene or process: Rivals match themselves, boast of superiority, overpower an opponent, and claim prestige or success.
- Active motifs: rivalry and competitive matching `س م و:B007/m01`; overpowering the opponent `ع ز ز:B002/m01`; competitive domination `ك ب ر:B011/m01`; boasting through glory `م ج د:B002/m01`; victory and deliverance `ف و ز:B001/m01`.
- Ayah anchors: `س م و` at 85:1, 85:9; `ع ز ز` at 85:8; `ك ب ر` and `ف و ز` at 85:11; `م ج د` at 85:15, 85:21.
- Synthesis: Competition escalates from comparison to boast, then to overpowering and possession of the winning outcome, while glory preserves the victory as status.

#### 3E. Administration, Delegation, and Tribute
- Reading type: latent/lexical
- Scene or process: A ruler assigns an office, sends an agent, exacts revenue, and requires continued performance.
- Active motifs: holding governmental office `ع م ل:B003/m01`; delegated agent or guarantor `ج ر ي:B003/m01`; tax, tribute, or levy `ء ت ي:B008/m01`; tithe governed as covenant `ر ب ب:B011/m02`; constancy in official duty `ح ف ظ:B003/m01`.
- Ayah anchors: `ع م ل` and `ج ر ي` at 85:11; `ء ت ي` at 85:17; `ر ب ب` at 85:12; `ح ف ظ` at 85:22.
- Synthesis: Office turns authority into procedure: appointment creates the agent, tribute creates the obligation, and habitual preservation keeps the institution functioning.

#### 3F. Social Strata, Humiliation, and Submission
- Reading type: latent/lexical
- Scene or process: Groups are ranked, some occupy a low stratum, and submission is displayed through lowered posture.
- Active motifs: social class or faction `خ د د:B005/m01`; grouped strata `ك ل ل:B009/m01`; disregarded lower ranks `ت ح ت:B002/m01`; ignoble or cowardly status `ق ع د:B013/m01`; bowed bodily submission `ك ف ر:B014/m01`.
- Ayah anchors: `خ د د` at 85:4; `ك ل ل` at 85:9; `ت ح ت` at 85:11; `ق ع د` at 85:6; `ك ف ر` at 85:19.
- Synthesis: Rank is encoded both collectively and bodily: classes occupy relative levels, while lowering the head or chest performs subordination within that hierarchy.

### 4. Moral Agency, Deception, and Judgment
- Semantic invariant: Intentional action acquires ethical character, may be falsified or misdirected, is tested under pressure, and receives censure, restraint, pardon, or punishment.
- Surface relation: direct; deeds at 85:7, faith and blame at 85:8, trial and punishment at 85:10, severe retribution at 85:12, and unconstrained action and will at 85:16.
- Surprising reach: The channel includes craftsmanship as a metaphor for fabrication, seductive display, metal assaying, weaning and abstention, verbal rebuke, and destruction figured as total enclosure.

#### 4A. Intentional Action and Causation
- Reading type: surface-primary
- Scene or process: A willing agent initiates an act, brings a new state into being, and produces an effect.
- Active motifs: enacted occurrence `ف ع ل:B001/m01`; purposive work `ع م ل:B001/m01`; initiation `ب د ء:B001/m01`; event arising after nonexistence `ح د ث:B001/m01`; will and purpose `ر و د:B001/m01`.
- Ayah anchors: `ف ع ل` at 85:7, 85:16; `ع م ل` at 85:11; `ب د ء` at 85:13; `ح د ث` at 85:17; `ر و د` at 85:16.
- Synthesis: Will supplies direction, initiation opens the process, work carries it out, and the resulting event is the changed state caused by the agent.

#### 4B. Character, Virtue, and Good Conduct
- Reading type: mixed
- Scene or process: Repeated actions reveal a person’s disposition and are judged as fitting, beneficial, generous, or blameworthy.
- Active motifs: noble or base character expressed in action `ف ع ل:B002/m01`; rectitude opposed to corruption `ص ل ح:B001/m01`; aptitude for good `ء ر ض:B003/m01`; tested approval `ح م د:B002/m01`; generosity of character `ع ذ ب:B008/m01`.
- Ayah anchors: `ف ع ل` at 85:7, 85:16; `ص ل ح` at 85:11; `ء ر ض` at 85:9; `ح م د` at 85:8; `ع ذ ب` at 85:10.
- Synthesis: The scene treats conduct as the visible test of disposition: fitting and reparative action earns approval, while its opposite exposes moral defect.

#### 4C. Fabrication, Forgery, and False Attribution
- Reading type: latent/lexical
- Scene or process: A maker constructs speech, poetry, or an account without a true model and presents the product as credible.
- Active motifs: invented fabrication `ف ع ل:B004/m01`; falsehood opposed to truth `ك ذ ب:B001/m01`; imputing falsehood `ك ذ ب:B002/m01`; manufactured report `ح د ث:B003/m02`; imposed poetic pattern `ق ر ء:B005/m01`.
- Ayah anchors: `ف ع ل` at 85:7, 85:16; `ك ذ ب` at 85:19; `ح د ث` at 85:17; `ق ر ء` at 85:21.
- Synthesis: Craft becomes deception when formal construction is detached from truth: a patterned utterance is made, circulated as news, and defended by redirecting the charge of falsehood.

#### 4D. Seduction and Misdirection
- Reading type: latent/lexical
- Scene or process: One party decorates an object or proposition, contests another’s will, and draws that person away from an intended course.
- Active motifs: diversion from the right course `ف ت ن:B003/m01`; contested persuasion `ر و د:B002/m01`; seductive display `ب ر ج:B003/m01`; coquettish movement or pleading `ق ت ل:B004/m01`; deceptive impulse `ك ذ ب:B008/m01`.
- Ayah anchors: `ف ت ن` at 85:10; `ر و د` at 85:16; `ب ر ج` at 85:1; `ق ت ل` at 85:4; `ك ذ ب` at 85:19.
- Synthesis: Display attracts attention, persuasion contests volition, and misdirection changes the target’s course, with bodily coquetry and inward deceit supplying parallel mechanisms.

#### 4E. Testing, Ordeal, and Crisis
- Reading type: mixed
- Scene or process: A person or material is exposed to severe pressure so that quality, endurance, or allegiance becomes visible.
- Active motifs: assaying metal or testing a person `ف ت ن:B001/m01`; ordeal and affliction `ف ت ن:B004/m01`; force and resilience `ش د د:B002/m01`; burdensome difficulty `ع ز ز:B005/m01`; crisis or momentous event `ي و م:B003/m01`.
- Ayah anchors: `ف ت ن` at 85:10; `ش د د` at 85:12; `ع ز ز` at 85:8; `ي و م` at 85:2.
- Synthesis: The assay supplies the mechanism, severity supplies the pressure, and crisis supplies the setting in which hidden quality is separated from failure.

#### 4F. Censure, Restraint, and Abstention
- Reading type: mixed
- Scene or process: An objection is voiced, the subject is rebuked, and an action or appetite is halted.
- Active motifs: disapproval and grievance `ن ق م:B001/m01`; forceful verbal rebuke `ن ه ر:B004/m01`; withholding, weaning, or abstention `ع ذ ب:B003/m01`; sitting out an action `ق ع د:B002/m01`; preventing grazing `ع ر ش:B010/m01`.
- Ayah anchors: `ن ق م` at 85:8; `ن ه ر` at 85:11; `ع ذ ب` at 85:10; `ق ع د` at 85:6; `ع ر ش` at 85:15.
- Synthesis: Judgment first appears as dissatisfaction, becomes speech in rebuke, and becomes behavioral control through withholding, abstention, or enforced inactivity.

#### 4G. Punishment, Ruin, and Mortal Outcome
- Reading type: mixed
- Scene or process: Condemned action is answered by pain, overpowering enclosure, destruction, severe illness, or death.
- Active motifs: punitive retaliation `ن ق م:B002/m01`; inflicted suffering `ع ذ ب:B005/m01`; engulfing defeat and destruction `ح و ط:B006/m01`; fatal calamity `ء ت ي:B011/m01`; death as departure `ف و ز:B002/m01`; annihilating removal `ل و ح:B007/m01`.
- Ayah anchors: `ن ق م` at 85:8; `ع ذ ب` at 85:10; `ح و ط` at 85:20; `ء ت ي` at 85:17; `ف و ز` at 85:11; `ل و ح` at 85:22.
- Synthesis: Punishment is represented as a closing field of force: pain and calamity progressively surround the target until capacity, property, health, or life itself is removed.

### 5. Conflict, Coercion, and Survival
- Semantic invariant: Opposed parties threaten, attack, seize, divide, reconcile, or traverse danger in pursuit of survival and advantage.
- Surface relation: direct; killing and the trench community at 85:4, persecution at 85:10, overpowering force at 85:12, and armies at 85:17.
- Surprising reach: The conflict frame reaches competitive prestige, emotional feud, capture and attachment, truces, wilderness crossings, and water as the resource that makes a dangerous journey possible.

#### 5A. Assault and Warfare
- Reading type: surface-primary
- Scene or process: Organized forces launch a violent charge and sustain reciprocal combat.
- Active motifs: forceful seizure or attack `ب ط ش:B001/m01`; charging the enemy `ش د د:B003/m01`; reciprocal fighting `ق ت ل:B011/m01`; allied army `ج ن د:B001/m01`; war and civil strife `ف ت ن:B006/m01`.
- Ayah anchors: `ب ط ش` and `ش د د` at 85:12; `ق ت ل` at 85:4; `ج ن د` at 85:17; `ف ت ن` at 85:10.
- Synthesis: The army supplies collective agency, the charge initiates contact, violent seizure marks tactical force, and sustained reciprocal fighting turns assault into war.

#### 5B. Feud, Turmoil, and Agitation
- Reading type: latent/lexical
- Scene or process: Hostility spreads through a group, disturbs minds and speech, and fragments common judgment.
- Active motifs: interpersonal enmity `ن و ر:B007/m01`; confusion and clamorous mixing `ب ل ل:B009/m01`; factional conflict `ف ت ن:B006/m01`; bodily tremor `ء ر ض:B008/m01`; restless movement `ر و د:B004/m01`.
- Ayah anchors: `ن و ر` at 85:5; the `بَلْ` tokens at 85:19, 85:21; `ف ت ن` at 85:10; `ء ر ض` at 85:9; `ر و د` at 85:16.
- Synthesis: Conflict is traced from social enmity into its embodied and communicative effects: agitation, confused speech, tremor, and inability to settle.

#### 5C. Capture, Domination, and Incapacity
- Reading type: latent/lexical
- Scene or process: A stronger party grasps a target, attaches it to itself, and closes off escape or independent action.
- Active motifs: seizure and possession `ب ل ل:B004/m01`; overpowering a rival `ع ز ز:B002/m01`; violent grasp `ب ط ش:B001/m01`; engulfing defeat `ح و ط:B006/m01`; disabling inability to rise `ق ع د:B009/m01`.
- Ayah anchors: the `بَلْ` tokens at 85:19, 85:21; `ع ز ز` at 85:8; `ب ط ش` at 85:12; `ح و ط` at 85:20; `ق ع د` at 85:6.
- Synthesis: Domination is a sequence from taking hold to enclosing the captured party and finally reducing that party’s capacity to move or resist.

#### 5D. Reconciliation and Truce
- Reading type: latent/lexical
- Scene or process: Opposed parties cease hostility, exchange promises, and preserve a negotiated social peace.
- Active motifs: reconciliation after estrangement `ص ل ح:B002/m01`; reciprocal agreement `و ع د:B004/m01`; guarded covenant `ح ف ظ:B006/m01`; witnessed attendance `ش ه د:B001/m01`; social compatibility `ص ح ب:B004/m01`.
- Ayah anchors: `ص ل ح` at 85:11; `و ع د` at 85:2; `ح ف ظ` at 85:22; `ش ه د` at 85:3, 85:7, 85:9; `ص ح ب` at 85:4.
- Synthesis: Peace is not mere absence of fighting; it is a witnessed agreement whose terms are made compatible and then actively protected.

#### 5E. Wilderness Crossing and Survival
- Reading type: latent/lexical
- Scene or process: A traveler enters a waterless, dangerous expanse and survives by orientation, competition with hazard, and control of scarce water.
- Active motifs: perilous wilderness passage `ف و ز:B003/m01`; striving against peers or terrain `س م و:B007/m01`; incoming flood from elsewhere `ء ت ي:B005/m01`; water that secures a camp’s existence `م ل ك:B007/m01`; visible route marker `ن و ر:B005/m01`.
- Ayah anchors: `ف و ز` at 85:11; `س م و` at 85:1, 85:9; `ء ت ي` at 85:17; `م ل ك` at 85:9; `ن و ر` at 85:5.
- Synthesis: The paradoxical “place of survival” is completed by practical motifs: the crossing is dangerous, markers guide movement, and possession of water determines whether the party can continue.

### 6. Social Belonging, Care, and Exchange
- Semantic invariant: People become a social unit through companionship, assembly, descent, dependency, guardianship, generosity, livelihood, and marriage.
- Surface relation: direct; companions at 85:4, believers as a community at 85:7-11, witnessed presence at 85:3 and 85:7, and affectionate relation at 85:14.
- Surprising reach: The social frame includes stepchildren and nurses, inherited kinship, escorts, recurring gifts, wages, hospitality, wedding attendance, and dependents compared with livestock.

#### 6A. Companionship and Amity
- Reading type: mixed
- Scene or process: Persons remain together through compatible attachment, mutual affection, and repeated shared presence.
- Active motifs: companionship and sustained association `ص ح ب:B001/m01`; making one thing accompany another `ص ح ب:B004/m01`; mutual affection `و د د:B001/m01`; social attachment `ب ل ل:B004/m02`; witnessed presence `ش ه د:B001/m01`.
- Ayah anchors: `ص ح ب` at 85:4; `و د د` at 85:14; the `بَلْ` tokens at 85:19, 85:21; `ش ه د` at 85:3, 85:7, 85:9.
- Synthesis: Companionship is represented as a durable fit: parties stay present, attach to one another, and convert proximity into reciprocal affection.

#### 6B. Assembly, Community, and Collective Strata
- Reading type: mixed
- Scene or process: Individuals gather into an organized body that may contain allied forces, a majority, factions, and ranked groups.
- Active motifs: allied collectivity `ج ن د:B001/m01`; mass of the people `ج ن ن:B013/m01`; numerous community `ر ب ب:B004/m01`; class or faction `خ د د:B005/m01`; grouped bodies `ك ل ل:B009/m01`.
- Ayah anchors: `ج ن د` at 85:17; `ج ن ن` at 85:11; `ر ب ب` at 85:12; `خ د د` at 85:4; `ك ل ل` at 85:9.
- Synthesis: The same assembling process yields both solidarity and differentiation: a mass becomes a community, while internal classes and factions determine its structure.

#### 6C. Lineage, Ancestry, and Inheritance
- Reading type: latent/lexical
- Scene or process: Social identity and property move through descent, proximity to an ancestor, collateral kin, and grandchildren.
- Active motifs: closeness in genealogy `ق ع د:B012/m01`; collateral inheritance `ك ل ل:B004/m01`; descendant through the son `و ر ي:B007/m01`; child becoming an adult companion `ص ح ب:B005/m01`; attributed kinship `ذ و و:B001/m01`.
- Ayah anchors: `ق ع د` at 85:6; `ك ل ل` at 85:9; `و ر ي` at 85:20; `ص ح ب` at 85:4; the `ذَات/ذُو` tokens at 85:1, 85:5, 85:15.
- Synthesis: Genealogy defines both social nearness and legal succession, linking the named possessor to ancestors, collateral heirs, maturing children, and later descendants.

#### 6D. Childcare and Dependents
- Reading type: latent/lexical
- Scene or process: A household raises a child or stepchild and carries the material burden of those unable to provide for themselves.
- Active motifs: stepchild, nurse, or guardian `ر ب ب:B005/m01`; dependent or ward `ك ل ل:B002/m01`; household wealth and dependents `ق ر ء:B013/m01`; child reaching companionable adulthood `ص ح ب:B005/m01`; gradual upbringing `ر ب ب:B002/m02`.
- Ayah anchors: `ر ب ب` at 85:12; `ك ل ل` at 85:9; `ق ر ء` at 85:21; `ص ح ب` at 85:4.
- Synthesis: Care moves through stages: the child begins as a ward and material responsibility, is gradually raised, and eventually becomes a companion within the household.

#### 6E. Guardianship, Escort, and Protective Care
- Reading type: mixed
- Scene or process: A custodian accompanies a person or object, watches it, and intervenes when danger or dishonor approaches.
- Active motifs: guarding and tending `ح ف ظ:B001/m01`; protective encirclement and care `ح و ط:B002/m01`; divinely accompanied protection `ص ح ب:B002/m01`; repair and upbringing `ر ب ب:B002/m01`; protective zeal `ح ف ظ:B005/m01`.
- Ayah anchors: `ح ف ظ` at 85:22; `ح و ط` at 85:20; `ص ح ب` at 85:4; `ر ب ب` at 85:12.
- Synthesis: Escort supplies presence, vigilance supplies awareness, and encircling care supplies intervention, making protection an active relationship rather than a static barrier.

#### 6F. Gift, Hospitality, and Recurring Benefaction
- Reading type: latent/lexical
- Scene or process: A benefactor presents goods, maintains a flow of support, and receives gratitude or reputation for generosity.
- Active motifs: kin-supporting gift `ب ل ل:B002/m01`; continuing provision `ج ر ي:B006/m01`; abundant benefaction `م ج د:B006/m01`; favor that solicits praise `ح م د:B005/m01`; returned kindness `ع و د:B006/m01`; presentation of a gift `ء ت ي:B002/m01`.
- Ayah anchors: the `بَلْ` tokens at 85:19, 85:21; `ج ر ي` at 85:11; `م ج د` at 85:15, 85:21; `ح م د` at 85:8; `ع و د` at 85:13; `ء ت ي` at 85:17.
- Synthesis: Giving becomes a social current: the benefaction is presented, continues over time, returns as welfare to the recipient, and returns again as praise to the giver.

#### 6G. Marriage, Espousal, and Wedding Attendance
- Reading type: latent/lexical
- Scene or process: A marriage contract is concluded before witnesses and the bride is conveyed within a socially attended household transition.
- Active motifs: marriage contract and espousal `م ل ك:B004/m01`; marital or witnessed presence `ش ه د:B001/m03`; woman’s litter on a mount `ع ر ش:B005/m01`; attendant or spouse `ق ع د:B004/m01`; reciprocal pact `و ع د:B004/m01`.
- Ayah anchors: `م ل ك` at 85:9; `ش ه د` at 85:3, 85:7, 85:9; `ع ر ش` at 85:15; `ق ع د` at 85:6; `و ع د` at 85:2.
- Synthesis: Contract, reciprocal promise, witnessed presence, attendant roles, and conveyance form a complete wedding scene centered on a change of household status.

### 7. Enclosure, Habitation, and Route
- Semantic invariant: Space is organized by hiding, covering, surrounding, dwelling, orienting, supporting, excavating, and moving between places.
- Surface relation: direct; celestial enclosure at 85:1, the trench at 85:4, seating at 85:6, land and gardens at 85:9-11, the throne at 85:15, surrounding at 85:20, and the tablet at 85:22.
- Surprising reach: The spatial frame reaches veils, mosquito screens, fireplaces, bastions, lunar crowns, homecoming, road traces, unfinished wells, migration, foreignness, and ancient routes.

#### 7A. Concealment, Veil, and Cover
- Reading type: mixed
- Scene or process: An object is hidden from sense by being veiled, covered, placed behind something, or absorbed into darkness.
- Active motifs: sensory concealment `ج ن ن:B001/m01`; protective covering `غ ف ر:B001/m01`; physical covering `ك ف ر:B001/m01`; hiding behind an apparent meaning `و ر ي:B005/m01`; night as enveloping darkness `ج ن ن:B002/m01`.
- Ayah anchors: `ج ن ن` at 85:11; `غ ف ر` at 85:14; `ك ف ر` at 85:19; `و ر ي` at 85:20.
- Synthesis: Concealment ranges from material covering to darkness and semantic indirection, but each operation removes the object from direct access while leaving it present behind a screen.

#### 7B. Shelter, Canopy, and Refuge
- Reading type: latent/lexical
- Scene or process: A raised cover creates an inhabitable protected interior, sometimes centered on a hearth.
- Active motifs: roof, awning, or animal shelter `ع ر ش:B002/m01`; light tent or protective screen `ك ل ل:B006/m01`; hiding place or refuge `ج ن ن:B017/m01`; fireplace or hearth `و ق د:B003/m01`; fixed residence `ع ر ش:B012/m01`.
- Ayah anchors: `ع ر ش` at 85:15; `ك ل ل` at 85:9; `ج ن ن` at 85:11; `و ق د` at 85:5.
- Synthesis: Roof and screen define the boundary, refuge gives the enclosure its protective function, and the hearth turns it from mere cover into an occupied dwelling.

#### 7C. Wall, Bastion, and Perimeter
- Reading type: mixed
- Scene or process: A place is defended or delimited by an encircling wall, fortified tower, covered pass, or crown-like boundary.
- Active motifs: physical encirclement and walling `ح و ط:B001/m01`; fortified tower or castle `ب ر ج:B001/m01`; covered mountain pass or low wall `ك ف ر:B013/m01`; encircling crown or border `ك ل ل:B005/m01`; protective shield `ج ن ن:B008/m01`.
- Ayah anchors: `ح و ط` at 85:20; `ب ر ج` at 85:1; `ك ف ر` at 85:19; `ك ل ل` at 85:9; `ج ن ن` at 85:11.
- Synthesis: The motifs share a perimeter function: tower, wall, crown, pass, and shield arrange material around a vulnerable center to mark and defend it.

#### 7D. Residence, Permanence, and Homecoming
- Reading type: mixed
- Scene or process: A person settles, remains attached to a place, and treats it as the endpoint to which return is directed.
- Active motifs: clinging to the ground `ء ر ض:B006/m01`; dwelling and duration `ر ب ب:B007/m01`; fixed settlement `ع ر ش:B012/m01`; taking up residence `ق ع د:B016/m01`; destination and homecoming `ع و د:B002/m01`; persistent attachment `ب ل ل:B004/m02`.
- Ayah anchors: `ء ر ض` at 85:9; `ر ب ب` at 85:12; `ع ر ش` at 85:15; `ق ع د` at 85:6; `ع و د` at 85:13; the `بَلْ` tokens at 85:19, 85:21.
- Synthesis: Groundedness becomes social and temporal permanence: remaining creates residence, attachment gives it continuity, and return defines it as home.

#### 7E. Roads, Tracks, and Practiced Ways
- Reading type: latent/lexical
- Scene or process: A traversable way is laid out by route, trace, repeated use, and a method that keeps movement from losing direction.
- Active motifs: inhabited thoroughfare `ء ت ي:B010/m01`; road trace or rut `خ د د:B006/m01`; worked road `ع م ل:B011/m01`; customary way `ج ر ي:B002/m01`; method or pattern `ق ر ء:B011/m01`; central line of road or valley `م ل ك:B006/m01`; track that preserves its trace `ح ف ظ:B007/m01`.
- Ayah anchors: `ء ت ي` at 85:17; `خ د د` at 85:4; `ع م ل` and `ج ر ي` at 85:11; `ق ر ء` at 85:21; `م ل ك` at 85:9; `ح ف ظ` at 85:22.
- Synthesis: A route is both physical and procedural: repeated passage leaves a trace, trace becomes a road, and the road becomes a model for method and disciplined practice.

#### 7F. Foundations, Lower Levels, and Support
- Reading type: mixed
- Scene or process: An upper structure rests on a lower layer, base, or ground that carries its weight.
- Active motifs: foundation or structural base `ق ع د:B007/m01`; lower spatial region `ت ح ت:B001/m01`; ground opposed to sky `ء ر ض:B001/m01`; structural firmness `م ل ك:B001/m01`; fixed frame `ع ر ش:B004/m02`.
- Ayah anchors: `ق ع د` at 85:6; `ت ح ت` at 85:11; `ء ر ض` and `م ل ك` at 85:9; `ع ر ش` at 85:15.
- Synthesis: The lower region is not merely beneath; it is the load-bearing support whose firmness allows the visible structure above it to stand.

#### 7G. Trenches, Wells, and Excavated Channels
- Reading type: mixed
- Scene or process: Earth is cut to form a trench, well, or watercourse and then reinforced so that the excavation can function.
- Active motifs: long sunken trench `خ د د:B002/m01`; newly dug well `ب د ء:B008/m01`; unfinished well `ق ع د:B015/m01`; timbered wellhead and water station `ع ر ش:B004/m01`; river channel cut through earth `ن ه ر:B001/m01`; directed watercourse `ء ت ي:B004/m01`.
- Ayah anchors: `خ د د` at 85:4; `ب د ء` at 85:13; `ق ع د` at 85:6; `ع ر ش` at 85:15; `ن ه ر` at 85:11; `ء ت ي` at 85:17.
- Synthesis: Cutting creates the void, timber and foundation stabilize it, and directed flow converts the excavation into infrastructure rather than a mere hole.

#### 7H. Migration, Foreignness, and Relocation
- Reading type: latent/lexical
- Scene or process: A person leaves one land, enters another as an outsider, and negotiates exposure, route, and settlement.
- Active motifs: foreigner among another people `ء ت ي:B006/m01`; outsider “son of the land” `ء ر ض:B004/m01`; departure from one land to another `ب د ء:B005/m01`; exposure or confrontation on arrival `ء ر ض:B007/m01`; pedestrian traveler `ع م ل:B012/m01`; old or ancestral road `ع و د:B009/m01`.
- Ayah anchors: `ء ت ي` at 85:17; `ء ر ض` at 85:9; `ب د ء` and `ع و د` at 85:13; `ع م ل` at 85:11.
- Synthesis: Migration joins departure, route, and arrival to a social role: the traveler crosses by an inherited way but enters the destination marked as foreign.

### 8. Celestial, Atmospheric, and Calendrical Order
- Semantic invariant: The upper world organizes space and time through sky, stars, daylight, cloud, rain, flood, season, calendar, and recurring festival.
- Surface relation: direct; sky and constellations at 85:1, the promised day at 85:2, firelight at 85:5, heavens and earth at 85:9, and flowing rivers at 85:11.
- Surprising reach: The channel includes ceilings and open air, lunar stations, Pleiades-like star groups, the rising strength of day, foreign floodwater, summer heat, ritual months, and festival attendance.

#### 8A. Sky, Ceiling, and Open Atmosphere
- Reading type: mixed
- Scene or process: An upper cover arches over the ground while open air and layered cloud occupy the interval.
- Active motifs: sky, ceiling, and overhanging upper region `س م و:B004/m01`; open air between earth and sky `ل و ح:B004/m01`; layered cloud `ر ب ب:B008/m01`; cloud mass `ن ه ر:B008/m01`; uncovered exposure to the sky `ع ذ ب:B004/m01`.
- Ayah anchors: `س م و` at 85:1, 85:9; `ل و ح` at 85:22; `ر ب ب` at 85:12; `ن ه ر` at 85:11; `ع ذ ب` at 85:10.
- Synthesis: Sky functions simultaneously as cover and spatial field: cloud layers occupy its open interval, while exposure is defined by the absence of any intervening shelter.

#### 8B. Stars, Constellations, and Celestial Markers
- Reading type: mixed
- Scene or process: Recurrent star groups divide and mark the upper field for orientation and timekeeping.
- Active motifs: celestial stations and constellations `ب ر ج:B002/m01`; named star throne or cluster `ع ر ش:B008/m01`; three-star lunar station `غ ف ر:B006/m01`; astronomical indicator `ش ه د:B008/m01`; lunar crown or station `ك ل ل:B005/m02`.
- Ayah anchors: `ب ر ج` and `س م و` at 85:1; `ع ر ش` at 85:15; `غ ف ر` at 85:14; `ش ه د` at 85:3, 85:7, 85:9; `ك ل ل` at 85:9.
- Synthesis: Constellations, star-thrones, lunar stations, and indicators convert the sky from undifferentiated height into a legible system of positions.

#### 8C. Daylight, Sunrise, and the Height of Day
- Reading type: mixed
- Scene or process: Light opens the day, rises toward its strongest point, and then passes into concealment.
- Active motifs: bounded daylight `ي و م:B001/m01`; opened day and brightness `ن ه ر:B002/m01`; high noon or elevated day `ش د د:B005/m01`; prime of day `ك ب ر:B013/m01`; sunset or darkness that covers `ك ف ر:B002/m02`; course of sun or light `ج ر ي:B001/m02`.
- Ayah anchors: `ي و م` at 85:2; `ن ه ر` and `ج ر ي` at 85:11; `ش د د` at 85:12; `ك ب ر` at 85:11; `ك ف ر` at 85:19.
- Synthesis: Day is a cycle of opening, ascent, culmination, motion, and covering, so temporal passage is rendered as a changing geometry of light.

#### 8D. Cloud, Rain, Flood, and Seasonal Heat
- Reading type: latent/lexical
- Scene or process: Atmospheric intensity accumulates as cloud, produces rain or a foreign flood, and alternates with severe seasonal heat.
- Active motifs: violent rain or flood `ع ز ز:B008/m01`; flood arriving from another country `ء ت ي:B005/m01`; rain-bearing cloud `ر ب ب:B008/m02`; extreme summer heat `و ق د:B004/m01`; sky and rain source `س م و:B004/m02`.
- Ayah anchors: `ع ز ز` at 85:8; `ء ت ي` at 85:17; `ر ب ب` at 85:12; `و ق د` at 85:5; `س م و` at 85:1, 85:9.
- Synthesis: Weather is organized by force and transfer: cloud gathers overhead, precipitation gains intensity, floodwater crosses territorial boundaries, and heat marks the opposing seasonal extreme.

#### 8E. Calendar, Appointment, and Festival Return
- Reading type: mixed
- Scene or process: A promised time becomes a calendrical appointment that communities repeatedly attend as festival or rite.
- Active motifs: appointed time or place `و ع د:B003/m01`; month of suspended travel `ق ع د:B014/m01`; recurring festival `ع و د:B007/m01`; ritual attendance `ش ه د:B001/m02`; bounded duration `ي و م:B002/m01`.
- Ayah anchors: `و ع د` and `ي و م` at 85:2; `ق ع د` at 85:6; `ع و د` at 85:13; `ش ه د` at 85:3, 85:7, 85:9.
- Synthesis: Promise fixes expectation, the calendar fixes its time, and repeated communal attendance converts the appointment into a festival cycle.

### 9. Fire, Radiance, and Visible Transformation
- Semantic invariant: Stored energy is kindled, becomes flame and heat, alters material, and yields light, flash, mark, or visible sign.
- Surface relation: direct; fire and fuel at 85:5, burning punishment at 85:10, and the visible tablet at 85:22.
- Surprising reach: The fire scene extends to assaying, firesticks, hearths, scorching flavor and skin, lightning, smiles compared with flashes, polished brilliance, road signs, and bodily indicators.

#### 9A. Ignition, Kindling, and Fuel
- Reading type: mixed
- Scene or process: A latent spark is struck, fed with fuel, and intensified into sustained combustion.
- Active motifs: hidden fire emerging from a firestick `و ر ي:B002/m01`; active ignition and burning `و ق د:B001/m01`; fuel or kindling `و ق د:B002/m01`; wood prolific in fire `م ج د:B005/m01`; rapid flare or fervor `و ق د:B005/m01`.
- Ayah anchors: `و ر ي` at 85:20; `و ق د` and `ن و ر` at 85:5; `م ج د` at 85:15, 85:21.
- Synthesis: The mechanism begins with fire stored in wood, proceeds through striking and feeding, and culminates in a flame whose vigor can also figure emotional or martial fervor.

#### 9B. Blaze, Scorching, and Material Change
- Reading type: mixed
- Scene or process: Flame acts on a body or material, causing pain, blackening, discoloration, or loss of form.
- Active motifs: consuming blaze `ح ر ق:B002/m01`; burning and blackening by fire `ف ت ن:B002/m01`; visible alteration by heat `ل و ح:B002/m01`; stinging or burning pain `ح ر ق:B003/m01`; trial by heat `ف ت ن:B001/m02`.
- Ayah anchors: `ح ر ق` and `ف ت ن` at 85:10; `ل و ح` at 85:22.
- Synthesis: Heat is both destructive and diagnostic: it burns and discolors, but the resulting visible change also reveals what the material or person can withstand.

#### 9C. Fire Tools and Hearth
- Reading type: latent/lexical
- Scene or process: Fire is produced and contained through a striker, fire-bearing implement, hearth, and suitable wood.
- Active motifs: fire-making implement `ح ر ق:B008/m01`; hearth or fireplace `و ق د:B003/m01`; successful firestick and practical aid `و ر ي:B003/m01`; wooden or incense stick `ع و د:B010/m02`; fire-rich wood `م ج د:B005/m01`.
- Ayah anchors: `ح ر ق` at 85:10; `و ق د` at 85:5; `و ر ي` at 85:20; `ع و د` at 85:13; `م ج د` at 85:15, 85:21.
- Synthesis: This is the technical counterpart of combustion: selected material, striker, and hearth cooperate to turn potential heat into a controlled domestic flame.

#### 9D. Radiance, Gleam, and Flash
- Reading type: mixed
- Scene or process: Light appears abruptly or continuously as illumination, polished gleam, lightning, or a flash compared with a smile.
- Active motifs: illumination and brightness `ن و ر:B001/m01`; visible gleam `ل و ح:B001/m01`; fire-like sparkle `و ق د:B006/m01`; flashing smile or lightning `ك ل ل:B011/m01`; lightning-like surge `ح ر ق:B005/m01`.
- Ayah anchors: `ن و ر` at 85:5; `ل و ح` at 85:22; `و ق د` at 85:5; `ك ل ل` at 85:9; `ح ر ق` at 85:10.
- Synthesis: Fire, lightning, polished surfaces, and teeth share a sudden visibility signature, allowing physical radiance to extend naturally into beauty and expression.

#### 9E. Visibility, Indicator, and Farsight
- Reading type: latent/lexical
- Scene or process: An elevated or conspicuous form becomes a sign that can be detected from afar and used to infer a hidden state.
- Active motifs: high visible figure `س م و:B002/m01`; diagnostic sign or marker `ش ه د:B008/m02`; long-distance vision `ش ي ء:B003/m01`; broad clear eye `ب ر ج:B004/m01`; route beacon `ن و ر:B005/m01`.
- Ayah anchors: `س م و` at 85:1, 85:9; `ش ه د` at 85:3, 85:7, 85:9; `ش ي ء` at 85:9; `ب ر ج` at 85:1; `ن و ر` at 85:5.
- Synthesis: Height and contrast make the sign visible, farsight detects it, and interpretation converts appearance into evidence about time, quality, route, or condition.

### 10. Water, Nourishment, and Cultivated Growth
- Semantic invariant: Water flows, moistens, sweetens, sustains, fills, and enables plants, food, and bodies to grow.
- Surface relation: direct; water-bearing heavens and earth at 85:9 and gardens with flowing rivers at 85:11.
- Surprising reach: The channel reaches dew and damp wind, algae-covered surfaces, diluted drink, satiety and fasting, palm seedlings, trellises, blossoms, sweet plant exudates, honeycomb, camphor, syrup, and gruel.

#### 10A. Streams, Irrigation, and Directed Flow
- Reading type: surface-primary
- Scene or process: Water moves through a natural or engineered channel and is directed toward a field, basin, or settlement.
- Active motifs: flowing water `ج ر ي:B001/m01`; river cut through the land `ن ه ر:B001/m01`; guided watercourse `ء ت ي:B004/m01`; timbered water station `ع ر ش:B004/m01`; abundant water securing habitation `م ل ك:B007/m01`.
- Ayah anchors: `ج ر ي` and `ن ه ر` at 85:11; `ء ت ي` at 85:17; `ع ر ش` at 85:15; `م ل ك` at 85:9.
- Synthesis: Natural flow becomes infrastructure when a channel captures it, a station controls it, and the resulting supply makes cultivation and settlement possible.

#### 10B. Dampness, Dew, and Wet Air
- Reading type: latent/lexical
- Scene or process: Moisture settles on surfaces, remains in containers, and moves gently through wind or air.
- Active motifs: wetness and dew `ب ل ل:B001/m01`; gentle moist movement `ر و د:B005/m01`; rain-bearing sky `س م و:B004/m02`; open atmospheric interval `ل و ح:B004/m01`; water arriving as yield `ء ت ي:B007/m02`.
- Ayah anchors: the `بَلْ` tokens at 85:19, 85:21; `ر و د` at 85:16; `س م و` at 85:1, 85:9; `ل و ح` at 85:22; `ء ت ي` at 85:17.
- Synthesis: The scene is one of low-intensity water transfer: moisture is carried in air, settles as dew, and remains as the wet residue that sustains living surfaces.

#### 10C. Sweet Water, Algae, and Drinkable Supply
- Reading type: latent/lexical
- Scene or process: A community secures abundant potable water whose surface condition and taste determine its usefulness.
- Active motifs: abundant sweet water `ر ب ب:B013/m01`; sweet palatable liquid `ع ذ ب:B001/m01`; water that secures subsistence `م ل ك:B007/m01`; algae covering water `ص ح ب:B007/m01`; mixing water into strong drink `ق ت ل:B007/m01`.
- Ayah anchors: `ر ب ب` at 85:12; `ع ذ ب` at 85:10; `م ل ك` at 85:9; `ص ح ب` at 85:4; `ق ت ل` at 85:4.
- Synthesis: Water is evaluated as a managed provision: quantity enables settlement, sweetness enables drinking, surface growth signals condition, and dilution moderates stronger liquids.

#### 10D. Satiety, Abundance, and Abstinence
- Reading type: latent/lexical
- Scene or process: Food or pasture fills a body or container, while fasting, thirst, and scarcity define the opposing state.
- Active motifs: bodily or pastoral fullness `م ج د:B004/m01`; broad provision in food and drink `ب ر ج:B009/m01`; filled sack or full volume `ق ع د:B011/m01`; refusal or inability to eat and drink `ع ذ ب:B002/m01`; thickened sustaining food `ر ب ب:B006/m01`.
- Ayah anchors: `م ج د` at 85:15, 85:21; `ب ر ج` at 85:1; `ق ع د` at 85:6; `ع ذ ب` at 85:10; `ر ب ب` at 85:12.
- Synthesis: Fullness is legible in bodies, pasture, and containers, while abstinence and thirst expose the same nourishment system through deprivation.

#### 10E. Garden, Palm, Trellis, and Blossom
- Reading type: mixed
- Scene or process: Fertile ground receives seed, supports young palms and trees, and carries growth from covered shoot to flower.
- Active motifs: enclosed garden `ج ن ن:B003/m01`; dense vigorous vegetation `ج ن ن:B011/m01`; fertile planted ground `ء ر ض:B002/m01`; persistent green plant `ر ب ب:B012/m01`; palm seedlings `ش ي ء:B006/m01`; blossom `ن و ر:B004/m01`; supporting trellis `ع ر ش:B003/m01`; seed-covering cultivation `ك ف ر:B008/m01`.
- Ayah anchors: `ج ن ن` at 85:11; `ء ر ض` at 85:9; `ر ب ب` at 85:12; `ش ي ء` at 85:9; `ن و ر` at 85:5; `ع ر ش` at 85:15; `ك ف ر` at 85:19.
- Synthesis: Cultivation is a staged mechanism: earth receives covered seed, the shoot emerges, support directs its growth, foliage encloses the garden, and flowering marks maturity.

#### 10F. Plant Exudates, Honeycomb, and Aromatics
- Reading type: latent/lexical
- Scene or process: Trees and flowers produce sweet or aromatic substances that are gathered, thickened, stored, or consumed.
- Active motifs: sweet tree gum or exudate `غ ف ر:B007/m01`; honey held in wax `ش ه د:B007/m01`; fruit sheath or calyx `ك ف ر:B010/m01`; camphor and fragrant plant `ك ف ر:B011/m01`; thick syrup or food preparation `ر ب ب:B006/m01`.
- Ayah anchors: `غ ف ر` at 85:14; `ش ه د` at 85:3, 85:7, 85:9; `ك ف ر` at 85:19; `ر ب ب` at 85:12.
- Synthesis: Protective plant coverings become reservoirs of value: calyx, bark, and wax hold sweet or aromatic matter that can be collected and processed.

#### 10G. Gruel, Syrup, and Prepared Provision
- Reading type: latent/lexical
- Scene or process: Raw liquid and grain are heated or thickened into sustaining food and adjusted for taste or strength.
- Active motifs: thick gruel or soup `ح ر ق:B009/m01`; thickened syrup or corrective mixture `ر ب ب:B006/m01`; palatable sweetness `ع ذ ب:B001/m01`; moderated drink `ق ت ل:B007/m01`; fullness produced by provision `م ج د:B004/m01`.
- Ayah anchors: `ح ر ق` at 85:10; `ر ب ب` at 85:12; `ع ذ ب` at 85:10; `ق ت ل` at 85:4; `م ج د` at 85:15, 85:21.
- Synthesis: Heating, thickening, sweetening, and dilution form a small food technology whose outcome is palatable nourishment and satiety.

### 11. Generation, Life Stages, and Bodily Health
- Semantic invariant: Living bodies mate, gestate, give birth, mature, age, suffer injury or disease, and recover through identifiable anatomical and physiological states.
- Surface relation: indirect; the active roots occur throughout 85:3-13, but most bodily scenes arise from lexical senses rather than the surface propositions.
- Surprising reach: The channel includes estrous livestock, womb contents, afterbirth, puberty, menopause, maidens, chest bones, hips, forelegs, marrow, gauntness, lung disease, infected ulcers, epidemics, relapse, and convalescence.

#### 11A. Mating, Estrus, and Animal Sexuality
- Reading type: latent/lexical
- Scene or process: A female enters estrus, a male signals and mounts, and observers test whether mating or conception has occurred.
- Active motifs: female seeking the male `ء ت ي:B012/m01`; estrous cycle and mating test `ق ر ء:B009/m01`; stallion mounting the herd `س م و:B003/m01`; bellow before sexual charge `و ع د:B005/m01`; copulation `ح ر ق:B006/m01`; difficult milk and reproductive effort `ع ز ز:B006/m01`.
- Ayah anchors: `ء ت ي` at 85:17; `ق ر ء` at 85:21; `س م و` at 85:1, 85:9; `و ع د` at 85:2; `ح ر ق` at 85:10; `ع ز ز` at 85:8.
- Synthesis: Cycle, signal, approach, mounting, and post-mating inspection form a complete reproductive behavior sequence rather than a generic sexuality cluster.

#### 11B. Womb and Gestation
- Reading type: latent/lexical
- Scene or process: A fetus is enclosed in the womb and carried together with blood and other concealed contents until birth.
- Active motifs: fetus hidden in the abdomen `ج ن ن:B007/m01`; womb gathering fetus or blood `ق ر ء:B003/m01`; child continuing through descent `و ر ي:B007/m01`; recent maternity `ر ب ب:B009/m01`; maternal womb `ع ذ ب:B009/m02`.
- Ayah anchors: `ج ن ن` at 85:11; `ق ر ء` at 85:21; `و ر ي` at 85:20; `ر ب ب` at 85:12; `ع ذ ب` at 85:10.
- Synthesis: Enclosure is physiological here: the womb gathers and hides developing life, links it to descent, and moves toward the state of recent maternity.

#### 11C. Birth Residues, Puberty, and Menopause
- Reading type: latent/lexical
- Scene or process: Birth and sexual maturation are marked by blood, afterbirth, discharge, menstruation, and its eventual cessation.
- Active motifs: afterbirth and maturation discharge `ش ه د:B006/m01`; postpartum matter from the womb `ع ذ ب:B009/m01`; expelled fetal or blood material `ق ر ء:B003/m02`; delayed or retained reproductive cycle `ق ر ء:B004/m01`; recent birth and milk `ر ب ب:B009/m01`; cessation of menstruation and marriageability `ق ع د:B003/m01`.
- Ayah anchors: `ش ه د` at 85:3, 85:7, 85:9; `ع ذ ب` at 85:10; `ق ر ء` at 85:21; `ر ب ب` at 85:12; `ق ع د` at 85:6.
- Synthesis: Reproductive time is read through bodily signs, from birth residue and first maturation discharge to cyclic retention and the later cessation of fertility.

#### 11D. Youth, Maidenhood, Adulthood, and Aging
- Reading type: latent/lexical
- Scene or process: A person moves from fresh youth through mature strength into experienced old age.
- Active motifs: youthful freshness `ح د ث:B002/m01`; beginning of youth `ج ن ن:B014/m01`; young maiden `ر و د:B008/m01`; completion of adult strength `ش د د:B004/m01`; child becoming an adult companion `ص ح ب:B005/m01`; aged animal or experienced elder `ع و د:B008/m01`; old age `ك ب ر:B004/m01`.
- Ayah anchors: `ح د ث` at 85:17; `ج ن ن` at 85:11; `ر و د` at 85:16; `ش د د` at 85:12; `ص ح ب` at 85:4; `ع و د` at 85:13; `ك ب ر` at 85:11.
- Synthesis: Life stage is defined relationally as well as biologically: freshness becomes attractiveness, strength becomes adult competence, and age becomes companionship and accumulated experience.

#### 11E. Chest, Hip, Limb, and Foreleg Anatomy
- Reading type: latent/lexical
- Scene or process: The body is mapped through load-bearing and moving structures of chest, hip, foot, and limb.
- Active motifs: chest bones and rib ends `ج ن ن:B016/m01`; chest or breast `ك ل ل:B007/m01`; prominent breast `ق ع د:B011/m02`; hip points `ع ز ز:B010/m01`; hip tendon `ح ر ق:B007/m01`; neck and upper foot structures `ع ر ش:B007/m01`; working limbs or eye `ع م ل:B010/m01`; camel foreleg gait `ء ت ي:B009/m01`.
- Ayah anchors: `ج ن ن` at 85:11; `ك ل ل` at 85:9; `ق ع د` at 85:6; `ع ز ز` at 85:8; `ح ر ق` at 85:10; `ع ر ش` at 85:15; `ع م ل` at 85:11; `ء ت ي` at 85:17.
- Synthesis: The motifs form a functional anatomy: chest and ribs stabilize the trunk, hip and foot transfer force, and limbs or forelegs enact movement.

#### 11F. Flesh, Marrow, and Gauntness
- Reading type: latent/lexical
- Scene or process: Bodily condition is read from the amount and distribution of flesh, fat, and marrow.
- Active motifs: full flesh, fat, and marrow `و ر ي:B004/m01`; wasted or contracted flesh `خ د د:B003/m01`; bodily fullness `م ج د:B004/m02`; hard compact flesh `ع ز ز:B007/m02`; aged residual strength `ع و د:B008/m01`.
- Ayah anchors: `و ر ي` at 85:20; `خ د د` at 85:4; `م ج د` at 85:15, 85:21; `ع ز ز` at 85:8; `ع و د` at 85:13.
- Synthesis: Plumpness and gauntness are opposing surface signatures of internal reserves, with marrow, firmness, and remaining strength indicating bodily viability.

#### 11G. Lung Disease, Infection, and Epidemic
- Reading type: latent/lexical
- Scene or process: Illness penetrates the chest or wound, produces pus or decay, spreads through a place, and overwhelms the patient.
- Active motifs: lung or internal suppurating disease `و ر ي:B001/m01`; infected ulcer `ء ر ض:B011/m01`; regional epidemic `ق ر ء:B008/m01`; overpowering illness `ع ز ز:B009/m01`; fatal calamity or severe sickness `ء ت ي:B011/m01`.
- Ayah anchors: `و ر ي` at 85:20; `ء ر ض` at 85:9; `ق ر ء` at 85:21; `ع ز ز` at 85:8; `ء ت ي` at 85:17.
- Synthesis: The scene moves from local lesion to internal infection and then to spatial spread, while overpowering force describes the patient’s declining control.

#### 11H. Recovery, Relapse, and Convalescent Visit
- Reading type: latent/lexical
- Scene or process: A patient improves, is revisited and cared for, or falls back into a worse condition.
- Active motifs: recovery and restored health `ب ل ل:B003/m01`; relapse of wound or disease `غ ف ر:B004/m01`; repeated sick visit or condolence `ع و د:B005/m01`; repair after damage `ص ل ح:B001/m02`; severe illness that threatens life `ء ت ي:B011/m01`.
- Ayah anchors: the `بَلْ` tokens at 85:19, 85:21; `غ ف ر` at 85:14; `ع و د` at 85:13; `ص ل ح` at 85:11; `ء ت ي` at 85:17.
- Synthesis: Health is a reversible process: repair produces improvement, social visitation accompanies convalescence, and relapse reopens the earlier wound or disease.

#### 11I. Eye, Gaze, and Bodily Beauty
- Reading type: latent/lexical
- Scene or process: A clear broad eye perceives at distance, while gaze, visible form, and bodily proportion generate judgments of beauty.
- Active motifs: broad clear eye `ب ر ج:B004/m01`; moving defect in the eye `ر و د:B007/m01`; distant sight `ش ي ء:B003/m01`; visible bodily handsomeness `ب ر ج:B010/m01`; diagnostic sign `ش ه د:B008/m02`; elevated visible form `س م و:B002/m01`.
- Ayah anchors: `ب ر ج` at 85:1; `ر و د` at 85:16; `ش ي ء` at 85:9; `ش ه د` at 85:3, 85:7, 85:9; `س م و` at 85:1, 85:9.
- Synthesis: Vision and beauty are reciprocal: the eye is itself an object of beauty, detects distant form, and uses visible signs to judge condition and proportion.

### 12. Animal Management, Hunting, and Mobility
- Semantic invariant: Animals and travelers are gathered, trained, mounted, tracked, and read through gait, cry, and bodily signal.
- Surface relation: indirect; the relevant roots occur at 85:1, 85:4, 85:6, 85:9, 85:11, and 85:17, while the animal scenes are lexical.
- Surprising reach: The channel includes cattle drives, donkey posture, saddle covers, taming, mounted litters, hunting blinds, falcon decoys, estrous calls, camel forelegs, and pedestrians.

#### 12A. Herding, Livestock, and the Drove
- Reading type: latent/lexical
- Scene or process: A herder gathers dispersed animals, drives them as a unit, and manages their posture, color, and dependent burden.
- Active motifs: cattle or wild herd `ر ب ب:B014/m01`; gathering and driving a drove `ح و ط:B003/m01`; donkey raising its head over the herd `ع ر ش:B009/m01`; livestock wealth and dependents `ق ر ء:B013/m01`; burden or dependent `ك ل ل:B002/m01`; reddish donkey coloring `ص ح ب:B008/m01`.
- Ayah anchors: `ر ب ب` at 85:12; `ح و ط` at 85:20; `ع ر ش` at 85:15; `ق ر ء` at 85:21; `ك ل ل` at 85:9; `ص ح ب` at 85:4.
- Synthesis: The drove is a managed collective: animals are gathered, led, observed through bodily cues, and valued as both property and burden-bearing support.

#### 12B. Riding, Saddle, and Taming
- Reading type: latent/lexical
- Scene or process: A difficult animal is trained to submit, fitted with riding equipment, mounted, and directed by a leading limb or guide.
- Active motifs: mount and saddle `ق ع د:B008/m01`; mounting an animal `ع ر ش:B011/m01`; tractability after resistance `ص ح ب:B003/m01`; taming by repeated handling `ق ت ل:B002/m01`; leading animal or guiding limb `م ل ك:B008/m01`; leather saddle cover `ف ت ن:B008/m01`.
- Ayah anchors: `ق ع د` at 85:6; `ع ر ش` at 85:15; `ص ح ب` and `ق ت ل` at 85:4; `م ل ك` at 85:9; `ف ت ن` at 85:10.
- Synthesis: Training changes the animal’s relation to force, equipment stabilizes the rider, and the trained body becomes a coordinated conveyance.

#### 12C. Hunting, Scouting, and Falconry
- Reading type: latent/lexical
- Scene or process: Hunters leave the settlement, scout pasture or prey, wait in concealment, and use a decoy to draw a raptor within reach.
- Active motifs: going out to hunt `س م و:B006/m01`; scouting pasture or prey `ر و د:B003/m01`; watchful ambush `ق ع د:B005/m01`; owl decoy for falconry `ل و ح:B008/m01`; animal running then stopping to look back `ك ذ ب:B007/m01`; protective watch `ح ف ظ:B004/m02`.
- Ayah anchors: `س م و` at 85:1, 85:9; `ر و د` at 85:16; `ق ع د` at 85:6; `ل و ح` at 85:22; `ك ذ ب` at 85:19; `ح ف ظ` at 85:22.
- Synthesis: Scouting locates the target, concealment and patience create the ambush, and the decoy manipulates the prey’s own visual attention.

#### 12D. Gait, Cry, and Animal Signal
- Reading type: latent/lexical
- Scene or process: Animal condition and intention are inferred from foreleg motion, mounting posture, bellow, birdsong, and interruption of flight.
- Active motifs: camel foreleg return in gait `ء ت ي:B009/m01`; stallion’s mounting posture `س م و:B003/m01`; threatening bellow before charge `و ع د:B005/m01`; bird call or moan `ب ل ل:B010/m01`; running then halting to inspect `ك ذ ب:B007/m01`; condition marker `ش ه د:B008/m02`.
- Ayah anchors: `ء ت ي` at 85:17; `س م و` at 85:1, 85:9; `و ع د` at 85:2; the `بَلْ` tokens at 85:19, 85:21; `ك ذ ب` at 85:19; `ش ه د` at 85:3, 85:7, 85:9.
- Synthesis: Motion and sound operate as a semiotic system: gait, cry, posture, and pause reveal readiness, aggression, fatigue, or reproductive state.

### 13. Labor, Craft, and Material Mechanisms
- Semantic invariant: Skilled agents transform materials through work, repair, rotation, cutting, binding, covering, transport, gaming apparatus, and surface treatment.
- Surface relation: mixed; action and work at 85:7, 85:11, 85:16 and the tablet at 85:22 provide direct anchors, while most tools and materials are lexical.
- Surprising reach: The channel includes carpenters and digging crews, mill and pulley pivots, termite-eaten timber, tassels, hairy hides, filing, incendiary ships, gambling arrows, depilatory lime, tattoo soot, and colored cloth.

#### 13A. Worker, Carpenter, and Crew
- Reading type: mixed
- Scene or process: Skilled and manual laborers organize around construction, digging, travel, and paid work.
- Active motifs: carpenter or workman `ف ع ل:B003/m01`; hand-working crew `ع م ل:B006/m01`; pedestrian work-travelers `ع م ل:B012/m01`; wage or stipend `ع م ل:B004/m01`; assigned office of work `ع م ل:B003/m01`.
- Ayah anchors: `ف ع ل` at 85:7, 85:16; `ع م ل` at 85:11.
- Synthesis: The scene differentiates craft role, crew, mobility, compensation, and supervision, presenting labor as an organized social and technical system.

#### 13B. Operation, Repair, and Application
- Reading type: mixed
- Scene or process: An agent applies a tool or process to repair, complete, strengthen, or activate an object.
- Active motifs: using or setting something to work `ع م ل:B002/m01`; gradual repair and completion `ر ب ب:B002/m01`; restoration opposed to corruption `ص ل ح:B001/m02`; effect-producing action `ف ع ل:B001/m01`; material cohesion and strength `م ل ك:B001/m01`.
- Ayah anchors: `ع م ل` at 85:11; `ر ب ب` at 85:12; `ص ل ح` at 85:11; `ف ع ل` at 85:7, 85:16; `م ل ك` at 85:9.
- Synthesis: Application supplies controlled action, repair supplies direction, and cohesion or completion supplies the finished state of the worked material.

#### 13C. Timber, Rotation, Tablet, and Termite
- Reading type: mixed
- Scene or process: Wood is selected, shaped into a board or rotating implement, installed in machinery, and exposed to material decay.
- Active motifs: timber or wooden implement `ع و د:B010/m01`; pivot, mill handle, or pulley axle `ر و د:B006/m01`; circular operation `ح و ط:B005/m01`; board or writing tablet `ل و ح:B003/m01`; wood-eating termite `ء ر ض:B010/m01`.
- Ayah anchors: `ع و د` at 85:13; `ر و د` at 85:16; `ح و ط` at 85:20; `ل و ح` at 85:22; `ء ر ض` at 85:9.
- Synthesis: Timber shifts roles from material to inscribed surface to moving machine part, while termite damage supplies the mechanism’s natural failure mode.

#### 13D. Cordage, Tassel, and Ornament
- Reading type: latent/lexical
- Scene or process: Flexible strands are tied, hung, beaded, or arranged as decorative edging on dress, tack, or conveyance.
- Active motifs: dangling strap, cord, or tassel `ع ذ ب:B006/m01`; circular beaded ornament `ح و ط:B007/m01`; encircling crown or garland `ك ل ل:B005/m01`; woman’s ornamented litter `ع ر ش:B005/m01`; patterned decorative cloth `ك ذ ب:B009/m01`.
- Ayah anchors: `ع ذ ب` at 85:10; `ح و ط` at 85:20; `ك ل ل` at 85:9; `ع ر ش` at 85:15; `ك ذ ب` at 85:19.
- Synthesis: The shared mechanism is flexible attachment: cords suspend, beads encircle, patterned cloth covers, and the assembled ornament marks a body or conveyance.

#### 13E. Leather, Hair, and Material Coverings
- Reading type: latent/lexical
- Scene or process: Animal skin is removed, retained with hair, used as a cover, or altered as its surface fibers shed.
- Active motifs: hide retaining hair or wool `ص ح ب:B006/m01`; leather saddle covering `ف ت ن:B008/m01`; fuzz or raised surface fibers `غ ف ر:B003/m01`; hair shedding or scorching `ح ر ق:B004/m01`; protective covering `غ ف ر:B001/m02`.
- Ayah anchors: `ص ح ب` at 85:4; `ف ت ن` and `ح ر ق` at 85:10; `غ ف ر` at 85:14.
- Synthesis: Skin moves from body surface to worked material, while retention, shedding, and covering describe successive choices in its preparation and use.

#### 13F. Scraping, Filing, and Surface Abrasion
- Reading type: latent/lexical
- Scene or process: A hard edge or surface is rubbed, filed, blunted, or visibly altered by friction.
- Active motifs: hot scraping or filing `ح ر ق:B001/m01`; wetting during abrasion `ب ل ل:B001/m02`; loss of sharpness `ك ل ل:B001/m02`; visible surface alteration `ل و ح:B002/m01`; polishing and renewal `ح د ث:B007/m01`.
- Ayah anchors: `ح ر ق` at 85:10; the `بَلْ` tokens at 85:19, 85:21; `ك ل ل` at 85:9; `ل و ح` at 85:22; `ح د ث` at 85:17.
- Synthesis: Friction removes material and sharpness, moisture moderates the operation, and polishing can reverse dullness by restoring a visible finish.

#### 13G. Ship, Incendiary Vessel, and Naval Crew
- Reading type: latent/lexical
- Scene or process: A large vessel is built from planks, commanded by a captain, and equipped to project fire in combat.
- Active motifs: large warship `ب ر ج:B007/m01`; fire-bearing vessel or implement `ح ر ق:B008/m02`; ship planks `ل و ح:B003/m03`; captain of sailors `ر ب ب:B017/m01`; military pavilion or camp structure `ف و ز:B004/m01`.
- Ayah anchors: `ب ر ج` at 85:1; `ح ر ق` at 85:10; `ل و ح` at 85:22; `ر ب ب` at 85:12; `ف و ز` at 85:11.
- Synthesis: Hull material, command role, incendiary equipment, and martial encampment combine into a specific naval warfare scene.

#### 13H. Gambling Arrows and Gaming Kit
- Reading type: latent/lexical
- Scene or process: Marked lots are stored, drawn, and interpreted within a portable gaming apparatus.
- Active motifs: leather case holding gaming arrows `ر ب ب:B010/m01`; winning lot drawn for its owner `ف و ز:B001/m02`; dangling marker or cord `ع ذ ب:B006/m01`; circular or beaded ornament `ح و ط:B007/m01`; patterned deceptive cloth `ك ذ ب:B009/m01`.
- Ayah anchors: `ر ب ب` at 85:12; `ف و ز` at 85:11; `ع ذ ب` at 85:10; `ح و ط` at 85:20; `ك ذ ب` at 85:19.
- Synthesis: Container, lots, markers, and decorated covering form a coherent portable kit in which a random draw is converted into an assigned outcome.

#### 13I. Depilation, Tattooing, and Surface Marking
- Reading type: latent/lexical
- Scene or process: Hair and skin are prepared, coated, pierced, darkened, or decorated to change visible bodily appearance.
- Active motifs: depilatory lime coating `ن و ر:B009/m01`; soot used for tattoo or eye cosmetic `ن و ر:B008/m01`; surface fuzz or hair `غ ف ر:B003/m01`; heat-altered skin color `ل و ح:B002/m01`; circular body ornament `ح و ط:B007/m01`.
- Ayah anchors: `ن و ر` at 85:5; `غ ف ر` at 85:14; `ل و ح` at 85:22; `ح و ط` at 85:20.
- Synthesis: Removal, coating, puncture, pigment, and ornament are distinct operations within one grooming and body-marking scene.

### 14. Inner Stability, Attention, and Affect
- Semantic invariant: The inner person moves among security, derangement, desire, admiration, aversion, agitation, and exhaustion.
- Surface relation: indirect; belief at 85:7-11, censure at 85:8, trial at 85:10, severity at 85:12, love at 85:14, and will at 85:16 supply the surface anchors.
- Surprising reach: The channel extends from trust to hidden thought, madness attributed to spirits or passion, attentive listening, aesthetic delight, chastity as flight, social turmoil as chest agitation, and dullness of tongue and perception.

#### 14A. Security, Reliability, and Inner Calm
- Reading type: mixed
- Scene or process: Fear subsides when the heart trusts a stable support and remains watchful enough to preserve that security.
- Active motifs: calm trust and reliability `ء م ن:B001/m01`; hidden heart or inner thought `ج ن ن:B010/m01`; vigilance `ح ف ظ:B004/m01`; firmness under strain `ش د د:B002/m02`; mainstay of an affair `م ل ك:B005/m01`.
- Ayah anchors: `ء م ن` at 85:7, 85:8, 85:10, 85:11; `ج ن ن` at 85:11; `ح ف ظ` at 85:22; `ش د د` at 85:12; `م ل ك` at 85:9.
- Synthesis: Trust settles the inner heart, a reliable mainstay grounds it, and vigilance keeps calm from becoming careless exposure.

#### 14B. Madness and Derangement
- Reading type: latent/lexical
- Scene or process: Reason, property, or self-command is covered or carried away by affliction, passion, or imagined spirit possession.
- Active motifs: loss of reason `ج ن ن:B006/m01`; derangement or loss `ف ت ن:B007/m01`; passion or spirit overpowering the person `ق ت ل:B006/m01`; involuntary bodily disturbance `ء ر ض:B012/m01`; hidden spirits `ج ن ن:B005/m01`.
- Ayah anchors: `ج ن ن` at 85:11; `ف ت ن` at 85:10; `ق ت ل` at 85:4; `ء ر ض` at 85:9.
- Synthesis: The scene treats derangement as dispossession: an external or internal force covers reason, disturbs the body, and removes ordinary control.

#### 14C. Will, Desire, and Attentive Listening
- Reading type: mixed
- Scene or process: A desired object draws the mind, becomes a purpose, and receives focused listening or pursuit.
- Active motifs: will and intended purpose `ر و د:B001/m01`; volition `ش ي ء:B001/m01`; wished-for attainment `و د د:B002/m01`; attentive listening `ش ي ء:B005/m01`; approved or satisfying object `ح م د:B002/m01`.
- Ayah anchors: `ر و د` and `ف ع ل` at 85:16; `ش ي ء` at 85:9; `و د د` at 85:14; `ح م د` at 85:8.
- Synthesis: Desire identifies the object, will commits to it, attention keeps it present, and approval registers the object as worth attaining.

#### 14D. Admiration, Pleasure, and Approval
- Reading type: latent/lexical
- Scene or process: A visible or experienced object produces delight, attachment, and an enlarged estimation of its worth.
- Active motifs: admiration and pleasure `ش ي ء:B004/m01`; affective attachment `ب ل ل:B004/m02`; tested satisfaction `ح م د:B002/m01`; magnification in the heart `ك ب ر:B003/m01`; visible beauty `ب ر ج:B010/m01`.
- Ayah anchors: `ش ي ء` at 85:9; the `بَلْ` tokens at 85:19, 85:21; `ح م د` at 85:8; `ك ب ر` at 85:11; `ب ر ج` at 85:1.
- Synthesis: Perception becomes affect when beauty enlarges the object in the observer’s estimation, producing delight and a desire to remain attached.

#### 14E. Chastity, Shyness, and Aversion
- Reading type: latent/lexical
- Scene or process: A person preserves integrity by recoiling from what is indecent or threatening and guarding intimate boundaries.
- Active motifs: chaste flight from impropriety `ن و ر:B006/m01`; guarding chastity and private honor `ح ف ظ:B006/m01`; restraint from action `ع ذ ب:B003/m01`; watchful self-protection `ح ف ظ:B004/m01`; withdrawal from marriage `ق ع د:B003/m02`.
- Ayah anchors: `ن و ر` at 85:5; `ح ف ظ` at 85:22; `ع ذ ب` at 85:10; `ق ع د` at 85:6.
- Synthesis: Aversion is protective rather than passive: recoil creates distance, restraint prevents approach, and guarded boundaries preserve personal integrity.

#### 14F. Agitation, Confusion, and Restlessness
- Reading type: latent/lexical
- Scene or process: Conflicting impulses disturb the chest, language, and group, producing circular movement and inability to settle.
- Active motifs: inner and social confusion `ب ل ل:B009/m01`; interpersonal enmity `ن و ر:B007/m01`; warlike disturbance `ف ت ن:B006/m01`; tremor `ء ر ض:B008/m01`; restless back-and-forth motion `ر و د:B004/m01`.
- Ayah anchors: the `بَلْ` tokens at 85:19, 85:21; `ن و ر` at 85:5; `ف ت ن` at 85:10; `ء ر ض` at 85:9; `ر و د` at 85:16.
- Synthesis: Agitation is represented across scales, from bodily tremor and unsettled thought to clamorous speech and factional disturbance.

#### 14G. Fatigue, Bluntness, and Diminished Capacity
- Reading type: latent/lexical
- Scene or process: Repeated use or strain dulls a blade, tongue, sense, animal, or person until performance weakens.
- Active motifs: fatigue and loss of sharpness `ك ل ل:B001/m01`; moisture and residual softness `ب ل ل:B001/m02`; blunt tongue or expression `ش ه د:B005/m02`; polishing that restores clarity `ح د ث:B007/m01`; inability to rise `ق ع د:B009/m01`.
- Ayah anchors: `ك ل ل` at 85:9; the `بَلْ` tokens at 85:19, 85:21; `ش ه د` at 85:3, 85:7, 85:9; `ح د ث` at 85:17; `ق ع د` at 85:6.
- Synthesis: Dullness unifies physical and cognitive fatigue, while polishing and rest imply the possibility of recovering edge, clarity, or mobility.

### 15. Origination, Recurrence, and Temporal Transition
- Semantic invariant: Events and lives are structured by beginning, manifestation, return, novelty, habit, and restoration.
- Surface relation: direct; beginning and return at 85:13, purposeful action at 85:16, and the arrival of a report at 85:17.
- Surprising reach: The temporal frame reaches creation, revelation as showing, homecoming, recurrent illness and festival, youthful freshness, habitual practice, and routes understood as repeated patterns.

#### 15A. Beginning, Creation, and Showing
- Reading type: surface-primary
- Scene or process: An agent initiates what did not exist and brings the new event into visibility.
- Active motifs: beginning and origination `ب د ء:B001/m01`; coming into being `ح د ث:B001/m01`; disclosure and showing `ح د ث:B006/m01`; effect-producing action `ف ع ل:B001/m01`; arrival or manifestation `ء ت ي:B001/m01`.
- Ayah anchors: `ب د ء` at 85:13; `ح د ث` and `ء ت ي` at 85:17; `ف ع ل` at 85:7, 85:16.
- Synthesis: Origination is both ontological and perceptual: action causes a new event, and showing completes the process by making the new state available to observers.

#### 15B. Return, Restoration, and Homecoming
- Reading type: mixed
- Scene or process: What departed or ceased comes back to its earlier state, destination, relationship, or cycle.
- Active motifs: return after departure `ع و د:B001/m01`; destination or place of return `ع و د:B002/m01`; beginning paired with restoration `ب د ء:B001/m01`; appointed return `و ع د:B003/m01`; homecoming presence `ش ه د:B001/m01`; recurring beneficial return `ع و د:B006/m01`.
- Ayah anchors: `ع و د` and `ب د ء` at 85:13; `و ع د` at 85:2; `ش ه د` at 85:3, 85:7, 85:9.
- Synthesis: Return reverses departure but does more than repeat it: destination, appointment, and renewed benefit give recurrence a directed and restorative shape.

#### 15C. Novelty, Freshness, and Early Stage
- Reading type: latent/lexical
- Scene or process: A thing is perceived at the first, fresh phase of its existence before maturity or habituation.
- Active motifs: marvelous novelty `ب د ء:B002/m01`; beginning of youth or era `ج ن ن:B014/m01`; youthful freshness `ح د ث:B002/m01`; recent birth or fresh state `ر ب ب:B009/m01`; new yield or emergence `ء ت ي:B007/m01`.
- Ayah anchors: `ب د ء` at 85:13; `ج ن ن` at 85:11; `ح د ث` at 85:17; `ر ب ب` at 85:12; `ء ت ي` at 85:17.
- Synthesis: Novelty is a temporal texture shared by event, person, crop, and era: each is close enough to its beginning to retain freshness and surprise.

#### 15D. Habit, Practice, and Constancy
- Reading type: latent/lexical
- Scene or process: Repetition turns an action into a trained habit, stable method, or traceable way.
- Active motifs: habit and acquired practice `ع و د:B004/m01`; disciplined constancy `ح ف ظ:B003/m01`; customary way `ج ر ي:B002/m01`; method or model `ق ر ء:B011/m01`; gentle measured pacing `ر و د:B005/m01`.
- Ayah anchors: `ع و د` at 85:13; `ح ف ظ` at 85:22; `ج ر ي` at 85:11; `ق ر ء` at 85:21; `ر و د` at 85:16.
- Synthesis: Repetition stabilizes both behavior and route: practice becomes habit, habit becomes method, and method leaves a reliable trace that can be followed again.

## Standalone Subchannels

### S1. Proverbial Thief and Serpent
- Reading type: latent/lexical
- Scene or process: A proverbial danger scene pairs a named thief with a concealed serpent and the compact wisdom of a fire proverb.
- Active motifs: thief named in proverb `ب ر ج:B012/m01`; serpent or white snake `ج ن ن:B012/m01`; proverbial abundance of fire in suitable wood `م ج د:B005/m02`; hidden danger `ج ن ن:B001/m02`.
- Ayah anchors: `ب ر ج` at 85:1; `ج ن ن` at 85:11; `م ج د` at 85:15, 85:21.
- Synthesis: Theft, concealment, serpent danger, and proverbial fire form a compact cautionary image whose relation is figurative rather than part of the broader social or animal scenes.

### S2. Camp Pavilion and Portable Provision
- Reading type: latent/lexical
- Scene or process: A temporary camp combines a military pavilion, mounted litter, leather covering, and compact sweet provision.
- Active motifs: military pavilion `ف و ز:B004/m01`; woman’s mounted litter `ع ر ش:B005/m01`; leather saddle cover `ف ت ن:B008/m01`; honey retained in wax `ش ه د:B007/m01`; water securing the encampment `م ل ك:B007/m01`.
- Ayah anchors: `ف و ز` at 85:11; `ع ر ش` at 85:15; `ف ت ن` at 85:10; `ش ه د` at 85:3, 85:7, 85:9; `م ل ك` at 85:9.
- Synthesis: Shelter, conveyance, leather equipment, concentrated food, and water make a coherent portable camp scene that does not reduce to warfare, hospitality, or craft alone.


