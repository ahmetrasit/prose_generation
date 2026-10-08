Surah: 61. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own phrases), channels.md (an earlier reader's proposal: ignore its judgements (grades, strength or confidence labels, reading types, statements of what a reading may or may not do) and make your own) and your own knowledge of Arabic and the Quran. Return only the map as your final message.

When your discovery is complete and before you write your final output, run this command once, with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py S61 <refs separated by spaces>`. It lists refs from an earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

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

===== _commentary/v16/work/s061/surah.r2/text.md =====
# Surah 61

- 61:1 سَبَّحَ لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۖ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
- 61:2 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لِمَ تَقُولُونَ مَا لَا تَفْعَلُونَ
- 61:3 كَبُرَ مَقْتًا عِندَ ٱللَّهِ أَن تَقُولُوا۟ مَا لَا تَفْعَلُونَ
- 61:4 إِنَّ ٱللَّهَ يُحِبُّ ٱلَّذِينَ يُقَٰتِلُونَ فِى سَبِيلِهِۦ صَفًّۭا كَأَنَّهُم بُنْيَٰنٌۭ مَّرْصُوصٌۭ
- 61:5 وَإِذْ قَالَ مُوسَىٰ لِقَوْمِهِۦ يَٰقَوْمِ لِمَ تُؤْذُونَنِى وَقَد تَّعْلَمُونَ أَنِّى رَسُولُ ٱللَّهِ إِلَيْكُمْ ۖ فَلَمَّا زَاغُوٓا۟ أَزَاغَ ٱللَّهُ قُلُوبَهُمْ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْفَٰسِقِينَ
- 61:6 وَإِذْ قَالَ عِيسَى ٱبْنُ مَرْيَمَ يَٰبَنِىٓ إِسْرَٰٓءِيلَ إِنِّى رَسُولُ ٱللَّهِ إِلَيْكُم مُّصَدِّقًۭا لِّمَا بَيْنَ يَدَىَّ مِنَ ٱلتَّوْرَىٰةِ وَمُبَشِّرًۢا بِرَسُولٍۢ يَأْتِى مِنۢ بَعْدِى ٱسْمُهُۥٓ أَحْمَدُ ۖ فَلَمَّا جَآءَهُم بِٱلْبَيِّنَٰتِ قَالُوا۟ هَٰذَا سِحْرٌۭ مُّبِينٌۭ
- 61:7 وَمَنْ أَظْلَمُ مِمَّنِ ٱفْتَرَىٰ عَلَى ٱللَّهِ ٱلْكَذِبَ وَهُوَ يُدْعَىٰٓ إِلَى ٱلْإِسْلَٰمِ ۚ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلظَّٰلِمِينَ
- 61:8 يُرِيدُونَ لِيُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَٱللَّهُ مُتِمُّ نُورِهِۦ وَلَوْ كَرِهَ ٱلْكَٰفِرُونَ
- 61:9 هُوَ ٱلَّذِىٓ أَرْسَلَ رَسُولَهُۥ بِٱلْهُدَىٰ وَدِينِ ٱلْحَقِّ لِيُظْهِرَهُۥ عَلَى ٱلدِّينِ كُلِّهِۦ وَلَوْ كَرِهَ ٱلْمُشْرِكُونَ
- 61:10 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ هَلْ أَدُلُّكُمْ عَلَىٰ تِجَٰرَةٍۢ تُنجِيكُم مِّنْ عَذَابٍ أَلِيمٍۢ
- 61:11 تُؤْمِنُونَ بِٱللَّهِ وَرَسُولِهِۦ وَتُجَٰهِدُونَ فِى سَبِيلِ ٱللَّهِ بِأَمْوَٰلِكُمْ وَأَنفُسِكُمْ ۚ ذَٰلِكُمْ خَيْرٌۭ لَّكُمْ إِن كُنتُمْ تَعْلَمُونَ
- 61:12 يَغْفِرْ لَكُمْ ذُنُوبَكُمْ وَيُدْخِلْكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ ۚ ذَٰلِكَ ٱلْفَوْزُ ٱلْعَظِيمُ
- 61:13 وَأُخْرَىٰ تُحِبُّونَهَا ۖ نَصْرٌۭ مِّنَ ٱللَّهِ وَفَتْحٌۭ قَرِيبٌۭ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ
- 61:14 يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوٓا۟ أَنصَارَ ٱللَّهِ كَمَا قَالَ عِيسَى ٱبْنُ مَرْيَمَ لِلْحَوَارِيِّۦنَ مَنْ أَنصَارِىٓ إِلَى ٱللَّهِ ۖ قَالَ ٱلْحَوَارِيُّونَ نَحْنُ أَنصَارُ ٱللَّهِ ۖ فَـَٔامَنَت طَّآئِفَةٌۭ مِّنۢ بَنِىٓ إِسْرَٰٓءِيلَ وَكَفَرَت طَّآئِفَةٌۭ ۖ فَأَيَّدْنَا ٱلَّذِينَ ءَامَنُوا۟ عَلَىٰ عَدُوِّهِمْ فَأَصْبَحُوا۟ ظَٰهِرِينَ


===== _commentary/v16/work/s061/surah.r2/dictionary.md =====
# Dictionary: every branch of every focus root

Every root of the surah's words, each once, headed by the ayah and word where it first occurs; it also serves the later words listed with it.
One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ب ح (root_000666): 61:1 سَبَّحَ

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

## ء ل ه (root_000047): 61:1 لِلَّهِ, 61:3 ٱللَّهِ, 61:4 ٱللَّهَ, 61:5 ٱللَّهِ, 61:5 ٱللَّهُ, 61:5 وَٱللَّهُ, 61:6 ٱللَّهِ, 61:7 ٱللَّهِ, 61:7 وَٱللَّهُ, 61:8 ٱللَّهِ, 61:8 وَٱللَّهُ, 61:11 بِٱللَّهِ, 61:11 ٱللَّهِ, 61:13 ٱللَّهِ, 61:14 ٱللَّهِ, 61:14 ٱللَّهِ, 61:14 ٱللَّهِ

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## و ل ه (root_005296): documented alternative for 61:1 لِلَّهِ, 61:3 ٱللَّهِ, 61:4 ٱللَّهَ, 61:5 ٱللَّهِ, 61:5 ٱللَّهُ, 61:5 وَٱللَّهُ, 61:6 ٱللَّهِ, 61:7 ٱللَّهِ, 61:7 وَٱللَّهُ, 61:8 ٱللَّهِ, 61:8 وَٱللَّهُ, 61:11 بِٱللَّهِ, 61:11 ٱللَّهِ, 61:13 ٱللَّهِ, 61:14 ٱللَّهِ, 61:14 ٱللَّهِ, 61:14 ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## س م و (root_000745): 61:1 ٱلسَّمَٰوَٰتِ, 61:6 ٱسْمُهُۥٓ

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

## و س م (root_001650): documented alternative for 61:6 ٱسْمُهُۥٓ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı (also echo for 61:1 ٱلسَّمَٰوَٰتِ)

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

## ء ر ض (root_000025): 61:1 ٱلْأَرْضِ

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

## ع ز ز (root_001008): 61:1 ٱلْعَزِيزُ

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

## ح ك م (root_000348): 61:1 ٱلْحَكِيمُ

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

## ء م ن (root_000054): 61:2 ءَامَنُوا۟, 61:10 ءَامَنُوا۟, 61:11 تُؤْمِنُونَ, 61:13 ٱلْمُؤْمِنِينَ, 61:14 ءَامَنُوا۟, 61:14 فَـَٔامَنَت, 61:14 ءَامَنُوا۟

- **B001** guven ve guvenilirlik — ihanetin karsiti olan guvenilirlik ve emanet edilen sey · korkunun kalkmasi ve ic yatiskinligi · guven, eminlik ve yatiskinlik hali · guven verme, guven hali veya guvenceye birakilan sey · guven icinde olmak ve korkusu kalkmak · birini guven icine almak ve ona guven saglamak · guven icinde duruma gelmek · kendisine guvenilen emin kisi · emanet edilen veya kendisine guvenilen kisi · guven icinde olan, emin · guvenilir veya emanet edilebilir olan · kendisine bir sey emanet edilen kisi · guven icinde, tehlikeden uzak ve yatiskin · insanlarin zararindan korkmadigi guvenilir kimse · herkese guvenen ve duydugunu dogru sayan kisi · kisinin en degerli ve icinin yatistigi mali · guvenli yer veya guven icindeki mesken · birinin guvencesi altina girmek · bir seyi birine emanet etmek ve onu guvenilir saymak · zayiflamasindan veya surcmesinden korkulmayan saglam deve · kullarini veya dostlarini zulümden ve azaptan guvende kilan
  الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)
- **B002** dogru sayip kabul etme — ozellikle haber veya hakikati dogru kabul etme · herkese guvenen ve duydugunu dogru sayan kisi · kuluna vaat ettigi odulu dogrulayan · bizi dogru sayan veya bize inanan · bildirilen dine girme ve onu kabul etme adi · hakka kalp, dil ve davranisla baglanarak dogru kabul etme · iyi amel anlaminda namaz veya ibadet · guven vermeyen batil seylere guven duymak diye yerilen tutum
  الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)
- **B003** duada kabul istegi sozu — duada 'kabul et' veya 'oyle olsun' anlamina gelen soz · ilahi ad oldugu aktarilan dua sozu · duada kabul istegi bildiren sozu soyleme
  قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)

## ق و ل (root_001272): 61:2 تَقُولُونَ, 61:3 تَقُولُوا۟, 61:5 قَالَ, 61:6 قَالَ, 61:6 قَالُوا۟, 61:14 قَالَ, 61:14 قَالَ

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

## ECHO ق ل ل (root_001251): for 61:2 تَقُولُونَ, 61:3 تَقُولُوا۟, 61:5 قَالَ, 61:6 قَالَ, 61:6 قَالُوا۟, 61:14 قَالَ, 61:14 قَالَ: withheld observed target; not identity

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

## ف ع ل (root_001167): 61:2 تَفْعَلُونَ, 61:3 تَفْعَلُونَ

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

## ECHO ء ب و (root_000007): for 61:2 تَفْعَلُونَ, 61:3 تَفْعَلُونَ: withheld observed target; not identity

- **B001** babalık, besleyip yetiştirme ve oluşuma ya da iyileşmeye kaynaklık etme — baba · babalar, atalar ve baba yönünden onlara katılanlar · anne ile baba; bağlama göre baba ile amca veya dede · babalık veya baba soyu · birinin ya da bir topluluğun babası olmak · ebeveyn gibi besleyip büyütmek · birini baba edinmek · bir şeyin ortaya çıkmasına, düzelmesine veya görünür olmasına sebep olan kimse · konuklarla yakından ilgilenen kimse · savaşı kışkırtan kimse · bir kadının bekâretini bozan erkek
  يدل على التربية والغذو (maqayis)؛ أبوت الشيء آبوه أبوا إذا غذوته (maqayis)؛ فلان يأبو هذا اليتيم إباوة أي يغذوه كما يغذو الوالد ولده (ayn;tahdhib)؛ الأب أصله أبو (sihah)؛ الأب الوالد ويسمى كل من كان سببا في إيجاد شيء أو صلاحه أو ظهوره أبا (mufradat)
- **B002** babaya seslenme ve bağlama göre övgü ya da ağır yergi bildiren hitap kalıpları [kalıp] — babacığım diye seslenme · bağlama göre övgü ya da ağır sövgü bildiren hitap kalıbı · seni çekemeyenin babası olmasın anlamında onurlandırıcı hitap
  يا أبة افعل (sihah)؛ يا أبت ويا أبت لغتان (sihah)؛ لا أبا لك كأنه يمدحه (ayn)؛ لا أبا لك ولا أب لك مدح (sihah)؛ لا أبا لك ولا أب لك مدح ولا أم لك ذم (tahdhib)
- **B003** dağ keçisi idrarının kokusundan hastalanma — dağ keçisi idrarını koklayınca hastalanan dişi keçi · dağ keçisi idrarını koklayınca hastalanan erkek keçi
  عنز أبواء إذا أصابها وجع عن شم أبوال الأروى (maqayis)؛ عنز أبواء وتيس آبى إذا شم بول الأروى فمرض منه (sihah)

## ك ب ر (root_001281): 61:3 كَبُرَ

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

## م ق ت (root_001436): 61:3 مَقْتًا

- **B001** çirkin davranışta bulunana duyulan en güçlü nefret — çirkin bir davranışta bulunana duyulan çok güçlü nefret · çirkin bir iş yaptığı için ondan güçlü biçimde nefret etmek · çirkin bir işi yüzünden insanların nefret ettiği biri durumuna gelmek · çirkin davranışı yüzünden nefret edilen · çirkin davranışı yüzünden nefret edilen
  كلمة واحدة تدل على شناءة وقبح (maqayis)؛ المقت بغض من أمر قبيح ركبه (ayn;tahdhib)؛ مقته مقتا أبغضه (sihah)؛ المقت البغض الشديد لمن تراه تعاطى القبيح (mufradat)؛ المقت أشد البغض (tahdhib)
- **B002** İslam öncesinde bir erkeğin babasının eşiyle evlenmesi — İslam öncesinde bir erkeğin babasının eşiyle evlenmesi · bir erkeğin babasının eşiyle evlenmesinden doğan çocuk
  ونكاح المقت كان في الجاهلية أن يتزوج الرجل امرأة أبيه (maqayis;sihah)؛ كان يقال له مقت (tahdhib)؛ كان المولود عليه يقال له المقتي (tahdhib)؛ وكان يسمى تزوج الرجل امرأة أبيه نكاح المقت (mufradat)

## ع ن د (root_001052): 61:3 عِندَ

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

## ح ب ب (root_000286): 61:4 يُحِبُّ, 61:13 تُحِبُّونَهَا

- **B001** tane, tohum ve taneye benzeyen tek parça — tahıl tanesi ve yenebilir bitki tohumu · tek tane, tohum veya taneye benzeyen parça · dolu tanesi
  الحبة واحد الحب (jamhara;sihah)؛ الحب والحبة في الحنطة والشعير وبزور الرياحين (maqayis;tahdhib;mufradat)؛ الحبة من الشيء القطعة منه وحب الغمام وحب المزن وحب قر والحب القرط من حبة واحدة (sihah;tahdhib)
- **B002** sevgi ve yeğleme — sevgi; nefretin karşıtı · iyi görülen şeye yönelen güçlü sevgi · sevmek veya sevdirmek · yeğlemek veya sevmeye yönelmek · birbirini sevmek
  الحب والمحبة اشتقاقه من أحبه إذا لزمه (maqayis)؛ أحببته نقيض أبغضته (ayn)؛ المحبة إرادة ما تراه أو تظنه خيرا (mufradat)؛ استحبوا أي آثروه عليه (mufradat)
- **B003** övgü, güçlü istek ve kabul bildiren kalıplar — ne güzel; ne iyi · en büyük isteğin bunu yapmaktır · peki, memnuniyetle ve baş üstüne
  حبذا حرفان حب وذا تقول حبذا زيد (ayn;sihah;tahdhib)؛ حبابك أن تفعل ذاك معناه غاية محبتك (ayn;sihah;tahdhib;mufradat)؛ الحبة بالضم الحب يقال نعم وحبة وكرامة (sihah)
- **B004** kalbin içindeki kara öz [kalıp] — kalbin kara iç noktası veya özü
  حبة القلب سويداؤه ويقال ثمرته (maqayis;sihah)؛ حبة القلب هي العلقة السوداء التي تكون داخل القلب (tahdhib)؛ حبة القلب تشبيها بالحبة في الهيئة (mufradat)
- **B005** devenin güçsüzlükten yerinden ayrılamaması — devenin güçsüzlükten durup yerinden ayrılamaması · devenin hastalık veya güçsüzlükten çökmesi
  المحب البعير الذي يحسر فيلزم مكانه (maqayis)؛ بعير محب وقد أحب إحبابا وهو أن يصيبه مرض أو كسر فلا يبرح من مكانه (sihah;tahdhib)؛ أحب البعير إذا حرن ولزم مكانه (mufradat)
- **B006** suyla dolmak veya doldurup dolulaştırmak — su içip dolmak veya suya kanmak · doldurup dolu hale getirmek
  تحبب الحمار إذا امتلأ من الماء وشربت الإبل حتى حببت (sihah)؛ أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره (tahdhib)
- **B007** iri küp ve iki kulplu küpün dört parçalı desteği — iri küp veya büyük saklama kabı · iki kulplu küpün dört parçalı ayağı
  الحب الجرة الضخمة ويجمع على حببة وحباب (ayn;tahdhib)؛ الحب الخابية فارسي معرب والجمع حباب وحببة (sihah)؛ الحب الخشبات الأربع التي توضع عليها الجرة ذات العروتين (ayn;tahdhib)
- **B008** su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy — su kabarcıkları, suyun ana kütlesi, dalgası veya yüzey çizgileri · ağaç üzerindeki çiy
  حباب الماء فقاقيعه الطافية (ayn;tahdhib)؛ حباب الماء معظمه (maqayis;ayn;sihah;tahdhib)؛ حباب الماء موجه والطرائق التي في الماء (tahdhib)؛ الحباب من الماء النفاخات تشبيها به (mufradat)؛ الحباب الطل على الشجر (tahdhib)
- **B009** düzenli diş dizisi ve beyaz tükürük parıltısı — düzenli diş dizisi veya dişlerdeki beyaz tükürük parıltısı
  الحبب تنضد الأسنان (maqayis;ayn;sihah;tahdhib)؛ الحبب تنضد الأسنان تشبيها بالحب (mufradat)؛ حبب الفم ما يتحبب من بياض الريق على الأسنان (tahdhib)
- **B010** kısa veya küçük yapılı; develerde cılız — kısa boylu veya küçük bedenli kimse · cılız develer
  الحبحاب الرجل القصير (maqayis)؛ الحباحب الصغار (maqayis;sihah)؛ الحبحاب الصغير الجسم (tahdhib)؛ إبل حبحبة مهازيل (tahdhib)
- **B011** yararsız zayıf kıvılcım veya gece ışıldayan böcek — yararsız zayıf kıvılcım veya gece ışıldayan böcek · zayıf kıvılcımın tutuşması
  نار الحباحب ما اقتدحت من شرار النار في الهواء من تصادم الحجارة (ayn;tahdhib)؛ نار الحباحب ما أورت الخيل لا ينتفع به (maqayis;sihah;tahdhib)؛ ذباب يطير بالليل له شعاع كالسراج (ayn;sihah;tahdhib)
- **B012** yılan; yılanla ilişkilendirilen kötücül ruh adı — yılan veya yılanla ilişkilendirilen kötücül ruh adı
  ومما شذ عن الباب الحباب وهو الحية (maqayis)؛ الحباب أيضا الحية (sihah)؛ الحباب الحية وإنما قيل الحباب اسم شيطان لأن الحية يقال لها شيطان (tahdhib)

## ق ت ل (root_001200): 61:4 يُقَٰتِلُونَ

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

## س ب ل (root_000672): 61:4 سَبِيلِهِۦ, 61:11 سَبِيلِ

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

## ص ف ف (root_000871): 61:4 صَفًّا

- **B001** düz bir sıra oluşturma — düz çizgi üzerinde yan yana duran ögelerden oluşan sıra · yan yana sıraya dizmek · yan yana sıraya girmek · sıra halinde duran; kanatlarını açıp sabit tutan · savaş sırasının kurulduğu mevki · sıra halinde dizilmiş
  الصف معروف (ayn;tahdhib); الصف أن تجعل الشيء على خط مستو (mufradat); صففت القوم فاصطفوا (ayn;sihah;tahdhib); المصف الموقف والجمع المصاف (ayn;sihah;tahdhib); الصافات صفا يعني الملائكة (mufradat;tahdhib); الطير الصواف التي تصف أجنحتها فلا تحركها (ayn;tahdhib); البدن الصواف التي تصفف ثم تنحر (ayn;tahdhib)
- **B002** bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve — bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve · dişi deveyi tek sağımda iki veya üç kaba sağma
  الصفوف الناقة التي تجمع بين محلبين في حلبة (maqayis;tahdhib); الصف أن تحلب الناقة في محلبين أو ثلاثة تصف بينها (sihah); ناقة صفوف للتي تصف أقداحا من لبنها (sihah); الصفوف ناقة تصف بين محلبين فصاعدا لغزارتها (mufradat); الصفوف أيضا التي تصف يديها عند الحلب (maqayis;sihah;tahdhib)
- **B003** kurutmak ya da közlemek için sıra sıra serilmiş et — güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmiş et · eti şeritlere ayırıp sıra sıra sermek · eti genişletip inceltecek biçimde dilimleme
  الصفيف قال قوم هو القديد (maqayis); اللحم يحمل في الأسفار طبيخا أو شواء فلا ينضج (maqayis); الصفيف القديد اذا شر في الشمس (ayn;tahdhib); الصفيف ما صف من اللحم على الجمر لينشوي (sihah); صففت اللحم قددته وألقيته صفا صفا (mufradat); التصفيف نحو التشريح (tahdhib)
- **B004** yapı ya da eyer bölümü — yapıda ya da eyerde bulunan bölüm veya düzenek · hayvan için eyer düzeneği yapmak
  الصفة من البنيان والسرج ايضا (ayn); صفة الدار والسرج واحدة الصفف (sihah); صفة السرج (tahdhib); صففت للدابة صفة أي عملتها له (tahdhib); الصفة من البنيان وصفة السرج (mufradat)
- **B005** düz ve pürüzsüz arazi — düz ve pürüzsüz, kimi kullanımda bitkisiz arazi · düz ve pürüzsüz araziler
  الصفصف وهو المستوي من الأرض (maqayis); الصفصف الفلاة المستوية الملساء (ayn); الصفصف المستوى من الأرض (sihah); الصفصف الذي لا نبات فيه (tahdhib); الصفصف القرعاء (tahdhib); الصفصف المستوي الأملس (tahdhib); الصفصف المستوي من الأرض كأنه على صف واحد (mufradat)
- **B006** söğüt ağacı — söğüt ağacı
  الصفصف شجر الخلاف الواحدة بالهاء (ayn); الصفصاف شجر الخلاف (sihah;mufradat); الصفصاف الخلاف (tahdhib); هو شجر الخلاف بلغة أهل الشام (tahdhib)
- **B007** su başında toplanma [kalıp] — su başında toplanmak · su başında toplanmak
  تضافوا على الماء وتصافوا عليه بمعنى واحد إذا اجتمعوا عليه (tahdhib)

## ب ن ي (root_000156): 61:4 بُنْيَٰنٌ, 61:6 ٱبْنُ, 61:6 يَٰبَنِىٓ, 61:14 ٱبْنُ, 61:14 بَنِىٓ

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

## ر ص ص (root_000567): 61:4 مَّرْصُوصٌ

- **B001** sıkıca bitiştirip sağlamlaştırmak — bir şeyi sıkıca bitiştirip sağlamlaştırmak · sıkıca birleştirilmiş ve sağlamlaştırılmış · parçaları birbirine sıkıca yapıştırma · sırada boşluk bırakmadan sıklaşmak · dişleri birbirinin üzerine binmiş kimse · devenin eyer bağlarını birbirine yaklaştırmak · sıkıca birleştirilmiş, sağlam
  انضمام الشيء إلى الشيء بقوة وتداخل (maqayis); رصصت البنيان رصا إذا ضممت بعضه إلى بعض (maqayis;ayn;tahdhib); رص بناءه يرصه رصا إذا أحكم عمله (jamhara); رصصت الشيء أرصه رصا أي ألصقت بعضه ببعض (sihah); تراصوا في الصلاة أي تضايقوا فيها (mufradat); رجل أرص الأسنان أي ركب بعضها بعضا (ayn); رصصت قتبي البعير إذا قاربت قيدهما (ayn)
- **B002** kurşun ve kurşun kaplama — kurşun metali · kurşunla kaplanmış
  الرصاص أصل الباب (maqayis); اشتقاق الرصاص من هذا لتداخل أجزائه (jamhara); الرصاص بالفتح معروف وشيء مرصص مطلى به (sihah); الرصاص معروف (tahdhib); محكم كأنما بني بالرصاص (mufradat)
- **B003** yüz örtüsünü yalnız gözler görünecek kadar sıkılaştırmak — yüz örtüsünü yalnız gözler görünecek kadar sıkılaştırma · aynı sıkı örtünme biçiminin bölgesel söyleyişi · gözlere kadar yaklaştırılmış yüz örtüsü · yüz örtüsünü sıkılaştırıp gözlere yaklaştırmak
  الترصيص أن تنتقب المرأة فلا يرى إلا عيناها (maqayis;sihah); ترصيص المرأة أن تشدد التنقب (mufradat); الرصيص نقاب المرأة إذا أدنته من عينيها (tahdhib); تميم تقول هو التوصيص بالواو (tahdhib)
- **B004** su kaynağını çevreleyen bitişik taşlar — akan su kaynağının çevresindeki bitişik taşlar
  الرصراص الحجارة تكون مرصوصة حول عين الماء (maqayis); الرصاصة والرصراصة حجارة لازقة بحوالي العين الجارية (ayn;tahdhib)
- **B005** sert zemin veya yerinde sabit kalma — sert ve sıkı zemin · bulunduğu yerde sabit kalmak
  الرصراصة الأرض الصلبة (maqayis); رصرص إذا ثبت في المكان (tahdhib)
- **B006** ısrarla sormak — soru veya istekte ısrar etmek
  رصص إذا ألح في السؤال (tahdhib)

## ق و م (root_001273): 61:5 لِقَوْمِهِۦ, 61:5 يَٰقَوْمِ, 61:5 ٱلْقَوْمَ, 61:7 ٱلْقَوْمَ

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

## ء ذ ي (root_000023): 61:5 تُؤْذُونَنِى

- **B001** kişiyi ya da hayvanı inciten kötü etki — incitici veya can yakıcı şey · incitmek, canını yakmak · incitme, can yakma · bir şey yüzünden acı çekmek · incinmek veya canı yanmak · incinme veya canın yanması · incitici şey · incinme veya incitme · işitilen incitici söz · yeni doğanın başındaki saç · çok çabuk rahatsız olan kişi
  الشيء تتكرهه ولا تقر عليه (maqayis)؛ الأذى مقصور: معروف، وأذيت بالشيء آذى أذى شديدا (jamhara)؛ آذاه يؤذيه إيذاء فأذى هو أذى وأذاة وأذية وتأذيت به (sihah)؛ الأذى: كل ما تأذيت به، وما تسمعه من المكروه (tahdhib)؛ ما يصل إلى الحيوان من الضرر إما في نفسه أو جسمه أو تبعاته (mufradat)
- **B002** ağrıdan değil yaratılıştan yerinde durmayan deve [kalıp] — ağrıdan değil yaratılıştan yerinde durmayan erkek deve · ağrıdan değil yaratılıştan yerinde durmayan dişi deve
  بعير أذ وناقة أذية إذا كان لا يقر في مكان من غير وجع (maqayis;sihah;tahdhib)؛ ولكن خلقة (sihah;tahdhib)
- **B003** deniz dalgası veya rüzgarın kaldırdığı dalga dışı su tabakası — deniz dalgası · deniz dalgaları · rüzgarın su yüzeyinden kaldırdığı, dalga olmayan tabakalar
  الآذي: الموج (jamhara;sihah;tahdhib;mufradat)؛ آذي الماء: الأطباق التي تراها ترفعها من متنه الريح دون الموج (tahdhib)

## ع ل م (root_001040): 61:5 تَّعْلَمُونَ, 61:11 تَعْلَمُونَ

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

## ر س ل (root_000563): 61:5 رَسُولُ, 61:6 رَسُولُ, 61:6 بِرَسُولٍ, 61:9 أَرْسَلَ, 61:9 رَسُولَهُۥ, 61:11 وَرَسُولِهِۦ

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

## ز ي غ (root_000658): 61:5 زَاغُوٓا۟, 61:5 أَزَاغَ

- **B001** doğrultudan sapma — düz doğrultudan sapma · doğrultudan ya da yoldan sapmak · birini yoldan saptırmak · karşılıklı olarak sağa sola salınma · yoldan sapmış topluluk · doğrultudan sapmış
  الزيغ الميل (maqayis;ayn;sihah;tahdhib); الميل عن الاستقامة (mufradat); زاغ يزيغ زيغا (maqayis;sihah); أزاغه عن الطريق أماله (sihah); قوم زاغة أي زائغون (maqayis;sihah;mufradat); التزايغ التمايل (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** bakışın kayması ya da yorulması [kalıp] — bakışı kaymak ya da gözü yorulmak
  زاغ البصر أي كل (sihah); زاغت الأبصار (mufradat); ما زاغ البصر وما طغى (mufradat)
- **B003** güneş eğilirken gölgenin geri dönmesi [kalıp] — güneşin eğilip yerinden ayrılması ve gölgenin geri dönmesi
  زاغت الشمس إذا مالت وفاء الفيء (maqayis); زاغت الشمس أي مالت وذلك إذا فاء الفئ (sihah); زاغت الشمس تزيغ زيوغا فهي زائغة إذا مالت وزالت (tahdhib); زاغت الشمس (mufradat)
- **B004** birini sapmış durumda tutmak [kalıp] — birinin sapmasını sürdürüp yerleştirmek
  زيغت فلانا تزييغا إذا أقمت زيغه (tahdhib)
- **B005** kadının süslenip kendini göstermesi — kadının süslenip kendini göstermesi · kadının kendini süslemesi
  تزيغت المرأة من باب الإبدال وهي نون أبدلت غينا (maqayis); تزيغت المرأة أي تزينت وتبرجت (sihah); تزيغت المرأة وتزيقت تزيقا إذا تزينت (tahdhib)
- **B006** bir kuş adı — türü belirtilmemiş bir kuşun adı · bu kuş adının çoğul biçimi
  الزاغ هذا الطائر وجمعه الزيغان ولا أدري أعربي أم معرب (tahdhib)

## ق ل ب (root_001248): 61:5 قُلُوبَهُمْ

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

## ه د ي (root_001583): 61:5 يَهْدِى, 61:7 يَهْدِى, 61:9 بِٱلْهُدَىٰ

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

## ECHO ه د د (root_001580): for 61:5 يَهْدِى, 61:7 يَهْدِى, 61:9 بِٱلْهُدَىٰ: withheld observed target; not identity

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

## ف س ق (root_001156): 61:5 ٱلْفَٰسِقِينَ

- **B001** itaatten çıkıp Tanrı'nın buyruğuna karşı gelme ve kötülüğe yönelme — itaatten çıkma, Tanrı'nın buyruğunu bırakma ve kötülüğe yönelme · itaatten çıkıp buyruğa karşı gelmek; kötülük etmek · Tanrı'nın buyruğuna karşı gelmek ve itaatinden çıkmak · itaatten çıkmış, dinsel kuralları bütünüyle ya da kısmen çiğneyen kimse · itaatten çıkma; günah işleme ya da Tanrı'ya ortak koşma · itaatten çıkmış ve kötülüğe yönelmiş adam · sürekli olarak itaatten çıkan ve dinsel kuralları çiğneyen kimse
  الفسق وهو الخروج عن الطاعة (maqayis)؛ الفسق الترك لأمر الله؛ الميل إلى المعصية (ayn;tahdhib)؛ فسق الرجل يفسق فسقا وفسوقا أي فجر؛ فسق عن أمر ربه أي خرج (sihah)؛ الفسوق معناه الخروج؛ الشرك ويكون الإثم (tahdhib)؛ خرج عن حجر الشرع؛ أعم من الكفر (mufradat)
- **B002** taze hurmanın kabuğundan çıkması [kalıp] — taze hurma tanesinin kabuğundan çıkması
  فسقت الرطبة عن قشرها (maqayis;sihah)؛ فسقت الرطبة من قشرها لخروجها منه (tahdhib)؛ فسق الرطب إذا خرج عن قشره (mufradat)
- **B003** küçültmeli bir kötüleme adıyla anılan fare — küçültmeli bir kötüleme adıyla anılan fare
  إن الفأرة فويسقة (maqayis)؛ الفويسقة الفأرة (ayn;sihah)؛ سميت فويسقة لخروجها من جحرها (tahdhib)؛ سميت الفأرة فويسقة لما اعتقد فيها من الخبث والفسق؛ لخروجها من بيتها (mufradat)

## ب ن و (root_001959): documented alternative for 61:6 ٱبْنُ, 61:6 يَٰبَنِىٓ, 61:14 ٱبْنُ, 61:14 بَنِىٓ: İbn Fâris, Muʿcemü Mekāyîsi’l-luğa; incelenmiş Furûk root_001959/B001 dalı

- **B001** bir kaynaktan doğan ya da türeyen şey — 
  الشيء يتولد عن الشيء كابن الإنسان وغيره؛ النسبة إليه بنوي وكذلك النسبة إلى بنت وإلى بنيات الطريق
- **B002** çocukluk kalıbıyla kurulan geleneksel ad — 
  ثم تفرع العرب فتسمى أشياء كثيرة بابن كذا؛ ابن ذكاء الصبح وذكاء الشمس؛ ابن ترنا اللئيم؛ ابن ثأداء ابن الأمة؛ ابن الماء طائر؛ ابن جلا الصبح؛ ابن ملمة؛ ابن أحذار؛ ابن أقوال؛ ابن الفلاة؛ ابن غبراء؛ ابن السبيل؛ ابن ليل؛ ابن عمل؛ ابن مدينة؛ ابن بجدتها؛ ابن إحداها؛ ابن خلاوة؛ ابن حبة؛ ابن نعامة؛ ابنك ابن بوحك؛ فحمة ابن جمير؛ ابن طاب؛ وسائر ما تركنا ذكره من هذا الباب فهو مفرق في الكتاب

## ص د ق (root_000852): 61:6 مُّصَدِّقًا

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

## ب ي ن (root_000170): 61:6 بَيْنَ, 61:6 بِٱلْبَيِّنَٰتِ, 61:6 مُّبِينٌ

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

## ي د ي (root_001693): 61:6 يَدَىَّ

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

## ء ي د (root_000071): 61:14 فَأَيَّدْنَا (also echo for 61:6 يَدَىَّ)

- **B001** güç ve güçlendirme — güçlü kıldı · güç
  أيده الله أي قواه الله (maqayis)؛ والسماء بنيناها بأيد فهذا معنى القوة (maqayis)؛ الأيد أي القوة الشديدة (mufradat)؛ يؤيد بنصره أي يكثر تأييده (mufradat)؛ له أيد ومنه قيل للأمر العظيم مؤيد (mufradat)
- **B002** koruyucu engel — bir şeyi koruyan engel
  الإياد كل حاجز الشيء يحفظه (maqayis)؛ إياد الشيء ما يقيه (mufradat)

## ب ش ر (root_000120): 61:6 وَمُبَشِّرًۢا, 61:13 وَبَشِّرِ

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

## ء ت ي (root_000009): 61:6 يَأْتِى

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

## ب ع د (root_000131): 61:6 بَعْدِى

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

## ج ي ء (root_000281): 61:6 جَآءَهُم

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

## ج ي ء (root_000282): 61:6 جَآءَهُم

- **B001** gelmek veya ulaşmak — gelmek; ulaşmak · benimle sık gelme yarışına girdi, ben de onu geçtim · geliş; gelme
  جاء يجيء مجيئا (maqayis)؛ جاءاني فجئته أي غالبني بكثرة المجيء فغلبته (maqayis)؛ الجيئة مصدر جاء (maqayis)؛ جاء فلان جيأة (tahdhib)
- **B002** suyun biriktiği yer veya çukur — kale çevresinde, alçak yerde veya büyük çukurda su birikme yeri · suların aktığı yer; kötü nitelikli durgun su
  الجئة مجتمع الماء حوالي الحصن وغيره (maqayis)؛ الجيأة مجتمع ماء في هبطة حوالي الحصون (tahdhib)؛ الجيأة الموضع الذي يجتمع فيه الماء (tahdhib)؛ الجيأة الحفرة العظيمة يجتمع فيها ماء المطر (tahdhib)؛ يقال له جية وجيأة وكل من كلام العرب (tahdhib)
- **B003** çıban veya yarada birikmiş irin — çıban veya yarada birikmiş irin
  الجائية ما اجتمع في الخراج من المدة والقيح (tahdhib)؛ جاءت جائية الجراح (tahdhib)

## س ح ر (root_000682): 61:6 سِحْرٌ

- **B001** boğaz ve yemek borusu çevresindeki göğüs üstü iç organ bölgesi — boğaz ve yemek borusuna bağlı göğüs üstü iç organ bölgesi · korkudan içi kabardı · kesimde çıkarılıp atılan boğaz-göğüs dokusu · geniş karınlı ya da göğüs içi hasta · iç boşluğu bulunan ve besine gereksinen canlı
  السحر وهو ما لصق بالحلقوم والمرئ من أعلى البطن (maqayis)؛ السحر والسحر الرئة في البطن وما تعلق بالحلقوم؛ السحر أعلى الصدر (ayn)؛ السحر الرئة وما تعلق بها؛ انتفخ سحرك؛ كل ما كان له سحر فهو مسحر (jamhara)؛ السحر الرئة؛ انتفخ سحره (sihah)؛ السحر خفيف ما لصق بالحلقوم وبالمريء من أعلى البطن؛ انتفخ سحره للجبان (tahdhib)؛ السحر طرف الحلقوم والرئة؛ السحارة ما ينزع من السحر عند الذبح (mufradat)
- **B002** aldatma ve gerçeğinden saptırma — büyü, aldatma ve göz yanıltma · gizli güçlerden yardım alarak yapılan büyü · bazı sözler büyü gibi etkiler · aldattı ya da yönünden çevirdi · gözü yanıltıp gerçeği başka gösterdi · büyü yapan kimse; kimi eski kullanımlarda bilgili ve etkili kişi · çokça veya ustalıkla büyü yapan kimse · büyüden etkilenmiş ya da aklı ve durumu bozulmuş · işlevi bozulmuş yiyecek · ürün vermeyen ya da aşırı yağmurla bozulmuş toprak · sütü azalmış keçi · suyu aşırı olup zarar veren yağmur
  إخراج الباطل في صورة الحق؛ الخديعة (maqayis)؛ كل ما كان من الشيطان فيه معونة؛ الأخذة التي تأخذ العين؛ البيان في الفطنة (ayn)؛ السحر معروف سحر يسحر سحرا والفاعل ساحر وسحار (jamhara)؛ كل ما لطف مأخذه ودق فهو سحر؛ سحره بمعنى خدعه (sihah)؛ أصل السحر صرف الشيء عن حقيقته؛ تصرفون؛ ما سحرك عن وجه كذا؛ مسحورا ذاهب العقل مفسدا (tahdhib)؛ الخداع وتخييلات لا حقيقة لها؛ استجلاب معاونة الشيطان (mufradat)
- **B003** yiyecek ve içecekle besleme — besin; yiyecek veya içecekle doyurma · yiyecek ve içecekle beslenip oyalanırız · iç boşluğu bulunan ve besine gereksinen canlı
  من كان ذا سحر لم يجد بدا من مطعم ومشرب (maqayis)؛ السحر الغذو؛ المخلوق الذي يطعم ويسقى (ayn)؛ المرزوق الذي يأكل الرزق؛ نسحر بالطعام وبالشراب (jamhara)؛ نسحر بالطعام وبالشراب؛ المسحر من المعللين (sihah)؛ السحر الغذاء؛ نسحر بالطعام أي نعلل به (tahdhib)؛ سموا الغذاء سحرا؛ محتاج إلى الغذاء (mufradat)
- **B004** tan ağarmadan önceki son gece dilimi — tan ağarmadan önceki son gece dilimi · tan öncesi vaktin sabaha en yakın bölümü · belirsiz bir gecenin tan öncesi vaktinde · tan öncesi vaktin en üst ucu, sabahın ilk soluğu · tan öncesi vakte girdik ya da o vakitte yola çıktık · tan öncesinde yola çıktı ya da kuş o vakitte öttü · tan ağarmadan önce yola çıkan kimse · erken davrandı ya da tan öncesinde çıktı
  السحر والسحرة وهو قبل الصبح؛ أتيتك سحر؛ أتيتك سحرا (maqayis)؛ السحر آخر الليل؛ أسحرنا (ayn)؛ أسحر القوم إذا خرجوا في السحر؛ استحر الطائر إذا غرد في السحر؛ أعلى سحرين (jamhara)؛ السحر قبيل الصبح؛ السحرة السحر الأعلى؛ استحر الديك (sihah)؛ السحر قطعة من الليل؛ السحر آخر الليل؛ أسحرنا؛ استحرنا؛ سحر إذا بكر (tahdhib)؛ السحر والسحرة اختلاط ظلام آخر الليل بضياء النهار؛ المسحر الخارج سحرا (mufradat)
- **B005** tan öncesi öğünü — tan ağarmadan önce yenilen öğün · tan öncesi öğününü yeme
  تسحرنا أكلنا سحورا؛ السحور على فعول وضع اسما لما يؤكل في ذلك الوقت (ayn)؛ السحور ما أكل في السحر (jamhara)؛ السحور ما يتسحر به (sihah)؛ السحور ما يتسحر به وقت السحر من طعام أو لبن أو سويق؛ تسحر الرجل ذلك الطعام (tahdhib)؛ السحور اسم للطعام المأكول سحرا؛ التسحر أكله (mufradat)
- **B006** iki renk gösteren çekmeli çocuk oyuncağı — çekildiği yana göre başka renk gösteren çocuk oyuncağı
  السحارة شيء يلعب به الصبيان إذا مد خرج على لون وإذا مد من جانب آخر خرج على لون آخر (ayn;tahdhib)
- **B007** hayvanları semirten saplı bir ot — hayvanları semirten, saplı, küçük yapraklı ve siyah tohumlu ot
  الإسحارة بقلة يسمن عليها المال (ayn;tahdhib)؛ بقلة حارة تنبت على ساق لها ورق صغار لها حبة سوداء (tahdhib)
- **B008** bir şeyin kenarı, sonu ya da üst ucu — her şeyin kenarı ya da sonu · açık arazinin kıyıları · vadinin üst kesimi · siyahın üstünde görünen beyazlık
  السحر والسحرة بياض يعلو السواد؛ سحر كل شيء طرفه؛ أسحار الفلاة أطرافها؛ سحر الوادي أعلاه (tahdhib)

## ظ ل م (root_000967): 61:7 أَظْلَمُ, 61:7 ٱلظَّٰلِمِينَ

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

## ف ر ي (root_001150): 61:7 ٱفْتَرَىٰ

- **B001** onarmak veya yapmak için kesip biçmek — onarmak veya dikmek için kesip biçmek · deriyi dikiş ve onarım için kesme · su tulumunu kesip biçerek yapmak
  فريت الشيء أفريه فريا وذلك قطعه لإصلاحه (maqayis)؛ فرى إذا خرز (maqayis)؛ فريته أصلحته (ayn)؛ فريت الشئ أفريه قطعته لأصلحه (sihah)؛ فريت المزادة خلقتها وصنعتها (sihah)؛ الفري قطع الجلد للخرز والإصلاح (mufradat)
- **B002** bozarak kesmek veya yarmak — bozacak biçimde kesmek veya yarmak · boyun damarlarını kesmek · yarılıp ayrılmak · yarılmış
  أفريته إذا أنت قطعته للإفساد (maqayis)؛ فريت الشيء بالسيف وبالشفرة قطعته وشققته (ayn)؛ التفري التشقق (ayn)؛ أفريت الأوداج قطعتها (sihah)؛ أفريت الشيء شققته فانفرى وتفرى (sihah)؛ أفرى الذئب بطن الشاة (sihah)؛ الإفراء للإفساد (mufradat)
- **B003** asılsız söz veya suçlama uydurmak — yalan veya ağır bir asılsızlık uydurmak · uydurulmuş yalan veya asılsız suçlama · bir yalanı üretip uydurmak
  فرى فلان كذبا يفريه إذا خلقه (maqayis)؛ فرى يفري فلان الكذب إذا اختلقه والفرية الكذب والقذف (ayn)؛ فرى فلان كذبا إذا خلقه وافتراه اختلقه والاسم الفرية (sihah)؛ الافتراء في الإفساد أكثر وكذلك استعمل في القرآن في الكذب والشرك والظلم (mufradat)
- **B004** şaşırtıcı, büyük ya da düzülmüş şey — şaşırtıcı, büyük veya yapılmış şey · şaşırtıcı, büyük ya da düzülmüş bir şey · işinde hayret verici bir şey yapmak
  فلان يفري الفري إذا كان يأتي بالعجب (maqayis)؛ الفرى أيضا مثل الفري وهو العجب (maqayis)؛ الفري الأمر العظيم في قوله لقد جئت شيئا فريا (ayn)؛ فلان يفري الفري إذا كان يأتي بالعجب في عمله (sihah)؛ لقد جئت شيئا فريا أي مصنوعا مختلقا وقيل عظيما (sihah)؛ لقد جئت شيئا فريا قيل معناه عظيما وقيل عجيبا وقيل مصنوعا (mufradat)
- **B005** yerin yarılıp kaynaklardan su fışkırtması [kalıp] — yerin kaynaklarla yarılıp su fışkırtması
  تفرت الأرض بالعيون انبجست (maqayis)؛ تبجست الأرض بالعيون وتفرت (ayn)؛ غمارا تفرى بالسلاح وبالدم (ayn)؛ تفرت الأرض بالعيون انبجست (sihah)
- **B006** kürk ve kalın örtü; baş derisi, zenginlik veya kuru bitki kümesi — giyilen kürk veya kalın deri örtü · kürkler · kürk giydi · baş derisi · varlık ve zenginlik · kuruyup bir araya kümelenmiş bitki topluluğu
  الفروة التي تلبس (maqayis)؛ فروة الرأس وهي جلدته (maqayis)؛ الفروة وهي الغنى والثروة (maqayis)؛ الفروة كل نبات مجتمع إذا يبس (maqayis)؛ التغطية والستر بشيء ثخين (maqayis)؛ الفرو الذي يلبس والجمع الفراء (sihah)؛ الفروة جلدة الرأس (sihah)؛ الفروة إبدال الثروة وهي الغنى (sihah)؛ الفروة قطعة نبات مجتمعة يابسة (sihah)
- **B007** şaşırıp bocalamak — şaşırıp bocalamak
  الفرى البهت والدهش يقال فري يفرى فرى (maqayis)؛ فري بالكسر يفرى فرى تحير ودهش (sihah)
- **B008** öne atılmaktan korkan kişi — öne atılmaktan korkan kişi
  الفرى الجبان سمي بذلك لأنه فري عن الإقدام أي قطع (maqayis)
- **B009** gürültülü patırtı — gürültülü patırtı
  الفرية الجلبة (ayn)

## ECHO ف ت ر (root_001125): for 61:7 ٱفْتَرَىٰ: withheld observed target; not identity

- **B001** şiddetini yitirerek zayıflama, yumuşama ve durulma — zayıflamak; sertliği ya da şiddeti azalıp durulmak · bir şeyi zayıflatmak ya da şiddetini gidermek · bir şeyi zayıflatmak veya ılık duruma getirmek · şiddetten sonra durulma, sertlikten sonra yumuşama ve güçten sonra zayıflama · bedende ya da iç dünyada kırılma ve güçsüzlük · keskin olmayan, durgun bakış · göz kapakları zayıflayıp bakışı kırılmak · içilince bedeni gevşeten şey · sıcak ile soğuk arasında, ılık su · sıcağın şiddeti kırılıp azalmak · yağmur suyunu boşaltıp kesilmek ve duraksamak · taşkınlıktan sonra benim izlediğim yola yönelip durulmak
  أصل صحيح يدل على ضعف في الشيء (maqayis)؛ الفترة الانكسار والضعف (sihah)؛ الفتور سكون بعد حدة ولين بعد شدة وضعف بعد قوة (mufradat)؛ فتر فلان إذا سكن عن حدته ولان بعد شدته (tahdhib)؛ فتر الإنسان إذا لانت مفاصله وضعفت (jamhara)؛ لا يفتر أي لا يضعف (maqayis)؛ لا يسكنون عن نشاطهم (mufradat)؛ المفتر الذي يفتر الجسد (tahdhib)؛ ماء فاتر بين الحار والبارد (tahdhib)؛ فتر مطر فرغ ماءه وكف وتحير (tahdhib)
- **B002** iki elçinin gelişi arasındaki dönem — iki elçinin gelişi arasındaki, yeni bir elçinin gelmediği dönem
  الفترة ما بين كل نبيين (jamhara)؛ الفترة ما بين الرسولين من رسل الله عزوجل (sihah)؛ على فترة من الرسل أي سكون حال عن مجيء رسول الله (mufradat)
- **B003** başparmak ile işaret parmağı arasındaki açıklık ve bununla ölçme — başparmak ile işaret parmağı açıldığında uçları arasında kalan açıklık · bir şeyi başparmak ile işaret parmağı arasındaki açıklığı kullanarak ölçmek
  الفتر ما بين طرف الإبهام وطرف السبابة إذا فتحتهما (maqayis)؛ الفتر ما بين طرفي السبابة وطرف الإبهام إذا فتحتهما (jamhara)؛ الفتر ما بين طرف السبابة والابهام إذا فتحتهما (sihah)؛ الفتر قدر ما بين طرف الإبهام وطرف المسبحة وقد فترت الشيء إذا قدرته بفترك (tahdhib)؛ الفتر ما بين طرف الإبهام وطرف السبابة يقال فترته بفتري (mufradat)

## ك ذ ب (root_001290): 61:7 ٱلْكَذِبَ

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

## د ع و (root_000478): 61:7 يُدْعَىٰٓ

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

## ECHO د ع ع (root_000477): for 61:7 يُدْعَىٰٓ: withheld observed target; not identity

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

## س ل م (root_000737): 61:7 ٱلْإِسْلَٰمِ

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

## ر و د (root_000610): 61:8 يُرِيدُونَ

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

## ECHO ر د د (root_000555): for 61:8 يُرِيدُونَ: withheld observed target; not identity

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

## ط ف ء (root_000938): 61:8 لِيُطْفِـُٔوا۟

- **B001** ateşin sönmesi veya söndürülerek alevinin dindirilip közünün soğutulması — ateşin alevi dinip közü soğuyarak sönmesi · ateşin sönmesi ve alevinin kesilmesi · ateşi söndürmek ve soğuyuncaya kadar dindirmek · alevi dinmiş, közü soğumuş sönük ateş · Tanrı'nın ışığını söndürmeye veya ortadan kaldırmaya çalışma · yaşlı kadın günlerinden, közün sönmesiyle adlandırılan bir gün
  طفئت النار تطفأ وأطفأتها (maqayis;ayn;sihah;tahdhib;mufradat)؛ سكن لهبها وبرد جمرها (ayn;tahdhib)؛ انطفأت ومطفئ الجمر (sihah)؛ يريدون أن يطفؤا نور الله وإطفاء نور الله (mufradat)

## ط ف ء (root_000939): 61:8 لِيُطْفِـُٔوا۟

- **B001** alevin dinmesinden közün soğumasına uzanan sönme ve söndürme — ateşin alevi dinip közü yanmayı sürdürebilen sönük duruma gelmesi veya közü de soğuyarak bütünüyle sönmesi · ateşi sönüp soğuyuncaya kadar söndürmek · alevi dinmiş, közü soğumuş sönmüş ateş
  طفئت النار تطفأ وأنا أطفأتها (maqayis)؛ أهمدها حتى تبرد (tahdhib)؛ النار سكن لهبها وجمرها يتقد فهي خامدة (tahdhib)؛ فإذا سكن لهبها وبرد جمرها فهي هامدة طافئة (tahdhib)

## ن و ر (root_001564): 61:8 نُورَ, 61:8 نُورِهِۦ

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

## ف و ه (root_001190): 61:8 بِأَفْوَٰهِهِمْ

- **B001** ağız ve ağız ağıza konuşma — ağız adının temel ve eski söz biçimi · ağızlar · onunla ağız ağıza, doğrudan konuşmak
  أصل الفم فوه (maqayis)؛ الفوه أصل بناء الفم (ayn)؛ الفوه أصل قولنا فم (sihah)؛ كلمته فاه إلى في أي مشافها (sihah)؛ أصل بناء تأسيس الفم (tahdhib)؛ أفواه جمع فم وأصل فم فوه (mufradat)
- **B002** geniş ağızlılık ve öne çıkmış uzun üst dişler — ağız genişliği · geniş ağızlı veya uzun dişli kimse · geniş ağızlı veya uzun dişli dişi ya da at · ipin geçtiği uzun dişleri olan çark
  الفوه سعة الفم (maqayis)؛ رجل أفوه وامرأة فوهاء (maqayis)؛ الأفوه الواسع الفم وفرس فوهاء شوهاء واسعة الفم (ayn)؛ الفوه خروج الثنايا العليا وطولها (maqayis;ayn;sihah;tahdhib)؛ محالة فوهاء إذا كانت أسناتها طوالا (sihah;tahdhib)
- **B003** söz söyleme, konuşma gücü ve arkadan çekiştirme — sözü dile getirmek, ağzını açıp söylemek · konuşma yeteneği güçlü kimse · iyi ve akıcı konuşan kimse · söze karşılık verme veya sözü geri çevirme · insanları arkalarından çekiştirme · onunla konuşup söz ve övünme yarışına girmek · açlığını belli edip açıkça söylemek
  فاه الرجل بالكلام يفوه به إذا لفظ به (maqayis)؛ المفوه القادر على الكلام (maqayis)؛ ما فهت بكلمة وما تفوهت أي ما فتحت فمي بها (sihah)؛ المفوه المنطيق والفيه المنطيق (sihah;tahdhib)؛ إن رد الفوهة لشديد أي القالة (sihah;tahdhib)؛ الفوهة تقطيع المسلمين بعضهم بعضا بالغيبة (tahdhib)؛ علق حكم القول بالفم (mufradat)
- **B004** yerin ağzı, girişi, çıkışı veya başlangıcı [kalıp] — nehir ağzı veya suyun çıktığı yer · vadinin başı veya çıkışı · yolun girişi veya başlangıcı · sokakların girişleri · yerin ilk bölümleri · deve sürüsünün önü ve ilk hayvanları · yerin girişinden içeri girmek
  الفوهة فم النهر (maqayis)؛ الفوهة رأس الوادي وفم النهر (ayn)؛ فوهة النهر الموضع الذي يخرج منه ماؤه وكذلك فوهة الوادي (jamhara)؛ أفواه الأزقة والأنهار واحدتها فوهة (sihah)؛ فوهة الطريق وفوهة النهر (tahdhib)؛ المفوهة فم النهر ورأس الوادي (tahdhib)؛ أفواه المكان أوائله (tahdhib)؛ فوهة النهر كقولهم فم النهر (mufradat)
- **B005** koku karışımında kullanılan hoş kokulu madde — hoş koku hazırlamada kullanılan kokulu maddeler · hoş koku hazırlamada kullanılan tek bir madde · kokulu karışım maddelerinin genişletilmiş çoğulu
  الفوه واحد أفواه الطيب (maqayis)؛ أفواه الطيب واحدها فوه (jamhara)؛ الأفواه ما يعالج به الطيب (sihah)؛ فوه وأفواه ثم أفاويه (sihah)؛ واحد أفواه الطيب فوه (tahdhib)؛ أفواه الطيب الواحد فوه (mufradat)
- **B006** iştahın güçlenmesi; hayvanın yiyişi, sulanması ve otlatılarak yürütülmesi — az yemeden sonra yemesi artıp güçlenmek · çok ve iştahlı yiyen kimse · bu yemekten çok ve güçlü biçimde yemek · hayvanın iyi yiyişi besililiğini gösterir · develeri önceden yalak doldurmadan vardıkları yerde sulamak · develeri serbestçe otlatıp yürütmek
  استفاه الرجل كثر أكله بعد القلة (ayn)؛ رجل فيه أي أكول (ayn)؛ استفاه الرجل إذا اشتد أكله بعد ضعف وقلة (sihah)؛ الفيه الأكول (sihah;tahdhib)؛ شديد الأكل وشد ما فوهت في هذا الطعام وتفوهت وفهت (tahdhib)؛ أفواهها مجاسها (tahdhib)؛ سقى إبله على أفواهها (tahdhib)؛ جر فلان إبله على أفواهها (tahdhib)
- **B007** boyamada kullanılan bitki kökleri — boyamada kullanılan bitki kökleri
  الفوهة عروق يصبغ بها (ayn)؛ الفوه عروق يصبغ بها (tahdhib)؛ لم أسمع الفوه بهذا المعنى (tahdhib)
- **B008** ağız ve yer görüntülü kalıplaşmış ilenme sözü [kalıp] — umduğunu bulamayasın; ağzın yere gelsin · ağzın yere yapışsın veya kırılsın; yıkım getiren şeyin ağzı
  فاها لفيك ومعناه الخيبة لك (sihah;tahdhib)؛ جعل الله لفيك الأرض (sihah;tahdhib)؛ فاها بفيك منونا أي ألصق الله فاك بالأرض (tahdhib)؛ دعا عليه بكسر الفم (tahdhib)؛ يريد فا الداهية (tahdhib)

## ت م م (root_000188): 61:8 مُتِمُّ

- **B001** tamamlanma ve tamamlama — bir seyin tamamlanmasi · bir seyi tamamlamak · bir seyi eksiksiz hale getirmek · tamamlanmasini istemek veya tamamlamak · bir seyin eksiksiz son siniri · eksigi tamamlayan parca · eksiksiz · hepsi gelip tamamlanmak · insanlarin toplanip tamamlanmasi · sozu sonuna kadar surdurmek · kesinlesmek ve gerekli olmak
  تم الشيء إذا كمل وأتممته أنا (maqayis)؛ تم الشئ تماما وأتمه غيره وتممه واستتمه بمعنى (sihah)؛ تم الشيء يتم تماما وتممه الله تتميما وتتمة (tahdhib)؛ تمام الشيء انتهاؤه إلى حد لا يحتاج إلى شيء خارج عنه (mufradat)؛ تتاموا أي جاءوا كلهم وتموا (sihah)؛ أبى قائلها إلا تما أي تماما ومضى على قوله (sihah)؛ التم الناس وجمعه تممة (tahdhib)
- **B002** korunma boncugu — korunma icin asilan boncuk veya nesne
  التميمة كأنهم يريدون أنها تمام الدواء والشفاء المطلوب (maqayis)؛ التميمة عوذة تعلق على الانسان ويقال هي خرزة (sihah)؛ التمائم واحدتها تميمة وهي خرزات كانت الأعراب يعلقونها على أولادهم (tahdhib)
- **B003** sert ve saglam — sert, siddetli veya uzun
  التميم أيضا الشيء الصلب (maqayis)؛ التميم الشديد (sihah)؛ التميم الصلب (tahdhib)؛ التميم الطويل (tahdhib)
- **B004** suresi veya miktari dolma — hamilelik gunleri dolmak · hamilelik suresi dolmus kadin · tam vaktinde dogmak · dolunay halindeki ay · en uzun gece veya tam gece · ayin tamamlanmasi vaktinde
  امرأة حبلى متم وولدت لتمام وليل التمام (maqayis)؛ أتمت الحبلى فهي متم إذا تمت أيام حملها وولد المولود لتمام وقمر تمام إذا تم ليلة البدر وليل التمام أطول ليلة في السنة (sihah)؛ ولد فلان لتمام وتمام وليل التمام بالكسر لا غير (tahdhib)؛ يقال ذلك للمعدود والممسوح تقول عدد تام وليل تام (mufradat)
- **B005** konusmada takilma — konusmada ses yineleyerek takilma · konusurken takilan veya zor anlasilan kisi
  التمتام الذي في تمتمة وهو الذي يتردد في التاء (sihah)؛ التمتمة من الكلام ألا يبين اللسان فيرجع إلى لفظ كأنه التاء أو الميم ورجل تمتام (tahdhib)؛ التمتمة الترديد في التاء (tahdhib)
- **B006** paylari tamamlayip yedirme — ok payi oyununda paydan yedirmek veya eksigi tamamlamak · ard arda kazanip etini yoksullara yediren kisi
  تتميم الأيسار أن تطعمهم فوز قدحك فلا تنتقص منه شيئا (maqayis)؛ إذا فاز قدح الرجل مرة بعد مرة فأطعم لحمه المساكين سمي متمما (tahdhib)؛ التميم في الأيسار أن ينقص الأيسار في الجزور فيأخذ رجل ما بقي حتى يتمم الأنصباء (tahdhib)
- **B007** dokumayi tamamlayan parca — dokumasini tamamlamak icin yün veya tüy isteyen kisi · dokumayi tamamlayan hediye yün veya tüy parcasi
  المستتم الذي يطلب شيئا من صوف أو وبر يتم به نسج كسائه والموهوب تمة (maqayis)؛ المستتم هو الذي يطلب الصوف والوبر ليتم به نسج كسائه والموهوب تمة (sihah)
- **B008** kirilip helak sinirina varma — kirilmak veya son sinira ulasmak · helak etmek veya eceline vardirmak · kirilmis veya kirilma sinirina varmis
  المتتمم المتكسر قد يكون من هذا لأنه يتناهى حتى يتكسر ويجوز أن يكون التاء بدلا من ثاء (maqayis)؛ تم إذا كسر وتم إذا بلغ (tahdhib)؛ تتممه أي تهلكه وتبلغه أجله (tahdhib)؛ تتمم تتمما أي تم عرجه كسرا (tahdhib)
- **B009** kabile adi ve nispeti — belirli bir kabile adi veya ona mensup olma · gorus, egilim veya yer bakimindan o kabileye mensup olmak
  تميم قبيلة (sihah)؛ تميم بن مر بن أد ابن طابخة بن إياس بن مضر (sihah)؛ تمم الرجل إذا صار تميمي الرأي والهوى والمحلة (tahdhib)

## ك ر ه (root_001295): 61:8 كَرِهَ, 61:9 كَرِهَ

- **B001** hoşlanmama ve istememe — bir şeyden hoşlanmamak ve onu istememek · hoşnutsuzluk; istenmeyen şey · hoşnutsuzluk ve tiksinme · hoşnutsuzluk ve tiksinme · hoşnutsuzluk ve kaçınma · sevimsiz, ağır gelen · istenmeyen, hoş görülmeyen · bir şeyi birine sevimsiz göstermek · hoşa gitmeyen, ağır gelen iş
  خلاف الرضا والمحبة (maqayis)؛ كرهت الشيء أكرهه كرها والكراهية (maqayis)؛ الكره المكروه وأمر كريه مستكره مكروه وكرهته كراهة وكراهية ومكرهة (ayn)؛ كرهت الشئ أكرهه كراهة وكراهية فهو شئ كريه ومكروه وكرهت إليه الشئ تكريها نقيض حببته إليه (sihah)؛ يقال كرهت الشيء كرها وكرها وكراهة وكراهية والكره المكروه وكره إلي هذا الأمر تكريها (tahdhib)؛ ما يعاف من حيث الطبع وما يعاف من حيث العقل أو الشرع (mufradat)
- **B002** isteksizce katlanılan güçlük — güçlük; isteksizce yapılan iş · güçlük içinde ve gönülsüzce · bir şeyi istemeye istemeye yapmak · bir işi gönülsüzce yapmak · bundan hoşnut olmayarak · bundan hoşnut olmayarak
  الكره المشقة والكره أن تكلف الشيء فتعمله كارها (maqayis)؛ فعلته على كره وفعلته كرها (ayn)؛ الكره بالضم المشقة قمت على كره أي على مشقة (sihah)؛ كراهتهم القتال أنهم كرهوه على جنس غلظه عليهم ومشقته (tahdhib)؛ الكره المشقة التي تنال الإنسان من خارج والكره ما يناله من ذاته وهو يعافه (mufradat)
- **B003** istemediği bir şeye zorlama — birini istemediği bir işe zorlamak · bir insanı istemediği şeye zorlama · zor kullanılarak cinsel saldırıya uğratılmış kadın
  امرأة مستكرهة غصبت نفسها فأكرهت على ذلك وأكرهته حملته على أمر وهو كاره (ayn)؛ أكرهته على كذا حملته عليه كرها (sihah)؛ امرأة مستكرهة إذا غصبت نفسها وأكرهت فلانا حملته على أمر هو له كاره (tahdhib)؛ الإكراه يقال في حمل الإنسان على ما يكرهه (mufradat)
- **B004** savaşın ağır şiddeti — savaşın ağır şiddeti · zamanın felaketleri ve ağır olayları · darbede işleyen keskin kılıç
  الكريهة الشدة في الحرب والسيف الماضي في الضرائب ذو الكريهة (maqayis)؛ الكريهة الشدة في الحرب وكذلك الكرائه وهي نوازل الدهر (ayn)؛ الكريهة الشدة في الحرب وذو الكريهة السيف الماضي في الضريبة (sihah)؛ الكريهة الشدة في الحرب وكذلك كرايه الدهر نوازل الدهر وذو الكريهة وهو الذي يمضي في الضرائب (tahdhib)
- **B005** inatçı ve zor mizaçlı [kalıp] — başı sert, yönlendirilmeye direnen deve · zor mizaçlı, hoşnutsuz ve içine kapanık adam
  الكره الجمل الشديد الرأس كأنه يكره الانقياد (maqayis)؛ رجل كره متكره وجمل كره شديد الرأس (ayn)؛ الكره الجمل الشديد الرأس (sihah)؛ رجل كره متكره وجمل كره شديد الرأس (tahdhib)
- **B006** çukurun üst bölümü — çukurun üst bölümü
  الكرهاء أعلى النقرة بلغة هذيل (ayn)؛ الكرهاء هي أعلى النقرة بلغة هذيل (tahdhib)
- **B007** sert ve kaba arazi — sert ve kaba yapılı arazi
  يقال للأرض الصلبة الغليظة مثل القف وما قاربه كرهة (tahdhib)

## ك ف ر (root_001307): 61:8 ٱلْكَٰفِرُونَ, 61:14 وَكَفَرَت

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

## د ي ن (root_000504): 61:9 وَدِينِ, 61:9 ٱلدِّينِ

- **B001** boyun eğerek uyma ve buna dayalı inanç düzeni — boyun eğme, kulluk ve inanç düzeni · ona boyun eğdi ve buyruğuna uydu · gerçek inanç yolu · hükümdarın buyruğu ya da yargısı
  أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)؛ فالدين الطاعة (maqayis;sihah)؛ الدين لله طاعته والتعبد له (tahdhib)؛ الدين كالملة اعتبارا بالطاعة والانقياد للشريعة (mufradat)
- **B002** yargılayıp hesap görerek karşılığını verme — hesap, yargı ve yapılanın karşılığı · hesap ve karşılık günü · hesaba çekilip karşılığı verilecek olanlar · yargılayan ve karşılığını veren · hükümdarın buyruğu ya da yargısı · kendini alçalttı ya da hesaba çekti
  يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)؛ الدين الجزاء والمكافأة (sihah)؛ الدين الحساب ومنه مالك يوم الدين ومالك يوم الجزاء (tahdhib)؛ غير مدينين أي غير مجزيين (mufradat)
- **B003** borç alıp verme ve vadeli ödeme ilişkisi — borç ve vadeli ödeme yükümlülüğü · onunla borç alıp verme işlemi yaptı · ona ödünç verdi · ödünç aldı ve borçlandı · borçlu veya çok borçlanmış kişi · onu vadeli olarak sattım
  الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)؛ الدين واحد الديون وتداينوا تبايعوا بالدين (sihah)؛ دنت الرجل أقرضته وأدنت الرجل إذا أقرضته (tahdhib)؛ التداين والمداينة دفع الدين (mufradat)
- **B004** zorla alçaltıp egemenliği altına alma — onu alçalttı, boyunduruk altına aldı ve köleleştirdi · topluluğu alçalttım ve köleleştirdim · onu mülk edindim veya buyruğum altına aldım · köleleştirilmiş erkek · köleleştirilmiş kadın · kendini alçalttı ya da hesaba çekti · kalbini alçaltan şey; ayrıca alışkanlık, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)؛ دانه دينا أي أذله واستعبده ودينته ملكته (sihah)؛ غير مدينين غير مملوكين ودنت القوم أدينهم إذا أذللتهم (tahdhib)؛ المدين والمدينة العبد والأمة (mufradat)
- **B005** alışılmış davranış ve öteden beri bilinen hal — alışkanlık, olağan iş ve öteden beri bilinen hal · kalbinin alışkanlığı; ayrıca alçaltma, istemediği şeye zorlama veya eski gönül derdi diye yorumlanan tartışmalı söz
  العادة يقال لها دين (maqayis)؛ الدين بالكسر العادة والشأن (sihah)؛ الدين أيضا العادة (tahdhib)؛ الحال والأمر الذي تعهده (maqayis)
- **B006** kent — kent; yöneticilerin buyruğuna uyulan yer olarak açıklanan büyük yerleşim
  المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)؛ ومنه سمى المصر مدينة (sihah)؛ جعل بعضهم المدينة من هذا الباب (mufradat)
- **B007** kişiyi sözüne ve vicdani sorumluluğuna göre değerlendirme — onu vicdani yükümlülüğüyle baş başa bıraktı · yargıda veya Tanrı'yla arasındaki konuda sözünü doğru kabul etti · yeminini kendi niyetine göre değerlendirdi
  دينت الرجل تديينا إذا وكلته إلى دينه (sihah)؛ دينت الرجل في القضاء وفيما بينه وبين الله أي صدقته (tahdhib)؛ دينت الحالف أي نويته فيما حلف وهو التديين (tahdhib)

## ح ق ق (root_000347): 61:9 ٱلْحَقِّ

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

## ظ ه ر (root_000970): 61:9 لِيُظْهِرَهُۥ, 61:14 ظَٰهِرِينَ

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

## ك ل ل (root_001315): 61:9 كُلِّهِۦ

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

## ش ر ك (root_000791): 61:9 ٱلْمُشْرِكُونَ

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

## د ل ل (root_000484): 61:10 أَدُلُّكُمْ

- **B001** bir şeyi belirtiyle anlaşılır kılma — bir şeyi belirtiyle anlaşılır kılma veya bilgiye ulaştırma · kendisiyle sonuca ulaşılan kanıt veya yol gösteren kimse · gösteren veya bilgiye ulaştıran kimse · birine yolu göstermek · kanıt veya yol gösterici · yolu tanıyıp doğru yöne gitmek
  إبانة الشيء بأمارة تتعلمها والدليل الأمارة في الشيء (maqayis)؛ الدليل ما يستدل به ودله على الطريق (sihah)؛ دل إذا هدى ودللت بهذا الطريق دلالة (tahdhib)؛ الدلالة ما يتوصل به إلى معرفة الشيء (mufradat)
- **B002** denge bulamadan gidip gelme — sarkarak sallanmak veya düzensizce hareket etmek · düzensizlik ve iki seçenek arasında gidip gelme · iki taraf arasında kararsız kalan topluluk
  تدلدل الشيء إذا اضطرب ودلدال بين القسوط وبين الدين (maqayis)؛ تدلدل الشيء أي تحرك متدليا والدلدال الاضطراب (sihah)؛ وقع القوم في دلدال وبلبال إذا اضطرب أمرهم وتذبذب وتدلدل الشيء إذا تحرك (tahdhib)
- **B003** beğenilen görünüş ve tavır — beğenilen görünüş, ağırbaşlı tavır ve hoş konuşma · kadının kendinden emin ve nazlı tavrı · kadının eşine karşı nazlı ve çekinmez davranması
  دلال المرأة جرأتها في تغنج وشكل (maqayis)؛ الدل الغنج والشكل وحسنة الدل والدلال (sihah)؛ هديه ودله من السكينة والوقار في الهيئة والمنظر والشمائل والدل حسن الحديث وحسن المزح والهيئة (tahdhib)
- **B004** bir dayanağa güvenme veya onu öne sürerek çekinmeden davranma — savaşta benzerlerine karşı üstünlük ve gözüpeklik göstermek · birine güvenip dayanmak · birine karşı cüretli davranmak · yaptığı iyiliği başa kakma veya yakınlığına güvenerek çekinmeme · yaptığı işle övünüp onu başa kakan kişi · gözüpekliğine güvenerek atılgan davranan kişi · ortada neden yokken karşısındakini suçlayan kişi
  فلان يدل على أقرانه في الحرب كالبازي يدل على صيده (maqayis;sihah;tahdhib)؛ وهو يدل بفلان أي يثق به (sihah)؛ الدلة ممن يدل على من له عنده منزلة شبه جراءة منه والدل المنة والأدل المنان بعمله ودل إذا افتخر (tahdhib)
- **B005** kılıç kınıyla vurmak — kılıç kınıyla vurmak
  أدل يدل إذا ضرب بقرابه (maqayis)
- **B006** kirpi, özellikle iri kirpi — kirpi veya özellikle iri kirpi
  الدلدل عظيم القنافذ (sihah)؛ الدلدل والشيهم والأزيب من أسماء القنفذ (tahdhib)

## ت ج ر (root_000176): 61:10 تِجَٰرَةٍ

- **B001** kazanc amacli alis satis — kazanc icin mal alip satmak · kazanc icin alis satis isine girmek · sermayeyi kazanc icin alip satma isi · alis satisla ugrasan kimse · alis satisla ugrasan kimseler toplulugu · alis satis yapan kimseler · alis satisinda kar etmek
  التجارة معروفة (maqayis)؛ وقد تجر تجارة (ayn;tahdhib)؛ تجر يتجر تجرا وتجارة (sihah)؛ التجارة التصرف في رأس المال طلبا للربح (mufradat)؛ ربح فلان في تجارته (tahdhib)
- **B002** alis satis yeri [kalıp] — alis satis icin gidilen veya bu isin yapildigi yer
  أرض متجرة يتجر إليها (ayn;tahdhib)؛ أرض متجرة يتجر فيها (sihah)
- **B003** pazarda ragbet goren deve [kalıp] — satisa ciktiginda kolay alici bulan disi deve · pazarda ragbet goren disi deve · satista kolay alici bulan develer
  ناقة تاجرة للنافقة وأخرى كاسدة (sihah)؛ ناقة تاجر أي نافقة في التجارة والسوق (sihah)؛ ناقة تاجرة إذا كانت تنفق إذا عرضت على البيع لنجابتها ونوق تواجر (tahdhib)
- **B004** kazanc yolunu bilen usta [kalıp] — o konuda usta · bir seyi iyi bilen ve ondan kazanc saglama yolunu taniyan
  إنه لتاجر بذلك الأمر أي حاذق به (tahdhib)؛ فلان تاجر بكذا أي حاذق به عارف الوجه المكتسب منه (mufradat)

## ن ج و (root_001476): 61:10 تُنجِيكُم

- **B001** ayrilarak kurtulma — serden ayrilip kurtulmak · baskasini kurtarmak · kurtulus sebebi
  ينجو من شيء بذهاب عنه (maqayis)؛ نجا فلان من الشر ينجو نجاة (ayn)؛ نجوت من كذا نجاء ونجاة وأنجيت غيري ونجيته (sihah)؛ نجا الرجل من الشر ينجو نجوا أو نجاة (tahdhib)؛ أصل النجاء الانفصال من الشيء ومنه نجا فلان من فلان وأنجيته ونجيته (mufradat)
- **B002** hizla gitme — hizlanip one gecmek · hizli deve · yolda acele etmek
  نجا الإنسان ينجو نجاة ونجاء في السرعة؛ ناقة ناجية ونجاة سريعة (maqayis)؛ نجا ينجو في السرعة نجاء فهو ناج وناقة ناجية سريعة (ayn)؛ نجوت أيضا نجاء أي أسرعت وسبقت (sihah)؛ النجاء النجاء؛ استنجوا معناه أسرعوا السير (tahdhib)
- **B003** soyup ayirma — deriyi kaziyip yuzmek · dali agactan kesip almak · ince cubugu agactan kesmek · agaci kokunden kesmek · soyulmus dal veya cubuklar · teli cekip ayirmak
  نجوت الجلد أنجوه والجلد نجا إذا كشطته؛ يستنجي من شجرها العصي؛ أنجني عصا (maqayis)؛ نجوت العود إذا اقتضبته من الشجرة؛ نجوت الجلد عن الناقة إذا كشطته (jamhara)؛ نجوت جلد البعير عنه وأنجيته إذا سلخته؛ النجاة الغصن (sihah)؛ أنجيت قضيبا من الشجرة؛ نجوت الوتر واستنجيته إذا خلصته (tahdhib)؛ نجوت قشر الشجرة وجلد الشاة؛ النجا عيدان قد قشرت (mufradat)
- **B004** sel basmaz yuksek yer — sel basmaz yuksek yer · selden korunmus yuksek arazi · arazide genis aciklik · arazisini su basmasin diye yukseltmek
  النجاة والنجوة من الأرض وهي التي لا يعلوها سيل؛ بيني وبينهم نجاوة من الأرض أي سعة (maqayis)؛ النجاة النجوة من الأرض أي الارتفاع لا يعلوه الماء (ayn)؛ النجوة الربوة من الأرض (jamhara)؛ النجوة والنجاة المكان المرتفع الذي تظن أنه نجاؤك لا يعلوه السيل (sihah)؛ كل سند مشرف لا يعلوه السيل فهو نجوة من الأرض (tahdhib)؛ النجوة والنجاة المكان المرتفع المنفصل بارتفاعه عما حوله (mufradat)
- **B005** gizli konusma — gizli konusma veya sir · biriyle gizlice konusmak · kendi aralarinda sirlasmak · birini sir icin ayirmak · gizli konusma arkadasi
  النجو والنجوى السر بين اثنين وناجيته وتناجوا وانتجوا (maqayis)؛ النجو كلام بين اثنين كالسر والتسار (ayn)؛ النجوى الكلام المسر؛ نجوت الرجل إذا أقعدته نجيا لتناجيه (jamhara)؛ النجو السر بين اثنين؛ ناجيته؛ تناجوا؛ انتجيته (sihah)؛ النجوى في الكلام ما يتفرد به الجماعة والاثنان (tahdhib)؛ ناجيته أي ساررته؛ انتجيت فلانا استخلصته لسري (mufradat)
- **B006** bedensel cikinti ve temizlenme — tuvalet sonrasi temizlenmek · bedenden cikan diski veya gaz · bedenden cikinti cikarmak · ilacin bagirsaklari bosaltmasi
  استنجى إذا أراد قضاء حاجته أتى نجوة من الأرض تستره (maqayis)؛ الاستنجاء التنظف بمدر أو ماء؛ النجو ما خرج من البطن من ريح وغيرها؛ النجو استطلاق البطن (ayn)؛ النجو كناية عن ذي البطن؛ احتبس نجوه في بطنه؛ استنجى (jamhara)؛ النجو ما يخرج من البطن؛ استنجى أي مسح موضع النجو أو غسله؛ شرب دواء فما أنجاه (sihah)؛ النجو العذرة نفسها؛ استنجيت بالماء الحجارة أي تطهرت بها؛ أنجى إذا عرق؛ أنجاني الدواء أي أقعدني (tahdhib)؛ كني عما يخرج من الإنسان بالنجو؛ الاستنجاء تحري إزالة النجو أو طلب نجوة لإلقاء الأذى (mufradat)
- **B007** bulut adi [kalıp] — durumu tartismali bulut adi · bulutun uzaklasmasi
  النجو السحاب والجمع النجاء وهو من انكشافه؛ أنجت السحابة ولت (maqayis)؛ نجو السحاب أول ما ينشأ والجميع النجاء (ayn)؛ النجو السحاب والجمع نجاء (jamhara)؛ النجو السحاب الذي هراق ماءه؛ أنجت السحابة إذا ولت (sihah)؛ النجو السحاب الذي هراق ماءه (tahdhib)
- **B008** agiz kokusunu sinama [kalıp] — birinin agiz kokusunu sinamak
  نجوت فلانا استنكهته (maqayis)؛ نجوته استنهكته (ayn)؛ نجوت فلانا إذا استنكهته (sihah)؛ نجوت فلانا إذا استنكهته (tahdhib)؛ فليس في البيت حجة له وإنما أراد أني ساررته (mufradat)
- **B009** gerinme — gerinme
  النجواء التمطي مثل المطواء

## ع ذ ب (root_000994): 61:10 عَذَابٍ

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

## ء ل م (root_000046): 61:10 أَلِيمٍ

- **B001** acı duyma — acı; bazı aktarımlarda şiddetli acı · acı duymak veya ağrı çekmek · acı içinde olan, acıya uğramış · acı çekme ve acıdan yakınma · karna ya da kişinin iç varlığına acı isabet etmesi · acı; özellikle acı bulunmadığını söyleyen kullanımda
  أصل واحد وهو الوجع (maqayis)؛ الألم الوجع والفعل من الألم ألم (maqayis)؛ الألم الوجع والفعل ألم يألم ألما فهو ألم (ayn;sihah;tahdhib)؛ الألم الوجع الشديد يقال ألم يألم ألما فهو آلم (mufradat)؛ التألم التوجع (sihah)؛ تألم فلان من فلان إذا تشكى منه وتوجع (tahdhib)؛ ألمت بطنك أي ألم بطنك (sihah;tahdhib)؛ ألمت نفسك كما تقول سفهت نفسك (maqayis)
- **B002** acı verme — acı vermek, başkasını incitmek · acı verici, incitici · acı veren, inciten
  المجاوز أليم فهو فعيل بمعنى مفعل (maqayis)؛ عذاب أليم أي مؤلم ورجل أليم ومؤلم أي موجع (maqayis)؛ المؤلم الموجع والمجاوز آلم يؤلم إيلاما فهو مؤلم (ayn)؛ الإيلام الإيجاع والأليم الموجع (sihah)؛ عذاب أليم فهو بمعنى مؤلم ومنه رجل وجع وضرب وجع أي موجع (tahdhib)؛ آلمت فلانا وعذاب أليم أي مؤلم (mufradat)

## ج ه د (root_000268): 61:11 وَتُجَٰهِدُونَ

- **B001** gücün sonuna dek çaba gösterme ve güçlüğe katlanma — güç, yeterlik ve erişilebilen sınır · güçlük, sıkıntı ve yorucu durum · gücünün ve yapabileceklerinin sonuna varmak · düşüncesini ve kendini son sınırına kadar zorlamak · bütün gücünü ortaya koyup güçlüğe katlanma · dar ve sıkıntılı geçim; az bir şeyle yaşama · yemini elinden geldiğince güçlü biçimde pekiştirme · işine sıkıca sarılıp elinden geleni yapan kişi
  أصله المشقة والجهد الطاقة (maqayis)؛ ما جهد الإنسان من مرض أو أمر شاق وبلوغك غاية الأمر (ayn;tahdhib)؛ بلغ أقصى قوته وطوقه وجاد فيه (jamhara)؛ الطاقة والمشقة وبذل الوسع والمجهود (sihah)؛ الطاقة والمشقة وأقسموا بالله جهد أيمانهم والاجتهاد أخذ النفس ببذل الطاقة وتحمل المشقة (mufradat)
- **B002** düşmana karşı bütün gücüyle direnme veya savaşma — düşmana karşı bütün gücüyle direnme veya savaşma · düşmanla savaşmak veya ona var gücüyle karşı koymak
  جاهدت العدو مجاهدة وهو قتالك إياه (ayn)؛ جاهد في سبيل الله مجاهدة وجهادا (sihah)؛ جاهدت العدو مجاهدة (tahdhib)؛ الجهاد والمجاهدة استفراغ الوسع في مدافعة العدو والجهاد ثلاثة أضرب (mufradat)
- **B003** birini gücünün sınırına dek zorlama — birini gücünün sınırına dek zorlamak · hayvanı yolculukta gücünün üstünde sürmek · bize karşı düşmanlıkta aşırıya gidip baskıyı artırmak
  جهدت فلانا بلغت مشقته وأجهدته على أن يفعل كذا وأجهد القوم علينا في العداوة (ayn;tahdhib)؛ جهدت الرجل إذا حملته على أن يبلغ مجهوده (jamhara)؛ جهد دابته وأجهدها إذا حمل عليها في السير فوق طاقتها (sihah)
- **B004** sert, açık ya da bitkisiz arazi — sert veya çok düz arazi · açık, boş ya da bitkisiz kıraç arazi
  الجهاد وهي الأرض الصلبة (maqayis)؛ الجهاد بالفتح الأرض الصلبة (sihah)؛ الجهاد أظهر الأرض وأسواها وأرض فضاء وجهاد وبراز بمعنى واحد والجماد والجهاد الأرض الجدبة التي لا شيء فيها (tahdhib)
- **B005** bir kaynağı özünü alarak, seyrelterek ya da kullanarak tüketme — sütün yağını çıkarmak veya su ve sağmayla sütü zayıflatmak · hayvanların sürekli otlayıp tükettiği otlak · malını oraya buraya vererek azaltmak veya tüketmek
  المجهود اللبن الذي أخرج زبده ولا يكاد ذلك يكون إلا بمشقة ونصب ومرعى جهيد جهده المال (maqayis)؛ جهدت اللبن فهو مجهود أي أخرجت زبده كله ومرعى جهيد جهده المال (sihah)؛ كل لبن شد مذقه بالماء فهو مجهود ولا يجهدها الحلب فينهك لبنها وهذا كلأ يجهده المال ولا يجهد الرجل ماله (tahdhib)
- **B006** yiyeceğe güçlü istek duyma veya ona yüklenip çok yeme — yiyeceği veya içeceği çok isteyip ona ısrarla yönelmek · yiyeceğe yüklenip çok ve şiddetli biçimde yemek · isteği çok güçlü olan kimse
  فلان يجهد الطعام إذا حمل عليه بالأكل الكثير الشديد والجاهد الشهوان (maqayis)؛ جهدت الطعام اشتهيته والجاهد الشهوان وجهدت الطعام إذا أكثرت من أكله (sihah)؛ مجهود المشتهى الذي يلح عليه في الشرب لطيبه وحلاوته (tahdhib)
- **B007** belirip görünür, açık veya erişilebilir hale gelme — saçına ak düşmek ve ağarma çoğalmak · yolun veya gerçeğin belirip açık hale gelmesi · işin önüne çıkıp yapılabilir hale gelmesi · topluluğun görünür hale gelip görüş alanına çıkması
  أجهد فيه الشيب إجهادا إذا بدا فيه وكثر؛ أجهد لك الطريق وأجهد لك الحق برز وظهر ووضح؛ أجهد لك هذا الأمر فاركبه أي أمكنك وأعرض لك؛ أجهد القوم لي أي أشرفوا (tahdhib)

## م و ل (root_001457): 61:11 بِأَمْوَٰلِكُمْ

- **B001** varlık; edinme, çoğalma ve başkasına kazandırma — kişinin sahip olduğu değerli varlık · kişinin sahip olduğu değerli varlıklar · göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri · varlık sahibi veya çok varlıklı kimse · kendine kalıcı varlık edinmek · varlığı çoğalmak veya varlık sahibi duruma gelmek · birini varlık sahibi yapmak veya ona değerli varlık vermek · mal sözcüğünün küçültme biçimi · ne çok varlığı var!
  تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)
- **B002** örümcek için tartışmalı bir ad — 
  إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)

## ن ف س (root_001533): 61:11 وَأَنفُسِكُمْ

- **B001** soluk alıp verme — soluk alıp verme · gövdeye girip çıkan hava; soluk · tek soluk ya da soluklanma arası · soluklar
  التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)
- **B002** sıkıntıyı hafifletip ferahlatma — Tanrı onun sıkıntısını giderdi · beni sıkıntıdan kurtarıp rahatlat · Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı
  نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)
- **B003** kem gözle zarar verme — zarar verdiğine inanılan bakış · ona kem göz değdi · kem gözle zarar veren kişi
  يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)
- **B004** canlıdaki akışkan kan — kaybıyla yaşamın da yitirildiği kan · hayvandaki akışkan kan
  النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)
- **B005** doğum ve doğuma bağlı kadın-çocuk durumu — doğum yapmış ya da doğum sonrası kanaması olan kadın · doğum ve doğum sonrası kanama dönemi · yeni doğan çocuk · doğmadan önce
  الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)
- **B006** soluk aralı içim ve bir içimlik yudum — bir solukta alınan yudum ya da içim · üç soluk arasıyla içme
  كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)
- **B007** bir deri işlemeye yetecek sepi maddesi payı — deriyi bir kez işlemeye yetecek sepi maddesi · bir işlemelik sepi maddesi payı
  في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)
- **B008** yaşamı sürdüren, bol ve doyurucu su — yaşamı ayakta tutan su · bol ve susuzluğu gideren içecek · tadı kötü, bayat ve içimi güç içecek
  يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)
- **B009** kalıba bağlı yarılıp açılma ve genişleme [kalıp] — yay çatladı ya da yarıldı · sabah söktü, aydınlık yayıldı · gündüz uzayıp genişledi · ırmağın suyu artıp yayıldı
  تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)
- **B010** değerli ve uğrunda yarışılan şey — değerli, önemli ve arzulanan · bir şeyi elde etme ya da üstünlere benzeme yarışı · başkasına vermeye kıyamayıp esirgemek · sahip olduğu şey yüzünden onu kıskanmak
  شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)
- **B011** bedene yaşam veren can — bedene yaşam veren can · insan ya da canlı birey
  النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)
- **B012** şeyin kendisi ve bütün öz varlığı [kalıp] — şeyin tam kendisi ve gerçeği · başkası aracılığıyla değil, bizzat kendisi
  كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)
- **B013** iç düşünce, niyet ve ayırt etme gücü — onun içinden geçen düşünce ya da niyet · ayırt etmeyi sağlayan zihinsel güç
  نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)
- **B014** sağlam, cömert ve onurlu yaradılış — sağlam karakterli, dayanıklı ve cömert adam · büyüklük duygusu, onur, yüksek amaç ve kendine saygı
  رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)
- **B015** uzaklık, genişlik ve zaman payı — işinde rahat hareket edecek genişlikte · ek süre ya da hareket alanı · daha uzak, daha uzun ya da daha geniş
  هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)
- **B016** eski bahis oyunundaki beşinci pay oku — eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok
  النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)

## خ ي ر (root_000452): 61:11 خَيْرٌ

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

## ك و ن (root_001332): 61:11 كُنتُمْ, 61:14 كُونُوٓا۟

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

## غ ف ر (root_001096): 61:12 يَغْفِرْ

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

## ذ ن ب (root_000521): 61:12 ذُنُوبَكُمْ

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

## د خ ل (root_000464): 61:12 وَيُدْخِلْكُمْ

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

## ج ن ن (root_000266): 61:12 جَنَّٰتٍ, 61:12 جَنَّٰتِ

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

## ج ر ي (root_000240): 61:12 تَجْرِى

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

## ت ح ت (root_000177): 61:12 تَحْتِهَا

- **B001** alt konum — alt, altinda kalan yer
  تحت الشيء (maqayis)؛ تحت نقيض فوق (tahdhib)؛ تحت مقابل لفوق (mufradat)؛ يستعمل في المنفصل (mufradat)
- **B002** itibarsiz dusuk kimseler — dusuk ve itibarsiz kimseler
  التَّحوت الدون من الناس (maqayis)؛ الذين كانوا تحت أقدام الناس لا يؤبه لهم وهم السفل والأنذال (tahdhib)؛ الأراذل من الناس (mufradat)

## ن ه ر (root_001559): 61:12 ٱلْأَنْهَٰرُ

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

## س ك ن (root_000726): 61:12 وَمَسَٰكِنَ

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

## ط ي ب (root_000961): 61:12 طَيِّبَةً

- **B001** bağlama göre hoş, temiz, iyi veya dinen izinli olan — hoş, iyi veya temiz duruma gelmek; öyle olmak · kötünün karşıtı olan hoş, temiz ve iyi şey · kullanılmasına veya tüketilmesine izin verilen · yenmesine izin verilen, hoş ve insana dokunmayan yiyecek · bilgisizlikten ve kötü davranışlardan arınmış, inançlı ve iyi insan · üzerinde pislik bulunmayan temiz toprak · hoş, temiz ve iyi olan · son derece hoş ve iyi
  الطيب ضد الخبيث (maqayis)؛ طاب يطيب طيبا فهو طيب (ayn;mufradat)؛ الطيب خلاف الخبيث (jamhara;sihah)؛ أصل الطيب ما تستلذه الحواس وما تستلذه النفس (mufradat)؛ الطعام الطيب في الشرع ما كان متناولا من حيث ما يجوز (mufradat)؛ الطيب من الإنسان من تعرى من نجاسة الجهل والفسق (mufradat)؛ صعيدا طيبا أي ترابا لا نجاسة به (mufradat)؛ الطاب الطيب (maqayis;sihah;mufradat)؛ شيء طياب أي طيب جدا (sihah)
- **B002** aldatmasız ve antlaşmayı bozmadan tutsak alma [kalıp] — aldatma veya antlaşmayı bozma olmadan gerçekleştirilen tutsak alma
  سبي طيبة أي طيب (maqayis)؛ سبي طيبة صحيح السباء لم يكن عن غدر ولا نقض عهد (sihah)
- **B003** tuvalet sonrası pisliği gidererek temizlenme — tuvalet sonrasında bedendeki pisliği giderip temizlenme
  الاستطابة الاستنجاء لأن الرجل يطيب نفسه مما عليه من الخبث بالاستنجاء (maqayis)؛ الاستطابة أيضا الاستنجاء (sihah)؛ سمي الاستنجاء استطابة لما فيه من التطيب والتطهر (mufradat)
- **B004** yeme ile cinsel birlikteliği birlikte adlandıran ikili — yeme ve cinsel birlikteliği birlikte gösteren ikili ifade
  الأطيبان الأكل والنكاح (maqayis)؛ الأطيبان الأكل والجماع (sihah)؛ قيل الأطيبان الأكل والنكاح (mufradat)
- **B005** Peygamber'in şehri için kullanılan özel ad — Peygamber'in şehri için kullanılan özel ad
  طيبة مدينة الرسول (maqayis)؛ المدينة تسمى طيبة (jamhara)؛ طيبة اسم مدينة الرسول (sihah)؛ سميت المدينة طيبة (mufradat)
- **B006** içten razı olma ve iç rahatlığı bulma [kalıp] — kendi isteğimle, hiçbir baskı görmeden · içime sindi ve ondan hoşnut oldum · iç rahatlatan, insana ferahlık veren şey
  هذا طعام مطيبة للنفس (maqayis)؛ فعلت ذاك بطيبة نفسي إذا لم يكرهك عليه أحد (sihah)؛ طبت به نفسا أي طابت نفسي به (sihah)؛ طعام مطيبة للنفس إذا طابت به النفس (mufradat)
- **B007** güzel koku sürünmek için kullanılan koku maddesi — güzel koku sürünmek için kullanılan koku maddesi
  الطيب ما يتطيب به (sihah)؛ ما به من الطيب (sihah)
- **B008** biriyle şakalaşıp hoşça takılmak — biriyle şakalaşmak ve ona hoşça takılmak
  طايبه أي مازحه (sihah)
- **B009** sonsuz mutluluk yurdundaki özel ağaç veya bütün güzel şeyler — sonsuz mutluluk yurdundaki özel bir ağaç ya da oradaki bütün güzel şeyler
  طوبى فعلى من الطيب (sihah)؛ طوبى اسم شجرة في الجنة (sihah)؛ طوبى لهم قيل هو اسم شجرة في الجنة وقيل بل إشارة إلى كل مستطاب في الجنة (mufradat)

## ف و ز (root_001186): 61:12 ٱلْفَوْزُ

- **B001** iyiliğe erişip kötülükten kurtulma — iyiliğe erişip kötülükten kurtulma · kurtulup iyiliğe erişmek · kurtulup iyiliğe erişen kimse · bir şeyi ele geçirip onunla uzaklaşmak · Tanrı'nın ona bir şeyi alıp götürtmesi · kumarda kura payının sahibine çıkması
  الفوز الظفر بالخير والنجاة من الشر (ayn;sihah;tahdhib;mufradat)؛ فاز بالأمر إذا ذهب به وخلص (maqayis;sihah)؛ إذا خرج قدح قوم في القمار قيل قد فاز (ayn;tahdhib)
- **B002** ölüp dünyadan ayrılma — ölmek, yaşamını yitirmek
  فوز الرجل إذا مات (maqayis;sihah;tahdhib)؛ فوز الرجل إذا هلك (mufradat)؛ صار في مفازة بين الدنيا والآخرة (ayn;tahdhib)
- **B003** kurtuluş; susuz ve tehlikeli ıssız çöl — susuz çöle girip orada yol almak · cezadan kurtuluş · susuz, ölüm tehlikesi taşıyan ıssız çöl · kurtuluş veya kurtuluş yeri
  المفازة المنجاة (maqayis;ayn;sihah;tahdhib)؛ المفازة الفلاة التي لا ماء فيها (tahdhib)؛ سميت مفازة تفاؤلا بالسلامة والفوز (maqayis;sihah;mufradat)؛ سميت من فوز إذا هلك (maqayis;sihah;mufradat)؛ فوز الرجل تفويزا ركب المفازة ومضى فيها (ayn;tahdhib)
- **B004** askerî konak yerinde kurulan yapı veya direkli gölgelik — askerî konak yerinde kurulan yapı veya direkli gölgelik
  الفازة من أبنية الحزق وغيرها تبنى في العساكر (ayn;tahdhib)؛ الفازة مظلة تمد بعمود (sihah)

## ع ظ م (root_001029): 61:12 ٱلْعَظِيمُ

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

## ء خ ر (root_000019): 61:13 وَأُخْرَىٰ

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ن ص ر (root_001510): 61:13 نَصْرٌ, 61:14 أَنصَارَ, 61:14 أَنصَارِىٓ, 61:14 أَنصَارُ

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

## ف ت ح (root_001124): 61:13 وَفَتْحٌ

- **B001** fiziksel açma, açılma ve geniş açıklık — fiziksel açma ve kapalılığı giderme · kapıyı, kilidi veya kapalı eşyayı açmak · açılmak; çiçeğin açması · geniş ve açık kapı · ağzı geniş, tıpasız ve kılıfsız şişe · açıklık veya gedik · idrar yolu geniş dişi deve
  خلاف الإغلاق ونقيض الإغلاق (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ فتحت الباب وغيره فتحا (maqayis;sihah)؛ كل شيء انكشف عن شيء فقد انفتح عنه ومنه تفتح النور (jamhara)؛ باب فتح أي واسع مفتوح (maqayis;ayn;sihah;tahdhib;mufradat)؛ قارورة فتح واسعة الرأس والفتحة الفرجة والفتوح الناقة الواسعة الإحليل (sihah;tahdhib)
- **B002** sonrasını başlatan ilk bölüm veya eylem — bir şeyin başlangıcı ve ilk bölümü · kitabın açılış bölümü · kutsal metindeki bölümlerin başlangıçları · ibadeti başlatan ilk yüceltme sözü · bir şeye başlamak ve girişmek
  فواتح القرآن أوائل السور (maqayis;ayn;tahdhib)؛ كل ما بدأت به فقد استفتحته وبه سميت الحمد فاتحة الكتاب (jamhara)؛ فاتحة الشيء أوله (sihah)؛ فاتحة كل شيء مبدؤه الذي يفتح به ما بعده وافتتح فلان كذا إذا ابتدأ به (mufradat)؛ افتتاح الصلاة التكبيرة الأولى (ayn)
- **B003** uyuşmazlığı hükümle çözüme bağlama — çekişen taraflar arasında hüküm vermek · hüküm ve yargı işi · hükmeden ve karar veren · hükmeden yargıç
  الفتح والفتاحة الحكم والله الفاتح أي الحاكم (maqayis)؛ الفتح أن تحكم بين قوم يختصمون إليك والفتاح الحاكم (ayn)؛ فتح فلان بين بني فلان إذا حكم بينهم والفتاح العليم (jamhara)؛ افتح بيننا أي احكم والفتاحة الحكم (sihah)؛ الفتاح الحكومة والقاضي لأنه يفتح مواضع الحق (tahdhib)؛ فتح القضية فتاحا فصل الأمر فيها وأزال الإغلاق عنها (mufradat)
- **B004** üstün gelerek zafere ulaşma — zafer, üstün gelme veya savaşta ele geçirme · düşman ülkesini yenerek ele geçirmek · Tanrı'dan birine karşı zafer istemek
  الفتح النصر والإظفار واستفتحت استنصرت (maqayis)؛ الفتح افتتاح دار الحرب والفتح النصرة واستفتحت الله سألته النصر (ayn)؛ الاستفتاح الاستنصار والفتح النصر (sihah)؛ إن تستنصروا فقد جاءكم النصر (tahdhib)؛ يحتمل النصرة والظفر والاستفتاح طلب الفتح أو الفتاح وطلب الظفر (mufradat)
- **B005** kaynaktan çıkıp akan su — kaynaktan çıkan veya akarsuda ilerleyen su · nehir suyuyla sulanan ekin veya hurmalık · mevsim yağmurlarının ilki
  الفتح الماء يخرج من عين أو غيرها (maqayis)؛ الفتح الماء يجري من عين أو غيرها (sihah)؛ الفتح النهر وما جرى في الأنهار من الماء وما سقي فتحا وأول مطر الوسمي الفتوح (tahdhib)
- **B006** kapalıyı açan araç — kapıyı, kilidi veya başka bir kapalı şeyi açan anahtar · kilitli olanı açmaya yarayan araç · bilinmeyene erişmeyi sağlayan yollar
  المفاتيح جمع المفتاح الذي يفتح به المغلاق (ayn)؛ المفتاح معروف (jamhara)؛ المفتاح مفتاح الباب وكل مستغلق (sihah)؛ الذي يفتح به المغلاق مفتح بكسر الميم ومفتاح (tahdhib)؛ المفتح والمفتاح ما يفتح به ومفاتح الغيب ما يتوصل به إلى غيبه (mufradat)
- **B007** servet saklanan yer veya içindeki servet — servet saklanan yer veya gömü · servet depoları, gömüler veya bunlardaki mallar
  المفتح الخزانة ومفاتحه الكنوز وصنوف أمواله (ayn)؛ المفتح الكنز ومفاتحه كنوزه (jamhara)؛ المفتح الخزانة ومفاتحه كنوزه وخزائنه وما في الخزائن من مال (tahdhib)؛ مفاتح خزائنه وقيل الخزائن أنفسها (mufradat)
- **B008** güçlüğü giderme ve bilgiyi erişilir kılma [kalıp] — kaygıyı veya sıkıntıyı gidermek · bir şeyi bildirip kavratmak · anlaşılması güç bir bilgi alanını açıklığa kavuşturmak · okuyan kişiye takıldığı yeri söylemek
  الفتح أن تفتح على من يستقرئك (ayn)؛ إزالة الإغلاق والإشكال وما يدرك بالبصيرة كفتح الهم وإزالة الغم وفقر يزال بإعطاء المال وفتح المستغلق من العلوم وفتح عليه كذا إذا أعلمه ووقفه عليه (mufradat)
- **B009** serveti veya bilgisiyle böbürlenme — serveti veya bilgisiyle böbürlenme
  الفتحة تفتح الإنسان بما عنده من أموال أو أدب يتطاول به (ayn)؛ الفتحة التيه والتكبر وأحسبها مولدة (jamhara)؛ الفتحة تفتح الإنسان بما عنده من ملك أو أدب يتطاول به (tahdhib)

## ق ر ب (root_001212): 61:13 قَرِيبٌ

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

## ح و ر (root_000369): 61:14 لِلْحَوَارِيِّۦنَ, 61:14 ٱلْحَوَارِيُّونَ

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

## ط و ف (root_000957): 61:14 طَّآئِفَةٌ, 61:14 طَّآئِفَةٌ

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

## ع د و (root_000993): 61:14 عَدُوِّهِمْ

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

## ECHO ع د د (root_000989): for 61:14 عَدُوِّهِمْ: withheld observed target; not identity

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

## ECHO ع و د (root_001058): for 61:14 عَدُوِّهِمْ: withheld observed target; not identity

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

## ص ب ح (root_000839): 61:14 فَأَصْبَحُوا۟

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



===== _commentary/v16/work/s061/surah.r2/channels.md =====
(source: latent_activation/network/v3/reviews/s061/reader_a_pilot.md)

# s061 Semantic Channel Discovery

## Parent Channels

### 1. Commitment Becomes Action
- Semantic invariant: An inward or spoken commitment becomes sound only when it is transferred into a corresponding act and sustained under strain.
- Surface relation: direct; 61:2-3 opposes saying to doing, while 61:11 and 61:14 turn belief into exertion and pledged support.
- Surprising reach: Truth is not only propositional: it behaves like an obligation that must be carried, handed over, defended, and made operative.

#### Subchannel A. Word Answered by Deed
- Reading type: mixed
- Scene or process: A spoken claim is tested against enacted work, fulfilled promise, and fixed reality; falsehood is the failure of that correspondence.
- Active motifs: uttered statement `quranic:root_001272:B001/m01`; enacted work `quranic:root_001167:B001/m01`; speech matching reality `quranic:root_000852:B001/m01`; promise realized in action `quranic:root_000852:B004/m01`; truth fixed against falsehood `quranic:root_000347:B001/m01`; lie contrary to truth `quranic:root_001290:B001/m01`
- Ayah anchors: 61:2-3 `تَقُولُ` (ق و ل) and `تَفْعَلُ` (ف ع ل); 61:6 `مُّصَدِّقًا` (ص د ق); 61:7 `كَذِبَ` (ك ذ ب); 61:9 `حَقِّ` (ح ق ق)
- Synthesis: The spoken word and the performed deed occupy matching roles: declaration proposes a reality, action verifies it, and fulfilled promise locks the two together. The rebuke in 61:2-3 is therefore materialized as a failed fit, whereas truth is a statement whose structure survives transfer into conduct.

#### Subchannel B. Trust Carried as a Pledge
- Reading type: mixed
- Scene or process: Belief settles into trust, creates a protected obligation, and is expressed by entrustment, handover, and the yielding hand.
- Active motifs: believing assent `quranic:root_000054:B002/m01`; obligation that must be defended `quranic:root_000347:B007/m01`; entrusting a person in judgment or oath `quranic:root_000504:B007/m01`; yielding or guaranteeing hand `quranic:root_001693:B006/m01`; handing something over and relinquishing it `quranic:root_000737:B012/m01`
- Ayah anchors: 61:2, 61:11, and 61:14 forms of `ءَامَنَ` (ء م ن); 61:9 `حَقِّ` (ح ق ق) and `دِينِ` (د ي ن); 61:6 `يَدَىَّ` (ي د ي); 61:7 `إِسْلَٰمِ` (س ل م)
- Synthesis: Faith is rendered as custody rather than bare assent. A truth received in trust becomes something owed protection; the hand then marks guarantee, surrender, and transfer. This gives the call to believe and become God's supporters the social force of a pledge placed into responsible hands.

#### Subchannel C. Intention Sustained Under Strain
- Reading type: mixed
- Scene or process: Desire becomes resolve, resolve rises into exertion, and capacity is measured by the hardship the self continues to bear.
- Active motifs: intention and directed will `quranic:root_000610:B001/m01`; rising to undertake an affair `quranic:root_001273:B003/m01`; exerting one's full capacity under hardship `quranic:root_000268:B001/m01`; strenuous effort `quranic:root_000076:B010/m01`; available power or capacity `quranic:root_000076:B011/m01`; vigor and fortitude of self `quranic:root_001533:B014/m01`
- Ayah anchors: 61:8 `يُرِيدُ` (ر و د); 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:11 `تُجَٰهِدُ` (ج ه د) and `أَنفُسِ` (ن ف س); surface anchor unavailable for ء ل ي
- Synthesis: The scene separates wanting, undertaking, and expending capacity. The hostile will of 61:8 and the believers' exertion in 61:11 are competing trajectories of intention; only the latter recruits the whole self and converts latent power into sustained action.

#### Subchannel D. Inner Word Passed to the Hand
- Reading type: mixed
- Scene or process: Intention forms within the heart and self, becomes an unspoken statement, passes through the tongue, and is finally owned as a deed of the hands.
- Active motifs: heart as the faculty of understanding `quranic:root_001248:B001/m02`; inward reason and intention `quranic:root_001533:B013/m01`; statement formed but not voiced `quranic:root_001272:B012/m01`; tongue as the instrument of speech `quranic:root_001272:B002/m01`; enacted work `quranic:root_001167:B001/m01`; deed attributed to one's hands `quranic:root_001693:B009/m01`
- Ayah anchors: 61:5 `قُلُوبَ` (ق ل ب); 61:11 `أَنفُسِ` (ن ف س); 61:2-3, 61:5-6, and 61:14 forms of `ق و ل`; 61:2-3 forms of `ف ع ل`; 61:6 `يَدَىَّ` (ي د ي)
- Synthesis: Saying and doing are stages in a single agency chain. The inward self frames a word, the tongue exposes it, and the hand receives responsibility for what follows. The rebuke of 61:2-3 therefore reaches behind audible speech to intention and forward into the bodily authorship of action.

### 2. Guided Orientation and Perception
- Semantic invariant: A destination becomes reachable when signs, direction, bodily orientation, and perception converge; deviation breaks that convergence.
- Surface relation: direct; guidance, path, deviation, arrival, and nearness are explicit in 61:5-7, 61:9-11, and 61:13.
- Surprising reach: The channel distinguishes having a visible organ, standing on a route, and actually seeing or following it; outward availability does not guarantee reception.

#### Subchannel A. The Waymarked Road
- Reading type: mixed
- Scene or process: A traveler enters a public route, meets its junctions and endpoint, and is gently directed by identifying marks, a leading vanguard, and a visible beacon.
- Active motifs: gentle direction to road and truth `quranic:root_001583:B001/m01`; settled direction and manner of proceeding `quranic:root_001583:B002/m01`; guide or vanguard at the leading edge `quranic:root_001583:B003/m01`; indication by a recognizable sign `quranic:root_000484:B001/m01`; traversable route `quranic:root_000672:B001/m01`; travelers who use the road `quranic:root_000672:B002/m01`; public road, junction, and final limit `quranic:root_000009:B010/m01`; waymark or boundary sign `quranic:root_001040:B002/m01`; guiding beacon `quranic:root_001564:B005/m01`; grooves and branches of a road `quranic:root_000791:B005/m01`
- Ayah anchors: 61:5, 61:7, and 61:9 forms of `ه د ي`; 61:10 `أَدُلُّ` (د ل ل); 61:4 and 61:11 `سَبِيلِ` (س ب ل); 61:6 `يَأْتِى` (ء ت ي); 61:5 and 61:11 `تَعْلَمُ` (ع ل م); 61:8 `نُور` (ن و ر); 61:9 `مُشْرِكُونَ` (ش ر ك)
- Synthesis: Guidance is assembled as a navigable environment: travelers supply the participants, a public road and its junctions supply continuity and choice, marks make it legible, and a vanguard fixes its forward edge. The invitation to a saving trade in 61:10 thus functions as route disclosure toward a known limit, not merely as instruction.

#### Subchannel B. Course Abandoned Beyond Its Limit
- Reading type: surface-primary
- Scene or process: A traveler resists a known straight course, inclines toward its side, reaches a bank or margin, and passes beyond it until departure becomes hostile transgression.
- Active motifs: inclination away from straightness `quranic:root_000658:B001/m01`; resisting known truth `quranic:root_001052:B001/m01`; leaving the common direction for a side `quranic:root_001052:B002/m01`; straight and balanced course `quranic:root_001273:B008/m01`; bank or lateral boundary `quranic:root_000993:B009/m01`; passing beyond the intended object `quranic:root_000993:B004/m01`; overstepping a limit in aggression `quranic:root_000993:B001/m01`
- Ayah anchors: 61:5 `زَاغُ` (ز ي غ) and `قَوْمِ` (ق و م); 61:3 `عِندَ` (ع ن د); 61:14 `عَدُوِّ` (ع د و)
- Synthesis: Deviation develops by degrees: resistance breaks orientation, a sideward lean reaches the route's margin, and crossing that margin turns divergence into aggression. The enemy of 61:14 is thus reframed as one whose relation to the right course is defined by exceeded limits, not mere distance.

#### Subchannel C. Hidden Heart Turned at Its Core
- Reading type: mixed
- Scene or process: The heart lies concealed in the chest as a center of understanding; deviation reaches that hidden core, turns its orientation, and settles there like an illness.
- Active motifs: anatomical heart `quranic:root_001248:B001/m01`; heart as the faculty of understanding `quranic:root_001248:B001/m02`; pure interior core `quranic:root_001248:B002/m01`; hidden heart within the breast `quranic:root_000266:B010/m01`; turning a thing from one face to another `quranic:root_001248:B004/m01`; establishing another's deviation `quranic:root_000658:B004/m01`; disease lodged in the heart `quranic:root_001248:B011/m01`
- Ayah anchors: 61:5 `قُلُوبَ` (ق ل ب) and `أَزَاغَ` (ز ي غ); 61:12 `جَنَّٰت` (ج ن ن)
- Synthesis: The causative movement in 61:5 is localized inside the body. A faculty meant to understand is physically reoriented at its concealed center, and repeated deviation acquires the persistence of disease. This separates the traveler's outward departure from the inward condition that the departure produces.

#### Subchannel D. The Eye That Stands but Does Not See
- Reading type: latent/lexical
- Scene or process: An outwardly present eye can be bright, protruding, filmed, fatigued, or structurally intact while its sight has departed.
- Active motifs: high-contrast eye `quranic:root_000369:B001/m01`; moving defect within the eye `quranic:root_000610:B007/m01`; intact-looking eye deprived of sight `quranic:root_001273:B021/m01`; protruding visible eye `quranic:root_000970:B009/m01`; woven film over the eye `quranic:root_000672:B010/m01`; gaze inclining and failing `quranic:root_000658:B002/m01`
- Ayah anchors: 61:14 `حَوَارِيُّونَ` (ح و ر); 61:8 `يُرِيدُ` (ر و د); 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:9 and 61:14 forms of `ظ ه ر`; 61:4 and 61:11 `سَبِيلِ` (س ب ل); 61:5 forms of `ز ي غ`
- Synthesis: The scene presses the difference between manifestation and apprehension. An eye may remain visibly in place while a film, fatigue, or inner defect disables sight. That bodily contrast reframes the rejection of clear signs in 61:6: evidence can be outwardly manifest without becoming inwardly seen.

#### Subchannel E. Distance Closed Into Presence
- Reading type: mixed
- Scene or process: Separation places an object at a distance; directed approach closes the interval until arrival becomes immediate presence.
- Active motifs: spatial or relational remoteness `quranic:root_000131:B001/m01`; actively putting distance between two sides `quranic:root_000131:B003/m01`; spatial and relational nearness `quranic:root_001212:B001/m01`; presence beside or before an object `quranic:root_001052:B004/m01`; arrival and reaching `quranic:root_000009:B001/m01`
- Ayah anchors: 61:6 `بَعْدِ` (ب ع د) and `يَأْتِى` (ء ت ي); 61:13 `قَرِيبٌ` (ق ر ب); 61:3 `عِندَ` (ع ن د)
- Synthesis: Nearness is the result of a changed relation, not merely a short measurement. Distance can be imposed, approach reverses it, and arrival converts remoteness into presence. The messenger's coming in 61:6 and the near opening of 61:13 consequently share a geometry of a closing interval.

#### Subchannel F. Matter Examined Until Known
- Reading type: mixed
- Scene or process: An unknown matter is found, turned over from every side, retained without a written aid, and resolved through accurate knowledge and judgment.
- Active motifs: disclosure of a thing to the knower `quranic:root_001040:B001/m01`; finding out and reaching knowledge `quranic:root_000970:B008/m01`; turning an affair outside and inside for examination `quranic:root_000970:B018/m01`; retention by heart without a book `quranic:root_000970:B019/m01`; wisdom as knowledge that reaches the right judgment `quranic:root_000348:B003/m01`
- Ayah anchors: 61:5 and 61:11 forms of `ع ل م`; 61:9 and 61:14 forms of `ظ ه ر`; 61:1 `حَكِيمُ` (ح ك م)
- Synthesis: Knowing is staged as inquiry rather than passive possession. Discovery brings the matter within reach, examination rotates it through multiple faces, memory holds it, and wisdom fixes the fitting judgment. This process intensifies the culpability of rejecting the clear signs in 61:6 after they have become examinable.

#### Subchannel G. Succession From Before to After
- Reading type: mixed
- Scene or process: A prior object stands before a bearer; a later event is prepared, follows its predecessor, approaches its time, and is brought into presence.
- Active motifs: what stands ahead or immediately before `quranic:root_001693:B008/m01`; an affair becoming accessible and prepared `quranic:root_000009:B003/m01`; coming into presence `quranic:root_000281:B001/m01`; bringing something forward `quranic:root_000281:B004/m01`; succession after what precedes `quranic:root_000131:B002/m01`; temporal nearness of an awaited event `quranic:root_001212:B002/m01`
- Ayah anchors: 61:6 `يَدَىَّ` (ي د ي), `يَأْتِى` (ء ت ي), `جَآءَ` (ج ي ء), and `بَعْدِ` (ب ع د); 61:13 `قَرِيبٌ` (ق ر ب)
- Synthesis: Succession is oriented from both sides. The Torah stands before Jesus as prior testimony, while the announced messenger comes after him; preparation and temporal approach then move the later term into presence. The near opening of 61:13 occupies the same forward-moving sequence.

### 3. Covering, Opening, and Manifestation
- Semantic invariant: Boundaries regulate exposure: a cover can obstruct, protect, or erase an effect, while opening and light reverse concealment.
- Surface relation: direct; 61:8 stages extinguishment against completed light, 61:9 and 61:14 stage manifestation, and 61:12 promises forgiveness and sheltered dwelling.
- Surprising reach: The same physical operation that can hide truth can also shield a vulnerable body or cancel an offense; the moral value lies in what the cover prevents from reaching its object.

#### Subchannel A. Extinguished Ember and Completed Light
- Reading type: mixed
- Scene or process: Mouths attempt to still a flame, but weak sparks and cooling embers are contrasted with light brought to completion.
- Active motifs: illuminating light `quranic:root_001564:B001/m01`; flame stilled and ember cooled `quranic:root_000938:B001/m01`; fire reduced to inert ash `quranic:root_000939:B001/m01`; useless weak sparks `quranic:root_000286:B011/m01`; kindled fire as moving light `quranic:root_001564:B002/m01`; completion of what was lacking `quranic:root_000188:B001/m01`; open mouth `quranic:root_001190:B001/m01`
- Ayah anchors: 61:8 forms of `نُور` (ن و ر), `يُطْفِـُٔ` (ط ف ء), `مُتِمُّ` (ت م م), and `أَفْوَٰهِ` (ف و ه); 61:4 and 61:13 forms of `ح ب ب`
- Synthesis: Extinguishment is rendered as the removal of motion, heat, and useful radiance. The adversarial mouths of 61:8 aim to reduce revelation to an inert ember, while divine completion supplies precisely what extinguishment removes. Even the latent image of profitless sparks sharpens the difference between mere flicker and sustaining light.

#### Subchannel B. Obstructive Cover and Disclosure
- Reading type: mixed
- Scene or process: Truth is veiled or engulfed, then opened, exposed, understood, and raised into dominance.
- Active motifs: covering that blocks acknowledgment `quranic:root_001307:B003/m01`; engulfing darkness or expanse `quranic:root_001307:B002/m01`; sensory concealment `quranic:root_000266:B001/m01`; emergence into clarity `quranic:root_000170:B004/m01`; exposure from hiddenness `quranic:root_000970:B001/m01`; opening of knowledge and guidance `quranic:root_001124:B008/m01`
- Ayah anchors: 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); 61:12 `جَنَّٰت` (ج ن ن); 61:6 forms of `ب ي ن`; 61:9 `يُظْهِرَ` and 61:14 `ظَٰهِرِينَ` (ظ ه ر); 61:13 `فَتْحٌ` (ف ت ح)
- Synthesis: Denial acts as a cover placed over an already present object, not as the object's absence. Disclosure reverses that operation through clarity, exposure, and an opening of understanding. The movement from veiling to dominance connects the clear signs of 61:6 with the promised manifestation of 61:9 and 61:14.

#### Subchannel C. Gate, Key, and Interior Store
- Reading type: latent/lexical
- Scene or process: A closed entrance is reached with the proper key, opened into a wider passage, crossed, and made to disclose the store held within.
- Active motifs: closed entrance widening open `quranic:root_001124:B001/m01`; key that gives access to what is shut `quranic:root_001124:B006/m01`; entry into an interior `quranic:root_000464:B001/m01`; opened treasury or repository `quranic:root_001124:B007/m01`
- Ayah anchors: 61:13 `فَتْحٌ` (ف ت ح); 61:12 `يُدْخِلْ` (د خ ل)
- Synthesis: Opening is a complete access mechanism. The key answers a closure, widening makes passage possible, entry crosses the boundary, and the interior yields what had been stored out of reach. This reframes the opening of 61:13 as access to a previously blocked good, not only victory over an opponent.

#### Subchannel D. Layered Protection
- Reading type: latent/lexical
- Scene or process: A vulnerable body or possession is enclosed by shield, head covering, weapon cover, leather shelter, netted tent, and guarding barrier.
- Active motifs: defensive shield `quranic:root_000266:B008/m01`; protective head covering `quranic:root_001096:B001/m01`; weapon-covering layer `quranic:root_001307:B001/m01`; leather shelter `quranic:root_000156:B004/m01`; thin protective tent `quranic:root_001315:B006/m01`; guarding barrier `quranic:root_000071:B002/m01`
- Ayah anchors: 61:12 `جَنَّٰت` (ج ن ن) and `يَغْفِرْ` (غ ف ر); 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); 61:4, 61:6, and 61:14 forms of `ب ن ي`; 61:9 `كُلِّ` (ك ل ل); 61:14 `أَيَّدْ` (ء ي د)
- Synthesis: Protection is built by nested surfaces rather than a single wall. Shield, covering, shelter, and barrier each intercept an incoming force at a different distance from the body. This latent defensive architecture reinforces the surah's compact formation and promised dwellings without collapsing them into one object.

#### Subchannel E. Fortified Perimeter and Night Watch
- Reading type: latent/lexical
- Scene or process: A fortified wall encloses a refuge while a custodian circles its perimeter at night and maintains a barrier against entry.
- Active motifs: fortified wall around a place `quranic:root_000957:B010/m01`; night guard circling on patrol `quranic:root_000957:B005/m01`; custody and sustained guardianship `quranic:root_001273:B004/m01`; concealed place of refuge `quranic:root_000266:B017/m01`; guarding barrier `quranic:root_000071:B002/m01`
- Ayah anchors: 61:14 forms of `ط و ف` and `أَيَّدْ` (ء ي د); 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:12 `جَنَّٰت` (ج ن ن)
- Synthesis: Protection here is active and territorial rather than worn on the body. The wall fixes a perimeter, the patrol repeatedly inspects it, guardianship sustains the duty, and the refuge preserves an interior. The scene extends the surah's collective support into watchfulness that keeps a protected space viable.

#### Subchannel F. Offense Covered and Its Effect Stopped
- Reading type: surface-primary
- Scene or process: An offense exposes its bearer to painful consequence; forgiveness covers the offense, while expiation makes it as though it had not been enacted.
- Active motifs: culpable offense `quranic:root_000521:B001/m01`; forgiveness that shields the offender from consequence `quranic:root_001096:B002/m01`; expiation by covering an offense `quranic:root_001307:B009/m01`; punitive pain `quranic:root_000994:B005/m01`; grave offense with enlarged consequence `quranic:root_001281:B007/m01`
- Ayah anchors: 61:12 `ذُنُوبَ` (ذ ن ب) and `يَغْفِرْ` (غ ف ر); 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); 61:10 `عَذَابٍ` (ع ذ ب); 61:3 `كَبُرَ` (ك ب ر)
- Synthesis: Forgiveness is a causal interruption: the offense remains identifiable, but the cover prevents its punitive effect from reaching the bearer. Expiation intensifies the image by making the deed functionally disappear, setting the rescue promised in 61:10-12 against the enlarged moral weight of 61:3.

#### Subchannel G. Dawn Breathing Through Night
- Reading type: latent/lexical
- Scene or process: Night covers the field, pre-dawn forms its threshold, first signs appear, and daylight opens as though taking a breath.
- Active motifs: night enveloping what lies beneath it `quranic:root_000266:B002/m01`; pre-dawn interval `quranic:root_000682:B004/m01`; first visible signs `quranic:root_000120:B007/m01`; first light of morning `quranic:root_000839:B001/m01`; dawn expanding like an exhalation `quranic:root_001533:B009/m01`; day opening in light `quranic:root_001559:B002/m01`
- Ayah anchors: 61:12 `جَنَّٰت` (ج ن ن) and `أَنْهَٰرُ` (ن ه ر); 61:6 `سِحْرٌ` (س ح ر) and `مُبَشِّرًا` (ب ش ر); 61:13 `بَشِّرِ` (ب ش ر); 61:14 `أَصْبَحُ` (ص ب ح); 61:11 `أَنفُسِ` (ن ف س)
- Synthesis: Manifestation unfolds by degrees rather than appearing all at once. Night's cover thins into a threshold, anticipatory signs become visible, and day expands into the opened field. This temporal scene gives the completed light of 61:8 a latent process of emergence.

### 4. Collective Force Under Opposition
- Semantic invariant: A dispersed population becomes effective force by differentiating sides, aligning bodies, reinforcing one another, and converting contest into dominance; that force fails when internal bonds reverse.
- Surface relation: direct; 61:4 depicts an aligned fighting structure, and 61:13-14 move from supporters and opposing factions to reinforcement and victory.
- Surprising reach: Collective strength is simultaneously social, architectural, and anatomical: people can function as courses of masonry, supporting backs, joined ribs, and assisting hands, while turned backs make the same formation fall apart.

#### Subchannel A. Crowd Differentiated Into Factions
- Reading type: mixed
- Scene or process: A broad human mass is gathered, bounded as a group, then divided into distinct parties.
- Active motifs: human collective `quranic:root_001273:B001/m01`; bounded faction or piece of a whole `quranic:root_000957:B004/m01`; mass of people `quranic:root_000266:B013/m01`; whole crowd arriving without remainder `quranic:root_001096:B008/m01`; humanity as visible-skinned beings `quranic:root_000120:B002/m01`; gathered company `quranic:root_000992:B005/m01`
- Ayah anchors: 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:14 `طَّآئِفَةٌ` (ط و ف); 61:12 forms of `جَنَّٰت` (ج ن ن) and `يَغْفِرْ` (غ ف ر); 61:6 `مُبَشِّرًا` and 61:13 `بَشِّرِ` (ب ش ر); surface anchor unavailable for ع د ن
- Synthesis: The faction in 61:14 is not merely a number but a bounded portion cut from a wider people. Images of mass, total crowd, and visible humanity supply the undifferentiated field; the party image then explains how belief and rejection organize that field into opposed social bodies.

#### Subchannel B. Rank Compacted Into a Load-Bearing Body
- Reading type: mixed
- Scene or process: Individuals align on one line, are pressed into contiguous courses, and become a stable structure whose internal members carry one another.
- Active motifs: straight battle rank `quranic:root_000871:B001/m01`; construction by joining components `quranic:root_000156:B001/m01`; forceful compacting of adjacent pieces `quranic:root_000567:B001/m01`; lead binding the masonry `quranic:root_000567:B002/m01`; exact and durable finishing `quranic:root_000348:B004/m01`; rib-like structural struts `quranic:root_000156:B009/m01`; chest-bone frame `quranic:root_000266:B016/m01`
- Ayah anchors: 61:4 `صَفًّا` (ص ف ف), `بُنْيَٰنٌ` (ب ن ي), and `مَّرْصُوصٌ` (ر ص ص); 61:1 `حَكِيمُ` (ح ك م); 61:12 `جَنَّٰت` (ج ن ن)
- Synthesis: The row is transformed from a visual arrangement into an engineered body. Joining creates the frame, pressure removes gaps, lead secures interfaces, and rib-like members distribute load. The anatomical reach makes the formation organic without weakening its architectural precision.

#### Subchannel C. Formation Unbound From Within
- Reading type: latent/lexical
- Scene or process: A joined company separates, members turn their backs on one another, mutual affiliation is disavowed, and connected parts fall in sequence.
- Active motifs: separation after union `quranic:root_000170:B001/m01`; mutual back-turning `quranic:root_000970:B022/m01`; parties disowning one another `quranic:root_001307:B005/m01`; one part collapsing after another `quranic:root_000478:B005/m01`
- Ayah anchors: 61:6 forms of `ب ي ن`; 61:9 and 61:14 forms of `ظ ه ر`; 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); 61:7 `يُدْعَىٰ` (د ع و)
- Synthesis: The compact rank has an exact negative process. Separation breaks contact, turned backs withdraw mutual support, disavowal cancels affiliation, and failure then propagates from one member to the next. This makes the disciples' answer in 61:14 structurally decisive: declared support prevents a social body from unbinding internally.

#### Subchannel D. Opponents Meet as Counterparts
- Reading type: mixed
- Scene or process: Hostile counterparts face one another, enter mutual combat, and sustain a contest in which each side acts against a matched rival.
- Active motifs: mutual combat `quranic:root_001200:B011/m01`; reciprocal confrontation `quranic:root_001273:B014/m01`; declared enemy and enmity `quranic:root_000993:B003/m01`; rival counterpart `quranic:root_001200:B008/m01`; feud ignited among people `quranic:root_001564:B007/m01`; far-reaching hostility `quranic:root_000131:B010/m01`
- Ayah anchors: 61:4 `يُقَٰتِلُ` (ق ت ل); 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:14 `عَدُوِّ` (ع د و); 61:8 forms of `نُور` (ن و ر); 61:6 `بَعْدِ` (ب ع د)
- Synthesis: Combat is framed as a relation between counterparts, not as isolated violence. Enmity supplies durable orientation, confrontation brings the sides into contact, and mutual fighting activates the relation. This makes the disciplined rank of 61:4 a response to a structured opposing side.

#### Subchannel E. Charge Carried Into Mortal Risk
- Reading type: mixed
- Scene or process: A fighter commits to a charge, proves its truth by carrying through to contact, becomes exposed to death, and stakes the self in the lethal outcome of combat.
- Active motifs: mutual combat `quranic:root_001200:B011/m01`; charge proved true or false by follow-through `quranic:root_001290:B004/m01`; exposing a person to killing `quranic:root_001200:B005/m01`; killing as removal of life `quranic:root_001200:B001/m01`; desperate self-exposure as though to die `quranic:root_001200:B012/m01`
- Ayah anchors: 61:4 `يُقَٰتِلُ` (ق ت ل); 61:7 `كَذِبَ` (ك ذ ب)
- Synthesis: Combat tests correspondence under irreversible pressure. A charge is called true only when it does not stop before contact; follow-through then exposes the fighter to death and turns commitment into a stake of the self. This martial sense gives the surah's opening contrast between saying and doing a lethal edge.

#### Subchannel F. A Network of Backs, Hands, and Helpers
- Reading type: mixed
- Scene or process: Supporters reinforce a vulnerable side through helping roles figured as a strengthening hand and a back that bears force.
- Active motifs: disciple-helper `quranic:root_000369:B003/m01`; aid that makes a side prevail `quranic:root_001510:B001/m01`; assisting and protective hand `quranic:root_001693:B016/m01`; strength gained from a backing helper `quranic:root_000970:B006/m01`; active reinforcement `quranic:root_000071:B001/m01`; strengthening one member with another `quranic:root_001008:B004/m01`
- Ayah anchors: 61:14 `حَوَارِيُّونَ` (ح و ر), forms of `ن ص ر`, `أَيَّدْ` (ء ي د), and `ظَٰهِرِينَ` (ظ ه ر); 61:13 `نَصْرٌ` (ن ص ر); 61:6 `يَدَىَّ` (ي د ي); 61:1 `عَزِيزُ` (ع ز ز)
- Synthesis: Alliance becomes a distributed support mechanism. One person functions as another's back, another as a protective hand, and reinforcement increases the load the whole can bear. The disciples' verbal answer in 61:14 therefore enters the same structural field as the compacted rank.

#### Subchannel G. Victory as Opening and Rising Above
- Reading type: mixed
- Scene or process: Aid opens a blocked contest, rescue separates a side from danger, and the supported party rises above its opponent.
- Active motifs: victory as an opening `quranic:root_001124:B004/m01`; successful escape with the good attained `quranic:root_001186:B001/m01`; rising above and gaining mastery `quranic:root_000970:B007/m01`; overpowering an opponent `quranic:root_001008:B002/m01`; outmatching a rival `quranic:root_001281:B011/m01`; prevailing through repeated arrival `quranic:root_000281:B002/m01`
- Ayah anchors: 61:13 `فَتْحٌ` (ف ت ح); 61:12 `فَوْزُ` (ف و ز); 61:9 `يُظْهِرَ` and 61:14 `ظَٰهِرِينَ` (ظ ه ر); 61:1 `عَزِيزُ` (ع ز ز); 61:3 `كَبُرَ` (ك ب ر); 61:6 `جَآءَ` (ج ي ء)
- Synthesis: Victory is a transition in spatial relation. A closure opens, danger releases its hold, and one side becomes uppermost. This physical sequence joins the near opening of 61:13 to the final state of visible ascendancy in 61:14.

### 5. Water Directed for Survival
- Semantic invariant: Water sustains or overwhelms according to how it enters, is bounded, channeled, crossed, or escaped.
- Surface relation: direct at 61:12's flowing rivers and indirect through the heavens of 61:1, rescue of 61:10, and aid of 61:13.
- Surprising reach: Victory and rescue acquire hydrological form: help can arrive as rain, an outlet can turn pressure into flow, and survival can mean either steering on water or gaining ground above it.

#### Subchannel A. Rain Front Arriving as Relief
- Reading type: latent/lexical
- Scene or process: Water descends from the overhead sky, arrives from another region, intensifies into an encircling flood, and revives the land as aid.
- Active motifs: flood arriving from a rain-struck region `quranic:root_000009:B005/m01`; rain suspended between cloud and earth `quranic:root_000672:B005/m01`; overhead rain-bearing sky `quranic:root_000745:B004/m02`; enveloping flood `quranic:root_000957:B002/m01`; forceful rain and torrent `quranic:root_001008:B008/m01`; rain as relief and irrigation `quranic:root_001510:B004/m01`; encircling cloud `quranic:root_001315:B005/m01`
- Ayah anchors: 61:6 `يَأْتِى` (ء ت ي); 61:4 and 61:11 `سَبِيلِ` (س ب ل); 61:1 `سَّمَٰوَٰتِ` and 61:6 `ٱسْمُ` (س م و); 61:14 `طَّآئِفَةٌ` (ط و ف); 61:1 `عَزِيزُ` (ع ز ز); 61:13-14 forms of `ن ص ر`; 61:9 `كُلِّ` (ك ل ل)
- Synthesis: The rain scene gives aid a direction and a body. It comes from elsewhere, occupies the interval between sky and ground, and can surround before it nourishes. Calling rain “support” makes divine aid in 61:13 both forceful and life-restoring.

#### Subchannel B. Outlet, Channel, and River Network
- Reading type: mixed
- Scene or process: Earth breaks open into springs, collected water widens an outlet, enters channels, travels along valley tails, and joins tributaries in a flowing river system.
- Active motifs: directed water conduit `quranic:root_000009:B004/m01`; catchment hollow `quranic:root_000281:B003/m01`; earth bursting open with springs `quranic:root_001150:B005/m01`; valley-tail channels `quranic:root_000521:B004/m01`; water breaking from an outlet `quranic:root_001124:B005/m01`; opening widened until flow begins `quranic:root_001559:B003/m01`; river mouth or outlet `quranic:root_001190:B004/m01`; river cutting a channel through earth `quranic:root_001559:B001/m01`; distant tributaries entering a basin `quranic:root_001510:B007/m01`; continuous flow `quranic:root_000240:B001/m01`
- Ayah anchors: 61:6 forms of `ء ت ي` and `ج ي ء`; 61:7 `ٱفْتَرَىٰ` (ف ر ي); 61:12 `ذُنُوبَ` (ذ ن ب), `أَنْهَٰرُ` (ن ه ر), and `تَجْرِى` (ج ر ي); 61:13 `فَتْحٌ` (ف ت ح) and `نَصْرٌ` (ن ص ر); 61:8 `أَفْوَٰهِ` (ف و ه)
- Synthesis: The rivers of 61:12 are expanded into a functional network rather than a static landscape. Rupture, widening, basin, outlet, channel, tributary, and current form a causal chain in which stored pressure becomes directed abundance. The opening of 61:13 resonates with the aperture that enlarges until water can reach cultivated ground.

#### Subchannel C. Raft, Skiff, and Stabilizing Stern
- Reading type: latent/lexical
- Scene or process: A constructed float carries people over water while a smaller boat and a stern or rudder keep the craft stable and serviceable.
- Active motifs: tied-wood or inflated-skin raft `quranic:root_000957:B006/m01`; service skiff `quranic:root_001212:B011/m01`; stern or rudder that stills a vessel's oscillation `quranic:root_000726:B008/m01`; composite frame `quranic:root_000156:B002/m01`; leather canopy `quranic:root_000156:B004/m01`; tent-like protective cover `quranic:root_001315:B006/m01`
- Ayah anchors: 61:14 `طَّآئِفَةٌ` (ط و ف); 61:13 `قَرِيبٌ` (ق ر ب); 61:12 `مَسَٰكِنَ` (س ك ن); 61:4, 61:6, and 61:14 forms of `ب ن ي`; 61:9 `كُلِّ` (ك ل ل)
- Synthesis: Buoyancy alone does not complete the vessel scene. A frame binds the float, a cover protects its occupants, a skiff handles local movement, and a stern converts unstable motion into a directed crossing. This latent transport mechanism gives rescue an engineered form.

#### Subchannel D. Refuge Above Flood and Through Waste
- Reading type: mixed
- Scene or process: Escape separates a traveler from danger by reaching high ground or crossing a waterless expanse whose name holds both rescue and ruin.
- Active motifs: separation from danger `quranic:root_001476:B001/m01`; raised ground beyond flood reach `quranic:root_001476:B004/m01`; deadly waterless waste `quranic:root_001186:B003/m01`; wilderness construed as a saving passage `quranic:root_001186:B003/m02`; breadth for movement and livelihood `quranic:root_000666:B005/m01`; spatial breadth and respite `quranic:root_001533:B015/m01`; remote settlement `quranic:root_001307:B012/m01`
- Ayah anchors: 61:10 `تُنجِي` (ن ج و); 61:12 `فَوْزُ` (ف و ز); 61:1 `سَبَّحَ` (س ب ح); 61:11 `أَنفُسِ` (ن ف س); 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر)
- Synthesis: Deliverance is spatially exact: one must become detached from the threat and occupy terrain it cannot overtake. The double image of the waterless waste, both lethal and called a place of salvation, keeps rescue from becoming effortless; passage remains a demanding exposure between danger and refuge.

### 6. Cultivation Into Abiding Provision
- Semantic invariant: Concealed potential is planted, irrigated, ripened, and transformed into a sheltered environment that feeds, houses, and delights.
- Surface relation: direct at 61:12's gardens, rivers, and good dwellings; indirect through earth, love, light, and completion elsewhere in the surah.
- Surprising reach: The promised abode is not only a destination but the mature state of a growth process whose stages include burial, sprouting, flowering, ripening, fragrance, and settled use.

#### Subchannel A. Seed Buried, Sprouted, and Ripened
- Reading type: latent/lexical
- Scene or process: Seed is covered in fertile ground, rises into an ear, flowers, yields produce, ripens from its end, and finally breaks its husk.
- Active motifs: germinating seed `quranic:root_000286:B001/m01`; seed covered with soil `quranic:root_001307:B008/m01`; fertile yielding earth `quranic:root_000025:B002/m01`; extended grain ear `quranic:root_000672:B008/m01`; flowering plant `quranic:root_001564:B004/m01`; crop and fruit yield `quranic:root_000009:B007/m01`; fruit ripening from its tip `quranic:root_000521:B005/m01`; ripe fruit emerging from its skin `quranic:root_001156:B002/m01`
- Ayah anchors: 61:4 and 61:13 forms of `ح ب ب`; 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); 61:1 `أَرْضِ` (ء ر ض); 61:4 and 61:11 `سَبِيلِ` (س ب ل); 61:8 `نُور` (ن و ر); 61:6 `يَأْتِى` (ء ت ي); 61:12 `ذُنُوبَ` (ذ ن ب); 61:5 `فَٰسِقِينَ` (ف س ق)
- Synthesis: Growth begins with an apparent disappearance: seed is deliberately covered so that it can emerge transformed. The stages move from concealment to extension, flowering, yield, and rupture of the husk. This makes the surah's completed light and promised gardens parallel outcomes of protected maturation rather than instant display.

#### Subchannel B. Screened Orchard Fed by Running Water
- Reading type: surface-primary
- Scene or process: Dense growth forms a screened garden while opened watercourses run beneath and through it.
- Active motifs: tree-screened garden `quranic:root_000266:B003/m01`; dense and vigorous vegetation `quranic:root_000266:B011/m01`; river channel `quranic:root_001559:B001/m01`; running current `quranic:root_000240:B001/m01`; lower course beneath the garden `quranic:root_000177:B001/m01`; irrigation released from an opening `quranic:root_001124:B005/m01`; tender palm heart `quranic:root_001248:B003/m01`
- Ayah anchors: 61:12 forms of `جَنَّٰت` (ج ن ن), `أَنْهَٰرُ` (ن ه ر), `تَجْرِى` (ج ر ي), and `تَحْتِ` (ت ح ت); 61:13 `فَتْحٌ` (ف ت ح); 61:5 `قُلُوبَ` (ق ل ب)
- Synthesis: The garden is a coupled system of cover and flow. Trees make an interior by screening it, dense vegetation maintains that cover, and released water feeds the living center. The palm-heart image makes the landscape itself seem inwardly alive.

#### Subchannel C. Dwelling That Brings Motion to Rest
- Reading type: mixed
- Scene or process: Movement ceases in a supported residence whose location, provisions, and durable station make continued inhabitation possible.
- Active motifs: cessation of motion `quranic:root_000726:B001/m01`; inhabited dwelling `quranic:root_000726:B002/m01`; place of comfort and familiarity `quranic:root_000726:B004/m01`; abiding residence `quranic:root_000992:B001/m01`; established station `quranic:root_001273:B006/m01`; place and standing `quranic:root_001332:B002/m01`; house columns `quranic:root_000156:B009/m02`
- Ayah anchors: 61:12 `مَسَٰكِنَ` (س ك ن); surface anchor unavailable for ع د ن; 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:11 `كُن` and 61:14 `كُونُ` (ك و ن); 61:4, 61:6, and 61:14 forms of `ب ن ي`
- Synthesis: A dwelling is complete only when it arrests wandering, supports the structure, and supplies a station that can be maintained. The unanchored lexical image of abiding residence deepens the explicit “good dwellings” of 61:12 into a durable end-state rather than temporary shelter.

#### Subchannel D. Fragrance and Sweetness of the Mature Abode
- Reading type: mixed
- Scene or process: Aromatic substances, sweet exudates, perfume, and fresh water give the settled garden a sensory atmosphere of goodness.
- Active motifs: aromatic perfume `quranic:root_000961:B007/m01`; blended aromatic materials `quranic:root_001190:B005/m01`; camphor fragrance `quranic:root_001307:B011/m01`; aloeswood incense `quranic:root_000076:B014/m01`; sweet tree gum `quranic:root_001096:B007/m01`; sweet and palatable water `quranic:root_000994:B001/m01`
- Ayah anchors: 61:12 `طَيِّبَةً` (ط ي ب) and `يَغْفِرْ` (غ ف ر); 61:8 `أَفْوَٰهِ` (ف و ه) and `كَٰفِرُونَ` (ك ف ر); 61:10 `عَذَابٍ` (ع ذ ب); surface anchor unavailable for ء ل ي
- Synthesis: “Good” dwelling is materialized through smell and taste rather than left as a generic evaluation. Incense wood, gum, camphor, composed perfume, and fresh water turn the promised abode into a fully sensed environment, contrasting the painful taste of punishment in 61:10.

### 7. Transfer, Accounting, and Redress
- Semantic invariant: Goods, obligations, rights, and aid move between parties under rules that determine profit, debt, possession, and restoration.
- Surface relation: direct in the saving trade of 61:10-11 and indirect through truth, injustice, support, and victory in 61:7-14.
- Surprising reach: The surah's commercial invitation opens into a broader economy in which belief, property, gift, legal claim, and redress all require a valid transfer between accountable parties.

#### Subchannel A. Profitable Exchange as Rescue
- Reading type: surface-primary
- Scene or process: A guide identifies a transaction; capital and skill are committed, useful good is gained, and the trader exits danger with profit.
- Active motifs: trade seeking profit `quranic:root_000176:B001/m01`; skill in a mode of earning `quranic:root_000176:B004/m01`; accumulated property `quranic:root_001457:B001/m01`; useful and desirable good `quranic:root_000452:B001/m01`; escape from harm `quranic:root_001476:B001/m01`; attainment of good `quranic:root_001186:B001/m01`; indication of the route to an object `quranic:root_000484:B001/m01`
- Ayah anchors: 61:10 `تِجَٰرَةٍ` (ت ج ر), `تُنجِي` (ن ج و), and `أَدُلُّ` (د ل ل); 61:11 `أَمْوَٰلِ` (م و ل) and `خَيْرٌ` (خ ي ر); 61:12 `فَوْزُ` (ف و ز)
- Synthesis: The trade metaphor is a complete transaction scene, not only a comparison. Guidance identifies the opportunity, wealth is exposed as capital, practiced action executes the exchange, and rescue is the realized return. Profit is measured by separation from punishment and acquisition of durable good.

#### Subchannel B. Goods Enter a Brisk Market
- Reading type: latent/lexical
- Scene or process: A trader brings saleable stock to a recognized marketplace, the goods receive a valuation, demand makes the stock move, and the market becomes active.
- Active motifs: trade seeking profit `quranic:root_000176:B001/m01`; place to which trade is brought `quranic:root_000176:B002/m01`; she-camel that sells readily when offered `quranic:root_000176:B003/m01`; valuation of goods `quranic:root_001273:B010/m01`; market becoming brisk `quranic:root_001273:B018/m01`
- Ayah anchors: 61:10 `تِجَٰرَةٍ` (ت ج ر); 61:5 and 61:7 forms of `قَوْم` (ق و م)
- Synthesis: The offered trade of 61:10 is placed inside an operating market rather than left as an abstract bargain. A venue gathers participants, valuation makes comparison possible, and demand converts offered stock into a completed sale. The ready-selling animal materializes the invitation as something whose worth becomes evident when properly presented.

#### Subchannel C. Credit, Income, and Hand-to-Hand Payment
- Reading type: latent/lexical
- Scene or process: Wealth enters as income, may be advanced on credit, receives a valuation, and is discharged through immediate payment or a recognized due.
- Active motifs: financial debt and deferred sale `quranic:root_000504:B003/m01`; incoming revenue `quranic:root_000464:B006/m01`; advance payment `quranic:root_000737:B005/m01`; hand-to-hand settlement `quranic:root_001693:B007/m01`; valuation of goods `quranic:root_001273:B010/m01`; tribute or assessed payment `quranic:root_000009:B008/m01`; alms or financial due `quranic:root_000852:B006/m01`
- Ayah anchors: 61:9 forms of `دِين` (د ي ن); 61:12 `يُدْخِلْ` (د خ ل); 61:7 `إِسْلَٰمِ` (س ل م); 61:6 `يَدَىَّ` (ي د ي), `يَأْتِى` (ء ت ي), and `مُّصَدِّقًا` (ص د ق); 61:5 and 61:7 forms of `قَوْم` (ق و م)
- Synthesis: The latent economy distinguishes time and direction: income enters, credit postpones settlement, advance payment reverses that timing, valuation fixes equivalence, and hand-to-hand exchange closes the obligation. This pressures the saving trade to be read as accountable commitment rather than costless assent.

#### Subchannel D. Obligation Brought to Account
- Reading type: mixed
- Scene or process: A binding due is brought into the adjudicator's presence, evasion closes, an account is taken, and each party receives the assigned recompense or punitive share.
- Active motifs: binding obligation and fixed entitlement `quranic:root_000347:B002/m01`; accounting, judgment, and recompense `quranic:root_000504:B002/m01`; presence before the deciding authority `quranic:root_001052:B004/m01`; absence of an escape or alternative `quranic:root_001052:B005/m01`; allotted share, especially of punishment `quranic:root_000521:B006/m01`; judicial decision `quranic:root_000348:B002/m01`
- Ayah anchors: 61:9 `حَقِّ` (ح ق ق) and forms of `دِين` (د ي ن); 61:3 `عِندَ` (ع ن د); 61:12 `ذُنُوبَ` (ذ ن ب); 61:1 `حَكِيمُ` (ح ك م)
- Synthesis: Accounting converts a moral or commercial obligation into an unavoidable settlement. Presence removes distance, judgment determines what is due, and recompense assigns the resulting share. This gives the surah's trade, painful punishment, forgiveness, and great attainment a common frame of liabilities and returns finally brought to account.

#### Subchannel E. Gift Without Counterpayment
- Reading type: latent/lexical
- Scene or process: A benefit is brought forward and placed in another's hand as grace, generous provision, or affectionate gift rather than bargained return.
- Active motifs: giving and presentation `quranic:root_000009:B002/m01`; gratuitous grant `quranic:root_000076:B012/m01`; generosity and gift `quranic:root_000452:B005/m01`; willing and easy giving `quranic:root_000563:B010/m01`; aid as bestowal `quranic:root_001510:B005/m01`; beneficent hand `quranic:root_001693:B003/m01`; affectionate gift `quranic:root_001583:B004/m01`
- Ayah anchors: 61:6 `يَأْتِى` (ء ت ي), `يَدَىَّ` (ي د ي), and forms of `ر س ل` and `ه د ي`; 61:11 `خَيْرٌ` (خ ي ر) and `رَسُولِ` (ر س ل); 61:13-14 forms of `ن ص ر`; surface anchor unavailable for ء ل ي
- Synthesis: Gift is distinguished from trade by the absence of counterpayment. The donor brings the benefit into reach, the hand marks receipt, and generous willingness determines the transfer's quality. Divine aid can therefore resonate simultaneously as victory and unbargained bestowal.

#### Subchannel F. Claim Tested by Judgment
- Reading type: latent/lexical
- Scene or process: Parties assert ownership, contest the same right, submit possession and evidence to judgment, and receive a separating verdict.
- Active motifs: privately held right `quranic:root_000347:B003/m01`; rival claims to truth or entitlement `quranic:root_000347:B004/m01`; asserted right or affiliation `quranic:root_000478:B002/m01`; co-owned share `quranic:root_000791:B001/m01`; withholding another's right `quranic:root_000967:B008/m01`; possessive hand `quranic:root_001693:B004/m01`; judicial decision `quranic:root_000348:B002/m01`; judgment that opens a closed dispute `quranic:root_001124:B003/m01`
- Ayah anchors: 61:9 `حَقِّ` (ح ق ق) and `مُشْرِكُونَ` (ش ر ك); 61:7 `يُدْعَىٰ` (د ع و) and forms of `ظ ل م`; 61:6 `يَدَىَّ` (ي د ي); 61:1 `حَكِيمُ` (ح ك م); 61:13 `فَتْحٌ` (ف ت ح)
- Synthesis: A claim becomes valid only after it survives contest, evidence, and judgment. Possession by the hand is not enough when another right has been withheld; the verdict must open the dispute and separate legitimate share from wrongful control. This legal scene gives truth and right institutional as well as doctrinal force.

#### Subchannel G. Grievance Carried to Redress
- Reading type: latent/lexical
- Scene or process: An injured party voices a grievance, petitions authority, receives protection, and is restored against the wrongdoer.
- Active motifs: grievance seeking equity `quranic:root_000967:B003/m01`; petition to authority for vindication `quranic:root_000993:B005/m01`; recovery of the oppressed party's due `quranic:root_001510:B002/m01`; protective assisting hand `quranic:root_001693:B016/m01`; restraint of wrongdoing `quranic:root_000348:B001/m01`; withholding that prevents further harm `quranic:root_000994:B003/m01`
- Ayah anchors: 61:7 forms of `ظ ل م`; 61:14 `عَدُوِّ` (ع د و); 61:13-14 forms of `ن ص ر`; 61:6 `يَدَىَّ` (ي د ي); 61:1 `حَكِيمُ` (ح ك م); 61:10 `عَذَابٍ` (ع ذ ب)
- Synthesis: Redress is a directed social process: complaint travels upward, authority restrains the aggressor, and aid returns the injured party to an equitable position. The same root that names support in 61:13-14 can thus mean the concrete restoration of someone denied a right.

### 8. Message and Response
- Semantic invariant: Communication becomes socially effective when a bearer and public signs make an identity legible, a receiving community answers, and the message's truth survives distortion.
- Surface relation: direct; messengers, speech, clear signs, accusation of magic, lying, invitation, and the disciples' answer structure 61:2-9 and 61:14.
- Surprising reach: A message can travel as a carried object, make a foreign bearer socially present, circulate through name and reputation, turn into reciprocal dialogue, or be counterfeited like a misleadingly patterned cloth.

#### Subchannel A. The Carried and Clarified Message
- Reading type: mixed
- Scene or process: A delegated bearer transports a statement, opens its meaning through speech or sign, and releases it into public circulation.
- Active motifs: dispatch and release from restraint `quranic:root_000563:B001/m01`; messenger-bearer `quranic:root_000563:B002/m01`; carried message `quranic:root_000563:B002/m02`; delegated representative `quranic:root_000240:B003/m01`; authoritative speaker `quranic:root_001272:B004/m01`; clarification by word or sign `quranic:root_000170:B005/m01`; speech issuing through the mouth `quranic:root_001190:B003/m01`; report circulating among people `quranic:root_001272:B007/m01`; truthful statement `quranic:root_000852:B001/m01`
- Ayah anchors: 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:12 `تَجْرِى` (ج ر ي); 61:2-3, 61:5-6, and 61:14 forms of `ق و ل`; 61:6 forms of `ب ي ن` and `مُّصَدِّقًا` (ص د ق); 61:8 `أَفْوَٰهِ` (ف و ه)
- Synthesis: The message is assembled from role-separated parts: dispatch, bearer, carried content, utterance, clarifying medium, and social circulation. This prevents “messenger” from collapsing into “speech”; release initiates the movement, the bearer transports it, and clarification makes it publicly legible.

#### Subchannel B. Name and Sign Made Public
- Reading type: mixed
- Scene or process: A name fixes a referent, signs clarify it, the bearer rises into public visibility, and a good reputation travels beyond the original utterance.
- Active motifs: naming that makes identity known `quranic:root_000745:B005/m01`; indication by a recognizable sign `quranic:root_000484:B001/m01`; clarification through word or sign `quranic:root_000170:B005/m01`; a thing's condition speaking its meaning `quranic:root_001272:B014/m01`; elevated figure visible from afar `quranic:root_000745:B002/m01`; good reputation spreading publicly `quranic:root_000745:B008/m01`
- Ayah anchors: 61:1 `سَّمَٰوَٰتِ` and 61:6 `ٱسْمُ` (س م و); 61:10 `أَدُلُّ` (د ل ل); 61:6 forms of `ب ي ن`; 61:2-3, 61:5-6, and 61:14 forms of `ق و ل`
- Synthesis: Ahmad's announced name in 61:6 functions as a public sign before the named messenger arrives. Designation fixes identity, clear signs make the designation readable, and reputation extends that legibility through the community. Even an object's condition can “speak,” so evidence need not depend on an ungrounded verbal claim.

#### Subchannel C. Call, Reply, and Deliberation
- Reading type: mixed
- Scene or process: A voice draws recipients toward a position, they answer, exchange correspondence, keep pace in conversation, and develop reciprocal speech into deliberation or private counsel.
- Active motifs: vocal summons and invitation `quranic:root_000478:B001/m01`; reply and reciprocal dialogue `quranic:root_000369:B006/m01`; reciprocal correspondence `quranic:root_000563:B008/m01`; accompanying another in conversation `quranic:root_000240:B007/m01`; negotiation over an affair `quranic:root_001272:B009/m01`; confidential counsel `quranic:root_001476:B005/m01`; answering a caller `quranic:root_001573:B003/m01`; speech obstructed by repeated sounds `quranic:root_000188:B005/m01`
- Ayah anchors: 61:7 `يُدْعَىٰ` (د ع و); 61:14 forms of `حَوَارِيُّونَ` (ح و ر) and `قَالَ` (ق و ل); 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:12 `تَجْرِى` (ج ر ي); 61:10 `تُنجِي` (ن ج و); 61:8 `مُتِمُّ` (ت م م); surface anchor unavailable for ه ا ء
- Synthesis: The disciples' response in 61:14 completes a call-and-answer scene rather than merely adding another quotation. Summons changes orientation, correspondence sustains exchange, and keeping pace in speech allows a group to negotiate its role. The latent stutter marks the opposite condition, where sound recurs without successful transfer.

#### Subchannel D. Stranger Received or Kept Apart
- Reading type: latent/lexical
- Scene or process: A foreign bearer enters a people not his own, mixes with the host group, and is either joined to them by a social bond or held apart through separation.
- Active motifs: foreigner entering another people `quranic:root_000009:B006/m01`; stranger figured as a son of the land `quranic:root_000025:B004/m01`; outsider mixing into a group's affairs `quranic:root_000464:B005/m01`; bond connecting separate parties `quranic:root_000170:B003/m01`; separation after contact `quranic:root_000170:B001/m01`
- Ayah anchors: 61:6 `يَأْتِى` (ء ت ي) and forms of `ب ي ن`; 61:1 `أَرْضِ` (ء ر ض); 61:12 `يُدْخِلْ` (د خ ل)
- Synthesis: A messenger's arrival is also a test of communal boundaries. Entry makes the bearer physically present, but reception determines whether presence becomes relation or estrangement. The accusations in 61:5-7 and the disciples' affiliation in 61:14 become opposite social outcomes for a bearer who addresses a people from a position they may treat as alien.

#### Subchannel E. Counterfeit and Redirecting Discourse
- Reading type: mixed
- Scene or process: Speech diverts attention, attributes what was never said, fabricates a form without precedent, and presents a surface that misstates its underlying condition.
- Active motifs: deceptive redirection by magic or rhetoric `quranic:root_000682:B002/m01`; falsely attributing words `quranic:root_001272:B005/m01`; declaring another false `quranic:root_001290:B002/m01`; invented lie `quranic:root_001150:B003/m01`; fabricated composition `quranic:root_001167:B004/m01`; patterned cloth whose surface deceives `quranic:root_001290:B009/m01`
- Ayah anchors: 61:6 `سِحْرٌ` (س ح ر) and forms of `ق و ل`; 61:2-3 forms of `ق و ل` and `ف ع ل`; 61:7 `ٱفْتَرَىٰ` (ف ر ي) and `كَذِبَ` (ك ذ ب)
- Synthesis: False discourse is more than an incorrect sentence. It is a production process that redirects perception, assigns alien words, and manufactures a persuasive exterior. The counterfeit cloth gives the lie a material analogy: surface pattern claims a condition the substance does not possess.

### 9. Household Formation and Descent
- Semantic invariant: A household is formed and continued through regulated union, bodily entry, birth, naming, and recognized lines of descent.
- Surface relation: indirect but persistent; “son,” “children,” “after me,” personal naming, and communal descent in 61:6 and 61:14 activate the frame.
- Surprising reach: Construction language extends into marriage and gestation, while distorted unions expose the boundary conditions required for legitimate continuity.

#### Subchannel A. Bridal Transfer and Consummation
- Reading type: latent/lexical
- Scene or process: A bride is transferred to a spouse, a household is established through entry and bodily contact, and dower and affinity formalize the union.
- Active motifs: establishing a household by entering upon a wife `quranic:root_000156:B006/m01`; bride conveyed to her spouse `quranic:root_001583:B006/m01`; conjugal entry `quranic:root_000464:B002/m01`; skin-to-skin contact `quranic:root_000120:B003/m01`; bridal dower `quranic:root_000852:B007/m01`; widowed or divorced woman approached by suitors `quranic:root_000563:B009/m01`; partnership by affinity `quranic:root_000791:B003/m01`
- Ayah anchors: 61:6 and 61:14 forms of `ب ن ي`; 61:5, 61:7, and 61:9 forms of `ه د ي`; 61:12 `يُدْخِلْ` (د خ ل); 61:6 and 61:13 forms of `ب ش ر`; 61:6 `مُّصَدِّقًا` (ص د ق); 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:9 `مُشْرِكُونَ` (ش ر ك)
- Synthesis: Marriage is represented as a regulated transfer with spatial, bodily, and economic stages. The bride is conveyed, entry establishes the new interior, contact consummates it, and dower and affinity give the relation public standing. The scene makes “building” a social as well as architectural operation.

#### Subchannel B. Violated Household Boundary
- Reading type: latent/lexical
- Scene or process: Coercion, prohibited inheritance of a father's wife, captivity, or repudiating comparison distorts the regulated union.
- Active motifs: prohibited marriage to a father's wife `quranic:root_001436:B002/m01`; repudiating a wife through maternal comparison `quranic:root_000970:B010/m01`; forcing another into an unwanted act `quranic:root_001295:B003/m01`; taking a person captive `quranic:root_000737:B013/m01`; approaching sexual intimacy `quranic:root_001212:B007/m01`
- Ayah anchors: 61:3 `مَقْتًا` (م ق ت); 61:9 `يُظْهِرَ` and 61:14 `ظَٰهِرِينَ` (ظ ه ر); 61:8-9 `كَرِهَ` (ك ر ه); 61:7 `إِسْلَٰمِ` (س ل م); 61:13 `قَرِيبٌ` (ق ر ب)
- Synthesis: These are not variants of ordinary courtship but breaches of its governing relations. Coercion removes consent, captivity removes freedom, prohibited succession confuses generations, and repudiating comparison corrupts kin categories. The severe disgust of 61:3 gains a latent household frame in which misordered relation itself is hateful.

#### Subchannel C. Gestation, Birth, and First Issue
- Reading type: latent/lexical
- Scene or process: A hidden fetus reaches term, nears delivery, exits with postpartum blood and afterbirth, and becomes the first young of a new generation.
- Active motifs: fetus hidden in the womb `quranic:root_000266:B007/m01`; approaching delivery `quranic:root_001212:B012/m01`; childbirth and postpartum blood `quranic:root_001533:B005/m01`; womb as birth setting `quranic:root_000994:B009/m01`; afterbirth following the child `quranic:root_000994:B009/m02`; completed gestational term `quranic:root_000188:B004/m01`; first camel calf `quranic:root_000369:B008/m01`; young ibex `quranic:root_001096:B005/m01`; mother ibex `quranic:root_001096:B005/m02`
- Ayah anchors: 61:12 forms of `جَنَّٰت` (ج ن ن) and `يَغْفِرْ` (غ ف ر); 61:13 `قَرِيبٌ` (ق ر ب); 61:11 `أَنفُسِ` (ن ف س); 61:10 `عَذَابٍ` (ع ذ ب); 61:8 `مُتِمُّ` (ت م م); 61:14 forms of `حَوَارِيُّونَ` (ح و ر)
- Synthesis: Birth is a threshold process with hidden occupant, completed measure, approaching event, bodily exit, and new issue. It supplies a concrete generational mechanism beneath the surah's language of sons, children, and a messenger who comes afterward.

#### Subchannel D. Lineage, Naming, and Succession
- Reading type: mixed
- Scene or process: Descent establishes relation, a name marks affiliation, collateral and later members occupy ordered positions, and successive bands continue the line.
- Active motifs: filiation and attribution to an origin `quranic:root_000156:B007/m01`; kinship by descent `quranic:root_001212:B003/m01`; collateral kin outside the direct line `quranic:root_001315:B004/m01`; naming that makes identity known `quranic:root_000745:B005/m01`; later or other successor `quranic:root_000019:B001/m01`; coming after a predecessor `quranic:root_000131:B002/m01`; successive bands following one another `quranic:root_000563:B005/m01`
- Ayah anchors: 61:6 and 61:14 forms of `ب ن ي`; 61:13 `قَرِيبٌ` (ق ر ب) and `أُخْرَىٰ` (ء خ ر); 61:9 `كُلِّ` (ك ل ل); 61:1 `سَّمَٰوَٰتِ` and 61:6 `ٱسْمُ` (س م و); 61:6 `بَعْدِ` (ب ع د) and forms of `ر س ل`
- Synthesis: Naming does not merely label an isolated individual; it places the named bearer within a sequence of origin, kin, predecessor, and successor. The announcement of Ahmad in 61:6 is therefore both communicative and genealogical, while the later believing faction in 61:14 becomes a continuing band within that succession.

### 10. Pastoral Provision and Mobility
- Semantic invariant: Herd life converts managed animal bodies into offspring, milk, transport, and sustained movement.
- Surface relation: indirect; fighting in ranks, striving with wealth and selves, and near victory activate a latent pastoral infrastructure of mounts, breeding, watering, and load-bearing.
- Surprising reach: The surah's collective discipline is echoed in milking posture, matched hoof placement, controlled gait, and the careful timing of breeding and watering.

#### Subchannel A. Breeding and Milk Production
- Reading type: latent/lexical
- Scene or process: A receptive female meets a stallion, reaches breeding maturity, produces young, and is positioned and managed for milk flow.
- Active motifs: female camel seeking the male `quranic:root_000009:B012/m01`; stallion mounting the herd `quranic:root_000745:B003/m01`; camel reaching breeding maturity `quranic:root_000347:B008/m01`; first camel calf `quranic:root_000369:B008/m01`; combined milk yields `quranic:root_000871:B002/m01`; forelegs aligned for milking `quranic:root_000871:B002/m02`; constricted udder with little milk `quranic:root_001008:B006/m01`; continuing milk flow `quranic:root_000563:B006/m01`; retained milk that draws down what follows `quranic:root_000478:B003/m01`
- Ayah anchors: 61:6 `يَأْتِى` (ء ت ي), `ٱسْمُ` (س م و), and forms of `ر س ل`; 61:9 `حَقِّ` (ح ق ق); 61:14 forms of `حَوَارِيُّونَ` (ح و ر); 61:4 `صَفًّا` (ص ف ف); 61:1 `عَزِيزُ` (ع ز ز); 61:7 `يُدْعَىٰ` (د ع و)
- Synthesis: Provision depends on ordered biological and handling stages: readiness, mating, maturity, birth, posture, and milk release. The milking image gives alignment a productive rather than martial outcome, while the constricted udder shows how a blocked channel limits communal provision.

#### Subchannel B. Herd Driven to Water and Fullness
- Reading type: latent/lexical
- Scene or process: Herds are driven toward a water source, thirsty animals are reintroduced to the trough, and mouth, draught, and fresh water complete bodily replenishment.
- Active motifs: night approach to the watering place `quranic:root_001212:B008/m01`; drinking to fullness `quranic:root_000286:B006/m01`; returning a thirsty camel to the trough `quranic:root_000464:B007/m01`; vigorous eating and drinking by mouth `quranic:root_001190:B006/m01`; fresh palatable water `quranic:root_000994:B001/m01`; measured draught `quranic:root_001533:B006/m01`; water sufficient to sustain life `quranic:root_001533:B008/m01`
- Ayah anchors: 61:13 `قَرِيبٌ` (ق ر ب); 61:4 and 61:13 forms of `ح ب ب`; 61:12 `يُدْخِلْ` (د خ ل); 61:8 `أَفْوَٰهِ` (ف و ه); 61:10 `عَذَابٍ` (ع ذ ب); 61:11 `أَنفُسِ` (ن ف س)
- Synthesis: Watering is a timed route with a physiological endpoint. Approach, re-entry, mouth, individual draught, and fullness form a complete replenishment cycle. The life-sustaining water gives “selves” in 61:11 a concrete dependency even as those selves are offered in exertion.

#### Subchannel C. Controlled Gait and Load-Bearing Mount
- Reading type: latent/lexical
- Scene or process: Bit, easy gait, coordinated forelegs, matched hoof placement, and a prepared back convert animal motion into reliable transport.
- Active motifs: bit that restrains the mount `quranic:root_000348:B006/m01`; smooth and easy gait `quranic:root_000563:B003/m01`; forelegs cycling back in travel `quranic:root_000009:B009/m01`; hind hooves matching forehoof placement `quranic:root_000347:B014/m01`; measured horse gait below full gallop `quranic:root_001212:B014/m01`; mount prepared to bear a load `quranic:root_000970:B005/m01`; rapid sure-footed travel `quranic:root_001476:B002/m01`
- Ayah anchors: 61:1 `حَكِيمُ` (ح ك م); 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:6 `يَأْتِى` (ء ت ي); 61:9 `حَقِّ` (ح ق ق) and `يُظْهِرَ` (ظ ه ر); 61:13 `قَرِيبٌ` (ق ر ب); 61:10 `تُنجِي` (ن ج و)
- Synthesis: Reliable movement is produced by controlled degrees rather than maximum speed. The bit bounds motion, the gait smooths it, coordinated limbs conserve direction, and the back carries the mission's load. This latent mounted procession materializes disciplined striving along the path.

### 11. Material Work and Functional Form
- Semantic invariant: Raw material becomes useful through cutting, stripping, tanning, weaving, joining, tensioning, and rotation.
- Surface relation: indirect; the compact building of 61:4, mouths and light in 61:8, and rivers and dwellings in 61:12 provide the surface anchors for these craft mechanisms.
- Surprising reach: Semantic integrity is repeatedly expressed as workmanship: a truthful surface matches its substrate, a finished weave closes a lack, and a water-lift works only when container, handle, and axle cooperate.

#### Subchannel A. Hide Stripped, Tanned, and Sewn
- Reading type: latent/lexical
- Scene or process: Skin is removed from a body, scraped clean, treated with bark, cut for repair, and made into finished leather.
- Active motifs: removing the outer skin `quranic:root_000120:B004/m01`; flaying and scraping a hide `quranic:root_001476:B003/m01`; tanning bark `quranic:root_000737:B008/m02`; cutting and sewing leather for repair `quranic:root_001150:B001/m01`; measured dose of tanning material `quranic:root_001533:B007/m01`; prepared hide `quranic:root_000369:B004/m01`; leather garment `quranic:root_000666:B007/m01`
- Ayah anchors: 61:6 and 61:13 forms of `ب ش ر`; 61:10 `تُنجِي` (ن ج و); 61:7 `إِسْلَٰمِ` (س ل م) and `ٱفْتَرَىٰ` (ف ر ي); 61:11 `أَنفُسِ` (ن ف س); 61:14 forms of `حَوَارِيُّونَ` (ح و ر); 61:1 `سَبَّحَ` (س ب ح)
- Synthesis: The leather scene is a strict transformation chain: separation, scraping, chemical treatment, measured repetition, cutting, and joining. Each operation changes the material's role, turning vulnerable skin into a durable covering. It offers a concrete analogue for disciplined remaking rather than cosmetic change.

#### Subchannel B. Finished Weave and Truthful Surface
- Reading type: latent/lexical
- Scene or process: A missing section is supplied, fibers are tightened, surface nap or cover is raised, and the finished exterior is tested for whether it truthfully represents the material beneath.
- Active motifs: piece supplied to complete a weave `quranic:root_000188:B007/m01`; tightly woven fabric `quranic:root_000347:B010/m01`; raised nap covering a surface `quranic:root_001096:B003/m01`; thin sewn cover `quranic:root_001315:B006/m01`; deceptive patterned cloth `quranic:root_001290:B009/m01`; completion joining exterior and interior excellence `quranic:root_000120:B008/m01`; layered matching fabrics or armor `quranic:root_000970:B020/m01`
- Ayah anchors: 61:8 `مُتِمُّ` (ت م م); 61:9 `حَقِّ` (ح ق ق), `كُلِّ` (ك ل ل), and `يُظْهِرَ` (ظ ه ر); 61:12 `يَغْفِرْ` (غ ف ر); 61:6 and 61:13 forms of `ب ش ر`; 61:7 `كَذِبَ` (ك ذ ب)
- Synthesis: Completion closes a structural lack, while tight weave makes the whole resistant to separation. Yet a patterned surface can still misrepresent its substrate. The craft scene therefore distinguishes real integrity, where inside and outside are jointly finished, from decorative falsehood.

#### Subchannel C. Pulley, Handle, and Water Container
- Reading type: latent/lexical
- Scene or process: A rotating axle and crank operate a standing device that raises a handled bucket, transfers its full contents, and stores water in a repaired skin vessel.
- Active motifs: rotating pulley axle `quranic:root_000369:B007/m01`; crank and rotating iron pin `quranic:root_000610:B006/m01`; upright pulley component `quranic:root_001273:B012/m01`; single-handled drawing bucket `quranic:root_000737:B011/m01`; full water bucket `quranic:root_000521:B007/m01`; waterskin `quranic:root_001212:B009/m01`; patch enlarging a bucket or skin vessel `quranic:root_000992:B004/m01`
- Ayah anchors: 61:14 forms of `حَوَارِيُّونَ` (ح و ر); 61:8 `يُرِيدُ` (ر و د); 61:5 and 61:7 forms of `قَوْم` (ق و م); 61:7 `إِسْلَٰمِ` (س ل م); 61:12 `ذُنُوبَ` (ذ ن ب); 61:13 `قَرِيبٌ` (ق ر ب); surface anchor unavailable for ع د ن
- Synthesis: The device is a cross-root mechanism with distinct components and operations. Rotation at the axle becomes leverage at the handle, lift at the bucket, and transfer into storage; the repair patch increases capacity rather than merely covering damage. This is a compact model of coordinated parts producing flow.

### 12. Attraction, Aversion, and Relief
- Semantic invariant: Bodies and selves orient toward what settles and delights them, recoil from what harms them, and register relief as an opening of constriction.
- Surface relation: direct; love, severe disgust, aversion, painful punishment, and glad tidings appear across 61:3-4, 61:8-10, and 61:13.
- Surprising reach: Emotional change is bodily and spatial: trust becomes stillness, disgust creates distance, distress constricts breath, and good news visibly opens the skin and face.

#### Subchannel A. Affection Settling Into Trust
- Reading type: mixed
- Scene or process: Love draws the self toward an object, trust removes fear, familiarity allows relaxation, and the beloved becomes a place of inward rest.
- Active motifs: abiding love `quranic:root_000286:B002/m01`; security and trusted calm `quranic:root_000054:B001/m01`; familiarity and ease with another `quranic:root_000563:B007/m01`; beloved object in which the self rests `quranic:root_000726:B004/m01`; willing contentment `quranic:root_000961:B006/m01`; truthful friendship and counsel `quranic:root_000852:B005/m01`
- Ayah anchors: 61:4 and 61:13 forms of `ح ب ب`; 61:2, 61:10-11, and 61:13-14 forms of `ء م ن`; 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:12 `مَسَٰكِنَ` (س ك ن) and `طَيِّبَةً` (ط ي ب); 61:6 `مُّصَدِّقًا` (ص د ق)
- Synthesis: Love is not momentary appetite but a force that ends defensive motion. Trust quiets fear, familiarity permits openness, and the beloved supplies rest. This gives the love of disciplined fighters in 61:4 and the desired victory of 61:13 a shared orientation toward dependable good.

#### Subchannel B. Harm Producing Aversion and Abhorrence
- Reading type: mixed
- Scene or process: Injury or ugliness provokes recoil, sustained burden creates unwillingness, and repeated offense intensifies into severe abhorrence.
- Active motifs: natural, rational, or moral repugnance `quranic:root_001295:B001/m01`; hardship borne unwillingly `quranic:root_001295:B002/m01`; severe hatred of ugly conduct `quranic:root_001436:B001/m01`; harmful offense by deed or speech `quranic:root_000023:B001/m01`; felt bodily pain `quranic:root_000046:B001/m01`
- Ayah anchors: 61:8-9 `كَرِهَ` (ك ر ه); 61:3 `مَقْتًا` (م ق ت); 61:5 `تُؤْذُ` (ء ذ ي); 61:10 `أَلِيمٍ` (ء ل م)
- Synthesis: The scene grades negative response from hurt, through reluctant endurance, to moral revulsion. The severe disgust of 61:3 is therefore not interchangeable with the opponents' aversion in 61:8-9: one judges corrupt action, while the other resists an unwelcome truth.

#### Subchannel C. Breath, Lifeblood, and Release
- Reading type: latent/lexical
- Scene or process: Breath and blood sustain life; distress constricts that system, while relief opens space and lets the self breathe again.
- Active motifs: breath leaving the body `quranic:root_001533:B001/m01`; release of constriction `quranic:root_001533:B002/m01`; flowing blood as support of life `quranic:root_001533:B004/m01`; water sustaining the self `quranic:root_001533:B008/m01`; living soul `quranic:root_001533:B011/m01`; lung `quranic:root_000682:B001/m01`; opening that removes distress `quranic:root_001124:B008/m02`
- Ayah anchors: 61:11 `أَنفُسِ` (ن ف س); 61:6 `سِحْرٌ` (س ح ر); 61:13 `فَتْحٌ` (ف ت ح)
- Synthesis: The self is rendered as a life system requiring air, blood, water, and interior space. Relief is therefore an opening operation, not merely a changed opinion. The near opening of 61:13 can resonate as the first full breath after sustained constriction.

#### Subchannel D. Glad Tidings Opening the Countenance
- Reading type: mixed
- Scene or process: News arrives before its promised event, releases distress, and visibly changes skin and face into an open, bright expression.
- Active motifs: glad news that opens the skin with joy `quranic:root_000120:B005/m01`; open and pleasant countenance `quranic:root_000120:B006/m01`; anticipatory first signs `quranic:root_000120:B007/m01`; relief from constriction `quranic:root_001533:B002/m01`; opening that dispels distress `quranic:root_001124:B008/m02`
- Ayah anchors: 61:6 `مُبَشِّرًا` and 61:13 `بَشِّرِ` (ب ش ر); 61:11 `أَنفُسِ` (ن ف س); 61:13 `فَتْحٌ` (ف ت ح)
- Synthesis: Good news is temporally prior but bodily effective in the present. It supplies first signs of what is coming, loosens constriction, and makes joy visible on the face. The command to announce victory in 61:13 thus begins materializing the promised outcome before its arrival.

### 13. Glorification as Answered Alignment
- Semantic invariant: What proceeds from God is rightly answered when voice, posture, obedience, gratitude, and created motion align toward their source.
- Surface relation: direct; 61:1 places glorification in the heavens and earth, while 61:8-9 contrast denial with God's completed light and true religion.
- Surprising reach: Praise is not confined to words: it can stand upright in worship, acknowledge a gift instead of covering it, and move through the cosmos as continuous running.

#### Subchannel A. Praise Enacted as Obedience
- Reading type: surface-primary
- Scene or process: A worshipper stands, directs devotion to its proper object, declares that object free of defect, and turns praise into prayer, thanksgiving, and obedient conduct.
- Active motifs: devotional worship `quranic:root_000047:B001/m01`; object of worship `quranic:root_000047:B001/m02`; glorification as worship, prayer, and thanksgiving `quranic:root_000666:B001/m01`; declaring God transcendent and free of defect `quranic:root_000666:B002/m01`; obedience and religious submission `quranic:root_000504:B001/m01`; standing in prayer or remembrance `quranic:root_001273:B002/m01`
- Ayah anchors: 61:1, 61:3-8, 61:11, and 61:13-14 forms of `ء ل ه`; 61:1 `سَبَّحَ` (س ب ح); 61:9 forms of `دِين` (د ي ن); 61:5 and 61:7 forms of `قَوْم` (ق و م)
- Synthesis: The opening glorification is given bodily and social form. The worshipper's stance supports vocal praise, transcendence fixes its object, and obedience carries the act beyond utterance. This makes the surah's criticism of words without deeds applicable even to praise: glorification reaches completion when conduct assumes its direction.

#### Subchannel B. Gift Acknowledged or Covered
- Reading type: mixed
- Scene or process: A benefit is presented as an unearned favor; the recipient either answers it with thanksgiving or covers the favor by refusing acknowledgment.
- Active motifs: blessings and favors `quranic:root_000076:B006/m01`; gratuitous grant `quranic:root_000076:B012/m01`; giving and presentation `quranic:root_000009:B002/m01`; thanksgiving within glorification `quranic:root_000666:B001/m01`; denial that covers a blessing `quranic:root_001307:B004/m01`
- Ayah anchors: 61:6 `يَأْتِى` (ء ت ي); 61:1 `سَبَّحَ` (س ب ح); 61:8 `كَٰفِرُونَ` and 61:14 `كَفَرَت` (ك ف ر); surface anchor unavailable for ء ل ي
- Synthesis: Gratitude and denial are opposite responses to the same transfer. Presentation places the favor within reach, thanksgiving makes its source visible, and ingratitude hides precisely what has been received. The attempt to extinguish God's light in 61:8 can therefore resonate as covering a benefit whose presence has already been disclosed.

#### Subchannel C. Creation Released Into Its Courses
- Reading type: latent/lexical
- Scene or process: The heavens arch above the earth while celestial and created bodies are released into sustained swimming, running, and flowing through their appointed field.
- Active motifs: earth lying below the heavens `quranic:root_000025:B001/m01`; overhead heavens `quranic:root_000745:B004/m01`; swimming and celestial running `quranic:root_000666:B004/m01`; dispatch and release into motion `quranic:root_000563:B001/m01`; continuous running and flow `quranic:root_000240:B001/m01`
- Ayah anchors: 61:1 `أَرْضِ` (ء ر ض), `سَّمَٰوَٰتِ` (س م و), and `سَبَّحَ` (س ب ح); 61:5, 61:6, 61:9, and 61:11 forms of `ر س ل`; 61:12 `تَجْرِى` (ج ر ي)
- Synthesis: The lexical movement from glorifying to swimming gives cosmic praise a kinematic form. Sky and earth establish the field, release initiates motion, and running sustains it without stasis. Messenger and river imagery then enter the same ordered circulation: revelation is dispatched and promised water flows within a creation already moving in praise.

## Standalone Subchannels

### S1. Wound That Suppurates and Relapses
- Reading type: latent/lexical
- Scene or process: A hidden lesion gathers pus, breaks into visible corruption, appears to improve, then returns in a worse state and requires removal of waste.
- Active motifs: ulcer corrupted by pus `quranic:root_000025:B011/m01`; pus gathered in a wound `quranic:root_000281:B006/m01`; accumulated wound discharge `quranic:root_000282:B003/m01`; wound relapsing after improvement `quranic:root_001096:B004/m01`; concealed internal corruption `quranic:root_000464:B004/m01`; removal of bodily waste `quranic:root_001476:B006/m01`
- Ayah anchors: 61:1 `أَرْضِ` (ء ر ض); 61:6 `جَآءَ` (ج ي ء); 61:12 `يَغْفِرْ` (غ ف ر) and `يُدْخِلْ` (د خ ل); 61:10 `تُنجِي` (ن ج و)
- Synthesis: The scene distinguishes surface improvement from cured structure. Corruption can collect inwardly, announce itself through discharge, and relapse after seeming recovery. It usefully pressures the surah's concern with speech that appears sound while action leaves an internal disorder untreated.

### S2. Hunter, Trap, and Sequential Quarry
- Reading type: latent/lexical
- Scene or process: A hunter goes out, installs a connected snare, uses a means of access or flushing, and takes quarry in sequence as animals run, stop, or emerge from cover.
- Active motifs: departure for the hunt `quranic:root_000745:B006/m01`; hunter's snare `quranic:root_000791:B006/m01`; driving an animal from its burrow `quranic:root_000452:B006/m01`; trained falcon `quranic:root_001040:B006/m01`; small bird entering thickets and caves `quranic:root_000464:B009/m01`; successive taking of quarry `quranic:root_000993:B008/m01`; wild animal running and stopping to look back `quranic:root_001290:B007/m01`
- Ayah anchors: 61:1 `سَّمَٰوَٰتِ` and 61:6 `ٱسْمُ` (س م و); 61:9 `مُشْرِكُونَ` (ش ر ك); 61:11 `خَيْرٌ` and `تَعْلَمُ` (خ ي ر, ع ل م); 61:12 `يُدْخِلْ` (د خ ل); 61:14 `عَدُوِّ` (ع د و); 61:7 `كَذِبَ` (ك ذ ب)
- Synthesis: This is a complete pursuit mechanism rather than a generic animal cluster. Departure, access, concealment, trained falcon, snare, and sequential capture occupy distinct roles. Its unexpected pressure lies in the contrast between a disclosed saving route and a route engineered to entangle the one who follows it.


