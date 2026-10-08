Surah: 71. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S71 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s071/surah.r2/text.md =====
# Surah 71

- 71:1 إِنَّآ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦٓ أَنْ أَنذِرْ قَوْمَكَ مِن قَبْلِ أَن يَأْتِيَهُمْ عَذَابٌ أَلِيمٌۭ
- 71:2 قَالَ يَٰقَوْمِ إِنِّى لَكُمْ نَذِيرٌۭ مُّبِينٌ
- 71:3 أَنِ ٱعْبُدُوا۟ ٱللَّهَ وَٱتَّقُوهُ وَأَطِيعُونِ
- 71:4 يَغْفِرْ لَكُم مِّن ذُنُوبِكُمْ وَيُؤَخِّرْكُمْ إِلَىٰٓ أَجَلٍۢ مُّسَمًّى ۚ إِنَّ أَجَلَ ٱللَّهِ إِذَا جَآءَ لَا يُؤَخَّرُ ۖ لَوْ كُنتُمْ تَعْلَمُونَ
- 71:5 قَالَ رَبِّ إِنِّى دَعَوْتُ قَوْمِى لَيْلًۭا وَنَهَارًۭا
- 71:6 فَلَمْ يَزِدْهُمْ دُعَآءِىٓ إِلَّا فِرَارًۭا
- 71:7 وَإِنِّى كُلَّمَا دَعَوْتُهُمْ لِتَغْفِرَ لَهُمْ جَعَلُوٓا۟ أَصَٰبِعَهُمْ فِىٓ ءَاذَانِهِمْ وَٱسْتَغْشَوْا۟ ثِيَابَهُمْ وَأَصَرُّوا۟ وَٱسْتَكْبَرُوا۟ ٱسْتِكْبَارًۭا
- 71:8 ثُمَّ إِنِّى دَعَوْتُهُمْ جِهَارًۭا
- 71:9 ثُمَّ إِنِّىٓ أَعْلَنتُ لَهُمْ وَأَسْرَرْتُ لَهُمْ إِسْرَارًۭا
- 71:10 فَقُلْتُ ٱسْتَغْفِرُوا۟ رَبَّكُمْ إِنَّهُۥ كَانَ غَفَّارًۭا
- 71:11 يُرْسِلِ ٱلسَّمَآءَ عَلَيْكُم مِّدْرَارًۭا
- 71:12 وَيُمْدِدْكُم بِأَمْوَٰلٍۢ وَبَنِينَ وَيَجْعَل لَّكُمْ جَنَّٰتٍۢ وَيَجْعَل لَّكُمْ أَنْهَٰرًۭا
- 71:13 مَّا لَكُمْ لَا تَرْجُونَ لِلَّهِ وَقَارًۭا
- 71:14 وَقَدْ خَلَقَكُمْ أَطْوَارًا
- 71:15 أَلَمْ تَرَوْا۟ كَيْفَ خَلَقَ ٱللَّهُ سَبْعَ سَمَٰوَٰتٍۢ طِبَاقًۭا
- 71:16 وَجَعَلَ ٱلْقَمَرَ فِيهِنَّ نُورًۭا وَجَعَلَ ٱلشَّمْسَ سِرَاجًۭا
- 71:17 وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا
- 71:18 ثُمَّ يُعِيدُكُمْ فِيهَا وَيُخْرِجُكُمْ إِخْرَاجًۭا
- 71:19 وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا
- 71:20 لِّتَسْلُكُوا۟ مِنْهَا سُبُلًۭا فِجَاجًۭا
- 71:21 قَالَ نُوحٌۭ رَّبِّ إِنَّهُمْ عَصَوْنِى وَٱتَّبَعُوا۟ مَن لَّمْ يَزِدْهُ مَالُهُۥ وَوَلَدُهُۥٓ إِلَّا خَسَارًۭا
- 71:22 وَمَكَرُوا۟ مَكْرًۭا كُبَّارًۭا
- 71:23 وَقَالُوا۟ لَا تَذَرُنَّ ءَالِهَتَكُمْ وَلَا تَذَرُنَّ وَدًّۭا وَلَا سُوَاعًۭا وَلَا يَغُوثَ وَيَعُوقَ وَنَسْرًۭا
- 71:24 وَقَدْ أَضَلُّوا۟ كَثِيرًۭا ۖ وَلَا تَزِدِ ٱلظَّٰلِمِينَ إِلَّا ضَلَٰلًۭا
- 71:25 مِّمَّا خَطِيٓـَٰٔتِهِمْ أُغْرِقُوا۟ فَأُدْخِلُوا۟ نَارًۭا فَلَمْ يَجِدُوا۟ لَهُم مِّن دُونِ ٱللَّهِ أَنصَارًۭا
- 71:26 وَقَالَ نُوحٌۭ رَّبِّ لَا تَذَرْ عَلَى ٱلْأَرْضِ مِنَ ٱلْكَٰفِرِينَ دَيَّارًا
- 71:27 إِنَّكَ إِن تَذَرْهُمْ يُضِلُّوا۟ عِبَادَكَ وَلَا يَلِدُوٓا۟ إِلَّا فَاجِرًۭا كَفَّارًۭا
- 71:28 رَّبِّ ٱغْفِرْ لِى وَلِوَٰلِدَىَّ وَلِمَن دَخَلَ بَيْتِىَ مُؤْمِنًۭا وَلِلْمُؤْمِنِينَ وَٱلْمُؤْمِنَٰتِ وَلَا تَزِدِ ٱلظَّٰلِمِينَ إِلَّا تَبَارًۢا


===== _commentary/v16/work/s071/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر س ل (root_000563): 71:1 أَرْسَلْنَا, 71:11 يُرْسِلِ

- **B001** bir şeyi gönderme veya serbest bırakma — göndermek veya salıvermek · gönderme, yöneltme veya serbest bırakma · gönderilmiş rüzgarlar veya görevlendirilmiş melekler
  أصل واحد يدل على الانبعاث والامتداد (maqayis)؛ أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة (sihah)؛ إرسال الله أنبياءه وإرسال الشياطين تخليتهم وإياهم (tahdhib)؛ الإرسال يقابل الإمساك (mufradat)
- **B002** haber taşıyıcısı veya taşınan haber — elçi veya haberci · taşınan ileti veya haber · ileti veya taşınan haber · iletiler veya taşınan haberler · elçiler veya haberciler
  الرسول معروف (maqayis)؛ الرسول بمعنى الرسالة والرسائل جمع الرسالة (ayn)؛ أرسلت فلانا في رسالة فهو مرسل ورسول والرسول أيضا الرسالة (sihah)؛ الرسول معناه الذي يتابع أخبار الذي بعثه (tahdhib)؛ الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة (mufradat)
- **B003** harekette veya uzanışta yumuşak akıcılık — rahat ve yumuşak ilerleyiş · rahat yürüyen, bacakları ve eklemleri yumuşak dişi deve · rahat yürüyen deve · düz ve salık saç · saçın düzleşip salık duruma gelmesi · hızlı veya rahatça ilerleyen deve sürüleri · uzun ya da yumuşak ve rahat hareketli bacaklar
  فالرسل السير السهل وناقة رسلة لينة المفاصل وشعر رسل (maqayis)؛ ناقة رسلة القوائم سلسة لينة المفاصل (ayn)؛ شعر رسل وبعير رسل وناقة رسلة وإبل مراسيل (sihah)؛ الرسل الذي فيه لين واسترخاء وناقة مرسال رسلة القوائم (tahdhib)؛ ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا (mufradat)
- **B004** acele etmeden ölçülü ilerleme — Acele etme; yavaş ve sakin ol · işte veya konuşmada sakin, ağırbaşlı ve temkinli davranma · metni acele etmeden açık seçik okuma
  على رسلك أي على هينتك (maqayis)؛ تكلم على رسلك والترسل في الأمر والمنطق كالتمهل والتوقر والتثبت (ayn)؛ على رسلك أي اتئد فيه وترسل في قراءته (sihah)؛ الترسل من الرسل في الأمور والمنطق كالتمهل والتوقر والتثبت والترسيل التحقيق بلا عجلة (tahdhib)؛ على رسلك إذا أمرته بالرفق (mufradat)
- **B005** peş peşe gelen topluluklar — deve, koyun veya başka varlıklardan oluşan sürü · gruplar halinde, birbirinin ardından
  الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا (maqayis)؛ الرسل القطيع من كل شيء وجمعه أرسال (ayn)؛ الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا (sihah)؛ جاءت الإبل أرسالا رسل بعد رسل والرسل قطيع من الإبل (tahdhib)؛ جاءوا أرسالا أي متتابعين (mufradat)
- **B006** bol ve sürekli gelen süt — süt; özellikle bol ve sürekli gelen süt · hayvanlarından süt elde eder duruma gelmek
  الرِّسل اللبن لأنه يترسل من الضرع (maqayis)؛ والرسل اللبن (ayn)؛ والرسل أيضا اللبن وقد أرسل القوم أي صار لهم اللبن (sihah)؛ كثر الرسل العام أي كثر اللبن (tahdhib)؛ الرسل اللبن الكثير المتتابع الدر (mufradat)
- **B007** ısınıp güvenerek açılma — birine veya bir şeye ısınıp güvenmek · sana güvenip yanında rahat davranan kimse
  استرسلت إلى الشيء إذا انبعثت نفسك إليه وأنست (maqayis)؛ الاسترسال إلى شيء كالاستئناس والطمأنينة (ayn)؛ استرسل إليه أي انبسط واستأنس (sihah)؛ الاسترسال إلى الإنسان كالاستئناس والطمأنينة (tahdhib)
- **B008** karşılıklı iletişim ve eşlik — karşılıklı haberleşmek veya birbirine ayak uydurmak · atışmada veya başka bir uğraşta eşlik eden kişi · şarkıda veya işte bir öncekinin ardından giden eşlikçi
  رسيل الرجل الذي يقف معه في نضال أو غيره (maqayis)؛ راسله مراسلة فهو مراسل ورسيل الرجل الذي يراسله في نضال أو غيره (sihah)؛ العرب تسمي المراسل في الغناء والعمل المتالي (tahdhib)
- **B009** taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın [kalıp] — eşi ölmüş, boşanmış veya ayrılmak üzere olduğu için taliplerin haber gönderdiği kadın
  المرأة المراسل التي مات بعلها فالخطاب يراسلونها (maqayis)؛ امرأة مراسل كان لها زوج والخطاب يراسلونها الخطبة (ayn)؛ امرأة مراسل يموت زوجها أو أحست منه أنه يريد تطليقها (sihah)؛ امرأة مراسل وهي التي مات عنها زوجها أو طلقها (tahdhib)
- **B010** rahatlık ve gönül hoşluğuyla verme [kalıp] — sıkıntısında ve rahatlığında; gönül hoşluğuyla verirken
  النجدة الشدة والرسل الرخاء (maqayis)؛ في نجدتها ورسلها يريد الشدة والرخاء (sihah)؛ إلا من أعطى في رسلها أي بطيب نفس منه (tahdhib)
- **B011** özel adlandırma kümesi — kısa ok · iki damar · belirli bir topluluğun damızlık erkek devesi · aktarım zinciri kesintili söz · boncuklu kolye · başını henüz örtmeyen küçük kız
  الراسلان عرقان (maqayis)؛ المرسال سهم قصير (sihah)؛ هذا رسيل بني فلان أي فحل إبلهم وحديث مرسل والمرسلة القلادة وجارية رسل (tahdhib)

## ق و م (root_001273): 71:1 قَوْمِهِۦٓ, 71:1 قَوْمَكَ, 71:2 يَٰقَوْمِ, 71:5 قَوْمِى

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

## ن ذ ر (root_001488): 71:1 أَنذِرْ, 71:2 نَذِيرٌ

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ق ب ل (root_001198): 71:1 قَبْلِ

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

## ء ت ي (root_000009): 71:1 يَأْتِيَهُمْ

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

## ع ذ ب (root_000994): 71:1 عَذَابٌ

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

## ء ل م (root_000046): 71:1 أَلِيمٌ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ق و ل (root_001272): 71:2 قَالَ, 71:5 قَالَ, 71:10 فَقُلْتُ, 71:21 قَالَ, 71:23 وَقَالُوا۟, 71:26 وَقَالَ

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

## ECHO ق ل ل (root_001251): for 71:2 قَالَ, 71:5 قَالَ, 71:10 فَقُلْتُ, 71:21 قَالَ, 71:23 وَقَالُوا۟, 71:26 وَقَالَ: withheld observed target; not identity

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

## ب ي ن (root_000170): 71:2 مُّبِينٌ

- **B001** ayrılıp kopma — ayrılık ve kopuş · ayrılmak, kopmak, kesilip ayrılmak · karşılıklı ayrılma ve uzaklaşma
  البين الفراق (maqayis;sihah)؛ البينونة مصدر بأن يبين بينا وبينونة أي قطع (ayn)؛ البين مصدر بان يبين بينا (jamhara)؛ بان كذا أي انفصل (mufradat)
- **B002** arada olma — iki veya daha çok şey arasındaki orta ve aralık · önünde, yanında veya yakınında · topluluğun içinden veya topluluğa dahil
  بين بمعنى وسط (sihah)؛ بين موضوع للخلالة بين الشيئين ووسطهما (mufradat)؛ لا يستعمل بين إلا فيما كان له مسافة أو له عدد ما اثنان فصاعدا (mufradat)
- **B003** arayı bağlayan ilişki — taraflar arasındaki bağ ve bağlantı · aranızdaki akrabalık, yakınlık ve sevgi durumları
  البين الوصل (ayn;sihah)؛ لقد تقطع بينكم أي وصلكم (mufradat)؛ ذات بينكم أي الأحوال التي تجمعكم من القرابة والوصلة والمودة (mufradat)
- **B004** açığa çıkıp belirginleşme — görünmek, açığa çıkmak, belirginleşmek · açık hale getirmek ve ortaya koymak · açık kanıt veya açık tanıklık · açık veya açıklayıcı işaretler
  بان الشيء وأبان إذا اتضح وانكشف (maqayis)؛ البيان معروف وبان الشيء وأبان وتبين وبين واستبان (ayn)؛ بان الشيء بيانا اتضح فهو بين (sihah)؛ البينة الدلالة الواضحة (mufradat)
- **B005** anlamı açıkça ortaya koyma — anlamı söz, yazı veya işaretle açıkça ortaya koyma · açık ve düzgün konuşan adam
  أبين من فلان أي أوضح كلاما منه (maqayis)؛ البين من الرجال الفصيح (ayn)؛ البيان الفصاحة واللسن (sihah)؛ البيان الكشف عن الشيء وهو أعم من النطق (mufradat)
- **B006** geniş uzaklık — ikisi arasında büyük uzaklık · dibi uzak veya geniş kuyu
  أصل واحد وهو بعد الشيء (maqayis)؛ البائنة البئر البعيدة القعر الواسعة (sihah)؛ بيون لبعد ما بين الشفير والقعر (mufradat)
- **B007** göz erimindeki arazi parçası — göz erimindeki arazi parçası, yöre veya kabarık yer
  البين قطعة من الأرض قدر مد البصر (maqayis)؛ البين الغلظ من الأرض (jamhara)؛ البين بالكسر القطعة من الأرض قدر منتهى البصر (sihah)؛ البين أيضا الناحية (sihah)
- **B008** bağlı yerinden ayrılma [kalıp] — devenin ayağının yanından açılması · teli gövdesinden uzak duran yay · başını gövdesinden kesip ayırmak
  بانت يد الناقة عن جنبها (ayn)؛ قوس بائن وهي التي بان وترها عن كبدها (ayn)؛ ضربه فأبان رأسه من جسده وفصله (sihah)؛ البائنة القوس التي بانت عن وترها كثيرا (sihah)
- **B009** sol yandan sağan kişi — sağımda hayvanın sol yanından gelen sağan
  البائن أحد الحالبين والآخر يسمى المستعلي (ayn)؛ البائن الذي يأتي الحلوبة من قبل شمالها والمعلى من قبل يمينها (sihah)
- **B010** o sırada — o sırada, bir şey olurken
  قولك بينا فلان معناه بينما (ayn)؛ بينا نحن نرقبه أتانا أي أتانا بين أوقات رقبتنا إياه (sihah)؛ يزاد في بين ما أو الألف فيجعل بمنزلة حين (mufradat)
- **B011** iki arada kalmış hal — iki uç arasında kalan orta veya zayıf hal
  هذا الشيء بين بين أي بين الجيد والرديء (sihah)؛ الهمزة المخففة تسمى بين بين (sihah)؛ يسقط بين بينا أي يتساقط ضعيفا غير معتد به (sihah)
- **B012** geri dönüşsüz boşanma [kalıp] — geri dönüş hakkını kesen boşanma
  تطليقة بائنة وهي فاعلة بمعنى مفعولة (sihah)
- **B013** ayrılık uğursuzu kuş [kalıp] — ayrılığı uğursuz biçimde haber verdiği sayılan kuş
  غراب البين يقال هو الأبقع (sihah)؛ غراب البين هو الأحمر المنقار والرجلين (sihah)؛ يحتم بالفراق (sihah)

## ع ب د (root_000973): 71:3 ٱعْبُدُوا۟, 71:27 عِبَادَكَ

- **B001** özgür olmayan, sahip olunan kişi — özgür olmayan, sahip olunan kişi · köleler · köle doğmuş veya kuşaklar boyunca köle kalmış kişiler
  العبد وهو المملوك (maqayis)؛ العبد المملوك وجمعه عبيد (ayn)؛ العبد ضد الحر (jamhara)؛ العبد خلاف الحر والجمع عبيد (sihah)؛ العبيد مماليك (tahdhib)؛ عبد بحكم الشرع الإنسان الذي يصح بيعه وابتياعه (mufradat)
- **B002** Tanrı'ya ait sayılan insan veya topluluk — Tanrı'nın kulu · Tanrı'nın kulları veya ona bağlı topluluk · Tanrı'ya ait sayılan bütün kullar
  تفرقة ما بين عباد الله والعبيد المملوكين (maqayis)؛ العبد الإنسان حرا أو رقيقا هو عبد الله (ayn)؛ فادخلي في عبادي أي في حزبي (sihah)؛ عبد بالإيجاد وذلك ليس إلا لله (mufradat)
- **B003** boyun eğerek itaat ve tapınma — Tanrı'ya boyun eğerek tapındı · boyun eğerek tapınma · kendini tapınmaya verme · sahte tanrısal güce boyun eğip itaat etti · sahte tanrısal güçlere veya putlara tapan topluluk
  عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis;ayn)؛ تعبدت للرجل إذا تذللت له (jamhara)؛ العبادة الطاعة والتعبد التنسك (sihah)؛ إياك نعبد إياك نطيع الطاعة التي نخضع معها (tahdhib)؛ العبودية إظهار التذلل والعبادة غاية التذلل (mufradat)
- **B004** köleleştirmek veya köle gibi boyunduruk altına almak — onu köleleştirdi · kişiyi ezip köleleştirdi; topluluğu köle edindi · onu köle durumuna getirdi · özgür olsa da onu köle gibi boyunduruk altına aldı
  استعبدت فلانا اتخذته عبدا (maqayis;ayn)؛ عبدت الرجل إذا ذللته وعبدت القوم اتخذتهم عبيدا (jamhara)؛ التعبيد الاستعباد (sihah)؛ عبدت العبيد وأعبدتهم أي صيرتهم عبيدا (tahdhib)؛ عبدت فلانا إذا ذللته وإذا اتخذته عبدا (mufradat)
- **B005** düzleşmiş yol, katranlanmış deve veya kaplanmış gemi — çok geçilerek düzleşmiş yol · derisi baştan başa katranlanmış ve uysallaştırılmış deve · katranla kaplanmış gemi
  الطريق المعبد وهو المسلوك المذلل (maqayis)؛ طريق معبد أي مذلل (jamhara;mufradat)؛ البعير المعبد المهنوء بالقطران المذلل (maqayis;sihah)؛ المعبدة السفينة المقيرة (sihah;tahdhib)؛ المعبد من الإبل الذي عم جلده بالقطران (tahdhib)
- **B006** saygı gösterilip hizmet edilen kişi — saygı gösterilen, yüceltilen ve hizmet edilen kişi
  المعبد المكرم والمعظم كأنه يعبد (jamhara)؛ المعبد أي معظما مخدوما (tahdhib)
- **B007** güç, sağlamlık ve dayanıklılık — güç, sağlamlık ve dayanıklılık · güçlü ve semiz dişi deve · kumaşının hiç dayanıklılığı yok
  العبدة وهي القوة والصلابة (maqayis)؛ ناقة ذات عبدة أي ذات قوة وسمن وما لثوبك عبدة أي قوة (sihah)؛ العبدة البقاء وقيل الشدة (tahdhib)
- **B008** incinmiş gurur, öfke veya kederli iç duygulanım — incinmiş gurur, öfke, keder veya iç sıkıntısı · gururu incindiği için sustu
  العبد مثل الأنف والحمية (maqayis)؛ العبد الأنفة وعبدت فصمت أي أنفت فسكت (jamhara)؛ العبد بالتحريك الغضب والأنف والاسم العبدة (sihah)؛ العبد الأنف والحمية ويقال عبد عليه أي غضب والعبد الحزن والوجد (tahdhib)
- **B009** gecikmeden yapmak veya koşuda biraz hızlanmak [kalıp] — yapmakta gecikmedi · koşarken biraz hızlandı
  ما عبد أن فعل ذاك أي ما لبث (sihah;tahdhib)؛ عبد يعدو إذا أسرع بعض الإسراع (tahdhib)
- **B010** her yana dağılmış kümeler, nesneler veya yollar — her yana dağılmış insan kümeleri, nesneler veya yollar
  العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)؛ العباديد والعبابيد الأطراف البعيدة والأشياء المتفرقة والطرق المختلفة (tahdhib)
- **B011** bineği yüzünden yolda kalma veya güçlükle direnen deve — bineği yorulduğu, zarar gördüğü veya kaybolduğu için yolda kaldı · insanlara güçlük çıkararak direnen deve
  أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)؛ أعبد به إذا ذهبت راحلته وكذلك أبدع به (tahdhib)؛ بعير متعبد ومتأبد إذا امتنع على الناس صعوبة (tahdhib)
- **B012** güzel koku maddesi ezme taşı — güzel koku maddelerini ezme taşı
  العبدة صلاءة الطيب (jamhara)

## ء ل ه (root_000047): 71:3 ٱللَّهَ, 71:4 ٱللَّهِ, 71:13 لِلَّهِ, 71:15 ٱللَّهُ, 71:17 وَٱللَّهُ, 71:19 وَٱللَّهُ, 71:23 ءَالِهَتَكُمْ, 71:25 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 71:3 ٱللَّهَ, 71:4 ٱللَّهِ, 71:13 لِلَّهِ, 71:15 ٱللَّهُ, 71:17 وَٱللَّهُ, 71:19 وَٱللَّهُ, 71:23 ءَالِهَتَكُمْ, 71:25 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## و ق ي (root_001677): 71:3 وَٱتَّقُوهُ

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

## ط و ع (root_000956): 71:3 وَأَطِيعُونِ

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

## ECHO س ط ع (root_000706): for 71:3 وَأَطِيعُونِ: withheld observed target; not identity

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

## غ ف ر (root_001096): 71:4 يَغْفِرْ, 71:7 لِتَغْفِرَ, 71:10 ٱسْتَغْفِرُوا۟, 71:10 غَفَّارًا, 71:28 ٱغْفِرْ

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

## ذ ن ب (root_000521): 71:4 ذُنُوبِكُمْ

- **B001** günah veya kötü sonuç doğuran suç — günah, suç veya kötü sonuç doğuran davranış · günah ya da suç işlemek
  الذنب والجرم (maqayis)؛ الذنب معروف أذنب يذنب إذنابا (jamhara)؛ الذنب الجرم وقد أذنب الرجل (sihah)؛ الذنب الإثم والمعصية (tahdhib)؛ يستعمل في كل فعل يستوخم عقباه (mufradat)
- **B002** kuyruk; bir şeyin arka ucu veya sonu — hayvan kuyruğu veya bir şeyin arka ucu · kuşun kuyruğu veya kuyruk kökü; at ve devede de kullanılan ad · bir şeyin sonu veya arka ucu · uzun kuyruklu at · başlığından kuyruk gibi bir parçayı aşağı sarkıtmak · çok öne geçip yakalanamaz olmak · geçmiş bir işin ardından gidip kaçırdığına hayıflanmak
  ذنب وهو مؤخر الدواب (maqayis)؛ ذنب الدابة معروف (jamhara)؛ ذنب الطائر وذناباه وذنب الفرس وذناباه (jamhara)؛ الذنب واحد الأذناب والذنابى ذنب الطائر (sihah)؛ ذنب كل شيء آخره (tahdhib)؛ ذنب الدابة وغيرها معروف (mufradat)
- **B003** ardından giden takipçiler — halkın aşağı görülen, geriden gelen takipçileri · birinin veya bir şeyin ardından gelen takipçi · sürünün kuyruğu yanında duran veya izini bırakmadan ardından giden kişi · takipçileriyle birlikte gelmek
  الأتباع الذنابي (maqayis)؛ أذناب الناس رذالهم (jamhara)؛ الذنابى الأتباع والذانب التابع (sihah)؛ ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء (tahdhib)؛ يعبر به عن المتأخر والرذل (mufradat)
- **B004** su yatağı ve vadinin son kesimi — yamaçlı dere yataklarındaki su akış yolları · vadinin veya nehrin sonu, suyunun ulaştığı yer · iki yamaçlı dere yatağı arasındaki su yolu · su yolu veya çayırlıktan dışarı akan küçük kanal
  المذانب مذانب التلاع وهي مسايل الماء فيها (maqayis)؛ ذنبة الوادي والنهر آخره وذِنابته (jamhara)؛ المذنب مسيل ماء وذنابة الوادي (sihah)؛ ذنب التلعة ومذنب النهر والمذنب كهيئة الجدول (tahdhib)؛ مذانب التلاع لمسائل مياهها (mufradat)
- **B005** hurmanın uçtan başlayarak kısmen olgunlaşması — bir ucundan olgunlaşmaya başlamış hurma · ham hurmanın kuyruk sayılan ucundan olgunlaşmaya başlaması · ucu olgunlaşmaya başlamış ham hurma
  المذنب من الرطب ما أرطب بعضه (maqayis)؛ ذنب البسر وأذنب إذا أرطب مما يلي أقماعه وهو التذنوب (jamhara)؛ التذنوب البسر الذي قد بدأ فيه الإرطاب من قبل ذنبه (sihah)؛ إذا بدت نكت من الإرطاب في البسر من قبل ذنبها قيل قد ذنبت فهي مذنبة (tahdhib)؛ المذنب ما أرطب من قبل ذنبه (mufradat)
- **B006** kişiye düşen pay veya nasip — pay veya nasip, özellikle azaptan düşen pay · eksik bir paya razı olmak
  الثالث كالحظ والنصيب (maqayis)؛ الذنوب في التنزيل هو النصيب (jamhara)؛ الذنوب النصيب (sihah)؛ تذهب به إلى النصيب والحظ (tahdhib)؛ استعير للنصيب (mufradat)
- **B007** kova; özellikle büyük, dolu veya kuyruk ipli olanı — büyük, dolu veya kuyruk ipi bulunan kova
  الذنوب الدلو (jamhara)؛ الذنوب الدلو الملأى ماء (sihah)؛ الذنوب الدلو العظيمة (tahdhib)؛ الدلو التي لها ذنب (mufradat)
- **B008** kepçe — kepçe veya büyük servis kaşığı
  المذانب أيضا المغارف والواحدة مذنب ومذنبة (jamhara)؛ المذنب المغرفة (sihah)؛ المذانب المغارف واحدها مذنبة (tahdhib)
- **B009** tilkikuyruğu da denen bir bitki — tilkikuyruğu da denen bilinen bir bitki
  الذنبان ضرب من النبت (jamhara)؛ الذنبان نبت (sihah)؛ الذنبان نبت معروف الواحدة ذنبانة وبعض العرب تسميه ذنب الثعلب (tahdhib)
- **B010** hayvanın kuyruğa bağlı özel davranışı — çekirgenin yumurtlamak için arka kısmını yere saplaması · kertenkelenin kuyruğu önde geri çıkması veya kuyruğuyla vurması · hayvanın kuyruğa bağlı çiftleşme veya vurma davranışı
  ذنب الجراد إذا غرز ليبيض (jamhara)؛ ذنب الضب إذا خرج بذنبه من جحره موليا (jamhara)؛ التذنيب للضباب والفراش إذا أرادت التعاظل والسفاد (tahdhib)؛ إنما يقال للضب مذنب إذا ضرب بذنبه (tahdhib)

## ء خ ر (root_000019): 71:4 وَيُؤَخِّرْكُمْ, 71:4 يُؤَخَّرُ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ء ج ل (root_000016): 71:4 أَجَلٍ, 71:4 أَجَلَ

- **B001** belirlenmiş süre, son zaman ve o zamana erteleme — belirlenmiş süre veya son zaman · adı konmuş belirli süre · ölüm zamanı yaklaştı · hemen olmayıp sonraya kaldı · sonraya bırakılmış olan · belirli bir zamana ertelenmiş · öteki dünya · ona belirli bir süre koydu · süre istedi, o da süre verdi
  الأجل غاية الوقت في الموت ومحل الدين ونحوه (ayn;tahdhib)؛ الأجل مدة الشيء (sihah)؛ الأجل المدة المضروبة للشيء (mufradat)؛ الأجيل المرجأ أي المؤخر إلى وقت والآجل نقيض العاجل (maqayis)
- **B002** nedeniyle veya yüzünden — bundan dolayı, bunun yüzünden · senin yüzünden veya senin için · bundan dolayı · sen böyle olduğun için
  فعلت ذاك من أجل كذا ومن جراء كذا أي من أجله (ayn)؛ فعلت ذاك من أجلك ومن إجلك ومن أجلاك أي من جراك (sihah)؛ من أجلاك وإجلاك ومن جلالك بمعنى واحد (tahdhib)؛ من أجل ذلك فعلت كذا محمول على أجلت الشيء أي جنيته (maqayis)
- **B003** evet, doğrudur — evet, doğrudur
  قولهم أجل إنما هو جواب مثل نعم (sihah)؛ قولهم أجل في الجواب هو من هذا الباب كأنه يريد انتهى وبلغ الغاية (maqayis)
- **B004** yaban sığırı sürüsü ve sürüleşme — yaban sığırı sürüsü · yaban sığırı sürüleri · sürü veya sürüler haline geldi
  الإجل القطيع من بقر الوحش والجميع الآجال وتأجل الصوار صار قطيعا قطيعا (ayn)؛ الإجل القطيع من بقر الوحش والجمع الآجال وتأجلت البهام أي صارت آجالا (sihah)؛ الأجل القطيع من بقر الوحش وجمعه الآجال (tahdhib)؛ الإجل القطيع من بقر الوحش والجمع آجال (maqayis)
- **B005** kötülük işleyip hedefe yöneltme — başlarına kötülük getirip körükledi · kötülük işleyip yöneltme
  أجل عليهم شرا أجلا أي جناه وبحثه (ayn)؛ أجل عليهم شرا يأجل ويأجل أجلا أي جناه وهيجه (sihah)؛ أجلت عليهم آجل أجلا أي جررت جريرة (tahdhib)؛ الأجل مصدر أجل عليهم شرا أي جناه وبحثه (maqayis)
- **B006** boyun ağrısı, buna yol açan yatış ve tedavisi — boyun ağrısı · boynu üzerine yatıp ağrı çekti · boyun ağrısını tedavi etme · boynum ağrıyor, beni tedavi edin
  الأجل وجع في العنق (ayn)؛ الإجل وجع في العنق وقد أجل الرجل أي نام على عنقه فاشتكاها والتأجيل المداواة منه (sihah)؛ الإجل وجع في العنق وبي إجل فأجلوني أي داووني (tahdhib)؛ الإجل وجع في العنق وبي إجل فأجلوني أي داووني منه (maqayis)
- **B007** su biriktiren havuz ve suyun toplanması — su biriktiren havuz veya su birikintisi · su biriktiren havuzlar · su birikintisi · su toplandı · toplanmış su · hurma ağacın için havuz yap
  المأجل شبه حوض واسع يؤجل فيه ماء البئر وماء القناة (ayn)؛ المأجل مستنقع الماء وقد تأجل الماء وماء أجيل أي مجتمع (sihah)؛ المأجل شبه حوض واسع يؤجل فيه ماء القناة والمأجل الجبأة التي يجتمع فيها مياه الأمطار (tahdhib)؛ المأجل شبه حوض واسع يؤجل فيه ماء البئر أو القناة (maqayis)؛ الماجل مستنقع الماء وهذا من باب أجل (maqayis)
- **B008** sürü hayvanlarını otlakta tutma — develerini veya sürülerini otlakta tuttular · sürü hayvanlarını otlakta tutma
  الأجل مصدر قولك أجلوا إبلهم أي حبسوها في المرعى (ayn)؛ أجلوا مالهم يأجلونه أجلا أي حبسوه والأصل في ذلك الزاء أزلوه (maqayis)

## س م و (root_000745): 71:4 مُّسَمًّى, 71:11 ٱلسَّمَآءَ, 71:15 سَمَٰوَٰتٍ

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

## ECHO و س م (root_001650): for 71:4 مُّسَمًّى, 71:11 ٱلسَّمَآءَ, 71:15 سَمَٰوَٰتٍ: withheld observed target; not identity

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

## ج ي ء (root_000281): 71:4 جَآءَ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · geliş; varış · bir kez geliş veya geliş biçimi · sık sık iyilik getiren · iyi ki geldin
  جاء يجيء مجيئا (maqayis;mufradat)؛ جاء فلان يجيء جيئة إذا جاء مرة واحدة وجيئة حسنة (jamhara)؛ المجئ: الاتيان، جاء يجئ جيئة، وجئت مجيئا حسنا (sihah)؛ المجيء كالإتيان لكن المجيء أعم ويقال في الأعيان والمعاني ولمن قصد مكانا أو عملا أو زمانا (mufradat)
- **B002** gelip gitmede üstün gelmek [kalıp] — benimle sık gelme yarışına girdi, ben de onu geçtim
  جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ وجاءانى على فاعلنى فجئته أجيئه، أي غالبني بكثرة المجئ فغلبته (sihah)
- **B003** suyun biriktiği çukur veya yer — suyun biriktiği yer veya büyük çukur · tuzlu ya da idrar karışmış kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره ويقال هي جيئة (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون، والموضع الذي يجتمع فيه الماء، والحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ جية من ماء أي ماء ناقع خبيث (tahdhib)
- **B004** bir şeyi getirmek veya hazır bulundurmak — sık sık iyilik getiren · bir şeyi getirmek veya hazır bulundurmak · onu getirmek
  أجأته، أي جئت به (sihah)؛ جاءه بكذا وأجاءه، وجاء بكذا: استحضره (mufradat)
- **B005** birini bir şeye zorlamak [kalıp] — onu belirli bir şeye zorlamak · seni buna gerek duyar duruma düşürmek
  أجأته إلى كذا بمعنى ألجأته واضطررته إليه (sihah)؛ أجاءها المخاض إلى جذع النخلة، قيل: ألجأها، وإنما هو معدى عن جاء (mufradat)
- **B006** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح، يقال: جاءت جائية الجراح (tahdhib)

## ج ي ء (root_000282): 71:4 جَآءَ

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## ك و ن (root_001332): 71:4 كُنتُمْ, 71:10 كَانَ

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

## ع ل م (root_001040): 71:4 تَعْلَمُونَ

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

## ر ب ب (root_000532): 71:5 رَبِّ, 71:10 رَبَّكُمْ, 71:21 رَّبِّ, 71:26 رَّبِّ, 71:28 رَّبِّ

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

## ECHO ر ب و (root_000537): for 71:5 رَبِّ, 71:10 رَبَّكُمْ, 71:21 رَّبِّ, 71:26 رَّبِّ, 71:28 رَّبِّ: withheld observed target; not identity

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

## د ع و (root_000478): 71:5 دَعَوْتُ, 71:6 دُعَآءِىٓ, 71:7 دَعَوْتُهُمْ, 71:8 دَعَوْتُهُمْ

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

## ECHO د ع ع (root_000477): for 71:5 دَعَوْتُ, 71:6 دُعَآءِىٓ, 71:7 دَعَوْتُهُمْ, 71:8 دَعَوْتُهُمْ: withheld observed target; not identity

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

## ل ي ل (root_001392): 71:5 لَيْلًا

- **B001** gündüzün karşıtı olan gece ve onun karanlığı — gündüzün karşıtı olan gece · gece karanlığı · tek bir gece · geceler · geceler · geceler · çok karanlık ve çetin gece · çok karanlık gece · uzun ya da şiddeti pekiştirilmiş gece · ayın en karanlık ve son gecesi
  الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)
- **B002** geceye girme ya da geceleyin iş görüp yol alma — geceye göre karşılıklı işlem yapma · geceye girmek · gece yol alan veya gece yolculuğuna dayanabilen kimse
  عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)
- **B003** bugüne göre belirlenen en yakın gece — bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece
  إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)
- **B004** bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı — bir kadın adı · şarap için kullanılan örtülü ad
  وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)

## ن ه ر (root_001559): 71:5 وَنَهَارًا, 71:12 أَنْهَٰرًا

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

## ز ي د (root_000657): 71:6 يَزِدْهُمْ, 71:21 يَزِدْهُ, 71:24 تَزِدِ, 71:28 تَزِدِ

- **B001** artma, büyüme ya da artırma — kendiliğinden arttı ve büyüdü · onu artırdı veya ona daha çok verdi · artış, büyüme veya bir şeye başka bir öğenin katılması · ek artış ya da fazladan şey · artmış veya başkasından fazla · artış · artış · belirtilen sayıyı aşan topluluk · bunu ötekine ek olarak yaparım · anlatılandan da fazlası oldu · fiyat yükseldi
  أصل يدل على الفضل (maqayis)؛ زدته زيدا وزيادة (ayn)؛ الزيادة النمو (sihah)؛ زاد الشيء يزيد وزدته أنا أزيده زيادة (tahdhib)؛ الزيادة أن ينضم إلى ما عليه الشيء في نفسه شيء آخر (mufradat)
- **B002** fazladan bölüm ya da uzantı — fazlalıklar ve ek parçalar · uzuvlardaki fazladan parçalar veya uzantılar · karaciğerin yanında asılı küçük parça · olağandan fazla parmaklar · bedendeki fazladan parçalara dayanarak verilmiş takma ad
  شيء كثير الزيايد أي الزيادات (maqayis)؛ زيادة الكبد قطيعة معلقة منها (ayn)؛ زائدة الكبد هنية منها صغيرة إلى جنبها (sihah)؛ الزوائد في قوائم الدابة (tahdhib)؛ زيادة الأصابع والزوائد في قوائم الدابة وزيادة الكبد (mufradat)
- **B003** ölçüyü zorlayarak aşma [kalıp] — kükremesini, sesini ve saldırısını ölçünün ötesine taşıyan aslan · yürüyüşünde gücünü aşacak ölçüde kendini zorlayan dişi deve · konuşurken gereğinden fazla zorlamaya ve abartıya kaçmak · anlatıda yalan söyleme veya yapmacık abartıya kaçma · orta hızlı yürüyüşten daha hızlı gitme
  الأسد ذو زوائد وهو الذي يتزيد في زئيره وصولته (maqayis)؛ الناقة تتزيد في سيرها أي تتكلف فوق قدرها (ayn)؛ التزيد في الحديث الكذب (sihah)؛ الإنسان يتزيد في حديثه وكلامه إذا تكلف مجاوزة ما ينبغي (tahdhib)
- **B004** daha çoğunu isteme ve açık artırmada yarışma — onu yetersiz buldu veya hoşnut olmadığı bir iş için kınadı · verdiğinden daha çoğunu ondan istedi · sana verilenden daha çoğunu ister misin? · alıcılar malın fiyatını artırarak birbirleriyle yarıştı · daha var mı; bağlama göre daha çoğunu isteme ya da doluluğu bildirme
  استزاده أي استقصره (sihah)؛ إذا أعطى رجل رجلا مالا وطلب زيادة على ما أعطاه قيل قد استزاده (tahdhib)؛ تزايد أهل السوق على السلعة إذا بيعت فيمن يزيد (tahdhib)؛ هل من مزيد يجوز أن يكون ذلك استدعاء للزيادة (mufradat)
- **B005** yol azığı edinme ve azık kapları — o anki gereksinimin ötesinde saklanan yol azığı · yol azığı edinme ve yanına alma · birine yol azığı verdi · yol yiyeceğinin konduğu deri torba · su taşımaya yarayan tulum ya da kap · yol için su konan kap · su tulumları ve taşıma kapları
  المزادة مفعلة من الزيادة والجميع المزايد (ayn)؛ المزادة الرواية (sihah)؛ الزادة مفعلة من الزاد يتزود فيها الماء والمزود شبه جراب من أدم يتزود فيه الطعام للسفر (tahdhib)؛ الزاد المدخر الزائد على ما يحتاج إليه في الوقت والتزود أخذ الزاد (mufradat)

## ECHO ز و د (root_000653): for 71:6 يَزِدْهُمْ, 71:21 يَزِدْهُ, 71:24 تَزِدِ, 71:28 تَزِدِ: withheld observed target; not identity

- **B001** geçişte taşınacak birikimi hazırlama, edinme veya verme — yol gereğini hazırlayıp hazır bulundurma · yolculukta veya konaklamada kullanılmak üzere saklanan yiyecek ve gereç · birine yolculukta kullanacağı yiyecek ve gereci verme · yol gereğini edinmek veya bir geçişte taşınacak iş ve kazanç biriktirmek · yanında yol gereği ya da işlerinden doğan birikimi taşıyan kimse
  أصل يدل على انتقال بخير من عمل أو كسب؛ الزاد وهو الطعام يتخذ للسفر (maqayis)؛ الزاد وهو الطعام الذي يتخذ للسفر والحضر؛ كل منتقل بخير أو عمل فهو متزود (ayn)؛ الزاد طعام يتخذ السفر؛ زودت الرجل فتزود (sihah)؛ كل من انتقل معه بخير أو شر من عمل أو كسب فقد تزود (tahdhib)؛ الزاد المدخر الزائد؛ التزود أخذ الزاد (mufradat)
- **B002** yol yiyeceği kabı — yol yiyeceğinin konduğu kap · boyunları yol yiyeceği kaplarına benzetilenler
  المزود الوعاء يجعل للزاد؛ تلقب العجم برقاب المزاود (maqayis)؛ المزود وعاء الزاد (ayn)؛ المزود ما يجعل فيه الزاد؛ العرب تلقب العجم برقاب المزاود (sihah)؛ المزود وعاء يجعل فيه الزاد (tahdhib)؛ المزود ما يجعل فيه الزاد من الطعام (mufradat)
- **B003** binicinin taşıdığı büyük deri su kabı — binicinin taşıdığı büyük deri su kabı · eyer arkasına bağlanan tek büyük su kabı · büyük deri su kapları
  المزادة بمنزلة راوية لا عزلاء لها؛ المزاد بغير ها هي الفردة التي يحتقبها الراكب خلف رحله؛ سميت مزادة لأنها تزيد على السطيحتين (tahdhib)؛ المزادة ما يجعل فيه الزاد من الماء (mufradat)

## ف ر ر (root_001142): 71:6 فِرَارًا

- **B001** kaçıp uzaklaşma — kaçtı, bir yerden ya da topluluktan uzaklaştı · onu kaçırdı veya kaçmasına yol açtı · birbirlerinden kaçtılar · topluluktan kaçan kimse veya kimseler · kaçışın kendisi, kaçılan yer veya kaçış zamanı · üzerinde kaçmaya elverişli at
  فر يفر فرارا هرب (sihah;tahdhib)؛ الفرار يقال فر يفر والمفر المصدر والموضع (maqayis)؛ المفر الموضع الذي تفر إليه (jamhara)؛ المفر موضع الفرار ووقته والفرار نفسه (mufradat)؛ أفره غيره وتفاروا أي تهاربوا (sihah)
- **B002** açıp inceleyerek ortaya çıkarma — yaşını anlamak için hayvanın ağzını açıp dişlerine baktı · gülümseyip dişlerini gösterdi · konuyu araştırdı · onu konuşturup içinde sakladığını öğrendi · iyi atın görünüşü, dişlerini incelemeye gerek bırakmaz
  فر عن أسنانه؛ افتر الإنسان إذا تبسم؛ فر فلانا عما في نفسه؛ فر عن الأمر ابحث (maqayis)؛ فررت الدابة أفرها فرا إذا فتحت فاه لتعرف سنه (jamhara)؛ فررت الفرس إذا نظرت إلى أسنانه؛ فررت عن الأمر بحثت عنه؛ افتر أبدى أسنانه (sihah)؛ كشف عنها لينظر إليها؛ استنطقه ليدل بنطقه على ما في نفسه؛ أكشف سترها عنك (tahdhib)؛ أصل الفر الكشف عن سن الدابة؛ الافترار ظهور السن من الضحك (mufradat)
- **B003** işin yeniden başa dönmesi [kalıp] — iş veya zaman yeniden başlangıçtaki haline döndü
  فر الأمر جذعا إذا رجع وده على بدئه (jamhara)؛ فر الدهر جذعا (mufradat)
- **B004** çeşitli türlerden genç hayvan — kaynağa göre sığır veya başka bir hayvan yavrusu · bağlama göre hayvan yavrusu veya yavrular topluluğu · eski kayıtlarda çeşitli hayvan yavrularına verilen adlar
  الفرير ولد البقرة؛ الفرار من ولد المعز ما صغر جسمه (maqayis)؛ الفرير والفرار ولد البقرة الوحشية وكذلك ولد الحمار والجذع من الظباء (jamhara)؛ الفرير ولد البقرة الوحشية وكذلك الفرار (sihah)؛ الفرير ولد البقرة؛ إذا فطم الجمل وسمن قيل له فرير وفرار وفرارة وفرفر وفرفور وفرافر؛ فرار جمع فرارة وهي الخرفان؛ الفرار البهم الكبار واحدها فرفور (tahdhib)
- **B005** düşüncesizce acele edip taşkın davranma — düşüncesiz hafiflik, taşkınlık ve acele · hafif, düşüncesiz ve taşkın kişi
  الفرفرة الطيش والخفة (maqayis;sihah;tahdhib)؛ رجل فرفار وامرأة فرفارة (maqayis;tahdhib)؛ فرفر الرجل إذا استعجل بالحماقة؛ الفرفرة العجلة (tahdhib)
- **B006** hareket ettirme, yarma ve parçalama — şeyi hareket ettirdi · at gem demirine dişleriyle vurup başını oynattı · baş, tulum veya hayvan bedenini yardı ve parçaladı
  فرفرت الشيء حركته؛ فرفر الفرس إذا ضرب بفأس لجامه أسنانه وحرك رأسه (sihah)؛ أفررت رأسه بالسيف إذا شققته؛ إذا فلقته؛ فرفر إذا شقق الزقاق وغيرها؛ الذئب يفرفر الشاة أي يمزقها (tahdhib)
- **B007** sıcağın başlangıcı veya en şiddetli evresi [kalıp] — sıcağın başlangıcı veya en şiddetli zamanı
  فره الحر أوله ويقال شدته؛ أفرة الحر وأفرة الحر (sihah)؛ أفرة الصيف أوله؛ أتانا فلان في أفرة الحر أي أوله؛ بل في شدته؛ في فرة الحر؛ في أفرة الحر (tahdhib)
- **B008** topluluğun veya malın en seçkin kısmı — topluluğun önde gelenleri veya malın en iyi bölümü
  هو فرة قومه أي خيارهم؛ وهذا فرة مالي أي خيرته؛ هذا فر بني فلان وهو وجههم وخيارهم
- **B009** yakacak olarak kullanılan ateşe dayanıklı ağaç — belirli bir ağaç türü · ateşe dayanıklı ağaç veya ondan elde edilen yakacak
  الفرفارة شجرة (maqayis)؛ فرفر إذا أوقد بالفرفار؛ هي شجرة صبور على النار (tahdhib)
- **B010** kadınlar ve çobanlar için binek düzeneği — kadınlar ve çobanların kullandığı özel binek düzeneği
  فرفر إذا عمل الفرفار؛ وهو مركب من مراكب النساء والرعاء شبه الحوية والسوية
- **B011** küçük bir kuş veya serçe — küçük bir kuş veya küçük serçe
  الفرفور طائر (sihah)؛ الفرفور العصفور الصغير (tahdhib)
- **B012** yerdeki ince su yolu — 
  زعم قوم من أهل اللغة أن الفر نهر دقيق في الأرض
- **B013** kadınlar için eski bir niteleme — 
  الفرور من النساء النوار
- **B014** belirli bir Arap soy topluluğu kolu — belirli bir Arap boy kolunun adı
  بنو فرير بطن من طيئ (jamhara)؛ فرير بطن من العرب (sihah)
- **B015** gevşeklikten sonra aklını başına toplama — gevşeklikten sonra aklını başına topladı
  فر يفر إذا عقل بعد استرخاء
- **B016** insanların birbirine karışmış hali [kalıp] — insanlar birbirine karışmış durumdaydı
  الناس في أفرة يعني الاختلاط

## ك ل ل (root_001315): 71:7 كُلَّمَا

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

## ج ع ل (root_000248): 71:7 جَعَلُوٓا۟, 71:12 وَيَجْعَل, 71:12 وَيَجْعَل, 71:16 وَجَعَلَ, 71:16 وَجَعَلَ, 71:19 جَعَلَ

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

## ص ب ع (root_000841): 71:7 أَصَٰبِعَهُمْ

- **B001** el parmağı — el parmağı
  الأصل إصبع الإنسان واحده أصابعه (maqayis)؛ والإصبع يؤنث وبعض يذكرها (ayn)؛ والإصبع معروفة (jamhara)؛ الإصبع يذكر ويؤنث وفيه لغات (sihah)؛ والإصبع واحدة الأصابع (tahdhib)
- **B002** parmakla göstererek çekiştirme ya da birini işaretle bildirme [kalıp] — birini parmakla gösterip arkasından çekiştirmek · birini başka birine işaretle göstermek
  صبع فلان بفلان إذا أشار نحوه بإصبعه مغتابا له (maqayis)؛ صبعت بفلان وعلى فلان أصبع صبعا إذا أشرت نحوه بإصبعك مغتابا (sihah)؛ صبعت فلانا على فلان دللته عليه بالإشارة (sihah;tahdhib)
- **B003** olumlu ve güzel etki — malda veya bakım işinde bırakılan olumlu etki · mal üzerindeki etkinin iyi olması
  والإصبع الأثر الحسن (maqayis;tahdhib)؛ لفلان في ماله إصبع أي أثر جميل (maqayis)؛ لفلان على ماله إصبع حسنة أي أثر جميل (jamhara)؛ للراعي على ماشيته إصبع أي أثر حسن (sihah)؛ حسن الإصبع في ماله أي حسن الأثر (tahdhib)
- **B004** parmak aralığından boşaltma veya dar ağızdan içeri yerleştirme — kabın içindekini parmakların arasından kontrollü biçimde akıtmak · bir şeyi dar ağızlı bir nesnenin içine yerleştirmek
  الصبع إراقتك ما في الإناء من بين إصبعيك (maqayis)؛ الصبع أن تأخذ إناء فتقابل بين إبهاميك وسبابتيك ثم تسيل ما فيه (ayn)؛ تجعل شيئا في شيء ضيق الرأس فهو يصبعه صبعا (ayn)؛ صبعت الإناء إذا فعلت به ذلك (jamhara)؛ صبعت الإناء إذا كان فيه شراب فوضعت عليه إصبعك حتى سال عليه ما فيه في إناء آخر (sihah)؛ صبع الإناء أن يرسل الشراب الذي فيه من طرفي الإبهامين أو السبابتين (tahdhib)
- **B005** güveni bozan, sözünde durmayan kimse [kalıp] — güveni bozan, sözünde durmayan kimse
  للغدر خائنة مغل الإصبع (jamhara;tahdhib)؛ فلان مغل الإصبع إذا كان خائنا (tahdhib)
- **B006** aşırı büyüklenme — kendini başkalarından üstün gören · aşırı ve tam büyüklenme
  رجل مصبوع إذا كان متكبرا؛ والصبع الكبر التام (tahdhib)

## ء ذ ن (root_000022): 71:7 ءَاذَانِهِمْ

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

## غ ش و (root_001088): 71:7 وَٱسْتَغْشَوْا۟

- **B001** örtme ve perdeleme — bir şeyin üstünü örtmek · örtü · gözü veya gönlü örten perde · göz perdesi · örtmek veya görüşü engellemek · giysisiyle örtünmek · giysisiyle örtünmek · eyer örtüsü
  أصل صحيح يدل على تغطية شيء بشيء (maqayis)؛ الغشاوة ما غشي القلب من رين الطبع (ayn)؛ الغشاء الغطاء وغشاوة أي غطاء وتغطيته واستغشى بثوبه (sihah)؛ الغشاوة ما غشي القلب من الطبع والغشاء الغطاء وغاشية السرج غطاؤه والرجل يستغشي ثوبه (tahdhib)؛ الغشاوة ما يغطى به الشيء واستغشوا ثيابهم (mufradat)
- **B002** her yanı saran büyük olay — dünyanın sonu ve hesap günü · herkesi kuşatan ağır karşılık veya bela · karnında ağır bir hastalığa tutuldu
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها ورماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ الغاشية القيامة لأنها تغشى بإفزاعها ورماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم وغاشية اسم من أسماء القيامة وداء يأخذه في جوفه (tahdhib)؛ الغاشية كل ما يغطي الشيء ونائبة تغشاهم وتجللهم وكناية عن القيامة (mufradat)
- **B003** gelip uğrama — yanına gelmek · bir yere gelmek · bir kimsenin ziyaretçileri ve gelip gidenleri
  غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك وغاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B004** kadınla cinsel ilişkiyi dolaylı anlatma — kadınla birlikte olmak; cinsel ilişkiyi dolaylı anlatır · eşiyle birlikte olmak; cinsel ilişkiyi dolaylı anlatır
  الغشيان غشيان الرجل المرأة (maqayis)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة وتغشى امرأته (tahdhib)؛ غشيت موضع كذا أتيته وكني بذلك عن الجماع وغشاها وتغشاها (mufradat)
- **B005** bilincini yitirip bayılma — bilincini yitirip bayılmak · baygınlık; ölüm baygınlığı · baygın, bilinci kapalı
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B006** kamçı veya kılıçla vurma — bir kimseye kamçıyla vurmak · üzerine kamçı veya kılıç darbesi indirmek
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** hayvanın başını veya yüzünü kaplayan aklık — başı bütünüyle ak at · yüzü bütünüyle ak keçi · keçinin yüzünü kaplayan aklık
  الأعشى من الخيل وغيرها ما ابيض رأسه كله وعنزة غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

## ECHO غ ش ي (root_001089): for 71:7 وَٱسْتَغْشَوْا۟: withheld observed target; not identity

- **B001** örtüp kapatma ve örten şey — bir şeyin üstünü örtüp kapatmak · örtü; kaplayıcı tabaka · bir şeyi, gözü veya gönlü örten perde · görüşü kapatan perde · kılıcın ve yük semerinin örtüsü · eyer örtüsü · görmemek ve işitmemek için giysisine bürünmek · giysisine bürünmek · bir şeyi başka bir şeyin üstünü örter duruma getirmek · bir şeyi örten şey · üstten kaplayan örtüler
  يدل على تغطية شيء بشيء (maqayis)؛ الغشاء الغطاء (maqayis;sihah;tahdhib)؛ غاشية السيف والرحل غطاؤه (ayn)؛ غاشية السرج غطاؤه (tahdhib)؛ جعل على بصره غشوة وغشاوة أي غطاء (sihah)؛ يستغشي ثوبه كي لا يسمع ولا يرى (ayn;tahdhib)؛ الغشاوة ما يغطى به الشيء (mufradat)
- **B002** herkesi kuşatan son gün veya ağır yıkım — dünyanın son bulup herkesin yeniden diriltileceği gün · Tanrı'dan gelen, herkesi kuşatan ağır ceza
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها (maqayis;sihah)؛ الغاشية القيامة (ayn)؛ الغاشية اسم من أسماء القيامة في القرآن (tahdhib)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم (tahdhib)؛ نائبة تغشاهم وتجللهم (mufradat)
- **B003** içini tutan hastalığa uğrama [kalıp] — kişinin içini tutan bir hastalığa uğraması
  رماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ رماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ رماه الله بغاشية وهو داء يأخذه في جوفه (tahdhib)
- **B004** kadınla cinsel birleşmeyi örtmeceli anlatma — erkeğin kadınla cinsel birleşmesi · kadınla cinsel birleşmeye girmek · karısıyla cinsel birleşmeye girmek
  الغشيان غشيان الرجل المرأة (maqayis)؛ الغشيان إتيان الرجل المرأة (ayn)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة (tahdhib)؛ كني بذلك عن الجماع يقال غشاها وتغشاها (mufradat)
- **B005** birine veya bir yere gelme ve gelip gidenler — yanına gelmek · bir yere gelmek · iyilik umarak gelenler ve ziyaretçiler · bir kişinin ziyaretçileri ve dostları
  الغاشية الذين يغشونك يرجون فضلك (ayn)؛ غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك يرجون فضلك ومعروفك (tahdhib)؛ غاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B006** kırbaç veya kılıçla vurma [kalıp] — adama kırbaçla vurmak
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** kavrayışı kapanıp bayılma — bilinci kapanıp bayılmak · baygınlık · baygın; bilinci kapalı · ölümü andıran baygınlık
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B008** hayvanın yüzünü veya başını kaplayan beyazlık — yüzü bütünüyle beyaz keçi · başı bütünüyle beyaz, gövdesi başka renkte hayvan
  الأعشى من الخيل وغيرها ما ابيض رأسه كله من بين جسده (sihah)؛ عنز غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

## ث و ب (root_000209): 71:7 ثِيَابَهُمْ

- **B001** önceki yere ya da duruma geri dönme — gittikten sonra geri dönmek; önceki yerine veya durumuna gelmek · insanların bir araya gelip toplanması · çekilen suyun geri gelmesi veya kabın yeniden dolması · insanların tekrar tekrar döndüğü yer · kuyu ağzında su çekenin durduğu yer veya suyun geri ulaştığı düzey · havuzda suyun geri dönüp toplandığı bölüm · birbirlerine doğru gelerek toplanan insan topluluğu · arıların geri döndüğü şey olarak bal
  الثاء والواو والباء قياس صحيح من أصل واحد وهو العود والرجوع (maqayis)؛ ثاب يثوب إذا رجع (maqayis)؛ وثاب يثوب ثوبا وثؤوبا إذا رجع وكل راجع ثائب (jamhara)؛ ثاب الرجل يثوب ثوبا وثوبانا رجع بعد ذهابه وثاب الناس اجتمعوا وجاءوا (sihah)؛ أصل الثوب رجوع الشيء إلى حالته الأولى (mufradat)؛ المثابة المكان يثوب إليه الناس (maqayis;sihah;mufradat)؛ ثاب الماء إذا بلغ إلى حاله الأولى بعد ما يستقى (jamhara)؛ ثبة الحوض ما يثوب إليه الماء (mufradat)
- **B002** yapılan işin sahibine dönen karşılık — yapılan işin karşılığı; çoğunlukla ödül · bir iş karşılığında verilen karşılık veya ödül · birine yaptığının karşılığını vermek · inanmayanlara yaptıklarının kötü karşılığını vermek
  الثواب من الأجر والجزاء أمر يثاب إليه (maqayis)؛ أعطيت فلانا ثوابه أي جزاء ما عمل (jamhara)؛ أثاب الله العباد يثيبهم إثابة وثوابا إذا جازاهم بأعمالهم (jamhara)؛ الثواب جزاء الطاعة وكذلك المثوبة (sihah)؛ هل ثوب الكفار ما كانوا يفعلون أي جوزوا (sihah)؛ الثواب ما يرجع إلى الإنسان من جزاء أعماله (mufradat)؛ الثواب يقال في الخير والشر لكن الأكثر المتعارف في الخير (mufradat)
- **B003** giysi — giysi · giysiler · giysi sözüyle kişinin kendisini dolaylı olarak anlatma
  الثوب الملبوس محتمل أن يكون من هذا القياس لأنه يلبس ثم يلبس ويثاب إليه (maqayis)؛ ربما عبروا عن النفس بالثوب (maqayis)؛ الثوب واحد الأثواب والثياب (sihah)؛ الثوب سمي بذلك لرجوع الغزل إلى الحالة التي قدرت له (mufradat)؛ وثيابك فطهر يحمل على تطهير الثوب وقيل الثياب كناية عن النفس (mufradat)
- **B004** çağrıyı yineleme — çağrıyı yineleme veya yeniden ibadete çağırma · sabah ibadet çağrısına, uykudan daha iyi olduğunu bildiren özel sözü ekleme · insanı tekrar tekrar etkileyen rahatsızlık
  التثويب الدعاء للصلاة وغيرها وأصله أن الرجل كان إذا جاء فزعا أو مستصرخا لوح بثوبه (jamhara)؛ صار يسمى الدعاء تثويبا (jamhara)؛ التثويب في أذان الفجر أن يقول الصلاة خير من النوم (sihah)؛ التثويب تكرار النداء ومنه التثويب في الأذان (mufradat)؛ الثوباء التي تعتري الإنسان سميت بذلك لتكررها (mufradat)
- **B005** evlilikte cinsel birliktelik yaşamış kişi — evlilikte cinsel birliktelik yaşamış erkek veya kadın; ayrıca eşinin yanından ayrılıp dönmüş kadın · kadınla evlilikte cinsel birliktelik kurup onu bu duruma getirmek
  رجل ثيب وامرأة ثيب الذكر والأنثى فيه سواء وذلك إذا كانت المرأة قد دخل بها أو كان الرجل قد دخل بامرأته (sihah)؛ الثيب التي تثوب عن الزوج (mufradat)

## ص ر ر (root_000856): 71:7 وَأَصَرُّوا۟

- **B001** bağlayıp sıkma — bağlamak, sıkıca tutturmak · bağlı para kesesi · yavrunun emmesini önlemek için hayvanın memesine bağlanan bez veya ip · birbirine sokulmuş topluluk
  صر الدراهم يصرها صرا وتلك الخرقة صرة (maqayis); الصرار خرقة تشد على أطباء الناقة (maqayis;ayn;mufradat); صررت الصرة شددتها (sihah); الصرة ما تعقد فيه الدراهم (mufradat); الصرة الجماعة المنضم بعضهم إلى بعض (maqayis;sihah;mufradat)
- **B002** kararından dönmeden sürdürme — bir şeyde kararlı olup vazgeçmeme · kesin kararım ve ciddi sözüm
  الإصرار العزم على الشيء (maqayis;ayn); أصررت على الشيء إذا أقمت ودمت عليه (sihah;tahdhib); الإصرار التعقد في الذنب والتشدد فيه والامتناع من الإقلاع عنه (mufradat); هذا مني صري وأصري أي جد وعزيمة (sihah;tahdhib;mufradat)
- **B003** zarar veren keskin soğuk; ayrıca şiddetli sıcaklık — bitkiye zarar veren keskin soğuk · çok soğuk ve sert rüzgâr · güneşin veya yazın şiddetli sıcağı
  الصر البرد الذي يضرب كل شيء (ayn;sihah;tahdhib); ريح صرصر باردة (sihah;tahdhib); صرة القيظ شدة حره (sihah); الصارة شدة الحر حر الشمس (maqayis); ريحا صرصرا لفظه من الصر (mufradat)
- **B004** gür veya uzayan ses çıkarma — uğultulu veya gürültülü rüzgâr · şiddetli bağırış veya gürültü · gıcırtı veya uzayan ses · sesi yinelemek veya dalgalandırmak · vurulduğunda çınlayan para
  الصرة شدة الصياح (maqayis;ayn;sihah;tahdhib); صر الجندب صريرا وصرصر الأخطب صرصرة (maqayis;ayn;sihah;tahdhib); صر الباب يصر صريرا (ayn;sihah;tahdhib); وقيل الصرة الصيحة (mufradat)
- **B005** kulağını dikme veya başına doğru toplama [kalıp] — kulağını dikmek veya başına doğru toplamak · kulağını dikmek
  صر الحمار أذنه إذا أقامها (maqayis); صر الحمار أذنيه أي سواهما وأصر الحمار (ayn); صر الفرس أذنيه ضمهما إلى رأسه (sihah); جاءت الخيل مصرة آذانها محددة رافعة لها (tahdhib)
- **B006** toynağın daralıp büzülmesi — dar ve büzülmüş, özellikle toynak için · toynak ileri derecede daraldı
  حافر مصرور أي منقبض (maqayis); حافر مصرور أي ضيق مقبوض (sihah); الحافر المصرور المنقبض (tahdhib); اصطر الحافر إذا كان فاحش الضيق (tahdhib)
- **B007** kutsal ziyaret görevini yapmamış veya evlilikten uzak duran kimse — kutsal ziyaret görevini yapmamış veya evlilikten uzak duran kimse
  الصرورة الذي لم يحجج والذي لم يتزوج (maqayis); الصرورة من الرجال والنساء الذي لم يحج ولا يريد التزوج (ayn;mufradat); رجل صرورة للذي لم يحج (sihah); الصرورة هو التبتل وترك النكاح (tahdhib)
- **B008** susuzluk — susuzluk; belirli bir söyleyişte susuzluğun giderilmesi · susuzluk · susamak
  الصارة العطش وجمعها صوار (maqayis;sihah); الصريرة العطش والجمع صرائر (maqayis); قصع الحمار صارته إذا شرب الماء فذهب عطشه (sihah); صر يصر إذا عطش (tahdhib)
- **B009** bir kimseden beklenen gereksinim veya talep — bir kimse nezdindeki gereksinim, istek veya talep
  الصارة هي الحاجة (maqayis); لي قبل فلان صارة (maqayis;sihah); لنا قبله صارة وجمعها صوار (tahdhib)

## ك ب ر (root_001281): 71:7 وَٱسْتَكْبَرُوا۟, 71:7 ٱسْتِكْبَارًا, 71:22 كُبَّارًا

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

## ج ه ر (root_000269): 71:8 جِهَارًا

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

## ع ل ن (root_001041): 71:9 أَعْلَنتُ

- **B001** açığa çıkıp yayılma; açığa vurup belli etme — açığa çıkmak; duyulup yayılmak · açığa vurmak; açıkça belli etmek · işin duyulup yaygınlaşması · gizli olmayan açık durum; açıklık · karşılıklı açık konuşma; iki tarafın içindekini birbirine söylemesi · içindekileri karşılıklı olarak açıkça söyleme · sırrını açıkça söyleyen kişi · bir şeyi açığa vurmak
  يدل على إظهار الشيء والإشارة إليه وظهوره، علن الأمر يعلن، وأعلنته أنا، والعلان المعالنة (maqayis)؛ علن الأمر يعلن علونا وعلانية أي شاع وظهر، وأعلنته إعلانا (ayn)؛ العلانية خلاف السر، علن الأمر يعلن علونا، وأعلنته أنا إذا أظهرته، والعلان المعالنة، ورجل علنة يبوح بسره (sihah)؛ علن الأمر يعلن علنا، وعلن يعلن إذا شاع وظهر، أعلن الأمر إذا اشتهر، استعلن أي أظهره، العلان المعالنة إذا أعلن كل واحد لصاحبه ما في نفسه، العلانية ظهور الأمر (tahdhib)؛ العلانية ضد السر، وأكثر ما يقال ذلك في المعاني دون الأعيان، علن كذا، وأعلنته أنا (mufradat)
- **B002** kitap başlığı ve başlık koyma — kitabın başlığı · kitaba başlık koymak
  علوان الكتاب عنوانه، وقد علونت الكتاب إذا عنونته (sihah)

## س ر ر (root_000697): 71:9 وَأَسْرَرْتُ, 71:9 إِسْرَارًا

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

## د ر ر (root_000469): 71:11 مِّدْرَارًا

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

## د و ر (root_000499): 71:26 دَيَّارًا (also echo for 71:11 مِّدْرَارًا)

- **B001** dönme ve çevreleme — dönmek veya çevresini dolanmak · dönme hareketi · bir tam dönüş · bir şeyi döndürmek · bir şeyi yuvarlaklaştırmak · dönme odağı veya dönülen yer · halka, çember veya yuvarlak çizgi · kuyu kovası biçiminde dikilmiş deri kap
  أصل واحد يدل على إحداق الشيء بالشيء من حواليه؛ دار يدور دورانا (maqayis)؛ دار دورة واحدة؛ المدار موضع للشيء الذي تدير به؛ الدائرة الحلقة والشيء المستدير (ayn)؛ دار الشيء يدور دورا ودورانا؛ تدوير الشيء جعله مدورا؛ الدائرة واحدة الدوائر (sihah)؛ الدار اعتبارا بدورانها؛ الدائرة عبارة عن الخط المحيط؛ دار يدور دورانا (mufradat)
- **B002** yerleşilen yer ve yurt — ev, konut veya insanların yerleştiği yer · kabile veya yerleşik topluluk · evler, konutlar veya yurtlar · çevresi yükseltilerle ya da sınırla kuşatılmış yer · ayın çevresindeki ışık halkası · bu yaşamın yurdu · öte yaşamın yurdu · esenlik yurdu · yıkım yurdu · yoldan çıkanların varacağı yurt
  الدار القبيلة؛ الدارة أرض سهلة تدور بها جبال؛ أصل الدار دارة (maqayis)؛ الدار كل موضع حل به قوم؛ الدار اسم جامع للعرصة والبناء والمحلة؛ الدارة دارة القمر وكل موضع يدار به شيء يحجزه (ayn)؛ الدار مؤنثة؛ الكثير ديار ودور؛ الدارة أخص من الدار؛ الدارة التي حول القمر وهي الهالة (sihah)؛ الدار المنزل اعتبارا بدورانها الذي لها بالحائط؛ تسمى البلدة دارا والصقع دارا والدنيا دارا والدار الآخرة (mufradat)
- **B003** durumların dönüp değişmesi — insanın durumlarını değiştirip duran zaman · işleri evirip çevirerek ele alma
  الدواري الدهر لأنه يدور بالناس أحوالا (maqayis)؛ الدواري الدهر الدوار بالناس؛ الدائرة الدولة؛ مداورة الشؤون معالجتها (ayn)؛ المداورة كالمعالجة؛ الدواري الدهر يدور بالإنسان أحوالا (sihah)؛ الدواري الدهر الدائر بالإنسان من حيث إنه يدور بالإنسان (mufradat)
- **B004** kuşatan kötü durum veya yenilgi — kuşatıcı kötü durum veya yenilgi · dönüp sahibini bulacak kötülük
  دارت بهم الدوائر أي الحالات المكروهة أحدقت بهم (maqayis)؛ الدائرة الهزيمة؛ عليهم دائرة السوء (sihah)؛ الدورة والدائرة في المكروه (mufradat)
- **B005** baş dönmesi ve baygınlık — baş dönmesi · başı döndü veya bayıldı
  الدوار في الرأس هو من الباب؛ يقال دير به وأدير به (maqayis)؛ الدوار أن يأخذ الإنسان في رأسه كهيئة الدوران تقول دير به أي غشي عليه (ayn)؛ الدوار أيضا من دوار الرأس؛ يقال دير بالرجل وأدير به (sihah)
- **B006** çevresinde dönülen tapınma nesnesi veya yeri — çevresinde dönülen taş, dikili tapınma nesnesi veya yer
  الدوار مثقل ومخفف حجر كان يؤخذ من الحرم إلى ناحية ويطاف به (maqayis)؛ الدوار صنم كانت العرب تنصبه يجعلون موضعا حوله يدورون فيه واسم ذلك الصنم والموضع الدوار (ayn)؛ دوار بالضم صنم وقد يفتح (sihah)
- **B007** yere bağlı kişi — yer bağlantısıyla adlandırılan koku ve baharat satıcısı · evinde oturan yerleşik kişi veya sürü sahibi
  الداري العطار؛ وإنما سمي داريا من الدار أي هو يسكن الدار؛ الداري الرجل المقيم في داره (maqayis)؛ الداري العطار وهو منسوب إلى دارين؛ والداري أيضا رب النعم سمي بذلك لأنه مقيم في داره (sihah)
- **B008** manastır ve ona bağlı kullanımlar — Hristiyan manastırı veya kilisesi · manastır sahibi, görevlisi veya sakini · orada hiç kimse yok · topluluğun başındaki kişi
  الدال والياء والراء أظنه منقلبا عن الواو من الدار والدور؛ ومن الباب الدير؛ وما بها ديور وديار أي أحد؛ رأس الدير (maqayis_dyr)؛ الدير البيعة وساكنه وعامله ديراني وديار؛ الديور الواحد الفرد من الناس (ayn)؛ دير النصارى أصله الواو والجمع أديار؛ الديراني صاحب الدير؛ هو رأس الدير (sihah)

## م د د (root_001407): 71:12 وَيُمْدِدْكُم

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

## م و ل (root_001457): 71:12 بِأَمْوَٰلٍ, 71:21 مَالُهُۥ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ب ن ي (root_000156): 71:12 وَبَنِينَ

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

## ب ن و (root_001959): documented alternative for 71:12 وَبَنِينَ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## ج ن ن (root_000266): 71:12 جَنَّٰتٍ

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

## ر ج و (root_000548): 71:13 تَرْجُونَ

- **B001** sevindirici bir sonucu umutla bekleme — umut; sevindirici bir sonucun gerçekleşmesini bekleme · bir şeyi veya bir kimseden gelecek iyiliği ummak · umut ederek beklemek · bir şeyin gerçekleşmesini umup beklemek · iyilik umarak gelme veya iyilik beklentisi · bir kimseden umulan şey veya iyilik · ummak anlamındaki seyrek kullanım
  الرجاء وهو الأمل (maqayis)؛ الرجاء ممدود نقيض اليأس (ayn;tahdhib)؛ الرجاء من الأمل ممدود (sihah)؛ الرجاء ظن يقتضي حصول ما فيه مسرة (mufradat)
- **B002** olumsuz yapıda korkma veya önemseme okuması — korkmamak, çekinmemek veya saygı göstermemek · aldırmamak veya önemsememek · sokmasından korkmamak veya onu umursamamak
  ربما عبر عن الخوف بالرجاء (maqayis)؛ ما أرجو أي ما أبالي (maqayis;ayn;tahdhib)؛ لا تخافون ولا تبالون (ayn)؛ وقد يكون الرجو والرجاء بمعنى الخوف (sihah)؛ لا تخافون لله عظمة (tahdhib)؛ قيل ما لكم لا تخافون (mufradat)
- **B003** bir şeyin yanı veya kenarı — bir şeyin yanı, tarafı veya kenarı · bir şeyin iki yanı veya kuyunun iki kenarı · yanlar, taraflar veya kenarlar · tehlikeye atılmak veya tutunamaz duruma düşmek
  الرجا مقصور الناحية من البئر وكل ناحية رجا (maqayis)؛ الرجا مقصور ناحية كل شيء (ayn;tahdhib)؛ ناحية البئر وحافتاها وكل ناحية رجا (sihah)؛ رجا البئر والسماء وغيرهما جانبها والجمع أرجاء (mufradat)
- **B004** bir işi sonraya bırakma — bir şeyi ertelemek veya sonraya bırakmak · bir şeyi ertelemek; aynı fiilin ses değişkesi · Tanrı'nın buyruğuna ve ilerideki hükmüne bırakılmış olanlar · inanç bildirimini öne alıp eylemi sonraya bırakan topluluk · eylemi sonraya bırakma görüşüne bağlı kişi
  أرجأت الشيء أخرته (maqayis)؛ أرجأت الأمر أخرته (sihah:رجأ)؛ أرجيت الأمر أخرته يهمز ولا يهمز (sihah:رجا)؛ أرجأت الأمر وأرجيته إذا أخرته (tahdhib)؛ آخرون مرجون لأمر الله (mufradat)
- **B005** doğumu yaklaşmış olma — dişi devenin doğumunun yaklaşması · dişi devenin doğumunun yaklaşması; aynı fiilin ses değişkesi · gebenin doğumunun ve yavrunun çıkışının yaklaşması
  للفرس إذا دنا نتاجها قد أرجت ترجي إرجاء (maqayis)؛ أرجأت الناقة دنا نتاجها (sihah:رجأ)؛ أرجت الناقة دنا نتاجها (sihah:رجا)؛ أرجأت الحامل إذا دنا أن يخرج ولدها (tahdhib)؛ أرجت الناقة دنا نتاجها وحقيقته جعلت لصاحبها رجاء (mufradat)

## ECHO م ر ج (root_001411): for 71:13 تَرْجُونَ: withheld observed target; not identity

- **B001** bitkili otlak ve hayvanı serbest otlatma — geniş ve bitkili otlak · geniş ve bitkili otlaklar · hayvanı otlamaya saldı · hayvanı otlattı veya otlamaya saldı · çobansız otlayan deve sürüsü · çoban denetimi olmadan salınmış hayvan · atların bırakıldığı veya erkekleriyle dişilerinin birlikte tutulduğu yer · Horasan'daki bir yer adı · Şam bölgesindeki bir yer adı · belirli bir yere nispet edilen tarihî savaş günü · bozkırdaki bir konak yerinin adı
  المرج أرض واسعة فيها نبت كثير تمرج فيها الدواب (ayn;tahdhib)؛ مرج الخيل الذي تمرج فيه أي تترك الذكور مع الإناث (jamhara)؛ المرج الموضع الذي ترعى فيه الدواب؛ مرجت الدابة إذا أرسلتها ترعى (sihah)؛ إبل مرج إذا كانت لا راعي لها وهي ترعى (tahdhib)؛ أرض ذات نبات تمرج فيها الدواب (maqayis)
- **B002** iki su kütlesini salıp buluşturma [kalıp] — iki su kütlesini salıp buluşturdu · iki su kütlesini salıp buluşturdu
  مرج البحرين يلتقيان أي لاقى بين البحر العذب والملح؛ لا يختلط أحدهما بالآخر (ayn)؛ خلاهما لا يلتبس أحدهما بالآخر (sihah)؛ أرسلهما ثم يلتقيان؛ خلاهما ثم جعلهما لا يلتبس ذا بذا؛ مرج خلط؛ المرج الإجراء (tahdhib)؛ أرسلهما فمرجا (maqayis)
- **B003** parlak ve güçlü ateş alevi [kalıp] — parlak ve güçlü ateş alevi
  المارج من النار الشعلة الساطعة ذات لهب شديد (ayn;tahdhib)؛ مارج من نار أي متفرق الشعاع (jamhara)؛ مارج من نار نار لا دخان لها (sihah)؛ المارج اللهب المختلط بسواد النار؛ من خلط من نار (tahdhib)
- **B004** işlerin karışıp bozulması — karışıklık, bozulma veya içinden çıkılmaz kargaşa · iş karıştı ve belirsizleşti · karmakarışık ve belirsiz iş · karışık iş · inanç düzeni sarsıldı ve çıkış yolu belirsizleşti · sözleşmeler ve emanetler bozulup güvenilmez hale geldi · sözleşmeleri karıştırdılar ve sözlerini tutmadılar · karıştırma ve birbirine katma
  أمر مريج أي ملتبس؛ مرجت عهودهم وأمرجوها أي لم يفوا بها وخلطوها (ayn)؛ مرج أمر الناس إذا اختلط (jamhara)؛ مرجت أمانات الناس فسدت؛ مرج الدين والأمر اختلط واضطرب (sihah)؛ مرج الدين أي اضطرب والتبس المخرج فيه؛ المرج الفتنة المشكلة والمرج الفساد (tahdhib)؛ أصل المرج الخلط والمرج الاختلاط (mufradat)؛ أمانات القوم وعهودهم اضطربت واختلطت (maqayis)؛ الهمرجة الاختلاط وهو من همج وهرج ومرج (maqayis)
- **B005** yerinde gevşekçe oynamak — yerinde gevşeklik ve oynama · yüzük parmakta bol gelip oynadı
  مرج الخاتم في الإصبع إذا تقلقل فيها (jamhara)؛ مرج الخاتم في إصبعي أي قلق (sihah)؛ أصل المرج القلق؛ مرج الخاتم في يدي إذا قلق (tahdhib)؛ مرج الخاتم في أصبعي (mufradat)؛ مرج الخاتم في الإصبع قلق (maqayis)
- **B006** dalların dolaşması veya okun eğrilmesi [kalıp] — küçük dalları birbirine dolaşmış dal · dalların arasına karışıp dolaşmış ince sürgün · burulmuş ve eğri ok
  غصن مريج قد التبست شناغيبه (ayn)؛ خوط مريج أي مشتبك في الأغصان؛ سهم مريج ملتو أعوج (jamhara)؛ غصن مريج قد التبست شناغيبه؛ غصن له شعب قصار قد التبست (tahdhib)؛ غصن مريج مختلط (mufradat)
- **B007** küçük inci veya kırmızı süs taşı — 
  المرجان صغار اللؤلؤ (sihah;mufradat)؛ المرجان صغار اللؤلؤ؛ هو البستذ وهو جوهر أحمر؛ المرجان الخرز الأحمر؛ لا أدري أرباعي هو أم ثلاثي (tahdhib)
- **B008** dişi devenin gelişmiş yavruyu düşürmesi — dişi deve gelişmiş yavrusunu düşürdü · yavru düşürmesi alışkanlık olmuş dişi deve
  أمرجت الناقة ألقت ولدها بعد ما يصير غرسا ودما (sihah)؛ أمرجت الناقة إذا ألقت ولدها بعدما يصير غرسا؛ وناقة ممراج إذا كان ذلك من عادتها (tahdhib)

## و ق ر (root_001674): 71:13 وَقَارًا

- **B001** işitme ağırlığı — kulakta işitme ağırlığı · kulağı ağırlaştı, işitmesi güçleşti · işitmesi ağırlaşmış kulak
  الوَقْر ثقل في الأذن (maqayis;ayn;sihah;tahdhib;mufradat)؛ وقرت أذنه فهي موقورة (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** ağır yük — sırtta, başta veya hayvanda taşınan ağır yük · ona ağır yük taşıttı · çok ürünle yüklü ağaç · ağır yük taşıyan kadın · borç onu ağır yük altında bıraktı · yiyecekten taşıyabileceği kadarını aldı · borç yükü altında ezilmiş yoksul; ayrıca uyaklı pekiştirme sözü
  الوِقْر الحمل (maqayis;ayn;sihah;tahdhib;mufradat)؛ نخلة موقرة وموقر (maqayis;ayn;sihah;tahdhib;mufradat)؛ امرأة موقرة إذا حملت حملا ثقيلا (sihah;tahdhib)؛ أوقره الدين (ayn;sihah;tahdhib)
- **B003** sakin ve ölçülü ağırbaşlılık — sakinlik, ölçülülük ve ağırbaşlılık · sakin ve ağırbaşlı kimse · ölçülü ve ağırbaşlı kimse · birini yüceltti ve ona saygı gösterdi · saygı gösterme ve yüceltme · ağırbaşlılık veya saygı gösterme için kullanılan değişken biçim · ağırbaşlılık sahibi
  الوقار الحلم والرزانة (maqayis;ayn;sihah;tahdhib)؛ السكينة والوداعة (ayn;tahdhib)؛ التوقير التبجيل (ayn)؛ وقرت الرجل إذا عظمته (tahdhib)؛ لا ترجون لله وقارا أي عظمة (sihah;tahdhib)؛ التيقور لغة في التوقير (ayn;sihah;tahdhib)
- **B004** hareketsiz kalma veya oturma — 
  ليس من الوقار إنما هو من الجلوس يقال منه وقرت (maqayis)؛ وقر يقر وقارا إذا سكن والأمر منه قر (tahdhib)؛ وقرت أقر وقرا أي جلست (mufradat)
- **B005** sert yüzeyde çentik veya oyuk — gözde, toynakta, taşta veya kemikte çentik ve oyuk · kemiği çatlattı veya ezdi · kayada su tutabilen oyuk · hayvanın toynağı taşa çarpıp incindi
  الوقيرة نقر في الصخر (maqayis)؛ الوقرة في العظم (maqayis)؛ وقرت العظم صدعته (sihah)؛ الوقرة شبه وكتة لها حفرة في العين والحافر والحجر (ayn;tahdhib)؛ الوقر في العظم شيء من الكسر وهو الهزم (tahdhib)
- **B006** koyun sürüsü — koyun veya küçükbaş sürüsü · insanlardan veya başka varlıklardan oluşan topluluk · koyun topluluğunun adı
  الوقير القطيع من الضأن (maqayis;ayn;mufradat)؛ الوقير الغنم (sihah;tahdhib)؛ الوقير صغار الشاء (ayn)؛ الوقير الجماعة من الناس وغيرهم (tahdhib)
- **B007** deneyimle pişip dayanıklı olma [kalıp] — olayların veya yolculukların pişirdiği deneyimli kişi · yolculuklar beni sertleştirdi ve koşullarına alıştırdı
  رجل موقر مجرب (maqayis;sihah)؛ رجل موقر إذا وقحته الأمور واستمر عليها (tahdhib)؛ وقرتني الأسفار أي صلبتني ومرنتني عليها (tahdhib)

## خ ل ق (root_000434): 71:14 خَلَقَكُمْ, 71:15 خَلَقَ

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

## ط و ر (root_000955): 71:14 أَطْوَارًا

- **B001** yanı boyunca aynı hizada uzanan bölüm — ev ya da yapıyla aynı hizada uzanan avlu veya yapı bölümü
  طوار الدار وهو الذي يمتد معها من فنائها (maqayis)؛ الطوار ما كان على حذو الشيء أو بحذائه (ayn)؛ طوار الدار ما كان ممتدا معها من الفناء (sihah)؛ طوار الدار وطواره ما امتد منها من البناء (mufradat)
- **B002** çevresinde dolanıp yaklaşmak — ona ya da avlusuna yaklaşmam · çevremize veya korunaklı alanımıza yaklaşma · çevresinde dolanıp ona yaklaşmak
  طار فلان يطور طورا أي كأنه يحوم حواليه ويدنو منه (ayn)؛ لا أطور به أي لا أقربه (sihah)؛ لا تطر حرانا أي لا تقرب ما حولنا (sihah)؛ لا أطور به أي لا أقرب فناءه (mufradat)
- **B003** kişiye veya şeye ait sınır — kendine düşen sınırı ya da ölçüyü aşmak · bir alanın başlangıç ve bitiş uçları
  عدا طوره أي جاز الحد الذي هو له من داره (maqayis)؛ عدا طوره أي جاوز حده (sihah)؛ بلغ فلان في العلم أطوريه أي حديه أوله وآخره (sihah)؛ عدا فلان طوره أي تجاوز حده (mufradat)
- **B004** ayrı kez, durum veya evre — kez veya evre · bir kezden sonra bir kez daha; dönem dönem · çeşitli durumlar, türler veya ardışık evreler
  فعل ذلك طورا بعد طور كأنه فعله مدة بعد مدة (maqayis)؛ الطور التارة يقال طورا بعد طور (ayn)؛ الناس أطوار أي أصناف على حالات شتى (ayn)؛ الطور التارة (sihah)؛ خلقكم أطوارا طورا علقة وطورا مضغة (sihah)؛ فعل كذا طورا بعد طور أي تارة بعد تارة (mufradat)؛ خلقكم أطوارا (mufradat)
- **B005** dağ veya belirli bir dağın adı — dağ; bağlama göre belirli bir dağın adı
  الطور جبل (maqayis)؛ الطور جبل معروف (ayn)؛ الطور الجبل (sihah)؛ الطور اسم جبل مخصوص وقيل اسم لكل جبل (mufradat)
- **B006** yabanıl ve insanlara alışmamış — yabanıl, yabanıllaşmış veya insanlara alışmamış
  للوحشي من الطير وغيرها طوري وطوارني فهو من هذا كأنه توحش فعدا الطور (maqayis)؛ رجل طوري وطوراني (ayn)؛ الطوري الوحشي من الطير والناس (sihah)؛ حمام طوري وطوراني (sihah)
- **B007** orada hiç kimsenin bulunmaması — orada hiç kimse yok
  ما بها طوري أي أحد (sihah)

## ر ء ي (root_000531): 71:15 تَرَوْا۟

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

## ECHO ر و ي (root_000615): for 71:15 تَرَوْا۟: withheld observed target; not identity

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

## س ب ع (root_000669): 71:15 سَبْعَ

- **B001** yedi sayısı ve yediye dayalı pay, sıra, dönem, işlem ve çokluk anlatımları — yedi · yedide bir · altı kişilik topluluğun yedincisi oldu · topluluğun malının yedide birini aldı · develer için yediye bağlı sulama aralığı · hafta; yedi günlük dönem · yapının çevresinde yedi tur döndü · metnin tamamını yedi geceye bölerek okudu · eşinin yanında yedi gece kaldı · bebeğin yedinci gününde saçını kesip onun için hayvan kesti · kabı yedi kez yıkadı · Tanrı onun ödülünü yedi katına ya da kat kat çıkardı · bir şeyi yedi yapmak ya da kat kat çoğaltmak · yetmiş; kimi bağlamlarda pek çok · yedide bir ya da yediye bağlı sulama aralığı için seyrek kullanılan biçim
  السين والباء والعين أصلان أحدهما في العدد؛ السبعة؛ السبع جزء من سبعة؛ سبعت القوم إذا أخذت سبع أموالهم أو كنت لهم سابعا؛ السبع ظمء من أظماء الإبل (maqayis)؛ السبع من العدد معروف؛ صرت سابعهم؛ سبع الشيء واحد من سبعة؛ الأسبوع؛ طفت بالبيت سبعا وسبوعا؛ سبع المولود؛ سبعت الإناء؛ سبع الله لك أي أعطاك أجرك سبع مرات (jamhara)؛ سبعة رجال وسبع نسوة؛ السبع جزء من سبعة؛ السبع الظمء؛ الأسبوع من الأيام؛ تسبيعا جعلته سبعة؛ وزن سبعة (sihah)؛ السبع من العدد معروف؛ السبعون معروف؛ أقام عندها سبعا؛ سبع فلان القرآن؛ الأسبوع؛ التكثير والتضعيف لا من باب حصر العدد (tahdhib)؛ أصل السبع العدد؛ سبع سماوات؛ سبعين مرة؛ سبعا من المثاني؛ السبع الطوال؛ السبيع والسبع في الورود؛ الأسبوع؛ طفت بالبيت أسبوعا؛ سبعت القوم (mufradat)
- **B002** avlayan yırtıcı hayvan ve onun saldırısına bağlı durumlar — yırtıcı hayvan · dişi yırtıcı; özellikle dişi aslan · yırtıcı hayvanların bol bulunduğu yer · onu yırtıcı hayvana yem etti · kurt sürüye saldırıp hayvanları parçaladı · yavrusu yırtıcı tarafından yenmiş dişi sığır ya da yabani hayvan · sürüsüne yırtıcı hayvan saldırmış çoban
  السبع واحد من السباع؛ أرض مسبعة إذا كثر سباعها؛ أسبعته أطعمته السبع؛ سبعت الذئاب الغنم إذا فرستها وأكلتها (maqayis)؛ السبع واحد السباع والأنثى سبعة (ayn)؛ السبع اسم يجمع السباع أسودها وذئابها؛ الذكر من السباع سبع والأنثى سبعة؛ أرض مسبعة ذات سباع (jamhara)؛ السبع واحد السباع؛ السبعة اللبؤة؛ أرض مسبعة ذات سباع؛ سبع الذئب الغنم أي فرسها؛ المسبوعة البقرة التي أكل السبع ولدها (sihah)؛ السبع يقع على ماله ناب من السباع ويعدو على الناس والدواب فيفترسها مثل الأسد والذئب والنمر والفهد؛ الثعلب ليس بسبع؛ الضبع لا يعد من السباع العادية؛ أرض مسبعة كثيرة السباع؛ سبعت الوحشية إذا أكل السبع ولدها (tahdhib)؛ والسبع معروف؛ قد وقع السبع في غنمه؛ المسبع موضع السبع (mufradat)
- **B003** birini kötüleyip arkasından çekiştirmek; sınırlı kullanımda ısırmak — onu kötüledi, arkasından çekiştirdi ya da ona sövdü · onu dişiyle ısırdı
  سبعته إذا وقعت فيه كأنه شبه نفسه بسبع في ضرره وعضه (maqayis)؛ سبعت فلانا عند فلان إذا وقعت فيه وقيعة مضرة (ayn)؛ سبعت الرجل عند السلطان وغيره إذا طعنت فيه (jamhara)؛ سبعته أي شتمته ووقعت فيه (sihah)؛ سبع فلان فلانا إذا قصبه واقترضه أي عابه واغتابه؛ سبع فلانا إذا عضه بسنه؛ يتساب الرجلان فيرمي كل واحد منهما صاحبه بما يسوءه (tahdhib)؛ سبع فلان فلانا اغتابه وأكل لحمه أكل السباع (mufradat)
- **B004** biçime bağlı adlandırmalar — el üstünde tutulmuş, bolluk içinde yaşatılan hizmetli · sürüsüne yırtıcı hayvan saldırmış çoban · başıboş bırakılmış kimse · babası bilinmeyen ya da soyu kuşkulu kimse · yedi aylık doğmuş bebek · çocuğunu sütanneye verdi · yırtıcı hayvanın bulunduğu yer
  عبد مسبع؛ أحدها المترف؛ الراعي؛ لم يكن لرشده؛ عبد إلى سبعة آباء؛ ولد لسبعة أشهر؛ المسبع المهمل (maqayis)؛ عبد مسبع عبد مترف؛ هو في لغة الدعي؛ المسبع الراعي الذي أغارت السباع على غنمه (ayn)؛ رجل مسبع إذا عاث السبع في غنمه؛ غلام مسبع إذا أهمل حتى صار كأنه سبع؛ المسبع الدعي (jamhara)؛ أسبع ابنه دفعه إلى الظؤورة؛ أسبع عبده أهمله؛ عبد قد صادف في غنمه سبعا؛ المسبوعة البقرة التي أكل السبع ولدها (sihah)؛ المسبع المهمل؛ ينسب إلى أربع أمهات؛ إلى سبع أمهات؛ التابعة؛ يولد لسبعة أشهر؛ وقع السباع في ماشيته (tahdhib)؛ وقع السبع في غنمه؛ المهمل مع السباع؛ كني بالمسبع عن الدعي الذي لا يعرف أبوه؛ المسبع موضع السبع (mufradat)
- **B005** çok sert biçimde ele geçirmek ya da en ağır kötülüğü yapmak [kalıp] — onu çok sert biçimde ele geçirdi · ona yapılabilecek en ağır kötülüğü yaptı
  لأفعلن به فعل سبعة يريدون به المبالغة في الشر؛ أراد بالسبعة اللبؤة؛ أراد سبعة فخفف (maqayis)؛ لأفعلن بك فعل سبعة؛ كان سبعة رجلا ماردا؛ فنكل به فصار مثلا (jamhara)؛ أخذه أخذ سبعة؛ أصلها سبعة فخففت؛ اللبؤة أنزق من الأسد؛ سبعة ابن عوف وكان رجلا شديدا (sihah)؛ أخذه أخذ سبعة؛ أصلها سبعة فخففت؛ اللبؤة أنزق من الأسد؛ سبعة بن عوف وكان رجلا شديدا؛ لأعملن بفلان عمل سبعة المبالغة وبلوغ الغاية (tahdhib)

## ط ب ق (root_000927): 71:15 طِبَاقًا

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

## ق م ر (root_001255): 71:16 ٱلْقَمَرَ

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

## ن و ر (root_001564): 71:16 نُورًا, 71:25 نَارًا

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

## ش م س (root_000818): 71:16 ٱلشَّمْسَ

- **B001** güneş, güneş diski ve ışığı; güneşli olma ve güneşe çıkma — güneş; güneşin görünen diski ve yayılan ışığı · gündüzünün tamamı güneşli olan gün · günümüz güneşli oldu; güneşi güçlendi · güneşte yapılmış ya da güneşe tutulmuş · güneşe çıkıp ona yönelmek
  الشمس معروفة (maqayis)؛ الشمس عين الضح (ayn;tahdhib)؛ الشمس يقال للقرصة وللضوء المنتشر عنها (mufradat)؛ يوم شامس وقد شمس يشمس شموسا (ayn;tahdhib)؛ شيء مشمس وتشمس (sihah)
- **B002** ürküp kaçınma, durulmama ve güçlük çıkarma — yerinde durmayan, dürtülünce sırtını kullandırmayan hayvan · huysuz, geçimsiz ve tutumu değişken adam · kuşkulu bir durumdan ürküp uzak duran kadın · kaçıp yerinde durmadı
  الشموس من الدواب الذي لا يكاد يستقر (maqayis)؛ الشمس والشموس من الدواب الذي إذا نخس لم يستقر (ayn;tahdhib)؛ شمس الفرس شموسا وشماسا أي منع ظهره (sihah)؛ رجل شموس عسر (ayn;tahdhib)؛ رجل شموس صعب الخلق (sihah)؛ امرأة شموس إذا كانت تنفر من الريبة (maqayis)؛ شمس فلان شماسا إذا ند ولم يستقر (mufradat)
- **B003** birine düşmanlığını açıkça göstermek [kalıp] — bana düşmanlığını açıkça gösterdi ve sert davrandı
  شمس لي فلان إذا أبدى لك عداوته (maqayis;sihah)؛ شمس لي فلان إذا أبدى لك عدواته (ayn)؛ شمس لي فلان إذا أبدى لك عداوته كأنه قد هم أن يفعل (tahdhib)
- **B004** kolye sarkıtları ya da bir kolye türü — kolyeye asılan süsler ya da bir kolye türü
  الشموس معاليق القلائد (ayn;tahdhib)؛ الشمس ضرب من القلائد (sihah)
- **B005** başı ortadan tıraşlı, kiliseye bağlı Hristiyan önder din görevlisi — başının ortasını tıraş eden ve kiliseye sürekli bağlı kalan Hristiyan önder din görevlisi
  الشماس من رؤساء النصارى الذي يحلق وسط رأسه لازما للبيعة (ayn;tahdhib)؛ الجميع الشمامسة (ayn;tahdhib)
- **B006** arkasındakini koruma, topluluğunu savunma ve iyiliğini esirgeme — arkasındakini koruyup engelleyen ya da topluluğunu güçlü biçimde savunan adam · bize karşı cimrilik etti ve iyiliğini esirgedi
  المتشمس من الرجال الذي يمنع ما وراء ظهره (tahdhib)؛ وهو الشديد القومية (tahdhib)؛ البخيل أيضا متشمس (tahdhib)؛ تشمس علينا أي بخل (tahdhib)
- **B007** güneş kökünden kişi, topluluk, put ve yer adları ile bağlılık türetmeleri — kul ve güneş öğelerinden kurulmuş birleşik bir Arap kişi adı · güneş adı verilen eski bir put · güneş adı verilen tanınmış bir su kaynağı · belirli bir topluluk içinde güneş sözcüğüne bağlanan kişi ya da soy adı · güneş öğeli kişi ya da soy adına mensup olan · güneş öğeli topluluğa antlaşma, koruma ilişkisi ya da bağlılık yoluyla bağlanmak · çıkışı zor olduğu için bu kökten adlandırılmış tanınmış bir tepe · Firdevs'in karşısında bulunan iki bahçenin ortak adı
  عبد شمس (maqayis;sihah)؛ الشمس صنم قديم (maqayis)؛ شمس عين ماء معروفة (maqayis)؛ عبشمس وعبشمي (maqayis;sihah)؛ تعبشم الرجل (sihah)؛ الشموس هضبة معروفة (tahdhib)؛ الشميستان جنتان بإزاء الفردوس (tahdhib)

## س ر ج (root_000693): 71:16 سِرَاجًا

- **B001** fitilli ve yağlı ışık aracı; ayrıca aydınlatan şey — ışık veren lamba; ayrıca aydınlatan her şey · lambayı yaktı · fitil ile yağın konduğu lamba kabı · lamba kabının konduğu yer · güneş, gündüzün lambasıdır · doğru yol, inananların ışığıdır · apaçık bir kitap ya da karanlıkta yol gösteren kişi
  السراج سمي لضيائه وحسنه (maqayis)؛ السراج الزاهر الذي يزهر بالليل (ayn;tahdhib)؛ السراج معروف وتسمى الشمس سراجا (jamhara;sihah)؛ السراج الزاهر بفتيلة ودهن ويعبر به عن كل مضيء (mufradat)
- **B002** eyer ve buna bağlı eylem, usta ve zanaat — eyer; hayvanın binme aracı ve süsü · hayvanı eyerledi · eyer yapan usta · eyer yapımcılığı
  السرج للدابة هو زينته (maqayis)؛ حرفة السراج السراجة وأسرجت السرج وأسرجت الدابة (ayn)؛ السرج معروف (jamhara;sihah)؛ السرج رحالة الدابة ومتخذه سراج وحرفته السراجة (tahdhib)؛ السرج رحالة الدابة والسراج صانعه (mufradat)
- **B003** güzelleştirme; burunda incelik, uzanış veya parlaklık — yüzünü güzelleştirdi ve hoşlaştırdı · ince ve düzgün uzanan ya da parlak görünen burun
  سرج وجهه أي حسنه (maqayis)؛ سرج الله وجهه وبهجه أي حسنه (ayn;tahdhib)؛ أنف مسرج دقيق كالسيف السريجي (jamhara;sihah;tahdhib)؛ مسرجا أراد منيرا كلون السراج (jamhara)؛ سرجت كذا جعلته في الحسن كالسراج (mufradat)
- **B004** doğuştan huy, tutulan yol ve huy uyumu — doğuştan huy veya tutulan yol · doğuştan huy · aynı yol üzerinde veya uyumlu huyda · iyi huylu
  قولهم للطريقة سرجوجة (maqayis)؛ السرجوجة الطبيعة والطريقة (sihah)؛ كريم السرجوجة والسرجيجة أي كريم الطبيعة وهم على سرجوجة واحدة (tahdhib)
- **B005** yalancı olma, yalan söyleme ve sözü yalanla örtme — yalancı · yalan söyledi · sözünün üstünü başka bir yalanla örttü
  السراج الكذاب وقد سرج أي كذب؛ تكلم بكلمة فسرج عليها بأسروجة (tahdhib)

## ن ب ت (root_001465): 71:17 أَنۢبَتَكُم, 71:17 نَبَاتًا

- **B001** yerden çıkan ve büyüyen bitki; bitkinin filizlenip büyümesi — yerden çıkan canlı bitki · bitki; bitkinin çıkıp büyümesi · filizlenip büyümek · toprak bitkisini çıkardı · onu yeşertip büyüttü · ot filizlendi · yerde biten irili ufaklı bitkiler
  أصل واحد يدل على نماء في مزروع (maqayis)؛ نبت الشيء نباتا ونبتا وأنبته الله إنباتا (jamhara)؛ النبت: النبات، نبتت الأرض وأنبتت (sihah)؛ كل ما أنبتت الأرض فهو نبت (tahdhib)؛ النبت والنبات ما يخرج من الأرض من الناميات (mufradat)
- **B002** dikerek veya ekerek yetişmesini başlatmak [kalıp] — ağacı dikerek yetişmesini başlatmak · tohumu ekmek
  نبت الشجر: غرسته (maqayis)؛ نبت الشجر تنبيتا: غرسته (sihah)؛ نبت فلان الحب والشجر تنبيتا إذا غرسه وزرعه (tahdhib)
- **B003** bir toplulukta sonradan yetişen genç kuşak — bir toplulukta yeni yetişen genç kuşak · kötülüğe yönelen yeni grup · genç ve deneyimsiz kimseler
  نبتت لبني فلان نابتة إذا نشأ لهم نشء صغار من الولد (maqayis)؛ نابتة شر (maqayis;mufradat)؛ النوابت من الأحداث الأغمار (sihah)؛ إنباتة لحقت يعني بالنابتة ناسا ولدوا فلحقوا (tahdhib)
- **B004** kökten türeyen kişi ve topluluk adları — Yemen'den bir topluluğun adı · Araplardan bir topluluğun adı · bir Arap kişi adı · bir Arap kişi adı · bir erkek kişi adı
  النبيت حي من اليمن (maqayis;sihah)؛ سمت العرب نابتا ونبتا ونبيتا ونباتة وبنو النبت حي منهم (jamhara)؛ نباتة اسم رجل ونبت من الأسماء (tahdhib)
- **B005** yetişme yeri, köken ve gelişme biçimi — köken veya yetişme yeri · iyi ve saygın bir köken · yetişme hali ve görünüşü · bir ailenin malı ve çocuklarının geliştiği durum
  ما أحسن نبتة هذا الشجر، وهو في منبت صدق أي أصل كريم (maqayis)؛ الرجل في منبت صدق أي في أصل كريم (jamhara)؛ المنبت موضع النبات، ما أحسن نابتة بني فلان أي ما تنبت عليه أموالهم وأولادهم (sihah)؛ المنبت الأصل والموضع الذي ينبت فيه الشيء، حسن النبتة أي الحالة التي ينبت عليها (tahdhib)
- **B006** insanın büyüyüp yetişmesi veya bakımla yetiştirilmesi [kalıp] — ergenliğe yaklaşıp belirli beden tüyü belirmek · çocuğu besleyip yetiştirmek · kızı besleyip iyi bakarak yetiştirmek · onu güzel biçimde yetiştirmek
  أنبت الغلام إذا راهق واستبان شعر عانته (jamhara)؛ أنبت الغلام أي نبتت عانته، ونبت الصبى تنبيتا ربيته (sihah)؛ أنبتها نباتا حسنا أي جعل نشوها نشوا حسنا، والرجل ينبت الجارية يغذوها (tahdhib)؛ يستعمل في كل نام نباتا كان أو حيوانا أو إنسانا (mufradat)
- **B007** iki türü ve meyvesi bulunan belirli bir ağaç — iki türü ve meyvesi bulunan belirli bir ağaç · bu ağaç türünden tek bir birey
  الينبوت فشجر معروف (jamhara)؛ الينبوت: شجر (sihah)؛ الينبوت شجر الخشخاش الواحدة ينبوتة، والينبوت ضربان (tahdhib)
- **B008** aşağılık ve değersiz olma [kalıp] — aşağılık ve değersiz adam · aşağılık ve değersiz şey
  رجل خبيت نبيت إذا كان خسيسا حقيرا، وكذلك شيء خبيث نبيث (tahdhib)

## ء ر ض (root_000025): 71:17 ٱلْأَرْضِ, 71:19 ٱلْأَرْضَ, 71:26 ٱلْأَرْضِ

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

## ع و د (root_001058): 71:18 يُعِيدُكُمْ

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

## ECHO ع د د (root_000989): for 71:18 يُعِيدُكُمْ: withheld observed target; not identity

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

## خ ر ج (root_000400): 71:18 وَيُخْرِجُكُمْ, 71:18 إِخْرَاجًا

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

## ب س ط (root_000116): 71:19 بِسَاطًا

- **B001** yaymak ve uzatmak — bir şeyi yaymak, uzatmak ve genişletmek · toplamanın karşıtı olan yayılma ve açılma · bir şeyin yere yayılıp uzanması · bir şeyi yaymak
  أصل واحد وهو امتداد الشيء في عرض أو غير عرض (maqayis)؛ البسط نقيض القبض (ayn)؛ بسط الشيء نشره وانبسط الشيء على الأرض (sihah)؛ البسط نقيض القبض (tahdhib)؛ بسط الشيء نشره وتوسيعه (mufradat)
- **B002** yaygı; geniş ve düz arazi — yaygı veya geniş, yayılmış arazi · yayılmış, geniş arazi · geniş veya yayılmış yer · çıkıntısız, düz arazi
  البساط ما يبسط والبساط الأرض وهي البسيطة (maqayis)؛ البسيطة من الأرض كالبساط من المتاع (ayn)؛ البساط ما يبسط والبساط الأرض الواسعة ومكان بسيط وبساط (sihah)؛ البساط الأرض العريضة الواسعة وأرض بساط مستوية لا نبك فيها (tahdhib)؛ البساط اسم لكل مبسوط والله جعل لكم الأرض بساطا (mufradat)
- **B003** genişlik, artış ve üstünlük — genişlik, artış ve üstünlük · genişlik veya artış · geçim imkanlarını genişletip çoğaltmak · bilgi ve bedende genişlik ve artış · geniş yapılı veya erişimi uzun · sahibini rahatça alacak geniş yatak
  البسطة في كل شيء السعة وهو بسيط الجسم والباع والعلم (maqayis)؛ البسطة الفضيلة على غيرك (ayn)؛ البسطة السعة وفلان بسيط الجسم والباع وفراش يبسطك إذا كان واسعا (sihah)؛ فالبسطة الزيادة وفراش يبسطني إذا كان سابغا (tahdhib)؛ ولو بسط الله الرزق أي وسعه وزاده بسطة أي سعة (mufradat)
- **B004** eli uzatıp serbestçe kullanmak [kalıp] — eli istemek, almak, saldırmak veya vermek için uzatmak · vermeye açık ve serbest el · iki kolunu uzatmış · istemek için iki avucunu suya doğru uzatan
  يد فلان بسط إذا كان منفاقا (maqayis)؛ بسط إلينا فلان يده بما نحب ونكره (ayn)؛ يد بسط أي مطلقة وبل يداه بسطان (sihah)؛ بسط فلان يده بما يحب ويكره وبسطان مبسوطتان (tahdhib)؛ بسط اليد مدها وبسط الكف للطلب والأخذ والصولة والبذل (mufradat)
- **B005** rahat ve açık ilişki kurmak — rahat ve akıcı konuşan erkek · rahat konuşan veya kolay ilişki kuran kadın · çekingenliği bırakıp rahatça ilişki kurma · insanlara sevimli gelen açık yüz
  البسيط الرجل المنبسط اللسان والمرأة بسيطة (ayn)؛ الانبساط ترك الاحتشام وبسطت من فلان فانبسط (sihah)؛ البسيط الرجل المنبسط اللسان وليكن وجهك بسطا (tahdhib)
- **B006** beni de sevindirir [kalıp] — seni sevindiren şey beni de sevindirir
  إنه ليبسطني ما بسطك ويقبضني ما قبضك أي يسرني ما سرك ويسوءني ما ساءك (ayn)؛ إنه ليبسطني ما بسطك ويقبضني ما قبضك أي يسرني ما سرك ويسوءني ما ساءك (tahdhib)
- **B007** dolaşmak ve gezintiye çıkmak — ülkede enine boyuna dolaşmak · bitkili açık alanda gezintiye çıkmak
  تبسط في البلاد أي سار فيها طولا وعرضا (sihah)؛ التبسط التنزه خرج يتبسط مأخوذ من البساط وهي الأرض ذات الرياحين (tahdhib)
- **B008** yavrusuyla serbest bırakılan dişi deve — yavrusuyla bırakılan ve ondan esirgenmeyen dişi deve · yavrularıyla serbest bırakılmış dişi develer · dişi deveyi yavrusuyla bırakmak
  الناقة التي خليت هي وولدها لا تمنع منه بسط (maqayis)؛ الأبساط من النوق التي معها أولادها والواحد بسط (ayn)؛ البسط الناقة تخلى مع ولدها لا يمنع منها (sihah)؛ البساط جمع بسط وهي الناقة التي تركت وولدها لا يمنع منها (tahdhib)؛ البسط الناقة تترك مع ولدها وقد أبسط ناقته أي تركها مع ولدها (mufradat)
- **B009** belirli bir şiir ölçüsü — belirli bir şiir ölçüsü türü
  البسيط نحو من العروض (ayn)؛ البسيط جنس من العروض (sihah)
- **B010** sunulan gerekçeyi kabul etmek [kalıp] — kusur için sunulan gerekçeyi kabul etmek
  بسط العذر قبوله (sihah)
- **B011** uzak mesafe ve tam uzanma erişimi [kalıp] — uzun ve uzak geçit · ayakta durup eli uzatarak ulaşılan tam boy mesafesi · ulaşılabilir bir millik mesafe
  سرنا عقبة باسطة وهي البعيدة (sihah)؛ عقبة باسطة أي بعيدة طويلة وقامة باسطة إذا حفر مدى قامته وقد مد يده (tahdhib)
- **B012** yapısal olarak bileşiksiz — parçalardan oluşması veya düzenlenmesi düşünülemeyen
  استعار قوم البسط لكل شيء لا يتصور فيه تركيب وتأليف ونظم (mufradat)
- **B013** çatallı olmayan deve semeri — çatallı olmayan deve semeri · çatalsız, yayvan deve semeri
  الباسوط من الأقتاب ضد المفروق ويقال قتب مبسوط ويجمع مباسيط (tahdhib)

## س ل ك (root_000735): 71:20 لِّتَسْلُكُوا۟

- **B001** yolda ilerleme ve izlenen yol — yolda ilerleme · yola girip yol boyunca ilerlemek · izlenen yol
  سلكت الطريق أسلكه (maqayis)؛ والمسلك الطريق سلكته سلوكا (ayn)؛ السلوك مصدر سلك طريقا والمسلك الطريق (tahdhib)؛ السلوك النفاذ في الطريق (mufradat)
- **B002** bir şeyi başka bir şeyin içine sokup ilerletme — bir şeyi başka bir şeyin içine sokma · bir şeyi başka bir şeyin içine sokma · bir şeyi başka bir şeyin içine sokup ilerletmek · onu içine sokmak · içine sokulunca içeri girmek
  سلكت الشيء في الشيء أنفذته (maqayis)؛ إدخال الشيء في شيء تسلكه فيه (ayn)؛ أدخلته فيه فدخل ومنه أسلكته فيه (sihah)؛ الله يسلك الكفار في جهنم أي يدخلهم فيها وسلكته في المكان وأسلكته بمعنى واحد (tahdhib)؛ من الثاني قوله ما سلككم في سقر وكذلك نسلكه في قلوب المجرمين (mufradat)
- **B003** doğrudan karşıya yönelen düz saplama; düzgün iş veya görüş — doğrudan karşıya yönelen düz saplama · doğru ve düzgün · doğrudan karşıya yapılan saplama
  الطعنة السلكى إذا طعنه تلقاء وجهه (maqayis)؛ والسلكى الأمر المستقيم (ayn)؛ الطعنة السلكى المستقيمة تلقاء وجهه (sihah)؛ الطعنة السلكى هي المستقيمة والرأي مخلوجة وليس بسلكى أي ليس بمستقيم (tahdhib)؛ الطعنة السلكة تلقاء وجهك (mufradat)
- **B004** dikiş ipliği — dikiş ipliği · dikiş iplikleri · bir dikiş ipliği
  السلك والجميع السلوك الخيوط التي يخاط بها الثياب الواحدة سلكة (ayn)؛ السلك الخيط (sihah)؛ السلك الخيوط التي يخاط بها الثياب الواحدة سلكة والجميع السلوك (tahdhib)
- **B005** kumaş kenarı boyunca uzanan şerit — kumaş kenarı boyunca uzanan şerit
  المسلكة طرة تشق من ناحية الثوب وإنما سميت بذلك لامتدادها وهي كالسكك (maqayis)
- **B006** cinsiyet ve sayı biçimleriyle keklik yavrusu; kimi kullanımda bağırtlak yavrusu — erkek keklik yavrusu; kimi kullanımda bir bağırtlak yavrusu · dişi keklik yavrusu; kimi kullanımda dişi bağırtlak yavrusu · keklik yavruları; kimi kullanımda bağırtlak yavruları · bir bağırtlak yavrusu
  السلكة الأنثى من ولد الحجل والذكر سلك وجمعه سلكان (maqayis)؛ والسلكان فراخ القطا الواحد سلك والأنثى سلكة ويقال سلكانة (ayn)؛ السلك ولد الحجل والأنثى سلكة والجمع سلكان (sihah)؛ السلك ولد الحجل وجمعه سلكان والسلكان فراخ القطا (tahdhib)؛ السلكة الأنثى من ولد الحجل والذكر السلك (mufradat)

## س ب ل (root_000672): 71:20 سُبُلًا

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

## ف ج ج (root_001131): 71:20 فِجَاجًا

- **B001** dağlar arasındaki geniş yol veya geçit — dağ içindeki veya iki dağ arasındaki geniş yol · geniş yollar; geniş geçitler · dağdaki geniş yol · geniş geçitlerden geçti · geniş vadi
  الفج الطريق الواسع (maqayis;ayn;sihah;tahdhib)؛ الطريق الواسع في الجبل أوسع من الشعب (jamhara)؛ شقة يكتنفها جبلان ويستعمل في الطريق الواسع (mufradat)؛ كل طريق بعد فهو فج والإفجيج الوادي الواسع (tahdhib)
- **B002** bacakların arasını açmak — bacakların veya uylukların birbirinden fazla açık olması · bacaklarını birbirinden ayırdı · bacaklarımın arasını açtım · bir bacağını ötekinden uzaklaştırdı · uylukları birbirinden çok ayrık
  أصل صحيح يدل على تفتح وانفراج والفجج أقبح من الفحج (maqayis)؛ الفجج أقبح من الفحج ورجل أفج (ayn)؛ فج الرجل رجليه إذا باعد بينهما وكذلك الدابة (jamhara)؛ فججت ما بين رجلي إذا فتحت ورجل أفج (sihah)؛ تفريجك بين الشيئين وفاج الرجل إذا باعد إحدى رجليه من الأخرى (tahdhib)
- **B003** kirişi gövdesinden ayrık yay; kubbemsi toynak — kirişi gövdesinden uzak duran yay · kirişi gövdesinden ayrık yay · kirişi gövdesinden ayrık yay · yayın kirişini gövdesinden kaldırdı · kubbe biçimli toynak
  قوس فجاء إذا بان وترها عن كبدها وحافر مفج أي مقبب (maqayis)؛ قوس فجاء إذا ارتفعت سيتها فبان وترها عن عجسها (jamhara)؛ قوس فجاء وفجواء إذا بان وترها عن كبدها وحافر مفج أي مقبب (sihah)؛ فج قوسه إذا رفع وترها من كبدها والفجاء والمنفجة والفجواء (tahdhib)
- **B004** hızlanmak veya çok hızlı koşmak; ayrıca salıvermek — hızlandı; çok hızlı koştu · salıverdi
  أفج يفج إذا أسرع (maqayis)؛ أفج إفجاجا أي أسرح وأفاج لغة (ayn)؛ افج فهو مفج إذا عدا عدوا شديدا (jamhara)؛ أفج الرجل أي أسرع (sihah)
- **B005** devekuşunun dışkısını atması — devekuşu dışkısını attı · devekuşu dışkısını attı
  النعامة تفج إفجاجا إذا رمت بصومها (ayn)؛ أفجت النعامة رمت بصومها (sihah)؛ النعامة تفج إذا رمت بصومها (tahdhib)
- **B006** ham ve olgunlaşmamış — ham; olgunlaşmamış · sert, olgunlaşmamış kavun
  الفج الشيء لم ينضج مما ينبغي نضجه (maqayis)؛ كل شيء من البطيخ والفواكه لم ينضج فهو فج (sihah)؛ بطيخ فج إذا كان صلبا غير نضيج والثمار كلها تكون فجة والفج الني (tahdhib)
- **B007** çok konuşma, gürültücülük ve küstahlık — çok konuşan; geveze · çok konuşup bağırıp çağıran · küstahlık; kendini beğenmişlik
  رجل فجفاج كثير الكلام (maqayis;sihah)؛ الفجفجة الصلف (ayn)؛ رجل فجافج كثير الكلام والصياح والجلبة (tahdhib)
- **B008** ağır kimseler — ağır kimseler
  الفجج الثقلاء من الناس (tahdhib)

## ع ص ي (root_001022): 71:21 عَصَوْنِى

- **B001** buyruğa uymayıp söz dinlemekten çıkma — buyruğa karşı gelmek; söz dinlememek · söz dinlememe; buyruğa karşı gelme · buyruğa aykırı davranış · söz dinlemeyen, buyruğa karşı gelen kimse · boyun eğmeyen, söz dinlemeyen kimse · ona karşı gelmek; sözünü dinlememek · söz dinlemez duruma gelmek; boyun eğmemek · topluluğun birliğini bozup onu bölmek · anlaşmazlık çıkıp birliğin dağılması
  العصيان خلاف الطاعة، وقد عصاه يعصيه عصيا ومعصية (sihah)؛ عصى فلان أميره يعصيه عصيا وعصيانا إذا لم يطعه، وعصى العبد ربه إذا خالف أمره (tahdhib)؛ عصى عصيانا إذا خرج عن الطاعة (mufradat)

## ت ب ع (root_000175): 71:21 وَٱتَّبَعُوا۟

- **B001** ardından gitmek ve yolunu benimsemek — birlikte ya da arkasından yürümek · izinden gitmek, örneğini veya buyruğunu benimsemek · ardından giden kimse · ardından giden kimse veya topluluk
  التابع التالي؛ يتبعه يتلوه؛ تبعه يتبعه تبعا؛ هؤلاء تبع وأتباع (ayn)؛ تبعت الرجل إذا مشيت معه (jamhara)؛ تبعت القوم تبعا وتباعة إذا مشيت خلفهم؛ التبع يكون واحدا وجماعة (sihah)؛ التابع التالي؛ اتباع بالمعروف؛ اتبعوا القرآن (tahdhib)؛ تبعه واتبعه قفا أثره تارة بالجسم وتارة بالارتسام والائتمار (mufradat)
- **B002** geriden yetişmek veya peşine takmak — önden gidene yetişmek veya başkasını peşine takmak · uzaklaşan topluluğun izlerini gözle sürdürmek
  وأتبعت القوم بصري إذا أتبعت النظر في آثارهم (jamhara)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعت غيري؛ أتبعه الشيء فتبعه (sihah)؛ أتبعت القوم إذا كانوا قد سبقوك فلحقتهم؛ أتبعه يريد به شرا؛ ما زلت أتبعهم حتى أتبعتهم أي حتى أدركتهم (tahdhib)؛ أتبعه إذا لحقه (mufradat)
- **B003** adım adım iz sürüp araştırmak — bir şeyi zaman içinde parça parça aramak · izleri adım adım araştırmak
  التتبع فعلك شيئا بعد شيء؛ تتبعت علمه أي اتبعت آثاره (ayn)؛ تتبعت الشيء تتبعا أي تطلبته متتبعا له (sihah)؛ التتبع أن يتتبع في مهلة شيئا بعد شيء؛ يتتبع مساوىء فلان وأثره؛ أتتبعه من اللخاف والعسب (tahdhib)
- **B004** aralıksız peş peşe gelmek — kesintisiz ardışıklık · iki şeyi ara vermeden peş peşe yapmak · aralıksız olarak peş peşe
  التباع الولاء؛ تابعه على كذا متباعة وتباعا (sihah)؛ تابع بين الصلاة وبين القراءة إذا والى بينهما؛ تباعا أي ولاء؛ يتابع الحديث إذا كان يسرده (tahdhib)؛ فأتبعنا بعضهم بعضا (mufradat)
- **B005** hak istemek ve alacağı ödeyene yöneltmek — hak, öç veya alacak isteyen kimse · alacak için ödeme gücü olan kişiye yönlendirilmek · kan bedelini veya hakkı uygun biçimde istemek
  ليس عليك من هذا الأمر تبيعة وتباعة وتبعة (jamhara)؛ التبيع الذي لك عليه مال (sihah)؛ التبيع تابع بالثأر أو مطالب؛ اتباع بالمعروف أي المطالبة بالدية؛ له عليك مال يتابعك به أي يطالبك به؛ إذا أتبع أحدكم على مليء فليتبع (tahdhib)؛ أتبعت عليه أي أحلت عليه؛ أتبع فلان بمال أي أحيل عليه (mufradat)
- **B006** üzerinde kalan yükümlülük veya olumsuz sonuç — kişinin üzerinde kalan hak, sorumluluk veya istenmeyen sonuç
  ليس عليك من هذا الأمر تبيعة وتباعة وتبعة أي لا يلحقك منه شيء تكرهه (jamhara)؛ التباعة مثل التبعة (sihah)؛ التبعة والتباعة اسم للشيء الذي لك فيه بغية شبه ظلامة (tahdhib)
- **B007** ilk yılındaki sığır yavrusu ve yavrusu ardındaki inek — ilk yaş yılındaki erkek sığır yavrusu · ilk yaş yılındaki dişi sığır yavrusu · yavrusu arkasından gelen inek
  بقرة متبع إذا كان ولدها يتبعها والولد تبيع (jamhara)؛ التبيع ولد البقرة في أول سنة والأنثى تبيعة (sihah)؛ يأخذ من كل ثلاثين من البقر تبيعا؛ ولد البقرة أول سنة تبيع؛ بقرة متبع خلفها تبيع (tahdhib)؛ التبيع خص بولد البقر إذا تبع أمه؛ المتبع من البهائم التي يتبعها ولدها (mufradat)
- **B008** biçime bağlı adlandırmalar — güneşin hareketini izleyen gölge · belirli bir yıldızın adı · belirli bir kuş veya iri kanatlı böcek türü · binek hayvanının ayağı veya bacakları
  القوائم يقال لها تبع (ayn)؛ سمي الظل تبعا لاتباعه الشمس (jamhara)؛ التبع أيضا الظل؛ التبع أيضا ضرب من الطير (sihah)؛ التبع الطل؛ التبع هو الدبران؛ التابع والتويبع؛ التبع ضرب من اليعاسيب؛ التبع سيد النحل (tahdhib)؛ التبع رجل الدابة؛ التبع الظل (mufradat)
- **B009** eski güneybatı Arabistan hükümdar unvanı — eski güneybatı Arabistan krallık geleneğinde hükümdar · aynı gelenekte birbirinin ardından gelen hükümdarlar
  التبابعة سموا بذلك لاتباع بعضهم في الملك بعضا (jamhara)؛ التبابعة ملوك اليمن الواحد تبع (sihah)؛ تبع الملك؛ كان تبع ملكا من الملوك؛ فيهم تبابعة (tahdhib)؛ تبع كانوا رؤساء سموا بذلك لاتباع بعضهم بعضا في الرياسة والسياسة؛ تبع ملك يتبعه قومه (mufradat)
- **B010** insanı her yerde izleyen dişi doğaüstü eşlikçi — bir insanı gittiği her yerde izleyen dişi doğaüstü varlık
  التابعة جنية تكون مع الإنسان تتبعه حيثما ذهب (ayn)؛ معه تابعة أي من الجن (sihah)
- **B011** kadınların peşinden cinsel amaçla gitmek [kalıp] — kadın kölelerle evlilik dışı ilişki kurmak veya bunun için peşlerinden gitmek · kadınların peşinden cinsel amaçla giden erkek
  فلان يتابع الإماء أي يزانيهن (ayn)؛ فلان تبع نساء أي يتبعهن؛ حدث نساء يحادثهن؛ وزير نساء يزورهن (tahdhib)
- **B012** sağlamlaştırmak, uyumlu olmak veya iyi duruma getirmek — işini sağlam ve ustaca yapmak · sözünü sağlam kurmak veya anlatıyı ustaca sürdürmek · beden yapısı düzgün ve orantılı · bilgisi kendi içinde tutarlı · otlak hayvanları besleyip semirtmek ve güzelleştirmek
  تابع الرجل عمله أي أتقنه وأحكمه (sihah)؛ تابعنا الأعمال أي أحكمناها وعرفناها؛ تابع فلان كلامه؛ فرس متتابع الخلق أي مستو؛ متتابع العلم إذا كان علمه يشاكل بعضه بعضا؛ تابع المرتع المال فتتابعت (tahdhib)

## و ل د (root_001683): 71:21 وَوَلَدُهُۥٓ, 71:27 يَلِدُوٓا۟, 71:28 وَلِوَٰلِدَىَّ

- **B001** ana babadan doğan kişi veya kişiler — birinin çocuğu; bir veya birden çok doğmuş kişi · çocuklar · doğmuş çocuk; yeni doğan · kim olduğunu bilmiyorum · birbirlerinden çocuk sahibi olup çoğaldılar
  أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)
- **B002** öz ana baba — öz baba · öz ana · ana baba
  الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)
- **B003** çocuğu dünyaya getirme — kadın çocuğunu dünyaya getirdi · doğum; çocuğu dünyaya getirme · doğum zamanı geldi · gebe koyun · koyunun doğumunu üstlendik · birbirlerinden çocuk sahibi olup çoğaldılar
  ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)
- **B004** yeni doğmuş çocuk veya köle — yeni doğmuş erkek çocuk; erkek köle · kız çocuk; kadın köle
  الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)
- **B005** bir şeyden nedenle türeme veya sonradan oluşturulma — bir şeyin başka bir şeyden bir nedenle ortaya çıkması · sonradan oluşturulmuş, uydurulmuş veya katışıksız olmayan · katışıksız sayılmayan dil veya kişi
  تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)
- **B006** yaşıt — yaşıt; aynı yaşta olan kimse
  اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)
- **B007** çok büyük bir durum ya da pek bol bir şey [kalıp] — çok büyük veya ağır bir durum yahut çok bol bir şey için söylenen kalıp söz
  أمر لا ينادى وليده؛ قيل ذلك لكل أمر عظيم ولكل شيء كثير (sihah)؛ هو أمر لا ينادى وليده؛ أمر جليل شديد؛ أصله في الغارة؛ طعام لا ينادى وليده؛ عشب لا ينادى وليده (tahdhib)

## خ س ر (root_000409): 71:21 خَسَارًا

- **B001** eksilme ve değer yitimi — eksilme ve değerden düşme · eksilme, azalma ve değer yitimi · azalmak veya bir eksilmeye uğramak · eksilme ya da eksik kalan sonuç
  أصل واحد يدل على النقض (maqayis); الخسر النقصان والخسران كذلك (ayn;tahdhib); خسر إذا نقص ميزانا أو غيره (tahdhib)
- **B002** alım satımda kazanç sağlayamama veya anaparadan yitirme — satıcının anaparasından yitirmesi veya kazanç sağlayamaması · satışta kazanç sağlayamamak · alışverişinde kazanç sağlayamayan veya anaparasından yitiren kişi · alım satımda kazanç sağlayamama ya da anaparadan yitirme · kazanç getirmeyen alışveriş · alışveriş işinin kazanç getirmemesi veya anaparayı eksiltmesi
  الخاسر الذي وضع في تجارته (ayn;tahdhib); خسر التاجر إذا وضع من رأس ماله (jamhara); خسر في البيع خسرا وخسرانا (sihah); انتقاص رأس المال (mufradat); صفقة خاسرة أي غير مربحة (ayn;tahdhib)
- **B003** ölçü ve tartıda eksiltme — teraziyi veya tartılan şeyi eksik bırakmak · ölçerken ya da tartarken eksik vermek · verirken eksik ölçüp alırken daha çoğunu isteyen kişi · ölçü ve tartıda eksiltmeyin, haksızlık etmeyin
  خسرت الميزان وأخسرته إذا نقصته (maqayis); كلته ووزنته فأخسرته أي نقصته (ayn;tahdhib); أخسرت الميزان وخسرته (tahdhib); خسرت الشيء وأخسرته نقصته (sihah); ولا تخسروا الميزان (mufradat); ينقصون في الكيل والوزن (tahdhib)
- **B004** doğru yoldan sapıp iyiliklerini yitirerek yıkıma düşme — doğru yoldan sapma ve yıkıma uğrama · sapma, yitim ve yıkım · maddi olmayan iyilikleri de kapsayan yitim ve yıkım · yıkıma uğramak · yıkıma uğratma veya iyilikten uzaklaştırma · bu dünyadaki ve öte dünyadaki kazanımlarını yitirmek · kendilerini ve yakınlarını yitirmek · yarar sağlamayan dönüş · yaptıkları en çok boşa giden
  الخسر والخسار والخسران واحد وهو الضلال (jamhara); التخسير الإهلاك (sihah); الخسار والخسارة والخيسرى الضلال والهلاك (sihah); خسر إذا هلك (tahdhib); لفي عقوبة بذنوبه (tahdhib); غير إبعاد من الخير (tahdhib); المقتنيات النفسية كالصحة والسلامة والعقل والإيمان والثواب (mufradat)
- **B005** yitim, yıkım veya güçsüz kişileri bildiren genişlemiş biçimler — yitim veya kayıp bildiren genişlemiş biçim · yitim ya da yıkım bildiren genişlemiş biçim · güçsüz veya aşağı görülen insanlar · tekili bulunmayan, yıkım anlamındaki çoğul biçim
  رجل خنسرى وقالوا خيسرى في موضع الخسران النون والياء زائدتان (jamhara); الخناسر جمع خنسر وهو نحو الخنسرى وفي معناه وهم لئام الناس ورذالهم (jamhara); الخناسر الضعاف من الناس (jamhara); الخناسير الهلاك لا واحد له (sihah)

## م ك ر (root_001438): 71:22 وَمَكَرُوا۟, 71:22 مَكْرًا

- **B001** gizli hileyle amacından saptırma — gizli hile ve aldatmayla amacından saptırma · birine hile yapmak ve onu aldatmak · hileye karşılık ceza verme · savaşta taktik düzen ve hile
  المكر: الاحتيال والخداع (maqayis;sihah)؛ المكر احتيال في خفية (ayn;tahdhib)؛ صرف الغير عما يقصده بحيلة (mufradat)؛ المكرة: التدبير والحيلة في الحرب (tahdhib)؛ المكر من الله: جزاء (tahdhib)
- **B002** dolgun ve biçimli baldır — baldırın dolgun ve güzel biçimli oluşu · dolgun ve biçimli baldırlı kadın · sıkı ve toplu yapılı kadın · kalınca ve güzel biçimli baldır
  المكر: خدالة الساق؛ امرأة ممكورة الساقين (maqayis)؛ المكر حسن خدالة الساق؛ مرتوية الساق خدلة (ayn;tahdhib)؛ الممكورة: المطوية الخلق من النساء؛ خدلاء (sihah)؛ المكرة: الساق الغليظة الحسناء (tahdhib)
- **B003** belirli bir bitki veya ağaç türü — belirli bir bitki türü · bu bitkinin tek bir örneği · bir ağaç türü veya ağaç türleri · bu bitkinin meyvesi
  المكر ضرب من النبات الواحدة مكرة وسميت لارتوائها (ayn;tahdhib)؛ المكور ضرب من الشجر وضروب من الشجر (ayn;sihah;tahdhib)؛ الواحد مكر وفراخ المكر ثمره (sihah)
- **B004** boyamada kullanılan aşı boyası — boyamada kullanılan aşı boyası · aşı boyasıyla boyamak ve boyanmak · sakalların aşı boyasıyla boyanması
  المكر: المغرة (ayn;sihah)؛ مكره فامتكر أي خضبه فاختضب (sihah)؛ تمتكر اللحى أي تختضب؛ طلي بالمغرة (tahdhib)
- **B005** toprağı veya ürünü sulama — toprağı sulama · sert toprağı sulayıp sonra sürmek · ürüne verilen bir sulama · sulanmış ürün
  المكر: سقي الأرض؛ امكروا الأرض فإنها صلبة ثم احرثوها؛ المكرة: السقية للزرع؛ زرع ممكور أي مسقي (tahdhib)
- **B006** bozulmuş yaş hurma — bozulmuş yaş hurma
  المكرة: الرطبة الفاسدة (tahdhib)

## و ذ ر (root_001638): 71:23 تَذَرُنَّ, 71:23 تَذَرُنَّ, 71:26 تَذَرْ, 71:27 تَذَرْهُمْ

- **B001** et parçası; bir aktarımda etsiz kemik parçası — et parçası; bir aktarıma göre etsiz kemik parçası · et parçaları · bol et parçalı ekmek yemeği
  الوذرة وهي الفدرة من اللحم (maqayis)؛ الوذرة قطعة عظم لا لحم فيه (ayn)؛ الوذرة بالتسكين الفدرة وهي القطعة من اللحم (sihah)؛ الوذرة القطعة من اللحم مثل الفدرة (tahdhib)؛ الوذر بضع اللحم (tahdhib)؛ الوذرة قطعة من اللحم (mufradat)؛ ثريدة كثيرة الوذر (tahdhib)
- **B002** eti parçalama veya yarayı çizerek açma — eti parçalama veya yarayı çizerek açma · eti parçalara ayırmak · yarayı çizerek açmak · et parçasını küçük parçalara bölmek
  التوذير أن يشرط الجرح (maqayis)؛ وذرت اللحم توذيرا قطعته وكذلك الجرح إذا شرطته (sihah)؛ وقد وذرت الوذرة أذرها وذرا إذا بضعتها بضعا (tahdhib)
- **B003** bir şeyi bırakmak — bir şeyi bırakmak · önemsiz gördüğü şeyi bir yana atmak · bunu bırak · onu bırakmak
  ذر ذا (maqayis)؛ أماتت المصدر من يذر والفعل الماضي واستعملته في الحاضر والأمر (ayn)؛ ذره أي دعه وهو يذره (sihah)؛ ذرذا ودع ذا ولا يقال وذرته (tahdhib)؛ يذر الشيء أي يقذفه لقلة اعتداده به (mufradat)
- **B004** cinsel göndermeli ağır soy sövgüsü; ad biçiminde klitoris — cinsel organ göndermeli ağır bir soy sövgüsü · ağır bir soy sövgüsü · klitoris
  يا ابن شامة الوذر (maqayis;ayn;sihah;tahdhib)؛ كلمة قذف (sihah)؛ كلمة معناها القذف (tahdhib)؛ عرض لها بأعضاء الرجال (maqayis)؛ أراد المذاكير (tahdhib)؛ أرادوا بها القلف (tahdhib)؛ الوذفة والوذرة بظارة المرأة (tahdhib)

## و د د (root_001634): 71:23 وَدًّا

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

## س و ع (root_000760): 71:23 سُوَاعًا

- **B001** zamanın sürmesi ve belirli bir zaman kesiti — şimdiki zaman ya da gece ve gündüzden bir bölüm · dünyanın sona erip insanların yeniden dirileceği gün · zaman bölümleri · kısacık bir zaman · gecenin sakinleşmesinden bir süre sonra · gecenin sakinleşmesinden bir süre sonra · zaman dilimi başına işlem yapma · bir çalışanı zaman dilimi başına tutmak · çetin bir zaman kesiti
  استمرار الشيء ومضيه (maqayis)؛ الساعة سميت بذلك (maqayis)؛ الساعة الوقت الحاضر (sihah)؛ الساعة القيامة (ayn;sihah;tahdhib)؛ الساعة جزء من آخر الليل والنهار (tahdhib)؛ جاءنا بعد سوع من الليل وبعد سواع (maqayis;sihah;tahdhib)؛ عاملته مساوعة (maqayis;sihah)؛ ساوعت الأجير إذا استأجرته ساعة بعد ساعة (tahdhib)؛ ساعة سوعاء أي شديدة (sihah)
- **B002** gözetimsiz bırakıp başıboş gitmesine yol açma — develeri kendi yönlerine gidecek biçimde gözetimsiz bırakmak · bir şeyi kaybetmek · gözetimsiz kaldığı için kendi yönüne gitmek · başıboş gitmek veya yavrusunu gözetimsiz bırakmak · kaybolmuş ve gözetimsiz kalmış · otlakta kendi başına uzaklaşan dişi deve · yavrusunu yırtıcıya açık biçimde bırakan dişi deve · malını savuran adam · malı savuran kişi
  أسعت الإبل إساعة إذا أهملتها (maqayis;sihah;tahdhib)؛ ساعت فهي تسوع (maqayis;sihah;tahdhib)؛ ضائع سائع (maqayis;sihah;tahdhib)؛ ناقة مسياع تذهب في المرعى (maqayis;sihah;tahdhib)؛ رجل مسياع مضياع للمال (sihah;tahdhib)؛ ناقة مسياع تدع ولدها حتى يأكله السبع (tahdhib)
- **B003** eski anlatılarda geçen belirli bir putun özel adı — eski anlatılarda tapınılan belirli bir putun özel adı
  سواع اسم صنم في زمن نوح (ayn;tahdhib)؛ سواع اسم صنم كان لقوم نوح ثم صار لهذيل (sihah)
- **B004** saman karıştırılmış çamur — saman karıştırılmış çamur
  السياع الطين فيه التبن (maqayis)
- **B005** boşalma öncesi salgı — boşalma öncesi salgı · boşalmadan önce çıkan salgı · boşalma öncesi salgıyla ilgilenme buyruğu
  السواعي مأخوذ من السواع وهو المذي وهو السوعاء (tahdhib)؛ السوعاء المذي الذي يخرج قبل النطفة (tahdhib)؛ سع سع إذا أمرته أن يتعهد سوعاءه (tahdhib)
- **B006** ölüp yok olanlar — ölüp yok olmuş kimseler
  الساعة الهلكى (tahdhib)

## ن س ر (root_001496): 71:23 وَنَسْرًا

- **B001** kapıp almak, gagayla didiklemek ya da azar azar almak — kapıp almak; gagayla didiklemek; azar azar almak
  أصل صحيح يدل على اختلاس واستلاب؛ ونسره كأنه شيء يسير استلبه (maqayis); النسر نتف اللحم بالمنقار (ayn;tahdhib); النسر: نتف البازي اللحم بمنسره (sihah); مصدر: نسر الطائر الشيء بمنسره؛ ونسرت كذا: تناولته قليلا قليلا (mufradat)
- **B002** kartal; kartal gibi güçlenme — kartal · güçsüz kuşun kartal gibi güçlenmesi · kartala benzetilen bir yırtıcı kuş adı
  ومنه النسر كأنه ينسر الشيء (maqayis); النسر طائر معروف (ayn;tahdhib); النسر: طائر (sihah); والنسر: طائر (mufradat); استنسر البغاث إذا صار كالنسر (sihah)
- **B003** kartal adıyla anılan put — kartal adıyla anılan put
  نسر: صنم كان لذي الكلاع...من أصنام قوم نوح (sihah); نسر: اسم صنم في قوله تعالى ونسرا (mufradat)
- **B004** yırtıcı kuş gagası — yırtıcı kuş gagası
  منقار البازي ونحوه منسر (ayn;tahdhib); المنسر بكسر الميم لسباع الطير بمنزلة المنقار لغيرها (sihah); نسر الطائر الشيء بمنسره (mufradat)
- **B005** ordunun önünde ilerleyen atlı birlik — ordunun önünde ilerleyen atlı birlik
  المنسر خيل ما بين المائة إلى المائتين...لينسر شيئا أي يختطفه ويستلبه (maqayis); المنسر ما بين المائة إلى المائتين ويقال ما بين الثلاثين إلى الأربعين (ayn); المنسر قطعة من الجيش تمر أمام الجيش الكبير (sihah); المنسر ما بين الثلاثين إلى الأربعين من الخيل؛ من الثلاثة إلى العشرة (tahdhib)
- **B006** uçan ve konmuş kartal adlı iki yıldız — kartal adı verilen iki yıldız · uçan kartal adlı yıldız · konmuş kartal adlı yıldız
  النسر كواكب في السماء النسر الطائر والنسر الواقع (maqayis); النسران نجمان في السماء...الواقع...الطائر (ayn;tahdhib); في النجوم النسر الطائر والنسر الواقع (sihah); النسران نجمان طائر وواقع (mufradat)
- **B007** toynak tabanındaki sert et çıkıntısı [kalıp] — toynak tabanındaki sert ve çıkıntılı et parçası
  نسر الحافر ما في بطنه كأنه النوى والحصى (maqayis); نسر الحافر لحمة يابسة...بالنوى (ayn); لحمة يابسة في بطن الحافر كأنها نواة أو حصاة (sihah); نسر الحافر لحمة...والنسور الشواخص اللواتي في بطن الحافر (tahdhib); نسر الحافر لحمة ناتئة تشبيها به (mufradat)
- **B008** kapkaççı hırsız — kapkaççı hırsız
  والمنسر اللص (ayn)
- **B009** sürekli akıntılı anormal kanal — içi bozulmuş, sürekli akıntılı anormal damar ya da kanal
  الناسور في العربية العرق الغبر (ayn); الناسور بالسين والصاد جميعا علة تحدث...وهو معرب (sihah); الناسور بالسن والصاد عرق غبر...في باطنه فساد (tahdhib)
- **B010** kokulu bir gül ya da bitki türü — kokulu bir gül ya da hoş kokulu bitki türü
  النسرين من الرياحين ترجمة الفارسية (ayn); نسرين الورد معروف ولا أدري أعربي أم لا (tahdhib)
- **B011** bir su yerinin ve ona bağlı günün adı — bir su yerinin ve ondan adını alan tarihsel günün adı
  النسار بكسر النون ماء لبني عامر ومنه يوم النسار (sihah)

## ض ل ل (root_000913): 71:24 أَضَلُّوا۟, 71:24 ضَلَٰلًا, 71:27 يُضِلُّوا۟

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

## ك ث ر (root_001286): 71:24 كَثِيرًا

- **B001** çokluk ve sayıca artma — çokluk; sayının artması ve azlığın karşıtı · bir şey çoğaldı, sayısı arttı · çok, sayıca fazla · bir şeyi çoğaltmak · bir şeyden çokça edinmek veya onu çok saymak · malın ya da durumun azı ve çoğu · pek çok, çok büyük sayıda
  الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)
- **B002** çokluk yarışı ve çoklukla üstün gelme — onlarla çokluk yarışına girdik ve onları sayıca geçtik · mal, sayı veya güç bakımından çokluk yarışı ve övünme · çokluk yarışında yenilmiş
  كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)
- **B003** kişiye bağlı çokluk nitelemeleri [kalıp] — malı çok kişi · çok konuşan kadın veya erkek · iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi · başkasının malıyla kendini varlıklı göstermek
  رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)
- **B004** özel ırmak veya bol iyilik — cennetteki özel ırmak · bol veya büyük iyilik · iyiliği ve bağışı bol, cömert önder
  الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)
- **B005** kabarıp yükselen yoğun toz — kabarıp yükselen yoğun toz · son derece çoğalmak
  الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)
- **B006** hurma ağacının iç göbeği — hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü · meyve veya hurma göbeği için el kesme cezası yoktur · hurma ağacı çiçek sürgünü verdi
  الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)
- **B007** bir araya toplanma — bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir
  الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)

## ظ ل م (root_000967): 71:24 ٱلظَّٰلِمِينَ, 71:28 ٱلظَّٰلِمِينَ

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

## خ ط ء (root_000420): 71:25 خَطِيٓـَٰٔتِهِمْ

- **B001** istemeden doğruyu tutturamama — istemeden yapılan yanlış; doğruyu tutturamama · yanılmak; doğruyu tutturamamak · yanılmak; amaçlanan sonucu elde edememek · yanılmak; yanlış yapmak · doğruyu amaçlayıp yanılan kimse · yanlış yaptığını söylemek; yanlış bulmak · ıskalamak; değmemek · kötülük senden uzak olsun · çok yanılan da bazen doğruyu bulur
  أخطأ إذا لم يصب الصواب؛ الخطأ ما لم يتعمد؛ خطأته تخطئة (ayn)؛ الخطأ نقيض الصواب؛ المخطئ من أراد الصواب فصار إلى غيره؛ خطأته تخطئة وتخطيئا (sihah)؛ أخطأ إذا لم يصب الصواب؛ أخطأت لما صنعه خطأ غير عمد؛ خطىء عنك السوء إذا دعوا له أن يدفع عنه السوء (tahdhib)؛ الخطأ العدول عن الجهة؛ يقع منه خلاف ما يريد؛ أصاب الخطأ وأخطأ الصواب (mufradat)؛ الخطاء مجاوزة حد الصواب؛ أخطأ إذا تعدى الصواب (maqayis)
- **B002** bilerek işlenen günah — sorumluluk doğuran günah · günah; suç · günah işlemek · hesabı sorulan günah veya kötü eylem · günahı bilerek işleyen kimse; günahkâr · büyük günah · günahlar · ne büyük günah işledi!
  الخطء الذنب؛ خطئ يخطأ خطأ وخطأة؛ الخطيئة (sihah)؛ خطئت إذا أثمت؛ خاطئين أي آثمين؛ خطئت لما صنعه عمدا وهو الذنب؛ الخطيئة الذنب على عمد (tahdhib)؛ الخطأ التام المأخوذ به الإنسان؛ الخطيئة والسيئة يتقاربان؛ الخاطئ هو القاصد للذنب؛ الذنب العظيم (mufradat)؛ خطئ يخطأ إذا أذنب (maqayis)
- **B003** yağmurun atladığı arazi — yağmurun atladığı arazi · iki yağışlı arazi arasında yağışsız kalan yer · oraya yağmur yağmasın
  الخطيئة أرض يخطئها المطر ويصيب غيرها (ayn)؛ الأرض الخطيطة هي التي لم تمطر بين أرضين ممطورتين؛ من أخطأ كأن المطر أخطأها؛ خطأ الله نوءها (maqayis)

## غ ر ق (root_001080): 71:25 أُغْرِقُوا۟

- **B001** suda batıp boğulma veya boğma; bunaltıcı bir şey içinde kalma — suda boğulmak; borç, bela veya nimet içinde kalmak · boğulan kimse; borç ya da belanın bastırdığı kimse · suda boğulmakta olan · birini suda boğmak · boğulmak üzere olanın çaresiz yakarışı
  الغرق في الماء (maqayis); رجل غرق وغريق رسب في الماء وابتلي بالدين والبلوى تشبيها به (ayn); غرق في الماء غرقا وأغرقه غيره (sihah); الغرق الرسوب في الماء ويشبه به الذي ركبه الدين وغمرته البلايا (tahdhib); الغرق الرسوب في الماء وفي البلاء وفلان غرق في نعمة فلان تشبيها بذلك (mufradat)
- **B002** sıvıyla boğarak öldürme ve bunun genelleşmiş öldürme kullanımı — sıvıda boğarak öldürme; genel olarak öldürme · ebenin doğum sıvısını bebeğin burnuna kaçırarak onu öldürmesi
  والتغريق القتل وغرقته القابلة في ماء السلا ثم تخرجه ميتا (ayn); والتغريق القتل وكانت تغرق المولود في ماء السلى حتى يموت ثم جعل كل قتل تغريقا (sihah); غرقت القابلة الولد وذلك إذا لم ترفق بالمولود حتى تدخل السابياء أنفه فتقتله (tahdhib)
- **B003** gözün yaşla, toprağın suyla dolması — suya doymuş toprak · gözlerin yaşla dolması, fakat yaşların dışarı taşmaması
  والغرقة أرض تكون في غاية الري وأغرورقت العين والأرض (maqayis); اغرورقت عيناه دمعتا (sihah); وأغرورقت عيناه إذا امتلأتا دموعا ولم تفيضاها (tahdhib)
- **B004** yayı son sınırına kadar çekme [kalıp] — yayı veya oku son çekiş sınırına kadar germek · oku atmak için yayı son sınırına kadar çekmek; aşırılığa varmak
  أغرقت في القوس مددتها غاية المد (maqayis); أغرقت النبل وغرقته بلغت به غاية المد في القوس (ayn); أغرق النازع في القوس أي استوفى مدها (sihah); الإغراق في النزع أن ينزع حتى يشرب بالرصاف (tahdhib)
- **B005** bir alanı tümüyle kapsama; sürüye karışıp öne geçme — atların arasına karışıp sonra hepsini geçmek · bütünüyle kapsama ve hiçbir bölümü dışarıda bırakmama · nefesi verirken soluk kapasitesini sonuna kadar kullanma · insanların bütün bakışlarını kendine çekmek · hayvanın iri gövdesinin göğüs ve karın kayışlarını doldurup dar bırakması
  اغترق الفرس في الخيل إذا خالطها ثم سبقها (maqayis); الفرس إذا خالط الخيل ثم سبقها يقال اغترقها (ayn); الاستغراق الاستيعاب واغتراق النفس استيعابه في الزفير (sihah); فلانة تغترق نظر الناس وقد اغترق التصدير والبطان واستغرقه (tahdhib)
- **B006** bir içimlik süt ya da başka içecek — bir içimlik veya küçük bir kap kadar süt ya da başka içecek
  الغرقة من اللبن قدر ثلث الإناء والجمع غرق (maqayis); الغرقة القليل من اللبن قدر قدح أو أقل (ayn); الغرقة بالضم مثل الشربة من اللبن وغيره والجمع غرق (sihah); الغرقة مثل الشربة من اللبن وغيره من الأشربة وجمعها غرق (tahdhib)
- **B007** yumurtanın iç kabuğu ya da yenilen beyazı — yumurtanın iç kabuğu veya yenilen beyaz kısmı
  الغرقىء قشرة البيض الداخلة (ayn); الغرقيء البياض الذي يؤكل واتفق النحويون على همز الغرقيء وأن همزته ليست بأصلية (tahdhib)
- **B008** baştan başa süslenmiş gem [kalıp] — baştan başa süslenmiş veya gümüşle kaplanmış gem
  لجام مغرق بالفضة أي محلى (sihah); لجام مغرق إذا عمته الحلية (tahdhib)

## د خ ل (root_000464): 71:25 فَأُدْخِلُوا۟, 71:28 دَخَلَ

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

## و ج د (root_001626): 71:25 يَجِدُوا۟

- **B001** bulma ve duyusal ya da zihinsel olarak algılama — bir şeyi bulmak veya ona erişmek · yitiği bulmak · bulma ve erişme · birini aradığı şeye ulaştırmak · duyularla veya akılla algılama · onları gördüğünüz veya kendilerine eriştiğiniz yerde
  الشيء يلفيه (maqayis)؛ وجدت الضالة وجدانا (maqayis;sihah)؛ الوجدان والجدة من قولك وجدت الشيء أي أصبته (ayn)؛ وجدت الشيء أجده وجدانا (jamhara)؛ وجد مطلوبه يجده وجودا (sihah)؛ الوجود أضرب: وجود بإحدى الحواس الخمس ... ووجود بالعقل (mufradat)؛ حيث وجدتموهم أي حيث رأيتموهم (mufradat)
- **B002** varlığa gelme, var olma ve var etme — yokluktan sonra varlığa gelmek · var olan, mevcut · Tanrı onu var etti · var olan şeyler
  وجد الشيء عن عدم فهو موجود (sihah)؛ أوجده الله (sihah)؛ الموجودات ثلاثة أضرب (mufradat)
- **B003** varlıklı veya yeterli olmak; varlıklı ya da güçlü kılmak — maddi genişlik ve varlıklılık · malca genişleyip varlıklı olmak · varlıklı ve ödeme gücü bulunan kimse · onu varlıklı kılmak · onu zayıflıktan sonra güçlendirmek · imkanınız ve maddi gücünüz ölçüsünde · suya ulaşmaya gücünüz yetmediyse
  الوجدان والجدة من قولك وجدت الشيء أي أصبته (ayn)؛ وجدت في المال جدة ووجدا ووجدا؛ الواجد الغني (jamhara)؛ وجد في المال وجدا ووجدا وجدة أي استغنى؛ أوجده أي أغناه؛ آجدني بعد ضعف أي قواني (sihah)؛ يعبر عن التمكن من الشيء بالوجود؛ من وجدكم أي تمكنكم وقدر غناكم (mufradat)
- **B004** üzüntü veya sevgi duymak; güçlü isteğin doyumunu yaşamak — üzüntü ve keder · sevgi ve duygusal bağlılık · ona sevgi duymak · üzüntü duymak · bir kimse için üzülmek · güçlü iştahla doyuma erişmek
  الوجد من الخزن (ayn)؛ الوجد: الحب؛ وجدت به أجد وجدا (jamhara)؛ وجد في الحزن وجدا؛ توجدت لفلان أي حزنت له (sihah)؛ وجود بقوة الشهوة؛ يعبر عن الحزن والحب بالوجد (mufradat)
- **B005** öfke duymak ve birine kızmak — öfke ve kızgınlık · öfkeye kapılmak · o kişiye kızmak · öfke bağlamındaki kızgınlık duygusu
  وجدت في الغضب وجدانا (maqayis)؛ الموجدة من الغضب (ayn)؛ وجدت على الرجل موجدة (jamhara)؛ وجد عليه في الغضب موجدة ووجدانا (sihah)؛ يعبر عن الغضب بالموجدة (mufradat)

## ECHO ج د د (root_000227): for 71:25 يَجِدُوا۟: withheld observed target; not identity

- **B001** değer ve konum yüceliği — büyüklük, yücelik ve yüksek değer
  العظمة (maqayis)؛ جد ربنا عظمته (ayn)؛ تعالى جد ربنا أي عظمة ربنا؛ جد في عيني أي عظم (sihah)؛ جد ربنا جلال ربنا؛ جل قدره وعظم (tahdhib)؛ جد ربنا أي فيضه وقيل عظمته (mufradat)
- **B002** iyi yazgı ve varlık payı — iyi yazgı, dünyalık pay ve varlık · iyi yazgı veya varlık sahibi
  الغني والحظ؛ لا ينفع ذا الجد منك الجد (maqayis)؛ جد الرجل بخته (ayn)؛ الجد الحظ والبخت؛ لا ينفع ذا الجد منك الجد أي لا ينفع ذا الغنى (sihah)؛ الجد الغنى والحظ في الرزق؛ صاعد الجد؛ رجل جديد إذا كان ذا حظ (tahdhib)؛ الحظوظ الدنيوية جدا وهو البخت (mufradat)
- **B003** kesme ve ayırma — bir şeyi kesmek · kesilmiş · hurma ağaçlarının ürününü kesip toplamak · hurma ürününü kesip toplama ve bunun vakti · dişi devenin meme uçlarını bağ yüzünden kesip zedelemek · birine annesinden kopması için ilenmek · kulağı kesik koyun · ekildiğinde yüz ölçek ürün veren tarla
  جددت الشيء جدا وهو مجدود وجديد أي مقطوع؛ الجداد صرام النخل (maqayis)؛ جداد النخل صرامه؛ جد ثدي أمك اذدعي عليه بالقطيعة (ayn)؛ جددت الشيء أجده جدا قطعته؛ جد النخل أي صرمه؛ جدت أخلاف الناقة (sihah)؛ جد التمرة؛ الجداد الصرام؛ أصل الجد القطع؛ جد ثدي أمه (tahdhib)؛ جددت الثوب إذا قطعته؛ جد ثدي أمه على طريق الشتم (mufradat)
- **B004** yeni olma ve yenilenme — yeni, eskimemiş veya yenilenmiş · gece ile gündüz · yenilik ve yeni olma
  ثوب جديد؛ سمي كل شيء لم تأت عليه الأيام جديدا؛ الليل والنهار الجديدين والأجدين (maqayis)؛ الجدة مصدر الجديد؛ الجديدان الليل والنهار (ayn)؛ صار جديدا؛ تجدد الشيء صار جديدا؛ الجديدان والأجدان الليل والنهار (sihah)؛ ثوب جديد جد حديثا أي قطع؛ الجدة مصدر الجديد؛ الجديدان والأجدان الليل والنهار (tahdhib)؛ ثوب جديد أصله المقطوع؛ جعل لكل ما أحدث إنشاؤه؛ الجديدان والأجدان (mufradat)
- **B005** belirgin şerit veya ana yol — çevresinden ayrılan yol veya çizgi · dağlardaki farklı renkli şeritler · yolun ortası veya en çok kullanılan ana bölümü · farklı çizgiler taşıyan dokuma
  كل جدة طريقة؛ جادة الطريق سواؤه (maqayis)؛ الجدد والجديد وجه الأرض؛ الزم الطريق الجدد؛ الجادة الطريق (ayn)؛ الجدة الخطة؛ كل خط جدة؛ جدد بيض أي طرائق تخالف لون الجبل (jamhara)؛ الجدة الطريقة؛ جادة الطريق؛ كساء مجدد فيه خطوط مختلفة (sihah)؛ الجدد الخطط والطرق تكون في الجبال؛ كل طريقة جدة وجادة؛ كساء مجدد فيه خيوط مختلفة (tahdhib)؛ جدد بيض جمع جدة أي طريقة ظاهرة؛ جادة الطريق (mufradat)
- **B006** su kıyısı — ırmak veya dere yatağı kıyısı · deniz kıyısı; ayrıca kıyıdaki belirli yer
  جدة النهر أي ما قرب من الأرض؛ الجدة ساحل البحر بمكة (ayn)؛ جدة النهر حافته وكذلك الوادي (jamhara)؛ جدة بلد على الساحل (sihah)؛ الجدة شاطىء النهر؛ الجدة ساحل البحر بحذاء مكة (tahdhib)
- **B007** düz ve sert yer yüzeyi — düz veya sert yer · düz ve pürüzsüz yer · yerin yüzü · tümseksiz ve geçişi kolay düz yol
  الجدجد الأرض المستوية؛ الجدد مثل الجدجد؛ الجديد وجه الأرض (maqayis)؛ الجدد والجديد وجه الأرض؛ الجدجد الفيف الأملس (ayn)؛ الجدد الأرض الصلبة؛ الجدجد الأرض الصلبة المستوية (sihah)؛ الأرض المستوية التي ليس فيها رمل ولا اختلاف جدد؛ جديد الأرض وجهها (tahdhib)؛ قطع الأرض المستوية؛ طريق مجدود (mufradat)
- **B008** şakadan uzak kararlı çaba — şaka olmayan gerçek ve kararlı tutum · bir işe var gücüyle sarılıp kararlılıkla uğraşmak · bir işte bütün gücünü ortaya koymak · gerçekten mi, kesin kararın bu mu · işine var gücüyle sarılan kimse · bir işte haklılık çekişmesine girmek
  الجد في الأمر والمبالغة فيه؛ أجدك تفعل كذا أي أجدا منك أصريمة منك أعزيمة منك (maqayis)؛ الجد نقيض الهزل؛ جد فلان في أمره وسيره (ayn)؛ الجد نقيض الهزل؛ الجد الاجتهاد في الأمور؛ جاد مجد (sihah)؛ الجد إنما هو الاجتهاد في العمل؛ أجد الرجل في أمره؛ جاد مجد؛ جد فلان في أمره إذا كان ذا حقيقة ومضاء (tahdhib)؛ جد في سيره؛ جد في أمره (mufradat)
- **B009** büyükanne ve büyükbaba — anne veya baba tarafından büyükbaba · anne veya baba tarafından büyükanne
  الجد أبو الأب وأبو الأم (sihah)؛ الجد أب الأب؛ أم الأم وأم الأب يقال لها جدة (tahdhib)؛ الجد أبو الأب وأبو الأم (mufradat)
- **B010** otlak kuyusu — bol ot bulunan yerdeki kuyu
  الجد البئر؛ البئر تقطع لها الأرض قطعا (maqayis)؛ الجد البئر تكون في موضع الكلأ (ayn)؛ الجد بالضم البئر التي تكون في موضع كثير الكلا (sihah)؛ الجد بلا هاء البئر الجيدة الموضع من الكلأ (tahdhib)
- **B011** susuz yer veya sütü kesilmiş dişi hayvan — susuz ve kuru kır · sütü azalmış veya kesilmiş dişi hayvan · sütü kesilmiş, memesi kurumuş dişi hayvan
  الجداء الأرض التي لا ماء بها؛ الجدود والجداء من الضان التي جف لبنها ويبس ضرعها (maqayis)؛ الجدود كل أنثى يبس لبنها؛ الجداء مفازة يابسة؛ شاة جداء يابسة اللبن (ayn)؛ فلاة جداء لا ماء بها؛ الجدود النعجة التي قل لبنها؛ الجداء التي ذهب لبنها (sihah)؛ ناقة جدود؛ نعجة جدود؛ الجداء الناقة التي قد انقطع لبنها (tahdhib)؛ الجدود والجداء من الضأن التي انقطع لبنها (mufradat)
- **B012** düğümlü ipler ve dolaşık kalıntılar — çadır ipleri; dolaşmış ip ve dallar; eskimiş kumaş parçaları
  جدادها الخيوط التي تعقد بالخيمة؛ جداد الخيمة الخيوط؛ الجداد صغار الشجر (maqayis)؛ الجداد الخلقان من الثياب؛ كل شيء تعقد بعضه في بعض من الخيوط وأغصان الشجر فهو جداد (sihah)؛ الجداد خيوط المظلة؛ الجداد بالنبطية الخيوط المعقدة (tahdhib)
- **B013** cırcır böceği — cırcır böceği
  الجدجد دويبة على خلقة الجندب (ayn)؛ الجدجد صرار الليل وفيه شبه من الجراد (sihah)
- **B014** kıyı ve kır yer adları — kıyıda bulunan bir yerin adı · çölde veya su bulunan yerdeki bir yerin adı
  جدة موضع؛ جدود موضع بالبادية (ayn)؛ جدة بلد على الساحل؛ جدود موضع فيه ماء (sihah)

## د و ن (root_000502): 71:25 دُونِ

- **B001** yakın, aşağı ya da hedefin gerisinde olma — yakın; altında; hedefin gerisinde · bu, ötekinden daha yakındır · yaklaş
  أصل واحد يدل على المداناة والمقاربة (maqayis)؛ دون نقيض فوق وهو تقصير عن الغاية (sihah)؛ أدن دونك أي اقترب (tahdhib)؛ يقال للقاصر عن الشيء دون (mufradat)
- **B002** değersiz, önemsiz veya aşağı olma — değersiz, aşağılık ve önemsiz · küçümseme bildiren küçültülmüş biçim · aşağılık, bayağı · değeri yakın ya da düşük sayılan iş veya kumaş
  إذا أردت تحقيره قلت دوين والشيء الدون أي الهين (maqayis)؛ الدون الحقير الخسيس (sihah)؛ الأدون الدنيء (mufradat)
- **B003** başkası ya da daha aşağıda olan [kalıp] — sizin düzeyinize ulaşmamış olanlar · bundan daha azı veya bunun dışındakiler · Tanrı'dan başkası ya da O'na ulaşmak için aracı sayılan şey · ondan başkası veya onun buyruğu dışında olan
  ممن لم يبلغ منزلته منزلتكم؛ ما كان أقل من ذلك وقيل ما سوى ذلك؛ من دون الله أي غير الله
- **B004** buyur, bunu al — buyur, bunu al
  في الإغراء دونكه أي خذه أقرب منه وقربه منك (maqayis)؛ في الاغراء بالشئ دونكه ودونكموه (sihah)؛ يغرى بلفظ دون فيقال دونك كذا أي تناوله (mufradat)
- **B005** kayıt defteri ve kayıtları düzenleme — kayıt defteri veya kayıtların tutulduğu yer · kayıtları yazıya geçirip düzenledim
  الديوان أصله دوان فعوض من إحدى الواوين لأنه يجمع على دواوين؛ وقد دونت الدواوين
- **B006** zayıflamak (aktarımı tartışmalı) — 
  دان يدون دونا إذا ضعف (maqayis;mufradat)؛ يروى لم يدن وغيره يرويه لم يدن بتشديد النون من دنى يدنى أي ضعف (sihah)

## ن ص ر (root_001510): 71:25 أَنصَارًا

- **B001** yardım edip üstün gelmesini sağlama — yardım etti ve düşmana karşı üstün gelmesini sağladı · yardım, destek · iyi ve etkili yardım · yardımcı, destekçi · yardımcı, destekçi · yardımcılar, destekçiler · düşmanına karşı kendisine yardım etmesini istedi · birbirlerine yardım ettiler, dayanıştılar
  النصر والنصرة العون (mufradat)؛ عون المظلوم (ayn;tahdhib)؛ نصره الله على عدوه ينصره نصرا (sihah)؛ آتاهم الظفر على عدوهم (maqayis)؛ النصير الناصر (ayn;sihah;tahdhib)؛ التناصر التعاون (mufradat)
- **B002** zulmedene karşı koyup hakkını alma — zulmeden kişiden hakkını aldı, öcünü aldı
  انتصر انتقم وهو منه (maqayis)؛ انتصر الرجل انتقم من ظالمه (ayn)؛ وانتصر منه انتقم (sihah)؛ انتصر الرجل إذا امتنع من ظالمه (tahdhib)؛ الانتصاف والانتقام منه (tahdhib)؛ إذا أصابهم البغي هم ينتصرون (mufradat)
- **B003** bir ülkeye veya toprağa gelmek [kalıp] — belirtilen ülkeye veya toprağa geldim
  نصرت بلد كذا إذا أتيته (maqayis)؛ نصرت أرض بني فلان أي أتيتها (tahdhib)
- **B004** toprağı sulayıp yeşerten, insanları ferahlatan yağmur — yağmur · eksiksiz ve doyurucu yağmur · yağmur ülkeyi suladı veya yeşertti · toprağa yağmur yağdı · halk yağmura kavuşup rahatladı
  يسمى المطر نصرا (maqayis)؛ نصر الغيث البلاد أرواها (ayn)؛ نصر الغيث الأرض أي غاثها (sihah)؛ النصرة المطرة التامة (tahdhib)؛ نصر الغيث البلاد إذا أنبتها (tahdhib)؛ نصر القوم إذا أغيثوا (tahdhib)
- **B005** iyilik veya armağan verme — armağan, veriş
  النصر العطاء (maqayis;sihah)؛ أصل صحيح يدل على إتيان خير وإيتائه (maqayis)
- **B006** Hristiyanlık ve Hristiyan olma ya da yapma — Hristiyan oldu, Hristiyanlığı benimsedi · onu Hristiyan yaptı · Hristiyan erkek, Hristiyan · Hristiyan kadın · Hristiyanlar
  تنصر دخل في النصرانية (ayn;tahdhib)؛ نصره جعله نصرانيا (sihah)؛ رجل نصراني وامرأة نصرانية (sihah)؛ النصارى قيل سموا بذلك لقوله كونوا أنصار الله (mufradat)؛ انتسابا إلى قرية يقال لها نصرانة (mufradat)
- **B007** uzaktan gelip su toplanma yerine ulaşan su yatağı — uzaktan gelip su toplanma yerine ulaşan su yatakları · bu tür su yatağı için olası tekil ad · bu tür su yatağı için diğer olası tekil ad
  النواصر من الشعاب ما جاء من مكان بعيد إلى الوادي؛ النواصر مسايل المياه واحدها ناصرة؛ تجيء من مكان بعيد حتى تقع في مجتمع الماء

## ك ف ر (root_001307): 71:26 ٱلْكَٰفِرِينَ, 71:27 كَفَّارًا

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

## ف ج ر (root_001132): 71:27 فَاجِرًا

- **B001** genişçe yarılma ve içinden suyun akıp çıkması — suyu yarıp akıtma · su açılıp akmaya başladı · suyu yarıp dışarı akıttı · çokça açılıp fışkırdı · suyun açılıp çıktığı yer · suyun çıktığı ağız · suların ve vadilerin açılıp çıktığı alçak alan · vadinin su boşaltım ağızları · kum içindeki yol
  التفتح في الشيء (maqayis)؛ انفجر الماء انفجارا تفتح (maqayis)؛ الفجر تفجيرك الماء (ayn;tahdhib)؛ وانفجر الماء وغيره انفجارا إذا انبعث سائلا (jamhara)؛ فجرت الماء فانفجر أي بجسته فانبجس (sihah)؛ شق الشيء شقا واسعا (mufradat)؛ المفجر الموضع الذي ينفجر منه الماء (ayn;tahdhib)؛ الفجرة موضع تفتح الماء (maqayis;sihah)؛ مفاجر الوادي مرافضه (maqayis;sihah)
- **B002** sabah aydınlığının gece karanlığını yararak belirmesi — tan aydınlığı · ufka yayılan gerçek tan · dikey görünüp dağılan yalancı tan · tan vaktine girdik
  الفجر انفجار الظلمة عن الصبح (maqayis)؛ الفجر ضوء الصباح والفجر الصبح (ayn)؛ الفجر حمرة الشمس في سواد الليل وهما فجران (jamhara)؛ الفجر في آخر الليل كالشفق في أوله (sihah)؛ الفجر ضوء الصبح وقد انفجر الصبح (tahdhib)؛ قيل للصبح فجر لكونه فجر الليل (mufradat)
- **B003** kalabalığın ya da çok sayıda belanın ansızın üzerlerine gelmesi [kalıp] — kalabalık ansızın üzerlerine geldi · çok sayıda bela ansızın başlarına geldi
  انفجر عليهم القوم وانفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة (ayn)؛ انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغته (tahdhib)
- **B004** doğruluk sınırını çiğneyerek kötülüğe sapma — taşkın kötülük, başkaldırı ve yalan · doğru yoldan sapıp kötülüklere daldı · yalan söyledi · yalan söyledi, cinsel sınırı çiğnedi ya da inancı reddetti · doğru yoldan sapmış kimse · terkin oturma yeri yana yatıktır · kötülük, kuşku ve yalan · ey doğru yoldan sapmış kadın · sana yalan söyleyen, karşı gelen ya da sözünden çıkan kişi
  الانبعاث والتفتح في المعاصي فجورا (maqayis)؛ سمي الكذب فجورا (maqayis)؛ كل مائل عن الحق فاجر (maqayis)؛ الفجور الريبة والكذب (ayn;tahdhib)؛ انبعاثه في المعاصي (jamhara)؛ فجر فجورا أي فسق وفجر أي كذب وأصله الميل (sihah)؛ الفجور شق ستر الديانة (mufradat)؛ سمي الكاذب فاجرا لكون الكذب بعض الفجور (mufradat)؛ أفجر إذا كذب وأفجر إذا عصى بفرجه وأفجر إذا كفر (tahdhib)
- **B005** taşarcasına bol iyilik ve eli açıklık — bol iyilik ve eli açıklık · iyiliği ve yardımı · iyiliği taşarcasına bol kimse · iyiliğin taşıp yayılması · çokça varlık getirdi
  الفجر وهو الكرم والتفجر بالخير (maqayis)؛ وما أكثر فجره أي معروفه (ayn)؛ رجل ذو فجر إذا كان يتفجر بالخير (jamhara)؛ الفجر الكرم والتفجر في الخير (sihah)؛ الفجر الجود الواسع والكرم (tahdhib)؛ أفجر الرجل إذا جاء بالفجر وهو المال الكثير (tahdhib)
- **B006** dokunulmazlığın çiğnenmesiyle adlandırılan belirli savaş günleri — dokunulmazlığın çiğnendiği belirli savaş günleri
  يوم الفجار يوم للعرب استحلت فيه الحرمة (maqayis)؛ انفجار من وقعات العرب بعكاظ (ayn)؛ أيام الفجار أربعة أفجرة (jamhara;sihah)؛ وإنما سمت قريش هذه الحرب فجارا لأنها كانت في الأشهر الحرم (sihah)؛ أيام الفجار أيام وقائع كانت بعكاظ واستحلوا الحرمات (tahdhib)؛ أيام الفجار وقائع اشتدت بين العرب (mufradat)

## ب ي ت (root_000166): 71:28 بَيْتِىَ

- **B001** barınak mesken — ev, mesken, barınak · gece kalınan yer · Tanri'nin evi veya eski ev diye anılan kutsal yer · orumcegin yuvası
  أصل واحد وهو المأوى والمآب ومجمع الشمل (maqayis)؛ البيت معروف (jamhara;sihah)؛ البيت سمي بيتا لأنه يبات فيه (tahdhib)؛ أصل البيت مأوى الإنسان بالليل (mufradat)
- **B002** hane halkı [kalıp] — ev halkı, haneye bağlı kimseler · erkeğin ailesi, hane halkı veya mecazen eşi
  البيت عيال الرجل والذين يبيت عندهم (maqayis)؛ امرأة الرجل بيته (jamhara;tahdhib)؛ أهل البيت (mufradat)؛ غير بيت من المسلمين إشارة إلى جماعة البيت (mufradat)
- **B003** şiir dizesi [kalıp] — ölçülü şiir dizesi
  لبيت الشعر بيت على التشبيه لأنه مجمع الألفاظ والحروف والمعاني (maqayis)؛ سمي البيت من الشعر بيتا لضمه الحروف والكلام (jamhara)؛ بيت شعر كتبه بالقلم (sihah)؛ كلام جمع منظوما (tahdhib)؛ الأبيات بالشعر (mufradat)
- **B004** geceleyin yapmak — geceleyin yapmak veya gece boyunca uğraşmak · bir işi gece tasarlamak veya planlamak · düşmana gece baskını yapmak · gece vakti geliş
  بيت الأمر إذا دبره ليلا (maqayis;sihah)؛ البيات والتبييت أن تأتي العدو ليلا (maqayis)؛ بيت القوم إذا أوقعت بهم ليلا (jamhara)؛ بات يفعل كذا إذا فعله ليلا (sihah)؛ كل ما فكر فيه أو خيض فيه بليل فقد بيت (tahdhib)؛ البيات والتبييت قصد العدو ليلا (mufradat)
- **B005** bir gecelik azık [kalıp] — bir gecelik yiyecek veya azık
  ما لفلان بيته ليلة أي ما يبيت عليه من طعام وغيره (maqayis)؛ ماله بيت ليلة وبيته ليلة أي قوت ليلة (sihah)؛ ما عند فلان بيت ليلة وبيتة ليلة أي ما عنده قوت ليلة (tahdhib)
- **B006** gece beklemiş şey [kalıp] — gece kapta beklemiş veya soğumuş su ya da sut · bayat haber, taze olmayan haber
  البيوت الماء الذي يبيت ليلا (maqayis)؛ ماء بيوت إذا بات ليلة في إنائه (jamhara)؛ خبر بائت وكذلك البيوت (sihah)؛ بيوت السقاء أي من لبن حلب ليلا وحقن في السقاء (tahdhib)؛ الماء إذا برد في المزادة ليلا بيوت (tahdhib)
- **B007** mezar evi [kalıp] — ev diye anılan mezar
  البيت القبر (jamhara)؛ وإنما أراد بالبيت القبر (tahdhib)
- **B008** soylu hane [kalıp] — kabilenin şerefi, soylu hanesi
  البيت من بيوتات العرب الذي يجمع شرف القبيلة (jamhara)؛ بيت العرب شرفها (tahdhib)؛ بيت تميم في بني حنظلة أي شرفها (tahdhib)
- **B009** bitişik komşu [kalıp] — ev eve bitişik komşum
  فلان جاري بيت بيت أي ملاصقا (sihah)؛ هو جاري يبت بيت وبيتا لبيت وبيت لبيت (tahdhib)
- **B010** evlenip zifafa girmek [kalıp] — erkeğin evlenmesi · eşi için ev kurup zifafa girmek
  بات الرجل يبيت بيتا إذا تزوج (tahdhib)؛ بنى فلان على امرأته بيتا إذا أعرس بها (tahdhib)

## ء م ن (root_000054): 71:28 مُؤْمِنًا, 71:28 وَلِلْمُؤْمِنِينَ, 71:28 وَٱلْمُؤْمِنَٰتِ

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ت ب ر (root_000174): 71:28 تَبَارًۢا

- **B001** yok edip boşa çıkarma — onu yok etti, boşa çıkardı ya da kırıp ufaladı · kırma ve yok etme · içinde bulundukları şey mahvolmuş ve boşa çıkmış durumdadır · yok oluş · yıkıp yok etme, kırıp parçalama · yok olmuş ya da eksilmiş
  تبر الله عمل الكافر أي أهلكه وأبطله (maqayis)؛ التبار الهلاك (jamhara;sihah)؛ تبره الله تتبيرا إذا أهلكه ومحقه (jamhara)؛ تبره تتبيرا أي كسره وأهلكه (sihah)؛ التتبير التدمير (tahdhib)؛ كل شيء كسرته وفتته فقد تبرته (tahdhib)؛ المتبور الهالك والمتبور الناقص (tahdhib)؛ التبر الكسر والإهلاك (mufradat)
- **B002** işlenmemiş değerli maden — işlenmemiş altın, gümüş veya başka değerli madde; kırık parça
  التبر ما كان من الذهب والفضة غير مصوغ (maqayis)؛ التبر الذهب (jamhara)؛ الذهب المستخرج من المعادن قبل أن يصاغ (jamhara)؛ التبر ما كان من الذهب غير مضروب فإذا ضرب دنانير فهو عين (sihah)؛ التبر الذهب والفضة قبل أن يصاغا (tahdhib)؛ التبر يقع على جميع جواهر الأرض قبل أن تصاغ (tahdhib)؛ مكسر الزجاج التبر وكذلك تبر الذهب (tahdhib)
- **B003** güzel renkli dişi deve — güzel renkli dişi deve
  التبراء الحسنة اللون من النوق



===== _commentary/v16/work/s071/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s071/reader_a_pilot.md)

# s071 Semantic Channel Discovery

## Parent Channels

### 1. [P1 71:1-14] The Summons Reaches a Closing Horizon
- Semantic invariant: A communicated danger is already in motion, while mercy opens a bounded interval before its arrival.
- Surface relation: direct; 71:1 anchors sending, warning, prior approach, arrival, punishment, and pain; 71:4 anchors the appointed term, delay, arrival, and knowledge.
- Surprising reach: The warning behaves at once like an approaching assailant, a maturing liability, and an account whose allotted share returns to its bearer.

#### Subchannel A. The herald runs ahead of the impact
- Reading type: surface-primary
- Scene or process: A messenger announces danger before an advancing event reaches the addressed community and inflicts pain.
- Active motifs: dispatched agent (`quranic:root_000563:B001/m01`); message-bearing envoy (`quranic:root_000563:B002/m01`); alarm that awakens caution (`quranic:root_001488:B001/m01`); temporal advance and approach (`quranic:root_001198:B002/m01`); coming and reaching (`quranic:root_000009:B001/m01`); arrival of calamity and destruction (`quranic:root_000009:B011/m01`); event coming into presence (`quranic:root_000281:B001/m01`); punitive affliction (`quranic:root_000994:B005/m01`); felt pain (`quranic:root_000046:B001/m01`); infliction of pain (`quranic:root_000046:B002/m01`).
- Ayah anchors: 71:1 (`ر س ل`, `ن ذ ر`, `ق ب ل`, `ء ت ي`, `ع ذ ب`, `ء ل م`); 71:4 (`ج ي ء`).
- Synthesis: The scene is not a static description of punishment. Dispatch and warning place a herald in front of something advancing; the arrival motifs let an event, command, enemy, illness, or destruction cross the remaining distance; and pain supplies its bodily outcome. The message is therefore an interception sent before impact.

#### Subchannel B. Reprieve stretches inside a fixed term
- Reading type: mixed
- Scene or process: A period is extended and deferred, but remains bounded by an appointed endpoint whose arrival cannot itself be moved.
- Active motifs: fixed term or maturity date (`quranic:root_000016:B001/m01`); postponement to a later time (`quranic:root_000019:B002/m01`); rear or terminal position (`quranic:root_000019:B003/m01`); deferral of an affair (`quranic:root_000548:B004/m01`); extended duration and respite (`quranic:root_001407:B004/m01`); temporal precedence (`quranic:root_001198:B002/m01`); limit reached or crossed (`quranic:root_000955:B003/m01`); event coming into presence (`quranic:root_000281:B001/m01`); knowledge as disclosed apprehension (`quranic:root_001040:B001/m01`).
- Ayah anchors: 71:4 (`ء ج ل`, `ء خ ر`, `ج ي ء`, `ع ل م`); 71:12 (`م د د`); 71:13 (`ر ج و`); 71:14 (`ط و ر`).
- Synthesis: Delay is modeled as added length within a measured span, not cancellation. The motifs distinguish the later position, the act of deferral, the duration being drawn out, and the terminal limit. Knowledge closes the mechanism: what is offered is time to recognize an endpoint, not an indefinitely movable horizon.

#### Subchannel C. Consequence returns as an allotted due
- Reading type: latent/lexical
- Scene or process: An offense creates a due share or binding obligation; its consequence returns to the actor unless forgiveness covers it.
- Active motifs: offense with an ominous outcome (`quranic:root_000521:B001/m01`); trailing end of a thing (`quranic:root_000521:B002/m01`); followers attached to a leader (`quranic:root_000521:B003/m01`); allotted share, especially of punishment (`quranic:root_000521:B006/m01`); full bucket as a measured allotment (`quranic:root_000521:B007/m01`); recompense returning to its worker (`quranic:root_000209:B002/m01`); self-imposed binding vow (`quranic:root_001488:B002/m01`); wound carrying a legally due compensation (`quranic:root_001488:B003/m01`); written guarantee and surety (`quranic:root_001198:B008/m01`); appointed maturity (`quranic:root_000016:B001/m01`); punitive affliction (`quranic:root_000994:B005/m01`); forgiveness that shields the offender from effect (`quranic:root_001096:B002/m01`).
- Ayah anchors: 71:1 (`ن ذ ر`, `ع ذ ب`, `ق ب ل`); 71:2 (`ن ذ ر`); 71:4 (`ء ج ل`, `ذ ن ب`, `غ ف ر`); 71:7 (`ث و ب`, `غ ف ر`); 71:10 (`غ ف ر`).
- Synthesis: The warning acquires the structure of a due account. Sin trails an act like a tail and gathers adherent consequences like followers; it can be an allotted bucket, warning can name a voluntarily or legally binding obligation, and recompense is what comes back from an act. Surety makes the liability transferable and enforceable, while forgiveness intervenes before its return by covering both fault and punitive effect.

### 2. [P1 71:1-14] The Message Changes Register Without Losing Its Aim
- Semantic invariant: One intelligible summons is carried, repeated, exposed, and concealed across different media and times.
- Surface relation: direct; 71:1-2 anchors envoy, warning, speech, and clarity; 71:5-10 anchors repeated calling, night, public proclamation, disclosure, secrecy, and renewed speech.
- Surprising reach: The message acts like a signal engineered for redundancy: carrier, voice, recurrence, visible sign, private address, and public broadcast all preserve the same directional pull.

#### Subchannel A. Carrier, voice, and sign disclose one meaning
- Reading type: mixed
- Scene or process: A commissioned carrier brings an alarm, voices it, and converts its meaning into an apprehensible sign.
- Active motifs: message-bearing envoy (`quranic:root_000563:B002/m01`); sending and release (`quranic:root_000563:B001/m01`); deliberate, measured delivery (`quranic:root_000563:B004/m01`); correspondence and matched exchange (`quranic:root_000563:B008/m01`); alarm that awakens caution (`quranic:root_001488:B001/m01`); vocal call that inclines its hearer (`quranic:root_000478:B001/m01`); articulated utterance (`quranic:root_001272:B001/m01`); tongue as speech instrument (`quranic:root_001272:B002/m01`); thing signifying by its state (`quranic:root_001272:B014/m01`); disclosure of meaning by speech or sign (`quranic:root_000170:B005/m01`); appearance and clarification (`quranic:root_000170:B004/m01`); announcement by call (`quranic:root_000022:B003/m01`); distinguishing mark that guides (`quranic:root_001040:B002/m01`).
- Ayah anchors: 71:1-2 (`ر س ل`, `ن ذ ر`, `ق و ل`, `ب ي ن`); 71:5-8 (`د ع و`, `ء ذ ن`); 71:4 (`ع ل م`).
- Synthesis: The carrier and the carried saying form one communicative scene. Warning is not merely noise: measured delivery and correspondence stabilize transmission, calling inclines an addressee, articulation gives it a linguistic body, clarification opens its meaning, and a mark or state makes that meaning locatable. The envoy is thus both bearer and signal.

#### Subchannel B. The call returns through the whole night-day cycle
- Reading type: mixed
- Scene or process: A summons is renewed until it occupies successive times and occasions rather than depending on a single hearing.
- Active motifs: vocal summons (`quranic:root_000478:B001/m01`); renewed or repeated call (`quranic:root_000209:B004/m01`); return to a place or state (`quranic:root_000209:B001/m01`); successive groups or dispatches (`quranic:root_000563:B005/m01`); night and its darkness (`quranic:root_001392:B001/m01`); action undertaken by night (`quranic:root_001392:B002/m01`); day opened by light (`quranic:root_001559:B002/m01`); total inclusion of parts (`quranic:root_001315:B003/m01`); increase and accretion (`quranic:root_000657:B001/m01`).
- Ayah anchors: 71:5 (`د ع و`, `ل ي ل`, `ن ه ر`); 71:6-8 (`د ع و`, `ز ي د`); 71:7 (`ك ل ل`, `ث و ب`); 71:1 and 71:11 (`ر س ل`).
- Synthesis: Repetition is rendered as return and successive release. Night and day supply complementary temporal chambers, while totality and increase make each renewed call cumulative. The response may increase flight, but the communicative operation itself keeps returning and filling the available cycle.

#### Subchannel C. Public exposure and secret address are complementary apertures
- Reading type: surface-primary
- Scene or process: The speaker alternately raises, displays, and privately deposits the same address so that no register remains unused.
- Active motifs: raised public utterance (`quranic:root_000269:B001/m01`); visible appearance after a barrier is removed (`quranic:root_000269:B002/m01`); imposing visibility (`quranic:root_000269:B003/m01`); disclosure after concealment (`quranic:root_001041:B001/m01`); written heading that makes a text findable (`quranic:root_001041:B002/m01`); hidden communication and confidence (`quranic:root_000697:B001/m01`); inward unvoiced saying (`quranic:root_001272:B012/m01`); penetration into hidden affairs (`quranic:root_000697:B014/m01`); disclosure of meaning (`quranic:root_000170:B005/m01`).
- Ayah anchors: 71:8 (`ج ه ر`, `د ع و`); 71:9 (`ع ل ن`, `س ر ر`); 71:2 and 71:5 (`ق و ل`, `ب ي ن`).
- Synthesis: Publicity and secrecy are not rival topics here but two apertures into one audience. Raised voice and visual exposure address the outer field; private confidence and inward speech enter the concealed field. Even the lexical heading functions as a locating device, making the proclaimed matter hard to lose in either register.

### 3. [P1 71:1-14] Covering Can Refuse Exposure or Convert It Into Safety
- Semantic invariant: A cover changes the relation between an exposed subject and what reaches it, either by blocking reception or by shielding from harm.
- Surface relation: direct; 71:7 anchors ears, fingers, clothing, self-covering, and forgiveness; 71:3-4 and 71:10 anchor protection and pardoning cover; 71:12 anchors the tree-covered garden.
- Surprising reach: The same material logic that makes a garment into an acoustic barricade also makes forgiveness a protective cover and a garden a habitable enclosure.

#### Subchannel A. The listener manufactures an acoustic enclosure
- Reading type: mixed
- Scene or process: Fingers, cloth, constricted hearing, and a covering of awareness are assembled into a barrier against an incoming call.
- Active motifs: ear as bodily aperture (`quranic:root_000022:B001/m01`); attentive reception and acceptance (`quranic:root_000022:B002/m01`); heaviness that blocks hearing (`quranic:root_001674:B001/m01`); human finger (`quranic:root_000841:B001/m01`); pouring through a narrow finger-gap (`quranic:root_000841:B004/m01`); garment and covering of the self (`quranic:root_000209:B003/m01`); overlying cover (`quranic:root_001088:B001/m01`); covering that overtakes awareness (`quranic:root_001088:B005/m01`); dull hearing and perception (`quranic:root_001315:B001/m01`); tent-like thin screen (`quranic:root_001315:B006/m01`); contraction and constriction (`quranic:root_000856:B006/m01`).
- Ayah anchors: 71:7 (`ء ذ ن`, `ص ب ع`, `ث و ب`, `غ ش و`, `ك ل ل`, `ص ر ر`); 71:13 (`و ق ر`).
- Synthesis: The scene has a precise mechanism: an aperture designed for reception is physically plugged, wrapped, and narrowed until sound and awareness are dulled. The finger-gap image intensifies the operation, because what can meter a flow is used instead to stop one. Refusal is materially built, not left as an abstract attitude.

#### Subchannel B. Pardoning cover interposes a shield against consequence
- Reading type: mixed
- Scene or process: Fault remains real, but a preserving layer covers it and stands between the offender and its damaging return.
- Active motifs: general covering that preserves (`quranic:root_001096:B001/m01`); forgiveness shielding from the effect of sin (`quranic:root_001096:B002/m01`); offense with a harmful outcome (`quranic:root_000521:B001/m01`); protective shield (`quranic:root_000266:B008/m01`); barrier that repels injury (`quranic:root_001677:B001/m01`); placing oneself in protection (`quranic:root_001677:B002/m01`); restraint and withholding (`quranic:root_000994:B003/m01`); garment as protective covering (`quranic:root_000209:B003/m01`).
- Ayah anchors: 71:1 (`ع ذ ب`); 71:3 (`و ق ي`); 71:4 (`غ ف ر`, `ذ ن ب`); 71:7 (`غ ف ر`, `ث و ب`); 71:10 (`غ ف ر`); 71:12 (`ج ن ن`).
- Synthesis: Forgiveness does not erase the causal scene by denial; it inserts a preserving layer. Shield, garment, restraint, and pardoning cover all modify exposure to harm. This reverses the crowd's operation: they cover themselves from the message, while the offered cover would protect them from the consequence.

#### Subchannel C. A covered interior becomes a productive refuge
- Reading type: latent/lexical
- Scene or process: Enclosure progresses from a hidden interior and defensive screen to a garden whose dense vegetation shelters and sustains life.
- Active motifs: concealment from perception (`quranic:root_000266:B001/m01`); tree-covered garden (`quranic:root_000266:B003/m01`); defensive screen (`quranic:root_000266:B008/m01`); hidden heart or interior (`quranic:root_000266:B010/m01`); dense, surging vegetation (`quranic:root_000266:B011/m01`); place of concealment (`quranic:root_000266:B017/m01`); preserving cover (`quranic:root_001096:B001/m01`); tent-like screen (`quranic:root_001315:B006/m01`).
- Ayah anchors: 71:4, 71:7, and 71:10 (`غ ف ر`); 71:7 (`ك ل ل`); 71:12 (`ج ن ن`).
- Synthesis: These motifs form a spatial transformation rather than a list of coverings. A hidden interior gains a defensive perimeter; that perimeter becomes a place of refuge; and thick vegetation turns refuge into a garden. The promised garden thus extends the logic of merciful covering into an inhabitable and fertile world.

### 4. [P1 71:1-14] Command Tests Whether the Human Becomes Traversable
- Semantic invariant: Response to command is figured as a change in resistance: yielding makes action smooth and passable, while refusal produces knots, stiffness, and upward competitive pressure.
- Surface relation: direct; 71:3 anchors worship, protection, and obedience; 71:7 anchors insistence and pride; 71:13 anchors refused reverence.
- Surprising reach: Obedience is not only a social posture; it is a road made level, a rein made responsive, and fruit made ready to gather.

#### Subchannel A. Worship aligns authority, will, and action
- Reading type: surface-primary
- Scene or process: A sovereign command is recognized, accepted, and carried through by a subject whose will moves with it.
- Active motifs: deity and worship (`quranic:root_000047:B001/m01`); lordship, ownership, and command (`quranic:root_000532:B001/m01`); servitude and owned status (`quranic:root_000973:B001/m01`); worship as humbled obedience (`quranic:root_000973:B003/m01`); bringing another under service (`quranic:root_000973:B004/m01`); willing obedience (`quranic:root_000956:B001/m01`); agreement and responsive following (`quranic:root_000956:B002/m01`); capacity to carry out action (`quranic:root_000956:B003/m01`); voluntary contribution beyond obligation (`quranic:root_000956:B005/m01`); self made ready for an act (`quranic:root_000956:B006/m01`); self-protective piety (`quranic:root_001677:B002/m01`).
- Ayah anchors: 71:3 (`ع ب د`, `ء ل ه`, `ط و ع`, `و ق ي`); 71:5 and 71:10 (`ر ب ب`).
- Synthesis: Authority, subjecthood, willingness, and execution occupy distinct roles. Worship names the relation, obedience supplies motion, capacity makes the act possible, and piety keeps the subject within protection. The scene therefore joins hierarchy to an internally consenting mechanism rather than reducing obedience to external compliance.

#### Subchannel B. Yielding makes a road smooth and a harvest ready
- Reading type: latent/lexical
- Scene or process: Resistance is removed from a route, rein, field, or fruit until movement and gathering become possible.
- Active motifs: paved and leveled road (`quranic:root_000973:B005/m01`); straightness and sound order (`quranic:root_001273:B008/m01`); sustaining support or framework (`quranic:root_001273:B009/m01`); easy limbs and gentle travel (`quranic:root_000563:B003/m01`); readiness and tractable approach (`quranic:root_000009:B003/m01`); pasture opened for grazing and fruit ready to pick (`quranic:root_000956:B007/m01`); fitness and preparedness (`quranic:root_000434:B005/m01`); acceptance with satisfaction (`quranic:root_001198:B004/m01`).
- Ayah anchors: 71:1 (`ء ت ي`, `ق ب ل`, `ر س ل`); 71:3 (`ع ب د`, `ط و ع`); 71:5 (`ق و م`); 71:14 (`خ ل ق`).
- Synthesis: These motifs share a functional invariant: an impediment is removed so that the intended operation can proceed. A road is leveled, limbs travel easily, a field permits grazing, and fruit permits gathering. Obedience is thereby materialized as becoming usable by a good direction.

#### Subchannel C. Refusal knots itself and rises into contest
- Reading type: mixed
- Scene or process: A subject contracts around a fixed decision, becomes heavy or immobile, then seeks elevation by resisting the command.
- Active motifs: binding and knotting (`quranic:root_000856:B001/m01`); fixed insistence (`quranic:root_000856:B002/m01`); constriction (`quranic:root_000856:B006/m01`); self-abasing submission refused (`quranic:root_001332:B004/m01`); self-exaltation and arrogance (`quranic:root_001281:B006/m01`); magnifying a thing inwardly (`quranic:root_001281:B003/m01`); rank and elevated headship (`quranic:root_001281:B005/m01`); burdensome resistance (`quranic:root_001281:B010/m01`); competitive domination (`quranic:root_001281:B011/m01`); confrontation and resistance (`quranic:root_001273:B014/m01`); stopping through exhaustion or rigidity (`quranic:root_001273:B016/m01`); complete pride (`quranic:root_000841:B006/m01`); heavy load (`quranic:root_001674:B002/m01`).
- Ayah anchors: 71:4 and 71:10 (`ك و ن`); 71:5 (`ق و م`); 71:7 (`ص ر ر`, `ك ب ر`, `ص ب ع`); 71:13 (`و ق ر`).
- Synthesis: The scene moves from inward fastening to outward rivalry. The will knots, the body contracts, the load grows heavy, and refusal seeks a higher rank from which to contest the command. Pride is thus the final mechanical state of accumulated resistance.

#### Subchannel D. Reverence balances hope, composure, and tested weight
- Reading type: mixed
- Scene or process: Expectation of divine good settles into deliberate conduct, dignified stillness, and the stable weight of tested character.
- Active motifs: heart reaching toward hoped-for good (`quranic:root_000548:B001/m01`); dignity, composure, and reverence (`quranic:root_001674:B003/m01`); character hardened by experience (`quranic:root_001674:B007/m01`); honoring and magnifying rightly (`quranic:root_000973:B006/m01`); measured deliberation (`quranic:root_000563:B004/m01`); elevation and high standing (`quranic:root_000745:B001/m01`); good reputation carried outward (`quranic:root_000745:B008/m01`).
- Ayah anchors: 71:1 and 71:11 (`ر س ل`); 71:3 (`ع ب د`); 71:4 and 71:11 (`س م و`); 71:13 (`ر ج و`, `و ق ر`).
- Synthesis: Reverence is neither fear alone nor social inflation. Hope supplies an inward orientation, experience gives weight, deliberation slows conduct, and composure makes honor visible without competitive self-elevation. The scene distinguishes warranted dignity from the swollen rank of refusal.

### 5. [P1 71:1-14] Released Water Becomes Organized Provision
- Semantic invariant: Supply moves through a causal system from elevated release, to capture and routing, to biological and economic increase.
- Surface relation: direct; 71:11 anchors sending, sky, and abundant pouring; 71:12 anchors extension, wealth, children, gardens, and rivers.
- Surprising reach: Rain is rendered not as atmosphere alone but as a complete infrastructure: cloud reservoir, discharge, basin, channel, productive estate, and circulating surplus.

#### Subchannel A. An elevated reservoir releases a sustained discharge
- Reading type: mixed
- Scene or process: Water gathers above, is released from its source, and descends in a repeated abundant flow.
- Active motifs: sky, cloud, and overhead cover (`quranic:root_000745:B004/m01`); layered rain-bearing cloud (`quranic:root_000532:B008/m01`); cloud mass (`quranic:root_001559:B008/m01`); sending and release (`quranic:root_000563:B001/m01`); abundant outflow from a source (`quranic:root_000469:B001/m01`); successive milk-like flow (`quranic:root_000563:B006/m01`); sky-exposed state (`quranic:root_000994:B004/m01`); circular turbulent water (`quranic:root_000469:B008/m01`); cloud-ring or encircling mass (`quranic:root_001315:B005/m01`).
- Ayah anchors: 71:4 and 71:11 (`س م و`); 71:5 and 71:10 (`ر ب ب`); 71:11 (`ر س ل`, `د ر ر`); 71:5 and 71:12 (`ن ه ر`); 71:1 (`ع ذ ب`); 71:7 (`ك ل ل`).
- Synthesis: The scene is hydraulic: an overhead cover holds a cloud mass, dispatch releases it, and abundant outflow supplies the process. The milk sense gives repeated rain the function of nourishment drawn continuously from a source.

#### Subchannel B. Basins, cuts, and channels capture and route the flow
- Reading type: latent/lexical
- Scene or process: Descending water is collected in depressions, cleaned, linked, and guided through cuts toward fields and rivers.
- Active motifs: directed watercourse (`quranic:root_000009:B004/m01`); incoming flood from another district (`quranic:root_000009:B005/m01`); collecting basin for later irrigation (`quranic:root_000016:B007/m01`); water hollow around a fort (`quranic:root_000281:B003/m01`); collecting water hollow (`quranic:root_000282:B002/m01`); rock basin or new well (`quranic:root_000434:B011/m01`); cleansing a well until water appears (`quranic:root_000269:B008/m01`); tail-channel and valley outlet (`quranic:root_000521:B004/m01`); large collected water (`quranic:root_001040:B005/m01`); one stream feeding another (`quranic:root_001407:B003/m01`); river cut through earth (`quranic:root_001559:B001/m01`); opening widened until flow passes (`quranic:root_001559:B003/m01`); sweet, drinkable water (`quranic:root_000994:B001/m01`).
- Ayah anchors: 71:1 (`ء ت ي`); 71:4 (`ء ج ل`, `ج ي ء`, `ذ ن ب`, `ع ل م`); 71:8 (`ج ه ر`); 71:12 (`م د د`, `ن ه ر`); 71:14 (`خ ل ق`).
- Synthesis: This is a complete waterworks scene. An external flood arrives, basins arrest it, wells and rock hollows hold it, cleansing exposes drinkable water, and linked courses send it onward. The promised rivers are thereby reframed as managed continuity between collection, purification, and release.

#### Subchannel C. Water is converted into garden, offspring, and bodily growth
- Reading type: mixed
- Scene or process: Routed supply enters living substrates, thickens vegetation, produces yield, and sustains human and familial increase.
- Active motifs: tree-covered garden (`quranic:root_000266:B003/m01`); dense and surging vegetation (`quranic:root_000266:B011/m01`); crop and palm yield (`quranic:root_000009:B007/m01`); pasture and fruit ready for use (`quranic:root_000956:B007/m01`); building flesh through food (`quranic:root_000156:B010/m01`); lineage and offspring (`quranic:root_000156:B007/m01`); connected reinforcement by material, wealth, or children (`quranic:root_001407:B002/m01`); making and bringing into being (`quranic:root_000248:B001/m01`); placing into a new condition (`quranic:root_000248:B002/m01`); wealth accumulated as property (`quranic:root_001457:B001/m01`).
- Ayah anchors: 71:1 (`ء ت ي`); 71:3 (`ط و ع`); 71:7 and 71:12 (`ج ع ل`); 71:12 (`ج ن ن`, `ب ن ي`, `م د د`, `م و ل`).
- Synthesis: The flow becomes productive only when it enters a living system. Yield, ripe pasture, thick vegetation, nourishment building flesh, children extending lineage, and wealth extending capacity are successive conversions of one supply. The surface gifts form an ecology rather than a loose inventory.

#### Subchannel D. Surplus circulates as payment, support, and travel stock
- Reading type: latent/lexical
- Scene or process: Yield is measured, transferred, stored, and used to reinforce people beyond the moment of production.
- Active motifs: levy or tribute paid (`quranic:root_000009:B008/m01`); wage assigned for work (`quranic:root_000248:B005/m01`); connected reinforcement by wealth and helpers (`quranic:root_001407:B002/m01`); increase and growth (`quranic:root_000657:B001/m01`); request and bidding for increase (`quranic:root_000657:B004/m01`); travel provision and its container (`quranic:root_000657:B005/m01`); gentle prosperity and willing giving (`quranic:root_000563:B010/m01`); property and wealth (`quranic:root_001457:B001/m01`); sustaining means of life (`quranic:root_001273:B009/m01`); valuation and pricing (`quranic:root_001273:B010/m01`); market circulation (`quranic:root_001273:B018/m01`).
- Ayah anchors: 71:1 (`ء ت ي`); 71:5 (`ق و م`); 71:6 (`ز ي د`); 71:7 and 71:12 (`ج ع ل`); 71:11 (`ر س ل`); 71:12 (`م د د`, `م و ل`).
- Synthesis: Productive abundance acquires a social afterlife. It becomes a wage, levy, price, reserve, travel stock, or reinforcement supplied to others. This circulation pressures a merely acquisitive reading of wealth: the latent system is healthy when surplus sustains further movement.

### 6. [P1 71:1-14] Creation Proceeds by Measure, Assembly, and Stage
- Semantic invariant: A formed being emerges through prior measure, joined structure, staged transition, and sustained maturation.
- Surface relation: direct; 71:12 anchors children and material extension; 71:14 anchors creation in successive forms.
- Surprising reach: Human creation is materialized as tailoring, architecture, bodily support, gestation, and gradual upbringing rather than a single instantaneous event.

#### Subchannel A. Measure becomes a joined and supported form
- Reading type: mixed
- Scene or process: A form is estimated, brought into existence, assembled from parts, and stabilized by internal supports.
- Active motifs: prior estimating and measuring (`quranic:root_000434:B001/m01`); originating a created thing (`quranic:root_000434:B002/m01`); completed and proportioned form (`quranic:root_000434:B003/m01`); inward disposition (`quranic:root_000434:B004/m01`); making and bringing into being (`quranic:root_000248:B001/m01`); placing into a condition (`quranic:root_000248:B002/m01`); construction by joining parts (`quranic:root_000156:B001/m01`); composite constitution (`quranic:root_000156:B002/m01`); ribs and structural props (`quranic:root_000156:B009/m01`); corresponding pieces joined face-to-face (`quranic:root_001198:B010/m01`); sustaining framework (`quranic:root_001273:B009/m01`); upright component or implement (`quranic:root_001273:B012/m01`); occurrence in existence (`quranic:root_001332:B001/m01`).
- Ayah anchors: 71:1 (`ق ب ل`); 71:4 and 71:10 (`ك و ن`); 71:5 (`ق و م`); 71:7 and 71:12 (`ج ع ل`); 71:12 (`ب ن ي`); 71:14 (`خ ل ق`).
- Synthesis: Creation has the internal sequence of craft. Estimation precedes production; production joins parts; joined parts receive ribs, props, and an upright frame; and the result takes a completed outward form and inward disposition. The body is read as a measured construction whose coherence is made.

#### Subchannel B. Development crosses successive limits and states
- Reading type: mixed
- Scene or process: A developing subject advances through repeated conditions, each with a boundary, threshold, and newly available capacity.
- Active motifs: successive stages and conditions (`quranic:root_000955:B004/m01`); boundary reached or exceeded (`quranic:root_000955:B003/m01`); edge and surrounding precinct (`quranic:root_000955:B001/m01`); intermediate condition between poles (`quranic:root_000170:B011/m01`); temporal precedence and early phase (`quranic:root_001198:B002/m01`); fresh beginning not prepared in advance (`quranic:root_001198:B015/m01`); beginning of a thing (`quranic:root_000266:B014/m01`); appointed span (`quranic:root_000016:B001/m01`); total joining of parts (`quranic:root_001315:B003/m01`).
- Ayah anchors: 71:1 (`ق ب ل`); 71:2 (`ب ي ن`); 71:4 (`ء ج ل`); 71:7 (`ك ل ل`); 71:12 (`ج ن ن`); 71:14 (`ط و ر`).
- Synthesis: A stage is neither a random variation nor merely a finished type. It is a bounded condition that begins, occupies an interval, and yields to another. The motifs preserve both discontinuity at thresholds and continuity of the one subject traversing them.

#### Subchannel C. Gestation and upbringing extend creation through care
- Reading type: latent/lexical
- Scene or process: Hidden gestation produces offspring whose bodies, capacities, and social place are gradually sustained into maturity.
- Active motifs: fetus concealed in the womb (`quranic:root_000266:B007/m01`); lineage and offspring (`quranic:root_000156:B007/m01`); food building flesh (`quranic:root_000156:B010/m01`); repair, completion, and gradual upbringing (`quranic:root_000532:B002/m01`); foster child and caregiver (`quranic:root_000532:B005/m01`); recent birth and maternal staying (`quranic:root_000532:B009/m01`); pregnancy nearing delivery (`quranic:root_000548:B005/m01`); midwife receiving the emerging child (`quranic:root_001198:B007/m01`); womb and post-birth discharge (`quranic:root_000994:B009/m01`); growth and yield (`quranic:root_000009:B007/m01`).
- Ayah anchors: 71:1 (`ء ت ي`, `ع ذ ب`, `ق ب ل`); 71:5 and 71:10 (`ر ب ب`); 71:12 (`ب ن ي`, `ج ن ن`); 71:13 (`ر ج و`).
- Synthesis: The hidden beginning is followed by delivery, nourishment, fostered care, and bodily growth. Creation therefore continues through relational labor after emergence. The parental and pastoral vocabulary makes staged creation a sustained economy of care.

### 7. [P1 71:1-14] A People Can Gather as a Household or Scatter as a Fleeing Herd
- Semantic invariant: Collective identity depends on a governing relation that gathers and tends members; rejection reverses that gathering into dispersal.
- Surface relation: direct; 71:1-5 repeatedly anchors the addressed people and their caller; 71:6 anchors flight; 71:11-12 anchors rain, wealth, children, gardens, and rivers as provision for the collective.
- Surprising reach: The people addressed as a social body are also legible as a tended herd whose keeper supplies pasture, water, and milk, yet whose response is to bolt and fragment.

#### Subchannel A. Community is assembled by relation and care
- Reading type: mixed
- Scene or process: Individuals become a people through kinship, gathering, governance, and the care that maintains their common life.
- Active motifs: human community and kin group (`quranic:root_001273:B001/m01`); settled gathering or council (`quranic:root_001273:B006/m01`); guardianship and governance (`quranic:root_001273:B004/m01`); sustaining framework of communal life (`quranic:root_001273:B009/m01`); large gathered groups (`quranic:root_000532:B004/m01`); sovereign owner and caretaker (`quranic:root_000532:B001/m01`); group facing one another (`quranic:root_001198:B009/m01`); public assembly (`quranic:root_000269:B006/m01`); mass of the people (`quranic:root_000266:B013/m01`); whole crowd without remainder (`quranic:root_001096:B008/m01`); assembled groups (`quranic:root_001315:B009/m01`).
- Ayah anchors: 71:1-2 and 71:5 (`ق و م`); 71:1 (`ق ب ل`); 71:5 and 71:10 (`ر ب ب`); 71:4, 71:7, and 71:10 (`غ ف ر`); 71:7 (`ك ل ل`); 71:8 (`ج ه ر`); 71:12 (`ج ن ن`).
- Synthesis: Community is not mere numerical plurality. Facing, council, shared lineage, governance, and maintenance gather members into a body. The repeated address “my people” therefore invokes an organized relation whose integrity the warning tries to preserve.

#### Subchannel B. Pastoral care releases, waters, and feeds a herd
- Reading type: latent/lexical
- Scene or process: A keeper gathers animals, releases them in ordered groups, provides water and milk, and holds them in usable pasture.
- Active motifs: wild herd gathered as one (`quranic:root_000016:B004/m01`); stock retained in pasture (`quranic:root_000016:B008/m01`); herd of cattle or camels (`quranic:root_000532:B014/m01`); successive groups sent to pasture or water (`quranic:root_000563:B005/m01`); repeated milk supply (`quranic:root_000563:B006/m01`); residual milk drawing the next flow (`quranic:root_000478:B003/m01`); watering directly at the animals' mouths (`quranic:root_001198:B014/m01`); pasture opened and fruit made available (`quranic:root_000956:B007/m01`); herd or flock (`quranic:root_001674:B006/m01`); young animal following its dam (`quranic:root_001142:B004/m01`).
- Ayah anchors: 71:1 (`ق ب ل`); 71:4 (`ء ج ل`); 71:5-8 (`د ع و`); 71:11 (`ر س ل`); 71:3 (`ط و ع`); 71:5 and 71:10 (`ر ب ب`); 71:6 (`ف ر ر`); 71:13 (`و ق ر`).
- Synthesis: This is a husbandry mechanism with keeper, herd, release, feeding ground, water, and milk. It gives the divine provision a pastoral form: restraint is used for care, release is ordered, and recurring nourishment draws more nourishment.

#### Subchannel C. The summoned herd breaks formation and scatters
- Reading type: mixed
- Scene or process: Instead of inclining toward the caller, members bolt, move erratically, and disperse into incompatible directions.
- Active motifs: flight and escape (`quranic:root_001142:B001/m01`); rash, foolish haste (`quranic:root_001142:B005/m01`); violent shaking and tearing motion (`quranic:root_001142:B006/m01`); crowd in confusion (`quranic:root_001142:B016/m01`); people or roads scattered in every direction (`quranic:root_000973:B010/m01`); mount disabled or refusing movement (`quranic:root_000973:B011/m01`); cascading collapse (`quranic:root_000478:B005/m01`); confrontation and resistance (`quranic:root_001273:B014/m01`); immobility and exhaustion (`quranic:root_001273:B016/m01`); competitive domination (`quranic:root_001281:B011/m01`).
- Ayah anchors: 71:3 (`ع ب د`); 71:5-8 (`د ع و`); 71:6 (`ف ر ر`); 71:5 (`ق و م`); 71:7 (`ك ب ر`).
- Synthesis: Flight is decomposed into escape, rash acceleration, tearing movement, confusion, and scattering. The disabled mount provides the inverse failure, while confrontation gives the social cause. The collective ceases to behave as a gathered people and becomes motion without common direction.

### 8. [P2 71:15-28] Creation Installs a Layered Canopy and Its Lights
- Semantic invariant: The upper world is formed as an ordered, superposed structure whose luminous bodies are placed as functional fixtures.
- Surface relation: direct; 71:15 anchors seeing, creation, seven, heavens, and layers; 71:16 anchors placing, moon, light, sun, and lamp.
- Surprising reach: The cosmos is simultaneously architecture, matched stack, optical field, and furnished interior.

#### Subchannel A. Measured parts are matched into superposed tiers
- Reading type: surface-primary
- Scene or process: A maker estimates and forms multiple overhead units, then aligns and stacks them into a coherent whole.
- Active motifs: prior measure and estimation (`quranic:root_000434:B001/m01`); origination of a created thing (`quranic:root_000434:B002/m01`); completed proportioned form (`quranic:root_000434:B003/m01`); making and bringing into being (`quranic:root_000248:B001/m01`); placing into a condition (`quranic:root_000248:B002/m01`); sevenfold number and multiplication (`quranic:root_000669:B001/m01`); overhead sky and ceiling (`quranic:root_000745:B004/m01`); layers placed one above another (`quranic:root_000927:B002/m01`); one surface covering its counterpart (`quranic:root_000927:B001/m01`); correspondence and fit (`quranic:root_000927:B003/m01`); transition from state to state (`quranic:root_000927:B004/m01`); ranked class or stratum (`quranic:root_000927:B005/m01`); smooth level surface (`quranic:root_000434:B008/m01`).
- Ayah anchors: 71:15 (`خ ل ق`, `س ب ع`, `س م و`, `ط ب ق`); 71:16 and 71:19 (`ج ع ل`).
- Synthesis: The tiers are not merely numerous. Measure supplies dimensions, completed form supplies bounded units, matching supplies fit, and superposition supplies architecture. The sevenfold upper world is a deliberately assembled stack.

#### Subchannel B. Moon and sun are installed as differentiated fixtures
- Reading type: surface-primary
- Scene or process: Distinct luminous objects are placed within the layered structure to perform complementary lighting functions.
- Active motifs: placing and assigning function (`quranic:root_000248:B002/m01`); moon and its light (`quranic:root_001255:B001/m01`); illumination (`quranic:root_001564:B001/m01`); sun and its radiance (`quranic:root_000818:B001/m01`); luminous lamp (`quranic:root_000693:B001/m01`); visible elevated object (`quranic:root_000745:B002/m01`); direct visual apprehension (`quranic:root_000531:B001/m01`); showing a thing so another sees it (`quranic:root_000531:B012/m01`).
- Ayah anchors: 71:15 (`ر ء ي`, `س م و`); 71:16 (`ج ع ل`, `ق م ر`, `ن و ر`, `ش م س`, `س ر ج`).
- Synthesis: Placement turns light into furnishing. The moon supplies reflected nocturnal visibility, the sun supplies direct radiance, and the lamp image makes luminosity an installed service within the larger structure. Seeing is the human operation matched to that arrangement.

### 9. [P2 71:15-28] Light Can Guide Sight or Capture It
- Semantic invariant: Visibility is an active relation: light may reveal an orienting sign, overwhelm perception, or manufacture a persuasive appearance.
- Surface relation: direct and indirect; 71:15-16 anchors sight and celestial light; 71:22-23 anchors plotting and cult objects; 71:25 turns light's fire-sense into punitive exposure.
- Surprising reach: The same optical field contains landmark, glare, nocturnal hunter, cosmetic enhancement, false lamp, and consuming fire.

#### Subchannel A. Illumination makes landmarks and routes legible
- Reading type: mixed
- Scene or process: Light reveals forms and elevated markers by which an observer can orient thought and movement.
- Active motifs: direct visual apprehension (`quranic:root_000531:B001/m01`); reflective judgment and deliberation (`quranic:root_000531:B002/m01`); reciprocal visibility between facing sides (`quranic:root_000531:B004/m01`); visible aspect and mirror (`quranic:root_000531:B006/m01`); raised banner (`quranic:root_000531:B011/m01`); showing a thing to another (`quranic:root_000531:B012/m01`); interrogative summons to notice (`quranic:root_000531:B013/m01`); luminous moon (`quranic:root_001255:B001/m01`); illumination (`quranic:root_001564:B001/m01`); visible beacon or boundary marker (`quranic:root_001564:B005/m01`); luminous lamp (`quranic:root_000693:B001/m01`); sun and daylight (`quranic:root_000818:B001/m01`); two celestial stars named as vultures (`quranic:root_001496:B006/m01`).
- Ayah anchors: 71:15 (`ر ء ي`); 71:16 (`ق م ر`, `ن و ر`, `س ر ج`, `ش م س`); 71:23 (`ن س ر`); 71:25 (`ن و ر`).
- Synthesis: Vision, reflection, mirror, banner, beacon, moon, sun, and lamp occupy one orienting scene. Light makes a sign available; a sign gives sight a target; and sight becomes deliberative rather than merely sensory. Celestial luminosity thus supports both wayfinding and recognition.

#### Subchannel B. Glare and nocturnal exposure turn the observer into prey
- Reading type: latent/lexical
- Scene or process: Excess or badly situated light confuses sight, prevents rest, and exposes a subject to hunters or hostile force.
- Active motifs: hunting by moonlight (`quranic:root_001255:B003/m01`); sight bewildered by intense whiteness (`quranic:root_001255:B005/m01`); wakefulness under moonlight (`quranic:root_001255:B009/m01`); property left unguarded at night (`quranic:root_001255:B011/m01`); refractory animal or hostile disposition (`quranic:root_000818:B002/m01`); open hostility (`quranic:root_000818:B003/m01`); withholding what lies behind one's back (`quranic:root_000818:B006/m01`); flight and instability (`quranic:root_001564:B006/m01`); enmity between groups (`quranic:root_001564:B007/m01`).
- Ayah anchors: 71:16 (`ق م ر`, `ش م س`, `ن و ر`); 71:25 (`ن و ر`).
- Synthesis: Light no longer simply serves the viewer. It blinds, keeps the subject awake, exposes unattended property, and gives the night hunter an advantage. The optical relation reverses: what should reveal the path can make the observer visible to a hostile gaze.

#### Subchannel C. Manufactured brilliance can pass for truth
- Reading type: latent/lexical
- Scene or process: Surface enhancement, display, and false luminosity create an attractive but unreliable appearance.
- Active motifs: beautifying and brightening a face or object (`quranic:root_000693:B003/m01`); false lamp and lying speech (`quranic:root_000693:B005/m01`); gambling victory by deception (`quranic:root_001255:B007/m01`); action performed to be seen (`quranic:root_000531:B005/m01`); cosmetic coating (`quranic:root_001564:B009/m01`); smoke pigment used as kohl or tattoo (`quranic:root_001564:B008/m01`); ochre coating (`quranic:root_001438:B004/m01`); fabricated speech (`quranic:root_000434:B007/m01`); fire and branding flame (`quranic:root_001564:B002/m01`).
- Ayah anchors: 71:15 (`ر ء ي`, `خ ل ق`); 71:16 (`ق م ر`, `س ر ج`, `ن و ر`); 71:22 (`م ك ر`); 71:25 (`ن و ر`).
- Synthesis: Cosmetic brightness and ostentatious display can simulate disclosure while hiding fabrication. The false lamp joins verbal invention to optical persuasion, and the same fire that lends brilliance can brand or consume. This gives the polemic a precise pressure point: appearance is not self-authenticating.

### 10. [P2 71:15-28] Human Life Is Planted, Returned, and Raised
- Semantic invariant: Human existence follows a cultivated cycle of placement in earth, growth, return, and renewed emergence.
- Surface relation: direct; 71:17 anchors human growth from earth; 71:18 anchors return into it and exit from it; 71:27-28 anchors generation, parents, and offspring.
- Surprising reach: Agriculture, burial, education, and biological descent become phases of one generative process.

#### Subchannel A. The earth is a growing medium for human formation
- Reading type: mixed
- Scene or process: A cultivator places living material in receptive ground, tends it, and brings a formed human subject to maturity.
- Active motifs: soft fertile earth (`quranic:root_000025:B002/m01`); plant emerging from ground (`quranic:root_001465:B001/m01`); deliberate planting (`quranic:root_001465:B002/m01`); source and growing site (`quranic:root_001465:B005/m01`); human growth and upbringing (`quranic:root_001465:B006/m01`); grain spike extending from the stalk (`quranic:root_000672:B008/m01`); tree flower as emitted light (`quranic:root_001564:B004/m01`); seed covered by soil (`quranic:root_001307:B008/m01`); fruit enclosed in its sheath (`quranic:root_001307:B010/m01`); origination (`quranic:root_000434:B002/m01`); gradual repair and completion (`quranic:root_000532:B002/m01`).
- Ayah anchors: 71:15 (`خ ل ق`); 71:16 and 71:25 (`ن و ر`); 71:17 (`ء ر ض`, `ن ب ت`); 71:20 (`س ب ل`); 71:21, 71:26, and 71:28 (`ر ب ب`); 71:26-27 (`ك ف ر`).
- Synthesis: Earth supplies setting and material receptivity; planting supplies agency; seed-covering supplies protected latency; and upbringing extends cultivation into human care. “Growing you” therefore remains biologically, pedagogically, and spiritually active.

#### Subchannel B. Burial is a return to the source before emergence
- Reading type: mixed
- Scene or process: A subject re-enters its originating ground, disappears within a terminal dwelling, and is brought outward again.
- Active motifs: return after departure (`quranic:root_001058:B001/m01`); place and time of return (`quranic:root_001058:B002/m01`); repeated visitation of the sick or mourning place (`quranic:root_001058:B005/m01`); benefit that returns to its recipient (`quranic:root_001058:B006/m01`); ancient return-road (`quranic:root_001058:B009/m01`); entering a place or state (`quranic:root_000464:B001/m01`); penetration to the outside (`quranic:root_000400:B001/m01`); extraction from concealment (`quranic:root_000400:B002/m01`); grave as a house (`quranic:root_000166:B007/m01`); remote village or grave (`quranic:root_001307:B012/m01`); disappearance into earth (`quranic:root_000913:B002/m01`); clinging to the ground (`quranic:root_000025:B006/m01`).
- Ayah anchors: 71:17 and 71:26 (`ء ر ض`); 71:18 (`ع و د`, `خ ر ج`); 71:24 and 71:27 (`ض ل ل`); 71:25 and 71:28 (`د خ ل`); 71:26-27 (`ك ف ر`); 71:28 (`ب ي ت`).
- Synthesis: Return, entry, disappearance, grave-house, extraction, and exit form one reversible spatial sequence. Earth is not merely the place of disposal; it is the prior source and temporary interior from which renewed outward movement is possible.

#### Subchannel C. Offspring are new growth carrying prior formation forward
- Reading type: mixed
- Scene or process: Birth produces descendants whose bodily and moral formation extends a lineage into a new cycle.
- Active motifs: child or descendant (`quranic:root_001683:B001/m01`); parents as source of birth (`quranic:root_001683:B002/m01`); childbirth (`quranic:root_001683:B003/m01`); recently born child (`quranic:root_001683:B004/m01`); derivative generated from a prior thing (`quranic:root_001683:B005/m01`); peer of the same birth-age (`quranic:root_001683:B006/m01`); new human generation (`quranic:root_001465:B003/m01`); human upbringing (`quranic:root_001465:B006/m01`); pregnancy becoming visibly apparent (`quranic:root_000531:B010/m01`); completed created form (`quranic:root_000434:B003/m01`).
- Ayah anchors: 71:15 (`خ ل ق`, `ر ء ي`); 71:17 (`ن ب ت`); 71:21, 71:27, and 71:28 (`و ل د`).
- Synthesis: Birth, derivative formation, peer generation, and upbringing all make offspring more than numerical additions. Each child is a new growth generated from prior embodied and social material. That continuity makes moral reproduction in 71:27 a concrete extension of the creation cycle.

### 11. [P2 71:15-28] Prepared Ground Becomes Route, Dwelling, and Contested Residence
- Semantic invariant: Space is made usable by spreading, opening, traversing, and inhabiting it; judgment then contests who may remain and who may enter a protected house.
- Surface relation: direct; 71:19-20 anchors the spread earth and broad paths; 71:26 anchors residence on earth; 71:28 anchors entry into the house.
- Surprising reach: The earth-carpet is not passive scenery but civic infrastructure whose routes lead either to inhabited refuge or to an emptied settlement.

#### Subchannel A. A spread floor releases movement
- Reading type: surface-primary
- Scene or process: Ground is flattened and widened until bodies can range across it without being held by constriction.
- Active motifs: spreading and extension against contraction (`quranic:root_000116:B001/m01`); broad level earth or carpet (`quranic:root_000116:B002/m01`); breadth and added capacity (`quranic:root_000116:B003/m01`); travel across lands (`quranic:root_000116:B007/m01`); extended reach and distance (`quranic:root_000116:B011/m01`); massive woven carpet (`quranic:root_000025:B005/m01`); lower ground beneath the sky (`quranic:root_000025:B001/m01`); firm rooting in earth (`quranic:root_000025:B002/m01`).
- Ayah anchors: 71:17 and 71:19 (`ء ر ض`); 71:19 (`ب س ط`).
- Synthesis: The floor is made by a sequence of release: contraction gives way to spread, spread to breadth, and breadth to range. Carpet and fertile ground add tactile and functional qualities, making the earth a stable surface prepared for living movement.

#### Subchannel B. Openings become roads through difficult terrain
- Reading type: mixed
- Scene or process: A traveler enters a route, follows its line, and passes through widened gaps between constraining sides.
- Active motifs: extended road and means of access (`quranic:root_000672:B001/m01`); travelers and road-users (`quranic:root_000672:B002/m01`); penetration along a route (`quranic:root_000735:B001/m01`); insertion into a course (`quranic:root_000735:B002/m01`); sewing thread passing through material (`quranic:root_000735:B004/m01`); extended border cut along a garment (`quranic:root_000735:B005/m01`); broad pass between mountains (`quranic:root_001131:B001/m01`); opening a gap between two sides (`quranic:root_001131:B002/m01`); rapid release into motion (`quranic:root_001131:B004/m01`); straight-directed course (`quranic:root_000735:B003/m01`).
- Ayah anchors: 71:20 (`س ب ل`, `س ل ك`, `ف ج ج`).
- Synthesis: Route, traveler, insertion, penetration, thread, border, and mountain pass occupy distinct roles in one movement scene. The path is an engineered line through resistant material: it receives the traveler, keeps direction, and turns an obstructed landscape into a passage.

#### Subchannel C. House, household, and resident define protected belonging
- Reading type: mixed
- Scene or process: A dwelling shelters a recognized household and admits a trusted entrant into its interior.
- Active motifs: shelter and dwelling (`quranic:root_000166:B001/m01`); household and dependents (`quranic:root_000166:B002/m01`); house of inherited standing (`quranic:root_000166:B008/m01`); entry into an interior (`quranic:root_000464:B001/m01`); inward confidential domain (`quranic:root_000464:B003/m01`); outsider incorporated among a people (`quranic:root_000464:B005/m01`); settled householder or resident (`quranic:root_000499:B007/m01`); security and trustworthy belonging (`quranic:root_000054:B001/m01`); faith as heart-settling assent (`quranic:root_000054:B002/m01`).
- Ayah anchors: 71:25 and 71:28 (`د خ ل`); 71:26 (`د و ر`); 71:28 (`ب ي ت`, `ء م ن`).
- Synthesis: Belonging is built through shelter, kin relation, recognized standing, admission, and trust. Entry is not generic movement; it crosses a social boundary into an interior whose members are secured by a shared assent.

#### Subchannel D. The inhabited earth can be emptied of its rejecting householder
- Reading type: mixed
- Scene or process: Residence becomes the object of removal until a formerly inhabited territory contains no remaining occupant.
- Active motifs: absence of any resident (`quranic:root_000499:B008/m01`); terminal hostile circuit around a group (`quranic:root_000499:B004/m01`); staying fixed to the ground (`quranic:root_000025:B006/m01`); remote or cut-off settlement (`quranic:root_001307:B012/m01`); abandoning and leaving (`quranic:root_001638:B003/m01`); dwelling and shelter (`quranic:root_000166:B001/m01`); destruction and breaking (`quranic:root_000174:B001/m01`).
- Ayah anchors: 71:17, 71:19, and 71:26 (`ء ر ض`); 71:23, 71:26, and 71:27 (`و ذ ر`); 71:26 (`د و ر`, `ك ف ر`); 71:28 (`ب ي ت`, `ت ب ر`).
- Synthesis: The prayer's resident is not just an isolated individual. Dwelling, fixed attachment, settlement, and hostile encirclement make residence a durable claim; leaving and breaking reverse it. The prepared earth can therefore move from hospitable infrastructure to a territory deliberately cleared of a destructive occupancy.

### 12. [P2 71:15-28] Following Converts Increase Into Multiplying Loss
- Semantic invariant: Allegiance propagates a governing direction, so assets and descendants amplify either ordered life or the loss already embedded in their leader.
- Surface relation: direct; 71:21 anchors disobedience, following, increase, wealth, children, and loss; 71:24 anchors many being led astray and increased error; 71:27 anchors generated transgression and denial.
- Surprising reach: Loss behaves like a bad balance sheet and a reproductive process: capital, claims, speech, followers, and offspring all enlarge the same deficit.

#### Subchannel A. Following transfers another's direction and liability
- Reading type: mixed
- Scene or process: A follower places movement, judgment, and consequence behind a leader, allowing one direction to become a succession.
- Active motifs: following person, command, or trace (`quranic:root_000175:B001/m01`); catching what went ahead (`quranic:root_000175:B002/m01`); tracing an effect step by step (`quranic:root_000175:B003/m01`); uninterrupted succession (`quranic:root_000175:B004/m01`); liability that follows an act (`quranic:root_000175:B006/m01`); rulers succeeding one another (`quranic:root_000175:B009/m01`); ordered and proportionate execution (`quranic:root_000175:B012/m01`); departure from obedience or group (`quranic:root_000400:B006/m01`); departure from obedience (`quranic:root_001022:B001/m01`); ruling speaker whose word takes effect (`quranic:root_001272:B004/m01`); circulating public saying (`quranic:root_001272:B007/m01`); negotiation over an affair (`quranic:root_001272:B009/m01`); imposing judgment on another (`quranic:root_001272:B010/m01`); professed creed or position (`quranic:root_001272:B013/m01`).
- Ayah anchors: 71:18 (`خ ر ج`); 71:21 (`ت ب ع`, `ع ص ي`, `ق و ل`); 71:23 and 71:26 (`ق و ل`).
- Synthesis: Following is simultaneously motion, succession, and transferred consequence. The leader's operative word supplies direction; the follower catches and continues it; and liability trails the sequence. Disobedience can therefore become organized rather than merely individual.

#### Subchannel B. Wealth and children compound a deficit
- Reading type: surface-primary
- Scene or process: Property and descendants are added to an already losing account, magnifying rather than correcting its direction.
- Active motifs: property and accumulated wealth (`quranic:root_001457:B001/m01`); increase and growth (`quranic:root_000657:B001/m01`); strained excess (`quranic:root_000657:B003/m01`); bidding for further increase (`quranic:root_000657:B004/m01`); general diminution (`quranic:root_000409:B001/m01`); commercial loss of capital (`quranic:root_000409:B002/m01`); short measure or weight (`quranic:root_000409:B003/m01`); revenue paid out from a holding (`quranic:root_000400:B003/m01`); partners or heirs dividing shares (`quranic:root_000400:B012/m01`); numerical abundance (`quranic:root_001286:B001/m01`); rivalry by number and possessions (`quranic:root_001286:B002/m01`); person burdened by many claims (`quranic:root_001286:B003/m01`); child or descendant (`quranic:root_001683:B001/m01`).
- Ayah anchors: 71:18 (`خ ر ج`); 71:21 (`ز ي د`, `م و ل`, `و ل د`, `خ س ر`); 71:24 (`ز ي د`, `ك ث ر`); 71:28 (`ز ي د`).
- Synthesis: The accounting scene distinguishes capital, addition, excess, claim, deficient measure, and terminal loss. More assets do not change the sign of the account; they scale it. Children similarly become extensions of the prior direction rather than independent proof of success.

#### Subchannel C. Error reproduces itself through numbers and generation
- Reading type: mixed
- Scene or process: Misguidance spreads across a crowd and then through offspring, turning a present deviation into a durable lineage.
- Active motifs: deviation from path and guidance (`quranic:root_000913:B001/m01`); loss of the thing or its location (`quranic:root_000913:B003/m01`); failed retention and memory (`quranic:root_000913:B004/m01`); increase and accretion (`quranic:root_000657:B001/m01`); multiplication of number (`quranic:root_001286:B001/m01`); new human generation (`quranic:root_001465:B003/m01`); childbirth (`quranic:root_001683:B003/m01`); derivative generated from a prior source (`quranic:root_001683:B005/m01`); transgressive rupture (`quranic:root_001132:B004/m01`); covering and denial of truth (`quranic:root_001307:B003/m01`); coercion into disobedience (`quranic:root_001307:B007/m01`).
- Ayah anchors: 71:17 (`ن ب ت`); 71:21, 71:24, and 71:28 (`ز ي د`); 71:24 and 71:27 (`ض ل ل`); 71:24 (`ك ث ر`); 71:26-27 (`ك ف ر`); 71:27 (`و ل د`, `ف ج ر`).
- Synthesis: The process has both horizontal and vertical propagation. Deviation spreads through many contemporaries, then childbirth and derivation carry it into another generation. Forgetting and loss show how guidance disappears from transmission, while coercion explains how a formed social system can make later disobedience easier.

### 13. [P2 71:15-28] The Plot Is Cultivated Beneath a Treated Surface
- Semantic invariant: A destructive plan develops through hidden preparation, managed inputs, and a surface that conceals the condition of what is ripening underneath.
- Surface relation: direct and indirect; 71:22 anchors plotting; 71:17 anchors growth from earth; 71:26-27 anchors concealed denial and its generated outcome.
- Surprising reach: Plotting becomes an agricultural and cosmetic operation: water the hard ground, grow the plant, coat the exterior, and discover rot in the fruit.

#### Subchannel A. Concealed defect is covered by a persuasive finish
- Reading type: latent/lexical
- Scene or process: An internal fault is held beneath an applied surface that improves appearance while obscuring what lies inside.
- Active motifs: inward corruption, deceit, and hostility (`quranic:root_000464:B004/m01`); concealed interior and confidence (`quranic:root_000464:B003/m01`); interpenetrating internal parts (`quranic:root_000464:B008/m01`); planning and arranging by night (`quranic:root_000166:B004/m01`); chief share of a great affair (`quranic:root_001281:B002/m01`); ochre coating (`quranic:root_001438:B004/m01`); cosmetic plaster or depilatory coating (`quranic:root_001564:B009/m01`); covering and concealment (`quranic:root_001307:B001/m01`); denial that hides truth (`quranic:root_001307:B003/m01`); visible appearance or mirror (`quranic:root_000531:B006/m01`).
- Ayah anchors: 71:15 (`ر ء ي`); 71:22 (`م ك ر`, `ك ب ر`); 71:25 (`د خ ل`, `ن و ر`); 71:26-27 (`ك ف ر`); 71:28 (`د خ ل`, `ب ي ت`).
- Synthesis: The scene distinguishes substrate from finish. Corruption and hostility occupy the inward layer; ochre, cosmetic coating, and general covering occupy the visible layer. The plot's danger lies in the functional gap between those layers.

#### Subchannel B. Managed growth can culminate in rotten yield
- Reading type: latent/lexical
- Scene or process: Hard ground is watered, a named plant is raised, and apparently successful cultivation terminates in spoiled fruit.
- Active motifs: watering hard earth before cultivation (`quranic:root_001438:B005/m01`); irrigated plant or tree (`quranic:root_001438:B003/m01`); rotten ripe date (`quranic:root_001438:B006/m01`); date spoiled by cold before ripening (`quranic:root_001255:B004/m01`); waterskin spoiled under moonlight (`quranic:root_001255:B006/m01`); deliberate planting (`quranic:root_001465:B002/m01`); plant emerging from ground (`quranic:root_001465:B001/m01`); seed covered with earth (`quranic:root_001307:B008/m01`); fruit enclosed in its sheath (`quranic:root_001307:B010/m01`); palm heart or shoot (`quranic:root_001286:B006/m01`); fertile ground (`quranic:root_000025:B002/m01`).
- Ayah anchors: 71:16 (`ق م ر`); 71:17 (`ء ر ض`, `ن ب ت`); 71:22 (`م ك ر`); 71:24 (`ك ث ر`); 71:26-27 (`ك ف ر`).
- Synthesis: The cultivation is technically competent but teleologically corrupt. Watering, planting, seed-cover, and fruit-sheath all support growth, yet the final yield is rotten. This reframes the “great plot” as sustained investment in an outcome whose decay is internal to the process.

### 14. [P2 71:15-28] Cult Objects Bind Affection to Fabrication and Predation
- Semantic invariant: An idol gains social force by being made, named, loved, circled, and endowed with a predatory persona.
- Surface relation: direct; 71:23 anchors deity, Wadd, Suwa', and Nasr; 71:22 anchors the collective plot that sustains them; 71:24 anchors their misleading effect.
- Surprising reach: The cult object moves from plastered artifact and cherished name to beak, claw, thief, and raiding detachment.

#### Subchannel A. A fabricated object receives a name and ritual orbit
- Reading type: mixed
- Scene or process: Material is formed into an object, designated as a deity, and made the stationary center of repeated circling.
- Active motifs: deity made an object of worship (`quranic:root_000047:B001/m01`); name of the idol Wadd (`quranic:root_001634:B005/m01`); name of the idol Suwa' (`quranic:root_000760:B003/m01`); vulture as named cult figure (`quranic:root_001496:B002/m01`); circular orbit and enclosure (`quranic:root_000499:B001/m01`); stone, idol, or place circled in ritual (`quranic:root_000499:B006/m01`); clay mixed with straw as plaster (`quranic:root_000760:B004/m01`); making an object (`quranic:root_000248:B001/m01`); fabricated narrative (`quranic:root_000434:B007/m01`); name as designation and public standing (`quranic:root_000745:B005/m01`); crown that covers and elevates a ruler (`quranic:root_001307:B015/m01`).
- Ayah anchors: 71:15 (`خ ل ق`, `س م و`); 71:16 and 71:19 (`ج ع ل`); 71:23 (`ء ل ه`, `و د د`, `س و ع`, `ن س ر`); 71:26 (`د و ر`, `ك ف ر`).
- Synthesis: The object has maker, material, name, theological status, and ritual use. Plaster gives it a fabricated body; designation gives it identity; circling gives it a social center; and invented narrative secures its prestige. The scene sharply distinguishes manufactured centrality from inherent divinity.

#### Subchannel B. Affection and wish fasten worshipers to the name
- Reading type: latent/lexical
- Scene or process: Love, desire, and cherished expectation make a named object emotionally adhesive.
- Active motifs: affection and mutual attachment (`quranic:root_001634:B001/m01`); wishing for a desired outcome (`quranic:root_001634:B002/m01`); idol named Wadd (`quranic:root_001634:B005/m01`); worshipful subjection (`quranic:root_000973:B003/m01`); honoring and magnifying (`quranic:root_000973:B006/m01`); inward magnification (`quranic:root_001281:B003/m01`); elevated inherited prestige (`quranic:root_001281:B005/m01`).
- Ayah anchors: 71:22 (`ك ب ر`); 71:23 (`و د د`, `ء ل ه`); 71:27 (`ع ب د`).
- Synthesis: The name Wadd opens a complete affective mechanism. Love and wish attach the worshiper, honor raises the object, and inward magnification lets inherited prestige feel self-validating. Idolatry is thereby sustained by emotional investment as well as assertion.

#### Subchannel C. The vulture figure becomes a machinery of seizure
- Reading type: latent/lexical
- Scene or process: A predatory bird strips flesh with its beak, scales up into a raiding troop, and finally appears as a thief taking by stealth.
- Active motifs: snatching and stripping bit by bit (`quranic:root_001496:B001/m01`); predatory vulture (`quranic:root_001496:B002/m01`); tearing beak (`quranic:root_001496:B004/m01`); cavalry or troop that uproots what it meets (`quranic:root_001496:B005/m01`); thief who takes by stealth (`quranic:root_001496:B008/m01`); fraudulent victory in gambling (`quranic:root_001255:B007/m01`); circulating but unreliable report (`quranic:root_001272:B007/m01`); false attribution and invented claim (`quranic:root_001272:B005/m01`); abandonment and waste (`quranic:root_000760:B002/m01`).
- Ayah anchors: 71:16 (`ق م ر`); 71:21, 71:23, and 71:26 (`ق و ل`); 71:23 (`س و ع`, `ن س ر`).
- Synthesis: Beak, stripping action, troop, and thief share a single predatory invariant at increasing scales. Fraudulent play and false report provide social tools for the same seizure. The idol that is cherished as a protector is lexically reframed as an extraction system.

### 15. [P2 71:15-28] Covering Divides Denial, Burial, and Mercy
- Semantic invariant: Covering changes what remains available to sight, memory, consequence, or protection; its moral force depends on what is covered and for what end.
- Surface relation: direct; 71:25 anchors engulfment and entry into fire; 71:26-27 anchors denial; 71:28 anchors forgiveness, faith, and protected entry.
- Surprising reach: Seed-cover, truth-cover, grave, flood, expiation, and forgiveness are materially similar operations with opposed outcomes.

#### Subchannel A. Denial covers truth and benefit at their source
- Reading type: mixed
- Scene or process: A subject places a screen over disclosed truth and over the benefit already received, preventing acknowledgment from reaching either.
- Active motifs: general covering (`quranic:root_001307:B001/m01`); denial and concealment of truth (`quranic:root_001307:B003/m01`); covering a benefit by ingratitude (`quranic:root_001307:B004/m01`); darkness or vast water as engulfing cover (`quranic:root_001307:B002/m01`); seed hidden by soil (`quranic:root_001307:B008/m01`); withdrawal and disavowal (`quranic:root_001307:B005/m01`); transgressive rupture of a protective boundary (`quranic:root_001132:B004/m01`).
- Ayah anchors: 71:26-27 (`ك ف ر`); 71:27 (`ف ج ر`).
- Synthesis: Covering moves from physical screen to epistemic and ethical operation. Truth is made unavailable, benefit is detached from gratitude, and disavowal removes relational responsibility. Seed-cover shows that concealment can serve life, which exposes denial's distortion: it covers not to protect emergence but to prevent recognition.

#### Subchannel B. Engulfment hides body, route, and memory
- Reading type: mixed
- Scene or process: Water, earth, or darkness occupies the subject's whole field until location, route, and retained trace disappear.
- Active motifs: sinking under water to destruction (`quranic:root_001080:B001/m01`); total occupation of a field (`quranic:root_001080:B005/m01`); ground filled with water (`quranic:root_001080:B003/m01`); disappearance and burial (`quranic:root_000913:B002/m01`); loss of location (`quranic:root_000913:B003/m01`); loss from memory (`quranic:root_000913:B004/m01`); remote grave or settlement (`quranic:root_001307:B012/m01`); lower realm beneath another (`quranic:root_000502:B001/m01`); entering an enclosing state (`quranic:root_000464:B001/m01`).
- Ayah anchors: 71:18 (`خ ر ج` as the counter-operation); 71:24 and 71:27 (`ض ل ل`); 71:25 (`غ ر ق`, `د خ ل`, `د و ن`); 71:26-27 (`ك ف ر`).
- Synthesis: Immersion does more than kill. It removes coordinates, interrupts the route, suppresses the trace, and turns the surrounding medium into a total cover. The later promise of exit from earth stands as the exact counter-operation to this disappearance.

#### Subchannel C. Mercy covers fault while preserving the person
- Reading type: mixed
- Scene or process: A fault is covered in a way that removes its punitive effect without erasing the subject, who is instead admitted into security.
- Active motifs: preserving cover (`quranic:root_001096:B001/m01`); forgiveness shielding from sin's effect (`quranic:root_001096:B002/m01`); expiation that covers an offense (`quranic:root_001307:B009/m01`); security and trust (`quranic:root_000054:B001/m01`); assent that settles the heart (`quranic:root_000054:B002/m01`); prayer for response (`quranic:root_000054:B003/m01`); entering an interior (`quranic:root_000464:B001/m01`); dwelling as refuge (`quranic:root_000166:B001/m01`).
- Ayah anchors: 71:25 and 71:28 (`د خ ل`); 71:28 (`غ ف ر`, `ء م ن`, `ب ي ت`); 71:26-27 (`ك ف ر`).
- Synthesis: Merciful covering preserves identity and relationship. Expiation removes the offense's operative trace, trust settles the entrant, and the house receives rather than obliterates the person. This is the opposite of engulfment: the fault disappears while the subject remains locatable and sheltered.

### 16. [P2 71:15-28] Judgment Closes Every Exit and Settles the Account
- Semantic invariant: Terminal judgment occupies the subject's environment, removes assistance and alternatives, and converts accumulated wrong into irreversible loss.
- Surface relation: direct; 71:21 anchors loss; 71:24 anchors wrong and increased error; 71:25 anchors drowning, fire, failed finding, and absent helpers; 71:28 anchors destruction.
- Surprising reach: Water, fire, accounting, broken material, failed search, and denied redress converge on one terminal condition.

#### Subchannel A. Immersion and fire form consecutive enclosures
- Reading type: surface-primary
- Scene or process: Water first closes the outer field by engulfment; entry then transfers the subject into a second enclosing medium of fire.
- Active motifs: drowning and submersion (`quranic:root_001080:B001/m01`); killing by drowning (`quranic:root_001080:B002/m01`); total occupation and engulfment (`quranic:root_001080:B005/m01`); decorated bridle wholly covered by its material (`quranic:root_001080:B008/m01`); entry into an interior (`quranic:root_000464:B001/m01`); fire and consuming flame (`quranic:root_001564:B002/m01`); lower or nearer enclosing realm (`quranic:root_000502:B001/m01`); no alternative besides the enclosing thing (`quranic:root_000502:B003/m01`).
- Ayah anchors: 71:25 (`غ ر ق`, `د خ ل`, `ن و ر`, `د و ن`).
- Synthesis: The sequence is spatially exact. Drowning fills the first medium until no external field remains; entry then crosses into fire, a second total environment. The fully overlaid bridle provides a shape analogy for engulfment: nothing of the underlying object escapes the covering material.

#### Subchannel B. Search finds neither capacity nor helper
- Reading type: mixed
- Scene or process: A distressed subject searches for an available resource, ally, or alternative but encounters absence at every role.
- Active motifs: finding and reaching a sought thing (`quranic:root_001626:B001/m01`); material capacity and means (`quranic:root_001626:B003/m01`); grief and distressed attachment (`quranic:root_001626:B004/m01`); anger and grievance (`quranic:root_001626:B005/m01`); aid that overcomes an enemy (`quranic:root_001510:B001/m01`); self-redress after oppression (`quranic:root_001510:B002/m01`); rescuing rain and relief (`quranic:root_001510:B004/m01`); aid as a granted good (`quranic:root_001510:B005/m01`); tributary carrying water from afar (`quranic:root_001510:B007/m01`); alternate or substitute (`quranic:root_000502:B003/m01`); low or inadequate thing (`quranic:root_000502:B002/m01`); security and reliable trust (`quranic:root_000054:B001/m01`).
- Ayah anchors: 71:25 (`و ج د`, `ن ص ر`, `د و ن`); 71:28 (`ء م ن`).
- Synthesis: Finding requires a target, capacity requires usable means, and aid requires another agent. Judgment removes all three. Emotion remains, but it cannot become resource, substitute, or redress. The contrast with secure believers makes the absence relational as well as material.

#### Subchannel C. Wrong resolves into deficit, breakage, and dust
- Reading type: mixed
- Scene or process: Misplaced action accumulates as a deficient account and ends in the physical breakup of what had seemed valuable or durable.
- Active motifs: general diminution (`quranic:root_000409:B001/m01`); lost commercial capital (`quranic:root_000409:B002/m01`); deficient measure (`quranic:root_000409:B003/m01`); revenue paid out (`quranic:root_000400:B003/m01`); partners or heirs dividing shares (`quranic:root_000400:B012/m01`); written register or ledger (`quranic:root_000502:B005/m01`); missing the right direction (`quranic:root_000420:B001/m01`); deliberate offense (`quranic:root_000420:B002/m01`); grievance seeking redress (`quranic:root_000967:B003/m01`); putting a thing in the wrong place or time (`quranic:root_000967:B004/m01`); withholding a right (`quranic:root_000967:B008/m01`); destruction and fragmentation (`quranic:root_000174:B001/m01`); precious material reduced to unworked fragments (`quranic:root_000174:B002/m01`).
- Ayah anchors: 71:18 (`خ ر ج`); 71:21 (`خ س ر`); 71:24 and 71:28 (`ظ ل م`); 71:25 (`خ ط ء`, `د و ن`); 71:28 (`ت ب ر`).
- Synthesis: Wrong is first a directional error, then a misplacement or withheld right, then a measurable deficit. Destruction finally translates the account into matter: fashioned value is broken back into fragments. The terminal loss is both juridical and material.

### 17. [P2 71:15-28] Household Continuity Forks Into Corrupt and Believing Succession
- Semantic invariant: A household transmits identity through birth, upbringing, following, and admission; the transmitted direction can reproduce rebellion or secure trust.
- Surface relation: direct; 71:21 anchors wealth and children under corrupt following; 71:27 anchors offspring characterized by transgression and denial; 71:28 anchors parents, believing men and women, and entry into the house.
- Surprising reach: Lineage is a transmission system rather than a guarantee: biological generation, fostered formation, social imitation, and house-entry can carry opposed inheritances.

#### Subchannel A. Birth can reproduce an already corrupted pattern
- Reading type: mixed
- Scene or process: Existing rebellion shapes upbringing and succession so that a new child emerges inside the same moral trajectory.
- Active motifs: childbirth (`quranic:root_001683:B003/m01`); child and descendant (`quranic:root_001683:B001/m01`); derivative generated from a prior source (`quranic:root_001683:B005/m01`); new generation within a people (`quranic:root_001465:B003/m01`); human upbringing (`quranic:root_001465:B006/m01`); low and debased growth (`quranic:root_001465:B008/m01`); following and imitation (`quranic:root_000175:B001/m01`); uninterrupted succession (`quranic:root_000175:B004/m01`); departure from obedience (`quranic:root_001022:B001/m01`); transgressive rupture (`quranic:root_001132:B004/m01`); denial of truth (`quranic:root_001307:B003/m01`).
- Ayah anchors: 71:17 (`ن ب ت`); 71:21 (`ت ب ع`, `ع ص ي`, `و ل د`); 71:26-27 (`ك ف ر`); 71:27 (`و ل د`, `ف ج ر`).
- Synthesis: Biology supplies continuity, but following and upbringing give that continuity direction. The child is a derivative in both bodily and social senses, so entrenched rebellion can enter the next generation before it appears as an independent choice.

#### Subchannel B. Parental and foster care can redirect formation
- Reading type: latent/lexical
- Scene or process: Parents and caregivers sustain a developing child through gradual repair, nourishment, and responsible oversight.
- Active motifs: father and mother as sources of birth (`quranic:root_001683:B002/m01`); young child (`quranic:root_001683:B004/m01`); same-age peer (`quranic:root_001683:B006/m01`); gradual repair and upbringing (`quranic:root_000532:B002/m01`); lordly care and ownership (`quranic:root_000532:B001/m01`); human growth and education (`quranic:root_001465:B006/m01`); liability that follows an act (`quranic:root_000175:B006/m01`); household and dependents (`quranic:root_000166:B002/m01`).
- Ayah anchors: 71:17 (`ن ب ت`); 71:21 (`ت ب ع`, `و ل د`); 71:21, 71:26, and 71:28 (`ر ب ب`); 71:28 (`ب ي ت`).
- Synthesis: Upbringing is a role-governed process: parent, child, peer, caregiver, household, and responsibility all participate. The same lineage that can transmit corruption therefore contains a mechanism for guided formation, which is why moral inheritance is not biologically fixed.

#### Subchannel C. Faith admits kin and community into a protected house
- Reading type: surface-primary
- Scene or process: Trusted entrants cross into a dwelling where kinship and shared assent define a secure community.
- Active motifs: dwelling and refuge (`quranic:root_000166:B001/m01`); household and dependents (`quranic:root_000166:B002/m01`); inherited household standing (`quranic:root_000166:B008/m01`); entry into an interior (`quranic:root_000464:B001/m01`); security and trust (`quranic:root_000054:B001/m01`); faith as settled assent (`quranic:root_000054:B002/m01`); prayer seeking response (`quranic:root_000054:B003/m01`); parents (`quranic:root_001683:B002/m01`); child or descendant (`quranic:root_001683:B001/m01`); forgiveness preserving the entrant (`quranic:root_001096:B002/m01`).
- Ayah anchors: 71:25 and 71:28 (`د خ ل`); 71:28 (`ب ي ت`, `ء م ن`, `و ل د`, `غ ف ر`).
- Synthesis: House-entry integrates spatial, familial, and confessional belonging. Trust qualifies the entrant, forgiveness preserves rather than excludes, and kinship is widened to believing men and women. This is a deliberately formed succession opposed to the lineage of 71:27.

## Standalone Subchannels

### S1. [P1 71:1-14] Affliction Gathers Like a Relapsing Wound
- Reading type: latent/lexical
- Scene or process: Pain localizes in a wound, discharge accumulates, temporary improvement reverses, and the injury acquires a due compensation.
- Active motifs: felt pain (`quranic:root_000046:B001/m01`); inflicted pain (`quranic:root_000046:B002/m01`); painful neck disorder (`quranic:root_000016:B006/m01`); collected pus in a wound (`quranic:root_000281:B006/m01`); wound discharge (`quranic:root_000282:B003/m01`); suppuration extending through a wound (`quranic:root_001407:B007/m01`); relapse after improvement (`quranic:root_001096:B004/m01`); wound carrying a due compensation (`quranic:root_001488:B003/m01`); punitive affliction (`quranic:root_000994:B005/m01`).
- Ayah anchors: 71:1 (`ء ل م`, `ع ذ ب`, `ن ذ ر`); 71:2 (`ن ذ ر`); 71:4 (`ء ج ل`, `ج ي ء`, `غ ف ر`); 71:12 (`م د د`).
- Synthesis: The scene gives warning a somatic timescale. Pain becomes a localized lesion; the lesion fills and extends; apparent recovery can relapse; and injury creates an accountable due. Affliction is thus both a bodily process and an unresolved claim.

### S2. [P1 71:1-14] The Envoy Crosses a Community Boundary Without Ceasing to Belong
- Reading type: latent/lexical
- Scene or process: A message-bearer moves across the line between insider and outsider, entering a group while addressing it through kinship and shared relation.
- Active motifs: stranger entering a people not his own (`quranic:root_000009:B006/m01`); human kin group (`quranic:root_001273:B001/m01`); group facing one another (`quranic:root_001198:B009/m01`); lineage and attribution to an origin (`quranic:root_000156:B007/m01`); separation after connection (`quranic:root_000170:B001/m01`); bond connecting parties (`quranic:root_000170:B003/m01`); message-bearing envoy (`quranic:root_000563:B002/m01`); general calling that inclines another (`quranic:root_000478:B001/m01`).
- Ayah anchors: 71:1 (`ء ت ي`, `ر س ل`, `ق و م`, `ق ب ل`); 71:2 (`ب ي ن`, `ق و م`); 71:5 (`د ع و`, `ق و م`); 71:12 (`ب ن ي`).
- Synthesis: Stranger, kin group, lineage, separation, bond, and envoy define a social threshold. The messenger's authority does not depend on being socially alien, yet his commission gives him a word that crosses the group's established boundary. The scene holds intimacy and disruptive exteriority together.

### S3. [P2 71:15-28] Ordered Sevenfold Multiplicity Casts a Predatory Shadow
- Reading type: latent/lexical
- Scene or process: The same root that counts an ordered seven also names predators, verbal mauling, and taking carried to an extreme.
- Active motifs: sevenfold number and multiplication (`quranic:root_000669:B001/m01`); predatory beast (`quranic:root_000669:B002/m01`); verbal attack modeled on a beast's bite (`quranic:root_000669:B003/m01`); extreme taking or punishment (`quranic:root_000669:B005/m01`); vulture predator (`quranic:root_001496:B002/m01`); snatching and stripping (`quranic:root_001496:B001/m01`); magnitude and greatness (`quranic:root_001281:B001/m01`); numerical abundance (`quranic:root_001286:B001/m01`).
- Ayah anchors: 71:15 (`س ب ع`); 71:22 (`ك ب ر`); 71:23 (`ن س ر`); 71:24 (`ك ث ر`).
- Synthesis: The same-root transformation is sharply contrastive. Seven orders a layered cosmos; the predatory senses turn multiplicity into devouring force and excess into terminal taking. Ordered magnitude above pressures the crowd's claim to greatness below.

### S4. [P2 71:15-28] Justice Begins as Correct Placement and Ends as Redress
- Reading type: latent/lexical
- Scene or process: A wrong puts action, time, measure, or property out of place; a claim then seeks restoration from the one who withheld it.
- Active motifs: missing the correct direction (`quranic:root_000420:B001/m01`); deliberate offense (`quranic:root_000420:B002/m01`); grievance and demand for equity (`quranic:root_000967:B003/m01`); putting a thing in the wrong time or place (`quranic:root_000967:B004/m01`); withholding a right (`quranic:root_000967:B008/m01`); claimant pursuing a due (`quranic:root_000175:B005/m01`); liability following an act (`quranic:root_000175:B006/m01`); deficient measure (`quranic:root_000409:B003/m01`); self-redress after oppression (`quranic:root_001510:B002/m01`); aid that manifests against an adversary (`quranic:root_001510:B001/m01`).
- Ayah anchors: 71:21 (`ت ب ع`, `خ س ر`); 71:24 and 71:28 (`ظ ل م`); 71:25 (`خ ط ء`, `ن ص ر`).
- Synthesis: The scene moves from error to claim. Wrong is first a deviation or misplacement, then a short measure or withheld right, then a liability that follows the actor. Redress restores relation and measure, explaining why the absence of helpers in 71:25 is also the absence of any available mechanism of vindication.

### S5. [P2 71:15-28] Transgression Breaches an Enclosure and Releases What It Held
- Reading type: mixed
- Scene or process: A containing boundary splits open, releasing light, water, a sudden mass, or conduct that had been held within a norm.
- Active motifs: broad splitting and bursting water (`quranic:root_001132:B001/m01`); dawn breaking out of night (`quranic:root_001132:B002/m01`); sudden influx of a great mass (`quranic:root_001132:B003/m01`); moral deviation and rupture of restraint (`quranic:root_001132:B004/m01`); historical violation of protected sanctity (`quranic:root_001132:B006/m01`).
- Ayah anchors: 71:27 (`ف ج ر`).
- Synthesis: The same-root senses preserve one operation across physical, temporal, social, and ethical settings. Water bursts from confinement, dawn splits night, a crowd breaks suddenly upon a place, and transgression ruptures a norm. The wicked offspring of 71:27 are therefore figured not only as immoral persons but as continuing breaches through which disorder is released.

### S6. [Whole-surah 71:1-28] A Household Is Built, Entered, Severed, and Reopened to Courtship
- Reading type: latent/lexical
- Scene or process: Marriage establishes a house through a socially marked entry and consummation; divorce can then cut the right of return, after which a formerly married woman may receive new courtship messages.
- Active motifs: building upon one's wife, entering the marriage, and erecting the bridal pavilion (`quranic:root_000156:B006/m01`); marriage as building a house upon a woman at entry (`quranic:root_000166:B010/m01`); marital consummation expressed through entry (`quranic:root_000464:B002/m01`); intercourse expressed euphemistically as coming over a woman (`quranic:root_001088:B004/m01`); the status of a previously married person after consummation or return from a spouse (`quranic:root_000209:B005/m01`); irrevocable divorce that cuts the possibility of return (`quranic:root_000170:B012/m01`); a divorced or widowed woman receiving messages from suitors (`quranic:root_000563:B009/m01`).
- Ayah anchors: 71:1 and 71:11 (`ر س ل`); 71:2 (`ب ي ن`); 71:7 (`ث و ب`, `غ ش و`); 71:12 (`ب ن ي`); 71:25 and 71:28 (`د خ ل`); 71:28 (`ب ي ت`).
- Synthesis: This scene reframes the children of 71:12 and the house of 71:28 as products of an enacted and legally vulnerable bond, not automatic biological continuity. Building, entry, and consummation establish a household; irrevocable separation can dismantle that relation; renewed courtship can begin another. It usefully pressures the surah's opposed lineages by showing that household transmission depends on bonds that must be formed and maintained.

### S7. [Whole-surah 71:1-28] A Night Ration Is Gathered, Measured, and Kept
- Reading type: latent/lexical
- Scene or process: Ripening dates are gathered into a woven palm container, food is apportioned for one night, and water or milk is kept cool and served in a small measured draught.
- Active motifs: dates beginning to ripen from the tail end (`quranic:root_000521:B005/m01`); woven palm-leaf basket made to hold fresh dates (`quranic:root_000464:B010/m01`); known dry measure used to portion food (`quranic:root_001407:B006/m01`); food sufficient for one night (`quranic:root_000166:B005/m01`); water or milk kept and cooled overnight in its vessel (`quranic:root_000166:B006/m01`); small draught or cup of milk or drink (`quranic:root_001080:B006/m01`).
- Ayah anchors: 71:4 (`ذ ن ب`); 71:12 (`م د د`); 71:25 (`غ ر ق`, `د خ ل`); 71:28 (`د خ ل`, `ب ي ت`).
- Synthesis: The scene materializes the rain, gardens, wealth, and household of the primary reading as the ordinary work that converts yield into sustenance: gathering, containing, measuring, keeping, and serving. It also pressures reliance on abundance in 71:21. Possession is not yet provision; increase becomes life-supporting only when it is timed, bounded, and distributed.

### S8. [Whole-surah 71:1-28] A Bow Stores Force in the Gap Between Bow and String
- Reading type: latent/lexical
- Scene or process: The bow's working geometry is established by controlling the distance between its body and string; the arched instrument is then drawn to its limit so that the arrow can travel far.
- Active motifs: bow clinging so tightly to its string that it nearly breaks (`quranic:root_000156:B005/m01`); bowstring standing apart from the belly of the bow (`quranic:root_000170:B008/m01`); arched bow formed by raising the string away from its body (`quranic:root_001131:B003/m01`); reaching the extreme of the draw so the arrow travels far (`quranic:root_001080:B004/m01`).
- Ayah anchors: 71:2 (`ب ي ن`); 71:12 (`ب ن ي`); 71:20 (`ف ج ج`); 71:25 (`غ ر ق`).
- Synthesis: This compact mechanism materializes the surah's warning and appointed delay as stored rather than absent force: a bow may already be fully drawn while release remains prospective. It also reframes separation. Too little gap threatens breakage, while controlled distance creates reach, so the interval before consequence is functional tension rather than cancellation.

### S9. [Whole-surah 71:1-28] A Familiar, Lot Case, and Face-Turning Charm Form a Diviner's Apparatus
- Reading type: latent/lexical
- Scene or process: A familiar jinn supplies divinatory or medicinal disclosure, lots are kept together in a leather case, and a sorcerer's bead is used to redirect one person's face toward another.
- Active motifs: familiar jinn who appears to a person or shows divination and medicine (`quranic:root_000531:B008/m01`); leather container holding lots or gambling arrows (`quranic:root_000532:B010/m01`); bead made or hung by a sorcerer to turn one face toward another (`quranic:root_001198:B016/m01`).
- Ayah anchors: 71:1 (`ق ب ل`); 71:5, 71:10, 71:21, 71:26, and 71:28 (`ر ب ب`); 71:15 (`ر ء ي`).
- Synthesis: The apparatus materializes the cultic plot of 71:22-24 as a practical system for claiming hidden knowledge, allocating chance, and engineering attachment. It usefully pressures the primary reading of cherished named idols: orientation toward an object can be manufactured by instruments and intermediaries rather than warranted by truth.

### S10. [P1 71:1-14 -> P2 71:15-28 | causal reversal: wear -> turnover -> return -> re-existence] Material Form Wears, Turns, and Reappears
- Reading type: latent/lexical
- Scene or process: A garment wears thin and loses its nap; conditions turn; a matter returns to its beginning; and what had been absent comes into existence again.
- Active motifs: garment worn, torn, and stripped of its nap through use (`quranic:root_000434:B009/m01`); conditions and affairs circulating through changing states (`quranic:root_000499:B003/m01`); a matter or span of time returning to its beginning (`quranic:root_001142:B003/m01`); a thing existing again after nonexistence (`quranic:root_001626:B002/m01`).
- Ayah anchors: 71:6 (`ف ر ر`); 71:14-15 (`خ ل ق`); 71:25 (`و ج د`); 71:26 (`د و ر`).
- Synthesis: The P1-to-P2 bridge is a causal reversal through material state-change. P1 supplies worn created form and return to origin; P2 supplies circulating conditions and existence after absence. Together they support the surah's return and raising sequence by separating deterioration of form from cancellation of existence: wear and changing states become stages in a circuit whose disappearance can reverse.


