Surah: 96. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S96 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s096/surah.r2/text.md =====
# Surah 96

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/s096/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ر ء (root_001210): 96:1 ٱقْرَأْ, 96:3 ٱقْرَأْ

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

## ق ر ء (root_001211): 96:1 ٱقْرَأْ, 96:3 ٱقْرَأْ

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

## س م و (root_000745): 96:1 بِٱسْمِ

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

## و س م (root_001650): documented alternative for 96:1 بِٱسْمِ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı

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

## ر ب ب (root_000532): 96:1 رَبِّكَ, 96:3 وَرَبُّكَ, 96:8 رَبِّكَ

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

## ECHO ر ب و (root_000537): for 96:1 رَبِّكَ, 96:3 وَرَبُّكَ, 96:8 رَبِّكَ: withheld observed target; not identity

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

## خ ل ق (root_000434): 96:1 خَلَقَ, 96:2 خَلَقَ

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

## ء ن س (root_000059): 96:2 ٱلْإِنسَٰنَ, 96:5 ٱلْإِنسَٰنَ, 96:6 ٱلْإِنسَٰنَ

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

## ع ل ق (root_001039): 96:2 عَلَقٍ

- **B001** takılma ve bağlı kalma — bir şeye takılıp kalmak · bir şeyi başka bir şeye asmak · kapıyı yerine takıp kurmak · askı parçası veya kapı sürgüsü · kamçı, yay ya da kılıç askısı · kabı asmaya yarayan bağ · kolye ve küpe askı süsleri · göç imkanı kalmayacak biçimde yerleşmek · dikilen fidanın tutması · öldürülen kişinin kan sorumluluğunun birine yüklenmesi
  يناط الشيء بالشيء العالي (maqayis)؛ علق به إذا لزمه (maqayis)؛ علق بالشيء نشب به (ayn)؛ كل شيء علق به شيء فهو معلاقه (ayn;sihah;tahdhib)؛ تعليق الباب نصبه وتركيبه (ayn;tahdhib)؛ علق القربة الذي تشد به ثم تعلق (sihah;tahdhib)
- **B002** makara taşıyıcı su çekme düzeneği — makarayı taşıyan su çekme düzeneği
  العلق ما تعلق به البكرة من القامة (maqayis;ayn;sihah)؛ آلة البكرة (maqayis;sihah)؛ اسم جامع لجميع آلات الاستقاء بالبكرة (tahdhib)؛ الحبل المعلق بالبكرة (tahdhib)
- **B003** pıhtılaşmış kan ve kan emici su canlısı — koyu veya pıhtılaşmış kan · bir parça pıhtılaşmış kan · suda yaşayan kan emici sülük · boğazına sülük yapışmış kimse veya hayvan · su içerken boğazına sülük yapışmak
  العلق الدم الجامد والقطعة منه علقة (maqayis;ayn)؛ الدم الغليظ والقطعة منه علقة (sihah)؛ العلقة الدم الجامد الغليظ (tahdhib)؛ دويبة في الماء تجمع على علق (ayn;sihah)؛ أخذ العلق بحلقه (maqayis;ayn;tahdhib)
- **B004** kalbe yerleşen sevgi — kalbe yerleşen sevgi · bir kadına gönül vermek · kalıcı sevgi bağı · eşini seven ve ona bağlı kadın
  العلق الهوى (maqayis;sihah)؛ نظرة من ذي علق أي ذي هوى (maqayis;sihah)؛ علقت فلانة أي أحببتها (ayn)؛ علاقة الحب (sihah)؛ العلاقة الهوى اللازم للقلب (tahdhib)؛ العلوق من النساء المحبة لزوجها (maqayis;ayn)
- **B005** yapışkan ve ısrarlı çekişme — biriyle çatışıp çekişmek · kişiye bağlı dava veya çekişme · sert ve ısrarlı tartışmacı · tartışmada etkili dil · birine diliyle saldırmak
  علق فلان بفلان خاصمه (maqayis;ayn)؛ العلاقة الخصومة (maqayis)؛ علاقة الخصومة (sihah)؛ رجل معلاق إذا كان شديد الخصومة (maqayis;ayn;sihah;tahdhib)؛ الدعوى يقال لها علاقة (tahdhib)؛ علقه إذا تناوله بلسانه (tahdhib)
- **B006** yaşamı sürdürecek az besin — hayvanın yetindiği kıt otlak · yaşamı sürdürecek az yiyecek · devenin ağzıyla koparıp yediği ot · meyveleri ağzıyla alıp yemek · hayvana asılan yem veya ağaca sarılan bitki · devenin otladığı bir bitki · azla yetinen, seçerek yaşayan gibi değildir
  العلاق الذي يجتزىء به الماشية من الكلأ (maqayis)؛ ما يأكل فلان إلا علقة أي ما يمسك نفسه (maqayis)؛ كل شيء يتبلغ به فهو علقة (ayn;sihah)؛ العلقة من الطعام القليل الذي يتبلغ به (tahdhib)؛ العلوق ما تعلقه الإبل أي ترعاه (maqayis;ayn;sihah;tahdhib)؛ تعلق من ثمار الجنة أي تناول بأفواهها (sihah;tahdhib)
- **B007** elden çıkarılmaya kıyılmayan değerli şey — elden çıkarılmaya kıyılmayan değerli şey · özenle sakınılan değerli şey · değerli sayılan bir içki veya hurma içkisi
  هذا علق من الأعلاق للشيء النفيس (maqayis)؛ علق مضنة ومضنة (maqayis;sihah;tahdhib)؛ العلق المال الذي يكرم عليك تضن به (ayn)؛ العلق بالكسر النفيس من كل شيء (sihah)؛ يقال للشراب عليق (ayn;tahdhib)
- **B008** evlilikte askıda bırakılmış kadın — evlilikte askıda bırakılmış kadın · konuşursa boşanır, susarsa askıda kalır
  كالمعلقة هي التي لا تكون أيما ولا ذات بعل (maqayis)؛ المعلقة من النساء التي فقد زوجها (sihah)؛ امرأة معلقة إذا لم ينفق عليها زوجها ولم يطلقها فهي لا أيم ولا ذات بعل (tahdhib)؛ إن أنطق أطلق وإن أسكت أعلق (maqayis)
- **B009** döllenmenin tutup gebeliğin başlaması — kadının gebe kalması · döllenmesi tutmuş dişi veya erkek üreme sıvısı
  علقت المرأة حبلت (maqayis;sihah)؛ العلوق التي قد علقت لقاحا (ayn)؛ علقت وعقدت على الماء (tahdhib)؛ العلوق ماء الفحل (tahdhib)
- **B010** yavruyu benimsemeyip sütünü esirgeyen deve — yavruyu benimsemeyip sütünü esirgeyen deve · yavruyu benimsemeyen veya süt vermeyen develer · başkasının çocuğunu emziren kadın
  العلوق الناقة التي تأبى أن ترأم ولدها (maqayis)؛ من النوق التي تألف الفحل ولا ترأم البو (ayn)؛ المرأة إذا أرضعت ولد غيرها يقال لها علوق (ayn)؛ العلوق والمعالق الناقة تعطف على غير ولدها فلا ترأمه (sihah)؛ ناقة علوق إذا رئمت بأنفها ومنعت درتها (tahdhib)
- **B011** avın tuzağa takılıp yakalanması — ceylanın veya avın tuzağa takılması · avcının tuzağına av düşmesi
  علق الظبي في الحبالة يعلق إذا نشق فيها (maqayis)؛ أعلق الحابل إذا وقع في حبالته الصيد (maqayis)؛ علق الظبي في الحبالة (sihah)؛ أعلقت فأدرك أي علق الصيد في حبالتك (sihah)
- **B012** biçime bağlı adlandırmalar — sülüğü kan emmesi için bedene yerleştirme · çocuğun boğazındaki hastalıklı bölgeyi parmakla tedavi etme
  أعلقت الأم من عذرة الصبي بيدها (maqayis)؛ الإعلاق إرسال العلق على الموضع ليمص الدم (sihah)؛ الإعلاق أيضا الدغر (sihah)؛ معالجة عذرة الصبي ورفعها بالإصبع (tahdhib)؛ غمز حلق الصبي المعذور (tahdhib)
- **B013** sahibi adına erzak getirmeye gönderilen yük hayvanı — sahibi adına erzak getirmeye gönderilen yük hayvanı
  العليقة الدابة تدفع إلى الرجل ليمتار عليها لصاحبها (maqayis)؛ البعير يوجهه الرجل مع قوم يمتارون (sihah)؛ الناقة يعطيها الرجل القوم يمتارون (tahdhib)
- **B014** insanın peşini bırakmayan ağır bela — kişinin başına gelen büyük bela · insanı yakalayıp bırakmayan ölüm · belalar, ölümler veya insanı bağlayan uğraşlar
  جاء فلان بعلق فلق أي بداهية (maqayis;sihah;tahdhib)؛ أعلق وأفلق (maqayis;tahdhib)؛ المنية علوق (maqayis;sihah;tahdhib)؛ العلق الدواهي والمنايا والأشغال (tahdhib)
- **B015** bele kadar inen küçük üst giysisi — bele veya göbeğe kadar inen küçük üst giysisi
  العلقة قميص يكون إلى السرة (maqayis)؛ ثوب صغير وهو أول ثوب يتخذ للصبي (sihah)؛ العلقة الإتب (tahdhib)؛ الصدرة تلبسها الجارية (tahdhib)
- **B016** bir eylemi yapmaya koyulmak — belirtilen eylemi yapmaya koyulmak
  علق يفعل كذا كأنه يتعلق بالأمر الذي يريده (maqayis)؛ علق فلان يفعل كذا أي طنق وصار (ayn)؛ علق يفعل كذا مثل طفق (sihah)؛ علق فلان يفعل كذا كقولك طفق يفعل كذا (tahdhib)؛ يقال أحبه واعتاده (sihah)

## ك ر م (root_001294): 96:3 ٱلْأَكْرَمُ

- **B001** övgüye değer soyluluk, eli açıklık ve onurlandırma — soyluluk, eli açıklık ve övgüye değer huy · soylu, eli açık, bağışlayıcı; kendi türünde seçkin · soylular; seçkin ve övgüye değer olanlar · onurlandırdı veya değerli kıldı · onurlandırma ve incitmeden değerli yarar sağlama · onurlandırma; saygınlık · ayıp ve utanç verici şeylerden uzak durdu · soylu ve değerli çocukları oldu · değerli bir bağ ya da varlık edindi · yumuşak ve saygılı söz · kendi alanında yararlı ve övgüye değer tür · içerdiği yol gösterme, açıklama, bilgi ve bilgelikle övgüye değer kitap · içeriği güzel, saygın ya da mühürlü yazı · en soylu ve en erdemli · güzel ve saygın giriş yeri
  شرف في الشيء في نفسه أو شرف في خلق من الأخلاق (maqayis)؛ الكريم الصفوح (maqayis;sihah)؛ الكرم شرف الرجل (ayn)؛ تكرم عن الشائنات أي تنزه (ayn;tahdhib)؛ الكرم ضد اللؤم (sihah)؛ أتى بأولاد كرام واستحدث علقا كريما (sihah)؛ الكثير الخير الجواد المنعم المفضل (tahdhib)؛ اسم جامع لكل ما يحمد (tahdhib)؛ الأخلاق والأفعال المحمودة (mufradat)؛ كل شيء شرف في بابه (mufradat)
- **B002** yağmur getirme ve toprağın verimli oluşu [kalıp] — bulut yağmur getirdi ve suyunu bolca verdi · bitkisi gür, toprağı iyi ve taşları ayıklanmış arazi · toprağı işlenip gübrelendikten sonra bitkisi gürleşti
  كرم السحاب أتى بالغيث (maqayis;sihah)؛ أرض مكرمة للنبات إذا كانت جيدة النبات (maqayis;sihah)؛ إذا جاد السحاب بغيثه قيل كرم (ayn)؛ أرض مثارة منقاة من الحجارة (ayn;tahdhib)؛ البقعة الطيبة التربة العذاة المنبت بقعة مكرمة (tahdhib)؛ كرمت أرض فلان إذا دملها فزكا نبتها (tahdhib)
- **B003** boyun kolyesi — boyna takılan kolye veya dizili süs · kolyeler
  الكَرْم وهي القلادة (maqayis)؛ الكَرْم القلادة (ayn;sihah)؛ رأيت في عنقها كَرْما حسنا من لؤلؤ (sihah)؛ الكروم القلائد واحدها كَرْم (tahdhib)
- **B004** üzüm ve asma — üzüm, asma veya asmanın meyvesi · tek asma sürgünü veya bir asma
  الكَرْم فالعنب أيضا لأنه مجتمع الشعب منظوم الحب (maqayis)؛ الكرمة طاقة من الكرم (ayn)؛ الكَرْم كرم العنب (sihah)؛ الكرمة الطاقة الواحدة من الكرم (tahdhib)؛ يسمى الكرم كرما لأنه وصف بكرم شجرته وثمرته (tahdhib)
- **B005** kap ağzına konan tabak biçimli kapak — testi veya tencere ağzına konan tabak biçimli kapak
  الكرامة طبق يوضع على رأس الحب (ayn;sihah)؛ لطبق القدر والحب الكرامة (tahdhib)
- **B006** eli açıklıkta övünme yarışı ve üstün gelme — onunla eli açıklık konusunda övünme yarışına girdi · eli açıklıkta onu geçti
  كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه (sihah)
- **B007** uyluk kemiğinin kalça yuvasındaki yuvarlak başı — uyluk kemiğinin kalça yuvasındaki yuvarlak başı
  الكرمة رأس الفخذ المستدير كأنه جوزة تدور في قلت الورك (sihah)
- **B008** karşılık bekleyerek sunma ve övgüyü ödüllendirme — karşılığında ödül almak için onu sundu · kendisine yöneltilen övgüyü ödüllendiren kişi
  أكارم بها يهود أي أهديها إليهم فيثيبوني عليها (tahdhib)؛ أخ مكارم أي يكافئني على مدحي إياه (tahdhib)
- **B009** memnuniyetle kabul ve saygı bildiren kalıp yanıt [kalıp] — evet, memnuniyetle ve seve seve · senin için seve seve; sana duyduğum saygıyla
  نعم وحبا وكرامة (sihah)؛ نعم وحبا وكرما وحبا وكرمة (sihah)؛ أفعل ذلك وكرمة لك وكرمى لك وكرامة لك وكرما لك وكرمة عين (tahdhib)
- **B010** değer verilen varlık ve topluluğun seçkin kişisi — senin için çok değerli olan kişi veya şey · topluluğun soylu, saygın ve seçkin kişisi
  كل شيء يكرم عليك فهو كريمك وكريمتك (tahdhib)؛ الكريمة الرجل الحسيب (tahdhib)؛ إذا أتاكم كريمة قوم فأكرموه أي كريم قوم (tahdhib)؛ لا تدخر عنه شيئا يكرم عليك (tahdhib)

## ع ل م (root_001040): 96:4 عَلَّمَ, 96:5 عَلَّمَ, 96:5 يَعْلَمْ, 96:14 يَعْلَم

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

## ق ل م (root_001252): 96:4 بِٱلْقَلَمِ

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

## ط غ ي (root_000937): 96:6 لَيَطْغَىٰٓ

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

## ECHO ط غ و (root_000936): for 96:6 لَيَطْغَىٰٓ: withheld observed target; not identity

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

## ر ء ي (root_000531): 96:7 رَّءَاهُ, 96:9 أَرَءَيْتَ, 96:11 أَرَءَيْتَ, 96:13 أَرَءَيْتَ, 96:14 يَرَىٰ

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

## ECHO ر و ي (root_000615): for 96:7 رَّءَاهُ, 96:9 أَرَءَيْتَ, 96:11 أَرَءَيْتَ, 96:13 أَرَءَيْتَ, 96:14 يَرَىٰ: withheld observed target; not identity

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

## غ ن ي (root_001110): 96:7 ٱسْتَغْنَىٰٓ

- **B001** maddi bolluk ve ihtiyaçtan bağımsızlık — maddi zenginlik, bolluk ve ihtiyaçsızlık · varlıklı, zengin · zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek · ona ihtiyaç duymamak · onunla yetinip başka bir şeye ihtiyaç duymamak · bir şeye ihtiyaç duymama durumu · zenginlik ve bolluk · gönül tokluğu ve az şeye ihtiyaç duyma · zengin etmek veya yoksunluğunu gidermek · Kur'an'la yetinip başka bir şeye ihtiyaç duymamak
  الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)
- **B002** ihtiyacı karşılayıp yarar sağlama ve yerini tutma — yeterlilik, ihtiyacı karşılama ve yarar · onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak · bu sana yetmez ve yarar sağlamaz · yeterli ve ihtiyacı karşılayan · birinin yerini tutan yeterlilik ve işlev · zararını benden uzak tut
  الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)
- **B003** sesle ezgi söyleme, dinleme ve ezgili okuma — şarkı söyleme, ezgili seslendirme ve dinleti · şarkı; ezgili söylenen parça · şarkı söylemek · şarkı söylemek veya sesi ezgili ve duygulu kullanmak · Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak
  الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)
- **B004** bir yerde uzun süre kalıp yaşama — bir yerde oturmak ve uzun süre kalmak · sanki daha dün orada hiç yaşamamıştı · bir topluluğun oturduğu evler ve yurtlar · oturma eylemi veya oturulan yer
  غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)
- **B005** süsten bağımsız sayılan; bazen genç, güzel veya evli kadın — eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın · bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar
  الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)
- **B006** evlenme ve evlendirme — evlenme; bekâr kişi için koruyucu sayılan evlilik · gelinleri evlendirme
  الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)

## ر ج ع (root_000544): 96:8 ٱلرُّجْعَىٰٓ

- **B001** geri dönmek veya geri döndürmek — kendiliğinden önceki yere veya duruma dönmek · birini ya da bir şeyi yerine geri göndermek · başkasını geri döndürmek
  أصل كبير مطرد منقاس يدل على رد وتكرار (maqayis)؛ رجعت رجوعا ورجعته يستوي فيه اللازم والمجاوز (ayn)؛ رجعته إلى أهله أي رددته إليهم (jamhara)؛ رجع بنفسه رجوعا ورجعة غيره رجعا (sihah)؛ رجعته رجعا فرجع رجوعا (tahdhib)؛ الرجوع العود إلى ما كان منه البدء والرجع الإعادة (mufradat)
- **B002** ölümden sonra dönüş ve yeniden diriliş — Tanrı'ya dönüş veya nihai varış · Tanrı'ya kaçınılmaz dönüş · ölümden sonra dünyaya yeniden gelme
  إلى الله عز وجل مرجعك ورجوعك ورجعاك (jamhara)؛ فلان يؤمن بالرجعة أي بالرجوع إلى الدنيا بعد الموت (sihah)؛ إنه على بعثه يوم القيامة لقادر (tahdhib)؛ إلى الله مرجعكم وإن إلى ربك الرجعى (mufradat)
- **B003** bir şeyden vazgeçip geri dönmek [kalıp] — bir işten vazgeçmek veya yanlış davranışı bırakmak
  رجعت عن كذا رجعا؛ يرجعون عن الذنب؛ حرمنا عليهم أن يتوبوا ويرجعوا عن الذنب (mufradat)
- **B004** boşama sonrası evlilik bağına geri alma — boşanan eşi geri alma hakkı · boşadığı eşini evlilik bağına geri almak · eşi öldükten veya boşandıktan sonra ailesine dönen kadın
  راجع الرجل امرأته وهي الرجعة (maqayis)؛ طلاقا يملك الرجعة والرجعة والرجعى (jamhara)؛ له على امرأته رجعة (sihah)؛ المراجع من النساء التي يموت زوجها أو يطلقها فترجع إلى أهلها (tahdhib)؛ الرجعة والرجعة في الطلاق (mufradat)
- **B005** iletiye dönen yanıt — mektubun veya iletinin yanıtı · geri dönen yanıt · cevabı sahibine geri iletmek
  المرجوع جواب الرسالة (maqayis)؛ رجعى رسالتي أي مرجوعها ورجعان الكتاب جوابه (sihah)؛ رجع الجواب ورجع الرشق في الرمي ما يرد عليه (tahdhib)؛ بم يرجع المرسلون فمن رجع الجواب (mufradat)
- **B006** yinelenen yağmur veya biriken su — yağmur veya yeniden biriken su · su birikintileri veya su toplayan vadi üstleri
  الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث (maqayis)؛ الرجع الغدير أو الماء يترقرق والرجع المطر (jamhara)؛ الرجع المطر والرجع الغدير (sihah)؛ ذات الرجع أي ذات المطر والرجع في كلام العرب الماء والرجعان أعالي التلاع (tahdhib)؛ والسماء ذات الرجع أي المطر وسمي الغدير رجعا (mufradat)
- **B007** sesi yineleyip dalgalandırma — okuma veya söylemede sesi yineleyip dalgalandırma · namaza çağrıda tanıklık sözlerini tekrarlama · gök gürültüsünün yinelenen sesi
  الترجيع في الصوت ترديده (maqayis)؛ الترجيع تقارب ضروب الحركات في الصوت (ayn)؛ ترجيع الصوت ترديده في الحلق والترجيع في الأذان (sihah)؛ يقولون للرعد رجع والترجيع في الأذان (tahdhib)؛ الترجيع ترديد الصوت باللحن في القراءة وفي الغناء وتكرير قول مرتين فصاعدا (mufradat)
- **B008** hayvanın ön ayak adımı [kalıp] — hayvanın ön ayaklarını geri getirerek attığı adım · dişi devenin yürüyüş biçimini değiştirmesi
  الرجع رجع الدابة يديها في السير (maqayis)؛ الرجع ترجيع الدابة يدها في السير (ayn)؛ رجع الدابة يديها في السير خطوها (sihah)؛ الرجع الخطو وراجعت الناقة رجاعا إذا كانت في ضرب من السير فرجعت إلى سير سواه (tahdhib)
- **B009** çizgileri yeniden çekip karartmak [kalıp] — dövme çizgilerini yeniden çekmek veya karartmak
  ترجيع وشي النقش والوشم والكتابة خطوطها (ayn)؛ رجع الواشمة خطها (sihah)؛ رجع الوشم والنقوش وترجيعه أن يعاد عليه السواد مرة بعد أخرى (tahdhib)
- **B010** elini geriye uzatmak [kalıp] — elini geriye, ok kılıfına veya kılıca uzatmak
  أرجع الرجل يده في كنانته (maqayis)؛ أرجع يده إلى سيفه ليستله أو إلى كنانته ليأخذ سهما (jamhara)؛ أرجع الرجل إذا أهوى بيده إلى خلفه ليتناول شيئا (sihah)؛ أرجع الرجل يده إذا أهوى بها إلى كنانته (tahdhib)؛ أرجع يده إلى سيفه ليستله (mufradat)
- **B011** satış bedeliyle yerine mal almak — hayvanları satıp bedeliyle yerlerine başkalarını almak · satılanın bedeliyle alınan veya tahsilde yerine kabul edilen karşılık
  الراجعة الناقة تباع ويشترى بثمنها مثلها (maqayis)؛ ارتجع فلان إبلا إذا باع الذكور واشترى الإناث (jamhara)؛ الرجعة في الصدقة إذا أخذ المصدق مكانها أسنانا فوقها أو دونها (sihah)؛ الارتجاع أن يبيعها ثم يشتري بثمنها مثلها أو غيرها (tahdhib)؛ دابة لها مرجوع يمكن بيعها بعد الاستعمال وارتجع إبلا (mufradat)
- **B012** kuşların göçten geri dönüşü — kuşların mevsimsel geçişten sonra geri dönüşü
  الرجاع رجوع الطير بعد قطاعها (maqayis)؛ الرجاع رجوع الطير بعد قطاعها إذا رجعت من المواضع الحارة إلى المواضع الباردة (jamhara)؛ الرجاع أيضا رجوع الطير بعد قطاعها (sihah)؛ الرجاع مختص برجوع الطير بعد قطاعها (mufradat)
- **B013** gebeliğin oluşmaması veya çok erken sona ermesi [kalıp] — çiftleştiği halde gebe kalmayan veya gebe sanılıp boş çıkan dişi deve · yavrusu biçimlenmeden düşük yapmak
  ناقة راجع وهي التي يضربها الفحل فلا تلقح (jamhara)؛ أتان راجع وناقة راجع فيظن أن بها حملا ثم تخلف (sihah)؛ إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت (tahdhib)؛ ناقة راجع ترد ماء الفحل فلا تقبله (mufradat)
- **B014** yolculukta yıpranma veya güçsüzlükten sonra toparlanma [kalıp] — bir yolculuktan ötekine sürülerek bitkin düşmüş hayvan · zayıflıktan sonra semirip iyi duruma gelmek · hastalıktan sonra kendini ve gücünü yeniden bulmak
  الرجيع من الدواب ما رجعته من سفر إلى سفر وأرجعت الإبل إذا كانت مهازيل فسمنت (maqayis)؛ بعير رجيع سفر مثل نضو سفر (jamhara)؛ الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال (sihah)؛ يقال للمريض إذا ثابت إليه نفسه بعد تهوك من العلة راجع (tahdhib)؛ من الدابة ما رجعته من سفر إلى سفر ورجع سفر كناية عن النضو (mufradat)
- **B015** geri çıkan veya yeniden işlenen şey — sindirimden sonra çıkan dışkı veya bağırsak artığı · hayvanın ağzına getirip yeniden çiğnediği geviş · sahibine geri çevrilen veya yinelenen söz · eskimiş veya sökülüp yeniden yapılmış giysi · soğuduktan sonra yeniden ısıtılmış yemek
  الرجيع الجرة لأنه يردد مضغها (maqayis)؛ الرجيع يكنى به عن ذي البطن وحبل رجيع وثوب رجيع (jamhara)؛ الرجيع الروث والبعر وذو البطن وكل شئ يردد فهو رجيع (sihah)؛ الرجيع يكون الروث والعذرة والرجيع العرق وكل طعام برد فأعيد على النار فهو رجيع (tahdhib)؛ الرجيع كناية عن أذى البطن وجبة رجيع أعيدت بعد نقضها (mufradat)

## ن ه ي (root_001560): 96:9 يَنْهَىٰ, 96:15 يَنتَهِ

- **B001** bir eylemi yasaklama, engelleme veya ondan geri durma — yasaklama ve engelleme · onu bundan alıkoyup bıraktırdı · ondan geri durdu · kötülükten birbirlerini alıkoydular · benliği tutkudan alıkoymak · kötülükten sık sık alıkoyan · onu bizden alıkoyacak kimse yok
  النهي خلاف الأمر (ayn;sihah)؛ النهي الزجر عن الشيء (mufradat)؛ نهيته عنه فانتهى عنك (maqayis;sihah)؛ وتناهوا عن المنكر أي نهى بعضهم بعضا (sihah)؛ ما تنهاه عنا ناهية أي ما تكفه عنا كافة (ayn)
- **B002** son noktaya varma veya bir şeyi hedefine ulaştırma — bitiş noktası ve son sınır · varış sınırı · son sınır · haberi ona ulaştırdı · oku ona ulaştırdı · ulaştırma ve bildirme · devenin burun bağının uç bölümü
  النهاية الغاية حيث ينتهي إليه الشيء وهو النهاء (ayn)؛ نهاية كل شيء غايته (maqayis)؛ أنهيت إليه الخبر بلغته إياه (maqayis;mufradat)؛ الإنهاء الإبلاغ وأنهيت إليه الخبر فانتهى وتناهى أي بلغ (sihah)؛ النهاية طرف العران الذي في أنف البعير (ayn)
- **B003** kötü davranışı önleyen akıl ve sağduyu — kötü davranışı önleyen sağduyu · kötü davranışı önleyen akıllar · onu durduracak aklı yok
  النهية العقل لأنه ينهى عن قبيح الفعل والجمع نهى (maqayis)؛ النهية العقول لأنها تنهى عن القبيح (sihah)؛ النهية العقل الناهي عن القبائح جمعها نهى (mufradat)
- **B004** akış sonunda suyun durulup biriktiği yer — suyun akıp toplandığı doğal gölcük · suyun akıp toplandığı doğal gölcük · su gölcükte durup sakinleşti · vadide sel sularının son bulup yayıldığı yer
  النهي والنهي الغدير لأن الماء ينتهي إليه (maqayis)؛ النهي الغدير حيث ينخرم السيل في الغدير (ayn)؛ تناهى الماء إذا وقف في الغدير وسكن (sihah)؛ تنهية الوادي حيث ينتهي إليه السيول (maqayis;mufradat)
- **B005** başkasını aratmayacak kadar yeterli [kalıp] — başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli adam · başkasını aratmayacak kadar yeterli kadın
  فلان ناهيك من رجل ونهيك كما يقال حسبك (maqayis)؛ هذا رجل ناهيك من رجل ونهيك من رجل ونهاك من رجل (sihah)؛ ناهيك من رجل كقولك حسبك (mufradat)
- **B006** semizliğin doruğuna ulaşmış deve [kalıp] — semizliğin doruğuna ulaşmış dişi deve · iri ve semiz kesimlik deve
  ناقة نهية تناهت سمنا (maqayis;mufradat)؛ جزور نهية أي ضخمة سمينة (sihah)
- **B007** sonuçtan bağımsız olarak ihtiyacı aramayı bırakma [kalıp] — ihtiyacı aramayı, bulsa da bulmasa da bıraktı
  طلب الحاجة حتى نهي عنها تركها ظفر بها أم لا (maqayis)؛ طلب الحاجة حتى نهى عنها أي تركها ظفر بها أو لم يظفر (sihah)؛ طلب الحاجة حتى نهي عنها أي انتهى عن طلبها ظفر بها أو لم يظفر (mufradat)
- **B008** günün veya suyun yükselmesi [kalıp] — günün yükselip öğleye yaklaşması · suyun yükselmesi
  نهاء النهار ارتفاعه (maqayis;mufradat)؛ نهاء النهار ارتفاعه قراب نصف النهار (ayn)؛ نهاء الماء بالضم ارتفاعه (sihah)
- **B009** şişe veya cam eşya için tartışmalı ad — 
  النهاء القوارير وليس كذلك عندنا (maqayis)؛ النهاء القوارير والزجاج (sihah)
- **B010** yaklaşık yüzlük miktar [kalıp] — yaklaşık yüz kişi veya öğelik miktar
  هم نهاء مائة ونهاء مائة أيضا أي قدر مائة (sihah)

## ع ب د (root_000973): 96:10 عَبْدًا

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

## ص ل و (root_000879): 96:10 صَلَّىٰٓ

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

## ECHO ص ل ي (root_000880): for 96:10 صَلَّىٰٓ: withheld observed target; not identity

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

## ك و ن (root_001332): 96:11 كَانَ

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

## ه د ي (root_001583): 96:11 ٱلْهُدَىٰٓ

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

## ECHO ه د د (root_001580): for 96:11 ٱلْهُدَىٰٓ: withheld observed target; not identity

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

## ء م ر (root_000051): 96:12 أَمَرَ

- **B001** konu ve hal — konu, hal veya tekil iş · konular, haller ve işler
  الأمر من الأمور، الواحد من الأمور (maqayis)؛ الأمر واحد من أمور الناس (ayn)؛ الأمر واحد الأمور (sihah;tahdhib)؛ الأمر الشأن وجمعه أمور (mufradat)
- **B002** buyrukla yükümlü kılma — yapma buyruğu ve yükümlü kılma · ona bir şeyi yapmasını buyurdum · buyurma fiilinin söz içindeki biçimi · uyulacak tek bir buyruk hakkı · iyiliği çokça buyuran · onlara uymaları buyruldu, onlar da karşı geldi
  الأمر الذي هو نقيض النهي قولك افعل كذا (maqayis)؛ الأمر نقيض النهي وإذا أمرت من الأمر قلت اؤمر (ayn)؛ أمرته بكذا أمرا والجمع الأوامر (sihah)؛ الأمر معروف نقيض النهي (tahdhib)؛ مصدر أمرته إذا كلفته أن يفعل شيئا، والتقدم بالشيء (mufradat)
- **B003** yönetme yetkisi — yönetme makamı ve yetkisi · yetkili yönetici · yönetici kılınmış kimse · onu yönetici yaptım · topluluğunun yöneticisi oldu · yetki sahipleri · onları yönetici kıldık
  الإمرة والإمارة وصاحبها أمير ومؤمر (maqayis)؛ الإمرة الإمارة وهو أمير مؤمر (ayn)؛ الأمير ذو الأمر والتأمير تولية الامارة (sihah)؛ أمر الرجل إمارة إذا صار عليهم أميرا (tahdhib)؛ أولي الأمر عنى الأمراء، وقرئ أمرنا أي جعلناهم أمراء (mufradat)
- **B004** bereketli çoğalma — artış, verim ve bereket · çoğaldı ve büyüdü · topluluk çoğaldı, malları veya nimetleri arttı · uğurlu, bereket getiren kişi · çok yavrulayan ve bereketli kısrak · Tanrı onun malını çoğalttı · onları veya varlıklılarını çoğalttık
  الأمر النماء والبركة، وقد أمر الشيء أي كثر (maqayis)؛ الأمرة البركة وامرأة أمرة، وأمر الشيء أي كثر (ayn)؛ أمر هو أي كثر، وأمر القوم أي كثروا (sihah)؛ الأمرة الزيادة والنماء والبركة (tahdhib)؛ أمر القوم كثروا، وآمرنا بمعنى أكثرنا (mufradat)
- **B005** belirti veya belirlenmiş vakit — belirti, belirlenmiş zaman veya buluşma vakti · yolun işaretleri · çöl veya yol üzerindeki küçük işaret taşı
  الأمارة الموعد، والأمارة العلامة، والأمار أمار الطريق معالمه (maqayis)؛ الأمار الموعد (ayn)؛ الأمار والأمارة الوقت والعلامة، والأمر بالتحريك جمع أمرة وهي العلم الصغير من أعلام المفاوز من الحجارة (sihah)؛ الأمار الوقت والعلامة، والأمرات الأعلام واحدتها أمرة (tahdhib)
- **B006** ağır ve yadırganan şey — büyük, ağır, yadırganan veya şaşırtıcı iş · büyük ve yadırganan bir şey
  العجب، لقد جئت شيئا إمرا (maqayis)؛ أمر أمره أي اشتد والاسم الإمر، ويقال عجبا (sihah)؛ لقد جئت شيئا إمرا أي جئت شيئا عظيما من المنكر (tahdhib)؛ إمرا أي منكرا، من قولهم أمر الأمر أي كبر وكثر (mufradat)
- **B007** danışıp görüş oluşturma — işimde ona danıştım · karşılıklı danışma veya birbirinin görüşünü kabul etme · kendi içinde düşünüp görüşünü karara bağladı · senin hakkında birbirleriyle danışıyorlar
  فلان يؤامر نفسيه أي نفس تأمره بشيء ونفس تأمره بآخر (maqayis)؛ آمرته في أمري إذا شاورته، والائتمار والاستئمار المشاورة وكذلك التآمر (sihah)؛ ائتمر القوم إذا تشاوروا، أي كيف يرتئي رأيا ويشاور نفسه ويعقد عليه (tahdhib)؛ الائتمار قبول الأمر، ويقال للتشاور ائتمار (mufradat)
- **B008** zayıf görüşlü kişi — görüşü zayıf, her sözü dinleyip uyan akılsız kişi
  الإمر الرجل الضعيف الرأي الأحمق الذي يسمع كلام هذا وكلام هذا (maqayis)؛ الإمر الضعيف من الرجال (ayn)؛ رجل إمر وإمرة أي ضعيف الرأي يأتمر لكل أحد (sihah)؛ رجل إمر وإمرة أي يستأمر كل أحد في أمره، والإمر الأحمق (tahdhib)
- **B009** küçük koyun yavrusu — küçük koyun yavrusu; dişisi dişi kuzu veya genç dişi koyun
  الإمرة الأنثى من الحملان (ayn)؛ الإمر الصغير من ولد الضأن والأنثى إمرة (sihah)؛ الإمر الخروف والإمرة الرخل (tahdhib)
- **B010** Tanrı'ya özgü yaratma — Tanrı'ya özgü yaratma ve var etme
  ويقال للإبداع أمر، ويختص ذلك بالله تعالى دون الخلائق؛ قل الروح من أمر ربي أي من إبداعه؛ إنما قولنا لشيء إذا أردناه أن نقول له كن فيكون
- **B011** mızrağa uç takma — sivriltilmiş veya uç takılmış mızrak ucu · mızrağına keskin uç tak
  سنان مؤمر أي محدد؛ أمر قناتك أي اجعل فيها سنانا

## و ق ي (root_001677): 96:12 بِٱلتَّقْوَىٰٓ

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

## ك ذ ب (root_001290): 96:13 كَذَّبَ, 96:16 كَٰذِبَةٍ

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

## و ل ي (root_001684): 96:13 وَتَوَلَّىٰٓ

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

## ء ل ه (root_000047): 96:14 ٱللَّهَ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 96:14 ٱللَّهَ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## س ف ع (root_000713): 96:15 لَنَسْفَعًۢا

- **B001** başın ön saçından tutma — başın ön kısmındaki saçtan tutmak
  سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته (maqayis)؛ سفعت بناصيته أي أخذت (sihah)؛ لنأخذن بها (tahdhib)؛ السفع الأخذ بسفعة الفرس أي سواد ناصيته (mufradat)
- **B002** kızıllık karışmış siyahlık — kızıllık karışmış siyahlık · kızıla çalan koyu renkli · koyu renkli dişi veya kadın · öfkeden yüzüne koyu bir renk çökmüş · yanakları koyu renkli kadın · koyu renkli veya kararmış olanlar · yer izlerinin çevreden ayrılan karalığı
  السفعة وهي السواد (maqayis)؛ السفعة بالضم سواد مشرب حمرة (sihah)؛ سفعاء الخدين امرأة سوداء (tahdhib)؛ باعتبار السواد قيل للأثافي سفع وبه سفعة غضب (mufradat)
- **B003** hafifçe kavurup ten rengini değiştirme — ateş onu hafifçe kavurup tenini kararttı · yakıcı sıcak rüzgar yüzünün rengini değiştirdi · kavurucu sıcak rüzgarlar
  سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة (sihah)؛ سفعته النار إذا لفحته لفحا يسيرا فسودت بشرته وسفعته السموم إذا لوحت بشرة الوجه (tahdhib)
- **B004** tokatlama veya vurma — kuş kanadıyla veya avına vurdu · başına değnekle vurdu · karşılıklı dövüşme ve tokatlaşma
  سفع الطائر ضريبته أي لطمه (maqayis)؛ سفع الطائر لطمه بجناحيه (sihah)؛ سفعته أي لطمته والمسافعة المضاربة (tahdhib)
- **B005** kovalamaca — kovalamaca ve peşinden gitme
  المسافعة كالمطاردة (sihah)
- **B006** kötücül varlığa bağlanan zarar — kötücül bir varlıktan geldiğine inanılan dokunma, vuruş, kem göz veya delilik · böyle bir etkiyle delirmiş sayılan kişi · kem göz değmiş kadın
  به سفعة من الشيطان أي مس كأنه أخذ بناصيته (sihah)؛ سفعة أي ضربة منه والسفعة والشفعة الجنون والمسفوعة التي أصابتها العين (tahdhib)
- **B007** özellikle boyalı giysileri giyme — kadın giysilerini giydi; çoğunlukla boyalı giysiler için söylenir · kadının giysileri
  استفعت المرأة ثيابها إذا لبستها وأكثر ما يقال ذلك في الثياب المصبوغة (tahdhib)

## ن ص ي (root_001512): 96:15 بِٱلنَّاصِيَةِ, 96:16 نَاصِيَةٍ

- **B001** alın saç çizgisi; buradan tutup çekme ve denetim altına alma — alındaki saç çizgisi ya da ön saçın çıktığı yer · birini ön saçından tutmak veya çekmek · karşılıklı olarak ön saçlarından tutup çekişmek · alındaki saç çizgisi için bölgesel bir söyleyiş · ön saçlardan tutma · onu denetimi altında tutan ve üzerinde söz sahibi olan
  الناصية قصاص الشعر (maqayis;ayn;sihah;mufradat)؛ الناصية منبت الشعر في مقدم الرأس (tahdhib)؛ نصوته قبضت على ناصيته ومددتها (maqayis;ayn;sihah;tahdhib;mufradat)؛ ناصيته أخذ كل واحد بناصية صاحبه (maqayis;ayn;tahdhib;mufradat)؛ آخذ بناصيتها أي متمكن منها (mufradat)
- **B002** saçı tarama, saçın uzaması ve ölünün ön saçını çekip uzatma — saçın uzaması · ölünün başı hazırlanırken ön saçını çekip uzatmak · kadının saçını tarayıp düzene sokması · saçını tarayıp düzene sokmak
  تنصت المرأة إذا رجلت شعرها (sihah;tahdhib)؛ أن تنصى أي تسرح شعرها (tahdhib)؛ انتصى الشعر طال (maqayis;sihah;mufradat)؛ تنصون ميتكم أي تمدون ناصيته (maqayis;sihah;tahdhib;mufradat)
- **B003** seçkin kesim, en iyiyi seçme ve önde gelme — bir topluluğun ya da şeyin en iyi kesimi; kimi bağlamda geride kalan bölüm · bir şeyin en iyisini seçip almak · insanların önde gelenleri ve seçkinleri · bir topluluğun en yüksek konumdaki kesiminden evlenmek · topluluğunun önderi ve en seçkin kişisi · önden gidenler
  النصية من القوم ومن كل شيء الخيار (maqayis;sihah)؛ انتصيت الشيء اخترته (maqayis;sihah)؛ نخبة الناس وخيارهم هم نصية انتصوا (ayn)؛ نواصي الناس أشرافهم والنصية الخيار الأشراف (sihah;tahdhib)؛ النصية البقية (sihah;tahdhib)؛ الأنصاء السابقون (tahdhib)؛ فلان ناصية قومه وفلان نصية قوم أي خيارهم (mufradat)؛ تنصيتهم إذا تزوجت في الذروة منهم والناصية (sihah)
- **B004** tazeyken değerli bir otlak bitkisi — tazeyken değerli bir otlak bitkisi · o bitkinin bir arazide çokça yetişmesi
  النصي نبات من أفضل المراعي (ayn;mufradat)؛ النصى نبت ما دام رطبا فإذا ابيض فهو الطريفة وإذا ضخم ويبس فهو الحلي (sihah)؛ النصي نبت معروف ما دام رطبا فإذا يبس فهو حلي (tahdhib)؛ أنصت الأرض أي كثر نصيها (sihah)
- **B005** bir çöl düzlüğünün başka bir çöl düzlüğüne bitişmesi — bir çöl düzlüğünün başka bir çöl düzlüğüne, onun önünü kavrar gibi bitişmesi
  مفازة تناصي أخرى كأنها تتصل بها كالقابضة على ناصيتها (maqayis)؛ مفازة تناصي مفازة إذا كانت الأولى متصلة بالأخرى (ayn)؛ فلاة تناصي فلاة أي تتصل بها (sihah;tahdhib)؛ تناصي أرض كذا وتواصيها أي تتصل بها (tahdhib)
- **B006** karında batıcı, huzursuz eden sancı — karında duyulan, kişiyi rahat duramaz hale getiren batıcı sancı
  أجد في بطني نصوا ووخزا (tahdhib)؛ النصو مثل المفس سمي نصوا لأنه ينصوك أي يزعجك عن القرار (tahdhib)؛ وجدت في بطني حصوا ونصوا وقبصا بمعنى واحد (tahdhib)

## خ ط ء (root_000420): 96:16 خَاطِئَةٍ

- **B001** istemeden doğruyu tutturamama — istemeden yapılan yanlış; doğruyu tutturamama · yanılmak; doğruyu tutturamamak · yanılmak; amaçlanan sonucu elde edememek · yanılmak; yanlış yapmak · doğruyu amaçlayıp yanılan kimse · yanlış yaptığını söylemek; yanlış bulmak · ıskalamak; değmemek · kötülük senden uzak olsun · çok yanılan da bazen doğruyu bulur
  أخطأ إذا لم يصب الصواب؛ الخطأ ما لم يتعمد؛ خطأته تخطئة (ayn)؛ الخطأ نقيض الصواب؛ المخطئ من أراد الصواب فصار إلى غيره؛ خطأته تخطئة وتخطيئا (sihah)؛ أخطأ إذا لم يصب الصواب؛ أخطأت لما صنعه خطأ غير عمد؛ خطىء عنك السوء إذا دعوا له أن يدفع عنه السوء (tahdhib)؛ الخطأ العدول عن الجهة؛ يقع منه خلاف ما يريد؛ أصاب الخطأ وأخطأ الصواب (mufradat)؛ الخطاء مجاوزة حد الصواب؛ أخطأ إذا تعدى الصواب (maqayis)
- **B002** bilerek işlenen günah — sorumluluk doğuran günah · günah; suç · günah işlemek · hesabı sorulan günah veya kötü eylem · günahı bilerek işleyen kimse; günahkâr · büyük günah · günahlar · ne büyük günah işledi!
  الخطء الذنب؛ خطئ يخطأ خطأ وخطأة؛ الخطيئة (sihah)؛ خطئت إذا أثمت؛ خاطئين أي آثمين؛ خطئت لما صنعه عمدا وهو الذنب؛ الخطيئة الذنب على عمد (tahdhib)؛ الخطأ التام المأخوذ به الإنسان؛ الخطيئة والسيئة يتقاربان؛ الخاطئ هو القاصد للذنب؛ الذنب العظيم (mufradat)؛ خطئ يخطأ إذا أذنب (maqayis)
- **B003** yağmurun atladığı arazi — yağmurun atladığı arazi · iki yağışlı arazi arasında yağışsız kalan yer · oraya yağmur yağmasın
  الخطيئة أرض يخطئها المطر ويصيب غيرها (ayn)؛ الأرض الخطيطة هي التي لم تمطر بين أرضين ممطورتين؛ من أخطأ كأن المطر أخطأها؛ خطأ الله نوءها (maqayis)

## د ع و (root_000478): 96:17 فَلْيَدْعُ, 96:18 سَنَدْعُ

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

## ECHO د ع ع (root_000477): for 96:17 فَلْيَدْعُ, 96:18 سَنَدْعُ: withheld observed target; not identity

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

## ن د و (root_001486): 96:17 نَادِيَهُۥ

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

## ECHO ن د ي (root_001487): for 96:17 نَادِيَهُۥ: withheld observed target; not identity

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

## ECHO ن و د (root_001563): for 96:17 نَادِيَهُۥ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## ز ب ن (root_000622): 96:18 ٱلزَّبَانِيَةَ

- **B001** itip uzaklaştırma ve savuşturma — itme, savuşturma ve çarpma · onu engelleyip itti · deve sağanı ya da yavrusunu memesinden ayağıyla itti · sağanı tekmeleyip uzaklaştıran huysuz deve · savaş insanlara çarpıp onları sürükler · insanlara çarpıp onları süren savaş · topluluk birbirini itti · kendi tarafını güçlü biçimde savunan adam · kendini savunan, kibirli tavırlı adam · iki pisliği dışarı atan
  الزبن دفع الشيء عن الشيء (ayn;sihah;tahdhib); ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها (maqayis;ayn;jamhara;sihah;tahdhib); الحرب تزبن الناس إذا صدمتهم وحرب زبون (maqayis;ayn;jamhara;sihah;tahdhib); رجل ذو زبونة مانع لجانبه ذو دفع (maqayis;sihah;tahdhib); الزَّبين الدافع للأخبثين (tahdhib)
- **B002** zorla sevk eden sert görevliler — sert kolluk görevlileri veya cehenneme süren azap melekleri · bu görevlilerden biri · bu görevlilerden biri · bu görevlilerden biri · bu görevlilerden biri
  الزبانية سموا بذلك لأنهم يدفعون أهل النار إلى النار (maqayis;sihah); الزبانية ملائكة موكلون بتعذيب أهل النار (ayn); من هذا اشتقاق الزبانية (jamhara); الزبانية الشرط في كلام العرب والملائكة الغلاظ الشداد (tahdhib); واحدهم زبنية أو زبني (sihah;tahdhib)
- **B003** ağaçtaki hurmayı kuru hurmayla götürü satma — ağaçtaki yaş hurmayı kuru hurma karşılığında götürü satma
  المزابنة بيع الثمر في رؤوس النخل (maqayis); المزابنة بيع التمر في رأس النخل بالتمر (ayn;tahdhib); بيع الرطب في رؤوس النخل بالتمر ونهى عنه (sihah); لأن كل واحد إذا ندم زبن صاحبه عما عقد عليه (tahdhib)
- **B004** akrebin kıskaçları ve bunları simgeleyen yıldızlar — akrebin iki kıskacı veya boynuzu · Akrep'in kıskaçlarını simgeleyen iki parlak yıldız · bu gök bölgesindeki ilgili yıldız topluluğu
  زباني العقرب يجوز أن يكون من هذا ويجوز أن يكون شاذا (maqayis); الزبانى قرن العقرب ولها زبانيان (jamhara); زبانيا العقرب قرناها والزبانيان كوكبان نيران (sihah); زبانيا العقرب كوكبان وزبانيا العقرب قرناها (tahdhib)
- **B005** uzakta bulunma ve uzaklaşma — uzaklık ve yerleşimden uzaklaşma · topluluğunun evlerinden uzakta konakladı
  الزبن البعد (maqayis); حل فلان زبنا عن قومه وزبنا إذا تباعد عن بيوتهم (jamhara)
- **B006** yiyecekten ihtiyacı kadarını almak [kalıp] — bu yiyecekten ihtiyacım kadarını aldım
  أخذت زبني من هذا الطعام أي حاجتي (tahdhib)
- **B007** orada hiç kimsenin bulunmaması — orada hiç kimse yok
  ما بها زبين أي ليس بها أحد (tahdhib)
- **B008** boynundan tutmak [kalıp] — boynundan
  خذ بقردنه وبزبونته أي بعنقه (tahdhib)

## ط و ع (root_000956): 96:19 تُطِعْهُ

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

## ECHO س ط ع (root_000706): for 96:19 تُطِعْهُ: withheld observed target; not identity

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

## س ج د (root_000675): 96:19 وَٱسْجُدْ

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

## ق ر ب (root_001212): 96:19 وَٱقْتَرِب

- **B001** yakın olma, yaklaşma veya yaklaştırma — yakın olmak veya yaklaşmak · yaklaştırmak, yakına getirmek · yaklaşma · ses değişmesiyle yaklaşmak · suyu yakın kuyu · parçaları birbirine yakın, kısa yapılı
  أصل صحيح يدل على خلاف البعد (maqayis)؛ كرب الشيء دنا فليس من الباب وإنما هو من الإبدال من القرب (maqayis-ibdal)؛ قرب الشيء قربا ضد البعد (jamhara)؛ قرب الشيء يقرب قربا أي دنا والقرب ضد البعد (sihah)؛ القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو والقرب البئر القريبة الماء والرجل القصير متقارب (tahdhib)؛ القرب والبعد يتقابلان ويستعمل ذلك في المكان (mufradat)
- **B002** zamanca yaklaşma veya yakın geçmişe ait olma — vaadin veya hesap vaktinin yaklaşması · son saatin yaklaşması · ürünün olgunlaşma vaktinin yaklaşması · güneşin batmaya yaklaşması · henüz taze olan tuzlu balık
  اقترب الوعد أي تقارب (sihah)؛ تقارب الزمان اقتراب الساعة وتقارب الزرع إذا دنا إدراكه والشيء إذا ولى وأدبر قد تقارب والقريب السمك المملح ما دام في طراءته (tahdhib)؛ في الزمان نحو اقترب للناس حسابهم (mufradat)؛ كربت الشمس دنت للمغيب (maqayis-ibdal)
- **B003** akrabalık ve yakın akraba — akrabalık, soy bağı · yakın akraba · yakın akrabalığı olan kimse
  فلان ذو قرابتي وهو من يقرب منك رحما والقربة والقربى القرابة (maqayis)؛ قريب الرجل مدانيه من نسب أم أو أب والجمع قرابة وقرباء وأقرباء (jamhara)؛ القرابة القربى في الرحم وهو قريبي وذو قرابتي وهم أقربائي وأقاربي (sihah)؛ القريب والقريبة ذو القرابة وفلان ذو قرابتي وذو مقربة وذو قربى (tahdhib)؛ في النسبة أولوا القربى والأقربون وذو قربى ولذي القربى والجار ذي القربى ويتيما ذا مقربة (mufradat)
- **B004** ayrıcalıklı yakın çevre — yakın kılınmış, gözde kişiler · hükümdarın özel çevresi, oturum arkadaşları ve yöneticileri · yakın kılınmış melekler
  قربان الملك وقرابينه وزراؤه وجلساؤه (maqayis)؛ قرابين الملك خاصته وقربان الملك قرابته والجمع قرابين (jamhara)؛ القربان واحد قرابين الملك وهم جلساؤه وخاصته (sihah)؛ القرابين جلساء الملوك وخاصته وقرابين الملك وزراؤه (tahdhib)؛ في الحظوة الملائكة المقربون ومن المقربين وقربناه نجيا (mufradat)؛ الملائكة الكروبيون وهم المقربون (maqayis-ibdal)
- **B005** Tanrı'ya yakınlık kazandıran iş veya sunu — Tanrı'ya yakınlık kazandıran iyi iş veya araç · Tanrı'ya yakınlık için sunulan şey veya kesilen hayvan · iyi bir iş veya sunuyla Tanrı'ya yakınlık aramak
  القربان ما قرب إلى الله تعالى من نسيكة أو غيرها (maqayis)؛ ما له عند الله قربة والقربان الأضاحي وكل ما تقرب إلى الله فهو قربان (jamhara)؛ القربان ما تقربت به إلى الله وتقرب إلى الله بشيء طلب به القربة (sihah)؛ القربان ما قربت إلى الله تبتغي بذلك قربة ووسيلة وهي ذبائح كانوا يذبحونها (tahdhib)؛ القربان ما يتقرب به إلى الله وصار اسما للنسيكة التي هي الذبيحة والقربة قربات عند الله (mufradat)
- **B006** gözetme, güç ve ruhsal yöneliş bakımından yakınlık — gözetip karşılık vermek üzere yakın · gücü ve erişimi bakımından insana en yakından hakim · insanın Tanrı'ya ruhsal yakınlığı
  في الرعاية نحو فإني قريب أجيب دعوة الداع وفي القدرة نحو ونحن أقرب إليه من حبل الوريد وقرب الله تعالى من العبد هو بالإفضال عليه والفيض لا بالمكان وقرب العبد من الله قرب روحاني لا بدني (mufradat)
- **B007** temas edip içine girecek ölçüde yaklaşma — bir işe bulaşmak, girişmek veya onu yapmak üzere olmak · yasak şeye yönelmemek ve onunla temas kurmamak · eşiyle cinsel ilişkide bulunmak
  ما قربت هذا الأمر ولا أقربه إذا لم تشامه ولم تلتبس به (maqayis)؛ قرب فلان أهله قربانا إذا غشيها وما قربت هذا الأمر ولا قربته ولا تقربا هذه الشجرة ولا تقربوا الزنى (tahdhib)؛ ولا تقربوهن كناية عن الجماع ولا تقربوا مال اليتيم أبلغ من النهي عن تناوله ولا تقربوا الزنى (mufradat)
- **B008** geceleyin su kaynağına yönelme — suya varıştan önceki gece yolculuğu · su arayıp kaynağa doğru gitmek · geceleyin su arayan kişi veya hayvan · suya doğru giderken acele etmek · suya gidip gelen hiç kimsesi yok
  من الباب القرب وهي ليلة ورود الإبل الماء والقارب الطالب الماء ليلا (maqayis)؛ القرب أن يرعى القوم بينهم وبين المورد حتى إذا كان بينهم وبين الماء عشية أو ليلة عجلوا فقربوا وحمار قارب يطلب الماء (ayn)؛ قربت الإبل الماء إذا طلبته وليلة القرب ليلة طلب الماء (jamhara)؛ القرب سير الليل لورد الغد والقارب طالب الماء ليلا (sihah)؛ ليلة القرب هو السوق الشديد وتقرب أي اعجل وقربت الماء أي طلبته والقرب سير الليل (tahdhib)؛ رجل قارب قرب من الماء وليلة القرب وأقربوا إبلهم (mufradat)
- **B009** su tulumu — su tulumu, deri su kabı
  القربة معروفة (jamhara)؛ القربة ما يستقى فيه الماء والجمع قربات وقربات وقربات وللكثير قرب (sihah)؛ القربة وجمعها قرب من الأساقي (tahdhib)
- **B010** kılıç kını veya deri dış kabı — kılıç kını veya kını saran deri kap · kılıcı kabına koymak veya ona bir kap yapmak
  منه القراب قراب السيف والجمع قرب (maqayis)؛ قراب السيف جلد يكون فيه وليس بالغمد والجمع قرب (jamhara)؛ قراب السيف جفنه وهو وعاء يكون فيه السيف بغمده وحمالته (sihah)؛ القراب للسيف والسكين وقربته جعلته في القراب (tahdhib)؛ القراب وعاء السيف وقيل جلد فوق الغمد لا الغمد نفسه (mufradat)
- **B011** gemiye bağlı küçük hizmet teknesi — gemiye eşlik eden küçük hizmet teknesi
  القارب سفينة صغيرة تكون مع أصحاب السفن البحرية وكأنها سميت بذلك لقربها منهم (maqayis)؛ قارب السفينة وهو الصغير الذي يتبعها (jamhara)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم (sihah)؛ القارب سفينة صغيرة تكون مع أصحاب السفن البحرية تستخف لحوائجهم والجميع القوارب (tahdhib)
- **B012** doğumu yaklaşmış gebe dişi — koyunun doğumu yaklaşmak · doğumu yaklaşmış gebe dişi
  أقربت الشاة دنا نتاجها (maqayis)؛ شاة مقرب إذا دنا ولادها (jamhara)؛ أقربت المرأة إذا قرب ولادها وكذلك الفرس والشاة فهي مقرب ولا يقال للناقة (sihah)؛ أقربت الشاة والأتان فهي مقرب ولا يقال للناقة إلا إذا أدنت فهي مدن (tahdhib)؛ المقرب الحامل التي قربت ولادتها (mufradat)
- **B013** yakında tutulan ve binmeye hazırlanan hayvan — yakında tutulan, gözetilen ve binmeye hazır at · binmek için bağlanmış veya eyerlenmiş develer
  فرس مقربة وهي التي ترتاد وتقرب ولا تترك أن ترود (maqayis)؛ فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة (jamhara)؛ المقرب من الخيل الذي يدنى ويكرم والأنثى مقربة (sihah)؛ الخيل المقربة التي تكون قريبا معدة والتي تدنى وتقرب وتكرم والإبل المقربة التي حزمت للركوب (tahdhib)
- **B014** atın dörtnaldan yavaş özel koşusu — atın dörtnaldan yavaş özel koşu biçimi
  قرب الفرس تقريبا وهو دون الحضر وله تقريبان أدنى وأعلى (maqayis)؛ قرب الفرس تقريبا وهو تقريبان التقريب الأدنى والتقريب الأعلى وهو دون الحضر (jamhara)؛ التقريب ضرب من العدو وهو دون الحضر (sihah)؛ إذا رفع الفرس يديه معا ووضعهما معا فذلك التقريب (tahdhib)؛ تقريب الفرس سير يقرب من عدوه (mufradat)
- **B015** böğür, bedenin yan bölgesi — böğür, bel ile karnın alt yanı arasındaki bölge · böğürler, bedenin yanları · yürürken elini böğrüne koymuş
  الخاصرة هي القرب سميت لقربها من الجنب (maqayis)؛ قرب الفرس كشحه وهو الخصر والجمع أقراب (jamhara)؛ القرب من الشاكلة إلى مراق البطن والجمع الأقراب (sihah)؛ القرب من لدن الشاكلة إلى مراق البطن ومتقربا أي واضعا يده على قربه (tahdhib)؛ فرس لاحق الأقراب أي الخواصر (mufradat)
- **B016** bir ölçü veya sınıra yaklaşık olma — bir şeyin doluluğuna, sayısına veya miktarına yakın değer · neredeyse dolu kap · ses değişmesiyle neredeyse dolu kap · orta kalitede veya ucuz kumaş · satışta önerileri birbirine yaklaştırmak · akşama veya geceye yakın vakit
  ثوب مقارب إذا لم يكن جيدا وهذا على معنى أنه مقارب في ثمنه (maqayis)؛ الدراهم قراب مائة وإناء قربان إذا قارب أن يمتلىء وقراب كل شيء ما قارب الامتلاء (jamhara)؛ شيء مقارب وسط بين الجيد والردئ أو رخيص وقدح قربان إذا قارب أن يمتلئ وقاربته في البيع مقاربة (sihah)؛ القراب مقاربة الشيء معه ألف درهم أو قرابه وأتيته قراب العشي أو قراب الليل وقدح قربان ماء ولو أن في قراب هذا ذهبا (tahdhib)؛ القراب المقاربة وقدح قربان قريب من الملء (mufradat)؛ إناء كربان كرب أن يمتلىء (maqayis-ibdal)



===== _commentary/v16/work/s096/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s096/reader_a_pilot.md)

# s096 Semantic Channel Discovery

## Parent Channels

### 1. Making Things Knowable
- Semantic invariant: Something hidden or unknown becomes apprehensible through instruction, perception, inquiry, indication, or controlled disclosure.
- Surface relation: direct; 96:1-5 centers reading, naming, teaching, the pen, and human learning, while 96:9, 96:11, 96:13, and 96:14 repeatedly stage seeing, questioning, and knowing.
- Surprising reach: The channel extends from pedagogy and eyesight to banners, landmarks, appointments, and verification procedures.

#### Subchannel A. Teaching, Reading, and Inscription
- Reading type: surface-primary
- Scene or process: A knowledgeable source gathers words, teaches a human recipient, and fixes instruction with a prepared writing implement.
- Active motifs: gathered recitation `ق ر ء:B001/m01`; divinely grounded learning `ر ب ب:B003/m01`; acquired knowledge `ع ل م:B001/m01`; writing stylus `ق ل م:B003/m01`; human learner `ء ن س:B001/m01`
- Ayah anchors: `ق ر ء` 96:1, 96:3 (ٱقْرَأْ); `ر ب ب` 96:1, 96:3, 96:8 (رَبّ); `ع ل م` 96:4-5, 96:14 (عَلَّمَ، يَعْلَمْ); `ق ل م` 96:4 (ٱلْقَلَمِ); `ء ن س` 96:2, 96:5-6 (ٱلْإِنسَانَ)
- Synthesis: Recitation supplies the ordered verbal material, teaching transfers it, and the pared stylus gives it durable form. The human figure is both the object of creation and the recipient whose prior lack is changed into knowledge.

#### Subchannel B. Eye, Pupil, and Sustained Regard
- Reading type: mixed
- Scene or process: Detection begins with the eye, focuses through the dark pupil, and can settle into a prolonged, quiet gaze.
- Active motifs: visual perception `ر ء ي:B001/m01`; sensory detection `ء ن س:B002/m01`; dark pupil `ء ن س:B005/m01`; sustained gaze `س ج د:B005/m01`; dark-red or black tinge `س ف ع:B002/m01`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14 (رَأَى، أَرَأَيْتَ، يَرَى); `ء ن س` 96:2, 96:5-6 (ٱلْإِنسَانَ); `س ج د` 96:19 (ٱسْجُدْ); `س ف ع` 96:15 (لَنَسْفَعًا)
- Synthesis: The scene is an optical mechanism rather than a generic cognition cluster: an object is detected, received in the pupil, and held under an unbroken gaze. The chromatic branch sharpens the concrete blackness through which sight is imagined.

#### Subchannel C. Deliberation and Interrogative Attention
- Reading type: surface-primary
- Scene or process: An affair is turned over in thought, opened to consultation, and brought before an addressee through an attention-commanding question.
- Active motifs: inward judgment `ر ء ي:B002/m01`; consultation `ء م ر:B007/m01`; matter under consideration `ء م ر:B001/m01`; interrogative attention `ر ء ي:B013/m01`; recognition `ع ل م:B001/m02`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14 (رَأَى، أَرَأَيْتَ، يَرَى); `ء م ر` 96:12 (أَمَرَ); `ع ل م` 96:4-5, 96:14 (عَلَّمَ، يَعْلَمْ)
- Synthesis: The repeated interrogative surface form becomes a deliberative frame. A matter is mentally weighed, exposed to counsel, and then presented so that the hearer must recognize its moral or practical consequence.

#### Subchannel D. Flags, Marks, and Guiding Landmarks
- Reading type: latent/lexical
- Scene or process: A visible object is raised or differentiated so that it marks a place, time, party, or route.
- Active motifs: appointed sign `ء م ر:B005/m01`; raised flag `ر ء ي:B011/m01`; distinguishing landmark `ع ل م:B002/m01`; elevation `س م و:B001/m01`; gentle directional indication `ه د ي:B001/m01`
- Ayah anchors: `ء م ر` 96:12 (أَمَرَ); `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ع ل م` 96:4-5, 96:14; `س م و` 96:1 (ٱسْمِ); `ه د ي` 96:11 (ٱلْهُدَى)
- Synthesis: Elevation makes a marker conspicuous, the flag embodies that visibility, and the landmark turns visibility into guidance. Appointment adds a temporal function, so the same sign can orient movement or announce a due moment.

#### Subchannel E. Showing, Detecting, and Verifying
- Reading type: mixed
- Scene or process: A concealed condition is deliberately shown, sensed by an observer, and held long enough for verification.
- Active motifs: deliberate showing `ر ء ي:B012/m01`; sensory detection `ء ن س:B002/m01`; detention for verification `ق ر ء:B010/m01`; manifest appearance `ن د و:B008/m01`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ء ن س` 96:2, 96:5-6; `ق ر ء` 96:1, 96:3; `ن د و` 96:17 (نَادِيَهُ)
- Synthesis: Showing is the initiating act, detection is the observer's uptake, and temporary detention protects the judgment from haste. The image of something becoming so manifest that it seems to call out completes the disclosure process.

### 2. Address and Response
- Semantic invariant: Speech moves between parties by attracting attention, projecting a voice, requesting uptake, and eliciting an answer.
- Surface relation: direct; commands to read at 96:1 and 96:3, repeated interrogative address at 96:9, 96:11, and 96:13, and reciprocal calling at 96:17-18 provide the surface frame.
- Surprising reach: The same exchange structure reaches greeting formulas, echoes, song, riddles, exhortation, and exchanged verse.

#### Subchannel A. Call, Raised Voice, Echo, and Song
- Reading type: mixed
- Scene or process: A caller projects a voice across distance, the sound carries or returns, and repeated tone can become song or public repute.
- Active motifs: vocal summons `د ع و:B001/m01`; raised call `ن د و:B002/m01`; returned echo `ر ج ع:B007/m01`; singing voice `غ ن ي:B003/m01`; far-reaching good repute `س م و:B008/m01`
- Ayah anchors: `د ع و` 96:17-18 (يَدْعُ، نَدْعُ); `ن د و` 96:17 (نَادِيَهُ); `ر ج ع` 96:8 (ٱلرُّجْعَى); `غ ن ي` 96:7 (ٱسْتَغْنَى); `س م و` 96:1 (ٱسْمِ)
- Synthesis: Calling supplies an emitter and addressee, raised voice supplies range, and echo supplies acoustic return. Song and reputation extend the same propagation pattern from immediate sound to a voice that continues socially.

#### Subchannel B. Greeting and Courteous Reply
- Reading type: latent/lexical
- Scene or process: A formulaic greeting reaches another party and is met by a returned, gracious response.
- Active motifs: conveyed greeting `ق ر ء:B006/m01`; verbal reply `ر ج ع:B005/m01`; gracious acceptance `ك ر م:B009/m01`; attention to the addressee `ر ء ي:B013/m01`
- Ayah anchors: `ق ر ء` 96:1, 96:3; `ر ج ع` 96:8; `ك ر م` 96:3 (ٱلْأَكْرَمُ); `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: The greeting is not isolated wording but the first half of a social transaction. Return speech completes it, while graciousness specifies the expected quality of the answer.

#### Subchannel C. Riddle and Answer
- Reading type: latent/lexical
- Scene or process: An opaque verbal problem is posed, held before an interlocutor, and resolved by a returned answer.
- Active motifs: enigmatic utterance `د ع و:B007/m01`; answer returned in speech `ر ج ع:B005/m02`; satisfying response `ك ر م:B009/m02`; interrogative attention `ر ء ي:B013/m02`
- Ayah anchors: `د ع و` 96:17-18; `ر ج ع` 96:8; `ك ر م` 96:3; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: The opaque utterance creates an information gap, interrogative attention assigns it to a respondent, and the returned answer closes the exchange. The courteous-response motif gives the successful solution a social as well as intellectual outcome.

#### Subchannel D. Injunction and Exhortation
- Reading type: mixed
- Scene or process: A speaker draws attention, presses an obligation, and urges the hearer toward an action.
- Active motifs: imperative obligation `ك ذ ب:B003/m01`; verbal urging `د ع و:B001/m02`; command and requirement `ء م ر:B002/m01`; interrogative alert `ر ء ي:B013/m01`
- Ayah anchors: `ك ذ ب` 96:13, 96:16 (كَذَّبَ، كَاذِبَة); `د ع و` 96:17-18; `ء م ر` 96:12; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: Attention is first captured, then obligation is placed upon the addressee, and the call supplies forward pressure. This scene explains how interrogative address and direct command can operate as one exhortative mechanism.

#### Subchannel E. Poetic Pattern and Exchange
- Reading type: latent/lexical
- Scene or process: A verbal model supplies the pattern for composition, and completed verse is passed between speakers.
- Active motifs: poetic model `ق ر ء:B005/m01`; intended verbal method `ق ر ء:B011/m01`; exchanged verse `ه د ي:B011/m01`; voiced delivery `ن د و:B002/m02`
- Ayah anchors: `ق ر ء` 96:1, 96:3; `ه د ي` 96:11; `ن د و` 96:17
- Synthesis: A model determines the path of composition, while reciprocal gifting of verse turns form into a social exchange. Raised delivery gives the patterned text an audible public life.

### 3. Truth, Claim, and Deceptive Presentation
- Semantic invariant: A representation is asserted, tested against what is known, and either sustained as truth or exposed as fabrication.
- Surface relation: direct; denial and turning away at 96:13, divine seeing at 96:14, and the lying, erring forelock at 96:16 make truth status an explicit surface concern.
- Surprising reach: Falsehood expands into authorship, attached legal claims, imputation, and a self that protects its own deception.

#### Subchannel A. Fabricating a False Account
- Reading type: surface-primary
- Scene or process: Speech is invented, presented as an account of reality, and contradicted by the truth it displaces.
- Active motifs: fabricated speech `خ ل ق:B007/m01`; falsehood `ك ذ ب:B001/m01`; attribution of lying `ك ذ ب:B002/m01`; known reality `ع ل م:B001/m03`
- Ayah anchors: `خ ل ق` 96:1-2 (خَلَقَ); `ك ذ ب` 96:13, 96:16; `ع ل م` 96:4-5, 96:14
- Synthesis: Fabrication supplies the production act, falsehood names the defective product, and imputation assigns responsibility for it. Knowledge provides the counter-state against which the invented account fails.

#### Subchannel B. Claim, Lineage, and Attached Litigation
- Reading type: latent/lexical
- Scene or process: A party asserts a right or affiliation, the assertion adheres to an opponent as a dispute, and speech is returned in contest.
- Active motifs: asserted right `د ع و:B002/m01`; attached lawsuit `ع ل ق:B005/m01`; fabricated pleading `خ ل ق:B007/m02`; contested reply `ر ج ع:B005/m03`
- Ayah anchors: `د ع و` 96:17-18; `ع ل ق` 96:2 (عَلَق); `خ ل ق` 96:1-2; `ر ج ع` 96:8
- Synthesis: The claim initiates a social and legal attachment rather than a neutral statement. Once it adheres to another party, fabrication and reply become opposing operations within one dispute.

#### Subchannel C. Imputation and Refutation
- Reading type: mixed
- Scene or process: A person or statement is branded false, displayed for examination, and measured against recognized knowledge.
- Active motifs: imputation of falsehood `ك ذ ب:B002/m01`; deliberate display `ر ء ي:B012/m01`; recognition `ع ل م:B001/m02`; reply to accusation `ر ج ع:B005/m04`
- Ayah anchors: `ك ذ ب` 96:13, 96:16; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ع ل م` 96:4-5, 96:14; `ر ج ع` 96:8
- Synthesis: Imputation creates a disputed status, display makes the disputed object examinable, and recognition supplies the basis for refutation. Returned speech completes the adversarial exchange.

#### Subchannel D. The Deceiving and Self-Protective Self
- Reading type: mixed
- Scene or process: The inner self generates a misleading account, facilitates its own course, and encloses itself against correction.
- Active motifs: deceitful self `ك ذ ب:B008/m01`; self-protective enclosure `و ق ي:B002/m01`; inward facilitation `ط و ع:B006/m01`; self-assertion `د ع و:B002/m03`
- Ayah anchors: `ك ذ ب` 96:13, 96:16; `و ق ي` 96:12 (ٱلتَّقْوَى); `ط و ع` 96:19 (تُطِعْهُ); `د ع و` 96:17-18
- Synthesis: Deception is internalized as a self-maintaining process. The self makes its chosen action easy, asserts its account, and converts protection from harm into insulation from contradiction.

### 4. Origination, Shaping, and Material Form
- Semantic invariant: Form emerges through creation, measurement, cutting, smoothing, differentiation, and completion.
- Surface relation: direct; creation at 96:1-2 and teaching by the pen at 96:4 provide both origination and tool-mediated shaping.
- Surprising reach: The same formative logic reaches mirrors, pared edges, cleft surfaces, raised slabs, and solid barriers.

#### Subchannel A. Origination and Coming-to-Be
- Reading type: surface-primary
- Scene or process: Something is brought into occurrence, then nurtured toward a completed state.
- Active motifs: origination `خ ل ق:B002/m01`; temporal occurrence `ك و ن:B001/m01`; nurture and completion `ر ب ب:B002/m01`; completed form `خ ل ق:B003/m01`
- Ayah anchors: `خ ل ق` 96:1-2; `ك و ن` 96:11 (كَانَ); `ر ب ب` 96:1, 96:3, 96:8
- Synthesis: Creation initiates existence, occurrence places it in an actual time, and nurture carries it toward completion. The process therefore joins event, development, and finished form.

#### Subchannel B. Measuring, Paring, and Cutting to Fit
- Reading type: mixed
- Scene or process: A desired measure is established and hard material is pared or clipped until it conforms.
- Active motifs: estimation and measure `خ ل ق:B001/m01`; paring to level `ق ل م:B001/m01`; cutting shears `ق ل م:B006/m01`; bounded amount `ن ه ي:B010/m01`
- Ayah anchors: `خ ل ق` 96:1-2; `ق ل م` 96:4; `ن ه ي` 96:9, 96:15 (يَنْهَى، يَنْتَهِ)
- Synthesis: Measurement supplies the intended form, paring removes excess, and shears perform the controlled separation. The terminal amount defines when shaping is complete.

#### Subchannel C. Proportion, Appearance, and Reflection
- Reading type: latent/lexical
- Scene or process: A completed, proportioned body becomes available as an appearance and is duplicated in a reflecting surface.
- Active motifs: proportioned form `خ ل ق:B003/m02`; visible appearance `ر ء ي:B006/m01`; reflected likeness `ر ء ي:B006/m02`; recognition of form `ع ل م:B001/m04`
- Ayah anchors: `خ ل ق` 96:1-2; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ع ل م` 96:4-5, 96:14
- Synthesis: Proportion gives the object a stable outline, appearance presents that outline, and reflection repeats it. Recognition closes the scene by identifying the likeness as belonging to the formed object.

#### Subchannel D. Smooth Slabs, Raised Places, and Solid Blockage
- Reading type: latent/lexical
- Scene or process: Stone or ground is apprehended through surface qualities: level smoothness, elevation, or impenetrable closure.
- Active motifs: smooth level surface `خ ل ق:B008/m01`; imperforate rock `خ ل ق:B012/m01`; smooth slab `ط غ ي:B005/m01`; raised rocky place `ط غ و:B006/m01`; conspicuous elevation `س م و:B002/m01`
- Ayah anchors: `خ ل ق` 96:1-2; `ط غ ي` 96:6 (يَطْغَى); `ط غ و` has no separate surface token; `س م و` 96:1
- Synthesis: Smoothness and elevation make a slab visually distinct, while imperforation changes the same material into a barrier. The scene is a topology of stone in which surface and passage determine function.

#### Subchannel E. Clefts, Tips, and Deliberate Edges
- Reading type: latent/lexical
- Scene or process: A continuous surface is opened by a cleft or terminated in a pared point.
- Active motifs: visible cleft `ع ل م:B004/m01`; pared tip `ق ل م:B005/m01`; controlled trimming `ق ل م:B001/m02`
- Ayah anchors: `ع ل م` 96:4-5, 96:14; `ق ل م` 96:4
- Synthesis: The cleft marks where continuity fails, while paring deliberately creates a terminal edge. Together they form a compact morphology of opening, boundary, and point.

### 5. The Reproductive Sequence
- Semantic invariant: Animal and human life proceeds through mating, conception, gestation, visible signs, birth, milk, fostering, and separation of the young.
- Surface relation: direct; 96:2 names human creation from `عَلَق`, and the lexical branches unfold that compact origin into a full reproductive cycle.
- Surprising reach: The sequence includes estrus, pregnancy verification, milk interruption, foster care, and weaning.

#### Subchannel A. Mating and Conception
- Reading type: latent/lexical
- Scene or process: An animal enters estrus, the male mounts, and a conception becomes fixed in the womb.
- Active motifs: estrus `ق ر ء:B009/m01`; mounting male `س م و:B003/m01`; fixed conception `ع ل ق:B009/m01`; checking pregnancy `ر ج ع:B013/m01`
- Ayah anchors: `ق ر ء` 96:1, 96:3; `س م و` 96:1; `ع ل ق` 96:2; `ر ج ع` 96:8
- Synthesis: Estrus supplies reproductive readiness, mounting supplies contact, and the fastening sense of conception supplies the outcome. Rechecking the animal turns an initially hidden event into a monitored state.

#### Subchannel B. Gestation, Bodily Signs, and Imminent Birth
- Reading type: mixed
- Scene or process: The womb gathers its contents, pregnancy becomes visible, and detention in gestation ends as birth approaches.
- Active motifs: gathered womb contents `ق ر ء:B003/m01`; visible pregnancy `ر ء ي:B010/m01`; gestational holding `ق ر ء:B004/m01`; imminent birth `ق ر ب:B012/m01`; menstrual sign `ر ء ي:B007/m01`
- Ayah anchors: `ق ر ء` 96:1, 96:3; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ق ر ب` 96:19; `ع ل ق` 96:2
- Synthesis: Gathering and holding describe the interior process, menstrual and visible-pregnancy signs disclose its condition, and nearness changes from spatial relation into the approach of delivery.

#### Subchannel C. Milk, Fosterage, and Maternal Substitution
- Reading type: latent/lexical
- Scene or process: A caregiver or surrogate tends the young while milk starts, is withheld, or fails.
- Active motifs: foster caregiver `ر ب ب:B005/m01`; first call of milk `د ع و:B003/m01`; surrogate dam withholding milk `ع ل ق:B010/m01`; milk ceasing `ك ذ ب:B006/m01`
- Ayah anchors: `ر ب ب` 96:1, 96:3, 96:8; `د ع و` 96:17-18; `ع ل ق` 96:2; `ك ذ ب` 96:13, 96:16
- Synthesis: Fosterage provides the social role, while the milk branches describe the resource on which care depends. Initiation, withholding, and cessation make nourishment a changing process rather than a static possession.

#### Subchannel D. Young Animals, Nurture, and Weaning
- Reading type: latent/lexical
- Scene or process: A newly born lamb or ewe is tended, matured, and eventually separated from the older stock.
- Active motifs: young lamb `ء م ر:B009/m01`; newly delivered ewe `ر ب ب:B009/m01`; nurture to completion `ر ب ب:B002/m01`; separation of young stock `و ل ي:B015/m01`
- Ayah anchors: `ء م ر` 96:12; `ر ب ب` 96:1, 96:3, 96:8; `و ل ي` 96:13
- Synthesis: Newness identifies the dependent animal, nurture carries it through early development, and sequential separation marks weaning. The process converts biological birth into managed herd continuity.

### 6. Marriage, Kinship, and Household Bond
- Semantic invariant: Social continuity is created and altered through marriage, return or separation, descent, covenant, clientage, and care for dependents.
- Surface relation: indirect; human identity at 96:2, claimed self-sufficiency at 96:7, return at 96:8, and turning away at 96:13 activate lexical branches concerned with dependence and relational status.
- Surprising reach: The channel moves from bridal transfer to suspended marriage, foster relations, oath-bound alliance, manumission, and household surety.

#### Subchannel A. Bridal Transfer and Marriage
- Reading type: latent/lexical
- Scene or process: A woman recognized for beauty or independence is transferred as a bride and enters marriage through a gift-bearing social act.
- Active motifs: marriageable woman `غ ن ي:B005/m01`; marriage `غ ن ي:B006/m01`; bride led to her spouse `ه د ي:B006/m01`; reciprocal bridal gift `ك ر م:B008/m01`
- Ayah anchors: `غ ن ي` 96:7; `ه د ي` 96:11; `ك ر م` 96:3
- Synthesis: Marriage changes status, bridal guidance supplies the public transfer, and the recompense-seeking gift places the union inside a reciprocal social economy.

#### Subchannel B. Suspension, Separation, and Marital Return
- Reading type: latent/lexical
- Scene or process: A spouse is left between marriage and singleness, may become fully separated, or may be restored to the household.
- Active motifs: suspended wife `ع ل ق:B008/m01`; marital return `ر ج ع:B004/m01`; spouseless separation `ق ل م:B009/m01`
- Ayah anchors: `ع ل ق` 96:2; `ر ج ع` 96:8; `ق ل م` 96:4
- Synthesis: Suspension names the unstable middle state, separation resolves it toward singleness, and return resolves it toward renewed household membership.

#### Subchannel C. Descent, Clientage, and Covenant
- Reading type: latent/lexical
- Scene or process: Kinship or claimed descent is extended by oath, covenant, neighborhood, manumission, and alliance.
- Active motifs: blood kinship `ق ر ب:B003/m01`; clientage and manumission `و ل ي:B005/m01`; covenant `ر ب ب:B011/m01`; binding oath `ء ل ي:B007/m01`; lineage assertion `د ع و:B002/m02`
- Ayah anchors: `ق ر ب` 96:19; `و ل ي` 96:13; `ر ب ب` 96:1, 96:3, 96:8; `ء ل ي` 96:8 (إِلَى); `د ع و` 96:17-18
- Synthesis: Descent supplies inherited proximity, while oath and covenant create chosen proximity. Clientage and manumission show how the resulting bond can reorganize legal belonging beyond blood.

#### Subchannel D. Dependents, Care, and Surety
- Reading type: latent/lexical
- Scene or process: A household head holds wealth and dependents, assumes care, and guarantees another person's standing.
- Active motifs: wealth and dependents `ق ر ء:B013/m01`; ward or stepchild `ر ب ب:B005/m02`; guardianship `و ل ي:B003/m02`; surety `ك و ن:B003/m01`
- Ayah anchors: `ق ر ء` 96:1, 96:3; `ر ب ب` 96:1, 96:3, 96:8; `و ل ي` 96:13; `ك و ن` 96:11
- Synthesis: Dependents create an obligation, guardianship supplies ongoing administration, and surety makes the caregiver answerable for another. The ward motif gives the household relation a concrete recipient.

### 7. Devotion and Consecrated Approach
- Semantic invariant: A worshipper recognizes sovereignty, adopts a posture of service, and approaches through prayer, prostration, offering, and consecrated preparation.
- Surface relation: direct; lordship and the divine name at 96:1, 96:3, 96:8, and 96:14, prayer at 96:10, and prostration with approach at 96:19 establish the channel.
- Surprising reach: Worship opens into sacred places, sanctuary livestock, fragrant anointment, aloeswood, and perfume grinding.

#### Subchannel A. Lordship, Invocation, and Worship
- Reading type: surface-primary
- Scene or process: The divine is named and invoked as sovereign, and the human participant answers as servant and worshipper.
- Active motifs: divine invocation `ء ل ه:B002/m01`; sovereignty `ر ب ب:B001/m01`; worshipped deity `ء ل ه:B001/m01`; submissive worship `ع ب د:B003/m01`; blessing and praise `ص ل و:B002/m01`
- Ayah anchors: `ء ل ه` 96:14 (ٱللَّهَ); `ر ب ب` 96:1, 96:3, 96:8; `ع ب د` 96:10 (عَبْدًا); `ص ل و` 96:10 (صَلَّى)
- Synthesis: Naming identifies the sovereign, invocation addresses that sovereignty, and servanthood defines the human role. Praise and blessing turn recognition into an enacted relation.

#### Subchannel B. Prayer, Prostration, and Sacred Place
- Reading type: surface-primary
- Scene or process: A worshipper enters a designated place, lowers the body, and performs prayer through prostration.
- Active motifs: prescribed prayer `ص ل و:B003/m01`; bodily lowering `س ج د:B001/m01`; place of prostration `س ج د:B002/m01`; house of worship `ص ل و:B007/m01`; prostrating limbs and mark `س ج د:B003/m01`
- Ayah anchors: `ص ل و` 96:10; `س ج د` 96:19; `ع ب د` 96:10
- Synthesis: Place, posture, limbs, and act form one ritual scene. The bodily mark extends a momentary prostration into a visible trace carried after worship.

#### Subchannel C. Offering and Sanctuary Approach
- Reading type: mixed
- Scene or process: A gift or animal is brought near, directed toward sanctuary, and converted into an offering.
- Active motifs: approach-offering `ق ر ب:B005/m01`; sanctuary animal `ه د ي:B005/m01`; bestowed gift `ء ل ي:B012/m01`; devotional companionship `ء ن س:B003/m01`
- Ayah anchors: `ق ر ب` 96:19; `ه د ي` 96:11; `ء ل ي` 96:8 (إِلَى); `ء ن س` 96:2, 96:5-6
- Synthesis: Nearness becomes ritual transfer: a gift is directed toward a sacred destination, and the offered animal embodies that movement. Companionship supplies the relational aim of restored nearness.

#### Subchannel D. Fragrance, Aloeswood, and Ritual Grinding
- Reading type: latent/lexical
- Scene or process: Aromatic material is ground on stone, compounded, and applied in a setting of honor or worship.
- Active motifs: fragrant anointment `خ ل ق:B010/m01`; perfume mortar `ع ب د:B012/m01`; grinding slab `ص ل و:B008/m01`; aloeswood `ء ل ي:B014/m01`; worship place `ص ل و:B007/m02`
- Ayah anchors: `خ ل ق` 96:1-2; `ع ب د` 96:10; `ص ل و` 96:10; `ء ل ي` 96:8 (إِلَى)
- Synthesis: Aloeswood supplies aromatic material, mortar and slab supply the preparation mechanism, and anointment supplies the outcome. Its repeated attachment to worship places turns fragrance into consecrated atmosphere.

### 8. Authority, Obedience, and Restraint
- Semantic invariant: Conduct is regulated by command, moral inhibition, willing submission, refusal, and coercive enforcement.
- Surface relation: direct; transgression at 96:6, prohibition at 96:9 and 96:15, command to piety at 96:12, denial and turning away at 96:13, forelock seizure at 96:15-16, and non-obedience at 96:19 form the surface sequence.
- Surprising reach: Regulation extends from conscience and repentance to repulsion, striking, enslavement, and submission at an endpoint.

#### Subchannel A. Command and Moral Inhibition
- Reading type: surface-primary
- Scene or process: An authority imposes a requirement, while reason and protective restraint inhibit a prohibited act.
- Active motifs: binding command `ء م ر:B002/m01`; prohibition `ن ه ي:B001/m01`; morally restraining reason `ن ه ي:B003/m01`; protective restraint `و ق ي:B001/m01`
- Ayah anchors: `ء م ر` 96:12; `ن ه ي` 96:9, 96:15; `و ق ي` 96:12
- Synthesis: Command supplies positive direction, prohibition blocks an opposing action, and reason internalizes the restraint. Protection frames inhibition as preservation rather than mere stoppage.

#### Subchannel B. Obedience, Submission, and Prostration
- Reading type: surface-primary
- Scene or process: A participant consents, yields status, lowers the body, and carries out an act under authority.
- Active motifs: obedience `ط و ع:B001/m01`; concurrence `ط و ع:B002/m01`; submissive worship `ع ب د:B003/m01`; abasement `ك و ن:B004/m01`; bodily lowering `س ج د:B001/m01`
- Ayah anchors: `ط و ع` 96:19; `ع ب د` 96:10; `ك و ن` 96:11; `س ج د` 96:19
- Synthesis: Concurrence marks assent, obedience turns assent into action, and lowering makes the changed rank visible. Worship gives submission a chosen sacred form.

#### Subchannel C. Refusal, Turning Away, and Transgression
- Reading type: surface-primary
- Scene or process: A subject crosses a limit, refuses direction, and turns away from an imposed or recognized claim.
- Active motifs: moral excess `ط غ ي:B001/m01`; refusal and retreat `و ل ي:B007/m01`; crossing the correct boundary `خ ط ء:B001/m01`; rejected prohibition `ن ه ي:B001/m02`
- Ayah anchors: `ط غ ي` 96:6; `و ل ي` 96:13; `خ ط ء` 96:16; `ن ه ي` 96:9, 96:15
- Synthesis: Transgression is a boundary crossing, refusal is a directional reversal, and turning away gives that reversal a bodily image. Prohibition remains the limit against which the refusal is legible.

#### Subchannel D. Forelock Seizure and Repulsive Force
- Reading type: surface-primary
- Scene or process: An offending person is seized at the forelock, physically driven back, and struck or restrained.
- Active motifs: forelock seizure `س ف ع:B001/m01`; grasped forelock `ن ص ي:B001/m01`; repulsion `ز ب ن:B001/m01`; striking `س ف ع:B004/m01`; enforced stoppage `ن ه ي:B001/m03`
- Ayah anchors: `س ف ع` 96:15; `ن ص ي` 96:15-16; `ز ب ن` 96:18; `ن ه ي` 96:9, 96:15
- Synthesis: The forelock supplies the point of control, repulsion supplies directed force, and striking supplies enforcement. The lexical scene concretizes moral restraint as capture and bodily displacement.

#### Subchannel E. Wrongdoing, Return, and Desistance
- Reading type: mixed
- Scene or process: A wrong is recognized, the actor turns back from it, and pursuit of the former course ceases.
- Active motifs: sinful error `خ ط ء:B002/m01`; repentance and reversal `ر ج ع:B003/m01`; desistance `ن ه ي:B007/m01`; turning away from a course `و ل ي:B007/m02`
- Ayah anchors: `خ ط ء` 96:16; `ر ج ع` 96:8; `ن ه ي` 96:9, 96:15; `و ل ي` 96:13
- Synthesis: Error establishes the defective course, return reverses its direction, and desistance prevents renewed pursuit. The same turning image can therefore express culpable refusal or corrective repentance according to its object.

### 9. Council, Assembly, and Rank
- Semantic invariant: People become a public body by gathering, calling, deliberating, assigning rank, or dispersing into absence.
- Surface relation: direct; 96:17 names a caller and his club or council, while 96:18 answers with a counter-summons.
- Surprising reach: The social field includes multitudes, empty dwellings, intimate retainers, court privilege, leadership, and delegated office.

#### Subchannel A. Forum and Deliberative Council
- Reading type: mixed
- Scene or process: People meet face to face in a recognized forum and deliberate over an affair.
- Active motifs: public council `ن د و:B001/m01`; gathering place `ن د ي:B003/m01`; consultation `ء م ر:B007/m01`; face-to-face encounter `ر ء ي:B004/m01`
- Ayah anchors: `ن د و` 96:17; `ن د ي` has no separate surface token; `ء م ر` 96:12; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: The forum supplies place and participants, facing supplies reciprocal visibility, and consultation supplies the joint operation. The result is a social decision scene rather than an undifferentiated crowd.

#### Subchannel B. Summons and Assembly
- Reading type: mixed
- Scene or process: A raised call draws separate people into a gathered body.
- Active motifs: summons `د ع و:B001/m01`; raised call `ن د و:B002/m01`; multitude `ر ب ب:B004/m01`; collection `ق ر ء:B001/m02`
- Ayah anchors: `د ع و` 96:17-18; `ن د و` 96:17; `ر ب ب` 96:1, 96:3, 96:8; `ق ر ء` 96:1, 96:3
- Synthesis: Voice initiates movement toward a center, collection supplies the converging action, and multitude names the resulting body. The two surface summons sharpen this into competing mobilizations.

#### Subchannel C. Dispersal and the Empty Dwelling
- Reading type: latent/lexical
- Scene or process: A former group scatters until the dwelling has neither caller nor inhabitant.
- Active motifs: dispersal in different directions `ع ب د:B010/m01`; scattered remnants `ن د ي:B012/m01`; empty house `د ع و:B008/m01`; nobody present `ز ب ن:B007/m01`
- Ayah anchors: `ع ب د` 96:10; `ن د ي` has no separate surface token; `د ع و` 96:17-18; `ز ب ن` 96:18
- Synthesis: Dispersal is the process, scattered remnants are its spatial trace, and the silent house is its social outcome. Absence is defined concretely by the disappearance of both speaker and audience.

#### Subchannel D. Elite, Leader, and Court Intimate
- Reading type: latent/lexical
- Scene or process: A selected person advances at the front, gains privileged proximity, and serves as an intimate of power.
- Active motifs: chosen elite `ن ص ي:B003/m01`; leading front `ه د ي:B003/m01`; court favorite `ق ر ب:B004/m01`; intimate confidant `ء ن س:B006/m01`
- Ayah anchors: `ن ص ي` 96:15-16; `ه د ي` 96:11; `ق ر ب` 96:19; `ء ن س` 96:2, 96:5-6
- Synthesis: Selection differentiates the elite, precedence gives that person a leading position, and nearness to authority becomes court privilege. Intimacy describes the social access produced by rank.

#### Subchannel E. Governance and Delegated Care
- Reading type: mixed
- Scene or process: A ruler or officeholder assumes an affair and becomes responsible for its administration.
- Active motifs: political authority `ء م ر:B003/m01`; holding office `و ل ي:B003/m01`; affair under rule `ء م ر:B001/m02`; lordly sovereignty `ر ب ب:B001/m02`; delegated surety `ك و ن:B003/m02`
- Ayah anchors: `ء م ر` 96:12; `و ل ي` 96:13; `ر ب ب` 96:1, 96:3, 96:8; `ك و ن` 96:11
- Synthesis: The affair supplies an object of administration, office assigns a responsible agent, and sovereignty supplies the hierarchy above that agent. Surety extends governance into answerability for those placed under care.

### 10. Value, Gift, and Social Esteem
- Semantic invariant: Persons and goods acquire social value through honor, attachment, generosity, reciprocal giving, praise, and rivalry.
- Surface relation: direct; the divine superlative `ٱلْأَكْرَمُ` at 96:3 and the claim of self-sufficiency at 96:7 place generosity, worth, and independence on the surface.
- Surprising reach: Esteem attaches to treasured objects, gracious answers, gifts seeking recompense, public boasting, and reputational sound.

#### Subchannel A. Precious Attachment and Veneration
- Reading type: mixed
- Scene or process: A valued object or person is held close, treated as precious, and publicly honored.
- Active motifs: precious attachment `ع ل ق:B007/m01`; beloved rarity `ك ر م:B010/m01`; veneration `ع ب د:B006/m01`; honorable worth `ك ر م:B001/m01`
- Ayah anchors: `ع ل ق` 96:2; `ك ر م` 96:3; `ع ب د` 96:10
- Synthesis: Attachment supplies possession and emotional closeness, preciousness supplies scarcity, and veneration converts private value into public treatment.

#### Subchannel B. Gift, Assignment, and Recompense
- Reading type: latent/lexical
- Scene or process: A gift is sent or assigned to another with an expectation of affection, return, or recompense.
- Active motifs: bestowal `ء ل ي:B012/m01`; affectionate gift `ه د ي:B004/m01`; recompense-seeking gift `ك ر م:B008/m01`; assigned benefit or harm `و ل ي:B013/m01`
- Ayah anchors: `ء ل ي` 96:8 (إِلَى); `ه د ي` 96:11; `ك ر م` 96:3; `و ل ي` 96:13
- Synthesis: Bestowal initiates transfer, the dispatched gift gives it a recipient and route, and expected recompense makes the act reciprocal. Assignment shows that transfer can carry either favor or burden.

#### Subchannel C. Generosity, Favor, and Prosperity
- Reading type: mixed
- Scene or process: Abundant giving produces favor, growth, and a condition in which need is relieved.
- Active motifs: openhanded generosity `ن د و:B004/m01`; growth and blessing `ء م ر:B004/m01`; divine favors `ء ل ي:B006/m01`; favor relieving a need `ر ب ب:B016/m03`; noble generosity `ك ر م:B001/m02`
- Ayah anchors: `ن د و` 96:17; `ء م ر` 96:12; `ء ل ي` 96:8 (إِلَى); `ر ب ب` 96:1, 96:3, 96:8; `ك ر م` 96:3
- Synthesis: Giving is pictured as an abundance that nourishes growth. Favor is the received outcome, while relief of need shows prosperity at the level of the beneficiary.

#### Subchannel D. Rivalry, Ostentation, and Reputation
- Reading type: mixed
- Scene or process: Competitors display themselves, boast of excellence, and seek a reputation that travels beyond the encounter.
- Active motifs: rivalry `س م و:B007/m01`; boastful contest in generosity `ك ر م:B006/m01`; ostentatious display `ر ء ي:B005/m01`; spreading repute `س م و:B008/m01`
- Ayah anchors: `س م و` 96:1; `ك ر م` 96:3; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: Rivalry supplies opposing agents, ostentation supplies display, boasting supplies the claim to superiority, and reputation is the social residue that persists after the contest.

### 11. Orientation, Nearness, and Completion
- Semantic invariant: Relations are organized by direction, distance, contact, return, succession, and arrival at a limit.
- Surface relation: direct; return to the Lord at 96:8, turning away at 96:13, and the imperative to approach at 96:19 make directed relation central to the surface.
- Surprising reach: Spatial nearness expands into bodily facing, residence, temporal imminence, race order, and goal attainment.

#### Subchannel A. Facing and Direction
- Reading type: mixed
- Scene or process: A body presents its inward side, turns its face, and adopts a direction or intended course.
- Active motifs: inward-facing side `ء ن س:B004/m01`; turning the face `و ل ي:B006/m01`; direction `ه د ي:B002/m01`; attentive sight `ر ء ي:B001/m02`
- Ayah anchors: `ء ن س` 96:2, 96:5-6; `و ل ي` 96:13; `ه د ي` 96:11; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14
- Synthesis: Orientation begins in anatomy, becomes a deliberate turn, and culminates in a chosen direction. Sight aligns attention with the body's facing.

#### Subchannel B. Nearness, Adjacency, and Contact
- Reading type: surface-primary
- Scene or process: Separate entities close distance, become adjacent without an interval, and may enter direct contact.
- Active motifs: nearness `ق ر ب:B001/m01`; interval-free adjacency `و ل ي:B001/m01`; contact and engagement `ق ر ب:B007/m01`; kinship nearness `ق ر ب:B003/m02`
- Ayah anchors: `ق ر ب` 96:19; `و ل ي` 96:13
- Synthesis: Nearness is the approach, adjacency is the resulting position, and contact is the intensified relation. Kin proximity shows how the same spatial structure can organize social belonging.

#### Subchannel C. Return, Abiding, and Residence
- Reading type: mixed
- Scene or process: A moving subject reverses course, reaches a place, and remains there.
- Active motifs: return `ر ج ع:B001/m01`; abiding `ر ب ب:B007/m01`; dwelling in a place `غ ن ي:B004/m01`; place and station `ك و ن:B002/m01`
- Ayah anchors: `ر ج ع` 96:8; `ر ب ب` 96:1, 96:3, 96:8; `غ ن ي` 96:7; `ك و ن` 96:11
- Synthesis: Return supplies directional reversal, place supplies a destination, and abiding changes arrival into residence. The surface `ٱلرُّجْعَى` thus opens both eschatological and locative readings.

#### Subchannel D. Endpoint and Attainment
- Reading type: mixed
- Scene or process: Movement proceeds toward a terminal boundary that can be reached, possessed, or completed.
- Active motifs: endpoint `ء ل ي:B001/m01`; terminal limit `ن ه ي:B002/m01`; goal attainment `و ل ي:B012/m01`; imminent completion `ق ر ب:B002/m01`
- Ayah anchors: `ء ل ي` 96:8 (إِلَى); `ن ه ي` 96:9, 96:15; `و ل ي` 96:13; `ق ر ب` 96:19
- Synthesis: Endpoint defines the boundary, imminence describes the approach, and attainment names successful arrival. The same structure supports spatial, temporal, and purposive completion.

#### Subchannel E. Succession, Gait, and Race Order
- Reading type: latent/lexical
- Scene or process: Bodies move in sequence, one follows another, and gait determines position in a race or procession.
- Active motifs: succession `و ل ي:B002/m01`; second horse `ص ل و:B006/m01`; trotting approach `ق ر ب:B014/m01`; animal gait `ر ج ع:B008/m01`; swaying walk `ه د ي:B008/m01`
- Ayah anchors: `و ل ي` 96:13; `ص ل و` 96:10; `ق ر ب` 96:19; `ر ج ع` 96:8; `ه د ي` 96:11
- Synthesis: Succession supplies order, gait supplies the repeated motion that maintains it, and the second horse makes relative position explicit. Swaying and trotting are contrasting realizations of patterned advance.

### 12. Readiness, Need, and Sufficiency
- Semantic invariant: Action depends on fitness, acquired capacity, effort, provision, and the point at which need is adequately met.
- Surface relation: direct; perceived self-sufficiency at 96:7, command to protective piety at 96:12, and obedience at 96:19 place capacity and dependence in explicit tension.
- Surprising reach: The channel includes vocation, beginning a task, food need, subsistence fodder, surety, and voluntary exertion.

#### Subchannel A. Aptitude, Entitlement, and Undertaking
- Reading type: latent/lexical
- Scene or process: A suitable agent is judged fit, gains priority, and begins the assigned action.
- Active motifs: fitness `خ ل ق:B005/m01`; beginning an undertaking `ع ل ق:B016/m01`; entitlement `و ل ي:B008/m01`; intended course `ه د ي:B002/m02`
- Ayah anchors: `خ ل ق` 96:1-2; `ع ل ق` 96:2; `و ل ي` 96:13; `ه د ي` 96:11
- Synthesis: Fitness answers who can act, entitlement answers who should act, intention gives the action direction, and commencement changes potential into execution.

#### Subchannel B. Capacity and Exertion
- Reading type: mixed
- Scene or process: Ability is present or deliberately acquired, then expended as effort.
- Active motifs: capacity `ء ل ي:B011/m01`; practical ability `ط و ع:B003/m01`; taking on ability `ط و ع:B004/m01`; exertion `ء ل ي:B010/m01`; bodily strength `ع ب د:B007/m01`
- Ayah anchors: `ء ل ي` 96:8 (إِلَى); `ط و ع` 96:19; `ع ب د` 96:10
- Synthesis: Capacity is the available resource, taking on ability is its acquisition, strength is its bodily substrate, and exertion is its expenditure toward a task.

#### Subchannel C. Subsistence and Provision
- Reading type: latent/lexical
- Scene or process: Food need motivates effort, while a small provision or ready pasture sustains dependents and animals.
- Active motifs: food need `ز ب ن:B006/m01`; minimal subsistence `ع ل ق:B006/m01`; wealth and dependents `ق ر ء:B013/m01`; ready pasture `ط و ع:B007/m01`
- Ayah anchors: `ز ب ن` 96:18; `ع ل ق` 96:2; `ق ر ء` 96:1, 96:3; `ط و ع` 96:19
- Synthesis: Need is the deficit, provision is the portable remedy, and pasture is the environmental remedy. Dependents make adequacy a household responsibility rather than an individual state.

#### Subchannel D. Adequacy and Independence
- Reading type: surface-primary
- Scene or process: Provision reaches a sufficient level, further seeking stops, and the possessor experiences independence.
- Active motifs: adequacy `غ ن ي:B002/m01`; sufficient endpoint `ن ه ي:B005/m01`; independence `غ ن ي:B001/m01`; cessation of seeking `ن ه ي:B007/m01`
- Ayah anchors: `غ ن ي` 96:7; `ن ه ي` 96:9, 96:15
- Synthesis: Adequacy names the threshold, cessation marks its behavioral effect, and independence names the resulting social condition. The surface warns that perceived independence can also misrecognize continuing dependence.

#### Subchannel E. Care, Guarantee, and Protective Support
- Reading type: mixed
- Scene or process: A responsible party guarantees another, supplies what is lacking, and protects against breakdown.
- Active motifs: surety `ك و ن:B003/m01`; adequate support `غ ن ي:B002/m02`; nurture `ر ب ب:B002/m02`; protection from harm `و ق ي:B001/m01`
- Ayah anchors: `ك و ن` 96:11; `غ ن ي` 96:7; `ر ب ب` 96:1, 96:3, 96:8; `و ق ي` 96:12
- Synthesis: Surety assigns responsibility, nurture supplies continued care, adequacy defines the required outcome, and protection preserves the supported person from loss.

### 13. Water, Rain, and Fertile Ground
- Semantic invariant: Water descends, surges, gathers, is drawn or carried, and turns ground into pasture and ripened growth.
- Surface relation: indirect; the transgression root at 96:6 carries a flood sense, generosity at 96:3 carries fertile rain, and approach at 96:19 carries a watering-place sense.
- Surprising reach: The hydrological scene includes cloud cover, seasonal rain, terminal pools, wells, pulleys, waterskins, herd watering, and overripe fruit.

#### Subchannel A. Cloud, Rain, and Seasonal Succession
- Reading type: latent/lexical
- Scene or process: Cloud cover gathers overhead, rain returns to the ground, and one seasonal shower follows another.
- Active motifs: cloud bank `ر ب ب:B008/m01`; overhanging sky `س م و:B004/m01`; returning rain `ر ج ع:B006/m01`; following seasonal rain `و ل ي:B010/m01`; dew and rainfall `ن د و:B003/m01`
- Ayah anchors: `ر ب ب` 96:1, 96:3, 96:8; `س م و` 96:1; `ر ج ع` 96:8; `و ل ي` 96:13; `ن د و` 96:17
- Synthesis: The cloud is the source, descent is the event, return expresses recurrence, and following rain creates seasonal order. Dew supplies the gentler end of the same moisture continuum.

#### Subchannel B. Flood, Gathering Water, and Terminal Pool
- Reading type: latent/lexical
- Scene or process: Water rises beyond bounds, flows with force, and settles where the channel terminates.
- Active motifs: overpowering flood `ط غ ي:B002/m01`; water exceeding its limit `ط غ و:B002/m01`; terminal pool `ن ه ي:B004/m01`; gathered great water `ع ل م:B005/m01`
- Ayah anchors: `ط غ ي` 96:6; `ط غ و` has no separate surface token; `ن ه ي` 96:9, 96:15; `ع ل م` 96:4-5, 96:14
- Synthesis: Excess and force describe the moving flood, while the terminal pool supplies its endpoint. The gathered-water motif scales the result from a local basin to a broad body of water.

#### Subchannel C. Well, Pulley, and Waterskin
- Reading type: latent/lexical
- Scene or process: Water is retained in an excavation, lifted by suspended gear, and transferred into a portable skin.
- Active motifs: water-holding well `خ ل ق:B011/m01`; suspended pulley `ع ل ق:B002/m01`; waterskin `ق ر ب:B009/m01`; abundant water `ر ب ب:B013/m01`
- Ayah anchors: `خ ل ق` 96:1-2; `ع ل ق` 96:2; `ق ر ب` 96:19; `ر ب ب` 96:1, 96:3, 96:8
- Synthesis: The well supplies storage, the pulley supplies mechanical lift, and the waterskin supplies transport. Abundance describes the resource before it is divided into usable loads.

#### Subchannel D. Rain-Fed Pasture and Plant Growth
- Reading type: latent/lexical
- Scene or process: Fertile rain prepares soil, plants emerge, and pasture becomes available to grazing animals.
- Active motifs: fertile rain and soil `ك ر م:B002/m01`; general plant growth `ر ب ب:B012/m01`; fodder grass `ن ص ي:B004/m01`; camel pasture `ص ل و:B009/m01`; herb outside the main stock `ق ل م:B007/m01`
- Ayah anchors: `ك ر م` 96:3; `ر ب ب` 96:1, 96:3, 96:8; `ن ص ي` 96:15-16; `ص ل و` 96:10; `ق ل م` 96:4
- Synthesis: Rain changes the condition of the soil, plant motifs specify the resulting vegetation, and pasture gives that growth an ecological consumer. The stray herb preserves diversity within the field.

#### Subchannel E. Watering Circuit and Ripening
- Reading type: latent/lexical
- Scene or process: Herds travel between water and pasture while fruit or herbage advances from readiness to over-ripeness.
- Active motifs: night approach to water `ق ر ب:B008/m01`; herd watering circuit `ن د و:B006/m01`; ready pasture and fruit `ط و ع:B007/m01`; overripe drying fruit `و ل ي:B016/m01`
- Ayah anchors: `ق ر ب` 96:19; `ن د و` 96:17; `ط و ع` 96:19; `و ل ي` 96:13
- Synthesis: Watering and grazing form a repeated route, while ripening supplies the parallel temporal cycle of the field. Readiness is the usable interval before drying and decline.

### 14. Bodily Signs, Illness, and Vitality
- Semantic invariant: Internal condition becomes legible through breath, blood, pain, bodily marks, weakness, or fullness.
- Surface relation: indirect; `عَلَق` at 96:2, seeing at 96:7-14, and the forelock at 96:15-16 activate concrete physiological and diagnostic branches.
- Surprising reach: The channel includes lung disease, epidemic terrain, menstruation, leech treatment, cleft tissue, flank pain, hip sockets, and corpulence.

#### Subchannel A. Lung Ailment and Epidemic Environment
- Reading type: latent/lexical
- Scene or process: A diseased environment affects breathing, produces torpor, and calls for bodily protection.
- Active motifs: lung and its ailment `ر ء ي:B009/m01`; epidemic land `ق ر ء:B008/m01`; protective enclosure `و ق ي:B002/m02`; sluggish weakness `ه د ي:B009/m01`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ق ر ء` 96:1, 96:3; `و ق ي` 96:12; `ه د ي` 96:11
- Synthesis: The epidemic supplies the setting, the lung supplies the affected organ, torpor supplies the state, and protection supplies the response.

#### Subchannel B. Blood Sign and Therapeutic Leech
- Reading type: mixed
- Scene or process: Thick blood or cyclical discharge is observed, and a leech or tissue intervention is used to draw blood.
- Active motifs: clot or thick blood `ع ل ق:B003/m01`; medicinal leech `ع ل ق:B003/m02`; menstrual sign `ر ء ي:B007/m01`; leech bloodletting `ع ل ق:B012/m02`; cleft upper lip `ع ل م:B004/m01`
- Ayah anchors: `ع ل ق` 96:2; `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ع ل م` 96:4-5, 96:14
- Synthesis: Blood appears first as substance and diagnostic sign, then the leech changes role from bloodlike creature to therapeutic instrument. The cleft or treated tissue provides the bodily site of intervention.

#### Subchannel C. Belly, Flank, Back, and Hip Pain
- Reading type: latent/lexical
- Scene or process: Pain is localized by adjacent anatomical regions and the joints that bear movement.
- Active motifs: abdominal pang `ن ص ي:B006/m01`; flank `ق ر ب:B015/m01`; back and side `ص ل و:B005/m01`; hip socket `ك ر م:B007/m01`; hoof-protective response to pain `و ق ي:B003/m01`
- Ayah anchors: `ن ص ي` 96:15-16; `ق ر ب` 96:19; `ص ل و` 96:10; `ك ر م` 96:3; `و ق ي` 96:12
- Synthesis: The pang supplies sensation, flank and back supply location, and the hip socket supplies a load-bearing joint. Hoof protection extends the same pain-to-compensation process into animal biomechanics.

#### Subchannel D. Strength, Fullness, and Corpulence
- Reading type: latent/lexical
- Scene or process: Sustained nourishment becomes bodily firmness and reaches a terminal fullness.
- Active motifs: bodily strength `ع ب د:B007/m01`; extreme fatness `ن ه ي:B006/m01`; animal of noble lineage `ن د و:B007/m01`
- Ayah anchors: `ع ب د` 96:10; `ن ه ي` 96:9, 96:15; `ن د و` 96:17
- Synthesis: Strength names functional capacity, fatness names accumulated bodily reserve, and noble lineage provides the husbandry setting in which fullness is read as condition and value.

### 15. Textile, Marking, and Adornment
- Semantic invariant: Bodies and materials are covered, colored, worn, cut, marked, and ornamented so that surface appearance carries social meaning.
- Surface relation: indirect; the pen at 96:4, seeing and deceptive display at 96:7 and 96:13, and the forelock at 96:15-16 provide the surface hinges.
- Surprising reach: The channel joins bodices, dyed and iridescent cloth, fraying, recycled material, tattoo lines, combed hair, necklaces, and the neck itself.

#### Subchannel A. Dyed, Iridescent, and Deceptive Cloth
- Reading type: latent/lexical
- Scene or process: Cloth is dyed or woven with changing color, fitted to the body, and made capable of overstating its quality.
- Active motifs: dyed garment `س ف ع:B007/m01`; deceptive cloth `ك ذ ب:B009/m01`; iridescent fabric `ق ل م:B010/m01`; small bodice `ع ل ق:B015/m01`
- Ayah anchors: `س ف ع` 96:15; `ك ذ ب` 96:13, 96:16; `ق ل م` 96:4; `ع ل ق` 96:2
- Synthesis: Dye and iridescence create visual attraction, the bodice gives the fabric bodily placement, and deceptive appearance explains how surface can claim a value the material does not possess.

#### Subchannel B. Wear, Fraying, and Recycled Material
- Reading type: latent/lexical
- Scene or process: Repeated use removes a garment's nap, turns it into worn material, and redirects it into another use.
- Active motifs: worn cloth `خ ل ق:B009/m01`; returned or recycled matter `ر ج ع:B015/m01`; repair and completion `ر ب ب:B002/m03`; visible wear mark `ع ل م:B002/m02`
- Ayah anchors: `خ ل ق` 96:1-2; `ر ج ع` 96:8; `ر ب ب` 96:1, 96:3, 96:8; `ع ل م` 96:4-5, 96:14
- Synthesis: Fraying is the process, worn material is the changed object, and return becomes material reuse. Repair counters that decline, while visible marks retain the history of wear.

#### Subchannel C. Tattoo, Dark Trace, and Repeated Line
- Reading type: latent/lexical
- Scene or process: A line is repeatedly inscribed into a surface and darkened until it becomes a durable identifying trace.
- Active motifs: repeated tattoo line `ر ج ع:B009/m01`; black-red coloration `س ف ع:B002/m02`; pathlike trace `ن د ي:B013/m01`; distinguishing mark `ع ل م:B002/m03`
- Ayah anchors: `ر ج ع` 96:8; `س ف ع` 96:15; `ن د ي` has no separate surface token; `ع ل م` 96:4-5, 96:14
- Synthesis: Repetition lays down the line, coloration makes it visible, and the resulting trace acquires identifying force. The scene links inscription and bodily marking without collapsing either into generic writing.

#### Subchannel D. Hair, Forelock, and Grooming
- Reading type: mixed
- Scene or process: Hair is lengthened, combed, trimmed, or grasped at the front of the head.
- Active motifs: combed long hair `ن ص ي:B002/m01`; trimming `ق ل م:B001/m03`; forelock `ن ص ي:B001/m02`; grasping the forelock `س ف ع:B001/m01`
- Ayah anchors: `ن ص ي` 96:15-16; `ق ل م` 96:4; `س ف ع` 96:15
- Synthesis: Growth and combing describe care, trimming controls form, and grasping changes the groomed forelock into a point of domination. The surface punishment scene therefore touches a broader bodily-adornment system.

#### Subchannel E. Necklace, Neck, and Precious Attachment
- Reading type: latent/lexical
- Scene or process: A precious ornament is arranged around the neck and marks the wearer's status.
- Active motifs: necklace `ك ر م:B003/m01`; neck `ز ب ن:B008/m01`; precious attachment `ع ل ق:B007/m02`; public honor `ع ب د:B006/m02`
- Ayah anchors: `ك ر م` 96:3; `ز ب ن` 96:18; `ع ل ق` 96:2; `ع ب د` 96:10
- Synthesis: The neck supplies the support, the necklace supplies the object, attachment supplies fixation, and honor supplies the social meaning of wearing it.

### 16. Wildlife, Hunting, and Animal Movement
- Semantic invariant: Animals are identified, pursued, trapped, nourished, bred, and tracked through characteristic motion.
- Surface relation: indirect; transgression at 96:6 carries a young wild-cow branch, denial at 96:13 carries an animal run-and-halt branch, and approach at 96:19 carries equine motion.
- Surprising reach: The channel contains snares, raptors, shrikes, hyenas, lambs, herds, migration, halted flight, racing order, and hoof care.

#### Subchannel A. Hunt, Trap, and Captured Prey
- Reading type: latent/lexical
- Scene or process: A hunter goes out, sets a fixed snare, and holds an animal that has become entangled.
- Active motifs: going out to hunt `س م و:B006/m01`; snared prey `ع ل ق:B011/m01`; fixed hunting trap `ص ل و:B004/m01`; quarry that runs then halts `ك ذ ب:B007/m02`
- Ayah anchors: `س م و` 96:1; `ع ل ق` 96:2; `ص ل و` 96:10; `ك ذ ب` 96:13, 96:16
- Synthesis: The hunt supplies the agent and purpose, the fixed trap supplies the mechanism, and entanglement supplies the capture outcome. The quarry's run and halt describe the movement interrupted by capture.

#### Subchannel B. Raptors, Shrikes, and Foraging
- Reading type: latent/lexical
- Scene or process: Predatory birds range over a food field and secure the subsistence on which they live.
- Active motifs: falcon or hawk `ع ل م:B006/m01`; shrike `و ق ي:B005/m01`; subsistence portion `ع ل ق:B006/m02`; fodder plant `ن ص ي:B004/m02`
- Ayah anchors: `ع ل م` 96:4-5, 96:14; `و ق ي` 96:12; `ع ل ق` 96:2; `ن ص ي` 96:15-16
- Synthesis: The named birds supply agents, pasture supplies hunting terrain, and subsistence supplies the functional outcome. The channel is ecological rather than a simple list of species.

#### Subchannel C. Herd, Young Wild Animal, and Predator
- Reading type: latent/lexical
- Scene or process: Herd animals and their young occupy a field also traversed by a carnivorous predator.
- Active motifs: herd `ر ب ب:B014/m01`; young wild cow `ط غ و:B009/m01`; lamb `ء م ر:B009/m01`; male hyena `ع ل م:B007/m01`
- Ayah anchors: `ر ب ب` 96:1, 96:3, 96:8; `ط غ و` has no separate surface token; `ء م ر` 96:12; `ع ل م` 96:4-5, 96:14
- Synthesis: Herd and young animals supply vulnerable participants, while the hyena supplies the predator role. The scene places husbanded and wild life within one shared risk field.

#### Subchannel D. Chase, Halt, and Migration
- Reading type: latent/lexical
- Scene or process: An animal runs under pursuit, abruptly halts, or returns after seasonal movement.
- Active motifs: run then halt `ك ذ ب:B007/m01`; pursuit `س م و:B006/m02`; migrating birds returning `ر ج ع:B012/m01`; animal gait `ر ج ع:B008/m02`
- Ayah anchors: `ك ذ ب` 96:13, 96:16; `س م و` 96:1; `ر ج ع` 96:8
- Synthesis: Pursuit supplies external pressure, the halt interrupts flight, and migration supplies a larger cycle of departure and return. Gait is the repeated bodily mechanism common to each movement.

#### Subchannel E. Horse Pace, Race Position, and Hoof Care
- Reading type: latent/lexical
- Scene or process: A horse advances at a controlled pace, occupies a place in a race, and adjusts movement around hoof pain.
- Active motifs: trotting approach `ق ر ب:B014/m01`; swift running `ع ب د:B009/m01`; second horse `ص ل و:B006/m01`; hoof protection `و ق ي:B003/m01`
- Ayah anchors: `ق ر ب` 96:19; `ع ب د` 96:10; `ص ل و` 96:10; `و ق ي` 96:12
- Synthesis: Pace and speed determine race position, while hoof protection modifies movement to preserve the animal. The scene joins competitive order with the biomechanics that sustain it.

### 17. Measure, Allocation, and Exchange
- Semantic invariant: Goods, land, and chances are divided by counting, weighing, approximation, selection, and reciprocal transfer.
- Surface relation: indirect; the pen at 96:4 carries cutting and lot-arrow branches, return at 96:8 carries resale, and protective piety at 96:12 carries a weight-unit branch.
- Surprising reach: The channel includes lottery arrows, measured amounts, ounces, resale, image-bearing coins, and territorial sections.

#### Subchannel A. Lottery Vessel and Drawn Arrow
- Reading type: latent/lexical
- Scene or process: Prepared arrows are collected in a covered vessel and one is drawn to allocate an outcome.
- Active motifs: lot-arrow container `ر ب ب:B010/m01`; pared lot arrow `ق ل م:B004/m01`; polished shaft `خ ل ق:B008/m03`; vessel lid `ك ر م:B005/m01`
- Ayah anchors: `ر ب ب` 96:1, 96:3, 96:8; `ق ل م` 96:4; `خ ل ق` 96:1-2; `ك ر م` 96:3
- Synthesis: Paring and polishing prepare equivalent lots, the vessel conceals them, and the lid preserves uncertainty until selection. The apparatus converts crafted objects into a decision mechanism.

#### Subchannel B. Amount, Approximation, and Weight
- Reading type: latent/lexical
- Scene or process: A quantity is estimated, bounded, and expressed through a recognized unit of weight.
- Active motifs: estimation `خ ل ق:B001/m02`; approximate amount `ق ر ب:B016/m01`; numerical extent `ن ه ي:B010/m01`; ounce weight `و ق ي:B004/m01`
- Ayah anchors: `خ ل ق` 96:1-2; `ق ر ب` 96:19; `ن ه ي` 96:9, 96:15; `و ق ي` 96:12
- Synthesis: Estimation proposes a value, approximation admits a range, numerical extent sets a bound, and the ounce supplies a conventional standard.

#### Subchannel C. Resale, Return, and Replacement
- Reading type: latent/lexical
- Scene or process: A transferred good is returned, replaced, or sold onward at an assessed value.
- Active motifs: return or replacement in trade `ر ج ع:B011/m01`; resale `و ل ي:B014/m01`; approximate price `ق ر ب:B016/m02`; weight standard `و ق ي:B004/m02`
- Ayah anchors: `ر ج ع` 96:8; `و ل ي` 96:13; `ق ر ب` 96:19; `و ق ي` 96:12
- Synthesis: Return reverses the first transfer, resale redirects the good to a new party, and approximation with weight supplies valuation for the renewed exchange.

#### Subchannel D. Territorial Partition and Boundary Marking
- Reading type: latent/lexical
- Scene or process: Land is measured, cut into a section, and made recognizable by a boundary mark.
- Active motifs: measured layout `خ ل ق:B001/m03`; cut tract of land `ق ل م:B008/m01`; guiding boundary mark `ع ل م:B002/m04`; place and station `ك و ن:B002/m02`
- Ayah anchors: `خ ل ق` 96:1-2; `ق ل م` 96:4; `ع ل م` 96:4-5, 96:14; `ك و ن` 96:11
- Synthesis: Measurement establishes extent, cutting creates the tract, the mark distinguishes it, and place gives the partition a stable spatial identity.

#### Subchannel E. Image-Bearing Coin and Denomination
- Reading type: latent/lexical
- Scene or process: A struck image marks a coin whose value is related to a weight standard.
- Active motifs: image-bearing dirham `س ج د:B006/m01`; repeated engraving `ر ج ع:B009/m02`; ounce standard `و ق ي:B004/m03`; distinguishing sign `ع ل م:B002/m05`
- Ayah anchors: `س ج د` 96:19; `ر ج ع` 96:8; `و ق ي` 96:12; `ع ل م` 96:4-5, 96:14
- Synthesis: The engraved image identifies the coin, repeated marking records the production operation, and the weight standard anchors denomination. Sign and value coincide on one portable object.

### 18. Heat, Collapse, and Misfortune
- Semantic invariant: Material or circumstance is overtaken by force, producing controlled transformation, scorching, collapse, or calamity.
- Surface relation: indirect; prayer at 96:10 carries a fire branch, forelock seizure at 96:15 carries scorching and striking branches, and error at 96:16 opens the calamity sequence.
- Surprising reach: The channel contrasts cooking and aromatic preparation with destructive heat, cascading ruin, bodily breakdown, doom, and public disgrace.

#### Subchannel A. Controlled Heating and Preparation
- Reading type: latent/lexical
- Scene or process: Thick material is heated or roasted and may be ground into a prepared food or aromatic compound.
- Active motifs: thick syrup or paste `ر ب ب:B006/m01`; roasting heat `ص ل و:B001/m02`; grinding slab `ص ل و:B008/m01`; perfume mortar `ع ب د:B012/m01`
- Ayah anchors: `ر ب ب` 96:1, 96:3, 96:8; `ص ل و` 96:10; `ع ب د` 96:10
- Synthesis: Heat changes consistency, grinding reduces material, and the resulting paste or perfume is a controlled product. This is force used constructively.

#### Subchannel B. Scorch and Defensive Shelter
- Reading type: latent/lexical
- Scene or process: Fire or hot wind strikes the body or material, creating a need for protective enclosure.
- Active motifs: scorching blast `س ف ع:B003/m01`; exposure to fire `ص ل و:B001/m01`; self-protection `و ق ي:B002/m01`; blackened tinge `س ف ع:B002/m03`
- Ayah anchors: `س ف ع` 96:15; `ص ل و` 96:10; `و ق ي` 96:12
- Synthesis: The blast is the agent, exposure is the contact, darkening is the visible result, and shelter is the compensating response.

#### Subchannel C. Cascading Fall and Breakdown
- Reading type: latent/lexical
- Scene or process: One failing element pulls another down until an organized body or structure breaks apart.
- Active motifs: cascading collapse `د ع و:B005/m01`; breakdown and interruption `ع ب د:B011/m01`; succession `و ل ي:B002/m02`; cutting separation `ق ل م:B001/m04`
- Ayah anchors: `د ع و` 96:17-18; `ع ب د` 96:10; `و ل ي` 96:13; `ق ل م` 96:4
- Synthesis: Succession turns an initial fall into a chain, breakdown names loss of function, and cutting completes separation. The process can describe either built structure or organized activity.

#### Subchannel D. Vicissitude, Doom, and Disgrace
- Reading type: latent/lexical
- Scene or process: Adverse events attach themselves to a person, culminate in calamity, and leave a public condition of shame.
- Active motifs: vicissitudes `د ع و:B006/m01`; attached calamity or doom `ع ل ق:B014/m01`; overwhelming punishment `ط غ و:B005/m01`; disgrace `ن د و:B005/m01`
- Ayah anchors: `د ع و` 96:17-18; `ع ل ق` 96:2; `ط غ و` has no separate surface token; `ن د و` 96:17
- Synthesis: Vicissitude supplies repeated adversity, attachment makes the calamity inescapably personal, punishment supplies culmination, and disgrace supplies the social aftermath.

### 19. Imaginal and Unseen Presence
- Semantic invariant: A figure appears to perception without ordinary bodily presence, as dream image, reflection, spirit, or unseen counterpart.
- Surface relation: indirect; repeated seeing at 96:7-14 and repeated references to the human at 96:2, 96:5, and 96:6 supply the surface poles of appearance and embodiment.
- Surprising reach: The channel distinguishes the dream image inside perception from the spirit or apparition opposed to ordinary human visibility.

#### Subchannel A. Dream Image
- Reading type: latent/lexical
- Scene or process: A sleeping perceiver receives a formed image that appears inwardly rather than as an external body.
- Active motifs: dream vision `ر ء ي:B003/m01`; human image in the dark pupil `ء ن س:B005/m02`; reflected appearance `ر ء ي:B006/m03`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ء ن س` 96:2, 96:5-6
- Synthesis: Dream supplies the mode of perception, the pupil-image supplies an inward visual carrier, and reflected appearance gives the dream a coherent figure despite the absence of an external body.

#### Subchannel B. Spirit and Apparition
- Reading type: latent/lexical
- Scene or process: An unseen being or image becomes perceptible at the boundary between human presence and the nonhuman unseen.
- Active motifs: spirit or apparition `ر ء ي:B008/m01`; human contrasted with the unseen `ء ن س:B001/m02`; apparition-like pupil image `ء ن س:B005/m03`; misleading cultic power `ط غ ي:B003/m01`
- Ayah anchors: `ر ء ي` 96:7, 96:9, 96:11, 96:13-14; `ء ن س` 96:2, 96:5-6; `ط غ ي` 96:6
- Synthesis: The human/unseen contrast establishes the boundary, apparition crosses it as perceived presence, and the cultic-power motif shows how such presence can be elevated into a misleading authority.

## Standalone Subchannels

### S1. Weapon Readied from Its Case
- Reading type: latent/lexical
- Scene or process: A weapon is fitted with a point, kept in a case, and drawn by the hand for immediate use.
- Active motifs: hand returning to the weapon `ر ج ع:B010/m01`; sword scabbard `ق ر ب:B010/m01`; fitted spearhead `ء م ر:B011/m01`; pared weapon tip `ق ل م:B005/m02`
- Ayah anchors: `ر ج ع` 96:8; `ق ر ب` 96:19; `ء م ر` 96:12; `ق ل م` 96:4
- Synthesis: Paring and fitting prepare the point, the scabbard contains the weapon, and the returning hand changes stored readiness into deployment.

### S2. Relational Grammar and Collectivity
- Reading type: latent/lexical
- Scene or process: Particles and connective forms place entities at an endpoint or location, join them together, and construe them as a collective.
- Active motifs: endpoint preposition `ء ل ي:B001/m02`; locative relation `ء ل ي:B002/m01`; particle of approximation or possibility `ر ب ب:B015/m01`; connective joining `ء ل ي:B003/m01`; plural connective `ء ل ي:B004/m01`; lexical gathering `ق ر ء:B001/m03`
- Ayah anchors: `ء ل ي` 96:8 (إِلَى); `ر ب ب` 96:1, 96:3, 96:8; `ق ر ء` 96:1, 96:3
- Synthesis: Endpoint and location establish grammatical relation, the modal particle qualifies assertion, and connective forms gather separate referents into one construed group.


