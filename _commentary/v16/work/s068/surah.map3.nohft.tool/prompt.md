Surah: 68. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S68 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s068/surah.r2/text.md =====
# Surah 68

- 68:1 نٓ ۚ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ
- 68:2 مَآ أَنتَ بِنِعْمَةِ رَبِّكَ بِمَجْنُونٍۢ
- 68:3 وَإِنَّ لَكَ لَأَجْرًا غَيْرَ مَمْنُونٍۢ
- 68:4 وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍۢ
- 68:5 فَسَتُبْصِرُ وَيُبْصِرُونَ
- 68:6 بِأَييِّكُمُ ٱلْمَفْتُونُ
- 68:7 إِنَّ رَبَّكَ هُوَ أَعْلَمُ بِمَن ضَلَّ عَن سَبِيلِهِۦ وَهُوَ أَعْلَمُ بِٱلْمُهْتَدِينَ
- 68:8 فَلَا تُطِعِ ٱلْمُكَذِّبِينَ
- 68:9 وَدُّوا۟ لَوْ تُدْهِنُ فَيُدْهِنُونَ
- 68:10 وَلَا تُطِعْ كُلَّ حَلَّافٍۢ مَّهِينٍ
- 68:11 هَمَّازٍۢ مَّشَّآءٍۭ بِنَمِيمٍۢ
- 68:12 مَّنَّاعٍۢ لِّلْخَيْرِ مُعْتَدٍ أَثِيمٍ
- 68:13 عُتُلٍّۭ بَعْدَ ذَٰلِكَ زَنِيمٍ
- 68:14 أَن كَانَ ذَا مَالٍۢ وَبَنِينَ
- 68:15 إِذَا تُتْلَىٰ عَلَيْهِ ءَايَٰتُنَا قَالَ أَسَٰطِيرُ ٱلْأَوَّلِينَ
- 68:16 سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ
- 68:17 إِنَّا بَلَوْنَٰهُمْ كَمَا بَلَوْنَآ أَصْحَٰبَ ٱلْجَنَّةِ إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ
- 68:18 وَلَا يَسْتَثْنُونَ
- 68:19 فَطَافَ عَلَيْهَا طَآئِفٌۭ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ
- 68:20 فَأَصْبَحَتْ كَٱلصَّرِيمِ
- 68:21 فَتَنَادَوْا۟ مُصْبِحِينَ
- 68:22 أَنِ ٱغْدُوا۟ عَلَىٰ حَرْثِكُمْ إِن كُنتُمْ صَٰرِمِينَ
- 68:23 فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ
- 68:24 أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ
- 68:25 وَغَدَوْا۟ عَلَىٰ حَرْدٍۢ قَٰدِرِينَ
- 68:26 فَلَمَّا رَأَوْهَا قَالُوٓا۟ إِنَّا لَضَآلُّونَ
- 68:27 بَلْ نَحْنُ مَحْرُومُونَ
- 68:28 قَالَ أَوْسَطُهُمْ أَلَمْ أَقُل لَّكُمْ لَوْلَا تُسَبِّحُونَ
- 68:29 قَالُوا۟ سُبْحَٰنَ رَبِّنَآ إِنَّا كُنَّا ظَٰلِمِينَ
- 68:30 فَأَقْبَلَ بَعْضُهُمْ عَلَىٰ بَعْضٍۢ يَتَلَٰوَمُونَ
- 68:31 قَالُوا۟ يَٰوَيْلَنَآ إِنَّا كُنَّا طَٰغِينَ
- 68:32 عَسَىٰ رَبُّنَآ أَن يُبْدِلَنَا خَيْرًۭا مِّنْهَآ إِنَّآ إِلَىٰ رَبِّنَا رَٰغِبُونَ
- 68:33 كَذَٰلِكَ ٱلْعَذَابُ ۖ وَلَعَذَابُ ٱلْءَاخِرَةِ أَكْبَرُ ۚ لَوْ كَانُوا۟ يَعْلَمُونَ
- 68:34 إِنَّ لِلْمُتَّقِينَ عِندَ رَبِّهِمْ جَنَّٰتِ ٱلنَّعِيمِ
- 68:35 أَفَنَجْعَلُ ٱلْمُسْلِمِينَ كَٱلْمُجْرِمِينَ
- 68:36 مَا لَكُمْ كَيْفَ تَحْكُمُونَ
- 68:37 أَمْ لَكُمْ كِتَٰبٌۭ فِيهِ تَدْرُسُونَ
- 68:38 إِنَّ لَكُمْ فِيهِ لَمَا تَخَيَّرُونَ
- 68:39 أَمْ لَكُمْ أَيْمَٰنٌ عَلَيْنَا بَٰلِغَةٌ إِلَىٰ يَوْمِ ٱلْقِيَٰمَةِ ۙ إِنَّ لَكُمْ لَمَا تَحْكُمُونَ
- 68:40 سَلْهُمْ أَيُّهُم بِذَٰلِكَ زَعِيمٌ
- 68:41 أَمْ لَهُمْ شُرَكَآءُ فَلْيَأْتُوا۟ بِشُرَكَآئِهِمْ إِن كَانُوا۟ صَٰدِقِينَ
- 68:42 يَوْمَ يُكْشَفُ عَن سَاقٍۢ وَيُدْعَوْنَ إِلَى ٱلسُّجُودِ فَلَا يَسْتَطِيعُونَ
- 68:43 خَٰشِعَةً أَبْصَٰرُهُمْ تَرْهَقُهُمْ ذِلَّةٌۭ ۖ وَقَدْ كَانُوا۟ يُدْعَوْنَ إِلَى ٱلسُّجُودِ وَهُمْ سَٰلِمُونَ
- 68:44 فَذَرْنِى وَمَن يُكَذِّبُ بِهَٰذَا ٱلْحَدِيثِ ۖ سَنَسْتَدْرِجُهُم مِّنْ حَيْثُ لَا يَعْلَمُونَ
- 68:45 وَأُمْلِى لَهُمْ ۚ إِنَّ كَيْدِى مَتِينٌ
- 68:46 أَمْ تَسْـَٔلُهُمْ أَجْرًۭا فَهُم مِّن مَّغْرَمٍۢ مُّثْقَلُونَ
- 68:47 أَمْ عِندَهُمُ ٱلْغَيْبُ فَهُمْ يَكْتُبُونَ
- 68:48 فَٱصْبِرْ لِحُكْمِ رَبِّكَ وَلَا تَكُن كَصَاحِبِ ٱلْحُوتِ إِذْ نَادَىٰ وَهُوَ مَكْظُومٌۭ
- 68:49 لَّوْلَآ أَن تَدَٰرَكَهُۥ نِعْمَةٌۭ مِّن رَّبِّهِۦ لَنُبِذَ بِٱلْعَرَآءِ وَهُوَ مَذْمُومٌۭ
- 68:50 فَٱجْتَبَٰهُ رَبُّهُۥ فَجَعَلَهُۥ مِنَ ٱلصَّٰلِحِينَ
- 68:51 وَإِن يَكَادُ ٱلَّذِينَ كَفَرُوا۟ لَيُزْلِقُونَكَ بِأَبْصَٰرِهِمْ لَمَّا سَمِعُوا۟ ٱلذِّكْرَ وَيَقُولُونَ إِنَّهُۥ لَمَجْنُونٌۭ
- 68:52 وَمَا هُوَ إِلَّا ذِكْرٌۭ لِّلْعَٰلَمِينَ


===== _commentary/v16/work/s068/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ل م (root_001252): 68:1 وَٱلْقَلَمِ

- **B001** sert ucu kesip yontarak düzeltme ve çıkan parça — tırnağı kesmek; sert bir şeyi yontarak düzeltmek · kesilen tırnak parçası
  تسوية شيء عند بريه وإصلاحه (maqayis)؛ قلمت الظفر وقلمته (maqayis)؛ القلامة ما يسقط من الظفر إذا قلم (maqayis)؛ القلم قطع الظفر بالقلمين وبالقلم (ayn;tahdhib)؛ قلمت ظفري وقلمت أظفاري والقلامة ما سقط منه (sihah)؛ قلمت الشيء بريته (tahdhib)؛ أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب (mufradat)
- **B002** tırnağı kesilmiş gibi güçsüz [kalıp] — tırnağı kesilmiş ya da körelmiş gibi güçsüz
  يقال للضعيف هو مقلوم الأظفار (maqayis)؛ يقال للضعيف مقلوم الظفر وكليل الظفر (sihah)
- **B003** yazı yazma aracı — yazı yazma aracı · yazı araçlarını taşıyan kap
  سمي القلم قلما لأنه يقلم منه كما يقلم من الظفر (maqayis)؛ الأقلام جماعة القلم (ayn)؛ أقلامهم التي كانوا يكتبون بها التوراة (ayn)؛ القلم الذي يكتب به (sihah)؛ المقلمة وعاء الأقلام (sihah)؛ القلم الذي يكتب به وإنما سمي قلما لأنه قلم مرة بعد مرة (tahdhib)؛ خص ذلك بما يكتب به وجمعه أقلام (mufradat)
- **B004** işaretli kura çubuğu veya oku — kura için kullanılan işaretli çubuk veya ok
  شبه القدح به فقيل قلم؛ يلقون أقلامهم (maqayis)؛ القلم السهم الذي يجال به بين القوم (ayn)؛ القلم الزلم (sihah)؛ الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة (tahdhib)؛ بالقدح الذي يضرب به وجمعه أقلام (mufradat)
- **B005** özel adlandırma kümesi — erkek devenin üreme organının çengelli ucu · erkek devenin üreme organının kılıfı · mızrağın boğumları; mızrak veya kamışın dip bölümü
  المقلم طرف قنب البعير؛ مقالم الرمح كعوبه (maqayis)؛ المقلم طرف قضيب البعير (ayn)؛ المقلم وعاء قضيب البعير؛ مقالم الرمح كعوبه (sihah)؛ المقلم طرف قضيب البعير وفي طرفه حجنة (tahdhib)؛ كعب الرمح والقصب (mufradat)
- **B006** iki ağızlı kesme aracı — iki ağızlı kesme aracı
  القلم قطع الظفر بالقلمين وبالقلم (ayn)؛ القلم الجلم (sihah)؛ يقال للمقراض المقلام والقلمان والجلمان (tahdhib)
- **B007** gövdesiz tuzcul bir bitki türü — gövdesiz tuzcul bir bitki türü
  مما شذ عن هذا الأصل القلام وهو نبت (maqayis)؛ القلام بالتشديد القاقلى وهو من الحمض (sihah)؛ القلام القاقلى؛ القلام من الحمض لا ساق له (tahdhib)
- **B008** yeryüzünün büyük coğrafi bölümlerinden biri — yeryüzünün büyük coğrafi bölümlerinden biri
  الإقليم واحد أقاليم الأرض السبعة (sihah)؛ الإقليم واحد الأقاليم وأحسبه عربيا (tahdhib)؛ سمي إقليما لأنه مقلوم من الإقليم الذي يتاخمه أي مقطوع عنه (tahdhib)؛ الإقليم واحد الأقاليم السبعة؛ الدنيا مقسومة على سبعة أسهم (mufradat)
- **B009** eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması — eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması
  القلمة العزاب من الرجال الواحد قالم ونساء مقلمات؛ القلم طول أيمة المرأة وامرأة مقلمة أي أيم؛ مقلمات بغير أزواج
- **B010** gözde farklı renklere bürünen yabancı kökenli dokuma — gözde farklı renklere bürünen yabancı kökenli kumaş
  أبو قلمون ضرب من ثياب الروم يتلون للعيون ألوانا

## س ط ر (root_000704): 68:1 يَسْطُرُونَ, 68:15 أَسَٰطِيرُ

- **B001** düzenli sıra oluşturma ve yazıyı sıra sıra kayda geçirme — nesne sırası; yazı sırası veya yazı çizgisi · yazmak; sıra sıra yazıya geçirmek · yazmak · yazılmış, kayda geçirilmiş ve korunmuş · adımın bulunduğu yazı sırasını geçti
  أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر (maqayis)؛ السطر سطر من كتب وسطر من شجر مغروس (ayn;tahdhib)؛ السطر الصف من الشيء والخط والكتابة (sihah)؛ السطر والسطر الصف من الكتابة ومن الشجر المغروس ومن القوم الوقوف (mufradat)؛ سطر يسطر إذا كتب (ayn;sihah;tahdhib)؛ كتاب مسطور ومسطورا أي مثبتا محفوظا (mufradat)
- **B002** asılsız veya düzensiz anlatı ve temelsiz söz uydurma — asılsız veya düzensiz anlatılar · asılsız veya düzensiz bir anlatı · asılsız veya düzensiz bir anlatı · asılsız veya düzensiz bir anlatı · asılsız veya düzensiz bir anlatı · asılsız veya düzensiz bir anlatı · bize gerçeğe aykırı anlatılar getirdi · hiçbir temeli olmayan şeyler uydurur
  الأساطير أشياء كتبت من الباطل (maqayis)؛ أحاديث تشبه الباطل (ayn;tahdhib)؛ أحاديث لا نظام لها بشيء (ayn)؛ الأساطير الأباطيل (sihah)؛ يسطر ما لا أصل له أي يؤلف (ayn;tahdhib)
- **B003** gözeten, koruyan ve hesap tutan yetkili denetleyici — koruyup gözeten, sorumluluğunu üstlenen yetkili denetleyici · durumları izlemekle görevli yetkili gözetmen · yetkili gözetim, koruma ve denetim · üzerimizde yetki kurup durumlarımızı gözetti
  المسيطر المتعهد للشيء المتسلط عليه (maqayis)؛ السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء (ayn;tahdhib)؛ المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله (sihah)؛ المسيطرون الأرباب المسلطون (tahdhib)
- **B004** yere serme veya kılıçla düz bir iz gibi kesme — onu yere serdi · onu kılıçla düz bir iz gibi kesti · et doğrama bıçağı · et doğrayan kişi · et doğrayan kişi
  سطره أي صرعه (sihah)؛ سطر فلان فلانا بالسيف سطرا إذا قطعه به كأنه سطر مسطور ومنه قيل لسيف القصاب ساطور (tahdhib)؛ يقال للقصاب ساطر وسطار (tahdhib)
- **B005** biçime bağlı adlandırmalar — 
  المسطار بكسر الميم ضرب من الشراب فيه حموضة (sihah)؛ المسطار هو الغبار المرتفع في السماء وقيل كان في الأصل مستطارا (tahdhib)؛ مسطار ماشية لم يعد أن عصرا (tahdhib)
- **B006** yanlış yapma ve bunu dolaylı yoldan söyleme — bugün yanlış yaptı; yanılması dolaylı biçimde söylendi · yanlış yapma, yanılma
  يقولون للرجل إذا أخطأ فكنوا عن خطئه أسطر فلان اليوم وهو الإسطار بمعنى الإخطاء (tahdhib)
- **B007** genç erkek küçükbaş hayvan — genç erkek küçükbaş hayvan
  السطر العتود من الغنم (tahdhib)

## ن ع م (root_001525): 68:2 بِنِعْمَةِ, 68:34 ٱلنَّعِيمِ, 68:49 نِعْمَةٌ

- **B001** iyi yaşam durumu ve başkasına ulaştırılan iyilik — bağış, iyilik veya elverişli yaşam durumu · iyi durum ve esenlik · bolluk ve rahatlık · bol ve rahat yaşam · iyiliği başkasına ulaştırma
  أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)
- **B002** yumuşamak, rahat yaşamak veya rahat yaşatmak — yumuşamak · yumuşak; rahat yaşayan · rahat ve bolluk içinde yaşayan kadın · çocuklarını bolluk içinde yaşattı · rahat ve bolluk içindeki yaşam
  نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)
- **B003** övgü ve beğeni bildirmek — ne güzel; övgü bildirir · bu ne güzel · öyleyse ne güzel, yerinde olur
  نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)
- **B004** evet diyerek onaylamak veya söz vermek — evet; doğru; olur · ona evet dedi
  نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)
- **B005** develer ve geniş anlamda otlayan evcil hayvanlar — develer; deve varlığı · deve, sığır ve koyun topluluğu
  النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)
- **B006** devekuşu — devekuşu; erkek veya dişi birey · devekuşu türü veya topluluğu
  النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)
- **B007** devekuşuna benzetilerek ad verilen şeyler — devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol · Ay'ın konak yerlerinden biri
  على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)
- **B008** bir topluluğun dağılıp gücünü yitirmesi [kalıp] — dağıldılar, ayrıldılar veya güçlerini yitirdiler · hızla yola koyulup gittiler · yenilip dağıldılar
  شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)
- **B009** yumuşak esen nemli güney rüzgarı — yumuşak esen nemli güney rüzgarı
  النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)
- **B010** daha da artırmak veya ileri dereceye götürmek — artırdı; daha ileri götürdü · onu iyice ince öğüttü
  فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)
- **B011** bir yeri kendine uygun bulup orada kalmak [kalıp] — bir yere geldi, orayı uygun bulup kaldı
  أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)
- **B012** birine yaya gitmek ve ayakları yürüyerek kullanmak [kalıp] — ona yaya gitti veya onu yürüyerek aradı · ayaklarını yürümekle eskitti; hafif yürüdü
  تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)
- **B013** birini göz sevinci saymak veya bunun için dua etmek [kalıp] — Tanrı seni gözlere sevinç kaynağı kılsın · göz sevinci ve hoşnutluğu
  نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)

## ر ب ب (root_000532): 68:2 رَبِّكَ, 68:7 رَبَّكَ, 68:19 رَّبِّكَ, 68:29 رَبِّنَآ, 68:32 رَبُّنَآ, 68:32 رَبِّنَا, 68:34 رَبِّهِمْ, 68:48 رَبِّكَ, 68:49 رَّبِّهِۦ, 68:50 رَبُّهُۥ

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

## ECHO ر ب و (root_000537): for 68:2 رَبِّكَ, 68:7 رَبَّكَ, 68:19 رَّبِّكَ, 68:29 رَبِّنَآ, 68:32 رَبُّنَآ, 68:32 رَبِّنَا, 68:34 رَبِّهِمْ, 68:48 رَبِّكَ, 68:49 رَّبِّهِۦ, 68:50 رَبُّهُۥ: withheld observed target; not identity

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

## ج ن ن (root_000266): 68:2 بِمَجْنُونٍ, 68:17 ٱلْجَنَّةِ, 68:34 جَنَّٰتِ, 68:51 لَمَجْنُونٌ

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

## ء ج ر (root_000015): 68:3 لَأَجْرًا, 68:46 أَجْرًا

- **B001** iş veya anlaşma karşılığında sağlanan yarar — emeğin karşılığı; dünyalık veya öte dünyaya ilişkin ödül · iş ya da kullanım karşılığında ödenen bedel · iş veya kullanım için bedel karşılığında yapılan kiralama sözleşmesi · bir işin karşılığını vermek · ödüllendirmek, ücret ödemek veya kiraya vermek · ücret karşılığı çalıştırılan kişi · ücret karşılığı çalıştırmak üzere tutmak · onun karşılığında ücret almak · kadınlara evlilik nedeniyle verilen bedeller · belli bir süre onun için çalışmak · çocukları ölüp kendisi için manevi ödüle dönüşmek
  الأجر جزاء العمل (maqayis;ayn)؛ الأجرة الكراء (sihah)؛ الإجارة ما أعطيت من أجر في عمل (maqayis;ayn)؛ مهر المرأة ... فآتوهن أجورهن (maqayis;mufradat)؛ الأجر والأجرة ما يعود من ثواب العمل دنيويا كان أو أخرويا (mufradat)؛ استئجره أي اتخذه أجيرا (tahdhib)
- **B002** kırığın birleştirilip, çoğu kullanımda eğri kaynaması — kırığın eğri ya da çıkıntılı biçimde kaynaması · eli kaynadı, fakat eğrilik veya çıkıntı kaldı · kırığın eğri biçimde kaynaması · kırığı ya da eli eğri veya çıkıntılı kalacak biçimde birleştirmek · uyaklarda denk harfler yerine farklı harfler kullanılması
  جبر العظم الكسير (maqayis)؛ الأجور جبر الكسر على عوج العظم (ayn)؛ أجر العظم ... برأ على عثم (sihah)؛ أجر الكسر ... إذا برأ على اعوجاج (tahdhib)؛ الإجارة ... القافية طاء والأخرى دالا ... من أجور الكسر (tahdhib)
- **B003** çevresi korkuluksuz açık dam — çevresi korkulukla çevrilmemiş dam · çevresi korkulukla çevrilmemiş damlar · korkuluksuz dam anlamındaki zayıf sayılan söyleyiş biçimi
  الإجار سطح ليس حواليه سترة (ayn;tahdhib)؛ الاجار السطح بلغة أهل الشام والحجاز (sihah)؛ ليست من كلام البادية (maqayis)؛ الإنجار لغة والصواب الإجار (tahdhib)

## غ ي ر (root_001119): 68:3 غَيْرَ

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

## م ن ن (root_001449): 68:3 مَمْنُونٍ

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

## خ ل ق (root_000434): 68:4 خُلُقٍ

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

## ع ظ م (root_001029): 68:4 عَظِيمٍ

- **B001** büyük ve güçlü olma; büyük sayıp yüceltme — büyük ve güçlü olmak; değeri yükselmek · büyük, güçlü veya yüce · büyüklük ve yücelik · büyütmek, yüceltmek ve ululamak · gözünde büyütmek veya görkemli göstermek · büyük saymak · Karnın ne kadar büyük! · büyüklük hali
  أصل واحد صحيح يدل على كبر وقوة (maqayis)؛ عظم الشيء عظما فهو عظيم (ayn;sihah;tahdhib)؛ أعظم الأمر وعظمه أي فخمه والتعظيم التبجيل (sihah)؛ عظم الشيء أصله كبر عظمه ثم استعير لكل كبير (mufradat)
- **B002** bir şeyin çoğu veya büyük bölümü [kalıp] — şeyin çoğu · şeyin büyük bölümü · insanların çoğunluğuna katılmak
  ومعظم الشيء أكثره (maqayis)؛ معظم الشيء أكثره والعظم جل الشيء وأكثره (ayn)؛ عظم الشيء أكثره ومعظمه (sihah)؛ عظم الشيء ومعظمه جله وأكبره ودخل في عظم الناس أي في معظمهم (tahdhib)
- **B003** uzvun belirli kalın kesimi [kalıp] — kolun dirseğe yakın kalın bölümü · dilin köke yakın kalın bölümü
  عظمة الذراع مستغلظها (maqayis;sihah;tahdhib)؛ عظمة اللسان مستغلظه فوق العكدة (tahdhib)؛ العظمة ما يلي المرفق من مستغلظ الذراع (tahdhib)؛ عظمة الذراع لمستغلظها (mufradat)
- **B004** ağır ve içinden çıkılmaz felaket — ağır ve korkunç felaket · büyük felaket · içinden çıkılmaz ağır felaket
  العظيمة النازلة الملمة الشديدة (maqayis)؛ العظيمة الملمة النازلة الفظيعة (ayn)؛ العظيمة والمعظمة النازلة الشديدة (sihah)؛ العظمية الملمة إذا أعضلت (tahdhib)؛ العظيمة النازلة (mufradat)
- **B005** kemik — kemik · kemikler
  العَظْم معروف سمي بذلك لقوته وشدته (maqayis)؛ العظام جمع العَظْم وهو قصب المفاصل (ayn)؛ العَظْم واحد العظام (sihah)؛ العَظْم بتسكين الظاء يجمع عظاما (tahdhib)؛ العَظْم جمعه عظام (mufradat)
- **B006** kibirlenip böbürlenme — kibir ve böbürlenme · kibirlenmek ve kurumlanmak · böbürlenmek
  العظمة من التعظم والزهو والنخوة (ayn)؛ استعظم وتعظم تكبر والعظمة الكبرياء (sihah)؛ العظمة التعظم والنخوة والزهو وأما عظمة العبد فهو كبره المذموم وتجبره (tahdhib)
- **B007** yadırgayıp gözünde büyütmek — yadırgamak veya ürkütücü bulmak · iş gözümde büyüdü ve beni ürküttü · söylediğin beni ürküttü · bunu yapmak gözümü korkutmaz
  استعظمته أنكرته ولا يتعاظمني ذلك أي لا يعظم في عيني (ayn)؛ استعظمت الأمر إذا أنكرته وأعظمني أي هالني وعظم علي وما يعظمني أي ما يهولني (tahdhib)
- **B008** kalçayı büyük gösteren dolgu — kalçayı büyük gösteren yastık · kalça dolgusu · kalçayı büyütme dolgusu
  الإعظامة والعظامة كالوسادة تعظم بها المرأة عجيزتها (sihah)؛ العظمة شيء تعظم به المرأة ردفها من مرفقة وغيرها والعظامة بكسر العين (tahdhib)؛ الإعظامة والعظامة شبه وسادة تعظم بها المرأة عجيزتها (mufradat)
- **B009** eyerin donanımsız ahşap iskelet parçası [kalıp] — eyerin kayışsız ve donanımsız ahşap parçası
  عظم الرحل خشبة بلا أنساع ولا أداة (sihah)؛ عظم الرجل خشبة بلا أنساع ولا أداة (tahdhib)؛ عظم الرحل خشبة بلا أنساع (mufradat)
- **B010** şerefli ve saygın bir mevki edinme — görüş ve şan bakımından yükselmek · insanlar arasında saygınlık · saygınlıklar ve dokunulmaz değerler · topluluğun ileri gelenleri
  عظم الرجل عظامة فهو عظيم في الرأي والمجد (ayn)؛ عظمة عند الناس أي حرمة يعظم لها وله معاظم مثله وعظيم المعاظم أي عظيم الحرمة وعظمات القوم سادتهم وذوو شرفهم (tahdhib)

## ب ص ر (root_000121): 68:5 فَسَتُبْصِرُ, 68:5 وَيُبْصِرُونَ, 68:43 أَبْصَٰرُهُمْ, 68:51 بِأَبْصَٰرِهِمْ

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

## ف ت ن (root_001128): 68:6 ٱلْمَفْتُونُ

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

## ع ل م (root_001040): 68:7 أَعْلَمُ, 68:7 أَعْلَمُ, 68:33 يَعْلَمُونَ, 68:44 يَعْلَمُونَ, 68:52 لِّلْعَٰلَمِينَ

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

## ض ل ل (root_000913): 68:7 ضَلَّ, 68:26 لَضَآلُّونَ

- **B001** doğru yoldan ve amaçtan sapma ya da başkasını saptırma — doğru yoldan, amaçtan veya doğruluktan sapmak · doğru yoldan ve doğruluktan sapma · doğru yoldan veya amaçtan sapmış kimse · sapmada direnen, çok sapmış kimse · iyilikten uzak, yanlış ve boş işlere dalmış kimse · asılsız ve yanlış düşünceler · birini doğru yoldan saptırmak · bir kimseyi sapmış saymak · yanlışlığın ve sapmanın içine düşülen yer · yolun bulunamadığı şaşırtıcı arazi · o işi yanlış ve sağduyusuz bir tutumla yapmak
  كل جائر عن القصد ضال؛ الضلال والضلالة بمعنى (maqayis); ضل إذا جار عن القصد؛ لا يوفق لخير صاحب غوايات وبطالات (ayn); الضلال ضد الهدى؛ ضل في الأمر إذا لم يهتد له؛ ضل في الأرض إذا لم يهتد للسبيل (jamhara); الضلال والضلالة ضد الرشاد؛ رجل ضليل ومضلل أي ضال جدا (sihah); الإضلال في كلام العرب ضد الهداية والإرشاد؛ ضل الكافر غاب عن الحجة؛ ضل فلان عن القصد إذا جار (tahdhib)
- **B002** gizlenerek, karışıp eriyerek veya gömülerek gözden yitme — gizlenip gözden kaybolmak · ölüyü gömüp gözden kaldırmak · bir sıvının ötekine karışıp içinde kaybolması · kaya altında güneş görmeyen su
  أضل الميت إذا دفن؛ ضل اللبن في الماء ثم استهلك (maqayis); ضل الشيء إذا خفي وغاب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (jamhara); أضل الميت إذا دفن؛ أضل عنه أي أخفى عليه وأغيب؛ أئذا ضللنا في الأرض أي خفينا وغبنا (sihah); أصل الضلال الغيبوبة؛ ضل الماء في اللبن؛ أضلت بنو قيس عميدها أي دفنته (tahdhib)
- **B003** bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması — bir şeyin kaybolması, yitip gitmesi veya yok olması · devesini ya da başka bir hayvanını kaybetmek · evin, ibadet yerinin ya da başka bir yerin konumunu bulamamak · bir işin elinden kaçması ve ona güç yetirememek · kanı yerde kalmak, öcü alınmamak · yitme veya yok olma
  أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تهتد لهما (maqayis); ضللت مكاني إذا لم تهتد له؛ أضل بعيره إذا أفلت فذهب (ayn); ذهب فلان ضلة إذا لم يدر أين ذهب؛ ذهب دمه ضلة إذا لم يثأر به (jamhara); أضللت بعيري إذا ذهب منك؛ ضللت المسجد والدار إذا لم تعرف موضعهما (sihah); أضللت الشيء إذا ضاع منك؛ ضللت الشيء أضله إذا جعلته في مكان ولم تدر أين هو (tahdhib)
- **B004** bir şeyi unutmak veya bellekte tutamamak [kalıp] — bir şeyi unutmak ya da belleğinde tutamamak
  ضللت الشيء أنسيته (jamhara); إن تضل أي إن تنس؛ أن تضل إحداهما أي تغيب عن حفظها أو يغيب حفظها عنها (tahdhib)
- **B005** sahibi bilinmeyen kayıp hayvan, özellikle deve — sahibi bilinmeyen kayıp hayvan, özellikle deve · sahibi bilinmeyen kayıp hayvanlar veya develer
  الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn); الضالة ما ضل من البهيمة للذكر والأنثى (sihah); الضالة من الإبل التي بمضيعة لا يعرف لها مالك؛ الجميع الضوال (tahdhib)

## س ب ل (root_000672): 68:7 سَبِيلِهِۦ

- **B001** yol ve bir amaca ulaştıran yol — yol; bir şeye ulaştıran bağlantı veya yöntem · yollar, izlenen güzergahlar · dinsel doğruluk ve iyilik yolu
  السبيل وهو الطريق سمي بذلك لامتداده (maqayis)؛ والسبيل يذكر ويؤنث وجمعه سبل (ayn)؛ السبيل معروف تذكر وتؤنث والجمع سبل وهي الطرق (jamhara)؛ السبيل الطريق؛ أي سببا ووصلة (sihah)؛ السبيل الطريق؛ لا يستطيعون في أمرك حيلة (tahdhib)؛ السبيل الطريق الذي فيه سهولة؛ لكل ما يتوصل به إلى شيء (mufradat)
- **B002** yol kullanan kişi veya yolcu — yollarda gidip gelenler · yolu izleyen kişi · evinden uzaktaki veya yolda kalmış yolcu
  السابلة المختلفة في السبل جائية وذاهبة (maqayis)؛ السابلة المختلفة في الطرقات للحوائج (ayn)؛ السابلة هم الذين يسلكون السبل (jamhara)؛ السابلة أبناء السبيل المختلفة في الطرقات (sihah)؛ ابن السبيل المسافر الذي انقطع به (tahdhib)؛ قيل لسالكه سابل؛ وابن السبيل المسافر البعيد عن منزله (mufradat)
- **B003** malı sürekli iyilik kullanımına ayırmak [kalıp] — malı veya taşınmazı sürekli iyilik kullanımına ayırmak · yol gideri olmayan savaş görevlisine ayrılan yardım payı
  سبلت مالا في سبيل الله أي وقفته (ayn)؛ سبل ضيعته أي جعلها في سبيل الله (sihah)؛ حبس الرجل عقدة له وسبل ثمرها أو غلتها فإنه يسلك بما سبل سبل الخير (tahdhib)؛ ادع إلى سبيل ربك؛ قتلوا في سبيل الله (mufradat)
- **B004** aşağı doğru salmak — perdeyi aşağı salmak · yağmak; bulutun suyunu aşağı bırakması · giysiyi veya eteği yere doğru sarkıtmak · atın kuyruğunu aşağı salması · giysisini sürekli yere doğru sarkıtan kişi
  إرسال شيء من علو إلى سفل؛ أسبلت الستر أسبلت السحابة ماءها (maqayis)؛ الفرس أسبل ذنبه والمرأة أسبلت ذيلها؛ رجل مسبال عادته إسبال ثيابه (ayn)؛ أسبلت الستر إسبالا إذا أرخيته؛ أسبل الرجل إزاره (jamhara)؛ أسبل المطر والدمع إذا هطل؛ أسبل إزاره أي أرخاه (sihah)؛ الفرس يسبل ذنبه والمرأة تسبل ذيلها؛ أسبل فلان ثيابه إذا طولها وأرسلها إلى الأرض (tahdhib)؛ أسبل الستر والذيل وفرس مسبل الذنب (mufradat)
- **B005** yağan yağmur — yağmur, özellikle düşmekte olan yağmur · geniş ve bol sağanak
  السبل المطر الجود (maqayis)؛ السبل المطر (ayn)؛ والسبل المطر (jamhara)؛ السبل بالتحريك المطر؛ المطر بين السحاب والأرض (sihah)؛ السبل المطر المسبل؛ السبلة المطرة الواسعة؛ السبل المطر بين السحاب والأرض (tahdhib)؛ سبل المطر وأسبل؛ قيل للمطر سبل ما دام سابلا (mufradat)
- **B006** üst dudak ve sakal önündeki sarkan kıl — üst dudak kılı, bıyık veya sakalın öne sarkan bölümü · üst dudak kılı ya da sakalı uzun olan · ağız kılını yayarak tehdit etmek; bıyıklı kimseleri betimlemek
  سبال الإنسان من هذا لأنه شعر منسدل (maqayis)؛ السبلة ما على الشفة العليا من الشعر (ayn)؛ السبلة ما أسبل من شعر الشارب في اللحية (jamhara)؛ السبلة الشارب والجمع السبال (sihah)؛ السبلة مقدم اللحية وما أسبل منها على الصدر (tahdhib)؛ خص السبلة بشعر الشفة العليا لما فيها من التحدر (mufradat)
- **B007** kap kenarı veya hayvanın boğaz kesim yeri [kalıp] — kovanın dudakları veya kabın üst kenarı · büyükbaş hayvanın boğaz kesim noktası ve çevresi
  لأعالي الدلو أسبال (maqayis)؛ لتب في سبل الناقة إذا طعن في ثغرة نحرها (jamhara)؛ أسبال الدلو شفاهها (sihah)؛ السبلة المنحر من البعير وهو التريبة؛ ملأ الإناء إلى سبلته أي إلى رأسه (tahdhib)
- **B008** tahıl başağı ve başak çıkarmak — tahıl başağı; başaklar · ekinin başak çıkarması veya başaklı hale gelmesi · mısır, pirinç ve benzeri ürünlerin başağı
  سمي السنبل سنبلا لامتداده؛ أسبل الزرع إذا خرج سنبله (maqayis)؛ السبولة سنبلة الذرة والأرز وأسبل الزرع أي سنبل (ayn)؛ أسبل الزرع وسنبل إذا صار فيه السنبل (jamhara)؛ السبل أيضا السنبل؛ أسبل الزرع أي خرج سنبله (sihah)؛ السبولة هي سنبلة الذرة والأرز؛ قد أسبل الزرع إذا سنبل (tahdhib)؛ السنبلة جمعها سنابل؛ أسبل الزرع صار ذا سنبلة (mufradat)
- **B009** eski pay oyunundaki beşinci veya altıncı çubuk — eski pay oyunundaki beşinci veya altıncı çubuk
  المسبل اسم خامس سهام القداح (ayn)؛ المسبل السادس من سهام الميسر (sihah)؛ المسبل من قداح الميسر السادس وفيه ستة فروض (tahdhib)؛ المسبل اسم القدح الخامس (mufradat)
- **B010** kırmızı damarlı ağsı göz perdesi — kırmızı damarlı, ağsı perde oluşturan göz hastalığı
  السبل داء في العين شبه غشاوة كأنها نسج العنكبوت بعروق حمر (sihah)

## ه د ي (root_001583): 68:7 بِٱلْمُهْتَدِينَ

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

## ECHO ه د د (root_001580): for 68:7 بِٱلْمُهْتَدِينَ: withheld observed target; not identity

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

## ط و ع (root_000956): 68:8 تُطِعِ, 68:10 تُطِعْ, 68:42 يَسْتَطِيعُونَ

- **B001** zorlanmadan boyun eğme ve kolay yönlenme — zorlamanın karşıtı olan isteyerek boyun eğme · emre uyma ve gereğini yerine getirme · ona boyun eğdi · emrini yerine getirdi · zorlanmadan uyan kimse · uyan ve boyun eğen kimse · çok söz dinleyen ve kolay uyan kimse · kolay yönlendirilen ve söz dinleyen · elin altında ve tasarrufa hazır · dizginle kolay yönlendirilen · yatak arkadaşına uyum gösteren · dili buna dönmüyor · güçlüklere alışkın ve onları göğüsleyen
  أصل صحيح واحد يدل على الإصحاب والانقياد (maqayis); الطوع نقيض الكره (ayn;tahdhib;mufradat); طاع له إذا انقاد له (ayn;sihah;tahdhib;mufradat); فرس طوع العنان (ayn;sihah;tahdhib); بعير طيع سلس القياد (tahdhib); لسانه لا يطوع بكذا (sihah)
- **B002** taraflar arasında uyum gösterme — ona uyum gösterdi veya onu izledi · taraflar arasında uyum gösterme · uyumlu olma ve kolay söz dinleme niteliği
  لمن وافق غيره قد طاوعه (maqayis); إذا وافقك فقد طاوعك (ayn;tahdhib); الطواعية اسم لما يكون مصدر المطاوعة (ayn;tahdhib); المطاوعة الموافقة (sihah)
- **B003** bir işi yapabilecek güç ve elverişlilik — bir işi yapabilecek güç ve elverişli durum · bir şeyi yapabildi veya yapabilir oldu
  الاستطاعة مشتقة من الطوع (maqayis;ayn); الاستطاعة الإطاقة (sihah); الاستطاعة استفالة من الطوع وذلك وجود ما يصير به الفعل متأتيا (mufradat); يقال ما أستطيع وما اسطيع وما أسطيع وما أستيع (tahdhib)
- **B004** yapabilir hale gelmek için kendini zorlama — işi yapabilir hale gelene kadar kendini zorladı · yapmaya kendini zorladı veya isteyerek üstlendi
  تطاوع لهذا الأمر حتى تستطيعه (maqayis;ayn;sihah;tahdhib); تطوع أي تكلف استطاعته (maqayis;sihah;tahdhib); وتطوع كذا تحمله طوعا (mufradat)
- **B005** yükümlü olmadığı iyiliği gönüllü yapma — yükümlü olmadığı şeyi gönüllü olarak verdi veya yaptı · zorunlu olmayan iyiliği gönüllü yapma · savaş hizmetine gönüllü katılan topluluk
  التبرع بالشيء قد تطوع به (maqayis); لا يقال هذا إلا في باب الخير والبر (maqayis); التطوع ما تبرعت به مما لا يلزمك فريضته (ayn;sihah;tahdhib); المطوعة القوم الذين يتطوعون بالجهاد (ayn;sihah;tahdhib); التطوع في التعارف التبرع بما لا يلزم كالتنفل (mufradat)
- **B006** iç benliğin işi kolay gösterip yöneltmesi — nefsi ona işi kolay gösterdi ve ona yöneltti
  قد تطوع لك طوعا إذا انقاد (ayn); فطوعت له نفسه رخصت وسهلت (sihah); فتابعته نفسه (tahdhib); شجعته (tahdhib); أعانته على ذلك وأجابته إليه (tahdhib); سمحت وسهلت له نفسه (tahdhib); أسمحت له قرينته وانقادت له وسولت (mufradat)
- **B007** otlak veya meyvenin yararlanılabilir hale gelmesi — otlağı bulup ondan istediği kadar yedi · otlak ona genişleyip otlamaya elverişli oldu · meyveli ağaç ürünü olgunlaşıp toplanabilir oldu · otlak ona genişleyip otlamayı mümkün kıldı
  أطاع لها الكلأ إذا أصابت فأكلت منه ما شاءت (ayn); أطاع النخل والشجر إذا أدرك ثمره وأمكن أن يجتنى (sihah); أطاع له المرتع إذا اتسع له وأمكنه من الرعي (sihah;tahdhib); قد يقال في هذا الموضع طاع (tahdhib)

## ECHO س ط ع (root_000706): for 68:8 تُطِعِ, 68:10 تُطِعْ, 68:42 يَسْتَطِيعُونَ: withheld observed target; not identity

- **B001** havada uzama, yükselme veya yayılma — havada yükselmek, uzamak veya yayılmak · yukarı doğru uzanan sabah aydınlığı · sabah aydınlığı · okun göğe yükselip parlaması · misk kokusunun burnuna ulaşması
  أصل يدل على طول الشيء وارتفاعه في الهواء (maqayis)؛ كل شيء ينتشر فينبسط نحو البرق والغبار والريح الطيبة (ayn)؛ سطع الغبار والرائحة والصبح إذا ارتفع (sihah)؛ سطع ضوؤه في السماء والبرق يسطع في السماء وسطع السهم فشخص في السماء وسطعت الرائحة إذا فاحت (tahdhib)
- **B002** boyun uzunluğu — boyun uzunluğu · başını kaldırıp boynunu uzatmak · uzun boyunlu erkek devekuşu · uzun boyunlu dişi devekuşu
  السطع وهو طول العنق وظليم أسطع ونعامة سطعاء (maqayis)؛ السطع طول العنق نعامة سطعاء (sihah)؛ ظليم أسطع إذا كان عنقه طويلا والأنثى سطعاء وفي عنقه سطع أي طول (tahdhib)
- **B003** ev direği — ev veya çadır direği · direğe benzetilen uzun deve
  السطاع عمود من عمد البيت (maqayis)؛ السطاع عمود البيت (sihah)؛ السطاع عمود من أعمدة البيت وللبعير الطويل سطاع تشبيها بسطاع البيت (tahdhib)
- **B004** deve boynundaki uzunlamasına damga — deve boynundaki uzunlamasına damga · boynu uzunlamasına damgalı deve
  السطاع سمة في عنق البعير بالطول يقال بعير مسطع (sihah)؛ السطاع من سمات الإبل في العنق بالطول وناقة مسطوعة وإبل مسطعة (tahdhib)
- **B005** avuç ya da parmak vuruşu ve sesi — bir şeye avuç içiyle veya parmakla vurma · vuruş sesi · vuruş veya vuruş sesi
  السطع ارتفاع صوت الشيء إذا ضربت عليه شيئا يقال سطعة (maqayis)؛ السطع أن تسطع شيئا براحتك أو بإصبعك ضربا وسمعت لضربته سطعا يعني صوت الضربة (tahdhib)
- **B006** belirli bir dağın özel adı — belirli bir dağın özel adı
  أما السطاع في شعر هذيل فهو جبل بعينه (maqayis)؛ السطاع اسم جبل بعينه (tahdhib)

## ك ذ ب (root_001290): 68:8 ٱلْمُكَذِّبِينَ, 68:44 يُكَذِّبُ

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

## و د د (root_001634): 68:9 وَدُّوا۟

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

## د ه ن (root_000497): 68:9 تُدْهِنُ, 68:9 فَيُدْهِنُونَ

- **B001** yağ ve yağla kaplama — sürülebilir yağ · yağlar · yağla kaplamak · kendine yağ sürmek
  الدهن (maqayis;sihah;tahdhib;mufradat)؛ الدهان ما يدهن به (maqayis)؛ الدهان جمع دهن (sihah)؛ تنبت بالدهن وجمع الدهن أدهان (mufradat)؛ دهنته بالدهان وتدهن وادهن (sihah)؛ الدهن الفعل المجاوز والادهان الفعل اللازم (ayn;tahdhib)
- **B002** çıkarcı yumuşama ve içtekini gizleyerek yanaşma — ciddiyeti bırakarak yumuşak ve uzlaşmacı davranma · çıkar gözeten yumuşak davranış ve gizleyici uzlaşma · birine içindekinin tersini göstererek yanaşmak · çıkar için yumuşak davranan ve gerçeği gizleyen kimse
  الإدهان من المداهنة وهي المصانعة (maqayis)؛ داهنت الرجل إذا واربته وأظهرت له خلاف ما تضمر (maqayis)؛ الإدهان اللين والمصانعة (ayn)؛ المداهنة كالمصانعة والإدهان مثله (sihah)؛ الإدهان المقاربة في الكلام والتليين في القول (tahdhib)؛ الإدهان المداراة والملاينة وترك الجد (mufradat)
- **B003** hafif yağmurla yüzeyi azıcık ıslatma — yağmurun yerin yüzünü hafifçe ıslatması · hafif yağmurlar
  دهن المطر الأرض بلها بلا يسيرا (maqayis)؛ الدهن من المطر قدر ما يبل وجه الأرض (ayn;tahdhib)؛ دهن المطر الأرض إذا بلها بلا يسيرا (sihah)؛ الدهان المطر الضعيف (sihah;tahdhib)؛ دهن المطر الأرض بلها بللا يسيرا (mufradat)
- **B004** sopayla, kimi kullanımda hafif ve alaycı biçimde vurma [kalıp] — sopayla vurmak; kimi kullanımda hafif veya alaycı bir vuruş
  دهنه بالعصا دهنا إذا ضربه بها ضربا خفيفا (maqayis)؛ دهنه بالعصا ضربته بها (sihah)؛ دهن غلامه إذا ضربه (ayn;tahdhib)؛ دهنه بالعصا إذا ضربه كما يقال مسحه بالعصا (tahdhib)؛ دهنه بالعصا كناية عن الضرب على سبيل التهكم (mufradat)
- **B005** yağ kabı veya su tutan kaya oyuğu — yağ kabı · suyun biriktiği kaya veya dağ oyuğu
  المدهن ما يجعل فيه الدهن (maqayis;mufradat)؛ المدهن قارورة الدهن (sihah)؛ المدهن نقرة في الجبل يستنقع فيها الماء (maqayis;sihah;tahdhib)؛ مكان يستقر فيه ماء قليل مدهن تشبيها بذلك (mufradat)؛ كل موضع حفره سيل أو ماء واكف في حجر فهو مدهن (ayn)
- **B006** az süt verme ve bundan genişleyen güçsüzlük — az süt veren dişi deve · güçsüz kişi veya iş
  الدهين الناقة القليلة الدر (maqayis)؛ ناقة دهين قليلة اللبن (sihah;tahdhib)؛ ناقة دهين قليلة اللبن لا تدر قطرة (ayn)؛ استعير الدهين للناقة القليلة اللبن (mufradat)؛ رجل دهين ضعيف وأمر دهين (tahdhib)
- **B007** topluluk, yer, mensubiyet ve kişi adları kümesi — bir Arap topluluğunun adı · yumuşak kumlu belirli bir yerin adı · bu yere mensup olan · belirli bir kadının adı
  بنو دهن حي من العرب (maqayis)؛ دهن حي من اليمن (sihah)؛ الدهناء موضع وهو رمل لين والنسبة إليها دهناوي (maqayis)؛ الدهناء موضع ببلاد تميم وينسب إليه دهناوي (sihah)؛ الدهناء موضع كله رمل (ayn)؛ الدهناء من ديار بني تميم (tahdhib)؛ الدهناء بنت مسحل (sihah)
- **B008** kızıl ya da değişken yağ benzeri görünüm — kızıl deri, yağ tortusu veya renk değiştiren kızgın yağ görünümüyle kurulan renk benzetmesi
  فكانت وردة كالدهان هو دردي الزيت (maqayis;mufradat)؛ الدهان الأديم الأحمر (sihah)؛ الدهان في القرآن الأديم الأحمر الصرف (tahdhib)؛ تتلون كما تتلون الدهان المختلفة (tahdhib)؛ كالزيت الذي قد أغلي (tahdhib)
- **B009** şiirde pürüzsüz yol — şiirde geçen pürüzsüz yol
  الدهان الطريق الأملس هاهنا (tahdhib)
- **B010** yağ satıcısı — yağ satıcısı
  الدهان الذي يبيع الدهن (tahdhib)
- **B011** bir toplulukta görülen bolluk izleri [kalıp] — bolluk izleri üzerlerinde görülen topluluk
  قوم مدهنون عليهم آثار النعم (sihah)

## ك ل ل (root_001315): 68:10 كُلَّ

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

## ح ل ف (root_000349): 68:10 حَلَّافٍ

- **B001** ant içme ve ant içirtme — ant içmek · ant içme · tek bir ant · Tanrı adına ant olsun · ant içme eyleminin adı · çok sık ant içen · birinden ant istemek veya ona ant içirtmek
  الحلف والحلف لغتان في القسم (ayn;tahdhib)؛ حلف أي أقسم يحلف حلفا وحلفا ومحلوفا (sihah)؛ الحلف أصله اليمين (mufradat)؛ الحلف يقال حلف يحلف حلفا (maqayis)؛ حلفت له أحلف حلفا وحلفا (jamhara)؛ رجل حلاف كثير الحلف (ayn;jamhara;tahdhib;mufradat)
- **B002** karşılıklı sözleşip bağlanma — topluluklar arası bağlaşma · biriyle karşılıklı sözleşip ona bağlı kalmak · yardımlaşmak üzere karşılıklı sözleşmek · karşılıklı sözleşme ve bağlaşma · bağlaşık veya ayrılmaz yoldaş · cömertlikten ayrılmayan kimse · sıkıntısı ve üzüntüsü ondan ayrılmadı · bağlaşıklar · bağlaşmalarıyla tanınan topluluklar · bağlaşmalarıyla birlikte anılan iki topluluk
  أصل واحد وهو الملازمة (maqayis)؛ حالف فلان فلانا إذا لازمه (maqayis)؛ بينهما حلف لأنهما تحالفا بالأيمان (ayn;tahdhib)؛ الحلف بالكسر العهد يكون بين القوم (sihah)؛ تحالف القوم محالفة على النصرة (jamhara)؛ الحلف العهد بين القوم والمحالفة المعاهدة (mufradat)؛ الأحلاف أسد وغطفان (sihah)؛ الحليفان أسد وغطفان (jamhara)
- **B003** üzerine karşıt antlar içilen tartışmalı şey — üzerine karşıt antlar içilen tartışmalı şey · ergenliğe erişip erişmediği tartışılır oldu · rengi iki tür arasında tartışmalı at · kimliği başka bir yıldızla karıştırılıp üzerine ant içilen iki yıldız · hörgücünde yağ olup olmadığı bilinmeyen deve · izlerinin silinip silinmediği tartışılan yıkıntılar
  هذا شيء محلف إذا كان يشك فيه فيتحالف عليه (maqayis)؛ أحلف الغلام جاوز رهاق الحلم فهو محلف (ayn)؛ حضار والوزن محلفان (sihah;tahdhib)؛ كميت محلفة (sihah;tahdhib;mufradat)؛ ناقة محلفة السنام (tahdhib)؛ أطلال محلفة الرسوم (tahdhib)؛ شيء محلف يحمل الإنسان على الحلف (mufradat)
- **B004** dilde etkili, mızrak ucunda keskin [kalıp] — dili keskin, düzgün ve etkili konuşan · ucu keskin mızrak
  حليف اللسان إذا كان حديده (maqayis)؛ رجل حليف اللسان إذا كان حديد اللسان فصيحا (jamhara;sihah)؛ سنان حليف أي حديد (jamhara;tahdhib)
- **B005** belirli bir bitki türü — belirli bir bitki türü · bu bitkinin tek bir bireyi · bu bitkilerin oluşturduğu topluluk
  الحلفاء نبت الواحدة حلفاءة (maqayis)؛ الحلفاء نبات حمله قصب النشاب الواحدة حلفة (ayn;tahdhib)؛ الحلفاء هذا النبت الواحدة حلفة (jamhara)؛ الحلفاء نبت في الماء (sihah)
- **B006** bağırıp çağıran kadın köle — bağırıp çağıran kadın köle
  الحلفاء الأمة الصخابة (tahdhib)

## م ه ن (root_001453): 68:10 مَّهِينٍ

- **B001** değersizlik, güçsüzlük ve azlık — değersiz, güçsüz ve yetersiz · değersizlik ve azlık · güçsüz kimseler
  أصل صحيح يدل على احتقار وحقارة في الشيء (maqayis)؛ مهين أي حقير (maqayis;sihah)؛ رجل مهين أي حقير ضعيف (ayn;tahdhib)؛ المهانة الحقارة (maqayis)؛ المهانة وهي القلة (tahdhib)
- **B002** hizmet etme veya işte ustalık — hizmet; işte ustalık · onlara hizmet etti · hizmet eden kimse veya köle · kendi toprağında çalıştı · ailesine hizmet edip kendini onların işlerine verdi
  المهن الخدمة والمهنة (maqayis)؛ المهنة الخدمة (ayn;sihah;tahdhib)؛ المهنة الحذاقة في العمل ونحوه (ayn;tahdhib)؛ الماهن الخادم (maqayis;sihah)؛ الماهن العبد (ayn;tahdhib)؛ مهنهم أي خدمهم (ayn;tahdhib)؛ مهن القوم يمهنهم مهنة أي خدمهم (sihah)؛ إذا عمل في ضيعته (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)
- **B003** giysiyi çekmek [kalıp] — giysiyi çekti · çekilmiş giysi
  مهنت الثوب جذبته وثوب ممهون (maqayis)
- **B004** develeri sağmak, özellikle dönüş vaktinde [kalıp] — develeri dönüş vaktinde sağdı
  مهنت الإبل حلبتها (maqayis)؛ مهنت الإبل أمهنها إذا جلبتها عند الصدر (ayn)؛ مهنت الإبل مهنة إذا حليتها عن الصدر (sihah)؛ مهنت الإبل مهنة إذا حلبها عند الصدر (tahdhib)
- **B005** kullanıma koşup yıpratma veya güçten düşürme — onu kullanıp değerden düşürdü · onu güçsüzleştirdi · kendini hizmet için kullandı · var olan koşu gücünü sonuna kadar kullandı ve tüketti · ailesine hizmet edip kendini onların işlerine verdi
  امتهنت الشئ ابتذلته (sihah)؛ أمهنته أضعفته (sihah)؛ امتهن نفسه أي مستخدم (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)؛ أخرج ما عنده من العدو وابتذله (tahdhib)
- **B006** üreme sıvısı yetersiz olduğu için dölleyemeyen — üreme sıvısı az ve güçsüz olduğu için dölleyemeyen erkek hayvan
  للفحل من الإبل والغنم إذا لم يلقح من مائه مهين (tahdhib)؛ من ماء قليل ضعيف (tahdhib)

## ه م ز (root_001600): 68:11 هَمَّازٍ

- **B001** elle bastırıp sıkma — bir şeyi bastırıp sıkma veya ezme · bir şeyi avucunda bastırıp sıkmak · başı bastırıp ezecek kadar sıkmak
  تدل على ضغط وعصر (maqayis)؛ همزت الشيء في كفي (maqayis;sihah;mufradat)؛ الهمز كالعصر (mufradat)؛ همزت رأسه وهمزت الجوز بكفي (tahdhib)
- **B002** sesi baskılı biçimde çıkarma — konuşmada sesi baskılı biçimde çıkarma · sesi sıkıştırarak belirgin çıkarmak · sesin baskılı ve sıkışmış biçimde çıkması
  الهمز في الكلام كأنه يضغط الحرف (maqayis)؛ ومنه الهمز في الكلام لأنه يضغط وقد همزت الحرف فانهمز (sihah)؛ ومنه الهمز في الحرف (mufradat)
- **B003** itme, vurma veya dürtme — onu itti veya vurdu · oku güçlü biçimde ileri süren yay · binicinin hayvanı dürtmek için topuğunda kullandığı metal araç
  قوس همزي شديدة الدفع للسهم (maqayis)؛ همزه أي دفعه وضربه (sihah)؛ قوس همزى أي شديدة الدفع للسهم والمهمز والمهماز حديدة في مؤخر خف الرائض (sihah)؛ همزته ولمزته ولهزته ونهزته إذا دفعته (tahdhib)؛ كل شيء دفعته فقد همزته (tahdhib)؛ من النخس والغمز (tahdhib)
- **B004** ayıplama ve çekiştirme — insanları ayıplama veya arkalarından kötüleme · kusur bulan veya başkalarını kötüleyen kimse · sürekli kusur bulan veya arkadan kötüleyen kimse · ayıplayan veya çekiştiren kimse · bir insanı arkasından kötülemek veya ayıplamak · yakınını arkasından ayıplayıp kötülemek
  الهماز العياب وكذا الهمزة (maqayis)؛ الهمز مثل اللمز والهامز والهماز العياب والهمزة مثله (sihah)؛ الهماز المغتابون في الغيب واللماز المغتابون في الحضرة (tahdhib)؛ الهمز العيب (tahdhib)؛ الهماز والهمزة الذي يهمز أخاه في قفاه من خلفه (tahdhib)؛ همز الإنسان اغتيابه (mufradat)
- **B005** şeytanın kalbe kötü düşünce veya ağır etki salması [kalıp] — şeytanın insanın kalbine düşürdüğü kötü düşünceler · şeytanın kalbi bastıran, delilik veya içten dürtme gibi açıklanan etkisi
  همز الشيطان كالموتة تغلب على قلب الإنسان (maqayis)؛ همزات الشيطان خطراته التي يخطرها بقلب الإنسان (sihah)؛ أما همزه فالموتة والموتة الجنون وإنما سماه همزا لأنه جعله من النخس والغمز (tahdhib)؛ أعوذ بك من همزات الشياطين (mufradat)

## م ش ي (root_001427): 68:11 مَّشَّآءٍۭ

- **B001** yürümek; iradeyle bir yerden başka bir yere ilerlemek — yürümek, hareket ederek ilerlemek · yürüyüş biçimi · yürüme · yürütmek · yürütmek
  أصل يدل على حركة الإنسان وغيره (maqayis)؛ المشية ضرب من المشي (ayn;tahdhib)؛ مشى يمشي مشيا (maqayis;sihah;tahdhib)؛ المشي الانتقال من مكان إلى مكان بإرادة (mufradat)
- **B002** bağırsakları boşaltan ilaç ve bu ilacın yol açtığı boşalma — bağırsakları boşaltan ilaç · bağırsakları boşaltan ilaç; bu ilacı içme ve bağırsakların boşalması · bağırsakları boşaltan ilaç · bağırsakları boşaltan ilacı içmek · ilacın onun bağırsaklarını boşaltması · ilaç bağırsaklarımı boşalttı · ilacı içtikten sonra bağırsakları çokça boşalmak
  شربت مشوا ومشيا وهو الدواء الذي يمشي (maqayis)؛ المشاء الدواء الذي يسهل وهو المشو والمشي واستطلاق البطن (ayn;tahdhib)؛ شربت مشوا ومشيا وهو الدواء الذي يسهل واستمشيت وأمشاني الدواء (sihah)؛ يكنى به عن شرب المسهل (mufradat)
- **B003** artma ve üreme yoluyla çoğalma; sürü hayvanı — çoğalma ve bol yavru verme · sürü hayvanları; özellikle koyun, deve ve sığırlar · sürü hayvanları · çok çocuklu kadın · çok yavrulu dişi deve · sürüsü çoğalmak · sürü hayvanlarının yavruları çoğalmak · kadının çocukları çoğalmak · bol yavrulu ve çok sürü hayvanlı kişi
  النماء والزيادة (maqayis)؛ المشاء النتاج الكثير وبه سميت الماشية وامرأة ماشية كثر ولدها وأمشي الرجل كثرت ماشيته (maqayis)؛ فعل الماشية وذو مشاء وماشية وأمشى فلان كثرت ماشيته (ayn;tahdhib)؛ مشت المرأة مشاء إذا كثر ولدها وكذلك الماشية وناقة ماشية كثيرة الأولاد والماشية معروفة (sihah)؛ المشاء النماء وأصل الشاء النماء والكثرة والتناسل وكل مال يكون سائمة للنسل والقنية فهو ماشية (tahdhib)؛ الماشية الأغنام وامرأة ماشية كثر أولادها (mufradat)
- **B004** insanlar arasında kötüleyici söz taşımak [kalıp] — insanlar arasında kötüleyici söz taşımak · durmadan kötüleyici söz taşıyan kimse
  مشى يمشي بالنمائم (tahdhib)؛ يكنى بالمشي عن النميمة (mufradat)
- **B005** içkinin yakıcı etkisinin kişinin içine yayılması [kalıp] — içkinin yakıcı etkisi bedenine yayıldı
  تمشت فيه حميّا الكأس (sihah)
- **B006** yenilen havuç — havuç
  المشاء الجزر الذي يؤكل وهو الإصطفلين (tahdhib)

## ن م م (root_001557): 68:11 بِنَمِيمٍ

- **B001** karnında su kalmamış develer [kalıp] — karınlarında su kalmamış develer
  إبل نمة لم يبق في أجوافها الماء (maqayis)
- **B002** söz taşıma ve söz taşıyan kimse — duyduğu sözü çekiştirme amacıyla başkasına aktarmak · sözü çekiştirme amacıyla başkasına aktarma · söz taşıma · söz taşıma · söz taşıyan kimse · duyduğu sözleri taşıyan kimse
  النمام منه لأنه لا يبقي الكلام في جوفه ورجل نمام (maqayis)؛ نم ينم نما ونميمة ورجل نمام وهو القتات (jamhara)؛ نم الحديث ينمه نما أي قته والاسم النميمة والرجل نم ونمام أي قتات (sihah)؛ الفعل نم ينم نما ونميما ونميمة والنعت نمام (tahdhib)؛ النم إظهار الحديث بالوشاية والنميمة الوشاية ورجل نمام (mufradat)
- **B003** kişiyi ele veren hafif ses ya da hareket belirtisi — belli belirsiz ses, fısıltı ya da hafif hareket · kişiyi ele veren hareket belirtisi · bir şeyden duyulan hafif ses · bir şeyin belli belirsiz sesi
  النميمة الصوت والهمس لأنهما ينمان على الإنسان واسكت الله نامته ما ينم عليه من حركته (maqayis)؛ سمعت نمة الشيء ونميمته إذا سمعت حسه (jamhara)؛ النميمة أيضا الهمس والحركة ومنه أسكت الله نامته (sihah)؛ النميمة صوت الكتابة ووسواس همس الكلام والصوت الخفي من حركة شيء أو وطء قدم (tahdhib)؛ أصل النميمة الهمس والحركة الخفيفة ومنه أسكت الله نامته (mufradat)
- **B004** kokusuyla kendini belli eden hoş kokulu bitki — kokusuyla kendini belli eden hoş kokulu bitki
  النمام ريحان يدل عليه رائحته (maqayis)؛ النمام نبت طيب الرائحة (sihah)؛ النمام نبت ينم عليه رائحته (mufradat)
- **B005** orada hiç kimse yok — orada hiç kimse yok
  ما بها نمي أي أحد كأنهم يريدون ذو حركة تدل عليه (maqayis)؛ وما بها نمي أي ما بها أحد (sihah)
- **B006** bakır ya da karışımlı eski para — bakır para veya kurşun ya da bakır karışımlı gümüş para · bu para türünden tek bir tane
  قولهم للفلس نمي ليس عربيا (maqayis)؛ النمى بالضم الفلس بالرومية والدرهم الذى فيه رصاص أو نحاس والواحدة نمية (sihah)
- **B007** sık kısa çizgilerle bezeme — bir şeyi ince desenlerle bezemek · birbirine yakın kısa çizgilerden oluşan desen · ince desenlerle bezenmiş
  النمنمة مقاربة الخطوط (maqayis)؛ نمنم الشيء تمنمة أي رقشه وزخرفه وثوب منمنم أي موشى (sihah)؛ النمنمة خطوط متقاربة قصار ولكل وشي نمنمة وكتاب منمنم منقش (tahdhib)؛ النمنمة خطوط متقاربة لقلة الحركة من كاتبها في كتابته (mufradat)
- **B008** zemin renginden ayrılan küçük renk izi — tırnaklardaki küçük beyazlıklar · tırnaktaki tek bir beyaz benek · gençlerin tırnaklarındaki beyazlık · koyu zeminde açık ya da açık zeminde koyu küçük parıltı
  النمنم البياض يكون على الأظفار الواحد نمنمة (maqayis)؛ البياض الذي يكون على أظفار الأحداث تمنمة (sihah)؛ النمنم البياض الذي يكون على أظفار الأحداث والواحدة نمنمة والنمة اللمعة من بياض في سواد أو سواد في بياض (tahdhib)
- **B009** bazı dillerde küçük karınca — bazı dillerde küçük karınca
  النملة الصغيرة في بعض اللغات تسمى النمة (jamhara)

## م ن ع (root_001448): 68:12 مَّنَّاعٍ

- **B001** vermeme ve esirgeme — vermenin karşıtı olarak vermeme ve esirgeme · vermeyen veya verilecek şeyi elinde tutan · iyiliği sürekli esirgeyen çok cimri kişi · başkasına vermeyen, cimrice elinde tutan kişi · yalnızca vermemeyi hak edenden esirgeyen ve adaletle veren
  خلاف الإعطاء (maqayis;sihah)؛ ضد العطية (mufradat)؛ رجل منوع ومناع إذا كان بخيلا ممسكا (tahdhib)؛ مناع للخير (tahdhib;mufradat)
- **B002** isteğinden alıkoyma — onu istediği şeyden alıkoymak · seni bunu yapmaktan ne alıkoydu? · önüne engel çıkınca geri durmak
  منعته أمنعه منعا فامتنع أي حلت بينه وبين إرادته (ayn)؛ منعت الرجل عن الشئ فامتنع منه (sihah)؛ المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)؛ ما الذي صدك وحملك على ترك ذلك (mufradat)
- **B003** erişilmez kılan koruyucu güç — inananları çevreleyip koruyan ve destekleyen · gücü ve koruması sayesinde erişilemez · koruyucu güç, saygınlık ve destekçiler · saygınlık ve güçlü koruma içinde
  مكان منيع وهو في عز ومنعة (maqayis)؛ رجل منيع لا يخلص إليه وهو في عز ومنعة (ayn)؛ مكان منيع وقد منع مناعة؛ المنعة جمع مانع أي من يمنعه من عشيرته (sihah)؛ يحوطهم وينصرهم؛ في قوم يمنعونه ويحمونه (tahdhib)؛ يقال في الحماية ومنه مكان منيع وفلان ذو منعة (mufradat)
- **B004** cinsel ahlaksızlığa yanaşmayan kadın [kalıp] — cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın · ahlak dışı cinsel ilişkiyi kabul etmeyen kadın
  امرأة منيعة متمنعة لا تؤاتى على فاحشة (ayn)؛ امرأة منعة متمنعة لا تؤاتى على فاحشة (tahdhib)؛ امرأة منيعة كناية عن العفيفة (mufradat)
- **B005** Engelle! — Engelle!
  مناع بمعنى امنع (ayn)؛ مناع أي امنع كقولهم نزال أي انزل (mufradat)
- **B006** bir şey üzerinde karşılıklı engelleşme — bir şey üzerinde onunla karşılıklı engelleşmek
  مانعته الشئ ممانعة (sihah)
- **B007** çetin yıla direnen genç dişi deve ile dişi oğlak — gençlikleriyle çetin yıla direnen ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak · çetin yıla karşı koyan ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak
  المتمنعان البكرة والعناق تمتنعان على السنة بفتائهما (sihah)؛ المتمنعتان البكرة والعناق تمنعان على السنة لفنائهما (tahdhib)؛ المقاتلتان للزمان عن أنفسهما (sihah;tahdhib)

## خ ي ر (root_000452): 68:12 لِّلْخَيْرِ, 68:32 خَيْرًا, 68:38 تَخَيَّرُونَ

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

## ع د و (root_000993): 68:12 مُعْتَدٍ

- **B001** hakkı aşan saldırganlık — uygun sınırı aşma · açık haksızlık ve saldırganlık · hakkı çiğneyerek sınırı aşma · sınırı aşan haksızlık · ona saldırıp malını alma ya da onu vurma · baskın yapan atlılar
  التعدي تجاوز ما ينبغي أن يقتصر عليه (maqayis;ayn)؛ العدوان الظلم الصراح (maqayis;sihah)؛ الاعتداء مجاوزة الحق (mufradat)؛ العادية الخيل المغيرة (ayn;sihah)
- **B002** yaya ya da atla koşma — yaya koşu ya da at koşusu · koşmak · atın iyi ve çok koşması
  العَدْو هو الحضر (maqayis;ayn;sihah)؛ يقال من عدو الفرس عدوان أي جيد العدو وكثيره (maqayis)؛ بالمشي فيقال له العدو (mufradat)
- **B003** düşmanlık ve düşman — düşman, dostun karşıtı · düşmanlar · düşmanlar · düşmanlık
  العَدُوّ ضد الولي والجمع الأعداء (sihah)؛ العداوة والمعاداة (sihah;mufradat)؛ يقال للواحد والاثنين والجمع عَدُوّ (maqayis)
- **B004** aşma, dışarıda bırakma ve öteye geçirme — belirtilen ögeyi kapsam dışında tutma · konuyu geçip başkasına yönelme · eylemin etkisini nesneye geçirme
  ما عدا زيدا أي ما جاوز زيدا (maqayis;ayn)؛ عدا فعل يستثنى به (sihah)؛ ما عدا كذا يستعمل في الاستثناء (mufradat)؛ عد عن هذا الأمر أي تجاوزه وخذ في غيره (maqayis)
- **B005** yetkiliden hakkını almasını isteme — yetkiliden yardım ve hakkını almasını isteme
  العَدْوى طلبك إلى وال أو قاض أن يعديك على من ظلمك (maqayis)؛ طلبك إلى وال ليعديك على من ظلمك (ayn;sihah)
- **B006** hastalığın bulaşması — hastalığın bulaşması · hastalığın birinden ötekine geçmesi
  العَدْوى ما يقال إنه يعدي من جرب أو داء (maqayis;ayn)؛ ما يعدي من جرب أو غيره ومجاوزته من صاحبه إلى غيره (sihah)
- **B007** işten alıkoyan uğraş veya engel — işten alıkoyan uğraş veya kötü olay · zamanın getirdiği engeller ve sıkıntılar · bir iş beni senden alıkoydu
  العادية شغل من أشغال الدهر يعدوك عن أمرك (maqayis;ayn)؛ عوادي الدهر عوائقه (sihah)؛ عدواء الشغل موانعه (sihah)
- **B008** iki avı peş peşe ele geçirme — iki avı peş peşe izleyip ele geçirme
  العِداء أن يعادي الفرس أو الكلب أو الصياد بين صيدين (maqayis)؛ العِداء الموالاة بين الصيدين (sihah)؛ فعادى عداء بين ثور ونعجة أي أعدى أحدهما إثر الآخر (mufradat)
- **B009** boyunca uzanan yan ve kıyı — bir şeyin eni ya da boyu boyunca uzanan yanı · ırmak kıyısı boyunca uzanan yan · vadinin yanı ve kıyısı
  العَداء طوار كل شيء (maqayis;sihah)؛ لزمت عداء النهر وطريق يأخذ عداء الجبل (maqayis)؛ العدوة جانب الوادي وحافته (sihah)؛ بالعدوة الدنيا أي الجانب المتجاوز للقرب (mufradat)
- **B010** sert, kuru ve engebeli yer — sert, kuru ve engebeli yer
  العَدْواء الأرض اليابسة الصلبة (maqayis)؛ العدواء المكان الذي لا يطمئن من قعد عليه (sihah)؛ مكان ذو عدواء أي غير متلائم الأجزاء (mufradat)
- **B011** develerin otladığı yaz yeşermesi — bahar geçince yeşeren ve develerin otladığı yaz bitkisi
  العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر فترعاه الإبل (maqayis)؛ العَدَوِيّة من نبات الصيف بعد ذهاب الربيع يخضر صغار الشجر فترعاه الإبل (sihah)
- **B012** eğrilik ve güçlük — eğrilik ve güçlük
  العَنْدَأْوَة التواء وعسر وهو من العداء (maqayis)

## ECHO ع د د (root_000989): for 68:12 مُعْتَدٍ: withheld observed target; not identity

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

## ECHO ع و د (root_001058): for 68:12 مُعْتَدٍ: withheld observed target; not identity

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

## ء ث م (root_000013): 68:12 أَثِيمٍ

- **B001** gecikme ve iyilikten geri bırakan suç — geri kalan veya ağır ilerleyen dişi deve · günah; iyilikten ve ödülden geri bırakan kötü eylem · günah veya günaha düşülen yer · günaha girmek · günah işleyen veya günah yükünü taşıyan kimse · günahla nitelenen kimse · çok günah işleyen veya ahlaksız kimse · çokça günah işleyen kimse · günah veya ödülden geri bırakan eylemler
  أصل واحد وهو البطء والتأخر (maqayis)؛ ناقة آثمة أي متأخرة (maqayis)؛ ناقة آثمة ونوق آثمات أي مبطئات (sihah)؛ الإثم مشتق من ذلك لأن ذا الإثم بطيء عن الخير (maqayis)؛ الأثم الذنب (sihah)؛ أثم فلان يأثم إثما أي وقع في الإثم (sihah;tahdhib;ayn)؛ الإثم والأثام اسم للأفعال المبطئة عن الثواب (mufradat)؛ الأثيم والأثام والأثيمة في كثرة ركوب الإثم والآثم الفاعل (ayn)
- **B002** günahtan sakınma ve günah yükünden çıkma — günahtan sakınmak, ondan geri durmak veya günahından sıyrılmak
  فإذا تحرج وكف قيل تأثم (maqayis)؛ تأثم أي تحرج عنه وكف (sihah)؛ تأثم أي تحرج من الإثم وكف عنه (tahdhib;ayn)؛ وتأثم خرج من إثمه (mufradat)
- **B003** günahın cezası ve karşılığı — günahın cezası, karşılığı veya azabı · günahının karşılığını görmüş veya cezalandırılmış kimse
  الأثام جزاء الإثم (sihah)؛ الأثام في جملة التفسير عقوبة الإثم (tahdhib;ayn)؛ تأويل الأثام المجازاة (tahdhib)؛ يلق أثاما أي عذابا (mufradat)؛ العبد مأثوم أي مجزي جزاء إثمه (tahdhib)
- **B004** günah sayma, günaha sokma, suçlama veya cezalandırma — bir davranışın kişiye günah sayılması veya kişinin günahının karşılığını görmesi · birini günaha sokmak · birine günah işlediğini söylemek veya onu günahla suçlamak
  أثمه الله أي عده عليه إثما (sihah)؛ آثمه أوقعه في الإثم (sihah)؛ آثمه بالتشديد أي قال له أثمت (sihah)؛ أثمه الله أي جازاه جزاء الإثم (tahdhib)؛ فعل ما يؤثمه (mufradat)
- **B005** şarap için tartışmalı ad — 
  أن الإثم الخمر (maqayis)؛ وقد تسمى الخمر إثما (sihah)؛ الإثم من أسماء الخمر (tahdhib)؛ وليس الإثم في أسماء الخمر بمعروف ولم يصح فيه بيت صحيح (tahdhib)؛ ولا أعلم كيف صحته (maqayis)

## ع ت ل (root_000980): 68:13 عُتُلٍّۭ

- **B001** zorla çekme, itme ve sürme — birini giysisinden ya da bir şeyi kavrama yerlerinden tutup zorla çekme, itme ve sürme · onu sertçe çekip kendine doğru sürükledi · onu zorla çekip iterek hapse, eziyete veya sıkıntıya götürdü · deveyi yularından tutup sertçe çekerek götürdü
  فتعتله أي تجره إليك بقوة وشدة (maqayis)؛ تجره إليك وتذهب به إلى حبس أو عذاب (ayn;tahdhib)؛ جذبته جذبا عنيفا (jamhara;sihah)؛ الدفع والإرهاق بالسوق العنيف (tahdhib)؛ الأخذ بمجامع الشيء وجره بقهر كعتل البعير (mufradat)
- **B002** güçlü ve sağlam yapılı ya da kaba ve sert kimse — güçlü ve sağlam yapılı adam · kaba ve sert adam · obur ve elindekini vermeyen adam · kötülüğe çabuk yönelmek · kaba ve sert kimse
  الرجل العتل وهو الشديد القوي المصحح الجسم (maqayis)؛ رجل عتل أي أكول منوع (ayn;tahdhib;mufradat)؛ جافيا غليظا وكل جاف عتل (jamhara)؛ الغليظ الجافي وسريع إلى الشر (sihah;tahdhib)؛ الشديد الخصومة والجافي الخلق اللئيم الضريبة (tahdhib)
- **B003** ağır kazı, sökme ve vurma aracı — kazma, sökme veya marangozlukta kullanılan demir ya da tahta araç · kalın tahta sopa · yassı başlı, uzun ve kalın demir çubuk
  العتلة التي يحفر بها والعتلة أيضا الهراوة الغليظة من الخشب (maqayis)؛ حديدة كحد فأس عريضة يحفر بها الأرض والحيطان وعصا من حديد ضخمة طويلة والهراوة الغليظة من الخشب (ayn;tahdhib)؛ المجثاث وهي الحديدة التي يقلع بها فسيل النخل (jamhara)؛ بيرم النجار والمجتاب والهراوة الغليظة (sihah;tahdhib)
- **B004** güç ve şiddet; kalın kargı, Fars yayı, büyük toprak kesesi ve ağır hastalık — kalın kargı · Fars yayları · Fars yaylarından biri · yerden sökülen büyük toprak kesesi · ağır hastalık
  أصل صحيح يدل على شدة وقوة في الشيء (maqayis)؛ رمح عتل غليظ (jamhara;sihah)؛ العتل القسي الفارسية وواحدتها عتلة (sihah;tahdhib)؛ المدرة الكبيرة تتقلع من الأرض (tahdhib)؛ داء عتيل شديد (tahdhib)
- **B005** seninle gelmeyi ve sana uymayı reddetme — Seninle gelmem, sana uymam ve yerimden ayrılmam. · Seninle bir adım bile gelmem; yerimden ayrılmam.
  لا أنعتل معك أي لا أنقاد معك (maqayis;ayn)؛ لا أنعتل معك أي لا أبرح مكاني (sihah)؛ لا أتعتل معك شبرا أي لا أبرح مكاني ولا أجيء معك (tahdhib)
- **B006** ücretli işçi veya hizmet görevlisi — ücretli işçi veya hizmetçi · görevli hizmet eri
  جديلة طيئ تقول للأجير عتيل والجمع عتلاء (sihah)؛ العتيل الأجير بلغة طيء وجمعه العتلاء (tahdhib)؛ العاتل الجلواز وجمعه عتل والعتيل الخادم (tahdhib)
- **B007** gebe kalmayıp gücünü koruyan dişi deve — gebe kalmadığı için gücünü sürekli koruyan dişi deve
  العتلة الناقة التي لا تلقح فهي قوية أبدا (sihah)

## ب ع د (root_000131): 68:13 بَعْدَ

- **B001** uzak olma — yerde veya anlamda uzaklik · uzak, yakin olmayan · uzak yer veya uzak akrabalik · uzak saymak ya da uzaklasmak
  البعد خلاف القرب (maqayis;sihah;mufradat)؛ بعد يبعد بعدا فهو بعيد (ayn;jamhara;tahdhib)؛ يقال ذلك في المحسوس وفي المعقول (mufradat)؛ بيننا بعدة من الأرض والقرابة (sihah)
- **B002** sonra gelme — sonra, oncekinin ardindan gelen · sonradan, ondan sonra · bundan sonra soz gecisi
  بعد ضد قبل (ayn;jamhara;sihah)؛ من بعد كما تقول في خلافه من قبل (maqayis)؛ بعد كلمة دالة على الشيء الأخير (tahdhib)؛ وما خلف بعقبه فهو من بعده (ayn)؛ يقال في مقابلة قبل (mufradat)
- **B003** uzaklastirma — uzaklastirmak veya arayi acmak · uzaklastirmak, kovmak ya da uzaklara gitmek · uzaklastirma, karsilikli uzak durma
  باعدته مباعدة وأبعده الله نحاه عن الخير وباعد الله بينهما (ayn)؛ والبعاد مصدر باعدته مباعدة وبعادا (jamhara)؛ وأبعده غيره وباعده وبعده تبعيدا (sihah)؛ باعد بين أسفارنا (ayn;tahdhib)؛ أبعد فلان في الأرض إذا أمعن فيها (tahdhib)
- **B004** yikim bedduasi — yok olmak ya da beddua anlamina gelmek · kahrolsun, yok olup gitsin · onu iyilikten uzak kilsin diye beddua etmek · hain veya dislanmis kotu kisi
  البعد والبعد الهلاك (maqayis;sihah)؛ بعدت ثمود أي هلكت (maqayis;mufradat)؛ بعدا وسحقا (ayn;tahdhib)؛ أبعده الله أي لا يرثى له (tahdhib)؛ بعد يبعد بعدا من قولهم أبعده الله (jamhara)
- **B005** uzak yakinlar — uzak akrabalar veya uzak kimseler · uzak kimseler, yakin cevre disindakiler
  الأباعد خلاف الأقارب (maqayis;tahdhib)؛ الأبعد ضد الأقرب والجمع أقربون وأبعدون وأباعد وأقارب (ayn)؛ فلان من قربان الأمير ومن بعدانه (sihah)؛ إذا لم تكن من قربان الأمير فكن من بعدانه (tahdhib)
- **B006** uzak degil kalibi — kucuk dusmus degil · uzak degil, yakin sayilir
  تنح غير باعد أي غير صاغر وتنح غير بعيد أي كن قريبا (maqayis;sihah;tahdhib)؛ فلان غير بعيد وغير بعد (jamhara)؛ هم مني غير بعد أي ليسوا ببعيد (tahdhib)
- **B007** aralikli gorusme — aradan sonra ve araliklarla
  لقيته بعيدات بين (sihah;tahdhib)؛ إذا كان الرجل يمسك عن إتيان صاحب الزمان ثم يأتيه (sihah)؛ بعد حين ثم أمسكت عنه ثم أتيته (tahdhib)
- **B008** derin gorusluluk — derin ve tedbirli gorus sahibi
  إنه لذو بعدة أي ذو رأي وحزم؛ رجل ذو بعدة إذا كان نافذ الرأي ذا غور وذا بعد رأي
- **B009** faydasizlik — faydasi yok, hayir yok
  رجعت بغير أبعد أي بغير منفعة؛ ما عندك أبعد؛ إنك لغير أبعد أي لا خير فيك ليس لك بعد مذهب
- **B010** dusmanlikta ileri gitme — dusmanlikta ileri giden kisi
  ذا البعدة الذي يبعد في المعاداة

## ز ن م (root_000647): 68:13 زَنِيمٍ

- **B001** bağlandığı yerden sarkan veya çıkıntı yapan parça — kulak ya da boğazdan sarkan et parçası veya kesilip asılı bırakılan damga parçası · okun arka ucundaki iki yarık ve bunların çıkıntılı kenarları
  أصل يدل على تعليق شيء بشيء (maqayis)؛ زنمتا العنز من الأذن (ayn;tahdhib)؛ زنمتا الفوق من السهم (ayn;tahdhib)؛ الزنمة اللحمة المتدلية في الحلق (maqayis;ayn;tahdhib)؛ الزنمة شيء يقطع من أذن البعير فيترك معلقا (sihah)؛ الزنمة سمة تحز ثم تترك (ayn)؛ الزنمتان من الشاة المتدليتان من أذنها ومن الحلق (mufradat)
- **B002** soyca onlardan olmadığı halde topluluğa eklenmiş kişi — soyca onlardan olmadığı halde bir topluluğa eklenmiş kişi · kötülüğü ya da aşağılığıyla tanınan kimse · bir topluluğa sonradan eklenmiş, onlardan olmayan kişi
  الزنيم وهو الدعي (maqayis;ayn)؛ كل مستلحق فهو مزنم (ayn)؛ الزنيم والمزنم المستلحق في قوم ليس منهم (sihah)؛ الزنيم الدعي الملصق بالقوم وليس منهم (tahdhib)؛ الزنيم والمزنم الزائد في القوم وليس منهم (mufradat)؛ الذي يعرف بالشر كما تعرف الشاة بزنمتها (tahdhib)
- **B003** değerli sayıldığını gösteren sarkık damga taşıyan hayvan — değerli oluşunu göstermek için kulağında sarkık damga bırakılmış deve veya benzeri hayvan · değerli sayılan dişi koyun
  إنما يفعل ذلك بالكرام من الإبل (sihah)؛ الضائنة الزنمة فهي الكريمة (sihah)؛ المزنم من الإبل الكريم الذي جعل له زنمة علامة لكرمه (tahdhib)

## ك و ن (root_001332): 68:14 كَانَ, 68:22 كُنتُمْ, 68:29 كُنَّا, 68:31 كُنَّا, 68:33 كَانُوا۟, 68:41 كَانُوا۟, 68:43 كَانُوا۟, 68:48 تَكُن

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

## م و ل (root_001457): 68:14 مَالٍ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ب ن ي (root_000156): 68:14 وَبَنِينَ

- **B001** parçaları birleştirerek yapı kurma, kurulan yapı ve kurmaya olanak sağlama — parçaları birleştirip yapı kurmak · kurulmuş yapı; duvar, ev veya gök · çok sayıda saray yapmak · bir ev yapmak ve edinmek · birine ev yapması için ev ya da gerekli gereci vermek · keçi sürüsü çadır kurmaya yetecek kıl ve topluluk sağlamaz
  بناء الشيء بضم بعضه إلى بعض (maqayis)؛ بنى البناء يبني بنيا وبناء (ayn;tahdhib;mufradat)؛ بنى فلان بيتا من البنيان وبنى قصورا (sihah)؛ البنيان الحائط (sihah)؛ البناء اسم لما يبنى بناء (mufradat)؛ السماء بنيناها (mufradat)؛ أبنيت فلانا بيتا إذا أعطيته بيتا يبنيه (sihah;tahdhib)
- **B002** kuruluş biçimi ve doğuştan yapı — kuruluş biçimi; doğuştan beden yapısı
  فلان صحيح البنية أي الفطرة (sihah)؛ البنية الهيئة التي بني عليها (tahdhib)
- **B003** Kabe, Allah'ın Evi veya Mekke için özel ad — Kabe, Allah'ın Evi veya Mekke için kullanılan ad
  تسمى مكة البنية (maqayis)؛ البنية الكعبة (ayn;sihah;tahdhib)؛ البنية يعبر بها عن بيت الله (mufradat)
- **B004** deriden örtü, çadırımsı kap, yaygı veya saklama kabı — deriden çadırımsı örtü, yaygı, hasır ya da kap · yağmurdan korunmak ya da yere sermek için yaygı · otururken bacaklarını birbirinden ayırmak
  المبناة كهيئة الستر؛ كهيئة القبة تجلل بيتا عظيما (ayn)؛ المبناة النطع؛ ويقال هي العيبة (sihah;tahdhib)؛ المبناة قبة من أدم (tahdhib)؛ المبناة حصير أو نطع يبسطه التاجر على بيعه (tahdhib)؛ بسطنا له بناء أي نطعا (tahdhib)
- **B005** kirişine aşırı yapışan kusurlu yay — kirişine yapışıp onu kopma sınırına getiren kusurlu yay · kirişine yapışan kusurlu yay için bölgesel biçim
  قوس بانية وهي التي بنت على وترها (maqayis;sihah;tahdhib)؛ يكاد وترها ينقطع للصوقه بها (maqayis;tahdhib)؛ طيئ تقول قوس باناة (maqayis;tahdhib)؛ البائنة التي بانت من وترها وكلاهما عيب (tahdhib)
- **B006** gelini yeni evine götürme, eşle birleşme ve bunu yapan damat — gelini yeni evine götürmek veya eşiyle birleşmek · düğün sonrası eşiyle birleşen damat
  بنى على أهله بناء أي زفها (sihah)؛ الداخل بأهله كان يضرب عليها قبة ليلة دخوله بها (sihah)؛ الباني العروس الذي بنى على أهله (tahdhib)؛ بنى فلان على أهله وقد زفها (tahdhib)؛ العامة تقول بنى بأهله وليس من كلام العرب (sihah;tahdhib)
- **B007** oğul ve kız bağı, çocuk edinme ve kaynağa dayalı adlandırma — oğul; bir kaynaktan çıkan veya onun yetiştirdiği kimse · kız çocuk · oğullar, çocuklar ve kızlar · oğulluk ve çocukluk bağı · birini oğul edinmek veya oğulluğunu ileri sürmek · bir şeye kaynağı, yetişmesi, hizmeti ya da sürekli bağlılığı nedeniyle bağlanan kimse
  الابن أصله بنو (sihah;mufradat)؛ البنوة مصدر الابن (tahdhib)؛ تبنيت فلانا إذا اتخذته ابنا (sihah)؛ تبنيته إذا ادعيت بنوته (tahdhib)؛ سماه بذلك لكونه بناء للأب (mufradat)؛ كل ما يحصل من جهة شيء أو من تربيته أو بتفقده أو كثرة خدمته له أو قيامه بأمره هو ابنه (mufradat)؛ فلان ابن الحرب وابن السبيل وابن الليل وابن العلم (mufradat)؛ بنت فلان وابنة فلان وبنات (sihah;tahdhib;mufradat)
- **B008** küçük, dallanmış veya yerden çıkan şeylere çocuk adı verme — ana yoldan ayrılan küçük yollar · kız çocukların oynadığı küçük insan biçimli oyuncaklar · tapınma yerindeki çakıl taşları · bir çakıl taşı ile bir ot türü
  بنيات الطريق هي الطرق الصغار تتشعب من الجادة (sihah)؛ البنات التماثيل الصغار التي تلعب بها الجواري (sihah)؛ إحدى بنات مساجد الله كأنه جعله حصاة (sihah)؛ بنت الأرض الحصاة وابن الأرض ضرب من البقل (sihah)؛ يقال لكل ما يحصل من جهة شيء هو ابنه (mufradat)
- **B009** kaburgalar veya ev direkleri; yerleşip huzur bulma — göğüs kafesi kaburgaları veya ev direkleri · bir yere yerleşip huzur bulmak
  البواني أضلاع الزور؛ ألقى بوانيه إذا أقام بالمكان واطمأن؛ البوائن جمع البوان وهو اسم كل عمود في البيت
- **B010** yiyeceğin eti büyütüp besili kılması — yiyeceğin eti büyütüp besili kılması · otururken bacaklarını birbirinden ayırmak
  بنى لحم فلان طعامه يبنيه بناء إذا عظم من الأكل؛ بنى السويق لحمها؛ كما بنى بخت العراق القت

## ب ن و (root_001959): documented alternative for 68:14 وَبَنِينَ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## ت ل و (root_000186): 68:15 تُتْلَىٰ

- **B001** ardından izleme — bir şeyin ardından gelen · onu peşinden izledi · ay onun ardından sıra ve örnek alma bakımından geldi · atlar art arda geldi · hakkımı tam alıncaya kadar izini sürdüm
  أصل واحد وهو الاتباع (maqayis)؛ تلو الشيء الذي يتلوه (sihah)؛ تلاه تبعه متابعة (mufradat)؛ جاءت الخيل تتاليا أي متتابعة (sihah)
- **B002** kutsal kitabı okuyup izleme — indirilen kutsal kitapları okuyup anlamına uymak · kutsal kitabı okudum · onu hakkıyla bilgi ve eylemle izlerler · sözleri sana indirip bildiriyoruz
  تلاوة القرآن لأنه يتبع آية بعد آية (maqayis)؛ تلوت القرآن تلاوة (sihah)؛ التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام (mufradat)
- **B003** ardından kalan bakiye — önceki kısmın ardından kalan borç veya hak payı · borç ya da haktan geriye kalan pay · hakkımdan bana kalan bir pay oldu · hakkımdan onun yanında bir pay bıraktım · kalan ihtiyacın peşine düşüyorum · ona izleyip alacağı bir kalan pay bıraktım
  التلية والتلاوة وهي البقية لأنها تتلو ما تقدم منها (maqayis)؛ التلية بقية الدين وكذلك التلاوة (sihah)؛ التلاوة والتلية بقية مما يتلى أي يتبع (mufradat)
- **B004** bağlı güvence ve talep — kişiyi izleyen güvence veya yükümlülük · ona güvence verdim · birini hakkı nedeniyle başka birine yönelttim
  التلاء الذمة لأنها تتبع وتطلب يقال أتليته ذمة (maqayis)؛ التلاء الذمة (sihah)؛ أتليته أحلته من الحوالة (sihah)؛ أتليت فلانا على فلان بحق أي أحلته عليه (mufradat)
- **B005** geride bırakıp terk etme — adamı terk edip yardımsız bıraktım · onu geçtim ve arkamda bıraktım
  تلوت الرجل إذا خذلته وتركته (maqayis;sihah)؛ حتى أتليته أي حتى تقدمته وصار خلفي (sihah)؛ أتليته أي سبقته (sihah)
- **B006** anneyi izleyen yavru — devenin annesini izleyen yavrusu · erken doğuran koyun · devenin yavrusu onun peşinden geldi · Tanrı ona peş peşe çocuklar verdi · sürülerin yavrusuz kalması dileği
  تلو الناقة ولدها الذي يتلوها؛ التلوة من الغنم التي تنتج قبل الصفرية؛ أتلت الناقة إذا تلاها ولدها؛ أتلاه الله أطفالا أي أتبعه أولادا
- **B007** sese karşılık veren eşlikçi — şarkıcıya sesle karşılık veren kişi
  المتالي الذي يراد صاحبه الغناء لأن كل واحد منهما يتلو صاحبه (maqayis)؛ المتالي الذي يراسل المغني بصوت رفيع (sihah)
- **B008** son nefeste olmak [kalıp] — adam son nefesindeydi
  تلى الرجل بالتشديد إذا كان بآخر رمق
- **B009** hakkında yalan söylemek [kalıp] — biri hakkında yalan söylüyor
  فلان يتلو على فلان ويقول عليه أي يكذب عليه

## ECHO ت ل ل (root_000185): for 68:15 تُتْلَىٰ: withheld observed target; not identity

- **B001** küçük tepe veya yer kabartısı — tepe, tepecik veya yüksekçe yer
  التل معروف (maqayis); التل واحد التلال (sihah); التلال الروابي المخلوقة; التل من أصاغر الآكام (tahdhib); أصل التل المكان المرتفع (mufradat)
- **B002** boyun — boyun
  التليل العنق (maqayis); التليل العنق (sihah); التليل العنق; بعنق ذي خصل من الشعر (tahdhib); والتليل العنق (mufradat)
- **B003** yere serme veya yüzüstü düşürme — yere serdi veya düşürdü · alnı ya da yüzü üzerine düşürdü · yere serilmiş kimse · yere serilmiş kimse
  فتله أي صرعه; وتله للجبين (maqayis); وتله للجبين أي صرعه; كبه لوجهه (sihah); معنى تله صرعه; كبه لفيه (tahdhib); تله للجبين أسقطه على التل; أسقطه على تليله (mufradat)
- **B004** dökme; ele verme veya teslim etme — eline verdi veya teslim etti · döktü · bir dökümlük miktar veya dökülen şey · elime döküldü veya bırakıldı
  تل إذا صب; التلة الصبة; فتلت في يدي معناه فصبت في يدي; تللت في يديه أي دفعت إليه سلما
- **B005** sarsıp huzursuz etme; ağır sıkıntılar — sarsma, oynatma ve huzursuz etme · sarstı, oynattı ve huzursuz etti · ağır sıkıntılar · huzursuz etme ve hareket
  التلتلة الإقلاق (maqayis); تلتله أي زعزعه وأقلقه وزلزله; التلاتل الشدائد (sihah); التليلة الإقلاق والحركة; البلابل والتلاتل الشدائد (tahdhib)
- **B006** iri ve güçlü oluş; kalın, sağlam mızrak — iri ve güçlü; kalın, sağlam mızrak · kalın, sağlam ve yere seren mızrak · iri yapılı ve güçlü adam
  المتل الرمح الذي يصرع به (maqayis); المتل الشديد; رمح متل يتل به (sihah); رجل متل إذا كان غليظا شديدا; رمح متل غليظ شديد (tahdhib); المتل الرمح الذي يتل به (mufradat)
- **B007** hurma salkımı kabuğundan içki kabı — hurma salkımı kabuğundan içki kabı
  التلتلة مشربة تتخذ من قيقاءة الطلع (sihah); التلتلة قشر الطلعة يشرب فيه النبيذ; منه قيل للمشربة تلتلة لأنه يصب ما فيها في الحلق (tahdhib)
- **B008** kötü durumda olma — kötü durumda olma
  هو بتلة سوء; ببيئة سوء; بحالة سوء
- **B009** uzanma ya da tembellik — uzanıp yatma; tembellik
  والتلة الضجعة والكسل
- **B010** borçtan kalan tutar — borçtan kalan bölüm
  والتلة بقية الدين
- **B011** ağızdaki ıslaklık — ağızdaki nem veya ıslaklık
  ما هذه التلة بفيك أي البلة; التلل والبلل والتلة والبلة شيء واحد
- **B012** sapma sözünde uyaklı pekiştirme — sapmış, büsbütün sapmış · sapıklık ve onu pekiştiren uyaklı söz
  رجل ضال تال; جاءنا بالضلالة والتلالة; كل ذلك إتباع (sihah); ضال تال آل وجاء بالضلالة والتلالة والألالة (tahdhib)
- **B013** kısrağa damızlık erkek aramaya gitme — kısrağına damızlık erkek aramaya gitti
  ذهب يتال أي يطلب لفرسه فحلا وهو يفاعل

## ء ي ي (root_000074): 68:15 ءَايَٰتُنَا

- **B001** bekleyerek oyalanma — durup oyalanmak · isin imkanini beklemek · kalinacak veya oyalanilacak yer
  تأيا يتأيا تأييا أي تمكث؛ تأييت الأمر انتظرت إمكانه؛ ليست هذه بدار تئية أي مقام (maqayis)؛ تأيا أي توقف وتمكث؛ منزل تئية أي منزل تلبث وتحبس (sihah)
- **B002** kisiyi bilerek hedefleme — onu belirtisiyle bilerek kastetmek
  تآييت وأصله تعمدت آيته وشخصه (maqayis)؛ تآييته وتأييته إذا قصدت آيته وتعمدته (sihah)
- **B003** gorunen belirti — gorunen isaret · belirlenmis isaret · kisinin sahsi · topluca cikmak · kitaptaki harf toplulugu parcasi · gunesin isigi · gunesin isigi
  الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ آية القرآن لأنها جماعة حروف؛ إياة الشمس ضوءها لأنه كالعلامة لها (maqayis)؛ الآية العلامة والآية من آيات الله والجميع الآي (ayn)؛ الآية العلامة؛ آية الرجل شخصه؛ خرج القوم بآيتهم أي بجماعتهم؛ الآية من كتاب الله جماعة حروف؛ أياة الشمس ضوؤها (sihah)
- **B004** hangi belirleyicisi — soru, sart veya ilgiyle belirleyen ad · hangi olursa veya herhangi bir
  لم يجىء إلا في قولهم أي في الاستفهام (jamhara)؛ أي مثقلة بمنزلة من وما؛ أيهم أخوك؛ أيما الأخوين؛ أيا ما تحب؛ أي لا تنون لأن أي مضاف (ayn)؛ أي اسم معرب يستفهم به ويجازى؛ وقد يكون بمنزلة الذي؛ وقد يكون نعتا للنكرة؛ وأي قد يتعجب بها (sihah)
- **B005** nesne zamiri dayanagi — nesne zamiri icin dayanak unsur
  إياك ضربت فتكون إيا عمادا للكاف؛ ولا تكون إيا مع كاف ولا هاء ولا ياء في موضع الرفع والجر؛ إياك وزيدا (ayn)
- **B006** zaman sorusu — ne zaman anlaminda zaman sorusu
  أيان بمنزلة متى؛ يختلف في نونها فيقال هي أصلية ويقال هي زائدة (ayn)
- **B007** nice cok — ne kadar cok anlaminda nicelik birimi · ne kadar cok anlaminda varyant
  كأين في معنى كم؛ أصل بنائها أي (ayn)؛ تدخل على أي الكاف فينقل إلى تكثير العدد بمعنى كم؛ كائن وكأين (sihah)
- **B008** ey seslenmesi — yakin muhataba seslenme birimi · yakin veya uzak muhataba seslenme birimi · uzatilmis seslenme bicimi
  في النداء أي فلان وقد يمد آي فلان (ayn)؛ أيا من حروف النداء ينادى بها القريب والبعيد؛ أي حرف ينادى به القريب (sihah)
- **B009** yani aciklayicisi — anlami aciklayan yani birimi
  أي تفسيرا للمعاني أي كذا وكذا (ayn)؛ أي كلمة تتقدم التفسير تقول أي كذا بمعنى تريد كذا (sihah)
- **B010** yemin oncesi evet — yemin oncesi evet veya bilakis sozu
  إي تدخل في اليمين كالصلة والافتتاح؛ إي وربي؛ المعنى نعم والله (ayn)؛ إى بالكسر كلمة تتقدم القسم معناها بلى؛ إى ربى وإى والله (sihah)

## ق و ل (root_001272): 68:15 قَالَ, 68:26 قَالُوٓا۟, 68:28 قَالَ, 68:28 أَقُل, 68:29 قَالُوا۟, 68:31 قَالُوا۟, 68:51 وَيَقُولُونَ

- **B001** söze dökme — sözü sesle dile getirmek · söylenmiş söz veya sözlü ifade · söylenmiş söz için kullanılan adlar
  القول من النطق (maqayis)؛ قال يقول قولا وقولة ومقالا ومقالة (sihah)؛ القول والقيل واحد (mufradat)؛ المركب من الحروف المبرز بالنطق (mufradat)؛ القيل من القول اسم (ayn)
- **B002** konuşma organı — konuşma organı olan dil
  المقول اللسان (maqayis;ayn;sihah)
- **B003** çok sözlü kişi — çok konuşan, dili güçlü kişi
  رجل قولة وقوال كثير القول (maqayis)؛ رجل تقوالة أي منطيق وقوال وقوالة أي كثير القول (ayn)؛ رجل مقول ومقوال وقولة وقوال وتقوالة أي لسن كثير القول (sihah)
- **B004** sözü geçen yönetici unvanı — sözü geçen yerel hükümdar unvanı · bu unvanın çoğul adları · bu unvanın kadın için kullanılan biçimi
  المقول بلغة أهل اليمن القيل وهم المقاولة والأقيال والأقوال والواحد القيل (ayn)؛ القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة (sihah)؛ كأنه الذي له قول أي ينفذ قوله (sihah)
- **B005** yalan söyleme veya isnat etme [kalıp] — olmayan bir şeyi söyledi · ona yalan isnat etti · bana söylemediğim şeyi yükledi
  تقول باطلا أي قال ما لم يكن (ayn)؛ قولتني ما لم أقل وأقولتني ما لم أقل أي ادعيته علي (sihah)؛ تقول عليه أي كذب عليه (sihah)
- **B006** sözü üzerine alma [kalıp] — iyi ya da kötü bir sözü kendi üzerine aldı
  اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر (ayn)
- **B007** dolaşımdaki söz — hakkında iyi veya kötü söz yayıldı · insanlar arasında yayılmış söz · dedikodu ve çokça dönen laf
  انتشرت له قالة حسنة أو قبيحة في الناس (ayn)؛ القالة القول الفاشي في الناس (ayn)؛ كثر فيه القيل والقال (ayn)؛ كثرت قالة الناس (sihah)؛ كثر القيل والقال (sihah)
- **B008** oyun sopası — oyunda küçük parçaya vurulan tahta sopa
  القال الخشبة التي تضرب بها القلة (sihah)
- **B009** müzakere etme [kalıp] — bir iş hakkında karşılıklı görüştük
  قاولته في أمره وتقاولنا أي تفاوضنا (sihah)
- **B010** hükmünü dayatma [kalıp] — üzerinde hüküm yürüttü, tahakküm etti
  اقتال عليه تحكم (sihah)
- **B011** sanma işlevli söyleme — söyleme fiilini sanmak gibi kurmak
  العرب تجري تقول وحدها في الاستفهام مجرى تظن في العمل (sihah)؛ بنو سليم يجرون متصرف قلت في غير الاستفهام أيضا مجرى الظن (sihah)
- **B012** içte kalmış söz [kalıp] — içte tasarlanıp henüz söylenmemiş anlam
  المتصور في النفس قبل الإبراز باللفظ قول (mufradat)؛ في نفسي قول لم أظهره (mufradat)
- **B013** görüş benimseme [kalıp] — bir görüş veya mezhebi benimsedi
  للاعتقاد نحو فلان يقول بقول أبي حنيفة (mufradat)
- **B014** durumuyla belli etme [kalıp] — durumuyla yeter olduğunu belli etti
  للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني (mufradat)
- **B015** içten önemseme [kalıp] — bir şeye içten önem verdi
  للعناية الصادقة بالشيء كقولك فلان يقول بكذا (mufradat)
- **B016** teknik tanım [kalıp] — bir şeyin teknik tanımı
  يستعمله المنطقيون في معنى الحد فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما (mufradat)
- **B017** içe doğan anlam — içe doğan anlamın söz diye adlandırılması
  في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا (mufradat)

## ECHO ق ل ل (root_001251): for 68:15 قَالَ, 68:26 قَالُوٓا۟, 68:28 قَالَ, 68:28 أَقُل, 68:29 قَالُوا۟, 68:31 قَالُوا۟, 68:51 وَيَقُولُونَ: withheld observed target; not identity

- **B001** azlık — az şey; azlık · azlık ve yetersizlik; yoksulluk ve düşüklük · az; az sayıda veya az miktarda · azalmak; az olmak · gözünde az göstermek · yoksullaşmak · az saymak; az görmek · hiç; ne azı ne çoğu · pek seyrek; hemen hemen hiç · yoksulluğa ve aşağılanmaya uğrasın · hiç malı olmamak · kendisi de ailesi de tanınmayan adam
  القل القليل؛ رماه الله بالقل والذل أي بالقلة والذلة (jamhara)؛ شيء قليل وجمعه قلل؛ قل الشيء يقل قلة؛ قلله في عينه؛ أقل افتقر؛ استقله عده قليلا (sihah)؛ قل الشيء يقل قلة فهو قليل وقلال؛ القل من الرجال الخسيس الدنيء؛ قليلة ولا كثيرة؛ قليلا ما يؤمنون؛ قاللت لفلان؛ تقاللت ما أعطاني (tahdhib)؛ القلة والكثرة يستعملان في الأعداد؛ يكنى بالقلة عن الذلة؛ يكنى بها تارة عن العزة؛ قليل يعبر به عن النفي (mufradat)
- **B002** bir şeyin tepesi veya başı — dağın tepesi; doruk · bir şeyin tepesi veya başı · insanın başı · sap ucunda topuzu bulunan kılıç
  القلة قلة الجبل وهي القطعة تستدير في أعلاه وهي القنة (jamhara)؛ القلة أعلى الجبل؛ قلة كل شيء أعلاه؛ رأس الإنسان قلة (sihah)؛ قلة كل شيء رأسه؛ قلة الجبل أعلاه؛ قبيعة السيف قلته؛ سيف مقلل (tahdhib)؛ قلة الجبل شعفه (mufradat)
- **B003** büyük küp — büyük küp; iri kap · belirli bir bölgenin iri küpleri · iki büyük küp veya bunların aldığı miktar
  القلة التي جاءت في الحديث مثل قلال هجر هي جرار عظام (jamhara)؛ القلة إناء للعرب كالجرة الكبيرة؛ قلال هجر شبيهة بالحباب (sihah)؛ قلتين يعني هذه الحباب العظام واحدتها قلة؛ قلال هجر؛ القلة منها تأخذ مزادة من الماء (tahdhib)؛ القلة ما أقله الإنسان من جرة وحب (mufradat)
- **B004** yük kaldırma, yükselme ve yola koyulma — küpü taşıyabilmek · bir şeyi taşımak; yüklenmek · ağır bulutları taşımak · uçuşa kalkmak; havalanmak · yüklenip yola çıkmak · yükselmek
  أقل الجرة أطاق حملها؛ استقلت السماء ارتفعت؛ استقل القوم مضوا وارتحلوا (sihah)؛ أقل الرجل الشيء واستقله إذا احتمله؛ استقل الطائر إذا نهض للطيران؛ استقل النبات أناف؛ استقل القوم إذا احتملوا ظاعنين؛ أقلت سحابا ثقالا أي حملت؛ قل إذا رفع وقل إذا علا (tahdhib)؛ أقلت سحابا ثقالا أي احتملته؛ أقللت كذا وجدته قليل المحمل (mufradat)
- **B005** korku veya öfkeden titreme — korku veya öfkeden doğan titreme · korku veya öfkeden titremeye tutulmak · öfkeden titremek
  القل الرعدة والانتفاض؛ أخذ فلانا القل إذا أخذته رعدة من فزع (jamhara)؛ القل بالكسر شبه الرعدة؛ أخذه قل من الغضب (sihah)؛ القل الرعدة؛ أخذه قل إذا أرعد من الغضب؛ إذا غضب قد استقل (tahdhib)
- **B006** oynatma ve kararsızca sallanma — sallanma, yerinde duramama ve hareket sesi · sallayıp oynatmak · sallanmak; yerinde duramamak · çevik; hızlı
  قلقل أي صوت وهو حكاية؛ قلقله قلقلة وقلقالا فتقلقل أي حركه فتحرك واضطرب (sihah)؛ القلقلة والتقلقل قلة الثبوت في المكان؛ يتقلقل في موضعه؛ القلق ألا يستقر الشيء في مكان واحد (tahdhib)؛ تقلقل الشيء إذا اضطرب؛ تقلقل المسمار؛ القلقلة حكاية صوت الحركة (mufradat)

## ء و ل (root_000067): 68:15 ٱلْأَوَّلِينَ

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

## ECHO و ل ي (root_001684): for 68:15 ٱلْأَوَّلِينَ: withheld observed target; not identity

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

## و س م (root_001650): 68:16 سَنَسِمُهُۥ

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

## خ ر ط م (root_000404): 68:16 ٱلْخُرْطُومِ

- **B001** burun veya burun görevli uzantı; damga bağlamında yüz — burun veya hayvandaki burun görevli uzantı; damga bağlamında yüz
  الخرطوم: الأنف (sihah;tahdhib)؛ الخرطوم وإن خص بالسمة فإنه في مذهب الوجه (tahdhib)؛ الخرطوم للفيل، وهو أنفه (tahdhib)؛ وللبعوضة خرطوم (tahdhib)
- **B002** topluluğun ileri gelenleri [kalıp] — topluluğun ileri gelenleri ve önderleri
  خراطيم القوم: سادتهم (sihah)
- **B003** şarap; özellikle kendiliğinden süzülen seçkin şarap — şarap; özellikle sıkılmadan kendiliğinden akan seçkin şarap
  الخرطوم: الخمر (sihah;tahdhib)؛ الخرطوم: السلاف الذي سال من غير عصر (tahdhib)
- **B004** başını kaldırarak böbürlenen öfkeli kişi — başını yukarı kaldırarak böbürlenen öfkeli kişi
  المخرنطم: الغضبان المتكبر مع رفع رأسه (sihah)؛ المخرنطم: الغضبان المستكبر مع رفع رأسه (tahdhib)

## ب ل و (root_000153): 68:17 بَلَوْنَٰهُمْ, 68:17 بَلَوْنَآ

- **B001** eskime ve yolculukta yıpranma — nesnenin ya da giysinin eskimesi ve yıpranması · eskime, yıpranma · yolculuğun yıprattığı binek · Güle güle eskit; Tanrı yerine yenisini versin
  بلي الشيء يبلى بلى فهو بال (ayn)؛ بلي الثوب يبلى بلى وبلاء (sihah;tahdhib;mufradat)؛ ناقة بلو سفر أبلاها السفر (ayn;sihah;tahdhib;mufradat)
- **B002** deneyerek sınama ve gerçek niteliği ortaya çıkarma — durumunu anlamak için denemek ve sınamak · bir insanı sınamak · iyilik veya güçlük yoluyla sınama · çetin sınama ve deneme · sınama
  بلي الإنسان وابتلي إذا امتحن (ayn)؛ بلوته بلوا جربته واختبرته (sihah)؛ بلاه يبلوه بلوا إذا جربه (tahdhib)؛ بلوته اختبرته وتبلوا كل نفس ما أسلفت أي تعرف حقيقة ما عملت (mufradat)
- **B003** iyilikte bulunma ve üstün çaba gösterme — ona iyilik etti · cömertlikte veya savaşta üstün çaba gösterdi · ona iyilik ettim
  والله يبلي العبد بلاء حسنا وبلاء سيئا (ayn)؛ أبلاه الله بلاء وأبلاه إبلاء حسنا وأبليته معروفا (sihah)؛ أبلاه الله يبليه إبلاء حسنا إذا صنع به صنيعا جميلا وأبلى فلان إذا اجتهد في صفة كرم أو حرب (tahdhib)؛ اختبار الله للعباد تارة بالمسار وتارة بالمضار وليبلي المؤمنين منه بلاء حسنا (mufradat)
- **B004** mazereti açıklama veya yeminle güven verme ya da sınama — ona mazeretimi açıklayıp kınanmayı giderdim · ona güven vermek için yemin ettim veya sınansın diye yemin sundum
  أبليت فلانا عذرا أي بينت فيما بيني وبينه ما لا لوم علي بعده (ayn)؛ أبليت فلانا يمينا إذا طيبت نفسه بها (sihah;tahdhib)؛ أبليت فلانا يمينا إذا عرضت عليه اليمين لتبلوه بها (mufradat)
- **B005** mezar başında ölüme bırakılan binek ve çevresindeki ağıtçılar — sahibinin mezarı yanında bağlanıp ölüme bırakılan binek · ölen kişinin bineği çevresinde ağıt yakan kadınlar
  البلية الدابة التي كانت تشد في الجاهلية على قبر صاحبها حتى تموت (ayn)؛ البلية أيضا الناقة التي كانت تعقل في الجاهلية عند قبر صاحبها (sihah)؛ البلية الناقة تعقل عند قبر صاحبها فلا تعلف حتى تموت (tahdhib)؛ قامت مبليات فلان ينحن عليه (sihah;tahdhib)
- **B006** olumsuz sözü tersine çeviren olumlu cevap — olumsuz sözü geri çevirip durumu doğrulayan cevap sözü
  بلى جواب استفهام فيه حرف نفي (ayn)؛ بلى جواب للتحقيق توجب ما يقال لك لأنها ترك للنفي (sihah)؛ بلى رد للنفي أو جواب لاستفهام مقترن بنفي (mufradat)
- **B007** önemsememe ve umursamama — onu umursamıyorum, ona önem vermiyorum · önemseme, umursama
  ما أباليه أي ما أكترث له ولم أبل (sihah)؛ بالى يبالي مبالاة (tahdhib)
- **B008** bir topluluk adı ve o topluluğa mensubiyet — Beli adlı boy veya kabile · Beli boyuna mensup, Belevi
  بلي حي والنسبة إليه بلوي (ayn)؛ بلى على فعيل قبيلة من قضاعة والنسبة إليهم بلوى (sihah)؛ بلي حي من اليمن والنسبة إليهم بلوي (tahdhib)
- **B009** belirli bir deyimde farklı yönlere dağılmış olma [kalıp] — her biri farklı bir yana dağılmış
  الناس بذي بلي وذي بلي أي متفرقون (ayn)

## ECHO ب ل ي (root_000154): for 68:17 بَلَوْنَٰهُمْ, 68:17 بَلَوْنَآ: withheld observed target; not identity

- **B001** kullanımla eskime ve yolculukta yıpranma — eskimek, kullanımdan yeniliğini yitirmek · eskime, yıpranma · eskimiş, yıpranmış · yolculuğun yıprattığı dişi deve ya da binek
  بلي الشيء يبلى بلى فهو بال (ayn)؛ بلي الثوب يبلى بلى وبلاء (sihah;tahdhib)؛ بلي الثوب بلى وبلاء أي خلق (mufradat)؛ ناقة بلو سفر وبلي سفر للتي قد أبلاها السفر (ayn;sihah;tahdhib;mufradat)
- **B002** iyi ya da kötü koşulla sınama — sınamak ve deneyip tanımak · sınanmak, bir sınamaya uğramak · iyi ya da kötü bir durumla sınanma
  بلي الإنسان وابتلي إذا امتحن (ayn;tahdhib)؛ بلوته بلوا جربته واختبرته (sihah;tahdhib;mufradat)؛ البلاء في الخير والشر (ayn;sihah;tahdhib)؛ المحنة والمنحة جميعا بلاء (mufradat)
- **B003** güzel bir iyilikte bulunma ve üstün çaba [kalıp] — iyilik etmek, güzel bir davranışta bulunmak · cömertlikte ya da savaşta yoğun çaba göstermek
  أبلاه الله إبلاء حسنا إذا صنع به صنيعا جميلا (tahdhib)؛ أبليته معروفا (sihah)؛ أبلى فلان إذا اجتهد في صفة كرم أو حرب (tahdhib)؛ ليبلي المؤمنين منه بلاء حسنا (mufradat)
- **B004** mazeretini açıklayarak kınanmayı kaldırma [kalıp] — mazeretini açıklayıp kınanmayı ortadan kaldırmak
  أبليت فلانا عذرا أي بينت فيما بيني وبينه ما لا لوم علي بعده (ayn)؛ أبليت فلانا عذرا أي بينت له وجه العذر لأزيل عني اللوم (tahdhib)
- **B005** rahatlatmak veya sınamak için yemin sunma [kalıp] — birine yemin ederek içini rahatlatmak veya sınamak üzere ona yemin sunmak
  أبليت فلانا يمينا إذا طيبت نفسه بها (sihah)؛ أبليت فلانا إذا حلفت له فطيبت بها نفسه (tahdhib)؛ أبليت فلانا يمينا إذا عرضت عليه اليمين لتبلوه بها (mufradat)
- **B006** mezar yanında bağlanıp ölüme bırakılan binek — mezar yanında bağlanıp beslenmeden ölüme bırakılan dişi deve ya da binek hayvanı
  البلية الدابة التي كانت تشد في الجاهلية على قبر صاحبها (ayn)؛ البلية أيضا الناقة التي كانت تعقل في الجاهلية عند قبر صاحبها (sihah)؛ البلية الناقة تعقل عند قبر صاحبها فلا تعلف حتى تموت (tahdhib)
- **B007** bir topluluk adı ve ona mensubiyet — belirli bir boyun ya da topluluğun adı · bu boya ya da topluluğa mensup olan
  بلي حي والنسبة إليه بلوي (ayn)؛ بلي قبيلة من العرب ينسب إليها بلوي (jamhara)؛ بلى على فعيل قبيلة من قضاعة والنسبة إليهم بلوى (sihah)؛ بلي حي من اليمين والنسبة إليهم بلوي (tahdhib)
- **B008** ayrı yerlere dağılmış olma [kalıp] — dağınık ve ayrı yerlere yayılmış olmak
  تقول الناس بذي بلي وذي بلي أي متفرقون (ayn)
- **B009** umursamama ve önem vermeme — umursamamak, önem vermemek · umursamama, önem vermeme
  ما أباليه أي ما أكترث له؛ لم أبل؛ ما أباليه بالة (sihah)
- **B010** olumsuzlamayı kaldıran doğrulama cevabı — olumsuzlananı doğrulayan cevap sözü
  بلى جواب استفهام فيه حرف نفي (ayn)؛ بلى جواب للتحقيق توجب ما يقال لك لأنها ترك للنفي (sihah)؛ بلى رد للنفي أو جواب لاستفهام مقترن بنفي (mufradat)

## ص ح ب (root_000844): 68:17 أَصْحَٰبَ, 68:48 كَصَاحِبِ

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

## ق س م (root_001226): 68:17 أَقْسَمُوا۟

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

## ص ر م (root_000861): 68:17 لَيَصْرِمُنَّهَا, 68:20 كَٱلصَّرِيمِ, 68:22 صَٰرِمِينَ

- **B001** kesip ayırma; bağı koparma — bir şeyi, ipi ya da salkımı kesip ayırmak · birinin sözünü kesmek · kesilip sona ermek veya geçip gitmek · parça parça kesilmek veya süresi dolmak · ipleri çokça kesmek · iplikçilerin kullandığı kesici orak
  الصاد والراء والميم أصل واحد صحيح مطرد وهو القطع (maqayis)؛ الصرم قطع بائن لحبل وعذق ونحوه (ayn;tahdhib)؛ صرمت الشيء إذا قطعته وصرمت الرجل إذا قطعت كلامه (sihah)؛ الصرم القطيعة وانصرم الشيء انقطع (mufradat)
- **B002** hurma salkımlarını kesip toplama ve toplama zamanı — hurma salkımlarını kesip toplama veya bunun zamanı · hurmaların toplanma zamanı gelmek
  الصرام وقت صرم الأعذاق وقد أصرم النخل حان صرامه (maqayis)؛ الصرام وقت صرام النخل وصرم العذق عن النخلة (ayn;tahdhib)؛ صرم النخل أي جده وأصرم النخل أي حان له أن يصرم (sihah)؛ ليصرمنها أي يجتنونها ويتناولونها (mufradat)
- **B003** kesin karar ve ödünsüz ilerleyiş — kesin karar, sağlam kararlılık ve etkili görüş · işlerinde kararlı, dayanıklı ve gözü pek kişi · keskin ve iyi kesen kılıç
  الصريمة العزيمة على الشيء (maqayis)؛ الصريمة إحكامك أمرا والعزم عليه والصريمة الرأي النافذ (ayn)؛ الصريمة العزيمة على الشيء (sihah)؛ رجل صارم أي ماض في كل أمر وسيف صارم أي قاطع (tahdhib)؛ الصريمة إحكام الأمر وإبرامه والصارم الماضي (mufradat)
- **B004** birbirini sona erdiren gece ve gündüz; yanıp kararmış veya ürünü kesilmiş görünüm — gece veya karanlık gece · geceyi kesip bitiren sabah veya gündüz · yanıp kararmış ya da ürünü kesilip çıplak kalmış gibi
  الصريم اسم الصبح واسم الليل لأن كل واحد منهما يصرم صاحبه (maqayis)؛ فأصبحت كالصريم أي كالليل (ayn)؛ الصريم الليل المظلم والصريم الصبح وهو من الأضداد (sihah)؛ الصريم الليل والصريم النهار وقيل أرض سوداء لا تنبت شيئا (tahdhib)؛ قيل أصبحت كالأشجار الصريمة وقيل كالليل (mufradat)
- **B005** bütünden ayrılmış parça veya sınırlı küme — sert zeminden veya ana kumluktan ayrılan kum parçası · ana kum kütlesinden ayrılmış iri kumluk · yaklaşık on ile kırk deve arasındaki sürü · ayrı bir bulut parçası · develeriyle suyun bir yanında konaklayan küçük insan topluluğu
  الصريم الرمل ينقطع عن الجدد والصرمة القطيع من الإبل والصرم القطع من السحاب والصرم طائفة من القوم (maqayis)؛ الصريمة الرمل المتصرم من معظم الرمل والصرمة قطيع من الإبل والصرمة قطعة من السحاب (ayn)؛ الصريمة ما انصرم من معظم الرمل وصريمة من غضى ومن سلم أي جماعة منه (sihah)؛ الصريمة من الرمل قطعة ضخمة تنصرم عن سائر الرمال والصرم الفرقة من الناس (tahdhib)؛ الصريم قطعة منصرمة عن الرمل (mufradat)
- **B006** meme başı kesilerek sütü kurutulmuş dişi deve — meme başı kesilip süt kanalı kuruduğu için sütü kesilmiş dişi deve
  ناقة مصرمة أي يصرم طبيها فيفسد الإحليل فييبس (maqayis)؛ ناقة مصرمة يصرم طبيها فيقرح عمدا (ayn;tahdhib)؛ ناقة مصرمة وهو أن يقطع طبياها لييبس الإحليل (sihah)؛ ناقة مصرومة كأنها قطع ثديها فلا يخرج لبنها (mufradat)
- **B007** sona ererken kalan son miktar veya son sınır — bol dönemden sonraki son süt veya bir şeyin kesildiği son sınır
  الصرام آخر اللبن بعد التغزير (maqayis;sihah)؛ بلغ من الشر آخره وآخر الشيء عند انقطاعه (maqayis)؛ فقد حلبت صرام لكم صراها (tahdhib)
- **B008** kötü duruma düşme; savaş veya ağır felaket — durumu kötüleşmek veya yoksullaşmak, yine de biraz dayanmak · savaş veya ağır felaket · perişan ve korkmuş gelmek veya bir işten umudu kesmiş olmak
  أصرم الرجل ساءت حاله وفيه تماسك بعد (ayn)؛ أصرم الرجل افتقر وصرام من أسماء الحرب والداهية (sihah)؛ جاء فلان صريم سحر إذا جاء بائسا خائفا وصرام من أسماء الحرب وصرام داهية (tahdhib)؛ أصرم ساءت حاله (mufradat)
- **B009** gün boyu yeten tek öğün; her şeyi yok eden karışıklık — kuşluktan ertesi kuşluğa kadar yeten tek öğün · her şeyi kökünden gideren yıkıcı karışıklık
  الصيرم وهي الوجبة لأنه إذا أكلها قطع سائر يومه (maqayis)؛ الصيرم الوجبة (sihah)؛ فلان يأكل الصيرم في اليوم والليلة إذا كان يأكل الوجبة وهي أكلة عند الضحى إلى مثلها من الغد (tahdhib)؛ الصيرم هي التي تستأصل كل شيء (tahdhib)
- **B010** su ve insan yakınlığından kopuk ıssızlık — suyu bulunmayan ıssız arazi · insanlardan uzak sayılan kurt ile karga
  الصرماء الأرض لا ماء بها والأصرمان الذئب والغراب سميا بذلك لقطعهما الأنيس (maqayis)؛ الأصرمان الذئب والغراب لأنهما انصرما من الناس والصرماء المفازة التي لا ماء فيها (sihah)؛ الصرماء الفلاة من الأرض والأصرمان الذئب والغراب لأنهما انصرما من الناس (tahdhib)

## ص ب ح (root_000839): 68:17 مُصْبِحِينَ, 68:20 فَأَصْبَحَتْ, 68:21 مُصْبِحِينَ

- **B001** günün ilk aydınlığı — tan ve günün ilk aydınlığı · günün başı, gecenin karşıtı olan erken gündüz · her günün ilk bölümü · günün ilk bölümüne girme ya da o an · günün ilk bölümüne varılan yer ya da o an
  الصباح نور النهار (maqayis)؛ الصبح والصباح أول النهار (mufradat)؛ الصبح الفجر والصباح نقيض المساء (sihah)؛ الصبح معروف والصبيحة من كل يوم أول النهار (jamhara)؛ صبحني فلان إذا أتاك صباحا والمصبح الموضع الذي يصبح فيه (ayn)
- **B002** günün başında gelmek — ona günün başında geldim ya da o bana günün başında geldi · onlara günün başında su getirdim · günün başına özgü esenlik sözü
  صبحني فلان إذا أتاك صباحا (ayn)؛ صبحته إذا أتيته صباحا وصبحته أي قلت له عم صباحا (sihah)؛ صبحتهم ماء كذا أتيتهم به صباحا (mufradat)
- **B003** günün başındaki içecek ve içme — günün başında içme ya da yeme; o vakitte içilen şey · ona günün başı içeceğini verdim · günün başında içti · günün başı içeceğini içmiş kimse · günün başı içeceğinin verildiği kap · günün başında içmek için kullanılan kadehler · günün başı içeceğinden önce oyalanılan şey
  لشرب الغداة الصبوح والمصابيح الأقداح التي يصطبح بها (maqayis)؛ الصبوح ما يشرب بالغداة وفعلك الاصطباح (ayn)؛ الصبوح الأكل والشرب في أول النهار وصبحت الإبل إذا سقيتها في أول النهار (jamhara)؛ الصبوح الشرب بالغداة وهو خلاف الغبوق (sihah)؛ الصبوح شرب الصباح يقال صبحته سقيته صبوحا والمصباح ما يسقى منه (mufradat)
- **B004** günün başında baskın — günün başındaki baskın günü · savaşta onlara günün başında atla vardık · tehlike anında söylenen yardım çağrısı
  يوم الصباح يوم الغارة (maqayis;sihah)؛ في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا (ayn)
- **B005** ışık veren lamba — lamba, kandil ya da lambalık · lambanın kendisi · onunla ışık yakmak ya da onu yakıt yapmak · gök cisimlerinin ışıkları
  سمي المصباح مصباحا لحمرته (maqayis)؛ الصباح السراج بعينه والمصباح المسرجة (jamhara)؛ المصباح السراج وقد استصبحت به إذا أسرجت والشمع مما يصطبح به أي يسرج به (sihah)؛ يقال للسراج مصباح والمصباح مقر السراج والمصابيح أعلام الكواكب (mufradat)
- **B006** kızılımsı parlak güzellik — kızıllıkla toprak rengi arası renk · kızılımsı ya da açık kestane renkte · güzel ve aydınlık yüzlü · saçtaki güçlü kızıllık · demir ve benzeri şeylerde parlaklık
  أصل واحد وهو لون من الألوان أصله الحمرة ووجه صبيح والصبح شدة حمرة في الشعر (maqayis)؛ الصبحة لون بين الحمرة والغبرة ورجل صبيح الوجه جميله (jamhara)؛ الصباحة الجمال ورجل أصبح وأسد أصبح بين الصبح والأصبح قريب من الأصهب (sihah)؛ الصبح شدة حمرة في الشعر وقيل صبح فلان أي وضؤ (mufradat)
- **B007** günün başı uykusu — günün başında ya da gün aydınlanınca uyuma
  التصبح النوم بالغداة (maqayis;mufradat)؛ الصبحة النوم بالغداة (jamhara)؛ ينام الصبحة أي ينام حين يصبح (sihah)
- **B008** gün doğana dek çöken deve — çökülü yerinden gün başına kadar kalkmayan dişi deve · gün başına kadar çökülü kalan dişi develer
  المصباح الناقة تبرك في معرسها فلا تنبعث حتى تصبح (maqayis)؛ ناقة مصباح والجمع مصابيح وهي التي تصبح في مبركها (jamhara)؛ المصباح الناقة التي تصبح في مبركها ولا ترتعي حتى يرتفع النهار (sihah)؛ من الإبل ما يبرك فلا ينهض حتى يصبح (mufradat)
- **B009** gün başı zaman kalıbı [kalıp] — her günün başında, gelme veya görüşme zamanı olarak · beşinci günün başında · belirli bir gün başında görüşme ya da eylem zamanı
  أتيته أصبوحة كل يوم ولقيته ذا صبوح وأتانا لصبح خامسة وصبح خامسة (maqayis)؛ أتيته لصبح خامسة وصبح خامسة وأتيته أصبوحة كل يوم ولقيته صباحا وذا صباح (sihah)
- **B010** bir duruma gelmek — bir duruma geçti, o hale geldi
  الإصباح مصدر أصبح إصباحا مثل قولهم أمسى إمساء (jamhara)؛ أصبح فلان عالما أي صار (sihah)

## ث ن ي (root_000208): 68:18 يَسْتَثْنُونَ

- **B001** iki olma, ikiye çıkarma veya ikili oluşturma — onu iki yaptı; yanına bir ikincisini kattı · ona ikinci oldu; yanında ikinci kişi olarak yer aldı · malının yarısını aldı · iki sayısı; birlikte bulunan iki öğe · iki kişiden veya iki öğeden biri · ikişer ikişer · iki çocuk doğurmuş ya da ikinci doğumunu yapmış kadın
  الاثنان في العدد معروفان؛ امرأة ثنى ولدت اثنين (maqayis)؛ ثنيته تثنية أي جعلته اثنين؛ اثنان من عدد المذكر واثنتان للمؤنث؛ هذا ثاني اثنين أي أحد الاثنين (sihah)؛ فلان ثاني اثنين أي هو أحدهما؛ وإذا فعل الرجل أمرا ثم ضم إليه أمرا آخر قيل ثنى بالأمر الثاني (tahdhib)؛ الثني والاثنان أصل لمتصرفات هذه الكلمة؛ كنت له ثانيا أو ضممت إليه ما صار به اثنين (mufradat)
- **B002** önderden sonra gelen veya alt sıradaki kişi — önderin ardından gelen, ondan aşağı sıradaki kişi · ailesinin en düşük konumdaki kişisi
  الثنى والثنيان الذي يكون بعد السيد كأنه ثانية (maqayis)؛ الثنيان بالضم الذي يكون دون السيد في المرتبة؛ فلان ثنية أهل بيته أي أرذلهم (sihah)؛ الذي يجيء ثانيا في السؤدد ولا يجيء أولا ثنى وثنيان وثني (tahdhib)؛ الثنيان الذي يثنى به إذا عد السادات؛ فلان ثنية أهل بيته كناية عن قصور منزلته (mufradat)
- **B003** bir şeyi ikinci kez ya da art arda yineleme — iki kez veya art arda yapılan iş · ödemenin ikinci kez alınmaması; ayrıca geri dönülmemesi yorumu · payı yeniden almak veya iyiliği yinelemek; ayrıca kesilen kura hayvanından artan paylar
  الثنى الأمر يعاد مرتين؛ لا ثنى في الصدقة يعني لا تؤخذ في السنة مرتين (maqayis)؛ الثني مقصور الأمر يعاد مرتين؛ لا ثني في الصدقة أي لا تؤخذ في السنة مرتين؛ مثنى الأيادي أن يأخذ القسم مرة بعد مرة (sihah)؛ الثنى إعادة الشيء مرة بعد مرة؛ مثنى الأيادي أن يعيد معروفه مرتين أو ثلاثا (tahdhib)؛ الثنى ما يعاد مرتين؛ لا ثنى في الصدقة أي لا تؤخذ في السنة مرتين (mufradat)
- **B004** tekrar okunan Kur'an bütünü ya da bölümleri — tekrar tekrar okunan Kur'an bütünü, ayetleri veya bölümleri · okunup yinelenen kitap parçası
  المثناة ما قرئ من الكتاب وكرر؛ سبعا من المثاني أراد أن قراءتها تثنى وتكرر (maqayis)؛ المثاني من القرآن ما كان أقل من المائتين؛ فاتحة الكتاب مثاني لأنها تثنى في كل ركعة؛ جميع القرآن مثاني (sihah)؛ سمى الله القرآن كله مثاني؛ وسمى فاتحة الكتاب مثاني؛ المثاني ما دون المئين (tahdhib)؛ سميت سور القرآن مثاني لأنها تثنى على مرور الأوقات وتكرر (mufradat)
- **B005** bükme, katlama ve yönünden çevirme — bir şeyi bükmek, eğmek veya katlamak · alıkoymak ya da yöneldiği yerden çevirmek · içindekini gizlemek için kapanmak · yanını çevirerek yüz çevirmek · bir şeyin katları ve kıvrımları · adı ilk sırada sayılırken parmakların büküldüğü kimse
  ثنيت الشيء إذا حنيته وعطفته وطويته؛ كل شيء عطفته فقد ثنيته؛ يثنون صدورهم أي يطوون ما فيها ويسترونه؛ إذا أراد الرجل وجها فصرفته عن وجهه قلت ثنيته ثنيا؛ ثني الثوب لما كف من أطرافه (tahdhib)؛ الثنى واحد أثناء الشيء أي تضاعيفه؛ في ثنى كتابي أي في طيه؛ ثنيت الشيء ثنيا عطفته؛ ثناه أي كفه؛ انثنى أي انعطف (sihah)؛ يقال للاوي الشيء قد ثناه؛ يثنون صدورهم؛ ثاني عطفه عبارة عن التنكر والإعراض؛ ثنيت الشيء أثنيه عقدته بثنايين (mufradat)
- **B006** dağ ya da vadi kıvrımındaki geçit — dağ veya vadinin kıvrımı ya da kesildiği yer · yokuş yolu veya çıkılarak aşılan dağ geçidi
  الثني من الوادي والجبل منعطفه؛ الثنية طريق العقبة (sihah)؛ مثاني الوادي ومحانيه معاطفه؛ كل عقبة مسلوكة ثنية وجمعها ثنايا وهي المدارج أيضا (tahdhib)؛ الثنية من الجبل ما يحتاج في قطعه وسلوكه إلى صعود وحدود فكأنه يثني السير (mufradat)
- **B007** iki uçlu bağlama ipi ve katlanmış dizgin ucu — saç veya yünden yapılan, iki ucuyla bağlanan ip · devenin iki ön ayağını tek ipin iki ucuyla bağladı · hayvan bağı ve benzeri katlanmış ip · dizginin burun bağındaki katlanmış ucu
  الثناية حبل من شعر أو صوف؛ المثناة طرف الزمام في الخشاش كأنه ثاني الزمام (maqayis)؛ الثناية حبل من شعر أو صوف؛ عقلت البعير بثنايين؛ ثني الحبل ما ثنيت (sihah)؛ مثنية بثنايين؛ يسمى ذلك الحبل الثناية؛ ثنيا الحبل طرفاه؛ الثناية حبل يشد طرفاه في قتب السانية (tahdhib)؛ ثنيت الشيء أثنيه عقدته بثنايين؛ المثناة ما ثني من طرف الزمام (mufradat)
- **B008** genel hükmün bir bölümünü kapsam dışında bırakma — genel sözün doğurduğu hükmün bir bölümünü kaldırma · yeminde konan dışarıda bırakma veya koşul kaydı · kesilen hayvanın sahibince ayrılan başı veya ayakları · inancı uğruna ölenlerin toplu çarpılmadan ayrı tutulduğu sözü
  الثنيا من الجزور الرأس أو غيره إذا استثناه صاحبه؛ معنى الاستثناء من قياس الباب (maqayis)؛ الثنيا بالضم الاسم من الاستثناء وكذلك الثنوي بالفتح (sihah)؛ حلف يمينا ليس فيها ثنيا ولا ثنوى ولا ثنية ولا مثنوية ولا استثناء؛ الثنيا المنهي عنها في البيع أن يستثنى منه شيء مجهول؛ الثنيا من الجزور الرأس والقوائم (tahdhib)؛ حلف يمينا فيها ثنيا وثنوى وثنية ومثنوية؛ الاستثناء إيراد لفظ يقتضي رفع بعض ما يوجبه عموم لفظ متقدم (mufradat)
- **B009** ön kesici diş ve bu dişle belirlenen hayvan yaş evresi — ön kesici dişlerden biri · ön kesici dişini dökmüş veya bu diş yaşına girmiş hayvan · hayvan ön kesici dişini döktü
  الثنية واحدة الثنايا من السن؛ الثني الذي يلقى ثنيته (sihah)؛ ثنايا الإنسان في فمه الأربع التي في مقدم فيه؛ البعير إذا استكمل الخامسة وطعن في السادسة فهو ثني؛ الثني من الغنم الذي استكمل الثانية ودخل في الثالثة (tahdhib)؛ الثنية من السن تشبيها بالثنية من الجبل في الهيئة والصلابة؛ الثني من الشاة ما دخل في السنة الثانية وما سقطت ثنيته من البعير (mufradat)
- **B010** iyi yönlerini yeniden anarak övme — iyi yönleri zaman zaman yeniden anılarak söylenen övgü · onu iyi sözlerle andı ve övdü
  أثنى عليه خيرا والاسم الثناء (sihah)؛ الثنوى والثناء ما يذكر في محامد الناس فيثنى حالا فحالا ذكره يقال أثني عليه؛ يصح أن يكون ذلك من الثناء (mufradat)
- **B011** hareket ederken bedeni, boynu veya kalçayı bükme — salınarak veya kurumlu biçimde yürümek · hayvanın boynunu koşarken bükmek · inerken kalçasını bükmek · hayvanın dizleri ve dirsekleri
  يقال للفارس إذا ثنى عنق دابته جاء ثاني العنان؛ جاء سابقا ثانيا إذا جاء وقد ثنى عنقه نشاطا؛ ثنى وركه فنزل (tahdhib)؛ تثنى في مشيته تأود (sihah)؛ تثنى في مشيته نحو تبختر (mufradat)

## ط و ف (root_000957): 68:19 فَطَافَ, 68:19 طَآئِفٌ

- **B001** bir şeyin çevresinde dolaşma — bir şeyin çevresinde dolaşmak · yapının çevresinde dönmek · çevresinde dolaşma · tekrar tekrar çevresinde dolaşmak · bir şeyin çevresini dolaşmak · bir konuyu her yönüyle kuşatıp incelemek · çokça dolaşmak · çok dolaşan adam · sürekli dolaşan hizmetçiler · bir şeyin çevresinde yürüme
  طاف به وبالبيت يطوف طوفا وطوافا واطاف به واستطاف (maqayis)؛ طاف بالبيت يطوف فالمصدر طواف (ayn)؛ طاف حول الشئ يطوف طوفا وطوفانا وتطوف واستطاف (sihah)؛ الطوف المشي حول الشيء؛ الطوافون عبارة عن الخدم (mufradat)
- **B002** her yanı kaplayan baskın su veya olay — her yanı kaplayan baskın su, yağmur veya olay
  لما يدور بالأشياء ويغشيها من الماء طوفان (maqayis)؛ الطوفان الماء الذي يغشى كل مكان ويشبه به الظلام (ayn)؛ الطوفان المطر الغالب والماء الغالب يغشى كل شئ (sihah)؛ الطوفان كل حادثة تحيط بالإنسان (mufradat)
- **B003** kişiye gelip yaklaşan varlık, görüntü veya olay — kişiye gelip dokunan görünmeyen varlık, görüntü veya olay · zihinde beliren görüntü · ona gelip yaklaşmak
  الطيف والطائف ما أطاف بالإنسان من الجنان؛ في الخيال طاف وأطاف (maqayis)؛ أطاف به أي ألم به وقاربه (sihah)؛ استعير الطائف من الجن والخيال والحادثة؛ طيف خيال الشيء وصورته (mufradat)
- **B004** topluluk veya bütünden ayrılan parça — bir veya daha çok kişiden oluşabilen topluluk · bir şeyden veya kumaştan ayrılan parça
  الطائفة من الناس فكأنها جماعة تطيف بالواحد أو بالشيء؛ طائفة من الثوب أي قطعة منه (maqayis)؛ طائفة من الناس والليل أي قطعة (ayn)؛ الطائفة من الشئ قطعة منه (sihah)؛ الطائفة من الناس جماعة منهم ومن الشيء القطعة منه (mufradat)
- **B005** gece dolaşan koruma görevlisi — geceleri dolaşarak koruma yapan görevli
  الطائف وهو العاس (maqayis)؛ الطائف العاس بالليل (ayn)؛ الطائف العسس (sihah)؛ الطائف لمن يدور حول البيوت حافظا (mufradat)
- **B006** bağlı tulum veya ağaçtan yapılan yük ve geçiş salı — bağlı tulumlardan veya ağaçtan yapılan yük ve geçiş salı
  الطوف قرب ينفخ فيها ثم يشد بعضها إلى بعض كهيئة سطح فوق الماء يحمل عليها الميرة ويعبر عليها (ayn)؛ الطوف قرب ينفخ فيها ثم يشد بعضها إلى بعض فتجعل كهيئة السطح يركب عليها في الماء ويحمل عليها وهو الرمث وربما كان من خشب (sihah)
- **B007** örtmeceli dışkı adı ve dışkılamaya gitme — örtmeceli olarak dışkı · dışkılamaya gitmek
  الطوف الغائط؛ طاف يطوف طوفا واطاف اطيافا إذا ذهب إلى البراز ليتغوط (sihah)؛ الطوف كني به عن العذرة (mufradat)
- **B008** yayın uç ile göbek arasındaki göbeğe bitişik kesimi [kalıp] — yayın dış ucu ile göbeği arasındaki göbeğe bitişik kesim
  طائف القوس فهو ما يلي أبهرها (maqayis)؛ طائف القوس ما بين السية والابهر (sihah)؛ طائف القوس ما يلي أبهرها (mufradat)
- **B009** boynunun çevresinden yakalamak [kalıp] — boynunun çevresinden yakalamak · boynunun çevresinden yakalamak
  أخذه بطوف رقبته وبطاف رقبته مثل صوف رقبته (sihah)
- **B010** yerleşimi kuşatan sağlam duvar ve bundan türeyen yer adı — yerleşimi kuşatan sağlam duvar ve bu duvardan adını alan yerleşim
  الطائف الذي بالغور سمي به الحائط الذي بنوا حولها في الجاهلية حصنوها به (ayn)؛ طائف بلاد ثقيف (sihah)

## ن و م (root_001568): 68:19 نَآئِمُونَ

- **B001** uyku ve uyuma — uyku · uyumak · uyku; uyuma
  منه النوم؛ نام ينام نوما ومناما (maqayis)؛ ينام نوما فهو نائم إذا رقد (ayn;tahdhib)؛ النوم معروف (sihah)؛ المنام النوم (mufradat)
- **B002** çok uyuma ve uykunun bastırması — çok uyuyan · çok uyuyan kimse · uykucu; çok uyuyan · uykusu bastırdı
  نؤوم ونومة كثير النوم (maqayis;mufradat)؛ يا نومان للكثير النوم (ayn;sihah)؛ أخذه نوام إذا جعل النوم يعتريه (sihah)؛ رجل نومان كثير النوم ورجل نومة ينام كثيرا (tahdhib)
- **B003** uyur gibi yapmak — uyur gibi yapmak · uyuma isteğiyle uyur gibi yapmak
  استنام أيضا إذا تناوم شهوة للنوم (ayn)؛ تناوم أرى من نفسه أنه نائم وليس به (sihah)؛ استنام الرجل بمعنى تناوم شهوة للنوم (tahdhib)
- **B004** adı sanı duyulmayan, önemsenmeyen kimse — adı sanı duyulmayan, önemsenmeyen kimse · dalgın, çevresinden habersiz kimse
  رجل نومة خامل لا يؤبه له (maqayis)؛ رجل نومة أيضا أي خامل الذكر (ayn)؛ رجل نومة أي لا يؤبه له (sihah)؛ النومة الخامل الذكر الغامض في الناس (tahdhib)؛ النومة أيضا خامل الذكر (mufradat)؛ رجل نويم ونومة أي مغفل (ayn;tahdhib)
- **B005** güvenip içi rahat etmek — birine ya da bir şeye güvenip içi rahat etmek
  استنام لي فلان إذا اطمأن إليه وسكن (maqayis)؛ استنام فلان إلى فلان إذا أنس به واطمأن إليه (ayn;tahdhib)؛ استنام إليه أي سكن إليه واطمأن (sihah)؛ استنام فلان إلى كذا اطمأن إليه (mufradat)؛ غير نائم أي غير واثق به (tahdhib)
- **B006** uyku örtüsü — uyumak için kullanılan örtü veya tüylü yaygı
  المنامة القطيفة لأنه ينام فيها (maqayis;tahdhib)؛ المنامة ثوب ينام فيه وهو القطيفة (sihah;mufradat)؛ ربما سموا الدكان منامة (sihah)
- **B007** pazarın durgunlaşması veya giysinin eskimesi [kalıp] — pazar durgunlaştı · giysi ya da kürk eskidi
  نامت السوق كسدت (maqayis;sihah;mufradat)؛ نامت السوق وحمقت إذا كسدت (tahdhib)؛ نام الثوب أخلق (maqayis;sihah;tahdhib;mufradat)؛ نام الثوب والفرو إذا أخلق (tahdhib)
- **B008** ölüm, öldürme ve ölü beden — hayvan öldü · onları öldürdü · ölü hayvan
  نامت الشاة وغيرها من الحيوان إذا ماتت؛ فأنيموهم أي اقتلوهم؛ النائمة الميتة؛ النامية الجثة (tahdhib)
- **B009** hareketten sonra durup yerinde kalmak [kalıp] — hareketi kesilip durmak · suyun yerinde durup kalması
  أصل صحيح يدل على جمود وسكون حركة (maqayis)؛ كل شيء سكن فقد نام (tahdhib)؛ ما نامت السماء الليلة مطرا (tahdhib)؛ نام الماء إذا دام وقام ومنامه حيث يقوم (tahdhib)
- **B010** ince kürk — ince kürk
  النيم الفرو الرقيق (ayn)

## ن د و (root_001486): 68:21 فَتَنَادَوْا۟, 68:48 نَادَىٰ

- **B001** topluluğun buluşma yeri ve toplantısı — toplantı yeri, toplantı ve orada bulunanlar · toplanmış topluluğun buluşması · danışma toplantısı ve buluşma yeri · toplanma yeri ve toplantı · danışmak üzere toplanılan yer · toplantıya katıldım · topluluğu toplantıda bir araya getirdim · onunla toplantıda oturdu veya danıştı
  النادي والندى المجلس يندو القوم حواليه (maqayis)؛ الندى مجلس القوم ومتحدثهم وكذلك الندوة والنادي والمنتدى (sihah)؛ النادي المجلس يندو إليه من حواليه (tahdhib)؛ قيل للمجلس النادي والمنتدى والندي (mufradat)
- **B002** yüksek sesle çağırma ve sesin uzağa erişmesi — seslenme ve yüksek sesle çağırma · ona seslendi ve onu çağırdı · birbirlerine seslendiler · namaza çağrı · çağrıda bulunan kimse · sesin eriştiği uzaklık ve yayılma · sesi daha uzağa ulaşan
  النداء الصوت وناداه مناداة ونداء أي صاح به (sihah)؛ النداء رفع الصوت وظهوره (mufradat)؛ النداء ممدود والدعاء أرفع الصوت وندى الصوت بعد مذهبه (tahdhib)
- **B003** çiğ, yağmur ve bunların oluşturduğu ıslaklık — çiğ, nem, ıslaklık veya yağmur · toprağın nemi ve ıslaklığı · ıslandı ve nemlendi · onu ıslattı · nemli toprak · nemli ağaç · hayvansal yağ
  الأصل الآخر الندى من البلل (maqayis)؛ الندى المطر والبلل وندى الأرض نداوتها وبللها (sihah)؛ ندى الماء فمنه المطر وما أصابك من البلل (tahdhib)؛ أصل النداء من الندى أي الرطوبة ويسمى الشجر ندى (mufradat)
- **B004** eli açıklık ve bol iyilikte bulunma — cömertlik, iyilik ve bağış · eli açık ve cömert · ondan daha cömert ve daha çok iyilik eden · arkadaşlarına karşı cömert davranır · adamın bağışı ve iyiliği çoğaldı
  وهو أندى من فلان أي أكثر خيرا منه وهو يتندى على أصحابه (maqayis)؛ الندى الجود وفلان ندي الكف إذا كان سخيا (sihah)؛ ندى الخير هو المعروف وإن يده لندية بالمعروف (tahdhib)؛ يعبر عن السخاء بالندى (mufradat)
- **B005** kötülüğe bulaşma ve utandırıcı leke — elimi onun hoşlanmayacağı bir kötülüğe bulaştırmadım · utandırıcı eylemler veya sözler
  ما نديت كفي لفلان بشيء يكرهه (maqayis)؛ المنديات المخزيات وما نديت بشيء تكرهه (sihah)؛ ما نديني من فلان شيء أكرهه ما بلني ولا أصابني والمنديات المخزيات (tahdhib)؛ منديات الكلم المخزيات (mufradat)
- **B006** hayvanları su ile yakın otlak arasında dolaştırma — develerin sudan yakın otlağa gidip yeniden suya dönmesi · develer iki sulama arasında otladı · develerini su ile otlak arasında gidip gelir duruma getirdi · hayvanların iki sulama arasında otladığı yer · atları su ile otlak arasında dolaştırma; ayrıca terleyinceye dek çalıştırma
  ندوة الإبل أن تندو من المشرب إلى المرعى القريب منه ثم تعود إلى الماء (maqayis)؛ ندت الإبل إذا رعت فيما بين النهل والعلل والموضع مندى (sihah)؛ التندية في الإبل والخيل والتندية معنى آخر وهو تضمير الخيل حتى تعرق (tahdhib)
- **B007** dişi devenin soyca seçkin develere çekmesi [kalıp] — dişi deve soyca seçkin develere çekiyor
  هذه الناقة تندو إلى نوق كرام أي تنزع في النسب (sihah)؛ إن هذه الناقة تندو إلى نوق كرام أي تنزع إليها في النسب (tahdhib)
- **B008** seslenircesine belirginleşme ve kendini belli etme [kalıp] — şey seslenircesine belirginleşti · yol kendini açıkça gösteriyor · onu bildirdim veya ona açıkça gösterdim
  نادى ظهر وناديته علمته وهذا الطريق يناديك (tahdhib)؛ كالكرم إذ نادى أي ظهر ظهور صوت المنادي (mufradat)
- **B009** merkezden ayrılıp uzakta veya dışta kalma — zaman zaman ortaya çıkan söz parçaları · uzak yanlar ve uçlar · o kişi ayrılıp uzaklaştı · sudan uzakta bulunan hurma ağaçları · onlardan hiç kimse kalmadı
  نوادي كلامك أي ما يخرج منك وقتا بعد وقت؛ النوادي النواحي؛ ندا فلان يندو ندوا إذا اعتزل وتنحى؛ الناديات من النخيل البعيدة من الماء؛ لم يند منهم ناد لم يبق منهم أحد (tahdhib)

## ECHO ن د ي (root_001487): for 68:21 فَتَنَادَوْا۟, 68:48 نَادَىٰ: withheld observed target; not identity

- **B001** yüksek sesle seslenme ve çağırma — yüksek sesli çağrı ve sesleniş · ona seslenip çağırdı · birbirlerine seslendiler
  النداء الصوت وقد يضم مثل الدعاء (sihah)؛ ناداه مناداة ونداء أي صاح به (sihah)؛ النداء رفع الصوت وظهوره (mufradat)؛ وقد يقال ذلك للصوت المجرد وللمركب الذي يفهم منه المعنى (mufradat)؛ ندى الصوت بعد مذهبه والنداء ممدود والدعاء أرفع الصوت وقد ناديته نداء (tahdhib)
- **B002** sesin erişim uzaklığı ve menzili — sesin uzaklara erişmesi ve sürmesi · sesi daha uzağa erişen veya daha yüksek çıkan · son sınır, menzil
  ومن الباب ندى الصوت بعد مذهبه وهو أندى صوتا منه أي أبعد (maqayis)؛ الندى الغاية مثل المدى (sihah)؛ الندى أيضا بعد ذهاب الصوت (sihah)؛ فلان أندى صوتا من فلان إذا كان بعيد الصوت (sihah)؛ ندى الصوت بعد مذهبه (tahdhib)؛ فلان أندى صوتا من فلان أي أبعد مذهبا وأرفع صوتا (tahdhib)؛ صوت ندي رفيع (mufradat)
- **B003** topluluğun buluşup görüştüğü toplantı yeri — topluluğun toplantı yeri · toplantı ve sohbet yeri · toplanma ve danışma kurulu · buluşma ve toplantı yeri · yakın topluluğu veya toplantı çevresi · toplantıya katıldı · topluluğu toplantı yerinde bir araya getirdi · onunla toplantı yerinde oturup görüştü
  الأول النادي والندى المجلس يندو القوم حواليه وإذا تفرقوا فليس بندى (maqayis)؛ دار الندوة بمكة لأنهم كانوا يندون فيها أي يجتمعون (maqayis)؛ ناديته جالسته في الندى (maqayis)؛ الندى مجلس القوم ومتحدثهم وكذلك الندوة والنادي والمنتدى (sihah)؛ فإن تفرق القوم فليس بندي (sihah)؛ فليدع ناديه أي عشيرته وإنما هم أهل النادي (sihah)؛ ندوت أي حضرت الندي وانتديت مثله (sihah)؛ ندوت القوم جمعتهم في الندي (sihah)؛ النادي المجلس يندو إليه من حواليه ولا يسمى ناديا حتى يكون فيه أهله (tahdhib)؛ أناديك أشاورك وأجالسك من النادي (tahdhib)؛ يعبر عن المجالسة بالنداء حتى قيل للمجلس النادي والمنتدى والندي (mufradat)
- **B004** hayvanı su ile yakın otlak arasında döndürme — develerin su ile yakın otlak arasında gidip dönmesi · hayvanı sulayıp kısa süre otlattıktan sonra yeniden suya getirme · atın su, otlak ve dönüş döngüsünü yapması · hayvanın su ile otlak arasında döndürüldüğü yer · develerin sulama yeri · iki sulama arasındaki otlama öğünü
  ندوة الإبل أن تندو من المشرب إلى المرعى القريب منه ثم تعود إلى الماء (maqayis)؛ وكذلك تندو من الحمض إلى الخلة وأندى إبله من هذا (maqayis)؛ ندت الإبل إذا رعت فيما بين النهل والعلل فهي نادية (sihah)؛ أنديتها أنا ونديتها تندية والموضع مندى (sihah)؛ الندوة بالضم موضع شرب الإبل (sihah)؛ التندية في الإبل والخيل أن يوردها الماء ثم يردها إلى المرعى ساعة ثم يعيدها (tahdhib)؛ وقد ندا الفرس يندو إذا فعل ذلك (tahdhib)؛ الندى الأكلة بين الشربتين (tahdhib)
- **B005** ıslaklık ve nem; yağmur ve çiy — yağmur, çiy, ıslaklık ve nem · ıslanıp nemlenmek · yerin nemi ve ıslaklığı
  الأصل الآخر الندى من البلل معروف (maqayis)؛ الندى المطر والبلل (sihah)؛ ندى الأرض نداوتها وبللها (sihah)؛ ندي الشيء إذا ابتل فهو ند (sihah)؛ ندى الماء فمنه المطر أصابه ندى من طل ويوم ندي وليلة ندية (tahdhib)؛ الندى ما أصابك من البلل (tahdhib)؛ أصل النداء من الندى أي الرطوبة (mufradat)
- **B006** yağmur nemiyle yetişen otlak bitkisi — yağmur nemiyle yetişen ot ve otlak bitkisi · nemle yetişmiş ağaç
  الندى الكلأ (sihah)؛ تسف الند (sihah)؛ قيل للنبت ندى لأنه عن ندى المطر نبت (tahdhib)؛ يسمى الشجر ندى لكونه منه وذلك لتسمية المسبب باسم سببه (mufradat)
- **B007** hayvan yağı — hayvan yağı
  ربما عبروا عن الشحم بالندى (maqayis)؛ الندى الشحم (sihah)؛ فالندى الأول المطر والثاني الشحم (sihah)؛ قيل للشحم ندى لأنه عن ندى النبت يكون (tahdhib)؛ أراد بالندى الثاني الشحم وبالأول الغيث (tahdhib)
- **B008** iyilik ve vermede eli açıklık — cömertlik, iyilik ve bol verme · eli açık, cömert · vermesi ve iyiliği arttı · arkadaşlarına cömert davranıyor · ondan hiçbir cömertlik payı elde etmedim
  هو أندى من فلان أي أكثر خيرا منه (maqayis)؛ وهو يتندى على أصحابه أي يتسخى (maqayis)؛ الندى الجود (sihah)؛ فلان ندي الكف إذا كان سخيا (sihah)؛ فلان يتندى على أصحابه أي يتسخى (sihah)؛ الندوة السخاء (tahdhib)؛ ندى الخير هو المعروف (tahdhib)؛ أندى الرجل إذا كثر نداه على إخوانه وكذلك انتدى وتندى (tahdhib)؛ يعبر عن السخاء بالندى (mufradat)؛ فلان أندى كفا من فلان وهو يتندى على أصحابه أي يتسخى (mufradat)
- **B009** kötü bir şeye uğrama veya bulaşma ve utandırıcı şeyler — istemediğim bir şeye uğramadım · utandırıcı sözler veya davranışlar · yasak kana bulaşmak
  ما نديت كفي لفلان بشيء يكرهه (maqayis)؛ المنديات المخزيات ويقال ما نديت بشيء تكرهه (sihah)؛ ما نديت كفي بشر وما نديت بشيء تكرهه (tahdhib)؛ من لقي الله ولم يتند من الدم الحرام بشيء (tahdhib)؛ منديات الكلم المخزيات التي تعرف (mufradat)
- **B010** dişi devenin seçkin bir soya çekmesi [kalıp] — dişi deve soyca seçkin develere çekiyor
  هذه الناقة تندو إلى نوق كرام أي تنزع في النسب (sihah)؛ هذه الناقة تندو إلى نوق كرام أي تنزع إليها في النسب (tahdhib)
- **B011** açıkça belirme, bildirme ve yön gösterme — açıkça belirdi · ona bildirdi ve açıkladı · bu yol sana açıkça yön gösteriyor
  نادى ظهر (tahdhib)؛ ناديته علمته (tahdhib)؛ هذا الطريق يناديك (tahdhib)؛ كالكرم إذ نادى من الكافور أي ظهر ظهور صوت المنادي (mufradat)
- **B012** aralıklı çıkan sözler ve uzakta kalan uçlar — zaman zaman ağızdan çıkan sözler · yanlar ve uzak uçlar · ayrılıp uzaklaştı · sudan uzaktaki hurma ağaçları
  نوادي كلامك أي ما يخرج منك وقتا بعد وقت (tahdhib)؛ النوادي النواحي (tahdhib)؛ ندا فلان يندو ندوا إذا اعتزل وتنحى (tahdhib)؛ أراد بنواديه قواصيه (tahdhib)؛ الناديات من النخيل البعيدة من الماء (tahdhib)
- **B013** renk şeridi veya sıcak külde pişirme — etin renginden farklı bir yağ şeridi, gökkuşağı veya bulut kızıllığı · eti sıcak küle gömüp pişirdi · pişmiş yemek
  إذا همز تغير إلى شيء يدل على طرائق وآثار (maqayis)؛ الندأة طريقة من الشحم مخالفة للون اللحم (maqayis)؛ الندأة قوس قزح والحمرة التي تكون في الغيم نحو الشفق (maqayis)؛ ندأت اللحم في الملة دفنته حتى ينضج (maqayis)؛ الندىء مثل الطبيخ (maqayis)

## ECHO ن و د (root_001563): for 68:21 فَتَنَادَوْا۟, 68:48 نَادَىٰ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## غ د و (root_001076): 68:22 ٱغْدُوا۟, 68:25 وَغَدَوْا۟

- **B001** günün ilk vakti ve bu vakitte yola çıkma — günün erken vaktinde gitmek · günün ilk vakti ve bu vakitteki gidiş · erken ibadet ile güneşin doğuşu arasındaki vakit · günün erken vakti · günün erken vaktinde yola çıkma · birinin yanına günün erken vaktinde gitmek · ertesi günün erken vakti · sabahları ve akşamları gidip gelmek
  أصل صحيح يدل على زمان؛ الغدو يقال غدا يغدو (maqayis)؛ غدا غدوا واغتدى اغتداء (ayn)؛ الغدوة ما بين صلاة الغداة وطلوع الشمس؛ الغدو نقيض الرواح؛ غاداه أي غدا عليه (sihah)؛ غدوت أغدو غدوا؛ الغدو جمع مثل الغدوات (tahdhib)؛ الغدوة والغداة من أول النهار؛ قد غدوت أغدو (mufradat)
- **B002** yarın — ertesi günün erken vakti · yarın · yarın
  أفعل ذلك غدا؛ والأصل غدوا (maqayis)؛ الغد أصله غدو (sihah)؛ قدمت لغد بغير واو فإذا صرفوها قالوا غدوت أغدو (tahdhib)؛ غد يقال لليوم الذي يلي يومك الذي أنت فيه (mufradat)
- **B003** günün erken vaktinde beliren bulut — günün erken vaktinde beliren bulut · günün erken vaktinde beliren bulutlar
  الغادية سحابة تنشأ صباحا (maqayis)؛ الغادية سحابة تنشأ صباحا وجمعها غوادي (ayn)؛ الغادية سحابة تنشأ صباحا (sihah)؛ الغادية سحابة تنشأ صباحا وجمعها الغوادي (tahdhib)؛ الغادية السحاب ينشأ غدوة (mufradat)
- **B004** günün başında yenen yemek — günün başında yenen yemek · günün ilk öğününü yemek · günün ilk öğününü yiyen kişi · günün ilk öğününü yiyen kişi
  الغداء الطعام بعينه سمي بذلك لأنه يؤكل في ذلك الزمان (maqayis)؛ الغداء ما يؤكل من أول النهار (ayn)؛ الغداء الطعام بعينه وهو خلاف العشاء؛ تغدى؛ الغديان المتغدي (sihah)؛ الغداء ما يؤكل أول النهار وقد تغدى الرجل فهو متغد (tahdhib)؛ الغداء طعام يتناول في ذلك الوقت (mufradat)
- **B005** gebe hayvanın karnındaki yavru — gebe hayvanın karnındaki yavru; ayrıca beklenen yavruya dayalı belirsiz satış
  الغدوي كل ما كان في بطون الحوامل وربما جعل في الشاء خاصة (ayn)؛ الغدوي بالدال أن يبيع الشيء بنتاج ما نزى به الكبش ذلك العام؛ كل ما في بطون الحوامل غدوي من الإبل والشاء؛ نهي عن الغدوي وهو كل ما في بطون الحوامل؛ الغدوي الحمل والجدي لا يغذى بلبن أمه (tahdhib)

## ح ر ث (root_000303): 68:22 حَرْثِكُمْ

- **B001** çalışarak kazanma ve biriktirme — kazanç, biriktirme ve çalışma · mal edinme ya da kazanç arama · dünya hayatı veya ölüm sonrası için çalışmak · ailesinin geçimi için kazanıp çabalamak · kazanan kimse · ailesinin geçimi için kazanmak; ses değişmeli biçim
  الاحتراث من كسب المال (ayn;tahdhib)؛ الحرث كسب المال وجمعه (sihah)؛ حرث الرجل لدنياه أو آخرته إذا عمل لها (jamhara)؛ الحرث العمل للدنيا والآخرة (tahdhib)؛ يحرث لعياله ويحترث أي يكتسب (tahdhib)؛ الحارث معناه الكاسب (tahdhib;mufradat;maqayis)؛ هو من حرث أي كسب وجمع (maqayis-ibdal)
- **B002** toprağı hazırlayıp tohum ekme — tohumu toprağa atma ve toprağı ekime hazırlama · toprağı işleyip ekmek · ekin, ekilmiş ürün ya da ekili tarla · ekime hazırlanmış yer · çiftçiler
  الحرث قذفك الحب في الأرض (ayn;tahdhib)؛ حرث الزرع (jamhara)؛ الحرث الزرع والحراث الزراع (sihah)؛ إلقاء البذر في الأرض وتهيؤها للزرع ويسمى المحروث حرثا (mufradat)؛ من هذا الباب حرث الزرع (maqayis)
- **B003** evlilik ve cinsel birliktelik için ekim benzetmesi — evlilik ya da cinsel birliktelik için ekim benzetmesi · kadınlar, çocuk ve haz için ürün yetiştirilen yere benzetilir · kadın, kocanın çocuğunun yetiştiği yere benzetilir · karısıyla cinsel ilişkide bulunmak · dört kadınla aynı anda evli olmak · çok sık cinsel ilişkide bulunma
  الحرث النكاح (jamhara)؛ المرأة حرث الزوج مزدرع ولده (maqayis)؛ حرث الرجل امرأته والجماع الكثير (tahdhib)؛ فيهن تحرثون الولد واللذة (tahdhib)؛ بالنساء زرع ما فيه بقاء نوع الإنسان (mufradat)؛ حرث الرجل إذا جمع بين أربع نسوة (tahdhib)
- **B004** hayvanı kullanma veya kullanarak zayıf düşürme — atı kullanarak ya da sürerek zayıf düşürme · dişi devesini sürerek ya da kullanarak zayıf düşürmek · dişi deveyi zayıflayıncaya kadar sürmek veya onu kullanmak
  الإحراث هزل الخيل (ayn)؛ أحرث الرجل ناقته إذا هزلها (jamhara)؛ حرثت الناقة وأحرثتها أي سرت عليها حتى هزلت (sihah;tahdhib)؛ حرث ناقته إذا استعملها (mufradat)؛ حرث ناقته هزلها وأحرثها (maqayis)
- **B005** ateşi karıştırıp canlandırma — ateşi karıştırıp canlandırmak · ateşi karıştırmaya yarayan demir ya da tahta araç · savaşı kışkırtan şey · ateşi canlandırmaya yarayan araç
  المحراث من الحديد كهيئة المسحاة تحرك بها النار (ayn)؛ محراث الحرب ما يهيجها (ayn;tahdhib)؛ المحراث خشبة تحرك بها النار (jamhara)؛ حرثت النار حركتها (sihah)؛ الحرث إشعال النار ومحراث النار مسحاتها (tahdhib)؛ حرثت النار ولما تهيج به النار محرث (mufradat)
- **B006** metni inceleyip üzerinde düşünme — kutsal metni incelemek ya da çokça okumak · kutsal metni uzun süre inceleyip üzerinde düşünmek · bir kitabı araştırıp üzerinde düşünme · bilgi edinip derinlemesine araştırmak
  احرث القرآن أي ادرسه (sihah)؛ حرث إذا تفقه وفتش (tahdhib)؛ الحرث تفتيش الكتاب وتدبره (tahdhib)؛ حرثت القرآن إذا أطلت دراسته وتدبرته (tahdhib)؛ احرث القرآن أي أكثر تلاوته (mufradat)
- **B007** kiriş için kertik ve oluk hazırlama — ok kertiğinde yayın kirişinin geçtiği oluk · ok kertiklerindeki kiriş olukları · yayın ucunda kiriş için açılmış kertik · yayda kiriş halkası için yer hazırlamak · yay ucunda kiriş yerini son delme işleminden önce hazırlamak
  الحراث مجرى الوتر في الفوق والجمع أحرثة (jamhara)؛ الأحرثة مجاري الأوتار في الأفواق لأنها تجمعها (maqayis)؛ الحرثة الفرضة التي في طرف القوس للوتر (tahdhib)؛ حرثت القوس إذا هيأت موضعا لعروة الوتر (tahdhib)؛ الزندة تحرث ثم تكظر بعد الحرث (tahdhib)
- **B008** toprağı çiğneyip bozma veya ekim için çevirme — insanların çiğneyip kabartarak bozduğu toprak · toprağı çiğneyip bozmak veya ekim için çevirmek · toynaklarla dövülmüş yol
  أرض محروثة ومحرثة وطئها الناس حتى أحرثوها وحرثوها (tahdhib)؛ وطئت حتى أثاروها وهو فساد (tahdhib)؛ تقلب للزرع (tahdhib)؛ المحجة المكدودة بالحوافر (tahdhib)
- **B009** insan erkeğinin cinsel organı dibindeki damar ya da erkek eşeğin cinsel organ kökü — erkeğin cinsel organının dibindeki damar · erkek eşeğin cinsel organının kökü
  الحَرْثة عرق في أصل أداف الرجل (tahdhib)؛ الحَرْث أصل جردان الحمار (tahdhib)
- **B010** kişi, topluluk ve yer adları — kazanan anlamıyla verilmiş bir erkek adı · geleneksel bir kişi adı · geleneksel bir kişi adı · geleneksel bir kişi adı · geleneksel bir kişi adı · aslan için kullanılan bir lakap · bir dağ tepesi adı · iki kişi ya da iki topluluk için kullanılan ikili adlandırma · bir soy topluluğunu belirten kısaltılmış ad
  به سمي الرجل حارثا (maqayis)؛ سمت العرب حارثا وحراثا وحريثا ومحرثا وحرثان (jamhara)؛ أبو الحارث كنية الأسد (sihah)؛ الحارث قلة من قلل الجولان (sihah)؛ الحارثان في باهلة (sihah)؛ أصدق الأسماء الحارث (tahdhib;mufradat)

## ط ل ق (root_000946): 68:23 فَٱنطَلَقُوا۟

- **B001** bağdan kurtarıp serbest bırakma — dişi devenin bağını çözüp salmak · bağı çözülüp serbest bırakılmış tutsak · bağsız deve · topluluktan ayrılıp onları bırakmak · ülkeden ayrılmak
  التخلية والإرسال (maqayis)؛ أطلقت الأسير أي خليته (sihah)؛ أصل الطلاق التخلية من الوثاق (mufradat)؛ التطليق التخلية والإرسال وحل العقد (tahdhib)؛ الطليق الأسير يطلق عنه إساره (ayn)
- **B002** evlilik bağını sona erdirme — evlilik bağının sona erdirilmesi · evlilik bağı sona erdirilmiş kadın · eşlerini sık sık boşayan erkek
  امرأة طالق طلقها زوجها (maqayis)؛ والطلاق تخلية سبيلها (ayn)؛ طلق الرجل امرأته تطليقا (sihah)؛ طلقت المرأة من الطلاق (tahdhib)؛ طلقت المرأة نحو خليتها فهي طالق (mufradat)
- **B003** tutulmadan ilerleyip gitme — yola çıkıp gitmek · ceylanın arkasına bakmadan ilerlemesi · at koşusunda bir koşu bölümü · atların hedefe kadar durmadan ilerlemesi · atlarını yarış alanında koşuya salmak
  انطلق الرجل ينطلق انطلاقا (maqayis)؛ إذا خلى الظبي عن قوائمه فمضى لا يلوي على شيء قيل تطلق (ayn;tahdhib)؛ الانطلاق الذهاب (sihah;mufradat)؛ عدا الفرس طلقا أو طلقين (maqayis;sihah;tahdhib;mufradat)؛ تطلقت الخيل إذا مضت طلقا لم تحتبس إلى الغاية (ayn;tahdhib)
- **B004** açık, rahat ve akıcı olma [kalıp] — güler yüzlü ve açık çehreli · dili akıcı · eli açık ve cömert · gönlüm bu işe yatmıyor · yüzü açılıp güler görünmek · kır çiçeklerinin bulut çekilince güneşe çıkması
  رجل طلق الوجه وطليقه (maqayis;ayn;sihah;tahdhib;mufradat)؛ رجل طلق اللسان وطليقه (maqayis;ayn;sihah;tahdhib)؛ طلق اليدين سمح بالعطاء (ayn;sihah;tahdhib;mufradat)؛ ما تطلق نفسي لهذا الأمر أي لا تنشرح (maqayis;ayn;sihah;tahdhib)؛ انطلق الوجه (tahdhib)؛ تطلق إذا انجلى عنها الغيم (tahdhib)
- **B005** yasaksız ve kısıtsız olma — yasak olmayan, kullanımı serbest şey · bu işten çıkmış ve bağı kalmamışsın · hükümde istisna konmamış ifade
  والطلق الشيء الحلال (maqayis)؛ الطلق بالكسر الحلال (sihah)؛ هذا لك طلق أي حلال (tahdhib)؛ قيل للحلال طلق أي مطلق لا حظر عليه (mufradat)؛ المطلق في الأحكام ما لا يقع منه استثناء (mufradat)
- **B006** deveyi otlama ve sulama için salma [kalıp] — serbestçe otlayan veya sağılmadan bırakılan dişi deve · sürünün otlayarak suya salındığı gece · çobanın bir dişi deveyi kendine ayırıp sağmaması
  الطالق الناقة ترسل ترعى حيث شاءت (maqayis;ayn;sihah;tahdhib)؛ ليلة الطلق ليلة يخلى الراعي إبله إلى الماء (maqayis;sihah;tahdhib;mufradat)؛ استطلق الراعي لنفسه ناقة (maqayis;sihah)؛ الطالق التي يتركها بصرارها (tahdhib)
- **B007** havası yumuşak ve rahat zaman [kalıp] — havası yumuşak, eziyetsiz ve uğursuz sayılmayan gün · soğuksuz, rahat ve hoş gece
  يوم طلق وليلة طلقة نقيض النحس والنحسة (ayn)؛ يوم طلق وليلة طلق إذا لم يكن فيهما قر ولا شيء يؤذى (sihah)؛ يوم طلق وليلة طلقة لا قر فيها ولا أذى (tahdhib)
- **B008** doğum sancısı — doğum sırasındaki sancı
  طلقت المرأة فهي مطلوقة إذا ضربها الطلق عند الولادة (ayn)؛ الطلق وجع الولادة (sihah)؛ الطلق طلق المخاض عند الولادة (tahdhib)
- **B009** bağırsakların sürmesi [kalıp] — bağırsakların sürmesi · ilacın bağırsakları sürmesi
  استطلق البطن وأطلقه الدواء فأسهل (ayn)؛ استطلاق البطن مشيه (sihah)؛ استطلق بطنه وأطلقه الدواء (tahdhib)
- **B010** ısırık ağrısının dinmesi — ısırılan kişinin ağrısının dinip kendine gelmesi · zehir ağrısı dinmiş veya sancıların geri dönmesinden korkulan ısırılmış kişi
  طلق السليم إذا سكن وجعه بعد العداد (maqayis;sihah)؛ طلق السليم خلاه الوجع (mufradat)؛ للسليم إذا لدغ قد طلق وذلك حين ترجع إليه نفسه (tahdhib)
- **B011** belirsiz bir ilaç ya da bitki türü — bir ilaç ya da bitki türü
  الطلق ضرب من الأدوية (sihah)؛ لضرب من الدواء أو نبت طلق (tahdhib)
- **B012** deri köstek ya da kısa sıkı bükümlü ip — deriden yapılmış köstek · kısa ve sıkı bükülmüş ip
  الطلق الحبل القصير الشديد الفتل (ayn)؛ الطلق بالتحريك قيد من جلود (sihah;tahdhib)
- **B013** bir ayağı beyaz nişansız at [kalıp] — bir ayağında beyaz nişan bulunmayan at
  فرس طلق إحدى القوائم إذا كانت إحدى قوائمها لا تحجيل فيها (sihah)
- **B014** uzun hurma ağaçlarını tozlaştırma — tozlaştırılmış uzun hurma ağacı · uzun hurma ağaçlarını tozlaştırmak
  المطلق الملقح من النخل وقد أطلق نخله وطلقها إذا كانت طوالا فألقحها (tahdhib)
- **B015** düşmana zehir içirme [kalıp] — düşmanına zehir içirmek
  أطلق عدوه إذا سقاه سما (tahdhib)
- **B016** atın koşudan sonra işemesi — atın koşudan sonra işemesi
  التطلق أن تبول الفرس بعد الجري (tahdhib)
- **B017** karındaki yol benzeri çizgiler — karın üzerindeki yol benzeri çizgiler
  في البطن أطلاق واحدها طلق وهي طرائق البطن (tahdhib)

## خ ف ت (root_000425): 68:23 يَتَخَٰفَتُونَ

- **B001** sesi alçaltıp gizlice konuşma — sesi alçaltarak gizli konuşma · alçak sesle gizli konuşma · birbirine alçak sesle konuşma · kendi aralarında gizlice görüşme · sözünü yüksek sesle açıkça söylememe · sesin alçalması ve güç duyulur olması
  أصل واحد وهو إسرار وكتمان (maqayis)؛ الخفت إسرار النطق (maqayis)؛ صوت خفيت وخفت خفوتا أي خفض خفوضا (ayn)؛ تخافت بقولته إذا لم يبينها برفع الصوت وهم يتخافتون إذا تشاوروا سرا (ayn)؛ المخافتة والتخافت إسرار المنطق والخفت مثله (sihah)؛ المخافتة والخفت إسرار المنطق (mufradat)
- **B002** sesin dinmesi; ansızın ya da fark edilmeden ölme — sesin dinmesi ve tınısının kesilmesi · ölen kişinin konuşmasının kesilip susması · ansızın ya da kimse fark etmeden ölme · Tanrı'nın onu kimse fark etmeden öldürmesi
  خفت الصوت خفوتا سكن (sihah)؛ إذا مات قد خفت أي انقطع كلامه (ayn)؛ للميت خفت إذا انقطع كلامه وسكت (sihah)؛ خفت خفاتا أي مات فجأة (sihah)؛ مات خفاتا أي لم يشعر بموته وأخفته الله (ayn)
- **B003** hastalık ya da açlıktan güçsüz düşme — erkeğin hastalık ya da açlıktan güçsüz düşmesi · hastalık ya da açlığın yol açtığı güçsüzlük
  خفت الرجل إذا أصابه ضعف من مرض أو جوع والاسم الخفات (jamhara)
- **B004** tam boya erişememiş ekin [kalıp] — tam boya erişememiş ekin
  زرع خافت كأنه بقى فلم يبلغ غاية الطول (ayn)
- **B005** yalnızken güzel, başkaları yanında sönük kalan kadın [kalıp] — yalnızken güzel, başka kadınlar yanında sönük kalan kadın
  امرأة خفوت لفوت وهي التي تأخذها العين ما دامت وحدها أي تستحسنها فإذا صارت بين النساء غمرنها (ayn)؛ الخفوت التي تخفت في جنب من كان أحسن منها (ayn)

## د خ ل (root_000464): 68:24 يَدْخُلَنَّهَا

- **B001** içeri girmek veya içeri sokmak — bir yere, zamana veya işe girmek · içeri girme veya giriş · başkasını ya da bir şeyi içeri sokmak · bir şeyin içine azar azar girmek · girme eylemi veya giriş yeri
  أصل مطرد منقاس وهو الولوج (maqayis)؛ دخل يدخل دخولا (maqayis)؛ ادخل في غار وتدخل فيه (ayn)؛ دخلت الدار وغيرها وأدخلت غيري (jamhara)؛ دخلت البيت وادخل وتدخل الشيء (sihah)؛ الدخول نقيض الخروج ويستعمل في المكان والزمان والأعمال (mufradat)
- **B002** eşiyle cinsel birleşmede bulunmak [kalıp] — eşiyle cinsel birleşmede bulunmak
  دخل بامرأته كناية عن الإفضاء إليها (mufradat)
- **B003** içte kalan yan — bir işin veya kişinin iç yüzü · giysinin bedene bakan iç kenarı · saklı tutulan iş veya açılan gizli iç yüz
  الدخلة باطن أمر الرجل وأنا عالم بدخلته (maqayis)؛ الدخلة بطانة من الأمر وعالم بدخلة أمرهم (ayn)؛ دخلل أمري إذا بثثته مكتومك (jamhara)؛ داخلة الإزار طرفه الذي يلي الجسد وداخلة الرجل باطن أمره (sihah)
- **B004** içten bozan kusur — içteki kusur, bozukluk veya kuşku · antları hile ve aldatma aracı yapmak · içten kusurlu, zayıf veya zihni bozuk · içi çürümüş palmiye · böcekçe yenmiş veya kurtlanmış yiyecek
  الدخل العيب في الحسب وكالدغل (maqayis)؛ دخل فلان وهو مدخول إذا كان في عقله دخل ونخلة مدخولة عفنة الجوف (maqayis)؛ عيب في الحسب وفي هذا الأمر دخل ودغل ودخل حسبه أو عقله (ayn)؛ في أمره دخل أي فساد (jamhara)؛ الدخل العيب والريبة ومكرا وخديعة ومدخول في عقله ونخلة مدخولة (sihah)؛ الدخل كناية عن الفساد والعداوة المستبطنة كالدغل ومدخول كناية عن بله في عقله وفساد في أصله (mufradat)
- **B005** sonradan araya katılan kimse — özel işlere alınan veya bir topluluğa dışarıdan katılan kimse · kişinin özel işlerine aldığı yakın kimse · bilmediği işlere zorla karışan kimse
  دخيلك الذي يداخلك في أمورك وبنو فلان في بني فلان دخيل (maqayis)؛ دخيلك الذي تدخله في أمورك ودخلل والمتدخل في الأمور المتكلف فيها (ayn)؛ فلان دخيل في بني فلان إذا كان من غيرهم (jamhara)؛ هم دخل في بني فلان ودخيل الرجل ودخلله الذي يداخله في أموره (sihah)؛ وعن الدعوة في النسب (mufradat)
- **B006** gelir — gelir veya içeri giren kazanç
  الدخل ما دخل ضيعة الإنسان من المنالة (ayn)؛ الدخل خلاف الخرج (sihah)
- **B007** develeri yeniden ya da araya katarak sulama — develeri ikinci kez suya götürme veya susuz deveyi sürüye katma
  الدخال في الورد أن تشرب الإبل ثم ترد إلى الحوض (maqayis)؛ سقيت الإبل دخالا إذا حملتها على الحوض ثانية والدخال في وجه آخر أن تحملها على الحوض بمرة واحدة عراكا (ayn)؛ أورد الرجل إبله دخالا (jamhara)؛ الدخال في الورد أن يشرب البعير ثم يرد من العطن إلى الحوض (sihah)؛ الدخال في الإبل أن يدخل إبل في أثناء ما لم تشرب لتشرب معها ثانيا (mufradat)
- **B008** iç içe geçme ve arada kalma — eklemlerin birbirine geçmesi · bir sinir üzerinde toplanmış et parçası · bir ana renge karışmış başka renkler · kuşun sırtıyla karnı arasındaki tüyler · ağaç köklerinin arasına girmiş ot
  كل لحمة مجتمعة دخلة والدخل من ريش الطائر ما بين الظهران والبطنان والدخل من الكلأ ما دخل منه في أصول الشجر (maqayis)؛ الدخلة في اللون تحليط من ألوان في لون والدخال مداخلة المفاصل بعضها في بعض (ayn)؛ كل لحمة مجتمعة على عصب فهي دخلة (jamhara)؛ الدخل من الكلأ ما دخل منه في أصول الشجر (sihah)
- **B009** sık ağaçlıkta barınan küçük kuş — oyuklarda ve sık ağaç altında barınan küçük kuş · bu küçük kuş adının bir çoğul biçimi · bu küçük kuş adının öteki çoğul biçimi
  بذلك سمي هذا الطائر دخلا (maqayis)؛ الدخل صغار الطير مأواها الغيران وبطون الأودية تحت شجر ملتف والجميع الدخاخيل (ayn)؛ الدخل طائر صغير وجمع دخل دخاخيل (jamhara)؛ الدخل طائر صغير والجمع الدخاليل (sihah)؛ الدخل طائر سمي بذلك لدخوله فيما بين الأشجار الملتفة (mufradat)
- **B010** taze palmiye meyvesi için küçük örgü sepet — taze palmiye meyvesi konan küçük örgü sepet
  الدوخلة سفيفة من خوص صغيرة يجعل فيها الرطب (ayn)؛ الدوخلة هذا المنسوج من الخوص يجعل فيه الرطب (sihah)؛ الدوخلة معروفة (mufradat)

## ي و م (root_001700): 68:24 ٱلْيَوْمَ, 68:39 يَوْمِ, 68:42 يَوْمَ

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

## س ك ن (root_000726): 68:24 مِّسْكِينٌ

- **B001** hareketin dinip durulması — hareketin sona erip şeyin durması · hareketi veya çalkantısı dindi ve durdu · rüzgar, yağmur ya da öfke dindi · hareketsiz, yerinde duran veya dingin
  خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك
- **B002** bir yere yerleşip orada yaşama — bir yere yerleşip orada yaşadı · konut, ev veya yaşanan yer · bir evi kira almadan oturması için verme · onu bir evde veya yerde oturttu · konut olarak kullanılan ev veya yer
  يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن
- **B003** ev halkı ve orada yaşayanlar — ev halkı ve aile üyeleri · bir yerde yaşayanlar · evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar
  السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار
- **B004** insanı rahatlatıp içini yatıştıran dayanak — insanın yanında rahatlayıp içinin yatıştığı kişi veya şey · yanında oturulup rahatlık bulunan ateş · senin yakarışların onları rahatlatır · geceyi dinlenme ve dinginleşme zamanı yaptı · eğri sırığı ateş ve yağla doğrultma
  كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها
- **B005** güven veren ağırbaşlı iç dinginlik — ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği · sandıktaki, kalpleri yatıştırıp güven veren şey · inananların kalplerine güven ve dinginlik verdi
  السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين
- **B006** yoksulluk, güçsüzlük ve ezilmişlik — yoksul ya da ezilmiş ve güçsüz kişi · yoksulluk veya ezilmişlik durumu · yoksul duruma geldi ya da boyun eğip kendini alçalttı · boyun eğdi ve alçaldı · Tanrı onu yoksul duruma düşürdü
  المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل
- **B007** kesici bıçak — kesici bıçak · bıçak yapan kimse
  السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح
- **B008** geminin kıçındaki dengeleyici yöneltme aracı — geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç · gemiyi dengede tutup çalkantısını azaltan kıç parçası
  سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به
- **B009** sabit yer ve konum bildiren özel kullanımlar — başın boyuna oturduğu yer · yerlerinizde, konumlarınızda veya alışılmış düzeninizde · belirli bir bölgedeki özel yer adı
  موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم
- **B010** yerinde kalmayı sağlayan geçimlik ve bol otlak — bulunduğu yerde geçinmeyi sağlayan yiyecekler · yerinde kalmayı sağlayan bir geçimlik · sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak
  الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه

## ح ر د (root_000305): 68:25 حَرْدٍ

- **B001** bir şeye yönelip onu amaçlama; bir işe kararlılıkla koyulma — bir şeyi amaçlayıp ona yönelme · senin yöneldiğin hedefe yöneldi · ona yönelip onu amaçladı
  القصد (maqayis;tahdhib)؛ حردت حردك أي قصدت قصدك (sihah;tahdhib)؛ حردت نحوه إذا قصدته (jamhara)؛ على جد من أمرهم (ayn;tahdhib)
- **B002** alıkoyma ve vermekten geri durma — alıkoyma ve vermekten kaçınma · eli vermeye kapalı, eli sıkı
  على منع (sihah;tahdhib)؛ الحرد المنع (tahdhib)؛ الحرد المنع من حدة وغضب (mufradat)؛ أي على امتناع (mufradat)؛ أحرد اليدين أي فيهما انقباض عن العطاء (tahdhib)
- **B003** öfkeye kapılma — öfkelenip kendisini öfkelendirene sataşmaya yönelmek · öfkeli aslan
  الغضب (maqayis;jamhara;tahdhib)؛ إذا اغتاظ فتحرش بالذي غاظه وهم به (ayn;tahdhib)؛ حرد غضب (mufradat)؛ أسد حارد وليوث حوارد (maqayis;jamhara;sihah;tahdhib)
- **B004** topluluktan çekilip ayrı ve karışmadan durma — topluluğundan ayrılıp uzaklaşmak · insanlara karışmayan, tek başına yaşayan adam · boydan ayrı yere konan ve onlara karışmayan topluluk · öteki yıldızlardan ayrı görünen yıldız · Hüzeyl ağzında tek başına bulunan kimse veya şey · adamın bir kulübeye sığınması
  التنحي والعدول (maqayis)؛ نزل فلان حريدا أي متنحيا (maqayis)؛ حي حريد لا يخالطهم (ayn;tahdhib)؛ رجل حريد المحل (jamhara;sihah;mufradat)؛ كوكب حريد معتزل (jamhara;sihah)
- **B005** sütün ya da yıllık yağışın azalması veya kesilmesi — dişi devenin sütünün azalması veya kesilmesi · yılın yağmurunun azalması · hayvan sütünün kesilmesi · sütü az dişi develer
  حاردت الناقة إذا قل لبنها (maqayis;jamhara;sihah;tahdhib)؛ المحاردة انقطاع اللبن (ayn)؛ حاردت السنة إذا قل مطرها (maqayis;sihah;mufradat)؛ منعت قطرها والناقة منعت درها (mufradat)
- **B006** yüksek adımlı yürüyüş, uzuv veya yük kaynaklı hareket kısıtlılığı ve düzensiz yol alış — bacaklarını olağandan yüksek kaldırarak yürüyen ya da bir ön bacak kirişi gevşek olan · zırhının ağırlığı yüzünden adımlarını rahat atamayan adam · yol alışın düzenli bölümlere ayrılmaması · hızlı bağırtlaklar; kısa bacaklı açıklaması yanlış sayılmıştır
  الأحرد إذا مشى رفع قوائمه (ayn;tahdhib)؛ حرد الرجل إذا ثقلت عليه درعه (ayn;tahdhib)؛ حرد البعير إذا استرخى عصب إحدى يديه (jamhara;sihah;tahdhib)؛ بعير أحرد في إحدى يديه حرد (mufradat)؛ حرد السير إذا لم يستو قطعه (ayn)
- **B007** eğrilik ve kemer biçiminde eğme; eğri ip ve kamış yapı adları — eğri olan şey · bir şeyi kemer biçiminde eğmek · örülünce kolları eğrilip düğümlenen ip · sırtı tümsek, kulübe biçimli ev · kamıştan yapılmış çevre örgüsü veya ağıl · başka bir dilden alınmış belirli bir kamış adı
  المحرد من كل شيء المعوج (maqayis;tahdhib;sihah)؛ تحريد الشيء تعويجه كهيئة الطاق (sihah)؛ حبل محرد وحبل فيه حرود (maqayis;sihah;tahdhib)؛ الحردية حياصة الحظيرة من قصب (ayn;tahdhib)؛ الحردية حظيرة من قصب (mufradat)؛ الحردي من القصب نبطي معرب (jamhara)
- **B008** bağırsaklar; tartışmalı olarak hörgüçten bir parça — devenin bağırsakları · bağırsaklar · hörgüçten bir parça; bu aktarım yanlış sayılarak bağırsak anlamı da verilmiştir · bağırsakları geniş adam
  الحرود مباعر الإبل واحدها حرد (maqayis;sihah;tahdhib)؛ الحرود الأمعاء (tahdhib)؛ الحرد قطعة من السنام (ayn;tahdhib)؛ رجل حردي واسع الأمعاء (tahdhib)

## ق د ر (root_001205): 68:25 قَٰدِرِينَ

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

## ر ء ي (root_000531): 68:26 رَأَوْهَا

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

## ECHO ر و ي (root_000615): for 68:26 رَأَوْهَا: withheld observed target; not identity

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

## ح ر م (root_000313): 68:27 مَحْرُومُونَ

- **B001** yapılması veya çiğnenmesi yasak olan şey — yasak olan, yapılmasına veya çiğnenmesine izin verilmeyen · yasak olan şey · bir şeyi yasak sayma veya yasaklama hükmü verme · yıkılmış yerleşimin geri dönmesi olanaksızdır; bazı yorumlarda geri dönmemesi kesin bir hükümdür
  الحرام ضد الحلال (maqayis;sihah); الحرمة ما لا يحل لك انتهاكه (ayn;tahdhib); الحرام الممنوع منه (mufradat); حرام على قرية أهلكناها وقرئت وحرم (maqayis;sihah;tahdhib;mufradat)
- **B002** henüz yumuşatılmamış veya ehlileştirilmemiş — henüz yumuşamamış veya esneklik kazanmamış kırbaç · tabaklaması tamamlanmamış deri · henüz alıştırılmamış ve ehlileştirilmemiş dişi deve
  سوط محرم إذا لم يلين بعد (maqayis); جلد محرم أي لم تتم دباغته وسوط محرم لم يلين بعد وناقة محرمة أي لم تتم رياضتها (sihah); ناقة محرمة الظهر إذا كانت صعبة لم ترض ولم تذلل وجلد محرم غير مدبوغ والقطيع المحرما (tahdhib); سوط محرم لم يدبغ جلده وقيل الذي لم يلين (mufradat)
- **B003** korunan yer ve ona bağlı kullanım çevresi — kutsal bölge ve dokunulmaz çevresi · iki kutsal şehir · kutsal bölge · kuyu, ev, ırmak veya ibadethaneye bağlı koruma ve kullanım çevresi · kutsal bölgeye veya oranın halkına mensup
  الحريم حريم البئر وهو ما حولها (maqayis); الحرمان مكة والمدينة (maqayis;sihah); الحرم حرم مكة وما أحاط بها (ayn;tahdhib); مكة حرم الله (sihah); الحرم سمي بذلك لتحريم الله تعالى فيه كثيرا (mufradat); حريم الدار وحريم النهر وحريم فناء المسجد (tahdhib)
- **B004** dinsel ziyaret ibadetinin kısıtlı durumuna girme — dinsel ziyaret ibadetine niyetle girip özel kısıtları üstlenme · dinsel ziyaret ibadetinin özel kısıtlı durumunda bulunan kişi
  أحرم الرجل بالحج لأنه يحرم عليه ما كان حلالا له (maqayis); أحرم الرجل فهو محرم وحرام وقوم حرم (ayn); الحرم بالضم الإحرام ورجل حرام أي محرم (sihah); أحرم الرجل إذا دخل في الإحرام بالإهلال (tahdhib); رجل حرام وحلال ومحل ومحرم (mufradat)
- **B005** savaşın yasak sayıldığı kutsal ay dönemi — savaşın yasak sayıldığı dört kutsal ay · yılın ilk ve savaşın yasak sayıldığı kutsal ayı · kutsal aya girdi
  أحرم الرجل دخل في الشهر الحرام (maqayis); الأشهر الحرم ذو القعدة وذو الحجة والمحرم ورجب (ayn;sihah;tahdhib); المحرم سمي به لأنهم لا يستحلون فيه القتال (ayn); أحرمت دخلت في الشهر الحرام (sihah); وكذلك الشهر الحرام (mufradat)
- **B006** çiğnenmemesi gereken saygınlık ve korunmuş hak — çiğnenmemesi gereken saygınlık, hak ve ilişki bağı · sözleşme veya güvenceyle zarar görmekten korunmuş kişi
  بين القوم حرمة ومحرمة حرام إضاعته وترك حفظه (maqayis); فلان له حرمة أي تحرم منا بصحبة وبحق (ayn); وقد تحرم بصحبته (sihah); الحرمة المهابة وللمسلم على المسلم حرمة ومهابة (tahdhib); محرم عنك يحرم أذاك عليه (tahdhib); أحرم إذا صار في حرمة من عهد أو ميثاق (tahdhib)
- **B007** kumarda yenip umduğu kazançtan yoksun bırakma — kumarda rakibini yenip beklediği kazancı almasını engelledi · onu kumarda yendim ve umduğu kazançtan yoksun bıraktım
  أحرمت الرجل قمرته كأنك حرمته ما طمع فيه منك (maqayis); حرم الرجل بالكسر يحرم حرما أي قمر وأحرمته أنا إذا قمرته (sihah); أحرمت الرجل إذا قمرته وحرم الرجل يحرم حرما إذا قمر (tahdhib)
- **B008** umulan yarardan yoksun bırakılma veya onu elde edememe — bağışı vermedi ve kişiyi ondan yoksun bıraktı · umulan herhangi bir iş veya yarardan elde edilemeyen şey · iyilikten yoksun kalan veya geçim imkânı genişletilmeyen kişi
  حرمت الرجل العطية حرمانا (maqayis); الحريمة اسم ما فات من كل هم مطموع فيه (maqayis); الحرمة أيضا الحرمان والحريمة ما فات من كل مطموع فيه (sihah); حرمت الرجل العطية أحرمه حرمانا وحريمة (tahdhib); المحروم الذي حرم الخير حرمانا (tahdhib); بل نحن محرومون أي ممنوعون من جهة الجد والسائل والمحروم أي الذي لم يوسع عليه الرزق (mufradat)
- **B009** geceleyin korkulup geçilmekten kaçınılan yol ve yerler — çekingen kişinin geceleyin korkup geçmekten kaçındığı yollar ve yerler
  محارم الليل مخاوفه التي يحرم على الجبان أن يسلكها (maqayis;sihah)
- **B010** kutsal alanda giyilmesi bırakılan ibadet giysisi — ibadetin özel durumundaki kişinin giysisi veya kutsal alanda çıkarılıp bırakılan giysi
  يسمى الثوب إذا حرم لبسه الحريم (maqayis); الحريم ثوب المحرم (sihah); تخلع ثيابها التي عليها إذا دخلوا الحرم ولم يلبسوها ما داموا في الحرم ومنه لقى بين أيدي الطائفين حريم (tahdhib); ثوب حرمي (tahdhib)
- **B011** korunan aile çevresi ve evlenilmesi yasak yakınlar — bir erkeğin kadınları, ailesi ve koruduğu hane halkı · yakın akrabalık nedeniyle evlenilmesi yasak kişiler
  حرم الرجل نساؤه وما يحمي والمحارم ما لا يحل استحلاله والمحرم ذو الرحم في القرابة (ayn); حرمة الرجل حرمه وأهله وهو ذو محرم منها إذا لم يحل له نكاحها (sihah); حرم الرجل نساؤه وما يحمي والمحرم ذات الرحم في القرابة التي لا يحل تزوجها (tahdhib)
- **B012** cinsel dürtünün yükselmesi ve dişinin erkeği istemesi — cinsel dürtünün yükselmesi · dişi hayvan çiftleşmek üzere erkeği istedi
  الحرمة بالكسر الغلمة واستحرمت الشاة وكل أنثى من ذوات الظلف إذا اشتهت الفحل (sihah); استحرمت الكلبة إذا اشتهت السفاد والاستحرام لكل ذات ظلف خاصة واستحرمت الماعزة إذا اشتهت الفحل (tahdhib); المحرمة والمحرمة والحرمة واستحرمت الماعز كناية عن إرادتها الفحل (mufradat)
- **B013** Tanrı adına bir işi yapmama yemini — Tanrı adına, bunu yapmayacağıma yemin ederim
  حرام الله لا أفعل كقولهم يمين الله لا أفعل (sihah); حرام الله لا أفعل ذاك ويمين الله لا أفعل ذاك ومعناهما واحد (tahdhib)

## و س ط (root_001646): 68:28 أَوْسَطُهُمْ

- **B001** adil ve seçkin orta olma — adil, seçkin ve aşırılıktan uzak ölçülü olma · en adil veya topluluğun en seçkinlerinden · topluluğunda soyu seçkin ve konumu yüksek kişi
  بناء صحيح يدل على العدل والنصف، وأعدل الشيء أوسطه (maqayis)؛ فلان وسيط الحسب في قومه (ayn)؛ الوسط من كل شيء أعدله، أمة وسطا أي عدلا (sihah)؛ وسطا عدلا، خيارا، أوسط قومه أي من خيارهم (tahdhib)؛ يستعمل استعمال القصد المصون عن الإفراط والتفريط، فيمدح به نحو السواء والعدل والنصفة (mufradat)
- **B002** uçlar veya parçalar arasındaki orta yer — iki uç veya parçalar arasındaki orta yer · kolyenin ortasındaki değerli taş · orta parmak · sıralamadaki yerine göre orta sayılan ibadet · iki kent arasındaki konumundan adını alan şehir
  النصف، ضربت وسط رأسه، وسط القوم (maqayis)؛ الوسط مخففا يكون موضعا للشيء، اسما لما بين طرفي كل شيء، واسطة القلادة جوهرة تكون في وسط الكرس المنظوم (ayn)؛ الأصبع الوسطى، واسطة القلادة، واسط بلد سمي بالقصر بين الكوفة والبصرة (sihah)؛ ما كان يبين جزء من جزء فهو وسط، وسط الدار، واسطة القلادة (tahdhib)؛ وسط الشيء ما له طرفان، الصلاة الوسطى بين الركعتين وبين الأربع أو بين صلاة الليل والنهار (mufradat)
- **B003** ortaya girme veya ortaya yerleştirme — topluluğun ortasına girip aralarında yer almak · bir şeyi ortaya yerleştirmek
  وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم (ayn)؛ وسطت القوم أسطهم وسطا وسطة أي توسطتهم، التوسيط أن تجعل الشيء في الوسط (sihah)؛ أوسطت القوم ووسطتهم وتوسطتهم بمعنى واحد إذا دخلت وسطهم (tahdhib)
- **B004** iyi ile kötü arasında orta nitelikte — iyi ile kötü arasında, kimi bağlamda iyinin altında
  شيء وسط أي بين الجيد والردئ (sihah)؛ يقال فيما له طرف محمود وطرف مذموم، ويكنى به عن الرذل، فلان وسط من الرجال تنبيها أنه قد خرج من حد الخير (mufradat)
- **B005** insanlar arasında aracılık etme [kalıp] — insanlar arasında aracılık etmek
  التوسط بين الناس، من الوساطة (sihah)
- **B006** ortasından kesip ikiye ayırma — bir şeyi ortasından kesip iki yarıya ayırmak
  التوسيط قطع الشيء نصفين (sihah)
- **B007** özel adlandırma kümesi — benzer küçük bir çadırdan daha büyük kıl çadırı · sütüyle kabı dolduran deve
  الوسوط بيت من بيوت الشعر أكبر من المظلة، ويقال الوسوط من النوق كالصفوف تملأ الإناء (maqayis)

## س ب ح (root_000666): 68:28 تُسَبِّحُونَ, 68:29 سُبْحَٰنَ

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

## ظ ل م (root_000967): 68:29 ظَٰلِمِينَ

- **B001** isik yoklugu ve karanlik benzetmesi — karanlik; isigin yoklugu · karanliklar; bilgisizlik, ortak kosma veya yoldan cikma icin benzetme · karanlik; gecenin baslangici · karanliga girmek veya bir yerin kararmasi · gecenin kararmasi · karanlik; karanlik gece · gormeyi ilk kapatan anda onunla karsilasmak · en yakin anda veya ilk gorus noktasinda onunla karsilasmak · takvim ayindaki belirli uc karanlik gece
  الظلمة والجمع ظلمات؛ الظلمة خلاف النور (maqayis;sihah)؛ الظلمة ذهاب النور والظلام اسم لذلك (tahdhib)؛ الظلمة عدم النور ويعبر بها عن الجهل والشرك والفسق (mufradat)
- **B002** haksiz yerinden etme ve siniri asma — bir seyi yerli yerine koymama; haksizlik ve siniri asma · birine haksizlik etmek veya onun sinirini asmak · kendine haksizlik etmek veya kendi payini eksiltmek · eksiltmek veya payini kismak · yoldan ya da dogru yonden sapmak · Tanri'ya ortak kosmayi en agir haksizlik sayan kullanim · haksiz davranan veya kisilere ait paylari engelleyen kisi · cok haksizlik eden kisi · bir toplulugun birbirine haksizlik etmesi · gercekten; ya da isin yerli yerinde olmamasi
  الأصل وضع الشيء في غير موضعه (maqayis;sihah;tahdhib)؛ الظلم مجاوزة الحق ويقال فيما يكثر وفيما يقل (mufradat)؛ ما نقصونا شيئا ولكن نقصوا أنفسهم (tahdhib)؛ إن الشرك لظلم عظيم (mufradat;tahdhib)
- **B003** haksizliga karsi yakinma ve geri istem — birini haksizlikla suclamak veya ona haksiz davrandigini bildirmek · haksizlikla alinan seyin geri istenen konusu · haksiz alinmis pay veya mal icin geri istem · haksizligi dile getirip duzeltilmesini istemek · haksizliga katlanmak ve bunu kabul etmek · gucunu asan istek yuklendiginde buna katlanmak
  الظلامة ما تطلبه من مظلمتك عند الظالم (maqayis)؛ الظلامة والظليمة والمظلمة ما تطلبه عند الظالم (sihah)؛ تظلم منه أي اشتكى ظلمه (sihah)؛ ظلمته تظليما إذا نبأته أنه ظالم (tahdhib)؛ ظلم فلان فاظلم معناه أنه احتمل الظلم (tahdhib)
- **B004** yersiz veya zamansiz somut islem — tulumdaki sutu olgunlasmadan icmek veya icirmek · olgunlasmadan icilen veya icirilen sut · onceden kazilmamis ya da kazi yeri olmayan topragin kazilmasi · cukurdan veya mezardan cikarilip geri konan toprak · hastalik yokken deveyi kesmek · vadi suyunun daha once ulasmadigi yere varmasi · havuzu uygun olmayan yerde yapmak · erkek esegin gebe disi esege ciftlesmek uzere yanasmasi
  ظلم وطبه إذا سقى منه قبل أن يروب (maqayis;sihah;tahdhib)؛ ظلمت السقاء وظلمت اللبن إذا شربته أو سقيته قبل إدراكه (tahdhib;mufradat)؛ الأرض المظلومة التي لم تحفر قط ثم حفرت (maqayis;sihah)؛ ظلمت الأرض حفرتها ولم تكن موضعا للحفر (mufradat)؛ ظلم الوادي إذا بلغ الماء منه موضعا لم يكن بلغه (sihah;tahdhib)؛ ظلمت البعير إذا نحرته من غير داء (sihah)؛ ظلم الحمار الأتان إذا كامها وقد حملت (tahdhib)
- **B005** dislerde su gibi parilti — dislerin su gibi parlakligi · agzin ince su gibi parildamasi
  الظلم ماء الأسنان وبريقها (sihah)؛ الظلم الماء الذي يجري على الأسنان من اللون لا من الريق (tahdhib)؛ أظلم الثغر إذا تلألأ عليه كالماء الرقيق (tahdhib)؛ الظلم ماء الأسنان (mufradat)
- **B006** erkek devekusu — erkek devekusu
  الظليم الذكر من النعام (sihah)؛ الظليم الذكر من النعام وجمعه الظلمان (tahdhib)؛ الظليم ذكر النعام (mufradat)
- **B007** siniri asan uzun surgunlu bitki — sinirini asan uzun surgunleri olan bitki · o uzun surgunlu bitkinin adi
  ومن غريب الشجر الظلم واحدها ظلمة وهو الظلام والظلام والظالم؛ هو شجر له عساليج طوال وتنبسط حتى تجوز حد أصل شجرها
- **B008** paydan alikoyma — kisileri kendilerine ait paylardan alikoyanlar · seni bundan ne alikoydu
  الظلمة المانعون أهل الحقوق حقوقهم؛ ما ظلمك عن كذا أي ما منعك

## ق ب ل (root_001198): 68:30 فَأَقْبَلَ

- **B001** karşı karşıya olma ve ön yön — ön taraf, karşıya dönük yön · ön taraftaki cinsel bölge · yüz yüze, göz göre göre yapmak · karşısında, tam karşı hizada · dağın karşıdan görünen yamacı veya yükseltisi · yönelecek bir yönü yok; işin yolunu bulamıyor
  مواجهة الشيء للشيء (maqayis)؛ القبل خلاف الدبر (ayn;tahdhib)؛ قبل ضد الدبر (jamhara)؛ المقابلة المواجهة (sihah)؛ الإقبال التوجه نحو القبل (mufradat)
- **B002** önce olma ve sırada yaklaşma — önce; zaman, yer veya sırada önde · gelecek veya yaklaşan yıl, gece ve benzeri dönem · bundan sonraki zamanda · gençliğinin başında, yaşlılık izi belirmemiş
  قبل الذي هو خلاف بعد (maqayis)؛ من قبل ومن بعد غايتان (ayn;tahdhib)؛ قبل ضد بعد (jamhara)؛ القابلة الليلة المقبلة والعام القابل المقبل (sihah;tahdhib)؛ قبل يستعمل في التقدم المتصل والمنفصل (mufradat)
- **B003** birinin tarafından veya nezdinde [kalıp] — o kişiden, onun tarafından veya yanından · o kişide hakkım var; ondan alacağım var
  هذا من قبل فلان أي من عنده (maqayis)؛ أصيب هذا من قبله أي من تلقائه ومن لدنه (ayn;tahdhib)؛ لي قبل فلان حق أي عنده (sihah;mufradat)
- **B004** uygun bulup benimseme — bir şeyi uygun bulup benimsemek · olumlu karşılayıp benimsemek ve karşılığını vermek · göze ve gönle hoş gelmek
  قبلت الشيء قبولا (maqayis)؛ التقبل القبول (ayn)؛ تقبلت الشيء وقبلته قبولا (sihah)؛ قبلت الشيء قبولا إذا رضيته (tahdhib)؛ قبلت عذره وتوبته وغيره وتقبلته (mufradat)
- **B005** namazda yönelinen yön — namazda yönelinen yön veya yer
  القبلة سميت قبلة لإقبال الناس عليها في صلاتهم (maqayis)؛ القبلة قبلة الصلاة (jamhara)؛ القبلة التي يصلى نحوها (sihah)؛ صار اسما للمكان المقابل المتوجه إليه للصلاة (mufradat)
- **B006** öpücük ve öpme — öpücük; dudakla öpmek
  الفعل من القبلة التقبيل (ayn)؛ القبلة من التقبيل معروفة (sihah)؛ القبلة معروفة وجمعها القبل وفعلها التقبيل (tahdhib)؛ ومنه القبلة وجمعها قبل وقبلته تقبيلا (mufradat)
- **B007** çıkanı karşılayıp teslim alma — doğumda bebeği karşılayıp alan kadın · kuyudan çıkan kovayı teslim alan kişi
  القابلة التي تقبل الولد عند الولاد (maqayis)؛ القابلة التي تقبل الولد عند الولاد (ayn)؛ القابلة التي تقبل الصبي (jamhara)؛ القابلة من النساء معروفة (sihah)؛ القابل الذي يستقبل الدلو من البئر (mufradat)
- **B008** güvence ve sorumluluk üstlenme — başkası için güvence veren kişi · güvence üstlenme veya yazılı yüklenim
  القبيل الكفيل يقال قبل به قبالة (maqayis)؛ القبيل الكفيل (jamhara)؛ القبيل الكفيل والعريف (sihah)؛ قبل به يقبل به قبالة إذا كفل به (tahdhib)؛ قيل للكفالة قبالة (mufradat)
- **B009** soy veya kuşak topluluğu — insan topluluğu veya kuşak · aynı atadan gelen soy topluluğu · topluluğun işlerini gözeten temsilci
  قبائل العرب (maqayis)؛ كل جيل من الجن والإنس قبل (ayn)؛ القبيل جيل من الناس (jamhara)؛ القبيل الجماعة تكون من الثلاثة فصاعدا (sihah)؛ القبيلة بنو أب واحد (tahdhib)؛ القبيل جمع قبيلة وهي الجماعة المجتمعة (mufradat)
- **B010** karşılıklı birleşen ve bağlayan parçalar — kafatası bölümleri ve birleşme çizgileri · ayakkabının parmaklar arasındaki bağı · iplik veya ipin ileri ve geri büküm yönleri · gem, giysi ve eyerin bağlı kayış, yama ve kemerleri
  القبال زمام البعير والنعل (maqayis)؛ قبيلة الرأس كل فلقة قوبلت بالأخرى (ayn)؛ قبال النعل معروف (jamhara)؛ قبال النعل الزمام (sihah)؛ قبائلا اللجام سيوره (tahdhib)؛ قبال النعل زمامها (mufradat)
- **B011** beden bölümünün belirli yöne dönüklüğü — göz bebeğinin buruna veya iç yana yönelmesi · bacakların veya ayakların ayrık duruşu · kulağı ön yandan kesik veya boynuzları öne dönük koyun
  القبل في العين إقبال السواد على المحجر (maqayis)؛ القبال شبه فحج (ayn)؛ رجل أقبل والأنثى قبلاء (jamhara)؛ شاة قبلاء بينة القبل (sihah)؛ الأقبل الذي أقبلت حدقتاه على أنفه (tahdhib)؛ وشاة مقابلة قطع من قبل أذنها (mufradat)
- **B012** batı rüzgarının karşıtı olan rüzgar — batı rüzgarının karşıtı olan rüzgar
  القبول من الرياح الصبا لأنها تقابل الدبور (maqayis)؛ القبول الصبا (ayn)؛ الريح القبول الصبا (jamhara)؛ القبول أيضا الصبا (sihah)؛ القبول من الرياح الصبا (tahdhib)؛ القبول ريح الصبا (mufradat)
- **B013** onunla başa çıkacak gücü olmama [kalıp] — onunla başa çıkacak veya ona karşı koyacak gücüm yok
  لا قبل لي به أي لا طاقة (maqayis)؛ القبل الطاقة (ayn)؛ ما لي به قبل أي طاقة (sihah)؛ لا قبل معناه لا طاقة لهم بها (tahdhib)؛ لا قبل لي بكذا أي لا يمكنني أن أقابله (mufradat)
- **B014** develer içerken önlerine su çekip dökme — develer içerken başları veya ağızları üzerinde su çekip dökme
  أقبلنا على الإبل إذا استقينا على رءوسها وهي تشرب (maqayis)؛ القبل أن يورد الرجل إبله ثم يستقي لها (jamhara)؛ القبل أن تشرب الإبل الماء وهو يصب على رؤوسها (sihah)؛ القبل أن يورد الرجل إبله فيستقي على أفواهها (tahdhib)
- **B015** ilk elden veya yeniden başlama — ayı daha önce görülmemişken ilk kez ince haliyle görmek · önceden hazırlamadan konuşmak veya söylemek · işi yeniden ele alıp başlamak
  القبل استئناف الشيء (ayn)؛ رأيت هلال كذا قبلا فكان صغيرا (jamhara)؛ تكلم فلان قبلا فأجاد (sihah)؛ اقتبل أمره إذا استأنفه (tahdhib)
- **B016** asılan boncuk veya makara biçimli takı — asılan boncuk veya makara biçimli takı; yüzü birine çevirdiğine inanılan türü
  القبلة خرزة شبيهة بالفلكة (maqayis)؛ القبلة خرزة من خرز نساء الأعراب (jamhara)؛ القبل جمع قبلة وهي الفلكة (sihah)؛ القبلة حجر أبيض عظيم تجعل في عنق الفرس (tahdhib)؛ القبلة خرزة يزعم الساحر أنه يقبل بالإنسان (mufradat)

## ب ع ض (root_000133): 68:30 بَعْضُهُمْ, 68:30 بَعْضٍ

- **B001** parça ve parçalara ayırma — bir şeyin parçası, bölümü veya ondan bir kesim · parçalar, bölümler · bir şeyi parçalara ayırmak · parçalara ayrılmak
  بعض كل شيء طائفة منه (maqayis;ayn;tahdhib)؛ بعض الشيء جزء منه (mufradat)؛ بعض الشيء واحد أبعاضه (sihah)؛ بعض الشيء معروف (jamhara)؛ بعضت الشيء تبعيضا إذا فرقته أجزاء (maqayis;ayn;tahdhib)؛ تبعض الشيء وبعضته أي فرقته (jamhara)؛ بعضته تبعيضا أي جزأته فتبعض (sihah)؛ بعضت كذا جعلته أبعاضا نحو جزأته (mufradat)
- **B002** sivrisinek ve ona bağlı zarar veya bulunma kullanımları — sivrisinek · sivrisinekler, sivrisinek topluluğu veya tahtakurusu · sivrisineğin çok olduğu gece · topluluğa sivrisineklerin zarar vermesi · sivrisineklerden zarar görmüş topluluk · bulundukları yerde sivrisinek olması · sivrisinek bulunan arazi · aşırı küçüklüğü veya olanaksızlığı yüzünden elde edilemeyen şey
  البعوضة وهي معروفة والجمع بعوض (maqayis)؛ البعوض جمع البعوضة وهي المؤذية العاضة في الصيف (ayn)؛ البعوض البق الواحدة بعوضة (sihah)؛ قوم مبعوضون وقد بعض القوم إذا آذاهم البعوض وأبعضوا إذا كان في أرضهم بعوض (tahdhib)؛ البعوض بني لفظه من بعض وذلك لصغر جسمها (mufradat)

## ل و م (root_001386): 68:30 يَتَلَٰوَمُونَ

- **B001** ayıplanacak bir şeyi birine yükleyerek kınama — kınama; ayıplama · kınamak; ayıplamak · çokça ve ağır biçimde kınamak · kınanan veya kınanmayı hak eden · kınanmayı hak eden · kınanacak bir davranışta bulunmak ve kınanmayı hak etmek · kınama veya kişinin kınandığı davranış · kişinin kınandığı davranış · bir kez kınama; kınama · kınama · kınayan kimse · kınayanlar · iki kişinin birbirini kınaması · birbirini kınama · yanlış yaptığında sahibini kınayan ya da başkasını düzeltmek için kınayan benlik · söylenişine göre insanları kınayan veya insanlarca kınanan adam
  اللوم وهو العذل؛ لمته لوما والرجل ملوم؛ المليم الذي يستحق اللوم؛ اللامة الأمر يلام عليه الإنسان (maqayis)؛ اللوم الملامة والفعل لام يلوم؛ رجل ملوم ومليم قد استحق اللوم؛ اللوماء الملامة (ayn)؛ اللوم: العذل؛ اللائمة: الملامة؛ ألام الرجل إذا أتى بما يلام عليه؛ الملاومة أن تلوم رجلا ويلومك؛ تلاوموا لام بعضهم بعضا (sihah)؛ اللوم: عذل الإنسان بنسبته إلى ما فيه لوم؛ وألام: استحق اللوم؛ والتلاوم: أن يلوم بعضهم بعضا؛ النفس اللوامة (mufradat)
- **B002** bekleyip ağır davranma — bekleme, bir süre durup kalma ve ağır davranma
  الكلمة الأخرى التلوم وهو التمكث؛ الأخرى على الإبطاء (maqayis)؛ التلوم: الانتظار والتمكث (sihah)

## ECHO ل م م (root_001378): for 68:30 يَتَلَٰوَمُونَ: withheld observed target; not identity

- **B001** dağınık olanı bütünüyle bir araya getirip düzenleme [kalıp] — dağınıklığını giderip toparladı · insanları bir araya toplayan ev · bölükleri birleşmiş kalabalık birlik · hepsini sonuna kadar aldı · kendi payıyla arkadaşının payını birlikte yiyiş
  لممت شعثه إذا ضممت ما كان متشعثا منتشرا (maqayis)؛ لم الله شعثه أي أصلح وجمع ما تفرق من أموره (sihah)؛ داركم لمومة أي تلم الناس وتربهم وتجمعهم (sihah)؛ كتيبة ملمومة كثر عددها واجتمع المقنب فيها إلى المقنب (maqayis)؛ كتيبة ململمة وملمومة أي مجتمعة مضموم بعضها إلى بعض (sihah)؛ لممته أجمع حتى أتيت على آخره (sihah)
- **B002** yanına gelip yakınında bulunma veya bir sınıra yaklaşma — yanına gelip yakınında bulundu · ergenliğe yaklaşmış oğlan · o sonuca ulaşmadan yaklaşır · bizi ara sıra ziyaret eder
  ألممت بالرجل إلماما إذا نزلت به وضاممته (maqayis)؛ الإلمام النزول وقد ألم به أي نزل به (sihah)؛ غلام ملم أي قارب البلوغ (sihah)؛ ما يقتل حبطا أو يلم أي يقرب من ذلك (sihah)؛ فلان يزورنا لماما أي في الأحايين (sihah)
- **B003** küçük yanlış veya yanlışı işlemeden ona yaklaşma — küçük yanlışlar veya yanlışı işlemeden ona yaklaşma · küçük yanlışlara bulaştı veya yanlışa yaklaştı
  اللمم ليس بمواقعة الذنب وإنما هو مقاربته ثم ينحجز عنه (maqayis)؛ اللمم وهو صغار الذنوب (sihah)؛ مقاربة المعصية من غير مواقعة (sihah)
- **B004** görünmeyen bir varlığın dokunmasına bağlanan zihinsel etkilenme — görünmeyen bir varlığın dokunması sayılan etki · hafif akıl bozukluğu · böyle bir etkilenmesi bulunan adam
  أصابت فلانا من الجن لمة وذلك كالمس (maqayis)؛ اللمم أيضا طرف من الجنون (sihah)؛ رجل ملموم أي به لمم (sihah)؛ أصابت فلانا من الجن لمة وهو المس (sihah)
- **B005** kulak memesini geçip omuzlara yaklaşan saç — kulak memesini geçip omuzlara yaklaşan saç · bu uzunluktaki saçlar
  اللمة بكسر اللام الشعر إذا جاوز شحمة الأذنين (maqayis)؛ لأنه شام المنكبين وقاربهما (maqayis)؛ اللمة بالكسر الشعر يجاوز شحمة الأذن فإذا بلغت المنكبين فهي جمة (sihah)
- **B006** başa gelen ağır olay ve zamanın sertliği — dünyada başa gelen ağır olay · zamanın ağır olayları ve sertliği
  الملمة النازلة من نوازل الدنيا (maqayis)؛ الملمة النازلة من نوازل الدنيا (sihah)؛ حادثات اللمة فهو الدهر ويقال الشدة (sihah)؛ صروف الدهر أو دولاتها اللمة من لماتها (sihah)
- **B007** kötülük verdiğine inanılan bakış [kalıp] — kötülük verdiğine inanılan göz
  العين اللامة الأصل ملمة لما قرنت بالسامة قيل لامة وهي التي تصيب بالسوء (maqayis)؛ العين اللامة التى تصيب بسوء (sihah)؛ أعيذه من كل هامة ولامة (sihah)
- **B008** sert ve yuvarlak kaya [kalıp] — sert, yuvarlak kaya · yuvarlak, sert kaya
  صخرة ململمة أي صلبة مستديرة وملمومة أيضا (maqayis)؛ صخرة ملمومة وململمة أي مستديرة صلبة (sihah)
- **B009** filin uzun burnu [kalıp] — filin uzun burnu
  ململمة الفيل خرطومه (sihah)
- **B010** Yemen halkı için belirlenmiş durak yeri — Yemen halkı için belirlenmiş durak olan yer · Yemen halkı için belirlenmiş durak olan yer
  يلملم وألملم موضع وهو ميقات أهل اليمن (sihah)

## ط غ ي (root_000937): 68:31 طَٰغِينَ

- **B001** itaatsizlikte veya ölçüde sınırı aşma — sınırı veya ölçüyü aşmak, azmak · itaatsizlikte sınırı aşan, azgın · itaatsizlikte sınır tanımazlık ve azgınlık · sınırı aşma ve azgınlık · sınırı aşma durumu, azgınlık · onu azdırdı veya sınır aşmaya sürükledi · inatçı, kibirli ve sınır tanımaz zorba · Roma hükümdarına verilen unvan
  مجاوزة الحد في العصيان (maqayis;mufradat); جاوز الحد وكل مجاوز حده في العصيان (sihah); كل شيء جاوز القدر فقد طغا (tahdhib); أطغاه المال أي جعله طاغيا (sihah); الطاغية الجبار العنيد (tahdhib)
- **B002** ölçüyü aşarak kabarıp bastırma [kalıp] — sel bol suyla geldi ve kabardı · su olağan düzeyi aşıp yükseldi · denizin dalgaları kabarıp yükseldi · kan kabarıp coştu · çığlık ya da rüzgar ölçüyü aşan güçle baskın geldi
  طغى السيل إذا جاء بماء كثير (maqayis;sihah); طغى الماء خروجه عن المقدار (maqayis); طغى البحر هاجت أمواجه (maqayis;sihah); طغى الدم تبيغ (maqayis;sihah); طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib); استعير الطغيان فيه لتجاوز الماء الحد (mufradat)
- **B003** yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç — yanlış yolun önderi, Tanrı dışında tapınılan varlık veya iyilikten saptıran zorba güç
  الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah); كل معبود من دون الله جبت وطاغوت (tahdhib); الطاغوت الشيطان (tahdhib); الطاغوت عبارة عن كل متعد وكل معبود من دون الله (mufradat); الساحر والكاهن والمارد من الجن والصارف عن طريق الخير طاغوتا (mufradat)
- **B004** yıkıma götüren ezici olay veya sınır aşımı — yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ya da yıkıma yol açan sınır aşımı
  الطاغية الصاعقة ويعني صيحة العذاب (sihah); أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib); فأهلكوا بالطاغية فإشارة إلى الطوفان (mufradat)
- **B005** pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer — pürüzsüz ve kaygan kaya yüzeyi · dağın doruğu · yüksek yer
  الطغية الصفاة الملساء (maqayis;tahdhib); الطغية أعلى الجبل (sihah); كل مكان مرتفع طغوة (sihah); تنبي العقاب لملاستها (sihah)

## ECHO ط غ و (root_000936): for 68:31 طَٰغِينَ: withheld observed target; not identity

- **B001** başkaldırıda sınırı aşma ve buna sürükleme — başkaldırıda sınırı aşmak · başkaldırıda sınırı aşan · başkaldırıda sınırı aşma · azdırmak; sınırı aşmaya sürüklemek
  مجاوزة الحد في العصيان (maqayis;sihah;mufradat)؛ كل شيء جاوز القدر فقد طغا (tahdhib)؛ أطغاه المال أي جعله طاغيا وأطغاه كذا حمله على الطغيان (sihah;mufradat)
- **B002** su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması [kalıp] — sel bol suyla taşmak · deniz kabarıp sürükleyici olmak · su olağan düzeyini aşmak · kan coşmak · ses ya da rüzgar baskın gelmek
  طغى السيل إذا جاء بماء كثير (maqayis;sihah)؛ طغى البحر هاجت أمواجه (maqayis;sihah)؛ طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib)؛ استعير الطغيان فيه لتجاوز الماء الحد (mufradat)
- **B003** hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık — hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık
  الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah)؛ كل معبود من دون الله جبت وطاغوت (tahdhib)؛ عبارة عن كل متعد وكل معبود من دون الله والساحر والكاهن والمارد من الجن (mufradat)
- **B004** pervasız ve ezici zorba — pervasız, kendini büyük gören ve insanları ezen zorba
  الطاغية ملك الروم (sihah)؛ الطاغية الجبار العنيد (tahdhib)؛ الذي لا يبالي ما أتى يأكل الناس ويقهرهم (tahdhib)؛ الأحمق المستكبر الظالم (tahdhib)
- **B005** yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel — yıkıcı yıldırım ya da çığlık; sınır aşımı veya büyük sel
  الطاغية الصاعقة ويعني صيحة العذاب (sihah)؛ طغت الصيحة على ثمود (tahdhib)؛ أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib)؛ إشارة إلى الطوفان المعبر عنه بإنا لما طغى الماء (mufradat)
- **B006** düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer — düz ve pürüzsüz kaya ya da dağ doruğu · yüksek yer
  الطغية الصفاة الملساء (maqayis;tahdhib)؛ الطغية أعلى الجبل وكل مكان مرتفع طغوة (sihah)
- **B007** bir şeyden küçük parça — herhangi bir şeyden küçük parça
  الطغية من كل شيء نبذة منه (sihah)
- **B008** bir kimsenin ya da topluluğun sesi [kalıp] — bir kimsenin ya da topluluğun sesi
  سمعت طغي فلان أي صوته هذلية؛ سمعت طغي القوم وطهيهم ووغيهم أي صوتهم (tahdhib)
- **B009** yabani sığır yavrusu; bir aktarımda böğüren inek — yabani sığır yavrusu; bir aktarımda böğüren inek
  طغيا وهو الصغير من بقر الوحش (sihah)؛ يقال للبقرة الخائرة والطغيا (tahdhib)

## ع س ي (root_001015): 68:32 عَسَىٰ

- **B001** yaklaşma, umut ve kaygılı beklenti bildiren; Tanrı bildirince özel kesinlik taşıyabilen görev sözü — yaklaşma, umut ve kimi bağlamlarda kaygılı beklenti bildiren görev sözü · Tanrı'nın bildiriminde sonucu kesin sayılan veya insanda umut uyandıran kullanım
  عسى من أفعال المقاربة وفيه طمع وإشفاق (sihah)؛ عسى حرف من حروف المقاربة وفيه ترج وطمع (tahdhib)؛ عسى طمع وترجى (mufradat)؛ عسى من الله واجبة (sihah;tahdhib)
- **B002** kuruyup sertleşme; elin işten, bitkinin gelişirken kalınlaşması — kuruyup sertleşmek · sertleşme veya kalınlaşma · bir şeyin, özellikle dalın sertleşmesi · eli çalışmaktan kalınlaşmak · bitki kalınlaşıp kabalaşmak
  عسا الشيء يعسو عسوا وعساء أي يبس واشتد وصلب (sihah)؛ عست يده تعسو عسوا إذا غلظت من العمل (sihah;tahdhib)؛ عسا النبات إذا غلظ (sihah;tahdhib)؛ عسي الشيء يعسو إذا صلب (mufradat)؛ العساء مصدر عسا العود يعسو (tahdhib)
- **B003** yaşlı erkeğin iyice yaşlanması — yaşlı erkek daha da yaşlanıp ömrünün ileri dönemine varmak · yaşlı erkeğin ileri yaşa varması · yaşlı erkek iyice yaşlanmak
  عسا الشيخ يعسو عسوة وعسي يعسى عسى إذا كبر (ayn)؛ عسا الشيخ يعسو عسيا ولى وكبر (sihah)؛ يقال للشيخ إذا ولى وكبر عسا يعسو (tahdhib)؛ عسا الشيخ يعسو عسوة وعساء إذا كبر (tahdhib)
- **B004** gecenin iyice kararması [kalıp] — gecenin karanlığı şiddetlenmek · gece kararmak
  عسا الليل اشتدت ظلمته (ayn)؛ عسي الليل يعسى أي أظلم (mufradat)
- **B005** hurma salkımının dalı ve ham hurma adları — hurma salkımının dalı · ham hurma
  العاسِي شمراخ النخل (sihah)؛ العَساء مقصور البلح (sihah)
- **B006** sütü kesilmiş ya da sütü olup olmadığı belirsiz deve; kesilmede geri dönüş umulur — sütü olup olmadığı belirsiz dişi deve · sütü kesilmiş, sütünün geri gelmesi beklenen develer
  المعسية الناقة التي يشك فيها أبها لبن أم لا (tahdhib)؛ المعسيات من الإبل ما انقطع لبنه فيرجى أن يعود لبنها (mufradat)

## ب د ل (root_000095): 68:32 يُبْدِلَنَا

- **B001** yerine gecme ve yerine koyma — bir seyin yerini tutan karsilik · karsilik, bedel anlami veren diger soyleyis · baskasinin yerine gecen sey veya kisi · bir seyi kaldirip yerine baskasini koymak · bir seyi giderip yerine baskasini getirmek · bir seyi baska bir seyin yerine almak · karsilikli olarak degis tokus etmek · biri gidince yerine ayni nitelikte baskasi gelen secilmis kisiler
  قيام الشيء مقام الشيء الذاهب (maqayis)؛ البديل البدل (sihah)؛ استبدل الشيء بغيره وتبدله به إذا أخذه مكانه (sihah)؛ أبدلت الخاتم بالحلقة إذا نحيت هذا وجعلت هذا مكانه (tahdhib)؛ الأبدال خيار بدل من خيار (tahdhib)
- **B002** bicimini veya halini degistirme — yerine karsilik getirmeden bir seyi degistirmek · cevheri ayni kalirken bicimi veya hali degistirme · yuzugu eritip ayni maddeden halka bicimine sokmak
  بدلت الشيء إذا غيرته وإن لم تأت له ببدل (maqayis)؛ تبديل الشيء أيضا تغييره وإن لم يأت ببدل (sihah)؛ التبديل تغيير الصورة إلى صورة أخرى والجوهرة بعينها (tahdhib)
- **B003** gogus eti — gogus eti; boyun ile kopru kemigi arasindaki kisim
  البآدل لحم الصدر واحدتها بأدلة (jamhara)؛ البآدل واحدتها بأدلة وهي ما بين العنق إلى الترقوة (tahdhib)؛ البأدلة لحم الصدر (tahdhib)
- **B004** el ve ayak agrisi — ellerde ve ayaklarda agri · ellerinde ve ayaklarinda bu agriya tutulmak
  البَدَل وجع في اليدين والرجلين
- **B005** yiyecek saticisi — her tur yiyecek maddesini satan kisi
  العرب تقول للذي يبيع كل شيء من المأكولات بَدّال

## ر غ ب (root_000575): 68:32 رَٰغِبُونَ

- **B001** isteyerek yönelmek veya istemeyip yüz çevirmek — istek, yöneliş ve isteme · bir şeyi istemek ve ona yönelmek · bir şeye istekle yönelmek · bir şeyi istememek ve ondan yüz çevirmek · istenen ve aranan şey · istenmeyen ve kaçınılan şey · onu bilerek terk eden · ondan uzaklaşma yolu veya imkanı · ona istek duymak · birini bir şeyi istemeye özendirmek · isteğim ve dileğim sanadır
  الرغبة في الشيء الإرادة له؛ رغبت عنه إذا لم ترده (maqayis)؛ إليك الرغباء ومنك النعماء وأنا رغيب عنه إذا تركته عمدا (ayn)؛ رغبت في الشيء إذا ملت إليه ورغبت عنه إذا صددت عنه (jamhara)؛ رغبت في الشئ إذا أردته ورغبت عن الشئ إذا لم ترده وزهدت فيه (sihah)؛ رغب فيه وإليه يقتضي الحرص عليه ورغب عنه اقتضى صرف الرغبة عنه والزهد فيه (mufradat)
- **B002** iç hacim, alan veya hareket açıklığı bakımından genişlik — içi geniş veya geniş hacimli · geniş havuz · içi geniş su tulumu · geniş adımlı veya geniş koşulu at · geniş arazi veya ancak bol yağmurda su akıtan yumuşak toprak · genişlemek veya arazinin geniş ve yumuşak hale gelmesi · bir yerin veya nehrin adı · bu genişlik anlamından türemiş bir yer adı
  الشيء الرغيب الواسع الجوف وحوض رغيب وسقاء رغيب وفرس رغيب الشحوة والرغاب الأرض الواسعة (maqayis)؛ رجل رغيب واسع الجوف أكول وحوض رغيب أي واسع (ayn)؛ فرس رغيب الشحوة كثير الأخذ بقوائمه من الأرض وموضع رغيب واسع ومواضع رغاب (jamhara)؛ حوض رغيب وسقاء رغيب وفرس رغيب الشحوة والرغاب الأرض اللينة التي لا تسيل إلا من مطر كثير (sihah)؛ أصل الرغبة السعة في الشيء وحوض رغيب وفلان رغيب الجوف وفرس رغيب العدو (mufradat)
- **B003** yemede aşırı istek ve oburluk — obur ve çok yiyen adam · oburluk ve yeme düşkünlüğü
  رجل رغيب واسع الجوف أكول وفي الحديث الرغب شؤم (ayn)؛ رجل رغيب نهم شديد الأكل (jamhara)؛ الرغب بالضم الشره وقد رغب بالضم رغبا فهو رغيب (sihah)
- **B004** bol ve istenen bağış — çok ve istenen bağış; çoğulda bol bağışlar
  الرغيبة العطاء الكثير والجمع رغائب (maqayis)؛ رغيبة أي مرغوب فيها وجمعها رغائب (ayn)؛ الرغيبة العطاء الكثير الذي يرغب في مثله والجمع رغائب (jamhara)؛ الرغيبة العطاء الكثير والجمع الرغائب (sihah)؛ الرغيبة العطاء الكثير إما لكونه مرغوبا فيه وإما لسعته (mufradat)

## ع ذ ب (root_000994): 68:33 ٱلْعَذَابُ, 68:33 وَلَعَذَابُ

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

## ء خ ر (root_000019): 68:33 ٱلْءَاخِرَةِ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ك ب ر (root_001281): 68:33 أَكْبَرُ

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

## و ق ي (root_001677): 68:34 لِلْمُتَّقِينَ

- **B001** araya engel koyarak zarardan koruma — bir şeyi koruyucu bir engelle zarardan saklamak · koruma; zararı önleyen araç veya engel · bir şeyi korumaya yarayan araç ya da engel · zarardan koruyan şey · zararı savan koruyucu · kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez · koruyucu şeyler
  دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)
- **B002** korkulan şeyden ya da yanlış davranıştan kendini koruma — kendini korkulan ya da zarar verecek şeyden korumak · bir şeyi kendine koruyucu yapmak · Tanrı'ya karşı gelmekten sakınmak · kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması · sakınma ve kendini koruma · sakınan ve kendini yanlış davranıştan koruyan kimse · sakınma; kendini kötülükten koruma · sakınıp kendini koruma · kendini yanlış davranışlardan koruyan kimse · sakınan ve kendini yanlış davranıştan koruyan kimse
  اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)
- **B003** hafif topallama ve toynak ağrısıyla yürümekten çekinme — hafif topallama · topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at · hayvanın sırtında yara açmayan eyer · aksayışını gözet ve ağırdan al
  الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)
- **B004** kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü — kırk gümüş para ağırlığına eşit bilinen ölçü · yağ için yedi temel ağırlık birimine eşit ölçü · bu ağırlık ölçüsü adının çoğul biçimleri
  الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)
- **B005** örümcek kuşu — örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri
  الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)

## ع ن د (root_001052): 68:34 عِندَ, 68:47 عِندَهُمُ

- **B001** doğruyu bile bile geri çevirerek karşı koyma ve sınırı aşma — azıp sınırı aşmak ve doğruyu bile bile geri çevirmek · bildiği şeyi kabul etmeyi bile bile reddetme · birine karşı durup onunla boy ölçüşmek; kimi zaman onun yaptığının benzerini yapmak · zorbalık eden ve doğruya uymaktan yüz çeviren kimse · doğruyu kabul etmeyip karşı çıkan kimse · devenin yulara yüklenip onu yöneten kişiyi çekmesi
  أصل صحيح واحد يدل على مجاوزة وترك طريق الاستقامة (maqayis)؛ عند الرجل إذا طغى وعتا وجاوز قدره (maqayis;ayn)؛ المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله (maqayis;ayn;tahdhib)؛ خالف ورد الحق وهو يعرفه (sihah)؛ العنيد المعرض عن طاعة الله تعالى (tahdhib)؛ استعند البعير إذا غلب قائده على الزمام (maqayis)؛ عاند البعير خطامه أي عارضه (tahdhib)
- **B002** ortak doğrultudan yana sapıp ayrı durma — yoldan ya da amaçlanan yönden sapıp uzaklaşmak · bir yana çekilip topluluğa karışmayan · tek başına yaşayıp insanlara karışmayan adam · sürünün bir yanında durup öteki develere karışmayan deve · canlılığı ve gücü yüzünden yoldan yana sapan dişi deve · düz doğrultudan yana sapmış yol · yan, taraf · sağa sola yönelen saplama vuruşu · öteki kura oklarından başka bir yönde çıkarak kazanan ok · dirseği göğüsten uzakta duran
  العنود من الإبل الذي لا يخالط الإبل إنما هو في ناحية (maqayis;ayn;tahdhib)؛ رجل عنود لا يخالط الناس (maqayis;ayn)؛ طريق عاند أي مائل (maqayis)؛ العند بالتحريك الجانب (sihah)؛ العاند البعير الذي يجور عن الطريق ويعدل عن القصد (sihah)؛ قدح عنود وهو الذي يخرج فائزا على غير وجهة سائر القداح (tahdhib)
- **B003** sıvının yana yönelerek veya kesilmeden akması [kalıp] — kanı fışkırıp bir türlü dinmeyen damar · kanın yana doğru akması · kanı yaralıdan uzağa doğru akan yara · kusmanın art arda sürüp kesilmemesi · bol yağmur taşıyan bulut
  العرق العاند الذي يتفجر منه الدم فلا يكاد يرقأ (maqayis)؛ عند العرق سال ولم يرقأ وهو عرق عاند (sihah)؛ أعند في قيئه إذا لم ينقطع (maqayis)؛ أعند الرجل في قيئه إذا أتبع بعضه بعضا (sihah;tahdhib)؛ عند الدم إذا سال في جانب (tahdhib)؛ سحابة عنود كثيرة المطر (tahdhib)
- **B004** yakınında veya birinin değerlendirmesinde bulunma — bir şeyin yer veya zaman bakımından yakınında · birinin görüşünde, değerlendirmesinde, gözünde veya katında
  عند فحضور الشيء ودنوه (sihah)؛ عند لفظ موضوع للقرب (mufradat)؛ يستعمل في المكان وفي الاعتقاد وفي الزلفى والمنزلة (mufradat)؛ عند حرف صفة يكون موضعا لغيره ولفظه نصب (tahdhib)؛ في التقريب شبه اللزق (tahdhib)؛ مال عن الناس كلهم إليه حتى قرب منه ولزق به (maqayis)
- **B005** başka seçenek, kaçınma payı veya çıkış yolu — başka bir seçenek, kaçınma payı veya çıkış yolu · bir işe ulaşma yolu ya da başka seçenek
  ما عنه عِنْدَد أي ما عنه ميل ولا حيدودة (maqayis)؛ مالي منه عِنْدَد ومُعْلَنْدَد أي بد (sihah;tahdhib)؛ العندد الحيلة (tahdhib)؛ ما وجدت إلى كذا معلنددا أي سبيلا (sihah)
- **B006** sözü dinleyeni almaya veya tutmaya yönelten buyruk — onu al; ona bağlı kal
  وقد يغرى بها تقول عندك زيدا أي خذه (sihah)؛ العرب تأمر من الصفات بعليك وعندك ودونك وإليك (tahdhib)

## ج ع ل (root_000248): 68:35 أَفَنَجْعَلُ, 68:50 فَجَعَلَهُۥ

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

## س ل م (root_000737): 68:35 ٱلْمُسْلِمِينَ, 68:43 سَٰلِمُونَ

- **B001** kusur ve zarardan uzak esenlik — hastalık, kusur ve zarardan uzak olma · hastalık ve zararlı etkilerden kurtulmak · iç kötülükten arınmış yürek · seni koruyana andolsun anlamındaki yemin kalıbı
  السلامة أن يسلم الإنسان من العاهة والأذى (maqayis)؛ السلام يكون بمعنى السلامة (ayn)؛ السلام البراءة من العيوب وقلب سليم أي سالم (sihah)؛ السلامة والعافية (tahdhib)؛ السلم والسلامة التعري من الآفات الظاهرة والباطنة (mufradat)
- **B002** ilahi ad, esenlik selamı ve esenlik yurdu — Tanrı'nın kusur ve yok oluştan uzaklığını bildiren adı · esenlik sizinle olsun · sonsuz esenlik yurdu, cennet · kutsal taşa elle dokunma ya da onu öpme
  الله جل ثناؤه هو السلام وداره الجنة (maqayis)؛ السلام عليكم أي السلامة من الله عليكم وقيل اسم من أسماء الله (ayn)؛ السلام اسم من أسماء الله تعالى (sihah)؛ السلام دعاء للإنسان بأن يسلم من الآفات واسم الله (tahdhib)
- **B003** buyruğa boyun eğip onu kabul etme — Tanrı'nın buyruğuna boyun eğip itaati kabul etme · boyun eğmek · boyun eğip itaate girme
  الإسلام وهو الانقياد لأنه يسلم من الإباء والامتناع (maqayis)؛ الإسلام الاستسلام لأمر الله تعالى وهو الانقياد لطاعته والقبول لأمره (ayn)؛ السلم الاستسلام وأسلم أي دخل في السلم (sihah)؛ الإسلام إظهار الخضوع والقبول (tahdhib)
- **B004** barış ve karşılıklı uzlaşma — barış, uzlaşma ve savaşsızlık · karşılıklı barışma ve çatışmayı bırakma
  السلام المسالمة (maqayis)؛ السلم ضد الحرب (ayn)؛ السلم الصلح والتسالم التصالح والمسالمة المصالحة (sihah)؛ السلم والسلم الصلح (tahdhib)
- **B005** bedeli peşin ödenen vadeli satış — bedeli peşin ödenen vadeli satış · yiyeceğin bedelini önceden ödemek
  السلم الذي يسمى السلف كأنه مال أسلم (maqayis)؛ السلم ما أسلفت به (ayn)؛ السلم بالتحريك السلف وأسلم الرجل في الطعام أي أسلف فيه (sihah)؛ السلم السلف يقال أسلم في كذا وأسلف فيه (tahdhib)
- **B006** merdiven ve amaca ulaştıran araç — merdiven veya bir hedefe ulaştıran araç
  السلم أي السبب والمرقاة والجميع السلاليم (ayn)؛ السلم واحد السلاليم التي يرتقى عليها (sihah)؛ السلم الذي يرتقى عليه والسبب إلى الشيء (tahdhib)
- **B007** sert taşlar ve tekil sert taş — sert taşlar topluluğu · tek bir sert taş · kutsal taşa elle dokunma ya da onu öpme
  الحجارة سميت سلاما لأنها أبعد شيء من الفناء لشدتها (maqayis)؛ السلام الحجارة (ayn)؛ السلمة واحدة السلام وهي الحجارة (sihah)؛ السلام بكسر السين الحجارة الصلبة والواحدة سلمة (tahdhib)
- **B008** deri tabaklamada kullanılan dikenli ağaç — deri tabaklamada kullanılan dikenli ağaç · bir ağaç adı · ağacın yaprak ya da kabuğuyla deriyi tabaklamak
  السلامة شجر والسلم شجر والسلامان شجر (maqayis)؛ السلم ضرب من الشجر وورقه القرظ يدبغ به (ayn)؛ السلم شجر من العضاه والواحدة سلمة وسلمت الجلد إذا دبغته بالسلم (sihah)؛ السلام شجر والسلمة شجرة ذات شوك يدبغ بورقها وقشرها (tahdhib)
- **B009** iyileşme dileğiyle adlandırılan yılan ısırığı mağduru — iyileşme dileğiyle adlandırılan yılan ısırığı mağduru · yılan tarafından ısırılmış kişi · tartışmalı bir aktarımda yılan ısırması
  السليم وهو اللديغ قيل أسلم لما به وقيل تفاءلوا بالسلامة (maqayis)؛ السلم لدغ الحية والملدوغ مسلوم وسليم (ayn)؛ السلام والسليم اللديغ تفاءلوا له بالسلامة ويقال أسلم لما به (sihah)؛ الملدوغ مسلوم وسليم ثم قلت وما قاله غيره في السلم اللدغ (tahdhib)
- **B010** parmak, ayak veya deve tırnağındaki küçük kemik — parmak, ayak veya deve tırnağındaki küçük kemik
  السلامى عظام الأصابع والأشاجع والأكارع (ayn)؛ السلاميات عظام الأصابع والسلامى في الأصل عظم يكون في فرسن البعير (sihah)؛ السلامى عظم يكون في فرسن البعير وعظام القدم كلها سلاميات (tahdhib)
- **B011** tek kulplu kova — tek kulplu uzun kova
  السلم الدلو التي لها عروة واحدة (maqayis)؛ السلم دلو مستطيل له عروة واحدة (ayn)؛ السلم الدلو لها عروة واحدة نحو دلو السقائين (sihah)؛ السلم الدلو التي لها عروة واحدة (tahdhib)
- **B012** bir şeyi başkasına verme veya yüzüstü bırakma [kalıp] — bir şeyi ona verip almasını sağlamak · onu yüzüstü bırakmak veya başkasının eline vermek
  سلمت إليه الشيء فتسلمه أي أخذه وأسلمه أي خذله (sihah)؛ أسلم أمره إلى الله أي سلم (sihah)؛ أسلمت عنها أي تركتها وكل شيء تركته فقد أسلمت عنه (tahdhib)
- **B013** birini tutsak almak [kalıp] — birini tutsak almak
  أخذه سلما أي أسره (ayn)

## ج ر م (root_000239): 68:35 كَٱلْمُجْرِمِينَ

- **B001** kesip ayırma — kesme, kesip ayırma · hurma ürününü ağaçtan kesip toplamak · hurma kesim zamanı veya kesim işi · koyunun yününü kırkmak · ondan keserek almak · hurma ürününü kesip toplayan topluluk · yerden kesilmiş bir parça gibi yükselip yerleşen köklü oluşum
  فالجرم القطع؛ لصرام النخل الجرام؛ جرمت صوف الشاة وأخذته (maqayis)؛ الجرم القطع وقد جرم النخل واجترمه أي صرمه وجرمت صوف الشاة أي جززته (sihah)؛ جرمه يجرمه جرما إذا قطعه؛ جرم النخل وجزمه إذا خرصه وجززه (tahdhib)؛ أصل الجرم قطع الثمرة عن الشجر (mufradat)؛ جرثومة من كلمتين من جرم وجثم كأنه اقتطع من الأرض قطعة فجثم فيها (maqayis-routing)
- **B002** hurma hasadı artığı ve çekirdeği — kesimden sonra düşen veya toplanan hurma artığı · hurma çekirdeği veya kuru hurma · bir müd tutarında yiyecek · hurma salkımının çıktığı çekirdek
  الجرامة ما سقط من التمر إذا جرم؛ الجرام والجريم التمر اليابس (maqayis)؛ الجرامة ما سقط من التمر إذا جرم؛ الجريم النوى وهما أيضا التمر اليابس (sihah)؛ الجرامة ما التقط من التمر بعدما يصرم؛ الجريم النوى وقيل البؤرة التي يرضخ فيها النوى؛ الجرام والجريم هما النوى وهما أيضا التمر اليابس؛ المد يدعى بالحجاز جريما (tahdhib)
- **B003** kazanıp edinme ve bir sonuca sürükleme — kazanmak, elde etmek · ailesinin geçimini kazanan kişi · sizi buna sürüklemesin veya size bunu kazandırmasın · topluluğa öfke kazandırdı veya onu öfkeye sürükledi
  جرم أي كسب لأن الذي يحوزه فكأنه اقتطعه؛ فلان جريمة أهله أي كاسبهم؛ جرمت فزارة أي كسبتهم غضبا (maqayis)؛ جرم يجرم أي كسب؛ فلان جريمة أهله أي كاسبهم؛ ولا يجرمنكم أي لا يحملنكم ويقال لا يكسبنكم (sihah)؛ خرج يجرم قومه أي يكسبهم؛ لا يحملنكم ولا يكسبنكم؛ أجرمني كذا وجرمني وجرمت وأجرمت بمعنى واحد (tahdhib)
- **B004** suç veya günah işleme — suç, günah veya haksız fiil · suç veya günah · suç veya günah işlemek · suçlu veya günahkar kişi · suç işleyen veya haksızlık yapan kişi · birine işlemediği bir suçu yüklemek
  فلان له جريمة أي جرم وهو مصدر الجارم الذي يجرم على نفسه وقومه شرا؛ الجرم الذنب وفعله الإجرام والمجرم المذنب والجارم الجاني (ayn)؛ الجرم الذنب والجريمة مثله؛ جرم وأجرم واجترم بمعنى (sihah)؛ الجرم مصدر الجارم؛ الجارم الجاني والمجرم والمذنب؛ لا يدخلنكم في الجرم؛ الجرم التعدي والجرم الذنب (tahdhib)؛ الجرم والجريمة الذنب وهو من الأول لأنه كسب (maqayis)
- **B005** kuşkusuz ve kaçınılmaz olarak — kuşkusuz, mutlaka veya kaçınılmazdır · kesinlik bildiren kalıplaşmış söyleyiş
  لا جرم يجري مجرى لا بد ويفسر حقا (ayn)؛ لاجرم كانت في الأصل بمنزلة لا بد ولا محالة ثم صارت بمنزلة حقا؛ لا جرم لآتينك (sihah)؛ لا جرم بمنزلة لا بد ولا محالة؛ صارت بمنزلة حقا؛ لا ذا جرم ولا جر (tahdhib)؛ لا جرم هو من قولهم جرمت أي كسبت (maqayis)
- **B006** bir zaman döneminin tamamlanıp sona ermesi — tamamlanıp sona ermiş bir yıl · eksiksiz tamamlanmış bir yıl · bu yılı tamamlayıp geride bıraktık · yıl geçti ve sona erdi
  أقمت عنده حولا مجرما أي حولا تاما حتى انقضى؛ جرمنا هذه السنة أي خرجنا منها وتجرمت السنة والشتاء والصيف (ayn)؛ حول مجرم وسنة محرمة أي تامة؛ تجرمت السنون أي انقضت؛ تجرم الليل ذهب (sihah)؛ سنة مجرمة وشهر مجرم ويوم مجرم وهو التام؛ جرمنا هذه السنة أي خرجنا منها؛ تجرمت السنة؛ كله من الجرم وهو القطع (tahdhib)؛ سنة مجرمة أي تامة كأنها تصرمت عن تمام؛ تجرم الليل ذهب (maqayis)
- **B007** beden, gövde ve bedensel büyüklük — beden, gövde veya cismani yapı · gövdeli veya cüsseli erkek ve kadın · iri gövdeli develer
  الجرم ألواح الجسد وجثمانه؛ رجل جريم وامرأة جريمة أي ذات جرم أي جسم (ayn)؛ الجرم بالكسر الجسد؛ جلة جريم أي عظام الأجرام (sihah)؛ الجرم الجسد؛ الجرم البدن؛ جرم إذا عظم جرمه؛ ألواح الجسد وجثمانه (tahdhib)؛ الجسد جرم لأن له قدرا وتقطيعا؛ مشيخة جلة جريم أي عظام الأجرام (maqayis)
- **B008** sesin gürlüğü ve bedenden iyi çıkışı [kalıp] — sesin gürlüğü veya bedenden iyi çıkışı · ses ya da boğaz berraklığı denmiş, ancak yanlış sayılmış kullanım
  جرم الصوت جهارته؛ ما عرفته إلا بجرم صوته (ayn)؛ الجرم الصوت؛ فلان صافي الجرم أي الصوت أو الحلق وهو خطأ (sihah)؛ الجرم الصوت؛ جرم الصوت جهارته؛ ما عرفته إلا بجرم صوته (tahdhib)؛ قال قوم الصوت يقال له الجرم وأصح من ذلك حسن خروج الصوت من الجرم (maqayis)
- **B009** renk ve rengin durulaşması — rengi saflaştı veya duruldu · renk
  الجرم اللون (sihah)؛ الجرم اللون؛ جرم لونه إذا صفا؛ الجرم اللون والصوت والبدن (tahdhib)
- **B010** sıcaklık ve sıcak bölge — soğuk yerin karşıtı olan sıcak toprak · sıcaklık
  أرض جرم وأرض صرد دخيلان مستعملان في الحر والبرد (ayn)؛ الجرم الحر فارسي معرب؛ الجروم من البلاد خلاف الصرود (sihah)؛ الجرم نقيض الصرد؛ أرض جرم وأرض صرد دخيلان مستعملان في الحر والبرد (tahdhib)
- **B011** Arap kabilesi ve topluluk adı — bir Arap kabilesi veya kabile kolunun adı · bir Arap topluluğunun adı
  جرم قبيلة من اليمن (ayn;tahdhib)؛ جرم بطنان من العرب أحدهما في قضاعة والآخر في طيئ؛ بنو جارم قوم من العرب (sihah)؛ بنو جارم في العرب؛ جرم سميت به وهما بطنان أحدهما في قضاعة والآخر في طي (maqayis)

## ح ك م (root_000348): 68:36 تَحْكُمُونَ, 68:39 تَحْكُمُونَ, 68:48 لِحُكْمِ

- **B001** alıkoyup geri çevirmek — haksızlıktan veya bozulmadan alıkoyup geri çevirmek · sorumsuz kişinin elini tutup zarar vermesini önlemek · yetimi bozulmadan koruyup durumunu düzeltmek · birini yapmak istediği şeyden alıkoymak
  الحكم وهو المنع من الظلم (maqayis)؛ كل شيء منعته من الفساد فقد حكمته وحكمته وأحكمته (ayn)؛ حكمت السفيه وأحكمته إذا أخذت على يده (sihah)؛ كل من منعته من شيء فقد حكمته وأحكمته (tahdhib)؛ حكم أصله منع منعا لإصلاح (mufradat)
- **B002** uyuşmazlığı bağlayıcı kararla sonuçlandırmak — insanlar arasında doğru ölçüyle karar vermek · biri lehine veya aleyhine karar vermek · karar verme veya işi karara bağlama · insanlar arasında karar veren kişi · karar verme işiyle özellikle görevli kişi · çekişmede verilen karar veya yaralanma karşılığını belirleme · çekişmeyi karar verecek bir mercie götürmek
  الحكم وهو المنع من الظلم (maqayis)؛ حاكمناه إلى الله دعوناه إلى حكم الله (ayn)؛ الحكم مصدر قولك حكم بينهم أي قضى (sihah)؛ الحكم أيضا القضاء بالعدل (tahdhib)؛ الحكم بالشيء أن تقضي بأنه كذا أو ليس بكذا (mufradat)
- **B003** bilgi ve usla doğruyu bulma yetkinliği — bilgi ve kavrayış ya da doğru bir önerme · bilgi ve usla doğruyu bulma yetkinliği · bilgili, deneyimli ve doğruyu bulan kişi · deneyimle olgunlaşmış bilge yaşlı
  الحكمة تمنع من الجهل (maqayis)؛ الحكمة مرجعها إلى العدل والعلم والحلم (ayn)؛ الحكمة من العلم والحكيم العالم وصاحب الحكمة (sihah)؛ الحكم العلم والفقه (tahdhib)؛ الحكمة إصابة الحق بالعلم والعقل (mufradat)
- **B004** sağlam ve kusursuz duruma getirmek — bir şeyi sağlamlaştırmak veya sağlam duruma gelmek · kusur ve kuşkuya yer bırakmayacak biçimde sağlamlaştırılmış · işleri sağlam ve kusursuz yapan · övgüye değer niteliğinde doruğa varmak · kendisine zarar verecek şeylerden bütünüyle uzaklaşmak
  استحكم الأمر وثق (ayn)؛ أحكمت الشيء فاستحكم أي صار محكما (sihah)؛ آياته أحكمت وفصلت (tahdhib)؛ المحكم ما لا يعرض فيه شبهة (mufradat)؛ حكم الرجل إذا بلغ النهاية في معناه (tahdhib)
- **B005** karar verme yetkisini başkasına bırakmak — bir işte karar verme yetkisini ona bırakmak · malı üzerinde uygun gördüğü gibi davranabilmek · yetim malını yönetmeye elverişli duruma geldiğinde malı üzerinde tasarruf etmesine izin vermek · birinin elini istediğini yapmakta serbest bırakmak
  حكم فلان في كذا إذا جعل أمره إليه (maqayis)؛ احتكم في ماله إذا جاز فيه حكمه (ayn)؛ حكمته في مالي إذا جعلت إليه الحكم فيه (sihah)؛ حكمنا فلانا بيننا أي أجزنا حكمه بيننا (tahdhib)؛ الحكمين أن يتوليا الحكم عليهم ولهم حسب ما يستصوبانه (mufradat)
- **B006** gemin çene çevresini kuşatan kısıtlayıcı parçası — gemin hayvanın çene çevresini kuşatıp koşmasını sınırlayan parçası · hayvana gem takmak veya onu gemle durdurmak · koyunun çenesi · başında gemin kısıtlayıcı parçası bulunan at
  حكمة الدابة لأنها تمنعها (maqayis)؛ حكمة اللجام ما أحاط بحنكيه (ayn)؛ حكمة اللجام ما أحاط بالحنك (sihah)؛ حكمة اللجام ما أحاط بحنكيه (tahdhib)؛ سميت اللجام حكمة الدابة (mufradat)
- **B007** bir şeyden geri dönmek veya birini döndürmek — bir şeyden geri dönmek · birini bir şeyden geri döndürmek
  حكم فلان عن الشيء أي رجع؛ وأحكمته أنا أي رجعته (tahdhib)

## ك ت ب (root_001283): 68:37 كِتَٰبٌ, 68:47 يَكْتُبُونَ

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

## د ر س (root_000470): 68:37 تَدْرُسُونَ

- **B001** izin silinip belirsizleşmesi veya silik kalıntısının sürmesi — gizlenmiş, güç seçilen yol · izi silinip belirsizleşmek veya silik kalıntısı sürmek · rüzgar izini silmek · silinme ve belirsizleşme
  يدل على خفاء وخفض وعفاء؛ الدرس الطريق الخفي (maqayis;sihah)؛ درس المنزل عفا (maqayis)؛ الدرس بقية أثر الشيء الدارس ودرسته الرياح أي عفته (ayn)؛ درس الرسم يدرس دروسا أي عفا ودرسته الريح (sihah)؛ درس الأثر دروسا أو درسه الريح أي محته (tahdhib)؛ درس الدار معناه بقي أثرها وبقاء الأثر يقتضي انمحاءه (mufradat)
- **B002** bir metni öğrenmek ve akılda tutmak için sürekli okuyup inceleme — öğrenmek ve akılda tutmak için okuma · kitabı, kutsal metni veya bilgiyi okuyup öğrenmek · bir metni biriyle birlikte okuyup akılda tutmak için tekrarlamak · kitapları karşılıklı okuyup gözden geçirmek · okuma ve öğrenme yeri · okunup çalışılan kitap · kutsal metinlerin okunup öğretildiği yer
  درست القرآن وغيره (maqayis)؛ الدرس درس الكتاب للحفظ ودارست فلانا كتابا لكي أحفظ (ayn)؛ درست الكتاب درسا ودراسة ودارست الكتب وتدارستها وادارستها (sihah)؛ درست الكتاب أدرسه دراسة والمدرس المكان والمدرس الكتاب والدراس المدارسة (tahdhib)؛ درس الكتاب ودرست العلم تناولت أثره بالحفظ وإدامة القراءة (mufradat)
- **B003** giysi veya dokumanın eskiyip yıpranması — eskiyip yıpranmış giysi veya yaygı · eskiyip yıpranmış giysiler · giysiyi eskitip yıpratmak
  الدريس الثوب الخلق (maqayis)؛ الدريس الثوب الخلق وكذلك من البسط ونحوها (ayn)؛ الدرس بالكسر الدريس وهو الثوب الخلق وقد درس الثوب أي أخلق (sihah)؛ الدرس والدرس والدريس الثوب الخلق ودرست الثوب أي أخلقته (tahdhib)
- **B004** kadının aybaşı görmesi — kadın aybaşı görmek · kadının cinsel organı için aybaşıyla ilgili örtmeceli ad · aybaşı gören genç kız
  درست المرأة حاضت وأبو أدراس (maqayis;sihah)؛ الدروس دروس الجارية إذا طمشت وجارية دارس وجوار درس ودوارس (tahdhib)؛ درست المرأة كناية عن حاضت (mufradat)
- **B005** buğdayı, tahılı veya yiyeceği ayakla çiğneme — buğdayı, tahılı veya bu bağlamdaki yiyeceği ayakla çiğnemek · tahılı veya bu bağlamdaki yiyeceği ayakla çiğneme işlemi
  درست الحنطة وغيرها في سنبلها إذا دستها (maqayis)؛ درسوا الحنطة دراسا أي داسوها (sihah)؛ درس الطعام يدرس دراسا إذا ديس والدراس الدياس (tahdhib)
- **B006** devede uyuzun ortaya çıkması ve deride iz bırakması — devedeki uyuz veya deride bıraktığı iz · deve uyuza tutulmak veya derisinde uyuz izi oluşmak · uyuzlu veya derisinde uyuz izi bulunan deve
  الدرس الجرب القليل يكون بالبعير (maqayis;sihah)؛ الدرس ضرب من الجرب يبقى له أثر متفش في الجلد (ayn)؛ شيء خفيف من درس والدرس الجرب أول ما يظهر منه ودرس البعير إذا جرب جربا شديدا (tahdhib)؛ درس البعير صار فيه أثر جرب (mufradat)
- **B007** iri veya kalın boyunlu canlı — kalın boyunlu veya iri yapılı kişi ya da hayvan · iri veya uysal ve kalın boyunlu develer
  مما شذ عن الباب الدرواس الغليظ العنق من الناس والدواب (maqayis)؛ الدرواس الغليظ العنق من الناس والكلاب وهو العظيم والدراوس العظام من الإبل (sihah)؛ الدرواس الكبير الرأس من الكلاب والدراوس من الإبل الذلل الغلاظ الأعناق (tahdhib)

## ي م ن (root_001698): 68:39 أَيْمَٰنٌ

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

## ب ل غ (root_000151): 68:39 بَٰلِغَةٌ

- **B001** bir yere, şeye veya son sınıra ulaşma; bağlama göre yaklaşma ya da olgunluğa erme — yere veya şeye ulaşmak · yer, zaman veya iş bakımından en son sınıra varma · belirlenmiş sürenin sonuna yaklaşmak · çocuğun olgunluk çağına erişmesi · güç veya yaş bakımından belirlenmiş sınıra erişmek
  الوصول إلى الشيء؛ بلغت المكان إذا وصلت إليه (maqayis;sihah)؛ بلغت المكان بلوغا وصلت إليه (sihah)؛ بلغ الشيء يبلغ بلوغا (ayn)؛ البلوغ والبلاغ الانتهاء إلى أقصى المقصد والمنتهى مكانا كان أو زمانا أو أمرا (mufradat)؛ المشارفة بلوغا بحق المقاربة (maqayis)؛ بلغ الغلام أدرك (sihah)
- **B002** bir şeyi, özellikle iletiyi, hedefine ulaştırma — ulaştırmak veya erişmesini sağlamak · iletiyi yerine ulaştırmak · iletme ve ulaştırma işi
  أبلغته إبلاغا؛ بلغته تبليغا في الرسالة ونحوها (ayn)؛ بلغت الرسالة تبليغا (jamhara)؛ الإبلاغ الإيصال وكذلك التبليغ؛ بلغت الرسالة (sihah)
- **B003** yaşamı sürdürmeye yetecek ölçü ve geçim aracı — yeterli miktar veya yeten şey · yaşamı sürdürecek azık ve geçimlik · eldeki şeyle yetinmek · bir iş için yeterli olma
  البلغة ما يتبلغ به من عيش؛ لي في هذا بلاغ أي كفاية (maqayis)؛ في كذا بلاغ وتبليغ أي كفاية (ayn)؛ البلغة القوت يتبلغ به الإنسان (jamhara)؛ البلاغ أيضا الكفاية؛ البلغة ما يتبلغ به من العيش؛ تبلغ بكذا أي اكتفى به (sihah)
- **B004** amacını açık ve etkili sözle anlatma yetkinliği — amacını açık ve etkili sözle anlatma yetkinliği · dili güçlü, sözünü açık ve etkili anlatan kişi · anlatılmak isteneni açık ve etkili biçimde ileten söz
  البلاغة التي يمدح بها الفصيح اللسان لأنه يبلغ بها ما يريده (maqayis)؛ رجل بلغ بليغ وقد بلغ بلاغة (ayn)؛ كلام بلغ وبليغ؛ بلغ الرجل بلاغة إذا صار بليغا (jamhara)؛ البلاغة الفصاحة؛ بلغ الرجل أي صار بليغا (sihah)
- **B005** bir şeyi ulaşılabilir en ileri dereceye götürme — iyi veya nitelikli şey · bütün gücünü kullanıp eksik bırakmamak · eksiksiz buyruk veya en güçlü biçimde pekiştirilmiş ant
  شيء بالغ أي جيد؛ المبالغة أن تبلغ من العمل جهدك (ayn)؛ شيء بالغ أي جيد؛ بلغ في الجودة مبلغا؛ أمر الله بلغ أي بالغ؛ بالغ فلان في أمري إذا لم يقصر فيه (sihah)؛ أيمان علينا بالغة أي منتهية في التوكيد (mufradat)
- **B006** düşüncesizliğine karşın istediğine ulaşan kişi — düşüncesizliğine karşın istediğini elde eden kişi
  هو أحمق بلغ وبلغ أي إنه مع حماقته يبلغ ما يريده (maqayis)؛ أحمق بلغ أي أحمق يبلغ ما يريد (jamhara)؛ أحمق بلغ أي هو مع حماقته يبلغ ما يريده (sihah)
- **B007** atı hızlandırmak için dizgini ileri verme [kalıp] — binicinin atı hızlandırmak için dizgini ileri vermesi
  بلغ الفارس يراد به أنه يمد يده بعنان فرسه ليزيد في عدوه (maqayis)؛ بلغ الفارس إذا مد يده بعنان فرسه ليزيد في جريه (sihah)
- **B008** yokluk veya hastalığın kişiyi iyice sıkıştırması [kalıp] — yokluğun veya hastalığın kişinin üzerinde ağırlaşması
  تبلغت القلة بفلان إذا اشتدت (maqayis)؛ تبلغت به العلة أي اشتدت (sihah)
- **B009** üzücü olayı duyup ondan uzak kalmayı dileme — insanı üzen ve kendisine ulaşan haber · duyalım ama başımıza gelmesin dileği
  اللهم سمع لا بلغ أي نسمع بمثل هذا فلا تنزله بنا (ayn)؛ اللهم سمع لا بلغ معناه يسمع به ولا يتم (sihah)
- **B010** birini kötüleyici bildirimler — bir kimseyi kötüleyen bildirimler ve çekiştirmeler
  البلاغات كالوشايات (sihah)
- **B011** başa gelen ağır ve yıkıcı büyük olay — ağır ve yıkıcı büyük olay · başımıza ağır ve yıkıcı bir olay geldi
  البُلغين الداهية؛ بلغت منا البُلغين (sihah)

## ق و م (root_001273): 68:39 ٱلْقِيَٰمَةِ

- **B001** erkekler topluluğu ve yakın çevresi — aslen erkeklerden oluşan topluluk · bir erkeğin yandaşları ve yakın soy çevresi · topluluklar; çoğulun çoğulu
  القوم الرجال دون النساء؛ قوم كل رجل شيعته وعشيرته (ayn;tahdhib)؛ القوم الرجال دون النساء؛ ربما دخل النساء فيه على سبيل التبع (sihah)؛ القوم جماعة الرجال في الأصل دون النساء؛ وفي عامة القرآن أريدوا به والنساء جميعا (mufradat)؛ القوم جمع امرئ ولا يكون ذلك إلا للرجال؛ وربما استعير في غيرهم (maqayis)
- **B002** ayağa kalkma ve dik durma — ayağa kalkmak veya dikilmek · bir kez ayağa kalkma; iki bölüm arasındaki ayakta duruş · kökleri üzerinde dikili kalmış
  القومة ما بين الركعتين من القيام؛ قمت قياما؛ منها هامد ومنها قائم (ayn;tahdhib)؛ قام الرجل قياما؛ القومة المرة الواحدة؛ قامت الدابة وقفت (sihah)؛ قيام بالشخص إما بتسخير أو اختيار؛ ساجدا وقائما؛ تركتموها قائمة على أصولها (mufradat)؛ قام قياما والقومة المرة الواحدة إذا انتصب (maqayis)
- **B003** bir işe kararlılıkla girişme [kalıp] — bu işi üstlenip kararlılıkla girişti
  قام بمعنى العزيمة؛ قام بهذا الأمر إذا اعتنقه؛ قيام عزم (maqayis)؛ القيام الذي هو العزم؛ إذا قمتم إلى الصلاة (mufradat)
- **B004** sürekli gözetip yönetme — işi gözeten, koruyan ve yürüten kişi · topluluğun işlerini yöneten kişi · her şeyi sürekli yöneten ve koruyan · onu taşıyamadı veya buna gücü yetmedi
  قيم القوم من يسوس أمرهم ويقومهم؛ القائم في الملك ونحوه الحافظ؛ القيوم (ayn)؛ قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم؛ القيوم اسم من أسماء الله (sihah)؛ قيم القوم الذي يقومهم ويسوس أمرهم؛ القائم بالأمر؛ القيوم القائم على كل شيء (tahdhib)؛ قيام للشيء هو المراعاة للشيء والحفظ له؛ قوامين لله؛ القيوم القائم الحافظ لكل شيء (mufradat)؛ قام بهذا الأمر إذا اعتنقه؛ قوام الدين والحق أي به يقوم (maqayis)
- **B005** sürdürüp gereğini yerine getirme [kalıp] — bir şeyi sürdürmek, işler halde tutmak veya gereğini yerine getirmek · ibadetin ya da kitabın gereklerini eksiksiz uygulamak
  أقام الشيء أي أدامه؛ يقيمون الصلاة (sihah)؛ أقمت الشيء وقومته فقام بمعنى استقام؛ إقام الصلاة (tahdhib)؛ إقامة الشيء توفية حقه؛ تقيموا التوراة والإنجيل؛ أقيموا الصلاة؛ مقيم الصلاة (mufradat)
- **B006** bir yerde kalma ve kalınan yer — bir yerde yerleşip kalmak · ayak basılan veya kalınan yer ya da süre; oturum veya toplanmış topluluk
  أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين؛ المقام والمقامة الموضع الذي تقيم فيه (ayn;tahdhib)؛ المقامة الإقامة؛ المقامة المجلس والجماعة من الناس؛ المقام موضع القيام أو الإقامة (sihah)؛ المقام يكون مصدرا واسم مكان القيام وزمانه؛ المقامة الإقامة؛ لا مقام لكم أي لا مستقر لكم (mufradat)
- **B007** başkasının yerini ve işlevini alma [kalıp] — onun yerine geçti veya adına görev yaptı
  القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)؛ قام فلان مقام فلان إذا ناب عنه؛ يقومان مقامهما (mufradat)؛ أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك (maqayis)
- **B008** düzgünlük, denge ve doğru yoldan sapmama — düzgün ve dengeli olmak; doğru yoldan ayrılmamak · düzgün, dengeli ve doğru
  رمح قويم ورجل قويم؛ القيمة الملة المستقيمة؛ إذا انقاد واستمرت طريقته فقد استقام (ayn)؛ الاستقامة الاعتدال؛ استقام له الأمر؛ قومت الشيء فهو قويم أي مستقيم؛ القوام العدل؛ دينا قيما (sihah)؛ الاستقامة على الطاعة؛ القيم هو المستقيم؛ أقوم كلاما أي أعدل كلاما (tahdhib)؛ الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم؛ دينا قيما أي ثابتا (mufradat)
- **B009** ayakta tutan dayanak ve geçim temeli — bir şeyi ayakta tutan dayanak, düzen ve geçim temeli
  هذا الأمر لا قومية له أي لا قوام له؛ القوام من العيش ما يقيمك ويغنيك؛ القيام العماد؛ قوام كل شيء ما استقام به (ayn)؛ قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه؛ جعل الله لكم قياما (sihah)؛ قوام الأمر وملاكه؛ تقيمكم فتقومون بها؛ قوام الجسم تمامه؛ قوام كل شيء ما استقام به (tahdhib)؛ القيام والقوام اسم لما يقوم به الشيء؛ جعلها مما يمسككم؛ قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم (mufradat)؛ قوام الدين والحق أي به يقوم (maqayis)
- **B010** değer biçme ve belirlenen bedel — değer biçmeyle belirlenen bedel · malın değerini belirlemek veya ulaştığı bedeli bildirmek
  القيمة ثمن الشيء بالتقويم؛ تقاوموا فيما بينهم (ayn)؛ قومت السلعة؛ استقمت السلعة؛ القيمة واحدة القيم (sihah)؛ القيمة ثمن الشيء بالتقويم؛ تقاوموه فيما بينهم؛ استقمت المتاع أي قومته؛ قامت الأمة مائة دينار أي بلغت قيمتها (tahdhib)؛ تقويم السلعة بيان قيمتها (mufradat)؛ قومت الشيء تقويما؛ أصل القيمة الواو (maqayis)
- **B011** insanın boyu ve düzgün beden yapısı — insanın boyu ve beden uzunluğu · düzgün ve güzel boy; beden yapısı
  القامة مقدار قيام الرجل؛ قوام الجسم تمامه وطوله (ayn)؛ قوام الرجل قامته وحسن طوله؛ قامة الإنسان قده (sihah)؛ القامة قامة الرجل؛ حسن القامة والقمة والقومية؛ قوام الجسم تمامه (tahdhib)؛ تقويم الإنسان في أحسن تقويم؛ انتصاب القامة (mufradat)؛ القوام الطول الحسن؛ القومية القوام والقامة (maqayis)
- **B012** düzeneğin dik, taşıyıcı veya tutulan parçası — kuyu makarası veya ona bağlı donanım · kuyu başındaki insan biçimli yapı diye aktarılmış, fakat yanlış sayılmış yorum · kılıç sapı veya yatak, masa ve hayvanın dik duran parçası · çiftçinin elinde tuttuğu ahşap parça
  القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر؛ قائم السيف مقبضه؛ قائمة السرير والخوان والدابة (ayn)؛ القامة البكرة بأداتها؛ قائم السيف وقائمته مقبضه؛ القائمة واحدة قوائم الدواب؛ المقوم الخشبة التي يمسكها الحراث (sihah)؛ القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة؛ قائم السيف مقبضه وما سوى ذلك فهو قائمة (tahdhib)؛ القامة البكرة بأداتها (maqayis)
- **B013** ölülerin diriltildiği ve insanların yargı için kalktığı gün — ölülerin diriltildiği ve insanların yargı için ayağa kalktığı son gün
  القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)؛ يوم القيامة معروف (sihah)؛ القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم (tahdhib)؛ القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين (mufradat)
- **B014** karşılıklı direnip mücadele etme [kalıp] — ona karşı durup mücadele etmek; tarafların birbirine karşı koyması
  قاومته في كذا أي نازلته (ayn)؛ قاومه في المصارعة وغيرها؛ تقاوموا في الحرب أي قام بعضهم لبعض (sihah)؛ ما زلت أقاوم فلانا في هذا الأمر أي أنازله (tahdhib)
- **B015** tam ve denk ağırlıktaki para — ölçün ağırlığa tam denk gelen, ağır basmayan para
  دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)؛ دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح (tahdhib)
- **B016** donup akmama veya yorulup ilerleyememe [kalıp] — su dondu veya akmaz halde kaldı · binek hayvanı durdu veya yorulup yürüyemedi
  قام الماء جمد؛ قامت الدابة وقفت (sihah)؛ قامت لفلان دابته إذا كلت أو عيت فلم تسر (tahdhib)
- **B017** güneşin tam tepede olduğu öğle ortası — güneşin ortada, günün iki yarısının dengede olduğu öğle vakti
  قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn;tahdhib)؛ قام ميزان النهار إذا انتصف؛ قام ميزان النهار فاعتدل (tahdhib)
- **B018** pazarın canlanıp satışların artması [kalıp] — pazar canlandı ve mallar alıcı buldu
  قامت السوق نفقت (sihah)؛ قامت السوق إذا نفقت ونامت إذا كسدت (tahdhib)
- **B019** bir beden bölümünün kişiye ağrı vermesi [kalıp] — sırtım veya gözlerim ağrıdı
  قام بي ظهري أي أوجعني؛ قامت بي عيناي؛ كل ما أوجعك من جسدك فقد قام بك (tahdhib)
- **B020** koyunun bacaklarını tutan hastalık — koyunun bacaklarını tutup onu ayağa kaldıran hastalık
  القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)؛ أخذها قوام وهو داء يأخذها في قوائمها تقوم منه (tahdhib)
- **B021** göz bebeği sağlamken görme yetisinin kaybolması — göz bebeği sağlam kaldığı halde görmeyen göz
  عين قائمة ذهب بصرها والحدقة صحيحة (ayn)؛ العين القائمة أن يذهب بصرها والحدقة صحيحة (tahdhib)

## س ء ل (root_000661): 68:40 سَلْهُمْ, 68:46 تَسْـَٔلُهُمْ

- **B001** bilgi sormak veya bir şey istemek — sormak; istemek · sorma; soru; istekte bulunma · soru veya istek konusu · çok soru soran kimse · sor; iste · sorular veya istek konuları · soran ya da isteyen kimse; yardım isteyen yoksul · ondan bir şeyi istemek · ona bir şey hakkında soru sormak · bir kişi hakkında soru sormak · ilk ses düşürülerek söylenen sormak biçimi
  سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)
- **B002** istenen şey — bir kimsenin istediği şey
  السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)
- **B003** birinin isteğini yerine getirmek — birinin isteğini veya gereksinimini karşılamak
  أسألته سؤلته ومسألته أي قضيت حاجته (sihah)
- **B004** birbirine soru sormak — birbirlerine soru sormak
  تساءلوا أي سأل بعضهم بعضا (sihah)

## ECHO س ل ل (root_000736): for 68:40 سَلْهُمْ, 68:46 تَسْـَٔلُهُمْ: withheld observed target; not identity

- **B001** nazikçe ve fark ettirmeden çekip çıkarma — bir şeyi çekip çıkarmak · kılıcı kınından çekmek · hamurdaki kılı ayıklayıp çıkarmak
  سللت الشيء أسله سلا (maqayis;sihah;tahdhib)؛ إخراجك الشعر من العجين (ayn;tahdhib)؛ سل الشيء من الشيء نزعه (mufradat)
- **B002** gizlice çalma — hırsızlık; gizli hırsızlık · gizli hırsızlık; ayrıca rüşvet · çalmak · hırsız
  السلة والإسلال السرقة (maqayis)؛ الإسلال السرقة الخفية (ayn;tahdhib)؛ الإسلال الرشوة والسرقة (sihah)؛ سل الشيء من البيت على سبيل السرقة (mufradat)
- **B003** kökenden çıkan yavru veya öz — oğul; çocuk · kız evlat · tay ve dişi tay · kökten ayrılan öz; üreme maddesi
  السليل الولد (maqayis;sihah;tahdhib)؛ السلالة ما استل منه والنطفة سلالة الإنسان (sihah;tahdhib;mufradat)؛ السليل والسليلة المهر والمهرة (ayn;tahdhib)
- **B004** aradan sıyrılıp çıkma — dar yerden veya kalabalıktan sıyrılıp çıkma · aralarından çıkmak · topluluktan gizlice ayrılma
  الانسلال المضي والخروج من بين مضيق أو زحام (ayn;tahdhib)؛ انسل من بينهم أي خرج (sihah)؛ يتسللون منكم لواذا (tahdhib;mufradat)
- **B005** birbirine bağlı dizi — zincir; parçaların birbirine bağlanması · birbirine bağlı · bulut boyunca uzanan şimşek · birbirine eklenen kıvrımlı kum
  السلسلة اتصال الشيء بالشيء (maqayis)؛ شيء مسلسل متصل بعضه ببعض (sihah)؛ السلسلة معروفة وبرق ذو سلاسل ورمل ذو سلاسل (tahdhib)؛ ومنه السلسلة (mufradat)
- **B006** tatlı, duru ve kolay akan su — suyun boğazdan veya eğimden kolayca akması · tatlı, duru ve kolay içilen su · boğazdan kolay geçen duru şarap · kolay içilen, lezzetli ve hızlı akan kaynak suyu
  تسلسل الماء في الحلق إذا جرى وماء سلسل وسلسال (maqayis;sihah;tahdhib)؛ السلسل الماء العذب الصافي (ayn;tahdhib)؛ ماء سلسل متردد في مقره حتى صفا (mufradat)
- **B007** vadi içindeki su yolu veya çukur arazi — vadide dar su yolu; su toplayan alçak yer · vadi içindeki dar su yolları veya ağaçlı çukur yerler · geniş ve ağaçlı vadi
  السال مسيل في مضيق الوادي (maqayis;sihah;tahdhib)؛ السليل الوادي الواسع ينبت السلم والسمر (sihah;tahdhib)؛ السلان بطون من الأرض غامضة ذات شجر (tahdhib)
- **B008** tüberküloz — tüberküloz · tüberküloz · tüberküloz hastası
  السلال من المرض كأن لحمه قد سل (maqayis)؛ السل والسلال داء يأخذ الإنسان ويقتل (ayn)؛ السلال بالضم السل (sihah)؛ داء يهزل ويضني ويقتل (tahdhib)؛ مرض ينزع به اللحم والقوة (mufradat)
- **B009** atın yarıştaki güçlü ileri atılımı [kalıp] — atın yarışta ileri atılıp öne çıkması
  فرس شديد السلة وهي دفعته في سباقه (maqayis;sihah;tahdhib)؛ خرجت سلة هذا الفرس على سائر الخيل (ayn;tahdhib)
- **B010** çuvaldız — çuvaldız; iri dikiş iğnesi
  المسلة معروفة لأنها تسل الخيط سلا (maqayis)؛ المسلة المخيط وجمعه مسال (ayn)؛ المسلة واحدة المسال وهي الإبر العظام (sihah)
- **B011** sepet veya kapaklı kap — ekmek sepeti · kapaklı sepet veya kap
  سلة الخبز معروفة (sihah)؛ السلة السبذة المطبقة كالجؤنة (ayn;tahdhib)؛ سبذة الطين السلة (tahdhib)
- **B012** ince uzun şerit, lif veya uç — saçtan veya dokudan ince uzun şerit · hörgüçteki uzun şeritler veya burun içi doku parçaları · dilin ince ucu · uzun ve sivri diken · hurma dalından sıyrılmış ince parça
  السليلة عقبة أو عصبة أو لحمة شبه طرائق (ayn;tahdhib)؛ سليلة من شعر لما استل من ضريبته (sihah)؛ سلائل السنام طرائق طوال (tahdhib)؛ أسلة اللسان الطرف الرقيق (mufradat)؛ السلاءة من الشوك لأن فيها امتدادا (maqayis)
- **B013** biçime bağlı adlandırmalar — kumaşın giyilmekten incelmesi · kılıç yüzeyinin dalgalı parıltısı · çizgili süslü kumaş · eti azalıp bedeni oluklaşmış kişi
  تسلسل الثوب وتخلخل إذا لبس حتى رق؛ التسلسل بريق فرند السيف ودبيبه؛ ثوب ملسلس فيه وشي مخطط؛ المتسلسل الذي تخدد لحمه وقل
- **B014** dişleri düşmüş olma — dişleri düşmüş erkek, kadın veya koyun · yaşlılıktan dişleri düşmüş dişi deve
  السلة الناقة التي سقطت أسنانها؛ رجل سل وامرأة سلة وشاة سلة أي ساقطة الأسنان
- **B015** su teknesi destekleri arasındaki boşluk — su teknesinin dikili parçaları arasındaki boşluk
  السلة الفرجة بين نصائب الحوض

## ز ع م (root_000633): 68:40 زَعِيمٌ

- **B001** doğruluğu kesinleşmemiş bir sözü aktarma veya ileri sürme — doğruluğu kesinleşmemiş bir sözü aktarmak veya ileri sürmek · yalan söylemek, yalan yere iddia etmek · güvenilmeyen veya tartışmalı iddialar · güvenilmeyen ve üzerinde çekişilen iş veya iddia · semiz olup olmadığı bilinmediği için elle yoklanan hayvan · doğrulanmamış bir sözü aktarırken kullanılan kuşku sözü
  القول من غير صحة ولا يقين والتزعم الكذب والزعوم التي يشك في سمنها (maqayis)؛ إذا شك في قوله وبزعمهم أي بقولهم الكذب والتزعم التكذب (ayn)؛ زعم أي قال والأمر الذي لا يوثق به مزعم وفي قول فلان مزاعم وناقة زعوم وشاة زعوم (sihah)؛ الزعم يكون حقا ويكون باطلا وبزعمهم أي بقولهم الكذب والزعم والتزاعم أكثر ما يقال فيما يشك فيه ولا يحقق (tahdhib)؛ الزعم حكاية قول يكون مظنة للكذب (mufradat)
- **B002** bir şeyi elde etmeyi umup ona yönelme — bir şeyi elde etmeyi ummak · olmayacak şeye umut bağlamak · umut bağlanan şey veya elde etme fırsatı
  زعم في غير مزعم أي طمع في غير مطمع (maqayis)؛ الزعم بالتحريك الطمع وليس بمزعم أي ليس بمطمع (sihah)؛ زعم يزعم زعما إذا طمع وأمر مزعم أي مطمع (tahdhib)
- **B003** sözle güvence verip sorumluluğu üstlenme — bir şey için güvence verip sorumluluğunu üstlenmek · güvence veren ve doğan yükü üstlenen kişi · sözle güvence verme ve sorumluluk üstlenme · bir iş üzerinde birleşip birbirine arka çıkmak
  زعم بالشيء إذا كفل به (maqayis)؛ زعمت به أي كفلت والزعيم الكفيل (sihah)؛ الزعيم غارم وأنا به زعيم أي كفيل وتزاعم القوم إذا تظافروا عليه (tahdhib)؛ الضمان بالقول زعامة والمتكفل زعيم (mufradat)
- **B004** topluluğun işlerini üstlenip adına konuşan önderlik — önderlik, saygın baş olma ve topluluğu temsil etme · topluluğun başı ve onun adına konuşan önder · bir topluluğun önderi olmak · önderin ganimet payı veya malın en iyi bölümü
  الزعامة وهي السيادة لأن السيد يتكفل بالأمور وحظ السيد من المغنم أو أفضل المال (maqayis)؛ زعيم القوم سيدهم ورأسهم الذي يتكلم عنهم (ayn)؛ الزعامة السيادة وزعيم القوم سيدهم (sihah)؛ الزعامة الشرف والرئاسة وزعيم القوم سيدهم ومدرههم (tahdhib)؛ الرئاسة زعامة والرئيس زعيم (mufradat)
- **B005** savaş aracı, özellikle zırh — savaş aracı veya zırh
  والزعامة للغلام يريد السلاح (sihah)؛ الزعامة الدرع (tahdhib)
- **B006** yılan — yılan
  المزعامة الحية (tahdhib)

## ش ر ك (root_000791): 68:41 شُرَكَآءُ, 68:41 بِشُرَكَآئِهِمْ

- **B001** ortaklık ve ortak olma — ortaklık ve ortak olma · ortak · ortak olmak veya birini ortak etmek · karşılıklı olarak ortaklaşmak · herkesin ortak olduğu veya eşit yararlandığı şey · ortaklık payı
  الشركة أن يكون الشيء بين اثنين لا ينفرد به أحدهما (maqayis)؛ الشركة مخالطة الشريكين (ayn;tahdhib)؛ شاركت فلانا صرت شريكه (sihah)؛ شركه في الأمر إذا دخل معه فيه (tahdhib)؛ خلط الملكين أو شيء لاثنين فصاعدا (mufradat)
- **B002** Tanrı'ya ortak koşma — Tanrı'ya ortak koşma · Tanrı'ya ortak koşmak · Tanrı'ya ortak koşan kimse · büyük ve küçük ortak koşma türleri
  الشرك ظلم عظيم (ayn)؛ الشرك أيضا الكفر (sihah)؛ أن تجعل لله شريكا في ربوبيته (tahdhib)؛ إثبات شريك لله تعالى (mufradat)
- **B003** eş veya evlilik yoluyla hısım — eş veya evlilik yoluyla hısım · sizinle evlilik yoluyla hısım olmak istedik
  في المصاهرة رغبنا في شرككم وصهركم (ayn;tahdhib)؛ فلان شريك فلان إذا تزوج بابنته أو بأخته (tahdhib)؛ امرأة الرجل شريكته (tahdhib)
- **B004** sandal kayışı ve sandala kayış takma — sandal kayışı · sandala kayış takmak
  شراك النعل مشبه بهذا (maqayis)؛ الشراك سير النعل (ayn;tahdhib)؛ أشركت نعلي جعلت لها شراكا (sihah)؛ شركت النعل وأشركتها إذا جعلت لها شراكا (tahdhib)
- **B005** yolun ana yatağı, izleri ve küçük kolları — yolun ana yatağı, ortası veya izleri · ana yoldan ayrılan küçük yollar · otlağın yollar veya izler halinde uzanması
  الشرك لقم الطريق وهو شراكه (maqayis)؛ الشرك أخاديد الطريق الواضح (ayn)؛ الشركة معظم الطريق ووسطه (sihah)؛ شرك الطريق أنساع الطريق (tahdhib)؛ أم الطريق معظمه وبنياته أشراك صغار (tahdhib)
- **B006** avın dolandığı kapan ve tuzak benzetmesi — avın dolandığı av kapanı · tek bir av kapanı · dünyanın tuzağı
  شرك الصائد سمي بذلك لامتداده (maqayis)؛ الشرك حبالة يرتبك فيها الصيد (ayn)؛ الشرك بالتحريك حبالة الصائد (sihah)؛ شرك الصائد حبالته يرتبك فيها الصيد (tahdhib)؛ شرك الدنيا أي حبالتها (mufradat)
- **B007** özel yapılarda hızlı ve art arda oluş — hızlı ve art arda tokatlar · suya birbiri ardından geliş
  لطمه لطما شركيا أي سريعا متتابعا (sihah)؛ لطمه لطما شركيا أي متتابعا (tahdhib)؛ ورد بعد ورد متتابع (sihah)
- **B008** kaygılı iç konuşma veya bölünmüş görüş — kaygılı biçimde kendi kendine konuşan · görüşü tek olmayan veya bölünmüş
  رأيت فلانا مشتركا إذا كان يحدث نفسه كالمهموم (sihah;tahdhib)؛ رأيه مشترك ليس بواحد (tahdhib)

## ء ت ي (root_000009): 68:41 فَلْيَأْتُوا۟

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

## ص د ق (root_000852): 68:41 صَٰدِقِينَ

- **B001** sözün inançla ve gerçekle uyuşması — doğruluk; sözün inançla ve gerçekle uyuşması · konuşurken doğruyu söylemek · birine doğru söz söylemek veya onun sözünü doğru saymak · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse · çok doğru sözlü kimse
  الصدق خلاف الكذب (maqayis;ayn;sihah;tahdhib)؛ الصدق والكذب أصلهما في القول (mufradat)؛ الصدق مطابقة القول الضمير والمخبر عنه معا (mufradat)
- **B002** nesnenin sağlamlığı veya düzgünlüğü — bir nesnedeki sertlik veya düzgünlük · sert ve güçlü nesne ya da mızrak
  شيء صدق أي صلب (maqayis)؛ رمح صدق (maqayis)؛ الصدق الصلب والمستوي (sihah;tahdhib)
- **B003** tamlık, iyilik ve güvenilirlik — iyi, güvenilir ve erdemli kişi ya da topluluk · bir şeyde tamlık ve kusursuzluk · övülmeye değer, iyi ve sağlam durum
  رجل صدق (maqayis;ayn;sihah;tahdhib)؛ الصدق الكامل من كل شيء (ayn;tahdhib)؛ في مقعد صدق وقدم صدق ومدخل صدق ومخرج صدق ولسان صدق (mufradat)
- **B004** sözü veya beklentiyi doğrulayıp gerçekleştirme — savaşta gereğini yerine getirip sebat etmek · atılımında veya koşusunda verdiği sözü tutan · tahmini gerçekleşmek veya tahminini gerçekleştirmek · bir sözün veya durumun doğruluğunu ortaya koyma ve onaylama · öncekini doğrulayan ve destekleyen · sözü doğru kabul edip onaylayan kimse · doğruluğa sürekli bağlı ve kuşkusuz onaylayan kimse
  صدقوهم القتال (maqayis;sihah;tahdhib)؛ صدق في القتال إذا وفى حقه (mufradat)؛ صدق ظني (mufradat)؛ لقد صدق عليهم إبليس ظنه أي حقق ظنه (tahdhib)؛ مصدق لما معهم (mufradat)
- **B005** içten sevgiye dayalı dostluk — dost veya yakın arkadaş · içten sevgiye dayalı arkadaşlık ve dostluk kurma
  الصداقة مشتقة من الصدق في المودة (maqayis)؛ الصداقة مصدر الصديق (ayn;tahdhib)؛ الصداقة والمصادقة المخالة (sihah)؛ الصداقة صدق الاعتقاد في المودة (mufradat)
- **B006** mal vererek yardım etme veya haktan vazgeçme — iyilik amacıyla maldan verilen yardım veya bu adla anılan yükümlü pay · bir hakkından bağışlayarak vazgeçmek · mali yardım veren kimse · hayvanlara ilişkin yardım paylarını toplayan görevli · mali yardım veren erkekler ve kadınlar
  الصدقة ما يتصدق به المرء عن نفسه وماله (maqayis)؛ المتصدق المعطي للصدقة (ayn;sihah;tahdhib)؛ المصدق الذي يأخذ صدقات الغنم (maqayis;sihah;tahdhib)؛ الصدقة ما يخرجه الإنسان من ماله على وجه القربة (mufradat)؛ من تجافى عنه (mufradat)
- **B007** kadına belirlenen evlilik hakkı olan mal — kadına verilen veya belirlenen evlilik hakkı olan mal · kadının evlilikte aldığı mal veya kadınlara ait bu tür mallar · kadına evlilik hakkı olarak mal belirlemek
  الصداق صداق المرأة (maqayis)؛ الصداق والصدقة والصدقة المهر (ayn)؛ الصداق والصداق مهر المرأة (sihah)؛ صداق المرأة وصدقة المرأة (tahdhib)؛ صداق المرأة وصداقها وصدقتها ما تعطى من مهرها (mufradat)

## ك ش ف (root_001302): 68:42 يُكْشَفُ

- **B001** örtüyü kaldırıp açığa çıkarma — örtüyü kaldırıp açığa çıkarmak · açığa çıkmak · açığa çıkmak · sıkıntısını gidermek · kötülüğü gidermek ve uzaklaştırmak
  سرو الشيء عن الشيء (maqayis)؛ كشفت الثوب وغيره (maqayis)؛ رفعك شيئا عما يواريه ويغطيه (ayn;tahdhib)؛ كشفت الشئ فانكشف وتكشف (sihah)؛ كشفت الثوب عن الوجه وغيره (mufradat)؛ كشف غمه (mufradat)؛ يكشف السوء (mufradat)
- **B002** belirli yapılarda güçlü biçimde açığa çıkma [kalıp] — şimşek görünüşüyle göğü doldurdu · birbirlerinin kusurları karşılıklı olarak açığa çıktı
  تكشف البرق إذا ملأ السماء (maqayis;sihah)؛ لأن المتكشف بارز (maqayis)؛ لو تكاشفتم ما تدافنتم أي لو انكشف عيب بعضكم لبعض (sihah)
- **B003** belirli beden ve donanım durumlarında açıkta kalma veya biçim özelliği — alın saç çizgisindeki halka biçimli veya yukarı doğru çıkan saç · alın saç çizgisindeki halka veya yukarı yönlü saç dönüşü · alın saç çizgisinde halka ya da yukarı yönlü saç dönüşü bulunan kimse · atın kuyruk sokumundaki eğrilik · savaşta kalkanı bulunmayan adam · gülerken dudağı dönüp diş etleri görünmek
  الكشفة دائرة في قصاص الناصية (maqayis;ayn;tahdhib)؛ الكشف في الخيل التواء في عسيب الذنب (maqayis;sihah)؛ الأكشف الرجل الذي لا ترس معه في الحرب (maqayis;sihah;tahdhib)؛ أكشف الرجل إكشافا إذا ضحك فانقلبت شفته حتى تبدو درادره (tahdhib)
- **B004** düşmanlığı açıkça başlatma [kalıp] — ona karşı düşmanlığı açıkça başlatmak
  كاشفه بالعداوة أي بادأه بها (sihah)
- **B005** dişi devenin üreme aralığına ilişkin tartışmalı teknik kullanım — 
  الكشاف نتاج في إثر نتاج (maqayis)؛ أن تبقى الأنثى سنتين أو ثلاثا لا يحمل عليها (maqayis)؛ الكشوف الناقة التي يضربها الفحل وهي حامل (ayn;sihah;tahdhib)؛ هذا التفسير خطأ (tahdhib)؛ الكشاف أن يحمل على الناقة بعد نتاجها وهي عائذ قد وضعت حديثا (tahdhib)؛ إذا حمل على الناقة سنتين متواليتين فذاك الكشاف (sihah;tahdhib)
- **B006** şiddetli durumun ortaya çıkması — 
  يوم يكشف عن ساق (mufradat)؛ أصله من قامت الحرب على ساق أي ظهرت الشدة (mufradat)؛ وقال بعضهم أصله من تذمير الناقة (mufradat)

## س و ق (root_000762): 68:42 سَاقٍ

- **B001** sürüp götürme — sürüp götürmek · sürme ve götürme · sürücü · sürüp götürmek; sürülerek gitmek · sürülüp götürülen hayvan topluluğu · rüzgarın sürüklediği bulut · sürüp götürmesi için deve vermek · kadına evlilik ödemesini götürüp vermek · kadına götürülen evlilik ödemesi
  أصل واحد وهو حدو الشيء (maqayis)؛ ساقه يسوقه سوقا (maqayis)؛ سقته سوقا (ayn)؛ ساق الماشية يسوقها سوقا وسياقا (sihah)؛ سوق الإبل جلبها وطردها (mufradat)؛ السيقة ما استيق من الدواب (maqayis)؛ السيقة ما يساق من الدواب (mufradat)؛ السيق من السحاب ما طردته الريح (tahdhib)؛ أسقتك إبلا أي أعطيتك إبلا تسوقها (sihah)
- **B002** ölüm sancısı ve son varışa götürülüş — ölüm anında can çekişmek · ölüm sancısı, can çekişme · son varış ve oraya götürülüş · can çekişmek; ses değişmeli söyleyiş
  رأيته يسوق سياقا أي ينزع نزعا يعني الموت (ayn)؛ السياق نزع الروح (sihah)؛ فلان في السياق أي في النزع (tahdhib)؛ إلى ربك يومئذ المساق (mufradat)؛ يفوق بنفسه وهذا من باب الإبدال وإنما أصله يسوق (maqayis)
- **B003** bacak ya da taşıyıcı gövde — bacak; bitki gövdesi · ağaç gövdesi · bacaklar; gövdeler · iri ya da uzun bacaklı · bacağından vurmak veya yaralamak · uzun gövdeli bitki
  الساق لكل شجر وإنسان وطائر (ayn)؛ الساق ساق القدم والجمع سوق وسيقان وأسؤق (sihah)؛ ساق الشجرة جذعها (sihah)؛ الساق للإنسان وغيره والجمع سوق إنما سميت بذلك لأن الماشي ينساق عليها (maqayis)؛ فاستوى على سوقه هو جمع ساق (mufradat)؛ سقت الإنسان إذا أصبت ساقه (tahdhib)؛ امرأة سوقاء ورجل أسوق إذا كان عظيم الساق (maqayis)
- **B004** şiddetin açığa çıkması ve işe sıkı sarılma [kalıp] — şiddetin ve güçlüğün açığa çıkması · işe ciddiyetle ve hazırlıkla sarılmak · savaş iyice kızıştı
  يوم يكشف عن ساق أي عن شدة (sihah)؛ عن ساق عن شدة (tahdhib)؛ قيل للأمر الشديد ساق (tahdhib)؛ قام فلان على ساق إذا عني بالأمر وتحزم له (tahdhib)؛ كشفت الحرب عن ساقها (mufradat)
- **B005** pazar yeri — pazar yeri · alışveriş yapmak
  السوق موضع البياعات (ayn;tahdhib)؛ السوق مشتقة من هذا لما يساق إليها من كل شيء والجمع أسواق (maqayis)؛ تسوق القوم إذا باعوا واشتروا (sihah)؛ السوق الموضع الذي يجلب إليه المتاع للبيع (mufradat)
- **B006** savaşın en kızgın yeri [kalıp] — savaşın en kızgın yeri
  سوق الحرب حومة القتال (ayn;sihah;tahdhib)؛ سوق الحرب حومة القتال وهي مشتقة من الباب الأول (maqayis)
- **B007** sıradan halk ve yönetilenler — sıradan halk, yönetilenler
  السوقة أوساط الناس والجميع السوق (ayn)؛ السوقة خلاف الملك (sihah)؛ السوقة بمنزلة الرعية التي يسوسها الملك (tahdhib)
- **B008** erkek güvercin ya da kumru — erkek güvercin veya kumru · erkek kumru adı veya ses taklidi
  الساق الذكر من الحمام (ayn)؛ ساق حر ذكر القماري (sihah)؛ الساق الحمام الذكر (tahdhib)؛ ساق حر صوت القمري كأنه حكاية صوته (tahdhib)
- **B009** üzengi kayışı — üzengi kayışı
  الأساقة سير الركاب للسروج (ayn)؛ الإساقة سير الركاب للسروج (tahdhib)
- **B010** tekili kaydedilmemiş kolyeler — kolyeler; tekili kaydedilmemiş çoğul ad
  الأياسق القلائد ولم نسمع لها بواحد (tahdhib)
- **B011** güçlülükte övünme yarışına girmek — güçlülükte karşılıklı övünmek
  ومنه قولهم ساوقه أي فاخره أينا أشد (sihah)
- **B012** birbiri ardınca gelme — peş peşe ilerlemek · birbiri ardınca
  تساوقت الإبل إذا تتابعت (tahdhib)؛ ولدت فلانة ثلاثة بنين على ساق واحد أي بعضهم على إثر بعض (sihah;tahdhib)
- **B013** ordunun art bölümü [kalıp] — ordunun art bölümü
  ساقه الجبش مؤخره (sihah)
- **B014** tanımı verilmeyen bilinen bir ad — 
  السويق معروف (sihah;tahdhib)

## د ع و (root_000478): 68:42 وَيُدْعَوْنَ, 68:43 يُدْعَوْنَ

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

## ECHO د ع ع (root_000477): for 68:42 وَيُدْعَوْنَ, 68:43 يُدْعَوْنَ: withheld observed target; not identity

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

## س ج د (root_000675): 68:42 ٱلسُّجُودِ, 68:43 ٱلسُّجُودِ

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

## خ ش ع (root_000412): 68:43 خَٰشِعَةً

- **B001** boyun eğip dinginleşme — boyun eğip başını ya da bedenini alçaltmak · beden, ses, bakış ve organlarda beliren boyun eğiş ve dinginlik · boyun eğen, kendini alçaltan; kimi kullanımda eğilerek duran · göğsünü eğip alçakgönüllü bir tutum almak · boyun eğişi zorlayarak sergilemek veya öyle görünmeye çalışmak · yalvararak boyun eğen ve kendini alçaltan · alçakgönüllü görünerek başını eğmek · bakışını kısmak veya yere indirmek · seslerin dinip alçalması · içteki yakarışın organların sakin duruşuna yansıması
  أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه؛ الخاشع المستكين والراكع (maqayis)؛ الخشوع رميك ببصرك إلى الأرض؛ متخشع متضرع؛ خشعت الأصوات أي سكنت (ayn)؛ الخاشع المستكين؛ الخاشع الراكع؛ خشع ببصره إذا غضه (jamhara)؛ الخشوع الخضوع؛ التخشع تكلف الخشوع (sihah)؛ التخشع لله الإخبات والتذلل؛ خشع الرجل إذا رمى ببصره إلى الأرض؛ الخشوع في البدن والصوت والبصر (tahdhib)؛ الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح (mufradat)
- **B002** yere yakın arazi parçası — yere yakın arazi parçası veya küçük yükselti · yere yakın, basık sırt veya yükselti · tozlu ve yerleşimsiz yöre · kurumuş, bitkisiz ve cansız toprak · çöküp yerle bir olmuş duvar
  الخشعة قطعة من الأرض قف قد غلبت عليه السهولة؛ قف خاشع لاطئ بالأرض؛ بلدة خاشعة مغبرة (maqayis)؛ الخشعة قف غلبت عليه السهولة؛ أكمة خاشعة لاطئة بالأرض (ayn)؛ الخشعة قطعة من الأرض تغلظ؛ الخاشع المطمئن من الأرض (jamhara)؛ بلدة خاشعة مغبرة؛ مكان خاشع؛ الخشعة أكمة متواضعة (sihah)؛ الحثمة اللاطئة بالأرض هي الخشعة؛ الخشعة الأكمة؛ إذا يبست الأرض ولم تمطر قيل قد خشعت؛ أرض خاشعة هامدة؛ جدار خاشع (tahdhib)
- **B003** görünürlüğü azalıp kaybolmaya yaklaşma [kalıp] — güneşin tutulup kararması · yıldızların ufka inip batmaya yaklaşması
  خشعت الشمس وكسفت وخسفت بمعنى واحد؛ خشوع الكواكب إذا غارت فكادت تغيب في مغيبها؛ خشعت الكواكب إذا دنت من المغيب (tahdhib)
- **B004** hörgücün yağını yitirip çökmesi [kalıp] — devenin hörgücünün yağını yitirip çökmesi
  خشع سنام البعير إذا ذهب إلا أقله (maqayis)؛ خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه (tahdhib)
- **B005** göğüsten yapışkan salgı çıkarmak [kalıp] — göğüsten gelen yapışkan salgıyı çıkarıp atmak
  خشع خراشي صدره إذا ألقى بزاقا لزجا (maqayis)؛ خشع الإنسان خراشي صدره إذا ألقى من صدره بزاقا لزجا (jamhara)؛ خشع الرجل خراشي صدره إذا رمى بها؛ جعل خشع واقعا ولم أسمعه لغيره (tahdhib)

## ر ه ق (root_000606): 68:43 تَرْهَقُهُمْ

- **B001** baskıyla kuşatıp etkisi altına alma — bir şeyin onu baskıyla kuşatması · taşkınlığın onu kaplaması · istemediği bir şeyin veya borcun başına çökmesi
  رهقه الأمر غشيه (maqayis)؛ الرهق غشيان الشيء (ayn;tahdhib)؛ رهقه بالكسر يرهقه رهقا أي غشيه (sihah)؛ رهقه الأمر غشيه بقهر (mufradat)
- **B002** hedefe veya eşiğe iyice yaklaşma — peşinden gidip yetişmesine çok yaklaşmak · yetişip yakalamak · ergenliğe yaklaşmış oğlan · ergenliğe yaklaşmak · geniş adımlarıyla kendisini yönetene yaklaşan dişi deve · yüze yakın
  المراهق الغلام الذي دانى الحلم؛ الرهوق من النوق الجواد الوساع التي ترهقك (maqayis)؛ رهق فلان فلانا إذا تبع فقرب أن يلحقه (ayn;tahdhib)؛ طلبت فلانا حتى رهقته أي حتى دنوت منه (sihah)؛ القوم رهاق مائة أي زهاء مائة (sihah;tahdhib)
- **B003** ağır bir yükümlülüğü zorla yükleme — ona güç ve ağır bir iş yüklemek · beni güçlüğe sokma · ona zahmetli bir çıkış yükleyeceğim
  أرهقتهم أمرا صعبا إذا حملتهم عليه (ayn)؛ أرهقه عسرا أي كلفه إياه (sihah)؛ المحمول عليه في الأمر ما لا يطيق (tahdhib)؛ سأرهقه صعودا (ayn;mufradat)
- **B004** geciktirerek zamanı daraltma ve aceleye sıkıştırma — namazı bir sonraki vaktin yaklaşmasına kadar geciktirmek · süre dolmak üzereyken kente girmek · topluluğun onu namaz kılmaya acele ettirmesi · acele
  أرهق القوم الصلاة أخروها حتى يدنو وقت الصلاة الأخرى؛ الرهق العجلة (maqayis)؛ أرهقنا الصلاة أي استأخرنا عنها (ayn)؛ أرهق الصلاة أي أخرها حتى يدنو وقت الأخرى (sihah)؛ أرهقني القوم أن أصلي أي أعجلوني؛ دخل مكة مراهقا أي ضاق عليه الوقت (tahdhib)؛ أرهقت الصلاة إذا أخرتها حتى غشي وقت الأخرى (mufradat)
- **B005** ağır ahlaki sapma ve sınır aşımı — haksızlık · yalan ve kusur · bilgisizlik, akıl hafifliği, sertlik ve düşüncesizlik · onda yasakları çiğneme eğilimi bulunması · hakkında kötülük düşünülen veya inancı bakımından suçlanan kişi · ağır bir büyüklük taslama ve bozulmuşluk taşıması · onların kötü durumunu daha da artırdılar
  الرهق العجلة والظلم؛ الرهق عجلة في كذب وعيب (maqayis)؛ الرهق جهل في الإنسان وخفة في عقله؛ الرهق الكذب؛ الرهق العظمة؛ الرهق الظلم؛ الرهق العيب (ayn)؛ فيه رهق أي غشيان للمحارم؛ فلا يخاف بخسا ولا رهقا أي ظلما؛ فزادوهم رهقا أي سفها وطغيانا (sihah)؛ فزادوهم رهقا أي ذلة وضعفا؛ طغيانا؛ إثما؛ غيا؛ به رهق شديد وهي العظمة والفساد؛ الخفة والعربدة (tahdhib)
- **B006** konukların ve yardım isteyenlerin sık uğradığı cömert kişi — konukların, ziyaretçilerin ve yardım isteyenlerin sık uğradığı kişi
  رجل مرهق تنزل به الضيفان (maqayis)؛ رجل مرهق أيضا أي ينزل به الضيفان يأتونه (ayn)؛ رجل مرهق إذا كان يغشاه الناس وينزل به الضيفان (sihah)؛ المرهق الذي يغشاه السؤال والضيفان؛ المرهق الكريم الجواد (tahdhib)
- **B007** safran — safran
  الريهقان الزعفران (sihah)؛ الريهقان الزعفران قاله أبو عبيدة (tahdhib)

## ذ ل ل (root_000519): 68:43 ذِلَّةٌ

- **B001** hor ve güçsüz duruma düşüp boyun eğme — horluk içinde boyun eğme · hor düşmüş ve güçsüz kişi · horluk ve güçsüzlük hali · hor düşürülme ve aşağılanma · güçsüz ve korumasız kimseler · onu hor düşürdü · onu boyun eğdirip horladı · onu hor görüp aşağılamaya çalıştı · ona boyun eğdi · adamın yanındakiler güçsüz düştü · aileyi ve malı korumak için bir ölçüde boyun eğmek · acıma duygusuyla ezilmiş gibi boyun eğmek · güçsüzlük yüzünden edinilen koruyucu müttefik
  الخضوع والاستكانة واللين والذل ضد العز (maqayis)؛ الذل ضد العز ورجل ذليل بين الذل والذلة والمذلة (sihah)؛ الذل الخسة ولم يكن له ولي من الذل (tahdhib)؛ الذل ما كان عن قهر (mufradat)
- **B002** değerini yitirmeden gönüllü yumuşaklık [kalıp] — inananlara karşı yumuşak ve sevecen olmak · sevecenlikten gelen yumuşaklık ve uyum
  أذلة على المؤمنين رحماء رفيقين وجانبهم لين ليس أنهم أذلاء مهانون (tahdhib)؛ الذل متى كان من جهة الإنسان نفسه لنفسه فمحمود (mufradat)
- **B003** direnç veya güçlüğün azalıp yönlendirme, erişim ya da kullanıma elverişli hale gelmesi — zorluktan sonra yumuşayıp uysallaşma · uysal ve kolay yönlendirilen · aileyi ve malı koruyan ölçülü yumuşaklık veya eziyete sabır · yürünerek kolay geçilir olmuş yol · meyve salkımlarını sarkıtıp kolay erişilir kılmak · hurma salkımlarını indirip toplamayı kolaylaştırmak · sulanıp ürün vermeye elverişli kılınmış hurma ağaçları · suyun oraya giden yolunu kolaylaştırdı · kolay izlenen yollar veya direnmeden yönelen arılar · uyaklar ozan için kolaylaştı · huysuzluktan sonra uysallaşan binek
  الذل خلاف الصعوبة ودابة ذلول وذلل القطف تذليلا إذا لان وتدلى (maqayis)؛ الذل بالكسر اللين ضد الصعوبة ودابة ذلول وذللت قطوفها (sihah)؛ طريق مذلل إذا كان موطوءا سهلا وسبل ربك ذللا وذللت قطوفها وتسهيل القوافي (tahdhib)؛ الذل ما كان بعد تصعب وشماس وذلت الدابة وسبل ربك ذللا وذللت قطوفها (mufradat)
- **B004** işleri uygun akışında yürütme [kalıp] — işleri kendi uygun yolu ve halinde yürütmek · kendi hali veya yönü üzere
  أجر الأمور على أذلالها أي استقامتها (maqayis)؛ جاء على أذلاله أي على وجهه وأمور الله جارية على أذلالها أي على مجاريها وطرقها (sihah)؛ أجر الأمور على أذلالها أي على أحوالها التي تصلح عليها وتتيسر وتسهل وعلى أذلاله أي على وجهه (tahdhib)؛ الأمور تجري على أذلالها أي مسالكها وطرقها (mufradat)
- **B005** aşağı sarkan alt bölüm ve fiziksel kısalık — gömleğin yere yakın sarkan etek uçları · gömleğin tek bir alt etek ucu · kısa veya alçak duvar, ev ve mızrak
  ذلاذل القميص ما يلي الأرض من أسافله (maqayis)؛ ذلاذل القميص ما يلي الأرض من أسافله وقصر الذلاذل (sihah)؛ حائط ذليل أي قصير وبيت ذليل قصير السمك ورمح ذليل قصير والذلاذل أسافل القميص الطويل (tahdhib)
- **B006** başı darbeyle yarılan kazık [kalıp] — başı darbelerle yarılan kazık
  عير المذلة الوتد لأنه يشج رأسه (sihah)
- **B007** belirli fiil biçiminde hızla ilerleme — adam hızla ilerledi
  اذلولى الرجل إذليلاء إذا أسرع وهو من الباب (maqayis)

## و ذ ر (root_001638): 68:44 فَذَرْنِى

- **B001** et parçası; bir aktarımda etsiz kemik parçası — et parçası; bir aktarıma göre etsiz kemik parçası · et parçaları · bol et parçalı ekmek yemeği
  الوذرة وهي الفدرة من اللحم (maqayis)؛ الوذرة قطعة عظم لا لحم فيه (ayn)؛ الوذرة بالتسكين الفدرة وهي القطعة من اللحم (sihah)؛ الوذرة القطعة من اللحم مثل الفدرة (tahdhib)؛ الوذر بضع اللحم (tahdhib)؛ الوذرة قطعة من اللحم (mufradat)؛ ثريدة كثيرة الوذر (tahdhib)
- **B002** eti parçalama veya yarayı çizerek açma — eti parçalama veya yarayı çizerek açma · eti parçalara ayırmak · yarayı çizerek açmak · et parçasını küçük parçalara bölmek
  التوذير أن يشرط الجرح (maqayis)؛ وذرت اللحم توذيرا قطعته وكذلك الجرح إذا شرطته (sihah)؛ وقد وذرت الوذرة أذرها وذرا إذا بضعتها بضعا (tahdhib)
- **B003** bir şeyi bırakmak — bir şeyi bırakmak · önemsiz gördüğü şeyi bir yana atmak · bunu bırak · onu bırakmak
  ذر ذا (maqayis)؛ أماتت المصدر من يذر والفعل الماضي واستعملته في الحاضر والأمر (ayn)؛ ذره أي دعه وهو يذره (sihah)؛ ذرذا ودع ذا ولا يقال وذرته (tahdhib)؛ يذر الشيء أي يقذفه لقلة اعتداده به (mufradat)
- **B004** cinsel göndermeli ağır soy sövgüsü; ad biçiminde klitoris — cinsel organ göndermeli ağır bir soy sövgüsü · ağır bir soy sövgüsü · klitoris
  يا ابن شامة الوذر (maqayis;ayn;sihah;tahdhib)؛ كلمة قذف (sihah)؛ كلمة معناها القذف (tahdhib)؛ عرض لها بأعضاء الرجال (maqayis)؛ أراد المذاكير (tahdhib)؛ أرادوا بها القلف (tahdhib)؛ الوذفة والوذرة بظارة المرأة (tahdhib)

## ح د ث (root_000299): 68:44 ٱلْحَدِيثِ

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

## د ر ج (root_000468): 68:44 سَنَسْتَدْرِجُهُم

- **B001** yol boyunca ilerleme — çocuğun veya yaşlının kendine özgü yürüyüşü · çocuk yürümeye başladı · adam ya da kertenkele yürüyüp ilerledi · geçit, yol veya geçilen güzergah · tepeyi ya da dağ aralarını kesen yollar · geldiği yoldan geri döndü · kertenkelenin yolunu açık bırak · geçip giden rüzgar · bineğin ayakları · burası senin yuvan değil, yoluna git · yürüyenlerle ölüp gidenleri birlikte anarak aşırı yalancılığı anlatan söz · çocuğun ilk yürüyüşünde tutunup ilerlediği araç
  أصل واحد يدل على مضي الشيء والمضي في الشيء؛ رجع فلان أدراجه؛ درج الصبي إذا مشى مشيته؛ مدارج الأكمة الطرق المعترضة فيها (maqayis)؛ الدرجان مشية الشيخ والصبي؛ المدرجة ممر الأشياء؛ رجعت في أدراجي ودرجي أي طريقي (ayn)؛ درج الصبي إذا مشى؛ فلان على درج كذا أي على سبيله؛ مدرجة الطريق قارعته (jamhara)؛ درج الرجل والضب أي مشى؛ المدرجة المذهب والمسلك؛ رجعت أدراجي (sihah)؛ الريح التي تدرج أي تمر مرا؛ درج في غير مثل هذا الموضع مثل دب؛ للطريق الذي يدرج فيه الغلام والريح وغيرهما مدرج ومدرجة ودرج (tahdhib)؛ مدرجة قارعة الطريق؛ درج الشيخ والصبي درجانا مشى (mufradat)
- **B002** yükseliş dizisindeki basamak veya düzey — basamaklar ve yükselen sıralar · düzey, sıra veya yüksek konum · cennet katları ve düzeyleri · gök kuşağının ölçü bölümü
  الدرج جماعة عتب الدرجة؛ الدرجة في الرفعة والمنزلة؛ درجات الجنان منازل؛ كل برج من بروج السماء ثلاثون درجة (ayn)؛ الدرج الواحدة درجة وهي المنزلة؛ فلان في درجة عالية أي في منزلة رفيعة (jamhara)؛ الدرجة المرقاة؛ الدرجة واحدة الدرجات وهي الطبقات من المراتب (sihah)؛ الدرجة الرفعة في المنزلة؛ كل برج من بروج السماء ثلاثون درجة (tahdhib)؛ الدرجة نحو المنزلة إذا اعتبرت بالصعود؛ درجات النجوم (mufradat)
- **B003** aşama aşama ilerleme veya ilerletme — onu bir şeye azar azar yaklaştırdı · kandırıp yavaş yavaş bir işe çekti · bir konuda basamak basamak ilerledi · hastaya önce az verip yiyeceği giderek artırdı · onları azar azar ele geçireceğiz
  درجه إلى كذا واستدرجه أي أدناه منه على التدريج (sihah)؛ سنأخذهم قليلا قليلا ولا نباغتهم؛ استدرجه أي خدعه حتى حمله على أن درج في ذلك؛ درجت العليل تدريجا إذا أطعمته شيئا قليلا ثم زدته؛ استدرجه كلامي أي أقلقه حتى تركه يدرج (tahdhib)؛ يتدرج في كذا أي يتصعد فيه درجة درجة؛ نأخذهم درجة فدرجة؛ إدناؤهم من الشيء شيئا فشيئا (mufradat)
- **B004** tükenip geride kimse bırakmama — topluluk yok olup tükendi · adam öldü ve soy bırakmadı · yaşayanlarla ölüp gidenleri birlikte anarak aşırı yalancılığı anlatan söz
  درج الشيء إذا مضى لسبيله؛ درج الرجل إذا مضى ولم يخلف نسلا (maqayis)؛ درج قرن بعد قرن أي فنوا (ayn)؛ درج أي مات وانقرض؛ درج الرجل إذا لم يخلف نسلا وليس كل من مات درج (jamhara)؛ درج القوم إذا انقرضوا؛ أكذب الأحياء والأموات (sihah)؛ درج قرن بعد قرن أي فنوا؛ يقال للقوم إذا انقرضوا درجوا (tahdhib)؛ استعير الدرج للموت؛ من مات فطوى أحواله (mufradat)
- **B005** katlayıp içine sararak kapatma — bir yoruma göre onları kitap gibi dürüp kapatacağız · belgeyi katladı veya katının içine yerleştirdi · ölüyü kefenlerine sardı · bükümleri birbirine geçmiş sıkı nesne
  أصل آخر يدل على ستر وتغطية؛ أدرجت الكتاب وأدرجت الحبل (maqayis:درج)؛ المحدرج المفتول حتى يتداخل بعضه في بعض؛ درج من أدرجت (maqayis:المحدرج)؛ أدرجت الكتاب وفي درج الكتاب كذا (ayn)؛ درجت الشيء وأدرجته إذا طويته (jamhara)؛ أدرجت الكتاب طويته؛ في درج الكتاب أي في طيه (sihah)؛ أدرجت الكتاب إدراجا؛ الإدراج لف الشيء في الشيء؛ أدرج الميت في أكفانه؛ أدرجت الكتاب في الكتاب إذا جعلته في درجه أي في طيه (tahdhib)؛ الدرج طي الكتاب والثوب؛ يقال للمطوي درج (mufradat)
- **B006** eşya koymaya yarayan kutu veya kap — özellikle güzel koku ve kişisel araçlar için kullanılan küçük eşya kutusu
  الدرج لبعض الأصونة والآلات أصل آخر يدل على ستر وتغطية (maqayis)؛ الدرج حفش من أحفاش النساء (ayn)؛ الدرج سفيط صغير تجعل فيه المرأة طيبها (jamhara)؛ الدرج الذي يكتب فيه؛ الدرج بالضم حفش النساء (sihah)؛ الدرج درج المرأة تضع فيه طيبها وأداتها وهو الحفش (tahdhib)؛ الدرج سفط يجعل فيه الشيء (mufradat)
- **B007** yabancı yavruyu benimseten sarılı bez — dişi deveye başka yavruyu benimsetmek için kullanılan sarılı bez
  الدرجة خرق تجعل في حياء الناقة ثم تسل فإذا شمتها الناقة حسبتها ولدها فعطفت عليه (maqayis)؛ الدرجة خرقة تدرج فتجعل في حياء الناقة إذا ظئرت (ayn)؛ الدرجة خرق تلف وتدخل في حياء الناقة تعالج بها (jamhara)؛ الدرجة شيء يدرج فيدخل في حياء الناقة ثم تشمه فتظنه ولدها فترأمه (sihah)؛ الخرق التي تدرج إدراجا وتلف وتدس في حياء الناقة يقال لها الدرجة (tahdhib)؛ الدرجة خرقة تلف فتدخل في حياء الناقة (mufradat)
- **B008** doğum zamanı bakımından nitelenen dişi deve — doğum zamanıyla ilişkisi kaynaklara göre farklı açıklanan gebe dişi deve
  المدراج الناقة تضمر حتى يلحق حقبها بالتصدير؛ المدراج أيضا الناقة لا تجاوز يومها الذي ضربت فيه حتى تنتج والتي تجاوز يقال لها الجرور (ayn)؛ ناقة مدراج إذا تأخرت عن وقت ولادها أياما (jamhara)؛ درجت الناقة وأدرجت إذا جازت السنة ولم تنتج فهي مدراج (sihah)؛ ناقة مدراج إذا كانت تؤخر جهازها؛ المدراج الناقة التي تجر الحمل إذا أتت على مضربها (tahdhib)
- **B009** belirli bir kuş türü — yürüyüşü veya rengiyle betimlenen belirli bir kuş türü
  الدراج من الطير بمنزلة الحيقطان من طير العراق أرقط (ayn)؛ الدراج ضرب من الطير أحسبه مولدا (jamhara)؛ الدرجة طائر أسود باطن الجناحين؛ الدراج الدراجة ضرب من الطير (sihah)؛ الدرجة طائر أسود باطن الجناحين؛ الدراج من الطير بمنزلة الحيقطان (tahdhib)؛ الدراج طائر يدرج في مشيته (mufradat)

## ح ي ث (root_000375): 68:44 حَيْثُ

- **B001** ardından gelen yan tümceyle belirlenen yer — ardından gelen yan tümceyle belirlenen yer · her nerede; nerede olursa · belirtilen yerden · aynı yer anlamındaki lehçe varyantı
  كلمة موضوعة لكل مكان وهي مبهمة (maqayis)؛ كلمة معروفة يستدل بها على المكان مبنية على الضم (jamhara)؛ كلمة تدل على المكان لأنه ظرف في الأمكنة بمنزلة حين في الأزمنة (sihah)؛ حيث ظرف من المكان أي الموضع الذي كنت فيه وإلى أي موضع شئت (tahdhib)؛ عبارة عن مكان مبهم يشرح بالجملة التي بعده (mufradat)

## م ل و (root_001446): 68:45 وَأُمْلِى

- **B001** zamansal uzama ve süre tanıma — uzun bir yaşam ya da zaman dilimi · ona süre tanımak · gece ile gündüz · uzun bir zaman · uzun süre · bir zaman boyunca kalmak · uzatma ve süre verme · yaşam süren
  أصل صحيح يدل على امتداد في شيء زمان (maqayis)؛ الملوان الليل والنهار (maqayis)؛ الملاوة ملاوة العيش أي قد أملي له (maqayis)؛ الإملاء الإمداد (mufradat)؛ للمدة الطويلة ملاوة من الدهر وملي من الدهر (mufradat)؛ أملي لهم أي أمهلهم (mufradat)؛ عشت مليا أي طويلا (mufradat)؛ الملوان قيل الليل والنهار وحقيقة ذلك تكررهما وامتدادهما (mufradat)
- **B002** uzun süre yararlanıp tadını çıkarma — yaşamının tadını çıkarmak · giysiyi uzun süre kullanıp ondan yararlanmak · bir şeyden uzun süre yararlanıp tadını çıkarmak
  تمليت عمري إذا استمتعت به (maqayis)؛ تمليت الثوب تمتعت به طويلا (mufradat)؛ تملى بكذا تمتع به بملاوة من الدهر (mufradat)
- **B003** zamansal olmayan uzama ve genişletme — devenin bağını gevşetip hareket alanı açmak · genişçe uzanan açık arazi
  يدل على امتداد في شيء زمان أو غيره (maqayis)؛ أمليت القيد للبعير إملاء إذا وسعته (maqayis)؛ الملا مقصور المفازة الممتدة (mufradat)
- **B004** dinlenmesi veya yazılması için sözlü aktarma — metni yazdırmak üzere söylemek · kendisine metin sözlü olarak aktarılmak
  ومن الباب إملاء الكتاب (maqayis)؛ أمليت الكتاب أمليه إملاء (mufradat)؛ فهي تملى عليه بكرة وأصيلا (mufradat)؛ أصل أمليت أمللت (mufradat)

## ECHO م ل ي (root_001447): for 68:45 وَأُمْلِى: withheld observed target; not identity

- **B001** uzun zaman ve uzun süre devam etme — uzun süre; uzun zaman · uzun zaman dilimi · uzun süre yanında kalmak · ondan uzun süre yararlanmak · uzun bir dönem boyunca kalmak · gece ile gündüz · Tanrı ömrünü uzun etsin
  كلمة واحدة هي الزمن الطويل (maqayis)؛ أقام مليا أي دهرا طويلا (maqayis)؛ المدة الطويلة ملاوة من الدهر وملي من الدهر (mufradat)؛ تمليت دهرا أبقيت وتملى بكذا تمتع به بملاوة من الدهر (mufradat)؛ ملاك الله غير مهموز عمرك وعشت مليا أي طويلا (mufradat)؛ الملوان طرفا الليل والنهار (maqayis)
- **B002** ek süre vermek ve ertelemek — ek süre verme; erteleme · onlara ek süre vermek
  الإملاء الإمداد (mufradat)؛ وأملي لهم إن كيدي متين أي أمهلهم (mufradat)؛ أنما نملي لهم خير لأنفسهم (mufradat)
- **B003** yazıya geçirilmek üzere söylemek — metni yazması için söylemek · ona yazması için söylenmek
  أمليت الكتاب أمليه إملاء (mufradat)؛ فهي تملى عليه بكرة وأصيلا (mufradat)؛ فليملل وليه بالعدل (mufradat)
- **B004** uzayıp giden ıssız kır — uzayıp giden ıssız kır
  الملا مقصور المفازة الممتدة (mufradat)

## ك ي د (root_001334): 68:45 كَيْدِى (also echo for 68:51 يَكَادُ)

- **B001** bir şeyi yoğun çabayla işleme — bir şeyi yoğun çabayla işleme ve onunla uğraşma · onu yoğun çabayla ele alıp işlemek
  يدل على معالجة لشيء بشدة (maqayis)؛ الكيد المعالجة (maqayis)؛ كل شيء تعالجه فأنت تكيده (maqayis;sihah)
- **B002** dolaylı ve gizli düzen kurma — dolaylı düzen ve tuzak · gizli ve aldatıcı düzen · birine tuzak kurmak · karşılıklı tuzak kurma yarışı · onlara kötülük etmeye kesin karar vermek · cezaya götüren süre tanıma ve erteleme
  يسمون المكر كيدا (maqayis)؛ الكيد من المكيدة وقد كاده يكيده مكيدة (ayn)؛ الكيد المكر وكاده يكيده كيدا ومكيدة وكذلك المكايدة (sihah)؛ الكيد ضرب من الاحتيال وقد يكون مذموما وممدوحا والاستدراج والمكر (mufradat)؛ لأريدن بها سوءا (mufradat)؛ الإملاء والإمهال المؤدي إلى العقاب (mufradat)
- **B003** can çekişerek can verme [kalıp] — can çekişmek ve canını vermek üzere olmak
  هو يكيد بنفسه أي يجود بها (maqayis;sihah;mufradat)؛ رأيته يكيد بنفسه أي يسوق سياقا (ayn)
- **B004** karşılaşılmayan savaş [kalıp] — savaşla karşılaşmamak
  الكيد الحرب يقال خرجوا ولم يلقوا كيدا أي حربا (maqayis)؛ ربما سمي الحرب كيدا يقال غزا فلان فلم يلق كيدا (sihah)
- **B005** karganın var gücüyle bağırması — karganın var gücüyle bağırması
  صياح الغراب بجهد (maqayis)؛ يسمى اجتهاد العرب في صياحه كيدا (sihah)
- **B006** ateşi yavaş ve güçlükle çıkarma [kalıp] — çakmak taşının ateşi yavaşça ve güçlükle çıkarması
  أن يخرج الزند النار ببطء وشدة (maqayis)؛ كاد الزند إذا تباطأ بإخراج ناره (mufradat)
- **B007** kusma ve kusmuk — kusma veya kusmuk
  الكيد القيء (maqayis)؛ وكذلك القيء (sihah)
- **B008** aybaşı görme için seyrek bir ad — kimi zaman aybaşı görme anlamında kullanılan ad
  ربما سموا الحيض كيدا (maqayis)

## م ت ن (root_001396): 68:45 مَتِينٌ

- **B001** uzunlamasına sağlamlık ve güç — sert ve dayanıklı adam · sağlam, güçlü ve sert · sağlamlık, güç ve dayanıklılık
  أصل صحيح واحد يدل على صلابة في الشيء مع امتداد وطول (maqayis)؛ كل صلب شديد فهو متين والاسم المتانة (jamhara)؛ متن الشيء متانة فهو متين أي صلب (sihah)؛ المتين من كل شيء القوي وقد متن متانة (tahdhib)؛ قوي متنه فصار متينا ومنه حبل متين (mufradat)
- **B002** sert yükselti ya da belirgin dış bölüm — sert ve yükselmiş arazi kesimi · bir şeyin görünen bölümü · kılıcın ortasındaki sırt · su tulumunun dışa çıkık yüzü · okun tüylerin altından ortasına kadarki gövde bölümü · yüksek arazi yanları
  المتن ما صلب من الأرض وارتفع وانقاد (maqayis)؛ الغلظ من الأرض والجمع متان (jamhara)؛ المتن من الأرض ما صلب وارتفع ومتن السهم ما دون الريش منه إلى وسطه (sihah)؛ متن كل شيء ما ظهر منه ومتن السيف عيره ومتن المزادة وجهها البارز (tahdhib)؛ به شبه المتن من الأرض (mufradat)
- **B003** omurganın iki yanındaki etli sırt bölümleri — omurganın iki yanındaki sinirli ve etli sırt bölümleri · omurga yanındaki etli sırt bölümü · omurgayı iki yandan kuşatan etli sırt bölümleri
  المتنان من الإنسان مكتنفا الصلب من عصب ولحم (maqayis)؛ متن الظهر من الناس والدواب والجمع متون (jamhara)؛ متنا الظهر مكتنفا الصلب عن يمين وشمال من عصب ولحم (sihah)؛ المتن والمتنة لغتان وهما متنان لحمتان معصوبتان بينهما صلب الظهر (tahdhib)؛ المتنان مكتنفا الصلب (mufradat)
- **B004** sırtına vurmak — adamın sırtına vurmak veya sırtını kamçılamak
  متنته ضربت متنه (maqayis)؛ متنت الرجل متنا ضربت متنه (sihah)؛ متنت الرجل متنا إذا ضربت متنه بالسوط (tahdhib)؛ متنته ضربت متنه (mufradat)
- **B005** uzatmak; bütün gün ya da uzağa yol almak — uzatmak · onu bütün gün boyunca götürmek · bütün günü yolda geçirmek · uzak ve zorlu yolculuk
  متن يومه ساره أجمع (maqayis)؛ المماتنة المباعدة في الغاية وسار سيرا مماتنا شديدا بعيدا (maqayis)؛ متن به متنا سار به يومه أجمع (sihah)؛ متنه متنا إذا مده ومتن به متنا إذا مضى به يومه أجمع (tahdhib)؛ المماتنة المباعدة في الغاية يقال سار سيرا مماتنا أي بعيدا (tahdhib)
- **B006** bir yerde kalıp oturmak — bir yerde kalıp oturmak
  متن الرجل بالمكان متونا إذا أقام به (jamhara)
- **B007** oyalama ya da karşılıklı karşılık verme — oyalayıp geciktirmek · tartışma veya çekişmede ona karşı çıkmak · onun yaptığı gibi yapmak · iki şairin sırayla birer dizeyle karşılık vermesi
  ماتنه ماطله (maqayis)؛ مماتنة الشاعرين إذا قال هذا بيتا وذلك بيتا (maqayis)؛ ماتنت الرجل مماتنة ومتانا إذا فعلت كما يفعل (jamhara)؛ ماتنه أي ماطله (sihah)؛ ماتن فلان فلانا إذا عارضه في جدل أو خصومة (tahdhib)
- **B008** bağlayıp gererek sağlamlaştırma — yayı hayvan kirişiyle gerip sağlamlaştırmak · su tulumunu bağla sıkıp onarmak · çadırı ve büyük çadırı geren ipler · gölgelik ve çadırları iplerle gerip bağlama · çadır dokumasının şeritleri arasına kıldan bağ şeridi koymak
  متن قوسه وترها بعقب (maqayis)؛ التماتين الخيوط التي يضرب بها الفسطاط والخيمة (jamhara)؛ تمتين القوس بالعقب والسقاء بالرب شده وإصلاحه بذلك (sihah)؛ التمتين تضريب المظال والفساطيط بالخيوط (tahdhib)؛ متنوا بيتهم تمتينا أن يجعلوا بين الطرائق متنا من شعر (tahdhib)
- **B009** erbezlerini çıkarma ya da ezip gevşetme — hayvanın erbezi torbasını yarıp erbezini çıkarmak · koçun erbezi torbasını yarıp erbezini damarlarıyla çıkarmak · erbezi torbasını yarıp iki erbezini damarlarıyla çıkarmak · koçun erbezlerini gevşeyinceye kadar ezmek
  ومما شذ عن الباب متنت الدابة شققت صفنه واستخرجت بيضته (maqayis)؛ متنت الكبش شققت صفنه واستخرجت بيضته بعروقها (sihah)؛ إذا شققت الصفن وأخرجتهما بعروقهما فذلك المتن (tahdhib)؛ المتن أن يرض خصيا الكبش حتى تسترخيا (tahdhib)
- **B010** yarışta öne geçme payı verip yetişme — yarışta rakibe önden başlama payı verip sonra yetişme · rakibe belirli bir mesafe kadar öne geçme payı verip sonra yetişmek
  التمتين أن تقول لمن سابقك تقدمني إلى موضع كذا وكذا ثم ألحقك (tahdhib)؛ متن فلان لفلان كذا وكذا ذراعا ثم لحقه (tahdhib)

## غ ر م (root_001081): 68:46 مَّغْرَمٍ

- **B001** kusursuz doğan zorunlu mali yük ve ödeme — kusursuz doğan zorunlu mali yük veya bunun ödenmesi · mali yük altına girdi ve gereken tutarı ödedi · birini mali yükümlülük altına sokma · ödenmesi gereken mali yük · ödenmesi zorunlu tutar · birini mali yükümlülük altına soktu veya kendisi böyle bir yük altına girdi
  غرم المال من هذا أيضا سمي لأنه مال الغريم (maqayis)؛ الغرم أداء شيء لزم من قبل كفالة أو لزوم نائبة في ماله من غير جناية (ayn)؛ الغرامة ما يلزم أداؤه وكذلك المغرم (sihah)؛ الغرم ما ينوب الإنسان في ماله من ضرر لغير جناية منه أو خيانة (mufradat)
- **B002** borç ilişkisine bağlı alacaklı ya da borçlu — borç ilişkisindeki alacaklı ya da borçlu · borç veya mali yük altındaki kişi · borç ya da mali yükümlülük altındaki kişi
  الغريم سمي غريما للزومه وألحاحه (maqayis)؛ الغريم الملزوم ذلك والغريمان سواء الغارم والمغرم (ayn)؛ الغريم الذي عليه الدين وقد يكون الغريم أيضا الذي له الدين (sihah)؛ الغريم يقال لمن له الدين ولمن عليه الدين (mufradat)
- **B003** yakayı bırakmayan ağır sıkıntı ve yıkım — yakayı bırakmayan ağır sıkıntı, sürekli kötülük veya yıkım
  الغرام العذاب اللازم (maqayis)؛ الغرام العذاب أو العشق أو الشر وحب غرام أي لازم (ayn)؛ الغرام الشر الدائم والعذاب أي هلاكا ولزاما لهم (sihah)؛ الغرام ما ينوب الإنسان من شدة ومصيبة (mufradat)
- **B004** yakayı bırakmayan tutku ve yoğun düşkünlük — yakayı bırakmayan tutku ve yoğun düşkünlük · kalıcı, kişiyi bırakmayan sevgi · sevgiye tutkuyla bağlanmış · bir şeye tutulup ondan kopamaz oldu · kadınlara tutkuyla bağlanmış ve onlardan kopamayan
  الغرام العذاب أو العشق أو الشر وحب غرام أي لازم (ayn)؛ رجل مغرم بالحب والغرام الولوع وقد أغرم بالشئ أي أولع به (sihah)؛ هو مغرم بالنساء أي يلازمهن ملازمة الغريم (mufradat)

## ث ق ل (root_000202): 68:46 مُّثْقَلُونَ

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

## غ ي ب (root_001117): 68:47 ٱلْغَيْبُ

- **B001** gözden, duyudan ya da bilgiden uzak kalma — gözden, duyudan veya bilgiden saklı olan · gözden kaybolmak veya bulunduğu yerden uzaklaşmak · hazır bulunmayan, uzakta olan · muhatabın hazır bulunmadığı iletişim · yokluk, hazır bulunmama
  أصل صحيح يدل على تستر الشيء عن العيون؛ الغيب ما غاب مما لا يعلمه إلا الله؛ الغيبة من الغيبوبة؛ الغيب كل ما استتر عنك؛ الغيب كل ما غاب عنك؛ غابت الشمس أي غربت؛ المغايبة خلاف المخاطبة؛ ما غاب عن العيون؛ مصدر غابت الشمس وغيرها إذا استترت عن العين؛ كل غائب عن الحاسة وعما يغيب عن علم الإنسان
- **B002** içine gireni gizleyen çukur yer — içine gireni gizleyen çukur veya dip yer · kuyunun dibi · çukur arazi
  وقعنا في غيبة وغيابة أي هبطة من الأرض يغاب فيها؛ الغيابة الموضع الذي يستتر فيه؛ غيابة الجب قعره؛ غيابة الوادي؛ الغيب المطمئن من الأرض؛ الغيابة منهبط من الأرض
- **B003** içine gireni örten sık koruluk — sık koruluk, yoğun ağaçlık · koruluklar, sık ağaçlıklar
  الغابة الأجمة؛ سميت لأنه يغاب فيها؛ الغاب الآجام؛ ومنه الغابة للأجمة
- **B004** kişiyi yokluğunda iyi ya da kötü anma — kişinin arkasından kötü konuşma · birinin arkasından kötü konuşmak, kusurunu söylemek · hakkında konuşulan kişinin yokluğunda, arkasından · birini yokluğunda iyi ya da kötü anmak
  الغيبة الوقيعة في الناس؛ الغيبة من الاغتياب؛ اغتابه اغتيابا إذا وقع فيه؛ يتكلم خلف إنسان مستور بما يغمه لو سمعه؛ لا يتناول رجلا بظهر الغيب بما يسوءه مما هو فيه؛ غاب إذا ذكر إنسانا بخير أو شر؛ الغيبة فعلة منه تكون حسنة وقبيحة؛ يذكر الإنسان غيره بما فيه من عيب
- **B005** kocası uzakta olan kadın ve yokluğunda bağlılığı koruma — kadının kocasının yanında bulunmaması · kocası yanında bulunmayan kadın · eşlerinin yokluğunda korunması gerekeni gözeten kadınlar
  أغابت المرأة فهي مغيبة إذا غاب بعلها؛ إذا غاب زوجها؛ أغابت المرأة إذا غاب عنها زوجها فهي مغيبة؛ امرأة مغيبة ومغيب إذا غاب زوجها؛ حافظات للغيب أي لا يفعلن في غيبة الزوج ما يكرهه الزوج
- **B006** kuşku — kuşku, şüphe
  الغيب الشك
- **B007** koyunun işkembe ve bağırsaklarını örten ince yağ — koyunun işkembe ve bağırsaklarını örten ince yağ
  الغيب شحم ثرب الشاة
- **B008** toprağa saklanmış ağaç kökleri [kalıp] — ağacın toprağa saklanmış kökleri
  بدا غيبان الشجرة وهي عروقها التي تغيبت في الأرض فحفرت عنها حتى ظهرت
- **B009** ölüyü mezara gömme — ölüyü mezarına gömmek
  غيبه غيابه أي دفن في قبره

## ص ب ر (root_000840): 68:48 فَٱصْبِرْ

- **B001** kendini tutarak dayanma — kendini tutarak dayanma · kendimi o işte tuttum · kendini zorlayarak dayanma · çaba göstererek dayan · dayanma gücü yüksek kişi · her defasında çabayla dayanan kişi
  الصبر نقيض الجزع (ayn;jamhara;tahdhib)؛ الصبر حبس النفس عن الجزع (sihah)؛ صبرت نفسي أي حبستها (maqayis;tahdhib)؛ حبس النفس على ما يقتضيه العقل والشرع (mufradat)
- **B002** zorla alıkoyma — onu zorla alıkoydu · öldürülmek üzere bağlı tutma · ölümü beklemek üzere alıkonmuş canlı · yetkili önünde zorla ettirilen ant · ona bütün gücüyle ant içirdi
  المصبورة المحبوسة على الموت (maqayis;sihah)؛ الصبر نصب الإنسان للقتل (ayn;tahdhib)؛ صبرت يمينه أي حلفته (ayn;maqayis;tahdhib)؛ قتل صبر ويمين صبر (sihah;tahdhib)؛ الصبر الإكراه (tahdhib)
- **B003** yükümlülüğe güvence veren kişi — yükümlülüğe güvence veren kişi · onun yükümlülüğüne güvence verdim · bana bir güvence veren kişi bul · topluluğun işlerinde yanında duran kişi
  الصبير هو الكفيل (maqayis;sihah)؛ صبرت بفلان إذا كفلت به فأنا به صبير (tahdhib)؛ صبير القوم الذي يصبر لهم ويكون معهم في أمورهم (ayn)
- **B004** üst ya da yan sınır — şeyin üstü ya da yanı · kabın çevre yanları · mezarın çevre yanları · üst ya da yan sınırına kadar · bahçenin en üst bölümü
  صبر كل شيء أعلاه (maqayis;ayn;tahdhib)؛ أصبار الإناء نواحيه (maqayis;ayn;sihah)؛ أصبار القبر نواحيه (ayn;tahdhib)؛ الصبر جانب الشيء (tahdhib)
- **B005** sert taş ve taşlı arazi — sert ve kalın taş · sert ve düz taşlar · taşlar ya da kaba yüksekçe arazi · çok engebeli olmayan çakıllı yer · katı kaya yüzeyi ya da taşlık alan
  الصبرة من الحجارة ما اشتد وغلظ (maqayis;ayn;tahdhib)؛ الصبارة الحجارة (sihah;tahdhib)؛ الصبر الأرض التي فيها حصباء (maqayis;sihah;tahdhib)؛ أم صبار الحرة أو الصفاة (maqayis;sihah;tahdhib)
- **B006** çıkışsız ağır durum — savaş ya da ağır yıkım · çıkış yolu olmayan büyük sıkıntı
  وقع القوم في أم صبور إذا وقعوا في أمر عظيم (maqayis)؛ أم صبار الحرب والداهية الشديدة (ayn)؛ وقع القوم في أم صبور أي في أمر شديد (sihah)؛ أم صبور أمر لا منفذ له عنه (tahdhib)
- **B007** kışın ayazı — kışın şiddetli soğuğu
  صبارة الشتاء شدة برده (sihah)؛ أتيته في صبارة الشتاء أي في شدة البرد (tahdhib)
- **B008** acı ağaç özü — acı ağaç özü ve bundan yapılan ilaç
  الصبر بكسر الباء عصارة شجرة (ayn;tahdhib)؛ الصبر هذا الدواء المر (sihah)
- **B009** demirhindi meyvesi — demirhindi meyvesi
  الصبار حمل شجرة طعمه أشد حموضة من المصل (ayn;tahdhib)؛ الصبار التمر الهندي (tahdhib)
- **B010** katmanlı beyaz bulut — üst üste yığılmış beyaz bulut · yoğun bulutun üstündeki düz bulut · beyaz bulutlar
  الصبر سحاب مستو فوق السحاب الكثيف (ayn)؛ الصبير السحاب الأبيض (sihah;tahdhib)؛ السحاب الأبيض الذي يصبر بعضه فوق بعض درجا (sihah;tahdhib)؛ الاصبار السحائب البيض (sihah)
- **B011** sofra yaygısı ya da yiyecek yığını — yiyeceğin altına serilen geniş ince yaygı · üst üste konmuş yiyecek yığını · malı tartmadan ya da ölçmeden topluca aldım · düğün yemeğinin üstüne konduğu ince yaygı
  صبير الخوان رقاقته العريضة تبسط تحت ما يؤكل من الطعام (ayn;tahdhib)؛ الصبرة من الطعام بعضه فوق بعض (ayn;tahdhib)؛ اشتريت الشيء صبرة أي بلا وزن ولا كيل (sihah)
- **B012** öldürmeye karşılık ölüm cezası — öldürmeye karşılık ölüm cezası istesin · yetkili onu önceki öldürmeye karşılık öldürdü
  فليصطبر معناه فليقتص (tahdhib)؛ أقاد السلطان فلانا وأقصه وأصبره بمعنى واحد إذا قتله بقود (tahdhib)
- **B013** ateşe götüren işlerde pervasızlık — ateşi hak edecek işleri yapmaya ne kadar da gözü pekler
  الصبر الجرأة ومنه فما أصبرهم على النار (tahdhib)؛ لغة بمعنى الجرأة (mufradat)؛ ما أعملهم بعمل أهل النار (mufradat)
- **B014** kendini tutarak bekleme — kendini tutarak bekleme · yöneticinin hükmünün gerçekleşmesini bekle
  يعبر عن الانتظار بالصبر لما كان حق الانتظار أن لا ينفك عن الصبر (mufradat)؛ فاصبر لحكم ربك أي انتظر حكمه (mufradat)
- **B015** kendini tutma türü olarak oruç — oruç, kendini tutmanın bir türüdür · oruç ayı
  سمي الصوم صبرا لكونه كالنوع له (mufradat)؛ صيام شهر الصبر (mufradat)
- **B016** bir Arap boyunun adı — belirli bir Arap topluluğuna bağlı boyun adı
  الصبر أيضا بطن من غسان (sihah)
- **B017** dağ ya da dağların orta kesimi — dağ · dağların orta kesimi
  الصبير الأقدر وهو الوسط من الجبال (tahdhib)؛ الصبير الجبل (tahdhib)
- **B018** şişe tıkacı ve tıkama — şişe tıkacı ya da kapakçığı · kabın ağzını tıkaçla kapattı
  أصبر سد رأس الحوجلة بالصبار وهو السداد (tahdhib)؛ الصبار صمام القارورة (tahdhib)

## ح و ت (root_000366): 68:48 ٱلْحُوتِ

- **B001** balık, özellikle iri balık — balık; özellikle iri balık · balıklar; özellikle iri balıklar · balıklar; özellikle iri balıklar
  الحوت العظيم من السمك (maqayis); الحوت معروف والجميع الحيتان وهو السمك (ayn); الحوت معروف وهو ما عظم من السمك والجمع حيتان وأحوات (jamhara); الحوت السمكة والجمع الحيتان (sihah); الحوت معروف وجمعه الحيتان وهو السمك (tahdhib); وهو السمك العظيم (mufradat)
- **B002** kıvrak manevrayla atlatma — biri beni kıvrak manevralarla atlattı · kıvrak manevrayla atlatma · beni kıvrak manevralarla atlatıyor
  حاوتني فلان إذا راوغني (maqayis); حاوتني فلان إذا راوغك (sihah); المحاوتة المراوغة يقال هو يحاوتني يراوغني (tahdhib); حاوتني فلان أي راوغني مراوغة الحوت (mufradat)
- **B003** bir şeyin çevresinde dönüp dolanma — suyun veya bir şeyin çevresinde dönüp dolanma · kuşun bir şeyin çevresinde dönmesi
  الحوت والحوتان حومان الطائر حول الماء وحومان الوحشية حول شيء (ayn); حات الطائر على الشئ يحوت أي حام حوله (sihah); الحوت والحوتان حومان الطائر حول الماء وحومان الوحشية حول شيء (tahdhib)
- **B004** Balık burcu — Balık burcu
  الحوت برج من الاثني عشر وهو آخرها (ayn); الحوت برج في السماء (sihah)
- **B005** küçük bir Arap kabile kolunun adı — Araplar arasındaki küçük bir kabile kolu
  بنو حوت بطين من العرب (jamhara)
- **B006** çok kınayan kişi — çok kınayan kişi
  الحائت الكثير العذل (tahdhib)

## ك ظ م (root_001303): 68:48 مَكْظُومٌ

- **B001** öfkeyi içine atıp dışa vurmama — öfkeyi içine gömüp dışa vurmama · öfkesini içine atıp belli etmemek · öfkelerini içlerine atıp belli etmeyenler
  الكظم اجتراع الغيظ والإمساك عن إبدائه (maqayis)؛ كظم الرجل غيظه اجترعه (ayn)؛ كظم غيظه كظما اجترعه (sihah)؛ كظمت الغيظ إذا أمسكت على ما في نفسك منه (tahdhib)؛ كظم الغيظ حبسه (mufradat)
- **B002** soluk çıkışı ve soluğun tutulup daralması — soluğu tutulduğu için sessiz kalma · sessiz duran topluluk · soluğunu içinde tutmak · soluk çıkış yolu · soluk yolunu sıkıp nefes alamaz hâle getirmek · soluğu daralmış, bunalmış · soluğu tutulmuş, sıkıntıya düşmüş
  الكظوم السكوت (maqayis)؛ الكظم مخرج النفس (maqayis;ayn;tahdhib;mufradat)؛ أخذ بكظمه فما يقدر أن يتنفس (ayn)؛ الكظوم احتباس النفس (mufradat)؛ كظم فلان حبس نفسه (mufradat)؛ قوم كظم أي ساكتون (sihah)
- **B003** devenin geviş lokmasını yutup gevişi kesmesi — devenin geviş lokmasını yutup gevişi kesmesi · geviş getirmeyi kesmiş deve · geviş getirmeyen dişi deve ya da develer
  الكظوم إمساك البعير عن الجرة (maqayis)؛ كظم البعير جرته إذا ازدردها وكف عنها (ayn;mufradat)؛ إذا أمسك عن الجرة فهو كاظم (sihah)؛ كظم البعير إذا لم يجتر (tahdhib)
- **B004** açıklığı kapatıp geçişi kesme — kapının kapatılması · kanalı tıkayıp akış yolunu kapatmak · dolu tulumun ağzını sıkıca bağlamak
  كظمت القناة سددتها (ayn)؛ الكظيم غلق الباب (sihah)؛ كظم السقاء شده بعد ملئه مانعا لنفسه (mufradat)
- **B005** kuyular ve aralarındaki su iletim yolu — yan yana kuyular ve aralarındaki su geçidi · kuyular arasında suyun aktığı kazılmış geçitlerden biri · kuyular arasında su taşıyan kazılmış geçitler
  الكظائم خروق تحفر يجرى فيها الماء من بئر إلى بئر (maqayis)؛ الكظيمة واحدة الكظائم وهي خروق تحفر فيجري فيها الماء (ayn)؛ الكظامة بئر إلى جنبها بئر وبينهما مجرى (sihah)؛ آبار تحفر ويخرق ما بين كل بئرين بقناة تؤدي الماء (tahdhib)؛ الكظائم خروق بين البئرين يجري فيها الماء (mufradat)
- **B006** uçları bir arada tutan bağlayıcı parça — terazi demirinin ucundaki ipleri toplayan halka · yayın üst ucunu kirişe bağlayan kayış · devenin burnunu bağlamaya yarayan ip · ok tüylerinin başlarını tutan sinir bağ
  الكظامة الحلقة التي تجمع خيوط حديدة الميزان (maqayis;sihah;mufradat)؛ الكظامة سير يوصل بوتر القوس العربية (maqayis;ayn;mufradat)؛ حبلا يكظم به خطم البعير (ayn)؛ الكظامة العقب الذي على رؤوس القذذ (sihah;tahdhib)
- **B007** deniz canlısınca yutulup içinde kapalı kalan kişi — büyük bir deniz canlısınca yutulup içinde kapalı kalan kişi
  المكظوم الذي يلتقمه الحوت (ayn)؛ كظم فلان حبس نفسه (mufradat)
- **B008** çölde ya da kıyıda bulunan belirli bir yer adı — çölde ya da deniz kıyısında bulunan belirli bir yer adı
  كاظمة موضع بالبادية (ayn)؛ كاظمة موضع (sihah)؛ كاظمة جو على سيف البحر وفيها ركايا كثيرة (tahdhib)
- **B009** işin güvenilir dayanağına tutunma [kalıp] — işin güvenilir dayanağına tutunup onu esas almak
  أخذت بكظام الأمر أي بالثقة (tahdhib)

## د ر ك (root_000471): 68:49 تَدَٰرَكَهُۥ

- **B001** yetişip erişme — yetişmek, ulaşmak ve erişmek · yetişme, ulaşma ve erişme · istenene yetişme ve onu elde etme · gözüyle görüp bütünüyle algılamak · bilgisiyle kuşatıp kavramak · çocuğun erginleşmesi, meyvenin olgunlaşması · birbirine yetişip art arda gelmek · yağmur ıslaklığı ile toprak ıslaklığının birbirine ulaşması · kaçırılanı sonradan yetişip tamamlamak · bir iyiliğin yetişip yardım veya kurtuluş sağlaması · art arda yetişme ve sık sık erişme · yetiş! · iki hareketli birimden sonra bir durgun birimin geldiği ölçü örüntüsü · erginliğe ulaşmış olanlar · yakalanmaktan veya doğacak sorumluluktan korkmamak
  لحوق الشيء بالشيء ووصوله إليه (maqayis)؛ الإدراك اللحوق (sihah)؛ الدرك إدراك الحاجة والطلبة (ayn;tahdhib)؛ أدرك بلغ أقصى الشيء (mufradat)؛ تدارك القوم لحق آخرهم أولهم (maqayis;sihah)؛ لا تدركه الأبصار وهو يدرك الأبصار (mufradat)
- **B002** en dip katman — bir şeyin en aşağı dibi · kuyunun suya ulaşılan dibi · azap yerinin aşağı katları · azap yerinin en aşağı katı
  الدرك أسفل قعر الشيء (ayn)؛ قعرها الذي أدرك فيه الماء (tahdhib)؛ أقصى قعر الشيء (tahdhib)؛ دركات النار منازل أهلها (sihah)؛ الدرك كالدرج لكن الدرج يقال اعتبارا بالصعود والدرك اعتبارا بالحدور (mufradat)؛ منازل أهل النار (maqayis)
- **B003** bağlantı ipi ya da kiriş halkası — ipin ucuna bağlanan kısa bağlantı ve uzatma parçası · yay kirişinin çentiğe oturan halkası
  الدرك القطعة من الحبل تشد في طرف الرشاء إلى عرقوة الدلو (maqayis)؛ الدرك حبل من ليف يعقد على عراقي الدلو (ayn)؛ قطعة حبل تشد في طرف الرشاء (sihah)؛ حبل يوثق في طرف الحبل الكبير (tahdhib)؛ الحبل الذي يوصل به حبل آخر ليدرك الماء (mufradat)؛ الدركة حلقة الوتر (ayn;tahdhib)
- **B004** sonradan doğan sorumluluk ve karşılama güvencesi — sonradan doğan sorumluluk ve güvence yükü · satıştaki sorumluluğu karşılama güvencesi · yakalanmaktan veya doğacak sonuçtan korkmamak
  الدرك اللحق من التبعة (ayn;tahdhib)؛ ما لحقك من درك فعلى خلاصه (sihah)؛ ضمان الدرك في عهدة البيع (tahdhib)؛ لما يلحق الإنسان من تبعة درك كالدرك في البيع (mufradat)

## ن ب ذ (root_001466): 68:49 لَنُبِذَ

- **B001** elden atma veya değersiz sayıp bir yana bırakma — bir şeyi elinden atmak veya önemsemeyip bir yana bırakmak · bir şeyi tekrar tekrar ya da çokça atmak
  أصل صحيح يدل على طرح وإلقاء (maqayis)؛ نبذت الشيء أنبذه نبذا إذا ألقيته من يدك (jamhara;sihah)؛ النبذ طرحك الشيء من يدك أمامك أو خلفك (tahdhib)؛ النبذ إلقاء الشيء وطرحه لقلة الاعتداد به (mufradat)
- **B002** ilişkiyi açıkça kesip karşı tarafa çatışmayı bildirme — birinden düşmanlıkla ayrılıp karşısına açıkça çıkmak · anlaşmanın bittiğini eşit bilgi koşulunda bildirip çatışmaya dönmek
  نابذ فلان فلانا إذا فارقه عن قلى (jamhara)؛ نابذه الحرب كاشفه (sihah)؛ نابذناهم الحرب ونبذنا إليهم الحرب على سواء (tahdhib)؛ فانبذ إليهم على سواء فمعناه ألق إليهم السلم (mufradat)
- **B003** atma işaretinin satışı kesinleştirdiği satış biçimi [kalıp] — kumaş, mal veya taş atılınca bağlayıcı hale gelen satış
  المنابذة أن يقول الرجل لصاحبه انبذ إلي الثوب أو غيره من المتاع أو أنبذه إليك وقد وجب البيع؛ إذا نبذت الحصاة إليك فقد وجب البيع
- **B004** bir yana çekilme veya kenarda bulunma — bir yana gitmek veya kenara çekilmek · yan tarafta oturulan yer veya kenar
  جلس فلان نبذة ونبذة أي ناحية (sihah;tahdhib)؛ انتبذ فلان أي ذهب ناحية (sihah)؛ انتبذ فلان ناحية إذا انتحى ناحية (tahdhib)
- **B005** az miktar veya küçük parça — az miktarda mal, otlak veya küçük bir topluluk · biraz saç ağarması veya az yağmur · güzel kokulu bir maddeden küçük parça
  نبذ من مال أي شيء يسير (maqayis)؛ نبذ من الشيب أي يسير (maqayis)؛ نبذ من بني فلان أي فرق يسيرة (jamhara)؛ نبذ من مطر أي قليل (jamhara)؛ نبذ من مال ومن كلأ وفي رأسه نبذ من شيب وأصاب الأرض نبذ من مطر أي شيء يسير (sihah)؛ نبذة قسط وأظفار يعني قطعة منه (tahdhib)؛ في هذا العذق نبذ قليل من الرطب (tahdhib)
- **B006** hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek — hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek · hurma veya kuru üzümü suya koyarak içecek hazırlamak
  النبيذ التمر يلقى في الآنية ويصب عليه الماء (maqayis)؛ سمي النبيذ لأن التمر كان يلقى في الجر وفي غيره (jamhara)؛ النبيذ واحد الأنبذة يقال نبذت نبيذا أي اتخذته (sihah)؛ يأخذ تمرا أو زبيبا فينبذه أي يلقيه في وعاء أو سقاء ويصب عليه الماء (tahdhib)
- **B007** annesi tarafından bırakılıp başkalarınca bulunan çocuk — annesi tarafından bırakılıp başkalarınca bulunan çocuk
  الصبي المنبوذ الذي تلقيه أمه (maqayis;jamhara)؛ المنبوذ الصبي تلقيه أمه في الطريق (sihah)؛ المنبوذ الولد الذي تنبذه والدته حين تلده فيلتقطه الرجل أو جماعة من المسلمين (tahdhib)
- **B008** oturmak için yere atılan yastık — oturmak için yere atılıp konan yastık
  المنبذة الوسادة (sihah;tahdhib)؛ المنبذة الوسادة سميت منبذة لأنها تنبذ بالأرض أي تطرح للجلوس عليها (tahdhib)
- **B009** özel adlandırma kümesi — sahiplerinin ihmal ettiği cılız koyun · çukurdan çıkarak çevreye saçılan toprak
  يقال للشاة المهزولة التي يهملها أهلها نبيذة؛ لما ينبث من تراب الحفرة نبيثة ونبيذة وجمعها النبائت والنبائذ

## ع ر ي (root_001005): 68:49 بِٱلْعَرَآءِ

- **B001** bir durumun kişiyi kuşatıp etkilemesi — bir olayın onu kuşatıp etkilemesi · bir kötülüğün ya da akıl sağlığını bozan bir hâlin ona musallat olması · kaygının onu sarıp etkisi altına alması
  عراه أمر يعروه عروا إذا غشيه وأصابه (ayn;tahdhib)؛ عراني هذا الأمر واعتراني إذا غشيك (sihah)؛ مسك بعض أصنامنا بجنون (tahdhib)
- **B002** birine yönelip varmak — bir ihtiyacını istemek için ona uğramak · bir ihtiyacını istemek üzere yanına gitmek · misafirlerin onun yanına gelip konaklaması · onun bulunduğu yana yönelmek
  عروت الرجل أعروه عروا إذا ألممت به وأتيته طالبا (sihah)؛ إذا أتيت رجلا تطلب منه حاجة قلت عروته وعررته واعتريته واعتررته (tahdhib)؛ فلان تعروه الأضياف وتعتريه (sihah)؛ عراه واعتراه قصد عراه (mufradat)
- **B003** fiziksel örtüden yoksun ve açıkta olma — giysisiz kalıp çıplak olmak · çıplak, örtüsüz · giysisiz kalmamak · eyersiz at · ata eyersiz binmek · insanın açılabilen ve görünür olabilen organları · üzerinde ağaç bulunmayan kumluk · tehlikeyi en çarpıcı biçimde haber veren uyarıcı
  عري فلان عريا فهو عريان والمرأة عريانة ورجل عار (ayn;sihah;tahdhib;mufradat)؛ فرس عري ليس على ظهره شيء وأفراس أعراء (ayn;sihah;tahdhib)؛ معاري الإنسان الأعضاء التي من شأنها أن تعرى (mufradat;tahdhib)؛ العريان من الرمل ما ليس عليه شجر (ayn;tahdhib)
- **B004** sipersiz açık alan — siper bulunmayan açık yer · örtüsüz ve boş bir açık alanda · avlu, saha veya yön · yeryüzünün açıkta görünen yüzleri
  العراء الأرض الفضاء التي لا يستتر فيها بشيء (ayn)؛ العراء بالمد الفضاء لا ستر به (sihah)؛ العراء وجه الأرض الخالي والمكان الخالي (tahdhib)؛ العراء مكان لا سترة به (mufradat)؛ العرا الفناء والساحة والناحية (sihah;tahdhib;mufradat)
- **B005** tutunmaya yarayan sağlam dayanak [kalıp] — giysinin iliği veya kabın tutma halkası · kopmaz ve güvenilir dayanak · kuraklıkta hayvanların tutunduğu kökü kalıcı bitki · su tulumunun bağlama kulakları · güçsüzlerin sığınıp korunduğu önderler
  عروة القميص والكوز معروفة (sihah)؛ العروة ما يتعلق به من عراه (mufradat)؛ العروة من الشجر الذي لا يزال باقيا في الأرض (sihah;tahdhib)؛ فقد استمسك بالعروة الوثقى لا انفصام لها (tahdhib;mufradat)؛ عرا المزادة آذانها وعرا سادات الناس الذين يعتصم بهم الضعفى (tahdhib)
- **B006** hurma ürününü bir yıllığına ihtiyaç sahibine ayırma — ürünü ihtiyaç sahibine ayrılmış veya satış dışında bırakılmış hurma ağacı · hurmanın bir yıllık ürününü bir kişiye ayırma · ayrılmış ağaçların taze hurmalarını yiyip çevreye dağılmak
  العرية النخلة يعريها صاحبها رجلا محتاجا فيجعل له ثمرها عاما (sihah)؛ العرايا واحدتها عرية وهي النخلة يعريها صاحبها رجلا محتاجا والإعراء أن يجعل له ثمرة عامها (tahdhib)؛ النخلة العرية ما يعرى عن البيع (mufradat)
- **B007** hastalık titremesi veya keskin hava soğuğu — ateşli hastalığın başlangıcındaki üşüme ve titreme nöbeti · soğuk rüzgâr, soğuk gece veya akşam soğuğu
  أخذته الحمى بعروائها (ayn)؛ العرواء قرة الحمى ومسها في أول ما تأخذ بالرعدة (sihah;tahdhib)؛ العرية أيضا الريح الباردة (sihah)؛ شمال عرية باردة وقد أعرينا إذا بلغنا برد العشي (tahdhib)؛ العري والعرية ما يعرو من الريح الباردة (mufradat)
- **B008** bir iş veya isnatla ilişkisiz olma — bir işten veya suçtan uzak ve ilişkisiz · bir işten sıyrılıp kurtulmak
  أنا عرو منه أي خلو (sihah)؛ هو عرو من هذا الأمر كما يقال هو خلو منه (tahdhib)؛ وهو عرو من الذنب أي عار (mufradat)؛ عريت من جملة التحريم فعريت أي خلت وخرجت منها (tahdhib)
- **B009** ilgiyi kesip kendi hâline bırakmak — arkadaşının uzaklaşıp onu desteksiz bırakması · topluluğun arkadaşını geride bırakıp gitmesi · onu ihmal edip kendi hâline bırakmak · yüksüz ve başıboş salınan deve
  أعراه صديقه إذا تباعد منه ولم ينصره (sihah)؛ أعرى القوم صاحبهم إذا تركوه في مكانه وذهبوا عنه (tahdhib)؛ لكل شيء أهملته وخليته قد عريته (tahdhib)؛ المعرى الجمل الذي يرسل سدى ولا يحمل عليه (tahdhib)
- **B010** bir şeye özlemle yönelmek [kalıp] — gönlünün ona özlemle yönelmesi · sattığı malın ardından ona özlem duymak
  عريت إلى مال لي أشد العرواء إذا بعته ثم تبعته نفسك؛ عري هواه إلى كذا أي حن إليه (tahdhib)

## ذ م م (root_000520): 68:49 مَذْمُومٌ

- **B001** ayıplayıp kınama — ayıplama ve kınama · ayıplanacak kadar kusurlu veya övülmez · kınanmış veya kusurlu bulunmuş · kınanma ve ayıplanma nedeni · sana yönelik hiçbir kınama yok · kınanmasına yol açacak bir iş yaptı · kınanacak bir davranışta bulundu · onu kusurlu ve kınanır buldu · ayıplanmaz, kusurlu bulunmaz veya suyu eksik çıkmaz
  ذممت فلانا أذمه فهو ذميم ومذموم إذا كان غير حميد (maqayis)؛ ذممت الشيء أذمه ذما والذم خلاف المدح (jamhara)؛ الذم نقيض المدح وذممته فهو ذميم (sihah)؛ ذم يذم ذما وهو اللوم في الإساءة (tahdhib)؛ ذممته أذمه ذما فهو مذموم وذميم (mufradat)
- **B002** bağlayıcı güvence ve dokunulmazlık — bağlayıcı söz, güvence ve yükümlülük · çiğnenmemesi gereken söz, hak ve dokunulmazlık · bir güvence sözleşmesiyle koruma altına alınmış topluluk · bir güvence sözleşmesiyle korunma hakkı edinmiş kişi · sütannenin gözetilmesi gereken hakkı · haklarını karşılayacak bir şey ver · benim güvencem ve sorumluluğum altında · gözetilmesi gereken hak ve dokunulmazlık · kınanmamak için hakkı çiğnemekten çekindi
  الذمام لأنه يذم على إضاعته وأهل الذمة أهل العقد والذمة الأمان (maqayis)؛ الذمة العهد والمذمة من الذمام (jamhara)؛ الذمام الحرمة وأهل الذمة أهل العقد والذمة الأمان (sihah)؛ الذمام كل حرمة تلزمك والذمة العهد والأمان والضمان (tahdhib)؛ الذمام ما يذم الرجل على إضاعته من عهد (mufradat)
- **B003** suyu az kuyu — suyu az kuyu · az suyu olan kuyu · istenmeyen veya yetersiz su · suyu az kuyular · ayıplanmaz, kusurlu bulunmaz veya suyu eksik çıkmaz
  الذمة هي البئر القليلة الماء وجمع الذمة ذمام (maqayis)؛ بئر ذمة قليلة الماء (jamhara)؛ بئر ذمة قليلة الماء وماء ذميم أي مكروه (sihah)؛ الذمة البئر القليلة الماء ولا يوجد ماؤها ناقصا (tahdhib)
- **B004** burun veya yüzde çıkan küçük kabarcık — burun veya yüzde çıkan küçük kabarcık · bu küçük kabarcıklardan biri
  الذميم بثر يخرج على الأنف (maqayis)؛ الذميم بثر يظهر في الوجه (jamhara)؛ الذميم شيء يخرج من مسام المارن كبيض النمل (sihah)؛ الذميم بثر أمثال بيض النمل تخرج على الأنف من حر والواحدة ذميمة (tahdhib)
- **B005** burun akıntısı, keçi idrarı, süt sızıntısı veya çiy — burun akıntısı, erkek keçinin idrarı, memeden sızan süt veya bitkiye düşen çiy · burnu aktı
  الذميم البول الذي يذم ويذن من قضيب التيس والنسل من اللبن (maqayis)؛ الذميم ما انتضح من أخلاف النوق من اللبن وهو ندى يسقط من السماء على الشجر (jamhara)؛ الذميم المخاط والبول وكذلك اللبن من أخلاف الشاة (sihah)؛ الذميم والذنين ما يسيل من الأنف (tahdhib)
- **B006** yorulup geride kalma ve kıpırdayamama — binek hayvanı yorulup kıpırdayamaz oldu · binekler yorulup sürünün gerisinde kaldı · devesi gecikip diğer develerden koptu · kıpırdayamayan, hareket gücü kalmamış
  أذم به بعيره إذا أخر وانقطع عن سائر الإبل ورجل مذم لا حراك به (maqayis)؛ أذمت راحلة الرجل إذا أعيت فلم يكن بها حراك (jamhara)؛ أذمت ركاب القوم أي أعيت وتأخرت عن جماعة الإبل ولم تلحق بها ورجل مذم لا حراك به (sihah)؛ أذمت ركاب القوم إذا تأخرت عن الإبل ولم تلحق بها فهي مذمة (tahdhib)
- **B007** azaltma ve verilen payı kısma — verdiği payı azalttı · azalttı, eksiltti
  ذمذم إذا قلل عطيته وذم إذا نقص (tahdhib)

## ج ب ي (root_000220): 68:50 فَٱجْتَبَٰهُ

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

## ص ل ح (root_000876): 68:50 ٱلصَّٰلِحِينَ

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

## ك و د (root_001329): 68:51 يَكَادُ

- **B001** bir şeyi biraz güçlükle aramak — bir şeyi biraz güçlükle aradı
  التماس شيء ببعض العناء؛ كاد يكود كودا ومكادا
- **B002** eyleme ramak kalmak; olumluda yapmamak, olumsuzda güçlükle yapmak — az kalsın yapacaktı, ama yapmadı · güçlükle de olsa yaptı · az kalsın yapacaktı · bir kimse az kalsın yapacaktı
  فأما قولهم في المقاربة كاد فمعناها قارب (maqayis)؛ كاد يفعل كذا يكاد كودا ومكادة أي قارب ولم يفعل (sihah)؛ مجردة فلم يقع ذلك الشيء وقرنت بجحد فقد وقع (maqayis)؛ مجرده ينبئ عن نفي الفعل ومقرونه بالجحد ينبئ عن وقوع الفعل (sihah)
- **B003** vermeyi ya da yapmayı kesin biçimde reddetmek [kalıp] — Hayır, vermeye hiç niyetim yok. · Bunu kesinlikle yapmam. · Bunu ne önemsiyorum ne de yapmaya yanaşıyorum.
  لمن يطلب منك الشيء فلا تريد إعطاءه لا ولا مكادة (maqayis)؛ لا أفعل ذلك ولا كودا (sihah)؛ لا مهمة لي ولا مكادة أي لا أهم ولا أكاد (sihah)
- **B004** istemek, niyet etmek — ondan ne istendiği · onu gizlemek istiyorum
  عرف فلان ما يكاد منه أي ما يراد منه؛ قال بعضهم في قوله أكاد أخفيها أريد أخفيها؛ كادت وكدت وتلك خير إرادة

## ك ف ر (root_001307): 68:51 كَفَرُوا۟

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

## ز ل ق (root_000640): 68:51 لَيُزْلِقُونَكَ

- **B001** kayma, kaygan yer ve kayganlaştırma — kayma veya yerinden kayma · ayağın tutunamadığı kaygan yer · kaygan ve bitkisiz düzlük · kaygan yer · onu düzleştirdi · yeri kayganlaştıracak biçimde düzleştirme
  أصل واحد يدل على تزلج الشيء عن مقامه؛ المزلقة والمزلق الموضع لا يثبت عليه (maqayis)؛ الموضع مزلق صار كالمزلقة وإن لم يكن فيه ماء (ayn)؛ مكان زلق أي دحض؛ الموضع الذي لا تثبت عليه قدم؛ أرضا ملساء ليس بها شيء (sihah)؛ التزليق تمليسك الموضع حتى يصير كالمزلقة؛ زلقا لا نبات فيه؛ لا يثبت عليه القدمان (tahdhib)؛ الزلق والزلل متقاربان؛ دحضا لا نبات فيه؛ المزلق المكان الدحض (mufradat)
- **B002** bakışla yerinden etme veya yok etme — bakışlarıyla yerinden edecek veya düşürecek gibi olmak · yok ettik
  حقيقة معناه أنه من حدة نظرهم حسدا يكادون ينحونك عن مكانك؛ نظرا يزيل موطئ الأقدام (maqayis)؛ ليرمون بك ويزيلونك عن موضعك بأبصارهم؛ يكاد يسقطك؛ يصيبونك بعيونهم (tahdhib)؛ ليزلقونك بأبصارهم؛ نظرا يزيل مواضع الأقدام؛ أزلقنا ثم الآخرين أي أهلكنا (mufradat)
- **B003** üreme sürecinde erken atma veya boşalma — gebelik ürününü erken atmak veya üreme sıvısını tutmamak · sık sık düşük yapan kısrak · erken düşmüş yavru · birleşmeden önce boşalan erkek · birleşmeden önce boşalan erkek
  أزلقت الحامل إذا أزلقت ولدها؛ إذا ألقت الماء ولم تقبله رحمها؛ الزلق الذي إذا دنا من المرأة رمى بمائه قبل أن يغشاها (maqayis)؛ الزمالق الذي إذا باشر أراق ماءه قبل أن يجامع؛ ميم زائدة لأنه من الزلق؛ من باب أزلقت الأنثى (maqayis-variant)؛ أزلقت الفرس ألقت ولدها تاما كالسقط؛ فرس مزلاق كثير الإزلاق (ayn)؛ أزلقت الناقة أسقطت؛ فرس مزلاق كثيرة الإزلاق؛ الزليق السقط؛ رجل زلق وزملق وهو الذي ينزل قبل أن يجامع (sihah)؛ ألقت الناقة ولدها قبل أن يستبين خلقه وقبل الوقت قيل أزلقت وأجهضت؛ لا يكون الإزلاق إلا قبل التمام؛ رجل زلق وزملق وهو الشكاز الذي ينزل إذا حدث المرأة من غير جماع (tahdhib)
- **B004** hayvanın sağrısı — hayvan sağrısı
  الزلق العجز منها ومن كل دابة؛ سميت بذلك لأن اليد تزلق عنها وكذلك ما يصيبها من مطر وندى (maqayis)؛ الزلق العجز من كل دابة (ayn)؛ الزلق أيضا عجز الدابة (sihah)؛ الزلق العجز من كل دابة (tahdhib)
- **B005** kapı sürgüsü — kapı sürgüsü
  المزلاق والمزلاج الذي تغلق به الباب (ayn)؛ المزلاق لغة في المزلاج الذي يغلق به الباب ويفتح بلا مفتاح (sihah)
- **B006** hızlı dişi deve [kalıp] — hızlı dişi deve
  ناقة زلوق زلوج أي سريعة (ayn)؛ ناقة زلوق زلوج أي سريعة (tahdhib)
- **B007** bedeni yağlayıp parlatma ve bakımlı biçimde ışıldama — bedeni yağlayıp parlatma · bakımla teni ışıldamak
  التزلق صبغك البدن بالأدهان ونحوها (ayn)؛ التزلق صبغك البدن بالأدهان ونحوها؛ خرجا من الحمام متزلقين؛ تزلق فلان وتزيق إذا تنعم حتى يكون للونه بصيص ولبشرته بريق (tahdhib)
- **B008** başını tıraş etmek [kalıp] — başını tıraş etmek
  زلق الرجل رأسه حلقه (maqayis)؛ زلق رأسه يزلقه زلقا حلقه وكذلك أزلقه وزلقه تزليقا (sihah)؛ الذي يحلق الرأس قد زلقه وأزلقه؛ زلق رأسه وأزلقه وزلقه إذا حلقه ثلاث لغات (tahdhib)
- **B009** pürüzsüz şeftali çeşidi — pürüzsüz şeftali çeşidi
  الزليق بالضم والتشديد ضرب من الخوخ أملس (sihah)
- **B010** türü açıklanmayan özel yapı adı — türü açıklanmayan özel yapı adı
  يقال للمصنعة زلقة وزلفة بالقاف والفاء (tahdhib)

## س م ع (root_000741): 68:51 سَمِعُوا۟

- **B001** duymak ve dikkatle dinlemek — sesi kulakla algılamak · işitme gücü veya duyma eylemi · duyma eylemi veya duyulan şey · dikkatle dinlemek · duymaya çalışarak kulak vermek · beni dinle ve söylediklerime kulak ver · dinle · söylenenleri çokça dinleyen kimse · işiten kimse · kendi kulağımla duydum; görmeyle ilgili aktarılmış yorum kaynakta reddedilir
  إيناس الشيء بالأذن (maqayis)؛ سمعت الشيء سمعا (maqayis;sihah;mufradat)؛ الاستماع الإصغاء (sihah;mufradat)؛ سماع أي اسمع (maqayis;sihah)؛ السمع سمع الإنسان وغيره (tahdhib)
- **B002** kulak ve kulak açıklığı — kulak veya işitme yeri · kulak veya kulak açıklığı · kulak açıklığı veya işitme yeri · kulak · iki kulak veya iki işitme yeri
  السمع الأذن وهي المسمعة (ayn;tahdhib)؛ المسمعة خرقها (ayn)؛ المسمع خرق الأذن (tahdhib;mufradat)؛ السامعة الأذن (sihah)؛ المسمعان الأذنان (sihah;tahdhib)
- **B003** anlayıp kabul etmek ve uymak — sözü anlayıp kabul etmek ve ona uymak
  تارة عن الفهم وتارة عن الطاعة (mufradat)؛ فهمنا وارتسمنا (mufradat)؛ فهمنا وهم لا يفهمون (mufradat)؛ لم يستعملوا هذه الحواس استعمالا يجدي عليهم (tahdhib)
- **B004** duyurmak veya kavratmak — duymasını sağlamak veya kavratmak · başkasına duyuran kimse
  سمعه الصوت وأسمعه (sihah)؛ السميع المسمع (sihah;tahdhib)؛ أسمعهم أي أفهمهم (mufradat)؛ فعلت ذلك تسمعتك وتسمعة لك أي لتسمعه (tahdhib)
- **B005** adı yayılıp tanınmak — yaymak, tanınır kılmak veya adını öne çıkarmak · güzel ün ve iyi ad · duyulup yayılan ve konuşulan şey · insanlar duysun diye yapılan gösteriş · insanların haberi birbirinden duyup yayması
  السمع الذكر الجميل (maqayis;sihah)؛ السماع ما سمعت به فشاع (ayn;tahdhib)؛ سمعت بالشيء إذا أشعته (maqayis)؛ فعله رياء وسمعة (ayn;sihah)؛ سمع به أي شهره (sihah)؛ سمعت بفلان في الناس إذا نوهت بذكره (tahdhib)
- **B006** kötü söz işittirip sövmek [kalıp] — sövmek ve hoşlanmayacağı sözleri yüzüne söylemek · sövmek veya duymaz olmasını dilemek
  أسمعه الحديث وسمعه أي شتمه (sihah)؛ أسمعت فلانا إذا سببته (mufradat)؛ أسمعك الله أي جعلك الله أصم (mufradat)؛ سمعت بالرجل تسميعا إذا نددت به وشهرته وفضحته (tahdhib)؛ أسمعته القبيح وشتمته (tahdhib)
- **B007** kulağa hoş gelen ezgili ses — şarkı veya kulağa hoş gelen güzel ses · kadın şarkıcı
  المسمعة المغنية (maqayis;sihah)؛ السماع الغناء (ayn)؛ السماع اسم ما استلذت الأذن من صوت حسن (tahdhib)؛ المسمعة القينة المغنية (ayn)
- **B008** taşıma kabının sap veya denge parçası — kova veya su kabının yükü dengeleyen sapı ya da halkası · büyük su kabının iki yanı veya yük sepetinin iki taşıyıcı tahtası · kovaya sap takmak veya saplarını yükü hafifletecek biçimde bağlamak
  المسمع كالأذن للغرب (maqayis)؛ مسمع الدلو والغرب عروة في وسطه (ayn;sihah)؛ المسمع من المزادة ما جاوز خرت العروة إلى الظرف (ayn)؛ المسمعان جانبا الغرب (tahdhib)؛ المسمع عروة في داخل الدلو (tahdhib)؛ حلقة مسمع الغرب (mufradat)
- **B009** ayak bağı veya hareket kısıtlayıcı bağ — ayak bağı veya bağlama aracı · iki ayak bağı ve bir boyun bağıyla bağlanmış
  من أسماء القيد المسمع؛ ولي مسمعان وزمارة؛ مسمعا مزمرا أي مقيدا مسوجرا
- **B010** kurt ile sırtlan arasında sayılan yırtıcı — kurt ile sırtlan arasında sayılan yırtıcı veya onların yavrusu · o yırtıcıdan bile daha keskin işiten
  السمع ولد الذئب من الضبع (maqayis;tahdhib)؛ السمع سبع بين الذئب والضبع (ayn)؛ السمع سبع مركب (sihah)؛ أسمع من السمع الأزل (sihah)
- **B011** duyulsun ama bana ulaşmasın — duyulsun ama bana ulaşmasın
  اللهم سمعا لا بلغا (sihah)؛ سمع لا بلغ معناه يسمع ولا يبلغ (tahdhib)؛ أسمع بالدواهي ولا تبلغني (tahdhib)
- **B012** küçük başlı, ince uzun veya çevik atılgan kimse — küçük başlı, ince uzun, çevik atılgan veya kötü
  السمعمع الصغير الرأس (sihah;tahdhib)؛ السمعمع من الرجال المنكمش الماضي (tahdhib)؛ الشيطان الخبيث يقال له سمعمع (tahdhib)؛ السمعمع من الرجال الدقيق الطويل (tahdhib)؛ امرأة سمعمعة (tahdhib)
- **B013** bakıp dinlediği hâlde göremeyince tahmin eden kadın — dinleyip baktığı hâlde bir şey göremeyince tahmin eden kadın
  امرأة سمعنة نظرنة (sihah;tahdhib)؛ إذا تسمعت أو تبصرت فلم تر شيئا تظنته تظنيا (sihah)؛ إذا سمعت أو تبصرت فلم تر شيئا تظنت تظنيا (tahdhib)
- **B014** kimsenin görüp duymadığı boş arazide [kalıp] — kimsenin görüp duymadığı boş arazide
  تخرج بين سمع الأرض وبصرها؛ ليس معها أحد يسمع كلامها أو يبصرها إلا الأرض القفر؛ لقيته يمشي بين سمع الأرض وبصرها أي بأرض خلاء ما بها أحد
- **B015** öküz koşumundaki iki uzun çubuk — toprak sürmek için iki öküzün bağlandığı düzenekteki iki uzun çubuk
  السميعان من أدوات الحراثين؛ عودان طويلان في المقرن الذي يقرن به الثوران لحراثة الأرض
- **B016** beyin — beyin
  أم السمع وأم السميع الدماغ؛ نقبن الحرة السوداء عنهم كنقب الرأس عن أم السميع

## ذ ك ر (root_000516): 68:51 ٱلذِّكْرَ, 68:52 ذِكْرٌ

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



===== _commentary/v16/work/s068/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s068/reader_a_pilot.md)

# s068 Semantic Channel Discovery

## Parent Channels

### 1. [P1 68:1-16] Legible Surfaces and Attributed Identity
- Semantic invariant: A surface becomes socially legible when lines, colors, marks, or attached signs assign content and identity to it.
- Surface relation: direct; 68:1 `قَلَمِ`/`يَسْطُرُ`, 68:11 `نَمِيمٍ`, 68:13 `زَنِيمٍ`, 68:15 `ءَايَٰتُ`/`قَالَ`/`أَسَٰطِيرُ`, and 68:16 `نَسِمُ`/`خُرْطُومِ`.
- Surprising reach: The opening pen and closing facial brand belong to one material semiotics: inscription may preserve truth, fabricate reputation, or fasten an identity to a body.

#### Subchannel A. Pared Reed, Ordered Rows, and Audible Inscription
- Reading type: mixed
- Scene or process: A hard tip is pared into a writing tool; it lays down ordered rows whose fine traces can even be imagined as a faint sound.
- Active motifs: successive paring (`quranic:root_001252:B001/m01`); writing reed (`quranic:root_001252:B003/m01`); cutting shears (`quranic:root_001252:B006/m01`); ordered written rows (`quranic:root_000704:B001/m01`); articulated statement (`quranic:root_001272:B001/m01`); faint sound of writing (`quranic:root_001557:B003/m01`); close fine lines (`quranic:root_001557:B007/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م] and `يَسْطُرُ` [س ط ر]; 68:11 `نَمِيمٍ` [ن م م]; 68:15 `قَالَ` [ق و ل].
- Synthesis: The pen is not an abstract emblem. Its point is produced by repeated cutting, then converts speech into aligned, durable traces. The minute noise and close lines supplied by `ن م م` make inscription a tactile and acoustic operation as well as a textual one.

#### Subchannel B. Fabricated Text Becomes Circulating Reputation
- Reading type: mixed
- Scene or process: Invented material is attributed to another, repeated as report, and carried through a community as slander or fable.
- Active motifs: baseless legends (`quranic:root_000704:B002/m01`); invented discourse (`quranic:root_000434:B007/m01`); lying about another (`quranic:root_000186:B009/m01`); false attribution (`quranic:root_001272:B005/m01`); circulating report (`quranic:root_001272:B007/m01`); falsehood (`quranic:root_001290:B001/m01`); declaring another false (`quranic:root_001290:B002/m01`); carried tale-bearing (`quranic:root_001557:B002/m01`); defaming people (`quranic:root_001600:B004/m01`).
- Ayah anchors: 68:4 `خُلُقٍ` [خ ل ق]; 68:8 `مُكَذِّبِينَ` [ك ذ ب]; 68:11 `نَمِيمٍ` [ن م م] and `هَمَّازٍ` [ه م ز]; 68:15 `تُتْلَىٰ` [ت ل و], `قَالَ` [ق و ل], and `أَسَٰطِيرُ` [س ط ر].
- Synthesis: Falsehood is assembled in stages: invention, attribution, repetition, and social circulation. This gives “legends of the former peoples” a processual underside and places the tale-bearer in the same economy of manufactured textual identity.

#### Subchannel C. The Body Is Read Through Brand, Appendage, and Facial Sign
- Reading type: mixed
- Scene or process: A cut or burned mark, a conspicuous appendage, and facial features become indices by which a person or animal is recognized.
- Active motifs: identifying brand or ear-cut (`quranic:root_001650:B001/m01`); reading character from a visible trace (`quranic:root_001650:B002/m01`); hanging ear-tag (`quranic:root_000647:B001/m01`); outsider recognized by an attached tag (`quranic:root_000647:B002/m01`); pedigree mark (`quranic:root_000647:B003/m01`); manifest sign (`quranic:root_000074:B003/m01`); distinguishing mark or banner (`quranic:root_001040:B002/m01`); split upper lip (`quranic:root_001040:B004/m01`); nose or animal snout (`quranic:root_000404:B001/m01`); head-raised anger and pride (`quranic:root_000404:B004/m01`).
- Ayah anchors: 68:7 `أَعْلَمُ` [ع ل م]; 68:13 `زَنِيمٍ` [ز ن م]; 68:15 `ءَايَٰتُ` [ء ي ي]; 68:16 `نَسِمُ` [و س م] and `خُرْطُومِ` [خ ر ط م].
- Synthesis: The brand on the snout materializes social legibility. `زَنِيم` adds an attached tag that identifies an alien affiliation, while the “sign” and “mark” senses turn bodily appearance into evidence that observers interpret.

#### Subchannel D. Coating and Pattern Can Beautify or Misstate a Surface
- Reading type: latent/lexical
- Scene or process: Oil, pigment, dye, and fine patterning alter a body or textile until its visible state may conceal its underlying condition.
- Active motifs: oil coating (`quranic:root_000497:B001/m01`); soft social dissimulation (`quranic:root_000497:B002/m01`); iridescent cloth (`quranic:root_001252:B010/m01`); patterned cloth that “lies” by appearance (`quranic:root_001290:B009/m01`); close ornamental lines (`quranic:root_001557:B007/m02`); contrasting fleck or gleam (`quranic:root_001557:B008/m01`); perfumed pigment (`quranic:root_000434:B010/m01`); visible beauty mark (`quranic:root_001650:B005/m01`); dye-bearing plant (`quranic:root_001650:B006/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م]; 68:4 `خُلُقٍ` [خ ل ق]; 68:8 `مُكَذِّبِينَ` [ك ذ ب]; 68:9 `تُدْهِنُ`/`يُدْهِنُ` [د ه ن]; 68:11 `نَمِيمٍ` [ن م م]; 68:16 `نَسِمُ` [و س م].
- Synthesis: The reciprocal “oiling” of 68:9 expands into a surface technology. Applied substances and textile patterns can produce genuine adornment, but they can also make an appearance assert what the underlying material does not warrant.

### 2. [P1 68:1-16] Covers Regulate Access to Sight and Interior Truth
- Semantic invariant: Seeing and knowing depend on whether a physical, mental, or social cover protects, obscures, or reveals what lies within.
- Surface relation: direct; 68:2 `مَجْنُونٍ`, 68:5 `تُبْصِرُ`/`يُبْصِرُ`, 68:7 `أَعْلَمُ`/`ضَلَّ`/`سَبِيلِ`, and 68:15 `ءَايَٰتُ`.
- Surprising reach: The charge of madness is reframed as an argument about covered interiors: eye-films, shields, shelters, ribs, and unspoken thought all test what observers can legitimately infer.

#### Subchannel A. Eye, Insight, and the Film That Defeats Both
- Reading type: mixed
- Scene or process: An eye opens onto a visible object, inward discernment interprets it, and a woven film or disappearance can interrupt both perception and retention.
- Active motifs: ocular sight (`quranic:root_000121:B001/m01`); inward discernment (`quranic:root_000121:B002/m01`); eye-film like a web (`quranic:root_000672:B010/m01`); hidden disappearance (`quranic:root_000913:B002/m01`); loss from memory (`quranic:root_000913:B004/m01`); cognition as disclosure (`quranic:root_001040:B001/m01`).
- Ayah anchors: 68:5 `تُبْصِرُ`/`يُبْصِرُ` [ب ص ر]; 68:7 `سَبِيلِ` [س ب ل], `ضَلَّ` [ض ل ل], and `أَعْلَمُ` [ع ل م].
- Synthesis: Perception proceeds from open eye to inward verification. The eye-film, disappearance, and failed memory show three distinct ways that evidence can cease to be available, sharpening the contrast between human seeing and divine knowing.

#### Subchannel B. A Covered Mind and an Unspoken Interior
- Reading type: mixed
- Scene or process: Thought and disposition are enclosed inside the chest; madness is imagined as the mind being covered or lost, while interior speech remains unvoiced.
- Active motifs: concealment from sense (`quranic:root_000266:B001/m01`); mind covered by madness (`quranic:root_000266:B006/m01`); hidden heart or inward matter (`quranic:root_000266:B010/m01`); reason or property lost in derangement (`quranic:root_001128:B007/m01`); speech held in the mind (`quranic:root_001272:B012/m01`); inward disposition (`quranic:root_000434:B004/m01`).
- Ayah anchors: 68:2 `مَجْنُونٍ` [ج ن ن]; 68:4 `خُلُقٍ` [خ ل ق]; 68:6 `مَفْتُونُ` [ف ت ن]; 68:15 `قَالَ` [ق و ل].
- Synthesis: The accusation “mad” purports to read an inaccessible interior. The branch imagery instead distinguishes hidden thought, durable disposition, and a mind overtaken by derangement, preventing those states from collapsing into one polemical label.

#### Subchannel C. Shield, Shelter, and Covering Skin
- Reading type: latent/lexical
- Scene or process: Leather, cloth, armor, and a screened place interpose a fitted layer between a vulnerable occupant and exterior force.
- Active motifs: protective shield (`quranic:root_000266:B008/m01`); hiding-place (`quranic:root_000266:B017/m01`); worn armor (`quranic:root_000121:B005/m01`); tent-like insect screen (`quranic:root_001315:B006/m01`); leather shelter or groundsheet (`quranic:root_000156:B004/m01`); leather saddle-cover (`quranic:root_001128:B008/m01`).
- Ayah anchors: 68:2 `مَجْنُونٍ` [ج ن ن]; 68:5 `تُبْصِرُ`/`يُبْصِرُ` [ب ص ر]; 68:6 `مَفْتُونُ` [ف ت ن]; 68:10 `كُلَّ` [ك ل ل]; 68:14 `بَنِينَ` [ب ن ي].
- Synthesis: Concealment is not only epistemic failure. The same invariant produces armor, shelter, and screened habitation, so a cover can preserve a life even as another cover prevents an observer from seeing truly.

#### Subchannel D. The Chest Frames Speech and Character
- Reading type: latent/lexical
- Scene or process: Ribs and thick bones form a load-bearing chest around the heart, while tongue and sharp articulation carry the enclosed person outward.
- Active motifs: chest-rib ends (`quranic:root_000266:B016/m01`); ribs and structural supports (`quranic:root_000156:B009/m01`); thick limb segment (`quranic:root_001029:B003/m01`); hard bone (`quranic:root_001029:B005/m01`); chest (`quranic:root_001315:B007/m01`); tongue as speech instrument (`quranic:root_001272:B002/m01`); sharp, fluent tongue (`quranic:root_000349:B004/m01`).
- Ayah anchors: 68:2 `مَجْنُونٍ` [ج ن ن]; 68:4 `عَظِيمٍ` [ع ظ م]; 68:10 `حَلَّافٍ` [ح ل ف] and `كُلَّ` [ك ل ل]; 68:14 `بَنِينَ` [ب ن ي]; 68:15 `قَالَ` [ق و ل].
- Synthesis: The person appears as a built interior: ribs and bone hold the chest, and the tongue projects what the chest contains. This anatomical scene gives material form to the pericope’s contrast between inward character and outward verbal aggression.

### 3. [P1 68:1-16] Direction Can Guide Bodies or Circulate Harm
- Semantic invariant: Movement acquires moral and social force through its route, guide, gait, and carried content.
- Surface relation: direct; 68:7 `ضَلَّ`/`سَبِيلِ`/`مُهْتَدِينَ`, 68:9 `تُدْهِنُ`, and 68:11 `مَّشَّآءٍ`/`نَمِيمٍ`.
- Surprising reach: Tale-bearing becomes a corrupted form of wayfaring: the same moving body that can follow a guide can also transport injury between people.

#### Subchannel A. Marked Route, Leading Guide, and Deviation
- Reading type: mixed
- Scene or process: A route offers access, a guide or leading point establishes direction, and deviation bends a traveler away from the intended line.
- Active motifs: traversable route (`quranic:root_000672:B001/m01`); traveler of the road (`quranic:root_000672:B002/m01`); gentle guidance to route and truth (`quranic:root_001583:B001/m01`); direction and manner of proceeding (`quranic:root_001583:B002/m01`); leading front or guide (`quranic:root_001583:B003/m01`); deviation from aim (`quranic:root_000913:B001/m01`); lost object or location (`quranic:root_000913:B003/m01`); inducement away from truth (`quranic:root_001128:B003/m01`); smooth road (`quranic:root_000497:B009/m01`).
- Ayah anchors: 68:6 `مَفْتُونُ` [ف ت ن]; 68:7 `سَبِيلِ` [س ب ل], `ضَلَّ` [ض ل ل], and `مُهْتَدِينَ` [ه د ي]; 68:9 `تُدْهِنُ`/`يُدْهِنُ` [د ه ن].
- Synthesis: Guidance is a spatial operation before it is an abstraction: route, direction, and leading front align movement. Error can be a wrong turn, a lost destination, or an agent’s active deflection of another traveler.

#### Subchannel B. Gait Registers Capacity, Terrain, and Exhaustion
- Reading type: latent/lexical
- Scene or process: A traveler moves on foot across edges and uneven ground; fatigue, bodily weakness, or reliance on companions alters the gait.
- Active motifs: deliberate walking (`quranic:root_001427:B001/m01`); running (`quranic:root_000993:B002/m01`); bank or side of a route (`quranic:root_000993:B009/m01`); hard uneven ground (`quranic:root_000993:B010/m01`); travel on foot (`quranic:root_001525:B012/m01`); supported swaying walk (`quranic:root_001583:B008/m01`); calm, composed gait (`quranic:root_001583:B010/m01`); exhaustion of walker or mount (`quranic:root_001315:B001/m01`); body worn down by use (`quranic:root_001453:B005/m01`).
- Ayah anchors: 68:7 `مُهْتَدِينَ` [ه د ي]; 68:10 `كُلَّ` [ك ل ل] and `مَّهِينٍ` [م ه ن]; 68:11 `مَّشَّآءٍ` [م ش ي]; 68:12 `مُعْتَدٍ` [ع د و]; 68:2 `نِعْمَةِ` [ن ع م].
- Synthesis: Movement discloses condition. The same route can carry a runner, an exhausted mount, a composed traveler, or a weakened pedestrian, so gait becomes a visible measure of agency rather than a neutral change of place.

#### Subchannel C. Tale-Bearing Is Speech Put on Foot
- Reading type: surface-primary
- Scene or process: A speaker extracts a damaging report, carries it from place to place, and presses or prods others with it.
- Active motifs: walking with tales (`quranic:root_001427:B004/m01`); emitted slander (`quranic:root_001557:B002/m01`); betraying whisper or footfall (`quranic:root_001557:B003/m02`); circulating public report (`quranic:root_001272:B007/m02`); prod that sets a body in motion (`quranic:root_001600:B003/m01`); defamation (`quranic:root_001600:B004/m01`); clamorous crowd (`quranic:root_000349:B006/m01`).
- Ayah anchors: 68:10 `حَلَّافٍ` [ح ل ف]; 68:11 `هَمَّازٍ` [ه م ز], `مَّشَّآءٍ` [م ش ي], and `نَمِيمٍ` [ن م م]; 68:15 `قَالَ` [ق و ل].
- Synthesis: The collocation in 68:11 is internally mechanized: the tale exits, the carrier walks, and the verbal prod moves its target. Rumor is thus a transported force with an itinerary and social impact.

### 4. [P1 68:1-16] Authority Binds, Restrains, and Releases
- Semantic invariant: Authority is enacted by keeping charge, binding parties, directing motion, or deciding whether restraint continues.
- Surface relation: direct; 68:2/7 `رَبِّ`/`رَبَّ`, 68:8/10 `تُطِعِ`/`تُطِعْ`, 68:10 `حَلَّافٍ`, 68:12 `مُعْتَدٍ`, and 68:13 `عُتُلٍّ`.
- Surprising reach: Lordship, contract, bridle-like obedience, coercive hauling, and release from captivity occupy one field of controlled attachment without being reduced to one moral value.

#### Subchannel A. Mastery as Care, Knowledge, and Watch
- Reading type: mixed
- Scene or process: A master owns and tends what is under charge; learned oversight and watchful supervision preserve and direct it.
- Active motifs: lordship and ownership (`quranic:root_000532:B001/m01`); gradual nurture and repair (`quranic:root_000532:B002/m01`); cultivated authoritative knowledge (`quranic:root_000532:B003/m01`); captain of sailors (`quranic:root_000532:B017/m01`); supervising controller (`quranic:root_000704:B003/m01`); chief whose word carries (`quranic:root_001272:B004/m01`).
- Ayah anchors: 68:2 `رَبِّ` and 68:7 `رَبَّ` [ر ب ب]; 68:1 `يَسْطُرُ` and 68:15 `أَسَٰطِيرُ` [س ط ر]; 68:15 `قَالَ` [ق و ل].
- Synthesis: The master is not only an owner but a cultivator, knower, captain, and watcher. These roles clarify why the pericope repeatedly locates final knowledge of direction and error with the `رَبّ`.

#### Subchannel B. Covenant, Surety, and Attached Membership
- Reading type: latent/lexical
- Scene or process: An oath or covenant fastens people to one another; a surety carries another’s obligation, and an attached outsider acquires a disputed membership.
- Active motifs: alliance and binding pact (`quranic:root_000349:B002/m01`); covenant and protected relation (`quranic:root_000532:B011/m01`); liability that follows its bearer (`quranic:root_000186:B004/m01`); standing surety (`quranic:root_001332:B003/m01`); member attached to a group not originally his (`quranic:root_000647:B002/m02`).
- Ayah anchors: 68:7 `رَبَّ` [ر ب ب]; 68:10 `حَلَّافٍ` [ح ل ف]; 68:13 `زَنِيمٍ` [ز ن م]; 68:14 `كَانَ` [ك و ن]; 68:15 `تُتْلَىٰ` [ت ل و].
- Synthesis: Social belonging is represented as an attachment that can arise through oath, guarantee, or annexation. The marked outsider is therefore not merely an insult but the unstable edge of a binding social mechanism.

#### Subchannel C. Obedience, Refusal, and Coercive Hauling
- Reading type: mixed
- Scene or process: A command seeks smooth compliance; resistance hardens into mutual pushing or refusal, and force then drags the resistant body.
- Active motifs: obedient following (`quranic:root_000956:B001/m01`); mutual compliance (`quranic:root_000956:B002/m01`); the self making action easy (`quranic:root_000956:B006/m01`); violent hauling (`quranic:root_000980:B001/m01`); refusal to move or submit (`quranic:root_000980:B005/m01`); servant or enforcer (`quranic:root_000980:B006/m01`); transgressive overstepping (`quranic:root_000993:B001/m01`); obstructing barrier (`quranic:root_001448:B002/m01`); protected force (`quranic:root_001448:B003/m01`); mutual resistance (`quranic:root_001448:B006/m01`).
- Ayah anchors: 68:8 `تُطِعِ` and 68:10 `تُطِعْ` [ط و ع]; 68:12 `مُعْتَدٍ` [ع د و] and `مَّنَّاعٍ` [م ن ع]; 68:13 `عُتُلٍّ` [ع ت ل].
- Synthesis: Compliance ranges from willing alignment to reciprocal accommodation. Against it stand barrier, fortified resistance, and the brutal hauling encoded by `عُتُلّ`, giving the prohibition on obedience a concrete politics of who directs whose body.

#### Subchannel D. Arms, Captivity, and Uncompensated Release
- Reading type: latent/lexical
- Scene or process: Shield, cutting weapon, spear-part, and heavy tool produce capture; authority may then release the captive without ransom.
- Active motifs: shield (`quranic:root_000266:B008/m02`); armor (`quranic:root_000121:B005/m02`); sword-cut or butcher’s blade (`quranic:root_000704:B004/m01`); pared spear-tip or shaft (`quranic:root_001252:B005/m01`); crowbar or heavy club (`quranic:root_000980:B003/m01`); release of a captive without exchange (`quranic:root_001449:B004/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م] and `يَسْطُرُ` [س ط ر]; 68:2 `مَجْنُونٍ` [ج ن ن]; 68:3 `مَمْنُونٍ` [م ن ن]; 68:5 `تُبْصِرُ`/`يُبْصِرُ` [ب ص ر]; 68:13 `عُتُلٍّ` [ع ت ل].
- Synthesis: The martial scene keeps protection, violence, custody, and release distinct. Its unexpected pressure on “uninterrupted reward” is that `م ن ن` can also name the sovereign interruption of captivity without a compensating payment.

### 5. [P1 68:1-16] Provision Builds Households or Is Arrested at the Hand
- Semantic invariant: Material good becomes socially meaningful through giving, nurturing, earning, withholding, and household reproduction.
- Surface relation: direct; 68:2 `نِعْمَةِ`, 68:3 `أَجْرًا`/`مَمْنُونٍ`, 68:12 `مَّنَّاعٍ لِّلْخَيْرِ`, and 68:14 `مَالٍ`/`بَنِينَ`.
- Surprising reach: Wealth and sons are not static possessions; lexical scenes show provision moving through wages, gifts, marriage, livestock, and care, or failing through blocked hands and depleted stores.

#### Subchannel A. Favor Moves as Reward, Gift, and Nurture
- Reading type: mixed
- Scene or process: A benefactor gives a useful good, a caretaker grows it over time, and recompense returns value for work without exhausting the source.
- Active motifs: favor and good condition (`quranic:root_001525:B001/m01`); ease and comfortable living (`quranic:root_001525:B002/m01`); delight to the eye (`quranic:root_001525:B013/m01`); favor that can burden its recipient (`quranic:root_001449:B003/m01`); nurturing benefaction (`quranic:root_000532:B016/m01`); desired beneficial good (`quranic:root_000452:B001/m01`); generosity and gift (`quranic:root_000452:B005/m01`); recompense or wage (`quranic:root_000015:B001/m01`); visible traces of prosperity (`quranic:root_000497:B011/m01`).
- Ayah anchors: 68:2 `نِعْمَةِ` [ن ع م] and `رَبِّ` [ر ب ب]; 68:3 `أَجْرًا` [ء ج ر] and `مَمْنُونٍ` [م ن ن]; 68:9 `تُدْهِنُ` [د ه ن]; 68:12 `خَيْرِ` [خ ي ر].
- Synthesis: Favor is a flow joining giver, work, recipient, and visible result. The branch contrast inside `م ن ن` adds a precise risk: a gift can sustain, or its verbal recounting can crush the recipient and undo the social good.

#### Subchannel B. The Withholding Hand Produces Scarcity and Weakness
- Reading type: mixed
- Scene or process: A hand refuses transfer, a barrier blocks access, and the resulting shortage appears as scant water, little milk, depleted strength, or an emptied belly.
- Active motifs: hand withheld from giving (`quranic:root_001448:B001/m01`); barrier to desired access (`quranic:root_001448:B002/m02`); weakness and contempt (`quranic:root_001453:B001/m01`); scant water or sterile issue (`quranic:root_001453:B006/m01`); little milk (`quranic:root_000497:B006/m01`); lost strength (`quranic:root_001449:B002/m01`); camel belly retaining no water (`quranic:root_001557:B001/m01`).
- Ayah anchors: 68:3 `مَمْنُونٍ` [م ن ن]; 68:9 `تُدْهِنُ` [د ه ن]; 68:10 `مَّهِينٍ` [م ه ن]; 68:11 `نَمِيمٍ` [ن م م]; 68:12 `مَّنَّاعٍ` [م ن ع].
- Synthesis: Withholding is rendered hydrologically and bodily. What begins as a social refusal at the hand terminates in low milk, low water, weak reproductive force, and an emptied animal, making deprivation a material outcome rather than only a vice.

#### Subchannel C. House, Marriage, Children, and Wealth Form One Productive Unit
- Reading type: mixed
- Scene or process: A dwelling is assembled, marriage initiates a household, children and livestock increase it, and food builds its members’ flesh.
- Active motifs: house built by joined parts (`quranic:root_000156:B001/m01`); marriage and entry into household (`quranic:root_000156:B006/m01`); descent and filiation (`quranic:root_000156:B007/m01`); food building flesh (`quranic:root_000156:B010/m01`); accumulated wealth (`quranic:root_001457:B001/m01`); growth of livestock and offspring (`quranic:root_001427:B003/m01`); bride-gift (`quranic:root_001583:B004/m01`); bride conducted to spouse (`quranic:root_001583:B006/m01`); bridal payment (`quranic:root_000015:B001/m02`); separation from a spouse (`quranic:root_001252:B009/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م]; 68:3 `أَجْرًا` [ء ج ر]; 68:7 `مُهْتَدِينَ` [ه د ي]; 68:11 `مَّشَّآءٍ` [م ش ي]; 68:14 `بَنِينَ` [ب ن ي] and `مَالٍ` [م و ل].
- Synthesis: “Wealth and sons” expands into a household production scene: architecture, marriage, payment, descent, nourishment, and animal increase. Its reverse is equally concrete in spousal separation and arrested circulation of wealth.

#### Subchannel D. Affiliation Distinguishes Household Member, Ally, and Attached Outsider
- Reading type: latent/lexical
- Scene or process: A populous group organizes around a leader and kin; alliance can attach outsiders, but distance of lineage and visible tagging preserve status differences.
- Active motifs: tagged outsider (`quranic:root_000647:B002/m03`); distant kin (`quranic:root_000131:B005/m01`); alliance (`quranic:root_000349:B002/m02`); assembled tribal groups (`quranic:root_000532:B004/m01`); herd as social aggregate (`quranic:root_000532:B014/m01`); mass of people (`quranic:root_000266:B013/m01`); regional chief (`quranic:root_001272:B004/m02`).
- Ayah anchors: 68:2/7 `رَبِّ`/`رَبَّ` [ر ب ب]; 68:10 `حَلَّافٍ` [ح ل ف]; 68:13 `بَعْدَ` [ب ع د] and `زَنِيمٍ` [ز ن م]; 68:15 `قَالَ` [ق و ل]; 68:2 `مَجْنُونٍ` [ج ن ن].
- Synthesis: Belonging is not one relation. Kinship, pact, leadership, mass membership, and annexed outsider status are distinguishable mechanisms, which prevents the social portrait in 68:10-14 from becoming a generic list of insults.

### 6. [P1 68:1-16] Assay Exposes Formation and Moral Texture
- Semantic invariant: Pressure reveals whether a formed thing is sound, rough, delayed, brittle, or fit for its intended work.
- Surface relation: direct; 68:4 `خُلُقٍ عَظِيمٍ`, 68:6 `مَفْتُونُ`, 68:10 `مَّهِينٍ`, 68:12 `مُعْتَدٍ أَثِيمٍ`, and 68:13 `عُتُلٍّ`.
- Surprising reach: Character is treated like material under assay: measured before formation, tested by fire or ordeal, and disclosed through hardness, lag, excess, and capacity for repair.

#### Subchannel A. Fire and Ordeal Separate Sound Material from Dross
- Reading type: mixed
- Scene or process: Metal or a person is placed under testing heat; burning changes color, while hardship or conflict discloses quality.
- Active motifs: assay of metal and person (`quranic:root_001128:B001/m01`); burning and blackening (`quranic:root_001128:B002/m01`); ordeal in hardship or ease (`quranic:root_001128:B004/m01`); conflict as testing disturbance (`quranic:root_001128:B006/m01`).
- Ayah anchors: 68:6 `مَفْتُونُ` [ف ت ن].
- Synthesis: `مَفْتُون` activates a metallurgical scene in which exposure does not merely hurt but discriminates. Fire, changed surface, ordeal, and conflict all serve the operation of making hidden quality observable.

#### Subchannel B. Measured Formation Produces Shape, Disposition, and Fitness
- Reading type: mixed
- Scene or process: Material is measured before cutting, brought into a balanced form, and judged fit for a role; human disposition is the inward analogue of that formation.
- Active motifs: prior measuring and proportioning (`quranic:root_000434:B001/m01`); creative production (`quranic:root_000434:B002/m01`); complete balanced form (`quranic:root_000434:B003/m01`); inward disposition (`quranic:root_000434:B004/m02`); fitness and readiness (`quranic:root_000434:B005/m01`); magnitude and force (`quranic:root_001029:B001/m01`); awe before a great matter (`quranic:root_001029:B007/m01`); honor and dignity (`quranic:root_001029:B010/m01`).
- Ayah anchors: 68:4 `خُلُقٍ` [خ ل ق] and `عَظِيمٍ` [ع ظ م].
- Synthesis: Great character is a formed capacity, not a decorative epithet. Measurement, balanced shape, inward nature, readiness, magnitude, and earned awe compose a precise account of moral constitution.

#### Subchannel C. Lag, Roughness, and Overstepping Reveal Defective Material
- Reading type: mixed
- Scene or process: A subject lags behind good, crosses a boundary, resists easy handling, and presents a coarse or blunt texture under pressure.
- Active motifs: delay from good (`quranic:root_000013:B001/m01`); abstention from wrongdoing (`quranic:root_000013:B002/m01`); penalty of wrongdoing (`quranic:root_000013:B003/m01`); loading another with guilt (`quranic:root_000013:B004/m01`); unjust overstepping (`quranic:root_000993:B001/m02`); twisted difficulty (`quranic:root_000993:B012/m01`); coarse hostile character (`quranic:root_000980:B002/m01`); severe thickness (`quranic:root_000980:B004/m01`); low weak judgment (`quranic:root_001453:B001/m02`); bluntness and exhaustion (`quranic:root_001315:B001/m02`).
- Ayah anchors: 68:10 `كُلَّ` [ك ل ل] and `مَّهِينٍ` [م ه ن]; 68:12 `مُعْتَدٍ` [ع د و] and `أَثِيمٍ` [ء ث م]; 68:13 `عُتُلٍّ` [ع ت ل].
- Synthesis: The denunciatory sequence has distinct mechanics. Sin delays movement toward good, transgression crosses the limit, `عُتُلّ` supplies coarse resistant bulk, and `مَهِين` names depleted discernment; these are not interchangeable moral labels.

#### Subchannel D. Pride Hardens; Repair Restores Fit
- Reading type: mixed
- Scene or process: Self-magnification and head-raised anger harden a person against correction, while repair, exchange, and selection restore useful form.
- Active motifs: arrogant self-enlargement (`quranic:root_001029:B006/m01`); angry raised-head pride (`quranic:root_000404:B004/m02`); imposing judgment on another (`quranic:root_001272:B010/m01`); nurture and repair (`quranic:root_000532:B002/m02`); material or practical repair (`quranic:root_001119:B001/m01`); transformation or replacement (`quranic:root_001119:B003/m01`); selected excellence (`quranic:root_000452:B002/m01`).
- Ayah anchors: 68:2/7 `رَبِّ`/`رَبَّ` [ر ب ب]; 68:3 `غَيْرَ` [غ ي ر]; 68:4 `عَظِيمٍ` [ع ظ م]; 68:12 `خَيْرِ` [خ ي ر]; 68:15 `قَالَ` [ق و ل]; 68:16 `خُرْطُومِ` [خ ر ط م].
- Synthesis: Pride is a deformation of magnitude into self-hardening. The counter-process is not mere condemnation but correction: tend, repair, exchange the damaged state, and select what is genuinely fit.

### 7. [P1 68:1-16] Rain Materializes Provision in Soil, Plant, and Herd
- Semantic invariant: Provision becomes visible through a water-driven sequence from cloud and rain to marked earth, vegetation, stored water, and animal yield.
- Surface relation: indirect; 68:2 `نِعْمَةِ`, 68:7 `رَبَّ`/`أَعْلَمُ`, 68:10 `حَلَّافٍ`, and 68:12 `خَيْرِ`.
- Surprising reach: The abstract vocabulary of favor is grounded in an ecology whose failures are equally specific: insufficient rain, dry basins, weak milk, and wandering livestock.

#### Subchannel A. Cloud and Falling Water Mark the Ground
- Reading type: latent/lexical
- Scene or process: Layered cloud persists, rain descends between sky and earth, and the first seasonal water inscribes the soil with growth.
- Active motifs: layered rain-cloud (`quranic:root_000532:B008/m01`); abundant gathered water (`quranic:root_000532:B013/m01`); downward release of cloud and rain (`quranic:root_000672:B004/m01`); rain suspended between cloud and earth (`quranic:root_000672:B005/m01`); first rain marking earth with plants (`quranic:root_001650:B003/m01`); light wetting rain (`quranic:root_000497:B003/m01`); gentle moist wind (`quranic:root_001525:B009/m01`).
- Ayah anchors: 68:2 `نِعْمَةِ` [ن ع م]; 68:7 `رَبَّ` [ر ب ب] and `سَبِيلِ` [س ب ل]; 68:9 `تُدْهِنُ` [د ه ن]; 68:16 `نَسِمُ` [و س م].
- Synthesis: Rain functions like the pericope’s writing and branding: it descends and leaves a readable mark. Cloud persistence, falling water, moist wind, and newly signed ground form a complete meteorological process.

#### Subchannel B. Covered Garden, Grain Ear, and Aromatic Growth
- Reading type: latent/lexical
- Scene or process: Water drives enclosing vegetation upward; grain extends into ears, low plants spread, and aromatic growth announces itself by scent.
- Active motifs: tree-covered garden (`quranic:root_000266:B003/m01`); dense rising vegetation (`quranic:root_000266:B011/m01`); persistent green plant (`quranic:root_000532:B012/m01`); extended grain ear (`quranic:root_000672:B008/m01`); low salt plant (`quranic:root_001252:B007/m01`); halfa grass (`quranic:root_000349:B005/m01`); aromatic plant disclosed by smell (`quranic:root_001557:B004/m01`); summer browse after spring (`quranic:root_000993:B011/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م]; 68:2 `مَجْنُونٍ` [ج ن ن]; 68:7 `رَبَّ` [ر ب ب] and `سَبِيلِ` [س ب ل]; 68:10 `حَلَّافٍ` [ح ل ف]; 68:11 `نَمِيمٍ` [ن م م]; 68:12 `مُعْتَدٍ` [ع د و].
- Synthesis: The scene is a succession of plant forms rather than a generic “nature” motif. Enclosure, upward density, earing grain, low browse, and scent each mark a different stage or mode by which provision occupies the land.

#### Subchannel C. Rock Pool, Oil Basin, and Deep Water Store
- Reading type: latent/lexical
- Scene or process: Natural and made depressions catch water; their stone edges and depth determine whether the collected resource remains available.
- Active motifs: rainwater caught in a rock hollow (`quranic:root_000434:B011/m01`); oil vessel or mountain pool (`quranic:root_000497:B005/m01`); sea or water-rich well (`quranic:root_001040:B005/m01`); abundant collected water (`quranic:root_000532:B013/m02`); soft pale basin-stone (`quranic:root_000121:B007/m01`).
- Ayah anchors: 68:4 `خُلُقٍ` [خ ل ق]; 68:5 `تُبْصِرُ`/`يُبْصِرُ` [ب ص ر]; 68:7 `رَبَّ` [ر ب ب] and `أَعْلَمُ` [ع ل م]; 68:9 `تُدْهِنُ` [د ه ن].
- Synthesis: Provision is stored by topology: hollow, vessel, well, and stone rim. This compact hydrological mechanism usefully pressures the language of favor by showing the material infrastructure through which water becomes durable benefit.

#### Subchannel D. Herd, Milk, and the Risk of Depletion
- Reading type: latent/lexical
- Scene or process: A herd is maintained through recent birth, watering, milking, and pasture; shortage appears as low milk, weak issue, or a stray animal outside ownership.
- Active motifs: recently delivered milk-animal (`quranic:root_000532:B009/m01`); herd of cattle or camels (`quranic:root_000532:B014/m02`); livestock wealth (`quranic:root_001525:B005/m01`); milking camels at the chest (`quranic:root_001453:B004/m01`); low milk and weakness (`quranic:root_000497:B006/m02`); scant reproductive fluid (`quranic:root_001453:B006/m02`); ownerless stray camel (`quranic:root_000913:B005/m01`).
- Ayah anchors: 68:2 `نِعْمَةِ` [ن ع م] and `رَبِّ` [ر ب ب]; 68:7 `ضَلَّ` [ض ل ل]; 68:9 `تُدْهِنُ` [د ه ن]; 68:10 `مَّهِينٍ` [م ه ن].
- Synthesis: The herd makes wealth biologically contingent. Birth, milk, pasture, and ownership must remain aligned; weakness, low yield, or straying breaks the sequence by which living assets reproduce provision.

### 8. [P1 68:1-16] Fitted Parts Make Shelters, Implements, and Cuts
- Semantic invariant: Material becomes functional by cutting, joining, tensioning, or arranging parts into a load-bearing whole.
- Surface relation: indirect; 68:1 `قَلَمِ`, 68:4 `عَظِيمٍ`, 68:6 `مَفْتُونُ`, 68:10 `كُلَّ`, and 68:13 `عُتُلٍّ`.
- Surprising reach: The writing tool belongs to a larger craft world of stitched leather, tent frames, bows, lots, clubs, and terminal cuts; “whole” and “part” are physical operations before they become discourse categories.

#### Subchannel A. Stitched Leather Stretches Across a Wooden Frame
- Reading type: latent/lexical
- Scene or process: Poles, ribs, and saddle wood support a fitted leather or cloth cover whose seams create a protected interior.
- Active motifs: carrying frame or tent poles (`quranic:root_000067:B008/m01`); leather dome or groundsheet (`quranic:root_000156:B004/m02`); ribs and house-posts (`quranic:root_000156:B009/m02`); saddle wood (`quranic:root_001029:B009/m01`); leather saddle-cover (`quranic:root_001128:B008/m02`); protective screen (`quranic:root_001315:B006/m02`); joining two hides or cloth panels (`quranic:root_000121:B006/m01`).
- Ayah anchors: 68:4 `عَظِيمٍ` [ع ظ م]; 68:5 `تُبْصِرُ`/`يُبْصِرُ` [ب ص ر]; 68:6 `مَفْتُونُ` [ف ت ن]; 68:10 `كُلَّ` [ك ل ل]; 68:14 `بَنِينَ` [ب ن ي]; 68:15 `أَوَّلِينَ` [ء و ل].
- Synthesis: The shelter is a distributed assembly: frame, posts, saddle wood, cover, and seam. Its coherence rests on fitted tension, giving the pericope a concrete model for how separate parts become a protective whole.

#### Subchannel B. Lot-Arrows and Game-Sticks Turn Cut Wood into Decision
- Reading type: latent/lexical
- Scene or process: Pared shafts are collected in a container, cast as lots, or used as striking sticks, turning shaped wood into an instrument of selection or play.
- Active motifs: lot-arrow (`quranic:root_001252:B004/m01`); hide container holding arrows (`quranic:root_000532:B010/m01`); stick for striking a game-piece (`quranic:root_001272:B008/m01`); heavy levering tool (`quranic:root_000980:B003/m02`); carrying implement (`quranic:root_000067:B008/m02`); saddle timber (`quranic:root_001029:B009/m02`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م]; 68:2/7 `رَبِّ`/`رَبَّ` [ر ب ب]; 68:4 `عَظِيمٍ` [ع ظ م]; 68:13 `عُتُلٍّ` [ع ت ل]; 68:15 `قَالَ` [ق و ل] and `أَوَّلِينَ` [ء و ل].
- Synthesis: Cutting does not predetermine use. The same shaped wood can write, strike, lever, or enter a lot, so material preparation precedes a social decision about the implement’s operation.

#### Subchannel C. Successive Cutting Ends a Line, Bond, or Life
- Reading type: mixed
- Scene or process: A blade removes material piece by piece until a line, cord, relation, or living duration is interrupted.
- Active motifs: repeated paring (`quranic:root_001252:B001/m02`); shears (`quranic:root_001252:B006/m02`); sword-line cut (`quranic:root_000704:B004/m02`); cutting and diminution of duration (`quranic:root_001449:B001/m01`); last breath (`quranic:root_000186:B008/m01`); imposed separation (`quranic:root_000131:B003/m01`); destruction or expulsion from good (`quranic:root_000131:B004/m01`).
- Ayah anchors: 68:1 `قَلَمِ` [ق ل م] and `يَسْطُرُ` [س ط ر]; 68:3 `مَمْنُونٍ` [م ن ن]; 68:13 `بَعْدَ` [ب ع د]; 68:15 `تُتْلَىٰ` [ت ل و].
- Synthesis: The concrete act of cutting supplies a precise contrast to the reward that is `غَيْرَ مَمْنُونٍ`: the reward neither runs down nor reaches the last severed point. The same operation also explains how separation becomes social or mortal.

### 9. [P1 68:1-16] Discourse Operators Allocate Reference, Scope, and Sequence
- Semantic invariant: A claim becomes intelligible by selecting its referent, setting its scope, and locating it before, after, or at an outcome.
- Surface relation: direct; 68:3 `غَيْرَ`, 68:10 `كُلَّ`, and 68:15 `ءَايَٰتُ`/`أَوَّلِينَ`.
- Surprising reach: The pericope’s contest over “which of you,” “every,” “other than,” and “former” has a latent architecture of questioning, totalization, exception, succession, and return.

#### Subchannel A. Question, Demonstration, and Explanation Fix the Referent
- Reading type: latent/lexical
- Scene or process: Interrogation selects among alternatives, a demonstrative points to one, and an explanatory operator unfolds what the pointer means.
- Active motifs: interrogative selection (`quranic:root_000074:B004/m01`); explanatory “that is” (`quranic:root_000074:B009/m01`); oath-opening affirmation (`quranic:root_000074:B010/m01`); relative “the one who” (`quranic:root_000527:B002/m01`); demonstrative pointer (`quranic:root_000527:B003/m01`); interrogative-relative “what?” (`quranic:root_000527:B004/m01`).
- Ayah anchors: 68:15 `ءَايَٰتُ` [ء ي ي]; surface anchor unavailable for root `ذ و و`.
- Synthesis: Reference is built in three operations: ask which entity is meant, point to it, then explain the selected content. The oath-opening sense adds commitment to the act of reference rather than new subject matter.

#### Subchannel B. Totality, Exception, Priority, and Outcome Bound the Claim
- Reading type: mixed
- Scene or process: A discourse gathers all parts, excludes or contrasts one, orders what comes first and after, and finally returns an expression to its outcome.
- Active motifs: total inclusion (`quranic:root_001315:B003/m01`); difference, exception, or negation (`quranic:root_001119:B005/m01`); firstness and priority (`quranic:root_000067:B001/m01`); return to outcome or interpretation (`quranic:root_000067:B002/m01`); temporal succession after (`quranic:root_000131:B002/m01`); following in sequence (`quranic:root_000186:B001/m01`); remainder that follows (`quranic:root_000186:B003/m01`).
- Ayah anchors: 68:3 `غَيْرَ` [غ ي ر]; 68:10 `كُلَّ` [ك ل ل]; 68:13 `بَعْدَ` [ب ع د]; 68:15 `تُتْلَىٰ` [ت ل و] and `أَوَّلِينَ` [ء و ل].
- Synthesis: Scope and sequence jointly regulate interpretation. `كُلّ` gathers, `غَيْر` removes or contrasts, `أَوَّل` establishes precedence, and the following/after/outcome senses determine how a statement continues and where it finally lands.

### 10. [P2 68:17-33] The Orchard Moves from Assay to Cultivation, Cutting, and Meal
- Semantic invariant: Productive value is disclosed through a staged cycle: weathering and test, prepared soil, ripened growth, harvest, and consumption.
- Surface relation: direct; 68:17 `بَلَوْ`/`جَنَّةِ`/`يَصْرِمُ`/`مُصْبِحِينَ`, 68:22 `حَرْثِ`/`صَٰرِمِينَ`, and 68:25 `غَدَ`/`قَٰدِرِينَ`.
- Surprising reach: The owners are themselves processed like the orchard: wear and testing reveal condition, while planning, cutting, and morning consumption specify the material sequence they try to control.

#### Subchannel A. Wear and Trial Reveal Condition
- Reading type: mixed
- Scene or process: Use wears a surface down; testing then makes the hidden quality of work or character appear.
- Active motifs: wear and fraying (`quranic:root_000153:B001/m01`); test that manifests quality (`quranic:root_000153:B002/m01`); worn material (`quranic:root_000154:B001/m01`); ordeal disclosing condition (`quranic:root_000154:B002/m01`).
- Ayah anchors: 68:17 `بَلَوْ` [ب ل و]; surface anchor unavailable for root `ب ل ي`.
- Synthesis: The two lexical root analyses preserve the same transformation with distinct provenance. Wear supplies a slow material assay; explicit trial accelerates the same disclosure by making quality, intention, or workmanship observable.

#### Subchannel B. Soil Is Prepared and Growth Is Tended
- Reading type: mixed
- Scene or process: Seed enters worked ground, cultivation compacts a route through the field, and sheltered vegetation rises toward fruiting.
- Active motifs: tree-covered orchard (`quranic:root_000266:B003/m02`); dense rising vegetation (`quranic:root_000266:B011/m02`); earning through labor (`quranic:root_000303:B001/m01`); casting seed into prepared soil (`quranic:root_000303:B002/m01`); worked or trampled field (`quranic:root_000303:B008/m01`); tending and completion (`quranic:root_000532:B002/m03`); persistent green plant (`quranic:root_000532:B012/m02`); pollinating tall palms (`quranic:root_000946:B014/m01`); palm cluster and dates (`quranic:root_001015:B005/m01`).
- Ayah anchors: 68:17 `جَنَّةِ` [ج ن ن]; 68:19 `رَّبِّ` [ر ب ب]; 68:22 `حَرْثِ` [ح ر ث]; 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:32 `عَسَىٰ` [ع س ي].
- Synthesis: The orchard is a managed system rather than an undifferentiated abundance. Soil preparation, seed, compacted access, tending, palm pollination, and fruit cluster each occupy a different role in production.

#### Subchannel C. Ripened Growth Is Cut into Shares
- Reading type: surface-primary
- Scene or process: The crop reaches cutting-time, is severed from its plant, and becomes a field of pieces that can be gathered, divided, and carried.
- Active motifs: cutting and separation (`quranic:root_000861:B001/m01`); palm harvest (`quranic:root_000861:B002/m01`); harvested field or cut portion (`quranic:root_000861:B005/m01`); separated share (`quranic:root_001226:B003/m01`); woven palm container for fresh dates (`quranic:root_000464:B010/m01`); measured limit (`quranic:root_001205:B001/m01`); planned and fitted operation (`quranic:root_001205:B005/m01`).
- Ayah anchors: 68:17 `أَقْسَمُ` [ق س م] and `يَصْرِمُ` [ص ر م]; 68:20 `صَّرِيمِ` and 68:22 `صَٰرِمِينَ` [ص ر م]; 68:24 `يَدْخُلَ` [د خ ل]; 68:25 `قَٰدِرِينَ` [ق د ر].
- Synthesis: Harvest translates living continuity into countable portions. The cut, cleared field, allocated share, carrying basket, measured limit, and prior plan expose exactly where distributive justice could enter the production sequence.

#### Subchannel D. Morning Converts Harvest into a Scheduled Meal
- Reading type: mixed
- Scene or process: Dawn sets the work-time; arrival in the morning is coordinated with a first meal, drink, and cooking vessel.
- Active motifs: first light (`quranic:root_000839:B001/m01`); morning arrival (`quranic:root_000839:B002/m01`); morning drink or food (`quranic:root_000839:B003/m01`); becoming in the morning (`quranic:root_000839:B010/m01`); early departure (`quranic:root_001076:B001/m01`); breakfast (`quranic:root_001076:B004/m01`); day-cutting meal (`quranic:root_000861:B009/m01`); cooking pot and prepared food (`quranic:root_001205:B007/m01`).
- Ayah anchors: 68:17 `مُصْبِحِينَ`, 68:20 `أَصْبَحَتْ`, and 68:21 `مُصْبِحِينَ` [ص ب ح]; 68:22 `ٱغْدُ` and 68:25 `غَدَ` [غ د و]; 68:22 `صَٰرِمِينَ` [ص ر م]; 68:25 `قَٰدِرِينَ` [ق د ر].
- Synthesis: Morning is an operational clock joining departure, cutting, drink, meal, and cooking. The ruined orchard interrupts not only ownership but the timed conversion of crop into daily sustenance.

### 11. [P2 68:17-33] Water and Milk Must Keep Moving Through a Managed Circuit
- Semantic invariant: A living resource remains productive only when rain, stored water, pasture, herd movement, and milk transfer continue through connected stages.
- Surface relation: indirect; 68:17 `جَنَّةِ`, 68:19 `طَافَ`/`رَّبِّ`, 68:21 `تَنَادَ`, 68:24 `يَدْخُلَ`, 68:25 `حَرْدٍ`, and 68:27 `مَحْرُومُونَ`.
- Surprising reach: The garden’s loss is reframed as a broken hydrological and husbandry circuit: dew, trough, repeated watering, pasture, lactation, and access can each be the point of arrest.

#### Subchannel A. Rain, Dew, Flood, and Deep Water Form the Supply
- Reading type: latent/lexical
- Scene or process: Cloud and dew wet the land, an encircling flood enlarges the flow, and water collects in a deep store that may be sweet and usable.
- Active motifs: rain cloud (`quranic:root_000532:B008/m02`); abundant collected water (`quranic:root_000532:B013/m03`); dew and rain (`quranic:root_001486:B003/m01`); moisture and wet ground (`quranic:root_001487:B005/m01`); surrounding flood (`quranic:root_000957:B002/m01`); wetness retained in a skin (`quranic:root_000152:B001/m01`); deep well or sea (`quranic:root_001040:B005/m02`); sweet potable water (`quranic:root_000994:B001/m01`).
- Ayah anchors: 68:19 `طَافَ`/`طَآئِفٌ` [ط و ف] and `رَّبِّ` [ر ب ب]; 68:21 `تَنَادَ` [ن د و]; 68:33 `عَذَابُ` [ع ذ ب] and `يَعْلَمُ` [ع ل م]; surface anchors unavailable for roots `ن د ي` and `ب ل ل`.
- Synthesis: The supply is assembled across atmospheric, surface, and stored water. The “sweetness” branch of `ع ذ ب` provides a sharp latent reversal: the verse’s punishment stands lexically beside the desirable water whose loss makes deprivation tangible.

#### Subchannel B. Herds Cycle Between Trough, Pasture, and Return
- Reading type: latent/lexical
- Scene or process: Animals leave the watering place, graze nearby, return for another drink, and are held within a managed rhythm of release and rest.
- Active motifs: cycling herd between water and pasture (`quranic:root_001486:B006/m01`); repeated watering circuit (`quranic:root_001487:B004/m01`); re-entry to the trough (`quranic:root_000464:B007/m01`); watering at the animals’ mouths (`quranic:root_001198:B014/m01`); camels released to graze and drink (`quranic:root_000946:B006/m01`); camel that remains at its morning resting-place (`quranic:root_000839:B008/m01`); herd (`quranic:root_000532:B014/m03`).
- Ayah anchors: 68:19 `رَّبِّ` [ر ب ب]; 68:20/21 `أَصْبَحَتْ`/`مُصْبِحِينَ` [ص ب ح]; 68:21 `تَنَادَ` [ن د و]; 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:24 `يَدْخُلَ` [د خ ل]; 68:30 `أَقْبَلَ` [ق ب ل]; surface anchor unavailable for root `ن د ي`.
- Synthesis: Husbandry depends on regulated recurrence rather than one act of watering. Release, mouth-level watering, nearby grazing, re-entry, and morning rest define a complete circuit whose interruption produces loss without requiring the animal itself to disappear.

#### Subchannel C. Cessation Appears as Dry Rain, Cut Milk, and Denied Access
- Reading type: mixed
- Scene or process: Rain or milk stops, the final remnant is drawn, an animal or person waits for return, and deprivation names the failed flow.
- Active motifs: rain and milk cut off (`quranic:root_000305:B005/m01`); lactation severed (`quranic:root_000861:B006/m01`); final remnant at cessation (`quranic:root_000861:B007/m01`); waterless isolation (`quranic:root_000861:B010/m01`); hope that milk returns (`quranic:root_001015:B006/m01`); deprivation of provision (`quranic:root_000313:B008/m01`); beneficial wet provision (`quranic:root_000152:B002/m01`); recovery from depletion (`quranic:root_000152:B003/m01`).
- Ayah anchors: 68:17/20/22 forms of `ص ر م` [ص ر م]; 68:25 `حَرْدٍ` [ح ر د]; 68:27 `مَحْرُومُونَ` [ح ر م]; 68:32 `عَسَىٰ` [ع س ي]; surface anchor unavailable for root `ب ل ل`.
- Synthesis: Cessation is not one shortage. It can occur in sky, udder, last draw, isolated terrain, or gatekeeping. The hope in 68:32 is thereby materialized as the uncertain return of a life-sustaining flow.

### 12. [P2 68:17-33] An Unseen Night Passage Produces a Visible Morning State
- Semantic invariant: Concealment and stillness permit an event to pass around its target, after which morning makes the transformed condition visible.
- Surface relation: direct; 68:19 `طَافَ`/`نَآئِمُونَ`, 68:20 `أَصْبَحَتْ كَٱلصَّرِيمِ`, and 68:26 `رَأَ`.
- Surprising reach: The nocturnal event combines watch, encirclement, flood, dreamless stillness, blackening, and visual recognition into a temporal mechanism rather than a bare calamity.

#### Subchannel A. Garden, Night, and Sleep Layer Concealment
- Reading type: mixed
- Scene or process: Trees enclose the garden, night covers it, and sleeping occupants become still, trusting, and inattentive.
- Active motifs: sensory cover (`quranic:root_000266:B001/m02`); night covering in blackness (`quranic:root_000266:B002/m01`); enclosed garden (`quranic:root_000266:B003/m03`); sleep (`quranic:root_001568:B001/m01`); obscurity and heedlessness (`quranic:root_001568:B004/m01`); restful trust (`quranic:root_001568:B005/m01`); sleeping after dawn (`quranic:root_000839:B007/m01`); voice extinguished into deathlike silence (`quranic:root_000425:B002/m01`).
- Ayah anchors: 68:17 `جَنَّةِ` [ج ن ن]; 68:19 `نَآئِمُونَ` [ن و م]; 68:20/21 forms of `ص ب ح` [ص ب ح]; 68:23 `يَتَخَٰفَتُ` [خ ف ت].
- Synthesis: Four covers coincide: vegetation, darkness, sleep, and silence. Their joint effect is not guilt by association but scene construction: the owners cannot observe or answer the event while it acts.

#### Subchannel B. The Visitor Circles as Event, Watch, and Enclosure
- Reading type: mixed
- Scene or process: Something approaches and circles the orchard like a patrol or enclosing flood, traversing its perimeter while its occupants remain still.
- Active motifs: circling around a target (`quranic:root_000957:B001/m01`); encompassing flood or incident (`quranic:root_000957:B002/m02`); approaching apparition or event (`quranic:root_000957:B003/m01`); night watchman (`quranic:root_000957:B005/m01`); defensive perimeter wall (`quranic:root_000957:B010/m01`).
- Ayah anchors: 68:19 `طَافَ`/`طَآئِفٌ` [ط و ف].
- Synthesis: The visitor’s operation is spatially exact: approach, circuit, enclosure. The watchman sense reverses the expected function of patrol, since what circles under divine commission does not preserve the owners’ property regime.

#### Subchannel C. Blackened Ground Is Recognized at First Light
- Reading type: mixed
- Scene or process: The orchard becomes a black or bare cut surface; dawn lights it, and sight moves from mistaken location to recognized deprivation.
- Active motifs: black night, dawn, or burned barrenness (`quranic:root_000861:B004/m01`); calamity and impoverished state (`quranic:root_000861:B008/m01`); dawn (`quranic:root_000839:B001/m02`); lamp or light-source (`quranic:root_000839:B005/m01`); bright visible face or color (`quranic:root_000839:B006/m01`); change of state by morning (`quranic:root_000839:B010/m02`); direct sight (`quranic:root_000531:B001/m01`); visible appearance or mirror (`quranic:root_000531:B006/m01`); showing an object (`quranic:root_000531:B012/m01`); lost place (`quranic:root_000913:B003/m02`).
- Ayah anchors: 68:17/20/22 forms of `ص ر م` [ص ر م]; 68:17/20/21 forms of `ص ب ح` [ص ب ح]; 68:26 `رَأَ` [ر ء ي] and `ضَآلُّونَ` [ض ل ل].
- Synthesis: Morning does not merely follow destruction; it performs disclosure. Light meets a surface transformed by cutting or burning, and the owners’ visual error is corrected into recognition of loss.

### 13. [P2 68:17-33] Boundary Operations Decide What Remains Inside the Whole
- Semantic invariant: Folding, exception, enclosure, entry, binding, and release all alter membership in a bounded whole.
- Surface relation: direct; 68:18 `يَسْتَثْنُ`, 68:24 `يَدْخُلَ`/`مِّسْكِينٌ`, and 68:27 `مَحْرُومُونَ`.
- Surprising reach: The exclusion of the poor is represented as a general boundary technology: a whole can be folded, have a portion excepted, be walled, or be opened by release.

#### Subchannel A. Folding and Exception Remove a Portion from the Whole
- Reading type: mixed
- Scene or process: One item is doubled, repeated, folded back, or explicitly removed from the rule governing the surrounding set.
- Active motifs: joining a second to a first (`quranic:root_000208:B001/m01`); repeated operation (`quranic:root_000208:B003/m01`); folding or turning aside (`quranic:root_000208:B005/m01`); exception from a general rule (`quranic:root_000208:B008/m01`); allotted portion (`quranic:root_001226:B003/m02`); part opposed to whole (`quranic:root_000133:B001/m01`); group or piece (`quranic:root_000957:B004/m01`); cut portion (`quranic:root_000861:B005/m02`).
- Ayah anchors: 68:17 `أَقْسَمُ` [ق س م] and `يَصْرِمُ` [ص ر م]; 68:18 `يَسْتَثْنُ` [ث ن ي]; 68:19 `طَآئِفٌ` [ط و ف]; 68:30 `بَعْضُ`/`بَعْضٍ` [ب ع ض].
- Synthesis: Exception is materially modeled by the fold: a portion is turned out of the common line and separately treated. The repeated, doubled, allotted, and cut senses distinguish several operations that can produce an excluded part.

#### Subchannel B. Enclosure, Interior, and Poverty at the Gate
- Reading type: mixed
- Scene or process: A protected domain has an inside, a surrounding right, and an entry point; concealed corruption can occupy the same interior while a poor entrant is barred.
- Active motifs: protected prohibition (`quranic:root_000313:B001/m01`); spatial sanctuary and perimeter rights (`quranic:root_000313:B003/m01`); inviolable claim (`quranic:root_000313:B006/m01`); deprived claimant (`quranic:root_000313:B008/m02`); entry into an interior (`quranic:root_000464:B001/m01`); hidden interior (`quranic:root_000464:B003/m01`); concealed corruption (`quranic:root_000464:B004/m01`); inhabited dwelling (`quranic:root_000726:B002/m01`); household occupants (`quranic:root_000726:B003/m01`); poverty and abasement (`quranic:root_000726:B006/m01`); stable place (`quranic:root_000726:B009/m01`).
- Ayah anchors: 68:24 `يَدْخُلَ` [د خ ل] and `مِّسْكِينٌ` [س ك ن]; 68:27 `مَحْرُومُونَ` [ح ر م].
- Synthesis: The orchard is a jurisdiction as well as a garden. Rights define its perimeter, entry controls its interior, residents enjoy stability, and the poor person appears precisely where a property boundary becomes an ethical decision.

#### Subchannel C. Release and Constraint Reverse One Another
- Reading type: latent/lexical
- Scene or process: A bound body, legal condition, or guarded thing is either kept under restraint or sent out without remaining liability.
- Active motifs: release from fetter (`quranic:root_000946:B001/m01`); unrestricted permission (`quranic:root_000946:B005/m01`); leather bond or short rope (`quranic:root_000946:B012/m01`); withdrawal from the group (`quranic:root_000305:B004/m01`); preventing or weaning away (`quranic:root_000994:B003/m01`); discursive break and restart (`quranic:root_000152:B008/m01`).
- Ayah anchors: 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:25 `حَرْدٍ` [ح ر د]; 68:33 `عَذَابُ` [ع ذ ب]; surface anchor unavailable for root `ب ل ل`.
- Synthesis: Constraint and release are inverse boundary operations. A rope keeps the body within a range, law can remove prohibition, withdrawal moves a participant outside the group, and `بَل` cuts one discourse-state to begin another.

### 14. [P2 68:17-33] Group Speech Reconfigures the Speakers
- Semantic invariant: Collective identity changes as speech moves from summons and secrecy to confrontation, mediation, confession, and blame.
- Surface relation: direct; 68:21 `تَنَادَ`, 68:23 `يَتَخَٰفَتُ`, 68:28-31 repeated `قَالَ`/`قَالُ`, 68:28 `أَوْسَطُ`, and 68:30 `أَقْبَلَ`/`بَعْضُ`/`يَتَلَٰوَمُ`.
- Surprising reach: Speech does not merely narrate the owners’ change; its forms reorganize them from a coordinated bloc into facing parts with a middle voice and shared admission.

#### Subchannel A. Public Summons Contracts into Secret Consultation
- Reading type: surface-primary
- Scene or process: A call gathers a council, but the coordinated group lowers its voice and carries part of its plan as unspoken interior speech.
- Active motifs: council or assembly (`quranic:root_001486:B001/m01`); raised summons (`quranic:root_001486:B002/m01`); public call (`quranic:root_001487:B001/m01`); gathering place (`quranic:root_001487:B003/m01`); lowered secret consultation (`quranic:root_000425:B001/m01`); articulated statement (`quranic:root_001272:B001/m02`); deliberative exchange (`quranic:root_001272:B009/m01`); unspoken interior statement (`quranic:root_001272:B012/m02`).
- Ayah anchors: 68:21 `تَنَادَ` [ن د و]; 68:23 `يَتَخَٰفَتُ` [خ ف ت]; 68:26/28/29/31 forms of `ق و ل` [ق و ل]; surface anchor unavailable for root `ن د ي`.
- Synthesis: The voice changes scale: call creates the assembly, consultation coordinates it, whisper limits the audience, and internal statement withholds content entirely. Each operation modifies who participates in the plan.

#### Subchannel B. Facing Parts Exchange Blame
- Reading type: surface-primary
- Scene or process: Former collaborators turn toward one another as distinct parts, exchange accusations, and delay over fault.
- Active motifs: face-to-face encounter (`quranic:root_001198:B001/m01`); group or tribe facing inward (`quranic:root_001198:B009/m01`); part opposed to part (`quranic:root_000133:B001/m02`); deserved blame and reciprocal reproach (`quranic:root_001386:B001/m01`); delay before action (`quranic:root_001386:B002/m01`); report circulating among the group (`quranic:root_001272:B007/m03`).
- Ayah anchors: 68:28/29/31 forms of `ق و ل` [ق و ل]; 68:30 `أَقْبَلَ` [ق ب ل], `بَعْضُ`/`بَعْضٍ` [ب ع ض], and `يَتَلَٰوَمُ` [ل و م].
- Synthesis: The group’s geometry changes with its discourse. Facing replaces marching in one direction, “some” partitions the collective, and reciprocal blame sustains the new opposition.

#### Subchannel C. The Middle Voice Mediates Confession and Reorientation
- Reading type: mixed
- Scene or process: A central participant occupies a just mediating position, recalls omitted worship, and redirects the group toward exoneration and redress.
- Active motifs: just and best center (`quranic:root_001646:B001/m01`); spatial middle (`quranic:root_001646:B002/m01`); entry into the middle (`quranic:root_001646:B003/m01`); mediation between parties (`quranic:root_001646:B005/m01`); worship and thanksgiving (`quranic:root_000666:B001/m01`); exoneration from wrong (`quranic:root_000666:B002/m01`); sincere care in speech (`quranic:root_001272:B015/m01`); grievance and request for justice (`quranic:root_000967:B003/m01`); withholding another’s right (`quranic:root_000967:B008/m01`).
- Ayah anchors: 68:28 `أَوْسَطُ` [و س ط], `تُسَبِّحُ` [س ب ح], and `قَالَ`/`أَقُل` [ق و ل]; 68:29 `سُبْحَٰنَ` [س ب ح] and `ظَٰلِمِينَ` [ظ ل م].
- Synthesis: “The middle one” is both a location and a social function. Mediation interrupts mutual blame, and exonerating God permits the group to relocate wrong in its own withheld rights and conduct.

#### Subchannel D. A Cohesive Group Fragments into Portions
- Reading type: latent/lexical
- Scene or process: A formerly assembled body scatters, becomes factions or isolated pieces, and loses the prestige that held it together.
- Active motifs: people scattered in directions (`quranic:root_000153:B009/m01`); dispersal and disarray (`quranic:root_000154:B008/m01`); cut-off tract or group (`quranic:root_000861:B005/m03`); faction or fragment (`quranic:root_000957:B004/m02`); divided attention (`quranic:root_001226:B006/m01`); fall of inherited status (`quranic:root_001281:B005/m01`).
- Ayah anchors: 68:17 `بَلَوْ` [ب ل و], `أَقْسَمُ` [ق س م], and `يَصْرِمُ` [ص ر م]; 68:19 `طَآئِفٌ` [ط و ف]; 68:33 `أَكْبَرُ` [ك ب ر]; surface anchor unavailable for root `ب ل ي`.
- Synthesis: Fragmentation is the social analogue of harvest-cutting. The group that jointly planned exclusion is itself rendered into scattered portions, with status no longer functioning as cohesion.

### 15. [P2 68:17-33] Purposeful Motion Turns into Disorientation
- Semantic invariant: Intention becomes effective only when plan, capacity, route, bodily movement, and recognition remain aligned.
- Surface relation: direct; 68:22 `ٱغْدُ`, 68:23 `ٱنطَلَقُ`, 68:25 `حَرْدٍ قَٰدِرِينَ`, and 68:26 `رَأَ`/`ضَآلُّونَ`.
- Surprising reach: The owners’ confident departure is anatomized into distinct failure points: crooked gait, wrong direction, insufficient capacity, or a seeing that cannot identify its own destination.

#### Subchannel A. Intent Is Calculated Before the Body Moves
- Reading type: mixed
- Scene or process: A goal is selected, deliberated, measured against capacity, and converted into an operational plan.
- Active motifs: directed intent and effort (`quranic:root_000305:B001/m01`); anger energizing intent (`quranic:root_000305:B003/m01`); reflective judgment (`quranic:root_000531:B002/m01`); ability and possession (`quranic:root_001205:B003/m01`); planning by measure (`quranic:root_001205:B005/m02`); proportioned fit (`quranic:root_001205:B006/m01`); divided deliberation (`quranic:root_001226:B006/m02`); cultivated knowledge (`quranic:root_000532:B003/m02`).
- Ayah anchors: 68:19 `رَّبِّ` [ر ب ب]; 68:25 `حَرْدٍ` [ح ر د] and `قَٰدِرِينَ` [ق د ر]; 68:26 `رَأَ` [ر ء ي]; 68:17 `أَقْسَمُ` [ق س م].
- Synthesis: Purpose is not identical with capacity. Anger can intensify intention, but deliberation, proportion, knowledge, and actual ability must still agree before the plan can reach its object.

#### Subchannel B. Departure Tests Route, Gait, and Capacity to Confront
- Reading type: mixed
- Scene or process: Travelers set out freely toward a direction; ease of weather and body may accelerate them, while crooked gait or rough movement disturbs the approach.
- Active motifs: unimpeded departure (`quranic:root_000946:B003/m01`); open face and ease (`quranic:root_000946:B004/m01`); benign travel-time (`quranic:root_000946:B007/m01`); morning movement (`quranic:root_001076:B001/m02`); direction or source (`quranic:root_001198:B003/m01`); capacity to face a force (`quranic:root_001198:B013/m01`); disturbed heavy gait (`quranic:root_000305:B006/m01`); crooked line or building (`quranic:root_000305:B007/m01`).
- Ayah anchors: 68:22 `ٱغْدُ` [غ د و]; 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:25 `حَرْدٍ` [ح ر د]; 68:30 `أَقْبَلَ` [ق ب ل].
- Synthesis: The departure scene distinguishes freedom to leave from ability to arrive. Direction, weather, bodily gait, and confrontational capacity can support or defeat the same declared intention.

#### Subchannel C. Sight Corrects the Mistaken Destination
- Reading type: mixed
- Scene or process: The travelers fail to locate what they expect, confront its altered appearance, and move from ocular registration to corrected understanding.
- Active motifs: moral and spatial deviation (`quranic:root_000913:B001/m02`); missing object or place (`quranic:root_000913:B003/m03`); ownerless stray (`quranic:root_000913:B005/m02`); eye and inward sight (`quranic:root_000531:B001/m02`); reciprocal visibility (`quranic:root_000531:B004/m01`); appearance in a reflective surface (`quranic:root_000531:B006/m02`); attention-seeking “tell me” (`quranic:root_000531:B013/m01`); grasping what has come into hand (`quranic:root_000152:B004/m01`).
- Ayah anchors: 68:26 `رَأَ` [ر ء ي] and `ضَآلُّونَ` [ض ل ل]; surface anchor unavailable for root `ب ل ل`.
- Synthesis: “We are lost” first names a mismatch between map and visible place. The progression from absent object to altered appearance and finally recognition keeps spatial disorientation distinct from the moral realization that follows.

### 16. [P2 68:17-33] Oaths Allocate Risk, Exception, and Protection
- Semantic invariant: A spoken commitment binds parties only through its scope, reservation, guarantor, and protected rights.
- Surface relation: direct; 68:17 `أَقْسَمُ`, 68:18 `يَسْتَثْنُ`, and 68:19/29/32 `رَّبِّ`/`رَبِّ`/`رَبُّ`.
- Surprising reach: The owners’ oath is lexically surrounded by legal mechanisms that they suppress: exception, distributed liability, truce, surety, companionship, and inviolable claim.

#### Subchannel A. A Sworn Commitment Can Carry a Reservation
- Reading type: surface-primary
- Scene or process: A group divides and voices an oath; an explicit exception can remove a condition or share from its otherwise binding scope.
- Active motifs: sworn oath (`quranic:root_001226:B004/m01`); exception in oath or sale (`quranic:root_000208:B008/m02`); publicly offered oath as test (`quranic:root_000153:B004/m01`); oath offered for reassurance (`quranic:root_000154:B005/m01`); oath-binding (`quranic:root_000076:B007/m01`).
- Ayah anchors: 68:17 `بَلَوْ` [ب ل و] and `أَقْسَمُ` [ق س م]; 68:18 `يَسْتَثْنُ` [ث ن ي]; surface anchors unavailable for roots `ب ل ي` and `ء ل ي`.
- Synthesis: Reservation is part of the oath’s architecture, not an afterthought. By refusing it, the speakers present a totalized commitment that leaves no verbal opening for contingency or another claimant.

#### Subchannel B. Treaty, Surety, and Companionship Carry Protected Rights
- Reading type: latent/lexical
- Scene or process: Truce restrains conflict, a surety bears liability, covenant defines inviolable rights, and a companion preserves the person under care.
- Active motifs: truce (`quranic:root_001226:B008/m01`); protected time without fighting (`quranic:root_000313:B005/m01`); inviolable right and guarantee (`quranic:root_000313:B006/m02`); surety and written undertaking (`quranic:root_001198:B008/m01`); covenant (`quranic:root_000532:B011/m02`); companionship and charge (`quranic:root_000844:B001/m01`); preservation through companionship (`quranic:root_000844:B002/m01`).
- Ayah anchors: 68:17 `أَصْحَٰبَ` [ص ح ب] and `أَقْسَمُ` [ق س م]; 68:19/29/32 forms of `ر ب ب` [ر ب ب]; 68:27 `مَحْرُومُونَ` [ح ر م]; 68:30 `أَقْبَلَ` [ق ب ل].
- Synthesis: Obligation distributes vulnerability. Truce protects time, covenant protects relation, surety carries another’s burden, and companionship protects a person; the owners’ compact instead concentrates protection inside their own group.

### 17. [P2 68:17-33] Excess Crosses Its Limit and Returns as Overwhelming Force
- Semantic invariant: What rises beyond measure becomes a material or political overflow whose return is loss, domination, or punishment.
- Surface relation: direct; 68:29 `ظَٰلِمِينَ`, 68:31 `طَٰغِينَ`, and 68:33 `عَذَابُ`/`أَكْبَرُ`.
- Surprising reach: Moral excess shares a shape with floodwater, raised terrain, tyrannical rule, and a burden too large to carry; judgment is the reversal of uncontrolled magnitude.

#### Subchannel A. Transgression Behaves Like Floodwater
- Reading type: mixed
- Scene or process: Conduct exceeds its channel as water rises above its banks, sweeps material away, and deposits it where it does not belong.
- Active motifs: crossing the limit in rebellion (`quranic:root_000937:B001/m01`); surging water or force (`quranic:root_000937:B002/m01`); rebellious excess (`quranic:root_000936:B001/m01`); flooding water or blood (`quranic:root_000936:B002/m01`); action put in the wrong place or time (`quranic:root_000967:B004/m01`); growth extending beyond its origin (`quranic:root_000967:B007/m01`); rights withheld (`quranic:root_000967:B008/m02`).
- Ayah anchors: 68:29 `ظَٰلِمِينَ` [ظ ل م]; 68:31 `طَٰغِينَ` [ط غ ي]; surface anchor unavailable for root `ط غ و`.
- Synthesis: Excess is given hydraulic shape. It rises, exceeds its channel, and relocates material improperly, making “we were transgressors” a diagnosis of uncontrolled flow as well as unlawful conduct.

#### Subchannel B. The False Head Converts Excess into Rule and Disaster
- Reading type: latent/lexical
- Scene or process: A misleading head claims authority, becomes a coercive ruler, and brings an overwhelming punitive event upon the group.
- Active motifs: head of misguidance (`quranic:root_000937:B003/m01`); smooth high rock (`quranic:root_000937:B005/m01`); false sacred head (`quranic:root_000936:B003/m01`); coercive tyrant (`quranic:root_000936:B004/m01`); overwhelming punitive event (`quranic:root_000936:B005/m01`); inherited leadership and rank (`quranic:root_001281:B005/m02`); arrogant greatness (`quranic:root_001281:B006/m01`).
- Ayah anchors: 68:31 `طَٰغِينَ` [ط غ ي]; 68:33 `أَكْبَرُ` [ك ب ر]; surface anchor unavailable for root `ط غ و`.
- Synthesis: Excess can be institutionalized in a head who directs others. The lexical reversal is exact: the figure who rises above the group is answered by a force that rises beyond that ruler’s control.

#### Subchannel C. Punishment Is Pain Made Larger and Later
- Reading type: mixed
- Scene or process: Harm becomes a severe penalty; its later form exceeds the present event in size, burden, and consequence.
- Active motifs: severe inflicted punishment (`quranic:root_000994:B005/m01`); magnitude (`quranic:root_001281:B001/m01`); inward apprehension of greatness (`quranic:root_001281:B003/m01`); grave wrongdoing (`quranic:root_001281:B007/m01`); crushing difficulty (`quranic:root_001281:B010/m01`); later term (`quranic:root_000019:B001/m01`); postponement (`quranic:root_000019:B002/m01`); disclosed knowledge (`quranic:root_001040:B001/m02`).
- Ayah anchors: 68:33 `عَذَابُ` [ع ذ ب], `ءَاخِرَةِ` [ء خ ر], `أَكْبَرُ` [ك ب ر], and `يَعْلَمُ` [ع ل م].
- Synthesis: The verse’s comparison is mechanized by four axes: pain, size, burden, and temporal deferral. “Greater” therefore denotes not a vague intensifier but a later penalty whose weight and consequence exceed the orchard event.

### 18. [P2 68:17-33] Loss Reorients Desire Toward Replacement and Repair
- Semantic invariant: After deprivation, hope becomes a directed search for a substitute that restores function and exceeds the lost provision.
- Surface relation: direct; 68:27 `مَحْرُومُونَ` and 68:32 `عَسَىٰ`/`يُبْدِلَ`/`خَيْرًا`/`رَٰغِبُونَ`.
- Surprising reach: Replacement is not a reset: it can change only outward form, occupy another’s place, restore a depleted flow, or answer desire with a more generous provision.

#### Subchannel A. Substitution and Repair Restore a Failed Function
- Reading type: mixed
- Scene or process: One thing takes another’s place or changes form; tending and recovery seek to make the replacement function better than what failed.
- Active motifs: substitute occupying another’s place (`quranic:root_000095:B001/m01`); changed form (`quranic:root_000095:B002/m01`); gradual repair (`quranic:root_000532:B002/m04`); recovery after wasting (`quranic:root_000152:B003/m02`); selection of the better option (`quranic:root_000452:B003/m01`); compatibility through association (`quranic:root_000844:B004/m01`).
- Ayah anchors: 68:17 `أَصْحَٰبَ` [ص ح ب]; 68:19/29/32 forms of `ر ب ب` [ر ب ب]; 68:32 `يُبْدِلَ` [ب د ل] and `خَيْرًا` [خ ي ر]; surface anchor unavailable for root `ب ل ل`.
- Synthesis: Replacement has two distinct operations: exchange the occupant, or transform the existing form. Repair and compatibility then test whether the new arrangement truly restores the broken function.

#### Subchannel B. Directed Desire Seeks a More Generous Provision
- Reading type: mixed
- Scene or process: Desire turns toward a chosen good whose spaciousness and generosity answer the constriction of loss.
- Active motifs: desire directed toward or away (`quranic:root_000575:B001/m01`); spacious capacity (`quranic:root_000575:B002/m01`); abundant desirable gift (`quranic:root_000575:B004/m01`); beneficial good (`quranic:root_000452:B001/m02`); selected excellence (`quranic:root_000452:B002/m02`); generosity (`quranic:root_000452:B005/m02`); hope of returning milk (`quranic:root_001015:B006/m02`); favor and need answered (`quranic:root_000532:B016/m02`).
- Ayah anchors: 68:32 `خَيْرًا` [خ ي ر]; 68:29/32 forms of `ر ب ب` [ر ب ب]; 68:32 `عَسَىٰ` [ع س ي] and `رَٰغِبُونَ` [ر غ ب].
- Synthesis: Desire is directional and capacious. It leaves the destroyed object, turns toward the giver, and asks not merely for equivalence but for a more spacious, generous, and durable good.

### 19. [P2 68:17-33] Folding and Joining Build Portable or Fixed Enclosures
- Semantic invariant: Boundaries are made by folding flexible material, fastening parts, or raising a perimeter around a protected interior.
- Surface relation: indirect; 68:18 `يَسْتَثْنُ`, 68:19 `طَافَ`, 68:24 `يَدْخُلَ`, and 68:27 `مَحْرُومُونَ`.
- Surprising reach: Logical exception and property exclusion share a craft image: a fold or wall redirects a portion away from common access.

#### Subchannel A. Folded Cloth and Palm Fiber Make a Container
- Reading type: latent/lexical
- Scene or process: Cloth is folded, doubled with cord, cut into a piece, and joined to palm fiber or straps to hold a harvest.
- Active motifs: fold of cloth or book (`quranic:root_000208:B005/m02`); doubled-ended rope (`quranic:root_000208:B007/m01`); first fold of cloth (`quranic:root_001226:B007/m01`); cloth-piece (`quranic:root_000957:B004/m03`); woven palm basket (`quranic:root_000464:B010/m02`); joined straps and patches (`quranic:root_001198:B010/m01`).
- Ayah anchors: 68:17 `أَقْسَمُ` [ق س م]; 68:18 `يَسْتَثْنُ` [ث ن ي]; 68:19 `طَآئِفٌ` [ط و ف]; 68:24 `يَدْخُلَ` [د خ ل]; 68:30 `أَقْبَلَ` [ق ب ل].
- Synthesis: The portable enclosure is assembled through operations, not motifs piled by topic: fold, double, cut, weave, and join. It converts a flat surface into a volume capable of holding produce.

#### Subchannel B. Wall, Sanctuary, and Raft Define an Interior by Perimeter
- Reading type: latent/lexical
- Scene or process: A wall circles a place, sacred rights thicken its boundary, and lashed timbers can carry a bounded platform over water.
- Active motifs: perimeter wall (`quranic:root_000957:B010/m02`); circling a bounded place (`quranic:root_000957:B001/m02`); lashed raft (`quranic:root_000957:B006/m01`); sanctuary and surrounding rights (`quranic:root_000313:B003/m02`); interior entry (`quranic:root_000464:B001/m02`); rudder stabilizing a vessel (`quranic:root_000726:B008/m01`).
- Ayah anchors: 68:19 `طَافَ`/`طَآئِفٌ` [ط و ف]; 68:24 `يَدْخُلَ` [د خ ل] and `مِّسْكِينٌ` [س ك ن]; 68:27 `مَحْرُومُونَ` [ح ر م].
- Synthesis: Fixed wall and floating raft share a perimeter principle: joined material produces a stable inside despite pressure from outside. Sanctuary adds the social right that makes such a boundary more than construction.

### 20. [P2 68:17-33] Worship Redirects Blame into Redress and Giving
- Semantic invariant: Corrective speech exonerates the giver, acknowledges wrong, and restores outward movement through worship, acceptance, and generosity.
- Surface relation: direct; 68:28 `تُسَبِّحُ`, 68:29 `سُبْحَٰنَ رَبِّ`/`ظَٰلِمِينَ`, and 68:32 `رَبُّ`/`خَيْرًا`/`رَٰغِبُونَ`.
- Surprising reach: Praise is not isolated ritual language; it changes the social direction of goods by replacing exclusion and self-justification with accepted fault, protected relation, and largesse.

#### Subchannel A. Praise, Prayer, and Orientation Reorder the Group
- Reading type: surface-primary
- Scene or process: Participants turn toward a worship center, pray or praise, and separate the divine giver from the wrong they committed.
- Active motifs: prayer, worship, and thanksgiving (`quranic:root_000666:B001/m02`); exoneration and transcendence (`quranic:root_000666:B002/m02`); direction of prayer (`quranic:root_001198:B005/m01`); sacred precinct (`quranic:root_000313:B003/m03`); central position (`quranic:root_001646:B002/m02`); proportioned middle (`quranic:root_001205:B006/m02`).
- Ayah anchors: 68:25 `قَٰدِرِينَ` [ق د ر]; 68:27 `مَحْرُومُونَ` [ح ر م]; 68:28/29 `تُسَبِّحُ`/`سُبْحَٰنَ` [س ب ح]; 68:28 `أَوْسَطُ` [و س ط]; 68:30 `أَقْبَلَ` [ق ب ل].
- Synthesis: Worship spatially and morally reorients the speakers. A common center replaces their closed property-direction, and exoneration distinguishes divine provision from their own disordered use of it.

#### Subchannel B. Generosity Reopens the Arrested Flow
- Reading type: mixed
- Scene or process: Good deed, recovery, gift, and largesse move provision outward after deprivation has exposed the harm of enclosure.
- Active motifs: excellent benefaction (`quranic:root_000153:B003/m01`); witnessed good deed (`quranic:root_000154:B003/m01`); recovery and welfare (`quranic:root_000152:B003/m03`); generosity (`quranic:root_000452:B005/m03`); abundant gift (`quranic:root_000575:B004/m02`); gracious provision (`quranic:root_000532:B016/m03`); noble character (`quranic:root_000994:B008/m01`); dew-like giving (`quranic:root_001486:B004/m01`); generous hand (`quranic:root_001487:B008/m01`).
- Ayah anchors: 68:17 `بَلَوْ` [ب ل و]; 68:19/29/32 forms of `ر ب ب` [ر ب ب]; 68:21 `تَنَادَ` [ن د و]; 68:32 `خَيْرًا` [خ ي ر] and `رَٰغِبُونَ` [ر غ ب]; 68:33 `عَذَابُ` [ع ذ ب]; surface anchors unavailable for roots `ب ل ي`, `ب ل ل`, and `ن د ي`.
- Synthesis: Generosity is the inverse of the owners’ plan at the level of flow. It converts possession into outward provision, while good deed and recovery show that giving can restore both social relation and material condition.

#### Subchannel C. Admission Opens a Claim for Redress
- Reading type: mixed
- Scene or process: A wronged or self-correcting party names the misplacement, accepts blame, and seeks an accepted replacement rather than defending the prior claim.
- Active motifs: grievance seeking justice (`quranic:root_000967:B003/m02`); wrong placement or timing (`quranic:root_000967:B004/m02`); accepted excuse or repentance (`quranic:root_001198:B004/m01`); mutual blame (`quranic:root_001386:B001/m02`); exonerating correction (`quranic:root_000666:B002/m03`); leaving or preventing a harmful course (`quranic:root_000994:B003/m02`).
- Ayah anchors: 68:28/29 `تُسَبِّحُ`/`سُبْحَٰنَ` [س ب ح]; 68:29 `ظَٰلِمِينَ` [ظ ل م]; 68:30 `أَقْبَلَ` [ق ب ل] and `يَتَلَٰوَمُ` [ل و م]; 68:33 `عَذَابُ` [ع ذ ب].
- Synthesis: Confession becomes operative when it moves beyond self-reproach. Exoneration locates responsibility, acceptance receives the corrected claim, and redress directs the speakers toward a different future provision.

### 21. [P2 68:17-33] Life-Cycle Thresholds Can Be Nurtured or Arrested
- Semantic invariant: Birth, maturation, lactation, and death are thresholds whose continuation depends on care, release, and supply.
- Surface relation: indirect; 68:17 `بَلَوْ`/`أَصْحَٰبَ`, 68:19 `نَآئِمُونَ`, 68:22 `ٱغْدُ`, and 68:32 `عَسَىٰ`.
- Surprising reach: The threatened orchard is mirrored by animal and human life cycles: fetus, labor, midwife, milk, grave, and death each show growth either brought through a threshold or deliberately stopped.

#### Subchannel A. Fetus, Labor, and Reception at Birth
- Reading type: latent/lexical
- Scene or process: A concealed fetus reaches labor, the body opens under pain, and an attendant receives the newborn into social care.
- Active motifs: fetus hidden in the womb (`quranic:root_000266:B007/m01`); dependent child under care (`quranic:root_000532:B005/m01`); labor pain (`quranic:root_000946:B008/m01`); abdominal release (`quranic:root_000946:B009/m01`); inner bodily channels (`quranic:root_000946:B017/m01`); afterbirth and womb (`quranic:root_000994:B009/m01`); unborn livestock (`quranic:root_001076:B005/m01`); midwife receiving the child (`quranic:root_001198:B007/m01`).
- Ayah anchors: 68:17 `جَنَّةِ` [ج ن ن]; 68:19/29/32 forms of `ر ب ب` [ر ب ب]; 68:22/25 forms of `غ د و` [غ د و]; 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:30 `أَقْبَلَ` [ق ب ل]; 68:33 `عَذَابُ` [ع ذ ب].
- Synthesis: Birth is a multi-role transition: concealed occupant, laboring body, opening passage, expelled afterbirth, and receiving attendant. It gives precise biological content to the pericope’s concern with whether a hoped-for yield reaches completion.

#### Subchannel B. The Grave-Camel Makes Arrested Care Visible
- Reading type: latent/lexical
- Scene or process: A camel is tied at its owner’s grave, denied food and water until death, while related senses register stopped milk, immobility, and the end of productive life.
- Active motifs: grave-camel left to die (`quranic:root_000153:B005/m01`); tethered burial animal (`quranic:root_000154:B006/m01`); milk and rain stopped (`quranic:root_000305:B005/m02`); camel remaining down at morning (`quranic:root_000839:B008/m02`); grazing camel otherwise released (`quranic:root_000946:B006/m02`); death or killing figured as sleep (`quranic:root_001568:B008/m01`); burial cover (`quranic:root_000266:B009/m01`).
- Ayah anchors: 68:17 `بَلَوْ` [ب ل و] and `جَنَّةِ` [ج ن ن]; 68:17/20/21 forms of `ص ب ح` [ص ب ح]; 68:19 `نَآئِمُونَ` [ن و م]; 68:23 `ٱنطَلَقُ` [ط ل ق]; 68:25 `حَرْدٍ` [ح ر د]; surface anchor unavailable for root `ب ل ي`.
- Synthesis: The grave-camel is a complete counter-husbandry scene: binding replaces release, fasting replaces pasture, and death replaces yield. It intensifies the orchard narrative’s exposure of possession severed from sustaining care.

### 22. [P3 68:34-52] Protected Growth Turns Cover into Provision
- Semantic invariant: A productive enclosure protects living growth long enough for seed, plant, fruit, animal, and human occupant to reach a beneficial state.
- Surface relation: direct; 68:34 `مُتَّقِينَ`/`جَنَّٰتِ`/`نَّعِيمِ`, 68:35 `نَجْعَلُ`/`مُسْلِمِينَ`, and 68:49 `نِعْمَةٌ`.
- Surprising reach: Paradise is lexically materialized as shield, tree-cover, seed-cover, fruit husk, cultivated field, and usable tree product; protection is productive rather than merely defensive.

#### Subchannel A. Shielded Garden Gives Its Occupant Ease
- Reading type: mixed
- Scene or process: A protective barrier and dense tree-cover preserve an interior where the occupant can remain sound, settled, and well-provisioned.
- Active motifs: barrier against harm (`quranic:root_001677:B001/m01`); self placed in protection (`quranic:root_001677:B002/m01`); tree-covered garden (`quranic:root_000266:B003/m04`); protective shield (`quranic:root_000266:B008/m03`); soundness from defect (`quranic:root_000737:B001/m01`); favor and good condition (`quranic:root_001525:B001/m02`); softness and ease (`quranic:root_001525:B002/m02`); congenial place of residence (`quranic:root_001525:B011/m01`); lordship over the protected domain (`quranic:root_000532:B001/m02`); gracious provision (`quranic:root_000532:B016/m04`).
- Ayah anchors: 68:34 `مُتَّقِينَ` [و ق ي], `رَبِّ` [ر ب ب], `جَنَّٰتِ` [ج ن ن], and `نَّعِيمِ` [ن ع م]; 68:35 `مُسْلِمِينَ` [س ل م].
- Synthesis: Protection is an enabling environment. Barrier and tree-cover preserve soundness, while ease and congenial residence name the state made possible inside; the “gardens of delight” therefore join enclosure to sustained flourishing.

#### Subchannel B. Seed-Cover and Fruit-Husk Guard Development
- Reading type: latent/lexical
- Scene or process: Seed is covered in soil, new vegetation thickens, a fruit remains sheathed until ripe, and the yield emerges from its protected stage.
- Active motifs: covering seed with soil (`quranic:root_001307:B008/m01`); fruit or palm sheath (`quranic:root_001307:B010/m01`); dense plant growth (`quranic:root_000266:B011/m03`); ripe pasture or fruit ready for use (`quranic:root_000956:B007/m01`); young palms (`quranic:root_000248:B006/m01`); strong male plant (`quranic:root_000516:B002/m01`); crop yield and fruit (`quranic:root_000009:B007/m01`); persistent green growth (`quranic:root_000532:B012/m03`).
- Ayah anchors: 68:34 `رَبِّ` [ر ب ب] and `جَنَّٰتِ` [ج ن ن]; 68:35 `نَجْعَلُ` [ج ع ل]; 68:41 `يَأْتُ` [ء ت ي]; 68:42 `يَسْتَطِيعُ` [ط و ع]; 68:51 `كَفَرُ` [ك ف ر] and `ذِّكْرَ` [ذ ك ر].
- Synthesis: Cover is stage-specific rather than absolute concealment. Soil and husk protect what is not ready; ripening and emerging yield then convert the covered potential into accessible provision.

#### Subchannel C. Cultivation Produces Food, Fiber, Tannin, and Scent
- Reading type: latent/lexical
- Scene or process: Fields are threshed and plowed; trees yield tanning material and aromatic substance that pass from ecology into craft and use.
- Active motifs: threshing grain underfoot (`quranic:root_000470:B005/m01`); long plow implements (`quranic:root_000741:B015/m01`); tanning tree and bark (`quranic:root_000737:B008/m01`); camphor as plant and perfume (`quranic:root_001307:B011/m01`); green tanning shrub (`quranic:root_000076:B005/m01`); gathered produce (`quranic:root_000009:B007/m02`).
- Ayah anchors: 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:37 `تَدْرُسُ` [د ر س]; 68:41 `يَأْتُ` [ء ت ي]; 68:51 `سَمِعُ` [س م ع] and `كَفَرُ` [ك ف ر]; surface anchor unavailable for root `ء ل ي`.
- Synthesis: The garden’s yield extends beyond fruit. Threshing, plow, bark, tannin, and perfume show cultivation feeding both body and craft, while the unavailable `ء ل ي` anchor remains a purely lexical plant contribution.

### 23. [P3 68:34-52] Claims Become Durable Through Text, Judgment, and Guarantee
- Semantic invariant: A claim acquires force when it is assembled into a durable record, interpreted under judgment, and backed by a responsible party.
- Surface relation: direct; 68:36 `تَحْكُمُ`, 68:37 `كِتَٰبٌ`/`تَدْرُسُ`, 68:39 `أَيْمَٰنٌ`/`بَٰلِغَةٌ`/`تَحْكُمُ`, 68:40 `سَلْ`/`زَعِيمٌ`, and 68:41 `شُرَكَآءُ`/`صَٰدِقِينَ`.
- Surprising reach: The polemical questions expose a complete documentary institution: material joining, written decree, study, scope, oath, guarantor, partner, fulfillment, and adjudication.

#### Subchannel A. Joining Material Becomes Writing, Decree, and Register
- Reading type: mixed
- Scene or process: Separate pieces are joined like stitched leather, letters are ordered into a record, and the record fixes a decree or enters a name in an official register.
- Active motifs: joining and stitching (`quranic:root_001283:B001/m01`); written record (`quranic:root_001283:B002/m01`); binding decree (`quranic:root_001283:B003/m01`); entry into register or class (`quranic:root_001283:B004/m01`); erased trace (`quranic:root_000470:B001/m01`); repeated study and memorization (`quranic:root_000470:B002/m01`); worn book-like material (`quranic:root_000470:B003/m01`); renewed report (`quranic:root_000299:B003/m01`).
- Ayah anchors: 68:37 `كِتَٰبٌ` [ك ت ب] and `تَدْرُسُ` [د ر س]; 68:44 `حَدِيثِ` [ح د ث]; 68:47 `يَكْتُبُ` [ك ت ب].
- Synthesis: Durability has a material history. Joining precedes writing; writing permits decree and registration; study counters the fading of the trace. The claimed book in 68:37 is therefore tested as object, institution, and transmission practice.

#### Subchannel B. Judgment Restrains Error and Brings a Matter to Firmness
- Reading type: mixed
- Scene or process: A judge restrains disorder, identifies the right, issues a decision, and makes the resulting matter firm enough to hold.
- Active motifs: restraint for correction (`quranic:root_000348:B001/m01`); adjudication (`quranic:root_000348:B002/m01`); right-discerning wisdom (`quranic:root_000348:B003/m01`); firm and perfected decision (`quranic:root_000348:B004/m01`); delegated arbitration (`quranic:root_000348:B005/m01`); restraining bridle (`quranic:root_000348:B006/m01`); quality carried to its limit (`quranic:root_000151:B005/m01`); established sound standing (`quranic:root_000852:B003/m01`).
- Ayah anchors: 68:36/39 `تَحْكُمُ` [ح ك م]; 68:39 `بَٰلِغَةٌ` [ب ل غ]; 68:41 `صَٰدِقِينَ` [ص د ق]; 68:48 `حُكْمِ` [ح ك م].
- Synthesis: Judgment is neither preference nor naked command. It combines corrective restraint, knowledge, delegation, completion, and firmness; the bridle supplies a concrete image for preventing a claim from running wherever desire takes it.

#### Subchannel C. Oath, Guarantor, Partner, and Fulfillment Back the Claim
- Reading type: mixed
- Scene or process: A sworn undertaking invokes power, a guarantor assumes liability, partners share the interest, and truthful action fulfills what speech pledged.
- Active motifs: sworn oath (`quranic:root_001698:B003/m01`); oath as power and right (`quranic:root_001698:B004/m01`); uncertain assertion (`quranic:root_000633:B001/m01`); guarantor (`quranic:root_000633:B003/m01`); leader speaking for a group (`quranic:root_000633:B004/m01`); shared interest (`quranic:root_000791:B001/m01`); false divine partnership (`quranic:root_000791:B002/m01`); truthful statement (`quranic:root_000852:B001/m01`); action fulfilling promise (`quranic:root_000852:B004/m01`); oath-binding (`quranic:root_000076:B007/m02`).
- Ayah anchors: 68:39 `أَيْمَٰنٌ` [ي م ن]; 68:40 `زَعِيمٌ` [ز ع م]; 68:41 `شُرَكَآءُ` [ش ر ك] and `صَٰدِقِينَ` [ص د ق]; surface anchor unavailable for root `ء ل ي`.
- Synthesis: These are separate support roles. Oath binds the speaker, guarantor absorbs failure, partner shares the claim, and fulfillment tests speech against action. The questions strip away each possible backing in turn.

#### Subchannel D. Question and Answer Expose the Missing Warrant
- Reading type: mixed
- Scene or process: An interrogator requests a named basis; parties question one another, an answer affirms or refuses, and a putative explanation must identify its referent.
- Active motifs: request and inquiry (`quranic:root_000661:B001/m01`); thing requested (`quranic:root_000661:B002/m01`); reciprocal questioning (`quranic:root_000661:B004/m01`); attention-opening particle (`quranic:root_001573:B002/m01`); answer or response (`quranic:root_001573:B003/m01`); interrogative substitution (`quranic:root_001573:B004/m01`); interrogative-relative reference (`quranic:root_000527:B004/m02`); affirmative answer (`quranic:root_001525:B004/m01`); reported supposition (`quranic:root_001272:B011/m01`).
- Ayah anchors: 68:40 `سَلْ` [س ء ل]; 68:51 `يَقُولُ` [ق و ل]; surface anchors unavailable for roots `ه ا ء` and `ذ و و`; 68:34 `نَّعِيمِ` [ن ع م].
- Synthesis: Interrogation is a warrant-seeking mechanism. It fixes the requested object, identifies who answers, and tests whether a demonstrable referent lies behind the assertion rather than leaving it as ungrounded supposition.

### 24. [P3 68:34-52] Obligation Acquires Weight, Price, and Market Form
- Semantic invariant: A social or verbal demand becomes tangible when it attaches as debt, is measured as weight, or enters exchange as a price.
- Surface relation: direct; 68:40 `زَعِيمٌ`, 68:46 `أَجْرًا`/`مَّغْرَمٍ`/`مُّثْقَلُونَ`, and 68:47 `يَكْتُبُ`.
- Surprising reach: The rejected fee is surrounded by a full political economy of wages, debtors, standards, levies, markets, advance payment, charity, and emancipation installments.

#### Subchannel A. Wage Becomes Attaching Debt and Surety
- Reading type: mixed
- Scene or process: Compensation is requested for work; if treated as liability, it adheres to debtor and creditor until a guarantor or installment discharges it.
- Active motifs: wage or contractual compensation (`quranic:root_000015:B001/m03`); financial charge (`quranic:root_001081:B001/m01`); creditor-debtor attachment (`quranic:root_001081:B002/m01`); lasting punitive liability (`quranic:root_001081:B003/m01`); guarantor (`quranic:root_000633:B003/m02`); manumission contract paid by installments (`quranic:root_001283:B005/m01`).
- Ayah anchors: 68:40 `زَعِيمٌ` [ز ع م]; 68:46 `أَجْرًا` [ء ج ر] and `مَّغْرَمٍ` [غ ر م]; 68:47 `يَكْتُبُ` [ك ت ب].
- Synthesis: Fee and debt are not synonyms. Wage compensates work, debt binds parties across time, guaranty reallocates default risk, and installments can turn payment into emancipation; 68:46 denies that this apparatus explains rejection.

#### Subchannel B. Weight and Valuation Make Burden Comparable
- Reading type: mixed
- Scene or process: A burden is placed on a scale, assigned a standard weight or price, and judged heavy, precious, slow, or equal.
- Active motifs: physical and figurative heaviness (`quranic:root_000202:B001/m01`); standard weight (`quranic:root_000202:B004/m01`); precious weighty object (`quranic:root_000202:B005/m01`); heaviness producing slowness (`quranic:root_000202:B006/m01`); hearing made unreceptive by weight (`quranic:root_000202:B009/m01`); pricing and valuation (`quranic:root_001273:B010/m01`); equal standard weight (`quranic:root_001273:B015/m01`); active market (`quranic:root_001273:B018/m01`); ounce as measured weight (`quranic:root_001677:B004/m01`); threshing as measured processing (`quranic:root_000470:B005/m02`).
- Ayah anchors: 68:34 `مُتَّقِينَ` [و ق ي]; 68:37 `تَدْرُسُ` [د ر س]; 68:39 `قِيَٰمَةِ` [ق و م]; 68:46 `مُّثْقَلُونَ` [ث ق ل].
- Synthesis: Weight converts an attaching obligation into something comparable. The branches distinguish mass, standard, price, preciousness, delay, and impaired reception, showing how “burdened” can describe both economic pressure and a listener’s slowed response.

#### Subchannel C. Levy, Sale, Advance, and Charity Organize Exchange
- Reading type: latent/lexical
- Scene or process: Goods enter a market, are priced or sold by a sign, taxed, paid in advance, or transferred as charitable wealth.
- Active motifs: market-place (`quranic:root_000762:B005/m01`); common market population (`quranic:root_000762:B007/m01`); competitive boasting (`quranic:root_000762:B011/m01`); sale made binding by throwing an object (`quranic:root_001466:B003/m01`); levy or tribute (`quranic:root_000009:B008/m01`); revenue gathering (`quranic:root_000220:B001/m01`); promised fee for work (`quranic:root_000248:B005/m01`); advance payment (`quranic:root_000737:B005/m01`); charitable transfer (`quranic:root_000852:B006/m01`); marriage payment (`quranic:root_000852:B007/m01`).
- Ayah anchors: 68:35 `نَجْعَلُ` [ج ع ل] and `مُسْلِمِينَ` [س ل م]; 68:39 `قِيَٰمَةِ` [ق و م]; 68:41 `يَأْتُ` [ء ت ي] and `صَٰدِقِينَ` [ص د ق]; 68:42 `سَاقٍ` [س و ق]; 68:49 `نُبِذَ` [ن ب ذ]; 68:50 `ٱجْتَبَٰ` [ج ب ي].
- Synthesis: Exchange can be coercive, contractual, competitive, or generous. Levy, sign-sale, wage, advance, dower, and charity specify different transfer rules, keeping the fee question from collapsing into a generic “money” motif.

### 25. [P3 68:34-52] The Body Must Be Able to Stand, Bend, and Obey
- Semantic invariant: Submission is a bodily capacity expressed through posture, jointed movement, lowered profile, and response to command.
- Surface relation: direct; 68:42 `سَاقٍ`/`يُدْعَ`/`سُّجُودِ`/`يَسْتَطِيعُ`, and 68:43 `خَٰشِعَةً أَبْصَٰرُ`/`ذِلَّةٌ`/`يُدْعَ`/`سُّجُودِ`/`سَٰلِمُونَ`.
- Surprising reach: Failure to prostrate is rendered as a breakdown across posture, limb, gaze, footing, tractability, and jointed capacity, not simply unwillingness at the final moment.

#### Subchannel A. Standing and Prostration Form a Postural Sequence
- Reading type: surface-primary
- Scene or process: A standing body receives the summons, lowers head and articulated limbs, places marked contact points, and completes prostration.
- Active motifs: prostration and submission (`quranic:root_000675:B001/m01`); limbs and contact marks (`quranic:root_000675:B003/m01`); bending under weight (`quranic:root_000675:B004/m01`); lowered sustained gaze (`quranic:root_000675:B005/m01`); bodily standing (`quranic:root_001273:B002/m01`); upright stature (`quranic:root_001273:B011/m01`); rising at resurrection (`quranic:root_001273:B013/m01`); bowed or kneeling posture (`quranic:root_000220:B006/m01`).
- Ayah anchors: 68:39 `قِيَٰمَةِ` [ق و م]; 68:42/43 `سُّجُودِ` [س ج د]; 68:50 `ٱجْتَبَٰ` [ج ب ي].
- Synthesis: Prostration is a sequence of controlled articulations. Standing, summons, flexion, contact, and gaze must coordinate; the resurrection sense makes the inability especially stark because bodies have been raised but cannot complete the answering posture.

#### Subchannel B. Low Ground, Spent Hump, and Hanging Edge Materialize Humbling
- Reading type: mixed
- Scene or process: A proud profile loses height like low ground, a setting star, or a depleted camel hump, while the body and garment hang downward.
- Active motifs: bowed humility (`quranic:root_000412:B001/m01`); low lifeless terrain (`quranic:root_000412:B002/m01`); sinking star (`quranic:root_000412:B003/m01`); hump with its crest depleted (`quranic:root_000412:B004/m01`); abasement under force (`quranic:root_000519:B001/m01`); gentle lowliness (`quranic:root_000519:B002/m01`); hanging lower edge (`quranic:root_000519:B005/m01`); struck peg (`quranic:root_000519:B006/m01`); head-and-chest lowering (`quranic:root_001307:B014/m01`).
- Ayah anchors: 68:43 `خَٰشِعَةً` [خ ش ع] and `ذِلَّةٌ` [ذ ل ل]; 68:51 `كَفَرُ` [ك ف ر].
- Synthesis: Humbling is a loss of vertical prominence. Terrain, star, hump, garment edge, head, and chest all descend by different mechanisms, giving the verse’s lowered eyes and covering humiliation a coherent shape.

#### Subchannel C. Tractability and Ability Can Fail Before the Command
- Reading type: mixed
- Scene or process: A subject may obey, become capable through effort, or be internally eased toward action; fatigue, damaged limbs, or lost sight can instead arrest performance.
- Active motifs: willing obedience (`quranic:root_000956:B001/m02`); capacity to act (`quranic:root_000956:B003/m01`); effortful acquisition of capacity (`quranic:root_000956:B004/m01`); self-facilitation (`quranic:root_000956:B006/m02`); immobility and exhaustion (`quranic:root_001273:B016/m01`); leg disease preventing stance (`quranic:root_001273:B020/m01`); intact eye without sight (`quranic:root_001273:B021/m01`); sound bodily condition (`quranic:root_000737:B001/m02`); power or ability (`quranic:root_000076:B011/m01`).
- Ayah anchors: 68:39 `قِيَٰمَةِ` [ق و م]; 68:42 `يَسْتَطِيعُ` [ط و ع]; 68:43 `سَٰلِمُونَ` [س ل م]; surface anchor unavailable for root `ء ل ي`.
- Synthesis: Inability can arise at several levels: no power, no acquired skill, no inner facilitation, exhausted stance, damaged leg, or failed sight. The branches keep these operational failures distinct from refusal.

#### Subchannel D. Bared Shin Signals Mobilization into Crisis
- Reading type: mixed
- Scene or process: A driving force exposes the shin, brings bodies into a battle-like zone, and orders them in a following column whose rear remains under pressure.
- Active motifs: driving and herding (`quranic:root_000762:B001/m01`); leg or supporting stem (`quranic:root_000762:B003/m01`); shin bared for crisis (`quranic:root_000762:B004/m01`); battle-zone (`quranic:root_000762:B006/m01`); stirrup strap (`quranic:root_000762:B009/m01`); following in one track (`quranic:root_000762:B012/m01`); rear of an army (`quranic:root_000762:B013/m01`).
- Ayah anchors: 68:42 `سَاقٍ` [س و ق].
- Synthesis: The “shin” scene expands by role rather than by loose association: supporting limb, exposure, mobilizing drive, battle-space, riding strap, column, and rear guard. Crisis is a coordinated demand on bodies, not merely a visual disclosure.

### 26. [P3 68:34-52] Perception Can Stabilize Knowledge or Strip Away Footing
- Semantic invariant: Sensory contact becomes reliable only when eye, ear, inward understanding, and stable bodily position cooperate.
- Surface relation: direct; 68:43 `أَبْصَٰرُ`, 68:44 `يَعْلَمُ`, 68:46 `مُّثْقَلُونَ`, 68:51 `يُزْلِقُ`/`أَبْصَٰرِ`/`سَمِعُ`/`ذِّكْرَ`/`مَجْنُونٌ`, and 68:52 `ذِكْرٌ`.
- Surprising reach: Hostile looking is rendered as a literal destabilization of ground and skin, while hearing can progress to understanding or become weighted, bound, and merely reputational.

#### Subchannel A. Sight Becomes Insight by Reading Marks
- Reading type: mixed
- Scene or process: The eye registers a surface, inward sight interprets it, blood-trace or stone supplies visible evidence, and a remembered mark guides cognition.
- Active motifs: ocular sight (`quranic:root_000121:B001/m02`); inward discernment (`quranic:root_000121:B002/m02`); visible blood trace (`quranic:root_000121:B004/m01`); pale gleaming stone (`quranic:root_000121:B007/m02`); knowledge as disclosure (`quranic:root_001040:B001/m03`); identifying landmark (`quranic:root_001040:B002/m02`); retained remembrance (`quranic:root_000516:B003/m01`); reminder restoring presence (`quranic:root_000516:B009/m01`).
- Ayah anchors: 68:43 and 68:51 `أَبْصَٰرُ`/`أَبْصَٰرِ` [ب ص ر]; 68:44/52 `يَعْلَمُ`/`عَٰلَمِينَ` [ع ل م]; 68:51/52 `ذِّكْرَ`/`ذِكْرٌ` [ذ ك ر].
- Synthesis: Sight supplies data, not completion. Trace and landmark make the surface readable; remembrance preserves the evidence; inward discernment converts it into knowledge. This sequence contrasts with the hostile gaze that seeks effect without understanding.

#### Subchannel B. Hearing Moves from Ear to Comprehension or Burden
- Reading type: mixed
- Scene or process: Sound reaches the ear, is transmitted and understood, then either elicits compliance or is blocked by weight, binding, or ungrounded inference.
- Active motifs: auditory perception (`quranic:root_000741:B001/m01`); ear and auditory opening (`quranic:root_000741:B002/m01`); understanding and compliance (`quranic:root_000741:B003/m01`); making another hear (`quranic:root_000741:B004/m01`); auditory fetter (`quranic:root_000741:B009/m01`); inference from hearing and seeing without object (`quranic:root_000741:B013/m01`); brain as auditory center (`quranic:root_000741:B016/m01`); weighted unreceptive hearing (`quranic:root_000202:B009/m02`).
- Ayah anchors: 68:46 `مُّثْقَلُونَ` [ث ق ل]; 68:51 `سَمِعُ` [س م ع].
- Synthesis: Hearing is decomposed into organ, event, transmission, understanding, and response. A fettered or heavy ear may receive sound without accepting it, while hasty inference treats sensory contact as knowledge before an object has been secured.

#### Subchannel C. A Gaze Can Make Ground and Skin Slippery
- Reading type: mixed
- Scene or process: Hostile looking dislodges the target from a stable place as though the ground, animal body, or oiled skin had become too smooth to grip.
- Active motifs: slick barren surface that defeats footing (`quranic:root_000640:B001/m01`); slick animal hindquarter (`quranic:root_000640:B004/m01`); fast gliding camel (`quranic:root_000640:B006/m01`); oiled shining skin (`quranic:root_000640:B007/m01`); shaved smooth head (`quranic:root_000640:B008/m01`); hostile ocular act (`quranic:root_000121:B001/m03`); covering that blocks secure perception (`quranic:root_001307:B001/m01`).
- Ayah anchors: 68:43/51 `أَبْصَٰرُ`/`أَبْصَٰرِ` [ب ص ر]; 68:51 `يُزْلِقُ` [ز ل ق] and `كَفَرُ` [ك ف ر].
- Synthesis: `يُزْلِقُونَكَ بِأَبْصَارِهِمْ` acquires a physical scene of failed traction. Ground, skin, hair, and moving animal all participate in one functional analogy: smoothness removes the hold needed to remain in place.

#### Subchannel D. The Madness Charge Confuses Hidden Mind with Covered Truth
- Reading type: mixed
- Scene or process: Observers encounter an inaccessible interior, cover the truth, and replace inquiry with an accusation that attributes corruption or derangement to the speaker.
- Active motifs: sensory concealment (`quranic:root_000266:B001/m03`); mind covered by madness (`quranic:root_000266:B006/m02`); hidden heart (`quranic:root_000266:B010/m02`); overpowering affliction (`quranic:root_000606:B001/m01`); attributed corruption and falsehood (`quranic:root_000606:B005/m01`); denial covering truth (`quranic:root_001307:B003/m01`); assigning unbelief to another (`quranic:root_001307:B006/m01`); false attribution in speech (`quranic:root_001272:B005/m02`).
- Ayah anchors: 68:43 `تَرْهَقُ` [ر ه ق]; 68:51 `كَفَرُ` [ك ف ر], `يَقُولُ` [ق و ل], and `مَجْنُونٌ` [ج ن ن].
- Synthesis: The accusation mistakes epistemic cover for diagnosed interior state. Concealment, denial, attribution, and overpowering affliction are different operations; their separation exposes how polemical naming substitutes for knowledge.

### 27. [P3 68:34-52] Utterance Summons, Attributes, and Makes Reputation
- Semantic invariant: Speech changes social reality by calling participants, asserting claims, circulating reports, and fixing a person’s public name.
- Surface relation: direct; 68:40 `سَلْ`/`زَعِيمٌ`, 68:42-43 `يُدْعَ`, 68:44 `حَدِيثِ`, 68:48 `نَادَىٰ`, and 68:51 `سَمِعُ`/`ذِّكْرَ`/`يَقُولُ`.
- Surprising reach: The same communicative field includes prayer-call, council, riddle, public anecdote, praise, insult, false attribution, and truthful fulfillment; “speech” is split by operation and social effect.

#### Subchannel A. Call, Council, and Voice Assemble an Audience
- Reading type: mixed
- Scene or process: A caller raises a voice, draws participants toward a place or act, gathers them in council, and may pose a riddle whose answer tests the assembly.
- Active motifs: vocal summons and attraction (`quranic:root_000478:B001/m01`); enigmatic question (`quranic:root_000478:B007/m01`); empty house without a respondent (`quranic:root_000478:B008/m01`); council and gathering (`quranic:root_001486:B001/m02`); raised far-reaching voice (`quranic:root_001486:B002/m02`); public call (`quranic:root_001487:B001/m02`); assembly place (`quranic:root_001487:B003/m02`); manifest announcement (`quranic:root_001487:B011/m01`); effortful cry (`quranic:root_001334:B005/m01`).
- Ayah anchors: 68:42/43 `يُدْعَ` [د ع و]; 68:45 `كَيْدِ` [ك ي د]; 68:48 `نَادَىٰ` [ن د و]; surface anchor unavailable for root `ن د ي`.
- Synthesis: A call is successful only if it travels, finds an audience, and elicits response. Council supplies the social setting, the riddle tests understanding, and the empty-house sense makes failed response a structural absence rather than mere silence.

#### Subchannel B. A Report Can Polish the Heart or Turn a Person into an Anecdote
- Reading type: mixed
- Scene or process: Renewed speech enters memory, circulates among hearers, and produces either inward clarification, durable renown, or public shame.
- Active motifs: renewed news or discourse (`quranic:root_000299:B003/m02`); becoming a public anecdote (`quranic:root_000299:B004/m01`); making a matter manifest (`quranic:root_000299:B006/m01`); polishing sword or heart (`quranic:root_000299:B007/m01`); verbal mention (`quranic:root_000516:B004/m01`); public honor and renown (`quranic:root_000516:B007/m01`); documentary memorial of a right (`quranic:root_000516:B008/m01`); reminder (`quranic:root_000516:B009/m02`); public repute (`quranic:root_000741:B005/m01`); insult made audible (`quranic:root_000741:B006/m01`); circulating report (`quranic:root_001272:B007/m04`).
- Ayah anchors: 68:44 `حَدِيثِ` [ح د ث]; 68:51 `سَمِعُ` [س م ع], `ذِّكْرَ` [ذ ك ر], and `يَقُولُ` [ق و ل]; 68:52 `ذِكْرٌ` [ذ ك ر].
- Synthesis: Public memory is made by transmission. A report can cleanse perception like polish, preserve a right in documentary mention, elevate a name, or turn that name into a cautionary anecdote or audible insult.

#### Subchannel C. False Attribution Is Answered by Fulfilled Speech
- Reading type: mixed
- Scene or process: A doubtful assertion becomes explicit false attribution; counter-speech tests it against action, promise, and a stable definition.
- Active motifs: assertion under suspicion (`quranic:root_000633:B001/m02`); vain expectation (`quranic:root_000633:B002/m01`); falsehood (`quranic:root_001290:B001/m02`); accusing another of falsehood (`quranic:root_001290:B002/m03`); failed charge or attack (`quranic:root_001290:B004/m01`); acting without delay (`quranic:root_001290:B005/m01`); false attribution (`quranic:root_001272:B005/m03`); imposed judgment (`quranic:root_001272:B010/m02`); formal definition (`quranic:root_001272:B016/m01`); truthful statement (`quranic:root_000852:B001/m02`); fulfilled promise (`quranic:root_000852:B004/m02`).
- Ayah anchors: 68:40 `زَعِيمٌ` [ز ع م]; 68:41 `صَٰدِقِينَ` [ص د ق]; 68:44 `يُكَذِّبُ` [ك ذ ب]; 68:51 `يَقُولُ` [ق و ل].
- Synthesis: The channel distinguishes saying, attributing, defining, and fulfilling. A claim is not vindicated by more forceful speech but by correspondence between the report, the named referent, and enacted promise.

### 28. [P3 68:34-52] Covering Establishes the Stakes of Disclosure and Exposure
- Semantic invariant: A cover creates an interior that may protect, hide, or entomb; lifting or losing it changes the occupant’s vulnerability and public status.
- Surface relation: direct; 68:42 `يُكْشَفُ`, 68:47 `غَيْبُ`, 68:49 `نُبِذَ بِٱلْعَرَآءِ`, and 68:51 `كَفَرُ`.
- Surprising reach: Unseen knowledge, armor, grave, grove, fruit-husk, uncovered defect, open hostility, exposed terrace, and abandoned child occupy distinct positions in one cover-removal mechanism.

#### Subchannel A. Pit, Grove, Root, and Grave Make Nested Interiors
- Reading type: mixed
- Scene or process: A thing passes from ordinary visibility into a low place, dense growth, underground root, or grave, each providing a different depth and permanence of concealment.
- Active motifs: absence from eye and knowledge (`quranic:root_001117:B001/m01`); hidden pit or depression (`quranic:root_001117:B002/m01`); concealing grove (`quranic:root_001117:B003/m01`); hidden root later excavated (`quranic:root_001117:B008/m01`); burial (`quranic:root_001117:B009/m01`); sensory cover (`quranic:root_000266:B001/m04`); burial wrapping (`quranic:root_000266:B009/m02`); hiding-place (`quranic:root_000266:B017/m02`); vast darkness or water that covers (`quranic:root_001307:B002/m01`); fruit-sheath (`quranic:root_001307:B010/m02`); hidden mountain pass (`quranic:root_001307:B013/m01`).
- Ayah anchors: 68:47 `غَيْبُ` [غ ي ب]; 68:51 `كَفَرُ` [ك ف ر] and `مَجْنُونٌ` [ج ن ن].
- Synthesis: Concealment has topology. Pit lowers, grove surrounds, root passes underground, grave seals, and mountain pass hides by terrain; this differentiates ordinary unseen knowledge from physical inaccessibility and burial.

#### Subchannel B. Uncovering Reveals Defect or Open Hostility
- Reading type: mixed
- Scene or process: A covering is lifted; what appears may be a relieved burden, a bodily defect, a public flaw, or an adversary no longer concealing opposition.
- Active motifs: lifting a cover or distress (`quranic:root_001302:B001/m01`); visible defect (`quranic:root_001302:B002/m01`); bodily exposure (`quranic:root_001302:B003/m01`); open initiation of hostility (`quranic:root_001302:B004/m01`); bringing a matter into view (`quranic:root_000299:B006/m02`); manifestation like a calling voice (`quranic:root_001486:B008/m01`).
- Ayah anchors: 68:42 `يُكْشَفُ` [ك ش ف]; 68:44 `حَدِيثِ` [ح د ث]; 68:48 `نَادَىٰ` [ن د و].
- Synthesis: Disclosure does not guarantee a benign result. The same removal can alleviate distress, disclose defect, expose the body, or convert latent enmity into overt confrontation; context determines the revealed object.

#### Subchannel C. Casting Out Produces the Open and Unprotected
- Reading type: mixed
- Scene or process: An occupant is thrown from a containing relation into a side-place or bare expanse, where abandonment and lack of cover become the decisive state.
- Active motifs: casting away (`quranic:root_001466:B001/m01`); moving to a side (`quranic:root_001466:B004/m01`); abandoned child (`quranic:root_001466:B007/m01`); neglected weak animal or scattered earth (`quranic:root_001466:B009/m01`); stripped body or land (`quranic:root_001005:B003/m01`); uncovered open ground (`quranic:root_001005:B004/m01`); abandonment without aid (`quranic:root_001005:B009/m01`); roof without parapet (`quranic:root_000015:B003/m01`).
- Ayah anchors: 68:46 `أَجْرًا` [ء ج ر]; 68:49 `نُبِذَ` [ن ب ذ] and `عَرَآءِ` [ع ر ي].
- Synthesis: Exposure is produced by an operation: remove from hand or group, place at the side, strip the cover, and leave without support. The open plain in 68:49 is thus social abandonment and architectural defenselessness as well as terrain.

#### Subchannel D. Shield and Armor Preserve an Interior Under Attack
- Reading type: latent/lexical
- Scene or process: A fitted shield, armor, or covering layer absorbs exterior force while keeping the enclosed body sound.
- Active motifs: protective barrier (`quranic:root_001677:B001/m02`); shield (`quranic:root_000266:B008/m04`); armor (`quranic:root_000121:B005/m03`); defensive weapon or mail (`quranic:root_000633:B005/m01`); covering layer (`quranic:root_001307:B001/m02`); wounded person named “sound” in hope or surrender (`quranic:root_000737:B009/m01`).
- Ayah anchors: 68:34 `مُتَّقِينَ` [و ق ي]; 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:40 `زَعِيمٌ` [ز ع م]; 68:43/51 `أَبْصَٰرُ`/`أَبْصَٰرِ` [ب ص ر]; 68:51 `كَفَرُ` [ك ف ر] and `مَجْنُونٌ` [ج ن ن].
- Synthesis: This is protective concealment rather than epistemic evasion. The cover remains fitted to a vulnerable body and is judged by whether soundness survives the blow.

### 29. [P3 68:34-52] Reprieve Stages a Gradual Capture
- Semantic invariant: Extended time can be organized into incremental approach, deception, pursuit, and eventual arrival at a fixed limit.
- Surface relation: direct; 68:39/42 `يَوْمِ`/`يَوْمَ`, 68:44 `نَسْتَدْرِجُ`/`يَعْلَمُ`, 68:45 `أُمْلِى`/`كَيْدِ`/`مَتِينٌ`, and 68:49 `تَدَٰرَكَ`.
- Surprising reach: Delay is not inactivity. Dictation, head-start, slow-kindling fire, stepwise luring, long pursuit, and final overtaking describe how time itself becomes an instrument.

#### Subchannel A. Extended Time Grants a Head-Start
- Reading type: mixed
- Scene or process: A period is lengthened for enjoyment or apparent freedom, like a runner allowed to advance before the pursuer closes the distance.
- Active motifs: temporal extension and reprieve (`quranic:root_001446:B001/m01`); prolonged enjoyment (`quranic:root_001446:B002/m01`); dictation over time (`quranic:root_001446:B004/m01`); long duration (`quranic:root_001447:B001/m01`); explicit respite (`quranic:root_001447:B002/m01`); dictation (`quranic:root_001447:B003/m01`); indefinite duration (`quranic:root_001700:B002/m01`); severe event-day (`quranic:root_001700:B003/m01`); head-start in a race (`quranic:root_001396:B010/m01`).
- Ayah anchors: 68:39/42 `يَوْمِ`/`يَوْمَ` [ي و م]; 68:45 `أُمْلِى` [م ل و] and `مَتِينٌ` [م ت ن]; surface anchor unavailable for root `م ل ي`.
- Synthesis: Reprieve creates distance but not escape. Prolonged enjoyment and dictation occupy the interval, while the race image shows the concealed relation: the apparent lead belongs to a pursuit whose endpoint remains controlled.

#### Subchannel B. Stepwise Luring Converts Movement into Entrapment
- Reading type: mixed
- Scene or process: A target advances one grade at a time, believing itself free, while stratagem and slow preparation carry it into an increasingly closed situation.
- Active motifs: walking a route (`quranic:root_000468:B001/m01`); incremental luring (`quranic:root_000468:B003/m01`); path toward extinction (`quranic:root_000468:B004/m01`); folding and insertion (`quranic:root_000468:B005/m01`); forceful manipulation (`quranic:root_001334:B001/m01`); stratagem and deceptive respite (`quranic:root_001334:B002/m01`); fire slow to kindle (`quranic:root_001334:B006/m01`); arduous seeking (`quranic:root_001329:B001/m01`); near-completion of an act (`quranic:root_001329:B002/m01`); luring an animal from its burrow (`quranic:root_000452:B006/m01`).
- Ayah anchors: 68:38 `تَخَيَّرُ` [خ ي ر]; 68:44 `نَسْتَدْرِجُ` [د ر ج]; 68:45 `كَيْدِ` [ك ي د]; 68:51 `يَكَادُ` [ك و د].
- Synthesis: Gradation is the mechanism of deception. Each step remains locally plausible, yet fold, insertion, slow fire, and lure progressively reduce the target’s available exits.

#### Subchannel C. Approach Ends in Overtaking at the Limit
- Reading type: mixed
- Scene or process: A pursuer draws near, urgency narrows the remaining time, and arrival or catch reaches the target before it passes beyond recovery.
- Active motifs: following until near capture (`quranic:root_000606:B002/m01`); deadline pressure (`quranic:root_000606:B004/m01`); catching and reaching (`quranic:root_000471:B001/m01`); liability that catches up (`quranic:root_000471:B004/m01`); arrival (`quranic:root_000009:B001/m01`); road and endpoint (`quranic:root_000009:B010/m01`); calamity arriving (`quranic:root_000009:B011/m01`); penetrating efficacy (`quranic:root_000009:B013/m01`); reaching a limit (`quranic:root_000151:B001/m01`); severe condition reaching its height (`quranic:root_000151:B008/m01`); final calamity (`quranic:root_000151:B011/m01`).
- Ayah anchors: 68:39 `بَٰلِغَةٌ` [ب ل غ]; 68:41 `يَأْتُ` [ء ت ي]; 68:43 `تَرْهَقُ` [ر ه ق]; 68:49 `تَدَٰرَكَ` [د ر ك].
- Synthesis: Arrival can save or destroy depending on what arrives first. The same pursuit geometry holds divine favor that overtakes the fish-companion before exposure and liability or calamity that catches the uncorrected actor.

### 30. [P3 68:34-52] Holding Pressure Can Preserve Control or Seal Distress Inside
- Semantic invariant: Restraint governs pressure by holding the self, closing an opening, tying parts, or building a structure able to bear load.
- Surface relation: direct; 68:45 `مَتِينٌ`, 68:46 `مُّثْقَلُونَ`, and 68:48 `ٱصْبِرْ`/`حُكْمِ`/`مَكْظُومٌ`.
- Surprising reach: Patience and choking distress share a mechanics of containment, but differ in agency and outcome: one disciplines pressure; the other traps breath behind a sealed outlet.

#### Subchannel A. Patience Holds the Self While Distress Holds the Breath
- Reading type: mixed
- Scene or process: A person restrains panic and anger, but under extreme pressure breath, speech, or life itself may become trapped within.
- Active motifs: self-restraint against panic (`quranic:root_000840:B001/m01`); coercive confinement (`quranic:root_000840:B002/m01`); no-exit adversity (`quranic:root_000840:B006/m01`); swallowed anger (`quranic:root_001303:B001/m01`); trapped breath and silence (`quranic:root_001303:B002/m01`); life struggling to leave (`quranic:root_001334:B003/m01`); inward unspoken statement (`quranic:root_001272:B012/m03`).
- Ayah anchors: 68:45 `كَيْدِ` [ك ي د]; 68:48 `ٱصْبِرْ` [ص ب ر], `نَادَىٰ` [ن د و], and `مَكْظُومٌ` [ك ظ م]; 68:51 `يَقُولُ` [ق و ل].
- Synthesis: Both patience and anguish hold something back, but patience retains governed agency while `مَكْظُوم` marks pressure trapped at the outlet. The contrast makes the command to endure a transformation of containment, not a demand for numbness.

#### Subchannel B. Bridle, Stopper, and Tie Close an Opening
- Reading type: latent/lexical
- Scene or process: A bridle checks motion, a filled channel or door is closed, and straps gather loose ends into a controlled system.
- Active motifs: restraining bridle (`quranic:root_000348:B006/m02`); camel prevented from chewing cud (`quranic:root_001303:B003/m01`); filled conduit sealed (`quranic:root_001303:B004/m01`); binding loop joining loose parts (`quranic:root_001303:B006/m01`); secure hold on an affair (`quranic:root_001303:B009/m01`); tent or bow tensioned by thongs (`quranic:root_001396:B008/m01`); stopper for vessel or well (`quranic:root_000840:B018/m01`).
- Ayah anchors: 68:45 `مَتِينٌ` [م ت ن]; 68:48 `حُكْمِ` [ح ك م], `ٱصْبِرْ` [ص ب ر], and `مَكْظُومٌ` [ك ظ م].
- Synthesis: Restraint is implemented at points of escape: jaw, cud, conduit, door, vessel-neck, and loose cord. A secure system does not erase pressure; it directs where motion or flow may occur.

#### Subchannel C. Stone, Cloud, Food, and Mountain Bear Stacked Load
- Reading type: latent/lexical
- Scene or process: Hard ground, layered cloud, piled food, and mountain mass remain stable because each supports weight across a broad base.
- Active motifs: hard stone and gravel ground (`quranic:root_000840:B005/m01`); layered white cloud (`quranic:root_000840:B010/m01`); piled food and broad support (`quranic:root_000840:B011/m01`); mountain and central massif (`quranic:root_000840:B017/m01`); extended solidity (`quranic:root_001396:B001/m01`); high hard ground (`quranic:root_001396:B002/m01`); stable residence (`quranic:root_001396:B006/m01`).
- Ayah anchors: 68:45 `مَتِينٌ` [م ت ن]; 68:48 `ٱصْبِرْ` [ص ب ر].
- Synthesis: Endurance is modeled by load paths. Layered, piled, broad, and grounded forms bear pressure without immediate collapse, giving physical content to patience under a firm judgment.

### 31. [P3 68:34-52] Grace Intercepts Exposure and Refashions Status
- Semantic invariant: Beneficent intervention catches a vulnerable person before abandonment, gathers that person into chosen proximity, and repairs social-moral standing.
- Surface relation: direct; 68:49 `تَدَٰرَكَ`/`نِعْمَةٌ`/`رَّبِّ`/`نُبِذَ`/`عَرَآءِ`/`مَذْمُومٌ`, and 68:50 `ٱجْتَبَٰ`/`رَبُّ`/`جَعَلَ`/`صَّٰلِحِينَ`.
- Surprising reach: Rescue is a sequence of timed interception, removal of blame, collection, selection, transformation, reconciliation, and fitted usefulness.

#### Subchannel A. Favor Reaches Before Casting and Blame
- Reading type: surface-primary
- Scene or process: Favor overtakes a distressed person before expulsion into open ground and before blame becomes the final public status.
- Active motifs: timely overtaking (`quranic:root_000471:B001/m02`); favor and good condition (`quranic:root_001525:B001/m03`); honored delight (`quranic:root_001525:B013/m02`); sovereign care (`quranic:root_000532:B001/m03`); nurture and completion (`quranic:root_000532:B002/m05`); beneficent gift (`quranic:root_000532:B016/m05`); casting away (`quranic:root_001466:B001/m02`); exposed plain (`quranic:root_001005:B004/m02`); blame and defect (`quranic:root_000520:B001/m01`).
- Ayah anchors: 68:49 `تَدَٰرَكَ` [د ر ك], `نِعْمَةٌ` [ن ع م], `رَّبِّ` [ر ب ب], `نُبِذَ` [ن ب ذ], `عَرَآءِ` [ع ر ي], and `مَذْمُومٌ` [ذ م م].
- Synthesis: Grace acts before the threatened state closes. It reaches, catches, and restores relation at the exact threshold between contained distress and irreversible exposure with blame.

#### Subchannel B. Gathering and Selection Make a New Placement
- Reading type: mixed
- Scene or process: A dispersed subject is gathered, chosen for proximity, and actively made into a different status rather than merely returned to the former location.
- Active motifs: gathering and collection (`quranic:root_000220:B001/m02`); choosing and drawing near (`quranic:root_000220:B004/m01`); making or producing (`quranic:root_000248:B001/m01`); transforming status (`quranic:root_000248:B002/m01`); beginning and sustaining an action (`quranic:root_000248:B004/m01`); selected excellence (`quranic:root_000452:B002/m03`); choosing the better (`quranic:root_000452:B003/m02`).
- Ayah anchors: 68:35 and 68:50 `نَجْعَلُ`/`جَعَلَ` [ج ع ل]; 68:38 `تَخَيَّرُ` [خ ي ر]; 68:50 `ٱجْتَبَٰ` [ج ب ي].
- Synthesis: Selection is followed by making. The subject is not only picked from a set but repositioned and transformed into a status whose fitness must now be enacted.

#### Subchannel C. Repair, Reconciliation, and Suitability Stabilize the New Status
- Reading type: mixed
- Scene or process: Damage is repaired, estrangement is removed, and the restored person is fitted to a durable role under covenant.
- Active motifs: correction opposed to corruption (`quranic:root_000876:B001/m01`); reconciliation removing estrangement (`quranic:root_000876:B002/m01`); suitability for a role (`quranic:root_000876:B003/m01`); heart polished by admonition (`quranic:root_000299:B007/m02`); nurturing repair (`quranic:root_000532:B002/m06`); covenant and protected right (`quranic:root_000520:B002/m01`); peace after conflict (`quranic:root_000737:B004/m01`); handing over and leaving a former state (`quranic:root_000737:B012/m01`).
- Ayah anchors: 68:34/48/49/50 forms of `ر ب ب` [ر ب ب]; 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:44 `حَدِيثِ` [ح د ث]; 68:49 `مَذْمُومٌ` [ذ م م]; 68:50 `صَّٰلِحِينَ` [ص ل ح].
- Synthesis: Repair becomes stable when relation and role are both restored. Reconciliation removes hostility, covenant protects the relation, and suitability makes the new placement function rather than remain a nominal pardon.

### 32. [P3 68:34-52] Joined Parts Create Load-Bearing and Water-Handling Systems
- Semantic invariant: Cutting, joining, tying, and fitting convert separate materials into containers, conduits, rigging, and frames that can carry load or govern flow.
- Surface relation: indirect; 68:37/47 `كِتَٰبٌ`/`تَكْتُبُ`, 68:43 `سَٰلِمُونَ`, 68:45 `مَتِينٌ`, 68:48 `مَكْظُومٌ`, and 68:51 `سَمِعُ`.
- Surprising reach: Stitched hide, tanning bark, sandal strap, bucket handle, well-rope splice, underground channel, body joint, shin, and tool-leg share an engineering logic of fitted parts under tension.

#### Subchannel A. Stitched and Tensioned Hide Becomes a Working Container
- Reading type: latent/lexical
- Scene or process: Hide is tanned, edged, stitched to another panel, treated, and held under tension until it can function as a vessel, tent panel, or fitted strap.
- Active motifs: joining and stitching (`quranic:root_001283:B001/m01`); joining hide or cloth panels at a thick edge (`quranic:root_000121:B006/m01`); tanning tree and bark (`quranic:root_000737:B008/m01`); sandal strap and its repair (`quranic:root_000791:B004/m01`); hide or tent tensioned by thongs (`quranic:root_001396:B008/m01`); thick syrup used to dress or repair a skin vessel (`quranic:root_000532:B006/m01`).
- Ayah anchors: 68:34/48/49/50 forms of `ر ب ب` [ر ب ب]; 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:37/47 `كِتَٰبٌ`/`تَكْتُبُ` [ك ت ب]; 68:41 `شُرَكَآءُ` [ش ر ك]; 68:43/51 `أَبْصَٰرُ`/`أَبْصَٰرِ` [ب ص ر]; 68:45 `مَتِينٌ` [م ت ن].
- Synthesis: The container is not a natural whole. Plant material prepares the hide, edge thickness permits a seam, stitch and strap join the parts, and tension gives the assembly usable form; treatment then preserves the skin as a vessel rather than leaving it raw material.

#### Subchannel B. Rope, Handle, Basin, and Channel Complete a Water Circuit
- Reading type: latent/lexical
- Scene or process: A rope is lengthened to reach water, attached to a handled bucket, raised over a well-edge, and emptied into a basin or managed conduit.
- Active motifs: well-rope splice and ring (`quranic:root_000471:B003/m01`); single-handled water-carrier's bucket (`quranic:root_000737:B011/m01`); bucket handle or balancing crosspiece (`quranic:root_000741:B008/m01`); linked wells or openings that preserve water flow (`quranic:root_001303:B005/m01`); binding loop that joins cord ends (`quranic:root_001303:B006/m01`); collected basin-water (`quranic:root_000220:B002/m01`); excavated rim around well or basin (`quranic:root_000220:B003/m01`); directed watercourse (`quranic:root_000009:B004/m01`); water-rich well or sea (`quranic:root_001040:B005/m01`).
- Ayah anchors: 68:41 `يَأْتُ` [ء ت ي]; 68:43 `سَٰلِمُونَ` [س ل م]; 68:44/52 `يَعْلَمُ`/`لِّلْعَٰلَمِينَ` [ع ل م]; 68:48 `مَكْظُومٌ` [ك ظ م]; 68:49 `تَدَٰرَكَ` [د ر ك]; 68:50 `ٱجْتَبَٰ` [ج ب ي]; 68:51 `سَمِعُ` [س م ع].
- Synthesis: Each component answers a different hydraulic problem: depth requires a splice, weight a handle, lifting a balanced attachment, collection a basin, and distribution a controlled channel. The scene is a complete flow system assembled from small lexical parts.

#### Subchannel C. Body and Implement Share a Supporting Frame
- Reading type: latent/lexical
- Scene or process: Back muscles, bones, joints, shin, and bodily mass bear weight in the same structural positions as an upright tool-part or standing support.
- Active motifs: back muscles flanking the spine (`quranic:root_001396:B003/m01`); finger, foot, and hoof bones and joints (`quranic:root_000737:B010/m01`); shin or load-bearing plant stem (`quranic:root_000762:B003/m01`); bodily mass and frame (`quranic:root_000239:B007/m01`); upright part of pulley, sword, bed, table, animal, or plough (`quranic:root_001273:B012/m01`); burden borne in the body (`quranic:root_000202:B007/m01`).
- Ayah anchors: 68:35 `مُجْرِمِينَ` [ج ر م]; 68:39 `قِيَٰمَةِ` [ق و م]; 68:42 `سَاقٍ` [س و ق]; 68:43 `سَٰلِمُونَ` [س ل م]; 68:45 `مَتِينٌ` [م ت ن]; 68:46 `مُّثْقَلُونَ` [ث ق ل].
- Synthesis: Anatomy and implement are analogized by load path rather than appearance alone. Jointed bones articulate, the shin stands, back musculature stabilizes, and an upright fitted part transfers force through a tool or frame.

### 33. [P3 68:34-52] Ground Surface Controls Posture, Footing, and Exposure
- Semantic invariant: Surface composition and elevation determine whether a body can stand, lower itself, move securely, find cover, or remain publicly exposed.
- Surface relation: direct; 68:42-43 `سَاقٍ`/`يَسْجُدُوا۟`/`خَٰشِعَةً`/`سَٰلِمُونَ`, 68:49 `بِٱلْعَرَآءِ`, and 68:51 `لَيُزْلِقُونَكَ`.
- Surprising reach: Hard and soft stone, low dead earth, bare expanse, slick soil, hoof-protecting gait, mountain-center, hidden grove, floor cushion, and parapetless roof make bodily posture a property of terrain and shelter.

#### Subchannel A. Hardness and Elevation Establish a Bearing Surface
- Reading type: mixed
- Scene or process: Stone and elevated ground provide differing degrees of hardness, levelness, and support beneath a standing or prostrating body.
- Active motifs: hard stone mass (`quranic:root_000737:B007/m01`); soft or pale gleaming stone (`quranic:root_000121:B007/m02`); hard gravel ground (`quranic:root_000840:B005/m01`); mountain and central massif (`quranic:root_000840:B017/m01`); high hard ground (`quranic:root_001396:B002/m01`); solid and level object (`quranic:root_000852:B002/m01`).
- Ayah anchors: 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:41 `صَٰدِقِينَ` [ص د ق]; 68:43/51 `أَبْصَٰرُ`/`أَبْصَٰرِ` [ب ص ر]; 68:45 `مَتِينٌ` [م ت ن]; 68:48 `ٱصْبِرْ` [ص ب ر].
- Synthesis: A bearing surface is defined by how it receives weight. Soft stone yields, gravel resists, a level solid permits stable placement, and mountain or raised hard ground extends support to landscape scale.

#### Subchannel B. Low, Bare, or Slick Ground Changes the Body's Gait
- Reading type: mixed
- Scene or process: A body lowers itself toward lifeless ground, crosses an uncovered surface, or adjusts its gait when smoothness and roughness threaten secure footing.
- Active motifs: low lifeless terrain (`quranic:root_000412:B002/m01`); uncovered open ground (`quranic:root_001005:B004/m01`); slick barren surface that defeats footing (`quranic:root_000640:B001/m01`); animal guarding a sore hoof from rough ground (`quranic:root_001677:B003/m01`); walking and proceeding along a route (`quranic:root_000468:B001/m01`).
- Ayah anchors: 68:34 `مُتَّقِينَ` [و ق ي]; 68:43 `خَٰشِعَةً` [خ ش ع]; 68:44 `نَسْتَدْرِجُ` [د ر ج]; 68:49 `بِٱلْعَرَآءِ` [ع ر ي]; 68:51 `لَيُزْلِقُونَكَ` [ز ل ق].
- Synthesis: Posture responds to substrate. Lowness invites or figures lowering, exposure removes protective margins, slickness defeats traction, and painful roughness makes even a capable animal place each step defensively.

#### Subchannel C. Shelter Distinguishes a Protected Interior from an Open Edge
- Reading type: latent/lexical
- Scene or process: A person moves between grove, hiding-place, floor cushion, bare land, and an unguarded roof, each position supplying or removing a different kind of enclosure.
- Active motifs: roof without parapet (`quranic:root_000015:B003/m01`); hiding-place (`quranic:root_000266:B017/m01`); concealing grove (`quranic:root_001117:B003/m01`); cushion cast on the floor for sitting (`quranic:root_001466:B008/m01`); stripped body or land (`quranic:root_001005:B003/m01`); uncovered open ground (`quranic:root_001005:B004/m01`).
- Ayah anchors: 68:46 `أَجْرًا` [ء ج ر]; 68:47 `غَيْبُ` [غ ي ب]; 68:49 `نُبِذَ` [ن ب ذ] and `عَرَآءِ` [ع ر ي]; 68:51 `مَجْنُونٌ` [ج ن ن].
- Synthesis: Cover is spatially graded. Grove and hiding-place obscure the occupant, a cushion supports an interior posture, the bare plain removes enclosure, and a roof without parapet raises the body while leaving its edge unprotected.

### 34. [P3 68:34-52] Identity Is Made by Classification and Association
- Semantic invariant: A person's status becomes legible through a moral condition, household bond, collective affiliation, or assigned relation of protection and dependence.
- Surface relation: direct; 68:35 `نَجْعَلُ`/`مُسْلِمِينَ`/`مُجْرِمِينَ`, 68:40-41 `زَعِيمٌ`/`شُرَكَآءُ`, 68:43 `سَٰلِمُونَ`, 68:48 `صَاحِبِ`, and 68:50 `جَعَلَ`/`صَّٰلِحِينَ`.
- Surprising reach: Made status, earned offense, marriage payment, stepchild, tribe-name, spokesperson, captive, guarantor, and protective companion reveal identity as a structured relation rather than a free-standing label.

#### Subchannel A. Conduct and Transformation Produce a Moral Class
- Reading type: surface-primary
- Scene or process: Action accrues as earning or offense, and an act of making places the person into a publicly distinguishable condition.
- Active motifs: transformation into a status (`quranic:root_000248:B002/m01`); soundness from defect (`quranic:root_000737:B001/m01`); handing over or leaving a former condition (`quranic:root_000737:B012/m01`); earning and causing another to acquire (`quranic:root_000239:B003/m01`); offense and transgression (`quranic:root_000239:B004/m01`); one thing standing in another's place (`quranic:root_001273:B007/m01`); occurrence and presence in time (`quranic:root_001332:B001/m01`); position and rank (`quranic:root_001332:B002/m01`).
- Ayah anchors: 68:35 `نَجْعَلُ` [ج ع ل], `مُسْلِمِينَ` [س ل م], and `مُجْرِمِينَ` [ج ر م]; 68:39 `قِيَٰمَةِ` [ق و م]; 68:41/43/48 forms of `ك و ن` [ك و ن].
- Synthesis: Moral identity is neither mere nomenclature nor static essence. Conduct is acquired, transgression becomes an attributable condition, and making or substitution installs a person in a status whose soundness or defect can be tested.

#### Subchannel B. Partnership, Marriage, and Care Define Household Position
- Reading type: mixed
- Scene or process: Shared property, marriage, payment, child-care, and maturity establish who stands as partner, spouse, dependent, or adult companion within a household.
- Active motifs: shared interest and participation (`quranic:root_000791:B001/m01`); partnership through marriage or affinity (`quranic:root_000791:B003/m01`); sincere friendship (`quranic:root_000852:B005/m01`); marriage payment (`quranic:root_000852:B007/m01`); stepchild or dependent under care (`quranic:root_000532:B005/m01`); abandoned child received by another (`quranic:root_001466:B007/m01`); son grown into his father's companion (`quranic:root_000844:B005/m01`).
- Ayah anchors: 68:34/48/49/50 forms of `ر ب ب` [ر ب ب]; 68:41 `شُرَكَآءُ` [ش ر ك] and `صَٰدِقِينَ` [ص د ق]; 68:48 `صَاحِبِ` [ص ح ب]; 68:49 `نُبِذَ` [ن ب ذ].
- Synthesis: Household identity is relational and developmental. Agreement and payment formalize alliance, care assigns dependence, abandonment ruptures it, and maturation can convert a child once under care into a companion.

#### Subchannel C. Collective Naming and Representation Locate a Person in a Group
- Reading type: latent/lexical
- Scene or process: A collective receives a name, members form a body around it, and a recognized leader or speaker stands for the group in public exchange.
- Active motifs: group, followers, or kin-body (`quranic:root_001273:B001/m01`); leader speaking for a group (`quranic:root_000633:B004/m01`); companionship and charge (`quranic:root_000844:B001/m01`); making something a fitting companion (`quranic:root_000844:B004/m01`); tribal names formed from the offense-root (`quranic:root_000239:B011/m01`).
- Ayah anchors: 68:35 `مُجْرِمِينَ` [ج ر م]; 68:39 `قِيَٰمَةِ` [ق و م]; 68:40 `زَعِيمٌ` [ز ع م]; 68:48 `صَاحِبِ` [ص ح ب].
- Synthesis: Group identity requires both membership and representation. Collective naming fixes affiliation, companionship marks durable association, and the spokesperson converts a plurality into one accountable public voice.

#### Subchannel D. Captive, Guarantor, and Protector Are Assigned Reciprocal Roles
- Reading type: latent/lexical
- Scene or process: One person is taken under another's control while a guarantor, custodian, or protective companion assumes responsibility for that person's continued safety or appearance.
- Active motifs: taking a person captive (`quranic:root_000737:B013/m01`); bearing surety and remaining with the guaranteed person (`quranic:root_000840:B003/m01`); preservation through companionship (`quranic:root_000844:B002/m01`); standing surety for a person (`quranic:root_001332:B003/m01`); dependent child and custodian (`quranic:root_000532:B005/m02`).
- Ayah anchors: 68:34/48/49/50 forms of `ر ب ب` [ر ب ب]; 68:35/43 `مُسْلِمِينَ`/`سَٰلِمُونَ` [س ل م]; 68:41/43/48 forms of `ك و ن` [ك و ن]; 68:48 `ٱصْبِرْ` [ص ب ر] and `صَاحِبِ` [ص ح ب].
- Synthesis: These identities arise together: captivity creates dependence, surety creates answerability, and protective companionship makes custody an ongoing relation rather than a momentary seizure.

### 35. [P3 68:34-52] Discourse Coordinates Endpoint, Location, and Reference
- Semantic invariant: Relational and deictic operators place an event at a limit, in a setting, or before an interlocutor, then identify or question the entity under discussion.
- Surface relation: indirect; 68:39 `بَٰلِغَةٌ`/`يَوْمِ`, 68:40/46 `سَلْهُمْ`/`تَسْـَٔلُهُمْ`, 68:41/43/48 forms of `ك و ن`, 68:44 `حَيْثُ`, 68:47 `عِندَهُمُ`, and 68:51 `يَقُولُ`.
- Surprising reach: Endpoint, proximity, accompaniment, vague location, bounded day, demonstrative, relative, interrogative, attention-call, response, copular presence, and formal definition expose the small grammatical operations that stage a claim.

#### Subchannel A. Endpoint, Proximity, and Duration Place the Event
- Reading type: mixed
- Scene or process: Discourse fixes movement at a limit, locates something at or with another thing, and bounds the resulting situation by a day or an open duration.
- Active motifs: endpoint and attained limit (`quranic:root_000076:B001/m01`); “at” as proximal location (`quranic:root_000076:B002/m01`); accompaniment and joining (`quranic:root_000076:B003/m01`); vague location resolved by its clause (`quranic:root_000375:B001/m01`); nearness or presence “at” something (`quranic:root_001052:B004/m01`); reaching an endpoint (`quranic:root_000151:B001/m01`); bounded daylight (`quranic:root_001700:B001/m01`); duration of any length (`quranic:root_001700:B002/m01`).
- Ayah anchors: 68:39 `بَٰلِغَةٌ` [ب ل غ] and `يَوْمِ` [ي و م]; 68:42 `يَوْمَ` [ي و م]; 68:44 `حَيْثُ` [ح ي ث]; 68:47 `عِندَهُمُ` [ع ن د]; surface anchors unavailable for root `ء ل ي`.
- Synthesis: Placement is assembled from distinct relations. A limit answers “how far,” proximity answers “where relative to what,” accompaniment answers “with whom,” and temporal span answers “for how long”; together they turn an unplaced assertion into an event with coordinates.

#### Subchannel B. Pointing, Asking, Answering, and Defining Stabilize the Referent
- Reading type: latent/lexical
- Scene or process: An attention-call opens an exchange, a demonstrative or relative expression selects the referent, a question tests it, and an answer or formal definition closes ambiguity.
- Active motifs: relative “the one who” (`quranic:root_000527:B002/m01`); demonstrative pointer (`quranic:root_000527:B003/m01`); interrogative-relative “what?” (`quranic:root_000527:B004/m01`); attention-opening particle (`quranic:root_001573:B002/m01`); answer or response (`quranic:root_001573:B003/m01`); interrogative substitution (`quranic:root_001573:B004/m01`); request and inquiry (`quranic:root_000661:B001/m01`); formal definition (`quranic:root_001272:B016/m01`); occurrence made present in predication (`quranic:root_001332:B001/m02`).
- Ayah anchors: 68:40/46 `سَلْهُمْ`/`تَسْـَٔلُهُمْ` [س ء ل]; 68:41/43/48 forms of `ك و ن` [ك و ن]; 68:51 `يَقُولُ` [ق و ل]; surface anchors unavailable for roots `ذ و و` and `ه ا ء`.
- Synthesis: Reference is stabilized through an ordered exchange: summon attention, point or relate, interrogate, answer, and define. Copular presence then installs the selected entity inside a proposition rather than leaving it as an unattached name.

## Standalone Subchannels

### S1. [P3 68:34-52] Fish, Circling, and Navigated Evasion
- Reading type: mixed
- Scene or process: A fish moves through managed water, circles an object or pool, evades capture, and expands into an orbital figure watched over by a navigator.
- Active motifs: fish, especially a great fish (`quranic:root_000366:B001/m01`); evasive movement like a fish (`quranic:root_000366:B002/m01`); circling over water or around an object (`quranic:root_000366:B003/m01`); zodiacal fish (`quranic:root_000366:B004/m01`); directed watercourse (`quranic:root_000009:B004/m01`); walking or following a route (`quranic:root_000468:B001/m01`); captain of sailors (`quranic:root_000532:B017/m01`).
- Ayah anchors: 68:41 `يَأْتُ` [ء ت ي]; 68:44 `نَسْتَدْرِجُ` [د ر ج]; 68:48 `صَاحِبِ ٱلْحُوتِ` [ح و ت] and `رَبِّهِ` [ر ب ب].
- Synthesis: The fish-root supplies creature, evasive operation, circular motion, and celestial analogue. Channel, route, and captain make those motions navigable, linking the fish-companion's constrained course to a larger geometry of circling and attempted escape.

### S2. [P3 68:34-52] Ripe Harvest Becomes Stored Drink and Residue
- Reading type: latent/lexical
- Scene or process: Ripe fruit is gathered, sorted from dry remnants, steeped in a vessel, and concentrated into a durable preparation.
- Active motifs: crop yield and fruit (`quranic:root_000009:B007/m01`); pasture or fruit ripe and ready to gather (`quranic:root_000956:B007/m01`); dry dates, pits, and remnants after cutting (`quranic:root_000239:B002/m01`); tamarind fruit (`quranic:root_000840:B009/m01`); dates or raisins steeped in water inside a vessel (`quranic:root_001466:B006/m01`); thick syrup used with food or skin vessels (`quranic:root_000532:B006/m02`).
- Ayah anchors: 68:34/48/49/50 forms of `ر ب ب` [ر ب ب]; 68:35 `مُجْرِمِينَ` [ج ر م]; 68:41 `يَأْتُ` [ء ت ي]; 68:42 `تَسْتَطِيعُونَ` [ط و ع]; 68:48 `ٱصْبِرْ` [ص ب ر]; 68:49 `نُبِذَ` [ن ب ذ].
- Synthesis: The scene begins at readiness, not mere vegetation. Harvest separates usable fruit from dry remnants, steeping transfers fruit into water, and concentration turns it into a preparation that can be kept or used to condition its container.

### S3. [Whole Surah 68:1-52] Consecration Orders Garment, Gathering, Offering, and Prostration
- Reading type: mixed
- Scene or process: A worshipper enters ritual restriction, assumes its marked clothing, joins an appointed gathering, leads an offering to the sanctuary, and reaches the communal place of prostration.
- Active motifs: entering pilgrimage consecration and its abstentions (`quranic:root_000313:B004/m01`); garment of the consecrated worshipper (`quranic:root_000313:B010/m01`); marked pilgrimage season and assembly (`quranic:root_001650:B004/m01`); livestock, wealth, or goods offered to the sanctuary (`quranic:root_001583:B005/m01`); communal prayer and prostration place (`quranic:root_000675:B002/m01`).
- Ayah anchors: 68:7 `مُهْتَدِينَ` [ه د ي]; 68:16 `نَسِمُ` [و س م]; 68:27 `مَحْرُومُونَ` [ح ر م]; 68:42-43 `سُّجُودِ` [س ج د].
- Synthesis: The rite makes the summons to prostration in 68:42-43 a disciplined sequence rather than an isolated pose: restriction, clothing, appointed company, surrendered property, and bodily placement converge. It also pressures the orchard owners' use of restriction: consecration restrains the possessor while directing wealth outward as an offering, whereas their morning plan restrains the needy so the yield can remain enclosed.

### S4. [Whole Surah 68:1-52] Foster-Mothering Transfers Milk to Another's Young
- Reading type: latent/lexical
- Scene or process: Pregnancy becomes visible, an offspring follows its mother, and a herder uses a rolled fostering cloth to make a she-camel accept another's young while retained milk summons the next flow.
- Active motifs: visible pregnancy in camel or ewe (`quranic:root_000531:B010/m01`); young animal following its mother (`quranic:root_000186:B006/m01`); rolled fostering cloth used so a she-camel accepts another's young (`quranic:root_000468:B007/m01`); milk deliberately left in the udder to call forth more (`quranic:root_000478:B003/m01`).
- Ayah anchors: 68:15 `تُتْلَىٰ` [ت ل و]; 68:26 `رَأَ` [ر ء ي]; 68:42-43 `يُدْعَ` [د ع و]; 68:44 `نَسْتَدْرِجُ` [د ر ج].
- Synthesis: This practice materializes replacement and restorative favor across the surah: deliberate care can attach provision to a young animal outside the original maternal bond and keep nourishment moving. It therefore usefully pressures the owners' attempt to bar the needy from the garden and gives concrete force to the hope for replacement in 68:32 and the remaking of status in 68:49-50.

### S5. [Whole Surah 68:1-52] A Hunter Turns the Quarry's Path into a Snare
- Reading type: latent/lexical
- Scene or process: The hunter reads tracks and grooves, sets a noose where the quarry travels, waits through its run-and-pause evasion, and brings successive quarry down.
- Active motifs: road grooves and pasture tracks (`quranic:root_000791:B005/m01`); hunter's noose in which quarry becomes entangled (`quranic:root_000791:B006/m01`); wild quarry running, stopping, and looking behind (`quranic:root_001290:B007/m01`); successive quarry brought down in one release (`quranic:root_000993:B008/m01`).
- Ayah anchors: 68:8/44 `مُكَذِّبِينَ`/`يُكَذِّبُ` [ك ذ ب]; 68:12 `مُعْتَدٍ` [ع د و]; 68:41 `شُرَكَآءُ` [ش ر ك].
- Synthesis: The scene materially reframes the false partners of 68:41 through the same root's hunter's `شَرَك`: what appears to be a shared or traversable path can already be arranged for capture. The quarry's backward look after running also sharpens the surah's staged `نَسْتَدْرِجُ` and `كَيْد`, where partial recognition arrives inside, rather than outside, the enclosing sequence.

### S6. [Whole Surah 68:1-52] Drum and Answering Voice Produce a Public Performance
- Reading type: latent/lexical
- Scene or process: A one-faced drum marks the performance, a lead voice projects, a second singer answers in sequence, and the carried sound becomes pleasurable hearing for an audience.
- Active motifs: one-faced drum (`quranic:root_001281:B012/m01`); emergence and carrying force of the voice (`quranic:root_000239:B008/m01`); answering singer whose voice follows the lead (`quranic:root_000186:B007/m01`); song and pleasurable listening (`quranic:root_000741:B007/m01`); range and distance reached by a voice (`quranic:root_001487:B002/m01`).
- Ayah anchors: 68:15 `تُتْلَىٰ` [ت ل و]; 68:33 `أَكْبَرُ` [ك ب ر]; 68:35 `مُجْرِمِينَ` [ج ر م]; 68:51 `سَمِعُ` [س م ع]; surface anchor unavailable for root `ن د ي`.
- Synthesis: Performance materializes how sound gains social force through rhythm, projection, response, range, and pleasure. It usefully pressures the hostile hearing and accusation in 68:51-52: coordinated uptake and compelling sound can create an audience, but neither pleasure nor repetition establishes whether the utterance is false attribution or `ذِكْرٌ لِّلْعَٰلَمِينَ`.

### S7. [Whole Surah 68:1-52] A Petition Moves a Wrong toward Retaliation or Blood Money
- Reading type: latent/lexical
- Scene or process: A wronged person petitions a governor or judge, authority orders equivalent retaliation, and blood money may stand in place of that retaliatory outcome.
- Active motifs: appeal to a governor or judge for redress against an oppressor (`quranic:root_000993:B005/m01`); retaliation or execution under authority (`quranic:root_000840:B012/m01`); blood money accepted instead of retaliation (`quranic:root_001119:B002/m01`).
- Ayah anchors: 68:3 `غَيْرَ` [غ ي ر]; 68:12 `مُعْتَدٍ` [ع د و]; 68:48 `ٱصْبِرْ` [ص ب ر].
- Synthesis: This procedure gives concrete social stakes to `كَيْفَ تَحْكُمُونَ` and to the refusal to make the submissive and the criminal alike. Judgment must identify the wrong, fit the response to it, and distinguish equivalent retaliation from compensatory substitution; collapsing unlike parties or remedies is itself failed adjudication.

### S8. [Whole Surah 68:1-52] A Stranger Is Received as Guest and Protected Dependent
- Reading type: mixed
- Scene or process: A non-kin arrival enters another people, becomes attached to the group, seeks protected standing, and tests a generous host through the concrete demand for reception and giving.
- Active motifs: stranger entering a people not his own (`quranic:root_000009:B006/m01`); affiliated outsider mixing with a group (`quranic:root_000464:B005/m01`); sanctuary-seeker awaiting covenant or protection (`quranic:root_001583:B007/m01`); generous man crowded by guests and petitioners (`quranic:root_000606:B006/m01`); bringing and giving a thing (`quranic:root_000009:B002/m01`).
- Ayah anchors: 68:7 `مُهْتَدِينَ` [ه د ي]; 68:24 `يَدْخُلَ` [د خ ل]; 68:41 `يَأْتُ` [ء ت ي]; 68:43 `تَرْهَقُ` [ر ه ق].
- Synthesis: The scene directly pressures the resolve in 68:24 that no needy person should enter the garden. Reception is tested precisely by someone without prior kinship or secure membership: arrival, affiliation, protection, and giving can turn an outsider into a dependent presence, while exclusion treats belonging as a precondition for provision.

## Cross-Pericope Channels

### X1. Yield Advances from Input to Growth, Harvest, and Storage
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: causal sequence — water and prepared ground enable growth; cultivation brings yield to ripeness; cutting, use, and storage complete the productive chain.
- Canonical scene placements: `P1/7A` Cloud and Falling Water Mark the Ground; `P1/7B` Covered Garden, Grain Ear, and Aromatic Growth; `P1/7C` Rock Pool, Oil Basin, and Deep Water Store; `P2/10B` Soil Is Prepared and Growth Is Tended; `P2/10C` Ripened Growth Is Cut into Shares; `P2/10D` Morning Converts Harvest into a Scheduled Meal; `P3/22B` Seed-Cover and Fruit-Husk Guard Development; `P3/22C` Cultivation Produces Food, Fiber, Tannin, and Scent; `S2` Ripe Harvest Becomes Stored Drink and Residue.
- Synthesis: P1 supplies the ecological inputs, P2 places human intention and labor inside the production cycle, and P3 shows protection and processing carrying yield beyond immediate consumption. The orchard's destruction is therefore a break in a staged chain whose value never belonged to the final cutting act alone.

### X2. Provision Survives by Reaching Another
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: causal sequence with reversal — gift and care initiate a resource flow, withholding arrests it, and replacement or reception restores the relation between provision and recipient.
- Canonical scene placements: `P1/5A` Favor Moves as Reward, Gift, and Nurture; `P1/5B` The Withholding Hand Produces Scarcity and Weakness; `P1/7D` Herd, Milk, and the Risk of Depletion; `P2/11B` Herds Cycle Between Trough, Pasture, and Return; `P2/11C` Cessation Appears as Dry Rain, Cut Milk, and Denied Access; `P2/18A` Substitution and Repair Restore a Failed Function; `P2/20B` Generosity Reopens the Arrested Flow; `P3/22A` Shielded Garden Gives Its Occupant Ease; `P3/31` Grace Intercepts Exposure and Refashions Status; `S4` Foster-Mothering Transfers Milk to Another's Young; `S8` A Stranger Is Received as Guest and Protected Dependent.
- Synthesis: P1 establishes the opposition between nurture and the withholding hand; P2 makes interruption visible as a failed circuit and repair as renewed transfer; P3 makes favor an intervention that changes placement and status. Foster-mothering and guest reception sharpen the invariant: provision remains beneficent by crossing toward a recipient, not by remaining secured to an original possessor.

### X3. Cover Reverses from Protection to Concealment to Exposure
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: repeated scene signature with contrast and reversal — a boundary creates an interior, but its value depends on whether it protects vulnerability, hides condition, or is removed to disclose and expose.
- Canonical scene placements: `P1/2` Covers Regulate Access to Sight and Interior Truth; `P2/12` An Unseen Night Passage Produces a Visible Morning State; `P3/28` Covering Establishes the Stakes of Disclosure and Exposure.
- Synthesis: P1 distinguishes protective and deceptive cover, P2 turns concealment into a timed passage whose result appears at morning, and P3 follows removal into disclosure, abandonment, or defended survival. The shared mechanism makes exposure an outcome of changed boundary conditions rather than a synonym for knowledge.

### X4. Route Progresses from Guidance through Intent to Entrapment
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: role progression and causal sequence — a route first offers direction, intention then commits a traveler to it, and staged movement can finally convert apparent progress into capture.
- Canonical scene placements: `P1/3A` Marked Route, Leading Guide, and Deviation; `P1/3B` Gait Registers Capacity, Terrain, and Exhaustion; `P2/15A` Intent Is Calculated Before the Body Moves; `P2/15B` Departure Tests Route, Gait, and Capacity to Confront; `P3/29` Reprieve Stages a Gradual Capture; `S1` Fish, Circling, and Navigated Evasion; `S5` A Hunter Turns the Quarry's Path into a Snare.
- Synthesis: P1 supplies orientation and bodily capacity, P2 shows intention selecting and testing a course, and P3 reveals that continued motion can be organized by another agent. The fish and quarry scenes complete the reversal: evasive movement remains inside a navigated or trapped field, so distance traveled is not evidence of escape.

### X5. Speech Changes Hands and Reconfigures Its Speakers
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: repeated social scene signature and role progression — an utterance leaves one speaker, passes through carriers or respondents, reorganizes a group, and returns as public reputation or accusation.
- Canonical scene placements: `P1/3C` Tale-Bearing Is Speech Put on Foot; `P2/14` Group Speech Reconfigures the Speakers; `P3/27` Utterance Summons, Attributes, and Makes Reputation; `S6` Drum and Answering Voice Produce a Public Performance.
- Synthesis: P1 makes harmful speech portable, P2 follows speech as it contracts into consultation and turns speakers toward one another, and P3 tracks the resulting summons, attribution, and remembered name. The performance scene confirms the role progression: coordinated response can amplify an utterance socially without settling whether its attribution is true.

### X6. A Claim Acquires Scope, Bond, and Warrant
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: role progression — discourse first fixes referent and scope, an oath or covenant binds a responsible party, and record, guarantor, and interrogation test the claim's warrant.
- Canonical scene placements: `P1/4B` Covenant, Surety, and Attached Membership; `P1/9` Discourse Operators Allocate Reference, Scope, and Sequence; `P2/16` Oaths Allocate Risk, Exception, and Protection; `P3/23A` Joining Material Becomes Writing, Decree, and Register; `P3/23C` Oath, Guarantor, Partner, and Fulfillment Back the Claim; `P3/23D` Question and Answer Expose the Missing Warrant.
- Synthesis: A claim becomes answerable in stages. P1 prevents an assertion from floating free of reference or obligation, P2 shows that even sworn commitment must specify reservation and protected risk, and P3 asks whether record, responsible backing, and fulfilled action actually exist.

### X7. Joined Parts Become Functional Systems
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: repeated scene signature — separate materials become useful only through cutting, folding, joining, tensioning, and fitting into a load-bearing or containing whole.
- Canonical scene placements: `P1/8` Fitted Parts Make Shelters, Implements, and Cuts; `P2/19` Folding and Joining Build Portable or Fixed Enclosures; `P3/32` Joined Parts Create Load-Bearing and Water-Handling Systems.
- Synthesis: The same fabrication grammar persists while the artifact changes: P1 forms tools and framed shelter, P2 forms portable and fixed enclosure, and P3 forms vessels, hydraulic assemblies, and supporting frames. Wholeness is an achieved coordination of parts, which gives concrete force to the surah's repeated concern with whether words, plans, groups, and claims hold together.

### X8. Restraint Is Judged by What It Protects, Seals, or Releases
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: contrast and reversal — restraint can coordinate care and disciplined passage, or become coercive seizure and no-exit closure; release reveals which function the bond served.
- Canonical scene placements: `P1/4A` Mastery as Care, Knowledge, and Watch; `P1/4C` Obedience, Refusal, and Coercive Hauling; `P1/4D` Arms, Captivity, and Uncompensated Release; `P2/13` Boundary Operations Decide What Remains Inside the Whole; `P3/30` Holding Pressure Can Preserve Control or Seal Distress Inside; `S3` Consecration Orders Garment, Gathering, Offering, and Prostration.
- Synthesis: P1 distinguishes responsible oversight from forced submission, P2 tests control at the boundary between inclusion and exclusion, and P3 locates restraint inside pressure-bearing bodies and closures. Consecration supplies the decisive contrast: self-binding can order worship and outward offering, while coercive binding arrests another's movement or seals distress within.

### X9. Assay Becomes Threshold, Measure, and Fitted Consequence
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: causal sequence — trial exposes condition, excess crosses a limit, comparison measures the resulting burden, and judgment assigns a proportionate or substitutive consequence.
- Canonical scene placements: `P1/6` Assay Exposes Formation and Moral Texture; `P2/10A` Wear and Trial Reveal Condition; `P2/17` Excess Crosses Its Limit and Returns as Overwhelming Force; `P3/23B` Judgment Restrains Error and Brings a Matter to Firmness; `P3/24B` Weight and Valuation Make Burden Comparable; `S7` A Petition Moves a Wrong toward Retaliation or Blood Money.
- Synthesis: P1 establishes testing as disclosure rather than arbitrary pain, P2 joins revealed condition to threshold-crossing and consequence, and P3 adds comparison and adjudicative closure. The redress procedure makes the invariant socially exact: a fitted judgment must distinguish the wrong, the liable party, and the difference between equivalent retaliation and compensatory replacement.

### X10. A Mark Becomes Knowledge Only Through Interpretation
- Pericopes: P1 (68:1-16), P2 (68:17-33), and P3 (68:34-52).
- Bridge: repeated interpretive scene signature with contrast — a visible or audible sign requires a reader, and the same act of perception can yield orientation, misattribution, or destabilizing hostility.
- Canonical scene placements: `P1/1` Legible Surfaces and Attributed Identity; `P2/15C` Sight Corrects the Mistaken Destination; `P3/26` Perception Can Stabilize Knowledge or Strip Away Footing.
- Synthesis: P1 shows marks and crafted surfaces becoming attributed identity, P2 gives sight a corrective role when intention has chosen wrongly, and P3 splits perception between insight and hostile force. The bridge prevents visibility from being equated with truth: knowledge depends on how the sign is read and what relation the perceiver establishes to its bearer.


