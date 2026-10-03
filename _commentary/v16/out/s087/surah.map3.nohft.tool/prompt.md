Surah: 87. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S87 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/map3/surah_map.md (adapted) =====
Read the surah as one text and write its map of image chains: the lexical images that run through several of
its ayat and join them into one scene, process or movement. A later writer will read one ayah at a time, with
only that ayah's own dictionary. The map lets that writer hear what the ayah's words carry in the surah as a
whole, including senses whose evidence sits under the words of other ayat.

Your evidence is the surah text, the dictionary of every root in the surah (each branch with the classical
dictionaries' own phrases), an earlier reader's channel review (channels.md),
and your own knowledge of Arabic and the Quran. Where a member or passage comes from memory rather than from
the dictionary or the text, say so. Do not use tools, delegate, browse or inspect files.

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

===== _commentary/v16/work/s087/surah.r2/text.md =====
# Surah 87

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/s087/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ب ح (root_000666): 87:1 سَبِّحِ

- **B001** Tanrı'yı yücelterek anma ve kulluk — dua ve anma biçimindeki gönüllü kulluk · Tanrı'yı sözle, eylemle veya niyetle yüceltme ve anma
  السُّبحة وهي الصلاة (maqayis)؛ التسبيح يكون في معنى الصلاة (ayn)؛ سبح الرجل تسبيحا إذا عظم الله ومجده (jamhara)؛ السبحة التطوع من الذكر والصلاة (sihah)؛ السبحة من الصلاة التطوع (tahdhib)؛ التسبيح عاما في العبادات قولا كان أو فعلا أو نية (mufradat)
- **B002** Tanrı'yı her türlü eksiklikten uzak sayma — Tanrı her türlü kötülük ve eksiklikten uzaktır · Tanrı'yı her türlü kötülük ve eksiklikten uzak sayarak yüceltme · şaşma veya söz konusu kişiyi bir iddiadan uzak tutma sözü · her türlü kötülükten ve kendisine yakışmayan nitelikten uzak olan Tanrı
  التسبيح وهو تنزيه الله من كل سوء (maqayis)؛ سبحان الله تنزيه لله (ayn)؛ سبحان تنزيه وتبرئة (jamhara)؛ التسبيح التنزيه (sihah)؛ سبحان في اللغة تنزيه لله عز وجل عن السوء (tahdhib)؛ التسبيح تنزيه الله تعالى (mufradat)
- **B003** Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı — Tanrı'nın yüzünün görkemi, büyüklüğü ve ışığı · yere kapanma yerleri
  السبحات جلال الله وعظمته (maqayis)؛ سبحات وجه ربنا يعني جلاله وعظمته ونوره (ayn)؛ سبحات وجهه نور وجهه (jamhara)؛ سبحات وجه ربنا أي جلالته (sihah)؛ سبحات وجهه نور وجهه؛ السبحات مواضع السجود (tahdhib)
- **B004** yüzerek veya akıcı biçimde hızla ilerleme — yüzme ve su ya da havada hızla ilerleme · yıldızların yörüngede akıp ilerlemesi · ön ayaklarını ileri uzatarak koşan at · yörüngede ya da koşuda hızla akıp gidenler
  السَّبح والسباحة العوم في الماء (maqayis)؛ السبح مصدر كالسباحة سبح السابح في الماء (ayn)؛ سبح الرجل وغيره في الماء سبحا وسباحة (jamhara)؛ السباحة العوم (sihah)؛ النجوم تسبح في الفلك؛ السابح من الخيل يمد يديه في الجري (tahdhib)؛ السبح المر السريع في الماء وفي الهواء (mufradat)
- **B005** iş ve geçim için zaman ve hareket imkânı — serbest zaman, geçim için hareket ve gidip gelme imkânı · yeryüzünde uzaklara gitmek · sözü uzatıp çok konuşmak
  أصلان أحدهما جنس من العبادة والآخر جنس من السعي (maqayis)؛ سبحا طويلا أي فراغا للنوم (ayn)؛ السبح الفراغ والتصرف في المعاش والمنقلب والجيئة والذهاب (sihah)؛ فراغا وتصرفا؛ اضطرابا ومعاشا؛ منقلبا طويلا (tahdhib)؛ سرعة الذهاب في العمل (mufradat)
- **B006** anma sözlerini saymaya yarayan boncuk dizisi — Tanrı'yı anma sözlerini saymaya yarayan boncuk dizisi
  السبحة خرزات يسبح بعدها (ayn)؛ السبحة بالضم خرزات يسبح بها (sihah)؛ الخرزات التي يعد بها المسبح تسبيحه السبحة وهي كلمة مولدة (tahdhib)؛ الخرزات التي بها يسبح سبحة (mufradat)
- **B007** çocuk deri giysisi; güçlü ve sıkı örtü — çocuklar için deriden yapılmış gömlek veya giysi · güçlü, sağlam ve sıkı örtü
  السبحة قميص يعمل للصبيان من جلود وسلف رقيق والجمع سباح (jamhara)؛ السبحة بفتح السين وجمعها سباح ثياب من جلود؛ السباح قمص للصبيان من جلود؛ كساء مسبح أي قوي شديد (tahdhib)
- **B008** kutsal kent veya hac bölgesindeki bir vadinin adı — kutsal kent ya da hac sırasında durulan bölgedeki bir vadinin adı
  سَبّوحة البلد الحرام ويقال واد بعرفات (sihah)

## س م و (root_000745): 87:1 ٱسْمَ, 87:15 ٱسْمَ

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

## و س م (root_001650): documented alternative for 87:1 ٱسْمَ, 87:15 ٱسْمَ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı

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

## ر ب ب (root_000532): 87:1 رَبِّكَ, 87:15 رَبِّهِۦ

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

## ECHO ر ب و (root_000537): for 87:1 رَبِّكَ, 87:15 رَبِّهِۦ: withheld observed target; not identity

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

## ع ل و (root_001042): 87:1 ٱلْأَعْلَى

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

## خ ل ق (root_000434): 87:2 خَلَقَ

- **B001** ölçüp sınırlarını belirleme — ölçüp sınırlarını belirlemek · ölçüp biçme
  أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)
- **B002** var etme ve ortaya çıkarma — yaratmak, var etmek · yaratan, var eden · yaratan, var eden; özellikle Tanrı için kullanılan ad · yaratılanlar, insanlar · yaratılmış varlık ya da varlıklar topluluğu
  الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)
- **B003** tam ve dengeli dış biçim — dış görünüş ve beden yapısı · beden yapısı tam ve dengeli · yapısı tamamlanmış ve ölçülü · biçimi belirmiş ve oluşumu tamamlanmış
  رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)
- **B004** huy ve iç karakter — huy, iç karakter · doğal huy ve yaradılıştan eğilim · iyi huyluluk ve iyi geçim · insanlarla huyuna göre geçinmek · bir huyu edinmeye veya öyle görünmeye çalışmak
  الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)
- **B005** bir şeye yaraşır ve uygun olma — yaraşır, uygun · bunu yapması ne kadar beklenir · iyiliğe veya o işe çok uygun
  فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)
- **B006** iyilikten düşen pay — pay, özellikle iyilikten düşen pay · iyilikten veya öte dünyadaki karşılıktan payı yok
  الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)
- **B007** uydurup yalan üretme — söz uydurmak ve çarpıtmak · zihninde yalan kurup ortaya atmak · yanlış kişiye bağlanmış, uydurma · uydurma öyküler ve asılsız anlatılar
  الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)
- **B008** engebesiz ve düz olma — yüzeyini düzeltmek ve pürüzsüzleştirmek · engebesiz, düz ve yoğun · düz ve engebesiz kaya · alnın veya gözler arasının düz bölümü · yayılıp düzleşmek · düzeltilmiş ve yüzeyi engebesiz
  الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)
- **B009** kullanımdan yıpranıp eskime — kullanımdan yıpranıp tüyünü yitirmek · eski ve yıpranmış giysi · her yanı yıpranmış veya parçalanmış giysi · birine eski ve yıpranmış bir giysi vermek · istemekten yüzünü eskitmek
  أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)
- **B010** sürülen hoş koku karışımı — sürülen hoş koku karışımı · hoş koku karışımı sürmek veya sürünmek
  الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)
- **B011** su tutan kaya oyuğu veya yeni kuyu — su tutan kaya oyuğu veya yeni kuyu · yeni kazılmış kuyular
  الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)
- **B012** kapalı üreme yolu — üreme yolu kapalı kadın
  امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)

## س و ي (root_000766): 87:2 فَسَوَّىٰ

- **B001** iki şeyi birbirine denk kılma veya denk sayma — bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek · iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme · bir işte aynı düzeyde ve eşit durumda · eş, benzer · ikisi de bir, ikisi eşit · özellikle, hele
  أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)
- **B002** kendi içinde düzgün ve tam duruma gelme — bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek · eğrilikten kurtulup doğrulmak · yapısı düzgün, eksiksiz ve sağlıklı · çocuklarımız ve hayvanlarımız iyi durumda · düz arazi
  سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)
- **B003** üzerine çıkıp yerleşmek veya egemen olmak [kalıp] — bineğinin sırtına çıkıp yerleşmek · üzerine çıkmak ya da egemen olmak
  استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)
- **B004** bir hedefe yönelip onu amaç edinmek [kalıp] — göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek
  استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)
- **B005** gençlik olgunluğuna erişmek — gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak
  استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)
- **B006** iki yanın ortasında ve ikisine karşı yansız olma — orta; iki yana eşit ve yansız durum · iki yana eşit, ortada ve herkesçe bilinen yer · iki tarafın da hakkını gözeten ortak söz
  السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)
- **B007** başka ve ayrı olan — başka, öteki
  سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)
- **B008** birinin yöneldiği hedefe yönelmek [kalıp] — birinin tuttuğu yöne ya da hedefe yönelmek
  يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)
- **B009** geniş ve açık arazi — geniş, açık ya da pürüzsüz arazi
  السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)
- **B010** devenin sırtına konan dolgulu binme örtüsü — devenin sırtına ya da hörgücü çevresine konan binme örtüsü
  السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)
- **B011** atlayıp dışarıda bırakmak — atlamak, dışarıda bırakmak ve göz ardı etmek
  أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)
- **B012** ayın on üçüncü gecesi — ayın dengeli göründüğü on üçüncü gece
  ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)
- **B013** başına denk mal ve bolluk [kalıp] — başına denk sayılan mal miktarı ya da bolluk
  جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)

## ق د ر (root_001205): 87:3 قَدَّرَ

- **B001** bir şeyin ölçüsü ve eriştiği sınır — bir şeyin ölçüsü, niceliği ve sınırı · belirlenmiş ölçü, sınır veya süre
  مبلغ الشيء وكنهه ونهايته (maqayis)؛ القدر مبلغ الشيء؛ لكل شيء مقدار وأجل (ayn)؛ قدر الشيء مبلغه (sihah)؛ المقدار هو الهنداز؛ ينزل المطر بمقدار (tahdhib)؛ القدر والتقدير تبيين كمية الشيء (mufradat)
- **B002** Tanrı'nın varlıkları ölçülü biçimde hükme bağlaması — Tanrı'nın varlıklar için belirlediği ölçülü hüküm · Tanrısal belirlemeyi reddetmekle anılan topluluk · belirli işlere ayrılmış özel gece
  قضاء الله تعالى الأشياء على مبالغها ونهاياتها (maqayis)؛ القدر القضاء الموفق؛ قدره الله تقديرا (ayn;tahdhib)؛ ما يقدره الله عزوجل من القضاء (sihah)؛ يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة (mufradat)
- **B003** bir şeyi yapmaya veya ona egemen olmaya elveren güç — bir işi yapmaya elveren güç ve yetkinlik · gücü yeten ve yapabilen · dilediğini gerçekleştirecek ölçüde güçlü · gücü olan veya güç edinmiş · varlıklı ve geniş olanaklı
  قدرة الله تعالى على خليقته؛ رجل ذو قدرة وذو مقدرة أي يسار (maqayis)؛ قدر على الشيء قدرة أي ملك فهو قادر (ayn;tahdhib)؛ الاقتدار على الشيء القدرة عليه؛ رجل ذو قدرة أي ذو يسار (sihah)؛ القدرة إذا وصف بها الإنسان فاسم لهيئة له بها يتمكن (mufradat)
- **B004** birinin geçim payını kısmak [kalıp] — onun geçim payını kıstı · onu darlığa sokarız
  من قدر عليه رزقه فمعناه قتر (maqayis)؛ قدر على عياله مثل قتر؛ قدر على الإنسان رزقه مثل قتر (sihah)؛ نضيق عليه؛ ضيق عليه (tahdhib)؛ قدرت عليه الشيء ضيقته؛ ومن قدر عليه رزقه أي ضيق عليه (mufradat)
- **B005** ölçüp biçerek tasarlamak ve hazırlamak — ölçüsünü belirleyip hazırladı · ayın gün sayısını hesaplayıp otuza tamamlayın · örgülü işi düzgün ve sağlam kurdu · o şey onun için hazır duruma geldi
  اقتدرت الشيء جعلته قدرا؛ قدرت الشيء أي هيأته (ayn)؛ فاقدروا له أي أتموا ثلاثين؛ تقدر له الشيء أي تهيأ (sihah)؛ التروية والتفكير في تسوية أمر وتهيئته؛ نظرت فيه ودبرته وقايسته؛ قدر في السرد أي أحكمه (tahdhib)؛ التقدير من الإنسان التفكر في الأمر؛ فكر وقدر؛ قدر في السرد أي أحكمه (mufradat)
- **B006** söz öbeğine göre ölçüye uygun, orta veya yapıca ölçülü olma [kalıp] — ölçüsüne uydu ve tam denk geldi · orta büyüklükte eyer · orta boylu adam · kısa boyunlu veya kısa adam · arka ayaklarını ön ayak izlerine basan at · yol alması kolay gece
  جاء على قدره؛ المقتدر الوسط؛ سرج قدر أي وسط (ayn)؛ بين أرضك وأرض فلان ليلة قادرة؛ الأقدر القصير؛ الأقدار من الخيل (sihah)؛ كل شيء مقتدر فهو الوسط؛ القدر من الرحال والسروج الوسط؛ الأقدر من الرجال القصير العنق؛ الأقدر من الخيل (maqayis;tahdhib)؛ الأقدر القصير العنق؛ فرس أقدر (mufradat)
- **B007** pişirme kabı ve ona bağlı yemek, pişirme işi ve görevli sözleri — et veya yemek pişirme tenceresi · tencerede pişmiş et veya yemek · pişmiş çorba suyu · topluluk tencerede yemek pişirdi · hayvanı kesip etini pişiren kasap veya aşçı
  القدر وهي معروفة؛ القدير اللحم يطبخ في القدر؛ القدار الجزار ويقال الطباخ (maqayis)؛ القدير ما طبخ من اللحم؛ مرق مقدور؛ القدار الطباخ (ayn)؛ القدير المطبوخ في القدر؛ القدار الجزار ويقال الطباخ (sihah)؛ القدر مؤنثة؛ قدرت القدر إذا طبخت قدرا؛ القدار الجزار (tahdhib)؛ القدر اسم لما يطبخ فيه اللحم؛ قدرت اللحم طبخته؛ القدار الذي ينحر ويقدر (mufradat)

## ه د ي (root_001583): 87:3 فَهَدَىٰ

- **B001** doğru yolu gösterme ve doğruya yönelme — doğru yol, doğruyu gösterme ve açıklama · ona yolu gösterip tanıttım · doğru yolu kabul edip buldu · yol gösteren, doğruya çağıran kimse
  الهدى نقيض الضلالة؛ هدي فاهتدى (ayn;tahdhib)؛ الهدى الرشاد والدلالة؛ هداه الله للدين هدى؛ أولم يبين لهم؛ هديته الطريق والبيت هداية أي عرفته (sihah)؛ الهدى البيان وإخراج شيء إلى شيء والطاعة والورع؛ دله على الطريق (tahdhib)؛ الهداية دلالة بلطف؛ تعريف الطرق؛ التوفيق (mufradat)؛ التقدم للإرشاد؛ هديته الطريق هداية؛ الهدى خلاف الضلالة (maqayis)
- **B002** yön, izlenen yol ve tutum — işin yönü, doğrultusu ve amacı · bir kimsenin gidişi, tutumu ve yöntemi · onun benzeri veya onu yeniden yapma
  خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه؛ هدية أمره وسيرته؛ هدى هدي فلان أي سار سيرته (sihah)؛ هدية أمره أي جهة أمره؛ هديت به أي قصدت به؛ هديه أي سمته؛ ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة؛ هدياها أي مثلها أو أعاودك (tahdhib)؛ هدية فلان وهديه أي طريقته (mufradat)؛ نظر فلان هدي أمره أي جهته؛ ما أحسن هديته أي هديه؛ رميت بآخر هدياه أي قصده (maqayis)
- **B003** bir şeyin ilk veya öndeki bölümü — bir şeyin ilki veya öndeki bölümü · atların boyunları ya da ilk sırası; yaban hayvanlarının öncüleri · okun ucu ve koyunun boynu
  الهادي من كل شيء أوله؛ هوادي الخيل أعناقها أو أول رعيل؛ العصا هاديا لأنها تتقدمه؛ الدليل يسمى هاديا لتقدمه (ayn)؛ هادي السهم نصله؛ الهادي العنق؛ هوادي الخيل أعناقها أو أول رعيل؛ الهاديات أوائل الوحش (sihah)؛ الهادية من كل شيء أوله وما تقدم منه؛ هادية الشاة الرقبة؛ هوادي الخيل أعناقها أو أول رعيل؛ هاديات الوحش أوائلها (tahdhib)؛ هوادي الوحش متقدماتها الهادية لغيرها (mufradat)؛ كل متقدم لذلك هاد؛ هوادي الخيل أعناقها؛ هاديها أول رعيل؛ الهادية العصا لأنها تتقدم ممسكها (maqayis)
- **B004** incelik göstergesi armağan verme — yakınlık ve incelik göstergesi armağan · armağan gönderdi veya verdi · karşılıklı armağanlaşma · armağanın sunulduğu tabak · sık sık armağan veren kimse
  الهدية ما أهديت إلى ذي مودة من بر (ayn)؛ الهدية واحدة الهدايا؛ أهديت له وإليه؛ المهدى ما يهدى فيه؛ التهادي أن يهدي بعضهم إلى بعض؛ المهداء الذي من عادته أن يهدي (sihah)؛ أهديت الهدية إهداء؛ امرأة مهداء؛ المهدى الطبق الذي يهدى عليه (tahdhib)؛ الهدية مختصة باللطف؛ المهدى الطبق؛ المهداء من يكثر إهداء الهدية (mufradat)؛ الهدية ما أهديت من لطف إلى ذي مودة؛ المهدي الطبق تهدى عليه (maqayis)
- **B005** kutsal yere adanan hayvan, mal veya eşya — kutsal bölgeye adanan hayvan, mal veya eşya · adanmış sunu adından genişleyen deve adı
  الهدي والهدي ما أهديت إلى مكة؛ كل شيء تهديه من مال أو متاع فهو هدي (ayn)؛ الهدي ما يهدى إلى الحرم من النعم؛ مالى هدي؛ حتى يبلغ الهدى محله (sihah)؛ أهديت الهدي إلى بيت الله؛ الهدي خفيف وعليه هدية أي بدنة؛ ما يهدى إلى مكة من النعم وغيره من مال أو متاع؛ العرب تسمي الإبل هديا (tahdhib)؛ الهدي مختص بما يهدى إلى البيت؛ فما استيسر من الهدي؛ هديا بالغ الكعبة (mufradat)؛ الهدي والهدي ما أهدي من النعم إلى الحرم قربة إلى الله تعالى (maqayis)
- **B006** gelini eşinin yanına götürme — gelini eşinin yanına götürdü · gelinin eşinin yanına götürülmesi · eşine götürülen gelin
  الهداء مصدر قولك هديت المرأة إلى زوجها؛ وهي مهدية وهدي (sihah)؛ هديت العروس فأنا أهديها هداء؛ أهدى الرجل امرأته جمعها إليه وضمها؛ المرأة سميت هديا لأنها كالأسيرة عند زوجها أو لأنها تهدى إلى زوجها (tahdhib)؛ الهدي يقال في العروس؛ هديت العروس إلى زوجها (mufradat)؛ الهدى العروس وقد هديت إلى بعلها هداء (maqayis)
- **B007** dokunulmaz sığınmacı; kimi açıklamalarda tutsak — dokunulmaz sığınmacı; kimi açıklamalarda tutsak
  الرجل الذي له حرمة كحرمة هدي البيت؛ يقال للأسير أيضا هدي (sihah)؛ الهدي الرجل ذو الحرمة وهو أن يأتي القوم يستجيرهم أو يأخذ منهم عهدا؛ يقال للأسير أيضا الهدي (tahdhib)؛ وقيل الهدي الأسير (maqayis)
- **B008** sallanarak, gerektiğinde başkalarına dayanarak yürüme — güçsüzlükten iki kişiye dayanarak yürümek · yürürken sağa sola sallandı
  التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)؛ يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله؛ المرأة إذا تمايلت في مشيتها قيل تهادى (sihah)؛ يهادى بين اثنين معناه يعتمد عليهما من ضعفه وتمايله؛ هي تهادى إذا تمايلت في مشيها (tahdhib)؛ يهادي بين اثنين إذا مشى بينهما معتمدا عليهما؛ تهادت المرأة إذا مشت مشي الهدي (mufradat)؛ جاء فلان يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما (maqayis)
- **B009** bön, güçsüz ve ağır kimse — bön, güçsüz, ağır ve uyuşuk adam
  الهداء الرجل البليد الضعيف (ayn)؛ رجل هداء وهدان للثقيل الوخم (tahdhib)
- **B010** sakin, ölçülü ve düzgün ilerleyiş — sakinlik ve güzel, telaşsız tutum
  الهدي السكون؛ ما هدى هدي مهزوم؛ لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن (ayn)؛ الهدي السكون؛ لم يسرع إسراع المنهزم ولكن على سكون وحسن هدي (tahdhib)
- **B011** övgü veya yergi şiiri sunma ve şiirle yergileşme — birine övgü veya yergi şiiri sunma · şiirle karşılıklı yergileşme
  الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)؛ هاداني فلان الشعر وهاديته أي هاجاني وهاجيته (tahdhib)

## ECHO ه د د (root_001580): for 87:3 فَهَدَىٰ: withheld observed target; not identity

- **B001** agir kirip yikma — kirip yikmak, sarsip bozmak · agir yikim ve kirilma · kirilip yikilmak · bir felaketin kisiyi sarsip gucunu kirmasi · yer cokmesi ya da yikima benzer agir olay
  أصل صحيح يدل على كسر وهضم وهدم (maqayis)؛ الهد الهدم الشديد (ayn;tahdhib)؛ هددت الحائط إذا هدمته (jamhara)؛ هد البناء يهده هدا كسره وضعضعه (sihah;tahdhib)؛ انهد الجبل أي انكسر (sihah)؛ الهدة الخسوف والهد الهدم (tahdhib)؛ هد ركني إذا بلغ منه وكسره (tahdhib)
- **B002** zayif ve korkak kisi — zayif veya korkak adam · korkak veya zayif adam · korkak adam · korkak topluluk · birini zayif saymak · zayif olmayan
  الهد من الرجال الضعيف كأنه هد (maqayis)؛ رجل هد جبان (jamhara)؛ رجل هد وأهد بمعنى الجبن والضعف (jamhara)؛ الهد الرجل الضعيف (sihah;tahdhib)؛ الهد بالكسر الجبان الضعيف (sihah;tahdhib)؛ استهددت فلانا أي استضعفته (tahdhib)
- **B003** cömert ve guclu kisi — cömert, degerli veya guclu adam · adam gucu ve dayanikliligiyla ovulmek · adami dayanikli diye ovmek
  الهد من الرجال الجواد الكريم (maqayis;tahdhib)؛ الهد الكريم الهاد لماله (maqayis)؛ فلان يهد إذا أثني عليه بالجلد والقوة (sihah)؛ لهد الرجل إذا أثني عليه بالجلد والشدة (tahdhib)؛ هد الرجل جلد الرجل (tahdhib)
- **B004** siddetli ugultu — duvar, kose veya dag dusmesinin siddetli sesi · deniz tarafindan duyulan siddetli ugultu · gok gurultusu · ses ve ugultu · kumru veya erkek devenin gurleyis ugultusu
  الهدة صوت وقع الحائط (maqayis;sihah)؛ الهدة صوت تسمعه من سقوط ركن أو ناحية جبل (ayn;tahdhib)؛ الهاد صوت شديد يسمعه أهل السواحل (ayn;sihah;tahdhib)؛ ما سمعنا العام هادة أي رعدا (jamhara)؛ هدهد الحمام صوت (maqayis)؛ الفحل يهدهد في هديره (ayn;sihah;tahdhib)؛ الهديد والغديد الصوت (tahdhib)
- **B005** ibibik kusu — ibibik kusu · ibibik veya guvercine benzetilen kus adlari
  الهدهد معروف (maqayis;tahdhib)؛ الهدهد طائر والهداهد مثله (sihah)؛ الهداهد طائر يشبه الحمام (tahdhib)؛ هداهد تصغير هدهد (tahdhib)
- **B006** uyutmak icin sallama [kalıp] — cocugu uyusun diye sallamak
  هدهدت المرأة ابنها حركته لينام (maqayis;sihah)؛ الهدهدة تحريك الأم ولدها لينام (tahdhib)؛ يهدهد الصبي (tahdhib)
- **B007** ovgu yeterlik kalibi — bir erkegi 'ona diyecek yok' anlaminda oven kalip
  مررت برجل هدك من رجل كقولهم حسبك من رجل (maqayis)؛ هدك فلان من رجل أي حسبك به (jamhara)؛ مررت برجل هدك من رجل معناه أثقلك وصف محاسنه (sihah)؛ مررت برجل هدك من رجل فهو بمعنى حسبك وهو مدح (tahdhib)
- **B008** agir basarak yurume [kalıp] — yururken yere cok sert basmak
  فلان يهد الأرض في مشيه إذا جاء يطأ وطأ شديدا (jamhara)
- **B009** sarp inisli gecit — sarp inisli tepe veya zorlu gecit
  أكمة هدود صعبة المنحدر وربما تردت الإبل منها (jamhara)؛ الهدود العقبة الشاقة (tahdhib)
- **B010** gozdagi vererek korkutma — gozdagi verme ve korkutma · korkutma ve gozdagi verme · gozdagi verme · uzaktan savrulan gozdagi
  التهديد التخويف وكذلك التهدد (sihah)؛ التهدد والتهديد والتهداد من الوعيد (tahdhib)؛ يقال للوعيد من وراء وراء الفديد والهديد (tahdhib)
- **B011** kesinlesmemis sani [kalıp] — kisinin icine kesinlesmemis bir sani gibi belirmek
  يقال يهدهد إلي كذا إذا شبه للإنسان في نفسه بالظن ما لم يثبته ولم يعقد عليه التشبيه (tahdhib)
- **B012** uzun boylu adam — uzun boylu adam
  الهديد الرجل الطويل (tahdhib)

## خ ر ج (root_000400): 87:4 أَخْرَجَ

- **B001** bir yerden ya da durumdan dışarı çıkma — dışarı çıktı; bir yerden veya durumdan ayrıldı · dışarı çıkma; bir durumdan ayrılma · dışarı çıkan veya ayrılan · çıkış yeri veya çıkış yönü
  النفاذ عن الشيء (maqayis)؛ الخروج نقيض الدخول (ayn;jamhara;tahdhib)؛ خرج خروجا برز من مقره أو حاله (mufradat)
- **B002** bir şeyi çıkarma, elde etme veya yetiştirme — dışarı çıkardı veya ortaya koydu · nesneleri dışarı çıkarma veya görünür kılma · çıkarıp elde etti · işleyip ortaya çıkarma veya çeşitlere ayırma · eğitim görüp yetişti · birinin elinde yetişmiş öğrenci
  اخترجت الرجل واستخرجته سواء (ayn)؛ الاستخراج كالاستنباط (sihah)؛ الإخراج أكثر ما يقال في الأعيان (mufradat)؛ خريج فلان كأنه أخرجه من حد الجهل (maqayis)
- **B003** düzenli mali yükümlülük, getiri veya gider — mali ödeme, vergi veya ürün getirisi · ürün getirisi, vergi veya zorunlu ödeme · hizmetindeki kişiyle aylık ödeme üzerinde anlaştı · efendisine düzenli ödeme yapmakla yükümlü köle · sorumluluk karşılığında elde edilen ürün getirisi
  الخراج والخرج الإتاوة لأنه مال يخرجه المعطي (maqayis)؛ الخرج والخراج ما يخرج من المال في السنة بقدر معلوم (ayn;tahdhib)؛ الخراج الغلة (tahdhib)؛ الخرج بإزاء الدخل (mufradat)
- **B004** bedende çıkan irinli şişlik veya yara — bedende çıkan şişlik, çıban veya irinli yara
  الخراج بالجسد (maqayis)؛ الخراج ورم وقرح يخرج من ذاته (ayn)؛ ما خرج على الجسد من دمل ونحوه (jamhara)؛ ما يخرج في البدن من القروح (sihah)؛ ورم وقرح يخرج بدابة أو غيرها من الحيوان (tahdhib)
- **B005** bulutun ilk kez oluşup belirmesi [kalıp] — bulut oluşmaya veya belirmeye başladı · gökyüzü bulutlandıktan sonra açıldı
  الخروج خروج السحابة (maqayis)؛ الخروج السحاب أول ما يبدأ (ayn)؛ السحاب أول ما ينشأ (sihah)؛ أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن (tahdhib)؛ الخرج أيضا من السحاب (mufradat)
- **B006** yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma — kendi değeriyle seçkinleşen kimse · soyu seçkin olmadığı halde üstün çıkan at · yöneticinin itaatinden ayrılan topluluk · birinin yeteneğinin ve iş bilirliğinin ortaya çıkması
  الخارجي الرجل المسود بنفسه من غير أن يكون له قديم (maqayis)؛ الخارجي الذي لم يكن له شرف في آبائه فيخرج ويشرف بنفسه (ayn)؛ فرس خارجي إذا خرج جوادا بين مقرفين (jamhara)؛ الخارجية من الخيل التي ليس لها عرق في الجودة فتخرج سوابق (tahdhib)؛ الخوارج خارجين عن طاعة الإمام (mufradat)
- **B007** iki renkli ya da yer yer kesintili görünüm — bir işi çeşitlendirme veya yer yer farklılaştırma · iki renkli veya kesintili görünüm · siyahı beyazından çok olan iki renkli · iki renkli dişi hayvan veya iki renkli yer · bitkisi yer yer çıkan arazi · otlağın bir bölümünü yiyip bir bölümünü bıraktı · yazı yüzeyinde bazı yerleri boş bıraktı · verimli ve verimsiz yerleri bir arada bulunan yıl
  الخرج لونان بين سواد وبياض (maqayis)؛ الأخرج لون سواده أكثر من بياضه (ayn;tahdhib)؛ أرض مخرجة نبتها في مكان دون مكان (ayn;sihah;tahdhib;mufradat)؛ خرج الغلام لوحه إذا ترك فيه مواضع لم يكتبها (tahdhib)
- **B008** erkek deve yapısında doğmuş dişi deve [kalıp] — erkek deve yapısında doğmuş dişi deve
  ناقة مخترجة إذا خرجت على خلقة الجمل (maqayis;ayn;sihah)؛ المخترجة أنها جبلت على خلقة الجمل (tahdhib)
- **B009** iki gözlü taşıma torbası — iki gözlü taşıma torbası · iki gözlü taşıma torbaları
  الخرج والخرجة جمعه جوالق ذو أونين (ayn)؛ الخرج من الأوعية معروف والجمع خرجة (sihah)؛ الخرج هذا الوعاء ثلاثة خرجة وهو جوالق ذو أونين (tahdhib)
- **B010** özel çağrılı geleneksel çocuk oyunu — erkek çocukların oynadığı geleneksel oyun · çocukların oynadığı geleneksel oyun · oyunda eldekini çıkarmayı isteyen çağrı
  الخريج لعبة لفتيان العرب يقال فيها خراج خراج (maqayis;sihah)؛ الخراج والخريج مخارجة لعبة لفتيان العرب (ayn)؛ الخراج لعبة يلعب بها الصبيان (jamhara)؛ خراج اسم لعبة لهم معروفة (tahdhib)
- **B011** uyakta bağlantı sesinden sonraki elif harfi — uyakta bağlantı sesinden sonra gelen elif harfi
  الخروج الألف التي بعد الصلة في القافية (ayn;tahdhib)
- **B012** ortak payları karşılıklı bölüşüp tasfiye etme — karşılıklı katkı ve bölüşme · ortakların veya mirasçıların paylarını tasfiye etmesi · iki ortağın mal ve alacak üzerinde karşılıklı hesaplaşması
  المخارجة المناهدة بالأصابع والتخارج التناهد (sihah)؛ يتخارج الشريكان وأهل الميراث (tahdhib)؛ لا بأس أن يتخارجا يعني العين والدين (tahdhib)
- **B013** uzun boyunlu at niteliği — uzun boynuyla dizginin erişimini aşan at
  الخروج من صفات الخيل وهو الذي يطول عنقه (tahdhib)

## ر ع ي (root_000574): 87:4 ٱلْمَرْعَىٰ

- **B001** otlama, ot ve otlak — ot, otlak ve otlama · hayvanın otlaması · hayvanlar için ot bitirmek · başka hayvanlarla birlikte otlamak
  الرَّعي الكلأ؛ المرعى الرعي والموضع والمصدر (sihah)؛ الرعي مصدر رعى يرعى رعيا الكلأ ونحوه (tahdhib)؛ الرعي ما يرعاه والمرعى موضع الرعي (mufradat)
- **B002** gözetip koruma ve yönetme — hayvanı gözetip korumak · çoban veya yönetici · yönetilen halk veya topluluk · yöneticinin halkını yönetip koruması · gözetme ve koruma; çobanlık veya yönetim · sürü veya mal yönetiminde becerikli kimse · bir şeyi birinin gözetimine vermek
  الراعي الوالي (maqayis)؛ الراعي جمعه رعاة والراعي الوالي والرعية العامة (sihah)؛ الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته (tahdhib)؛ جعل الرعي والرعاء للحفظ والسياسة (mufradat)
- **B003** dikkatle izleme ve gidişatı gözetme — dikkatle gözleyip izlemek · işin nereye varacağını izlemek · yıldızları gözlemek · kimsenin sözüne kulak asmamak
  رعيت الشيء رقبته ورعيته إذا لاحظته؛ راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها (maqayis)؛ راعيته لاحظته؛ رعيت النجوم رقبتها (sihah)؛ المراعاة المناظرة والمراقبة (tahdhib)؛ مراعاة الإنسان للأمر مراقبته إلى ماذا يصير (mufradat)
- **B004** kulak verip dinleme — ona kulak vermek; bana kulak ver · bizi dinle, sözümüze kulak ver
  أرعيته سمعي أصغيت إليه؛ أرعني سمعك (maqayis)؛ أرعيته سمعي أي أصغيت إليه؛ راعنا من المراعاة على معنى أرعنا سمعك (sihah)؛ راعنا سمعك أي اسمع منا؛ أرعنا سمعك وراعنا سمعك بمعنى واحد (tahdhib)؛ أرعيته سمعي؛ أرعني سمعك (mufradat)
- **B005** yanlıştan dönüp vazgeçme — çirkinlikten veya bilgisizlikten dönüp vazgeçmek · işlerden el çekmek · yanlışından güzelce dönme ve vazgeçme
  الأصل الآخر ارعوى عن القبيح إذا رجع (maqayis)؛ رعا يرعو أي كف عن الأمور؛ ارعوى عن القبيح (sihah)؛ ارعوى فلان عن الجهل وهو نزوعه وحسن رجوعه (tahdhib)
- **B006** esirgeyip koruma ve sözü gözetme — onu esirgemek veya ona acımak · esirgeme ve koruyup bırakma · esirgeme; verilen sözü gözetme · hakları ve verilen sözü gözetme · bana karşı daha gözetici ve koruyucu
  الإرعاء الإبقاء (maqayis)؛ أرعيت عليه إذا أبقيت عليه وترحمته (sihah)؛ الإرعاء الإبقاء على أخيك؛ الرعوى رعاية الحفاظ للعهد (tahdhib)؛ أرع على كذا أي أبق عليه (mufradat)
- **B007** iş develeri — işte kullanılan veya yerleşim çevresinde otlayan develer
  الرعاوى والرعاوى وهي الإبل التي يعتمل عليها (maqayis)؛ الرعاوى والرعاوى الإبل التي ترعى حوالي القوم وديارهم لأنها الإبل التي يعتمل عليها (sihah)؛ الرعاوى والرعاوى جميعا الإبل التي يعتمل عليها؛ لم أسمع الرعاوي بهذا المعنى إلا ها هنا (tahdhib)

## ج ع ل (root_000248): 87:5 فَجَعَلَهُۥ

- **B001** bir şeyi yapıp var etme — bir şeyi yapmak, yaratmak veya var etmek
  جعلت الشيء صنعته (maqayis)؛ جعل جعلا صنع صنعا (ayn)؛ جعل خلق؛ خلقنا (tahdhib)؛ يجري مجرى أوجد (mufradat)
- **B002** birini veya şeyi belirli bir duruma getirme — bir şeyi belirli bir duruma, niteliğe veya konuma getirmek · bir şeyi belirli bir duruma getirmek
  جعله الله نبيا أي صيره (sihah)؛ جعل صير؛ جعلته أحذق الناس؛ صيرهم؛ صيرته (tahdhib)
- **B003** öyle adlandırma ya da öyle olduğunu söyleme; başka yorumda öyle kılma — 
  جعلوا الملائكة إناثا أي سموهم (sihah)؛ جعل قال؛ أي قلناه؛ وقال غيره صيرناه (tahdhib)
- **B004** bir eylemi yapmaya başlama — bir şeyi yapmaya başlamak
  تقول جعل يقول ولا تقول صنع يقول (maqayis)؛ جعل يأكل وجعل يصنع كذا (ayn)؛ جعل فلان يصنع كذا كقولك طفق وعلق يفعل (tahdhib)؛ يجري مجرى صار وطفق فلا يتعدى نحو جعل زيد يقول (mufradat)
- **B005** iş karşılığı belirlenen ücret veya ortaklaşa kararlaştırılan ödeme — bir iş karşılığında belirlenen ücret, ödeme veya ödül · önemli bir iş için ortaklaşa kararlaştırılan ödemeler · ona bir ödeme veya armağan ayırmak
  الجعل والجعالة والجعلية ما يجعل للإنسان على الأمر يفعله (maqayis)؛ الجعل ما جعلت لإنسان أجرا له على عمل يعمله؛ الجعالات ما يتجاعل الناس بينهم (ayn)؛ الجعل ما جعل للانسان من شئ على الشئ يفعله؛ الجعالة؛ الجعيلة مثله (sihah)؛ الجعل في العطية؛ الجعالة بالفتح من الشيء تجعله للإنسان؛ ما جعلته للإنسان أجرا على عمله (tahdhib)
- **B006** kısa veya küçük hurma ağaçları — kısa veya küçük hurma ağaçları; tekili bu ağaçlardan biri
  الجعل النخل يفوت اليد والواحدة جعلة (maqayis)؛ الجعل واحدها جعلة وهي النخل الصغار (ayn)؛ الجعل النخل القصار الواحدة جعلة (sihah)؛ الجعل قصار النخل (tahdhib)
- **B007** sıcak tencereyi indirme bezi ve onunla indirme — sıcak tencereyi ateşten indirmeye yarayan koruyucu bez · tencereyi koruyucu bezle ateşten indirmek
  الجعال الخرقة التي تنزل بها القدر عن الأثافي (maqayis)؛ الجعال والجعالة خرقة تنزل بها القدر عن رأس النار يتقى بها من الحر (ayn)؛ الجعال الخرقة التي تنزل بها القدر عن النار؛ أجعلت القدر (sihah)؛ الجعال الخرقة التي تنزل بها القدور؛ أجعلت القدر إجعالا إذا أنزلتها بالجعال (tahdhib)
- **B008** kara küçük yer hayvanı ve bunlarla dolu su — kara renkli küçük bir yer hayvanı · bu hayvanların çokça bulunduğu su
  الجعل دابة من هوام الأرض (ayn)؛ الجعل دويبة؛ جعل الماء بالكسر أي كثر فيه الجعلان (sihah)؛ الجعل دابة سوداء من دواب الأرض تجمع جعلانا؛ ماء مجعل وجعل إذا تهافتت فيه الجعلان (tahdhib)
- **B009** dişinin çiftleşmek için erkeği istemesi — çiftleşmek isteyen dişi köpek · dişinin çiftleşmek için erkeği istemesi
  كلبة مجعل إذا أرادت السفاد (maqayis)؛ أجعلت الكبة واستجعلت فهي مجعل إذا أرادت السفاد وكذلك سائر السباع (sihah)؛ أجعلت الكلبة والسباع كلها إذا اشتهت الفحل؛ استجعلت أيضا بمعناه (tahdhib)
- **B010** deve kuşu yavrusu — deve kuşu yavrusu
  الجعول ولد النعام (maqayis)؛ الجعول الرأل ولد النعام (tahdhib)
- **B011** belirtilmemiş bir yer adı — kimliği belirtilmemiş bir yer adı
  الجَعْلة اسم مكان (maqayis)
- **B012** kısa, şişman ve inatçı olma — kısa, şişman ve inatçı kişi
  الجعل القصر مع السمن واللجاج (tahdhib)

## غ ث و (root_001073): 87:5 غُثَآءً

- **B001** akışla taşınan veya sıvı yüzeyine çıkan döküntü — selin taşıdığı ya da suyun ve tencerenin yüzüne çıkan kuru bitki, köpük ve döküntü · vadi yüzeyde toplanan değersiz döküntüler getirdi · yüzeyde toplanan döküntü getirdi veya bunlarla doldu · selin taşıdığı kumaş parçası ve benzeri yüzey döküntüsü · selin taşıdığı yüzey döküntüleri · suda hayvan pisliği, yaprak, kamış ve benzeri döküntüler çoğaldı
  الغثاء غثاء السيل (maqayis)؛ الغثاء ما جاء به السيل من نبات قد يبس (ayn)؛ ما يحمله السيل من القماش (sihah)؛ غثا الماء إذا كثر فيه البعر والورق والقصب (tahdhib)؛ الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر (mufradat)
- **B002** bitkiyi kuru ve ufalanmış hale getirmek — sel otlağı bir araya yığıp tadını giderdi · otlağı bir araya yığıp tadını giderdi · onu yeşillikten sonra kuru ve ufalanmış ota çevirdi
  غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته (sihah;tahdhib)؛ جففه حتى صيره هشيما جافا كالغثاء (tahdhib)؛ يابسا بعد خضرته (tahdhib)؛ ما يطفح ويتفرق من النبات اليابس (mufradat)
- **B003** iç bulanması — içi bulandı ve rahatsız edici bir şeyle kabardı · bulantı ve iç bulanması · içi bozulup bulandı · iç bulanması ve bulantı
  غثت نفسه تغثي كأنها جاشت بشيء مؤذ (maqayis)؛ الغثيان خبث النفس وغثيت نفسه تغثى (ayn)؛ الغثيان خبث النفس وقد غثت نفسه تغثي غثيا وغثيانا (sihah)؛ غثت نفسه تغثى غثيا وغثيانا (tahdhib)؛ غثت نفسه تغثي غثيانا خبثت (mufradat)
- **B004** değersiz görülüp önemsenmeyen kimse veya şey — toplumun aşağı ve değersiz görülen kesimi · değer verilmeyip boşa giden şey
  يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه (maqayis)؛ يضرب به المثل فيما يضيع ويذهب غير معتد به (mufradat)

## ح و ي (root_000374): 87:5 أَحْوَىٰ

- **B001** toplayıp güvenceye veya denetim altına alma — bir şeyi toplamak ve güvenceye almak · üzerinde denetim kurup kendi tasarrufuna almak · hak kazandıktan sonra sahip olan kimse
  حويت الشيء أحويه حيا إذا جمعته (maqayis)؛ حوى فلان مالا حيا وحواية أي جمعه وأحرزه واحتوى عليه (ayn;tahdhib)؛ احتوى فلان على كذا إذا استولى عليه (jamhara)؛ حواه يحويه حيا أي جمعه واحتواه مثله (sihah)؛ الحوي المالك بعد استحقاق (tahdhib)
- **B002** toplanıp dairesel biçimde kıvrılma — dairesel biçimde kıvrılma · toplanıp kıvrılarak halka olmak
  الحوي استدارة كل شيء كحوي الحية وكحوي بعض النجوم (ayn;tahdhib)؛ تحوى أي تجمع واستدار يقال تحوت الحية (sihah)
- **B003** bağırsaklar ve karındaki kıvrımlı bölümleri — bağırsak veya bağırsakların bir bölümü · bağırsağın kıvrımlı bir bölümü · bağırsakların tek bir kıvrımlı bölümü · bağırsaklar ve karındaki kıvrımlı iç bölümler
  الحوية والواحدة من الحوايا وهي الأمعاء (maqayis)؛ الحوية والحاوية والجميع الحوايا الأمعاء (ayn)؛ الحاوية والحاوياء الأمعاء التي تسمى بنات اللبن (jamhara)؛ حوية البطن وحاوية البطن وحاوياء البطن كله بمعنى وجمع الحوية حوايا وهي الأمعاء (sihah)؛ هي المباعر وبنات اللبن وهي الحواية والحاوية وهي الدوارة التي في بطن الشاة (tahdhib)
- **B004** kadın bineği veya hörgüç çevresine sarılan binme minderi — kadın bineği veya hörgüç çevresine sarılan binme minderi · üzerine binilen taşıma düzenekleri
  الحوية كساء يحوي حول سنام البعير ثم يركب (maqayis;tahdhib)؛ الحوية مركب يهيأ للمرأة (ayn;tahdhib)؛ الحوية مركب من مراكب النساء ليس بحدج ولا هودج (jamhara)؛ الحوية كساء محشو يدار حول سنام البعير (sihah)؛ الحوية شبيهة بالمحفة تركبها النساء (jamhara)
- **B005** tek barınak veya yakın barınaklardan oluşan yerleşim kümesi — tek çadır veya yakın çadırlardan oluşan konaklama kümesi · konaklama kümeleri · topluluğun evlerinin bir araya geldiği yer · toplu konaklama yeri · aynı konaklama kümesinde yaşayan topluluk
  الحي من أحياء العرب والحواء البيت الواحد (maqayis)؛ الحواء جماعة بيوت من الناس مجتمعة والجمع الأحوية وهي من الوبر (sihah)؛ الحواء أخبية تدانى بعضها من بعض وهم أهل حواء واحد وجمع الحواء أحوية (tahdhib)؛ لمجتمع بيوت الحي محوى وحواء ومحتوى والجميع أحوية ومحاء (tahdhib)
- **B006** siyah veya siyaha çalan koyu kızıl, esmer ya da yeşil renk — siyaha çalan koyu kızıl veya koyu esmer renk · siyah ya da siyah karışmış koyu yeşil renkli · siyah veya siyaha çalan koyu renkli dişi · atın siyah veya siyaha çalan koyu renge dönüşmesi
  الحوة شية من شيات الخيل وهي بين الدهمة والكمتة وكل أسود أحوى وامرأة حواء (jamhara)؛ الحوة لون يخالط الكمتة وحمرة تضرب إلى السواد والحوة سمرة الشفة وبعير أحوى إذا خالط خضرته سواد وصفرة (sihah)؛ الأحوى من الخيل هو الأحمر السراة والحوة في الشفاه شبيه باللمى والأحوى الأسود من الخضرة (tahdhib)
- **B007** ok uçlu yapraklı veya kurt renkli belirli bir ot — belirli bir ot veya otsu bitki · bu bitkinin tek bir örneği · aynı bitkinin sığırla ilişkilendirilen türü · tuzcul çalılar arasında yetişen kaba türü
  الحواء ضرب من البقل يشبه ورقه بنصال السهام (jamhara)؛ الحواء نبت يشبه لون الذئب الواحدة حواءة (sihah)؛ الحواء نبت معروف الواحدة حوءة وحواء الذعاليق وحواء البقر وحواء الكلاب (tahdhib)
- **B008** suyu tutan küçük yalak, kıvrımlı çukur veya çevrili yüzey — deve sulamak için yapılmış küçük yalak · sel suyunu tutan kıvrımlı çukurlar veya çevrili yüzeyler
  الحوي الحويض الصغير يسويه الرجل لبعيره يسقيه فيه (tahdhib)؛ الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل (tahdhib)؛ الحوايا المساطح وهو أن يعمدوا إلى الصفا فيحوون له ترابا وحجارة ليحبس عليهم الماء (tahdhib)
- **B009** hasta veya rahatsız kimse — hasta veya rahatsız kimse
  الحوي العليل والدوي الأحمق مشددات كلها (tahdhib)

## ق ر ء (root_001210): 87:6 سَنُقْرِئُكَ

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

## ق ر ء (root_001211): 87:6 سَنُقْرِئُكَ

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

## ن س ي (root_001501): 87:6 تَنسَىٰٓ

- **B001** hatırdan çıkma veya akılda tutmayı bırakma — önceden bilinen bir şeyi unutmak · unutma; hatırda tutmanın karşıtı · çok unutkan · çok unutkan adam · birine bir şeyi unutturmak · unutmuş gibi davranmak
  نسي فلان شيئا كان يذكره وإنه لنسي أي كثير النسيان (ayn;tahdhib)؛ النسيان خلاف الذكر والحفظ ورجل نسيان كثير النسيان (sihah)؛ ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد (mufradat)؛ نسيت الشيء إذا لم تذكره نسيانا (maqayis)
- **B002** bilerek bırakma ve yerine getirmeme — bir şeyi bırakmak veya savsaklamak · Tanrı'yı bıraktılar, O da karşılık olarak onları bıraktı
  النسيان الترك، نسوا الله فنسيهم (sihah)؛ النسيان على الترك نتركها فلا ننسخها، وبناسيها بتاركها (tahdhib)؛ إذا نسب ذلك إلى الله فهو تركه إياهم استهانة بهم ومجازاة لما تركوه (mufradat)؛ الثاني ترك شيء، فترك العهد (maqayis)
- **B003** unutulup atılmış değersiz şey — unutulmuş veya atılmış, önemsenmeyen şey · unutulup atılmış, yok sayılan şey · göç edenlerin geride bıraktığı değersiz ufak tefek eşya
  النسي الشيء المنسي الذي لا يذكر ويقال هو خرقة الحائض (ayn)؛ النسي والنسي ما تلقيه المرأة من خرق اعتلالها والنسي أيضا ما نسي وما سقط من رذال أمتعتهم (sihah)؛ الشيء المطروح لا يؤبه له، انظروا أنساءكم أي الشيء اليسير (tahdhib)؛ النسي ما يقل الاعتداد به وما من شأنه أن ينسى (mufradat)؛ النسي ما سقط من منازل المرتحلين من رذال أمتعتهم (maqayis)
- **B004** kalçadan bacağa uzanan damar — kalçadan veya uyluk ayrımından bacağa uzanan damar · bu damarın iki tanesi · bu damarın çoğulu · kalçadan bacağa uzanan damarı ağrımak · birinin bu damarına vurmak · bu damarı ağrıyan
  النسا عرق يأخذ من منشق ما بين الفخذين وهما نسيان وجمعه أنساء (ayn)؛ النسا عرق يخرج من الورك والجمع أنساء ويقال نسي الرجل إذا اشتكى نساه (sihah)؛ الذي يشتكي نساه نس ورجل أنسى وامرأة نسيا إذا اشتكيا عرق النسا (tahdhib)؛ النسا عرق وتثنيته نسيان وجمعه أنساء (mufradat)؛ ومما شذ عن الأصلين النسا عرق والجمع أنساء والاثنان نسيان (maqayis)
- **B005** sonraya bırakma ve süreyi uzatma — bir şeyi ertelemek veya uzak bir zamana bırakmak · kadının aybaşı gecikmek · ödemesi sonraya bırakılan satış · dokunulmaz ayın yerini sonraya kaydırma · develerin susuz kalacağı süreye bir iki gün eklemek · dökülmeden sonra geç çıkan deve tüyü
  معنى أنسيت أخرت (ayn)؛ ولا منسيها أي ولا مؤخرها من أنسأت الدين أي أخرته (tahdhib)؛ إذا همز تغير المعنى إلى تأخير الشيء، ونسئت المرأة تأخر حيضها، والنسيئة بيعك الشيء نساء، ونسأ الله في أجلك، والنسيء في كتاب الله التأخير، ونسأت الإبل في ظمئها، والنسء ما نبت من وبر الناقة بعد تساقط وبرها (maqayis)
- **B006** sopayla vurup itme veya sürme — bir şeyi itip uzaklaştırmaya yarayan sopa · deveyi itme sopasıyla vurup sürmek
  ونسأتها ضربتها بالمنسأة العصا لأن العصا كأنه يبعد بها الشيء ويدفع (maqayis)؛ المنساة العصا وأصله الهمز (sihah)
- **B007** üzerine su dökülmüş süt — üzerine su dökülmüş süt
  النسيء الحليب يصب عليه الماء وهو النسء أيضا (maqayis)؛ النسي بغير همز وهو كل ما نسى العقل وهو اللبن الحليب يصب عليه ماء (tahdhib)

## ش ي ء (root_000831): 87:7 شَآءَ

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

## ش ي ء (root_000832): 87:7 شَآءَ

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

## ء ل ه (root_000047): 87:7 ٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 87:7 ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ع ل م (root_001040): 87:7 يَعْلَمُ

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

## ج ه ر (root_000269): 87:7 ٱلْجَهْرَ

- **B001** açıkça duyurma ve yüksek sesle söyleme — açıkça duyurma ve açığa vurma · sözü yüksek sesle söylemek · okumayı yüksek sesle yapmak · işi açıkça yapmak ve saklamamak · yüksek ya da gür sesli · alışkanlıkla yüksek sesle konuşan
  جهرت بالكلام أعلنت به؛ رجل جهير الصوت أي عاليه (maqayis)؛ جهر بكلامه وصلاته وقراءته؛ كلام جهير وصوت جهير أي عال (ayn)؛ الجهر ضد السر؛ رجل جهير الصوت إذا كان غليظه (jamhara)؛ جهر بالقول رفع به صوته؛ إجهار الكلام إعلانه؛ المجاهرة بالعداوة المبادأة بها (sihah)؛ ظهور الشيء بإفراط حاسة السمع؛ ولا تجهر بصلاتك؛ كلام جوهري وجهير ورجل جهير يقال لرفيع الصوت (mufradat)
- **B002** gözle açıkça görme ve görünür olma — örtüsüz ve göz önünde · göze göründü ve belirdi · onu göz önünde açıkça görmek
  إعلان الشيء وكشفه (maqayis)؛ اجتهر القوم فلانا أي نظروا إليه عيانا جهارا؛ كل شيء بدا فقد جهر (ayn)؛ رأيته جهرة؛ عيانا يكشف ما بيننا وبينه (sihah)؛ ظهور الشيء بإفراط حاسة البصر؛ رأيته جهارا؛ نرى الله جهرة؛ أرنا الله جهرة (mufradat)
- **B003** göze büyük ve gösterişli görünme — görenin gözünde büyük görünmek · güzelliği ve görünüşüyle beni hayran bıraktı · gösterişli ve güzel görünüşlü · orduyu gözümde çok ve büyük gördüm
  جهرت الشيء إذا كان في عينك عظيما؛ وجهرت الرجل؛ رأيت جهر فلان أي هيئته؛ جهير بين الجهارة إذا كان ذا منظر (maqayis)؛ رجل جهير إذا كان في الجسم والمنظر مجتهرا (ayn)؛ جهرني الرجل إذا راعك جماله وهيئته؛ رجل جهير ذو رواء؛ أجهرت الجيش واجتهرته معناه كثروا في عيني (jamhara)؛ جهرت الرجل واجتهرته إذا رأيته عظيم المرآة؛ رجل جهير بين الجهارة أي ذو منظر؛ ما أحسن جهره أي ما يجتهر من هيئته وحسن منظره (sihah)؛ من رآه جهره معنى جهره عظم في عينيه؛ جهرت الجيش واجتهرتهم إذا كثروا في عينك (tahdhib)؛ رجل جهير يقال لمن يجهر لحسنه (mufradat)
- **B004** güneşte görememe; kimi kullanımda şaşılık — güneşte göremeyen; başka aktarımda şaşı · güneş gözünü kamaştırdı
  العين الجهراء التي لا تبصر في الشمس (maqayis)؛ جهرته الشمس إذا أسدرت بصره؛ كبش أجهر إذا سدر في الشمس (jamhara)؛ الأجهر الذي لا يبصر في الشمس؛ كبش أجهر بين الجهر ونعجة جهراء (sihah)؛ كبش أجهر ونعجة جهراء وهي التي لا تبصر في الشمس؛ الجهرة الحولة ورجل أجهر وامرأة جهراء في عيونهما حول (tahdhib)
- **B005** sabahleyin gafil avlayarak varma — onlara sabahleyin gafilken vardık · sabah vakti
  جهرنا بني فلان أي صبحناهم على غرة؛ أتيناهم صباحا والصباح جهر (maqayis)؛ جهرنا بني فلان أي صبحناهم على غرة (sihah)
- **B006** insan topluluğu — insan topluluğu
  يقال للجماعة الجهراء (maqayis)؛ كيف جهراؤكم أي عند جماعتكم (sihah)
- **B007** geniş ve yayvan tepe — geniş ve yayvan tepe
  يقال إن الجهراء الرابية العريضة (maqayis)
- **B008** kuyuyu boşaltıp temizleyerek suyunu açığa çıkarma [kalıp] — kuyuyu boşaltıp çamurunu temizleyerek suyunu açığa çıkarmak · kuyuyu temizleyip suyunu görünür hale getirmek · temizlenmiş ve suyu açığa çıkarılmış kuyu
  جهرت البئر إذا نزفت ماءها (jamhara)؛ جهرت البئر واجتهرتها أي نقيتها وأخرجت ما فيها من الحمأة؛ جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو (sihah)؛ جهرت البئر واجتهرتها إذا نزحتها؛ نزفوا مياه الآبار (tahdhib)؛ جهر البئر واجتهرها إذا أظهر ماءها (mufradat)
- **B009** bilinmeyen araziyi katetme [kalıp] — araziyi yolunu bilmeden geçtik
  جهرنا الأرض سلكناها من غير معرفة (sihah)
- **B010** tulumu çalkalama; süt için yağı alınmış ya da sulandırılmamış olma [kalıp] — süt tulumunu çalkalamak · yağı alınmış ya da su katılmamış süt
  جهرت السقاء مخضته؛ لبن جهير لم يمذق بماء (sihah)؛ جهرت السقاء إذا مخضته؛ الجهير اللبن الذي أخرج زبده (tahdhib)
- **B011** nefesi tutup ses akışıyla çıkarılan harf [kalıp] — nefesi tutup ses akışıyla çıkarılan harf
  الحروف المجهورة عند النحويين تسعة عشر؛ سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه حتى ينقضي الاعتماد بجرى الصوت (sihah)

## خ ف ي (root_000428): 87:7 يَخْفَىٰ

- **B001** gizli kalma ya da gizleme — şey gizli kaldı, görünmedi · şeyi ve onun haberini sakladı · şeyi gizledi ve sakladı · gizlilik ve saklılık hâli · gizlilik, görünmezlik · gizlenip gözden uzaklaştı · bir aktarıma göre gizlendi · gizlenen kişi · onunla gizlice buluştum
  خفي الشيء يخفى وأخفيته وهو في خفية وخفاء إذا سترته (maqayis); أخفيت الصوت إخفاء وفعله اللازم اختفى والخافية ضد العلانية ولقيته خفيا أي سرا (ayn); خفيت الشئ أخفيه كتمته وأخفيت الشئ سترته وكتمته واستخفيت منك أي تواريت (sihah); خفي الشيء خفية استتر وأخفيته أوليته خفاء وذلك إذا سترته ويقابل به الإبداء والإعلان (mufradat)
- **B002** örten ya da gizli kalan şey — gizli ya da örtülü şey · örtü veya örten giysi · kanadın iç tüyleri; hurma göbeğine yakın yapraklar · görünmeyen varlık · kanadın iç tüylerinden biri · bedende gizlendiğine inanılan görünmeyen varlık · kuyu, koruluk veya gizli yer · bu adla anılan iki aslan yatağı · su tulumunun üzerine atılan örtüler · kadının sesi ile yerdeki ayak izi
  الخوافي سعفات يلين قلب النخلة والخافي الجن (maqayis); الخفا مقصور الشيء الخافي والموضع الخافي والخفاء رداء تلبسه المرأة وكل شيء غطيت به شيئا فهو خفاء والخفية غيضة والخفية بئر والخوافي من الجناحين (ayn); الخافي الجن والخافية ما يخفى في البدن من الجن والخفية الركية والخوافى ما دون الريشات العشر والخوافي من السعف (sihah); الخفاء ما يستر به كالغطاء والخوافي جمع خافية وهي ما دون القوادم من الريش (mufradat)
- **B003** gizliliği giderip açığa çıkarma — gizli olan açığa çıktı, sır belli oldu · şeyi açığa çıkardı · şeyin gizliliğini giderip onu gösterdi · yağmur fareleri yuvalarından çıkardı · gizli şeyi çıkarıp ortaya koydu · kefenleri çıkardığı için mezar soyguncusu
  الأصل الآخر الإظهار وخفيت الشيء بغير ألف إذا أظهرته وخفا المطر الفأر من حجرتهن أخرجهن (maqayis); الخفا إخراجك الشيء الخفي وإظهاركه وخفيت الخرزة من تحت التراب أخفيها خفيا (ayn); وخفيته أيضا أظهرته وهو من الأضداد وخفى المطر الفأر إذا أخرجهن واستخفيت الشئ أي استخرجته وأخفيها أي أزيل عنها خفاءها (sihah); وخفيته أزلت خفاه وذلك إذا أظهرته (mufradat)
- **B004** belli belirsiz şimşek çakması — şimşek belli belirsiz ve zayıfça çaktı
  خفا البرق خفوا إذا لمع ويكون ذلك في أدنى ضعف (maqayis); وخفا البرق يخفو خفوا ويخفى خفيا أي ظهر من الغيم (ayn); خفا البرق يخفو خفوا وخفوا إذا لمع لمعانا خفيا (jamhara); وخفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم (sihah)

## ي س ر (root_001694): 87:8 وَنُيَسِّرُكَ, 87:8 لِلْيُسْرَىٰ

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

## ذ ك ر (root_000516): 87:9 فَذَكِّرْ, 87:9 ٱلذِّكْرَىٰ, 87:10 سَيَذَّكَّرُ, 87:15 وَذَكَرَ

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

## ن ف ع (root_001536): 87:9 نَّفَعَتِ

- **B001** zararın karşıtı olan ve iyiliğe ulaştıran yarar — zararın karşıtı olan, iyiliğe ulaşmaya yardım eden yarar · ona yarar sağladı · ondan yararlandı · yarar · yarar · yararlı · insanlara sürekli yarar sağlayan ve zarar vermeyen kişi
  النون والفاء والعين كلمة تدل على خلاف الضر (maqayis)؛ النفع ضد الضر (ayn;sihah;tahdhib)؛ نفعه نفعا وانتفعت بكذا (ayn)؛ نفعه ينفعه نفعا ومنفعة وانتفع بكذا (maqayis)؛ ما يستعان به في الوصول إلى الخيرات (mufradat)؛ ما عندهم نفيعة أي منفعة (tahdhib)؛ رجل نفاع إذا كان ينفع الناس ولا يضرهم (tahdhib)
- **B002** deri su kabının iki yanındaki yarılmış deri parçalardan biri — deri yarılarak su kabının iki yanına yerleştirilen parçalardan biri
  النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة (ayn)؛ النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة (tahdhib)
- **B003** değnek — değnek · değnek alıp satmak
  النَّفعة العصا وهي فعلة من النفع؛ أنفع الرجل إذا اتجر في النفعات وهي العصي

## خ ش ي (root_000413): 87:10 يَخْشَىٰ

- **B001** korku duyma — korku; özellikle saygı ve bilgiyle karışan korku · korkmak · korkan erkek · korkan kadın · ondan daha çok korku duydum · bu yer ötekinden daha çok korku verir · onu korkuttu
  الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذاك أي أفزعه (ayn)؛ خشي الرجل يخشى خشية أي خاف فهو خشيان والمرأة خشياء؛ كنت أشد خشية منه؛ هذا المكان أخشى أي أشد خوفا؛ خشاه تخشية أي خوفه (sihah)؛ الخشية الخوف والفعل خشي يخشى؛ هذا المكان أخشى من ذلك المكان؛ معناها من الآدميين الخوف (tahdhib)؛ الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم (mufradat)؛ يدل على خوف وذعر فالخشية الخوف ورجل خشيان؛ كنت أشد خشية منه؛ هذا المكان أخشى من ذلك أي أشد خوفا (maqayis)
- **B002** bilmek — bildim
  خشيت بأن من تبع الهدى معناه علمت (sihah)؛ فخشينا أي فعلمنا (tahdhib)؛ المجاز قولهم خشيت بمعنى علمت؛ أي علمت (maqayis)
- **B003** istememe ve hoşnutsuzluk [kalıp] — Tanrı'ya yüklenen kullanımda istememe ve hoşnutsuzluk
  فخشينا أن يرهقهما طغيانا وكفرا قال الأخفش معناه كرهنا (sihah)؛ فخشينا عن الله لأن الخشية من الله تعالى معناها الكراهة ومعناها من الآدميين الخوف (tahdhib)
- **B004** kuruyup sertleşmiş veya buruşup niteliğini yitirmiş olma — buruşmuş, düşük nitelikli hurma · hurma ağacı buruşmuş, düşük nitelikli meyve verdi · kuru et
  الخشي وهو اليابس؛ الخشو الحشف من التمر؛ خشت النخلة تخشو إذا أحشفت (sihah)؛ مما شذ عن الباب وقد يمكن الجمع بينهما على بعد الخشو التمر الحشف؛ خشت النخلة تخشو خشوا؛ الخشي من اللحم اليابس (maqayis)

## ج ن ب (root_000262): 87:11 وَيَتَجَنَّبُهَا

- **B001** bedenin veya şeyin yanı ve bitişik çevresi — insanın veya hayvanın böğrü · yan, taraf · evin önü veya topluluğun yerleşimine bitişik çevre · vadinin, ordunun veya ırmağın iki yanı · devenin böğür derisinden alınan parça · ordunun sağ ve sol kanadı
  أصل الجنب الجارحة وجمعه جنوب (mufradat)؛ الجنب للإنسان وغيره (maqayis)؛ الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء (ayn)؛ الجنب معروف والجانب الناحية (sihah)؛ جنبتا الوادي ناحيتاه وجناب القوم ما حولهم (tahdhib)؛ جنب الإنسان والدابة معروف وأعطني جنبة جلد جنب بعير (jamhara)
- **B002** yanında yakın bulunma ve eşlik etme — yaklaşması ve ilişki kurması kolay · yol arkadaşı veya yakın eşlikçi · Tanrı'ya yakınlıkta veya Tanrı'nın buyruğu ve yolu üzerinde · kardeşin hakkında, özellikle onu çekiştirme konusunda
  رجل لين الجانب والجنب أي سهل القرب (ayn;tahdhib)؛ الصاحب بالجنب صاحبك في السفر (sihah)؛ الجنب القرب وفي قرب الله وجواره (tahdhib)؛ في أمره وحده الذي حده لنا (mufradat)
- **B003** uzak durma veya uzaklaştırma — uzak durmak, sakınmak veya bırakmak · birini bir şeyden uzaklaştırmak veya kötülükten korumak · beni ve çocuklarımı putlara tapmaktan uzak tut · insanlardan ayrı bir yerde durma · akrabalıkta, soyda veya yerleşimde uzak olan yabancı · başka bir topluluktan gelip akrabalığı bulunmayan komşu · uzaktan ve yabancı olarak · birini iyilikten yoksun bırakmak
  الأصل الآخر البعد والجنابة (maqayis)؛ جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها (ayn)؛ الجناب مصدر جانبته مجانبة وهو من المباعدة (jamhara)؛ جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه (sihah)؛ أجنب تباعد والجنابة ضد القرابة (tahdhib)؛ جنبته عن كذا أي أبعدته واجتنبوا عبارة عن تركهم إياه (mufradat)
- **B004** cinsel ilişki sonrası arınma gerektiren dinsel durum — cinsel ilişkiden sonra arınana dek dinsel kısıt altında bulunan kişi · cinsel ilişki sonrası arınma gerektiren duruma girmek
  الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد (maqayis)؛ أجنب الرجل إذا أصابته الجنابة (ayn;jamhara;sihah;tahdhib)؛ رجل جنب وامرأة جنب وقوم جنب (jamhara;sihah;tahdhib)؛ سميت الجنابة بذلك لكونها سببا لتجنب الصلاة في حكم الشرع (mufradat)
- **B005** yanında yönlendirerek götürme — hayvanı veya atı yanında yürütmek · tutsağı yürütmek veya hayvanın yanına bağlamak · yanda çekilerek götürülen hayvan · yarış atının yanında yedek bir at koşturma yasağı
  جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير (maqayis;jamhara)؛ الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة (ayn)؛ جنبت الدابة إذا قدتها إلى جنبك ومنه خيل مجنبة (sihah)؛ جنبت الفرس أجنبه جنبا إذا قدته والجنيبة الدابة تقاد (tahdhib)؛ من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك (mufradat)
- **B006** güneyden esen yel — güney yeli · yelin güneyden esmesi veya topluluğun bu yele girip ona tutulması · güney yelinin sürüklediği bulut
  مما شذ عن الباب ريح الجنوب (maqayis)؛ الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح (ayn)؛ الجنوب ريح معروفة (jamhara)؛ الجنوب الريح التي تقابل الشمال (sihah)؛ الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور (tahdhib)؛ الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة (mufradat)
- **B007** böğür bölgesini tutan ağrı veya hastalık — böğrü ağrımak veya akciğer zarı hastalığına tutulmak · vurarak böğrünü incitmek veya kırmak · devenin aşırı susuzluktan akciğeri böğrüne yapışacak ölçüde hastalanması
  الجنب أن يشتد عطش البعير حتى تلتصق رئته بجنبه (maqayis)؛ أجنب فلان إذا أخذته ذات الجنب والجنيب الذي يشتكي جنبه (ayn)؛ جنب الرجل إذا اشتكى جنبه (jamhara)؛ المجنوب الذي به ذات الجنب وجنب البعير من شدة العطش (sihah)؛ ذات الجنب علة صعبة وجنب جنبا إذا اشتكى جنبه (tahdhib)؛ جنب شكا جنبه (mufradat)
- **B008** develerde sütün azalması veya tükenmesi — topluluğun develerinde sütün azalması veya tükenmesi · süt kıtlığı yaşanan yıl
  جنب القوم إذا قلت ألبانهم (maqayis;sihah)؛ جنب بنو فلان إذا لم يكن في إبلهم لبن (ayn;tahdhib)؛ جنب الرجل إذا قلت ألبان إبله (jamhara)؛ جنب بنو فلان إذا لم يكن في إبلهم اللبن (mufradat)
- **B009** çok miktarda iyilik veya kötülük [kalıp] — pek çok iyilik veya kötülük
  المجنب الخير الكثير كأنه إلى جنب الإنسان (maqayis)؛ شرا مجنبا وخيرا مجنبا أي كثيرا (ayn)؛ خيرا مجنبة ومجنبا وشرا مجنبا أي كثيرا (jamhara)؛ المجنب بالفتح الشيء الكثير وخيرا مجنبا وشرا مجنبا (sihah)؛ المجنب الخير الكثير والمجنب يقال في الشر إذا كثر (tahdhib)؛ جنب فلان خيرا وجنب شرا (mufradat)
- **B010** yazın kalan köklü küçük bitkiler — yazın kalan, köklü küçük bitki veya çalı
  الجنبة اسم يقع على عامة الشجر يترك في الصيف (ayn)؛ الجنبة ضرب من النبت (jamhara)؛ الجنبة اسم لكل نبت يتربل في الصيف (sihah)؛ الجنبة اسم واحد لنبوت كثيرة هي كلها عروة (tahdhib)
- **B011** yanı koruyan kalkan veya örtü — kişinin yanında taşıdığı kalkan veya koruyucu örtü
  سمي الترس مجنبا لأنه إلى جنب الإنسان (maqayis)؛ المجنب الترس (ayn;sihah;tahdhib)؛ المجنب الترس ويقال المجنب والمجنب الستر أيضا (jamhara)
- **B012** atın bacaklarında doğuştan ölçülü açıklık — atın bacaklarının doğuştan birbirinden ayrı durması, fakat aşırı ayrık olmaması
  التجنيب انحناء وتوتير في رجل الفرس (sihah)؛ المجنب من الخيل البعيد ما بين الرجلين من غير فجج والتجنيب بالجيم في الرجلين (tahdhib)؛ التجنيب الروح في الرجلين وذلك إبعاد إحدى الرجلين عن الأخرى خلقة (mufradat)

## ش ق و (root_000808): 87:11 ٱلْأَشْقَى

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ش ق ي (root_000809): for 87:11 ٱلْأَشْقَى: withheld observed target; not identity

- **B001** bedbahtlık ve bedbaht duruma düşürme — bedbaht olmak · bedbahtlık · bedbahtlık · bu dünyada veya ölümden sonraki yaşamda bedbahtlık · onu bedbaht duruma düşürmek
  الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)
- **B002** zorluk ve yorucu uğraş — güçlük, zorluk ve yorucu sıkıntı · bir işte yorulmak veya güçlük çekmek · uğraşma, yaşayarak sürdürme ve katlanma · bir işle uğraşmak ve ona katlanmak
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** biriyle karşılıklı uğraşıp mücadele etme — biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak · benimle çekişti, ben de onu o işte yendim
  المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)
- **B004** kolay çıkılan, oturmaya elverişli uzun dağ sırtı — kolay çıkılan ve oturmaya elverişli uzun dağ sırtı
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ص ل ي (root_000880): 87:12 يَصْلَى (also echo for 87:15 فَصَلَّىٰ)

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

## ص ل و (root_000879): 87:15 فَصَلَّىٰ (also echo for 87:12 يَصْلَى)

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

## ن و ر (root_001564): 87:12 ٱلنَّارَ

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

## ك ب ر (root_001281): 87:12 ٱلْكُبْرَىٰ

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

## م و ت (root_001454): 87:13 يَمُوتُ

- **B001** yaşamın ve canlı gücünün sona ermesi — ölüm; yaşamın sona ermesi · öldü; yaşamdan ayrıldı · öldü; yaşamdan ayrıldı · yakında ölecek kimse · ölmüş veya ölecek kimse · kesin ve gerçek ölüm
  أصل صحيح يدل على ذهاب القوة من الشيء (maqayis)؛ الموت خلاف الحياة (maqayis;sihah)؛ الموت معروف مات يموت موتا (jamhara)؛ الموت خلق من خلق الله (tahdhib)؛ أنواع الموت بحسب أنواع الحياة (mufradat)
- **B002** öldürme veya pişirerek keskinliğini giderme — öldürdü; gücünü giderdi · pişirerek keskinliğini giderin · içki pişirilip keskinliği giderildi
  أميتوها طبخا (maqayis)؛ أميتت الخمر طبخت (maqayis)؛ أماته الله وموته شدد للمبالغة (sihah)
- **B003** cansız şey; işlenmemiş veya sahipsiz arazi — işlenmemiş arazi; canlı olmayan şey · cansız şey; sahipsiz ve kullanılmayan arazi
  الموتان الأرض لم تحي بعد بزرع ولا إصلاح وكذلك الموات (maqayis)؛ الموات ما لا روح فيه (sihah)؛ الموات الأرض التي لا مالك لها ولا ينتفع بها أحد (sihah)؛ الموتان أن يبيع المتاع وكل شيء غير ذي روح (tahdhib)
- **B004** insanlar veya hayvan varlığı içinde ölüm görülmesi — insanlarda veya hayvanlarda görülen ölüm · mal veya hayvan varlığı içindeki ölüm
  وقع في الناس موتان (maqayis)؛ الموتان بالضم موت يقع في الماشية (sihah)؛ وقع في المال موتان وموات وهو الموت (tahdhib)
- **B005** çocuğu ölmüş ebeveyn veya ana hayvan — yavrusu ölmüş ana hayvan veya çocuğu ölmüş kadın · oğlu veya oğulları öldü
  ناقة مميت ومميتة للتي يموت ولدها (maqayis)؛ أماتت الناقة إذا مات ولدها فهي مميت ومميتة (sihah)؛ وكذلك المرأة (sihah)؛ أمات فلان إذا مات له ابن أو بنون (sihah)
- **B006** zekâ ve anlayıştan yoksunluk — zekâsı ve anlayışı kıt kimse · ne kadar anlayışsız!
  رجل موتان الفؤاد وامرأة موتانة (maqayis)؛ رجل موتان الفؤاد وامرأة موتانة الفؤاد (sihah)؛ رجل موتان الفؤاد إذا كان غير ذكي ولا فهم (tahdhib)
- **B007** usulüne uygun kesilmeden ölen yenilebilir hayvan — usulüne uygun kesilmeden ölmüş yenilebilir hayvan
  الميتة ما مات مما يؤكل لحمه إذا ذكي (maqayis)؛ الميتة ما لم تلحقه الذكاة (sihah)
- **B008** bir kez ölme veya ölüm biçimi — ölüm biçimi veya hali · bir kez ölme
  الموتة الواحدة من الموت (maqayis)؛ الميتة حال من الموت حسنة أو قبيحة (maqayis)؛ مات فلان ميتة حسنة (sihah)؛ الميتة الحال من أحوال الموت (tahdhib)
- **B009** ardından ayılınan geçici delilik, nöbet veya baygınlık — ardından ayılınan delilik benzeri hal, nöbet veya baygınlık
  الموتة شبه الجنون يعترى الإنسان (maqayis)؛ الموتة جنس من الجنون والصرع يعتري الإنسان (sihah)؛ الموتة الجنون (tahdhib)؛ الموتة الذي يصرع من الجنون أو غيره ثم يفيق (tahdhib)؛ الموتة شبه الغشية (tahdhib)
- **B010** bir işe kendini bütünüyle verme; savaşta ölümü göze alma [kalıp] — işe kendini bütünüyle veren · savaşta ölümü göze alarak dövüşen · ölümü gönüllü karşıladı
  المستميت للأمر المسترسل له (maqayis;sihah)؛ المستميت المستقتل الذي لا يبالي في الحرب من الموت (sihah)؛ استمات الرجل إذا طاب نفسا بالموت (tahdhib)؛ المستميت الذي يقاتل على الموت (tahdhib)
- **B011** ölmüş, deli veya alçakgönüllüymüş gibi davranma — gösteriş için aşırı alçakgönüllü görünen · canlıyken ölmüş gibi davrandı · deli veya alçakgönüllüymüş gibi davranan
  المتماوت من صفة الناسك المرائي (sihah)؛ المستميت الذي يتجان وليس بمجنون (tahdhib)؛ يتخاشع ويتواضع لهذا حتى يطعمه (tahdhib)؛ ضربته فتماوت إذا أرى أنه ميت وهو حي (tahdhib)؛ المتماوتون المراءون (tahdhib)
- **B012** rüzgârın dinmesi, kumaşın eskimesi veya insanın uyuması [kalıp] — rüzgâr dindi · kumaş eskidi ve yıprandı · adam uyudu ve hareketsizleşti
  الموت السكون (tahdhib)؛ ماتت الريح إذا سكنت (tahdhib)؛ مات الثوب ونام إذا بلي (tahdhib)؛ مات الرجل وهمد وهوم إذا نام (tahdhib)
- **B013** gerçeğe boyun eğme [kalıp] — adam gerçeğe boyun eğdi
  مات الرجل إذا خضع للحق (tahdhib)
- **B014** vurulmuş avın ölüp ölmediğini inceleme [kalıp] — avınızın ölüp ölmediğine bakın
  استميتوا صيدكم أي انظروا مات أم لا (tahdhib)؛ إذا أصيب فشك في موته (tahdhib)

## ح ي ي (root_000383): 87:13 يَحْيَىٰ, 87:16 ٱلْحَيَوٰةَ

- **B001** canlı olma, sürüp gitme ve canlandırma — yaşam · canlı; ölmesi düşünülemeyen varlık · canlı oldu ya da canlı kaldı · canlandırdı ya da yeniden yaşama döndürdü · yaşam · bitmeyen gerçek yaşam · ateşi üfleyerek canlandırdı · çocuğu yaşatan besin
  خلاف الموت (maqayis); الحياة ضد الموت والحي ضد الميت (jamhara;sihah); يقال حيي يحيا فهو حي (ayn;tahdhib); الحياة تستعمل للقوة النامية والحساسة والعاقلة والأخروية والباري حي (mufradat)
- **B002** yağmurla gelen toprak canlılığı ve bolluk — toprağı canlandıran yağmur ve bolluk · toprağı bitkili ve verimli buldum · topluluk yağmura ve bol ota kavuştu · körpe ve canlı bitki
  يسمى المطر حيا لأن به حياة الأرض (maqayis); الحيا مقصور حيا الربيع وهو ما تحيا به الأرض من الغيث (ayn); أحيا القوم أي صاروا في الحيا وهو الخصب وأتيت الأرض فأحييتها أي وجدتها خصبة (sihah); الحي من النبات ما كان طريا يهتز والحيا الغيث (tahdhib); الحيا المطر لأنه يحيي الأرض بعد موتها (mufradat)
- **B003** canlı varlık veya bitmeyen gerçek yaşam — canlı varlık, özellikle duyup hareket eden varlık · bitmeyen gerçek yaşam
  الحيوان كل ذي روح (ayn); الحيوان خلاف الموتان (sihah); الحيوان اسم يقع على كل شيء حي وكل ذي روح حيوان (tahdhib); الحيوان مقر الحياة وما له الحاسة وما له البقاء الأبدي (mufradat)
- **B004** yılan ve yılanla ilgili adlandırmalar — yılan · erkek yılan · yılan bakıcısı · yılanlı toprak
  الحية معروف يقال حية ذكر وحية أنثى والحيوت ذكر الحيات (jamhara); الحية اشتقاقها من الحياة (ayn); الحية تكون للذكر والأنثى والحيوت ذكر الحيات (sihah); اشتقاق الحية من الحياة ومن قال حواء قال من حويت لأنها تتحوى (tahdhib)
- **B005** kötü olandan utanarak çekinme — utanma ve kötü davranıştan çekinme · ondan utandı ve çekindi · ondan utandı ya da konuşmasına karşılık vermedi
  الاستحياء الذي هو ضد الوقاحة واستحييت منه (maqayis); حييت عن فلان إذا استحييت عنه (jamhara); حييت منه أحيا استحييت واستحياه واستحيا منه من الحياء (sihah); الحياء من الاستحياء ورجل حيي واستحيا الرجل (tahdhib); الحياء انقباض النفس عن القبائح وتركه (mufradat)
- **B006** öldürmeyip sağ bırakma — kadınları sağ bırakıyor ve öldürmüyorlar
  ويستحيون نساءكم أي لا يستبقي (sihah); استحيوا شرخهم بمعنى استفعلوا من الحياة أي استبقوهم ولا تقتلوهم (tahdhib); ويستحيون نساءكم أي يستبقونهن (mufradat)
- **B007** esenlik, uzun ömür ve kalıcılık dileği — Tanrı sana yaşam, kalıcılık ve esenlik versin · karşılama ve esenlik dileği · yoruma göre bütün esenlik, kalıcılık ya da egemenlik Tanrı'nındır
  حياك الله أي ملكك الله والتحيات لله أي الملك لله (sihah); التحية ما يحيي به بعضهم بعضا وتحية الله السلام عليكم ورحمة الله وحياك الله أي أبقاك (tahdhib); التحية أن يقال حياك الله أي جعل لك حياة ثم يجعل دعاء (mufradat)
- **B008** egemenlik bildiren kalıplaşmış söz — egemenlik ve yönetme gücü · bütün egemenlik Tanrı'nındır
  التحية الملك وحياك الله أي ملكك الله (sihah); التحية الملك وأنشد يعني على ملكه والتحيات لله الألفاظ التي تدل على الملك (tahdhib)
- **B009** bir şeye gelmeye çağırma — haydi ibadete gel · haydi et suyuna ekmek yemeğine gel
  قولهم حي على الصلاة معناه هلم وأقبل والعرب تقول حي على الثريد وهو اسم لفعل الأمر (sihah)
- **B010** ortak soylu topluluk veya boylar birliği — soy topluluğu ya da boy · aynı soydan gelen bir topluluk
  الحي حي من العرب وبنو حي بطن من العرب (jamhara); الحي واحد أحياء العرب (sihah); الحي الواحد من أحياء العرب يقع على بني أب كثروا أم قلوا وعلى شعب يجمع القبائل (tahdhib)
- **B011** dişi canlının üreme organı veya döl yatağı — dişi insan ya da hayvanın üreme organı veya döl yatağı
  حياء الناقة وهو فرجها يمكن أن يكون من هذا (maqayis); الحياء أيضا رحم الناقة والجمع أحيية (sihah); الحي فرج المرأة وحياء الشاة والناقة والمرأة ممدود (tahdhib)
- **B012** yüz — yüz
  المحيا الوجه (sihah)
- **B013** yarar, iyilik ve yok olmaktan koruma — yarar, iyilik ve yok olmaktan koruma · çocuğu yaşatan besin
  في القصاص حياة أي منفعة وليس بفلان حياة أي ليس عنده نفع ولا خير (tahdhib); ولكم في القصاص حياة أي يرتدع بالقصاص ومن أحياها أي من نجاها من الهلاك (mufradat)
- **B014** yaşamla ilişkilendirilen erkek kişi adları — yaşamla ilişkilendirilen erkek kişi adları
  حيي اسم رجل (jamhara); حيوة اسم رجل (sihah); حيوة اسم رجل بسكون الياء (tahdhib); اسمه يحيى نبه أنه سماه بذلك من حيث إنه لم تمته الذنوب (mufradat)

## ف ل ح (root_001175): 87:14 أَفْلَحَ

- **B001** yarmak veya kesip ayırmak — bir şeyi yarmak veya kesmek · toprağı sürmek üzere yarmak · toprağı sürmek üzere yarmak · demiri başka bir demirle yarmak veya kesmek · bir uzuvdaki yarıklar
  أصل يدل على شق (maqayis)؛ فلحت الأرض شققتها (maqayis;sihah;tahdhib)؛ فلحت الشيء إذا شققته أو قطعته (jamhara)؛ الحديد بالحديد يفلح أي يشق أو يقطع (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)
- **B002** dudakta, özellikle alt dudakta yarık — dudaktaki yarık · alt dudağı yarık olan erkek · dudağında yarık bulunan kadın · dudaktaki yarığın kendisi
  الفلح الشق في الشفة (ayn;tahdhib)؛ الأفلح المشقوق الشفة السفلى (maqayis;jamhara;sihah;tahdhib)؛ امرأة فلحاء وعنترة الفلحاء لفلحة كانت به (maqayis;jamhara;sihah;tahdhib)
- **B003** çiftçi ve toprağı işleme işi — çiftçi, toprağı işleyen kimse · toprağı sürme ve çiftçilik işi
  سمي الأكار فلاحا لأنه يشق الأرض (maqayis;jamhara;sihah;tahdhib;mufradat)؛ الفلاحون الزراعون (ayn)؛ الفلاحة الحراثة أو صناعة الفلاح (jamhara;sihah;tahdhib)
- **B004** çiftçiye benzetilen ücretli taşıyıcı — çiftçiye benzetilerek adlandırılan ücretli taşıyıcı
  الفلاح المكاري وإنما قيل له فلاح تشبيها بالأكار (ayn;tahdhib)؛ وجعله ابن أحمر المكاري (jamhara)
- **B005** iyilik içinde kalma, amaca ulaşma ve kurtuluş — iyilik içinde kalma, başarı ve kurtuluş · iyilik içinde kalma ve başarı · başarmak, amacına ulaşmak veya iyilik elde etmek · dilediğin biçimde yaşa · işinde başarı kazan ve onu kendi başına yürüt · kurtuluşa ve kalıcı iyiliğe yönel · iyilik elde eden başarılı kişi · dünya hayatında kalıcılık, varlık ve saygınlık elde etme · son bulmayan yaşam, yoksulluksuz varlık, aşağılanmayan saygınlık ve bilgisizlikten uzak bilgi · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الأصل الثاني الفلاح البقاء والفوز (maqayis)؛ الفلاح والفلح البقاء في الخير (ayn;tahdhib)؛ الفلح والفلاح البقاء (jamhara)؛ الفلاح الفوز والنجاة والبقاء (sihah)؛ أفلح وأنجح إذا أدرك مطلوبه (jamhara)؛ استفلحي بأمرك أي فوزي أو اظفري بأمرك (maqayis;sihah;tahdhib)؛ الفلاح الظفر وإدراك بغية (mufradat)
- **B006** orucu sürdürmeye güç veren şafak öncesi öğün — şafak öncesi öğün · şafak öncesi öğünü ya da gece ibadetinin kazancını kaçırmaktan korkmak
  الفلاح السحور (maqayis;ayn;sihah;tahdhib)؛ سمي فلاحا لأن الإنسان تبقى معه قوته على الصوم (maqayis)؛ لأن به بقاء الصوم (sihah;tahdhib)؛ سمي السحور الفلاح (mufradat)
- **B007** alışverişi çekici gösterme; yalanla kandırma ve alaya alma — satış ve alışverişi satıcıya ve alıcıya çekici göstermek · satış ve alışverişi satıcıya ve alıcıya çekici göstermek · onları kandırıp gerçeğe aykırı söz söylemek · başkasını daha yüksek bedel vermeye kandırmak için kiracının bedeli artırması · kandırma ve alaya alma
  فلحت للقوم وبالقوم أفلح فلاحة وهو أن يزين البيع والشراء للبائع والمشتري (tahdhib)؛ فلحت بهم تفليحا إذا مكر بهم وقال لهم غير الحق (tahdhib)؛ الفلح النجس وهو زيادة المكتري ليزيد غيره فيغر به (tahdhib)؛ التفليح المكر والاستهزاء (tahdhib)

## ز ك و (root_000637): 87:14 تَزَكَّىٰ

- **B001** büyüyüp artma — büyümek, artmak ve verim kazanmak · büyüme ve artış · gelişmiş ve artışı belirgin · Tanrı onu büyütüp artırdı · ekin büyüyüp arttı · kişi bolluğa kavuşup rahat yaşadı
  أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)
- **B002** ahlaken arınıp düzgünleşme — arınmak ve düzgünleşmek · temiz, doğru ve kötülükten sakınan · arındırıp düzeltmek · arındırma, düzeltme ve iyiliklerle geliştirme · iç temizliği ve ahlaki düzgünlük · kendini övmek veya sözle temiz saymak · dinen uygun ve sonu zarar vermeyen yiyecek · temizlik ve düzgünlük
  الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)
- **B003** yoksula verilmesi gereken mal payı — yoksullara verilmesi gereken mal payı · malının gereken payını ödemek · malından karşılıksız vermek
  زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)
- **B004** yakışmamak [kalıp] — ona yakışmamak veya durumuna uygun düşmemek
  أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)
- **B005** çift olma — çift veya iki öğeli · tek veya çift · avuçtaki çift mi tek mi · avuçtaki şey için tek-çift söylemek
  الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)

## ء ث ر (root_000011): 87:16 تُؤْثِرُونَ

- **B001** en başa almak; yapmaya kesin karar vermek [kalıp] — her şeyden önce · ilk iş olarak · yapmaya kesin karar verdi
  له أصل تقديم الشيء (maqayis)؛ آثرا ما وآثر ذي أثير أي أول كل شيء (maqayis;sihah;tahdhib)؛ إن آثرت أن تأتينا فأتنا وقد أثر أن يفعل ذلك الأمر أي فرغ له وعزم عليه (tahdhib)؛ خذه آثرا ما وإثرا ما وأثر ذي أثير (mufradat)
- **B002** aktarılıp kalıcılaşan anlatı veya bilgi — sözü başkasından aktardı · kuşaktan kuşağa aktarılan söz · anlatılagelen değerli işler · aktarılmış veya yazıya geçirilmiş bilgi
  من قولك أثرت الحديث وحديث مأثور (maqayis)؛ أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور (sihah)؛ حديث مأثور أي يخبر الناس به بعضهم بعضا (tahdhib)؛ أثرت العلم رويته وآثره أثرا وأثارة وأثرة (mufradat)؛ المآثر ما يروى من مكارم الإنسان (mufradat;tahdhib)
- **B003** geride kalan belirti veya iz — geride kalan iz · yara izi · bilgiden kalma bir parça veya belirti
  الأثر بقية ما يرى من كل شيء وما لا يرى بعد أن تبقى فيه علقة (maqayis)؛ الأثر بالتحريك ما بقي من رسم الشيء (sihah)؛ أثر الشيء حصول ما يدل على وجوده (mufradat)؛ أثارة من علم بقية من علم وعلامة (tahdhib)؛ الأثر من الجرح وغيره في الجسد يبرأ ويبقى أثره (sihah;tahdhib)
- **B004** izinden giderek takip etmek — ardından, izinden giderek · öncekinin geçtiğini gösteren yol
  الأثر الاستقفاء والاتباع وذهبت في إثره (maqayis)؛ خرجت في إثره أي في أثره (sihah)؛ جاء فلان على إثري وأثري وجاء في أثره وإثره (tahdhib)؛ الطريق المستدل به على من تقدم آثار وهم أولاء على أثري (mufradat)
- **B005** üstün tutmak ve gözde saymak — başkasını veya bir şeyi üstün tutma · özel yakınlık gören gözde kişi
  الأثير الكريم عليك الذي تؤثره بفضلك وصلتك (maqayis)؛ آثرت فلانا على نفسي من الإيثار (sihah)؛ آثرتك إيثارا أي فضلتك وآثرك الله علينا (tahdhib)؛ الإيثار للتفضل ويؤثرون على أنفسهم وتالله لقد آثرك الله علينا (mufradat)
- **B006** başkalarını dışlayarak kendine ayırmak — bir şeyi yalnız kendine ayırma · başkaları dışlanarak sağlanan ayrıcalık · ortaklarına karşı her şeyi kendine ayıran kişi
  استأثر الله بفلان واستأثرت عليك ورجل أثر يستأثر على أصحابه وستَرون بعدي أثرة (maqayis)؛ استأثر فلان بالشيء أي استبد به والاسم الأثرة (sihah)؛ رجل أثر وهو الذي يستأثر على أصحابه وإنكم ستلقون بعدي أثرة واستأثر الله بالبقاء أي انفرد بالبقاء (tahdhib)؛ الاستئثار التفرد بالشيء من دون غيره وسيكون بعدي أثرة (mufradat)
- **B007** kılıcın yüzey deseni, parlaklığı veya darbesi — kılıcın yüzey deseni, parlaklığı veya darbesi · yüzeyinde özel bir iz bulunan ya da insanüstü varlıkların yaptığı söylenen kılıç
  أثر السيف ضربته والأثر في السيف الفرند ويسمى السيف مأثورا (maqayis)؛ الأثر فرند السيف والمأثور السيف (sihah)؛ أثر السيف فرنده وأثر السيف ضربته وأثره مفتوح رونقه (tahdhib)؛ أثر السيف جوهره وأثر جودته وهو الفرند وسيف مأثور (mufradat)
- **B008** deve ayağını iz bırakacak biçimde işaretleme ve işaretleme demiri — deve ayağı işaretleme demiri · devenin ayağına yerde iz bırakacak işaret koydu
  الآثر الذي يؤثر خف البعير والمئثرة حديدة يؤثر بها في باطن فرسن البعير (maqayis)؛ الأثرة أن يسحى باطن خف البعير بحديدة وتلك الحديدة مئثرة (sihah)؛ المئثرة حديدة يؤثر بها خف البعير ليعرف أثره في الأرض (tahdhib)؛ أثرت البعير جعلت على خفه أثرة أي علامة تؤثر في الأرض (mufradat)
- **B009** eski yağ kalıntısı, yağ özü veya arınmış süt — devede önceden kalma yağ · yağ özü veya tereyağından ayrılarak arınmış süt
  الإبل على أثارة أي على شحم قديم وإذا تخلص اللبن من الزبد وخلص فهو الأثر (maqayis)؛ الأثر بالكسر خلاصة السمن وسمنت الإبل على أثارة أي بقية شحم (sihah)؛ الأثر خلاصة السمن والإثر بكسر الهمزة خلاصة السمن وسمنت الناقة على أثارة (tahdhib)؛ سمنت الإبل على أثارة أي على أثر من شحم (mufradat)
- **B010** ömrün sonu veya kişinin ardından kalan işler — ömrün belirlenmiş sonu · kişinin ardından kalan işler ve uygulamalar
  ينسأ في أثره أي في أجله وسمي الأجل أثرا لأنه يتبع العمر (tahdhib)؛ ونكتب ما قدموه من الأعمال وسنوه من سنن يعمل بها (tahdhib)
- **B011** alışarak kavrayıp ustalaşmak [kalıp] — konuyu iyice kavrayıp ustalaştı
  أثر فلان يقول كذا وطبن وطبق ودبق ولفق وفطن وذلك إذا أبصر الشيء وضري بمعرفته وحذقه (tahdhib)
- **B012** keçi memesi koruyucu torbası — keçinin memesine bağlanan koruyucu torba
  الإثار شبه الشمال يشد على ضرع العنز شبه كيس لئلا تعان (tahdhib)

## ECHO ث و ر (root_000210): for 87:16 تُؤْثِرُونَ: withheld observed target; not identity

- **B001** gizlilikten çıkıp belirerek yayılma — durgunluktan çıkıp belirmek ve yayılmak · tozun veya bulutun yükselip yayılması · hastalık döküntüsünün ortaya çıkıp yayılması · böcek sürüsünün saklandığı yerden çıkıp sıçrayarak yayılması · alacakaranlığın yayılması veya en yoğun bölümünün görünmesi · içi kalkmak · saçı dağılıp kabarmış
  أصل انبعاث الشيء (maqayis)؛ ثار الغبار والسحاب ونحوهما انتشر ساطعا (mufradat)؛ ثار الغبار يثور ثورا وثورانا أي سطع (sihah)؛ ثارت الحصبة... وثار الجراد... وثار الماء... وثار الغبار وغيره كذلك (jamhara)
- **B002** yerinden kaldırıp harekete geçirme — bir şeyi yerinden oynatıp harekete geçirmek · toprağı eşeleyip kaldırmak · erkek sığırın toprağı ayaklarıyla eşeleyip kaldırması · tavşanı ürkütüp saklandığı yerden çıkarmak · Kur'an bilgisini derinlemesine araştırıp ortaya çıkarmak · rahatsız edip yerinden kaldırmak
  أثرت الأرض إثارة (jamhara)؛ أثار الثور التراب إذا بحثه بقوائمه (jamhara)؛ وأثاره غيره (sihah)؛ وثور القرآن أي بحث عن علمه (sihah)؛ فتثير سحابا... وأثاروا الأرض (mufradat)
- **B003** saldırgan biçimde kabarıp karşı koyma — birinin üzerine atılıp saldırmak · halkın birinin üzerine ayaklanması · kötülüğü kışkırtıp onlara karşı ortaya çıkarmak · öfkesi kabarıp dışa vurulmak · taşkınlık ve kargaşa
  ثاور فلان فلانا إذا واثبه (maqayis;jamhara)؛ ثار به الناس أي وثبوا عليه (sihah)؛ المثاورة المواثبة (sihah)؛ انتظر حتى تسكن هذه الثورة وهي الهيج (sihah)؛ ثور فلان عليهم الشرا أي هيجه وأظهره (sihah)؛ ثار ثائره كناية عن انتشار غضبه (mufradat)
- **B004** erkek sığır — yabani veya evcil erkek sığır · dişi sığır · erkek sığırlar · sığırların sudan kaçınması üzerine söylenen, hayvan ya da yosun diye yorumlanan örnek söz
  جنس من الحيوان (maqayis)؛ والثور ذكر البقر الوحشية والأهلية (jamhara)؛ والثور الذكر من البقر والأنثى ثورة (sihah)؛ والثور البقر الذي يثار به الأرض (mufradat)
- **B005** kurutulmuş çökelek parçası — kurutulmuş çökelekten bir parça, özellikle iri bir parça
  الثور فالقطعة من الأقط (maqayis)؛ والثور القطعة العظيمة من الأقط والجمع أثوار وثورة (jamhara)؛ والثور قطعة من الأقط والجمع ثورة (sihah)
- **B006** dağ, topluluk veya burç için özel ad — belirli bir dağın adı · belirli bir boyun veya kabilenin adı · gökteki belirli bir burcun adı
  وثور جبل وثور قوم من العرب وهذا على التشبيه (maqayis)؛ والثور جبل معروف يسمى ثور أطحل وبنو ثور بطن من الرباب (jamhara)؛ وثور أبو قبيلة من مضر وثور جبل بمكة... والثور برج من السماء (sihah)
- **B007** su yüzeyini kaplayan yosun — su yüzeyine çıkıp tabaka oluşturan yosun · sığırların sudan kaçınması üzerine söylenen, hayvan ya da yosun diye yorumlanan örnek söz
  الثور فيمن يقول إنه الطحلب... ثار على متن الماء (maqayis)؛ يقال للطحلب ثور الماء (sihah)

## ح ي و (root_005544): documented alternative for 87:16 ٱلْحَيَوٰةَ: Halîl b. Ahmed, el-Ayn; incelenmiş Furûk root_005544/B001 dalı

- **B001** yaşam ve canlı olma — 
  الحيوة كتبت بالواو؛ يقال حيي يحيا فهو حي؛ ولغة أخرى حي يحي والجميع حيوا (ayn)
- **B002** canlı varlık — 
  والحيوان كل ذي روح الواحد والجميع فيه سواء (ayn)
- **B003** cennette, değdiği her şeyi Tanrı'nın izniyle canlandıran su — 
  والحيوان ماء في الجنة لا يصيب شيئا إلا حي بإذن الله (ayn)
- **B004** yılan adının yaşam kökenli çözümlemesi — 
  والحَيَّة اشتقاقها من الحياة؛ هي في أصل البناء حيوة؛ ومن قال لصاحب الحَيّات حاي فهو فاعل من هذا البناء؛ ومن قال حواء على فعال فإنه يقول اشتقاق الحَيَّة من حَوَيْت لأنها تتحوى في التوائها (ayn)
- **B005** toprağı canlandıran bahar yağmuru — 
  والحَيَا مقصور حَيَا الربيع وهو ما تحيا به الأرض من الغيث (ayn)

## د ن و (root_000493): 87:16 ٱلدُّنْيَا

- **B001** yakın olma, yaklaşma veya yaklaştırma — yakın olmak veya yaklaşmak · yakında bulunan · birini veya bir şeyi yaklaştırmak · iki şeyi birbirine yaklaştırmak · yakın akrabalık · adım adım yaklaşmak · birbirlerine yaklaşmak · yakın olan · yakın dereceden amca oğlu · yemekte önündeki yakın kısımdan yemek
  أصل واحد وهو المقاربة (maqayis)؛ دنوت منه دنوا وأدنيت غيري (sihah)؛ الدنو القرب بالذات أو بالحكم (mufradat)؛ دانيت بين الأمرين قاربت بينهما (maqayis;sihah;mufradat)؛ دناوة أي قرابة (sihah)؛ فدنوا أي كلوا مما يليكم (maqayis;sihah;mufradat)
- **B002** bu yaşam veya karşıtına göre yakın, küçük ya da ilk olan — bu yaşam, ilk yaşam · bu yaşama ilişkin · bu yaşama ilişkin · karşıtına göre daha yakın veya daha küçük olan · ilk iş olarak · yakın kıyı veya yakın taraf
  سميت الدنيا لدنوها (maqayis;sihah)؛ يعبر بالأدنى تارة عن الأصغر وتارة عن الأول وتارة عن الأقرب (mufradat)؛ الدنيا والآخرة (mufradat)؛ العدوة الدنيا والعدوة القصوى (mufradat)؛ لقيته أدنى دنى أي أول شيء (maqayis;sihah)
- **B003** değersizlik, aşağı konum, güçsüzlük veya eksiklik — değersiz ve aşağı kimse · değersizleşmek veya alçalmak · kusur veya eksiklik · küçük ve değersiz işlerin peşine düşmek · daha kötü ve aşağı olan
  الدني من الرجال الضعيف الدون (maqayis)؛ الدنىء الدون مهموز (maqayis)؛ الدنية النقيصة (maqayis)؛ الدني بمعنى الدون فهو مهموز (sihah)؛ يدني في الأمور تدنية أي يتتبع صغيرها وخسيسها (sihah)؛ خص الدنيء بالحقير القدر (mufradat)؛ الأدنى عن الأرذل (mufradat)
- **B004** dişi hayvanda doğumun yaklaşması [kalıp] — kısrak veya dişi devenin doğumunun yaklaşması
  أدنت الفرس وغيرها إذا دنا نتاجها (maqayis)؛ أدنت الناقة إذا دنا نتاجها (sihah)؛ أدنت الفرس دنا نتاجها (mufradat)
- **B005** üst gövdesi göğsüne doğru kapanmış erkek — üst gövdesi göğsüne doğru kapanmış erkek
  الأدنأ من الرجال الذي فيه انكباب على صدره (maqayis)؛ لأن أعلاه دان من وسطه (maqayis)

## ء خ ر (root_000019): 87:17 وَٱلْءَاخِرَةُ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## خ ي ر (root_000452): 87:17 خَيْرٌ

- **B001** arzulanan iyilik — iyilik; yarar veya üstünlük taşıyan olumlu şey
  فالخير خلاف الشر لأن كل أحد يميل إليه (maqayis)؛ الخير ضد الشر (jamhara;sihah)؛ الخير ما يرغب فيه الكل وضده الشر (mufradat)؛ يقابل به الشر مرة والضر مرة (mufradat)
- **B002** iyi ve seçkin olma — iyi ve üstün nitelikli · üstün, güzel veya seçkin olan · üstün veya seçkin kimse ya da şey · iyi ve erdemli kişiler · üstün, güzel veya seçilmiş olanlar
  رجل خير وامرأة خيرة فاضلة وقوم خيار وأخيار في صلاحها وامرأة خيرة في جمالها وميسمها (maqayis;ayn)؛ رجل خير إذا كان فيه خير ورجل خيار من قوم خيار وأخيار والأخيار خلاف الأشرار (jamhara)؛ الخيرات جمع خيرة وهي الفاضلة من كل شيء (sihah)؛ فيهن مختارات لا رذل فيهن والخير الفاضل المختص بالخير (mufradat)
- **B003** daha iyi olanı seçme — seçim veya seçim hakkı · seçim, seçilmiş şey veya seçim sonucu · daha iyi olanı arayıp seçme · seçmek veya üstün tutmak · Yaratıcıdan kişi için iyi sonucu dilemek · Yaratıcının kişi için iyi olanı seçip vermesi · iki şey arasında seçim hakkını ona bırakmak · seçimde üstün gelmek veya diğerini geçmek · seçen ya da seçilmiş olan
  الخيرة الخيار والاستخارة أن تسأل خير الأمرين لك ويقال خايرت فلانا فخرته وتقول اختر (maqayis)؛ خايرت فلانا فخرته والله يخير للعبد إذا استخاره وهذا وهذه وهؤلاء خيرتي وهو ما تختاره (ayn)؛ الخيار الاسم من الاختيار والخيرة من قولك خار الله لك والاختيار الاصطفياء والاستخارة الخيرة وخيرته بين الشيئين (sihah)؛ الاختيار طلب ما هو خير وفعله واستخار الله العبد فخار له وخايرت فلانا كذا فخرته (mufradat)
- **B004** mal, özellikle çok veya övülen bir yoldan edinilmiş servet — mal, özellikle çok veya iyi yoldan edinilmiş servet
  إن ترك خيرا أي مالا (sihah;mufradat)؛ لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب (mufradat)؛ وإنه لحب الخير لشديد أي المال الكثير (mufradat)؛ ما كان مجموعا من المال من وجه محمود (mufradat)
- **B005** cömertlik ve armağan verme — cömertlik, armağan ve verme
  والخير الكرم (maqayis)؛ الخير الهبة (ayn)؛ رجل ذو خير إذا كان كثير الخير (jamhara)؛ الخير بالكسر الكرم (sihah)
- **B006** bir geçidi tıkayıp hayvanı yuvasından çıkarma [kalıp] — sırtlanı, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma · çöl sıçanını, yuvasının bir geçidini tıkayarak başka çıkıştan çıkarma
  استخاره الضبع وهو أن تجعل خشبة في ثقبة بيتها حتى تخرج من مكان إلى آخر (maqayis)؛ يستخير الضبع واليربوع إذا جعل في موضع النافقاء فخرج من القاصعاء (ayn)

## ب ق ي (root_000142): 87:17 وَأَبْقَىٰٓ

- **B001** varlığını sürdürme ve yok olmama — varlığını sürdürdü, yok olmadı · sürdü, kalıcı oldu · varlığını sürdürme, yok olmama · varlığını sürdüren, yok olmayan · kalmasını sağladı veya ömrünü uzattı · daha kalıcı, daha uzun süreli · karşılığı kalıcı olan iyi işler veya ibadetler · kalma, geride kalan kişi veya topluluk
  أصل واحد وهو الدوام (maqayis)؛ بقي الشيء يبقى بقاء وهو ضد الفناء (maqayis;ayn;tahdhib)؛ بقى الشيء يبقى بقاء وبقي الرجل زمانا طويلا أي عاش (sihah)؛ البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء (mufradat)؛ الباقيات الصالحات هي الصلوات الخمس وقيل الأعمال الصالحة كلها (tahdhib;mufradat)
- **B002** bir şeyden geriye kalan bölüm — bir şeyden geriye kalan, artık · geriye kalan bölüm · gelir veya vergiden kalan tutar · kendilerinde iyilik ve sağlamlık kalmış kimseler · Tanrı'nın size helal olarak bıraktığı şey; ayrıca Tanrı'yı gözetme
  نشدتك الله والبقيا وهي البقية (maqayis;ayn;tahdhib)؛ بقي من الشيء بقية والباقية توضع موضع المصدر (sihah)؛ الباقي حاصل الخراج ونحوه (tahdhib)؛ بقيت الله أي ما أبقى لكم من الحلال (tahdhib)؛ أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير (tahdhib)؛ فهل ترى لهم من باقية أي جماعة باقية أو فعلة لهم باقية وقيل معناه بقية (mufradat)
- **B003** bağışlayıp sağ bırakma — Tanrı aşkına bize acıyın ve bizi sağ bırakın · acıma ve sağ bırakma · ona acıdı ve onu sağ bıraktı · onu bağışlayıp sağ bıraktı veya sevgisini korudu · bizi yok etmeyin, sağ bırakın
  استبقيت فلانا أن تعفو عن زلله فتستبقي مودته (maqayis)؛ استبقيت فلانا إذا أوجبت عليه قتلا وعفوت عنه واستبقيت مودته (ayn;tahdhib)؛ أبقيت على فلان إذا أرعيت عليه ورحمته واستبقاه استحياه (sihah)؛ العرب تقول للعدو إذا غلب البقية أي أبقوا علينا ولا تستأصلونا (tahdhib)
- **B004** bir bölümünü ayırıp elde tutma — bir bölümünü ayırıp elde tuttum · koşu gücünün bir bölümünü sonraya saklayan atlar
  إذا أعطيت شيئا وحبست بعضه قلت استبقيت بعضه (ayn;tahdhib)؛ استبقيت من الشيء أي تركت بعضه (sihah)؛ المبقيات من الخيل التي تبقي بعض جريها تدخره (tahdhib)
- **B005** gözetleyerek bekleme — onu gözetip bekledim · onu gözleriyle izleyip gözetliyor · geceyi şimşeğin nerede parlayacağını gözleyerek geçirdi · ibadet çağrısını benim için gözet · Tanrı'nın elçisini uzun süre bekleyip gözledik · ona bakıp onu gözetledi · ona bakıp onu gözetledi · ona bakıp onu gözetledi
  يبقى الشيء ببصره إذا كان ينظر إليه ويرصده (maqayis;ayn)؛ بات فلان يبقي البرق أي ينظر إليه من أين يلمع (maqayis;ayn)؛ بقيت فلانا أبقيه إذا رعيته وانتظرته (maqayis)؛ بقيته أبقيه أي نظرت إليه وترقبته وبقينا رسول الله أي انتظرناه (sihah)؛ بقينا رسول الله أي انتظرناه وترصدنا له مدة كثيرة (mufradat)

## ص ح ف (root_000845): 87:18 ٱلصُّحُفِ, 87:19 صُحُفِ

- **B001** yayılmış geniş yüzey — yayılmış geniş yüzey · yeryüzünün görünen yüzü · yüz derisi
  أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)
- **B002** yazı yaprağı veya kitap — yazı yazılan yaprak veya kitap · yazı yaprakları · yazı yaprakları · yazı yaprakları için seyrek bir çoğul biçim
  الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)
- **B003** iki kapak arasında toplanmış yazı yaprakları — iki kapak arasında toplanmış yazı yaprakları bütünü · yazı yapraklarını iki kapak arasında toplamak
  سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)
- **B004** yayvan çanak; küçük su biriktirme çukuru — geniş ve yayvan çanak · geniş ve yayvan çanaklar · su için yapılmış küçük biriktirme çukurları
  الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)
- **B005** harf benzerliğinden doğan yanlış okuma veya aktarım — benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım · benzer harfleri karıştırıp metni yanlış aktaran kişi
  الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)

## ء و ل (root_000067): 87:18 ٱلْأُولَىٰ

- **B001** başlangıç ve öncelik — ilk; önde gelen · ilk olan kadın ya da dişil şey · ilkler; öncekiler · topluluğun önünde bulunma · sürünün önünde giden dişi ya da erkek deve · önceki yıl · her şeyden önce
  الأول وهو مبتدأ الشيء؛ ناقة أولة وجمل أول إذا تقدما الإبل (maqayis)؛ أول في اللغة على الحقيقة ابتداء الشيء؛ جاء فلان في أولية الناس إذا جاء في أولهم (tahdhib)
- **B002** sonuca dönme ve varma — geri dönmek; sonunda bir duruma varmak · hükmü sahiplerine geri vermek · bedeni zayıflamak · sözün sonucu veya anlamının açıklanması · açıklamak; anlamına döndürmek · onunla ilgili ödülü gözetmek ve aramak
  آل يؤول أى رجع؛ تأويل الكلام وهو عاقبته وما يؤول إليه (maqayis)؛ التأويل تفسير ما يؤول إليه الشئ؛ آل أي رجع (sihah)؛ آل يؤول أي رجع وعاد؛ التأويل المرجع والمصير (tahdhib)
- **B003** aile ve bağlı çevre — kişinin ailesi, ev halkı ve yakınları · onun izleyicileri ve bağlıları · kişinin sığındığı ev halkı · kişinin kökü ve bağlı olduğu aile
  آل الرجل أهل بيته؛ لأنه إليه مآلهم وإليهم مآله (maqayis)؛ آل الرجل أهله وقرابته (jamhara)؛ آل الرجل أهله وعياله؛ وآله أيضا أتباعه (sihah)؛ إلة الرجل أهل بيته؛ إيلة الرجل فهم أصله الذين يؤول إليهم (tahdhib)
- **B004** iyi yönetip düzene koyma — iyi yönetme ve gözetme · yöneticinin halkını iyi yönetip gözetmesi · malını düzeltip iyi yönetmek · düzeltme ve iyi yönetme · Tanrı işini toparlayıp düzeltsin
  الإيالة السياسة؛ آل الرجل رعيته يؤولها إذا أحسن سياستها (maqayis)؛ الايالة السياسة؛ آل الأمير رعيته يؤولها أولا وإيالا؛ آل ما له أي أصلحه وساسه (sihah)؛ ألت الشيء جمعته وأصلحته؛ أول الله عليك أمرك أي جمعه (tahdhib)
- **B005** koyulaşıp pıhtılaşma — sütün koyulaşıp pıhtılaşması · katranın veya balın koyulaşıp katılaşması · pıhtılaşmış süt
  آل اللبن أي خثر؛ لا يخثر إلا آخر أمره؛ آل القطران إذا خثر (maqayis)؛ آل القطران أو العسل إذا أعقد بالنار (jamhara)؛ آل القطران والعسل أي خثر؛ الآيل اللبن الخاثر (sihah)
- **B006** görünür siluet ve dış uçlar — görünür siluet; uzaktan beliren görüntü · adamın görünen silueti · dağın uçları ve yanları
  آل الرجل شخصه؛ آل كل شيء؛ آل الجبل أطرافه ونواحيه (maqayis)؛ الآل السراب؛ آل كل شيء شخصه (jamhara)؛ الآل الشخص؛ الآل الذي تراه في أول النهار وآخره كأنه يرفع الشخوص وليس هو السراب (sihah)
- **B007** içinde bulunulan durum — içinde bulunulan durum
  الآلة الحالة (maqayis)؛ والآلة الحالة (jamhara)؛ والآلة الحالة يقال هو بآلة سوء (sihah)
- **B008** araç ve taşıyıcı düzen — araç · çadır direkleri ve taşıyıcı ağaçları · cenaze veya ölüyü taşıyan sedye
  آل الخيمة العمد (maqayis)؛ الآلة الأداة؛ خشبات تبنى عليها الخيمة؛ الآلة الجنازة (sihah)
- **B009** erkek yabani dağ keçisi — erkek yabani dağ keçisi
  الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن (maqayis)؛ الايل أيضا الذكر من الاوعال (sihah)
- **B010** içecek olgunlaştırma kabı — içecek olgunlaştırma kabı
  الإيال على فعال وعاء يجمع فيه الشراب اياما حتى يجود (maqayis)
- **B011** kumda yetişen yem bitkisi — kumda yetişen bir yem bitkisi
  التأويل نبت يعتلفه الحمار؛ التأويل اسم بقلة يولع بها بقر الوحش تنبت في الرمل (tahdhib)

## ECHO و ل ي (root_001684): for 87:18 ٱلْأُولَىٰ: withheld observed target; not identity

- **B001** aralıksız yakınlık — yakınlık ve bitişiklik · sana yakın veya yanında olan şey · bir eve bitişik olan ev
  أصل صحيح يدل على قرب؛ الولي القرب؛ جلس مما يليني أي يقاربني (maqayis)؛ دار فلان ولي دار فلان؛ الدار ولية أي قريبة (jamhara)؛ الولي القرب والدنو؛ كل مما يليك أي مما يقاربك (sihah)؛ الولي القرب (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما؛ يستعار ذلك للقرب (mufradat)
- **B002** kesintisiz ardışıklık — kesintisiz sıra · araya kesinti girmeden peş peşe oluş · şeyleri veya işleri peş peşe getirme · iki şeyi peş peşe getirmek · peş peşe isabet eden üç ok
  يوالي بين رميتين أو فعلين؛ أصبته بثلاثة أسهم ولاء؛ على الولاء أي الشيء بعد الشيء (ayn)؛ واليت بين الشيئين؛ افعل هذا على الولاء أي مرتبا (maqayis)؛ واليت بين الشيئين موالاة وولاء (jamhara)؛ والى بينهما ولاء أي تابع؛ على الولاء أي متتابعة؛ توالى عليه شهران (sihah)؛ الموالاة المتابعة؛ بثلاثة أسهم ولاء أي تباعا؛ توالت إلي كتب فلان (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما (mufradat)
- **B003** bir işi üstlenip yönetme — yönetim ve yetki alanı · bir yeri veya işi yöneten kişi · başkasının işlerinden sorumlu kişi · bir işi üstlenmek
  الولاية مصدر الوالي (ayn)؛ كل من ولى أمر آخر فهو وليه (maqayis)؛ الولاية الإمارة (jamhara)؛ ولي الوالي البلد؛ تولى العمل أي تقلد؛ الولاية بالكسر السلطان (sihah)؛ الولاية التي بمنزلة الإمارة؛ ولي اليتيم الذي يلي أمره؛ ولي المرأة؛ وليت فلانا عمل ناحيته؛ توليت الأمر توليا (tahdhib)؛ الولاية تولي الأمر؛ حقيقته تولي الأمر (mufradat)
- **B004** yakın durup destek olma — dost, seven veya destekleyen kişi · destekçi, anlaşmalı dost veya yakın yoldaş · birini sevip destekleme veya kayırma · birini sevmek, desteklemek veya kayırmak
  المولى الحليف والولي؛ الموالاة اتخاذ المولى (ayn)؛ المولى الصاحب والحليف والناصر؛ كل هؤلاء من الولي وهو القرب (maqayis)؛ الولي خلاف العدو (jamhara)؛ الولى ضد العدو؛ المولى الناصر والحليف؛ الموالاة ضد المعاداة (sihah)؛ الولي التابع المحب؛ الولاية من النصرة والنسب؛ الولاية على الإيمان؛ المولى في الدين؛ الناصر؛ والى فلان فلانا إذا أحبه؛ فيواليه أي يحابيه (tahdhib)؛ يستعار للقرب من حيث الدين والصداقة والنصرة والاعتقاد؛ الولاية النصرة (mufradat)
- **B005** özel yakınlık ve bağlılık bağı — özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi · özgür bırakma ilişkisine bağlı özel hak ve mensubiyet · soy yakınları veya özgür bırakma bağıyla bağlı kişiler · nimet veya özgür bırakma bağı kuran kişi
  الموالي بنو العم؛ المولى المعتق والحليف والولي؛ الولي ولي النعم (ayn)؛ المولى المعتق والمعتق والصاحب والحليف وابن العم والناصر والجار؛ الولاء ولاء المعتق (maqayis)؛ المولى المعتق والمعتق وابن العم والناصر والجار؛ الولي الصهر؛ بينهما ولاء أي قرابة؛ الولاء ولاء المعتق (sihah)؛ المولى العصبة؛ المولى الحليف؛ المولى المعتق؛ ابن العم والعم والأخ والابن والعصبات كلهم؛ مولى النعمة؛ المعتق؛ يجب عليك أن تنصره وترثه (tahdhib)
- **B006** yüzünü veya dikkatini yöneltme — yüzünü bir şeye çevirmek · yüzünü o yöne dönmüş veya ona uyan kişi · kulağını veya dikkatini bir şeye vermek
  موليها أي مستقبلها بوجهه (sihah)؛ التولية تكون إقبالا؛ فول وجهك أي وجه وجهك نحوه؛ هو مستقبلها؛ متوليها أي متبعها وراضيها (tahdhib)؛ وليت سمعي كذا ووليت عيني كذا ووليت وجهي كذا أقبلت به عليه (mufradat)
- **B007** dönüp yüz çevirme [kalıp] — arkasını dönüp kaçarak uzaklaşmak · birinden yüz çevirmek ve ilgiyi kesmek
  ولى الرجل أي أدبر (ayn)؛ تولى عنه أي أعرض؛ ولى هاربا أي أدبر (sihah)؛ التولية تكون انصرافا؛ وليتم مدبرين؛ التولي يكون بمعنى الإعراض (tahdhib)؛ إذا عدي بعن اقتضى معنى الإعراض وترك قربه؛ التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار (mufradat)
- **B008** daha uygun ve hak sahibi olma — bir şeye daha uygun, daha layık veya daha hak sahibi olmak · iki daha haklı veya daha uygun kişi
  فلان أولى بكذا أي أحرى به وأجدر (maqayis)؛ فلان أولى بكذا أي أحرى به وأجدر (sihah)؛ فلان أولى بهذا الأمر أي أحق به؛ الأوليان أي الأحقان (tahdhib)
- **B009** yaklaşan kötü sonuç tehdidi — tehdit ve uyarı sözü; sana kötü şey yaklaştı
  أولى تهدد ووعيد؛ معناه قاربه ما يهلكه؛ أولى تحسير له على ما فاته (maqayis)؛ أولى لك تهدد ووعيد؛ معناه قاربه ما يهلكه؛ قارب أن يزيد (sihah)؛ أولى لك تهدد ووعيد؛ قاربك ما تكره؛ يحسره على ما فاته (tahdhib)
- **B010** önceki yağmuru izleyen yağmur — önceki yağmurdan sonra gelen yağmur · erken mevsim yağmurunu izleyen yağmur adı · toprağa izleyen yağmurun yağması · iyilik ardından gelen yağmur veya iyilik
  الولي المطر الذي يكون بعد الوسمي؛ وليت الأرض وليا فهي مولية (ayn)؛ الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي (maqayis)؛ الولي المطرة بعد الوسمي؛ وليت الأرض فهي مولية (jamhara)؛ الولي المطر بعد الوسمي؛ وليت الأرض وليا (sihah)؛ الولي المطر الذي يأتي بعد المطر؛ وليت الأرض وليا؛ أمطرني ولية منك (tahdhib)
- **B011** deve sırtı alt örtüsü — deve sırtında semer altında kullanılan örtü · semer altı örtüleri
  الولية الحلس والولايا جمعه (ayn)؛ الولية شبيهة بالبرذعة تطرح على ظهر البعير؛ الجمع ولايا (jamhara)؛ الولية البرذعة؛ التي تكون تحت البرذعة؛ الجمع الولايا (sihah)؛ الولية البرذعة وجمعها الولايا؛ البرذعة التي تحت الرحل (tahdhib)
- **B012** ele geçirip hedefe ulaşma [kalıp] — bir şeyi ele geçirmek veya ona üstün gelmek · hedefe varmak veya ona önce ulaşmak
  استولى فلان على شيء إذا صار في يده؛ استولى الفرس على الغاية أي بلغها (ayn)؛ استولى على الأمد أي بلغ الغاية (sihah)؛ استولى أحدهما على الغاية إذا سبق الآخر إليها؛ استيلاؤه على الأمد أن يغلب عليه بسبقه؛ استولى فلان على مالي إذا غلب عليه (tahdhib)
- **B013** birine iyi ya da kötü şey yöneltme [kalıp] — birine iyilik yapmak veya bir şeyi ona ulaştırmak · birine iyilik veya kötülük yöneltmek
  أوليته الشيء فوليه؛ أوليته معروفا (sihah)؛ أوليت فلانا شرا وأوليته خيرا؛ أوليته معروفا أسديته إليه (tahdhib)
- **B014** aldığı fiyatla devretme — satın alınan malı bilinen aynı fiyatla başkasına devretme
  التولية في البيع أن تشتري سلعة بثمن معلوم ثم توليها رجلا آخر بذلك الثمن (tahdhib)
- **B015** küçük sürü hayvanlarını ayırma — küçük sürü hayvanlarını büyüklerinden ayırmak · yavru develeri analarından ayırıp alıştırma
  للموالاة معنى ثالث؛ والوا حواشي نعمكم من الجلة أي اعزلوا صغارها عن كبارها؛ توالي ربعي السقاب؛ تواليه أن يفصل عن أمه (tahdhib)
- **B016** taze hurmanın kurumaya dönmesi — taze hurmanın solup kurumaya başlaması · taze hurmadaki solgun kuruma rengi
  يقال للرطب إذا أخذ في الهيج قد ولى وتولى؛ توليه شهبته (tahdhib)



===== _commentary/v16/work/s087/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s087/reader_a_pilot.md)

# S087 Semantic Channel Discovery

## Parent Channels

### 1. Ordered Formation, Measure, and Governance
- Semantic invariant: An ordering agency brings entities or situations into form, assigns their measure, and directs their subsequent course.
- Surface relation: direct; 87:2-3 and 87:5 present creation, proportion, determination, guidance, and state-making, while 87:8 presents facilitation toward an intended course.
- Surprising reach: The same invariant reaches craft competence, administrative reform, sustained action, ownership, and the governance of a flock or community.

#### Subchannel A. Origination and State-Making
- Reading type: surface-primary
- Scene or process: Something is originated, made, or caused to pass into a newly specified condition.
- Active motifs: originating creation `خ ل ق:B002/m01`; making `ج ع ل:B001/m01`; state-transformation `ج ع ل:B002/m01`; willing a state `ش ي ء:B001/m01`; nurturing or repairing to completion `ر ب ب:B002/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:5 `جَعَلَهُ`; 87:7 `شَاءَ`; 87:1 and 87:15 `رَبِّ`
- Synthesis: Creation is rendered not as a bare beginning but as an ordered transition whose product is brought into a fitting state.

#### Subchannel B. Measurement, Proportion, and Fitness
- Reading type: surface-primary
- Scene or process: A form is estimated, proportioned, equalized, and tested for fitness or completion.
- Active motifs: estimation before making `خ ل ق:B001/m01`; assigned amount `ق د ر:B001/m01`; proportioning `ق د ر:B006/m01`; equality `س و ي:B001/m01`; straight or complete form `س و ي:B002/m01`; proportioned appearance `خ ل ق:B003/m01`; fitness `خ ل ق:B005/m01`; suitability `ز ك و:B004/m01`; practiced competence `ء ث ر:B011/m01`
- Ayah anchors: 87:2 `خَلَقَ فَسَوَّىٰ`; 87:3 `قَدَّرَ`; 87:14 `تَزَكَّىٰ`
- Synthesis: The sequence of creating, leveling, and determining supports a channel in which right form is inseparable from adequacy for a role.

#### Subchannel C. Planning, Oversight, and Reform
- Reading type: mixed
- Scene or process: A responsible agent plans a course, watches its execution, and corrects or sustains the governed process.
- Active motifs: planning `ق د ر:B005/m01`; monitoring `ر ع ي:B003/m01`; shepherd-governance `ر ع ي:B002/m01`; governance and reform `ء و ل:B004/m01`; beginning or persisting in action `ج ع ل:B004/m01`; watching and waiting `ب ق ي:B005/m01`; a major governing matter `ك ب ر:B002/m01`
- Ayah anchors: 87:3 `قَدَّرَ فَهَدَىٰ`; 87:4 `ٱلْمَرْعَىٰ`; 87:5 `جَعَلَهُ`; 87:12 `ٱلْكُبْرَىٰ`
- Synthesis: Determination and guidance expand into an administrative scene: a course is set, supervised, and adjusted rather than merely announced.

#### Subchannel D. Direction, Course, and Intentional Aim
- Reading type: surface-primary
- Scene or process: A traveler, process, or utterance receives a course, leading edge, orientation, or intended model.
- Active motifs: guidance `ه د ي:B001/m01`; course or manner `ه د ي:B002/m01`; leading or going in front `ه د ي:B003/m01`; approach or direction `س و ي:B004/m01`; directed aim `س و ي:B008/m01`; path, model, or intention `ق ر ء:B011/m01`; movement toward a side `ج ن ب:B005/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:6 `سَنُقْرِئُكَ`; 87:8 `نُيَسِّرُكَ لِلْيُسْرَىٰ`; 87:11 `يَتَجَنَّبُهَا`
- Synthesis: Guidance is a directed process with a front, a path, and a chosen destination; avoidance is its negative spatial counterpart.

#### Subchannel E. Capacity, Lordship, and Possession
- Reading type: latent/lexical
- Scene or process: An agent has the capacity, authority, resources, or possession needed to determine an outcome.
- Active motifs: lordship `ر ب ب:B001/m01`; capacity `ق د ر:B003/m01`; possession `ذ و و:B001/m01`; wealth or means `ي س ر:B003/m01`; retained property and dependents `ق ر ء:B013/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:3 `قَدَّرَ`; 87:8 `ٱلْيُسْرَىٰ`; 87:18 `هَٰذَا`
- Synthesis: Ordered action presupposes not only knowledge but effective capacity and a domain over which that capacity can operate.

### 2. Knowledge, Visibility, and Signs
- Semantic invariant: Information becomes available through disclosure, observation, recognition, or a perceivable sign, while concealment and impaired sight mark its limits.
- Surface relation: direct; 87:7 explicitly joins divine knowledge with what is public and what is hidden.
- Surprising reach: The channel includes tracking marks, bodily gaze, glare, faint lightning, unknown terrain, learned expertise, and landmarks.

#### Subchannel A. Knowing the Manifest and the Hidden
- Reading type: surface-primary
- Scene or process: A knower encompasses both disclosed content and what remains concealed.
- Active motifs: knowledge `ع ل م:B001/m01`; public or audible disclosure `ج ه ر:B001/m01`; visibility `ج ه ر:B002/m01`; concealment `خ ف ي:B001/m01`; unveiling or removing concealment `خ ف ي:B003/m01`; bringing something out from cover `خ ر ج:B002/m01`
- Ayah anchors: 87:4 `أَخْرَجَ`; 87:7 `يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ`
- Synthesis: Knowledge spans the full disclosure gradient, from hidden content through unveiling to public manifestation.

#### Subchannel B. Conditions and Failures of Visibility
- Reading type: latent/lexical
- Scene or process: Perception depends on cover, illumination, scale, and the eye's ability to withstand what appears.
- Active motifs: covering `خ ف ي:B002/m01`; faint lightning `خ ف ي:B004/m01`; an eye overwhelmed by magnitude `ج ه ر:B003/m01`; sun-blinded sight `ج ه ر:B004/m01`; a visible elevated figure `س م و:B002/m01`; uncertain or unknown terrain `ج ه ر:B009/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:7 `ٱلْجَهْرَ` and `يَخْفَىٰ`; 87:12 `ٱلْكُبْرَىٰ`
- Synthesis: Hiddenness can arise from cover or dimness, but also paradoxically from excessive scale or brightness.

#### Subchannel C. Watching, Gaze, and Foresight
- Reading type: latent/lexical
- Scene or process: A watcher fixes attention, tracks a course, or anticipates what lies ahead.
- Active motifs: monitoring `ر ع ي:B003/m01`; fixed gaze `ب ر ه م:B001/m01`; knowledge as reverent apprehension `خ ش ي:B002/m01`; farsight `ش ي ء:B003/m01`; following a trace `ء ث ر:B004/m01`; waiting observation `ب ق ي:B005/m01`
- Ayah anchors: 87:4 `ٱلْمَرْعَىٰ`; 87:7 `يَعْلَمُ`; 87:10 `يَخْشَىٰ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: Knowing is recast as disciplined attention: one watches, follows indications, and apprehends consequences before they arrive.

#### Subchannel D. Trace, Mark, and Landmark
- Reading type: latent/lexical
- Scene or process: An otherwise absent object or route is recognized through a residue, brand, sign, or beacon.
- Active motifs: remaining trace `ء ث ر:B003/m01`; hoof-brand `ء ث ر:B008/m01`; sign or distinguishing mark `ع ل م:B002/m01`; beacon `ن و ر:B005/m01`; body marks `ي س ر:B008/m01`; a leading marker `ه د ي:B003/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:7 `يَعْلَمُ`; 87:8 `ٱلْيُسْرَىٰ`; 87:16 `تُؤْثِرُونَ`; 87:12 `ٱلنَّارَ`
- Synthesis: Guidance can operate through sparse visible residues: a mark identifies what passed, while a beacon identifies where to go.

#### Subchannel E. Learned Knowledge and Skilled Recognition
- Reading type: latent/lexical
- Scene or process: Knowledge is stabilized as scholarship, practiced craft, or a reliable model for performance.
- Active motifs: learned knowledge `ع ل م:B001/m01`; scholar or learned person `ر ب ب:B003/m01`; practiced skill `ء ث ر:B011/m01`; poetic model `ق ر ء:B005/m01`; recognized course `ق ر ء:B011/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:6 `سَنُقْرِئُكَ`; 87:7 `يَعْلَمُ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: What is known becomes transmissible competence when it is embodied in a learned person, a practiced act, or an imitable model.

### 3. Speech, Memory, and Written Transmission
- Semantic invariant: Meaning is voiced, heard, retained, recalled, read, and carried forward in stable verbal or written form.
- Surface relation: direct; 87:6-10 center recitation, non-forgetting, and reminder, while 87:18-19 name written sheets.
- Surprising reach: The channel reaches articulation, reputation, legal records, poetic models, scribal error, grammatical notation, and deliberate withholding.

#### Subchannel A. Voice, Articulation, and Listening
- Reading type: mixed
- Scene or process: Speech becomes public through voiced articulation and is completed by an attentive listener.
- Active motifs: loud or public speech `ج ه ر:B001/m01`; tongue and articulation `ب ل ل:B006/m01`; voiced consonant `ج ه ر:B011/m01`; listening `ش ي ء:B005/m01`; attentive hearing `ر ع ي:B004/m01`; spoken mention `ذ ك ر:B004/m01`
- Ayah anchors: 87:6 `سَنُقْرِئُكَ`; 87:7 `ٱلْجَهْرَ`; 87:9 `فَذَكِّرْ`; 87:15 `ذَكَرَ`
- Synthesis: Recitation is a public vocal event whose semantic completion requires both formed sound and receptive hearing.

#### Subchannel B. Remembering, Reminding, and Forgetting
- Reading type: surface-primary
- Scene or process: Content is preserved in memory, reactivated by reminder, or lost through forgetting and neglect.
- Active motifs: memory `ذ ك ر:B003/m01`; reminder `ذ ك ر:B009/m01`; spoken recollection `ذ ك ر:B004/m01`; forgetting `ن س ي:B001/m01`; neglect `ن س ي:B002/m01`; discarded remnant `ن س ي:B003/m01`
- Ayah anchors: 87:6 `فَلَا تَنسَىٰ`; 87:9 `فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ`; 87:10 `سَيَذَّكَّرُ`; 87:15 `ذَكَرَ`
- Synthesis: Reminder opposes two kinds of loss: involuntary forgetting and practical neglect that leaves content unused.

#### Subchannel C. Reading, Sheets, and Collected Text
- Reading type: surface-primary
- Scene or process: Speech is collected into recitation and stabilized on a written surface or in a codex.
- Active motifs: reading or collecting `ق ر ء:B001/m01`; written sheet `ص ح ف:B002/m01`; codex or collected pages `ص ح ف:B003/m01`; broad writing surface `ص ح ف:B001/m01`; transmitted report `ء ث ر:B002/m01`; deed or certificate `ذ ك ر:B008/m01`
- Ayah anchors: 87:6 `سَنُقْرِئُكَ`; 87:18-19 `ٱلصُّحُفِ` and `صُحُفِ`
- Synthesis: Recitation and sheet are complementary storage forms: one collects language in performance, the other fixes it as a portable record.

#### Subchannel D. Model, Dedication, and Transmission
- Reading type: latent/lexical
- Scene or process: A verbal work is shaped by an inherited model, dedicated to a recipient, and passed on as report or reputation.
- Active motifs: poetic model `ق ر ء:B005/m01`; poetic dedication `ه د ي:B011/m01`; transmitted report `ء ث ر:B002/m01`; reputation `ذ ك ر:B007/m01`; name-based renown `س م و:B008/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:6 `سَنُقْرِئُكَ`; 87:15 `ذَكَرَ ٱسْمَ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: Transmission preserves more than wording; it also preserves a model of composition, an addressee, and a public afterlife.

#### Subchannel E. Misreading, Fabrication, and Scribal Form
- Reading type: latent/lexical
- Scene or process: Written or spoken form can be corrupted through misreading, invention, or a small formal feature that changes analysis.
- Active motifs: textual misreading `ص ح ف:B005/m01`; fabricated speech `خ ل ق:B007/m01`; grammatical exit-alif `خ ر ج:B011/m01`; a letter as an object `ه ا ء:B006/m01`; interrogative substitution `ه ا ء:B004/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:4 `أَخْرَجَ`; 87:18-19 `ٱلصُّحُفِ`; 87:18 `هَٰذَا`
- Synthesis: The written channel contains its own failure modes: content may be invented, a text misread, or interpretation redirected by a minimal graphic or grammatical unit.

#### Subchannel F. Holding, Delay, and Reserved Utterance
- Reading type: latent/lexical
- Scene or process: A reading, response, or piece of information is held back until an appointed occasion.
- Active motifs: delaying or holding `ق ر ء:B004/m01`; holding in reserve `ق ر ء:B010/m01`; postponement `ن س ي:B005/m01`; concealed content `خ ف ي:B001/m01`; retained remainder `ب ق ي:B004/m01`
- Ayah anchors: 87:6 `سَنُقْرِئُكَ فَلَا تَنسَىٰ`; 87:7 `يَخْفَىٰ`; 87:17 `أَبْقَىٰ`
- Synthesis: Retention can be active rather than deficient: content may remain hidden or delayed precisely because it is being preserved.

### 4. Naming, Reference, and Grammatical Relation
- Semantic invariant: Language identifies entities, points to them, relates them to other entities, and frames how an utterance is received.
- Surface relation: direct; 87:1 and 87:15 foreground the name, while 87:18 uses a demonstrative expression.
- Surprising reach: The channel includes reputation, relational pronouns, particles, calls for attention, responses, exclamations, and formal letter names.

#### Subchannel A. Name, Appellation, and Reputation
- Reading type: surface-primary
- Scene or process: An entity is made present through its name, while repeated mention builds a public reputation.
- Active motifs: name or appellation `س م و:B005/m01`; reputation `س م و:B008/m01`; public renown `ذ ك ر:B007/m01`; spoken mention `ذ ك ر:B004/m01`; elevated distinction `س م و:B001/m01`
- Ayah anchors: 87:1 and 87:15 `ٱسْمَ`; 87:9-10 and 87:15 forms of `ذ ك ر`
- Synthesis: Naming is both reference and elevation: it singles out an entity and allows its mention to persist socially.

#### Subchannel B. Deixis, Relation, and Interrogation
- Reading type: mixed
- Scene or process: A speaker points to an entity, asks after it, or defines it through a relational link.
- Active motifs: demonstrative reference `ذ و و:B003/m01`; relative relation `ذ و و:B002/m01`; interrogative or relative use `ذ و و:B004/m01`; interrogative substitute `ه ا ء:B004/m01`; circumstantial or state frame `ء و ل:B007/m01`
- Ayah anchors: 87:18 `هَٰذَا`; 87:16-17 the contrasted relation between `ٱلدُّنْيَا` and `ٱلْءَاخِرَةُ`
- Synthesis: Deixis anchors discourse in a present object, while relative and circumstantial forms situate that object within a wider relation or state.

#### Subchannel C. Particles, Prepositions, and Letters
- Reading type: latent/lexical
- Scene or process: Small grammatical units redirect the relation among larger meanings.
- Active motifs: contrastive particle `ب ل ل:B008/m01`; approximating particle `ر ب ب:B015/m01`; preposition of superposition `ع ل و:B012/m01`; letter-name `ه ا ء:B006/m01`; grammatical exit-alif `خ ر ج:B011/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:4 `أَخْرَجَ`; 87:16 `بَلْ`; 87:1 and 87:15 `رَبِّ`; 87:18 `هَٰذَا`
- Synthesis: The surah's semantic turns can be mirrored at the smallest grammatical scale, where a particle or letter establishes contrast, height, approximation, or syntactic release.

#### Subchannel D. Summons, Offer, and Response
- Reading type: latent/lexical
- Scene or process: One party calls attention, presents something, and receives an answering acknowledgment.
- Active motifs: take or receive this `ه ا ء:B001/m01`; attention-call `ه ا ء:B002/m01`; response `ه ا ء:B003/m01`; greeting `ق ر ء:B006/m01`; spoken summons `ذ ك ر:B004/m01`
- Ayah anchors: 87:6 `سَنُقْرِئُكَ`; 87:9 `فَذَكِّرْ`; 87:18 `هَٰذَا`
- Synthesis: Reference becomes interpersonal when pointing is joined to an offer, a summons, and a response.

#### Subchannel E. Exclamation, Admiration, and Regret
- Reading type: latent/lexical
- Scene or process: An encounter exceeds neutral description and erupts as admiration or retrospective regret.
- Active motifs: admiration `ش ي ء:B004/m01`; exclamation or regret `ش ي ء:B007/m01`; exclamation or regret variant `ش ي ء:B009/m01`; magnifying admiration `ك ب ر:B003/m01`
- Ayah anchors: 87:7 `شَاءَ`; 87:12 `ٱلْكُبْرَىٰ`
- Synthesis: The will-root's lexical margins turn volition into affective speech, while magnitude supplies the trigger for astonishment.

### 5. Worship, Praise, and Sacred Address
- Semantic invariant: A worshipper names, praises, remembers, blesses, or approaches the sacred through ordered speech and embodied observance.
- Surface relation: direct; 87:1 commands glorification, and 87:14-15 join purification, naming, remembrance, and prayer.
- Surprising reach: The channel reaches exoneration, greeting, beads, sanctuaries, offerings, predawn food, and a lexical hinge between prayer and fire.

#### Subchannel A. Glorification, Remembrance, and Prayer
- Reading type: surface-primary
- Scene or process: Sacred address moves from glorification and naming to remembered praise and formal prayer.
- Active motifs: worshipful glorification `س ب ح:B001/m01`; formal prayer `ص ل و:B003/m01`; prayer variant `ص ل ي:B001/m01`; spoken remembrance `ذ ك ر:B004/m01`; deity and worship `ء ل ه:B001/m01`; divine name, oath, or call `ء ل ه:B002/m01`
- Ayah anchors: 87:1 `سَبِّحِ ٱسْمَ رَبِّكَ`; 87:15 `ذَكَرَ ٱسْمَ رَبِّهِ فَصَلَّىٰ`; 87:7 `ٱللَّهُ`
- Synthesis: Sacred practice forms a verbal sequence: identify the addressee, declare transcendence, retain the name, and enact prayer.

#### Subchannel B. Exoneration, Elevation, and Honor
- Reading type: mixed
- Scene or process: Praise removes deficiency from its object and affirms elevated rank or honor.
- Active motifs: exoneration `س ب ح:B002/m01`; elevation `ع ل و:B001/m01`; honor `ع ل و:B002/m01`; elevated naming `س م و:B001/m01`; rank `ك ب ر:B005/m01`; high position `ع ل و:B005/m01`
- Ayah anchors: 87:1 `سَبِّحِ ... ٱلْأَعْلَى`; 87:12 `ٱلْكُبْرَىٰ`; 87:15 `ٱسْمَ رَبِّهِ`
- Synthesis: Glorification combines a negative movement, clearing defect, with a positive movement, affirming height and rank.

#### Subchannel C. Blessing, Peace, and Greeting
- Reading type: latent/lexical
- Scene or process: Sacred or social speech confers favor and establishes peaceful recognition between parties.
- Active motifs: blessing or praise `ص ل و:B002/m01`; blessing variant `ص ل ي:B002/m01`; blessing within a need or knot `ر ب ب:B016/m03`; greeting `ق ر ء:B006/m01`; salutation `ح ي ي:B007/m01`; answer to a call `ه ا ء:B003/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:6 `سَنُقْرِئُكَ`; 87:13 `يَحْيَىٰ`; 87:15 `فَصَلَّىٰ`
- Synthesis: Blessing and greeting share a performative structure: words do not merely describe well-being but enact a relation of favor or peace.

#### Subchannel D. Worship Place, Gift, and Offering
- Reading type: latent/lexical
- Scene or process: Worship is localized at a designated place and accompanied by a gift or consecrated offering.
- Active motifs: worship place `ص ل و:B007/m01`; worship-place variant `ص ل ي:B008/m01`; gift `ه د ي:B004/m01`; ritual offering `ه د ي:B005/m01`; protected refuge `ه د ي:B007/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:15 `فَصَلَّىٰ`
- Synthesis: The abstract course of guidance becomes a ritual itinerary involving destination, protected approach, and transferred offering.

#### Subchannel E. Counted Remembrance and Predawn Observance
- Reading type: latent/lexical
- Scene or process: Devotion is paced through counted tokens and a meal or observance before daybreak.
- Active motifs: remembrance beads `س ب ح:B006/m01`; predawn meal `ف ل ح:B006/m01`; verbal reminder `ذ ك ر:B009/m01`; beginning of action `ج ع ل:B004/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:5 `جَعَلَهُ`; 87:9 `ٱلذِّكْرَىٰ`; 87:14 `أَفْلَحَ`
- Synthesis: Repetition and predawn timing turn remembrance into a measured devotional routine.

#### Subchannel F. Prayer and Fire Lexical Hinge
- Reading type: mixed
- Scene or process: Closely neighboring lexical branches hold prayer, blessing, fire, and roasting in a charged relation without collapsing their distinct scenes.
- Active motifs: prayer `ص ل ي:B001/m01`; fire `ص ل ي:B003/m01`; roasting at fire `ص ل ي:B004/m01`; prayer `ص ل و:B003/m01`; fire or heat `ص ل و:B001/m01`; blaze `ن و ر:B002/m01`
- Ayah anchors: 87:12 `يَصْلَى ٱلنَّارَ`; 87:15 `فَصَلَّىٰ`
- Synthesis: The surah places punitive burning and worshipful prayer close enough to activate a sharp lexical contrast between two forms of approach.

### 6. Goodness, Purification, and Moral Return
- Semantic invariant: A person or condition improves through benefit, selection, purification, restraint, and orientation toward an enduring good.
- Surface relation: direct; 87:9 links reminder to benefit, 87:14 names purification and success, and 87:16-17 contrast the lower life with the better and more lasting hereafter.
- Surprising reach: The channel reaches generosity, fitness, repentance, calm submission, preference, and admiration.

#### Subchannel A. Benefit, Welfare, and Abundant Good
- Reading type: surface-primary
- Scene or process: An intervention produces practical benefit, restored welfare, or an abundance that can be directed toward good.
- Active motifs: benefit `ن ف ع:B001/m01`; welfare or benefaction `ب ل ل:B002/m01`; beneficial good `ح ي ي:B013/m01`; abundant good or evil `ج ن ب:B009/m01`; generosity and gift `خ ي ر:B005/m01`
- Ayah anchors: 87:9 `نَّفَعَتِ`; 87:13 `يَحْيَىٰ`; 87:17 `خَيْرٌ`
- Synthesis: Benefit is not merely possession of good; it is good becoming effective in a recipient's condition.

#### Subchannel B. Selection, Purity, and Success
- Reading type: surface-primary
- Scene or process: A person distinguishes the better option, removes impurity, and reaches a flourishing outcome.
- Active motifs: good `خ ي ر:B001/m01`; virtue or selection `خ ي ر:B002/m01`; seeking good or choosing `خ ي ر:B003/m01`; preference and selection `ء ث ر:B005/m01`; purification `ز ك و:B002/m01`; growth `ز ك و:B001/m01`; success `ف ل ح:B005/m01`
- Ayah anchors: 87:14 `أَفْلَحَ مَن تَزَكَّىٰ`; 87:16 `تُؤْثِرُونَ`; 87:17 `خَيْرٌ`
- Synthesis: Purification is presented as discriminating growth: the better is chosen, cultivated, and realized as success.

#### Subchannel C. Restraint, Reverence, and Submission
- Reading type: mixed
- Scene or process: Awareness of consequence restrains action and produces reverence, repentance, or calm yielding.
- Active motifs: reverent fear `خ ش ي:B001/m01`; restraint or repentance `ر ع ي:B005/m01`; calm bearing `ه د ي:B010/m01`; submission `م و ت:B013/m01`; preserved covenant `ر ع ي:B006/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:4 `ٱلْمَرْعَىٰ`; 87:10 `يَخْشَىٰ`; 87:13 `يَمُوتُ`
- Synthesis: Moral responsiveness appears as controlled motion: one stops, turns, yields, and remains faithful to a binding course.

#### Subchannel D. The Lower Life and the Enduring Outcome
- Reading type: surface-primary
- Scene or process: Immediate nearness and later outcome compete for preference, with persistence marking the superior horizon.
- Active motifs: the lower or near world `د ن و:B002/m01`; later or other `ء خ ر:B001/m01`; outcome or return `ء و ل:B002/m01`; persistence `ب ق ي:B001/m01`; precedence or preference `ء ث ر:B001/m01`; good `خ ي ر:B001/m01`
- Ayah anchors: 87:16 `تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا`; 87:17 `وَٱلْءَاخِرَةُ خَيْرٌ وَأَبْقَىٰ`
- Synthesis: The moral contrast is temporal and evaluative at once: what is nearest is not necessarily what deserves precedence.

#### Subchannel E. Generosity, Favor, and Reciprocal Improvement
- Reading type: latent/lexical
- Scene or process: Goods, favor, or labor pass between parties and improve the recipient's state.
- Active motifs: generosity or gift `خ ي ر:B005/m01`; benefaction `ب ل ل:B002/m01`; gift `ه د ي:B004/m01`; wage `ج ع ل:B005/m01`; benefit `ن ف ع:B001/m01`; recovery `ب ل ل:B003/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:5 `جَعَلَهُ`; 87:9 `نَّفَعَتِ`; 87:17 `خَيْرٌ`
- Synthesis: Goodness becomes reciprocal and material when guidance, labor, payment, and recovery form one exchange of improvement.

#### Subchannel F. Admiration and Inward Magnification
- Reading type: latent/lexical
- Scene or process: Perceived goodness, scale, or distinction becomes affectively enlarged in the observer.
- Active motifs: admiration `ش ي ء:B004/m01`; magnifying admiration `ك ب ر:B003/m01`; honor `ع ل و:B002/m01`; reputation `س م و:B008/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:7 `شَاءَ`; 87:12 `ٱلْكُبْرَىٰ`; 87:15 `ٱسْمَ`
- Synthesis: Evaluation can move inward, where worth or magnitude is registered as admiration before it becomes explicit choice.

### 7. Hardship, Contest, and Corruption
- Semantic invariant: Difficulty becomes morally charged when it provokes struggle, monopolization, pride, deception, or refusal to yield.
- Surface relation: direct; 87:8 contrasts ease with difficulty by implication, and 87:11-13 portray wretched avoidance and the greatest fire.
- Surprising reach: The channel includes rivalry, victory, endurance, rebellious outliers, obstinate contention, deceptive sale, and feigned submission.

#### Subchannel A. Difficulty, Burden, and Ease
- Reading type: mixed
- Scene or process: An agent confronts a constricted course, limited means, or a heavy obligation, against which facilitation appears.
- Active motifs: ease `ي س ر:B001/m01`; hardship `ش ق و:B002/m01`; hardship variant `ش ق ي:B002/m01`; burden `ك ب ر:B010/m01`; scarcity `ق د ر:B004/m01`; small amount `ي س ر:B002/m01`
- Ayah anchors: 87:3 `قَدَّرَ`; 87:8 `نُيَسِّرُكَ لِلْيُسْرَىٰ`; 87:11 `ٱلْأَشْقَىٰ`; 87:12 `ٱلْكُبْرَىٰ`
- Synthesis: Ease is not mere comfort but the opening of a course otherwise constricted by scarcity, burden, or hardship.

#### Subchannel B. Wretchedness as Failed Flourishing
- Reading type: surface-primary
- Scene or process: A person avoids corrective remembrance and enters a condition opposed to purification and success.
- Active motifs: wretchedness `ش ق ي:B001/m01`; hardship `ش ق و:B002/m01`; success `ف ل ح:B005/m01`; purification `ز ك و:B002/m01`; avoidance by separation `ج ن ب:B003/m01`
- Ayah anchors: 87:11 `يَتَجَنَّبُهَا ٱلْأَشْقَى`; 87:14 `أَفْلَحَ مَن تَزَكَّىٰ`
- Synthesis: Wretchedness is the negative image of flourishing: refusal of reminder becomes separation from the process that purifies.

#### Subchannel C. Rivalry, Endurance, and Overcoming
- Reading type: latent/lexical
- Scene or process: Parties compete for precedence, persist under strain, and attempt to overcome or monopolize the field.
- Active motifs: endurance or contest `ش ق و:B003/m01`; endurance or contest variant `ش ق ي:B003/m01`; overcoming `ك ب ر:B011/m01`; victory `ب ل ل:B004/m01`; rivalry `س م و:B007/m01`; monopolizing possession `ء ث ر:B006/m01`
- Ayah anchors: 87:1 `ٱسْمَ`; 87:11 `ٱلْأَشْقَىٰ`; 87:12 `ٱلْكُبْرَىٰ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: Preference hardens into contest when several agents seek the same precedence and endurance becomes a means of domination.

#### Subchannel D. Pride, Obstinacy, and Rebellion
- Reading type: latent/lexical
- Scene or process: An agent magnifies the self, clings to a position, and departs from an ordered course.
- Active motifs: pride `ك ب ر:B006/m01`; obstinacy `ج ع ل:B012/m02`; obstinate contention `ب ل ل:B005/m01`; rebellion `خ ر ج:B006/m02`; domination `ع ل و:B004/m01`; clinging `ب ل ل:B004/m02`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:4 `أَخْرَجَ`; 87:5 `جَعَلَهُ`; 87:12 `ٱلْكُبْرَىٰ`; 87:16 `بَلْ`
- Synthesis: Corruption begins as a distortion of height and firmness: elevation becomes pride, persistence becomes clinging, and departure becomes rebellion.

#### Subchannel E. Fabrication, False Submission, and Deceptive Exchange
- Reading type: latent/lexical
- Scene or process: Appearance and declared intent are manipulated to mislead another party.
- Active motifs: fabricated speech `خ ل ق:B007/m01`; feigned death or submission `م و ت:B011/m01`; deceptive sale `ف ل ح:B007/m01`; disfigured appearance `ش ي ء:B002/m01`; deviation from a class or norm `خ ر ج:B006/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:4 `أَخْرَجَ`; 87:7 `شَاءَ`; 87:13 `يَمُوتُ`; 87:14 `أَفْلَحَ`
- Synthesis: Deception exploits the gap between visible state and actual condition, whether by invented speech, altered appearance, simulated surrender, or corrupt exchange.

### 8. Life, Death, and Preservation
- Semantic invariant: Vitality can be granted, diminished, suspended, spared, extinguished, or retained as a remainder.
- Surface relation: direct; 87:13 explicitly denies both death and life to the sufferer, while 87:16 names worldly life and 87:17 names persistence.
- Surprising reach: The channel reaches coma, dullness, dormancy, material wear, epidemic, carrion, recovery, stored reserves, and game verification.

#### Subchannel A. Vitality and Death
- Reading type: surface-primary
- Scene or process: A living condition is opposed to death while intermediate states unsettle the binary.
- Active motifs: animal or living being `ح ي ي:B003/m01`; life `ح ي ي:B013/m01`; death `م و ت:B001/m01`; weakening toward death `م و ت:B002/m01`
- Ayah anchors: 87:13 `لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ`; 87:16 `ٱلْحَيَوٰةَ`
- Synthesis: The explicit negation of both poles opens a channel for conditions in which vitality persists without flourishing and death remains incomplete.

#### Subchannel B. Suspended and Diminished States
- Reading type: mixed
- Scene or process: Agency or vitality falls into a deathlike interval without reaching final extinction.
- Active motifs: deathlike circumstance `م و ت:B008/m01`; seizure or coma `م و ت:B009/m01`; dullness of mind `م و ت:B006/m01`; dormancy `م و ت:B012/m01`; material wear `م و ت:B012/m02`; discarded or forgotten residue `ن س ي:B003/m01`
- Ayah anchors: 87:5 `غُثَاءً أَحْوَىٰ`; 87:6 `تَنسَىٰ`; 87:13 `لَا يَمُوتُ ... وَلَا يَحْيَىٰ`
- Synthesis: The neither-dead-nor-living state generalizes to suspended consciousness, dormant matter, and residues that remain after active use.

#### Subchannel C. Sparing Life and Preserving Bonds
- Reading type: latent/lexical
- Scene or process: Destruction is withheld so that a life, obligation, or protected relation continues.
- Active motifs: sparing life `ح ي ي:B006/m01`; sparing or leaving a remainder `ب ق ي:B003/m01`; preserving a covenant `ر ع ي:B006/m01`; protected refuge or captive `ه د ي:B007/m01`; remaining bond `ب ق ي:B001/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:4 `ٱلْمَرْعَىٰ`; 87:13 `يَحْيَىٰ`; 87:17 `أَبْقَىٰ`
- Synthesis: Preservation joins biological survival to social fidelity: to spare is to allow both life and binding relation to continue.

#### Subchannel D. Remainder, Reserve, and Controlled Holding
- Reading type: mixed
- Scene or process: A portion survives immediate consumption or release and is deliberately kept for later.
- Active motifs: remainder `ب ق ي:B002/m01`; reserve `ب ق ي:B004/m01`; persistence `ب ق ي:B001/m01`; holding in reserve `ق ر ء:B010/m01`; delayed holding `ق ر ء:B004/m01`; watchful waiting `ب ق ي:B005/m01`
- Ayah anchors: 87:6 `سَنُقْرِئُكَ`; 87:17 `أَبْقَىٰ`
- Synthesis: Persistence is made concrete as inventory and timing: something remains because it is withheld, watched, and released later.

#### Subchannel E. Outbreak, Carrion, and Biological Loss
- Reading type: latent/lexical
- Scene or process: Vital systems fail collectively or leave biologically charged remains.
- Active motifs: outbreak `م و ت:B004/m01`; epidemic `ق ر ء:B008/m01`; carrion `م و ت:B007/m01`; offspring loss `م و ت:B005/m01`; dead land `م و ت:B003/m01`
- Ayah anchors: 87:4-5 the emergence and death of pasture; 87:6 `سَنُقْرِئُكَ`; 87:13 `يَمُوتُ`
- Synthesis: Death expands from an individual endpoint into contagion, reproductive loss, carrion, and ecological failure.

#### Subchannel F. Collapse and Recovery
- Reading type: latent/lexical
- Scene or process: A weakened person or system returns from incapacity toward health and effective action.
- Active motifs: recovery `ب ل ل:B003/m01`; health recovery `ع ل و:B011/m01`; beneficial restoration `ح ي ي:B013/m01`; weakening `م و ت:B002/m01`; supported gait `ه د ي:B008/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:3 `هَدَىٰ`; 87:13 `يَحْيَىٰ`; 87:16 `بَلْ`
- Synthesis: Recovery reverses diminished life by restoring height, movement, and practical benefit.

#### Subchannel G. Risked Life and Verified Death
- Reading type: latent/lexical
- Scene or process: A person risks death through reckless commitment, or a hunter tests whether an animal is truly dead.
- Active motifs: reckless devotion to the point of death `م و ت:B010/m01`; verification of game death `م و ت:B014/m01`; hunting `س م و:B006/m01`; animal lure `خ ي ر:B006/m01`; trap `ص ل ي:B005/m01`
- Ayah anchors: 87:1 and 87:15 `ٱسْمَ`; 87:13 `يَمُوتُ`; 87:17 `خَيْرٌ`
- Synthesis: Death becomes an operational threshold in scenes of dangerous commitment and lawful or practical verification.

### 9. Priority, Delay, and Cyclical Time
- Semantic invariant: Events and values are organized by beginning, precedence, succession, postponement, recurrence, maturity, and final outcome.
- Surface relation: direct; 87:16-19 contrast present preference with the later life and explicitly invoke earlier sheets.
- Surprising reach: The channel reaches waiting, delayed recitation, race order, lunar timing, old age, predawn, seasonal rut, and curdling as an end-state.

#### Subchannel A. Beginning, Firstness, and Precedence
- Reading type: surface-primary
- Scene or process: A sequence opens with a first term that may also claim evaluative priority.
- Active motifs: beginning or firstness `ء و ل:B001/m01`; precedence `ء ث ر:B001/m01`; choosing precedence `ء ث ر:B001/m02`; beginning an action `ج ع ل:B004/m01`
- Ayah anchors: 87:5 `جَعَلَهُ`; 87:16 `تُؤْثِرُونَ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Temporal firstness and chosen priority overlap but remain distinguishable: what comes first may be inherited, while what receives precedence is selected.

#### Subchannel B. Later Outcome, Following, and the Rear
- Reading type: mixed
- Scene or process: A later term follows what precedes it and may reveal the sequence's true outcome.
- Active motifs: later or other `ء خ ر:B001/m01`; outcome or return `ء و ل:B002/m01`; following `ء ث ر:B004/m01`; rear position `ء خ ر:B003/m01`; second place in a race `ص ل و:B006/m01`; race-second variant `ص ل ي:B007/m01`
- Ayah anchors: 87:16 `تُؤْثِرُونَ`; 87:17 `ٱلْءَاخِرَةُ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: What follows can be spatially behind yet evaluatively superior, making sequence order an unreliable guide to final worth.

#### Subchannel C. Delay, Postponement, and Staying
- Reading type: latent/lexical
- Scene or process: An event, reading, or departure is deferred while a person or object remains in place.
- Active motifs: delay `ء خ ر:B002/m01`; postponement `ن س ي:B005/m01`; delayed holding `ق ر ء:B004/m01`; staying `ر ب ب:B007/m01`; watchful waiting `ب ق ي:B005/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:6 `سَنُقْرِئُكَ فَلَا تَنسَىٰ`; 87:17 `أَبْقَىٰ`
- Synthesis: Delay is an active temporal arrangement in which retention, residence, and watchfulness keep an outcome open.

#### Subchannel D. Cycle, Maturity, and Recurrence
- Reading type: latent/lexical
- Scene or process: Time is registered through bodily, lunar, reproductive, or ritual cycles.
- Active motifs: recurring cycle `ق ر ء:B002/m01`; youth reaching maturity `س و ي:B005/m01`; old age `ك ب ر:B004/m01`; full-moon night `س و ي:B012/m01`; predawn meal `ف ل ح:B006/m01`; camel rut `ق ر ء:B009/m01`; high or full day `ك ب ر:B013/m01`
- Ayah anchors: 87:2 `سَوَّىٰ`; 87:6 `سَنُقْرِئُكَ`; 87:12 `ٱلْكُبْرَىٰ`; 87:14 `أَفْلَحَ`
- Synthesis: Recurrence is embodied in maturation, aging, rut, lunar fullness, and the daily threshold before dawn.

#### Subchannel E. End-State and Persistence
- Reading type: mixed
- Scene or process: A process culminates in a settled result that either persists or decays into residue.
- Active motifs: final outcome `ء و ل:B002/m01`; curdling or settled end-state `ء و ل:B005/m01`; persistence `ب ق ي:B001/m01`; dried pasture `غ ث و:B002/m01`; remaining residue `ب ق ي:B002/m01`
- Ayah anchors: 87:4-5 pasture becoming dark stubble; 87:17 `أَبْقَىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: A final state can be durable or depleted; persistence is therefore distinguished from mere lateness or residue.

### 10. Elevation, Proximity, and Measured Space
- Semantic invariant: Bodies, objects, and routes are located through height, nearness, side relation, scale, direction, and terrain.
- Surface relation: direct; 87:1 names the highest, 87:11 describes avoidance, 87:12 names the greatest, and 87:16 names the lower or nearer life.
- Surprising reach: The channel reaches overhead loads, body sides, plains, hills, mountain spurs, leftward movement, place-names, and downward thrusts.

#### Subchannel A. Height, Superposition, and Descent
- Reading type: surface-primary
- Scene or process: An entity is raised above another, bears something overhead, or bends downward toward a middle point.
- Active motifs: elevation `ع ل و:B001/m01`; being above `ع ل و:B005/m01`; overhead load `ع ل و:B008/m01`; raised implements `ع ل و:B009/m01`; tallness `ع ل و:B010/m01`; sky `س م و:B004/m01`; upper part bending toward the middle `د ن و:B005/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:16 `ٱلدُّنْيَا`
- Synthesis: Height is not a single point but a vertical relation among what is above, what is carried overhead, and what descends toward a center.

#### Subchannel B. Nearness, Side, Separation, and Rear
- Reading type: mixed
- Scene or process: A figure approaches, occupies a side or rear position, or withdraws to create distance.
- Active motifs: proximity `د ن و:B001/m01`; bodily side `ج ن ب:B001/m01`; separation `ج ن ب:B003/m01`; movement toward a side `ج ن ب:B005/m01`; rear position `ء خ ر:B003/m01`; back or side `ص ل و:B005/m01`; back variant `ص ل ي:B006/m01`
- Ayah anchors: 87:11 `يَتَجَنَّبُهَا`; 87:15 `فَصَلَّىٰ`; 87:16 `ٱلدُّنْيَا`; 87:17 `ٱلْءَاخِرَةُ`
- Synthesis: Near, side, rear, and apart form a relational geometry for approach and avoidance.

#### Subchannel C. Magnitude, Scarcity, and the Just Middle
- Reading type: mixed
- Scene or process: An amount or size is compared against a limited supply, an equivalent, or a balanced midpoint.
- Active motifs: size or magnitude `ك ب ر:B001/m01`; assigned amount `ق د ر:B001/m01`; scarcity `ق د ر:B004/m01`; small amount `ي س ر:B002/m01`; middle or just position `س و ي:B006/m01`; equivalent wealth `س و ي:B013/m01`
- Ayah anchors: 87:2 `سَوَّىٰ`; 87:3 `قَدَّرَ`; 87:8 `ٱلْيُسْرَىٰ`; 87:12 `ٱلْكُبْرَىٰ`
- Synthesis: Scale is relational: greatness, smallness, scarcity, equivalence, and the middle all emerge through comparison.

#### Subchannel D. Plain, Hill, and Uncertain Terrain
- Reading type: latent/lexical
- Scene or process: Movement crosses an open plain, a broad hill, or terrain whose features are not yet known.
- Active motifs: broad smooth plain `س و ي:B009/m01`; broad hill `ج ه ر:B007/m01`; unknown terrain `ج ه ر:B009/m01`; open expanse `ص ح ف:B001/m01`; roaming across land `س ب ح:B005/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:2 `سَوَّىٰ`; 87:7 `ٱلْجَهْرَ`; 87:18 `ٱلصُّحُفِ`
- Synthesis: The visual field alternates between legible openness and uncertain ground, making terrain itself a problem of disclosure.

#### Subchannel E. Mountain Ridge, Spur, and Length
- Reading type: latent/lexical
- Scene or process: A long raised form presents as a ridge, projecting spur, or extended neck.
- Active motifs: mountain ridge `ش ق و:B004/m01`; mountain spur `ش ق ي:B004/m01`; tall or long form `ع ل و:B010/m01`; long horse neck `خ ر ج:B013/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:4 `أَخْرَجَ`; 87:11 `ٱلْأَشْقَىٰ`
- Synthesis: Hardship-root branches unexpectedly become topography, converging with height and bodily extension in one projecting form.

#### Subchannel F. Directional Geometry and Named Place
- Reading type: latent/lexical
- Scene or process: Motion is resolved by orientation toward, away from, leftward, downward, or toward a named destination.
- Active motifs: approach or direction `س و ي:B004/m01`; directed relation `س و ي:B008/m01`; left side `ي س ر:B004/m01`; downward twist `ي س ر:B009/m01`; face-level thrust `ي س ر:B009/m02`; place-name `ي س ر:B010/m01`; place-name `ج ع ل:B011/m01`; named place `س ب ح:B008/m01`
- Ayah anchors: 87:2 `سَوَّىٰ`; 87:5 `جَعَلَهُ`; 87:8 `ٱلْيُسْرَىٰ`
- Synthesis: Direction is both vector and destination: bodily orientation acquires stability when a route terminates in a named place.

### 11. Ecological Renewal and Decay
- Semantic invariant: Land and vegetation move through emergence, watering, growth, grazing, drying, and decomposition.
- Surface relation: direct; 87:4-5 compress the full transformation from emerging pasture to dark stubble.
- Surprising reach: The channel includes sky openings, rainclouds, wells, basins, young palms, flowers, flotsam, farmland, and the dryness of both vegetation and terrain.

#### Subchannel A. Sky, Cloud, Wind, and Reviving Rain
- Reading type: mixed
- Scene or process: Water-bearing conditions gather overhead, open, and descend to restore vitality to land.
- Active motifs: sky `س م و:B004/m01`; raincloud `ر ب ب:B008/m01`; cloud or sky opening `خ ر ج:B005/m01`; south wind `ج ن ب:B006/m01`; rain-revived land `ح ي ي:B002/m01`; light `ن و ر:B001/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:4 `أَخْرَجَ ٱلْمَرْعَىٰ`; 87:13 `يَحْيَىٰ`
- Synthesis: Emergent pasture is placed within a larger atmospheric cycle in which height, opening, wind, light, and rain reactivate the earth.

#### Subchannel B. Water, Basin, Well, and Moisture
- Reading type: latent/lexical
- Scene or process: Water is abundant, collected, uncovered, or retained as moisture in a bounded place.
- Active motifs: abundant water `ر ب ب:B013/m01`; water basins `ح و ي:B008/m01`; basin `ع ل م:B005/m01`; clearing a well `ج ه ر:B008/m01`; water pit or well `خ ل ق:B011/m01`; moisture `ب ل ل:B001/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:2 `خَلَقَ`; 87:5 `أَحْوَىٰ`; 87:7 `ٱلْجَهْرَ`; 87:16 `بَلْ`
- Synthesis: Water becomes ecologically effective through containment and access: it must collect, remain, or be cleared into view.

#### Subchannel C. Pasture, Herbage, and Grazing Plants
- Reading type: surface-primary
- Scene or process: Vegetation emerges as pasture and is maintained through grazing, cultivation, or custodial care.
- Active motifs: pasture `ر ع ي:B001/m01`; plant `ر ب ب:B012/m01`; middle-growing plant `ج ن ب:B010/m01`; plant or herbage `ح و ي:B007/m01`; grazing grass `ص ل و:B009/m01`; grazing-grass variant `ص ل ي:B010/m01`; farmer `ف ل ح:B003/m01`
- Ayah anchors: 87:4 `أَخْرَجَ ٱلْمَرْعَىٰ`; 87:5 `جَعَلَهُ غُثَاءً`; 87:14 `أَفْلَحَ`
- Synthesis: Pasture is a relational ecology involving plant growth, animal use, human cultivation, and eventual depletion.

#### Subchannel D. Dryness, Stubble, Flotsam, and Refuse
- Reading type: surface-primary
- Scene or process: Once-living material dries, darkens, fragments, and becomes floating or discarded residue.
- Active motifs: flotsam or surface refuse `غ ث و:B001/m01`; dried pasture `غ ث و:B002/m01`; worthless refuse `غ ث و:B004/m01`; dryness `خ ش ي:B004/m01`; dead land `م و ت:B003/m01`; discarded remnant `ن س ي:B003/m01`
- Ayah anchors: 87:5 `غُثَاءً أَحْوَىٰ`; 87:6 `تَنسَىٰ`; 87:10 `يَخْشَىٰ`; 87:13 `يَمُوتُ`
- Synthesis: Decay is a loss of cohesion and value: the green field becomes dry matter, then residue liable to drift or discard.

#### Subchannel E. Young Palms and Vegetal Increase
- Reading type: latent/lexical
- Scene or process: New shoots emerge in clustered, still-developing forms and proceed toward increase.
- Active motifs: dwarf or young palms `ج ع ل:B006/m01`; young palms `ش ي ء:B006/m01`; young-palms variant `ش ي ء:B008/m01`; vegetal growth `ز ك و:B001/m01`; continuing remainder `ب ق ي:B001/m01`
- Ayah anchors: 87:5 `جَعَلَهُ`; 87:7 `شَاءَ`; 87:14 `تَزَكَّىٰ`; 87:17 `أَبْقَىٰ`
- Synthesis: The emergence of young palms supplies a concrete model for purification as increase and for persistence as renewed growth.

#### Subchannel F. Blossom, Flower, and Visible Renewal
- Reading type: latent/lexical
- Scene or process: A plant's inward vitality becomes externally visible in bloom.
- Active motifs: tree bloom `ب ر ه م:B002/m01`; blossom `ن و ر:B004/m01`; growth `ز ك و:B001/m01`; visible emergence `خ ر ج:B001/m01`
- Ayah anchors: 87:4 `أَخْرَجَ`; 87:12 `ٱلنَّارَ`; 87:14 `تَزَكَّىٰ`; 87:19 `إِبْرَٰهِيمَ`
- Synthesis: Bloom joins life, color, and disclosure: growth becomes readable when it breaks outward into flower.

#### Subchannel G. Cultivation, Herding, and Inhabited Terrain
- Reading type: mixed
- Scene or process: People and animals occupy a landscape through farming, grazing, roaming, and local knowledge.
- Active motifs: farmer `ف ل ح:B003/m01`; shepherd-governance `ر ع ي:B002/m01`; herd `ر ب ب:B014/m01`; roaming for livelihood `س ب ح:B005/m01`; unknown terrain `ج ه ر:B009/m01`; named place `س ب ح:B008/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:4 `ٱلْمَرْعَىٰ`; 87:7 `ٱلْجَهْرَ`; 87:14 `أَفْلَحَ`
- Synthesis: Land becomes inhabited space when cultivation and herding are joined to mobility, place knowledge, and livelihood.

### 12. Dairy, Food, and Material Thickening
- Semantic invariant: Organic and mineral materials are collected, diluted, thickened, heated, ground, served, or used as coatings.
- Surface relation: indirect; 87:4-5 supply pasture and dried matter, while 87:12 supplies fire, but the production scenes are lexically mediated.
- Surprising reach: The channel includes lactation, udder protection, watered milk, syrup, fat residue, curdling, perfume, soot, lime, pots, grinding stones, and serving bowls.

#### Subchannel A. Lactation, Milk Scarcity, and Udder Protection
- Reading type: latent/lexical
- Scene or process: A milk animal produces, withholds, or has its milk diluted, while equipment protects or gathers the yield.
- Active motifs: lactation `ي س ر:B006/m01`; scarcity of milk `ج ن ب:B008/m01`; udder bag or cover `ء ث ر:B012/m01`; fresh ewe `ر ب ب:B009/m01`; watered milk `ن س ي:B007/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:6 `تَنسَىٰ`; 87:8 `ٱلْيُسْرَىٰ`; 87:11 `يَتَجَنَّبُهَا`; 87:16 `تُؤْثِرُونَ`
- Synthesis: Pastoral abundance is unstable: lactation, scarcity, dilution, and protection describe competing controls over nourishment.

#### Subchannel B. Moisture, Curdling, Syrup, and Residue
- Reading type: latent/lexical
- Scene or process: A wet substance settles, concentrates, curdles, or leaves a fatty remainder.
- Active motifs: moisture `ب ل ل:B001/m01`; curdling or settled end-state `ء و ل:B005/m01`; thick syrup `ر ب ب:B006/m01`; fat residue `ء ث ر:B009/m01`; viscous containment `ح و ي:B001/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:5 `أَحْوَىٰ`; 87:16 `بَلْ` and `تُؤْثِرُونَ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Transformation proceeds through concentration: fluid matter becomes thicker, bounded, and increasingly defined by what remains.

#### Subchannel C. Paste, Perfume, Soot, and Lime
- Reading type: latent/lexical
- Scene or process: Fine matter is compounded into an aromatic, darkening, cleansing, or caustic preparation.
- Active motifs: perfume compound `خ ل ق:B010/m01`; soot or kohl `ن و ر:B008/m01`; depilatory lime `ن و ر:B009/m01`; compact paste-like consistency `ج ع ل:B012/m01`; worthless residue `غ ث و:B004/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:5 `جَعَلَهُ غُثَاءً`; 87:12 `ٱلنَّارَ`
- Synthesis: The same movement from dispersed matter to concentrated substance can yield fragrance, pigment, cleanser, or refuse.

#### Subchannel D. Pot, Boiling, Roasting, and Fermentation
- Reading type: latent/lexical
- Scene or process: A vessel receives matter that is heated, boiled, roasted, or allowed to ferment.
- Active motifs: cooking pot `ق د ر:B007/m01`; boiling `خ ر ج:B004/m01`; roasting at fire `ص ل ي:B004/m01`; fire or heat `ص ل و:B001/m01`; blaze `ن و ر:B002/m01`; fermenting beverage vessel `ء و ل:B010/m01`
- Ayah anchors: 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:12 `يَصْلَى ٱلنَّارَ`; 87:15 `فَصَلَّىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Heat and time transform contained material, making the vessel a controlled site of emergence and end-state.

#### Subchannel E. Grinding, Serving, and Kitchen Implements
- Reading type: latent/lexical
- Scene or process: Food is processed on a stone, contained in a pot, and presented on a broad vessel.
- Active motifs: grinding stone `ص ل و:B008/m01`; grinding-stone variant `ص ل ي:B009/m01`; broad bowl `ص ح ف:B004/m01`; pot cloth `ج ع ل:B007/m01`; two-eared vessel `خ ر ج:B009/m01`; cooking pot `ق د ر:B007/m01`
- Ayah anchors: 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:5 `جَعَلَهُ`; 87:15 `فَصَلَّىٰ`; 87:18-19 `صُحُفِ`
- Synthesis: Preparation and service form a tool chain from grinding surface through heated container to serving vessel.

### 13. Household, Nurture, and Collective Life
- Semantic invariant: Individuals are gathered into households, camps, neighborhoods, herds, and governed groups sustained by care and shared resources.
- Surface relation: indirect; lordship and pasture in 87:1-4 provide the governing and pastoral anchors.
- Surprising reach: The channel includes stepchildren, clans, encampments, neighbors, large groups, communal need, restless livestock, and dependents.

#### Subchannel A. Household, Clan, Camp, and Gathering
- Reading type: latent/lexical
- Scene or process: People or possessions are gathered into a bounded domestic or communal unit.
- Active motifs: household `ء و ل:B003/m01`; clan `ح ي ي:B010/m01`; gathering or containment `ح و ي:B001/m01`; encampment `ح و ي:B005/m01`; group `ج ه ر:B006/m01`; large groups `ر ب ب:B004/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:5 `أَحْوَىٰ`; 87:7 `ٱلْجَهْرَ`; 87:13 `يَحْيَىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Collective life is organized by enclosure at several scales, from household and clan to camp and public group.

#### Subchannel B. Ward, Pair, and Dependent
- Reading type: latent/lexical
- Scene or process: A household assumes responsibility for paired members, children, wards, and those economically dependent on it.
- Active motifs: stepchild or ward `ر ب ب:B005/m01`; pair `ز ك و:B005/m01`; property and dependents `ق ر ء:B013/m01`; offspring loss `م و ت:B005/m01`; nurturing or repair `ر ب ب:B002/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:6 `سَنُقْرِئُكَ`; 87:13 `يَمُوتُ`; 87:14 `تَزَكَّىٰ`
- Synthesis: Nurture becomes socially concrete as responsibility for those whose life, property, or development is entrusted to another.

#### Subchannel C. Shepherding, Governance, and Collective Need
- Reading type: mixed
- Scene or process: A leader tends a group, manages common resources, and resolves shared need or entanglement.
- Active motifs: shepherding or governance `ر ع ي:B002/m01`; herd `ر ب ب:B014/m01`; governance and reform `ء و ل:B004/m01`; collective need `ر ب ب:B016/m01`; binding knot `ر ب ب:B016/m02`; monitoring `ر ع ي:B003/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:4 `ٱلْمَرْعَىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Governance is figured as pastoral care: authority must watch, untangle, and provision the collective rather than merely command it.

#### Subchannel D. Neighbor, Covenant, and Social Proximity
- Reading type: latent/lexical
- Scene or process: Proximity creates obligations that are maintained by covenant or broken through separation.
- Active motifs: neighbor `ج ن ب:B002/m01`; bodily or social side `ج ن ب:B001/m01`; covenant `ر ب ب:B011/m01`; covenant preservation `ر ع ي:B006/m01`; separation `ج ن ب:B003/m01`; abundant good or evil between parties `ج ن ب:B009/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:4 `ٱلْمَرْعَىٰ`; 87:11 `يَتَجَنَّبُهَا`
- Synthesis: Being beside another creates a field of possible care, harm, fidelity, and withdrawal.

#### Subchannel E. Herd, Ewe, and Restless Livestock
- Reading type: latent/lexical
- Scene or process: Herd animals graze under care, yield nourishment, or move with difficult-to-control energy.
- Active motifs: herd `ر ب ب:B014/m01`; fresh ewe `ر ب ب:B009/m01`; pasture `ر ع ي:B001/m01`; skittish animal `ن و ر:B006/m01`; mounted or settled animal `س و ي:B003/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:2 `سَوَّىٰ`; 87:4 `ٱلْمَرْعَىٰ`; 87:12 `ٱلنَّارَ`
- Synthesis: The pastoral scene joins nourishment and volatility, requiring governance that can both sustain and settle animal movement.

#### Subchannel F. Wealth, Dependents, and Group Provision
- Reading type: latent/lexical
- Scene or process: A collective is sustained through wealth, taxable yield, equivalent shares, and responsibility for dependents.
- Active motifs: wealth or means `ي س ر:B003/m01`; property and dependents `ق ر ء:B013/m01`; levy or tax `خ ر ج:B003/m01`; equivalent wealth `س و ي:B013/m01`; wage `ج ع ل:B005/m01`
- Ayah anchors: 87:2 `سَوَّىٰ`; 87:4 `أَخْرَجَ`; 87:5 `جَعَلَهُ`; 87:6 `سَنُقْرِئُكَ`; 87:8 `ٱلْيُسْرَىٰ`
- Synthesis: Material provision links household responsibility to assessment, compensation, and equitable division.

### 14. Covenant, Property, and Reciprocal Exchange
- Semantic invariant: Goods, labor, protection, and obligations move among parties under rules of possession, equivalence, retention, and release.
- Surface relation: indirect; 87:9 and 87:17 supply benefit and enduring value, while 87:16 supplies the problem of preferential retention.
- Surprising reach: The channel includes refuge, ransom-like protection, gifts, wages, taxation, partner-share division, monopoly, feud, and binding knots.

#### Subchannel A. Covenant, Refuge, and Protected Release
- Reading type: latent/lexical
- Scene or process: A binding promise secures a neighbor, captive, or person seeking refuge against uncontrolled harm.
- Active motifs: covenant `ر ب ب:B011/m01`; preservation of covenant `ر ع ي:B006/m01`; captive, refuge, or protection `ه د ي:B007/m01`; neighbor `ج ن ب:B002/m01`; sparing `ب ق ي:B003/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:3 `هَدَىٰ`; 87:4 `ٱلْمَرْعَىٰ`; 87:11 `يَتَجَنَّبُهَا`; 87:17 `أَبْقَىٰ`
- Synthesis: Protection converts bare power into bounded obligation by requiring that life or liberty be preserved under a pledged relation.

#### Subchannel B. Gift, Wage, and Benefaction
- Reading type: latent/lexical
- Scene or process: Value passes to another as gift, payment, generosity, or welfare-producing favor.
- Active motifs: gift `ه د ي:B004/m01`; wage `ج ع ل:B005/m01`; generosity or gift `خ ي ر:B005/m01`; welfare or benefaction `ب ل ل:B002/m01`; benefit `ن ف ع:B001/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:5 `جَعَلَهُ`; 87:9 `نَّفَعَتِ`; 87:16 `بَلْ`; 87:17 `خَيْرٌ`
- Synthesis: Exchange is evaluated by its effect: gift and wage become benefaction when transferred value genuinely improves another's condition.

#### Subchannel C. Retention, Monopoly, and Sharing
- Reading type: mixed
- Scene or process: A holder chooses between keeping value exclusively, reserving it legitimately, and releasing it toward others.
- Active motifs: monopolizing possession `ء ث ر:B006/m01`; reserve `ب ق ي:B004/m01`; preference or selection `ء ث ر:B005/m01`; generosity `خ ي ر:B005/m01`; clinging `ب ل ل:B004/m02`; abundant good or evil `ج ن ب:B009/m01`
- Ayah anchors: 87:11 `يَتَجَنَّبُهَا`; 87:16 `تُؤْثِرُونَ` and `بَلْ`; 87:17 `خَيْرٌ وَأَبْقَىٰ`
- Synthesis: Retention is morally ambivalent: prudent reserve and enduring value differ from preference that hardens into monopoly.

#### Subchannel D. Levy, Ownership, and Partner-Share Division
- Reading type: latent/lexical
- Scene or process: Property is assessed, owned, divided between partners, and balanced against an equivalent share.
- Active motifs: levy or tax `خ ر ج:B003/m01`; possession `ذ و و:B001/m01`; property and dependents `ق ر ء:B013/m01`; partner-share division or buyout `خ ر ج:B012/m01`; equivalent wealth `س و ي:B013/m01`; assigned amount `ق د ر:B001/m01`
- Ayah anchors: 87:2 `سَوَّىٰ`; 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:6 `سَنُقْرِئُكَ`; 87:18 `هَٰذَا`
- Synthesis: Fair division depends on identifying possession, assessing amount, and converting an undivided partnership into equivalent claims.

#### Subchannel E. Feud, Attachment, and Broken Relation
- Reading type: latent/lexical
- Scene or process: A social bond becomes a site of hostile reciprocity, clinging attachment, or deliberate separation.
- Active motifs: feud `ن و ر:B007/m01`; clinging `ب ل ل:B004/m02`; separation `ج ن ب:B003/m01`; household bond `ء و ل:B003/m01`; covenant `ر ب ب:B011/m01`; obstinate contention `ب ل ل:B005/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:11 `يَتَجَنَّبُهَا`; 87:12 `ٱلنَّارَ`; 87:16 `بَلْ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Broken reciprocity does not erase relation; feud and contentious attachment preserve the bond in an antagonistic form.

### 15. Reproduction, Pairing, and Life Stage
- Semantic invariant: Living beings pass through pairing, gestation, birth, nourishment, maturity, and aging.
- Surface relation: indirect; 87:2 supplies formed life, 87:13 and 87:16 name life, and 87:14 supplies growth.
- Surprising reach: The channel includes womb cycles, imminent birth, postpartum recovery, estrus, stallion display, camel rut, brides, fresh ewes, and named youth.

#### Subchannel A. Womb, Cycle, and Imminent Birth
- Reading type: latent/lexical
- Scene or process: A reproductive cycle gathers life in the womb and approaches the threshold of delivery.
- Active motifs: womb `ق ر ء:B003/m01`; cycle `ق ر ء:B002/m01`; nearing birth `د ن و:B004/m01`; living formation `خ ل ق:B003/m01`
- Ayah anchors: 87:2 `خَلَقَ فَسَوَّىٰ`; 87:6 `سَنُقْرِئُكَ`; 87:16 `ٱلدُّنْيَا`
- Synthesis: Collection, recurrence, and nearness converge in gestation as a bounded process moving toward emergence.

#### Subchannel B. Birth, Nourishment, Loss, and Recovery
- Reading type: latent/lexical
- Scene or process: Delivery opens a vulnerable interval of nourishment, possible offspring loss, and bodily recovery.
- Active motifs: nearing delivery `د ن و:B004/m01`; lactation `ي س ر:B006/m01`; offspring loss `م و ت:B005/m01`; recovery `ب ل ل:B003/m01`; sparing life `ح ي ي:B006/m01`
- Ayah anchors: 87:8 `ٱلْيُسْرَىٰ`; 87:13 `يَمُوتُ` and `يَحْيَىٰ`; 87:16 `بَلْ` and `ٱلدُّنْيَا`
- Synthesis: Birth is not a single event but a risk-laden transition in which nourishment and recovery preserve newly separated life.

#### Subchannel C. Estrus, Pairing, and Mating Display
- Reading type: latent/lexical
- Scene or process: Reproductive readiness becomes visible through pairing, estrus, display, and seasonal animal behavior.
- Active motifs: estrus `ج ع ل:B009/m01`; pair `ز ك و:B005/m01`; stallion rearing or display `س م و:B003/m01`; camel rut `ق ر ء:B009/m01`; male sex `ذ ك ر:B001/m01`
- Ayah anchors: 87:1 and 87:15 `ٱسْمَ`; 87:5 `جَعَلَهُ`; 87:6 `سَنُقْرِئُكَ`; 87:14 `تَزَكَّىٰ`; 87:15 `ذَكَرَ`
- Synthesis: Pair formation is embodied through sex, seasonal readiness, and conspicuous display.

#### Subchannel D. Bride and Household Transition
- Reading type: latent/lexical
- Scene or process: A bride moves into a newly constituted household and kin relation.
- Active motifs: bride `ه د ي:B006/m01`; household `ء و ل:B003/m01`; clan `ح ي ي:B010/m01`; pair `ز ك و:B005/m01`; guided or led course `ه د ي:B003/m01`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:13 `يَحْيَىٰ`; 87:14 `تَزَكَّىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Marriage joins guided movement, pairing, and incorporation into a household or clan.

#### Subchannel E. Youth, Maturity, Freshness, and Old Age
- Reading type: latent/lexical
- Scene or process: A living being is identified at a stage between youth, full development, freshness, and senescence.
- Active motifs: youth reaching maturity `س و ي:B005/m01`; named youth Yasar `ي س ر:B011/m01`; fresh ewe `ر ب ب:B009/m01`; old age `ك ب ر:B004/m01`; living animal `ح ي ي:B003/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:2 `سَوَّىٰ`; 87:8 `ٱلْيُسْرَىٰ`; 87:12 `ٱلْكُبْرَىٰ`; 87:13 `يَحْيَىٰ`
- Synthesis: Life stage is read through bodily completion, freshness, naming, and eventual age.

### 16. Anatomy, Appearance, and Bodily Affliction
- Semantic invariant: The body is known through formed appearance, internal organs, posture, directional surfaces, and disruptions of health or movement.
- Surface relation: indirect; 87:2 supplies bodily formation, while 87:11-13 supply avoidance, burning, and impaired life.
- Surprising reach: The channel includes viscera, pudendum, face, cleft lip, sciatica, pleurisy, seizure, glare, malformed form, compact build, and supported gait.

#### Subchannel A. Face, Form, Build, and Disposition
- Reading type: latent/lexical
- Scene or process: A person's visible form and compact build express or conceal an inward disposition.
- Active motifs: face `ح ي ي:B012/m01`; disfiguring the face `ش ي ء:B002/m01`; proportioned form `خ ل ق:B003/m01`; disposition or character `خ ل ق:B004/m01`; malformed form `خ ر ج:B008/m01`; compact stockiness `ج ع ل:B012/m01`
- Ayah anchors: 87:2 `خَلَقَ فَسَوَّىٰ`; 87:4 `أَخْرَجَ`; 87:5 `جَعَلَهُ`; 87:7 `شَاءَ`; 87:13 `يَحْيَىٰ`
- Synthesis: Appearance is treated as a formed surface that may align with, distort, or misleadingly stand in for disposition.

#### Subchannel B. Viscera, Pudendum, Side, and Back
- Reading type: latent/lexical
- Scene or process: The body is mapped from concealed interior organs to protected or exposed lateral and posterior surfaces.
- Active motifs: viscera `ح و ي:B003/m01`; pudendum `ح ي ي:B011/m01`; bodily side `ج ن ب:B001/m01`; back or side `ص ل و:B005/m01`; back variant `ص ل ي:B006/m01`; binding knot `ر ب ب:B016/m02`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:5 `أَحْوَىٰ`; 87:11 `يَتَجَنَّبُهَا`; 87:13 `يَحْيَىٰ`; 87:15 `فَصَلَّىٰ`
- Synthesis: Anatomical hiddenness is relational: interior, side, back, and covered parts are defined by degrees of exposure and access.

#### Subchannel C. Posture, Gait, and Supported Movement
- Reading type: latent/lexical
- Scene or process: A body mounts, spreads its stance, bears support, or moves with a distinctive sway or thrust.
- Active motifs: splayed-leg stance `ج ن ب:B012/m01`; supported swaying gait `ه د ي:B008/m01`; mounted or settled posture `س و ي:B003/m01`; downward twist `ي س ر:B009/m01`; face-level thrust `ي س ر:B009/m02`; overhead load `ع ل و:B008/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:2 `سَوَّىٰ`; 87:3 `هَدَىٰ`; 87:8 `ٱلْيُسْرَىٰ`; 87:11 `يَتَجَنَّبُهَا`
- Synthesis: Posture records the interaction of balance, load, support, and directional force.

#### Subchannel D. Cleft, Fissure, Sharpness, and Cut
- Reading type: latent/lexical
- Scene or process: A hard or living surface is split by a sharp edge or bears a congenital fissure.
- Active motifs: splitting or cutting `ف ل ح:B001/m01`; cleft lip `ف ل ح:B002/m01`; cleft lip variant `ع ل م:B004/m01`; hardness or sharpness `ذ ك ر:B002/m01`; imperforate rock `خ ل ق:B012/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:7 `يَعْلَمُ`; 87:14 `أَفْلَحَ`; 87:15 `ذَكَرَ`
- Synthesis: The cut-channel spans tool action, bodily fissure, and resistant material, with sharpness mediating between them.

#### Subchannel E. Sciatica, Pleurisy, and Seizure
- Reading type: latent/lexical
- Scene or process: Pain or seizure compromises movement, breathing, or consciousness along a bodily side.
- Active motifs: sciatic nerve or sciatica `ن س ي:B004/m01`; pleurisy `ج ن ب:B007/m01`; seizure or coma `م و ت:B009/m01`; bodily side `ج ن ب:B001/m01`; weakening `م و ت:B002/m01`
- Ayah anchors: 87:6 `تَنسَىٰ`; 87:11 `يَتَجَنَّبُهَا`; 87:13 `يَمُوتُ`
- Synthesis: Side-oriented pain and neural disruption create a bodily analogue of the surah's suspended state between effective life and death.

#### Subchannel F. Illness, Epidemic, and Recovery
- Reading type: latent/lexical
- Scene or process: Disease spreads or incapacitates, after which the body may regain height, motion, and welfare.
- Active motifs: epidemic `ق ر ء:B008/m01`; outbreak `م و ت:B004/m01`; health recovery `ع ل و:B011/m01`; recovery `ب ل ل:B003/m01`; benefit or restored good `ح ي ي:B013/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:6 `سَنُقْرِئُكَ`; 87:13 `يَمُوتُ` and `يَحْيَىٰ`; 87:16 `بَلْ`
- Synthesis: Recovery reverses the downward course of illness by restoring stature, movement, and useful life.

#### Subchannel G. Fixed Gaze, Glare, and Overwhelmed Sight
- Reading type: latent/lexical
- Scene or process: The eye fixes on an object, sees farther, or fails under excessive brightness or magnitude.
- Active motifs: fixed gaze `ب ر ه م:B001/m01`; overwhelmed eye `ج ه ر:B003/m01`; sun-blinded eye `ج ه ر:B004/m01`; farsight `ش ي ء:B003/m01`; face `ح ي ي:B012/m01`
- Ayah anchors: 87:7 `ٱلْجَهْرَ` and `شَاءَ`; 87:12 `ٱلْكُبْرَىٰ`; 87:13 `يَحْيَىٰ`; 87:19 `إِبْرَٰهِيمَ`
- Synthesis: Sight ranges from focused and far-reaching attention to breakdown under what is too bright or too large.

### 17. Hunting, Racing, and Mobile Equipment
- Semantic invariant: Directed pursuit organizes bodies, animals, routes, and equipment around capture, speed, position, and controlled movement.
- Surface relation: indirect; 87:3 supplies guidance, 87:4 emergence into open terrain, and 87:8 facilitated movement.
- Surprising reach: The channel includes lures, traps, game verification, horse-race rank, surprise attack, saddle blankets, leather wear, and long-necked mounts.

#### Subchannel A. Lure, Trap, Hunt, and Verified Kill
- Reading type: latent/lexical
- Scene or process: A hunter attracts game, constrains its movement, pursues it, and verifies the endpoint.
- Active motifs: hunting `س م و:B006/m01`; animal lure `خ ي ر:B006/m01`; trap `ص ل و:B004/m01`; trap variant `ص ل ي:B005/m01`; verification of game death `م و ت:B014/m01`; falcon `ع ل م:B006/m01`
- Ayah anchors: 87:1 and 87:15 `ٱسْمَ`; 87:7 `يَعْلَمُ`; 87:13 `يَمُوتُ`; 87:15 `فَصَلَّىٰ`; 87:17 `خَيْرٌ`
- Synthesis: Pursuit becomes an ordered sequence from attraction and confinement to recognition of a valid end-state.

#### Subchannel B. Running, Following, and Second Place
- Reading type: latent/lexical
- Scene or process: Competitors move rapidly along a course whose order is measured by who leads and who follows.
- Active motifs: swimming or swift running `س ب ح:B004/m01`; following `ء ث ر:B004/m01`; second place in a horse race `ص ل و:B006/m01`; race-second variant `ص ل ي:B007/m01`; agile movement `ي س ر:B005/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:8 `ٱلْيُسْرَىٰ`; 87:15 `فَصَلَّىٰ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: The race literalizes precedence: movement produces a leading trace and a precisely ordered follower.

#### Subchannel C. Mount, Saddle, Blanket, and Riding Posture
- Reading type: latent/lexical
- Scene or process: A rider settles onto an equipped animal whose load and movement are stabilized by layered gear.
- Active motifs: mounted or settled `س و ي:B003/m01`; camel pack blanket `س و ي:B010/m01`; saddle or blanket `ح و ي:B004/m01`; leather garment `س ب ح:B007/m01`; splayed stance `ج ن ب:B012/m01`; supported gait `ه د ي:B008/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:2 `سَوَّىٰ`; 87:3 `هَدَىٰ`; 87:5 `أَحْوَىٰ`; 87:11 `يَتَجَنَّبُهَا`
- Synthesis: Mobile equipment turns unstable animal motion into a settled, supported course for rider and load.

#### Subchannel D. Exit, Roaming, and Approach
- Reading type: mixed
- Scene or process: A traveler leaves an enclosure, crosses open ground, and approaches a destination.
- Active motifs: exit `خ ر ج:B001/m01`; roaming for livelihood `س ب ح:B005/m01`; coming or approaching `ح ي ي:B009/m01`; approach or direction `س و ي:B004/m01`; movement toward a side `ج ن ب:B005/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:2 `سَوَّىٰ`; 87:4 `أَخْرَجَ`; 87:11 `يَتَجَنَّبُهَا`; 87:13 `يَحْيَىٰ`
- Synthesis: Travel is articulated as a sequence of release, open traversal, orientation, and arrival.

#### Subchannel E. Surprise Attack, Weapon Mark, and Thrust
- Reading type: latent/lexical
- Scene or process: Rapid directed motion becomes hostile through sudden attack, weapon contact, or a leveled thrust.
- Active motifs: morning surprise attack `ج ه ر:B005/m01`; sword mark or sheen `ء ث ر:B007/m01`; face-level thrust `ي س ر:B009/m02`; downward twist `ي س ر:B009/m01`; overcoming `ك ب ر:B011/m01`
- Ayah anchors: 87:7 `ٱلْجَهْرَ`; 87:8 `ٱلْيُسْرَىٰ`; 87:12 `ٱلْكُبْرَىٰ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: The pursuit channel becomes violent when speed, concealment, edge, and direction are coordinated against a target.

#### Subchannel F. Carrier, Load, and Extended Mount
- Reading type: latent/lexical
- Scene or process: A carrier or mount bears equipment across distance, its bodily form adapted to load and forward motion.
- Active motifs: carrier or hireling `ف ل ح:B004/m01`; overhead load `ع ل و:B008/m01`; carrying implement `ء و ل:B008/m01`; long horse neck `خ ر ج:B013/m01`; camel pack blanket `س و ي:B010/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:2 `سَوَّىٰ`; 87:4 `أَخْرَجَ`; 87:14 `أَفْلَحَ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Transit depends on a coordinated system of carrier, load, implement, and an animal body proportioned for extension.

### 18. Fabric, Color, Hardness, and Implements
- Semantic invariant: Materials are recognized and transformed through texture, color, edge, resistance, folding, containment, and practical use.
- Surface relation: indirect; 87:5 supplies darkened residue and 87:12 supplies fire, but most material scenes are lexical extensions.
- Surprising reach: The channel includes worn cloth, damp folds, saddle leather, waterskins, shields, stone, sword sheen, soot, lime, staffs, pots, and lot-arrow containers.

#### Subchannel A. Smooth Surface, Worn Fabric, and Damp Folding
- Reading type: latent/lexical
- Scene or process: A flexible surface is smoothed, worn thin, wetted, and folded into layers.
- Active motifs: smooth surface `خ ل ق:B008/m01`; worn fabric `خ ل ق:B009/m01`; damp folding `ب ل ل:B007/m01`; leather garment `س ب ح:B007/m01`; pack blanket `س و ي:B010/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:2 `خَلَقَ` and `سَوَّىٰ`; 87:16 `بَلْ`
- Synthesis: Material age and handling are legible in surface texture, moisture, and fold.

#### Subchannel B. Black-Red Color, Bicoloration, Soot, and Coating
- Reading type: mixed
- Scene or process: A surface darkens, carries contrasting colors, or receives a black or pale mineral coating.
- Active motifs: reddish black or black color `ح و ي:B006/m01`; bicoloration `خ ر ج:B007/m01`; soot or kohl `ن و ر:B008/m01`; depilatory lime `ن و ر:B009/m01`; sword sheen or mark `ء ث ر:B007/m01`
- Ayah anchors: 87:4 `أَخْرَجَ`; 87:5 `أَحْوَىٰ`; 87:12 `ٱلنَّارَ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: The dark stubble image opens into a material palette defined by darkening, contrast, reflective edge, and applied coating.

#### Subchannel C. Hardness, Edge, Fissure, and Stone
- Reading type: latent/lexical
- Scene or process: A resistant surface meets a sharp implement, producing a cut, mark, or revealing fissure.
- Active motifs: hardness or sharpness `ذ ك ر:B002/m01`; sword mark or sheen `ء ث ر:B007/m01`; splitting or cutting `ف ل ح:B001/m01`; imperforate rock `خ ل ق:B012/m01`; cleft or fissure `ف ل ح:B002/m01`
- Ayah anchors: 87:2 `خَلَقَ`; 87:14 `أَفْلَحَ`; 87:15 `ذَكَرَ`; 87:16 `تُؤْثِرُونَ`
- Synthesis: Hardness is disclosed by resistance to an edge, while the resulting mark or fissure records the encounter.

#### Subchannel D. Leather, Waterskin, Saddle, and Side Protection
- Reading type: latent/lexical
- Scene or process: Flexible animal material is shaped into clothing, liquid containment, riding gear, or lateral protection.
- Active motifs: leather garment `س ب ح:B007/m01`; waterskin sides `ن ف ع:B002/m01`; saddle or blanket `ح و ي:B004/m01`; side shield `ج ن ب:B011/m01`; udder cover `ء ث ر:B012/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:5 `أَحْوَىٰ`; 87:9 `نَّفَعَتِ`; 87:11 `يَتَجَنَّبُهَا`; 87:16 `تُؤْثِرُونَ`
- Synthesis: One material technology repeatedly solves problems of enclosing, carrying, and protecting vulnerable sides.

#### Subchannel E. Staff, Goad, Raised Tool, and Carrier
- Reading type: latent/lexical
- Scene or process: A handheld or raised implement supports movement, directs an animal, or bears a load.
- Active motifs: staff `ن ف ع:B003/m01`; goad or staff `ن س ي:B006/m01`; raised implements `ع ل و:B009/m01`; carrying tool `ء و ل:B008/m01`; carrier or hireling `ف ل ح:B004/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:6 `تَنسَىٰ`; 87:9 `نَّفَعَتِ`; 87:14 `أَفْلَحَ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Tools extend bodily agency by supporting, directing, lifting, or transferring force and weight.

#### Subchannel F. Vessel, Pot Cloth, and Broad Bowl
- Reading type: latent/lexical
- Scene or process: Containers of different shapes hold substances, protect hands from heat, or organize small objects.
- Active motifs: fermenting beverage vessel `ء و ل:B010/m01`; two-eared vessel `خ ر ج:B009/m01`; broad bowl `ص ح ف:B004/m01`; cooking pot `ق د ر:B007/m01`; pot cloth `ج ع ل:B007/m01`; lot-arrow container `ر ب ب:B010/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:5 `جَعَلَهُ`; 87:18-19 `صُحُفِ`
- Synthesis: Containment is specialized by contents and handling: liquid, heat, food, and tokens each require a differently formed vessel.

### 19. Tokens, Lots, and Games
- Semantic invariant: Uncertain allocation or counted repetition is externalized through small manipulable objects and rule-bound gestures.
- Surface relation: none; the channel arises from lexical branches rather than the surah's surface scenes.
- Surprising reach: Lot arrows connect distribution, gambling, equivalent shares, hidden-hand play, counted remembrance, and reserves.

#### Subchannel A. Lot Arrows, Gambling, and Allocation
- Reading type: latent/lexical
- Scene or process: Tokens are drawn or compared to assign uncertain outcomes, divide value, or stake wealth.
- Active motifs: lot-arrow container `ر ب ب:B010/m01`; gambling lots `ي س ر:B007/m01`; equivalent wealth `س و ي:B013/m01`; partner-share division `خ ر ج:B012/m01`; assigned amount `ق د ر:B001/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:2 `سَوَّىٰ`; 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:8 `ٱلْيُسْرَىٰ`
- Synthesis: The lot converts uncertainty into an actionable allocation, while equivalence and division determine what is at stake.

#### Subchannel B. Hidden-Hand Play, Beads, and Counting
- Reading type: latent/lexical
- Scene or process: Small objects are concealed, counted, or moved by hand according to a repeated rule.
- Active motifs: hidden-hand game `خ ر ج:B010/m01`; remembrance beads `س ب ح:B006/m01`; assigned amount `ق د ر:B001/m01`; held reserve `ب ق ي:B004/m01`; body or identifying marks `ي س ر:B008/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:3 `قَدَّرَ`; 87:4 `أَخْرَجَ`; 87:8 `ٱلْيُسْرَىٰ`; 87:17 `أَبْقَىٰ`
- Synthesis: Concealment and count create suspense, whether the tokens serve play, devotion, identification, or inventory.

### 20. Animal Identity Through Form, Sound, and Habitat
- Semantic invariant: Animals are distinguished through bodily form, characteristic motion or sound, life stage, and ecological niche.
- Surface relation: indirect; pasture in 87:4 and life in 87:13 and 87:16 provide the broad biological setting.
- Surprising reach: The channel includes a coiling snake, mountain stag, hyena, falcon, nightingale, ostrich chick, dung beetle, fresh ewe, stallion, and skittish herd animal.

#### Subchannel A. Serpent and Coil
- Reading type: latent/lexical
- Scene or process: A snake is recognized through the gathering and coiling of its elongated body.
- Active motifs: snake `ح ي ي:B004/m01`; coil `ح و ي:B002/m01`; living animal `ح ي ي:B003/m01`; gathering or containment `ح و ي:B001/m01`
- Ayah anchors: 87:5 `أَحْوَىٰ`; 87:13 `يَحْيَىٰ`; 87:16 `ٱلْحَيَوٰةَ`
- Synthesis: Animal identity emerges from motion and geometry: living elongation becomes recognizable when it coils into a bounded form.

#### Subchannel B. Mountain Stag, Hyena, Ridge, and Spur
- Reading type: latent/lexical
- Scene or process: Mountain animals are identified against the raised ridges and projecting spurs of their habitat.
- Active motifs: mountain stag `ء و ل:B009/m01`; male hyena `ع ل م:B007/m01`; mountain ridge `ش ق و:B004/m01`; mountain spur `ش ق ي:B004/m01`; tallness `ع ل و:B010/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:7 `يَعْلَمُ`; 87:11 `ٱلْأَشْقَىٰ`; 87:18 `ٱلْأُولَىٰ`
- Synthesis: Species and terrain form a single scene signature: projecting animal forms inhabit projecting landforms.

#### Subchannel C. Falcon, Nightingale, and Ostrich Chick
- Reading type: latent/lexical
- Scene or process: Birds are distinguished through predatory role, characteristic sound, or juvenile form.
- Active motifs: falcon `ع ل م:B006/m01`; nightingale or bird sound `ب ل ل:B010/m01`; ostrich chick `ج ع ل:B010/m01`; young animal form `ح ي ي:B003/m01`
- Ayah anchors: 87:5 `جَعَلَهُ`; 87:7 `يَعْلَمُ`; 87:13 `يَحْيَىٰ`; 87:16 `بَلْ`
- Synthesis: Bird identity is distributed across action, voice, and life stage rather than a single shared morphology.

#### Subchannel D. Dung Beetle and Residue Habitat
- Reading type: latent/lexical
- Scene or process: A small beetle is identified through its compact body and association with organic residue.
- Active motifs: dung beetle `ج ع ل:B008/m01`; compact stockiness `ج ع ل:B012/m01`; refuse `غ ث و:B004/m01`; rolling or roaming movement `س ب ح:B005/m01`
- Ayah anchors: 87:1 `سَبِّحِ`; 87:5 `جَعَلَهُ غُثَاءً`
- Synthesis: The decay field becomes habitat and material for a creature whose form and movement are adapted to residue.

#### Subchannel E. Herd Animal, Ewe, Stallion, and Skittishness
- Reading type: latent/lexical
- Scene or process: Domestic herd animals are differentiated by sex, freshness, display, and unstable movement.
- Active motifs: herd `ر ب ب:B014/m01`; fresh ewe `ر ب ب:B009/m01`; stallion display `س م و:B003/m01`; skittish animal `ن و ر:B006/m01`; long horse neck `خ ر ج:B013/m01`; male sex `ذ ك ر:B001/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ` and `ٱسْمَ`; 87:4 `أَخْرَجَ`; 87:12 `ٱلنَّارَ`; 87:15 `ذَكَرَ`
- Synthesis: Domestic animal identity is read through body, sex, age, display, and manageability within the herd.

#### Subchannel F. Animal Appraisal and Dullness
- Reading type: latent/lexical
- Scene or process: Animal or human behavior is reduced to an evaluative type such as dull, unruly, or difficult to direct.
- Active motifs: dullard `ه د ي:B009/m01`; dullness of mind `م و ت:B006/m01`; skittishness `ن و ر:B006/m01`; obstinate compactness `ج ع ل:B012/m02`
- Ayah anchors: 87:3 `هَدَىٰ`; 87:5 `جَعَلَهُ`; 87:12 `ٱلنَّارَ`; 87:13 `يَمُوتُ`
- Synthesis: Failed direction can be perceived as diminished cognition, unstable movement, or refusal to yield.

## Standalone Subchannels

### S1. Brahmin Messenger Doctrine and Abrahamic Naming
- Reading type: latent/lexical
- Scene or process: A named Abrahamic figure and a doctrinal community are linked through discourse about messengers and inherited sacred identity.
- Active motifs: Abraham or Ibrahim and name variants `ب ر ه م:B003/m01`; Brahmins and doctrine concerning messengers `ب ر ه م:B004/m01`; written sheets `ص ح ف:B002/m01`; transmitted report `ء ث ر:B002/m01`
- Ayah anchors: 87:18-19 `ٱلصُّحُفِ ٱلْأُولَىٰ صُحُفِ إِبْرَٰهِيمَ`
- Synthesis: The named scriptural endpoint activates an unusually specific intercommunal doctrinal scene that does not reduce to the broader writing or naming channels.

### S2. Nausea, Turmoil, and Revulsion
- Reading type: latent/lexical
- Scene or process: Disturbance turns inward as physical nausea or spreads outward as collective agitation.
- Active motifs: nausea `غ ث و:B003/m01`; turmoil or social disturbance `ب ل ل:B009/m01`
- Ayah anchors: 87:5 `غُثَاءً`; 87:16 `بَلْ`
- Synthesis: A shared pattern of destabilizing churn links bodily revulsion to social disorder while remaining distinct from ordinary decay.

### S3. Sailor-Captain and Directed Transit
- Reading type: latent/lexical
- Scene or process: A captain directs movement while a carrier bears people or goods along a chosen route.
- Active motifs: sailor-captain `ر ب ب:B017/m01`; carrier or hireling `ف ل ح:B004/m01`; guided front or leader `ه د ي:B003/m01`; exit and departure `خ ر ج:B001/m01`
- Ayah anchors: 87:1 and 87:15 `رَبِّ`; 87:3 `هَدَىٰ`; 87:4 `أَخْرَجَ`; 87:14 `أَفْلَحَ`
- Synthesis: Captaincy isolates a specialized command scene in which authority, route-setting, departure, and carriage converge.

### S4. Drum, High Call, and Acoustic Signaling
- Reading type: latent/lexical
- Scene or process: A sound is projected over distance through a raised voice, resonant instrument, or recognizable bird call.
- Active motifs: drum `ك ب ر:B012/m01`; high call `ع ل و:B006/m01`; loud or public voice `ج ه ر:B001/m01`; nightingale or bird sound `ب ل ل:B010/m01`
- Ayah anchors: 87:1 `ٱلْأَعْلَى`; 87:7 `ٱلْجَهْرَ`; 87:12 `ٱلْكُبْرَىٰ`; 87:16 `بَلْ`
- Synthesis: Acoustic prominence forms a compact standalone channel spanning human call, instrument, and animal voice.


