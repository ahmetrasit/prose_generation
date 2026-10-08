Surah: 62. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S62 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s062/surah.r2/text.md =====
# Surah 62

- 62:1 يُسَبِّحُ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ٱلْمَلِكِ ٱلْقُدُّوسِ ٱلْعَزِيزِ ٱلْحَكِيمِ
- 62:2 هُوَ ٱلَّذِى بَعَثَ فِى ٱلْأُمِّيِّۦنَ رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍۢ
- 62:3 وَءَاخَرِينَ مِنْهُمْ لَمَّا يَلْحَقُوا۟ بِهِمْ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 62:4 ذَٰلِكَ فَضْلُ ٱللَّهِ يُؤْتِيهِ مَن يَشَآءُ ۚ وَٱللَّهُ ذُو ٱلْفَضْلِ ٱلْعَظِيمِ
- 62:5 مَثَلُ ٱلَّذِينَ حُمِّلُوا۟ ٱلتَّوْرَىٰةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ ٱلْحِمَارِ يَحْمِلُ أَسْفَارًۢا ۚ بِئْسَ مَثَلُ ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ بِـَٔايَٰتِ ٱللَّهِ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- 62:6 قُلْ يَٰٓأَيُّهَا ٱلَّذِينَ هَادُوٓا۟ إِن زَعَمْتُمْ أَنَّكُمْ أَوْلِيَآءُ لِلَّهِ مِن دُونِ ٱلنَّاسِ فَتَمَنَّوُا۟ ٱلْمَوْتَ إِن كُنتُمْ صَٰدِقِينَ
- 62:7 وَلَا يَتَمَنَّوْنَهُۥٓ أَبَدًۢا بِمَا قَدَّمَتْ أَيْدِيهِمْ ۚ وَٱللَّهُ عَلِيمٌۢ بِٱلظَّٰلِمِينَ
- 62:8 قُلْ إِنَّ ٱلْمَوْتَ ٱلَّذِى تَفِرُّونَ مِنْهُ فَإِنَّهُۥ مُلَٰقِيكُمْ ۖ ثُمَّ تُرَدُّونَ إِلَىٰ عَٰلِمِ ٱلْغَيْبِ وَٱلشَّهَٰدَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ
- 62:9 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا نُودِىَ لِلصَّلَوٰةِ مِن يَوْمِ ٱلْجُمُعَةِ فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ وَذَرُوا۟ ٱلْبَيْعَ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- 62:10 فَإِذَا قُضِيَتِ ٱلصَّلَوٰةُ فَٱنتَشِرُوا۟ فِى ٱلْأَرْضِ وَٱبْتَغُوا۟ مِن فَضْلِ ٱللَّهِ وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ
- 62:11 وَإِذَا رَأَوْا۟ تِجَٰرَةً أَوْ لَهْوًا ٱنفَضُّوٓا۟ إِلَيْهَا وَتَرَكُوكَ قَآئِمًۭا ۚ قُلْ مَا عِندَ ٱللَّهِ خَيْرٌۭ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّجَٰرَةِ ۚ وَٱللَّهُ خَيْرُ ٱلرَّٰزِقِينَ


===== _commentary/v16/work/s062/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ب ح (root_000666): 62:1 يُسَبِّحُ

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

## ء ل ه (root_000047): 62:1 لِلَّهِ, 62:4 ٱللَّهِ, 62:4 وَٱللَّهُ, 62:5 ٱللَّهِ, 62:5 وَٱللَّهُ, 62:6 لِلَّهِ, 62:7 وَٱللَّهُ, 62:9 ٱللَّهِ, 62:10 ٱللَّهِ, 62:10 ٱللَّهَ, 62:11 ٱللَّهِ, 62:11 وَٱللَّهُ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 62:1 لِلَّهِ, 62:4 ٱللَّهِ, 62:4 وَٱللَّهُ, 62:5 ٱللَّهِ, 62:5 وَٱللَّهُ, 62:6 لِلَّهِ, 62:7 وَٱللَّهُ, 62:9 ٱللَّهِ, 62:10 ٱللَّهِ, 62:10 ٱللَّهَ, 62:11 ٱللَّهِ, 62:11 وَٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## س م و (root_000745): 62:1 ٱلسَّمَٰوَٰتِ

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

## ECHO و س م (root_001650): for 62:1 ٱلسَّمَٰوَٰتِ: withheld observed target; not identity

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

## ء ر ض (root_000025): 62:1 ٱلْأَرْضِ, 62:10 ٱلْأَرْضِ

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

## م ل ك (root_001444): 62:1 ٱلْمَلِكِ

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

## ق د س (root_001206): 62:1 ٱلْقُدُّوسِ

- **B001** arınma, arıtma ve eksiklikten uzak sayma — arılık, arınma ve eksiklikten uzak sayma · arıtma ve eksiklikten uzak sayma · arındı, arı duruma geldi · arındırdı, arı duruma getirdi · kendimizi ya da şeyleri senin için arındırırız · seni her türlü eksiklikten uzak diye niteleriz
  يدل على الطهر (maqayis)؛ القدس تنزيه الله وهو القدوس والمقدس والمتقدس (ayn)؛ القدس والقدس الطهر والتقديس التطهير وتقدس أي تطهر (sihah)؛ نقدس لك أي نطهر أنفسنا لك ونقدسه أي نطهره والقدوس الطاهر والقدوس المبارك وأرض مقدسة أي مباركة (tahdhib)؛ التقديس التطهير الإلهي ونقدس لك أي نطهر الأشياء ارتساما لك وقيل نقدسك أي نصفك بالتقديس (mufradat)
- **B002** arınmış veya bereketli sayılan yer [kalıp] — arınmış veya bereketli toprak · arınmışların bulunduğu ölüm sonrası mutluluk yurdu · arınmanın kazanıldığı dinî yol ve kurallar bütünü · günah ve ortak koşma kirinden arındırdığı düşünülen tapınak
  الأرض المقدسة هي المطهرة وحظيرة القدس أي الطهر (maqayis)؛ الأرض المقدسة المطهرة وبيت المقدس والمقدس (sihah)؛ بيت المقدس البيت المطهر وأرض مقدسة أي مباركة (tahdhib)؛ البيت المقدس هو المطهر من النجاسة وكذلك الأرض المقدسة وحظيرة القدس قيل الجنة وقيل الشريعة (mufradat)
- **B003** Tanrı'dan kutsallıkla inen belirli vahiy meleği [kalıp] — Tanrı'dan kutsallıkla inen belirli vahiy meleği
  جبرئيل عليه السلام روح القدس (maqayis)؛ روح القدس جبريل عليه السلام (sihah)؛ روح القدس يعني به جبريل من حيث إنه ينزل بالقدس من الله (mufradat)
- **B004** Tanrı'nın mutlak arılığını ve eksiksizliğini bildiren adı — Tanrı'nın mutlak arılığını ve eksiksizliğini bildiren adı · Tanrı'yı arı ve eksiklikten uzak diye niteleyen, kullanımı tartışmalı söz · Tanrı'yı arı ve eksiklikten uzak diye niteleyen, kaynakta kabulü tartışmalı söz
  في صفة الله تعالى القدوس وهو منزه عن الأضداد والأنداد والصاحبة والولد (maqayis)؛ القدس تنزيه الله وهو القدوس والمقدس والمتقدس (ayn)؛ القدوس اسم من أسماء الله تعالى وهو فعول من القدس وهو الطهارة (sihah)؛ القدوس الطاهر وهو من أسماء الله ولم يجىء في صفة الله غير القدوس ولا أعرف المتقدس في صفاته (tahdhib)
- **B005** yıkanıp arınmak için kullanılan kova — yıkanıp arınmak için kullanılan kova
  القدس بالتحريك السطل بلغة أهل الحجاز لأنه يتطهر فيه (sihah)؛ قيل للسطل القدس لأنه يتقدس منه أي يتطهر (tahdhib)
- **B006** gümüşten yapılmış boncuk benzeri süs — gümüşten yapılmış boncuk veya boncuk benzeri süs
  القداس شيء كالجمان يعمل من فضة (maqayis)؛ القداس الجمان من فضة (ayn)؛ القداس بالضم شئ يعمل كالجمان من فضة (sihah)؛ القداس الجمان من فضة (tahdhib)
- **B007** kutsallık dilenen hac konaklama yerinin özel adı — kutsallık dilenen ve hac yolcularına konak sayılan yerin özel adı
  القادسية سميت بذلك وإن إبراهيم دعا لها بالقدس وأن تكون محلة الحاج (maqayis)؛ القادسية دعا لها إبراهيم عليه السلام بالقدس وأن تكون محلة الحاج (sihah)
- **B008** belirli büyük bir dağın özel adı — belirli büyük bir dağın özel adı
  قدس جبل (maqayis)؛ قدس بالتسكين جبل عظيم بأرض نجد (sihah)
- **B009** büyük gemi — büyük gemiler · büyük gemi
  القوادس السفن الكبار والقادس السفينة العظيمة (tahdhib)
- **B010** develerin suya doyduğunu gösteren havuz taşı — suyun örttüğünde develerin doyduğu anlaşılan havuz taşı
  القداس الحجر ينصب على مصب الماء في الحوض وحجر يكون في وسط الحوض إذا غمره الماء رويت الإبل (tahdhib)
- **B011** arınmış tapınağın bulunduğu yere mensup kimse — arınmış tapınağın bulunduğu yere mensup; tanıkta Yahudi
  بيت المقدس والمقدس والنسبة إليه مقدسي مثال مجلسي ومقدسي ويعنى يهوديا (sihah)
- **B012** bereket umulan Hristiyan rahip — bereket umularak giysisine dokunulan Hristiyan rahip
  أراد بالمقدس الراهب وصبيان النصارى يتبركون به ويمسحون ثيابه (tahdhib)

## ع ز ز (root_001008): 62:1 ٱلْعَزِيزِ, 62:3 ٱلْعَزِيزُ

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

## ح ك م (root_000348): 62:1 ٱلْحَكِيمِ, 62:2 وَٱلْحِكْمَةَ, 62:3 ٱلْحَكِيمُ

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

## ب ع ث (root_000129): 62:2 بَعَثَ

- **B001** durgun olanı harekete geçirme — harekete geçirmek; uyandırmak · devenin bağını çözüp onu ayağa kaldırmak · uyuyanı uyandırmak · kargaşanın kabarmaları ve alevlenmeleri · neredeyse hiç uyumayan adam · neredeyse hiç çökmeyen dişi deve
  الباء والعين والثاء أصل واحد وهو الإثارة (maqayis)؛ بعثت الناقة إذا أثرتها (maqayis;sihah)؛ بعثت البعير أرسلته وحللت عقاله أو كان باركا فهجته (ayn)؛ بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته (tahdhib)؛ بعثته من نومه فانبعث وبعثت النائم إذا أهببته (sihah;tahdhib)؛ أصل البعث إثارة الشيء وتوجيهه (mufradat)
- **B002** gönderme veya yöneltme — göndermek; yöneltmek · görevle göndermek; yola çıkarmak · birini bir iş için göndermek · birini bir işi yapmaya isteklendirip yöneltmek · asker birliğini düşmana karşı göndermek · göreve gönderilmiş topluluk veya birlik · gönderilmiş ordular
  البعث الإرسال كبعث الله من في القبور (ayn)؛ بعثت الرجل في الحاجة وبعثته على الشيء إذا أرغته أن يفعله (jamhara)؛ ابتعثه بمعنى أي أرسله (sihah)؛ البعث بعث الجند إلى العدو والقوم المبعوثون المشخصون (tahdhib)؛ بعث الإنسان في حاجة وفبعث الله غرابا أي قيضه ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا (mufradat)
- **B004** yola koyulup ilerleme — harekete geçip ilerlemek; hızlanmak · yola koyulma ve ilerleme · şiir benden akıp geldi
  انبعث القوم في الخير والشر انبعاثا إذا تتابعوا (jamhara)؛ انبعث في السير أي أسرع (sihah)؛ كره الله انبعاثهم أي توجههم ومضيهم (mufradat)

## ء م م (root_000053): 62:2 ٱلْأُمِّيِّۦنَ

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

## ر س ل (root_000563): 62:2 رَسُولًا

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

## ت ل و (root_000186): 62:2 يَتْلُوا۟

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

## ECHO ت ل ل (root_000185): for 62:2 يَتْلُوا۟: withheld observed target; not identity

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

## ء ي ي (root_000074): 62:2 ءَايَٰتِهِۦ, 62:5 بِـَٔايَٰتِ

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

## ز ك و (root_000637): 62:2 وَيُزَكِّيهِمْ

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

## ع ل م (root_001040): 62:2 وَيُعَلِّمُهُمُ, 62:7 عَلِيمٌۢ, 62:8 عَٰلِمِ, 62:9 تَعْلَمُونَ

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

## ك ت ب (root_001283): 62:2 ٱلْكِتَٰبَ

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

## ك و ن (root_001332): 62:2 كَانُوا۟, 62:6 كُنتُمْ, 62:8 كُنتُمْ, 62:9 كُنتُمْ

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

## ق ب ل (root_001198): 62:2 قَبْلُ

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

## ض ل ل (root_000913): 62:2 ضَلَٰلٍ

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

## ب ي ن (root_000170): 62:2 مُّبِينٍ

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

## ء خ ر (root_000019): 62:3 وَءَاخَرِينَ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ل ح ق (root_001347): 62:3 يَلْحَقُوا۟

- **B001** yetişip erişme — yetişmek, erişmek · ona yetiştirmek veya ulaştırmak · yetişmek, erişmek · yetişen, erişen · binekler birbirine yetişti · öteki develerin geride bırakamadığı hızlı dişi deve · önceden yola çıkan topluluğa sonradan yetişenler
  أصل يدل على إدراك شيء وبلوغه إلى غيره (maqayis)؛ لحق فلان فلانا فهو لاحق (maqayis)؛ اللحق كل شيء لحق شيئا أو ألحقته به (ayn)؛ لحقت الشيء ألحقه لحقا ولحاقا (jamhara)؛ لحقه ولحق به لحاقا أي أدركه (sihah)؛ تلاحقت المطايا أي لحق بعضها بعضا (sihah)
- **B002** soy bağı yakıştırma — soyu başka bir baba veya topluluğa bağlanmış kişi · kendi çocuğu olduğunu ileri sürmek
  الملحق الدعي الملصق (maqayis;sihah)؛ واللحق الدعي الموصل بغير أبيه (ayn)؛ رجل ملحق بقوم إذا كان ملصقا بهم (jamhara)؛ واستلحقه أي ادعاه (sihah)
- **B003** ilkinden sonra gelen bitki veya ürün — ilkinden sonra gelen bitki veya ürün
  اللحق كل شيء لحق شيئا أو ألحقته به من النبات ومن حمل النخل (ayn)؛ يخرج في بعضه شيء أخضر قل ما يرطب حتى يدركه الشتاء ويكون نحو ذلك في الكرم يسمى لحقا (ayn)؛ اللحق بالتحريك شيء يلحق بالأول (sihah)؛ اللحق أيضا من التمر الذي يأتي بعد الأول (sihah)
- **B004** cılızlaşıp incelme — cılızlaşıp incelmek
  لحق لحوقا أي ضمر (sihah)

## ف ض ل (root_001163): 62:4 فَضْلُ, 62:4 ٱلْفَضْلِ, 62:10 فَضْلِ

- **B001** gereksinimi aşan veya bir işlemden sonra kalan fazlalık — gereksinimden fazla olan ve geride kalan bölüm · herhangi bir şeyden artakalan kısım · artık, geriye kalan bölüm · bir miktarı geride kaldı · yiyeceğin bir kısmını bıraktı · ondan bir miktar geride bıraktım · ganimet bölüşümünden artanlar · sudan geriye kalanlar · malın gelirleri ve getirileri · içki ve benzerlerinden kalan artıklar
  الفضل الزيادة والخير (maqayis); الفضالة ما فضل من كل شيء والفضلة البقية من كل شيء (ayn;tahdhib); الفضل الزيادة عن الاقتصاد (mufradat); الفضل والفضيلة خلاف النقص والنقيصة (sihah); أفضل من الأرض والطعام إذا ترك منه شيئا (ayn); فضول الغنائم ما فضل من القسم وفضلات الماء بقاياه (tahdhib)
- **B002** nitelikçe üstün olma, yüksek değer taşıma ve karşılaştırmada öne geçme — üstünlük, yüksek değer ve derece · yüksek nitelik ve değer derecesi · topluluktaki kişiler arasındaki üstünlük farkı · birini başkasından üstün sayma · birini üstünlükte geçti · adamı üstünlükte geçtim · onunla üstünlük yarışına girip onu geçtim · yüksek nitelikli, değerli · başkası tarafından üstünlükte geçilmiş · üstünlük karşılaştırması
  الفضيلة الدرجة والرفعة في الفضل (ayn); الفضيلة الدرجة الرفيعة في الفضل (tahdhib); الفضل والفضيلة خلاف النقص والنقيصة (sihah); الفضل إذا استعمل لزيادة أحد الشيئين على الآخر فعلى ثلاثة أضرب (mufradat); التفاضل بين القوم أن يكون بعضهم أفضل من بعض (tahdhib); فاضلته ففضلته إذا غلبته بالفضل (sihah)
- **B003** başkasına gönüllü iyilik etme ve yükümlülük dışı bağış verme — başkasına iyilik etme · birine kendi imkânından verip iyilik etti · başkasına iyilik ve bağışta bulunma · verilmesi zorunlu olmayan bağış · çok iyilik yapan ve eli açık kişi
  الإفضال الإحسان (maqayis;sihah); أفضل فلان على فلان أناله من فضله وأحسن إليه (ayn;tahdhib); التفضل التطول على غيرك (ayn;tahdhib); كل عطية لا تلزم من يعطي يقال لها فضل (mufradat); رجل مفضال كثير الخير والمعروف (tahdhib)
- **B004** akranlarına karşı üstünlük iddia etme ve daha yüksek konum isteme — akranlarına karşı üstünlük iddiasında bulunan kişi · başkalarından daha yüksek konum isteme · size karşı daha yüksek konum istemek
  المتفضل فالمدعي للفضل على أضرابه وأقرانه (maqayis); المتفضل أيضا الذي يدعي الفضل على أقرانه (sihah); يريد أن يكون له الفضل عليكم في القدر والمنزلة وليس من التفضل الذي هو بمعنى الإفضال والتطول (ayn;tahdhib)
- **B005** giysiyi omuzlara dolayarak kuşanma veya evde tek giysiyle bulunma — giysiyi omuzlara dolayarak kuşanma · üstüne tek giysi almış erkek · evde tek giysiyle bulunan kadın · uçları omuzda çaprazlanarak kuşanılan giysi · erkeğin evde giydiği tek giysi · kadının tek başına giydiği giysi · tek giysiyi kuşanışının güzel olması
  التفضل التوشح (maqayis;ayn;tahdhib); رجل فضل ومتفضل وامرأة فضل ومتفضلة (ayn;tahdhib); الفضل الذي عليه قميص ورداء وليس عليه إزار ولا سراويل (maqayis); تفضلت المرأة في بيتها إذا كانت في ثوب واحد (sihah); الفضال الثوب الواحد يتفضل به الرجل (ayn;tahdhib)

## ء ت ي (root_000009): 62:4 يُؤْتِيهِ

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

## ش ي ء (root_000831): 62:4 يَشَآءُ

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

## ش ي ء (root_000832): 62:4 يَشَآءُ

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

## ع ظ م (root_001029): 62:4 ٱلْعَظِيمِ

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

## م ث ل (root_001397): 62:5 مَثَلُ, 62:5 كَمَثَلِ, 62:5 مَثَلُ

- **B001** benzerlik ve denklik — benzeri, dengi · benzer, eşdeğer · bunu başka bir şeye benzettim
  يدل على مناظرة الشيء للشيء (maqayis); المثل النظير (jamhara); كلمة تسوية (sihah); مثل وشبه بمعنى واحد (tahdhib); أعم الألفاظ الموضوعة للمشابهة (mufradat)
- **B002** ibret verici ağır cezalandırma — onu ibret verici biçimde cezalandırdı · öldürülen kişinin bedenini kesip bozdu · ibret verici ağır ceza · caydırıcı ağır cezalar · yönetici onu kısas gereği öldürdü · ondan hakkının karşılığını aldı · suça denk karşılık
  مثل به إذا نكل (maqayis); مثلت بالرجل إذا نكلت به (jamhara); مثل به يمثل مثلا أي نكل به (sihah); المثلة الاسم (tahdhib); نقمة تنزل بالإنسان فيجعل مثالا يرتدع به غيره (mufradat)
- **B003** benzer duruma aktarılan örnek söz — benzer bir duruma aktarılan örnek söz · dilden dile dolaşan özlü söz · örnek bir söz söyledi · bu dizeyi örnek gösterdi
  المثل المضروب (maqayis); المثل السائر (jamhara); ما يضرب به من الأمثال (sihah); يقال تمثل فلان إذا ضرب مثلا (tahdhib); عبارة عن قول في شيء يشبه قولا في شيء آخر (mufradat)
- **B004** nitelik veya hakkında verilen bilgi — niteliği veya hakkında verilen bilgi
  مثل الشيء صفته (sihah); مثلها هو الخبر عنها (tahdhib); مثلها صفتها (tahdhib); يعبر بهما عن وصف الشيء (mufradat)
- **B005** ayağa kalkıp dik durma — adam ayağa kalkıp dikildi · ayakta dik duran
  مثل الرجل قائما انتصب (maqayis); مثل الرجل مثولا إذا انتصب قائما (jamhara); مثل بين يديه مثولا أي انتصب قائما (sihah); الماثل القائم (tahdhib); أصل المثول الانتصاب (mufradat)
- **B006** yerinden ayrılma; yere sinip silinme — bulunduğu yerden ayrılıp gitti · yere sinmiş veya izi silinmiş
  مثل يمثل إذا زال عن موضعه (jamhara); مثل أي لطأ بالأرض وهو من الأضداد (sihah); الماثل اللاطىء بالأرض (tahdhib); ثم مثل أي ذهب (tahdhib); الماثل الدارس (tahdhib)
- **B007** döşek veya yere serilen yaygı — döşek veya yere serilen yaygı
  المثال الفراش والجمع مثل (maqayis); المثال الفراش (jamhara); المثال الفراش والجمع مثل (sihah); ما مثالان قال نمطان (tahdhib); النمط ما يفترش (tahdhib)
- **B008** başkasına benzetilerek yapılmış görüntü — başkasına benzetilerek yapılmış görüntü veya nesne · benzetilerek yapılmış görüntüler veya nesneler · onun görüntüsünü oluşturdu · bir biçim olarak canlandı veya göründü · örnek alınan biçim veya karşılık
  التمثال الصورة (jamhara); التمثال الصورة (sihah); مثلت له كذا تمثيلا إذا صورت له مثاله (sihah); التمثال اسم للشيء المصنوع مشبها (tahdhib); الممثل المصور على مثال غيره (mufradat)
- **B009** iyilik ve erdem bakımından üstün — daha iyi veya erdeme daha yakın · topluluğun en iyileri · en iyi olan veya en iyi yol · adam daha iyi ve seçkin bir duruma geldi
  أمثل بني فلان أدناهم للخير (maqayis); أماثل القوم خيارهم (jamhara); صار فاضلا (sihah); أمثل من فلان أي أفضل (tahdhib); الأشبه بالفضيلة (mufradat)
- **B010** buyruk veya örneğe uygun davranma [kalıp] — buyruğunu yerine getirdi · onun izinden ve yolundan gitti
  امتثل أمره أي احتذاه (sihah); امتثلت مثال فلان أي احتذيت حذوه وسلكت طريقته (tahdhib); وضع شيء ما ليحتذى به فيما يفعل (mufradat)
- **B011** ders çıkarılan olay veya gösterge — ders çıkarılan olay veya gerçeği gösteren belirti
  يكون المثل بمعنى العبرة (tahdhib); يكون المثل بمعنى الآية (tahdhib)
- **B012** hastalıktan sonra toparlanıp iyileşme [kalıp] — hastalığından sonra toparlanmaya başladı · hasta bugün daha iyi durumda
  تماثل من علته أي أقبل (sihah); تماثل المريض من المثول والانتصاب (tahdhib); المريض اليوم أمثل أي أفضل حالا (tahdhib)

## ح م ل (root_000357): 62:5 حُمِّلُوا۟, 62:5 يَحْمِلُوهَا, 62:5 يَحْمِلُ

- **B001** bir yükü kaldırıp götürme veya üstlenme — bir şeyi kaldırıp taşımak · sırtta, başta veya başka bir yerde dıştan taşınan yük · selin sürükleyip getirdiği çer çöp ve köpük
  حملت الشيء أحمله حملا (maqayis)؛ حملت الشئ على ظهرى أحمله حملا (sihah)؛ حمل الشيء يحمله حملا وحملانا (ayn;tahdhib)؛ حملت الثقل والرسالة والوزر حملا (mufradat)؛ حميل السيل ما يحمله من غثائه (maqayis)؛ حميل السيل ما يحمل من الغثاء (ayn;sihah)؛ حميل السيل ما حمله السيل (tahdhib)؛ حملناكم في الجارية (mufradat)
- **B002** gebelik veya ağacın meyve yükü — rahimdeki yavru veya ağacın üzerindeki meyve · gebe kadın · gebe olmadan sütü gelmek
  الحمل ما كان في بطن أو على رأس شجر (maqayis;sihah)؛ الحمل ما في البطن (ayn)؛ حمل الشجر (ayn)؛ حملت المرأة والشجرة حملا (sihah)؛ حملت المرأة حبلت وكذا حملت الشجرة (mufradat)؛ حملت حملا خفيفا (mufradat)
- **B003** görev veya suç yükünü üstlenme [kalıp] — suçun ve kötülüğün yükünü üzerine almak · güvenilerek verilen işi üstlenmek veya onu yerine getirmemek · iletiyi ulaştırma görevini üstlenmek
  حملت الثقل والرسالة والوزر حملا (mufradat)؛ كلفوا أن يتحملوها أي يقوموا بحقها فلم يحملوها (mufradat)؛ حمل الأمانة أي خيانتها وترك أدائها (tahdhib)؛ من باء بالإثم يسمى حاملا للإثم (tahdhib)؛ وساء لهم يوم القيامة حملا أي وزرا (sihah)
- **B004** başkasının borcunu üstlenip güvence verme — uzlaşma için üstlenilen kan bedeli veya ödeme yükü · başkası adına güvence vermek · borcun ödenmesini güvence altına alan kişi
  الحمالة أن يحمل الرجل دية ثم يسعى عليها والضمان حمالة (maqayis)؛ الحمالة الدية يحملها قوم عن قوم (ayn)؛ الحمالة ما يحمله القوم من الديات (jamhara)؛ حملت به حمالة أي كفلت (sihah)؛ الحميل الكفيل (jamhara;tahdhib;mufradat)؛ الحميل لكونه حاملا للحق مع من عليه الحق (mufradat)
- **B005** soy bağı doğrulanamayan getirilmiş çocuk — terk edilmiş, başka yerden getirilmiş veya soyu doğrulanamayan çocuk · soyu doğrulanamayan kişinin mirası
  الحميل المنبوذ يحمل فيربى (ayn;tahdhib)؛ الحميل الولد في بطن الأم إذا أخذت من أرض الشرك (ayn;tahdhib)؛ الحميل الذي يحمل من بلده صغيرا ولم يولد في الإسلام (sihah)؛ الحميل الدعي (maqayis;sihah)؛ ميراث الحميل لمن لا يتحقق نسبه (mufradat)
- **B006** taşıma kayışı, binek düzeneği veya yük hayvanı — kılıç askısı · deve üzerinde yolcu taşıyan iki yanlı düzenek · yük taşımaya ayrılmış deve veya başka hayvan · yükleri veya yolcu düzenekleriyle birlikte develer · armağan olarak verilen binek hayvanı
  الحمالة والمحمل علاقة السيف (maqayis;ayn;sihah)؛ حمالة السيف وحميلته والجمع الحمائل (jamhara)؛ المحمل الشقان على البعير يحمل فيهما نفسان (ayn)؛ المحمل واحد محامل الحاج (sihah)؛ الحمولة الإبل تحمل عليها الأثقال (maqayis;ayn)؛ الحمولة ما احتمل عليه الحي من بعير أو حمار أو غيره (sihah;tahdhib)
- **B007** zorlanarak yüklenme, eğilme veya dayanak olma — güç bir işe zorlanarak girişmek · yolculukta kendini sonuna kadar zorlamak · birinin üzerine doğru eğilmek veya yüklenmek · güvenilip dayanılan kişi veya şey
  تحاملت إذا تكلفت الشيء على مشقة (maqayis)؛ تحاملت في الشيء إذا تكلفته على مشقة (ayn)؛ حمل على نفسه في السير أي جهدها فيه (sihah)؛ تحامل عليه أي مال (sihah)؛ ما على فلان محمل أي معتمد (sihah;tahdhib)؛ المحمل بفتح الميم المعتمد (tahdhib)
- **B008** öfkeye kapılma veya incinmeye ağırbaşlılıkla katlanma — öfkelenmek veya öfkenin etkisine kapılmak · incitici davranışa öfkesini tutarak katlanmak
  الاحتمال الغضب (maqayis)؛ احتمل إذا غضب (maqayis;tahdhib)؛ احتمله الغضب وأقله الغضب (maqayis)؛ حملت عنه أي حلمت عنه (ayn)؛ احتمل الرجل إذا غضب ويكون بمعنى حلم (tahdhib)
- **B009** kuzu — kuzu
  الحمل الخروف والجميع الحملان (ayn;tahdhib)؛ الحمل من الضأن معروف وهو الجذع فما دونه (jamhara)؛ خص الضأن الصغير بذلك لكونه محمولا (mufradat)
- **B010** Koç burcu ve onunla ilişkilendirilen yağışlı gök olayı — Koç, burçlar kuşağının ilk burcu · bol su taşıyan kara bulut veya şimşek · bol su taşıyan bulut · Koç burcuna bağlanan yağış dönemi
  الحمل برج من البروج (ayn;tahdhib)؛ الحمل أول البروج (sihah)؛ البرق يقال له حمل (maqayis)؛ الحمل السحاب الكثير الماء (jamhara)؛ الحمل السحاب الأسود (tahdhib)؛ الحمل النوء وهو الطلي (tahdhib)؛ الحميل السحاب الكثير الماء لكونه حاملا للماء (mufradat)

## ح م ر (root_000356): 62:5 ٱلْحِمَارِ

- **B001** kırmızılık ve kızarma — kırmızılık; kırmızı rengin bulunması veya görünmesi · kırmızı renkli, kızıl · kızarmak, kırmızı rengi kalıcı biçimde almak · sonradan ve geçici olarak kızarmak
  الحمرة لون الأحمر (ayn;sihah;tahdhib)؛ أصل يعرف بالحمرة (maqayis)؛ رجل أحمر والجمع الأحامر (maqayis;jamhara;sihah)؛ احمر الشيء احمرارا واحمار (ayn;sihah;tahdhib)
- **B002** renk adıyla insan ve topluluk belirtme — yabancı halklar; özellikle Doğu Roma ve İran toplulukları · yerli ve yabancı bütün insanlar · bayraklarını kırmızıya boyamasıyla tanınan grup · yanında silah bulunmayan adam
  الحمراء العجم (maqayis;sihah)؛ هذه الحمراء يعني العجم والموالي (ayn)؛ كل أسود وأحمر (sihah;tahdhib)؛ الأسود والأحمر العرب والعجم (tahdhib)؛ المحمرة خلاف المبيضة (sihah;tahdhib)
- **B003** kalıplaşmış şiddet ve zorluk anlatımı [kalıp] — şiddetli ölüm veya kanlı öldürme · savaş çok şiddetlendi · çok çetin veya kıtlıkla geçen yıl · yaz sıcağının en şiddetli zamanı · güzelliğin peşinden gitmek sıkıntı ve eziyet getirir · yeni ve henüz silinmemiş ayak izi · yeri soyacak kadar şiddetli yağmur · birine karşı öfkeden yanıp tutuşmak
  موت أحمر (maqayis;ayn;sihah;tahdhib)؛ إذا احمر البأس (maqayis;sihah;tahdhib)؛ سنة حمراء شديدة (maqayis;ayn;sihah;tahdhib)؛ حمارة القيظ شدة حره (ayn;jamhara;sihah;tahdhib)؛ غيث حمر شديد (maqayis;jamhara;sihah)
- **B004** evcil ya da yaban eşeği — evcil veya yaban eşeği · dişi eşek · yaban eşeği · eşek gibi yavaş koşan melez at · eşek sahibi kişi · yolculukta eşek kullananlar
  الحمار معروف (maqayis)؛ الحمار العير الأهلي والوحشي (ayn;tahdhib)؛ الحمار العير والجمع حمير وحمر وحمرات وأحمرة (sihah)؛ الحمار الحيوان المعروف وجمعه حمير وأحمرة وحمر (mufradat)؛ فرس محمر (ayn;jamhara;sihah;tahdhib)؛ رجل حامر وحمار ذو حمار (tahdhib)
- **B005** tahta veya taş dayanak — eyer, yük takımı veya tezgâhta kullanılan tahta dayanak · üzerine araç veya yük konan iki taş ayak · havuz, siper, ev veya mezar çevresine dikilen taşlar
  الحمار شيء يجعل حول الحوض (maqayis)؛ الحمار خشبة في مقدم الرحل والإكاف (ayn;tahdhib)؛ حمار الصيقل خشبته (ayn;tahdhib)؛ حمار السرج والرحل الذي يوضع عليه (jamhara)؛ الحماران حجران يجفف عليهما الأقط (maqayis;jamhara;sihah)؛ الحمائر حجارة تنصب حول الحوض أو القترة (maqayis;sihah;tahdhib)
- **B006** kızartıcı şişlik hastalığı — insanda tuttuğu yeri kızartan hastalık veya şişlik
  الحمرة داء يعتري الناس فتحمر مواضعها (ayn)؛ الحمرة تعتري الناس فيحمر موضعها (tahdhib)؛ الحمرة ورم من جنس الطواعين (tahdhib)
- **B007** arpa fazlalığına bağlı hayvan hazımsızlığı — fazla arpanın hayvanda yol açtığı hazımsızlık ve kötü ağız kokusu · binek hayvanı fazla arpadan rahatsızlandı
  الحمر داء يعتري الدابة من كثرة الشعير (ayn;tahdhib)؛ حمر الفرس إذا سنق أي بشم فأنتن فوه (jamhara)؛ الحمر سنق يصيب الدابة من الشعير فينتن فوه (sihah)
- **B008** dış yüzeyi soymak veya kazımak — yeri soyacak kadar şiddetli yağmur · bir şeyi soymak, kazımak veya tıraşlamak · kayışın içini kazıyıp yağlayarak dikmek · koyunun yüzeyini sıcak işlemle gidermek veya derisini çıkarmak · dış yüzeyi soyulmuş beyaz kayış
  كل شيء قشرته فقد حمرته فهو محمور (ayn;tahdhib)؛ حمر الخارز سيره (sihah;tahdhib)؛ حمرت الجلد إذا قشرته وحلقته (tahdhib)؛ حمر الشاة إذا سمطها (sihah;tahdhib)؛ الحمير والحميرة الأشكز سير أبيض مقشور ظاهره (sihah)
- **B009** çok ayaklı küçük canlı, serçemsi kuş ve bitki adları — belirli bir kuş türü · yere yakın yaşayan, çok ayaklı küçük canlı · serçeye benzeyen bir kuş türü · belirli bir bitki türü · eşek kulağına benzeyen geniş yapraklı bitki
  حمار قبان دويبة (maqayis;ayn;jamhara;sihah;tahdhib)؛ الحمرة ضرب من الطير كالعصافير (ayn;sihah)؛ الحمر طائر والواحدة حمرة (jamhara;tahdhib)؛ الحمرة بسكون الميم نبت (tahdhib)؛ أذن الحمار نبت عريض الورق (tahdhib)
- **B010** renk adıyla kurulan geleneksel ikili ve üçlüler — bağlama göre safran ile altın veya et ile şarap · şarap, et ve safrandan oluşan geleneksel üçlü · şarap ile kumaşlar
  الأحمران الزعفران والذهب (ayn;jamhara)؛ أهلك الرجال الأحمران اللحم والخمر (sihah)؛ الأحمران الخمر واللحم (tahdhib)؛ الأحامرة الثلاثة الراح واللحم والزعفران (sihah;tahdhib)؛ الأحمرين الراح والمحبرا (tahdhib)
- **B011** kişi, topluluk, yer ve lakap adları — Güney Arabistan kökenli büyük bir Arap kabilesi · bu kabilenin dilini konuşmak veya öğrenmek · çeşitli kişi adları · bir Arap boyu veya topluluğu · iki ayrı yer adı · belirli bir yer adı · dişi deveyi öldüren kişi için kullanılan lakap · Araplar arasında tanınmış bir hatip için kullanılan ad · inkârcılığıyla anılan eski bir topluluk mensubuna ilişkin deyiş veya anlatı
  بنو حمرى (jamhara)؛ حمير حي عظيم من العرب (jamhara)؛ حمران وأحمر وحميرا (jamhara)؛ أحامر وحامر موضع (jamhara;sihah)؛ حمراء الأسد موضع (jamhara)؛ أحمر ثمود (sihah)؛ ابن لسان الحمرة (jamhara;sihah)؛ حمير أبو قبيلة من اليمن (sihah;tahdhib)

## س ف ر (root_000712): 62:5 أَسْفَارًۢا

- **B001** örtüyü kaldırıp açığa çıkarma — örtüyü kaldırıp nesneyi açığa çıkarma · sarığı baştan açma · kadının yüzündeki örtüyü açması · bir şeyi ötekinin üzerinden sıyırıp örtüsünü kaldırma · evi süpürüp döküntüyü giderme · süpürge · dökülen yaprak, toprak veya süprüntü · süprüntü ve süpürülen döküntü
  الانكشاف والجلاء (maqayis)؛ سفرت الشيء عن الشيء أي كشطته (ayn)؛ سفرت المرأة كشفت عن وجهها (sihah;tahdhib)؛ سفرت البيت كنسته (maqayis;ayn;sihah;tahdhib;mufradat)؛ السفير ما تساقط من الشجر (maqayis;ayn;sihah;tahdhib)؛ السفر كشف الغطاء (mufradat)
- **B002** aydınlanıp belirginleşme — günün ağarması ve aydınlığı · sabahın ağarıp aydınlanması · aydınlık ve ışıldayan yüz · sabah namazını tan yeri iyice belirince kılmak
  أسفر الصبح انكشاف الظلام (maqayis)؛ السفر بياض النهار (ayn;sihah)؛ وجه مسفر منير مشرق (maqayis;ayn;sihah;tahdhib)؛ الإسفار يختص باللون (mufradat)؛ سفر الصبح وسفر المساء (tahdhib)
- **B003** yolculuğa çıkıp mesafe katetme — yolculuk etme ve mesafe katetme · yolcular veya yolcu topluluğu · yolcu, yolculuğa çıkan kişi · bir kente yolculuk etmek · yolcular topluluğu · develerin dağılıp araziye gitmesi · yol yiyeceği veya yemeğin üzerine konduğu yaygı · yolculuğa dayanıklı deve
  السفر سمي بذلك لأن الناس ينكشفون عن أماكنهم (maqayis)؛ السفر قوم مسافرون (maqayis;ayn)؛ السفر قطع المسافة (sihah)؛ سفرت خرجت إلى السفر (sihah)؛ كثرت السافرة يعني المسافرين (sihah;tahdhib)؛ سفرة طعام يتخذ للمسافر (maqayis;ayn;sihah;mufradat)؛ بعير مسفر قوي على السفر (maqayis;sihah;tahdhib)
- **B004** yazılı kitap ve yazıcılık alanı — kitap, cilt veya büyük kitap bölümü · kitaplar veya büyük kitap bölümleri · yazıcılar; göksel yazıcılar da buna dahildir · yazıcı, yazan kişi · kitabı yazmak
  السفر الكتابة والسفرة الكتبة (maqayis)؛ الأسفار أجزاء التوراة (ayn)؛ السفر بالكسر الكتاب والجمع أسفار (sihah)؛ السفرة الكتبة يعني الملائكة (tahdhib)؛ السفر الكتاب الذي يسفر عن الحقائق (mufradat)
- **B005** elçi ve uzlaştırıcı aracılık — elçi veya topluluklar arası uzlaştırıcı · toplulukların arasını düzeltmek · elçilik görevi veya uzlaştırma işi · haberci, yardımcı, hizmetli, simsar veya iş yöneticisi
  سفر بين القوم سفارة إذا أصلح (maqayis;tahdhib)؛ السفير رسول بعض القوم إلى قوم (ayn)؛ السفير الرسول المصلح بين القوم (sihah)؛ السفير الرسول بين القوم يكشف ويزيل ما بينهم من الوحشة (mufradat)؛ السفسير الفيج والتابع والخادم (ayn;tahdhib)؛ السمسار والقيم بالأمر المصلح له (tahdhib)
- **B006** devenin burnuna takılan dizgin bağı — devenin burnuna veya başlığına takılan demir, ip ya da bağ · deveye burun bağı takmak · deve burun bağları
  السِّفار حديدة تجعل في أنف الناقة (maqayis;sihah;tahdhib;mufradat)؛ خيط يشد طرفه على خطام البعير (maqayis;ayn;sihah;tahdhib)؛ جمعه الأسفرة (ayn;tahdhib)
- **B007** yalıtık adlandırmalar — bir şeyin geri çekilip açılması · saçın başın önünden çekilmesi · eti az at · deride veya başka bir yüzeyde kalan iz
  الإسفار أيضا الانحسار (sihah)؛ السفر مقدم رأسه من الشعر (tahdhib)؛ فرس سافر اللحم أي قليله (tahdhib)؛ السفر الأثر يبقى على جلد الإنسان وغيره (tahdhib)؛ الملفوه سفيرا (ayn)
- **B008** yaban öküzü için bir ad — yaban öküzüne verilen bir ad
  يقال للثور الوحشي مسافر ونابىء وناشط

## ب ء س (root_000079): 62:5 بِئْسَ

- **B001** zorlayıcı sert güç — savaşta sert güç, ağır karşılık ve yıldırıcı zarar · savaşta cesur ve güçlü adam · sert gücü olan cesur kişi · ağır ve sert karşılık · çok ağır karşılık · savaş ve yıldırıcı sertlik
  البأس الشدة في الحرب (maqayis;sihah); رجل ذو بأس وبئيس أي شجاع (maqayis;ayn;sihah;tahdhib); البأس العذاب وعذاب بئيس أي شديد (sihah;tahdhib); البأس والبأساء في النكاية (mufradat)
- **B002** ağır geçim sıkıntısı — geçimde sert darlık, yoksulluk ve kötü hal · başına yoksunluk ya da kötü hal gelmiş acınacak kişi · adam yoksullaştı ve ihtiyacı ağırlaştı · güçlük, zarar ve açlık hali · yoksulluk · kötü günler ya da büyük yıkıcı durum · başına yoksulluk gelsin anlamında beddua · iyi halin karşıtı olan darlık · yoksullukla boyun eğme ya da kendini düşkün gösterme
  البؤس الشدة في العيش (maqayis); البأساء اسم للحرب والمشقة والضرر (ayn;tahdhib); بئس الرجل اشتدت حاجته فهو بائس (sihah); البائس الرجل النازل به بلية أو عدم (ayn;tahdhib); البأساء الجوع (tahdhib); الأبؤس الداهية (sihah); بؤسا له وتوسا وجوسا بمعنى واحد (tahdhib); البؤس والتباؤس والتبؤس أي الضراعة للفقر أو أن يجعل نفسه ذليلا (mufradat)
- **B003** üzülüp yakınma — hoşnutsuz ve üzgün kişi · hoşlanmadığı bir şey kendisine ulaştı ve üzüldü · üzülme ve yakınma
  المبتئس المفتعل من الكراهة والحزن (maqayis); لا تبتئس أي لا تحزن ولا تشتك (sihah); ابتأس الرجل إذا بلغه شيء يكرهه (tahdhib); غير حزين ولا كاره (tahdhib); لا تلزم البؤس ولا تحزن (mufradat)
- **B004** kötüleme sözü — övgünün karşıtı olan kötüleme sözü · sonrasındaki sözle birlikte kullanılan kötüleme kalıbı
  بئس نقيض صلح يجري مجرى نعم (ayn); بئس ضد نعم (jamhara); بئس كلمة ذم ونعم كلمة مدح (sihah); بئس مستوفية لجميع الذم (tahdhib); بئس كلمة تستعمل في جميع المذام (mufradat)
- **B005** sana zarar yok — sana zarar yok; güvendesin · sana zarar yok anlamındaki yerel söz
  إذا قال الرجل لعدوه لا بأس عليك فقد أمنه (tahdhib); لبات أي لا بأس (tahdhib)

## ق و م (root_001273): 62:5 ٱلْقَوْمِ, 62:5 ٱلْقَوْمَ, 62:11 قَآئِمًا

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

## ك ذ ب (root_001290): 62:5 كَذَّبُوا۟

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

## ه د ي (root_001583): 62:5 يَهْدِى (also echo for 62:6 هَادُوٓا۟)

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

## ECHO ه د د (root_001580): for 62:5 يَهْدِى, 62:6 هَادُوٓا۟: withheld observed target; not identity

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

## ظ ل م (root_000967): 62:5 ٱلظَّٰلِمِينَ, 62:7 بِٱلظَّٰلِمِينَ

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

## ق و ل (root_001272): 62:6 قُلْ, 62:8 قُلْ, 62:11 قُلْ

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

## ECHO ق ل ل (root_001251): for 62:6 قُلْ, 62:8 قُلْ, 62:11 قُلْ: withheld observed target; not identity

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

## ه و د (root_001605): 62:6 هَادُوٓا۟

- **B001** yanlıştan dönüp doğruya yönelme — pişmanlıkla yanlıştan dönüp doğruya yönelme · sana yönelerek yanlışımızdan döndük · yanlışından döndü ve doğruya yöneldi · yanlıştan dönme ve iyi işler yapma · yanlışından dönüp doğruya yönelen kişi · yanlışlarından dönüp doğruya yönelen kişiler
  إنا هدنا إليك في التوبة (maqayis)؛ الهود التوبة (ayn)؛ هاد يهودا هودا تاب ورجع إلى الحق (sihah)؛ الهود الرجوع برفق وصار في التعارف التوبة (mufradat)
- **B002** Yahudiler ve Yahudiliğe girme ya da onun yolunu izleme — Yahudiler · Yahudiler · Yahudi oldu veya Yahudiliğin din yolunu izledi · Yahudi oldu · bir kişinin Yahudi olması · onu Yahudi yaparlar
  أما اليهود فمن هاد يهود إذا تاب هودا (maqayis)؛ الهود اليهود هادوا يهودون هودا وسميت اليهود اشتقاقا من هادوا (ayn)؛ هاد وتهود إذا صار يهوديا والهود اليهود (sihah)؛ هاد فلان إذا تحرى طريقة اليهود في الدين (mufradat)
- **B003** yavaş ve yumuşak ilerleme ya da sakin söyleyiş — sürünürcesine yavaş yürüme · yumuşak ve ağır adımlarla yürüdü · eğitici hayvanı yumuşak tempoyla sürdü · konuşmada sakin ve düşük söyleyiş · sakin ve düşük sesli şarkı
  التهويد المشي الرويد (maqayis)؛ التهويد شبه الدبيب في المشي والسكون في الكلام (ayn)؛ التهويد المشي الرويد مثل الدبيب والتهويد في المنطق هو الساكن (sihah)؛ تهود في مشيه إذا مشى مشيا رفيقا وهود الرائض الدابة سيرها برفق (mufradat)
- **B004** uyuma veya içkinin gevşetip sarhoş etmesi — uyudu · uyuma · içki, içen kişiyi gevşetip ağırlaştırdı · içkinin sarhoş etmesi
  هود إذا نام (maqayis)؛ هود الشراب نفس الشارب إذا خثرت له نفسه (maqayis)؛ التهويد أيضا النوم وتهويد الشراب إسكاره (sihah)
- **B005** güvenlik umduran barış ve karşılıklı uzlaşma — güvenlik veya düzelme umduran durum; barış ve yumuşak yönelim · karşılıklı çatışmazlık, uzlaşma ve birbirine yaklaşma
  الهوادة الحال ترجى معها السلامة بين القوم والمهاودة الموادعة (maqayis)؛ الهوادة البقية من القوم يرجى بها صلاحهم (ayn)؛ الهوادة الصلح والميل والمهاودة المصالحة والممايلة (sihah)
- **B006** hörgüç — hörgüç · hörgüçler
  الهودة بالتحريك السنام والجمع هود (sihah)
- **B007** bir peygamberin ve onun adını taşıyan surenin adı — bir peygamberin adı; bağlama göre o adı taşıyan sure
  هود اسم نبي (sihah;mufradat)؛ تقول هذه هود إذا أردت سورة هود (sihah)

## ز ع م (root_000633): 62:6 زَعَمْتُمْ

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

## و ل ي (root_001684): 62:6 أَوْلِيَآءُ

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

## د و ن (root_000502): 62:6 دُونِ

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

## ء ن س (root_000059): 62:6 ٱلنَّاسِ

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

## م ن ي (root_001450): 62:6 فَتَمَنَّوُا۟, 62:7 يَتَمَنَّوْنَهُۥٓ

- **B001** ölçüp belirleyerek hükme bağlama — onun için gerçekleşecek şeyi belirlemek · belirlenmiş pay veya hüküm
  أصل واحد صحيح يدل على تقدير شيء ونفاذ القضاء به (maqayis)؛ منى له الماني أي قدر المقدر (maqayis;sihah;mufradat)؛ المنى القدر (sihah;tahdhib)؛ قدر الله لك ما يسرك (tahdhib)
- **B002** meni — meni; yavrunun oluşmasına kaynaklık eden erkek üreme sıvısı · yeni canlının biçimlendiği meni damlasından
  ماء الإنسان مني أي يقدر منه خلقته (maqayis)؛ المني ماء الرجل من شهوته الذي يكون منه الولد (ayn)؛ المنى ماء الرجل وهو مشدد (sihah)؛ المني مشدد (tahdhib)؛ المني للذي قدر به الحيوانات (mufradat)
- **B003** belirlenmiş ölüm — belirlenmiş ölüm veya ecel · ölüme götüren olaylar veya eceller · ölüm
  المنية الموت لأنها مقدرة على كل (maqayis;sihah)؛ المنا الموت وكذلك المنية والمنايا (ayn)؛ المنايا الأحداث والحمام الأجل والحتف القدر (tahdhib)؛ المنية وهو الأجل المقدر للحيوان (mufradat)
- **B004** dilemek ve zihinde tasarlamak — bir şeyi zihninde tasarlayıp gerçekleşmesini dilemek · dilekler; kişinin içinden geçirdiği istekler · dilek
  تمنى الإنسان كذا أمل يقدره (maqayis)؛ المنى جماعة المنية وهي ما يتمناه الرجل والأمنية أفعولة (ayn)؛ الأمنية واحدة الأماني (sihah)؛ التمني حديث النفس بما يكون وبما لا يكون (tahdhib)؛ التمني تقدير شيء في النفس وتصويره فيها (mufradat)
- **B005** Mekke'deki hac ibadeti yeri — Mekke'deki belirli hac ibadeti yeri · o ibadet yerine gelmek veya orada konaklamak
  ومنى منى مكة سمي به لما قدر أن يذبح فيه (maqayis)؛ منى مقصور موضع معروف بمكة (ayn)؛ منى مقصور موضع بمكة (sihah)؛ سميت منى لما يمنى بها من الدم أي يراق (tahdhib)
- **B006** standart tartı veya hacim ölçüsü — standart tartı veya hacim ölçüsü
  المنا الذي يوزن به لأنه تقدير يعمل عليه (maqayis)؛ المنا الذي يوزن به والجميع الأمناء (ayn)؛ المنا مقصور الذي يوزن به (sihah)؛ المكيال الذي يكيلون به السمن وغيره (tahdhib)؛ المنا الذي يوزن به فيما قيل (mufradat)
- **B007** metni düzeniyle okuyup aktarma — kitabı okumak veya sesli aktarmak · kitap okuma veya sesli aktarma
  تمنى الكتاب قرأه (maqayis)؛ لأن القراءة تقدير ووضع كل آية موضعها (maqayis)؛ تمنى كتاب الله أي تلاه (ayn)؛ تمنيت الكتاب قرأته (sihah)؛ التمني التلاوة (tahdhib)
- **B008** eylemini başkasınınkiyle ölçüp ona denk olmaya çalışma — başkasıyla yarışıp ona denk olmaya çalışmak · işi uzatma veya bekleme · yapılana denk karşılık verme
  مانى يماني مماناة إذا بارى غيره (maqayis)؛ يقدر فعله بفعل غيره يريد أن يساويه (maqayis)؛ المماناة المطاولة (sihah;tahdhib)؛ المماناة الانتظار (sihah;tahdhib)؛ المماناة المكافأة (tahdhib)؛ المماناة المعاقبة في الركوب (tahdhib)
- **B009** devenin gebeliğini denetleme dönemi ve muayenesi — devenin gebeliğinin araştırıldığı günler · devenin gebe kalıp kalmadığını elle muayene etme
  منية الناقة الأيام التي يتعرف فيها ألاقح هي أم حامل (maqayis)؛ الأيام التي يستبرأ فيها لقاحها من حيالها (sihah;tahdhib)؛ الاستمناء أن يأتي صاحبها فيضرب بيده على صلاها (tahdhib)
- **B010** tam karşısında ve hizasında bulunma [kalıp] — evim senin evinin tam karşısında ve hizasında
  المنا الحذاء تقول داري منا دارك أي حذاءها (ayn)؛ داري منا دار فلان أي مقابلتها (sihah)؛ داري بمنى داره أي بحذائها (tahdhib)
- **B011** bir durumla sınanıp ona uğratılma [kalıp] — bununla sınandım; bu başıma geldi
  منيت بكذا أي ابتليت (ayn)؛ منوته ومنيته إذا ابتليته (sihah)؛ مناه الله بحبها يمنيه ويمنوه أي ابتلاه (tahdhib)
- **B012** belirli bir puta verilen ad — Kureyş'e ya da Hüzeyl ve Huzaa'ya ait belirli bir putun adı · o puta bağlılık bildiren nispet biçimi
  مناة اسم صنم لقريش (ayn)؛ مناة اسم صنم كان لهذيل وخزاعة بين مكة والمدينة (sihah)؛ النسبة إليها منوى (sihah)
- **B013** asılsız söz veya haber uydurma [kalıp] — asılsız haberler uydurmak · bu sözü asılsız olarak uydurmak
  فلان يتمنى الأحاديث أي يفتعلها (sihah)؛ تمنى كذب ووضع حديثا لا أصل له (tahdhib)؛ تمتني هذا القول أي تختلقه (tahdhib)؛ أماني أي أكاذيب (tahdhib)
- **B014** ailesine karşı koruma kıskançlığından yoksun olma — ailesine karşı koruma kıskançlığı göstermeyen erkek · aileye karşı koruma kıskançlığının azlığı
  المماناة قلة الغيرة على الحرم (tahdhib)؛ يقال للديوث المماذل والمماني والمماذي (tahdhib)

## م و ت (root_001454): 62:6 ٱلْمَوْتَ, 62:8 ٱلْمَوْتَ

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

## ص د ق (root_000852): 62:6 صَٰدِقِينَ

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

## ء ب د (root_000004): 62:7 أَبَدًۢا

- **B001** sonsuz süre ve kalıcı kılma — sonsuz zaman, çok uzun süre · sonsuza dek, kesintisiz olarak · çağlar boyunca, sonsuza dek · bütün zaman boyunca · kalıcı kılma · sürekli kılınmış, devredilemez · sonsuza dek veya çok uzun süre kalmak
  طول المدة (maqayis)؛ الأبد الدهر (maqayis;sihah)؛ أبد الآبدين وأبد الدهر (tahdhib)؛ الأبد الدائم والتأبيد التخليد (sihah)؛ مدة الزمان الممتد (mufradat)؛ وقفا مؤبدا وتأبيدا (tahdhib)
- **B002** yabanıllaşıp insandan ürkme — devenin yabanıllaşması · hayvanın yabanıllaşıp insandan ürkmesi · yabani ve ürkek hayvanlar · yabani inek
  تأبد البعير توحش (maqayis;mufradat)؛ أوابد كأوابد الوحش (maqayis;tahdhib)؛ أبدت البهيمة أي توحشت (sihah)؛ توحشت ونفرت من الإنس (tahdhib)؛ الوحشيات (mufradat)
- **B003** terk edilip ıssızlaşmak [kalıp] — evin terk edilip ıssızlaşması ve yabani hayvanlara kalması
  تأبد المنزل خلا (maqayis)؛ تأبد المنزل أي أقفر وألفته الوحوش (sihah)؛ خلا منها أهلها خلفتهم الوحش بها قد تأبدت (tahdhib)
- **B004** her yıl doğuran dişi — her yıl doğuran dişi eşek, kısrak veya köle kadın
  الإبد ذات النتاج من المال كالأمة والفرس والأتان (maqayis)؛ الابد الولود من أمة أو أتان (sihah)؛ أتان إبد في كل عام تلد (tahdhib)
- **B005** yüzün lekelenip sertleşmesi [kalıp] — yüzün lekelenmesi, sertleşmesi veya öfkeden değişmesi
  تأبد وجهه كلف (maqayis)؛ تأبد وجه فلان توحش وقد فسر بغضب (mufradat)
- **B006** bir yerde kalıp ayrılmama — bir yerde kalıp oradan ayrılmamak · kış yaz aynı arazide kalan kuşlar
  أبد بالمكان أي أقام به (sihah)؛ أبدت بالمكان إذا أقمت به ولم تبرحه (tahdhib)؛ الطير المقيمة بأرض شتاءها وصيفها أوابد (tahdhib)
- **B007** uzun süre anılan olağanüstü olay — uzun süre anılan olağanüstü iş veya olay · unutulmayacak kadar sıra dışı bir iş yapmak
  الأبدة الفعلة تبقى على الأبد (maqayis)؛ جاء فلان بآبدة أي بداهية يبقى ذكرها على الأبد (sihah)
- **B008** yadırgatıcı söz veya başıboş uyak — yadırgatıcı, alışılmadık sözcük · şiirin başıboş veya aykırı uyakları
  الشوارد من القوافي أوابد (sihah)؛ الكلمة الوحشية آبدة وجمعه الأوابد (tahdhib)
- **B009** öfkelenmek veya birine öfkelenmek [kalıp] — adamın öfkelenmesi · ona öfkelenmek
  أبد الرجل غضب (sihah)؛ أبد إذا غضب عليه (tahdhib)؛ وقد فسر بغضب (mufradat)

## ق د م (root_001207): 62:7 قَدَّمَتْ

- **B001** ayak — ayak
  القدم ما يطأ عليه الإنسان (ayn;tahdhib)؛ القدم واحد الأقدام (sihah)؛ القدم قدم الرجل وجمعه أقدام (mufradat)؛ قدم الإنسان معروفة ولعلها سميت بذلك لأنها آلة للتقدم والسبق (maqayis)
- **B002** önceden oluşmuş etki veya paye — öncül etki, iyilik veya saygın konum · önceden kazanılmış iyi paye · önceden işlenmiş kötülük · önder ve saygın kişi · hükümdar veya önder
  القدمة والقدم أيضا السابقة في الأمر وللكافرين قدم شر (ayn)؛ القدم أيضا السابقة في الأمر ولفلان قدم صدق أي أثرة حسنة (sihah)؛ قدم الصدق المنزلة الرفيعة والقدم السابقة وكل ما قدمت من خير والعمل الصالح واليد والمعروف والصنيعة والشرف القديم (tahdhib)؛ متقدم على فلان أي أشرف منه (mufradat)؛ لفلان قدم صدق أي شيء متقدم من أثر حسن والملك هو المقدم (maqayis)؛ رجل قدموس سيد وهو ذلك المعنى (maqayis-variant)
- **B003** eskilik ve önceden var olma — eskilik; sonradan oluşmama · eski; geçmiş zamana dayanan · eskiden; geçmiş zamanda · eski olan
  القدم مصدر القديم من كل شيء (ayn)؛ قدم الشيء فهو قديم والقدم خلاف الحدوث وقدما كان كذا (sihah)؛ القدم العتق مصدر القديم وقد قدم يقدم (tahdhib)؛ حديث وقديم والقدم وجود فيما مضى (mufradat)؛ القدم خلاف الحدوث وشيء قديم إذا كان زمانه سالفا (maqayis)؛ القدموس القديم وأصله من القدم (maqayis-variant)
- **B004** öne geçme, önde ilerleme veya erken davranma — öne geçmek; önde olmak · öne geçme ve ilerleme · ön taraf; önde · önüne geçmek; vaktinden önce davranmak · duraksamadan ileri gitmek
  قدم فلان قومه أي يكون أمامهم والقدم المضي أمام ويمضي قدما أي لا ينثني وقدام خلاف وراء والقدم ضد الأخر (ayn)؛ قدم أي تقدم وقدم بين يديه أي تقدم ومضى قدما لم يعرج ولم ينثن واستقدم وتقدم بمعنى ومقدم نقيض مؤخر (sihah)؛ القدم المضي وهو الإقدام وقدام خلاف وراء والقدم ضد أخر وقدم فلان فلانا إذا تقدمه ولا تقدموا معناه لا تتقدموا قبل الوقت (tahdhib)؛ به اعتبر التقدم والتأخر (mufradat)؛ أصل صحيح يدل على سبق وأصله مضى فلان قدما لم يعرج ولم ينثن ومقدمة الجيش أوله (maqayis)
- **B005** yolculuktan dönüş — yolculuktan dönmek; geri gelmek · yolculuktan dönüş; yolcunun geliş zamanı · yolculuktan dönenler
  القدوم الرجوع من السفر وقدم يقدم (ayn)؛ قدم من سفره قدوما ومقدما والقدام القادمون من سفر (sihah)؛ القدوم الإياب من السفر وقدم فلان من سفره يقدم قدوما (tahdhib)؛ من الباب قدم من سفره قدوما ويقال القدام القادمون من سفر (maqayis)
- **B006** cesaretle öne atılma ve gözüpeklik — gözüpeklik; cesaretle öne atılma · bir işe cesaretle girişmek · gözüpek, atılgan savaşçı · ileri! · gözüpek ve öne atılan kişi
  رجل قدم مقتحم للأشياء يتقدم الناس ويمضي في الحرب قدما (ayn)؛ أقدم على الأمر إقداما والإقدام الشجاعة وأقدم زجر للفرس والمقدام الكثير الإقدام على العدو (sihah)؛ أقدم على قرنه إقداما وقدما ومقدما إذا تقدم عليه بجرأة وضده الإحجام ورجل مقدام في الحرب جريء (tahdhib)؛ أقدم على الشيء إقداما وأقدم زجر للفرس ومضى القوم في الحرب اليقدمية (maqayis)
- **B007** ön bölüm veya ilk kesim — ordunun öncü birliği · gözün veya başın ön kısmı · alın önü ve perçem bölgesi · kuşun ön kanat telekleri · eyer takımının ön kısmı · deve veya ineğin öndeki iki meme başı · dağın öne çıkan burnu · yüzüstü düşmek
  مقدم العين ما يلي الأنف والمقدمة الناصية وما استقبلك من الجبهة والجبين وقادمة الرحل والقادمة الريشة التي تلي منكب الجناح (ayn)؛ قوادم الطير مقاديم ريشه وقيدوم الجبل أنف يتقدم منه وقيدوم كل شيء مقدمه وصدره ومقدمة الجيش أوله وقادمتا الناقة (sihah)؛ مقدمة الجيش الذين يتقدمون الجيش ومقدم العين ومقدم الرأس والمقدمة الناصية وقادمة الرحل وللناقة قادمان وقوادم ريش الطائر (tahdhib)؛ قادمة الرحل خلاف آخرته وقادمة من أطباء الناقة وقادم الإنسان رأسه وقوادم الطير ومقدمة الجيش أوله وقيدوم الجبل أنف يتقدم منه (maqayis)
- **B008** ahşap yontma keseri — ahşap yontma keseri
  القدوم مخفقة الحديدة التي ينحت بها الخشب (ayn)؛ القدوم التي ينحت بها مخففة ولا تقل قدوم بالتشديد (sihah)؛ القدوم التي ينحت بها وجمعها قدم واختتن إبراهيم بالقدوم قال قطعه بها (tahdhib)؛ مما شذ عن هذا الأصل القدوم الحديدة ينحت بها وهي معروفة (maqayis)
- **B009** belirli bir yer adı — belirli bir yer adı
  القدوم أيضا اسم موضع (sihah)؛ القدوم مكان (maqayis)
- **B010** bir işe yönelip onu amaçlamak [kalıp] — bir işe yönelip onu amaçlamak
  قدم فلان إلى أمر كذا أي قصد له ومنه وقدمنآ إلى ما عملوا قال الفراء والزجاج قدمنا عمدنا وقصدنا (tahdhib)

## ي د ي (root_001693): 62:7 أَيْدِيهِمْ

- **B001** el ve elin uğradığı bedensel durumlar — el · elinden vurmak · eli kökünden kesilmiş kimse · el ağrısı · eli tuzağa yakalanmış olmak
  اليَد الجارحة (mufradat)؛ اليد أصلها يدي وجمعها أيد ويدي (sihah)؛ يديت الرجل إذا ضربت يده (jamhara;sihah;tahdhib;mufradat)؛ رجل ميدي أي مقطوع اليد واليداء وجع اليد (tahdhib)
- **B002** güç, yeterlik ve güçlendirme — güç ve yeterlik · güç · güçlendirmek · buna gücüm yetmez
  اليد القوة وأيده أي قواه (sihah)؛ ما لي به يدان أي قوة (tahdhib;mufradat)؛ أولي الأيدي أي أولي القوة (tahdhib;mufradat)
- **B003** karşılıksız iyilik ve bağış — iyilik ve karşılıksız yarar · iyilikte bulunmak · satış, borç ya da karşılık olmadan vermek
  أيديت إلى الرجل يدا إذا أسديتها إليه (jamhara)؛ اليد النعمة والإحسان (sihah;tahdhib;mufradat)؛ أعطاه مالا عن ظهر يد تفضلا ليس من قرض ولا مكافأة (sihah;tahdhib)؛ يده مطلقة عبارة عن إيتاء النعيم (mufradat)
- **B004** elinde bulunma, sahiplik ve denetim [kalıp] — onun elinde, sahipliğinde ve denetiminde
  هذا الشيء في يدي أي في ملكي (sihah)؛ هذه الضيعة في يد فلان أي ملكه (tahdhib)؛ للحوز والملك يقال هذا في يد فلان (mufradat)
- **B005** egemenlik ve buyurma gücü — egemenlik ve buyurma gücü · rüzgarın yön verme gücü
  اليد السلطان (tahdhib)؛ اليد في هذا لفلان أي الأمر النافذ لفلان (tahdhib)؛ أيديكم فوق أيديهم (mufradat)؛ عن قهر وذل (tahdhib)
- **B006** boyun eğme, bağlılık ve güvence üstlenme — boyun eğme ve uyma · buyruğuna girdim · bunun için sana güvence veriyorum · bağlılıktan çıkmak
  عن يد أي عن ذلة واستسلام (sihah)؛ اليد الطاعة واليد الاستسلام (tahdhib)؛ هذه يدي لك (tahdhib)؛ يدي لك رهن بكذا أي ضمنت وكفلت (tahdhib)؛ خلع فلان يده عن الطاعة (tahdhib)
- **B007** elden ele verme, peşin ödeme ve iki fiyatlı satış — elden ele, doğrudan karşılık vererek · karşılığını elden vermek · elden ele verme · iki ayrı fiyatla
  ياديت فلانا جازيته يدا بيد (sihah)؛ أعطيته مياداة أي من يدي إلى يده (sihah)؛ عن يد نقدا عن ظهر يد ليس بنسيئة (sihah;tahdhib)؛ ابتعت الغنم باليدين أي بثمنين مختلفين (sihah;tahdhib)؛ باع غنمه اليدين أن يسلمها بيد ويأخذ ثمنها بيد (tahdhib)
- **B008** önünde ya da hemen öncesinde [kalıp] — önünde veya hemen öncesinde
  بين يدي الساعة أهوال أي قدامها (sihah)؛ بين يديك كذا لكل شيء أمامك (tahdhib)؛ يثور الرهج بين يدي المطر ويهيج السباب بين يدي القتال (tahdhib)
- **B009** kişinin kendi yaptığı iş ve doğurduğu sorumluluk [kalıp] — senin yaptığın, işlediğin ve kazandığın şey
  هذا ما قدمت يداك أي جنيته أنت (sihah)؛ ذلك بما كسبت يداك (tahdhib)؛ مما كتبت أيديهم فنسبته إلى أيديهم تنبيه على أنهم اختلقوه (mufradat)
- **B010** pişman olup hayıflanma [kalıp] — pişman olup hayıflanmak
  سقط في يديه وأسقط أي ندم (sihah)؛ اليد الندم ويقال سقط في يده إذا ندم (tahdhib)؛ ولما سقط في أيديهم أي ندموا (mufradat)
- **B011** yönlere dağılıp gitme ve izlenen yol [kalıp] — her yana dağılıp gitmek · deniz yolu
  ذهبوا أيدي سبا وأيادي سبا أي متفرقين (sihah)؛ اليد الطريق يقال أخذ فلان يد بحر إذا أخذ طريق البحر (tahdhib)؛ ذهب القوم أيدي سبا أي متفرقين في كل وجه (tahdhib)
- **B012** zaman boyunca, sonsuza dek [kalıp] — zaman boyunca, sonsuza dek
  لا أفعله يد الدهر أي أبدا (sihah)؛ يد الدهر مد زمانه (tahdhib)؛ شبه الدهر فجعل له يد في قولهم يد الدهر (mufradat)
- **B013** bir nesnenin tutacağı, ucu ya da uzantısı [kalıp] — nesnenin tutacağı, ucu, kolu veya uzantısı
  يد الثوب ما فضل منه إذا تعطفت به والتحفت (sihah)؛ يد الفأس مقبضها ويد القوس سيتها (tahdhib)؛ قميص قصير اليدين أي قصير الكمين (tahdhib)؛ يد المسند (mufradat)
- **B014** geniş, bol ve rahat [kalıp] — geniş ve rahat yaşam · bol ve geniş giysi
  عيش يدي واسع (jamhara)؛ ثوب يدي وأدي أي واسع (sihah)؛ ثوب يدي واسع (tahdhib)
- **B015** eli işe yatkın ve becerikli — eli işe yatkın, becerikli
  امرأة يدية أي صناع (sihah;mufradat)؛ رجل يدي (sihah;mufradat)؛ النسبة إلى يد يدي (tahdhib)
- **B016** birlik içinde destek ve koruma [kalıp] — başkalarına karşı tek güç olarak dayanışmak · onun destekçisi ve koruyucusu
  المسلمون يد على من سواهم أي كلمتهم ونصرتهم واحدة (tahdhib)؛ اليد الغياث واليد منع الظلم (tahdhib)؛ فلان يد فلان أي وليه وناصره (mufradat)؛ أنا يدك (mufradat)
- **B017** yemeye başlama buyruğu [kalıp] — ye, yemeğe başla
  اليد الأكل يقال ضع يدك أي كل (tahdhib)

## ECHO ء ي د (root_000071): for 62:7 أَيْدِيهِمْ: withheld observed target; not identity

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## ف ر ر (root_001142): 62:8 تَفِرُّونَ

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

## ل ق ي (root_001372): 62:8 مُلَٰقِيكُمْ

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

## ر د د (root_000555): 62:8 تُرَدُّونَ

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

## ECHO م ر د (root_001413): for 62:8 تُرَدُّونَ: withheld observed target; not identity

- **B001** doğal örtüsünden yoksun veya arındırılmış olma — üzerindeki doğal örtüden yoksun · sakalı henüz çıkmamış genç · yapraksız veya kabuğu soyulmuş dal · yapraksız ağaç · bitkisiz, düz kumluk · bitki bitmeyen düz arazi veya kumluk · çenesinin altında tüy bulunmayan at · kasık kılları bulunmayan kadın
  تجريد الشيء من قشره أو ما يعلوه من شعره؛ شجرة مرداء وغصن أمرد ورملة مرداء وغلام أمرد وفرس أمرد (maqayis;sihah;tahdhib;mufradat)؛ الرمال المرداء التي لا تنبت شجرة والأمرد الذي لم تنبت له لحية (ayn)
- **B002** yüzeyi düzleyip pürüzsüzleştirme ve böyle işlenmiş yapı — düz ve pürüzsüz; düzgün ve yüksek yapı · yapıyı sıvayıp düzleştirme · bir şeyi yumuşatıp perdahlamak veya pürüzsüzleştirmek
  الممرد البناء الطويل (maqayis)؛ تمريد البناء تمليسه (sihah)؛ الممرد المملس والتمريد التمليس والتطيين (tahdhib)؛ ممرد من قوارير أي مملس (mufradat)؛ التمريد تمليس الطين والتسوية (ayn)
- **B003** iyilikten kopup azgınca direnme ve kötülükte ısrar etme — iyilikten yoksun, azgın ve başkaldıran kimse · şiddetle başkaldıran, iyilikten yoksun kimse · ikiyüzlülüğe alışıp onda yerleşmek · kötülükte azıp sınırı aşmak · ona başkaldırıp direnmek · bir şeye alışıp onda beceri kazanma
  المارد العاتي وكذا المريد كأنه تجرد من الخير (maqayis)؛ المارد العاتي والمرود على الشيء المرون عليه (sihah)؛ المريد من شياطين الإنس والجن وتمرد علينا أي عتا واستعصى ومرد على الشر أي عتا وطغى (tahdhib)؛ المارد والمريد المتعري من الخيرات ومردوا على النفاق أي ارتكسوا عن الخير (mufradat)؛ تمرد عليه أي عصى واستعصى ومرد على الشيء أي عتا وطغى (ayn)
- **B004** yiyeceği ezip sıvıyla karıştırarak yumuşatma — yiyeceği ezip karıştırarak yumuşatmak · ekmeği suda ezip yumuşatmak · sütte bekletilip yumuşatılmış hurma · çocuğun annesinin memesini emmesi
  مرد الطعام يمرد مردا ماثه حتى يلين وهو من الإبدال والأصل مرس (maqayis)؛ مرد الخبز يمرده مردا أي ماثه حتى يلين والمريد التمر ينقع في اللبن ومرد الصبي ثدي أمه (sihah)؛ المرد الثريد ومرد الطعام إذا ماثه حتى يلين فقد مرده وتمر مريد (tahdhib)
- **B005** Salvadora persica ağacının ham meyvesi — Salvadora persica ağacının ham meyvesi
  المرد حمل الأراك (ayn)؛ المرد ثمر الأراك الغض منه (sihah)؛ البرير ثمر الأراك فالغض منه المرد والنضيج الكباث (tahdhib)
- **B006** tekneyi sırıkla iterek ilerletme — tekneyi uzun bir sırıkla iterek ilerletmek · tekneyi itmeye yarayan uzun sırık
  المرد دفعك السفينة بالمردي أي خشبة يدفع بها الملاح السفينة والفعل مرد يمرد (ayn)؛ المرد دفعك السفينة بالمروي وهي خشبة يدفع بها الملاح (tahdhib)
- **B007** güvercinlikteki küçük yumurtlama bölmesi — güvercinlikteki küçük yumurtlama bölmesi · üst üste dizilmiş güvercin yuvalıkları
  التمراد بيت الحمام يجعل لمبيضه فإذا جعلت نسقا بعضها فوق بعض فهي التماريد (ayn)؛ التمراد بيت صغير يجعل في بيت الحمام لمبيضه فإذا جعلت نسقا بعضها فوق بعض فهي التماريد (tahdhib)
- **B008** boyun — boyun
  المراد العنق وهو القياس إن صح (maqayis)؛ المراد بالفتح العنق (sihah)

## غ ي ب (root_001117): 62:8 ٱلْغَيْبِ

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

## ش ه د (root_000822): 62:8 وَٱلشَّهَٰدَةِ

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

## ن ب ء (root_001464): 62:8 فَيُنَبِّئُكُم

- **B001** bir yerden başka bir yere geçip belirme — bir yerden başka bir yere çıktı veya gelip belirdi · başka bir yerden gelen ya da çıkan · toprak onu getirip ortaya çıkardı
  الإتيان من مكان إلى مكان (maqayis)؛ ينبأ من أرض إلى أرض وسيل نابئ ورجل نابئ (maqayis;ayn;sihah;tahdhib)؛ نبأت على القوم إذا طلعت عليهم (sihah;tahdhib)؛ نبأت به الأرض جاءت به (sihah)
- **B002** bilgi taşıyan haber — haber · bilgi sağlayan önemli haber · haberler · ona güçlü biçimde haber verdim · ona haber verdim · ona bu konuda haber verdim · ona bunu bildirdim · ondan haber istedim
  النبأ الخبر (maqayis;ayn;sihah;tahdhib)؛ نبأته وأنبأته واستنبأته والجميع الأنباء (ayn;sihah;tahdhib)؛ خبر ذو فائدة عظيمة يحصل به علم أو غلبة ظن (mufradat)؛ نبأته أبلغ من أنبأته (mufradat)
- **B003** Tanrı'dan haber veren elçi — Tanrı'dan haber veren elçi · Tanrı ile insanlar arasındaki kutsal elçilik görevi
  من همز النبي فلأنه أنبأ عن الله تعالى (maqayis)؛ النبي ينبئ الأنباء عن الله عز وجل (ayn)؛ النبئ لانه أنبأ عن الله تعالى (sihah)؛ النبوة سفارة بين الله وبين ذوي العقول من عباده (mufradat)؛ النبي لكونه منبئا بما تسكن إليه العقول الذكية (mufradat)
- **B004** Tanrı elçiliğini yalan yere ileri sürme — Tanrı elçisi olduğunu yalan yere ileri sürdü · haberleri Tanrı'dan gelmeyen yalancı elçi
  تنبأ مسيلمة بالهمز (sihah)؛ العرب كانت نبيئة مسيلمة نبيئة سوء (sihah)؛ تنبأ فلان ادعى النبوة (mufradat)؛ لم يستعمل إلا في المتقول في دعواه (mufradat)
- **B005** okun hedefi çizmeden başka yere düşmesi [kalıp] — attı; oku hedefi çizmeden sapıp başka yere düştü
  رمى الرامي فأنبأ إذا لم يشرم كأن سهمه عدل عن الخدش وسقط مكانا آخر (maqayis)؛ رمى فأنبأ إذا لم يشرم ولم يخدش (sihah)
- **B006** hafif ve belirsiz ses — hafif, gizli ve belirsiz ses
  النبأة الصوت (maqayis)؛ النبأة النغية وهو صوت يشك فيه ولا يتيقن (ayn)؛ النبأة الصوت الخفى (sihah)؛ النبأة الصوت ليس الشديد (tahdhib)؛ النبأة الصوت الخفي (mufradat)
- **B007** istenen yere götüren açık yol — istenen yere götüren açık yol; kolay geçilen düz yer
  النبي يقال الطريق الواضح يأخذك إلى حيث تريد (ayn)؛ مكان النبي من الكاثب هو ما سهل من الأرض (ayn)

## ع م ل (root_001046): 62:8 تَعْمَلُونَ

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

## ء م ن (root_000054): 62:9 ءَامَنُوٓا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ن د و (root_001486): 62:9 نُودِىَ

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

## ECHO ن د ي (root_001487): for 62:9 نُودِىَ: withheld observed target; not identity

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

## ECHO ن و د (root_001563): for 62:9 نُودِىَ: withheld observed target; not identity

- **B001** bir yandan öbür yana sallanarak hareket etme — sallanmak, salınarak hareket etmek · sallanma, salınarak hareket etme · sallanma, salınarak hareket etme · dalın hareket edip sallanması · Yahudilerin okullarında bedenlerini sallamaları
  ناد الإنسان ينود نَوْدا ونَوَداناً؛ تَنَوَّد الغصن وتنوع إذا تحرك؛ نَوَدان اليهود في مدارسهم مأخوذ من هذا

## ص ل و (root_000879): 62:9 لِلصَّلَوٰةِ, 62:10 ٱلصَّلَوٰةُ

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

## ECHO ص ل ي (root_000880): for 62:9 لِلصَّلَوٰةِ, 62:10 ٱلصَّلَوٰةُ: withheld observed target; not identity

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

## ي و م (root_001700): 62:9 يَوْمِ

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

## ج م ع (root_000259): 62:9 ٱلْجُمُعَةِ

- **B001** dağınık parçaları bir araya toplama — dağınık şeyi bir araya toplamak · mal biriktirmek ve saymak · ayrı yerlerdeki şeyleri bütünüyle bir araya getirmek · çeşitli yerlerden toplanmış şey · çeşitli yerlerden toplanıp götürülen yağma malı
  أصل واحد يدل على تضام الشيء (maqayis)؛ الجمع مصدر جمعت الشيء (ayn)؛ الجمع خلاف التفريق جمعت الشيء إذا ضممت بعضه إلى بعض (jamhara)؛ جمعت الشئ المتفرق فاجتمع (sihah)؛ الجمع أن تجمع شيئا إلى شيء (tahdhib)؛ الجمع ضم الشيء بتقريب بعضه من بعض (mufradat)
- **B002** bir araya gelmiş insan topluluğu — insan topluluğu veya çokluk · farklı boylardan karışık insan topluluğu · toplanmış topluluk veya ordu
  الجماع الأشابة من قبائل شتى (maqayis)؛ الجمع اسم لجماعة الناس والجموع اسم لجماعة الناس (ayn)؛ الجماع ما تجمع من أشابة الناس وأخلاطهم (jamhara)؛ جماع الناس أخلاطهم وهم الأشابة من قبائل شتى (sihah)؛ الجماع يقال في أقوام متفاوتة اجتمعوا (mufradat)
- **B003** düşünüp kesin bir tutuma bağlanma — bir işi yapmaya kesin biçimde karar vermek · hazırlık, kesin karar veya görüş birliği · işi veya düzeni sağlamlaştırıp kesinleştirmek
  أجمعت على الأمر إجماعا وأجمعته (maqayis)؛ أجمعت على الأمر إجماعا إذا عزمت عليه (jamhara)؛ أجمعت الأمر وعلى الأمر إذا عزمت عليه (sihah)؛ الإجماع الإعداد والعزيمة على الأمر (tahdhib)؛ أجمعت كذا فيما يكون جمعا يتوصل إليه بالفكرة (mufradat)
- **B004** toplanmayla belirlenen yer veya gün — insanların toplandığı yer · insanların bir araya geldiği kutsal yer veya günler için kullanılan ad · insanların ibadet veya yeniden diriliş için toplandığı gün · haftalık toplu ibadete katılıp namazı kılmak · halkı toplu ibadet için bir araya getiren ibadet yeri · ibadet için toplanma çağrısı · yolunu yitirme korkusuyla insanların ayrılmadığı ıssız alan
  جمع مكة سمي لاجتماع الناس به وكذلك يوم الجمعة (maqayis)؛ المجمع حيث يجمع الناس (ayn)؛ أيام جمع أيام منى والجمعة مشتقة من اجتماع الناس فيها للصلاة (jamhara)؛ يقال للمزدلفة جمع لاجتماع الناس فيها (sihah)؛ يوم الجمع ويوم يجمعكم ليوم الجمع (mufradat)
- **B005** sıkılmış avuç veya bir avuçluk miktar — sıkılmış avuç veya bu avuçla vurma · bir avuç dolusu
  ضربته بجمع كفي وجمع كفي (maqayis)؛ ضربته بجمع كفي وأعطيته من الدراهم جمع الكف (ayn)؛ ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها (jamhara)؛ جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه (sihah)
- **B006** cinsel birleşme — cinsel birleşme için kullanılan örtülü söz · cinsel ilişkide bulunma
  الجماع كناية عن النكاح (jamhara)؛ المجامعة المباضعة (sihah)
- **B007** çocuğu karnındayken ölen veya el değmemiş kalan kadın — çocuğu karnındayken veya el değmemişken ölmek · kocasıyla cinsel birleşme yaşamamış kadın · ilk kez gebe kalan dişi eşek
  ماتت بجمع أي في بطنها ولد (maqayis)؛ ماتت المرأة بجمع أي مع ما في بطنها وكذلك إذا ماتت عذراء (ayn)؛ ماتت المرأة بجمع إذا ماتت وولدها في بطنها (jamhara)؛ أمر بني فلان بجمع أي لم يقتضها وماتت فلانة بجمع أي ماتت وولدها في بطنها (sihah)
- **B008** elleri boyna bağlayan kelepçe — elleri boyna bağlayan kelepçe veya demir bağ
  الجوامع الأغلال (maqayis)؛ الجوامع الأغلال الواحدة جامعة (jamhara)؛ الجامعة الغل لأنها تجمع اليدين إلى العنق (sihah)
- **B009** eksiksiz bütünlük — bedeni eksiksiz hayvan veya varlık · bedence derli toplu veya gelişimini tamamlamış adam · büyüyüp bütün dış giysileri giyecek çağa gelmek · bütünlük bildiren pekiştirme sözleri · dağılmamış bütün veya hepsi
  الجمعاء من البهائم وغيرها التي لم يذهب من بدنها شيء (maqayis)؛ رجل جميع أي مجتمع في خلقه (ayn)؛ الرجل المجتمع الذي بلغ أشده (sihah)؛ جميع لدينا محضرون (mufradat)
- **B010** parçaları toplanıp tamamlanma [kalıp] — koşusunu ve gücünü bütünüyle toplamak · çeşitli yerlerden birleşip büyümek · işlerin kişi için yoluna girip hazır duruma gelmesi
  استجمع الفرس جريا (maqayis)؛ استجمع للمرء أموره (ayn)؛ استجمع السيل اجتمع من كل موضع واستجمع الفرس جريا (sihah)
- **B011** adı bilinmeyen çekirdekten yetişme hurma ağacı — adı bilinmeyen çekirdekten yetişme hurma ağacı
  الجمع كل لون من النخل لا يعرف اسمه لنخل خرج من النوى (maqayis)؛ الجمع أيضا الدقل لنخل يخرج من النوى ولا يعرف اسمه (sihah)
- **B012** büyük kazan — büyük kazan
  قدر جماع وجامعة وهي العظيمة (maqayis)؛ قدر جامعة وهي العظيمة وقدر جماع أيضا للعظيمة (sihah)
- **B013** bir işte başkasıyla birleşip destek olma [kalıp] — bir işte başkasıyla birleşip ona destek olmak
  جامعت الرجل على الأمر مجامعة وجماعا إذا مالأته عليه (jamhara)؛ جامعه على أمر كذا أي اجتمع معه (sihah)

## س ع ي (root_000709): 62:9 فَٱسْعَوْا۟

- **B001** hedefe doğru hızlı ve amaçlı ilerleme — hızlı yürüme, hafif koşma veya amaçlı gidiş · hızlı yürümek, hafifçe koşmak veya yönelmek · anma çağrısına yönelmek veya gitmek · iki kutsal durak arasındaki özel ibadet yürüyüşü
  السعي عدو ليس بشديد (ayn)؛ سعى الرجل يسعى سعيا أي عدا (sihah)؛ السعي والذهاب بمعنى واحد وليس هذا باشتداد؛ سعى إذا مشى وسعى إذا عدا وسعى إذا قصد (tahdhib)؛ السعي المشي السريع وهو دون العدو؛ وخص المشي فيما بين الصفا والمروة بالسعي (mufradat)
- **B002** bir işte çalışıp kazanma ve çaba gösterme — iş, kazanç ve ciddi çaba · çalışmak, kazanmak ve bir işi yürütmek · ailesinin geçimi için çalışmak · çalışma ve iş yürütme
  كل عمل من خير أو شر فهو السعي؛ السعي العمل أي الكسب (ayn)؛ إذا عمل وكسب (sihah)؛ أصل السعي التصرف في كل عمل؛ السعي يكون في الصلاح ويكون في الفساد؛ المرء يسعى لغاريه أي يكسب (tahdhib)؛ يستعمل للجد في الأمر خيرا كان أو شرا (mufradat)
- **B003** bir topluluğun işini yürüten yetkili görevli — vergi toplama görevi · atanmış yönetici veya vergi toplama görevlisi · atanmış yöneticiler veya vergi toplama görevlileri · vergi toplamakla görevlendirilmek · bir din topluluğunun başkanı ve yetkili temsilcisi
  السعاية في أخذ الصدقات (maqayis)؛ الساعي الذي يولى قبض الصدقات والجمع سعاة (ayn)؛ من ولى شيئا على قوم فهو ساع عليهم وأكثر ما يقال ذلك في ولاة الصدقة (sihah)؛ الساعي الذي يقوم بأمر أصحابه عند السلطان؛ عامل الصدقات ساع؛ ساعي اليهود والنصارى هو رئيسهم؛ من ولى عملا على قوم فهو ساع عليهم (tahdhib)؛ خصت السعاية بأخذ الصدقة (mufradat)
- **B004** birini üst makama kötüleyerek ihbar etme — üst makama kötüleyerek ihbar etme · birini yöneticiye kötüleyerek ihbar etmek · üst makama söz taşıyan ihbarcı
  السعاية أن تسعى بصاحبك إلى وال أو من فوقه (ayn)؛ سعى به إلى الوالي إذا وشى به (sihah)؛ الساعي الذي يسعى بصاحبه إلى سلطانه؛ القتات والساعي والماحل واحد؛ الساعي مثلث بإهلاكه ثلاثة نفر (tahdhib)؛ خصت السعاية بالنميمة (mufradat)
- **B005** özgürlük bedelini çalışarak ödeme — köleleştirilmiş kişinin özgürlüğü için çalışması · özgürlük bedelini çalışarak kazanma · özgürlük sözleşmesinin bedelini çalışarak ödemek · köleleştirilmiş kişiyi kendi bedeli için çalıştırmak · kalan özgürlük bedelini çalışarak ödeyen kişi
  سعاية العبد إذا كوتب أن يسعى فيما يفك رقبته (maqayis)؛ السعاية ما يستسعى فيه العبد من ثمن رقبته (ayn)؛ سعى المكاتب في عتق رقبته سعاية؛ استسعيت العبد في قيمته (sihah)؛ استسعاء العبد إذا عتق بعضه ورق بعضه؛ يستسعى في ثلثي رقبته (tahdhib)؛ خصت السعاية بكسب المكاتب لعتق رقبته (mufradat)
- **B006** övünç getiren soylu ve cömert iş — cömertlikle kazanılan onurlu iş ve başarı · övünç veren onurlu işler ve başarılar · barış için bedel üstlenen uzlaştırıcılar
  المسعاة في الكرم والجود (maqayis)؛ المسعاة في الكرم والجود (ayn)؛ المسعاة واحدة المساعي في الكرم والجود (sihah)؛ أصحاب الحمالات لحقن الدماء وإطفاء النائرة سعاة؛ مآثر أهل الشرف والفضل مساعي واحدتها مسعاة (tahdhib)؛ المسعاة بطلب المكرمة (mufradat)
- **B007** köleleştirilmiş kadınla ilişki veya onu cinsel kazanca zorlama — köleleştirilmiş bir kadınla evlilik dışı cinsel ilişkiye girmek · köleleştirilmiş kadınlarla sınırlı evlilik dışı ilişki veya onları cinsel kazanca zorlama
  ساعي الرجل الأمة إذا فجر بها؛ لا تكون المساعاة إلا في الإماء خاصة (maqayis)؛ يقال في الأمة خاصة قد ساعاها؛ لا تكون المساعاة إلا في الإماء؛ إماء ساعين في الجاهلية (sihah)؛ المساعاة الزنى؛ لا تكون في الحرائر إنما تكون في الإماء؛ مساعاة الأمة إذ ساعاها مالكها فضرب عليها ضريبة تؤديها بالزنى (tahdhib)؛ خصت المساعاة بالفجور (mufradat)
- **B008** aynı uğraşta rakibini yenme — benimle aynı uğraşta yarıştı, ben de onu yendim
  ساعانى فلان فسعيته أسعيه إذا غلبته فيه (sihah)

## ECHO س و ع (root_000760): for 62:9 فَٱسْعَوْا۟: withheld observed target; not identity

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

## ذ ك ر (root_000516): 62:9 ذِكْرِ, 62:10 وَٱذْكُرُوا۟

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

## و ذ ر (root_001638): 62:9 وَذَرُوا۟

- **B001** et parçası; bir aktarımda etsiz kemik parçası — et parçası; bir aktarıma göre etsiz kemik parçası · et parçaları · bol et parçalı ekmek yemeği
  الوذرة وهي الفدرة من اللحم (maqayis)؛ الوذرة قطعة عظم لا لحم فيه (ayn)؛ الوذرة بالتسكين الفدرة وهي القطعة من اللحم (sihah)؛ الوذرة القطعة من اللحم مثل الفدرة (tahdhib)؛ الوذر بضع اللحم (tahdhib)؛ الوذرة قطعة من اللحم (mufradat)؛ ثريدة كثيرة الوذر (tahdhib)
- **B002** eti parçalama veya yarayı çizerek açma — eti parçalama veya yarayı çizerek açma · eti parçalara ayırmak · yarayı çizerek açmak · et parçasını küçük parçalara bölmek
  التوذير أن يشرط الجرح (maqayis)؛ وذرت اللحم توذيرا قطعته وكذلك الجرح إذا شرطته (sihah)؛ وقد وذرت الوذرة أذرها وذرا إذا بضعتها بضعا (tahdhib)
- **B003** bir şeyi bırakmak — bir şeyi bırakmak · önemsiz gördüğü şeyi bir yana atmak · bunu bırak · onu bırakmak
  ذر ذا (maqayis)؛ أماتت المصدر من يذر والفعل الماضي واستعملته في الحاضر والأمر (ayn)؛ ذره أي دعه وهو يذره (sihah)؛ ذرذا ودع ذا ولا يقال وذرته (tahdhib)؛ يذر الشيء أي يقذفه لقلة اعتداده به (mufradat)
- **B004** cinsel göndermeli ağır soy sövgüsü; ad biçiminde klitoris — cinsel organ göndermeli ağır bir soy sövgüsü · ağır bir soy sövgüsü · klitoris
  يا ابن شامة الوذر (maqayis;ayn;sihah;tahdhib)؛ كلمة قذف (sihah)؛ كلمة معناها القذف (tahdhib)؛ عرض لها بأعضاء الرجال (maqayis)؛ أراد المذاكير (tahdhib)؛ أرادوا بها القلف (tahdhib)؛ الوذفة والوذرة بظارة المرأة (tahdhib)

## ب ي ع (root_000169): 62:9 ٱلْبَيْعَ

- **B001** bedel karsiligi alis-satis — bedel karsiliginda satma veya satis islemi · satin alma yonuyle kullanilan alis-satis adi · bir seyi bedel karsiliginda satmak · bir seyi satin almak · baskasinin alisi uzerine araya girip satin almamak · satilan sey veya satisin konusu olan mal · satici ve alici olan iki taraf · ticaret icin alinip satilan mallar · satin alma · alis-satis islemi · karsilikli alisveriste bulunma · birinden seyi kendisine satmasini isteme · satis sozlesmesi veya satis islemi · satis bicimi veya satistaki iyi tutum
  بيع الشيء وربما سمي الشرى بيعا والمعنى واحد (maqayis)؛ بعت الشيء بمعنى اشتريته والابتياع الاشتراء والبيعان البائع والمشتري (ayn)؛ البيع مصدر باع والبيع أيضا الشراء (jamhara)؛ بعت الشيء شريته وبعته أيضا اشتريته وهو من الأضداد والابتياع الاشتراء (sihah)؛ البيع إعطاء المثمن وأخذ الثمن والشراء إعطاء الثمن وأخذ المثمن (mufradat)
- **B002** satisa sunma — bir seyi satisa cikarmak · satisa konmus veya satilik
  فإن عرضته للبيع قلت أبعته (maqayis)؛ أبعت الشيء عرضته (sihah;mufradat)
- **B003** baglilik sozu verme — baglilik sozu veya uyma taahhudu · baglilik sozu verme · hukumdara baglilik sozu vermek
  البيعة الصفقة على إيجاب البيع وعلى المبايعة والطاعة (ayn)؛ بايعته من البيع والبيعة جميعا والتبايع مثله (sihah)؛ بايع السلطان إذا تضمن بذل الطاعة له ويقال لذلك بيعة ومبايعة (mufradat)
- **B004** Hristiyan kilisesi — Hristiyan kilisesi veya toplanma evi · Hristiyan kiliseleri
  البيعة كنيسة النصارى وجمعها بيع (ayn)؛ البيعة والجمع بيع بيت للنصارى يجتمعون فيه (jamhara)؛ البيعة بالكسر للنصارى (sihah)

## خ ي ر (root_000452): 62:9 خَيْرٌ, 62:11 خَيْرٌ, 62:11 خَيْرُ

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

## ق ض ي (root_001237): 62:10 قُضِيَتِ

- **B001** kesin hüküm veya buyruk vermek — hükme bağladı veya kesin olarak buyurdu · hüküm verme ve işi kesin sonuca bağlama · hüküm veya karara bağlanmış konu · insanlar arasında hüküm veren ve kararları uygulayan yargıç · yargıç olarak görevlendirildi
  قضى يقضي قضاء وقضية أي حكم (ayn); القضاء الحكم وقضى أي حكم (sihah); قضى ربك أي أمر ربك والقضاء الفصل في الحكم (tahdhib); القضاء فصل الأمر وقضى ربك أي أمر (mufradat); القضاء الحكم وسمي القاضي قاضيا لأنه يحكم الأحكام وينفذها (maqayis)
- **B002** kalıp içinde kesin bildirmek veya ahit ya da talimat iletmek [kalıp] — ona bir ahit veya talimat iletti · onlara kesin biçimde bildirdik
  قضى إليه عهدا معناه الوصية (ayn); قضينا إليه ذلك الأمر أي أنهيناه إليه وأبلغناه (sihah); قضينا إلى بني إسرائيل أي أعلمناهم إعلاما قاطعا وقضى الله عهدا معناه الوصية (tahdhib); أعلمناهم وأوحينا إليهم وحيا جزما (mufradat)
- **B003** ölümün gerçekleşmesi veya gerçekleştirilmesi — ölüm onun yaşamını sona erdirdi · öldü · insanın yaşamını sona erdiren ölüm · öldürücü zehir · insanların arasında gerçekleşen ölümler
  فلما قضينا عليه الموت أي أتى والقاضية المنية (ayn); ضربه فقضى عليه أي قتله وقضى نحبه أي مات (sihah); فلما قضينا عليه الموت أي أتى عليه والقاضية المنية (tahdhib); يعبر عن الموت بالقضاء وقضى نحبه معناه مات (mufradat); سميت المنية قضاء لأنه أمر ينفذ (maqayis)
- **B004** tamamlayıp bitirmek veya sona erip tükenmek — kendine yüklediği adağı yerine getirdi · gereksinimini giderip işini bitirdi · sona erdi, tükenip gitti · ibadetini tamamladı · süreyi tamamlayıp sonuna ulaştı · isteğini giderip işini bitirdi · içindekileri bütünüyle döküp ağlamasını bitirdi · gereksinimini bütünüyle giderdi · iş geri alınamayacak biçimde sonuçlandı
  انقضى الشيء وتقضى أي فني وذهب (ayn); بمعنى الفراغ وقضيت حاجتي وانقضى الشيء وتقضى (sihah); قضي الأمر أتم إهلاكهم وقضى صلاته فرغ منها والانقضاء ذهاب الشيء وفناؤه (tahdhib); فإذا قضيتم مناسككم وليقضوا تفثهم وأيما الأجلين قضيت وفلما قضى زيد منها وطرا (mufradat)
- **B005** yapıp kusursuzca tamamlamak ve yürürlüğe koymak — giysiyi ve evi yapıp işçiliğini kusursuzlaştırdı · onları yedi gök olarak yaratıp kusursuzca tamamladı · yapacağın işi gerçekleştir · tasarlamadan sonra kesinleştirip yürürlüğe koyma · işçiliği tamamlanmış sağlam zırhlar
  قضاه أي صنعه وقدره ومنه فقضاهن سبع سموات (sihah); كل ما أحكم فقد قضي وخلقهن وعملهن وصنعهن وفاقض ما أنت قاض أي فاعمل (tahdhib); فقضاهن سبع سماوات إشارة إلى إيجاده الإبداعي والفراغ منه (mufradat); أصل يدل على إحكام أمر وإتقانه وإنفاذه لجهته (maqayis)
- **B006** borcu ödeyerek veya tahsil ederek kapatmak — borcunu ödeyip aradaki yükümlülüğü kapattı · borcunun ödenmesini istedi veya alacağını tahsil etti · ondan hakkını istedi veya hakkını teslim aldı · kan bedeli veya zorunlu ödemede geçerli sayılan deve
  قضيت ديني واقتضى دينه وتقاضاه (sihah); قضى فلان دينه وقطع ما بينه وبينه وتقاضيته حقي فقضانيه واقتضيت مالي عليه (tahdhib); قضى الدين فصل الأمر فيه برده والاقتضاء المطالبة بقضائه (mufradat)
- **B007** uzun süre bırakılan tulumun bozulup eskimesi — tulum uzun süre bırakıldığı için bozulup eskidi
  قضي السقاء قضا فهو قض إذا طال تركه في مكان ففسد وبلي (ayn)
- **B008** kuru üzüm çekirdeği ve onu yemek — adam kuru üzüm çekirdeğini yedi · kuru üzüm çekirdeği
  قضى الرجل إذا أكل القضى وهو عجم الزبيب (tahdhib)

## ن ش ر (root_001503): 62:10 فَٱنتَشِرُوا۟

- **B001** açıp yayma, dallandırıp dağıtma — bir şeyi açmak, serip yaymak ve görünür hale getirmek · haberi duyurup yaymak · insanların yeryüzüne dağılıp kendi işlerine yönelmesi · sıçrayıp çevreye saçılan su damlacıkları · Tanrı dağılmış işlerini toparlasın · geniş, uzun ve yayvan tüyler · dağınık halde esen veya yağmur bulutlarını yayan rüzgarlar · yağmur getiren ya da bulutları yayan rüzgarlar; ayrıca rüzgarları yayan melekler yorumu
  أصل صحيح يدل على فتح شيء وتشعبه (maqayis)؛ نشرت الثوب والكتاب نشرا بسطته (ayn)؛ نشر المتاع وغيره بسطه وانتشر الخبر ذاع (sihah)؛ جاء الجيش نشرا أي متفرقين وضم الله نشرك ما انتشر من أمرك ونشر الماء ما تطاير منه (tahdhib)؛ نشر الثوب والصحيفة والسحاب والنعمة والحديث بسطها (mufradat)؛ اكتسى البازي ريشا نشرا أي منتشرا واسعا طويلا (maqayis;sihah;mufradat)
- **B002** ölüyü yeniden hayata döndürme ve yeniden dirilme — ölümden sonra yeniden hayat bulma · ölünün yeniden yaşaması · Tanrı'nın ölüyü yeniden hayata döndürmesi · ölü toprağı yağmurla canlandırmak
  نشر الله الموتى فنشروا وأنشر الله الموتى أيضا (maqayis)؛ النشور الحياة بعد الموت ينشرهم الله إنشارا (ayn)؛ نشر الميت نشورا أي عاش بعد الموت وأنشرهم الله أي أحياهم (sihah)؛ أنشر الله الميت ونشره فنشر الميت لا غير ونشرهم الله أي بعثهم (tahdhib)؛ نشر الميت نشورا وأنشر الله الميت فنشر وفأنشرنا به بلدة ميتا (mufradat)
- **B003** hoş koku; uykudan sonraki ağız ve beden kokusu — hoş ve duyulur koku · bir kadının uykudan sonra ağzından, burnundan ve beden kıvrımlarından gelen koku
  النشر الريح الطيبة (maqayis;ayn;tahdhib)؛ النشر الرائحة الطيبة (sihah)؛ نشره أمامه يعني ريح المسك (ayn;tahdhib)؛ النشر ريح فم المرأة وأنفها وأعطافها بعد النوم (tahdhib)
- **B004** kuruduktan veya kaybolduktan sonra yeniden belirme — toprağın bahar veya yağmurla yeniden bitki vermesi · yağmurla yeniden yeşeren ve hayvanlara zarar verebilen kuru ot · uyuzun geri gelmesi veya iyileşen yerde tüyün yeniden çıkması
  نشرت الأرض أصابها الربيع فأنبتت والنشر الكلأ ييبس ثم يصيبه المطر (maqayis)؛ نشرت الأرض تنشر نشورا إذا أصابها الربيع فأنبتت (ayn)؛ النشر الكلأ إذا يبس ثم أصابه مطر فاخضر (sihah)؛ النشر أن يخرج النبت يبطئ عنه المطر فييبس ثم يصيبه مطر بعد اليبس (tahdhib)؛ النشر الكلأ اليابس إذا أصابه مطر فينشر أي يحيا (mufradat)؛ نشر الجرب ينشر نشرا ونشورا إذا حيي بعد ذهابه ونبات الوبر على الجرب بعد ما يبرأ (tahdhib)
- **B005** ahşabı testereyle kesme ve çıkan talaş — ahşabı testereyle kesmek · testereyle keserken dökülen ahşap talaşı
  نشرت الخشبة بالمنشار نشرا (maqayis)؛ نشرت الخشبة أنشرها إذا قطعتها بالمنشار والنشارة ما سقط منه (sihah)؛ نشرت الخشبة بالمنشار أنشرها نشرا (tahdhib)
- **B006** koyunların gece otlamaya dağılması veya dağılmış sürü — koyunların gece otlamak için dağılması veya bu haldeki sürü
  النشر أن تنتشر الغنم بالليل فترعى (maqayis;sihah;tahdhib)؛ النشر الغنم المنتشر (mufradat)
- **B007** ön kol damarları; hayvanda kiriş bozukluğu; cinsel sertleşme — ön kolun iç yüzündeki damarlar · hayvanda yorgunluktan kirişin şişmesi veya yerinden oynaması · erkeğin cinsel organının sertleşmesi
  النواشر عروق باطن الذراع (maqayis;ayn;sihah;tahdhib;mufradat)؛ الانتشار انتفاخ عصب الدابة من تعب (maqayis;sihah;tahdhib)؛ انتشر الرجل أنعظ (sihah)؛ انتشر ذكره إذا قام (tahdhib)
- **B008** sözlü koruma ve tedaviyle sıkıntıyı giderme — akıl sağlığı bozulmuş veya büyüden etkilendiği düşünülen kişiden sıkıntıyı gideren sözlü tedavi · koruyucu sözlerle tedavi uygulama · etkilenmiş kişiyi bu uygulamayla tedavi edip sıkıntısını gidermek
  النشرة رقية علاج للمجنون ينشر بها عنه تنشيرا (ayn)؛ التنشير من النشرة وهي كالتعويذ والرقية ونشره أي رقاه (sihah)؛ النشرة علاج رقية يعالج بها المجنون ينشر بها عنه تنشيرا (tahdhib)
- **B009** çocuk yazısı; açılmış sayfalar; mühürsüz resmi yazı — çocukların deftere yazdığı yazılar · hükümdarın mühürsüz yazılı buyruğu · açılıp serilmiş sayfalar
  التناشير كتابة الغلمان في الكتاب (ayn;tahdhib)؛ صحف منشرة شدد للكثرة (sihah)؛ المنشور من كتب السلطان ما كان غير مختوم (tahdhib)؛ نشر الصحيفة بسطها وإذا الصحف نشرت (mufradat)
- **B010** cömertlik ve onurluluk — cömert ve onurlu kadın · cömertlik ve onurluluk
  امرأة منشورة ومشبورة إذا كانت سخية كريمة؛ نشرا بين يدي رحمته أي سخاء وكرامة (tahdhib)

## ب غ ي (root_000138): 62:10 وَٱبْتَغُوا۟

- **B001** bir şeyi arayıp istemek; başkası için aramak veya arayışına yardım etmek — bir şeyi aramak ve istemek · bir şeyi çaba göstererek aramak · ihtiyaç; aranan veya istenen şey · bir şeyi birisi için aramak · birinin bir şeyi aramasına yardım etmek veya onu arayan duruma getirmek
  طلب الشيء؛ بغيت الشيء إذا طلبته؛ البغية الحاجة؛ أبغيتك الشيء إذا أعنتك على طلبه (maqayis)؛ البغية مصدر الابتغاء؛ بغيت الشيء وابتغيته طلبته (ayn)؛ بغى ضالته؛ ابتغيت الشيء وتبغيته إذا طلبته (sihah)؛ البغي طلب تجاوز الاقتصاد؛ الابتغاء خص بالاجتهاد في الطلب (mufradat)
- **B002** uygun, mümkün veya hak edilmiş olmak — uygun olmak; mümkün olmak; hak edilmiş olmak
  ما ينبغي لك أن تفعل كذا؛ بغيته فانبغى (maqayis)؛ لا ينبغي لك أن تفعل كذا وما انبغى لك (ayn)؛ ينبغي لك أن تفعل كذا هو من أفعال المطاوعة (sihah)؛ ينبغي مطاوع بغى؛ لا يتسخر ولا يتسهل له؛ على معنى الاستئهال (mufradat)
- **B003** haddi aşarak haksızlık etmek — haddi aşma, haksızlık ve baskı · birine karşı haddini aşıp haksızlık etmek · haddini aşan ve haksızlık eden kişi · birbirine haksızlık etmek
  جنس من الفساد؛ أن يبغي الإنسان على آخر؛ البغي الظلم (maqayis)؛ البغي الظلم والباغي الظالم (ayn)؛ البغي التعدي؛ بغى الرجل على الرجل استطال؛ كل مجاوزة في الحد وإفراط على المقدار فهو بغي؛ تباغوا أي بغى بعضهم على بعض (sihah)؛ البغي على ضربين؛ تجاوز الحق إلى الباطل؛ بغى تكبر (mufradat)
- **B004** yaranın şişip bozulması veya içinde irin kalmış halde kapanması [kalıp] — yaranın şişip ilerleyerek bozulması · yaranın içinde irinli bozukluk kalmış halde kapanması
  بغى الجرح إذا ترامى إلى فساد (maqayis)؛ بغى الجرح ورم وترامى إلى فساد؛ برئ جرحه على بغى وفيه شيء من نغل (sihah)؛ بغى الجرح تجاوز الحد في فساده (mufradat)
- **B005** evlilik dışı cinsel ilişki ve buna bağlı kişi adları — kadının evlilik dışı cinsel ilişkiye girmesi · evlilik dışı cinsel ilişki; cinsel ahlaka aykırı davranış · evlilik dışı cinsel ilişkiye giren kadın; bu adla anılan kadın köle · kadın köleler veya evlilik dışı cinsel ilişkiye giren kadınlar · evlilik dışı cinsel ilişkiden doğan çocuk
  البغي الفاجرة؛ بغت تبغي بغاء وهي بغي (maqayis)؛ بغى بغاء أي فجر؛ البغية من الزنى؛ البغايا الجواري (ayn)؛ بغت المرأة بغاء أي زنت فهي بغي والجمع بغايا؛ خرجت المرأة تباغي أي تزاني؛ الأمة يقال لها بغي (sihah)؛ بغت المرأة بغاء إذا فجرت (mufradat)
- **B006** göğün şiddetli, bol ve gereğinden fazla yağdırması [kalıp] — göğün şiddetli veya gereğinden fazla yağmur yağdırması · göğün en şiddetli ve bol yağmuru
  بغي المطر وهو شدته ومعظمه؛ بغي السماء أي معظم مطرها (maqayis)؛ بغت السماء اشتد مطرها؛ بغي السماء أي معظم مطرها (sihah)؛ بغت السماء تجاوزت في المطر حد المحتاج إليه (mufradat)
- **B007** atın koşarken çalımlı ve neşeli davranması [kalıp] — atın koşarken çalımlı ve neşeli davranması
  اختيال الفرس ومرحه بغي؛ لا يقال فرس باغ (maqayis)؛ البغي في عدو الفرس اختيال ومرح؛ لا يقال فرس باغ (ayn)؛ البغي اختيال ومرح في الفرس؛ لا يقال فرس باغ (sihah)
- **B008** ordudan önce ilerleyen öncüler — ordudan önce ilerleyen öncüler · öncü topluluğun tek bir üyesi
  البغايا الطلائع الواحدة بغية أيضا (ayn)؛ البغايا أيضا الطلائع التي تكون قبل ورود الجيش (sihah)

## ك ث ر (root_001286): 62:10 كَثِيرًا

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

## ف ل ح (root_001175): 62:10 تُفْلِحُونَ

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

## ر ء ي (root_000531): 62:11 رَأَوْا۟

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

## ECHO ر و ي (root_000615): for 62:11 رَأَوْا۟: withheld observed target; not identity

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

## ت ج ر (root_000176): 62:11 تِجَٰرَةً, 62:11 ٱلتِّجَٰرَةِ

- **B001** kazanc amacli alis satis — kazanc icin mal alip satmak · kazanc icin alis satis isine girmek · sermayeyi kazanc icin alip satma isi · alis satisla ugrasan kimse · alis satisla ugrasan kimseler toplulugu · alis satis yapan kimseler · alis satisinda kar etmek
  التجارة معروفة (maqayis)؛ وقد تجر تجارة (ayn;tahdhib)؛ تجر يتجر تجرا وتجارة (sihah)؛ التجارة التصرف في رأس المال طلبا للربح (mufradat)؛ ربح فلان في تجارته (tahdhib)
- **B002** alis satis yeri [kalıp] — alis satis icin gidilen veya bu isin yapildigi yer
  أرض متجرة يتجر إليها (ayn;tahdhib)؛ أرض متجرة يتجر فيها (sihah)
- **B003** pazarda ragbet goren deve [kalıp] — satisa ciktiginda kolay alici bulan disi deve · pazarda ragbet goren disi deve · satista kolay alici bulan develer
  ناقة تاجرة للنافقة وأخرى كاسدة (sihah)؛ ناقة تاجر أي نافقة في التجارة والسوق (sihah)؛ ناقة تاجرة إذا كانت تنفق إذا عرضت على البيع لنجابتها ونوق تواجر (tahdhib)
- **B004** kazanc yolunu bilen usta [kalıp] — o konuda usta · bir seyi iyi bilen ve ondan kazanc saglama yolunu taniyan
  إنه لتاجر بذلك الأمر أي حاذق به (tahdhib)؛ فلان تاجر بكذا أي حاذق به عارف الوجه المكتسب منه (mufradat)

## ل ه و (root_001382): 62:11 لَهْوًا, 62:11 ٱللَّهْوِ

- **B001** başka bir uğraşla belirli bir şeyden alıkoyma — insanı başka bir şeyden alıkoyan uğraş · bir şeyi unutup bırakmak ve ondan yüz çevirmek · bir şeyden yüz çevirip onu bırakmak · onu bırak ve onunla uğraşma · birini başka bir şeyle oyalayıp alıkoymak · birini bir şeyle avutmak ve oyalamak · önemsiz şeylerle oyalanmış, dalgın gönüller
  اللهو كل شيء شغلك عن شيء فقد ألهاك، ولهيت عن الشيء إذا تركته لغيره (maqayis); اللهو ما شغلك من هوى أو طرب، واللهو الصدوف عن الشيء (ayn); لهيت عن الشيء إذا سلوت عنه وتركت ذكره وأضربت عنه، وألهاه أي شغله، ولهاه به تلهية أي علله (sihah); اللهو ما يشغل الإنسان عما يعنيه ويهمه، وألهاه كذا أي شغله (mufradat)
- **B002** oyun ve zevk veren uğraşla eğlenme — oyun, neşe ve zevk veren eğlence · bir şeyle oynayıp eğlenmek · onunla oynayıp oyalanmak · bir kadınla oyalanmak · kişinin oyalanıp eğlendiği kadın · kadın veya çocuk için kullanılan örtmece · cinsel birleşme için kullanılan örtmece · birbirleriyle oyalanıp eğlenmek · bilmeceye benzer ortak bir eğlence
  وقد يكنى باللهو عن غيره، المرأة، الولد (maqayis); اللهو ما شغلك من هوى أو طرب، والتهى بامرأة، يقال هو أي اللهو المرأة نفسها (ayn); لهوت بالشيء إذا لعبت به، وقد يكنى باللهو عن الجماع، امرأة، ولدا، والألهية من اللهو (sihah); يعبر عن كل ما به استمتاع باللهو، المرأة والولد (mufradat)
- **B003** değirmen ağzına atılan tahıl ve ona benzetilen armağan — öğütülmek üzere değirmen ağzına atılan tahıl · değirmenin ağzına tahıl atmak · değirmene atılan tahıla benzetilen armağan veya para · bol armağan veren · çok cömert ve bol armağan veren
  اللهوة ما يطرحه الطاحن في ثقبة الرحى بيده، وبذلك سمي العطاء لهوة (maqayis); اللهوة ما يلقى في فم الرحى من الحب للطحن (ayn); اللهوة بالضم ما يلقيه الطاحن في فم الرحى، واللهوة أيضا العطية (sihah); اللهوة ما يشغل به الرحى مما يطرح فيه، وسميت العطية لهوة تشبيها بها (mufradat)
- **B004** küçük dil — boğaza doğru sarkan küçük dil; kimi kullanımlarda ağzın en arkası · küçük diller
  اللهاة أقصى الفم، سميت لهاة لما يلقى فيها من الطعام (maqayis); اللهاة أقصى الفم وهي لحمة مشرفة على الحلق (ayn); اللهاة الهنة المطبقة في أقصى سقف الفم والجمع اللها واللهوات واللهيات (sihah); اللهاة اللحمة المشرفة على الحلق، وقيل بل هو أقصى الفم (mufradat)

## ف ض ض (root_001162): 62:11 ٱنفَضُّوٓا۟

- **B001** parçalarını ayırarak kırmak — bir şeyi parçalarını ayırarak kırmak · yazının mührünü kırıp açmak · Tanrı dişlerini dökmesin · toprak keseklerini kırmaya yarayan alet · kırılıp dağılmak
  فضضت الشيء إذا فرقته (maqayis)؛ فضضت الخاتم من الكتاب كسرته؛ الفض كسر الأسنان (ayn)؛ فضضت الشيء إذا كسرته أو فرقته ولا يكون إلا الكسر بالتفرقة نحو فضضت الختام (jamhara)؛ الفض الكسر بالتفرقة وفضضت ختم الكتاب ولا يفضض الله فاك (sihah)؛ فضضت الخاتم من الكتاب أي كسرته؛ لا يفضض الله فاك؛ معناه لا يسقط الله أسنانك (tahdhib)؛ الفض كسر الشيء والتفريق بين بعضه وبعضه كفض ختم الكتاب (mufradat)
- **B002** topluluğu dağıtmak veya toplulukça dağılmak — topluluğu dağıtmak · toplulukça dağılıp gitmek · hizmet topluluğunuzu dağıtmak
  انفض القوم تفرقوا (maqayis)؛ الفض تفريقك حلقة من الناس بعد اجتماع؛ فضضتهم فانفضوا (ayn)؛ الانفضاض التفرق وانفض القوم وارفضوا إذا تفرقوا (jamhara)؛ فضضت القوم فانفضوا أي فرقتهم فتفرقوا (sihah)؛ تفريقك حلقة من الناس بعد اجتماعهم؛ فضضتهم فانفضوا؛ لانفضوا من حولك أي تفرقوا (tahdhib)؛ عنه استعير انفض القوم (mufradat)
- **B003** gümüş — gümüş · gümüş kakmalı gem
  وممكن أن يكون الفضة من هذا الباب (maqayis)؛ الفضة وتجمع على فضض (ayn)؛ الفضة معروفة (jamhara)؛ الفضة معروفة ولجام مفضض أي مرصع بالفضة (sihah)؛ الفضة معروفة؛ قوارير من فضة (tahdhib)؛ الفضة اختصت بأدون المتعامل بها من الجواهر (mufradat)
- **B004** kırılıp saçılan parçalar — bir şey kırılınca ondan ayrılan parçalar · kırıntı ve dağınık kalıntı · sen ondan kopmuş bir parçasın · parçalanıp dağılmak
  الفضاض ما تفضض من الشيء إذا انفض (maqayis)؛ كل شيء تفرق من شيء تكسر فهو فضاضة؛ فضض من لعنة الله (jamhara)؛ فضاض الشيء ما تفرق منه عند كسرك إياه؛ كل شيء تفرق فهو فضض؛ أنت فضض من لعنة الله (sihah)؛ أنت فضض منه أرادت أنك قطعة منه (tahdhib)
- **B005** geniş ve bol olmak — giysi, zırh veya yaşayışta genişlik ve bolluk · bol ve geniş giysi · geniş zırh · ferah ve bolluk içindeki yaşayış · çok su taşıyan bulut · uzun, iri yapılı ve eti dolgun genç kadın · çok veren, eli açık adam · idrarın dişi devenin butlarına yayılması
  الفضفضة سعة الثوب وثوب فضفاض ودرع فضفاضة (maqayis)؛ الفضفضة سعة الثوب ودرع فضفاضة واسعة وسحابة فضفاضة كثيرة الماء (ayn)؛ الفضفضة سعة الثوب والدرع والعيش؛ ثوب فضفاض وعيش فضفاض ودرع فضفاضة (sihah)؛ الفضفاضة الدرع الواسعة؛ قميص فضفاض واسع؛ جارية فضفاضة كثيرة اللحم؛ رجل فضفاض كثير العطاء؛ تفضفض البول (tahdhib)؛ درع فضفاضة وفضفاض واسعة (mufradat)
- **B006** tatlı ve akıcı su — tatlı, akıcı ve içimi kolay su · suya çıktığı ilk anda erişmek · temizlenirken çevreye yayılan su
  الفضيض الماء العذب سمي لفضاضته وسهولة مره في الحلق (maqayis)؛ الفضيض ماء عذب تصيبه ساعة يخرج (ayn)؛ الفضيض الماء العذب؛ افتضضت الماء إذا أصبته ساعة يخرج؛ الفضيض الماء السائل (sihah)؛ الفضيض الماء السائل؛ فضض الماء ما انتشر منه إذا تطهر به (tahdhib)
- **B007** dağıtıcı büyük felaket — dağıtıp perişan eden büyük felaket
  الفاضة الداهية والجمع فواض كأنها تفض أي تفرق (maqayis)؛ الفاضة الداهية (sihah)
- **B008** ilk alan olup el değmemiş durumunu sona erdirmek — bir şeyi ilk alan olup el değmemiş durumunu sona erdirmek · kadın kölesiyle ilk kez cinsel ilişkiye girmek · bekleme süresinde mahrem yerini bezle silip bezi atmak
  افتضضته أي كنت أول من أخذ منه كما يفتض الرجل المرأة (ayn)؛ افتض فلان جاريته واقتضها إذا افترعها (tahdhib)؛ تفتض بها؛ وهو من فضضت الشيء أي كسرته (tahdhib)

## ت ر ك (root_000180): 62:11 وَتَرَكُوكَ

- **B001** bir seyden el cekme — bir seyi birakma ve ondan el cekme · hicbir sey birakmadi
  الترك ودعك الشيء تتركه (ayn;tahdhib)؛ تركت الشيء تركا خليته (sihah)؛ ترك الشيء رفضه قصدا واختيارا أو قهرا واضطرارا (mufradat)؛ الترك التخلية عن الشيء وهو قياس الباب (maqayis)؛ ما أترك أي ما ترك شيئا (sihah)
- **B002** geride iz birakma — arkada iz veya sey birakma
  الترك الإبقاء وتركنا عليه أي أبقينا عليه ذكرا حسنا (tahdhib)؛ ومن الثاني كم تركوا من جنات (mufradat)
- **B003** belirtilen halde bırakma [kalıp] — birini veya seyi belirtilen halde birakmak
  الترك الجعل في بعض الكلام تقول تركت الحبل شديدا أي جعلته (ayn;tahdhib)؛ قد يقال في كل فعل ينتهي به إلى حالة ما تركته كذا أو يجري مجرى جعلته كذا نحو تركت فلانا وحيدا (mufradat)؛ يقال تركت الحبل شديدا أي جعلته شديدا وما أحسب هذا من كلام الخليل (maqayis)
- **B004** bırak buyruğu sözü — birak anlaminda buyruk sozu
  تراك بمعنى اترك وهو اسم لفعل الأمر (sihah)؛ وتراك بمعنى أترك (maqayis)
- **B005** karsilikli cekilme [kalıp] — satisi karsilikli olarak birakmak
  تاركته البيع متاركة (sihah)؛ فاركت صاحبي مثل تاركته فهذا من باب الإبدال (maqayis-ibdal)
- **B006** ölenin ardinda kalani — olen kisinin ardinda kalan mal
  تركة الميت تراثه المتروك (sihah)؛ تركة فلان لما يخلفه بعد موته (mufradat)؛ تركه الميت ما يتركه من تراثه (maqayis)
- **B007** evlenmeden birakilan kadin — evlenmeden birakilan kadin · evlenmeden birakilmis kadinla evlenmek
  التريكة من النساء التي تترك فلا يتزوجها أحد (sihah)؛ ترك الرجل إذا تزوج بالتريكة وهي العانس في بيت أبويها (tahdhib)؛ امرأة تريكة وهي التي تترك فلا تتزوج (tahdhib)
- **B008** birakilmis deve kusu yumurtasi — bozkirda birakilmis deve kusu yumurtasi · deve kusu yumurtasi · yumurtaya benzetilen demir baslik
  الترك ضرب من البيض مستدير شبيه بالتركة والتركية وهي بيض النعام (ayn)؛ التريكة بيضة النعام التي تتركها والتركة البيضة من الحديد والجمع ترك (sihah)؛ الترك البيض للرأس واحدته تركة (tahdhib)؛ التريكة أصله البيض المتروك في مفازته ويسمى بيضة الحديد بها (mufradat)؛ تسمى البيضة بالعراء تريكة وتركه السلاح وهي البيضة محمول على هذا ومشبه به (maqayis)
- **B009** geride kalmis su veya cayir — selden geriye durgun kalan su · insanlarin otlatmadan biraktigi cayirlik
  التريكة ماء يمضي عنه السيل ويتركه ناقعا (ayn)؛ التريكة روضة يغفلها الناس فلا يرعونها (sihah;maqayis)
- **B010** insan toplulugu adi — bir insan toplulugu
  الترك جيل من الناس (ayn)؛ الترك جبل من الناس (sihah)

## ع ن د (root_001052): 62:11 عِندَ

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

## ر ز ق (root_000560): 62:11 ٱلرَّٰزِقِينَ

- **B001** yararlanılmak üzere verilen pay — yararlanılan pay veya sağlanan geçimlik · Tanrı ona yararlanacağı bir pay verdi · kendisine bilgi verildi · yararı sağlayan veya ulaşmasına aracılık eden · bütün varlıklara sürekli geçim payı sağlayan Tanrı için özel niteleme
  أصيل واحد يدل على عطاء لوقت ثم يحمل عليه غير الموقوت (maqayis)؛ الرزق عطاء الله (maqayis)؛ رزق الله يرزق العباد رزقا اعتمدوا عليه (ayn)؛ الرزق ما ينتفع به والرزق العطاء (sihah)؛ الرزق معروف (tahdhib)؛ الرزق يقال للعطاء الجاري وللنصيب (mufradat)؛ الرازق يقال لخالق الرزق ومعطيه والمسبب له والرزاق لا يقال إلا لله تعالى (mufradat)
- **B002** yenip beslenilen yiyecek — yenip bedeni besleyen yiyecek
  وجد عندها رزقا عنبا في غير حينه (tahdhib)؛ لما يصل إلى الجوف ويتغذى به (mufradat)؛ فليأتكم برزق منه أي بطعام يتغذى به (mufradat)؛ عني به الأغذية (mufradat)
- **B003** yağmur — yağmur; gökten inerek canlılığı sürdüren su
  وقد يسمى المطر رزقا (sihah)؛ في السماء رزقكم قال المطر (tahdhib)؛ في السماء رزقكم قيل عني به المطر الذي به حياة الحيوان (mufradat)
- **B004** asker ödeneği — yönetici askerlere ödeneklerini verdi · askerlere tek seferde verilen ödeme · askerler ödeneklerini aldı
  إذا أخذ الجند أرزاقهم قيل ارتزقوا رزقة واحدة (ayn)؛ الرزقة بالفتح المرة الواحدة وهي أطماع الجند وارتزق الجند أي أخذوا أرزاقهم (sihah)؛ رزق الأمير جنده فارتزقوا ارتزاقا (tahdhib)؛ رزق الجند رزقة واحدة ورزقوا رزقتين (tahdhib)؛ ارتزق الجند أخذوا أرزاقهم والرزقة ما يعطونه دفعة واحدة (mufradat)
- **B005** iyiliğe gönül borcunu bildirme — size verilen iyiliğe karşılık yalanlamayı seçiyorsunuz · bana yaptığım iyilik için gönül borcunu bildirdin
  الرزق بلغة أزدشنوءة الشكر (maqayis)؛ فعلت ذلك لما رزقتني أي لما شكرتني (maqayis)؛ وتجعلون رزقكم أنكم تكذبون أي شكر رزقكم (sihah)؛ تجعلون شكر رزقكم التكذيب (tahdhib)؛ تجعلون نصيبكم من النعمة تحري الكذب (mufradat)
- **B006** iyi talih sahibi olma — talihli; payına iyi sonuçlar düşen
  رجل مرزوق أي مجدود (sihah)؛ تنبيه أن الحظوظ بالمقادير (mufradat)
- **B007** biçime bağlı adlandırmalar — beyaz keten giysiler · belirli bir üzüm çeşidi
  الرازقية ثياب كتان بيض (sihah)؛ الرازقية ثياب كتان بيض (tahdhib)؛ الرازقي من الأعناب هو الملاحي (tahdhib)



===== _commentary/v16/work/s062/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s062/reader_a_pilot.md)

# s062 Semantic Channel Discovery

## Parent Channels

### 1. Guidance as Route and Relay
- Semantic invariant: Direction is preserved by a marked course and an ordered succession in which what comes later can follow, advance, and catch what went before.
- Surface relation: direct; 62:2 places signs, teaching, and manifest straying in one transformation, 62:3 names those who have not yet caught up, 62:5 names guidance, and 62:9 commands purposeful movement toward prayer.
- Surprising reach: Guidance becomes road infrastructure and then a race or relay, making later inclusion an act of oriented catch-up rather than belated imitation.

#### Subchannel A. The Marked Road Out of Error
- Reading type: mixed
- Scene or process: A traversable road is made legible by signs and waymarks; a guide supplies its direction, while error is departure from its intended course.
- Active motifs: visible sign (`quranic:root_000074:B003/m01`); distinguishing waymark (`quranic:root_001040:B002/m01`); gentle guidance to road and truth (`quranic:root_001583:B001/m01`); direction and manner of proceeding (`quranic:root_001583:B002/m01`); straying from course (`quranic:root_000913:B001/m01`); inhabited thoroughfare and junction (`quranic:root_000009:B010/m01`); worked, well-trodden road (`quranic:root_001046:B011/m01`); clear road over easy ground (`quranic:root_001464:B007/m01`).
- Ayah anchors: 62:2 `ءَايَٰتِ`, `يُعَلِّمُ`, `ضَلَٰلٍ`; 62:4 `يُؤْتِي`; 62:5 `ـَٔايَٰتِ`, `يَهْدِى`; 62:8 `عَٰلِمِ`, `تَعْمَلُ`, `يُنَبِّئُ`; 62:9 `تَعْلَمُ`.
- Synthesis: The signs function as external waymarks rather than detached propositions. They distinguish a worked and passable road, teaching makes that road knowable, and guidance supplies its heading. Manifest error is correspondingly spatialized as leaving the course, while the clear road promises arrival rather than mere possession of directions.

#### Subchannel B. The Later Runner Catches the Lead
- Reading type: mixed
- Scene or process: A leading member sets the line; successive groups follow, the second runner stays at the leader's flank, and a later participant closes the gap.
- Active motifs: later or other after the first (`quranic:root_000019:B001/m01`); following in sequence (`quranic:root_000186:B001/m01`); successive groups (`quranic:root_000563:B005/m01`); second horse following the winner (`quranic:root_000879:B006/m01`); catching what is ahead (`quranic:root_001347:B001/m01`); forward advance and precedence (`quranic:root_001207:B004/m01`); leading front of a moving group (`quranic:root_001583:B003/m01`); animal leader followed by the rest (`quranic:root_001444:B008/m01`); purposeful rapid movement (`quranic:root_000709:B001/m01`).
- Ayah anchors: 62:1 `مَلِكِ`; 62:2 `يَتْلُوا۟`, `رَسُولًا`; 62:3 `ءَاخَرِينَ`, `يَلْحَقُ`; 62:5 `يَهْدِى`; 62:7 `قَدَّمَتْ`; 62:9 `ٱسْعَ`, `صَّلَوٰةِ`.
- Synthesis: The later group is not static at the rear. Following, advancing, and catching form one relay scene, with the lexical image of prayer as the second racehorse fixing disciplined proximity to the leader. The mission thus extends by ordered succession: a front is established, the next group enters its line, and distance can be overcome without erasing sequence.

### 2. Message in Voice and Record
- Semantic invariant: A message crosses distance and persists through a chain that bears it, externalizes it in voice or record, makes it legible, and receives it into assent.
- Surface relation: direct; 62:2 joins messenger, recitation, signs, teaching, and book, 62:5 names scrolls, 62:8 promises a report, and 62:9 joins the raised call with remembrance.
- Surprising reach: Recitation and scripture expand into a complete transmission system: dispatched bearer, responsive voice, crafted record, lifted cover, and receptive uptake.

#### Subchannel A. Call and Responsive Voice
- Reading type: mixed
- Scene or process: A low sound is raised into a far-reaching call; one voice follows another through correspondence, and tongue-borne remembrance becomes audible witness.
- Active motifs: voice following voice (`quranic:root_000186:B007/m01`); correspondence and paired performance (`quranic:root_000563:B008/m01`); faint, ambiguous sound (`quranic:root_001464:B006/m01`); raised call with extended range (`quranic:root_001486:B002/m01`); remembrance moving on the tongue (`quranic:root_000516:B004/m01`); tongue as instrument of speech (`quranic:root_001272:B002/m01`); witnessing tongue (`quranic:root_000822:B005/m01`).
- Ayah anchors: 62:2 `يَتْلُوا۟`, `رَسُولًا`; 62:6 `قُلْ`; 62:8 `شَّهَٰدَةِ`, `يُنَبِّئُ`, `قُلْ`; 62:9 `نُودِىَ`, `ذِكْرِ`; 62:10 `ٱذْكُرُ`; 62:11 `قُلْ`.
- Synthesis: The recited message behaves as a relay rather than a solitary utterance. A voice answers or follows a prior voice, correspondence maintains the sequence, and the call gains enough range to summon a public response. Remembrance on the tongue then turns reception into renewed transmission, while the same articulator can later stand as witness.

#### Subchannel B. The Joined and Unfolded Record
- Reading type: mixed
- Scene or process: A document is constructed by joining material and ordering letters, then entered into a register, opened for reading, and retained as an instrument of right.
- Active motifs: joining and stitching material (`quranic:root_001283:B001/m01`); ordered letters and writing (`quranic:root_001283:B002/m01`); registering a name in a roll (`quranic:root_001283:B004/m01`); writing and scribal disclosure (`quranic:root_000712:B004/m02`); opened or unsealed writing (`quranic:root_001503:B009/m01`); document establishing a right (`quranic:root_000516:B008/m01`).
- Ayah anchors: 62:2 `كِتَٰبَ`; 62:5 `أَسْفَارًۢا`; 62:9 `ذِكْرِ`; 62:10 `ٱذْكُرُ`, `ٱنتَشِرُ`.
- Synthesis: The book is materially assembled before it is semantically received: pieces are joined, letters are ordered, and names are registered. Opening the record makes its content public, while its documentary function allows a right or obligation to persist beyond the moment of utterance. This sharpens the difference between access to a text and incorporation of what it fixes.

#### Subchannel C. The Dispatched Word Is Taken Up
- Reading type: mixed
- Scene or process: An envoy is directed outward bearing speech; a recipient takes and learns the words, accepts them willingly, and settles into trusting assent.
- Active motifs: dispatched envoy (`quranic:root_000129:B002/m01`); messenger as carrier of speech (`quranic:root_000563:B002/m01`); words received and taught (`quranic:root_001372:B011/m01`); willing acceptance (`quranic:root_001198:B004/m01`); heart-settled assent (`quranic:root_000054:B002/m01`).
- Ayah anchors: 62:2 `بَعَثَ`, `رَسُولًا`, `قَبْلُ`; 62:8 `مُلَٰقِي`; 62:9 `ءَامَنُ`.
- Synthesis: Dispatch does not complete transmission. The messenger bears speech across the interval, but the words must then be taken, learned, accepted, and believed. The mission therefore terminates in inward assent rather than in proximity to a messenger or possession of a record.

#### Subchannel D. Cover Lifted Into Clarity
- Reading type: latent/lexical
- Scene or process: A covering is removed, light advances like dawn, the concealed object becomes visible, and speech or sign discloses its meaning.
- Active motifs: removing a cover or obscuring layer (`quranic:root_000712:B001/m01`); dawn-like illumination (`quranic:root_000712:B002/m01`); emergence into visible clarity (`quranic:root_000170:B004/m01`); meaning disclosed by speech or sign (`quranic:root_000170:B005/m01`).
- Ayah anchors: 62:2 `مُّبِينٍ`; 62:5 `أَسْفَارًۢا`.
- Synthesis: The scroll root supplies a physical unveiling, while manifestness supplies cognitive disclosure. Removing the cover lets an object be seen; explanation makes what is seen intelligible. The paired operation pressures the loaded-scroll image: exposure of writing is still short of illumination by its meaning.

### 3. Bearing Weight and Holding Form
- Semantic invariant: Weight can be transported, guaranteed, mechanically supported, or made into the mainstay of a larger order; these are distinct forms of bearing.
- Surface relation: direct; 62:5 repeatedly names loading and carrying, with a donkey bearing scrolls, while 62:11 leaves one figure standing after the crowd departs.
- Surprising reach: The burden image develops into a complete load-bearing ecology: cargo, legal surety, pack-frame construction, and the upright support on which a whole arrangement depends.

#### Subchannel A. Cargo Without Uptake
- Reading type: mixed
- Scene or process: A pack animal transports a visible load whose documentary content remains external to the bearer, while the same load also figures an entrusted responsibility.
- Active motifs: donkey as pack animal (`quranic:root_000356:B004/m01`); visible load carried on back or mount (`quranic:root_000357:B001/m01`); entrusted burden or message (`quranic:root_000357:B003/m01`); book or scroll as carried object (`quranic:root_000712:B004/m01`).
- Ayah anchors: 62:5 `حِمَارِ`, `حُمِّلُ`, `يَحْمِلُ`, `أَسْفَارًۢا`.
- Synthesis: The animal successfully performs transport but not uptake. Physical carrying moves the scrolls, whereas entrusted carrying requires the bearer to stand under their demand. The scene therefore distinguishes successful conveyance from failed responsibility without dissolving the concrete weight of the books.

#### Subchannel B. Liability Must Be Discharged
- Reading type: latent/lexical
- Scene or process: A right follows its holder, a guarantor assumes its burden, and the obligation remains in force until payment or performance discharges it.
- Active motifs: liability or right following its owner (`quranic:root_000186:B004/m01`); compensation and surety borne for another (`quranic:root_000357:B004/m01`); guarantee and written undertaking (`quranic:root_001198:B008/m01`); discharge and collection of a due right (`quranic:root_001237:B006/m01`).
- Ayah anchors: 62:2 `يَتْلُوا۟`, `قَبْلُ`; 62:5 `حُمِّلُ`, `يَحْمِلُ`; 62:10 `قُضِيَتِ`.
- Synthesis: The entrusted text acquires the structure of a liability. Its claim follows the responsible party, surety transfers the weight without cancelling it, and only actual discharge closes the relation. This legal mechanism pressures any account of scripture that ends at possession or recitation.

#### Subchannel C. Constructing the Pack Frame
- Reading type: latent/lexical
- Scene or process: Wood is cut into saddle and upright components, padded beneath the load, and braced so that the mounted weight does not fall.
- Active motifs: wooden and stone supports called "donkey" (`quranic:root_000356:B005/m01`); carrying apparatus and mount (`quranic:root_000357:B006/m01`); saddle-frame timber (`quranic:root_001029:B009/m01`); wood cut by a saw (`quranic:root_001503:B005/m01`); pad beneath the saddle (`quranic:root_001684:B011/m01`); prop preventing collapse (`quranic:root_000555:B009/m01`); upright implement or structural leg (`quranic:root_001273:B012/m01`).
- Ayah anchors: 62:4 `عَظِيمِ`; 62:5 `حِمَارِ`, `حُمِّلُ`, `يَحْمِلُ`, `قَوْمِ`, `قَوْمَ`; 62:6 `أَوْلِيَآءُ`; 62:8 `تُرَدُّ`; 62:10 `ٱنتَشِرُ`; 62:11 `قَآئِمًا`.
- Synthesis: The lexical network supplies the hidden engineering beneath the burden. A saddle timber is sawn, a pad protects the mount, upright pieces establish the frame, and a prop keeps the assembly from collapsing. The image makes bearing a constructed relation among animal, apparatus, and load rather than a single undifferentiated act.

#### Subchannel D. The Upright Mainstay
- Reading type: mixed
- Scene or process: A durable central support holds an arrangement together and supplies the standing capacity on which its continuation depends.
- Active motifs: mainstay that supports order and livelihood (`quranic:root_001273:B009/m01`); governing mainstay of an affair (`quranic:root_001444:B005/m01`); remaining in place without departure (`quranic:root_000004:B006/m01`).
- Ayah anchors: 62:1 `مَلِكِ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:7 `أَبَدًۢا`; 62:11 `قَآئِمًا`.
- Synthesis: Standing is not merely posture here but structural function. The mainstay gives an affair coherence and allows dependent parts to remain ordered around it. Against the pack animal that bears an external load, the standing center embodies the support the departing group fails to provide.

### 4. Assembly and Dispersal
- Semantic invariant: A collective is defined by how separate bodies are gathered around a time and place, released after completion, or broken apart before the center has ceased to stand.
- Surface relation: direct; 62:9 names the gathering day and call, 62:10 authorizes dispersal after prayer is completed, and 62:11 depicts a crowd breaking away and leaving its standing center.
- Surprising reach: The surah's movements distinguish orderly release from fracture: both scatter bodies, but only one follows completion and preserves the governing relation.

#### Subchannel A. Constituting the Congregation
- Reading type: mixed
- Scene or process: Dispersed persons are gathered at a designated day and place, become present to one another, and form a public forum.
- Active motifs: joining what was dispersed (`quranic:root_000259:B001/m01`); day, place, or summons that gathers (`quranic:root_000259:B004/m01`); public forum and council (`quranic:root_001486:B001/m01`); place of standing or assembled residence (`quranic:root_001273:B006/m01`); presence and witnessed gathering (`quranic:root_000822:B001/m01`); bounded day (`quranic:root_001700:B001/m01`).
- Ayah anchors: 62:5 `قَوْمِ`, `قَوْمَ`; 62:8 `شَّهَٰدَةِ`; 62:9 `جُمُعَةِ`, `نُودِىَ`, `يَوْمِ`; 62:11 `قَآئِمًا`.
- Synthesis: A congregation is produced by convergence, not assumed as a pre-existing mass. Time, location, summons, and bodily presence cooperate to turn scattered people into a forum. The gathering day is therefore an operation that constitutes a public around a standing place.

#### Subchannel B. Release After Completion
- Reading type: surface-primary
- Scene or process: A bounded rite reaches completion, after which the gathered body is deliberately released to spread across terrain.
- Active motifs: completion and release from a finished act (`quranic:root_001237:B004/m01`); people opening out and spreading (`quranic:root_001503:B001/m01`); imperative release or leaving (`quranic:root_001638:B003/m01`).
- Ayah anchors: 62:9 `ذَرُ`; 62:10 `قُضِيَتِ`, `ٱنتَشِرُ`.
- Synthesis: This dispersal is licensed by sequence: completion first, spreading second. The collective opens into the land without becoming a broken collective, because its release observes the boundary of the rite. Movement away from the place can thus preserve rather than negate the relation formed there.

#### Subchannel C. Fracture and Abandonment
- Reading type: mixed
- Scene or process: Attraction elsewhere breaks a gathered body into detached pieces, abandons the standing center, and leaves the former place socially empty.
- Active motifs: breaking by separating parts (`quranic:root_001162:B001/m01`); crowd dispersing after assembly (`quranic:root_001162:B002/m01`); detached fragments (`quranic:root_001162:B004/m01`); deliberate abandonment (`quranic:root_000180:B001/m01`); distraction that turns one away (`quranic:root_001382:B001/m01`); bodily standing (`quranic:root_001273:B002/m01`); deserted dwelling after its people leave (`quranic:root_000004:B003/m01`).
- Ayah anchors: 62:5 `قَوْمِ`, `قَوْمَ`; 62:7 `أَبَدًۢا`; 62:11 `ٱنفَضُّ`, `تَرَكُ`, `لَهْوًا`, `لَّهْوِ`, `قَآئِمًا`.
- Synthesis: The crowd does not simply relocate; it fractures. Breaking, detached pieces, distraction, and abandonment form a causal sequence whose outcome is an empty social space with one figure still upright. This differs from post-prayer release because the dispersal is organized by a rival attraction rather than by fulfilled completion.

### 5. Purification Opens Into Growth
- Semantic invariant: Removal of defilement and increase are two phases of making life fit to flourish, joined by the same root of purification and growth and materialized through managed water.
- Surface relation: direct; 62:1 names the Holy and cosmic praise, 62:2 names purification, and 62:10 joins earthly seeking with flourishing.
- Surprising reach: Moral purification becomes hydraulic and agricultural: channel, bucket, basin, cloud, rain, fertile ground, and cultivation form a continuous life-making system.

#### Subchannel A. Cleansing Waterworks
- Reading type: mixed
- Scene or process: Water is routed into a basin, measured at its edge, lifted in a cleansing vessel, and applied to remove impurity.
- Active motifs: purity and cleansing (`quranic:root_001206:B001/m01`); bucket used for purification (`quranic:root_001206:B005/m01`); basin stone marking the water point (`quranic:root_001206:B010/m01`); directed watercourse (`quranic:root_000009:B004/m01`); fresh running water (`quranic:root_001162:B006/m01`); purification and moral fitness (`quranic:root_000637:B002/m01`); transcendence and clearing from defect (`quranic:root_000666:B002/m01`); abundant collected water (`quranic:root_001040:B005/m01`).
- Ayah anchors: 62:1 `قُدُّوسِ`, `يُسَبِّحُ`; 62:2 `يُزَكِّي`, `يُعَلِّمُ`; 62:4 `يُؤْتِي`; 62:7 `عَلِيمٌۢ`; 62:8 `عَٰلِمِ`; 62:9 `تَعْلَمُ`; 62:11 `ٱنفَضُّ`.
- Synthesis: Purification is rendered as a controlled water operation. A channel supplies flow, a basin receives it, a stone fixes the watering point, and a bucket makes the water usable for cleansing. Transcendence removes attributed defect while purification makes the recipient fit, so holiness is presented as active maintenance rather than sterile separation.

#### Subchannel B. Rain Becomes Harvest
- Reading type: latent/lexical
- Scene or process: A water-bearing cloud releases provision onto fertile ground; dry pasture revives, growth appears, and a cultivator opens the soil toward a flourishing outcome.
- Active motifs: cloud bearing water (`quranic:root_000357:B010/m01`); rain descending as provision (`quranic:root_000560:B003/m01`); soft fertile ground (`quranic:root_000025:B002/m01`); dry pasture revived by rain (`quranic:root_001503:B004/m01`); growth and increase (`quranic:root_000637:B001/m01`); yield and emerging produce (`quranic:root_000009:B007/m01`); cultivator splitting earth for seed (`quranic:root_001175:B003/m01`); flourishing, survival, and attained good (`quranic:root_001175:B005/m01`).
- Ayah anchors: 62:1 `أَرْضِ`; 62:2 `يُزَكِّي`; 62:4 `يُؤْتِي`; 62:5 `حُمِّلُ`, `يَحْمِلُ`; 62:10 `أَرْضِ`, `ٱنتَشِرُ`, `تُفْلِحُ`; 62:11 `رَّٰزِقِينَ`.
- Synthesis: Increase is not an isolated abundance term but the outcome of a causal ecology. Water is carried, descends as provision, revives dormant pasture, and enables cultivated earth to yield. The same lexical field that purifies persons thus also describes the conditions under which land becomes productive.

### 6. Competing Economies of Value
- Semantic invariant: Value is first perceived and chosen, then either negotiated through exchange and price or received as allotted and surplus benefaction; these economies compete for practical allegiance.
- Surface relation: direct; 62:4 identifies divine favor as a gift, 62:9 suspends sale, 62:10 commands seeking divine favor, and 62:11 contrasts trade with what is with God and names the Provider.
- Surprising reach: The market is not a generic temptation but a complete transactional mechanism, and even before price the seeing eye must convert display into wise comparison with provision and unowed excess.

#### Subchannel A. Market Price and Turnover
- Reading type: mixed
- Scene or process: Goods are displayed, assessed, exchanged for price, transferred or rescinded, and promoted within a market whose activity can rise.
- Active motifs: trade for profit (`quranic:root_000176:B001/m01`); skill in a mode of earning (`quranic:root_000176:B004/m01`); exchange for a price (`quranic:root_000169:B001/m01`); offering goods for sale (`quranic:root_000169:B002/m01`); valuation and pricing (`quranic:root_001273:B010/m01`); a market becoming active (`quranic:root_001273:B018/m01`); transfer at a known price (`quranic:root_001684:B014/m01`); rescission and return of goods (`quranic:root_000555:B004/m01`); deceptive embellishment of a sale (`quranic:root_001175:B007/m01`).
- Ayah anchors: 62:5 `قَوْمِ`, `قَوْمَ`; 62:6 `أَوْلِيَآءُ`; 62:8 `تُرَدُّ`; 62:9 `بَيْعَ`; 62:10 `تُفْلِحُ`; 62:11 `تِجَٰرَةً`, `تِّجَٰرَةِ`, `قَآئِمًا`.
- Synthesis: The rival attraction is a functioning market: display elicits assessment, price permits transfer, turnover animates the market, and rescission remains possible. The branch of deceptive salesmanship adds pressure to visible commercial appeal, showing how apparent advantage can be manufactured rather than discovered.

#### Subchannel B. Allotted Provision and Surplus Gift
- Reading type: mixed
- Scene or process: A giver assigns a sustaining share and then exceeds strict allocation through generosity, benefaction, and a hand extended in favor.
- Active motifs: giving and bestowal (`quranic:root_000009:B002/m01`); remainder and excess beyond need (`quranic:root_001163:B001/m01`); unowed benefaction (`quranic:root_001163:B003/m01`); generosity and gift (`quranic:root_000452:B005/m01`); allotted provision (`quranic:root_000560:B001/m01`); beneficent hand (`quranic:root_001693:B003/m01`); blessing and good condition (`quranic:root_000053:B010/m01`).
- Ayah anchors: 62:2 `أُمِّيِّۦنَ`; 62:4 `يُؤْتِي`, `فَضْلُ`, `فَضْلِ`; 62:7 `أَيْدِي`; 62:9 `خَيْرٌ`; 62:10 `فَضْلِ`; 62:11 `خَيْرٌ`, `خَيْرُ`, `رَّٰزِقِينَ`.
- Synthesis: Provision contains both measure and overflow. The allotted share sustains, while favor is explicitly surplus, a remainder not owed by exchange. Generosity and the beneficent hand therefore recast "better" as a different mode of value, not merely a larger quantity of the same market good.

#### Subchannel C. The Eye Must Judge What Is Better
- Reading type: mixed
- Scene or process: The eye receives a display, inward sight reflects on it, wisdom judges, and choice distinguishes the better object; this process can fail while the eye remains outwardly intact.
- Active motifs: visual perception (`quranic:root_000531:B001/m01`); inward insight (`quranic:root_000531:B001/m02`); deliberative judgment (`quranic:root_000531:B002/m01`); wisdom as accurate knowledge (`quranic:root_000348:B003/m01`); choosing what is better (`quranic:root_000452:B003/m01`); intact but sightless eye (`quranic:root_001273:B021/m01`).
- Ayah anchors: 62:1 `حَكِيمِ`; 62:2 `حِكْمَةَ`; 62:3 `حَكِيمُ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:9 `خَيْرٌ`; 62:11 `رَأَ`, `خَيْرٌ`, `خَيْرُ`, `قَآئِمًا`.
- Synthesis: Seeing merchandise is only the first stage of valuation. Sensory sight must pass into reflection, wisdom, and comparative choice before it can recognize what is better. The image of an eye whose globe still stands after sight has departed materializes the failure in 62:11: visible trade is registered, but the superior value is not discerned.

### 7. Belonging by Center, Attachment, and Patronage
- Semantic invariant: Belonging is produced through orientation to a shared center, attachment of those previously outside, and relations of proximity and support.
- Surface relation: direct; 62:2 names the unlettered community and a messenger from among them, 62:3 extends the group to others who have not joined, 62:5 addresses a people, and 62:6 tests an exclusive claim to divine patronage.
- Surprising reach: Community is not confined to inherited identity: lexical outsiders, uncertain lineages, attached claimants, neighbors, clients, and allies expose several mechanisms by which a boundary can open or harden.

#### Subchannel A. Community Around Center, Path, and Leader
- Reading type: mixed
- Scene or process: A collective gathers around an origin or center, shares a way, and follows an exemplary figure who can stand for the group.
- Active motifs: origin, center, and gathering reference (`quranic:root_000053:B002/m01`); community or kind (`quranic:root_000053:B004/m01`); community as religion and followed way (`quranic:root_000053:B005/m01`); exemplar and leader (`quranic:root_000053:B009/m01`); people as a social body (`quranic:root_001273:B001/m01`); mixed company gathered by one direction (`quranic:root_000259:B002/m01`); unlettered person outside scribal practice (`quranic:root_000053:B007/m01`).
- Ayah anchors: 62:2 `أُمِّيِّۦنَ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:9 `جُمُعَةِ`; 62:11 `قَآئِمًا`.
- Synthesis: The community is organized by more than descent. A center gathers, a way supplies common orientation, and an exemplar can represent the whole. The unlettered condition places this social formation before scribal possession, allowing recitation and teaching to constitute a community around a transmitted direction.

#### Subchannel B. The Stranger Becomes Attached
- Reading type: latent/lexical
- Scene or process: A foreign entrant crosses into another people, passes through uncertain or carried affiliation, and is attached through kinship, clientage, or neighborhood.
- Active motifs: stranger entering a people not his own (`quranic:root_000009:B006/m01`); stranger as "son of the land" (`quranic:root_000025:B004/m01`); carried outsider or child of uncertain lineage (`quranic:root_000357:B005/m01`); person appended to a people or lineage (`quranic:root_001347:B002/m01`); affiliation through kinship, emancipation, or neighborhood (`quranic:root_001684:B005/m01`).
- Ayah anchors: 62:1 `أَرْضِ`; 62:3 `يَلْحَقُ`; 62:4 `يُؤْتِي`; 62:5 `حُمِّلُ`, `يَحْمِلُ`; 62:6 `أَوْلِيَآءُ`; 62:10 `أَرْضِ`.
- Synthesis: Inclusion appears as a social operation on an outsider. Entry, carrying, attachment, and clientage are successive ways of crossing a boundary that descent alone does not settle. The scene gives concrete social force to later persons joining an already formed mission.

#### Subchannel C. Exclusive Patronage Under Pressure
- Reading type: mixed
- Scene or process: A group claims immediate proximity and protective alliance while placing others outside; return to truth tests whether inherited identity actually sustains that relation.
- Active motifs: nearness without an intervening gap (`quranic:root_001684:B001/m01`); alliance, love, and support (`quranic:root_001684:B004/m01`); Jewish identity and adopted tradition (`quranic:root_001605:B002/m01`); return and repentance toward truth (`quranic:root_001605:B001/m01`); the other, excluded, or lower-ranked party (`quranic:root_000502:B003/m01`).
- Ayah anchors: 62:6 `هَادُ`, `أَوْلِيَآءُ`, `دُونِ`.
- Synthesis: Patronage combines closeness and active support, so an exclusive claim must establish more than a group name. The counter-sense of return makes affiliation directional: identity is validated by movement toward truth, not by placing the rest of humanity on the far side of a verbal boundary.

### 8. Speech Bound to Performance
- Semantic invariant: A meaning-bearing form is accountable to what it produces or truthfully manifests: declarations to action, parables to remembered conduct, and visible performances to underlying reality.
- Surface relation: direct; 62:5 gives a parable and names denial, 62:6 frames an asserted privilege as a conditional truth claim and commands a wish for death, 62:7 exposes refusal to perform that speech, and 62:11 makes a seen display practically decisive.
- Surprising reach: Claim, oath, and hand-pledge test whether words bear consequences; the parable must become a remembered pattern, while cloth and posture show how an outward performance can counterfeit truth.

#### Subchannel A. The Claim Is Tested by Enactment
- Reading type: mixed
- Scene or process: An uncertain assertion is opposed to truthful speech, and truth is determined by whether the speaker realizes the declared commitment in action.
- Active motifs: assertion made without certainty (`quranic:root_000633:B001/m01`); truthful speech (`quranic:root_000852:B001/m01`); fulfillment of promise or claim by action (`quranic:root_000852:B004/m01`); falsehood opposed to truth (`quranic:root_001290:B001/m01`); attribution of falsity (`quranic:root_001290:B002/m01`); desired image formed in the mind (`quranic:root_001450:B004/m01`); fabricated wish or story without reality (`quranic:root_001450:B013/m01`); words falsely attributed to another (`quranic:root_001272:B005/m01`).
- Ayah anchors: 62:5 `كَذَّبُ`; 62:6 `قُلْ`, `زَعَمْ`, `تَمَنَّ`, `صَٰدِقِينَ`; 62:7 `يَتَمَنَّ`; 62:8 `قُلْ`; 62:11 `قُلْ`.
- Synthesis: The speech moves from assertion to ordeal. A claim may remain an imagined or fabricated verbal object, but truthful speech must be realized by a corresponding act. The commanded wish makes performance the diagnostic hinge: refusal reveals the distance between asserted status and enacted commitment.

#### Subchannel B. The Oath and Hand-Pledge
- Reading type: latent/lexical
- Scene or process: The divine name and oath particle introduce a binding pledge, backed by a guarantor, a submitted hand, and the trust that makes reliance possible.
- Active motifs: divine name used in oath or address (`quranic:root_000047:B002/m01`); particle opening an oath (`quranic:root_000074:B010/m01`); oath and sworn pledge (`quranic:root_000076:B007/m01`); assuming surety (`quranic:root_000633:B003/m01`); hand given as pledge or submission (`quranic:root_001693:B006/m01`); security, trust, and entrusted property (`quranic:root_000054:B001/m01`).
- Ayah anchors: 62:1 `لَّهِ`; 62:2 `ءَايَٰتِ`; 62:4 `ٱللَّهِ`, `ٱللَّهُ`; 62:5 `ـَٔايَٰتِ`, `ٱللَّهِ`, `ٱللَّهُ`; 62:6 `زَعَمْ`, `لَّهِ`; 62:7 `أَيْدِي`, `ٱللَّهُ`; 62:9 `ءَامَنُ`, `ٱللَّهِ`; 62:10 `ٱللَّهِ`, `ٱللَّهَ`; 62:11 `ٱللَّهِ`, `ٱللَّهُ`. Ayah anchor unavailable for `quranic:root_000076:B007/m01` because root `ء ل ي` is listed in `missing_roots`.
- Synthesis: The exclusive claim is lexically pressured into the form of a pledge. Invocation, oath marker, sworn commitment, surety, and hand-pledge create a complete binding speech act whose credibility depends on trust. The claim to special alliance thereby carries oath-like liability once its consequence is demanded.

#### Subchannel C. The Parable Must Become a Pattern
- Reading type: mixed
- Scene or process: A spoken parable presents a warning, restores it to mind, lodges it in memory, and supplies a pattern for conduct; loss of retention interrupts the process.
- Active motifs: spoken parable (`quranic:root_001397:B003/m01`); parable as warning and sign (`quranic:root_001397:B011/m01`); reminder that restores presence (`quranic:root_000516:B009/m01`); retention and recollection (`quranic:root_000516:B003/m01`); imitation and enacted conformity (`quranic:root_001397:B010/m01`); loss of retention (`quranic:root_000913:B004/m01`).
- Ayah anchors: 62:2 `ضَلَٰلٍ`; 62:5 `مَثَلُ`, `مَثَلِ`; 62:9 `ذِكْرِ`; 62:10 `ٱذْكُرُ`.
- Synthesis: The donkey image is not exhausted by resemblance. As a struck parable it is designed to warn, return the demand to memory, and provide a pattern against which conduct can be conformed. Forgetting breaks that conversion, leaving the example as externally borne information rather than remembered instruction.

#### Subchannel D. Counterfeit Display
- Reading type: latent/lexical
- Scene or process: An outward surface or posture is arranged for observers, yet the display can falsify the condition beneath it and imitate a surrender that has not occurred.
- Active motifs: outward appearance and facial sign (`quranic:root_000531:B006/m01`); ostentation performed for observers (`quranic:root_000531:B005/m01`); patterned cloth that lies about its condition (`quranic:root_001290:B009/m01`); feigned death or humility (`quranic:root_001454:B011/m01`).
- Ayah anchors: 62:5 `كَذَّبُ`; 62:6 `مَوْتَ`; 62:8 `مَوْتَ`; 62:11 `رَأَ`.
- Synthesis: Visibility does not authenticate what it presents. A polished appearance can be staged for the gaze, a decorated garment can misreport its state, and a submissive posture can be feigned. The scene pressures both carried scripture and claimed privilege: outward resemblance to fidelity may itself become a false statement.

### 9. Flight, Return, and Disclosure
- Semantic invariant: Avoidance cannot dissolve the relation to truth: the fugitive is compelled back into disclosure, while a non-fugitive can relinquish resistance and yield before the encounter.
- Surface relation: direct; 62:7 attributes refusal to what hands have advanced, and 62:8 joins flight from death, unavoidable meeting, return, unseen and witnessed reality, report, and action.
- Surprising reach: Eschatological return is staged as pursuit, courtroom disclosure, and renewed standing, while the death root also opens a voluntary route of wholehearted submission to truth.

#### Subchannel A. Flight Meets What It Flees
- Reading type: surface-primary
- Scene or process: A fugitive turns away from death but enters a face-to-face convergence in which the avoided object approaches from the opposing direction.
- Active motifs: loss of life-force (`quranic:root_001454:B001/m01`); escape and flight (`quranic:root_001142:B001/m01`); meeting of opposing parties (`quranic:root_001372:B004/m01`); face-to-face encounter (`quranic:root_001198:B001/m01`).
- Ayah anchors: 62:2 `قَبْلُ`; 62:6 `مَوْتَ`; 62:8 `مَوْتَ`, `تَفِرُّ`, `مُلَٰقِي`.
- Synthesis: Flight and meeting are inverse motions in one scene. The fugitive attempts to increase distance, but the object of flight is itself represented as an approaching counterpart. Escape therefore changes neither destination nor relation; it converts avoidance into an eventual confrontation.

#### Subchannel B. Return Into Full Exposure
- Reading type: mixed
- Scene or process: A person is returned before complete knowledge, where hidden and present realities converge, testimony states what is known, and intentional acts become a delivered report.
- Active motifs: return to source or former jurisdiction (`quranic:root_000555:B001/m01`); what is concealed from sight (`quranic:root_001117:B001/m01`); presence with direct witnessing (`quranic:root_000822:B001/m02`); testimony that declares knowledge (`quranic:root_000822:B002/m01`); disclosed knowledge (`quranic:root_001040:B001/m01`); consequential report delivered to its recipient (`quranic:root_001464:B002/m01`); intentional deed (`quranic:root_001046:B001/m01`); deed attributed to the hands (`quranic:root_001693:B009/m01`); prior deed and established precedent (`quranic:root_001207:B002/m01`).
- Ayah anchors: 62:2 `يُعَلِّمُ`; 62:7 `قَدَّمَتْ`, `أَيْدِي`, `عَلِيمٌۢ`; 62:8 `تُرَدُّ`, `غَيْبِ`, `شَّهَٰدَةِ`, `عَٰلِمِ`, `يُنَبِّئُ`, `تَعْمَلُ`; 62:9 `تَعْلَمُ`.
- Synthesis: Return collapses the protective distance between hidden act and public evidence. What was absent from ordinary sight enters the same knowing field as what was witnessed; testimony articulates it, the report delivers it, and the hands identify agency. Deeds have already established a precedent before the speaker reaches the scene of disclosure.

#### Subchannel C. Death Decree and Re-Standing
- Reading type: latent/lexical
- Scene or process: Death is fixed as an executable determination, yet the stilled body is awakened, revived, and made to stand again.
- Active motifs: fated death (`quranic:root_001450:B003/m01`); death as an executed judgment (`quranic:root_001237:B003/m01`); stirring what was still or asleep (`quranic:root_000129:B001/m01`); revival after death (`quranic:root_001503:B002/m01`); resurrection and standing of creation (`quranic:root_001273:B013/m01`).
- Ayah anchors: 62:2 `بَعَثَ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:6 `مَوْتَ`, `تَمَنَّ`; 62:7 `يَتَمَنَّ`; 62:8 `مَوْتَ`; 62:10 `قُضِيَتِ`, `ٱنتَشِرُ`; 62:11 `قَآئِمًا`.
- Synthesis: The mortality branches first close life through a decree that reaches execution. The motion then reverses: stillness is stirred, death is opened into revival, and creation stands. This preserves both inevitabilities in 62:8, the certainty of death and the certainty that return is not mere extinction.

#### Subchannel D. The Non-Fugitive Yields
- Reading type: latent/lexical
- Scene or process: A person releases self-protective resistance, becomes willing to face death, submits to truth, and settles into humble yielding.
- Active motifs: wholehearted surrender without fear of death (`quranic:root_001454:B010/m01`); submission to truth (`quranic:root_001454:B013/m01`); humble submission (`quranic:root_001332:B004/m01`).
- Ayah anchors: 62:2 `كَانُ`; 62:6 `كُن`, `مَوْتَ`; 62:8 `كُن`, `مَوْتَ`; 62:9 `كُن`.
- Synthesis: The same lexical field that names the object of flight also names the end of resistance. Wholehearted surrender removes the fugitive posture, submission directs that surrender toward truth, and humble yielding gives it a settled form. The death challenge can thus pressure the claim not only through feared mortality but through willingness to relinquish the self-protective claim.

### 10. Authority That Holds and Redirects
- Semantic invariant: Effective authority receives grievance, adjudicates conflict, restrains deviation, and converts measured judgment into an order that actually takes effect.
- Surface relation: direct; 62:1 names King, Mighty, and Wise, 62:2-3 repeat wisdom and might, 62:5-7 join guidance, wrongdoing, and divine knowledge, and 62:8 names return to the Knower.
- Surprising reach: Wisdom is materialized as arbitration and bridle, sovereignty as a supporting hand and mainstay, and decree as fabrication whose precision makes an intended form hold.

#### Subchannel A. Sovereignty and Guardianship
- Reading type: mixed
- Scene or process: A sovereign possesses governing force, delegates care, judges among people, and maintains the affairs for which the governing hand is responsible.
- Active motifs: kingship and sovereign rule (`quranic:root_001444:B003/m01`); judgment between people (`quranic:root_000348:B002/m01`); care, preservation, and governance (`quranic:root_001273:B004/m01`); assuming an office or guardianship (`quranic:root_001684:B003/m01`); hand as effective authority (`quranic:root_001693:B005/m01`); might and inviolable strength (`quranic:root_001008:B001/m01`).
- Ayah anchors: 62:1 `مَلِكِ`, `حَكِيمِ`, `عَزِيزِ`; 62:2 `حِكْمَةَ`; 62:3 `حَكِيمُ`, `عَزِيزُ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:6 `أَوْلِيَآءُ`; 62:7 `أَيْدِي`; 62:11 `قَآئِمًا`.
- Synthesis: Sovereignty is a practiced office rather than a title alone. Judgment, guardianship, and the authoritative hand specify how rule preserves a collective and acts through assigned responsibility. Might protects this order from being overborne, while wisdom gives its judgments direction.

#### Subchannel B. Reins That Correct Deviation
- Reading type: latent/lexical
- Scene or process: A governing hand checks harmful motion as a bridle checks an animal, turns it from a wrong line, and restores straightness against obstinate resistance.
- Active motifs: restraint for reform (`quranic:root_000348:B001/m01`); bridle surrounding the jaws (`quranic:root_000348:B006/m01`); deflection and prevention (`quranic:root_000555:B002/m01`); withholding or blocking a right (`quranic:root_000967:B008/m01`); obstinate departure from the straight way (`quranic:root_001052:B001/m01`); straightness, balance, and rectitude (`quranic:root_001273:B008/m01`).
- Ayah anchors: 62:1 `حَكِيمِ`; 62:2 `حِكْمَةَ`; 62:3 `حَكِيمُ`; 62:5 `قَوْمِ`, `قَوْمَ`, `ظَّٰلِمِينَ`; 62:7 `ظَّٰلِمِينَ`; 62:8 `تُرَدُّ`; 62:11 `عِندَ`, `قَآئِمًا`.
- Synthesis: The bridle gives wisdom a tactile corrective function: it does not annihilate motion but redirects it. Prevention is reform when it checks departure from a just line, whereas wrongdoing is itself a blockage of what is due. Straightness is the desired state produced by disciplined restraint.

#### Subchannel C. Measured Order Becomes Effective
- Reading type: mixed
- Scene or process: An intended form is measured, fixed in a binding determination, crafted with precision, and carried through as a decisive order.
- Active motifs: firmness and precise construction (`quranic:root_000348:B004/m01`); decisive judgment (`quranic:root_001237:B001/m01`); crafted form and executed action (`quranic:root_001237:B005/m01`); measure and determination (`quranic:root_001450:B001/m01`); binding written decree (`quranic:root_001283:B003/m01`); cohesion that makes a structure hold (`quranic:root_001444:B001/m01`).
- Ayah anchors: 62:1 `مَلِكِ`, `حَكِيمِ`; 62:2 `حِكْمَةَ`, `كِتَٰبَ`; 62:3 `حَكِيمُ`; 62:6 `تَمَنَّ`; 62:7 `يَتَمَنَّ`; 62:10 `قُضِيَتِ`.
- Synthesis: Judgment becomes effective through a production sequence: measure establishes the intended form, writing fixes it, precise craft gives it coherence, and execution makes it operative. Wisdom and decree thus meet in the capacity to make an order hold rather than remain an unperformed intention.

#### Subchannel D. Grievance Moves Toward Arbitration
- Reading type: latent/lexical
- Scene or process: Overreach creates a grievance; the injured party seeks redress, the parties negotiate or confront one another, and authority is delegated to an arbiter.
- Active motifs: transgressive overreach (`quranic:root_000138:B003/m01`); grievance and demand for redress (`quranic:root_000967:B003/m01`); negotiation between parties (`quranic:root_001272:B009/m01`); resistance and confrontation (`quranic:root_001273:B014/m01`); delegated arbitration (`quranic:root_000348:B005/m01`).
- Ayah anchors: 62:1 `حَكِيمِ`; 62:2 `حِكْمَةَ`; 62:3 `حَكِيمُ`; 62:5 `ظَّٰلِمِينَ`, `قَوْمِ`, `قَوْمَ`; 62:6 `قُلْ`; 62:7 `ظَّٰلِمِينَ`; 62:8 `قُلْ`; 62:10 `ٱبْتَغُ`; 62:11 `قُلْ`, `قَآئِمًا`.
- Synthesis: Wrongdoing generates a social claim, not only a moral label. The wronged party raises a grievance; speech can open negotiation, resistance can harden into confrontation, and arbitration places the dispute under an authorized judgment. Divine wisdom is thereby materialized as the capacity to receive and settle the claim produced by injustice.

### 11. Praise as Ordered Circulation
- Semantic invariant: Praise and livelihood share a disciplined freedom of movement through created space, from celestial courses to terrestrial ranging.
- Surface relation: indirect; 62:1 places praise across heavens and earth, while 62:10 releases people into the earth to seek provision after prayer.
- Surprising reach: The root of praise also carries swimming, stellar motion, and room to move for one's livelihood, so post-prayer circulation can echo rather than interrupt cosmic worship.

#### Subchannel A. The Cosmos Swims in Praise
- Reading type: latent/lexical
- Scene or process: Celestial bodies traverse the upper expanse while earth remains its lower counterpart, and their ordered motion is folded into worship.
- Active motifs: worship through praise (`quranic:root_000666:B001/m01`); swimming and the running of stars (`quranic:root_000666:B004/m01`); sky as the upper covering (`quranic:root_000745:B004/m01`); earth as the lower counterpart to sky (`quranic:root_000025:B001/m01`).
- Ayah anchors: 62:1 `يُسَبِّحُ`, `سَّمَٰوَٰتِ`, `أَرْضِ`.
- Synthesis: Praise acquires kinematics. The heavens are not a static setting but an expanse traversed by swimmers and running stars, while earth supplies the answering lower plane. Ordered cosmic motion itself becomes a material image of continuous praise.

#### Subchannel B. Ranging for Livelihood
- Reading type: mixed
- Scene or process: Once released, seekers range across ground as a flock spreads to graze, looking for the food and provision that sustain life.
- Active motifs: freedom to range for livelihood (`quranic:root_000666:B005/m01`); flock dispersing to graze (`quranic:root_001503:B006/m01`); seeking a desired provision (`quranic:root_000138:B001/m01`); food that enters and sustains the body (`quranic:root_000560:B002/m01`); ground and animal footing (`quranic:root_000025:B001/m02`).
- Ayah anchors: 62:1 `يُسَبِّحُ`, `أَرْضِ`; 62:10 `ٱبْتَغُ`, `أَرْضِ`, `ٱنتَشِرُ`; 62:11 `رَّٰزِقِينَ`.
- Synthesis: Terrestrial dispersal is recast as purposeful ranging rather than departure from worship. Space opens for livelihood, seekers move through it as grazing animals spread over ground, and provision supplies the bodily outcome of the search. The same lexical root that names praise therefore links ritual concentration to disciplined economic movement.

### 12. Worship as Orientation and Response
- Semantic invariant: Worship answers divine benefaction by directing body and voice toward the giver, turning received holiness and favor into aligned action and invocation.
- Surface relation: direct; 62:1 names the Holy God and cosmic praise, 62:4 names divine favor, 62:9 joins call, prayer, and remembrance, and 62:10 completes prayer while sustaining remembrance.
- Surprising reach: Roots beneath "unlettered," "before," and patronage supply aiming, qibla, and face-turning, while favor opens a reciprocal movement between invocation and mercy.

#### Subchannel A. The Body Turns Into Prayer
- Reading type: mixed
- Scene or process: Intention fixes a target, the face turns toward a prayer center, the worshipper resolves and rises, and bodily alignment becomes ritual prayer.
- Active motifs: deliberate aim toward a target (`quranic:root_000053:B012/m01`); prayer direction and qibla (`quranic:root_001198:B005/m01`); turning the face toward (`quranic:root_001684:B006/m01`); resolve and rising into an undertaking (`quranic:root_001273:B003/m01`); enacted ritual prayer (`quranic:root_000879:B003/m01`).
- Ayah anchors: 62:2 `أُمِّيِّۦنَ`, `قَبْلُ`; 62:5 `قَوْمِ`, `قَوْمَ`; 62:6 `أَوْلِيَآءُ`; 62:9 `صَّلَوٰةِ`; 62:10 `صَّلَوٰةُ`; 62:11 `قَآئِمًا`.
- Synthesis: Prayer begins before the rite as directed intention. A target is chosen, the face and attention are turned toward it, qibla stabilizes the orientation, and resolve becomes bodily performance. The call to leave sale is thus answered by a whole-person reorientation rather than movement toward a venue alone.

#### Subchannel B. Favor Answered in Invocation
- Reading type: mixed
- Scene or process: The holy giver grants favors and mercy; the recipient responds in worship, supplication, blessing, and an "Amen" that asks for the invoked good to be realized.
- Active motifs: deity as object of worship (`quranic:root_000047:B001/m01`); worship and devotion (`quranic:root_000047:B001/m02`); Holy as a divine name (`quranic:root_001206:B004/m01`); bestowed favors (`quranic:root_000076:B006/m01`); supplication and blessing (`quranic:root_000879:B002/m01`); divine mercy and commendation (`quranic:root_000879:B002/m02`); "Amen" seeking response (`quranic:root_000054:B003/m01`).
- Ayah anchors: 62:1 `لَّهِ`, `قُدُّوسِ`; 62:4 `ٱللَّهِ`, `ٱللَّهُ`; 62:5 `ٱللَّهِ`, `ٱللَّهُ`; 62:6 `لَّهِ`; 62:7 `ٱللَّهُ`; 62:9 `ءَامَنُ`, `صَّلَوٰةِ`, `ٱللَّهِ`; 62:10 `صَّلَوٰةُ`, `ٱللَّهِ`, `ٱللَّهَ`; 62:11 `ٱللَّهِ`, `ٱللَّهُ`. Ayah anchor unavailable for `quranic:root_000076:B006/m01` because root `ء ل ي` is listed in `missing_roots`.
- Synthesis: Benefaction becomes relational rather than merely economic. The holy giver is worshipped; prayer voices request and blessing, while its reciprocal sense names mercy and commendation from God. "Amen" closes the circuit by asking that the invoked good take effect, so favor is answered by directed address rather than priced return.


